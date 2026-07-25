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

The increase in July hike pricing over the last week has put the Fed in position to deliver the largest non-cut meeting day “surprise” in recent memory. Our economists expect the Fed to keep the policy rate stable, the impact of which we think will hinge heavily on how Chair Warsh frames the decision and path ahead. In particular, we think the (relative) long-end stability and contained inflation risk premia are vulnerable to an on-hold decision that is accompanied by limited guidance on the outlook or reaction function. European front-end rates now meaningfully exceed our central bank forecast, but as long as energy—especially gas—prices head higher, momentum is likely to trump value. In both EU and UK front-ends, Z6Z7 bear steepening is unlikely to sustain—either inflation subsides or volatility will migrate to earlier meeting dates, flattening the front-end. We ultimately think 2s10s curves steepen over coming months, especially in the UK where fiscal risks will likely keep Gilt risk premium elevated. 2y JGB yields pushed higher alongside further JPY currency weakness on reports the BoJ may consider faster hikes, but more durable flattening would likely require more evidence of a tighter monetary and fiscal policy mix.

## United States and Canada

CPI relief retreats. The roughly 15% rise in oil since last week's CPI release has helped to take the market from pricing a hike in July as a remote possibility to a meaningful risk. Our economists' baseline remains for the Fed to remain on hold; if current pricing holds it would set the stage for what we estimate would be the largest non-cut "surprise" on a meeting day in recent decades regardless of outcome (Exhibit 1). While media reports during the last cycle helped steer pricing to the ultimate outcome in the days prior to the decision, a meeting day surprise would nonetheless reflect the shift away from more proactive guidance. Assuming oil prices remain higher through the meeting, we expect a hold would most likely see hike pricing reshuffle, keeping late-26/early-27 pricing stickier (whereas a hike would likely pull the peak of the front-end forward), but broader behavior will hinge heavily on how the decision is communicated. We think on-hold policy paired with limited explanation of the outlook or reaction function would present risk to belly and long-end longs insofar as it could undo the "credibility" repricing seen following the June FOMC (Exhibit 2) and reintroduce inflation risk into the forwards. Longer-term forward valuations have

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

moved to the cheap side of fair in the recent selloff, but are still not so stretched as to argue for correction without a macro catalyst that arrests inflation risk or undermines the perception of growth resilience—both of which we continue to think would exert greater effect on shorter maturities.

Exhibit 1: If current pricing for the July FOMC holds, we estimate it would be the largest non-cut “surprise” in recent decades

Estimated non-cut meeting day "surprise" versus market pricing

![](images/d2e6e566da90bd6d8d4133f969208d65a42602f1771db105489331fe14d081c5.jpg)  
“Surprise” measured as meeting day change in weighted first or 2nd fed funds futures prior to 2002, 1m OIS from 2002 to present  
Exhibit 2: June's FOMC prompted a strongly hawkish repricing Change in UST yields on 17Jun26 FOMC

![](images/ce6f84e101aef96f4065c5530377aa3465b3c9ee047cd9a48c664016880b6059.jpg)  
Source: Bloomberg, GS Global Investment Research  
Source: GS FICC and Equities, Bloomberg, GS Global Investment Research

