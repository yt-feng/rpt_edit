你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  ✅ 三大情景框架：DCF、P/ARR、EV/Sales
  ✅ 关键变量分析
  ✅ 估值逻辑、假设、终值占比等核心内容覆盖
  ✅ 适合准备 AI 相关面试、研究 AI 估值的同学
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
# EM Money Trail

# EM outflows broadening as well as deepening

EM equity fund outflows exacerbated this week to -\$7.5bn from -\$4.3bn last week. Outflows were equally across ETFs (-\$3.7bn, -\$3.1bn last week) and non-ETFs. The deceleration in non-ETF outflows we noted over the prior two weeks didn't hold this week, with redemptions widening to -\$\$3.8bn (-\$1.2bn last week). All regional funds were net-sold this week. GEMs funds saw a sharp rise in sell-off to -\$3.0bn from -\$363mn last week, while outflows from Asia ex-Japan also picked up to -\$4.4bn from -\$3.6bn last week. Redemptions eased in LatAm (-\$225mn, -\$268mn last week) and EMEA (-\$5mn, -\$75mn last week). EM ex-China funds saw marginal inflows (+\$50mn). YTD, EM equity funds are +\$66.8bn (from a peak of +\$83.3bn in April), of which ETFs are +\$78.2bn and non-ETFs are -\$11.5bn.

Market-level flows. Taiwan continued to attract subscriptions for the second week, albeit slower (+\$3.8bn, +\$8.7bn last week) while redemptions in Korea worsened again (-\$7.5bn) after easing to -\$1.3bn last week. Outflows in Korea have added up to -\$37.6bn in the past four weeks and -\$69.6bn YTD (see report for a detailed discussion). Outflows worsened sharply in India (-\$4.1bn, from -\$454mn last week) but continued to slow in Brazil (-\$394mn, from -\$473mn last week). Thailand (+\$147mn, +\$17mn last week) was the only market besides Taiwan that saw inflows. The rest of EM ASEAN saw large outflows: Malaysia (-\$625mn), Indonesia (-\$612mn), and the Philippines (-\$124mn). In EMEA, Qatar (-\$65mn), Dubai (-\$41mn) and Türkiye (-\$91mn, one-week lag) saw moderate outflows.

Table 1: Regional fund flows 

<table><tr><td rowspan="2">USD billion</td><td colspan="3">Flows</td><td></td><td></td></tr><tr><td>Current</td><td>YTD</td><td>vs 1w</td><td>Min</td><td>27-Ma</td></tr><tr><td>EM Equities</td><td>-7.5</td><td>66.8</td><td>▼</td><td>-7.5</td><td></td></tr><tr><td>GEMs</td><td>-3.0</td><td>58.3</td><td>▼</td><td>-3.0</td><td></td></tr><tr><td>GEMs ex-China</td><td>0.1</td><td>7.0</td><td>▲</td><td>-0.4</td><td></td></tr><tr><td>APAC</td><td>-4.4</td><td>-2.3</td><td>▼</td><td>-5.0</td><td></td></tr><tr><td>EMEA</td><td>0.0</td><td>1.4</td><td>▲</td><td>-0.1</td><td></td></tr><tr><td>LatAm</td><td>-0.2</td><td>9.4</td><td>▲</td><td>-0.4</td><td></td></tr><tr><td>Dev. Europe</td><td>-1.0</td><td>-4.0</td><td>▲</td><td>-4.7</td><td></td></tr><tr><td>US</td><td>20.7</td><td>196.1</td><td>▲</td><td>-40.5</td><td></td></tr><tr><td>International</td><td>17.6</td><td>260.2</td><td>▲</td><td>-7.3</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>Outflow</td><td>Zero Inflow</td></tr></table>

Source: EPFR Global. Note: Ex-onshore funds for EM. Total EM Equities include GEMs, LatAm, EMEA and Asia ex-Japan.

Figure 1: Weekly EM equity fund flows: ETF vs non-ETF   
![](images/4cde04cf2c157cd3e90417e172f4768ed40fd6c50aee58b5b39e541283212a49.jpg)

<details>
<summary>bar</summary>

