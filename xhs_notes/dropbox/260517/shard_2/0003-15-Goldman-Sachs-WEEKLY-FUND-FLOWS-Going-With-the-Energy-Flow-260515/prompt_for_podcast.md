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

# Going With the Energy Flow

# Global fund flows, week ending May 13

■ Flows into mutual funds and related investment products were positive across both equities and fixed income.   
Net flows into global equity funds remained positive in the week ending May 13 (+\$20bn vs +\$2bn in the previous week). DM equity funds led the net inflows, with US and Japan equity funds seeing strong demand. Within EM, global EM benchmark funds, Mainland China, and Korea equity funds saw net outflows; Mainland China funds have seen the largest net outflows in recent weeks. At the sector level, consumer goods funds saw the largest net outflows. Technology and infrastructure sector funds saw the largest net inflows across sectors. Energy funds saw outflows after strong inflows in the previous week (-\$0.5bn vs +\$4bn in the previous week) and flows have broadly tracked moves in the S&P GSCI (see chart of the week).   
- Flows into global fixed income funds were well supported from inflows into agg-type and government bond funds. Short-duration bond funds have also seen sustained inflows, while long-duration bond funds have lagged. Demand for inflation-protected bond funds has been strong, consistent with a backdrop of rising inflation risks. In EM, both hard-currency and local-currency bond funds saw net inflows. Money market fund assets rose by \$6bn.   
Cross-border FX flows were broadly positive, indicating supported risk sentiment. Foreign flows were positive across regions, with DM markets seeing particularly strong net inflows.

<table><tr><td rowspan="3"></td><td colspan="4">Global Fund Flows Summary</td></tr><tr><td colspan="2">Millions USD</td><td colspan="2">% AUM</td></tr><tr><td>4wk sum</td><td>13-May</td><td>4wk avg</td><td>13-May</td></tr><tr><td>Equity</td><td>71,958</td><td>20,458</td><td>0.06</td><td>0.07</td></tr><tr><td>Fixed Income</td><td>92,008</td><td>28,550</td><td>0.24</td><td>0.29</td></tr><tr><td>of which: EM</td><td>13,897</td><td>2,295</td><td>0.50</td><td>0.33</td></tr><tr><td>Money Markets</td><td>92,502</td><td>5,756</td><td>0.21</td><td>0.05</td></tr><tr><td>FX Flows*</td><td>70,136</td><td>25,746</td><td>0.11</td><td>0.16</td></tr></table>

\*Cross-border fund flows, excluding hard currency and FX-hedged funds   
Source: EPFR, Haver Analytics, GS Global Investment Research

# Lexi Kanter

+1(212)855-9701

alexandra.kanter@gs.com

GS & Co. LLC

Chart of the Week   
![](images/fbed439ba2000bef24967c033dc9e2535ef143db5e21c9236df8db790d4bed4f.jpg)

<details>
<summary>line</summary>

| Date   | Net flows into energy funds; 4-week moving average (left) | S&P GSCI (right) |
|--------|----------------------------------------------------------|------------------|
| Jan-25 | -0.5                                                     | 550              |
| Apr-25 | -1.0                                                     | 500              |
| Jul-25 | 0.2                                                      | 550              |
| Oct-25 | 0.3                                                      | 500              |
| Jan-26 | 1.0                                                      | 550              |
| Apr-26 | 2.5                                                      | 750              |
| Jul-26 | 0.7                                                      | 750              |
</details>

Source: EPFR, Haver Analytics, GS Global Investment Research

# Global Fund Flow Trends

![](images/0d37198a79bc070f985ba42c62d964b099584e93367545280af7e71bc5fde0b0.jpg)

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
| May-26 | ~600       | ~120              |
</details>

Source: EPFR, GS Global Investment Research

![](images/b7e5f7ea69a01c26743490597321b17f0d0925f8e31c9b6866a3d72e894a84dd.jpg)

<details>
<summary>line</summary>

| Date    | Flows into Mainland China Equity Funds from Mainland China ($bn) | Flows into Mainland China Equity Funds from Rest of World ($bn) |
|---------|---------------------------------------------------------------|------------------------------------------------------------------|
| Jan-23  | ~0                                                            | ~0                                                               |
| Aug-23  | ~0                                                            | ~0                                                               |
| Mar-24  | ~10                                                           | ~0                                                               |
| Oct-24  | ~30                                                           | ~5                                                               |
| May-25  | ~25                                                           | ~0                                                               |
| Dec-25  | ~10                                                           | ~0                                                               |
| Jul-26  | ~-20                                                          | ~0                                                               |
</details>

