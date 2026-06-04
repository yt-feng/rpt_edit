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

# Deal or No Deal: Trading Oil & Rates Scenarios in Global Credit

## Executive Summary

A month ago, when market attention remained firmly focused on the Middle East conflict, we highlighted the evolving relationship between rates and credit as yields began to move higher globally. Our thesis - "rates are higher, but not by enough to materially derail public fixed rate credit yet" - has held: over the past two months, IG/HY spreads have tightened by 17/60bp in the US and rates volatility has fully normalized, reverting close to pre-conflict levels. By contrast, while spreads rallied 18/69bp in Europe, rates volatility still remains elevated at \~1.5std above its 1y avg. Despite renewed headlines of a US-Iran deal (echoing March), we see risks in rates as two-sided, but still skewed towards widening in credit. As long as a policy regime shift is not fully priced in the US and sticky inflation concerns remain contained, tight spreads can hold. However, weakening supply chain indicators raise the risk of a more meaningful widening ahead. Additionally, stretched valuations and positioning mean that any rates relief is unlikely to drive further spread tightening. Against this backdrop, we outline how to position in 3 different scenarios for rates, alongside the rationale for taking profit on our long Europe vs. US trade.

## 1. Why Have Credit Spreads Not Reacted to Higher Rates?

Credit spreads have remained broadly resilient to higher rates, as the underlying drivers of the move have not materially challenged the macro or micro backdrop. Initially, the rise in US 10yr yields was driven predominantly by higher real rates and term premia, rather than a more destabilising shift in inflation expectations or the policy outlook, which limited the transmission to spreads. At the same time, investors have leaned into the AI theme, reinforcing expectations of productivity gains and stronger long-term growth. More recently, however, the composition of the move has begun to shift, with early signs of a repricing in long-term inflation expectations. After an initial decline, it began to edge higher again as negotiations in the Middle East stall and investors increasingly view AI-driven capex as a potential upside risk to inflation - yet levels remain below 2.5%, still comfortably beneath thresholds that would pose a more challenging rates backdrop for credit. At the same time, investor discussions point to some fatigue in trading the conflict, with repeated shifts in headlines reducing conviction. Fundamentals remain supportive: a “not too hot, not too cold” inflation environment has underpinned nominal earnings growth, complemented by incremental support to consumption from US tax refunds. Finally, technicals have stayed constructive: liquidity in the system is still ample, while higher all-in yields continue to attract demand, particularly from overseas, helping to contain spread widening.

## 2. How and When Do Credit Spreads Adjust to Higher Rates?

In our view, US credit is unlikely to react meaningfully to higher rates until breakeven inflation moves into the 2.65-2.75% range, a threshold at which we think investors will begin to question the degree of inflation control and, by extension, the credibility of the current policy path. Despite lower than expected US CPI last week, recent dynamics in supply chains reinforce this risk, with indicators deteriorating sharply (UBS Global Supply Chain Stress Index +1.2std in March-April), pointing to renewed inflation persistence that could challenge the current benign narrative. So far, markets, which have been pricing a deal in risky assets, still price low odds of a sustained Fed hiking cycle; any change in this would likely trigger a repricing of the rates curve. In such a scenario, we think the transmission to credit would be non-linear: rather than reacting to marginal adjustments, spreads would widen more decisively under a regime shift in monetary policy, where the Fed delivers multiple hikes rather than an adjustment hike. By contrast,

## Global Strategy

Global

Julien Conzano

Strategist

julien.conzano@ubs.com

+44-20-7567 2067

Sachin Ganesh

Associate Strategist

sachin.ganesh@ubs.com

+1-212-713 1062

Matthew Mish, CFA

Strategist

matthew.mish@ubs.com

+1-203-719 1242

Henry Morrison-Jones

Strategist

henry.morrison-jones@ubs.com

+44-20-7901 6656

Bhanu Baweja

Strategist

bhanu.baweja@ubs.com

+44-20-7568 6833

