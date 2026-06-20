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
WEEKLY FUND FLOWS

Tech Boost

## Global fund flows, week ending June 17

■ Flows into mutual funds and related investment products were positive across both equities and fixed income.  
- Net flows into global equity funds were positive again in the week ending June 17 (+\$126bn vs +\$31bn in the previous week). US funds continued to drive net inflows. Within EM, Mainland China equity funds drove the net outflows while Taiwan equity funds saw net inflows. At the sector level, technology funds saw the largest net inflows alongside industrial funds. Inflows into US technology sector funds have been particularly strong in recent weeks (see Chart of the Week) and we have noted that strong AI-led US demand has been a major factor behind higher growth, inflation and pricing for the neutral rate since the start of the year, pushing in a more Dollar positive direction.  
- Flows into global fixed income funds remained well-supported from inflows across fund types. Short-duration bond funds and inflation-protected bond funds have seen sustained inflows. In EM, hard-currency bond funds saw net inflows while local currency bond funds saw net outflows. Money market fund assets increased by \$25bn.  
Cross-border FX flows were broadly positive. USD, EUR and JPY saw the strongest net demand while CNY saw the largest net outflows.

<table><tr><td rowspan="3"></td><td colspan="4">Global Fund Flows Summary</td></tr><tr><td colspan="2">Millions USD</td><td colspan="2">% AUM</td></tr><tr><td>4wk sum</td><td>17-Jun</td><td>4wk avg</td><td>17-Jun</td></tr><tr><td>Equity</td><td>173,989</td><td>126,425</td><td>0.14</td><td>0.41</td></tr><tr><td>Fixed Income</td><td>103,830</td><td>19,160</td><td>0.26</td><td>0.19</td></tr><tr><td>of which: EM</td><td>9,341</td><td>193</td><td>0.33</td><td>0.03</td></tr><tr><td>Money Markets</td><td>166,701</td><td>25,110</td><td>0.37</td><td>0.22</td></tr><tr><td>FX Flows*</td><td>63,058</td><td>22,519</td><td>0.10</td><td>0.14</td></tr></table>

\*Cross-border fund flows, excluding hard currency and FX-hedged funds

## Lexi Kanter

+1(212)855-9701

alexandra.kanter@gs.com

GS & Co. LLC

Chart of the Week  
![](images/6b6272a97128223a659be28d7910b02c10f3f578cb2737a5ebe0ae00b885d533.jpg)

<details>
<summary>line chart</summary>

| Date     | Flow ($bn) |
| -------- | ---------- |
| Jan-22   | ~0         |
| Aug-22   | ~0         |
| Mar-23   | ~0         |
| Oct-23   | ~0         |
| May-24   | ~0         |
| Dec-24   | ~0         |
| Jul-25   | ~-10       |
| Feb-26   | ~25        |
</details>

Source: EPFR, Haver Analytics, GS Global Investment Research

## Global Fund Flow Trends

![](images/7d43d1be8e6be200d706ed9f9e0df6ccba35fc6992f27d6a35bed0de9ee0856b.jpg)

<details>
<summary>line chart</summary>

| Date   | USA (left) | Euro area (right) |
|--------|------------|-------------------|
| Jan-24 | 0          | 0                 |
| May-24 | ~100       | ~50               |
| Sep-24 | ~200       | ~100              |
| Jan-25 | ~300       | ~150              |
| May-25 | ~400       | ~250              |
| Sep-25 | ~450       | ~350              |
| Jan-26 | ~550       | ~500              |
| May-26 | ~650       | ~1300             |
</details>

Source: EPFR, GS Global Investment Research

![](images/af651f23e22249aee3ee484c3acb91fe3b5ca31524482fd75daa55a7c9ddc83e.jpg)

<details>
<summary>line chart</summary>

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

![](images/b2916d81530cf7af919b3e6fcef700024982d24097219decc5e018e6296aeb39.jpg)

<details>
<summary>line chart</summary>

| Date   | Technology | Defensives | Cyclicals ex. Tech |
|--------|------------|------------|---------------------|
| Jan-25 | -          | -          | -                   |
| Apr-25 | 4.5        | -          | -5.0                |
| Jul-25 | -          | 0.5        | 3.5                 |
| Oct-25 | 7.5        | 1.5        | 6.0                 |
| Jan-26 | 4.0        | 3.0        | 16.0                |
| Apr-26 | 1.0        | -          | 0.0                 |
| Jul-26 | 14.0       | 0.0        | 2.0                 |
</details>

