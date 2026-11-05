# PROSPERO registration draft: Lane 2 review

Draft v0.1, 5 Nov 2026. Not yet reviewed by the guide. Field order follows the main sections of the PROSPERO form; check field names and word limits against the live form before pasting. Paper 1 of Lane 2 (`03` §7 Phase 1a, §11).

**Registration status of the topic.** PROSPERO searched directly on 5 Nov 2026 (`local/REPORT-2.md` §3): no registered review of Allen Carr-type interventions in any substance, none of expectancy challenge in clinical AUD, and none of interventions that target addiction-related beliefs across substances. Nearest record: CRD42024583840 (expectancy challenge for college binge drinking). Published neighbours to cite and position against: Scott-Sheldon et al. 2012 (expectancy challenge, college students), Wang X et al. 2026 *J Am Coll Health* (expectancy challenge, 8 RCTs, college), and the 2023 *Tob Prev Cessat* review of Allen Carr for smoking (6 studies, no pooling, not registered). Re-check PROSPERO and OSF the week you submit.

---

## 1. Review title

Interventions that target beliefs about the benefits of substance use and the difficulty of stopping: a systematic review and meta-analysis across alcohol, tobacco and other drugs.

Short title for the paper: *Changing what people believe a drug gives them: a systematic review of belief-targeting interventions for substance use.*

## 2. Review question

Primary: In people who use alcohol, tobacco/nicotine or other drugs, do interventions whose stated primary aim is to change beliefs about the benefits of the substance, or about the difficulty and costs of stopping, reduce substance use compared with no intervention, usual care or an active comparator?

Secondary:
1. Do these interventions change the targeted beliefs (positive outcome expectancies, perceived benefits, beliefs about quitting), and is belief change associated with, or a mediator of, change in use?
2. Do effects differ by population (clinical or dependent vs non-clinical), substance, intervention type (seminar-style belief reversal such as the Allen Carr method; experiential or didactic expectancy challenge; counter-attitudinal advocacy or dissonance-based), dose, delivery format, follow-up length and country income level?
3. What harms or adverse effects are reported?

## 3. Searches

**Databases** (inception to search date, no language limit; non-English records screened with machine translation and a native speaker where possible):
- MEDLINE via PubMed
- Embase (Ovid or Embase.com)
- APA PsycINFO (Ovid or EBSCO)
- Cochrane CENTRAL
- Web of Science Core Collection (citation searching)
- Regional: IndMED / Indian Citation Index if accessible through AIIMS library; WHO Global Index Medicus (LMIC regional databases)

**Registers and grey literature:** ClinicalTrials.gov, WHO ICTRP (includes CTRI and ChiCTR), ISRCTN, OSF; ProQuest Dissertations; conference abstracts via Embase. Allen Carr's Easyway publishes a list of studies on its website: screen it for peer-reviewed reports, but do not include company outcome data that is not peer-reviewed.

**Other methods:** backward and forward citation searching of included studies and of the three neighbour reviews; contact corresponding authors of included trials for unpublished belief or mediation data (neither Allen Carr smoking RCT reported belief outcomes).

**Date restriction:** none. **Search dates:** to be filled at run time; rerun within 6 months of submission.

## 4. Search strategy (MEDLINE/PubMed draft; translate for other databases)

Not yet run (NCBI esearch was returning HTTP 500 on 5 Nov 2026). Pilot it against the test set below before registering, and report hit counts.

```
#1 Substance use
("Substance-Related Disorders"[Mesh] OR "Alcohol Drinking"[Mesh] OR "Tobacco Use"[Mesh]
 OR "Smoking Cessation"[Mesh] OR "Tobacco Use Cessation"[Mesh] OR "Marijuana Use"[Mesh]
 OR alcohol*[tiab] OR drink*[tiab] OR binge*[tiab] OR smok*[tiab] OR tobacco[tiab]
 OR cigarette*[tiab] OR nicotine[tiab] OR vaping[tiab] OR cannabis[tiab] OR marijuana[tiab]
 OR opioid*[tiab] OR heroin[tiab] OR cocaine[tiab] OR methamphetamine*[tiab]
 OR amphetamine*[tiab] OR "substance use"[tiab] OR "substance misuse"[tiab]
 OR addict*[tiab] OR dependen*[tiab])

#2 Named belief-targeting approaches
("Allen Carr"[tiab] OR "Allen Carr's"[tiab] OR Easyway[tiab] OR "easy way to stop"[tiab]
 OR "easy way to quit"[tiab] OR "expectancy challenge"[tiab] OR "expectancy challenges"[tiab]
 OR "expectancy-challenge"[tiab] OR "challenging expectancies"[tiab]
 OR "counter-attitudinal"[tiab] OR counterattitudinal[tiab] OR "cognitive dissonance"[tiab]
 OR "dissonance-based"[tiab])

#3 Belief or expectancy change as the target (proximity searching)
("expectancy change"[tiab:~3] OR "expectancies change"[tiab:~3]
 OR "expectancy modification"[tiab:~3] OR "expectancies modification"[tiab:~3]
 OR "belief change"[tiab:~3] OR "beliefs change"[tiab:~3]
 OR "belief modification"[tiab:~3] OR "beliefs challenge"[tiab:~3]
 OR "outcome expectancies intervention"[tiab:~4] OR "perceived benefits intervention"[tiab:~4]
 OR "positive expectancies reduce"[tiab:~4] OR "smoking beliefs"[tiab:~2]
 OR "drinking beliefs"[tiab:~2] OR "alcohol beliefs"[tiab:~2]
 OR "Alcohol Expectancies"[tiab] OR "outcome expectancies"[tiab])

#4 Controlled designs (adapted from the Cochrane highly sensitive RCT filter, plus non-randomised comparative terms)
(randomized controlled trial[pt] OR controlled clinical trial[pt] OR randomi*[tiab]
 OR randomly[tiab] OR trial[tiab] OR placebo[tiab] OR "control group"[tiab]
 OR "comparison group"[tiab] OR quasi-experiment*[tiab] OR "non-randomi*"[tiab]
 OR nonrandomi*[tiab] OR "controlled before"[tiab])

#5 #1 AND (#2 OR #3) AND #4
#6 #5 NOT (animals[mh] NOT humans[mh])
```

