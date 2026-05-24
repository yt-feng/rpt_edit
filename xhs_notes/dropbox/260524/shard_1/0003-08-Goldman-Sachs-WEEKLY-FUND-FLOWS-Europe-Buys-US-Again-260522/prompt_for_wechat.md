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

Europe Buys US Again

# Global fund flows, week ending May 20

■ Flows into mutual funds and related investment products were positive across both equities and fixed income.   
- Net flows into global equity funds remained positive in the week ending May 20 (+\$2bn vs +\$20bn in the previous week). Global benchmark funds led the net inflows, with US funds seeing strong demand. Within EM, global EM benchmark funds and Mainland China equity funds saw net outflows; Korea equity funds saw renewed net inflows. At the sector level, financials funds saw the largest net outflows. Technology sector funds saw the largest net inflows across sectors.   
Flows into global fixed income funds were well-supported from inflows into government and agg-type bond funds. US Treasury funds have seen cumulative inflows from the Euro Area since the start of the year, but cumulative outflows from Asia (see Chart of the Week). We see this as consistent with our view that a more range-bound Dollar over the course of the energy shock has been due, in part, to more stringent FX management. Short-duration bond funds and inflation-protected bond funds have also seen sustained inflows. In EM, local-currency bond funds saw net inflows while hard-currency bond funds saw net outflows. Money market fund assets rose by \$1bn.   
Cross-border FX flows were broadly positive, indicating supported risk sentiment. Foreign flows were positive across regions, with DM and Mainland China seeing particularly strong net inflows.

<table><tr><td rowspan="3"></td><td colspan="4">Global Fund Flows Summary</td></tr><tr><td colspan="2">Millions USD</td><td colspan="2">% AUM</td></tr><tr><td>4wk sum</td><td>20-May</td><td>4wk avg</td><td>20-May</td></tr><tr><td>Equity</td><td>48,460</td><td>2,385</td><td>0.04</td><td>0.01</td></tr><tr><td>Fixed Income</td><td>109,304</td><td>31,975</td><td>0.28</td><td>0.33</td></tr><tr><td>of which: EM</td><td>9,429</td><td>2,163</td><td>0.34</td><td>0.31</td></tr><tr><td>Money Markets</td><td>113,489</td><td>1,220</td><td>0.26</td><td>0.01</td></tr><tr><td>FX Flows*</td><td>65,299</td><td>17,493</td><td>0.10</td><td>0.11</td></tr></table>

\*Cross-border fund flows, excluding hard currency and FX-hedged funds   
Source: EPFR, Haver Analytics, GS Global Investment Research

# Lexi Kanter

+1(212)855-9701

alexandra.kanter@gs.com

GS & Co. LLC

Chart of the Week   
![](images/2556cd24f14f25b720e5b67e197aa0784923d6c4ce031fcc8e47d45cfce6eedb.jpg)

<details>
<summary>line</summary>

| Date   | Asia ($bn) | Euro Area ($bn) |
|--------|------------|-----------------|
| Jan-25 | 0          | 0               |
| Mar-25 | -1         | 2               |
| May-25 | -3         | 4.5             |
| Jul-25 | -2         | 2.5             |
| Sep-25 | -1         | 4.5             |
| Nov-25 | -2         | 6.5             |
| Jan-26 | -2         | 7.5             |
| Mar-26 | -4         | 6               |
| May-26 | -5         | 11              |
</details>

Source: EPFR, Haver Analytics, GS Global Investment Research

# Global Fund Flow Trends

![](images/9f8cca2871fffb493d4f758ab5951f6739aec9c14a1ad4ec615f1cc48c937050.jpg)

<details>
<summary>line</summary>

| Date   | USA (left) | Euro area (right) |
|--------|------------|-------------------|
| Jan-24 | 0          | 0                 |
| May-24 | ~100       | ~50               |
| Sep-24 | ~200       | ~100              |
| Jan-25 | ~300       | ~150              |
| May-25 | ~400       | ~250              |
| Sep-25 | ~450       | ~350              |
| Jan-26 | ~550       | ~500              |
| May-26 | ~600       | ~1200             |
</details>

Source: EPFR, GS Global Investment Research

![](images/f3bfbe1a5af10caf320fef78deb9ba477b1134856c67e5395313644e9438001d.jpg)

<details>
<summary>line</summary>

| Date   | Flows into Mainland China Equity Funds from Mainland China ($bn) | Flows into Mainland China Equity Funds from Rest of World ($bn) |
|--------|---------------------------------------------------------------|------------------------------------------------------------------|
| Jan-23 | ~0                                                            | ~0                                                               |
| Aug-23 | ~0                                                            | ~0                                                               |
| Mar-24 | ~10                                                           | ~0                                                               |
| Oct-24 | ~30                                                           | ~5                                                               |
| May-25 | ~25                                                           | ~0                                                               |
| Dec-25 | ~10                                                           | ~0                                                               |
| Jul-26 | ~-20                                                          | ~0                                                               |
</details>

