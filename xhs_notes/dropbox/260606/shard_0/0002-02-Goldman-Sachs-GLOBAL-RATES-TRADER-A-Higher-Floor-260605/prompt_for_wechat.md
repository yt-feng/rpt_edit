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
GLOBAL RATES TRADER

A Higher Floor

The strong employment report has reinforced a higher distribution around US yields. We still think a long pause from the Fed is more likely than hikes and expect US yields to end the year lower than spot levels. However, the combination of solid growth news and unresolved inflationary pressure is likely to keep front-end pricing skewed towards hikes in the near term, even with ongoing prospects for energy price relief on any confirmation of a US-Iran deal. We now expect 10y UST yields to end the year at $4.4\%$ from $4.1\%$ previously. Given yields are currently above this level, we expect limited spillover effects into other G10 markets and keep most other yield forecasts unchanged. That said, we raise our 10y Gilt forecasts by 10bp to $4.5\%$ for end-2026 given the higher beta exhibited by UK rates in recent years. We continue to expect earlier ECB hikes (starting next week) and weaker growth outcomes to restrain yields in Europe—tactically we think US 5y yields have room to rise on a relative basis versus Europe. In Japan, the hawkish shift in the BoJ communication raises the prospect of 5y rate underperformance on the curve, but we are not yet expecting the BoJ to signal a faster pace of tightening that would create the conditions to stabilize forward yields.

# United States and Canada

\- Shifting the distribution. We think the May US labor market report sets a higher floor on US yields for now. Firm growth and ongoing inflation risk are likely to keep the market pricing clear asymmetry towards hikes in the near term. The main factor that likely held the market back from an even more front-loaded selloff was the relative stability in the unemployment rate and wage growth. Our economists have revised their projected Fed path, pushing out the final two rate cuts in their forecast to June and December 2027. Reflecting this, we have revised our UST yield forecasts higher and now see 2y and 10y yields ending 2026 at $3.8\%$ and $4.4\%$ respectively (from $3.4\%$ and $4.1\%$ previously), levels consistent with the market converging towards a more balanced distribution of risks around the policy path by year-end alongside relative stability in longer-term forwards (e.g. 5y5y, which are currently about fair). That dovish convergence in pricing likely requires some amount of validation from the data, which we expect over time under our economists' forecast for a moderation in sequential inflation and an uptick in the unemployment rate by year-end. But nearer-term risks are more balanced, with vulnerability that firmer data or a

# George Cole

+44(20)7552-1214

george.cole@gs.com

GS International

# William Marshall

+1(212)357-0413

william.c.marshall@gs.com

GS & Co. LLC

# Simon Freycenet

+44(20)7774-5017

simon.freycenet@gs.com

GS Bank Europe SE - Paris

Branch

# Isabella Rosenberg

+1(212)357-7628

isabella.rosenberg@gs.com

GS & Co. LLC

# Friedrich Schaper

+1(917)343-3214

friedrich.schaper@gs.com

GS & Co. LLC

# Loic Mathys

+44(20)7051-1664

loic.mathys@gs.com

GS International

more concrete hawkish shift in Fed communication see hike risks pulled forward (which would likely see leadership in sell-offs move into late-26/early-27 from mid-27 pricing).

\- Reds run ahead. 1y1y rates (reds) have been the most volatile point along the US forward curve since the onset of the conflict, re-rating by about 110bp versus end-February levels and generally leading the way in both sell-offs and rallies. That repricing has shifted the prior front-end inversion into a hump, with a positive slope between 1y and 1y1y, and inversion from 1y1y to 2y1y. We think there are multiple routes to see that relative cheapness in 1y1y moderate. It is typical to see the 1y1y point lead on the curve in sharp inflections in front-end rates (Exhibit 1). While an extension of acute front-end cheapening can see further 1y1y underperformance, we would expect the opposite to hold on a reversal lower in yields, and we think that a period of stabilization can be a source of pressure relief. We think that can happen either via more benign inflation signals that moderate the upward slope priced into the front-end (1y/1y1y flattening), or due to a more resilient growth and labor market backdrop that either shift the timing of hike risk further in or start to undo the inversion priced in further out (1y1y/2y1y steepening) if the Fed signals a more patient approach.

