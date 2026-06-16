你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

【研报解析内容】
"""
## Investor Presentation | Asia Pacific

## Stronger Trade, Weaker Domestic Demand

MS ASIA LIMITED

## Robin Xing

Chief China Economist

Robin.Xing@morganstanley.com +852 2848-6511

## Jenny Zheng, CFA

Economist

Jenny.L.Zheng@morganstanley.com +852 3963-4015

![](images/98f17a9f8b3a7b281d1a49dae46f8c48ef6ced25b711135eabce7d79977f9de3.jpg)

<details>
<summary>text_image</summary>

Asia Summer School 2026
</details>

## Broadening Export Improvement

Global AI cycle drives China trade growth  
![](images/36b8ae9194349e795e95d1dfe46231c154a48154fc0ebc76b883419a73e0a9be.jpg)

<details>
<summary>line chart</summary>

| Month   | Exports: Tech | Imports: Tech | Exports: Non-Tech | Imports: Non-Tech |
|---------|---------------|---------------|-------------------|-------------------|
| May-21  | ~5%           | ~30%          | ~35%              | ~60%              |
| Aug-21  | ~20%          | ~15%          | ~25%              | ~35%              |
| Nov-21  | ~15%          | ~20%          | ~20%              | ~30%              |
| Feb-22  | ~0%           | ~-5%          | ~-10%             | ~-5%              |
| May-22  | ~10%          | ~-10%         | ~-15%             | ~-10%             |
| Aug-22  | ~-10%         | ~-15%         | ~-20%             | ~-15%             |
| Nov-22  | ~-30%         | ~-35%         | ~-25%             | ~-20%             |
| Feb-23  | ~-25%         | ~-30%         | ~-20%             | ~-15%             |
| May-23  | ~-15%         | ~-20%         | ~-10%             | ~-5%              |
| Aug-23  | ~-10%         | ~-15%         | ~-5%              | ~0%               |
| Nov-23  | ~5%           | ~0%           | ~0%               | ~5%               |
| Feb-24  | ~10%          | ~15%          | ~5%               | ~10%              |
| May-24  | ~20%          | ~25%          | ~10%              | ~15%              |
| Aug-24  | ~15%          | ~20%          | ~5%               | ~10%              |
| Nov-24  | ~10%          | ~15%          | ~0%               | ~5%               |
| Feb-25  | ~5%           | ~10%          | ~5%               | ~0%               |
| May-25  | ~10%          | ~15%          | ~10%              | ~5%               |
| Aug-25  | ~15%          | ~20%          | ~15%              | ~10%              |
| Nov-25  | ~20%          | ~25%          | ~20%              | ~15%              |
| Feb-26  | ~40%          | ~45%          | ~30%              | ~35%              |
| May-26  | ~90%          | ~70%          | ~10%              | ~15%              |
</details>

Elsewhere, export breadth is improving  
![](images/f795da5a04c35596209d281e242ea361a91405ade55dd979419721b2d3d0e19d.jpg)

<details>
<summary>bar chart</summary>

China Exports, YoY
| Category | Apr-26 (%) | May-26 (%) |
|---|---|---|
| Electronic Integrated Circuit | 100 | 110 |
| Computers | 45 | 65 |
| Mobile Phone | 10 | 45 |
| Auto | 45 | 40 |
| Refined Petroleum Product | -5 | 28 |
| Plastic Article | 8 | 13 |
| Auto Part | 6 | 4 |
| Furniture | -3 | 2 |
| Textile | -1 | 0 |
| Steel Product | -5 | 1 |
| Garment | -1 | 2 |
| Liquid Crystal Display Panel | -3 | -3 |
| Footwear | -15 | -8 |
</details>

Source: CEIC, MS

## Yet Private Credit Demand Weakened Further

Broad-based private credit demand weakness  
![](images/d1c788ea4651b5c0c7f1e2fcfa02352044c6efe58fd1170bbbf21ce927547f90.jpg)

<details>
<summary>bar chart</summary>

Data in May, RMB Bn
| Category | Past 5Y Avg (RMB Bn) | 2026 (RMB Bn) |
| :--- | :--- | :--- |
| New Short-term Household Loans | 110 | -70 |
| New Longer-term Household Loans | 165 | -50 |
| New Longer-term Corporate Loans+Bond Financing | 535 | 145 |
</details>

Continued household deleveraging in aggregate suggests the recent housing sales rebound is narrow  
![](images/c4feaca47b2790e435077bbef30355b8fc2ec30e740b4788cec8339eeba3bab6.jpg)

<details>
<summary>line chart</summary>

| Month | 2021-2025 Avg. | 2025 | 2026 |
|-------|----------------|------|------|
| Jan   | ~11,000        | ~14,000 | ~9,000 |
| Feb   | ~10,000        | ~13,000 | ~13,000 |
| Mar   | ~12,000        | ~14,500 | ~7,800 |
| Apr   | ~14,500        | ~16,500 | ~16,000 |
| May   | ~12,500        | ~8,000 | ~12,500 |
| Jun   | ~13,500        | ~13,500 | ~15,500 |
| Jul   | ~12,500        | ~13,500 | ~12,500 |
| Aug   | ~11,500        | ~11,500 | ~11,500 |
| Sep   | ~10,500        | ~9,500 | ~9,500 |
| Oct   | ~6,500         | ~6,500 | ~6,500 |
| Nov   | ~11,500        | ~12,500 | ~12,500 |
| Dec   | ~11,500        | ~13,500 | ~13,500 |
</details>

Source: CEIC, MS

## Sequentially Slower Oil Push, Limited Reflation Elsewhere

PPI MoM slipped on reduced oil price impulse  
![](images/60dd8c1d904cf4f9a1f737bd57d85a650a9fce19b77a63354f174e3ef7556a75.jpg)

<details>
<summary>bar-line hybrid</summary>

PPI Breakdown
| Month | Non-ferrous Metals (%) | Non-ferrous Metals Downstream (%) | Coal (%) | Oil & Petrochemical (%) | Remainder (%) | PPI MoM |
|---|---|---|---|---|---|---|
| Jan-25 | -0.1 | -0.1 | -0.1 | -0.1 | -0.2 | -0.2 |
| Feb | -0.1 | -0.1 | -0.1 | -0.1 | -0.2 | -0.1 |
| Mar | -0.1 | -0.1 | -0.1 | -0.1 | -0.4 | -0.4 |
| Apr | -0.1 | -0.1 | -0.1 | -0.1 | -0.3 | -0.4 |
| May | -0.1 | -0.1 | -0.1 | -0.1 | -0.3 | -0.4 |
| Jun | -0.1 | -0.1 | -0.1 | -0.1 | -0.3 | -0.4 |
| Jul | -0.1 | -0.1 | -0.1 | -0.1 | -0.3 | -0.2 |
| Aug | -0.1 | -0.1 | 0.05 | 0.05 | 0.05 | 0.05 |
| Sep | 0.05 | 0.05 | 0.1 | 0.1 | 0.15 | 0.1 |
| Oct | 0.15 | 0.15 | 0.15 | 0.15 | 0.25 | 0.2 |
| Nov | 0.15 | 0.15 | 0.25 | 0.25 | 0.25 | 0.2 |
| Dec | 0.25 | 0.25 | 0.25 | 0.25 | 0.25 | 0.3 |
| Jan-26 | 0.45 | 0.55 | 0.15 | 0.15 | 0.35 | 0.4 |
| Feb | 0.45 | 0.35 | 0.15 | 0.65 | -0.35 | 0.4 |
| Mar | 0.15 | 0.25 | 0.15 | 0.85 | 0.95 | 1.2 |
| Apr | 0.15 | 0.15 | 0.15 | 1.75 | 1.75 | 1.7 |
| May | 0.15 | 0.15 | 0.15 | 0.35 | 0.35 | 0.45 |
</details>

Limited transmission to core CPI  
![](images/72a06e95790541e297e3d615e82f393fb2ab9ef34184de1f0d13cdfa35f55233.jpg)

<details>
<summary>line chart</summary>

| Month   | 6M/6M SAAR | MoM SAAR |
|---------|------------|----------|
| May-23  | 0.5        | 0.6      |
| Aug-23  | 1.3        | 0.9      |
| Nov-23  | 0.7        | -0.8     |
| Feb-24  | 0.8        | -0.2     |
| May-24  | 0.4        | 0.6      |
| Aug-24  | -0.5       | -0.7     |
| Nov-24  | 0.6        | 1.7      |
| Feb-25  | 1.0        | -0.1     |
| May-25  | 0.8        | 0.3      |
| Aug-25  | 1.5        | -0.3     |
| Nov-25  | 1.2        | 1.9      |
| Feb-26  | 1.4        | -0.9     |
| May-26  | 0.8        | 0.5      |
</details>

Source: CEIC, MS

## Budget Rollout May Accelerate from 3Q to Support AI and Energy Transition

Pace of fiscal rollout slowed in Apr-May  
![](images/e957e961b4f0fa86c472b927f886e66e2eb99d3f6112e100a984b769b05f51da.jpg)

<details>
<summary>line chart</summary>

| Month | 2023 | 2024 | 2025 | 2026 |
|-------|------|------|------|------|
| Jan   | ~5%  | ~3%  | ~7%  | ~8%  |
| Feb   | ~10% | ~6%  | ~15% | ~17% |
| Mar   | ~15% | ~10% | ~25% | ~25% |
| Apr   | ~20% | ~10% | ~30% | ~32% |
| May   | ~25% | ~15% | ~40% | ~40% |
| Jun   | ~30% | ~20% | ~50% | -    |
| Jul   | ~35% | ~35% | ~60% | -    |
| Aug   | ~40% | ~45% | ~70% | -    |
| Sep   | ~50% | ~55% | ~80% | -    |
| Oct   | ~60% | ~65% | ~85% | -    |
| Nov   | ~75% | ~75% | ~90% | -    |
| Dec   | 100% | 100% | 100% | 100% |
</details>

Expecting stronger budget execution from 3Q, with Focus on AI and Energy Transition in the “Six Networks”  
![](images/56e82355fa868580e9f323fbff1a4dff3e47ec6a51c8c119dd452e9da597062d.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["THE &quot;SIX NETWORKS&quot;"] --> B["WATER NETWORK"]
  A --> C["LOG"]
  A --> D["PIPE"]
  A --> E["DATA"]
  A --> F["5G"]
  A --> G["LOGISTICS NETWORK"]
  A --> H["NEW-TYPE POWER GRID"]
  A --> I["COMPUTING NETWORK"]
  A --> J["Urban UNDERGROUND PIPELINE"]
  A --> K["2026-30E: > Rmb5trn"]
  A --> L["2026-30E: > Rmb2trn"]
  A --> M["2026-30E: ~Rmb7trn"]
  A --> N["2026-30E: ~30% of 2025 Infra Capex"]
```
</details>

- Only 41% of annual government bond quota was utilized (46% by May-25)  
• We thus expect an accelerated budget rollout, not additional stimulus, from 3Q  
- Policy focus will remain capex-centric, particularly on AI computing networks, internet data centers and smart grids under the "Six Networks" initiative

Source: CEIC, MS

## Smarter Industrial Policy Alone May Not Narrow Supply-Demand Imbalances

Investment ex-property growth slowed from 2021-23's spike, but only at a modest pace  
![](images/a160fcd1a832495391c95faee322e92434f0d2ebe828ab5a0ccc6dc6ee425011.jpg)

<details>
<summary>line chart</summary>

| Year | GFCF (%) | GFCF ex-Property (%) |
|---|---|---|
| 2014 | 7.4 | 9.0 |
| 2015 | 5.5 | 8.0 |
| 2016 | 7.3 | 7.7 |
| 2017 | 6.3 | 7.3 |
| 2018 | 7.5 | 6.9 |
| 2019 | 5.8 | 4.5 |
| 2020 | 3.7 | 2.9 |
| 2021 | 2.5 | 2.5 |
| 2022 | 3.5 | 7.8 |
| 2023 | 4.6 | 7.5 |
| 2024 | 2.5 | 5.8 |
| 2025 | 2.0 | 4.7 |
| 2026E | 3.5 | 5.9 |
| 2027E | 2.9 | 4.4 |
</details>

The "baton" of investment has been passed from sectors with overcapacity to those with less oversupply, for now  
![](images/bee57f9903e82d2658ffddd092ede0b2a79996e4eace3064919e8a8db49a9783.jpg)

<details>
<summary>scatter plot</summary>

| FAI CAGR in 2021-23 | FAI Growth in 2024-25 |
| ------------------- | --------------------- |
| -8%                 | 16%                   |
| -5%                 | 5%                    |
| 0%                  | 0%                    |
| 5%                  | -5%                   |
| 10%                 | 10%                   |
| 15%                 | 14%                   |
| 20%                 | -10%                  |
| 25%                 | 21%                   |
| 30%                 | -7%                   |
| 35%                 | -10%                  |
</details>

## "National unified market" and anti-involution are in the right direction but challenging to implement:

- Top-down coordination unworkable; market mechanisms for specialization still weak  
- Local incentives misaligned  
• Tax system biases production

Source: CEIC, MS estimates

## Reforms Needed for Economic Rebalancing

## Five-year plan remains supply-centric

## Growth Target

\- Not Specified

## Consumption

• Commitments to boost consumption/GDP ratio

## Tech & Green Transition

Clear numerical targets:

• R&D (5Y CAGR: >7%)  
• Labor productivity growth (>GDP growth)  
• Digital economy ( $\uparrow$ 2pp of GDP by 2030)  
• CO2 emissions per unit of GDP ( $\downarrow$ 17% by 2030 vs. 2025)  
• Additional target on non-fossil fuel consumption

## Local government incentives should be reoriented towards consumption

![](images/d8d9e2f5b5ea91c31e98ae8d5876bd5bc8fcb1bfeb5dfc68d6e45832805489b4.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Economic Rebalancing Reforms Needed"] --> B["CADRE EVALUATION REFORM"]
  A --> C["SOCIAL WELFARE REFORM"]
  A --> D["FISCAL SYSTEM REFORM"]
  A --> E["Social Welfare Reform"]
  B --> F["Reward outcomes that improve household well-being and the environment."]
  C --> G["Strengthen the safety net to reduce precautionary savings and boost consumption."]
  D --> H["Shift to efficiency-linked direct taxes and fund public services, not projects."]
```
</details>

Source: CEIC, MS

## Outbound Investment

## Tightening Outbound Investment Controls to Regulate Flows...

China's non-reserve balance of payments: from a unique "twin surplus" to the more common "mirror image"...  
![](images/7aa013dc024af20a752d23bf86024fc74bbf928cb3e43d55f99252e56082d49d.jpg)

<details>
<summary>line chart</summary>

| Date   | Current Account Balance | Capital and Financial Account Balance (Incl. Error and Omission) |
|--------|--------------------------|------------------------------------------------------------------|
| Mar-00 | 0                        | 0                                                                |
| Mar-01 | 0                        | 0                                                                |
| Mar-02 | 0                        | 0                                                                |
| Mar-03 | 0                        | 0                                                                |
| Mar-04 | 0                        | 0                                                                |
| Mar-05 | 0                        | 0                                                                |
| Mar-06 | 0                        | 0                                                                |
| Mar-07 | 0                        | 0                                                                |
| Mar-08 | 0                        | 0                                                                |
| Mar-09 | 0                        | 0                                                                |
| Mar-10 | 0                        | 0                                                                |
| Mar-11 | 0                        | 0                                                                |
| Mar-12 | 0                        | 0                                                                |
| Mar-13 | 0                        | 0                                                                |
| Mar-14 | 0                        | 0                                                                |
| Mar-15 | 0                        | 0                                                                |
| Mar-16 | 0                        | 0                                                                |
| Mar-17 | 0                        | 0                                                                |
| Mar-18 | 0                        | 0                                                                |
| Mar-19 | 0                        | 0                                                                |
| Mar-20 | 0                        | 0                                                                |
| Mar-21 | 0                        | 0                                                                |
| Mar-22 | 0                        | 0                                                                |
| Mar-23 | 0                        | 0                                                                |
| Mar-24 | 0                        | 0                                                                |
| Mar-25 | 0                        | 0                                                                |
| Mar-26 | 0                        | 0                                                                |
</details>

...with capital outflows increasingly led by portfolio investment  
![](images/c73bc7aa520e9a05ae9a7fdbea471f3c7a94a54fbe7024e9d7d691e95df51271.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Date   | FDI  | Portfolio Investment | Other Investment | Capital and Financial Account |
|--------|------|----------------------|------------------|-------------------------------|
| Dec-04 | 0    | 0                    | 0                | 0                             |
| Dec-05 | 0    | 0                    | 0                | 0                             |
| Dec-06 | 0    | 0                    | 0                | 0                             |
| Dec-07 | 0    | 0                    | 0                | 0                             |
| Dec-08 | 0    | 0                    | 0                | 0                             |
| Dec-09 | 0    | 0                    | 0                | 0                             |
| Dec-10 | 0    | 0                    | 0                | 0                             |
| Dec-11 | 0    | 0                    | 0                | 0                             |
| Dec-12 | 0    | 0            

[中间内容因长度限制已省略]

N-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the United States by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 4.9(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

© 2026 MS
"""
