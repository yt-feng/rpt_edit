你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
# China: Trade blows out, but composition matters

- Recent trade strength warrants outlook recalibration   
- Export strength is concentrated in memory ICs, EVs, solar, and batteries, driving 58% of total export gains   
- Imports are lifted more by AI supply-chain needs and commodity stockpiling, not domestic demand   
- Export prices for semis have surged, picked up modestly for EVs, solar, and batteries, but continue to deflate for the rest   
- Much depends on whether the trade truce with the US is extended and the impending new Section 301 tariffs

At the start of the year, we held a cautious view on China trade, expecting headwinds from rising trade barriers and stricter enforcement against transshipment. Setting aside the usual year-start seasonal distortions, the trade data for the first four months of the year has been much stronger than anticipated. It is strong enough to warrant a recalibration of our full-year export and import outlook.

The key questions are where that strength is concentrated, and how much of it reflects rising prices vs. volume. Export value growth has been disproportionately driven by AI-linked memory modules, legacy memory ICs, large batteries, EVs, and solar panels. But the spike in export values is distorted by a surge in semiconductor prices. On the import side, the rebound is tied more to a combination of AI-related demand and renewed commodity stockpiling and far less to domestic demand.

Together, these dynamics suggest that this year's trade strength is more sector- and price-sensitive than the broad, volume-driven story that supported net trade and GDP growth last year. i.e., the contribution to GDP growth and employment will be less.

# New drivers of export strength

Last year, the dominant narrative was China's cost advantage and export deflation improving competitiveness even as U.S. tariff uncertainties intensified and China lost U.S. market share. But this year's export outperformance reflects different forces, despite shipment disruptions to the Middle East. The decisive contributors are auto data processing (ADP) accessories and storage units (e.g. memory modules), integrated circuits (e.g. legacy memory chips), and the “new three” products (EVs, solar panels and lithium batteries).

Between January–April, exports in U.S. \$ terms rose 14.5% oya, and these three segments contributed 8.4% pts (or 58%) of the headline gain (Figure 1). AI-related memory modules and chips alone accounted for 12.4% of total exports in April (Figure 2).

Figure 1: New drivers of China exports %pts contribution to total exports (US\$) %oya growth   
![](images/833f31a1ee083eed7df417b4bc9c5d90c27484f42146209e58857b7ebcf1eae5.jpg)

<details>
<summary>bar_stacked</summary>

| Year | New-three exports | Circuits (mainly memory chips) | ADP accessories (e.g memory modules) |
|---|---|---|---|
| 22 | 3.5 | 1.0 | -0.5 |
| 23 | 1.8 | -1.5 | -0.5 |
| 24 | -0.5 | 1.5 | -0.5 |
| 25 | 0.5 | 1.0 | -0.5 |
| 26 | 9.0 | 7.0 | 2.0 |
</details>

Figure 2: Export growth of selected products   
![](images/c81cb73a9e574dbcc3605e01d9b52bb6b30abcd5a66a26290798e5428fadf3df.jpg)

<details>
<summary>bar</summary>

| Category | Metric | 21-22 (%) | 23-24 (%) | 25 (%) | 26ytd (%) |
|---|---|---|---|---|---|
| Memory module and chips | Avg growth | 10 | 2 | 25.2 | 88.2 |
| Memory module and chips | % of total | 49 | 47 | 7.6 | 11.3 |
| New-three products | Avg growth | 77 | 1 | 26.4 | 55.7 |
| New-three products | % of total | 20 | 3.5 | 4.6 | 5.6 |
Source: China Customs, JPM. Right y-axis for % of total exports.
</details>

Outside these three segments, export growth was relatively steady through 2025, then spiked in February on LNY-related front-loading, before easing in March and settling into mild growth in April (Figure 3).

Figure 3: China export growth breakdown   
![](images/a154c1f7ddd596a7f03dc54a6c58133a2c079d1fc060c5f9e6052845086ddc43.jpg)

<details>
<summary>line</summary>

| Year | Memory chips/modules and new-three products (%) | Others (%) |
|---|---|---|
| 22 | 45 | 20 |
| 23 | -5 | -10 |
| 24 | 10 | 5 |
| 25 | 5 | 0 |
| 26 | 85 | 35 |
</details>

# Middle East conflict: pains and gains

China's policymakers have often highlighted the post-pandemic shift in export composition from the traditional “old three” (clothing, home appliances, furniture) toward the “new three” (electric vehicles, lithium-ion batteries, solar products).

