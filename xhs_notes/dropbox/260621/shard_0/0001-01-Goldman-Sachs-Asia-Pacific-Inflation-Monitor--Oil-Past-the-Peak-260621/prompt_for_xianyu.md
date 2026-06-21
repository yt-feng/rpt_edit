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
# Asia-Pacific Inflation Monitor: Oil Past the Peak

This publication summarizes regional and economy-specific inflation data across the Asia-Pacific economies we cover. The latest CPI/PPI data points are generally for May 2026, with some energy price data through mid-June.  
- Our commodity strategists have lowered their energy price forecasts somewhat (to \$80/bbl for Brent in Q4, from \$90/bbl previously) reflecting increased prospects for a re-opening of the Strait of Hormuz and much lower global oil prices in recent weeks. Import prices and producer prices rose sharply across Asia since early 2026 (though implicit or explicit subsidies have moderated or capped retail fuel prices in some countries), but are set to ease materially in the next monthly update.  
■ Pre-war, CPI inflation was broadly in line with or below central bank targets in most countries. Now, headline and core CPI inflation are generally in line with targets or above.  
Inflation pressures have been particularly acute in lower-income economies with more limited subsidies—the pace of seasonally-adjusted CPI inflation over the past three months in Philippines and Thailand remains over 10% annualized. But these economies have also seen much lower month-on-month headline CPI inflation in May.  
CPI inflation forecasts (both ours and the consensus) moved higher across the region since the onset of the Iran war, closure of the Strait of Hormuz, and consequent reduction in energy supply to Asia. But with energy prices well off the peak for some time, forecasts have converged somewhat, and we now see risks skewed to the downside.  
Wage inflation has been mixed across Asia-Pacific, but stable or lower in most of the region. One theme is notable softness in higher-income economies (Japan is one exception).

## Andrew Tilton

+852-2978-1802

andrew.tilton@gs.com

GS (Asia) L.L.C.

## Andrew Boak, CFA

+61(2)9321-8576

andrew.boak@gs.com

GS Australia Pty Ltd

## Akira Otani

+81(3)4587-9960 | akira.otani@gs.com

GS Japan Co., Ltd.

## Goohoon Kwon, CFA

+852-2978-0048

goohoon.kwon@gs.com

GS (Asia) L.L.C.

## Hui Shan

+852-2978-6634 | hui.shan@gs.com

GS (Asia) L.L.C.

## Santanu Sengupta

+91(22)6616-9042

santanu.sengupta@gs.com

GS India SPL

## Xinquan Chen

+852-2978-2418

xinquan.chen@gs.com

GS (Asia) L.L.C.

## Irene Choi

+82(2)3788-1722 | irene.choi@gs.com

GS (Asia) L.L.C., Seoul

Branch

## Will Maher

+61(2)9320-1013 | will.maher@gs.com

GS Australia Pty Ltd

## Tomohiro Ota

+81(3)4587-9984

tomohiro.ota@gs.com

GS Japan Co., Ltd.

## Yuriko Tanaka

+81(3)4587-9964

yuriko.tanaka@gs.com

GS Japan Co., Ltd.

## Lisheng Wang

+852-3966-4004

lisheng.wang@gs.com

GS (Asia) L.L.C.

## Chris Poh

+65-6889-3454 | chris.poh@gs.com

GS (Singapore) Pte

## Oscar To

+61(2)9320-1367 | oscar.to@gs.com

GS Australia Pty Ltd

## Yuting Yang

+852-2978-7283

yuting.y.yang@gs.com

GS (Asia) L.L.C.

## The Energy Price Shock

Exhibit 1: Energy flows through the Strait of Hormuz have yet to revive...  
![](images/6c46350f62c312421b7bf760ba053da81f19778f284bec3512e36fb889240d30.jpg)

<details>
<summary>bar-line hybrid</summary>

Estimated oil exports through Strait of Hormuz, based on reported vessel count
| Date | Flows (Daily) (mb/d) | 4-Day moving average (RHS) |
|---|---|---|
| Normal | 3.0 | 10 |
| Apr-01 | 3.5 | 12 |
| Apr-04 | 5.0 | 18 |
| Apr-07 | 3.0 | 15 |
| Apr-10 | 4.0 | 20 |
| Apr-13 | 3.5 | 22 |
| Apr-16 | 5.5 | 25 |
| Apr-19 | 3.0 | 20 |
| Apr-22 | 3.5 | 18 |
| Apr-25 | 2.0 | 12 |
| Apr-28 | 2.5 | 10 |
| May-01 | 3.0 | 8 |
| May-04 | 1.0 | 5 |
| May-07 | 0.5 | 3 |
| May-10 | 3.0 | 10 |
| May-13 | 3.5 | 15 |
| May-16 | 3.0 | 18 |
| May-19 | 3.5 | 20 |
| May-22 | 3.0 | 18 |
| May-25 | 3.5 | 20 |
| May-28 | 3.0 | 18 |
| May-31 | 4.0 | 22 |
| Jun-03 | 3.5 | 20 |
| Jun-06 | 3.0 | 18 |
| Jun-09 | 2.5 | 15 |
| Jun-12 | 2.0 | 12 |
| Jun-15 | 1.5 | 10 |
</details>

