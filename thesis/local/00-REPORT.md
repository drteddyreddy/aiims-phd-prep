# 00 — Local research pass: report

Run on Dr Reddy's laptop, 5 Nov 2026, by a local Claude Code session working from `thesis/LOCAL-HANDOFF.md`. I did not change the cloud pack's files. Everything new is under `thesis/local/`.

## What was done

| Section | Status | How |
|---|---|---|
| 1 Inventory | Done | File-name scan of Desktop, Documents, Downloads, OneDrive, Zotero and `local brain`. Trial and personal files listed by type or path only. → `01` |
| 2 Verification | 20 of 21 sources done | Full text for 13 (PMC/Europe PMC), abstract for 6, web for 2. Rows extracted by `claude-haiku-5.5` via OpenRouter, then every quoted number string-matched to the source: **448/450 matched**. → `02` |
| 3 Registries | Partly done | ClinicalTrials.gov: done via the API. CTRI and PROSPERO: web search only (SECONDARY). Faculty: OpenAlex. ANRF: web search plus local files. **PubMed hit counts not obtained.** → `03`, `search-exports/` |
| 4 AIIMS rules | Done (IEC partly) | Both prospectus PDFs extracted verbatim and string-checked. IEC: local templates (structure only) plus web search. → `04` |
| 5 Allen Carr | Done | Both alcohol books obtained 5 Nov 2026 and mapped (`carr-maps/`); `05` rewritten from them by the cloud session; seminar format from official pages and the trials. → `05` |
| 6 Questions | Done | 3 answered at the machine, 6 still open, 7 new. → `06` |
| 7 Priority 3 | Not done | `references.bib` failed (Crossref BibTeX endpoint returned nothing). No work on scale availability, theses repository or model papers. |

**Could not do:**
- **PubMed search:** NCBI's search backend returned HTTP 500 all session. The strings are scripted; rerun with `python thesis/local/scripts/pubmed_review_searches.py thesis/local`.
- **CTRI:** the site timed out from this laptop.
- **Full texts not reached:** Harel 2022, Treiber 2025, Shanghai 2025, and the medRxiv living review (behind Cloudflare).
- **Free subdel workers:** all 6 dispatches ended without output (web-search keys missing on the laptop). The work was done with scripts and OpenRouter instead, costing about US$1.00 of OpenRouter credit.
- **Cost of this pass:** 15% of the Pro 5-hour window at start; Claude extra usage not used.

## Top 10 findings that change the cloud pack

1. **The PhD seat may be tied to the CBD trial.** The July 2026 advertisement lists Psychiatry **PSY02 as a Category A seat whose project is the CBD Phase III trial**. Dr Reddy reports that the guide (Dr Sharad Philip) sees the thesis as independent. If the seat is PSY02, the formal answer to the pack's "one question that decides everything" may already exist. → `06` Q-A.
2. **Review A, as drafted, is taken.** Five reviews already cover NIBS in AUD:
   - CRD42024567484 (*BMC Psychiatry* 2025, published)
   - CRD42024504362 (network meta-analysis protocol, *PLoS One* 2025)
   - Treiber 2025
   - the *Front Neurol* 2026 iTBS meta-analysis
   - a medRxiv living review of 208 trials

   Only the narrower angle survives: **stimulation timed to inpatient detox, or LMIC settings**. Review B topics (Allen Carr; expectancy challenge in clinical AUD) still look open.
3. **The strongest Indian neuromodulation result is tDCS, not TMS.** In Joshi et al. 2025 (AIIMS multisite, n=149, severe AUD), bilateral DLPFC tDCS twice daily for 5 days cut 3-month relapse from 63.5% to 44% (NNT 6). This schedule fits an inpatient stay and needs no sham coil. Lane 1 has to position itself against it.
4. **Belgers 2022 is overstated in the pack.** It randomised 34 and 30 started treatment; it was single-blind and reported no effect sizes. **At 12 months there was no effect on craving or abstinence.** Its benefit is a 3-month signal.
5. **The iTBS meta-analysis has one alcohol trial (n=44), and it reports abstinence only.** There is no alcohol craving estimate. Lane 1's d = 0.6 assumption leans on methamphetamine trials.
6. **Detox-to-stimulation timing is almost never reported.** Hoven 2023 says only "within 4 months", and the 2026 cTBS pilot doesn't say. Herremans 2015 is the exception: a mean of 17.8 days after the last drink. Hoven also reports **no benzodiazepine policy**. This strengthens the pack's "timing gap" argument.
7. **Rossi 2021 gives no quantified seizure risk for alcohol withdrawal or benzodiazepines.** It judges TBS at 80–100% RMT safe and names alcohol withdrawal as a provoking factor. The Lane 1 draft (90–100% RMT, CIWA-Ar < 8) already fits. Keep it there, and record benzodiazepine dose at every session.
8. **The g = −0.20 figure is misattributed.** It comes from Wang et al. 2026 (*J Am Coll Health*): binge frequency in college students at about 1 month, with no effect at 3–6 months. Scott-Sheldon 2012 reports d+ 0.23–0.28 at about 2 weeks, not maintained beyond 4 weeks. Both are college samples, not dependent patients.
9. **The Allen Carr evidence is thinner than the pack's summary suggests.**
   - Keogan 2019 is positive only under ITT. With complete-case CO-validated analysis, no time point is significant.
   - Frings 2020: OR 1.38 (0.90–2.10). Among people who attended, the NHS service did better at 4 weeks.
   - The 2023 systematic review did not pool its studies.
