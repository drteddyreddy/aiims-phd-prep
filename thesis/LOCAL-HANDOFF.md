# Handoff brief for the local Claude Code session (Dr. Reddy's laptop)

**Who you are working for:** Dr. Gowtham H R ("Dr. Reddy"), PhD scholar, Department of Psychiatry, AIIMS Guwahati, and Project Research Scientist on an ICMR Phase III trial of cannabidiol in inpatient alcohol detoxification.

**Who wrote this:** a cloud Claude Code session that cannot reach the laptop or most journal and registry websites. It has already produced a thesis prep pack in this repository under `thesis/` (seven files; read `thesis/README.md` first, then skim the rest). Your job is the part that needs local file access, unrestricted web access, and sustained reading. Do not rewrite the existing `thesis/` files. Write everything new under `thesis/local/` in the exact formats given in section 6, commit to the branch named below, and push. The cloud session will pull your output and integrate it.

**Repository:** `https://github.com/drteddyreddy/aiims-phd-prep`, branch `claude/peaceful-newton-6f6tfv`. Clone or pull before starting:

```bash
git clone https://github.com/drteddyreddy/aiims-phd-prep.git && cd aiims-phd-prep && git checkout claude/peaceful-newton-6f6tfv
```

or, if it already exists locally:

```bash
git fetch origin claude/peaceful-newton-6f6tfv && git checkout claude/peaceful-newton-6f6tfv && git pull
```

---

## 0. Hard rules

1. **Confidentiality.** Dr. Reddy's offer letter forbids sharing details of the cannabidiol trial without the PI's approval. Do not copy the trial protocol, CRFs, SOPs, randomisation lists, or any trial document into the repository. You may read them locally and write a *one-paragraph, non-identifying summary of what exists* (document types, not contents) so the cloud session knows what Dr. Reddy can draw on with permission.
2. **No patient data.** If you find spreadsheets, forms, or notes containing patient identifiers or clinical records anywhere on the machine, do not open them further, do not summarise contents, and do not commit them. List the file path only, flagged `PHI — not opened`.
3. **No copyrighted full texts in the repo.** Download papers and books to a local folder outside the repo (suggest `~/thesis-papers/`). Commit your *notes and extracted numbers*, never the PDFs. Add `thesis/local/pdfs/` to `.gitignore` if you stage anything there by mistake.
4. **Mark provenance.** Every number you report gets a source (DOI or URL) and a tag: `FULLTEXT` (you read the paper), `ABSTRACT` (abstract only), `SECONDARY` (review, registry, press release).
5. **Do not fabricate.** If a paper is paywalled and the laptop has no institutional access, say so and record whatever the abstract and supplementary material give.
6. **Commit often**, with plain messages, on the branch above only.

---

## 1. Inventory the "local brain" folder and the laptop (Priority 1, do first)

Dr. Reddy keeps a folder called **"local brain"** (it appears in his Remote Control list; it may sit inside a hidden directory under the home folder). Find it. Also check Downloads, Documents, Desktop, and any Obsidian / Notion export / Zotero / Mendeley library.

Produce `thesis/local/01-local-brain-inventory.md`:

- Directory tree to depth 3 with file counts and sizes per folder.
- For every file plausibly relevant to the thesis, one line: path, type, 1-sentence description, relevance tag (`TMS`, `CBD-trial`, `AllenCarr`, `AUD-general`, `PhD-admin`, `AIIMS-rules`, `measures/scales`, `digital/app`, `personal-notes`, `other`).
- Specifically hunt for: Allen Carr books (any format), any notes Dr. Reddy has written about his own quitting or about an intervention idea, any TMS manuals or machine brochures, the AIIMS Guwahati PhD prospectus or ordinances, IEC forms, Doctoral Committee correspondence, coursework schedules, synopsis templates from the department, prior synopses from other scholars (structure only), scale PDFs (PACS, OCDS, AUQ, SADQ, CIWA-Ar, AEQ, CEOA, AASE, URICA, DTQ), and anything about the department's ANRF technology-for-continuity-of-care project.
- Apply rules 0.1 and 0.2 throughout.

