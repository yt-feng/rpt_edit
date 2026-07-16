你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
# Hansoh Pharma (3692.HK): Continued BD execution; Out-licensed oral IL-23 through a NewCo-and-Merger structure

Licensing-out an oral IL-23 to NewCo Avere, with planned Nasdaq listing through merger: Hansoh announced an exclusive ex-Greater China licensing agreement with Avere Therapeutics for HS-20118 (AVR-001), a once-weekly oral IL-23 receptor antagonist, for US\$120mn upfront, up to US\$2.18bn in development and commercial milestones, and mid-single to low-double digit royalties on future sales outside Greater China. The transaction is centered around Avere, a NewCo established in 2025 by Hansoh together with a group of financial investors. In parallel with the licensing transaction, Avere completed a US\$320mn private financing led by Fairmount and Hansoh, with participation from a broad syndicate of crossover and specialist biotech investors, and subsequently entered into an agreement to merge with Nasdaq-listed NextCure in an all-stock transaction. Unlike many recent China biotech NewCo transactions that utilize cash shells, NextCure is an operating biotech with its own oncology pipeline, including CDH6 and B7-H4 ADC programs. Upon completion of the merger, Hansoh is expected to hold a 30-40% equity stake in the combined company, enabling the company to retain meaningful exposure to future value creation for HS-20118. Given Hansoh's expected ownership position, we would expect potential regulatory review considerations, such as CFIUS, although the scope, timing and outcome of any such review remain unclear. We view the transaction as another demonstration of Hansoh's continued BD execution. Management has previously communicated its target of 1-2 BD deals annually, and the company has delivered on this objective since 2023.

