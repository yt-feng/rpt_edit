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
Market-Perform

Price Target

KO

93.00 USD (83.00 OLD)

# Coca-Cola Q2 2026 Earnings Review - Great quarter, long-term forecast largely unchanged

KO reported strong Q2 results, beating VA consensus EPS estimates of \$0.93 by \$0.04. With strong fundamental drivers behind the beat, there is nothing to pick at. Results were driven by a beat on Organic Sales Growth, which came in at 6.0% (vs. consensus of 3.5%). Organic growth was in turn powered by strong consumption as Global Unit Case Volumes grew 5%, making the beat even more compelling. Operating Income Margin also beat, delivering 35.6%, vs consensus of 35.1%. Yearly guidance for Organic Growth was updated to the top of the range, at 5%. The stock closed at \$88, posting a 5% gain.

We update our model to incorporate the latest results, but keep our medium and long-term forecasts, which already reflected our view of KO as a resilient and high-quality compounder, mostly unchanged. We also update our target multiple, from 24.0x to 25.5x, to reflect recent appreciation, which we think will be sustained and has been driven, at least in part, from rotation into the sector (Consumer Staples closed \~2% up during the session, i.e., contributed 2 out of the 5 percentage points of gain for KO). As a result, we have updated our target price. We believe KO will retain its well-earned premium relative to expected OSG, but also believe that the multiple currently has limited room for further expansion.

<table><tr><td>Close Date</td><td>28 Jul 2026</td></tr><tr><td>KO Close Price (USD)</td><td>88.27</td></tr><tr><td>Price Target (USD)</td><td>93.00</td></tr><tr><td>Upside/(Downside)</td><td>5%</td></tr><tr><td>52-Week Range</td><td>90.22/65.35</td></tr><tr><td>SPX</td><td>7,428.78</td></tr><tr><td>FYE</td><td>Dec</td></tr><tr><td>Div Yield</td><td>2.4%</td></tr><tr><td>Market Cap (USD) (M)</td><td>379,780</td></tr><tr><td>EV (USD) (M)</td><td>409,117</td></tr></table>

<table><tr><td>Performance</td><td>YTD</td><td>1M</td><td>6M</td><td>12M</td></tr><tr><td>Absolute (%)</td><td>26.3</td><td>6.8</td><td>20.8</td><td>29.6</td></tr><tr><td>SPX (%)</td><td>8.5</td><td>1.0</td><td>6.5</td><td>16.3</td></tr><tr><td>Relative (%)</td><td>17.7</td><td>5.8</td><td>14.4</td><td>13.4</td></tr></table>

Source: Bloomberg, Bernstein estimates and analysis.

## (Continued on next page)

## Investment Implications

We rate Coca-Cola Market-Perform, with a PT of \$93. Coke is a high-quality compounder, with compelling offers in Functional Beverages (Protein, Hydration). We forecast 5% and 7% YoY EPS growth NTM and NTM+1, respectively, making us bearish vs. consensus on NTM+1 EPS by 70 bps. We apply a target multiple of 25.5x (old 24.0x) to arrive at our target price.

<table><tr><td>Adjusted EPS</td><td>F25A</td><td>F26E</td><td>F27E</td></tr><tr><td>KO (USD)</td><td>3.01</td><td>3.32</td><td>3.50</td></tr><tr><td>OLD</td><td>--</td><td>3.25</td><td>3.42</td></tr></table>

Price Performance, 1YR  
![](images/9414734b0b0cae35b7d58da4e7d3394b076ab633b569076f2020c7db6b5cab07.jpg)

<table><tr><td>Financials</td><td>F25A</td><td>F26E</td><td>F27E</td><td>CAGR</td></tr><tr><td>Revenues (M)</td><td>47,941</td><td>49,698</td><td>49,353</td><td>1.5%</td></tr><tr><td>EBITDA (M)</td><td>14,812</td><td>17,273</td><td>18,314</td><td>11.2%</td></tr><tr><td>EBIT (M)</td><td>17,652</td><td>19,694</td><td>20,691</td><td>8.3%</td></tr><tr><td>FCF (M)</td><td>5,296</td><td>11,963</td><td>14,131</td><td>63.3%</td></tr><tr><td>ROIC (%)</td><td>21.5</td><td>22.3</td><td>22.1</td><td>--</td></tr><tr><td>Net Debt/EBITDA (x)</td><td>1.85</td><td>1.48</td><td>1.29</td><td>(16.4)%</td></tr><tr><td>Dividend Payout Ratio (%)</td><td>67.7</td><td>64.0</td><td>63.4</td><td>--</td></tr></table>