---

## 2. Verify the flagged figures (Priority 1)

`thesis/06-sources.md` marks items **verify**. For each paper below, open the full text (PubMed Central, publisher, Sci-Hub-free routes only: PMC, Europe PMC, author repositories, preprints, ResearchGate requests are fine; institutional login if the laptop has it). Extract into `thesis/local/02-verification-table.md` as one row per paper with columns: *Citation | Design | N | Population and timing after detox | Stimulation or intervention parameters (target, localisation, frequency/TBS pattern, intensity %RMT, pulses/session, sessions, schedule) | Sham method | Primary outcome and instrument | Primary result with effect size and CI | Secondary results | Follow-up | Adverse events | Risk-of-bias notes | Provenance tag.* Then a one-paragraph "what this changes in the cloud pack" note per paper.

Papers, in order of importance:

1. iTBS for SUD meta-analysis, *Front Neurol* 2026;17:1866761. Also list all 9 included RCTs (first author, year, substance, target, protocol, N) as a sub-table.
2. rTMS for alcohol craving meta-analysis, PubMed 39665462. Included studies sub-table as above.
3. Hoven M et al. 2023, *Addiction* 118(1), 10 add-on HF-rTMS sessions in AUD inpatients. Get the relapse and grams-consumed secondary results, benzodiazepine policy, and timing of first session relative to detox.
4. Belgers M et al. 2022, PMC8878126. Exact N, timing after detox, parameters, craving instrument, effect sizes, 1-year outcomes.
5. Harel M et al. 2022, *Biol Psychiatry*, doi 10.1016/j.biopsych.2021.11.020. Confirm %HDD, craving, EtG/other biomarkers, connectivity findings, H7 parameters.
6. Right-DLPFC cTBS pilot in AUD with 12-month relapse HR 0.21, PMC12791151 (published around Jan 2026). Full parameters, blinding, how relapse was defined.
7. TBS in methamphetamine meta-analysis, PubMed 40757793.
8. Living meta-analysis of NIBS protocols in SUD, medRxiv 10.1101/2025.09.21.25335559. Pull the alcohol-specific protocol rankings and any dose-response finding. Check whether a peer-reviewed version has appeared.
9. Rossi S et al. 2021, *Clin Neurophysiol* 132:269–306. Extract verbatim the passages on alcohol, alcohol withdrawal, benzodiazepines, and theta-burst safety limits (pulse counts and intensities considered safe).
10. Ekhtiari H et al. 2019, *Neurosci Biobehav Rev*, consensus on tES/TMS in addiction medicine. Summarise recommendations on target, timing, sham, outcome measures.
11. Keogan S, Li S, Clancy L 2019, *Tobacco Control*. Exact quit rates per arm at 1, 3, 6, 12 months with CIs; verification method; description of the seminar.
12. Frings D et al. 2020, *Addiction*, doi 10.1111/add.14897, plus protocol Wood et al. 2017, *BMJ Open*, doi 10.1136/bmjopen-2017-016867. Primary result with OR and CI; all secondary outcomes; any belief or mechanism measures; description of seminar content; funder role.
13. Systematic review of Allen Carr's method, *Tob Prev Cessat* 2023, doi 10.18332/tpc/172314. Included studies, risk of bias, conclusions, any component description.
14. Herremans SC et al. 2015, accelerated right-DLPFC HF-rTMS fMRI study in recently detoxified AUD, PMC4546410.
15. Indian trials: Mishra BR et al. 2010 (PubMed 20078462); Mishra BR et al. 2015 right vs left; Raikwar et al. left-DLPFC null (PMC8188934); Indian tDCS RCT in severe AUD, *Indian J Psychiatry* Feb 2025 (PMC11964162). Parameters and results for each.
16. Shanghai 2025 left-DLPFC iTBS during alcohol withdrawal, *J Shanghai Jiao Tong Univ (Med Sci)* 45(3):349–356. Parameters and results (translate if needed).
17. Expectancy challenge meta-analysis in college students (g = −0.20 at 1 month) — identify the citation and pull effect sizes at each time point.

