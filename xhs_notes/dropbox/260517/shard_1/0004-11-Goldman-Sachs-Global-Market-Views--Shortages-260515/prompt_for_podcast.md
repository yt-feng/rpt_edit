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
# Global Market Views: Shortages

1. The risks of relief. The Iran ceasefire and the reduction in deep downside tails have allowed the market to look ahead and compress risk premia across a range of assets. That type of narrowing in the distribution is often associated with sharp market gains in situations of fundamental uncertainty, and this has proved to be the case again. Despite oil prices and yields staying elevated, a broad range of assets—including US equities, high carry/commodity FX, and EM—have recovered smartly, and renewed AI optimism has pushed those exposures to new cycle highs. The common element is that shortages—in commodities and the AI supply chain—are driving capital flows. After a sharp recovery, the distribution of risks is more balanced. The most obvious downside threat is still a re-escalation of hostilities in the Middle East or a prolonged Hormuz closure that raises the probability of even higher oil prices, higher rates, lower growth and recession. As we wait, the flip side of shortages alongside more resilient growth is upward pressure on bond yields, which the market tends to worry about more when they break new ground. By contrast, even a gradual restart of energy flows should allow some relief across oil prices and rates markets that are now quite hawkishly priced, and lead to a broadening of the positive price action geographically and across sectors. Beyond that, we are in many ways back to the tensions we highlighted in our outlook—between well-valued assets and increasing concentration on the one hand (with AI-related exposures a poster-child for that), and a macro cycle that does not yet show the imbalances and leverage excess that is typical of late-cycle behaviour. Those tensions mean that even if we avoid the worst tails, we are likely to see volatility rise alongside further equity price increases.

Dominic Wilson

+1(212)902-5924

dominic.wilson@gs.com

GS & Co. LLC

Kamakshya Trivedi

+44(20)7051-4005

kamakshya.trivedi@gs.com

GS International

Exhibit 1: Sharp relief in growth worries, policy shock lingers   
![](images/eeff1c31c87fb2982cc772202ff7ef2d29bd752075ba55c9cfe124f045e2207e.jpg)

<details>
<summary>line</summary>

| Date    | Cumulative US growth shocks | Cumulative US policy shocks |
|---------|-----------------------------|------------------------------|
| Apr-25  | -10                         | 10                           |
| Jun-25  | 5                           | 3                            |
| Aug-25  | 8                           | 0                            |
| Oct-25  | 9                           | -5                           |
| Dec-25  | 7                           | -10                          |
| Feb-26  | 9                           | -5                           |
| Apr-26  | 4                           | -10                          |
| Apr-27  | 15                          | -5                           |
</details>

Source: GS Global Investment Research

2. Iran re-escalation still the main risk. The biggest risk to the macro picture still comes from a failure to resolve the Iran war and the flow of oil. Equities and other risk assets have priced in sUBStantial relief on the basis that the deep tail risks are avoided. While that assumption holds, markets have been more tolerant of headline risk. But the flip side to this higher threshold for worry is that a more serious challenge to the market's optimism could lead to a larger repricing. Although we agree that the risks have fallen, the prospect of more adverse outcomes is still very real, and we think that deeper downside tail is underpriced. There is a challenging circularity here too: although markets are looking through any temporary disruptions, it may also be that another bout of market worry is needed to force an agreement that allows oil flows to resume. The longer we go without a clear peace agreement and a convincing reopening of the Strait of Hormuz, the more likely we are to revisit that risk as energy product shortages become clearer. We continue to think there is value in hedges against this outcome. Out-of-the money downside in European equities, credit and FX still screens best in our cross-asset comparisons. Longs in oil may also continue to be protective, though are also vulnerable to a full resolution of the crisis.

Exhibit 2: Oil price risks still skewed to the upside   
![](images/9c8a51ec964a3d3c0e40e37ee5fa6401b060ef50e3f4114633056fd68cdbf996.jpg)

<details>
<summary>line</summary>

| Date   | Benign* (Flows Fully Recover by Mid-June, No Scarring) | Base Case (Flows Fully Recover by End-June, 0.5mb/d Scarring) | Adverse (Flows Fully Recover by End-July, 0.5mb/d Scarring) | Severely Adverse (Flows Fully Recover by End-July, 2.5mb/d Scarring) | Forwards |
|--------|----------------------------------------------------------|---------------------------------------------------------------|-------------------------------------------------------------|------------------------------------------------------------------|----------|
| Jan-26 | 65                                                       | 65                                                            | 65                                                          | 65                                                               | 65       |
| Apr-26 | 100                                                      | 100                                                           | 100                                                         | 140                                                              | 100      |
| Jul-26 | 90                                                       | 95                                                            | 105                                                         | 130                                                              | 95       |
| Oct-26 | 85                                                       | 90                                                            | 100                                                         | 120                                                              | 90       |
| Jan-27 | 80                                                       | 85                                                            | 95                                                          | 115                                                              | 85       |
| Apr-27 | 75                                                       | 80                                                            | 90                                                          | 110                                                              | 80       |
| Jul-27 | 70                                                       | 75                                                            | 85                                                          | 105                                                              | 75       |
| Oct-27 | 65                                                       | 70                                                            | 80                                                          | 100                                                              | 70       |
</details>