<table><tr><td>Valuation Metrics</td><td>F25A</td><td>F26E</td><td>F27E</td></tr><tr><td>Adjusted P/E (x)</td><td>29.4</td><td>26.6</td><td>25.2</td></tr><tr><td>PEG Adjusted (x)</td><td>7.0</td><td>2.5</td><td>4.7</td></tr><tr><td>EV/Sales (x)</td><td>8.5</td><td>8.2</td><td>8.3</td></tr><tr><td>EV/EBITDA (x)</td><td>27.6</td><td>23.7</td><td>22.3</td></tr><tr><td>EV/EBIT (x)</td><td>23.2</td><td>20.8</td><td>19.8</td></tr><tr><td>EV/FCF (x)</td><td>77.3</td><td>34.2</td><td>29.0</td></tr><tr><td>Div Yield (%)</td><td>2.3</td><td>2.4</td><td>2.5</td></tr></table>

## DETAILS

## ... (continued)

While today's results were partly enabled by one-time events, such as soft volume comps from a year ago and the impact of the World Cup, they also serve as a reminder of KO's advantaged strategic position. After all, the resiliency comes in the context of numerous headwinds – reduction in SNAP benefits, excise taxes in Mexico, pressured consumers, and commodity inflation, to name a few. But it is no coincidence that KO is successfully navigating these challenges; at the end of the day, you need unmatched global scale to justify that level of sponsorship at the World Cup, and the company's exclusive focus on Beverages continues to play a role in their ability to offer alternative subcategories that capture an ever-evolving consumer demand.

EXHIBIT 1: KO 2Q26 Segment Results: Actual vs. Bernstein vs. Consensus - EMEA

<table><tr><td rowspan="2"></td><td colspan="4">Actual</td></tr><tr><td>2025 Q2</td><td>2026 Q1</td><td>2026 Q2</td><td>YoY Δ</td></tr><tr><td colspan="5">Europe, Middle East and Africa</td></tr><tr><td>Net operating revenues - Operating</td><td>$ 3,206</td><td>$ 3,004</td><td>$ 3,243</td><td>1.2%</td></tr><tr><td>Total growth</td><td>37.4%</td><td>12.5%</td><td>1.2%</td><td>-3627 bps</td></tr><tr><td>Organic growth</td><td>4.0%</td><td>10.7%</td><td>3.0%</td><td>-100 bps</td></tr><tr><td>Price/mix</td><td>3.0%</td><td>5.0%</td><td>1.0%</td><td>-200 bps</td></tr><tr><td>Volume growth</td><td>-1.0%</td><td>5.1%</td><td>1.0%</td><td>+200 bps</td></tr><tr><td>Organic Concentrate Sales Growth</td><td>-1.0%</td><td>-1.8%</td><td>1.0%</td><td>+200 bps</td></tr><tr><td>Other/Calendar impact</td><td>0.0%</td><td>6.9%</td><td>0.0%</td><td>+0 bps</td></tr><tr><td>Forex impact</td><td>1.0%</td><td>5.8%</td><td>2.0%</td><td>+100 bps</td></tr><tr><td>Structural change/other</td><td>0.0%</td><td>-3.1%</td><td>-3.0%</td><td>-300 bps</td></tr><tr><td>EMEA - Operating income/(loss) - Operating</td><td>$ 1,358</td><td>$ 1,249</td><td>$ 1,312</td><td>-3.4%</td></tr><tr><td>Operating income/(loss) - Operating Margin (%)</td><td>42.4%</td><td>41.6%</td><td>40.5%</td><td>-190 bps</td></tr></table>

Source: Company, Visible Alpha, Bernstein analysis and estimates

<table><tr><td colspan="3">Visible Alpha Consensus</td></tr><tr><td></td><td>2026 Q2E</td><td>Δ vs Cons</td></tr><tr><td>$</td><td>3,352</td><td>-3.2%</td></tr><tr><td></td><td>4.5%</td><td>-340 bps</td></tr><tr><td></td><td>3.9%</td><td>-86 bps</td></tr><tr><td></td><td>3.8%</td><td>-279 bps</td></tr><tr><td></td><td>0.1%</td><td>+93 bps</td></tr><tr><td></td><td>3.0%</td><td>-101 bps</td></tr><tr><td></td><td>-2.6%</td><td>-38 bps</td></tr><tr><td>$</td><td>1,427</td><td>-8.0%</td></tr><tr><td></td><td>42.6%</td><td>-211 bps</td></tr></table>

