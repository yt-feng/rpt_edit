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
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# China Economic Activity and Policy Tracker: June 5

In this note, we update four sets of high-frequency indicators that we track: 1) consumption and mobility; 2) production and investment; 3) other macro activity; and 4) markets and policy. To track closely the impact of higher energy price supply shock on Chinese economic activity, we now publish our tracker on a weekly basis.

# 1) Consumption and mobility

Exhibit 1: 30-city daily property transaction volume in the primary market was roughly flat over the last week but remained above year-ago level   
![](images/b674b48d656b41c48406eadd083a1f0e8ea63dc9bdcc9e18684a07b98302c70e.jpg)

<details>
<summary>line</summary>

| Month | 2019 (Thousand sqm) | 2025 (Thousand sqm) | 2026 (Thousand sqm) |
|-------|---------------------|---------------------|---------------------|
| Jan   | ~800                | ~600                | ~400                |
| Feb   | ~500                | ~100                | ~150                |
| Mar   | ~600                | ~200                | ~100                |
| Apr   | ~700                | ~300                | ~450                |
| May   | ~650                | ~250                | ~200                |
| Jun   | ~750                | ~300                | ~300                |
| Jul   | ~700                | ~500                | -                   |
| Aug   | ~650                | ~200                | -                   |
| Sep   | ~600                | ~250                | -                   |
| Oct   | ~750                | ~350                | -                   |
| Nov   | ~650                | ~250                | -                   |
| Dec   | ~750                | ~400                | -                   |
</details>

Source: Wind, GS Global Investment Research

# Chelsea Song

+852-2978-0106

chelsea.song@gs.com

GS (Asia) L.L.C.

Exhibit 2: 16-city daily property transaction volume in the secondary market declined but remained above year-ago level   
![](images/3dafcc70310a9ad097736f6f04fa04c503586aa4eab3dd6f6dae8a09ef012ac1.jpg)

<details>
<summary>line</summary>

| Month | 2019 (Thousand sqm) | 2025 (Thousand sqm) | 2026 (Thousand sqm) |
|-------|---------------------|---------------------|---------------------|
| Jan   | ~300                | ~420                | ~280                |
| Feb   | ~150                | ~0                  | ~0                  |
| Mar   | ~250                | ~300                | ~250                |
| Apr   | ~280                | ~350                | ~320                |
| May   | ~300                | ~360                | ~380                |
| Jun   | ~250                | ~300                | ~350                |
| Jul   | ~280                | ~280                | —                   |
| Aug   | ~250                | ~250                | —                   |
| Sep   | ~220                | ~220                | —                   |
| Oct   | ~180                | ~0                  | —                   |
| Nov   | ~250                | ~300                | —                   |
| Dec   | ~280                | ~320                | —                   |
</details>

Source: Wind, GS Global Investment Research

Exhibit 3: China's passenger flights for domestic routes declined and remained below year-ago level   
![](images/b05c9c53709a48c374c50b81a9db1bdf53c1bb9751539570c94055bcb5c486d7.jpg)

<details>
<summary>line</summary>

| Month | 2024 | 2025 | 2026 |
|-------|------|------|------|
| Jun 04 | - | - | -11.0% yoy* |
</details>

Source: Wind, GS Global Investment Research

Exhibit 4: China's passenger flights cancellation rate increased over the last week   
![](images/f18937818e2feef1600ebecb40cf73836174a3366f9c3f9dd2da46acceb2b2e1.jpg)

<details>
<summary>line</summary>

| Month | 2024 | 2025 | 2026 |
|-------|------|------|------|
| Jun 04 | 25.0 | 16.0 | 28.0 |
*11.3%*
</details>

Source: Wind, GS Global Investment Research

Exhibit 5: Traffic congestion edged down over the last week   
![](images/2e196f70918833af145da2ed615f0bcc699529f69dd554db31df30c91b184506.jpg)

<details>
<summary>line</summary>

| Month | 2019 | 2025 | 2026 |
|-------|------|------|------|
| Jun 03 | 1.55 | 1.40 | 1.48 |
| Oct   | 1.65 | 1.60 | 1.55 |
| Dec   | 1.60 | 1.55 | 1.50 |
</details>

From 2022 onwards, we changed our data source from Gaode map to Baidu map. Baidu congestion data starts from September 2021 and moves closely with that from Gaode map. The two sets of data are different in sample coverage: Gaode map covers 100 cities and Baidu map covers 98 cities.   
Source: Wind, Haver Analytics, GS Global Investment Research