| Date   | ETF  | Non-ETF |
|--------|------|---------|
| Jun-24 | -1   | 0       |
| Oct-24 | 10   | -1      |
| Feb-25 | -5   | 0       |
| Jun-25 | 5    | -1      |
| Oct-25 | 5    | -1      |
| Feb-26 | 15   | -1      |
| Jun-26 | -8   | 0       |
</details>

Source: EPFR Global, MSCI

Figure 2: Annual cumulative EM equity fund flows (US\$ bn)   
![](images/de3d9a24746dc4d712a379f8188858f283f7b89c503e6f1bd609d99e32566354.jpg)

<details>
<summary>line</summary>

| Month | 2022 | 2023 | 2024 | 2025 | 2026 |
|-------|------|------|------|------|------|
| Jan   |      |      |      |      | 40.0 |
| Feb   |      |      |      |      | 80.0 |
| Mar   |      |      |      |      | 70.0 |
| Apr   |      |      |      |      | 85.0 |
| May   |      |      |      |      | 75.0 |
| Jun   |      |      |      |      | 66.8 |
| Jul   |      |      |      |      |      |
| Aug   |      |      |      |      |      |
| Sep   |      |      |      |      |      |
| Oct   |      |      |      |      |      |
| Nov   |      |      |      |      |      |
| Dec   |      | 3.9  | -33.3| 29.2 |      |
</details>

Source: EPFR Global. \*Excludes onshore funds.

# Emerging Markets Equity Strategy

# Rajiv Batra AC

(65) 6882-8151

rajiv.j.batra@JPM.com

JPM Securities Singapore Private Limited

# Emy Shayo Cherman AC

(55-11) 4950-6684

emy.shayo@JPM.com

Banco JPM S.A

# Anindita Gandhi AC

(91-22) 6157-3248

anindita.gandhi@JPM.com

JPM India Private Limited

# CEEMEA Equity Strategy

# David Aserkoff, CFA

(44-20) 7134-5887

david.aserkoff@JPM.com

JPM Securities plc

Table 2: Summary – Market data and net foreign investment, 28 May - 3 June 2026 

