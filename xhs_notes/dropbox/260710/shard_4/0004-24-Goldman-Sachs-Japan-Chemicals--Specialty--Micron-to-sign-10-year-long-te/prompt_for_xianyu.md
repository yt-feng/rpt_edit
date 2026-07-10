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
# Japan Chemicals: Specialty: Micron to sign 10-year long-term wafer agreement with GlobalWafers; positive for two Japanese wafer makers

On July 9 (EDT), Micron Technology (covered by our US technology & semiconductor analyst James Schneider) announced a plan to invest up to US\$3 bn to strengthen the US semiconductor supply chain ecosystem and realize the critical semiconductor manufacturing footprint necessary for future technological innovation (release). As part of this, the company will provide GWC (GlobalWafers; Not Covered) with US\$500 mn in strategic financing support, as well as enter a 10-year long-term supply agreement (LTA) for silicon wafers and explore collaboration on next-generation wafer technologies. We summarize the potential implications for the silicon wafer industry, as well as for Shin-Etsu Chemical and SUMCO, below. In short, we see potentially positive implications for both Japanese companies. We reiterate our Buy ratings on the two stocks (see our earnings revisions report for semiconductor and electronic materials companies and our Asia Technology investment strategy report).

The surprises in this announcement are likely the possibility of the LTA starting earlier than expected and the 10-year contract period. We assume that many of the LTAs currently held by Shin-Etsu Chemical, SUMCO, and others are roughly 5- to 7-year agreements that generally run until the end of 2027 or the end of 2028, whereas this announcement by Micron Technology features a very long time horizon of 10 years. In particular, we think it is highly significant that this is being concluded with a player in the memory industry, which has historically been considered highly cyclical. In other words, this is likely evidence of visibility on future demand structurally increasing on the customer side and of growing concerns over future wafer supply/demand tightness and procurement. We reiterate our Buy ratings on Shin-Etsu Chemical and SUMCO.

According to the announcement, Micron Technology will provide strategic financing support of up to US\$500 mn (c.¥81 bn) to GWC. These funds will support the expansion of the 12-inch (300 mm) silicon wafer plant that GlobalWafers is constructing in Sherman, Texas, and the two companies simultaneously signed a 10-year LTA. With this, Micron Technology secures a stable supply of core materials for advanced memory. Micron Technology's management commented that securing a reliable supply of key inputs is essential to supporting the company's long-term growth and technology roadmap, demonstrating its commitment to securing key materials including silicon wafers. We presume this is driven by concerns over silicon wafer procurement within the industry.

During the Q&A session at its recent annual general meeting of shareholders,

Atsushi Ikeda  
+81(3)4587-9940 |  
atsushi.ikeda@gs.com  
GS Japan Co., Ltd.

Yuri Izumikawa  
+81(3)4587-3643 |  
yuri.x.izumikawa@gs.com  
GS Japan Co., Ltd.

Shin-Etsu Chemical also noted that demand for wafers for AI applications has expanded more rapidly than expected since May and June, and that a substantial number of customers are beginning to recognize that procurement of various semiconductor materials, including silicon wafers, could become tighter in 2027/2028. Supply and demand conditions for 300 mm wafers have rapidly tightened, and it appears that momentum is building toward the next round of LTAs.

On the other hand, we recognize that companies are becoming cautious about future investment plans, given the recent rapid rise in costs related to new silicon wafer investments, including greenfield investments, issues with construction schedules, and the recent challenging earnings for players other than Shin-Etsu Chemical (in its guidance, SUMCO expects an operating loss in 2Q12/26, as in 1Q). In fact, in a March 27, 2026 release, SUMCO just announced plans (link) to substantially revise its initial capacity expansion investments, including the construction of a new plant in Yoshinogari, Saga Prefecture (reducing it to around one-quarter of the initial plan). In light of these circumstances, we believe wafer companies will be forced to significantly raise their hurdle rates for new investments, and that substantial revisions (price hikes) will also be essential in the next LTAs. Furthermore, while the profitability of customer device makers is expanding significantly, attention will likely focus on the possibility that the magnitude of the price revisions in the next LTAs will exceed the previous two revisions, even taking into account their upcoming large-scale investments to increase production.

## Price Target Risks and Methodology - Shin-Etsu Chemical

We are Buy-rated on Shin-Etsu Chemical with a 12-month target price of ¥9,610. Our target price is based on the FY3/28-FY3/29 average correlation between the materials sector EV/GCI and CROCI/WACC estimates (using a cash return multiple of 0.7X and a 20% premium to the sector average).

Key risks: Deterioration in semiconductor supply/demand, and a negative earnings impact from swings in market prices for PVC and caustic soda, and in forex.

## Price Target Risks and Methodology - SUMCO

We are Buy-rated on SUMCO with a 12-month target price of ¥6,140. Our target price is based on the FY12/27-FY12/28 average correlation between the materials sector EV/GCI and CROCI/WACC estimate (using a cash return multiple of 0.7X).

