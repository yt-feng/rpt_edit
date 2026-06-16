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
# FOMC Roundtable

June 16-17 Meeting

June 2026

## The Recent Pick-Up in Job Growth Has Provided Reassurance About the Labor Market Outlook

![](images/019c13afc092020d8394d138054ef7fb58f84620bc7dddceaa027ab9b3f905f3.jpg)

<details>
<summary>bar chart</summary>

| Month    | Thousands per month | Underlying Trend Job Growth, GS Estimate* |
| -------- | ------------------- | ------------------------------------------ |
| Jan-24   | 205                 | -                                          |
| Feb-24   | 185                 | -                                          |
| Mar-24   | 210                 | -                                          |
| Apr-24   | 188                 | -                                          |
| May-24   | 158                 | -                                          |
| Jun-24   | 138                 | -                                          |
| Jul-24   | 128                 | -                                          |
| Aug-24   | 98                  | -                                          |
| Sep-24   | 148                 | -                                          |
| Oct-24   | 132                 | -                                          |
| Nov-24   | 168                 | -                                          |
| Dec-24   | 188                 | -                                          |
| Jan-25   | 165                 | -                                          |
| Feb-25   | 130                 | -                                          |
| Mar-25   | 75                  | -                                          |
| Apr-25   | 102                 | -                                          |
| May-25   | 58                  | -                                          |
| Jun-25   | 18                  | -                                          |
| Jul-25   | -10                 | -                                          |
| Aug-25   | -20                 | -                                          |
| Sep-25   | 5                   | -                                          |
| Oct-25   | -5                  | -                                          |
| Nov-25   | 38                  | -                                          |
| Dec-25   | 8                   | -                                          |
| Jan-26   | 60                  | 60                                         |
| Feb-26   | 25                  | 50                                         |
| Mar-26   | 50                  | 45                                         |
| Apr-26   | 75                  | 40                                         |
| May-26   | 130                 | 35                                         |
| Jun-26   | -                   | 30                                         |
| Jul-26   | -                   | 30                                         |
</details>

\* We estimate underlying trend job growth as 0.75\*3-month average payroll growth + 0.25\*9-month average household employment growth; see our report "How to Read the Employment Report."

![](images/05b715113da8e36e4f0980757b293660da703dc0be0d28592682a85b90de83c5.jpg)

<details>
<summary>line chart</summary>

| Date    | Unemployment Rate |
|---------|-------------------|
| Jan-23  | 3.5               |
| Oct-23  | 3.7               |
| Jul-24  | 4.2               |
| Apr-25  | 4.1               |
| Jan-26  | 4.5               |
| Oct-26  | 4.4               |
</details>

Source: GS Global Investment Research.

## The Combined Effect of Increases in Tariffs, Oil Prices, and Computer Memory Prices Is Likely to Hold Roughly Steady and Keep Year-over-Year Core PCE Inflation Above 3% All Year but Should Fade in 2027

![](images/203c2b000ad3bbfd5e6104e69ca13609fccbb8f90c0c15ee60fbd495bffdb2e5.jpg)

<details>
<summary>stacked bar chart</summary>

| Date | Tariff Effect (%) | Energy Effect (%) | Software & Access. Effect (%) |
| --- | --- | --- | --- |
| Jan-25 | 0.01 | 0.01 | 0.01 |
| Apr-25 | 0.03 | 0.04 | 0.03 |
| Jul-25 | 0.18 | 0.06 | 0.06 |
| Oct-25 | 0.38 | 0.09 | 0.09 |
| Jan-26 | 0.62 | 0.12 | 0.12 |
| Apr-26 | 0.84 | 0.15 | 0.15 |
| Jul-26 | 0.79 | 0.18 | 0.18 |
| Oct-26 | 0.62 | 0.21 | 0.21 |
| Jan-27 | 0.34 | 0.31 | 0.31 |
| Apr-27 | 0.18 | 0.37 | 0.37 |
| Jul-27 | 0.04 | 0.43 | 0.43 |
</details>

![](images/b38e61062905ec50a24436981cdea9e2429fcc55d822cdf7789ef724ca91157d.jpg)

<details>
<summary>line chart</summary>

| Date    | Year-Over-Year | 1-Month Annualized |
|---------|----------------|--------------------|
| Jan-24  | ~3.1           | ~6.5               |
| Jul-24  | ~2.8           | ~2.5               |
| Jan-25  | ~2.9           | ~5.5               |
| Jul-25  | ~2.8           | ~3.0               |
| Jan-26  | ~3.0           | ~5.2               |
| Jul-26  | ~3.3           | ~3.5               |
| Jan-27  | ~3.2           | ~2.5               |
| Jul-27  | ~2.2           | ~2.0               |
</details>

Source: GS Global Investment Research.

## We See Rate Hikes as Unlikely Because the Fed Tends Not to Hike in Response to Oil Shocks and Because the Oil Shock Is Less Likely to Spark Self-Sustaining High Inflation in a More Balanced Labor Market

![](images/42704bd8460d8ff16e4cfe74b51204b7490c9a38d0497675fed617873d15deb1.jpg)

