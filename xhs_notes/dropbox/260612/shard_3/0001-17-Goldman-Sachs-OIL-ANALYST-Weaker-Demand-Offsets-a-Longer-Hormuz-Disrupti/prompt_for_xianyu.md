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
OIL ANALYST

# Weaker Demand Offsets a Longer Hormuz Disruption

\- Same 2026Q4 price forecast. We keep our 2026Q4 Brent \$90 forecast as the easing effect from a smaller-than-expected deficit during the Hormuz disruption so far offsets the tightening effect from a longer disruption. We estimate a 5-6mb/d Q2 deficit, which is smaller than the 14-15mb/d hit to Mideast liquids production because of nearly 5mb/d of estimated demand losses and over 4mb/d of oversupply in the absence of the war. We now assume that oil exports from Gulf producers normalize by late August (vs. by late June prior), which may be achieved with a rise in Hormuz flows to $70 \%$ of pre-war levels given current redirections.

Nudging down 2027 forecast. We lower our 2027 average Brent forecast by \$5 to \$80 on higher supply and lower demand. We lift 2027 supply in the UAE (given its OPEC exit) and the Americas (i.e. US, Brazil, Guyana, and Venezuela) on firmer realized and projected supply in our Top Projects dataset. While demand is likely to largely bounce back after reopening, we assume that just over 10% of the demand weakness persists as China's shift to alternatives (e.g. EVs) accelerates.

■ Resilient 2027 prices vs. large surplus. We forecast 2027 crude prices to exceed their 2025 average by \$10 despite an over 3mb/d 2027 surplus for two reasons. First, OECD commercial oil stocks are unlikely to reach very high levels following sharp 2026 draws and over 1mb/d of global strategic stockpiling in 2027. Second, a security premium compensating for disruption risk is likely to keep a floor under prices.

## ■ Two-sided but still net upside price risks.

☐ Adverse scenario: Brent 2026Q4 would average just over \$110 assuming Gulf exports only normalize by end-October.  
☐ Severely adverse scenario: Brent would average \$140 in 2027 assuming Hormuz remains disrupted through 2027 with Gulf countries' exports rising gradually by 5mb/d by Dec27 (with some expansion in allowed Hormuz flows and/or pipeline capacity).  
Benign scenario: Brent would average around \$70 in 2026Q4 and \$60 in 2027 assuming exports normalize by end-July, stickier demand losses, and stronger supply.

## Daan Struyven

+1(212)357-4172

daan.struyven@gs.com

GS & Co. LLC

## Yulia Zhestkova Grigsby

+1(646)446-3905

yulia.grigsby@gs.com

GS & Co. LLC

## Filippo Cuscito

+44(20)7051-9073

filippo.cuscito@gs.com

GS International

## Alexandra Paulus

+1(212)902-7111

alexandra.paulus@gs.com

GS & Co. LLC

We See Risks to Our Brent Price Forecast as Two-Sided but Tilted to the Upside on Net  
![](images/ef361f89f34aff35d036c0727756628e796065c88948c7746293994051d3a1e5.jpg)

<details>
<summary>line chart</summary>

| Date   | Severely Adverse ($/bbl) | Adverse ($/bbl) | Base Case ($/bbl) | Benign ($/bbl) | Forwards ($/bbl) |
|--------|---------------------------|-----------------|-------------------|----------------|------------------|
| Jan-26 | 115                       | 110             | 95                | 65             | 90               |
| Apr-26 | 130                       | 115             | 90                | 105            | 85               |
| Jul-26 | 145                       | 110             | 90                | 75             | 80               |
| Oct-26 | 150                       | 105             | 85                | 70             | 75               |
| Jan-27 | 145                       | 100             | 80                | 65             | 70               |
| Apr-27 | 140                       | 95              | 75                | 60             | 65               |
| Jul-27 | 135                       | 90              | 70                | 55             | 60               |
| Oct-27 | 130                       | 85              | 65                | 50             | 55               |
| Jan-28 | 125                       | 80              | 60                | 45             | 50               |
</details>

