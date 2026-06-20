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
# GLOBAL MARKETS ANALYST

# Updating Our G10 Term Premium Estimates — Still High

We introduce new term premium estimates for G10 economies that utilize surveyed data on short rate expectations. These complement our existing estimates that are based purely on the yield curve.  
The new estimates that incorporate survey information typically show a lower and more stable term premium than those derived purely from market data. While both have value, we think the survey-based estimates likely better reflect the recent structural shift in rate expectations, and thus current levels of term premium in major bond markets.  
Japan is a clear illustration of the advantages of survey-based models. Yield curve-only estimates interpret almost the entirety of the yield curve steepening as a rise in term premium, whereas the inclusion of surveys better identifies the structural rise in policy rate expectations.  
Yield curve-only term premium estimates tend to be more volatile and better at gauging changes in real time. However, they also tend to be better predictors of future excess returns to owning duration over the medium term, which suggests that yield curve-only measures offer useful signals on future returns.  
We think understanding the variation and drivers of term premium is more important than the precise level for market participants. All our estimates show a rise in term premium in recent years, partially due to the combination of macro risks and bond supply.

## Loic Mathys

+44(20)7051-1664

loic.mathys@gs.com

GS International

## Friedrich Schaper

+1(917)343-3214

friedrich.schaper@gs.com

GS & Co. LLC

## George Cole

+44(20)7552-1214

george.cole@gs.com

GS International

## William Marshall

+1(212)357-0413

william.c.marshall@gs.com

GS & Co. LLC

## Updating Our G10 Term Premium Estimates — Still High

## Old Question, New Models

Rising global bond term premium has been a key feature of rates markets in recent years. To improve our analysis of term premium and its drivers, we introduce additional estimates to complement our current model. Our existing estimates are based purely on yield curve data, similar to the Adrian, Crump and Moench (ACM) model. Our new survey-based estimates are based on the Kim-Wright (KW) method, which uses survey information on short rate expectations to complement yield curve data. We roll out these estimates for each G10 curve, and will in future provide both survey-based and yield curve-only versions of the term premium estimates for each market. As we discuss below, we think that both models have value for market views, but that the new survey-based measures get a better grip on any structural shifts in rate expectations and as a result offer more economically intuitive measures for several markets.

Exhibit 1: Survey-based estimations currently sit below yield curve only term premium estimates ...  
![](images/d2147a46476100bd2f552b236ae4536fa8ef168a83a1ebd9abbe3ef598fe85b4.jpg)

<details>
<summary>line chart</summary>

| Year | Survey-based | Yield curve-only |
|------|--------------|------------------|
| 1990 | ~1.8%        | ~4.5%            |
| 1995 | ~1.5%        | ~3.5%            |
| 2000 | ~1.2%        | ~2.5%            |
| 2005 | ~1.0%        | ~2.0%            |
| 2010 | ~0.8%        | ~1.5%            |
| 2015 | ~0.5%        | ~1.0%            |
| 2020 | ~-0.5%       | ~-1.5%           |
| 2025 | ~0.5%        | ~1.5%            |
</details>

Source: GS Global Investment Research, Consensus Economics, Haver Analytics, Federal Reserve Board

Exhibit 2: ... and also show relatively more stability  
![](images/872ef89f12a3ff4200d9e58dcb97afb3b9870e0342b2b588ab334020fc75aba4.jpg)

<details>
<summary>line chart</summary>

| Year | Survey-based | Yield curve-only |
|------|--------------|------------------|
| 2000 | ~1.5%        | ~3.5%            |
| 2003 | ~1.3%        | ~3.0%            |
| 2006 | ~1.2%        | ~2.5%            |
| 2009 | ~1.4%        | ~3.5%            |
| 2012 | ~1.0%        | ~2.0%            |
| 2015 | ~0.5%        | ~-1.0%           |
| 2018 | ~0.3%        | ~-1.5%           |
| 2021 | ~0.5%        | ~-1.8%           |
| 2024 | ~0.8%        | ~1.2%            |
</details>

Source: GS Global Investment Research, Consensus Economics, Haver Analytics, Bloomberg

The approach of these models is qualitatively similar. They use information from the current yield curve – and surveys in the case of the KW method – to project forward estimates of the short rate path. This then allows us to build a spot curve based on these projections, usually described as the risk neutral rate expectations path. Essentially, the difference between the observed yield curve and this path is the term premium estimate of the model. Our new estimates are shown in (Exhibit 1, Exhibit 2, Exhibit 3, and Exhibit 4) for G4, and Exhibit 5 for the smaller G10 markets, with full details on method, input data and estimates in the Appendix.

Exhibit 3: UK survey-based estimates are the lowest among the G4, indicating an important part comes from high rates expectations  
![](images/639cbb44aa49f047f9d0d3be2be3c4732373fb3d9b75a67745a0ce566774f603.jpg)

