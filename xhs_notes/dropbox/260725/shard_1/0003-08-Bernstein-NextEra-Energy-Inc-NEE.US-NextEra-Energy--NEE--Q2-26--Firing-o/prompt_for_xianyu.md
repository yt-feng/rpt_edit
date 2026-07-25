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
Americas Energy & Transition NextEra Energy Inc

Rating Outperform

Price Target

NEE

108.00 USD (107.00 OLD)

![](images/f2d765c1525ede639e190612fe469d6e3e30c5d1c4aa7961df947a90f55c14f7.jpg)

![](images/e477001c9c34ed5cf47c626d5a91848b5cc58966ddc80b029b589fd72ad2206e.jpg)

Sunaina Ocalan
.+1 917 344 8503
sunaina.ocalan@bernsteinsg.com

![](images/8c4216459ff8e395c11b9ec53944cd0f013eb4254ebc52d8403c2f03a7223419.jpg)

Anshika Bajpai
+1 917 344 8306
anshika.bajpai@bernsteinsg.com

Raphael Lee  
+1 917 344 8355  
raphael.lee@bernsteinsg.com

# NextEra Energy (NEE) Q2 26: Firing on all cylinders - large load tariffs at FPL, strong origination at NEER

NEE delivered a thesis-affirming Q2, with adj. EPS of \$1.15, ahead of consensus at \$1.13, and growing 9.5% y/y, while reiterating their 2026 adj. EPS guidance at the high end of \$3.92-\$4.02. The results reinforce our view that NEE is among the best positioned U.S. utilities to benefit from accelerating data center driven power demand.

Large-load demand at FPL: 21GW of large-load interest, of which 12GW in advance discussions, and 8GW in development expectations by 2032 (updated from 6GW). Management expects to announce at least one large-load transaction at FPL by the end of the year.

NEER Origination: Added 3.6GW of renewables and storage origination in the quarter, including 2 GW of battery storage, bringing total backlog to 35.1GW from 33GW in Q1.

Progress on the Dominion merger continues, with regulatory filings and shareholder meetings advancing as expected; expected close in H2 2027.

Positives from the quater: Adj. EPS beat, reaffirmation of 2026 and LT guidance, increased visibility into large-load demand, continue strength in NEE recontracting

Negatives: No guidance raise despite tracking above the 8% adj. EPS growth target

We raise our price target slightly from \$107 to \$108, reflecting our updated estimates following the Q2 26 results.

## Investment Implications

We remain Outperform on NEE, with an updated price target of \$108 (old \$107)

<table><tr><td>Adjusted EPS</td><td>F25A</td><td>F26E</td><td>F27E</td></tr><tr><td>NEE (USD)</td><td>3.71</td><td>4.31</td><td>4.49</td></tr><tr><td>OLD</td><td>--</td><td>4.30</td><td>4.48</td></tr></table>

<table><tr><td>Close Date</td><td>23 Jul 2026</td></tr><tr><td>NEE Close Price (USD)</td><td>89.79</td></tr><tr><td>Price Target (USD)</td><td>108.00</td></tr><tr><td>Upside/(Downside)</td><td>20%</td></tr><tr><td>52-Week Range</td><td>98.75/69.24</td></tr><tr><td>SPX</td><td>7,408.30</td></tr><tr><td>FYE</td><td>Dec</td></tr><tr><td>Div Yield</td><td>2.8%</td></tr><tr><td>Market Cap (USD) (M)</td><td>186,075</td></tr><tr><td>EV (USD) (M)</td><td>299,890</td></tr></table>

<table><tr><td>Performance</td><td>YTD</td><td>1M</td><td>6M</td><td>12M</td></tr><tr><td>Absolute (%)</td><td>11.1</td><td>1.8</td><td>5.2</td><td>24.0</td></tr><tr><td>SPX (%)</td><td>8.2</td><td>0.6</td><td>7.1</td><td>16.5</td></tr><tr><td>Relative (%)</td><td>2.9</td><td>1.2</td><td>(1.9)</td><td>7.5</td></tr></table>

Source: Bloomberg, Bernstein estimates and analysis.

Price Performance, 1YR  
![](images/889959002330df8b76a6ecaa0fc69f59ecb72d96638b4f242de7b86daa6bf1fa.jpg)

