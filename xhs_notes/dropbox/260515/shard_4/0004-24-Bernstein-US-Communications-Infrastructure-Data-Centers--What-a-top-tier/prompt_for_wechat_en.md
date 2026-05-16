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
# US Communications Infrastructure

# Data Centers: What a top-tier data center market looks like—including the DLR and EQIX footprints

![](images/d716b6bafe57267804ccc2e0551ba3245379e6c676dbe15af194226df96ac5f3.jpg)

Madison Rezaei

+1 917 344 8622

madison.rezaei@Bernsteinsg.com

![](images/a5ad0fcd06721aef3ab342e44e2572a9a4a422ae8b08291eef48424a9b9f080c.jpg)

Nancy Wu

+1 917 344 8545

nancy.wu@Bernsteinsg.com

We're fielding a lot of questions on data center buildouts, at least in part driven by the daily headlines on power delays, NIMBYism, and supply chain constraints. Most of our answers boil down to "it depends on what market(s) you're looking at - we feel pretty good about Major Metros and the players building / buying there". In this note, we do a comparison of market types and a deep dive into three of the top U.S. markets.

We think of three data center market archetypes: Major Metro markets (typically considered the top 8-10 in North America), Minor Metro markets (sometimes thought of as Tiers 2-4, smaller Cities or the extreme outskirts of Major Metros), and Rural markets. The two public data center company footprints, DLR (OP, \$232) and EQIX (OP, \$1,222) are overwhelmingly concentrated in Major and Minor Metros; they are among the most insulated from market noise.

Major Metros are and will continue to be the most important markets for latency-sensitive use cases (including inferencing), as well as enterprise colocation. These markets are well established and hard to build in. Power queues are long, build costs are high, and supply chains are tight. Existing capacity and in-progress, permitted builds are valuable. We are seeing an increase in NIMBYism in these markets, particularly NoVa and Phoenix, in part driven by rising power costs. We believe the established builders will manage this appropriately, but it is an emerging risk.

After Major Metros, overflow goes into Minor Metros. This works where there is marginally less latency sensitivity and/or marginally more price sensitivity. There has been significant growth in these markets over the last \~5 years, which we anticipate continuing.

Finally, training, latency-insensitive, and/or very price sensitive workloads take place in Rural markets. These markets tend to have larger facilities, more speculative builds, and less experienced developers than Major Metros. On the positive side, there is faster power availability and lower cost to build. On the negative side, there is not as clear visibility to sustained demand.

In the U.S., the biggest data center market is Northern Virginia (NoVa), which has \~8GW of supply today, \~5GW under construction, and power queues reportedly in the seven-year range. Pricing in NoVa has only gone up over the last several years, currently around \$217/KW/mo, with vacancy stable below 1%. While there has been some recent news around the Digital Gateway Project (QTS and Compass), this market is typically a well-oiled machine.

This quarter, both DLR and EQIX spoke about large hyperscale-focused builds outside of Atlanta, another top U.S. data center market growing quickly (\~2GW today, \~3GW under construction). Atlanta pricing is \$175/KW/mo today, with vacancy around 2%. We like this strategy - market dynamics are favorable, both DLR and EQIX are savvy builders with strong, experienced teams in the Major Metros, and relatively limited execution risk. We remain positive on both DLR and EQIX, believing both companies will deliver on their build projections given their Major Metro market exposure.

Bernstein TICKER TABLE 

<table><tr><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td colspan="2">14 May2026</td><td colspan="2">TTMRel.</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td rowspan="2">ClosingPrice</td><td rowspan="2">PriceTarget</td><td rowspan="2">Perf.</td><td rowspan="2">Cur</td><td rowspan="2">2025A</td><td rowspan="2">2026E</td><td rowspan="2">2027E</td><td rowspan="2">2025A</td><td rowspan="2">2026E</td><td rowspan="2">2027E</td><td></td></tr><tr><td>Ticker</td><td>Rating</td><td>Cur</td><td></td></tr><tr><td>DLR (Digital Realty)</td><td>O</td><td>USD</td><td>192.84</td><td>232.00</td><td>(10.9)%</td><td>USD</td><td>3.87</td><td>2.74</td><td>2.37</td><td>49.8</td><td>70.5</td><td>81.2</td><td></td></tr><tr><td>EQIX (Equinix)</td><td>O</td><td>USD</td><td>1,079.68</td><td>1,222.00</td><td>(1.6)%</td><td>USD</td><td>14.96</td><td>17.88</td><td>21.36</td><td>72.2</td><td>60.4</td><td>50.5</td><td></td></tr><tr><td>SPX</td><td></td><td></td><td>7,501.24</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended   
Source: Bloomberg, Bernstein estimates and analysis.

