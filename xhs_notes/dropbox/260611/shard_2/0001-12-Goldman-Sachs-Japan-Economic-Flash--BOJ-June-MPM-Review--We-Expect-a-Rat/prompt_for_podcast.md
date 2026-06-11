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
# Japan Economic Flash: BOJ June MPM Review: We Expect a Rate Hike in June, Followed by Roughly Semi-annual Hikes

The Japanese economy has remained robust without significant deterioration even amid heightened Middle East tensions. On the price front, business-to-business (B2B) prices are accelerating, and we expect upward pressure on consumer prices to increase going forward.  
Following the more hawkish tone of Governor Ueda's speech (June 3), we changed our expectation from a July rate hike to a June rate hike. We also expect the forward guidance on monetary policy to be slightly modified in conjunction with the June rate hike to maintain a hawkish stance while hinting that it is approaching the neutral rate.  
■ After the June hike, we expect the next rate hike in January 2027. We also maintain our view that the terminal rate will be $1.5\%$ , equal to the neutral rate, and that the policy rate will reach $1.5\%$ in July 2027. However, the timing of rate hikes is likely to be significantly influenced by market developments and the degree of progress in communication with the government.  
Meanwhile, regarding the reduction in JGB purchases to be discussed at the June meeting, we think it likely that the BOJ will maintain its current JGB purchase plan until March 2027 and keep purchases at c.¥2 tn from April 2027 onward.

Akira Otani

+81(3)4587-9960 | akira.otani@gs.com

GS Japan Co., Ltd.

## BOJ June MPM Review: June Rate Hike, Followed by Roughly Semi-annual Hikes

The Japanese economy has remained robust without significant deterioration even amid heightened Middle East tensions. On the price front, B2B prices are accelerating, and we expect upward pressure on consumer prices to increase going forward.

Indicators released since the April Monetary Policy Meeting (MPM) show that while soft data such as consumer confidence has deteriorated, hard data remains solid, and the Japanese economy has maintained its robustness without significant deterioration despite rising crude oil prices and heightened Middle East tensions (Exhibit 1, Exhibit 2).

Exhibit 1: Confidence is Deteriorating...  
Consumer Confidence and Economy Watchers Survey DI (Household Activity-Related)  
![](images/6d3a704514f6dfcb4d6f9a8d2ebae697a3efa65274aa173d6c8cdc84c8ceb405.jpg)

<details>
<summary>line chart</summary>

| Year | Consumer Confidence Index (lhs) | Economy Watchers Survey (household DI; rhs) |
|------|----------------------------------|-----------------------------------------------|
| 2019 | 42                               | 36                                            |
| 2020 | 38                               | 22                                            |
| 2021 | 34                               | 38                                            |
| 2022 | 39                               | 41                                            |
| 2023 | 30                               | 39                                            |
| 2024 | 38                               | 37                                            |
| 2025 | 35                               | 36                                            |
| 2026 | 33                               | 35                                            |
</details>

Source: Cabinet Office

Exhibit 2: ...But Hard Data Remains Solid  
Machinery Orders (Private Sector Excluding Volatile Orders) and BOJ Consumption Activity Index  
![](images/af5c66f98d84f2e0507be1b0c96a0cf8c7664d1f6bbdaf19ccff85decd06571e.jpg)

<details>
<summary>line chart</summary>

| Year | Core machinery orders (lhs) (Y bn) | BOJ Consumption Activity Index (rhs) (Y bn) |
|---|---|---|
| 2019 | 830 | 1050 |
| 2020 | 750 | 90 |
| 2021 | 850 | 100 |
| 2022 | 900 | 105 |
| 2023 | 880 | 104 |
| 2024 | 860 | 103 |
| 2025 | 920 | 105 |
| 2026 | 1120 | 108 |
</details>

Source: Cabinet Office, BoJ

On the price front, the April price revision period lacked broad-based price hikes, particularly for food items. Under these circumstances, even on a basis excluding the effects of government measures published by the BOJ, while core CPI growth has increased somewhat, growth in other indicators has slowed. However, corporate prices are rising significantly, mainly for petroleum products, and we expect this to spill over to downstream B-to-C transactions with a lag, gradually increasing inflationary pressure (Exhibit 3, Exhibit 4).

Exhibit 3: Even on a Basis Excluding the Effects of Government Measures, Growth in Many Price Indicators Has Slowed Recently, but...  
![](images/65ea2597006046550b50246656c18e47a2e26d2bc0c53c4a2f6ced9732b4a9a5.jpg)

