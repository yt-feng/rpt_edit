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
# China EV Tracker

# Exports offset soft domestic demand

- Domestic demand remains soft; new model cycle could support recovery into 2H   
- Exports remain the key growth and profitability anchor for China OEMs   
- Prefer technology leaders with strong product cycles and overseas exposure

# Domestic demand remains under pressure; full-year demand revised lower.

April China EV retail sales reached 848k units, flat m-o-m, but down 6% y-o-y, while total passenger car demand fell 21% y-o-y. The backdrop reflects fading policy support, residual effects from pulled-forward demand, and continued weakness in ICE demand amid elevated oil prices. The soft tone has continued into early May. Domestic passenger car sales for 1–10 May were again down 21% y-o-y, and elevated channel inventories point to ongoing destocking pressure across the industry. Meanwhile, lithium prices have risen to around RMB200k. BYD announced price increases effective in May to offset raw material cost inflation since the start of the year, with several other OEMs following. We see these price hikes as an additional near-term headwind to demand. Against the backdrop, we lower our 2026 domestic demand forecast (see page 9).

New model cycles and technology upgrades to gradually improve industry sentiment in 2H26. As subsidies taper, competitive intensity is shifting from last year's entry-level EV segment to this year's premium market. Recent launches continue to demonstrate strong consumer engagement, particularly for large-size SUVs integrating advanced ADAS, electrification and smart cockpit features at increasingly competitive prices. BYD's Da Tang secured c100k orders within two weeks of pre-sale, and further launches are expected in May, including the Li Auto L9 Livis, ONVO L80, XPeng GX and NIO ES9. We believe competition is gradually evolving from pure pricing toward technology integration and user experience.

Export momentum continues to support OEM profitability. China passenger car exports reached 2.7m units in 4M26, up $69\%$ y-o-y, led by Chery, BYD and Geely. Growth was primarily EV-driven, with the EV mix rising to $49\%$ from $38\%$ in 4M25. This strength reflects both competitive products and macro tailwinds including higher oil prices that enhance EV total cost of ownership. With domestic demand still subdued, exports remain an important support for utilisation, earnings resilience and mix improvement.

Stock highlights. We continue to favour technology leaders with clearer earnings visibility. BYD: Technology upgrade and strong new model cycle should drive a volume recovery. We remain positive on its longer-term ecosystem value and its growth potential in overseas market expansion. Geely: Resilient in profitability on better product mix, well positioned for volume opportunity from new models and overseas. XPeng: Improving fundamentals by new launch of GX, optionality from its Robotaxi and robotics narratives may attract growth/tech flows. NIO: Better visibility on its 2026e volume growth and earnings improvement, driven by new models and core portfolio growth (especially ES8). CATL: Remains our preferred core holding, supported by strong earnings visibility, market-share defence and growth from ESS and overseas markets.

# Equities Automobiles & Auto Components

China

# Yuqian Ding\*

Head of China Autos Research

The Hongkong and Shanghai Banking Corporation Limited
yuqian.ding@hsbc.com.hk

+852 2288 5108

# Li Yang\*

Analyst, China Autos

The Hongkong and Shanghai Banking Corporation Limited
li01.yang@hsbc.com.hk

+852 2288 6216

# Elaine Chen\* (Reg. No. S1700524030001)

Analyst, China Autos

HSBC Qianhai Securities Limited

elaine.chen@hsbcqh.com.cn

+86 010 5795 2364

\* Employed by a non-US affiliate of HSBC Securities (USA) Inc, and is not registered/ qualified pursuant to FINRA regulations.

# Disclosures & Disclaimer

This report must be read with the disclosures and the analyst certifications in the Disclosure appendix, and with the Disclaimer, which forms part of it.

Issuer of report: The Hongkong and Shanghai Banking Corporation Limited

View HSBC Global Investment Research at:

https://www.research.hsbc.com

