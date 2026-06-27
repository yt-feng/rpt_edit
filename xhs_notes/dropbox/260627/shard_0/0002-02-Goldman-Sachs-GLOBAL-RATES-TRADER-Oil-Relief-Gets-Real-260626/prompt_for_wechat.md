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
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`GS`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
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
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
GLOBAL RATES TRADER

Oil Relief Gets Real

The hawkish US front-end repricing has proven resilient despite the ongoing decline in energy prices. But the reduction in inflation risk has helped to restore nominal duration's role as a risk asset hedge. We think there is more favorable asymmetry to longs anchored slightly out from the very front-end of the US (e.g. 1y1y or 2y1y) curve given the likely front-loading of hike risk in response to hotter data. That said, we think milder job growth and inflation data over the coming months can see end-26 pricing consolidate towards an on-hold baseline. European rates should remain in a relatively tight range as September ECB pricing remains between 0-1 hike. Lower rates vol and growth risks should favour front-end EGB spreads, with the upcoming Solvency II review a tailwind for long-end sovereign credit. We think the hurdle for further Gilt term premium compression is high, but expect UK front-end rates to continue to outperform. The continued underperformance of Japan duration versus global peers reflects unresolved domestic risks that we think will likely maintain pressure on the belly of the curve despite cheap valuations.

## United States and Canada

On slightly firmer ground. Oil relief has curtailed inflation upside and left US rates better positioned as a risk asset hedge with inflation and growth risks co-moving rather than at odds with each other. Nearer-term real rates have started to participate in rallies again, front-end skew has rotated back towards receivers, and Fed pricing has moderated from the hawkish extremes (Exhibit 1). Given the information in hand and a Fed signal that, while mindful of inflation risk, did not as a whole imply a sense of urgency to hike, we think July pricing should decay absent clearly strong data. Further, while the focus coming out of the June FOMC was on price stability, we think it would be wrong to downgrade the significance of labor market data, particularly given the progress lower in oil prices. Acknowledging two-way risks to front-end pricing and the likelihood that near-term hike risk remains somewhat sticky given last week's signal and reaction function uncertainty, we think there's a more favorable near-term asymmetry to being long further out (e.g. 1y1y or 2y1y) as firmer data likely front-load hike risks alongside stickier forwards. Under our economists' baseline for near-term data, we think the probability mass for Z6 should build around an on-hold outcome, with our bias still to anchor longs further out on the forward curve or around the 5y point of the spot curve.

George Cole  
+44(20)7552-1214 |  
george.cole@gs.com  
GS International

William Marshall +1(212)357-0413 | william.c.marshall@gs.com GS & Co. LLC

Simon Freycenet  
+44(20)7774-5017 | simon.freycenet@gs.com GS Bank Europe SE - Paris Branch

Isabella Rosenberg +1(212)357-7628 | isabella.rosenberg@gs.com GS & Co. LLC

Friedrich Schaper +1(917)343-3214 | friedrich.schaper@gs.com GS & Co. LLC

Loic Mathys  
+44(20)7051-1664 |  
loic.mathys@gs.com  
GS International

Exhibit 1: Front-end skew has rotated back towards receivers as Fed pricing has moderated from the hawkish extremes

![](images/33088e82ff9fa0bdc5e8b3fc3c7e48840e4420f39a5ab780a65c7eeef5d0b5ca.jpg)  
Source: GS FICC and Equities, GS Global Investment Research

Exhibit 2: Current front-end steepness tends to see vol undershoot what is implied by macro fundamentals 2y1y/1y steepness vs residual vs macro fair value model  
![](images/7962caa13787d3c3b3b705b5a00a5f9af0de7e8bfbddba7319304391d84a7749.jpg)  
Source: GS Global Investment Research, GS FICC and Equities

\- Higher vol floor, flatter curve. While off the highs and towards the lower end of our fair value range, implied vol has settled at a higher level than before the conflict, with risk premium emerging at shorter tails. However, current levels of front-end steepness can see implied vol underperform macro fundamentals to an even greater degree (Exhibit 2), suggesting some scope for vol to moderate further. We think this setup can support returns to vol selling, especially if moderating hiring and inflation data lead the hawkish policy momentum to decay gradually (as has been the case in recent past). Overall, the reduction in supply-side risks and macro uncertainty should eventually reduce macro volatility and reduce the vol premium further. That said, we see some differentiation along the surface. We continue to think that the ongoing shift from macro to policy uncertainty should sustain a flatter tail curve, as uncertainty shifts to Fed's reaction function. At this point valuations along the surface suggest this is already somewhat reflected, with vol on 1y tails rich to both the macro and in the context of our vol surface PCA, while through the same lens implied vol on belly tenors are low in comparison to the wings.

