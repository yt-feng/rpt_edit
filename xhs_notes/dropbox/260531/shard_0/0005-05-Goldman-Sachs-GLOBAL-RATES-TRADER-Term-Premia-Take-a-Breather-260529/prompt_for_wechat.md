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

# Term Premia Take a Breather

Relaxation about risks from the conflict has compressed Treasury term premium, with only modest contribution from the policy expectations channel so far. We see room for US yields to fall further on additional progress towards a resolution or dovish macro data, but expect deeper rallies to be led by points further in on the curve as the case for continued long-end outperformance looks more challenging. The combination of a hawkish ECB, commodity relief and weaker activity numbers continues to support EUR duration despite the rally in recent weeks—stay long 5y5y EUR real yields. Rates vol should remain lower in Europe, supporting sovereign credit carry despite tight spreads. In the UK, term premium relaxation has probably run its course—we prefer front-end longs and curve steepeners. Next week’s speech by Governor Ueda will be a focal point as markets weigh the likely timing of the BOJ’s next rate hike; while volatility has remained concentrated in longer-term forwards, we think bearish pressure should shift in towards the 5y point over time.

# United States and Canada

Rate rally reflects reduced risk premia. Long-end Treasury yields have continued their descent from their mid-month peak amid ongoing optimism about a potential resolution to the conflict and rebuild in flows through the Strait. The long-end yield move has largely shown up as a compression in Treasury term premium, with only modest contribution from the expectations component of yields (Exhibit 1). That dynamic that has seen the yield curve move steadily flatter through the course of the month despite the back and forth in outright yield levels. While hawkish Fed communication has reinforced the curve shift, we think that the argument for continued long-end outperformance looks more challenging. The rally has undone the relatively modest valuation gap in longer-term forwards and the term premium compression suggests that the market has already embedded a combination of reduced uncertainty and a return of duration's portfolio value. We think a meaningful extension of the yield move would likely need to incorporate some shift in the distribution of risks around the Fed path. Although renewed oil upside would likely reinvigorate inflation worries and add to hawkish policy concerns, it would also erode the factors that have contributed to the relief thus far. Next week's labor market report presents two-way near-term risks—but we expect the slack and wage signals to be key to the market's interpretation—we think more benign

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

underlying inflation pressures and a further reduction in concerns around the conflict can support nearer-term forwards and a steeper curve. Our preference remains to tether any long bias to our performance of the 5y part of the curve.

Consolidation and vol compression favors considering hedges. US rates vol has turned lower following the most recent pop, taking implied vol on longer tails towards conflict-lows and the overall level of vol back to the lower end of our fair value estimates (Exhibit 2). We think there is value to using this reset lower to consider hedges as the rates market balances between a more hawkish Fed tone, optimistic growth pricing, and increased hope about a potential resolution to the conflict—a mix that has seen the front-end lag the reset lower in yields further out the curve. While our baseline is a non-recessionary one (curtailing the clearest route to receivers returns), fading fiscal tailwinds and the hit to disposable income from higher energy prices pose risks to the consumer, and we think US rates are putting too much mass on the right tail of the policy path. Such environments lend themselves well to using modestly out-the-money receivers on short-to-medium tails (i.e. 2-to-5y), with value to owning slightly longer expiries (i.e. 1y over 3m) as hedges against deeper downside risks. Against that, the combination of the relief priced in further out the curve (see above) and compression in rate vol leave short expiry at-the-money payers on longer (e.g. 10y) tails our preferred hedge for investors wary of renewed escalation.

Exhibit 1: The recent US rally has been predominantly driven by a reset in Treasury term premium   
Change in 10y UST term premium/rate expectations, GS estimate   
![](images/0e1923d27874188e877baf7aa52fd938f6ac860f3c937e358dc912adaaab4239.jpg)

<details>
<summary>line</summary>

