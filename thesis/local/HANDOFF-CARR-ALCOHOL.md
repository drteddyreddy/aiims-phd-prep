# Handoff: rewrite the Allen Carr map from the alcohol books (for the Fable cloud session)

**Status, 5 Nov 2026:** The laptop session has already read both alcohol books and pushed paraphrased chapter maps. You do not need the books; they stay on Dr Reddy's laptop for copyright reasons. Your job is the writing.

## Inputs (all in this branch)

- `thesis/local/carr-maps/easy-way-to-control-alcohol.md`: map of *The Easy Way to Control Alcohol* (27 chapters)
- `thesis/local/carr-maps/quit-drinking-without-willpower.md`: map of *Quit Drinking Without Willpower* (20 chapters, newer edition)

Each map has:
- a chapter table (core claim, reader instruction, mapping row, paraphrase)
- the illusions in book order
- the procedural instructions with the book's stated reasons
- what the book says about medication, detox, withdrawal, medical supervision, AA, controlled drinking and substitutes
- candidate new mapping rows

Mapping-row numbers are the rows of `thesis/03-lane2-belief-reversal-intervention.md` §2, numbered top to bottom (1 = little monster ... 10 = delivered by a former user).

**How the maps were made.** `scripts/carr_map.py` ran on the book text with `claude-haiku-5.5`. They were then checked by script:
- no quote is over 20 words
- one 12-word instruction line is the only verbatim run of 12 or more words

**No human has checked them chapter by chapter.** Treat claims about specific chapters as needing a look if a protocol decision rests on them.

Also read first: `thesis/local/00-REPORT.md`, the current `thesis/local/05-allen-carr-component-map.md` (built from the cannabis book as a proxy), and `thesis/03-lane2-belief-reversal-intervention.md` §2–3.

## Tasks

1. **Rewrite `thesis/local/05-allen-carr-component-map.md`:**
   - Use *Quit Drinking Without Willpower* as the main map, since it is the current edition. Use *The Easy Way to Control Alcohol* where it adds wording, especially on detox and medication.
   - Keep the seminar-format section as it is.
   - Shrink the cannabis-book proxy to a 3–5 line note on how the books differ, or drop it.
   - Add a section **"Carr vs the Lane 2 protocol"**: each point where the alcohol books' advice conflicts with safe care in a dependent, post-detox population (benzodiazepines, withdrawal seizures, medically supervised detox, anticraving medication, controlled drinking). For each, give the protocol's departure in one line, with the book's chapter number.
2. **Update `thesis/local/00-REPORT.md`:**
   - Change the section 5 row from "proxy only" to done.
   - Add bullets under "Changes the cloud session should make" for `03-lane2` §2 (new or changed mapping rows) and §3 (departures now citing the alcohol books' chapters).
3. **In `thesis/local/06-open-questions.md`,** mark question C as answered: both alcohol books obtained 5 Nov 2026.
4. Then make those changes to the cloud pack itself (`03-lane2-belief-reversal-intervention.md` §2–3), as with the other bullets in the report.

## Rules

- Paraphrase. Do not add quotes from the books beyond those already in the maps, and keep any quote under 20 words.
- Use they/them for Dr Reddy and anyone whose pronouns are not stated.
- Commit to `claude/peaceful-newton-6f6tfv` only.