<details>
<summary>bar chart</summary>

| Category | Fed | ECB |
|---|---|---|
| Higher Oil, Hawkish Words | 0.095 | 0.345 |
| Supply-Related Higher Oil, Hawkish Words | 0.025 | 0.365 |
</details>

![](images/d3fee97daa0e895e272455961a518ca91ae5a00c8e839d18b9be7daf1717bea4.jpg)

<details>
<summary>line chart</summary>

| Year | Wage Tracker* (left) | Slack Tracker (right, inverted, scaled to unemployment rate) |
|------|----------------------|---------------------------------------------------------------|
| 2000 | 5.0                  | 4.2                                                           |
| 2003 | 2.5                  | 3.0                                                           |
| 2006 | 3.8                  | 3.5                                                           |
| 2009 | 3.5                  | 3.0                                                           |
| 2012 | 1.5                  | 1.8                                                           |
| 2015 | 2.5                  | 3.0                                                           |
| 2018 | 3.5                  | 4.0                                                           |
| 2021 | 3.0                  | 1.0                                                           |
| 2024 | 5.5                  | 4.5                                                           |
| 2027 | 3.5                  | 3.0                                                           |
</details>

\*Adjusted for changes in the composition of the labor force between 2020Q1 and 2021Q4.

## Concerning Signals from Inflation Expectations or the Breadth of High Inflation Across Categories Would Make Hikes More Likely

![](images/6b01d99ac4538e735f251d1c49a0fcda5f2bac5bc413a20318b5cf5015dfa602.jpg)

<details>
<summary>line chart</summary>

| Year | Fed's Index of Common Inflation Expectations (Percent) | GS Estimate, Q2 Reading (Percent) |
|------|--------------------------------------------------------|------------------------------------|
| 2026 | 2.3                                                    | 2.3                                |
</details>

![](images/31504c844391d7237f9a191650d58a43223e852b3bf565dc3b42c5d910bc5b14.jpg)

<details>
<summary>area chart</summary>

| Year | >8% | 6-8% | 4-6% |
|------|-----|------|------|
| 1995 | ~15 | ~10 | ~5 |
| 1999 | ~15 | ~10 | ~5 |
| 2003 | ~20 | ~15 | ~10 |
| 2007 | ~30 | ~25 | ~20 |
| 2011 | ~15 | ~10 | ~5 |
| 2015 | ~5 | ~5 | ~5 |
| 2019 | ~10 | ~5 | ~5 |
| 2023 | ~65 | ~45 | ~35 |
| 2027 | ~20 | ~15 | ~10 |
</details>

Source: GS Global Investment Research.

## We Expect the FOMC to Shift to Balanced Guidance by Removing “the Extent and Timing of Additional” from Its Guidance, Though There Is Further Room to Simplify and Shorten the Statement

Recent indicators suggest that economic activity has been expanding at a solid pace. Job gains have remained lowpicked up, on average, and the unemployment rate has been little changed in recent months. Inflation is elevated, in part reflecting the recent increase in global energy prices.

The Committee seeks to achieve maximum employment and inflation at the rate of 2 percent over the longer run. Developments in the Middle East are contributing to a high level of uncertainty about the economic outlook. The Committee is attentive to the risks to both sides of its dual mandate.

In support of its goals, the Committee decided to maintain the target range for the federal funds rate at 3-1/2 to 3-3/4 percent. In considering the extent and timing of additional adjustments to the target range for the federal funds rate, the Committee will carefully assess incoming data, the evolving outlook, and the balance of risks. The Committee is strongly committed to supporting maximum employment and returning inflation to its 2 percent objective.

In assessing the appropriate stance of monetary policy, the Committee will continue to monitor the implications of incoming information for the economic outlook. The Committee would be prepared to adjust the stance of monetary policy as appropriate if risks emerge that could impede the attainment of the Committee's goals. The Committee's assessments will take into account a wide range of information, including readings on labor market conditions, inflation pressures and inflation expectations, and financial and international developments.

Source: GS Global Investment Research.

## The Economic Projections Are Likely to Show Lower GDP Growth, Slightly Lower Unemployment, and Considerably Higher Headline and Core Inflation in 2026

