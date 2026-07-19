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
# Company Intuitive Surgical

Rating Sell

North America United States

Health Care Medical Supplies & Devices

Reuters
ISRG.OQ

Bloomberg
ISRG US

Exchange NMS

Ticker
ISRG

Date 17 July 2026

## Forecast Change

<table><tr><td>Price at 16 Jul 2026 (USD)</td><td>402.33</td></tr><tr><td>Price Target</td><td>324.00</td></tr><tr><td>52-week range</td><td>592.85 - 379.50</td></tr></table>

# Choppy 2Q; maintain SELL and lower PT to \$324

## Portfolio Manager Summary

While 2Q WW procedure growth of +15% came in more or less in line with consensus, US volume growth of +12% fell short of expectations even despite having been tempered post HCA's preannouncement earlier this week, which showed weak inpatient and outpatient surgery volumes. While HCA attributed this weakness mainly to ACA premium subsidy cuts, we subsequently got more reassuring results and commentary from both J&J and Abbott – with neither citing any meaningful hit to their procedure volume-sensitive businesses from these cuts (and UNH remarking this morning that utilization held fairly steady in 2Q) – precipitating a relief rally for medtech stocks.

However, this week's roller-coaster ride now promises to continue post-ISRG's results, with management positing that ACA subsidy cuts drove slower-than-expected US da Vinci volume growth based on an observed sequential deceleration across several major elective/deferrable robotic surgery categories including benign hysterectomy, cholecystectomy, and hernia repair. Given this dynamic, procedure guidance was maintained, with full-year WW volume growth trending toward the midpoint of the $+13.5\%$ to $+15.5\%$ range. This lack of procedure upside is notable and will likely disappoint investors, given the company's long and consistent history of beating and raising. We lower our full-year US and WW procedure growth forecasts to $+12.1\%$ (down 110bps) $+14.9\%$ (down 30bps), respectively.

On systems, gross placements comfortably bettered consensus (468 vs. 446), reflecting continued healthy US demand for dV5. However, net installed base growth has clearly slowed over the past few quarters, and we continue to model further deceleration going forward. Notably, installations within the ASC channel are gaining nice momentum, thanks to launch of XiR into this more cost-sensitive channel, which should help drive higher technology adoption for simpler cases that are increasingly being performed in this site of care.

International installations were in line, though continued weakness in China placements is highly noteworthy, given that this market had previously been a key driver of OUS systems and procedure growth. While the company had placed 55–60 units in China in each of the past few years, only two systems were installed in 2Q and just six YTD vs 29 in 1H25, as the da Vinci tender win rate continues to

## Valuation & Risks

Imron Zafar Research Analyst +1-212-250-3676

Pito Chickering Research Analyst +1-917-635-9954

Kieran Ryan
Research Analyst
+1-212-250-6879

Ben Shaver
Research Associate
+1-212-250-9926

<table><tr><td colspan="4">Key changes</td></tr><tr><td>TP</td><td colspan="2">366.00 to 324.00 ↓</td><td>-11.5%</td></tr><tr><td>EPS (USD)</td><td colspan="2">10.43 to 10.88 ↑</td><td>4.3%</td></tr><tr><td>Revenue (USDm)</td><td colspan="2">11,552 to 11,747 ↑</td><td>1.7%</td></tr><tr><td colspan="4">Source: DB</td></tr></table>

decline amidst intensifying competition from domestically-made platforms. On the procedure side, while China technology adoption had been meaningfully accretive to consolidated volume growth, the dramatic slowdown in installed base expansion is now resulting in decelerating procedure growth as capacity utilization maxes out. In India, while 2Q volumes were notably strong, our recent checks with large Indian hospital systems point to continued installed base share gains by lower-cost systems made in India and China. We will be meeting with several Asian competitors next week at SRS to better understand the competitive landscape in these two key OUS robotic surgery markets. dV5 did receive Indian regulatory approval earlier this week, though we foresee fairly limited uptake of the premium-priced robot in this highly cost-sensitive market.

