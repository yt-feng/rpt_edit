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
# GC Telecom: Telcos' AI token plan released; 5G BTS deployment YoY/MoM increased in Apr

5G base station deployment in Apr 2026 was 51k units, up 16% YoY, leading to an accumulated base station deployment of 5.0mn units as of April 2026. Newly added 5G base stations stood at 171k units in 4M26, tracking at 32% of our estimate for new 5G base stations in 2026E (vs. 4M tracking at 32% of new 5G base stations in 2025). Base station production was down 19% YoY in April 2026, and export volumes maintained strong momentum: 1) China's telecom service industry revenue was up 2% YoY in April to Rmb155bn (per MIIT); 2) new 5G base station deployment decreased YoY in Apr 2026 to 51k units, vs. 44k units added in Apr 2025; and 3) 5G subscriber growth accelerated, to +8mn in Apr 2026, vs. +19mn in Apr 2025. Export values of BTS, PCB, CCL, and fiber cables all saw positive YoY growth in Apr 2026, indicating strong overseas demand. Read more: Review of China telcos' 10 key metrics.

# China Telcos AI token plan

We see China Telcos recently launched AI token plan for both ToC (Consumer) and ToB (Business) clients, and charges clients by monthly/ quarterly subscription fee or by clients' token usage. We are positive on the new AI token plan to drive clients' ARPU spending, and see China telcos' advantages on one-stop solution and safety. We expect the expansion of more AI applications/ features to support AI token user adoption.

China Mobile: Rmb1 per 400k tokens, or token package priced at Rmb5.99 to Rmb24.99   
China Unicom: Released coding plan/ token plan for users with discount, personal version starting from Rmb15 per month, and enterprise version starting from Rmb198 per month   
China Telecom: ToC user at Rmb9.9 to Rmb49.9 per month, and ToB user at Rmb39.9 to Rmb299.9 per month

# Allen Chang

+852-2978-2930

allen.k.chang@gs.com

GS (Asia) L.L.C.

# Verena Jeng

+852-2978-1681 | verena.jeng@gs.com

GS (Asia) L.L.C.

# Ting Song

+852-2978-6466 | ting.song@gs.com

GS (Asia) L.L.C.

Exhibit 1: China Telecom AI token plan 

<table><tr><td colspan="3">Enterprise version</td></tr><tr><td>Package</td><td>Fee (Rmb/ month)</td><td>Token usage/ month</td></tr><tr><td>Basic</td><td>39.9</td><td>15m</td></tr><tr><td>Professional</td><td>159.9</td><td>70m</td></tr><tr><td>Flagship</td><td>299.9</td><td>150m</td></tr><tr><td colspan="3">Personal version</td></tr><tr><td>Package</td><td>Fee (Rmb/ month)</td><td>Token usage/ month</td></tr><tr><td>Lite</td><td>9.9</td><td>10m</td></tr><tr><td>Standard</td><td>29.9</td><td>40m</td></tr><tr><td>Premium</td><td>49.9</td><td>80m</td></tr></table>

Source: Company data

# Key data points in Apr 2026

5G base station deployment increased YoY: Apr 2026 5G base station deployment was 51k units, vs. 44k in Apr 2025. In 4M26, newly added 5G base station stood at 171k units, vs. 188k units in 4M25, tracking at $32\%$ of our estimate for new 5G base stations in 2026E (vs. 4M tracking at $32\%$ of new 5G base stations in 2025). For macro 5G base stations, we expect to see 540k new 5G base stations in 2026E (vs. 588k new 5G base stations in 2025, per MIIT). China's telecom base station production was down $19\%$ YoY in Mar 2026 (vs. $+71\%$ YoY in Mar 2026).

\* Note that the MIIT changed its counting method for indoor 5G base stations from the number of Base Band Units (BBU) to the number of Remote Radio Units (RRU), leading to a much higher number from March 2023 to date compared with the same period in 2022.

Exhibit 2: We expect 540k 5G base stations to be added in 2026E 

