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
# China Data Centers: Scaling the AI Infrastructure

Initiate Range Intelligent at Buy, Athub at Neutral

May 2026

Timothy Zhao

GS (Asia) L.L.C.

+852 2978-2673

timothy.zhao@gs.com

# China data center operators toward higher-density infrastructure and frontier markets to capture growth opportunities driven by AI

China hyperscalers' spending on AI infrastructure remains well below US peers   
![](images/8163d533c05d045d91222cb66545ea3fbf3cf21340806f4ed8cd89750bcf121b.jpg)

<details>
<summary>bar_line</summary>

| Year | China: ByteDance, Alibaba, Tencent, Baidu and Kingsoft (Capex to cash flow) (US$ bn) | US: Amazon, Microsoft, Google, Meta and Oracle (%) |
|---|---|---|
| 2022 | 9 | 54 |
| 2023 | 18 | 41 |
| 2024 | 37 | 53 |
| 2025E | 56 | 73 |
| 2026E | 75 | 89 |
| 2027E | 86 | 85 |
| 2028E | 94 | 77 |
Capex to cash flow (%) | 15 | 15 |
| Capex to cash flow (%) | 37 | 63 |
| Capex to cash flow (%) | 63 | 63 |
| Capex to cash flow (%) | 54 | 49 |
| Capex to cash flow (%) | 49 | 54 |
| Hyperscaler capex (US$ bn) | 156 | 156 |
| Hyperscaler capex (US$ bn) | 254 | 254 |
| Hyperscaler capex (US$ bn) | 443 | 443 |
| Hyperscaler capex (US$ bn) | 722 | 722 |
| Hyperscaler capex (US$ bn) | 828 | 828 |
| Hyperscaler capex (US$ bn) | 909 | 909 |
The chart displays two data series: one for Capex to cash flow (%) and one for Hyperscaler capex (US$ bn). The values for the Capex to cash flow (%) are annotated above the bars. The US market share data is also shown for comparison.
</details>

We see Range and GDS lead in terms of total data center capacity and pipeline capacity   
![](images/9cd327877e4a7c576198573104ff162b4467dc2ccf9653ea966e92dd1a890f9d.jpg)

<details>
<summary>bar_stacked</summary>

| Category | Live (GW) | Under construction/in pipeline (GW) |
|---|---|---|
| Range | 0.7 | 5.5 |
| GDS | 1.5 | 3.9 |
| VNET | 1.1 | 1.3 |
| Sinnet | 0.4 | 0.4 |
| Athub | 0.4 | 0.0 |
</details>

We forecast China data center demand to grow at $20\%$ CAGR in 2025-28E   
![](images/6a780d6b052dae23b98f05e3a92b8768f61441d6a6437cd33deca6df3840750f.jpg)

<details>
<summary>bar_line</summary>

| Year | China Data Center Live Capacity (GW) | China Data Center Demand (GW) | Utilization rate (RHS) (%) |
| :--- | :--- | :--- | :--- |
| 2017 | 4 | 2 | 38 |
| 2018 | 6 | 3 | 34 |
| 2019 | 8 | 4 | 38 |
| 2020 | 10 | 5 | 38 |
| 2021 | 13 | 7 | 35 |
| 2022 | 16 | 8 | 36 |
| 2023 | 20 | 10 | 37 |
| 2024 | 23 | 13 | 40 |
| 2025 | 28 | 16 | 41 |
| 2026E | 34 | 19 | 41 |
| 2027E | 38 | 23 | 43 |
| 2028E | 43 | 27 | 45 |
The chart includes a line graph on the right showing the utilization rate trend. The bar values represent China Data Center Live Capacity (GW) and China Data Center Demand (GW), while the line graph shows the utilization rate (%) over time. The data series are labeled with the year and corresponding values for each metric. The title is 'China Data Center Live Capacity (GW)' and 'China Data Center Demand (GW)'.
</details>

We expect GDS, VNET and Range to lead market share gains on utilized capacity over the next 3 years

![](images/baefbd44559d92e49ba6378b649843fca03003d9c2ba44a9ed4ee4414dfae277.jpg)