<table><tr><td>Tingting Ge (852) 2800-0143</td><td>Jiayi Li (852) 2800-5229</td></tr><tr><td>tingting.ge@JPM.com</td><td>jiayi.c.li@JPM.com</td></tr><tr><td>JPM Chase Bank, N.A., Hong Kong Branch</td><td>JPM Chase Bank, N.A., Hong Kong Branch</td></tr><tr><td>Feng Zhu (852) 2800 1745</td><td>Tongfang Yuan (852) 2800-0085</td></tr><tr><td>feng.zhu@JPM.com</td><td>tongfang.yuan@JPM.com</td></tr><tr><td>JPM Chase Bank, N.A., Hong Kong Branch</td><td>JPM Chase Bank, N.A., Hong Kong Branch</td></tr></table>

However, these new-energy exports have also encountered mounting pushback in key destination markets, ranging from allegations of state subsidies and unfair competition to concerns over overcapacity and dumping. Against a high base, growth in these categories cooled in 2H 2023 and 2024, turning into a net drag on overall export growth.

Geopolitical uncertainties and the energy shock crisis appear to have created an opportunity for Chinese new energy product manufacturers. Higher and more volatile oil prices improve the relative economics of electrification and accelerate energy-security-driven demand for alternatives, lifting overseas interest in EVs, solar panels, and lithium batteries. At the same time, China's scale and supply-chain depth in these products allow firms to respond quickly with competitive supply, turning solar panels, lithium batteries, and EVs into a more important source of export strength even as domestic auto sales have weakened. Exports of the “new three” products contributed 2.3% pts to the 14.5% oya ytd headline exports growth (Figure 4).

Figure 4: Exports of new-three products   
![](images/b40e4a4c20cda29c1451005bcc9ad9262cc2a73a56df79f2968aaa33b2521384.jpg)

<details>
<summary>bar_stacked</summary>

%pts contribution to total exports %oya growth
| Year | Solar cell (%) | EV (%) | Lithium-ion batteries (%) |
|---|---|---|---|
| 22 | 0.9 | 0.5 | 1.3 |
| 23 | 0.4 | 0.7 | 1.3 |
| 24 | -0.3 | 0.3 | -0.8 |
| 25 | -0.2 | -0.3 | 0.3 |
| 26 | 0.6 | 0.8 | 2.9 |
</details>

# Price changes vary widely

Complicating the interpretation of recent export strength is the growing role of price effects in some of the new export drivers. Memory chips/modules stand out: ADP module unit prices in US\$ terms surged close to 200% oya (vs. 4.9% y/y in 2025), while IC prices rose 92.4% oya in April (vs. 6.9% y/y in 2025). Taken together, the primary driver of memory chip and module export growth has rotated from volume in 2025 to price in recent months (Figure 5). Their average price contribution to export value % oya growth rose to 85.2% pts in April (vs. 5.9% pts on average in 2025). Export prices for the three new products have also picked up this year, reversing the broad deflation seen over the prior two years, but in contrast to semiconductors, volumes appear to have done more of the heavy lifting.

<table><tr><td>Asia Pacific Economic Research China: Trade blows out, but composition matters 22 May 2026</td></tr></table>

Figure 5: Export decomposition   
![](images/95025422dc9020a96de13f695d84f6813e58281b86b8ca4be8d41e3532cb4722.jpg)

<details>
<summary>bar_stacked</summary>

%pts contribution to value %oya growth
| Category | Timeframe | Value (%) |
| :--- | :--- | :--- |
| Memory chips/modules | 22-23 | -10 |
| Memory chips/modules | 24-25 | 8 |
| Memory chips/modules | 26ytd | 87 |
| New-three products | 22-23 | 25 |
| New-three products | 24-25 | -10 |
| New-three products | 26ytd | 15 |
| Others | 22-23 | 0 |
| Others | 24-25 | -5 |
| Others | 26ytd | -5 |
Volume (%pts contribution to value %oya growth)
</details>

Source: China Customs, JPM

AI/memory-linked exporters have benefited from surging memory chip prices, while new energy sectors have been supported by renewed demand amid energy-shock resilience considerations. Beyond the new export drivers, however, export prices (in US\$ terms) for other products remained in deflation as of March (Figure 6), even as PPI and headline export price annual rates turned positive. With CNY strengthening, especially in basket terms, and PPI rising more than expected in April, questions are emerging over whether China's export price competitiveness could begin to erode.

Figure 6: Export price breakdown (in US\$ terms)   
![](images/cca6d20be13a24c5b0b2db4ae31aa7d2f138c50ad83da38b3dcc1139e0ce56e9.jpg)

<details>
<summary>line</summary>

| Year | Headline | Memory chips/moduels and new-three | Others |
|------|----------|-------------------------------------|--------|
| 21   | ~5       | ~-10                                | ~5     |
| 22   | ~10      | ~50                                 | ~10    |
| 23   | ~0       | ~25                                 | ~0     |
| 24   | ~-10     | ~-10                                | ~-10   |
| 25   | ~-5      | ~-5                                 | ~-5    |
| 26   | ~0       | ~60                                 | ~-10   |
</details>

