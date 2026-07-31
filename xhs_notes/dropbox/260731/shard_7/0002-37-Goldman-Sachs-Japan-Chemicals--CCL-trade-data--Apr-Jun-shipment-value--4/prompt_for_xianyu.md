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
# Japan Chemicals: CCL trade data: Apr–Jun shipment value +41% yoy, positive read-across for Mitsubishi Gas Chemical, Mitsui Kinzoku, others

According to Japan's Ministry of Finance trade statistics for June 2026, shipment volume of CCL (copper-clad laminates) on a volume basis increased $+15\%$ yoy, and shipment value rose $+46\%$ yoy. Demand thus remained very strong on a value basis. Total shipment value for the Apr-Jun 2026 quarter reached $+41\%$ yoy and $+12\%$ qoq, which we view as broadly positive for related companies such as Mitsubishi Gas Chemical and Resonac, as well as Mitsui Kinzoku and Nitto Boseki (all Buy-rated).

We assume that data are tracking at a favorable pace relative to guidance (full-year sales growth of +15% for BT materials) at Mitsubishi Gas Chemical, which has the top global market share in BT materials for semiconductor package substrates, and the 1H shipment volume outlook (+20% yoy) for MicroThin™ at Mitsui Kinzoku, which holds a large share in ultra-thin copper foil.

We assume this is driven by the larger size and higher layer counts of package substrates for AI servers (such as NVIDIA's next-generation Rubin GPUs) and strong demand for LPDDR and e-SSDs. We reaffirm our view that CCL price hikes will gain momentum from 2H, and we reiterate our Buy ratings on related companies, including Mitsui Kinzoku, where progress is being made with price increases, and Nitto Boseki, which has a strong presence in T-glass cloth, for which supply/demand is tight.

In June 2026, CCL shipment volume was +15% yoy/+15% mom, and shipment value was +46% yoy/+16% mom, both strong levels. Shipment value for the Apr-Jun 2026 quarter reached ¥32.7 bn, expanding considerably by +41% compared to the same period last year (¥23.2 bn). Even compared to the ¥29.3 bn in the previous quarter (Jan-Mar 2026), this represented +12% qoq growth. Furthermore, we think the resilience of global CCL demand can be further confirmed, considering shipments from Thailand are also likely increasing after Mitsubishi Gas Chemical brought its new Thailand plant online in December 2025 (+50% in total capacity).

Atsushi Ikeda
+81(3)4587-9940 |
atsushi.ikeda@gs.com
GS Japan Co., Ltd.

Yuri Izumikawa  
+81(3)4587-3643 |  
yuri.x.izumikawa@gs.com  
GS Japan Co., Ltd.

Exhibit 1: Monthly trends in CCL export volume and value  
![](images/3c29cf64c2a050107688f04cdf6d5ffe5150d42d49839aba8a82c335fce9d4f7.jpg)  
Source: Ministry of Finance, Bloomberg

## Price Target Risks and Methodology - Mitsubishi Gas Chemical

We are Buy rated on Mitsubishi Gas Chemical with a 12-month target price of ¥6,890. Our target price is based on the materials sector EV/GCI and FY3/28E CROCI/WACC correlation (sector cash-return multiple of 0.75X plus a 5% premium to the sector average).

Key risks: Stiffer competition in smartphone lens specialty resins and semiconductor package substrate materials, yen appreciation, and price declines for methanol and other market-sensitive products.

## Price Target Risks and Methodology - Resonac

We are Buy rated on Resonac with a 12-month target price of ¥23,920. Our target price is based on the correlation between the materials sector's EV/GCI and the FY12/27E CROCI/WACC (cash-return multiple of 0.7X plus a 30% premium to the sector average). Key risks include a slowdown in semiconductor demand, yen appreciation, and decline in graphite electrode earnings.

## Price Target Risks and Methodology - Mitsui Kinzoku

We are Buy rated on Mitsui Kinzoku with a 12-month target price of ¥62,600. Our target price is based on the correlation between the materials sector's EV/GCI and our FY3/28E CROCI/WACC forecast (cash return multiple of 0.7X plus a 60% premium to the sector average). Key risks include slowdown in AI server demand, yen appreciation, and decline in prices for zinc and other metals.

## Price Target Risks and Methodology - Nitto Boseki

We are Buy rated on Nitto Boseki with a 12-month target price of ¥4,820. Our target price is based on the correlation between the materials sector's EV/GCI and the FY3/28E CROCI/WACC forecast (cash-return multiple of 0.7x plus a 60% premium to the sector average). Key risks include fluctuations in semiconductor demand, currency volatility, and changes in the competitive landscape for specialty glass.

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

## Financial advisory disclosure

GS and/or one of its affiliates is acting as a financial advisor in connection with an announced strategic matter involving the following company or one of its affiliates: RESONAC HOLDINGS CORPORATION

The rating(s) for Mitsubishi Gas Chemical, Mitsui Kinzoku Co., Nitto Boseki Co and Resonac Holdings is/are relative to the other companies in its/their coverage universe: Asahi Kasei, Daicel, Denka, Fujimi Inc., JX Advanced Metals Corp., Kuraray, Mitsubishi Gas Chemical, Mitsui Chemicals Inc., Mitsui Kinzoku Co., Nippon Paint Holdings, Nitto Boseki Co, Resonac Holdings, SUMCO, Shin-Etsu Chemical, Tokyo Ohka Kogyo, Toray Industries, Tri Chemical Laboratories Inc., Zeon

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned 1% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the month end preceding this report: Mitsubishi Gas Chemical (¥3,820), Mitsui Kinzoku Co. (¥25,665), Nitto Boseki Co (¥2,622) and Resonac Holdings (¥12,245)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Mitsubishi Gas Chemical (¥3,820) and Resonac Holdings (¥12,245)

GS had an investment banking services client relationship during the past 12 months with: Mitsubishi Gas Chemical (¥3,820) and Resonac Holdings (¥12,245)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: Resonac Holdings (¥12,245)

GS had a non-securities services client relationship during the past 12 months with: Mitsui Kinzoku Co. (¥25,665) and Resonac Holdings (¥12,245)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td colspan="3">Rating Distribution</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>50%</td><td>34%</td><td>16%</td></tr></table>

<table><tr><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See 'Ratings, Coverage universe and related definitions' below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/6bbeb5666e90b6b0eca906f2d863b44b96b9e062c929f8af86b0319f6a77df6c.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/f4f380af48e8c728e2b76f3c2a855af1145ced38bbacd69418edae6ea4fc2adc.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/f11978c046e3d3275431fb87505c0bfed91032f6ce391072f8b328eb344e0342.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/3204c9edfb9b265937e4a6142903558d42a586b06dc6cb8b4188b5a9a9f8272d.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s)

