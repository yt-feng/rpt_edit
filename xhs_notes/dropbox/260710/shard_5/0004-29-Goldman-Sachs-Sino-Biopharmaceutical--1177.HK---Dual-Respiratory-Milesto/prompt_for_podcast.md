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
# Sino Biopharmaceutical (1177.HK): Dual Respiratory Milestones: AZ Out-licensing Deal and GSK Portfolio Expansion

Second BD deal with MNC; Licensing-out PDE3/4i to AZ: Sino Biopharm announced a licensing agreement with AstraZeneca for TQC3721 (a PDE3/4 inhibitor in phase 3), under which AZ obtains ex-China rights of TQC3721 for upfront payment of US\$200mn, up to US\$1.7bn in development, regulatory and commercial milestones, as well as tiered royalties ranging up to double-digit percentages based on net sales. In addition, AZ also gains global rights for certain future development programs for TQC3721, which are more innovative than ongoing clinical programs per company. TQC3721 has become the second China-originated PDE3/4 inhibitor to secure a major MNC partnership, following Hengrui's deal with GSK for its PDE3/4 inhibitor in 2025. The transaction marks Sino Biopharm's second major licensing-out deal with an MNC in 2026 following its earlier Sanofi partnership, further demonstrating the company's growing ability to generate globally competitive assets from its internal R&D platform.

Ziyi Chen  
+852-2978-0526 | ziyi.chen@gs.com  
GS (Asia) L.L.C.

Honglin Yan  
+852-2978-6666 | honglin.yan@gs.com  
GS (Asia) L.L.C.

Introducing two COPD drugs from GSK to strengthen respiratory portfolio: In addition to the TQC3721 out-licensing deal, the company also announced an expanding partnership with GSK following their collaboration on bepirovirsen. Through the introduction of Trelegy (LABA/LAMA/ICS) and Anoro (LABA/LAMA) from GSK for an initiation period of 5.5 years, Sino Biopharm further enriches its respiratory portfolio, which now comprises 30+ marketed respiratory products supported by a dedicated 2,000+ respiratory salesforce covering over 9,000 hospitals nationwide. The two products generated combined global sales of nearly US\$5bn in 2025, while current China sales remain below Rmb1bn in total, suggesting significant room for penetration and market share gains. More importantly, the products fit well within Sino Biopharm's existing COPD treatment matrix and strengthen the company's ability to serve the full spectrum of COPD patients for acute onset and maintenance therapy. Looking ahead, we believe the commercial platform could create meaningful synergies with the company's internally developed respiratory pipeline, including TQC3721 (PDE3/4 inhibitor), TSLP monoclonal antibody (TQC2731) and IL-4Ra monoclonal antibody (TQH2722).

Comparable efficacy of TQC3721 vs ensifentrine while differentiation from DPI formulation: Based on Phase 2 data, TQC3721 delivered placebo-adjusted improvements in FEV1 of approximately +100mL and +147mL at Week 4 for the 3mg and 6mg dose groups, respectively. This efficacy is largely comparable with the +124mL placebo-adjusted FEV1 improvement reported for first-mover ensifentrine 3mg in a non-head-to-head comparison (see Exhibit 1). Furthermore, TQC3721

demonstrated an encouraging safety profile, with no treatment discontinuations reported in the study. Beyond efficacy, we believe the dry powder inhaler (DPI) of TQC3721 could be a key differentiator with better convenience. While ensifentrine is currently marketed as a nebulized therapy, Sino Biopharm is simultaneously advancing both nebulized and DPI formulations of TQC3721, with the DPI version currently in Phase 2 development with Phase 1 data readout to be expected in 2H26.

