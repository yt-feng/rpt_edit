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
1. `# 标题`：一句主判断，不超过 32 字。
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
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# GLOBAL ECONOMICS ANALYST

# Assessing Global Growth Risks from Middle Eastern Supply Shortages

Three months into the Iran War and despite ongoing negotiations, transits through the Strait of Hormuz remain depressed. While global growth has so far held up reasonably well, concerns persist that it is just a matter of time before accumulating supply shortages lead to outsized reductions in activity. In this Global Economics Analyst we evaluate the economic impacts of a risk scenario where persistent closure of the strait leads to an indefinite loss of Middle Eastern commodity supplies.

We continue to expect that most of the demand destruction required to clear markets will be driven by prices, which have risen sharply for highly exposed products. This is especially true for oil, where we continue to see our growth rules of thumb as appropriate. That said, if supply constraints were to start binding for oil, the growth impacts could rise beyond the $1 - 1.5\%$ implied by our severely adverse price scenario.

The bigger risk of outright stockouts probably resides with non-oil commodities, where markets are less global and supply is often regional. Non-oil commodity supply from the Middle East only accounts for 1.3% of global GDP, but under an extreme assumption in which each input is critical and output in each industry declines in proportion to the binding commodity supply restriction—what economists call a Leontief production function—supply losses could drive very large reductions to output.

There are three reasons why we would expect the growth hit to remain more contained, however. First, the implied GDP hit falls sharply when we exclude inputs that account for a trivial share of production. Second, reallocation of scarce inputs from low- to high-value-add uses materially lowers the drag. Third, even modest substitutability across inputs lowers it further. Under reasonable assumptions for each channel, we estimate the direct growth headwinds from non-oil supply disruptions could lower global GDP by $0.4 - 0.5\%$ , with downstream supply impacts moderately amplifying these impacts.

Data so far appears to align with these predictions, as anecdotes suggest that demand destruction has skewed toward lower-income countries and lower-value added industries, and industrial production data has yet to show signs of binding supply constraints. Moreover, supply-constrained product prices have retraced somewhat in recent weeks.

# Megan Peters

+44(20)7051-2058

megan.l.peters@gs.com

GS International

# Assessing Global Growth Risks from Middle Eastern Supply Shortages

Three months into the Iran War and despite ongoing negotiations, transits through the Strait of Hormuz remain depressed, with reported vessel counts down over $90\%$ from normal levels. Our baseline commodity and economic forecasts assume a normalization in Gulf exports by end-June, but risks appear increasingly skewed towards a longer supply disruption.

Exports from the Persian Gulf account for sizeable shares of global trade in several key industrial and agricultural inputs—most notably oil, but also fertilizers, natural gas, refined products, petrochemicals, steel and aluminum (Exhibit 1). While we argued shortly after the start of the war that the supply shock would be manageable and mostly limited to energy, the extended supply disruption has raised concerns that accumulating shortages and production bottlenecks could be more disruptive to the global economy.

Against this backdrop, in this Global Economics Analyst we model an indefinite loss of Middle Eastern commodity supplies to estimate the GDP headwind if supply constraints increasingly become binding.

Exhibit 1: Exports from the Middle East Account for a Large Share of Global Trade in Certain Key Industrial and Agricultural Inputs, Although Their Share of Global GDP is Smaller   
Middle East Goods Exports to RoW   
![](images/2dd561a302f043a9adfbd57c15c2a054d21574e835d8b069c9a716c9d37ae743.jpg)

<details>
<summary>bar</summary>

| Category | As Share of Imports (%) |
|---|---|
| Other Fertilizer | 32 |
| Oil | 18.5 |
| Other Hydrocarbons | 17.5 |
| Tobacco | 16.0 |
| Natural Gas | 14.5 |
| Recycled Steel | 13.5 |
| Petroleum Refining | 12.5 |
| N-Fertilizer | 9.5 |
| Cement/Lime | 9.0 |
| Medical/Optical | 7.5 |
| Furniture/Other Mfg | 6.5 |
| Aluminum | 6.0 |
| Lead/Zinc/Tin | 5.5 |
| Veg/Fruit/Nuts | 5.5 |
| Basic Plastics | 4.5 |
| Glass | 4.5 |
| Fibers | 4.0 |
| Copper | 4.0 |
| Printed Media | 4.0 |
| Precious Metals | 4.0 |
| Total | 2.0 |
</details>

