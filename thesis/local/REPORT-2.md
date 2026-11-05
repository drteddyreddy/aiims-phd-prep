# Report 2: second local pass (5 Nov 2026)

Brief: `thesis/HANDOVER.md` §6, Priority 1 (evidence gaps). Rows are in `02-verification-table.md` under "Pass 2 additions" (rows 18–27). Scripts: `scripts/extract_rows.py` (OpenRouter `anthropic/claude-haiku-5.5`, verbatim quotes, string-match check) and `scripts/render_rows.py`. Source texts and raw JSON stay in `~/thesis-papers/pass2/` and `~/thesis-papers/extract/` (not committed). Quote check: **300 of 303 matched**. Cost: about $0.32 of OpenRouter credit ($4.38 left).

## 1. What was done, and what was not

| Task (HANDOVER §6) | Status |
|---|---|
| 1. Kinney 2026, PMID 41214823 | **Done, with a correction.** The PMID is the *Trials* 2025 **protocol** (PMC12604150), not a results paper. NCT04154111 completed Feb 2026 with 147 enrolled; no results on ClinicalTrials.gov and no outcome paper in Europe PMC. Protocol extracted (row 18). Searching for it turned up the paper that actually matters: **Hou et al. 2026** (row 19). Verdict in §4 below; `02-lane1` §§1.2, 1.3, 2, 3 and 4 edited. |
| 2. Harel 2022 | Done, full text (row 24). |
| 2. Treiber 2025 | Done, full text via the journal site in the browser (row 25). Included studies in §2. |
| 2. Wang H 2025 | **Partial.** The journal page gives only the abstract; its PDF and HTML buttons are script links. Tag moves from SEC to AB (row 26). %RMT and pulses still NR. Try the AIIMS library or CNKI. |
| 2. Durazzo (Jiang ref 25) | Done. It is Durazzo et al. 2025 *Drug Alcohol Depend* (full text, row 20); the craving paper on the same sample (*JSAD* 2026, abstract, row 21); the pilot (Padula 2024, abstract, row 22); an imaging sub-study (row 23). |
| 2. medRxiv living-review supplement | **Not attempted** this pass. Needs a browser session; the supplement is probably a file download, which needs Dr. Reddy's go-ahead. |
| 3. CTRI/2023/12/060572 | **Not done.** CTRI's search form needs a CAPTCHA that only a person can enter; the WHO ICTRP mirror timed out. Dr. Reddy to look it up by hand (2 minutes). |
| 4. PubMed hit counts | **Not done.** NCBI esearch still returns HTTP 500 (six retries, 5 Nov 2026). Rerun the script later. |
| 4. PROSPERO | **Done**, searched directly on crd.york.ac.uk. Results in §3. |

## 2. Treiber 2025: the 12 included RCTs (from its Table 1)

| Study | n | Technique, target | Sessions | Intensity (MT%) |
|---|---|---|---|---|
| Mishra 2010 | 45 | HF-rTMS, right DLPFC | 10 | 110 |
| Ceccanti 2015 | 18 | dTMS, mPFC | 10 | 120 |
| Addolorato 2017 | 11 | HF-rTMS, bilateral DLPFC | 12 | 100 |
| Raikwar 2020 | 60 | HF-rTMS, left DLPFC | 10 | 120 |
| Perini 2020 | 45 | dTMS, insula | 15 | 120 |
| Zhang 2022 | 48 | HF-rTMS, left DLPFC | 10 | 80–110 |
| Harel 2022 | 46 | dTMS, mPFC | 15 | 100 |
| Belgers 2022 | 32 | HF-rTMS, right DLPFC | 10 | 110 |
| McCalley 2023 | 50 | cTBS, mPFC | 10 | 110 |
| Hoven 2023 | 80 | HF-rTMS, right DLPFC | 10 | 110 |
| Selim 2023 | 38 | dTMS, left DLPFC | 20 | < 66 |
| Padula 2024 | 17 | iTBS, left DLPFC | 20 | 100–110 |

