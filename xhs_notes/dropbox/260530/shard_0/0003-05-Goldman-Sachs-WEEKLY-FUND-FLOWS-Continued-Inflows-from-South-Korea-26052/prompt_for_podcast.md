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