<table><tr><td>Valuation Metrics</td><td>F25A</td><td>F26E</td><td>F27E</td></tr><tr><td>Adjusted P/E (x)</td><td>24.2</td><td>20.8</td><td>20.0</td></tr><tr><td>EV/Sales (x)</td><td>10.9</td><td>9.3</td><td>8.7</td></tr><tr><td>EV/EBITDA (x)</td><td>20.2</td><td>16.6</td><td>14.9</td></tr><tr><td>EV/EBIT (x)</td><td>36.2</td><td>25.7</td><td>23.7</td></tr><tr><td>Div Yield (%)</td><td>2.5</td><td>2.8</td><td>3.1</td></tr></table>

## DETAILS

## FPL: RATE BASE COMPOUNDING CONTINUES

FPL reported Q2 adj. EPS of \$.067, in line with consensus estimates and up 8.1% y/y. Capex was \~\$2.8 billion in Q2, and full-year guide remained \$12-\$13 billion. Regulatory capital employed grew 9.3% y/y, accelerating from 8.8% y/y growth in Q1.

FPL continues to stand out operationally, while continuing to keep customer bills in check, (30% lower than national average). Reliability is more than 60% better than the national average.

## NEER: BACKLOG QUALITY AND RECONTRACTING STAND OUT

NEER reported Q2 adj. EPS of \$0.62, above consensus of \$0.59 and up 17% y/y. The segment added 3.6GW of renewables and storage origination in the quarter, including 2 GW of battery storage, bringing total backlog to 35.1GW from 33GW in Q1.

The 2 GW storage reaffirms NEER's backlog growth is tied to assets that can provide capacity, reliability, and load-following capability rather than just energy production, which fits better with current utility and hyperscaler needs.

Recontracting also remained constructive. Since the Q1 earnings call, NEER recontracted more than 500 MW of existing projects at an average premium of roughly \$20/MWh above recent realized pricing and with average terms of \~5 years, proving that the operating fleet can roll off legacy contracts without suffering a material value reset.

Other notable updates:

\- Duane Arnold remains on track to return no later than Q1 2029, the Iowa Utilities Commission approved a generating certificate, and NEER acquired the remaining minority interest, becoming the sole owner of the project.

\- NextEra Energy Transmission energized a 137-mile, 345-kV transmission line in New Mexico ahead of schedule and on budget, and MISO selected the company as part of a consortium for two large-scale 765-kV Illinois transmission projects.

## DATA-CENTER HUBS

NEER now has 30 potential hubs under discussion and expects to reach 40 by year-end. Four different origination channels (hyperscalers, investor-owned utilities, co-ops and municipal utilities, and federal partners) supporting a base case of 15 GW of new generation to serve large-load customers by 2035, with an upside case of 30 GW+.

## DOMINION: REGULATORY PATH IS NOW THE FOCUS

On July 15, the companies filed for approval with the Virginia State Corporation Commission, the North Carolina Utilities Commission, and the Public Service Commission of South Carolina; they also filed with FERC and the NRC, and the S-4 became effective on July 23.

Management still targets an H2 2027 close for the merger. The company reiterated the long-term combined-company growth of $\sim 11\%$ in regulatory capital employed through 2032 and $9\% +$ adjusted EPS through 2032, with a $9\%+$ target through 2035.

## WHAT MATTERS NEXT

\- Evidence of conversion of FPL's 12 GW of advanced discussions into signed customer commitments

\- Continued momentum in NEER's backlog growth and recontracting

\- Continued progress on Dominion approvals without incremental concessions

EXHIBIT 1: Adj. EPS Growth Outpacing 8%+ Target  
![](images/e2d6c82d608a0c91ede4e0b29744558e69b76d75a02079daea245e95185bc00b.jpg)  
Source: Company Reports, Bernstein Analysis

EXHIBIT 2: Rate Base Growth Remains Strong  
![](images/6360af7cffa3567383d384567968c9eacaae120e7ce7d99e5bce07c759c7b794.jpg)  
Source: Company Reports, Bernstein Analysis

EXHIBIT 3: Backlog Continues To Expand  
![](images/2b7d59b051a06d604ad5a469440e24fd1611eb1cc3c9c26b4a8ff9cb15660b3e.jpg)  
Source: Company Reports, Bernstein Analysis

