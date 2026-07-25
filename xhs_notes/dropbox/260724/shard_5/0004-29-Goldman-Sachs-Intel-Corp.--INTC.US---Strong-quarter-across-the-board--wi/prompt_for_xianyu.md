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
# Intel Corp. (INTC): Strong quarter across the board, with margin upside and positive process technology commentary

Key stock takeaways: We expect the stock to trade higher following a strong quarter and guidance driven by upside in the Datacenter and Client segments, significantly higher gross margins, and positive commentary on supply agreements and CapEx. Given the proof points the company is seeing on 18A and 14A as well as increased customer demand signals, Intel is raising its 2026 CapEx to \$20bn, with a significant increase expected in 2027. We believe investors were constructively positioned heading into the quarter, driven by near-term strength in Server CPUs, sustained momentum in advanced packaging, and signs of progress on its advanced foundry nodes – and we think the company’s results and commentary cleared this elevated bar. We expect Intel to be a beneficiary of rising server demand (driven by agentic AI), and we see upside optionality from Intel’s role as a US champion with its foundry business – with near-term traction in advanced packaging, and longer-term potential in wafer outsourcing. However, we are Neutral rated on the stock as Intel’s closest peers (i.e. AMD, NVDA and AVGO) offer relatively more revenue visibility and favorable risk/reward in our view.

Quarterly results were well above the Street: Intel reported revenue of \$16.1 bn, well above GS at \$14.3 bn and the Street at \$14.4 bn. Gross margin of 41.8% was well above GS at 39.3% and the Street at 39.2%. Operating margin of 17.2% was well above GS at 11.5% and the Street at 11.2%. Reported non-GAAP operating EPS of \$0.42 was far above GS at \$0.23 and the Street at \$0.22. CCG revenue of \$8.9 bn was well above GS and the Street at \$8.0 bn. DCAI revenue of \$6.3 bn was well above GS at \$5.7 bn and the Street at \$5.6 bn. Intel Foundry revenue of \$5.8 bn was above GS at \$5.6 bn and the Street at \$5.5 bn.

\- Datacenter CPU strength: Intel's DCAI segment grew 24% QoQ and 59% YoY, driven by strength in general-purpose server demand as well as agentic AI. Going forward, Intel sees an accelerating server CPU market being driven by agentic AI with sustained unit strength and higher ASPs - with a strong double-digit growth CAGR through at least 2028. The company expects to see stronger sequential growth in DCAI for 4Q as additional supply comes on line, as the company continues to run in a capacity shortage position.

■ Increased CapEx Investment: Intel increased its CapEx guidance to over \$20 bn in 2026 (from \$17 bn prior), and now expects to increase CapEx significantly in 2027 and beyond given the ramp in its expected capacity in Advanced Packaging and in anticipation of its 14A process launch. Intel expects to increase its

James Schneider, Ph.D.
+1(212)357-2929 |
jim.schneider@gs.com
GS & Co. LLC

Anmol Makkar
+1(212)357-1366 |
anmol.makkar@gs.com
GS & Co. LLC

Luya You
+1(212)902-5297 | luya.you@gs.com
GS & Co. LLC

Khalil Fenina
+1(212)357-6392 |
khalil.fenina@gs.com
GS & Co. LLC

spending on WFE tooling by \~40% in 2026 given its recent outsized investment in fab shells and cleanroom space. Going forward, the company plans to invest in both front-end wafer and advanced packaging capacity given the strong customer demand signals it is seeing.

\- Process technology progress and roadmap: Intel continues to see a strong yield and production volume ramp for its 18A process technology across both server and client products, and is increasing production capacity to respond to increasing demand. The company entered risk production on its 18A-P in 2Q. Relative to 14A, Intel’s internal process metrics are running ahead of 18A at the same point – and the company plans to release its PDK 0.9 this October, with risk production in 2H27 and volume production in 2028.

3Q guidance is well above the Street. Intel guided 3Q revenue and gross margin well above the Street. Revenue was guided to \$16.3 bn at the midpoint, which is well above GS at \$14.7 bn and the Street at \$15.1 bn. Non-GAAP gross margin was guided to 42%, which is well above GS at 39.5% and the Street at 40.3%. Non-GAAP EPS was guided to \$0.38 which is above GS at \$0.24 and the Street at \$0.28.

Estimate changes. We increase our estimates by $49\%$ on average as we reflect significantly higher revenue and gross margin assumptions across the company's Datacenter and Client segments, with modest changes to our estimates for Intel Foundry (Exhibit 3).

Price target and risks: We are Neutral rated on INTC. Our unchanged 12-month target price of \$150 is based on 30X applied to our normalized EPS estimate of \$5.00. Key upside risks: (1) increased traction for Intel Foundry services; (2) better demand and share trends in server CPUs; (3) stronger margin improvement. Downside risks include: (1) slower than anticipated ramp of advanced foundry nodes; (2) lower server CPU share.

