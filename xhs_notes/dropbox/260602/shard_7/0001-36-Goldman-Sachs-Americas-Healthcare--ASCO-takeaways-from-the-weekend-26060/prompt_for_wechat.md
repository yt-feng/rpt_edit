你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：一句主判断，不超过 32 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Americas Healthcare: ASCO takeaways from the weekend

We are attending the American Society of Clinical Oncology (ASCO) meeting. SMMT's partner Akeso presented late-breaking Ph3 HARMONi-6 overall survival data during the plenary session (simultaneously published in The Lancet), where ivonescimab + chemotherapy demonstrated a statistically significant and clinically meaningful 27.9 month benefit vs. 23.7 months for Tevimbra (anti-PD-1) + chemotherapy in frontline squamous non-small cell lung cancer, with a hazard ratio (HR) of 0.66 (one-sided p=0.0017), exceeding the \~0.72 bar per our investor conversations and the <0.80 physician bar (see our takeaways here). Additional key presentations from companies within our coverage include: IMNM (full Ph3 results for varegacestat in desmoid tumors further support a best-in-class position over Merck KGaA's Ogsiveo, noting all alpha-controlled secondary endpoints including key pain relief metrics achieved statistical significance), GILD (updated Ph1 data for GILD's TUB-040 continue to show encouraging results, in-line with the prior update at ESMO, and support a potentially differentiated profile in ovarian cancer; we also note Ph3 subgroup analyses for Trodelvy in 1L TNBC), INCY (full Ph3 results for tafasitamab in 1L DLBCL - acknowledging competitive dynamics, we see a potentially differentiated option for certain patients, e.g., GCB-subtype disease), SMMT (interim global Ph2 metastatic colorectal cancer data demonstrate durable efficacy at the selected Ph3 ivonescimab dose, including a landmark 9-month PFS rate of 76.1%, supporting the ongoing global Ph3 HARMONi-GI3 study), alongside presentations from Dizal and JNJ with readthrough to AVBP.

# Summit Therapeutics (SMMT, Buy, Salveen Richter)

Ivonescimab plus chemotherapy versus tislelizumab plus chemotherapy in previously untreated advanced squamous non-small cell lung cancer: overall survival results of the phase 3 harmoni-6 trial

SMMT's partner Akeso shared overall survival (OS) data from the single-region (China) Ph3 HARMONi-6 study of ivonescimab (ivo; a PD-1xVEGF) + chemotherapy vs. Tevimbra (ONC's anti-PD-1, similar to MRK's Keytruda) + chemotherapy in frontline squamous non-small cell lung cancer (NSCLC) during the plenary session (see our full takeaways from the presentation here). Recall, Akeso has previously shared progression-free survival results from the study (link), where the combination demonstrated a significant and clinically meaningful PFS benefit - 11.1 months vs. 6.9 months -with a hazard ratio (HR) of 0.60 (p<0.0001), in patients with squamous NSCLC. Per the late-breaking abstract presented today, ivo + chemotherapy demonstrated a statistically significant overall survival benefit of 27.9 months vs.

# Salveen Richter, CFA

+1(212)934-4204

salveen.richter@gs.com

GS & Co. LLC

# Corinne Johnson

+1(917)343-1445

corinne.johnson@gs.com

GS & Co. LLC

# Mark Aleynick, Ph.D.

+1(212)357-6820

mark.aleynick@gs.com

GS & Co. LLC

# Elizabeth Webster, Ph.D.

+1(212)357-9925

elizabeth.webster@gs.com

GS & Co. LLC

# Matt Dellatorre, Ph.D.

+1(212)855-0830

matt.dellatorre@gs.com

GS & Co. LLC

# Shrunatra Mishra

+1(332)245-7673

shrunatra.mishra@gs.com

GS India SPL

# Kevin Strang, Ph.D.

+1(212)357-7227

kevin.strang@gs.com

GS & Co. LLC

# Erik Wong

+1(212)357-9964 | erik.wong@gs.com

GS & Co. LLC

# Tommie Reerink, CFA

+1(212)357-2470

tommie.reerink@gs.com

GS & Co. LLC

# Lydia Erdman

+1(212)357-6383

lydia.erdman@gs.com

GS & Co. LLC

23.7 months for Tevimbra (anti-PD-1, similar to MRK's Keytruda) + chemotherapy, representing an 34% reduction in the risk of death (HR=0.66; 95% CI, 0.50 to 0.87; one-sided P =0.0017). Ivo + chemotherapy OS benefit was consistent across subgroups, where in PD-L1-negative patients (tumor proportion score (TPS) <1%), median OS was NE versus 18.6 months (HR, 0.64; 95% CI, 0.43 to 0.96), and in patients with PD-L1 TPS≥1%, median OS was NE versus 27.3 months (HR, 0.68; 95% CI, 0.46 to 0.99). On safety, ivo showed and manageable safety profile, which was consistent with prior Ph3 studies of ivonescimab plus chemotherapy. No additional safety signals were noted in the HARMONi-6 study in this current data cut compared to the previous data cut presented.

Overall, the data exceeds the HR<0.72 bar per our diligence and investor conversations, and are impressive in our view, noting this is the first time any regimen has demonstrated a statistically significant benefit over a PD-1 + chemotherapy (the global standard-of-care) in a Ph3 study in frontline NSCLC (see our full takeaways here). Today’s HARMONi-6 result further confirms the translation of ivo’s PFS benefit to OS, and provides positive readthrough to SMMT’s ongoing global Ph3 HARMONi-3 study of ivo + chemotherapy vs. Keytruda + chemotherapy in frontline NSCLC. SMMT will disclose final PFS and interim OS data from the HARMONi-3 study in 2H.

We additionally note a poster presentation from SMMT and Akeso with early Ph1/2 data for ivo in colorectal cancer, with readthrough to the ongoing global Ph3 HARMONi-GI3 study:

# Ivonescimab (ivo) with oxaliplatin + fluorouracil (5-FU) + leucovorin calcium (mFOLFOX6) for patients (pts) with unresectable metastatic colorectal cancer (mCRC): A phase 2 study.

The poster contained interim results evaluating ivo at 20 or 10mg/kg + mFOLFOX6 in frontline mCRC. As of the data cutoff (March 31, 2026), 49 patients were enrolled (ivo 20 mg/kg+ mFOLFOX6, n = 25; ivo 10 mg/kg + mFOLFOX6, n = 24), noting 53.1% had KRAS or BRAF tumor mutations, and 67.3% had liver metastases. Per the presenting KOL, the study included a majority of patients from Asia, and 9 patients from the US. Median duration of follow-up was 9.8 months and 9.9 months in the ivo 20 mg/kg + mFOLFOX6 and ivo 10 mg/kg + mFOLFOX6 arms, respectively. ORR was 70.8% in each treatment arm, and all were partial responses. DCR was 100% in each treatment arm, and median PFS was not reached. Treatment responses in the ivo 20 mg/kg + mFOLFOX6 arm were more durable than in the 10 mg/kg + mFOLFOX6 arm, with a duration of response (DoR) estimate at 9 months of 79.1% vs 41.5%, respectively. The landmark PFS rate at 9 months was 76.1% (95% CI, 51.7-89.4) and 70.1% (95% CI, 44.9-85.4) in the ivo 20 mg/kg + mFOLFOX6 and 10 mg/kg + mFOLFOX6 arms, respectively. Treatment related adverse events (TRAEs) occurred in 96% and 87.5% of patients in the ivo 20 mg/kg +mFOLFOX6 and ivo 10 mg/kg + mFOLFOX6 arms, respectively, with grade 3+ events reported in 44% and 33.3%, respectively, with no TRAEs leading to death. The presenting KOL was impressed by the responses, and noted that while a formal regional comparison was not performed, responses were consistent between patients from Asia and the US. The KOL acknowledged a modest increase in toxicity with the higher dose (noting 20mg/kg ivo + mFOLFOX6 is the selected Ph3 HARMONi-GI3 regimen), however highlighted increased efficacy and importantly, a longer DOR with the high dose. Overall, the KOL believes the data supports the ongoing global HARMONi-GI3 study in frontline mCRC.

We highlight notable interest in the Ph2 poster from KOLs during the poster session at ASCO. The data are encouraging in our view, and provide positive read through to SMMT's ongoing Ph3 HARMONi-GI3 study, which is investigating 20mg/kg ivo + mFOLFOX6 in frontline mCRC. Per the presenters, the slight increase in toxicity with the higher Ph3-selected dose, including VEGF-related toxicity, is manageable as the current standard-of-care in frontline mCRC is bevacizumab + chemotherapy, so physicians are accustomed to managing patients with these types of adverse events. Additionally, we note the data appear in-line or better vs. PFE's competing PD-1xVEGF molecule PF'4404, which demonstrated a confirmed ORR of 57.1% and a DCR of 95.2% (link) in a Ph2 study in 1L mCRC.

# Immunome (IMNM, Buy, Salveen Richter)

# RINGSIDE: A phase 3 randomized, placebo-controlled trial of varegacestat for treatment of progressing desmoid tumors

IMNM presented full results from the Ph3 RINGSIDE study of gamma-secretase inhibitor varegacestat in desmoid tumors. Recall, IMNM previously shared positive Ph3 topline data demonstrating a statistically significant progression-free survival (PFS; hazard ratio (HR) = 0.16; p<0.0001) benefit vs. placebo, objective response rate (ORR) of 56%, and tumor volume reduction of 83%, solidifying varegacestat's best-in-class position over Merck KGaA's Ogsiveo. The oral presentation at ASCO this weekend additionally included subgroup analyses and data on key secondary endpoints, including quality of life impacts, where we note all alpha-controlled secondary endpoints demonstrated statistically and clinically significant superiority for varegacestat vs. placebo. On the key endpoint of pain relief, varegacestat demonstrated a statistically significant difference of -2.42 vs. placebo per the Widespread Pain Index (WPI). The presenting KOL noted that while the study was not powered to detect statistical significance between subgroups, varegacestat did show PFS benefit across all subgroups examined, including patients with APC and CTNNBP1 mutations, those with larger tumors, and those who had previously received desmoid tumor therapy.

In the trial discussion portion of the session, the KOL leading the discussion aimed to compare varegacestat against Ogsiveo per the available data from the Ph3 RINGSIDE and Ph3 DeFi studies, noting deeper responses in patients who received varegacestat when comparing waterfall plots from the two studies, superiority on tumor volume reduction, and that varegacestat appeared to have a better and more rapid improvement in pain relief. On safety, the KOL highlighted varegacestat's superiority on ovarian toxicity (56% of patients with varegacestat, vs 76% for Ogsiveo), albeit noted overall similar levels of other AEs, and a greater number of dose reductions for varegacestat (80%, vs 42% for Ogsiveo in DeFi). The KOL leading the discussion also noted that both drugs appear to show efficacy in intra- and extra-abdominal disease. One remaining question per the KOL is how to define what is the optimal treatment duration balanced against efficacy and toxicity for the GSI class - the KOL highlighted recent 3-year data for Ogsiveo, noting that only 3 additional responses were observed with long-term use, thus in the KOL's view the benefit of continuous treatment remains unclear.

Overall, the data further demonstrates varegacestat's best-in-class profile in our view, where we note Varegacestat demonstrated 94.2%/88.9% 1-year/2-year PFS rates, vs. 85%/76% for Ogsiveo in the Ph3 DeFi study, alongside benefits on key patient outcome metrics including pain, per the KOLs. While the presenting KOL noted the lack of a head-to-head study, and

potential similarity given both Ogsiveo and varegacestat are in the GSI class, the KOL did highlight varegacestat's once-daily dosing as differentiating. The KOL leading the discussion portion of the session additionally highlighted varegacestat's superiority, cautioning cross-trial comparisons. We believe varegacestat is differentiated per the efficacy data, once-daily dosing vs. twice-daily for Ogsiveo in the context of physician/patient preference for the easier regimen, and on ovarian toxicity, observed in \~55.6% of premenopausal women vs. \~75% for Ogsiveo. An NDA for varegacestat was submitted in 2Q, and IMNM plans to submit a Marketing Authorization Application to the European Medicines Agency for varegacestat by YE26. Given the profile, we anticipate a stronger launch relative to Ogsiveo and model for global peak sales of \$1.6bn in 2037.

# Gilead (GILD, Neutral, Salveen Richter)

# NAPISTAR 1-01: Results of phase 1 dose escalation of monotherapy with TUB-040, a novel NaPi2b-targeting exatecan ADC, in patients (pts) with platinum-resistant ovarian cancer (PROC)

At the ongoing ASCO meeting, updated data from the Phase I/IIa NAPISTAR 1-01 trial (NCT06303505) for TUB-040 in platinum-resistant ovarian cancer (PROC) were presented. TUB-040 is a novel antibody-drug conjugate (ADC) targeting the sodium-dependent phosphate transporter NaPi2b, utilizing a topoisomerase I inhibitor (exatecan) payload with a drug-to-antibody ratio (DAR) of 8.

Background. Recall NaPi2b is overexpressed in high-grade serous ovarian cancer and non-small cell lung cancer (NSCLC). TUB-040 is a DAR8 ADC targeting NaPi2b, comprising a humanized Fc-silenced IgG1 mAb conjugated to exatecan via a cleavable, cysteine-selective, stable, solubility-mediating P5 linker providing excellent stability and biophysical ADC properties. In preclinical studies, TUB-040 induces potent antigen-specific cytotoxicity and demonstrates strong bystander activity.

NAPISTAR 1-01 is a phase 1/2a study in biomarker-unselected pts with PROC and NSCLC. TUB-040 was administered Q3W in dose escalation (range 0.5-5.3 mg/kg) to pts with PROC until progression or unacceptable toxicity. As of Dec 1, 2025, 67 PROC pts received TUB-040 for a median of 10 cycles (1-25), median duration of exposure was 213 days (21-546), and 42 (63%) pts were ongoing. Median age: 62 years (34-81), ECOG PS 0-1, median prior lines: 4 (1-7), prior treatment included bevacizumab (84%), PARPi (76%), and mirvetuximab soravtansine (13%).

Efficacy. The efficacy analysis focused on 46 patients treated at dose levels between 1.67 and 3.3 mg/kg. This population was heavily pre-treated, with a median of 4 prior lines of therapy, including bevacizumab (84%) and PARP inhibitors (76%).

Confirmed Overall Response Rate (cORR): 61% (including two confirmed complete responses).   
■ Unconfirmed ORR (uORR): 67%.   
■ Disease Control Rate (DCR): 96%.   
Median Progression-Free Survival (mPFS): 11 months across the broader 67-patient population (doses 0.5–5.3 mg/kg). This significantly outperforms the historical standard of care mPFS of approximately 5 months in PROC.   
■ CA-125 Response: 81% of evaluable patients (34/42) showed a biochemical

response.

Durability: 79% of responders maintained their response for over 6 months, and 57% for over 12 months. Median duration of response (mDOR) has not yet been reached.

Safety. The safety profile of TUB-040 appears differentiated from other ADCs in the NaPi2b and topoisomerase inhibitor classes, particularly regarding off-target toxicities.

■ Common Adverse Events: The most frequent treatment-emergent adverse events (TEAEs) were nausea (78%), fatigue (54%), and neutropenia (43.5%).   
■ Hematological Toxicity: Grade 3 or higher neutropenia occurred in 26% of patients at the 1.67–3.3 mg/kg dose levels. Anemia (13%) and thrombocytopenia (4%) of Grade 3+ were also reported.   
Differentiated Profile: Notably, there were no clinically relevant cases of interstitial lung disease (ILD)/pneumonitis (only 6.5% Grade 1, all resolved), ocular toxicity, or peripheral neuropathy. This lack of “class-effect” toxicities suggests a wider therapeutic window and potential for combination therapies.

Overall, we view the data as encouraging and broadly in-line with the previous update at ESMO (note the MTD was previously determined to be 4.4mg/kg), and see the drug as one of the leading emerging therapies in ovarian cancer. Physician feedback at the conference was highly positive. Dose optimization is currently ongoing. GILD has noted the potential for a registrational study initiation in FY27.

ASCENT-04: Analysis of efficacy by biomarker subgroups with sacituzumab govitecan (SG) + pembrolizumab (pembro) vs chemotherapy (chemo) + pembro in participants (pts) with previously untreated PD-L1+ metastatic triple-negative breast cancer (mTNBC)

ASCENT-03: Efficacy by biomarker subgroup with sacituzumab govitecan (SG) vs chemotherapy (chemo) in participants (pts) with previously untreated advanced triple-negative breast cancer (TNBC) who are not candidates for PD-(L)1 inhibitors (PD-[L]1i)

Pivotal data for Trodelvy (sacituzumab govitecan) in the first-line (1L) metastatic triple-negative breast cancer (mTNBC) setting were highlighted, primarily through updated subgroup and exploratory analyses from the Phase 3 ASCENT-03 and ASCENT-04 trials. Recall these presentations follow prior publication of the results in the NEJM.

# ASCENT-04: Trodelvy + Keytruda (PD-L1 positive)

The ASCENT-04 trial (KEYNOTE-D19) evaluated Trodelvy in combination with pembrolizumab versus standard-of-care (SOC) chemotherapy plus pembrolizumab in previously untreated patients with PD-L1-positive (CPS ≥ 10) mTNBC.

■ Primary Efficacy: The combination demonstrated a statistically significant improvement in progression-free survival (PFS).

☐ Median PFS: 11.2 months vs. 7.8 months for the control arm (HR: 0.65; p < 0.001).

☐ Risk Reduction: A 35% reduction in the risk of disease progression or death.

■ ASCO subgroup highlights: Data presented at the 2026 meeting demonstrated that the PFS benefit was observed across all Trop-2 expression quartiles (Q1–Q4), albeit stronger in high-expressors:

☐ High Trop-2 (Q4): Median PFS reached 16.6 months vs. 9.2 months (HR: 0.57).   
☐ Low Trop-2 (Q1): Median PFS was 9.3 months vs. 9.0 months (HR: 0.81), indicating benefit even in low-expressing tumors.

Safety: The safety profile was manageable and consistent with the known profiles of both agents, with Grade $\geq$ 3 neutropenia occurring in 43% of patients.

# ASCENT-03: Trodelvy Monotherapy (PD-L1 negative/IO ineligible)

The ASCENT-03 trial focused on 1L mTNBC patients who were not candidates for PD-(L)1 inhibitors (primarily PD-L1 negative or those who progressed after prior immunotherapy in the curative setting).

Primary Efficacy: Trodelvy monotherapy significantly outperformed physician's choice of chemotherapy.

☐ Median PFS: 9.7 months vs. 6.9 months (HR: 0.62; p < 0.0001).   
☐ Duration of Response (DOR): 12.2 months for Trodelvy vs. 7.2 months for chemotherapy.

■ ASCO 2026 Subgroup Highlights: Benefit was maintained across key biomarkers, including tumor BRCA (tBRCA) status and HER2-low status.

□ tBRCA Wild-type: HR 0.70.   
□ HER2-Low: HR 0.74.   
☐ Trop-2 Quartiles: Benefit was observed across all quartiles, with HRs ranging from 0.54 to 0.84.

Overall, we view the updates as incremental (given the prior publication of results). Recall the NCCN guidelines were updated earlier this year to reflect the data (both Trodelvy mono and Trodelvy + Keytruda are now Category 1 options in IO ineligible PD-L1 positive 1L TNBC patients, respectively). Recall Trodelvy is already the SoC in 2L TNBC. We are monitoring c

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal.

It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
