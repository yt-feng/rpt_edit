你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

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

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialis

[中间内容因长度限制已省略]

es, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

© 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