Volatility sticky through the latest energy surge. While yields reached new conflict-highs amidst the reacceleration in oil prices, implied volatility has so far been comparatively stable through the latest selloff, ticking up only slightly (Exhibit 3). The first phase of the conflict had seen a sharp increase in vol alongside a repricing of the rates path, which offered beneficial entry points to vol-selling strategies even before oil prices peaked. While vols are starting from a higher level, the lack of premium rebuild so far leaves the overall level of implied volatility at the bottom range of our valuation framework, suggesting little buffer for further shocks. In the near-term, we think returns to vol selling are likely to be counter-directional with energy prices (i.e. better returns hinge on lower energy). As we had argued before (and was visible initially following Warsh's first FOMC as Chair), greater uncertainty around the Fed's reaction function should also see volatility migrate in on the tail curve, continuing to skew the curve flatter, though there is near-term risk that a hold next week could boost belly and long-end vol if the market worries about a more dovish tilt to policy.

Questions ahead for stable swap spreads. Swap spreads have been by and large anchored around fair value against a backdrop of stable funding conditions, the relatively contained volatility discussed above, and a benign absorption picture for UST so far this year. Assuming status quo balance sheet policy from the Fed next week, the August refunding announcement the following week represents the next key piece of supply news. On the latter, we think there has been little perceived cost to Treasury of leaning into bill supply so far, but heightened front-end uncertainty and already-heavy bill supply over the next few quarters—our estimates imply about

1.2-to-1.3tn in net bill supply from 3Q26 to 1Q27—present risks, with the tepid reception of Thursday’s 8-week bill auction a recent indication of more cautious front-end demand dynamics. Our baseline remains for stable coupon auction sizes until May 2027—at which point we expect adjustments to be confined to 2s-7s—with Treasury’s “next several quarters” guidance once again a key focus. The relative stability in spreads and broader measures of Treasury convenience suggest macro risks rather than shifts in the supply/demand balance have been the primary factor behind the yield move, but we think Treasury would likely need to accompany any guidance change with some indication about where on the curve adjustments might come to avoid an adverse market response. We continue to think that 3y spread longs work as a carry expression, with valuations not a headwind, but think it makes sense to manage with a relatively tight stop and would close on meaningful widening.

Exhibit 3: The rise in energy prices has not yet translated into higher vol, or a flatter tail curve PCA Decomposition of USD Implied Volatility Surface

![](images/aab8051ebf4bb2cf554b1fdf5dcc49b754694373f00ffd6a77ec7e9fd8ddba73.jpg)  
Source: GS Global Investment Research, GS FICC and Equities

Exhibit 4: Global spillovers are pulling CAD yields higher Spillover contributions, Rigobon decomposition, since 24th April  
![](images/c6b76235680b556f31c776e09d987ac615039c4f88e71d025c0cb235de8b93d1.jpg)  
Source: GS Global Investment Research, GS FICC and Equities

\- Push and pull of oil vs trade risk in the CAD front-end. This week’s renewed focus on trade tensions following the White House’s announcement of a 50% tariff on \$20bn of Canadian goods is likely to stress dovish risks to the outlook for Canadian rates. The 2.5pp increase in the effective tariff rate on Canadian imports – if implemented – would likely create a 0.2pp drag on growth from lower exports. And while implementation remains somewhat uncertain (Polymarket suggests a 69% chance of some tariffs this year), our economists estimate heightened policy uncertainty and lower investment would be worth a further hit of 0.2pp to growth whether the tariffs take effect or not. The BoC had indicated willingness to ease policy in case of renewed trade restrictions; while we do not think this announcement is sufficient to argue for further easing just yet, it makes it unlikely that the BoC would hike back towards the mid-point of their neutral range absent clear evidence of underlying inflation pressures. With 19bp of hikes priced by December and 50bp by April, we think this points to further room for front-end hike premium to decay. In contrast, higher energy prices, and spillovers from a global repricing higher in yields create a tactical headwind for longs (Exhibit 4); we continue to prefer 2s10s CAD steepeners.

## Europe

Valuation vs momentum in European rates. European front-end rates remain tied to energy prices, with the re-escalation in the Iran war driving yields higher. Last week's ECB meeting did little to lower yields, with expectations consolidating around a September hike, our base case. But with limited fresh signalling for the near-term rate path, the front-end steepened with Z6Z7 now pricing close to a full hike, in addition to the two further hikes priced to Dec-26. This bear steepening is a familiar dynamic when inflation risk is rising, but volatility of front-meeting pricing remains contained. This could resolve in one of two ways: inflationary pressure subsides, or the speed limit on near-term meetings is raised. So far, it looks like 2y2y inflation is fairly priced alongside the movement in energy prices (Exhibit 5), but the lag in repricing of European rate volatility suggests some upside risk to front-end volatility unless energy risks subside – this is relevant for European sovereign credit which is tracking rates vol rather than the level of core rates. We continue to expect that the EUR swap curve will steepen on lower front-end yields – 1y1y OIS near 3% looks particularly elevated – but resilient economic data and sticky European gas prices are likely to delay relief.

## Exhibit 5: Forward HICP pricing in line with energy movements

![](images/3cb327b178c484a130f0de0c529dd6047a43622fcaa6a01f671a6de2c2c7f852.jpg)  
Source: GS Global Investment Research, GS FICC and Equities

## Exhibit 6: Market pricing of BoE path reflecting increasingly gas vs oil prices

Change in the beta of BoE meeting pricing to commodity prices (bp move per 1% move in commodities): 25 June to present vs 26 February to 19 March 2026

![](images/0103b099f1dc428fed460e9edff14b267ca2b2bc7c501e33cb99b52c5e595745.jpg)  
Source: GS Global Investment Research, GS FICC and Equities

Rising energy prices costing Gilts. The renewed rise in energy prices has driven Gilt yields and front-end pricing back towards their conflict highs. Like in Europe, inflationary pressure from higher energy prices has increasingly been reflected in 2027 rate pricing, with SFIZ6Z7 now steeper than when the war in Iran began. The latest re-escalation has resulted in two rotations: from Z6 to Z7 and from oil to gas, (Exhibit 6). These moves are consistent with BoE reluctance to hike faster than current market pricing, given Governor Bailey has maintained a comparatively dovish stance in recent communication. Our economists continue to expect the Bank to remain on hold at next week's meeting and through year-end, as activity remains sluggish and underlying inflation dynamics contained so far. However, the cost-of-living focus on Prime Minister Burnham – while not yet resulting in substantial spending commitments – is likely to keep the market focused on

potential fiscal measures should the energy shock worsen. With fiscal headroom a function of government funding costs, rising energy prices already add fiscal pressure that is likely to keep Gilt risk premium elevated. Although the near-term direction of front-end rates will be determined by movements in energy prices, with nearly three hikes priced into 2027 we continue to think the UK 2s10s curve will steepen over a three-month horizon.

## Japan

Support for a flatter curve dependent on BoJ signaling. Reports this week that the BoJ is open to raising rates faster than consensus expects—due to upside inflation risks from JPY depreciation—supported modest 5s30s flattening. As macro factors have been the biggest source of volatility in Japanese markets, a more hawkish BoJ could stem some of the cheapening pressure on rates and the currency. We think the extent of any relief likely depends not only on considerations around timing and pace, but also on the readthrough to terminal rate pricing. Simply pulling forward expected hikes may no longer durably curb further curve steepening and 10y underperformance because the market has for a while now viewed a 1.5% terminal rate as insufficient to sustainably curb inflation and thus for now requires further increases in term premium. The government has also grown more attuned to interest cost risks recently, proposing measures last week to encourage JGB inflows from GPIF and NISA accounts. We estimate both could lift demand for JGBs, though most of the impact is more likely to come through signaling and positive feedback loops—such as encouraging demand from other institutional investors—rather than outright purchases. We see room for outperformance in the parts of the yield and spread curves that have been hit hardest by supply-led cheapening, namely 20s and 30s (Exhibit 7). Ultimately, though, we continue to think that a sustainable decline in JGB volatility and support for the belly require support from the macroeconomic backdrop and/or monetary and fiscal policy mix. Our economists do not expect a hike next week, but Governor Ueda's messaging will be key, as will any follow-on commentary from Prime Minister Takaichi or Finance Minister Katayama. A hawkish tone, signaling openness to a higher terminal or short-run neutral rate, could ease concerns about BoJ independence and fiscal dominance risks and support further curve flattening.

Exhibit 7: JGB inflows from NISA or GPIF accounts could support parts of the curve hardest hit by supply factors

![](images/4e333bd0bec5e65173dbbc99e7031d4c61ee9dbfafa902734d925371d13a7fcb.jpg)  
Source: GS Global Investment Research, GS FICC and Equities

Exhibit 8: Medium-term forwards have borne the brunt of the recent oil-induced repricing, we expect the front-end to flatten  
![](images/f9b34d55e150c57163d38ebbdbee96a8d08b582f89768528ba1f9f44812842cf.jpg)  
Source: GS Global Investment Research, GS FICC and Equities

## Australia and New Zealand

Hawkish risks already priced in NZD, AUD forwards to take relief. Inflation data for 2Q26 in New Zealand came in hotter than expected, with CPI (yoy) 0.2pp above our economists' and the RBNZ's expectations. Given the RBNZ's prior hawkish pivot, this raises the likelihood of further tightening and our economists now expect an additional hike in December. We think recent communication coupled with the renewed rise in oil prices likely provides a floor under front-end rates for now. However, we continue to think the 120bp of tightening priced throughout the next year is excessive given core inflation remains within the target band and our economists expect labor market slack to ease underlying inflation pressure. Accumulation of data thus should curb hike premium over time, and we continue to expect 2s10s to steepen. In Australia, the 2y1y part has borne the brunt of the recent repricing in oil prices relative to the front-end (Exhibit 8). But while stronger labor market data raises the likelihood of a final RBA hike in August, as our economists expect, the tightening impulse delivered so far has started shifting the distribution around inflation risk, which in turn should allow longer-term forw

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
