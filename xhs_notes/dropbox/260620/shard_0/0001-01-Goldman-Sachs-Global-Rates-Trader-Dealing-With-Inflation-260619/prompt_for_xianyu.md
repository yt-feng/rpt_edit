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

Dealing With Inflation

Inflation risks have subsided somewhat given the energy relief following the US-Iran deal, but in their place the market has repriced US front-end rates following the hawkish FOMC messaging. As markets adapt to a shift in Fed communication, we expect greater policy uncertainty to support vol and see scope for greater reactivity to individual datapoints and Fed communication. Our forecasts and longer-term valuations argue for a steepening bias in the US, but with hawkish risks boosting front-end yields and compressing long-end risk premium, we think positioning for belly outperformance on the curve offers the best near-term risk/reward for longs. Energy relief narrows the outcomes for European rates, favouring lower vol and EGB carry, but we think the prospects for much lower yields are limited. In contrast, we expect more macro relief for front-end UK rates as the BoE remains on hold and energy inflation subsides. We favour 2s10s GBP steepeners as fiscal risk premium remains elevated following the Makerfield by-election. With the BoJ having delivered a hike without more hawkish guidance on the path or end-point of the tightening cycle, fiscal policy is likely a near-term focal point. We expect the long-end to be more reactive to any developments, but continue to think that risk/reward is more favourable to shorts further in on the curve.

## United States and Canada

Risk premia rotation. Wednesday's FOMC injected new life into the possibility of a series of rate hikes for a market that had been consolidating around a less severe inflation outcome. Our economists see an increased risk of hikes later this year but have maintained their baseline that the FOMC will leave the policy rate unchanged through the course of the year. What had been previously diffuse hike pricing has shifted in, with the market pricing nearly two hikes to the Mar/Apr-27 meeting peak in the OIS curve. While that risk is now more front-loaded, the rates curve has not priced a significantly higher peak than the one seen on the heels of the May labor market report (Exhibit 1). As we have observed in other markets, to the extent that the policy reaction function is seen as sufficiently front-footed, greater right tail risk around the very front-end can keep a lid on risk premia further out the curve. This dynamic is visible in the flattening that alongside taking hike pricing to levels consistent with a plausible “insurance” amount has pushed longer-term forwards to levels that are now rich to fair. That hawkish front-end/rich long-end backdrop tilts towards a steepening bias, and

## George Cole

+44(20)7552-1214

george.cole@gs.com

GS International

## William Marshall

+1(212)357-0413

william.c.marshall@gs.com

GS & Co. LLC

## Simon Freycenet

+44(20)7774-5017

simon.freycenet@gs.com

GS Bank Europe SE - Paris

Branch

## Isabella Rosenberg

+1(212)357-7628

isabella.rosenberg@gs.com

GS & Co. LLC

## Friedrich Schaper

+1(917)343-3214

friedrich.schaper@gs.com

GS & Co. LLC

## Loic Mathys

+44(20)7051-1664

loic.mathys@gs.com

GS International

we think that a relaxation in hike risks ought to correspond to a steeper curve with long-end forwards stickier. But we think for now there is clearer scope for the reevaluated reaction function to support the belly of the curve. An undoing of the broader hawkish repricing (on more benign data, for example) can undo the recent underperformance of 5s versus 2s and 10s, whereas our prior analysis suggests 5s ought to outperform on the curve from front-loading of hike risk against stickier or declining forwards further out the curve (Exhibit 2, which we would expect on hotter labor market or inflation data).

Exhibit 1: Hike risk is more front-loaded, but the curve is not pricing a significantly higher peak  
3m SOFR futures curve  
![](images/dc546a72885b6eab2bbbf409d21f7f89b72ae2329709034ddcffe1f9c0619329.jpg)

<details>
<summary>line chart</summary>

