# 04 — AIIMS Guwahati PhD rules and IEC formats

Sources (downloaded 5 Nov 2026 to `~/thesis-papers/aiims/`, not committed):
- PhD prospectus R2: https://www.aiimsguwahati.ac.in/uploads/pdfs/PhDprospectus_AIIMSG-R2.pdf (14 pp)
- PhD advertisement / prospectus, July 2026 session (`PhD_Advertisement_Jul2026.pdf`, 12 pp)
- Local: `Downloads/PG & PhD coursework Schedule for July 2026 Batch.pdf` (scanned; read as image)

Extraction: text layer → `claude-haiku-5.5` asked to copy rule text verbatim with page → each passage string-matched against the PDF text. Items marked "check the page" failed the match only because of the PDF's column layout; the wording is very likely right but confirm before quoting.

## 1. The rules that matter, in plain language

- Jul 2026 advertises only Category A (funded-project fellowship, seat-specific) and Category C (own fellowship); R2 also has Category B (sponsored), and Category D (40 AIIMS fellowships a year).
- Registration runs a minimum of 3 years and a maximum of 5 years, with limited extensions (6 months, then up to 6 more in exceptional cases); the wording is identical in both files.
- Coursework is thin: R2 requires a research methodology course with an exit exam within 6 months and mandatory courses; Jul 2026 mentions only a course-work exam fee.
- R2 has detailed rules for Doctoral Committee formation (within 6 months), protocol submission (within 3 months of DC, no later than 9 months from registration) and ethics approval, plus 6-monthly DC reviews; none of these appear in Jul 2026.
- R2 requires at least 2 peer-reviewed publications (IF >1.5) or one with IF >3 before thesis submission, and sets out examiner panels, viva-voce and grading; Jul 2026 contains none of this.
- Guide and co-guide eligibility (publications, experience, caps on students and co-guide roles) is only in R2.
- Jul 2026 lists clinical trials as project titles under Category A seats (4M kids TB trial; cannabidiol Phase III alcohol trial), while R2 says nothing about clinical trials.
- R2 and Jul 2026 differ on fee amounts, nursing eligibility (R2 only), and the funding agencies named for Category C (R2 adds NBHM and GATE).

Additional points from reading the extract:
- **Timeline that binds the synopsis:** DC formed within 6 months of registration → protocol to DC within 3 months of DC formation and **no later than 9 months from registration** → DC suggestions → Dean's approval through the guide → IEC (approval "preferably within 3 months"). Biostatistician advice must be obtained for the protocol, and a biostatistician on the DC is "preferable".
- **Six-monthly DC meetings and graded reports** (Excellent/Good/Satisfactory/Poor). Two consecutive reports below "Good" → warning; a third → possible cancellation.
- **Publication gate before thesis submission:** 2 papers in journals with IF > 1.5, **or** 1 paper with IF > 3. Reprints go in the thesis.
- **Co-guide:** at least one co-guide from the candidate's own department. Co-guides need ≥ 3 original articles; guides ≥ 5.
- **Final DC** at least 6 months before the end of maximum registration; thesis within 6 months of DC permission; six external examiners proposed (up to two from abroad).
- **Category A seats (fellowship in a funded project):** the Jul 2026 advertisement lists **Psychiatry PSY02 with project title "Cannabidiol as an adjunctive short-term treatment during inpatient detoxification in patients with Alcohol dependence: A multicenter Phase III Randomized controlled trial"**. A Category A candidate is appointed to that project's fellowship post. If this is Dr Reddy's seat, the PhD is formally attached to the CBD trial (see `06-open-questions.md` Q1). Neither document discourages clinical trials as PhD topics; the Jul 2026 list includes two RCTs as Category A projects.
- **Coursework (local schedule):** "Basics of Research Methodology for PG & PhD students", issued by the Dean (Research): six or more one-hour sessions from 2 Sep 2026 (choosing the topic and research question; objectives and outcomes; literature search; descriptive, case-control and cohort designs; study designs; cross-sectional studies). Exit exam required within 6 months of registration per the R2 prospectus.

## 2. Verbatim passages

