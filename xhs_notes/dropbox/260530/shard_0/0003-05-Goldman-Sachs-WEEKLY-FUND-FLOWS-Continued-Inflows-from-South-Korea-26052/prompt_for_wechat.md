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
WEEKLY FUND FLOWS

# Continued Inflows from South Korea

# Global fund flows, week ending May 27

■ Flows into mutual funds and related investment products turned negative for equities but remained positive for fixed income.   
Net flows into global equity funds turned slightly negative in the week ending May 27 (-\$7bn vs +\$2bn in the previous week). Within DM, US funds continued to see demand while Europe and Japan funds saw net outflows. Within EM, Mainland China equity funds drove the net outflows. Bilateral net flows into US equity funds from South Korea continued to increase (see Chart of the Week). While our economists expect South Korea's surplus to surge despite the energy shock as more valuable tech exports outweigh higher energy import costs, so far that surplus has largely bypassed the domestic economy as it continues to be recycled into foreign equities, weighing on the currency. At the sector level, energy funds saw the largest net outflows. Industrial sector funds saw the largest net inflows across sectors.   
Flows into global fixed income funds remained well-supported from inflows across fund types. Short-duration bond funds and inflation-protected bond funds have also seen sustained inflows. In EM, local-currency bond funds primarily drove net inflows though net flows into hard-currency bond funds were also positive. Money market fund assets rose by \$22bn.   
Cross-border FX flows slowed. USD saw the strongest net demand while CNY saw the largest net outflows after strong net inflows the previous week.

<table><tr><td rowspan="3"></td><td colspan="4">Global Fund Flows Summary</td></tr><tr><td colspan="2">Millions USD</td><td colspan="2">% AUM</td></tr><tr><td>4wk sum</td><td>27-May</td><td>4wk avg</td><td>27-May</td></tr><tr><td>Equity</td><td>18,370</td><td>-7,047</td><td>0.02</td><td>-0.02</td></tr><tr><td>Fixed Income</td><td>111,701</td><td>24,183</td><td>0.29</td><td>0.25</td></tr><tr><td>of which: EM</td><td>8,972</td><td>3,127</td><td>0.32</td><td>0.44</td></tr><tr><td>Money Markets</td><td>164,885</td><td>21,938</td><td>0.37</td><td>0.20</td></tr><tr><td>FX Flows*</td><td>60,759</td><td>7,363</td><td>0.09</td><td>0.05</td></tr></table>

\*Cross-border fund flows, excluding hard currency and FX-hedged funds   
Source: EPFR, Haver Analytics, GS Global Investment Research

# Lexi Kanter

+1(212)855-9701

alexandra.kanter@gs.com

GS & Co. LLC

Chart of the Week   
![](images/00a2a8c334e0dbbe5e99347186dc1d74fab28f39b1889e894a4f17c9907e6c24.jpg)

<details>
<summary>line</summary>

| Date   | Net Flows into US Equity Funds ($bn) | USDKRW |
|--------|--------------------------------------|--------|
| Jan-24 | 0.0                                  | 1300   |
| May-24 | 0.5                                  | 1350   |
| Sep-24 | 0.0                                  | 1300   |
| Jan-25 | 0.8                                  | 1450   |
| May-25 | 0.5                                  | 1400   |
| Sep-25 | 0.2                                  | 1350   |
| Jan-26 | -1.5                                 | 1450   |
| May-26 | 1.7                                  | 1500   |
</details>

Source: EPFR, Haver Analytics, GS Global Investment Research, Bloomberg

# Global Fund Flow Trends

![](images/eb396221a7b042331fb30124b6c52118e13dc7347d9cc72e9093fdf2f69b949c.jpg)

<details>
<summary>line</summary>