# INVESTMENT IMPLICATIONS

We value DLR on a Price to Adjusted Funds from Operations (AFFO) per share multiple. Our \$232 price target is based on 27x our 2027E AFFO per share of \$8.60.

We value EQIX on a Price to Adjusted Funds From Operations (AFFO) per share multiple. Our \$1,222 price target is based on 25x our 2027E AFFO per share of \$48.63

# DETAILS

# A DEEP DIVE INTO THE TOP U.S. MARKETS

The three market archetypes are essentially based on how developers and customers trade off latency vs. power availability vs. cost—with urban markets optimizing for proximity, rural markets optimizing for scale and power, and secondary markets sitting in between as an equilibrium zone. We see a clear gradient across data center market tiers: Major Metros are optimized for latency-sensitive inference and enterprise colocation, with the highest pricing (\$120–150/kW hyperscale, \$160–230 colo), highest build costs (\$12–15B per GW), tightest cap rates ( $\approx$ 4.5–6.5%), and the longest power delays (4–7 years), while Minor Metros sit in the middle with slightly lower pricing, costs, and delays but higher yields; in contrast, Rural markets are primarily focused on large-scale AI training, offering the lowest costs (\$7–9B per GW), fastest power availability (1–3 years), and cheapest hyperscale pricing (\$70–120/kW), but also the highest cap rates ( $\approx$ 6.5–9%+) and minimal colocation presence—leading to a broader industry shift where growth and new capacity increasingly migrate from constrained urban hUBS to lower-cost, power-rich rural regions.

EXHIBIT 1: Comparing Tiers of Data Center Markets 

<table><tr><td></td><td>Major Metro</td><td>Minor Metro</td><td>Rural</td></tr><tr><td>Use Cases</td><td>Inference, Enterprise Colo</td><td>Inference, Enterprise Colo</td><td>Training</td></tr><tr><td>Hyperscale Pricing</td><td>$120-150</td><td>$90-130</td><td>$70-120</td></tr><tr><td>Colo Pricing</td><td>$160-230</td><td>$150-190</td><td>-</td></tr><tr><td>Estimated Size Today (U.S. GW)</td><td>21.5</td><td>23.6</td><td>23.6</td></tr><tr><td>Estimated Planned (U.S. GW)</td><td>25.7</td><td>26.1</td><td>37.0</td></tr><tr><td>Build Costs per GW</td><td>$12-15B</td><td>$9-12B</td><td>$7-9B</td></tr><tr><td>Hyperscale Cap Rates</td><td>4.5-6.0%</td><td>5.5-6.75%</td><td>6.5-8.0%</td></tr><tr><td>Colo Cap Rates</td><td>5.5-6.5%</td><td>6.0-7.25%</td><td>7.0-9.0%</td></tr><tr><td>Power Queues</td><td>4-7 years</td><td>3-5 years</td><td>1-3 years</td></tr><tr><td>Development Risk</td><td>Med (zoning, local pushback)</td><td>Med (zoning, local pushback)</td><td>Low</td></tr></table>

Source: Omdia, CBRE, JLL, Bernstein analysis

EXHIBIT 2: NoVA, the Bay Area, and Dallas/Ft. Worth have the most existing facilities today   
Top U.S. Data Center Markets - # of Existing Facilities   
![](images/3055e7a8a96e353b5b3bf370d6d758b81278b1e96db62438c841095ed7c6e5fd.jpg)

<details>
<summary>bar</summary>

| Location | Value |
| :--- | :--- |
| Northern Virginia | 278 |
| Silicon Valley | 123 |
| Dallas/Ft. Worth | 109 |
| Chicago | 92 |
| New York Tri-State | 79 |
| Phoenix | 58 |
| Atlanta | 55 |
| Hillsboro | 33 |
</details>

Source: Omdia, Bernstein analysis

EXHIBIT 3: ... while NoVA, Dallas/Ft. Worth, and the Chicago metro area have the most capacity today   
Top U.S. Data Center Markets - Existing Capacity (MW)   
![](images/2a9996d92eb2967d8522904353ae90712f11233fd1cf538df57f4be0f06461ee.jpg)

