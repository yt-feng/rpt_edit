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
## US ECONOMICS ANALYST

# June FOMC Preview: Leadership Transition

The most important change in the economic data since the last FOMC meeting is the impressive pick-up in job growth that has put the labor market on a sturdier trajectory. This has left the focus on whether the inflation situation is becoming concerning enough to warrant a rate hike. The war and the increase in oil prices will likely drive headline PCE inflation above $4\%$ and leave core PCE inflation above $3\%$ all year. But so far the impact on inflation looks more like the usual passthrough from large oil shocks than the pandemic's wide-ranging shortages and price spikes.

We continue to see rate hikes as unlikely, both because the Fed has usually not hiked in response to oil price shocks in the past, and because conditions today, especially the more balanced state of the labor market, make it less likely that the oil shock will spark self-sustaining high inflation. That said, there have been some concerning signs already, and meaningful increases in inflation expectations or the breadth of high inflation across categories would make a hike more likely.

At its June meeting, the first under new Chairman Kevin Warsh, the FOMC is likely to keep the funds rate unchanged and drop the previous forward guidance suggesting cuts. We expect it to just remove from its post-meeting statement the phrase “the extent and timing of additional” in reference to adjustments to the funds rate, though there is plenty of room to simplify the statement further.

Consistent with the shift to balanced guidance, we expect the median dot to show no change to the funds rate in 2026, with three participants projecting a hike later this year. But we expect the median dot to still show two cuts eventually, most likely one in each of 2027 and 2028. A few neutral rate dots might rise, but the median is unlikely to increase. We assume that Warsh will not submit dots in light of his past criticism of forward guidance, but we are not sure.

The economic projections for 2026 are likely to show slightly lower GDP growth (-0.2pp to 2.2% Q4/Q4) and unemployment (-0.1pp to 4.3%) and much higher headline (+1.2pp to 3.9%) and core inflation (+0.6pp to 3.3%). We expect the 2027 inflation projections to rise by 0.1pp to 2.3%, implying that the consequences of the war for inflation will be limited beyond this year.

Because it will likely take quite a while for year-over-year core inflation to approach $2\%$ , we have penciled in the final two rate cuts in our forecast in June

## David Mericle

+1(212)357-2619

david.mericle@gs.com

GS & Co. LLC

and December 2027. A long pause would increase the probability that the FOMC could instead decide that the funds rate is already in an appropriate place if the economy continues to perform well, and we see a flat path as a plausible alternative to our baseline. Even so, our probability-weighted Fed forecast is meaningfully more dovish than market pricing, largely reflecting our skepticism of rate hikes.

Questions could come up in the press conference about Warsh's past criticisms of the Fed on themes including communications practices, balance sheet policy, and financial regulation. Our best guess is still that any changes to the first two will be limited, but this week's meeting should provide a better sense of Warsh's priorities and current thinking.

## June FOMC Preview: Leadership Transition

The most important change in the economic data since the last FOMC meeting is the impressive pick-up in job growth that has put the labor market on a much sturdier trajectory. While we still expect somewhat below-potential GDP growth in the second half of this year as high oil prices weigh on spending, we expect the unemployment rate to rise only a touch further to $4.4\%$ (Exhibit 1).

Exhibit 1: The Recent Pick-Up in Job Growth Has Provided Reassurance About the Labor Market Outlook  
![](images/fa923074406ba0a062758735d9c585ff44a17af3f30b0531c034094962aca22c.jpg)

<details>
<summary>bar chart</summary>

| Jan-24 | 208 |
| --- | --- |
| Feb-24 | 189 |
| Mar-24 | 213 |
| Apr-24 | 190 |
| May-24 | 160 |
| Jun-24 | 138 |
| Jul-24 | 129 |
| Aug-24 | 99 |
| Sep-24 | 150 |
| Oct-24 | 133 |
| Nov-24 | 168 |
| Dec-24 | 190 |
| Jan-25 | 165 |
| Feb-25 | 131 |
| Mar-25 | 76 |
| Apr-25 | 103 |
| May-25 | 59 |
| June-25 | -13 |
| Jul-25 | -30 |
| Aug-25 | -13 |
| Sep-25 | -3 |
| Oct-25 | -13 |
| Nov-25 | -3 |
| Dec-25 | -3 |
| Jan-26 | 61 |
| Feb-26 | 61 |
| Mar-26 | 61 |
| Apr-26 | 61 |
| May-26 | 61 |
| Jun-26 | 61 |
| Jul-26 | 50 (dashed line) |
</details>

\* We estimate underlying trend job growth as 0.75\*3-month average payroll growth + 0.25\*9-month average household employment growth; see our report "How to Read the Employment Report."

