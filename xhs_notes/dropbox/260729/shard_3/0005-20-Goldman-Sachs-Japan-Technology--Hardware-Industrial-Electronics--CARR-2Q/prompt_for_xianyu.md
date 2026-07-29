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
# Japan Technology: Hardware - Industrial Electronics: CARR 2Q: Favorable implications for MELCO and Pana, cost rises bear watching

Carrier (covered by our US Multi-Industry sector analyst Joe Ritchie) announced 2Q26 results on July 28 (JST). Key takeaways were as follows. 1) In the Americas, channel inventory is down -25% yoy, and the company expects strong demand to continue into 2H. 2) In Europe, heat pumps remain strong, growing +20% yoy. 3) Asia is also performing well, excluding China. From a sales perspective, we see positive implications for earnings at Mitsubishi Electric and Panasonic Holdings. On the other hand, for Carrier, rising raw material costs and other factors are impacting profit margins. We are upbeat about both Mitsubishi Electric and Panasonic Holdings working to reduce fixed costs, but the impact of high costs also needs to be kept in mind. Additionally, regarding Mitsubishi Electric, we think the earnings outlook is positive for its Factory Automation (FA) business, as the group's specialized trading company RYODEN raised its full-year earnings guidance on July 28.

Ryo Harada
+81(3)4587-9865 | ryo.harada@gs.com
GS Japan Co., Ltd.

Carrier's results also confirmed strong data center demand, particularly in the Americas. In the DC air conditioning space, Mitsubishi Electric develops chillers mainly in Europe, but is looking to expand its business to the US, and we see potential for positive developments on this front.

Hiroki Muramatsu
+81(3)4587-9872 |
hiroki.muramatsu@gs.com
GS Japan Co., Ltd.

## Key takeaways from Carrier's results briefing

2Q sales came to US\$6,351 mn (Bloomberg consensus: US\$6,021 mn), with organic growth of +3% yoy.

2Q adjusted operating profits finished at US\$1,095 mn (consensus: US\$1,041 mn), down -6% yoy. The adjusted operating profit margin was 17.2% (-190 bps yoy). Higher volumes and productivity improvements contributed, but this was offset by rising raw material costs and an unfavorable business mix.

2Q orders were up by +40% yoy. Commercial HVAC was strong at +65% yoy, with particularly strong demand seen in data center-related business, up over +300% yoy. Carrier guides for FY26 data center sales of US\$2.0 bn, an upward revision from previous guidance of US\$1.5 bn. The product portfolio for CDUs (coolant distribution units) is expanding, and orders for CARR's QuantumLeap cooling solution are increasing.

The order backlog at the end of 2Q was over USD8 bn, up +40% yoy and +20% qoq.

Climate Solutions Americas (CSA) business: 2Q sales were US\$3,372 mn (consensus: US\$3,138 mn), with organic growth of +4% yoy. Residential (+9% yoy) and Light Commercial (+10% yoy) were strong. Residential channel inventory was down -25% yoy, and the company expects strong growth in 2H. Commercial was down -8% yoy due to shipment timing, but the company expects expansion in data center-related business in 2H26. Commercial orders doubled yoy, driven by data center-related orders, which were up over +300% yoy.

Climate Solutions Europe (CSE) business: 2Q sales were US\$1,324 mn (consensus: US\$1,307 mn), with organic growth of +3% yoy. Residential & Light Commercial (RLC) saw positive high-single-digit % growth yoy. The electrification trend continues, and heat pump sales performed well, up +20% yoy. While Commercial saw a mid-single-digit % decline, CARR expects a recovery in 2H26 on data center-related demand.

Climate Solutions Asia Pacific Middle East & Africa (CSAME) business: 2Q sales were US\$917 mn (consensus: US\$867 mn), with organic growth of +4% yoy. In China, RLC remained weak, down -25% yoy. However, other regions excluding China were strong, with positive growth in India (+35% yoy), the Middle East (+35% yoy), Southeast Asia (+20% yoy), and Australia (+30% yoy).

The company raised its FY26 full-year guidance. Sales guidance was raised from US\$22 bn to US\$23 bn, and adjusted operating profit guidance from US\$3.4 bn to US\$3.5 bn.

## Price Target Risks and Methodology - Panasonic Holdings

We are Buy rated. Our 12-month target price is ¥5,000. We apply an EV/EBITDA multiple of 9.0X (FY3/28E base year, based on the historical correlation between EV/EBITDA and EBITDA margin). Risks: Companywide: (1) Weaker-than-expected progress with fixed-cost reductions or insufficiently realized benefits from business reforms across the company as a whole, (2) weaker growth prospects due to the loss of key personnel during the fixed-cost reduction process, (3) slower-than-expected progress in revamping the business portfolio as a result of delays selecting buyers, (4) additional investment and depreciation burdens arising due to increased demand for cylindrical batteries, and (5) forex trends (we estimate that every ¥1 appreciation vs. the USD/EUR/CNY impacts annual adjusted operating profits by -¥0.9 bn/-¥1.0 bn/+¥4.7 bn, respectively). Lifestyle updates business: Weaker demand for residential/commercial air conditioners due to a downturn in the global economy, or the loss of market share to more popular or cheaper products at competitors. Panasonic Connect: (1) A slump in the company's aircraft services business if the "bring your own devices" trend were to become more common for in-flight entertainment on commercial aircraft, (2) weaker-than-expected sales growth at acquired company Blue Yonder (standalone basis), (3) major impairment losses on Blue Yonder if the calculation of its present value were to require a higher WACC due to rising interest rates, softer demand or other factors (indication of impairment is checked every quarter), and (4) a longer-than-anticipated decline in demand for various mounting systems used in process automation, such as the manufacture of PCs and smartphones. Panasonic Energy: Tesla opting to increase its use of batteries made by other companies, leading to stronger pricing pressures, a further slowdown in the EV market, or increased