Exhibit 6: Domestic gasoline and diesel prices were adjusted downwards by 525 and 505 RMB/tonne respectively on June 4   
![](images/71a590058885be4971edaf428b8cda36988cf7f75143c7debb46c7d7faaa8408.jpg)

<details>
<summary>line</summary>

| Date     | China Diesel (RMB/Ton) | China Gasoline (USD) | Brent (right) (USD) |
|----------|------------------------|----------------------|---------------------|
| 25-Jan   | ~8500                  | ~9500                | ~7500               |
| 25-Mar   | ~8300                  | ~9400                | ~7300               |
| 25-May   | ~8100                  | ~9200                | ~6500               |
| 25-Jul   | ~8200                  | ~9100                | ~7800               |
| 25-Sep   | ~8000                  | ~9000                | ~6800               |
| 25-Nov   | ~7800                  | ~8900                | ~6500               |
| 26-Jan   | ~7600                  | ~8800                | ~6200               |
| 26-Mar   | ~7800                  | ~9500                | ~9500               |
| 26-May   | ~9800                  | ~11000               | ~11500              |
| 26-Jul   | ~9500                  | ~10500               | ~9500               |
</details>

Source: Haver Analytics, GS Global Investment Research

Exhibit 7: Prices for sulfuric acid slightly edged up over the last week while other exposed chemicals stabilized somewhat   
![](images/4426d778549f453eba690700d5f05b4286efe874269647c125fac37afda2dd1b.jpg)

<details>
<summary>line</summary>

| Date    | Methanol | Aluminum | Sulfuric acid | Compound fertilizer | Polypropylene | Urea |
|---------|----------|----------|---------------|---------------------|---------------|------|
| Mar-25  | ~100     | ~100     | ~85           | ~100                | ~105          | ~100 |
| May-25  | ~100     | ~100     | ~95           | ~100                | ~105          | ~100 |
| Jul-25  | ~100     | ~100     | ~100          | ~100                | ~105          | ~100 |
| Sep-25  | ~100     | ~100     | ~105          | ~100                | ~105          | ~100 |
| Nov-25  | ~100     | ~100     | ~125          | ~100                | ~105          | ~100 |
| Jan-26  | ~100     | ~115     | ~130          | ~105                | ~115          | ~100 |
| Mar-26  | ~100     | ~120     | ~140          | ~110                | ~125          | ~100 |
| May-26  | ~120     | ~125     | ~280          | ~115                | ~135          | ~100 |
</details>

Source: Wind, Haver Analytics, GS Global Investment Research

Exhibit 8: The Morning Consult consumer confidence edged up to multi-year high   
![](images/61906b6f86cceca90f4c36a97770fa87a694454887901c57b2a51b1402616a06.jpg)

<details>
<summary>line</summary>

| Date   | Morning Consult | NBS (right) |
|--------|-----------------|-------------|
| Jul-22 | 152             | 88.0        |
| Jan-23 | 135             | 95.0        |
| Jul-23 | 160             | 87.5        |
| Jan-24 | 145             | 88.0        |
| Jul-24 | 165             | 89.0        |
| Jan-25 | 138             | 87.0        |
| Jul-25 | 160             | 90.0        |
| Jan-26 | 168             | 92.0        |
| Jul-26 | 175             | 97.5        |
</details>

Source: Haver Analytics, Morning Consult, GS Global Investment Research

Exhibit 9: Weighted PMI employment sub-index edged up in May   
![](images/746856739818137e6ac906a358efba61593210bfb2a4bea3277e5bccc3862e04.jpg)

<details>
<summary>line</summary>

| Year | Single month | 3mma |
|------|--------------|------|
| 2015 | ~0.8         | ~1.0 |
| 2016 | ~0.3         | ~0.4 |
| 2017 | ~0.9         | ~0.8 |
| 2018 | ~0.7         | ~0.7 |
| 2019 | ~0.2         | ~0.1 |
| 2020 | ~-3.0        | ~-2.0 |
| 2021 | ~1.3         | ~1.0 |
| 2022 | ~-0.5        | ~-0.5 |
| 2023 | ~-2.0        | ~-1.5 |
| 2024 | ~-0.5        | ~-0.5 |
| 2025 | ~-0.8        | ~-0.8 |
| 2026 | ~-0.5        | ~-0.5 |
</details>

We include employment sub-index under NBS manufacturing PMI, construction PMI, and services PMI, Caixin manufacturing PMI and services PMI, CKGSB recruitment index, and emerging industries PMI.   
Source: NBS, Caixin, Haver Analytics, GS Global Investment Research

