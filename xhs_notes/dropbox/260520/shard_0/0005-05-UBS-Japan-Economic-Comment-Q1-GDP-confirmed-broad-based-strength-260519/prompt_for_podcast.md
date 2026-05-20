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
# Japan Economic Comment Q1 GDP confirmed broad-based strength

# Q1 real GDP grows solidly at $2.1\%$ q/q saar

Q1 real GDP grew solidly at 2.1% q/q, saar, following 0.8% in Q4, beating both our expectation and the consensus forecast of 1.7%. On a year-on-year basis, growth came in at 0.6% y/y, marking the seventh consecutive quarter of positive expansion. By demand component, growth was well balanced between domestic and external demand, both of which contributed positively to GDP. For FY2025 (from April to March), real GDP growth marked at 0.8%, steadily accelerating from -0.0% in FY2023 and 0.5% in FY2024. Nominal growth was supported by firm domestic inflation above 2%, reaching a stronger 4.2% in FY2025, following 4.7% in FY2023 and 3.7% in FY2024, broadly in line with levels in the US and the euro area.

While this result predates the impact of higher oil prices due to the closure of the Strait of Hormuz, we believe that the fact the economy remained strong right up until that point was itself a positive factor for the BoJ in moving forward with rate hikes.

# Solid growth across domestic demand components

In detail, real GDP growth was driven roughly equally by domestic demand (+1.0ppt of the 2.1%q/q saar) and net exports (+1.1ppt). Within domestic demand, private consumption rose 0.3%/q, contributing +0.6ppt to overall GDP growth, and exceeding our expectation of 0.1%. With the stabilization of consumer inflation (as measured by the private consumption deflator), from a peak of 3.2% in Q1 2025 to 2.0%, households are seeing gains in purchasing power, supported by historically high real employee compensation (+1.3%y/y since Q4 2024). Capex also remained moderately strong, increasing 0.5%q/q (+3.5%y/y), against the backdrop of the AI investment boom. Public demand expanded moderately as well, rising 0.3% q/q (1.0% y/y), supported by a larger FY2025 government budget compared with FY2024.

In the positively contributed net exports, export decently grew 1.7%q/q, better the imports at 0.5%. As expected, trade of goods finally picked up at 1.7%q/q after two consecutive quarter of fall thanks to a strong rebound in auto related sector (+6.5%q/q) and capital goods (+4.5%q/q) in BoJ trade series. Service exports slightly rose 0.4%q/q, supported by consulting service etc while there was no meaningful contribution from inbound spending (-1.6%q/q).

# Economic Outlook: Elevated downside risks with different conditions from 2022

Our primary concern is likely the downside impact on economic activity stemming from the deterioration in the terms of trade following the surge in crude oil prices. BoJ import/export price index for April confirmed a further worsening in the terms of trade, driven by a sharp increase in import prices (Figure 21). Elevated energy costs are expected to weigh on corporate profits, constrain capital expenditure, and dampen household consumption through a decline in real purchasing power amid rising inflation.

While a deterioration in the terms of trade was also observed in 2022, the current episode is likely to differ from the past. In 2022, the depreciation of the yen helped cushion the impact on corporate profits and capital investment (Figure 22). However, this time the weakening of the yen appears more limited. Moreover, in 2022, households were able to sustain consumption despite declining real purchasing power by drawing down savings (Figure 23). In contrast, the savings rate is already low at present, suggesting that such a buffer may be limited this time (Figure 24).

# Economics

Japan

Go Kurihara

Associate Economist go.kurihara@ubs.com +81-3-5293 3000

Figure 1: Real/nominal GDP (level)   
![](images/ba1b88d9bf4675db758a78dbb7a4ecd050bfeb7de344f51b780885d19bee5ea3.jpg)

<details>
<summary>line</summary>

| Year | Real GDP | Nominal GDP |
|------|----------|-------------|
| 00   | 490      | 540         |
| 02   | 500      | 550         |
| 04   | 510      | 530         |
| 06   | 520      | 540         |
| 08   | 530      | 550         |
| 10   | 510      | 500         |
| 12   | 520      | 510         |
| 14   | 540      | 530         |
| 16   | 560      | 550         |
| 18   | 570      | 560         |
| 20   | 580      | 570         |
| 22   | 590      | 580         |
| 24   | 600      | 610         |
| 26   | 610      | 630         |
</details>