competition in the generative AI-related battery backup unit (BBU) business. Panasonic Industry: Weaker-than-expected factory automation-related demand, stiffer competition in the generative AI-related hybrid capacitor and circuit board material businesses, or a longer-than-expected downturn in demand for smartphones and other consumer electronics.

## Price Target Risks and Methodology - Mitsubishi Electric

Valuation methodology: We are Buy rated. Our 12-month target price of ¥7,400 is based on an FY3/28E EV/EBITDA of 14X (based on the correlation between EV/EBITDA and EBITDA margins of global competitors).

Key downside risks: Industrial automation systems (FA): Marginal profit growth on top-line expansion failing to offset higher depreciation from the company's new production facilities if the slowdown in orders is prolonged. Industrial automation systems (automotive equipment): A lack of progress exiting from the car multi-media business, challenges finding partners in the CASE business, or a sharp slowdown in production at client automakers. Home appliances (HVAC): Challenges achieving production scale due to difficulties procuring components and other factors, or deteriorating margins in the ATW business in a stronger competitive landscape. Power semiconductors: Inability to secure sufficient sales/orders to cover new capex, or more intense price competition on significant investment by Chinese companies and other rivals. Elevator & escalator business: Stalled new construction demand in China and other markets, or the outflow to third parties of high-margin maintenance contracts in the domestic business. Infrastructure systems: Project delays or larger-than-expected losses generated in the defense & space systems business. Companywide: Weaker prospects for synergies realized between businesses, and yen appreciation.

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

The rating(s) for Mitsubishi Electric and Panasonic Holdings is/are relative to the other companies in its/their coverage universe: Anritsu, Daihen, Fuji Electric Co., Fujikura, Furukawa Electric, Hitachi, Meidensha, Mitsubishi Electric, Panasonic Holdings, SWCC, Sumitomo Electric Industries

The rating(s) for Carrier Global Corp. is/are relative to the other companies in its/their coverage universe: 3M Co., ATS Corp., Allegion Plc, Carrier Global Corp., Cognex Corp., Core & Main Inc., Dover Corp., DuPont de Nemours Inc., EquipmentShare, Flowserve Corp., Forgent Power Solutions Inc., GE Vernova, Graco Inc., Honeywell International Inc., INNIO, ITT Inc., Illinois Tool Works, Ingersoll Rand Inc., Johnson Controls International Plc, Kennametal Inc., Lennox International Inc., Madison Air Solutions, Mirion Technologies Inc., Parker Hannifin Corp., RBC Bearings Inc., Regal Rexnord Corp., Rockwell Automation Inc., Roper Technologies Inc., Stanley Black & Decker Inc., Timken Co., Trane Technologies Plc, Vontier Corp., Zurn Elkay Water Solutions Corp., nVENT Electric Plc.

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned 1% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the month end preceding this report: Panasonic Corp. (\$7.24) and Panasonic Holdings (\$3,604)

GS has received compensation for investment banking services in the past 12 months: Carrier Global Corp. (\$69.33), Mitsubishi Electric (¥5,319), Panasonic Corp. (\$7.24) and Panasonic Holdings (¥3,604)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Carrier Global Corp. (\$69.33), Mitsubishi Electric (¥5,319), Panasonic Corp. (\$7.24) and Panasonic Holdings (¥3,604)

GS has received compensation for non-investment banking services during the past 12 months: Carrier Global Corp. (\$69.33)

GS had an investment banking services client relationship during the past 12 months with: Carrier Global Corp. (\$69.33), Mitsubishi Electric (¥5,319), Panasonic Corp. (\$7.24) and Panasonic Holdings (¥3,604)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: Carrier Global Corp. (\$69.33), Mitsubishi Electric (¥5,319), Panasonic Corp. (\$7.24) and Panasonic Holdings (¥3,604)

GS had a non-securities services client relationship during the past 12 months with: Carrier Global Corp. (\$69.33), Mitsubishi Electric (¥5,319), Panasonic Corp. (\$7.24) and Panasonic Holdings (¥3,604)

GS makes a market in the securities or derivatives thereof: Carrier Global Corp. (\$69.33)

Distribution of ratings/investment banking relationships GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See 'Ratings, Coverage universe and related definitions' below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/c84030f34ef657f379eb0ffca43ef7874accba37cb53df1113dbe4cfb78f110f.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its indu

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
