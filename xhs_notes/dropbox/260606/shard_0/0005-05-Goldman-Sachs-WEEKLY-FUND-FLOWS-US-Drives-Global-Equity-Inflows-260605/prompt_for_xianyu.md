你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  ✅ 三大情景框架：DCF、P/ARR、EV/Sales
  ✅ 关键变量分析
  ✅ 估值逻辑、假设、终值占比等核心内容覆盖
  ✅ 适合准备 AI 相关面试、研究 AI 估值的同学
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

# US Drives Global Equity Inflows

# Global fund flows, week ending June 3

■ Flows into mutual funds and related investment products were positive across both equities and fixed income.   
- Net flows into global equity funds turned positive again in the week ending June 3 (+\$23bn vs -\$7bn in the previous week). US funds continued to see demand while elsewhere in DM largely saw net outflows. Within EM, global EM benchmark funds, Mainland China equity funds, and Korea equity funds drove the net outflows while Taiwan equity funds saw net inflows. At the sector level, financial sector and consumer goods funds saw the largest net outflows. Industrial sector funds saw the largest net inflows across sectors.   
- Flows into global fixed income funds remained well-supported from inflows across fund types. Short-duration bond funds and inflation-protected bond funds have seen sustained inflows while long-duration funds saw net outflows. In EM, local-currency bond funds and hard-currency bond funds saw net inflows. Money market fund assets rose by \$122bn.   
Cross-border FX flows were broadly positive. USD saw the strongest net demand while CNY saw the largest net outflows. GBP flows have also remained well-supported this year (see Chart of the Week). We've noted that recent data suggest the UK has seen larger-than-usual net cross-border M&A inflows so far this year, which we see as a potential source of resilience despite domestic political and fiscal risks.

<table><tr><td rowspan="3"></td><td colspan="4">Global Fund Flows Summary</td></tr><tr><td colspan="2">Millions USD</td><td colspan="2">% AUM</td></tr><tr><td>4wk sum</td><td>3-Jun</td><td>4wk avg</td><td>3-Jun</td></tr><tr><td>Equity</td><td>38,914</td><td>23,118</td><td>0.03</td><td>0.07</td></tr><tr><td>Fixed Income</td><td>125,129</td><td>40,422</td><td>0.32</td><td>0.41</td></tr><tr><td>of which: EM</td><td>13,849</td><td>6,264</td><td>0.49</td><td>0.88</td></tr><tr><td>Money Markets</td><td>151,041</td><td>122,128</td><td>0.34</td><td>1.09</td></tr><tr><td>FX Flows*</td><td>70,363</td><td>19,761</td><td>0.11</td><td>0.12</td></tr></table>

\*Cross-border fund flows, excluding hard currency and FX-hedged funds   
Source: EPFR, Haver Analytics, GS Global Investment Research

# Lexi Kanter

+1(212)855-9701

alexandra.kanter@gs.com

GS & Co. LLC

Chart of the Week   
![](images/ec43d957dafbc53eece42c39bbd1dbd308f84d413f103d7e3994756e4531499f.jpg)

<details>
<summary>line</summary>

| Year | 4-week moving avg. ($bn) | 1-year moving avg. ($bn) |
|------|---------------------------|---------------------------|
| 2010 | ~0.0                      | ~0.0                      |
| 2012 | ~-0.5                     | ~-0.2                     |
| 2014 | ~0.8                      | ~0.4                      |
| 2016 | ~-0.3                     | ~0.2                      |
| 2018 | ~1.2                      | ~0.6                      |
| 2020 | ~-2.0                     | ~-0.5                     |
| 2022 | ~1.5                      | ~0.8                      |
| 2024 | ~0.5                      | ~0.2                      |
| 2026 | ~2.8                      | ~1.4                      |
</details>

Source: EPFR, Haver Analytics, GS Global Investment Research, Bloomberg

# Global Fund Flow Trends

![](images/27bde677832dca5dacada175f7497f56a9bf8bbc3441a3663ed463efbaf43915.jpg)

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
| May-26 | ~650       | ~1300             |
</details>

Source: EPFR, GS Global Investment Research

![](images/ff6d207997a9fc6ed14b99d9ea99fbecd0e8abe738da7fffdd55b5834817b400.jpg)

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

![](images/9f07dfc4b469c11d71b822d9cd542fd47c6a6dea299584d10a7fd7f809dbd38b.jpg)

<details>
<summary>line</summary>

| Date   | Technology | Defensives | Cyclicals ex. Tech |
|--------|------------|------------|---------------------|
| Jan-25 | -2         | -1         | -1                  |
| Apr-25 | 4          | -3         | -6                  |
| Jul-25 | -3         | 0          | 0                   |
| Oct-25 | 8          | 1          | 6                   |
| Jan-26 | 4          | 3          | 16                  |
| Apr-26 | 1          | -1         | 0                   |
| Jul-26 | 5          | 0          | -2                  |
</details>