<table><tr><td colspan="5">Summary of Economic Projections</td></tr><tr><td></td><td>2026</td><td>2027</td><td>2028</td><td>Longer run</td></tr><tr><td colspan="5">Real GDP Growth*</td></tr><tr><td>GS Forecast</td><td>1.9</td><td>2.2</td><td>2.3</td><td></td></tr><tr><td>GS Forecast of June SEP</td><td>2.2</td><td>2.3</td><td>2.1</td><td>2.0</td></tr><tr><td>March SEP</td><td>2.4</td><td>2.3</td><td>2.1</td><td>2.0</td></tr><tr><td colspan="5">Unemployment*</td></tr><tr><td>GS Forecast</td><td>4.4</td><td>4.3</td><td>4.3</td><td></td></tr><tr><td>GS Forecast of June SEP</td><td>4.3</td><td>4.3</td><td>4.2</td><td>4.2</td></tr><tr><td>March SEP</td><td>4.4</td><td>4.3</td><td>4.2</td><td>4.2</td></tr><tr><td colspan="5">PCE Inflation*</td></tr><tr><td>GS Forecast</td><td>3.8</td><td>2.2</td><td>2.0</td><td></td></tr><tr><td>GS Forecast of June SEP</td><td>3.9</td><td>2.3</td><td>2.0</td><td>2.0</td></tr><tr><td>March SEP</td><td>2.7</td><td>2.2</td><td>2.0</td><td>2.0</td></tr><tr><td colspan="5">Core PCE Inflation*</td></tr><tr><td>GS Forecast</td><td>3.2</td><td>2.2</td><td>2.0</td><td></td></tr><tr><td>GS Forecast of June SEP</td><td>3.3</td><td>2.3</td><td>2.0</td><td></td></tr><tr><td>March SEP</td><td>2.7</td><td>2.2</td><td>2.0</td><td></td></tr><tr><td colspan="5">Fed Funds Rate* (Median)</td></tr><tr><td>GS Forecast</td><td>3.625</td><td>3.125</td><td>3.125</td><td></td></tr><tr><td>GS Forecast of June SEP</td><td>3.625</td><td>3.375</td><td>3.125</td><td>3.125</td></tr><tr><td>March SEP</td><td>3.375</td><td>3.125</td><td>3.125</td><td>3.125</td></tr><tr><td colspan="5">Addenda: Fed Funds Rate (Mean)</td></tr><tr><td>GS Forecast of June SEP</td><td>3.65</td><td>3.32</td><td>3.25</td><td>3.22</td></tr><tr><td>March SEP</td><td>3.35</td><td>3.19</td><td>3.19</td><td>3.16</td></tr></table>

\* Data shown are medians.  
Note: GDP growth and inflation forecasts are Q4/Q4. Unemployment is the Q4 average. The funds rate is the level at the end of the year.  
Source: GS Global Investment Research.

## We Expect the Median Dot to Show No Change in 2026 and One Cut in Each of 2027 and 2028

![](images/5de5a0a7225086626a28c27493e0f8485d9d7f9d6c332175bde4ff1a2205ddb5.jpg)  
Source: GS Global Investment Research.

## Our Baseline Fed Forecast Calls for Two Final Cuts in June and December 2027; Our Probability-Weighted Fed Forecast Remains More Dovish Than Market Pricing, Reflecting Our Skepticism of Hikes

![](images/a35df65c4960ee8da883b0a43d3716db574200b7ccdfb30e02af2e276d0a927a.jpg)

<details>
<summary>line chart</summary>

| Date    | Hikes (20%) | Higher Inflation / Growth / Terminal Rate (25%) | GS Baseline of Cuts in June & Dec. 2027 (30%) | Recession (25%) |
|---------|-------------|-----------------------------------------------|-----------------------------------------------|-----------------|
| Jan-24  |             |                                               | 5.4                                           |                 |
| Jul-24  |             |                                               | 5.4                                           |                 |
| Jan-25  |             |                                               | 4.4                                           |                 |
| Jul-25  |             |                                               | 4.4                                           |                 |
| Jan-26  |             |                                               | 3.6                                           |                 |
| Jul-26  |             |                                               | 3.6                                           | 3.6             |
| Jan-27  | 4.1         | 3.6                                           | 3.6                                           | 2.0             |
| Jul-27  |             |                                               | 3.4                                           | 1.0             |
| Jan-28  | 4.1         | 3.6                                           | 3.1                                           | 1.0             |
</details>

![](images/1a238371958a08bc790160206e608ef2389ec5ad0db4f80bf2063a930aa289f3.jpg)

<details>
<summary>line chart</summary>

| Date    | GS Baseline Path | GS Probability-Weighted Average Path | Market Pricing |
|---------|------------------|--------------------------------------|----------------|
| Jan-24  | 5.4              | -                                    | -              |
| Jul-24  | 5.4              | -                                    | -              |
| Jan-25  | 4.4              | -                                    | -              |
| Jul-25  | 4.4              | -                                    | -              |
| Jan-26  | 3.6              | 3.6                                  | 3.6            |
| Jul-26  | 3.6              | 3.6                                  | 3.6            |
| Jan-27  | 3.6              | 3.4                                  | 3.9            |
| Jul-27  | 3.4              | 3.1                                  | 3.9            |
| Jan-28  | 3.1              | 2.9                                  | 3.8            |
</details>

Source: GS Global Investment Research.

## Disclosure Appendix

June 15, 2026

## Disclosure Appendix

## Reg AC

We, Jan Hatzius, Alec Phillips, David Mericle, Ronnie Walker, Manuel Abecasis, Elsie Peng, Pierfrancesco Mei, hereby certify that all of the views expressed in this report accurately reflect our personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any 

[中间内容因长度限制已省略]

of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.fiadocumentation.org/fia/regulatory-disclosures\_1/fia-uniform-futures-and-options-on-futures-risk-disclosures-booklet-pdf-version-2018. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