Evolving COPD treatment aiming for broader patient coverage / long-acting agents: Compared with approved biologics for COPD such as dupilumab and mepolizumab, PDE3/4 inhibitors can potentially address a broader COPD population, as current biologics are largely focused on patients with type-2 inflammation and elevated eosinophil counts, which only account for a minority of COPD patients. However, the competitive landscape is evolving rapidly. AstraZeneca's tozorakimab (IL-33 mAb) has already delivered positive Phase 3 results and appears capable of treating a broad COPD population beyond traditional eosinophilic subgroups, potentially narrowing a key differentiation advantage of PDE3/4 inhibitors. Looking ahead, next-generation long-acting biologics may emerge as another disruptive force. For example, Keymed's CM512 (TSLP/IL13 bispecific antibody) is targeting a potential 3-6 month dosing interval and is expected to release Phase 2 COPD data by YE26, which could further shift the treatment paradigm toward broader coverage and improved convenience.

Estimates and valuation changes: Post deal announcement, we factor in the upfront payment of the AZ deal in 2H26, and also introduce sales estimates for Trelegy and Anoro, for which we expect to reach collective sales of Rmb1.2bn/1.4bn/1.7bn in 2026/27/28E (only reflecting 4Q sales for 2026). Therefore, our earnings estimates increased by +6.9%/+2.6%/+2.7% for 2026/27/28E. We also revise up PoLS for PDE3/4i from 80% to 100% given the global partner secured. Based on updated estimates and PoLS, our 12m-TP changed to HK\$8.41 from HK\$8.18.

Exhibit 1: Comparison of clinical data on COPD

<table><tr><td colspan="2"></td><td colspan="2">Ensifentrine</td><td colspan="2">TQC3721</td><td colspan="2">Dupilumab</td><td>Mepolizumab</td></tr><tr><td>MoA</td><td></td><td colspan="2">PDE3/4</td><td colspan="2">PDE3/4</td><td colspan="2">IL-4Rα</td><td>IL-5</td></tr><tr><td>Trial no.</td><td>NCT04535986</td><td>NCT04542057</td><td>NCT03937479</td><td>NCT06527144</td><td>NCT03930732</td><td colspan="2">NCT04456673</td><td>NCT04133909</td></tr><tr><td>Phase</td><td>Phase 3</td><td>Phase 3</td><td>Phase 2</td><td>Phase 2</td><td>Phase 3</td><td colspan="2">Phase 3</td><td>Phase 3</td></tr><tr><td colspan="9">Trial design</td></tr><tr><td>Indication</td><td></td><td colspan="2">COPD</td><td colspan="2">CDPD</td><td colspan="2">COPD with eosinophil &gt;=300/μL</td><td>COPD with eosinophil &gt;=300/μL</td></tr><tr><td>Intervention</td><td></td><td colspan="2">Ensifentrine vs placebo</td><td colspan="2">TQC3721 vs placebo</td><td colspan="2">Dupilumab vs placebo</td><td>Mepolizumab vs placebo</td></tr><tr><td>Dosing</td><td></td><td>Ensifentrine 3mg BID</td><td>Ensifentrine 0.375-3mg BID</td><td colspan="2">TQC3721 3/6mg BID</td><td colspan="2">Dupilumab 300mg Q2W</td><td>Mepolizumab 100mg Q4W</td></tr><tr><td>Background therapy</td><td></td><td></td><td></td><td colspan="2">LAMAs (28.8%), LABAs/LAMAs (71.2%)</td><td></td><td></td><td></td></tr><tr><td>Sample size</td><td>760</td><td>789</td><td>416</td><td>241</td><td>939</td><td colspan="2">935</td><td>804</td></tr><tr><td colspan="9">Efficacy data</td></tr><tr><td>annualized exacerbation rate</td><td>0.26 vs 0.41 (-36%)</td><td>0.24 vs 0.42 (-43%)</td><td></td><td></td><td>0.78 vs 1.10 (-30%)</td><td colspan="2">0.86 vs 1.30 (-34%)</td><td>0.80 vs 1.01 (-21%)</td></tr><tr><td>change in FEV1 at week 4 (ml)</td><td></td><td></td><td>+124 (3mg)</td><td>+100ml (3mg), +147ml (6mg)</td><td></td><td></td><td></td><td></td></tr><tr><td>change in FEV1 at week 12 (ml)</td><td>61 vs -26 (+87)</td><td>48 vs -46 (+94)</td><td></td><td></td><td>160 vs 77 (+83)</td><td colspan="2">139 vs 57 (+82)</td><td></td></tr><tr><td>SGRQ $^{1}$  score</td><td>-6.2 vs -3.9</td><td>-4.5 vs -4.1</td><td></td><td>-5.09</td><td>-9.7 vs -6.4</td><td colspan="2">comparable</td><td></td></tr><tr><td>E-RS-COPD $^{2}$  score</td><td>-2.2 vs -1.3</td><td>-2.1 vs -1.5</td><td></td><td></td><td>-2.7 vs -1.6</td><td></td><td></td><td></td></tr><tr><td colspan="9">Safety data</td></tr><tr><td>Serious TEAE</td><td>6.7% vs 6.7%</td><td>5.6% vs 5.8%</td><td></td><td>1.23% (3mg) vs 0% (6mg) vs 1.25%</td><td></td><td colspan="2">comparable for dupi vs pbo</td><td>comparable for mepo vs pbo</td></tr><tr><td>Any TEAE leading to death</td><td>0.4% vs 1.4%</td><td>0.8% vs 0.3%</td><td></td><td>0.0%</td><td></td><td colspan="2">comparable for dupi vs pbo</td><td>comparable for mepo vs pbo</td></tr><tr><td>Discontinued treatment owing to TEAE</td><td>6.1% vs 6.4%</td><td>9.0% vs 10.0%</td><td></td><td>0.0%</td><td></td><td colspan="2">comparable for dupi vs pbo</td><td>comparable for mepo vs pbo</td></tr></table>

