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
# Japan Shipbuilding: Japan Growth Strategy Council: Reaffirms shipbuilding importance from an economic security perspective

Materials from the fifth meeting of the Japan Growth Strategy Council, held on June 24, were disclosed (link, Japanese only). We summarize the Japanese government's view of current conditions as presented in its draft of a Public-Private Investment Roadmap, government targets and specific policy proposals, and the implications for our Japanese shipbuilding coverage (Namura Shipbuilding, Mitsui E&S, and Tokyo Keiki). All three companies operate businesses that are important from the perspective of Japan's economic security in our view, and we will be watching their business development leveraging future policies. We maintain our Buy rating on all three companies.

■ Next-generation vessels: The shipbuilding industry is vital to ensuring a stable supply of commercial vessels for maritime transport of food and other goods, as well as vessels for defense. However, current domestic shipbuilding volume is below demand from Japanese shipowners and operators. Demand for next-generation vessels (e.g., zero-emission ships) is poised to increase in the medium to long term, presenting a potentially game-changing opportunity in the shipbuilding market. Leveraging technologies related to next-generation vessels, the government aims to double shipbuilding volume by 2035 compared to 2024 levels to secure international competitiveness. Potential policies include support for strengthening shipbuilding systems, establishment of educational and research systems for human resource development, leading formulation of international rules at the IMO, and support for overseas shipbuilding in like-minded countries.

\- Ship repairs and maintenance: At present, the vast majority of repair and maintenance work in Japan is for domestic coastal vessels, including naval ships and patrol boats (over 90% of the total in 2024 were coastal vessels), and the country is highly dependent on specific overseas countries for ocean-going vessels. To address this, the government plans to establish systems to improve repair and maintenance capacity, and taking into account current conditions of repair docks, it assumes ¥100 bn in public-private investment. Potential policies include leveling out the timing of repairs for government vessels, promoting productivity improvements, establishing educational systems for human resource development, and utilizing repair facilities in like-minded countries.

■ LNG carriers: Currently, Japanese shipping companies and consumers (such as electric power and gas companies) have a fleet of c.200 LNG vessels, but the

Norihiro Miyazaki
+81(3)4587-9842 |
norihiro.miyazaki@gs.com
GS Japan Co., Ltd.

Ryohei Kurita
+81(3)4587-1799 |
ryohei.kurita@gs.com
GS Japan Co., Ltd.

construction of LNG carriers in Japan has ceased since 2019. The acquisition and retention of construction technology for LNG carriers is important from an economic security perspective. The government aims to establish systems to build three to five vessels per year from 2035 onward in order to capture the domestic and over, which is poised to see demand growth. Regarding the scale of public-private investment, the roadmap only states that this will be scrutinized in the future as discussions proceed among relevant parties. Potential policies include encouraging shipowners to place stable orders with domestic shipyards, integrating construction know-how possessed by like-minded countries, and establishing educational and research systems for human resource development.

Defense industry: The roadmap recommends building a foundation for the development/manufacturing/maintenance of small unmanned aerial vehicles, as well as transferring equipment to allied and like-minded countries and strengthening Japan's production base for naval vessels. The materials mention that the Mogami-class frigate has attracted interest from allied and like-minded countries. While investment in the naval vessel sector, including defense procurement, is slated at c.¥340 bn (FY2026 budget), additional investment is also expected in line with the revision of Japan's three strategic security documents.

■ Port cargo handling machinery (cranes): Japanese companies (we assume primarily Mitsui E&S) hold a global installed base share of c.10% for STS cranes and slightly over 10% for yard cranes, with the vast majority of the remainder supplied by a single specific company. In the US, policies are being promoted to revive the domestic manufacturing base for STS cranes, and bolstering competitiveness of port cargo handling machinery is also important for Japan from an economic security perspective. The target is to expand sales to overseas markets (¥20 bn-¥30 bn/year) with an eye on the US and Asia, aiming to capture a share of c.30% in the US market by around 2040. Potential policies include support for capex in port cargo handling machinery, subsidies for the introduction of automated cargo handling machinery, and support for overseas expansion.

