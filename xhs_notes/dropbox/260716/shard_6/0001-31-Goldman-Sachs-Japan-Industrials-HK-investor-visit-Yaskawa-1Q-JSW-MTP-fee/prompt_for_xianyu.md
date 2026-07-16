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
# Japan Industrials: HK investor visit/Yaskawa 1Q/JSW MTP feedback; focus on execution and pricing

We visited investors in Hong Kong from July 6 to 9, and received extensive feedback following Yaskawa Electric's 1Q results announced after the July 10 close and the Japan Steel Works medium-term plan update briefing on July 13. We summarize the key takeaways below.

While many investors agreed with our bullish view on FA, we came away with the impression that interest in non-FA stocks has grown stronger than we had anticipated, perhaps reflecting a shift in broader market sentiment and a change in the degree of interest in AI. We are also receiving more questions than before about where we currently stand in the cycle. We intend to maintain our preference for the FA subsector through the rest of the year, particularly ahead of the September quarter earnings announcements, as we expect consensus estimates to continue to be revised upward during this period.

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

## HK investor visit feedback: FA: AI proxy stocks — focus shifts from supply/demand tightness to whether price hikes are materializing

Many investors recognize that this capex cycle is entering its peak phase, and are reassessing its sustainability, when the peak period will arrive, and what the next drivers will be. Some held a constructive view that the current cycle, driven by semiconductors and AI/data centers, should remain very strong through CY2027-2028, in line with the direction of WFE and semiconductor capex forecasts. On the other hand, given that machine tool and FA cycles have historically tended to move more sharply and lead the broader cycle on both the upside and downside, some investors see the cycle peaking by end-2026. In any case, expectations were high that supply/demand tightness is very pronounced and that its benefits will be confirmed this summer, with the majority view being that order trends and earnings trends at FA-related companies should come in at or above market expectations.

It is precisely for this reason that many investors agreed with our view — also discussed in our Taiwan research trip report (our report) — that the possibility of product price hikes in response to supply/demand tightness is likely to become a key focus going forward. Ultimately, this will come down to whether companies can demonstrate an early return to peak profit levels, sustain those levels, and signal the potential for further profit growth. We believe many investors also agreed with our view that electrical/electronic FA companies are more likely to achieve this. Since the earnings miss at Yaskawa Electric — which was driven by company-specific factors — did not provide a clear picture of pricing trends, attention will likely turn to Keyence’s earnings, scheduled to be disclosed after the July 28 close, for more detail on this front.

We assume that the FA cycle driven primarily by semiconductors is likely to remain sustainable through CY2027-2028, but that order trends in areas closer to “general industry” will peak out in CY2026 (FY3/27). Accordingly, we also assume that machine tool orders will turn slightly negative year on year in CY2027 (FY3/28). We have the impression that a strong consensus has yet to form among investors and the broader market on this point.

## HK investor visit feedback: Aerospace & Defense: Interest from investors growing more than expected as a non-AI play

Within the Japan Industrials sector, where an AI ≈ FA equation tends to hold, we received more inquiries than expected asking whether Aerospace & Defense stocks — as non-AI plays — still offer upside potential. Given the current market sentiment driven by the tech sector, we had assumed that questions on Aerospace & Defense would be limited (with the balance of interest roughly 90% FA and 10% Aerospace & Defense), but our impression was that investor interest was closer to 70% FA and 30% Aerospace & Defense. Some investors expressed a strong desire to scrutinize the heavy industry companies as non-AI stocks with high earnings growth visibility, partly because of the sharp multiple contraction in AI-related stocks from their peak at the start of the year and the front-loading of capex sentiment into 2026.

However, in terms of individual stocks, investors showed stronger interest in a turnaround at IHI — whose multiples have fallen sharply from their peak at the start of the year — and a re-rating of Kawasaki Heavy Industries — which announced a share issuance and convertible bond issuance — rather than in Mitsubishi Heavy Industries, on which we have a Buy rating. Among the three heavy industry companies, we prefer