Source: CAO

Figure 2: Actual vs forecast 

<table><tr><td rowspan="2">% q/q, unless otherwise in</td><td colspan="3">q/q</td><td colspan="3">q/q, saar contribution</td><td rowspan="2">vs UBSe</td></tr><tr><td>Actual</td><td>UBS</td><td>BBG</td><td>Actual</td><td>UBS</td><td>BBG</td></tr><tr><td>Real GDP (q/q)</td><td>0.5</td><td>0.4</td><td>0.4</td><td>2.1</td><td>1.7</td><td>1.7</td><td>0.4</td></tr><tr><td>Private consumption</td><td>0.3</td><td>0.1</td><td>0.1</td><td>0.6</td><td>0.2</td><td>0.2</td><td>0.4</td></tr><tr><td>Residential investment</td><td>0.5</td><td>-5.0</td><td></td><td>0.1</td><td>-0.7</td><td></td><td>0.8</td></tr><tr><td>Capex</td><td>0.3</td><td>0.3</td><td>0.3</td><td>0.2</td><td>0.2</td><td>0.2</td><td>-0.0</td></tr><tr><td>Government consumption</td><td>0.1</td><td>0.1</td><td></td><td>0.1</td><td>0.1</td><td></td><td>0.0</td></tr><tr><td>Public investment</td><td>1.4</td><td>-1.0</td><td></td><td>0.3</td><td>-0.2</td><td></td><td>0.4</td></tr><tr><td>Inventories</td><td></td><td></td><td></td><td>-0.2</td><td>0.9</td><td></td><td>-1.1</td></tr><tr><td>Exports of goods &amp; serv.</td><td>1.7</td><td>2.6</td><td></td><td>1.5</td><td>1.9</td><td></td><td>-0.4</td></tr><tr><td>Imports of goods &amp; serv.</td><td>0.5</td><td>2.2</td><td></td><td>-0.4</td><td>-1.5</td><td></td><td>-1.1</td></tr><tr><td>Domestic demand</td><td>0.2</td><td>0.3</td><td></td><td>0.9</td><td>1.3</td><td></td><td>-0.4</td></tr><tr><td>Net exports</td><td></td><td></td><td></td><td>1.1</td><td>0.3</td><td></td><td>0.8</td></tr></table>

Source: CAO, BBG, UBSe

Figure 3: Real/nominal GDP (q/q, saar)   
![](images/0c829eadf8b6fe4cde69be46aceb6a509350b3948d34e37609599041e395b748.jpg)

<details>
<summary>line</summary>

| Year | Real GDP | Nominal GDP |
|------|----------|-------------|
| 16   | 5.0      | 5.0         |
| 17   | 3.0      | 6.0         |
| 18   | 2.0      | 3.0         |
| 19   | 1.0      | 2.0         |
| 20   | -8.0     | 2.0         |
| 21   | 4.0      | 12.0        |
| 22   | 5.0      | 8.0         |
| 23   | 3.0      | 8.0         |
| 24   | -6.0     | 8.0         |
| 25   | 1.0      | 4.0         |
</details>

Source: CAO

Figure 4: Real/nominal GDP (y/y)   
![](images/2ee21dcc343ff6bc6cbe7e9370d782e7edddf050b44aa31a2510f59f0716cf66.jpg)

<details>
<summary>line</summary>

| Year | Real GDP | Nominal GDP |
|------|----------|-------------|
| 10   | 4.0      | 3.5         |
| 11   | 6.0      | 4.5         |
| 12   | -1.0     | -2.5        |
| 13   | 3.5      | 2.0         |
| 14   | 3.0      | 3.5         |
| 15   | 2.5      | 4.0         |
| 16   | 2.0      | 3.5         |
| 17   | 1.5      | 2.5         |
| 18   | 2.0      | 2.0         |
| 19   | 0.5      | 1.0         |
| 20   | -8.0     | -7.0        |
| 21   | 8.0      | 8.0         |
| 22   | 2.0      | 3.0         |
| 23   | 1.0      | 5.0         |
| 24   | -1.0     | 6.0         |
| 25   | 2.0      | 5.0         |
| 26   | 0.5      | 4.0         |
</details>

