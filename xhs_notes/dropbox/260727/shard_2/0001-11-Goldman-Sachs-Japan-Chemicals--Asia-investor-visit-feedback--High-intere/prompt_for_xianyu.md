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
# Japan Chemicals: Asia investor visit feedback: High interest in electronic materials companies and individual catalysts amid volatility

We visited Asia (Hong Kong/Singapore) from the third to the fourth week of July, where we held meetings with c.55 investors over eight days. We summarize the key takeaways below. In the third week of July, in particular, stock market volatility was high amid concerns over the outlook for AI demand and the competitive landscape. Nevertheless, many investors remain positive on semiconductor and AI-related demand and fundamentals, and our impression was that interest remained high, particularly in electronic materials. Investor focus appeared to center on whether companies can make timely capex and exercise pricing power amid tightening supply/demand conditions for various AI-related materials. The stocks that generated the most discussion included Nitto Boseki (Nittobo), JX Advanced Metals, Mitsui Kinzoku, SUMCO, and Resonac (all of which we are Buy rated on).

Nitto Boseki (Buy): Our impression through our discussions with investors was that many had been shorting or underweighting Nittobo shares over the past three months or so amid a deteriorating supply/demand balance for its mainstay product, T-glass, and relatively high valuations. The backdrop to this appeared to be a consensus negative bias among investors, who believe the company's competitive advantage could be eroded by new market entries and production increases by manufacturers in Taiwan, Japan, and mainland China in both low thermal expansion glass and low dielectric glass. On the other hand, there was strong interest in our recent upgrade (from Neutral to Buy). In particular, regarding T-glass, despite moves by new entrants, we got the impression there was some agreement with our view that the company's competitive advantage will remain for the time being, with the actual adoption of competitors' products being significantly delayed. An announcement of additional capacity expansion for T-glass (and price revisions), as well as the strength of earnings of NER glass cloth for PCBs in results could serve as catalysts, in our view.

Mitsui Kinzoku (Buy): Previously, our impression was that many investors held a positive view, but during our recent meetings, pessimistic views were generally more prevalent due to concerns over a decline in market share resulting from delays in capacity expansion for VSP™ and competitors' capacity expansions. However, in the view of the company and ourselves (link), we have the impression that these concerns are overdone and far removed from reality. Although many investors expressed pessimistic views on VSP, we were surprised that there was almost no discussion regarding MicroThin™, which forms the core of copper foil business profits, could achieve high profit growth, and is a product category where the

Atsushi Ikeda
+81(3)4587-9940 |
atsushi.ikeda@gs.com
GS Japan Co., Ltd.

Yuri Izumikawa
+81(3)4587-3643 |
yuri.x.izumikawa@gs.com
GS Japan Co., Ltd.

company has a very high market share. We think this can be seen as evidence that investors have a pessimistic bias centered on VSP. Consequently, we believe the market is awaiting an announcement of a capacity expansion plan for VSP from the company to serve as a catalyst.

JX Advanced Metals (Buy): Our impression was that investor interest was focused on InP substrates. While the company has already announced a capacity expansion of c.10X, its pricing strategy remains largely unknown, and a few investors expressed concerns regarding capacity expansions by Chinese competitors. Therefore, if management provides explanations at future briefings regarding medium- to long-term earnings growth strategies, including long-term agreements, we believe investor expectations could rise for this business to become a second pillar alongside semiconductor sputtering targets, which are the profit driver of current focus businesses. We will be paying close attention to management's comments at the upcoming results briefing, as well as 1Q results, which we expect to be strong.

SUMCO (Buy): Compared to US investors, who generally held positive views, Asian investors' views were mixed (though this seemed to be heavily influenced by semiconductor sentiment at the time). The bearish view was that it will take time for wafer supply/demand conditions to tighten in the near term due to high inventory levels and the supply/demand gap resulting from past investments by various companies, making it difficult to implement substantial price hikes in long-term agreements (LTAs). We also noted a fair number of opinions that the stock does not look undervalued from a valuation perspective. On the other hand, we maintain a constructive stance based on our view that the 300 mm supply/demand balance will tighten considerably in 2027, driven by the broadening of AI demand and the impact of dual-wafer usage, and that we expect price increases from 2028 associated with LTAs.

Resonac (Buy): While we received a number of questions asking about the negative impact of glass cores on the company's earnings, we got the impression that almost no investors held concerns regarding the company's fundamentals. At the same time, there was a notable amount of feedback suggesting that the stock does not look undervalued based on consensus estimates. For FY12/27, we expect earnings to beat the consensus EPS estimate by slightly over $20\%$ . We conveyed our view that a P/E of around 15X at that level suggests significant undervaluation, given that Resonac covers many of the key areas in AI semiconductor back-end processes and the potential of new packaging-related materials such as organic interposers, making it an attractive core holding in back-end materials.

## Price Target Risks and Methodology - Nitto Boseki

