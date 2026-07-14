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
# China Brokers & Asset Managers: Strong 2Q earnings as expected, likely 3Q momentum supported by ROE recovery

Recent 1H26 earnings pre-announcements from Chinese brokers point to another quarter of strong performance. Across the nine brokers that have disclosed guidance, average net profit growth is approximately $155\%$ YoY, with CICC and CITICS reporting YoY growth of $78\%-90\%$ and $70\%$ , respectively.

Shuo Yang, Ph.D. +852-2978-0701 | shuo.yang@gs.com GS (Asia) L.L.C.

Claire Ouyang  
+852-2978-6686 |  
claire.x.ouyang@gs.com  
GS (Asia) L.L.C.

The earnings strength was primarily supported by continued momentum across both primary and secondary capital markets. A-share ADTV reached a record Rmb 2.9tn in 2Q26, while margin financing balances exceeded Rmb 3tn, reflecting sustained investor participation and supporting brokerage commissions and interest income. At the same time, A-share IPO issuance rose to Rmb 66bn, the highest level since 2024, while Hong Kong IPO activity remained robust due to a healthy project pipeline.

Looking into 3Q26, key areas to monitor include the sustainability of trading activity and IPO issuance, progress in capital deployment toward Hong Kong operations, and potential earnings contributions from upcoming technology listings. CICC management commentary suggests market activity remains resilient, while several brokers continue to expand their international platforms through capital injections and strategic transactions.

We maintain a preference for CICC-H and CITICS-A, given their leading positions in Hong Kong capital markets, growing international operations, and potential for medium-term ROE improvement through balance-sheet expansion and overseas business growth. CICC continues to benefit from its scale in Hong Kong investment banking and equities businesses, while CITICS is advancing its international expansion strategy through additional capital deployment, providing further flexibility for leverage optimization and business growth.

Recently, several brokers have released positive 1H26 profit alerts, with overall strong performance. The nine brokers that have disclosed their results reported average YoY net profit growth of approximately $155\%$ . Among them, CICC expects to see YoY growth of $78\% - 90\%$ , while CITICS anticipates YoY growth of $70\%$ . Based on calculations from the profit alert ranges, CICC's implied 2Q26 net profit is approximately Rmb 4.1-4.6bn, representing a YoY increase of $81\% - 103\%$ and a QoQ increase of $15\% - 30\%$ , $+61\% - 81\%$ higher than GSe. CITICS's implied 2Q26 net profit is Rmb 13.1bn, a YoY increase of $82\%$ and a QoQ increase of $28\%$ , which is $56\%$ higher than GSe.

We believe the broker sector's strong 2Q26 performance is largely in line with market expectations, primarily driven by sustained activity in both primary and secondary markets: 1) Trading sentiment in the A-share market remained high, with the 2Q26 ADTV reaching a historical high of Rmb 2.9tn and market turnover rate rising to $648\%$ . Concurrently, the balance of margin financing and securities lending surpassed Rmb 3tn, a YoY increase of $63\%$ , reflecting a continuous improvement in investor risk appetite and driving growth in brokerage commission and interest income. 2) Capital market financing activities showed a significant recovery. The A-share IPO fundraising volume reached Rmb 66bn, a YoY increase of $206\%$ , setting a new high since 2024 and indicating that the recovery trend in the IPO market is continuing. At the same time, the Hong Kong IPO market maintained a high level of activity, supported by a robust project pipeline, which provided strong support for investment banking revenue growth.

Looking ahead to 3Q26, we believe the industry's profitability is likely to continue the positive momentum from 2Q; however, several factors still require close attention: 1) The sustainability of market activity. According to feedback from CICC's management, there are currently no signs of a slowdown in either market trading volume or the pace of IPO project progression, with a substantial pipeline of projects still set for release in the second half of the year. 2) Progress on capital investment in international business. CICC has indicated that its M&A transaction is expected to be completed in 3Q26. Post-completion, CICC expects the capital base to double, creating the conditions for a further pivot towards businesses with higher returns on capital and the company notes this could potentially initiate a long-term cycle of ROE enhancement. 3) Investment income opportunities from the listings of technology companies. As technology leaders like CXMT advance their listing processes, the investment gains that brokers have secured through early-stage equity investments and STAR Board co-investments are expected to be further realized per market and our expectations. However, this could also simultaneously lead to increased earnings volatility, in our view.