<table><tr><td>5G macro base stations in China</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td></tr><tr><td>Volume estimates</td><td>150,000</td><td>620,000</td><td>654,000</td><td>887,000</td><td>1,065,000</td><td>874,000</td><td>588,000</td><td>540,000</td><td>500,000</td></tr><tr><td>5G BTS on 2.1G/ 2.6G/ 3.5G/ 4.9G</td><td>150,000</td><td>620,000</td><td>454,000</td><td>437,000</td><td>565,000</td><td>574,000</td><td>338,000</td><td>340,000</td><td>350,000</td></tr><tr><td>5G BTS on 700MHz/ 900MHz</td><td></td><td></td><td>200,000</td><td>450,000</td><td>500,000</td><td>300,000</td><td>250,000</td><td>200,000</td><td>150,000</td></tr><tr><td>Growth rate</td><td></td><td>313%</td><td>5%</td><td>36%</td><td>20%</td><td>-18%</td><td>-33%</td><td>-8%</td><td>-7%</td></tr></table>

Source: Company data, MIIT, GS Global Investment Research

# Base stations, fiber cable, CCL, and PCB growth mixed

For fiber cables, the key indicator is production volume, which includes shipments both locally and overseas. Apr 2026 fiber cable production was down $16\%$ YoY, and the overseas export volumes were up $9\%$ YoY in Apr 2026 (vs. $+20\%$ YoY in Mar 2026 vs. $+71\%$ YoY in Apr 2025).

Fiber cable export volumes were up 9% YoY in Apr 2026, and export value (in US dollar terms) increased by 287% YoY in Apr 2026. The export volume of 4,466 tons in Apr 2026 (vs. 3,224 tons in Mar 2026) represents an increase in overseas demand with better seasonality and client pull-in (Feb / Mar export volumes up 64% / 20% YoY).   
Fiber cable production was down by 16% YoY in Apr 2026 (vs. -6% YoY in Mar 2026).   
■ Fiber preform (a key raw material for fiber cables) import volumes were up 97%

YoY (vs. -7% MoM from Mar 2026) to 33 tons in Apr 2026 with a higher ASP (+57% MoM).

- BTS export volumes decreased 9% YoY in Apr 2026, and the export value was up 3% YoY; export volumes were up 8% MoM, and export value was up by 4% MoM. ASP was down by 4% MoM to US\$6,707, normalizing in Mar/ Apr after strong Feb.   
China CCL (copper clad laminate) export prices were up by 67% YoY in Apr 2026 (or +9% MoM). PCB export value increased 29% YoY; PCB net export value (exports minus imports) increased by 40% YoY in Apr 2026, compared to 55% in Mar 2026, representing the continued YoY growth momentum.   
■ 5G subscribers reached 1.3bn: +8mn in Apr 2026 vs. +13mn in Apr 2025, per MIIT.   
Taiwan telecom aggregate revenue was up 6% YoY to NT\$46bn in Apr 2026 (aggregate revenue of Chunghwa Telecom, Far EastTone, and Taiwan Mobile).   
Accumulated 5G users: The accumulated 5G users of China Mobile/ China Unicom reached 668m/ 314m units by the end of 1Q26, representing a 5G user penetration rate of $66\% / 71\%$ .

Unless otherwise noted, all production data is sourced from NBS, and trade data is sourced from China's General Administration of Customs.

Exhibit 3: Monthly new 5G base station additions: Apr 2026 deployment at 51k units, or $16\%$ YoY   
![](images/b9e6b34d79c2b234caaf5ec672bbfc2c16f43aa96c232743a33bab18c1b5bf5e.jpg)

<details>
<summary>bar</summary>