| Date   | USA (left) | Euro area (right) |
|--------|------------|-------------------|
| Jan-24 | 0          | 0                 |
| May-24 | ~100       | ~50               |
| Sep-24 | ~200       | ~70               |
| Jan-25 | ~300       | ~100              |
| May-25 | ~400       | ~150              |
| Sep-25 | ~450       | ~250              |
| Jan-26 | ~550       | ~350              |
| May-26 | ~620       | ~500              |
</details>

Source: EPFR, GS Global Investment Research

![](images/3354b2d0cde95755ca41a8a706b1896d8d2e3834693c9071a212c83ec52319d0.jpg)

<details>
<summary>line</summary>

| Date   | Flows into Mainland China Equity Funds from Mainland China ($bn) | Flows into Mainland China Equity Funds from Rest of World ($bn) |
|--------|---------------------------------------------------------------|------------------------------------------------------------------|
| Jan-23 | ~0                                                            | ~0                                                               |
| Aug-23 | ~0                                                            | ~0                                                               |
| Mar-24 | ~20                                                           | ~0                                                               |
| Oct-24 | ~30                                                           | ~10                                                              |
| May-25 | ~28                                                           | ~0                                                               |
| Dec-25 | ~10                                                           | ~0                                                               |
| Jul-26 | ~-20                                                          | ~0                                                               |
</details>

Source: EPFR, GS Global Investment Research

![](images/2495e11f7271eea4426921039e7ed07519bf452384913b77449be3d3bdbc3b40.jpg)

<details>
<summary>line</summary>

| Date   | Technology | Defensives | Cyclicals ex. Tech |
|--------|------------|------------|--------------------|
| Jan-25 | -2         | -1         | 0                  |
| Apr-25 | 4          | -3         | -5                 |
| Jul-25 | -3         | 0          | 0                  |
| Oct-25 | 8          | 2          | 6                  |
| Jan-26 | 16         | 3          | 17                 |
| Apr-26 | 2          | -1         | 0                  |
| Jul-26 | 5          | -1         | -1                 |
</details>

Source: EPFR, GS Global Investment Research

![](images/d11f098242a0da9af6016924eaee0995fbe30decc02941d190e9fc9c8e609f43.jpg)

<details>
<summary>line</summary>

| Sector                  | Jan-24 | May-24 | Sep-24 | Jan-25 | May-25 | Jan-26 | May-26 |
| ----------------------- | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| Commodities/Materials   | 0      | 0      | 0      | 0      | 0      | 30     | 30     |
| Consumer Goods          | 0      | 0      | 0      | 0      | 0      | 25     | 25     |
| Energy                  | 0      | -10    | -10    | -10    | -10    | -15    | -15    |
| Financials              | 0      | 0      | 0      | 0      | 0      | 15     | 15     |
| Health Care/Biotech     | 0      | 0      | 0      | 0      | 0      | 15     | 15     |
| Industrials             | 0      | 0      | 0      | 0      | 0      | 20     | 20     |
| Infrastructure          | 0      | 0      | 0      | 0      | 0      | 25     | 25     |
| Real Estate             | 0      | 0      | 0      | 0      | 0      | 25     | 25     |
| Technology               | 0      | 0      | 0      | 0      | 0      | 25     | 25     |
| Telecom                 | 0      | 0      | 0      | 0      | 0      | 25     | 25     |
| Utilities               | 0      | 0      | 0      | 0      | 0      | 25     | 25     |
</details>

Captures flows to sector dedicated funds

Source: EPFR, GS Global Investment Research   
![](images/f2d27dfe61408d231eed86f516687c2189992bd2f0d84b4b2ba6520fda988518.jpg)

<details>
<summary>line</summary>