<details>
<summary>line chart</summary>

| Year | Global core CPI (excl. food and energy) | Core CPI (Excl. freshfood) | New core CPI (excl. freshfood and energy) |
|------|------------------------------------------|----------------------------|-------------------------------------------|
| 2020 | 0.5                                      | 0.3                        | 0.6                                       |
| 2021 | 0.2                                      | -0.5                       | 0.1                                       |
| 2022 | 0.8                                      | 1.5                        | 1.2                                       |
| 2023 | 2.5                                      | 4.5                        | 4.2                                       |
| 2024 | 1.8                                      | 2.0                        | 2.5                                       |
| 2025 | 1.7                                      | 2.8                        | 3.5                                       |
| 2026 | 1.5                                      | 2.5                        | 2.8                                       |
</details>

![](images/481bcee41cf65c233ed310895526d80f0e9e584f4695645666dcca6b083e046b.jpg)

<details>
<summary>line chart</summary>

| Year | 10% trimmed mean | Weighted median | Mode |
|------|-------------------|-----------------|------|
| 2020 | 0.3               | 0.1             | 0.2  |
| 2021 | -0.5              | 0.1             | 0.1  |
| 2022 | 1.0               | 0.3             | 0.5  |
| 2023 | 3.0               | 1.5             | 2.5  |
| 2024 | 2.5               | 1.8             | 2.0  |
| 2025 | 2.0               | 1.5             | 1.8  |
| 2026 | 1.5               | 1.0             | 1.5  |
</details>

Source: BoJ

Exhibit 4: ...The Surge in B2B Prices is Expected to Increase Upward Pressure on Consumer Prices Going Forward  
![](images/0dfd8f9430723eaab4ab367cf51c8b4a3045c789765a7e90f047b81e9507d3b5.jpg)

<details>
<summary>line chart</summary>

| Year | Domestic CGPI (lhs) (%) | Import price (rhs) ($) |
|---|---|---|
| 2020 | 0 | 0 |
| 2021 | -3 | -4 |
| 2022 | 9 | 8 |
| 2023 | 10.5 | 9 |
| 2024 | 0.5 | -10 |
| 2025 | 4 | 0 |
| 2026 | 2.5 | 5 |
</details>

Source: BoJ

Following the more hawkish tone of Governor Ueda's speech (June 3), we changed our expectation from a July rate hike to a June rate hike.

We take into consideration not only economic and price conditions but also the political factor of laying the groundwork for a rate hike between the government and the BOJ as important for the timing of rate hikes. Since we had seen no signs of progress in laying such groundwork, we had previously expected a July rate hike to be more likely.

However, we revisited our assumption in the wake of the meeting between BOJ Governor Ueda and Prime Minister Takaichi on May 22, and Governor Ueda's speech on June 3. While that speech provided no clear hints about the timing of the next rate hike, we take the view that if the BOJ were not planning to raise the policy rate in June, Governor Ueda would have sent a message to temper market expectations for a June hike that had been priced in by the market, in order to minimize the market reaction. The speech appeared, if anything, more hawkish in tone. We believe this suggests that during his meeting with Prime Minister Takaichi two weeks ago, Governor Ueda laid the groundwork for the next rate hike—meaning he may have gained the sense that even if the government did not support the next rate hike, it would at least not oppose it—and subsequently hinted at the possibility of a June rate hike in his speech. For this reason, following Governor Ueda's speech, we changed our view to a June rate hike.

## We expect the BOJ to slightly modify its forward guidance to maintain a hawkish stance while hinting that it is approaching the neutral rate.

We expect the BOJ to slightly revise its forward guidance on monetary policy alongside the June rate hike. Specifically, as shown in Exhibit 5, we expect it to be modified to maintain a hawkish stance while hinting that it is approaching the neutral rate.

Exhibit 5: We Expect the BOJ to Modify its Forward Guidance to Maintain a Hawkish Stance While Hinting That It is Approaching the Neutral Rate

<table><tr><td>Current Forward Guidance</td><td>Forward Guidance Post June MPM</td></tr><tr><td>Given that real interest rates are at significantly low levels, the Bank will continue to raise the policy interest rate and adjust the degree of monetary accommodation, in response to developments in economic activity and prices as well as financial conditions. In this regard, it will consider the timing and pace of adjustment, while closely monitoring the impact of the future course of the situation in the Middle East on Japan&#x27;s economic activity and prices and examining the likelihood of realizing the baseline scenario of the outlook for economic activity and prices and the risks to the outlook.</td><td>Given that real interest rates remain at low levels, the Bank will continue to raise the policy interest rate and adjust the degree of monetary accommodation, in response to developments in economic activity and prices as well as financial conditions. In this regard, it will consider the timing and pace of adjustment, while closely monitoring the impact of the future course of the situation in the Middle East on Japan&#x27;s economic activity and prices and examining the likelihood of realizing the baseline scenario of the outlook for economic activity and prices and the risks to the outlook, especially upside risks to prices.</td></tr></table>