#### 1 registration period / minimum and maximum duration
*PhD_R2.txt, page 8 of 14* · verbatim match confirmed

> IX. Duration of Course 1. The duration of the course shall be the time period from registration to submission of thesis. The minimum period of registration in respect of all the candidates who are registered for Ph.D. shall be three years. The maximum period of registration shall not exceed five years. Extension beyond the period of 5 years can be given for a maximum period of 6 months on the recommendation of Doctoral Committee and final approval by Executive Director. Further extension beyond 5 years & 6 months can also be given by the Executive Director for a maximum period of 6 months in highly exceptional circumstances (like medical exigencies, natural calamities etc), subject to subsequent approval of the Academic Committee and such extension may not be given retrospectively. If thesis is not submitted within these timelines, the registration of the candidate may be summarily cancelled.

#### 1 registration period / minimum and maximum duration
*PhD_Jul2026.txt, page 10 of 12* · verbatim match confirmed

> 6. Duration of Course 1. The duration of the course shall be the time period from registration to submission of thesis. The minimum period of registration in respect of all the candidates who are registered for Ph.D. shall be three years. The maximum period of registration shall not exceed five years. Extension beyond the period of 5 years can be given for a maximum period of 6 months on the recommendation of Doctoral Committee and final approval by Executive Director. Further extension beyond 5 years & 6 months can also be given by the Executive Director for a maximum period of 6 months in highly exceptional circumstances (like medical exigencies, natural calamities etc), subject to subsequent approval of the Academic Committee and such extension may not be given retrospectively. If thesis is not submitted within these timelines, the registration of the candidate may be summarily cancelled.

#### 2 coursework
*PhD_R2.txt, page 10 of 14* · verbatim match confirmed

> 3. After registration, candidate must complete course in research methodology conducted by Research Section within 6 months of registration & should pass the exit exam.

#### 2 coursework
*PhD_R2.txt, page 14 of 14* · verbatim match confirmed

> XXI. Additional Points on Conduct of Ph.D. Course 1. A number of mandatory courses will be defined and developed for all Ph.D. students where attendance and evaluation will be compulsory. A certificate will be issued for courses attended by the candidates.

#### 2 coursework
*PhD_Jul2026.txt, page 11 of 12* · verbatim match confirmed

> 8 Course work examination fees 500/- 3 Years

#### 3 Doctoral Committee composition and when formed
*PhD_R2.txt, page 10 of 14* · verbatim match confirmed

> XIII. Formation of Doctoral Committee 1. The guide should submit a panel of experts to the Executive Director through proper channel for the constitution of Doctoral Committee (DC) for the candidate, within six months of the candidate's registration. ... 5. The DC shall consist of the following members. It is preferable to include � Biostatistician in the DC. a. Guide b. Minimum one expert from reputed organizations (External expert) c. Up to 3 experts from AIIIMS-G (Internal expert) d. Co-guide(s) e. HoD of the department where candidate is registered

#### 4 thesis protocol/synopsis submission timeline and approval route (incl. ethics)
*PhD_R2.txt, page 10 of 14* · verbatim match confirmed

> XIV. Submission of thesis protocol 1. After the constitution of DC, the candidate shall prepare a detailed protocol underlining his proposed research plan clearly stating the objectives and methodology to be employed. The protocol should also contain a brief formulation of the experimental designs & the advice of a biostatistician should invariably be obtained. 2. Protocol shall be submitted to the DC within 3 months of the formation of DC (but no later than 9 months from the date of registration). The DC will recommend the feasibility of the proposed research plan recommending such modification as the committee seems fit. The candidate will incorporate the suggestions of the DC and submit the final protocol for the approval of Dean through Guide. 3. After the approval of Dean, the research protocol will be submitted for the approval of ethics committee. 4. The approval from ethics committee must be obtained preferably within 3 months of submission of research protocol.

#### 5 progress assessment schedule (six-monthly reports etc.)
*PhD_R2.txt, page 11 of 14* · verbatim match confirmed

