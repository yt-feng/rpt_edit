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
# Biopharma | North America

# Front-line lung cancer takeaways from ASCO

ASCO conference featured a number of presentations of Ph2/3 data emerging in front-line NSCLC, which is currently dominated by MRK's Keytruda+/-chemo. We were most focused on MRK/Kelun's Sac-TMT (TROP2 ADC) and Akeso/SMMT's Ivo (PD1xVEGF bispec). See below and within for our takeaways.

At ASCO (see preview HERE) we were focused on MRK/Kelun's sacituzumab tirumotecan (sac-TMT; ADC to TROP2), and the PD(L)1xVEGF bispecifics - Akeso/SMMT's ivonescimab, BMY/BNTX's pumitamig, and PFE's PF'4404. These two modalities have emerged as some of the leading strategies to attempt to improve upon or replace Keytruda (PD1 antibody, which goes off patent in 2028). MRK is uniquely positioned in that it has a drug in each category (including LM-299, a PD-1xVEGF bispecific antibody from LaNova).

MRK (EW): We view the Sac-TMT OpiTROP-Lung05 Ph3 data (PD-L1 positive patients) as an incremental positive update for the drug, but generally consistent with the data released in the abstract (see HERE), and we see Ph3 data later this year from the OpiTROP-Lung06 China trial (vs. Keytruda+chemo in NSQ PD-L1 negative population) as another key input into the drug's profile. We also await further details in terms of MRK's strategy to address PD-L1 low population. For MRK we model sac-TMT 2035 risk-adjusted sales of \$4.1bn (at a 55% POS) across tumor types vs. VA cons' of \$5.4bn. Additional lateral data on TROP2's in 1L NSCLC will come from AstraZeneca and GILD (see Exhibit 1 below).

PD(L)1xVEGF bispecifics: The data sets at ASCO from Akeso/SMMT, BNTX/BMY, and PFE demonstrate that PD(L)1xVEGF bispecifics can elicit meaningful response across all PD-L1 levels, including TPS<1%. In addition, we note there were two firsts from this drug class at the conference: (1) first demonstration of a stat sig survival benefit (SMMT/Akeso's HARMONi-6), and (2) the first global data in 1L NSCLC (BMY/BNTX's ROSETTA-Lung02 Ph2 trial). However, a number of questions are still outstanding in our view and we await more definitive survival data from global trials vs. Keytruda+chemo. We continue to see BNTX (OW) as the best way to gain exposure to this class in our coverage.

Importantly, the Ivo+chemo HARMONI-6 (squamous all comers) OS data represents the first validation of translatibility of PFS to OS for the class, but there are a number of caveats noted by the discussant and in the Lancet publication. The discussant stated that while the results were provocative, there are several outstanding questions, including the shorter follow-up, benefit by age, and whether these results can be reproduced in a global study (i.e., HARMONi-3) vs. Keytruda +chemo. Hence, in our opinion OS data from the ongoing Ivo+chemo HARMONi-3 (all comers) Ph3 trial in 2H26 are more important for the outlook of PD(L)-

MS & CO. LLC

Terence C Flynn, Ph.D.

Equity Analyst

Terence.Flynn@morganstanley.com +1 212 761-2230

Chris Yu, J.D., Ph.D.

Equity Analyst

Chris.L.Yu@morganstanley.com +1 212 761-2535

Hailey Horowitz

Research Associate

Hailey.Horowitz@morganstanley.com +1 212 761-5264

Alexander Yevdokimov, Ph.D.

Research Associate

Alexander.Yevdokimov@morganstanley.com +1 212 761-2167

Connor M Massari

Equity Analyst

Connor.Massari@morganstanley.com +1 212 761-2417

Damien H Kerner

Research Associate

Damien.H.Kerner@morganstanley.com +1 212 761-3829

MS INDIA COMPANY PRIVATE LIMITED+

Saket Agarwal

Research Associate

Saket.Agarwal@morganstanley.com +91 22 6995-4012

2026 EXTEL

ALL-AMERICA RESEARCH POLL

May 26 – June, 12 2026

VIEW OUR ANALYSTS >

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

1xVEGF class given the global nature of the trial, coupled with a comparison to the Keytruda+chemo control arm. Recall this is also consistent with feedback from our Therapeutics Doctor Days earlier this year (see HERE). See HARMONI-6 takeaways from our China healthcare team HERE.