<details>
<summary>bar_stacked</summary>

| Year | GDS (%) | VNET (%) | Range (%) | Sinnet (%) | Athub (%) |
|---|---|---|---|---|---|
| 2022 | 9.6 | 2.6 | 2.4 | 1.8 | 2.6 |
| 2023 | 8.3 | 3.5 | 3.1 | 1.5 | 2.5 |
| 2024 | 7.5 | 3.8 | 3.5 | 1.3 | 2.3 |
| 2025 | 7.2 | 4.8 | 3.5 | 1.3 | 1.9 |
| 2026E | 6.9 | 5.5 | 3.7 | 1.3 | 1.7 |
| 2027E | 7.1 | 6.2 | 4.2 | 1.4 | 1.6 |
| 2028E | 8.0 | 6.4 | 4.6 | 1.3 | 1.4 |
</details>

# GPUaaS as the new business model: Rationale, economics and risks

GPUaaS pricing has seen $30\%+$ price increase YTD in the US   
![](images/07f942f2bbc12c02b09ab268655345c136c9c628b897f2aba8d8f83486f69ca5.jpg)

<details>
<summary>line</summary>

| Quarter | Value (US$ per hour) |
| :--- | :--- |
| 1Q24 | 2.80 |
| 2Q24 | 2.35 |
| 3Q24 | 2.30 |
| 4Q24 | 2.00 |
| 1Q25 | 1.95 |
| 2Q25 | 1.95 |
| Jul-25 | 1.85 |
| Aug-25 | 1.75 |
| Sep-25 | 1.75 |
| Oct-25 | 1.70 |
| Nov-25 | 1.73 |
| Dec-25 | 1.73 |
| Jan-26 | 1.77 |
| Feb-26 | 2.08 |
| Mar-26 | 2.35 |
+36% increase vs. Dec 2025
</details>

GPUaaS: Unit economics is attractive in the environment of strong price and utilization levels

![](images/60136d44541499c9cf9dc05106530e50424f2a55352a759b84230562d184df8f.jpg)

<details>
<summary>bar</summary>

| Category | Value |
|---|---|
| Revenue | 100 |
| Power | (10) |
| Labor, maintenance, etc | (3) |
| Colocation | (7) |
| EBITDA | 80 |
| Depreciation | (72) |
| EBIT | 8 |
</details>

H100/H200 avg. rental contract price in China sees a similar trend   
![](images/90159be4a29f985fdaebca87fbafce52a34fa63ddce730b13a9d1857dc948218.jpg)

<details>
<summary>bar</summary>

| Month   | H100 | H200 |
|---------|------|------|
| Feb-26  | 57   | 63   |
| Mar-26  | 63   | 70   |
| Apr-26  | 70   | 83   |
</details>

![](images/667b8ee9846a37f0b1671718cea8ff186a73f8a38ab1a47242aa7b740ec183d3.jpg)

1.Access to advanced GPUs   
2.CAPEX and cost efficiency   
3.Time-to-market and scalability   
4.Competition and data security

# Western China hUBS as the new markets for capacity expansion

Map of China's key data center hUBS and 10 clusters   
![](images/c959d00838e837f122bf72f9252e182de62c420f01171d02e5976f8414b78094.jpg)

<details>
<summary>text_image</summary>

Horinger cluster
Inner Mongolia hub
Beijing-Tianjin-Hebei Hub
Zhangjiakou cluster
Zhongwei cluster
Ningxia hub
Wuhu cluster
Qingyang cluster
Gansu hub
Yangtze River Delta Hub
Tianfu cluster
Chengdu-Chongqing hub
Yangtze River Delta cluster
Chongqing cluster
Guizhou hub
Greater Bay Area hub
Shaoguan cluster
Gui'an cluster
</details>

... which are home to majority of China's intelligent computing power   
![](images/25cb82d7627b05d4abeb0d4e5eacb806d1fdaf9a088464319d2fd6b3dec9b1cb.jpg)

<details>
<summary>bar_stacked</summary>

