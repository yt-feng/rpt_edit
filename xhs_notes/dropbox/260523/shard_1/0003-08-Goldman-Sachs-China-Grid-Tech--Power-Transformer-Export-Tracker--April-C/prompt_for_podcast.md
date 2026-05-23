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
# China Grid Tech: Power Transformer Export Tracker: April China transformer total exports at $27 \%$ yoy, while switchgear exports picked

In this latest Power Transformer Export Tracker, we provide an update as of April. US transformer PPI remained stable at an elevated level following a sharp increase in 2021-22, while China's export price in the 220-330MVA segment rose $23\%$ yoy on average in Feb-Apr (with April pricing down $14\%$ yoy). April total ( $>10$ MVA) transformer export value rose $27\%$ yoy, slowing vs $56\%$ yoy in March, while switchgear exports accelerated to $77\%$ yoy in April, from $5\%$ in March (indicating underlying demand strength combined with stronger PPI print for switchgear in the US at $14\%$ yoy). In particular, transformer exports to the US delivered $95\%$ yoy growth in April (vs $118\%$ yoy in March).

We continue to estimate that the US power transformer demand-local supply gap will narrow from 72% currently to 60% by 2028E, supported by the many capacity expansion plans announced by local transformer manufacturers. That said, we still expect the shortage to persist, leaving room for non-traditional suppliers, including those in China.

Key ideas: Sieyuan (Buy), Nari Tech (Buy), Huaming (Neutral): Among Chinese grid technology names, we favor Sieyuan and Nari Tech, while remain Neutral on Huaming. Our Buy on Sieyuan is driven by its transformer export opportunity amid persistent global supply tightness, as well as a wide product category to benefit from switchgear export, etc. We like Nari Tech for its exposure to domestic grid capex and rising export potential in converter valves and secondary equipment. On Huaming, steady transformer-component export growth potential is already well reflected in the share price.

Jacqueline Du

+852-2978-1783

jacqueline.du@gs.com

GS (Asia) L.L.C.

Exhibit 1: We continue to estimate that US power transformer demand/local supply gap would narrow from $72\%$ to $60\%$ in 2028E; while US PPI has stabilized at a high level, China export price is up $+23\%$ yoy (Feb-Apr avg, for 220-330MVA category)   
![](images/a2959bad888a84dd5cdd1d9a39e2cd234e8d7aee4f93d6b6510907fdded4976f.jpg)

<details>
<summary>bar</summary>

| Year | Demand, ytd change (%) | Supply, previous (%) |
|------|------------------------|----------------------|
| 2025 |                        | 72                   |
| 2023 |                        | 57                   |
</details>

![](images/b18e68c9fac5ef603c0b2d15bcd7f8ef141e9e9e75b2311c60f84cc7c48f4a58.jpg)

<details>
<summary>line</summary>

| Date    | US local pricing (benchmark to US PPI) | Export to US pricing (index Jan 2022 = 100, 3m rolling, 220-330MVA) |
|---------|------------------------------------------|------------------------------------------------------------------------|
| Feb-26  | ~200                                     | ~125                                                                   |
| Nov-25  | ~200                                     | ~175                                                                   |
| Aug-25  | ~200                                     | ~150                                                                   |
| May-25  | ~200                                     | ~100                                                                   |
| Feb-25  | ~200                                     | ~180                                                                   |
| Nov-24  | ~200                                     | ~190                                                                   |
| Aug-24  | ~200                                     | ~130                                                                   |
| May-24  | ~200                                     | ~150                                                                   |
| Feb-24  | ~200                                     | ~100                                                                   |
| Nov-23  | ~200                                     | ~120                                                                   |
| Aug-23  | ~200                                     | ~115                                                                   |
| May-23  | ~200                                     | ~115                                                                   |
| Feb-23  | ~200                                     | ~115                                                                   |
| Nov-22  | ~200                                     | ~115                                                                   |
| Aug-22  | ~195                                     | ~115                                                                   |
| May-22  | ~195                                     | ~115                                                                   |
| Feb-22  | ~165                                     | ~115                                                                   |
</details>

