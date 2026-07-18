你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

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
GLOBAL RATES TRADER

June's cooler inflation data has brought some reprieve to hawkish risks in the US. With Fed officials signaling a clear focus on the price side of the mandate, however, continued erosion in hike pricing requires further accumulation of quieting inflation news under a stable labor market baseline. Meanwhile, the relative stickiness in long-end yields makes sense given reduced cyclical risks and ongoing AI investment, so the mix of risks facing the US curve continues to argue for anchoring longs in 5s. Hawkish risks are now well-priced by both European and UK front-ends, although upside risks to gas prices may prevent relief in the near term. Nonetheless, we expect to see front-end relief and steeper curves to end-2026. Redirecting Japanese savings towards domestic assets and JGBs via GPIF and NISA may see pension and retail categories increasing JGB allocation, but apart from modest support to long-end spreads we think macro conditions will determine JGB yields, not flows.

## United States and Canada

Inflation grants a reprieve. A stable labor market has kept Fed officials firmly focused on the inflation side of the mandate, with recent communication suggesting dwindling patience to explain away further target overshoots. For one month, however, the data appears to have delivered a reprieve, with our economists expecting an 18bp monthly core PCE print for June following the week's inflation reports. With a year-on-year core PCE rate that is still solidly above $3\%$ , however, we think continued erosion of hike risk relies on further accumulation of benign inflation news. In the near term, the Fed's pre-meeting blackout and a sparser data calendar should limit scope for hike pricing to compress meaningfully; given the week's compression and volume of data to come before the September meeting, we think very front-end paid/steepening positions are a reasonable hedge to near-term energy upside. We expect longer-term yields to continue to lag in rallies, with the combination of cyclical resilience and the investment backdrop factors we continue to think should keep long-end yields comparatively sticky. Despite pockets of belly underperformance in the oil-driven move higher in yields, we maintain our preference for anchoring longs in the 5y part of the curve given greater scope for 2s5s flattening on inflation upside and stickier long-end forwards in rallies.

■ Mixed signals for US traded inflation. Traded inflation has been caught

George Cole  
+44(20)7552-1214 |  
george.cole@gs.com  
GS International

William Marshall
+1(212)357-0413 |
william.c.marshall@gs.com
GS & Co. LLC

Simon Freycenet
+44(20)7774-5017 |
simon.freycenet@gs.com
GS Bank Europe SE - Paris Branch

Isabella Rosenberg
+1(212)357-7628 |
isabella.rosenberg@gs.com
GS & Co. LLC

Friedrich Schaper
+1(917)343-3214 |
friedrich.schaper@gs.com
GS & Co. LLC

Loic Mathys
+44(20)7051-1664 |
loic.mathys@gs.com
GS International

between competing forces this week, with rising oil prices on one hand and hawkish Fedspeak plus the benign June CPI report on the other. Our updated macro valuation framework puts longer-term inflation forwards on the cheap side of fair. We suspect this reflects the market's perception of a more hawkish Fed following the June meeting—supported by Governor Waller's comments this week—and choppier price action in risk assets. That said, 1y1y and 2y2y, have traded somewhat rich, reflecting greater sensitivity to higher oil prices that longer-term forwards have been more immune to (Exhibit 1). Despite slightly cheap longer-term forwards, we do not think that traded inflation is a compelling outright long currently—our economists' baseline is for a softer-than-priced 12-to-18 month ahead inflation, and any upside inflation surprises are likely to be met with higher real rates without a dovish shift in the Fed's messaging.

Exhibit 1: Longer-term inflation forwards screen modestly cheap relative to fundamentals  
![](images/92ccb8bc455ea207d45d8c0d12d15f71a8edf2f4135a0f839264e17509d708b7.jpg)  
Source: GS Global Investment Research, GS FICC and Equities  
Exhibit 2: Greater long-end credit issuance tends to correspond to softer UST stripping activity y/y % change in UST bonds held in stripped form vs change in Bloomberg US Corporate 20y+ amount outstanding

![](images/adb7c7235dda73bbd16b038b4025c474a2d9de14d78173f6accc01f8130e0df0.jpg)  
Source: GS Global Investment Research, Bloomberg

Halftime check-in for Treasury demand—still benign, but pockets to watch. While several categories have lagged our initial expectations for Treasury demand so far this year, we still view the outlook as generally benign though there are clearer questions around absorption for the second half. Our baseline is for \$684bn net bill supply and \$605bn net coupon supply in 2H26, which we expect to be absorbed by a mix of buyers: we expect the Fed to buy an additional \$130-140bn in bills through year-end, and money funds to deploy future AUM growth, supported by elevated front-end rates and potentially more risk asset volatility, into repo and bills, as supply picks up after a seasonal lull. Increased long-end corporate supply may erode certain sources of Treasury demand—we’ll be attentive to stripping activity here (Exhibit 2)—though we do not think this has had an outsized effect on long-end valuations compared to macro drivers. Lower foreign official buying likely reflects the strength in USD, not a structural shift in demand patterns; foreign private buying has remained a steady source of net demand throughout the year. Lastly, while commercial bank buying has not yet clearly shown an acceleration from regulatory reforms, we think greater intermediation capacity should support absorption moving forward.