---

## 3. Registry and grey-literature searches the cloud could not run (Priority 1)

Write results to `thesis/local/03-registries-and-landscape.md`.

1. **CTRI (ctri.nic.in):** search "theta burst", "transcranial magnetic", "rTMS", "tDCS", "alcohol", "craving", "Allen Carr", "belief", "expectancy", "psychoeducation alcohol", "digital alcohol", "WhatsApp alcohol". For each hit: CTRI number, title, PI and institution, design, N, status, dates. **Identify the registrant of CTRI/2023/12/060572** (accelerated TBS at medial PFC in AUD with depression) and note whether results or a publication exist.
2. **ClinicalTrials.gov:** NCT06060496, NCT03932149, NCT06320366, NCT03470480, NCT05271175, NCT04990375, NCT06959342 — current status, results posted, any publications. Then a fresh search: condition "alcohol use disorder", intervention "theta burst" OR "iTBS" OR "cTBS" OR "accelerated", all statuses, 2020 onward.
3. **PROSPERO:** search for existing or ongoing reviews on (a) theta-burst or NIBS in alcohol use disorder, (b) timing of NIBS relative to detoxification, (c) Allen Carr / Easyway, (d) expectancy challenge interventions in clinical AUD, (e) belief-change or cognitive-restructuring interventions for craving. For each: registration number, title, status, expected completion. This decides whether the two planned reviews in the cloud pack are still free to take.
4. **PubMed** (use E-utilities or the web): run the two draft review search strings below, report the hit counts, and save the top 50 titles per search to `thesis/local/search-exports/` as CSV.
   - Review A: `("theta burst" OR iTBS OR cTBS OR "transcranial magnetic" OR rTMS OR "transcranial direct current" OR tDCS) AND (alcohol OR "substance use" OR addiction OR craving) AND (detox* OR withdrawal OR inpatient) AND (random* OR sham)`
   - Review B: `("Allen Carr" OR Easyway OR "expectancy challenge" OR "counter-attitudinal" OR "cognitive restructuring" OR "belief change" OR "outcome expectanc*") AND (alcohol OR smoking OR nicotine OR "substance use") AND (random* OR trial OR intervention)`
5. **Google Scholar:** "Sharad Philip" psychiatry; "Ramdas Ransing" digital substance use Assam; "Pranjal Dey" psychiatry Guwahati; "Sai Krishna Tikka" transcranial. List their 10 most relevant papers each. Note anything on TMS, digital interventions, or craving. This tells the cloud session which direction the likely guide and co-guides lean.
6. **ANRF / SERB project listing:** find the department's technology-for-continuity-of-care in SUD project (title, PI, duration, platform if described).

---

## 4. AIIMS Guwahati rules and formats (Priority 2)

Write to `thesis/local/04-aiims-rules.md`.

1. Download and read the AIIMS Guwahati PhD prospectus (`https://www.aiimsguwahati.ac.in/uploads/pdfs/PhDprospectus_AIIMSG-R2.pdf`) and the latest PhD advertisement/prospectus (Jul 2026). Extract verbatim: registration period, coursework, Doctoral Committee composition and timing, thesis protocol submission timeline and approval route, progress assessment schedule, publication requirements before submission, any rule about theses nested in funded projects, any statement discouraging clinical trials as PhD topics.
2. Find AIIMS Guwahati's IEC pages: current thesis-protocol format, PIS/ICF templates (languages required), submission calendar, fees, insurance requirements for interventional studies, SAE reporting form. Save links and extract headings.
3. If the local folder contains any departmental synopsis template or a prior scholar's synopsis, extract its section structure (not content).
4. Compare against `thesis/05-protocol-skeleton-aiims.md` and list every mismatch.

---