![](images/7d9b7ba07bcdeae9c0d877d97f3aa2d1897e1058362db56df99b9f605eb241fa.jpg)

<details>
<summary>bar_stacked</summary>

| Country/Region | Oil (%) | Non-oil (%) |
|---|---|---|
| South Korea | 2.8 | 1.3 |
| India | 2.5 | 1.8 |
| South Africa | 0.6 | 1.3 |
| Türkiye | 0.0 | 1.9 |
| China | 1.4 | 0.6 |
| Japan | 1.7 | 0.3 |
| Switzerland | 0.0 | 1.6 |
| Indonesia | 0.3 | 0.7 |
| Spain | 0.4 | 0.4 |
| Italy | 0.4 | 0.4 |
| Poland | 0.5 | 0.3 |
| France | 0.3 | 0.4 |
| Brazil | 0.2 | 0.4 |
| UK | 0.3 | 0.5 |
| Hungary | 0.3 | 0.4 |
| Romania | 0.3 | 0.4 |
| Canada | 0.2 | 0.3 |
| US | 0.2 | 0.3 |
| Australia | 0.2 | 0.3 |
| Russia | 0.2 | 0.3 |
| Czechia | 0.2 | 0.3 |
| Germany | 0.2 | 0.3 |
| Denmark | 0.2 | 0.3 |
| Sweden | 0.1 | 0.2 |
| Norway | 0.1 | 0.1 |
| Mexico | 0.1 | 0.1 |
| World ex-ME | 0.8 | 0.6 |
</details>

Source: Exiobase, GS Global Investment Research

We continue to expect that most of the demand destruction required to clear markets will be driven by prices, which have risen sharply for highly exposed products (Exhibit 2). Crude oil prices have risen by up to $50\%$ , with even larger increases for refined products like gasoline, jet fuel and diesel (Exhibit 2, left). At the same time, base chemical prices rose more than $60\%$ from the start of the conflict to April, the fastest rate ever recorded. Spot prices for helium—a byproduct of natural gas extraction and an indispensable input for cryogenic applications including semiconductor production—are reported to have doubled since the start of the conflict (though the majority of the industry works on contract pricing that is up much less). Sulfur and sulfuric acid, key inputs for copper refining, phosphate fertilizer and titanium dioxide production, are up over $60\%$ , while methanol—a critical feedstock for a range of petrochemicals including formaldehyde

and acetic acid—is up $40\%$ (Exhibit 2, right).

Exhibit 2: Commodity Prices Have Surged In Response to the Supply Shock   
Reported Price Increases Since Feb 27, 2026   
![](images/d9971e9baa8ae0b998975699798815f8227c19fd43c43edfd8ac821c4ee5824f.jpg)

<details>
<summary>bar</summary>

| Category | US (%) | Europe (%) | Asia (%) |
|---|---|---|---|
| Crude | 47 | 46 | 38 |
| Natural Gas | 5 | 45 | 40 |
| Jet Fuel | 29 | 37 | 43 |
| Gasoline | 56 | 44 | 44 |
| Fuel Oil | 31 | 39 | 50 |
| Diesel | 34 | 42 | 50 |
Organic Chemicals
| Percent: US | Organic Chemicals
| Percent: Europe | Organic Chemicals
| Percent: Asia |
The chart displays two vertical bars for each category. The first bar is labeled 'Natural Gas', and the second bar is labeled 'Gasoline'. The legend indicates the color coding: dark blue for US, light blue for Europe, gray for Asia.
</details>

![](images/c15a520835aa07953a93f568a1416d62dd83a9fb8dbc3b57221d4217d243b5d3.jpg)

<details>
<summary>bar</summary>

Other Chemicals and Metals
| Category | Percent (%) |
|---|---|
| Sulfur (Vancouver) | 116 |
| Helium | 100 |
| Sulfur (China) | 83 |
| Sulfuric Acid | 69 |
| Polypropylene | 45 |
| Methanol | 39 |
| Pesticide | 39 |
| Polyethylene | 30 |
| Butadiene Rubber | 25 |
| Polyester filament | 22 |
| Aluminum | 18 |
| Glacial Acetic Acid | 12 |
| Urea | 2 |
</details>

Source: ICE, Platts, Haver Analytics, GS FICC and Equities, Trading Economics, CNBC, GS Global Investment Research