| Date   | Term Premium | Rate Expectations |
|--------|--------------|-------------------|
| 27-02  | 0            | 0                 |
| 09-03  | 10           | 15                |
| 19-03  | 15           | 25                |
| 29-03  | 20           | 35                |
| 08-04  | 15           | 25                |
| 18-04  | 10           | 20                |
| 28-04  | 15           | 25                |
| 08-05  | 20           | 30                |
| 18-05  | 35           | 35                |
| 28-05  | 10           | 45                |
</details>

Source: GS Global Investment Research, GS FICC and Equities

Exhibit 2: Implied vol is at the bottom of our range of estimates of fair   
Average Implied Vol vs fair value model range   
![](images/56718d947abaeb1b7afc9be770bc12301a0c449a089a6a820d98b91ff5f0f53a.jpg)

<details>
<summary>line</summary>

| Year | Fair Value Model Range (bp/day) | Average Implied Vol (bp/day) |
|------|----------------------------------|------------------------------|
| 2000 | ~5.5                             | ~5.8                         |
| 2002 | ~6.0                             | ~7.5                         |
| 2004 | ~5.5                             | ~6.5                         |
| 2006 | ~5.0                             | ~5.5                         |
| 2008 | ~6.5                             | ~9.5                         |
| 2010 | ~5.0                             | ~7.0                         |
| 2012 | ~4.5                             | ~5.5                         |
| 2014 | ~4.8                             | ~4.5                         |
| 2016 | ~4.5                             | ~4.0                         |
| 2018 | ~4.8                             | ~3.5                         |
| 2020 | ~5.0                             | ~3.0                         |
| 2022 | ~6.0                             | ~7.5                         |
| 2024 | ~5.5                             | ~6.5                         |
| 2026 | ~5.0                             | ~5.5                         |
</details>

Source: GS Global Investment Research, GS FICC and Equities

Wider swap spreads led by risk relief. The long-end has led swap spreads wider over the past month, taking spreads to levels that are slightly wide and leaving the spread curve slightly steep versus the levels implied by our swap spread framework. The performance reflects a few key factors in our view. First has been the easy funding environment; despite some normalization in repo rates towards month-end, we expect the funding backdrop to remain relatively benign (if not necessarily as persistently rich) as the Fed manages reserves towards equilibrium levels. Second, rates vol has declined this week on reports that the US and Iran are nearing a deal to reopen the Strait. We think this has been more meaningful for the long end, supporting the spread curve steepening. Third, there has been little sustained

cheapening pressure on Treasuries versus other forms of duration that would suggest material shifts in the supply/demand balance outside of the initial stage of the conflict. The US-Iran conflict has generated some Treasury selling pressure from foreign official investors, but bank/dealer absorption in March and a more favorable bill supply backdrop in April and early May have likely been offsets. While spreads are slightly wide versus fundamentals, valuations are not stretched, and we think that further progress towards a resolution to the conflict can be supportive via vol moderation and potentially a turn in foreign official demand if the Dollar weakening trend reemerges. We have liked being long 3y spreads for carry, and continue to think that position make sense, but think more levered forward expressions that carry well (e.g. 5y2y) stand to outperform should recent dynamics extend.

# Europe

Still positive EUR duration. European yields have continued to fall alongside the global relief rally over the past week. The prospect of a deal in the Middle East has capped upside risks to inflation (for now) while ECB communication, particularly last week's interview from Board member Schnabel, points to a high likelihood of a June hike. This combination, together with ongoing weak activity signals from surveys, is positive for EUR duration, and we continue to recommend long 5y5y EUR real rates. EUR rates have outperformed the US since the middle of April, and the move in 1y1y cross-market spreads has been particularly large. But divergence in activity signals between the US and Europe should keep these spreads wide. Given that ECB tightening is predominantly due to higher energy prices, the European front-end will remain sensitive to news on commodity flows through the Strait of Hormuz. However, with lingering energy market tightness likely to lead to at least some ECB tightening, we retain a flattening bias beyond U6.