in Europe, the ECB is set to hike rates next week and the market is already pricing in \~60bp of hike for 2026. Vulnerabilities appear more acute in the region, where weaker-than-expected growth, driven by the energy shock and limited signs of fiscal support for corporates, is not fully reflected in credit spreads.

## 3. How Much Further Can Spreads Tighten on a Rates Rally?

We see limited room for credit spreads to tighten from here in the event that rates rally. Although a peace deal could reduce short- to medium-term inflation expectations and lead to more dovish central bank messaging, we believe credit valuations already look stretched. On a 1-year basis, US IG/HY spreads are now at the 2nd/3rd percentiles, while EU IG/HY spreads are at 30th/11th percentiles. In US HY, valuations appear broadly stretched at the sector level as well, with 10 out of 16 key sectors trading at spreads below the 25th percentile, although we see slightly more dispersion across sectors in Europe. Additionally, investor positioning appears near extremes across both asset managers and CTAs, leaving limited room for further institutional buying in credit. Using S&P 500 futures as a proxy for credit positioning, we find that asset managers are net long at near-record levels (\~95th percentile over 10 years). Meanwhile, UBS's CTA positioning model shows that credit positioning had plateaued in May. Historically, CTA positioning has been negatively correlated with spread tightening following geopolitical resolutions, with the largest spread tightening occurring when CTAs had previously been short credit. Given that CTAs are already long credit, we therefore see limited scope for spreads to rally, even in the event of a near-term deal.

## 4. Update to Our Trade Portfolio

First, we would emphasise that the portfolio was repositioned early in the conflict to benefit from a higher for longer rates environment, with a clear focus on: (i) maintaining short duration in rates; (ii) anchoring longs in the front end of the credit curve (1-3yr IG); (iii) preserving high quality floating rate exposure (CLO AAA); and (iv) adding decompression trades as a downside hedge (short CDX HY vs. CDX IG). Second, we have actively traded the US vs. EU call year to date - closing our long Europe at the onset of the war, reopening it in early April, and capturing most of the rally back to tights. As of today, however, the valuation case has largely run its course. From a monetary policy perspective, we see materially higher risks of multiple ECB hikes (UBSe +50bp in 2026) relative to the Fed (UBSe -25bp in 2026), which has not reached neutral. In addition, we see (i) increasing EU sensitivity to energy prices, (ii) limited fiscal support (iii) downside risks to growth - even more so in the context of a new hiking cycle from the ECB, and (iv) elevated political uncertainty in Europe/UK as key risks to the view. As a result, we take profit on our Long EU IG vs. US IG spreads and will look to re-enter at more attractive levels.

## 5. Key Scenarios and Best Associated Trades

Given the elevated uncertainty among investors around both the trajectory of the Middle East conflict and the outlook for inflation, we believe that thinking about portfolio positioning in scenarios is the best approach, with our top trades varying across each. We outline three scenarios alongside their corresponding trade implications:

Scenario 1: Energy normalises but inflation proves sticky (oil down, rates up) - We like Short US IG Office REITs vs. Index (duration adj.) which offers attractive downside convexity to higher rates despite being marginally carry negative. Additionally, valuations in REITs broadly screen tight as the market has played the hard asset trade through the start of the year. During prior stress periods, office REITs consistently underperform vs. other REIT subsectors due to their long-duration cash flow structures, higher leverage vs. other REITs, and rising illiquidity premium in stress.

Scenario 2: Energy normalises and inflation proves transitory (oil down, rates down) - In this scenario, we believe the value lies more in Europe than in the US. We like a Long EU IG Airlines vs. Index, which offers significant convexity given the lack of repricing (\~14%) since the beginning of the rally in late March-26, positive carry and a slightly long duration structure.

Scenario 3: Strait stays disrupted and inflation proves sticky (oil materially up, rates up) - In this scenario, we would turn more bearish on the consumer which, thus far, has proven resilient despite clear signs of a K shaped economy during the latest round of earnings. We would be Short US HY Retail vs. Index, playing for spread underperformance due to a negative growth shock, with a duration neutral and carry positive structure.