![](images/82f4d0897b09c597f44c647f99e0c51f5a7948a25e008009935069af1e78888a.jpg)

<details>
<summary>line chart</summary>

| Date   | Unemployment Rate |
|--------|-------------------|
| Jan-23 | 3.5               |
| Oct-23 | 3.7               |
| Jul-24 | 4.2               |
| Apr-25 | 4.1               |
| Jan-26 | 4.5               |
| Oct-26 | 4.4               |
</details>

Source: GS Global Investment Research, Department of Labor

The better labor market data allow the FOMC to focus on whether the inflation situation is becoming concerning enough to warrant a rate hike. The war and the increase in oil prices will likely drive headline PCE inflation above $4\%$ and leave core PCE inflation above $3\%$ all year, even as the effects of last year's tariff increases gradually drop out of the year-over-year calculation (Exhibit 2). But so far the impact on inflation looks more like the usual passthrough from large oil shocks than the pandemic's wide-ranging shortages and price spikes. We think that we have likely now moved through the most extreme effects of the increase in oil prices and in computer memory prices sparked by AI demand on the monthly pace of inflation, which we expect to decline in the remainder of the year.

Exhibit 2: The Combined Effect of Increases in Tariffs, Oil Prices, and Computer Memory Prices Is Likely to Hold Roughly Steady and Keep Year-over-Year Core PCE Inflation Above $3\%$ All Year but Should Fade in 2027  
![](images/83e2c702c399d9c47ca1b32418f45e0b78cfeb604317d8f2f6e691a8b87b3f5a.jpg)

<details>
<summary>bar chart</summary>

| Date    | Software & Acces. Effect | Energy Effect | Tariff Effect |
|---------|--------------------------|---------------|---------------|
| Jan-25  | 0.0                      | 0.0           | 0.0           |
| Jul-25  | 0.1                      | 0.0           | 0.1           |
| Jan-26  | 0.3                      | 0.1           | 0.3           |
| Jul-26  | 0.8                      | 0.4           | 0.8           |
| Jan-27  | 0.6                      | 0.3           | 0.6           |
| Jul-27  | 0.2                      | 0.2           | 0.2           |
</details>

![](images/7304234f1a78ca88d2ee4c5b0c502685dee3ba6ac3ac0f76b9343ee30e600f88.jpg)

<details>
<summary>line chart</summary>

| Date    | Year-Over-Year | 1-Month Annualized |
|---------|----------------|--------------------|
| Jan-24  | 3.0            | 6.5                |
| Jul-24  | 2.8            | 1.0                |
| Jan-25  | 3.0            | 5.5                |
| Jul-25  | 2.9            | 3.0                |
| Jan-26  | 3.1            | 5.2                |
| Jul-26  | 3.3            | 3.8                |
| Jan-27  | 3.2            | 2.5                |
| Jul-27  | 2.2            | 2.0                |
</details>

Source: GS Global Investment Research, Department of Commerce

## Rate Hikes Still Look Unlikely

We continue to see rate hikes as unlikely, for two main reasons. First, the Fed has usually not hiked in response to oil price shocks that looked unlikely to spark sustained high inflation historically, a difference with the reaction function of the ECB and other central banks (Exhibit 3, left). Second, conditions today, especially the more balanced state of the labor market and moderate starting point for wage growth (Exhibit 3, right), make it less likely that the oil shock will spark self-sustaining high inflation, at least if the effects of the war remain contained and oil prices follow roughly the path our strategists expect.

Exhibit 3: We See Rate Hikes as Unlikely Because the Fed Tends Not to Hike in Response to Oil Shocks and Because the Oil Shock Is Less Likely to Spark Self-Sustaining High Inflation in a More Balanced Labor Market  
![](images/162fd1d9db1d046c81f625ea681c60bb9c3ce87fa74f00cc3e9f6b09213a9ef9.jpg)

<details>
<summary>bar chart</summary>

Correlation Between Higher Oil Prices and Speech Hawkishness
| Category | Fed | ECB |
|---|---|---|
| Higher Oil, Hawkish Words | 0.1 | 0.34 |
| Supply-Related Higher Oil, Hawkish Words | 0.025 | 0.37 |
</details>

![](images/462f25b52ac4eaf48dba69e7259cc8c08ece57bb8f64224a4108bc4cfe923a2f.jpg)

<details>
<summary>line chart</summary>

