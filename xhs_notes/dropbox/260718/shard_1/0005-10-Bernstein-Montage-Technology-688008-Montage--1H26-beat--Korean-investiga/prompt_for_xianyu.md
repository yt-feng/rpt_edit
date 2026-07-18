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
China Semiconductors

Montage Technology

Rating
Outperform

Price Target

688008.CH 400.00 CNY

6809.HK 520.00 HKD

Qingyuan Lin, Ph.D.
+852 2123 2654
qingyuan.lin@bernsteinsg.com

![](images/c7e3657709d575b806539f6bb40b146d97657a27d29aa2662f2cca75278dffb2.jpg)

![](images/3b9251a4e00678014076e60332d002df5ce1ead8f0ddaed1385b501076f8e793.jpg)

![](images/aa4cc2d06d5b29b4e611294d491a5b60eff46b9234498b663abfe0e2cf376e3e.jpg)

Francis Ma
+852 2123 2626
francis.ma@bernsteinsg.com

Kai Zhang
+852 2123 2665
kai.zhang@bernsteinsg.com

# Montage: 1H26 beat; Korean investigation unlikely to alter fundamentals

1H26 preliminary results beat from revenue to profit, despite an FX headwind. Montage's 1H26 revenue grew $26.6\%$ YoY to RMB3.34Bn, $3.1\%$ above BBG consensus and $0.6\%$ above our forecast. At the midpoint, net income attributable to shareholders rose $72.6\%$ YoY to RMB 2.0Bn. The midpoint net margin expanded 1,596 bps YoY to $60\%$ , thanks to the positive contribution of fair-value gains on investments and asset disposal income. Importantly, RMB results understate the underlying business momentum: Montage prices its products in USD, while continued RMB appreciation reduced reported revenue growth. Maintain Outperform.

We don't expect the Korean authority investigation to have a material impact on Montage's fundamentals. Neither the company nor its executives currently face allegations of wrongdoing, and customer orders remain unaffected. Most importantly, we see limited commercial rationale for price manipulation, and so far no fact supports that as well. Montage cuts prices annually over the lifecycle of a product generation; and memory interface chips price have not increased even during the current surge of memory prices. These chips account for only $< 1\%$ of a DDR module's selling price, leaving memory manufacturers with little incentive to push for lower price as the quality matters more than price, which is the core reason for high margin. Therefore, we see limited risk to Montage's pricing, revenue, or margin. In our bear case, the investigation may result in a one time nonrecurring loss, rather than any fundamental changes.

The $30\%$ correction in Montage's A-share over the past month reflects a thematic memory sell-off, but we believe the market has a misunderstanding to Montage's fundamentals. Some profit-taking is understandable after shares had risen $168\%$ YTD in the peak. However, memory interface chip pricing does not move with memory ASP, so concerns over the sustainability of memory price surge have limited relevance to Montage's earnings. The more important driver is memory bit shipment growth used in server driven by CPU volume growth, which continues to expand steadily. We therefore see the current sector-driven correction as disconnected from Montage's underlying volume and earnings drivers. Upcoming earnings from global server CPU vendors should bring more positive sentiment. We suggest buying the dip.

<table><tr><td>Reported EPS</td><td>F25A</td><td>F26E</td><td>F27E</td></tr><tr><td>688008.CH (CNY)</td><td>1.97</td><td>3.21</td><td>5.68</td></tr><tr><td>6809.HK (CNY)</td><td>1.97</td><td>3.21</td><td>5.68</td></tr></table>

Source: Bloomberg, Bernstein estimates and analysis.

<table><tr><td>Close Date</td><td>17 Jul 2026</td></tr><tr><td>688008.CH Close Price (CNY)</td><td>183.60</td></tr><tr><td>Price Target (CNY)</td><td>400.00</td></tr><tr><td>Upside/(Downside)</td><td>118%</td></tr><tr><td>52-Week Range</td><td>332.90/81.66</td></tr><tr><td>ASIAX</td><td>1,921.27</td></tr><tr><td>FYE</td><td>Dec</td></tr><tr><td>Div Yield</td><td>0.4%</td></tr><tr><td>Market Cap (CNY) (M)</td><td>226,894</td></tr><tr><td>EV (CNY) (M)</td><td>210,151</td></tr></table>

<table><tr><td>Performance</td><td>YTD</td><td>1M</td><td>6M</td><td>12M</td></tr><tr><td>Absolute (%)</td><td>55.9</td><td>(30.1)</td><td>28.8</td><td>112.8</td></tr><tr><td>ASIAX (%)</td><td>17.5</td><td>(5.8)</td><td>11.9</td><td>32.1</td></tr><tr><td>Relative (%)</td><td>38.4</td><td>(24.2)</td><td>16.8</td><td>80.7</td></tr></table>

Source: Bloomberg, Bernstein estimates and analysis.  
Price Performance, 1YR

![](images/2886fceac1c363ef6ef450402006a1dffeafb208ce7cd03b1703399ab7b4559d.jpg)

<table><tr><td>Valuation Metrics</td><td>F25A</td><td>F26E</td><td>F27E</td></tr><tr><td>Reported P/E (x)</td><td>93.2</td><td>57.3</td><td>32.3</td></tr></table>

EXHIBIT 1: Montage 1H26 preliminary results beat consensus and our forecast across the board