| Period | 5-Jun (%) | Latest (%) |
|---|---|---|
| M6 | 3.67 | 3.72 |
| U6 | 3.80 | 3.94 |
| Z6 | 3.97 | 4.10 |
| H7 | 4.08 | 4.14 |
| M7 | 4.10 | 4.11 |
| U7 | 4.09 | 4.05 |
| Z7 | 4.03 | 3.96 |
| H8 | 3.99 | 3.89 |
| M8 | 3.96 | 3.85 |
</details>

Source: Bloomberg, GS Global Investment Research

Exhibit 2: 5s should outperform on the curve from front-loading of hike risk against stickier or declining forwards further out the curve  
Shift in curve segments implied by changes in pace of hikes over next 6m, extent of hikes over next 2y, and changes in longer-run (5y5y) rate levels  
![](images/730fa2eb85e0dafa24e768d16afa6bd47277d0bf143258c3ade7c0069d60b32e.jpg)

<details>
<summary>bar chart</summary>

| Category | 2s5s (bp) | 5s10s (bp) | 10s30s (bp) |
|---|---|---|---|
| Unch'd terminal Unch'd LR | -12.0 | -1.0 | -1.0 |
| Unch'd terminal 25bp higher terminal Unch'd LR | -6.0 | -8.0 | -8.0 |
| Unch'd pace 25bp higher terminal Unch'd LR | 5.5 | -7.0 | -6.0 |
| Unch'd pace 25bp higher terminal 25bp higher LR | 12.0 | 1.5 | -0.5 |
</details>

Source: GS FICC and Equities, GS Global Investment Research

Double trouble for traded inflation. The steep and steady decline in oil has reset front-end inflation pricing in alignment with our economists' latest headline CPI projections (Exhibit 3). While the energy picture has weighed on the forward curve as well, the reassessment of the Fed's reaction function corresponded to a sharp rise in real yields alongside a compression in inflation forwards. We highlighted a preference for beta-weighted real rate longs on the premise that a deeper rally would likely require a heavier lift from real rates and that it offered some insulation against the still-present geopolitical uncertainty. While we still think some elements of the former argument hold, as long as the recent hawkish shift proves somewhat durable, higher spot inflation is likely to be accompanied more reliably by higher real rate expectations rather than inflation risk further out the curve, narrowing the path to lower real rates (for example, benign scenarios where the Fed underdelivers versus what is priced without too much added disinflation). While our valuation framework puts longer term inflation forwards on the cheap side of fair, and our economists expect a more dovish reaction function than is priced, we close our long real rates on a beta recommendation at a small loss given the less favorable post-FOMC backdrop.

■ Shifting vol risks from macro to policy. The decline in energy prices and reduction in geopolitical uncertainty have weighed on implied volatility across the surface, but building clarity around the US-Iran conflict has given way to more uncertainty around the Fed's reaction function. We think this shift from macro to policy uncertainty should for now widen the distribution around the path for near-term rates, but greater vigilance against inflation can keep the long-end somewhat more stable. Consistent with this, our vol model suggests that the combination of a reduction in inflation survey dispersion and an increase in policy rate survey dispersion should typically be consistent with flatter tail curves (Exhibit 4). In the near-term, we expect greater sensitivity to communication from FOMC voters, as Chair Warsh offered little detail about the criteria for a rate hike or whether the news on the peace deal had been incorporated in FOMC members' dots, and continue to expect local volatility around FOMC meetings and minutes releases as markets adjust to a new communication regime.

Exhibit 3: Front-end inflation pricing aligns with our economists' forecasts  
![](images/7e8fd4ff6b5bca29c1f7920fe5d84ea15daeb102e72e9f459c1d32b6040b8df9.jpg)

<details>
<summary>line chart</summary>