Exhibit 1: The 1y1y point has typically led on the US curve during sharp inflections in front-end rates   
3m change in 2y swap rate vs 1y/1y1y/2y1y swap fly return (higher = belly underperforms)   
![](images/a5c646ec18c6db6ce1fa30d2d9defc11c201efb9e1bd6fc0b970c228d5dd91e2.jpg)

<details>
<summary>line</summary>

| Date   | 3m change in 2y swap rate (bp) | 3m return to 1y/1y1y2y1y swap fly (rhs) (bp) |
|--------|----------------------------------|-----------------------------------------------|
| Jun-21 | ~0                               | ~0                                            |
| Jun-22 | ~180                             | ~150                                          |
| Jun-23 | ~-100                            | ~-50                                          |
| Jun-24 | ~-150                            | ~-100                                         |
| Jun-25 | ~-50                             | ~-50                                          |
| Jun-26 | ~100                             | ~75                                           |
</details>

Source: GS Global Investment Research, GS FICC and Equities

Exhibit 2: Solid YTD Money Fund AUM growth reflects the higher-for-longer front-end yields   
![](images/48d1424026fac8353df5d2368a05e09cd7478f900f83da37d4387dd5facca246.jpg)

<details>
<summary>line</summary>

| Month | 2024 | 2025 | 2026 |
|-------|------|------|------|
| Jan   | 0.0  | 0.0  | 0.0  |
| Feb   | 0.05 | 0.05 | 0.05 |
| Mar   | 0.1  | 0.1  | 0.1  |
| Apr   | 0.15 | 0.15 | 0.15 |
| May   | -0.1 | -0.1 | -0.1 |
| Jun   | 0.15 | 0.15 | 0.15 |
| Jul   | 0.2  | 0.2  | 0.2  |
| Aug   | 0.3  | 0.3  | 0.3  |
| Sep   | 0.4  | 0.4  | 0.4  |
| Oct   | 0.5  | 0.5  | 0.5  |
| Nov   | 0.65 | 0.65 | 0.65 |
| Dec   | 0.8  | 0.8  | 0.8  |
</details>

Source: GS Global Investment Research, Crane Data

■ Money fund AUM heading higher. Growth in money fund AUM has been strong following a larger drop around the mid-April tax deadline compared to recent years. Year-to-date, however, cumulative AUM growth is only slightly above the 2024 and 2025 pace (Exhibit 2). We anticipated a deceleration in the pace of money fund growth this year on our expectations of lower front-end rates, a steeper overall curve, and positive equity returns. Even as the expectations for a steeper curve (e.g. 3m/2y or 3m/10y) and solid risk asset returns have been playing out, a Fed on hold baseline skews risks towards firmer AUM growth. Throughout this environment, T-bills have remained supported and still look slightly rich to fundamentals in spite of a rebuild in supply. Broadly, we think this reinforces our earlier assessment on underlying liquidity conditions and the scope to sustain a lower pace of RMPs.

Canadian data dashboard warrants pricing more two-sided risks. Following repeated downside inflation surprises and the growth contraction that has put the Canadian economy into a recession, the BoC will have to weigh uncertain inflation risks from the conflict in the Middle East against activity weakness even as this week's stronger labor report quelled more urgent concerns. Market pricing through year-end has remained notably hawkish through some of the more dovish signals from domestic fundamentals, with about 35bp of hikes priced by December. While we think placing some weight on an eventual return towards the middle of the neutral range is reasonable, we think the hurdle to hike in the near term is high, particularly as long as USMCA negotiations are unresolved. Given the risks to activity, we think additional cuts cannot be written off and continue to see value to receiving the front-end of the CAD curve. That said, we continue to prefer 2s5s steepeners over outright longs, as we think the front-end should be comparatively sticky versus the belly in broader sell-offs, whereas there is room still to reorient the near-term path and/or delay the timing of hikes on additional data disappointment.

# Europe

July signaling key for EUR front-end pricing. Our economists expect the ECB to deliver a 25bp hike as their macroeconomic projections are likely to show a substantial and sticky core HICP overshoot above the 2% target. We believe the ECB will continue to defend a meeting-by-meeting approach, but any signals on the likelihood of an additional hike in July will be closely watched. We note that July pricing has partly decoupled from its relationship with December pricing since mid-May, suggesting some vulnerability should President Lagarde hint at willingness to tighten policy faster than in quarterly increments. At the same time, any signals that July is likely to be a pass (for example, any sense of ‘patience’ in waiting for further data) is likely to see December pricing catch down to the July slope pricing as the market puts higher weight on the possibility of a ‘one-and-done’ hike in June. On our baseline, the ECB will hike, which offers relatively unattractive risk-reward longs on Z6. We prefer terminal rate longs instead as growth signals weaken and ECB hikes help anchor forward rates.

