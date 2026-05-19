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
# Global Strategy

# Rates Map - The real message of global yield curves

# Less central bank gradualism and higher energy prices have a real cost

Higher yields have been the path of least resistance for markets as policymakers have turned cautious on not just asset purchases but also forward guidance and will need time to digest the ongoing energy supply shock. Globally traded liquid bond markets are sending a relatively consistent message, even if the market may be underestimating cross-country differences in economic impact and central bank reaction functions (Figure 4). Last week, 10y rates rose even more than 2y rates, in a break with the underperformance of 2y bonds seen since the Iran conflict started. Investors want higher yields to hold duration risk. This is in line with Bernanke's view that a gradualist approach to monetary policy "may increase the ability of the Fed to affect long-term rates and thus influence economic behaviour." A less gradualist approach in favour of what Bernanke has called a "cold turkey" approach would then lead to higher long-term rates and more volatility.

# Japan re-joins the rates peloton and SNB pricing went to two hikes

Last week was a reminder that Japan has returned as an important driver to global bond markets (Figure 4). A total of 29 bps of Fed hikes is now priced by the Fed's March '27 meeting, but US 10y still rose to $4.60\%$ , crossing our Q2 forecast of $4.50\%$ . Meanwhile US 5y real rates, implied by Treasury Inflation-Protected Securities, rose 33 bps so far in May (to $1.55\%$ ) as the Fed is being repriced in line with stronger US data. Our takeaway from a range of meetings is that especially hedge funds had been positioning for the move higher in US rates and that April's US CPI validated this positioning. But SNB pricing also went to two hikes by Sep '27 as Swiss Q1 flash CPI was better than expected.

# German 10y vs US widens further

The stop on our long 10y bunds is 3.25% and we remain long. We think that the euro area is facing the larger adverse terms-of-trade shock and this limits how hawkish the ECB will get. We still forecast 10y US vs Germany to rise 150 (from 144 currently).

# Neutral on eur country spreads

We remain neutral on Italy, France and Spain against Germany but would not lean against further tightening in spreads. The European Commission is reviewing the escape clause for fiscal rules but we do not see a repeat of the fiscal support granted in the pandemic. That being said, we think that near-term EGB issuance could lead to some modest widening of sovereign rates versus swap rates as EGB issuance is running slightly below its 3y average, but we did not pick up material concerns on US or EUR funding markets in recent client meetings. German 30y yields (at 3.66%) are trading 40 bps above 30y EUR swap rates (at 3.26%), with the spread 17 bps higher year-to-date.

# UK 10y not a buy yet - Receiving June 'BoE

We have been telling clients not to go long UK 10y bonds as we think that political risks had been underpriced. The lesson from the mini budget of Liz Truss is that UK rates can price sharply higher on political uncertainty. There is more: the UK is an energy importer with inflation running above target for a while, so the bond market is also especially vulnerable to higher oil prices or higher US rates.

Clients have been asking how much gilt yields could reprice in response to political developments. As a reference point, we estimate that around 90bps of additional term premium was priced into 10-year gilts in 2022 following Liz Truss's mini-budget. However, at that time the BoE was in the middle of a rapid tightening cycle, which was also pushing up long-term rate expectations. Looking ahead, we think renewed fiscal

# Global Strategy

Global

Reinout De Bock

Strategist

reinout.de-bock@ubs.com

+44-20-7567 0152

Mustafa Oguz Caylan

Strategist

mustafa.caylan@ubs.com

+44-20-7901 5203

Bhanu Baweja

Strategist

bhanu.baweja@ubs.com

+44-20-7568 6833

concerns could add roughly 25–50bps to the term premium at the 10-year tenor from last week Monday's level of \~ 5% (more in the note here).

# Front-end - Stopped out of long SNB Sep '27 but unchanged otherwise

We continue to receive July ECB, June BoE, and 1y1y SEK vs US. We opened a long 1y1y SEK vs USD Tuesday 5 May given the persistent inflation undershoots vs target and relatively soft labour market in Sweden versus a drift up in US rate expectations. We move the target to 180 bps (from 165 bps) and put the new stop at 155 bps. We are also still paying Jun '27 vs Jun '28 Euribor.

# Curves - Adding UK 5s10s steepener to Japan steepener