## - Easier funding conditions point to supportive supply/demand dynamics.

Treasury funding conditions remain broadly accommodative, driven by a favorable balance between cash lending, primarily from money funds, paired with more subdued demand for funding from levered investors. On the supply side, money fund AUM has continued to grow, supported by a flatter Treasury curve and softer risk asset performance in June. Money funds' weighted-average maturity has shortened as well, with tightening in 1m Bills-OIS reflecting greater money fund demand for shorter-term assets. Meanwhile, appetite for funding has declined amid compressed Treasury futures basis opportunities, which has shown up in dwindling levered fund shorts (Exhibit 3). The benign backdrop for funding suggests the market has a comfortable buffer to absorb a shift back to more elevated cash demand without incurring meaningful upward pressure on funding costs. Quarter-end dynamics are a likely near-term source of temporary upward pressure on repo rates. While the medium-term prospects for balance sheet policy are a spot of uncertainty, we think the easier backdrop will lead to a slower pace of RMPs over the coming months.

Exhibit 3: Appetite for funding has declined amid compressed Treasury futures bases, evidenced by dwindling levered fund shorts  
![](images/6e5f05668f2e0408105d46f7f465e605d91bd69b1618d5fc6a4f9fa05af4f9a9.jpg)  
Source: CFTC, Haver Analytics, GS Global Investment Research

Exhibit 4: With limited pass-through from higher oil prices, CAD rates have more room to fall  
![](images/ab171ff2e1c6bb1b4ab6cad6cf2ef7394f5ebc19f3cc2bdc01fccc8450ce335b.jpg)  
Source: GS Global Investment Research, GS FICC and Equities

Wider spreads have staying power. We think swap spreads can continue to trade wide to the broader UST supply backdrop in the near term, supported by a decline in macro (if not reaction function) uncertainty and constructive demand picture. While bank buying has been somewhat uneven recently, we expect demand dynamics to remain generally supportive; meanwhile, the foreign official sector has scaled back its net selling of USTs with the stabilization in the Dollar. Alongside those benign spot considerations, uncertainty over the Fed's balance sheet policy is a potential medium-term risk. If the Fed begins to have a more serious debate about alternatives to ample reserves framework, we expect it would correspond to increased risk premium in belly and long-end swap spreads compared to the front-end (in part reflecting the likelihood that any concrete shift would take time and therefore more relevant over time). We still think shorter-term swap spreads offer value from a carry perspective, with valuations about fair. We have preferred to express this in 3y swap spreads, which we think should be more insulated from balance sheet risk while offering appealing carry-to-vol versus the rest of the curve.

Still room for CAD front end compression. The decline in oil prices has compressed hike premium for the BoC for this year to about 12bp alongside a generalized reset across the forward curve. Given still limited spillover risks from energy prices to other inflation categories, and underlying softness in activity, we think that the remaining hike premium through year-end should decay. Lower energy prices can allow focus to turn towards potential dovish risks to the outlook (Exhibit 4). The apparent likelihood that the July 1 USMCA deadline will pass without agreement should keep trade uncertainty elevated and lead to ongoing headline risks around the annual reviews. We see some potential for that to reintroduce weight on the risk of further easing (even if our economists expect BoC to remain on hold), given BoC's characterization of trade risks, and we can also see front-end yields decline towards pre-conflict levels.

## Europe

\- European rates settle in as tails decline further. Energy price relief has extended further this week as shipping flows through the Strait of Hormuz increase. We continue to expect this to reduce European rates volatility rather than yield levels, extending the decoupling that followed the April ceasefire. Because the ECB path and European rates volatility are more narrowly driven by energy uncertainty compared with a broader range of macro factors in the US, we also expect European rates vol to underperform the US. ECB commentary emphasises the fragility of the peace agreement and points to ongoing concern around inflation persistence, and our economists continue to forecast another hike in September. We don't expect a meaningful rally from here, with the market now trading below our 3% end-2026 Bund yield forecast, but, given the hawkish bias of the ECB, we think 5y rates are likely to outperform on the curve, especially should hikes coincide with further inflationary relief.

Solvency II review a tailwind to sovereign credit. The upcoming implementation of the Solvency II review – by 31 January 2027 – aims to steer insurance companies’ portfolios towards the real economy, which implies a rising marginal allocation to equities over time. But we think other elements of the review will be a net positive for sovereign credit. In particular, a revised methodology for risk-free rates will make long-dated discount rates more sensitive to shifts in market rates and is likely to increase interest rate hedging past the 20y point of the curve. Revisions to the Volatility Adjustment (VA) mechanism and more favourable correlation parameters between interest rates and credit spreads should also support insurers’ ability to bear credit risk. We expect this to support insurer demand for long-dated government bonds, adding to the already-favourable backdrop for sovereign credit as rates vol and growth risks decline.

