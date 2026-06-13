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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`GS`。标题格式建议：`# GS：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## China Economic Activity and Policy Tracker: June 12

In this note, we update four sets of high-frequency indicators that we track: 1) consumption and mobility; 2) production and investment; 3) other macro activity; and 4) markets and policy. To track closely the impact of higher energy price supply shock on Chinese economic activity, we now publish our tracker on a weekly basis.

## 1) Consumption and mobility

Exhibit 1: 30-city daily property transaction volume in the primary market fell below year-ago level  
![](images/f13b051bdce9ec0e01c48a45b225efaf098fc85a93c7da16a95088aed6028d70.jpg)

<details>
<summary>line chart</summary>

| Date       | 2019 (Thousand sqm) | 2025 (Thousand sqm) | 2026 (Thousand sqm) |
|------------|---------------------|---------------------|---------------------|
| Jun 11     | -                   | -                   | -                   |
| Jun 11 (Aug) | ~700                | ~500                | ~400                |
| Jun 11 (Oct)| ~800                | ~300                | ~200                |
| Jun 11 (Dec)| ~750                | ~400                | ~450                |
</details>

Source: Wind, GS Global Investment Research

## Chelsea Song

+852-2978-0106

chelsea.song@gs.com

GS (Asia) L.L.C.

Exhibit 2: 16-city daily property transaction volume in the secondary market declined but remained above year-ago level  
![](images/97ce76d9937b8eacc0992250f07683540c565e42f29d52edd2aaa165e9972495.jpg)

<details>
<summary>line chart</summary>

| Month | 2019 (thousand sqm) | 2025 (thousand sqm) | 2026 (thousand sqm) |
|-------|---------------------|---------------------|---------------------|
| Jan   | ~450                | ~350                | ~200                |
| Feb   | ~150                | ~0                  | ~0                  |
| Mar   | ~250                | ~300                | ~150                |
| Apr   | ~300                | ~350                | ~300                |
| May   | ~350                | ~350                | ~350                |
| Jun   | ~300                | ~300                | ~300                |
| Jul   | ~250                | ~250                | ~250                |
| Aug   | ~250                | ~250                | ~250                |
| Sep   | ~250                | ~250                | ~250                |
| Oct   | ~150                | ~0                  | ~0                  |
| Nov   | ~250                | ~300                | ~300                |
| Dec   | ~250                | ~300                | ~300                |
</details>

Source: Wind, GS Global Investment Research

Exhibit 3: China's passenger flights for domestic routes edged up but remained below year-ago level  
![](images/7ca0b0cec96d68714ef0142dd7fed24fd0f41615a5838aa05909b3d54ce84414.jpg)

<details>
<summary>line chart</summary>

| Month | 2024 | 2025 | 2026 |
|-------|------|------|------|
| Jun 11 | - | - | -9.9% yoy* |
</details>

Source: Wind, GS Global Investment Research

Exhibit 4: China's passenger flights cancellation rate declined over the last week but remained elevated  
![](images/d98c1ce657d21549756f9aa51143a80827c4835f8e546fb6018490675f0df7f6.jpg)

<details>
<summary>line chart</summary>

| Month | 2024 | 2025 | 2026 |
|-------|------|------|------|
| Jun 11 | +10.6%* | - | - |
</details>

Source: Wind, GS Global Investment Research

Exhibit 5: Traffic congestion was roughly flat over the last week  
![](images/34fd45fef966bff612c01c185ef0bf514f92cd05250b43c6d1117976f5c0031c.jpg)

<details>
<summary>line chart</summary>

| Date       | 2019 | 2025 | 2026 |
| ---------- | ---- | ---- | ---- |
| Jun 10     | 1.6  | 1.4  | 1.45 |
| Jun 10+    | 1.6  | 1.3  | 1.3  |
</details>

From 2022 onwards, we changed our data source from Gaode map to Baidu map. Baidu congestion data starts from September 2021 and moves closely with that from Gaode map. The two sets of data are different in sample coverage: Gaode map covers 100 cities and Baidu map covers 98 cities.  
Source: Wind, Haver Analytics, GS Global Investment Research

Exhibit 6: Domestic gasoline and diesel prices remained unchanged over the last week  
![](images/d1f796666a35cc31a4667044f7ef67dd238f2fbc88d12677db2a403e796a4fcb.jpg)

<details>
<summary>line chart</summary>

| Date   | China Diesel (RMB/Ton) | China Gasoline (USD/bbl) | Brent (right) (USD/bbl) |
|--------|------------------------|--------------------------|-------------------------|
| Jan-25 | ~8500                  | ~9500                    | ~7500                   |
| Mar-25 | ~8300                  | ~9400                    | ~7300                   |
| May-25 | ~7800                  | ~8800                    | ~6500                   |
| Jul-25 | ~8100                  | ~9100                    | ~7800                   |
| Sep-25 | ~7900                  | ~8900                    | ~7200                   |
| Nov-25 | ~7700                  | ~8700                    | ~6800                   |
| Jan-26 | ~7500                  | ~8500                    | ~6200                   |
| Mar-26 | ~8500                  | ~9500                    | ~11500                  |
| May-26 | ~9800                  | ~11000                   | ~11800                  |
| Jul-26 | ~9500                  | ~10500                   | ~9500                   |
</details>

Source: Haver Analytics, GS Global Investment Research

Exhibit 7: Prices for polypropylene edged up over the last week while other exposed chemicals stabilized somewhat  
![](images/38b7ad39e167831ab352bedf8cc880822568d4e0a6687acfc564187caf5fa2ab.jpg)

<details>
<summary>line chart</summary>

| Date    | Methanol | Aluminum | Sulfuric acid | Compound fertilizer | Polypropylene | Urea |
|---------|----------|----------|---------------|---------------------|---------------|------|
| Mar-25  | ~100     | ~100     | ~90           | ~100                | ~100          | ~100 |
| May-25  | ~100     | ~100     | ~95           | ~100                | ~100          | ~100 |
| Jul-25  | ~100     | ~100     | ~100          | ~100                | ~100          | ~100 |
| Sep-25  | ~100     | ~100     | ~105          | ~100                | ~100          | ~100 |
| Nov-25  | ~100     | ~100     | ~125          | ~100                | ~100          | ~100 |
| Jan-26  | ~100     | ~115     | ~130          | ~105                | ~105          | ~100 |
| Mar-26  | ~100     | ~120     | ~150          | ~110                | ~125          | ~100 |
| May-26  | ~125     | ~125     | ~280          | ~115                | ~135          | ~95  |
</details>

Source: Wind, Haver Analytics, GS Global Investment Research

Exhibit 8: Import prices for both energy products and integrated circuits surged in May  
![](images/87436b0b3c29d16dcdd2a9346f4eb0f138b0974b24cd44d9ec3028f242b567a7.jpg)

<details>
<summary>line chart</summary>

| Month   | Coal  | Crude Oil | Refined Petroleum Products | Natural Gas | Plastics in Primary Forms | Integrated circuits |
|---------|-------|-----------|----------------------------|-------------|---------------------------|---------------------|
| Jan-25  | 110   | 115       | 110                        | 105         | 100                       | 98                  |
| Mar-25  | 105   | 110       | 110                        | 105         | 100                       | 95                  |
| May-25  | 100   | 95        | 105                        | 105         | 100                       | 98                  |
| Jul-25  | 95    | 95        | 100                        | 105         | 100                       | 100                 |
| Sep-25  | 95    | 95        | 100                        | 100         | 100                       | 100                 |
| Nov-25  | 95    | 95        | 95                         | 95          | 95                        | 105                 |
| Jan-26  | 95    | 95        | 95                         | 85          | 95                        | 125                 |
| Mar-26  | 105   | 140       | 145                        | 100         | 130                       | 140                 |
| May-26  | 120   | 155       | 170                        | 115         | 130                       | 165                 |
</details>

USD-denominated import prices  
Source: Haver Analytics, GS Global Investment Research

Exhibit 9: Export prices of refined petroleum products and integrated circuits surged in May  
![](images/e7b1515567a543aa96962236aa5a06d148f14b969856865dc03ae919581b37d3.jpg)

<details>
<summary>line chart</summary>

| Month   | Aluminum | Refined Petroleum Products | Integrated circuits |
|---------|----------|-----------------------------|---------------------|
| Jan-25  | 100      | 105                         | 90                  |
| Mar-25  | 100      | 103                         | 92                  |
| May-25  | 100      | 100                         | 95                  |
| Jul-25  | 100      | 98                          | 102                 |
| Sep-25  | 100      | 97                          | 105                 |
| Nov-25  | 100      | 100                         | 115                 |
| Jan-26  | 105      | 100                         | 140                 |
| Mar-26  | 110      | 110                         | 148                 |
| May-26  | 115      | 165                         | 210                 |
</details>

USD-denominated export prices  
Source: Haver Analytics, GS Global Investment Research

Exhibit 10: The Morning Consult consumer confidence rose to multi-year high  
![](images/e103ddcf6e04f4faa76900acfbf99c434572a4ef82b1c39b63da5feca49703a4.jpg)

<details>
<summary>line chart</summary>

| Date   | Morning Consult | NBS (right) |
|--------|-----------------|-------------|
| Jul-22 | 150             | 87.5        |
| Jan-23 | 130             | 95.0        |
| Jul-23 | 160             | 87.5        |
| Jan-24 | 150             | 87.5        |
| Jul-24 | 165             | 87.5        |
| Jan-25 | 140             | 87.5        |
| Jul-25 | 160             | 90.0        |
| Jan-26 | 165             | 92.5        |
| Jul-26 | 180             | 97.5        |
</details>

Source: Haver Analytics, Morning Consult, GS Global Investment Research

Exhibit 11: New energy vehicles (NEVs) sales volume increased in May but remained below year-ago level  
![](images/a502da91c50a569ac884a45f0b77830f01b413c2675e419ec7b84991432abb39.jpg)

<details>
<summary>line chart</summary>

| Month | 2019 (thousand units per day) | 2025 (thousand units per day) | 2026 (thousand units per day) |
|-------|-------------------------------|-------------------------------|-------------------------------|
| Jan   | ~3                            | ~24                           | ~19                           |
| Feb   | ~2                            | ~24                           | ~17                           |
| Mar   | ~3                            | ~32                           | ~28                           |
| Apr   | ~3                            | ~30                           | ~29                           |
| May   | ~3                            | ~34                           | ~31                           |
| Jun   | ~4                            | ~37                           | —                             |
| Jul   | ~2                            | ~32                           | —                             |
| Aug   | ~2                            | ~36                           | —                             |
| Sep   | ~2                            | ~43                           | —                             |
| Oct   | ~2                            | ~41                           | —                             |
| Nov   | ~2                            | ~44                           | —                             |
| Dec   | ~4                            | ~43                           | —                             |
</details>

Source: Wind, GS Global Investment Research

Exhibit 12: Total auto sales volume edged higher in May but remained below year-ago level  
![](images/03e6ab2326f714cf97063f85696ad0577d5e1ee86a096018331e9c4ae8ed59db.jpg)

<details>
<summary>line chart</summary>

| Month | 2019 (Thousand units per day) | 2025 (Thousand units per day) | 2026 (Thousand units per day) |
|-------|-------------------------------|-------------------------------|-------------------------------|
| Jan   | ~63                           | ~61                           | ~53                           |
| Feb   | ~38                           | ~50                           | ~38                           |
| Mar   | ~50                           | ~61                           | ~54                           |
| Apr   | ~45                           | ~60                           | ~47                           |
| May   | ~47                           | ~63                           | ~50                           |
| Jun   | ~54                           | ~68                           | —                             |
| Jul   | ~44                           | ~59                           | —                             |
| Aug   | ~48                           | ~63                           | —                             |
| Sep   | ~53                           | ~75                           | —                             |
| Oct   | ~54                           | ~77                           | —                             |
| Nov   | ~56                           | ~76                           | —                             |
| Dec   | ~65                           | ~74                           | —                             |
</details>

Source: Wind, GS Global Investment Research

## 2) Production and investment

Exhibit 13: Steel demand edged down over the past week  
![](images/d1a07ae9b8a9da270be6bb9329371984b9b5fe85f1b4292e6935ea20ba42ad70.jpg)

<details>
<summary>line chart</summary>

| Month | 2019 (Million tons per week) | 2025 (Million tons per week) | 2026 (Million tons per week) |
|-------|-------------------------------|-------------------------------|-------------------------------|
| Feb   | ~9.5                          | ~8.5                          | ~8.0                          |
| Mar   | ~11.0                         | ~8.0                          | ~7.0                          |
| Apr   | ~11.5                         | ~9.0                          | ~8.5                          |
| May   | ~11.0                         | ~9.5                          | ~9.0                          |
| Jun   | ~10.5                         | ~8.5                          | ~8.5                          |
| Jul   | ~10.5                         | ~8.5                          | —                             |
| Aug   | ~10.5                         | ~8.5                          | —                             |
| Sep   | ~10.5                         | ~8.5                          | —                             |
| Oct   | ~10.5                         | ~7.5                          | —                             |
| Nov   | ~10.5                         | ~9.0                          | —                             |
| Dec   | ~10.0                         | ~8.5                          | —                             |
</details>

Source: Mysteel, GS Global Investment Research

Exhibit 14: Steel production was roughly flat over the past week  
![](images/c1ba99cb3fda92bbe4e3d67377984b56e377fed6955bda8ca211a754fb46ec06.jpg)

<details>
<summary>line chart</summary>

| Month | 2019 (Million tons per week) | 2025 (Million tons per week) | 2026 (Million tons per week) |
|-------|-------------------------------|------------------------------|------------------------------|
| Feb   | ~9.7                          | ~8.3                         | ~8.2                         |
| Mar   | ~9.8                          | ~8.4                         | ~8.1                         |
| Apr   | ~10.0                         | ~8.6                         | ~8.4                         |
| May   | ~10.8                         | ~8.7                         | ~8.6                         |
| Jun   | ~10.9                         | ~8.7                         | ~8.6                         |
| Jul   | ~10.8                         | ~8.7                         | —                            |
| Aug   | ~10.7                         | ~8.7                         | —                            |
| Sep   | ~10.5                         | ~8.7                         | —                            |
| Oct   | ~9.5                          | ~8.6                         | —                            |
| Nov   | ~10.3                         | ~8.7                         | —                            |
| Dec   | ~10.5                         | ~8.0                         | —                            |
</details>

Source: Mysteel, GS Global Investment Research

Exhibit 15: Daily coal consumption in coastal provinces fell from recent high  
![](images/4a265057bd02db184ae9c0d49c57f60a421c7b1ddc77305e5bf6e3af2f928620.jpg)

<details>
<summary>line chart</summary>

| Month | 2019 (Million tons per day) | 2025 (Million tons per day) | 2026 (Million tons per day) |
|-------|-----------------------------|-----------------------------|-----------------------------|
| Jan   | ~2.3                        | ~2.4                        | ~2.4                        |
| Feb   | ~1.0                        | ~1.1                        | ~1.2                        |
| Mar   | ~1.8                        | ~1.9                        | ~1.8                        |
| Apr   | ~1.7                        | ~1.8                        | ~1.7                        |
| May   | ~1.6                        | ~1.7                        | ~1.6                        |
| Jun   | ~1.8                        | ~1.9                        | ~2.0                        |
| Jul   | ~1.9                        | ~2.3                        | ~2.2                        |
| Aug   | ~2.0                        | ~2.5                        | ~2.4                        |
| Sep   | ~1.9                        | ~2.4                        | ~2.3                        |
| Oct   | ~1.8                        | ~2.2                        | ~2.1                        |
| Nov   | ~1.7                        | ~2.0                        | ~1.9                        |
| D

[中间内容因长度限制已省略]

 have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

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

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