| Region           | Jan-24 | May-24 | Sep-24 | Jan-25 | May-25 | Sep-25 | Jan-26 | May-26 |
| ---------------- | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| US               | 0      | 0      | 0      | 0      | 0      | 0      | 0      | 0      |
| Western Europe   | 0      | 0      | 0      | 0      | 0      | 0      | 0      | 0      |
| UK-Dedicated     | 0      | 0      | 0      | 0      | 0      | 0      | 0      | 0      |
| Japan            | 0      | 0      | 0      | 0      | 0      | 0      | 0      | 0      |
| Global EM        | 0      | 0      | 0      | 0      | 0      | 0      | 0      | 0      |
| Mainland China   | 0      | 0      | 0      | 0      | 0      | 0      | 0      | 0      |
| Taiwan           | 0      | 0      | 0      | 0      | 0      | 0      | 0      | 0      |
| Korea            | 0      | 0      | 0      | 0      | 0      | 0      | 0      | 0      |
| India            | 0      | 0      | 0      | 0      | 0      | 0      | 0      | 0      |
| Brazil           | 0      | 0      | 0      | 0      | 0      | 0      | 0      | 0      |
</details>

Captures flows to country- and region-dedicated funds   
Source: EPFR, GS Global Investment Research

![](images/e6592ca55ed958dc9296fda8ca31c4f73a714f1018fabd1c35757e8efa7728c4.jpg)

<details>
<summary>bar</summary>

Cumulative Global Equity Flows by Sector YTD (% AUM)
| Sector | Cumulative Global Equity Flows (%) |
| :--- | :--- |
| Industrials | 22 |
| Infrastructure | 16 |
| Energy | 15.5 |
| Commodities/Materials | 11 |
| Technology | 3 |
| Telecom | 1.5 |
| Utilities | 0.5 |
| Real Estate | -0.5 |
| Health Care/Biotech | -1 |
| Financials | -1.5 |
| Consumer Goods | -4.5 |
</details>

Captures flows to sector dedicated funds

Source: EPFR, GS Global Investment Research   
![](images/60d36e7ed6ca659b18d19713d3d2b2e5d7f39582bbd9daba8c99605c433601de.jpg)

<details>
<summary>bar</summary>

Cumulative Global Equity Flows by Region YTD (% AUM)
| Region | Cumulative Global Equity Flows (%) |
| :--- | :--- |
| Korea | 39 |
| Brazil | 27 |
| Taiwan | 12 |
| Global EM | 5 |
| Other DM | 4 |
| US | 1 |
| DM Funds | 1 |
| Japan | 1 |
| Other EM | 0.5 |
| Other Western Europe | 0 |
| Western Europe | 0 |
| UK-Dedicated | -2 |
| EM Funds | -3 |
| India | -5 |
| Mainland China | -23 |
</details>

Captures flows to country- and region-dedicated funds   
Source: EPFR, GS Global Investment Research

![](images/aa38719d253a80880c625c6b6050c39106099257ae650a4744ba8e6a1b59dfac.jpg)

<details>
<summary>line</summary>

| Date   | Euro Area | Rest of World |
|--------|-----------|---------------|
| Jan-24 | -1.0      | 1.0           |
| May-24 | 2.0       | 1.5           |
| Sep-24 | 3.0       | 2.0           |
| Jan-25 | 9.0       | 3.0           |
| May-25 | -4.0      | 4.0           |
| Sep-25 | 3.0       | 6.0           |
| Jan-26 | -1.0      | 3.0           |
| May-26 | 5.0       | 2.5           |
</details>

Source: EPFR, GS Global Investment Research

![](images/7c0809f632ae4c533e949cd8c925e88681fadd44a7e34db450ae191ee3a3fefc.jpg)

<details>
<summary>line</summary>

| Date   | Euro Area | Rest of World |
|--------|-----------|---------------|
| Jan-24 | 0.5       | 1.0           |
| May-24 | 2.8       | 1.2           |
| Sep-24 | 2.7       | 1.5           |
| Jan-25 | 0.0       | 0.5           |
| May-25 | -2.5      | -0.5          |
| Sep-25 | 3.2       | 0.8           |
| Jan-26 | 0.8       | 0.3           |
| May-26 | 1.5       | 0.5           |
</details>