| Month | 5G BTS (k units) |
|---|---|
| Jan-20 | 15 |
| Feb-20 | 20 |
| Mar-20 | 35 |
| Apr-20 | 45 |
| May-20 | 85 |
| Jun-20 | 140 |
| Jul-20 | 140 |
| Aug-20 | 20 |
| Sep-20 | 25 |
| Oct-20 | 25 |
| Nov-20 | 25 |
| Dec-20 | 15 |
| Jan-21 | 20 |
| Feb-21 | 35 |
| Mar-21 | 45 |
| Apr-21 | 50 |
| May-21 | 55 |
| Jun-21 | 60 |
| Jul-21 | 70 |
| Aug-21 | 80 |
| Sep-21 | 125 |
| Oct-21 | 130 |
| Nov-21 | 70 |
| Dec-21 | 65 |
| Jan-Feb 22 | 80 |
| Feb-Feb 22 | 55 |
| Mar-Feb 22 | 85 |
| Apr-Feb 22 | 155 |
| May-Feb 22 | 110 |
| Jun-Feb 22 | 130 |
| Jul-Feb 22 | 115 |
| Aug-Feb 22 | 35 |
| Sep-Feb 22 | 40 |
| Oct-Feb 22 | 70 |
| Nov-Feb 22 | 90 |
| Dec-Feb 22 | 265 |
| Jan-Mar 23 | 85 |
| Feb-Mar 23 | 110 |
| Mar-Mar 23 | 95 |
| Apr-Mar 23 | 115 |
| May-Mar 23 | 80 |
| Jun-Mar 23 | 75 |
| Jul-Mar 23 | 60 |
| Aug-Mar 23 | 45 |
| Sep-Mar 23 | 30 |
| Oct-Mar 23 | 65 |
| Nov-Mar 23 | 95 |
| Dec-Mar 23 | 135 |
| Jan-Dec 24 | 140 |
| Feb-Dec 24 | 100 |
| Mar-Dec 24 | 90 |
| Apr-Dec 24 | 85 |
| May-Dec 24 | 75 |
| Jun-Dec 24 | 70 |
| Jul-Dec 24 | 60 |
| Aug-Dec 24 | 50 |
| Sep-Dec 24 | 45 |
| Oct-Dec 24 | 55 |
| Nov-Dec 24 | 65 |
| Dec-Dec 24 | 75 |
| Jan-Jan-25 | 45 |
| Feb-Jan-25 | 60 |
| Mar-Jan-25 | 70 |
| Apr-Jan-25 | 65 |
| May-Jan-25 | 50 |
| Jun-Jan-25 | 60 |
| Jul-Jan-25 | 50 |
| Aug-Jan-25 | 60 |
| Sep-Jan-25 | 70 |
| Oct-Jan-25 | 65 |
| Nov-Jan-25 | 75 |
| Dec-Jan-25 | 60 |
| Jan-Mar-26 | 70 |
| Feb-Mar-26 | 65 |
| Mar-Mar-26 | 50 |
Apr-Mar-26 |
</details>

Source: MIIT

Exhibit 4: 5G base station deployment by quarter: 1Q26 deployment decreased QoQ   
![](images/6e83cd2c1ebcfe7dce77dad559e3cb58a526b78114d8c017ae1e64445d53023b.jpg)

<details>
<summary>bar</summary>

| Quarter | Units (k units) |
|---|---|
| 1Q20 | 68 |
| 2Q20 | 213 |
| 3Q20 | 300 |
| 4Q20 | 59 |
| 1Q21 | 48 |
| 2Q21 | 141 |
| 3Q21 | 197 |
| 4Q21 | 264 |
| 1Q22 | 133 |
| 2Q22 | 293 |
| 3Q22 | 367 |
| 4Q22 | 93 |
| 1Q23 | 360 |
| 2Q23 | 290 |
| 3Q23 | 251 |
| 4Q23 | 187 |
| 1Q24 | 270 |
| 2Q24 | 270 |
| 3Q24 | 173 |
| 4Q24 | 161 |
| 1Q25 | 143 |
| 2Q25 | 153 |
| 3Q25 | 156 |
| 4Q25 | 133 |
| 1Q26 | 119 |
</details>

Source: MIIT

Exhibit 5: Base station production was $-19\%$ YoY in Apr 2026   
![](images/a2c55962f475836dc7de8b5a4abbf42eaff019db15b308e14a2940f9fcd50bba.jpg)  
Source: NBS

Exhibit 6: The number of newly installed 5G base stations in China was up to 51k units in Apr 2026 from 49k units in Mar 2026   
![](images/1239dd53c583e933afa2de501503c26b03c6ab8bbe986e07b23851d40d909bb2.jpg)

<details>
<summary>line</summary>

| Date       | Value (k units) |
| ---------- | --------------- |
| Apr-26     | 51              |
</details>

\* From Mar 23, 5G indoor base station numbers are estimated based on the number of Remote Radio Units (vs. counting based on the number of Base Band Units before).   
Source: MIIT

Exhibit 7: Apr 2026 base station export volumes were -9.1% YoY   
![](images/b692c292b13171747a4ce05d99a3216350ad500370eabe144d633fc8500ee8f6.jpg)

<details>
<summary>bar</summary>

