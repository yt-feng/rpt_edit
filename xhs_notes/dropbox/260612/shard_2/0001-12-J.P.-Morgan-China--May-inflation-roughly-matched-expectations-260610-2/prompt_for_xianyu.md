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
| 12   |           | -15                   

[中间内容因长度限制已省略]

rmance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 10 Jun 2026 12:44 PM HKT

Disseminated 10 Jun 2026 01:03 PM HKT
"""