> XV. Assessment of the work of the candidates 1. The progress of the candidate work shall be periodically assessed by the DC and a report regarding the same shall be submitted to the Dean through the guide at the end of every 6 months. The grading of the candidate shall be done as Excellent/ good/ satisfactory/ poor. Any grading less than good is not acceptable. In case report of DC is below the accepted standard of good for two consecutive times, the candidate will be given a warning and in case further DC reports mentions the same grading, the registration of such candidates may be cancelled. 2. The Dean shall convey the candidate about the assessment report in writing (Excellent/Good/Satisfactory/Poor), and should also advise the candidate about his/ her short-comings.

#### 5 progress assessment schedule (six-monthly reports etc.)
*PhD_R2.txt, page 10 of 14* · verbatim match confirmed

> 5. The meetings of DC must be held every 6 months.

#### 6 publication requirements before thesis submission
*PhD_R2.txt, page 11 of 14* · verbatim match confirmed

> 3. Candidate shall be required to have 2 publications in peer reviewed journals with an Impact Factor > 1.5 or one publication in journals with Impact Factor more than 3 before the submission of the thesis. Reprints of these publications shall be included in the thesis.

#### 7 rules about theses within funded/extramural projects or project staff
*PhD_R2.txt, page 4 of 14* · **string-match failed (PDF column layout); check the page before quoting**

> 2. The individual should be a regular employee of the institute and should have rendered a minimum of five years of continuous service at the institute. The guidelines of in-service candidates will not be applicable to other staff members employed under various research schemes which are of tenure basis.

#### 7 rules about theses within funded/extramural projects or project staff
*PhD_R2.txt, page 6 of 14* · **string-match failed (PDF column layout); check the page before quoting**

> 1. Category A (Fellowship Available in Funded project) i. The candidates already working or interested to work under funded projects will apply under this category. ii. If selected for Ph.D. admission, they will be allowed to apply for JRF/SRF/equivalent position (depending upon experience) after joining the Ph.D. program. However, the candidates can not avail fellowship/salary from two different sources. iii. The number of seats available under this category will be provided to the academic section by the concerned department in the following format: [table: S. No. / Department / Project Title / Broad subject area proposed research for Ph.D. / Duration and Fellowship/Stipend per month (in Rs) / Any special requirement for the eligibility of candidates] iv. Candidates selected under this category will be automatically appointed to the fellowship posts within those projects for which they have been selected and no additional interviews will be held for selection on these posts within the project. (If the fellowship has some restrictions on eligibility of candidates, this must be stated as shown in the above table).

#### 7 rules about theses within funded/extramural projects or project staff
*PhD_Jul2026.txt, page 8 of 12* · verbatim match confirmed

> Note: 1) A candidate can submit application for one Department only. 2) If selected for Ph.D. admission, candidate(s) will be allowed to apply for JRF/SRF/equivalent position (depending upon experience) after joining the Ph.D. program. However, fellowship/salary cannot be availed from more than one source. 3) The posts are being advertised keeping in view the broad subject area of proposed research and general eligibility of applicants. The Department concerned may have specific requirement on the eligibility of candidates which will be adopted for shortlisting of candidates.

#### 8 any statement about clinical trials as PhD topics
*PhD_Jul2026.txt, page 7 of 12* · **string-match failed (PDF column layout); check the page before quoting**

> 8 Pharmacology Four-month moxifloxacin containing shorter regimen versus 6 months standard regimen for treatment of drug sensitive TB disease in children aged 1 year to 18 years � Open labelled randomised controlled trial (4M kids trial) Medical Device Monitoring Centre

#### 8 any statement about clinical trials as PhD topics
*PhD_Jul2026.txt, page 8 of 12* · **string-match failed (PDF column layout); check the page before quoting**

> 10 Psychiatry (PSY02) Cannabidiol as an adjunctive short-term treatment during inpatient detoxification in patients with Alcohol dependence: A multicenter Phase III Randomized controlled trial

#### 9 guide/co-guide eligibility and number of co-guides
*PhD_R2.txt, page 8 of 14* · verbatim match confirmed