Figure 1: Our supply chain stress indicator is surging again. The index rose 1.2 standard deviations in March–April; the second largest two-month increase since the pandemic induced increase in July 2020  
![](images/8fe6a28ee5ae080f5f372510e6d008ea04f04d95a90a14b25b9d51994d545e81.jpg)

<details>
<summary>line chart</summary>

| Date   | median | average | inter-quartile range (lower) | inter-quartile range (upper) |
|--------|--------|---------|------------------------------|-------------------------------|
| Apr14  | -0.5   | -0.3    | -0.8                         | 0.2                           |
| Jan16  | -0.7   | -0.9    | -1.0                         | 0.1                           |
| Oct17  | 0.8    | 0.6     | 0.4                          | 1.2                           |
| Jul19  | -0.2   | -0.5    | -0.8                         | 0.3                           |
| Apr21  | 5.0    | 5.8     | 4.5                          | 6.0                           |
| Jan23  | -0.8   | -0.6    | -1.2                         | 0.5                           |
| Oct24  | 1.5    | 1.8     | 1.0                          | 3.0                           |
| Jul26  | 1.8    | 2.5     | 1.5                          | 4.0                           |
</details>

Source: Haver, Bloomberg, UBS calculations

Figure 2: Initially\*, the rise in US 10yr yields was driven predominantly by higher real rates rather than a more destabilising shift in inflation expectations or the policy outlook, which limited the transmission to spreads  
![](images/a18f423ab0615a631ce3b6d7a34c3870fa700ffdd0fa913b3acf552fb72e3751.jpg)

<details>
<summary>bar chart</summary>

| Region | Maturity | Inflation | Real | Nominal |
|--------|----------|-----------|------|---------|
| US     | 2y       | -3        | 31   | 26      |
| US     | 5y       | -2        | 36   | 34      |
| US     | 10y      | -1        | 32   | 32      |
| US     | 30y      | 1         | 24   | 26      |
| EUR    | 2y       | -1        | 8    | 12      |
| EUR    | 5y       | 1         | 11   | 14      |
| EUR    | 10y      | 1         | 13   | 14      |
| EUR    | 30y      | 1         | 12   | 14      |
| UK     | 2y       | 16        | -5   | 10      |
| UK     | 5y       | 1         | 14   | 20      |
| UK     | 10y      | 0         | 18   | 20      |
| UK     | 30y      | -1        | 20   | 20      |
</details>

Source: Bloomberg, UBS. \*as of May 20

Figure 3: Oil & gas tankers passing through the Strait of Hormuz, in number of ships entering and exiting the Gulf. We saw some optimism in early April but negotiations are stalling  
![](images/acf816058e4dd7bd09df99c96eeba625dd36c85c61dce22ffec61c8af6d4c095.jpg)

<details>
<summary>stacked bar chart</summary>

