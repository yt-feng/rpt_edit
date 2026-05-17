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

# Rates Running Out of Patience

Supply-side volatility and uncertainty around the conflict continue to challenge global duration's usefulness. The introduction of some inflation risk into the UST curve—a feature that was absent earlier in the shock—and optimism priced into macro markets improve the value of duration as a medium-term hedge against the deeper downside tails. But with any near-term rally likely gradual in a benign deescalation scenario, or reliant first on a more adverse outcome for energy prices from the conflict that reignites growth concerns, we continue to see value to structures that limit downside in further selloffs. European front-end rates remain under pressure as no news on Strait of Hormuz flows weakens the case for longs. While we continue to recommend long EGBs vs OIS, we are tightening stops after recent spread tightening. Gilt risk premium emerged amid the late week global selloff after relative stability during the earlier increase in political uncertainty, potentially reflecting the already-elevated levels of UK risk premium. We think inflation and monetary policy outcomes will have the decisive impact on Gilt yields this year, with lower 10y yields likely to be driven by a lower policy path—for this reason we continue to favor front-end longs vs belly underweights.

# United States and Canada

Peer pressures. The break above 4.5% 10y and 5.0% 30y US yields has come against a backdrop of higher yields globally, with UK, Japan, and German long-end yields trending steadily higher—compared to the last time UST 30y yields exceeded 5% in 3Q25, the average of UK, Japan, and German 30s has risen about 50bp (Exhibit 1). Our estimate of global spillovers suggests that the year-to-date selloff in USTs has largely reflected bearish shocks from the UK and Japan. We are hesitant to write off domestic impulses entirely though, as the pairing of growth optimism and inflation upside risks have converged to erode market conviction in the likelihood of Fed cuts—a building sense of on hold (or higher) for longer front-end yields should shift the perception of what level offers attractive value further out the curve as well. Instead, we would interpret the global nature of the bearish pressure as underscoring the near-term challenges to achieving lasting relief without a shift in the macro picture—despite idiosyncratic factors, the paths to a meaningful rally in the UK and Japan hinge primarily on outcomes that either restore conviction in the path towards lower policy rates (for the UK) or validate the gradual approach to tightening (for

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

Japan).

An uneasy introduction of value. Treasuries have been a poor diversifier since the end of February—the one-month rolling correlation between 10y UST yield changes and equity returns reached its most negative in multiple decades (Exhibit 2). Continued uncertainty around the Iran conflict and supply shock remains an impediment to nominal duration's ability to dampen day-to-day portfolio volatility, which can sustain greater risk premium in the short term. However, the broader trends of growth optimism priced into risk markets and clearer build-up of inflation risk premia along the yield curve (more below) improves the value proposition of Treasuries as a medium-term hedge. Given the possibility that it takes a more acute spike in energy prices to reopen growth worries in the short term, we think expressions that lean bullish while limiting exposure to additional selloffs are a prudent implementation for now and would look either for deeper selloffs that more durably challenge the risk asset trend, or credible relief and a return of energy flows as catalysts to add to long duration exposure.

Exhibit 1: 30y UST yields' renewed break of $5\%$ has come amid a sustained uptrend in global long-end yields
UST 30y yield vs avg of UK, German, Japan 30y yields   
![](images/73d3174615fc45d35ae847342187ecee93a66ee41d38d377110296da7500d21f.jpg)

<details>
<summary>line</summary>

| Date   | US 30y yield | Average 30y yield across UK, Germany, and Japan |
|--------|--------------|-----------------------------------------------|
| Jan-23 | 3.7          | 2.5                                           |
| Jul-23 | 4.0          | 2.8                                           |
| Jan-24 | 5.1          | 3.3                                           |
| Jul-24 | 4.5          | 3.0                                           |
| Jan-25 | 4.9          | 3.5                                           |
| Jul-25 | 5.0          | 3.9                                           |
| Jan-26 | 5.1          | 4.4                                           |
</details>

Source: GS FICC and Equities, GS Global Investment Research   
1m rolling correlation of 10y UST yield change and S&P 500 returns

Exhibit 2: Treasuries have been a poor portfolio diversifier since the start of the conflict

![](images/4db2ca7ff34ac6d0f41033b642d3d54dcc786170deb17dfa74b62fd7dfd5c8ac.jpg)

<details>
<summary>line</summary>

| Year | 1m rolling correlation of 10y UST yield and S&P 500 changes (%) |
|------|------------------------------------------------------------------------|
| 1996 | -80                                                                    |
| 1999 | -80                                                                    |
| 2002 | -80                                                                    |
| 2005 | -80                                                                    |
| 2008 | -80                                                                    |
| 2011 | -80                                                                    |
| 2014 | -80                                                                    |
| 2017 | -80                                                                    |
| 2020 | -80                                                                    |
| 2023 | -80                                                                    |
| 2026 | -80                                                                    |
</details>

Source: GS FICC and Equities, GS Global Investment Research

