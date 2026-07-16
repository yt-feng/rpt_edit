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
# Kelun Biotech (6990.HK): Lung06 met primary endpoint; further validates sac-TMT as 1L NSCLC backbone

PFS superiority announced for OptiTROP-Lung06: On July 15th, Kelun Biotech announced positive topline for the China ph3 OptiTROP-Lung06 trial (1L nsq-NSCLC with PD-L1 TPS<1%) meeting the primary endpoint (PFS). In a head-to-head comparison with the SOC (pembro plus pemetrexed/platinum combo), sac-TMT/pembro combo demonstrated significantly prolonged PFS and a positive OS trend, as well as a manageable safety profile with no new safety findings. The positive topline of OptiTROP-Lung06 marks another significant China ph3 success in 1L NSCLC after the bar-setting success of OptiTROP-Lung05 (PFS HR of 0.35 in 1L NSCLC with PD-L1 TPS≥1%) at ASCO2026 (see our takeaways, LINK, LINK), and more importantly provided direct evidence of superiority of sac-TMT/pembro combo over the pembro/chemo combo (vs. Lung05 trial which used pembro mono as the control arm).

Eyes on ESMO for data details, reiterate expectation of 9-12m PFS: With the positive topline announcement, we expect detailed data to be shared at an upcoming conference, noting that mgmt were considering the ESMO LBA submission (see our Corp Day takeaway). We reiterate our previous expectations of 9-12m of PFS for Lung06, based on 1) the China ph2 OptiTROP-Lung01 trial that showed 12.4m of PFS in the TPS<1% subgroup for sac-TMT/A167 combo, and 2) the incremental information from Lung05 trial that we estimated mPFS of 13-15m for PD-L1 TPS 1-49% subgroup for sac-TMT/pembro combo, with the caveat that shorter survival benefit to be expected in TPS<1% given the lower PD-L1 expression.

Ziyi Chen  
+852-2978-0526 | ziyi.chen@gs.com  
GS (Asia) L.L.C.

population: We view OptiTROP-Lung06 as a key piece for the coverage of sac-TMT in 1L NSCLC (Exhibit 1), with continued discussions on whether MRK will initiate (and how) global ph3 trials targeting the KEYNOTE-189 population (pembro+chemo in 1L NSCLC regardless of TPS, c.40% TPS<1%), and the core debate is on the extent of superiority of sac-TMT/IO combo over pembro/chemo combo in 1L NSCLC in order to secure a significant survival superiority in a global ph3 head-to-head setting. We see the positive results of the Lung05/06 trials as incremental de-risking steps for the discussion, with: 1) the in-direct implications from Lung05 data, in particular the strong PFS observation of sac-TMT/pembro combo in PD-L1 TPS 1-49% subgroup (HR of 0.28 over pembro mono) suggested 13-15m of mPFS, which appears favorable towards statistical significance compared to historical data of pembro/chemo duplets with mPFS range of 7-9m (see our detailed takeaway on Lung05 subgroups), and 2) the upcoming detailed data of Lung06 at ESMO to

## Another key de-risk step for global clinical plan targeting KEYNOTE-189

Linhai Zhao, Ph.D. +852-3966-4059 | linhai.zhao@gs.com GS (Asia) L.L.C.

provide direct head-to-head superiority of sac-TMT/pembro combo over pembro/chemo. Recall that Kelun Biotech mgmt shared that the global ph3 trials of sac-TMT for $1 - 49\%$ population is a matter of whether to use PD-1 or PD-1/VEGF as the combo partner, and we expect more discussion on the potential global ph3 trials for KEYNOTE-189 population with the detailed data of Lung06 coming out.

Exhibit 1: We expect OptiTROP-Lung05/06 data as key de-risk step for global ph3 trials in 1L NSCLC, with eyes on PD-L1 1-49% group
Current standard of care and mapping of ph3 sac-TMT trials in 1L NSCLC  
![](images/0ab86e9321e7edd22e85cf7fe8e171d72fe73cbfeb459dbef11c373971846fc7.jpg)  
Source: NCCN Guidelines