CPI yoy Fixings vs GS Forecasts
| Date | Realized (%) | 2/27 Market-Implied (%) | Latest Market-Implied (%) | GS Econ Forecast (%) |
|---|---|---|---|---|
| May-25 | 2.5 | 2.6 | 2.6 | 2.6 |
| Sep-25 | 3.1 | 2.8 | 3.1 | 3.1 |
| Jan-26 | 2.6 | 2.5 | 2.5 | 2.5 |
| May-26 | 4.1 | 2.9 | 3.1 | 4.1 |
| Sep-26 | 3.5 | 2.6 | 3.3 | 3.5 |
| Jan-27 | 3.6 | 2.5 | 3.6 | 3.5 |
| May-27 | 2.1 | 2.3 | 2.3 | 2.1 |
| Sep-27 | 2.1 | 2.4 | 2.5 | 2.3 |
</details>

Source: GS FICC and Equities, GS Global Investment Research

## Exhibit 4: Greater policy uncertainty flattens the volatility tail curve

1y3m US rate uncertainty (orthogonalized against inflation, growth) vs implied vol tail curve

![](images/18652cc6579f06ba3b04d53ac1d587f057b3329bf7c0eb9d609f61a6dcea8fc7.jpg)

<details>
<summary>scatter plot</summary>

| Policy Rate Uncertainty | 1y30y - 1y2y Implied Vol. bp/day |
| ----------------------- | --------------------------------- |
| -0.4                    | -5                                |
| -0.3                    | 4                                 |
| -0.2                    | 3                                 |
| -0.1                    | 2                                 |
| 0                       | 1                                 |
| 0.1                     | 0                                 |
| 0.2                     | -1                                |
| 0.3                     | -2                                |
| 0.4                     | -3                                |
| 0.5                     | -4                                |
</details>

Source: GS Global Investment Research, GS FICC and Equities, Consensus Economics

\- Maintaining ample reserves, at least for now. The June FOMC statement added language on the balance sheet reaffirming the Fed’s “policy of maintaining ample reserves in the banking system.” We read this primarily as a statement of current policy, though it implicitly endorses the ample reserves framework, at least for now. Chair Warsh announced a task force to review the Fed’s balance sheet policy, and while other Fed officials have voiced support for the ample reserves framework in recent months, they have also acknowledged evidence that a reduction in reserve demand would warrant an adjustment in the supply of reserves. To that end, the implementation note was tweaked in a hawkish direction, adding “when appropriate” ahead of the directive to the New York Fed to increase the size of the SOMA portfolio to maintain ample reserves. While this still affords the NY Fed discretion on RMPs, it also points more clearly to periods when no growth in the SOMA portfolio might be deemed appropriate. Last week, the NY Fed decided to hold RMPs at \$10bn/month heading into June’s tax season. Although funding conditions tightened as mid-June corporate tax payments coincided with coupon settlements to start the week, the uptick in repo rates was shortlived against a still broadly stable backdrop. We continue to expect a \$5bn per month average in reserve management purchases over the coming quarters, which we think would be consistent with repo rates settling closer to IORB on average.

## Europe

\- Narrower range of outcomes, but relief well-priced in EUR rates. European duration rallied through the week as energy market relief extended. Front-end yields and inflation are slightly lagging the move in oil prices, but this is in part due to spillovers from the hawkish repricing of the US front-end. Given the price pressures already in train, our economists continue to expect the ECB to tighten policy once more in September, although the risk of no further hikes has risen. Markets price about 35bp of hikes over the next 12m, which suggests the market is still pricing somewhat hawkish risks relative to our modal view. This gap may decline should energy flows further reduce upside risks to commodity prices, but with the energy futures curve already below our revised oil and gas forecasts we think there is limited room for relief to extend. ECB surveys suggest $2.5\%$ is not seen as deeply restrictive, and the risk-neutral probability distribution priced into markets is only modestly hawkish to these surveyed expectations (Exhibit 5). This suggests that volatility is more likely to decline than yields (more below). Given the flattening that has already occurred in the EUR curve, and the outperformance of 10y, we close our long EUR 5y5y real rates recommendation for a potential gain of 11bp.