Our expectation that price increases will destroy enough demand to avoid outright stockouts applies especially to oil. While oil inventories are being drawn down rapidly, under our baseline forecasts OECD commercial oil inventories remain above pre-shale averages, although commercial products inventories are lower. Against this backdrop, we continue to see our standard rules of thumb—particularly those adjusted for natural gas price increases—as providing a valid guide to the hit to GDP from higher energy prices. Currently our growth estimates and baseline commodity forecasts imply a 1/2pp hit to GDP, although the drag could rise dramatically if supply remains curtailed for much longer (Exhibit 3).

Exhibit 3: Crude Inventories Remain Above Historical Levels Despite Rapid Drawdowns; Our Rules of Thumb Capture the Growth Impact of Demand Destruction via Higher Prices   
![](images/232be838f46af298e5e3693cd24b1dc1301ce95fa8625816e4c348a8298d4301.jpg)

<details>
<summary>line</summary>

| Year | Realized | GS Forecast |
|------|----------|-------------|
| 2000 | ~58      | ~56         |
| 2004 | ~51      | ~50         |
| 2008 | ~53      | ~52         |
| 2012 | ~59      | ~58         |
| 2016 | ~67      | ~66         |
| 2020 | ~74      | ~73         |
| 2024 | ~62      | ~61         |
| 2028 | ~63      | ~62         |
</details>

![](images/f86976346d3f8548e70f375ae8783ef3883342ca5e77e74ea96b491676e25cc8.jpg)

<details>
<summary>bar</summary>

GS Baseline: Effect of Energy Prices on Real GDP (1 Year Ahead)
| Country/Region | Baseline (%) | Adverse (%) | Severely Adverse (%) |
| :--- | :--- | :--- | :--- |
| Brazil | 1.25 | 1.65 | 2.35 |
| Canada | 0.95 | 1.3 | 1.75 |
| China | -0.2 | -0.4 | -0.6 |
| Japan | -0.4 | -0.5 | -0.8 |
| US | -0.4 | -0.6 | -0.7 |
| Australia | -0.9 | -1.1 | -1.8 |
| UK | -1.0 | -1.3 | -2.0 |
| Euro Area | -1.05 | -1.35 | -2.1 |
| India | -1.35 | -1.65 | -2.5 |
| Global ex-ME | -0.6 | -0.85 | -1.1 |
</details>

Source: GS Global Investment Research

# A Quantity-Based Approach to the GDP Impacts from Supply Reductions

A complementary approach to assessing the growth downside from supply disruptions is to look at quantity losses rather than price increases. This approach is agnostic to the price increases necessary to lower commodity demand enough to match supply, while potentially providing useful insights into where GDP hits could emerge due to supply shortages when markets are less global and regional dynamics matter more.

To implement this quantity-based approach, we leverage the Exiobase IO tables, which measure the supply linkages for 200 products in 163 industries across 44 countries. These tables allow us to measure not only the direct impacts from loss of Middle Eastern commodity supplies, but also the indirect effects on downstream industries. In all subsequent analysis we use these mapped linkages to simulate a complete loss of Middle Eastern supply without considering potential offsets from inventory drawdowns.

To start, Exhibit 4 shows the potential impact of a complete loss of Middle Eastern crude oil supply under the assumption that each downstream sector reduces its output in proportion to its direct and indirect Middle Eastern oil consumption. This exercise implies that around $2\%$ of global GDP is dependent on Middle Eastern oil supply—reflecting a reliance on oil both as a source of energy and petrochemical feedstocks (over $95\%$ of manufactured goods contain petrochemicals)—with South Korea $(-8\%)$ , India $(-7\%)$ and Mainland China $(-5\%)$ especially exposed to oil supply losses. As noted above, however, oil stockouts are less likely given the global nature of oil markets where an outsized price increase would likely be sufficient to destroy demand.

Exhibit 4: A Complete Loss of Middle Eastern Crude Oil Supply Would Likely Lower Global GDP by 2%   
![](images/ab695f95c8a36d9fa60ffcaf671489bc100843f30f12bdd0598f790ab710593f.jpg)

<details>
<summary>bar</summary>

