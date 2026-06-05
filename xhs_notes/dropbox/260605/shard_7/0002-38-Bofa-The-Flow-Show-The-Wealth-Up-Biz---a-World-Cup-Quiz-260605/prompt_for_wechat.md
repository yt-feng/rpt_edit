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
# The Flow Show

# The Wealth Up Biz & a World Cup Quiz

Scores on the Doors: oil 60.7%, ACWI 14.6%, SPX 11.0%, gold 3.2%, HY bonds 1.8%, cash 1.5%, US\$ 0.9%, IG bonds 0.7%, govt bonds -0.4%, bitcoin -18.4% YTD.

Zeitgeist: “I got guys making \$200mn over the next four or five years. I'm constantly telling them that's not a lot of money based upon where you're starting,” Rich Paul, 2026.

Zeitgeist: “Central bankers around the world...seem more comfortable with inflation closer to 3% than I wish were the case. That’s very dangerous stuff. We can have an economic boom in that scenario, but there’ll be a high price to pay,” Kevin Warsh, 2024.

Tale of the Tape: soaring stocks, soaring wealth...US household equity wealth up \$6tn YTD (Chart 4 – calculated via BofA private client equity holdings), follows \$10tn gain in '25, \$9tn gain in '24; K-shape economy (and cyclicals) booming due to wealth-equity "boom loop", inflation flaring due to "wealth-price spiral"; not all consumers created equal, but voters are, and Trump inflation approval now below Biden lows.

The Price is Right: 46 out of 68 global central banks currently overshooting their inflation target and/or midpoint of their inflation target range (Table 1); central banks behind the curve...why yield curves bear flattening as CB hikes priced-in, why long-duration (XBT), leverage (private credit), EM FX (Indonesia rupiah, India rupee record lows, Korea won close to GFC & Asia crisis lows – Charts 5 & 6) all struggling.

The Biggest Picture: outside shot next week US unemployment rate (consensus 4.3%) equals/falls below inflation rate (CPI consensus 4.2%) for just 7 $^{th}$ time since 1960; years when inflation running close to or above unemployment rate (e.g., '66, '73, '90, '00, '08, '21), years of Fed hikes, and none remembered well on Wall St (Chart 2); note U-rate minus CPI has strong correlation with US yield curve, and points to inversion (Chart 3).

Chart 2: When unemployment lower than inflation...there be dragons   
US unemployment rate minus US headline CPI YoY %   
![](images/5f4a23f0c9a2fe6ff05cbeaf8cb066f4d9df5498769fdc33fbdd383a945131ca.jpg)

<details>
<summary>line</summary>

| Year | US unemployment rate minus US headline CPI (YoY %) |
| ---- | -------------------------------------------------- |
| Oct'66 | 0 |
| Feb'68 | 0 |
| Apr'73 | 0 |
| Dec'77 | 0 |
| Feb'90 | 0 |
| Mar'00 | 0 |
| Nov'07 | 0 |
| Jul'08 | 0 |
| Jul'21 | 0 |
| 2022 | -5 |
| 2026 | 0 |
</details>

Source: BofA Global Investment Strategy, Bloomberg   
BofA GLOBAL RESEARCH

More on page 2...

Trading ideas and investment strategies discussed herein may give rise to significant risk and are not suitable for all investors. Investors should have experience in relevant markets and the financial resources to absorb any losses arising from applying these ideas or strategies.

BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.

Refer to important disclosures on page 17 to 19.

12981561

05 June 2026

Investment Strategy Global

BofA

# Data Analytics

![](images/3154e44f8f1f9fc66480bfad2d261e50991d1a27872140aeeb837486e9a2bc22.jpg)

Michael Hartnett

Investment Strategist

BofAS

+1 646 855 1508

michael.hartnett@bofa.com

Anya Shelekhin

Investment Strategist

BofAS

+1 646 855 3753

anya.shelekhin@bofa.com

Myung-Jee Jung

Investment Strategist

BofAS

+1 646 855 0389

myung-jee.jung@bofa.com

Jessica Guo

Investment Strategist

BofAS

+1 646 855 0033