| Category | 8 computing clusters (%) | Other regions (%) |
| :--- | :--- | :--- |
| Intelligent computing power (mid-2025) | 79 | 21 |
| New computing power supply (2021-25) | 70 | 30 |
| Data center cabinets (1Q26) | 47 | 53 |
</details>

<table><tr><td>HUBS</td></tr><tr><td>Clusters</td></tr><tr><td>Key metrics for respective cluster</td></tr><tr><td>Projects #</td></tr><tr><td>IT power capacity (MW)</td></tr><tr><td>Intelligent computing power (PFLOPS, FP16)</td></tr><tr><td>Total computing power (PFLOPS)</td></tr><tr><td>Latency to Beijing (ms)</td></tr><tr><td>Latency to Yangzte River Delta (ms)</td></tr><tr><td>Latency to Greater Bay Area (ms)</td></tr><tr><td>Electricity price (Rmb/kWh)</td></tr><tr><td>Average temperature (°C)</td></tr></table>

<table><tr><td colspan="3">Eastern clusters</td></tr><tr><td>Beijing-Tianjin-Hebei</td><td>Yangtze River Delta</td><td>Greater Bay Area</td></tr><tr><td>Zhangjiakou</td><td>Wuhu/Yangtze River Delta</td><td>Shaoguan</td></tr><tr><td>48</td><td>15</td><td>20</td></tr><tr><td>2,025</td><td>433</td><td>997</td></tr><tr><td>255,500</td><td>35,000</td><td>16,000</td></tr><tr><td>300,000</td><td></td><td></td></tr><tr><td>&lt;3</td><td>~10</td><td>~15</td></tr><tr><td>~15</td><td>~5</td><td>~10</td></tr><tr><td>&lt;20</td><td>~15</td><td>~5</td></tr><tr><td>0.37-0.42</td><td>0.35-0.45</td><td>0.40-0.50</td></tr><tr><td>8.6</td><td>15</td><td>20</td></tr></table>

<table><tr><td colspan="5">Western/Northern clusters</td></tr><tr><td>Guizhou</td><td>Inner Mongolia</td><td>Ningxia</td><td>Gansu</td><td>Chengdu-Chongqing</td></tr><tr><td>Guian</td><td>Horinger County</td><td>Zhongwei</td><td>Qingyang</td><td>Chengdu/Chongqing</td></tr><tr><td colspan="5"></td></tr><tr><td>26</td><td>46</td><td></td><td></td><td>29</td></tr><tr><td>3,500</td><td>1,305</td><td>575</td><td>255</td><td></td></tr><tr><td>79,380</td><td></td><td></td><td></td><td></td></tr><tr><td>81,000</td><td>101,000</td><td>130,000</td><td>114,000</td><td>20,000</td></tr><tr><td>&lt;20</td><td>~5</td><td>~8-10</td><td>&lt;8</td><td>&lt;18</td></tr><tr><td>&lt;20</td><td>&lt;15</td><td>&lt;18</td><td>&lt;12</td><td>&lt;18</td></tr><tr><td>&lt;10</td><td>n.a.</td><td>&lt;20</td><td>&lt;15</td><td>&lt;18</td></tr><tr><td>0.35</td><td>0.36</td><td>0.36</td><td>&lt;0.4</td><td>0.4-0.6</td></tr><tr><td>15</td><td>5.4</td><td>8.8</td><td>10.8</td><td>17</td></tr></table>

# Range Intelligent (300442.SZ) initiate at Buy with 12m TP of Rmb117; One of the fastest-growing data center operators in China