Mitsubishi Heavy Industries as one of the stocks likely to deliver the highest earnings growth with the greatest degree of certainty when looking out to FY2027-2028. We also recommend Japan Steel Works, AeroEdge, and SKY Perfect JSAT as small/mid-cap ideas within the Aerospace & Defense subsector.

FAQ post-Yaskawa earnings: Yaskawa's miss was company-specific, but execution risk at other FA names has become a new focus

After our follow-up with Yaskawa Electric (Buy, on CL), we made significant downward revisions to our estimates for FY2/27 in particular (our report). While the company repeatedly emphasized that the issues were specific to Yaskawa and not an industry-wide phenomenon, investor attention has shifted to execution risk at other companies. Our impression is that the constraints on Yaskawa's revenue, shipments, and production stemming from the ERP issues are largely attributable to internal factors, and that order trends themselves remain buoyant, with component procurement proceeding smoothly despite higher costs. However, while ERP-related issues are purely company-specific, the question of whether other companies may be harboring execution risks that are not visible from the outside has suddenly emerged as a key concern. This reflects a growing awareness not only of the lead time delay risk for certain products that we also flagged during our Taiwan research trip, but also of the risk of higher variable costs from being overly busy and the risk of operational issues arising from human resource constraints.

As a result, we think this quarter's earnings season will attract more attention than usual to whether companies are executing smoothly. More specifically, the following points are likely to be discussed more actively than simply whether orders and earnings beat expectations due to supply/demand tightness: (1) whether there are any headwinds to revenue and order trends from production or procurement constraints; (2) whether there have been any changes to the overall cost structure, including not only component costs but also labor and other fixed cost trends; (3) whether the overly buoyant demand environment is giving rise to speculative demand, such as advance ordering; (4) whether lead time extensions — a common cause of such speculative demand — are occurring; and (5) when supply capacity will be expanded (i.e., when supply/demand easing will be triggered).

In light of these shifts in investor sentiment and the current supply/demand environment, among the FA stocks with upcoming earnings announcements, we particularly prefer Keyence as a Buy-rated name with relatively limited downside risk.

## FAQ post-JSW MTP announcement: Focus on pricing assumptions

Japan Steel Works released an outline of updates to its medium-term plan JGP2028 on July 7 and held an investor briefing on July 13 (our report). Supply/demand tightness for critical components used in gas turbines and nuclear power has intensified further since the medium-term plan was originally formulated in 2024, and the key focus for investors was how far profitability in the material & engineering business could improve, driven by both (1) expansion of marginal profit from higher shipment volumes and (2) unit price improvement (pricing) for large components.

In this update, the segment operating profit target for the material & engineering business in FY3/29 was raised substantially, from ¥8 bn (OPM 15%) to ¥16 bn (OPM 20%). However, based on our conversations with investors, the prevailing reaction was one of mild disappointment, partly because Bloomberg consensus had already reached a similar profit level on the back of growing expectations for higher shipment volumes. While FY3/26 actual results had already reached approximately ¥8.9 bn (OPM 19%), the company's FY3/27 guidance of ¥9.5 bn (OPM 16%) implied a temporary decline in profitability, which had been a source of growing investor concern. While the company's explanation — citing front-loaded increases in fixed costs — was understandable, the overall investor reaction was that the new FY3/29 target also looks like a conservative numerical target.

In our view, the FY3/29 OPM target of 20% still incorporates conservative assumptions for the pass-through of fixed cost increases and unit price improvement driven by supply/demand tightness, and we believe meaningful upside potential remains. On the other hand, the company has indicated that the front-loaded increase in fixed costs is expected to continue not only in FY3/27 but through FY3/29 as well, and investors appear to be mindful of the possibility that the timing of a full-fledged profitability recovery could be pushed back, depending on the pace of progress in passing through fixed cost increases.

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

## Rating and pricing information

AeroEdge (Buy, ¥1,605), Japan Steel Works (Buy, ¥7,719), Keyence (Buy, ¥75,590), Mitsubishi Heavy Industries (Buy, ¥3,758), SKY Perfect JSAT Corp (Buy, ¥2,481) and Yaskawa Electric (Buy, ¥5,450)

Distribution of ratings/investment banking relationships
GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the prof

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
