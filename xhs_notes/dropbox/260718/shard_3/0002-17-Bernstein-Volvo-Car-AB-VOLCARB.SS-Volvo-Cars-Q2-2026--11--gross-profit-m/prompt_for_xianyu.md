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
European Automobiles & Components
Volvo Car AB

Rating
Underperform

Price Target
E VOLCARB.SS

17.00 SEK

![](images/69502a137d584ec223b76912403edbe8e14a40ae72a35df88c7836810cbd31b8.jpg)

![](images/3a619cf016191babeb882291574c4d39ee6ba952577936255a3bec9dfd4b1d8d.jpg)

Harry Martin, CFA
+44 20 7676 8965
harry.martin@bernsteinsg.com

![](images/4647d0fbd7ec5d3a946cba44ad9fdde37aa11ca60d28a035e9bf3f1e67966ca3.jpg)

Steve Pereira Fernandes, CFA
+44 20 7676 7254
steve.pereira-fernandes@bernsteinsg.com

![](images/fa6a8b88254b333eaddf0b559fd664e9b4d67128f876b2b9d0e6755194fdc07a.jpg)

Gali Salvatorelli Naraghi
+44 20 7676 6741
gali.salvatorelli-naraghi@bernsteinsg.com

Stephen Reitman
+44 20 7762 5535
stephen.reitman@bernsteinsg.com

# Volvo Cars Q2 2026: 11% gross profit miss, 25% EBIT miss. Company still expects materially better H2

Volvo Cars reported Q2 results this morning. Conference call 8:00am CEST/7:00am UK time.

Overall take. After the pre-close briefing call (Link) outlined a Q2 which would be hit by cost inflation and discounting as well as the tough China market, an 11% gross profit miss and 25% EBIT miss should perhaps come as little surprise. We went into the quarter meaningfully below consensus and the results are slightly better than our expectations for a 16% gross margin (actual 16.8%). Much lower R&D expenses also meant EBIT beat our forecast of slightly below breakeven. FCF burn was -€5bn SEK (consensus had positive FCF) but the company still expects approximately breakeven for the FY, where it will launch new models and unwind some of the inventory build. CMD also planned for September in Stockholm.

\- The quarter. Volvo reported revenue of SEK 77.7bn, missing consensus by 6%, gross margin of 16.8%, 90 bps below consensus, and EBIT excl. items affecting comparability of SEK 826mn, a significant (25%) miss to consensus. The decrease was driven by a combination of lower underlying wholesale volumes, weaker sales mix and pricing, FX effects, and a one-off sale of SEK 3.3 bn in 2Q25 that boosted last year's figures.

\- Retail sales were overall down 6% YoY, largely driven by a 37% decline in China, but were flat and up 9% in Europe and the US respectively. The US is said to be showing signs of a recovery in H2 after growth in May and June. In Europe, pricing pressure remains.

\- EBIT decline was mainly down to less favorable sales mix and pricing, weaker wholesale volumes, negative D&A effects, as well as lower revenue benefits from emission credits (SEK 0.8bn vs 1.7bn in 2Q25).

\- Volvo's free cash outflow of SEK 5.2bn was considerably below consensus (1.9bn inflow). Compared to our model which had a large working capital outflow, Volvo saw a minor working capital inflow.

\- Outlook. Volvo indicated that they expect “significantly stronger” sales in H2 vs H1, as well as “strong positive” FCF in the latter parts of H2, resulting in full year being break even.

EXPECTED CHANGE TO CONSENSUS EARNINGS  
![](images/101ab98dd333e86280cb84a423a1438e23a473e4e8ffb0848bb75e1693625ffe.jpg)

EXHIBIT 1: Volvo Car: Results vs Consensus