Valuation and TP changes: We adjust our 12-month target price to HK\$582.95 (prev. HK\$561.40), which is based on a risk-adjusted DCF methodology. We adjust 2027E-28E EPS from Rmb7.49/Rmb14.32 to Rmb7.51/Rmb14.46 to reflect the strengthened view on 1L NSCLC, with 1) increased POS for Lung06 from 81% to 90%, and 2) increased POS for 1L NSCLC PD-L1 TPS <50% in ex-China from 54% to 63%.

Kelun Biotech is a clinical-stage biotech company focused on developing and commercializing differentiated antibody drug conjugates (ADCs) for global patients. We believe Kelun Biotech is well-positioned to grow into a meaningful global ADC player with 1) differentiated late-stage ADCs; 2) deep R&D know-how driving pipeline expansion; and 3) extensive collaborations with MSD for global market access (3 clinical stage and 4 pre-clinical assets, and MSD as a top shareholder) and Kelun Pharma (the parent company) for China commercialization. We expect SKB264 (TROP2 ADC) to be the key driver of Kelun Biotech's future growth given: 1) the broad spectrum of indications where TROP2 has over-expression (e.g., BC/NSCLC/UC/GC), 2) the unique drug design of SKB264 could potentially deliver clinical benefits over TROP2 ADC peers as illustrated in early encouraging data, and 3) the strong leverage of MSD's expertise and network in the global market to drive clinical development and commercialization. We are Buy rated. Key risks: 1) R&D risks in developing new indications and future ADCs; 2) increasingly heated competition in ADC field; 3) limited commercial manufacturing and sales track record; 4) challenges in talent competition; and 5) alliance risks in partnership.

We have a Buy rating on Kelun Biotech. Our 12-m TP of HK\$582.95 is based on a risk-adjusted DCF methodology assuming: 1) 11% discount rate; 2) 3% terminal growth rate; and 3) probability of success (PoS) based on industry average success rates in different stages and adjustments based on available clinical data. Key risks: 1) R&D risks in developing new indications and future ADCs; 2) increasingly heated competition in ADC field; 3) limited commercial manufacturing and sales track record; 4) challenges in talent competition; and 5) alliance risks in partnership.

<table><tr><td>6990.HK</td><td colspan="2">12m Price Target: HK$582.95</td><td colspan="2">Price: HK$498.20</td><td colspan="2">Upside: 17.0%</td></tr><tr><td colspan="2">Buy</td><td colspan="5">GS Forecast</td></tr><tr><td colspan="2"></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td rowspan="11" colspan="2">Market cap: HK$114.9bn / $14.7bn Enterprise value: HK$111.3bn / $14.2bn 3m ADTV: HK$448.9mn / $57.3mn China China Pharma &amp; Biotech M&amp;A Rank: 3 Leases incl. in net debt &amp; EV?: Yes</td><td>Revenue (Rmb mn) New</td><td>2,057.9</td><td>3,111.1</td><td>5,447.6</td><td>7,907.2</td></tr><tr><td>Revenue (Rmb mn) Old</td><td>2,057.9</td><td>3,111.1</td><td>5,437.3</td><td>7,855.6</td></tr><tr><td>EBITDA (Rmb mn)</td><td>(435.3)</td><td>356.9</td><td>2,069.6</td><td>3,951.9</td></tr><tr><td>EPS (HK$) New</td><td>(1.66)</td><td>1.39</td><td>7.51</td><td>14.46</td></tr><tr><td>EPS (HK$) Old</td><td>(1.66)</td><td>1.39</td><td>7.49</td><td>14.32</td></tr><tr><td>P/E (X)</td><td>NM</td><td>NM</td><td>66.3</td><td>34.5</td></tr><tr><td>P/B (X)</td><td>15.4</td><td>18.3</td><td>13.4</td><td>9.0</td></tr><tr><td>Dividend yield (%)</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>CROCI (%)</td><td>(8.5)</td><td>25.4</td><td>94.0</td><td>140.2</td></tr><tr><td></td><td>6/25</td><td>12/25</td><td>6/26E</td><td>12/26E</td></tr><tr><td>EPS (HK$)</td><td>(0.64)</td><td>(1.03)</td><td>0.27</td><td>1.56</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 14 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Ziyi Chen and Linhai Zhao, Ph.D., hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Ziyi Chen GS (Asia) L.L.C., Linhai Zhao, Ph.D. GS (Asia) L.L.C..

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

