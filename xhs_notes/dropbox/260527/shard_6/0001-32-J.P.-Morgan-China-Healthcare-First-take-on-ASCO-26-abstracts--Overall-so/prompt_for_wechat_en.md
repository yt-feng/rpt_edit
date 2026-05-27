You are a senior financial newsletter editor with a consulting-style strategy lens. You turn research-report material into a long-form English article that is structured, insightful, and suitable for a serious business audience.

Objective:
- Write an English Markdown article based on the report parsing below.
- Target length: around 2200 words, plus or minus 15%.
- Tone: serious, analytical, strategic, and readable.
- The article should not feel like a summary. It should make an argument.
- You may extend the report's logic into reasonable second-order implications, but do not invent data, company actions, or quotes.
- Do not disclose every detail. Leave several meaningful open questions that make readers want the full report.

McKinsey-style writing principles:
1. Answer first: open with the controlling idea, not background.
2. Governing thought: every section must support the main answer.
3. Mutually exclusive, collectively exhaustive logic: avoid overlapping sections.
4. So what: every section must explain why the point matters.
5. Synthesis over summary: do not list facts; interpret what the pattern means.
6. Action titles: section headings must be complete, insight-bearing sentences. Do not use generic headings such as "Key Takeaways", "Market Background", "Core View", or "Reader Implications".
7. Natural hooks: if you want readers to join the community or read the full report, the hook should emerge from unresolved analytical questions, not from promotional language.

Required Markdown structure:
- `# Title`: make it a direct argument, not a topic label.
- Opening: 4-6 short paragraphs that state the main thesis and why now matters.
- 4-6 `##` sections. Each `##` heading must be an action title: a sentence that tells the reader the insight.
- One section should identify what the report does not fully answer yet.
- One section should translate the report into a decision framework for readers.
- Final section: naturally invite readers to join the community or read the full report using this CTA: Join the community to read the full report and review the original charts.
- End with: `*This article is for learning and discussion only and does not constitute investment advice.*`

