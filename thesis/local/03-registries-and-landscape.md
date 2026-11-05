# 03 — Registries and landscape

Run 5 Nov 2026. Routes that worked and failed:

| Source | Route | Result |
|---|---|---|
| ClinicalTrials.gov | API v2, scripted (`scripts/ctgov_search.py`) | **Done.** Primary data. |
| PubMed (Review A/B strings) | E-utilities esearch | **Not done.** NCBI search backend returned HTTP 500 ("Cannot connect to SOLR") all session; efetch worked. Rerun: `python thesis/local/scripts/pubmed_review_searches.py thesis/local` |
| CTRI | ctri.nic.in direct | **Not reachable** from this laptop (timeouts). Results below are from web search: SECONDARY, verify each on CTRI. |
| PROSPERO | web search (OpenRouter web plugin) | SECONDARY. Verify IDs on crd.york.ac.uk. |
| Faculty publications | OpenAlex API (primary bibliographic data) | Done. Google Scholar not used (blocks scripts). |
| ANRF project | web search + local files | SECONDARY + local notification document. |

Free subdel workers (opencode Zen DeepSeek) were tried first for CTRI, PROSPERO, faculty and AIIMS; all 6 dispatches ended without writing output (web-search keys missing on this laptop). Everything below came from scripts or the OpenRouter web plugin.

---

## 1. CTRI

### CTRI/2023/12/060572: registrant **NOT FOUND**
Web search found no record. The cloud pack's only source is a medpath.com aggregator page (`06-sources.md`). Needs a manual look-up on ctri.nic.in (Trial search → registration number) from a browser. Closest non-Indian matches (MUSC cTBS frontal pole; MUSC iTBS mPFC vs DLPFC protocol) are listed in the raw output below. None is the CTRI trial.

### Indian NIBS / alcohol trials found via secondary sources
I could not query the CTRI database directly; the search tool returned only the CTRI homepage and search page. The trials below are the ones whose CTRI numbers appear in published papers or protocols, so each row is SECONDARY. Fields I could not confirm are marked NOT FOUND. Please verify every row on ctri.nic.in before citing it.

**Table: Indian CTRI-registered trials (secondary sources)**