Exhibit 1. Stock valuations 

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Company</td><td rowspan="2">Rating</td><td rowspan="2">Ccy.</td><td rowspan="2">Market Cap (USDm)</td><td colspan="5">3M</td><td colspan="3">PE</td><td colspan="3">EPS growth</td><td colspan="3">PB</td><td colspan="3">ROE</td></tr><tr><td>ADTV (USDm)</td><td>Close price</td><td>Target price</td><td>Upside</td><td>2026e</td><td>2027e</td><td>2028e</td><td>2026e</td><td>2027e</td><td>2028e</td><td>2026e</td><td>2027e</td><td>2028e</td><td>2026e</td><td>2027e</td><td>2028e</td><td></td></tr><tr><td>002594 CH</td><td>BYD A</td><td>Buy</td><td>CNY</td><td>125,223</td><td>908</td><td>98.73</td><td>126.00</td><td>28%</td><td>22.4</td><td>16.5</td><td>14.2</td><td>23%</td><td>36%</td><td>16%</td><td>3.3</td><td>3.0</td><td>2.7</td><td>16%</td><td>19%</td><td>20%</td><td></td></tr><tr><td>1211 HK</td><td>BYD H</td><td>Buy</td><td>HKD</td><td>125,223</td><td>406</td><td>98.15</td><td>146.00</td><td>49%</td><td>19.3</td><td>14.2</td><td>12.2</td><td>23%</td><td>36%</td><td>16%</td><td>2.9</td><td>2.6</td><td>2.3</td><td>16%</td><td>19%</td><td>20%</td><td></td></tr><tr><td>175 HK</td><td>Geely</td><td>Buy</td><td>HKD</td><td>29,270</td><td>232</td><td>21.26</td><td>32.00</td><td>51%</td><td>8.7</td><td>7.0</td><td>6.6</td><td>30%</td><td>24%</td><td>7%</td><td>1.7</td><td>1.5</td><td>1.3</td><td>22%</td><td>23%</td><td>21%</td><td></td></tr><tr><td>XPEV US</td><td>XPeng</td><td>Buy</td><td>USD</td><td>12,620</td><td>112</td><td>16.12</td><td>27.70</td><td>72%</td><td>51.0</td><td>21.6</td><td>N/A</td><td>240%</td><td>136%</td><td>N/A</td><td>3.2</td><td>2.8</td><td>N/A</td><td>7%</td><td>14%</td><td>N/A</td><td></td></tr><tr><td>NIO US</td><td>NIO</td><td>Buy</td><td>USD</td><td>14,360</td><td>229</td><td>6.25</td><td>6.80</td><td>9%</td><td>N/A</td><td>303.4</td><td>105.0</td><td>93%</td><td>128%</td><td>189%</td><td>8.4</td><td>8.1</td><td>7.6</td><td>-9%</td><td>3%</td><td>7%</td><td></td></tr><tr><td>300750 CH</td><td>CATL</td><td>Buy</td><td>CNY</td><td>296,534</td><td>2,145</td><td>427.00</td><td>547.00</td><td>28%</td><td>19.6</td><td>16.6</td><td>14.6</td><td>37%</td><td>18%</td><td>14%</td><td>4.9</td><td>4.3</td><td>3.8</td><td>27%</td><td>28%</td><td>28%</td><td></td></tr><tr><td>3750 HK</td><td>CATL H</td><td>Buy</td><td>HKD</td><td>296,534</td><td>339</td><td>686.00</td><td>790.00</td><td>15%</td><td>27.3</td><td>23.1</td><td>20.2</td><td>37%</td><td>18%</td><td>14%</td><td>6.9</td><td>6.0</td><td>5.2</td><td>27%</td><td>28%</td><td>28%</td><td></td></tr></table>

Note: Priced as of 14 May 2026.
Source: WIND, HSBC estimates

# Sector highlights

Exhibit 2. China EV market: Top 10 EV makers took $71\%$ market share in 4M26   
![](images/0718671f1227130f4ffd69ee0d4855fc15cc951c707722fba42a41a521a18888.jpg)

<details>
<summary>bar</summary>

| Brand | Market Share (%) |
| :--- | :--- |
| BYD | 20.5 |
| Geely | 13.0 |
| Changan | 7.0 |
| Tesla Li | 5.0 |
| Leap | 4.8 |
| Xiaomi | 4.5 |
| Nio Wuling | 4.2 |
| Seres | 3.8 |
| Top 10 took 71% market share in 4M26 (vs. 75% in 2025, 78% in 2024) |
| Long tail: 47 brands are competing for the remaining 29% of the market
</details>

