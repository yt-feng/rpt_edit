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
Global Luxury Goods
Burberry Group PLC

Rating
Outperform

Price Target

BRBY.LN

1,300.00 GBp

![](images/b923f814370509a22b1ee4f3d9a5f247b97695a06bab04152d12a2f603a4ea92.jpg)

![](images/ff67e6129db8f51776a7d951df344fb84d3fcd95828eb6c5529d015f9c8a91cf.jpg)

Luca Solca
+41 582 723 126
luca.solca@bernsteinsg.com

![](images/b86eb3bb2bdf2473ad18f60b1140ce6763d204718f2d9ba2f2cb084f62e00707.jpg)

Maria Meita
+44 20 7170 0540
maria.meita@bernsteinsg.com

![](images/b30e1d7cce799214e8c54ab1035aec50125ce3ca12824d411b8f32b56d2d95c6.jpg)

Eric Chen, CFA
+852 2123 2628
eric.chen@bernsteinsg.com

Yi-Peng Khoo, CFA
+44 20 7676 6822
yi-peng.khoo@bernsteinsg.com

## Burberry: 2Q26 calendar in line with expectations

Burberry has just reported its 1Q27E (= calendar 2Q26) trading update. Retail performance is almost exactly in line with consensus expectations. Comparable retail sales growth is 24bps ahead at +5%. A -1% headwind from space leads to CFx growth of +4%. Overall retail revenues came in-line with consensus expectations in absolute terms (£455m vs. consensus at £454m).

By geography EMEIA saw -3% comparable retail sales growth (vs. consensus at -2.3%) - ex. the ME, EMEIA declined by -1%. The Americas saw +12% (vs. +10.6%), Greater China at +9% (vs. +9.3%) and APAC ex. GC at +3% (vs. +6.3%) - with South Korea growing +11% and Japan declining by -2%.

Burberry also indicated that outerwear grew DD in the quarter, while handbags returned to growth. Burberry has also upgraded its 1H27 wholesale revenue guidance and now expects HSD growth in 1H27 vs. MSD previously, pointing to a positive response from wholesale partners. FY27 FX guidance has also been updated for recent FX movements, with Burberry now seeing a \~£20m tailwind to revenue and a broadly neutral impact to adj. EBIT vs. a \~£10m headwind to both previously. FY27 guidance is otherwise unchanged.

Burberry has successfully gone through its first brand revival chapter. Burberry Forward works. The ball is now in management's court to sustain the recovery, adding spice and oomph to it.

We rate Burberry Outperform, PT 1,300.00GBp. The conference call will take place at 0900 UKT | 1000 CET (webinar link here)

<table><tr><td>Performance</td><td>YTD</td><td>1M</td><td>6M</td><td>12M</td></tr><tr><td>Absolute (%)</td><td>(11.7)</td><td>(3.2)</td><td>(11.9)</td><td>(8.3)</td></tr><tr><td>EDME (%)</td><td>8.7</td><td>0.7</td><td>4.7</td><td>18.0</td></tr><tr><td>Relative (%)</td><td>(20.4)</td><td>(3.9)</td><td>(16.6)</td><td>(26.4)</td></tr></table>

<table><tr><td>Close Date</td><td>16 Jul 2026</td></tr><tr><td>BRBY.LN Close Price (GBp)</td><td>1,120.50</td></tr><tr><td>Price Target (GBp)</td><td>1,300.00</td></tr><tr><td>Upside/(Downside)</td><td>16%</td></tr><tr><td>52-Week Range</td><td>1,376.50/985.00</td></tr><tr><td>EDME</td><td>1,598.24</td></tr><tr><td>FYE</td><td>Mar</td></tr><tr><td>Div Yield</td><td>NA</td></tr><tr><td>Market Cap (GBP) (M)</td><td>4,045</td></tr><tr><td>EV (GBp) (M)</td><td>4,903</td></tr></table>

Source: Bloomberg, Bernstein estimates and analysis.  
Price Performance, 1YR

Links to research

![](images/698be6d4b1ead3005cabbda30360227228e8c625a62ca6bbbe9eb24427a7dcab.jpg)

• Burberry: CEO at Bernstein SDC - key takeaways

• Global Luxury Goods Mega-transect: Resilient Labour Day traffic

\- Global Luxury Goods Mega-transect: Strong Lunar New Year 2026 foot traffic points to a gradual recovery

\- Burberry: Back to basics — Upgrading to Outperform, PT 930 GBp

<table><tr><td>Adjusted EPS</td><td>F26A</td><td>F27E</td><td>F28E</td><td>Financials</td><td>F26A</td><td>F27E</td><td>F28E</td><td>CAGR</td><td>Valuation Metrics</td><td>F26A</td><td>F27E</td><td>F28E</td></tr><tr><td>BRBY.LN (GBP)</td><td>0.24</td><td>0.39</td><td>0.55</td><td>Revenues (M)</td><td>2,420</td><td>2,563</td><td>2,724</td><td>--</td><td>Adjusted P/E (x)</td><td>45.9</td><td>28.8</td><td>20.4</td></tr></table>