| Year | Wage Tracker* (left) (%) | Slack Tracker (right, inverted, scaled to unemployment rate) (%) |
|---|---|---|
| 2000 | 5.0 | 4.2 |
| 2003 | 2.5 | 3.0 |
| 2006 | 3.8 | 3.5 |
| 2009 | 3.5 | 1.3 |
| 2012 | 1.5 | 1.8 |
| 2015 | 2.5 | 3.0 |
| 2018 | 3.5 | 4.0 |
| 2021 | 3.0 | 1.0 |
| 2024 | 5.5 | 4.5 |
| 2027 | 3.5 | 3.5 |
</details>

Source: GS Global Investment Research

That said, there have been some concerning signs already, including firmer PPI prints, large increases in the prices received components of the manufacturing surveys, and the now-reversed May spike in long-run Michigan inflation expectations. While we do not

see much risk of broad overheating, a longer war, higher oil prices, and more severe trade disruptions and supply shortages than we expect would raise the risk of pandemic-style inflation contagion, where initial shortage-driven price spikes make larger-than-usual price increases seem normal even to unaffected businesses. The clearest signs of drifting in that direction would be meaningful increases in either inflation expectations or the breadth of high inflation across categories (Exhibit 4), either of which would make a rate hike more likely.

Exhibit 4: Concerning Signals from Inflation Expectations or the Breadth of High Inflation Across Categories Would Make Hikes More Likely  
![](images/10cf478806ba0716ca28ca4c605381835b71c69a7f47d03dc76620e17ee279bf.jpg)

<details>
<summary>line chart</summary>

| Year | Fed's Index of Common Inflation Expectations (Percent) |
|------|--------------------------------------------------------|
| 1999 | 2.05                                                   |
| 2000 | 2.10                                                   |
| 2001 | 2.12                                                   |
| 2002 | 2.08                                                   |
| 2003 | 2.07                                                   |
| 2004 | 2.09                                                   |
| 2005 | 2.11                                                   |
| 2006 | 2.13                                                   |
| 2007 | 2.15                                                   |
| 2008 | 2.22                                                   |
| 2009 | 2.00                                                   |
| 2010 | 2.05                                                   |
| 2011 | 2.10                                                   |
| 2012 | 2.11                                                   |
| 2013 | 2.10                                                   |
| 2014 | 2.08                                                   |
| 2015 | 2.07                                                   |
| 2016 | 2.06                                                   |
| 2017 | 2.08                                                   |
| 2018 | 2.07                                                   |
| 2019 | 2.06                                                   |
| 2020 | 2.05                                                   |
| 2021 | 2.15                                                   |
| 2022 | 2.35                                                   |
| 2023 | 2.30                                                   |
| 2024 | 2.15                                                   |
| 2025 | 2.33                                                   |
| 2026 | 2.30                                                   |
</details>

![](images/0bc26b7243ce81b37fe9f5b224345314387acd163b3fe76513254b7fa04e948c.jpg)

<details>
<summary>area chart</summary>

| Year | >8% | 6-8% | 4-6% |
|------|-----|------|------|
| 1995 | ~10 | ~5   | ~5   |
| 1999 | ~15 | ~10  | ~10  |
| 2003 | ~20 | ~15  | ~15  |
| 2007 | ~30 | ~20  | ~20  |
| 2011 | ~15 | ~10  | ~10  |
| 2015 | ~5  | ~5   | ~5   |
| 2019 | ~10 | ~5   | ~5   |
| 2023 | ~65 | ~45  | ~40  |
| 2027 | ~20 | ~15  | ~15  |
</details>

Source: GS Global Investment Research, Federal Reserve, Department of Commerce

## The June Meeting

The June FOMC meeting will be the first under new Chairman Kevin Warsh. The FOMC is widely expected to keep the funds rate unchanged and drop the previous forward guidance suggesting cuts. We expect the FOMC to accomplish that by just removing the phrase “the extent and timing of additional” in reference to adjustments to the funds rate. But Exhibit 5 shows that there is plenty of further room to shorten and simplify the statement, which Warsh might prefer, because some sentences (pairs of which are highlighted in yellow and blue) partially overlap. The statement is also likely to acknowledge the pick-up in job growth in its first paragraph. We do not expect any dissents, though a dissent in favor of a hike is possible.

Exhibit 5: We Expect the FOMC to Shift to Balanced Guidance by Removing “the Extent and Timing of Additional” from Its Guidance, Though There Is Further Room to Simplify and Shorten the Statement

Recent indicators suggest that economic activity has been expanding at a solid pace. Job gains have remained lowpicked up, on average, and the unemployment rate has been little changed in recent months. Inflation is elevated, in part reflecting the recent increase in global energy prices.

The Committee seeks to achieve maximum employment and inflation at the rate of 2 percent over the longer run. Developments in the Middle East are contributing to a high level of uncertainty about the economic outlook. The Committee is attentive to the risks to both sides of its dual mandate.

