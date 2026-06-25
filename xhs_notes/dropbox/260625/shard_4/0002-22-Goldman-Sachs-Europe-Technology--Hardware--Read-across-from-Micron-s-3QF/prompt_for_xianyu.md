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
# Europe Technology: Hardware: Read-across from Micron's 3QFY26 results for European semicap and AI Infrastructure players

EUROPE TECHNOLOGY: HARDWARE
Analysing the role of European AI enablers and updating our view on long-term upside potential

Explore >

![](images/406b35d0c95ec59c591623c7ee41cc8e85bab52280ef60179adf0bc9a85a7788.jpg)

Alexander Duval  
+44(20)7552-2995 | alexander.duval@gs.com GS International

Anant Jakhar +1(332)245-7829 | anant.x.jakhar@gs.com GS India SPL

Micron (covered by our US team) reported 3QFY26 revenues of c.\$41.5bn (up +346% yoy and +74% qoq), materially above the Visible Alpha Consensus Data estimate of \$36.3bn. Further, the company guided for 4QFY26 revenues of \$50bn at the mid-point (up +21% qoq), which is c.15% above the Visible Alpha Consensus Data estimate of \$43.3bn going into the print. The company highlighted that its data center revenue in 3QFY26 came in above \$25bn (implying an ARR of around \$100bn). Additionally, Micron stated that AI is driving robust growth in DCs, with Memory demand significantly above supply. We note that MU expects this supply-demand imbalance to persist beyond CY27, with supply expected to improve gradually in 2028. In this vein, the company has now signed 16 take-or-pay strategic customer agreements (SCAs) across DC, consumer and automotive end markets. Importantly, our US semis team highlighted that many of these agreements contain both floor and ceiling prices, and the cumulative amount of committed revenue from these agreements represents c.\$100bn over five years at floor prices. Further, these contracts account for c.20% of MU's expected DRAM volume and a third of its NAND volume over the period. Separately, we note that Micron expects capex investment of c.\$10bn in 4QFY26 (implying FY26 capex of around \$27bn). Additionally, the company expects capex in FY27 to increase significantly yoy (GS currently models FY27 capex of \$50bn), with around 50% of the increase due to construction capex. Finally, we highlight that Micron recently agreed a multi-year EUV supply agreement with ASML (per Micron) supporting increased EUV adoption at its 1-delta node and future generations, which is a positive development for ASML and congruent with our view on increasing EUV layers in the coming years (more details in our note here). Below, we contextualise the implications of Micron's earnings and outlook for the European semicap and AI Infra players: ASML (Buy), ASMI (Buy), BESI (Buy), and NBIS (Buy).

## Readacross for European semicap and AI Infrastructure players:

We note that supply-demand tightness in Memory (both DRAM and NAND) due to continued AI demand suggests a positive near- to medium-term dynamic for the European semicap stocks ASML, ASMI and BESI given supply side tightness

Ayo Odunaiya  
+44(20)7051-5995 |  
ayo.x.odunaiya@gs.com  
GS International

results in better visibility for these players as customers are willing to share incremental details around technological and product ramp cadences.

Further, we believe ASML is best positioned on in our semicap coverage to benefit from this positive demand backdrop given its relatively higher exposure to Memory chips (around $40\%$ ) and longer lead times ( $>12$ months for its EUV tools). We note that ASM International is more skewed towards Logic demand, although it also has some memory exposure.

Furthermore, we see the continued strength of HBM demand as a positive for all three European semicap names but especially BESI given the company at its CMD reiterated that all three major Memory players are actively testing its Hybrid Bonding solutions for future adoption (see more details in our CMD note here). We believe that Memory adoption is a key component of HB demand in the coming years, and we see continued strong demand as encouraging for the adoption of this technology.

Finally, commentary around strong demand from AI bodes well for AI Infrastructure provider NBIS given the company's broad product portfolio of both bare metal and software offerings in tandem with its encouraging progress in expanding its contracted power capacity to serve this demand.

## Valuation and Key risks

ASML: We are Buy rated on ASML with a 12-month price target of €1,770 based on a 40x CY27 P/E multiple. Key risks to our view and price target include EUV delays, capex cyclicality and unfavourable market share shifts.

ASMI: We are Buy rated on ASMI with a 12-month price target of €955 based on a 25x CY27E EV/EBITDA multiple. Key risks to our view and price target include a worsening of the semi cycle, stronger-than-expected competition and high customer concentration.

BESI: We are Buy rated on BESI with a 12-month price target of €315 based on a 33x CY27 EV/EBITDA multiple. Key risks to our view and price target include customer spend cyclicality, hybrid bonding adoption delays and increasing competition.

Nebius: We are Buy rated on Nebius with a 12-month price target of \$267 based on a 9x CY27E EV/Sales multiple. Key risks to our view and price target include competitive pressure from Hyperscalers, slower-than-expected adoption of AI and reduced visibility from shorter-term contracts.

## Disclosure Appendix

## Reg AC

We, Alexander Duval, Anant Jakhar and Ayo Odunaiya, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Alexander Duval GS International, Anant Jakhar GS India SPL, Ayo Odunaiya GS International.

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

