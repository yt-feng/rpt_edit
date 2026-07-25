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
# Digital Realty Trust Inc. (DLR): 2Q26 review: Growing backlog and favorable pricing dynamics support beat & raise

DLR’s core FFO per share of \$2.65 beat GS/consensus (Visible Alpha) of \$1.97/\$1.98 driven by strong underlying growth, as well as net promote; excluding net promote, core FFO per share of \$2.13 still beat. First, bookings of \$208 mn at DLR share included \$108 mn of 0-1MW and interconnection bookings, beating consensus bookings of \$199 mn (but missing our estimate of \$247 mn). Notably, DLR signed 2 hyperscaler leases in July representing \$205 mn bookings at DLR share. Second, DLR renewed \$261 mn of annualized rental revenue at 25% cash renewal spread reflecting 5% spreads in 0-1MW and 67% spreads in >1MW related to supply/demand tightness in Singapore. Third, DLR raised its 2026E core FFO per share (excludes net promote) guidance to \$8.15-\$8.20 (v. \$8.00-\$8.10). DLR expects commencements to accelerate meaningfully in 2H26 as \$635mn of annualized rent is scheduled to commence (45% in 3Q26 & 55% in 4Q26). DLR is also seeing growing fee income within its strategic private capital platform. We continue to view DLR as among the best positioned to satisfy hyperscale demand for wholesale capacity with \~1.4GW under construction, and view the company’s growing and increasingly diversified backlog (\$1.4 bn DLR share exiting 2Q26 with new markets and 142 customers added in 2Q26) as reflective of the visibility into the company’s ability to see continued growth over the medium term.

Read-through to our coverage: DLR noted increasing levels of engagement from customers deploying AI-enabled applications, which we see as a positive read through for Equinix (reporting July 29), which is more indexed towards retail colocation.

DLR delivered an in-quarter beat and raise driven by strength in rental revenues.

■ DLR rental revenue of \$1,146 mn beat GSe/Visible Alpha Consensus \$1,094/\$1,119 mn.

☐ Total revenue came in at \$1,924 mn above GS at \$1,615 mn and the Street at \$1,655 mn.

☐ DLR’s share of total new bookings came in at \$208 mn at its share (v. GS at \$247 mn), down from \$243 mn in 1Q26 but up from \$135 mn in 2Q25. 0-1 MW plus interconnect bookings were \$108 mn, up from \$98 mn in 1Q26 and \$90 mn in 2Q25.

\- Adjusted EBITDA of \$978 mn beat our estimate of \$913 mn and the Street at \$914 mn.

Michael Ng, CFA
+1(212)902-8618 | michael.ng@gs.com
GS & Co. LLC

Lindsey Shema
+1(801)578-2673 |
lindsey.shema@gs.com
GS & Co. LLC

Yash Goenka, CFA
+1(212)934-6312 |
yash.goenka@gs.com
GS India SPL

Zorayda Montemayor
+1(212)357-6403 |
zorayda.montemayor@gs.com
GS & Co. LLC

Core FFO per share (excluding net promote) came in at \$2.13, above GSe/consensus at \$1.97/\$1.98.

■ AFFO per share came in at \$2.47, above GS/Street at \$1.84/\$1.80.

2026 guidance updated, including: (1) Core FFO per share of \$8.15-\$8.20 (v. \$8.00-\$8.10 prior); (2) 2026 revenues of \$6,850-\$6,950 mn (v. \$6,650-\$6,750 mn prior); (3) 2026 cash basis rental rates on renewal leases of 9.0-11.0% (v. 6.5-8.5% prior); (4) Adjusted EBITDA between \$3.75-\$3.85 bn (v. \$3.65-\$3.75 bn prior); (5) Development capex (net of partner contributions) between \$4.25-\$4.75 bn (v. \$3.5-\$4.0 bn prior); and (6) recurring capex between \$400-\$425 mn (unchanged).

Estimate changes: We raise our revenue/EBITDA estimates by 7%/4% on average in 2026/27/28 on the company’s raised outlook.

Price target and risks. We are Buy rated on DLR with a 12-month revised target price of \$223 (vs \$215 prior) based on a 26X (unchanged) NTM+1Y P/AFFO. Our price target increases due to rolling over our NTM+1Y AFFO.

Key downside risks: (1) excess supply-side dynamics in the data center market; (2) weaker-than-expected demand dynamics from key datacenter customers; (3) more intense price competition.