<table><tr><td>Calendar year</td><td>GDS</td><td>VNET</td><td>Range</td><td>Sinnet</td><td>Athub</td><td>SUNeVision</td><td>DayOne</td></tr><tr><td>Market cap (US$ bn)*</td><td>8.2</td><td>2.6</td><td>21.3</td><td>4.2</td><td>3.9</td><td>1.8</td><td>14.1</td></tr><tr><td>Enterprise value (US$ bn)*</td><td>13.5</td><td>5.6</td><td>25.5</td><td>4.9</td><td>4.0</td><td>4.6</td><td>19.5</td></tr><tr><td>2026E EV/EBITDA**</td><td>12x</td><td>11x</td><td>29x</td><td>24x</td><td>23x</td><td>15x</td><td>42x</td></tr><tr><td>2027E EV/EBITDA**</td><td>11x</td><td>10x</td><td>22x</td><td>21x</td><td>22x</td><td>13x</td><td>23x</td></tr><tr><td>2025-28E revenue CAGR</td><td>12%</td><td>16%</td><td>40%</td><td>7%</td><td>4%</td><td>13%</td><td>80%</td></tr><tr><td>2025-28E EBITDA CAGR</td><td>12%</td><td>23%</td><td>47%</td><td>13%</td><td>3%</td><td>13%</td><td>88%</td></tr><tr><td>Listed market</td><td>ADR/HKEx</td><td>ADR</td><td>A-share</td><td>A-share</td><td>A-share</td><td>HKEx</td><td>Private</td></tr><tr><td>GS rating</td><td>Buy</td><td>Buy</td><td>Buy</td><td>Sell</td><td>Neutral</td><td>Buy</td><td>n.a.</td></tr></table>

Scorecard by key metrics (1 = best) 

<table><tr><td>Current</td><td>2.7</td><td>3.0</td><td>2.3</td><td>4.0</td><td>2.3</td><td>4.0</td><td>4.3</td></tr><tr><td>Capacity</td><td>1</td><td>2</td><td>3</td><td>5</td><td>5</td><td>6</td><td>4</td></tr><tr><td>Profitability</td><td>3</td><td>4</td><td>2</td><td>5</td><td>1</td><td>1</td><td>4</td></tr><tr><td>Leverage</td><td>4</td><td>3</td><td>2</td><td>2</td><td>1</td><td>5</td><td>5</td></tr><tr><td>Forecast</td><td>3.6</td><td>4.0</td><td>2.6</td><td>3.2</td><td>4.0</td><td>3.8</td><td>2.6</td></tr><tr><td>Capacity growth %</td><td>3</td><td>3</td><td>2</td><td>4</td><td>5</td><td>2</td><td>1</td></tr><tr><td>Capacity reserve</td><td>2</td><td>3</td><td>1</td><td>4</td><td>6</td><td>5</td><td>3</td></tr><tr><td>EBITDA growth %</td><td>5</td><td>4</td><td>3</td><td>5</td><td>6</td><td>5</td><td>1</td></tr><tr><td>Pricing trend</td><td>4</td><td>5</td><td>3</td><td>1</td><td>2</td><td>4</td><td>2</td></tr><tr><td>Leverage</td><td>4</td><td>5</td><td>4</td><td>2</td><td>1</td><td>3</td><td>6</td></tr></table>

Range Intelligent has a total capacity of 6GW in China, including 750MW capacity in service and 5.25GW capacity under construction and as reserve   
![](images/566f4a8eebcc7dc3850a5f6758323c04b0dce8b4eae563679d322f2885390e7c.jpg)

<details>
<summary>bar_stacked</summary>

| Region | Live | Under construction and reserve |
| :--- | :--- | :--- |
| Beijing - Tianjin - Hebei | 400 | 2500 |
| Yangtze River Delta | 250 | 450 |
| Greater Bay Area | 150 | 500 |
| Chengdu - Chongqing | 0 | 300 |
| Gansu | 0 | 150 |
| Others | 0 | 900 |
</details>

We expect Range Intelligent to deliver 40%/47%/26% revenue/EBITDA/net profit CAGRs in 2025-28E, the fastest among our data center coverage   
![](images/c77d1b259cf948be165c7d503a9649217d1bd6acbba91004f11a6b9b609a542d.jpg)

<details>
<summary>bar_line</summary>

| Year | Revenue (Rmb bn) | EBITDA (Rmb bn) | Net profit (Rmb bn) | Live capacity (MW) |
| :--- | :--- | :--- | :--- | :--- |
| 2022 | 2.7 | 1.5 | 1.1 | 250 |
| 2023 | 4.4 | 2.2 | 1.7 | 400 |
| 2024 | 4.4 | 2.6 | 1.8 | 450 |
| 2025 | 5.7 | 3.6 | 1.9 | 650 |
| 2026E | 8.5 | 5.9 | 2.7 | 950 |
| 2027E | 11.9 | 8.6 | 3.3 | 1300 |
| 2028E | 15.5 | 11.2 | 3.8 | 1800 |
</details>