Source: CAO

Figure 5: Quarterly contribution (q/q, saar)   
![](images/d9dc54ff86d7c1d4f2cae1dc58d5ff2f90c2ff9de1d707230682ed7fd726c950.jpg)

<details>
<summary>bar_line</summary>

| Year | Quarter | Private demand (%) | Public demand (%) | Net export (%) | Real GDP (%) |
|---|---|---|---|---|---|
| 2023 | 1 | 1.5 | 1.8 | 3.2 | 3.4 |
| 2023 | 2 | -3.0 | -3.5 | 4.5 | 0.5 |
| 2023 | 3 | -0.5 | -5.5 | -5.0 | -5.8 |
| 2023 | 4 | 2.8 | 0.0 | -0.5 | 2.2 |
| 2024 | 1 | -2.0 | 0.0 | 0.5 | -1.5 |
| 2024 | 2 | 1.8 | 2.0 | -2.0 | 0.0 |
| 2024 | 3 | 3.5 | 0.5 | -1.0 | 2.8 |
| 2024 | 4 | -1.5 | -1.8 | 3.2 | 1.5 |
| 2025 | 1 | 4.3 | 0.0 | -3.0 | 1.8 |
| 2025 | 2 | 0.5 | 1.0 | 1.3 | 1.4 |
| 2025 | 3 | -0.5 | -1.5 | -1.8 | -2.8 |
| 2025 | 4 | 0.5 | 0.8 | 0.7 | 0.9 |
| 2026 | 1 | 0.5 | 0.8 | 1.8 | 2.1 |
</details>

Source: CAO

Figure 6: Domestic demand was flat   
![](images/6e2df26fbe19b344c1f86818090122c31651d90323eb42f4ea4f0a3a90a22bf8.jpg)

<details>
<summary>bar_line</summary>

%q/q, saar
| Period | Private consumption (%) | Capex (%) | Public demand (%) | Residential investment (%) | Private inventories (%) | Domestic demand (%) |
|---|---|---|---|---|---|---|
| 2023 | 1.0 | 1.5 | 0.5 | 0.5 | -0.5 | -4.0 |
| 2024 | 0.5 | 1.0 | 0.0 | -1.0 | -0.5 | 2.5 |
| 2025 | 1.0 | 0.5 | -0.5 | -0.5 | -1.0 | -1.5 |
| 2026 | 0.5 | 1.0 | 0.5 | -0.5 | -1.0 | 1.0 |
</details>

Source: CA

Figure 7: Private consumption rose 0.3%q/q, better than our expectation (0.1%)   
![](images/795067602efad1b8fe744570fcf6d01e20dedd6151de375e7b9ee1502474cf66.jpg)

<details>
<summary>line</summary>

| Year | Private consumption (LHS) | %q/q |
|------|---------------------------|------|
| 10   | 305                       | -4   |
| 11   | 295                       | -6   |
| 12   | 300                       | -2   |
| 13   | 310                       | 0    |
| 14   | 320                       | 2    |
| 15   | 305                       | -2   |
| 16   | 308                       | -1   |
| 17   | 310                       | 0    |
| 18   | 312                       | 1    |
| 19   | 315                       | 2    |
| 20   | 280                       | -8   |
| 21   | 325                       | -2   |
| 22   | 315                       | 0    |
| 23   | 305                       | 1    |
| 24   | 308                       | 2    |
| 25   | 310                       | 3    |
| 26   | 312                       | 4    |
</details>

Source: CAO

Figure 8: Consumption of both goods and services   
![](images/39c86c88caeb8e1fa7097554629a07f4a53d7321288d5551a056113feb9d4584.jpg)

<details>
<summary>line</summary>

