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
# Japan Machinery: Automation: Robot/Robodrill May 2026 volume trends

The Ministry of Finance announced May 2026 trade data (customs data) during morning trading on June 26. We use this data as an indicator of volume trends for Fanuc's (Sell) robots and Robodrill No. 30 vertical machining centers, and Yaskawa Electric's (Buy, on CL) robots. Japanese companies have a large share of the global robot market and high domestic production ratios. Since Japan accounts for the majority of global robot production, we believe export volume trends from Japan to the rest of the world can be viewed as an indicator of investment in robots and automation, mainly in the auto and electronics industries. In this note, we outline our views on the robot industry and casing demand trends inferred from this month's data.

Yuichiro Isayama  
+81(3)4587-9806 |  
yuichiro.isayama@gs.com  
GS Japan Co., Ltd.

Takeru Adachi  
+81(3)4587-4067 |  
takeru.adachi@gs.com  
GS Japan Co., Ltd.

Takato Enoki  
+81(3)4587-1739 |  
takato.enoki@gs.com  
GS Japan Co., Ltd.

Chie Hu  
+81(3)4587-6330 | chie.hu@gs.com  
GS Japan Co., Ltd.

Exhibit 1: Robots: Trade statistics summary

<table><tr><td colspan="5">Robot: Japan</td></tr><tr><td></td><td>N. America</td><td>Europe</td><td>China</td><td>Global</td></tr><tr><td>Volume</td><td>1,720</td><td>1,497</td><td>5,390</td><td>10,828</td></tr><tr><td>yoy</td><td>3%</td><td>7%</td><td>6%</td><td>9%</td></tr><tr><td>mom</td><td>-17%</td><td>-25%</td><td>-13%</td><td>-24%</td></tr><tr><td>Value (¥mn)</td><td>4,966</td><td>4,334</td><td>8,541</td><td>21,550</td></tr><tr><td>yoy</td><td>-18%</td><td>-34%</td><td>9%</td><td>-8%</td></tr><tr><td>mom</td><td>-11%</td><td>-16%</td><td>-22%</td><td>-22%</td></tr><tr><td>ASP (¥mn)</td><td>2.89</td><td>2.90</td><td>1.58</td><td>1.99</td></tr><tr><td>yoy</td><td>-20%</td><td>-39%</td><td>3%</td><td>-16%</td></tr><tr><td>mom</td><td>7%</td><td>11%</td><td>-10%</td><td>3%</td></tr></table>

Exhibit 2: Robodrills: Trade statistics summary

<table><tr><td colspan="5">Robodrill: Japan</td></tr><tr><td></td><td>Asia</td><td>China</td><td>AeCJ</td><td>Global</td></tr><tr><td>Volume</td><td>1,134</td><td>559</td><td>575</td><td>1,204</td></tr><tr><td>yoy</td><td>-26%</td><td>-4%</td><td>-39%</td><td>-26%</td></tr><tr><td>mom</td><td>-28%</td><td>-33%</td><td>-22%</td><td>-27%</td></tr><tr><td>Value (¥mn)</td><td>8,480</td><td>4,649</td><td>3,832</td><td>9,619</td></tr><tr><td>yoy</td><td>-11%</td><td>16%</td><td>-31%</td><td>-18%</td></tr><tr><td>mom</td><td>-22%</td><td>-22%</td><td>-22%</td><td>-24%</td></tr><tr><td>ASP (¥mn)</td><td>7.48</td><td>8.32</td><td>6.66</td><td>7.99</td></tr><tr><td>yoy</td><td>20%</td><td>21%</td><td>14%</td><td>12%</td></tr><tr><td>mom</td><td>8%</td><td>16%</td><td>-1%</td><td>4%</td></tr></table>

