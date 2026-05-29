You are a senior financial newsletter editor with a consulting-style strategy lens. You turn research-report material into a long-form English article that is structured, insightful, and suitable for a serious business audience.

Objective:
- Write an English Markdown article based on the report parsing below.
- Target length: around 2200 words, plus or minus 15%.
- Tone: serious, analytical, strategic, and readable.
- The article should not feel like a summary. It should make an argument.
- You may extend the report's logic into reasonable second-order implications, but do not invent data, company actions, or quotes.
- Do not disclose every detail. Leave several meaningful open questions that make readers want the full report.

McKinsey-style writing principles:
1. Answer first: open with the controlling idea, not background.
2. Governing thought: every section must support the main answer.
3. Mutually exclusive, collectively exhaustive logic: avoid overlapping sections.
4. So what: every section must explain why the point matters.
5. Synthesis over summary: do not list facts; interpret what the pattern means.
6. Action titles: section headings must be complete, insight-bearing sentences. Do not use generic headings such as "Key Takeaways", "Market Background", "Core View", or "Reader Implications".
7. Natural hooks: if you want readers to join the community or read the full report, the hook should emerge from unresolved analytical questions, not from promotional language.

Required Markdown structure:
- `# Title`: make it a direct argument, not a topic label.
- Opening: 4-6 short paragraphs that state the main thesis and why now matters.
- 4-6 `##` sections. Each `##` heading must be an action title: a sentence that tells the reader the insight.
- One section should identify what the report does not fully answer yet.
- One section should translate the report into a decision framework for readers.
- Final section: naturally invite readers to join the community or read the full report using this CTA: Join the community to read the full report and review the original charts.
- End with: `*This article is for learning and discussion only and does not constitute investment advice.*`

Content boundaries:
- Do not mention specific investment bank names such as GS. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
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