<table><tr><td rowspan="2"></td><td colspan="10">Net Flows ($mn)</td></tr><tr><td>Current</td><td>ETF</td><td>Non-ETF</td><td>Last Week</td><td>4W</td><td>8W</td><td>3M</td><td>12M</td><td>YTD</td><td>AUM</td></tr><tr><td>Total EM Equity Funds*</td><td>(7,543)</td><td>(3,726)</td><td>(3,817)</td><td>(4,322)</td><td>(13,645)</td><td>(9,531)</td><td>(21,445)</td><td>117,959</td><td>66,776</td><td>2,632,627</td></tr><tr><td>ETFs</td><td>(3,726)</td><td>(3,726)</td><td>--</td><td>(3,086)</td><td>(1,275)</td><td>7,882</td><td>1,750</td><td>157,703</td><td>78,232</td><td>1,046,585</td></tr><tr><td>Non-ETFs</td><td>(3,817)</td><td>--</td><td>(3,817)</td><td>(1,236)</td><td>(12,370)</td><td>(17,414)</td><td>(23,195)</td><td>(39,744)</td><td>(11,456)</td><td>1,586,042</td></tr><tr><td>GEMs Equity Funds*</td><td>(2,953)</td><td>(388)</td><td>(2,564)</td><td>(363)</td><td>(6,688)</td><td>(3,090)</td><td>(3,608)</td><td>96,071</td><td>58,294</td><td>1,871,288</td></tr><tr><td>GEMs ex-China Equity Funds*</td><td>50</td><td>6</td><td>44</td><td>5</td><td>32</td><td>1,043</td><td>3,854</td><td>7,111</td><td>6,959</td><td>47,083</td></tr><tr><td>Asia ex-Japan Equity Funds*</td><td>(4,360)</td><td>(3,151)</td><td>(1,209)</td><td>(3,616)</td><td>(5,793)</td><td>(8,108)</td><td>(19,665)</td><td>6,630</td><td>(2,317)</td><td>685,382</td></tr><tr><td>EMEA Equity Funds*</td><td>(5)</td><td>(2)</td><td>(3)</td><td>(75)</td><td>(261)</td><td>(234)</td><td>(642)</td><td>3,050</td><td>1,444</td><td>29,437</td></tr><tr><td>LatAm Equity Funds*</td><td>(225)</td><td>(185)</td><td>(40)</td><td>(268)</td><td>(903)</td><td>1,900</td><td>2,470</td><td>12,208</td><td>9,355</td><td>46,520</td></tr><tr><td>Developed Europe Equity Funds</td><td>(1,048)</td><td>(692)</td><td>(357)</td><td>(1,609)</td><td>(6,505)</td><td>(17,821)</td><td>(23,829)</td><td>7,266</td><td>(3,963)</td><td>2,274,063</td></tr><tr><td>US Equity Funds</td><td>20,714</td><td>31,522</td><td>(10,807)</td><td>8,459</td><td>60,558</td><td>124,554</td><td>181,788</td><td>450,496</td><td>196,068</td><td>27,197,029</td></tr><tr><td>International Equity Funds</td><td>17,599</td><td>19,206</td><td>(1,608)</td><td>8,443</td><td>57,159</td><td>103,197</td><td>144,647</td><td>444,379</td><td>260,190</td><td>11,600,869</td></tr><tr><td colspan="11">Stock Exchanges Investors Trading Data **</td></tr><tr><td>Japan (1 wk lag)***</td><td>(3,084)</td><td>-</td><td>-</td><td>6,787</td><td>18,860</td><td>63,697</td><td>30,070</td><td>114,673</td><td>70,541</td><td>-</td></tr><tr><td>Korea</td><td>(7,526)</td><td>-</td><td>-</td><td>(1,308)</td><td>(35,523)</td><td>(33,011)</td><td>(56,339)</td><td>(62,866)</td><td>(69,586)</td><td>-</td></tr><tr><td>Taiwan</td><td>3,768</td><td>-</td><td>-</td><td>8,662</td><td>6,596</td><td>15,901</td><td>(5,589)</td><td>5,978</td><td>650</td><td>-</td></tr><tr><td>India</td><td>(4,075)</td><td>-</td><td>-</td><td>(454)</td><td>(6,034)</td><td>(9,077)</td><td>(25,796)</td><td>(35,327)</td><td>(27,694)</td><td>-</td></tr><tr><td>Brazil (2 day lag)***</td><td>(394)</td><td>-</td><td>-</td><td>(473)</td><td>(2,886)</td><td>(2,887)</td><td>(339)</td><td>8,459</td><td>7,587</td><td>-</td></tr><tr><td>Thailand</td><td>147</td><td>-</td><td>-</td><td>17</td><td>297</td><td>80</td><td>(929)</td><td>(185)</td><td>933</td><td>-</td></tr><tr><td>Saudi Arabia (2 wk lag)***</td><td>267</td><td>-</td><td>-</td><td>(109)</td><td>(21)</td><td>971</td><td>696</td><td>7,849</td><td>2,946</td><td>-</td></tr><tr><td>Indonesia</td><td>(612)</td><td>-</td><td>-</td><td>(263)</td><td>(403)</td><td>(1,179)</td><td>(2,887)</td><td>(1,408)</td><td>(3,288)</td><td>-</td></tr><tr><td>Malaysia</td><td>(625)</td><td>-</td><td>-</td><td>(182)</td><td>(1,103)</td><td>(1,114)</td><td>(1,067)</td><td>(3,404)</td><td>(692)</td><td>-</td></tr><tr><td>Philippines</td><td>(124)</td><td>-</td><td>-</td><td>(23)</td><td>(166)</td><td>(308)</td><td>(614)</td><td>(601)</td><td>(230)</td><td>-</td></tr><tr><td>Qatar</td><td>(65)</td><td>-</td><td>-</td><td>(19)</td><td>(162)</td><td>(257)</td><td>(531)</td><td>538</td><td>20</td><td>-</td></tr><tr><td>Dubai</td><td>(41)</td><td>-</td><td>-</td><td>11</td><td>(244)</td><td>(476)</td><td>(1,900)</td><td>(784)</td><td>(1,311)</td><td>-</td></tr><tr><td>Türkiye (1 wk lag)***</td><td>(91)</td><td>-</td><td>-</td><td>(293)</td><td>(454)</td><td>426</td><td>(1,008)</td><td>3,627</td><td>1,407</td><td>-</td></tr><tr><td>Vietnam</td><td>(118)</td><td>-</td><td>-</td><td>(321)</td><td>(675)</td><td>(1,296)</td><td>(1,926)</td><td>(5,724)</td><td>(2,444)</td><td>-</td></tr><tr><td>Pakistan</td><td>(3)</td><td>-</td><td>-</td><td>(9)</td><td>(20)</td><td>(15)</td><td>(62)</td><td>(690)</td><td>(415)</td><td>-</td></tr><tr><td>Sri Lanka</td><td>(5)</td><td>-</td><td>-</td><td>(10)</td><td>(16)</td><td>(35)</td><td>(52)</td><td>(198)</td><td>(104)</td><td>-</td></tr><tr><td colspan="11">Monthly Tracking of Cross Border Funds****</td></tr><tr><td>Australia</td><td>829</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>2,251</td><td>6,029</td><td>2,985</td><td>-</td></tr><tr><td>Hong Kong</td><td>797</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1,903</td><td>14,063</td><td>3,063</td><td>-</td></tr><tr><td>Singapore</td><td>489</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1,171</td><td>3,769</td><td>1,993</td><td>-</td></tr><tr><td>China</td><td>2,744</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>6,721</td><td>35,749</td><td>17,065</td><td>-</td></tr><tr><td>Mexico</td><td>773</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>2,010</td><td>5,020</td><td>3,454</td><td>-</td></tr><tr><td>Chile</td><td>244</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>455</td><td>1,913</td><td>1,083</td><td>-</td></tr><tr><td>Poland</td><td>274</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>757</td><td>2,704</td><td>1,548</td><td>-</td></tr><tr><td>Peru</td><td>177</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>470</td><td>1,332</td><td>1,006</td><td>-</td></tr><tr><td>Colombia</td><td>87</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>171</td><td>515</td><td>321</td><td>-</td></tr></table>