Source: EPFR, GS Global Investment Research

![](images/c10b6a1b53fece9a0c7ebb194acf8479ff9f30cf4f1e8c973ea9d6d9c412c36f.jpg)

<details>
<summary>line</summary>

| Date   | Technology | Defensives | Cyclicals ex. Tech |
|--------|------------|------------|---------------------|
| Jan-25 | -2         | -1         | 0                   |
| Apr-25 | 5          | -3         | -6                  |
| Jul-25 | 0          | 0          | 4                   |
| Oct-25 | 8          | 2          | 6                   |
| Jan-26 | 4          | 3          | 16                  |
| Apr-26 | 0          | -1         | 3                   |
</details>

Source: EPFR, GS Global Investment Research

![](images/2da4ea67ed97d8f55a7725f5356ebf192407ee82199fa3ce2a69647b29b7f747.jpg)

<details>
<summary>line</summary>

| Sector                  | Cumulative % AUM |
| ----------------------- | ---------------- |
| Commodities/Materials   | 30               |
| Consumer Goods          | 25               |
| Energy                  | -15              |
| Financials              | -10              |
| Health Care/Biotech     | -5               |
| Industrials             | 10               |
| Infrastructure          | 20               |
| Real Estate             | 15               |
| Technology              | 25               |
| Telecom                 | 30               |
| Utilities               | 20               |
</details>

Captures flows to sector dedicated funds

Source: EPFR, GS Global Investment Research   
![](images/20aaec66daee4d86a73b6aa88adf85bd2ffc0fc63bd72958d741d93a2bdafdd6.jpg)

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

![](images/00c9b0adfcb83fce270b21f0ee021c35b139d3b5870fd40862762e1c7c84597f.jpg)

<details>
<summary>bar</summary>

Cumulative Global Equity Flows by Sector YTD (% AUM)
| Sector | Cumulative Global Equity Flows (%) |
|---|---|
| Industrials | 21.0 |
| Energy | 16.5 |
| Infrastructure | 14.5 |
| Commodities/Materials | 12.0 |
| Technology | 2.0 |
| Telecom | 1.5 |
| Utilities | 0.5 |
| Real Estate | -0.5 |
| Health Care/Biotech | -0.5 |
| Financials | -0.5 |
| Consumer Goods | -5.0 |
</details>

Captures flows to sector dedicated funds

Source: EPFR, GS Global Investment Research   
![](images/77f77d2b81a7db68fc15086eb35efdeb030af5e612341893e91ddcd8f39667bc.jpg)

<details>
<summary>bar</summary>

Cumulative Global Equity Flows by Region YTD (% AUM)
| Region | Cumulative Global Equity Flows (%) |
|---|---|
| Korea | 35.0 |
| Brazil | 31.0 |
| Taiwan | 10.0 |
| Other DM | 5.0 |
| Global EM | 4.5 |
| Japan | 2.5 |
| Other EM | 1.0 |
| DM Funds | 1.0 |
| US | 1.0 |
| Other Western Europe | 0.5 |
| Western Europe | 0.5 |
| UK-Dedicated | -1.5 |
| EM Funds | -2.0 |
| India | -5.0 |
| Mainland China | -20.0 |
</details>

Captures flows to country- and region-dedicated funds   
Source: EPFR, GS Global Investment Research

![](images/2688c1769aa6010d0f807279e03e81d2b89ee65cacb492874db9ec1e83172219.jpg)

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
| May-26 | 5         | 3             |
</details>

Source: EPFR, GS Global Investment Research

![](images/3f8d55c74895ba81c3c4f6f9479063cdaed8a630e495d52112a043d8cea6f0a6.jpg)

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
![](images/d3280d6fb4b595709b91db96b9c2cf8c1b64a46359fb5854fb12eb12c1424e8e.jpg)

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
| 2026 | ~2.6                      | ~0.6                      |
</details>

![](images/c9dbb2041027fa69205900b2d9258e48ec3445ee8ac551f0fe5af656c46f97f3.jpg)

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

![](images/e00b8dc51a266061762a242c3558968fc8e59f488f218b74a4e7689ae5e0d230.jpg)

<details>
<summary>line</summary>

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

![](images/b6a2c1c15847d8845e6a03091e1d7cb35b5ad71aa22cf18840609b84d2891e0e.jpg)

<details>
<summary>line</summary>

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

![](images/5000f8dd92e96d56971e4b5bc5d0de861622e103375d7ff748bafdb9e166a306.jpg)

<details>
<summary>line</summary>