<details>
<summary>bar</summary>

| Location | Value |
| :--- | :--- |
| Northern Virginia | 7,988 |
| Dallas/Ft. Worth | 3,078 |
| Chicago | 2,689 |
| Phoenix | 2,117 |
| Atlanta | 1,990 |
| Silicon Valley | 1,672 |
| Hillsboro | 1,096 |
| New York Tri-State | 688 |
</details>

Source: Omdia, Bernstein analysis

EXHIBIT 4: Chicago, Atlanta, and Phoenix are expected to gain the most capacity over 2026-2030   
Top U.S. Data Center Markets - Planned Capacity w/ Known Open Dates (MW)   
![](images/ead1ca893ceb5165cc6a4aa609d527ea9d368b197d697dd1179101087b1c646b.jpg)

<details>
<summary>bar_stacked</summary>

| Year | Northern Virginia | Dallas/Ft. Worth | Chicago | Phoenix | Silicon Valley | Hillsboro | Atlanta | New York Tri-State |
|------|-------------------|------------------|---------|---------|----------------|-----------|---------|--------------------|
| 2026 | ~250              | ~400             | ~1000   | ~300    | ~50            | ~50       | ~50     | ~50                |
| 2027 | ~200              | ~350             | ~800    | ~250    | ~50            | ~50       | ~50     | ~50                |
| 2028 | ~100              | ~150             | ~400    | ~150    | ~50            | ~50       | ~50     | ~50                |
| 2029 | ~50               | ~100             | ~100    | ~50     | ~50            | ~50       | ~50     | ~50                |
| 2030 | ~10               | ~10              | ~10     | ~10     | ~10            | ~10       | ~10     | ~10                |
</details>

Source: Omdia, Bernstein analysis

EXHIBIT 5: ... as well as the greatest increase in number of facilities   
Top U.S. Data Center Markets - # of Planned Builds w/ Known Open Dates   
![](images/b24a03e95360582cbb7836881598d701e749c4096ff2f515869a3279c7258d33.jpg)

<details>
<summary>bar_stacked</summary>

| Year | Northern Virginia | Dallas/Ft. Worth | Chicago | Phoenix | Silicon Valley | Hillsboro | Atlanta | New York Tri-State |
|------|-------------------|------------------|---------|---------|----------------|-----------|---------|--------------------|
| 2026 | 3                 | 5                | 14      | 3       | 0              | 1         | 0       | 7                  |
| 2027 | 1                 | 3                | 8       | 2       | 1              | 0         | 0       | 4                  |
| 2028 | 0                 | 0                | 7       | 1       | 0              | 1         | 1       | 2                  |
| 2029 | 0                 | 0                | 2       | 0       | 1              | 0         | 1       | 0                  |
| 2030 | 0                 | 0                | 0       | 0       | 1              | 0         | 0       | 0                  |
</details>

Source: Omdia, Bernstein analysis

EXHIBIT 6: Chicago, NoVA, and Atlanta have the most number of planned builds, including planned builds with unknown open dates   
Top U.S. Data Center Markets - Total # of Planned Builds   
![](images/e3797da5810fd9ac351a5f580d913fe38b71c01be025d6e75f0e5c65eb625b9f.jpg)

<details>
<summary>bar</summary>

| City | Value |
| :--- | :--- |
| Chicago | 56 |
| Northern Virginia | 45 |
| Atlanta | 30 |
| Phoenix | 20 |
| Dallas/Ft. Worth | 15 |
| Silicon Valley | 9 |
| Hillsboro | 6 |
| New York Tri-State | 4 |
</details>

Source: Omdia, Bernstein analysis

EXHIBIT 7: ... as well as the most planned capacity, with \~5GW in both NoVA and Chicago, and >3GW in Atlanta   
Top U.S. Data Center Markets - Total Planned Capacity (MW)   
![](images/a48d56a665c2d7701662c8aecbbbd3204c948d7bc21fc7539753fedba6fb6fdf.jpg)

<details>
<summary>bar</summary>

| Location | Value |
| :--- | :--- |
| Northern Virginia | 5,108 |
| Chicago | 5,089 |
| Atlanta | 3,222 |
| Phoenix | 2,212 |
| Silicon Valley | 1,677 |
| Dallas/Ft. Worth | 1,493 |
| Hillsboro | 445 |
| New York Tri-State | 444 |
</details>

