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
# Yili Industrial (600887.SS): Youran Dairy positive profit alert- positive to Yili and signal for S/D rebalance; Ausnutria negative profit alert on

## What's new#1:

Youran Dairy (not covered) issued a positive profit alert on 28 July on a 1H26 net profit range of Rmb739-903mn, vs a -Rmb297mn net loss in 1H25. The turnaround was primarily driven by: i) a substantial reduction in biological asset fair-value losses, supported by a narrowing decline in raw milk prices (latest raw milk price at Rmb3.05/kg by Ministry of Agriculture, vs. Rmb3.02/kg in end-2025), continued recovery in cull cow prices, improved operating efficiency with lower feed costs and higher milk yield; and ii) continued improvement in core operating performance, with higher sales volume scale and lower feed costs, driving higher gross profit along with product upgrades and business structure optimization.

Implication to Yili - positive and earnings accretion: On a simple stake basis, the profit alert implies c.Rmb233-284mn associate income for Yili in 1H26, based on its 31.5% stake in Youran as of 29 June 2026, vs. an estimated c.-Rmb101mn associate loss in 1H25 (based on Yili's c.33.9% stake before its 1H25 results date), implying yoy uplift of c.Rmb333-385mn (mid point at Rmb359mn) in associate income in the PBT level; and already higher vs GSe of total associate income at Rmb168mn in 1H26. For 2H26, completed on June 30, 2026, Yili's subsidiary, Boyuan Investment, subscribed to 299,250,000 newly issued shares at a price of HK\$3.92 per share, which led to Yili's total stake in Youran to increase from 31.5% to 36.07% since 30 June 2026, which will lead to incremental associate income to Yili from Youran in 2H26.

GS view - Beyond earnings, another signal for S/D inflection: We view the profit alert as a positive read-across to Yili and China Dairy Industry. Youran's turnaround from loss making to profit making in 1H26, following Modern Dairy's recent positive profit alert (also turning losses into profits), provides further evidence that China's upstream S/D cycle is reaching an inflection point and rebalancing (see our China Dairy: Navigating S/D inflection in May). Both companies highlighted improving farming profitability driven by continued herd rationalization, narrowing decline of raw milk price or stabilizing raw milk price, lower feed costs and improving operating efficiency. While the sector remains in a recovery phase, improving profitability of upstream dairy operators should reduce earnings drag from Yili/Mengniu's upstream investment, driving easing competition/promotion environment in China Dairy industry, benefitting leaders with upstream resources, and ultimately benefit the broader dairy value chain over the medium term.

Leaf Liu  
+852-3966-4169 | leaf.liu@gs.com  
GS (Asia) L.L.C.

Christina Liu
+852-2978-6983 | christina.liu@gs.com
GS (Asia) L.L.C.

Valerie Zhou
+852-2978-0820 | valerie.zhou@gs.com
GS (Asia) L.L.C.

GS does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. For Reg AC certification and other important disclosures, see the Disclosure Appendix, or go to www.gs.com/research/hedge.html. Analysts employed by non-US affiliates are not registered/qualified as research analysts with FINRA in the U.S.

## What's new#2:

Ausnutria (not covered) announced 1H26 profit warning on 24 July, guiding for Rmb3.07bn-3.17bn revenue (mid point at Rmb3.12bn, down c.20% yoy) and -Rmb685-785 net loss (vs. Rmb181mn net profit in 1H25) due to a combination of phased adjustments and external environmental factors. Excluding a one-time inventory-related adjustment, non-cash asset impairments and other related impacts, Ausnutria expects to record a core net operating profit at Rmb155mn-255mn for 1H26 (mid point at c. Rmb205mn, largely steady yoy). We attended its pre-results briefing call with below takeaways: 1) 1H26 earnings were weighted by one-off items and industry headwinds, incl. inventory optimization, overseas geopolitical tensions which directly impact shipping and air freight costs, temporarily restricting supply capacity and hitting top-line revenues, and non-cash asset impairments. The company has been actively destocking with channel inventory down by over 40% and inventory days below 30 days, alongside ongoing SKUs streamlining and operating efficiency improvements. 2) The company will continue to aim for a slight full-year revenue growth and revenue at HSD% yoy growth/resuming to positive Net Profit in 2H26.

Implication to Yili -negative read-across to IMF segment: As Ausnutria is a subsidiary of Yili (Yili owns c. 60.2% controlling stake), the profit alert implies a negative NP (after MI) impact at c. Rmb521mn\~581mn (mid point at Rmb551mn) to Yili in 1H26. We also calculate Ausnutria sales as c. 22% Yili's "IMF and others" segment sales and 6% of Yili's total sales in both 1H26 and 2026 (i.e., a c.20% decline in Ausnutria sales would translate to c. 1.2% negative impact on Yili sales, and c.4% negative impact on Yili's "IMF and others" segment sales), while current GSe is at c. 6% yoy positive growth for Yili's "IMF and others" segment sales for 1H26 and 7% in 2H26. That said, we expect Yili's Pro-Kido main brand to continue to gain market share to support overall IMF segment growth.

GS View: Ausnutria's profit alert implies a negative NP impact at c. Rmb551mn (the mid point) to Yili in 1H26, vs. a positive yoy uplift of c.Rmb359mn (in the mid point) in associate income in the PBT level from Youran Dairy's positive profit alert. That said, Ausnutria's core OP remain largely steady in 1H26, and we expect a clean start in 2H26 for Ausnutria post its channel inventory streamlining. Overall, we expect the market to focus more on the positive read across from Youran Dairy to Yili.

The authors would like to thank Lily Qi for her contribution to this report.

## Price Target Risks and Methodology - Yili

Valuation methodology: Our 12-month Rmb37.0 TP is based on 2027E P/E of 18.9x (20% A/H premium to the target level of 1STD below prior downcycle P/E in 2015-16) discount back to mid-2027.

Key risks: 1) Slower-than-expected liquid milk premium demand; 2) A slower dairy demand recovery; 3) More intense competition.