<details>
<summary>line chart</summary>

| Year | Survey-based | Yield curve-only |
|------|--------------|------------------|
| 1997 | ~1.0         | ~3.0             |
| 2000 | ~0.5         | ~0.0             |
| 2003 | ~0.8         | ~1.5             |
| 2006 | ~0.6         | ~0.5             |
| 2009 | ~1.2         | ~4.0             |
| 2012 | ~1.0         | ~3.5             |
| 2015 | ~0.8         | ~2.5             |
| 2018 | ~0.5         | ~-1.0            |
| 2021 | ~0.3         | ~-1.5            |
| 2024 | ~0.7         | ~1.8             |
</details>

Source: GS Global Investment Research, Consensus Economics, Haver Analytics, Bloomberg

Exhibit 4: Using surveys shows that the rise in JGBs is not only a term premium story  
![](images/298842a52afd170870c1180ab79a42694eb593a9dc02e82077f40e374ab8b03c.jpg)

<details>
<summary>line chart</summary>

| Year | Survey-based | Yield curve-only |
|------|--------------|------------------|
| 1993 | ~1.5%        | ~4.0%            |
| 1996 | ~2.5%        | ~3.5%            |
| 1999 | ~0.0%        | ~2.0%            |
| 2002 | ~1.0%        | ~1.5%            |
| 2005 | ~1.5%        | ~1.8%            |
| 2008 | ~0.5%        | ~1.2%            |
| 2011 | ~0.8%        | ~1.0%            |
| 2014 | ~0.2%        | ~0.5%            |
| 2017 | ~-0.5%       | ~0.0%            |
| 2020 | ~-0.8%       | ~-0.2%           |
| 2023 | ~0.5%        | ~0.8%            |
| 2026 | ~1.0%        | ~2.0%            |
</details>

Source: GS Global Investment Research, Consensus Economics, Haver Analytics, Bloomberg

For most curves, our survey-based term premium estimates are lower and less volatile than the yield curve-only model. In the US, the survey-based approach estimates 10y term premium is 70bp, 40bp lower than the yield curve-only estimates. Similarly, in Europe the survey-based 10y term premium is around 15bp lower than yield curve-only estimates. The UK, which for most part of the last year had the highest term premium among the G4 (but has since been overtaken by Japan) by the yield curve-only estimates instead is showing the lowest level of term premium among peers on the survey-based estimates. The lower survey-based term premium therefore implies a higher rate expectation path for each market.

## Great Survey Expectations

In the yield-curve only estimates, expectations are inferred primarily from the information embedded in the yield curve itself. In the survey-based specification, survey data directly discipline the projections for the short rate. This matters because when surveys point to a lower-for-longer or a structural rise in the policy path, the survey-based model will attribute more of the shift in the level of long-dated yields to expected future short rates and less to term premium. The yield curve-only based estimates rely more heavily on the long-run mean as an anchor for rate expectations, making them considerably more sensitive to the estimation window. That results in less volatility in the survey-based term premium estimates versus the yield curve-only estimates (Exhibit 6).

Exhibit 5: Within some of the smaller G10 the level of term premium differs meaningfully depending on approach  
![](images/d91e2f482018ea8603132f067695b6129d8522b42e6799ca8aaf76fd43bd7ffe.jpg)

<details>
<summary>bar chart</summary>

Current G10 10y Term Premium Estimates
| Currency | Yield curve-only (bp) | Survey-based (bp) |
| :--- | :--- | :--- |
| AUD | 98 | 28 |
| NZD | 78 | 38 |
| CAD | 89 | 59 |
| CHF | 9 | -6 |
| SEK | 101 | -42 |
| NOK | 39 | 56 |
</details>

Source: GS Global Investment Research, Consensus Economics, Haver Analytics, Bloomberg

Exhibit 6: Our existing estimates of term premium are more volatile than survey-augmented estimates  
![](images/a9d87d8d08dfda04e885558b6873503813583ad90c9ea349fa0d09dd1d149ea0.jpg)

<details>
<summary>bar chart</summary>

Standard Deviation of Term Premium Estimates
| Currency Pair | Yield curve-only (bp) | Survey-based (bp) |
| :--- | :--- | :--- |
| USD | 5.8 | 3.1 |
| EUR | 4.4 | 1.4 |
| GBP | 6.1 | 1.6 |
| JPY | 3.4 | 3.2 |
</details>

Source: GS Global Investment Research

A recent illustration was the aftermath of the German debt brake reform in March 2025; the survey-based estimates reported a lower increase in term premium than the yield curve-only, as markets adjusted not just to higher bond supply, but also incorporated an upgraded growth outlook that justified a structurally higher path for real rates (Exhibit 7).

Exhibit 7: The debt brake removal might be a justification for higher real rates over time  
![](images/e6ac7b899cc455b8299ce95a946195cef5f667b60e1362885bd8e2b9bd95d295.jpg)

