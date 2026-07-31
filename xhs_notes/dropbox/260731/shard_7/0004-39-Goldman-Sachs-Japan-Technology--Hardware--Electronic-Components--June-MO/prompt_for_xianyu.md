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
# Japan Technology: Hardware - Electronic Components: June MOF trade statistics (MLCC): ASP/volume up mom suggests further tightening

According to Ministry of Finance (MOF) trade statistics for June, announced on July 30, the average export price for MLCCs was up +4% mom, while export volume was up +6%, and export value was up +11%. On a yoy basis, these figures were +23%/+6%/+31%. According to our industry supply chain checks, there is a possibility that supply/demand tightness strengthened further in June, and we believe these figures align with this view. Amid an ongoing strong demand outlook for AI/DC applications, supply concerns are growing for other applications as well, and we believe customers generally may be rushing to procure for 2026 and increasing their requests for 2027 LTAs.

We maintain our Buy ratings on Murata Mfg. (on CL), Taiyo Yuden, and TDK. Murata Mfg., TDK, and Taiyo Yuden are scheduled to announce 1Q results on July 31 (14:00), July 31 (15:30), and August 5 (15:30), respectively. Although share prices of MLCC stocks are currently in a correction phase, we believe fundamentals have actually strengthened further over the past month. At the upcoming results, we will be focusing on (1) BB ratio (potential for further qoq increase in Apr-Jun), (2) pricing strategy (whether there are any new moves or signs from Japanese manufacturers, which have kept prices flat, amid increasing activity by Asian companies), and (3) capacity utilization and supply capabilities.

Daiki Takayama
+81(3)4587-9870 |
daiki.takayama@gs.com
GS Japan Co., Ltd.

Mitsuhiro Icho
+81(3)4587-9836 |
mitsuhiro.x.icho@gs.com
GS Japan Co., Ltd.

Makoto Takahara
+81(3)4587-4270 |
makoto.takahara@gs.com
GS Japan Co., Ltd.

Yuji Hidaka
+81(3)4587-3656 | yuji.hidaka@gs.com
GS Japan Co., Ltd.

Exhibit 1: MLCC export volume and average export price (ASP)  
![](images/75feffa364ce745a73ebd67d7491008108d9883db821ff00e9fd944d24eb7cbb.jpg)  
Source: Ministry of Finance

## Price target risks and methodology

## Price Target Risks and Methodology - Murata Mfg.

Valuation methodology: We are Buy-rated on Murata Mfg. with a 12-month price target of ¥12,600. Our target price is based on FY3/29E EV/GCI vs. CROCI/WACC, applying an 80% premium to our sector multiple of 10X (implies FY3/29E P/E of 30X).

Key risks: Decline in smartphone production volume, deterioration in MLCC supply/demand, and yen appreciation.

## Price Target Risks and Methodology - Taiyo Yuden

Valuation methodology: We are Buy-rated on Taiyo Yuden with a 12-month price target of ¥21,200. Our target price is based on FY3/29E EV/GCI vs. CROCI/WACC, applying an 80% premium to our sector multiple of 10X (our TP implies FY3/29E P/E of 31X).

Key risks: Weaker-than-expected smartphone demand, deterioration in MLCC supply/demand, and yen appreciation.

## Price Target Risks and Methodology - TDK

Valuation methodology: We are Buy-rated on TDK with a 12-month price target of ¥4,600. Our target price is based on FY3/29E EV/GCI vs. CROCI/WACC, applying a 10% premium to our sector average EV/DACF multiple of 10X (implies FY3/28E P/E of 31X).

Key risks: Decline in smartphone production volume, higher input costs, and yen appreciation.

## Disclosure Appendix

## Reg AC

We, Daiki Takayama, Mitsuhiro Icho, Makoto Takahara and Yuji Hidaka, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Daiki Takayama GS Japan Co., Ltd., Mitsuhiro Icho GS Japan Co., Ltd., Makoto Takahara GS Japan Co., Ltd., Yuji Hidaka GS Japan Co., Ltd..

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

The rating(s) for Murata Mfg., TDK and Taiyo Yuden is/are relative to the other companies in its/their coverage universe: Alps Alpine, Dai Nippon Printing, Hirose Electric, IRISO Electronics, Ibiden, Japan Aviation Electronics Industry, Kohoku Kogyo, Kyocera, MARUWA, Mabuchi Motor, Maxell Ltd., MinebeaMitsumi Inc., Murata Mfg., NGK Corp., Nichicon, Nidec, Nippon Ceramic, Niterra, Nitto Denko, Renesas Electronics, Rohm, TDK, TOPPAN Holdings, Taiyo Yuden

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned 1% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the month end preceding this report: Taiyo Yuden (¥9,005)

GS has received compensation for investment banking services in the past 12 months: Murata Mfg. (¥6,231), TDK (¥2,746) and TDK (ADR) (\$45.24)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Murata Mfg. (¥6,231), Taiyo Yuden (¥9,005), TDK (¥2,746) and TDK (ADR) (\$45.24)

GS has received compensation for non-investment banking services during the past 12 months: Murata Mfg. (¥6,231)

GS had an investment banking services client relationship during the past 12 months with: Murata Mfg. (¥6,231), Taiyo Yuden (¥9,005), TDK (¥2,746) and TDK (ADR) (\$45.24)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: Murata Mfg. (¥6,231), TDK (¥2,746) and TDK (ADR) (\$45.24)