<table><tr><td>600887.SS</td><td>12m Price Target: Rmb37.00</td><td>Price: Rmb26.58</td><td>Upside: 39.2%</td></tr></table>

<table><tr><td>Buy</td><td colspan="5">GS Forecast</td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Market cap:</td><td>Revenue (Rmb mn)</td><td>115,931.1</td><td>121,626.4</td><td>125,911.2</td><td>129,577.9</td></tr><tr><td>Rmb170.1bn / $25.1bn</td><td>EBITDA (Rmb mn)</td><td>16,083.2</td><td>17,404.8</td><td>18,562.0</td><td>19,806.0</td></tr><tr><td>Enterprise value:</td><td>EPS (Rmb)</td><td>1.74</td><td>1.86</td><td>2.03</td><td>2.26</td></tr><tr><td>Rmb192.3bn / $28.4bn</td><td>P/E (X)</td><td>16.2</td><td>14.3</td><td>13.1</td><td>11.7</td></tr><tr><td>3m ADTV: Rmb1.7bn / $251.5mn</td><td>P/B (X)</td><td>3.3</td><td>2.9</td><td>2.7</td><td>2.6</td></tr><tr><td>China Consumer Staples</td><td>Dividend yield (%)</td><td>4.9</td><td>5.3</td><td>5.8</td><td>6.4</td></tr><tr><td>M&amp;A Rank: 3</td><td>N debt/EBITDA (ex lease,X)</td><td>1.7</td><td>1.0</td><td>0.5</td><td>(0.1)</td></tr><tr><td>Leases incl. in net debt &amp; EV?:</td><td>CROCI (%)</td><td>18.9</td><td>17.2</td><td>18.6</td><td>20.1</td></tr><tr><td>Yes</td><td>FCF yield (%)</td><td>6.2</td><td>9.9</td><td>10.8</td><td>11.8</td></tr><tr><td></td><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td></td><td>EPS (Rmb)</td><td>0.84</td><td>0.39</td><td>0.50</td><td>0.12</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 28 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Leaf Liu, Christina Liu and Valerie Zhou, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Leaf Liu GS (Asia) L.L.C., Christina Liu GS (Asia) L.L.C., Valerie Zhou GS (Asia) L.L.C..

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

The rating(s) for Yili Industrial is/are relative to the other companies in its/their coverage universe: Anhui Gujing Distillery Co., Budweiser APAC, Busy Ming Group, China Feihe Ltd., China Resources Beer, China Resources Beverage, Chongqing Brewery, Eastroc Beverage (A), Foshan Haitian Flavouring & Food (A), Foshan Haitian Flavouring & Food (H), Fujian Wanchen Food, Jiangsu King's Luck Brewery, Jiangsu Yanghe, Jiugui Liquor, Jonjee Hi-Tech, Kweichow Moutai, Luzhou Laojiao, Mengniu Dairy, Nongfu Spring, Qianhe Condiment and Food, Shanghai Bairun, Shanxi Xinghuacun Fen Wine, Sichuan Swellfun Co., Sichuan Teway Food Group, Tingyi, Tsingtao Brewery (A), Tsingtao Brewery (H), Uni-President China, Wuliangye Yibin, Yihai International Holding, Yili Industrial, ZJLD

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Yili Industrial (Rmb26.58)

GS had an investment banking services client relationship during the past 12 months with: Yili Industrial (Rmb26.58)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/a42ed5c04253755686a7935a1eb1f4d408b2c8ef6231d103629c96508ef1f53e.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s) Yili Industrial (600887.SS)

<table><tr><td>Date of report</td><td>Target price (Rmb)</td><td>Closing price (Rmb)</td></tr><tr><td>10-Jul-26</td><td>37.00</td><td>24.88</td></tr><tr><td>30-Apr-26</td><td>35.00</td><td>27.46</td></tr><tr><td>08-Oct-25</td><td>33.90</td><td>-</td></tr><tr><td>29-Aug-25</td><td>34.50</td><td>28.57</td></tr><tr><td>14-Jul-25</td><td>33.10</td><td>27.49</td></tr><tr><td>01-May-25</td><td>33.40</td><td>29.76</td></tr><tr><td>16-Apr-25</td><td>32.30</td><td>29.70</td></tr><tr><td>16-Jan-25</td><td>31.90</td><td>28.33</td></tr><tr><td>31-Oct-24</td><td>31.30</td><td>27.91</td></tr><tr><td>10-Sep-24</td><td>30.30</td><td>21.95</td></tr><tr><td>01-Sep-24</td><td>29.70</td><td>22.63</td></tr><tr><td>19-Jul-24</td><td>30.50</td><td>26.40</td></tr><tr><td>12-May-24</td><td>32.50</td><td>27.95</td></tr><tr><td>02-May-24</td><td>34.20</td><td>28.61</td></tr><tr><td>15-Apr-24</td><td>34.80</td><td>27.04</td></tr><tr><td>31-Jan-24</td><td>35.10</td><td>27.09</td></tr><tr><td>06-Nov-23</td><td>36.00</td><td>27.55</td></tr><tr><td>10-Oct-23</td><td>34.00</td><td>26.79</td></tr><tr><td>06-Sep-23</td><td>35.00</td><td>26.19</td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosur

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