<table><tr><td colspan="3">Bernstein Estimates</td></tr><tr><td></td><td>2026 Q2E</td><td>Δ vs BERNe</td></tr><tr><td>$</td><td>3,351</td><td>-3.2%</td></tr><tr><td></td><td>4.5%</td><td>-336 bps</td></tr><tr><td></td><td>4.5%</td><td>-150 bps</td></tr><tr><td></td><td>3.5%</td><td>-250 bps</td></tr><tr><td></td><td>1.0%</td><td>+0 bps</td></tr><tr><td></td><td>1.0%</td><td>+0 bps</td></tr><tr><td></td><td>0.0%</td><td>+0 bps</td></tr><tr><td></td><td>2.5%</td><td>-51 bps</td></tr><tr><td></td><td>-2.5%</td><td>-50 bps</td></tr><tr><td>$</td><td>1,457</td><td>-10.0%</td></tr><tr><td></td><td>43.5%</td><td>-303 bps</td></tr></table>

EXHIBIT 2: KO 2Q26 Segment Results: Actual vs. Bernstein vs. Consensus - LATAM

<table><tr><td rowspan="2"></td><td colspan="4">Actual</td></tr><tr><td>2025 Q2</td><td>2026 Q1</td><td>2026 Q2</td><td>YoY Δ</td></tr><tr><td colspan="5">Latin America</td></tr><tr><td>Net operating revenues - Operating</td><td>$ 1,611</td><td>$ 1,692</td><td>$ 1,827</td><td>13.4%</td></tr><tr><td>Total growth</td><td>-0.1%</td><td>11.4%</td><td>13.4%</td><td>+1353 bps</td></tr><tr><td>Organic growth</td><td>13.0%</td><td>8.7%</td><td>5.0%</td><td>-800 bps</td></tr><tr><td>Price/mix</td><td>15.0%</td><td>1.0%</td><td>3.0%</td><td>-1200 bps</td></tr><tr><td>Volume growth</td><td>2.0%</td><td>7.1%</td><td>1.0%</td><td>-100 bps</td></tr><tr><td>Organic Concentrate Sales Growth</td><td>2.0%</td><td>0.2%</td><td>1.0%</td><td>-100 bps</td></tr><tr><td>Other/Calendar impact</td><td>0.0%</td><td>6.9%</td><td>0.0%</td><td>+0 bps</td></tr><tr><td>Forex impact</td><td>-17.0%</td><td>4.5%</td><td>11.0%</td><td>+2800 bps</td></tr><tr><td>Structural change/other</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>+0 bps</td></tr><tr><td>Operating income/(loss) - Operating</td><td>$ 1,012</td><td>$ 1,052</td><td>$ 1,165</td><td>15.1%</td></tr><tr><td>Operating income/(loss) - Operating Margin (%)</td><td>62.8%</td><td>62.2%</td><td>63.8%</td><td>+95 bps</td></tr></table>

<table><tr><td colspan="3">Visible Alpha Consensus</td></tr><tr><td></td><td>2026 Q2E</td><td>Δ vs Cons</td></tr><tr><td>$</td><td>1,754</td><td>4.2%</td></tr><tr><td></td><td>8.9%</td><td>+454 bps</td></tr><tr><td></td><td>5.0%</td><td>-0 bps</td></tr><tr><td></td><td>4.0%</td><td>-100 bps</td></tr><tr><td></td><td>1.0%</td><td>+0 bps</td></tr><tr><td></td><td>3.8%</td><td>+719 bps</td></tr><tr><td></td><td>0.0%</td><td>+0 bps</td></tr><tr><td>$</td><td>1,103</td><td>5.6%</td></tr><tr><td></td><td>62.9%</td><td>+87 bps</td></tr></table>

