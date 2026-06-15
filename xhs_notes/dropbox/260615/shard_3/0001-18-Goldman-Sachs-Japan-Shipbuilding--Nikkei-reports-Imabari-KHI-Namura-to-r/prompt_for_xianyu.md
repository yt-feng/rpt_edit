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
# Japan Shipbuilding: Nikkei reports Imabari/KHI/Namura to resume LNG carrier construction; potential to capture stable medium to LT demand

On June 15, the Nikkei reported that Imabari Shipbuilding (private), Kawasaki Heavy Industries, and Namura Shipbuilding will jointly resume construction of LNG carriers (link). The main details and implications are as follows:

Details of the article: Imabari Shipbuilding, Kawasaki Heavy Industries, and Namura Shipbuilding to jointly resume the construction of LNG carriers around 2035. Per the article, the companies will share their LNG carrier design technologies and the welders involved in the construction. The leading proposal is to utilize Kawasaki Heavy Industries' Sakaide Works as the production base. They aim to build three to five vessels annually. Around 100 vessels are currently in operation to supply LNG to Japan, and assuming they are replaced every 20 years, building five vessels a year could secure the capacity needed for LNG imports, all else equal. The article also notes that the Japanese government will consider supporting this by providing introduction subsidies to shipowners with plans to include these details in the “Public-Private Investment Roadmap” to be formulated in June 2026.

Implications for the Japan shipbuilding industry and our coverage: In the Japanese shipbuilding industry, the construction of LNG carriers has not taken place since the last delivery in 2019, as companies withdrew due to low-price offensives by Chinese and South Korean competitors. The current unit price for a 170,000 cubic meter class LNG carrier is around US\$250 mn (¥40 bn based on a forex rate of ¥160/US\$). If three to five vessels are built annually as the article states, this could generate stable replacement demand of ¥120 bn-¥200 bn annually for the Japanese shipbuilding industry (we estimate the market size for the Japanese shipbuilding industry, limited to commercial vessels, to be around ¥1.3 tn-¥1.5 tn as of FY2025). If confirmed, for our coverage companies, Namura Shipbuilding (Buy) and Kawasaki Heavy Industries (Neutral), we would view the development positively as it provides scope for the companies to capture stable medium- to long-term demand. However, for Kawasaki Heavy Industries, the product mix would likely need to be closely examined for potential margin implications. We also think the development could be positive for Mitsui E&S (Buy), which provides marine engines for domestic shipbuilders.

Norihiro Miyazaki

+81(3)4587-9842

norihiro.miyazaki@gs.com

GS Japan Co., Ltd.

Yuichiro Isayama

+81(3)4587-9806

yuichiro.isayama@gs.com

GS Japan Co., Ltd.

Ryohei Kurita

+81(3)4587-1799

ryohei.kurita@gs.com

GS Japan Co., Ltd.

Takato Enoki

+81(3)4587-1739

takato.enoki@gs.com

GS Japan Co., Ltd.

## Price Target Risks and Methodology - Kawasaki Heavy Industries (7012.T)

Our 12-month target price of ¥3,900 is based on a FY3/28E EV/EBITDA, applying the Japan Aerospace & Defense subsector-average multiple of 14X and a 20% sector-relative discount.

The key upside and downside risks include (1) yen depreciation/appreciation relative to our assumed exchange rate, (2) faster-/slower-than-expected expansion of defense order and revenue momentum, (3) lower-/higher-than-expected cost variability in PS&E, particularly promotional expenses in the North American four-wheeler business, and (4) faster-/slower-than-expected progress on portfolio restructuring and the turnaround of low-profitability segments, with implications for the conglomerate discount.

## Price Target Risks and Methodology - Namura Shipbuilding Co.

Our 12-month target price of ¥5,600 is based on a target P/B of 2.6X applied to our end-FY3/30E BPS estimate, discounted back to FY3/27E using a cost of equity of 9.8%.

Key risks include a sudden increase in production capacity in the shipbuilding industry, higher steel prices, production problems, and a decline in vessel prices.

## Disclosure Appendix

## Reg AC

We, Norihiro Miyazaki, Yuichiro Isayama, Ryohei Kurita and Takato Enoki, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Norihiro Miyazaki GS Japan Co., Ltd., Yuichiro Isayama GS Japan Co., Ltd., Ryohei Kurita GS Japan Co., Ltd., Takato Enoki GS Japan Co., Ltd..

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

Mitsui E&S Co. (Buy, ¥4,157)

The rating(s) for Namura Shipbuilding Co. is/are relative to the other companies in its/their coverage universe: ANYCOLOR, Cover Corp., Japan Airport Terminal, Kotobuki Spirits Co., Kyoritsu Maintenance, Mitsui E&S Co., Namura Shipbuilding Co., Rakus Co., Sansan Inc., Visional, giftee Inc.

The rating(s) for Kawasaki Heavy Industries is/are relative to the other companies in its/their coverage universe: AeroEdge, CKD, Daifuku, Daikin Industries, Fanuc, Harmonic Drive Systems, Hoshizaki, IHI, Japan Steel Works, Kawasaki Heavy Industries, Keyence, Makita, Misumi Group, Mitsubishi Heavy Industries, Okuma, Omron, SKY Perfect JSAT Corp, SMC, THK, Yaskawa Electric

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned 1% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the month end preceding this report: Kawasaki Heavy Industries (¥2,834)

