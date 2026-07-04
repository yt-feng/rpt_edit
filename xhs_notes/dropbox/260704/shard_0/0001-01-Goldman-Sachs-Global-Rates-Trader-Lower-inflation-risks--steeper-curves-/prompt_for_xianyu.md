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

# Lower inflation risks, steeper curves

The slowdown in hiring and less hawkish Fedspeak have curtailed near-term hike risks. How pricing evolves from here hinges on inflation in a week and a half, where a benign print can support further front-end consolidation and re-steepening of the curve, or vice versa. Beyond the very front-end, ongoing AI capex spend and financing is likely to limit room for long-end yields to fall. While the decline in front-end traded inflation has largely tracked the usual relationship with energy prices, forwards have underperformed; despite more favorable valuations, we think upside to inflation longs is limited absent dovish re-evaluation of the Fed reaction function. Traded inflation's continued decline in Europe reinforces a narrow channel for front-end core yields, lower vol and carry via EGB longs and curve steepeners. UK 2s10s steepening can continue as the BoE hike premium continues to decay and term premium remains sticky. The apparent willingness to rely on FX intervention rather than faster rate hikes to address JPY weakness continues to point to disequilibrium in Japanese macro assets, with ongoing upside risks for belly and longer-term JGB yields. Still hawkish 2027 pricing and richer long-end valuations point towards a steeper NZD curve.

## United States and Canada

Letting some air out of the balloon. Softer than expected June payroll growth coupled with downward revisions to the prior months have curbed rates market concerns about underlying acceleration. Month-to-month noise in the labor market data—this time coming most clearly from the outsized labor force decline that supported the drop in the unemployment rate—reinforces the idea that accumulation of milder activity data is necessary, but not sufficient to curtail broader hike risk. But the softer print combined with Chairman Warsh’s comment that “inflation risks have come down” have deflated the argument that there may be urgency to raise rates and reduces the risk that an on-hold July rate decision could reintroduce long-end volatility. The June CPI data will be key to pricing and how the market reacts to any eventual decision. Our economists’ preliminary estimates for the coming prints are for a clear step down from the recent trend, which we think could further sustain the recent consolidation in hike risk. We find that when the market prices in hikes for the front meeting prior to an eventual on hold decision, how broader policy pricing—i.e. 1y ahead meeting OIS—adjusts tends to be directional with the change in inflation pricing (Exhibit 1). Stable oil prices and benign inflation news can continue to support a gradual erosion of

George Cole  
+44(20)7552-1214 |  
george.cole@gs.com  
GS International

William Marshall +1(212)357-0413 | william.c.marshall@gs.com GS & Co. LLC

Simon Freycenet  
+44(20)7774-5017 | simon.freycenet@gs.com GS Bank Europe SE - Paris Branch

Isabella Rosenberg +1(212)357-7628 | isabella.rosenberg@gs.com GS & Co. LLC

Friedrich Schaper +1(917)343-3214 | friedrich.schaper@gs.com GS & Co. LLC

Loic Mathys +44(20)7051-1664 | loic.mathys@gs.com GS International

hike risk and in time press towards a steeper curve, but we think the hedge value of paying near-term meetings will put a floor on how much more the front-end can compress over the near-term. Supporting a steeper curve, however, is the limited ability of long-end rates to rally given reduced downside growth risks and ongoing AI capex.

## Exhibit 1: Whether an on-hold Fed decision sustains a reduction in broader hike pricing likely depends on near-term inflation risks

Intermeeting change in 1y ahead Fed pricing versus 1y inflation swap conditioned on Fed on hold and market pricing some risk of hikes at start of intermeeting period

![](images/5bd5d3995dfa8afdd57060181f2dda04e947495859b042682f0f0a5b6390afa1.jpg)  
Source: GS Global Investment Research, GS FICC and Equities  
Exhibit 2: Longer term inflation forwards have underperformed typical macro drivers

![](images/7a60fd4beddb4f543a5aff499d6fb25d8df2a8b26ccdcaa84ee17ef45bca6651.jpg)  
Model includes 1m and 12m oil prices, 1y-ahead consensus inflation forecasts, 1y-ahead inflation forecast dispersion, long-run inflation forecasts, 1y-ahead growth forecasts, and a measure of 1y-ahead forecasted policy changes. Sample includes weekly data from 2010 to present.  
Source: Consensus Economics, Haver Analytics, Bloomberg, GS FICC and Equities, GS Global Investment Research