EXHIBIT 4: Battery Storage Drives Incremental Backlog Additions  
![](images/aeb90c0527ad41af27f7972b3cc11a6ea2e0a3f87a9e88cbb8ad8e04cef0c469.jpg)  
Source: Company Reports, Bernstein Analysis

## APPENDIX - FINANCIAL FORECASTS

EXHIBIT 5: NEE Income Statement

<table><tr><td>Income Statement</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td></tr><tr><td>($MM)</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>OPERATING REVENUES</td><td>27,412</td><td>32,284</td><td>34,538</td><td>37,349</td><td>40,506</td><td>43,612</td></tr><tr><td>Fuel, purchased power and interchange</td><td>4,944</td><td>5,300</td><td>5,464</td><td>5,772</td><td>6,039</td><td>6,318</td></tr><tr><td>Other operations and maintenance</td><td>5,399</td><td>6,167</td><td>5,999</td><td>5,837</td><td>5,583</td><td>5,371</td></tr><tr><td>Depreciation and amortization</td><td>6,580</td><td>6,368</td><td>7,447</td><td>8,512</td><td>9,706</td><td>10,205</td></tr><tr><td>Taxes other than income taxes and other - net</td><td>2,469</td><td>2,797</td><td>2,962</td><td>3,160</td><td>2,927</td><td>3,128</td></tr><tr><td>Total operating expenses - net</td><td>19,392</td><td>20,632</td><td>21,871</td><td>23,280</td><td>24,254</td><td>25,022</td></tr><tr><td>Gains on disposal of businesses/assets - net</td><td>260</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>OPERATING INCOME</td><td>8,280</td><td>11,653</td><td>12,667</td><td>14,069</td><td>16,251</td><td>18,590</td></tr><tr><td>Interest expense</td><td>-4,572</td><td>-3,975</td><td>-4,867</td><td>-6,288</td><td>-7,083</td><td>-7,903</td></tr><tr><td>Total other income (deductions) - net</td><td>(3,750)</td><td>(3,393)</td><td>(4,273)</td><td>(5,679)</td><td>(6,457)</td><td>(7,261)</td></tr><tr><td>Income before income taxes</td><td>4,530</td><td>8,260</td><td>8,394</td><td>8,391</td><td>9,794</td><td>11,329</td></tr><tr><td>Income taxes</td><td>(802)</td><td>(753)</td><td>(989)</td><td>(1,072)</td><td>(1,164)</td><td>(1,104)</td></tr><tr><td>Net income</td><td>5,332</td><td>9,013</td><td>9,383</td><td>9,463</td><td>10,958</td><td>12,434</td></tr><tr><td>Net loss attributable to noncontrolling interests</td><td>1,503</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Net income attributable to NEE</td><td>6,835</td><td>9,013</td><td>9,383</td><td>9,463</td><td>10,958</td><td>12,434</td></tr><tr><td>Earnings per share attributable to NEE:</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Basic</td><td>3.31</td><td>4.32</td><td>4.50</td><td>4.54</td><td>5.25</td><td>5.96</td></tr><tr><td>Assuming dilution</td><td>3.30</td><td>4.31</td><td>4.49</td><td>4.52</td><td>5.24</td><td>5.94</td></tr><tr><td>Avg. share count (basic)</td><td>2,065</td><td>2,086</td><td>2,086</td><td>2,086</td><td>2,086</td><td>2,086</td></tr><tr><td>Avg. share count (diluted)</td><td>2,071</td><td>2,092</td><td>2,092</td><td>2,092</td><td>2,092</td><td>2,092</td></tr><tr><td>Adjustments to net income</td><td>848</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Adjusted Earnings (Loss)</td><td>7,683</td><td>9,013</td><td>9,383</td><td>9,463</td><td>10,958</td><td>12,434</td></tr><tr><td>Adjusted EPS (assuming dilution)</td><td>3.71</td><td>4.31</td><td>4.49</td><td>4.52</td><td>5.24</td><td>5.94</td></tr></table>

Source: Company Reports, Bernstein Estimates and Analysis

## BERNSTEIN TICKER TABLE

