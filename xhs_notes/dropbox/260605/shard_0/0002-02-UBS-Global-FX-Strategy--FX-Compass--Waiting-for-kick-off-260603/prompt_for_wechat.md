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
# Global FX Strategy

# FX Compass: Waiting for kick-off

Figure 1: Previous recent world cups have seen FX vol come under pressure   
![](images/e7ce0204ed614868885b4f308f0ddf2a0b23cea702e5641edbd010d3a90f8fe1.jpg)

<details>
<summary>line</summary>

| Days from start | 1m implied | 3m implied | 1m realized |
| --------------- | --------- | --------- | ----------- |
| -30             | ~3        | ~4        | ~-5         |
| -25             | ~5        | ~6        | ~-3         |
| -20             | ~10       | ~8        | ~-2         |
| -15             | ~8        | ~7        | ~-1         |
| -10             | ~5        | ~5        | ~0          |
| -5              | ~3        | ~3        | ~-1         |
| 0               | ~0        | ~0        | ~-2         |
| 5               | ~-2       | ~-2       | ~-3         |
| 10              | ~-3       | ~-3       | ~-4         |
| 15              | ~-4       | ~-4       | ~-5         |
| 20              | ~-5       | ~-5       | ~-6         |
| 25              | ~-6       | ~-6       | ~-7         |
| 30              | ~-7       | ~-7       | ~-8         |
| 35              | ~-8       | ~-8       | ~-9         |
| 40              | ~-9       | ~-9       | ~-10        |
| 45              | ~-10      | ~-10      | ~-11        |
| 50              | ~-11      | ~-11      | ~-12        |
| 55              | ~-12      | ~-12      | ~-13        |
| 60              | ~-13      | ~-13      | ~-14        |
| 65              | ~-14      | ~-14      | ~-15        |
| 70              | ~-15      | ~-15      | ~-16        |
| 75              | ~-16      | ~-16      | ~-17        |
| 80              | ~-17      | ~-17      | ~-18        |
| 85              | ~-18      | ~-18      | ~-19        |
| 90              | ~-19      | ~-19      | ~-20        |
</details>

Source: Bloomberg, UBS

FX markets remain in thrall to the US-Iran negotiations. Most of last week's G10 FX gains vs the USD were reversed at the start of this week when Iran's threat to break off talks over Israeli operations in Lebanon sent oil prices sharply higher. This geopolitics-driven back and forth is by now well understood and has therefore failed to rekindle implied FX vols, which continue to grind lower. With the USD near the top of the G10 carry rankings, we have argued that this low-vol environment is likely to keep the greenback supported, especially with the intact tailwinds of the AI narrative and high real rates. We do not see clear reasons to change that view, particularly with the football world cup starting next week, an event that has historically coincided with lower realized FX vol (Figure 1). With this in mind, this week we focus on potential challenges to our views.

The first point of focus is today's speech by BoJ Governor Ueda, which marks the last scheduled BoJ communication before the 16 June rate decision. From an FX strategy standpoint, ambiguity about the BoJ's tightening plans is a key reason why we continue to view USDJPY as a buy-on-dips story. A forceful reaffirmation and even an extension of BoJ hiking intentions would be needed to break this yen-negative dynamic, in our view. In absence of that, a USDJPY test above 160 is likely, and if that triggers renewed FX intervention, a rapid return of dip buyers.

Regarding US-Iran negotiations, markets seem focused on the fact that President Trump's rhetoric and actions continue to support expectations of a market-friendly resolution. These expectations suggest the risk asymmetry now lies towards a break in negotiations, which is a scenario that would likely feature renewed USD strength. It is not our baseline scenario, but important to consider given depressed vol levels.

As for US data, markets are positioned for a May employment report that supports the current pricing for a modicum of Fed hikes. With the first FOMC meeting chaired by Chair Warsh two weeks out, we think a very large and clear data surprise in either direction is needed for this priced-in outlook to be meaningfully challenged.

This week we also look into the fundamental flow backdrop underpinning GBP's resilience, highlighting the strength of inbound M&A activity YTD.