## 5. Allen Carr source mapping (Priority 2; depends on finding the books)

If the books are available locally or purchasable as e-books: *The Easy Way to Stop Smoking*, *The Easy Way to Control Alcohol* (also published as *Stop Drinking Now*), *Quit Drinking Without Willpower*, and the seminar FAQ pages at allencarr.com.

Write `thesis/local/05-allen-carr-component-map.md`:

- Chapter-by-chapter table: chapter title | core claim in one sentence | instruction given to the reader (if any) | which row of the mapping table in `thesis/03-lane2-belief-reversal-intervention.md` section 2 it corresponds to | a short paraphrase (no quotations longer than 25 words).
- A list of every "illusion" the alcohol book dismantles, in the book's order.
- Every procedural instruction (keep drinking while reading, no cutting down, no substitutes, final drink, etc.) with the book's stated reason.
- Anything the alcohol book says about medication, detox, withdrawal, or medical supervision, quoted briefly, because the cloud pack departs from Carr on exactly these points and needs the original wording.
- What the seminar format is, from official pages: duration, group size, facilitator background, follow-up, money-back terms.

---

## 6. Output format and report-back (mandatory)

Create these files. Keep the names exact.

```
thesis/local/00-REPORT.md                      # 1–2 pages: what you did, what you could not do, top 10 findings that change the cloud pack
thesis/local/01-local-brain-inventory.md
thesis/local/02-verification-table.md
thesis/local/03-registries-and-landscape.md
thesis/local/04-aiims-rules.md
thesis/local/05-allen-carr-component-map.md    # or a note saying the books were not available
thesis/local/06-open-questions.md              # anything you need Dr. Reddy to answer, numbered
thesis/local/search-exports/*.csv
```

`00-REPORT.md` must end with a section titled **"Changes the cloud session should make"**: a bulleted list, each bullet naming the target file and section in `thesis/` and the change, e.g. "`02-lane1-neuromodulation.md` §1.1: Hoven 2023 first session was day X post-detox; update the timing argument."

Then:

```bash
git add thesis/local && git commit -m "Local research pass: verification, registries, AIIMS rules, Allen Carr map" && git push origin claude/peaceful-newton-6f6tfv
```

---

## 7. If time remains (Priority 3)

- Build a Zotero library (or a BibTeX file at `thesis/local/references.bib`) with every item in `thesis/06-sources.md` plus what you found, Vancouver-exportable.
- Download Hindi versions of AUDIT, PHQ-9, GAD-7 and note which craving or expectancy scales have *any* published Indian-language translation (PACS, OCDS, AUQ, AEQ, CEOA, AASE, DTQ, URICA). Write to `thesis/local/07-scales-availability.md`.
- Check whether AIIMS Guwahati or Gauhati University has an institutional repository with PhD theses in psychiatry; note the structure of one recent thesis.
- Find three recent (2022–2026) published PhD- or MD-thesis-derived Indian papers on rTMS in psychiatry and three on psychosocial intervention development in SUD, as models of what a committee here accepts.

---

## 8. Questions you should ask Dr. Reddy directly while running (he is at the machine)

These are in `thesis/01-context-and-constraints.md` section 7. Ask them in one batch and record the answers in `thesis/local/06-open-questions.md` under "Answered":

1. Official guide and co-guides; is the thesis expected to nest inside the cannabidiol trial?
2. TMS machine: make, model, coils, sham coil, EMG, neuronavigation, owning department, bookable hours.
3. Ward throughput: alcohol-detox admissions per month, mean stay, usual benzodiazepine-free day, proportion in the trial.
4. Acceptable relationship to the trial: nested aftercare, parallel cohort, or neither.
5. Patient languages, literacy, smartphone ownership.
6. Psychologist or social worker available to co-deliver.
7. Intramural funding for PhD scholars; budget ceiling.
8. MRI research access.
9. Self-disclosure stance: A, B, or C (see `thesis/03-lane2-belief-reversal-intervention.md` section 9).