We added a 5s10s steepener in UK to our 2s10s steepener in Japan (6 months forward). We see scope for a pick-up in rates volatility, some disinflationary impulse to the US economy and flatter 5s30s curve if Fed communication turns less gradualist under Kevin Warsh.

# Recent Notes

Weekly Supply - Deep dive on Euro issuance (15 May)

Client views - Oil vs Fed vs ECB vs Carry vs Political risk (14 May)

UK curve: Higher and steeper for longer (12 May)

2026 Outlook – Iran conflict meets hawkish US (11 May)

AI releases did not lower rates or reduce fiscal risks in '25-26 (8 May)

Not long 10y UK at 4.94% - Rate uncertainty, politics and oil (7 May)

Receive 1y1y SEK versus USD (5 May)

AI - No clear path to lower rates (5 May)

Receiving July ECB at 19 bps, still short June '27 vs June '28 Euribor (30 Apr)

US Refunding - Revising expected '26 coupon supply slightly lower (29 Apr)

Receive BoE June Meeting at 19 bps (29 Apr)

Warsh vs Bernanke Fed - More volatile rates ahead? (28 Apr)

UK Remit Revisions and Supply Chart Pack (23 Apr)

IMF Takeaways - Trading "one transitory shock after another" (20 April)

UK 10y higher for longer: 4.75% at end '26 (from 4.05%) (20 April)

End '26 Forecast: 10y US at 4.25% (4%) - bund at 2.75% (3%) (16 April)

# Summary of views

Figure 1: Open Trades 

<table><tr><td>Market</td><td>Position</td><td>Entry Date</td><td>Entry Level</td><td>Current Level</td><td>Target</td><td>Stop</td><td>Gain (bps)</td></tr><tr><td>USD</td><td>Long 2s7s10s SOFR butterfly</td><td>27-Mar-26</td><td>-8</td><td>1</td><td>-40</td><td>10</td><td>-9</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EUR</td><td>Receive July ECB</td><td>30-Apr-26</td><td>19</td><td>14</td><td>0</td><td>28</td><td>5</td></tr><tr><td>EUR</td><td>Long 10y EU vs Germany</td><td>27-Mar-26</td><td>35</td><td>34</td><td>20</td><td>45</td><td>1</td></tr><tr><td>EUR</td><td>Long 10y bunds (%)</td><td>26-Mar-26</td><td>3.00</td><td>3.17</td><td>2.75</td><td>3.25</td><td>-17</td></tr><tr><td>EUR</td><td>Pay June &#x27;27 Euribor vs receive June &#x27;28 Euribo</td><td>21-Mar-26</td><td>-3</td><td>-11</td><td>-30</td><td>-10</td><td>8</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>GBP</td><td>Long nominal 5s10s steepener</td><td>12-May-26</td><td>45</td><td>47</td><td>65</td><td>30</td><td>2</td></tr><tr><td>GBP</td><td>Receive BoE June Meeting</td><td>29-Apr-26</td><td>19</td><td>9</td><td>0</td><td>30</td><td>11</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>AUD</td><td>Receive 5y2y (%)</td><td>14-Jan-26</td><td>4.83</td><td>5.12</td><td>4.40</td><td>5.10</td><td>-29</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>JPY</td><td>Long 6m fwd 2s10s steepener</td><td>09-Feb-26</td><td>64</td><td>98</td><td>100</td><td>55</td><td>34</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SEK VS USD</td><td>Receive 1y1y SEK vs USD (%)</td><td>05-May-26</td><td>-1.31</td><td>-1.67</td><td>-1.80</td><td>-1.55</td><td>36</td></tr></table>

Source: Bloomberg, UBS. Note: Target extended and stop revised for SEK vs USD trade on 18-May-26

The Map is our summary on the rates outlook. We would like to thank Deepak Joy and Mehak Bhalla, our research support service professionals in our Hyderabad Research BSC, for assisting in preparing this research report.

# Charts of the week

Figure 2: Month-to-date nominal and real moves in May '26 so far   
![](images/f6eadf63549854b5ab1958e4da45daea0f6a0f5bed23ae74da319a9033a2678c.jpg)

<details>
<summary>bar</summary>