| Date | Oil tankers | Oil product tankers | LPG carriers | LNG carriers |
|---|---|---|---|---|
| 01-Feb-26 | 15 | 10 | 5 | 30 |
| 04-Feb-26 | 20 | 15 | 10 | 45 |
| 07-Feb-26 | 25 | 20 | 15 | 50 |
| 10-Feb-26 | 30 | 25 | 20 | 55 |
| 13-Feb-26 | 35 | 30 | 25 | 60 |
| 16-Feb-26 | 40 | 35 | 30 | 55 |
| 19-Feb-26 | 45 | 40 | 35 | 50 |
| 22-Feb-26 | 50 | 45 | 40 | 45 |
| 25-Feb-26 | 55 | 50 | 45 | 40 |
| 28-Feb-26 | 60 | 55 | 50 | 35 |
| 03-Mar-26 | 10 | 5 | 5 | 10 |
| 06-Mar-26 | 5 | 5 | 5 | 5 |
| 09-Mar-26 | 5 | 5 | 5 | 5 |
| 12-Mar-26 | 5 | 5 | 5 | 5 |
| 15-Mar-26 | 5 | 5 | 5 | 5 |
| 18-Mar-26 | 5 | 5 | 5 | 5 |
| 21-Mar-26 | 5 | 5 | 5 | 5 |
| 24-Mar-26 | 5 | 5 | 5 | 5 |
| 27-Mar-26 | 5 | 5 | 5 | 5 |
| 30-Mar-26 | 5 | 5 | 5 | 5 |
| 02-Apr-26 | 10 | 10 | 10 | 10 |
| 05-Apr-26 | 10 | 10 | 10 | 10 |
| 08-Apr-26 | 10 | 10 | 10 | 10 |
| 11-Apr-26 | 10 | 10 | 10 | 10 |
| 14-Apr-26 | 10 | 10 | 10 | 10 |
| 17-Apr-26 | 10 | 10 | 10 | 10 |
| 20-Apr-26 | 10 | 10 | 10 | 10 |
| 23-Apr-26 | 10 | 10 | 10 | 10 |
| 26-Apr-26 | 10 | 10 | 10 | 10 |
| 29-Apr-26 | 10 | 10 | 10 | 10 |
| 02-May-26 | 10 | 10 | 10 | 10 |
| 05-May-26 | 10 | 10 | 10 | 10 |
| 08-May-26 | 10 | 10 | -10 | -10 |
| 11-May-26 | -10 | -10 | -10 | -10 |
| 14-May-26 | -10 | -10 | -10 | -10 |
| 17-May-26 | -10 | -10 | -10 | -10 |
| 20-May-26 | -10 | -10 | -10 | -10 |
The chart displays a stacked bar chart with categories labeled as 'Oil tankers', 'Oil product tankers', 'LPG carriers', and 'LNG carriers'. The x-axis represents dates from January to May in increments of two days, while the y-axis indicates the count or percentage of total occurrences for each category. The data is grouped by date, with each bar representing the cumulative count of occurrences for that specific category. There are no bars for any category, but labels above the bars indicate the corresponding categories. The chart is saved as a PNG file named 'oil' and is displayed on the right side.
</details>

Source: UBS Evidence Lab, includes content supplied by S&P Global Market Intelligence (Maritime & Trade)

Figure 4: Weak May PMIs suggest clear downside risk to Eurozone GDP growth in Q2. We see signs of inventory build up as companies try and anticipate further supply chain disruption  
![](images/69adc7360df097612e41b5e04b38d648392a7263f0fed4f2a0ca31c17327fbe6.jpg)

<details>
<summary>line chart</summary>

| Date   | PMI Manufacturing | PMI Services | PMI Composite |
|--------|-------------------|--------------|---------------|
| Jan16  | ~52               | ~53          | ~53           |
| Jan18  | ~60               | ~58          | ~57           |
| Jan20  | ~40               | ~40          | ~40           |
| Jan22  | ~63               | ~58          | ~60           |
| Jan24  | ~43               | ~53          | ~50           |
| Jan26  | ~52               | ~50          | ~48           |
</details>

Source: Copyright © 2026, UBS, S&P GlobalTM. All rights reserved.

Figure 5: From a monetary policy perspective, we see materially higher risks of multiple ECB hikes (UBSe +50bp in 2026) relative to the Fed (UBSe -25bp in 2026), which has effectively never reached neutral  
![](images/2387f9c3e985473e06ccba874cbe5106a485492da494ae27371da829e3f3d128.jpg)

<details>
<summary>bar chart</summary>

