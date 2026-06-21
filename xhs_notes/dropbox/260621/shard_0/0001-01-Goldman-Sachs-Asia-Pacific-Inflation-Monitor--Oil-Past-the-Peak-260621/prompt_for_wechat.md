你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`GS`。标题格式建议：`# GS：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

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

<table><tr><td rowspan="2" colspan="2"></td><td rowspan="2">As of</td><td rowspan="2">year-over-year</td><td rowspan="2">3m annl. Change, sa**</td><td rowspan="2">Monthly annl. Change, sa</td><td rowspan="2" colspan="14">2023</td><td colspan="101">2024</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>J</td><td>J</td><td>A</td><td>S</td><td>O</td><td>N</td><td>D</td><td>J</td><td>F</td><td>M</td><td>A</td><td>M</td><td>J</td><td>J</td><td>A</td><td>S</td><td>O</td><td>N</td><td>D</td><td>J</td><td>F</td><td>M</td><td>A</td><td>M</td><td>J</td><td>J</td><td>A</td><td>S</td><td>O</td><td>N</td><td>D</td><td>J</td><td>F</td><td>M</td><td>A</td><td>M</td><td>J</td><td>J</td><td>A</td><td>S</td><td>O</td><td>N</td><td>D</td><td>J</td><td>F</td><td>M</td><td>A</td><td>M</td><td>J</td><td>J</td><td>A</td><td>S</td><td>O</td><td>N</td><td>D</td><td>J</td><td>F</td><td>M</td><td>A</td><td>M</td><td>J</td><td>A</td><td>S</td><td>O</td><td>N</td><td>D</td><td>J</td><td>F</td><td>M</td><td>A</td><td>M</td><td>J</td><td>J</td><td>A</td><td>S</td><td>O</td><td>N</td><td>D</td><td>J</td><td>F</td><td>M</td><td>A</td><td>M</td><td>J</td><td>J</td><td>A</td><td>S</td><td>O</td><td>N</td><td>D</td><td>J</td><td>F</td><td>M</td><td>A</td><td>M</td><td>J</td><td>J</td><td>A</td><td>S</td><td>O</td><td>N</td><td>D</td><td>J</td><td>F</td><td>M</td><td>A</td><td>M</td><td>J</td><td>J</td><td>B</td><td>C</td><td>D</td><td>J</td><td>F</td><td>M</td><td>A</td><td>M</td><td>J</td><td>J</td><td>A</td><td>S</td><td>O</td><td>N</td><td>D</td><td>J</td><td>F</td><td>M</td><td>A</td><td>M</td><td>J</td><td>J</td><td>A</td><td>S</td><td>O</td><td>N</td><td>D</td><td>J</td><td>F</td><td>M</td><td>A</td><td>M</td><td>J</td><td>J</td><td>A</td><td>S</td><td>O</td><td>N</td><td>D</td><td>J</td><td>F</td><td>M</td><td>A</td><td>M</td><td>J</td><td>J</td><td>A</td><td>S</td><td>O</td><td>N</td><td>D</td><td colspan="100">2026</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><t

[中间内容因长度限制已省略]

 have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

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
