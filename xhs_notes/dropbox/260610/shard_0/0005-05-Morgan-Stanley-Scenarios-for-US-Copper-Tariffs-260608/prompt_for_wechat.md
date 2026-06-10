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
## metal&ROCK | Europe

# Scenarios for US Copper Tariffs

A decision on US refined copper import tariffs is due sometime in 2H26. Advanced notice of tariff implementation would be the most bullish scenario for 2H26, while ruling out tariffs would be the most bearish, removing the \~2.5% of global copper going to the US for stockpiling.

## Key Takeaways

We expect a decision sometime after 30th June, once President Trump has received an update on domestic markets from the Secretary of Commerce.  
Most bullish = Advanced notice of a 15% tariff from Jan 2027, driving COMEX and LME copper higher and tightening LME spreads. Less notice would be less bullish.  
Most bearish = Refined copper tariffs are ruled out completely, putting the 2.5% of copper supply currently going to the US for stockpiling at risk.  
Status quo = Decision is delayed, with not enough evidence to make a decision for now.

What is the upcoming decision? The US is due to decide whether to put in place a 15% refined copper import tariff from 1 Jan 2027, potentially escalating to 30% in 2028. A 50% import tariff is already in place for aluminium, steel and most imports of semi-finished copper products and copper derivative products. The 1 June White House fact sheet highlighted recent developments in steel, aluminium and copper output in the US, noting "this buildout [...] is only possible through the continued implementation and strengthening of the President's Section 232 tariff programs."

Why does it matter? The COMEX copper price is a US-delivered benchmark and therefore should reflect any customs duties, meaning it could trade \~15% higher than the LME benchmark if tariffs are announced. It is already trading \~6% higher than the LME benchmark, incentivising market participants to ship copper to the US ahead of potential implementation. We estimate YTD over-importing at 260 kt, or 2.6% of global demand when annualised. The US now holds over a year of "normal" refined copper imports in inventory, we estimate. Whether or not this overimporting continues will be meaningful for copper prices and the supply demand balance.

When will the tariff decision be announced? A report is due to President Trump from the Secretary of Commerce by 30th June (based on this proclamation) or 1st July (90 days from this proclamation), providing "an update on domestic copper markets [...] so that the President may determine whether imposing a phased universal import duty on refined copper [...] is warranted to ensure that copper imports do not continue to threaten to impair the national security." In our view, this means an update from the Trump administration should come sometime in 2H26, but is unlikely to come on 30th June/1st July directly.

For discussion of outcomes, see inside...

MS & CO. INTERNATIONAL PLC+

## Amy Gower (Amy Sergeant), CFA

Commodities Strategist

Amy.Gower1@morganstanley.com +44 20 7677-6937

MS & CO. LLC

## Carlos De Alba

Equity Analyst

Carlos.De.Alba@morganstanley.com +1 212 761-4927

MS & CO. INTERNATIONAL PLC+

## Ben Kelson

Research Associate

Ben.Kelson@morganstanley.com +44 20 7677-1392

## Martijn Rats, CFA

Equity Analyst and Commodities Strategist

Martijn.Rats@morganstanley.com +44 20 7425-6618

Exhibit 1: Using forward curve differentials, the copper market is pricing 43% chance of a 15% tariff in place by Jan 2027 and 73% by Dec 2027  
![](images/ce6bdd88d23fe38f33e9f5a71a060c283217ccbc0548867896b89105fc680fac.jpg)

<details>
<summary>line chart</summary>

| Date   | Spot arb | 3m Arb | Jan-27 | Dec-27 |
|--------|----------|--------|--------|--------|
| Jan-25 | ~0%      | ~0%    | ~0%    | ~0%    |
| Apr-25 | ~10%     | ~8%    | ~10%   | ~15%   |
| Jul-25 | ~35%     | ~20%   | ~25%   | ~30%   |
| Oct-25 | ~5%      | ~3%    | ~5%    | ~10%   |
| Jan-26 | ~0%      | ~0%    | ~0%    | ~0%    |
| Apr-26 | ~5%      | ~3%    | ~5%    | ~10%   |
</details>

