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

VOLCARB.SS

17.00 SEK

![](images/d33bae6667c57fdb5bd3e28066c0fdcdc1e593949792c543745ae91c58250f97.jpg)

Harry Martin, CFA
+44 20 7676 8965
harry.martin@bernsteinsg.com

![](images/6d6214e87b7c63c979224ba91c40b09bc2214c2cb6ab51b5e3eddffb109ea4b0.jpg)

Gali Salvatorelli Naraghi
+44 20 7676 6741
gali.salvatorelli-naraghi@bernsteinsg.com

![](images/1fe35d027ca65a7d1f57b222e55696273b3d9ae06417ac3ee3da98afc81fe6f4.jpg)

Stephen Reitman
+44 20 7762 5535
stephen.reitman@bernsteinsg.com

Specialist Sales

![](images/e0e579a0157b6c328e078ab379d7ac9e275276249fa4373c4e7092568cff8be6.jpg)

James Brady
+44 20 7762 5272
james.brady@bernsteinsg.com

## Volvo Cars Q2 2026: Summer break (Underperform)

Volvo Cars, much like the world's top footballers who have just completed the longest World Cup of all time, reaches mid-July in need of a summer break and reset. And while car plants in Europe do cease production lines at this time of year, most of the industry's (and Volvo's) issues are too pressing to be ignored until September. Q2 was clearly a tough quarter: EBIT missed consensus by 25%, FY volume guidance was removed, and the stock dropped 10% on the day. To Volvo's credit, the predominant issues are market-level (collapse of pricing and European brand performance in China, discounting in Europe and removal of EV credits in the U.S.) which are causing volume and mix headwinds. Company-specific performance metrics are better: cost cutting is running ahead of plan, and even in Q2 Volvo gained share of the global electric+hybrid car market. Much from here rests on the success of the EX60 launch, but we retain our Underperform, with many risks still there in H2 and beyond.

Q2 miss driven by volume & mix. Volvo reported a worse-than-expected Q2 on both revenue and EBIT (6% and 25% misses respectively). This was mainly attributable to its sales mix being more heavily weighted towards smaller and lower-priced cars such as the EX30 and EX40, as well as having a lower PHEV share (unit sales down 12% yoy). As a result of global volume down -4% in H1, Volvo withdrew its previous guidance for FY volume growth, but does still expect to hit breakeven FCF in 2026 despite a 15bn SEK outflow in H1.

Q2 the floor? In the near term, the most critical question for the investment case is whether Q2's struggles are the floor, and how much self-help on the cost side plus the EX60 launch can improve things from here. While the EX60 is expected to be accretive to group margins over time, and management expects an improved US pricing environment, we see a number of offsets to the downside. Cost savings which also materially improved H2 2025 performance will have a reduced YoY impact, raw material headwinds increase, emission credit sales comp is materially harder, and the EX60 ramp is not risk free and will be gradual over summer only really impacting Q4. In the face of rising competition from Chinese brands, Volvo lost market share in Europe in H1, and we do not see the wave of new competition slowing down. We also continue to expect a miss to FCF guidance, even giving more credit in our updated model for lower capex/R&D than previously.

## Investment Implications

Source: Bloomberg, Bernstein estimates and analysis.

<table><tr><td colspan="9">We rate Volvo Underperform with a SEK 17 target price.</td></tr><tr><td>Reported EPS</td><td>F25A</td><td>F26E</td><td>F27E</td><td>Financials</td><td>F25A</td><td>F26E</td><td>F27E</td><td>CAGR</td></tr><tr><td>VOLCARB.SS (SEK)</td><td>0.06</td><td>3.09</td><td>6.56</td><td>Revenues (M)</td><td>357,263</td><td>333,845</td><td>362,190</td><td>0.7%</td></tr><tr><td>OLD</td><td>--</td><td>2.48</td><td>7.61</td><td>FCF (M)</td><td>(877.00)</td><td>(9,416)</td><td>(179.44)</td><td>(54.8)%</td></tr><tr><td></td><td></td><td></td><td></td><td>Adjusted EBIT</td><td>12,543.0</td><td>9,181.2</td><td>18,574.6</td><td>21.7%</td></tr></table>

<table><tr><td>Close Date</td><td>20 Jul 2026</td></tr><tr><td>VOLCARB.SS Close Price (SEK)</td><td>19.15</td></tr><tr><td>Price Target (SEK)</td><td>17.00</td></tr><tr><td>Upside/(Downside)</td><td>(11)%</td></tr><tr><td>52-Week Range</td><td>36.54/17.80</td></tr><tr><td>EDME</td><td>1,587.83</td></tr><tr><td>FYE</td><td>Dec</td></tr><tr><td>Div Yield</td><td>NA</td></tr><tr><td>Market Cap (SEK) (M)</td><td>57,058</td></tr><tr><td>EV (SEK) (M)</td><td>53,962</td></tr></table>

<table><tr><td>Performance</td><td>YTD</td><td>1M</td><td>6M</td><td>12M</td></tr><tr><td>Absolute (%)</td><td>(37.6)</td><td>(1.7)</td><td>(36.9)</td><td>2.1</td></tr><tr><td>EDME (%)</td><td>8.0</td><td>0.6</td><td>6.2</td><td>17.5</td></tr><tr><td>Relative (%)</td><td>(45.6)</td><td>(2.4)</td><td>(43.1)</td><td>(15.3)</td></tr></table>

Price Performance, 1YR  
Source: Bloomberg, Bernstein estimates and analysis.

![](images/c5ba4e4a23e13855b8d41f21209ab89dc9998195d1fe38fd60fdbc6f52f3e0ee.jpg)

<table><tr><td>Valuation Metrics</td><td>25A</td><td>26E</td><td>27E</td></tr><tr><td>Adjusted P/E (x)</td><td>327.0</td><td>6.2</td><td>2.9</td></tr><tr><td>EV/Sales (x)</td><td>0.2</td><td>0.2</td><td>0.1</td></tr><tr><td>EV/Adj EBITDA (x)</td><td>1.5</td><td>1.5</td><td>1.1</td></tr></table>

## RESULTS RECAP

Overall take. After the briefing call (Link) outlined a Q2 which would be hit by cost inflation and discounting as well as the tough China market, an 11% gross profit miss and 25% EBIT miss should perhaps come as little surprise. We went into the quarter meaningfully below consensus and the results are slightly better than our expectations for a 16% gross margin (actual 16.8%). Much lower R&D expenses also meant EBIT beat our forecast of slightly below breakeven. FCF burn was -€5bn SEK (consensus had positive FCF) but the company still expects approximately breakeven for the FY, where it will launch new models and unwind some of the inventory build. CMD also planned for September in Stockholm.

\- The quarter. Volvo reported revenue of SEK 77.7bn, missing consensus by 6%, gross margin of 16.8%, 90 bps below consensus, and EBIT excl. items affecting comparability of SEK 826mn, a significant (25%) miss to consensus. The decrease was driven by a combination of lower underlying wholesale volumes, weaker sales mix and pricing, FX effects, and a one-off sale of SEK 3.3 bn in 2Q25 that boosted last year's figures.

\- Retail sales were overall down 6% YoY, largely driven by a 37% decline in China, but were flat and up 9% in Europe and the US respectively. The US is said to be showing signs of a recovery in H2 after growth in May and June. In Europe, pricing pressure remains.

\- EBIT decline was mainly down to less favorable sales mix and pricing, weaker wholesale volumes, negative D&A effects, as well as lower revenue benefits from emission credits (SEK 0.8bn vs 1.7bn in 2Q25).

\- Volvo's free cash outflow of SEK 5.2bn was considerably below consensus (1.9bn inflow). Compared to our model which had a large working capital outflow, Volvo saw a minor working capital inflow.

\- Outlook. Volvo indicated that they expect “significantly stronger” sales in H2 vs H1, as well as “strong positive” FCF in the latter parts of H2, resulting in full year being break even.

EXHIBIT 1: Volvo Car: Results vs Consensus

<table><tr><td rowspan="2">2026 Q2SEK mns</td><td colspan="3">Actual</td><td colspan="2">BERNe</td><td colspan="2">Consensus</td></tr><tr><td>2025 Q2</td><td>2026 Q2</td><td>vs 2025(%)</td><td>2026 Q2E</td><td>Δ</td><td>2026 Q2E</td><td>Δ</td></tr><tr><td>Total Revenue</td><td>93,492</td><td>77,673</td><td>(16.9%)</td><td>84,308</td><td>(7.9%)</td><td>82,736</td><td>(6.1%)</td></tr><tr><td>Gross Income (excl. items affecting comparability)</td><td>12,590</td><td>13,083</td><td>3.9%</td><td>13,489</td><td>(3.0%)</td><td>14,683</td><td>(10.9%)</td></tr><tr><td>Gross Margin</td><td>13.5%</td><td>16.8%</td><td>3.4%</td><td>16.0%</td><td>0.8%</td><td>17.7%</td><td>(0.9%)</td></tr><tr><td>EBIT</td><td>-9,955</td><td>826</td><td>(108.3%)</td><td>-71</td><td>(1256.4%)</td><td>1,105</td><td>(25.2%)</td></tr><tr><td>Margin</td><td>-10.6%</td><td>1.1%</td><td>11.7%</td><td>-0.1%</td><td>1.1%</td><td>1.3%</td><td>(0.3%)</td></tr><tr><td>EBIT (excl. items affecting comparability)</td><td>2,912</td><td>826</td><td>(71.6%)</td><td>429</td><td>92.7%</td><td>1,105</td><td>(25.2%)</td></tr><tr><td>Margin</td><td>3.1%</td><td>1.1%</td><td>(2.1%)</td><td>0.5%</td><td>0.6%</td><td>1.3%</td><td>(0.3%)</td></tr><tr><td>Net Income (shareholders)</td><td>-7,512</td><td>1,256</td><td>(116.7%)</td><td>-34</td><td>(3828.8%)</td><td>1,050</td><td>19.6%</td></tr><tr><td>Basic EPS</td><td>-2.53</td><td>0.54</td><td>(121.3%)</td><td>-0.02</td><td>(3407.2%)</td><td>0.35</td><td>52.4%</td></tr><tr><td>Cash flow from operating and investing</td><td>4,182</td><td>-5,243</td><td>(225.4%)</td><td>-14,806</td><td>(64.6%)</td><td>1,857</td><td>(382.3%)</td></tr><tr><td>Working Capital Cash Flow</td><td>12,635</td><td>898</td><td>(92.9%)</td><td>-11,618</td><td>(107.7%)</td><td></td><td></td></tr><tr><td>Net Capex</td><td>-11,423</td><td>-8,323</td><td>(27.1%)</td><td>-9,600</td><td>(13.3%)</td><td></td><td></td></tr></table>

Source: Company reports, Infront consensus, Bernstein analysis and estimates

## TOP 10 QUESTIONS FOR MANAGEMENT

1. Could you give some further detail on the MoU with the Belgian government that involves the receiving of a €119m package to be used for operations in Gent? What are the cash flow dynamics? Going forward, how much of production will be taken up by other brands in Geely group?

2. What is the run-rate volume of EX60 needed for it to be margin accretive as planned? Do we get to these levels by the end of 2026?

3. You point out H1 savings already higher than the SEK 5bn for the full year, so should we assume more than SEK10bn by the end of 2026, or are there some non-underlying effects? Or ultimately are the underlying savings in H2 washed out due to cost inflation?

4. What are the main drivers behind removing the annual YoY sales growth target for 2026 volumes?

5. You expect FCF to improve in 2026 vs 2025 despite the base containing SEK 8bn of proceeds from the sale of Lynk&Co. Many headwinds from 2025 continue/worsen: FX, raw material inflation including semis, restructuring, new model ramp. What gives you confidence you can grow FCF despite these headwinds?

6. In your strategy update in November, you laid out the path to an 8% EBIT margin. What timeline do you expect to achieve this over? What level of margin would you expect to achieve in 2026, and what is the phasing between H1 and H2?

7. You spoke at Q4 about a net tariff impact of 1bn for 2025. Do you expect this to be lower in 2026? You have now begun production of the EX30 at Gent in response to the EU-China tariffs. How much more production needs to be shifted locally in order to have the right manufacturing footprint? How much capex do you expect to spend moving production in the coming years?

8. How do you see the competitive environment today? Is pressure on pricing stepping up, and how does it vary by region? How competitive are Chinese players' EV launches in Europe? What unit sales are you targeting for the EX60 during peak production?

9. How do you see your competitive position in BEVs, particularly in China? Would it be fair to say it is unreasonable to expect you can compete with local players on cost? How does the Volvo brand position itself in China to deliver a strong proposition to consumers in this context?

10. How is the relationship with Geely? You spoke about integrating governance more closely with them, how do you expect this to evolve?

## SUMMARY CHANGES TO MODEL

We update our model for the Q2 results and the latest FX rates. Our 2026 revenue comes down on the Q2 miss, but our EBIT comes up due to the company beating our estimates on lower R&D. FCF for 2026 is also revised up after the company reported capex notably lower than our estimates going into results, but we remain below guidance for FY breakeven. Our future years, however, are broadly unchanged. Our EPS estimates are altered due to a change in the way we forecast minorities.

EXHIBIT 2: Volvo Cars: Summary Changes to Model

<table><tr><td rowspan="2"></td><td rowspan="2">Actual2025 FY</td><td colspan="3">OLD</td><td colspan="3">NEW</td><td colspan="3">Δ</td></tr><tr><td>2026 FYE</td><td>2027 FYE</td><td>2028 FYE</td><td>2026 FYE</td><td>2027 FYE</td><td>2028 FYE</td><td>2026 FYE</td><td>2027 FYE</td><td>2028 FYE</td></tr><tr><td>Total Wholesale Volumes</td><td>693,024</td><td>695,937</td><td>740,061</td><td>782,613</td><td>678,551</td><td>728,400</td><td>771,634</td><td>(2%)</td><td>(2%)</td><td>(1%)</td></tr><tr><td>Revenue: New Cars</td><td>250,468</td><td>238,595</td><td>256,876</td><td>274,424</td><td>233,884</td><td>256,743</td><td>274,754</td><td>(2%)</td><td>(0%)</td><td>0%</td></tr><tr><td>Contract Manufacturing Revenue</td><td>10,249</td><td>9,952</td><td>10,947</td><td>12,042</td><td>9,760</td><td>10,736</td><td>11,810</td><td>(2%)</td><td>(2%)</td><td>(2%)</td></tr><tr><td>Other Revenue</td><td>96,546</td><td>95,901</td><td>97,652</td><td>99,551</td><td>90,201</td><td>94,711</td><td>99,446</td><td>(6%)</td><td>(3%)</td><td>(0%)</td></tr><tr><td>Total Revenue</td><td>357,263</td><td>344,448</td><td>365,475</td><td>386,018</td><td>333,845</td><td>362,190</td><td>386,010</td><td>(3%)</td><td>(1%)</td><td>(0%)</td></tr><tr><td>Gross Profit</td><td>60,221</td><td>58,885</td><td>68,899</td><td>76,624</td><td>57,726</td><td>68,303</td><td>76,652</td><td>(2%)</td><td>(1%)</td><td>0%</td></tr><tr><td>Margin</td><td>16.9%</td><td>17.1%</td><td>18.9%</td><td>19.8%</td><td>17.3%</td><td>18.9%</td><td>19.9%</td><td>0.2%</td><td>0.0%</td><td>0.0%</td></tr><tr><td>EBITDA</td><td>35,186</td><td>35,291</td><td>47,106</td><td>53,292</td><td>36,601</td><td>47,261</td><td>53,442</td><td>4%</td><td>0%</td><td>0%</td></tr><tr><td>Margin</td><td>9.8%</td><td>10.2%</td><td>12.9%</td><td>13.8%</td><td>11.0%</td><td>13.0%</td><td>13.8%</td><td>0.7%</td><td>0.2%</td><td>0.0%</td></tr><tr><td>EBIT excl. items affecting comparability</td><td>12,543</td><td>8,695</td><td>18,654</td><td>23,798</td><td>9,181</td><td>18,575</td><td>23,793</td><td>6%</td><td>(0%)</td><td>(0%)</td></tr><tr><td>Margin</td><td>3.5%</td><td>2.5%</td><td>5.1%</td><td>6.2%</td><td>2.8%</td><td>5.1%</td><td>6.2%</td><td>0.2%</td><td>0.0%</td><td>(0.0%)</td></tr><tr><td>Tax</td><td>-2,302</td><td>-2,795</td><td>-5,577</td><td>-7,150</td><td>-3,124</td><td>-5,522</td><td>-7,122</td><td>(12%)</td><td>(1%)</td><td>(0%)</td></tr><tr><td>Net Income after Minorities</td><td>174</td><td>5,620</td><td>15,718</td><td>20,296</td><td>7,243</td><td>13,528</td><td>17,449</td><td>29%</td><td>(14%)</td><td>(14%)</td></tr><tr><td>Diluted EPS</td><td>0.1</td><td>2.5</td><td>7.6</td><td>9.8</td><td>3.1</td><td>6.6</td><td>8.5</td><td>24%</td><td>(14%)</td><td>(14%)</td></tr><tr><td>Net Debt/(Cash)</td><td>-13,996</td><td>-167</td><td>1,575</td><td>-6,542</td><td>335</td><td>1,524</td><td>-6,458</td><td>(300%)</td><td>(3%)</td><td>(1%)</td></tr><tr><td>Total D&amp;A Charge</td><td>-23,945</td><td>-26,596</td><td>-28,452</td><td>-29,494</td><td>-27,419</td><td>-28,686</td><td>-29,649</td><td>(3%)</td><td>(1%)</td><td>(1%)</td></tr><tr><td>Free Cash Flow</td><td>-877</td><td>-12,903</td><td>-786</td><td>9,073</td><td>-9,416</td><td>-179</td><td>8,993</td><td>27%</td><td>(77%)</td><td>(1%)</td></tr></table>

Source: Company reports, Bernstein estimates & analysis

## APPENDIX - FINANCIAL FORECASTS

EXHIBIT 3: Volvo Cars: Summary Model

<table><tr><td>SEK mn</td><td>2020 FY</td><td>2021 FY</td><td>2022 FY</td><td>2023 FY</td><td>2024 FY</td><td>2025 FY</td><td>2026 H1</td><td>2

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