Effect of a 100% Loss of Middle East Oil Supply on GDP (Ghosh Model)
| Country | Region | Percent |
| :--- | :--- | :--- |
| Norway | US & Canada | -0.1 |
| UK | Western Europe | -0.1 |
| Sweden | Western Europe | -0.1 |
| Switzerland | Western Europe | -0.1 |
| Russia | Central & Eastern Europe | -0.2 |
| Denmark | Central & Eastern Europe | -0.2 |
| Germany | Central & Eastern Europe | -0.2 |
| US | US & Canada | -0.3 |
| Mexico | Latin America | -0.4 |
| Czechia | Latin America | -0.5 |
| Türkiye | Central & Eastern Europe | -0.6 |
| Brazil | Latin America | -0.7 |
| Canada | US & Canada | -0.8 |
| Romania | Central & Eastern Europe | -0.9 |
| France | Western Europe | -1.0 |
| Hungary | Central & Eastern Europe | -1.1 |
| Italy | Western Europe | -1.2 |
| Poland | Central & Eastern Europe | -1.3 |
| Spain | Western Europe | -1.4 |
| Australia | Asia-Pacific | -1.5 |
| Indonesia | Asia-Pacific | -2.8 |
| Japan | Asia-Pacific | -3.2 |
| South Africa | Asia-Pacific | -3.5 |
| China | Asia-Pacific | -5.2 |
| India | Asia-Pacific | -7.0 |
| South Korea | Asia-Pacific | -8.0 |
Global Average (ex-ME): -2.0%
</details>

The Ghosh model assumes that each downstream sector reduces its output in proportion to its direct and indirect consumption of the shocked inputs.

Source: Exiobase, GS Global Investment Research

For other refined products and chemicals, supply and stockout concerns are more pressing. Our commodities strategists see the largest shortage risks for petrochemical feedstocks (particularly naphtha), diesel and jet fuel. Shortage risks are particularly acute for diesel, where demand is highly price-inelastic given its importance in industrial applications and limited available substitutes. Across countries, South Africa, India and Taiwan appear most at-risk given large reductions in local product supply and relatively low crude stocks. On the chemicals side, some Asian petrochemical plants have already declared force majeure, and our analysts warn that supply disruptions could extend through to 2027 even if the Strait of Hormuz opens imminently.

We therefore repeat the analysis in Exhibit 4 for non-oil exports from the Middle East in Exhibit 5. Indefinite loss of supply of these products would reflect an $0.7\%$ loss of global non-oil imports and $1.3\%$ hit to global GDP—led by declines in India $(-3.6\%)$ , Turkiye $(-3.3\%)$ and South Korea $(-3.1\%)$ —under the assumption that downstream output is proportionally affected.

Exhibit 5: Downstream GDP Exposure to Middle East Goods Supply Ranges from $0.3\%$ in the US to Over $3\%$ in India, Turkiye and South Korea   
Effect of a 100% Loss of Middle East Non-Oil Goods Supply on GDP (Ghosh Model)   
![](images/7b6a04f988b7371b2e2b76d0d2efa5b226a72399824c1f83cd21c78281fe93dd.jpg)

<details>
<summary>bar_stacked</summary>

| Category | US & Canada (%) | Latin America (%) | Western Europe (%) | Central & Eastern Europe (%) | Asia-Pacific (%) | Africa (%) |
|---|---|---|---|---|---|---|
| Other Fertilizer | -1.5 | -20.0 | -18.0 | -24.0 | -23.0 | -27.0 |
| Iron Ore | 0.0 | 0.0 | 0.0 | -24.0 | -23.0 | 0.0 |
| N-Fertilizer | 0.0 | -12.0 | -16.0 | -24.0 | -23.0 | -21.0 |
| Recycled Ash | 0.0 | 0.0 | -18.0 | -24.0 | -23.0 | -19.0 |
| Sugar | 0.0 | -14.0 | -16.0 | -24.0 | -23.0 | -17.0 |
| Steam/Hot Water | 0.0 | 0.0 | -16.0 | -24.0 | -23.0 | -17.0 |
| Precious Metals | 0.0 | 0.0 | -16.0 | -24.0 | -23.0 | -17.0 |
| Wood/Straw | 1.5 | 0.0 | -14.0 | -24.0 | -23.0 | -17.0 |
| Petroleum Refining | 0.0 | 0.0 | -14.0 | -24.0 | -23.0 | -17.0 |
| Copper | 0.0 | 0.0 | -14.0 | -24.0 | -23.0 | -17.0 |
| Pork | 0.0 | 0.0 | -14.0 | -24.0 | -23.0 | -17.0 |
| Rubber/Plastic Prod | 0.0 | 0.0 | -14.0 | -24.0 | -23.0 | -17.0 |
| Beef | 0.0 | 0.0 | -14.0 | -24.0 | -23.0 | -17.0 |
| Recycled Scrap | 0.0 | 0.0 | -14.0 | -24.0 | -23.0 | -17.0 |
| Recycled Steel | 1.5 | 0.0 | -14.0 | -24.0 | -23.0 | -17.0 |
| Recycled Glass | 1.5 | 1.5 | -14.0 | -24.0 | -23.0 | -17.0 |
| Aluminum | 1.5 | 1.5 | -14.0 | -24.0 | -23.0 | -17.0 |
| Other NF Metals | 1.5 | 1.5 | -14.0 | -24.0 | -23.0 | -17.0 |
| Medical/Optical Products (Coke Products) | 1.5 | 1.5 | -14.0 | -24.0 | -23.0 | -17.0 |
By Industry (ex-ME) Percent
-
</details>