Two of the 12 are Indian (Mishra 2010, Raikwar 2020). Only one is iTBS (Padula, n = 17). Treiber's text says three TBS studies but cites two.

## 3. PROSPERO, searched 5 Nov 2026

| Topic | Query | Result |
|---|---|---|
| Allen Carr in any substance | "Allen Carr" OR Easyway OR "easy way" | 14 hits, **none about Allen Carr** ("easy way" matches stray text). Unregistered. |
| Expectancy challenge in clinical AUD | "expectancy challenge" OR "alcohol expectancy/expectancies" | 7 hits. The only intervention review is CRD42024583840 (expectancy challenge for **college binge drinking**). Clinical AUD is unregistered. |
| Belief-targeting interventions across substances | Title-restricted: (belief* OR expectanc* OR myth* OR misconception* OR "permission giving" OR "positive outcome") AND (addiction OR smoking OR alcohol* OR substance* OR tobacco OR drinking OR quit*) | 10 hits, all on attitudes/beliefs as **exposures** (youth, health workers, tobacco control) or on college expectancy challenge. **No review of interventions that target addiction beliefs.** Unregistered. |
| Lane 1 timing review | alcohol* AND (detox* OR withdrawal OR inpatient*) AND (NIBS terms) | 53 hits. None on timing relative to detox, but at least eight AUD neuromodulation reviews registered 2025–26 (listed in `02-lane1` §5). Crowded. |

Lane 2's review is open on all three framings. The Lane 1 timing review is open by title but sits in a crowded space.

## 4. Verdict on Lane 1's premise and the d = 0.6 assumption

The Wake Forest trial does not threaten Lane 1: its PMID is a protocol, its results are unpublished, and it tests a different question (MPFC vs DLPFC in non-abstinent outpatients). **Hou et al. 2026 is the paper that changes the premise.** It is a sham-controlled trial of accelerated left-DLPFC iTBS (5 sessions a day for 10 weekdays) in detoxified male AUD inpatients with 6-month follow-up, which is most of Lane 1's Question 1. Its craving primary was not significant (p = 0.074, about 20 per arm), although abstinence duration favoured accelerated iTBS. The Durazzo trial (accelerated, 2–3 sessions a day, residential, n = 44) found no craving difference against sham, while heavy drinking days fell. Treiber's pooled left-DLPFC craving effect is SMD −0.27 with a CI crossing zero. So the premise survives only in narrower form: what is still new is **starting inside the detox admission, at adequate power, with a proper sham coil and a hard relapse outcome, in India**. Acceleration and the inpatient setting are no longer new. **The d = 0.6 planning value does not survive.** A defensible value is d = 0.45 (Harel 0.48, Joshi 0.45), which needs N ≈ 148 with baseline adjustment and 20% attrition, or N ≈ 196 without adjustment. That is about 25 months of recruitment at 6 per month. This strengthens the existing recommendation (Lane 2 primary, Lane 1 a small pilot), and it makes Joshi-style tDCS (Question 4) relatively more attractive. Dr. Reddy has not chosen a lane; this is evidence for that choice, not the choice.

## 5. Other findings

- **Harel 2022** at full text: the ± values are SEM, not SD; d = 0.50 for heavy drinking days; abstinent 5–30 days before session 1; stopped early at 62 of 84.
- **Treiber 2025** has an internal error: its 3-month SMD −0.44 is given with CI −0.77 to 0.11 but P < 0.01. The pack's earlier line "every subgroup CI crosses zero" was wrong for mPFC in the Results (−4.34 to −0.09) but right in the Abstract (−4.34 to 0.09).
- **Durazzo 2025**: stimulation intensity is in **active** motor threshold (100–110% aMT), not resting; residential stay 28–35 days; one direction error in the paper (Project MATCH odds).
- **Bickart 2026 (*Int Rev Psychiatry*)** is linked to NCT04154111 by Europe PMC but describes cTBS to the frontal pole in 17 people, which fits the MUSC trial. Do not cite it as the Wake Forest result.

## 6. Changes the cloud session should make