We reiterate our Buy ratings on CICC-H and CITICS-A. CICC remains one of the Chinese brokers with the most significant international advantages. According to management, the revenue and profit contributions from the company's Hong Kong business are at industry-leading levels. Notably, its market share in Hong Kong's investment banking business is holding at 25%-30%, its equities business possesses a significant competitive advantage, and its asset management and wealth management businesses are also experiencing rapid growth. Year-to-date, the company has injected approximately Rmb 100bn into its Hong Kong operations. Following the completion of the M&A, management expect its capital strength to be further enhanced, unlocking potential for long-term ROE upside. Meanwhile, as the major shareholder's private placement is gradually implemented, CITICS said capital investment in its international business will also accelerate, providing greater room for balance sheet expansion, leverage

enhancement, and ROE improvement.

Exhibit 1: The nine brokers that have disclosed their results reported an average YoY net profit growth of approximately 155%.

<table><tr><td colspan="2">1H26 NPAT</td><td>yoy</td></tr><tr><td colspan="3">Top players</td></tr><tr><td>国泰海通</td><td>Guotai Haitong</td><td>164%-171%(ex. NRI)</td></tr><tr><td>CMS</td><td>CMS</td><td>93%-112%</td></tr><tr><td>CICC</td><td>CICC</td><td>78%-90%</td></tr><tr><td>CITIC</td><td>CITICS</td><td>70%</td></tr><tr><td colspan="3">Others</td></tr><tr><td>天风证券</td><td>TF Sec.</td><td>429%-694%</td></tr><tr><td>中泰证券</td><td>Zhongtai Sec.</td><td>146%</td></tr><tr><td>财达证券</td><td>Caida Sec.</td><td>90%-116%</td></tr><tr><td>长江证券</td><td>Changjiang Sec.</td><td>80%-90%</td></tr><tr><td>财通证券</td><td>Caitong Sec.</td><td>70%-80%</td></tr><tr><td colspan="2">Average</td><td>155%</td></tr></table>

Source: Company data, Data compiled by GS Global Investment Research

Exhibit 2: Among them, CICC expects to see YoY growth of $78\% -90\%$ , while CITICS anticipates YoY growth of $70\%$ .

<table><tr><td>Attributable NPAT(Rmb bn)</td><td>2Q25</td><td>1Q26</td><td>2Q26E</td><td>2Q26 Implied</td><td>YoY</td><td>QoQ</td><td>vs. G Se</td><td>1H26 Prelim</td><td>YoY</td><td>vs. G Se</td></tr><tr><td>CICC</td><td>2.3</td><td>3.6</td><td>2.6</td><td>4.1~4.6</td><td>81%~103%</td><td>15%~30%</td><td>61%~81%</td><td>7.7~8.2</td><td>78%~90%</td><td>26%~34%</td></tr><tr><td>CITICS</td><td>7.2</td><td>10.2</td><td>8.4</td><td>13.1</td><td>82%</td><td>28%</td><td>56%</td><td>23.3</td><td>70%</td><td>25%</td></tr></table>

Source: Company data, GS Global Investment Research  
Exhibit 3: Trading sentiment in the A-share market remained high, with 2Q26 ADTV reaching a historical high of Rmb 2.9tn and market turnover rate rising to 648%.

![](images/7abe90922e1f491674855db728d253d53f914791295d48bf778aa3532ebf4387.jpg)  
Source: Wind  
Exhibit 4: The balance of margin financing and securities lending surpassed Rmb 3tn, a YoY increase of 63%, reflecting a continuous improvement in investor risk appetite.

