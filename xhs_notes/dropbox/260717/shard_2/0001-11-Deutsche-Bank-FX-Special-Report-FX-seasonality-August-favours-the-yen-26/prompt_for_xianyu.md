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
# Foreign Exchange FX Special Report

## FX seasonality: August favours the yen

August is one of the strongest seasonal months in FX, with more than 20 currency pairs exhibiting significant seasonality based on daily closing prices.

Unlike December's flow-driven seasonality, August appears more closely associated with risk-off dynamics and information-sensitive trading behaviour.

\- Broad-based JPY outperformance is the dominant August theme, with the yen appreciating against both G10 and EM currencies and generally outperforming the USD. JPY gains are concentrated in the London–New York overlap, suggesting a role for investor positioning, changing expectations and ongoing price discovery.

High-beta, commodity and carry currencies such as ZAR, MXN, AUD and NZD tend to underperform, particularly against JPY. NZD is a notable exception, exhibiting persistent August weakness driven largely by Asian-session moves and potentially also linked to seasonal export dynamics.

Overall, JPY strength remains the most robust and persistent August seasonal pattern across both developed and emerging market currencies. The current focus on Japanese repatriation flows provides an interesting backdrop, coinciding with a period that has historically favoured yen strength.

Figure 1: USD/JPY exhibits strong seasonality in August  
![](images/b60b5a7b6db0d7d6541cd93bc94add1dfb2477f713aecdd1c1997147f659bf65.jpg)  
Source : DB, Bloomberg Finance LP, Refinitiv Tick History. Each line shows cumulative August returns by trading session. Session (London time): Asia 00:00–07:00, London morning (LDN) 07:00–12:00, Mixed LDN/NY 12:00–16:00, NY afternoon 16:00–20:00.

## Introduction

This report examines recurring seasonal patterns in FX markets during August. To identify seasonality, we test whether August returns are systematically different from those observed during the rest of the year. Specifically, for each currency pair, we regress returns on a dummy variable that takes the value one in August and zero otherwise. A statistically significant coefficient indicates that returns in August have historically been consistently higher or lower than in other months. We apply this framework to returns measured using London closing prices, returns across trading sessions, and intraday returns, allowing us to assess not only whether seasonality exists but also when during the trading day it tends to emerge.

The analysis proceeds in three steps. First, we establish the breadth of August seasonality across closing prices and intraday sessions. Second, we show that the strongest and most persistent pattern is broad-based JPY outperformance, particularly against high-beta and carry currencies. Third, we examine the main currency-specific exceptions, including ZAR and NZD, to distinguish the general August risk-off effect from more local or flow-related seasonal patterns.

## Strong seasonality in August: what stands out?

Historical patterns suggest that seasonality has been an important driver of FX returns in August, particularly when measured using daily closing prices rather than intraday moves. Figure 2 shows that more than 20 of the 60 currency pairs in our sample exhibit statistically significant August seasonality based on daily closing prices, compared with around 15 when returns are measured across time zones Figure 3). While the breadth of August seasonality in daily prices is similar to that observed in December, the intraday effect is less pronounced: more than 30 currency pairs exhibit December seasonality on an intraday basis, versus around 15 in August.

August has historically been associated with risk-off market behaviour. Consistent with this pattern, we find that JPY tends to appreciate against both G10 and EM currencies. These close-to-close moves are primarily driven by price action during the London–New York overlap (12:00–16:00 London time). We also observe weakness in some EM currencies against the dollar, particularly ZAR and MXN, with these moves largely occurring during the New York afternoon session (16:00–20:00 London time).

The yen pattern and fewer seasonality pairs during non-overlapping time zones suggest that August seasonality is not driven by liquidity conditions alone. In our earlier work, we argued that FX seasonality can arise from trading imbalances linked to liquidity-related activity, reflecting investors' preference to transact during local market hours. However, some seasonal patterns may be driven by information-related factors rather than liquidity needs alone. The concentration of August price moves in the London–New York overlap is consistent with this interpretation, given that this is typically the most information-rich period of the global trading day. In the case of JPY appreciation, we find that price moves originating in the London morning tend to persist into the London–New York overlap. Consistent with our previous findings, this return persistence may reflect information asymmetries among market participants or the continuation of the price discovery process as information is progressively incorporated into prices across trading sessions. Lower market liquidity during August may further amplify the impact of these information-driven flows.