The external energy-shock-driven rise in producer prices raises input costs and increases pressure to pass these costs through to export prices. While China's export prices tend to co-move with PPI, the recent spike in PPI inflation appears to be more concentrated in upstream, labor-light raw materials, with limited transmission into mid-to-downstream sectors so far. Consumer goods PPI remained in deflation. The extent of pass-through also hinges on how persistent the energy shock proves to be.

That said, China's export competitiveness should remain underpinned by its structural cost advantages, namely supply-chain depth, scale efficiencies as a manufacturing hub, and an ecosystem supported by efficient logistics. The energy shock is also hitting economies unevenly: China's energy consumption mix and reserves have made energy-cost pass-through less complete than some of its peers. As a result, even if headline export price growth turns positive, we expect consumer goods, which account for nearly $20\%$ of China's exports, to continue to experience mild deflation, which could help underpin overall export competitiveness.

<table><tr><td>Tingting Ge (852) 2800-0143</td><td>Jiayi Li (852) 2800-5229</td></tr><tr><td>tingting.ge@JPM.com</td><td>jiayi.c.li@JPM.com</td></tr><tr><td>JPM Chase Bank, N.A., Hong Kong Branch</td><td>JPM Chase Bank, N.A., Hong Kong Branch</td></tr><tr><td>Feng Zhu (852) 2800 1745</td><td>Tongfang Yuan (852) 2800-0085</td></tr><tr><td>feng.zhu@JPM.com</td><td>tongfang.yuan@JPM.com</td></tr><tr><td>JPM Chase Bank, N.A., Hong Kong Branch</td><td>JPM Chase Bank, N.A., Hong Kong Branch</td></tr></table>

# Linking to the regional AI supply chain

As China's apparent demand for ADP memory chips and modules has risen, imports of related products have also jumped, primarily driven by prices. Memory module import prices surged $359\%$ oya in April, while import volumes, after expanding solidly through much of the past two years, have recently turned into a net drag. By source market, Korea stands out. Its shipments to China began to gain momentum late last year and have accelerated further recently, lifting the trend pace to $158\% 3\mathrm{m} / 3\mathrm{m}$ saar. A more granular breakdown suggests the strength was concentrated in memory ICs. Import values have been increasingly lifted by the price effect, although underlying volume momentum has also firmed (Figure 7).

Figure 7: China imports from Korea breakdown   
![](images/80a5c6de124fccf7c7908fd4d0661a943c14459749a58ecf77c3058f55e4c85a.jpg)

<details>
<summary>bar</summary>

%pts contr. to %oya growth, both scales
| Category | Year | Value (%) |
| :--- | :--- | :--- |
| Total (by product) | 2025 | -1 |
| Memory IC (b) | 2025ytd | 7 |
| Memory IC (b) | 2026ytd | 48 |
| Others | 2026ytd | -9 |
| Memory IC (RHS) | 2025 | -1 |
| Memory IC (RHS) | 2026ytd | 13 |
| Volume | 2025 | 1 |
| Volume | 2026ytd | 140 |
| Price | 2025 | 140 |
| Price | 2026ytd | 130 |
</details>

Source: China Customs, JPM

This highlights how current import/export momentum is tied to global semiconductor supply tightness and the memory price cycle. Debate has intensified over whether China is also benefiting from the AI upcycle as Korea and Taiwan. We see some evidence: parts of China's AI tech ecosystem have gained from the global AI upcycle, supporting capex expansion. China's legacy chip producers have capacity and cost advantages in mature nodes and have benefited from chip inflation amid strong demand and tight supply. Global demand has broadened as hyperscaler capex extends beyond data-center buildouts to upstream enablers and smaller-cap players, while cybersecurity and infrastructure upgrades are also underpinning chip demand.

That said, China's position in the AI hardware supply chain remains structurally different from Korea and Taiwan, key producers of high-end chips and advanced memory for AI data-center demand that is closely tied to US hyperscalers' capex. China remains a net importer of memory chips and modules, albeit with a narrowing deficit especially for ICs

(Figure 8), and is largely a price taker in that segment. This is more than offset by China's surplus in ICT trade. The AI tech sector's share of the overall economy is also relatively small.

Figure 8: Net trade of selected tech products   
![](images/7f631425cb72e18b4771d83c0d6ab32b330c75220304b168f2abaf0975cc5e67.jpg)

<details>
<summary>line</summary>

| Year | ICT (US$bn, sa) | Electronic ICs (US$bn, sa) |
|---|---|---|
| 16 | 28 | -15 |
| 17 | 27 | -16 |
| 18 | 30 | -17 |
| 19 | 33 | -19 |
| 20 | 30 | -16 |
| 21 | 34 | -18 |
| 22 | 37 | -20 |
| 23 | 39 | -21 |
| 24 | 32 | -15 |
| 25 | 31 | -14 |
| 26 | 30 | -12 |
Source: China Customs, JPM
</details>

