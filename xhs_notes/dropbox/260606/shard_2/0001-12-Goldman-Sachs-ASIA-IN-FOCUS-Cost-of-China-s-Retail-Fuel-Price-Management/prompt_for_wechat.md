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
# ASIA IN FOCUS

# Cost of China's Retail Fuel Price Management Modest and Sustainable

To mitigate the global energy-supply shock, Chinese policymakers have implemented a multi-pronged response encompassing domestic price interventions, temporary export restrictions, and import diversification, broadly in line with their past practice. At the core is a pricing mechanism where the government has limited the pass-through rate of global oil price increases to around half since the start of the Middle East conflict. This has partially shielded the domestic economy, albeit at the cost of margin compression for refiners and even fiscal burdens.   
China regulates domestic retail fuel prices through a mechanism anchored by a USD40-130/bbl international crude price corridor. Specifically, when international crude prices fall below USD40/bbl, retail fuel prices freeze, with the surplus directed to a Risk Reserve Fund. International prices above USD130 trigger retail price freezes and government subsidies for refiners. Within this range, full pass-through applies below USD80/bbl, while it shifts to partial pass-through above USD80/bbl.   
Historical patterns suggest that every $10\%$ increase in Brent crude prices would raise domestic gasoline and diesel prices by around $5\%$ , with variations by product and price level. Given that Brent crude has fluctuated within the USD80-130/bbl range in recent months, the pass-through rate is expected to remain modestly below its historical average, reflecting recent discretionary price interventions by the NDRC. We also estimate that every $10\%$ increase in China's domestic retail fuel prices is associated with around $5\%$ decline in domestic oil product retail sales volume historically.   
Since the start of the Middle East conflict, domestic oil product retail sales volume fell 17% yoy in March-April 2026, while average retail prices rose 17% yoy. This implies a larger demand response than historical patterns would suggest, likely because alternatives such as non-oil/gas energy supply and rapid EV adoption are now more widely available than in earlier oil-price upcycles.   
China's oil price interventions appear fiscally manageable, in our view. Based on our estimates, government intervention costs remain modest at around $0.3\%$ of GDP annualized, and could be further mitigated by inventory valuation gains and stronger upstream profitability. This suggests that the broad government sector can comfortably absorb the cost if international prices continue to fluctuate within the recent range.

# Lisheng Wang

+852-3966-4004

lisheng.wang@gs.com

GS (Asia) L.L.C.

# Cost of China's Retail Fuel Price Management Modest and Sustainable

To mitigate the global energy supply shock triggered by the Middle East conflict and the closure of the Strait of Hormuz, Chinese policymakers have implemented a multi-pronged response encompassing domestic price interventions, temporary export restrictions, and import diversification, broadly in line with their past practice. At the core is a pricing mechanism overseen by the National Development and Reform Commission (NDRC), China's top economic planner. Since March 2026, the NDRC has partially insulated domestic retail fuel prices from international volatility by permitting only around half of global oil price increases to be passed through (Exhibit 1). These measures entail costs, as major state-owned refiners such as Sinopec and PetroChina are required to absorb margin compression, and the government may need to provide subsidies when international prices exceed certain thresholds.

In this note, we explain China's domestic retail oil product pricing mechanism, quantify the pass-through from international crude price changes to domestic retail prices and consumption, and estimate the government costs for oil price interventions. China's oil price interventions appear fiscally manageable, in our view. We estimate that government intervention costs remain modest – below 0.3% of GDP annualized – and could be further mitigated by inventory valuation gains and stronger upstream profitability.

Beyond direct price intervention, China has also acted on the supply side by temporarily tightening exports of refined oil products – including gasoline, diesel, and jet fuel – as well as selected by-products such as sulphuric acid (a key input for fertilizers and copper mining). At the same time, it has significantly increased oil imports from Russia and Latin America to partially offset the sharp decline in Middle East supply, $^{1}$ while drawing on previously accumulated inventories to alleviate near-term shortages. Based on our estimates, total oil import volume fell 11% yoy in March-April, as a 38% yoy contraction in imports from the Middle East more than offset the gains from Russia and Latin America (+13% yoy and +64% yoy, respectively; Exhibit 2). Our Global Commodities Strategy team's high-frequency tracker pointed to a sharper drop in China's crude oil imports in May.