| Year | Services (LHS) | Goods (RHS) |
|------|----------------|-------------|
| 10   | 168            | 120         |
| 11   | 170            | 118         |
| 12   | 172            | 122         |
| 13   | 175            | 125         |
| 14   | 178            | 130         |
| 15   | 179            | 128         |
| 16   | 180            | 126         |
| 17   | 181            | 124         |
| 18   | 182            | 122         |
| 19   | 183            | 120         |
| 20   | 145            | 120         |
| 21   | 160            | 125         |
| 22   | 170            | 123         |
| 23   | 175            | 125         |
| 24   | 178            | 123         |
| 25   | 180            | 125         |
| 26   | 182            | 127         |
</details>

Source: CAO

Figure 9: Breakdown of private consumption (%y/y)   
![](images/318b97fcf322de5afbe5c73677d5dede282b88599463fbf136b9d4d133805a59.jpg)

<details>
<summary>bar_line</summary>

| Year | Category | Private consumption (%) |
| :--- | :--- | :--- |
| 22 | Services | 1.8 |
| 22 | Durables | 0.3 |
| 22 | Semi-durables | 0.4 |
| 22 | Non-durables | -0.5 |
| 22 | Total | 1.7 |
| 23 | Services | 1.9 |
| 23 | Durables | 0.5 |
| 23 | Semi-durables | 0.6 |
| 23 | Non-durables | -0.7 |
| 23 | Total | 2.5 |
| 24 | Services | -1.8 |
| 24 | Durables | -0.4 |
| 24 | Semi-durables | -0.6 |
| 24 | Non-durables | -0.6 |
| 24 | Total | -1.9 |
| 2025 | Services | 0.1 |
| 2025 | Durables | 0.5 |
| 2025 | Semi-durables | 0.6 |
| 2025 | Non-durables | -0.3 |
| 2025 | Total | 1.1 |
| 2026 | Services | 0.6 |
| 2026 | Durables | 0.4 |
| 2026 | Semi-durables | 0.7 |
| 2026 | Non-durables | -0.3 |
| 2026 | Total | 1.0 |
</details>

Source: CAO

Figure 10: Inbound consumption fell by $0.6\% \mathrm{q} / \mathrm{q}$   
![](images/04fecd70057079908ab8215445d94449ec2fa8b10fc6e9c0458de7f69a9c77a2.jpg)

<details>
<summary>line</summary>

| Year | Direct purchase in the domestic market by non-residential households (JPY trillion, saar) |
| ---- | ------------------------------------------------------------------------ |
| 10   | 1.0                                                                      |
| 11   | 0.5                                                                      |
| 12   | 1.0                                                                      |
| 13   | 1.5                                                                      |
| 14   | 2.0                                                                      |
| 15   | 2.5                                                                      |
| 16   | 3.0                                                                      |
| 17   | 3.5                                                                      |
| 18   | 4.0                                                                      |
| 19   | 4.5                                                                      |
| 20   | 0.5                                                                      |
| 21   | 0.5                                                                      |
| 22   | 0.5                                                                      |
| 23   | 3.5                                                                      |
| 24   | 7.0                                                                      |
| 25   | 8.0                                                                      |
| 26   | 8.5                                                                      |
</details>

Source: CAO

Figure 11: Contribution of inbound consumption to real GDP growth (y/y)   
![](images/c9eadf62fcfc3d57c3cf3d77c24f2ee4ac9a0da7b1a0deb68bb92085906d73b3.jpg)

<details>
<summary>bar</summary>

| Year | Inbound consumption (contribution to real GDP) (%y/y) |
|------|--------------------------------------------------|
| 2022 | -                                                |
| 2023 | 0.7                                              |
| 2024 | 0.4                                              |
| 2025 | 0.1                                              |
</details>

Source: CAO

Figure 12: Residential investment showed an rebound but not back to the previous level   
![](images/73e647c3e5fa5676ae7037b9671a600007610d79205b0d1324950c2710c2646e.jpg)

<details>
<summary>line</summary>