10. **People to bring in for Lane 1.** Sai Krishna Tikka (AIIMS Bibinagar) runs intensive TBS trials and co-wrote the Indian rTMS guidelines, a fit for external DC member. Pranjal Dey ran a sham-controlled cTBS RCT in opioid use disorder. Philip's and Ransing's work is implementation, telepsychiatry and digital, which fits Lane 2's digital delivery and the ANRF project. That project is confirmed under Dr Philip: ANRF-funded, 3 years, recruiting a Psychology/Social Work JRF.

Also from the AIIMS rules:
- Protocol due to the DC within 3 months of the DC's formation and **no later than 9 months from registration**.
- DC meets every 6 months with a graded report.
- **Publication gate:** 2 papers with IF > 1.5, or 1 with IF > 3.
- Guwahati IEC wants PIS/ICF **and validated questionnaires** in English, Hindi and Assamese.

## Changes the cloud session should make

- `01-context-and-constraints.md` §1/§5: add that the July 2026 advertisement lists the CBD trial as Category A seat PSY02. The "independent vs nested" decision may be fixed by the seat; flag it for confirmation (`local/06` Q-A).
- `01-context-and-constraints.md` §7: mark Q1 (guide = Sharad Philip; thesis independent per guide), Q4 (ask PI) and Q9 (A vs B undecided) as answered.
- `01-context-and-constraints.md`, AIIMS rules section: add the verbatim timeline (DC within 6 months; protocol ≤ 9 months from registration; DC → Dean → IEC), six-monthly graded DC reports, the publication gate (2 × IF > 1.5 or 1 × IF > 3), co-guide from own department, 3–5 year registration.
- `02-lane1-neuromodulation.md` §1.1 table: Belgers row → n = 34 randomised / 30 treated, single-blind, <6 weeks post-detox, effect at 3 months, **no effect at 12 months**. Remove "verify".
- `02-lane1-neuromodulation.md` §1.1: Mishra 2015 → n = 20 (not 22), *J Neuropsychiatry Clin Neurosci* 2015;27(1):e54-9. Mishra 2010 → 2:1 allocation (30 active / 15 sham), entry CIWA-Ar ≤ 10.
- `02-lane1-neuromodulation.md` §1.1: Hoven → eligibility <4 months post-detox, interval not reported, benzodiazepine policy not reported, relapse HR 0.90 (0.55–1.48), grams consumed null.
- `02-lane1-neuromodulation.md` §1.1: Treiber 2025 → add that the 3-month SMD −0.44 has a CI crossing zero (−0.77 to 0.11), so durability is unproven.
- `02-lane1-neuromodulation.md` §1.2 (TBS table): cTBS pilot → 100% RMT, 600 pulses, F4, perpendicular sham, relapse defined loosely by phone, baseline AUDIT imbalance. Shanghai 2025 → citation Wang H et al., doi 10.3969/j.issn.1674-8115.2025.03.012, 10 sessions/2 weeks, VAS craving interaction p = 0.011; %RMT still unknown. iTBS MA → note only one alcohol trial (abstinence only).
- `02-lane1-neuromodulation.md`, Indian/tDCS evidence: give Joshi 2025 (CTRI/2022/03/040823) its own row with relapse 44% vs 63.5%, NNT 6, twice-daily × 5 days, and treat it as the comparator Lane 1 must beat or complement. Consider a tDCS arm or a tDCS-first option given sham-coil uncertainty.
- `02-lane1-neuromodulation.md` gaps item 2: support it with Herremans (17.8 days post last drink) and the non-reporting in Hoven and Zhao.
- `02-lane1-neuromodulation.md` safety section: Rossi gives no quantified risk for withdrawal or benzodiazepines; TBS 80–100% RMT judged safe. Keep the draft at ≤ 100% RMT and add per-session benzodiazepine dose recording.
- `02-lane1-neuromodulation.md` sample size: state that the d = 0.6 craving assumption comes from methamphetamine-dominated pooled data. Consider the Joshi relapse difference as an alternative basis.
- `02-lane1-neuromodulation.md` §1.2: CTRI/2023/12/060572 → registrant still unknown. The only source is an aggregator; needs a manual CTRI check (`local/06` Q-D). Add from ClinicalTrials.gov: NCT04154111 (Wake Forest TBS, n = 147, completed 2026, paper PMID 41214823) and NCT04998916 (MUSC mPFC TBS, recruiting).
- `02-lane1-neuromodulation.md` systematic review (title near line 155): narrow the scope to "NIBS timed to inpatient detoxification" because broad NIBS-in-AUD reviews exist (CRD42024567484, CRD42024504362, Treiber 2025, Front Neurol 2026, medRxiv living review).
- `03-lane2-belief-reversal-intervention.md` §1 evidence table: Keogan → add "significant under ITT only; complete-case CO-validated differences not significant; 101/300 retained at 12 months". Frings → add OR 1.38 (0.90–2.10), Bayes factor 1.24, attenders' 4-week abstinence favoured the NHS service, funded by Allen Carr's Easyway.
- `03-lane2-belief-reversal-intervention.md` §2 mapping table (big-monster row): replace "meta-analysis g = −0.20 at 1 month" with **Wang et al. 2026, J Am Coll Health, doi 10.1080/07448481.2026.2643638** (binge frequency, college students, not sustained at 3–6 months). Add Scott-Sheldon 2012 d+ 0.23–0.28 at ~2 weeks.
- `03-lane2-belief-reversal-intervention.md` §3 departures: cite Carr's hostility to anti-anxiety medication and the framing of withdrawal as trivial (cannabis book Ch 3, 5, 9; `local/05`). Replace with alcohol-book wording once obtained.
- `03-lane2-belief-reversal-intervention.md` §6 or the components section: consider two manualisable Carr components found in the book: a written record of harms carried on the person, and a pre-planned response to future pangs.
- `03-lane2-belief-reversal-intervention.md` systematic review: Allen Carr and expectancy-challenge-in-clinical-AUD topics appear unregistered; register now.
- `05-protocol-skeleton-aiims.md`:
  - rebuild on the Guwahati Section III proforma and ICMR Common Forms 2020 headings
  - add the Research Cell title-approval step, DC → Dean → IEC route, biostatistician sign-off, trilingual validated questionnaires (English/Hindi/Assamese) as a pre-IEC task, and six-monthly DC reports
  - see `local/04` §4 for the full mismatch list