\*Benign scenario includes higher US and core OPEC production.   
Source: GS Global Investment Research

Exhibit 3: Real income softness ahead for the US   
![](images/d5e61bce643393ff311627483e8d30e230e2ddac1c52c1e1de589f2818ff36db.jpg)

<details>
<summary>line</summary>

| Date   | US Real Disposable Personal Income | US Real Consumer Cash Flow* |
|--------|------------------------------------|-----------------------------|
| Jun-25 | 1.9                                | -                           |
| Sep-25 | 1.8                                | -                           |
| Dec-25 | 1.3                                | 1.3                         |
| Mar-26 | 1.1                                | 1.6                         |
| Jun-26 | 0.6                                | 1.3                         |
| Sep-26 | 0.8                                | 0.3                         |
| Dec-26 | 1.2                                | 0.6                         |
</details>

Note: Dashed lines indicate GS forecasts.   
\*Adjusted for the timing of OBBBA-related boosts to tax refunds and reductions in tax payments.   
Source: Bureau of Economic Analysis, Haver Analytics, GS Global Investment Research

3. Macro optimism already well priced. The market has already priced significant relief. Our standard estimates of US growth pricing from the joint shifts in equities and bonds now stand at 2.5%. These measures may overstate the true cyclical optimism, since tech and commodity strength may be boosting them for other reasons, but they are consistent with a market that is already looking through the short-term weakness we expect to the better growth outlook in 2027, and is now potentially overshooting those levels. On our forecasts, there is room for some policy relief in the months ahead (our rate forecasts are generally dovish to market pricing) conditional on an Iran resolution. But with the US economy and labor market holding up better than widely expected, and inflation likely to be elevated at least in the short term, the scope for near-term policy relaxation is likely limited unless there is a very clear improvement in oil flows and an end to the war. Part of the reason why our measures of growth pricing have risen sharply is that bond yields and equities have been rising steadily together. Markets are now beginning to question whether that combination is sustainable. We think that inflation pressure is likely to begin to fade within a couple of months of the energy price peak and the market is already priced for hikes, including now in the US. So, while we may well see further near-term pressure for higher yields, we think that pressure will ultimately be contained. But given how relaxed equity markets have been about rising rates so far, markets may continue to worry in the coming weeks that a mix of more hawkish policy pricing and less bullish growth pricing may be needed.

Exhibit 4: Market pricing of US growth already moving past our 2027 growth forecasts   
![](images/1a35cdc13a8037100adc7c0f89c67d522eb8936c571483757c037286c90c4687.jpg)

<details>
<summary>line</summary>

| Date    | Value |
|---------|-------|
| Apr-26  | 1.9   |
| Apr-26  | 2.2   |
</details>

Source: GS Global Investment Research

4. Back to AI amid booming capex. The AI theme is back in force and has again been a focal point for markets. Outside energy-related areas, the markets that have moved most decisively through their pre-war highs are AI-heavy indices such as Korea, Taiwan and Nasdaq. As in 2025, concerns in Q1 about the sustainability of the AI boom have dissipated in Q2 in a way that has overlapped with, but is separate to, a broader macro shock. The value creation here continues to favor heavily those involved in supplying the AI investment boom, especially in the semis/memory spaces where shortages are clear. Capex projections have moved sharply higher, driving positive earnings revisions across those beneficiaries, and tech investment spending has now exceeded the peaks from the late 1990s as a share of GDP. But with profits holding up (corporate profits as a share of GDP are also at their highest on record), most of the macro imbalances that signaled growing trouble in the late 1990s are still not visible yet. Worries about private credit, which we think are unlikely to have systemic consequences, have also settled a little.

Exhibit 5: Another sharp rise in hyperscaler capex expectations   
![](images/40893b650da559a2feff5887bee7205dd544a25543ef2980fa28b6776f010c8e.jpg)

<details>
<summary>bar</summary>

Consensus US Hyperscaler Capex Estimates
| Period | Year | Value (US$ bn) |
| :--- | :--- | :--- |
| Start of Q1 earnings season | 2026 | 673 |
| Start of Q1 earnings season | 2027 | 790 |
| Start of Q1 earnings season | 2028 | 815 |
| Current | 2026 | 755 |
| Current | 2027 | 890 |
| Current | 2028 | 919 |
</details>

Source: FactSet, GS Global Investment Research

Exhibit 6: Tech investment already at record levels   
![](images/cc39a36002468c36786286f04b69448c5285459ebd82e65fbd5eb302f49ee935.jpg)

<details>
<summary>line</summary>

| Year | Tech Investment |
|------|-----------------|
| 1990 | 3.0             |
| 2000 | 4.5             |
| 2010 | 3.5             |
| 2020 | 4.0             |
| 2025 | 4.8             |
</details>

Shading indicates NBER recessions. Tech investment includes private nonresidential fixed investment in software and information processing equipment.   
Source: Haver Analytics, GS Global Investment Research