We are Buy rated on Nitto Boseki with a 12-month target price of ¥4,820. Our target price is based on the correlation between the materials sector's EV/GCI and the FY3/28E CROCI/WACC forecast (cash-return multiple of 0.7x plus a 60% premium to the sector average). Key risks include fluctuations in semiconductor demand, currency volatility, and changes in the competitive landscape for specialty glass.

## Price Target Risks and Methodology - JX Advanced Metals Corp.

We are Buy rated on JX Advanced Metals with a 12-month target price of ¥5,010. Our target price is based on the materials sector EV/GCI and FY3/28E CROCI/WACC (CROCI multiple of 0.7X, plus the stock's recent historical premium of 25% to the sector

average).

Key risks: (1) Slowdown in semiconductor demand, (2) slowdown in AI server demand, (3) delays in structural reforms, (4) yen appreciation, and (5) fluctuations in copper and other metal prices.

## Price Target Risks and Methodology - Mitsui Kinzoku

We are Buy rated on Mitsui Kinzoku with a 12-month target price of ¥62,600. Our target price is based on the correlation between the materials sector's EV/GCI and our FY3/28E CROCI/WACC forecast (cash return multiple of 0.7X plus a 60% premium to the sector average). Key risks include slowdown in AI server demand, yen appreciation, and decline in prices for zinc and other metals.

## Price Target Risks and Methodology - SUMCO

We are Buy-rated on SUMCO with a 12-month target price of ¥6,140. Our target price is based on the FY12/27-FY12/28 average correlation between the materials sector EV/GCI and CROCI/WACC estimate (using a cash return multiple of 0.7X).

Key risks: A slowdown in semiconductor demand, yen appreciation, and a greater-than-expected increase in depreciation and other fixed costs.

## Price Target Risks and Methodology - Resonac

We are Buy rated on Resonac with a 12-month target price of ¥23,920. Our target price is based on the correlation between the materials sector's EV/GCI and the FY12/27E CROCI/WACC (cash-return multiple of 0.7X plus a 30% premium to the sector average). Key risks include a slowdown in semiconductor demand, yen appreciation, and decline in graphite electrode earnings.

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

GS and/or one of its affiliates is acting as a financial advisor in connection with an announced strategic matter involving the following company or one of its affiliates: Resonac Holdings Corporation

The rating(s) for JX Advanced Metals Corp., Mitsui Kinzoku Co., Nitto Boseki Co, Resonac Holdings and SUMCO is/are relative to the other companies in its/their coverage universe: Asahi Kasei, Daicel, Denka, Fujimi Inc., JX Advanced Metals Corp., Kuraray, Mitsubishi Gas Chemical, Mitsui Chemicals Inc., Mitsui Kinzoku Co., Nippon Paint Holdings, Nitto Boseki Co, Resonac Holdings, SUMCO, Shin-Etsu Chemical, Tokyo Ohka Kogyo, Toray Industries, Tri Chemical Laboratories Inc., Zeon

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned 1% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the month end preceding this report: Mitsui Kinzoku Co. (¥31,910), Nitto Boseki Co (¥3,195), Resonac Holdings (¥14,505) and SUMCO (¥3,623)

GS has received compensation for investment banking services in the past 12 months: JX Advanced Metals Corp. (¥3,770)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: JX Advanced Metals Corp. (¥3,770), Resonac Holdings (¥14,505) and SUMCO (¥3,623)

GS has received compensation for non-investment banking services during the past 12 months: JX Advanced Metals Corp. (¥3,770)

GS had an investment banking services client relationship during the past 12 months with: JX Advanced Metals Corp. (¥3,770), Resonac Holdings (¥14,505) and SUMCO (¥3,623)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: JX Advanced Metals Corp. (¥3,770), Resonac Holdings (¥14,505) and SUMCO (¥3,623)

GS had a non-securities services client relationship during the past 12 months with: JX Advanced Metals Corp. (¥3,770), Mitsui Kinzoku Co. (¥31,910), Resonac Holdings (¥14,505) and SUMCO (¥3,623)

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>59%</td><td>43%</td></tr></table>

GS has managed or co-managed a public or Rule 144A offering in the past 12 months: JX Advanced Metals Corp. (¥3,770)

## Distribution of ratings/investment banking relationships GS Investment Research global Equity coverage universe

As of July 1, 2026, GS Global Investment Research had investment ratings on 3,104 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See 'Ratings, Coverage universe and related definitions' below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Price target and rating history chart(s)

![](images/da5f086f58fa3d405f01699eeaefb1d0e3e72abbe636f00269ab28ce0b80439a.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may not have included price targets, as well as developments relating to the company, its industry and financial markets.

![](images/a0eec2cbd6536a5d635c2218a4f18f46095eecf719c93dc70986a92bd1f95a91.jpg)  
The price targets shown should be considered in the context of all prior published GS, which may or may 

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