Rising bill issuance to anchor repo rates higher in the range. The July ramp up in bill supply has helped to lift short-term funding costs to the middle of the Fed's target range. We have viewed easier funding conditions as reflecting a mix of constrained bill supply due to seasonal patterns and Fed buying, continued growth in money funds assets, and signs of a moderation in funding demand from levered investors. Several factors point to a shifting balance, however. While the broader trend in money fund AUM remains positive and the recent WAM reduction has held, 1-month bills cheapened versus OIS alongside larger auction sizes and a drop in MMF AUM on the week. Leveraged funds' short position in Treasury futures also stopped declining in recent weeks, which may mean a more stable appetite for repo funding moving forward. The drop in the TGA to its lowest levels since May—which in part likely reflected the impact of tariff refund payments on Treasury's cashflows—was also a factor behind the easy early month conditions; rising bill issuance should help rebuild the TGA closer to steady state. While bill supply absorption in the context of shorter money fund WAM may lead to pockets of pressure and a flatter bills-OIS curve, our baseline is for repo rates to remain anchored a bit below IORB, supported in part by a more cautious approach to RMPs through the September tax season.

BoC policy appropriate, as normalization steepens the curve and tightens USD-CAD spreads. The BoC kept rates on hold this week, returning to the pre-war guidance that policy is “appropriate,” in line with expectations. The assessment that there was “slightly more excess supply than anticipated,” and the removal of the reference to the potential for consecutive hikes were modestly dovish developments, which were balanced by the acknowledgment of signs of a pickup in activity. We think this points to policy remaining at the bottom end of the neutral range, which should continue to support the recovery in activity. But with the more severe trade risks curtailed for now, we think markets will continue to price an eventual return to normal, translating into a steeper curve over time led by intermediate and longer-term forwards. As activity headwinds and supply constraints fade and accommodative policy and tailwinds from the AI build-out support the forward outlook, we see scope for relative underperformance of the belly of the CAD curve versus the US. With the USD-CAD 5y spread at its widest outside last year’s trade war, while the growth outlook narrower, we think there is room for that gap to tighten (Exhibit 3).

Exhibit 5: Euro area bank sovereign bond holdings increasing towards highs
Euro area MFI general government holdings as share of total assets  
Exhibit 3: While the difference in growth expectations has narrowed, USD-CAD belly rates have diverged again  
![](images/f5b79d80fd0cd79047d6b20a7bd583f692f47fa197d42ba1eea480cc74d83a79.jpg)  
Source: GS Global Investment Research, GS FICC and Equities, Consensus Economics

## Europe

EUR 1y1y under pressure, but hawkish risks well-priced. Renewed concerns about upside risks to global energy and European gas prices have driven yields higher in recent weeks. Since the 2 July low, 1y1y has repriced over 30bp, and now prices a ‘higher-for-longer’ path for the ECB. With almost two additional hikes priced for 2026, it is notable to see hike pricing in 2027 increasing alongside higher 2026 pricing. Last week we had thought 1y1y rates were already too elevated, and this remains the case vs our forecasts. We think 1y1y-2y2y will eventually steepen, but ongoing upside risks to gas prices suggest more balanced tactical risk in the near term, especially as 1y1y does not look dislocated vs 1y1y traded HICP (Exhibit 4). Next week’s ECB meeting should offer few surprises, with the GC on hold and offering limited guidance – although soft signals towards a September hike are possible. Further out the curve, we continue to think that 10y Bund yields will end the year near 3%, and with the ECB on hold this should result in steeper core curves.

Exhibit 4: 1y1y OIS is trading in line with 1y1y HICP  
![](images/c274bc39592042c507f348e89258e027c18fac8b21841db8cc0d7b140be5c90e.jpg)  
Source: GS Global Investment Research, GS FICC and Equities

![](images/3b9957e68e1449ab4a41f375ee3e10c3fd487e7c84c1a79e01256c31a72282fc.jpg)  
Source: GS Global Investment Research, ECB, Haver Analytics

■ Potential leverage ratio relief for EGB swap spreads. Reports suggest the EU is considering loosening leverage ratio requirements in the Euro area, which should provide incremental support for EGBs on asset swaps. Our Banks research team estimate that this could boost overall balance sheet capacity by EUR180bn. At current levels of European bank government bond holdings (\~5%, Exhibit 5), this would translate into EUR9bn of additional direct bond ownership, with further room for the broader financial system to absorb government bonds, among other assets. Additionally, they note that a reduction in the leverage ratio provides incremental support for government bond ownership, which is leverage-intense but has limited impact on risk-weighted asset requirements. Although the direct estimate is small (less than 1% on government bond free-float), this suggests modest support for EGBs on asset swaps. The rise in rates volatility and rate hike risk from higher gas prices is a near-term headwind, but with a hawkish ECB path already well-priced, we see positive risk-reward for sovereign carry and EGBs on asset swaps.