# 2) Production and investment

Exhibit 10: Steel demand edged down over the past week   
![](images/6a93e1b7863b0bff103e8e46906a9d23e5677ad625f9fd1bd4ea1767b382abb0.jpg)

<details>
<summary>line</summary>

| Month | 2019 (Million tons per week) | 2025 (Million tons per week) | 2026 (Million tons per week) |
|-------|------------------------------|------------------------------|------------------------------|
| Feb   | ~9.5                         | ~5.0                         | ~8.0                         |
| Mar   | ~11.0                        | ~7.5                         | ~6.0                         |
| Apr   | ~11.5                        | ~9.0                         | ~8.5                         |
| May   | ~11.0                        | ~9.5                         | ~9.0                         |
| Jun   | ~10.5                        | ~8.5                         | ~8.5                         |
| Jul   | ~10.5                        | ~8.5                         | ~8.5                         |
| Aug   | ~10.5                        | ~8.5                         | ~8.5                         |
| Sep   | ~10.5                        | ~8.5                         | ~8.5                         |
| Oct   | ~10.5                        | ~7.5                         | ~8.5                         |
| Nov   | ~10.5                        | ~9.0                         | ~8.5                         |
| Dec   | ~10.0                        | ~8.5                         | ~8.5                         |
</details>

\*Percentage change relative to the same week in 2025.   
Source: Mysteel, GS Global Investment Research

Exhibit 11: Steel production edged down over the past week   
![](images/86a84a9ba879ee8808cde353af14d3ae668c3ba975fe4c9a0c70341b9dfb9963.jpg)

<details>
<summary>line</summary>

| Month | 2019 (Million tons per week) | 2025 (Million tons per week) | 2026 (Million tons per week) |
|-------|-------------------------------|------------------------------|------------------------------|
| Feb   | ~9.7                          | ~8.1                         | ~8.2                         |
| Mar   | ~9.6                          | ~8.3                         | ~8.0                         |
| Apr   | ~10.0                         | ~8.6                         | ~8.4                         |
| May   | ~10.8                         | ~8.7                         | ~8.6                         |
| Jun   | ~10.9                         | ~8.6                         | ~8.5                         |
| Jul   | ~10.8                         | ~8.7                         | —                            |
| Aug   | ~10.7                         | ~8.7                         | —                            |
| Sep   | ~10.5                         | ~8.7                         | —                            |
| Oct   | ~9.5                          | ~8.6                         | —                            |
| Nov   | ~10.3                         | ~8.7                         | —                            |
| Dec   | ~10.5                         | ~8.0                         | —                            |
</details>

\*Percentage change relative to the same week in 2025.   
Source: Mysteel, GS Global Investment Research

Exhibit 12: Daily coal consumption in coastal provinces increased further over the last week and remained above year-ago level   
![](images/a99ca1738c2f4a2aa478b0e05b3ced1d9944f10a3953e6c74723b44eee1e89af.jpg)

<details>
<summary>line</summary>

| Month | 2019 (Million tons per day) | 2025 (Million tons per day) | 2026 (Million tons per day) |
|-------|-----------------------------|-----------------------------|-----------------------------|
| Jan   | ~2.3                        | ~2.3                        | ~2.4                        |
| Feb   | ~1.0                        | ~1.1                        | ~1.2                        |
| Mar   | ~1.8                        | ~1.9                        | ~1.7                        |
| Apr   | ~1.7                        | ~1.8                        | ~1.8                        |
| May   | ~1.6                        | ~1.7                        | ~1.6                        |
| Jun   | ~1.5                        | ~1.8                        | ~2.0                        |
| Jul   | ~1.7                        | ~2.0                        | —                           |
| Aug   | ~2.0                        | ~2.5                        | —                           |
| Sep   | ~1.9                        | ~2.4                        | —                           |
| Oct   | ~1.7                        | ~2.0                        | —                           |
| Nov   | ~1.6                        | ~1.8                        | —                           |
| Dec   | ~2.0                        | ~2.2                        | —                           |
</details>

\*Percent change relative to 2025. Note: Data available since July 2020, data prior to that are derived based on coal consumption at six major coastal power plants.   
Source: Haver, CCTD, GS Global Investment Research

Exhibit 13: RMB 1.50bn local government special bonds have been issued year-to-date   
![](images/f3a917bf2a54bda7981de3eaa031db2593c2114b0050b5c706d31282a0e6a070.jpg)

<details>
<summary>area</summary>