Source: Omdia, Bernstein analysis

EXHIBIT 8: Across the top 8 markets we have identified, the average existing facility is 27 MW versus 112 MW for planned builds, or >4x more capacity   
Avg Facility Size by Market - Operational & Future Builds (MW)   
![](images/b228aae91fd576b26e17b2eccf14508b8b591c476bf436a36e774ee89a793219.jpg)

<details>
<summary>bar</summary>

| City | Operational | Future |
| :--- | :--- | :--- |
| Phoenix | 37 | 111 |
| Atlanta | 36 | 107 |
| Hillsboro | 33 | 74 |
| Chicago | 29 | 91 |
| Northern Virginia | 29 | 114 |
| Dallas/Ft. Worth | 28 | 100 |
| Silicon Valley | 14 | 186 |
| New York Tri-State | 9 | 111 |
</details>

Source: Omdia, Bernstein analysis

EXHIBIT 9: While the largest current providers are Amazon, Meta, Google, and Digital Realty, Amazon and Microsoft have the most ambitious capacity expansion plans, each with 5-6 GW slotted   
10 Largest Providers in Top Markets - Operational & Future Capacity (MW)   
![](images/bb4b773f1ab9dd0fad96ce17ea3608b601f45252f9b00ce1b43d320468d9a67f.jpg)

<details>
<summary>bar_stacked</summary>

| Company | Operational | Future |
| :--- | :--- | :--- |
| Amazon | 2792 | 5047 |
| Microsoft | 1498 | 6088 |
| Google | 2087 | 1812 |
| Meta | 2491 | 180 |
| Digital Realty | 1940 | 317 |
| Vantage | 745 | 1296 |
| CyrusOne | 944 | 1083 |
| QTS | 1564 | 222 |
| Aligned | 1083 | 654 |
| DataBank | 361 | 911 |
</details>

Source: Omdia, Bernstein analysis

# INDIVIDUAL MARKET SNAPSHOTS: COMPARING NOVA, PHOENIX, AND ATLANTA

Northern Virginia (NoVA), Phoenix, and Atlanta illustrate three distinct archetypes within the U.S. data center landscape, each shaped by a different balance of power availability, cost, and ecosystem maturity. NoVA remains the dominant global hub, characterized by unmatched scale, dense interconnection, and hyperscale concentration—supporting premium pricing, the lowest cap rates, and the tightest supply conditions, but also facing the longest power timelines and highest barriers to entry. Phoenix represents a power-advantaged growth market, attracting large hyperscale deployments due to relatively lower costs and more available land, with rising importance as an alternative to constrained Tier 1 hUBS, though with less network density and ecosystem depth than NoVA. Atlanta, meanwhile, sits in between as a rapidly scaling secondary hub that combines proximity to enterprise demand with improving power access and economics, increasingly capturing spillover from primary markets while maintaining a more balanced profile across pricing, growth, and development risk.

EXHIBIT 10: NoVA is the largest and most developed market by far, with a much earlier ramp starting in 2000-2009, though Phoenix and Atlanta are currently the fastest-growing   
Top Markets Total Capacity Growth, 1990-2025   
![](images/2b45d118b561b2fd7331c5b7c3a32d7ff8e0d474da334f4701e113e5c5d96cc5.jpg)

<details>
<summary>line</summary>

| Year | Northern Virginia | Phoenix | Atlanta |
|---|---|---|---|
| 1990-1999 | 357 | 113 | 113 |
| 2000-2009 | 624 | 381 | 381 |
| 2010-2019 | 3,572 | 585 | 585 |
| 2020 | 4,603 | 636 | 636 |
| 2021 | 5,491 | 673 | 868 |
| 2022 | 6,233 | 1,064 | 1,099 |
| 2023 | 6,967 | 1,064 | 1,443 |
| 2024 | 7,368 | 1,676 | 1,873 |
| 2025 | 7,988 | 2,117 | 1,990 |
</details>

Source: Omdia, Bernstein analysis

EXHIBIT 11: The top three markets have seen a consistent decline in available capacity, as rising demand continues to absorb and secure newly delivered supply   
Top Markets Available MW   
(Units, 2021-2025)   
![](images/1f04098004d72173a36524ac35e8e72c619260d79d72f0be710393a6f83f06fc.jpg)