| Region | Maturity | Inflation | Real | Nominal |
|--------|----------|-----------|------|---------|
| US     | 2y       | -3        | 22   | 19      |
| US     | 5y       | -1        | 25   | 24      |
| US     | 10y      | 0         | 23   | 22      |
| US     | 30y      | 1         | 18   | 19      |
| EUR    | 2y       | -2        | 3    | 6       |
| EUR    | 5y       | 6         | 5    | 9       |
| EUR    | 10y      | 8         | 7    | 10      |
| EUR    | 30y      | 10        | 9    | 11      |
| UK     | 2y       | 15        | -8   | 8       |
| UK     | 5y       | 12        | 11   | 16      |
| UK     | 10y      | 16        | 15   | 17      |
| UK     | 30y      | -2        | 18   | 16      |
</details>

Source: Bloomberg, UBS

Figure 3: Apr- till now nominal and real moves   
![](images/c938adf87d3bc15c46340ceee42d9c2d5b43c903d26d269a6c3369320e383441.jpg)

<details>
<summary>bar_stacked</summary>

| Region | Maturity | Inflation (bps) | Real (bps) | Nominal (bps) |
| :--- | :--- | :--- | :--- | :--- |
| US | 2y | 27 | 1 | 27 |
| US | 5y | 28 | 8 | 32 |
| US | 10y | 21 | 12 | 29 |
| US | 30y | 14 | 16 | 26 |
| EUR | 2y | 33 | -24 | 9 |
| EUR | 5y | 24 | -14 | 11 |
| EUR | 10y | 14 | -2 | 14 |
| EUR | 30y | 15 | 8 | 16 |
| UK | 2y | 1 | 18 | 19 |
| UK | 5y | 26 | 22 | 27 |
| UK | 10y | 3 | 25 | 30 |
| UK | 30y | 30 | 30 | 31 |
</details>

Source: Bloomberg, UBS

Figure 4: Globally traded liquid yield curves - Japan re-joins the peloton   
![](images/30586c7e288438aae64baf2f59a5f0afb828bfb97af03c8e3a29de1a4b788579.jpg)

<details>
<summary>line</summary>

| Date   | UK 10y | AUD 10y | US10y | IT 10y | FR 10y | CAD 10y | ES 10y | DE 10y | SEK 10y | JP 10y | CNY 10y | Swiss 10y |
|--------|--------|---------|-------|--------|--------|---------|--------|--------|---------|--------|---------|-----------|
| Jan-90 | 13.0   | 12.5    | 9.0   | 8.5    | 8.0    | 7.5     | 12.0   | 9.5    | 8.5     | 6.0    | 7.0     | 7.5       |
| Jul-93 | 9.0    | 8.5     | 7.5   | 7.0    | 6.5    | 6.0     | 11.0   | 8.5    | 7.5     | 4.5    | 5.5     | 6.0       |
| Jan-97 | 7.0    | 6.5     | 6.0   | 5.5    | 5.0    | 4.5     | 9.0    | 6.5    | 5.5     | 3.0    | 4.0     | 4.5       |
| Jul-00 | 5.0    | 4.5     | 4.0   | 3.5    | 3.0    | 2.5     | 6.0    | 4.5    | 3.5     | 1.5    | 2.5     | 3.0       |
| Jan-04 | 3.0    | 2.5     | 2.0   | 1.5    | 1.0    | 0.5     | 4.0    | 2.5    | 1.5     | 0.5    | 1.5     | 2.0       |
| Jul-07 | 4.0    | 3.5     | 3.0   | 2.5    | 2.0    | 1.5     | 5.0    | 3.5    | 2.5     | 1.0    | 2.0     | 2.5       |
| Jan-11 | 6.0    | 5.5     | 4.5   | 4.0    | 3.5    | 3.0     | 7.0    | 5.5    | 4.5     | 2.0    | 3.0     | 3.5       |
| Jul-14 | 4.0    | 3.5     | 3.0   | 2.5    | 2.0    | 1.5     | 4.0    | 3.5    | 2.5     | 1.0    | 2.0     | 2.5       |
| Jan-18 | 2.0    | 1.5     | 1.0   | 0.5    | 0.0    | -0.5    | 2.0    | 1.5    | 1.0     | -1.0   | 1.0     | -0.5      |
| Jul-21 | 3.0    | 2.5     | 2.0   | 1.5    | 1.0    | 0.5     | 3.0    | 2.5    | 2.0     | -0.5   | 2.0     | -1.0      |
| Jan-25 | 4.0    | 3.5     | 3.0   | 2.5    | 2.0    | 1.5     | 4.0    | 3.5    | 3.0     | -1.0   | 3.0     | -1.5      |
</details>