Key risks: A slowdown in semiconductor demand, yen appreciation, and a greater-than-expected increase in depreciation and other fixed costs.

## Disclosure Appendix

## Reg AC

We, Atsushi Ikeda and Yuri Izumikawa, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Atsushi Ikeda GS Japan Co., Ltd., Yuri Izumikawa GS Japan Co., Ltd..

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

The rating(s) for SUMCO and Shin-Etsu Chemical is/are relative to the other companies in its/their coverage universe: Asahi Kasei, Daicel, Denka, Fujimi Inc., JX Advanced Metals Corp., Kuraray, Mitsubishi Gas Chemical, Mitsui Chemicals Inc., Mitsui Kinzoku Co., Nippon Paint Holdings, Nitto Boseki Co, Resonac Holdings, SUMCO, Shin-Etsu Chemical, Tokyo Ohka Kogyo, Toray Industries, Tri Chemical Laboratories Inc., Zeon

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned 1% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the month end preceding this report: SUMCO (¥4,544)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Shin-Etsu Chemical (¥7,010) and SUMCO (¥4,544)

GS had an investment banking services client relationship during the past 12 months with: Shin-Etsu Chemical (¥7,010) and SUMCO (¥4,544)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: Shin-Etsu Chemical (¥7,010) and SUMCO (¥4,544)

GS had a non-securities services client relationship during the past 12 months with: Shin-Etsu Chemical (¥7,010) and SUMCO (¥4,544)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/ddf9a217849283f6f067b090195437e9e0eacaa79eccd169de066953ee2f207f.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/30e8c0b64d89b07bfda53295a6e288bfbc515fd29dfe729cadbb7186e0e70583.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s)

SUMCO (3436.T)  
Shin-Etsu Chemical (4063.T)

<table><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td></tr><tr><td>06-Jul-26</td><td>6,140</td><td>5,171</td><td>06-Jul-26</td><td>9,610</td><td>7,415</td></tr><tr><td>05-Jun-26</td><td>5,130</td><td>4,041</td><td>05-Jun-26</td><td>9,520</td><td>7,350</td></tr><tr><td>01-Mar-26</td><td>1,910</td><td>1,828</td><td>01-May-26</td><td>8,300</td><td>7,104</td></tr><tr><td>21-Nov-25</td><td>1,600</td><td>1,175</td><td>01-Mar-26</td><td>7,240</td><td>6,168</td></tr><tr><td>10-Oct-25</td><td>2,060</td><td>1,658</td><td>28-Oct-25</td><td>6,000</td><td>4,672</td></tr><tr><td>17-Aug-25</td><td>1,370</td><td>1,201</td><td>10-Oct-25</td><td>6,380</td><td>5,020</td></tr><tr><td>08-May-25</td><td>1,270</td><td>994</td><td>28-Jul-25</td><td>5,900</td><td>4,480</td></tr><tr><td>30-Apr-25</td><td>1,440</td><td>984</td><td>30-Apr-25</td><td>6,200</td><td>4,330</td></tr><tr><td>09-Apr-25</td><td>1,630</td><td>779</td><td>17-Apr-25</td><td>5,960</td><td>3,861</td></tr><tr><td>17-Feb-25</td><td>1,740</td><td>1,114</td><td>30-Jan-25</td><td>6,390</td><td>4,900</td></tr><tr><td>10-Jan-25</td><td>1,890</td><td>1,155</td><td>30-Oct-24</td><td>6,830</td><td>5,680</td></tr><tr><td>18-Nov-24</td><td>2,140</td><td>1,270</td><td>02-Sep-24</td><td>6,900</td><td>6,400</td></tr><tr><td>23-Aug-24</td><td>2,500</td><td>1,807</td><td>04-Aug-24</td><td>7,100</td><td>5,921</td></tr><tr><td>30-Jul-24</td><td>2,900</td><td>2,465</td><td>01-May-24</td><td>7,000</td><td>6,074</td></tr><tr><td>25-Mar-24</td><td>3,000</td><td>2,425</td><td>25-Mar-24</td><td>7,600</td><td>6,750</td></tr><tr><td>26-Feb-24</td><td>2,700</td><td>2,374</td><td>30-Jan-24</td><td>6,700</td><td>5,822</td></tr><tr><td>31-Jan-24</td><td>2,440</td><td>2,256</td><td>22-Dec-23</td><td>6,440</td><td>5,781</td></tr><tr><td>19-Dec-23</td><td>2,490</td><td>2,186</td><td>03-Nov-23</td><td>5,640</td><td>4,806</td></tr><tr><td>28-Sep-23</td><td>2,210</td><td>1,945</td><td>28-Sep-23</td><td>5,320</td><td>4,319</td></tr><tr><td>06-Sep-23</td><td>2,230</td><td>1,998</td><td>31-Jul-23</td><td>5,480</td><td>4,679</td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid

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