Source: S&P Global Commodities at Sea, Kpler, GS Global Investment Research

Exhibit 2: ...though some Asian economies have secured imports from other sources  
![](images/3d1c79ba12f952919f2333b0822d8eab594d76e662a253a59e88b18ab064a16f.jpg)

<details>
<summary>line chart</summary>

| Date | South Korea (Percent change, yoy) | China (Percent change, yoy) | Japan (Percent change, yoy) | Other Asia* (Percent change, yoy) |
|---|---|---|---|---|
| Jan-26 | ~1 | ~-5 | ~-3 | ~8 |
| Feb-26 | ~8 | ~12 | ~-5 | ~13 |
| Mar-26 | ~15 | ~-20 | ~-5 | ~5 |
| Apr-26 | ~-5 | ~-15 | ~-10 | ~-5 |
| May-26 | ~-10 | ~-15 | ~-10 | ~0 |
| Jun-26 | ~-15 | ~5 | ~5 | ~-5 |
</details>

Source: GS Global Investment Research

Exhibit 3: Oil prices are down sharply over the past month  
![](images/f2d309702152855895aa2a131d1fc8d2b07de1d5d172767d1e87acf66dc2417f.jpg)

<details>
<summary>line chart</summary>

| Date   | Brent dated (USD/bbl) | Brent nearby futures (USD/bbl) |
|--------|------------------------|---------------------------------|
| Jan-26 | ~60                    | ~60                             |
| Feb-26 | ~70                    | ~65                             |
| Mar-26 | ~100                   | ~90                             |
| Apr-26 | ~140                   | ~110                            |
| May-26 | ~120                   | ~100                            |
| Jun-26 | ~80                    | ~70                             |
</details>

Source: Bloomberg, GS Global Investment Research

Exhibit 4: Refined product prices are also down, though they remain notably above pre-war levels  
![](images/848d2c57646071d0d632a5581283179e6e46c0e922215e56d63e576196fc1bce.jpg)

<details>
<summary>line chart</summary>

| Date | USD/bbl |
|---|---|
| Jan-26 | 70 |
| Feb-26 | 75 |
| Mar-26 | 80 |
| Apr-26 | 190 |
| May-26 | 130 |
| Jun-26 | 100 |
</details>

Source: GS Global Investment Research

Exhibit 5: Our base case oil forecast now has Brent at \$80/bbl in Q4  
![](images/78c5178e7db654e1df04af262fe163346ff7fb69e97d30fad04266df1fef28dc.jpg)

<details>
<summary>line chart</summary>

Monthly Brent oil price
| Date | Price Upside (Hormuz Remains Disrupted, Gulf Exports Trend Up 10mb/d by Dec27) (USD/bbl) | Forwards (Nearby Contract Traded That Month) (USD/bbl) | Base Case (Gulf Fully Recover by End-July) (USD/bbl) | Price Downside (Gulf Normalize by Early-July, Higher Production, Lower Demand) (USD/bbl) |
|---|---|---|---|---|
| Jan-26 | 65 | 75 | 65 | 60 |
| Apr-26 | 100 | 80 | 100 | 70 |
| Jul-26 | 105 | 78 | 85 | 65 |
| Oct-26 | 130 | 77 | 82 | 60 |
| Jan-27 | 135 | 76 | 80 | 58 |
| Apr-27 | 125 | 75 | 78 | 55 |
| Jul-27 | 115 | 74 | 76 | 53 |
| Oct-27 | 95 | 73 | 74 | 52 |
| Jan-28 | 80 | 72 | 72 | 50 |
</details>

Prices correspond to nearby futures contract traded that month.  
Source: ICE, GS Global Investment Research

## Regional inflation summary

This section provides an overview of regional trends; core inflation measures are economy-specific definitions. $^{1}$

Exhibit 6: Median headline CPI inflation up to 3% regionally  
![](images/2fdca6d1d82a710a6da74149dde54d67d52485f0b5cb09684c3ec109843dc189.jpg)

<details>
<summary>line chart</summary>

