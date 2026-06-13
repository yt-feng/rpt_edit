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

# Convergence Currents

## Global fund flows, week ending June 10

■ Flows into mutual funds and related investment products were positive across both equities and fixed income.  
- Net flows into global equity funds were positive again in the week ending June 10 (+\$31bn vs +\$23bn in the previous week). US funds continued to see demand while Europe dedicated funds saw net outflows. Within EM, Taiwan and Korea equity funds drove the net inflows while global EM benchmark funds and Mainland China equity funds saw net outflows. At the sector level, technology funds saw the largest net inflows while consumer goods funds saw continued net outflows.  
- Flows into global fixed income funds remained well-supported from inflows across fund types. Short-duration bond funds and inflation-protected bond funds have seen sustained inflows. In EM, hard-currency bond funds saw net outflows. Money market fund assets declined by -\$2bn.  
Cross-border FX flows were broadly positive. USD and KRW saw the strongest net demand while INR, BRL, and CNY saw the largest net outflows. Hungary bond inflows have also increased meaningfully since the start of the year (see Chart of the Week), consistent with our view that the upcoming shift in Hungary's economic policy, including the prospects of Euro adoption, argues for gradual yield convergence to the Euro Area and asymmetric risks toward further HUF appreciation.

<table><tr><td rowspan="3"></td><td colspan="4">Global Fund Flows Summary</td></tr><tr><td colspan="2">Millions USD</td><td colspan="2">% AUM</td></tr><tr><td>4wk sum</td><td>10-Jun</td><td>4wk avg</td><td>10-Jun</td></tr><tr><td>Equity</td><td>49,949</td><td>31,494</td><td>0.04</td><td>0.10</td></tr><tr><td>Fixed Income</td><td>114,275</td><td>17,696</td><td>0.29</td><td>0.18</td></tr><tr><td>of which: EM</td><td>11,020</td><td>-533</td><td>0.39</td><td>-0.08</td></tr><tr><td>Money Markets</td><td>142,810</td><td>-2,475</td><td>0.32</td><td>-0.02</td></tr><tr><td>FX Flows*</td><td>58,032</td><td>13,416</td><td>0.09</td><td>0.08</td></tr></table>

\*Cross-border fund flows, excluding hard currency and FX-hedged funds  
Source: EPFR, Haver Analytics, GS Global Investment Research

## Lexi Kanter

+1(212)855-9701

alexandra.kanter@gs.com

GS & Co. LLC

Chart of the Week  
![](images/e2df585fc0ac53df8e69a85d7e4b1a5a54fd451b9da3b9b5af2f2f8e7ccd3fc7.jpg)

<details>
<summary>line chart</summary>

| Date    | Value ($mn) |
|---------|-------------|
| Jan-24  | ~0          |
| May-24  | ~8          |
| Sep-24  | ~0          |
| Jan-25  | ~3          |
| May-25  | ~7          |
| Sep-25  | ~0          |
| Jan-26  | ~-5         |
| May-26  | ~21         |
</details>

Source: EPFR, Haver Analytics, GS Global Investment Research

## Global Fund Flow Trends

![](images/baa50c38f16fdf99e662b4a5c88468890693edae716b677219cb07f3ea21edf2.jpg)

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

![](images/351cb9f46d82ce8ba240c651530c3ebf692843a140c017cd4b0fe1f94e9fc08c.jpg)

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
| Jul-26 | ~-25                                                          | ~0                                                               |
</details>

Source: EPFR, GS Global Investment Research

![](images/0738b7c5bb332e4a5f0c169a2efdf33fd1ebe1cb13519a6cf5a1031b79792dad.jpg)

<details>
<summary>line chart</summary>

| Date   | Technology | Defensives | Cyclicals ex. Tech |
|--------|------------|------------|---------------------|
| Jan-25 | -          | -          | -                   |
| Apr-25 | 4.5        | -          | -5.0                |
| Jul-25 | -          | 0.5        | 3.0                 |
| Oct-25 | 7.0        | 1.0        | 6.0                 |
| Jan-26 | 4.0        | 3.0        | 16.0                |
| Apr-26 | 0.0        | -          | 0.0                 |
| Jul-26 | 8.0        | 0.0        | -2.0                |
</details>

Source: EPFR, GS Global Investment Research

