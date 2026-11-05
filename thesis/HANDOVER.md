# Handover: continue the thesis work on the local machine

Written 05 Nov 2026 at the end of the cloud session. Give this file to Claude Code on Dr. Reddy's laptop. It replaces `LOCAL-HANDOFF.md` as the entry point; that older brief is complete and kept only for history.

## 0. Get the current state

```bash
cd ~/aiims-phd-prep 2>/dev/null || git clone https://github.com/drteddyreddy/aiims-phd-prep.git ~/aiims-phd-prep && cd ~/aiims-phd-prep
```

```bash
git fetch origin claude/peaceful-newton-6f6tfv && git checkout claude/peaceful-newton-6f6tfv && git pull origin claude/peaceful-newton-6f6tfv
```

Latest commit at handover: `Integrate local research pass into thesis pack`. Work on this branch only.

## 1. Who and what

- **Dr. Gowtham H R ("Dr. Reddy")**, PhD scholar, Department of Psychiatry, AIIMS Guwahati (July 2026 session), and Project Research Scientist-I on the ICMR multicentre Phase III RCT of cannabidiol during inpatient alcohol detoxification. **Guide: Dr. Sharad Philip.**
- The thesis has two candidate lanes:
  - **Lane 1:** neuromodulation for craving (accelerated iTBS during the inpatient detox window; tDCS replication as fallback).
  - **Lane 2:** a belief-reversal ("counter-brainwashing") intervention inspired by the Allen Carr method, which is how Dr. Reddy quit after about eight years of dependence. This is private; see rule 2.4.
- **Current recommendation:** Lane 2 as the thesis (development → proof of concept → pilot RCT), Lane 1 as a small sham-controlled pilot in years 2–3. Dr. Reddy has not yet formally chosen.

## 2. Hard rules (carry these forward)

1. **CBD trial confidentiality.** The offer letter forbids sharing trial details without PI approval. Never copy trial protocols, CRFs, SOPs, randomisation lists or participant data into the repo. Refer to the trial only by its public title.
2. **No patient or personal data.** Do not open, summarise or commit files with identifiers. List paths only, flagged `PHI — not opened`.
3. **No copyrighted full texts in the repo.** PDFs and books stay in `~/thesis-papers/` (outside the repo). Commit notes, extracted numbers and paraphrase only; quotations under 20 words.
4. **Personal history is private.** Do not write Dr. Reddy's own addiction history into any repo file beyond what already exists. The disclosure decision (Lane 2 file, section 9) is theirs.
5. **Provenance on every number:** FT (full text read), AB (abstract), SEC (registry/web). Do not fabricate; mark NOT FOUND.
6. **Pronouns:** use they/them for Dr. Reddy and anyone whose pronouns are not stated.
7. Commit often to `claude/peaceful-newton-6f6tfv`. Do not open a pull request unless asked.

## 3. File map

| File | Status | Purpose |
|---|---|---|
| `thesis/README.md` | Current | Eight-line bottom line, file index, 14-day checklist. Read first. |
| `thesis/01-context-and-constraints.md` | Current | Seat question, people, assets, verbatim AIIMS PhD rules, IEC requirements, regulation, open questions. |
| `thesis/02-lane1-neuromodulation.md` | Current, verified | Evidence tables with tags, gaps, five ranked questions, full draft protocol, safety, review scope. |
| `thesis/03-lane2-belief-reversal-intervention.md` | Current, verified | Carr method from both alcohol books, smoking RCTs at full text, 16-row mechanism map, departures table, module architecture, development pathway, measures, disclosure options. |
| `thesis/04-decision-and-integration.md` | Current | Comparison, combination options, decision rules, Gantt pegged to AIIMS deadlines, target journals. |
| `thesis/05-protocol-skeleton-aiims.md` | Current | Route and gates, Guwahati IEC document set, ICMR Common Forms 2020 headings with seeds. |
| `thesis/06-sources.md` | Current | All sources with DOIs/PMCIDs and tags; remaining gaps. |
| `thesis/local/` | Complete | Prior local pass: report, inventory, verification table, registries, AIIMS rules, Allen Carr maps, open questions, scripts, search exports. |
| `thesis/LOCAL-HANDOFF.md` | Done, historical | The first brief. Do not re-run. |

## 4. Decisions already made (do not re-litigate unless Dr. Reddy asks)

- Lane 2 is the recommended primary; Lane 1 secondary.
- Lane 2 departs from Carr on ten points (Lane 2 file, section 3): no drinking during the programme, honest withdrawal education, anti-craving medication retained, no "ignore conflicting advice", soft drinks allowed, no hypnotherapy, no "easy" claims, vulnerability acknowledged, family included, comorbidity screened.
- Lane 1 intensity capped at ≤ 100% RMT; stimulation only after the benzodiazepine taper with per-session dose logging.
- Broad NIBS-in-AUD review is taken; Lane 1 review narrowed to timing relative to detox. Lane 2 review (belief-targeting interventions across substances) looks open.
- Delivery for Lane 2 v1 is WhatsApp, not a custom app; v2 may ride on Dr. Philip's ANRF continuity-of-care platform.

## 5. Open questions (ask Dr. Reddy in one batch, record answers in `thesis/local/06-open-questions.md` under "Answered")

