你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 1800 字，允许上下浮动 15%。
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
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来社群继续拆完整报告。
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
- 默认避免出现具体投行品牌名，比如“高盛”“Goldman Sachs”，统一写作“某外资投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Initiation of Coverage

# Kioxia Holdings Corp

# Peak is not here yet

# Initiating coverage with Buy rating and price target of ¥79,000

Consensus OP estimates are ¥6.43trn for FY3/27 and ¥7.47trn for FY3/28. In comparison, we forecast ¥7.11trn and ¥8.99trn for the respective fiscal years, significantly exceeding consensus, especially for FY3/28. NAND flash memory prices are likely to rise qoq for the next six quarters before peaking in Q3 2027 (about 1.5 years from now, link). Kioxia has established a competitive advantage in terms of bit cost by successfully focusing on horizontal miniaturisation technology, which limits wafer cost increases. We think this sustained favourable market environment and cost advantage are not yet priced into the stock.

# AI demand has transformed the NAND flash memory market

Historically, NAND flash memory has been used primarily for storage for PCs, smartphones, tablets, and AI training data. For AI inference applications, though, NAND flash memory has become a part of the computational system, akin to DRAM, due to the need to retain users' chat history. Even with such compression technologies as TurboQuant KV cache, overall demand is likely to continue to rise, with the rapid growth driven by AI still unmitigated. And with the company's bit supply growth remaining below +20% yoy, we expect supply-demand conditions to remain tight (link).

# Established cost advantages within the industry

The company has maintained the highest operating margin in the industry since 2022. While Korean competitors have focused on vertical stacking, Kioxia has prioritised horizontal bit expansion and selected technologies for reducing costs. This strategy has succeeded in cutting wafer costs by about 50% and bit costs by 10–20%, on our estimates. Investor perceptions of the company's lag based on simple comparisons of stacked layers are likely to improve.

# Valuation: Upside for both earnings and multiples

Our price target is set at ¥79,000, based on estimated BPS at the FY3/28 fiscal year end and a PBR of 4.7x. The PBR multiple of 4.7x is derived from an average ROE of 41% for FY3/28-FY3/31 and a cost of equity (CoE) of 8.6%. This valuation method has been applied consistently across all Asian memory companies. The price target corresponds to an EV/EBITDA of 4x, which aligns with both the historical 10-year average EV/EBITDA for the memory sector and the company's average since its public listing.

Equities 

<table><tr><td>Japan</td></tr><tr><td>Semiconductors</td></tr></table>

<table><tr><td>12-month rating</td><td>BuyPrior : No Rating</td></tr><tr><td>12m price target</td><td>¥79,000Prior :</td></tr><tr><td>Price (28 May 2026)</td><td>¥61,280</td></tr></table>

RIC: 285A.T BBG: 285A JP

Trading data and key metrics 

