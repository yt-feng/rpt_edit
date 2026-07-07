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
Japan Semiconductors
Sony Group Corp

Rating
Market-Perform

Price Target

6758.JP 3,500.00 JPY

SONY 22.00 USD

![](images/e35d977052065f885e23dcc81232184ef343fe1fd40859b098cdf507aa55164a.jpg)

![](images/94c0cabbe8c0ca62cbbb9ea758f7485dff693f153aaddb73d5e1b7069765070c.jpg)

Robin Zhu
+852 2123 2659
robin.zhu@bernsteinsg.com

David Dai, CFA
+852 2918 5704
david.dai@bernsteinsg.com

![](images/636c55b3bbe998a20f2e6827d299185c746b152cc37de359589b964d71f2d91b.jpg)

Jack Lin
+852 2123 2683
jack.lin@bernsteinsg.com

![](images/68799b8fece94f255a715a06aa9aa90a6ba859ddbfd5d366c3651a902d96690e.jpg)

Hyrum Caesar
+81 3 6777 6979
hyrum.caesar@bernsteinsg.com

## Sony: Thoughts on Playstation going all-digital, and fan backlash

The backlash was probably expected, does it matter? Since Sony announced on July 1 that Playstation games would be digital-only from January 2028, there's been considerable - if entirely predictable - pushback from online gamers. A Change.org petition against the decision has 109,400 signatures at the time of writing, while the Playstation tweet announcing the decision has 138mn views, and more replies than likes. While the desire to offset high memory costs represented the obvious driver of Sony's move, we've received questions from investors on backlash impact.

The financial impact of any backlash is likely manageable. To put things in perspective, Playstation generated 11.3% of FY3/26 game sales revenue from physical sales. This equaled just 4.8% of aggregate software revenues including PS Plus and off-platform revenues... and 2.3% of overall Playstation revenue. We estimate physical game sales contributed c. 3-4% of Playstation gross profit last financial year. Assuming Playstation permanently loses 30% of all physical sales - and the rest convert to digital sales would only have a 3-4% negative impact on normalised Playstation operating profit... before considering hardware cost savings. PS Plus cancellations from angry fans would actually be more impactful: 5-10% cancellations would imply a mid-single digit cut to normalised operating profit. But in aggregate we're probably talking 2-3% of Sony's group operating profit at risk, in a worst case scenario.

Maybe if gamers had bought more physical games... Physical sales ratios tend to be higher for new games at launch (e.g. 20-30%), but in some ways PlayStation's move simply brings video gaming in line with other media formats like video streaming and music, where physical editions are the domain of niche collectors. Instead of accusing preservationists and others protesting the decision of Luddism, we'll simply note that the industry has already mostly moved on, at least financially, from physical distribution. GTA VI won't have a physical edition at launch, and the new Steam Machine (released two days before PlayStation's announcement) comes with no physical disc drive. For physical media purists, there's always Nintendo's game key cards...

<table><tr><td>Reported EPS</td><td>F25A</td><td>F26E</td><td>F27E</td></tr><tr><td>6758.JP (JPY)</td><td>171.30</td><td>198.75</td><td>207.66</td></tr><tr><td>SONY (USD)</td><td>1.08</td><td>1.25</td><td>1.30</td></tr></table>

\*Values shown in billions; Source: Bloomberg, Bernstein estimates and analysis.

<table><tr><td>Close Date</td><td>3 Jul 2026</td></tr><tr><td>6758.JP Close Price (JPY)</td><td>3,380.00</td></tr><tr><td>Price Target (JPY)</td><td>3,500.00</td></tr><tr><td>Upside/(Downside)</td><td>4%</td></tr><tr><td>52-Week Range</td><td>4,776.00/3,043.00</td></tr><tr><td>JPL</td><td>2,655.16</td></tr><tr><td>FYE</td><td>Mar</td></tr><tr><td>Div Yield</td><td>1.0%</td></tr><tr><td>Market Cap (JPY) (B)</td><td>20,162.77</td></tr><tr><td>EV (JPY) (B)</td><td>20,018.14</td></tr></table>

<table><tr><td>Performance</td><td>YTD</td><td>1M</td><td>6M</td><td>12M</td></tr><tr><td>Absolute (%)</td><td>(16.0)</td><td>(4.5)</td><td>(16.0)</td><td>(5.1)</td></tr><tr><td>JPL (%)</td><td>20.3</td><td>2.5</td><td>15.5</td><td>46.1</td></tr><tr><td>Relative (%)</td><td>(36.3)</td><td>(7.0)</td><td>(31.5)</td><td>(51.2)</td></tr></table>

Source: Bloomberg, Bernstein estimates and analysis.  
Price Performance, 1YR

![](images/0f29f1bafd88894ddac1248f872d6c516326e9e7b268a3650ebf83930bacfc79.jpg)

