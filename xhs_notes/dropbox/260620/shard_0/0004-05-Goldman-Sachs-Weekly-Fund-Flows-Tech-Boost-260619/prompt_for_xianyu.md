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
| Nov

[中间内容因长度限制已省略]

ttempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

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