# FX

Global

Alvise Marino

Strategist

alvise.marino@ubs.com

+41-44-237 8440

Shahab Jalinoos

Strategist

shahab.jalinoos@ubs.com

+1-212-882-5532

Benjamin Jarrett

Strategist

benjamin.jarrett@ubs.com

+44-20-7567 5430

# Macro overview: Waiting for kick-off

FX markets remain in thrall to the US-Iran negotiations. Most of last week's G10 FX gains vs the USD, driven by expectations of a deal, were reversed at the start of this week when Iran's threat to break off talks over Israeli operations in Lebanon sent oil prices sharply higher. While this geopolitics-driven back and forth supports realized volatility, it is by now well understood by market participants and has therefore failed to rekindle implied FX vols, which continue to grind lower. With the USD near the top of the G10 carry rankings, we have argued that this low-vol environment is likely to keep the greenback supported against lower yielding G10 peers (EUR, JPY and CHF), especially with the intact tailwinds of the AI narrative and high real rates attracting inflows. We do not see clear reasons to change that view, particularly with the football world cup starting next week on 11 Jun, an event that has historically coincided with lower implied and realized FX volatility (Figure 1). With this in mind, this week we focus on upcoming event outcomes that could challenge our views and on potential near-term catalysts.

# Risk #1: Ueda's speech

The first point of focus is today's speech by BoJ Governor Ueda. It marks the last scheduled BoJ communication before the 16 June rate decision, for which 19bp of hikes are currently implied; markets will be alert to any attempt to influence expectations ahead of the meeting (our economists expect a hike). Recent data and market developments point to simmering risks of a dovish lean: oil prices remain below \$100, both national and Tokyo CPI surprised lower in April and in May, with "core core" CPI printing 1.9% y/y and 1.6% y/y respectively from 2.4% and 1.9% in April, and the selloff at the long end of the JGB curve has eased sharply since mid-May. That undermines the case of those who argue the BoJ needs to reassert its anti-inflation credentials to keep the long end under control.

Alvise Marino

Strategist

With USD near the top of G10 FX carry rankings, low vol conditions can be USD-positive

Ahead of Ueda's speech, the data-based case for the BoJ to hike rates has become less clear

Figure 2: Japan's underlying inflation keeps trending lower   
![](images/b0b43bba930a02dc98ee581ae7fc597cfe75f0732ae78cfc366835c557aa3c02.jpg)

<details>
<summary>line</summary>

| Date    | Japan median underlying inflation (%, y/y) |
|---------|------------------------------------------|
| Jan-21  | ~0.00                                    |
| Apr-22  | ~0.40                                    |
| Jul-23  | ~2.20                                    |
| Oct-24  | ~1.40                                    |
| Jan-26  | ~0.60                                    |
</details>

Source: Macrobond, UBS

Figure 3: CB pricing changed the least for the BoJ in G10   
![](images/24bb77bd55cb42d3d5bbf13e0bdad59bbde45b9b89d7a9a312a5dcf0056bc3cf.jpg)

<details>
<summary>bar_line</summary>

1y1y swap rates (%)
| Currency | Change since 27 feb (bp, rhs) | Latest (%) |
| :--- | :--- | :--- |
| JPY | 0.85 | 40 |
| AUD | 1.48 | 108 |
| CHF | 1.49 | 6 |
| CAD | 2.28 | 69 |
| SEK | 2.32 | 58 |
| NZD | 2.41 | 88 |
| NOK | 2.45 | 103 |
| EUR | 2.58 | 63 |
| GBP | 3.75 | 102 |
| USD | 3.90 | 95 |
</details>

Source: Bloomberg, UBS

Moreover, earlier concerns around the Takaichi administration's fiscal expansion plans were eased by a supplementary budget announcement with mostly benign details, including an upward revision to FY2025 tax revenues. Our economists note that these improvements should allow the government to extend gasoline subsidies beyond this year; as things stand, they expect subsidies to depress core CPI by \~0.5-0.6pp from August to October. While the BoJ has historically looked through such temporary effects, and our economists think inflation is likely to rebound from current levels, the deceleration in underlying inflation measures to well below 1.0% y/y (Figure 2) remains notable. It is also likely one reason why BoJ policy expectations have risen only modestly