<table><tr><td colspan="4">Montage 1H26 Preliminary Results</td></tr><tr><td></td><td>Midpoint</td><td>Low</td><td>High</td></tr><tr><td>Revenue</td><td>3,335</td><td></td><td></td></tr><tr><td>YoY</td><td>26.6%</td><td></td><td></td></tr><tr><td>Bern. Rev.</td><td>3,316</td><td></td><td></td></tr><tr><td>YoY</td><td>25.9%</td><td></td><td></td></tr><tr><td>Actual vs. Bern.</td><td>0.6%</td><td></td><td></td></tr><tr><td>Consensus Rev.</td><td>3,234</td><td></td><td></td></tr><tr><td>YoY</td><td>22.8%</td><td></td><td></td></tr><tr><td>Actual vs. Cons.</td><td>3.1%</td><td></td><td></td></tr><tr><td>Net Income (attributable)</td><td>2,000</td><td>1,900</td><td>2,100</td></tr><tr><td>YoY</td><td>72.6%</td><td>63.9%</td><td>81.2%</td></tr><tr><td>Bern. Net Income</td><td>1,717</td><td></td><td></td></tr><tr><td>YoY</td><td>48.2%</td><td></td><td></td></tr><tr><td>Actual vs. Bern.</td><td>16.5%</td><td>10.6%</td><td>22.3%</td></tr><tr><td>Consensus Net Income</td><td>1,689</td><td></td><td></td></tr><tr><td>YoY</td><td>45.7%</td><td></td><td></td></tr><tr><td>Actual vs. Cons.</td><td>18.4%</td><td>12.5%</td><td>24.3%</td></tr><tr><td>Net Profit Margin</td><td>60.0%</td><td>57.0%</td><td>63.0%</td></tr><tr><td>VS. last year</td><td>1596bps</td><td>1296bps</td><td>1896bps</td></tr><tr><td>Bern. NPM</td><td>51.8%</td><td></td><td></td></tr><tr><td>Actual vs. Bern.</td><td>818bps</td><td>519bps</td><td>1118bps</td></tr><tr><td>Cons. NPM</td><td>52.2%</td><td></td><td></td></tr><tr><td>Actual vs. Cons.</td><td>774bps</td><td>474bps</td><td>1074bps</td></tr><tr><td>Recurring net Income (attributable)</td><td>1,350</td><td>1,250</td><td>1,450</td></tr><tr><td>YoY</td><td>23.7%</td><td>14.5%</td><td>32.9%</td></tr><tr><td>Recurring net profit Margin</td><td>40.5%</td><td>37.5%</td><td>43.5%</td></tr><tr><td>YoY</td><td>(95bps)</td><td>(395bps)</td><td>205bps</td></tr></table>

Source: company report, Bloomberg, Bernstein analysis and estimates

EXHIBIT 2: Memory interface chips account for only an LSD portion of module costs, limiting pricing pressure to interface chip suppliers  
![](images/ac32408b87a9a3f1e99c42b79b6e36c03d3568fc9b7c1976a1dd42c0f268b26f.jpg)  
MRDIMM remains a niche product without an established contract pricing track record. The MRDIMM pricing shown in the chart is an estimate based on public information; in general, we estimate MRDIMM enjoys a \$300-350 markup over RDIMM at the same capacity
Source: TrendForce, Bernstein analysis and estimates

## INVESTMENT IMPLICATIONS

We rate Montage Outperform, with A-Share TP at CNY 400, and H-Share TP at HKD 520.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2"></td><td colspan="4">17 Jul 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td>Rating</td><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>688008.CH (Montage)</td><td>O</td><td>CNY</td><td>183.60</td><td>400.00</td><td>80.7%</td><td>CNY</td><td>1.97</td><td>3.21</td><td>5.68</td><td>93.2</td><td>57.3</td><td>32.3</td></tr><tr><td>6809.HK (Montage)</td><td>O</td><td>HKD</td><td>255.00</td><td>520.00</td><td>NA</td><td>CNY</td><td>1.97</td><td>3.21</td><td>5.68</td><td>111.8</td><td>68.7</td><td>38.8</td></tr><tr><td>ASIAX</td><td></td><td></td><td>1,921.27</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
Source: Bloomberg, Bernstein estimates and analysis.

## I. REQUIRED DISCLOSURES

References to "Bernstein" or the "Firm" in these disclosures relate to the following entities: Bernstein Institutional Services LLC (April 1, 2024 onwards), Bernstein & Co., LLC (pre April 1, 2024), Bernstein Autonomous LLP, BSG France S.A. (April 1, 2024 onwards), Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited, Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社) and analysts employed by SG Africa Technologies & Services to produce Bernstein under a Global Services Agreement in place between Bernstein and SG.

Bernstein is part of a joint venture between SG (SG) and AllianceBernstein, L.P. (AB). Unless specifically noted otherwise, for purposes of these disclosures, references to Bernstein's “affiliates” relate to both SG and AB and their respective affiliates.

## VALUATION METHODOLOGY

## Montage Technology

We set our A-share TP at CNY 400, based on 50x 2BF P/E (27Q3–28Q2 earnings). We raise our 2027/2028 EPS estimates to CNY 5.68/10.82, respectively, on a stronger outlook for the CPU cycle and MRDIMM penetration. For the H shares, we set a target price of HKD 520, implying a 15% premium to our A-share TP (we use the CNY to HKD exchange rate at 1:1.13). The H share premium reflects that global investors favor Montage as a scarce China AI-exposed name without direct geopolitical risks, unlike many other Chinese semiconductor companies that face entity list restrictions or export control headwinds. At our target price, the implied P/E multiple on 2BF EPS for H shares is 58x.

## RISKS

## Montage Technology

Key potential risks:

1. A decrease in memory and AIDC server demand;

2. Intensify competition that leads to share loss and lower margin;

3. Failure to introduce new products for the AIDC networking market.

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

\- Credit Underperform (C-UP): The total return of the Reference Credit Instrument is expected to underperform the credit spread of bonds of other issuers operating in similar sectors or

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