jessica.guo@bofa.com

Chart 1: BofA Bull & Bear Indicator   
Up to 8.7 from 8.5   
![](images/087de5e1f54939df9171c12705685b84765d7e6f1d599decc811ec4b003eae71.jpg)

<details>
<summary>gauge</summary>

| Sentiment | Value |
|---|---|
| Buy | 8.7 |
| Extreme Bearish | 0 |
| Sell | 10 |
</details>

Source: BofA Global Investment Strategy. The indicator identified above as the BofA Bull & Bear Indicator is intended to be an indicative metric only and may not be used for reference purposes or as a measure of performance for any financial instrument or contract, or otherwise relied upon by third parties for any other purpose, without the prior written consent of BofA Global Research. This indicator was not created to act as a benchmark.

BofA GLOBAL RESEARCH

The World Cup Quiz: 7 days to go before FIFA World Cup 2026 begins, the biggest tournament of the world's most popular sport; call it soccer, call it football, it's got 5 billion fans worldwide; in '26 the World Cup is hosted by the United States, Canada and Mexico and with 48 teams, 104 matches across 16 host cities, and expected attendance of 6.5 million people; the tournament is set to be the biggest global sporting event ever staged; read our BofA 2026 World Cup Guide for its surprisingly big macro, market, and AI impacts, but before then, test how well you know “the beautiful game” ahead of the Thursday, June $11^{\text{th}}$ kickoff at the Azteca stadium with our World Cup Quiz on page 6.