\- Watching funding spillovers to Europe. The market focus on equity supply through IPOs, primarily in the US but also to a lesser extent in Europe, has seen equity funding spreads increase. This period is analogous to the second half of 2024, where building long positions in equities had generated pressures on funding markets. Back then, we saw evidence that Bund spread cheapening had run ahead of fundamentals, opening a residual of about 15bp against our fair value estimate over a period of 6 months, suggesting the increase in funding costs from equity markets had spilled over to fixed income markets (Exhibit 5). The macro and market context is different now, with ECB QT no longer accelerating, and spreads generally cheaper and global curves steeper. But we think this is a risk worth watching in coming months as QT continues to drain excess liquidity in the Euro area. We expect the liquidity backdrop to remain abundant into 2027, consistent with the still-low levels of bank borrowing at the ECB's facilities (\~EUR15bn under the MRO). But funding pressures are one potential risk to the generally favourable backdrop for carry described above.

Exhibit 5: In the past, sharp moves in equity funding have spilled over to Bund spreads
Euro STOXX funding spread to OIS of 2nd nearest future

![](images/afba18ff4b6e607fb0e5fadb79747b3f8bc48d8811a7d6a2af102a774107aaed.jpg)  
Source: GS Global Investment Research, GS FICC and Equities

Exhibit 6: The rally in 10y Gilts has been mostly driven by term premium compression

Change in 10y UK term premium and rates expectations (yield curve-only model)

![](images/e9f3f6f8816bf5deb40c4621f9877377f84a8c2555a47f9606ff0c4789cd3ed9.jpg)  
Source: GS Global Investment Research

Gilt relief likely to slow, prefer GBP steepeners. The ongoing decline in oil prices following the US-Iran deal remains a tailwind for UK rates, reducing headline inflation risk at the same time as underlying price pressures are looking more benign. We expect markets to become increasingly confident about a BoE holding through 2026, and the erosion of the remaining hike premium in the UK front-end may now slow given how far the market has rallied. At the same time, most of the decline in 10y Gilt yields in recent months has been due to term premium compression (Exhibit 6). With Andy Burnham likely to be the next UK Prime Minister, we think the market will retain some premium in coming months as focus turns to the Autumn budget. In the recent rally, front-end nominals have rallied mostly through lower inflation, while the 5y5y move has been largely real-rate-led, with forward inflation only modestly lower. In contrast to the Euro area and the US, where risk-reward is likely better in the belly of the curve, we instead lean towards steepening in the UK, with outperformance of the 1y1y part of the curve as front-end real rates eventually normalise lower.

## Australia and New Zealand

Balanced risks around RBA pricing. Market pricing for the RBA has moderated to pricing less than 50% of a hike through the year-end peak in the curve. While our economists think underlying labor market conditions are softening at an orderly and gradual pace, the latest labor force report left the unemployment rate below both the level where the Governor described the labor market as “a bit tight” as well as the RBA’s estimate for NAIRU. Our economists continue to lean towards the RBA delivering one additional hike this year, but falling oil prices likely make that outcome contingent on a sufficiently firm inflation print outside oil-affected categories. That leaves the risks around near-term meetings more balanced in our view, with risk-reward still better to setting longs further out the curve. Whether or not the RBA delivers an additional hike, we see scope for the market to price greater risk of cuts on a 1-to-2y forward horizon as evidence of weaker growth and softer inflation

accumulate. We recommend to receive 2y1y OIS vs pay August RBA (Entry: -18bp, Target: -35bp, Stop: -10bp).

## Latest Thematic Research:

Global Markets Analyst: Updating Our G10 Term Premium Estimates — Still High — 19 June 2026

Euro Area Sovereign Credit Monitor: EU Bonds — Still Deepening — 12 June 2026

Global Markets Analyst: Revisiting the Outlook for the Fed's Balance Sheet — 21 May 2026

Global Rates Notes: US Treasury Valuations and Requirements for a Yield Reversal — 20 May 2026

Global Markets Analyst: UK T-bills: Not A Magic Bullet For Gilts — 11 May 2026

## Latest Global Markets Dailies:

Solvency II Review to Reinforce Benign Sovereign Credit Risk Backdrop — 23 June 2026

G10 Rates Views—Lower Vol, Not Yields — 22 June 2026

Fed Communication And Rates Volatility — 10 June 2026

The Hedge Value Of Rate Receivers — 28 May 2026

The Energy Shock Impact on Foreign Official Treasury Demand — 27 May 2026