Red text indicates our expected revisions to the forward guidance.  
Source: BoJ, GS Global Investment Research

After the June hike, we expect the next rate hike in January 2027. We also maintain our view that the terminal rate will be $1.5\%$ , equal to the neutral rate, and that the policy rate will reach $1.5\%$ in July 2027. However, the timing of rate hikes is likely to be significantly influenced by market developments and the degree of progress in communication with the government.

Regarding the rate hike path from June onward, considering that the BOJ is not behind the curve (with underlying inflation still below $2\%$ ) and that the future pace of growth will be gradual, we believe the BOJ will conduct gradual but steady rate hikes at intervals of around six months. After the June hike, we accordingly expect rate hikes in December or January next year, followed by June or July, with the policy rate reaching $1.5\%$ , equal to the neutral rate.

Given that the policy rate has been raised to $1\%$ and is approaching the neutral rate, the current assessment and outlook for the economy and prices, as well as risk assessments, are likely to become more important in decisions to raise interest rates. Because of this, the actual timing of rate hikes is more likely to be at meetings where the Outlook Report is published (January, April, July, and October), when analysis on these issues has been accumulated within the BOJ and assessments have solidified, rather than at meetings where the Outlook Report is not published (March, June, September, and December).

After the June hike, we therefore expect the next rate hike in January 2027, followed by July, with the policy rate reaching the terminal rate of $1.5\%$ .

However, the timing of rate hikes could be significantly influenced by market developments and the degree of progress in communication with the government. On this point, prior to the December meeting last year and the June meeting this year (which saw yen depreciation and a rise in long-term interest rates), a meeting was held between Governor Ueda and Prime Minister Takaichi, and once the groundwork for a rate hike was laid, a speech by the Governor or Deputy Governor hinted at the possibility of a rate hike at the upcoming meeting. For this reason, while our base case scenario for rate hikes after June is January and July 2027, the timing of rate hikes could be brought forward depending on when the conditions for a rate hike are in place from the perspective of communication with the government.

Regarding the reduction in JGB purchases, it is likely that the BOJ will maintain its current JGB purchase plan until March 2027 and keep purchases at c.¥2 tn from April 2027 onward.

At the June meeting, the BOJ will also conduct an interim assessment of its current JGB purchase plan up to March 2027 and consider its JGB purchase policy for April 2027 onward. As we discussed in a separate report, we believe it is likely that the BOJ will maintain its current JGB purchase plan until March 2027 and keep purchases at c.¥2 tn from April 2027 onward (Exhibit 6).

Exhibit 6: BOJ is Expected to Gradually Reduce Monthly JGB Purchases Until March 2027 and Maintain Purchases Volume from April 2027 Onward  
BOJ's Monthly JGB Purchase Reduction Schedule  
![](images/2449444bde3af063a15140b777f31e5837e5c81899d9bebdc1fc5b2638cf1f98.jpg)

<details>
<summary>bar-line hybrid</summary>

| Date | Plan (Trillion yen) | Actual (Trillion yen) |
|---|---|---|
| 2024/7 | 5.8 | 6.0 |
| Aug 2024- Reduce monthly purchase by Y400bn per quarter | 5.3 | 5.3 |
| Apr 2026- Reduce monthly purchase by Y200bn per quarter | 2.7 | 2.7 |
| 2027/1 | 2.1 | 2.1 |
| 2027/7 | 2.1 | 2.1 |
</details>

Source: BoJ, Data compiled by GS Global Investment Research

## The Japan Economics Team

## Akira Otani

+81(3)4587-9960

akira.otani@gs.com

GS Japan Co., Ltd.

## Tomohiro Ota

+81(3)4587-9984

tomohiro.ota@gs.com

GS Japan Co., Ltd.

## Yuriko Tanaka

+81(3)4587-9964

yuriko.tanaka@gs.com

GS Japan Co., Ltd.

## Disclosure Appendix

## Reg AC

I, Akira Otani, hereby certify that all of the views expressed in this report accurately reflect my personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Akira Otani GS Japan Co., Ltd..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; $1\%$ or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst

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