Source: Bloomberg, UBS

Figure 5: 10y US vs Germany Spread moves across the Hormuz timeline   
![](images/fa65d0375fb00ed0eca3a5a9a1f791c1e4d8339420e4df942b5b2a5b1e22c06f.jpg)

<details>
<summary>line</summary>

| Date       | 10y US vs Germany (bps) |
| ---------- | ------------------------ |
| 20-Feb     | ~130                     |
| 2-Mar      | ~135                     |
| 12-Mar     | ~125                     |
| 22-Mar     | ~135                     |
| 1-Apr      | ~130                     |
| 11-Apr     | ~115                     |
| 21-Apr     | ~125                     |
| 1-May      | ~130                     |
| 11-May     | ~140                     |
</details>

Source: Bloomberg, UBS

Figure 6: Timeline on oil pricing   
![](images/eab3415900336658195ed656a087feb9a452b080da16c2f030aca95be4b6ecbc.jpg)

<details>
<summary>line</summary>

| Date       | WTI  | Brent | Dubai Oil | Oman Oil | Brent 6th Contract - Dec26 |
|------------|------|-------|-----------|----------|---------------------------|
| 20-Feb     | ~65  | ~70   | ~70       | ~70      | ~70                       |
| 2-Mar      | ~75  | ~80   | ~80       | ~80      | ~75                       |
| 12-Mar     | ~95  | ~100  | ~110      | ~140     | ~85                       |
| 22-Mar     | ~90  | ~110  | ~130      | ~160     | ~85                       |
| 1-Apr      | ~100 | ~110  | ~120      | ~120     | ~80                       |
| 11-Apr     | ~95  | ~95   | ~100      | ~100     | ~80                       |
| 21-Apr     | ~90  | ~95   | ~100      | ~105     | ~85                       |
| 1-May      | ~100 | ~115  | ~105      | ~105     | ~90                       |
| 11-May     | ~105 | ~105  | ~105      | ~105     | ~90                       |
</details>

Source: Bloomberg, UBS

Figure 7: UK Inflation prints hovering around 3% mark   
![](images/539d5975e475d830d2b50eface9a09714f6f620a3bbae1d6eef6053b25d687b9.jpg)

<details>
<summary>line</summary>

| Date    | UK CPI | UK Core | EZ Core HICP | US Core CPI |
|---------|--------|---------|--------------|-------------|
| Feb-91  | 9.0    | 8.5     | 7.0          | 6.0         |
| Feb-96  | 2.5    | 2.0     | 1.5          | 2.0         |
| Feb-01  | 1.0    | 0.5     | 0.0          | 1.5         |
| Feb-06  | 3.0    | 2.5     | 2.0          | 2.5         |
| Feb-11  | 5.0    | 4.5     | 3.5          | 4.0         |
| Feb-16  | 1.0    | 0.5     | 0.0          | 1.5         |
| Feb-21  | 10.0   | 8.0     | 6.0          | 7.0         |
| Feb-26  | 3.0    | 2.5     | 2.0          | 2.5         |
</details>

Source: Haver, UBS

Figure 8: ECB Receivers   
![](images/1f3410b0dc526d77620c80b03befc1cbbaf40ac3e99675f19abd74f916ce6698.jpg)

<details>
<summary>line</summary>

| Date    | ECB Apr26 (bps) | ECB Jul26 |
|---------|-----------------|----------|
| Oct-25  | -18             | -1              |
| Nov-25  | -7              | -1              |
| Dec-25  | -1              | 1                |
| Jan-26  | -1              | -1               |
| Feb-26  | -1              | -1               |
| Mar-26  | 5               | 10       |
| Apr-26  | 10              | 15       |
| May-26  | 1               | 14       |
</details>

Source: Bloomberg and UBS

Figure 9: We pay June '27 ECB vs receiving June '28 ECB. We think that the EURIBOR market will continue to back load cuts in the 2y "red" segment   
Euribor jun'27 jun'28 spread (so paying jun'27 vs receiving jun'28)   
![](images/feff554623c9ace27ed02cc35699fff187902f3cd4bdf49a9d00deed61bbb64d.jpg)