China Customs export pricing is on a FOB basis. US local pricing is estimated with a bidding document, then applied with the PPI for transformers of all power range, not 220-300MVA specifically.   
Source: Company data, Expert estimate, FRED, State Grid, China Customs, GS Global Investment Research

Exhibit 2: China total transformer export value grew $27\%$ in April (slowing vs $56\%$ in March)   
![](images/91da14f65b71ffced78ec7ba0a57f56c0ede598d07f199aca55a582bb4b5e65c.jpg)  
Source: China Customs, Data compiled by GS Global Investment Research

Exhibit 3: China transformer export value to the US grew +95% yoy in April (vs 118% yoy in March)   
![](images/0c58c718c41f9bd91c85c2b860eb22168d5bff3e6938c7de2dc80afc879d9a56.jpg)

<details>
<summary>area</summary>

Transformer export value to US (Rmb mn)
| Date | 10MVA-220MVA | 220MVA-330MVA | 330MVA-400MVA | 400MVA-500MVA | >500MVA |
|---|---|---|---|---|---|
| Jan-18 | 5.0 | 3.0 | 2.0 | 1.0 | 1.0 |
| Jul-18 | 15.0 | 12.0 | 8.0 | 7.0 | 3.0 |
| Jan-19 | 25.0 | 18.0 | 12.0 | 10.0 | 5.0 |
| Jul-19 | 45.0 | 35.0 | 25.0 | 20.0 | 15.0 |
| Jan-20 | 60.0 | 55.0 | 45.0 | 40.0 | 25.0 |
| Jul-20 | 55.0 | 50.0 | 45.0 | 40.0 | 25.0 |
| Jan-21 | 15.0 | 12.0 | 10.0 | 8.0 | 5.0 |
| Jul-21 | 5.0 | 3.0 | 2.0 | 1.0 | 1.0 |
| Jan-22 | 35.0 | 30.0 | 25.0 | 22.0 | 18.0 |
| Jul-22 | 45.0 | 40.0 | 35.0 | 32.0 | 28.0 |
| Jan-23 | 65.0 | 60.0 | 55.0 | 52.0 | 48.0 |
| Jul-23 | 75.0 | 70.0 | 65.0 | 62.0 | 58.0 |
| Jan-24 | 85.0 | 80.0 | 75.0 | 72.0 | 68.0 |
| Jul-24 | 115.0 | 110.0 | 105.0 | 102.0 | 98.0 |
| Jan-25 | 135.0 | 130.0 | 125.0 | 122.0 | 118.0 |
| Jul-25 | 145.0 | 140.0 | 135.0 | 132.0 | 128.0 |
| Jan-26 | 165.0 | 160.0 | 155.0 | 152.0 | 148.0 |
</details>

Source: China customs, Data compiled by GS Global Investment Research

Pricing remained stable in US: US transformer PPI has remained stable since Oct 2025 at a high level, after a sharp increase in 2021-22. Power transformers had an earlier price appreciation than other categories (due to renewable energy penetration prior to AIDC), while switchgear has caught up in pricing appreciation and turbine pricing also inched up in recent months, reaching $14\%$ yoy growth in April vs power transformers at $4\%$ yoy growth.

Among China exports to US pricing, it's hard to observe a trend in 10-220MVA category given the wide range. But 220-330MVA segment transformers saw a decline by $14\%$ in April alone, but the past 3-month rolling average price grew $+23\%$ yoy (Feb-Apr).

Key raw materials for transformer, GOES, saw price inching down; while copper price had a sharp increase in 4Q25, it saw a turnaround in March 2026.

Exhibit 4: Export transformer to the US market has seen a relatively volatile ASP in 10-220MVA due to volatile mix change...   
![](images/5f24f22c09b22ec7bb8185072fad0840474c4e696dba1f3e974d78a59df1ce40.jpg)

<details>
<summary>line</summary>

