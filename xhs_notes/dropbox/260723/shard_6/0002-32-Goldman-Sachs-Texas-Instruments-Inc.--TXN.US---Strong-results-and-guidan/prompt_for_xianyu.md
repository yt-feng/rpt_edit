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
# Texas Instruments Inc. (TXN): Strong results and guidance suggests continued momentum in the analog recovery

Key stock takeaways: We expect the stock to be range bound following a quarter and guidance that came in above the Street. We believe expectations were somewhat elevated given management's intra-quarter commentary on a fundamental recovery and the stock's outperformance over the past quarter, and based on our conversations we believe results were consistent with these expectations. We see the strong recovery in the industrial end market, as well as the beginning of broadening automotive demand improvement, as a particularly encouraging read-across for the sector. Although we continue to see a recovery across the analog sector (including for TI), we believe peers have managed their inventory levels more proactively — and hence we believe gross margins are likely to recover faster for peers (along with significant upward earnings revisions) than for TI. We continue to have a preference for peers (including Microchip and NXP) who are likely to see greater upward earnings revisions in the near term, and we retain our relative Sell rating on TXN given the ongoing gross margin headwinds we expect in the coming quarters.

Read-through to our coverage: We expect a positive initial reaction for the analog group, with the most direct read-across for NXPI (Buy), ON (Neutral), and ADI (Buy) given their relatively high automotive exposures following the incrementally positive commentary around this end market.

Quarterly revenue and EPS are above the Street: TI reported 2Q26 revenue of \$5.46 bn, above GS at \$5.38 bn and the Street (Visible Alpha) at \$5.26 bn. Gross margin of 61.4% was well above GS at 59.4% and the Street at 59.5%. Operating margin of 42.3% was well above GS at 40.9% and the Street at 40.5%. EPS of \$2.14 was above GS at \$1.99 and the Street at \$1.94.

End market trends: TI's 1Q26 industrial revenue increase of about $10\%$ QoQ was ahead of our expectations - and the company's 3Q revenue guidance of up $\sim 8\%$ QoQ (at the midpoint) suggests a continued cyclical recovery across the supply chain. The company noted that it continues to see the market continuing to improve, with demand broadening to areas such as automotive. Automotive was up in the high-single digits QoQ, personal electronics was up high-single digits QoQ, communications equipment was up QoQ, and datacenter revenue was up $20\%$ QoQ in 2Q.

\- Inventory levels: Inventory on the balance sheet was lower (down \~\$90mn) on a sequential basis to \$4.6bn and inventory days ticked 13 days lower to 196, which

James Schneider, Ph.D.  
+1(212)357-2929 | jim.schneider@gs.com GS & Co. LLC

Khalil Fenina
+1(212)357-6392 |
khalil.fenina@gs.com
GS & Co. LLC

Anmol Makkar
+1(212)357-1366 |
anmol.makkar@gs.com
GS & Co. LLC

Luya You
+1(212)902-5297 | luya.you@gs.com
GS & Co. LLC

we view as encouraging. Management intends to manage its factory loadings dynamically in order to manage internal inventory levels according to customer demand. Although we see this trend as a positive for the company's gross margins over time, we expect TI's gross margin expansion to lag peers as the recovery continues.

\- Margins: TI's implied 2Q gross margin guidance is for gradual expansion QoQ as the company manages its factory loadings to end demand, which implies gross margins up by \~100bp in 3Q (we model for 3Q26 GM of 62.4% vs. 61.4% in 2Q26)— and we expect this trend to largely continue over the course of 2026.

3Q revenue and EPS guidance are above the Street. TI guided 3Q above the Street on revenue and EPS. Revenue was guided to \$5.90 bn at the midpoint, which is above GS at \$5.65 bn and the Street at \$5.63 bn. OpEx is expected to be roughly flat QoQ in 3Q. TI's tax rate is expected to be \~13%. EPS guidance of \$2.40 at the midpoint is well above both GS at \$2.14 and the Street at \$2.18.

Estimate changes. We increase our 2025-2027 EPS estimates by an average of $9\%$ to mainly reflect higher revenue and gross margins than we had previously modeled (see detailed estimates below — Exhibit 3).

Price target. We raise our 12-month price target to \$225 (from \$200 previously) is based on a 25X P/E multiple (unchanged) applied to our normalized EPS estimate of \$9.00 (from \$8.00 previously on higher estimates). Key upside risks: 1) upside to end-demand across key verticals; 2) a reversal in market share dynamics; 3) better-than-expected gross margin performance and/or OpEx leverage.

We are Sell rated on TXN. Our Sell rating on TXN is driven by our view that its margin expansion is likely to under-run peers (such as Microchip and NXP) during the ongoing analog recovery given TI's significantly higher inventory levels.