Source: Bloomberg

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Continued.

## What could the outcomes be and what do they mean for copper prices?

1) Tariffs are announced: Bullish: We assume the decision is purely on whether or not to implement a 15% tariff from 1 Jan 2027, and will not consider another tariff level or a different implementation date. If advanced notice is given, e.g. a July announcement for January implementation, this would accelerate copper flows into the US, tightening ex-US markets and driving both COMEX and LME copper prices higher (all else equal). We would expect LME time spreads to tighten and the forward curve to move into backwardation at the front of the market, and COMEX to move towards a 15% premium to LME. If the tariff is only announced closer to the implementation date, or the implementation date is brought forward, there would be less time to front-load shipments which would be a less bullish outcome.

2) Tariffs are ruled out: Bearish: If the US rules out introducing refined copper tariffs, this extra US importing ( $\sim$ 2.6% of demand) would likely cease, weighing on both benchmarks. COMEX copper would fall to parity with, or even slightly below, LME copper and the LME forward curve would loosen as more metal is available. Both benchmarks would likely fall in absolute terms as this US stockpiling demand ceases. However, we view US copper exports as unlikely given metal could just be moved from COMEX to LME warehouses within the US if COMEX traded below LME. Further, we see support around the 12,000 level given the sector ongoing structural supply issues and expected deficits.

3) Decision is rolled forward: Neutral? The decision could also be rolled over to a future date, keeping the option of tariffs on the table but not necessarily for 1 Jan 2027. This would be more of a continuation of the status quo but could be modestly negative for copper prices if market participants see it as a signal that tariffs are less likely.

What happens in 2027 if a tariff is in place? If a 15% tariff is implemented, we would expect the COMEX-LME copper spread to reflect that tariff level, implying room for some COMEX outperformance versus LME. However, we would expect a drop in the over-importing from the US given the financial incentive to ship excess metal will be removed once tariffs need to be paid. If the tariff is expected to escalate to 30% in 2028, import volumes could stay slightly higher than normal but the US already has >1 year of import cover on our estimates. We would also then expect the COMEX-LME spread to rise to somewhere between 15% and 30%.

MS outlook: We noted in Copper: Fundamentals Improving? that the outlook for copper is supported by tightening supply, strong demand from China and US import demand for stockpiling. The upcoming US tariff decision is therefore key risk event, with the potential to accelerate, or halt, the excess US copper imports. At the moment, the market is pricing around a 43% chance of a 15% tariff being in place by Jan 2027. It is difficult to take a strong call on the decision timing and outcome but it remains a key risk to be aware of. Macro factors matter too, as shown by the negative reaction in copper prices to increased expectations for a Fed rate hike in 2026, with COMEX copper tending to outperform on risk-on days, but underperform on risk-off days. COMEX net long positioning is already at an all-time high.

Exhibit 2: The COMEX-LME spread has been rising  
![](images/88cbea9a6fad031e48a3f2229df1b6f50ba35cbde5278811ba7e80a999382cbc.jpg)

<details>
<summary>line chart</summary>

| Date   | Spot arb | 3m Arb | Jan-27 | Dec-27 |
|--------|----------|--------|--------|--------|
| Jan-25 | ~0%      | ~0%    | ~0%    | ~0%    |
| Apr-25 | ~15%     | ~18%   | ~20%   | ~22%   |
| Jul-25 | ~10%     | ~15%   | ~25%   | ~35%   |
| Oct-25 | ~5%      | ~8%    | ~10%   | ~12%   |
| Jan-26 | ~0%      | ~2%    | ~5%    | ~15%   |
| Apr-26 | ~5%      | ~8%    | ~10%   | ~12%   |
</details>

Source: Bloomberg

Exhibit 3: Seaborne copper imports remain above the estimate 15-20kt/week that the US needs  
![](images/6142b1c45816d5b204eba79cb9b6bb269ebe1f711f85fae75004884ddb9b5053.jpg)