Weekly Flows: \$122bn to cash, \$39.0bn to bonds (record inflow), \$23.1bn to stocks, \$2.0bn from crypto (biggest since Nov'25), \$3.1bn from gold (biggest in 10 weeks).

# Flows to Know:

- IG bonds: \$20.1bn inflow, $2^{\text{nd}}$ biggest on record (Chart 10),   
• HY bonds: \$3.2bn inflow, biggest since May'25,   
• EM debt: \$6.3bn inflow, biggest in 6 weeks,   
• Bank loans: \$0.2bn outflow, first in 10 weeks,   
• US small cap: \$1.6bn inflow, biggest since Mar'26,   
• US growth: \$13.1bn outflow, biggest since Dec'25,   
• Consumer: \$1.7bn outflow, biggest since Dec'24,   
• Utilities: \$0.8bn inflow, biggest since Mar'26.

BofA Private Clients: \$4.6tn AUM...66.1% stocks (record high), 17.2% bonds (lowest since Mar'22), 9.6% cash (record high); largest weekly inflow to cash YTD but private client bid for stocks still strong...equity ETF share count up 0.2% past week, 0.7% MTD, 4.8% YTD; in ETFs past 4 weeks, private clients buying TIPS, munis, materials, selling utilities, low-vol, tech.

BofA Bull & Bear Indicator $^{1}$ : rises to 8.7 from 8.5 (3 $^{rd}$ week of “sell signal”) on strong inflows to HY & EM bonds, partially offset by widening AT1 spreads & slowing inflows to equities; 17 “sell signals” since '02, average loss for global stocks over 2-3 months is 2-3% (hit ratio of \~60%), with max drawdowns of 15-20% (see BofA Bull & Bear Indicator revamp - caveats always “tops are a process, lows are a moment”, i.e. greed harder to reverse than fear; BofA Global Breadth Rule (favorite high-frequency trading rule) shows 48% of global equity markets overbought (“sell signal” when net 88% trading >50dma & >200dma); most extreme overbought equity markets are Korea, Taiwan, Finland; most oversold are Indonesia (extreme), India, and China, and it’s the latter that will likely bounce the most on a proper US-Iran peace deal.

June Swoon Risks: booms, bubbles ended by bonds...June events that send 30-year bond yields in UK >6%, US >5%, Japan >4% likely -ve for risk assets given bullish Positioning & bullish Profit expectations, so watch...

- 5 $^{th}$ US payrolls: have averaged 150k past 2 months, after averaging -50k prior 12 months; May payrolls >125k & U-rate at/below 4.2% means US labor market reaccelerating sharply and GT30 yield to test 5¼% highs,   
- $10^{\text{th}}$ US CPI...up $0.6\%$ MoM past 3 months, up $0.4\%$ past 6 months; a May print above $0.4\%$ means US CPI $>4\%$ YoY (and on course for $5\%$ by US midterms) and risk assets get twitchy...past 100 years once CPI crosses $4\%$ on average SPX $-4\%$ next 3 months, $-7\%$ next 6 months. (Table 2 and Ground Control to Major TAM),

• 11 $^{th}$ ECB...98% prob of 25bps hike,   
- 16 $^{th}$ BoJ...83% prob of 25bps hike...needed to stop Japanese yen blowing through Maginot Line of 160 versus US dollar,   
- 17 $^{th}$ first Warsh FOMC...arguably one of the two most important June events; Warsh too dovish and long-end heads toward 6%; Warsh too hawkish and SPX pullback toward 7k; Goldilocks Warsh and best Wall Street barometer NYSE index (NYA) can decisively break to new all-time highs (>24,000).

A short history of IPOs: Table 3 shows price action in broad indices after top ten IPO launches of all time; Alibaba and ICBC IPOs were like rocket fuel for Chinese equities in following 3-12 months; NTT & ENEL were timed before big bear markets but big bear began a year later; in contrast, Visa & AIA were “toppy” IPOs, with SPX & Hang Seng much lower 9-12 months after launch; Aramco, Softbank, Facebook, GM launches were inconsequential for broader stock market.

A short history of Latin American & European politics: number of Latin America governments with right-leaning economic ideologies up to 10 of 19 after likely Peru/Columbia election outcomes this month (Chart 7), could rise to highest since 2003 if Brazil flips from Lula to Bolsonaro in Oct; shift right in LatAm politics why bond yields & spreads currently so low (USD-denominated LatAm govt & corp bond spreads 217bps, lowest since Nov'07) in historically inflationary LatAm; political shift to right also visible in Europe...last year 19 of 28 governments right-wing, highest level since 1990 (Chart 8).

Chart 3: U-rate minus CPI inflation pointing to yield curve inversion   
US unemployment rate minus CPI and 2s10s yield curve   
![](images/507aabce3e285fc88e6a1b958e015f71efaebb8eed60e9706954a5ede76cbe0f.jpg)

<details>
<summary>line</summary>

| Year | US unemployment rate minus US headline CPI (YoY %) | US 2s10s Curve (RHS) |
|------|--------------------------------------------------|------------------------|
| '78  | ~0                                               | ~0                     |
| '82  | ~-5                                              | ~-100                  |
| '86  | ~5                                               | ~50                    |
| '90  | ~0                                               | ~100                   |
| '94  | ~5                                               | ~150                   |
| '98  | ~0                                               | ~0                     |
| '02  | ~5                                               | ~100                   |
| '06  | ~0                                               | ~50                    |
| '10  | ~5                                               | ~150                   |
| '14  | ~0                                               | ~100                   |
| '18  | ~-5                                              | ~50                    |
| '22  | ~-10                                             | ~-100                  |
| '26  | ~0                                               | ~0                     |
</details>

Source: BofA Global Investment Strategy, Bloomberg   
BofA GLOBAL RESEARCH

Chart 4: US household equity wealth up \$6tn YTD... "boom loop"   
US household and BofA private client equity holdings (q/q change)   
![](images/899d7fc33af58d0d1a777f33b9b6218a9d71f725680f579ae1c8d50a0bf73615.jpg)

<details>
<summary>bar_line</summary>

| Year | US household equity holdings (q/q chg, $tn) | GWIM equity holdings (q/q, $bn) - RHS |
|------|-----------------------------------------------|----------------------------------------|
| '14  | ~1.5                                          | ~10                                    |
| '15  | ~0.5                                          | ~-5                                    |
| '16  | ~1.0                                          | ~-2                                    |
| '17  | ~1.5                                          | ~0                                     |
| '18  | ~1.0                                          | ~5                                     |
| '19  | ~1.5                                          | ~40                                    |
| '20  | ~6.0                                          | ~-80                                   |
| '21  | ~5.5                                          | ~30                                    |
| '22  | ~2.0                                          | ~-80                                   |
| '23  | ~2.5                                          | ~-20                                   |
| '24  | ~4.0                                          | ~100                                   |
| '25  | ~3.5                                          | ~-30                                   |
| '26  | ~5.5                                          | ~-50                                   |
</details>

Source: BofA Global Investment Strategy, Bloomberg   
BofA GLOBAL RESEARCH

Chart 5: Korea won close to GFC & Asia crisis lows   
Korean won spot (USD/KRW)   
![](images/111e94e73a38e4972ad59e6b85812211300b48b5fec0e6b902a9aa614083b78f.jpg)

<details>
<summary>line</summary>

| Year | Korean won |
| ---- | ---------- |
| Jun'26 | 1500 |
</details>

Source: BofA Global Investment Strategy, Bloomberg   
BofA GLOBAL RESEARCH

Chart 7: LatAm politics on course to shift more right in '26   
Political lean of Latin American country leaders since 1990   
![](images/b78df2a1e87faef6776f2b507a2a03c05fe277c101d27f8bdad2f3595000de0b.jpg)

<details>
<summary>bar_stacked</summary>

| Year | Rightist | Centrist | Leftist |
| ---- | -------- | -------- | ------- |
| '90  | 70%      | 10%      | 10%     |
| '93  | 75%      | 15%      | 10%     |
| '96  | 60%      | 15%      | 20%     |
| '99  | 65%      | 15%      | 15%     |
| '02  | 70%      | 15%      | 15%     |
| '05  | 55%      | 10%      | 25%     |
| '08  | 30%      | 5%       | 40%     |
| '11  | 20%      | 5%       | 50%     |
| '14  | 30%      | 5%       | 40%     |
| '17  | 40%      | 5%       | 30%     |
| '20  | 45%      | 5%       | 25%     |
| '23  | 40%      | 5%       | 30%     |
| '26  | 40%      | 5%       | 63%     |
</details>

Source: Herre, Bastian. 2023. Identifying Ideologues: A Global Dataset on Political Leaders, 1945-2020. British Journal of Political Science 53(2): 740-748.   
Note: 2026 assumes right-wing candidate wins in Peru and Colombia. LatAm = Brazil, Colombia, Argentina, Peru, Venezuela, Chile, Ecuador, Bolivia, Paraguay, Uruguay, Guyana, Suriname, Mexico, Guatemala, Honduras, Nicaragua, El Salvador, Costa Rica, Panama   
BofA GLOBAL RESEARCH

Chart 9: US CPI on course for >5% by November midterms   
Paths for US CPI assuming pace of monthly change   
![](images/d3c96a4f50ce4944aae93db0bfc257c7b599e8b085b5a43c647a6ed514cc09e6.jpg)

<details>
<summary>line</summary>

| Year | 0.1% MoM | 0.2% MoM | 0.3% MoM | 0.4% MoM | 0.5% MoM |
|------|----------|----------|----------|----------|----------|
| '20  | ~2.5%    | ~2.5%    | ~2.5%    | ~2.5%    | ~2.5%    |
| '21  | ~1.5%    | ~1.5%    | ~1.5%    | ~1.5%    | ~1.5%    |
| '22  | ~8.5%    | ~8.5%    | ~8.5%    | ~8.5%    | ~8.5%    |
| '23  | ~6.5%    | ~6.5%    | ~6.5%    | ~6.5%    | ~6.5%    |
| '24  | ~3.5%    | ~3.5%    | ~3.5%    | ~3.5%    | ~3.5%    |
| '25  | ~2.5%    | ~2.5%    | ~2.5%    | ~2.5%    | ~2.5%    |
| '26  | ~3.0%    | ~3.7%    | ~4.4%    | ~4.4%    | ~5.9%    |
| >26  | ~3.0%    | ~3.7%    | ~4.4%    | ~4.4%    | ~5.9%    |
</details>

Source: BofA Global Investment Strategy, Bloomberg   
BofA GLOBAL RESEARCH

Chart 6: Indonesian rupiah at record low   
Indonesia rupiah spot (USD/IDR)   
![](images/321f185679550c6e46547ce2837e0b0f8888e3a4b9033751a6dd9186b3e5abf2.jpg)

<details>
<summary>line</summary>

| Year | Indonesia rupiah |
| ---- | ---------------- |
| Jun'26 | 17000 |
</details>

Source: BofA Global Investment Strategy, Bloomberg   
BofA GLOBAL RESEARCH

Chart 8: 19 out of 28 govts in Europe were right-leaning in '25   
Political lean of European heads of government since 1990   
![](images/f8f4024263304cd67f746ae320f0a120bfab62152072627f378bac16df16f609.jpg)

<details>
<summary>bar_stacked</summary>

| Year | Rightist | Centrist | Leftist |
| ---- | -------- | -------- | ------- |
| '90  | 48%      | 32%      | 22%     |
| '93  | 45%      | 35%      | 25%     |
| '96  | 35%      | 30%      | 40%     |
| '99  | 38%      | 28%      | 32%     |
| '02  | 45%      | 25%      | 25%     |
| '05  | 50%      | 20%      | 20%     |
| '08  | 48%      | 22%      | 28%     |
| '11  | 55%      | 18%      | 15%     |
| '14  | 52%      | 20%      | 20%     |
| '17  | 48%      | 25%      | 25%     |
| '20  | 50%      | 28%      | 20%     |
| '23  | 58%      | 25%      | 15%     |
| '26  | 64%      | 20%      | 10%     |
</details>

Source: Herre, Bastian. 2023. Identifying Ideologues: A Global Dataset on Political Leaders, 1945-2020. British Journal of Political Science 53(2): 740-748.   
\*Europe = Austria, Belgium, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Ireland, Italy, Latvia, Lithuania, Luxembourg, Malta, Netherlands, Poland, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden, United Kingdom   
BofA GLOBAL RESEARCH

Chart 10: Second largest inflow to IG bonds on record   
IG bond fund flows vs 4 week moving average (\$bn)   
![](images/85380e52b8f2d5d7d14884fbc743d0e7a79d82ab3d41683572c60d29dcbe0696.jpg)

<details>
<summary>line</summary>

| Year | Corp IG flows ($bn) | Corp IG flows 4-week MA ($bn) |
|------|----------------------|-------------------------------|
| '17  | ~5                   | ~5                            |
| '18  | ~5                   | ~5                            |
| '19  | ~5                   | ~5                            |
| '20  | ~-60                 | ~-40                          |
| '21  | ~15                  | ~10                           |
| '22  | ~-10                 | ~-5                           |
| '23  | ~-5                  | ~0                            |
| '24  | ~10                  | ~5                            |
| '25  | ~-10                 | ~-5                           |
| '26  | ~20                  | ~15                           |
</details>

Source: BofA Global Investment Strategy, EPFR   
BofA GLOBAL RESEARCH

Table 1: 46 of 68 global central banks overshooting inflation target

Top 30 country inflation rates vs central bank inflation targets

<table><tr><td>Country</td><td>Central Bank</td><td>Inflation target*</td><td>Latest CPI</td><td>CPI vs. target</td></tr><tr><td>United States</td><td>Fed</td><td>2%</td><td>3.8%</td><td>1.8%</td></tr><tr><td>China</td><td>PBoC</td><td>2%</td><td>1.2%</td><td>-0.8%</td></tr><tr><td>Eurozone</td><td>ECB</td><td>2%</td><td>3.2%</td><td>1.2%</td></tr><tr><td>Japan</td><td>B

[中间内容因长度限制已省略]

ch information is distributed simultaneously to internal and client websites and other portals by BofA and is not publicly-available material. Any unauthorized use or disclosure is prohibited. Receipt and review of this information constitutes your agreement not to redistribute, retransmit, or disclose to others the contents, opinions, conclusion, or information contained herein (including any investment recommendations, estimates or price targets) without first obtaining express permission from an authorized officer of BofA.

Materials prepared by BofA Global Research personnel are based on public information. Facts and views presented in this material have not been reviewed by, and may not reflect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