<table><tr><td colspan="3"></td><td rowspan="2">23 Jul 2026 Closing Price Target</td><td rowspan="2">TTM Rel. Perf.</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Ticker</td><td>Rating</td><td>Cur</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>NEE (NextEra Energy)</td><td>O</td><td>USD</td><td>89.79</td><td>108.00</td><td>7.5%</td><td>USD</td><td>3.71</td><td>4.31</td><td>4.49</td><td>24.2</td><td>20.8</td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>107.00</td><td></td><td></td><td></td><td>4.30</td><td>4.48</td><td></td><td></td></tr><tr><td>SPX</td><td></td><td></td><td>7,408.30</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## PRICE TARGET CHANGE / ESTIMATE CHANGE IN BOLD

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended Source: Bloomberg, Bernstein estimates and analysis.

## I. REQUIRED DISCLOSURES

References to "Bernstein" or the "Firm" in these disclosures relate to the following entities: Bernstein Institutional Services LLC (April 1, 2024 onwards), Bernstein & Co., LLC (pre April 1, 2024), Bernstein Autonomous LLP, BSG France S.A. (April 1, 2024 onwards), Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited, Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社) and analysts employed by SG Africa Technologies & Services to produce Bernstein under a Global Services Agreement in place between Bernstein and SG.

Bernstein is part of a joint venture between SG (SG) and AllianceBernstein, L.P. (AB). Unless specifically noted otherwise, for purposes of these disclosures, references to Bernstein's "affiliates" relate to both SG and AB and their respective affiliates.

## VALUATION METHODOLOGY

## NextEra Energy Inc

We blend a DCF valuation on FPL using a 2% growth rate and 6% discount rate on FPL's regulated earnings, with a 14x EV/EBITDA multiple on NEER 2027-28 EBITDA of \$12.1B to arrive at a combined target price of \$108/sh.

## RISKS

## NextEra Energy Inc

Key downside risks to our price target include FPL returns falling short of the midpoint of guidance, lower overall power demand growth dampening NEER generation, and supply chain risks from higher than expected tariff exposure.

## RATINGS DEFINITIONS, BENCHMARKS AND DISTRIBUTION

## EQUITY RATINGS DEFINITIONS

## Bernstein brand

The Bernstein brand rates stocks based on forecasts of relative performance for the next 12 months versus the S&P 500 for stocks listed on the U.S. and Canadian exchanges, versus the Bloomberg Europe Developed Markets Large and Mid Cap Price Return Index EUR (EDME) for stocks listed on the European exchanges and emerging markets exchanges outside of the Asia Pacific region, versus the Bloomberg Japan Large and Mid Cap Price Return Index USD (JPL) for stocks listed on the Japanese exchanges, and versus the Bloomberg Asia ex-Japan Large and Mid Cap Price Return Index (ASIAX) for stocks listed on the Asian (ex-Japan) exchanges -unless otherwise specified.

The Bernstein brand has three categories of ratings:

• Outperform: Stock will outpace the market index by more than 15 pp

\- Market-Perform: Stock will perform in line with the market index to within +/-15 pp

• Underperform: Stock will trail the performance of the market index by more than 15 pp

Coverage Suspended: Coverage of a company under the Bernstein brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Not Covered (NC) denotes companies that are not under coverage.

Bernstein brand stock ratings are based on a 12-month time horizon.

## Autonomous brand – common stocks

The Autonomous brand rates common stocks as indicated below. As our benchmarks we use the Bloomberg Europe 600 Financials Price Return Index (E600BK) and Bloomberg Europe Dev Mkt Financials Large and Mid Cap Price Ret Index EUR (EDMFI) index for developed European banks and Payments, the Bloomberg Europe 600 Insurance Price Return Index (E600IN) for European insurers, the S&P 500 and S&P Financials for US banks and Payments coverage, S5LIFE for US Insurance, the S&P Insurance Select Industry (SPSIINS) for US Non-Life Insurers coverage, the Bloomberg Emerging Markets Financials Large, Mid and Small Cap Price Return Index (EMLSF) for emerging market banks and insurers and Payments, and the Bloomberg Japan Financials Large & Mid Cap Price Return Index (JPFILM) for Japanese Financials. Ratings are stated relative to the sector (not the market).

The Autonomous brand has three categories of common stock ratings:

\- Outperform (OP): Stock will outpace the relevant index by more t

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