| Year | %q/q (%) | Residential investment (%) |
|------|----------|-----------------------------|
| 10   | 21       | 0                           |
| 11   | 23       | 0                           |
| 12   | 24       | 0                           |
| 13   | 25       | 0                           |
| 14   | 27       | 4                           |
| 15   | 24       | 0                           |
| 16   | 25       | 0                           |
| 17   | 25       | 0                           |
| 18   | 24       | 0                           |
| 19   | 25       | 0                           |
| 20   | 24       | 0                           |
| 21   | 23       | -4                          |
| 22   | 23       | -4                          |
| 23   | 23       | -4                          |
| 24   | 23       | -4                          |
| 25   | 22       | -8                          |
| 26   | 22       | -8                          |
</details>

Source: CAO

Figure 13: Capex rose $0.3\% \mathrm{q} / \mathrm{q}$ , steadily rising   
![](images/b3aaaf4e136a90378fc9cbd6ef06ad2b3f4fb7c29c64b433d670e5894fd6d3e0.jpg)

<details>
<summary>bar_line</summary>

| Year | Capex (LHS) | %q/q |
|------|-------------|------|
| 10   | 76          | -4   |
| 11   | 78          | -3   |
| 12   | 82          | -2   |
| 13   | 85          | 0    |
| 14   | 90          | 1    |
| 15   | 95          | 2    |
| 16   | 98          | 3    |
| 17   | 100         | 4    |
| 18   | 102         | 5    |
| 19   | 105         | 6    |
| 20   | 95          | -8   |
| 21   | 100         | -6   |
| 22   | 102         | -4   |
| 23   | 104         | -2   |
| 24   | 106         | 0    |
| 25   | 108         | 2    |
| 26   | 110         | 4    |
</details>

Source: CAO

Figure 14: Both public consumption and investment rose $0.4\% \mathrm{q / q}$ and $-0.2\%$ respectively   
![](images/6b526dce819f16857baff1a2d1d8bc6814d81a6d4c126ba0471ba8aded69c1b2.jpg)

<details>
<summary>line</summary>

| Year | Public consumption (LHS) | Public investment (RHS) |
|------|--------------------------|--------------------------|
| 10   | 95                       | 117                      |
| 11   | 98                       | 105                      |
| 12   | 100                      | 95                       |
| 13   | 102                      | 105                      |
| 14   | 104                      | 115                      |
| 15   | 106                      | 105                      |
| 16   | 107                      | 108                      |
| 17   | 108                      | 107                      |
| 18   | 109                      | 109                      |
| 19   | 110                      | 112                      |
| 20   | 112                      | 115                      |
| 21   | 115                      | 122                      |
| 22   | 118                      | 105                      |
| 23   | 120                      | 108                      |
| 24   | 121                      | 105                      |
| 25   | 122                      | 103                      |
| 26   | 123                      | 99                       |
</details>

Source: CAO

Figure 15: Exports of goods rebounded supported by auto related and capital goods (2.2%q/q vs 0.4% in services)   
![](images/b732117937b2da54f9f84299605b8b1ebcf4a364d3228d21c5d524c74f0c4835.jpg)

<details>
<summary>line</summary>

| Year | Export of goods (LHS) | Export of services (RHS) |
|------|------------------------|--------------------------|
| 10   | 60                     | 10                       |
| 11   | 65                     | 12                       |
| 12   | 60                     | 14                       |
| 13   | 65                     | 16                       |
| 14   | 70                     | 18                       |
| 15   | 75                     | 20                       |
| 16   | 70                     | 22                       |
| 17   | 75                     | 24                       |
| 18   | 78                     | 26                       |
| 19   | 75                     | 28                       |
| 20   | 60                     | 16                       |
| 21   | 75                     | 20                       |
| 22   | 80                     | 24                       |
| 23   | 78                     | 26                       |
| 24  

[中间内容因长度限制已省略]