Oral IL-23 remains an attractive but competitive opportunity: According to the company announcement, HS-20118 demonstrated PASI and PASI75 responses broadly comparable to a first-generation once-daily oral IL-23 inhibitor (we believe to be J&J's icotrokinra) while offering once-weekly dosing supported by an approximately 100-hour half-life. While oral IL-23 remains an attractive concept given the convenience advantage versus injectable biologics, available Phase 3 psoriasis data suggest efficacy may still lag leading IL-23 and IL-17 biologics based on cross-trial comparisons. Icotrokinra reported PASI90 rates of 50% at Week 16, compared with roughly 70-80% historically reported by injectable IL-23 and IL-17 biologics in pivotal studies (see Exhibit 1). As such, we believe the commercial opportunity for oral IL-23 therapies will ultimately depend on whether they can offer a sufficiently attractive balance between efficacy, safety, convenience and pricing, rather than convenience alone. For HS-20118 specifically, the once-weekly dosing profile and long half-life may provide differentiation within the oral IL-23 category, but further clinical data will be required to establish its competitive positioning.

Ziyi Chen
+852-2978-0526 | ziyi.chen@gs.com
GS (Asia) L.L.C.

Honglin Yan
+852-2978-6666 | honglin.yan@gs.com
GS (Asia) L.L.C.

Eddie Song
+852-2978-6426 | eddie.song@gs.com
GS (Asia) L.L.C.

Exhibit 1: Comparison of clinical data of IL-23 / IL-17 targeted drugs

<table><tr><td>Drug</td><td>Icotrokinra</td><td>Secukinumab</td><td>HS-20137</td><td>Guselkumab</td><td>Mirikizumab</td><td>Ixekizumab</td></tr><tr><td>Target</td><td>Oral IL-23</td><td>IL-17A mAb</td><td>IL-23 mAb</td><td>IL-23 mAb</td><td>IL-23 mAb</td><td>IL-17A mAb</td></tr><tr><td>Company</td><td>JNJ</td><td>Novartis</td><td>Hansoh / Qyuns</td><td>JNJ</td><td>Eli Lilly</td><td>Eli Lilly</td></tr><tr><td colspan="7">Clinical trial</td></tr><tr><td>Trials</td><td>NCT06095115</td><td>NCT02826603</td><td>ChiCTR2300075645</td><td>NCT03090100</td><td>NCT03482011</td><td>NCT01474512</td></tr><tr><td>Phase</td><td>Phase III</td><td>Phase III</td><td>Phase II</td><td>Phase III</td><td>Phase III</td><td>Phase III</td></tr><tr><td>Sample size</td><td>684</td><td>1,102</td><td>159</td><td>1,048</td><td>530</td><td>1,296</td></tr><tr><td>Control</td><td>Placebo</td><td rowspan="2">secukinumab 300 mg (n = 550) or ustekinumab 45/90 mg (n = 552)</td><td>Placebo</td><td>secukinumab</td><td>Placebo</td><td>Placebo</td></tr><tr><td>Dose</td><td>oral, QD</td><td>100/200mg Q8W, 200mg Q12W</td><td>guselkumab 100 mg Q8W vs secukinumab</td><td>250mg s.c. Q4W</td><td>80mg Q2W or Q4W s.c</td></tr><tr><td colspan="7">Patient baseline</td></tr><tr><td>Median age (year)</td><td>42.6</td><td>45.4</td><td>41-46</td><td>45.8</td><td>45.7-46.4</td><td>45 - 46</td></tr><tr><td>Race</td><td>White (72%), Asian (24%)</td><td>White (75.3%)</td><td>Chinese</td><td>White (93%), Asian (3%)</td><td></td><td>White (91.9%-93%)</td></tr><tr><td>Psoriasis duration (mean, year)</td><td>17.1</td><td></td><td></td><td>18.4</td><td>17.0 - 17.7</td><td>19 - 20</td></tr><tr><td>PASI score mean</td><td>20</td><td></td><td>24-29</td><td>20</td><td>22.3 - 23.5</td><td>20 - 21</td></tr><tr><td>Bioexperienced</td><td>34%</td><td>-</td><td>-</td><td>29%</td><td></td><td></td></tr><tr><td colspan="7">Efficacy data</td></tr><tr><td>Assessment time</td><td>Week 16</td><td>Week 12 / 16</td><td>Week 16</td><td>Week 12/48</td><td>Week 16</td><td>Week 12</td></tr><tr><td colspan="7">PASI response</td></tr><tr><td>- PASI75 (%)</td><td>69% vs 11%</td><td>88.0% (week 12); 91.7% (week 16)</td><td>92.3% (200mg Q8W)</td><td>89% vs 92% (week 12)</td><td>82.5% vs 9.3%</td><td>89.1% vs 3.9% (Q2W)</td></tr><tr><td>- PASI90 (%)</td><td>50% vs 4%</td><td>76.6% (week 16)</td><td>76.9% (200mg Q8W) vs 7.5% (pbo)</td><td>69% vs 76% (week 12)</td><td>64.3% vs 6.5%</td><td>70.9% vs 0.5% (Q2W)</td></tr><tr><td>- PASI100 (%)</td><td>27% vs &lt;1%</td><td>38.1% (week 12); 45.3% (week 16)</td><td>40% (200mg Q12W)</td><td>58% vs 48% (week 48)</td><td>32.4% vs 0.9%</td><td>35.3% vs 0% (Q2W)</td></tr><tr><td colspan="7">PGA response</td></tr><tr><td>- Minimal or cleared (%)</td><td>65% vs 8%</td><td></td><td></td><td></td><td>69.3% vs 6.5%</td><td>81.8% vs 3.2% (Q2W)</td></tr><tr><td>- ss-PGA0/1 (scalp)</td><td>72% vs 15%</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="7">Safety data</td></tr><tr><td>AEs</td><td>49% vs 49%</td><td>47.5%</td><td>71.8% (200mg Q8W) vs 70% (pbo)</td><td></td><td>47.4% vs 47.7%</td><td>58.4% vs 46.8%</td></tr><tr><td>Serious AEs</td><td>1% vs 3%</td><td>2.5%</td><td>7.7% (200mg Q8W) vs 0% (pbo)</td><td>6% vs 7%</td><td>1.2% vs 1.9%</td><td>1.7% vs 1.5%</td></tr><tr><td>AE leading to withdrawal</td><td>1% vs &lt;1%</td><td></td><td></td><td>2% vs 2%</td><td>0.7% vs 0.9%</td><td>2.1% vs 1.1%</td></tr></table>

Source: NEJM, AAD 2025, British Journal of Dermatology

Exhibit 2: HS-20118's once-weekly dosing profile may provide differentiation Landscape of oral IL-23 and IL-17 drugs in plaque psoriasis

<table><tr><td>Molecule</td><td>Target</td><td>Modality</td><td>Company</td><td>Stage</td><td>Dose interval</td></tr><tr><td>icotrokinra</td><td>IL-23R</td><td>peptide</td><td>J&amp;J / Protagonist</td><td>Approved</td><td>QD</td></tr><tr><td>HSK47388</td><td>IL-23</td><td>peptide</td><td>Haisco</td><td>Phase 2</td><td>QD</td></tr><tr><td>simepdekinra</td><td>IL-17</td><td>small molecule</td><td>DICE Therapeutics</td><td>Phase 2</td><td>n.a.</td></tr><tr><td>HS-20118</td><td>IL-23R</td><td>peptide</td><td>Hansoh / Avere</td><td>Phase 2</td><td>QW</td></tr><tr><td>UA026</td><td>IL-17A</td><td>small molecule</td><td>Usynova</td><td>Phase 1</td><td>n.a.</td></tr><tr><td>ZB021</td><td>IL-17A / IL-17F</td><td>small molecule</td><td>InnoCare / Zenas</td><td>Phase 1</td><td>QD or BID</td></tr><tr><td>ASC50</td><td>IL-17A</td><td>small molecule</td><td>Ascletis</td><td>Phase 1</td><td>QD or QW</td></tr><tr><td>PN-881</td><td>IL-17A / IL-17F</td><td>peptide</td><td>Protagonist</td><td>Phase 1</td><td>QD or BID</td></tr></table>

Source: Pharmcube

## Price Target Risks and Methodology - Hansoh Pharma

Valuation methodology: We are Buy rated on Hansoh Pharma with a 12-m TP of HK\$50.10. Our TP is based on a SOTP, comprised of 1) a DCF of HK\$281.4bn for innovative drugs; and 2) a valuation of HK\$21.9bn for generics, with a FY26 P/E of 10x.