| Month | Fed | ECB |
|---|---|---|
| Feb-26 | -2.3 | -0.1 |
| Mar-26 | -1.9 | 0.4 |
| Mar-26 | -1.5 | -0.2 |
| Mar-26 | -0.8 | 1.3 |
| Mar-26 | 0.2 | 3.3 |
| Mar-26 | -0.4 | 2.9 |
| Apr-26 | -0.3 | 3.1 |
| Apr-26 | -0.5 | 2.3 |
| Apr-26 | -0.4 | 2.2 |
| Apr-26 | -0.3 | 2.9 |
| May-26 | -0.1 | 3.0 |
| May-26 | 0.3 | 3.0 |
| May-26 | 0.4 | 2.9 |
| May-26 | 0.8 | 2.3 |
| May-26 | 0.7 | 0.0 |
</details>

Source: Bloomberg, UBS

Figure 6: Global credit is unlikely to react meaningfully to higher rates until breakeven inflation moves into the 2.65-2.75% range, a threshold at which we think investors will begin to question the credibility of the current policy path  
![](images/3729a0f71f1d227c7410aa69e6829e3eb53fbc219401337544654f9052f1263f.jpg)

<details>
<summary>line chart</summary>

| Date   | 5y5y USD | 5y5y EUR (rhs) |
|--------|----------|----------------|
| Feb-26 | 2.3      | 2.1            |
| Apr-26 | 2.4      | 2.15           |
| May-26 | 2.5      | 2.2            |
</details>

Source: Bloomberg, UBS

Figure 7: Asset manager S&P 500 futures positioning, which we use as a proxy for broader risk positioning, currently sits near 10-year highs. We therefore see limited room for additional institutional buying in credit from here, even if rates rally  
![](images/15d73ce56073ffcf086dad621423cc11ccaa4e3706f5f36744822a1e6b82569c.jpg)

<details>
<summary>line chart</summary>

| Date   | S&P 500 Futures Asset Manager Net Positioning 10-Year Percentile |
|--------|---------------------------------------------------------------|
| May-16 | 0.1                                                           |
| May-17 | 0.3                                                           |
| May-18 | 0.9                                                           |
| May-19 | 0.4                                                           |
| May-20 | 0.9                                                           |
| May-21 | 0.8                                                           |
| May-22 | 0.1                                                           |
| May-23 | 0.3                                                           |
| May-24 | 0.9                                                           |
| May-25 | 0.8                                                           |
| May-26 | 0.9                                                           |
</details>

Source: UBS, Haver

Figure 8: Historically, the largest spread tightening following geopolitical resolutions has occurred when CTAs had previously been short credit. Current CTA longs in credit suggest limited tightening ahead, even if we see a resolution to the US-Iran conflict  
![](images/0f038fdffde0e8bdbb980e4f5c910764c5c03405e6030ad526c988a437ec74c4.jpg)

<details>
<summary>scatterplot</summary>

| CTA Positioning Prior to Resolution | CDX HY | iTraxx Xover |
| ----------------------------------- | ------ | ------------ |
| -0.6                                | -30    | 5            |
| -0.2                                | -35    | -25          |
| 0.1                                 | -20    | -10          |
| 1.0                                 | -10    | 0            |
</details>

Source: UBS, Bloomberg

Figure 9: USD IG - percentage of spread repricing per sector since Mar-26 peak. All sectors fully retraced (and more) the move wider in March

<table><tr><td></td><td>Repricing to Peak (Mar-30)

[中间内容因长度限制已省略]