![](images/5271abd06a2c603fe6988b464a3d35d785ac71f6647620d2bbeff934cf6ed3cd.jpg)

<details>
<summary>bar_stacked</summary>

| Country | Agriculture (%) | Mining (%) | Manufacturing (%) | Services (%) | Utilities (%) |
|---|---|---|---|---|---|
| India | -0.2 | -0.4 | -2.8 | -3.5 | 0.0 |
| Turkey | -0.1 | -0.3 | -2.6 | -3.3 | 0.0 |
| South Korea | -0.1 | -0.2 | -2.4 | -3.1 | 0.0 |
| South Africa | -0.1 | -0.2 | -2.2 | -2.9 | 0.0 |
| China | -0.1 | -0.2 | -2.1 | -2.7 | 0.0 |
| Switzerland | -0.1 | -0.2 | -2.0 | -2.5 | 0.0 |
| Indonesia | -0.1 | -0.2 | -1.9 | -2.3 | 0.0 |
| Brazil | -0.1 | -0.2 | -1.8 | -2.1 | 0.0 |
| Hungary | -0.1 | -0.2 | -1.7 | -1.9 | 0.0 |
| Czechia | -0.1 | -0.2 | -1.6 | -1.8 | 0.0 |
| Spain | -0.1 | -0.2 | -1.5 | -1.7 | 0.0 |
| Italy | -0.1 | -0.2 | -1.4 | -1.6 | 0.0 |
| Australia | -0.1 | -0.2 | -1.3 | -1.5 | 0.0 |
| Japan | -0.1 | -0.2 | -1.2 | -1.4 | 0.0 |
| Romania | -0.1 | -0.2 | -1.1 | -1.3 | 0.0 |
| Poland | -0.1 | -0.2 | -1.0 | -1.2 | 0.0 |
| France | -0.1 | -0.2 | -0.9 | -1.1 | 0.0 |
| Denmark | -0.1 | -0.2 | -0.8 | -1.0 | 0.0 |
| Russia | -0.1 | -0.2 | -0.7 | -0.9 | 0.0 |
| UK | -0.1 | -0.2 | -0.6 | -0.8 | 0.0 |
| Germany | -0.1 | -0.2 | -0.5 | -0.7 | 0.0 |
| Sweden | -0.1 | -0.2 | -0.4 | -0.6 | 0.0 |
| Canada | -0.1 | -0.2 | -0.3 | -0.5 | 0.0 |
| Mexico | -0.1 | -0.2 | -0.2 | -0.4 | 0.0 |
| Norway | -0.1 | -0.2 | -0.1 | -0.3 | 0.0 |
| US | -0.1 | -0.2 | 0.0 | 0.1 | 0.2 |
Global Average: -1.3%
</details>

The Ghosh model assumes that each downstream sector reduces its output in proportion to its direct and indirect consumption of the shocked inputs.   
Source: Exiobase, GS Global Investment Research

While these losses are notable, a key lesson from the supply disruptions after the pandemic is that product shortages can create critical chokepoints that propagate through supply chains, thereby reducing output by a larger amount than the share of lost inputs. These dynamics have been of particular concern to investors, since amplified supply reductions (particularly due to limited chemical supplies) could lead to much sharper increases in prices of downstream goods, as was the case for global semiconductor shortages in 2021-2022.

To shed light on these concerns, we repeat our analysis using a bottleneck model of production (formally, a Leontief production function) where a 10% loss of supply of any input leads to a 10% reduction in output in the receiving sector, regardless of whether other inputs are available. Under this more extreme assumption, each input is critic

[中间内容因长度限制已省略]

e have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