Source: American Journal of Respiratory and Critical Care Medicine, American College of Chest Physicians, NEJM

## Price Target Risks and Methodology - Sino Biopharmaceutical

Our 12m SOTP-based TP is HK\$8.41. Our TP consists of 1) innovative pipeline: a DCF-based valuation of HK\$101.6bn; 2) generics: a valuation of HK\$50.2bn, based on an exit P/E of 10.0x and a 5-year CAGR of 5%; 3) anlotinib and PD-(L)1: a DCF-based valuation of HK\$6.0bn. Key downside risks: 1) broader price cut on generics portfolio; 2) delay in regulatory approval of key products in the pipeline; 3) low return of R&D investment due to inappropriate resource allocation; 4) below-expectation ramp-up of innovative drugs.

Sino Biopharm is a leading pharma company in China that is engaged in both innovative and generic drugs. Its key focus areas include hepatitis, oncology, cardio-cerebral, orthopaedic, respiratory and analgesic indications. As the majority of the negative impact from VBP implementation has been reflected for hepatitis drugs since 2019, we expect a neutral impact from VBP going forward for the company as it has $100+$ new generics expected to launch in the next three years to provide incremental sales. While we remain cautious on the company's R&D progress given the challenges of resource allocation within subsidiaries of the group, we see near-term drivers for the company from new to-be launched innovative drugs, including PD-1/L1, G-CSF, ROS1, ALKi, bepirovirsen and multiple biosimilars. We are Buy rated as we expect resilient earnings growth over the next two years and potentially more BD deals given its strong cash balance. The company is trading at the low end of its 5-year historical range. Key risks: 1) broader price cut on generics portfolio; 2) delay in regulatory approval of key products in the pipeline; 3) low return of R&D investment due to inappropriate resource allocation; 4) below-expectation ramp-up of innovative drugs.