Source: Bloomberg Finance L.P., JPM, EPFR Global data. \*Total EM Equity includes GEMs, LatAm, EMEA and Asia ex-Japan and excludes onshore funds (DM funds figures represent total inflows). \*\*Net foreign flows data from local stock exchanges. \*\*\*Data for Japan is for 23 - 29 May 2026. Data for Brazil is for 27 May - 1 June 2026. Data for Saudi Arabia is for 15 - 21 May 2026. Data for Türkiye is for 23 - 29 May 2026. \*\*\*\*Monthly tracking of cross-border fund (EPFR) flows – data is until April 2026.

For markets that do not publish official foreign transactions in their equity markets, we use monthly data from EPFR Global (they cover 12,000 international, EM and US funds with total net assets greater than US\$6.0trn).

During the month of April, funds were net buyers in Australia, Hong Kong, Singapore, China, Mexico, Poland, Chile, Peru and Colombia. Please see page 21 for consensus overweight and underweight markets.

# EM Equity Funds: Flows

Figure 3: EM equity fund flows vs performance   
![](images/7ebfc95c4809d4ae3713faf2ab8b4254c90186a23976d5d0f438e3fc4aca4799.jpg)

<details>
<summary>line</summary>

| Year | EM Equity Flows (US$bn) | MSCI EM (rhs) |
|------|--------------------------|---------------|
| 2004 | ~10                      | ~400          |
| 2005 | ~30                      | ~600          |
| 2006 | ~60                      | ~900          |
| 2007 | ~100                     | ~1300         |
| 2008 | ~150                     | ~1800         |
| 2009 | ~30                      | ~400          |
| 2010 | ~100                     | ~800          |
| 2011 | ~150                     | ~1100         |
| 2012 | ~200                     | ~1300         |
| 2013 | ~250                     | ~1500         |
| 2014 | ~200                     | ~1300         |
| 2015 | ~150                     | ~1100         |
| 2016 | ~100                     | ~800          |
| 2017 | ~150                     | ~1100         |
| 2018 | ~200                     | ~1300         |
| 2019 | ~150                     | ~1100         |
| 2020 | ~100                     | ~800          |
| 2021 | ~150                     | ~1100         |
| 2022 | ~250                     | ~1300         |
| 2023 | ~350                     | ~1500         |
| 2024 | ~300                     | ~1300         |
| 2025 | ~350                     | ~1500         |
| 2026 | ~400                     | ~1800         |
</details>