Exhibit 1: INTC - Variance summary

<table><tr><td rowspan="2">Financials ($ mn, except EPS)</td><td colspan="5">2Q26</td></tr><tr><td>Actual</td><td>GS</td><td>Street</td><td>Actual/GS</td><td>Actual/Street</td></tr><tr><td>CCG</td><td>8,877</td><td>7,959</td><td>7,975</td><td>11.5%</td><td>11.3%</td></tr><tr><td>DCAI</td><td>6,262</td><td>5,683</td><td>5,595</td><td>10.2%</td><td>11.9%</td></tr><tr><td>Intel Foundry</td><td>5,765</td><td>5,556</td><td>5,525</td><td>3.8%</td><td>4.3%</td></tr><tr><td>All Other</td><td>701</td><td>558</td><td>630</td><td>25.7%</td><td>11.3%</td></tr><tr><td>Total Revenue</td><td>16,128</td><td>14,299</td><td>14,435</td><td>12.8%</td><td>11.7%</td></tr><tr><td>QoQ</td><td>18.8%</td><td>5.3%</td><td>6.3%</td><td></td><td></td></tr><tr><td>YoY</td><td>25.4%</td><td>11.2%</td><td>12.3%</td><td></td><td></td></tr><tr><td>Gross Margin (excl. SBC)</td><td>41.8%</td><td>39.3%</td><td>39.2%</td><td>+254 bps</td><td>+258 bps</td></tr><tr><td>Operating Income (excl. SBC)</td><td>2770</td><td>1644</td><td>1,617</td><td>68.5%</td><td>71.3%</td></tr><tr><td>Operating Margin (%)</td><td>17.2%</td><td>11.5%</td><td>11.2%</td><td>+568 bps</td><td>+598 bps</td></tr><tr><td>EPS (excl. SBC)</td><td>$0.42</td><td>$0.23</td><td>$0.22</td><td>81.1%</td><td>88.2%</td></tr></table>

Source: Company data, GS Global Investment Research, Visible Alpha Consensus Data

Exhibit 2: INTC - Guidance

<table><tr><td rowspan="2">Financials ($ mn, except EPS)</td><td colspan="7">3Q26E</td></tr><tr><td>High</td><td>Low</td><td>Guidance (midpoint)</td><td>GS</td><td>Street</td><td>Guidance/GS</td><td>Guidance/Street</td></tr><tr><td>Total Revenue</td><td>16,800</td><td>15,800</td><td>16,300</td><td>14,708</td><td>15,118</td><td>10.8%</td><td>7.8%</td></tr><tr><td>QoQ</td><td></td><td></td><td>1.1%</td><td>2.9%</td><td>4.7%</td><td></td><td></td></tr><tr><td>YoY</td><td></td><td></td><td>28.7%</td><td>7.7%</td><td>10.7%</td><td></td><td></td></tr><tr><td>Gross margin (ex SBC)</td><td></td><td></td><td>42.0%</td><td>39.5%</td><td>40.3%</td><td>+253 bps</td><td>+169 bps</td></tr><tr><td>EPS (excl. SBC)</td><td></td><td></td><td>$0.38</td><td>$0.24</td><td>$0.28</td><td>60.5%</td><td>36.4%</td></tr></table>

Source: Company data, GS Global Investment Research

Exhibit 3: INTC - New vs Old Estimates

<table><tr><td rowspan="2">Financials ($mn, except EPS)</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>GS</td><td>Old</td><td>Δ</td><td>GS</td><td>Old</td><td>Δ</td><td>GS</td><td>Old</td><td>Δ</td></tr><tr><td>CCG</td><td>34,372</td><td>31,791</td><td>+8.1%</td><td>35,996</td><td>33,202</td><td>+8.4%</td><td>37,163</td><td>34,469</td><td>+7.8%</td></tr><tr><td>DCAI</td><td>26,453</td><td>23,508</td><td>+12.5%</td><td>37,254</td><td>29,899</td><td>+24.6%</td><td>48,883</td><td>37,518</td><td>+30.3%</td></tr><tr><td>Intel Foundry</td><td>23,699</td><td>22,759</td><td>+4.1%</td><td>32,421</td><td>29,912</td><td>+8.4%</td><td>47,280</td><td>44,884</td><td>+5.3%</td></tr><tr><td>All Other</td><td>2,795</td><td>2,351</td><td>+18.8%</td><td>2,967</td><td>2,390</td><td>+24.2%</td><td>3,063</td><td>2,509</td><td>+22.1%</td></tr><tr><td>Total Revenue</td><td>64,686</td><td>58,151</td><td>+11.2%</td><td>79,338</td><td>68,496</td><td>+15.8%</td><td>96,369</td><td>81,486</td><td>+18.3%</td></tr><tr><td>YoY</td><td>22.4%</td><td>10.0%</td><td>+1236 bps</td><td>22.7%</td><td>17.8%</td><td>+486 bps</td><td>21.5%</td><td>19.0%</td><td>+250 bps</td></tr><tr><td>Gross Margin (excl. SBC)</td><td>42.4%</td><td>40.0%</td><td>+239 bps</td><td>45.2%</td><td>43.4%</td><td>+182 bps</td><td>50.1%</td><td>50.0%</td><td>+14 bps</td></tr><tr><td>Operating Income (excl. SBC)</td><td>10,742</td><td>7,107</td><td>+51.1%</td><td>17,285</td><td>11,643</td><td>+48.5%</td><td>27,952</td><td>20,647</td><td>+35.4%</td></tr><tr><td>EPS (excl. SBC)</td><td>$1.65</td><td>$1.05</td><td>+56.4%</td><td>$2.70</td><td>$1.75</td><td>+54.1%</td><td>$4.60</td><td>$3.35</td><td>+37.4%</td></tr></table>