The government is also using the shock to accelerate China's long-term shift toward energy independence. Policy support for the “New Three” industries – electric vehicles, lithium-ion batteries, and solar products – has been strengthened, reducing the economy’s long-term exposure to fossil-fuel price jumps. Reflecting this shift, the penetration ratio of new energy vehicles (NEVs) – measured as the share of NEV in total auto sales – rose from 1% in 2016 to 54% in 2025, and increased further to 63% in May 2026, according to data from the China Passenger Car Association (CPCA). During the Labor Day holiday this year (1-5 May), highway EV charging demand jumped 52.8% yoy, meaningfully outpacing passenger trips via roads (+3.5% yoy). Within roads transportation, passenger flows via public transportation services gained 9.5% yoy, while self-driving trips only rose 2.6% yoy. These highlighted the elasticity of oil demand amid higher oil prices, with EV usage and public transportation replacing traditional Internal Combustion Engine (ICE) cars amid higher oil prices.

Exhibit 1: Domestic retail fuel prices have risen less than Brent crude oil prices since the start of the Middle East conflict   
![](images/593609aaca6715499ab186c7881a25fc1a681f2497677f6a0c89a2a0db2d0cb1.jpg)

<details>
<summary>line</summary>

| Date   | China Gasoline (RMB/Ton) | China Diesel (RMB/Ton) | Brent (right) (USD/bbl) |
|--------|--------------------------|------------------------|-------------------------|
| Jan-25 | ~9500                    | ~8500                  | ~75                     |
| Mar-25 | ~9800                    | ~8300                  | ~78                     |
| May-25 | ~9200                    | ~7800                  | ~65                     |
| Jul-25 | ~9000                    | ~8000                  | ~78                     |
| Sep-25 | ~8800                    | ~7800                  | ~70                     |
| Nov-25 | ~8500                    | ~7500                  | ~65                     |
| Jan-26 | ~8300                    | ~7300                  | ~60                     |
| Mar-26 | ~9500                    | ~8500                  | ~110                    |
| May-26 | ~11000                   | ~9500                  | ~105                    |
</details>

Source: Haver Analytics, GS Global Investment Research

Exhibit 2: Increased imports from Russia and Latin America have partially offset falling Middle East supply   
![](images/d73b509eeff462ba20e8ae16d0471b16d2783bd1abcf02a018fbf2f8931b43c4.jpg)

<details>
<summary>area</summary>

| Date     | Total | Others | Latin America | Middle East | Russia |
|----------|-------|--------|---------------|-------------|--------|
| Jan 2023 | 10.5  | 3.0    | 1.5           | 2.0         | 1.0    |
| Jan 2024 | 11.0  | 3.5    | 1.8           | 2.5         | 1.2    |
| Jan 2025 | 11.5  | 4.0    | 2.0           | 3.0         | 1.5    |
| Jan 2026 | 12.5  | 4.5    | 2.5           | 3.5         | 2.0    |
</details>

Source: China Customs, Wind, GS Global Investment Research

# How China's domestic retail oil product pricing framework works

China's domestic retail oil products pricing framework uses a ceiling mechanism to shield the domestic economy from extreme global volatility (Exhibit 3). When international crude prices reach or exceed USD130/bbl, the NDRC typically suspends retail price increases to protect consumers, with the resulting losses absorbed through government transfers to major state-owned refiners. The framework is complemented by a fuel-price linkage system that provides targeted support to essential and price-sensitive sectors such as agriculture and public transport once domestic prices cross specified thresholds.

Conversely, when international prices fall below USD40/bbl, a floor mechanism applies. Rather than allowing refiners to retain the windfall from unchanged retail prices, the surplus is directed to a state-managed Risk Reserve Fund. The fund is earmarked for strategic uses, including energy conservation and emissions reduction, fuel-quality upgrades to meet higher national standards, and measures to strengthen energy security.

When international prices fall between the floor of USD40/bbl and the ceiling of USD130/bbl, USD80/bbl serves as an additional threshold. Below USD80/bbl, the NDRC allows full pass-through to domestic retail prices. Above USD80/bbl, it permits only partial pass-through of the calculated increase and requires refiners to absorb part of the shock through lower processing margins.

Although these price interventions do not involve direct cash transfers to consumers, they remain an important policy tool for stabilizing domestic prices during severe global energy-supply shocks. In addition, the NDRC's reference price is not tied to a single benchmark. Instead, it is based on a weighted basket of international crude prices. While the exact weights are not disclosed to avoid market speculation, industry consensus, including sources quoted by CCTV, identifies Brent, Dubai, and Minas as the main components.