| Year | 4-week moving avg. ($bn) | 1-year moving avg. ($bn) |
|------|---------------------------|---------------------------|
| 2019 | -2.5                      | -0.5                      |
| 2020 | -3.0                      | -0.8                      |
| 2021 | 1.5                       | 0.5                       |
| 2022 | 1.0                       | 1.0                       |
| 2023 | -1.0                      | -0.5                      |
| 2024 | 0.5                       | 0.0                       |
| 2025 | 1.5                       | 0.5                       |
| 2026 | 3.5                       | 1.5                       |
</details>

![](images/f11ffcd961ed177293e3e349bc9cd1f363ab0ca57e5f09b45965d29aba680b54.jpg)

<details>
<summary>line</summary>

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

Exhibit 1:   
Net Unhedged Flows into US Equity Funds   
![](images/e8d8616b58d65740b5df864640e0a230d2955ad1ce4e1af55ca0b8b5bc0ecf9a.jpg)

<details>
<summary>line</summary>

| Date    | Weekly | 4-week moving avg. |
|---------|--------|---------------------|
| Jan-24  | ~0     | ~0                  |
| May-24  | ~2     | ~1                  |
| Sep-24  | ~3     | ~2                  |
| Jan-25  | ~14    | ~8                  |
| May-25  | ~-13   | ~-5                 |
| Sep-25  | ~3     | ~1                  |
| Jan-26  | ~4     | ~2                  |
| May-26  | ~6     | ~4                  |
</details>

![](images/d68ac36f7efec88d14f37382d4e9146e506bcffc31ce8ca29eeca874433c8693.jpg)

<details>
<summary>line</summary>

| Date   | Weekly | 4-week moving avg. |
|--------|--------|---------------------|
| Jan-24 | ~0.0   | ~0.0                |
| May-24 | ~0.5   | ~0.0                |
| Sep-24 | ~0.0   | ~0.0                |
| Jan-25 | ~1.0   | ~0.5                |
| May-25 | ~0.0   | ~0.0                |
| Sep-25 | ~0.5   | ~0.0                |
| Jan-26 | ~-2.5  | ~-1.5               |
| May-26 | ~1.5   | ~1.0                |
</details>

![](images/f22396cefa26215e416cdbbea2235fb523837ab479b1351acb064fe97f49118e.jpg)

<details>
<summary>line</summary>

| Date    | Weekly | 4-week moving avg. |
|---------|--------|---------------------|
| Jan-24  | 0.0    | 0.0                 |
| May-24  | -1.0   | -0.5                |
| Sep-24  | -3.0   | -1.5                |
| Jan-25  | 1.5    | 0.5                 |
| May-25  | 4.5    | 1.0                 |
| Sep-25  | -6.0   | -4.0                |
| Jan-26  | -1.0   | -2.0                |
| May-26  | 2.5    | 1.0                 |
</details>

![](images/245d392868eb490fe745b4bb2d5342765832f396bbe6b050dd89625a3c9cecf5.jpg)

<details>
<summary>line</summary>

| Date    | Weekly | 4-week moving avg. |
|---------|--------|---------------------|
| Jan-24  | ~0     | ~0                  |
| May-24  | ~0     | ~0                  |
| Sep-24  | ~-8    | ~-4                 |
| Jan-25  | ~2     | ~1                  |
| May-25  | ~2     | ~1                  |
| Sep-25  | ~0     | ~0                  |
| Jan-26  | ~-6    | ~-2                 |
| May-26  | ~0     | ~0                  |
</details>

![](images/822f2cb1e05341ed34e16d4afcfc1e610c3f46a9dce6e683efee4b6dadad225c.jpg)

<details>
<summary>line</summary>

| Date   | Weekly | 4-week moving avg. |
|--------|--------|---------------------|
| Jan-24 | 0.0    | 0.0                 |
| May-24 | 0.2    | 0.1                 |
| Sep-24 | 0.3    | 0.1                 |
| Jan-25 | 0.4    | 0.2                 |
| May-25 | -0.4   | -0.2                |
| Sep-25 | -0.2   | -0.3                |
| Jan-26 | -1.2   | -0.8                |
| May-26 | -1.6   | -1.4                |
</details>

![](images/a1f7ca9416239c598e62fcbd1f729f62b9645377cc527ce6cdecccf65d077977.jpg)

<details>
<summary>line</summary>

| Date    | Weekly | 4-week moving avg. |
|---------|--------|---------------------|
| Jan-24  | ~0     | ~0                  |
| May-24  | ~0     | ~0           

[中间内容因长度限制已省略]

e have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to sUBStantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
