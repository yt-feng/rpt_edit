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
## U.S. Apparel & Specialty Retail

# Nike and Adidas: Pou Sheng - June revenue down HSD%

![](images/e72f9c91a5cbd2eb3532068223d7015b2a5560d67e1a9a68a4227768d55df802.jpg)

Aneesha Sherman

+1 917 344 8457

aneesha.sherman@bernsteinsg.com

![](images/10a25d3f169ea25d6a8f126f1edc7d36fa9c48f4c6e62df038b405868cab674b.jpg)

Jessica Tian

+1 917 344 8413

jessica.tian@bernsteinsg.com

![](images/9e3a44864799955f201fd9d345040e689c068c57a68855288eca0d36b73e497e.jpg)

Jed Hodulik

+1 917 344 8594

jed.hodulik@bernsteinsg.com

Nike and Adidas' biggest China wholesale partner, Pou Sheng, reported a $-8.6\%$ decline in June retail sales. $\sim 80\%$ of Pou Sheng's China sales are from Nike and Adidas products. June further declined following a negative May and off of an even weaker June 2025. It was also the weakest month of CY Q2, rounding out a quarter that was down $3.4\%$ . Revenue also remained below the pre-covid average. On a two-year stacked basis, June's result is the worst result since June 2025, driven by the DD% YoY June 2025 decline. YTD Pou Sheng growth is $-2.1\%$ YoY, which is better than the prior two years to date.

Parent company Yue Yuen's revenue growth deteriorated sequentially, with June revenue down 11.8% YoY. Yue Yuen is the world's largest Sportswear manufacturer, working with Nike, Adidas and other Western brands. The June growth rate was worse than May, and against a tough comparison from last June amid uneven but stronger comparisons from the first half of 2025. Regarding the global sportswear landscape and macro conditions, in Q1 Mgmt said, "Reciprocal tariff-related challenges, inflation pressures and uncertainties around the macroeconomic trajectory may continue to weaken consumer momentum. Multiple factors may lead to volatile sentiment, with near-term order demand expected to remain fluctuating. The Group will continue to closely monitor developments in the global economic and political environment, as well as the potential impact of recent regional conflicts on delivery timelines and the stability of raw material supplies."

Read across for Sportswear: China demand remains muted. The negative YoY growth and two-year stack in June continues the trend of generally weak results seen this year, suggesting no structural improvement yet, and Yue Yuen remains mostly negative and volatile over the past six months. The trade / tariff / macro landscape also remains uncertain (which could challenge employment and demand locally), and disruptions in the Middle East can create further headwinds through raising energy prices and disrupting shipping.

Other recent work on Nike and Adidas:

Nike Q4: Quality over Quantity

Nike: Goodbye, Friend - CFO transition, Q4 guide confirmed

Global Sportswear: State of the sector in China

Nike and Adidas: Pou Sheng - May growth negative after flat April

Adidas: Takeaways from CFO fireside conversation

China Sportswear Online Monitor: April slowdown, leaders diverge

Adidas: Performance is performing - not just a Lifestyle brand

Nike and Adidas: Product, marketing and sales impact into the World Cup

Quick take: Tariff rollback? Potential impacts to US Discretionary Brands/Retailers

US Apparel & Sportswear: Assessing the margin impact of Aug 1st tariffs

US Specialty Retail & US Transportation: How does China tariff relief impact US supply and demand?

EXHIBIT 1: Pou Sheng June sales growth was weaker than May

Pou Sheng Monthly Revenue - YOY

![](images/b61acccacacbd11c0fc182bff79e339bb30410ca2ecbf73dcfdff3e6d462169e.jpg)  
Source: Company disclosures, Bernstein analysis

EXHIBIT 2: 2Y stacked revenue was down $24.9\%$ , continuing the generally negative trend over the past two years Pou Sheng Monthly Revenue - YOY - 2 year stack  
![](images/e59085191f56bdf56c94aba8155c38c041f66b3dfaf06d5f99035ec938c585d4.jpg)  
Source: Company disclosures, Bernstein analysis