This helps distinguish August from December, despite both months showing strong seasonality in daily closing prices. In December, seasonal FX patterns appear more closely tied to calendar-driven liquidity and hedging flows around year-end reporting, balance-sheet management and portfolio rebalancing; in August, by contrast, the evidence points more to information-sensitive risk-off dynamics amplified by thinner summer liquidity.

Figure 2: Breadth of seasonality highest in August (based on London closing prices)  
![](images/29801c402b9a1bd43a24466ba1e44a42e4736811b5798c967d8f8756425bf7cf.jpg)  
Source : DB.  
Figure 3: Breadth of seasonality moderate in August (based on intraday prices)

![](images/d6360d6373b152d4da192dc74c9f90c74f3e788d1809ff83a3485e0750c89572.jpg)  
Source : DB
Session times (London time): Asia 00:00–07:00, London (LDN) morning 07:00–12:00, London–New York overlap (LDN/NY) 12:00–16:00, New York afternoon (NY) 16:00–20:00.

## Seasonality stronger for currencies weakening against JPY over USD

August exhibits one of the clearest risk-off seasonal patterns in FX. While the USD tends to strengthen against many currencies, the dominant feature is broad-based JPY outperformance. For JPY, the outperformance appears to be driven by price moves in the Mixed London/NY session while USD appreciation appears to be driven by the NY afternoon session.

The contrast between USD and JPY performance is particularly evident across currency groups. While EM currencies tend to underperform more than G10 currencies against the dollar during August, weakness against the yen is both broader and more pronounced across the FX complex. This suggests that August seasonality is not solely a dollar-strength phenomenon, but also reflects a more widespread preference for defensive currencies, with JPY emerging as the primary beneficiary (Figure 4 - Figure 8).

Figure 4: August a risk-off month - G10 and EM currencies weakening versus USD and JPY  
![](images/bfed329cd0c8faf13d98470d89d2a52b40e4e33fe58f7a6621f3d968a46bb0a5.jpg)  
Source :DB

![](images/d48f32fb915aef6bea0c6564745d4d5b82445e6acf82ca4ad8127b83ec7384d4.jpg)  
Figure 5: Currencies weakening vs JPY driven by Mixed London/NY session

![](images/71a0f083ee6f9654c6e029e6abe18cb4d2284c6c3efda8513419072e0de86dfd.jpg)  
Source : DB

Figure 6: Currencies weakening against USD driven by NY afternoon session  
![](images/d1e47a0493f242e2b0c6ca1a805e151af0fadc5825c31e881a31f6fd857a2fa5.jpg)  
Source : DB

Figure 7: G10 currencies weaken more consistently against JPY than USD  
![](images/46e42007a54875a8e9de8d43f86d03d30a34fea2465f680312bc086ebf95ee72.jpg)  
Source :DB

![](images/9734d3068fd427258a4aeab520913ba13d0f87343cfe6f6a9b1032c5bda230db.jpg)

Figure 8: EM currencies weaken more consistently against JPY than USD  
![](images/e4dc0022312fa547f1baff7dffeb7f31f3a0f5b11122cc3fc7f7e01285ad7d26.jpg)  
Source :DB

![](images/372cca71160b874751f862f287b8fc9f1d33e680badcf87a205f1df6a5930bf0.jpg)

Figure 9: Currencies tend to weaken against the dollar  
![](images/a411de7230fc90ce304e253f45be526f4f516f2e1883528f7ccef4b9e6714e4a.jpg)  
Source : DB

Figure 10: And even more so against the yen  
![](images/f8dd39af7fe8c3c162b4818df79e4b5906b778c0b87d87cee2e5c852ba544972.jpg)  
Source : DB

High-beta, commodity and carry currencies such as ZAR, MXN, AUD and NZD experience the largest declines, suggesting that lower summer liquidity and seasonal risk reduction contribute to a recurring flight-to-safety dynamic. The pattern is remarkably widespread, with both G10 and EM currencies underperforming against USD and, even more significantly, against JPY, making long JPY exposure the strongest August seasonal theme (Figure 9 and Figure 10).

