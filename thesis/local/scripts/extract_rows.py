"""Extract verification-table rows from paper texts, then string-check every quote.

Usage: python extract_rows.py OUT_DIR TAG file1.txt [file2.txt ...]
  TAG = FULLTEXT | ABSTRACT. Writes OUT_DIR/<stem>.json, prints quote-match counts.
Model: anthropic/claude-haiku-5.5 via OpenRouter; key in ~/.config/jev/openrouter.key.
Source texts stay outside the repo (~/thesis-papers/).
"""
import json, re, sys, time, urllib.request
from pathlib import Path

MODEL = "anthropic/claude-haiku-5.5"
KEY = (Path.home() / ".config/jev/openrouter.key").read_text().strip()
FIELDS = [
    "citation", "design", "n", "population_and_timing_after_detox",
    "parameters", "sham_or_control", "primary_outcome_and_instrument",
    "primary_result_with_effect_size_and_ci", "secondary_results", "follow_up",
    "adverse_events", "risk_of_bias_notes", "full_parameters",
]
PROMPT = """You are extracting data from ONE paper for a PhD evidence table. Use ONLY the text below.
Return a single JSON object with these keys: {fields}.
Each key maps to {{"value": "<concise extraction>", "quotes": ["<verbatim quote from the text>", ...]}}.
Rules:
- Every number in a value must appear in at least one quote, copied character-for-character from the text (short quotes, under 30 words each).
- If the text does not report something, write NR in the value and give no quote. Never infer or calculate unless you label it "derived".
- "parameters": target, localisation method, coil/device, frequency or TBS pattern, intensity (%RMT/%aMT), pulses per session, sessions per day, total sessions, schedule. For non-stimulation studies describe the intervention dose.
- "population_and_timing_after_detox": who, setting, and the interval between detoxification/last drink/benzodiazepines and the first session.
- "full_parameters": value is a semicolon-separated list "Item: detail".
- "risk_of_bias_notes": randomisation, allocation concealment, blinding and blinding checks, attrition, ITT, multiplicity, funding/conflicts.
Output JSON only, no prose.

TEXT ({tag}):
"""


def call(text, tag):
    body = {"model": MODEL, "max_tokens": 12000, "temperature": 0,
            "messages": [{"role": "user", "content": PROMPT.format(fields=", ".join(FIELDS), tag=tag) + text}]}
    req = urllib.request.Request("https://openrouter.ai/api/v1/chat/completions", data=json.dumps(body).encode(),
                                 headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                j = json.loads(r.read())
            out = j["choices"][0]["message"]["content"]
            out = out[out.find("{"): out.rfind("}") + 1]
            return json.loads(out, strict=False), j.get("usage", {})
        except Exception as e:
            print("  retry", attempt, type(e).__name__, str(e)[:120]); time.sleep(5)
    raise RuntimeError("extraction failed")


def norm(s):
    s = s.replace(" ", " ").replace(" ", " ").replace("−", "-").replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", s).strip().lower()


def check(rows, text):
    src = norm(text); ok = bad = 0; misses = []
    for k, v in rows.items():
        for q in (v.get("quotes") or []) if isinstance(v, dict) else []:
            if norm(q) in src: ok += 1
            else: bad += 1; misses.append((k, q))
    return ok, bad, misses


if __name__ == "__main__":
    out_dir, tag, files = Path(sys.argv[1]), sys.argv[2], sys.argv[3:]
    out_dir.mkdir(parents=True, exist_ok=True)
    for f in files:
        f = Path(f); text = f.read_text(encoding="utf-8", errors="replace")
        try:
            rows, usage = call(text, tag)
        except RuntimeError as e:
            print(f"{f.name}: FAILED ({e})"); continue
        ok, bad, misses = check(rows, text)
        rows["_meta"] = {"source": f.name, "tag": tag, "model": MODEL, "quotes_ok": ok, "quotes_missed": bad,
                         "misses": misses, "usage": usage}
        (out_dir / f"{f.stem}.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False), encoding="utf-8")
        print(f"{f.name}: quotes {ok}/{ok + bad} matched; tokens {usage.get('prompt_tokens')}/{usage.get('completion_tokens')}")