HICP pricing some relief, real rates to fall further. HICP pricing has declined in recent weeks, alongside relief in energy markets as confidence in an eventual US-Iran deal increased. Pricing is still modestly above our forecasts in the coming year, but our fair value model for inflation forward pricing shows that the recent relief rally has moved further than macro factors and energy prices imply (Exhibit 3). The rebalancing of the oil market via not only temporary inventory drawdowns but also weaker oil demand not only clips the upside risks to energy prices but also reveals the potential downside growth effects from the current shock. As a result, risk-reward remains balanced on the HICP curve. Given the modest cheapening in inflation vs our macro model, in combination with ongoing weakness in growth signals we continue to recommend long 5y5y real EUR swap rates.

Exhibit 3: The recent decline in traded inflation has outpaced what the macro and energy pricing imply   
Fair value model based on energy prices, core inflation, the euro currency and the level of nominal yields   
![](images/b9210ddb0b0bcf69646ea2b5549abe52a6b3e03beaca0ac25c874a5d092e96e3.jpg)

<details>
<summary>line</summary>

| Date    | Change in EUR 2y2y inflation fitted | Change in EUR 2y2y inflation |
|---------|-------------------------------------|-------------------------------|
| Jan-01  | ~0                                  | ~0                            |
| Jan-22  | ~5                                  | ~5                            |
| Feb-12  | ~0                                  | ~0                            |
| Mar-05  | ~15                                 | ~15                           |
| Mar-26  | ~30                                 | ~25                           |
| Apr-16  | ~35                                 | ~30                           |
| May-07  | ~30                                 | ~25                           |
| May-28  | ~25                                 | ~20                           |
</details>

Source: GS Global Investment Research, GS FICC and Equities, Haver Analytics

Exhibit 4: Signals for Gilt spreads suggest supply is not the key issue for Gilts   
Fair value model based on repo-ois spread, rates volatility, free float, the level of yield and the curve   
![](images/6e0de76e2dde52268511d99644653977ca6869e7cc7b097e6d1db86cef8a4e2f.jpg)

<details>
<summary>line</summary>

| Date    | UK 10y swap spread | UK 10y swap fair value |
|---------|--------------------|------------------------|
| Jun-20  | ~0                 | ~0                     |
| Mar-21  | ~-10               | ~-15                   |
| Dec-21  | ~-5                | ~-10                   |
| Sep-22  | ~30                | ~20                    |
| Jun-23  | ~-10               | ~-15                   |
| Mar-24  | ~-30               | ~-25                   |
| Dec-24  | ~-60               | ~-40                   |
| Sep-25  | ~-55               | ~-50                   |
| Jun-26  | ~-45               | ~-65                   |
</details>

Source: GS Global Investment Research, GS FICC and Equities, Haver Analytics

Fiscal policy still relevant for European spreads. We continue to be positive on front-end sovereign credit as a carry expression in European rates markets. With inflation risks now more balanced, there are reduced prospects for much higher rates volatility, and the market already prices the extent of the upcoming ECB hiking cycle, in our view. The fiscal response to higher energy prices has so far been muted, including in places like France which had provided substantial relief back in 2022/23. But pressure remains on European budgets, especially should flows through Hormuz stay muted. For instance, this week the European Commission decided to allow some exemptions for “energy resilience” measures in the context of fiscal rules, worth 0.3% of GDP for the years 2026-28. While this remains modest, against this backdrop we think front-end EGBs should be better protected should energy price upside re-emerge, in which case we’d expect the credit curve to steepen curves.