Source: EPFR, GS Global Investment Research

![](images/2772b72a3289997345520d7c5b22386fa0cc3ac993cffd7b0e35cf8fb8e0ee92.jpg)

<details>
<summary>line</summary>

| Date   | Technology | Defensives | Cyclicals ex. Tech |
|--------|------------|------------|---------------------|
| Jan-25 | -2         | -1         | 0                   |
| Apr-25 | 5          | -3         | -6                  |
| Jul-25 | 0          | 0          | 4                   |
| Oct-25 | 8          | 2          | 6                   |
| Jan-26 | 4          | 3          | 16                  |
| Apr-26 | 0          | -1         | 0                   |
</details>

Source: EPFR, GS Global Investment Research

![](images/e83503a9b37c2f6792e1c6107b66b430b8b4b25923e7b8c8adec9aa5de5f2285.jpg)

<details>
<summary>line</summary>

| Sector                  | Cumulative % AUM |
| ----------------------- | ----------------- |
| Commodities/Materials   | 30                |
| Consumer Goods          | 25                |
| Energy                  | -10               |
| Financials              | -15               |
| Health Care/Biotech     | -10               |
| Industrials             | 10                |
| Infrastructure          | 20                |
| Real Estate             | 15                |
| Technology              | 25                |
| Telecom                 | 20                |
| Utilities               | 15                |
</details>

Captures flows to sector dedicated funds

Source: EPFR, GS Global Investment Research   
![](images/9daaba85f1a79a0f79ae754df1b9026de0a40ea47a0ec4341111ca546eaa2091.jpg)

<details>
<summary>line</summary>

| Region           | Cumulative % AUM |
| ---------------- | ---------------- |
| US               | ~0%              |
| Western Europe   | ~0%              |
| UK-Dedicated     | ~0%              |
| Japan            | ~0%              |
| Global EM        | ~0%              |
| Mainland China   | ~0%              |
| Taiwan           | ~0%              |
| Korea            | ~0%              |
| India            | ~0%              |
| Brazil           | ~0%              |
</details>

Captures flows to country- and region-dedicated funds   
Source: EPFR, GS Global Investment Research

![](images/5d0d49de9214e65308156690db01d06d73e09343a4fea13af6c31e4f49a3cf6a.jpg)

<details>
<summary>bar</summary>

Cumulative Global Equity Flows by Sector YTD (% AUM)
| Sector | Cumulative Global Equity Flows (%) |
|---|---|
| Industrials | 21.5 |
| Energy | 16.5 |
| Infrastructure | 15.0 |
| Commodities/Materials | 11.5 |
| Technology | 3.0 |
| Telecom | 2.5 |
| Utilities | 0.5 |
| Real Estate | -0.5 |
| Health Care/Biotech | -0.5 |
| Financials | -1.0 |
| Consumer Goods | -4.5 |
</details>

Captures flows to sector dedicated funds

Source: EPFR, GS Global Investment Research   
![](images/49be8616c855fdc0283a6892d10a7b6886f84fe54bba6a123df2264ebc34c2fb.jpg)

<details>
<summary>bar</summary>

Cumulative Global Equity Flows by Region YTD (% AUM)
| Region | Cumulative Global Equity Flows (%) |
|---|---|
| Korea | 38 |
| Brazil | 27 |
| Taiwan | 11 |
| Global EM | 5 |
| Other DM | 4 |
| Japan | 2 |
| US | 1 |
| DM Funds | 1 |
| Other EM | 1 |
| Other Western Europe | 0 |
| Western Europe | 0 |
| UK-Dedicated | -2 |
| EM Funds | -3 |
| India | -5 |
| Mainland China | -22 |
</details>

Captures flows to country- and region-dedicated funds   
Source: EPFR, GS Global Investment Research

![](images/aefc47301f5b995da5105ea93a54960cfa9338307d8be347739f6b9260a66603.jpg)

<details>
<summary>line</summary>

| Date   | Euro Area | Rest of World |
|--------|-----------|---------------|
| Jan-24 | -1        | 1             |
| May-24 | 2         | 1             |
| Sep-24 | 3         | 2             |
| Jan-25 | 9         | 3             |
| May-25 | -4        | 4             |
| Sep-25 | 3         | 6             |
| Jan-26 | -1        | 3             |
| May-26 | 5         | 2             |
</details>

Source: EPFR, GS Global Investment Research

![](images/26d1c36f25431056685a0b9d6480b2d097ced42ddf5307413074ee7a7472840d.jpg)