<table><tr><td rowspan="2">2026 Q2SEK mns</td><td colspan="3">Actual</td><td colspan="2">BERNe</td><td colspan="2">Consensus</td></tr><tr><td>2025 Q2</td><td>2026 Q2</td><td>vs 2025( %)</td><td>2026 Q2E</td><td>Δ</td><td>2026 Q2E</td><td>Δ</td></tr><tr><td>Total Revenue</td><td>93,492</td><td>77,673</td><td>(16.9%)</td><td>84,308</td><td>(7.9%)</td><td>82,736</td><td>(6.1%)</td></tr><tr><td>Gross Income (excl. items affecting comparability)</td><td>12,590</td><td>13,083</td><td>3.9%</td><td>13,489</td><td>(3.0%)</td><td>14,683</td><td>(10.9%)</td></tr><tr><td>Gross Margin</td><td>13.5%</td><td>16.8%</td><td>3.4%</td><td>16.0%</td><td>0.8%</td><td>17.7%</td><td>(0.9%)</td></tr><tr><td>EBIT</td><td>-9,955</td><td>826</td><td>(108.3%)</td><td>-71</td><td>(1256.4%)</td><td>1,105</td><td>(25.2%)</td></tr><tr><td>Margin</td><td>-10.6%</td><td>1.1%</td><td>11.7%</td><td>-0.1%</td><td>1.1%</td><td>1.3%</td><td>(0.3%)</td></tr><tr><td>EBIT (excl. items affecting comparability)</td><td>2,912</td><td>826</td><td>(71.6%)</td><td>429</td><td>92.7%</td><td>1,105</td><td>(25.2%)</td></tr><tr><td>Margin</td><td>3.1%</td><td>1.1%</td><td>(2.1%)</td><td>0.5%</td><td>0.6%</td><td>1.3%</td><td>(0.3%)</td></tr><tr><td>Net Income (shareholders)</td><td>-7,512</td><td>1,256</td><td>(116.7%)</td><td>-34</td><td>(3828.8%)</td><td>1,050</td><td>19.6%</td></tr><tr><td>Basic EPS</td><td>-2.53</td><td>0.54</td><td>(121.3%)</td><td>-0.02</td><td>(3407.2%)</td><td>0.35</td><td>52.4%</td></tr><tr><td>Cash flow from operating and investing</td><td>4,182</td><td>-5,243</td><td>(225.4%)</td><td>-14,806</td><td>(64.6%)</td><td>1,857</td><td>(382.3%)</td></tr><tr><td>Working Capital Cash Flow</td><td>12,635</td><td>898</td><td>(92.9%)</td><td>-11,618</td><td>(107.7%)</td><td></td><td></td></tr><tr><td>Net Capex</td><td>-11,423</td><td>-8,323</td><td>(27.1%)</td><td>-9,600</td><td>(13.3%)</td><td></td><td></td></tr></table>

Source: Company reports, Infront consensus, Bernstein analysis and estimates

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2"></td><td colspan="4">16 Jul 2026</td><td>TTM</td><td colspan="4">Reported EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Rating</td><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Rel. Perf.</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>VOLCARB.SS (Volvo Car)</td><td>U</td><td>SEK</td><td>21.15</td><td>17.00</td><td>1.0%</td><td>SEK</td><td>0.06</td><td>2.48</td><td>7.61</td><td>361.1</td><td>8.5</td><td>2.8</td></tr><tr><td>EDME</td><td></td><td></td><td>1,598.24</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

Source: Bloomberg, Bernstein estimates and analysis.

## I. REQUIRED DISCLOSURES

References to "Bernstein" or the "Firm" in these disclosures relate to the following entities: Bernstein Institutional Services LLC (April 1, 2024 onwards), Bernstein & Co., LLC (pre April 1, 2024), Bernstein Autonomous LLP, BSG France S.A. (April 1, 2024 onwards), Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited, Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社) and analysts employed by SG Africa Technologies & Services to produce Bernstein under a Global Services Agreement in place between Bernstein and SG.