The rating(s) for ASM International, ASML Holding, BE Semiconductor Industries and Nebius Group is/are relative to the other companies in its/their coverage universe: ASM International, ASML Holding, BE Semiconductor Industries, CD Projekt, Ericsson, Infineon, Logitech, Nebius Group, Nokia, STMicroelectronics, Stillfront

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS is acting as a manager or co-manager of a pending underwriting: Nebius Group (\$259.66)

GS beneficially owned 5% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the month end preceding this report: Nebius Group (\$259.66)

GS has received compensation for investment banking services in the past 12 months: ASM International (€969.20), ASM International NV (ADR) (\$1,099.17), ASML Holding (€1,553.80), ASML Holding NV (ADR) (\$1,762.77) and Nebius Group (\$259.66)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: ASM International (€969.20), ASM International NV (ADR) (\$1,099.17), ASML Holding (€1,553.80), ASML Holding NV (ADR) (\$1,762.77), BE Semiconductor Industries (€292.90) and Nebius Group (\$259.66)

GS has received compensation for non-investment banking services during the past 12 months: Nebius Group (\$259.66)

GS had an investment banking services client relationship during the past 12 months with: ASM International (€969.20), ASM International NV (ADR) (\$1,099.17), ASML Holding (€1,553.80), ASML Holding NV (ADR) (\$1,762.77), BE Semiconductor Industries (€292.90) and Nebius Group (\$259.66)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: ASM International (€969.20), ASM International NV (ADR) (\$1,099.17), ASML Holding (€1,553.80), ASML Holding NV (ADR) (\$1,762.77) and Nebius Group (\$259.66)

GS had a non-securities services client relationship during the past 12 months with: ASML Holding (€1,553.80), ASML Holding NV (ADR) (\$1,762.77) and Nebius Group (\$259.66)

GS has managed or co-managed a public or Rule 144A offering in the past 12 months: ASM International (€969.20), ASM International NV

<table><tr><td>Date of report</td><td>Target price (€)</td><td>Closing price (€)</td><td>Date of report</td><td>Target price ($)</td><td>Closing price ($)</td></tr><tr><td>10-Jun-26</td><td>1,770.00</td><td>1,507.20</td><td>10-Jun-26</td><td>267.00</td><td>211.69</td></tr><tr><td>13-May-26</td><td>1,600.00</td><td>1,327.00</td><td>15-May-26</td><td>234.00</td><td>219.94</td></tr><tr><td>16-Apr-26</td><td>1,570.00</td><td>1,222.60</td><td>13-Apr-26</td><td>205.00</td><td>154.56</td></tr><tr><td>29-Jan-26</td><td>1,450.00</td><td>1,192.00</td><td>15-Feb-26</td><td>160.00</td><td>98.01</td></tr><tr><td>12-Jan-26</td><td>1,270.00</td><td>1,086.40</td><td>14-Nov-25</td><td>155.00</td><td>83.54</td></tr><tr><td>08-Dec-25</td><td>1,200.00</td><td>963.20</td><td>08-Oct-25</td><td>137.00</td><td>122.00</td></tr><tr><td>16-Oct-25</td><td>1,050.00</td><td>877.40</td><td>17-Sep-25</td><td>120.00</td><td>94.08</td></tr><tr><td>17-Jul-25</td><td>935.00</td><td>650.20</td><td>08-Aug-25</td><td>77.00</td><td>68.78</td></tr></table>

## (ADR) (\$1,099.17) and Nebius Group (\$259.66)

GS makes a market in the securities or derivatives thereof: ASML Holding (€1,553.80), ASML Holding NV (ADR) (\$1,762.77) and Nebius Group (\$259.66)

## Distribution of ratings/investment banking relationships

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/97677c2f5b978a8b19f330703786ad11d738c48d58ce6380bcb8074087bfa99d.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/5bf8124e64d95b76b33052f2bde1ba8aa47c52519e23563b494d364cffbfb99a.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/3930ec31c1800d8a702c5468d01ebea958241b3aff75f5a487ae2ab2086ed04b.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/0aac64543d554b3b4340186e9d48e35fb67947389b80aac306e6c25dbd1b5263.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s)

## ASML Holding (ASML.AS)

## Nebius Group (NBIS)

<table><tr><td colspan="3">ASML Holding (ASML.AS)</td></tr><tr><td>Date of report</td><td>Target price (€)</td><td>Closing price (€)</td></tr><tr><td>16-Apr-25</td><td>910.00</td><td>574.00</td></tr><tr><td>16-Oct-24</td><td>1,010.00</td><td>633.90</td></tr><tr><td>14-Jun-24</td><td>1,185.00</td><td>953.00</td></tr><tr><td>17-Apr-24</td><td>1,075.00</td><td>852.40</td></tr><tr><td>18-Mar-24</td><td>1,070.00</td><td>870.80</td></tr><tr><td>12-Feb-24</td><td>980.00</td><td>877.60</td></tr><tr><td>24-Jan-24</td><td>885.00</td><td>775.80</td></tr><tr><td>15-Jan-24</td><td>820.00</td><td>648.20</td></tr><tr><td>18-Oct-23</td><td>785.00</td><td>553.20</td></tr><tr><td>20-Sep-23</td><td>850.00</td><td>556.60</td></tr><tr><td>19-Jul-23</td><td>860.00</td><td>651.90</td></tr><tr><td>05

[中间内容因长度限制已省略]

including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS.

This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