# Renewed commodity stockpiling

While the AI upcycle and chip inflation explain part of the import strength since late 2025, questions persist over whether this primarily signals a broader domestic-demand recovery. An additional, and underappreciated, driver is renewed commodity stockpiling. China's stockpiling accelerated in 2023 following the Russia–Ukraine conflict, with commodity import volumes reaching record highs that are difficult to explain by macro fundamentals or price effects (Figure 9).

Figure 9: China commodity import volume growth decomposition   
![](images/3ef93ecae12b6d203882dc77bc7a40b74c68a9cf39d994f403974f0a4394a817.jpg)

<details>
<summary>bar_line</summary>

| Date | Macro fundamentals (%) | Price effect (%) | Non-macro-linked (%) |
|---|---|---|---|
| 12 | 7 | 0 | 15 |
| 13 | 10 | 0 | 20 |
| 14 | 8 | 0 | 18 |
| 15 | 6 | 0 | -15 |
| 16 | 9 | 0 | 12 |
| 17 | 7 | 0 | 10 |
| 18 | 5 | 0 | 8 |
| 19 | 3 | 0 | -5 |
| 20 | 4 | 0 | 10 |
| 21 | 12 | 0 | 20 |
| 22 | 3 | -5 | -5 |
| 23 | 5 | 0 | 15 |
| 24 | 4 | 0 | 10 |
| 25 | 3 | 0 | -10 |
| 26 | 1 | -2 | 10 |
Source: China Customs, NBS, PBOC, JPM
</details>

More recently, heightened geopolitical uncertainty, particularly the Middle East conflict and the associated energy shock, has reinforced energy-security concerns, a theme highlighted by top policymakers at the April Politburo meeting. Stockpiling signals have been visible since 2H last year, even as FAI was collapsing, and appear to have intensified in recent months despite higher commodity prices.

That said, the import picture offers muted evidence of a broad-based domestic demand recovery. Outside of memory chips and modules, and a range of “stockpiling-prone” commodities (energy, minerals, chemicals, and metals), imports of other product categories have seen muted growth (Figure 10).

This composition points to demand that is still relatively narrow and policy-tilted: strength appears concentrated in high-end manufacturing supply chains, while more cyclical, consumption- and private-sector-driven import categories show limited momentum.

Figure 10: China imports breakdown   
![](images/4675cb7743a1f7dc7a7cbd9def4b4d644d7d389b17a4f899ec8869989f98a38f.jpg)

<details>
<summary>line</summary>

| Year | Commodities* | Memory chips/modules | Others |
|------|--------------|------------------------|--------|
| 16   | -10          | -5                     | -5     |
| 17   | 40           | 10                     | 5      |
| 18   | 30           | 20                     | 10     |
| 19   | 0            | 0                      | 0      |
| 20   | -10          | -5                     | -5     |
| 21   | 60           | 40                     | 30     |
| 22   | 0            | 0                      | 0      |
| 23   | -30          | -10                    | -10    |
| 24   | 0            | 0                      | 0      |
| 25   | 0            | 0                      | 0      |
| 26   | 20           | 60                     | 20     |
</details>

Source: China Customs, JPM. \*include HS25-40, 68-83.

# "AI/energy winners"

Taken together, the recent trade impulse looks asymmetric: strength is concentrated in a narrow set of AI- and energy-transition-linked “winners”, while the broader economy remains exposed to higher oil and gas costs that could weigh on margins and activity (seen in April activity data) even as select export categories stay resilient. This backdrop is further complicated by lingering policy uncertainty, though the feared headwinds from rising trade barriers and stricter enforcement against transshipment have not yet materialized to derail broad export strength. US–China tariff risks remain, and there was no major breakthrough from the recent Trump-Xi summit or the extension of the 1-year truce. In addition, the U.S. could reimpose or extend new Section 301 tariffs soon. Global growth has also been more resilient than expected despite the energy shock, but pressures could still build if energy supply disruptions remain, keeping the external environment a swing factor for trade into 2H.

# Implications for growth and employment

The GDP implications are less clear-cut. Barring a sharp pullback, this year's nominal export growth could reach the high single digits (around $8\%$ in our latest forecast), roughly double our expectation at the start of the year $(3.5\% y / y)$ . Meanwhile, with imports strengthening, driven in part by renewed stockpiling and AI supply-chain inpu

[中间内容因长度限制已省略]

dates may be provided on companies/industries based on company-specific developments or announcements, market

conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 22 May 2026 12:43 AM HKT

Disseminated 22 May 2026 12:43 AM HKT
"""
