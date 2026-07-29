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
# Japan Technology: Hardware - Industrial Electronics: GLW 2Q: DC demand strong; valuation gap with Japanese peers to narrow

Corning (Not Covered) held its 2QFY26 results briefing on July 28 (from 21:30 JST). 2Q companywide core sales were US\$4,738 mn (Bloomberg consensus: US\$4,644 mn), and core EPS was US\$0.78 (vs. US\$0.76). In the Optical Communications segment, which supplies optical fiber/cables, 2Q sales of US\$2,072 mn (vs. BBG consensus of US\$2,011 mn) and segment profits of US\$438 mn (vs. consensus of US\$403 mn) both beat expectations. In 2Q, while Enterprise Network sales were up 65% yoy, Carrier Networks sales were up just 1% yoy and down 9% qoq due to timing shifts in customer projects. However, Corning commented that it expects continued solid demand, supported by data center interconnect (DCI) and FTTH demand. The company also said its view on demand for photonics such as CPO/NPO, and scale-up demand, such as in-rack optical interconnects for AI servers, has not changed significantly since its Investor Day in May.

Ryo Harada
+81(3)4587-9865 | ryo.harada@gs.com
GS Japan Co., Ltd.

Hiroki Muramatsu  
+81(3)4587-9872 |  
hiroki.muramatsu@gs.com  
GS Japan Co., Ltd.

As of 10:48 AM local time, Corning's stock was trading down $19\%$ from the previous day. While its data center optics-related business is strong, we think the share price decline owes to the Solar business falling into the red in 2Q on one-off expenses and weak 3Q sales guidance.

Near-term sentiment on AI-related stocks warrants caution as they have recently tended to fall despite strong results. However, forward P/E multiples (LSEG basis) are down to 26X for Fujikura, 19X for Sumitomo Electric, and 22X for Furukawa Electric, versus 41X for Corning, and as such we look for eventual re-ratings for these coverage names. In addition, while we have heard concerns from market participants about competition with Chinese manufacturers, this is precisely why Japanese manufacturers have refrained from capacity expansion investments in commodity areas like optical fiber (where oversupply has previously been an issue) and instead focused on high-value-added cables and other products. We believe that once the market calms down, the time will come when these management decisions will be recognized.

## Key takeaways from Corning's results briefing

The following summarizes company commentary on the Optical Communications segment.

■ 2Q sales: US\$2,072 mn (Bloomberg consensus: US\$2,011 mn), up 32% yoy.

■ 2Q segment profits: US\$438 mn (vs. consensus of US\$403 mn), up 77% yoy.

2Q sales for the Enterprise Network subsegment were US\$1,269 mn (vs. consensus of US\$1,057 mn), up 65% yoy, while sales for the Carrier Network subsegment were US\$803 mn (vs. consensus of US\$939 mn), up 1% yoy.

In Enterprise Networks, AI data center-related demand nearly doubled yoy. The company said generative AI-related demand is strong and that orders are accelerating further.

Carrier Networks sales were down 9% qoq, but this was due to timing shifts in customer projects; for 1H26, sales were solid, up 17% yoy. The company said it expects mid-single-digit sales growth in the long term, driven by strong demand from data center interconnect (DCI) and fiber-to-the-home (FTTH).

According to Corning, its major capacity expansion initiatives are based on long-term contracts with customers, proceeding with an appropriate sharing of investment risk and return. It indicated that it expects the number of long-term contracts to increase in the future.

Regarding business opportunities in Photonics and Scale-up, the company said there has been no significant change in its view from the May Investor Day, and that it is preparing to capture demand related to the optical transition of next-generation scale-up networks.

## Price Target Risks and Methodology - Fujikura

We are Buy rated. Our 12-month price target of ¥7,500 is based on an EV/EBITDA of 25.0X (FY3/28E; multiple based on the EV/EBITDA and EBITDA margin correlation across its domestic and global competitors). Downside risks: Telecommunications: A delay in benefits from hyperscaler investment, a prolonged restraint in telecom carrier investment, and competitors in ultra-high-density optical fiber cables catching up with Fujikura. Electronics: A greater-than-expected slowdown in the smartphone market and/or more intense competition. Automotive products: Automobile production volume undershooting our assumptions. Companywide: Forex swings.

## Price Target Risks and Methodology - Furukawa Electric