<details>
<summary>line chart</summary>

| Date     | Survey-based | Yield curve-only |
| -------- | ------------ | ---------------- |
| 2Jan25   | 0            | 0                |
| 22Jan25  | 5            | 15               |
| 11Feb25  | 5            | -5               |
| 3Mar25   | 10           | 40               |
| 23Mar25  | 15           | 50               |
| 12Apr25  | 10           | 40               |
</details>

Source: GS Global Investment Research

Exhibit 8: Including surveys suggests a larger role for rates expectations in the recent increase in JGB yields  
![](images/16e35e4197440d0449f21498e11a6a836aab90db1c80d5328d38793c7b37d4f1.jpg)

<details>
<summary>line chart</summary>

| Date    | Survey-based 10y JP rate expectations | Yield curve-only 10y JP rate expectations | Long-term survey JP short rate |
|---------|----------------------------------------|-------------------------------------------|--------------------------------|
| Dec-22  | -10                                    | 0                                         | 0                              |
| Jun-23  | -5                                     | 0                                         | -5                             |
| Dec-23  | 0                                      | 0                                         | 0                              |
| Jun-24  | 20                                     | 5                                         | 30                             |
| Dec-24  | 60                                     | 15                                        | 60                             |
| Jun-25  | 80                                     | 25                                        | 80                             |
| Dec-25  | 100                                    | 30                                        | 90                             |
| Jun-26  | 110                                    | 35                                        | 95                             |
</details>

Source: GS Global Investment Research, Consensus Economics

Another example of this is in Japan. Since 2023, surveyed policy rate projections have been rising alongside the convergence of longer-term inflation expectations towards $2\%$ . Market pricing of OIS swap rates have moved to similar or even higher levels on a two-to-five year horizon. At the same time, the JGB yield curve has steepened significantly alongside a shrinking BoJ balance sheet and the market repricing duration risk in Japan. The yield curve-only model attributes bear steepening to a rise in term premium—short rates are moving only gradually, and based on the prior history (especially in Japan) these models will usually not show a rise in future short rates without some clearer sign of rises in the near-term, too.

In contrast, our survey-based model shows a more substantial rise in rate expectations – and correspondingly a smaller rise in JGB term premium – given the surveyed expectations have risen substantially. (Exhibit 8).

## Survey-Based Estimates Capture Structural Shifts, but Yield Curve-Only Models Still Useful

The inclusion of surveys to estimate the expected short rate path is particularly helpful amid structural shifts in rate expectations that are less well picked up by yield curve models. We think that makes survey-augmented models more economically intuitive when judging the level of market expectations about future rates. At the same time, survey-based models can be slower to adjust to day-to-day changes in expectations given the lower frequency (usually monthly) of surveys – in the debt brake reform example above, that pickup in rate expectations became only visible once surveys for the month of March became available, with a notable delay.

We also find that the constraint imposed by the inclusion of surveys means that yield curve-only estimates tend to do a better job of predicting future excess returns to holding duration over the medium term (Exhibit 9 and Exhibit 10). This suggests that purely market-based term premium measures offer greater value for trading signals.

Exhibit 9: Term premium is typically a useful predictor of duration excess returns over medium horizons  
1y holding excess return of 10y UST vs term premium  
![](images/be81f5ff6ce6388e5f7b1731c52e6f6c6c969f4589e714e027eee115e57aff5f.jpg)

<details>
<summary>scatterplot</summary>

| 10y Term Premium at Purchase | 1y Excess Return of Holding 10y ZC UST |
| ---------------------------- | -------------------------------------- |
| -2                           | -5                                     |
| -1                           | 0                                      |
| 0                            | 5                                      |
| 1                            | 10                                     |
| 2                            | 15                                     |
| 3                            | 20                                     |
| 4                            | 25                                     |
</details>

Source: GS Global Investment Research, GS FICC and Equities

Exhibit 10: Yield curve-based (GS) approach better at predicting excess duration returns than survey-augmented estimates (KW)  
![](images/522ccbdf4cadec2784484d5e72aced51a10223a80ff133539effca7b99ee5028.jpg)

<details>
<summary>bar chart</summary>

G4 Average
| Holding Period, Months | Yield curve-only | Survey-based |
|---|---|---|
| 6 | 11 | 5 |
| 12 | 20 | 11 |
| 24 | 38 | 22 |
| 60 | 50 | 40 |
R-Squared Term Premium as Predictor of Excess Duration Returns G4 Average R-Squared
</details>

Source: GS Global Investment Research, GS FICC and Equities

The different approaches also show different responses to yield changes: for any given shock to the level of rates, the yield curve-only approach will result in a greater response in term premium than the survey-based estimates. The same holds true for a given steepening of the curve (Exhib

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