<table><tr><td colspan="5">Robot: Fanuc (GSE)</td></tr><tr><td></td><td>N. America</td><td>Europe</td><td>China</td><td>Global</td></tr><tr><td>Volume</td><td>1,389</td><td>1,150</td><td>3,591</td><td>7,175</td></tr><tr><td>yoy</td><td>13%</td><td>27%</td><td>5%</td><td>18%</td></tr><tr><td>mom</td><td>-15%</td><td>-27%</td><td>-23%</td><td>-24%</td></tr><tr><td>Value (¥mn)</td><td>4,309</td><td>3,717</td><td>7,061</td><td>17,049</td></tr><tr><td>yoy</td><td>12%</td><td>53%</td><td>8%</td><td>22%</td></tr><tr><td>mom</td><td>-11%</td><td>-18%</td><td>-24%</td><td>-17%</td></tr><tr><td>ASP (¥mn)</td><td>3.10</td><td>3.23</td><td>1.97</td><td>2.38</td></tr><tr><td>yoy</td><td>-1%</td><td>21%</td><td>2%</td><td>4%</td></tr><tr><td>mom</td><td>5%</td><td>13%</td><td>-1%</td><td>9%</td></tr></table>

Source: Ministry of Finance, GS Global Investment Research

<table><tr><td colspan="5">Robodrill: Fanuc (GSE)</td></tr><tr><td></td><td>Asia</td><td>China</td><td>AeCJ</td><td>Global</td></tr><tr><td>Volume</td><td>797</td><td>376</td><td>421</td><td>801</td></tr><tr><td>yoy</td><td>-35%</td><td>-27%</td><td>-41%</td><td>-35%</td></tr><tr><td>mom</td><td>-31%</td><td>-39%</td><td>-20%</td><td>-30%</td></tr><tr><td>Value (¥mn)</td><td>5,066</td><td>2,714</td><td>2,352</td><td>5,083</td></tr><tr><td>yoy</td><td>-25%</td><td>-7%</td><td>-38%</td><td>-25%</td></tr><tr><td>mom</td><td>-25%</td><td>-30%</td><td>-19%</td><td>-26%</td></tr><tr><td>ASP (¥mn)</td><td>6.36</td><td>7.22</td><td>5.59</td><td>6.35</td></tr><tr><td>yoy</td><td>16%</td><td>27%</td><td>5%</td><td>15%</td></tr><tr><td>mom</td><td>7%</td><td>16%</td><td>1%</td><td>7%</td></tr></table>

Source: Ministry of Finance, GS Global Investment Research

## Robot export volume (Fanuc, Yaskawa Electric, and Japan total)

Fanuc: We estimate that Fanuc robots made at its Yamanashi main plant and its Tsukuba plant account for the bulk of exports from Tokyo/Yokohama. Mom momentum for export volume to China was -14% in April and -23% in May, suggesting that exports have not seen the strong continued growth observed in machine tools and some other FA equipment. We believe that companies with relative strength in small 6-axis or SCARA robots are benefiting more from AI-related demand in China. Exports to North America, where yoy momentum turned negative in April, saw yoy momentum rebound to +8% in May, but momentum appears to be losing steam, partly due to a high prior-year hurdle.

Yaskawa Electric (global exports from Moji in May: 347 units, -54% yoy/-73% mom): Yaskawa Electric is the only major robot maker with a production base in Kyushu, and we therefore believe its robots account for the majority of export volume from the port of Moji. Exports to South Korea totaled 74 units (-80% mom) and exports to China totaled 60 units (-51% mom), both declining, which we believe is a sign that OEM-related projects are starting to wind down. Exports to India, which saw a sharp increase in April, fell in May (-86% mom).

Exhibit 3: Fanuc: Robot shipment value by destination (GSe)  
![](images/694f4a9c3419fdd8ed1b92e2d296a990e41be822c87ab46247b6482bd78bab49.jpg)  
Source: Ministry of Finance, GS Global Investment Research

Exhibit 4: Japan: Robot shipment value by destination  
![](images/46500ba1986ab5f8b089115a74090ebf93c62c9c505c8f164c1c7f8b029967b8.jpg)  
Source: Ministry of Finance, Data compiled by GS Global Investment Research

Exhibit 5: Fanuc: Robot export volume to China and average export price (GSe)  
![](images/8f6fd630479af680f0970076e69c54584ce3b81528383826cd79780d39aa52fd.jpg)  
Source: Ministry of Finance, GS Global Investment Research