| Month | 2025 (RMB tn) | 2026 (RMB tn) |
|-------|---------------|---------------|
| Jan   | 0             | 0             |
| Feb   | ~0.1          | ~0.2          |
| Mar   | ~0.3          | ~0.5          |
| Apr   | ~0.5          | ~0.7          |
| May   | ~0.8          | ~1.0          |
| Jun   | ~1.5          | ~1.5          |
| Jul   | ~2.0          | -             |
| Aug   | ~2.5          | -             |
| Sep   | ~3.0          | -             |
| Oct   | ~3.5          | -             |
| Nov   | ~4.0          | -             |
| Dec   | ~4.5          | -             |
| Jan   | ~4.8          | -             |
</details>

\*Updated with issuance plan through Jun 05.   
Source: Wind, GS Global Investment Research

Exhibit 14: PSL loans outstanding contracted in May 2026   
![](images/0ddbb5f400deb13d0bb72fb5c703b5be70efc3dbf3020ea6cbf74ab8aacab77a.jpg)

<details>
<summary>bar_line</summary>

PSL: Net injection vs outstanding amount
| Year | Net injection (RMB bn) | Outstanding (RHS) (RMB tn) |
|---|---|---|
| 2014 | 0 | 0 |
| 2015 | 387 | 0.5 |
| 2016 | 145 | 1.5 |
| 2017 | 100 | 2.2 |
| 2018 | 155 | 3.0 |
| 2019 | 60 | 3.6 |
| 2020 | -20 | 3.4 |
| 2021 | -150 | 3.0 |
| 2022 | -50 | 2.8 |
| 2023 | 370 | 3.2 |
| 2024 | -350 | 3.4 |
| 2025 | -250 | 2.0 |
| 2026 | -180 | 1.0 |
</details>

Source: PBOC, Wind, GS Global Investment Research

# 3) Other macro activity

Exhibit 15: Official port container throughput rose over the last week and was above year-ago level   
![](images/8394320e3803c154fce5090b168607b2fe9f7b764e0769d913a96dfc45fb7b3c.jpg)

<details>
<summary>line</summary>

| Month | 2024 (Million TEU) | 2025 (Million TEU) | 2026 (Million TEU) |
|-------|---------------------|---------------------|---------------------|
| Jan   | ~6.0                | ~6.5                | ~6.8                |
| Feb   | ~5.3                | ~5.3                | ~7.5                |
| Mar   | ~4.4                | ~5.8                | ~5.6                |
| Apr   | ~5.8                | ~6.2                | ~6.8                |
| May   | ~6.0                | ~6.7                | ~7.0                |
| Jun   | ~6.3                | ~6.5                | ~7.1* yoy*          |
| Jul   | ~6.2                | ~6.7                | —                   |
| Aug   | ~5.6                | ~5.7                | —                   |
| Sep   | ~6.0                | ~6.8                | —                   |
| Oct   | ~6.0                | ~6.7                | —                   |
| Nov   | ~5.8                | ~6.9                | —                   |
| Dec   | ~5.5                | ~6.5                | —                   |
</details>

Source: Ministry of Transport, Haver Analytics, GS Global Investment Research

Exhibit 16: Freight volume of departing ships at 20 major ports rose over the past week and was above year-ago level   
![](images/ca7231654f02a623b0981191a9a415b7b32fcd7c0b9096d66ba651fb82639238.jpg)

<details>
<summary>line</summary>

| Month | 2024 (Million tons) | 2025 (Million tons) | 2026 (Million tons) |
|-------|---------------------|---------------------|---------------------|
| Jan   | ~36.5               | ~31.0               | ~31.5               |
| Feb   | ~31.0               | ~20.5               | ~33.0               |
| Mar   | ~29.0               | ~27.5               | ~22.5               |
| Apr   | ~31.0               | ~30.5               | ~31.5               |
| May   | ~31.5               | ~32.5               | ~31.0               |
| Jun   | ~31.0               | ~31.0               | ~32.5 (Jun 03: +8.2% yoy) |
| Jul   | ~31.5               | ~31.5               | -                   |
| Aug   | ~31.0               | ~26.5               | -                   |
| Sep   | ~31.5               | ~31.0               | -                   |
| Oct   | ~31.0               | ~33.5               | -                   |
| Nov   | ~31.5               | ~26.5               | -                   |
| Dec   | ~34.5               | ~34.0               | -                   |
</details>

Source: CEIC, GS Global Investment Research

Exhibit 17: Our nowcast indicates China oil demand increased to 16.5mb/d in the latest reading   
![](images/906d37e

[中间内容因长度限制已省略]

e have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