5. The value challenge. As we highlighted in our outlook for 2026, the AI theme is a poster child for the broader tension between a macro cycle that (ex the Iran shock) still looks like it has room to run and market pricing that already looks quite generous. The latest rally has continued to drive the cumulative value embedded in AI-related companies higher. And while not all of this is directly attributable to AI, the market is taking credit for sUBStantial macro benefits. This increases the vulnerability to worries about whether the benefits will be justified and whether they are appropriately allocated (in particular, whether it is sustainable for them to accrue so heavily to the chip layer). There has been more focus on potential winners and losers this year—and dispersion has risen. But the risk is that the market falls into either a fallacy of aggregation (assuming that more individual companies can be winners than the economy overall can deliver) or of extrapolation (assuming that earnings supported by the investment boom itself can be sustained). As long as earnings and spending plans continue to rise more quickly than expected, there is likely to be a tailwind to the AI complex. But in the process, the market may build a valuation overhang that may need to be resolved at some point.

Exhibit 7: Even more value built into AI-related areas   
![](images/29c497cbb6df2aeaa73370e03df38a3a3991024e71aafffa5147173d143add77.jpg)

<details>
<summary>bar_stacked</summary>

Change in Market Cap/Valuation From Nov. 30 2022 to May 14 2026 vs. GS Estimates of PDV of Potential AI Capital Revenues
| Category | Change in Market Cap ($ trillion) | Change in Reported Valuation ($ trillion) | GS Estimates of Present Discounted Value ($ trillion) |
| :--- | :--- | :--- | :--- |
| S&P 500 | 31.5 | 0.0 | |
| GS TMT AI Basket + Private Companies | 11.8 | 2.7 | Hyperscalers |
| GS Estimate - Upper Bound | 0.0 | 0.0 | |
| Semiconductors + Private Companies | 11.8 | 2.7 | Semiconductors |
| GS Estimate - Baseline | 0.0 | 0.0 | |
| GS Estimate - Lower Bound | 0.0 | 0.0 | |
Private AI-Related Companies (GS Estimate - Upper Bound) and Private AI-Related Companies (GS Estimate - Lower Bound) are highlighted.
</details>

"Semiconductors", "hyperscalers", and "other AI-related" are constituents of the GS TMT AI basket (developed by GS Global Banking & Markets)

Source: Bloomberg, FactSet, GS FICC and Equities, GS Global Investment Research

6. Higher volatility, but not yet broad-based. One of our core views for 2026 was that longer-dated equity volatility was likely to rise structurally, as volatility around the AI theme and its financing or late-cycle macro dynamics became more prominent. Since last September, there has been a clear upward drift in longer-dated implied volatility in the SPX, despite a sharp rally in equities over that period. But the rise in average single stock volatility—and in concentrated indices like Korea—has been much larger and more persistent than the index story. We think that this is partly because there has been more focus on “distributional” volatility within the AI theme (winners versus losers) than on “macro” volatility (the aggregate value). This has raised single stock volatility but pushed correlations to record lows, limiting the upward pressure on volatility in broad-based indices. We still think that there are good reasons for index volatility to rise over time and any macro shock should drive correlations higher. So we still like pairing long equity views with longs in longer-dated SPX volatility and see longer-dated equity options as appealing ways to limit losses while retaining exposure to further equity upside. And we generally like the idea of owning volatility across assets, whenever it cheapens meaningfully. But the mix of high single stock volatility and low correlation—which we saw at points in the late 1990s too—does mean that index volatility may rise less than expected in some of these shocks.

Exhibit 8: Rise in single stock volatility more persistent than at the index level   
![](images/01738bd485d74cfb0c0b52d338800a98baf193afd54bd97c0fcc51ffd360472f.jpg)

<details>
<summary>line</summary>

| Date   | Implied Volatility | Average Single Stock Implied Volatility | Implied Correlation (right) |
|--------|--------------------|------------------------------------------|-----------------------------|
| Sep-25 | ~0.1               | ~0.1                                     | ~0.2                        |
| Oct-25 | ~1.5               | ~2.5                                     | ~0.25                       |
| Nov-25 | ~2.5               | ~4.5                                     | ~0.3                        |
| Dec-25 | ~3.5               | ~5.5                                     | ~0.28                       |
| Jan-26 | ~2.5               | ~4.5                                     | ~0.24                       |
| Feb-26 | ~3.5               | ~6.5                                     | ~0.26                       |
| Mar-26 | ~4.5               | ~7.5                                     | ~0.3                        |
| Apr-26 | ~5.5               | ~8.5                                     | ~0.32                       |
| May-26 | ~2.5               | ~9.5                                     | ~0.2                        |
</details>

Source: GS FICC and Equities, GS

Exhibit 9: Index volatility and correlations still low versus the late 1990s   
![](images/f7b83c70002e4bd23ebe034dfb4d112abe2725c3381a037325fdd77fa244518b.jpg)

<details>
<summary>bar_line</summary>

| Category                     | Volatility Range | Correlation |
| ---------------------------- | ---------------- | ----------- |
| Average Single Stock Implied Volatility | 27        

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