<table><tr><td colspan="2">Bernstein Estimates</td></tr><tr><td>2026 Q2E</td><td>Δ vs BERNe</td></tr><tr><td>$ 1,716</td><td>6.5%</td></tr><tr><td>6.5%</td><td>+691 bps</td></tr><tr><td>1.5%</td><td>+350 bps</td></tr><tr><td>2.5%</td><td>+50 bps</td></tr><tr><td>-1.0%</td><td>+200 bps</td></tr><tr><td>-1.0%</td><td>+200 bps</td></tr><tr><td>0.0%</td><td>+0 bps</td></tr><tr><td>5.0%</td><td>+600 bps</td></tr><tr><td>0.0%</td><td>+0 bps</td></tr><tr><td>$ 1,073</td><td>8.5%</td></tr><tr><td>62.6%</td><td>+121 bps</td></tr></table>

Source: Company, Visible Alpha, Bernstein analysis and estimates

EXHIBIT 3: KO 2Q26 Segment Results: Actual vs. Bernstein vs. Consensus - NA

<table><tr><td rowspan="2"></td><td colspan="4">Actual</td></tr><tr><td>2025 Q2</td><td>2026 Q1</td><td>2026 Q2</td><td>YoY Δ</td></tr><tr><td colspan="5">North America</td></tr><tr><td>Net operating revenues - Operating</td><td>$ 5,040</td><td>$ 4,889</td><td>$ 5,405</td><td>7.2%</td></tr><tr><td>Total growth</td><td>4.8%</td><td>12.0%</td><td>7.2%</td><td>+246 bps</td></tr><tr><td>Organic growth</td><td>3.0%</td><td>12.0%</td><td>7.0%</td><td>+400 bps</td></tr><tr><td>Price/mix</td><td>3.0%</td><td>1.0%</td><td>4.0%</td><td>+100 bps</td></tr><tr><td>Volume growth</td><td>-1.0%</td><td>11.0%</td><td>3.0%</td><td>+400 bps</td></tr><tr><td>Organic Concentrate Sales Growth</td><td>-1.0%</td><td>4.1%</td><td>3.0%</td><td>+400 bps</td></tr><tr><td>Other/Calendar impact</td><td>0.0%</td><td>6.9%</td><td>0.0%</td><td>+0 bps</td></tr><tr><td>Forex impact</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>+0 bps</td></tr><tr><td>Structural change/other</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>+0 bps</td></tr><tr><td>Operating income/(loss) - Operating</td><td>$ 1,576</td><td>$ 1,531</td><td>$ 1,769</td><td>12.2%</td></tr><tr><td>Operating income/(loss) - Operating Margin (%)</td><td>31.3%</td><td>31.3%</td><td>32.7%</td><td>+146 bps</td></tr></table>

Source: Company, Visible Alpha, Bernstein analysis and estimates

<table><tr><td colspan="3">Visible Alpha Consensus</td></tr><tr><td></td><td>2026 Q2E</td><td>Δ vs Cons</td></tr><tr><td>$</td><td>5,207</td><td>3.8%</td></tr><tr><td></td><td>3.3%</td><td>+394 bps</td></tr><tr><td></td><td>3.3%</td><td>+370 bps</td></tr><tr><td></td><td>2.9%</td><td>+109 bps</td></tr><tr><td></td><td>0.4%</td><td>+262 bps</td></tr><tr><td></td><td>0.0%</td><td>-1 bps</td></tr><tr><td></td><td>0.0%</td><td>+0 bps</td></tr><tr><td>$</td><td>1,641</td><td>7.8%</td></tr><tr><td></td><td>31.5%</td><td>+120 bps</td></tr></table>

Bernstein Estimates 2026 Q2E $\Delta$ vs BERNe

<table><tr><td>$</td><td>5,267</td><td>2.6%</td></tr><tr><td></td><td>4.5%</td><td>+274 bps</td></tr><tr><td></td><td>4.5%</td><td>+250 bps</td></tr><tr><td></td><td>3.0%</td><td>+100 bps</td></tr><tr><td></td><td>1.5%</td><td>+150 bps</td></tr><tr><td></td><td>1.5%</td><td>+150 bps</td></tr><tr><td></td><td>0.0%</td><td>+0 bps</td></tr><tr><td></td><td>0.0%</td><td>-0 bps</td></tr><tr><td></td><td>0.0%</td><td>+0 bps</td></tr><tr><td>$</td><td>1,674</td><td>5.7%</td></tr><tr><td></td><td>31.8%</td><td>+95 bps</td></tr></table>

EXHIBIT 4: KO 2Q26 Segment Results: Actual vs. Bernstein vs. Consensus - APAC