We reiterate our Buy rating on DLR. We believe Digital Realty is well positioned to benefit from the supply/demand tightness in the datacenter industry, which we think will persist for longer than the market expects.

Exhibit 1: Digital Realty - Variance summary

<table><tr><td></td><td colspan="5">2Q26</td><td colspan="2">2Q25</td></tr><tr><td>Consolidated ($ millions)</td><td>Actual</td><td>GS</td><td>Actual/Gse</td><td>Street</td><td>Actual/Street</td><td>Actual</td><td>Y/Y %</td></tr><tr><td>Rental revenues</td><td>1,146</td><td>1,094</td><td>4.7%</td><td>1,119</td><td>2.4%</td><td>1,004</td><td>19.3%</td></tr><tr><td>Total Revenue</td><td>1,924</td><td>1,615</td><td>19.1%</td><td>1,655</td><td>16.3%</td><td>1,493</td><td>36.7%</td></tr><tr><td>Adjusted EBITDA</td><td>978</td><td>913</td><td>7.1%</td><td>914</td><td>6.9%</td><td>823</td><td>23.6%</td></tr><tr><td>Core FFO per share</td><td>$2.13</td><td>$1.97</td><td>8.1%</td><td>$1.98</td><td>7.5%</td><td>$1.87</td><td>20.1%</td></tr><tr><td>AFFO</td><td>889</td><td>659</td><td>34.9%</td><td>642</td><td>38.4%</td><td>576</td><td>45.7%</td></tr><tr><td>AFFO per Share</td><td>$2.47</td><td>$1.84</td><td>34.4%</td><td>$1.80</td><td>37.2%</td><td>$1.68</td><td>38.9%</td></tr><tr><td>Leasing</td><td>208</td><td>247</td><td>-15.6%</td><td>199</td><td>4.7%</td><td>135</td><td>-14.0%</td></tr></table>

Source: Company data, GS Global Investment Research, Visible Alpha Consensus Data

Exhibit 2: Digital Realty - Old vs. new estimates

<table><tr><td></td><td colspan="7">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>Consolidated ($ millions)</td><td>New</td><td>Old</td><td>Δ</td><td>Y/Y (%)</td><td>Guidance</td><td>Street</td><td>GS/Street</td><td>New</td><td>Old</td><td>Δ</td><td>New</td><td>Old</td><td>Δ</td></tr><tr><td>Rental revenues</td><td>4,712</td><td>4,512</td><td>4.4%</td><td>15.4%</td><td></td><td>4,558</td><td>3.4%</td><td>5,642</td><td>5,182</td><td>8.9%</td><td>6,308</td><td>5,788</td><td>9.0%</td></tr><tr><td>Total Revenue</td><td>7,170</td><td>6,703</td><td>7.0%</td><td>17.3%</td><td>6,850 - 6,950 mn</td><td>6,754</td><td>6.2%</td><td>8,046</td><td>7,519</td><td>7.0%</td><td>8,889</td><td>8,298</td><td>7.1%</td></tr><tr><td>Adjusted EBITDA</td><td>3,855</td><td>3,758</td><td>2.6%</td><td>15.5%</td><td>3,750 - 3,850 mn</td><td>3,729</td><td>3.4%</td><td>4,394</td><td>4,214</td><td>4.3%</td><td>4,791</td><td>4,588</td><td>4.4%</td></tr><tr><td>EPS</td><td>$3.13</td><td>$2.68</td><td>16.8%</td><td>-14.1%</td><td></td><td>$2.08</td><td>50.5%</td><td>$2.08</td><td>$2.02</td><td>3.3%</td><td>$2.41</td><td>$2.33</td><td>3.6%</td></tr><tr><td>Core FFO per share</td><td>$8.20</td><td>$8.14</td><td>0.8%</td><td>10.9%</td><td>$8.150 - $8.200</td><td>$8.04</td><td>2.0%</td><td>$9.03</td><td>$8.83</td><td>2.3%</td><td>$9.68</td><td>$9.49</td><td>2.0%</td></tr><tr><td>AFFO</td><td>2,628</td><td>2,600</td><td>1.1%</td><td>15.9%</td><td></td><td>2,557</td><td>2.8%</td><td>3,244</td><td>3,008</td><td>7.8%</td><td>3,558</td><td>3,305</td><td>7.7%</td></tr><tr><td>AFFO per Share</td><td>$7.14</td><td>$7.25</td><td>-1.5%</td><td>9.0%</td><td></td><td>$7.12</td><td>0.3%</td><td>$8.35</td><td>$8.13</td><td>2.7%</td><td>$8.92</td><td>$8.72</td><td>2.3%</td></tr><tr><td>Leasing</td><td>1,071</td><td>1,168</td><td>-8.3%</td><td>50.0%</td><td></td><td>1,131</td><td>-5.3%</td><td>916</td><td>1,015</td><td>-9.8%</td><td>937</td><td>1,038</td><td>-9.8%</td></tr></table>