Risks: 1) generics sales post VBP that are below expectations; 2) a slower ramp-up of novel drugs; 3) R&D risk in innovative drug pipeline; 4) below-expected collaboration income from pipeline global expansion.

<table><tr><td>3692.HK</td><td colspan="2">12m Price Target: HK$50.10</td><td colspan="2">Price: HK$32.56</td><td colspan="2">Upside: 53.9%</td></tr><tr><td colspan="2">Buy</td><td colspan="5">GS Forecast</td></tr><tr><td colspan="2"></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td rowspan="9" colspan="2">Market cap: HK$192.7bn / $24.6bnEnterprise value:HK$159.0bn / $20.3bn3m ADTV: HK$374.8mn / $47.8mnChinaChina Pharma &amp; BiotechM&amp;A Rank: 3Leases incl. in net debt &amp; EV?: No</td><td>Revenue (Rmb mn)</td><td>15,028.3</td><td>16,946.8</td><td>19,331.2</td><td>21,656.7</td></tr><tr><td>EBITDA (Rmb mn)</td><td>5,825.2</td><td>6,441.3</td><td>7,236.9</td><td>8,314.7</td></tr><tr><td>EPS (Rmb)</td><td>0.93</td><td>1.01</td><td>1.14</td><td>1.30</td></tr><tr><td>P/E (X)</td><td>29.2</td><td>27.9</td><td>24.6</td><td>21.7</td></tr><tr><td>P/B (X)</td><td>4.6</td><td>4.3</td><td>3.9</td><td>3.5</td></tr><tr><td>Dividend yield (%)</td><td>1.2</td><td>1.3</td><td>1.4</td><td>1.6</td></tr><tr><td>N debt/EBITDA (ex lease,X)</td><td>(5.4)</td><td>(4.5)</td><td>(5.2)</td><td>(4.4)</td></tr><tr><td>CROCI (%)</td><td>72.2</td><td>62.7</td><td>60.5</td><td>60.6</td></tr><tr><td>FCF yield (%)</td><td>3.4</td><td>(0.1)</td><td>6.6</td><td>0.9</td></tr><tr><td colspan="2"></td><td></td><td>6/25</td><td>12/25</td><td>6/26E</td><td>12/26E</td></tr><tr><td colspan="2"></td><td>EPS (Rmb)</td><td>0.52</td><td>0.40</td><td>0.49</td><td>0.51</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 14 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Ziyi Chen, Honglin Yan and Eddie Song, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Ziyi Chen GS (Asia) L.L.C., Honglin Yan GS (Asia) L.L.C., Eddie Song GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis for all metrics).

