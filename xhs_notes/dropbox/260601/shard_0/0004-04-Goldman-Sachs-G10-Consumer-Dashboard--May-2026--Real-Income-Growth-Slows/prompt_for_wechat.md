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
1. `# 标题`：一句主判断，不超过 32 字。
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
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# G10 Consumer Dashboard: May 2026: Real Income Growth Slows in North America

We update our G10 consumer dashboard through April. G10 consumers generally continue to benefit from healthy balance sheets, but labor markets are more mixed, sentiment has worsened from already low levels following the start of the war in the Middle East, and we expect spending headwinds as higher energy prices erode real incomes in the next few months.

■ Household balance sheets remain strong. Household net worth as a share of income stands close to all time highs in the US, Japan and Australia, is around percentile 90 (P90) in Canada and the Euro area, and stands around P65 in the UK. Since we last published the dashboard, real net worth growth was little changed at P65 in the US and Japan (P65), P50 in the Euro area, and P40 in the UK, Canada and Australia. The saving rate declined to its lowest level since June 2022 in the US, and also declined in Canada (but remains elevated). Elsewhere, the saving rate remains elevated outside of Japan (Exhibit 10).

\- Consumer sentiment remains below its historical average across the G10 (Exhibit 13). In the US, the University of Michigan's index of consumer sentiment fell to its lowest level in the survey's history—with respondents mentioning that “high prices were eroding their personal finances”—and the Conference Board index of consumer confidence fell to its lowest level since May 2020, while the expectations component reached its lowest level since October 2011. In Australia, consumer sentiment improved by 3.5% but remains well below its historical average (83.0 vs 100.1).

Since we last published the dashboard, real income growth slowed in the US (P5)—partially reflecting a decline in payments from the Farmer Bridge Assistance program that had boosted personal income in March—and Canada (P20), moved sideways in the Euro area (P95), UK (P40) and Australia (P20) and improved in Japan (near all-time highs). In the UK, private sector pay growth slowed to $+3.0\%$ in March (vs. $+3.2\%$ in February) below consensus expectations. In Japan, basic wage growth for all workers slowed slightly but remained above $3\%$ ( $+3.2\%$ in March, vs. $+3.4\%$ ).

Real spending growth stands below historical averages across DMs, at P15 in Australia, P20 in the US, P35 in Canada, P40 in the Euro area and Japan and P45 in the UK. In Australia, nominal household spending declined by 1.1% mom in April, largely driven by a pullback in transport which the ABS noted “reflected widespread impacts and responses to the conflict in the Middle East”. In the US, real personal spending grew 0.1%, reflecting a 0.2% increase in real services

Megan Peters

+44(20)7051-2058

megan.l.peters@gs.com

GS International

spending but a $0.1\%$ decline in real goods spending. While spending growth has remained resilient so far (with real PCE growth tracking at a healthy $2.1\%$ year-over-year pace through March) we anticipate a slowdown in the months ahead as higher energy prices erode spending power.

Consumers benefit from healthy labor markets in the Euro area, Australia, and Japan, but labor markets have normalized in the US and are notably weaker in the UK and Canada. The unemployment rate is close to its historical low in the Euro area (6.2%), Japan (2.5%), and Australia (4.5%) but stands around P65 in the US (4.3%) P35 in the UK (5.0% 3mma) and P20 in Canada (6.9%). Since we last published the dashboard, the unemployment rate ticked down in the Euro area and Japan, moved sideways in the US and Japan, and increased in the UK, Canada and Australia.

\- Debt service ratios remain low by historical standards in the US (P75), the Euro area (P75), and Japan (P55) but are higher in Canada (P25), Australia (P40), and the UK (P45). House prices continued to decline in Canada (Exhibit 16). Outstanding mortgage debt growth stands above its historical averages in the US, Western Europe and Asia, but below in Canada.

Based on our percentile-based metrics, consumer health stands around P65 in the Euro area, followed by Japan and Australia around P50, the US around P45, and the UK around P40. Consumer health is weakest at around P30 in Canada. Since we last published the dashboard, our overall consumer health proxy deteriorated slightly in the UK.