Sovereign spreads tight but still a reasonable carry trade. Since the cease-fire was struck between the US and Iran, we have argued that the potential for a disconnect between front-end rate levels and volatility — with the former being sticky and the latter diminishing — would be consistent with sovereign spread compression. We still believe that further evidence of progress in negotiations towards a deal would see rates volatility decline and sovereign credit benefit as a result. However, we note that sovereign spread compression has run ahead not only of relief in core rates but also in rates volatility. Sovereign spreads have retraced a large portion of their post-conflict widening, with the retracement share decreasing with credit risk (Exhibit 3). Against this, we see a high hurdle for further tightening, even as we still see a place for sovereign credit for carry. Broadly speaking, the Euro area has been a receiver rather than provider of bearish shocks in recent weeks. Moreover, we do not expect domestic politics and policies to be a material headwind to sovereign credit. Fiscal policy responses to the energy shock continue to be muted across the Euro area, and we believe 2027 elections across a number of key Euro area countries are likely to become relevant into Q4.

Exhibit 3: Sovereign spread compression has run ahead of relief in rates levels and volatility   
Retracement from post-conflict peak / wides. Using GS fitted yields   
![](images/4af7d885e4034eb4e02c7786749e4da4fdf32b3e60421a15674e02b940ef8afe.jpg)

<details>
<summary>bar</summary>

| Category | Value (%) |
|---|---|
| 1y1y OIS | 29 |
| 1y1y vol | 53 |
| 10y BTP-Bund | 74 |
| 10y OAT-Bund | 78 |
| 10y Bonos-Bund | 92 |
| 10y EU-Bund | 93 |
</details>

Source: GS Global Investment Research, GS FICC and Equities

Exhibit 4: Recent bull-flattening is consistent with the relief in 10y term premium   
GS fitted yields and term premium model   
![](images/32f40e1bc0cedb17aeefe70de66bed095feae0f66d5dad10b482820ddf707b04.jpg)

<details>
<summary>line</summary>

| Date     | UK 2s10s (bp) | UK 10y term premium (rhs) |
|----------|---------------|----------------------------|
| 02-Jan   | ~75           | ~175                       |
| 22-Jan   | ~80           | ~170                       |
| 11-Feb   | ~95           | ~185                       |
| 03-Mar   | ~65           | ~150                       |
| 23-Mar   | ~45           | ~140                       |
| 12-Apr   | ~55           | ~155                       |
| 02-May   | ~60           | ~160                       |
| 22-May   | ~55           | ~165                       |
</details>

Source: GS Global Investment Research, GS FICC and Equities

Gilts notch up a strong week; expect steepening from here. Although politics will likely remain in focus into the 18 June Makerfield by-election, risks relaxed in the Gilt market again this week as renewed hopes for a US-Iran deal weighed on energy prices. The bull-flattening of the Gilt curve in the last two weeks is consistent with term premium compression — our term premium estimates show a sharp fall after the rise in early May (Exhibit 4). Additionally, Gilts have also outperformed swaps, pointing to a relaxation of supply-related risks. However, we continue to think that durable relief for Gilts will be front-end-led, given that macro data continues to soften, and the UK’s fiscal situation and political risks are likely to remain in focus over coming weeks and months. We recommend 1y forward 2s10s GBP OIS steepeners (target 55bp, stop 25bp) for this view, where negative carry is not particularly punitive.

# Japan

Waiting for a signal on hikes. Markets continue to price over 70% probability of a BoJ hike in June which, while elevated, still reflects some uncertainty about whether the BoJ will move in June or July. Our economists think that a July hike is more likely, judging that the BoJ may feel more comfortable tightening after receiving additional CPI and wage data. Governor Ueda's speech on June 3 $^{rd}$ could provide a meaningful policy signal ahead of the June meeting. His comments last week that the BoJ would conduct policy for “stable inflation” and is more attuned to supply risks at the long end supported long-end outperformance. That relief has extended this week on news of a potential US-Iran agreement, but the 2s10s JGB curve remains steep and over the course of May the repricing in yields was mainly a function of forwards further out, with very little movement in the front-end (Exhibit 5). Fiscal news in June, like the details of the supplementary budget, could raise that risk premium further. We continue to think that domestic factors are the primary driver of higher risk premium and it will take more than global rates relief to bring lasting stability. Given the instability of bear steepening regimes, we would look for the 5y point to bear a greater share of bearish pressure over time.