<table><tr><td>Valuation Metrics</td><td>F25A</td><td>F26E</td><td>F27E</td></tr><tr><td>Reported P/E (x)</td><td>19.7</td><td>17.0</td><td>16.3</td></tr><tr><td>EV/EBIT (x)</td><td>13.8</td><td>12.3</td><td>12.0</td></tr><tr><td>EV/EBITDA (x)</td><td>9.0</td><td>8.2</td><td>8.3</td></tr></table>

No country for old men. It feels telling the official Playstation Twitter/X account has been silent since July 1, but we'd be shocked if the online backlash ended up impacting Sony's decision-making. If the emotional arguments against abandoning physical media boil down to "it's always been this way", or consumer choice in the abstract sense, then the facts of the business show that consumers have mostly chosen digital for a long time. Repeat game sales on console are overwhelmingly digital. Steam has outgrown the PC market for years as a digital-first ecosystem, and we're still sometimes reminded by investors that the kids just play Roblox. More pragmatically, even the loss of some physical sales at launch might be excusable given publishers avoid paying retailer margins on sales that convert to digital, and gain more control over repeat pricing. We're obviously biased, but it feels hard to fault the video gaming industry for taking price, considering it's long remained the cheapest form of entertainment on a per-hour basis.

Implications for PS6. In our view, Sony's announcement all but confirms that (1) the PS6 won't launch before January 2028 (our base case is an early 2028 announcement for launch during the holiday period that year); and (2) Sony's next-generation console will come without a disc drive. There's some irony in the fact that the video game console that got its start thanks to (at the time revolutionary...) CD-ROMs became the one to abandon physical media... as opposed to, say, Xbox. But a single digital-only PS6 SKU should on the margin be positive for hardware margins. Our base case remains a PS5-to-PS6 transition that lasts at least as long as the PS4-to-PS5 one, given the impact of high memory costs, and the diminishing impact graphical fidelity now has on game quality.

## INVESTMENT IMPLICATIONS

We rate Sony Market-Perform (PT ¥3,500).

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2"></td><td rowspan="2"></td><td colspan="3">3 Jul 2026</td><td colspan="2">TTM</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td></td><td rowspan="2">Closing Price</td><td rowspan="2">Price Target</td><td rowspan="2">Rel. Perf.</td><td rowspan="2">Cur</td><td rowspan="2">2025A</td><td rowspan="2">2026E</td><td rowspan="2">2027E</td><td rowspan="2">2025A</td><td rowspan="2">2026E</td><td rowspan="2">2027E</td><td></td></tr><tr><td>Ticker</td><td>Rating</td><td>Cur</td><td></td></tr><tr><td>6758.JP (Sony)</td><td>M</td><td>JPY</td><td>3,380.00</td><td>3,500.00</td><td>(51.2)%</td><td>JPY</td><td>171.30</td><td>198.75</td><td>207.66</td><td>19.7</td><td>17.0</td><td>16.3</td><td></td></tr><tr><td>SONY (Sony )</td><td>M</td><td>USD</td><td>20.79</td><td>22.00</td><td>(35.8)%</td><td>USD</td><td>1.08</td><td>1.25</td><td>1.30</td><td>19.3</td><td>16.6</td><td>16.0</td><td></td></tr><tr><td>JPL</td><td></td><td></td><td>2,655.16</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SPX</td><td></td><td></td><td>7,483.24</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended Source: Bloomberg, Bernstein estimates and analysis.

## I. REQUIRED DISCLOSURES

References to "Bernstein" or the "Firm" in these disclosures relate to the following entities: Bernstein Institutional Services LLC (April 1, 2024 onwards), Bernstein & Co., LLC (pre April 1, 2024), Bernstein Autonomous LLP, BSG France S.A. (April 1, 2024 onwards), Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited, Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社) and analysts employed by SG Africa Technologies & Services to produce Bernstein under a Global Services Agreement in place between Bernstein and SG.

Bernstein is part of a joint venture between SG (SG) and AllianceBernstein, L.P. (AB). Unless specifically noted otherwise, for purposes of these disclosures, references to Bernstein's “affiliates” relate to both SG and AB and their respective affiliates.

## VALUATION METHODOLOGY

## Sony Group Corp

We have a ¥3,500 price target for Sony, based on a 17x P/E multiple of Q5-8 EPS, estimated at ¥208. We value the Sony ADR by converting the JPY price to USD based on an exchange rate of 159.21.

## RISKS

## Sony Group Corp

Upside risks to our Sony target price: (1) A smaller-than-expected memory price hike; (2) A smaller-than-expected share loss to Samsung in Apple CIS orders; (3) Stronger-than-expected game software sales. Downside risks: (1) Fewer mobile/auto CIS sales or larger share loss in CIS market; (2) Slowdown of music streaming market growth or less profit sharing from streaming; (3) Management risk and competition in anime streaming or insufficient successful anime works in the future.