## Forecasts

G10 10y yield forecast

<table><tr><td colspan="14">G10 10-Year Yield Forecasts</td></tr><tr><td></td><td>USD</td><td>DEM</td><td>FRA</td><td>ITA</td><td>ESP</td><td>GBP</td><td>JPY</td><td>CAD</td><td>CHF</td><td>SEK</td><td>NOK</td><td>AUD</td><td>NZD</td></tr><tr><td>Spot</td><td>4.37</td><td>2.85</td><td>3.63</td><td>3.58</td><td>3.34</td><td>4.69</td><td>2.63</td><td>3.36</td><td>0.27</td><td>2.65</td><td>4.22</td><td>4.73</td><td>4.34</td></tr><tr><td>2Q26</td><td>4.50</td><td>2.90</td><td>3.55</td><td>3.60</td><td>3.30</td><td>4.75</td><td>2.50</td><td>3.45</td><td>0.30</td><td>3.15</td><td>4.10</td><td>4.85</td><td>4.50</td></tr><tr><td>3Q26</td><td>4.45</td><td>2.95</td><td>3.60</td><td>3.65</td><td>3.35</td><td>4.60</td><td>2.50</td><td>3.50</td><td>0.40</td><td>3.20</td><td>4.00</td><td>4.75</td><td>4.50</td></tr><tr><td>4Q26</td><td>4.40</td><td>3.00</td><td>3.70</td><td>3.75</td><td>3.45</td><td>4.50</td><td>2.50</td><td>3.50</td><td>0.50</td><td>3.25</td><td>4.00</td><td>4.70</td><td>4.50</td></tr><tr><td>1Q27</td><td>4.35</td><td>3.00</td><td>3.75</td><td>3.80</td><td>3.50</td><td>4.50</td><td>2.45</td><td>3.50</td><td>0.50</td><td>3.25</td><td>4.00</td><td>4.60</td><td>4.50</td></tr><tr><td>2Q27</td><td>4.30</td><td>3.00</td><td>3.75</td><td>3.85</td><td>3.55</td><td>4.40</td><td>2.40</td><td>3.50</td><td>0.50</td><td>3.25</td><td>4.00</td><td>4.50</td><td>4.50</td></tr><tr><td>3Q27</td><td>4.25</td><td>3.00</td><td>3.75</td><td>3.90</td><td>3.60</td><td>4.40</td><td>2.30</td><td>3.50</td><td>0.50</td><td>3.25</td><td>4.00</td><td>4.50</td><td>4.50</td></tr><tr><td>4Q27</td><td>4.25</td><td>3.00</td><td>3.75</td><td>3.90</td><td>3.60</td><td>4.35</td><td>2.25</td><td>3.50</td><td>0.50</td><td>3.25</td><td>4.00</td><td>4.50</td><td>4.50</td></tr></table>

<table><tr><td colspan="14">Deviation from Forwards</td></tr><tr><td></td><td>USD</td><td>DEM</td><td>FRA</td><td>ITA</td><td>ESP</td><td>GBP</td><td>JPY</td><td>CAD</td><td>CHF</td><td>SEK</td><td>NOK</td><td>AUD</td><td>NZD</td></tr><tr><td>2Q26</td><td>0.12</td><td>0.05</td><td>-0.08</td><td>0.01</td><td>-0.04</td><td>0.05</td><td>-0.12</td><td>0.06</td><td>0.06</td><td>0.52</td><td>-0.11</td><td>0.13</td><td>0.14</td></tr><tr><td>3Q26</td><td>0.01</td><td>0.02</td><td>-0.05</td><td>-0.05</td><td>-0.01</td><td>-0.22</td><td>-0.21</td><td>0.07</td><td>0.10</td><td>0.55</td><td>-0.19</td><td>0.00</td><td>0.07</td></tr><tr><td>4Q26</td><td>-0.07</td><td>0.04</td><td>0.00</td><td>-0.02</td><td>0.04</td><td>-0.37</td><td>-0.28</td><td>0.02</td><td>0.18</td><td>0.57</td><td>-0.18</td><td>-0.08</td><td>0.00</td></tr><tr><td>1Q27</td><td>-0.16</td><td>0.01</td><td>-0.01</td><td>-0.02</td><td>0.04</td><td>-0.41</td><td>-0.40</td><td>-0.01</td><td>0.17</td><td>0.54</td><td>-0.16</td><td>-0.20</td><td>-0.07</td></tr></table>

Source: GS Global Investment Research

G4 Curve Forecast  
![](images/3150e7fb7826c4fa6ddaa50fcd7aa93c7831912cc96a6a7

[中间内容因长度限制已省略]

e have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