Easier funding costs lead stepdown in RMPs. The New York Fed announced a reduction in the pace of RMPs from \$25bn to \$10bn over the coming month, having slowed from \$40bn a month earlier. We previously argued that there was scope for a further reduction in the pace of purchases given recent funding market stability despite system-wide liquidity dipping to cycle lows relative to bank assets, and think the further easing in funding costs in recent weeks likely prompted the larger deceleration in RMPs. While the decline in overnight rates reflects a genuine moderation in the drivers of last year's funding volatility that we think is consistent with a leftward shift in the reserve demand curve, temporary factors have contributed to the recent decline in overnight rates. Net negative Treasury bill issuance alongside Fed RMPs took bill supply to a trough in early May, and although tax payments pulled liquidity from the system temporarily, the nearly \$300bn decline in the TGA from the April peak has boosted reserves, leaving short-end collateral supply at a local low and system-wide liquidity around a local high. While those factors should moderate as bill issuance turns positive and the TGA rebuilds, assuming the Fed aims for triparty repo rates close to but modestly below IORB in the steady state, we think that RMPs could slow further. We estimate that reserves stabilizing modestly around 11% of bank assets should be consistent with TGCR averaging modestly below IORB; assuming both bank asset and currency grow with trend nominal GDP, we assume RMPs of \$5bn per month and remain there to 1Q27, at which point reserves should be a bit above 11% of bank assets (beyond then we assume a return to a more trend-like pace of about \$25bn/mo in balance sheet growth absent other shifts). We would not rule out a period of zero growth in reserves, but continue to think there is a high bar to a lasting return to runoff given growth in currency, bank assets, and the TGA, as well as uncertainty around precisely where the steep part of the demand curve sits and the risks that arise from more rapidly draining liquidity.

Inflation forwards catching up to oil, and AI costs. Having lagged oil prices during most of the early part of the conflict (likely for multiple reasons, see here and here), inflation forwards recently have caught up with the general reset higher in yields and front-end inflation pricing. While the economic rationale for pricing persistently higher inflation over the coming years on the current supply shock is weak, particularly given the labor market backdrop, a return of supply-side volatility and the sanguine growth tone in markets both argue for more risk premium through the inflation curve. Our commodities analysts have noted that storage drawdowns and demand destruction have partially buffered the positive impact to energy prices, but inventory drawdowns risk reaching limits around summer should the Hormuz disruption last beyond June, likely requiring higher prices to incentivize further demand destruction. We also saw the clearest evidence in US data so far that higher costs from the AI-buildout phase can push inflation up initially (our economists estimate roughly half a percentage point boost to PPI from AI, but see mainly measurement errors at play for core PCE), before the productivity gains can lead to disinflation eventually. But with inflation forwards less cheap following the repricing (Exhibit 4), we now see a less clear case for using inflation longs as a hedge, and view risks as more two-sided, given risks of a slight pullback from the anticipatory growth optimism.

BoC minutes confirm dovish bias; steeper 2s5s. Canadian yields reset higher with rates globally over the past week as the conflict and energy shock drags on. While global shifts remain a headwind to longs, we continue to expect a more dovish than priced BoC path given expected inflation follow through and a weaker labor market. Reinforcing our bias to a steeper curve, the BoC minutes this week again emphasized the “scope to be patient” and ability “to look through the shock.” We thought the most notable takeaway was the unambiguously dovish characterization of trade risks. We see scope for focus to return to downside growth risks as the USMCA deadline approaches, and for hike premium to decay provided inflation stays along the BoC’s forecasts. That said, while cross-market longs have been popular, we view levels as less compelling from here, and the recent pickup in open interest in CORRA futures suggests some positioning risk. Given the better insulation to still-higher oil prices we still prefer 2s5s steepeners over outright longs. On a more technical note,

CORRA recently printed lower again, following a pocket of pressure in April amid a local low in repo liquidity. But with a looming bond maturity that would drain about 11% of settlement balances, we think there is a case for BoC to provide greater clarity about the balance sheet approach; one possible shift could be to lay out the target range as a share of bank assets (which have grown about 4% since the 50-70bn target range was laid out last year) rather than a fixed level.

Exhibit 3: Bill supply should return to positive territory over the coming quarters, with the Fed also likely buying at a slower pace for now   
![](images/aa1f00b0ec4890d2c362a097a06dcf6597aaefdbedb21e3f27eb76a6102076ee.jpg)

<details>
<summary>bar_stacked</summary>

| Quarter | Net coupons ($bn) | Net Bills to Public ($bn) | Net Bills to Fed ($bn) |
|---------|-------------------|---------------------------|------------------------|
| Q1 2026 | 300               | 100                       | 150                    |
| Q2 2026 | 300               | -200                      | 100                    |
| Q3 2026 | 300               | 300                       | 100                    |
| Q4 2026 | 300               | 250                       | 100                    |
| Q1 2027 | 300               | 400                       | 100                    |
| Q2 2027 | 250               | -250                      | 150                    |
| Q3 2027 | 300               | 150                       | 150                    |
| Q4 2027 | 400               | 150                       | 150                    |
</details>

