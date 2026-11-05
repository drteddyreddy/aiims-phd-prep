# 02 - Verification table

Built 5 Nov 2026 on Dr Reddy's laptop.

**How it was made.** Full texts came from PMC (BioC API) or Europe PMC. Abstracts came from PubMed efetch, Semantic Scholar or the bioRxiv API. `anthropic/claude-haiku-5.5` (via OpenRouter) extracted each row, told to use only the paper's text and to give a verbatim quote for every number. A script then string-matched every quote against the source text: **448 of 450 quotes matched**. The 2 misses are in the Wood 2017 row. The two SECONDARY rows (Mishra 2015, Shanghai 2025) come from web search and were not quote-checked.

Raw JSON with every quote is in `~/thesis-papers/extract/*.json` on the laptop (not committed). PDFs and full texts are in `~/thesis-papers/` (not committed).

Provenance tags: FULLTEXT = whole paper read; ABSTRACT = abstract only; SECONDARY = web or registry snippet.

## Summary table

| # | Paper | Design | N | Population and timing after detox | Parameters | Sham/control | Primary result | Tag |
|---|---|---|---|---|---|---|---|---|
| 1 | Jiang G, Kang J, Jiang R, Dong Q | Systematic review and meta-analysis of 9 randomized sham-controlled trials of prefrontal iTBS in SUDs. Craving analysed as SMD using a random-effects model; abs | 556 participants in 9 trials; 512 in the 8 craving trials; 44 in the alcohol trial (abstinence only). | Individuals with a formally diagnosed SUD: methamphetamine (5 trials, n=311), nicotine (3 trials, n=201), alcohol (1 trial, n=44). Time since detoxification: NR. | Prefrontal iTBS. Targets: left DLPFC (7 trials), right DLPFC (1), medial PFC (1). Pattern: 50-Hz triplets at 5 Hz. Sessions 10 to 28 across trials; intensity 80 to 110% RMT; pulses per session 600 to 1,200 by trial (per-trial values in extra table). Pooled sch | Sham stimulation per trial, e.g., coil rotated away from scalp, placebo side of an A/P coil with forehead electrical stimulation, magnetically shielded placebo  | Active iTBS reduced craving versus sham: SMD = −0.65, 95% CI −1.08 to −0.21; p = 0.003; I² = 81% (substantial heterogeneity). | FULLTEXT |
| 2 | Treiber M, Tsapakis EM, Fountoulakis K | Systematic review and random-effects meta-analysis of randomized controlled trials (abstract only) | 475 participants across treatment and control groups; 12 studies | Alcohol use disorder; timing after detoxification NR | Multiple-session rTMS, at least 10 sessions required for inclusion; targets analysed as medial prefrontal cortex, right DLPFC, left DLPFC; frequency, TBS pattern, %RMT, pulses/session and schedule NR | Sham stimulation (active rTMS vs sham); sham procedure details NR | Immediately post-treatment, active rTMS vs sham: SMD = -0.79, 95% CI -1.53 to -0.04, P = 0.04, I2 = 93% | ABSTRACT |
| 3 | Hoven M, Schluter RS, Schellekens AF, van Holst RJ, Goudriaan AE | Single-centre, single-blind, sham-controlled, parallel-group RCT, randomised 1:1 to TAU plus active or sham HF-rTMS; follow-up at 3 and 6 months (with 12-month  | 80 randomised (40 active, 40 sham); 100 screened, 82 included, 2 withdrew consent before start. | Detoxified, abstinent adult AUD inpatients at Jellinek Addiction Treatment Centre, Amsterdam; age 20–65, recent DSM-IV alcohol dependence (less than 4 months after detoxification). Recruitment March 2016 to February 2019 | Target: right DLPFC, localised at F4 by 10–20 EEG system. Pattern: 60 trains of 10 Hz, each 5 s, at 110% motor threshold (resting MT from 5/10 thumb abductor responses). Coil: 70-mm double air film coil, Magstim Rapid2. Sessions: 10 on 10 consecutive work-days | Identical procedure and stimulation parameters with the coil tilted 90° relative to the scalp. Authors note sham does not replicate somatosensory effects of sti | Abstinent days (ITT, missing = relapse): active 115 ± 69.8, sham 124 ± 65.9; difference 9 days. Poisson ratio (active vs sham) 1.421, 95% CI 0.578–3.547, P = 0.436 (Wald Z 0.779). Complete-case: active 152 ± 41.3, sham 158 ± 30.6 days; ratio 0.936 (0.775–1.128), P = 0.477. Bayesian 95% credible inte | FULLTEXT |
| 4 | Belgers M, et al | Single-blind, randomized, sham-controlled trial of rTMS added to treatment as usual (TAU); 1:1 allocation with a computer-generated sequence | Randomized 34 (37 screened, 3 lost to contact). Four withdrew consent after baseline, leaving 30 who started treatment.  | Adults aged 20 to 65 with DSM-5 AUD (SCID-5-CV) and recent (<6 weeks) inpatient alcohol detoxification. Recruited 2015 to 2019 at two addiction centres and Radboud UMC, Netherlands. All had six or more DSM-5 AUD criteria | Target: right dlPFC at F4 (10-20 EEG system), marked on a cap relative to nasion-inion landmarks. Figure-of-eight coil, Magstim Rapid2. Motor threshold found over right motor cortex (5 of 10 stimuli producing contraction). Intensity 110% MT. Frequency 10 Hz; 6 | Sham coil: two-wing coil rotated 90 degrees from the scalp, so most field lines do not enter the skull; procedure and sound were preserved. Both groups received | Significant group-by-time interaction on craving (Wilks' Λ = 0.348, p = 0.032). Less increase in craving over time in the rTMS group. Group-level differences were largest at 3 months. No CIs or effect sizes (e.g. partial eta-squared, Cohen's d) reported in text. Main effects: time Wilks' Λ = 0.203,  | FULLTEXT |
| 5 | Harel M, et al | Double-blind, randomized, sham-controlled proof-of-concept trial (per abstract) | 51 randomized (total); arm sizes NR | Recently abstinent, treatment-seeking patients with alcohol use disorder (moderate to severe). Time since last drink/detox at enrolment: NR | Deep TMS (dTMS) with H7 coil; target: midline frontocortical areas including medial prefrontal cortex and anterior cingulate cortex. Pattern: 100 trains of 30 pulses at 10 Hz per session (= 3,000 pulses per session, derived). Intensity %RMT: NR. Schedule: 15 s | Sham dTMS (described as sham control arm); sham method details NR | Percentage of heavy drinking days during follow-up lower in active vs sham: 2.9 ± 0.8% vs 10.6 ± 1.9%, p = .037. Effect size: NR. 95% CI: NR. Whether ± denotes SD or SEM: NR. | ABSTRACT |
| 6 | Zhao J-N, et al | Single-centre, randomized, double-blind, sham-controlled pilot trial with pre/post fMRI cue-reactivity and 12-month telephone relapse follow-up; ChiCTR220006545 | 28 randomized (16 active cTBS, 12 sham); 2 observations excluded from Cox analysis for loss to follow-up | Adults aged 18-60 with DSM-5 AUD recruited from the alcohol detoxification clinic of the First Specialized Hospital of Harbin. Exclusions: current acute withdrawal or severe withdrawal, epilepsy/seizure disorder, TMS/MRI | Inhibitory cTBS to right DLPFC, localised by F4 (International 10-20 EEG) scalp landmark; fig. 8 cooling coil; 3-pulse bursts at 50 Hz repeated at 5 Hz theta; 100% of individual RMT; 600 pulses over 40 s per session; 10 sessions, one per weekday over two conse | Same F4 location with coil oriented perpendicular (90°) to scalp; reproduces device sound and scalp sensation without effective field penetrating skull. Schedul | Relapse (12-month follow-up): HR = 0.210, 95% CI [0.070, 0.633], p = 0.006 (active vs sham). Log-rank p = 0.017. rSFG group x intervention interaction F = 4.347, p = 0.047 (no effect size or CI reported). Machine-learning relapse prediction: accuracy 78.7%, AUC 0.903 (no CI reported). | FULLTEXT |
| 7 | Rakesh G, Adams TG, Ballard DH, McLouth CJ, Rush CR | Systematic review and meta-analysis of randomized controlled trials (RCTs); abstract reports a meta-analysis of four RCTs with sham control and a narrative revi | NR | Adults with methamphetamine use disorder (MUD); time since detoxification NR | Target: NR for reviewed trials (abstract background mentions left dlPFC for prior TMS studies only). Protocols: intermittent TBS (iTBS) in the meta-analysis; accelerated iTBS in one non-sham trial; continuous TBS (cTBS) mentioned as not yet reviewed. Intensity | Sham iTBS (four RCTs in the meta-analysis); two additional RCTs had no sham control arm. Sham method details NR | iTBS more effective than sham iTBS in reducing cue-induced craving: SMD in change = 1.04; 95% CI [0.16, 1.92] | ABSTRACT |
| 8 | Living SR/MA: effectiveness of NIBS protocols on drug craving and consumption/relapse in SUD, 208 trials and 36 protocols | Living systematic review and meta-analysis (abstract only). Controlled trials up to January 1, 2024; 116 randomized sham-controlled trials eligible for meta-ana | 208 trials in the systematic review (121 TMS, 86 tES, 1 tFUS); 116 randomized sham-controlled trials (59 TMS, 57 tES) in | Participants with any type of substance use disorder (all SUD types). Timing after detoxification: NR. | Abstract reports protocol-level subgroups only: high-frequency deep TMS with H4 coil (maximum electric field over frontopolar cortex; single study); high-frequency rTMS over left DLPFC; bilateral anodal-right cathodal-left tDCS over DLPFC (maximum field on fro | Sham-controlled trials (sham method NR in abstract). | TMS: craving g = 0.52 (95% CI 0.29-0.75), I² = 89.36%; consumption g = 0.41 (95% CI 0.26-0.56), I² = 61.56%. tES: craving g = 0.40 (95% CI 0.25-0.55), I² = 60.69%; consumption g = 0.27 (95% CI 0.15-0.38), I² = 22.67%. Pooled effects by modality only; CIs for protocol-level results NR. | ABSTRACT |
| 9 | Rossi S, Antal A, Bestmann S, et al | n/a (guideline) | n/a (guideline) | n/a (guideline) | n/a (guideline) | n/a (guideline) | n/a (guideline) | FULLTEXT |
| 10 | Ekhtiari H, Tavakoli H, Addolorato G, et al | n/a (consensus) | n/a (consensus) | n/a (consensus) | n/a (consensus) | n/a (consensus) | n/a (consensus) | FULLTEXT |
| 11 | Keogan S, Li S, Clancy L | Single-centre, open, parallel-group, randomised superiority trial (CONSORT cited); block randomisation by gender, age and education; ITT primary analysis with c | 300 randomised (AC n=151; Quit.ie n=149); all 300 included in ITT denominators. | Adult smokers aged 18+, smoking at least 5 cigarettes/day, English-speaking, recruited by advertisement (July 2015–Feb 2016). Excluded: doctor-diagnosed acute cardiac/respiratory or serious psychiatric illness, current t | Not applicable (no neuromodulation). AC arm: free 5-hour group seminar (max 20 participants) delivered by experienced AC therapists; smoking continued until a ritual final cigarette, then 20-min relaxation; two free AC follow-ups; no pharmacotherapy permitted. | No sham. Active comparator: Quit.ie (HSE National Online Smoking Cessation Service). Medication in Quit.ie at client's discretion; AC participants instructed no | 3-month ITT CO-validated quit rate, AC 26.5% (40/151) vs Quit.ie 14.8% (22/149), p=0.006 (Table 2 decimals; abstract rounds to 27% vs 15%). Adjusted logistic regression AC vs Quit.ie OR 2.26 (95% CI 1.22 to 4.21), p=0.01. | FULLTEXT |
| 12 | Frings D, Albery IP, Moss AC, et al | Two-arm, parallel-group, single-blind randomized controlled trial in London, UK. Recruitment and first randomization 3 February 2017; last follow-up 25 May 2018 | 620 randomized (310 ACE; 310 SSS). 468 attended treatment (255 ACE; 213 SSS). 100 completed 6-month measures (23.7% ACE  | Adults aged 18 or older who were current smokers wanting to quit; mean age 40.8 years; 53.4% male. Excluded: pregnancy, mental health condition, respiratory disease, concurrent similar trial enrolment, unwillingness to u | Not a neuromodulation study (no target, localisation, frequency, TBS, %RMT or pulses). ACE: one group session of 4.5-6 h combining CBT elements with a brief relaxation exercise; scheduled smoking breaks every 45-60 min and a final ritual cigarette; one therapi | No sham. Active comparator was the specialist SSS providing behavioural and pharmacological support. Participants were blind to the treatment not received; trea | Verified 26-week continuous abstinence 19.4% (60/310) ACE vs 14.8% (46/310) SSS; risk difference 4.5% (95% CI -1.4 to 10.4%); OR 1.38 (95% CI 0.90 to 2.10); Pearson chi-square P = 0.165; Bayes factor 1.24 (described by authors as non-conclusive). Post hoc, with a 5% non-inferiority limit, the lower  | FULLTEXT |
| 12 | Wood CE, et al | Protocol for a two-arm, parallel-group, blinded randomised controlled trial. Randomisation is stratified on four factors (nicotine dependence, prior quit attemp | Planned, not analysed: initial sample of 620 (310 per arm). No results reported. | People who smoke tobacco cigarettes, aged at least 18, motivated to quit. Excluded: self-reported mental health condition, pregnancy, respiratory disease (COPD or emphysema), preference for NHS treatment, other concurren | Not applicable (behavioural/pharmacological intervention, not neurostimulation). ACE: single group session (up to 25 attendees), 5–6 hours, CBT elements, ends with about 20 min hypnotherapy/relaxation; optional top-up of two further sessions (about 3.5 hours,  | No sham. Comparator is the NHS stop-smoking service (active comparator). No no-treatment control. | Not reported (protocol). Planned analysis: logistic regression of treatment condition on cessation at 26 weeks, with 95% CIs. | FULLTEXT |
| 13 | Systematic review of Allen Carr's Easyway for smoking cessation | Systematic review (PRISMA-guided) of RCTs and observational studies of the Allen Carr (AC) method for smoking cessation; PubMed/MEDLINE and Embase searched 29 M | Six included studies; sample sizes ranged from 92 to 620 participants. Per-study N: Hutter 2006 = 223 respondents (out o | Population: adult smokers attending AC single-session seminars (workplace or community) or reading the AC book, including patients with head and neck disorders (Foshee). Pharmacotherapy-free method; detox/withdrawal timi | NR (not a neuromodulation study). Intervention description as reported in the review: AC single-session group seminar, typically 4 to 6 hours, small groups of about 20 or fewer, with up to two no-cost follow-up sessions. Keogan used a 5-hour seminar; Frings us | NR at review level. Included-study controls: no treatment (Dijkstra); Quit.ie online service (Keogan); Stop Smoking Service with NRT (Frings); not reading the b | Cessation rates for AC seminar attendees ranged from 19% to 51% across included studies (unadjusted, heterogeneous designs). Dijkstra 2014 (observational): 13-month abstinence 41.1% vs 9.6%; multivariate adjusted OR 6.52 (95% CI 3.10–13.72). Keogan 2019 (RCT, AC seminar vs Quit.ie): 3-month AOR 2.26 | FULLTEXT |
| 14 | Herremans SC, et al | Two-part fMRI study in one cohort. Part 1: single-session, randomised, single-blind, sham-controlled right DLPFC HF-rTMS (between-subjects, active vs sham, 13 p | Twenty-six patients analysed for the single-session part (13 active, 13 sham). Treatment part: 23 completed (event parad | Recently detoxified, hospitalised alcohol-dependent patients aged 18 to 65. Detoxified with diazepam (CIWA-AR). Days between last alcohol intake and stimulation start: M = 17.8, SD = 6.0 (overall). Single-session part on | Target: right DLPFC (Brodmann area 9/46), located by MRI non-stereotactic guidance. Figure-of-eight double 70 mm coil, tangential to skull. Frequency 20 Hz, 40 trains of 1.9 s, 12 s intertrain interval, 1560 pulses per session. Intensity 110% of resting MT. Tr | Sham: coil held at 90 degrees, resting on scalp with one edge. Patients wore earplugs and were blindfolded. Blinding was reported only for the single-session pa | Treatment part: general craving decreased on OCDS (Z = -2.41, P = 0.02) and AUQ (Z = -2.36, P = 0.02). Cue-induced TLS: Friedman X2(5) = 24.32, P = 0.001; post hoc, only first versus last scan comparisons were significant, all other TLS comparisons were not. Single session: no significant TLS change | FULLTEXT |
| 15 | Mishra BR, Nizamie SH, Das B, Praharaj SK | Prospective, single-blind, sham-controlled study. Allocation method and concealment NR. Abstract describes two-way repeated-measures ANOVA. | 45 randomised or allocated (abstract); 30 active rTMS, 15 sham. Dropouts and analysed N NR. | Patients with alcohol dependence syndrome (ICD-10 DCR). Entry criterion: CIWA-Ar scores <=10. Time since last drink or detoxification timing NR. | Target: right DLPFC. High-frequency rTMS at 10 Hz; 4.9 s per train; inter-train interval 30 s; 20 trains per session; 10 sessions in total. Coil, localisation method, intensity (%RMT) and pulses per session NR. Schedule (frequency of sessions over days) NR. Co | Sham rTMS (method NR in abstract). | Two-way repeated-measures ANOVA showed significant reduction in post-rTMS ACQ-NOW total and factor scores in the active group vs sham. Treatment x time interaction effect size moderate, eta(2) = 0.401. No CI, F, p value or group means reported in abstract. | ABSTRACT |
| 15 | Mishra BR, Praharaj SK, Katshu MZ, Sarkar S, Nizamie SH | see detail | | | | | see detail | SECONDARY |
| 15 | Raikwar et al | Prospective, single-blind, randomized, sham-controlled trial; sham = coil placed tangentially without switching on, with the circular coil switched on to provid | 60 randomized (30 active, 30 sham); all completed the trial | Right-handed male inpatients aged 25 to 56 years with ICD-10 alcohol dependence syndrome, recruited only after completion of detoxification. Drug-naive for anticraving medication per Discussion, though Table 1 reports 25 | Target: left DLPFC, located by the 5 cm rule. Device: STM 9000 (ATES MEDICA / EBNeuro), 70 mm air-cooled flat figure-of-eight coil, angled 45° tangentially, handle posterior. Motor threshold on right abductor pollicis brevis, visual method, Rossini-Rothwell al | Figure-of-eight coil placed tangentially to the head without switching on; no MT determined and no magnetic stimulation delivered; circular coil switched on and | No significant difference between active and sham groups at any time point. Pre-rTMS: active 218.17 ± 9.699 vs sham 216.17 ± 13.488 (F = 1.526, p = 0.226, partial eta squared 0.051). Post-rTMS: active 92.03 ± 6.625 vs sham 93.30 ± 6.342 (F, p and eta squared NR for this row). 2 weeks post-rTMS: acti | FULLTEXT |
| 15 | Joshi T, Dhiman V, Verma R, et al | Single-blind (per Limitations), randomized sham-controlled, parallel-group trial with 1:1 allocation; longitudinal follow-up at 1 and 3 months. Adjunct to treat | 149 randomized (75 active, 74 sham). 107 completed the 10 intended sessions (51 active, 56 sham). Derived: 42 did not co | Male adults aged 18-55 with DSM-5 alcohol use disorder, SADQ >30 (severe), OCDS >1, right-handed. Included after completion of acute withdrawal management and at least 3 days abstinent from alcohol and benzodiazepines. M | Bilateral tDCS, anode F3 (left dlPFC) and cathode F4 (right dlPFC), 10:20 EEG placement. Current 2 mA; ramp-up to 2 mA over 30 s, then 20 min at 2 mA. Two sessions per day spaced at least 2 h apart; 10 sessions over 5 consecutive days. Target/localisation: dlP | Sham tDCS: ramp-up for 30 s at the beginning, then stimulation ended (the paper describes the sham as ramp-up only). Participants blinded to allocation through  | 3 months OCDS: active 28.50 ± 13.23 vs sham 34.75 ± 14.07; t(147) = -2.79; Cohen's d = 0.45 (small); no CI reported for this test. Mixed ANOVA: F(2,294) = 5.52, P < 0.01; partial eta-squared for group x time 0.04 (small). Time main effect F(1.5)=201.2, P<0.001, partial eta-squared 0.58 (reported in  | FULLTEXT |
| 16 | Wang H, Yuan C, Gan H, Jiang H, Zhao Y, Du J, Zhang Y | see detail | | | | | see detail | SECONDARY |
| 17a | Scott-Sheldon LAJ, Terry DL, Carey KB, Garey L, Carey MP | Systematic search and meta-analysis of 14 studies (19 expectancy challenge [EC] interventions). Between-group (EC vs control) and within-group pre-post effect s | 1,415 (abstract); Results section gives 1,417 sampled (median 72 per study). Discrepancy between sources. | College students, mean age 20 (SD 0.93, range 19-21); 60% men (abstract reports 40% women); 88% White; 91% (k = 13) reported alcohol use; no past or current alcohol treatment. Timing (first assessment): 2 weeks (M = 2.07 | Not applicable (no neurostimulation). Behavioural EC interventions. Experiential EC (k = 11, 58%): median 3 sessions (range 1-3), median 105 min per session (range 75-105); alcohol or placebo administered in a bar-like group setting, social/party games, identi | Active comparison (53%; e.g., brief form of intervention; median 2 sessions of 21 min, range 10-105 min); assessment-only control (41%); 2 studies had no compar | Between-group at first follow-up (fixed effects; Table 2): positive expectancies d+ = 0.28 (95% CI 0.14, 0.43), k = 11; quantity d+ = 0.23 (0.08, 0.38), k = 11; frequency of heavy drinking d+ = 0.27 (0.06, 0.47), k = 5. Negative expectancies not significant (d+ = −0.17, −0.37 to 0.04, k = 5). Proble | FULLTEXT |
| 17b | Wang X, Yang S, Xie X, Sethabouppha H | Systematic review and meta-analysis of randomized controlled trials (PRISMA-compliant, PROSPERO-registered; registration number NR in abstract) | NR (abstract reports 8 trials; total participants NR) | College students. Detox: not applicable. Timing: approximately one month post-intervention for the binge-episode result; 3-6 months for sustained effects. | Not applicable (non-stimulation). Expectancy-challenge interventions in experiential, didactic, or digital formats. Dose, sessions and schedule: NR. | Non-alcohol control conditions (type not specified in abstract) | Hedges' g = -0.20 (95% CI -0.33 to -0.07), k NR, at approximately one month; small but significant reduction. | ABSTRACT |

## Per-paper detail

### 1. Jiang G, Kang J, Jiang R, Dong Q. Efficacy of iTBS for SUD: SR/MA of sham-controlled RCTs. Front Neurol 2026;17:1866761. doi:10.3389/fneur.2026.1866761 (PROSPERO CRD420261363708 per web search)

Source: PMC13486172 | Tag: **FULLTEXT** | Quotes verified: 30/30

**What this changes in the cloud pack:** Confirms the pack's SMD -0.65 (-1.08 to -0.21), I2 81%, and the null nicotine subgroup (SMD 0.01). There is **only one alcohol trial (n=44)**, and it feeds the abstinence analysis only, not craving. So this meta-analysis gives no craving estimate for alcohol, and the Lane 1 sample size (d = 0.6, `02-lane1` sample-size section) leans on methamphetamine trials. Say so in the synopsis.

| Field | Extracted |
|---|---|
| Design | Systematic review and meta-analysis of 9 randomized sham-controlled trials of prefrontal iTBS in SUDs. Craving analysed as SMD using a random-effects model; abstinence analysed as OR using a fixed-effect model. PROSPERO CRD420261363708. |
| N | 556 participants in 9 trials; 512 in the 8 craving trials; 44 in the alcohol trial (abstinence only). |
| Population and timing after detox | Individuals with a formally diagnosed SUD: methamphetamine (5 trials, n=311), nicotine (3 trials, n=201), alcohol (1 trial, n=44). Time since detoxification: NR. |
| Stimulation or intervention parameters (target, localisation, frequency/TBS pattern, intensity %RMT, pulses/session, sessions, schedule) | Prefrontal iTBS. Targets: left DLPFC (7 trials), right DLPFC (1), medial PFC (1). Pattern: 50-Hz triplets at 5 Hz. Sessions 10 to 28 across trials; intensity 80 to 110% RMT; pulses per session 600 to 1,200 by trial (per-trial values in extra table). Pooled schedule per trial as in Table 1. |
| Sham/control method | Sham stimulation per trial, e.g., coil rotated away from scalp, placebo side of an A/P coil with forehead electrical stimulation, magnetically shielded placebo coil, or integrated sham coil with forehead stimulation (see Table 1). |
| Primary outcome and instrument | Craving (continuous). Instruments differed across trials (cue-induced craving and clinical craving scales); pooled instrument NR. |
| Primary result with effect size and CI | Active iTBS reduced craving versus sham: SMD = −0.65, 95% CI −1.08 to −0.21; p = 0.003; I² = 81% (substantial heterogeneity). |
| Secondary results | Methamphetamine subgroup (5 trials, n=311): SMD = −1.03, 95% CI −1.29 to −0.77; I² = 11%. Nicotine subgroup (3 trials, n=201): SMD = 0.01, 95% CI −0.28 to 0.30; I² = 3%. Subgroup difference p < 0.00001 (I² = 96.3%). Abstinence (3 trials, nicotine and alcohol): OR = 2.19, 95% CI 1.09 to 4.39; p = 0.03; I² = 0%. |
| Follow-up | Most follow-up periods were 4 weeks or shorter. Exceptions: Durazzo 6 months; Dieler abstinence at 3, 6 and 12 months; Mikellides 1-week follow-up. |
| Adverse events | NR (not extracted in the pooled synthesis). |
| Risk-of-bias notes | Original Cochrane tool in RevMan 5.4 (RoB 2 not used). All 9 trials low risk for sequence generation. Allocation concealment adequate in 1 trial (ref 25); unclear in the rest. Blinding of participants and personnel reported in 8 trials; 1 trial (ref 27) high risk of performance bias. Detection and attrition bias low in all. Selective reporting and other bias often unclear. No funnel plot or Egger test (fewer than 10 studies). Sensitivity: leave-one-out did not change direction or significance. PROSPERO registered 8 April 2026, after the review had commenced. |

### Sub-table: included RCTs (n=9)

| First author | Year | Substance | Target | Protocol (per Table 1) | N (E/C; total) |
|---|---|---|---|---|---|
| Chen et al. (ref 23) | NR | Methamphetamine | L-DLPFC (Beam F3) | 20 sessions/4 weeks; 900 pulses/session; 100% RMT; 50-Hz triplets at 5 Hz; 2 s on/8 s off | 30/19; 49 |
| Dieler et al. (ref 24) | NR | Nicotine | R-DLPFC (F4) | 4 sessions over 2 weeks; 600 pulses/session; 80% MT; 50-Hz triplets at 5 Hz | 38/36; 74 |
| Durazzo et al. (ref 25) | NR | Alcohol | L-DLPFC (Beam F3) | 20 sessions in ≤14 days; 1,200 pulses/session; 100–110% aMT; 50-Hz triplets at 5 Hz | 22/22; 44 |
| Mikellides et al. (ref 26) | NR | Nicotine | L-DLPFC (Beam F3) | 20 sessions/5 days; 600 pulses/session; 100% RMT; 50-Hz triplets at 5 Hz; two active arms pooled | 59/30; 89 |
| Ren et al. (ref 27) | NR | Methamphetamine | L-DLPFC (F3) | 20 sessions/4 weeks (5/week); 600 pulses/session; 100% RMT; 2 s on/8 s off | 24/25; 49 |
| Su et al. (ref 28) | NR | Methamphetamine | L-DLPFC (F3) | 20 sessions/4 weeks; 900 pulses/session; 100% RMT; 2 s on/8 s off | 70/56; 126 |
| Su et al. (ref 29) | NR | Methamphetamine | L-DLPFC (Beam F3) | 20 sessions/4 weeks; 900 pulses/session; 100% RMT; 2 s on/8 s off | 25/25; 50 |
| Addicott et al. (ref 17) | NR | Nicotine | mPFC (AFz) | 28 sessions over 14 visits; 600 pulses/session; 110% RMT | 25/13; 38 |
| Chen et al. (ref 22) | NR | Methamphetamine | L-DLPFC (active arm) | 10 sessions/2 weeks; 900 pulses/session; 100% RMT; 2 s on/8 s off | 18/19; 37 |

Total N = 556 (matches the review). Year NR for each trial: the paper states only that trials were published 2014 to 2025. Craving analysis excludes Durazzo (n=44), giving 512.

*Extractor's caveat note:* A reader of the abstract alone could take away that iTBS reduces craving across substance use disorders. The pooled SMD of −0.65 is heterogeneous (I² = 81%) and is driven by methamphetamine (SMD −1.03, 5 trials). The nicotine craving estimate is null (SMD 0.01), and the paper says the overall pooled estimate should not be read as a single expected effect for all SUDs. The abstinence OR of 2.19 comes from only 3 small trials that pool nicotine and alcohol, with short follow-up (mostly 4 weeks or less). It is preliminary and does not show sustained abstinence or relapse prevention. The methamphetamine evidence is mostly from Chinese trials, the allocation concealment was often unclear, publication bias could not be formally tested, and the PROSPERO registration came after the review had started. The paper also reports no adverse-event data in the synthesis.

### 2. Treiber M, Tsapakis EM, Fountoulakis K. rTMS for alcohol craving in AUD: a meta-analysis. J Addict Med 2025;19(2):195-201. doi:10.1097/ADM.0000000000001416. PMID 39665462

Source: PubMed abstract (no PMC copy) | Tag: **ABSTRACT** | Quotes verified: 12/12

**What this changes in the cloud pack:** Confirms SMD -0.79 (-1.53 to -0.04), I2 93%, 12 studies, n=475. The 3-month result (SMD -0.44, CI -0.77 to 0.11, reported as P < 0.01) is internally inconsistent because its CI crosses zero. Do not cite it as evidence of durability. The included-studies sub-table needs the paywalled full text.

| Field | Extracted |
|---|---|
| Design | Systematic review and random-effects meta-analysis of randomized controlled trials (abstract only) |
| N | 475 participants across treatment and control groups; 12 studies |
| Population and timing after detox | Alcohol use disorder; timing after detoxification NR |
| Stimulation or intervention parameters (target, localisation, frequency/TBS pattern, intensity %RMT, pulses/session, sessions, schedule) | Multiple-session rTMS, at least 10 sessions required for inclusion; targets analysed as medial prefrontal cortex, right DLPFC, left DLPFC; frequency, TBS pattern, %RMT, pulses/session and schedule NR |
| Sham/control method | Sham stimulation (active rTMS vs sham); sham procedure details NR |
| Primary outcome and instrument | Alcohol craving; instrument NR |
| Primary result with effect size and CI | Immediately post-treatment, active rTMS vs sham: SMD = -0.79, 95% CI -1.53 to -0.04, P = 0.04, I2 = 93% |
| Secondary results | 3-month follow-up: SMD = -0.44, 95% CI -0.77 to 0.11, P < 0.01, I2 = 38% (described as medium effect). Immediate subgroups: medial PFC SMD = -2.12 (95% CI -4.34 to 0.09, P = 0.06, I2 = 94%); right DLPFC SMD = -1.04 (95% CI -2.56 to 0.48, P = 0.18, I2 = 96%); left DLPFC SMD = -0.27 (95% CI -0.60 to 0.05, P = 0.10, I2 = 0%) |
| Follow-up | Immediately post-treatment and up to 3 months |
| Adverse events | NR |
| Risk-of-bias notes | NR in abstract. Abstract reports I2 heterogeneity of 93% immediately post-treatment and 38% at 3 months; subgroup CIs cross zero |

| Comparison (immediate post-treatment) | SMD | 95% CI | P | I2 |
|---|---|---|---|---|
| Overall | -0.79 | -1.53 to -0.04 | 0.04 | 93% |
| Medial PFC | -2.12 | -4.34 to 0.09 | 0.06 | 94% |
| Right DLPFC | -1.04 | -2.56 to 0.48 | 0.18 | 96% |
| Left DLPFC | -0.27 | -0.60 to 0.05 | 0.10 | 0% |

| Timepoint | SMD | 95% CI | P | I2 |
|---|---|---|---|---|
| 3-month follow-up | -0.44 | -0.77 to 0.11 | <0.01 | 38% |

Included-studies list: NR (abstract only).

*Extractor's caveat note:* A reader relying on the abstract may take away that rTMS clearly reduces craving and that the effect lasts 3 months. The immediate overall effect is significant (P = 0.04) but its CI is wide and heterogeneity is very high (I2 = 93%). The 3-month effect is labelled a 'medium effect' with P < 0.01, yet its CI (-0.77 to 0.11) includes zero, so the reported significance and the 'sustained' conclusion are internally inconsistent and should be checked in the full text. The medial PFC 'may be more effective' claim rests on subgroup CIs that all cross zero, with high heterogeneity and few studies per subgroup, so the abstract itself calls it limited evidence. The abstract gives no stimulation protocol details, sham methods, craving instrument, adverse events or risk-of-bias assessment, so these columns are NR.

### 3. Hoven M, Schluter RS, Schellekens AF, van Holst RJ, Goudriaan AE. Effects of 10 add-on HF-rTMS sessions on alcohol use and craving among detoxified inpatients with AUD: a randomized sham-controlled clinical trial. Addiction 2023;118(1). doi:10.1111/add.16025

Source: PMC10087396 | Tag: **FULLTEXT** | Quotes verified: 27/27

**What this changes in the cloud pack:** The null holds on every outcome: abstinent days, relapse (HR 0.90, 0.55-1.48) and grams consumed. **Timing:** eligibility was up to 4 months after detox, and the exact detox-to-first-session interval is not reported. **No benzodiazepine policy is reported**; the paper gives only sedative use yes/no at baseline (3 active, 1 sham). The pack's timing argument (`02-lane1` gaps, item 2) should say "post-detox, interval unreported, up to 4 months". The authors' ceiling explanation (high TAU response, low craving) supports enriching the sample for SADQ >= 31.

| Field | Extracted |
|---|---|
| Design | Single-centre, single-blind, sham-controlled, parallel-group RCT, randomised 1:1 to TAU plus active or sham HF-rTMS; follow-up at 3 and 6 months (with 12-month treatment success). Trial registration: Netherlands Trial Register NTR 5291. |
| N | 80 randomised (40 active, 40 sham); 100 screened, 82 included, 2 withdrew consent before start. |
| Population and timing after detox | Detoxified, abstinent adult AUD inpatients at Jellinek Addiction Treatment Centre, Amsterdam; age 20–65, recent DSM-IV alcohol dependence (less than 4 months after detoxification). Recruitment March 2016 to February 2019. Exact interval from detox to first rTMS session NR; first rTMS session was on day 1 of the 10 consecutive work-day treatment block (after baseline assessments). Mean age 44.35 years (abstract); 20 females. |
| Stimulation or intervention parameters (target, localisation, frequency/TBS pattern, intensity %RMT, pulses/session, sessions, schedule) | Target: right DLPFC, localised at F4 by 10–20 EEG system. Pattern: 60 trains of 10 Hz, each 5 s, at 110% motor threshold (resting MT from 5/10 thumb abductor responses). Coil: 70-mm double air film coil, Magstim Rapid2. Sessions: 10 on 10 consecutive work-days (once per day). Derived, not reported by authors: 50 pulses per train x 60 trains = 3000 pulses per session. Inter-train interval NR. Add-on to TAU (CBT or ACT, plus some anti-craving/antidepressant/sedative medication). |
| Sham/control method | Identical procedure and stimulation parameters with the coil tilted 90° relative to the scalp. Authors note sham does not replicate somatosensory effects of stimulation. |
| Primary outcome and instrument | Total number of abstinent days over 6-month follow-up (days 1–180 after final session), from summed Timeline Follow-Back (TLFB) at 3 and 6 months. Primary analysis: Poisson generalised mixed model; missing data imputed as immediate relapse (zero abstinent days). |
| Primary result with effect size and CI | Abstinent days (ITT, missing = relapse): active 115 ± 69.8, sham 124 ± 65.9; difference 9 days. Poisson ratio (active vs sham) 1.421, 95% CI 0.578–3.547, P = 0.436 (Wald Z 0.779). Complete-case: active 152 ± 41.3, sham 158 ± 30.6 days; ratio 0.936 (0.775–1.128), P = 0.477. Bayesian 95% credible interval for difference (−0.13, 0.26). No significant group effect. |
| Secondary results | Relapse (time to first heavy drinking day, Cox model): HR 0.9014 (0.5476–1.484), P = 0.683; complete case HR 1.0935 (0.615–1.945), P = 0.761. Grams of alcohol (linear mixed model): group effect 820.15 (SE 1160.53; 95% CI −1449.28 to 3089.59; P = 0.482); time effect 1071.86 (95% CI 94.95 to 2048.89; P = 0.036); group x time −535.61 (95% CI −1897.54 to 802.81; P = 0.439). Complete-case Mann–Whitney U = 437.50, P = 0.599, effect size 0.0587 (−0.176 to 0.271). Craving: AUQ and OCDS mixed models with no significant group, time or interaction effects (AUQ group effect −3.531, 95% CI −9.147 to 2.066, P = 0.215; OCDS group effect 0.488, P = 0.615). Additional: full abstinence ITT 9/40 active vs 7/40 sham, χ2 = 0.078, P = 0.7799 (V = 0.031); complete-case χ2 = 0.088, P = 0.767. Treatment success at 12 months (OR 1.242, 95% CI 0.450–3.469, P = 0.815 ITT; complete case OR 1.520, 0.213–12.366, P = 0.691). |
| Follow-up | Telephone contact at 3 months (90 days), 6 months (180 days) and 12 months (360 days) after final session; craving questionnaires not collected at later re-contact. Missing-data counts: 9 incomplete (active), 13 incomplete (sham) for primary outcome. |
| Adverse events | Side effects by checklist plus free text. Sham group reported more headache (χ2(1) = 4.477, P = 0.034); active group reported more uncomfortable sensation at stimulation site (χ2(1) = 4.407, P = 0.036). Other side effects (pain or beep in ear, tiredness, etc.) not significantly different; no serious AE reported in the main text (NR). |
| Risk-of-bias notes | Single-blind (patients only); blinding test showed 63.2% correct guesses (binomial P = 0.038), above chance. Primary analysis assumed worst case (missing = relapse), with complete-case sensitivity analyses. Missing data assumed MAR. Outcomes self-reported by telephone TLFB. Sample size not formally powered (no proper power analysis; based on craving-trial effect size). Authors note possible ceiling effect from high TAU response and low craving, plus anti-craving medication in 27 of 80 patients. Sham coil does not mimic somatosensory effects. Pre-registered protocol. Randomisation concealed via Castor EDC, stratified by anti-craving medication and age. |

### Extra task A: Relapse and grams-consumed secondary results

| Outcome | Analysis | Result | 95% CI | P |
|---|---|---|---|---|
| Time to first relapse (heavy drinking day) | Cox, ITT (missing = immediate relapse) | HR 0.9014 | 0.5476–1.484 | 0.683 |
| Time to first relapse | Cox, complete case | HR 1.0935 | 0.615–1.945 | 0.761 |
| Grams of alcohol, group effect | Linear mixed model | 820.15 (SE 1160.53) | −1449.28 to 3089.59 | 0.482 |
| Grams of alcohol, time effect | Linear mixed model | 1071.86 (SE 498.66) | 94.95 to 2048.89 | 0.036 |
| Grams of alcohol, group x time | Linear mixed model | −535.61 (SE 687.52) | −1897.54 to 802.81 | 0.439 |
| Grams of alcohol, total 6 months | Mann–Whitney, complete case | U = 437.50; effect size 0.0587 | −0.176 to 0.271 | 0.599 |

Relapse definition: heavy drinking day (>60 g/day men; >40 g/day women). Censoring: non-relapsers censored at 180 days; lost-to-follow-up assigned relapse at day 0 (no follow-up) or day 90 (missing only at 6 months) in ITT.

### Extra task B: Benzodiazepine policy

Benzodiazepine policy: NR. The paper reports only 'Sedative medication (yes/no)' at baseline (active 3/37; sham 1/39). It does not name benzodiazepines or describe a prescribing or tapering policy.

### Extra task C: Timing of first rTMS relative to detox

- Eligibility window: recent DSM-IV alcohol dependence, less than 4 months after detoxification.
- Patients were abstinent and inpatients at recruitment.
- First rTMS session: day 1 of the 10 consecutive work-day block, after baseline questionnaires and motor threshold/location determination.
- Exact days or weeks from detox to first rTMS: NR.


*Extractor's caveat note:* A reader relying only on the abstract would see the primary null result and the 9-day difference, but might miss that the 95% CI is reported as a Poisson ratio (0.578–3.547) on a log-link scale, not in days, and that the primary analysis imputed relapse for all missing participants. The conclusion that there is 'no clear evidence' of a benefit is correct but does not mean HF-rTMS was shown to be ineffective; the authors note a possible ceiling effect from high TAU response and low craving, and the study was not formally powered. Relapse time and grams consumed were secondary and non-significant, but grams showed a significant time effect in both arms, which the abstract does not mention. Sham blinding was imperfect (63.2% correct guesses), and sham differed in somatosensory sensations, so any blinding bias would tend to inflate apparent active effects rather than mask them.

### 4. Belgers M, et al. rTMS reduces craving and alcohol use in AUD: randomized sham-controlled trial (MDPI journal, 2022). PMC8878126

Source: PMC8878126 | Tag: **FULLTEXT** | Quotes verified: 36/36

**What this changes in the cloud pack:** **Correct the pack.** 34 were randomised and 30 started treatment, and the arm sizes differ between the abstract and Table 1. Patients entered within 6 weeks of inpatient detox. The trial was single-blind. Craving showed a group x time effect (Wilks' lambda 0.348, p = 0.032), largest at 3 months. **At 12 months there was no effect on craving or abstinence**, even though the Discussion claims a one-year benefit. No effect sizes or CIs are reported. Cite it as a 3-month signal from a small single-blind trial.

| Field | Extracted |
|---|---|
| Design | Single-blind, randomized, sham-controlled trial of rTMS added to treatment as usual (TAU); 1:1 allocation with a computer-generated sequence |
| N | Randomized 34 (37 screened, 3 lost to contact). Four withdrew consent after baseline, leaving 30 who started treatment. Abstract gives rTMS n = 14 and sham n = 16. Table 1 gives rTMS+TAU n = 16 and TAU n = 18 (total 34), which is the pre-withdrawal allocation. The Results do not reconcile these figures. Analysed N for each group is therefore unclear. |
| Population and timing after detox | Adults aged 20 to 65 with DSM-5 AUD (SCID-5-CV) and recent (<6 weeks) inpatient alcohol detoxification. Recruited 2015 to 2019 at two addiction centres and Radboud UMC, Netherlands. All had six or more DSM-5 AUD criteria. Treatment started after detox (day 1 of rTMS). Follow-up at 1, 3 and 12 months after the last rTMS session. |
| Stimulation or intervention parameters (target, localisation, frequency/TBS pattern, intensity %RMT, pulses/session, sessions, schedule) | Target: right dlPFC at F4 (10-20 EEG system), marked on a cap relative to nasion-inion landmarks. Figure-of-eight coil, Magstim Rapid2. Motor threshold found over right motor cortex (5 of 10 stimuli producing contraction). Intensity 110% MT. Frequency 10 Hz; 60 trains of 5 s per session, i.e. 3000 pulses per session (30 min). Ten sessions on consecutive days (some interrupted over weekends, giving 10 to 14 days). Total 30,000 pulses. |
| Sham/control method | Sham coil: two-wing coil rotated 90 degrees from the scalp, so most field lines do not enter the skull; procedure and sound were preserved. Both groups received hearing sponges. Both arms received TAU (outpatient CBT and/or anti-craving medication). |
| Primary outcome and instrument | Alcohol craving (primary outcome), measured at baseline, end of treatment (day 10), and 1, 3 and 12 months after rTMS. Instruments: VAS (mean of two 0-100 mm items), Alcohol Urge Questionnaire (AUQ, 8 items, 7-point scale), and OCDS-5 (5 items, 0-4, past 7 days). Analysis: repeated-measures MANOVA, group x time interaction Wilks' Λ = 0.348, F(12,17) = 2.654, p = 0.032. No effect sizes or CIs were reported for this test. The Results say the group x time interaction was significant for all outcomes except OCDS-5 (univariate ANOVA); Table S1 is cited for these values but was not provided. |
| Primary result with effect size and CI | Significant group-by-time interaction on craving (Wilks' Λ = 0.348, p = 0.032). Less increase in craving over time in the rTMS group. Group-level differences were largest at 3 months. No CIs or effect sizes (e.g. partial eta-squared, Cohen's d) reported in text. Main effects: time Wilks' Λ = 0.203, F(12,17) = 5.575, p = 0.001; group Wilks' Λ = 0.585, F(3,26) = 6.156, p = 0.003. Degrees of freedom for group are not consistent with a 2-group x 4-timepoint design. |
| Secondary results | Alcohol use (six indices, MANOVA): group effect Λ = 0.46, F(5,24) = 5.6, p = 0.001 (Results); abstract gives Wilks' Λ = 0.44, F(6,23) = 4.9, p = 0.002. Post hoc: rTMS group consumed less alcohol (factor 1.86), fewer drinking days (average difference 40 DD) and fewer heavy drinking days (average difference 21 HDD). Percentage abstinence at endpoint did not differ between groups. Baseline: all had 0 g/day heavy drinking in both groups (Table 1). Univariate craving: VAS, AUQ showed time x group effects; OCDS-5 did not. |
| Follow-up | Up to 12 months (1, 3, and 12 months after last rTMS session; TLFB covering the previous month at each follow-up). The 12-month outcomes showed no effect of rTMS on craving or abstinence. The one patient with a missing 12-month measurement died (study-unrelated) after 5 months; LOCF was used. |
| Adverse events | No serious side effects reported or observed. Some participants found treatment uncomfortable because of muscle twitches around the eye. No numbers given. |
| Risk-of-bias notes | Single-blind (participants blinded); the investigator (first author) was not blinded to modality. Allocation sequence was computer-generated; concealment method NR. Small sample (n = 30 started), with no formal power calculation reported in the text. Unequal PTSD at baseline (sham group more PTSD, chi-square p = 0.002); sensitivity analysis without PTSD showed similar results. LOCF for missing data. Concomitant medication: benzodiazepines were largely tapered at detox, antipsychotics prescribed to 32% and not controlled for in follow-up. Sham may be discernible by patients, which the authors acknowledge. Sample counts and some statistical values are inconsistent between Abstract, Results and Table 1. Discussion states rTMS reduced craving and use over one year, contradicting the 12-month null result. |

### Sub-table: timepoints and outcomes

| Timepoint | Craving (VAS, AUQ, OCDS-5) | Alcohol use (TLFB or in-session report) |
|---|---|---|
| Baseline (day 1 rTMS) | Yes | Yes (self-report since last treatment) |
| Sessions 2 to 10 | Not stated | Yes (since last treatment) |
| End of treatment (day 10) | Yes | Not stated |
| 1 month | Yes | Yes (TLFB, past 1 month) |
| 3 months | Yes | Yes (TLFB, past 1 month) |
| 12 months | Yes (null effect) | Yes (TLFB, past 1 month; null for abstinence) |

### Reconciliation of N
- Screened 37; randomized 34; withdrew consent after baseline 4; started treatment 30.
- Abstract: rTMS 14, sham 16 (total 30).
- Table 1: rTMS+TAU 16, TAU 18 (total 34). Group labelled "TAU" in the table is the sham arm.

### Discrepancies in statistics
- Alcohol use MANOVA: Abstract Λ = 0.44, F(6,23) = 4.9, p = 0.002; Results Λ = 0.46, F(5,24) = 5.6, p = 0.001.
- Results list 364 days as time-to-relapse default for non-relapsers, consistent with a one-year window.

### Items NR
- Effect sizes and CIs for any outcome.
- Exact 12-month values for craving scales and alcohol indices (Table S4 cited but not supplied).
- Abstinence proportions by group.

*Extractor's caveat note:* An abstract-only reader would likely take away a clear, durable benefit of rTMS on craving and drinking over one year. The paper's 12-month results do not support that: there was no effect on craving or abstinence at 12 months, and group differences were most prominent at 3 months. The Discussion's statement that rTMS reduced craving and use over one year conflicts with its own Results. The trial is small (30 started; group sizes differ between the Abstract and Table 1), uses a single-blind design with an unblinded investigator, and has a baseline PTSD imbalance and LOCF imputation for one 12-month measurement. The OCDS-5 did not show the effect the other two craving instruments did, and abstinence at endpoint was not significantly different. Statistics are not identical across sections (alcohol-use Λ, F and df differ). No effect sizes or CIs are given, and the sham may have been partly discernible to participants. The safety signal was limited to eye-muscle twitches, with no serious adverse events reported.

### 5. Harel M, et al. Repetitive TMS in alcohol dependence: a randomized, double-blind, sham-controlled proof-of-concept trial targeting the medial prefrontal and anterior cingulate cortices. Biol Psychiatry 2022. doi:10.1016/j.biopsych.2021.11.020. PMID 35067356

Source: Abstract via Semantic Scholar (publisher PDF blocked) | Tag: **ABSTRACT** | Quotes verified: 13/13

**What this changes in the cloud pack:** Confirms n=51, the H7 coil, and %HDD 2.9 +/- 0.8 vs 10.6 +/- 1.9, p = .037 (the paper does not say whether +/- is SD or SEM; probably SEM). The abstract reports craving as lower but gives no numbers. EtG was a secondary outcome with no result in the abstract. Connectivity: decreased dACC-caudate and mPFC-sgACC resting-state connectivity. %RMT is not in the abstract. **Still unverified at full text**; get the PDF through the AIIMS library or from the author.

| Field | Extracted |
|---|---|
| Design | Double-blind, randomized, sham-controlled proof-of-concept trial (per abstract) |
| N | 51 randomized (total); arm sizes NR |
| Population and timing after detox | Recently abstinent, treatment-seeking patients with alcohol use disorder (moderate to severe). Time since last drink/detox at enrolment: NR |
| Stimulation or intervention parameters (target, localisation, frequency/TBS pattern, intensity %RMT, pulses/session, sessions, schedule) | Deep TMS (dTMS) with H7 coil; target: midline frontocortical areas including medial prefrontal cortex and anterior cingulate cortex. Pattern: 100 trains of 30 pulses at 10 Hz per session (= 3,000 pulses per session, derived). Intensity %RMT: NR. Schedule: 15 sessions over 3 weeks, then 5 sessions over 3 months of follow-up (20 sessions total, derived). Active vs sham allocation stated. |
| Sham/control method | Sham dTMS (described as sham control arm); sham method details NR |
| Primary outcome and instrument | Percentage of heavy drinking days (predefined primary outcome), assessed with timeline follow-back interviews |
| Primary result with effect size and CI | Percentage of heavy drinking days during follow-up lower in active vs sham: 2.9 ± 0.8% vs 10.6 ± 1.9%, p = .037. Effect size: NR. 95% CI: NR. Whether ± denotes SD or SEM: NR. |
| Secondary results | Craving (self-report) after treatment significantly lower in active vs sham (statistics NR). Ethyl glucuronide in urine: analysed as secondary outcome, result NR. Brain imaging: active dTMS associated with decreased resting-state functional connectivity of dorsal ACC with caudate nucleus, and decreased connectivity of mPFC to subgenual ACC (effect sizes, statistics, n NR). |
| Follow-up | Follow-up period of 3 months (five sessions over this period); craving measured after treatment (time point relative to end of treatment NR beyond 'after treatment') |
| Adverse events | NR |
| Risk-of-bias notes | Abstract only; allocation concealment, blinding success, assessor blinding, attrition, ITT handling, and missing-data methods NR. Proof-of-concept scale with 51 participants. Primary and secondary outcomes reported with a single p-value and no CI in abstract. Full text required to assess. |

### Abstract-only extraction sub-table

| Domain | What the abstract gives | Status |
|---|---|---|
| Heavy drinking days (%HDD) | 2.9 ± 0.8% (active) vs 10.6 ± 1.9% (sham), p = .037; measured by timeline follow-back | Reported; CI/effect size NR |
| Craving | Lower in active vs sham after treatment (significant) | Direction and significance only; numbers NR |
| Biomarkers | Ethyl glucuronide (EtG) in urine listed as secondary | Results NR |
| Connectivity | Decreased dACC–caudate; decreased mPFC–subgenual ACC (active dTMS) | Direction only; statistics NR |
| H7 coil parameters | H7 coil; 100 trains × 30 pulses at 10 Hz per session; 15 sessions/3 weeks + 5 sessions/3 months | Intensity %RMT, coil placement method, and sham method NR |
| Sample | 51 randomized | Arm sizes NR |

*Extractor's caveat note:* A reader relying only on the abstract would get the direction of the main result right but would not have an effect size, confidence interval, or arm sizes. The single p = .037 is the only inferential statistic given for %heavy drinking days, and the ± values are not identified as SD or SEM. Craving is reported as significantly lower after treatment without numbers, and the EtG and connectivity findings lack statistics. The 'persistent changes in brain network activity' conclusion rests on a connectivity finding with no reported effect size, and the abstract calls the study a proof-of-concept trial with 51 participants, so the evidence is preliminary. The abstract also does not give intensity (%RMT), sham method, adverse events, or blinding procedures, all of which must come from the full text.

### 6. Zhao J-N, et al. Neural response to theta-burst stimulation predicts long-term relapse in AUD (right-DLPFC cTBS pilot, 2026). PMC12791151

Source: PMC12791151 | Tag: **FULLTEXT** | Quotes verified: 27/27

**What this changes in the cloud pack:** Confirms n=28 (16/12) and HR 0.210 (0.070-0.633), adjusted for sex, age and PSS-10. Protocol: cTBS, 600 pulses at **100% RMT** over F4, 10 sessions in 2 weeks, double-blind with a perpendicular-coil sham. **The relapse definition is soft**: drinking severity similar to or worse than before treatment, assessed by phone. Baseline AUDIT differed between groups. Patients came from a detox clinic, but the detox-to-session interval is not reported. `02-lane1` RQ3 should mention the soft definition and the imbalance.

| Field | Extracted |
|---|---|
| Design | Single-centre, randomized, double-blind, sham-controlled pilot trial with pre/post fMRI cue-reactivity and 12-month telephone relapse follow-up; ChiCTR2200065453 |
| N | 28 randomized (16 active cTBS, 12 sham); 2 observations excluded from Cox analysis for loss to follow-up |
| Population and timing after detox | Adults aged 18-60 with DSM-5 AUD recruited from the alcohol detoxification clinic of the First Specialized Hospital of Harbin. Exclusions: current acute withdrawal or severe withdrawal, epilepsy/seizure disorder, TMS/MRI contraindications, severe psychiatric illness or intellectual disability. Intervention delivered over two weeks; time from detox to first session NR. Relapse contacts at 1, 3, 6, 9 and 12 months after treatment completion. |
| Stimulation or intervention parameters (target, localisation, frequency/TBS pattern, intensity %RMT, pulses/session, sessions, schedule) | Inhibitory cTBS to right DLPFC, localised by F4 (International 10-20 EEG) scalp landmark; fig. 8 cooling coil; 3-pulse bursts at 50 Hz repeated at 5 Hz theta; 100% of individual RMT; 600 pulses over 40 s per session; 10 sessions, one per weekday over two consecutive weeks. RMT defined as minimum output giving MEP of at least 50 μV in 5 of 10 trials from APB hotspot. |
| Sham/control method | Same F4 location with coil oriented perpendicular (90°) to scalp; reproduces device sound and scalp sensation without effective field penetrating skull. Schedule and procedures identical across groups. |
| Primary outcome and instrument | Time to relapse (Cox proportional hazards), relapse defined as drinking returning to preintervention level or worse, assessed by telephone. Neural primary/secondary analysis: group-by-intervention interaction on cue-reactivity beta maps in right superior frontal gyrus (repeated-measures ANOVA). Subjective craving outcome was hypothesized but its result is NR in the text. |
| Primary result with effect size and CI | Relapse (12-month follow-up): HR = 0.210, 95% CI [0.070, 0.633], p = 0.006 (active vs sham). Log-rank p = 0.017. rSFG group x intervention interaction F = 4.347, p = 0.047 (no effect size or CI reported). Machine-learning relapse prediction: accuracy 78.7%, AUC 0.903 (no CI reported). |
| Secondary results | Kaplan-Meier curves show lower relapse rate in active group. Sham group showed increased rSFG activity postintervention; active group stable. Strongest ML predictor: increase in left medial frontal cortex cue reactivity (posttest minus baseline); hippocampus and right supramarginal gyrus also contributed. Baseline AUDIT differed between groups (33.13 vs 25.17, p = 0.024). Craving and other clinical secondary outcomes NR. |
| Follow-up | 12 months after treatment completion (telephone contacts at 1, 3, 6, 9, 12 months). Time between intervention end and post-fMRI NR. |
| Adverse events | NR |
| Risk-of-bias notes | Double-blind with sham; blinding check asked participants to rate belief in active vs sham after final session (result NR). Small n (28), single centre, unequal groups (16 vs 12), baseline AUDIT imbalance, Cox model adjusted for sex, age, PSS-10 with 2 exclusions for loss to follow-up, no multiplicity correction described, machine-learning validation scheme not described, rSFG result p = 0.047. Relapse ascertainment by telephone only. Funding: none reported. Data on request only. |

### Full parameters
| Item | Detail |
|---|---|
| Device | Certified magnetic stimulator, fig. 8 cooling coil (Wuhan Yiruide) |
| Target | Right DLPFC, F4 landmark |
| Pattern | cTBS: 3 pulses per burst at 50 Hz, bursts at 5 Hz, 600 pulses, 40 s |
| Intensity | 100% individual RMT |
| Sessions | 10, one per weekday, two weeks |
| RMT | Minimum output for MEP ≥50 μV in 5/10 trials, APB |
| Imaging | 3T GE MR750, EPI TR/TE 2000/45 ms, 32 slices 4 mm; FMRIPREP 24.1.0; 2 mm voxels, 6 mm FWHM smoothing; block design 3×30 s per condition |

### Blinding
Randomized, double-blind, sham-controlled. Sham used perpendicular coil orientation. Post-final-session belief rating collected; results NR.

### Relapse definition
Drinking severity returning to a level similar to or worse than preintervention, ascertained by telephone at 1, 3, 6, 9, 12 months after treatment completion. Exact operational thresholds (e.g., drinks/day, AUDIT cut-off) NR.

### 12-month relapse hazard ratio
HR = 0.210, 95% CI [0.070, 0.633], p = 0.006 (active vs sham, Cox model adjusted for sex, age, PSS-10). Log-rank p = 0.017. Proportional hazards assumption check NR.

*Extractor's caveat note:* A reader of the abstract alone may assume a robust, well-powered clinical effect and a validated biomarker. In fact the HR (0.210, CI 0.070-0.633) comes from 28 patients in a single-centre pilot, with 2 excluded for loss to follow-up, and the log-rank test was only p = 0.017. The neural group-by-time effect in the right superior frontal gyrus is marginal (F = 4.347, p = 0.047) and reported without effect size or CI. The 78.7% accuracy and AUC 0.903 come from a machine-learning model whose validation scheme (cross-validation, held-out data) is not described in the text, so the prediction should be treated as exploratory. The abstract's 'prevented cue-induced hyperactivity' is a description of a sham-group increase rather than a demonstrated suppression below baseline. The hypothesized craving reduction is not reported in the results, and the groups differed at baseline on AUDIT.

### 7. Rakesh G, Adams TG, Ballard DH, McLouth CJ, Rush CR. Theta burst stimulation in methamphetamine use disorder: meta-analysis and systematic review. 2025. PMID 40757793

Source: PubMed abstract | Tag: **ABSTRACT** | Quotes verified: 6/6

**What this changes in the cloud pack:** Confirms SMD 1.04 (0.16-1.92) for cue-induced craving, from **only 4 sham RCTs**. The outcome is craving, not use.

| Field | Extracted |
|---|---|
| Design | Systematic review and meta-analysis of randomized controlled trials (RCTs); abstract reports a meta-analysis of four RCTs with sham control and a narrative review of two RCTs without sham arms |
| N | NR |
| Population and timing after detox | Adults with methamphetamine use disorder (MUD); time since detoxification NR |
| Stimulation or intervention parameters (target, localisation, frequency/TBS pattern, intensity %RMT, pulses/session, sessions, schedule) | Target: NR for reviewed trials (abstract background mentions left dlPFC for prior TMS studies only). Protocols: intermittent TBS (iTBS) in the meta-analysis; accelerated iTBS in one non-sham trial; continuous TBS (cTBS) mentioned as not yet reviewed. Intensity, pulses, sessions and schedule NR |
| Sham/control method | Sham iTBS (four RCTs in the meta-analysis); two additional RCTs had no sham control arm. Sham method details NR |
| Primary outcome and instrument | Cue-induced methamphetamine craving; instrument NR |
| Primary result with effect size and CI | iTBS more effective than sham iTBS in reducing cue-induced craving: SMD in change = 1.04; 95% CI [0.16, 1.92] |
| Secondary results | In one of the two non-sham RCTs, accelerated iTBS produced a significant reduction in craving. Other secondary outcomes NR |
| Follow-up | NR |
| Adverse events | NR |
| Risk-of-bias notes | Abstract states the search covered PubMed/Medline, EMBASE and Google Scholar to September 1, 2024, and that prior meta-analyses included overlapping cohorts whereas this review used unique patient cohorts. Formal risk-of-bias assessment NR in abstract. Only four RCTs contributed to the pooled estimate; no abstract data on heterogeneity or publication bias |

Sub-tables not produced: the abstract gives only the pooled SMD for four sham-controlled iTBS RCTs and one narrative result for accelerated iTBS. Per-study data, cTBS findings and other outcomes are NR in the abstract.

*Extractor's caveat note:* A reader relying on the abstract could take the conclusion that TBS is effective for MUD as firmly established. The pooled result rests on only four sham-controlled iTBS RCTs, with a wide CI (0.16 to 1.92) and no abstract detail on sample sizes, heterogeneity or risk of bias. The two non-sham trials are not pooled, and only one of them showed a significant craving reduction, following accelerated iTBS. The outcome is cue-induced craving, not methamphetamine use or return to use. cTBS and frontal pole targeting are described only as future directions. The abstract does not report protocol parameters, so the target and dose cannot be verified from it.

### 8. Living SR/MA: effectiveness of NIBS protocols on drug craving and consumption/relapse in SUD, 208 trials and 36 protocols. medRxiv doi:10.1101/2025.09.21.25335559 (v1 21 Sep 2025; v2 1 Apr 2026)

Source: medRxiv API abstract (full text behind Cloudflare) | Tag: **ABSTRACT** | Quotes verified: 11/11

**What this changes in the cloud pack:** **Not peer-reviewed as of 5 Nov 2026** (the bioRxiv API shows v2, published = NA). The abstract gives **no alcohol-specific ranking and no dose-response result**. Protocol order: H4 deep TMS first (single study, g 3.92), then HF rTMS to left DLPFC (craving g 0.66, consumption 0.52), then bilateral tDCS. Pooled TMS: craving g 0.52, consumption 0.41. Do not use it to choose an alcohol protocol until the full text or supplement is read.

| Field | Extracted |
|---|---|
| Design | Living systematic review and meta-analysis (abstract only). Controlled trials up to January 1, 2024; 116 randomized sham-controlled trials eligible for meta-analysis after risk-of-bias screening. |
| N | 208 trials in the systematic review (121 TMS, 86 tES, 1 tFUS); 116 randomized sham-controlled trials (59 TMS, 57 tES) in meta-analysis. Participants: 5,106 in active and 4,914 in sham groups. |
| Population and timing after detox | Participants with any type of substance use disorder (all SUD types). Timing after detoxification: NR. |
| Stimulation or intervention parameters (target, localisation, frequency/TBS pattern, intensity %RMT, pulses/session, sessions, schedule) | Abstract reports protocol-level subgroups only: high-frequency deep TMS with H4 coil (maximum electric field over frontopolar cortex; single study); high-frequency rTMS over left DLPFC; bilateral anodal-right cathodal-left tDCS over DLPFC (maximum field on frontopolar cortex); anodal-left cathodal-right tDCS over DLPFC. Intensity (%RMT), pulses per session, number of sessions and schedule: NR. 36 different protocols examined in total. |
| Sham/control method | Sham-controlled trials (sham method NR in abstract). |
| Primary outcome and instrument | Drug craving and consumption/relapse. Instruments: NR. |
| Primary result with effect size and CI | TMS: craving g = 0.52 (95% CI 0.29-0.75), I² = 89.36%; consumption g = 0.41 (95% CI 0.26-0.56), I² = 61.56%. tES: craving g = 0.40 (95% CI 0.25-0.55), I² = 60.69%; consumption g = 0.27 (95% CI 0.15-0.38), I² = 22.67%. Pooled effects by modality only; CIs for protocol-level results NR. |
| Secondary results | Protocol subgroups (g craving and consumption, p-values only, no CIs in abstract): H4 deep TMS g = 3.92 and 1.12 (p < 0.001, single study); high-frequency rTMS left DLPFC g = 0.66 and 0.52 (p < 0.05); bilateral anodal-right cathodal-left tDCS g = 0.49 and 0.42 (p < 0.0001); anodal-left cathodal-right tDCS g = 0.38 and 0.31 (p < 0.05). Alcohol-specific results: NR. Dose-response analysis: NR. |
| Follow-up | NR |
| Adverse events | NR |
| Risk-of-bias notes | Only trials judged low risk of bias were meta-analysed (abstract wording: 'due to a low risk of bias'). Tool and per-domain ratings NR. Very high heterogeneity for TMS craving (I² = 89.36%). H4 estimate based on a single study. Living-review update schedule NR. |

### Protocol rankings (abstract only)

**Alcohol-specific ranking:** None. The abstract does not report any alcohol-specific protocol ranking or alcohol subgroup. It refers only to 'all types of SUD'.

**Dose-response finding:** None. The abstract mentions 'varying stimulation parameters' but reports no dose-response or parameter-dependence analysis.

**Ranking as reported (drug craving / consumption, Hedges' g, abstract values):**

| Rank | Protocol | Craving g | Consumption g | p (abstract) | Notes |
|---|---|---|---|---|---|
| 1 | High-frequency deep TMS, H4 coil (frontopolar max field) | 3.92 | 1.12 | <0.001 | Single study; no CI given |
| 2 | High-frequency rTMS, left DLPFC | 0.66 | 0.52 | <0.05 | No CI given |
| 3 | Bilateral anodal-right cathodal-left tDCS, DLPFC | 0.49 | 0.42 | <0.0001 | No CI given |
| 4 | Anodal-left cathodal-right tDCS, DLPFC | 0.38 | 0.31 | <0.05 | No CI given |

The abstract gives no protocol-level CIs, no heterogeneity statistics, and no comparison test between protocols. Ranks are the abstract's ordering by effect size, not a formal comparison.

*Extractor's caveat note:* A reader using only the abstract may take the H4 deep TMS result (g = 3.92 craving, 1.12 consumption) as a robust best protocol. It comes from a single study, has no CI, and sits far above every other estimate, so it should be treated as provisional. The abstract also reports no alcohol-specific ranking or dose-response analysis, so it cannot be used to choose an alcohol protocol. The modality-level results (TMS and tES, with CIs) are the more reliable findings. The abstract does not state the risk-of-bias tool, follow-up, adverse events, or stimulation details (intensity, pulses, sessions). Its conclusion that frontopolar and DLPFC stimulation produce medium to large effects is framed by the authors as requiring replication. Heterogeneity is high for TMS craving (I² = 89.36%).

### 9. Rossi S, Antal A, Bestmann S, et al. Safety and recommendations for TMS use in healthy subjects and patient populations, with updates on training, ethical and regulatory issues: expert guidelines. Clin Neurophysiol 2021;132:269-306. doi:10.1016/j.clinph.2020.10.003

Source: PMC9094636 | Tag: **FULLTEXT** | Quotes verified: 26/26

**What this changes in the cloud pack:** **The guideline gives no quantified seizure risk for alcohol, alcohol withdrawal or benzodiazepines.** It lists alcohol withdrawal as a provoking factor and asks investigators to document alcohol intake. It notes six alcohol-associated seizures in psychiatric H1-coil cases. For TBS, it calls 80-100% RMT the usual range and judges that range safe; the first TBS seizure was cTBS to M1 at 100% RMT. Protocols beyond Suppl. Table S5 should follow its section 6.1. Implication: accelerated iTBS **during** withdrawal is outside what Rossi explicitly covers. Start after CIWA-Ar < 10 and the benzodiazepine taper, record benzodiazepine dose, and keep intensity at or below 100% RMT rather than 110-120%.

| Field | Extracted |
|---|---|
| Design | n/a (guideline) |
| N | n/a (guideline) |
| Population and timing after detox | n/a (guideline) |
| Stimulation or intervention parameters (target, localisation, frequency/TBS pattern, intensity %RMT, pulses/session, sessions, schedule) | n/a (guideline) |
| Sham/control method | n/a (guideline) |
| Primary outcome and instrument | n/a (guideline) |
| Primary result with effect size and CI | n/a (guideline) |
| Secondary results | n/a (guideline) |
| Follow-up | n/a (guideline) |
| Adverse events | n/a (guideline) |
| Risk-of-bias notes | n/a (guideline) |

## Extra task: verbatim passages (guideline, not a trial)

### Alcohol and alcohol withdrawal
| Section | Verbatim passage |
|---|---|
| Drugs | "...alcohol consumption, marijuana therapeutic and recreational use" (seizure-threshold factors) |
| Drugs (Recommendation) | "documentation of concurrent intake of drugs and other potentially seizure threshold lowering factors (such as sleep deprivation, infection, alcohol consumption) during TMS application" |
| General factors relevant to TMS-provoked seizure | "Common provoking factors that might be relevant to subjects receiving TMS include sleep deprivation, stress, depression/anxiety, increased alcohol consumption, and menses" |
| Medical factors relevant to TMS-provoked seizure | "alcohol withdrawal; use of stimulants such as cocaine or MDMA" |
| Neuropsychiatric disease | "having alcoholism or drug abuse"; "An elevated risk of developing seizures has also been reported in other neuropsychiatric diseases such as schizophrenia or autism, bipolar disorder and alcohol abuse." |
| Neurology and rehabilitation | "one had stroke and alcohol withdrawal syndrome"; cases were 8 seizures among 10 AE cases (no alcohol-specific rate given) |
| Psychiatry | "substance consumption (e.g. alcohol, caffeine)"; "reported alcohol consumption in six and poor sleep in two patients who had a seizure during H1 coil rTMS" |
| TBS (safety limits section) | "cocaine users or alcohol-dependent volunteers without incident" (protocol: 6 trains of cTBS at 110% RMT) |
| Ethics: vulnerable populations | "alcohol or drug use disorders, stroke or traumatic brain injury" (heightened seizure risk groups) |

No quantified alcohol-specific seizure rate or threshold for alcohol withdrawal is reported in the text.

### Benzodiazepines
| Section | Verbatim passage |
|---|---|
| Psychiatry | "A sub-manic activation syndrome ... likely accounts for the majority of cases where concomitant benzodiazepines or hypnotic medications were initiated as allowed in large regulatory RCTs." |

No benzodiazepine-specific seizure risk estimate is given.

### Theta-burst safety limits (pulse counts and intensities)
| Section | Verbatim passage |
|---|---|
| Patterned rTMS: TBS | Original Huang et al. parameters: "50 Hz bursts of 3 pulses repeated at 5 Hz; stimulus intensity of 80% AMT". Only one seizure reported with these parameters: "To the best of our knowledge, there has only been one seizure reported using these parameters." |
| Patterned rTMS: TBS | "The other seizures reported using TBS have used parameters that exceed these levels." |
| Patterned rTMS: TBS | "The first seizure was reported by in a healthy individual after cTBS to M1 delivered at an intensity of 100% RMT." |
| Patterned rTMS: TBS | Survey-reported range: "parameters of TBS are quite standard among studies, ranging between 80–100% of RMT"; exceptions at 110% and 120% RMT are noted in the same passage (Supplemental Table S5, not in text). |
| Patterned rTMS: TBS | "Based on these data, it can be concluded that TBS in this range is safe." |
| Patterned rTMS: TBS | "For future clinical trials exceeding the parameters of Supplemental Material, Table S5, the same recommendations suggested in the paragraph 6.1 should be followed." |
| Psychiatry | iTBS accelerated protocol: "iTBS has been applied in an accelerated fashion with five sessions per day and 1620 pulses per session in 54 triplet bursts (2 s. on, 8 s. off) or with a marked higher stimulation intensity of 120% RMT." |
| Psychiatry | "it cannot be concluded that higher intensity or stimuli numbers are superior to standard iTBS at 80% RMT or AMT" |
| Seizures: rate | "Specifically, for iTBS, the risk to induce seizures is very low." |

### Conventional rTMS ceiling (reference point, not TBS-specific)
| Section | Verbatim passage |
|---|---|
| Update of safety tables | "Clearly, the parameters of stimulation used for MST should not be exceeded." Lowest seizure-inducing MST parameters: "frequency of 25 Hz, delivered in a single train lasting up to 10 s". Conventional rTMS must stay "well below this combination of parameters." |
| Experimental/Pulse sequences | Original safety table range: "significantly exceeded the range (10 pulses at 5 Hz) of the original safety tables" (80-pulse 5 Hz train with asymmetric monophasic pulses) |

### Notes
- The text does not give an explicit numeric safe pulse-count or intensity ceiling for TBS. The 'safe' statement is inferred from survey-reported parameters and is expert opinion.
- Supplemental Tables S2, S3 and S5 are cited but not in the supplied text.

*Extractor's caveat note:* A reader relying on the abstract would see only that seizure risk is low and that traditional parameters are safe, with no alcohol, benzodiazepine or TBS detail. The full text gives no quantified seizure risk for alcohol, alcohol withdrawal or benzodiazepines. Alcohol appears only as a listed provoking factor (with case counts such as six alcohol-associated seizures in H1-coil psychiatric cases) and as a recommendation to document intake. Benzodiazepines appear only in the context of a sub-manic activation syndrome that likely explains why they were started in trials; no causal or safety rate is given. For TBS, the text reports that most studies used 50 Hz bursts of 3 pulses at 5 Hz and 80% AMT, that one seizure followed these parameters, and that seizures followed cTBS at 100% RMT and at 110% RMT in other reports. It then calls 80–100% RMT 'safe' based on a supplementary table that is not in the supplied text. The 1620-pulse accelerated iTBS regimen at 120% RMT is described as not shown to be superior, with no explicit safety ceiling. All recommendations are expert opinion, the text states that a formal rating of evidence was not possible, and the seizure survey has reporting biases and no denominators for many subgroups.

### 10. Ekhtiari H, Tavakoli H, Addolorato G, et al. Transcranial electrical and magnetic stimulation (tES and TMS) for addiction medicine: a consensus paper on the present state of the science and the road ahead. Neurosci Biobehav Rev 2019;104:118-140. doi:10.1016/j.neubiorev.2019.06.007

Source: PMC7293143 | Tag: **FULLTEXT** | Quotes verified: 29/29

**What this changes in the cloud pack:** A consensus paper, not a meta-analysis: a descriptive review of 84 studies with no pooled effects. Its recommendations on target, timing, sham and outcomes are in the detail block. In `06-sources`, change "Not retrieved" to "read".

| Field | Extracted |
|---|---|
| Design | n/a (consensus) |
| N | n/a (consensus) |
| Population and timing after detox | n/a (consensus) |
| Stimulation or intervention parameters (target, localisation, frequency/TBS pattern, intensity %RMT, pulses/session, sessions, schedule) | n/a (consensus) |
| Sham/control method | n/a (consensus) |
| Primary outcome and instrument | n/a (consensus) |
| Primary result with effect size and CI | n/a (consensus) |
| Secondary results | n/a (consensus) |
| Follow-up | n/a (consensus) |
| Adverse events | n/a (consensus) |
| Risk-of-bias notes | n/a (consensus) |

### Consensus recommendations (target, timing, sham, outcome measures)

Quote IDs refer to the `quotes` array. The paper gives no pooled effect sizes and no fixed protocol; recommendations are qualitative.

| Domain | Recommendation | Supporting quote |
|---|---|---|
| Target | Use focal manipulation of networks dysregulated in the individual's SUD subtype; the authors frame this as a direction for future work, not a validated rule. | Q3 |
| Target | Define the target location and how it was found (neuronavigation or not) for TMS; for tES, state montage, electrode number, and how the montage was determined. | Q28, Q29 |
| Target | Approach laterality from a network perspective, where target location matters as well as side. | Q4 |
| Target | Future work should personalise treatment and optimise parameters. | Q27 |
| Timing | Systematic comparison of repetition intervals is missing and is needed to set repetition rates and durations. | Q5 |
| Timing | Target both acute craving and withdrawal early in abstinence, as the relapse-critical period is the first few days. | Q6 |
| Timing | Timing of intervention may be critical; the paper distinguishes pretreatment, detoxification and long-term recovery. | Q7 |
| Timing | Neuromodulation should be an adjunct to behavioural treatment; psychotherapy may serve as add-on long-term therapy. | Q25, Q26 |
| Sham | tES sham: short ramp-in/ramp-out of 10–30 s to mimic cutaneous sensation (duration varies across studies). | Q8 |
| Sham | TMS sham: electrical pulse time-locked to TMS to mimic scalp muscle sensation; experienced participants may still discriminate active from sham. | Q9, Q10 |
| Sham | Avoid crossover designs at intensities of 2 mA or more because of unblinding risk. | Q11 |
| Sham | Measure and report blinding success for participants and staff; define sham methods for TMS (sham coil, tilted coil, metal plate). | Q12, Q13 |
| Outcomes | Consumption is the reference endpoint for FDA-approved SUD drugs; pair self-report with biomarkers repeated according to each biomarker's dissipation rate. | Q14, Q15 |
| Outcomes | Timeline follow-back is the gold-standard self-report of days of use (example window 30 days), with the caveat that it relies on self-report. | Q16 |
| Outcomes | Longitudinal studies should include at least a 3-month follow-up. | Q17 |
| Outcomes | Craving/cue-reactivity studies should include a biologic metric as well as self-report. | Q18 |
| Outcomes | Single-item VAS craving scales are debated (face validity without clear content or predictive validity). | Q19 |
| Outcomes | Cognitive and behavioural markers suggested: Go/No-Go, N-Back, Delay Discounting, TSST, among others. | Q20 |
| Outcomes | Functional/health correlates suggested: SIP-AD, WHOQOL-BREF, SF-36. | Q21 |
| Outcomes | Measures should meet validity, reliability and responsiveness criteria and be defined a priori. | Q22, Q23 |
| Outcomes | Multimodal biomarkers (fMRI plus EEG) are suggested for a fuller mechanistic picture. | Q24 |

*Extractor's caveat note:* A reader relying on the abstract alone may assume this is a pooled evidence synthesis with effect sizes that supports clinical use of tES/TMS in addiction. It is not. The paper is a consensus document with a descriptive literature review of 84 tDCS/rTMS studies, and it explicitly gives no pooled effect sizes or confidence intervals. The paper states that the number of studies and trials is the same (n = 84), and that few stimulation parameters have been systematically studied in addiction. Its recommendations on target, timing, sham and outcomes are expert suggestions, several framed as needs or future directions, and the abstract's 'guidelines for best practices' are not empirical validation. The authors also note that many SUD NIBS studies have small samples, weak controls and inadequate blinding, and that no published multisite RCTs for addiction existed at the time of the search. The abstract's mention of 'three meta-analyses' showing promise is cited as background only, not re-analysed.

### 11. Keogan S, Li S, Clancy L. Allen Carr's Easyway to Stop Smoking - a randomised clinical trial. Tob Control 2019;28(4):414-419. doi:10.1136/tobaccocontrol-2018-054243

Source: PMC6589447 | Tag: **FULLTEXT** | Quotes verified: 19/19

**What this changes in the cloud pack:** ITT CO-validated quit rates, AC vs Quit.ie: 37.7 vs 20.1% at 1 month; 26.5 vs 14.8% at 3 months (aOR 2.26, 1.22-4.21); 23.2 vs 15.4% at 6 months (p = 0.045); 21.9 vs 11.4% at 12 months. **Under complete-case analysis none of the CO-validated differences were significant**, and retention was low (101/300 at 12 months). Seminar: 5 hours, up to 20 people, smoking continues until a ritual final cigarette, then 20 minutes of relaxation, two free follow-ups, no pharmacotherapy. Add the ITT-only caveat to `03-lane2` section 1.

| Field | Extracted |
|---|---|
| Design | Single-centre, open, parallel-group, randomised superiority trial (CONSORT cited); block randomisation by gender, age and education; ITT primary analysis with complete-case analysis (CCA) as secondary. |
| N | 300 randomised (AC n=151; Quit.ie n=149); all 300 included in ITT denominators. |
| Population and timing after detox | Adult smokers aged 18+, smoking at least 5 cigarettes/day, English-speaking, recruited by advertisement (July 2015–Feb 2016). Excluded: doctor-diagnosed acute cardiac/respiratory or serious psychiatric illness, current treatment for alcohol/illicit drug use. No detox phase described; quit date set at registration (Quit.ie) or at seminar. Follow-up at 1, 3, 6, 12 months. |
| Stimulation or intervention parameters (target, localisation, frequency/TBS pattern, intensity %RMT, pulses/session, sessions, schedule) | Not applicable (no neuromodulation). AC arm: free 5-hour group seminar (max 20 participants) delivered by experienced AC therapists; smoking continued until a ritual final cigarette, then 20-min relaxation; two free AC follow-ups; no pharmacotherapy permitted. Comparator Quit.ie: online/phone national service, see extra. Schedule: AC one seminar; Quit.ie quit plan with daily texts/emails for 1 month, at least two further follow-ups, one counselling call. |
| Sham/control method | No sham. Active comparator: Quit.ie (HSE National Online Smoking Cessation Service). Medication in Quit.ie at client's discretion; AC participants instructed not to use pharmacotherapy. |
| Primary outcome and instrument | Pre-specified primary aim: CO-validated (Russell standard) quit status at 3 months (self-report confirmed by breath CO, Care fusion CO monitor). Dichotomous outcomes analysed by multivariable logistic regression. |
| Primary result with effect size and CI | 3-month ITT CO-validated quit rate, AC 26.5% (40/151) vs Quit.ie 14.8% (22/149), p=0.006 (Table 2 decimals; abstract rounds to 27% vs 15%). Adjusted logistic regression AC vs Quit.ie OR 2.26 (95% CI 1.22 to 4.21), p=0.01. |
| Secondary results | ITT CO-validated quit rates AC vs Quit.ie: 1 month 37.7% vs 20.1% (p<0.001); 6 months 23.2% vs 15.4% (p=0.045); 12 months 21.9% vs 11.4% (p=0.008). CCA CO-validated: no significant differences (1 m p=0.139; 3 m p=0.433; 6 m p=0.778; 12 m p=0.228). CCA self-report significant at all visits (p=0.002, 0.008, 0.025, 0.013). Retention significantly higher in AC. Weight gain among quitters at 3 m 3.8 kg AC vs 1.8 kg Quit.ie; at 12 m 5.02 vs 3.18 kg (p=0.15, NS). Education and baseline CO associated with quitting; OR for higher vs lower education 3.62 (95% CI 1.58 to 8.28). |
| Follow-up | Visits at 1, 3, 6 and 12 months (plus initial visit). Retained: 179, 127, 113, 101 participants at 1, 3, 6, 12 months. Electronic follow-up of non-attenders for CCA. |
| Adverse events | Only reported adverse effect: one AC participant visited her doctor for withdrawal symptoms. Authors state AC was well tolerated. Two serious-illness participants and three pregnant women were removed from weight analysis. |
| Risk-of-bias notes | Open-label; comparator is a different service, so no blinding of participants/therapists. High attrition, notably in Quit.ie (retention 179 of 300 at 1 month). ITT treats missing as failure to quit, which is conservative. Only one-tailed tests used for proportion comparisons (stated as superiority test). Recruitment via self-selected volunteers, mainly white Irish/UK, well people. Funding from DOH Ireland. Competing interest: LC has advisory roles and past research grants from Pfizer. Sample size assumed 25% vs 12% at 3 months, a larger difference than observed. |

## Quit rates per arm (ITT, CO-validated / Russell standard, from Table 2)

| Timepoint | AC quitters/N | AC rate | 95% CI | Quit.ie quitters/N | Quit.ie rate | 95% CI | p |
|---|---|---|---|---|---|---|---|
| 1 month | 57/151 | 37.7% | NR | 30/149 | 20.1% | NR | <0.001 |
| 3 months | 40/151 | 26.5% | NR | 22/149 | 14.8% | NR | 0.006 |
| 6 months | 35/151 | 23.2% | NR | 23/149 | 15.4% | NR | 0.045 |
| 12 months | 33/151 | 21.9% | NR | 17/149 | 11.4% | NR | 0.008 |

CIs for individual quit rates are not reported in the supplied text (NR). The only CI given is for the OR (2.26; 1.22–4.21).

Abstract-rounded values (AC 38/27/23/22%; Quit.ie 20/15/15/11%) agree with the table except that the abstract's 3-month and 6-month figures are rounded.

**Discrepancy:** Discussion states AC 26% and Quit.ie 11% at 12 months. Table 2 gives AC 21.9% (33/151), so the Discussion figure does not match the table.

## Verification method
- Quit status: self-report at each visit, validated by breath CO using a Care fusion CO monitor (Russell standard). Quote: 'validation by CO Breath test was carried out at each visit using a CO monitor'.
- Non-attenders: contacted by email/text/phone and self-reported status used in CCA and self-report ITT. CO validation not possible for them.
- Missing = failure: all missing quit data counted as not quit in ITT.
- Self-report ITT (not CO-validated) rates are also in Table 2 (e.g., 3 m: AC 31.8%, Quit.ie 17.5%).

## Seminar description (AC arm)
Free of charge, delivered by experienced AC therapists. 5-hour group seminar, maximum 20 participants, in a routine session. Participants smoke during smoking breaks until a ritualistic final cigarette, then a 20-minute relaxation exercise. Two free AC follow-ups available. No pharmacotherapy; not based on transtheoretical model per authors; no apps, texts, calls or social media component.

## Comparator description (Quit.ie arm)
Quit.ie is the HSE National Online Smoking Cessation Service, delivered free. Accredited NCSCT practitioners provide information and behavioural support by phone, text, online and via a Facebook community. Participants set a quit date, received daily support texts/emails for 1 month, at least two further follow-up communications, and a counselling phone call from a quit specialist. Medication use was the client's choice (NRT, varenicline or none); face-to-face sessions were available on request but were not requested.

*Extractor's caveat note:* A reader of the abstract alone would miss several caveats. The superiority claim rests on ITT with CO-validated quits. Under CCA with CO validation none of the timepoint differences were significant (p=0.139 to 0.778). The 6-month ITT difference is borderline (p=0.045). The 'AC superior at all timepoints' statement is therefore true only for ITT. Retention was low (179/300 at 1 month, 101 at 12 months), especially in Quit.ie, and missing data were counted as failures. The comparator is a different service, not a placebo or sham, and the trial was open-label. The Discussion's 26% AC 12-month rate conflicts with Table 2 (21.9%). The abstract's 'all AC quit rates were superior' is consistent with ITT only. The primary OR of 2.26 is from a multivariable model that adjusted for baseline CO and education. Weight gain differences were significant at 1, 3 and 6 months but not 12 months, and only among quitters. The trial was single-centre in Dublin with a self-selected, mainly white, middle-aged sample, and the sample-size assumption (25% vs 12%) was larger than the observed effect.

### 12. Frings D, Albery IP, Moss AC, et al. Comparison of Allen Carr's Easyway programme with a specialist behavioural and pharmacological smoking cessation support service: a randomized controlled trial. Addiction 2020;115(5):977-985. doi:10.1111/add.14897

Source: PMC7186816 | Tag: **FULLTEXT** | Quotes verified: 42/42

**What this changes in the cloud pack:** Verified 26-week abstinence 19.4 vs 14.8%: OR 1.38 (0.90-2.10), RD 4.5% (-1.4 to 10.4), Bayes factor 1.24 (inconclusive). Non-inferiority was shown only post hoc, with a 5% margin. Among people who attended treatment, **4-week abstinence favoured the NHS service** (33.7 vs 48.8%, p = 0.001). Allen Carr's Easyway funded the trial, with independent conduct by LSBU. About 28% were retained at 26 weeks.

| Field | Extracted |
|---|---|
| Design | Two-arm, parallel-group, single-blind randomized controlled trial in London, UK. Recruitment and first randomization 3 February 2017; last follow-up 25 May 2018. Analysis by intention to treat (missing smoking status assumed smoking). Registered NCT02855255, ISRCTN23584477, OSF t6vgs. |
| N | 620 randomized (310 ACE; 310 SSS). 468 attended treatment (255 ACE; 213 SSS). 100 completed 6-month measures (23.7% ACE vs 20.7% SSS of those attending). |
| Population and timing after detox | Adults aged 18 or older who were current smokers wanting to quit; mean age 40.8 years; 53.4% male. Excluded: pregnancy, mental health condition, respiratory disease, concurrent similar trial enrolment, unwillingness to use a non-NHS/NICE-approved service. Timing relative to quit or detox: NR beyond the quit date and session schedule (ACE participants were encouraged to keep smoking until the session). |
| Stimulation or intervention parameters (target, localisation, frequency/TBS pattern, intensity %RMT, pulses/session, sessions, schedule) | Not a neuromodulation study (no target, localisation, frequency, TBS, %RMT or pulses). ACE: one group session of 4.5-6 h combining CBT elements with a brief relaxation exercise; scheduled smoking breaks every 45-60 min and a final ritual cigarette; one therapist per group (7 therapists; mean 8.95 participants per group); SMS follow-up; up to two top-up sessions of about 3.5 h (face-to-face or online) within 12 weeks. SSS (NHS-standard service): one 30-minute session combining motivational interviewing and CBT; up to four follow-up sessions (brief 10-minute checks at 1, 2, 3 and 4 weeks post quit date); NRT via voucher or varenicline via GP letter; medication for up to 12 weeks; delivered by four therapists, sessions available 5 days a week. |
| Sham/control method | No sham. Active comparator was the specialist SSS providing behavioural and pharmacological support. Participants were blind to the treatment not received; treatment staff were not blind; the statistician/randomizer was the only person with access to allocation before final analysis. |
| Primary outcome and instrument | Self-reported continuous abstinence from quit/re-set date to 26 weeks (no more than 5 cigarettes in total), verified by exhaled breath CO < 10 p.p.m. (Russell Standard). Those not confirmed (including lost to follow-up) counted as failures. |
| Primary result with effect size and CI | Verified 26-week continuous abstinence 19.4% (60/310) ACE vs 14.8% (46/310) SSS; risk difference 4.5% (95% CI -1.4 to 10.4%); OR 1.38 (95% CI 0.90 to 2.10); Pearson chi-square P = 0.165; Bayes factor 1.24 (described by authors as non-conclusive). Post hoc, with a 5% non-inferiority limit, the lower CI bound (-1.4) lies within the margin (-5). |
| Secondary results | Verified abstinence at 4 weeks 27.7% vs 33.5%, OR 0.76 (0.54-1.07), RD -5.8% (-13.0 to 1.5%), P = 0.139. At 12 weeks 21.6% vs 21.9%, OR 0.98 (0.67-1.44), RD -0.3% (-6.8 to 6.2%). Among treatment attenders only: 4 weeks 33.7% vs 48.8% (P = 0.001, favouring SSS); 12 weeks 26.3% vs 31.9%; 26 weeks 23.5% vs 20.7%, OR 1.18 (0.75-1.85), RD 2.9%. Treatment attendance 82.3% ACE vs 68.7% SSS, OR 2.11 (1.45-3.08), RD 13.6%, P < 0.001. Pharmacotherapy use: 47.8% of ACE vs 95.7% of SSS completed study with aid use reported, OR 0.01 (0.00-0.07); pharmacotherapy-free at 26 weeks 83.5% vs 40.4%, OR 7.59 (3.71-15.52). Sensitivity analyses (re-set participants counted as non-abstainers at 12 and 26 weeks) found no significant difference. Quit efficacy (self-efficacy) was measured but follow-up results are NR. |
| Follow-up | Assessments at 4, 12 and 26 weeks. Retention at 26 weeks: 29% ACE and 28% SSS (48.7% of randomized participants overall accounted for at 6 months). |
| Adverse events | Only one question was asked: whether new medical issues might be due to the quit. Results of adverse events are NR. |
| Risk-of-bias notes | Single-blind; treatment staff not blinded; high attrition (51.3% lost to follow-up, with assumed smoking in the ITT); unequal attendance (82.3% vs 68.7%) with differing service structures (ACE offered at two sites, SSS at one); self-report verified by CO only (no cotinine); participants able to use funded or purchased aids in both arms; allocation concealed via independent randomizer with stratified block randomization; analysis protocol pre-registered on OSF; funded by ACE company (see extra); generalisability limited to a relatively healthy population. |

## Primary result with OR and CI
- Verified 26-week continuous abstinence, ITT: ACE 19.4% (60/310) vs SSS 14.8% (46/310).
- OR (ACE vs SSS) = 1.38, 95% CI 0.90 to 2.10 (logistic regression; table value). The CI includes 1.
- Risk difference 4.5% (95% CI -1.4 to 10.4%); chi-square P = 0.165; Bayes factor 1.24.
- The abstract gives the OR without its CI.

## All secondary outcomes
| Outcome | ACE | SSS | P | OR (95% CI) | RD (95% CI) |
|---|---|---|---|---|---|
| Verified abstinence 4 wk (ITT) | 27.7% (86/310) | 33.5% (104/310) | 0.139 | 0.76 (0.54-1.07) | -5.8% (-13.0 to 1.5) |
| Verified abstinence 12 wk (ITT) | 21.6% (67/310) | 21.9% (68/310) | 1.0 | 0.98 (0.67-1.44) | -0.3% (-6.8 to 6.2) |
| Verified abstinence 26 wk (ITT, primary) | 19.4% (60/310) | 14.8% (46/310) | 0.165 | 1.38 (0.90-2.10) | 4.5% (-1.4 to 10.4) |
| 4 wk, attenders only | 33.7% (86/255) | 48.8% (104/213) | 0.001 | 0.54 (0.37-0.79) | -15.1% (-24.1 to 5.9) |
| 12 wk, attenders only | 26.3% (67/255) | 31.9% (68/213) | 0.185 | 0.75 (0.50-1.13) | -5.7% (-14.9 to 2.9) |
| 26 wk, attenders only | 23.5% (60/255) | 20.7% (44/213) | 0.503 | 1.18 (0.75-1.85) | 2.9% (-5.1 to 10.6) |
| Attended treatment | 82.3% (255/310) | 68.7% (213/310) | <0.001 | 2.11 (1.45-3.08) | 13.6% (6.6 to 20.4) |
| Completed study, pharmacotherapy use (reported) | 47.8% (64/134) | 95.7% (154/161) | <0.001 | 0.01 (0.00-0.07) | -47.9% (-56.5 to -38.4) |
| Pharmacotherapy-free at 26 wk | 83.5% (76/91) | 40.4% (36/89) | <0.001 | 7.59 (3.71-15.52) | 43.1% (reported CI as 29.4 to -54.5, reversed) |

Post hoc non-inferiority (5% margin): lower CI bound -1.4 within -5. Authors state non-inferiority testing was not planned.

Attendance by site: 197 attended first session at LSBU and 58 at ACE London centre; no difference in primary outcome by site (chi-square 0.87, P = 0.351).

Top-ups: 36 ACE participants at LSBU, 32 at treatment centre and 22 online for first top-up; 15, 6 and 12 for a third session.

Re-sets: 82 participants re-set quit date (33 SSS; 49 ACE).

## Belief or mechanism measures
- Quit efficacy (four items, 7-point scale, 1 strongly disagree to 7 strongly agree), measured at baseline and at follow-ups. Baseline means: ACE 20.7 (SD 4.3), SSS 20.8 (SD 4.1), total 20.8 (SD 4.2). Follow-up quit efficacy results are NR.
- The ACE seminar targets positive expectancies about smoking; no outcome measure of beliefs or expectancies is reported.
- No mechanism measures are reported; the discussion notes qualitative data were absent.

## Description of seminar content
ACE session (4.5-6 h): facilitator helps participants recognise positive expectancies of smoking (pleasure, support) as a 'crutch', then moves them toward the conclusion that beliefs about smoking being beneficial are harmful. Participants are taught how psychological and pharmacological mechanisms of nicotine addiction maintain a problematic belief system. Elements of CBT; brief relaxation exercise at end; scheduled smoking breaks every 45-60 minutes; final 'ritual' cigarette; participants smoke as usual before attending. Post-session SMS messages from the clinical team. Top-ups (about 3.5 h) broadly follow the same format.

## Funder role and ACE organisation involvement
- Funding was provided by Allen Carr's Easyway International Ltd. The funder had no role in study design, data collection, analysis, interpretation or report writing.
- Declaration of interests: design, conduct, data collection, analysis and interpretation were by London South Bank University, independent of ACE (International) Ltd. ACE had no veto over publication but received advance notice of findings.
- The SSS was provided by Lambeth NHS Stop Smoking Service.
- Authors' mitigation steps: expert peer review of protocol, independent steering committee, pre-registered analysis on OSF.

*Extractor's caveat note:* A reader relying on the abstract could take away that ACE and the specialist service are equally effective, but the trial found only that the difference was not statistically significant. The 26-week OR of 1.38 is reported without its CI (0.90-2.10, which includes 1), the Bayes factor of 1.24 is weak and described as non-conclusive, and the abstract omits that SSS had higher 4-week abstinence among attenders and that both arms had heavy loss to follow-up (only 29% and 28% retained at 26 weeks, with missing counted as smoking). The abstract's attendance P value (< 0.05) conflicts with the table (< 0.001), and the pharmacotherapy-free percentages in the text (83.3% and 40.1%) differ from the table (83.5% and 40.4%), with a reversed CI for the risk difference. The non-inferiority conclusion is post hoc, and the study was funded by the company that delivers ACE, although the authors state it had no role in design or analysis and no veto over publication. The comparator was an NHS service that included pharmacotherapy, so the trial compares ACE's pharmacotherapy-free approach against an aid-based approach, and the 'pharmacotherapy' results should not be read as a cessation-efficacy finding.

### 12. Wood CE, et al. Protocol for an RCT of Allen Carr's Easyway vs NHS stop smoking service. BMJ Open 2017;7:e016867. doi:10.1136/bmjopen-2017-016867

Source: PMC5735399 | Tag: **FULLTEXT** | Quotes verified: 24/26

**What this changes in the cloud pack:** Seminar content per the protocol: 5-6 hours, up to 25 attendees, CBT elements, about 20 minutes of hypnotherapy or relaxation, and two optional top-up sessions. Two of 26 quotes (the sample-size and participant-payment lines) did not match the text and are listed as unverified below.

| Field | Extracted |
|---|---|
| Design | Protocol for a two-arm, parallel-group, blinded randomised controlled trial. Randomisation is stratified on four factors (nicotine dependence, prior quit attempts, age, gender) and the allocation ratio is 1:1. Researchers are blinded to condition. Therapists are not blinded. No no-treatment control. |
| N | Planned, not analysed: initial sample of 620 (310 per arm). No results reported. |
| Population and timing after detox | People who smoke tobacco cigarettes, aged at least 18, motivated to quit. Excluded: self-reported mental health condition, pregnancy, respiratory disease (COPD or emphysema), preference for NHS treatment, other concurrent RCT, inability to reach the treatment site. Timing: recruitment and intervention start February 2017, running for 8 months. Assessments at baseline, 4, 12 and 26 weeks. No detox phase is described (NR). |
| Stimulation or intervention parameters (target, localisation, frequency/TBS pattern, intensity %RMT, pulses/session, sessions, schedule) | Not applicable (behavioural/pharmacological intervention, not neurostimulation). ACE: single group session (up to 25 attendees), 5–6 hours, CBT elements, ends with about 20 min hypnotherapy/relaxation; optional top-up of two further sessions (about 3.5 hours, up to 15 clients, face-to-face or online) within 3 months. NHS: single session about 30 min (motivational interviewing and CBT), then four follow-up sessions (about 10 min each at 1, 2, 3 and 4 weeks after quit date), with NRT of patient choice including varenicline. |
| Sham/control method | No sham. Comparator is the NHS stop-smoking service (active comparator). No no-treatment control. |
| Primary outcome and instrument | Sustained abstinence at 26 weeks from quit date, defined by Russell 6 Standard (fewer than five smoking incidents), with breath CO confirmation of quits. Lost to follow-up counted as failure (intention to treat). |
| Primary result with effect size and CI | Not reported (protocol). Planned analysis: logistic regression of treatment condition on cessation at 26 weeks, with 95% CIs. |
| Secondary results | Not reported (protocol). Planned at 4, 12 and 26 weeks: self-reported abstinence, NRT/nicotine product use, perceived value of being nicotine free, life satisfaction, quit efficacy, readiness to change (1–10), adverse events. |
| Follow-up | Assessments at 4, 12 and 26 weeks after quit date. Primary endpoint 26 weeks. |
| Adverse events | Adverse events are to be recorded as a secondary outcome (relation to treatment). No results reported. |
| Risk-of-bias notes | Researchers blinded but therapists not blinded. Sponsor is ACE, which funds the trial; the protocol states LSBU has independent conduct and publication authority. Top-up and reset procedures may alter the smoke-free clock between arms; authors acknowledge this and plan a sensitivity analysis. Missing data are to be replaced by condition mean. Sample size assumes 25% loss to follow-up, while 30% attrition is also cited. Stratified randomisation via CAR software by a statistician. |

## Extra task: protocol summary

**Seminar content (ACE arm).** The paper does not use the word "seminar"; the ACE arm is a single group session (up to 25 attendees, 5–6 hours) led by a trained facilitator. Content: CBT elements; participants are encouraged to smoke normally until the clinic and during scheduled breaks (about every 45–60 min); they identify positive expectancies of smoking and work toward recognising those beliefs as erroneous and harmful; they learn how the psychological and pharmacological mechanisms of nicotine addiction sustain these beliefs; a 'ritual' final cigarette is followed by about 20 min of hypnotherapy/relaxation; each participant writes down what made them want to stop. Follow-up contacts (call, email or SMS) occur on days 1, 3, 7, 10, 14, 21, 30, 45, 60, 75 and 90.

**NHS arm content (comparator).** About 30 min session combining motivational interviewing and CBT: assessment, nicotine dependence and withdrawal education, NRT options, quit date within 2 weeks, CO test, high-risk situation planning. Four follow-up sessions (about 10 min each) at 1, 2, 3 and 4 weeks after quit date.

**Planned outcomes.** Primary: sustained abstinence at 26 weeks (Russell 6 Standard, CO-verified; lost to follow-up = failure). Secondary (4, 12, 26 weeks): self-reported cessation, NRT and nicotine product use, perceived value of nicotine-free status, life satisfaction, quit efficacy, readiness to change, adverse events. Sensitivity analyses at 4 and 12 weeks, and at 12/26 weeks excluding those who reset or topped up.

**Verification method.** Self-report plus breath carbon monoxide (Smokerlyzer piCO) for confirmation of successful quits. Lost-to-follow-up participants are classed as failed quits.

**Funder.** Trial fully funded by Allen Carr's Easyway (International) Ltd. The paper states that LSBU conducts the trial independently, has ultimate publication authority, and that ACE has no veto but receives advance notice of findings.

*Extractor's caveat note:* This is a protocol with no results, so an abstract-only reader could mistake planned sample sizes, analyses or the intended comparison for findings. The trial compares ACE against the NHS stop-smoking service rather than a no-treatment control, and therapists are not blinded, so the blinding claim is partial. The trial is funded by Allen Carr's Easyway, which is a potential conflict of interest, although the protocol describes an independent LSBU conduct and publication arrangement. Failure to confirm quit status counts as a failed quit, and top-ups or resets restart the smoke-free clock, which could differ between arms. Study authorship, year and journal are not given in the provided text.

Unverified quotes:
- sample of 480 for 30% vs 50% success: "a sample of 480 would be required"
- Payment of £15 per measurement point: "Participants will be paid £15 cash for attending each measurement point"

### 13. Systematic review of Allen Carr's Easyway for smoking cessation. Tob Prev Cessat 2023. doi:10.18332/tpc/172314

Source: PMC10540232 | Tag: **FULLTEXT** | Quotes verified: 32/32

**What this changes in the cloud pack:** Six studies: two RCTs, the rest observational or case series. **No pooled estimate.** The 19-51% range mixes designs, and the OR of 6.52 (Dijkstra) comes from a non-randomised comparison. Use this review only to say the evidence is two RCTs, both in smoking.

| Field | Extracted |
|---|---|
| Design | Systematic review (PRISMA-guided) of RCTs and observational studies of the Allen Carr (AC) method for smoking cessation; PubMed/MEDLINE and Embase searched 29 March 2023. Six studies included: four observational (two case series, one quasi-experimental/observational study by Dijkstra et al., and Foshee et al. categorised as non-randomised) and two RCTs (Keogan et al. 2019; Frings et al. 2020). Note: the text describes Foshee et al. as an RCT in one place and as non-randomised in another. |
| N | Six included studies; sample sizes ranged from 92 to 620 participants. Per-study N: Hutter 2006 = 223 respondents (out of 308); Moshammer and Neuberger 2007 = 510 (out of 515); Dijkstra 2014 = 285 (124 AC vs 161 controls); Keogan 2019 = 300 (151 vs 149); Frings 2020 = 620 (310 vs 310); Foshee 2017 = 92 randomised (48 free book, 44 recommended), 52 analysed (34 read, 18 did not read). Review-level N for the systematic review itself: 34 records retrieved, 6 included. |
| Population and timing after detox | Population: adult smokers attending AC single-session seminars (workplace or community) or reading the AC book, including patients with head and neck disorders (Foshee). Pharmacotherapy-free method; detox/withdrawal timing not described as a separate element. Abstinence follow-up ranged from 4 weeks to 3 years across studies (Frings 4, 12, 26 weeks; Keogan 1, 3, 6, 12 months; Dijkstra 13 months; Hutter 1 year; Moshammer 3 years; Foshee 6 to 12 months). |
| Stimulation or intervention parameters (target, localisation, frequency/TBS pattern, intensity %RMT, pulses/session, sessions, schedule) | NR (not a neuromodulation study). Intervention description as reported in the review: AC single-session group seminar, typically 4 to 6 hours, small groups of about 20 or fewer, with up to two no-cost follow-up sessions. Keogan used a 5-hour seminar; Frings used 4.5 to 6 hours. AC book: 'The Easy Way to Stop Smoking' (free vs recommended purchase in Foshee). Comparators: no treatment or general-population controls (Dijkstra), Irish National online service 'Quit.ie' (Keogan), specialist Stop Smoking Service including NRT (Frings), no book reading (Foshee). |
| Sham/control method | NR at review level. Included-study controls: no treatment (Dijkstra); Quit.ie online service (Keogan); Stop Smoking Service with NRT (Frings); not reading the book (Foshee, randomised to free book vs recommended purchase). Hutter and Moshammer had no comparison group. |
| Primary outcome and instrument | Smoking cessation/abstinence rate (review-defined outcome: any measure of AC effectiveness). Verification: self-report, with cotinine testing (Moshammer subsample of 10; Dijkstra for those reporting abstinence) or breath tests (Keogan, Frings). No pooled effect estimate was calculated. |
| Primary result with effect size and CI | Cessation rates for AC seminar attendees ranged from 19% to 51% across included studies (unadjusted, heterogeneous designs). Dijkstra 2014 (observational): 13-month abstinence 41.1% vs 9.6%; multivariate adjusted OR 6.52 (95% CI 3.10–13.72). Keogan 2019 (RCT, AC seminar vs Quit.ie): 3-month AOR 2.26 (95% CI 1.22–4.21); quit rates at 1, 3, 6, 12 months 38, 27, 23, 22% vs 20, 15, 15, 11%. Frings 2020 (RCT, AC vs SSS+NRT): 26-week abstinence 19.4% vs 14.8%, risk difference 4.5% (95% CI -1.4 to 10.4), p=0.165. Foshee 2017 (book vs no book): 29.4% vs 33.3%, p=0.81; OR 0.83 (95% CI 0.24–2.84) per table. Hutter 2006: 1-year cessation 40% (55% when unknown status assumed same proportion of quitters). Moshammer 2007: 3-year cessation 51%. |
| Secondary results | Keogan: 1-month OR 2.36 (1.40–3.95); 6-month OR 1.65 (0.92–2.96); 1-year OR 2.17 (1.15–4.10) (table values). Keogan: mean weight gain at 3 months higher in AC group, 3.8 vs 1.8 kg (p<0.01), reported in Discussion. Foshee: book reading higher with free book (78% vs 52%; p=0.05). Frings secondary timepoints appear only in table (4 and 12 weeks). Review did not report pooled estimates or heterogeneity statistics. |
| Follow-up | Ranged from 4 weeks to 3 years across included studies (see Population row). Varies by study and is not uniform. |
| Adverse events | NR as a systematic outcome. Only adverse-type finding reported: higher mean weight gain at 3 months in the AC group in Keogan et al. (3.8 vs 1.8 kg). |
| Risk-of-bias notes | Tools: ROBINS-I for the quasi-experimental and non-randomised study (Dijkstra; Foshee); RoB 2 for two RCTs; JBI case-series checklist for two case-series studies, with 0–33% Yes = low, 34–66% = moderate, 67%+ = high. Ratings: Hutter and Moshammer moderate (case series); Dijkstra moderate; Foshee serious; Keogan and Frings 'some concerns' (missing outcome data). Two reviewers (IP, MS) independently assessed. Review protocol not registered in PROSPERO. Search limited to two databases; two non-English papers were excluded on language grounds. Small samples, heterogeneous AC application, and self-report verification were noted as limitations. |

### Included studies
| Author, year | Design | N | Comparator | Quit outcome |
|---|---|---|---|---|
| Hutter 2006 | Observational case series (Austria) | 223 of 308 | None (single arm) | 40% at 1 year; 55% if unknown status assumed same proportion quit |
| Moshammer & Neuberger 2007 | Observational case series (Austria) | 510 of 515 | None (single arm) | 51% at 3 years |
| Dijkstra 2014 | Observational (Netherlands) | 285 (124 vs 161) | No treatment (general population) | 41.1% vs 9.6% at 13 months; OR 6.52 (3.10–13.72) |
| Keogan 2019 | RCT (Ireland) | 300 (151 vs 149) | Quit.ie online national service | 38/27/23/22% vs 20/15/15/11% at 1/3/6/12 months; 3-mo OR 2.26 (1.22–4.21) |
| Frings 2020 | RCT (UK) | 620 (310 vs 310) | Specialist Stop Smoking Service incl. NRT | 19.4% vs 14.8% at 26 weeks; RD 4.5% (-1.4 to 10.4), p=0.165 |
| Foshee 2017 | Non-randomised study based on RCT allocation (USA) | 92 randomised; 52 analysed | Did not read AC book | 29.4% vs 33.3% at 6–12 months; p=0.81 |

### Risk of bias
| Study | Tool | Rating |
|---|---|---|
| Hutter 2006 | JBI case series | Moderate |
| Moshammer 2007 | JBI case series | Moderate |
| Dijkstra 2014 | ROBINS-I | Moderate |
| Foshee 2017 | ROBINS-I | Serious |
| Keogan 2019 | RoB 2 | Some concerns (missing outcome data) |
| Frings 2020 | RoB 2 | Some concerns (missing outcome data) |

### Authors' conclusions
AC seminars 'may be an effective intervention' and 'appear promising', but evidence is limited by small samples, few RCTs, heterogeneous delivery and some concerns in all studies. Evidence on the AC book is 'extremely poor' (one study, serious risk of bias).

### Method component description (as reported)
Group seminar, typically 4 to 6 hours, small groups (about 20 or fewer), facilitator-guided; up to two no-cost follow-up sessions; online courses, webinars and self-help materials; book 'The Easy Way to Stop Smoking'. Premise: smoking is addiction to relief from cigarettes rather than nicotine, so no pharmacotherapy is used.

*Extractor's caveat note:* A reader using only the abstract may take the 19% to 51% cessation range as evidence of effectiveness, but that range mixes unadjusted case series, a single-arm observational study and two RCTs, and no pooled estimate was computed. The abstract's OR of 6.52 comes from a non-randomised comparison with a general-population control group, and the text calls it a multivariate adjusted OR; it does not show the seminar works better than a randomised control. The OR of 2.26 is the 3-month adjusted estimate from Keogan et al.; the 1-month OR in the table is 2.36, and the abstract does not say which time point is reported. The abstract reports the Frings RCT only as 'no significant difference' against a specialist service that included NRT, but the Discussion then states that this null result 'supports the efficacy' of the seminar, which is an overreach. The abstract also omits that Keogan's AC group gained more weight (3.8 vs 1.8 kg), that the book study rated serious for risk of bias, and that Foshee et al. randomised 92 but analysed 52 participants. The paper is internally inconsistent in places: Foshee is described as an RCT and as non-randomised, and the Results say all included studies had 'some concerns' although one was rated serious and two moderate. Authors cite the NICE review as concluding that AC was 'as good as' comparators; this is a secondary claim, not a finding of this review. Overall, the review's own conclusion is hedged (promising, needs RCTs), and the abstract should be read with that in mind.

### 14. Herremans SC, et al. The impact of accelerated right prefrontal HF-rTMS on cue-reactivity: an fMRI study on craving in recently detoxified alcohol-dependent patients. PLoS One 2015. PMC4546410

Source: PMC4546410 | Tag: **FULLTEXT** | Quotes verified: 32/32

**What this changes in the cloud pack:** **This gives the timing the pack needs:** stimulation began a mean 17.8 days (SD 6.0) after the last drink, after diazepam detox. Protocol: 15 sessions over 3 days (Wednesday to Friday), 20 Hz, 110% RMT, 1560 pulses per session, MRI-guided right DLPFC. The treatment phase was open-label with no sham. General craving fell (OCDS, AUQ); cue-induced craving did not change.

| Field | Extracted |
|---|---|
| Design | Two-part fMRI study in one cohort. Part 1: single-session, randomised, single-blind, sham-controlled right DLPFC HF-rTMS (between-subjects, active vs sham, 13 per arm). Part 2: open-label accelerated protocol of 15 active sessions over 4 days, no sham arm. Each scan used a block and an event-related alcohol cue paradigm. |
| N | Twenty-six patients analysed for the single-session part (13 active, 13 sham). Treatment part: 23 completed (event paradigm) and 21 (block paradigm). Thirty-three consented; dropouts are listed in Methods. |
| Population and timing after detox | Recently detoxified, hospitalised alcohol-dependent patients aged 18 to 65. Detoxified with diazepam (CIWA-AR). Days between last alcohol intake and stimulation start: M = 17.8, SD = 6.0 (overall). Single-session part on Monday; treatment part Wednesday to Friday, with final scan the following Monday. |
| Stimulation or intervention parameters (target, localisation, frequency/TBS pattern, intensity %RMT, pulses/session, sessions, schedule) | Target: right DLPFC (Brodmann area 9/46), located by MRI non-stereotactic guidance. Figure-of-eight double 70 mm coil, tangential to skull. Frequency 20 Hz, 40 trains of 1.9 s, 12 s intertrain interval, 1560 pulses per session. Intensity 110% of resting MT. Treatment part: 15 sessions (4 Wed, 5 Thu, 5 Fri) with 15 min between sessions, 23,400 pulses total. Single-session part: one active or sham session on Monday, opposite condition on Tuesday. |
| Sham/control method | Sham: coil held at 90 degrees, resting on scalp with one edge. Patients wore earplugs and were blindfolded. Blinding was reported only for the single-session part (52.2% guessed allocation correctly). No sham arm in the treatment part. |
| Primary outcome and instrument | Cue-induced craving: verbal 0-10 Likert scale (TLS) before and after cue exposures. General craving: Alcohol Urge Questionnaire (AUQ) and 5-item Obsessive Compulsive Drinking Scale (OCDS), outside scanner. fMRI: alcohol minus neutral contrast, SPM8, TIME x STIMULATION interaction (single session) and paired t-test (treatment part). |
| Primary result with effect size and CI | Treatment part: general craving decreased on OCDS (Z = -2.41, P = 0.02) and AUQ (Z = -2.36, P = 0.02). Cue-induced TLS: Friedman X2(5) = 24.32, P = 0.001; post hoc, only first versus last scan comparisons were significant, all other TLS comparisons were not. Single session: no significant TLS change for active (X2(5) = 3.56, P = 0.61) or sham (X2(5) = 4.51, P = 0.48). No effect sizes or CIs reported for the primary results. |
| Secondary results | Single session, event paradigm: TIME x STIMULATION interaction in right insula (F = 14.48, Z = 3.34, cluster 131) and right BA 9 IFG (cluster 100). Active session increased right insula (cluster 49) and right precentral gyrus BA6 (cluster 68). Sham session decreased insula activity. Block paradigm: no significant clusters. Treatment part, block paradigm: no significant change. Treatment part, event paradigm: decreased activity in left inferior parietal lobule BA40 (MNI -44, -50, 40; cluster 1141; peak T = 5.09, Z = 4.09). No increases. |
| Follow-up | Single session: first post-stimulation scan about 20 minutes after stimulation. Treatment part: last scan three days after the final stimulation (Monday), craving and fMRI. No longer follow-up reported. |
| Adverse events | Stimulation well tolerated. Two patients had post-stimulation headache that resolved with oral analgesic. One patient dropped out after finding active stimulation too painful (single-session part). One patient dropped out due to movement artifacts. |
| Risk-of-bias notes | No placebo arm for the treatment part, so time effects cannot be excluded (authors state this). Small sample. Patients hospitalised and knew no alcohol would be available, which may have reduced craving induction. Blinding of principal investigators not present in single session; treatment part not blinded. Non-normal TLS data analysed non-parametrically. Power analysis used an ANOVA assumption (f = 0.25, total N = 20) rather than the non-parametric tests actually used. Benzodiazepine-free days differed between arms (P = 0.03). Heavy-drinking and other table values are inconsistently reported. Block-paradigm sample sizes differ from event sample sizes. Multiple cluster-level tests across paradigms. |

| Question | Parameters | Timing after detox | Craving outcome | fMRI findings |
|---|---|---|---|---|
| Accelerated treatment part | Right DLPFC (BA 9/46), 20 Hz, 110% RMT, 40 trains x 1.9 s, 12 s ITI, 1560 pulses/session, 15 sessions Wed-Fri (4/5/5), 15 min apart, 23,400 pulses | Hospitalised, recently detoxified; last scan about 3 days after last session | OCDS Z = -2.41, P = 0.02; AUQ Z = -2.36, P = 0.02 (decreased). TLS cue craving: no change between cue exposures; first vs last scan differences only | Event paradigm: decreased left IPL BA40 (cluster 1141). Block paradigm: NR change |
| Single sham-controlled session | Same target and parameters, one session, 13 active vs 13 sham | Same admission; scans about 20 min after stimulation | No significant TLS change in either group | Event paradigm: TIME x STIMULATION interaction in right insula and right IFG BA9; active increased insula and BA6; sham decreased insula. Block paradigm: NR |

*Extractor's caveat note:* A reader of the abstract could assume that accelerated right DLPFC HF-rTMS reduced craving. The abstract's significant result refers to general self-reported craving (AUQ and OCDS), obtained outside the scanner, in an open-label design with no sham arm, so time effects cannot be excluded. Cue-induced craving (TLS) was not clearly changed; the authors' own discussion says it was not influenced. The fMRI changes are narrow: after 15 sessions, only one left IPL cluster decreased, and only in the event-related paradigm; the block paradigm showed nothing. The single-session insula and BA6 increases were active-versus-sham interactions observed only in the event paradigm, and the abstract's statement about the 'default mode network' is an interpretation of the IPL cluster. Follow-up was three days, so delayed effects were not assessed, and the sample was small with blinding and non-normal data caveats.

### 15. Mishra BR, Nizamie SH, Das B, Praharaj SK. Efficacy of repetitive transcranial magnetic stimulation in alcohol dependence: a sham-controlled study. Addiction 2010;105(1):49-55. PMID 20078462

Source: PubMed abstract | Tag: **ABSTRACT** | Quotes verified: 13/13

**What this changes in the cloud pack:** n=45 with **2:1 allocation (30 active, 15 sham)**. Entry required CIWA-Ar <= 10. 10 Hz right DLPFC, 20 trains of 4.9 s, 10 sessions. ACQ-NOW interaction eta2 = 0.401. The abstract gives neither %RMT nor the sham method.

| Field | Extracted |
|---|---|
| Design | Prospective, single-blind, sham-controlled study. Allocation method and concealment NR. Abstract describes two-way repeated-measures ANOVA. |
| N | 45 randomised or allocated (abstract); 30 active rTMS, 15 sham. Dropouts and analysed N NR. |
| Population and timing after detox | Patients with alcohol dependence syndrome (ICD-10 DCR). Entry criterion: CIWA-Ar scores <=10. Time since last drink or detoxification timing NR. |
| Stimulation or intervention parameters (target, localisation, frequency/TBS pattern, intensity %RMT, pulses/session, sessions, schedule) | Target: right DLPFC. High-frequency rTMS at 10 Hz; 4.9 s per train; inter-train interval 30 s; 20 trains per session; 10 sessions in total. Coil, localisation method, intensity (%RMT) and pulses per session NR. Schedule (frequency of sessions over days) NR. Concurrent medication NR. |
| Sham/control method | Sham rTMS (method NR in abstract). |
| Primary outcome and instrument | Alcohol craving measured with the Alcohol Craving Questionnaire (ACQ-NOW) total score and factor scores, at baseline, after last rTMS session, and 1 month after last session. |
| Primary result with effect size and CI | Two-way repeated-measures ANOVA showed significant reduction in post-rTMS ACQ-NOW total and factor scores in the active group vs sham. Treatment x time interaction effect size moderate, eta(2) = 0.401. No CI, F, p value or group means reported in abstract. |
| Secondary results | ACQ-NOW factor scores reported as significantly reduced in the abstract (individual factors NR). No other secondary outcomes reported in abstract. Relapse outcomes not reported. |
| Follow-up | ACQ-NOW assessed 1 month after the last rTMS session. Results at 1 month not reported separately in abstract. |
| Adverse events | NR |
| Risk-of-bias notes | Abstract only. Single-blind (which party blinded NR). Allocation sequence and concealment NR. Unequal 2:1 allocation. Attrition, ITT handling and missing data NR. Sham method not described. Conclusion about combination with anticraving drugs and reduced relapse is not tested in the study as reported in the abstract. |

### Parameter summary (abstract only)

| Item | Reported in abstract |
|---|---|
| Target | Right DLPFC |
| Frequency | 10 Hz |
| Train duration | 4.9 s |
| Inter-train interval | 30 s |
| Trains per session | 20 |
| Sessions | 10 |
| Intensity (%RMT) | NR |
| Coil/localisation method | NR |
| Session schedule (days/week) | NR |
| Sham method | NR |
| Time after detox | NR (entry CIWA-Ar <=10 only) |

Note: quote strings were joined across the abstract's line breaks with single spaces.

*Extractor's caveat note:* A reader relying on the abstract could assume this is a randomised trial with a full statistical report. The abstract gives only one effect size (eta squared = 0.401, treatment x time interaction) and no confidence intervals, group means, p values or ACQ-NOW change scores. It does not report adverse events, the sham method, intensity in %RMT, the session schedule, or how long patients had been abstinent or detoxified before entry. The allocation was 2:1 (30 active, 15 sham), and the study is described as single-blind without saying who was blinded. The conclusion that rTMS combined with other anticraving drugs can reduce relapse goes beyond the craving outcome reported, and relapse was not measured. The abstract mentions a 1-month follow-up, but it reports results only for the post-treatment comparison.

### 15. Mishra BR, Praharaj SK, Katshu MZ, Sarkar S, Nizamie SH. Comparison of anticraving efficacy of right and left rTMS in alcohol dependence: a randomized double-blind study. J Neuropsychiatry Clin Neurosci 2015;27(1):e54-9. doi:10.1176/appi.neuropsych.13010013. PMID 25255169. NCT01093716

Source: Web search: PubMed abstract + registry | Tag: **SECONDARY**

**What this changes in the cloud pack:** **Correct the pack: n = 20, not 22**, and the journal is J Neuropsychiatry Clin Neurosci. 10 Hz, 20 trains, 10 sessions, ACQ-NOW. Both sides reduced craving (time F 185.9, eta2 0.91), with no difference between groups. %MT is not reported.

### 15. Raikwar et al. Left DLPFC HF-rTMS for craving in alcohol dependence: sham-controlled RCT (India). PMC8188934

Source: PMC8188934 | Tag: **FULLTEXT** | Quotes verified: 33/33

**What this changes in the cloud pack:** n=60 men (30/30), enrolled after detox. Coil placed by the 5-cm rule; STM 9000 stimulator. No difference between groups: craving fell in both arms and partly came back by 2 weeks. Table 1 shows 25 patients on anticraving medication, which contradicts the Discussion. This supports the pack.

| Field | Extracted |
|---|---|
| Design | Prospective, single-blind, randomized, sham-controlled trial; sham = coil placed tangentially without switching on, with the circular coil switched on to provide auditory cue (per Methods). Conducted Sept 2016 to Sept 2018 at a tertiary care multispecialty hospital in India. |
| N | 60 randomized (30 active, 30 sham); all completed the trial |
| Population and timing after detox | Right-handed male inpatients aged 25 to 56 years with ICD-10 alcohol dependence syndrome, recruited only after completion of detoxification. Drug-naive for anticraving medication per Discussion, though Table 1 reports 25 patients on anticraving medication. Mean age 37.13 ± 7.07 years; mean AUDIT 29.03 ± 4.90. rTMS given on 10 consecutive days after detoxification. |
| Stimulation or intervention parameters (target, localisation, frequency/TBS pattern, intensity %RMT, pulses/session, sessions, schedule) | Target: left DLPFC, located by the 5 cm rule. Device: STM 9000 (ATES MEDICA / EBNeuro), 70 mm air-cooled flat figure-of-eight coil, angled 45° tangentially, handle posterior. Motor threshold on right abductor pollicis brevis, visual method, Rossini-Rothwell algorithm, starting at 36% in 5% steps. Intensity 120% MT (mean MT active 46.67 ± 5.34). 10 Hz, 4 s trains, 26 s inter-train interval, 20 trains per session, 800 pulses/day. 10 sessions over 10 consecutive days. Earplugs provided. Concurrent group and individual psychotherapy 2 days per week each; parenteral thiamine and paracetamol as needed. |
| Sham/control method | Figure-of-eight coil placed tangentially to the head without switching on; no MT determined and no magnetic stimulation delivered; circular coil switched on and connected to paddle switch to mimic sound. |
| Primary outcome and instrument | Alcohol Craving Questionnaire (ACQ-NOW) total score (ACQ-T), at pre-rTMS, on completion of rTMS, and 2 weeks after completion. Analysis: repeated-measures ANOVA (reported as Pillai's trace F). |
| Primary result with effect size and CI | No significant difference between active and sham groups at any time point. Pre-rTMS: active 218.17 ± 9.699 vs sham 216.17 ± 13.488 (F = 1.526, p = 0.226, partial eta squared 0.051). Post-rTMS: active 92.03 ± 6.625 vs sham 93.30 ± 6.342 (F, p and eta squared NR for this row). 2 weeks post-rTMS: active 138.17 ± 7.737 vs sham 140.77 ± 8.299 (F, p and eta squared NR). CIs NR; group x time interaction statistic NR. |
| Secondary results | Within-group mean ACQ-NOW fell from pre to post-rTMS in both groups and partly rose by 2 weeks, with no between-group difference (Discussion: effects not sustained at 2 weeks). Baseline comparisons (Table 2, t-tests): age 38.04 ± 6.80 vs 36 ± 7.20 (p = 0.20); age of onset 23.53 ± 5.12 vs 21.37 ± 5.60 (p = 0.13); years of dependence 5.70 ± 5.40 vs 6.0 ± 5.5 (p = 0.83); CIWA-Ar 16.06 ± 6.02 vs 17.53 ± 8.01 (p = 0.43). Alcohol use profile reported as comparable between groups. |
| Follow-up | ACQ-NOW at 2 weeks after the last rTMS session; patients then started on anticraving medication and discharged. No longer follow-up reported. |
| Adverse events | Active group: headache (4), drowsiness (4), scalp discomfort (1). Sham group: head heaviness (1). All described as short lasting; none led to discontinuation. |
| Risk-of-bias notes | Single-blind only (participants blinded; assessor/operator blinding NR). Sham used a coil placed without switching on, with auditory cue from a second coil. Random allocation by random number table, but allocation concealment NR. Localisation by 5 cm rule (crude, acknowledged by authors). Table 1 shows 25 patients on anticraving medication, conflicting with the Discussion claim that patients were not on such medication. Table 1 has an arithmetic error (age of initial use ≥30 total given as 56, should be 5). Baseline groups differed in new/old cases and nature of referral. Power calculation NR. Craving assessed only in hospital setting. Financial support nil; no conflicts declared. |

### Left-DLPFC rTMS in India: parameters and results

| Item | Reported value |
|---|---|
| Sample | 60 male inpatients (30 active, 30 sham), all completed |
| Target | Left DLPFC, 5 cm rule |
| Coil | 70 mm air-cooled figure-of-eight, tangential 45°, 3.2 T max output |
| Frequency / train | 10 Hz, 4 s trains, 26 s inter-train interval, 20 trains |
| Pulses | 800 per day |
| Intensity | 120% of MT (active mean MT 46.67 ± 5.34) |
| Schedule | 10 consecutive daily sessions |
| Sham | Coil not switched on, no MT; circular coil switched on for sound |
| Outcome | ACQ-NOW total score: pre, post, 2 weeks post |
| Pre-rTMS means | Active 218.17 ± 9.699; Sham 216.17 ± 13.488 |
| Post-rTMS means | Active 92.03 ± 6.625; Sham 93.30 ± 6.342 |
| 2-week means | Active 138.17 ± 7.737; Sham 140.77 ± 8.299 |
| Group effect | No significant difference at any timepoint (pre F = 1.526, p = 0.226) |
| Adverse events | Headache 4, drowsiness 4, scalp discomfort 1 (active); head heaviness 1 (sham) |

No between-group effect is reported at any time point. Only the pre-rTMS F statistic is given; post and 2-week F and p values are NR.

*Extractor's caveat note:* A reader relying on the abstract would correctly learn that 10 daily high-frequency left DLPFC rTMS sessions did not reduce craving versus sham, but could miss several caveats. The primary analysis is a repeated-measures ANOVA with no reported F, p or CI for the post and 2-week comparisons, only group means. Craving fell in both groups after treatment, so the drop is non-specific rather than a treatment effect, and the authors note the effect was not sustained at 2 weeks. The abstract does not mention that the design was single-blind, that DLPFC was located with the crude 5 cm rule, or that the sham coil was placed without switching on. The Discussion states participants were not on anticraving medication, yet Table 1 lists 25 patients on such medication, and Table 1 contains an arithmetic error. The study also differs from prior work in its 2-week follow-up window and coil type, so it is not a direct replication of the right-DLPFC or H-coil studies it cites.

### 15. Joshi T, Dhiman V, Verma R, et al. A randomized sham-controlled trial of bilateral tDCS on craving, abstinence and relapse in severe AUD. Indian J Psychiatry 2025;67(2):219-228. CTRI/2022/03/040823

Source: PMC11964162 | Tag: **FULLTEXT** | Quotes verified: 36/36

**What this changes in the cloud pack:** n=149 men (75/74), SADQ > 30, at least 3 days free of alcohol and benzodiazepines. Anode F3, cathode F4, 2 mA for 20 minutes, twice daily for 5 days. OCDS at 3 months: d = 0.45. **Relapse 44% vs 63.5%, NNT 6.** Single-blind; 107 of 149 completed. This is the strongest Indian relapse result for brain stimulation. It is an AIIMS multisite trial whose twice-daily, 5-day schedule fits an inpatient stay. Lane 1 should treat it as the incumbent comparator.

| Field | Extracted |
|---|---|
| Design | Single-blind (per Limitations), randomized sham-controlled, parallel-group trial with 1:1 allocation; longitudinal follow-up at 1 and 3 months. Adjunct to treatment as usual. Analysis reported as intention-to-treat (n=149) with a 2x3 split-plot (mixed) ANOVA. |
| N | 149 randomized (75 active, 74 sham). 107 completed the 10 intended sessions (51 active, 56 sham). Derived: 42 did not complete. All 149 followed up. |
| Population and timing after detox | Male adults aged 18-55 with DSM-5 alcohol use disorder, SADQ >30 (severe), OCDS >1, right-handed. Included after completion of acute withdrawal management and at least 3 days abstinent from alcohol and benzodiazepines. Mean age 36.22 ± 6.4 years (range 22-53). Outpatients and inpatients. All on treatment as usual; naltrexone or acamprosate received by part of each group. Timing: tDCS started after the 3-day abstinence and benzodiazepine washout; all 10 sessions given over 5 consecutive days. |
| Stimulation or intervention parameters | Bilateral tDCS, anode F3 (left dlPFC) and cathode F4 (right dlPFC), 10:20 EEG placement. Current 2 mA; ramp-up to 2 mA over 30 s, then 20 min at 2 mA. Two sessions per day spaced at least 2 h apart; 10 sessions over 5 consecutive days. Target/localisation: dlPFC. TBS pattern: NR. %RMT: NR. Pulses per session: NR (not applicable to tDCS). |
| Sham/control method | Sham tDCS: ramp-up for 30 s at the beginning, then stimulation ended (the paper describes the sham as ramp-up only). Participants blinded to allocation through the sham setting of the device. Control group also received treatment as usual. |
| Primary outcome and instrument | Craving measured by Obsessive Compulsive Drinking Scale (OCDS) at 3 months (English and Hindi versions). Between-group comparison at 3 months by independent t-test; time x group effect by mixed ANOVA. |
| Primary result with effect size and CI | 3 months OCDS: active 28.50 ± 13.23 vs sham 34.75 ± 14.07; t(147) = -2.79; Cohen's d = 0.45 (small); no CI reported for this test. Mixed ANOVA: F(2,294) = 5.52, P < 0.01; partial eta-squared for group x time 0.04 (small). Time main effect F(1.5)=201.2, P<0.001, partial eta-squared 0.58 (reported in Results as large, within-group time effect). Note: the abstract and Results text describe the ANOVA with different interpretations; the ANOVA df in the source (2,294 and 1.5) are as printed. |
| Secondary results | Relapse at 3 months: 33/75 (44%) active vs 47/74 (63.5%) sham; chi-square(1) = 5.7; P = 0.01 (abstract) or P = 0.02 (Results). Absolute difference 19.5 percentage points; NNT 6, 95% CI [2.8-26.2]. Time to first drink: active 38.46 ± 26.99 days vs sham 29.39 ± 23.83 (abstract: 38.50 ± 27.0 vs 29.40 ± 23.83); t(147) = 2.17 (abstract t = 2.20), P = 0.03; d = 0.35, 95% CI [0.03-0.67]. Time to relapse: 67.77 ± 29.70 vs 55.02 ± 30.72 days; t(147) = 2.57, P = 0.01; d = 0.42, 95% CI [0.09-0.74]. Kaplan-Meier (non-relapse survival): mean 55.4 days (95% CI 47.2-63.7) active vs 38.5 days (30.9-46.2) sham; chi-square(1) = 8.1, P = 0.004. Craving at 1 month: active 30.37 ± 11.66 vs sham 33.55 ± 13.73. Baseline OCDS: 48.33 ± 1.94 vs 48.27 ± 2.45. Abstinence at end of study: about 10% of all participants, of whom 3 in 5 were in the active group (per Discussion). |
| Follow-up | Assessments at baseline, 1 month and 3 months (OCDS and Timeline Follow-Back at 1 and 3 months). All 149 randomized participants followed up in person or by telephone. Follow-up beyond 3 months: NR. |
| Adverse events | Tolerability checked after every session with a tDCS side-effect checklist. Authors report no side effects in either arm. Reporting is self-report only. |
| Risk-of-bias notes | (1) Single-blinded; authors state double blinding would have strengthened results. (2) Allocation list generated in two batches at 1:1 ratio, kept by an investigator not delivering the intervention; concealment otherwise NR. (3) Sample size: G*Power assumed d = 0.5 and gave 128 needed; 149 randomized. (4) Convenience and purposive sampling with extensive exclusions. (5) Assumption violations: Box's M (P = 0.02), sphericity (Greenhouse-Geisser used), Levene's test at 1 month (P = 0.03). (6) Primary test (t-test) reports no CI or P value in the text. (7) Relapse P value differs between abstract (0.01) and Results (0.02). (8) Time-to-first-drink means differ slightly between abstract and Results. (9) Medication adherence not assessed; naltrexone and acamprosate use differed between arms (62.7% vs 54.1% naltrexone). (10) Authors note confounders (inpatient changes, medication changes, comorbidities) between follow-ups. (11) Only 107 of 149 completed the protocol; ITT analysis used. (12) Self-report outcomes. |

### Sub-table: tDCS parameters and key results (Indian AUD RCT)

| Item | Reported |
|---|---|
| Montage | Anode F3, cathode F4 (bilateral dlPFC; EEG 10:20) |
| Intensity | 2 mA (ramp 30 s; 20 min at 2 mA) |
| Schedule | 2 sessions/day, at least 2 h apart; 10 sessions over 5 consecutive days |
| Sham | 30 s ramp-up only, then off |
| Sample | 149 randomized (75 A / 74 S); 107 completed |
| Primary (3 m OCDS) | 28.50 ± 13.23 vs 34.75 ± 14.07; t(147) = -2.79; d = 0.45 |
| Relapse at 3 m | 44% vs 63.5%; chi-square = 5.7; NNT 6 [2.8-26.2] |
| Time to first drink | 38.46 ± 26.99 vs 29.39 ± 23.83 days; d = 0.35 [0.03-0.67] |
| Time to relapse | 67.77 ± 29.70 vs 55.02 ± 30.72 days; d = 0.42 [0.09-0.74] |
| Adverse events | None reported |

Discrepancies to note: relapse P (0.01 abstract vs 0.02 Results); time-to-first-drink values (38.50 vs 38.46; t 2.20 vs 2.17); primary-outcome CI absent.

*Extractor's caveat note:* A reader relying on the abstract would take away a clear, large-benefit story, but the data show a modest one. The primary OCDS difference at 3 months is small (d = 0.45) and reported without a CI; the abstract's F-test describes group x time differences that the authors themselves rate as small (partial eta-squared 0.04). The abstract also omits that only 107 of 149 completed the protocol, that the trial was single-blinded, that the sample was all male and that several assumption tests were violated. The relapse chi-square P value differs between abstract (0.01) and Results (0.02), and the time-to-first-drink values differ slightly. Survival and NNT figures come from a single-centre trial with self-reported outcomes, and the 3-month follow-up is short. The abstract's conclusion that tDCS 'demonstrated efficacy' should be read as a preliminary, single-centre finding with the caveats listed above, and the authors state that the effects were small at study end.

### 16. Wang H, Yuan C, Gan H, Jiang H, Zhao Y, Du J, Zhang Y. A randomized controlled study on the effect of iTBS on craving, mood and cognitive function in alcohol-dependent patients during the withdrawal period. J Shanghai Jiao Tong Univ (Med Sci) 2025;45(3):349-356. doi:10.3969/j.issn.1674-8115.2025.03.012

Source: Journal web page abstract (Chinese; machine-read and translated) | Tag: **SECONDARY**

**What this changes in the cloud pack:** n=41 (20/21). Sham used the same parameters. 10 sessions over 2 weeks. Craving (VAS) time x group F 7.08, p = 0.011, partial eta2 0.154. 2-back interaction p = 0.032. **%RMT and pulse count were not found**; the full text is needed.

### 17a. Scott-Sheldon LAJ, Terry DL, Carey KB, Garey L, Carey MP. Efficacy of expectancy challenge interventions to reduce college student drinking: a meta-analytic review. Psychol Addict Behav 2012;26(3):393-405. doi:10.1037/a0027565

Source: PMC3381876 | Tag: **FULLTEXT** | Quotes verified: 40/40

**What this changes in the cloud pack:** Reports d+ (not g) at first follow-up, about 2 weeks after the intervention: positive expectancies 0.28 (0.14-0.43, k=11), quantity 0.23 (0.08-0.38, k=11), heavy-drinking frequency 0.27 (0.06-0.47, k=5). **Effects were not maintained beyond about 4 weeks.** This paper is NOT the source of g = -0.20.

| Field | Extracted |
|---|---|
| Design | Systematic search and meta-analysis of 14 studies (19 expectancy challenge [EC] interventions). Between-group (EC vs control) and within-group pre-post effect sizes; fixed- and random-effects models; univariate moderator regressions (Bonferroni P = .005). Primary analyses restricted to first post-intervention assessment. |
| N | 1,415 (abstract); Results section gives 1,417 sampled (median 72 per study). Discrepancy between sources. |
| Population and timing after detox | College students, mean age 20 (SD 0.93, range 19-21); 60% men (abstract reports 40% women); 88% White; 91% (k = 13) reported alcohol use; no past or current alcohol treatment. Timing (first assessment): 2 weeks (M = 2.07 weeks; range 0 to 4.33). Second: 4 weeks (M = 6.95; range 2 to 13). Third: 26 weeks (M = 20.96; range 3 to 26). 'Detox' not applicable (behavioural prevention study). |
| Stimulation or intervention parameters (target, localisation, frequency/TBS pattern, intensity %RMT, pulses/session, sessions, schedule) | Not applicable (no neurostimulation). Behavioural EC interventions. Experiential EC (k = 11, 58%): median 3 sessions (range 1-3), median 105 min per session (range 75-105); alcohol or placebo administered in a bar-like group setting, social/party games, identification of who had consumed alcohol, discussion of expectancies. Didactic EC (k = 8, 42%): median 2 sessions (range 1-3), median 45 min per session (range 12-90); lectures, videos, writing/journaling, diaries, refutation statements. Targets: positive and negative alcohol expectancies; consumption. See 'extra' for session description. |
| Sham/control method | Active comparison (53%; e.g., brief form of intervention; median 2 sessions of 21 min, range 10-105 min); assessment-only control (41%); 2 studies had no comparison condition. Placebo beverages in experiential arms (some with minimal alcohol on glass rim). |
| Primary outcome and instrument | Global positive and negative alcohol expectancies; quantity of alcohol consumed; frequency of heavy drinking (usually 5+ drinks men, 4+ women). Instruments varied across studies (e.g., Alcohol Expectancy Questionnaire, Comprehensive Effects of Alcohol Scale); all self-report. |
| Primary result with effect size and CI | Between-group at first follow-up (fixed effects; Table 2): positive expectancies d+ = 0.28 (95% CI 0.14, 0.43), k = 11; quantity d+ = 0.23 (0.08, 0.38), k = 11; frequency of heavy drinking d+ = 0.27 (0.06, 0.47), k = 5. Negative expectancies not significant (d+ = −0.17, −0.37 to 0.04, k = 5). Problems: NR. |
| Secondary results | Within-group, EC vs baseline (Table 3, first follow-up): positive expectancies d+ 0.20 (0.11, 0.29), k = 14; quantity 0.13 (0.01, 0.25), k = 10; frequency 0.36 (0.17, 0.56), k = 4; negative 0.03 (−0.09, 0.15), k = 8. Specific expectancies (between-group, first follow-up): social 0.22 (0.07, 0.37), sexual 0.28 (0.13, 0.43), tension 0.34 (0.14, 0.54), arousal 0.23 (0.06, 0.40). Last assessment: positive expectancies d+ = 0.30 (0.07, 0.52), k = 5; no between-group differences in negative expectancies, quantity or heavy-drinking frequency at last assessment (no d+ reported). Moderators: older age associated with more negative AE after EC (β = 0.94); male-targeted content associated with reduced quantity (β = 0.98); other moderators non-significant. |
| Follow-up | First assessment typically ~2 weeks (range 0 to 4.33 weeks). Last assessment (8 of 13 multi-assessment studies) M = 8.67 weeks, range 2 to 26 weeks. Authors state consumption effects were not maintained at longer follow-ups. |
| Adverse events | NR |
| Risk-of-bias notes | Study quality score (12 items, range 0-17) for included studies ranged 6 to 14 (M 10.67, SD 2.54); newer studies higher quality (r = 0.80 with publication year). Outcomes all self-report (cognitive and social-desirability bias acknowledged). Few studies per outcome; moderator tests preliminary. Primary analyses limited to first follow-up to avoid non-independence. Ten/eleven experiential interventions used placebo-based deception; some studies had no comparison group. Publication bias assessment: NR. Inter-rater reliability: 80% agreement categorical; ICC mean 0.93. |

## Pooled effect sizes by outcome and follow-up interval

No d+ values are reported for 'problems' at any interval (NR).

**A. Between-group, EC vs control, first follow-up (~2 wk; Table 2)**

| Outcome | k | d+ fixed (95% CI) | d+ random (95% CI) |
|---|---|---|---|
| Positive AE (global) | 11 | 0.28 (0.14, 0.43) | 0.28 (0.14, 0.43) |
| Negative AE (global) | 5 | −0.17 (−0.37, 0.04) | −0.29 (−0.66, 0.08) |
| Combined AE | 4 | 0.07 (−0.14, 0.28) | 0.07 (−0.14, 0.28) |
| Quantity | 11 | 0.23 (0.08, 0.38) | 0.24 (0.05, 0.42) |
| Frequency of heavy drinking | 5 | 0.27 (0.06, 0.47) | 0.27 (0.02, 0.52) |
| Problems | NR | NR | NR |

**B. Between-group, last available assessment (up to 26 wk; text only)**

| Outcome | k | d+ (95% CI) |
|---|---|---|
| Positive AE (global) | 5 | 0.30 (0.07, 0.52) (model not stated; sits in last-assessment paragraph, so interval is inferred) |
| Negative AE, combined AE, quantity, frequency | NR | No d+ given; text says no differences |
| Problems | NR | NR |

**C. Within-group, EC pre- to post-test, first follow-up (Table 3; fixed effects only)**

| Outcome | k (EC) | d+ EC (95% CI) | k (control) | d+ control (95% CI) |
|---|---|---|---|---|
| Positive AE | 14 | 0.20 (0.11, 0.29) | 9 | −0.03 (−0.14, 0.08) |
| Negative AE | 8 | 0.03 (−0.09, 0.15) | 4 | 0.07 (−0.10, 0.25) |
| Quantity | 10 | 0.13 (0.01, 0.25) | 6 | −0.11 (−0.26, 0.04) |
| Frequency of heavy drinking | 4 | 0.36 (0.17, 0.56) | 2 | 0.01 (−0.22, 0.23) |
| Problems | NR | NR | NR | NR |

Within-group at last assessment: NR.

**D. Specific expectancies (first follow-up)**

| Expectancy | Between-group k, d+ fixed (95% CI) | Within-group EC k, d+ (95% CI) |
|---|---|---|
| Social | 9, 0.22 (0.07, 0.37) | 11, 0.33 (0.23, 0.44) |
| Sexual | 9, 0.28 (0.13, 0.43) [random 0.32 (0.12, 0.52)] | 11, 0.15 (0.05, 0.26) |
| Tension | 5, 0.34 (0.14, 0.54) [random 0.38 (0.06, 0.71)] | 7, 0.33 (0.20, 0.46) |
| Arousal | 8, 0.23 (0.06, 0.40) [random 0.32 (0.03, 0.62)]; I² = 63% (19-83) | 8, 0.17 (0.04, 0.31) |

## What the expectancy challenge sessions involved

- **Experiential EC (11 of 19 interventions):** Median 3 sessions of about 105 min, delivered mainly to small groups (median 11.5 participants). Participants received alcohol or placebo in a bar-like setting (in 2 studies, placebo with minimal alcohol on the glass rim). Activities included social or party games (social expectancies, arousal, or both). Participants identified who had and had not been drinking alcohol. Facilitators gave information on expectancies and asked participants to monitor expectancy exposure, sources, or reactions.
- **Didactic EC (8 of 19):** Median 2 sessions of about 45 min, delivered individually or in small groups. Content was presentation-based: information on expectancy theory and pharmacology, videos (e.g., mock EC, alcohol advertisements, alcohol and aggression), written or journaled expectancy diaries, essays, and refutation statements.
- **Common content:** Expectancy theory information (95%) and pharmacological information (79%); discussion or monitoring of expectancy sources (63%); writing or journaling (63%); personalised feedback (32%); booster sessions in only 16%.

Note: sources conflict on study and intervention counts (14 studies/19 interventions vs '15 manuscripts with 20 separate interventions' in Methods).

*Extractor's caveat note:* A reader relying on the abstract would get the headline right, but several caveats matter. The between-group effects on positive expectancies, quantity and heavy-drinking frequency are small (d+ 0.23 to 0.28) and come from the first follow-up, typically about 2 weeks after the intervention. The abstract's 'not maintained beyond 4 weeks' is consistent with the Discussion, though the Discussion also says effects lasted 'as long as one month' and the Limitations say reductions were 'not maintained two months' after intervention. At the last assessment (up to 26 weeks), only positive expectancies remained lower (d+ 0.30, 0.07 to 0.52, k = 5); there were no consumption differences. The within-group effects (d+ 0.13 to 0.36) include changes in the EC arm only and are not controlled comparisons, and control arms showed no change. Negative expectancies did not change, contrary to the hypothesis. Moderator results were preliminary (few studies, no multivariate tests), and the older-age effect on negative expectancies was contrary to prediction. Sample size is reported as 1,415 in the abstract and 1,417 in Results. Problems outcomes were not reported in this paper.

### 17b. Wang X, Yang S, Xie X, Sethabouppha H. The effects of expectancy-challenge interventions on binge drinking among college students: a systematic review and meta-analysis. J Am Coll Health 2026;74(7):2013-2023. doi:10.1080/07448481.2026.2643638. PMID 41855530

Source: PubMed abstract | Tag: **ABSTRACT** | Quotes verified: 7/7

**What this changes in the cloud pack:** **This is the source of g = -0.20.** Binge-episode frequency at about 1 month: g = -0.20 (-0.33 to -0.07), 8 trials. Positive expectancies g = -0.50 immediately after the intervention. **No significant effect at 3-6 months.** In `03-lane2` section 2, cite Wang 2026 for g = -0.20 and add that the effect is short-lived and comes from college students, not dependent patients.

| Field | Extracted |
|---|---|
| Design | Systematic review and meta-analysis of randomized controlled trials (PRISMA-compliant, PROSPERO-registered; registration number NR in abstract) |
| N | NR (abstract reports 8 trials; total participants NR) |
| Population and timing after detox | College students. Detox: not applicable. Timing: approximately one month post-intervention for the binge-episode result; 3-6 months for sustained effects. |
| Stimulation or intervention parameters (target, localisation, frequency/TBS pattern, intensity %RMT, pulses/session, sessions, schedule) | Not applicable (non-stimulation). Expectancy-challenge interventions in experiential, didactic, or digital formats. Dose, sessions and schedule: NR. |
| Sham/control method | Non-alcohol control conditions (type not specified in abstract) |
| Primary outcome and instrument | Binge-episode frequency; instrument NR |
| Primary result with effect size and CI | Hedges' g = -0.20 (95% CI -0.33 to -0.07), k NR, at approximately one month; small but significant reduction. |
| Secondary results | Alcohol outcome expectancies: positive expectancies g = -0.50 (CI NR, k NR, immediate); negative expectancies g = 0.27 (CI NR, k NR, immediate), attenuated at one month (effect size NR). Sustained behavioural effects at 3-6 months: limited and not statistically significant (effect size, CI and k NR). Subgroup moderation by delivery format, control type, or modality: no consistent moderation (statistics NR). |
| Follow-up | Approximately one month (main binge result); 3-6 months (sustained effects, non-significant) |
| Adverse events | NR |
| Risk-of-bias notes | NR in abstract. Abstract notes that most outcomes rest on few trials, especially long-term and subgroup results. |

### Effect sizes reported in the abstract (abstract only)

| Outcome | Effect (g) | 95% CI | k | Timing | Population |
|---|---|---|---|---|---|
| Binge-episode frequency | -0.20 | -0.33 to -0.07 | NR (8 trials total) | ~1 month post-intervention | College students |
| Positive alcohol expectancies | -0.50 | NR | NR | Immediate (post-intervention) | College students |
| Negative alcohol expectancies | 0.27 | NR | NR | Immediate; attenuated at 1 month (value NR) | College students |
| Sustained behavioural effect | NR (not significant) | NR | NR | 3-6 months | College students |
| Subgroup moderators (format, control type, modality) | NR (no consistent moderation) | NR | NR | NR | College students |

Note: 'k' per outcome is not given in the abstract. The only trial count is 8 trials overall.

*Extractor's caveat note:* A reader using only the abstract gets the headline g = -0.20 (95% CI -0.33 to -0.07) at about one month, which is a small effect whose interval excludes zero. The abstract does not give k, N, or CIs for the expectancy effects (g = -0.50 and g = 0.27), so their precision cannot be judged. The 'immediate' versus 'one month' timing for the expectancy results is only partly specified. The abstract also says the 3-6 month behavioural effect was not significant and rests on few trials, so the conclusion that ECIs reduce drinking is supported only for the short term. Subgroup findings have no statistics in the abstract. Risk of bias, intervention dose and adverse events cannot be assessed from the abstract.

## Gaps left open

- #2 Treiber 2025: the full text is paywalled, so its included studies are not listed. #1's included-RCT sub-table is in its detail block.
- #5 Harel 2022 and #16 Shanghai 2025: the full text is still needed for %RMT and the complete results.
- #8 medRxiv living meta-analysis: the full text and supplement, which hold any alcohol-specific ranking, sit behind Cloudflare. Open it in a browser.