Content boundaries:
- Do not mention specific investment bank names such as GS. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
"""
# China Healthcare

First take on ASCO'26 abstracts: Overall solid efficacy/safety

ASCO'26 released regular abstracts on Monday (May 25 $^{th}$ ) morning HKT for its upcoming conference over May 29 to June 2. The most important data presentation at ASCO'26 from a Chinese company will be Akeso's HARMONi-6 OS interim readout on May 31. We think a number of Chinese biotech and pharma companies will present key data at ASCO'26 - e.g., Kelun Biotech on sac-TMT (see our prior note), Innovent on IBI363, CStone on CS2009, among others. Overall, multi-specific antibodies and ADC continue to be key modalities for Chinese companies, given many Chinese companies will be presenting relevant data.

Hengrui's camrelizumab + rivoceranib + TACE deliver a meaningful but not transformative Phase 3 win in intermediate HCC. The PFS HR of 0.73 is more modest than the earlier Phase 2 suggested — a typical pattern when patient selection broadens — but the result is statistically clean and filing-ready. The more important read is strategic: this positions C+R across both the 1L systemic setting and now the TACE combination setting, covering the two largest HCC patient pools in China. The high grade ≥3 TRAE rate will be the main pushback from treating physicians at scale. The eventual OS readout will determine whether this becomes a genuine standard-of-care shift or a niche label.

Hengrui's trastuzumab rezetecan (SHR-A1811) delivers commercially significant result — the first Phase 3 positive ADC in refractory HER2-positive CRC. The clinical bar here is low (SOC delivers \~4–5% ORR) and this drug clears it emphatically. The key question is not whether it works, but whether Hengrui can convert it into a commercial win against T-DXd, which has first-mover advantage globally but no China domestic approval. OS immaturity at this early cutoff is not a concern — PFS and ORR data are sufficient for filing. Watch for the NMPA NDA submission timing as the next catalyst.

Hengrui's fuzuloparib (FUZUPRO trial) joins a crowded but validated class — PARP inhibitor + novel hormonal agent combinations in mCRPC. The overall rPFS benefit is positive but modest at HR 0.71, and critically, OS shows no separation at interim (HR 0.96), which will temper enthusiasm from payers and physicians. The DRD+ subgroup tells a more interesting story — HR 0.51 is clinically meaningful and in line with comparable data from olaparib+abiraterone and niraparib+abiraterone. The commercial challenge is that HRR-selected PARP combinations are already approved globally; fuzuloparib's path depends on China-first positioning and whether a China-only approval can anchor a credible partnership deal.

Hengrui's SHR-A2102 (Nectin-4 ADC) combined with adebrelimab puts up a pCR of 48% in perioperative MIBC — a number that directly challenges EV+pembrolizumab, the current benchmark in this space. The key differentiation is cisplatin-ineligibility: unlike standard NAC regimens, SHR-A2102 + adebrelimab showed no signal of harm in patients with impaired renal function, which is highly relevant given that >50% of MIBC patients are cisplatin-

# Healthcare

# Yang Huang AC

(852) 2800 3812

yang.huang@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

# Derek Choi

(852) 2800-8744

derek.c.choi@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

# Eric Zhao, CFA

(86-21) 6106 6256

eric.zhao@JPM.com

SAC Registration Number: S1730524050001

JPM Securities (China) Company Limited

ineligible. This is early Phase 2 data on n=37 and the pCR rate needs to hold in the Phase 3 expansion — but the signal is genuinely impressive and positions Hengrui's ADC pipeline in the bladder cancer space with a clear commercial narrative.

Innovent's IBI363 (PD-1xIL-2 alpha-biased bsAb) demonstrated solid efficacy in 1L NSCLC with AE profile manageable. Innovent has selected 3-1.5 mg as the dosing schedule to go forward, which is to give IBI363 3 mg/kg plus PDC (platinum-based doublet-chemotherapy) in cycle 1, then 1.5 mg/kg Q3W plus PDC in subsequent cycles. Grade≥3 treatment-emergent adverse events (TEAEs) occurred in 65.2% for the 3-1.5 mg/kg cohort. IBI363-related AEs led to corresponding treatment discontinuation and death in 6.3% and 1.3% patients. We think there might be no death in the 3-1.5 mg/kg cohort given there was only one death among 80 patients across three dosing cohorts. ORR was 86.4% (confirmed ORR [cORR]: 81.8%) and DCR was 100% for 3-1.5 mg/kg cohort. This is very good ORR with similar ORR in squamous and non-squamous patients, which is higher than the ORR of \~70% by PD-1xVEGF bsAb plus chemo. Interestingly enough, the ORR in the 3 mg/kg and 1.5 mg/kg are much lower than the 3-1.5 mg/kg cohort.

Akeso: Neoadjuvant Ivonescimab plus chemo demonstrated good radiological response depth and pathological remission rates in locally advanced head and neck squamous cell carcinoma (LA-HNSCC). In the Ph2 study, the efficacy readout is solid with radiological ORR at 100% (CR 50%, PR 50%) among 34 evaluable patients. Of 30 patients who proceeded to surgery, overall pCR was 50% (15/30), with primary lesion pCR of 70% (21/30) and lymph node pCR of 64.3% (18/28), and critically 100% R0 resection and 100% laryngeal and pharyngeal preservation were achieved. The biomarker data are also actionable with median CPS of 30 in pCR patients versus 10 in non-pCR, and 100% of patients with CPS>30 achieved pCR, suggesting a strong PD-L1 enrichment signal consistent with ivonescimab's PD-1 mechanism. Safety was broadly manageable, according to the abstract, but no further details have been given so far.

Ivonescimab combined with liposomal irinotecan demonstrated encouraging anti-tumor activity with a manageable safety profile in 2L SCLC pts. The Ph2 trial that enrolled 60 SCLC patients showed 6-month PFS rate of 72% at a median follow-up of 7.3 months, with confirmed ORR of 61.7%, DCR of 91.7%, and mPFS of 9.8 months. Subgroup stratification by chemo-free interval (CFI) showed mPFS of 11.9 months in CFI ≥90 days versus 7.0 months in CFI <90 days, suggesting platinum sensitivity status is still meaningful. The safety profile also looked good with grade ≥3 TRAEs occurring in 26.7% of patients, driven primarily by haematologic events, with no patient discontinuing all drugs due to TRAEs and no grade ≥4 immune-related AEs. Compared to the new standard of care tarlatamab (DLL3×CD3 BiTE), which showed ORR of 40% and mPFS of 4.9 months in the Ph2 DeLLphi-301 study (n=100), ivonescimab's 61.7% ORR and 9.8-month mPFS appear superior. However, DeLLphi-301 enrolled a more heavily pre-treated population (≥2 prior lines). Against the older SOC of lurbinectedin (Ph2: ORR 35.2%, mPFS 3.5 months), ivonescimab's efficacy profile also looks better, as well as a more favorable safety profile (grade ≥3 TRAEs 26.7% vs lurbinectedin's 46% grade 3/4).

Cadonilimab combined with axitinib demonstrated encouraging efficacy and tolerability in 1L advanced non-clear cell renal cell carcinoma (nccRCC) in the Phase Ib/II trial (n=37). In Ph1b, no DLTs were observed and the RP2D was confirmed at 10mg/kg Q3W; grade ≥3 TRAEs occurred in 66.7%. In Ph2, the primary endpoint ORR was 51.6% with a DCR of 96.8%; median PFS was 16.7 mos. The total cohort (Ph1b+Ph2) mPFS was 17.3 mos. Grade ≥3 TRAEs occurred in 58.1% of Ph2 patients, largely within expectations and manageable. In comparison, we identified 2 Ph2 comparators as pembrolizumab plus lenvatinib (KEYNOTE-B61, n=158) and nivolumab plus cabozantinib (n=40). KEYNOTE-B61 delivered an ORR of 51% and mDOR of 19.5 months at 22.8-month follow-up; nivolumab plus cabozantinib showed ORR 48%, mPFS 13 months, and mOS 28 months at 34-month follow-up. Against these benchmarks, cadonilimab's Ph2 ORR of 51.6% is essentially in line, while the mPFS of 16.7 months nominally exceeds nivolumab plus cabozantinib's 13 months, though the comparison is confounded by cadonilimab's shorter follow-up (14.4 vs 34 months).

Ascentage: Olverembatinib combined with blinatumomab showed solid clinical activity in patients with R/R Ph+ BCP-ALL or CML-LBP outside China. The Phase 1b 3+3 dose-escalation study enrolled 9 heavily pre-treated adults with R/R Ph+ BCP-ALL (n=8) or CML-LBP (n=1) outside China, with 6 patients having received and relapsed on prior blinatumomab. At 30mg QOD (n=3) no DLTs were observed; one DLT (grade 3 pancreatitis) occurred at 40mg QOD but resolved with dose reduction, and that patient achieved CR and MRD negativity. Safety was broadly manageable with grade ≥3 olverembatinib-related events in 4/9 patients.

Kelun Biotech: SKB500 (B7-H3-targeted ADC) demonstrated a manageable safety profile and antitumor activity in patients with refractory solid tumors, with notable efficacy in SCLC and ESCC. The FIH Ph1 trial enrolled 150 patients, establishing the RP2D at 12 mg/kg. Among 55 patients treated at 12 mg/kg with ≥6 weeks of follow-up (76.4% prior IO, 98.2% prior platinum, 34.5% ≥2 prior lines), overall confirmed ORR was 54.5% and DCR 92.7%. Efficacy was notable in SCLC and ESCC: SCLC (n=21) delivered ORR 71.4% and DCR 100%, while ESCC (n=18) showed ORR 55.6% and DCR 88.9%. The safety profile at 12 mg/kg is also promising with grade ≥3 TRAEs occurring in only 16.5%, with zero treatment discontinuations and only 2 cases of pneumonitis (2.1%), both grade 1 with no grade ≥2 ILD events.

Lunbotinib demonstrated robust efficacy in patients with advanced RET-fusion positive NSCLC, with high ORR and prolonged PFS in both pre-treated and treatment-naïve populations, and notable intracranial activity. The pivotal Ph2 study enrolled two cohorts: 71 pre-treated patients (platinum + IO) and 92 treatment-naïve (TN) patients. IRC-confirmed ORR reached 87.1% in pre-treated and 81.3% in TN patients; mPFS of 27.5 months in pretreated and NR in TN. Intracranial activity is a notable standout: among patients with baseline CNS metastases (23 pre-treated, 16 TN), ORR was 82.6% and 75% respectively, with 6 complete intracranial responses in each cohort. On safety, TRAEs occurred in 98.8% with grade≥3 in 40.5%, and only 1.2% discontinued due to TRAEs with no fatal events. Compared with first-generation selective RET inhibitors, selpercatinib (pretreated ORR 62%, mPFS 26.2 months; TN ORR 83%, mPFS 22.0 months; CNS-ORR 85%) and pralsetinib (pretreated ORR 59–63%, mPFS 16.5 months; TN ORR 72–78%, mPFS 13.0 months), Lunbotinib's pretreated ORR is much higher than both, while TN ORR is largely comparable. Lunbotinib's pretreated mPFS is broadly comparable to selpercatinib and materially superior to pralsetinib.

BeOne: BGB-B2033 (GPC3×4-1BB BsAb) was generally well tolerated in the Ph1 study in solid tumors, and durable responses were observed in pts with advanced HCC. The FIH Ph1 enrolled 61 patients across 8 dose levels. The safety profile is the validation of the molecule's engineering thesis: grade ≥3 treatment-related adverse events in only 8.2% of patients (5/61), immune-mediated AEs in 6.6% all grade 1–2, one DLT resolved after dose reduction, and no systemic 4-1BB-class hepatotoxicity signal. Efficacy in 59 HCC-evaluable patients shows confirmed ORR of 20.3% (All PRs), with 10/12 responses ongoing at data cutoff; at doses above the predicted target-efficacious threshold (n=38), ORR rises to 28.9% and motivates expansion into higher-dose cohorts.

BG-C9074 (B7-H4 ADC) demonstrates robust antitumor activity especially in OC and TNBC in the FIH Ph1 study (n=123, median 4 prior lines), but safety profile might be a concern. Confirmed ORR was 28.1% (2 CRs, 30 PRs) in the heavily pre-treated 114 evaluable patients at 6-month median follow-up, with an 33.3% unconfirmed ORR. Notably, responses showed no consistent correlation with B7-H4 expression, supporting an all-comers label strategy. However, safety is the main concern. Eight DLTs occurred across 6–9 mg/kg, including thrombocytopenia and febrile neutropenia at 6.5–7 mg/kg, and critically one unexplained death at 9 mg/kg.

BGB-43395 (CDK4 inhibitor) demonstrates an ORR of 58%/68% in 240/400 mg group, respectively, in CDK4/6i-naive pts with advanced or metastatic HR+/HER2− breast cancer. Without considering baseline difference, the ORR of BGB-43395 is somewhat higher than approved CDK4/6 inhibitors but not significantly higher. TEAEs led to dose modification in 53% of pts with 600mg group having the most dose change, and discontinuation occurred in 3% of patients.

CStone: CS2009 (PD-1xVEGFxCTLA-4 trispecific antibody) demonstrated an ORR of 20% among 40 NSCLC patients with >=2L prior therapies, which we consider much better than SoC. In the 30mg/kg group, ORR was 25%. Any-grade and grade ≥3 treatment-related adverse events (TRAEs) occurred in 27 (67.5%) and 8 (20.0%) patients, respectively, which we consider totally manageable. Updated efficacy and safety data in \~50 1L pts will be disclosed at the conference.

CSPC: SYS6002/CRB-701 (Nectin-4 ADC) has shown promising efficacy in patients with R/M cervical cancer, as well as a favorable safety profile. This Phase 1/2 update reports the cervical cancer cohort from parts A (dose escalation) and B (dose optimization), enrolling 54 R/M cervical cancer patients with ≥1 prior line. While most patients were still awaiting a confirmatory scan at data cut, the confirmed ORR was 5.6% at 2.7 mg/kg and 18.8% at 3.6 mg/kg; the unconfirmed ORR was 22.2% at 2.7 mg/kg and 37.5% at 3.6 mg/kg. An additional 6-month follow-up analysis with confirmed ORR, DOR, and PFS will be presented at ASCO meetings. The relevant clinical comparator for cervical cancer is tisotumab vedotin (Tivdak, Genmab/Pfizer), the only approved ADC in this setting, which has confirmed ORR of 24%, which is largely comparable with CRB-701's unconfirmed ORR.

SYS6043 (B7-H3 ADC) demonstrated robust cross-tumor antitumor activities and manageable safety. The Ph1/2 FIH study enrolled 502 patients across 8 tumor types, and DLTs (grade 3 GI disease and grade 4 febrile neutropenia) occurred at 10.0 mg/kg Q3W, with the RP2D set at 6–8 mg/kg Q3W. TRAEs occurred in 94.2% of patients; grade ≥3 in 28.5%, driven mainly by anemia (52%). The efficacy readout across Q3W cohorts is robust in breadth and magnitude: SCLC (n=50) ORR 75% including 1 CR at the 6mg/kg Q3W dose (n=28); breast cancer (n=55) ORR 83.8%/DCR 100%; nsq-NSCLC (n=34) ORR 57.1%; OC (n=46) ORR 46.2%/mPFS 5.6 months; and cervical (n=26), NPC (n=29), and EC (n=20) ORRs of 38.5%, 37.9%, and 30% respectively.

Innocare: Based on a global Ph1 trial, in treatment naïve (TN) AML patients, mesutoclax plus azacitidine (AZA) achieved a CR rate of 65.7% (23/35) and the MRD negative rate among those with cCR (composite complete response) is 86.7% (26/30). Although both CR rate and MRD negative rate are higher than Ascentage's lisaftoclax and BeOne's sonrotoclax, we think that could be partially because in the mesutoclax trial, patients were much younger. Among treatment-naive MDS patients, mesutoclax plus azacitidine (AZA) achieved ORR of 100% with CR of 20%. The ORR is higher than that in lisaftoclax's trials but the CR rate is lower. In terms of BCL-2+BTK, mesutoclax plus orelabrutinib achieved 100% ORR in R/R MCL, R/R MZL, TN CLL/SLL, suggesting similar ORR vs. other BCL-2+BTK combo.

Fosun Pharma: Luvometinib, MEK1/2 inhibitor, achieved confirmed BIRC (Blind Independent Review Committee) ORR of 43.8%, compared with 10.9% with placebo (p <0.0001) in a China Ph3 trial in adults with NF1 (neurofibromatosis type 1) and symptomatic, inoperable PNs (plexiform neurofibromas). Luvometinib will compete with selumetinib by AstraZeneca in the China market.

Biokin: For iza-bren in Ph3 trial of 2L ESCC, the median OS was 9.8 mo with iza-bren and 7.2 mo with chemotherapy (HR, 0.64; 95% CI, 0.49 to 0.83; P = 0.0004). The median PFS by BICR was 4.2 mo with iza-bren and 2.0 mo with chemotherapy (HR, 0.50; 95% CI, 0.40 to 0.63; P < 0.0001). ORR by BICR was 35.3% for iza-bren and 13.1% for chemotherapy. Grade≥3 TRAEs, which were predominantly hematologic in nature, occurred in 85.1% in the iza-bren group and 60.2% in the chemotherapy group. The overall efficacy and safety profile met our expectation.

Zelgen: The updated results of ZG006, a TCE targeting DLL3/DLL3/CD3, continue to demonstrate its ORR of 50%+ in 10mg Q2W for 3L+ SCLC patients, suggesting consistency with prior data. Median OS can potentially reach 15-16 months, which is very solid in 3L+ SCLC, much better than SoC.

Henlius's serplulimab (ASTRUM-006) is the only perioperative gastric PD-1 trial to read out at ASCO 2026, and the pCR delta of >15 percentage points is clinically meaningful. The EFS benefit in the CPS≥5 subgroup is the regulatory-relevant endpoint, but the question is whether Henlius can translate a statistically significant result into commercial traction in a market already served by tislelizumab and sintilimab in the periop setting. Serplulimab's differentiation remains primarily on price, not efficacy, and this dataset — while solid — is unlikely to shift prescribing patterns materially outside China.

Henlius's HLX43 (PD-L1 ADC) demonstrated promising efficacy in a pooled analysis of Ph1 and global Ph2 in 3L+ NSCLC. Across 5 dose groups (mainly 2 mg/kg and 2.5 mg/kg), ORR was \~31%. In non-squamous NSCLC, ORR appears to be higher than in squamous NSCLC. As a monotherapy, ORR of 30%+ in 3L+ NSCLC looks pretty solid. TRAEs led to treatment discontinuation in 17 (8.3%) patients, which suggests a manageable safety profile.

Hutchmed's savolitinib is on the cusp of becoming the first approved selective MET inhibitor for gastric cancer in China — and this ASCO 2026 readout is the full pivotal dataset supporting that NDA, already accepted with priority review by NMPA in December 2025. The ORR of 32% in a heavily pretreated, biomarker-selected population is clinically meaningful, and the rapid time to response of 1.4 months speaks to genuine target engagement. MET amplification as a driver in gastric cancer is under-exploited commercially, and a China approval would give Hutchmed/AZ a genuine first-mover position in a biomarker-enriched segment. The near-term binary catalyst is the NMPA approval decision, expected H2 2026.

Hutchmed and Innovent's fruquintinib + sintilimab (FRUSICA-2) presents one of the most compelling efficacy datasets in 2L+ RCC — mPFS of 22.2 months and ORR of 60.5% against a weak control are standout numbers. ASCO'26 abstract 4531 is a subgroup cut by IMDC risk and PD-L1 status, which will determine whether the benefit holds across all subgroups or is driven by a favourable-risk subset. O

[中间内容因长度限制已省略]

dates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All

Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 26 May 2026 04:14 AM HKT

Disseminated 26 May 2026 04:14 AM HKT
"""
