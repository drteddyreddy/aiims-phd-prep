# Handoff: redo the Allen Carr map from the alcohol book

**For:** the next session (Fable), on Dr Reddy's laptop.
**Why:** `05-allen-carr-component-map.md` was mapped from *Easy Way to Quit Cannabis* as a proxy, because no alcohol book was on the laptop. Dr Reddy is buying the alcohol book. The cloud pack departs from Carr on detox and medication, so it needs the alcohol book's own wording on those points.

## Before you start

1. Pull the branch: `git fetch origin claude/peaceful-newton-6f6tfv && git checkout claude/peaceful-newton-6f6tfv && git pull`.
2. Read `thesis/local/00-REPORT.md` and `thesis/local/05-allen-carr-component-map.md`. Then read the mapping table in `thesis/03-lane2-belief-reversal-intervention.md` §2 and the departures in §3.
3. Find the book in `C:\Users\reddy\thesis-papers\carr\`. Expected: *Allen Carr's Quit Drinking Without Willpower* (Arcturus), and possibly *The Easy Way to Control Alcohol*. EPUB is preferred.
   - If the folder is empty, or the file is DRM-locked (for example a Kindle file), stop and tell Dr Reddy. **Do not try to remove DRM.**
   - Do not download the book from shadow libraries.

## Hard rules

- **Never commit the book or any extracted book text.** It lives outside the repo, in `~/thesis-papers/carr/`.
- **Paraphrase only.** At most one quote per chapter, each under 20 words, and only where exact wording matters (detox, medication, withdrawal). No quotes in the illusions or instructions lists.
- The book text may go to OpenRouter for analysis. Commit only the paraphrased map.
- Use they/them for Dr Reddy and any third person.

## Steps

1. Run the mapper on each book:

   ```bash
   python thesis/local/scripts/carr_map.py "C:/Users/reddy/thesis-papers/carr/<book>.epub" "C:/Users/reddy/thesis-papers/carr/map_<short>.md"
   ```

   It uses `anthropic/claude-haiku-5.5` on OpenRouter, with the key in `~/.config/jev/openrouter.key`. One book costs about US$0.01–0.02. The OpenRouter balance was about $4.70 on 5 Nov 2026. The free subdel workers failed on this laptop (missing search keys), so don't route this job through them.

2. **Check the output yourself:**
   - The chapter list matches the book's table of contents.
   - No quote is longer than 20 words, and there is no more than one per chapter. Scan for quotation marks.
   - Spot-check three chapter paraphrases against the book.
   - Read the medication/detox section closely. That is the one the protocol depends on.

3. **Rewrite `thesis/local/05-allen-carr-component-map.md`:**
   - Make the alcohol-book map the main content: chapter table, illusions in book order, procedural instructions with the book's stated reasons, and what it says about medication, detox, withdrawal, medical supervision, AA, controlled drinking and substitutes.
   - Keep the seminar-format section as it is.
   - Move the cannabis-book proxy to a short appendix, or drop it. Keep a 3–5 line note on where the two books differ.
   - Add a section: **"Carr vs the Lane 2 protocol"**. List each point where the alcohol book's advice conflicts with safe practice in a dependent, post-detox population. Examples: benzodiazepines, withdrawal seizures, medical supervision of detox, anticraving medication. For each, give the protocol's departure in one line.

4. **Update `thesis/local/00-REPORT.md`.** Edit the section 5 row in the status table, and add bullets under "Changes the cloud session should make" for `03-lane2-belief-reversal-intervention.md` §2 (new or changed mapping rows) and §3 (departures, now citing the alcohol book's chapter numbers). In `06-open-questions.md`, mark question C as answered.

5. **Commit and push to `claude/peaceful-newton-6f6tfv` only:**

   ```bash
   git add thesis/local && git commit -m "Allen Carr alcohol-book component map" && git push origin claude/peaceful-newton-6f6tfv
   ```

   Before committing, run `git status` and confirm that no `.epub`, `.pdf` or book-text file is staged.

## Done when

`05` is built on the alcohol book, `00-REPORT.md` and `06` are updated, nothing from the book beyond short quotes is in the repo, and the branch is pushed.