## RATINGS DEFINITIONS, BENCHMARKS AND DISTRIBUTION

## EQUITY RATINGS DEFINITIONS

## Bernstein brand

The Bernstein brand rates stocks based on forecasts of relative performance for the next 12 months versus the S&P 500 for stocks listed on the U.S. and Canadian exchanges, versus the Bloomberg Europe Developed Markets Large and Mid Cap Price Return Index EUR (EDME) for stocks listed on the European exchanges and emerging markets exchanges outside of the Asia Pacific region, versus the Bloomberg Japan Large and Mid Cap Price Return Index USD (JPL) for stocks listed on the Japanese exchanges, and versus the Bloomberg Asia ex-Japan Large and Mid Cap Price Return Index (ASIAX) for stocks listed on the Asian (ex-Japan) exchanges -unless otherwise specified.

The Bernstein brand has three categories of ratings:

\- Outperform: Stock will outpace the market index by more than 15 pp

• Market-Perform: Stock will perform in line with the market index to within +/-15 pp

• Underperform: Stock will trail the performance of the market index by more than 15 pp

Coverage Suspended: Coverage of a company under the Bernstein brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Not Covered (NC) denotes companies that are not under coverage.

Bernstein brand stock ratings are based on a 12-month time horizon.

## Autonomous brand – common stocks

The Autonomous brand rates common stocks as indicated below. As our benchmarks we use the Bloomberg Europe 500 Banks And Financial Services Index (BEBANKS) and Bloomberg Europe Dev Mkt Financials Large and Mid Cap Price Ret Index EUR (EDMFI) index for developed European banks and Payments, the Bloomberg Europe 500 Insurance Index (BEINSUR) for European insurers, the S&P 500 and S&P Financials for US banks and Payments coverage, S5LIFE for US Insurance, the S&P Insurance Select Industry (SPSIINS) for US Non-Life Insurers coverage, and the Bloomberg Emerging Markets Financials Large, Mid and Small Cap Price Return Index (EMLSF) for emerging market banks and insurers and Payments. Ratings are stated relative to the sector (not the market).

The Autonomous brand has three categories of common stock ratings:

\- Outperform (OP): Stock will outpace the relevant index by more than 10 pp

\- Neutral (N): Stock will perform in line with the market index to within +/-10 pp

\- Underperform (UP): Stock will trail the performance of the relevant index by more than 10 pp

Coverage Suspended: Coverage of a company under the Autonomous research brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Those denoted as ‘Feature’ (e.g., Feature Outperform FOP, Feature Under Outperform FUP) are our core ideas.

Not Covered (NC) denotes companies that are not under coverage.

Autonomous brand common stock ratings are based on a 12-month time horizon.

## Autonomous brand – preferred stocks

The Autonomous brand has three categories of preferred stock ratings:

\- Outperform (OP): The total return of the preferred instrument is expected to outperform preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

\- Neutral (N): The total return of the preferred instrument is expected to perform in line with preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

\- Underperform (UP): The total return of the preferred instrument is expected to underperform preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

Autonomous preferred stock ratings are based on a 6-month time horizon.

## AUTONOMOUS CREDIT RESEARCH

Where this report contains investment recommendations for credit instruments, as defined in article 3(1)(35) of the Market Abuse Regulation, the information below is presented to comply with its disclosure requirements.

The report may also include reference(s) to published opinions by other Autonomous or Bernstein analysts covering the equity securities of the issuer(s) referenced herein. Please note an investment recommendation for credit instruments published by the author(s) of this report may differ from the published view of the analyst covering equity securities for the issuer(s) contained in this report and vice versa.

## CREDIT RATINGS DEFINITIONS

The Autonomous brand has three categories of credit ratings:

\- Credit Outperform (C-OP): The total return of the Reference Credit Instrument is expected to outperform the credit spread of bonds of other issuers operating in similar sectors or rating categories over the next six months.

\- Credit Neutral (C-N): The total return of the Reference Credit Instrument is expected to perform in line with the credit spread of bonds of other issuers operating in similar sectors or rating categories over the next six months.

\- Credit Underperform (C-UP): The total return of the Reference Credit Instrument is expected to underperform the credit spread of bonds of other issuers operating in similar sectors or rating categories over the next six months.

Autonomous credit ratings are based on a 6-month time horizon.

A list of all investment recommendations produced by the author(s) of this report alongside credit ratings history are available upon request.

It is at the sole discretion of the Firm as to when to initiate, update and cease research coverage. The Firm has established, maintains and relies on information barriers to control the flow of information contained in one or more areas (i.e. the p

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