Exhibit 5: Recent JPY rate repricing mainly a function of forwards further out   
JPY Forward rates, change since end April   
![](images/d5c24ed6f9053f9133287e1539eefe08dc852043f59ddb868632a80960468400.jpg)

<details>
<summary>bar</summary>

| Period | Change since end April (bp) |
|---|---|
| 1y | 1.5 |
| 1y1y | -6.0 |
| 2y1y | -1.5 |
| 3y1y | 5.0 |
| 4y1y | 11.0 |
| 5y1y | 19.0 |
| 6y1y | 24.0 |
| 7y1y | 28.0 |
| 8y1y | 30.5 |
| 9y1y | 31.0 |
| 10y1y | 33.0 |
</details>

Source: GS Global Investment Research, GS FICC and Equities

Exhibit 6: NZD forwards have decoupled notably from spot policy   
![](images/7840e7e4dc3655c83e20cb7095ced20fcd7ee973c09c1e783d83dc7f93207475.jpg)

<details>
<summary>line</summary>

| Year | 1y1y (%) | OCR (%) |
|------|----------|---------|
| 2006 | 7.0      | 7.0     |
| 2008 | 8.5      | 8.5     |
| 2010 | 4.0      | 3.0     |
| 2012 | 3.0      | 3.0     |
| 2014 | 4.5      | 3.5     |
| 2016 | 2.5      | 2.0     |
| 2018 | 2.0      | 2.0     |
| 2020 | 0.5      | 0.5     |
| 2022 | 5.5      | 5.5     |
| 2024 | 4.5      | 5.5     |
| 2026 | 4.0      | 2.5     |
</details>

Source: GS FICC and Equities, GS Global Investment Research

# Australia and New Zealand

Earlier RBNZ hikes. The RBNZ kept rates on hold this week in a contentious meeting in which Chair Breman had to cast a tie-breaking vote. The revisions to the policy path were notably hawkish across the forecast horizon, and our economists now expect a hike at each of the July and September meetings (instead of December and February) in line with the guidance at the press conference. Beyond the initial hikes, however, our economists think the outlook for inflation and the labor market should be sufficiently weak to keep further hikes in check. Against that, forwards remain quite elevated relative to our or the RBNZ's policy projections (about 60bp above the peak), with more than 125bp of hikes priced cumulatively through end-27 (Exhibit 6). While starting levels and the speed of response are decidedly different from the RBA, a willingness to tighten policy despite still notable slack in the economy and medium-term fiscal consolidation can still work to trim right tail risks and potentially help to compress some of the right tail risks priced into the forwards.

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

<table><tr><td colspan="14">G10 10-Year Yield Forecasts</td></tr><tr><td></td><td>USD</td><td>DEM</td><td>FRA</td><td>ITA</td><td>ESP</td><td>GBP</td><td>JPY</td><td>CAD</td><td>CHF</td><td>SEK</td><td>NOK</td><td>AUD</td><td>NZD</td></tr><tr><td>Spot</td><td>4.45</td><td>2.96</td><td>3.57</td><td>3.67</td><td>3.37</td><td>4.81</td><td>2.67</td><td>3.41</td><td>0.41</td><td>2.80</td><td>4.35</td><td>4.83</td><td>4.51</td></tr><tr><td>2Q26</td><td>4.30</td><td>2.90</td><td>3.65</td><td>3.70</td><td>3.45</td><td>4.65</td><td>2.50</td><td>3.45</td><td>0.30</td><td>3.15</td><td>4.10</td><td>4.85</td><td>4.50</td></tr><tr><td>3Q26</td><td>4.20</td

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