GS beneficially owned 5% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the month end preceding this report: Namura Shipbuilding Co. (¥3,545)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Kawasaki Heavy Industries (¥2,834)

GS had an investment banking services client relationship during the past 12 months with: Kawasaki Heavy Industries (¥2,834)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: Kawasaki Heavy Industries (¥2,834)

GS had a non-securities services client relationship during the past 12 months with: Kawasaki Heavy Industries (¥2,834)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td></tr></table>

<table><tr><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

Price target and rating history chart(s)  
![](images/3adb0820034182b2a8168c4deb222cfb16928c00efc85bed66408bc0d315c77c.jpg)

<details>
<summary>line chart</summary>

| Date       | Stock Price | Rating | Target Price |
|------------|-------------|--------|--------------|
| Sep 12     | NA          | B      | 2800         |
| Jun 2024   | NA          | B      | 2200         |
| May 2025   | NA          | B      | 2000         |
| Apr 2025   | NA          | B      | 2200         |
| Mar 2025   | NA          | B      | 2000         |
| Feb 2025   | NA          | B      | 3000         |
| Jan 2025   | NA          | B      | 3400         |
| Dec 2025   | NA          | B      | 4000         |
| Nov 2025   | NA          | B      | 3400         |
| Oct 2025   | NA          | B      | 3000         |
| Sep 2025   | NA          | B      | 2800         |
| Aug 2025   | NA          | B      | 2600         |
| Jul 2025   | NA          | B      | 2400         |
| Jun 2025   | NA          | B      | 2200         |
| May 2025   | NA          | B      | 2000         |
| Apr 2025   | NA          | B      | 1800         |
| Mar 2025   | NA          | B      | 1600         |
| Feb 2025   | NA          | B      | 1400         |
| Jan 2025   | NA          | B      | 1200         |
| Dec 2025   | NA          | B      | 1000         |
| Jan 2026   | NA          | B      | 800          |
| Feb 2026   | NA          | B      | 600          |
| Mar 2026   | NA          | B      | 400          |
| Apr 2026   | NA          | B      | 200          |
| May 2026   | NA          | B      | 100          |
| Jun 2026   | NA          | B      | 50           |
| Jul 2026   | NA          | B      | 25           |
| Aug 2026   | NA          | B      | 15           |
| Sep 2026   | NA          | B      | 10           |
| Oct 2026   | NA          | B      | 5            |
| Nov 2026   | NA          | B      | 2            |
| Dec 2026   | NA          | B      | 1            |
| Jan 2027   | NA          | B      | 1            |
| Feb 2027   | NA          | B      | 1            |
| Mar 2027   | NA          | B      | 1            |
| Apr 2027   | NA          | B      | 1            |
| May 2027   | NA          | B      | 1            |
| Jun 2027   | NA          | B      | 1            |
| Jul 2027   | NA          | B      | 1            |
| Aug 2027   | NA          | B      | 1            |
| Sep 2027   | NA          | B      | 1            |
| Oct 2027   | NA          | B      | 1            |
| Nov 2027   | NA          | B      | 1            |
| Dec 2027   | NA          | B      | 1            |
| Jan 2028   | NA          | B      | 1            |
| Feb 2028   | NA          | B      | 1            |
| Mar 2028   | NA          | B      | 1            |
| Apr 2028   | NA          | B      | 1            |
| May 2028   | NA          | B      | 1            |
| Jun 2028   | NA          | B      | 1            |
| Jul 2028   | NA          | B      | 1            |
| Aug 2028   | NA          | B      | 1            |
| Sep 2028   | NA          | B      | 1            |
| Oct 2028   | NA          | B      | 1            |
| Nov 2028   | NA          | B      | 1            |
| Dec 2028   | NA          | B      | 1            |
| Jan 2029   | NA          | B      | 1            |
| Feb 2029   | NA          | B      | 1            |
| Mar 2029   | NA          | B      | 1            |
| Apr 2029   | NA          | B      | 1            |
| May 2029   | NA          | B      | 1            |
| Jun 2029   | NA          | B      | 1            |
| Jul 2029   | NA          | B      | 1            |
| Aug 2029   | NA          | B      | 1            |
| Sep 2029   | NA          | B      | 1            |
| Oct 2029   | NA          | B      | 1            |
| Nov 2029   | NA          | B      | 1            |
| Dec 2029   | NA          | B      | 1            |
| Jan 21    | NA          | B      | 1            |
| Feb 21    | NA          | B      | 1            |
| Mar 21    | NA          | B      | 1            |
| Apr 21    | NA          | B      | 1            |
| May 21    | NA          | B      | 1            |
| Jun 21    | NA          | B      | 1            |
| Jul 21    | NA          | B      | 1            |
| Aug 21    | NA          | B      | 1            |
| Sep 21    | NA          | B      | 1            |
| Oct 21    | NA          | B      | 1            |
| Nov 21    | NA          | B      | 1            |
| Dec 21    | NA          | B      | 1            |
| Jan 22    | NA          | B      | 1            |
| Feb 22    | NA          | B      | 1            |
| Mar 22    | NA          | B      | 1            |
| Apr 22    | NA          | B      | 1            |
| May 22    | NA          | B      | 1            |
| Jun 22    | NA          | B      | 1            |
| Jul 22    | NA          | B      | 1            |


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