Exhibit 1: TXN - Variance summary

<table><tr><td rowspan="2">Financials ($ mn, except EPS)</td><td colspan="5">2Q26</td></tr><tr><td>Actual</td><td>GS</td><td>Street</td><td>Actual/GS</td><td>Actual/Street</td></tr><tr><td>Revenue</td><td>5,463</td><td>5,380</td><td>5,262</td><td>1.5%</td><td>3.8%</td></tr><tr><td>QoQ</td><td>13.2%</td><td>11.5%</td><td>9.0%</td><td></td><td></td></tr><tr><td>YoY</td><td>22.8%</td><td>21.0%</td><td>18.3%</td><td></td><td></td></tr><tr><td>Gross Margin</td><td>61.4%</td><td>59.4%</td><td>59.5%</td><td>+197 bps</td><td>+183 bps</td></tr><tr><td>Operating Income</td><td>2,310</td><td>2202</td><td>2,128</td><td>4.9%</td><td>8.5%</td></tr><tr><td>Operating Margin</td><td>42.3%</td><td>40.9%</td><td>40.5%</td><td>+136 bps</td><td>+183 bps</td></tr><tr><td>EPS - GAAP</td><td>$2.14</td><td>$1.99</td><td>$1.94</td><td>7.8%</td><td>10.4%</td></tr></table>

Source: Company data, GS Global Investment Research, Visible Alpha Consensus Data

Exhibit 2: TXN - Guidance summary

<table><tr><td rowspan="2">Financials ($ mn, except EPS)</td><td colspan="7">3Q26</td></tr><tr><td>High</td><td>Low</td><td>Guidance (midpoint)</td><td>GS</td><td>Street</td><td>Guidance/GS</td><td>Guidance/Street</td></tr><tr><td>Revenue</td><td>6,150</td><td>5,650</td><td>5,900</td><td>5,649</td><td>5,626</td><td>4.4%</td><td>4.9%</td></tr><tr><td>QoQ</td><td>12.6%</td><td>3.4%</td><td>8.0%</td><td>5.0%</td><td>6.9%</td><td></td><td></td></tr><tr><td>YoY</td><td>29.7%</td><td>19.1%</td><td>32.6%</td><td>19.1%</td><td>18.6%</td><td></td><td></td></tr><tr><td>EPS - GAAP</td><td>$2.57</td><td>$2.23</td><td>$2.40</td><td>$2.14</td><td>$2.18</td><td>12.1%</td><td>10.0%</td></tr></table>

Source: Company data, GS Global Investment Research, Visible Alpha Consensus Data

Exhibit 3: TXN - New vs. old estimates

<table><tr><td rowspan="2">Financials ($mn, except EPS and FCF/Share)</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>GS</td><td>Old</td><td>Δ</td><td>GS</td><td>Old</td><td>Δ</td><td>GS</td><td>Old</td><td>Δ</td></tr><tr><td>Revenue</td><td>22,167</td><td>21,277</td><td>+4.2%</td><td>25,068</td><td>23,638</td><td>+6.0%</td><td>26,344</td><td>25,000</td><td>+5.4%</td></tr><tr><td>YoY</td><td>25.4%</td><td></td><td></td><td>13.1%</td><td></td><td></td><td>5.1%</td><td></td><td></td></tr><tr><td>Gross Margin</td><td>60.9%</td><td>59.0%</td><td>+192 bps</td><td>61.8%</td><td>59.8%</td><td>+202 bps</td><td>61.4%</td><td>60.5%</td><td>+83 bps</td></tr><tr><td>Operating Income</td><td>9,409</td><td>8,544</td><td>+10.1%</td><td>10,964</td><td>9,730</td><td>+12.7%</td><td>11,234</td><td>10,439</td><td>+7.6%</td></tr><tr><td>EPS - GAAP</td><td>$8.60</td><td>$7.75</td><td>+11.0%</td><td>$10.20</td><td>$9.20</td><td>+11.0%</td><td>$10.50</td><td>$10.00</td><td>+5.0%</td></tr><tr><td>FCF/Share</td><td>$8.19</td><td>$7.82</td><td>+4.8%</td><td>$10.06</td><td>$10.30</td><td>-2.3%</td><td>$11.18</td><td>$11.59</td><td>-3.6%</td></tr></table>

Source: Company data, GS Global Investment Research

Exhibit 4: Price target