Notes for translation: in Ovid (Embase, PsycINFO) replace #3 with adjacency, e.g. `((expectanc* or belief* or "perceived benefit*") adj3 (challeng* or modif* or chang* or restructur* or revers* or reduc*)).ti,ab.`, and add the controlled-vocabulary terms each database offers for expectancies, health beliefs, attitudes to drinking or smoking, and cessation (look them up in the Emtree and APA thesaurus browsers; do not guess the headings). PubMed proximity (`[tiab:~N]`) does not accept wildcards, which is why #3 lists word forms; the Ovid version will be more sensitive than PubMed, so run both and deduplicate.

**Test set** (the strategy must retrieve all of these; extend after scoping): Keogan et al. 2019 *Tob Control*; Frings et al. 2020 *Addiction*; Wood et al. 2017 *BMJ Open* (protocol, for linking); Darkes & Goldman 1993 *J Consult Clin Psychol*; Dijkstra et al. 2014 (Allen Carr non-randomised comparison); three studies included in Scott-Sheldon 2012 picked at random; two studies included in Wang X 2026.

## 5. Condition or domain

Substance use and substance use disorders: alcohol, tobacco/nicotine, cannabis, opioids, stimulants and other drugs; hazardous use through to dependence.

## 6. Participants / population

Inclusion: people of any age who use one or more of the above substances, in any setting (community, college, primary care, specialist treatment, inpatient, workplace, online). Studies of mixed populations are included if at least 80% use the target substance or results are reported separately for users.

Exclusion: studies whose participants are only non-users (pure primary prevention in abstainers), and studies of behavioural addictions without a substance.

## 7. Intervention(s) / exposure(s)

Interventions whose **stated primary aim or main active component** is to change one or both of:
- **beliefs about what the substance gives** (positive outcome expectancies, perceived benefits such as relaxation, confidence, sociability, pleasure, taste, stress relief, sleep), and
- **beliefs about stopping** (that stopping is hard, needs willpower, means deprivation or loss).