Exhibit 5: Markets are hawkish vs policy rate surveys ECB surveys of the policy rate vs market probabilities based on swaption pricing  
![](images/b199dcb850e8601dbcb5be3d51785661b6b76f0deb2e7bdf97020ebff032ab04.jpg)

<details>
<summary>stacked bar chart</summary>

| Category | ≤1.75% (%) | 2.00% (%) | 2.25% (%) | 2.50% (%) | ≥2.75% (%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| SMA / Market Sep Meeting | 0 | 0 | 28 | 64 | 21 |
| SMA / Market Dec Meeting | 0 | 3 | 23 | 59 | 49 |
| SMA / Market 3Q27 | 8 | 29 | 34 | 24 | 56 |
| SMA / Market Long run | 6 | 61 | 24 | 14 | 51 |
</details>

Source: GS Global Investment Research, GS FICC and Equities, SMA

Exhibit 6: EU bid-ask spread has underperformed growth in the EU debt stock  
![](images/d422dd893c84a839ff0bb00faae006b52a7ac83128d44205d38648e582f94cfd.jpg)

<details>
<summary>scatterplot</summary>

Bid-ask spread of 10y benchmark vs Debt outstanding
| Region | Bid-ask spread (in bp) | Debt sec. outstanding (in EUR bn) |
| :--- | :--- | :--- |
| GR | 1.6 | 150 |
| FI | 0.8 | 200 |
| PT | 0.6 | 300 |
| AT | 0.7 | 400 |
| EU | 0.9 | 800 |
| BE | 0.4 | 600 |
| NL | 0.3 | 450 |
| ES | 0.2 | 1600 |
| DE | 0.1 | 2500 |
| IT | 0.2 | 2700 |
| FR | 0.3 | 3150 |
</details>

Source: GS Global Investment Research, Bloomberg

\- Reduced risks improve outlook for sovereign spreads. The narrower range of outcomes for core rates and the ECB should continue to dampen rates volatility in Europe. This should provide ongoing support for EGB carry – we continue to recommend longs in 3y BTPs, OATs and Bonos vs OIS. Further out the curve, in our last update, we reiterated our expectation for modest sovereign spread widening for 10y spreads across countries into year-end. This view was premised on a sluggish Euro area growth outlook as well as the likely increase in political risk as 2027 drew nearer. We believe the US-Iran deal improves the outlook for sovereign spreads for three reasons. First, it allows rates volatility – which we see as a strong guide to sovereign credit risk – to come down further. Second, it limits the downside risks to growth. And third, it reduces the risks of increased fiscal support, widening deficits, and higher bond supply. To reflect this improvement in the outlook, we revise our end-2026 10y OAT-Bund, BTP-Bund, and Bonos-Bund forecasts to 70bp, 75bp and 45bp (from 75bp, 85bp, and 55bp respectively). This revision is larger in BTPs and Bonos than OATs, given Italy is more exposed sustained energy price pressure and historically sensitive to rates volatility. From current levels, we maintain a widening bias as we continue to think politics will be increasingly relevant throughout 2026 H2.

EU bonds set to outperform semi-core. The EU will announce its issuance target for the H2 2026 in coming weeks. We think the recent guidance of €180bn gross bond issuance for 2026 as a whole (or €70bn for H2) is still on target, although a modestly higher target is possible depending on mobilisation of funds under the NGEU. We showed in a recent report that EU bonds have broadly tracked aggregate Euro area fundamentals since 2022. This suggests to us that EU pricing is close to fair, but we see risks tilted towards outperformance vs semi-core. On the one hand, the ongoing underperformance vs its AAA-rating makes further cheapening unlikely. On the other, we think market deepening and various measures to improve liquidity taken in recent years could be better reflected in pricing. For instance, we have shown that EU bid-ask spreads have not compressed as much as the increase in the EU d

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