Exhibit 3: An illustration of China's domestic retail oil product pricing framework   
![](images/edd699a6e98ac252d912e05f27520760b640988b30db97eae90f2bfa79e994df.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["NDRC Review Cycle Every 10 Working Days"] --> B{Average International Crude Oil Price (USD)}
    B -->|Below $40 (Floor Threshold)| C["Price Floor Triggered"]
    B -->|Above $130 (Ceiling Threshold)| D["Price Ceiling Triggered"]
    C --> E["No further reduction in domestic retail prices"]
    E --> F["Risk Reserve Fund Collection"]
    F --> G["Difference collected for energy saving and supply security"]
    G --> H["No Adjustment"]
    H --> I["Adjust domestic prices in full alignment with international benchmarks"]
    I --> J["Special Regulatory Intervention? (e.g., 2026)"]
    J --> K["Yes >=$80 to <$130"]
    K --> L["Capped Adjustment"]
    L --> M["Implicit Consumer Subsidy"]
    M --> N["Lower retail costs to protect the real economy"]
    N --> O["New Price Effective at Midnight"]
    O --> H
    J --> P["Direct Refiner Subsidies"]
    P --> Q["Govt covers losses to ensure continued fuel production"]
    Q --> R["Targeted Sector Subsidies"]
    R --> S["Direct payments to Agriculture, Fisheries, and Public Transport"]
    S --> O
    J --> T["Price Frozen or raised by a minimal margin"]
    T --> U["Price Ceiling Triggered"]
    U --> V["Normal Range: $40 to $130"]
    V --> W{Is model implied price change > RMB 50 /ton?}
    W -->|No| C
    W -->|Yes| J
```
</details>

Source: NDRC, GS Global Investment Research

# The impact of global oil price changes on domestic retail markets

Changes in international crude prices are only partially transmitted to China's domestic retail fuel prices. Our time series regressions based on monthly data from 2017-26 suggest that every $10\%$ increase in Brent crude price would raise domestic gasoline and diesel prices by around $5\%$ (Exhibit 4). The pass-through rate is generally lower when Brent prices are closer to the ceiling or floor than when they are within a more normal range (also see our earlier studies here and here for more analyses on the pass-through impact). Given that Brent crude has fluctuated within the USD80-130/bbl range in recent months, the pass-through rate is expected to remain modestly below its historical average, reflecting recent discretionary price interventions by the NDRC.

Exhibit 4: Every 10% increase in Brent crude price would raise domestic gasoline and diesel prices by around 5% 

<table><tr><td colspan="9">Sample period: 2017M1 - 2026M5</td></tr><tr><td>Dependent variables</td><td colspan="4">Log (Gasoline Price)</td><td colspan="4">Log (Diesel Price)</td></tr><tr><td>Explanatory variables</td><td>Full sample(1)</td><td>Brent &gt;= 70 and &lt;100(2)</td><td>Brent &lt; 70 or &gt;=100(3)</td><td>Brent &gt;= 80 and &lt;130 (recent range)(4)</td><td>Full sample(5)</td><td>Brent &gt;= 70 and &lt;100(6)</td><td>Brent &lt; 70 or &gt;=100(7)</td><td>Brent &gt;= 80 and &lt;130 (recent range)(8)</td></tr><tr><td>Log (Brent oil price)</td><td>0.54(16.44)***</td><td>0.55(5.51)***</td><td>0.49(13.80)***</td><td>0.49(5.07)***</td><td>0.50(8.73)***</td><td>0.78(9.80)***</td><td>0.46(7.57)***</td><td>0.31(5.03)***</td></tr><tr><td>Log (USDCNY)</td><td>0.75(4.36)</td><td>0.64(6.56)***</td><td>0.60(1.78)*</td><td>0.42(2.89)***</td><td>1.07(5.04)***</td><td>0.69(3.98)***</td><td>1.27(5.11)***</td><td>0.32(1.64)</td></tr><tr><td>Constant</td><td>1.85(1.63)</td><td>2.51(3.17)***</td><td>2.95(1.30)</td><td>5.19(5.23)***</td><td>-0.28(-0.21)</td><td>1.02(0.82)</td><td>-1.44(-0.91)</td><td>5.48(3.87)***</td></tr><tr><td># observations</td><td>113</td><td>53</td><td>60</td><td>34</td><td>113</td><td>53</td><td>60</td><td>34</td></tr><tr><td>Adjusted R-squared</td><td>0.88</td><td>0.66</td><td>0.87</td><td>0.40</td><td>0.86</td><td>0.78</td><td>0.85</td><td>0.46</td></tr></table>

Note: T-stats in robust standard errors are reported in parentheses;   
\*\*\*, \*\*, \* denotes statistical significance at 1%, 5%, and 10% levels, respectively.

We use Brent oil price at USD70/bbl and USD100/bbl as cut-off levels to divide our full-sample, with sufficient number of observations for sub-sample regressions. USD70/bbl and USD100/bbl have the same absolute distance to their neighboring intervention thresholds (USD40/bbl and USD130/bbl, respectively). Brent prices between USD80/bbl and USD130/bbl refer to the range in recent months, though the sample size is smaller than other regressions.

Source: GS Global Investment Research

Pass-through rates differ across refined oil products depending on the degree of administrative pricing control, end-demand conditions, and market structure. Gasoline and diesel together accounted for $46\%$ of China's total oil product consumption in 2025 (Exhibit 5), which means the NDRC-controlled segment covers less than half of all oil products. For other products such as LPG, naphtha, and fuel oil, refiners generally have greater flexibility to pass through changes in international prices to downstream buyers. Accordingly, the weighted average pass-through rate across all oil products should be higher than the around 0.5 that we estimated on gasoline and diesel prices.

The NBS measure of retail sales for gasoline and other oil products by enterprises above the designated size captures sales by the “Big Three” state-owned oil giants (i.e., Sinopec, PetroChina, CNOOC) and a small number of large private firms. $^{2}$ Compared with the broader NDRC measure of apparent oil product consumption, the NBS series excludes sales by smaller gas stations, direct supplies to industry and construction, as well as aviation and shipping sales. We estimate that NBS retail sales volume of gasoline and other oil products accounted for roughly 75% of NDRC apparent oil product consumption in recent years (Exhibit 6).

Exhibit 5: Gasoline and diesel together accounted for less than half of China's domestic oil product consumption in 2025   
![](images/56e0a6ca30e3e2985992a8434c7edc9b5dcb9f5f2359636f59278cf7d96f9e14.jpg)

<details>
<summary>pie</summary>

China oil consumption breakdown by major oil product category (in volume terms, 2025)
| Product Category | Volume (%) |
| :--- | :--- |
| Gasoline | 23 |
| Diesel/Gasoil | 23 |
| LPG | 17 |
| Naphtha | 14 |
| Other Products | 14 |
| Jet/Other Kerosene | 5 |
| Fuel Oil | 4 |
</details>

Source: Wood Mackenzie, Data compiled by GS Global Investment Research

Exhibit 6: NBS oil product retail sales volume accounted for around 75% of NDRC oil product apparent consumption in recent years   
![](images/b7446cb30a68839d21184fb848f90e1f3e29229a5ddc1940cb45bd88f2d09010.jpg)

<details>
<summary>bar_line</summary>

Oil product consumption volume
| Year | NDRC oil product apparent consumption (mn ton) | NBS oil product retail sales by firms at or above the designated size (mn ton) | NBS as % of NDRC (RHS) (%) |
| :--- | :--- | :--- | :--- |
| 14 | 270 | 210 | 78 |
| 15 | 275 | 255 | 93 |
| 16 | 290 | 280 | 95 |
| 17 | 305 | 290 | 94 |
| 18 | 325 | 275 | 83 |
| 19 | 330 | 305 | 90 |
| 20 | 310 | 320 | 106 |
| 21 | 340 | 290 | 88 |
| 22 | 345 | 245 | 71 |
| 23 | 385 | 275 | 70 |
| 24 | 380 | 290 | 76 |
| 25 | 375 | 290 | 77 |
</details>

NBS oil product retail sales volume is based on GS estimates using the weighted average of domestic refined oil prices.   
Source: NDRC, Wind, CEIC, GS Global Investment Research

# Recent government interventions to reduce global oil price pass-through

Since the Middle East conflict that began from end-February, the NDRC has adjusted domestic retail oil product prices seven times as of early June, including five increases and two cuts (Exhibit 7). During the two largest hikes, on 23 March and 7 April, the authority capped the increase at roughly half the level implied by the standard pricing formula, with the intervention cost absorbed by state-owned refiners through reduced processing margins. Across all the seven adjustments, we estimate that the NDRC has passed through around half of the increase in international crude prices to domestic retail oil prices (as the actual cumulative increase in domestic fuel prices since March is 47% less than model implied).

Exhibit 7: A summary of NDRC adjustments to domestic retail oil product prices since the start of the Middle East conflict (as of early June) 

<table><tr><td rowspan="2">Domestic Fuel Price Adjustment Date</td><td colspan="2">Gasoline

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
