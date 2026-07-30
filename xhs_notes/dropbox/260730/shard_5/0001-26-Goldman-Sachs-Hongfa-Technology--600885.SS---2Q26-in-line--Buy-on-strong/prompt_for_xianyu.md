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
## Hongfa Technology (600885.SS): 2Q26 in line; Buy on strong order visibility backed by market share gains and pricing power to support

Post market close on July 29, Hongfa announced 2Q26 results that were in line with our expectations. 2Q26 revenue/gross profit/operating profit/net profit reached Rmb5,914mn/1,963mn/1,007mn/672mn, +36%/+30%/+26%/+21% yoy, and +4%/+3%/+6%/+1% vs. GSe. 2Q26 GPM/OPM/NPM were 33%/17%/11%, -1pp/-1pp/-1pp yoy, all in line with GSe. We slightly adjust our 2026-30E EPS by <1% with 12-m TP now at Rmb45.5.

Jacqueline Du
+852-2978-1783 |
jacqueline.du@gs.com
GS (Asia) L.L.C.

We remain Buy rated on Hongfa, expecting the company to deliver 27% yoy revenue growth in 2026E, driven partially by its strong pricing power to pass through raw material price increases (with 10pp+ revenue growth contribution from price hikes), as well as strong volume growth across its end markets. This represents a significant acceleration versus its historical revenue CAGR of 15% over the past ten years. Volume growth should outperform underlying industry growth (such as in home appliances and autos), reflecting a structural acceleration in market share gains. Smaller players have been increasingly pressured by raw material price hikes and weaker operating cash flow, while global competitors such as Omron have announced the spin-off of its Device & Module Solutions Business (including relays, switches and sensors), recognizing intensifying global competition (link). With strong demand visibility into 2027E, we believe Hongfa should be well positioned to capture incremental demand, supported by its historical ability to increase production shifts and raise utilization rates towards 100%+ when demand is strong.

We also expect GPM to recover from $33.2\%$ in 2Q26 to $34.5\%$ in 3Q26E and $35.1\%$ in 4Q26E, as raw material prices stabilize and Hongfa completes its price hikes. We see limited risk of price reductions even if raw material prices pull back, given the current supply shortage environment. More importantly, strong revenue growth and higher utilization rates should provide meaningful operating leverage and support further GPM recovery.

HVDC relay: We expect 2026E revenue to grow 30% yoy, driven by continued market share gains through expanded global customer coverage across Europe and Southeast Asia, as well as higher content value from increasing penetration of 800V EV platforms.

General relay: We expect 2026E revenue to grow 36% yoy, driven by both price increases and market share gains against smaller players whose operations have been disrupted by raw material price increases, while also supported by strong ESS

demand.

Auto relay: We expect 2026E revenue to grow 16% yoy, as pricing increases were successfully implemented in 2Q26.

Power relay: We expect 2026E revenue to grow 24% yoy, driven by improving demand in Europe and higher State Grid-related smart meter installation volume.

Industrial control relay: We expect 2026E revenue to grow 29% yoy, driven by sustained demand from new energy, semiconductors, domestic substitution and overseas recovery, supported by improving OEM demand from customers such as Schneider.

Signal relay: We expect 2026E revenue to grow 20% yoy, supported by strong order visibility.

AIDC applications: The company completed sample deliveries by 2Q26 and expects to establish a clearer commercialization plan by 4Q26-2027E. In addition to HVDC relays and general relays, Hongfa is also exploring potential opportunities in connectors, film capacitors, vacuum capacitors and cabinets for data centers in the US and Southeast Asia.

Exhibit 1: Hongfa 2Q26 financial summary