- `README.md` bottom line #3: replace "must be checked against the unread 147-person Wake Forest theta-burst RCT (Kinney 2026)" with: Hou 2026 has already tested accelerated left-DLPFC iTBS against sham in detoxified inpatients (craving primary NS; abstinence duration better), and the Wake Forest PMID is a protocol with no results. Lane 1's novelty is now timing, power and outcome hardness.
- `README.md` 14-day checklist: tick the "full texts" item except Wang H; keep the CTRI item (CAPTCHA, by hand); add "rerun the PubMed script".
- `01-context-and-constraints.md` open question E: mark Harel, Treiber, Kinney and Durazzo done; only Wang H remains. Question D (CTRI): note the CAPTCHA.
- `04-decision-and-integration.md` comparison table, Novelty row, Lane 1 cell: replace "one 147-person trial (Kinney 2026) just completed and unread … Within-day accelerated dosing timed to detox is new" with "three small sham-controlled iTBS RCTs in AUD (Durazzo, Hou, Zhao), one with accelerated dosing in detoxified inpatients; the Wake Forest trial has no results. New: start point inside the detox admission, adequate power, hard relapse outcome, India".
- `04` decision rule (4): replace "Kinney 2026 does not remove the premise" with "the trial can be framed as the definitive step after Hou 2026 and recruitment supports N ≈ 148".
- `04` Gantt Y1 Q1–Q2 Lane 1 cell: replace "read Kinney 2026" with "read Hou 2026 and Durazzo 2025; re-check NCT04154111 results".
- `04` feasibility/effort rows if they quote N = 110 for Lane 1: change to N ≈ 148 (d = 0.45, baseline-adjusted) and say why.
- `03-lane2` review section (if it states the PROSPERO status as unverified): record that PROSPERO was searched on 5 Nov 2026 and all three Lane 2 framings are unregistered; the nearest record is CRD42024583840 (expectancy challenge, college binge drinking).
- `05-protocol-skeleton-aiims.md`: if section D seeds Lane 1's sample size, change d = 0.6 / N = 110 to d = 0.45 / N ≈ 148.
- `06-sources.md`: already updated locally (Kinney, Hou, Durazzo ×4, Bickart, tags for Harel, Treiber, Wang H).
- `02-lane1`: already updated locally (§§1.1, 1.2, 1.3, 1.4, 2, 3, 4 sample size and risk register, 5 PROSPERO, 6 reading list). Check the edits read well in context.

## 7. Priority 2 drafts (same day, HANDOVER §6 tasks 5, 6, 8)

Drafted in `thesis/drafts/`, all v0.1 and not yet reviewed by the guide:
- `review-lane2-prospero.md`: PROSPERO registration draft for the Lane 2 review (belief-targeting interventions across substances): question, sources, a PubMed strategy with proximity terms and a known-item test set (**not yet run**: NCBI esearch down), eligibility, RoB 2 / ROBINS-I, GRADE, synthesis plan, subgroups, declared conflict of interest. Open decision: all substances vs clinical populations only.
- `qual-expectancy-protocol.md`: Phase 1a qualitative study in ICMR Common Forms order: 20–25 inpatients, 10 family members, 8 staff; information power; framework analysis; topic guides; interviewer not on the participant's treating team; CBD-trial participants excluded until the PI rules on co-enrolment; English patient PIS draft; 9 PIS/ICF documents needed.
- `scale-translation-plan.md`: 20 instruments tiered by need; permissions and existing versions **marked unverified** except the Hindi OCDS (Joshi 2025); Beaton/ISPOR method; local standard-drink card; psychometrics (n ≥ 100 per language for PACS, CEOA, DTQ, AASE); unsent draft email to the Joshi group.
- Task 7 (DC synopsis) not done: it waits for the lane choice.

Changes the cloud session should make: `README.md` checklist, tick "PROSPERO draft", "qualitative protocol" and "translation plan" as drafted; `03` §8, link the translation plan from the OCDS/PACS row; `05` §B, link the translation plan from the "validated questionnaires" bullet.