The weakness in EM currencies may also reflect the tendency for major macroeconomic and geopolitical developments to have an outsized impact during the summer period, when market liquidity is often thinner. For example, August has coincided with a number of significant risk events, including the escalation of the European sovereign debt crisis and the downgrade of the US sovereign credit rating in 2011, the RMB devaluation in 2015, and the Turkish lira crisis in 2018. Similarly, EM currencies came under significant pressure in August 2019 as US-China trade tensions intensified. These episodes suggest that August seasonality may be influenced not only by liquidity conditions but also by information-related factors, with periods of heightened uncertainty reinforcing demand for defensive currencies such as JPY.

## ZAR selling against USD and JPY

ZAR stands out as the weakest currency in our sample during August. Against the USD, it records a volatility-adjusted return (t-statistic) of around -2.0, indicating a statistically significant tendency to depreciate during the month. The effect is even more pronounced against JPY, where the t-statistic falls to approximately -3.1, the weakest reading across both G10 and EM currencies.

August has historically been a difficult month for the rand. Over the last ten years, ZAR has weakened in roughly 60% of Augusts against the USD and 70% against JPY. The pattern is also evident over longer horizons, with the rand depreciating in 13 of the last 20 Augusts against both currencies. This underperformance is consistent with the broader August risk-off environment, during which investors have tended to favour safe-haven currencies, particularly JPY.

Although the historical sample shows consistent ZAR underperformance against both USD and JPY during August, more recent trends have been less uniform. The pattern did not hold against USD in 2024 and against either USD or JPY in 2025, coinciding with a period of favourable commodity-price dynamics, attractive carry and improved investor sentiment towards South African assets (Figure 11 - Figure 14).

Figure 11: ZAR has generally weakened vs the dollar  
![](images/c2c4e69ea044a3092496d7b673c97080d0e866ce8d01fde021fdeece3a5c06cf.jpg)  
Source : DB
Session times (London time): Asia 00:00–07:00, London (LDN) morning 07:00–12:00, London–New York overlap (LDN/NY) 12:00–16:00, New York afternoon (NY) 16:00–20:00. LDN close denotes London close-to-close returns.

Figure 12: However, 2024-2025 has seen more ZAR buying than selling against the dollar  
![](images/a6690c734f6851b26bb6c00ef4c14c226d2ff7522285ff474f28bd50d47afb73.jpg)  
Source : DB

Figure 13: ZAR has generally weakened vs the yen  
![](images/4150899e01117d43f0aa480e8fd32a226c8509e9630679ac113b6b8903e6d31a.jpg)  
Source : DB
Session times (London time): Asia 00:00–07:00, London (LDN) morning 07:00–12:00, London–New York overlap (LDN/NY) 12:00–16:00, New York afternoon (NY) 16:00–20:00. LDN close denotes London close-to-close returns.

Figure 14: Seasonality was weak last year vs yen but stronger than vs the dollar  
![](images/49cb53b14713559b59969e646036631d107a08fc07826ca8f8e233234fcc681d.jpg)  
Source : DB

## A closer look at JPY crosses

Across the most liquid JPY crosses, the yen has strengthened against all G10 currencies in August. Statistical significance is highest against GBP and lowest against NOK. Focusing on USD/JPY, JPY has appreciated against the dollar in 13 of the past 20 Augusts, with the pattern remaining strong in both 2024 and 2025 (Figure 15 and Figure 16). At a more granular level, USD and GBP tend to see their largest declines against JPY between 12:00 and 13:00 London time (Figure 17).

Figure 15: USD/JPY weakness in August  
![](images/a66c961c0308c935b09d9b6d325fab8204025baa4bbdd611f5a1d814f553529f.jpg)  
Session times (London time): Asia 00:00–07:00, London (LDN) morning 07:00–12:00, London–New York overlap (LDN/NY) 12:00–16:00, New York afternoon (NY) 16:00–20:00. LDN close denotes London close-to-close returns.

Figure 16: Recent trend is encouraging for JPY  
![](images/0ec20498cbdef957ae9337c20a48bbe55c2e15cd2ad5b1735fa13633e51eaf36.jpg)  
Source : DB

Figure 17: A closer look at hourly returns  
![](images/7d32c4b06a4734eea5425df4522584197c7493968527414f32871266e0887a2e.jpg)  
Source : DB

## NZD weakness close-to-close driven by weakness in Asia