Our 12-month target price is ¥7,200. We apply an EV/EBITDA multiple of 25.0X (FY3/28E, based on the correlation between EV/EBITDA and EBITDA growth rate for domestic and overseas competitors). We are Buy rated. Risks: Communications solutions: If sales expansion of high-margin optical products for data centers does not proceed as expected and there is no improvement in profits. If the profitability of the acquired Furukawa FITEL Optical Components (FFOC) deteriorates again due to factors such as changes in competitiveness. If generative AI data center investment slows for reasons such as delays in data center construction due to supply shortages of some essential products, or if investment in generative AI data centers starts to wane as project profitability deteriorates due to price hikes for component products. Energy infrastructure: If demand for both high-voltage and medium/low-voltage cables slows due to factors such as a slowdown in generative AI investment. If the company decides on capex for HVDC cables but fails to secure the expected orders from customers. Electronics & automotive systems: If auto production volume or sales of models supplied by the company do not grow as much as expected. If fluctuations in auto production volume are larger than expected and the company is unable to absorb fixed costs through measures such as price revisions. If material prices surge more than expected and the company is unable to pass these on to customers. Functional products: If, in the copper foil business, sales expansion of high-function circuit foils does not proceed as planned and profitability improvement is not expected, if orders for thermal products for generative AI are not booked as sales for some reason or are delayed, or if the acquisition of new customers for semiconductor manufacturing tape does not progress as expected.

## Price Target Risks and Methodology - Sumitomo Electric Industries

We are Buy rated. Our 12-month target price is ¥3,400. We apply a target EV/EBITDA multiple of 13.0X (based on FY3/28E, using an SOTP approach). Key downside risks: Automotive segment: Decline in automobile production volume; slower-than-expected pass-through of material procurement costs to selling prices. Infocommunications segment: Longer-than-expected inventory adjustments due to a slowdown in hyperscaler capex; catch-up by competitors in ultra-high density optical fiber cables. Environment & energy segment: Delays in new and replacement power infrastructure projects due to difficulties in procuring materials and securing workers; slower-than-expected earnings contributions from the Japanese government's clean energy strategy. Industrial materials and other segments: Slowdown in demand for cemented carbide tools, etc., due to a macroeconomic slowdown; increase in manufacturing costs for sintered parts, etc., due to rising energy prices. Company-wide: FX fluctuations; sustained high material prices.

## Price Target Risks and Methodology - SWCC

Valuation methodology: We have a Buy rating. Our 12-month target price of ¥16,200 is based on an EV/EBITDA of 11.5X (FY3/28E, multiple based on the correlation between EV/EBITDA and EBITDA margin for global competitors).

Key downside risks: Energy & infrastructure segment: The balancing out of supply and demand for wires/cables and power equipment in Japan, resulting in lower selling prices; a lack of progress with the further leveling of construction work and improvement of personnel allocation efficiency, resulting in slower-than-expected profit margin improvement; an influx of foreign workers significantly alleviating the shortage of construction workers in Japan. Communication & components segment: Sharp declines in optical fiber cable selling prices due to a large supply of inexpensive products from China, India, and other countries, and profitability deteriorating as a result; home appliance sales in China and Japan falling short of expectations; acceleration in the trend toward a paperless society, resulting in a steeper-than-expected decline in sales of printer rollers. A slower-than-expected shift to EVs by the company's customers, leading to lower demand; significant declines in automobile production volume, including EVs; increases in prices of materials such as copper, with the company unable to pass these increases on to customers. Company-wide: The implementation of large-scale growth investments aimed at furthering overseas expansion in the electronic equipment & components and communication & industrial devices segments, with returns on these investments falling short of expectations and significantly impacting company-wide margins; yen appreciation.

## Price Target Risks and Methodology - Anritsu

Our 12-month target price is ¥5,300, based on a target EV/EBITDA multiple of 17X on

FY3/28E (our target multiple is based on the correlation between EV/EBITDA and EBITDA margin for global competitors). We are Buy rated.

Risks: Test and Measurement: Demand for 5G applications has already cooled, and there is a risk that sales may not grow as expected, leading to a deterioration in profit margins. For the data center business, uncertainty due to US tariffs could lead to slower decision-making by customers, resulting in stagnating or weaker demand. Testing methods may change from $100\%$ testing to sampling testing. PQA: Possible decline in domestic market share, or the failure of sales expansion to proceed as expected in regions where the company is accelerating business development, such as North America, Europe, and China. Environmental Measurement: The possibility that earnings in battery test equipment fail to grow as expected due to a slowdown in the BEV market. Company-wide: Disappointing returns from M&A and/or growth investment. An increase in the R&D expense ratio. Yen appreciation.

## Disclosure Appendix

## Reg AC

We, Ryo Harada and Hiroki Muramatsu, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Ryo Harada GS Japan Co., Ltd., Hiroki Muramatsu GS Japan Co., Ltd..

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

The rating(s) for Anritsu, Fujikura, Furukawa Electric, SWCC and Sumitomo Electric Industries is/are relative to the other companies in its/their coverage universe: Anritsu, Daihen, Fuji Electric Co., Fujikura, Furukawa Electric, Hitachi, Meidensha, Mitsubishi Electric, Panasonic Holdings, SWCC, Sumitomo Electric Industries

## Company-specific regulatory disclosures

Compendium report: please see disclosures at https://www.gs.com/research/hedge.html. Disclosures applicable to the companies included in this compendium can be found in the latest relevant published research

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See 'Ratings, Coverage universe and related definitions' below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services wit

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