Source: CPCA, HSBC

Exhibit 3. China ICE car market: Top 10 brands took $73\%$ share in 1Q26   
![](images/45fa7a60f1dfb238f9fa71b9c80584d4bea20b7fbd2783c03203f174266df069.jpg)

<details>
<summary>bar</summary>

| Brand | 1Q26 ICE Market Share (%) |
| :--- | :--- |
| VW | 15.8 |
| Toyota | 13.0 |
| Geely | 9.0 |
| Audi | 5.5 |
| BMW | 5.0 |
| Chery | 4.5 |
| Honda | 4.5 |
| Nissan | 4.5 |
| Benz | 4.5 |
Top 10 took 73% market share in 1Q26 (vs 72% in 2025, 71% in 2024). Long tail: 69 brands are competing for the remaining 27% of the market (vs. 74 brands in 2025, 82 brands in 2024).
</details>

Source: CAAM, HSBC

Exhibit 4. China overall passenger car market: Top 15 brands took $62\%$ share in 1Q26   
![](images/31d74107c915511dfea4428b608e1a7fd19217f22d81f0e99c539fc2ccce9033.jpg)

<details>
<summary>bar</summary>

| Brand | Market Share (%) |
| :--- | :--- |
| VW | 9.5 |
| Toyota | 7.8 |
| BYD | 7.0 |
| Geely | 6.5 |
| Changan | 3.0 |
| Audi | 2.8 |
| Nissan | 2.5 |
| BMW | 2.3 |
| Tesla | 2.2 |
| Honda | 2.1 |
| Wuling | 2.0 |
| Benz | 1.8 |
| Li Auto | 1.7 |
| Buick | 1.6 |
Top 15 took 62% market share in 1Q26 (vs. 63% in 2025, 68% in 2024)
Long tail: 138 brands are competing for the remaining 38% of the market (vs. 145 brands in 2025, 150 brands in 2024)
</details>

Source: CAAM, HSBC

# Most frequently discussed charts of the month

Exhibit 5. China passenger car export volume booked $69\%$ y-o-y growth in 4M26   
![](images/ea49a7b0c982cd1eda09bc0a492032eb7289b54f0e088dfcd06ac06e45ca661c.jpg)

<details>
<summary>bar</summary>

China PC export volume (in units)
| Month | 2024 | 2025 | 2026 |
|---|---|---|---|
| Jan | 375,000 | 395,000 | 585,000 |
| Feb | 315,000 | 365,000 | 585,000 |
| Mar | 425,000 | 415,000 | 745,000 |
| Apr | 430,000 | 435,000 | 795,000 |
| May | 395,000 | 475,000 | - |
| Jun | 405,000 | 505,000 | - |
| Jul | 395,000 | 505,000 | - |
| Aug | 435,000 | 535,000 | - |
| Sep | 455,000 | 565,000 | - |
| Oct | 465,000 | 575,000 | - |
| Nov | 425,000 | 635,000 | - |
| Dec | 425,000 | 645,000 | - |
</details>

Source: CPCA, HSBC

Exhibit 6. Chery, BYD and Geely lead China's passenger car export volume in 4M26   
![](images/dae6c31b99fb19b4c80d74b7167dbdb91335c15db13b28b924ecedb0a5a97533.jpg)

<details>
<summary>pie</summary>

| Company | Share (%) |
| :--- | :--- |
| Chery | 21 |
| BYD | 18 |
| Geely | 6 |
| SAIC | 9 |
| Changan | 6 |
| GWM | 6 |
| Tesla | 6 |
| Wuling | 4 |
| Leapmotor | 2 |
| Yueda KIA | 2 |
| Others | 16 |
</details>

Source: CPCA, HSBC

Exhibit 7. EV penetration rate rose to 61% in April 2026   
![](images/ee13d5a849ed08e6efe0f22396522845f948e3a8deba7d794523326ffaffa685.jpg)

<details>
<summary>bar_line</summary>