In our view the incremental Ph2 data at ASCO suggest that BMY (UW)/BNTX (OW) Pumi and PFE's (EW) PF'4404 are competitive with SMMT/Akeso's Ivo in NSCLC, and they achieve high ORR's across both squamous (SQ) and non-squamous (NSQ) histologies and all PD-L1 levels. See Exhibit 6, Exhibit 7, and Exhibit 8 for cross-trial efficacy comparison, with the typical caveats for such comparisons. For Pumi, we project 2035 risk-adjusted WW sales (before profit split) of \$5.6bn, with POS ranging from 50-70% across different tumors. For PF'4404, we project 2035 risk-adjusted WW sales of \$2.7bn (50% POS).

Exhibit 1: Overview of select 1L metastatic NSCLC trials   
![](images/facd4b0cf863af1b3028240ecd0648943c31931df745b83ae891ee4d0bf997f9.jpg)

<details>
<summary>other</summary>

Histology
| PD-L1 Status | PD-L1+50% (PD-L1-High) | ARTEMIDE-Lung02 (AZN) + nlivegostomig+chemo vs. Key+chemo PCD Feb. 29 | ARTEMIDE-Lung02 (AZN) + nlivegostomig+chemo vs. Key+chemo PCD Feb. 29 | ARTEMIDE-Lung02 (AZN) + nlivegostomig+chemo vs. Key+chemo PCD Feb. 29 | ARTEMIDE-Lung02 (AZN) + nlivegostomig+chemo vs. Key+chemo PCPD Feb. 29 | ARTEMIDE-Lung02 (AZN) + nlivegostomig+chemo vs. Key+chemo PCD Feb. 29 | ARTEMIDE-Lung02 (AZN) + nlivegostomig+chemo vs. Key+chemo PCD Feb. 29 | ARTEMIDE-Lung02 (AZN) + nlivegostomig+chemo vs. Kep+chemo PCD Feb. 29 | ARTEMIDE-Lung02 (AZN) + nlivegostomig+chemo vs. Key+chemo PCD Feb. 29 | ARTEMIDE-Lung02 (AZN) + nlivegostomig+chemo vs. Key+chemo PCD Feb. 29 | ARTEMIDE-Lung02 (AZN) + nlivegostomig-chemo vs. Key+chemo PCD Feb. 29 | ARTEMIDE-Lung02 (AZN) + nlivegostomig-chemo vs. Key+chemo PCD Feb. 29 | ARTEMIDE-Lung02 (AZN) + nlivegostomig-chemo vs. Key+chemo PCD Feb. 29 | ARTEMIDE-Lung02 (AZN) + nivegostomig-chemo vs. Key+chemo PCD Feb. 29 | ARTEMIDE-Lung02 (AZN) + nivegostomig-chemo vs. Key+chemo PCD Feb. 29 | ARTEMIDE-Lung02 (AZN) + nivegostomig-chemo vs. Key+chemo PCD Feb. 29 | ARTEMIDE-Lung02 ( AZN / Daichi) + Nivegostomig-chemo vs. Key+chemo PCD Feb. 29 | ARTEMIDE-Lung02 ( AZN / Daichi) + Nivegostomig-chemo vs. Key+chemo PCD Feb. 29 | ARTEMIDE-Lung02 ( AZN / Daichi) + Nivegostomig-chemo vs. Key+chemo PCD Feb. 29 | ARTEMIDE-Lung02 ( AZN) + nivegostomig-chemo vs. Key+chemo PCD Feb. 29 | ARTEMIDE-Lung02 ( AZN) + nivegostomig-chemo vs. Key+chemo PCD Feb. 29 | ARTEMIDE-Lung02 ( AZN) + nivegostomig-chemo vs. Key+chemo PCD Feb. 29 | ARTEMIDE-Lung02 ( AZN) + nivegostomig-chemo vs. Key+chemo PCD Feb.<fcel>KEYNOTE-467 (MRK) & Key+chemo vs. Chemo HARMONi-6 (SMMT/Akeso) & Ivo+chemo vs. Televimbra+chemo Positive PFS data 10/19/25 OS data at ASCO '26 KEYNOTE-467 (MRK) & Key+chemo vs. Chemo HARMONi-6 (SMMT/Akeso) & Ivo+chemo vs. Televimbra+chemo Positive PFS data 10/19/25 OS data at ASCO '26 CheckMate ISLA (BMY) & Opdive-Yenvoy+chemo vs. Chemo KEYNOTE-624 (MRK) & Key+commo HARMONi-7 (SMMT/Akeso) & Ivo+ key PCD of Apr. 28 TROPION-Lung08 (AZN/Daichi) + Data=Key vs. Key Data expected -2H26 KEYNOTE-642 (MRK) & Key+commo HARMONi-7 (SMMT/Akeso) + Ivo+ key PCD of Apr. 28 TROPION-Lung08 (AZN/Daichi) + Data=Key vs. Key Data expected -2H26 KEYNOTE-642 (MRK) & Key+commo HARMONi-7 (SMMT/Akeso) + Ivo+ key PCD of Apr. 28 TROPION-Lung08 (AZN/Daichi) + Data=Key v. Key Data expected -2H26 KEYNOTE-642 (MRK) & Key+commo HARMONi-7 (SMMT/Akeso) + Ivo+ key PCD of Apr. 28 TROPION-Lung08 (AZN/Daichi) + Data=Key v. Key Data expected -2H26 KEYNOTE-642 (MRK) & Key+commo HARMONi-7(SMMT/Akeso) & Ivo+ key PCD of Apr. 28 TROPION-Lung08 (AZN/Daichi) + Data=Key v. Key Data expected -2H26 KEYNOTE-642 (MRK) & Key+commo HARMONi-7(SMMT/Akeso) & Ivo+ key PCD of Apr. 28 TROPION-Lung08 (AZN/Daichi) + Data=Keyv. Key Data expected -2H26 KEYNOTE-642 (MRK) & Key+commo HARMONi-7(SMMT/Akeso) & Ivo+ key PCD of Apr. 28 TROPION-Lung08 (AZN/Daichi) + Data=Key v. Key Data expected -2H26 KEYNOTE-642 (MRK) & Key+commo HARMONi-7(SMMT/Akeso) & Ivo+ key PCD of Apr. 28 TROPION-Lung08 (AZN/Daichi) + Data=Key v. Key Data expected -2H26 KEYNOTE-642 (MRK) & Key+commo HARMONi-7(SMMT/Akeso) & Ivo+ key PCD of Apr. 28 TROPION-Lung08 (AZN/Dauchi) + Data=Key v. Key Data expected -2H26 KEYNOTE-642 (MRK) & Key+commo HARMONi-7(SMMT/Akeso) & Ivo+ key PCD of Apr. 28 TROPION-Lung08 (AZN/Daichi) + Data=Key v. Key Data expected -2H26 KEYNOTE-642 (MRK) & Key+commo: Interim data at ESMO 26 or later<nl>
</details>

