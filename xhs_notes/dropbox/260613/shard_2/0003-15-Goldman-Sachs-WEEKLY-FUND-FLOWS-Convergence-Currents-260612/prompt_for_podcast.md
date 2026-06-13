你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

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
|---------|--------|---------------------|
| Jan-24  | 0.0    | 0.0                 |
| Jun-24  | 0.5    | 0.3                 |
| Nov-24  | 1.0    | 0.8                 |
| Apr-25  | 0.5    | 0.3                 |
| Sep-25  | 0.8    | 0.6                 |
| Feb-26  | -2.5   | -2.0                |
| Jul-26  | 1.8    | 1.5                 |
</details>

![](images/366e2b67096e4dc233f2d90a3ecf0bb3bf59b09c2f192e6f58ca78fb751970ef.jpg)

<details>
<summary>line chart</summary>

| Date    | Weekly Net Inflows ($bn) | 4-week moving avg. ($bn) |
|---------|--------------------------|---------------------------|
| Jan-24  | ~0                       | ~0                        |
| Jun-24  | ~0                       | ~0                        |
| Nov-24  | ~0                       | ~0                        |
| Apr-25  | ~5                       | ~1                        |
| Sep-25  | ~-6                      | ~-4                       |
| Feb-26  | ~-5                      | ~-3                       |
| Jul-26  | ~0                       | ~0                        |
</details>

![](images/9b6f18fe98a3890c37a662478a9f16be177ed653d8d51152cd6040326e7a071a.jpg)

<details>
<summary>line chart</summary>

| Date    | Weekly | 4-week moving avg. |
|---------|--------|---------------------|
| Jan-24  | ~0.5   | ~0.0                |
| Jun-24  | ~0.0   | ~0.0                |
| Nov-24  | ~-8.0  | ~-3.0               |
| Apr-25  | ~2.5   | ~1.5                |
| Sep-25  | ~0.0   | ~0.0                |
| Feb-26  | ~-6.0  | ~-3.0               |
| Jul-26  | ~1.0   | ~0.0                |
</details>

![](images/f5ec66a6ad19df6eb16a21079aa73f6673c2f707c32aecc2eb8ac36f69f7cae0.jpg)

<details>
<summary>line chart</summary>

| Date   | Weekly | 4-week moving avg. |
|--------|--------|---------------------|
| Jan-24 | 0.0    | 0.0                 |
| Jun-24 | 0.2    | 0.1                 |
| Nov-24 | 0.3    | 0.2                 |
| Apr-25 | -0.4   | -0.3                |
| Sep-25 | -0.2   | -0.1                |
| Feb-26 | -1.2   | -0.8                |
| Jul-26 | 0.5    | 0.4                 |
</details>

![](images/580a48093467ada397522598fdcec5301467d5c289596bd2e1acf7521a6466d2.jpg)

<details>
<summary>line chart</summary>

| Date    | Weekly | 4-week moving avg. |
|---------|--------|---------------------|
| Jan-24  | ~0     | ~0                  |
| Jun-24  | ~0     | ~0                  |
| Nov-24  | ~0     | ~0                  |
| Apr-25  | ~0     | ~0                  |
| Sep-25  | ~14    | ~5                  |
| Feb-26  | ~0     | ~0                  |
| Jul-26  | ~0     | ~0                  |
</details>

Source: EPFR, Haver Analytics, GS Global Investment Research

Fixed Income & Equity Flows

<t

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