Inflation looks slightly cheap, but risk/reward not all that compelling. The swift decline in traded inflation since the US-Iran MOU and June FOMC has been led by the front end of the inflation curve, where traded inflation's typical relationship with oil prices can account for nearly the entirety of the move. That said, forward inflation pricing has declined more than the drop in oil prices would typically justify, leaving 5y5y inflation trading around $2.35\%$ —close to levels last seen during the initial post-conflict growth scare. We suspect this larger-than-implied decline reflects the market's perception of reduced risk of the Fed falling behind the curve following the June FOMC, while choppier price action in risk assets may be adding marginal pressure as well. Despite slightly cheap valuations in forwards, we do not think traded inflation is a compelling long right now. The market is still pricing higher inflation on a 1-to-2y ahead horizon than our economists forecast in 2027, and hawkish Fed assumptions may keep a cap on inflation pricing for a while yet. The case for longs, in our view, is as a hedge to the Fed revealing a more dovish reaction function or another exogenous shock to prices.

Subdued funding pressure, but a wider medium-term distribution. The end-Q2 turn saw limited repo pressure despite a net cash inflow to TGA amid month-end Treasury settlements; only a small fraction of SOFR transactions took place above the Fed's Standing Repo rate, corresponding to no usage for a second consecutive quarter-end, whereas RRP uptake was the highest since the year-end turn. As noted previously, we think collateral and funding supply/demand dynamics have played a role in the benign funding backdrop—reserves are down modestly this year as a share of bank assets, but we estimate the relative shifts in T-bill free float and repo volumes versus money fund assets have been worth 1-to-1.5bp of downward pressure on equilibrium SOFR and TGCR levels. We also find evidence that the sensitivity of funding costs to changes in liquidity has become less negative this year, and while equity funding spreads had been elevated into quarter-end, we think the discrepancy is again largely attributable to divergence in end user demand for leverage. The Fed will announce the next schedule for reserve management purchases (RMPs) closer to the middle of July, and we see scope for another reduction in the monthly pace of purchases from \$10bn recently to \$0-to-5bn. We estimate that a monthly RMP pace of \$5bn per month would see reserves declining to around 11% of bank assets by 1Q27 and be consistent with TGCR at or slightly below IORB in the steady state, and SOFR slightly above it. Early-27 SOFR-FF pricing is consistent with our baseline assumptions, but the potential intersection with reaching the debt limit and medium-term uncertainty around potential changes to the balance sheet approach present two-sided risks.

## Europe

European inflation relief extends, fuels carry. Incoming data increasingly points to benign inflation risk in the Euro area. Our economists have shaved their inflation forecasts following the June flash report and highlight downside risk to their projections should commodity prices stabilise at current levels (which are below our energy price forecasts). This should keep front-end pricing in a narrow channel around a September hike, with risks fairly balanced. On the one hand, an increasingly secure inflation relief should weigh on hike pricing, all else equal. On the other, ECB speakers have highlighted the possibility of a rising neutral rate for the Euro area, which may see terminal rate pricing remain sticky until a clearer data signal emerges. That said, we think the positive slope in pricing beyond September (10bp between September and March-27) is hard to justify in this environment and should decay over time. Beyond the front-end, we continue to see more room for rates volatility to fall than the level of yields, with sovereign credit (see below) and curve steepeners continuing to offer carry in a low volatility environment.

OAT widening excessive. Despite strong tailwinds for sovereign credit—including an improving growth outlook, lower policy uncertainty, and reduced energy-related fiscal risks following the US-Iran deal—OATs have widened against Bunds over recent weeks. This likely reflects a range of factors, including early positioning for potential tensions around the 2027 budget negotiations, as well as increased political uncertainty over next week’s verdict (due in the afternoon of 7 July) on the ability of Rassemblement National’s Marine Le Pen to run in the 2027 elections. Despite the inevitable focus on next year’s election and budget, consensus expectations for the French deficit were actually falling into June (in absolute terms and against peers — Exhibit 3). For this reason, we do not think the recent widening will endure, with the reduction in macro and rates vol likely to reanchor spreads, particularly at shorter maturities. Long-end spreads also offer value — 30y OATs are near their wides since the onset of the Iran war despite much lower rates volatility — but are likely to remain stickier given the more medium-term fiscal uncertainties (Exhibit 4).

Exhibit 3: French deficit expectations have on net moved in a more favourable direction Change in 12m ahead deficit expectations, 3 months rolling sum

![](images/8a86b35c32f3bf3d667ddc722ef07a93afd193d2b450e3e1044bdd03eebed474.jpg)  
Source: GS Global Investment Research, Consensus Economics  
Exhibit 4: Long-end OATs are close to their conflict wides against Bunds Using GS fitted yields

![](images/3542be782e0436b013dbc5adb88442728547f1fd91e1c4e820c6274d8808fc96.jpg)  
Source: GS Global Investment Research, GS FICC and Equities