- `04-decision-and-integration.md` Gantt: add DC formation (≤ 6 months), protocol to DC (≤ 9 months from registration), six-monthly DC meetings, and pick target journals against the IF > 1.5 / > 3 gate.
- `06-sources.md`: add verified DOIs and PMC IDs from `local/02`. Remove "verify" flags for Belgers, Treiber, the cTBS pilot, Hoven and Keogan. Mark Ekhtiari as read. Keep "verify" on Harel and Shanghai (abstract only).

### Added after the alcohol-book maps (applied to the cloud pack on 5 Nov 2026)

- `03-lane2-belief-reversal-intervention.md` §2: six new mapping rows (11–16) from the alcohol books: reattribution of past failure; pleasure list and harms card; pre-planned pang responses; immediate re-entry into social situations; quit-now timing; disclosure and non-envy. Expectancy row now cites Scott-Sheldon 2012 and Wang X 2026 with their time courses.
- `03-lane2-belief-reversal-intervention.md` §3: departures table rebuilt with chapter citations from QDWW and EWCA (keep-drinking instruction, withdrawal-is-mild, no medication, ignore-advice, no-substitutes conflict between the books, hypnotherapy, unreferenced claims, vulnerability denial, family, screening).
- `03-lane2-belief-reversal-intervention.md` §1: Keogan and Frings rows now carry the ITT-only caveat, the OR with CI, the attenders' 4-week result, retention, funding, and the absence of belief measures; the 2023 review row notes no pooling.

**All bullets in "Changes the cloud session should make" above were applied on 5 Nov 2026.** Remaining open items are in `06-open-questions.md`.