| Date | Units |
|---|---|
| Jan-17 | 80000 |
| Apr-17 | 140000 |
| Jul-17 | 120000 |
| Oct-17 | 115000 |
| Jan-18 | 105000 |
| Apr-18 | 85000 |
| Jul-18 | 45000 |
| Oct-18 | 65000 |
| Jan-19 | 65000 |
| Apr-19 | 55000 |
| Jul-19 | 35000 |
| Oct-19 | 55000 |
| Jan-20 | 35000 |
| Apr-20 | 60000 |
| Jul-20 | 35000 |
| Oct-20 | 25000 |
| Jan-21 | 45000 |
| Apr-21 | 35000 |
| Jul-21 | 35000 |
| Oct-21 | 45000 |
| Jan-22 | 55000 |
| Apr-22 | 45000 |
| Jul-22 | 45000 |
| Oct-22 | 55000 |
| Jan-23 | 35000 |
| Apr-23 | 45000 |
| Jul-23 | 35000 |
| Oct-23 | 35000 |
| Jan-24 | 25000 |
| Apr-24 | 35000 |
| Jul-24 | 25000 |
| Oct-24 | 35000 |
| Jan-25 | 35000 |
| Apr-25 | 135000 |
| Jul-25 | 45000 |
| Oct-25 | 55000 |
| Jan-26 | 35000 |
| Apr-26 | 35000 |
</details>

Source: China Customs

Exhibit 8: Fiber cable production was down 16% YoY in Apr 2026   
![](images/310f8a8c22e253285d0879a49e3d8a932953a29f0fc9061aed4090fd0519f429.jpg)

<details>
<summary>bar</summary>

| Month | Value (mn fiber km) |
|---|---|
| Apr-18 | 25 |
| May-18 | 34 |
| Jun-18 | 27 |
| Jul-18 | 25 |
| Aug-18 | 23 |
| Sep-18 | 28 |
| Oct-18 | 23 |
| Nov-18 | 28 |
| Dec-18 | 34 |
| Jan-19 | 21 |
| Feb-19 | 19 |
| Mar-19 | 28 |
| Apr-19 | 24 |
| May-19 | 26 |
| Jun-19 | 27 |
| Jul-19 | 25 |
| Aug-19 | 26 |
| Sep-19 | 27 |
| Oct-19 | 25 |
| Nov-19 | 27 |
| Dec-19 | 24 |
| Jan-20 | 26 |
| Feb-20 | 23 |
| Mar-20 | 27 |
| Apr-20 | 25 |
| May-20 | 26 |
| Jun-20 | 24 |
| Jul-20 | 23 |
| Aug-20 | 29 |
| Sep-20 | 28 |
| Oct-20 | 30 |
| Nov-20 | 37 |
| Dec-20 | 26 |
| Jan-21 | 25 |
| Feb-21 | 24 |
| Mar-21 | 26 |
| Apr-21 | 27 |
| May-21 | 29 |
| Jun-21 | 30 |
| Jul-21 | 25 |
| Aug-21 | 30 |
| Sep-21 | 31 |
| Oct-21 | 30 |
| Nov-21 | 47 |
| Dec-21 | 30 |
| Jan-22 | 26 |
| Feb-22 | 33 |
| Mar-22 | 33 |
| Apr-22 | 34 |
| May-22 | 33 |
| Jun-22 | 30 |
| Jul-22 | 33 |
| Aug-22 | 33 |
| Sep-22 | 30 |
| Oct-22 | 43 |
| Nov-22 | 24 |
| Dec-22 | 36 |
| Jan-23 | 30 |
| Feb-23 | 30 |
| Mar-23 | 30 |
| Apr-23 | 27 |
| May-23 | 26 |
| Jun-23 | 25 |
| Jul-23 | 27 |
| Aug-23 | 26 |
| Sep-23 | 25 |
| Oct-23 | 27 |
| Nov-23 | 24 |
| Dec-23 | 23 |
| Jan-24 | 24 |
| Feb-24 | 25 |
| Mar-24 | 23 |
| Apr-24 | 25 |
| May-24 | 24 |
| Jun-24 | 25 |
| Jul-24 | 26 |
| Aug-24 | 24 |
| Sep-24 | 25 |
| Oct-24 | 34 |
| Nov-24 | 24 |
| Dec-24 | 34 |
| Jan-25 | 24 |
| Feb-25 | 25 |
| Mar-25 | 34 |
| Apr-25 | 18 |
| May-25 | 19 |
| Jun-25 | 19 |
| Jul-25 | 19 |
| Aug-25 | 19 |
| Sep-25 | 19 |
| Oct-25 | 19 |
| Nov-25 | 19 |
| Dec-25 | 19 |
| Jan-26 | 19 |
| Feb-26 | 19 |
| Mar-26 | 19 |
| Apr-26 | 18 |
</details>