Source: EPFR, GS Global Investment Research

![](images/74dbcf11048036bddc20a23be597ba2580a9610a006fa93ec5792d2ed5ded887.jpg)

<details>
<summary>line</summary>

Cumulative Global Equity Flows by Sector % AUM
| Sector | Jan-24 (%) | May-24 (%) | Sep-24 (%) | Jan-25 (%) | May-25 (%) | Sep-25 (%) | Jan-26 (%) | May-26 (%) |
|---|---|---|---|---|---|---|---|---|
| Commodities/Materials | ~0 | ~0 | ~0 | ~10 | ~30 | ~35 | ~30 | ~25 |
| Consumer Goods | ~0 | ~0 | ~0 | ~5 | ~5 | ~10 | ~15 | ~10 |
| Energy | ~0 | ~0 | ~0 | ~-10 | ~-5 | ~-15 | ~-10 | ~-10 |
| Financials | ~0 | ~0 | ~0 | ~5 | ~5 | ~10 | ~15 | ~10 |
| Health Care/Biotech | ~0 | ~0 | ~0 | ~10 | ~10 | ~15 | ~20 | ~15 |
| Industrials | ~0 | ~0 | ~0 | ~15 | ~20 | ~30 | ~40 | ~120 |
| Infrastructure | ~0 | ~0 | ~0 | ~10 | ~15 | ~25 | ~35 | ~45 |
| Real Estate | ~0 | ~0 | ~0 | ~5 | ~5 | ~10 | ~15 | ~20 |
| Technology | ~0 | ~0 | ~0 | ~10 | ~15 | ~20 | ~25 | ~25 |
| Telecom | ~0 | ~0 | ~0 | ~5 | ~10 | ~15 | ~20 | ~25 |
| Utilities | ~0 | ~0 | ~0 | ~-5 | ~-10 | ~-5 | ~-15 | ~-10 |
</details>

Captures flows to sector dedicated funds

Source: EPFR, GS Global Investment Research   
![](images/ef2d7b740cb591d73c8fc7bd5a2091e4de123f68d4b90a5d505a9d2c28890fd6.jpg)

<details>
<summary>line</summary>

Cumulative Global Equity Flows by Region % AUM
| Region | Jan-24 (%) | May-24 (%) | Sep-24 (%) | Jan-25 (%) | May-25 (%) | Sep-25 (%) | Jan-26 (%) | May-26 (%) |
|---|---|---|---|---|---|---|---|---|
| US | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Western Europe | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| UK-Dedicated | -10 | -15 | -10 | -5 | -5 | -10 | -15 | -20 |
| Japan | 10 | 15 | 30 | 10 | 35 | 15 | 25 | 20 |
| Global EM | 5 | 5 | 25 | 15 | 25 | 10 | 15 | 10 |
| Mainland China | 15 | 20 | 40 | 30 | 40 | 35 | 50 | 15 |
| Taiwan | 20 | 25 | 60 | 45 | 70 | 65 | 100 | 130 |
| Korea | 5 | 5 | 10 | 15 | 30 | 35 | 125 | 140 |
| India | -5 | -10 | -15 | -20 | -25 | -20 | -15 | -10 |
| Brazil | -15 | -20 | -25 | -30 | -35 | -30 | -25 | -15 |
The chart displays cumulative equity flows for each region over time. The x-axis represents time (Jan-24 to May-26), and the y-axis represents cumulative equity flow in percentage. Key trends: Asia-Pacific regions (US, Japan, Korea) show strong growth, especially Korea peaking at ~140% in May-26; Europe (Western Europe) and North America (Mainland China) also show strong upward trends. The chart includes a secondary axis for absolute values (AUM) on the right axis.
</details>

Captures flows to country- and region-dedicated funds   
Source: EPFR, GS Global Investment Research

![](images/ed29a8b35bd8d0b2bff7e3b53a87fcac7e37432eb83d95275e22814c62dc5714.jpg)

<details>
<summary>bar</summary>

Cumulative Global Equity Flows by Sector YTD (% AUM)
| Sector | Cumulative Global Equity Flows (%) |
|---|---|
| Industrials | 24 |
| Infrastructure | 17 |
| Energy | 15 |
| Commodities/Materials | 11 |
| Technology | 3 |
| Utilities | 1 |
| Telecom | 1 |
| Real Estate | -1 |
| Health Care/Biotech | -2 |
| Financials | -3 |
| Consumer Goods | -6 |
</details>

Captures flows to sector dedicated funds