| CTRI number | Title | PI and institution | Design | N | Status | Date | Publication | URL |
|---|---|---|---|---|---|---|---|---|
| CTRI/2022/01/039412 | Bifrontal tDCS on craving in alcohol use disorder | PI: NOT FOUND. Authors: Gairola A, Nischal A, Kar SK, Arya A, Singh A; affiliations not in retrieved text | Randomised, sham-controlled; active vs sham tDCS | Sample size estimated at 30; analysed N NOT FOUND | Completed (data collected Jan–Nov 2022) | Registration date NOT FOUND | Indian J Psychol Med 2024; doi 10.1177/02537176231223314 | https://journals.sagepub.com/doi/10.1177/02537176231223314 ; PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC11572694/ |
| CTRI/2022/03/040823 | tDCS for craving, abstinence and time to relapse in severe AUD | PI: NOT FOUND. Authors include Joshi T, Dhiman V, Verma R, Krishnan V, Basu A, Singh Y, from several AIIMS sites (registering site not stated) | Randomised sham-controlled trial | 149 randomised (75 active, 74 sham); 107 received intended sessions | Completed; published | Registration date NOT FOUND | Indian J Psychiatry 2025;67(2):219-228; doi 10.4103/indianjpsychiatry.indianjpsychiatry_744_24 | https://pubmed.ncbi.nlm.nih.gov/40181873/ ; https://journals.lww.com/indianjpsychiatry/fulltext/2025/02000/a_randomized_sham_controlled_trial_to_study_the.4.aspx |
| CTRI/2021/09/036989 | Prefronto-cerebellar tDCS on craving and relapse in alcohol dependence syndrome | PI: NOT FOUND. Government-funded multispecialty hospital, Raipur, Chhattisgarh | Randomised, sham-controlled, block randomisation; 10 sessions over 5 days | NOT FOUND | Start Oct 2021 per protocol; current status NOT FOUND | Registration date NOT FOUND | Protocol: medRxiv 2022.08.05.22278474 | https://www.medrxiv.org/content/10.1101/2022.08.05.22278474v1.full |
| CTRI/2020/09/027582 | PreCoTTA: prefrontal cortex tDCS in alcohol dependence syndrome | PI: NOT FOUND. Co-author affiliated with Kasturba Medical College, Manipal | Double-blind, randomised, sham-controlled; 2 active arms (left DLPFC, left OFC) and 1 sham | 225 male patients planned | Protocol; current status NOT FOUND | Registered 3 Sept 2020 (per abstract) | Study protocol, PubMed 34365959 | https://pubmed.ncbi.nlm.nih.gov/34365959/ |
| CTRI/2024/11/076108 | Adjunctive cathodal HD-tDCS over insula on cue-induced craving; fMRI BOLD | PI: NOT FOUND. Two units of a tertiary mental health and neuroscience institute (name NOT FOUND

Note: CTRI/2022/03/040823 is the Indian tDCS RCT already in the pack (Joshi et al. 2025, verified in `02` #15).

---

## 2. ClinicalTrials.gov

### Named trials (status as of 5 Nov 2026)
| nct | title | sponsor | status | start | completion | enrollment | results_posted | linked_pubs(RESULT/DERIVED) |
|---|---|---|---|---|---|---|---|---|
| NCT06060496 | Theta Burst Stimulation for Alcohol Use Disorder | Gopalkumar Rakesh | COMPLETED | 2023-10-01 | 2024-04-17 | 8 | yes |  |
| NCT03932149 | The Effect of Intermittent Theta Burst Stimulation (iTBS) in Patients With Alcohol Use Disorder | Shanghai Mental Health Center | UNKNOWN | 2019-12-06 | 2021-03 | 60 | no | 32218749:Yuan C, Su H, Chen T, Voon V, Du J. The Effect of Intermittent Theta Burst Stimulation (iT |
| NCT06320366 | Testing an Accelerated TMS Protocol for Methamphetamine Use Disorder | University of Colorado, Denver | RECRUITING | 2024-09-03 | 2028-05-31 | 20 | no |  |
| NCT03470480 | rTMS for Craving in Methamphetamine Use Disorder | Oregon Health and Science University | RECRUITING | 2018-02-07 | 2027-09-01 | 50 | no |  |
| NCT05271175 | Accelerated iTBS in Smoking Cessation | Cyprus rTMS Center | COMPLETED | 2019-04-19 | 2020-09-07 | 104 | yes | 35686190:Mikellides G, Michael P, Psalta L, Stefani A, Schuhmann T, Sack AT. Accelerated Intermitte |
| NCT04990375 | tDCS to Prevent Relapse in Alcohol Use Disorder | Brugmann University Hospital | COMPLETED | 2021-04-02 | 2022-06-06 | 40 | no |  |
| NCT06959342 | Modification of Inhibitory Control and Craving Through Transcranial Direct Current Stimulation (tDCS) as an Add-On Treatment for Substance Use Disorder | Central Institute of Mental Health, Mannheim | RECRUITING | 2024-09-23 | 2027-09-30 | 162 | no | 41084082:Vollstadt-Klein S, Turkmen C, Grundinger N, Wieland A, Aggensteiner PM, Stock AK, Stein M, |

### Fresh search: condition "alcohol use disorder", intervention theta burst / iTBS / cTBS / accelerated, start ≥ 2020: 14 records
| nct | title | sponsor | status | start | completion | enrollment | results_posted | linked_pubs(RESULT/DERIVED) |
|---|---|---|---|---|---|---|---|---|
| NCT03981185 | aTBS for Treatment of Depression in AUD | Stanford University | WITHDRAWN | 2024-01-01 | 2024-07-11 | 0 | no |  |
| NCT04223154 | Effect of Theta Burst Stimulation on Alcohol Cue Reactivity | Wake Forest University Health Sciences | COMPLETED | 2020-08-26 | 2021-04-16 | 11 | yes |  |
| NCT06770556 | Transcranial Magnetic Stimulation (TMS) Effects Using Magnetoencephalography (MEG) Study | Wake Forest University Health Sciences | COMPLETED | 2025-03-21 | 2026-07-29 | 5 | no |  |
| NCT06963476 | rTMS as Add on Treatment for Substance Use Disorders | Yale University | COMPLETED | 2025-05-12 | 2025-11-24 | 47 | no |  |
| NCT06648642 | Image-guided, Robot Navigated Transcranial Magnetic Stimulation (IR-TMS) for Alcohol Use Disorder (AUD) | The University of Texas Health Science Center at San Antonio | RECRUITING | 2025-02-03 | 2027-05-31 | 150 | no |  |
| NCT06299787 | Cognitive Dysfunction in the Addictions Study - Project 4 (P4) | Centre for Addiction and Mental Health | UNKNOWN | 2022-02-07 | 2025-07-01 | 40 | no |  |
| NCT07171359 | TMS to Improve Recovery Outcomes Among Patients With Opioid Use Disorder (OUD) and Alcohol Use Disorder (AUD) | Washington State University | RECRUITING | 2027-06-01 | 2027-10-01 | 60 | no |  |
| NCT04998916 | MPFC Theta Burst Stimulation as a Treatment Tool for Alcohol Use Disorder: Effects on Drinking and Incentive Salience | Medical University of South Carolina | RECRUITING | 2021-07-06 | 2026-12-31 | 86 | no |  |
| NCT06060496 | Theta Burst Stimulation for Alcohol Use Disorder | Gopalkumar Rakesh | COMPLETED | 2023-10-01 | 2024-04-17 | 8 | yes |  |
| NCT04154111 | Theta Burst Stimulation as a Tool to Decrease Drinking in Treatment-seeking Alcohol Users | Wake Forest University Health Sciences | COMPLETED | 2020-05-26 | 2026-02-09 | 147 | no | 41214823:Kinney KR, Kirse HA, Stewart NE, Ip EH, Saldana S, DeMaioNewton HE, Kimber M, Smith HR, Do |
| NCT06696365 | iTBS for Alcohol Use Disorder | Nicholas Balderston, PhD | TERMINATED | 2025-07-18 | 2026-04-08 | 2 | no |  |
| NCT06415721 | Developing Functional Connectivity-Guided TMS for Alcohol Use Disorder | VA Palo Alto Health Care System | RECRUITING | 2025-08-25 | 2026-01-01 | 40 | no |  |
| NCT07808190 | HD-tACS for Alcohol Use Disorder | Shanghai Mental Health Center | NOT_YET_RECRUITING | 2026-09-01 | 2026-12-31 | 140 | no |  |
| NCT05896332 | rTMS in Older Adults With MCI and AUD | Medical University of South Carolina | ACTIVE_NOT_RECRUITING | 2023-11-01 | 2026-11-30 | 35 | no |  |

Points for the pack: NCT03932149 (Shanghai iTBS) has a linked publication (Yuan C et al., PMID 32218749, protocol); status UNKNOWN, no results. NCT06060496 (Rakesh, n=8) has **results posted**. NCT04154111 (Wake Forest, n=147, completed Feb 2026) has a linked paper (PMID 41214823). NCT04998916 (MUSC mPFC TBS, n=86) is still recruiting to Dec 2026. No Indian TBS-in-AUD registration on ClinicalTrials.gov.

---

## 3. PROSPERO and existing reviews (SECONDARY)

**Scope note:** I could not query PROSPERO or OSF directly. These results come from web-search snippets, so every fact is tagged SECONDARY. Verify IDs on crd.york.ac.uk/prospero before relying on them. No OSF registration for any of the five topics turned up.

## Table

| Topic | Registration ID or citation + DOI | Title | Status | URL |
|---|---|---|---|---|
| (a) | CRD420261363708 | Efficacy of intermittent theta-burst stimulation for substance use disorders: SR and MA of sham-controlled RCTs (AUD in 1 trial) | Published, *Front Neurol* 2026, doi:10.3389/fneur.2026.1866761 | https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2026.1866761/full |
| (a) | CRD42024504362 | Non-invasive brain stimulation paradigms in AUD: SR and NMA protocol, *PLoS One* 2025, doi:10.1371/journal.pone.0332857 | Protocol published; completed review NOT FOUND | https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0332857 |
| (a) | CRD42024567484 | Efficacy of NIBS in reducing craving in AUD: SR and MA, *BMC Psychiatry* 2025, doi:10.1186/s12888-025-06883-4 | Published | https://link.springer.com/article/10.1186/s12888-025-06883-4 |
| (a) | No ID found (NOT FOUND) | rTMS for alcohol craving in AUD: SR and MA, *J Addict Med* 2025, doi:10.1097/ADM.0000000000001416 | Published; registration NOT FOUND | https://pubmed.ncbi.nlm.nih.gov/39665462/ |
| (a) | No ID found (NOT FOUND); medRxiv 10.1101/2025.09.21.25335559 | Living SR/MA of TMS, tES and

**Reading for the pack.** Review A (NIBS in AUD, broad) is **taken** several times over: CRD42024567484 (BMC Psychiatry 2025, published), CRD42024504362 (NMA protocol in PLoS One 2025), Treiber 2025, Front Neurol 2026 (CRD420261363708), and the medRxiv living review. The narrower angle in `02-lane1` (TBS **during inpatient detox / LMIC settings**) still looks open, but only as a timing-focused review. Review B topics (c) Allen Carr and (d) expectancy challenge in clinical populations look open apart from the 2023 TPC review (smoking only).

---

## 4. PubMed hit counts for Review A and B

**Not obtained** (see route table). The search strings are in `scripts/pubmed_review_searches.py`, which writes `search-exports/reviewA_pubmed_top50.csv` and `reviewB_pubmed_top50.csv` with counts printed.

---

## 5. Likely guide and co-guides (OpenAlex, top-cited works filtered for TMS/alcohol/craving/digital)


## Sharad Philip
Candidate author records (OpenAlex):
- https://openalex.org/A5042867687 | Sharad Philip | works 92 | All India Institute of Medical Sciences Guwahati, All India Institute of Medical Sciences | topics: Mental Health Treatment and Access, Psychiatric care and mental health services, Diabetes Management and Education, COVID-19 and Mental Health
- https://openalex.org/A5060765277 | Maruti Kumar Mudunuru | works 139 | Pacific Northwest National Laboratory | topics: Machine Learning in Materials Science, Neural Networks and Applications, Model Reduction and Neural Networks, Innovative Microfluidic and Catalytic Techniques Innovation
- https://openalex.org/A5114596733 | Philip Sharad | works 1 | All India Institute of Medical Sciences Guwahati | topics: Innovations in Medical Education, Mental Health Treatment and Access, Cultural Competency in Health Care

### Sharad Philip (All India Institute of Medical Sciences Guwahati All India Institute of Medical Sciences) — 3 relevant of top 40 cited
- 2025 | ICMR’s multistate implementation research study on integration of screening and management of mental and substance use disorders with other non-communicable diseases (ICMR-MINDS) – An implementation research study protocol | PLoS ONE | https://doi.org/10.1371/journal.pone.0332359
- 2021 | A report on successful introduction of tele mental health training for primary care doctors during the COVID 19 pandemic | Asian Journal of Psychiatry | https://doi.org/10.1016/j.ajp.2021.102967
- 2024 | Psychosocial characteristics of smartphone use behaviors – comparison between urban and rural school students in India | Journal of Neurosciences in Rural Practice | https://doi.org/10.25259/jnrp_377_2024

### Maruti Kumar Mudunuru (Pacific Northwest National Laboratory) — 0 relevant of top 40 cited

### Philip Sharad (All India Institute of Medical Sciences Guwahati) — 0 relevant of top 1 cited

## Ramdas Ransing
Candidate author records (OpenAlex):
- https://openalex.org/A5036979670 | Ramdas Sarjerao Ransing | works 145 | All India Institute of Medical Sciences Guwahati | topics: Mental Health Treatment and Access, COVID-19 and Mental Health, Suicide and Self-Harm Studies, Maternal Mental Health During Pregnancy and Postpartum
- https://openalex.org/A5136762259 | Ramdas Ransing | works 14 | All India Institute of Medical Sciences Guwahati | topics: Mental Health Treatment and Access, Suicide and Self-Harm Studies, Health Policy Implementation Science, School Health and Nursing Education

### Ramdas Sarjerao Ransing (All India Institute of Medical Sciences Guwahati) — 8 relevant of top 40 cited
- 2021 | Current state of cannabis use, policies, and research across sixteen countries: cross-country comparisons and international perspectives | Trends in Psychiatry and Psychotherapy | https://doi.org/10.47626/2237-6089-2021-0263
- 2020 | Telepsychiatry and healthcare access inequities during the COVID-19 pandemic | Asian Journal of Psychiatry | https://doi.org/10.1016/j.ajp.2020.102234
- 2020 | Telepsychiatry During the COVID-19 Pandemic: Development of a Protocol for Telemental Health Care | Frontiers in Psychiatry | https://doi.org/10.3389/fpsyt.2020.552450
- 2017 | Mean Platelet Volume and Platelet Distribution Width Level in Patients with Panic Disorder | Journal of Neurosciences in Rural Practice | https://doi.org/10.4103/jnrp.jnrp_445_16
- 2021 | Training and education in digital psychiatry: A perspective from Asia‐Pacific region | Asia-Pacific Psychiatry | https://doi.org/10.1111/appy.12501
- 2021 | Alcohol and Tobacco Use During the COVID-19 Pandemic. A Call for Local Actions for Global Impact | Frontiers in Psychiatry | https://doi.org/10.3389/fpsyt.2021.634254
- 2022 | Association of Internet gaming disorder symptoms with anxiety and depressive symptoms and substance use: an international cross-sectional study | Middle East Current Psychiatry | https://doi.org/10.1186/s43045-022-00180-6
- 2021 | The Impact of Stigma on Treatment Services for People With Substance Use Disorders During the COVID-19 Pandemic—Perspectives of NECPAM Members | Frontiers in Psychiatry | https://doi.org/10.3389/fpsyt.2021.634515

### Ramdas Ransing (All India Institute of Medical Sciences Guwahati) — 1 relevant of top 9 cited
- 2026 | Implementing integrated mental health and substance use disorder services in Indian primary care: a multi-state CFIR-based qualitative study | International Journal for Equity in Health | https://doi.org/10.1186/s12939-026-02986-w

## Pranjal Dey
Candidate author records (OpenAlex):
- https://openalex.org/A5109688305 | Pranjal Dey | works 14 |  | topics: Substance Abuse Treatment and Outcomes, Neurotransmitter Receptor Influence on Behavior, Mental Health Treatment and Access, Psoriasis: Treatment and Pathogenesis
- https://openalex.org/A5115419920 | Dey Pranjal | works 1 | All India Institute of Medical Sciences Guwahati | topics: Hearing Loss and Rehabilitation, Hearing, Cochlea, Tinnitus, Genetics, Vestibular and auditory disorders

### Pranjal Dey () — 2 relevant of top 14 cited
- 2021 | Efficacy of continuous theta burst stimulation - repetitive trancranial magnetic stimulation on the orbito frontal cortex as an adjunct to naltrexone in patients of opioid use disorder and its correlation with serum BDNF levels: a sham-controlled study | Journal of Addictive Diseases | https://doi.org/10.1080/10550887.2021.2007716
- 2025 | Low dose baclofen and standard dose acamprosate had comparable changes in brain glutamate, brain Gamma amino butyric acid (GABA) and craving among patients with alcohol dependence syndrome: A 1H-MRS based open label randomized study | Industrial Psychiatry Journal | https://doi.org/10.4103/ipj.ipj_187_23

### Dey Pranjal (All India Institute of Medical Sciences Guwahati) — 0 relevant of top 1 cited

## Sai Krishna Tikka
Candidate author records (OpenAlex):
- https://openalex.org/A5016097281 | Sai Krishna Tikka | works 181 | All India Institute of Medical Sciences Bibinagar, All India Institute of Medical Sciences | topics: Schizophrenia research and treatment, Transcranial Magnetic Stimulation Studies, Mental Health and Psychiatry, Electroconvulsive Therapy Studies
- https://openalex.org/A5026311557 | S. Leela Rama Krishna | works 3 | Aditya University | topics: Dementia and Cognitive Impairment Research, Alzheimer's disease research and treatments, Food composition and properties, Pharmaceutical Practices and Patient Outcomes

### Sai Krishna Tikka (All India Institute of Medical Sciences Bibinagar All India Institute of Medical Sciences) — 20 relevant of top 40 cited
- 2016 | The efficacy of cerebellar vermal deep high frequency (theta range) repetitive transcranial magnetic stimulation (rTMS) in schizophrenia: A randomized rater blind-sham controlled study | Psychiatry Research | https://doi.org/10.1016/j.psychres.2016.07.023
- 2020 | Efficacy of Intensive Cerebellar Intermittent Theta Burst Stimulation (iCiTBS) in Treatment-Resistant Schizophrenia: a Randomized Placebo-Controlled Study | The Cerebellum | https://doi.org/10.1007/s12311-020-01193-9
- 2023 | Clinical Practice Guidelines for the Therapeutic Use of Repetitive Transcranial Magnetic Stimulation in Neuropsychiatric Disorders | Indian Journal of Psychiatry | https://doi.org/10.4103/indianjpsychiatry.indianjpsychiatry_492_22
- 2021 | Efficacy of intensive orbitofrontal continuous Theta Burst Stimulation (iOFcTBS) in Obsessive Compulsive Disorder: A Randomized Placebo Controlled Study | Psychiatry Research | https://doi.org/10.1016/j.psychres.2021.113784
- 2021 | Repetitive transcranial magnetic stimulation and its role in suicidality – A systematic review | Asian Journal of Psychiatry | https://doi.org/10.1016/j.ajp.2021.102755
- 2015 | Resting State Dense Array Gamma Oscillatory Activity as a Response Marker for Cerebellar-Repetitive Transcranial Magnetic Stimulation (rTMS) in Schizophrenia | Journal of Ect | https://doi.org/10.1097/yct.0000000000000242
- 2022 | Safety and Efficacy of Continuous Theta Burst “Intensive” Stimulation in Acute-Phase Bipolar Depression | Journal of Ect | https://doi.org/10.1097/yct.0000000000000870
- 2015 | Adjuvant low-frequency rTMS in treating auditory hallucinations in recent-onset schizophrenia: a randomized controlled study investigating the effect of high-frequency priming stimulation | Annals of General Psychiatry | https://doi.org/10.1186/s12991-015-0046-2
- 2014 | Schneiderian First Rank Symptoms and Gamma Oscillatory Activity in Neuroleptic Naïve First Episode Schizophrenia: A 192 Channel EEG Study | Psychiatry Investigation | https://doi.org/10.4306/pi.2014.11.4.467
- 2022 | “Efficacy of intensive bilateral Temporo-Parietal Continuous theta-burst Stimulation for Auditory VErbal hallucinations (TPC-SAVE) in schizophrenia: A randomized sham-controlled trial”☆ | Asian Journal of Psychiatry | https://doi.org/10.1016/j.ajp.2022.103176

### S. Leela Rama Krishna (Aditya University) — 0 relevant of top 3 cited

**Reading.** Sharad Philip (AIIMS Guwahati; already the guide per Dr Reddy): implementation and tele-mental-health (ICMR-MINDS, tele-training, smartphone-use behaviour). No TMS papers in his top-cited list. Ramdas Ransing (AIIMS Guwahati): digital psychiatry, telepsychiatry, substance-use policy. A natural co-guide for Lane 2's digital delivery. **Pranjal Dey**: first author of a sham-controlled **cTBS (OFC) RCT in opioid use disorder** and a 1H-MRS alcohol study. The one person in the list with hands-on TBS-in-addiction trial experience. OpenAlex shows no current affiliation, and the AIIMS Guwahati record is an ENT namesake; confirm where they are now. **Sai Krishna Tikka**: now at **AIIMS Bibinagar**, not Guwahati; prolific in intensive TBS (schizophrenia, OCD, bipolar) and co-author of the Indian rTMS clinical practice guidelines (Indian J Psychiatry 2023). A strong external DC member for Lane 1.

---

## 6. ANRF project (department's technology-for-continuity-of-care study)

**Bottom line:** The project is confirmed as an ANRF-sanctioned study under Dr. Sharad Philip. I could not find its total amount, the app or platform name, or the SERB link. All sources are secondary (search results and web pages); I did not see a primary sanction letter or the full notice PDF.

| Field | Finding | Status | Source |
|---|---|---|---|
| Project title | "Leveraging Technology for Continuity of Care in Substance Use Disorders, including Intravenous Drug Use in Assam: An Intervention Study" | Confirmed (secondary) | https://aiimsguwahati.in/viewfile.aspx?fname=1a00960d.pdf&ftype=pdf&rdoctype=cms |
| PI | Dr. Sharad Philip, Assistant Professor, Department of Psychiatry, AIIMS Guwahati | Confirmed (secondary) | Same notice PDF |
| Funding agency / scheme | Anusandhan National Research Foundation (ANRF), New Delhi. The notice names ANRF only; I found no mention of SERB in the results. | ANRF confirmed; SERB NOT FOUND | Same notice PDF |
| Duration | Sanctioned for up to 3 years | Confirmed (secondary) | Same notice PDF |
| Total project amount | NOT FOUND | — | Searched the notice and related pages; not stated |
| Staff emoluments | The notice lists a Fellow amount of Rs. 37,000/- but the text is truncated, so I cannot confirm whether this is monthly or what the Associate amount is | Unclear | Same notice PDF |
| App / platform | NOT FOUND. The LinkedIn post describes it as technology-enabled, but names no app. | — | https://www.linkedin.com/in/dr-sharad-philip-6b4161203/ |

**Recruitment notices for this project**

1. **Research Fellow (ANRF project).** AIIMS Guwahati advertised a contractual Research Fellow post in this project. The notice is dated 15 Aug 2026 on the page metadata. The text I could see did not show a closing date, so I did not confirm one. Source: https://aiimsguwahati.in/viewfile.aspx?fname=1a00960d.pdf&ftype=pdf&rdoctype=cms
2. **Project Associate-I / JRF (possibly the same project).** A LinkedIn post by Dr. Philip describes a Project Associate-I/JRF post in the Department of Psychiatry under an ANRF-funded project on technology-enabled continuity of care for SUD in Assam, with a last date of 28 August 2026. Source: https://www.linkedin.com/in/dr-sharad-philip-6b4161203/ . A third-party listing gives the offline deadline as 29-08-2026 and requires a Master's in Psychology or Social Work: https://www.freejobalert.com/articles/aiims-guwahati-project-associate-i-junior-research-fellow-recruitment-2026-apply-offline-3063281 . I could not confirm from the results that this is the same advertisement as item 1, and the two sources disagree on the date.

**Not found:** the notice's registration number, the full eligibility list, and the official closing date for the Research Fellow post. Checking the AIIMS Guwahati website (aiimsguwahati.in) or the full PDF would settle these.

Local corroboration: `Desktop/rough research/interview/Filled/Result Notification_ANRF Leveraging Technology 19.10.2026.docx` (recruitment result notice; not opened beyond the file name) and the JRF/Project Associate applicant spreadsheets in Downloads (personal data; not opened).