> X. Eligibility Criteria for Recognition as a Ph.D. Guide and Co-Guide 1. Must have completed minimum 2 years as a regular faculty in the Institute. The last date for the calculation of two years will be 31 July for July session and 31 January for January session of respective year. For those with less than 2 years as faculty, exception on case-to-case basis, based on previous research experience of the faculty may be granted by the Executive Director. 2. The faculty member must have a medical postgraduate qualification or doctoral degree (MD/MS/MDS/DNB/DM/MCh/ Ph.D.). 3. The faculty member should have published minimum five original research articles to be a guide, and minimum three original research articles to be a co-guide (excluding case reports, review articles, editorial comment, and letter to editor) in PubMed, SCOPUS, or Web of Science indexed journals.

#### 9 guide/co-guide eligibility and number of co-guides
*PhD_R2.txt, page 9 of 14* · **string-match failed (PDF column layout); check the page before quoting**

> 7. There must be at least one co-guide from the department where the candidate is registered. If there is only one eligible guide in a department, a co-guide may be taken from another allied discipline/department of the Institute. 12. Each faculty member may guide a maximum of 8 MD/MS/MDS/DM/MCh/ Ph.D. students at any time. This will include a maximum of 5 Ph.D. students. 13. A faculty member of AIIMS-G with research experience can be a Co-Guide for a maximum of 5 Ph.D. theses of the Institute. In the event if a Faculty member is required to be a Co-Guide for more than 5 Ph.D. theses of the Institute, a special permission from the Executive Director, AIIMS-G will be required.

#### 10 thesis submission and evaluation
*PhD_R2.txt, page 11 of 14* · **string-match failed (PDF column layout); check the page before quoting**

> XVI. Thesis and Examination 1. No candidate will be allowed to submit thesis without the approval of the DC. The final DC meeting should be held at least 6 months before the end of the maximum registration period. After the recommendation of DC, the candidate will start writing the thesis. The same will be informed to the Dean in the DC report which should include a brief resume of the work done. 2. Candidate must submit thesis within 6 months of grant of permission by the DC. However, extension for maximum upto 3 months can be given by the Dean on the recommendation of guide mentioning justifiable reasons. 4. For the evaluation of Ph.D. thesis, the candidate shall submit four copies of his/her thesis along-with soft copy in CD/DVD not earlier than prescribed minimum period of 3 years and no later than the maximum period of registration (5 years or as the case may be). The thesis shall be certified by both the Guide and by the Co-Guide(s) before its submission. 5. The guide in consultation with the DC shall submit a panel of examiners at the time of submission of the final DC report that is at least six months before the expected date of submission of the thesis (end of registration period). The panel shall include six external examiners (of whom up to two may be from abroad) with their designation, complete postal address with PIN Code, e- mail, and telephone/mobile no.

#### 10 thesis submission and evaluation
*PhD_R2.txt, page 12 of 14* · **string-match failed (PDF column layout); check the page before quoting**

> 7. If both the examiners recommend acceptance of the thesis for the award of the Ph.D. degree, a public defence-cum-viva voce examination (here in after referred as viva voce examination) will be conducted to adjudge the general proficiency of the candidate in the subject allied to the candidate field of work of the thesis. 8. If the thesis is rejected by both examiners, it will stand rejected and shall not be referred to any other examiner. 19. The candidate shall be declared eligible for the award of the degree of Ph.D. only on the unanimous recommendations of the VVC for the award of the degree.

#### 11 differences between the R2 prospectus and the Jul 2026 advertisement
*PhD_Jul2026.txt, page 3 of 12* · verbatim match confirmed

> 2. Types of Ph.D. Seats 1. Category A (Fellowship Available in Funded project) 2. Category C (Candidates with own fellowship)

#### 11 differences between the R2 prospectus and the Jul 2026 advertisement
*PhD_R2.txt, page 6 of 14* · verbatim match confirmed

> VI. Types of Ph.D. Seats ... 2. Category B (sponsored candidates from other organization) ... 4. Category D (AIIMS Fellowship): Under this category, AIIMS-G will provide 40 fellowships each year (20 in each session) based on the performance of candidates in the entrance examination.

#### 11 differences between the R2 prospectus and the Jul 2026 advertisement
*PhD_R2.txt, page 3 of 14* · verbatim match confirmed