<table><tr><td rowspan="2"></td><td colspan="4">Actual</td></tr><tr><td>2025 Q2</td><td>2026 Q1</td><td>2026 Q2</td><td>YoY Δ</td></tr><tr><td colspan="5">Asia Pacific</td></tr><tr><td>Net operating revenues - Operating</td><td>$ 1,589</td><td>$ 1,505</td><td>$ 1,586</td><td>-0.2%</td></tr><tr><td>Total growth</td><td>5.4%</td><td>4.9%</td><td>-0.2%</td><td>-563 bps</td></tr><tr><td>Organic growth</td><td>5.0%</td><td>4.6%</td><td>2.0%</td><td>-300 bps</td></tr><tr><td>Price/mix</td><td>10.0%</td><td>-5.9%</td><td>-9.0%</td><td>-1900 bps</td></tr><tr><td>Volume growth</td><td>-5.0%</td><td>10.1%</td><td>11.0%</td><td>+1600 bps</td></tr><tr><td>Organic Concentrate Sales Growth</td><td>-5.0%</td><td>3.2%</td><td>11.0%</td><td>+1600 bps</td></tr><tr><td>Other/Calendar impact</td><td>-3.0%</td><td>6.9%</td><td>0.0%</td><td>+300 bps</td></tr><tr><td>Forex impact</td><td>-2.0%</td><td>1.7%</td><td>-1.0%</td><td>+100 bps</td></tr><tr><td>Structural change/other</td><td>-2.0%</td><td>-0.2%</td><td>0.0%</td><td>+200 bps</td></tr><tr><td>Operating income/(loss) - Operating</td><td>$ 664</td><td>$ 533</td><td>$ 661</td><td>-0.5%</td></tr><tr><td>Operating income/(loss) - Operating Margin (%)</td><td>41.8%</td><td>35.4%</td><td>41.7%</td><td>-11 bps</td></tr></table>

Source: Company, Visible Alpha, Bernstein analysis and estimates

<table><tr><td colspan="3">Visible Alpha Consensus</td></tr><tr><td></td><td>2026 Q2E</td><td>Δ vs Cons</td></tr><tr><td>$</td><td>1,617</td><td>-1.9%</td></tr><tr><td></td><td>1.8%</td><td>-197 bps</td></tr><tr><td></td><td>2.1%</td><td>-11 bps</td></tr><tr><td></td><td>-1.1%</td><td>-789 bps</td></tr><tr><td></td><td>3.2%</td><td>+778 bps</td></tr><tr><td></td><td>-0.3%</td><td>-69 bps</td></tr><tr><td></td><td>0.0%</td><td>+0 bps</td></tr><tr><td>$</td><td>668</td><td>-1.0%</td></tr><tr><td></td><td>41.3%</td><td>+40 bps</td></tr></table>

<table><tr><td colspan="3">Bernstein Estimates</td></tr><tr><td></td><td>2026 Q2E</td><td>Δ vs BERNe</td></tr><tr><td>$</td><td>1,557</td><td>1.8%</td></tr><tr><td></td><td>-2.0%</td><td>+180 bps</td></tr><tr><td></td><td>0.5%</td><td>+150 bps</td></tr><tr><td></td><td>-2.0%</td><td>-700 bps</td></tr><tr><td></td><td>2.5%</td><td>+850 bps</td></tr><tr><td></td><td>2.5%</td><td>+850 bps</td></tr><tr><td></td><td>0.0%</td><td>+0 bps</td></tr><tr><td></td><td>-2.5%</td><td>+149 bps</td></tr><tr><td></td><td>0.0%</td><td>+0 bps</td></tr><tr><td>$</td><td>654</td><td>1.1%</td></tr><tr><td></td><td>42.0%</td><td>-32 bps</td></tr></table>

EXHIBIT 5: KO 2Q26 Segment Results: Actual vs. Bernstein vs. Consensus - Bottling Investment

<table><tr><td rowspan="2"></td><td colspan="4">Actual</td></tr><tr><td>2025 Q2</td><td>2026 Q1</td><td>2026 Q2</td><td>YoY Δ</td></tr><tr><td colspan="5">Bottling Investment</td></tr><tr><td>Net operating revenues - Operating</td><td>$ 1,411</td><td>$ 1,640</td><td>$ 1,527</td><td>8.2%</td></tr><tr><td>Total growth</td><td>-8.3%</td><td>12.1

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