| Month | 2026 EV (PV) retail volume | 2025 EV (PV) retail volume | 2026 monthly penetration rate (RHS) (%) | 2025 monthly penetration rate (RHS) (%) |
|---|---|---|---|---|
| Jan | 480,000 | 720,000 | 38.6 | 44.9 |
| Feb | 500,000 | 750,000 | 44.9 | 48.1 |
| Mar | 800,000 | 850,000 | 51.7 | 53.1 |
| Apr | 850,000 | 950,000 | 61.3 | 55.3 |
| May | - | 1,050,000 | - | 56.4 |
| Jun | - | 1,100,000 | - | 56.7 |
| Jul | - | 1,120,000 | - | 57.1 |
| Aug | - | 1,130,000 | - | 57.5 |
| Sep | - | 1,300,000 | - | 58.9 |
| Oct | - | 1,320,000 | - | 59.3 |
| Nov | - | 1,330,000 | - | 60.1 |
| Dec | - | 1,350,000 | - | 60.5 |
</details>

Source: CPCA, HSBC

Exhibit 8. Overall auto retail sales decreased 21% y-o-y in April 2026   
![](images/4659f7c5f1f68970d9163ea64b5a031f9544b1dac16c7a1b5a7b7c48f21f4ec4.jpg)

<details>
<summary>bar_line</summary>

| Month | 2026 monthly sales volume | 2025 monthly sales volume | 2026 y-o-y growth (%) | 2025 y-o-y growth (%) |
|---|---|---|---|---|
| Jan | 1,550,000 | 1,800,000 | -12 | -14 |
| Feb | 1,050,000 | 1,350,000 | -25 | 25 |
| Mar | 1,650,000 | 1,950,000 | -15 | 15 |
| Apr | 1,350,000 | 1,750,000 | -21 | 14 |
| May | 1,850,000 | 1,850,000 | 13 | 18 |
| Jun | 2,050,000 | 2,050,000 | 18 | 7 |
| Jul | 1,850,000 | 2,050,000 | 6 | 6 |
| Aug | 1,850,000 | 2,150,000 | 6 | 6 |
| Sep | 1,850,000 | 2,350,000 | 0 | -8 |
| Oct | 2,350,000 | 2,350,000 | -8 | -14 |
| Nov | 2,350,000 | 2,350,000 | -14 | -14 |
The chart includes a bar chart (red) and a line chart (gray). The data is already in English. The labels 'Jan' through 'Dec' appear above the bars. The percentage change indicators are shown above each bar.
</details>

Source: CPCA, HSBC

Exhibit 9. Geely is the top share gainer in the China passenger car market in 4M26   
![](images/71fd0ab67ff77679be24c5c37939c2e3d712f4fd6e37f5bf168e6e8a1208c8a9.jpg)

<details>
<summary>bar</summary>

| Company | Market share change (1Q26 vs. 2025) (%) |
| :--- | :--- |
| BYD | -4.8 |
| Chery | -0.7 |
| SAIC Wuling | -0.9 |
| FAW Bestune | -0.3 |
| GAC Honda | -0.2 |
| FAW VW | 0.6 |
| Li Auto | 0.7 |
| NIO | 0.8 |
| GAC Toyota | 1.1 |
| Geely | 1.4 |
</details>

Note: This chart shows the top 5 OEMs gaining and losing market shares in 2025 China passenger car market. Source: CPCA, HSBC

Exhibit 10. Passive mix uplift in premium segment due to low-end slump in 1Q26   
![](images/9f9d576836c51bcc45ca3f00e281e436e65fce2e9ade3eac9a382dc21c4f0804.jpg)

<details>
<summary>bar_stacked</summary>

| Year | Above RMB300k (%) | RMB200k-300k (%) | RMB150k-200k (%) | RMB100k-150k (%) | Below RMB100k (%) |
|---|---|---|---|---|---|
| 1Q26 | 14 | 20 | 20 | 30 | 17 |
| 2025 | 13 | 17 | 19 | 31 | 20 |
| 2024 | 15 | 18 | 18 | 34 | 14 |
| 2023 | 15 | 17 | 18 | 34 | 15 |
| 2022 | 12 | 18 | 17 | 35 | 19 |
| 2021 | 11 | 16 | 16 | 34 | 23 |
| 2020 | 11 | 14 | 16 | 36 | 24 |
| 2019 | 9 | 11 | 15 | 36 | 29 |
</details>