<details>
<summary>line chart</summary>

| Date   | US Seaborne Copper Imports (t/week) | COMEX-LME Spread (3m, $/t, RH Axis) |
|--------|-------------------------------------|--------------------------------------|
| Jan-25 | ~30,000                             | ~500                                 |
| Apr-25 | ~55,000                             | ~1,500                               |
| Jul-25 | ~60,000                             | ~3,000                               |
| Oct-25 | ~35,000                             | ~1,000                               |
| Jan-26 | ~70,000                             | ~500                                 |
| Apr-26 | ~45,000                             | ~1,000                               |
</details>

Source: Bloomberg

Exhibit 4: US inventories are now covering >1 year of refined imports  
![](images/1b639bef2ab9e51f6b5955dd1934656c6fdf24260fd364d3451f722c5391bbfc.jpg)

<details>
<summary>stacked bar chart</summary>

US Implied Copper Stockpiling (kt)
| Date | COMEX Inventory (kt) | LME Inventory (kt) | Non Exchange Stockpiling (kt) |
|---|---|---|---|
| Mar-25 | 80 | 0 | 100 |
| May-25 | 120 | 0 | 150 |
| Jul-25 | 180 | 0 | 250 |
| Sep-25 | 240 | 0 | 350 |
| Nov-25 | 300 | 0 | 300 |
| Jan-26 | 400 | 0 | 250 |
| Mar-26 | 550 | 100 | 200 |
| May-26 | 580 | 150 | 180 |
</details>

Source: Bloomberg, MS

Exhibit 5: Ex-US LME inventories have been tightening in China and on the LME  
![](images/770fca9feb1e3cac7d2959be37a672c44353388eaae9c251acb7d4146d9e6bce.jpg)

<details>
<summary>line chart</summary>

| Month | 2022 | 2023 | 2024 | 2025 | 2026 |
|-------|------|------|------|------|------|
| Jan   | ~300 | ~200 | ~150 | ~350 | ~350 |
| Feb   | ~350 | ~250 | ~200 | ~400 | ~400 |
| Mar   | ~500 | ~300 | ~350 | ~500 | ~700 |
| Apr   | ~450 | ~350 | ~400 | ~450 | ~500 |
| May   | ~400 | ~300 | ~450 | ~400 | ~450 |
| Jun   | ~350 | ~250 | ~500 | ~350 | ~400 |
| Jul   | ~300 | ~200 | ~550 | ~300 | ~350 |
| Aug   | ~250 | ~150 | ~650 | ~250 | ~300 |
| Sep   | ~200 | ~150 | ~600 | ~250 | ~250 |
| Oct   | ~150 | ~150 | ~550 | ~250 | ~250 |
| Nov   | ~100 | ~150 | ~500 | ~250 | ~250 |
| Dec   | ~150 | ~150 | ~450 | ~350 | ~350 |
</details>

Source: Bloomberg

## Week in Review

Base Metals: Base metals are on track to end the week lower with the exception of zinc. Macro factors weighed on the complex with the DXY up 0.9% and the market now pricing in 1 US rate hike by year end after stronger non-farm payrolls data. The biggest drop comes in nickel with Platts reporting that HPAL producers are sourcing sulphur elsewhere. Copper is down 0.4% but LME and COMEX are down 3.3% and 5.3% from their Tuesday highs on growing demand worries. Aluminium fell 1.8%, likely dragged lower by other metals.

Precious Metals: Precious metals weakened sharply this week, with most of the drop on Friday after US employment data boosted rate hike expectations. Gold was trading below its 200 day moving average at the time of writing. India said reports that the RBI was selling gold was incorrect. Silver saw the largest drop, down 8.3% to below \$70/oz for the first time since March but remains below its 200dma for now.

