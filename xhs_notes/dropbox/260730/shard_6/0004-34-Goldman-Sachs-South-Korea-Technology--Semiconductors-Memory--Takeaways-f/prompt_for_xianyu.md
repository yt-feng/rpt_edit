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
# South Korea Technology: Semiconductors - Memory: Takeaways from Korea memory expert call

We hosted a Korea Memory Expert Webinar on July 28. Key takeaways include: 1) DRAM pricing to continue solid growth throughout this year, significant upside for HBM next year, 2) LTA to provide strong binding power, 3) Chinese memory suppliers limited threat in the near-to-mid term, 4) Stronger capacity addition however limited bit growth, and 5) Expects more of a gradual adoption of hybrid bonding. We reiterate our Buy rating on SEC.

DRAM pricing to continue solid growth throughout this year, significant upside for HBM next year: The expert expects conventional DRAM pricing could see solid double-digit% sequential growth in 3Q26 which is in line with recent strong spot pricing rally. The expert also sees possibility of another double-digit% sequential growth in 4Q26 on the back of ongoing supply shortage. For next year HBM pricing, the expert sees the possibility that pricing could potentially double due to rising conventional DRAM pricing. We expect SEC HBM pricing to rise $87\%$ yoy next year which is above sell-side consensus (Bloomberg) estimate of $52\%$ yoy.

LTA to provide strong binding power: The expert mentioned that LTA includes various terms to enhance binding power such as sizable prepayment, take-or-pay clause, and cancellation penalty. The expert also mentioned more than half of server DRAM is covered by LTA and expects LTA coverage ratio to increase going forward.

Chinese memory suppliers limited threat in the near-to-mid term: The expert mentioned that although Chinese suppliers are active in capacity expansion, expects less likelihood of Chinese suppliers to be a visible threat to leading players as there's still a sizable gap in production yield, technology level, and product reliability.

■ Stronger capacity addition however limited bit growth: The expert expects the capacity addition pace for this year to be stronger than its historical level, however expects bit growth to be below historical average due to the high HBM trade ratio.

■ Expects more of a gradual adoption of hybrid bonding: While the expert believes the existing HBM bonding technology will see increasing difficulty as the number of DRAM die stacks increases, at the same time does not expect an early adoption of hybrid bonding as the expert believes securing good enough yield on

Giuni Lee  
+82(2)3788-1177 | giuni.lee@gs.com  
GS (Asia) L.L.C., Seoul Branch

Taeyong Lee
+82(2)3788-0981 | taeyong.lee@gs.com
GS (Asia) L.L.C., Seoul Branch

Daiki Takayama
+81(3)4587-9870 |
daiki.takayama@gs.com
GS Japan Co., Ltd.

a mass production scale to take a considerable amount of time and effort. The expert believes memory companies will seek various options such as fluxless bonding along with aiming for a gradual adoption of hybrid bonding.

## Price Target Risks and Methodology - Samsung Electronics

Valuation methodology: Our 12m 2026-2027E EV/EBITDA-based SOTP target price for the common share is W480,000. Our 12-month target price for the preference share is W360,000, which is based on our target pref to common shares discount of 25%, derived from averaging: 1) the pref discount of the 2-factor model and 2) the average preference share discount to common shares during the past 1 month. We are Buy rated on both the common and preference shares.

Key downside risks: 1) major deterioration in memory supply/demand, 2) sharp contraction in smartphone margins, and 3) mobile OLED market share loss.

## Investment Thesis - Samsung Electronics

Samsung Electronics (SEC) is one of the largest tech companies in the world, with the #1 market share in several products including memory chips, OLED panels, smartphones, and TVs. We expect the strong earnings power led by memory to continue, supported by our expectation of solid memory pricing continuing and also remaining at an elevated level. We expect this to be helped by the long-term agreements (LTA) with customers, with a higher level of binding commitment likely this time compared to the past. The company is starting to show meaningful progress in HBM, and also considering the higher scope for meaningful shareholder returns, we remain constructive on the name and reiterate our Buy rating.

## Disclosure Appendix

## Reg AC

We, Giuni Lee, Taeyong Lee and Daiki Takayama, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Giuni Lee GS (Asia) L.L.C., Seoul Branch, Taeyong Lee GS (Asia) L.L.C., Seoul Branch, Daiki Takayama GS Japan Co., Ltd..

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

The rating(s) for Samsung Electronics and Samsung Electronics (Pref) is/are relative to the other companies in its/their coverage universe: Hansol Chemical, LG Display, LG Electronics, LG Innotek Co., SK Hynix Inc., SKC, Samsung Electro-Mechanics, Samsung Electronics, Samsung Electronics (Pref)

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS has received compensation for investment banking services in the past 12 months: Samsung Electronics (W208,500) and Samsung Electronics (Pref) (W153,400)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Samsung Electronics (W208,500) and Samsung Electronics (Pref) (W153,400)