y recommendations or opinions in such this publication or material are not made or provided to you, and (ii) to the maximum extent permitted by law (a) indemnify UBS and its associates or related entities (and their respective Directors, officers, agents and Advisors) (each a 'Relevant Person') for any loss, damage, liability or claim any of them may incur or suffer as a result of, or in connection with, your unauthorised reliance on this publication or material and (b) waive any rights or remedies you may have against any Relevant Person for (or in respect of) any loss, damage, liability or claim you may incur or suffer as a result of, or in connection with, your unauthorised reliance on this publication or material. Korea: Distributed in Korea by UBS Pte. Ltd., Seoul Branch. This report may have been edited or contributed to from time to time by affiliates of UBS Pte. Ltd., Seoul Branch. This material is intended for professional/institutional clients only and not for distribution to any retail clients. Malaysia: This material is authorized to be distributed in Malaysia by UBS Malaysia Sdn. Bhd (Capital Markets Services License No.: CMSL/A0063/2007). This material is intended for professional/institutional clients only and not for distribution to any retail clients. India: Distributed by UBS India Private Ltd. (Corporate Identity Number U67120MH1996PTC097299) 2/F, 3 North Avenue, Maker Maxity, Bandra Kurla Complex, Bandra (East), Mumbai (India) 400051. Phone: +912261556000. It provides brokerage services bearing SEBI Registration Number: INZ000259830; Merchant Banking services bearing SEBI Registration Number: INM000013101; and Research Analyst services bearing SEBI Registration Number: INH000001204. Name of Compliance Officer Mr Parameshwaran Shivaramakrishnan, Phone: +912261556151, Email: ol-ubs-sec-compliance@ubs.com Registration granted by SEBI, and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. UBS may have debt holdings or positions in the subject Indian company/companies. UBS may have financial interests (e.g. loan/derivative products, rights to or interests in investments, etc.) in the subject Indian company/companies from time to time. Within the past 12 months, UBS may have received compensation for non-investment banking securities-related services and/or non-securities services from the subject Indian company/companies. The subject company/companies may have been a client/clients of UBS during the 12 months preceding the date of distribution of the research report with respect to investment banking and/or non-investment banking securities-related services and/or non-securities services. With regard to information on associates, please refer to the Annual Report at: https://www.ubs.com/global/en/about\_ubs/investor\_relations/annualreporting.html The Research Annual Compliance Report for UBS India Private Limited is available on www.ubs.com/ubssi under Research tab. Taiwan: Except as otherwise specified herein, this material may not be distributed in Taiwan. Information and material on securities/instruments that are traded in a Taiwan organized exchange is deemed to be issued and distributed by UBS Pte. LTD., Taipei Branch, which is licensed and regulated by Taiwan Financial Supervisory Commission. Save for securities/instruments that are traded in a Taiwan organized exchange, this material should not constitute "recommendation" to clients or recipients in Taiwan for the covered companies or any companies mentioned in this document. No portion of the document may be reproduced or quoted by the press or any other person without authorisation from UBS. Indonesia: This report is being distributed by PT UBS Sekuritas Indonesia and is delivered by its licensed employee(s), including marketing/sales person, to its client. PT UBS Sekuritas Indonesia, having its registered office at Sequis Tower Level 22 unit 22-1,Jl.Jend. Sudirman, kav.71, SCBD lot 11B, Jakarta 12190. Indonesia, is a subsidiary company of UBS AG and licensed under Capital Market Law no. 8 year 1995, a holder of broker-dealer and underwriter licenses issued by the Capital Market and Financial Institution Supervisory Agency (now Otoritas Jasa Keuangan/OJK). PT UBS Sekuritas Indonesia is also a member of Indonesia Stock Exchange and supervised by Otoritas Jasa Keuangan (OJK). Neither this report nor any copy hereof may be distributed in Indonesia or to any Indonesian citizens except in compliance with applicable Indonesian capital market laws and regulations. This report is not an offer of securities in Indonesia and may not be distributed within the territory of the Republic of Indonesia or to Indonesian citizens in circumstance which constitutes an offering within the meaning of Indonesian capital market laws and regulations.

The disclosures contained in research documents produced by UBS AG, London Branch or UBS Europe SE shall be governed by and construed in accordance with English law.

UBS specifically prohibits the redistribution of this document in whole or in part without the written permission of UBS and in any event UBS accepts no liability whatsoever for any redistribution of this document or its contents or the actions of third parties in this respect. Images may depict objects or elements that are protected by third party copyright, trademarks and other intellectual property rights. © UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/3e72da55dee36c3d8d686dce6df0643027af10429a933e5a46a1fe0bb9882146.jpg)

## UBS
"""