<details>
<summary>line</summary>

| Date   | Euro Area | Rest of World |
|--------|-----------|---------------|
| Jan-24 | 0.5       | 0.8           |
| May-24 | 2.8       | 1.2           |
| Sep-24 | 2.7       | 1.5           |
| Jan-25 | 0.0       | -0.5          |
| May-25 | -2.8      | -0.8          |
| Sep-25 | 3.2       | 0.5           |
| Jan-26 | 0.8       | 0.3           |
| May-26 | -1.5      | -0.5          |
</details>

Source: EPFR, GS Global Investment Research

Total Unhedged Foreign Flows By Country   
![](images/67cdbd65d8a6e5401d4eb6443c1c922b5285dff12ccf37d135f03df34a503ec5.jpg)

<details>
<summary>line</summary>

| Year | 4-week moving avg. ($bn) | 1-year moving avg. ($bn) |
|------|---------------------------|---------------------------|
| 2019 | ~0.4                      | ~0.0                      |
| 2020 | ~-0.7                     | ~0.0                      |
| 2021 | ~0.8                      | ~0.3                      |
| 2022 | ~0.3                      | ~0.2                      |
| 2023 | ~0.7                      | ~0.1                      |
| 2024 | ~0.1                      | ~0.0                      |
| 2025 | ~0.6                      | ~0.1                      |
| 2026 | ~2.5                      | ~0.6                      |
</details>

![](images/d24b53e0ea9f84af697418f2c0f93a2ad713d7ad615f6e852f47b121a8a09097.jpg)

<details>
<summary>line</summary>

| Year | 4-week moving avg. ($bn) | 1-year moving avg. ($bn) |
|------|---------------------------|---------------------------|
| 2019 | -5                        | -1                        |
| 2020 | -18                       | 2                         |
| 2021 | 8                         | 4                         |
| 2022 | 5                         | 3                         |
| 2023 | -5                        | 1                         |
| 2024 | 6                         | 3                         |
| 2025 | 12                        | 6                         |
| 2026 | 8                         | 4                         |
</details>

![](images/5ad8da31d9f19b29d0e00fa442d5b99cb5b25961eb759a9bf3df948ad4027d0b.jpg)

<details>
<summary>line</summary>

| Year | 4-week moving avg. ($bn) | 1-year moving avg. ($bn) |
|------|---------------------------|---------------------------|
| 2019 | ~0                        | ~0                        |
| 2020 | ~-3                       | ~0                        |
| 2021 | ~1.5                      | ~0.5                      |
| 2022 | ~1.0                      | ~1.0                      |
| 2023 | ~0                        | ~0                        |
| 2024 | ~1.0                      | ~0.5                      |
| 2025 | ~0                        | ~0                        |
| 2026 | ~3.5                      | ~1.0                      |
</details>

![](images/6d33b2bd2741c7ce970453967987ddce1d4a11815130ca5ca427298acfc9ceac.jpg)

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

![](images/21839268ddb3edf674ae9ca3a5d32a0e1713cc4103be15047853baf2737e7c67.jpg)

<details>
<summary>line</summary>

| Year | 4-week moving avg. ($bn) | 1-year moving avg. ($bn) |
|------|---------------------------|---------------------------|
| 2019 | -2.5                      | -0.5                      |
| 2020 | -1.0                      | -0.8                      |
| 2021 | 1.5                       | 0.5                       |
| 2022 | 1.8                       | 1.0                       |
| 2023 | -0.5                      | -0.2                      |
| 2024 | 0.8                       | 0.3                       |
| 2025 | 1.2                       | 0.7                       |
| 2026 | 3.8                       | 1.8                       |
</details>

![](images/7e576c1d7cdee2f206ed04b5155e9dd218a6fadec9b9af1bdb7a787fcc8bbe0b.jpg)

<details>
<summary>line</summary>

| Year | 4-week moving avg. ($bn) | 1-year moving avg. ($bn) |
|------|---------------------------|---------------------------|
| 2019 | ~0.5                      | ~0.0                      |
| 2020 | ~-2.5                     | ~-0.5                     |
| 2021 | ~5.0                      | ~2.5                      |
| 2022 | ~2.5                      | ~1.5                      |
| 2023 | ~3.5                      | ~0.5                      |
| 2024 | ~-1.0                     | ~-0.5                     |
| 2025 | ~4.8                      | ~-0.5                     |
| 2026 | ~2.8                      | ~1.0                      |
</details>

Source: EPFR, GS Global Investment Research

Net Unhedged Flows into US Equity Funds   
![](images/e009fa07e69b98622d9b248bbb0f876a88fe4a080c09176580800f22b37453cf.jpg)

<details>
<summary>line</summary>