| Date    | Value (Rmb mn/unit) |
|---------|---------------------|
| Jan-18  | 7.5                 |
| Jul-18  | 5.0                 |
| Jan-19  | 4.5                 |
| Jul-19  | 2.0                 |
| Jan-20  | 8.0                 |
| Jul-20  | 10.0                |
| Jan-21  | 12.0                |
| Jul-21  | 0.0                 |
| Jan-22  | 6.0                 |
| Jul-22  | 8.0                 |
| Jan-23  | 11.0                |
| Jul-23  | 7.0                 |
| Jan-24  | 6.0                 |
| Jul-24  | 10.0                |
| Jan-25  | 5.0                 |
| Jul-25  | 3.0                 |
| Jan-26  | 5.0                 |
</details>

Source: China Customs, Data compiled by GS Global Investment Research

Exhibit 6: US in particular saw PPI for the power and specialty transformer price doubling in 2025 vs 2020 level, with recent pricing stable at a high level (3.8% yoy in April)   
![](images/ccb27c875f280ad1a08c4a4764ef67ff5d08cd18c799f48685c9755a8f9ed9fe.jpg)

<details>
<summary>line</summary>

US PPI for Electric Power and Specialty Transformer vs CPI (Jan 2018 indexed to 100)
| Date | US PPI for electrical equipment and specialty power transformer | US CPI |
|---|---|---|
| Jan-18 | 100 | 100 |
| Jun-18 | 105 | 102 |
| Nov-18 | 106 | 103 |
| Apr-19 | 107 | 104 |
| Sep-19 | 108 | 105 |
| Feb-20 | 109 | 106 |
| Jul-20 | 108 | 107 |
| Dec-20 | 110 | 108 |
| May-21 | 125 | 109 |
| Oct-21 | 145 | 112 |
| Mar-22 | 165 | 115 |
| Aug-22 | 175 | 118 |
| Jan-23 | 178 | 120 |
| Jun-23 | 179 | 122 |
| Nov-23 | 180 | 123 |
| Apr-24 | 182 | 124 |
| Sep-24 | 183 | 125 |
| Feb-25 | 184 | 126 |
| Jul-25 | 186 | 127 |
| Dec-25 | 190 | 130 |
</details>

Source: FRED, Data compiled by GS Global Investment Research

Exhibit 8: Key raw materials for transformer, GOES, saw prices inch down, while copper price had a sharp increase in 4Q25, and dipped in March 2026   
![](images/e47894687165411c2c140258d8cf16675c09c37b78e83a22b002c57c34b6998a.jpg)

<details>
<summary>line</summary>

| Date | Grain-oriented electrical steel (GOES) super high grade | Copper |
|---|---|---|
| Jan-18 | 100 | 100 |
| Jun-18 | 100 | 95 |
| Nov-18 | 100 | 90 |
| Apr-19 | 100 | 85 |
| Sep-19 | 100 | 80 |
| Feb-20 | 100 | 75 |
| Jul-20 | 100 | 70 |
| Dec-20 | 100 | 85 |
| May-21 | 135 | 135 |
| Oct-21 | 145 | 140 |
| Mar-22 | 165 | 135 |
| Aug-22 | 200 | 125 |
| Jan-23 | 225 | 130 |
| Jun-23 | 215 | 125 |
| Nov-23 | 195 | 120 |
| Apr-24 | 165 | 135 |
| Sep-24 | 175 | 140 |
| Feb-25 | 175 | 145 |
| Jul-25 | 175 | 150 |
| Dec-25 | 165 | 185 |
</details>

Source: TDEurope, Wind, Data compiled by GS Global Investment Research

Exhibit 5: ...but transformer in the 220-330MVA category saw pricing decline by 14% yoy in April, with Feb-April rolling average pricing still up 23% yoy   
![](images/87f30bdbf5a52c8e3df80ad45fa265d6750d4dbec281948fcb0cc7eadddc183c.jpg)

<details>
<summary>line</summary>

| Date    | Value (Rmb mn/unit) |
|---------|---------------------|
| Jan-18  | ~5                  |
| Jul-18  | ~7                  |
| Jan-19  | ~10                 |
| Jul-19  | ~8                  |
| Jan-20  | ~18                 |
| Jul-20  | ~5                  |
| Jan-21  | ~7                  |
| Jul-21  | ~7                  |
| Jan-22  | ~7                  |
| Jul-22  | ~10                 |
| Jan-23  | ~13                 |
| Jul-23  | ~15                 |
| Jan-24  | ~15                 |
| Jul-24  | ~18                 |
| Jan-25  | ~25                 |
| Jul-25  | ~13                 |
| Jan-26  | ~20                 |
</details>