Source: Bloomberg, Bernstein estimates and analysis.

EXHIBIT 1: Burberry 1Q27 results

<table><tr><td rowspan="2">Burberry (£m) Quarterly</td><td>Actual</td><td>Consensus</td><td>Beat/Miss</td><td colspan="2">Actual</td><td colspan="2">Actual</td></tr><tr><td>1Q27</td><td>1Q27</td><td>1Q27</td><td>1Q26</td><td>YoY %</td><td>4Q26</td><td>Seq%</td></tr><tr><td>Retail Revenue</td><td>455</td><td>454</td><td>+0%</td><td>433</td><td>5%</td><td>537</td><td>-15%</td></tr><tr><td>Comparable Retail Sales</td><td>5.0%</td><td>4.8%</td><td>+24</td><td>-1.0%</td><td>+600bps</td><td>4.8%</td><td>+15bps</td></tr><tr><td>EMEIA</td><td>-3.0%</td><td>-2.3%</td><td>-72</td><td>1.0%</td><td>-399bps</td><td>-2.0%</td><td>-101bps</td></tr><tr><td>Americas</td><td>12.0%</td><td>10.6%</td><td>+142</td><td>4.0%</td><td>+803bps</td><td>10.0%</td><td>+202bps</td></tr><tr><td>Greater China</td><td>9.0%</td><td>9.3%</td><td>-30</td><td>-5.1%</td><td>+1,406bps</td><td>10.0%</td><td>-101bps</td></tr><tr><td>APAC exc. Greater China</td><td>3.0%</td><td>6.3%</td><td>-330</td><td>-4.0%</td><td>+704bps</td><td>3.0%</td><td>-1bps</td></tr><tr><td>Space</td><td>-1.0%</td><td>-0.2%</td><td>-83</td><td>-1.0%</td><td>-0bps</td><td>-2.1%</td><td>+108bps</td></tr><tr><td>CFx Retail Growth</td><td>4.0%</td><td>4.6%</td><td>-61</td><td>-2.0%</td><td>+600bps</td><td>2.9%</td><td>+110bps</td></tr></table>

Source: Company reports, Visible Alpha, Bernstein analysis

EXHIBIT 2: Luxury Goods Calendar Year 2Q26 results, by division

<table><tr><td colspan="8">Luxury 2Q26 (calendar year) Results</td></tr><tr><td>(in reporting currency millions)</td><td>2Q26</td><td>2Q25</td><td>2Q21</td><td>Organic y/y</td><td>Reported y/y</td><td>Organic y/5y</td><td>Reported y/5y</td></tr><tr><td>Richemont (EUR)</td><td>6,329</td><td>5,412</td><td>4,397</td><td>+20%</td><td>+17%</td><td>+73%</td><td>+44%</td></tr><tr><td>Jewellery Maisons</td><td>4,732</td><td>3,914</td><td>2,515</td><td>+24%</td><td>+21%</td><td>+99%</td><td>+88%</td></tr><tr><td>Specialist Watchmakers</td><td>873</td><td>824</td><td>849</td><td>+8%</td><td>+6%</td><td>+6%</td><td>+3%</td></tr><tr><td>Burberry Retail (GBP)</td><td>455</td><td>433</td><td>479</td><td>+5%</td><td>+5%</td><td></td><td>-5%</td></tr></table>

For Burberry, the OSG are Comparable Store Growth  
Source: Company reports, Bernstein analysis

EXHIBIT 3: Luxury Goods Calendar Year 2Q26 results, by region