For a more detailed description of how we calculate the GS Factor Profile, please contact your GS representative.

## M&A Rank

Across our global coverage, we examine stocks using an M&A framework, considering both qualitative factors and quantitative factors (which may vary across sectors and regions) to incorporate the potential that certain companies could be acquired. We then assign a M&A rank as a means of scoring companies under our rated coverage from 1 to 3, with 1 representing high (30%-50%) probability of the company becoming an acquisition target, 2 representing medium (15%-30%) probability and 3 representing low (0%-15%) probability. For companies ranked 1 or 2, in line with our standard departmental guidelines we incorporate an M&A component into our target price. M&A rank of 3 is considered immaterial and therefore does not factor into our price target, and may or may not be discussed in research.

## Quantum

Quantum is GS' proprietary database providing access to detailed financial statement histories, forecasts and ratios. It can be used for in-depth analysis of a single company, or to make comparisons between companies in different sectors and markets.

## Disclosures

The rating(s) for Hansoh Pharma is/are relative to the other companies in its/their coverage universe: 3SBio Inc., Abbisko Therapeutics, Antengene, Ascletis Pharma Inc., BeOne Medicines Ltd. (A), BeOne Medicines Ltd. (ADR), Betta Pharma, CARsgen Therapeutics, CSPC Pharma, CStone Pharma, China Medical System Holdings, Everest Medicines, Fosun Pharma (A), Fosun Pharma (H), Hansoh Pharma, Hengrui Medicine, Henlius Biotech, Hepalink, Impact Therapeutics, InnoCare Pharma (A), InnoCare Pharma (H), Innovent Biologics, Jacobio Pharma, Kelun Biotech, Keymed Biosciences, Legend Biotech Corp., Livzon Pharmaceutical Group (A), Livzon Pharmaceutical Group (H), Luye Pharma Group, Ocumension, Sino Biopharmaceutical, United Laboratories Intl, Zai Lab (ADR), Zai Lab (H)

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Hansoh Pharma (HK\$32.56)

GS had an investment banking services client relationship during the past 12 months with: Hansoh Pharma (HK\$32.56)

GS makes a market in the securities or derivatives thereof: Hansoh Pharma (HK\$32.56)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/1ba1275a9b30b78ac0e6e2b3683b6a8f24cbb01f9ac04a4694e85f29e7ed02ef.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s) Hansoh Pharma (3692.HK)

<table><tr><td>Date of report</td><td>Target price (HK$)</td><td>Closing price (HK$)</td></tr><tr><td>01-Apr-26</td><td>50.10</td><td>37.42</td></tr><tr><td>05-Feb-26</td><td>49.49</td><td>36.62</td></tr><tr><td>18-Aug-25</td><td>39.93</td><td>37.06</td></tr><tr><td>08-Jul-25</td><td>34.83</td><td>30.65</td></tr><tr><td>23-Mar-25</td><td>22.71</td><td>20.10</td></tr><tr><td>11-Mar-25</td><td>21.51</td><td>18.80</td></tr><tr><td>28-Aug-24</td><td>20.97</td><td>20.60</td></tr><tr><td>19-May-24</td><td>19.27</td><td>18.24</td></tr><tr><td>29-Apr-24</td><td>17.91</td><td>17.48</td></tr><tr><td>26-Mar-24</td><td>17.11</td><td>14.88</td></tr><tr><td>05-Oct-23</td><td>16.86</td><td>10.06</td></tr><tr><td>31-Aug-23</td><td>16.86</td><td>10.20</td></tr><tr><td>13-Aug-23</td><td>17.61</td><td>10.26</td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's ar

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