Source: GS Global Investment Research

We Estimate a 5-6mb/d Q2 Deficit, Which is Smaller Than the 14-15mb/d Hit to Mideast Liquids Production  
![](images/b6257ba9ae40032758927dc2ec3e281fef0fc27b1cf5c4021967db641511ae59.jpg)

<details>
<summary>bar chart</summary>

Reconciling 14-15mb/d Mideast Supply Loss With 5-6mb/d 2026Q2 Global Deficit
| Category | Value (mb/d) |
| :--- | :--- |
| Mideast Supply Downgrade Since War | 14.5 |
| Surplus, Forecast as of Feb 22 | -2.9 |
| Global ex Mideast Supply Upgrade Since War | -1.5 |
| Global Demand Downgrade Since War | -4.8 |
| Deficit, New Forecast | 5.4 |
</details>

Supply includes crude and NGLs.  
Source: GS Global Investment Research

## Weaker Demand Offsets a Longer Hormuz Disruption

Spot Brent futures have declined around $25\%$ from the late March peak despite still low flows through Hormuz mainly for two reasons.

Exhibit 1: Investor Positioning Moderation Has Been One Driver of the Decline in Oil Prices  
![](images/2edda92b0073de5388cb766c94bbc618aa6cd752af9ef5bcc542dfcd75ef65c7.jpg)

<details>
<summary>line chart</summary>

| Date       | Spot Brent Futures Price ($/bbl) | Long/Short Managed Money Ratio (Crude and Products) (Right) |
| ---------- | --------------------------------- | ------------------------------------------------------------- |
| Jul 2024   | ~85                               | ~3.5                                                          |
| Oct 2024   | ~75                               | ~1.5                                                          |
| 2025       | ~80                               | ~3.0                                                          |
| Apr 2025   | ~70                               | ~1.0                                                          |
| Jul 2025   | ~75                               | ~2.5                                                          |
| Oct 2025   | ~65                               | ~1.5                                                          |
| 2026       | ~60                               | ~1.0                                                          |
| Apr 2026   | ~115                              | ~5.0                                                          |
| Jul 2026   | ~90                               | ~3.0                                                          |
</details>

Source: CFTC, ICE, GS Global Investment Research

First, on the physical side, the global oil market deficit during the disruption has been less large than expected. Second, on the financial side, investor positioning has moderated as market concerns about major escalation and large damage to production capacity have eased since the “ceasefire” (Exhibit 1).

In this Oil Analyst, we keep our 2026Q4 Brent \$90 price forecast because the easing effect from a smaller-than-expected deficit during the Hormuz disruption so far offsets the tightening effect from a longer disruption (Exhibit 2). We lower our 2027 average Brent forecast by \$5 to \$80 on higher supply and lower demand.

Exhibit 2: We Maintain Our 2026Q4 Brent Oil Price Forecast at \$90 But Reduce Our 2027 Average Forecast by \$5 to \$80  
![](images/6893bf003a11daa9da2b4e74ef7b28df7ea6dccf9dbf95c22eeca13bff7543c4.jpg)

<details>
<summary>line chart</summary>

| Month | Realized | GS Forecast (Old) | Forwards (Nearby Contract Traded That Month) | GS Forecast (New) |
|-------|----------|-------------------|-----------------------------------------------|-------------------|
| May   | 78       | 94                | 93                                            | 95                |
| Sep   | 64       | 91                | 88                                            | 90                |
| 2026  | 62       | 89                | 85                                            | 88                |
| May   | 105      | 95                | 93                                            | 95                |
| Sep   | 104      | 93                | 88                                            | 90                |
| 2027  | 103      | 91                | 85                                            | 88                |
| May   | 102      | 89                | 82                                            | 85                |
| Sep   | 101      | 87                | 80                                            | 82                |
| 2028  | 100      | 85                | 78                                            | 75                |
</details>

Source: ICE, GS Global Investment Research

## Same 2026Q4 Price Forecast