GS had a non-securities services client relationship during the past 12 months with: TDK (¥2,746) and TDK (ADR) (\$45.24)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/66ac020bd28a20f24d9a025e311f8a9fad4c872b349300d0728815ca365237e5.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/088b7be4bdf89b7768c69d1835e899fa852681c219fd7a35fe3300e95dd2336a.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/a6ca85dc3632be833603a5cd6f23261ab1d7f5f3ae64cbfef4cbc35359646f66.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s)

Taiyo Yuden (6976.T)  
Murata Mfg. (6981.T)

<table><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td></tr><tr><td>08-Jun-26</td><td>21,200</td><td>14,975</td><td>08-Jun-26</td><td>12,600</td><td>8,711</td></tr><tr><td>08-May-26</td><td>7,100</td><td>6,663</td><td>30-Apr-26</td><td>5,400</td><td>5,156</td></tr><tr><td>23-Mar-26</td><td>4,900</td><td>3,926</td><td>23-Mar-26</td><td>4,200</td><td>3,508</td></tr><tr><td>12-Jan-26</td><td>4,300</td><td>3,405</td><td>12-Jan-26</td><td>3,900</td><td>3,194</td></tr><tr><td>02-Oct-25</td><td>3,800</td><td>3,382</td><td>31-Oct-25</td><td>3,600</td><td>3,392</td></tr><tr><td>05-Aug-25</td><td>3,200</td><td>2,841</td><td>02-Oct-25</td><td>3,300</td><td>2,770</td></tr><tr><td>07-Jul-25</td><td>3,100</td><td>2,488</td><td>30-Apr-25</td><td>3,000</td><td>2,214</td></tr><tr><td>09-May-25</td><td>3,200</td><td>2,202</td><td>31-Mar-25</td><td>3,400</td><td>2,306</td></tr><tr><td>31-Mar-25</td><td>3,400</td><td>2,467</td><td>01-Oct-24</td><td>3,500</td><td>2,893</td></tr><tr><td>07-Nov-24</td><td>3,600</td><td>2,781</td><td>02-Jul-24</td><td>3,800</td><td>3,364</td></tr><tr><td>01-Oct-24</td><td>4,100</td><td>3,081</td><td>03-Apr-24</td><td>3,400</td><td>2,768</td></tr><tr><td>02-Jul-24</td><td>4,800</td><td>4,105</td><td>06-Dec-23</td><td>3,300</td><td>2,892</td></tr><tr><td>08-May-24</td><td>4,000</td><td>3,643</td><td>04-Oct-23</td><td>3,100</td><td>2,657</td></tr><tr><td colspan="3">Taiyo Yuden (6976.T)</td><td colspan="3">Murata Mfg. (6981.T)</td></tr><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td></tr><tr><td>07-Feb-24</td><td>4,100</td><td>3,431</td><td></td><td></td><td></td></tr><tr><td>06-Dec-23</td><td>4,500</td><td>3,627</td><td></td><td></td><td></td></tr><tr><td>07-Nov-23</td><td>4,400</td><td>3,695</td><td></td><td></td><td></td></tr><tr><td>04-Oct-23</td><td>4,800</td><td>3,963</td><td></td><td></td><td></td></tr><tr><td>03-Aug-23</td><td>4,900</td><td>4,164</td><td></td><td></td><td></td></tr></table>

## TDK (6762.T)

<table><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td></tr><tr><td>08-Jun-26</td><td>4,600</td><td>3,715</td></tr><tr><td>28-Apr-26</td><td>3,000</td><td>2,677</td></tr><tr><td>23-Mar-26</td><td>2,900</td><td>2,043</td></tr><tr><td>12-Jan-26</td><td>2,800</td><td>2,142</td></tr><tr><td>31-Oct-25</td><td>2,700</td><td>2,673</td></tr><tr><td>02-Oct-25</td><td>2,400</td><td>2,154</td></tr><tr><td>01-Aug-25</td><td>2,100</td><td>1,876</td></tr><tr><td>28-Apr-25</td><td>2,000</td><td>1,460</td></tr><tr><td>31-Mar-25</td><td>2,100</td><td>1,546</td></tr><tr><td>01-Nov-24</td><td>2,300</td><td>1,848</td></tr><tr><td>01-Oct-24</td><td>2,230</td><td>1,948</td></tr><tr><td>02-Sep-24</td><td>11,300</td><td>2,023</td></tr><tr><td>30-Jul-24</td><td>11,500</td><td>2,029</td></tr><tr><td>02-Jul-24</td><td>11,200</td><td>2,004</td></tr><tr><td>26-Apr-24</td><td>8,300</td><td>1,462</td></tr><tr><td>03-Apr-24</td><td>8,700</td><td>1,488</td></tr><tr><td>31-Jan-24</td><td>7,800</td><td>1,488</td></tr><tr><td>06-Dec-23</td><td>7,500</td><td>1,338</td></tr><tr><td>01-Nov-23</td><td>6,500</td><td>1,158</td></tr><tr><td>04-Oct-23</td><td>6,400</td><td>1,052</td></tr><tr><td>02-Aug-23</td><td>6,500</td><td>1,089</td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S

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