Beyond JPY and EMFX, NZD also shows consistent August weakness against USD, EUR, CAD and JPY, particularly during the Asian session. On a London close-to-close basis, this leaves NZD weakest against JPY, followed by EUR, USD and CAD. This pattern may not be solely a function of risk sentiment. Seasonal trade dynamics may also play a role: August is typically the weakest month for New Zealand dairy exports, reflecting the seasonal trough in milk production during the Southern Hemisphere winter. Given the importance of the dairy sector to New Zealand's economy, these seasonal trade patterns may contribute to the recurring August weakness observed in NZD.

Figure 18: NZD weakness in August – volatility-adjusted returns (t-statistics)  
![](images/a44a1d326ae827569cd3971772083e850213838103904134f66ab3732852fcb0.jpg)  
Source : DB

Figure 19: NZ dairy exports are the weakest in August  
![](images/c520a00df42179356fa70aa93df1ca461f8b0c3ac9e456bb57bb6bb8cbe0998c.jpg)  
Source : DB

## Appendix: Detailed tables

## Figure 20: Seasonality in August - T-stat

<table><tr><td></td><td>Asia</td><td>London Morning</td><td>Mixed London /NY</td><td>NY after noon</td><td>London close-to-close</td><td></td><td>Asia</td><td>London Morning</td><td>Mixed London /NY</td><td>NY after noon</td><td>London close-to-close</td><td></td><td>Asia</td><td>London Morning</td><td>Mixed London /NY</td><td>NY after noon</td><td>London close-to-close</td><td></td><td>Asia</td><td>London Morning</td><td>Mixed London /NY</td><td>NY after noon</td><td>London close-to-close</td></tr><tr><td></td><td colspan="5">G10/USD</td><td></td><td colspan="5">G10/EUR</td><td></td><td colspan="5">G10/JPY</td><td></td><td colspan="5">G10 crosses</td></tr><tr><td>EUR</td><td></td><td></td><td></td><td></td><td></td><td>USD</td><td></td><td></td><td></td><td></td><td></td><td>USD</td><td></td><td></td><td>-1.8</td><td></td><td>-2.1</td><td>GBPCHF</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>JPY</td><td></td><td></td><td>1.8</td><td></td><td>2.1</td><td>JPY</td><td></td><td></td><td></td><td></td><td>2.2</td><td>EUR</td><td></td><td></td><td></td><td></td><td>-2.2</td><td>NOKSEK</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>GBP</td><td></td><td></td><td></td><td>-1.8</td><td></td><td>GBP</td><td></td><td></td><td></td><td></td><td></td><td>GBP</td><td></td><td></td><td></td><td></td><td>-2.9</td><td>AUDNZD</td><td>2.5<

[中间内容因长度限制已省略]

r items of value for their personal use from issuers they cover.

Additional information relative to securities, other financial products or issuers discussed in this report is available upon request. This report may not be reproduced, distributed or published without DB's prior written consent.

Backtested, hypothetical or simulated performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG.

It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

<table><tr><td colspan="4">David Folkerts-LandauGroup Chief Economist and Global Head of Research</td></tr><tr><td>Pam FinelliCOO and Head of Fixed Income Research</td><td>Steve PollardGlobal Head of Company Research and Sales</td><td>Jim ReidGlobal Head of Macro and Thematic Research</td><td>Tim RokossaHead of European Company Research</td></tr><tr><td>Matthew BarnardHead of AmericasCompany Research</td><td>Debbie JonesGlobal Head of Sustainability and Data Innovation, Research</td><td>Robin WinklerHead of German Macro Research</td><td>Sameer GoelGlobal Head of EM &amp; APAC Research</td></tr><tr><td>Francis YaredGlobal Head of Rates Research</td><td>George SaravelosGlobal Head of FX Research</td><td>Peter HooperVice-Chair of Research</td><td>Nilendra de-MelHead of APAC &amp; Middle East Product Development</td></tr></table>

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip</td><td>60329 Frankfurt am Main</td><td>Centre,</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Streets</td><td>Germany</td><td>1 Austin Road West,Kowloon,</td><td>Japan</td></tr><tr><td>Sydney, NSW 2000</td><td>Tel: (49) 69 910 00</td><td>Hong Kong</td><td>Tel: (81) 3 6730 1000</td></tr><tr><td>Australia</td><td></td><td>Tel: (852) 2203 8888</td><td></td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr></table>
"""
