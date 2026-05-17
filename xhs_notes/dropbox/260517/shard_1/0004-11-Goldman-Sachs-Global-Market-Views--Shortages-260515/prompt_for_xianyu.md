你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `建议价格：` 一行，给一个资料类商品常见价格区间，例如 `8-20 元`，不要承诺成交价。
3. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
4. `搜索关键词：` 一行，给 8-15 个关键词，用空格分隔。

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

6. Higher volatility, but not yet broad-based. One of our core views for 2026 was that longer-dated equity volatility was likely to rise structurally, as volatility around the AI theme and its financing or late-cycle macro dynamics became more prominent. Since last September, there has been a clear upward drift in longer-dated implied volatility in the SPX, despite a sharp rally in equities over that period. But the rise in average single stock volatility—and in concentrated indices like Korea—has been much larger and more persistent than the index story. We think that th

[中间内容因长度限制已省略]

attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

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
