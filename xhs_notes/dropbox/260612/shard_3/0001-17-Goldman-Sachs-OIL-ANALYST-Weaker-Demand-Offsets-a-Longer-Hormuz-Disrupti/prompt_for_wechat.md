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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`GS`。标题格式建议：`# GS：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

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

We still see the availability of pipeline capacity to destock previously produced oil as the key constraint on reopening. In contrast, our research team's conversations with services companies suggest that the availability of materials and workers and well flow rates are unlikely to constrain production for most fields as producers appear to prepare a restart with ongoing drilling activity (Exhibit 9).

Exhibit 8: We Expect a Faster Rise in Production After Reopening Than Other Forecasters  
Crude Production from Persian Gulf Countries: Forecasts Comparison  
![](images/8efe88c7e722ce5012f4d830bee482340b2ada9cd3c13e2c78bfdb568f35d137.jpg)

<details>
<summary>line chart</summary>

| Month   | GS   | IEA  | EIA  |
|---------|------|------|------|
| Feb26   | 100  | 100  | 100  |
| Mar     | 80   | 60   | 70   |
| May     | 65   | 55   | 60   |
| Jul     | 65   | 60   | 60   |
| Sep     | 90   | 80   | 70   |
| Nov     | 100  | 90   | 80   |
| Feb27   | 105  | 95   | 85   |
</details>

IEA: Gulf Producers Total Liquids (Crude+NGLs) Supply  
EIA: OPEC + UAE Crude Production  
GS: Total OPEC + UAE Crude Production

![](images/8d8c9e8f0f7397cb05edd3aa1afc357d041d1fbde95833c5f16cc62f93cc4846.jpg)

<details>
<summary>line chart</summary>

| Month | Recovered Supply as % of Lost Supply | Cumulative Recovery |
|-------|--------------------------------------|---------------------|
| May   | 0                                    | 0                   |
| Jun   | 5                                    | 10                  |
| Jul   | 5                                    | 20                  |
| Aug   | 40                                   | 50                  |
| Sep   | 70                                   | 60                  |
| Oct   | 90                                   | 70                  |
| Nov   | 100                                  | 80                  |
| Dec   | 105                                  | 85                  |
</details>

Source: EIA, IEA, GS Global Investment Research

Exhibit 9: The Active Rig Count Has Increased Since the Start of the War in Saudi Arabia  
![](images/9b69a046ada2664e8119b38843477195b574adf5c5de26b6070e29c43fd0f332.jpg)

<details>
<summary>line chart</summary>

| Date   | Saudi Arabia | UAE  | Iraq |
|--------|--------------|------|------|
| Apr    | 310          | 60   | 60   |
| Jul    | 305          | 65   | 60   |
| Oct    | 295          | 70   | 60   |
| 2025   | 280          | 75   | 60   |
| Apr    | 275          | 75   | 60   |
| Jul    | 240          | 70   | 60   |
| Oct    | 235          | 80   | 60   |
| 2026   | 235          | 75   | 60   |
| Apr    | 260          | 70   | 60   |
| Jul    | 270          | 65   | 20   |
</details>

Last observation: May 2026.  
Source: Baker Hughes, GS Global Investment Research

We forecast liquids p

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