Source: EPFR, GS Global Investment Research

![](images/e63619061671dbba1b36a30f4168b325a0c3f675041d334c10162b67e8a23a2c.jpg)

<details>
<summary>line chart</summary>

Cumulative Global Equity Flows by Sector % AUM
| Sector | Jan-24 (%) | May-24 (%) | Sep-24 (%) | Jan-25 (%) | May-25 (%) | Jan-26 (%) | May-26 (%) |
|---|---|---|---|---|---|---|---|
| Commodities/Materials | ~0 | ~10 | ~15 | ~20 | ~30 | ~35 | ~40 |
| Consumer Goods | ~0 | ~5 | ~10 | ~15 | ~20 | ~25 | ~30 |
| Energy | ~0 | ~-10 | ~-15 | ~-10 | ~-5 | ~-10 | ~-15 |
| Financials | ~0 | ~5 | ~10 | ~15 | ~20 | ~25 | ~30 |
| Health Care/Biotech | ~0 | ~10 | ~15 | ~20 | ~25 | ~30 | ~35 |
| Industrials | ~0 | ~15 | ~20 | ~25 | ~30 | ~35 | ~40 |
| Infrastructure | ~0 | ~10 | ~15 | ~20 | ~25 | ~30 | ~35 |
| Real Estate | ~0 | ~5 | ~10 | ~15 | ~20 | ~25 | ~30 |
| Technology | ~0 | ~10 | ~15 | ~20 | ~25 | ~30 | ~35 |
| Telecom | ~0 | ~5 | ~10 | ~15 | ~20 | ~25 | ~30 |
| Utilities | ~0 | ~-10 | ~-15 | ~-10 | ~-5 | ~-10 | ~-15 |
</details>

Captures flows to sector-dedicated funds

Source: EPFR, GS Global Investment Research  
![](images/f54a616290a8594728133834e469b4833852d298e78ef69b93d88c873b2e81b2.jpg)

<details>
<summary>line chart</summary>

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

![](images/8183bd4d1ba166f2caa224ae00fd97c9bf84af76c16129d1c743b07eb972c7b4.jpg)

<details>
<summary>bar chart</summary>

Cumulative Global Equity Flows by Sector YTD (% AUM)
| Sector | Cumulative Global Equity Flows (%) |
|---|---|
| Industrials | 27.5 |
| Infrastructure | 17.5 |
| Energy | 14.5 |
| Commodities/Materials | 11.0 |
| Technology | 5.5 |
| Telecom | 3.0 |
| Utilities | 0.5 |
| Real Estate | 0.2 |
| Health Care/Biotech | -0.5 |
| Financials | -1.0 |
| Consumer Goods | -6.0 |
</details>

Captures flows to sector dedicated funds

Source: EPFR, GS Global Investment Research  
![](images/27247cb511feacbd4b53aa53090b8e408ff3415d8eb55d3972277fb7c42dc87a.jpg)

<details>
<summary>bar chart</summary>

Cumulative Global Equity Flows by Region YTD (% AUM)
| Region | Cumulative Global Equity Flows (%) |
|---|---|
| Mainland China | -25 |
| India | -7 |
| EM Funds | -3 |
| UK-Dedicated | -1 |
| Western Europe | 0.5 |
| Other Western Europe | 0.5 |
| Other EM | 0.5 |
| Japan | 1 |
| DM Funds | 2 |
| US | 2 |
| Global EM | 4 |
| Other DM | 5 |
| Taiwan | 17 |
| Brazil | 24 |
| Korea | 44 |
</details>

Captures flows to country- and region-dedicated funds  
Source: EPFR, GS Global Investment Research

![](images/76df9ac331917345fa1fce2b05820a82aac16b1b2a88f283193488674b4e0882.jpg)

<details>
<summary>line chart</summary>

| Date   | Euro Area | Rest of World |
|--------|-----------|---------------|
| Jan-24 | -1        | 1             |
| May-24 | 2         | 1             |
| Sep-24 | 3         | 2             |
| Jan-25 | 9         | 3             |
| May-25 | -4        | 4             |
| Sep-25 | 3         | 6             |
| Jan-26 | -1        | 3             |
| May-26 | 5         | 4             |
</details>