We maintain our 2026Q4 Brent crude price forecast because our 2026Q4 OECD commercial stocks forecast is roughly unchanged (Exhibit 3). While global visible and OECD commercial oil stocks have drawn less quickly than expected, we now expect draws to continue for a couple months longer as we now assume Gulf exports normalize by end-August (vs. end-June previously).

Exhibit 3: We Maintain Our 2026Q4 OECD Commercial Stocks Forecast as the Slower-Than-Expected Pace of Draws Roughly Offsets the Longer Expected Duration of Draws  
![](images/d8b3b2f375159dd86a49268cd73bb4bf42d608f4fc2c3cef850e80561722e17a.jpg)

<details>
<summary>line chart</summary>

| Year | Realized (mb) | GS Forecast (New) (mb) | GS Forecast (Old) (mb) |
|------|----------------|------------------------|------------------------|
| 2018 | ~3050          | -                      | -                      |
| 2020 | ~3250          | -                      | -                      |
| 2022 | ~2650          | -                      | -                      |
| 2024 | ~2800          | -                      | -                      |
| 2026 | ~2750          | ~2700                  | ~2650                  |
| 2028 | -              | ~3000                  | ~2900                  |
</details>

Source: GS Global Investment Research

Our crude price 2026Q4 forecast remains nearly \$30 higher than before the Hormuz shock because of 1) a \$19 net boost to spot prices vs. long-dated prices given large hits to Mideast production and commercial oil stocks (after lower demand, higher supply, and SPR releases) and 2) a \$9 boost to long-dated prices as the market is likely to continue to risk-adjust spare capacity for disruption risk (Exhibit 4).

Exhibit 4: A Nearly \$30 Boost From the Hormuz Shock to Brent Prices in 2026Q4 on Lower Commercial Stocks (Driven by Lower Gulf Production) and Higher Long-Dated Prices  
![](images/38a7fd006851b5fd4f60d9e2d34118e38004602f4ad2604963f876f776081c1d.jpg)

<details>
<summary>bar chart</summary>

GS 2026Q4 Brent Price Forecast
| Category | Value ($/bbl) |
|---|---|
| Pre-Hormuz Shock Forecast | 62 |
| Lower Persian Gulf Supply | 64 |
| Lower Global Demand | 21 |
| Higher US Supply | 3 |
| Higher Russia Supply | 4 |
| Other Supply Higher | 7 |
| Policy Response | 11 |
| Net Boost | 19 |
| Boost to Long-Dated Prices | 9 |
| New Forecast | 90 |
</details>

Source: GS Global Investment Research

We now see WTI averaging at \$85 in 2026Q4 (vs. \$83/bbl prior) as we now see a narrower Brent-WTI differential at \$5/bbl as high US exports and refinery runs have reduced US crude stocks.

## A Smaller Deficit During the Hormuz Disruption

We now estimate a 5-6mb/d deficit in Q2 during the disruption (vs. a 9-10mb/d Q2 deficit estimated in April). $^{1}$

This 5-6mb/d Q2 deficit is smaller than the 14-15mb/d hit to Mideast crude and NGL production because of nearly 5mb/d of oil demand losses, the nearly 3mb/d Q2 surplus we forecasted before the war, and the 1.5mb/d upgrade to global ex Mideast Q2 production since the war started (Exhibit 5).

We recently estimated that much of the estimated 4-5mb/d of global oil demand destruction is concentrated in China, the Middle East, and petrochemical feedstocks. While demand destruction estimates are uncertain, the nearly 4mb/d year-over-year recent decline in China crude import demand has been a key driver of the moderation in crude prices.

Exhibit 5: We Estimate a 5-6mb/d Q2 Deficit, Which Is Smaller Than the 14-15mb/d Hit to Mideast Production  
![](images/effbe5a843172959c6ba8bef2742e36241185383c83d630d247199818d01bd04.jpg)

<details>
<summary>bar chart</summary>