Assumes RMPs slow to \$5bn/mo from next month through 1Q27   
Source: GS Global Investment Research

Exhibit 4: Inflation forwards are no longer clearly lagging the change in oil prices   
![](images/efae88b7dd4c2ba416df32c2d943c57aa3e631ceaf8217942cdff917e02581ac.jpg)

<details>
<summary>line</summary>

| Date   | 2y2y Inflation | WTI (rhs) |
|--------|----------------|---------|
| Aug-20 | ~90            | ~0      |
| May-21 | ~60            | ~20     |
| Feb-22 | ~80            | ~40     |
| Nov-22 | ~-70           | ~-30    |
| Aug-23 | ~20            | ~10     |
| May-24 | ~30            | ~5      |
| Feb-25 | ~40            | ~10     |
| Nov-25 | ~30            | ~5      |
| Aug-26 | ~60            | ~70     |
</details>

Source: GS FICC and Equities, GS Global Investment Research

# Europe

No news puts a floor on EUR front-end rates. An absence of positive news on commodity flows via the SoH, tends to see EUR yields and HICP pricing drift higher. We have argued that forward HICP is now close to fair value (Exhibit 5), and this suggests the market is pricing a reasonable degree of passthrough from headline to core inflation. This makes risk reward more balanced in the European front-end, but Z6 and front-end curve slope will still be subject to shifts in oil prices. We still see a high hurdle for sUBStantial tightening (100bp or more) and so front-end volatility remains too high relative to the plausible policy outcomes. Next week's flash PMIs will offer clues to the growth outlook, but price components will also be a key part of the release. We continue to favour sovereign credit carry, and continue to recommend IT, ES, FR longs vs OIS. But following strong performance over the last month, we tighten stops to 0.32.

Exhibit 5: Forward HICP pricing reasonable degree of passthrough from headline to core inflation   
Change in 2y2y HICP and model fitted value since 1 Jan.   
![](images/bc42d736e464d6b12ce685b754986581d11cbc35b80f05b4fe4310af031a1001.jpg)

<details>
<summary>line</summary>

| Date   | Change in EUR 2y2y inflation fitted (bp) | Change in EUR 2y2y inflation |
|--------|------------------------------------------|-------------------------------|
| Jan-01 | 0                                        | 0                             |
| Jan-15 | 0                                        | 0                             |
| Jan-29 | 5                                        | 5                             |
| Feb-12 | 0                                        | 0                             |
| Feb-26 | -5                                       | -5                            |
| Mar-12 | 15                                       | 25                            |
| Mar-26 | 25                                       | 20                            |
| Apr-09 | 40                                       | 30                            |
| Apr-23 | 35                                       | 30                            |
| May-07 | 30                                       | 30                            |
</details>

Source: GS Global Investment Research, GS FICC and Equities, Haver Analytics

Exhibit 6: UK public interest cost fluctuations are large relative to headroom   
Vintage-to-vintage changes in the OBR's terminal debt interest forecast vs level of fiscal headroom   
![](images/8cb294f5964892f600d8f50d084089fab267e8ef9bfc0210d334d215099e29fc.jpg)

<details>
<summary>bar</summary>

| Month   | Δ Gross Debt Interest | Δ APF/QE | Fiscal Headroom (level) |
|---------|------------------------|----------|--------------------------|
| Oct-21  | 2                      | 3        | 25                       |
| Mar-22  | 4                      | 6        | 30                       |
| Nov-22  | 45                     | 10       | 9                        |
| Mar-23  | -3                     | -5       | 6                        |
| Nov-23  | 25                     | 0        | 13                       |
| Mar-24  | -8                     | -10      | 9                        |
| Oct-24  | 12                     | 0        | 10                       |
| Mar-25  | 9                      | 1        | 10                       |
| Nov-25  | 9                      | 0        | 22                       |
| Mar-26  | -3                     | 0        | 24                       |
</details>

Left bars show the change in end-of-horizon net debt interest, split into gross Gilt servicing and the BoE APF/QT adjustments.   
Source: GS Global Investment Research, BoE, OBR

Delayed reaction in Gilt premium. Despite an increase in political uncertainty on Monday and Tuesday, it took a global sell-off to shift Gilt risk premium higher late in the week. The UK curve steepened and our FX strategists' proxy for the political risk premium in Sterling — the gap between actual and GSBEER model-implied EUR/GBP performance — has risen. But overall, stress on UK assets has been more modest than in recent comparable periods. Our measure of the term premium also remains contained, and when we apply our spillover framework to the term premium, we find that the UK has not been contributing to upward pressure on global rates until very recently (Exhibit 7). This is consistent with the stability up until this week in Gilt swap spreads and 10s30s curve vs other G4 markets since last year's budget. Although political uncertainty will keep the market focused on fiscal policy, it is possible that some of the drivers of UK term premium, namely BoE QT and the rise in duration-adjusted free float

[中间内容因长度限制已省略]

e have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not

necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to sUBStantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