We continue to expect a deterioration in overall DM consumer health in the next few months due to higher inflation and activity headwinds associated with the war in the Middle East.

# Consumer Snapshot

Exhibit 1: Balance Sheets Remain a Source of Strength, but Sentiment Is Weak   
![](images/21328dec9ae4ff2f5b72721753bb35c5e098810b112a98b6416200dd802e299c.jpg)

<details>
<summary>bar</summary>

Consumer Health Indicators: Latest Observations by Country
| Indicator | US (%) | Canada (%) | Euro area (%) | UK (%) | Japan (%) | Australia (%) |
|---|---|---|---|---|---|---|
| Real Spending Growth | 22 | 33 | 37 | 46 | 39 | 14 |
| Unempl. Rate* | 65 | 21 | 92 | 28 | 84 | 83 |
| Real Income Growth | 6 | 20 | 97 | 39 | 100 | 22 |
| Consumer Confidence | 9 | 9 | 9 | 25 | 14 | 8 |
| Debt Service Ratio* | 74 | 25 | 74 | 43 | 54 | 40 |
| Net Worth to Income Ratio | 99 | 92 | 88 | 63 | 100 | 100 |
| Real Net Worth Growth | 65 | 40 | 52 | 38 | 65 | 39 |
| Weighted Average of Percentiles | 44 | 28 | 66 | 41 | 51 | 48 |
</details>

\* Percentile is inverted. High percentiles correspond to positive outcomes (e.g., low unemployment). We compute the weighted average through April. Variables that are not observed or nowcasted for April are assumed to be unchanged relative to March when taking the average. We have excluded pension assets from UK net worth in measuring the net-worth-to-income ratio as of June 2025, see methodological notes below for further details. We have incorporated Morning Consult's Index of Consumer Sentiment in Canada as of October 2025.   
Source: Haver Analytics, GS Global Investment Research, Morning Consult

Exhibit 2: Real Income Growth Slowed in Canada but Improved in Japan; Real Spending Growth Worsened in Australia but Edged Up in Canada   
![](images/d1efcabd7ec09b7d38fdfa39b7ae6e22f8bfdcbed4a8db1fdddb5722af99b24b.jpg)

<details>
<summary>bar</summary>

Change in Percentile
| Indicator | Change in Percentile |
|---|---|
| Japan Real Income Growth | 42 |
| Japan Unemp. Rate* | 11 |
| Canada Real Spending Growth | 6 |
| Australia Unemp. Rate* | -5 |
| Australia Real Spending Growth | -20 |
| Canada Real Income Growth | -35 |
</details>

\* Percentile is inverted. High percentiles correspond to positive outcomes (i.e. low unemployment).   
Source: Haver Analytics, GS Global Investment Research

# Consumer Health Trends

Exhibit 3: Our Consumer Health Indicator Stands Around P45 in the US and P25 in Canada   
Consumer Health Indicators: North America   
![](images/060e3b5188a9e981b6774ff842d189500dd1ce3b9542a7607684696f99859b08.jpg)

<details>
<summary>line</summary>

| Country | Year | Weighted average of percentiles |
|---------|------|---------------------------------|
| US      | 2020 | ~65                             |
| US      | 2021 | ~78                             |
| US      | 2022 | ~45                             |
| US      | 2023 | ~55                             |
| US      | 2024 | ~60                             |
| US      | 2025 | ~45                             |
| US      | 2026 | ~43                             |
| Canada  | 2020 | ~58                             |
| Canada  | 2021 | ~68                             |
| Canada  | 2022 | ~77                             |
| Canada  | 2023 | ~55                             |
| Canada  | 2024 | ~50                             |
| Canada  | 2025 | ~45                             |
| Canada  | 2026 | ~30                             |
</details>

We compute the weighted average through April. Variables that are not observed or nowcasted for April are assumed to be unchanged relative to March when taking the average.   
Source: Haver Analytics, GS Global Investment Research

Exhibit 4: Our Consumer Health Indicator Stands Around P65 in the Euro Area and P35 in the UK   
Consumer Health Indicators: Western Europe   
![](images/dfc01531bcb005c20334cad4770889d8526ec17e29da52520c4a9d467854b28e.jpg)