| Year | Median | Interquartile Range (Lower) | Interquartile Range (Upper) |
|------|--------|-----------------------------|-----------------------------|
| 2016 | 1.0    | 0.5                         | 2.5                         |
| 2017 | 1.5    | 0.8                         | 3.0                         |
| 2018 | 1.8    | 1.0                         | 3.5                         |
| 2019 | 1.6    | 0.7                         | 3.2                         |
| 2020 | 2.0    | 1.0                         | 3.8                         |
| 2021 | 0.5    | -0.5                        | 1.5                         |
| 2022 | 3.0    | 2.0                         | 4.5                         |
| 2023 | 5.5    | 4.0                         | 7.0                         |
| 2024 | 3.5    | 2.5                         | 4.5                         |
| 2025 | 2.5    | 1.5                         | 3.5                         |
| 2026 | 3.0    | 2.0                         | 4.0                         |
| 2027 | 3.5    | 2.5                         | 4.5                         |
</details>

Source: Haver Analytics, GS Global Investment Research

Exhibit 7: Core inflation generally has been well-behaved so far  
![](images/9e37a0c77c36508648e672948e8463c4887816d0f9e7bc7eafe33b039fdb6795.jpg)

<details>
<summary>line chart</summary>

| Year | Median | Interquartile range (Lower) | Interquartile range (Upper) |
|------|--------|-----------------------------|-----------------------------|
| 2016 | 1.5    | 0.8                         | 3.0                         |
| 2017 | 1.6    | 0.9                         | 3.1                         |
| 2018 | 1.7    | 1.0                         | 3.2                         |
| 2019 | 1.8    | 1.1                         | 3.3                         |
| 2020 | 1.9    | 1.2                         | 3.4                         |
| 2021 | 0.8    | 0.5                         | 2.5                         |
| 2022 | 2.0    | 1.5                         | 4.0                         |
| 2023 | 4.5    | 3.0                         | 6.0                         |
| 2024 | 3.0    | 2.0                         | 4.5                         |
| 2025 | 2.5    | 1.5                         | 3.5                         |
| 2026 | 2.8    | 1.8                         | 3.8                         |
| 2027 | 3.0    | 2.0                         | 4.0                         |
</details>

Source: Haver Analytics, GS Global Investment Research

Exhibit 8: Inflation has been high since the onset of the war, but eased in May in a few economies

<table><tr><td rowspan="2" colspan="2"></td><td rowspan="2">As of</td><td rowspan="2">year-over-year</td><td rowspan="2">3m annl. Change, sa**</td><td rowspan="2">Monthly annl. Change, sa</td><td rowspan="2" colspan="14">2023</td><td colspan="101">2024</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>J</td><td>J</td><td>A</td><td>S</td><td>O</td><td>N</td><td>D</td><td>J</td><td>F</td><td>M</td><td>A</td><td>M</td><td>J</td><td>J</td><td>A</td><td>S</td><td>O</td><td>N</td><td>D</td><td>J</td><td>F</td><td>M</td><td>A</td><td>M</td><td>J</td><td>J</td><td>A</td><td>S</td><td>O</td><td>N</td><td>D</td><td>J</td><td>F</td><td>M</td><td>A</td><td>M</td><td>J</td><td>J</td><td>A</td><td>S</td><td>O</td><td>N</td><td>D</td><td>J</td><td>F</td><td>M</td><td>A</td><td>M</td><td>J</td><td>J</td><td>A</td><td>S</td><td>O</td><td>N</td><td>D</td><td>J</td><td>F</td><td>M</td><td>A</td><td>M</td><td>J</td><td>A</td><td>S</td><td>O</td><td>N</td><td>D</td><td>J</td><td>F</td><td>M</td><td>A</td><td>M</td><td>J</td><td>J</td><td>A</td><td>S</td><td>O</td><td>N</td><td>D</td><td>J</td><td>F</td><td>M</td><td>A</td><td>M</td><td>J</td><td>J</td><td>A</td><td>S</td><td>O</td><td>N</td><td>D</td><td>J</td><td>F</td><td>M</td><td>A</td><td>M</td><td>J</td><td>J</td><td>A</td><td>S</td><td>O</td><td>N</td><td>D</td><td>J</td><td>F</td><td>M</td><td>A</td><td>M</td><td>J</td><td>J</td><td>B</td><td>C</td><td>D</td><td>J</td><td>F</td><td>M</td><td>A</td><td>M</td><td>J</td><td>J</td><td>A</td><td>S</td><td>O</td><td>N</td><td>D</td><td>J</td><td>F</td><td>M</td><td>A</td><td>M</td><td>J</td><td>J</td><td>A</td><td>S</td><td>O</td><td>N</td><td>D</td><td>J</td><td>F</td><td>M</td><td>A</td><td>M</td><td>J</td><td>J</td><td>A</td><td>S</td><td>O</td><td>N</td><td>D</td><td>J</td><td>F</td><td>M</td><td>A</td><td>M</td><td>J</td><td>J</td><td>A</td><td>S</td><td>O</td><td>N</td><td>D</td><td colspa

[中间内容因长度限制已省略]

ttempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be

supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