Source: Company data, GS Global Investment Research

<table><tr><td>Buy</td><td colspan="5">GS Forecast</td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Market cap: $64.7bn</td><td>Revenue ($ mn) New</td><td>6,112.7</td><td>7,170.5</td><td>8,045.7</td><td>8,889.3</td></tr><tr><td>Enterprise value: $83.6bn</td><td>Revenue ($ mn) Old</td><td>6,112.7</td><td>6,702.9</td><td>7,518.9</td><td>8,297.9</td></tr><tr><td>3m ADTV: $523.3mn</td><td>EBITDA ($ mn)</td><td>3,339.1</td><td>3,855.0</td><td>4,393.5</td><td>4,790.9</td></tr><tr><td>United States</td><td>EBIT ($ mn)</td><td>658.5</td><td>1,124.7</td><td>1,331.9</td><td>1,514.3</td></tr><tr><td rowspan="2">Americas Hardware, Media, Cable,Telco</td><td>EPS ($) New</td><td>3.65</td><td>3.13</td><td>2.08</td><td>2.41</td></tr><tr><td>EPS ($) Old</td><td>3.65</td><td>2.68</td><td>2.02</td><td>2.33</td></tr><tr><td rowspan="3">M&amp;A Rank: 3</td><td>P/E (X)</td><td>45.4</td><td>57.3</td><td>86.1</td><td>74.4</td></tr><tr><td>Dividend yield (%)</td><td>3.0</td><td>2.7</td><td>2.7</td><td>2.7</td></tr><tr><td>Net debt/EBITDA (X)</td><td>4.5</td><td>4.5</td><td>4.5</td><td>4.5</td></tr><tr><td></td><td></td><td>6/26</td><td>9/26E</td><td>12/26E</td><td>3/27E</td></tr><tr><td></td><td>EPS ($)</td><td>1.21</td><td>0.71</td><td>0.72</td><td>0.44</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 23 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Michael Ng, CFA, Lindsey Shema, Yash Goenka, CFA and Zorayda Montemayor, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Michael Ng, CFA GS & Co. LLC, Lindsey Shema GS & Co. LLC, Yash Goenka, CFA GS India SPL, Zorayda Montemayor GS & Co. LLC.

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

The rating(s) for Digital Realty Trust Inc. is/are relative to the other companies in its/their coverage universe: AT&T Inc., American Tower Corp., Apple Inc., Arista Networks Inc., Axon Enterprise Inc., Blend Labs, Celestica Inc., Charter Communications Inc., Cisco Systems Inc., Cogent Communications Holdings, Comcast Corp., Compass Inc., Crown Castle Inc., Dell Technologies Inc., Digital Realty Trust Inc., Equinix Inc., F5 Inc., HP Inc., Hewlett Packard Enterprise Co., IREN Ltd., Ingram Micro, Lumen Technologies Inc., NetApp Inc., Opendoor Technologies Inc., Optimum Communications Inc., Penguin Solutions Inc., SBA Communications Corp., Stagwell Inc., Super Micro Computer Inc., T-Mobile US Inc., TD SYNNEX Corp., Verizon Communications, Versant Media Group, Walt Disney Co., Zillow Group

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS has received compensation for investment banking services in the past 12 months: Digital Realty Trust Inc. (\$179.34)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Digital Realty Trust Inc. (\$179.34)

GS had an investment banking services client relationship during the past 12 months with: Digital Realty Trust Inc. (\$179.34)

GS had a non-securities services client relationship during the past 12 months with: Digital Realty Trust Inc. (\$179.34)

GS makes a market in the securities or derivatives thereof: Digital Realty Trust Inc. (\$179.34)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys

and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/73f3982de3ad9cddb23ea1ffde807c94f78dfb374fa0975a405a809b3e42bafc.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s) Digital Realty Trust Inc. (DLR)

<table><tr><td>Date of r

[中间内容因长度限制已省略]

including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any

such system.
"""