A more benign fiscal easing outlook could also undermine the urge for BoJ tightening

since the start of the US-Iran conflict, in contrast with the more hawkish repricing seen elsewhere in G10 (Figure 3).

From an FX strategy standpoint, this stability in BoJ pricing and the resulting loss of rate support vs G10 peers is a key reason why we continue to view USDJPY as a buy-on-dips story and remain open to the pair breaking above 160, especially if energy prices resume their ascent. While 10-year JGB yields are trading slightly above inflation breakevens, the BoJ policy rate remains well below realized inflation and the BoJ's willingness to close that gap through rate hikes is still clouded by ambiguity. Any signals from Governor Ueda that extend this lack of clarity are therefore likely to reinforce the case for JPY weakness. In that scenario, we still think moves north of 160 could prompt renewed MoF FX intervention, but any resulting dips in USDJPY are likely to attract carry-focused buyers looking to take advantage of low-vol market conditions.

As long as the BoJ's tightening intentions are ambiguous, JPY weakness can extend further

A forceful reaffirmation and even an extension of BoJ hiking intentions would be needed to break this yen-negative dynamic, in our view. We do not rule it out, but front-end USDJPY risk reversal skews remain bid for puts well within this year's range. So, while the premium for USDJPY puts over calls is fading at the long end of the risk reversal skew curve, in the near-term JPY bulls seem much less outnumbered, implying that FX risks around this event are likely balanced and not excessively biased towards expecting a weaker JPY.

A forceful reaffirmation of priced-in hikes is needed to break yen-negative dynamics

Figure 4: USDJPY lower optionality still in demand in 1m   
![](images/9c5a669a9de2542ad856b6cb0e08ae18965aae5b862c8508b8dffd3b7584e9ef.jpg)

<details>
<summary>line</summary>

| Date   | 1m     | 1y     |
|--------|--------|--------|
| Jan-25 | -1.00  | -0.50  |
| Apr-25 | -3.50  | -2.00  |
| Jul-25 | -1.50  | -1.00  |
| Oct-25 | -0.50  | -0.50  |
| Jan-26 | -2.50  | -0.50  |
| Apr-26 | -1.00  | -0.50  |
</details>

Source: Bloomberg, UBS

Figure 5: US-Iran conflict still dominates FX trading   
![](images/5639268c626efdedf406cb314da945fba0bda2eab09c82769c0042d1570dab55.jpg)

<details>
<summary>line</summary>

| Date   | Brent crude vs BBDXY |
|--------|----------------------|
| Jun-25 | ~70%                 |
| Sep-25 | ~80%                 |
| Dec-25 | ~-40%                |
| Mar-26 | ~80%                 |
| Jun-26 | ~90%                 |
</details>

Source: Bloomberg, UBS

# Risk #2: US-Iran negotiations

Turning to the US-Iran negotiations, markets seem focused on the fact that President Trump's rhetoric and actions continue to support expectations of a market-friendly resolution. That is helping keep implied volatility subdued despite the still unresolved state of negotiations and occasional local military skirmishes. Our longstanding view has been that a resolution announcement would initially weaken the USD in a knee-jerk move before the currency regains momentum on strong US fundamentals; the seesaw price action of recent days gives us confidence in that view. However, given how one-sided market expectations around a resolution are, the bigger risk asymmetry now is for a lasting breakdown in talks that leads potentially to renewed military activity. While seemingly a less likely scenario, this outcome is worth considering simply because it would represent a large shock to the relaxed volatility outlook markets are pricing in. In that scenario, renewed upside in energy prices would see the USD test the upper end of our Q2 ranges (EURUSD 1.1450, AUDUSD 0.70, USDJPY 162). To be clear, we see this as a tail risk rather than our baseline, but it again highlights the asymmetric risk profile towards further USD appreciation.