■ Macro risks not supply risks key for Gilts. Despite a strong narrative around political and supply risks for the UK bond market, 10y Gilts have quietly performed quite well on asset swap over recent weeks. Gilt risks have relaxed since mid-May with our term premium estimate declining by around 25bp. We think the relative stability — if not strength — of Gilts on asset swap is supporting evidence for the view that risk premium in the Gilt curve is currently more macro-driven rather than supply-driven. Indeed, on our models, we find swap spread valuation near fair (Exhibit 4). Although we find evidence that over recent years the increase in the supply of bonds via large deficits and BoE QT has contributed to higher long-end yields, current term premium volatility seems to derive from macro risks around the medium-term fiscal outlook and near-term inflation. Given that fiscal uncertainty is likely to linger through any potential Labour leadership contest, we think that further macro relief is required for Gilt outperformance, namely additional certainty around the path for inflation, and confirmation that the inflation path is consistent with the BoE on hold. As a result, we prefer to 2s10s curve steepeners given its compatibility with both macro relief and a sticky fiscal risk premium into the 18 June Makerfield by-election. Reflecting the higher beta to global yields in recent years, we raise our 10y Gilt forecast to $4.5\%$ from $4.4\%$ given our higher US 10y yield forecasts as

above.

# Japan

Behind the curve worries remain despite an earlier BOJ hike. The JGB curve flattened this week, reflecting a hawkish repricing of the June BoJ meeting, with BOJ OIS implying nearly a $95\%$ probability of a June hike (up from $70\%$ last week). Governor Ueda signaled greater urgency to tighten and the need to secure market confidence that the BoJ will properly control inflation, supporting the market's repricing and prompting our economists to pull forward their forecast for the next BoJ hike to June from July. Even with the timing adjustment, they have maintained their baseline for a roughly semi-annual pace of hikes. While the curve had flattened somewhat into the speech, the aftermath has seen yields move higher and the curve re-steepen, a pattern at odds with the intuitive response to a hawkish signal. Indeed we find that hawkish policy innovations—proxied as instances with higher 3m OIS yields and a stronger Yen—typically result in bear flattening consistent with a more front-loaded policy reaction (Exhibit 5). Although the shift at the very front-end was directionally hawkish and recent communications have emphasized the importance of securing market confidence, we think the muted move beyond the first few meetings and limited FX response suggests little perceived shift in broader reaction function at this point. A more explicit hawkish shift in the BoJ reaction function (i.e. openness to a faster pace of hikes/higher rate) would be impactful, in our view, but absent that we think that near-term risks remain towards further upward pressure on yields, with more of that cheapness migrating into the belly of the curve.

Exhibit 5: Hawkish BoJ policy innovations typically result in bear flattening consistent with a more front-loaded policy reaction   
![](images/ceae2cd2f119e359cf9821da181f1ab779db618c49768247c6f1db170195ebd3.jpg)

<details>
<summary>bar</summary>

JGB Curve Betas* to Changes in 3m OIS
| Scenario | 2s5s (pp) | 2s10s (pp) | 2s30s (pp) | 10s30s (pp) |
| :--- | :--- | :--- | :--- | :--- |
| JPY Weaker 3m OIS Lower | 0.1 | 0.5 | 1.6 | 1.1 |
| JPY Stronger 3m OIS Lower | -1.2 | -1.2 | -0.4 | 0.7 |
| JPY Weaker 3m OIS Higher | 0.0 | -0.1 | -1.0 | -0.9 |
| JPY Stronger 3m OIS Higher | -0.1 | -0.3 | -0.8 | -0.5 |
*Betas to OIS moving lower are inverted. Sample includes daily changes from 2024-present.
</details>

Source: Bloomberg, GS Global Investment Research

# Latest Thematic Research:

Global Markets Analyst: Revisiting the Outlook for the Fed's Balance Sheet — 21 May 2026

Global Rates Notes: US Treasury Valuations and Requirements for a Yield Reversal — 20 May 2026

Global Markets Analyst: UK T-bills: Not A Magic Bullet For Gilts — 11 May 2026

Global Markets Comment: Market Stress Monitor — 11 May 2026

Rates Vol Monitor: A Look at Hedging the Right Tail — 8 May 2026

# Latest Global Markets Dailies:

The Hedge Value Of Rate Receivers — 28 May 2026

The Energy Shock Impact on Foreign Official Treasury Demand — 27 May 2026

Why Always Gilts? — 14 May 2026

A More Durable Risk Premium in JGBs — 8 May 2026

Trading Terms of Trade Shocks in the Smaller G10 Rates Markets — 21 April 2026

# Forecasts

G10 10y yield forecast 

<table><tr><td colspan="14">G10 10-Year Yield Forecasts</td></tr><tr><td></td><td>USD</td><td>DEM</td><td>FRA</td><td>ITA</td><td>ESP</td><td>GBP</td><td>JPY</td><td>C

[中间内容因长度限制已省略]

e have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not

necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