Source: EPFR Global, MSCI. \*Excludes onshore funds

Figure 5: Annual EM equity fund flows: Offshore vs onshore   
![](images/be350b34aaadf9bbff1987e51547bd05bd6addce6287bd0d9ebf7cc37551f828.jpg)

<details>
<summary>bar_stacked</summary>

| Year | Onshore (US$ bn) | Offshore (US$ bn) |
| :--- | :--- | :--- |
| 2017 | 80 | 63 |
| 2018 | 65 | 16 |
| 2019 | 15 | -12 |
| 2020 | -15 | -20 |
| 2021 | 100 | 101 |
| 2022 | 90 | -4 |
| 2023 | 70 | 4 |
| 2024 | 232 | -33 |
| 2025 | 160 | 29 |
| 2026 | -165 | 67 |
</details>

Source: EPFR Global

Figure 7: Weekly flows into EM equity funds: Global vs regional funds   
![](images/c2b6d2ff9ed61dd3bd98af47d500f2b16fe229312bd46e2c3e1bf404556f11bb.jpg)

<details>
<summary>bar</summary>

| Month    | Regional | GEM  |
| -------- | -------- | ---- |
| Jun-24   | -1.5     | -0.5 |
| Oct-24   | 9.0      | 0.0  |
| Feb-25   | -3.0     | 0.5  |
| Jun-25   | 3.5      | 1.0  |
| Oct-25   | 5.0      | 2.0  |
| Feb-26   | 14.0     | 8.0  |
| Jun-26   | -6.0     | -1.0 |
</details>

Source: EPFR Global. \* Excludes onshore funds

Figure 4: Weekly flows into EM equity funds: By domicile   
![](images/cb04a7ffd57dbbb8763e430f1569ba6340ab6113b9e4b24da33bafb9cc24ee9d.jpg)

<details>
<summary>bar</summary>

| Month   | Europe | US  | Other |
|---------|--------|-----|-------|
| May-24  | -1.5   | -1.8| -1.7  |
| Oct-24  | -1.6   | 7.2 | 10.5  |
| Mar-25  | -1.7   | -3.5| -7.8  |
| Aug-25  | -1.8   | 2.5 | 3.0   |
| Jan-26  | 3.0    | 10.0| 13.5  |
| May-26  | -1.9   | -3.0| -6.5  |
</details>

Source: EPFR Global. \*Excludes onshore funds

Figure 6: Annual EM equity fund flows: ETF vs non-ETF   
![](images/ab9ac1ab651123d1c309374897a652998f42e933dc070a175c8abb321988696c.jpg)

<details>
<summary>bar_stacked</summary>

| Year | Non-ETFs (US$ bn) | ETF (US$ bn) |
| :--- | :--- | :--- |
| 2021 | 41 | 60 |
| 2022 | -59 | 55 |
| 2023 | -36 | 40 |
| 2024 | -54 | 21 |
| 2025 | -61 | 90 |
| 2026 | -11 | 78 |
</details>

Source: EPFR Global

Figure 8: Weekly flows into EM equity funds: Breakdown of regional funds   
![](images/1ac06fabc3a37a298af5968580ea51e7b0d683abd6507f51621aa2f2117d699e.jpg)

<details>
<summary>bar</summary>

| Month   | LatAm | EMEA | AxJp |
|---------|-------|------|------|
| Jun-24  |       |      | 0.5  |
| Jul-24  |       |      | -1.0 |
| Aug-24  |       |      | -2.5 |
| Sep-24  |       |      | -3.0 |
| Oct-24  |       |      | 9.0  |
| Nov-24  |       |      | 1.5  |
| Dec-24  |       |      | -6.0 |
| Jan-25  |       |      | -1.5 |
| Feb-25 

[中间内容因长度限制已省略]

rmance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 05 Jun 2026 01:42 PM HKT

Disseminated 05 Jun 2026 01:43 PM HKT
"""