Source: NBS

Exhibit 9: Fiber preform import volume decreased $7\%$ MoM to 33 tons in Apr 2026   
![](images/12a8926101ffe54ef80e723d48cfc8650ec6715b1fd61cb73f6b2a8b27e0d620.jpg)

<details>
<summary>bar_line</summary>

| Date | Import quantity (kg) | Import ASP (RHS) (US$/kg) |
|---|---|---|
| 2017-01 | 175,000 | 150 |
| 2017-06 | 200,000 | 160 |
| 2017-11 | 150,000 | 180 |
| 2018-04 | 165,000 | 200 |
| 2018-09 | 135,000 | 220 |
| 2019-02 | 125,000 | 240 |
| 2019-07 | 105,000 | 260 |
| 2019-12 | 130,000 | 280 |
| 2020-05 | 85,000 | 300 |
| 2020-10 | 75,000 | 320 |
| 2021-03 | 35,000 | 340 |
| 2021-08 | 35,000 | 360 |
| 2022-01 | 35,000 | 380 |
| 2022-06 | 35,000 | 400 |
| 2022-11 | 35,000 | 380 |
| 2023-04 | 35,000 | 360 |
| 2023-09 | 35,000 | 340 |
| 2024-02 | 35,000 | 320 |
| 2024-07 | 35,000 | 340 |
| 2024-12 | 35,000 | 360 |
| 2025-05 | 35,000 | 380 |
| 2025-10 | 35,000 | 400 |
| 2026-03 | 35,000 | 420 |
</details>

Source: China Customs

Exhibit 10: Fiber cable export volumes were up $9\%$ YoY to 4,466 tons in Apr 2026   
![](images/a8b2e5d2ad24cb7fc245ec5691e701b52d587fb8f939145891408f9fc34067bf.jpg)

<details>
<summary>bar_line</summary>

| Date | Export volume (LHS) (Kg) | Export value (US$ mn) |
|---|---|---|
| Jan-18 | 100000 | 30 |
| May-18 | 300000 | 45 |
| Sep-18 | 400000 | 55 |
| Jan-19 | 350000 | 50 |
| May-19 | 300000 | 45 |
| Sep-19 | 250000 | 40 |
| Jan-20 | 200000 | 35 |
| May-20 | 250000 | 35 |
| Sep-20 | 300000 | 35 |
| Jan-21 | 400000 | 45 |
| May-21 | 600000 | 55 |
| Sep-21 | 700000 | 65 |
| Jan-22 | 1,100,000 | 75 |
| May-22 | 1,800,000 | 95 |
| Sep-22 | 2,100,000 | 95 |
| Jan-23 | 2,300,000 | 85 |
| May-23 | 2,100,000 | 75 |
| Sep-23 | 1,900,000 | 65 |
| Jan-24 | 1,600,000 | 65 |
| May-24 | 2,500,000 | 75 |
| Sep-24 | 3,100,000 | 85 |
| Jan-25 | 4,100,000 | 115 |
| May-25 | 4,300,000 | 135 |
| Sep-25 | 4,400,000 | 145 |
| Jan-26 | 4,600,000 | 345 |
Export value went up MoM in Apr 266
Export value went up MoM in Apr 26
</details>

Source: China Customs

Exhibit 11: CCL export ASP increased $67\%$ YoY or increased $9\%$ MoM in Apr 2026   
![](images/4ae0a097e28545e5e44fd8d6679342b85db336e4c654a362ca3a7306c7c0a0b0.jpg)

<details>
<summary>line</summary>

| Date    | Value (US$/kg) |
|---------|----------------|
| Jan-26  | 12             |
</details>

Source: China Customs   
PCB net exports were $+47\%$ in 2025

Exhibit 12: China's PCB net export volume is expected to rise as domestic PCB production capacity increases

![](images/e0c07a6f08c0f33c9884f2094dbc33ce090accfecb08a310534bfb19ebe7f6e0.jpg)