<table><tr><td>Hongfa Technology (600885.SS)</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26</td><td>yoy %</td><td>qoq %</td><td>Prior 2Q26E GSe</td><td>Diff %</td></tr><tr><td>Revenue (Rmb mn)</td><td>3,983</td><td>4,364</td><td>4,567</td><td>4,288</td><td>5,108</td><td>5,914</td><td>36%</td><td>16%</td><td>5,674</td><td>4%</td></tr><tr><td colspan="11">Segment breakdown</td></tr><tr><td>Gross profit (Rmb mn)</td><td>1,345</td><td>1,513</td><td>1,615</td><td>1,432</td><td>1,639</td><td>1,963</td><td>30%</td><td>20%</td><td>1,906</td><td>3%</td></tr><tr><td>EBIT (Rmb mn)</td><td>605</td><td>798</td><td>764</td><td>388</td><td>751</td><td>1,007</td><td>26%</td><td>34%</td><td>947</td><td>6%</td></tr><tr><td>Net profit (Rmb mn)</td><td>411</td><td>553</td><td>506</td><td>288</td><td>484</td><td>672</td><td>21%</td><td>39%</td><td>663</td><td>1%</td></tr><tr><td>EPS (Rmb)</td><td>0.39</td><td>0.38</td><td>0.35</td><td>0.19</td><td>0.31</td><td>0.43</td><td>15%</td><td>39%</td><td>0.43</td><td>1%</td></tr><tr><td>Gross profit margin (%)</td><td>34%</td><td>35%</td><td>35%</td><td>33%</td><td>32%</td><td>33%</td><td>-1pp</td><td>1pp</td><td>34%</td><td>0pp</td></tr><tr><td>EBIT margin (%)</td><td>15%</td><td>18%</td><td>17%</td><td>9%</td><td>15%</td><td>17%</td><td>-1pp</td><td>2pp</td><td>17%</td><td>0pp</td></tr><tr><td>Net profit margin (%)</td><td>10%</td><td>13%</td><td>11%</td><td>7%</td><td>9%</td><td>11%</td><td>-1pp</td><td>2pp</td><td>12%</td><td>0pp</td></tr></table>

Source: Company data, GS Global Investment Research

The author would like to thank Zhou Li, Hao Chen, Zhihan Ye, and Junfang Zhang for their contributions to this report.

## Investment thesis, Valuation methodology and Risks

Hongfa is a top relay producer with $27\%$ global market share as of 2025 (No.1). We expect continued market share gains driven by technology strength in the autos (both ICE and EV)/home appliance/power/signal sectors, and by rising adoption of high-voltage DC architectures in AIDC and ESS applications. We believe the vehicle electrification mega-trend is poised to power China's industrial component champions as content per vehicle rises significantly in EV vs. ICE, while Hongfa's leading position in HVDC relays positions it to benefit from the 800V DC transition in both automotive and power infrastructure. In addition to strong smart meter demand as the global power grid enters a replacement cycle to incorporate more renewable energy generation and adapt for rising electricity demand, we now also see AIDC and ESS build-out adding incremental relay demand from data centers and backup/storage systems. We view the stock's valuation as attractive vs. our China Industrial Tech coverage, with potential catalysts coming from: (1) strong customer penetration among global EV OEM customers, (2) fast smart meter order gains against replacement demand, and (3) an acceleration in AIDC-related HVDC and general relay orders, as well as ESS-HVDC deployments, as global data center and power operators upgrade toward higher-efficiency DC and storage-rich architectures. We are Buy rated.

## Price Target Risks and Methodology - Hongfa Technology

Target price: Our 12m target price of Rmb45.5 is based on 2028E P/E of 24x discounted back to 2027E.

Downside risks: (1) Weaker-than-expected smart meter revenue recognition; (2) Weaker-than-expected revenue from front-loaded solar inverter revenue; (3) Further increase in copper and silver prices that negatively impacts GPM.

