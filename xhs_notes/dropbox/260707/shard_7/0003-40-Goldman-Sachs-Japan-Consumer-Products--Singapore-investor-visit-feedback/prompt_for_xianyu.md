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
# Japan Consumer Products: Singapore investor visit feedback: Focus on Middle East impact, consumption tax cut, and inflation resilience

We visited Singapore on July 2-3, meeting with 13 institutional investors over the two days. Key topics discussed included the impact of the Middle East situation, the potential consumption tax cut in Japan, and inflation resilience largely through price hikes. In terms of individual stocks, there was strong interest in Ajinomoto, Japan Tobacco (JT), Kikkoman, Shiseido, Unicharm, Kao, Toyo Suisan, Nissin Foods Holdings, and Rohto Pharmaceutical. We highlight in particular Buy-rated Toyo Suisan (on low valuation of c.13X P/E, governance improvement, and growth expectations driven by the startup of a new plant), Shiseido (on potential for qoq improvement in Apr-Jun sales momentum), Unicharm (we expect negative catalysts to be mostly priced in if guidance is lowered at Apr-Jun results), and Rohto (we believe concerns over a possible Apr-Jun profit decline are already priced in). We summarize the key points below.

Middle East impact: Although crude oil futures prices have recently peaked out/declined, procurement has not recovered to levels seen before the Strait of Hormuz closure. Given that there is a certain time lag for spot prices to materialize in costs, we see a high likelihood that the cost of raw materials derived from crude oil/naphtha will peak in the second half of 2026. On the other hand, we assume that multiple companies (including Ajinomoto and Toyo Suisan) that have not yet incorporated higher costs from the Middle East situation into FY26 guidance have indirectly priced in cost concerns. Please refer to our related report.

■ Potential consumption tax cut: We believe that in the event of a tax cut, it would be difficult for food companies, which cannot determine retail prices, to implement a de facto price hike by keeping the price reduction smaller than the amount of the tax cut. However, given that Yamazaki Baking has a large number of SKUs, such as seasonal products and collaborative products with retailers, the company may be able to improve margins during a tax cut by adjusting the margin range of new SKUs. Please refer to our related report.

\- Foods: Regarding Kikkoman, which we upgraded to Buy in late March, the share buyback announced in April was smaller than we expected, but the stock has outperformed within the sector (share price performance in May-Jun was +17%, while the performance of the 11 food and beverage companies in our coverage was +2.9% over the same period), as the market viewed positively the recovery in North American soy sauce sales in Jan-Mar, which was in line with our

Takashi Miyazaki
+81(3)4587-9896 |
takashi.miyazaki@gs.com
GS Japan Co., Ltd.

Megumi Taniguchi
+81(3)4587-9877 |
megumi.taniguchi@gs.com
GS Japan Co., Ltd.

expectations, and management's stated intention to implement price hikes globally in response to cost inflation. While there were few negative views on Kikkoman for the medium to long term, some investors expressed concerns about the short-term trend after its outperformance, as the cost drag from the start of new plant operations may be heavy in 1H3/27. Investors also discussed Meiji Holdings, which appears to be relatively well regarded within the sector, and NH Foods, which announced guidance for a profit decline and held a CEO meeting in late June. On Ajinomoto, some investors expressed expectations for profit momentum in Apr-Jun, as the company saw very little in the way of higher costs stemming from the Middle East situation during the quarter.

\- Beverages/tobacco: On JT, we noted a mix of recognition for its inflation resilience and concerns that profit growth from Apr-Jun could weaken vs Jan-Mar. We expect JT to show inflation resilience over the medium term and deliver net profits (return to profitability) in Oct-Dec. Interest in the three beverage companies was somewhat muted compared to the past.

Cosmetics/toiletries: On Kao, there was high interest in the CEO meeting held in late June and semiconductor-related fields in the chemical business, but we did not get the impression that expectations were particularly rising. On Shiseido, investors acknowledged our view of a possible qoq improvement in Apr-Jun sales momentum, but some highlighted a lack of medium-term sales growth drivers. On Unicharm, we noted concerns about saturation in Southeast Asia (including China) and a lack of medium-term growth drivers.

## Price Target Risks and Methodology - Toyo Suisan Kaisha

Valuation methodology: We are Buy rated on Toyo Suisan. Our 12-month target price of ¥14,200 is based on FY3/27E-FY3/28E average EV/NOPAT of 17.5X, representing a 14% discount (+1SD vs historical 3-year average) to the sector average multiple of 20.7X.

Risks: Lower sales volume and lower ASP than we expect, lower productivity in instant noodles, and deterioration in the business environment in Mexico.

## Price Target Risks and Methodology - Shiseido

Our 12-month target price of ¥3,600 is based on a FY12/27E P/E of 26.5X (discount of -1SD to the past 10-year average). We are Buy rated on the stock. Downside risks include lower-than-expected sales growth, margin deterioration in China-related business, downside to our assumed restructuring benefits, and the recording of one-off expenses.

## Price Target Risks and Methodology - Unicharm