<details>
<summary>bar</summary>

| Year | Export value (US$ mn) | Import value (US$ mn) | Net export (US$ mn) |
|---|---|---|---|
| 2009 | 8500 | 9000 | -1000 |
| 2010 | 11500 | 12000 | -1500 |
| 2011 | 12500 | 14000 | -1500 |
| 2012 | 13500 | 14500 | -1500 |
| 2013 | 13500 | 13500 | -1000 |
| 2014 | 13500 | 13500 | -500 |
| 2015 | 14500 | 12500 | 2500 |
| 2016 | 13000 | 10500 | 3000 |
| 2017 | 14000 | 11500 | 2500 |
| 2018 | 15500 | 12500 | 3500 |
| 2019 | 14500 | 11500 | 3500 |
| 2020 | 15000 | 11000 | 4500 |
| 2021 | 21000 | 12500 | 8500 |
| 2022 | 20000 | 11500 | 9500 |
| 2023 | 17500 | 8500 | 9500 |
| 2024 | 20500 | 7500 | 12500 |
| 2025 | 26000 | 7500 | 18500 |
</details>

Source: China Customs

Exhibit 13: Major TW telecom companies' aggregate revenue was $+6\%$ YoY in Apr 2026 (vs. $+6\%$ YoY in Mar 2026)   
![](images/97c89e6eb6aaf7d334b64b9e36de49945fb5c90b7164f290e59c263dc95c573d.jpg)

<details>
<summary>bar_line</summary>

| Month    | TW telecom company aggregate revenue (NT$ bn) | YoY (RHS) |
|----------|-----------------------------------------------|-----------|
| Jan-18   | 35                                            | -         |
| May-18   | 34                                            | -         |
| Sep-18   | 33                                            | -         |
| Jan-19   | 32                                            | -         |
| May-19   | 31                                            | -         |
| Sep-19   | 30                                            | -         |
| Jan-20   | 29                                            | -         |
| May-20   | 28                                            | -         |
| Sep-20   | 27                                            | -         |
| Jan-21   | 26                                            | -         |
| May-21   | 25                                            | -         |
| Sep-21   | 24                                            | -         |
| Jan-22   | 23                                            | -         |
| May-22   | 22                                            | -         |
| Sep-22   | 21                                            | -         |
| Jan-23   | 20                                            | -         |
| May-23   | 19                                            | -         |
| Sep-23   | 18                                            | -         |
| Jan-24   | 17                                            | -         |
| May-24   | 16                                            | -         |
| Sep-24   | 15                                            | -         |
| Jan-25   | 14                                            | -         |
| May-25   | 13                                            | -         |
| Sep-25   | 12                                            | -         |
| Jan-26   | 11                                            | -         |
</details>

Aggregate revenue of Chunghwa Telecom, Far East Tone, and Taiwan Mobile

Exhibit 14: China Mobile's 5G user penetration rate reached $6\%$ by the end of 1Q26   
![](images/f988cb95b948f317e1c1a64a1e35e1fc85673541b0b23857011d73ceb8152ec8.jpg)

<details>
<summary>bar_line</summary>

| Quarter | Accumulated 5G users (mn users) | 5G user penetration rate (RHS) (%) |
|---|---|---|
| 1Q20 | 30 | 8 |
| 2Q20 | 70 | 10 |
| 3Q20 | 110 | 14 |
| 4Q20 | 170 | 26 |
| 1Q21 | 90 | 12 |
| 2Q21 | 120 | 16 |
| 3Q21 | 160 | 20 |
| 4Q21 | 210 | 24 |
| 1Q22 | 240 | 28 |
| 2Q22 | 270 | 32 |
| 3Q22 | 300 | 36 |
| 4Q22 | 330 | 40 |
| 1Q23 | 380 | 44 |
| 2Q23 | 410 | 48 |
| 3Q23 | 440 | 52 |
| 4Q23 | 470 | 56 |
| 1Q24 | 500 | 60 |
| 2Q24 | 530 | 64 |
| 3Q24 | 550 | 66 |
| 4Q24 | 570 | 68 |
| 1Q25 | 590 | 70 |
| 2Q25 | 610 | 72 |
| 3Q25 | 630 | 74 |
| 4Q25 | 650 | 76 |
| end of 1Q26 | - |

[中间内容因长度限制已省略]

rm impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