<details>
<summary>line</summary>

| Year | Euro Area Weighted average of percentiles | UK Weighted average of percentiles |
|------|------------------------------------------|-----------------------------------|
| 2020 | ~70                                      | ~65                               |
| 2021 | ~80                                      | ~70                               |
| 2022 | ~55                                      | ~45                               |
| 2023 | ~45                                      | ~35                               |
| 2024 | ~55                                      | ~40                               |
| 2025 | ~70                                      | ~45                               |
| 2026 | ~65                                      | ~40                               |
</details>

We compute the weighted average through April. Variables that are not observed or nowcasted for April are assumed to be unchanged relative to March when taking the average.   
Source: Haver Analytics, GS Global Investment Research

Exhibit 5: Our Consumer Health Indicator Stands Around P50 in Japan and Australia   
Consumer Health Indicators: Asia Pacific   
![](images/908d7840192e3ed9146530e18820bda0511e5f60a936fd17726a0cf88c8b013a.jpg)

<details>
<summary>line</summary>

| Year | Weighted average of percentiles |
| ---- | ------------------------------ |
| 2020 | 60                             |
| 2021 | 30                             |
| 2022 | 75                             |
| 2023 | 45                             |
| 2024 | 55                             |
| 2025 | 40                             |
| 2026 | 50                             |
</details>

![](images/895fa43211584955f92a9cf4806dcc354bd1f3e9c65250f8008a5663182d0884.jpg)

<details>
<summary>line</summary>

| Year | Weighted average of percentiles |
| ---- | ------------------------------- |
| 2020 | ~45                             |
| 2021 | ~55                             |
| 2022 | ~75                             |
| 2023 | ~35                             |
| 2024 | ~45                             |
| 2025 | ~60                             |
| 2026 | ~48                             |
</details>

We compute the weighted average through April. Variables that are not observed or nowcasted for April are assumed to be unchanged relative to March when taking the average.   
Source: Haver Analytics, GS Global Investment Research

# Spending Indicators

Exhibit 6: Real Spending Growth Stands Close to Its Historical Mean in the US but Real Services GVA Growth Remains Subdued in Canada   
Monthly Spending Indicators: North America   
![](images/b01ef92b5169be499c5c7e9e4e8f9a7b40481fe0427579819a324d83994fd3c9.jpg)

<details>
<summary>line</summary>

| Month | Real Personal Spending | Nominal Retail Sales ex. Gasoline Stations |
|-------|------------------------|---------------------------------------------|
| Jul   | ~0.5                   | ~3.8                                        |
| Aug   | ~0.8                   | ~2.0                                        |
| Sep   | ~1.0                   | ~1.2                                        |
| Oct   | ~0.5                   | ~-0.5                                       |
| Nov   | ~0.8                   | ~1.5                                        |
| Dec   | ~1.0                   | ~2.8                                        |
| Jan   | ~0.5                   | ~-1.5                                       |
| Feb   | ~0.8                   | ~-0.5                                       |
| Mar   | ~1.0                   | ~1.0                                        |
| Apr   | ~0.5                   | ~-0.5                                       |
| May   | ~0.8                   | ~1.5                                        |
| Jun   | ~1.0                   | ~2.5                                        |
| Jul   | ~0.5                   | ~-0.5                                       |
| Aug   | ~0.8                   | ~1.0                                        |
| Sep   | ~1.0                   | ~2.0                                        |
| Oct   | ~0.5                   | ~-0.5                                       |
| Nov   | ~0.8                   | ~1.5                                        |
| Dec   | ~1.0                   | ~2.5                                        |
| Jan   | ~0.5                   | ~-1.0                                       |
| Feb   | ~0.8                   | ~-0.5                                       |
| Mar   | ~1.0                   | ~1.0                                        |
| Apr   | ~0.5                   | ~-0.5                                       |
| May   | ~0.8                   | ~1.5                                        |
| Jun   | ~1.0                   | ~2.0                                        |
| Jul   | ~0.5                   | ~-0.5                                       |
| Aug   | ~0.8                   | ~1.0                                        |
| Sep   | ~1.0                   | ~2.5                                        |
| Oct   | ~0.5                   | ~-1.0                                       |
| Nov   | ~0.8                   | ~-0.5                                       |
| Dec   | ~1.0                   | ~1.5                                        |
| Jan   | ~0.5                   | ~-0.5                                       |
| Feb   | ~0.8                   | ~1.0                                        |
| Mar   | ~1.0                   | ~2.0                                        |
| Apr   | ~0.5                   | ~-1.0                                       |
| May   | ~0.8                   | ~-0.5                                       |
| Jun   | ~1.0                   | ~1.5                                        |
| Jul   | ~0.5                   | ~-0.5                                       |
| Aug   | ~0.8                   | ~1.0                                        |
| Sep   | ~1.0                   | ~2.5                                        |
| Oct   | ~0.5                   | ~-1.0                                       |
| Nov   | ~0.8                   | ~-0.5                                       |
| Dec   | ~1.0                   | ~1.5                                                        |
| Jan   | ~0.5                   | ~-0.5                                       |
| Feb   | ~0.8                   | ~1.0                                        |
| Mar   | ~1.0                   | ~2.0                                        |
| Apr   | ~0.5                   | ~-1.0                                       |
| May   | ~0.8                   | ~-0.5                                       |
| Jun   | ~1.0                   | ~1.5                                        |
</details>