With markets anticipating a conflict resolution, the risk asymmetry is likely towards escalation

# Risk #3: US May employment report

To close the week, markets are looking for an +85K NFP print in May on Friday, with 0.3%mom average earnings growth and a 4.3% unemployment rate (vs +115k / 0.2% mom / 4.3% in Apr) – a touch below our economists' call for a 90K headline and 0.37%mom earnings growth. The run-up to this release has seen mixed US data, with improved reading in May ISM manufacturing (54.0 vs 52.7 in Apr) and Apr JOLTS (7618K vs 6887K in March), but also softer surprises including Apr personal income and spending (0.0%mom and 0.5% mom vs 0.5% and 1.0% in March) and Apr durable goods (0.4%mom non-defence ex air shipments vs 1.3%mom in March). This suggests that numbers in line with expectations, or stronger, could tilt the balance of opinions further in a positive direction and do little to undermine current pricing for possible Fed rate hikes (+18bp by year-end, +25bp by the 17 Mar 2027 meeting).

We suspect a clear negative surprise is likely needed for markets to question current Fed pricing, especially given the hawkish lean of recent comments from officials including Cleveland Fed President Hammack and Kansas City Fed President Schmid. At the same time, with the first FOMC led by Chair Warsh two weeks away, markets may be reluctant to push pricing to hawkish extremes absent a crystal clear case for it from the data, mindful that key elements of the current Fed framework, such as forward guidance, could change under the new leadership. All told, we believe it would take a large surprise in either direction to challenge the current narrative; absent that, the bar for vol to rebound on US data alone seems high.

A US employment report in line with consensus would reaffirm rate support for the USD

A large NFP surprise in either direction is likely needed to challenge the low vol market outlook

# GBP: Supported by fundamental flows

GBP has continued to show resilience in the face of ongoing political developments surrounding the future of Prime Minister Sir Keir Starmer's premiership. Ahead of the local elections last month, we wrote about how the key source of concern for GBP is ultimately the fiscal outlook, and that a lack of reaction in GBP to the political news flow could arguably be justified so long as the perceived risk of the existing fiscal rules being broken/loosened is sufficiently low. This has largely held true since. As we have covered it in detail in recent weeks (link, link, link), we leave the politics to one side in this article and instead look into the fundamental flow backdrop for GBP, arguing that it continues to provide fundamental support for sterling behind the noise. We target EURGBP 0.8750 for end-Q2, the upper end of the YTD range, followed by gradual GBP appreciation to 0.8500 by year-end.

# Benjamin Jarrett

Strategist

GBP has continued to show resilience despite ongoing political noise

Figure 6: UK broad basic balance supported by portfolio inflows   
![](images/ce925f9c41df279e6a51385530c256e9ff1a47bd0f23ce0a66eea20a4f2af4bb.jpg)

<details>
<summary>bar_line</summary>

UK Broad Basic Balance, Quarterly Data, %GDP (Positive = net inflow)
| Year | Current account (%) | FDI (%) | Portfolio investment (%) | Broad basic balance (curr acc + FDI + port inv) (%) |
|---|---|---|---|---|
| 2016 | -3.5 | 11.5 | 18.5 | 5.0 |
| 2017 | -4.0 | 13.0 | 17.0 | 10.0 |
| 2018 | -3.0 | 10.0 | 11.0 | 8.0 |
| 2019 | -3.5 | 4.0 | -18.0 | -25.0 |
| 2020 | -3.0 | 8.0 | 14.0 | 17.0 |
| 2021 | -3.5 | 7.0 | -12.0 | -5.0 |
| 2022 | -3.0 | -3.0 | 9.0 | 12.0 |
| 2023 | -3.5 | 3.0 | -18.0 | -10.0 |
| 2024 | -3.0 | 1.0 | -12.0 | -10.0 |
| 2025 | -3.5 | 3.0 | 18.0 | 14.0 |
| 2026 | -3.0 | -2.0 | 8.0 | 6.0 |
</details>