Source: Company data, CT.gov, MS

How to vote: To request a ballot, please go to https://www.extelinsights.com/voting.

![](images/e66ba96b1f473a4b8b487fa0153616da12afef96fd709bfe03146af77f64dfbd.jpg)

<details>
<summary>text_image</summary>

2026 EXTEL
ALL-AMERICA
RESEARCH POLL
May 26 – June 12, 2026
We appreciate your support
VOTE HERE
★★★★★
</details>

Akeso is covered by Jack Lin; AstraZeneca is covered by Sarita Kapila; BeOne is covered by Sean Laaman; Daiichi Sankyo is covered by Shinichiro Muraoka; Kelun is covered by Alexis Yan; SMMT is not covered.

# MRK/Kelun's Sac-TMT (TROP2 ADC)

# China-only Ph3 sac-TMT+Keytruda vs. Keytruda data in 1L PD-L1 positive NSCLC (OptiTROP-Lung05)

MRK's partner Kelun presented Ph3 China-only data from the OptiTROP-Lung05 trial of sac-TMT+Keytruda vs. Keytruda in 1L PD-L1-positive NSCLC; see our initial take on the abstract HERE. At median follow-up of 10.5mos, median PFS was not reached for sac-TMT vs. 5.7mos for Keytruda (p<0.0001). PFS data to date imply a mPFS for sac-TMT +Keytruda of \~15-17mos, which is generally in line with investor expectations of \~15-20mos; see Exhibit 2, and our prior estimate of \~16mos+ based on the HR. The PFS performance of the Keytruda control arm also appears in line with expectations (see Exhibit 10). The data for OS were not mature, and a favorable trend was observed in the sac-TMT+Key group (HR, 0.55; 95% CI, 0.36-0.85). The BICR-assessed ORR was 70.2% in the sac-TMT + Key group versus 42.0% in the Key group. In the pre-specified PD-L1 subgroups, the HRs for PFS in pts with TPS 1-49% and TPS ≥ 50% were 0.28 (95% CI, 0.19-0.41) and 0.47 (95% CI, 0.29-0.77). In the pre-specified histology subgroups, the HRs for PFS in pts with non-squamous and squamous were 0.28 (95% CI, 0.18-0.43) and 0.44 (95% CI, 0.29-0.66). The Lancet publication noted that the observed benefit of sac-TMT +Keytruda in patients with non-squamous NSCLC is consistent with findings from other studies of TROP2 ADCs, citing the global Ph3 TROPION-Lung01 trial of Datroway vs. chemo in 2L+ NSCLC.