Bulks: Iron ore dropped 3.6% WoW this week to \$101.5/t as hot weather in Asia weighs on construction activity earlier than normal. Met coal was up 1.7% WoW but with stronger price action in China as mine accidents have prompted mine inspections and closures. Thermal coal rose 7.5%, also supported by mine inspections as well as strong demand for cooling in Asia. Indonesia has also issued regulation that palm oil, coal, and ferroalloys can only be exported by a state-owned enterprise.

Exhibit 6: Base metals price indices (12-month rolling)  
![](images/a3534dd5af342c52e53f52835d7cbf05467b25f7152b7d123ab5e1b1edc31cfe.jpg)

<details>
<summary>line chart</summary>

| Date   | zinc | lead | aluminium | nickel | copper |
|--------|------|------|-----------|--------|--------|
| Jun-25 | 100  | 100  | 100       | 100    | 100    |
| Jul-25 | 105  | 102  | 103       | 98     | 101    |
| Aug-25 | 108  | 104  | 105       | 99     | 103    |
| Sep-25 | 110  | 106  | 107       | 100    | 105    |
| Oct-25 | 115  | 108  | 110       | 102    | 108    |
| Nov-25 | 120  | 110  | 115       | 105    | 112    |
| Dec-25 | 125  | 112  | 120       | 108    | 115    |
| Jan-26 | 130  | 115  | 125       | 110    | 120    |
| Feb-26 | 135  | 118  | 130       | 115    | 125    |
| Mar-26 | 140  | 120  | 135       | 120    | 130    |
| Apr-26 | 145  | 122  | 140       | 125    | 135    |
| May-26 | 150  | 125  | 145       | 130    | 140    |
| Jun-26 | 155  | 128  | 150       | 135    | 145    |
</details>

Source: Bloomberg, MS

Exhibit 7: Precious metals indices (12-month rolling)  
![](images/29239d464d779bd0d25e85ffe839394f2c0b70c18cd81e53d9a2471cdfcacb47.jpg)

<details>
<summary>line chart</summary>

| Date   | gold | silver | platinum | palladium |
|--------|------|--------|----------|-----------|
| Jan-25 | 90   | 90     | 90       | 90        |
| Feb-25 | 90   | 90     | 90       | 90        |
| Mar-25 | 90   | 90     | 90       | 90        |
| Apr-25 | 90   | 90     | 90       | 90        |
| May-25 | 90   | 90     | 90       | 90        |
| Jun-25 | 90   | 90     | 90       | 90        |
| Jul-25 | 90   | 90     | 90       | 90        |
| Aug-25 | 90   | 90     | 90       | 90        |
| Sep-25 | 90   | 90     | 90       | 90        |
| Oct-25 | 90   | 90     | 90       | 90        |
| Nov-25 | 90   | 90     | 90       | 90        |
| Dec-25 | 90   | 90     | 90       | 90        |
| Jan-26 | 180  | 380    | 300      | 180       |
| Feb-26 | 180  | 380    | 300      | 180       |
| Mar-26 | 180  | 380    | 300      | 180       |
| Apr-26 | 180  | 380    | 300      | 180       |
| May-26 | 180  | 380    | 300      | 180       |
</details>

Source: Bloomberg, MS

Exhibit 8: Bulk commodity price indices (12-month rolling)  
![](images/055a181c49dbbe612d843cab747c635077eb09afdd8bc90750a4a4de6bac3b85.jpg)

<details>
<summary>line chart</summary>

| Month   | iron ore | met-coal | thermal coal | all traded coals (wtg avg) |
|---------|----------|----------|--------------|-----------------------------|
| Jun-25  | 100      | 95       | 100          | 100                         |
| Jul-25  | 105      | 98       | 102          | 103                         |
| Aug-25  | 108      | 100      | 105          | 106                         |
| Sep-25  | 110      | 102      | 108          | 109                         |
| Oct-25  | 112      | 104      | 110          | 111                         |
| Nov-25  | 115      | 106      | 115          | 116                         |
| Dec-25  | 118      | 108      | 120          | 122                         |
| Jan-26  | 120      | 110      | 125          | 127                         |
| Feb-26  | 125      | 130      | 135          | 132                         |
| Mar-26  | 130      | 125      | 138          | 136                         |
| Apr-26  | 135      | 128      | 140          | 138                         |
| May-26  | 140      | 130      | 145          | 142                         |
| Jun-26  | 145      | 132      | 155          | 150                         |
</details>