<table><tr><td>600885.SS</td><td>12m Price Target: Rmb45.50</td><td colspan="2">Price: Rmb33.98</td><td colspan="2">Upside: 33.9%</td></tr><tr><td>Buy</td><td colspan="5">GS Forecast</td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td rowspan="11">Market cap: Rmb52.6bn / $7.8bn Enterprise value: Rmb55.8bn / $8.3bn 3m ADTV: Rmb762.2mn / $112.3mn China China Industrial Tech &amp; Machinery M&amp;A Rank: 3 Leases incl. in net debt &amp; EV?: No</td><td>Revenue (Rmb mn) New</td><td>17,202.5</td><td>21,827.2</td><td>25,432.1</td><td>28,196.5</td></tr><tr><td>Revenue (Rmb mn) Old</td><td>17,202.5</td><td>21,647.8</td><td>25,191.0</td><td>27,925.3</td></tr><tr><td>EBITDA (Rmb mn)</td><td>3,653.8</td><td>4,430.6</td><td>5,160.9</td><td>6,162.9</td></tr><tr><td>EPS (Rmb) New</td><td>1.14</td><td>1.42</td><td>1.74</td><td>2.09</td></tr><tr><td>EPS (Rmb) Old</td><td>1.14</td><td>1.41</td><td>1.72</td><td>2.07</td></tr><tr><td>P/E (X)</td><td>22.5</td><td>24.0</td><td>19.5</td><td>16.2</td></tr><tr><td>P/B (X)</td><td>3.1</td><td>3.7</td><td>3.3</td><td>2.9</td></tr><tr><td>Dividend yield (%)</td><td>1.4</td><td>1.5</td><td>1.8</td><td>2.2</td></tr><tr><td>CROCI (%)</td><td>18.6</td><td>16.4</td><td>17.2</td><td>18.0</td></tr><tr><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td>EPS (Rmb)</td><td>0.31</td><td>0.43</td><td>0.41</td><td>0.26</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 29 Jul 2026 close.

## Disclosure Appendix

## Reg AC

I, Jacqueline Du, hereby certify that all of the views expressed in this report accurately reflect my personal views about the subject company or companies and its or their securities. I also certify that no part of my compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Jacqueline Du GS (Asia) L.L.C..

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

The rating(s) for Hongfa Technology is/are relative to the other companies in its/their coverage universe: AVIC Jonhon, Best, Bochu, CRRC Corp. (A), CRRC Corp. (H), Centre Testing Intl Group, Estun Automation Co.(A), Estun Automation Co.(H), Faratronic, Haitian International Holdings, Han's Laser Technology, HangKe Technology, Hongfa Technology, Huaming, Kehua Data Co., Lead Intelligent (A), Lead Intelligent (H), Leader Harmonious Drive Systems Co., Luster LightTech Co., Megmeet, Moons' Electric, NARI Technology, Nantong Jianghai Capacitor Co., OPT Machine Vision Tech Co., Sanhua Intelligent Controls (A), Sanhua Intelligent Controls (H), Shanghai Baosight Software, Shenzhen Envicool Technology, Shenzhen Inovance Technology Co., Shenzhen Kstar Science & Tech, Shuanghuan Driveline, Sieyuan Electric, Techtronic Industries, Wuhan Raycus Fiber Laser Tech, Yiheda Automation, Yingliu, Zhejiang Supcon Technology Co., Zhuzhou CRRC Times Electric Co. (A), Zhuzhou CRRC Times Electric Co. (H)

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned 1% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the month end preceding this report: Hongfa Technology (Rmb33.98)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See 'Ratings, Coverage universe and related definitions' below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/f81c3a852133a133ccc779e0b27b9c8bd9914688c87df84d44f786baee8397e7.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s) Hongfa Technology (600885.SS)

Date of report Target price (Rmb) Closing price (Rmb)

<table><tr><td>22-Jul-26</td><td>45.00</td><td>33.33</td></tr><tr><td>30-Apr-26</td><td>37.20</td><td>31.14</td></tr><tr><td>03-Apr-26</td><td>35.30</td><td>25.57</td></tr><tr><td>24-Feb-26</td><td>35.40</td><td>30.93</td></tr><tr><td>12-Jan-26</td><td>36.40</td><td>31.36</td></tr><tr><td>03-Nov-25</td><td>30.80</td><td>30.77</td></tr><tr><td>06-Aug-25</t

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