## Mitsubishi Gas Chemical (4182.T)

<table><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td></tr><tr><td>05-Jun-26</td><td>6,890</td><td>5,180</td></tr><tr><td>01-Mar-26</td><td>5,930</td><td>4,364</td></tr><tr><td>21-Nov-25</td><td>3,040</td><td>2,537</td></tr><tr><td>10-Oct-25</td><td>3,460</td><td>2,706</td></tr><tr><td>06-Jun-25</td><td>3,040</td><td>2,181</td></tr><tr><td>13-Feb-25</td><td>3,490</td><td>2,724</td></tr><tr><td>13-Nov-24</td><td>3,640</td><td>2,795</td></tr><tr><td>28-Aug-24</td><td>3,570</td><td>2,687</td></tr><tr><td>17-May-24</td><td>3,540</td><td>3,020</td></tr><tr><td>10-Apr-24</td><td>3,160</td><td>2,752</td></tr><tr><td>09-Feb-24</td><td>2,890</td><td>2,316</td></tr><tr><td>23-Nov-23</td><td>2,760</td><td>2,264</td></tr><tr><td>19-Oct-23</td><td>2,460</td><td>2,018</td></tr></table>

## Resonac Holdings (4004.T)

<table><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td></tr><tr><td>05-Jun-26</td><td>23,920</td><td>17,315</td></tr><tr><td>01-Mar-26</td><td>15,770</td><td>11,930</td></tr><tr><td>12-Jan-26</td><td>8,050</td><td>6,810</td></tr></table>

<table><tr><td colspan="3">Mitsui Kinzoku Co. (5706.T)</td><td colspan="3">Nitto Boseki Co (3110.T)</td></tr><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td></tr><tr><td>05-Jun-26</td><td>62,600</td><td>44,490</td><td>06-Jul-26</td><td>4,820</td><td>3,515</td></tr><tr><td>01-Mar-26</td><td>44,100</td><td>36,910</td><td>05-Jun-26</td><td>23,800</td><td>4,050</td></tr><tr><td>12-Jan-26</td><td>24,000</td><td>19,900</td><td>01-Mar-26</td><td>27,770</td><td>5,040</td></tr><tr><td></td><td></td><td></td><td>12-Jan-26</td><td>10,840</td><td>2,508</td></tr></table>

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required unde

[中间内容因长度限制已省略]

including individuals from other parts of GS, do not

necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