<table><tr><td colspan="5">PRICE TARGET AND RISK/REWARD SUMMARY</td></tr><tr><td>Method</td><td>Metric</td><td>Base</td><td>Bull</td><td>Bear</td></tr><tr><td rowspan="4">P/E Method</td><td>Normalized EPS Estimate</td><td>$9.00</td><td>$9.90</td><td>$7.65</td></tr><tr><td>Multiple</td><td>25.0x</td><td>30.0x</td><td>22.0x</td></tr><tr><td>Valuation</td><td>$225.00</td><td>$297.00</td><td>$168.00</td></tr><tr><td>Upside/Downside</td><td>-21.1%</td><td>4.2%</td><td>-41.1%</td></tr><tr><td rowspan="4">Price Target</td><td>12-Month Price Target</td><td>$225.00</td><td></td><td></td></tr><tr><td>Potential Upside/Downside</td><td>-21.1%</td><td colspan="2">100% P/E</td></tr><tr><td>Dividend Yield at Current Price</td><td>0.5%</td><td></td><td></td></tr><tr><td>Potential Total Return</td><td>-20.6%</td><td></td><td></td></tr></table>

Source: GS Global Investment Research

<table><tr><td>TXN</td><td colspan="2">12m Price Target: $225.00</td><td colspan="2">Price: $294.19</td><td colspan="2">Downside: 23.5%</td></tr><tr><td colspan="2">Sell</td><td colspan="5">GS Forecast</td></tr><tr><td colspan="2"></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td rowspan="11" colspan="2">Market cap: $267.1bnEnterprise value: $273.4bn3m ADTV: $2.7bnUnited StatesAmericas Semiconductors &amp; IT ServicesM&amp;A Rank: 3</td><td>Revenue ($ mn) New</td><td>17,682.0</td><td>22,167.2</td><td>25,068.3</td><td>26,343.7</td></tr><tr><td>Revenue ($ mn) Old</td><td>17,682.0</td><td>21,276.7</td><td>23,638.3</td><td>24,999.7</td></tr><tr><td>EBITDA ($ mn)</td><td>7,941.0</td><td>11,651.5</td><td>13,512.0</td><td>14,101.7</td></tr><tr><td>EBIT ($ mn)</td><td>6,023.0</td><td>9,338.5</td><td>10,884.0</td><td>11,153.7</td></tr><tr><td>EPS ($) New</td><td>5.45</td><td>8.60</td><td>10.20</td><td>10.50</td></tr><tr><td>EPS ($) Old</td><td>5.45</td><td>7.75</td><td>9.20</td><td>10.00</td></tr><tr><td>P/E (X)</td><td>33.6</td><td>34.2</td><td>28.8</td><td>28.0</td></tr><tr><td>Dividend yield (%)</td><td>3.0</td><td>2.0</td><td>2.1</td><td>2.2</td></tr><tr><td>Net debt/EBITDA (X)</td><td>1.2</td><td>0.5</td><td>0.3</td><td>0.2</td></tr><tr><td></td><td>6/26</td><td>9/26E</td><td>12/26E</td><td>3/27E</td></tr><tr><td>EPS ($)</td><td>2.14</td><td>2.51</td><td>2.27</td><td>2.36</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 22 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, James Schneider, Ph.D., Khalil Fenina, Anmol Makkar and Luya You, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: James Schneider, Ph.D. GS & Co. LLC, Khalil Fenina GS & Co. LLC, Anmol Makkar GS & Co. LLC, Luya You GS & Co. LLC.

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

## Rating and pricing information

Analog Devices Inc. (Buy, \$386.73), Microchip Technology Inc. (Buy, \$85.02), NXP Semiconductors NV (Buy, \$278.80), and Onsemi (Neutral, \$92.33).

## Financial advisory disclosure

GS and/or one of its affiliates is acting as a financial advisor in connection with an announced strategic matter involving the following company or one of its affiliates: Texas Instruments Incorporated

Advanced Micro Devices Inc., Amkor Technology Inc., Analog Devices Inc., Applied Materials Inc., Broadcom Inc., Cadence Design Systems Inc., Camtek, Cognizant Technology Solutions, Credo Technology Group, EPAM Systems Inc., Entegris Inc., GlobalFoundries Inc., Globant SA, Intel Corp., International Business Machines Corp., KLA Corp., Lam Research Corp., MKS Instruments Inc., Marvell Technology Inc., Microchip Technology Inc., Micron Technology Inc., NXP Semiconductors NV, Nvidia Corp., ON Semiconductor Corp., Qnity, Qualcomm Inc., SanDisk Corp., Seagate Technology, SiTime Corp., Synopsys Inc., TaskUs Inc., Teradyne Inc., Texas Instruments Inc., Western Digital Corp.

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS has received compensation for investment banking services in the past 12 months: Texas Instruments Inc. (\$294.19)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Texas Instruments Inc. (\$294.19)

GS has received compensation for non-investment banking services during t

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