<details>
<summary>line</summary>

| Date | Northern Virginia | Phoenix | Atlanta |
| :--- | :--- | :--- | :--- |
| 2H 2021 | 86.1 | 48.1 | 19.0 |
| 1H 2022 | 35.6 | 25.5 | 9.1 |
| 2H 2022 | 27.5 | 28.1 | 9.1 |
| 1H 2023 | 21.3 | 19.2 | 21.3 |
| 2H 2023 | 34.7 | 14.2 | 41.1 |
| 1H 2024 | 38.6 | 16.9 | 27.3 |
| 2H 2024 | 14.0 | 11.5 | 25.7 |
| 1H 2025 | 25.4 | 10.5 | 24.2 |
| 2H 2025 | 21.5 | 10.5 | 28.5 |
</details>

Source: CBRE North America Data Center Trends, Bernstein Analysis

EXHIBIT 12: NoVA stands out as the most prominent market in terms of net absorption, reflecting strong demand for the segment. Similarly, Atlanta has been gaining momentum since 2024, while Phoenix continues to grow at a steady pace   
Top Markets Net Absorption   
(MW, 2021-2025)   
![](images/56e6ff114dc4f8785148a21803c8e10a7d9769b02d6bbd5ac5682646afc30d0d.jpg)

<details>
<summary>bar</summary>

| Period | Northern Virginia | Phoenix | Atlanta |
| :--- | :--- | :--- | :--- |
| 2H 2021 | 303 | 30 | 70 |
| 1H 2022 | 269 | 46 | 30 |
| 2H 2022 | 437 | 44 | 33 |
| 1H 2023 | 193 | 44 | 8 |
| 2H 2023 | 424 | 49 | 18 |
| 1H 2024 | 108 | 148 | 14 |
| 2H 2024 | 452 | 246 | 706 |
| 1H 2025 | 539 | 83 | 281 |
| 2H 2025 | 1,102 | 206 | 456 |
</details>

Source: CBRE North America Data Center Trends, Bernstein Analysis

EXHIBIT 13: Vacancy rates in top markets have significantly declined due to strong demand growth, reaching notably low levels of approximately 1%–2%   
![](images/812ce07ca6bf12721aa60e7526f2f4339fbff2a643749e2702b8d2d671289bd6.jpg)

<details>
<summary>line</summary>

| Period   | Northern Virginia | Phoenix | Atlanta |
| -------- | ----------------- | ------- | ------- |
| 2H 2021  | 5.1%              | 11.9%   | 8.3%    |
| 1H 2022  | 1.9%              | 7.8%    | 3.6%    |
| 2H 2022  | 1.0%              | 8.5%    | 3.6%    |
| 1H 2023  | 0.9%              | 5.3%    | 7.4%    |
| 2H 2023  | 1.4%              | 3.9%    | 13.3%   |
| 1H 2024  | 1.5%              | 3.3%    | 8.8%    |
| 2H 2024  | 0.5%              | 1.9%    | 2.6%    |
| 1H 2025  | 0.7%              | 1.5%    | 1.9%    |
| 2H 2025  | 0.5%              | 1.3%    | 2.0%    |
</details>

Source: CBRE North America Data Center Trends, Bernstein Analysis

EXHIBIT 14: Across the three markets, the average four-year CAGR is 13%, reflecting strong demand, with Phoenix the most stable since 2023.   
![](images/d037192cc0fa8969181d2e16fdcaa8ac75e3bbc6da991a65b1dbd7978b6dcb33.jpg)

<details>
<summary>line</summary>

| Period    | Northern Virginia | Phoenix | Atlanta |
| --------- | ----------------- | ------- | ------- |
| 2H 2021   | $103              |         | $123    |
| 1H 2022   | $118              | $123    | $113    |
| 2H 2022   | $120              | $130    |         |
| 1H 2023   | $130              | $185    | $118    |
| 2H 2023   | $170              | $185    | $125    |
| 1H 2024   | $185              | $190    

[中间内容因长度限制已省略]

is report, to train or finetune any third-party machine learning or artificial intelligence system, or as a prompt or input into any such system. You also may not, without Bernstein's express written consent, do any of the foregoing in connection with your own internal machine learning or artificial intelligence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or sUBScribe for shares, or to induce engage in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek for independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a Citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