EXHIBIT 3: Last month's revenue was below Pre-COVID levels  
Pou Sheng Monthly Revenue  
![](images/bbd9b9bdc08cabc56b33a2bdb260718749d64fd927e6967db5c20be6c87849e7.jpg)  
Source: Company disclosures, Bernstein analysis  
EXHIBIT 4: The June 2026 result makes it 6 years of consecutive revenue declines in the month  
Pou Sheng Monthly Revenue - June

![](images/b47771a5be4256fa5afcfe88d8b98e308a359c42bf3848b817f3f15be4cc1d12.jpg)  
Source: Company disclosures, Bernstein analysis  
EXHIBIT 5: Despite being negative, Pou Sheng's YTD growth is improved vs prior two years  
Pou Sheng YTD Revenue growth as of June

![](images/f6156b2e2bfc97c36b2daf6ab4bc364e33100f5563f9579106b438c62d2eef58.jpg)  
Source: Company disclosures, Bernstein analysis

EXHIBIT 6: Yue Yuen manufacturing monthly revenue growth deteriorated sequentially in June

Yue Yuen - Manufacturing Business - YOY Growth in Monthly Revenue

![](images/ee55c628fcdd35bd27cf15bd6a39f7962fb0a6cb339bb86c55357f09676b1b47.jpg)  
Source: Company disclosures, Bernstein analysis  
YOY Change in Footwear Exports vs Sportswear Manufacturing

EXHIBIT 7: YoY manufacturing growth remains volatile while China footwear exports run at -HSD%

![](images/3de3745fef6986aafe6fee50426d43b25f7ca23ef6b35a2060eca3ad44d52bbd.jpg)  
May China footwear exports were $-9\%$ . Data reporting is not as consistent as Yue Yuen Source: General Administration of Customs - People's Republic of China, Bernstein analysis

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended NKE base year is 2026;

## INVESTMENT IMPLICATIONS

## We are Outperform rated on NKE and ADS.

## BERNSTEIN TICKER TABLE

<table><tr><td colspan="3"></td><td rowspan="2">9 Jul 2026 Closing Price Target</td><td rowspan="2">TTM Rel. Perf.</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td><td></td></tr><tr><td>Ticker</td><td>Rating</td><td>Cur</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td><td></td></tr><tr><td>ADS.GR (adidas)</td><td>O</td><td>EUR</td><td>181.35</td><td>245.00</td><td>(30.7)%</td><td>EUR</td><td>7.46</td><td>9.71</td><td>12.45</td><td>24.3</td><td>18.7</td><td>14.6</td></tr><tr><td>ADDYY (adidas)</td><td>O</td><td>USD</td><td>103.80</td><td>132.50</td><td>(36.7)%</td><td>USD</td><td>4.21</td><td>5.76</td><td>7.39</td><td>24.7</td><td>18.0</td><td>14.0</td></tr><tr><td>NKE (Nike)</td><td>O</td><td>USD</td><td>42.78</td><td>72.00</td><td>(63.1)%</td><td>USD</td><td>2.10</td><td>2.10</td><td>2.67</td><td>20.4</td><td>20.4</td><td>16.0</td></tr><tr><td>EDME</td><td></td><td></td><td>1,593.15</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SPX</td><td></td><td></td><td>7,543.64</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Source: Bloomberg, Bernstein estimates and analysis.

## I. REQUIRED DISCLOSURES

References to "Bernstein" or the "Firm" in these disclosures relate to the following entities: Bernstein Institutional Services LLC (April 1, 2024 onwards), Bernstein & Co., LLC (pre April 1, 2024), Bernstein Autonomous LLP, BSG France S.A. (April 1, 2024 onwards), Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited, Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社) and analysts employed by SG Africa Technologies & Services to produce Bernstein under a Global Services Agreement in place between Bernstein and SG.

Bernstein is part of a joint venture between SG (SG) and AllianceBernstein, L.P. (AB). Unless specifically noted otherwise, for purposes of these disclosures, references to Bernstein's "affiliates" relate to both SG and AB and their respective affiliates.

## VALUATION METHODOLOGY

## adidas AG

We set a €245 (\$132.5) price target using a P/E multiple of 20x against our forward FY2027 EPS estimate of €12.45.

## Nike Inc

We set a \$72 price target using a P/E multiple of 27x our forward FY2028 EPS estimate of \$2.67