ECB Minimum Reserve Requirements back in focus. Reports this week suggested the ECB is considering an increase in minimum required reserves (MRR) from 1% to 2% of Euro area banks' short-term liabilities. With MRR currently standing at €172bn, a doubling of the MRR would imply a corresponding decrease in excess liquidity as banks relocate cash from the Deposit Facility to ECB current accounts. This would represent a roughly €4bn interest cost saving from the ECB's perspective, borne by banks, as required reserves are remunerated at 0% rather than the Deposit Facility Rate. We have previously argued that the implications for bank behaviour and money markets are likely to be limited given excess liquidity remains above €2tn. However, compared with the last time the ECB considered such a change at end-2023, excess liquidity is €1-1.5tn lower owing to the ongoing QT drain, and may be approaching the upper end of a plausible range for equilibrium reserve demand. A shift in MRR would see the ECB test that range in a less gradual way than with QT alone (Exhibit 5). Additionally, excess liquidity remains unevenly distributed across countries, with the bulk located in core countries (Exhibit 6), suggesting the potential for uneven consequences of an MRR hike. Finally, while we do not see this as a strong signal for rate policy, a higher MRR would mitigate the interest cost from higher policy rates for the ECB, which may improve the sustainability of higher rates from a political (rather than economic) perspective.

Exhibit 5: A change in MRR would pull forward the point in time at which liquidity is more binding
Stylised equilibrium reserve range depending on banks preferred level and composition of HQLA  
![](images/36c04090c827a27ac6ff9160f1b12583f82a7004d3723870d6398a4e7a4e0a8d.jpg)  
Source: GS Global Investment Research, ECB, Haver Analytics

Exhibit 6: Excess liquidity is heavily concentrated in core countries

![](images/c32f696f561550b3b185495c7ffe31f7c0887d1ee90a1f85a5da2f8f84131606.jpg)  
Source: GS Global Investment Research, ECB, Haver Analytics

UK 2s10s curve to keep steepening. We think the steepening of the UK curve is likely to continue. Governor Bailey's remarks in Sintra revealed the BoE is still focused on labour-market softening and weak growth, which, together with oil relief, should keep front-end yields trending lower as residual inflationary risks subside. The ongoing focus from Bailey on the pre-war cut pricing suggests the possibility of an eventual return to easing, potentially in 2027, that should continue to see the front-end outperform. At the same time, the curve steepened with longer-dated UK yields rising. We think this is consistent with limited further room for risk premium compression until the market has a clearer view on upcoming policy changes under a potential Burnham government, especially as the tension between spending ambitions, tight headroom and limited tax options remains unresolved. Next week's Financial Stability Report (7 July) could provide a modest tailwind to Gilts on asset swaps via tweaks to the leverage ratio. As a result, we continue to prefer GBP steepeners, with front-end macro relief doing the work to pull yields lower while ongoing fiscal uncertainties limit the scope for further UK term-premium compression.

## Japan

JGB term premium pressure builds. The JGB curve continues to steepen, with the 2s10s curve stuck at steep levels relative to the cyclical and spot fiscal backdrop (a residual we find remains even after introducing additional controls for the QE and YCC era). Part of the long-end cheapening also reflects a broader term premium normalization across much of the G10. This global normalization is part of the explanation for the more positive correlation between rising JGB term premium and risk-neutral rates. However, we think domestic fiscal and behind the curve risks are a clear contributing factor, remaining a key source of upward pressure on yields and weakness in the Yen (Exhibit 7). Absent a shift in the Takaichi administration's fiscal stance—around which this month's release of the administration's Basic Policy is potentially pivotal for near-term JGB volatility—we think risks skew towards 10s and 30s cheapening further, with mounting pressure on the belly over time. Potential JPY intervention is also likely to weigh on JGBs, as suppressing FX volatility through this channel (rather than via more proactive rate policy) leaves longer term rates the main domestic pressure-release valve. Together, we think ongoing fiscal risk and intervention-based FX management can continue to lift term premia and sustain JGB curve steepening.

Exhibit 7: Yen weakening is no longer corresponding to front-end JPY rates underperforming the typical beta to the US

USDJPY vs 2y JPY OIS (versus beta-implied by 2y USD OIS; higher = JPY cheaper)

![](images/23d0a41f845e5ae7392c340f531cb9e10efa00f2637a85b2722ba5b036ff2d10.jpg)  
Source: GS Global Investment Research, GS FICC and Equities  
Exhibit 8: 2s10s has room to steepen on relaxation of hike premium  
2s10s, 1y1y NZD OIS

![](images/b5a74c4cefa8c80dcb57430e8e39f7c0deab68577a2ffb226ab4dd6872122a04.jpg)  
Source: GS Global Investment Research, GS FICC and Equities

## Australia and New Zealand

Room for premium to migrate out the NZD curve. Our economists expect RBNZ to deliver the first of two hikes at its meeting next week following the hawkish guidance by Governor Breman and early evidence of second-ro

[中间内容因长度限制已省略]

ttempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global

Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