<details>
<summary>line</summary>

| Date    | ECB Deposit Rate | Generic 5th - 9th Euribor Future Spread (RHS) | Euribor Jun'27-Jun'28 Spread (RHS) |
|---------|------------------|-----------------------------------------------|------------------------------------|
| Jan-21  | -0.5             | 1.8                                           | -                                  |
| Nov-21  | -0.5             | 2.5                                           | -                                  |
| Sep-22  | 0.0              | 1.5                                           | -                                  |
| Jul-23  | 3.5              | 0.5                                           | -                                  |
| May-24  | 4.0              | 1.5                                           | -                                  |
| Mar-25  | 3.0              | 2.5                                           | 20                                 |
| Jan-26  | 2.0              | 1.0                                           | -10                                |
</details>

Source: Bloomberg and UBS.

Figure 10: YTD nominal and real moves   
![](images/e0b0bc6c5a3756b52a759e49f4ceffac20f27ed8c783c4d75c9bd60bddf386ea.jpg)

<details>
<summary>bar_stacked</summary>

| Region | Maturity | Inflation (bps) | Real (bps) | Nominal (bps) |
| :--- | :--- | :--- | :--- | :--- |
| US | 2y | 45 | -70 | -20 |
| US | 5y | 30 | -35 | -10 |
| US | 10y | 15 | -5 | 0 |
| US | 30y | 0 | 40 | 45 |
| EUR | 2y | 115 | -50 | 70 |
| EUR | 5y | 70 | 0 | 75 |
| EUR | 10y | 45 | 35 | 80 |
| EUR | 30y | 10 | 90 | 110 |
| UK | 2y | 25 | -20 | 10 |
| UK | 5y | 0 | 5 | 40 |
| UK | 10y | -5 | 60 | 60 |
| UK | 30y | 10 | 70 | 85 |
</details>

Source: Bloomberg, UBS

Figure 11: Central bank pricing - Market vs UBSe   
![](images/c975f56cb8831d3197dc8ddae2d206cc6e718208e3f54fc6857c2c50e1390625.jpg)

<details>
<summary>bar</summary>

|        | Market 2026 | Market 2027 | UBSe 2026 | UBSe 2027 |
| ------ | ----------- | ----------- | --------- | --------- |
| Fed    | 15          | -40         | -30       | -50       |
| ECB    | 80          | -5          | 50        | -30       |
| BoE    | 80          | -5          | 0         | -50       |
| SNB    | 20          | 30          | -5        | 30        |
| Riks   | 35          | 70          | -5        | 30        |
| BOJ    | 50          | 60          | 55        | 55        |
</details>

Source: Bloomberg, UBS

Figure 12: US market-based inflation expectations is expected to peak at 4.4% yoy in June '26 from 3.8% in April and 1y from now inflation (USSWIT1) is priced at 3.4%   
![](images/3b54a54834648727c4bfe5bb5d2a5a335181046b014ce1352e0803d53bd0898f.jpg)

<details>
<summary>line</summary>

| Date    | UBSe Core PCE | UBS PCE | UBS expected US CPI (yoy) | Market implied US CPI |
|---------|---------------|---------|---------------------------|----------------------|
| Oct-25  | ~2.8          | ~2.7    | ~2.8                      | ~2.9                 |
| Jan-26  | ~2.9          | ~2.8    | ~2.8                      | ~2.7                 |
| Apr-26  | ~3.3          | ~4.0    | ~4.0                      | ~4.4                 |
| Jul-26  | ~3.3          | ~3.8    | ~3.8                      | ~4.3                 |
| Oct-26  | ~3.0          | ~3.5    | ~3.5                      | ~3.8                 |
| Jan-27  | ~2.8          | ~3.0    | ~3.0                      | ~3.9                 |
| Mar-28  | ~2.0          | ~2.5    | ~2.5                      | ~3.0                 |
| Dec-

[中间内容因长度限制已省略]