Source: EPFR, GS Global Investment Research

![](images/81a5e61b40f794793f4401c1db8a006c28dea4257c88a692b7617923578a270a.jpg)

<details>
<summary>line chart</summary>

| Date   | Euro Area | Rest of World |
|--------|-----------|---------------|
| Jan-24 | 0.5       | 0.8           |
| May-24 | 2.8       | 1.2           |
| Sep-24 | 2.7       | 1.5           |
| Jan-25 | 0.0       | -0.5          |
| May-25 | -2.8      | -0.8          |
| Sep-25 | 3.2       | 0.5           |
| Jan-26 | 0.8       | 0.3           |
| May-26 | 1.8       | 0.0           |
</details>

Source: EPFR, GS Global Investment Research

Total Unhedged Foreign Flows By Country  
![](images/9c3c8199e1a11f6f785a832cc7a49a5976f8dc61d81c6f19042b3b765b5c9137.jpg)

<details>
<summary>line chart</summary>

| Year | 4-week moving avg. ($bn) | 1-year moving avg. ($bn) |
|------|---------------------------|---------------------------|
| 2019 | ~0.4                      | ~0.0                      |
| 2020 | ~-0.7                     | ~0.0                      |
| 2021 | ~0.8                      | ~0.2                      |
| 2022 | ~0.3                      | ~0.3                      |
| 2023 | ~0.7                      | ~0.1                      |
| 2024 | ~0.1                      | ~0.0                      |
| 2025 | ~0.6                      | ~0.1                      |
| 2026 | ~2.6                      | ~0.6                      |
</details>

![](images/d4e2ca65e2721c85d2b8a7260a46f48c862f10f157a246712cc0c6c200f5c44f.jpg)

<details>
<summary>line chart</summary>

| Year | 4-week moving avg. ($bn) | 1-year moving avg. ($bn) |
|------|---------------------------|---------------------------|
| 2019 | -5                        | -1                        |
| 2020 | -18                       | 2                         |
| 2021 | 8                         | 4                         |
| 2022 | 5                         | 3                         |
| 2023 | -5                        | 1                         |
| 2024 | 6                         | 3                         |
| 2025 | 12                        | 6                         |
| 2026 | 10                        | 5                         |
</details>

![](images/2690a48515aa750ab464c3c0eaca0ecfba55a8098390ec91cab6f70a586aaa1d.jpg)

<details>
<summary>line chart</summary>

| Year | 4-week moving avg. ($bn) | 1-year moving avg. ($bn) |
|------|---------------------------|---------------------------|
| 2019 | ~0                        | ~0                        |
| 2020 | ~-3                       | ~-0.5                     |
| 2021 | ~1.8                      | ~0.5                      |
| 2022 | ~1.2                      | ~0.8                      |
| 2023 | ~0                        | ~0                        |
| 2024 | ~1.0                      | ~0.5                      |
| 2025 | ~0                        | ~0                        |
| 2026 | ~3.5                      | ~1.0                      |
</details>

![](images/859b003e45987a0d593e4dee419db8c56fb2712bf3f6c47422b12cfbde2321a5.jpg)

<details>
<summary>line chart</summary>

| Year | 4-week moving avg. ($bn) | 1-year moving avg. ($bn) |
|------|---------------------------|---------------------------|
| 2019 | ~0.4                      | ~0.0                      |
| 2020 | ~-0.8                     | ~0.0                      |
| 2021 | ~0.4                      | ~0.0                      |
| 2022 | ~0.1                      | ~0.0                      |
| 2023 | ~0.3                      | ~0.0                      |
| 2024 | ~0.1                      | ~0.0                      |
| 2025 | ~0.4                      | ~0.0                      |
| 2026 | ~1.5                      | ~0.5                      |
</details>

![](images/486089e17d0d5b16e8d6836276a3f266adeae9dca25688d7f88087a8067c0a0a.jpg)

<details>
<summary>line chart</summary>

| Year | 4-week moving avg. ($bn) | 1-year moving avg. ($bn) |
|------|---------------------------|---------------------------|
| 2019 | -2.5                      | -0.5                      |
| 2020 | -3.0                      | -0.8                      |
| 2021 | 1.5                       | 0.5                       |
| 2022 | 1.8                       | 1.0                       |
| 2023 | -1.0                      | -0.5                      |
| 2024 | 0.5                       | 0.0                       |
| 2025 | 1.5                       | 0.5                       |
| 2026 | 3.5                       | 1.5                       |
</details>