Source: EPFR, GS Global Investment Research

Total Unhedged Foreign Flows By Country   
![](images/5b1993f0386ee0cac35e8fe80d1720faffe3982ee54220c8a6597f48e2c4c017.jpg)

<details>
<summary>line</summary>

| Year | 4-week moving avg. ($bn) | 1-year moving avg. ($bn) |
|------|---------------------------|---------------------------|
| 2019 | ~0.4                      | ~0.0                      |
| 2020 | ~-0.7                     | ~0.0                      |
| 2021 | ~0.8                      | ~0.2                      |
| 2022 | ~0.3                      | ~0.3                      |
| 2023 | ~0.7                      | ~0.1                      |
| 2024 | ~0.1                      | ~0.0                      |
| 2025 | ~0.6                      | ~0.1                      |
| 2026 | ~2.5                      | ~0.6                      |
</details>

![](images/f60acb61aaec81a7cd3cedd6c9219ae02db39ff70716b8c592d70abfa4bd165e.jpg)

<details>
<summary>line</summary>

| Year | 4-week moving avg. ($bn) | 1-year moving avg. ($bn) |
|------|---------------------------|---------------------------|
| 2019 | ~0                        | ~0                        |
| 2020 | ~-18                      | ~2                        |
| 2021 | ~8                        | ~4                        |
| 2022 | ~4                        | ~3                        |
| 2023 | ~-5                       | ~1                        |
| 2024 | ~6                        | ~3                        |
| 2025 | ~12                       | ~6                        |
| 2026 | ~8                        | ~4                        |
</details>

![](images/6febee7a98f5266b4e9da0f7b2b1fb6909211592b5ca8ba9f847947809f7d0a1.jpg)

<details>
<summary>line</summary>

| Year | 4-week moving avg. ($bn) | 1-year moving avg. ($bn) |
|------|---------------------------|---------------------------|
| 2019 | ~0                        | ~0                        |
| 2020 | ~-3                       | ~0                        |
| 2021 | ~1.5                      | ~0.5                      |
| 2022 | ~1.0                      | ~0.8                      |
| 2023 | ~0                        | ~0                        |
| 2024 | ~1.0                      | ~0.5                      |
| 2025 | ~0                        | ~0                        |
| 2026 | ~3.5                      | ~1.0                      |
</details>

![](images/6cabc9df2f2f1928a09631179f12e56fb84c5ecc94fe9a2799655222af2475d0.jpg)

<details>
<summary>line</summary>

| Year | 4-week moving avg. ($bn) | 1-year moving avg. ($bn) |
|------|---------------------------|---------------------------|
| 2019 | ~0.4                      | ~0.0                      |
| 2020 | ~-0.9                     | ~0.0                      |
| 2021 | ~0.4                      | ~0.0                      |
| 2022 | ~0.1                      | ~0.0                      |
| 2023 | ~0.3                      | ~0.0                      |
| 2024 | ~0.1                      | ~0.0                      |
| 2025 | ~0.4                      | ~0.0                      |
| 2026 | ~1.5                      | ~0.5                      |
</details>

![](images/371a5f1d4b03068ea13c8f7f1ed6c78a5d5a46bd657d5e60431d041776c78f35.jpg)

<details>
<summary>line</summary>

| Year | 4-week moving avg. ($bn) | 1-year moving avg. ($bn) |
|------|---------------------------|---------------------------|
| 2019 | -2.5                      | -0.5                      |
| 2020 | -2.8                      | -0.7                      |
| 2021 | 1.8                       | 0.8                       |
| 2022 | 1.5                       | 1.0                       |
| 2023 | -1.2                      | -0.3                      |
| 2024 | 0.5                       | 0.1                       |
| 2025 | 1.8                       | 0.5                       |
| 2026 | 3.8                       | 1.8                       |
</details>

![](images/ba4868f6a52bfd537593d4ff606bf3ff52fb6d6818d1d39a2344e5a8440e4684.jpg)