# Key Buy-rated stock ideas within data centers and cloud infra

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Company</td><td rowspan="2">Rating</td><td rowspan="2">Mkt Cap (US$mn)</td><td rowspan="2">FX</td><td rowspan="2">Latest close</td><td rowspan="2">12m TP</td><td rowspan="2">+/-</td><td colspan="2">EV/EBITDA</td><td colspan="2">P/S</td><td colspan="3">Sales yoy</td><td colspan="3">EBITDA yoy</td></tr><tr><td>CY26</td><td>CY27</td><td>CY26</td><td>CY27</td><td>CY26</td><td>CY27</td><td>CY28</td><td>CY26</td><td>CY27</td><td>CY28</td></tr><tr><td>300442.SZ</td><td>Range Intelligent</td><td>Buy</td><td>24,458</td><td>Rmb</td><td>101.62</td><td>117.00</td><td>15%</td><td>33x</td><td>24x</td><td>19.4x</td><td>14.0x</td><td>51%</td><td>39%</td><td>30%</td><td>67%</td><td>45%</td><td>31%</td></tr><tr><td>GDS/9698.HK</td><td>GDS Holdings</td><td>Buy</td><td>8,879</td><td>$</td><td>45.70</td><td>55.00</td><td>20%</td><td>16x</td><td>15x</td><td>4.8x</td><td>4.3x</td><td>10%</td><td>10%</td><td>16%</td><td>10%</td><td>11%</td><td>16%</td></tr><tr><td>300383.SZ</td><td>Sinnet Tech</td><td>Sell</td><td>4,712</td><td>Rmb</td><td>17.80</td><td>12.40</td><td>-30%</td><td>26x</td><td>23x</td><td>4.5x</td><td>4.1x</td><td>0%</td><td>8%</td><td>7%</td><td>7%</td><td>15%</td><td>11%</td></tr><tr><td>603881.SS</td><td>Shanghai Athub</td><td>Neutral</td><td>4,592</td><td>Rmb</td><td>43.41</td><td>34.00</td><td>-22%</td><td>27x</td><td>25x</td><td>18.1x</td><td>16.9x</td><td>0%</td><td>7%</td><td>6%</td><td>-2%</td><td>7%</td><td>5%</td></tr><tr><td>KC</td><td>Kingsoft Cloud</td><td>Buy</td><td>4,943</td><td>$</td><td>17.92</td><td>19.40</td><td>8%</td><td>12x</td><td>9x</td><td>2.7x</td><td>2.2x</td><td>30%</td><td>26%</td><td>18%</td><td>70%</td><td>45%</td><td>27%</td></tr><tr><td>VNET</td><td>VNET Group</td><td>Buy</td><td>3,466</td><td>$</td><td>11.28</td><td>15.50</td><td>37%</td><td>12x</td><td>11x</td><td>2.0x</td><td>1.7x</td><td>17%</td><td>18%</td><td>15%</td><td>22%</td><td>25%</td><td>20%</td></tr><tr><td>1686.HK</td><td>SUNeVision</td><td>Buy</td><td>2,110</td><td>Rmb</td><td>7.00</td><td>7.70</td><td>10%</td><td>16x</td><td>14x</td><td>4.8x</td><td>4.3x</td><td>6%</td><td>11%</td><td>nm</td><td>6%</td><td>11%</td><td>nm</td></tr></table>

Range Intelligent: Range Intelligent is one of China's largest data center operators in terms of live capacity (750MW as of 2025) and reserved capacity (6GW as of late, the majority of which has secured power quota approvals). We see Range Intelligent as one of the fastest growing data center operators in China with $27\% / 33\%$ utilized IT capacity/revenue CAGRs in 2025-30E, thanks to its 1) rich capacity reserve, 2) full-stack AIDC capabilities, 3) strong customer relationships, and 4) diverse, low-cost financing capabilities. We expect its GPUaaS investments to generate incremental profitability in a favorable demand and pricing environment, and are positive about its overseas expansion initiatives to capture rising AI demand in APAC in the long term, which leverages Range's supply chain and human resources capabilities.