![](images/d9615e0373072ae0e293dad47377540822c03150e49f72d7d06e17cc3aff89d9.jpg)

<details>
<summary>line chart</summary>

| Year | 4-week moving avg. ($bn) | 1-year moving avg. ($bn) |
|------|---------------------------|---------------------------|
| 2019 | ~0.5                      | ~0.3                      |
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
![](images/906ce2f01c675194d5879a914ade0edcc4dc61c045a103bbac9a245fd67ec446.jpg)

<details>
<summary>line chart</summary>

| Date    | Weekly | 4-week moving avg. |
|---------|--------|---------------------|
| Jan-24  | ~0     | ~0                  |
| Jun-24  | ~2     | ~1                  |
| Nov-24  | ~14    | ~8                  |
| Apr-25  | ~-13   | ~-5                 |
| Sep-25  | ~4     | ~2                  |
| Feb-26  | ~-5    | ~0                  |
| Jul-26  | ~5     | ~3                  |
</details>

![](images/4954955dfb16bde867bfe20ee284b766aea41476a9ab9bc945931eff2a91faa0.jpg)

<details>
<summary>line chart</summary>

| Date    | Weekly | 4-week moving avg. |
|---------|--------|---------------------|
| Jan-24  | 0.0    | 0.0                 |
| Jun-24  | 0.5    | 0.3                 |
| Nov-24  | 1.3    | 0.8                 |
| Apr-25  | 0.7    | 0.5                 |
| Sep-25  | 0.8    | 0.6                 |
| Feb-26  | -2.8   | -2.5                |
| Jul-26  | 1.8    | 1.5                 |
</details>

![](images/9bcf68c1b11055a9d4731610484fe17d6e958d9236220a3f1bc1b6849d3ec89e.jpg)

<details>
<summary>line chart</summary>

| Date    | Weekly Net Inflows ($bn) | 4-week moving avg. ($bn) |
|---------|--------------------------|---------------------------|
| Jan-24  | ~0                       | ~0                        |
| Jun-24  | ~0                       | ~0                        |
| Nov-24  | ~1.5                     | ~0.5                      |
| Apr-25  | ~5                       | ~3                        |
| Sep-25  | ~-6                      | ~-5                       |
| Feb-26  | ~-5                      | ~-4                       |
| Jul-26  | ~3                       | ~2                        |
</details>

![](images/bcc801bed1e6d1ab49f1e0e81c2bbe44efdab4c0fc56104278d5ff27f271d224.jpg)

<details>
<summary>line chart</summary>

| Date    | Weekly | 4-week moving avg. |
|---------|--------|---------------------|
| Nov-24  | -8.0   | -3.0                |
| Feb-26  | -6.0   | -2.0                |
| Jul-26  | 1.0    | 0.0                 |
</details>

![](images/ada2245946e7885e92780fe4d7b1b421a26de9ae6f229277fd04b88ead2f20a0.jpg)

<details>
<summary>line chart</summary>

| Date    | Weekly | 4-week moving avg. |
|---------|--------|---------------------|
| Jan-24  | 0.0    | 0.0                 |
| Jun-24  | 0.2    | 0.1                 |
| Nov-24  | 0.3    | 0.2                 |
| Apr-25  | -0.4   | -0.3                |
| Sep-25  | -0.2   | -0.1                |
| Feb-26  | -1.2   | -1.0                |
| Jul-26  | 0.6    | 0.5                 |
</details>

![](images/821278064cf4a30fa49fb039736d569b7a04c3b56a5817d92ce56ee5f89e98fb.jpg)

<details>
<summary>line chart</summary>

| Date    | Weekly Net Inflows ($bn) | 4-week moving avg. Net Inflows ($bn) |
|---------|---------------------------|----------------------------------------|
| Jan-24  | ~0                        | ~0                                     |
| Jun-24  | ~0                        | ~0                                     |
| Nov-24  | ~0                        | ~0                                     |
| Apr-25  | ~0                        | ~0                                     |
| Sep-25  | ~14                       | ~5                                     |
| Feb-26  | ~0                        | ~0                                     |
| Jul-26  | ~0                        | ~0                                     |
</details>

Source: EPFR, Haver Analytics, GS Global Invest

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