GS had an investment banking services client relationship during the past 12 months with: Samsung Electronics (W208,500) and Samsung Electronics (Pref) (W153,400)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: Samsung Electronics (W208,500) and Samsung Electronics (Pref) (W153,400)

GS had a non-securities services client relationship during the past 12 months with: Samsung Electronics (W208,500) and Samsung Electronics (Pref) (W153,400)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/164952161363c58fc9c747292e07c5205bc27c95801e204c6c1820c865961955.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/868648e54ca5137e5a3d4be53ba1508485b5f38ee3201014c25cd8f0991f5dde.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s)

## Samsung Electronics (005930.KS)

Samsung Electronics (Pref) (005935.KS)

<table><tr><td>Date of report</td><td>Target price (W)</td><td>Closing price (W)</td><td>Date of report</td><td>Target price (W)</td><td>Closing price (W)</td></tr><tr><td>31-May-26</td><td>360,000</td><td>202,500</td><td>31-May-26</td><td>480,000</td><td>317,000</td></tr><tr><td>30-Apr-26</td><td>245,000</td><td>158,300</td><td>30-Apr-26</td><td>320,000</td><td>220,500</td></tr><tr><td>07-Apr-26</td><td>220,000</td><td>130,900</td><td>07-Apr-26</td><td>285,000</td><td>196,500</td></tr><tr><td>11-Mar-26</td><td>200,000</td><td>138,900</td><td>11-Mar-26</td><td>260,000</td><td>190,000</td></tr><tr><td>29-Jan-26</td><td>159,000</td><td>115,600</td><td>29-Jan-26</td><td>205,000</td><td>160,700</td></tr><tr><td>08-Jan-26</td><td>142,000</td><td>101,900</td><td>08-Jan-26</td><td>180,000</td><td>138,800</td></tr><tr><td>16-Dec-25</td><td>110,000</td><td>79,800</td><td>16-Dec-25</td><td>140,000</td><td>102,800</td></tr><tr><td>30-Oct-25</td><td>99,000</td><td>82,500</td><td>30-Oct-25</td><td>123,000</td><td>104,100</td></tr><tr><td>14-Oct-25</td><td>89,000</td><td>72,300</td><td>14-Oct-25</td><td>109,000</td><td>91,600</td></tr><tr><td>22-Sep-25</td><td>78,000</td><td>66,700</td><td>22-Sep-25</td><td>96,000</td><td>83,500</td></tr><tr><td>31-Jul-25</td><td>69,000</td><td>57,600</td><td>31-Jul-25</td><td>84,000</td><td>71,400</td></tr><tr><td>01-May-25</td><td>61,000</td><td>46,850</td><td>01-May-25</td><td>74,000</td><td>55,500</td></tr><tr><td>01-Apr-25</td><td>64,000</td><td>47,700</td><td>01-Apr-25</td><td>77,000</td><td>58,800</td></tr><tr><td>02-Feb-25</td><td>59,000</td><td>43,000</td><td>02-Feb-25</td><td>72,000</td><td>52,400</td></tr><tr><td>08-Jan-25</td><td>60,000</td><td>46,800</td><td>08-Jan-25</td><td>73,000</td><td>57,300</td></tr><tr><td>16-Dec-24</td><td>63,000</td><td>46,550</td><td>16-Dec-24</td><td>75,000</td><td>55,600</td></tr><tr><td>31-Oct-24</td><td>68,000</td><td>47,950</td><td>31-Oct-24</td><td>82,000</td><td>59,200</td></tr><tr><td>08-Oct-24</td><td>71,000</td><td>49,900</td><td>08-Oct-24</td><td>86,000</td><td>60,300</td></tr><tr><td>23-Sep-24</td><td>78,000</td><td>52,400</td><td>23-Sep-24</td><td>95,000</td><td>62,600</td></tr><tr><td>31-Jul-24</td><td>88,000</td><td>64,900</td><td>31-Jul-24</td><td>110,000</td><td>83,900</td></tr><tr><td>05-Jul-24</td><td>87,000</td><td>68,000</td><td>05-Jul-24</td><td>108,000</td><td>87,100</td></tr><tr><td>05-Apr-24</td><td>85,000</td><td>69,000</td><td>01-Jul-24</td><td>105,000</td><td>81,800</td></tr><tr><td>21-Mar-24</td><td>81,000</td><td>65,800</td><td>30-Apr-24</td><td>103,000</td><td>77,500</td></tr><tr><td>17-Dec-23</td><td>77,000</td><td>59,300</td><td>05-Apr-24</td><td>102,000</td><td>84,500</td></tr><tr><td>31-Oct-23</td><td>75,000</td><td>53,600</td><td>21-Mar-24</td><td>97,000</td><td>79,300</td></tr><tr><td>20-Sep-23</td><td>76,000</td><td>56,100</td><td>17-Dec-23</td><td>95,000</td><td>73,300</td></tr><tr><td></td><td></td><td></td><td>20-Sep-23</td><td>93,000</td><td>69,600</td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a

principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA

[中间内容因长度限制已省略]

including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global

Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