| Date    | Weekly | 4-week moving avg. |
|---------|--------|---------------------|
| Jan-24  | ~0     | ~0                  |
| May-24  | ~3     | ~2                  |
| Sep-24  | ~5     | ~4                  |
| Jan-25  | ~14    | ~8                  |
| May-25  | ~-13   | ~-5                 |
| Sep-25  | ~4     | ~3                  |
| Jan-26  | ~5     | ~2                  |
| May-26  | ~6     | ~4                  |
</details>

![](images/55dfe212c8d3cc9b411aa2db64047554e27a1725686d011f4c9e1930a14b6caf.jpg)

<details>
<summary>line</summary>

| Date   | Weekly | 4-week moving avg. |
|--------|--------|---------------------|
| Jan-24 | 0.0    | 0.0                 |
| May-24 | 0.5    | 0.3                 |
| Sep-24 | 0.8    | 0.6                 |
| Jan-25 | 1.3    | 0.9                 |
| May-25 | 0.7    | 0.5                 |
| Sep-25 | 0.9    | 0.7                 |
| Jan-26 | -1.5   | -1.2                |
| May-26 | 1.8    | 1.5                 |
</details>

![](images/1b23c130dc587e3fb147c73c88ed41fedfaaa35593d0dd6367dc7e925cb66f23.jpg)

<details>
<summary>line</summary>

| Date   | Weekly Net Inflows ($bn) | 4-week moving avg. ($bn) |
|--------|--------------------------|---------------------------|
| Jan-24 | ~0                       | ~0                        |
| May-24 | ~0                       | ~0                        |
| Sep-24 | ~-1                      | ~-1                       |
| Jan-25 | ~4.5                     | ~1                        |
| May-25 | ~2.5                     | ~0                        |
| Sep-25 | ~-1                      | ~-1                       |
| Jan-26 | ~-6                      | ~-3                       |
| May-26 | ~2.5                     | ~0                        |
</details>

![](images/6d0c9451aa85204ffcd64ab78975779c82ce3e931cb06502148940585d2bb78e.jpg)

<details>
<summary>line</summary>

| Date    | Weekly | 4-week moving avg. |
|---------|--------|---------------------|
| Jan-24  | ~0.5   | ~0.3                |
| May-24  | ~0.2   | ~0.1                |
| Sep-24  | ~-8.5  | ~-4.0               |
| Jan-25  | ~2.5   | ~1.5                |
| May-25  | ~2.0   | ~1.0                |
| Sep-25  | ~-1.0  | ~-0.5               |
| Jan-26  | ~-6.0  | ~-3.0               |
| May-26  | ~-1.5  | ~-1.0               |
</details>

![](images/0015f5e534fabccd27de92aa10913faf4f5314fc73f9f3eb866d90ab7c41168d.jpg)

<details>
<summary>line</summary>

| Date   | Weekly | 4-week moving avg. |
|--------|--------|---------------------|
| Jan-24 | 0.0    | 0.0                 |
| May-24 | 0.2    | 0.1                 |
| Sep-24 | 0.3    | 0.2                 |
| Jan-25 | 0.4    | 0.1                 |
| May-25 | -0.4   | -0.2                |
| Sep-25 | -0.2   | -0.1                |
| Jan-26 | -1.2   | -0.8                |
| May-26 | -1.6   | -1.4                |
</details>

![](images/dc909cec62a2520fc80d72db10f5f484b6ebe3e62c69b20709f59a16746f2bd5.jpg)

<details>
<summary>line</summary>

| Date    | Weekly | 4-week moving avg. |
|---------|--------|---------------------|
| Jan-24  | ~0     | ~0                  |
| May-24  | ~0     | ~0                  |
| Sep-24  | ~0     | ~0                  |
| Jan-25  | ~0     | ~0                  |
| May-25  | ~0     | ~0                  |
| Sep-25  | ~14    | ~5                  |
| Jan-26  | ~0     | ~0                  |
| May-26  | ~0     | ~0                  |
</details>

Source: EPFR, Haver Analytics, GS Global Investment Research

Fixed Income & Equity Flows 

<table><tr><td rowspan="3"></td><td colspan="8">Global Fund Flows</td></tr><tr><td colspan="5">Millions USD</td><td colspan="2">% AUM</td><td rowspan="2">Z-score of 4wk sum</td></tr><tr><td>4wk sum</td><td>20-May</td><td>13-May</td><td>6-May</td><td>29-Apr</td><td>4wk avg</td><td>20-May</td></tr><tr><td>Total Equity</td><td>48,460</td><td>2,385</td><td>20,458</td><td>2,574</td><td>23,042</td><td>0.04</td><td>0.01</td><td>-0.11</td></tr>

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
