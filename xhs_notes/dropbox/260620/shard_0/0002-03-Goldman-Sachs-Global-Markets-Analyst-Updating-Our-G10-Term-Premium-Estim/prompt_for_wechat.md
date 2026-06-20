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

The different approaches also show different responses to yield changes: for any given shock to the level of rates, the yield curve-only approach will result in a greater response in term premium than the survey-based estimates. The same holds true for a given steepening of the curve (Exhibit 11). Shifts in the curvature have no notable difference in impact on the different models. That helps to assess the relative behavior during rate shocks.

Exhibit 11: Yield curve models only show more responsiveness to shifts in level and slope Term premium sensitivity (in pp) to a 1-standard deviation change in PC1 and 2  
![](images/fe473810e6879b756d1261482d33dfc852e35e3f6ab7fc18a5a6e203afe0c24a.jpg)

<details>
<summary>bar chart</summary>

| Scenario | Yield Curve Only | Survey-Based | Yield Curve Only | Survey-Based |
| --- | --- | --- | --- | --- |
| PC1 - Yield Level | 1.52 | 1.01 | 1.03 | 0.55 |
| PC2 - Slope | 1.43 | 1.11 | 1.03 | 0.31 |
| PC1 - Yield Level | 1.07 | 0.58 | 0.85 | 0.31 |
| PC2 - Slope | 1.43 | 0.52 | 1.01 | 0.27 |
| PC1 - Yield Level | 1.11 | 0.52 | 0.85 | 0.40 |
| PC2 - Slope | 1.11 | 0.52 | 0.85 | 0.40 |
</details>

Source: GS Global Investment Research

## Term Premium Still High Regardless of Estimate

Although there are key level differences between the survey-based and yield curve-only term premium estimates, we would not emphasise the precise level of either model's output. In our view, the value of these term premium estimates is to isolate drivers of movements in interest rates, and better understand the drivers of term premium. Currently, almost all models in all curves show that term premia have risen and sit near local highs, even as the precise levels vary. This implies only modest rises in rate expectations in most markets. The exceptions are Australia, the UK and Japan, which have seen sharper increases in rate expectations especially in the survey-based estimates.

However, the rise in G10 term premium in recent years does reflect changes in these key macro drivers over the same period, namely cyclical risk, the rise in inflation risk, the rise in the level and volatility of interest rates, high bond supply and a reversal of central bank balance sheet expansion (Exhibit 12 and Exhibit 13). While elevated bond supply may still be contributing to higher term premium, recent swap spread widening points to macro explanations around growth, inflation and fiscal risks rather than just bond-specific weakness. In recent years we have found that term premium has remained elevated despite a decline in rates volatility – this high premium, low volatility combination points to a structural rise in duration risk premium beyond (counter)cyclical fluctuations, which typically affect term premium variation. In upcoming research we will dive deeper into the drivers and valuation of G10 term premium, using and expanding our existing suite of valuation frameworks.

Exhibit 12: G4 term premium has risen alongside shrinkin

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