Source: GS Global Investment Research

Exhibit 4: Price target

<table><tr><td colspan="5">PRICE TARGET AND RISK/REWARD SUMMARY</td></tr><tr><td>Method</td><td>Metric</td><td>Base</td><td>Bull</td><td>Bear</td></tr><tr><td rowspan="5">P/E Method</td><td>Normalized EPS Estimate</td><td>$5.00</td><td>$6.50</td><td>$3.00</td></tr><tr><td>Multiple</td><td>30.0x</td><td>35.0x</td><td>15.0x</td></tr><tr><td>Valuation</td><td>$150.00</td><td>$228.00</td><td>$45.00</td></tr><tr><td>Calculated</td><td>$150.00</td><td>$227.50</td><td>$45.00</td></tr><tr><td>Upside/Downside</td><td>41.6%</td><td>115.3%</td><td>-57.5%</td></tr><tr><td rowspan="4">Price Target</td><td>12-Month Price Target</td><td>$150.00</td><td></td><td></td></tr><tr><td>Potential Upside/Downside</td><td>41.6%</td><td rowspan="3" colspan="2">100% P/E</td></tr><tr><td>Dividend Yield at Current Price</td><td>0.0%</td></tr><tr><td>Potential Total Return</td><td>41.6%</td></tr></table>

Source: GS Global Investment Research

12m Price Target: \$150.00

<table><tr><td>Neutral</td><td colspan="5">GS Forecast</td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Market cap: $511.6bn</td><td>Revenue ($ mn) New</td><td>52,853.0</td><td>64,685.6</td><td>79,337.9</td><td>96,368.5</td></tr><tr><td>Enterprise value: $535.5bn</td><td>Revenue ($ mn) Old</td><td>52,853.0</td><td>58,150.9</td><td>68,495.7</td><td>81,486.0</td></tr><tr><td>3m ADTV: $15.0bn</td><td>EBITDA ($ mn)</td><td>12,187.0</td><td>20,248.3</td><td>29,824.5</td><td>42,895.3</td></tr><tr><td>United States</td><td>EBIT ($ mn)</td><td>482.0</td><td>7,734.3</td><td>13,918.5</td><td>23,909.3</td></tr><tr><td rowspan="2">Americas Semiconductors &amp; IT Services</td><td>EPS ($) New</td><td>(0.09)</td><td>1.29</td><td>2.05</td><td>4.41</td></tr><tr><td>EPS ($) Old</td><td>(0.09)</td><td>0.69</td><td>1.12</td><td>3.04</td></tr><tr><td rowspan="3">M&amp;A Rank: 3</td><td>P/E (X)</td><td>NM</td><td>77.7</td><td>49.0</td><td>22.7</td></tr><tr><td>Dividend yield (%)</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Net debt/EBITDA (X)</td><td>0.8</td><td>1.2</td><td>0.6</td><td>(0.3)</td></tr><tr><td></td><td></td><td>6/26</td><td>9/26E</td><td>12/26E</td><td>3/27E</td></tr><tr><td></td><td>EPS ($)</td><td>0.30</td><td>0.33</td><td>0.31</td><td>0.33</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 23 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, James Schneider, Ph.D., Anmol Makkar, Luya You and Khalil Fenina, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: James Schneider, Ph.D. GS & Co. LLC, Anmol Makkar GS & Co. LLC, Luya You GS & Co. LLC, Khalil Fenina GS & Co. LLC.

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

The rating(s) for Intel Corp. is/are relative to the other companies in its/their coverage universe: ARM Holdings, Accenture Plc, Advanced Micro Devices Inc., Amkor Technology Inc., Analog Devices Inc., Applied Materials Inc., Broadcom Inc., Cadence Design Systems Inc., Camtek, Cognizant Technology Solutions, Credo Technology Group, EPAM Systems Inc., Entegris Inc., GlobalFoundries Inc., Globant SA, Intel Corp., International Business Machines Corp., KLA Corp., Lam Research Corp., MKS Instruments Inc., Marvell Technology

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