Note: Dashed lines indicate the 2015-19 average growth rate.

![](images/791eefb0f1399205bd552938c191ef56277019bd5f76ac4da6508ba6cfb1c0aa.jpg)

<details>
<summary>line</summary>

| Month | Real Services GVA | Nominal Retail Sales ex. Gasoline Stations |
|-------|-------------------|---------------------------------------------|
| Jul   | ~0.5              | ~2.5                                        |
| 2023  | ~1.5              | ~2.8                                        |
| Jul   | ~0.5              | ~1.5                                        |
| 2024  | ~0.5              | ~1.0                                        |
| Jul   | ~0.8              | ~3.8                                        |
| 2025  | ~0.5              | ~3.5                                        |
| Jul   | ~0.3              | ~1.5                                        |
| 2026  | ~0.2              | ~1.8                                        |
</details>

Source: Haver Analytics, GS Global Investment Research

Exhibit 7: Real Retail Sales Growth Is Negative in the Euro Area and UK   
Monthly Spending Indicators: Western Europe   
![](images/964da332264ea5998d934f3a9f4ab239afc3afc37d14a3326b769f12c90fa6bd.jpg)

<details>
<summary>line</summary>

| Date       | Euro Area: Real Retail Trade ex: Motor Vehicles, Fuel | Germany: Real Services Turnover | France: Real Expenditure on Manufactured Goods | Spain: Real Retail Trade |
| ---------- | ---------------------------------------------------- | ---------------------------------- | --------------------------------------------- | ------------------------- |
| Jul 2023   | -1.5                                                 | 4.5                                | -2.0                                          | 2.0                       |
| Aug 2023   | -0.5                                                 | 2.0                                | -1.0                                          | 1.5                       |
| Sep 2023   | 0.0                                                  | 1.0                                | 0.5                                           | 0.0                       |
| Oct 2023   | -1.0                                                 | -1.5                               | -2.5                                          | -1.0                      |
| Nov 2023   | -2.0                                                 | 3.0                                | -3.0                                          | -2.0                      |
| Dec 2023   | -1.0                                                 | -1.0                               | -1.5                                          | -1.5                      |
| Jan 2024   | 0.5                                                  | 2.5                                | 0.0                                           | 1.0                       |
| Feb 2024   | -0.5                                                 | -1.0                               | -1.5                                          | -1.0                      |
| Mar 2024   | 1.0                                                  | 3.5                                | 0.5                                           | 1.5                       |
| Apr 2024   | -0.5                                                 | -1.5                               | -2.0                                          | -1.5                      |
| May 2024   | 0.5                                                  | 2.0                           

[中间内容因长度限制已省略]

e have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