In support of its goals, the Committee decided to maintain the target range for the federal funds rate at 3-1/2 to 3-3/4 percent. In considering the extent and timing of additional adjustments to the target range for the federal funds rate, the Committee will carefully assess incoming data, the evolving outlook, and the balance of risks. The Committee is strongly committed to supporting maximum employment and returning inflation to its 2 percent objective.

In assessing the appropriate stance of monetary policy, the Committee will continue to monitor the implications of incoming information for the economic outlook. The Committee would be prepared to adjust the stance of monetary policy as appropriate if risks emerge that could impede the attainment of the Committee's goals. The Committee's assessments will take into account a wide range of information, including readings on labor market conditions, inflation pressures and inflation expectations, and financial and international developments.

Source: GS Global Investment Research, Federal Reserve Board

The economic projections for 2026 are likely to show slightly lower GDP growth (-0.2pp to 2.2% Q4/Q4) and unemployment (-0.1pp to 4.3%) but much higher headline (+1.2pp to 3.9%) and core inflation (+0.6pp to 3.3%). A key question is how much the 2027 inflation projections will change, because this will give a sense of how concerned FOMC participants are that the latest in a series of inflation shocks will have long-lasting consequences. We expect both headline and core to rise 0.1pp to 2.3% (Exhibit 6).

Exhibit 6: The Economic Projections Are Likely to Show Lower GDP Growth, Slightly Lower Unemployment, and Considerably Higher Headline and Core Inflation in 2026

<table><tr><td colspan="4">Summary of Economic Projections</td><td rowspan="2">Longer run</td></tr><tr><td></td><td>2026</td><td>2027</td><td>2028</td></tr><tr><td>Real GDP Growth*</td><td></td><td></td><td></td><td></td></tr><tr><td>GS Forecast</td><td>1.9</td><td>2.2</td><td>2.3</td><td></td></tr><tr><td>GS Forecast of June SEP</td><td>2.2</td><td>2.3</td><td>2.1</td><td>2.0</td></tr><tr><td>March SEP</td><td>2.4</td><td>2.3</td><td>2.1</td><td>2.0</td></tr><tr><td>Unemployment*</td><td></td><td></td><td></td><td></td></tr><tr><td>GS Forecast</td><td>4.4</td><td>4.3</td><td>4.3</td><td></td></tr><tr><td>GS Forecast of June SEP</td><td>4.3</td><td>4.3</td><td>4.2</td><td>4.2</td></tr><tr><td>March SEP</td><td>4.4</td><td>4.3</td><td>4.2</td><td>4.2</td></tr><tr><td>PCE Inflation*</td><td></td><td></td><td></td><td></td></tr><tr><td>GS Forecast</td><td>3.8</td><td>2.2</td><td>2.0</td><td></td></tr><tr><td>GS Forecast of June SEP</td><td>3.9</td><td>2.3</td><td>2.0</td><td>2.0</td></tr><tr><td>March SEP</td><td>2.7</td><td>2.2</td><td>2.0</td><td>2.0</td></tr><tr><td>Core PCE Inflation*</td><td></td><td></td><td></td><td></td></tr><tr><td>GS Forecast</td><td>3.2</td><td>2.2</td><td>2.0</td><td></td></tr><tr><td>GS Forecast of June SEP</td><td>3.3</td><td>2.3</td><td>2.0</td><td></td></tr><tr><td>March SEP</td><td>2.7</td><td>2.2</td><td>2.0</td><td></td></tr><tr><td>Fed Funds Rate* (Median)</td><td></td><td></td><td></td><td></td></tr><tr><td>GS Forecast</td><td>3.625</td><td>3.125</td><td>3.125</td><td></td></tr><tr><td>GS Forecast of June SEP</td><td>3.625</td><td>3.375</td><td>3.125</td><td>3.125</td></tr><tr><td>March SEP</td><td>3.375</td><td>3.125</td><td>3.125</td><td>3.125</td></tr><tr><td>Addenda: Fed Funds Rate (Mean)</td><td></td><td></td><td></td><td></td></tr><tr><td>GS Forecast of June SEP</td><td>3.65</td><td>3.32</td><td>3.25</td><td>3.22</td></tr><tr><td>March SEP</td><td>3.35</td><td>3.19</td><td>3.19</td><td>3.16</td></tr></table>

\* Data shown are medians.  
Note: GDP growth and inflation forecasts are Q4/Q4. Unemployment is the Q4 average. The funds rate is the level at the end of the year.  
Source: GS Global Investment Research, Federal Reserve Board

Consistent with the shift to balanced guidance, the median dot is likely to show no change to the funds rate in 2026. We think that a few participants will project a h

[中间内容因长度限制已省略]

 have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

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

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