In the I&A segment, as noted in the May press release, the company expects to begin launching Extended Use round two in the first half of 2027, which will enable customers to perform more surgeries per instrument for a handful of high-volume devices. The company did not provide much additional detail on the call, such as the number of instruments impacted or additional number of uses per unit, making it impossible to quantify the financial impact on the all-important I&A revenue-per-procedure line in 2027 and beyond. But based on the first round of Extended Use in 2021, which negatively impacted revenue per procedure by \~7%, it is fair to assume that this round will likewise exert meaningful pressure on this key model input over the next couple of years. Management's strategic rationale here is that the lower price point will drive higher adoption of robotic surgery, with which we concur – though our strong suspicion is that this was also a defensive move to help mitigate the impact from lower-cost remanufactured instruments and as more surgical robots are commercially launched in the US over the next couple of years. Regardless, bottom line is that launch of Extended Use round two will exert a meaningful hit to top-line growth in 2027–28.

On remanufactured instruments, while management continues to downplay this risk factor to its crown-jewel I&A business, our checks continue to confirm significant interest and growing adoption by hospitals, given the sizable discount vs. de novo instruments. In speaking with several major robotics programs, including HCA, Intuitive's largest US customer, adoption of the remanufactured monopolar scissors, the largest I&A SKU at \~14% of segment sales, continues to increase – and which we estimate has now captured \~5%–7% share of this product category. As several additional remanufactured instruments receive FDA approval and launch in coming quarters, we believe this will increasingly start to weigh on Intuitive's top line, specifically I&A per procedure, in 2027 and especially 2028.

Hence, with the deep moat that has heretofore surrounded the I&A segment—and justified the massive valuation premium for ISRG shares—increasingly at risk, and now coupled with growing questions around weakening fundamentals, including slowing US procedure growth, intensifying competition in key OUS markets such as China, and hospital margin pressures that could lead to capex budget cuts, we remain Sell-rated on ISRG shares and lower our PT to \$324 vs \$366 previously based on our valuation framework that continues to assume a 75% PEG premium vs a peer group of high-quality large-cap medtech peers (SYK, EW, and MDLN).

Upside risks to our target valuation include commercial execution missteps by third-party remanufacturers, lower-than-expected adoption of remanufactured instruments, and meaningful fundamental upside to procedure growth and/or dV5 placements and net installed base growth.

## Appendix 1

## Important Disclosures

\*Other information available upon request

<table><tr><td colspan="4">Disclosure checklist</td></tr><tr><td>Company</td><td>Ticker</td><td>Recent price*</td><td>Disclosure</td></tr><tr><td>Intuitive Surgical</td><td>ISRG.OQ</td><td>402.33 (USD) 16 Jul 2026</td><td>2, 14, 24</td></tr></table>

\*Prices are current as of the end of the previous trading session unless otherwise indicated and are sourced from local exchanges via Reuters, Bloomberg and other vendors. Other information is sourced from DB, subject companies, and other sources. For disclosures pertaining to recommendations or estimates made on securities other than the primary subject of this research, please see the most recently published company report or visit our global disclosure look-up page on our website at https://research.db.com/Research/Disclosures/EquityResearchDisclosures. Aside from within this report, important risk and conflict disclosures can also be found at https://research.db.com/Research/Disclosures/Disclaimer. Investors are strongly encouraged to review this information before investing.

## Important Disclosures Required by U.S. Regulators

Disclosures marked with an asterisk may also be required by at least one jurisdiction in addition to the United States. See Important Disclosures Required by Non-US Regulators and Explanatory Notes.

2. DB and/or its affiliate(s) may act as a market maker or liquidity provider in the financial instruments issued by this company.

14. DB and/or its affiliate(s) has received compensation from this company within the past year for non-investment banking related services.

## Important Disclosures Required by Non-U.S. Regulators