![](images/528be6dfe15fefd6207dfbc13d59a7229be86c194362f6d6136622feb0f0e6d0.jpg)

<details>
<summary>line chart</summary>

| Sector                  | Jan-24 | May-24 | Sep-24 | Jan-25 | May-25 | Sep-25 | Jan-26 | May-26 |
| ----------------------- | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| Commodities/Materials   | 0      | 0      | 0      | 0      | 0      | 0      | 30     | 30     |
| Consumer Goods          | 0      | 0      | 0      | 0      | 0      | 0      | 25     | 25     |
| Energy                  | 0      | 0      | -10    | -10    | -10    | -10    | -15    | -15    |
| Financials              | 0      | 0      | 0      | 0      | 0      | 0      | 15     | 15     |
| Health Care/Biotech     | 0      | 0      | 0      | 0      | 0      | 0      | 15     | 15     |
| Industrials             | 0      | 0      | 0      | 0      | 0      | 0      | 20     | 20     |
| Infrastructure          | 0      | 0      | 0      | 0      | 0      | 0      | 25     | 25     |
| Real Estate             | 0      | 0      | 0      | 0      | 0      | 0      | 25     | 25     |
| Technology              | 0      | 0      | 0      | 0      | 0      | 0      | 25     | 25     |
| Telecom                 | 0      | 0      | 0      | 0      | 0      | 0      | 25     | 25     |
| Utilities               | 0      | 0      | 0      | 0      | 0      | 0      | 25     | 25     |
</details>

Captures flows to sector-dedicated funds

Source: EPFR, GS Global Investment Research  
![](images/182b6a407e2d768d18ab3afc1a1f8b3c72c15c7e1655f9f9c166579fd3be4e3e.jpg)

<details>
<summary>line chart</summary>

| Region           | Cumulative % AUM |
| ---------------- | ---------------- |
| US               | 0                |
| Western Europe   | 0                |
| UK-Dedicated     | 0                |
| Japan            | 0                |
| Global EM        | 0                |
| Mainland China   | 0                |
| Taiwan           | 0                |
| Korea            | 0                |
| India            | 0                |
| Brazil           | 0                |
</details>

Captures flows to country- and region-dedicated funds  
Source: EPFR, GS Global Investment Research

![](images/7a82a56eec697175fdea317eff70d212acdfdc167c44302ca4eda50c9262ce9c.jpg)

<details>
<summary>bar chart</summary>

Cumulative Global Equity Flows by Sector YTD (% AUM)
| Sector | Cumulative Global Equity Flows (%) |
|---|---|
| Industrials | 24.5 |
| Infrastructure | 17.8 |
| Energy | 15.0 |
| Commodities/Materials | 10.8 |
| Technology | 4.0 |
| Telecom | 2.0 |
| Utilities | 0.8 |
| Real Estate | -0.5 |
| Health Care/Biotech | -1.0 |
| Financials | -2.0 |
| Consumer Goods | -6.0 |
</details>

Captures flows to sector dedicated funds

Source: EPFR, GS Global Investment Research  
![](images/f0abb0c1a9e9af3645006188005f103e8d02b75414a2cdf9db57f6f2e366bed8.jpg)

<details>
<summary>bar chart</summary>

Cumulative Global Equity Flows by Region YTD (% AUM)
| Region | Cumulative Global Equity Flows (%) |
|---|---|
| Korea | 44 |
| Brazil | 25 |
| Taiwan | 17 |
| Other DM | 6 |
| Global EM | 5 |
| US | 2 |
| DM Funds | 1 |
| Japan | 1 |
| Other EM | 0 |
| Other Western Europe | 0 |
| Western Europe | -1 |
| UK-Dedicated | -3 |
| EM Funds | -4 |
| India | -8 |
| Mainland China | -24 |
</details>

Captures flows to country- and region-dedicated funds  
Source: EPFR, GS Global Investment Research

![](images/99700a7a6f87b8341450e46ae1b4dd64c0d00ad8d1bdf7fe7fbfe604a2cfb515.jpg)

<details>
<summary>line chart</summary>