<table><tr><td>1177.HK</td><td>12m Price Target: HK$8.41</td><td colspan="2">Price: HK$4.82</td><td colspan="2">Upside: 74.5%</td></tr><tr><td>Buy</td><td colspan="5">GS Forecast</td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td rowspan="11">Market cap: HK$90.4bn / $11.5bn Enterprise value: HK$105.7bn / $13.5bn 3m ADTV: HK$446.4mn / $57.0mn China China Pharma &amp; Biotech M&amp;A Rank: 3 Leases incl. in net debt &amp; EV?: No</td><td>Revenue (Rmb mn) New</td><td>31,834.5</td><td>37,802.7</td><td>42,005.9</td><td>46,261.8</td></tr><tr><td>Revenue (Rmb mn) Old</td><td>31,834.5</td><td>36,768.2</td><td>40,571.3</td><td>44,540.4</td></tr><tr><td>EBITDA (Rmb mn)</td><td>7,466.5</td><td>11,125.3</td><td>11,972.5</td><td>13,396.2</td></tr><tr><td>EPS (Rmb) New</td><td>0.13</td><td>0.24</td><td>0.26</td><td>0.29</td></tr><tr><td>EPS (Rmb) Old</td><td>0.13</td><td>0.22</td><td>0.25</td><td>0.29</td></tr><tr><td>P/E (X)</td><td>39.3</td><td>17.7</td><td>16.1</td><td>14.3</td></tr><tr><td>P/B (X)</td><td>3.0</td><td>2.3</td><td>2.1</td><td>1.9</td></tr><tr><td>Dividend yield (%)</td><td>1.0</td><td>2.1</td><td>2.3</td><td>2.6</td></tr><tr><td>CROCI (%)</td><td>3.9</td><td>34.3</td><td>32.3</td><td>31.0</td></tr><tr><td></td><td>6/25</td><td>12/25</td><td>6/26E</td><td>12/26E</td></tr><tr><td>EPS (Rmb)</td><td>0.19</td><td>(0.06)</td><td>0.12</td><td>0.11</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 8 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Ziyi Chen and Honglin Yan, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Ziyi Chen GS (Asia) L.L.C., Honglin Yan GS (Asia) L.L.C..

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

The rating(s) for Sino Biopharmaceutical is/are relative to the other companies in its/their coverage universe: 3SBio Inc., Abbisko Therapeutics, Antengene, Ascletis Pharma Inc., BeOne Medicines Ltd. (A), BeOne Medicines Ltd. (ADR), Betta Pharma, CARsgen Therapeutics, CSPC Pharma, CStone Pharma, China Medical System Holdings, Everest Medicines, Fosun Pharma (A), Fosun Pharma (H), Hansoh Pharma, Hengrui Medicine, Henlius Biotech, Hepalink, Impact Therapeutics, InnoCare Pharma (A), InnoCare Pharma (H), Innovent Biologics, Jacobio Pharma, Kelun Biotech, Keymed Biosciences, Legend Biotech Corp., Livzon Pharmaceutical Group (A), Livzon Pharmaceutical Group (H), Luye Pharma Group, Ocumension, Sino Biopharmaceutical, United Laboratories Intl, Zai Lab (ADR), Zai Lab (H)

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS has received compensation for investment banking services in the past 12 months: Sino Biopharmaceutical (HK\$4.82)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Sino Biopharmaceutical (HK\$4.82)

GS had an investment banking services client relationship during the past 12 months with: Sino Biopharmaceutical (HK\$4.82)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: Sino Biopharmaceutical (HK\$4.82)

GS had a non-securities services client relationship during the past 12 months with: Sino Biopharmaceutical (HK\$4.82)

GS makes a market in the securities or derivatives thereof: Sino Biopharmaceutical (HK\$4.82)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/1ecf0ed27d4616e1794078bdf51c3fe72c4da17266125558360718a0dbcda0da.jpg)  
The price targets shown should be considered in the context of all prior published GS rese

[中间内容因长度限制已省略]

term impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

© 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