Implications for Namura Shipbuilding/Mitsui E&S/Tokyo Keiki: Namura Shipbuilding could benefit from Japan's efforts to bolster supply systems for next-generation vessels and LNG carriers, and strengthen repair and maintenance capacity. While the overall direction discussed in the materials is in line with the shipbuilding industry revitalization roadmap released at the end of 2025, a more specific direction was provided for repair and maintenance capacity and LNG carriers, and we see this as further broadening the scope of business opportunities for firms. Mitsui E&S, as Japan's largest marine engine manufacturer, should benefit from the expansion of domestic shipbuilding volume (including LNG carriers), and is also likely to see demand shift toward high-value-added products due to the transition to next-generation vessels. The Council's materials also mention support for capital investment in port cargo handling machinery, where the company estimates it holds a $100\%$ domestic order share (volume basis in FY3/26), and this could lead to improvements in capital efficiency (e.g., ROIC) in the future. Tokyo Keiki stands to benefit from growth in domestic shipbuilding volume as a supplier of marine equipment, and as a supplier of defense equipment, it could also benefit

from the export of frigates and the production of small unmanned aerial vehicles.

![](images/f63daf05c20357717f592fe4804c5f86249f2e9330d7a8a3834ce66c79daa6a3.jpg)  
Source: Ministry of Land, Infrastructure, Transport and Tourism, Data compiled by GS Global Investment Research

## Price Target Risks and Methodology - Namura Shipbuilding Co.

Our 12-month target price of ¥5,600 is based on a target P/B of 2.6X applied to our end-FY3/30E BPS estimate, discounted back to FY3/27E using a cost of equity of 9.8%. Key risks include a sudden increase in production capacity in the shipbuilding industry, higher steel prices, production problems, and a decline in vessel prices.

## Price Target Risks and Methodology - Mitsui E&S Co.

Our 12-month target price is ¥7,000. Using a Sum of the Parts (SOTP) model, we apply target P/E multiples of 10X-19X to our net profit estimates for each segment and the respective reference years we use for them, and discount the sum back to FY3/27 using a cost of equity of 9.8%. We apply a P/E of 19X on FY3/31E for marine propulsion systems, 14X on FY3/30E for logistics systems, 14X on FY3/28E for new business development, and 10X on FY3/28E for peripheral services. Key risks include a sharp increase in input costs, deterioration in container transport demand, production problems, and a decline in prices.

## Price Target Risks and Methodology - Tokyo Keiki

Our 12-month target price is ¥8,800. The target price is derived applying a target P/E multiple of 23X on our FY3/31E EPS estimate and discounting the value back to FY3/27 using a cost of equity of 10%. Key risks include a deterioration in defense demand, a decline in shipping demand, and a decline in prices caused by competition and other relevant factors.

## Disclosure Appendix

## Reg AC

We, Norihiro Miyazaki and Ryohei Kurita, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Norihiro Miyazaki GS Japan Co., Ltd., Ryohei Kurita GS Japan Co., Ltd..

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

The rating(s) for Mitsui E&S Co., Namura Shipbuilding Co. and Tokyo Keiki is/are relative to the other companies in its/their coverage universe: ANYCOLOR, Cover Corp., Japan Airport Terminal, Kotobuki Spirits Co., Kyoritsu Maintenance, Mitsui E&S Co., Namura Shipbuilding Co., Rakus Co., Sansan Inc., Tokyo Keiki, Visional, giftee Inc.

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned 1% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the month end preceding this report: Mitsui E&S Co. (¥4,109) and Tokyo Keiki (¥6,420)

GS beneficially owned 5% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the month end preceding this report: Namura Shipbuilding Co. (¥3,640)

GS had a non-securities services client relationship during the past 12 months with: Mitsui E&S Co. (¥4,109)

Distribution of ratings/investment banking relationships
GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/1db67e08e541afa550fbdc2b4d5aa068d3011126d435893407afd62df2eed423.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/1c7086aa2a4c028b6b3b6bcbf660aa71fd6696409efd305afce48b68d9cdf9f8.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

## Target price history table(s)

Mitsui E&S Co. (7003.T)

<table><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td></tr><tr><td>14-May-26</td><td>7,000</td><td>4,659</td></tr><tr><td>27-Nov-25</td><td>7,800</td><td>6,193</td></tr></table>

Namura Shipbuilding Co. (7014.T)

<table><tr><td>Date of report</td><td>Target price (¥)</td><td>Closing price (¥)</td></tr><tr><td>16-Dec-25</td><td>5,600</td><td>3,645</td></tr><tr><td>27-Oct-25</td><td>6,000</td><td>5,390</td></tr><tr><td>07-Aug-25</td><td>3,750</td><td>3,340</td></tr><tr><td>24-Jun-25</td><td>3,700</td><td>2,708</td></tr></table>

## Tokyo Keiki (7721.T)

Date of report Target price (¥) Closing price (¥)

18-Jun-26 8,800 6,070

Price targets shown in table(s) are unadjusted for corporate actions.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to compan

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