Source: CPCA, HSBC

Exhibit 11. China EV sales volume booked -17% y-o-y decline in 4M26   
![](images/db7b2822b49c5fd4c6d46b7feffcad1fae92a6297e8e15d018dd3c9312cfa02e.jpg)

<details>
<summary>line</summary>

| Year | BEV volume growth y-o-y (%) | PHEV+EREV volume growth y-o-y (%) |
|---|---|---|
| 2022 | 73 | 160 |
| 2023 | 21 | 83 |
| 2024 | 23 | 77 |
| 2025 | 8 | 24 |
| 4M26 | -22 | -14 |
</details>

Source: CPCA, HSBC

Exhibit 12. In 4M26, BEV mix in China EV sales volume increased to 64%   
![](images/33305e5072138d65913a26ec38a479739d9c68e28215926ca405aff321606c0a.jpg)

<details>
<summary>bar_stacked</summary>

| Year | BEV (%) | PHEV/EREV (%) |
|---|---|---|
| 2023 EV mix | 67 | 33 |
| 2024 EV mix | 58 | 42 |
| 2025 EV mix | 61 | 39 |
| 4M26 EV mix | 64 | 36 |
</details>

Source: CPCA, HSBC

Exhibit 13. China's EV passenger vehicle discount level rises slightly m-o-m to $10.9\%$ in April 2026   
![](images/e97e4ee8cf69ed4590481d7551f24147ec7e5d780cceb8dbda548fc583606eb1.jpg)

<details>
<summary>line</summary>

| Month | 2024 (%) | 2025 (%) | 2026 (%) |
|---|---|---|---|
| Jan | 5.3 | 8.4 | 10.1 |
| Feb | 7.9 | 9.9 | 10.4 |
| Mar | 8.6 | 10.6 | 10.6 |
| Apr | 10.8 | 8.4 | 10.9 |
| May | 12.1 | 9.9 | - |
| Jun | - | 9.2 | - |
| Jul | 7.1 | 9.2 | - |
| Aug | 6.8 | 9.5 | - |
| Sep | 7.3 | 10.2 | - |
| Oct | 7.8 | 9.8 | - |
| Nov | 7.1 | 10.1 | - |
| Dec | 7.0 | 10.1 | 0.1 |
</details>

Source: CPCA, HSBC

Exhibit 14. China's ICE passenger vehicle discount level decreased m-o-m to $22.1\%$ in April 2026   
![](images/aa39235e833c6b898001beb2fb0958b74c3bec8fbf34e09479c113c0dc603ae6.jpg)

<details>
<summary>line</summary>

| Month | 2025 (%) | 2024 (%) | 2026 (%) |
|---|---|---|---|
| Jan | 22.0 | 18.3 | 23.7 |
| Feb | 21.7 | 18.0 | 23.5 |
| Mar | 21.9 | 18.1 | 22.7 |
| Apr | 22.4 | 18.7 | 22.1 |
| May | 23.0 | 19.5 | - |
| Jun | 23.5 | 20.8 | - |
| Jul | 23.6 | 21.5 | - |
| Aug | 23.0 | 21.8 | - |
| Sep | 24.0 | 21.7 | - |
| Oct | 24.1 | 21.4 | - |
| Nov | 24.1 | 21.6 | - |
| Dec | 24.0 | 21.5 | - |
</details>

Source: CPCA, HSBC

Exhibit 15. New model launches expected to peak in 2Q26 and 4Q26   
![](images/a941e19963cb23fb54280dc1195cad2e863a35d8f03f8c2f171f5fb5099ce113.jpg)

<details>
<summary>bar_stacked</summary>

| Quarter | EV | ICE |
| :--- | :--- | :--- |
| 1Q26 | 19 | 3 |
| 2Q26 | 80 | 7 |
| 3Q26 | 41 | 5 |
| 4Q26 | 98 | 11 |
</details>

Source: China Associate of Automobile Manufacturers (CAAM; including estimates), HSBC

Exhibit 16. EVs account for c90% of new models in 2026e   
![](images/1b71011280c4e805cbdee9f3e4be005ff34d5548ca8be204d3a5495afdfe5244.jpg)

<details>
<summary>pie</summary>