Our 12-month target price is ¥1,250. It is based on the FY12/27E P/E of 25X (-1SD to the past 10-year average). We are Buy rated on the stock. Key risks include slower overseas sales growth, loss of momentum in baby care and feminine care businesses, and higher raw material costs.

## Price Target Risks and Methodology - Rohto Pharmaceutical

Our 12-month target price of ¥2,950 is based on a FY3/28E P/E multiple of 18X (-1SD to past 10-year average). We are Buy rated on the stock. Risks include lower sales growth, higher market demand ratio for high-/medium-priced products, and time required to respond to regulatory changes in each region.

## Disclosure Appendix

## Reg AC

We, Takashi Miyazaki and Megumi Taniguchi, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Takashi Miyazaki GS Japan Co., Ltd., Megumi Taniguchi GS Japan Co., Ltd..

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

The rating(s) for ROHTO Pharmaceutical, Shiseido, Toyo Suisan Kaisha and Unicharm is/are relative to the other companies in its/their coverage universe: Ajinomoto, Calbee Inc, Japan Tobacco, Kao, Kikkoman, Kirin Holdings, Kose Holdings, Lion, Meiji Holdings, NH Foods Ltd., Nissin Foods Holdings, Pola Orbis Holdings, ROHTO Pharmaceutical, Shiseido, Suntory Beverage & Food Ltd., Toyo Suisan Kaisha, Unicharm, Yamazaki Baking

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned 1% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the second most recent month end: Shiseido (¥2,769) and Toyo Suisan Kaisha (¥10,535)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: ROHTO Pharmaceutical (¥2,406), Shiseido (¥2,769) and Unicharm (¥960)

GS had an investment banking services client relationship during the past 12 months with: ROHTO Pharmaceutical (¥2,406), Shiseido (¥2,769) and Unicharm (¥960)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: Shiseido (¥2,769)

GS had a non-securities services client relationship during the past 12 months with: ROHTO Pharmaceutical (¥2,406), Shiseido (¥2,769) and Unicharm (¥960)

Distribution of ratings/investment banking relationships
GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/896a32fc655e1a9a13a7ad30bf5ae58d947c2802a62747d672484103b9927abe.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/f8e28baf5f4d3d86f4678e5c81a6b1b2de4543aedd9b06aac25e52b270d01a6d.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/b54c5f77f9c0bfd3cbe9bbd48f1b3b1ac0c0e0b721cdaca259abb13d027dcf97.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/5c773a5052d737ab5cfde1b1aaff80221901106d0a284d5f48c81034390e2be9.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s)

Unicharm (8113.T)

<table><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td></tr><tr><td>02-Apr-26</td><td>1,250</td><td>954</td></tr><tr><td>03-Mar-26</td><td>1,300</td><td>964</td></tr><tr><td>18-Nov-25</td><td>1,250</td><td>924</td></tr><tr><td>05-Aug-25</td><td>1,350</td><td>1,034</td></tr><tr><td>09-May-25</td><td>1,500</td><td>1,294</td></tr><tr><td>11-Mar-25</td><td>1,550</td><td>1,209</td></tr><tr><td>13-Jan-25</td><td>1,750</td><td>1,224</td></tr><tr><td>13-Dec-24</td><td>5,600</td><td>1,304</td></tr><tr><td>08-Nov-24</td><td>6,300</td><td>1,572</td></tr><tr><td>29-Aug-24</td><td>6,500</td><td>1,698</td></tr><tr><td>06-Aug-24</td><td>6,200</td><td>1,679</td></tr><tr><td>11-Jul-24</td><td>6,300</td><td>1,758</td></tr><tr><td>09-Apr-24</td><td>6,100</td><td>1,543</td></tr></table>

ROHTO Pharmaceutical (4527.T)

## Shiseido (4911.T)

<table><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td></tr><tr><td>12-May-26</td><td>3,600</td><td>3,304</td></tr><tr><td>10-Feb-26</td><td>3,400</td><td>2,783</td></tr><tr><td>08-Jan-26</td><td>3,000</td><td>2,322</td></tr><tr><td>10-Dec-25</td><td>2,800</td><td>2,269</td></tr><tr><td>28-Aug-25</td><td>2,700</td><td>2,432</td></tr><tr><td>23-Apr-25</td><td>2,550</td><td>2,297</td></tr><tr><td>24-Mar-25</td><td>2,900</td><td>2,828</td></tr><tr><td>29-Nov-24</td><td>2,700</td><td>2,856</td></tr><tr><td>27-Nov-24</td><td>3,000</td><td>2,806</td></tr><tr><td>09-Sep-24</td><td>3,400</td><td>3,206</td></tr><tr><td>11-Jul-24</td><td>4,100</td><td>4,603</td></tr><tr><td>05-Jun-24</td><td>4,000</td><td>5,148</td></tr><tr><td>09-Apr-24</td><td>3,500</td><td>4,087</td></tr></table>

<table><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td></tr><tr><td>12-Feb-26</td><td>2,950</td><td>2,603</td></tr><tr><td>19-Sep-25</td><td>2,900</td><td>2,503</td></tr><tr><td>06-Aug-25</td><td>2,700</td><td>2,157</td></tr></table>

Toyo Suisan Kaisha (2875.T)

<table><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing

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