1. **Seat:** is it Category A PSY02? If yes, will the Dean's office accept an independent thesis?
2. **Registration date** (sets the 6-month DC and 9-month protocol deadlines).
3. **Co-guides:** Dr. Ransing for Lane 2? Is Dr. Pranjal Dey in the department? Dr. Sai Krishna Tikka (AIIMS Bibinagar) as external DC member?
4. **TMS machine:** make, model, theta-burst capability, sham coil, EMG, neuronavigation, owning department, bookable hours.
5. **Ward throughput:** alcohol-detox admissions per month, mean stay, usual benzodiazepine-free day, share in the CBD trial.
6. **PI's position** on nested aftercare vs parallel cohort.
7. **Languages, literacy, smartphone ownership** on the ward.
8. **Co-deliverer:** can the ANRF JRF (Psychology/Social Work) help?
9. **Funding:** intramural funds for PhD scholars, budget ceiling.
10. **Target journals** the guide prefers.
11. **IEC Member Secretary** contact.
12. **Self-disclosure:** A or B (recommendation: tell the guide only).
13. **Primary lane choice**, once 1–6 are answered.

## 6. Next tasks, in priority order

### Priority 1 — finish the evidence gaps (needs library access or a browser)
1. **Kinney et al. 2026, PMID 41214823** (Wake Forest TBS RCT, NCT04154111, n = 147). Full-text extraction in the same row format as `thesis/local/02-verification-table.md`. Then write a one-paragraph verdict on whether Lane 1's premise and d = 0.6 assumption survive, and edit `02-lane1` sections 1.2, 3 and 4 accordingly.
2. Full texts of **Harel 2022** (*Biol Psychiatry*), **Treiber 2025** (*J Addict Med*; list its 12 included studies), **Wang H 2025** (*J Shanghai Jiao Tong Univ Med Sci*; %RMT and pulses), **Durazzo** (the alcohol iTBS trial, reference 25 in Jiang 2026), and the **medRxiv living review** supplement (alcohol-specific rankings). Append rows to the verification table; update `02-lane1` and `06-sources`; remove tags that change from AB/SEC to FT.
3. **CTRI/2023/12/060572**: open ctri.nic.in in a browser, record registrant, institution, status, publications. Update `02-lane1` section 1.2.
4. **PubMed hit counts**: rerun `python thesis/local/scripts/pubmed_review_searches.py thesis/local`. **PROSPERO**: confirm on crd.york.ac.uk that the Lane 2 review topics (Allen Carr in any substance; expectancy challenge in clinical AUD; belief-targeting interventions across substances) and the Lane 1 timing review are unregistered.

### Priority 2 — first deliverables (can start before the lane is chosen)
5. **PROSPERO registration draft for the Lane 2 review** at `thesis/drafts/review-lane2-prospero.md`: title, question (PICO), searches (databases + full strings), eligibility, outcomes, risk-of-bias tools (RoB 2, ROBINS-I), synthesis plan. Do the same for the Lane 1 timing review if Dr. Reddy wants both.
6. **Qualitative study protocol** (Lane 2 Phase 1a) at `thesis/drafts/qual-expectancy-protocol.md`, in the ICMR Common Forms structure from `05`: 20–25 detox inpatients, 10 family members, 8 staff; topic guide; framework analysis; trilingual PIS/ICF placeholders. This can go to the IEC early as a standalone study.
7. **Synopsis draft for the Doctoral Committee** at `thesis/drafts/synopsis-dc.md`, using section D of `05`, for whichever lane Dr. Reddy picks.
8. **Questionnaire translation plan** (English/Hindi/Assamese) at `thesis/drafts/scale-translation-plan.md`: which scales, permissions needed, forward/back translation, cognitive interviewing, reliability testing. Contact the Joshi 2025 group for their Hindi OCDS.

### Priority 3 — Lane 2 build (after the lane is chosen)
9. **Facilitator manual v1** at `thesis/drafts/bri-ad-manual-v1.md`: five sessions with scripts, workbook pages, fidelity checklist, built from `03` sections 3 and 5 and the Carr maps in `thesis/local/carr-maps/` (paraphrase only).
10. Video scripts for the six aftercare boosters and the session-opening clips.
11. TIDieR description of the intervention.

## 7. Report-back format for the next cloud session

When a batch of work is done, add or update `thesis/local/REPORT-2.md` with:
- What was done, what could not be done and why.
- Top findings that change the pack.
- A final section **"Changes the cloud session should make"**, one bullet per change naming file and section.

Then:

```bash
git add thesis && git commit -m "Local pass 2: <summary>" && git push origin claude/peaceful-newton-6f6tfv
```

## 8. Tools that worked last time on the laptop

- PMC BioC API and Europe PMC for full texts; PubMed efetch for abstracts (esearch was down); ClinicalTrials.gov API v2 (`thesis/local/scripts/ctgov_search.py`); OpenAlex for faculty bibliometrics.
- Not reachable by script: ctri.nic.in, PROSPERO search, medRxiv full text (Cloudflare), Google Scholar. Use a browser for these.
- Raw extraction JSON from the previous pass is in `~/thesis-papers/extract/`.