Source: China Customs, Data compiled by GS Global Investment Research

Exhibit 7: US power and specialty transformers' PPI rose earlier than other product categories, while switchgear pricing has caught up in recent months (+14% yoy in April)   
![](images/ee2f19952bb84ff58d2818221dd248a64f0bcd9e87fe79dd29056c6ee17d91d4.jpg)

<details>
<summary>line</summary>

| Date    | US PPI for electrical equipment and specialty power transformer | US PPI for switchgear and switchboard apparatus manufacturing | US PPI for electrical equipment manufacturing | US PPI for turbine and turbine generator set units manufacturing |
|---------|---------------------------------------------------------------|---------------------------------------------------------------|-----------------------------------------------|-------------------------------------------------------------|
| Jan-18  | 100                                                           | 100                                                           | 100                                           | 100                                                         |
| Jun-18  | 105                                                           | 104                                                           | 103                                           | 102                                                         |
| Nov-18  | 110                                                           | 108                                                           | 106                                           | 104                                                         |
| Apr-19  | 115                                                           | 112                                                           | 109                                           | 106                                                         |
| Sep-19  | 120                                                           | 116                                                           | 112                                           | 108                                                         |
| Feb-20  | 125                                                           | 120                                                           | 115                                           | 110                                                         |
| Jul-20  | 130                                                           | 124                                                           | 118                                           | 112                                                         |
| Dec-20  | 135                                                           | 128                                                           | 121                                           | 114                                                         |
| May-21  | 140                                                           | 132                                                           | 124                                           | 116                                                         |
| Oct-21  | 150                                                           | 138                                                           | 128                                           | 120                                                         |
| Mar-22  | 160                                                           | 145                                                           | 135                                           | 125                                                         |
| Aug-22  | 170                                                           | 155                                                           | 145                                           | 130                                                         |
| Jan-23  | 175                                                           | 160                                                           | 150                                           | 135                                                         |
| Jun-23  | 180                                                           | 165                                                           | 155                                           | 140                                                         |
| Nov-23  | 185                                                           | 170                                                           | 160                                           | 145                                                         |
| Apr-24  | 190                                                           | 175                                                           | 165                                           | 150                                                         |
| Sep-24  | 195                                                           | 180                                                           | 170                                           | 155                                                         |
| Feb-25  | 200                                                           | 185                                                           | 175                                           | 160                                                         |
| Jul-25  | 205                                                           | 190                                                           | 180                                           | 165                                                         |
| Dec-25  | 210                                                           | 195                                                           | 185                                           | 170                                                         |
</details>

Source: FRED, Data compiled by GS Global Investment Research

China total (>10MVA) transformer export value grew 27% in April (slowing vs 56% in March), which was in particular driven by Africa at 681% yoy (23% contribution to total export), North America at 66% yoy (19% contribution), Asia at 38% yoy (30% contribution), Middle East at -26% yoy (12% contribution), Europe at 9% yoy (21% contribution), Latin America at -63% yoy (3% contribution).

In particular, transformer export value to US grew +95% yoy in April (vs 118% yoy in March). Export breakdown by voltage level was 44% from 10-220MVA segment, 29% from 220-330MVA segment, and 15% from 330-400MVA segment.

For other categories, electronic meter exports were flat in April (bringing ytd exports to 4% yoy). On the contrary, switchgear exports were particularly strong, accelerating to 77% yoy growth in April (vs. 5% in March), bringing ytd exports to 38% yoy growth.

Exhibit 9: China total transformer export value grew $27\%$ in April (slowing vs $56\%$ in March)   
![](images/ecd4b44526bcce6f42616082ea6958b32026055dc29440619eb47c6183c09915.jpg)

<details>
<summary>area</summary>

Transformer (>10MVA) export value (Rmb mn)
| Date | Americas (Rmb mn) | Europe (Rmb mn) | Asia (Rmb mn) 

[中间内容因长度限制已省略]

rm impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