Exhibit 2: Model predictions for PFS in sac-TMT+Key arm 

<table><tr><td colspan="6">Table S1. Parametric model predictions for progression-free survival in the sac-TMT plus pembrolizumab group</td></tr><tr><td rowspan="2">Parametric Model</td><td colspan="3">Predicted progression-free survival in the Sac-TMT + Pembrolizumab group, median (95% CI)</td><td rowspan="2">Difference*, month</td><td rowspan="2">AIC</td></tr><tr><td>Overall</td><td>PD-L1 TPS of 1 to 49%</td><td>PD-L1 TPS of 50% or greater</td></tr><tr><td>Lognormal</td><td>16.7 (12.8-22.1)</td><td>15.7 (11.2-21.8)</td><td>18.4 (11.6-29.9)</td><td>11.0</td><td>552.0</td></tr><tr><td>LogLogistic</td><td>15.7 (12.4-20.0)</td><td>14.8 (11.1-20.2)</td><td>17.3 (11.3-27.2)</td><td>10.0</td><td>555.2</td></tr><tr><td>Exponential</td><td>17.5 (13.8-22.4)</td><td>16.9 (12.3-22.8)</td><td>18.5 (12.7-26.5)</td><td>11.8</td><td>560.4</td></tr><tr><td>Gamma</td><td>15.0 (12.0-18.3)</td><td>14.2 (10.9-18.4)</td><td>16.4 (11.2-22.7)</td><td>9.3</td><td>556.0</td></tr><tr><td>Weibull</td><td>15.0 (12.2-18.4)</td><td>14.1 (10.9-18.1)</td><td>16.5 (11.4-23.8)</td><td>9.3</td><td>556.9</td></tr></table>

\* The difference in median progression-free survival between the sac-TMT plus pembrolizumab group and the pembrolizumab group was based on the predicted median value for the sac-TMT plus pembrolizumab group minus the observed median value for the pembrolizumab group in the intent-to-treat population. The observed median progression-free survival for the pembrolizumab group was 5.7 months (95% CI, 4.3–7.0). Smaller AIC indicating better fitting. Sac-TMT=sacituzumab tirumotecan; AIC=Akaike Information Criterion; PD-L1=programmed death ligand 1; TPS=tumor proportion score; CI=confidence interval.   
Source: Xiong et al, Lancet 2026

Per the publication, the safety profile of sac-TMT+Key was consistent with the known safety profiles of the individual agents, with no new safety signals identified. The increased toxicity with the combo was primarily driven by expected sac-TMT-related heme tox and stomatitis vs. Keytruda monotherapy. This heme tox was generally manageable with supportive care, dose modification, or temporary treatment interruption, while permanent discontinuation rates were low (TEAEs led to discontinuation of sac-TMT/Keytruda in 3.8%/5.3% of pts in the sac-TMT+Keytruda group while discontinuation of Keytruda occurred in 4.9% of pts in the Keytruda mono group). Per the authors, taken together with the observed delay in deterioration of global health status, these findings suggest that the clinical benefit of the combination was not offset by unacceptable toxicity. Gr3+ TEAEs were 55.3% in the sac-TMT+Keytruda group and 31.4% in the Keytruda group. Most common Gr3+ TEAEs of special interest for sac-TMT were neutrophil count decreased (17.3%), anemia (9.1%), and stomatitis (5.3%).

MRK has previously commented that sac-TMT is differentiated from other TROP2 ADCs by its novel bifunctional linker design, which aims to balance stability with payload release, with the goal of potentially mitigating the hematologic toxicity observed with GILD's Trodelvy's looser linker, while avoiding the interstitial lung disease (ILD) risk associated with tighter linker systems such as AZN/Daiichi's Datroway. See Exhibit 11.