The rating(s) for Kelun Biotech is/are relative to the other companies in its/their coverage universe: 3SBio Inc., Abbisko Therapeutics, Antengene, Ascletis Pharma Inc., BeOne Medicines Ltd. (A), BeOne Medicines Ltd. (ADR), Betta Pharma, CARsgen Therapeutics, CSPC Pharma, CSstone Pharma, China Medical System Holdings, Everest Medicines, Fosun Pharma (A), Fosun Pharma (H), Hansoh Pharma, Hengrui Medicine, Henlius Biotech, Hepalink, Impact Therapeutics, InnoCare Pharma (A), InnoCare Pharma (H), Innovent Biologics, Jacobio Pharma, Kelun Biotech, Keymed Biosciences, Legend Biotech Corp., Livzon Pharmaceutical Group (A), Livzon Pharmaceutical Group (H), Luye Pharma Group, Ocumension, Sino Biopharmaceutical, United Laboratories Intl, Zai Lab (ADR), Zai Lab (H)

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS has received compensation for investment banking services in the past 12 months: Kelun Biotech (HK\$498.20)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Kelun Biotech (HK\$498.20)

GS had an investment banking services client relationship during the past 12 months with: Kelun Biotech (HK\$498.20)

GS has managed or co-managed a public or Rule 144A offering in the past 12 months: Kelun Biotech (HK\$498.20)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See 'Ratings, Coverage universe and related definitions' below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

Price target and rating history chart(s)  
![](images/c2cf8ffa370587e3ed2e30a11d523840295e01d88a06e277c33a165e5e92db1a.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s) Kelun Biotech (6990.HK)

<table><tr><td>Date of report</td><td>Target price (HK$)</td><td>Closing price (HK$)</td></tr><tr><td>31-May-26</td><td>561.40</td><td>462.00</td></tr><tr><td>23-Mar-26</td><td>526.49</td><td>397.60</td></tr><tr><td>05-Feb-26</td><td>531.69</td><td>420.20</td></tr><tr><td>07-Jan-26</td><td>495.78</td><td>473.80</td></tr><tr><td>20-Oct-25</td><td>492.40</td><td>479.20</td></tr><tr><td>18-Aug-25</td><td>454.04</td><td>446.80</td></tr><tr><td>08-Jul-25</td><td>406.74</td><td>343.00</td></tr><tr><td>26-May-25</td><td>284.14</td><td>315.60</td></tr><tr><td>24-Mar-25</td><td>262.91</td><td>260.60</td></tr><tr><td>13-Mar-25</td><td>239.14</td><td>238.00</td></tr><tr><td>19-Jan-25</td><td>226.56</td><td>162.60</td></tr><tr><td>27-Nov-24</td><td>226.32</td><td>196.00</td></tr><tr><td>20-Aug-24</td><td>219.74</td><td>168.30</td></tr><tr><td>26-Mar-24</td><td>209.81</td><td>160.60</td></tr><tr><td>13-Mar-24</td><td>136.66</td><td>135.20</td></tr><tr><td>11-Jan-24</td><td>123.09</td><td>106.50</td></tr><tr><td>29-Aug-23</td><td>116.77</td><td>81.00</td></tr><tr><td>13-Aug-23</td><td>115.00</td><td>77.20</td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client's objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the adv

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