This includes: seminar- or book-based belief-reversal methods (Allen Carr's Easyway and similar); experiential expectancy challenge (placebo or alcohol administration with feedback); didactic or digital expectancy challenge; counter-attitudinal advocacy and dissonance-based interventions aimed at substance beliefs; and multi-component programmes **if** belief change is named as the primary mechanism and gets at least half of the contact time.

Excluded: general CBT, motivational interviewing, relapse prevention, contingency management, personalised normative feedback or harm-information campaigns, **unless** they meet the criterion above. Risk-perception interventions (beliefs about harms only) are excluded; they are a different construct. Pharmacotherapy alone is excluded.

Decision rule for borderline cases: two reviewers judge from the methods section whether belief change is the declared primary target; disagreements go to a third reviewer; all borderline decisions are listed in a supplementary table.

## 8. Comparator(s) / control

No intervention, assessment only, waiting list, usual care or treatment as usual, or any active comparator (another psychosocial intervention, pharmacotherapy, specialist cessation services, attention-matched education). Head-to-head comparisons of two belief-targeting interventions are included and analysed separately.

## 9. Types of study to be included

Randomised controlled trials (individual or cluster), quasi-randomised trials, and non-randomised controlled studies with a concurrent comparison group. Excluded: single-arm studies, case series, cross-sectional studies, qualitative-only studies, protocols without results (protocols are used only to find results and check outcome switching). Single-arm Allen Carr case series (e.g., Hutter 2006, Moshammer 2007) are listed in a supplementary map but not included in synthesis.

## 10. Context

Any country and setting. Country income level (World Bank classification at the study's publication year) is coded for subgroup analysis because no included evidence is expected from South Asia; this gap is a reported finding.

## 11. Main outcome(s)

1. **Substance use** at the longest follow-up and at prespecified time points (≤ 1 month, > 1 to 6 months, > 6 months):
   - binary: abstinence (point-prevalence or continuous; biochemically verified preferred and coded separately from self-report), relapse;
   - continuous: quantity, frequency, heavy-use days, drinks per drinking day.
2. **Change in the targeted beliefs**: positive outcome expectancies (e.g., AEQ, CEOA, smoking consequences or expectancy scales), perceived benefits, beliefs about quitting.

Effect measures: risk ratio for binary outcomes; standardised mean difference (Hedges' g) for continuous outcomes, or mean difference where the same scale is used.

## 12. Additional outcome(s)

Craving; abstinence or quit self-efficacy; desire thinking; identity (non-user identity); readiness to change; engagement and attendance; treatment-seeking; quality of life; adverse events, including weight gain, distress and withdrawal complications; formal mediation analyses (whether reported, method, indirect effect).

## 13. Data extraction (selection and coding)

Records deduplicated in Zotero or Rayyan; title/abstract and full-text screening by two independent reviewers in Rayyan, with a pilot round of 50 records and Cohen's κ reported; disagreements resolved by discussion, then by the guide. Extraction on a piloted form (Excel or REDCap) by one reviewer, checked in full by a second: bibliographic data, design, setting, country and income level, population (substance, severity, clinical status, detox status), intervention (TIDieR items, including who delivers it, whether the deliverer is a former user, dose, format, group size, language), comparator, belief measures and timing, use outcomes and timing, analysis population, funding and conflicts of interest (including funding by the intervention's owner). Authors contacted twice for missing data.

## 14. Risk of bias (quality) assessment

RCTs: Cochrane RoB 2 (separate assessment for each main outcome; cluster variant where needed). Non-randomised studies: ROBINS-I (version 2 if released and stable at assessment time). Two independent assessors, consensus by discussion. Particular attention to: self-reported use without biochemical verification, open-label designs, differential attrition (Keogan retained about a third at 12 months), missing-equals-relapse assumptions, and developer funding. Certainty of evidence for each main outcome by GRADE, with a Summary of Findings table.

## 15. Strategy for data synthesis

Random-effects meta-analysis (REML estimator with Hartung–Knapp–Sidik–Jonkman confidence intervals) when at least three studies are sufficiently similar in population, intervention type, comparator and outcome. Separate syntheses for: (a) seminar-style belief reversal, (b) expectancy challenge, (c) counter-attitudinal/dissonance approaches; pooling across types only as a sensitivity analysis. One effect per study per analysis, chosen by a prespecified hierarchy (verified abstinence > self-reported abstinence > heavy-use frequency > quantity); if several effects must be combined, use robust variance estimation. Heterogeneity reported as τ², I² and 95% prediction intervals. Small-study effects examined with funnel plots and Egger's test when ≥ 10 studies. Where pooling is not appropriate, synthesis without meta-analysis following SWiM guidance (vote counting by direction of effect, with effect sizes tabulated). Belief-change outcomes synthesised the same way; the belief → use link summarised from studies reporting mediation or correlated change (narrative, with a meta-analytic correlation only if ≥ 5 studies report it).

## 16. Analysis of subgroups or subsets

Prespecified: clinical/dependent vs non-clinical samples; substance; intervention type; experiential vs didactic expectancy challenge; dose (single session vs multi-session); delivered by a former user vs not; follow-up period; country income level; verified vs self-reported outcome. Sensitivity: excluding high risk-of-bias studies; excluding developer-funded studies; excluding non-randomised studies.

## 17. Review team, funding, conflicts

- Dr. Gowtham H R, PhD scholar, Department of Psychiatry, AIIMS Guwahati (lead; screening, extraction, analysis).
- Dr. Sharad Philip, Department of Psychiatry, AIIMS Guwahati (guide; arbitration, methods).
- Second reviewer: to be named (a colleague or the ANRF project JRF; HANDOVER open question 8).
- Information specialist / librarian: to be named (AIIMS Guwahati library).
- Funding: none (unfunded PhD work) unless intramural funds are obtained.
- Conflicts: the lead reviewer is developing a belief-reversal intervention for alcohol dependence (BRI-AD) and could benefit from favourable findings; declare this. No relationship with Allen Carr's Easyway.

## 18. Dates and stage

Anticipated start: on registration. Anticipated completion: within 6 months. Stage at registration: preliminary searches done; formal screening not started (PROSPERO requires registration before data extraction begins).

---

## Open decisions for Dr. Reddy and the guide

1. **Scope width.** As drafted, this covers all substances, which makes it a stronger first paper but a bigger job (the expectancy-challenge college literature alone is 20+ trials). The narrower alternative is "belief-targeting interventions in clinical/dependent populations only" (likely under 15 studies, with the college literature summarised from existing reviews). Recommendation: keep all substances for the search, and decide after scoping whether the college expectancy-challenge trials are synthesised in full or summarised through Scott-Sheldon and Wang.
2. **Second reviewer** (open question 8).
3. **Target journal** (open question 10): *Addiction*, *Drug Alcohol Depend* or *Addict Behav* per `03` §11.
4. **Lane 1 timing review**: not drafted. `02-lane1` §5 now recommends it only as a short methods-and-reporting review because the AUD neuromodulation space is crowded. Say if you want it drafted too.
