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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`摩根斯坦利`。标题格式建议：`# 摩根斯坦利：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## US Economics Weekly | North America

# Reassessing risks to our Fed call after the latest data

Last week's data suggest that, on net, the balance of risks is shifting toward firmer inflation rather than weaker hiring. The labor market continues to firm, and while the tariff impulse appears to be nearing completion, sustained disinflation ahead depends on a resolution of the conflict.

## Key Takeaways

The labor market has strengthened, reducing downside risks and shifting the Fed's focus back toward inflation.  
CPI came in line with expectations, suggesting the payback in core goods is underway.  
However, a strong core PCE translation following PPI (0.36% m/m in May) indicates that the oil impulse to core persists—primarily through airfares.  
The extent of airfare payback—and broader core disinflation—will depend on how long the Strait of Hormuz remains disrupted.  
Consumption has been running slightly above wealth-implied levels, and we expect limited upside risks to real spending growth.

Exhibit 1: The longer oil prices remain elevated, the greater the risk of second-round effects on core inflation.  
![](images/1335f8536e7b10a7b4f1252fa1647c75787d146e72a599ea042ab6710a7687d5.jpg)

<details>
<summary>line chart</summary>

| Date   | Brent oil prices ($/bbl) |
|--------|--------------------------|
| Jan-26 | 60                       |
| Feb-26 | 70                       |
| Mar-26 | 80                       |
| Apr-26 | 110                      |
| May-26 | 115                      |
| Jun-26 | 90                       |
</details>

Source: Bloomberg, MS

MS & CO. LLC

## Michael T Gapen

Chief US Economist

Michael.Gapen@morganstanley.com +1 212 761-0571

## Sam D Coffin

Economist

Sam.Coffin@morganstanley.com +1 212 761-4630

## Diego Anzoategui

Economist

Diego.Anzoategui@morganstanley.com +1 212 761-8573

## Arunima Sinha

Global Economist

Arunima.Sinha@morganstanley.com +1 212 761-4125

## Heather Berger

Economist

Heather.Berger@morganstanley.com +1 212 761-2296

## Lingdi Xu

Economist

Lingdi.Xu@morganstanley.com +1 212 761-2957

2026 EXTEL

ALL-AMERICA

RESEARCH POLL

May 26 – June 12, 2026

VIEW OUR

ANALYSTS >

# Reassessing risks to our Fed call after the latest data

When we wrote our outlook, we highlighted two scenarios under which inflation would run higher and the Fed would either remain on hold for longer or potentially hike rates: a demand push scenario, and one featuring a persistent oil premium stemming from a prolonged US-Iran conflict.

In the demand push scenario, stronger consumption and business investment—supported by elevated wealth and improving confidence—drive a reacceleration in growth and tighter labor market conditions. As a result, inflation pressures remain firm even as oil dynamics normalize, with tighter labor markets reinforcing persistence in core inflation and ultimately prompting the Fed to begin hiking once it becomes clear that the strength reflects demand rather than productivity. By contrast, in the permanent oil premium scenario, oil prices remain structurally elevated, leading to sustained supply side pressures and gradual pass through into core prices. While growth is somewhat softer, inflation remains persistently above target, keeping the Fed cautious and on hold with a high bar for easing.

The recent developments in the Middle East, together with last week's employment report and this week's inflation data, suggest that both scenarios may be becoming more likely than we initially anticipated.

On net, the data indicate that the balance of risks is shifting in the direction of firmer inflation over weak hiring. This is different from a year ago when the Fed said downside risk to labor markets outweighed inflation concerns and cut its policy rate by 75bp,

The employment report pointed to a labor market that continues to firm. Payroll growth has reaccelerated, with the three month average rising to around 188k, a clear improvement relative to last year and stronger than both our expectations and likely those of the Fed. This strength should alleviate concerns about downside risks to the labor market and reinforce the shift in the balance of risks toward inflation.

At the same time, the unemployment rate remains low and broadly stable at around 4.3%. The key question is whether labor markets will tighten further, as in our demand push scenario. That, in turn, depends on the extent to which higher energy prices weigh on activity. The impact of oil shocks typically happens with a lag, suggesting some risk of a slowdown ahead. However, if that deceleration does not materialize and payroll growth remains around 100k—well above our estimated breakeven pace of roughly 50k—we would expect continued downward pressure on the unemployment rate. If sustained, this dynamic would move the labor market closer to our demand push scenario, raising the likelihood that the Fed shifts from a hold to a hiking stance.

On inflation, the May CPI data broadly aligned with our expectations but PPI data and our translation to PCE inflation surprised us to the upside. Core CPI came in at 0.21% m/m, with signs that the payback from earlier goods inflation has started. Tariff pass through appears to be nearing completion, with core goods prices turning negative on the month, and there were limited signs of broader spillovers from AI or oil into goods categories.

However, the translation into core PCE following the PPI release was stronger than expected. We now estimate core PCE increased $0.36\%$ m/m in May, implying a y/y pace of $3.4\%$ . This upward revision was driven in part by stronger than expected services components, including a notable pickup in airfares—particularly international fares—suggesting that oil related pressures continue.

While the oil impulse to core remains relatively narrow for now, the sharper than expected acceleration in airfares highlights potential upside risks. We continue to expect some of this strength to unwind over time, generating a payback in services inflation. However, in the absence of a near term resolution to the conflict—consistent with our permanent oil premium scenario—it would become increasingly difficult to see core PCE ending the year below 3%y/y, fast disinflation and Fed cuts in 2027.

Exhibit 2: A broad-based acceleration in payrolls so far this year  
![](images/e8d7a9983837f891e5f2b65770997e12c540025b4a75d1b038725e37a58a94bc.jpg)

<details>
<summary>bar chart</summary>

Payrolls change, 000s
| Category | YTD avg (in 000s) | 2025 avg (in 000s) |
|---|---|---|
| Government | 8 | -15 |
| Other services | 1 | 4 |
| Leisure & hospitality | 24 | 8 |
| Health & social services | 55 | 57 |
| Private education | -3 | 0 |
| Professional & bus services | 19 | -13 |
| Financial | -16 | 1 |
| Information | -12 | -4 |
| Utilities | 1 | 1 |
| Transport & warehousing | 8 | -9 |
| Retail | 9 | -4 |
| Wholesale | 1 | -4 |
| Manuf | 5 | -9 |
| Construction | 13 | 0 |
| Mining and logging | 2 | -2 |
</details>

Source: BLS, MS.

Exhibit 3: The tariff pass-through may be near completion, but a prolonged conflict adds upside risks  
![](images/adfe5c2c007bf369152b15deed63c2d4ff322461b4bd12e518bfb47c12fd6181.jpg)

<details>
<summary>line chart</summary>

PCE cumulative tariff pass-through (pp)
| Date | Effect of tariffs on headline PCE (pp) |
|---|---|
| Apr-25 | 0.04 |
| May-25 | 0.12 |
| Jun-25 | 0.22 |
| Jul-25 | 0.25 |
| Aug-25 | 0.29 |
| Sep-25 | 0.36 |
| Oct-25 | 0.36 |
| Nov-25 | 0.35 |
| Dec-25 | 0.39 |
| Jan-26 | 0.47 |
| Feb-26 | 0.60 |
| Mar-26 | 0.61 |
| Apr-26 | 0.63 |
| May-26 | 0.62 |
Estimated total passthrough
</details>

Source: BEA, BLS, MS forecasts.

## Consumption support from a low saving rate has limits

In our 2026 outlook, we expected that real consumer spending growth would take a backseat in driving headline real GDP growth for much of the year. The drag is largely cyclical and front loaded: tariff effects weighed on real purchasing power in 1Q, while the subsequent oil disruption is acting as an effective tax on households through 2Q and 3Q. In that environment, growth has rotated away from consumption toward other components, even as underlying demand has remained broadly intact.

Taking stock of incoming data, the pace of spending is tracking close to expectations. Real consumption growth had slowed to 1.4% q/q saar in 1Q26. Beneath the surface, the drivers of spending have improved modestly. Recent labor market gains imply that the nominal payroll proxy for production and non-supervisory workers is running a solid pace: 5.5% in April and May over the 1Q average (2m/3m % saar), and 4.4% for all employees. However, headline PCE growth in 2Q will continue to pressure real labor market income; a further acceleration in the labor market this summer could lead to real wage growth closer to flat, rather than slightly negative, and could incrementally support near-term consumption momentum.

At the same time, while the overall balance sheet of the consumer continues to be healthy, there could be some headwinds. Nominal household wealth gains slowed in 1Q26 with implications for how much upside risk there could be for consumption going forward. Our wealth model indicates that consumption has been running above levels implied by household wealth for the last year, suggesting some upside risk to the saving rate and, correspondingly, downside risk to spending. So, while income dynamics are likely stabilizing, the upside risk to consumption growth from wealth effects is much less likely.

Our view then is that real consumption growth is so far evolving largely in line with our baseline: a slower pace of growth most of this year, with some acceleration in 4Q26 onwards, but not a primary driver of growth. Risks around this profile remain skewed slightly to the downside if cyclical factors turn less favorable due to an extended oil disruption, particularly from slower income growth or asset market volatility. Absent a more durable acceleration in labor market momentum and “animal spirits,” we see limited scope for a material upside surprise to consumer spending from here.

Exhibit 4: The pace of net wealth gains for households have slowed, and nominal consumption has been overshooting wealth-implied target levels  
![](images/5766330fc433033c590c3cf38328bda1a66388623f7e7dcbe7ac9a2f2fadc015.jpg)

<details>
<summary>bar chart</summary>

Nominal consumption relative to model-implied target level (Bil $)
| Period | Nominal consumption relative to model-implied target level (Bil $) |
|---|---|
| Q1 2024 | -188 |
| Q2 2024 | -191 |
| Q3 2024 | -83 |
| Q4 2024 | -55 |
| Q1 2025 | -96 |
| Q2 2025 | 19 |
| Q3 2025 | 27 |
| Q4 2025 | 61 |
| Q1 2026 | 99 |
</details>

Source: Federal Reserve Board, BEA, Haver Analytics, MS

Exhibit 5: There could be some upside risk to the saving rate, if the cyclical factors in the economy turn less supportive in 2H26  
![](images/eeb9a48ee358943abe5346d75d1b979d9182a3d2144af84c22a2cd20e263acc1.jpg)

<details>
<summary>line chart</summary>

| Year | Personal Saving Rate |
| ---- | --------------------- |
| 00   | 4%                    |
| 01   | 5%                    |
| 02   | 6%                    |
| 03   | 5%                    |
| 04   | 5%                    |
| 05   | 4%                    |
| 06   | 2%                    |
| 07   | 3%                    |
| 08   | 2%                    |
| 09   | 6%                    |
| 10   | 7%                    |
| 11   | 6%                    |
| 12   | 8%                    |
| 13   | 11%                   |
| 14   | 5%                    |
| 15   | 6%                    |
| 16   | 5%                    |
| 17   | 6%                    |
| 18   | 7%                    |
| 19   | 8%                    |
| 20   | 24%                   |
| 21   | 19%                   |
| 22   | 2%                    |
| 23   | 6%                    |
| 24   | 5%                    |
| 25   | 4%                    |
| 26   | 3%                    |
</details>

Source: BEA, Haver Analytics, MS

# Oil Tracker: US ending stocks of crude oil edge lower amid increased exports and unchanged production

We continue to track the evolution of inventory and production amid the ongoing Middle East conflict. US ending inventory stocks of crude oil and petroleum products, which represents the EIA's estimate of how many barrels of oil and petroleum products are physically sitting in US storage at period end, continue to move lower. Inclusive of the SPR, inventory stocks are falling by about 2mn barrels a day. The spot price of oil for immediate purchase and delivery in the physical market remains elevated, despite futures prices moving lower on prospects for a near-term agreement between the US and Iran.

US domestic crude production has edged modestly higher in recent weeks, but it remains about in line with pre-conflict production. Net imports of oil (imports - exports) are declining because of increased oil exports.

Exhibit 6: US ending stocks of crude oil continue to move lower  
![](images/150464a4b6c8d2fcefb96bd36762b7dfd25918deb46683a28e1ca5e99f1ba470.jpg)

<details>
<summary>bar-line hybrid</summary>

US Ending Stocks of Crude Oil and Petroleum Products, Thousands.Barrels
| Date | including SPR (Thousand Barrels) | excluding SPR (Thousand Barrels) |
|---|---|---|
| 1/2 | 1,700,000 | 1,300,000 |
| 2/6 | 1,710,000 | 1,280,000 |
| 3/6 | 1,690,000 | 1,275,000 |
| 4/3 | 1,695,000 | 1,285,000 |
| 5/1 | 1,640,000 | 1,255,000 |
| 6/5 | 1,560,000 | 1,215,000 |
</details>

Source: Energy Information Administration, Haver Analytics, MS

Exhibit 7: Prices of oil in the physical market remain elevated  
![](images/4df996b850cfb5295387e6eceaf38198d5a1008a6cee8e63b35f69bd6c4466d9.jpg)

<details>
<summary>line chart</summary>

Crude Oil Spot Price FOB (US$ per Barrel)
| Date | WTI - Cushing Oklahoma (US$ per Barrel) | Brent - Europe (US$ per Barrel) |
|---|---|---|
| 1/2 | 53.0 | 66.0 |
| 1/3 | 53.5 | 67.0 |
| 1/4 | 54.5 | 68.5 |
| 1/5 | 55.0 | 69.0 |
| 1/6 | 56.0 | 70.0 |
| 1/7 | 56.5 | 70.0 |
| 1/8 | 57.0 | 70.5 |
| 1/9 | 57.5 | 70.5 |
| 1/10 | 58.0 | 71.0 |
| 1/11 | 58.5 | 71.0 |
| 1/12 | 59.0 | 71.5 |
| 1/13 | 60.0 | 72.0 |
| 1/14 | 62.0 | 74.0 |
| 1/15 | 64.0 | 76.0 |
| 1/16 | 66.0 | 78.0 |
| 1/17 | 68.0 | 80.0 |
| 1/18 | 70.0 | 82.0 |
| 1/19 | 72.0 | 84.0 |
| 1/20 | 74.0 | 86.0 |
| 1/21 | 76.0 | 88.0 |
| 1/22 | 78.0 | 90.0 |
| 1/23 | 80.0 | 92.0 |
| 1/24 | 82.0 | 94.0 |
| 1/25 | 84.0 | 96.0 |
| 1/26 | 86.0 | 98.0 |
| 1/27 | 88.0 | 100.0 |
| 1/28 | 90.0 | 102.0 |
| 1/29 | 92.0 | 104.0 |
| 1/30 | 94.0 | 106.0 |
| 2/2 | 96.0 | 108.0 |
| 2/3 | 98.0 | 110.0 |
| 2/4 | 100.0 | 112.0 |
| 2/5 | 102.0 | 114.0 |
| 2/6 | 104.0 | 116.0 |
| 2/7 | 106.0 | 118.0 |
| 2/8 | 108.0 | 120.0 |
| 2/9 | 110.0 | 122.0 |
| 2/10 | 112.0 | 124.0 |
| 2/11 | 114.0 | 126.0 |
| 2/12 | 116.0 | 128.0 |
| 3/4 | 118.0 | 130.0 |
| 3/5 | 120.0 | 132.0 |
| 3/6 | 122.0 | 134.0 |
| 3/7 | 124.0 | 136.0 |
| 3/8 | 126.0 | 138.0 |
| 3/9 | 128.0 | 140.0 |
| 3/10 | 130.0 | 142.0 |
| 3/11 | 132.0 | 144.0 |
| 3/12 | 134.0 | 146.0 |
| 3/13 | 136.0 | 148.0 |
| 3/14 | 138.0 | 150.0 |
| 3/15 | 140.0 | 152.0 |
| 3/16 | 142.0 | 154.0 |
| 3/17 | 144.0 | 156.0 |
| 3/18 | 146.0 | 158.0 |
| 3/19 | 148.0 | 160.0 |
| 3/20 | 150.0 | 162.0 |
| 3/21 | 152.0 | 164.0 |
| 3/22 | 154.0 | 166.0 |
| 3/23 | 156.0 | 168.0 |
| 3/24 | 158.0 | 170.0 |
| 3/25 | 160.0 | 172.0 |
| 3/26 | 162.0 | 174.0 |
| 3/27 | 164.0 | 176.0 |
| 3/28 | 166.0 | 178.0 |
| 3/29 | 168.0 | 180.0 |
| 3/30 | 170.0 | 182.0 |
| April-End: Cushing Oklahoma (US$ per Barrel) vs Brent-Europe (US$ per Barrel) (US$ per Barrel) (Note: The values in the image are estimated based on the formula, so they do not correspond to the actual values).) (Figure: Figure I).)
</details>

Source: Energy Information Administration, Haver Analytics, MS

Exhibit 8: Including the SPR, US oil stocks are falling about 2mn barrels per day  
![](images/37732b64e728ed1dac9361d0b1df0cd163bb785efd730daca645e5fbf61227ea.jpg)

<details>
<summary>bar chart</summary>

| Date   | Excluding SPR | SPR    |
|--------|---------------|--------|
| 1/2    | -500          | 0      |
| 2/6    | 1200          | 0      |
| 3/6    | 500           | 0      |
| 4/3    | 400           | -500   |
| 5/1    | -800          | -1000  |
| 6/5    | -1000         | -1500  |
</details>

Source: Energy Information Administration, Haver Analytics, MS

Exhibit 10: US exports of oil and petroleum products have risen, pushing down net imports of these energy goods  
![](images/c8a3f4520af5021b7d0e2f69ee33a50e2dfb274278c813c1450bc75fcbae2f37.jpg)

<details>
<summary>line chart</summary>

| Date | Net Imports (thousands of barrels per day) |
| --- | --- |
| 1/2 | -3200 |
| 1/3 | -2600 |
| 1/4 | -2800 |
| 1/5 | -4400 |
| 1/6 | -2400 |
| 1/7 | -3600 |
| 1/8 | -2200 |
| 1/9 | -2600 |
| 1/10 | -3200 |
| 1/11 | -3600 |
| 1/12 | -3800 |
| 1/13 | -4000 |
| 1/14 | -4200 |
| 1/15 | -4400 |
| 1/16 | -4600 |
| 1/17 | -4800 |
| 1/18 | -5000 |
| 1/19 | -5200 |
| 1/20 | -5400 |
| 1/21 | -5600 |
| 1/22 | -5800 |
| 1/23 | -6000 |
| 1/24 | -6200 |
| 1/25 | -6400 |
| 1/26 | -6600 |
| 1/27 | -6800 |
| 1/28 | -7000 |
| 1/29 | -7200 |
| 1/30 | -7400 |
| 1/31 | -7600 |
| 2/1 | -7800 |
| 2/2 | -8000 |
| 2/3 | -8200 |
| 2/4 | -8400 |
| 2/5 | -8600 |
| 2/6 | -8800 |
| 2/7 | -9000 |
| 2/8 | -9200 |
| 2/9 | -9400 |
| 2/10 | -9600 |
| 2/11 | -9800 |
| 2/12 | -10000 |
| 2/13 | -10200 |
| 2/14 | -10400 |
| 2/15 | -10600 |
| 2/16 | -10800 |
| 2/17 | -11000 |
| 2/18 | -11200 |
| 2/19 | -11400 |
| 2/20 | -11600 |
| 2/21 | -11800 |
| 2/22 | -12000 |
| 2/23 | -12200 |
| 2/24 | -12400 |
| 2/25 | -12600 |
| 2/26 | -12800 |
| 2/27 | -13000 |
| 2/28 | -13200 |
| 3/4 | -13400 |
| 3/5 | -13600 |
| 3/6 | -13800 |
| 3/7 | -14000 |
| 3/8 | -14200 |
| 3/9 | -14400 |
| 3/10 | -14600 |
| 3/11 | -14800 |
| 3/12 | -15000 |
| 3/13 | -15200 |
| 3/14 | -15400 |
| 3/15 | -15600 |
| 3/16 | -15800 |
| 3/17 | -16000 |
| 3/18 | -16200 |
| 3/19 | -16400 |
| 3/20 | -16600 |
| 3/21 | -16800 |
| 3/22 | -17000 |
| 3/23 | -17200 |
| 3/24 | -17400 |
| 3/25 | -17600 |
| 3/26 | -17800 |
| 3/27 | -18000 |
| 3/28 | -18200 |
| 3/29 | -18400 |
| 4/4 | -6888 |
| 4/5 | -5488 |
| 4/6 | -5888 |
| 4/7 | -6288 |
| 4/8 | -6688 |
| 4/9 | -7188 |
| 4/10 | -7688 |
| 4/11 | -7988 |
| 4/12 | -7888 |
| 4/13 | -7788 |
| 4/14 | -7688 |
| 4/15 | -7588 |
| 4/16 | -7488 |
| 4/17 | -7388 |
| 4/18 | -7288 |
| 4/19 | -7188 |
| 4/20 | -7588 |
| 4/21 | -7988 |
| 4/22 | -7988 |
| 4/23 | -7988 |
| 4/24 | -7988 |
| 4/25 | -7988 

[中间内容因长度限制已省略]

cepts responsibility for its contents; in Korea by MS & Co International plc, Seoul Branch; in India by MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi

Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the United States by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

© 2026 MS
"""