| Category | Percentage (%) |
| :--- | :--- |
| EV | 90 |
| ICE | 10 |
</details>

Source: CAAM (including estimates), HSBC

Exhibit 17. Inventory indicator decreased to 1.89 in Ap

[中间内容因长度限制已省略]

n and the Financial Supervisory Service of Korea. In Singapore, this publication is distributed by The Hongkong and Shanghai Banking Corporation Limited, Singapore Branch for the general information of institutional investors or other persons specified in Sections 274 and 304 of the Securities and Futures Act 2001 of Singapore ("SFA") and accredited investors and other persons in accordance with the conditions specified in Sections 275 and 305 of the SFA. Only Economics or Currencies reports are intended for distribution to a person who is not an Accredited Investor, Expert Investor or Institutional Investor as defined in SFA. The Hongkong and Shanghai Banking Corporation Limited, Singapore Branch accepts legal responsibility for the contents of reports. This publication is not a prospectus as defined in the SFA. It may not be further distributed in whole or in part for any purpose. The Hongkong and Shanghai Banking Corporation Limited Singapore Branch is regulated by the Monetary Authority of Singapore. Recipients in Singapore should contact a "Hongkong and Shanghai Banking Corporation Limited, Singapore Branch" representative in respect of any matters arising from, or in connection with this report. Please refer to The Hongkong and Shanghai Banking Corporation Limited Singapore Branch's website at www.business.hsbc.com.sg for contact details. In Australia, this publication has been distributed by The Hongkong and Shanghai Banking Corporation Limited (ABN 65 117 925 970, AFSL 301737) for the general information of its "wholesale" customers (as defined in the Corporations Act 2001). Where distributed to retail customers, this research is distributed by HSBC Bank Australia Limited (ABN 48 006 434 162, AFSL No. 232595). These respective entities make no representations that the products or services mentioned in this document are available to persons in Australia or are necessarily suitable for any particular person or appropriate in accordance with local law. No consideration has been given to the particular investment objectives, financial situation or particular needs of any recipient.

HSBC Securities (USA) Inc. accepts responsibility for the content of this research report prepared by its non-US foreign affiliate. The information contained herein is under no circumstances to be construed as investment advice and is not tailored to the needs of the recipient. All US persons receiving and/or accessing this report and wishing to effect transactions in any security discussed herein should do so with HSBC Securities (USA) Inc. in the United States and not with its non-US foreign affiliate, the issuer of this report. HSBC México, S.A., Institución de Banca Múltiple, Grupo Financiero HSBC is authorized and regulated by Secretaría de Hacienda y Crédito Público and Comisión Nacional Bancaria y de Valores (CNBV). In Brazil, this document has been distributed by Banco HSBC SA ("HSBC Brazil"), and/or its affiliates. As required by Resolution No. 20/2021 of the Securities and Exchange Commission of Brazil (Comissão de Valores Mobiliários), potential conflicts of interest concerning (i) HSBC Brazil and/or its affiliates; and (ii) the analyst(s) responsible for authoring this report are stated on the chart above labelled "HSBC & Analyst Disclosures".

If you are a customer of HSBC International Wealth & Premier Banking ("IWPB"), including HSBC Private Bank, you are eligible to receive this publication only if: (i) you have been approved to receive relevant research publications by an applicable HSBC legal entity; (ii) you have agreed to the applicable HSBC entity's terms and conditions and/or customer declaration for accessing research; and (iii) you have agreed to the terms and conditions of any other internet banking, online banking, mobile banking and/or investment services offered by that HSBC entity, through which you will access research publications (collectively with (ii), the "Terms"). If you do not meet the above eligibility requirements, please disregard this publication and, if you are a IWPB customer, please notify your Relationship Manager or call the relevant customer hotline. Distribution of this publication is the sole responsibility of the HSBC entity with whom you have agreed the Terms. Receipt of research publications is strictly subject to the Terms and any other conditions or disclaimers applicable to the provision of the publications that may be advised by IWPB.

© Copyright 2026, The Hongkong and Shanghai Banking Corporation Limited, ALL RIGHTS RESERVED. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, on any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of The Hongkong and Shanghai Banking Corporation Limited.

[1279533]
"""