GDS Holdings: GDS is the leader in China's carrier-neutral data center market with a wholesale-centric business model. We see GDS has established leadership as one of the largest data center platforms in China in terms of developable capacity via resource expansion in key computing clusters, and fortified its balance sheet via financial discipline and capital recycling, and hence is poised to capture demand from key customers including China's top hyperscalers. That said, we expect $-8\%$ MSR (monthly service revenue) CAGR in 2025-28E (in Rmb/kW) due to existing contract renewals and new order deliveries at lower prices vs. historical levels.

VNET Group: We see VNET transforming from a traditional retail IDC operator to a fast-growing wholesale IDC operator and entering a revenue/EBITDA growth acceleration phase over the next few years from intensifying AI investment, with wholesale IDC accounting for 35% of revenue in 2025 and growing at 37-38% revenue/EBITDA CAGRs in 2025-28E. We believe rising wholesale IDC contributions should lead to continued upward multiple re-rating and valuation compounding for VNET, despite near-term overhang on its largest shareholder selldown and potential financing.

Kingsoft Cloud: KC is a leading cloud service provider in China. We believe KC stands out among China's cloud service providers in 1) its highest AI contribution to revenue at $31\%$ in 2025 and 2) revenue growth visibility from its related party Xiaomi which provides $46\%$ revenue CAGR in 2025-28E. We see the company as a key beneficiary of Xiaomi's continued stepped-up AI investments (Rmb60bn over next 3 years) to support its ambition of becoming a leading LLM force and integrating AI with the physical world. Meanwhile, KC continues to capture AI demand (still mostly AI training) from other internet and AI companies.

SUNeVision Holdings: SUNeVision is the largest data center provider in HK in terms of live capacity. We expect SUNeVision to benefit from rising data and AI demand in HK thanks to its solid capacity expansion pipeline (i.e. power capacity to more than double post the launch of MEGA IDC future phases). We believe the company can maintain a 46% payout ratio in FY26-28E.

# Price target risks and methodology

Range Intelligent: Our 12-month target price of Rmb117 is based on an 18x 2030E EV/EBITDA discounted back to end-2026E at a $10\%$ CoE. Key risks: 1) Lower-than-expected order wins amid a competitive environment; 2) Slower-than-expected utilization rate ramp-up; 3) Larger-than-expected pricing pressure; 4) Worse-than-expected execution in overseas expansion; 5) Changes in chip availability due to regulatory changes, domestic capacity ramp-up delays, etc; 6) Difficulties in financing.

GDS Holdings: Our 12m target prices of US\$55/HK\$54 for GDS/9698.HK are based on a SOTP valuation for GDS China and DayOne, with a 10% holdco discount. Key risks: Below-expected move-in demand and utilization improvement, slower overseas revenue/profitability ramp-up, lower-than-expected pricing trend in China and overseas markets, customer churn, slower deleveraging process.

VNET Group: Our 12m target price of US\$15.5 is based on a target 12m-fwd EV/EBITDA multiple of 12x applied to 2027E adj. EBITDA. Key risks: 1) inability to finance the growth objectives; 2) softer-than-expected execution on order wins; 3) geopolitical risks regarding AI; 4) further downturn of traditional businesses; 5) faster than or unexpected change in AI model training demand brought by latest development in technology.

Kingsoft Cloud: Our 12m target price of US\$19.4 is based on a DCF (WACC 10.3%, TGR 3%). Key risks: 1) Supply chain disruptions and inability to secure high-end chips; 2) Heightened competitive pressure from peers; 3) 

[中间内容因长度限制已省略]

-term impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to sUBStantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.fiadocumentation.org/fia/regulatory-disclosures\_1/fia-uniform-futures-and-options-on-futures-risk-disclosures-booklet-pdf-version-2018. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

# Disclosure Appendix

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
