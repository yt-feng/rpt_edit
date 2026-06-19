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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`摩根斯坦利`。标题格式建议：`# 摩根斯坦利：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
Investor Presentation | Asia Pacific

Narrowing the K-shaped Recovery Gap

MS ASIA LIMITED+

Kathleen Oh

Chief Korea/Taiwan Economist

Kathleen.Oh@morganstanley.com

+852 2848-7340

Asia Summer School 2026

![](images/cbefdb185f39941f5c01972f7bd1b31b1f5828703041b7f937ca96fd2e7d9f60.jpg)

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

Korea: Macro Overview

## From K-shaped Recovery to a Broad-based Rebound

We see the Korean economy recovering on a broader-based rebound. Unprecedented resilience in tech exports coupled with a faster-than-expected consumption recovery look set to close the negative output gap two quarters earlier than our previous forecast. We see above-potential growth for the next two years and total four hikes by the BoK over one year from July 2026.

We expect a broad-based rebound in GDP growth to 2.8%Y in 2026 vs. 1.1% in 2025  
![](images/af85b8cff64a531581161ca0526d0b790e0fa25e29d8d3444bf8af96cee8fa06.jpg)

<details>
<summary>bar-line hybrid</summary>

Korea: Annual PP contribution to GDP by expenditure account
| Year | Net exports (%) | Government expenditure (%) | Real GDP, %Y (%) |
|---|---|---|---|
| 2021 | 1.8 | 0.6 | 4.6 |
| 2022 | 1.9 | 0.5 | 2.7 |
| 2023 | 1.0 | -0.1 | 1.5 |
| 2024 | 0.5 | 0.2 | 2.0 |
| 2025 | 0.6 | -0.8 | 1.0 |
| 2026F | 0.4 | 0.1 | 2.8 |
| 2027F | 0.3 | 0.1 | 2.2 |
MSe
</details>

Source: BoK, MS forecasts

## Key takeaways

- Korea set to move from K-shaped recovery to a broad-based rebound: Growth likely to jump 2.8% in 2026 vs 1.1% in 2025 before stabilizing to 2.2% in 2027.  
- CPI inflation faces upward pressure to 2.5%Y, not only from elevated oil prices but from a faster-than-expected consumption recovery among households.  
- With ample tax income amid strong corporate earnings, income and securities transaction taxes, the government could hand down an extra budget in 2H26.  
- With an above-potential growth outlook through 2027, we see the BoK entering tightening territory above the neutral range; terminal rate at $3.50\%$ by 1H27e.  
- The risk balance is tilted to the upside with the fiscal windfall expected from the tech exporter outperformance.

## Growth to See Above-Potential Level Rebound to 2.8%Y in 2026

Growth contribution from domestic and external demand to show a balanced dynamic  
![](images/70b6481d8b191d663fcbe7add545041512e1be3e22e8692cac49ea75db8076f0.jpg)

<details>
<summary>bar-line hybrid</summary>

Annual PP contribution to GDP by domestic vs external demand
| Year | Domestic Demand (%) | Net Exports (%) | Statistical Discrepancy (%) | Real GDP, %Y (%) |
|---|---|---|---|---|
| 2021 | 4.1 | 0.3 | 0.5 | 4.6 |
| 2022 | 2.7 | 0.1 | 0.0 | 2.8 |
| 2023 | 1.4 | 0.1 | 0.0 | 1.6 |
| 2024 | 0.2 | 1.6 | 0.1 | 2.0 |
| 2025 | 0.6 | 0.3 | 0.1 | 1.0 |
| 2026F | 1.2 | 1.4 | 0.1 | 2.8 |
| 2027F | 1.0 | 1.3 | 0.0 | 2.3 |
</details>

Unfavorable base to kick-in from 2Q26 before a rebound in 2H26  
![](images/416f57147dec8b3425bf61a6bbf09be84376b57ed067d64a1951c9f659437df8.jpg)

<details>
<summary>bar-line hybrid</summary>

| Quarter | Manufacturing (%) | Electricity, Gas & Water Supply (%) | Construction (%) | Services (%) | Others (%) | Real GDP, %Y |
| --- | --- | --- | --- | --- | --- | --- |
| 1Q22 | 1.1 | 0.1 | 0.0 | 1.8 | -0.4 | 3.4 |
| 2Q22 | 1.0 | 0.1 | 0.0 | 1.9 | -0.5 | 3.0 |
| 3Q22 | 1.1 | 0.1 | 0.0 | 2.0 | -0.4 | 3.5 |
| 4Q22 | 1.1 | 0.1 | 0.0 | 1.7 | -0.6 | 3.4 |
| 1Q23 | -0.8 | -0.3 | -0.2 | 1.6 | -1.3 | 1.3 |
| 2Q23 | -0.5 | -0.1 | -0.1 | 1.4 | -0.5 | 1.2 |
| 3Q23 | 0.3 | 0.1 | -0.1 | 1.4 | -0.4 | 1.5 |
| 4Q23 | 1.8 | 0.1 | -0.3 | 1.7 | -0.5 | 2.2 |
| 1Q24 | 1.6 | 0.1 | -0.1 | 1.5 | -0.4 | 3.4 |
| 2Q24 | 1.4 | 0.1 | -0.2 | 1.3 | -0.4 | 2.3 |
| 3Q24 | 1.3 | 0.1 | -0.3 | 1.9 | -0.5 | 1.4 |
| 4Q24 | 0.5 | 0.1 | -0.3 | 1.3 | -0.5 | 1.1 |
| 1Q25 | -0.5 | -0.1 | -0.4 | 0.5 | -0.6 | -0.1 |
| 2Q25 | -0.7 | -0.1 | -0.5 | 1.3 | -0.6 | 0.5 |
| 3Q25 | 0.9 | 0.1 | -0.4 | 1.7 | -0.6 | 1.8 |
| 4Q25 | 0.5 | 0.1 | -0.3 | 2.1 | -0.6 | 1.6 |
| 1Q26 | 1.6 | 0.1 | -0.2 | 2.7 | -0.6 | 3.7 |
</details>

Source: BoK, MS forecasts

## Exports: A New Cycle High

Korea's May trade recorded highest monthly export value, despite rising energy imports  
![](images/137d0acd6db4c8877bf4657933357f66873bf3e8637cf197349076f0ddcce362.jpg)

<details>
<summary>line chart</summary>

| Year | Trade balance, USD bn (RHS) | Exports, 3mma | Imports, 3mma |
|------|-----------------------------|---------------|---------------|
| 19   | ~0                          | ~0            | ~0            |
| 20   | ~-5                         | ~-10          | ~-5           |
| 21   | ~10                         | ~40           | ~30           |
| 22   | ~-10                        | ~20           | ~25           |
| 23   | ~-15                        | ~-10          | ~-5           |
| 24   | ~-5                         | ~10           | ~5            |
| 25   | ~0                          | ~5            | ~0            |
| 26   | ~15                         | ~30           | ~10           |
</details>

Both tech and non-tech momentum accelerating  
![](images/3092e24c7b828f7ed2efed100b2058917b14d5c50ca5fed3a493a91a67ae1f01.jpg)

<details>
<summary>bar chart</summary>

Per-day exports momentum past 3 months, %Y
| Category | Mar-26 (%) | Apr-26 (%) | May-26 (%) |
| :--- | :--- | :--- | :--- |
| Per-day exports, %Y | 44 | 48 | 60.9 |
| Exports excl. vessels | 45.5 | 47.5 | 62.2 |
| Exports excl. semis | 15.5 | 16 | 22.2 |
| Exports excl. vessels and semis | 16 | 15 | 22.5 |
</details>

Source: KITA, MS

## Rising Global Demand for HBM and Generic DRAM

Exports to rise significantly on AI-driven demand  
![](images/e375e6e7feee7d3a255d1906707ae1366d5e7e4ba5b432fac1b011c247a5b3cd.jpg)

<details>
<summary>line chart</summary>

| Quarter | GDP: Real exports, %Y | Exports volume, %Y |
| ------- | --------------------- | ------------------ |
| 3Q10    | ~13                   | ~23                |
| 4Q10    | ~22                   | ~15                |
| 1Q11    | ~10                   | ~8                 |
| 2Q11    | ~5                    | ~6                 |
| 3Q11    | ~3                    | ~4                 |
| 4Q11    | ~2                    | ~3                 |
| 1Q12    | ~1                    | ~2                 |
| 2Q12    | ~0                    | ~1                 |
| 3Q12    | ~-1                   | ~0                 |
| 4Q12    | ~-2                   | ~-1                |
| 1Q13    | ~-3                   | ~-2                |
| 2Q13    | ~-4                   | ~-3                |
| 3Q13    | ~-5                   | ~-4                |
| 4Q13    | ~-6                   | ~-5                |
| 1Q14    | ~-7                   | ~-6                |
| 2Q14    | ~-8                   | ~-7                |
| 3Q14    | ~-9                   | ~-8                |
| 4Q14    | ~-10                  | ~-9                |
| 1Q15    | ~-11                  | ~-10               |
| 2Q15    | ~-12                  | ~-11               |
| 3Q15    | ~-13                  | ~-12               |
| 4Q15    | ~-14                  | ~-13               |
| 1Q16    | ~-15                  | ~-14               |
| 2Q16    | ~-16                  | ~-15               |
| 3Q16    | ~-17                  | ~-16               |
| 4Q16    | ~-18                  | ~-17               |
| 1Q17    | ~-19                  | ~-18               |
| 2Q17    | ~-20                  | ~-19               |
| 3Q17    | ~-21                  | ~-20               |
| 4Q17    | ~-22                  | ~-21               |
| 1Q18    | ~-23                  | ~-22               |
| 2Q18    | ~-24                  | ~-23               |
| 3Q18    | ~-25                  | ~-24               |
| 4Q18    | ~-26                  | ~-25               |
| 1Q19    | ~-27                  | ~-26               |
| 2Q19    | ~-28                  | ~-27               |
| 3Q19    | ~-29                  | ~-28               |
| 4Q19    | ~-30                  | ~-29               |
| 1Q20    | ~-31                  | ~-30               |
| 2Q20    | ~-32                  | ~-31               |
| 3Q20    | ~-33                  | ~-32               |
| 4Q20    | ~-34                  | ~-33               |
| 1Q21    | ~-35                  | ~-34               |
| 2Q21    | ~-36                  | ~-35               |
| 3Q21    | ~-37                  | ~-36               |
| 4Q21    | ~-38                  | ~-37               |
| 1Q22    | ~-39                  | ~-38               |
| 2Q22    | ~-40                  | ~-39               |
| 3Q22    | ~-41                  | ~-40               |
| 4Q22    | ~-42                  | ~-41               |
| 1Q23    | ~-43                  | ~-42               |
| 2Q23    | ~-44                  | ~-43               |
| 3Q23    | ~-45                  | ~-44               |
| 4Q23    | ~-46                  | ~-45               |
| 1Q24    | ~-47                  | ~-46               |
| 2Q24    | ~-48                  | ~-47               |
| 3Q24    | ~-49                  | ~-48               |
| 4Q24    | ~-50                  | ~-49               |
| 1Q25    | ~-51                  | ~-50               |
| 2Q25    | ~-52                  | ~-51               |
| 3Q25    | ~-53                  | ~-52               |
| 4Q25    | ~-54                  | ~-53               |
| 1Q26    | ~-55                  | ~-54               |
| 2Q26    | ~-56                  | ~-55               |
| 3Q26    | ~-57                  | ~-56               |
| 4Q26    | ~-58                  | ~-57               |
| MSe     | -                     | -                  |
</details>

Bit shipments expected to maintain two-digit growth  
![](images/59c82c62a78674ac1efb55f0fe0738421a6600ee61acec7602985f6078511978.jpg)

<details>
<summary>bar-line hybrid</summary>

Exports and semis bit shipments forecast trend
| Quarter | Real export growth, %Y (%) | Semis bit shipments trend (1Gb eq, mn) (RHS) |
| :--- | :--- | :--- |
| 1Q20 | 5.6 | 58 |
| 2Q20 | -12.4 | 9.0 |
| 3Q20 | -1.2 | 7.0 |
| 4Q20 | 1.6 | 14.0 |
| 1Q21 | 6.8 | 16.0 |
| 2Q21 | 23.6 | 45.0 |
| 3Q21 | 7.6 | 10.0 |
| 4Q21 | 7.6 | 8.0 |
| 1Q22 | 7.6 | 5.0 |
| 2Q22 | 5.4 | -2.0 |
| 3Q22 | -2.4 | 1.0 |
| 4Q22 | -0.8 | -4.0 |
| 1Q23 | 0.4 | 3.0 |
| 2Q23 | 3.4 | 10.0 |
| 3Q23 | 11.0 | 30.0 |
| 4Q23 | 8.8 | 45.0 |
| 1Q24 | 8.8 | 18.0 |
| 2Q24 | 6.4 | 5.0 |
| 3Q24 | 3.4 | -18.0 |
| 4Q24 | 1.6 | -28.0 |
| 1Q25 | 4.4 | 10.0 |
| 2Q25 | 6.8 | 20.0 |
| 3Q25 | 4.4 | 30.0 |
| 4Q25 | 10.0 | 45.0 |
| 1Q26 | - | 10.0 |
| 2Q26 | - | 15.0 |
| 3Q26 | - | 18.0 |
| 4Q26 | - | 25.0 |
| 1Q27 | - | 30.0 |
| 2Q27 | - | 35.0 |
| 3Q27 | - | 38.0 |
</details>

Source: BoK, MS forecasts

## Semis Now 40% of Total Exports; Non-Tech Recovery Since End-2025

Tech-related goods continue to remain the key contributors to Korea's exports  
![](images/1fdb0c8013fb30e1cc5796f3d5adaf648425ae0356ed2d6236273d169af4dab5.jpg)

<details>
<summary>bar-line hybrid</summary>

Korea: Contribution to Export Growth by Product (pp)
| Month | Mobile Phones | Displays | General Machinery | Others | Computers | Petroleum Products | Autos | Semiconductors | Petrochemicals | Ships | Total Exports |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Feb-24 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| May-24 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 15.0 |
| Aug-24 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 12.5 |
| Nov-24 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 5.5 |
| Feb-25 | -5.5 | -5.5 | -5.5 | -5.5 | -5.5 | -5.5 | -5.5 | -5.5 | -5.5 | -5.5 | -13.5 |
| May-25 | -1.5 | -1.5 | -1.5 | -1.5 | -1.5 | -1.5 | -1.5 | -1.5 | -1.5 | -1.5 | -1.5 |
| Aug-25 | -1.5 | -1.5 | -1.5 | -1.5 | -1.5 | -1.5 | -1.5 | -1.5 | -1.5 | -1.5 | 12.5 |
| Nov-25 | -1.5 | -1.5 | -1.5 | -1.5 | -1.5 | -1.5 | -1.5 | -1.5 | -1.5 | -1.5 | 12.5 |
| Feb-26 | 2.5 | 2.5 | 2.5 | 2.5 | 2.5 | 2.5 | 2.5 | 2.5 | 2.5 | 2.5 | 33.7 |
| May-26 | 3.75 | 3.75 | 3.75 | 3.75 | 3.75 | 3.75 | 3.75 | 3.75 | 3.75 | 3.75 | 49.8 |
The chart displays a stacked bar chart with a line overlay showing the total exports over time.
</details>

Persistent energy market volatility drives crude petroleum and coal import growth  
![](images/56731509fee24cdcddfc0fd25dbc4d5928f749fc6a49b386148a94ea96b0e1c8.jpg)

<details>
<summary>line chart</summary>

| Month    | SA, Dec-24=100, 3mma | SA, Dec-24=100 |
| -------- | --------------------- | -------------- |
| May-26   | 112                   | 110            |
</details>

Source: KITA, MS

## Tech Supercycle Benefitting Capex Activities

Unprecedented tech super-cycle benefits exports  
![](images/e1c55a43906dcc7ce4cb665b86ce5f564182ad42aa8bdf22cc9c996e8521f748.jpg)

<details>
<summary>line chart</summary>

| Year | Korea semis exports, %Y | Philadelphia semis index (RHS) |
|------|--------------------------|----------------------------------|
| 15   | ~10                      | ~800                             |
| 16   | ~-20                     | ~700                             |
| 17   | ~50                      | ~600                             |
| 18   | ~70                      | ~500                             |
| 19   | ~-30                     | ~400                             |
| 20   | ~-40                     | ~300                             |
| 21   | ~30                      | ~200                             |
| 22   | ~40                      | ~100                             |
| 23   | ~-50                     | ~-200                            |
| 24   | ~60                      | ~500                             |
| 25   | ~-10                     | ~400                             |
| 26   | ~170                     | ~9000                            |
</details>

Capex and capital goods imports ramped up  
![](images/dfd550c90151537d50b1c072b6ce6690fe48e3c503cdcbcc6d25b246b590685a.jpg)

<details>
<summary>line chart</summary>

| Year | Index of equipment investment estimation, %Y 6M-trailing | Capital goods imports, %Y (RHS) |
|------|----------------------------------------------------------|-------------------------------|
| 17   | ~5                                                       | ~15                           |
| 18   | ~18                                                      | ~25                           |
| 19   | ~-15                                                     | ~-20                          |
| 20   | ~5                                                       | ~10                           |
| 21   | ~15                                                      | ~30                           |
| 22   | ~5                                                       | ~15                           |
| 23   | ~-5                                                      | ~-10                          |
| 24   | ~-10                                                     | ~-15                          |
| 25   | ~5                                                       | ~25                           |
| 26   | ~0                                                       | ~20                           |
</details>

Source: BoK, MS

## Consumption: Faster-Than-Expected Recovery

We see a more stable consumption path on fiscal support, wealth effect, and wage growth

GDP private consumption trend  
![](images/4e47846942c229b7be2a8008709eeed03ac31d7d887332a2d29f327d2ddeaa04.jpg)

<details>
<summary>bar-line hybrid</summary>

| Quarter | Private consumption, %Y | Services production, %Y | Long-term trend consumption growth (10-year) |
|---|---|---|---|
| 1Q23 | 5.0 | 6.4 | |
| 3Q23 | 1.7 | 2.9 | |
| 1Q24 | 0.7 | 2.0 | |
| 3Q24 | 1.3 | 0.3 | |
| 1Q25 | 0.5 | 0.9 | |
| 3Q25 | 1.9 | 3.3 | |
| 1Q26 | 2.6 | 4.0 | MSe-> |
| 3Q26 | 1.8 | 2.2 | |
| 1Q27E | 2.0 | 2.0 | |
</details>

Both goods and services consumption to sustain

Consumption breakdown by components  
![](images/bd047ae030eff00f7b05ef71278aa4464ab5a926e4fc4f395c9611212ad73028.jpg)

<details>
<summary>bar-line hybrid</summary>

| Quarter | Durable Goods (%) | Semi Durable Goods (%) | Non Durable Goods (%) | Services (%) | Total private consumption, %Y |
|---|---|---|---|---|---|
| 1Q21 | 0.8 | 0.5 | 0.4 | -0.5 | 0.7 |
| 2Q21 | -0.8 | 0.9 | 0.6 | 1.5 | 4.3 |
| 3Q21 | -0.6 | 1.0 | 0.7 | 1.8 | 3.7 |
| 4Q21 | -0.4 | 1.4 | 0.8 | 2.5 | 6.4 |
| 1Q22 | -0.3 | 0.7 | 0.3 | 2.5 | 4.3 |
| 2Q22 | -0.2 | 0.8 | -0.3 | 2.5 | 4.4 |
| 3Q22 | -0.1 | 0.6 | -0.8 | 3.0 | 5.3 |
| 4Q22 | 0.1 | 0.3 | -0.5 | 2.8 | 3.0 |
| 1Q23 | 0.3 | 0.4 | -0.4 | 2.5 | 5.0 |
| 2Q23 | 0.2 | -0.3 | -0.3 | 1.5 | 1.7 |
| 3Q23 | -0.1 | -0.6 | -0.4 | 0.5 | 0.6 |
| 4Q23 | -0.2 | -0.7 | -0.4 | 0.6 | 0.7 |
| 1Q24 | -0.3 | -0.8 | -0.4 | 0.7 | 1.1 |
| 2Q24 | -0.4 | -0.9 | -0.4 | 0.8 | 1.1 |
| 3Q24 | -0.5 | -1.0 | -0.4 | 0.9 | 1.3 |
| 4Q24 | -0.6 | -1.1 | -0.4 | 1.0 | 1.3 |
| 1Q25 | -0.7 | -1.2 | -0.4 | 1.1 | 1.1 |
| 2Q25 | -0.8 | -1.3 | -0.4 | 1.2 | 1.1 |
| 3Q25 | -0.9 | -1.4 | -0.4 | 1.3 | 1.9 |
| 4Q25E | -1.0 | -1.5 | -0.4 | 1.4 | 2.3 |
| 1Q26E | -1.1 | -1.6 | -0.4 | 1.5 | 2.6 |
| 2Q26E | -1.2 | -1.7 | -0.4 | 1.6 | 2.1 |
| 3Q26E | -1.3 | -1.8 | -0.4 | 1.7 | 2.1 |
The chart displays the percentage of total private consumption by year (as of Q4) for each quarter from Q1 to Q3 of the following year (from Q1 to Q3). The data is presented in a table format with columns for each category: 'Durable Goods' (dark green), 'Non Durable Goods' (orange), 'Services' (light green), and 'Total private consumption, %Y' (blue line with diamond markers). The values for the line are calculated based on the absolute percentage of total private consumption for each quarter and year respectively.
</details>

Source: BoK, MS forecasts

## Structural Factors Become Favorable for Wealth Effect From Equities

Retail investor stock ownership in Korea remains relatively high, nearly 50% of the adult population

% share of adult population with stock ownership  
![](images/5b155f5c070b784dcc221a0b324b3128ad844017f68026022171f22c06c547fe.jpg)

<details>
<summary>bar chart</summary>

| Country | Value |
| :--- | :--- |
| US | 60 |
| Australia | 55 |
| Korea | 50 |
| Canada | 40 |
| UK | 27 |
| Japan | 20 |
| Germany | 15 |
| China | 13 |
| India | 8 |
</details>

Liquidity in Korea's equity market remains ample, with a recent jump over the past two years

Korea: Securities investor deposits, KRW tn  
![](images/6211d7bc24b01

[中间内容因长度限制已省略]

cepts responsibility for its contents; in Korea by MS & Co International plc, Seoul Branch; in India by MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the United States by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 4.9(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

© 2026 MS
"""