Exhibit 6: Fanuc: Robot export volume to North America and average export price (GSe)  
![](images/43c10d86efe7fbf201a8b84329360571b9fc3c95d0d8947089e2f92c8652db0a.jpg)  
Source: Ministry of Finance, GS Global Investment Research

Vertical machining center export volume from Tokyo/Yokohama (assumes Fanuc accounts for the majority of export volume)

Fanuc: We estimate that Robodrills made at Fanuc's Tsukuba plant account for the bulk of the No. 30 vertical machining centers exported to Asia from Tokyo/Yokohama customs. Of these, 376 units were shipped to mainland China (-27% yoy/-39% mom). Exports to India totaled 173 units (-67% yoy/-30% mom), and exports to Vietnam totaled 26 units (-78% yoy/-30% mom), with the sense of having peaked continuing. While we will need to monitor trends going forward, we believe that smartphone-related demand has remained limited in CY26.

Exhibit 7: Fanuc: Breakdown of Robodrill export volume by region (GSe)  
![](images/4315dc70eb3294c99070e0a9f51e0415a48afdcb0195442e936707cbbed0eb25.jpg)  
Source: Ministry of Finance, GS Global Investment Research

Exhibit 8: Fanuc: Robodrill export volume to China and average export price (GSe)  
![](images/b63b0f4ee823e266a11fe1c532d912bdff1be168122f7b405ca5c2b35a313c26.jpg)  
Source: Ministry of Finance, GS Global Investment Research

## Price Target Risks and Methodology - Fanuc (6954.T)

Our 12-month target price of ¥5,600 is based on FY3/28E EV/EBITDA, applying the sector-average multiple of 10X and a 70% sector-relative premium.

Key upside risks include sales in the FA business recovering to levels above past peaks, greater-than-expected improvement in robot business margins, and share buybacks or other moves to strengthen shareholder returns.

## Price Target Risks and Methodology - Yaskawa Electric (6506.T)

Our 12-month target price of ¥9,200 is based on FY2/28E EV/EBITDA, applying the sector-average multiple of 10X and a 90% sector-relative premium.

Key downside risks include (1) a slowdown in semiconductor and AI Capex related business, (2) slower-than-expected results from cost optimization measures, and (3) disappointment in the capital policy and growth strategy in the next medium-term plan and long-term vision.

## Disclosure Appendix

## Reg AC

We, Yuichiro Isayama, Takeru Adachi, Takato Enoki and Chie Hu, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Yuichiro Isayama GS Japan Co., Ltd., Takeru Adachi GS Japan Co., Ltd., Takato Enoki GS Japan Co., Ltd., Chie Hu GS Japan Co., Ltd..

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

The rating(s) for Fanuc and Yaskawa Electric is/are relative to the other companies in its/their coverage universe: AeroEdge, CKD, Daifuku, Daikin Industries, Fanuc, Harmonic Drive Systems, Hoshizaki, IHI, Japan Steel Works, Kawasaki Heavy Industries, Keyence, Makita, Misumi Group, Mitsubishi Heavy Industries, Okuma, Omron, SKY Perfect JSAT Corp, SMC, THK, Yaskawa Electric

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned 1% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the month end preceding this report: Yaskawa Electric (¥6,824)

GS had a non-securities services client relationship during the past 12 months with: Yaskawa Electric (¥6,824)

There are no company-specific disclosures for: Fanuc (¥7,030)

Distribution of ratings/investment banking relationships GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

Price target and rating history chart(s)  
![](images/efb5607b4b7d9cdc494e1a7ac249b767aa0b7b0a7dcece95b58712c03f122724.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/7c00afb937a80de75c12196c6d2986f4898ad97d51ec7b5527d4587f596a736b.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s)

## Fanuc (6954.T)

Yaskawa Electric (6506.T)

<table><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td></tr><tr><td>28-May-26</td><td>5,600</td><td>7,984</td><td>28-May-26</td><td>9,200</td><td>7,136</td></tr><tr><td>26-Apr-26</td><td>5,300</td><td>6,256</td><td>29-Apr-26</td><td>7,300</td><td>5,381</td></tr><tr><td>14-Jan-26</td><td>5,000</td><td>6,935</td><td>10-Apr-26<

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