<table><tr><td colspan="8">Luxury 2Q26 (calendar year) Results</td></tr><tr><td>(in reporting currency millions)</td><td>2Q26</td><td>2Q25</td><td>2Q21</td><td>Organic y/y</td><td>Reported y/y</td><td>Organic y/5y</td><td>Reported y/5y</td></tr><tr><td>Richemont (EUR)</td><td>6,329</td><td>5,412</td><td>4,397</td><td>+11%</td><td>17%</td><td>+60%</td><td>+44%</td></tr><tr><td>Europe</td><td>1,429</td><td>1,295</td><td>905</td><td>+7%</td><td>+10%</td><td>+117%</td><td>+58%</td></tr><tr><td>Asia Pacific</td><td>2,068</td><td>1,731</td><td>1,933</td><td>+11%</td><td>+19%</td><td>+7%</td><td>+7%</td></tr><tr><td>Americas</td><td>1,670</td><td>1,335</td><td>955</td><td>+16%</td><td>+25%</td><td>+89%</td><td>+75%</td></tr><tr><td>Japan</td><td>632</td><td>527</td><td>240</td><td>+22%</td><td>+20%</td><td>+257%</td><td>+163%</td></tr><tr><td>Middle East &amp; Africa</td><td>530</td><td>524</td><td>364</td><td>-6%</td><td>+1%</td><td>+46%</td><td>+46%</td></tr><tr><td>Burberry (GBP)</td><td>455</td><td>510</td><td>556</td><td>+5%</td><td></td><td></td><td></td></tr><tr><td>Asia Pacific</td><td></td><td></td><td></td><td>+3%</td><td></td><td>+0%</td><td></td></tr><tr><td>Greater China</td><td></td><td></td><td></td><td>+9%</td><td></td><td>+0%</td><td></td></tr><tr><td>EMEIA</td><td></td><td></td><td></td><td>-3%</td><td></td><td>+0%</td><td></td></tr><tr><td>Americas</td><td></td><td></td><td></td><td>+12%</td><td></td><td>+0%</td><td></td></tr></table>

For Burberry, the OSG are Comparable Store Growth Source: Company reports, Bernstein analysis

## EXHIBIT 4: Luxury Goods Calendar Year 2Q26 results

CY 2Q26 Reported Organic Growth and Actual Change in Revenue  
![](images/a0c8e0d8582e78477a39c3d674c7fb0f50e71bd3c12f4b2195e7982731c826c3.jpg)  
Source: Company reports, Bernstein analysis

## INVESTMENT IMPLICATIONS

## We rate Burberry Outperform, PT 1,300.00GBp

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2"></td><td colspan="4">16 Jul 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Rating</td><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2026A</td><td>2027E</td><td>2028E</td><td>2026A</td><td>2027E</td><td>2028E</td></tr><tr><td>BRBY.LN (Burberry)</td><td>O</td><td>GBp</td><td>1,120.50</td><td>1,300.00</td><td>(26.4)%</td><td>GBP</td><td>0.24</td><td>0.39</td><td>0.55</td><td>45.9</td><td>28.8</td><td>20.4</td></tr><tr><td>EDME</td><td></td><td></td><td>1,598.24</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
Source: Bloomberg, Bernstein estimates and analysis.

## I. REQUIRED DISCLOSURES

References to "Bernstein" or the "Firm" in these disclosures relate to the following entities: Bernstein Institutional Services LLC (April 1, 2024 onwards), Bernstein & Co., LLC (pre April 1, 2024), Bernstein Autonomous LLP, BSG France S.A. (April 1, 2024 onwards), Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited, Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社) and analysts employed by SG Africa Technologies & Services to produce Bernstein under a Global Services Agreement in place between Bernstein and SG.

Bernstein is part of a joint venture between SG (SG) and AllianceBernstein, L.P. (AB). Unless specifically noted otherwise, for purposes of these disclosures, references to Bernstein's “affiliates” relate to both SG and AB and their respective affiliates.

## VALUATION METHODOLOGY

## Burberry Group PLC

We value Burberry on a target 1.7x relative P/E multiple to the MSCI Europe, applied to a blended forward EPS forecast on an NTM+1 basis to arrive at a PT of 1,300GBp.

## RISKS

## Burberry Group PLC

On the downside:

1. The new collection by Daniel Lee could fall short of expectations;

2. Execution of the brand turnaround could encounter problems;

3. Operating leverage may disappoint as the brand revival may cost more than anticipated.

## RATINGS DEFINITIONS, BENCHMARKS AND DISTRIBUTION

## EQUITY RATINGS DEFINITIONS

## Bernstein brand

The Bernstein brand rates stocks based on forecasts of relative performance for the next 12 months versus the S&P 500 for stocks listed on the U.S. and Canadian exchanges, versus the Bloomberg Europe Developed Markets Large and Mid Cap Price Return Index EUR (EDME) for stocks listed on the European exchanges and emerging markets exchanges outside of the Asia Pacific region, versus the Bloomberg Japan Large and Mid Cap Price Return Index USD (JPL) for stocks listed on the Japanese exchanges, and versus the Bloomberg Asia ex-Japan Large and Mid Cap Price Return Index (ASIAX) for stocks listed on the Asian (ex-Japan) exchanges -unless otherwise specified.

The Bernstein brand has three categories of ratings:

\- Outperform: Stock will outpace the market index by more than 15 pp

• Market-Perform: Stock will perform in line with the market index to within +/-15 pp

• Underperform: Stock will trail the performance of the market index by more than 15 pp

Coverage Suspended: Coverage of a company under the Bernstein brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors

on events and developments.

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

\- Credit Outperform (C-OP): The total return of the Reference Credit Instrument is expected to outperform the credit spread of bonds of other issuers operating in similar sectors or rating categor

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