![](images/1b431b650df43790d8bd7d33ec6ecf652e8954d1c42f6248faf3da70f73cacf2.jpg)  
Source: Wind

Exhibit 5: A-share IPO fundraising volume reached Rmb 66bn, a YoY increase of 206%, setting a new high since 2024 and indicating that the recovery trend in the IPO market is continuing.

![](images/2c576a6bd2b077a431b8762e30f75eaf268da9ac4bcea3f6b902986288ea9242.jpg)  
Source: Wind

Exhibit 6: The Hong Kong IPO market maintained a high level of activity, supported by a robust project pipeline.

![](images/53371b561aeab26c266cf1c86dfcfce0828e8a3c6e8b893c0e055ea310b4ebbd.jpg)  
Source: HKEX

## Price Target Risks and Methodology - China International Capital Corp.

We are Buy/Neutral on CICC-H/CICC-A. Our 12-month target prices of HK\$ 30.45/Rmb 45.72 are based on 11x/18x 2027E P/Es.

Downside risks: 1) weaker-than-expected China capital market, 2) OTC derivative losses, 3) decreased AUM and fee rate, 4) higher cost income ratio.

Upside risks for A shares: 1) improving brokerage fee and IBD income, 2) increasing OTC derivative business and income growth, 3) more cost savings to support ROE.

## Price Target Risks and Methodology - CITIC Co.

We are Buy/Neutral on CITICS A/H. Our 12-month target prices of Rmb 39.96/HK\$ 29.95 are based on 16x/11x 2027E P/Es.

Downside Risks: 1) further slower revenue growth on weaker capital market, 2) decreasing AUM and take rate of asset management business, 3) slower growth of investment income, 4) more operating expense to keep cost income ratio high.

Upside risks for H share: 1) improving capital market and higher ADTV to drive core business growth, 2) further greater than expected cost savings.

## Disclosure Appendix

## Reg AC

We, Shuo Yang, Ph.D. and Claire Ouyang, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Shuo Yang, Ph.D. GS (Asia) L.L.C., Claire Ouyang GS (Asia) L.L.C..

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

The rating(s) for CITIC Co. (H), CITIC Co.(A), China International Capital Corp. (A) and China International Capital Corp. (H) is/are relative to the other companies in its/their coverage universe: CITIC Co. (H), CITIC Co.(A), China International Capital Corp. (A), China International Capital Corp. (H), East Money Information Co., Futu Holdings, GF Securities Co. (A), GF Securities Co.(H), Hundsun, UP Fintech Holding

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS beneficially owned 1% or more of common equity (excluding positions managed by affiliates and business units not required to be aggregated under US securities law) as of the month end preceding this report: China International Capital Corp. (A) (Rmb35.37) and China International Capital Corp. (H) (HK\$21.12)

GS has received compensation for investment banking services in the past 12 months: China International Capital Corp. (A) (Rmb35.37) and China International Capital Corp. (H) (HK\$21.12)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: China International Capital Corp. (A) (Rmb35.37), China International Capital Corp. (H) (HK\$21.12), CITIC Co. (H) (HK\$26.72) and CITIC Co.(A) (Rmb28.12)

GS has received compensation for non-investment banking services during the past 12 months: China International Capital Corp. (A) (Rmb35.37), China International Capital Corp. (H) (HK\$21.12), CITIC Co. (H) (HK\$26.72) and CITIC Co.(A) (Rmb28.12)

GS had an investment banking services client relationship during the past 12 months with: China International Capital Corp. (A) (Rmb35.37), China International Capital Corp. (H) (HK\$21.12), CITIC Co. (H) (HK\$26.72) and CITIC Co.(A) (Rmb28.12)

GS had a non-investment banking securities-related services client relationship during the past 12 months with: China International Capital Corp. (A) (Rmb35.37), China International Capital Corp. (H) (HK\$21.12), CITIC Co. (H) (HK\$26.72) and CITIC Co.(A) (Rmb28.12)

GS had a non-securities services client relationship during the past 12 months with: Ch

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