> 2. Nursing qualification: Candidates holding M.Sc. degree with minimum 55% aggregate marks in Nursing Specialty will also be eligible for Ph.D. admission in College of Nursing.

#### 11 differences between the R2 prospectus and the Jul 2026 advertisement
*PhD_Jul2026.txt, page 9 of 12* · verbatim match confirmed

> 5. General Eligibility A candidate seeking admission to the program of study leading to the award of Ph.D. degree must possess at least one of the following qualifications: 5.1. Medical qualification: MBBS/BDS with minimum 55% aggregate marks or MD/MS/MDS/DM/MCh in the subject concerned or equivalent Diplomate of National Board of Examination degree.

#### 11 differences between the R2 prospectus and the Jul 2026 advertisement
*PhD_R2.txt, page 7 of 14* · verbatim match confirmed

> ii. The candidates who secure 50% in stage I (40 marks) will be eligible for stage II (Interview). However, the number of candidates called for stage II (interview) shall not exceed three times the number of seats advertised under each guide.

#### 11 differences between the R2 prospectus and the Jul 2026 advertisement
*PhD_Jul2026.txt, page 11 of 12* · verbatim match confirmed

> ii. The candidates who secure 50% in stage I (40 marks) will be eligible for stage II (Interview). However, the number of candidates called for stage II (interview) shall not exceed three times the number of seats advertised.

#### 11 differences between the R2 prospectus and the Jul 2026 advertisement
*PhD_R2.txt, page 6 of 14* · verbatim match confirmed

> 3. Category C (candidates with own fellowship/in service candidates from AIIMS-G) i. The candidates with their own fellowships from recognized Government agencies such as CSIR, UGC, ICMR, DBT, NBHM, GATE, INSPIRE, or similar government agencies will apply under this category.

#### 11 differences between the R2 prospectus and the Jul 2026 advertisement
*PhD_Jul2026.txt, page 8 of 12* · verbatim match confirmed

> 3B. Category C (candidates with own fellowship) The candidates with their own fellowships from recognized Government agencies such as CSIR, UGC, ICMR, DBT, INSPIRE, or similar government agencies will apply under this category.

#### 11 differences between the R2 prospectus and the Jul 2026 advertisement
*PhD_R2.txt, page 13 of 14* · verbatim match confirmed

> XVIII. Structure of the Fees for admission to Ph.D. program ... 5 Hostel rent 4,125/- ... Total (Rs)

#### 11 differences between the R2 prospectus and the Jul 2026 advertisement
*PhD_Jul2026.txt, page 11 of 12* · verbatim match confirmed

> Total (Rs) 5,400/-

## 3. Institutional Ethics Committee: what is known