<table><tr><td>52-wk range</td><td>¥65,450-1,982</td></tr><tr><td>Market cap.</td><td>¥33,464b/US$210b</td></tr><tr><td>Shares o/s</td><td>546m (ORD)</td></tr><tr><td>Free float</td><td>30%</td></tr><tr><td>Avg. daily volume (&#x27;000)</td><td>34,971</td></tr><tr><td>Avg. daily value (m)</td><td>¥1,130,121.5</td></tr><tr><td>Common s/h equity (03/27E)</td><td>¥4840b</td></tr><tr><td>P/BV (03/27E)</td><td>6.9x</td></tr><tr><td>Net debt to EBITDA (03/27E)</td><td>NM</td></tr></table>

EPS (reported, basic) (¥) 

<table><tr><td></td><td>From</td><td>To</td><td>% ch</td><td>Cons.</td></tr><tr><td>03/27E</td><td>-</td><td>9,002.5</td><td>-</td><td>7,475.0</td></tr><tr><td>03/28E</td><td>-</td><td>11,390.8</td><td>-</td><td>9,269.9</td></tr><tr><td>03/29E</td><td>-</td><td>9,757.0</td><td>-</td><td>11,237.3</td></tr></table>

Kenji Yasui

Analyst

kenji.yasui@ubs.com

+81-3-5208 6211

Atsuhiro Kinoshita

Analyst

atsuhiro.kinoshita@ubs.com

+81-3-5208 6768

<table><tr><td>Highlights (¥b)</td><td>03/24</td><td>03/25</td><td>03/26</td><td>03/27E</td><td>03/28E</td><td>03/29E</td><td>03/30E</td><td>03/31E</td></tr><tr><td>Revenues</td><td>1,076.6</td><td>1,706.5</td><td>2,337.6</td><td>9,121.0</td><td>11,301.0</td><td>10,181.0</td><td>9,711.0</td><td>9,711.0</td></tr><tr><td>EBIT (UBS)</td><td>(252.7)</td><td>451.7</td><td>870.4</td><td>7,107.0</td><td>8,991.0</td><td>7,701.0</td><td>6,961.0</td><td>6,941.0</td></tr><tr><td>Net earnings (UBS)</td><td>(243.7)</td><td>272.3</td><td>554.5</td><td>4,916.1</td><td>6,220.3</td><td>5,328.1</td><td>4,816.5</td><td>4,803.2</td></tr><tr><td>EPS (UBS, diluted) (¥)</td><td>(452.1)</td><td>505.2</td><td>1,015.4</td><td>9,002.5</td><td>11,390.8</td><td>9,757.0</td><td>8,820.1</td><td>8,795.7</td></tr><tr><td>DPS (net) (¥)</td><td>0.0</td><td>0.0</td><td>0.0</td><td>2,700.7</td><td>3,417.2</td><td>2,927.1</td><td>2,646.0</td><td>2,638.7</td></tr><tr><td>Net (debt) / cash</td><td>(1,101.3)</td><td>(827.6)</td><td>(775.3)</td><td>1,715.0</td><td>5,612.7</td><td>9,559.9</td><td>12,981.7</td><td>16,287.5</td></tr><tr><td>Profitability/valuation</td><td>03/24</td><td>03/25</td><td>03/26</td><td>03/27E</td><td>03/28E</td><td>03/29E</td><td>03/30E</td><td>03/31E</td></tr><tr><td>EBIT (UBS) margin %</td><td>(23.5)</td><td>26.5</td><td>37.2</td><td>77.9</td><td>79.6</td><td>75.6</td><td>71.7</td><td>71.5</td></tr><tr><td>ROIC (EBIT) %</td><td>(15.3)</td><td>28.1</td><td>45.5</td><td>263.9</td><td>264.7</td><td>219.0</td><td>205.8</td><td>205.0</td></tr><tr><td>EV/EBITDA (UBS core) x</td><td>-</td><td>2.8</td><td>4.5</td><td>4.4</td><td>3.2</td><td>3.2</td><td>3.0</td><td>2.6</td></tr><tr><td>P/E (UBS, diluted) x</td><td>-</td><td>4.3</td><td>8.0</td><td>6.8</td><td>5.4</td><td>6.3</td><td>6.9</td><td>7.0</td></tr><tr><td>Equity FCF (UBS) yield %</td><td>-</td><td>15.4</td><td>7.1</td><td>11.8</td><td>17.2</td><td>16.6</td><td>14.5</td><td>14.2</td></tr><tr><td>Dividend yield (net) %</td><td>-</td><td>0.0</td><td>0.0</td><td>4.4</td><td>5.6</td><td>4.8</td><td>4.3</td><td>4.3</td></tr></table>

Source: Company accounts, LSEG Eikon, UBS estimates. Metrics marked as (UBS) have had analyst adjustments applied. Valuations: based on an average share price that year, (E): based on a share price of ¥ 61,280 on 28-May-2026

# UBSResearch THESIS MAP a guide to our thinking and what's where in this report

# PIVOTAL QUESTIONS

# Q: Q: Can the company maintain its industry-leading NAND flash memory operating margin through 2027?

We expect Kioxia to sustain industry-leading NAND margins versus key peers through CY26–27, supported by its lead in lateral (horizontal) scaling. However, beyond 2027—particularly with the transition to BICS10 (332 layers) and subsequently the 400-layer generation—it remains uncertain whether this advantage in lateral scaling can be maintained to the same extent as today.

# Q: Is AI inference a temporary driver of NAND flash memory demand, as in the case of AI training, or is it a structural growth driver?

We view AI inference as a sustainable and structural driver of growth in NAND flash memory demand. For AI inference, NAND flash memory's performance and capacity are design variables that define user experience. This role is unlikely to change.

# Q: How long will NAND flash memory prices continue to rise?

We expect supply shortages to persist through 2027, as capacity expansion lags demand growth. Qoq price increases are likely to peak around 3Q 2027.

# UBSVIEW

NAND flash memory prices are likely to rise qoq for the next six quarters before peaking in Q3 2027 (about 1.5 years from now). By successfully focusing on horizontal miniaturisation technology, the company has established a competitive advantage in terms of bit cost, one that we expect to persist for several years.

# EVIDENCE

AI demand growth has benefited not only NAND flash memory companies but also HDD manufacturers, which occupy a lower tier of the storage hierarchy. Currently, few NAND flash memory or HDD companies expect demand from hyperscalers to decelerate.

On the supply side, companies in both the DRAM and NAND flash memory businesses are prioritising capacity expansion for DRAM. As a result, NAND flash memory supply is unlikely to grow in 2026 or 2027. Kioxia has similarly indicated that it intends to increase capex, but wafer shipment volumes are likely to decline.

# WHAT'S PRICED IN?

Based on our discussions with investors, most now think NAND flash memory prices will stay elevated. However, doubts persist about whether they can remain at such high levels. Compared to DRAM, NAND flash memory is more vulnerable to supply-demand imbalances.

# UPSIDE/DOWNSIDE SPECTRUM

![](images/220d211c7d42eb4a4ce0f1ec63a09c96634677c24d3e22afc1748e0dbd4c9836.jpg)

<details>
<summary>line</summary>

| Date       | Price     |
| ---------- | --------- |
| 28 May     | ¥61,280   |
| 28 May     | 104,000   |
| 28 May     | 79,000    |
| 28 May     | 40,000    |
| 28 May     | 11,264    |
| 28 May     | 16,837    |
| 28 May     | 19,454    |
| 28 May     | 5.3x      |
| 28 May     | 4.7x      |
| 28 May     | 3.6x      |
| 28 May     | +12 mo.   |
</details>

<table><tr><td>Value drivers</td><td>OP(FY3/28E)</td><td>NAND priceUSD$/GB(FY3/28E)</td><td>Bit costadvantage(FY3/28E)</td><td>EV/EBITDA(FY3/28E)</td><td>ROEFY3/28-FY3/31Eaverage</td><td>PBR(FY3/28E)</td></tr><tr><td>¥104,000 upside</td><td>¥11,062 bn</td><td>$0.35</td><td>20%</td><td>X 4</td><td>43%</td><td>X 5.3</td></tr><tr><td>¥79,000 base</td><td>¥8,991 bn</td><td>$0.30</td><td>10%</td><td>X 4</td><td>41%</td><td>X 4.7</td></tr><tr><td>¥40,000 downside</td><td>¥4,581 bn</td><td>$0.18</td><td>-5%</td><td>X 3</td><td>31%</td><td>X 3.6</td></tr></table>

Source: UBS estimates

# COMPANY DESCRIPTION

Kioxia is a leading global semiconductor manufacturer specializing in NAND flash memory and SSDs, holding a top-tier market share in this field. Originating from Toshiba's memory business, it operates as a dedicated manufacturer focused on the NAND business, offering products tailored for data centers and smart devices.

# PIVOTAL QUESTIONS

# Q: Can the company maintain its industry-leading NAND flash memory operating margin through 2027?

# UBSVIEW

We expect Kioxia to sustain industry-leading NAND margins versus key peers through CY26–27, supported by its lead in lateral (horizontal) scaling. However, beyond 2027—particularly with the transition to BICS10 (332 layers) and subsequently the 400-layer generation—it remains uncertain whether this advantage in lateral scaling can be maintained to the same extent as today.

# EVIDENCE

Key structural factors are high effective bit density, yield stability, sharing of facilities and technology through joint ventures, and competitors' shift in priority to DRAM (HBM) capex.

# WHAT'S PRICED IN?

Market participants appear to evaluate NAND flash memory competitiveness based primarily on superficial device specifications, such as vertical layer count and multilevel cell count. However, Kioxia's cost advantages per GB from lateral scaling and CBA architecture are likely not fully discounted as a factor differentiating the company from competitors.

# Low bit cost leads to high profitability

Kioxia consistently maintains the industry-leading operating margin per GB (Figure 1) owing primarily to its lower manufacturing cost per GB, or bit cost, than competitors' (Figure 2). Low bit cost underpins its industry-leading profitability.

Figure 1: NAND business: OPM   
![](images/f671856618f80a28c41b433aca58e350836942d71701ebdb5b031b58c8a86811.jpg)

<details>
<summary>line</summary>

| Fiscal Year | Kioxia | SK Hynix | Samsung | Micron |
|-------------|--------|----------|---------|--------|
| FY21        | 25%    | 10%      | 20%     | 5%     |
| FY22        | 35%    | 15%      | 25%     | 10%    |
| FY23        | -50%   | -50%     | -50%    | -50%   |
| FY24        | 45%    | 15%      | 25%     | 10%    |
| FY25        | 25%    | 10%      | 0%      | 0%     |
</details>

Source: Company data, UBS

Figure 2: NAND: Bit cost   
![](images/faec2db2f52c95e6ea3edc52dd3ba6908878e2a7c9b90cb7aac4051292bfef95.jpg)

<details>
<summary>line</summary>

| Fiscal Year | SK Hynix | Samsung | Micron | Kioxia |
|-------------|----------|---------|--------|--------|
| FY21        | 0.12     | 0.09    | 0.10   | 0.08   |
| FY22        | 0.10     | 0.08    | 0.09   | 0.07   |
| FY23        | 0.10     | 0.09    | 0.09   | 0.10   |
| FY24        | 0.07     | 0.06    | 0.08   | 0.05   |
| FY25        | 0.08     | 0.07    | 0.06   | 0.05   |
</details>

Source: Company data, UBS, Gartner

# Achieving bit density through lateral scaling

The most effective way to reduce NAND flash memory bit cost is to increase bit density per wafer in one of three ways:

1. Increasing vertical layer count (multi-layering)   
2. Increasing bits per cell (multi-levelling)   
3. Enhancing lateral bit density (lateral scaling)

Given that there is little difference among companies in terms of multi-layering and multi-levelling, the market uses these metrics as proxy indicators of competitiveness. In contrast, lateral scaling is less commonly used because it is more complex and involves trade-offs with multi-layering and multi-levelling. A plot of lateral bit density against total chip bit density (Figure 3) reveals Kioxia's advantage over competitors in terms of lateral scaling.

Figure 3: Lateral scaling vs bit density   
![](images/0649114cbf59f3c5b2344936c8ee2abad19b472398e9338c2d8f057904a35991.jpg)

<details>
<summary>scatter</summary>

| Material           | Bit Density (Gb/mm²) |
| ------------------ | -------------------- |
| KIOXIA/Sandisk BiCS FLASH | 10.00                |
| KIOXIA/Sandisk BiCS FLASH | 12.00                |
| KIOXIA/Sandisk BiCS FLASH | 18.00                |
| KIOXIA/Sandisk BiCS FLASH | 22.00                |
| KIOXIA/Sandisk BiCS FLASH | 29.00                |
| KIOXIA/Sandisk BiCS FLASH | 37.00                |
| Micron/intel       | 35.00                |
| Samsung V-NAND      | 29.00                |
| YMTC               | 20.00                |
| SK Hynix           | 15.00                |
</details>

Source: Company data, UBS, Gartner

# Lateral scaling inherently conflicts with multi-layering and multilevelling

To increase density through lateral scaling, memory hole diameters must be reduced and pitch tightened. The resulting increase in the aspect ratio significantly complicates hole etching. As multi-layering progresses, deeper holes lead to further increases in the aspect ratio, thereby making lateral scaling incompatible with multi-layering.

Additionally, reducing hole diameters can lead to lower read currents and greater variability, reducing design margins and complicating multi-levelling control. Lateral scaling is thus also incompatible with multi-levelling.

# Kioxia and Micron lead in terms of lateral scaling

Kioxia's and Micron's latest NAND flash memory products are ahead of competitors' in terms of lateral scaling, which is complex and not that compatible with multi-layering and multi-levelling. We attribute this lead to Kioxia's expertise in high-aspect-ratio etching, developed during Toshiba's trench-type DRAM era. Similar to NAND, trench-type DRAM requires high-aspect-ratio hole processing, which involves not only deep etching but also simultaneous optimisation of shape control, precision, and speed. Kioxia's accumulated expertise likely gives the company a competitive edge. Micron's ability to achieve lateral density comparable to Kioxia's may stem from its acquisition of Toshiba's trench-type DRAM plant and similar technologies.

# CUA/CBA: Not low-temperature processes but differentiated manufacturing

Another way to increase lateral density is CUA (CMOS under array), which places peripheral circuits beneath the array to improve area efficiency. Different companies may use different naming conventions, but their goals are the same.

However, as multi-layering progresses, the thermal processes used to form memory cells can damage the CMOS created earlier, leading to peripheral circuit degradation and, in turn, device performance deterioration and increased difficulty in controlling multilevelling. To address this issue, companies have developed low-temperature processes for CUA.

Starting with BiCS8, Kioxia has adopted CBA (CMOS direct bonding to array), whereby CMOS and arrays are fabricated on separate wafers and joined via hybrid bonding to prevent thermal damage.

Companies are cautious about adopting CBA because of such issues as reduced throughput and yield. Kioxia leveraged its technological expertise to achieve mass production, prompting competitors to follow suit.

# Increasing bit density without raising wafer costs

Bit cost does not decline on higher bit density alone; stable wafer costs are also necessary.

Kioxia has improved bit density across generations while keeping wafer manufacturing costs (per wafer) from rising (Figure 4). We estimate Samsung Electronics' cost per wafer at about \$4,000, Micron's and SK Hynix's at around \$6,000, and Kioxia's at a much lower \$2,000. With wafer costs less than half competitors', Kioxia's bit cost is also lower.

Kioxia's low wafer manufacturing costs probably result from comparing and selecting bit density improvement methods based on cost efficiency. Semiconductor wafer costs depend on capex and throughput. For example, increasing the number of layers in the next generation would reduce throughput and raise wafer manufacturing costs in the absence of countermeasures. Developing high-throughput equipment or using more equipment can boost throughput but also involves more capex and thus ultimately increases costs.

Kioxia carefully evaluates multi-layering, multi-levelling, and lateral scaling and keeps capex lower than competitors' so as to minimise the final bit cost (Figure 5).

Figure 4: Manufacturing cost per wafer   
![](images/161dfb82fc02c8775e2655e3a65c32716cd473b69de5a76283584a121f9c3349.jpg)

<details>
<summary>line</summary>

| Fiscal Year | SK Hynix | Micron | Samsung | Kioxia |
|-------------|----------|--------|---------|--------|
| FY20        | 3000     | 3000   | 2500    | 1800   |
| FY21        | 3500     | 3500   | 2700    | 2200   |
| FY22        | 4000     | 3800   | 2600    | 1900   |
| FY23        | 5500     | 6800   | 3500    | 2800   |
| FY24        | 5000     | 5000   | 4500    | 2500   |
| FY25        | 6800     | 6500   | 4800    | 3000   |
</details>

Source: Company data, UBS, Gartner

Figure 5: Capex required per TB increase (3-yr cumulative)   
![](images/2d59910456cd5b8360ac6f8376bd97248b78c837765409566f5c5abe0ecca1b8.jpg)

<details>
<summary>line</summary>

| Year | Samsung | SK Hynix | Micron | Kioxia+ | SanDisk |
|------|---------|----------|--------|---------|---------|
| CY13 | 400     | 850      | 350    | 350     | 350     |
| 

[中间内容因长度限制已省略]

ed Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS Securities LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS Securities LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

# Credit Suisse Wealth Management Disclaimer

This disclaimer must be read in conjunction with "Risk information" and "Important Information About Sustainable Investing Strategies" sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of Credit Suisse Wealth Management. Your personal data will be processed in accordance with the Credit Suisse privacy statement accessible at your domicile through the official Credit Suisse website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local Credit Suisse entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by Credit Suisse Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. Credit Suisse Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/80cf6c72f049618de08567abd277fbebd22cea18d25a74f64ebd0e6c24d3b922.jpg)
"""