Source: Macrobond, UBS

We came into the year constructive on GBP, with the benign balance of payments backdrop being a key part of our rationale. Data for Q4 (released end-Q1) showed continued strength in portfolio investment (Figure 6), marking the third consecutive quarter of net portfolio inflows. In Q4 on aggregate, domestic investors repatriated into domestic equities and reduced purchases of overseas debt, while overseas investors continued to buy both domestic equities and debt (Figure 7, Figure 8). These flows were clearly supportive for GBP last year and, given relatively rangebound and resilient price action in sterling so far in 2026, we would not be surprised if BoP data for Q1 and Q2 show a similar backdrop when released.

The UK's broad basic balance has been improving, supported by portfolio inflows

Figure 7: UK equity portfolio investment   
![](images/8620de1240711fa4a54ddfdb68ce99f58b23e5999c0e2c5f3bb8ed203b64b135.jpg)

<details>
<summary>bar_line</summary>

UK Portfolio Investment, Equity (Quarterly Data, %GDP) (Positive = net inflow)
| Year | Portfolio investment, equity, liabilities (overseas investors) (%) | Portfolio investment, equity, assets (domestic investors) (%) | Portfolio investment, equity, net (%) |
|---|---|---|---|
| 2016 | 3.5 | 4.8 | 9.2 |
| 2017 | -1.2 | -1.8 | -14.5 |
| 2018 | 4.2 | 14.5 | 8.9 |
| 2019 | -0.8 | 6.2 | -1.5 |
| 2020 | 1.5 | 18.0 | -7.0 |
| 2021 | -0.5 | -5.0 | -3.0 |
| 2022 | 3.8 | 15.5 | 8.5 |
| 2023 | -0.3 | -1.0 | -10.5 |
| 2024 | -0.7 | 5.0 | -6.0 |
| 2025 | 0.5 | 9.0 | -1.5 |
| 2026 | 1.2 | 5.5 | 6.0 |
</details>

Source: Macrobond, UBS

Figure 8: UK debt portfolio investment   
![](images/530624e9944482d9cadc59582cbc4fd3b27f074360e336e662016c3916e57872.jpg)

<details>
<summary>bar_line</summary>

UK Portfolio Investment, Debt (Quarterly Data, %GDP) (Positive = net inflow)
| Year | Portfolio investment, debt, liabilities (overseas investors) (%) | Portfolio investment, debt, assets (domestic investors) (%) | Portfolio investment, debt, net (%) |
|---|---|---|---|
| 2016 | 1.5 | -3.0 | 14.0 |
| 2017 | 3.0 | -8.0 | 15.0 |
| 2018 | 4.0 | -5.0 | 12.0 |
| 2019 | -12.0 | -10.0 | -13.0 |
| 2020 | 8.0 | -5.0 | 10.0 |
| 2021 | 5.0 | -3.0 | 8.0 |
| 2022 | 3.0 | -1.0 | 10.0 |
| 2023 | 5.0 | -8.0 | -8.0 |
| 2024 | 4.0 | -5.0 | -3.0 |
| 2025 | 3.0 | -4.0 | 7.0 |
| 2026 | 3.0 | -3.0 | 1.0 |
</details>

Source: Macrobond, UBS

In addition to official BoP data, wh

[中间内容因长度限制已省略]

