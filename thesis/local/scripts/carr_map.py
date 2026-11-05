"""Map an Allen Carr book onto the Lane 2 mapping rows, paraphrase only.

Usage: python carr_map.py <book.epub|book.txt> <out.md>
Needs an OpenRouter key in ~/.config/jev/openrouter.key (or OPENROUTER_API_KEY).
The book text is sent to OpenRouter; nothing from the book is written to the repo
except the paraphrased map this script returns.
"""
import html, json, os, pathlib, re, sys, urllib.request, zipfile

MODEL = "anthropic/claude-haiku-5.5"
ROWS = ("1 little monster/relief misread as pleasure; 2 pleasure is an illusion/wanting vs liking; "
        "3 big monster/brainwashing/outcome expectancies; 4 fear keeps you using; "
        "5 willpower fails/deprivation causes relapse; 6 nothing to give up/decision with certainty; "
        "7 identity: I am a non-drinker now; 8 keep drinking while you read, then one decision; "
        "9 residual craving as the monster dying/reappraisal; 10 delivered by a former user/peer credibility")
SYS = f"""You analyse an Allen Carr alcohol book for a psychiatry PhD scholar building a research intervention from the method.
COPYRIGHT RULES: paraphrase in your own words; never reproduce passages; at most ONE quote per chapter, never more than 20 words;
no quotes in the illusions or instructions lists. Use only the book text.
Mapping rows (by number): {ROWS}.
Return markdown with these sections:
## Chapter table
| Ch | Title | Core claim (1 sentence, paraphrase) | Instruction to reader (if any) | Mapping row(s) | Short paraphrase (<=40 words) |
## Illusions dismantled, in book order (paraphrased, with chapter)
## Procedural instructions (numbered as in the book if numbered), each with the book's stated reason (paraphrased) and chapter
## What the book says about medication, detox, withdrawal, medical supervision, AA/12-step, controlled drinking, substitutes
(paraphrase; at most one quote <=20 words per point; chapter)
## Components with no mapping row (candidate new rows)"""


def book_text(p):
    p = pathlib.Path(p)
    if p.suffix.lower() != ".epub":
        return p.read_text(encoding="utf-8", errors="replace")
    z = zipfile.ZipFile(p)
    out = []
    for n in sorted(x for x in z.namelist() if x.endswith((".xhtml", ".html", ".htm"))):
        t = z.read(n).decode("utf-8", "replace")
        t = re.sub(r"<(script|style).*?</\1>", "", t, flags=re.S)
        t = re.sub(r"</(p|h1|h2|h3|div|li)>", "\n", t)
        out.append(f"\n=== {n} ===\n" + html.unescape(re.sub(r"<[^>]+>", "", t)))
    return re.sub(r"\n\s*\n+", "\n", "".join(out))


key = os.environ.get("OPENROUTER_API_KEY") or (pathlib.Path.home() / ".config/jev/openrouter.key").read_text().strip()
body = {"model": MODEL, "temperature": 0, "max_tokens": 16000,
        "messages": [{"role": "system", "content": SYS}, {"role": "user", "content": book_text(sys.argv[1])}]}
req = urllib.request.Request("https://openrouter.ai/api/v1/chat/completions", data=json.dumps(body).encode(),
                             headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"})
j = json.loads(urllib.request.urlopen(req, timeout=900).read())
pathlib.Path(sys.argv[2]).write_text(j["choices"][0]["message"]["content"], encoding="utf-8")
print("cost USD", j.get("usage", {}).get("cost"))