Bernstein is part of a joint venture between SG (SG) and AllianceBernstein, L.P. (AB). Unless specifically noted otherwise, for purposes of these disclosures, references to Bernstein's “affiliates” relate to both SG and AB and their respective affiliates.

## VALUATION METHODOLOGY

## Volvo Car AB

We value Volvo on FCF yield. We value our 2028 FCF estimate of SEK 6.6bn at a $12\%$ FCF yield (a small discount to European peers). We discount this back using a WACC of $8\%$ based on the $3.5\%$ YTM where Volvo's bonds are trading today, and to take into account the risk premium. This gives our 17 SEK target price.

## RISKS

## Volvo Car AB

Upside risks include: another short squeeze (c.21% of the float is shorted), any relaxation of tariffs (including US-China, EU-China, US-EU), better than expected results from the cost and cash action plan.

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

The Autonomous brand rates common stocks as indicated below. As our benchmarks we use the Bloomberg Europe 600 Financials Price Return Index (E600BK) and Bloomberg Europe Dev Mkt Financials Large and Mid Cap Price Ret Index EUR (EDMFI) index for developed European banks and Payments, the Bloomberg Europe 600 Insurance Price Return Index (E600IN) for European insurers, the S&P 500 and S&P Financials for US banks and Payments coverage, S5LIFE for US Insurance, the S&P Insurance Select Industry (SPSIINS) for US Non-Life Insurers coverage, and the Bloomberg Emerging Markets Financials Large, Mid and Small Cap Price Return Index (EMLSF) for emerging market banks and insurers and Payments. Ratings are stated relative to the sector (not the market).

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

It is at the sole discretion of the Firm as to when to initiate, update and cease research coverage. The Firm has established, maintains and relies on information barriers to control the flow of information contained in one or more areas (i.e. the private side) within the Firm, and into other areas, units, groups or affiliates (i.e. public side) of the Firm

## DISTRIBUTION OF EQUITY RATINGS/INVESTMENT BANKING SERVICES

Outperform (O); Market-Perform (M); Underperform (U); Coverage Suspended (CS); Not Covered (NC)

<table><tr><td>Equity Rating</td><td>Market Abuse Regulation (MAR) and FINRA Rating Category</td><td>Global Rating Distribution</td><td>Investment Banking Relationships*</td></tr><tr><td>Outperform</td><td>BUY</td><td>51.2%</td><td>15.3%</td></tr><tr><td>Market-Perform (Bernstein Brand) Neutral (Autonomous Brand)</td><td>HOLD</td><td>35.8%</td><td>16.2%</td></tr><tr><td>Underperform</td><td>SELL</td><td>13.1%</td><td>13.6%</td></tr></table>

\* These figures represent the percentage of companies within each equity rating category for which affiliates of Bernstein have provided investment banking services within the previous 12 months.
As of June 30, 2026. All figures are updated quarterly.

## PRICE CHARTS / RATINGS AND PRICE TARGET HISTORY

Volvo Car AB (VOLCARB.SS) Rating History for Bernstein as of 07/16/2026  
![](images/6cfdbe4f7b90f26e81cd1b48aaeec1088aeba3c81f4ac1efe4a4e8ef77516e53.jpg)  
All price target and closing price data in the chart(s) above are denominated in the currency noted in the Ticker Table of this report.

## CONFLICTS OF INTEREST

Bernstein and/or affiliates have received compensation for investment banking services in the past twelve months from Volvo Car AB.

Bernstein and/or affiliates have received compensation for non-investment banking securities-related products or services in the previous twelve months from the following clients: Volvo Car AB.

Certain affiliates of Bernstein act as market maker or liquidity provider in the equities securities of: Volvo Car AB.

Certain affiliates of Bernstein act as market maker or liquidity provider in the debt securities of: Volvo Car AB.

## OTHER MATTERS

The legal entity(ies) employing the analyst(s) listed in this report, and their location, can be determined by the country code of their phone number, as follows:

+1

[中间内容因长度限制已省略]

 you of any change in the reported

information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