Source: Platts, Bloomberg, MS

## MS Price Forecasts

Exhibit 9: Summary of MS's commodity price forecasts (set on 8 April 2026)

<table><tr><td>commodity group</td><td>unit</td><td>1Q 26a</td><td>2Q 26e</td><td>3Q 26e</td><td>4Q 26e</td><td>1Q 27e</td><td>2Q 27e</td><td>3Q 27e</td><td>4Q 27e</td><td>2025e</td><td>2026e</td><td>2027e</td><td>2028e</td><td>2029e</td><td>2030e</td><td>2031e</td><td>LT real</td><td>LT nom.</td></tr><tr><td colspan="19">Base Metals</td></tr><tr><td rowspan="2">LME Aluminium</td><td>US$/lb</td><td>1.45</td><td>1.54</td><td>1.56</td><td>1.59</td><td>1.54</td><td>1.47</td><td>1.45</td><td>1.45</td><td>1.20</td><td>1.54</td><td>1.48</td><td>1.43</td><td>1.45</td><td>1.45</td><td>1.36</td><td>1.13</td><td>1.30</td></tr><tr><td>US$/t</td><td>3,195</td><td>3,400</td><td>3,450</td><td>3,500</td><td>3,400</td><td>3,250</td><td>3,200</td><td>3,200</td><td>2,638</td><td>3,386</td><td>3,263</td><td>3,150</td><td>3,200</td><td>3,200</td><td>3,000</td><td>2,500</td><td>2,871</td></tr><tr><td rowspan="2">LME Copper</td><td>US$/lb</td><td>5.81</td><td>5.15</td><td>5.44</td><td>5.90</td><td>5.90</td><td>5.90</td><td>5.22</td><td>5.22</td><td>4.56</td><td>5.58</td><td>5.56</td><td>5.22</td><td>5.22</td><td>5.22</td><td>5.22</td><td>4.40</td><td>5.05</td></tr><tr><td>US$/t</td><td>12,818</td><td>11,350</td><td>12,000</td><td>13,000</td><td>13,000</td><td>13,000</td><td>11,500</td><td>11,500</td><td>10,053</td><td>12,292</td><td>12,250</td><td>11,500</td><td>11,500</td><td>11,500</td><td>11,500</td><td>9,700</td><td>11,141</td></tr><tr><td rowspan="2">COMEX Copper</td><td>US$/lb</td><td>5.83</td><td>5.17</td><td>5.50</td><td>6.01</td><td>6.01</td><td>6.01</td><td>5.32</td><td>5.32</td><td>4.85</td><td>5.63</td><td>5.67</td><td>5.32</td><td>5.32</td><td>5.32</td><td>5.32</td><td>4.49</td><td>5.15</td></tr><tr><td>US$/t</td><td>12,852</td><td>11,407</td><td>12,120</td><td>13,260</td><td>13,260</td><td>13,260</td><td>11,730</td><td>11,730</td><td>10,691</td><td>12,410</td><td>12,495</td><td>11,730</td><td>11,730</td><td>11,730</td><td>11,730</td><td>9,894</td><td>11,364</td></tr><tr><td rowspan="2">LME Nickel</td><td>US$/lb</td><td>7.86</td><td>7.26</td><td>7.71</td><td>7.48</td><td>7.48</td><td>7.48</td><td>7.48</td><td>7.48</td><td>6.94</td><td>7.58</td><td>7.48</td><td>7.48</td><td>7.71</td><td>8.16</td><td>8.16</td><td>7.44</td><td>8.54</td></tr><tr><td>US$/t</td><td>17,325</td><td>16,000</td>

[中间内容因长度限制已省略]

ational Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., authorised and regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

© 2026 MS
"""