In our view, the more definitive sac-TMT data will come from global Ph3 trials. MRK/Kelun are pursuing a broad registrational development program for sac-TMT across NSCLC, breast cancer, gynecologic cancers (incl. endometrial, cervical, and ovarian), as well as urothelial cancer and gastroesophageal adenocarcinoma; see Exhibit 12 for a summary. Recall, MRK recently announced positive interim PFS/OS results for the TroFuse-005 trial in 2L+ endometrial cancer; LINK. We view the breadth of the program as a differentiator for sac-TMT, as successful execution across multiple tumor types could drive a meaningfully larger TAM and peak sales opportunity relative to competitors.

For MRK we model sac-TMT 2035 risk-adjusted sales of \$4.1bn (at a 55% POS) vs. MRK VA cons' of \$5.4bn. We'd note that the FDA granted MRK a Commissioner's National Priority Voucher for sac-TMT, which could enable a faster review once filed in the US.

# SMMT/Akeso's Ivonescimab (PD-1xVEGF)

# China-only Ph3 Ivo+chemo vs. Tevimbra+chemo data in 1L SQ NSCLC (HARMONi-6)

Background: SMMT/Akeso presented full PFS and OS data from the HARMONi-6 trial of Ivonescimab (Ivo)+chemo vs. Tevimbra (BeOne's PD-1)+chemo in 1L SQ NSCLC. We'd note that PFS data from the trial had previously been reported at ESMO in October '25 (11.1mos for Ivo+chemo vs. 6.9mos for Tevimbra+chemo, HR=0.6 p<0.0001; LINK), and thus the focus here was on OS. However, the trial uses Tevimbra+chemo rather than Keytruda +chemo as a comparator and hence investors are likely to somewhat discount the results in our view. We'd also caveat that these data are from a China-only population and will need to be replicated on a global basis. SMMT/Akeso are running a Ph3 global study in 1L NSCLC (HARMONi-3) against Keytruda +chemo, and final PFS and interim OS are expected in 2H26. Recall the Independent Data Monitoring Committee recently conducted an interim PFS analysis and recommended the study continue as planned.

At a high level in HARMONi-6, Ivo + chemo achieved a stat sig and meaningful OS benefit, which is the first evidence that the PFS benefits previously seen with the PD(L)1xVEGF class might translate into an OS benefit. However, based on the discussant's comments, we believe there are still a number of outstanding questions, including the short follow-up and whether these results can be reproduced in a global study (HARMONi-3 study) against Keytruda + chemo.

Key takeaways from HARMONi-6 presentation. At data cutoff (Feb 27, 2026) for the interim overall survival analysis, the median duration of follow-up was 21.4 months. See Exhibit 7 for 1L SQ NSCLC cross-trial efficacy comparison, and Exhibit 9 for 1L SQ NSCLC cross-trial safety comparison, with the typical caveats of such comparisons.

- In the ITT population, Ivo + chemo resulted in an mOS of 27.9 months vs. 23.7 months for Tevi + chemo, with a HR of 0.66 (Exhibit 3). For reference, the historical mOS for Tevi + chemo in this indication was 22.8 months in Ph3 RATIONALE-307 (LINK). We note as for Keytruda + chemo, the mOS was 15.9 months (KN-407) and 30.1 months (KN-407 China).   
- The presenter noted that the mOS in the lvo arm would have not been reached without the last single event.   
- The overall survival benefit was consistent across all key subgroups

• PD-L1 TPS l<1%, the HR was 0.64   
- TPS ≥1%, the HR was 0.68   
- TPS 1-49%, the HR was 0.67   
- TPS ≥50%, the HR was 0.64

\- Earlier this year we spoke with a couple lung KOLs, and they had varying degrees of excitement about the PD(L)1xVEGF bispecific drug class. Specifically on HARMONi-3 (global), they want to see an HR for OS of 0.7 to 0.75, which in their view would be transformational (LINK).

\- Ivo + chemo showed a manageable safety profile, with 69% Gr≥3 TRAEs vs. 59% for the control arm. Discontinuation rate was 4% vs. 4% for the control arm (Exhibit 5). VEGF-related AEs occurred more frequently in the Ivo arm, most of which were Gr1-2. See hemorrhage rate in Exhibit 9.

The independent discussant stated that while the results were provocative, there are some outstanding questions. Specifically, she provided 3 high-level takeaways: (1) Ivo + chemo is effective in Chinese patients, based on the interim OS data. (2) Ivo resulted in VEGF-related AEs, and there is uncer

[中间内容因长度限制已省略]

ational Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., authorised and regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

© 2026 MS
"""