Recent data benign, but energy risks remain ahead of BoE MPC. The UK curve has remained sensitive to energy prices, with Z7 bearing the brunt of repricing since the beginning of July, as we have seen in Europe, suggesting that the market is increasingly treating renewed energy pressure as a risk that could persist into next year. Next week's CPI is stale to recent energy moves, but may help the market assess risks around the pass-through of the initial energy shock from March. Historically, misses of 20bp or more have been needed to generate moves beyond one daily standard deviation (around 6-7bp), with the largest response in 5y rates (Exhibit 6). Despite symmetric risks around the inflation number itself, hawkish risks for the BoE meeting look well-priced in the front-end. Near-term political uncertainty may diminish as the leadership transition becomes formalised next week, but that does not resolve the underlying fiscal tension between spending ambitions, limited headroom and constrained tax options. With greater clarity on the policy agenda likely to emerge only gradually over the summer, and the Autumn Budget still the natural focal point for fiscal risk, we expect UK term premium to remain sticky even if weaker inflation allows the front end and belly to rally. As a result, we continue to recommend GBP 2s10s steepeners, with the BoE likely remaining more dovish than market pricing, and fiscal uncertainty limiting the scope for sustained long-end outperformance.

## Exhibit 6: Large UK inflation surprises have historically produced outsized moves in the belly

Volatility-adjusted average change in UK 2y, 5y and 10y rates conditional on headline CPI surprises

![](images/5628861ea287df7fd596881a9bf914564cdea745b68f40c7638c5d5a018d1098.jpg)  
Source: GS Global Investment Research, GS FICC and Equities, Bloomberg

## Latest Thematic Research:

Global Markets Analyst: Updating Our G10 Term Premium Estimates — Still High — 19 June 2026

Euro Area Sovereign Credit Monitor: EU Bonds — Still Deepening — 12 June 2026

Global Markets Analyst: Revisiting the Outlook for the Fed's Balance Sheet — 21 May 2026

Global Rates Notes: US Treasury Valuations and Requirements for a Yield Reversal — 20 May 2026

Global Markets Analyst: UK T-bills: Not A Magic Bullet For Gilts — 11 May 2026

## Latest Global Markets Dailies:

Halftime Check-In For Treasury Demand — 16 July 2026

Mixed Signals for US Traded Inflation — 13 July 2026

Euro Area Money Markets Closer to Crunch Time — 8 July 2026

Solvency II Review to Reinforce Benign Sovereign Credit Risk Backdrop — 23 June 2026

G10 Rates Views—Lower Vol, Not Yields — 22 June 2026

The authors would like to thank Dario Scordamaglia for his contribution to this report. Dario is an intern on the Markets team.

## Forecasts

G10 10y yield forecast

<table><tr><td colspan="14">G10 10-Year Yield Forecasts</td></tr><tr><td></td><td>USD</td><td>DEM</td><td>FRA</td><td>ITA</td><td>ESP</td><td>GBP</td><td>JPY</td><td>CAD</td><td>CHF</td><td>SEK</td><td>NOK</td><td>AUD</td><td>NZD</td></tr><tr><td>Spot</td><td>4.53</td><td>3.12</td><td>3.92</td><td>3.93</td><td>3.58</td><td>4.93</td><td>2.70</td><td>3.53</td><td>0.44</td><td>2.92</td><td>4.37</td><td>4.90</td><td>4.65</td></tr><tr><td>3Q26</td><td>4.45</td><td>2.95</td><td>3.60</td><td>3.65</td><td>3.35</td><td>4.60</td><td>2.50</td><td>3.50</td><td>0.40</td><td>3.20</td><td>4.00</td><td>4.75</td><td>4.50</td></tr><tr><td>4Q26</td><td>4.40</td><td>3.00</td><td>3.70</td><td>3.75</td><td>3.45</td><td>4.50</td><td>2.50</td><td>3.50</td><td>0.50</td><td>3.25</td><td>4.00</td><td>4.70</td><td>4.50</td></tr><tr><td>1Q27</td><td>4.35</td><td>3.00</td><td>3.75</td><td>3.80</td><td>3.50</td><td>4.50</td><td>2.45</td><td>3.50</td><td>0.50</td><td>3.25</td><td>4.00</td><td>4.60</td><td>4.50</td></tr><tr><td>2Q27</td><td>4.30</td><td>3.00</td><td>3.75</td><td>3.85</td><td>3.55</td><td>4.40</td><td>2.40</td><td>3.50</td><td>0.50</td><td>3.25</td><td>4.00</td><td>4.50</td><td>4.50</td></tr><tr><td>3Q27</td><td>4.25</td><td>3.00</td><td>3.75</td><td>3.90</td><td>3.60</td><td>4.40</td><td>2.30</td><td>3.50</td><td>0.50</td><td>3.25</td><td>4.00</td><td>4.50</td><td>4.50</td></tr><tr><td>4Q27</td><td>4.25</td><td>3.00</td><td>3.75</td><td>3.90</td><td>3.60</td><td>4.35</td><td>2.25</td><td>3.50</td><td>0.50</td><td>3.25</td><td>4.00</td><td>4.50</td><td>4.50</td></tr><tr><td>1Q28</td><td>4.25</td><td>3.00</td><td>3.75<

[中间内容因长度限制已省略]

attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