i) to the maximum extent permitted by law (a) indemnify UBS and its associates or related entities (and their respective Directors, officers, agents and Advisors) (each a 'Relevant Person') for any loss, damage, liability or claim any of them may incur or suffer as a result of, or in connection with, your unauthorised reliance on this publication or material and (b) waive any rights or remedies you may have against any Relevant Person for (or in respect of) any loss, damage, liability or claim you may incur or suffer as a result of, or in connection with, your unauthorised reliance on this publication or material. Korea: Distributed in Korea by UBS Pte. Ltd., Seoul Branch. This report may have been edited or contributed to from time to time by affiliates of UBS Pte. Ltd., Seoul Branch. This material is intended for professional/institutional clients only and not for distribution to any retail clients. Malaysia: This material is authorized to be distributed in Malaysia by UBS Malaysia Sdn. Bhd (Capital Markets Services License No.: CMSL/A0063/2007). This material is intended for professional/institutional clients only and not for distribution to any retail clients. India: Distributed by UBS India Private Ltd. (Corporate Identity Number U67120MH1996PTC097299) 2/F, 3 North Avenue, Maker Maxity, Bandra Kurla Complex, Bandra (East), Mumbai (India) 400051. Phone: +912261556000. It provides brokerage services bearing SEBI Registration Number: INZ000259830; Merchant Banking services bearing SEBI Registration Number: INM000013101; and Research Analyst services bearing SEBI Registration Number: INH000001204. Name of Compliance Officer Mr. Parameshwaran Shivaramakrishnan, Phone: +912261556151, Email: parameshwaran.s@ubs.com, Name of Grievance Officer Parameshwaran Shivaramakrishnan, Phone: +912261556151, Email: ol-ubs-sec-compliance@ubs.com Registration granted by SEBI, and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. UBS may have debt holdings or positions in the subject Indian company/companies. UBS may have financial interests (e.g. loan/derivative products, rights to or interests in investments, etc.) in the subject Indian company/companies from time to time. Within the past 12 months, UBS may have received compensation for non-investment banking securities-related services and/or non-securities services from the subject Indian company/companies. The subject company/companies may have been a client/clients of UBS during the 12 months preceding the date of distribution of the research report with respect to investment banking and/or non-investment banking securities-related services and/or non-securities services. With regard to information on associates, please refer to the Annual Report at: https://www.ubs.com/global/en/about\_ubs/investor\_relations/annualreporting.html The Research Annual Compliance Report for UBS India Private Limited is available on www.ubs.com/ubssi under Research tab. Taiwan: Except as otherwise specified herein, this material may not be distributed in Taiwan. Information and material on securities/instruments that are traded in a Taiwan organized exchange is deemed to be issued and distributed by UBS Pte. LTD., Taipei Branch, which is licensed and regulated by Taiwan Financial Supervisory Commission. Save for securities/instruments that are traded in a Taiwan organized exchange, this material should not constitute "recommendation" to clients or recipients in Taiwan for the covered companies or any companies mentioned in this document. No portion of the document may be reproduced or quoted by the press or any other person without authorisation from UBS. Indonesia: This report is being distributed by PT UBS Sekuritas Indonesia and is delivered by its licensed employee(s), including marketing/sales person, to its client. PT UBS Sekuritas Indonesia, having its registered office at Sequis Tower Level 22 unit 22-1,Jl.Jend. Sudirman, kav.71, SCBD lot 11B, Jakarta 12190. Indonesia, is a subsidiary company of UBS AG and licensed under Capital Market Law no. 8 year 1995, a holder of broker-dealer and underwriter licenses issued by the Capital Market and Financial Institution Supervisory Agency (now Otoritas Jasa Keuangan/OJK). PT UBS Sekuritas Indonesia is also a member of Indonesia Stock Exchange and supervised by Otoritas Jasa Keuangan (OJK). Neither this report nor any copy hereof may be distributed in Indonesia or to any Indonesian citizens except in compliance with applicable Indonesian capital market laws and regulations. This report is not an offer of securities in Indonesia and may not be distributed within the territory of the Republic of Indonesia or to Indonesian citizens in circumstance which constitutes an offering within the meaning of Indonesian capital market laws and regulations.

The disclosures contained in research documents produced by UBS AG, London Branch or UBS Europe SE shall be governed by and construed in accordance with English law.

UBS specifically prohibits the redistribution of this document in whole or in part without the written permission of UBS and in any event UBS accepts no liability whatsoever for any redistribution of this document or its contents or the actions of third parties in this respect. Images may depict objects or elements that are protected by third party copyright, trademarks and other intellectual property rights. © UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/8369aa5be91e72ace9b1e468b85971d3c272586071a2b8de9fc86d12c44c8d71.jpg)
"""