Reconciling 14-15mb/d Mideast Supply Loss With 5-6mb/d 2026Q2 Global Deficit
| Category | Tightening Effect (mb/d) | Easing Effect (mb/d) |
| :--- | :--- | :--- |
| Mideast Supply Downgrade Since War | 14.5 | |
| Surplus, Forecast as of Feb 22 | | -2.9 |
| Global ex Mideast Supply Upgrade Since War | | -1.5 |
| Global Demand Downgrade Since War | | -4.8 |
| Deficit, New Forecast | 5.4 | |
</details>

Source: GS Global Investment Research

## A Later Start to the Recovery in Mideast Supply

We now assume that oil exports from Gulf producers normalize by late August (vs. by late June previously). While the uncertainty around the August normalization assumption is very large (which has tilted client focus towards scenarios), this assumption seems broadly consistent with prediction markets pricing (see here and here).

This normalization in oil exports from Gulf producers to their pre-war level of 23mb/d may be achieved with a 13mb/d increase in Hormuz flows from current levels to just 70% of pre-war levels given current estimated 10mb/d of flows via Hormuz, and redirections via Yanbu, Fujairah, the Gulf of Oman, and Ceyhan (Exhibit 6).

Exhibit 6: Full Normalization in Oil Exports Requires Hormuz Flows to Recover to 70% of Pre-War Levels (Assuming Redirections Remain at Current Levels)  
![](images/f2fb6f189e76b988a7e9383f8d77e7a84dcbcfe2414c0055b52149a596f546a1.jpg)

<details>
<summary>bar chart</summary>

Estimating Hit to Oil Flows from Persian Gulf Countries
| Flow | Pre-War Flows (mb/d) | Flows Over Last 14 Days (mb/d) |
|---|---|---|
| Strait of Hormuz | 20.0 | -1.5 |
| Yanbu | 1.4 | -4.6 |
| Fujairah | 1.7 | -2.5 |
| Botas Ceyhan | 0.0 | -1.1 |
| Total | 23.1 | -0.1 |
| Net Hit | 13.3 | |
</details>

Yanbu is on the west coast of Saudi Arabia, bordering the Red Sea and connected to Saudi eastern oil fields via the East-West pipeline. Fujairah lies east (outside) of the Strait of Hormuz and is connected to Abu Dhabi's onshore fields via the Abu Dhabi Crude Oil Pipeline (ADCOP). The Gulf of Oman connects the Strait to the Arabian Sea (southeast). The Kirkuk-Ceyhan pipeline allows northern Iraqi crude to be pumped through Turkey to the Mediterranean sea.

Source: Kpler, S&P Global Commodities at Sea, GS Global Investment Research

While we now see a later start to the recovery in Mideast production (Exhibit 7), we think that most of lost supply is likely to recover in a few months and more quickly than consensus expects if the Strait reopens (Exhibit 8).

Exhibit 7: We Expect Recovery in Mideast Production to Begin Later But Occur at a Faster Pace  
![](images/cc4bea1d247193f833fa78c43de0c945f07a3b02c352222ad30673e899d9ef34.jpg)

<details>
<summary>line chart</summary>

| Year | New (mb/d) | As of Late April (mb/d) |
|------|------------|--------------------------|
| 2025 | 30.0       | 30.0                     |
| May  | 30.5       | 30.5                     |
| Sep  | 31.5       | 31.5                     |
| 2026 | 31.5       | 31.5                     |
| May  | 17.0       | 15.0                     |
| Sep  | 18.0       | 28.0                     |
| 2027 | 32.0       | 31.0                     |
| May  | 32.0       | 31.5                     |
| Sep  | 32.0       | 31.5                     |
| 2028 | 32.0       | 31.5                     |
</details>

Included countries: Iran, Iraq, Kuwait, Qatar, Saudi Arabia, United Arab Emirates. Liquids include crude oil and natural gas liquids (NGLs).

Source: OPEC Secondary Sources, GS Global Investment Research

We still see the availability of pipeline capacity to destock previously produced oil as the key constraint on reopen

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