ny recommendations or opinions in such this publication or material are not made or provided to you, and (ii) to the maximum extent permitted by law (a) indemnify UBS and its associates or related entities (and their respective Directors, officers, agents and Advisors) (each a 'Relevant Person') for any loss, damage, liability or claim any of them may incur or suffer as a result of, or in connection with, your unauthorised reliance on this publication or material and (b) waive any rights or remedies you may have against any Relevant Person for (or in respect of) any loss, damage, liability or claim you may incur or suffer as a result of, or in connection with, your unauthorised reliance on this publication or material. Korea: Distributed in Korea by UBS Pte. Ltd., Seoul Branch. This report may have been edited or contributed to from time to time by affiliates of UBS Pte. Ltd., Seoul Branch. This material is intended for professional/institutional clients only and not for distribution to any retail clients. Malaysia: This material is authorized to be distributed in Malaysia by UBS Malaysia Sdn. Bhd (Capital Markets Services License No.: CMSL/A0063/2007). This material is intended for professional/institutional clients only and not for distribution to any retail clients. India: Distributed by UBS India Private Ltd. (Corporate Identity Number U67120MH1996PTC097299) 2/F, 3 North Avenue, Maker Maxity, Bandra Kurla Complex, Bandra (East), Mumbai (India) 400051. Phone: +912261556000. It provides brokerage services bearing SEBI Registration Number: INZ000259830; Merchant Banking services bearing SEBI Registration Number: INM000013101; and Research Analyst services bearing SEBI Registration Number: INH000001204. Name of Compliance Officer Mr Parameshwaran Shivaramakrishnan, Phone: +912261556151, Email: ol-ubs-sec-compliance@ubs.com Registration granted by SEBI, and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. UBS may have debt holdings or positions in the subject Indian company/companies. UBS may have financial interests (e.g. loan/derivative products, rights to or interests in investments, etc.) in the subject Indian company/companies from time to time. Within the past 12 months, UBS may have received compensation for non-investment banking securities-related services and/or non-securities services from the subject Indian company/companies. The subject company/companies may have been a client/clients of UBS during the 12 months preceding the date of distribution of the research report with respect to investment banking and/or non-investment banking securities-related services and/or non-securities services. With regard to information on associates, please refer to the Annual Report at: https://www.ubs.com/global/en/about\_ubs/investor\_relations/annualreporting.html The Research Annual Compliance Report for UBS India Private Limited is available on www.ubs.com/ubssi under Research tab. Taiwan: Except as otherwise specified herein, this material may not be distributed in Taiwan. Information and material on securities/instruments that are traded in a Taiwan organized exchange is deemed to be issued and distributed by UBS Pte. LTD., Taipei Branch, which is licensed and regulated by Taiwan Financial Supervisory Commission. Save for securities/instruments that are traded in a Taiwan organized exchange, this material should not constitute "recommendation" to clients or recipients in Taiwan for the covered companies or any companies mentioned in this document. No portion of the document may be reproduced or quoted by the press or any other person without authorisation from UBS. Indonesia: This report is being distributed by PT UBS Sekuritas Indonesia and is delivered by its licensed employee(s), including marketing/sales person, to its client. PT UBS Sekuritas Indonesia, having its registered office at Sequis Tower Level 22 unit 22-1,Jl.Jend. Sudirman, kav.71, SCBD lot 11B, Jakarta 12190. Indonesia, is a subsidiary company of UBS AG and licensed under Capital Market Law no. 8 year 1995, a holder of broker-dealer and underwriter licenses issued by the Capital Market and Financial Institution Supervisory Agency (now Otoritas Jasa Keuangan/OJK). PT UBS Sekuritas Indonesia is also a member of Indonesia Stock Exchange and supervised by Otoritas Jasa Keuangan (OJK). Neither this report nor any copy hereof may be distributed in Indonesia or to any Indonesian citizens except in compliance with applicable Indonesian capital market laws and regulations. This report is not an offer of securities in Indonesia and may not be distributed within the territory of the Republic of Indonesia or to Indonesian citizens in circumstance which constitutes an offering within the meaning of Indonesian capital market laws and regulations.

The disclosures contained in research documents produced by UBS AG, London Branch or UBS Europe SE shall be governed by and construed in accordance with English law.

UBS specifically prohibits the redistribution of this document in whole or in part without the written permission of UBS and in any event UBS accepts no liability whatsoever for any redistribution of this document or its contents or the actions of third parties in this respect. Images may depict objects or elements that are protected by third party copyright, trademarks and other intellectual property rights. © UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/eb2552de8a39b17b40f811e4164cf6e41731760c24e889dfdac708f82c1b994c.jpg)

# UBS
"""