Source: EPFR, GS Global Investment Research   
![](images/6356d11bd1fa5189adc472c78823b277d253810d70578786630aaf1be585e2a0.jpg)

<details>
<summary>bar</summary>

Cumulative Global Equity Flows by Region YTD (% AUM)
| Region | Cumulative Global Equity Flows (%) |
|---|---|
| Korea | 37 |
| Brazil | 25 |
| Taiwan | 13 |
| Other DM | 5 |
| Global EM | 4 |
| US | 1 |
| DM Funds | 0.5 |
| Japan | 0.5 |
| Other EM | 0.5 |
| Other Western Europe | 0.5 |
| Western Europe | 0.5 |
| UK-Dedicated | -1 |
| EM Funds | -3 |
| India | -6 |
| Mainland China | -23 |
</details>

Captures flows to country- and region-dedicated funds   
Source: EPFR, GS Global Investment Research

![](images/55897706d13af33f33fdfab33900326ed771329b2f57f225079e00c7d9bfe0ee.jpg)

<details>
<summary>line</summary>

| Date   | Euro Area | Rest of World |
|--------|-----------|---------------|
| Jan-24 | -1.0      | 1.0           |
| May-24 | 1.0       | 1.5           |
| Sep-24 | 2.0       | 2.0           |
| Jan-25 | 9.0       | 3.0           |
| May-25 | -4.0      | 4.0           |
| Sep-25 | 3.0       | 6.0           |
| Jan-26 | -1.0      | 3.0           |
| May-26 | 5.0       | 3.0           |
</details>

Source: EPFR, GS Global Investment Research

![](images/8e0cad3248163cf4f0e12a680916e45351927840384063759cf17a362b0a62a9.jpg)

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
| May-26 | 1.8       | 0.5           |
</details>

Source: EPFR, GS Global Investment Research

Total Unhedged Foreign Flows By Country   
![](images/01c8af4279a447d79b3fd6b97e5b78a7e4c3b50bcb4fc82d88a715a644d066c6.jpg)

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

![](images/6d3ae64a5ca3ba745f7e321c64b9c33df32a56b66cadb75982fea4272bbb0484.jpg)

<details>
<summary>line</summary>

| Year | 4-week moving avg. ($bn) | 1-year moving avg. ($bn) |
|------|---------------------------|---------------------------|
| 2019 | -5                        | -1                        |
| 2020 | -18                       | -2                        |
| 2021 | 8                         | 3                         |
| 2022 | 5                         | 4                         |
| 2023 | -5                        | 1                         |
| 2024 | 6                         | 3                         |
| 2025 | 12                        | 7                         |
| 2026 | 9                         | 5                         |
</details>

![](images/9296f084f9edfeba4350135f9a90b2c4c7e3fdd5eeb73dbbb0be31be75959865.jpg)

<details>
<summary>line</summary>

| Year | 4-week moving avg. ($bn) | 1-year moving avg. ($bn) |
|------|---------------------------|---------------------------|
| 2019 | ~0                        | ~0                        |
| 2020 | ~-3.5                     | ~-0.5                     |
| 2021 | ~1.8                      | ~0.5                      |
| 2022 | ~1.2                      | ~1.0                      |
| 2023 | ~0                        | ~0                        |
| 2024 | ~1.0                      | ~0.5                      |
| 2025 | ~0                        | ~0                        |
| 2026 | ~3.5                      | ~1.0                      |
</details>

![](images/1a735332ae36f26d7ac4316205ef7237f0d4adefb6aa24f8adebda8e15a23164.jpg)

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

![](images/bbb2208683c21cd84ee53c031b7f9a6734bca4198e55dfc738238927da500259.jpg)

<details>
<summary>line</summary>

| Year | 4-week moving avg. ($bn) | 1-year moving avg. ($bn) |
|------|---------------------------|---------------------------|
| 2019 | -2.5                      | -0.5                      |
| 2020 | -1.8                      | -0.8                      |
| 2021 | 1.2                       | 0.5                       |
| 2022 | 1.5                       | 1.0                       |
| 2023 | -0.5                      | -0.2                      |
| 2024 | 0.8                       | 0.1                       |
| 2025 | 1.8                       | 0.6                       |
| 2026 | 3.8                       | 1.8                       |
</details>

![](images/8aa694fac49e8759717fbfb7ec8053a8ca2efe46a0cfe09eb32371a1bc214e22.jpg)

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
| 2025 | ~4.5                      | ~-0.5                     |
| 2026 | ~2.5                      | ~1.0                      |
</details>

Source: EPFR, GS Global Investment Research

Net Unhedged Flows into US Equity Funds   
![](images/dd1163b559422a0afb2ef220152910b8bf2e4a74d5f589ac12bc127e43590c39.jpg)

<details>
<summa

[中间内容因长度限制已省略]

attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

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
