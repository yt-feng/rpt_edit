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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`JPM`。标题格式建议：`# JPM：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
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
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JPM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# China: May inflation roughly matched expectations

- May inflation broadly met expectations: CPI stayed soft while PPI continued to be firm, at a slower pace.  
- CPI inched up 0.1%m/m sa, as firmer communications/entertainment prices were offset by ongoing food-price deflation.  
- PPI drivers were industrial upgrade/AI demand, reinforced by seasonal strength in coal/cooling-linked categories; oil-price swings capped gains.  
- AI-related cost pass-through is broadening into upstream semis and downstream electronics, adding a more durable inflation tailwind.  
- PPI has some upside risk but excess capacity and weak demand limit pass-through, leaving CPI benign. GDP deflator may turn positive in 2Q.

China's May inflation was broadly in line with expectations. The PPI sequential upturn continued (albeit at a slower pace), lifted by industrial upgrading and AI-driven compute demand, plus seasonal summer demand for coal, cooling appliances and power, while global oil price swings capped gains. CPI remained soft as firming transport/communication/entertainment was offset by food deflation.

Headline CPI stabilized at 1.2% oya (JPM and Bloomberg consensus: 1.3%), with a 0.1%m/m sa uptick and broadly muted moves across major components. Transport/communication rose 0.2%m/m sa after a 2.0% monthly average run rate over the prior two months: passenger cars and vehicle fuel fell 0.4%m/m nsa and 0.3%, while communication tools jumped 1.5% (or 1.8%m/m sa by our estimates) as AI-related memory tightness fed through. NBS flagged mobile phones and tablets, up 1.6% and 1.1%. Education/culture/entertainment rose 0.2%m/m sa on Labor holiday tourism. Food deflation persisted, led by fresh vegetables and pork. Misc. goods/services (incl. gold jewelry) slipped another 0.2%m/m, though the 9.9% oya elevated annual rate still added 0.3% pt to headline CPI. Ex-food/energy, core CPI eased to 1.1% oya (flat in %m/m), while service CPI moderated to 0.8% oya on a 0.1%m/m sa uptick.

PPI extended its upturn, rising 0.8%m/m sa or 3.9%oya (JPM: 3.8%oya; consensus: 3.9%). Relative to last month, the lift came from industrial upgrading and AI-driven compute demand, pushing up metals, electrical machinery and electronics prices. The NBS highlighted tin and copper smelting were up 4.8%m/m nsa and 3.1%, while IC packaging/testing and external storage devices/components rose 2.9% and 1.9%. Seasonal “summer peak” demand also supported coal, cooling appliances and power. Gains were partly capped by global oil price swings that pulled upstream oil and refining prices lower and cooled oil-linked chemicals. On the over-year-ago basis, after the prior two-month surge, strength was still led by non-ferrous metal, coal and energy-related sectors, offset by drags from non-metal minerals, utilities, autos and food processing. Producer-goods PPI rose 5.2%oya (1.1%m/m sa), while consumer-goods PPI stayed in deflation territory at -0.8%oya (+0.2%m/m sa) amid weak demand and limited pass-through.

As the Middle East developments remain fluid, our commodity strategists' base case continues to assume that the Strait of Hormuz reopens in June. Even so, normalization will likely lag: repairs to oil/LNG infrastructure, lingering logistics frictions, and

## Emerging Markets Asia, Economic and Policy Research

## Tingting Ge

(852) 2800-0143

tingting.ge@JPM.com

## Feng Zhu

(852) 2800 1745

feng.zhu@JPM.com

## Jiayi Li

(852) 2800-5229

jiayi.c.li@JPM.com

## Tongfang Yuan

(852) 2800-0085

tongfang.yuan@JPM.com

JPM Chase Bank, N.A., Hong Kong Branch

precautionary stockpiling could keep prices elevated, above pre-conflict levels, into the year-end. Contingency steps (greater domestic coal use, power-demand management) can cushion the oil supply disruption shock, but substitution is only partial and seasonally constrained into the summer peak, as reflected in rising coal mining/washing, household air-conditioner manufacturing, and power supply costs.

Pass-through from AI-related memory inflation is broadening. As hyperscaler capex extends beyond data-center buildouts into upstream enablers and smaller-cap players, global semiconductor supply has tightened further and memory price pressure has persisted. Against that backdrop, China's industrial upgrading and $\mathrm{AI + }$ push, together with its role in the tech supply chain, are adding to the lift in IC and electronics producer and retail prices. That said, even as the energy shock fades, the AI-related inflation impulse could prove more durable: the global tech upcycle remains intact, and China's industrial upgrade and $\mathrm{AI + }$ initiatives are multi-year blueprints.

These forces point to some upside risk to PPI inflation, though excess capacity elsewhere and weak consumer demand should cap the upside, keeping CPI more anchored. After narrowing to -0.06% oya in 1Q, the GDP deflator should turn positive in 2Q, pausing a three-year deflation stretch. This is supportive of the PBOC's price-recovery mandate and reflation expectations. Still, with core CPI muted around 1% oya, the energy shock weighing on near-term activity, tariff uncertainty resurfacing, and a more hawkish Fed tilt, the PBOC will likely stay on hold for now. A cut could be back on the table in 2H if growth downside risks persist.

Consumer price indices  
percent change

<table><tr><td></td><td>2025</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td></tr><tr><td colspan="6">Headline CPI</td></tr><tr><td>%oya</td><td>0.0</td><td>1.3</td><td>1.0</td><td>1.2</td><td>1.2</td></tr><tr><td>%m/m, sa</td><td></td><td>0.7</td><td>0.2</td><td>0.2</td><td>0.1</td></tr><tr><td colspan="6">Food CPI</td></tr><tr><td>%oya</td><td>-1.4</td><td>1.7</td><td>0.3</td><td>-1.6</td><td>-1.7</td></tr><tr><td>%m/m, sa</td><td></td><td>0.6</td><td>-0.6</td><td>-1.0</td><td>-0.2</td></tr><tr><td colspan="6">Non-food CPI</td></tr><tr><td>%oya</td><td>0.4</td><td>1.3</td><td>1.2</td><td>1.8</td><td>1.9</td></tr><tr><td>%m/m, sa</td><td></td><td>0.7</td><td>0.1</td><td>0.4</td><td>0.2</td></tr><tr><td colspan="6">Core CPI</td></tr><tr><td>%oya</td><td>0.8</td><td>1.8</td><td>1.1</td><td>1.2</td><td>1.1</td></tr><tr><td>%m/m, sa</td><td></td><td>0.8</td><td>-0.4</td><td>0.1</td><td>0.0</td></tr></table>

Source: NBS; JPM

Producer prices  
percent change

<table><tr><td></td><td>2025</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td></tr><tr><td colspan="6">Producer (NBS)</td></tr><tr><td>%oya</td><td>-2.6</td><td>-0.9</td><td>0.5</td><td>2.8</td><td>3.9</td></tr><tr><td>%m/m, sa</td><td></td><td>0.4</td><td>1.0</td><td>1.7</td><td>0.8</td></tr><tr><td colspan="6">Producer goods</td></tr><tr><td>%oya</td><td>-3.0</td><td>-0.7</td><td>1.0</td><td>3.8</td><td>5.2</td></tr><tr><td>%m/m, sa</td><td></td><td>0.5</td><td>1.2</td><td>2.0</td><td>1.1</td></tr><tr><td colspan="6">Consumer goods</td></tr><tr><td>%oya</td><td>-1.5</td><td>-1.6</td><td>-1.3</td><td>-1.0</td><td>-0.8</td></tr><tr><td>%m/m, sa</td><td></td><td>0.0</td><td>0.0</td><td>0.1</td><td>0.2</td></tr></table>

Source: NBS, JPM

China: CPI trends  
![](images/d9083c7a45d40785917ae044a627b7a9909c64fd54c7b7ca1cac9336147eaf3e.jpg)

<details>
<summary>line chart</summary>

| Year | Headline CPI | Core CPI |
|------|--------------|----------|
| 15   | ~1.0         | ~1.5     |
| 16   | ~1.8         | ~1.7     |
| 17   | ~2.0         | ~1.8     |
| 18   | ~2.5         | ~2.0     |
| 19   | ~2.0         | ~1.8     |
| 20   | ~5.0         | ~1.5     |
| 21   | ~-0.5        | ~0.5     |
| 22   | ~2.5         | ~1.0     |
| 23   | ~2.0         | ~0.8     |
| 24   | ~-0.5        | ~1.0     |
| 25   | ~0.5         | ~0.8     |
| 26   | ~1.5         | ~1.0     |
</details>

China PPI: consumer vs. producer  
![](images/da841a1316577c6bb6bcb8c81eaff9603c3e356ce813e778a5679ac538cccfe5.jpg)

<details>
<summary>line chart</summary>

| Year | Producer PPI | Consumer PPI |
|------|--------------|--------------|
| 15   | -7.0         | -3.0         |
| 16   | -8.0         | -3.0         |
| 17   | 12.0         | -3.0         |
| 18   | 7.0          | -3.0         |
| 19   | 2.0          | -3.0         |
| 20   | -3.0         | -3.0         |
| 21   | 12.0         | -3.0         |
| 22   | 12.0         | -3.0         |
| 23   | -3.0         | -3.0         |
| 24   | -8.0         | -3.0         |
| 25   | -3.0         | -3.0         |
| 26   | 6.0          | -3.0         |
</details>

China energy CPI and global oil price  
![](images/67d4303cebff366cd520906800a86b58fd6dd57416bc8cf8607de9cc0801e2a4.jpg)

<details>
<summary>line chart</summary>

| Year | Crude oil price | Energy |
|------|-----------------|--------|
| 19   | ~0.0            | ~0.0   |
| 20   | ~0.0            | ~-0.4  |
| 21   | ~1.6            | ~0.8   |
| 22   | ~1.2            | ~1.0   |
| 23   | ~0.0            | ~-0.4  |
| 24   | ~0.0            | ~0.0   |
| 25   | ~0.0            | ~-0.4  |
| 26   | ~0.5            | ~0.0   |
</details>

China: Miscellaneous CPI vs. gold prices  
![](images/5f7a0c2e7aceeec1f16db4e001f4656f6905d8ac9b225a0bce130f28e955cc6d.jpg)

<details>
<summary>line chart</summary>

| Year | Gold | CPI: Miscellaneous goods/services (rhs) |
|------|------|----------------------------------------|
| 2017 | -5   | 15                                     |
| 2018 | 10   | 5                                      |
| 2019 | -10  | 10                                     |
| 2020 | 30   | 15                                     |
| 2021 | 20   | 5                                      |
| 2022 | -5   | -10                                    |
| 2023 | 5    | 5                                      |
| 2024 | 10   | 10                                     |
| 2025 | 40   | 15                                     |
| 2026 | 75   | 24                                     |
</details>

Source: IMF, Haver, JPM

China's inflation dynamics  
![](images/77a13d5bf462a1c720121e5a4912b595b81f1837f7bf1f785be24cf95da474b8.jpg)

<details>
<summary>line chart</summary>

| Year | CPI  | PPI  |
|------|------|------|
| 2016 | ~2   | ~-6  |
| 2017 | ~3   | ~8   |
| 2018 | ~4   | ~5   |
| 2019 | ~3   | ~3   |
| 2020 | ~5   | ~-4  |
| 2021 | ~0   | ~9   |
| 2022 | ~3   | ~14  |
| 2023 | ~2   | ~-6  |
| 2024 | ~1   | ~-3  |
| 2025 | ~0   | ~-4  |
| 2026 | ~1   | ~4   |
</details>

PPI breakdown  
![](images/99747d750b1d20456909a1ccd741e4f9e50d36f216da420b4df50f21f9109b76.jpg)

<details>
<summary>line chart</summary>

| Year | Producer goods (%3m/3m saar) | Consumer goods (%3m/3m saar) |
|------|-------------------------------|-------------------------------|
| 07   | ~15                           | ~10                           |
| 08   | ~20                           | ~15                           |
| 09   | ~-20                          | ~-10                          |
| 10   | ~10                           | ~5                            |
| 11   | ~20                           | ~15                           |
| 12   | ~-5                           | ~-5                           |
| 13   | ~-10                          | ~-5                           |
| 14   | ~-5                           | ~-5                           |
| 15   | ~-10                          | ~-5                           |
| 16   | ~-5                           | ~-5                           |
| 17   | ~15                           | ~10                           |
| 18   | ~10                           | ~5                            |
| 19   | ~5                            | ~0                            |
| 20   | ~-5                           | ~-5                           |
| 21   | ~20                           | ~15                           |
| 22   | ~15                           | ~10                           |
| 23   | ~-5                           | ~-5                           |
| 24   | ~-10                          | ~-5                           |
| 25   | ~-5                           | ~-5                           |
| 26   | ~15                           | ~10                           |
</details>

China CPI: transport & communication vs. comm. tools  
![](images/bae6375424f3ac2c1b715cc416021a5a71ac36a3f156c7347b2ff61ffa8d8905.jpg)

<details>
<summary>line chart</summary>

| Year | Transport & Communication | Comm. Tools |
|------|---------------------------|-------------|
| 2021 | ~0.5                      | ~0.5        |
| 2022 | ~-1.5                     | ~-1.5       |
| 2023 | ~-1.0                     | ~-1.0       |
| 2024 | ~-0.5                     | ~-0.5       |
| 2025 | ~-1.0                     | ~-1.0       |
| 2026 | ~3.0                      | ~2.0        |
</details>

China: Headline CPI, food and nonfood CPI  
![](images/6a589fe4f6b5dc23b1b8e32449529d33ba5b77dcc83f431fc3a6ad562a54882c.jpg)

<details>
<summary>line chart</summary>

| Year | Headline CPI | Nonfood CPI |
|------|--------------|-------------|
| 19   | ~1.5         | ~1.0        |
| 20   | ~5.5         | ~1.5        |
| 21   | ~-1.0        | ~-1.5       |
| 22   | ~2.0         | ~2.5        |
| 23   | ~1.5         | ~1.0        |
| 24   | ~-1.5        | ~-1.0       |
| 25   | ~0.5         | ~0.0        |
| 26   | ~1.0         | ~1.5        |
</details>

![](images/80e77bbd1fe8079be2cba84ab7bcf75e5e5f446a9295a9af0c4a39507f102ded.jpg)

<details>
<summary>line chart</summary>

| Year | Healthcare and medicines | Transportation and communication | Recreation, education and cultural services |
|------|---------------------------|------------------------------------|---------------------------------------------|
| 2019 | ~100                      | ~100                               | ~100                                        |
| 2020 | ~100                      | ~100                               | ~100                                        |
| 2021 | ~100                      | ~100                               | ~100                                        |
| 2022 | ~100                      | ~105                               | ~105                                        |
| 2023 | ~100                      | ~105                               | ~105                                        |
| 2024 | ~100                      | ~105                               | ~110                                        |
| 2025 | ~100                      | ~105                               | ~110                                        |
| 2026 | ~100                      | ~105                               | ~110                                        |
</details>

![](images/773d998da976fdfbc12e50b6b67f942962bffcaa5fda79ecb05624c9ec5eb662.jpg)

<details>
<summary>line chart</summary>

| Year | Consumer confidence - income | Consumer confidence - employment |
|------|-------------------------------|----------------------------------|
| 2018 | ~125                          | ~125                             |
| 2019 | ~120                          | ~120                             |
| 2020 | ~130                          | ~135                             |
| 2021 | ~125                          | ~125                             |
| 2022 | ~80                           | ~100                             |
| 2023 | ~90                           | ~100                             |
| 2024 | ~75                           | ~95                              |
| 2025 | ~70                           | ~95                              |
| 2026 | ~75                           | ~95                              |
</details>

![](images/a7c24a09cf92624c9ba112285c9386c5b38087fdba437ba174c3d20018f204a3.jpg)

<details>
<summary>line chart</summary>

| Year | China PPI | Global commodity price (ex. gold) |
|------|-----------|-----------------------------------|
| 12   |           | -15                               |
| 13   |           | -10                               |
| 14   |           | -5                                |
| 15   |           | -15                               |
| 16   |           | -30                               |
| 17   |           | 40                                |
| 18   |           | 30                                |
| 19   |           | 20                                |
| 20   |           | -30                               |
| 21   |           | 75                                |
| 22   |           | 60                                |
| 23   |           | -30                               |
| 24   |           | -10                               |
| 25   |           | 0                                 |
| 26   |           | 30                                |
</details>

![](images/34640eda303a9d50b897a2897f8ed487481bc971172d54ba52f538fc875439e1.jpg)

<details>
<summary>line chart</summary>

| Year | Pork prices - level | Pork prices - %oya change |
|------|---------------------|----------------------------|
| 2018 | ~100                | ~-40                       |
| 2019 | ~120                | ~-20                       |
| 2020 | ~220                | ~120                       |
| 2021 | ~180                | ~-40                       |
| 2022 | ~100                | ~-60                       |
| 2023 | ~160                | ~-20                       |
| 2024 | ~120                | ~-40                       |
| 2025 | ~100                | ~-60                       |
| 2026 | ~80                 | ~-80                       |
</details>

![](images/f3915667c0935777fddf919ea45b0f2feb22965c1082d16a98d76f1a92888e0b.jpg)

<details>
<summary>line chart</summary>

| Year | Consumer goods | Ferrous metal processing | Petrol, coal and other fuel processing | Non ferrous metal processing |
|------|----------------|--------------------------|----------------------------------------|------------------------------|
| 18   | ~10            | ~10                      | ~10                                    | ~10                          |
| 19   | ~20            | ~15                      | ~5                                     | ~5                           |
| 20   | ~0             | ~0                       | ~0                                     | ~0                           |
| 21   | ~30            | ~40                      | ~30                                    | ~30                          |
| 22   | ~50            | ~55                      | ~40                                    | ~40                          |
| 23   | ~-20           | ~-10                     | ~-10                                   | ~-10                         |
| 24   | ~-5            | ~-5                      | ~-5                  

[中间内容因长度限制已省略]

dates may be provided on companies/industries based on company-specific developments or announcements, market

conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 10 Jun 2026 12:44 PM HKT

Disseminated 10 Jun 2026 01:03 PM HKT
"""