that any recommendations or opinions in such this publication or material are not made or provided to you, and (ii) to the maximum extent permitted by law (a) indemnify UBS and its associates or related entities (and their respective Directors, officers, agents and Advisors) (each a 'Relevant Person') for any loss, damage, liability or claim any of them may incur or suffer as a result of, or in connection with, your unauthorised reliance on this publication or material and (b) waive any rights or remedies you may have against any Relevant Person for (or in respect of) any loss, damage, liability or claim you may incur or suffer as a result of, or in connection with, your unauthorised reliance on this publication or material. Korea: Distributed in Korea by UBS Pte. Ltd., Seoul Branch. This report may have been edited or contributed to from time to time by affiliates of UBS Pte. Ltd., Seoul Branch. This material is intended for professional/institutional clients only and not for distribution to any retail clients. Malaysia: This material is authorized to be distributed in Malaysia by UBS Malaysia Sdn. Bhd (Capital Markets Services License No.: CMSL/A0063/2007). This material is intended for professional/institutional clients only and not for distribution to any retail clients. India: Distributed by UBS India Private Ltd. (Corporate Identity Number U67120MH1996PTC097299) 2/F, 3 North Avenue, Maker Maxity, Bandra Kurla Complex, Bandra (East), Mumbai (India) 400051. Phone: +912261556000. It provides brokerage services bearing SEBI Registration Number: INZ000259830; Merchant Banking services bearing SEBI Registration Number: INM000013101; and Research Analyst services bearing SEBI Registration Number: INH000001204. Name of Compliance Officer Mr. Parameshwaran Shivaramakrishnan, Phone: +912261556151, Email: ol-ubs-sec-compliance@ubs.com Registration granted by SEBI, and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. UBS may have debt holdings or positions in the subject Indian company/companies. UBS may have financial interests (e.g. loan/derivative products, rights to or interests in investments, etc.) in the subject Indian company/companies from time to time. Within the past 12 months, UBS may have received compensation for non-investment banking securities-related services and/or non-securities services from the subject Indian company/companies. The subject company/companies may have been a client/clients of UBS during the 12 months preceding the date of distribution of the research report with respect to investment banking and/or non-investment banking securities-related services and/or non-securities services. With regard to information on associates, please refer to the Annual Report at: https://www.ubs.com/global/en/about\_ubs/investor\_relations/annualreporting.html The Research Annual Compliance Report for UBS India Private Limited is available on www.ubs.com/ubssi under Research tab. Taiwan: Except as otherwise specified herein, this material may not be distributed in Taiwan. Information and material on securities/instruments that are traded in a Taiwan organized exchange is deemed to be issued and distributed by UBS Pte. LTD., Taipei Branch, which is licensed and regulated by Taiwan Financial Supervisory Commission. Save for securities/instruments that are traded in a Taiwan organized exchange, this material should not constitute "recommendation" to clients or recipients in Taiwan for the covered companies or any companies mentioned in this document. No portion of the document may be reproduced or quoted by the press or any other person without authorisation from UBS. Indonesia: This report is being distributed by PT UBS Sekuritas Indonesia and is delivered by its licensed employee(s), including marketing/sales person, to its client. PT UBS Sekuritas Indonesia, having its registered office at Sequis Tower Level 22 unit 22-1,Jl.Jend. Sudirman, kav.71, SCBD lot 11B, Jakarta 12190. Indonesia, is a subsidiary company of UBS AG and licensed under Capital Market Law no. 8 year 1995, a holder of broker-dealer and underwriter licenses issued by the Capital Market and Financial Institution Supervisory Agency (now Otoritas Jasa Keuangan/OJK). PT UBS Sekuritas Indonesia is also a member of Indonesia Stock Exchange and supervised by Otoritas Jasa Keuangan (OJK). Neither this report nor any copy hereof may be distributed in Indonesia or to any Indonesian citizens except in compliance with applicable Indonesian capital market laws and regulations. This report is not an offer of securities in Indonesia and may not be distributed within the territory of the Republic of Indonesia or to Indonesian citizens in circumstance which constitutes an offering within the meaning of Indonesian capital market laws and regulations.

The disclosures contained in research documents produced by UBS AG, London Branch or UBS Europe SE shall be governed by and construed in accordance with English law.

UBS specifically prohibits the redistribution of this document in whole or in part without the written permission of UBS and in any event UBS accepts no liability whatsoever for any redistribution of this document or its contents or the actions of third parties in this respect. Images may depict objects or elements that are protected by third party copyright, trademarks and other intellectual property rights. © UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/d7aaec685ee796e96c7ecaf5325843e41b27d2edcd78127970a3bc7bad373dac.jpg)
"""