Disclosures marked with an asterisk may also be required by at least one jurisdiction in addition to the United States. See Important Disclosures Required by Non-US Regulators and Explanatory Notes.

2. DB and/or its affiliate(s) may act as a market maker or liquidity provider in the financial instruments issued by this company.

24. DB and/or its affiliate(s) is or has been over the previous 12 months party to an agreement with the company relating to the provision of services set out in Sections A and B of Annex I of Directive 2014/65/EU, or has over the previous 12 months been obliged or entitled (as applicable) to pay or receive compensation relating to the provision of services set out in Sections A and B of Annex I of Directive 2014/65/EU.

For disclosures pertaining to recommendations or estimates made on securities other than the primary subject of this research, please see the most recently published company report or visit our global disclosure look-up page on our website at https://research.db.com/Research/Disclosures/EquityResearchDisclosures. Aside from within this report, important risk and conflict disclosures can also be found at https://research.db.com/Research/Disclosures/Disclaimer. Investors are strongly encouraged to review this information before investing.

## Analyst Certification

The views expressed in this report accurately reflect the personal views of the undersigned lead analyst(s) about the subject issuer and the securities of the issuer. In addition, the undersigned lead analyst(s) has not and will not receive any compensation for providing a specific recommendation or view in this report. Imron Zafar.

![](images/6881852ae9307617caf73269f24704647d0ac61ce79accb164caa85627fd9877.jpg)

<table><tr><td>1.</td><td>07/21/2023</td><td>Hold, Target Price Change USD 335.00, Current Price USD 336.66 Imron Zafar</td><td>6.</td><td>10/18/2024</td><td>Hold, Target Price Change USD 505.00, Current Price USD 521.15 Imron Zafar</td></tr><tr><td>2.</td><td>10/20/2023</td><td>Hold, Target Price Change USD 275.00, Current Price USD 266.91 Imron Zafar</td><td>7.</td><td>01/24/2025</td><td>Hold, Target Price Change USD 585.00, Current Price USD 584.05 Imron Zafar</td></tr><tr><td>3.</td><td>01/24/2024</td><td>Hold, Target Price Change USD 370.00, Current Price USD 370.07 Imron Zafar</td><td>8.</td><td>04/23/2025</td><td>Hold, Target Price Change USD 515.00, Current Price USD 487.93 Imron Zafar</td></tr><tr><td>4.</td><td>04/19/2024</td><td>Hold, Target Price Change USD 390.00, Current Price USD 366.34 Imron Zafar</td><td>9.</td><td>06/08/2025</td><td>Downgraded to Sell, Target Price Change USD 440.00, Current Price USD 557.08 Imron Zafar</td></tr><tr><td>5.</td><td>07/19/2024</td><td>Hold, Target Price Change USD 445.00, Current Price USD 455.01 Imron Zafar</td><td>10.</td><td>06/02/2026</td><td>Sell, Target Price Change USD 366.00, Current Price USD 402.30 Imron Zafar</td></tr></table>

Equity rating dispersion and banking relationships  
![](images/2a82de127e210fa19892702ad09cf51ea3fecb6b63bd99c935ccf63a0b0abd85.jpg)  
Equity Rating and Dispersion Key  
The Equity Rating Dispersion Chart depicts the following:

The proportion of recommendations that are rated "buy", "sell" and "hold" over the previous 12 months. This is shown for securities issued in the stated region e.g. "Europe Universe". See rating definitions below. This is represented by the "Companies Covered" bars in the chart. The percentage value displayed above the bar is the proportion as a percentage. E.g. $50\%$ above the "buy" / "Companies Covered" bar means that $50\%$ of DB's equity research covered companies over the past 12 months have a "buy" rating.

Next to each of the three respective bars showing the proportion of "buy", "sell" and "hold" recommendations we provide two additional bars to show:

\- The proportion of "buy", "sell" or "hold recommendations where DB and or/Affiliates provided MIFID Investment or Ancillary Services in the past 12 months. This is represented in the "MIFID Investment and Ancillary Services" bar. The percentage value displayed above the bar shows the proportion of Companies Covered with the given rating where DB has also provided MIFID Investment and Ancillary Services in the past 12 months. E.g. $50\%$ above the "Cos. w/ MIFID Investment and Ancillary Services" bar means $50\%$ of the Companies Covered with the rating stated have also received MIFID Investment and Ancillary Services from DB.

\- The proportion of "buy" (or "sell" or "hold) recommendations where DB and or/Affiliates has provided Investment Banking services in the past 12 months for which it has received compensation. The percentage value displayed above the bar shows the proportion of Companies Covered with the stated rating where DB has also provided Investment Banking services in the past 12 months. E.g. $50\%$ above the "Cos. w/ Investment Banking relationship" bar means $50\%$ of the Companies Covered with the rating stated also have an Investment Banking Relationship with DB.

Buy: Based on a current 12-month view of TSR, we recommend that investors buy the stock.

Sell: Based on a current 12-month view of TSR, we recommend that investors sell the stock.

Hold: We take a neutral view on the stock 12-months out and, based on this time horizon, do not recommend either a Buy or Sell.

TSR = Total Shareholder Return. Percentage change in share price from current price to projected target price plus projected dividend yield

Newly issued research recommendations and target prices supersede previously published research.

## Additional Information

The information and opinions in this report were prepared by DB AG or one of its affiliates (collectively 'DB'). Though the information herein is believed to be reliable and has been obtained from public sources believed to be reliable, DB makes no representation as to its accuracy or completeness. Hyperlinks to third-party websites in this report are provided for reader convenience only. DB neither endorses the content nor is responsible for the accuracy or security controls of those websites.

If you use the services of DB in connection with a purchase or sale of a security that is discussed in this report, or is included or discussed in another communication (oral or written) from a DB analyst, DB may act as principal for its own account or as agent for another person.

DB may consider this report in deciding to trade as principal. It may also engage in transactions, for its own account or with customers, in a manner inconsistent with the views taken in this research report. Others within DB, including strategists, sales staff and other analysts, may take views that are inconsistent with those taken in this research report. DB issues a variety of research products, including fundamental analysis, equity-linked analysis, quantitative analysis and trade ideas.

[中间内容因长度限制已省略]

lue for their personal use from issuers they cover.

Additional information relative to securities, other financial products or issuers discussed in this report is available upon request. This report may not be reproduced, distributed or published without DB's prior written consent.

Backtested, hypothetical or simulated performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG. It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

<table><tr><td colspan="4">David Folkerts-Landau Group Chief Economist and Global Head of Research</td></tr><tr><td>Pam Finelli COO and Head of Fixed Income Research</td><td>Steve Pollard Global Head of Company Research and Sales</td><td>Jim Reid Global Head of Macro and Thematic Research</td><td>Tim Rokossa Head of European Company Research</td></tr><tr><td>Matthew Barnard Head of Americas Company Research</td><td>Debbie Jones Global Head of Sustainability and Data Innovation, Research</td><td>Robin Winkler Head of German Macro Research</td><td>Sameer Goel Global Head of EM &amp; APAC Research</td></tr><tr><td>Francis Yared Global Head of Rates Research</td><td>George Saravelos Global Head of FX Research</td><td>Peter Hooper Vice-Chair of Research</td><td>Nilendra de-Mel Head of APAC &amp; Middle East Product Development</td></tr></table>

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip</td><td>60329 Frankfurt am Main</td><td>Centre,</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Streets</td><td>Germany</td><td>1 Austin Road West,Kowloon,</td><td>Japan</td></tr><tr><td>Sydney, NSW 2000</td><td>Tel: (49) 69 910 00</td><td>Hong Kong</td><td>Tel: (81) 3 6730 1000</td></tr><tr><td>Australia</td><td></td><td>Tel: (852) 2203 8888</td><td></td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr></table>
"""