| Date   | Euro Area ($bn) | Rest of World ($bn) |
|--------|-----------------|----------------------|
| Jan-24 | -1              | 1                    |
| May-24 | 2               | 1                    |
| Sep-24 | 3               | 2                    |
| Jan-25 | 9               | 3                    |
| May-25 | -4              | 4                    |
| Sep-25 | 3               | 6                    |
| Jan-26 | -1              | 3                    |
| May-26 | 5               | 3                    |
</details>

Source: EPFR, GS Global Investment Research

![](images/8c3cb53b466ff0c21d1e40206a682e45fd5ae076eeaf980c0b926cfadb8e45f5.jpg)

<details>
<summary>line chart</summary>

| Date   | Euro Area | Rest of World |
|--------|-----------|---------------|
| Jan-24 | 0.5       | 1.0           |
| May-24 | 2.8       | 1.2           |
| Sep-24 | 2.7       | 1.5           |
| Jan-25 | 0.0       | 0.5           |
| May-25 | -2.8      | -0.5          |
| Sep-25 | 3.2       | 0.8           |
| Jan-26 | 0.8       | 0.3           |
| May-26 | 2.0       | 0.5           |
</details>

Source: EPFR, GS Global Investment Research

Total Unhedged Foreign Flows By Country  
![](images/ff5f154d690904d7fa99f6ef9b3c9468650a995ce0a764d10ff1b15913b0b837.jpg)

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
| 2026 | ~2.5                      | ~0.6                      |
</details>

![](images/7b3e9d1e038be08a3627678d5e13ff623a35ac14a6d4b1d4eb3d9af733859662.jpg)

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
| 2026 | 9                         | 4                         |
</details>

![](images/0491c9b92e7bafb4872b547afc44d3aae66330d3adf4d2ce470ccfdb7d8159b9.jpg)

<details>
<summary>line chart</summary>

| Year | 4-week moving avg. ($bn) | 1-year moving avg. ($bn) |
|------|---------------------------|---------------------------|
| 2019 | ~0                        | ~0                        |
| 2020 | ~-3.5                     | ~-0.5                     |
| 2021 | ~1.8                      | ~0.8                      |
| 2022 | ~1.2                      | ~1.0                      |
| 2023 | ~0                        | ~0.2                      |
| 2024 | ~1.0                      | ~0.3                      |
| 2025 | ~0                        | ~0.1                      |
| 2026 | ~3.5                      | ~1.0                      |
</details>

![](images/b76188a032ffe31691223280b6530866d4a08df6b2771eb45123f50b9aa8b5f9.jpg)

<details>
<summary>line chart</summary>

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

![](images/e9f024e59f36af8a32cca6254fc20dfc3fd1f78b83cc589d9435c7ccaf0b33ac.jpg)

<details>
<summary>line chart</summary>

| Year | 4-week moving avg. ($bn) | 1-year moving avg. ($bn) |
|------|---------------------------|---------------------------|
| 2019 | -2.5                      | -0.5                      |
| 2020 | -1.8                      | -0.8                      |
| 2021 | 1.2                       | 0.5                       |
| 2022 | 1.5                       | 1.0                       |
| 2023 | -0.5                      | -0.2                      |
| 2024 | 0.8                       | 0.3                       |
| 2025 | 1.8                       | 0.7                       |
| 2026 | 3.8                       | 1.8                       |
</details>

![](images/4f6d73e1353e4e8aa891ce0324f0a45f3a5f714d1bf3f60afdb3644859e21ca0.jpg)

<details>
<summary>line chart</summary>

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
![](images/17ab58ef985d6c5bbdabbb86459cef90232b522d8d50d7f0e08094d9859a7a04.jpg)

<details>
<summary>line chart</summary>

| Date    | Weekly | 4-week moving avg. |
|---------|--------|---------------------|
| Jan-24  | ~0     | ~0                  |
| Jun-24  | ~2     | ~1                  |
| Nov-24  | ~15    | ~8                  |
| Apr-25  | ~-15   | ~-5                 |
| Sep-25  | ~0     | ~0                  |
| Feb-26  | ~5     | ~3                  |
| Jul-26  | ~5     | ~4                  |
</details>

![](images/4bdbe0c1ab93518dc9de0a75ccf33aeb6a8b789332314ffb7b3578e5adab5e75.jpg)

<details>
<summary>line chart</summary>

| Date    | Weekly | 4-week moving avg. |
|---------|---

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