## RISKS

## adidas AG

Downside risks: • Slower growth in Sportswear overall, comping against strong pandemic growth • Loss of brand heat from overdiscounting and/or over-distribution • Pressure on margins as a result of inflation, freight, channel costs, or other opex headwinds • Risk of interruption from concentrated supplier base

## Nike Inc

Downside risks: • Slower growth in Sportswear overall • Slower recovery of Nike in China, and continuing loss of market share • Pressure on margins as a result of inflation, freight, channel costs, or other opex headwinds • Share loss to competitors in key markets including North America • Risk of interruption from concentrated supplier base

RATINGS DEFINITIONS, BENCHMARKS AND DISTRIBUTION

## EQUITY RATINGS DEFINITIONS

## Bernstein brand

The Bernstein brand rates stocks based on forecasts of relative performance for the next 12 months versus the S&P 500 for stocks listed on the U.S. and Canadian exchanges, versus the Bloomberg Europe Developed Markets Large and Mid Cap Price Return Index EUR (EDME) for stocks listed on the European exchanges and emerging markets exchanges outside of the Asia Pacific region, versus the Bloomberg Japan Large and Mid Cap Price Return Index USD (JPL) for stocks listed on the Japanese exchanges, and versus the Bloomberg Asia ex-Japan Large and Mid Cap Price Return Index (ASIAX) for stocks listed on the Asian (ex-Japan) exchanges -unless otherwise specified.

The Bernstein brand has three categories of ratings:

\- Outperform: Stock will outpace the market index by more than 15 pp

• Market-Perform: Stock will perform in line with the market index to within +/-15 pp

\- Underperform: Stock will trail the performance of the market index by more than 15 pp

Coverage Suspended: Coverage of a company under the Bernstein brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Not Covered (NC) denotes companies that are not under coverage.

Bernstein brand stock ratings are based on a 12-month time horizon.

## Autonomous brand – common stocks

The Autonomous brand rates common stocks as indicated below. As our benchmarks we use the Bloomberg Europe 600 Financials Price Return Index (E600BK) and Bloomberg Europe Dev Mkt Financials Large and Mid Cap Price Ret Index EUR (EDMFI) index for developed European banks and Payments, the Bloomberg Europe 600 Insurance Price Return Index (E600IN) for European insurers, the S&P 500 and S&P Financials for US banks and Payments coverage, S5LIFE for US Insurance, the S&P Insurance Select Industry (SPSIINS) for US Non-Life Insurers coverage, and the Bloomberg Emerging Markets Financials Large, Mid and Small Cap Price Return Index (EMLSF) for emerging market banks and insurers and Payments. Ratings are stated relative to the sector (not the market).

The Autonomous brand has three categories of common stock ratings:

\- Outperform (OP): Stock will outpace the relevant index by more than 10 pp

\- Neutral (N): Stock will perform in line with the market index to within $+/-10$ pp

\- Underperform (UP): Stock will trail the performance of the relevant index by more than 10 pp

Coverage Suspended: Coverage of a company under the Autonomous research brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Those denoted as 'Feature' (e.g., Feature Outperform FOP, Feature Under Outperform FUP) are our core ideas.

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

DISTRIBUTION OF EQUITY RATINGS/INVESTMENT BANKING SERVICES

<table><tr><td>Equity Rating</td><td>Market Abuse Regulation (MAR) and FINRA Rating Category</td><td>Global Rating Distribution</td><td>Investment Banking Relationships*</td></tr><tr><td>Outperform</td><td>BUY</td><td>51.2%</td><td>15.3%</td></tr><tr><td>Market-Perform (Bernstein Brand) Neutral (Autonomous Brand)</td><td>HOLD</td><td>35.8%</td><td>16.2%</td></tr><tr><td>Underperform</td><td>SELL</td><td>13.1%</td><td>13.6%</td></tr></table>

\* These figures represent the percentage of companies within each equity rating category for which affiliates of Bernstein have provided investment banking services within the previous 12 months.
As of June 30, 2026. All figures are updated 

[中间内容因长度限制已省略]

 you of any change in the reported

information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively "Bloomberg"). Bloomberg or Bloomberg's licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg's licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