<details>
<summary>line</summary>

| Year | 4-week moving avg. ($bn) | 1-year moving avg. ($bn) |
|------|---------------------------|---------------------------|
| 2019 | ~0.5                      | ~0.3                      |
| 2020 | ~-1.5                     | ~-0.5                     |
| 2021 | ~5.0                      | ~2.5                      |
| 2022 | ~2.5                      | ~1.5                      |
| 2023 | ~3.5                      | ~0.5                      |
| 2024 | ~-1.0                     | ~-0.5                     |
| 2025 | ~4.8                      | ~-0.5                     |
| 2026 | ~2.8                      | ~1.0                      |
</details>

Source: EPFR, GS Global Investment Research

Net Unhedged Flows into US Equity Funds   
![](images/1063376ca944494b248050d9ac062648cb4f7b9c6e421609f2a2b900eb164c21.jpg)

<details>
<summary>line</summary>

| Date    | Weekly | 4-week moving avg. |
|---------|--------|---------------------|
| Jan-24  | ~0     | ~0                  |
| May-24  | ~3     | ~2                  |
| Sep-24  | ~14    | ~8                  |
| Jan-25  | ~10    | ~6                  |
| May-25  | ~-14   | ~-5                 |
| Sep-25  | ~4     | ~2                  |
| Jan-26  | ~5     | ~3                  |
| May-26  | ~6     | ~4                  |
</details>

![](images/8a3d7b1b74eb50046cb7fc22363b1f4f08bddfba6114582811357de6785582bc.jpg)

<details>
<summary>line</summary>

| Date   | Weekly | 4-week moving avg. |
|--------|--------|---------------------|
| Jan-24 | ~0.0   | ~0.0                |
| May-24 | ~0.5   | ~0.3                |
| Sep-24 | ~0.8   | ~0.6                |
| Jan-25 | ~1.3   | ~0.9                |
| May-25 | ~0.7   | ~0.5                |
| Sep-25 | ~0.3   | ~0.2                |
| Jan-26 | ~-1.5  | ~-1.8               |
| May-26 | ~-2.8  | ~-2.5               |
</details>

![](images/b0038b66a8420c85d5dcbac9683bb584911e6e6b0f1eda0266470b823cb456d8.jpg)

<details>
<summary>line</summary>

| Date    | Weekly Net Inflows ($bn) | 4-week moving avg. ($bn) |
|---------|--------------------------|---------------------------|
| Jan-24  | ~0                       | ~0                        |
| May-24  | ~0                       | ~0                        |
| Sep-24  | ~-1                      | ~-1                       |
| Jan-25  | ~1                       | ~0                        |
| May-25  | ~5                       | ~1                        |
| Sep-25  | ~-3                      | ~-2                       |
| Jan-26  | ~-6                      | ~-4                       |
| May-26  | ~3                       | ~1                        |
</details>

![](images/35b8f7259330e9368ce2f07ba3560b9bcc92f6f7b4127116a007fcae3ecad475.jpg)

<details>
<summary>line</summary>

| Date    | Weekly | 4-week moving avg. |
|---------|--------|---------------------|
| Jan-24  | ~0     | ~0                  |
| May-24  | ~0     | ~0                  |
| Sep-24  | ~-8    | ~-4                 |
| Jan-25  | ~2     | ~1                  |
| May-25  | ~2     | ~1                  |
| Sep-25  | ~-2    | ~-2                 |
| Jan-26  | ~-6    | ~-4                 |
| May-26  | ~0     | ~0                  |
</details>

![](images/314e6592ce922c7eb72e8cf041f698005be4fe6cf283ed08e922d33f783ca21f.jpg)

<details>
<summary>line</summary>

| Date   | Weekly | 4-week moving avg. |
|--------|--------|---------------------|
| Jan-24 | 0.0    | 0.0 

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