**Local structural evidence (headings only; other scholars' documents, content not reproduced):**
- An AIIMS Guwahati thesis protocol (another scholar's) follows **"Section III — Proforma to be submitted to the Institute Ethics Committee (Human Studies)"**. Its Informed Consent Document comes in **English, Hindi and Assamese**, followed by a consent form and a submission checklist. Checklist items include: exact title as approved by the Research Cell; date of approval; source of funding; validated questionnaire in Assamese, English and Hindi; no discrepancy between the three consent-form languages; ethical exemption form if applicable; questionnaire and patient proforma.
- A psychiatry IEC application from Assam (LGBRIMH Tezpur, another scholar) and `Downloads/CommonForms_Ethics_Committee_review.19032020.docx` both use the **ICMR Common Forms for Ethics Committee Review (2020)** structure: Section A basic information, administrative details, funding and budget, methodology, recruitment and participants, benefits and risks, informed consent, payment/compensation, storage and confidentiality, publication/benefit sharing/IPR, annexures (PIS, tool permissions, self-funding undertaking, amendment notification).

**Web search (SECONDARY):**

**Bottom line:** The search index has very little on the AIIMS Guwahati IEC itself. Most IEC templates it returned belong to AIIMS New Delhi, so don't treat them as Guwahati requirements without confirming with the Guwahati IEC or Research Cell. Everything below is SECONDARY (search snippets, not the primary documents).

## 1. Guwahati-specific pages found

| Item | URL | Notes |
|---|---|---|
| Committees page (member list, contact) | https://aiimsguwahati.ac.in/page/committees | Lists a contact mail, icc@aiimsguwahati.ac.in. It does not clearly identify an IEC section, so I could not confirm this is the IEC page. |
| Downloads / Scheduled Forms | https://aiimsguwahati.ac.in/page/downloads | Listed, but no form contents were returned. |
| Annexures PDF (PI declaration and related annexures) | https://aiimsguwahati.ac.in/uploads/pdfs/2-Annexures.pdf | Most relevant Guwahati document found. See section 2. |
| Ph.D. prospectus | https://aiimsguwahati.ac.in/uploads/pdfs/PhDprospectus_AIIMSG-R2.pdf | Covers thesis-protocol and doctoral committee rules. See section 4. |
| Research archive | https://aiimsguwahati.ac.in/page/recarchive | Recruitment notices only; nothing on ethics. |

## 2. Guwahati annexures: language and consent points

- **Languages:** Assamese, English & Hindi. The same document says the Informed Consent Document should comprise Patient Information Sheet and the consent form.
- **Style:** The investigator must provide information to the subjects in a simple language, and it should address the subjects, in a dialogue format.
- **Language rule for the sheet:** The sheet should be in language in English, Assamese and Hindi which can be understood by the participant.
- **Paediatric consent:** Studies involving children below 7 years should include parent / legally-authorized representative (LAR) consent form while studies involving children above 7 years and below 18 years of age should include assent form in addition to parent / LAR consent.
- **Separate consent forms:** A separate consent form for the patient/test group and control (drug/procedure or placebo) should be provided as applicable.
- **Other items the annexure lists:** a summary of about 300 words, Permission from DCGI (if applicable)., and a conflict-of-interest declaration covering the researcher is also the lecturer, teacher, treatment- provider, colleague or employer of the research participants.
- **Caveat:** The document is not clearly labelled as the IEC's, and the text refers to a "Research Cell". Confirm which body issues it.

## 3. Templates and submission rules (AIIMS New Delhi, not Guwahati)

These are the only consent-form and submission-format documents I found. They are New Delhi documents, dated 2012–2014.

- **Consent form (English/Hindi):** https://www.aiims.edu/aiims/academic/pic_ethics.pdf. Only the title block was returned. The English version is https://aiims.edu/aiims/academic/ethics-committee/Patient_Informed_Consent_Ethics_Committee.pdf.
- **Submission format (thesis/protocol):** https://www.aiims.edu/aiims/academic/ethics-committee/Format%20of%20Institution%20Ethics%20Committee.doc. Its sections include the Covering letter, Full title, Conflict of interest, Attached documents, and whether work has started. The attachment list covers the protocol, investigator CVs, investigator's brochure, an ICMR/GCP undertaking, and Participant Informed Consent Form (PICF) and Participant Information Sheet (PIS), both in English and Hindi.
- **Thesis format:** https://www.aiims.edu/aiims/academic/ethics-committee/Thesis%20Format%20IEC.pdf. It covers M.Ch/ MD / MS / MHA / MDS /M.Sc / M.Biotech./MBBS AND Ph.D. STUDENTS.
- **Download index:** https://aiims.edu/aiims/academic/ethics-committee/download_forms_in_msword_format.htm

## 4. Calendar and deadlines

- **Guwahati:** NOT FOUND. I searched the IEC and Research Cell pages and the annexure and prospectus documents and found no meeting or submission calendar.
- **New Delhi format (not Guwahati):** Proposals received till 15th of any month will be processed in the coming Institution Ethics Committee meeting and those received after 15th will be processed in the next Institution Ethics Committee meeting. Meetings are held as far as possible on first Monday of Jan, Feb, March, April, May, June, July, August, September, October, November, and December.
- **Conflicting version:** One 2014 New Delhi form says first Friday of Jan, Feb, March, April, May, June, July, August, September, October, November, and December.
- **Guwahati Ph.D. rules:** The meetings of DC must be held every 6 months. The prospectus also says on approval of their project by the ethics committee and submission of thesis protocol. that a research grant can be released to fellows.

## 5. Fees

- **Guwahati:** NOT FOUND. No fee schedule appeared in any search.

## 6. Insurance and compensation (interventional studies)

- **Guwahati:** NOT FOUND in any Guwahati document.
- **New Delhi format:** If insurance is intended, an insurance certificate must be provided (as per ICMR guidelines). The protocol must also state who bears the expenditure of injury. This is in the New Delhi format: https://www.aiims.edu/aiims/academic/ethics-committee/Format%20of%20Institution%20Ethics%20Committee.doc
- **General principle:** An IEC protocol must address proposed compensation, reimbursement of incidental expenses and management of research related injury/illness during and after research period and insurance policy. This comes from a different institute's SOP (AIIMS Bibinagar: https://aiimsbibinagar.edu.in/pdf/IEC/IEC%20SOP%20AIIMS%20BBN.pdf).

## 7. Serious adverse event (SAE) reporting

- **Form:** NOT FOUND for Guwahati. No SAE form appeared in the results.
- **Timelines in the New Delhi SOP:** Serious Adverse Effects should be reported to Institute Ethics Committee within 24 hours and to DCGI within 10 working days. Source: https://www.aiims.edu/aiims/academic/ethics-committee/forms%20in%20pdf/IEC/sop%20for%20Institute%20of%20Ethics%20Committee_1_5_14.pdf
- **Related rule:** The SOP also says the IEC Its function includes giving opinion on causality of Serious Adverse Events and also decide the amount of compensation to be given to the patients with trial related injury. This is a 2014 New Delhi document.

## 8. Not found, and suggested next steps

- Guwahati IEC fee schedule, meeting calendar, insurance requirements, and SAE form: **NOT FOUND**.
- Assamese participant sheet and consent template for Guwahati: **NOT FOUND** as standalone files. The only Assamese reference is the annexure requirement in section 2.
- Next steps: email the Member-Secretary (the IEC contact is listed on the committees page). Ask for the current SOP, the SAE form, the fee schedule, the meeting calendar, and the Assamese PIS/consent template. Also ask whether the 2014 New Delhi formats still apply to Guwahati.

## 4. Mismatches with `thesis/05-protocol-skeleton-aiims.md`

1. **Format basis.** The skeleton follows the AIIMS **New Delhi** IEC thesis format. Guwahati's evidence points to its own "Section III proforma" plus ICMR Common Forms (2020) section headings. Rebuild the skeleton's section order on the Common Forms headings and add the Guwahati checklist.
2. **Approval route missing.** The skeleton's pre-submission checklist says "through Chief Guide and HoD". The prospectus route is **DC → Dean (through guide) → IEC**, with the protocol due to the DC within 3 months of DC formation and ≤ 9 months from registration. Add the DC and Dean steps and the 9-month deadline.
3. **Research Cell step.** The Guwahati checklist asks for the "exact title as approved by Research Cell" and its approval date. The skeleton has no Research Cell step.
4. **Languages.** The skeleton says English, Hindi, Assamese "(and Bengali if needed)". Guwahati requires all three of English, Hindi and Assamese, **and validated questionnaires in all three**, with no discrepancy between versions. This makes scale translation (PACS, AEQ etc.) a pre-IEC task, not an annexure.
5. **Biostatistician.** The prospectus says biostatistician advice "should invariably be obtained" for the protocol. Add a biostatistician sign-off line to the skeleton.
6. **Six-monthly DC reports.** Not in the skeleton or the Gantt in `04-decision-and-integration.md`. Add DC meetings every 6 months.
7. **Publication gate.** Two papers with IF > 1.5 or one with IF > 3 before submission. `04-decision` plans four papers but does not check journal impact factors. *Indian J Psychiatry* and *Indian J Psychol Med* may fall below 1.5. Pick target journals now.
8. **Relationship to the CBD trial** is listed in the skeleton's ethics section as a choice. If the seat is Category A PSY02, the relationship is fixed by the seat, not chosen.
9. **Insurance, fees and IEC calendar:** NOT FOUND for Guwahati. Ask the IEC member secretary.
