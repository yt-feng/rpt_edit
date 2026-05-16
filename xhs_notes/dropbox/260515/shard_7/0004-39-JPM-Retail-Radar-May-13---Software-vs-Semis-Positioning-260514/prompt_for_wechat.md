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
# Retail Radar

# May 13 - Software vs Semis Positioning

As we will be hosting our flagship NY Quantitative & AI Conference on May 19-20, there will be no edition of the Retail Radar next week. If you are attending, we look forward to seeing you there in person.

# Retail Trading Activity Overview

- Last week's stronger retail buying proved short-lived, with purchases moderating again this week to just below their 12m average, as markets look ahead to the Trump–Xi meeting beginning tomorrow. Both ETF and single stock purchases were moderate, tracking around the 55%ile vs the past year's history.   
- Within ETFs, Tech-related names continued to be popular (e.g. QQQM: 4.2z and KWEB: 5.3z, Figure 8), although overall at lower volumes (see Equity Sector ETFs in Figure 15). Attention shifted toward copper, which continued to climb amid a rebound in Chinese demand, strong AI-driven fundamentals, and rising supply risks—most notably around Middle Eastern sulfur. Retail investors quickly traded around the theme, recording their largest single-day purchase in COPX on Tuesday (+6.7z), followed by profit-taking on Wednesday (-3.4z, Figure 10).   
- This month, breaking from prior patterns, retail investors have begun trimming their exposure to software stocks—particularly MSFT and PLTR. MSFT, for example, shifted from the $2^{nd}$ most-bought stock in April (behind TSLA) to the $2^{nd}$ most-sold MTD in May—and the most-sold last week. By contrast, retail investors have continued adding to semis positions this month: ETFs such as SOXX and SMH continue to see inflows (1.6z and 1.1z, respectively), while their buying into DRAM remained robust after more than quadrupling last week (report, Figure 6).   
- Looking at broader positioning on the theme, we refreshed our Software vs Semis Crowding analysis to assess how dislocated these two sectors are (Figure 1 and report) — and the distortion has only expanded further. It was supported by another leg of re-crowding in semis following a stellar earnings season for the group (+124% YoY earnings growth) and a resumption of the “risk-on” trade in April, all the while software positioning remained at lows despite good results (+25% earnings growth). In addition, retail crowding has continued to rise in semis while easing in software (for example, net selling MSFT and PLTR). Finally, shorts continue to build in software (100%ile, a squeeze risk), while remaining stable and lower in semis.   
- Earnings Season continues to deliver robust results, with Software companies (DDOG, FTNT, PTC, NET, APP) and Semis & Tech Hardware (COHR, AKAM, GEN, CDW, CSCO) broadly reinforcing strong fundamentals, see Single Stock Stories with Elevated Retail Activity and 1Q26 Earnings Update.

# Equity Strategy and Quantitative Research

Arun Jain AC

(1-212) 622-9454

arun.p.jain@JPM.com

JPM Securities LLC

Shizuka Suga, CFA AC

(1-212) 622-2134

shizuka.suga@JPM.com

JPM Securities LLC

Ana Pous Avila

(1-212) 622-0496

ana.pousavila@JPM.com

JPM Securities LLC

William Matheson

(1-212) 622-9538

william.matheson@jpmchase.com

JPM Securities LLC

Khuram Chaudhry

(44-20) 7134-6297

khuram.chaudhry@JPM.com

JPM Securities plc

Bhupinder Singh AC

(1-212) 622-9812

bhupinder.singh@JPM.com

JPM Securities LLC

Dubravko Lakos-Bujas AC

(1-212) 622-3601

dubravko.lakos-bujas@JPM.com

JPM Securities LLC

# Past Issues:

5/6 - Memory and AI, the Catch-Up Trade

4/29 - Peak Earnings, Peak Mag-7

4/22 - Towards a MEME Revival?

4/15 - Back to Average

4/8 - Not Buying Despite the Ceasefire

4/1 - In Defensive Mode

3/25 - Selling Rips

3/18 - From FOMO to FOHO: Fear Of Higher Oil

3/11 - Buying Oil, Selling Energy

3/4 - Cautiously Optimistic

2/25 - Balanced Optimism

2/18 - AI Software Averaging Down

2/11 - Positioning around Dislocations

2/4 - Softening Sentiment, Software vs Semis

1/28 - Earnings, Intl Equities, Precious Metals

1/21 - Unfazed through Vol Shock

1/14 - The January Effect?

1/7 - December Spree and a good start to January

12/10 - 2025 Retail Mania

12/3 - The Retail AI Trade

11/26 - Weekly Highlights

11/19 - 2025 Retail Mania: Dip-buying in AI

# Retail Trading Activity in Numbers for the Week: May 7 to May 13

- Retail flows were at \$6.4B this week, above the 12-month avg of \$6.6B/week. Retail investors continued to favor ETFs (+\$5.5B) over Single Stocks (+\$824M).   
- Outside of Broad Based Equity ETFs (+\$1.6B), retail ETF buying was influenced by Fixed Income — Multi Sector (+247M), Equity Sector Technology (+\$217M), Equity Style Dividend (+\$189M) and International Equity - EAFE (\$184M).   
- This week, and in line with prior weeks, retail investors continued to buy AI datacenters and electrification (JPAMAIDE), Growth, Top 30 AI/Datacenter Beneficiaries, Mag 7 and Growth, along with Fed Cut Outperformers, see Figure 12.   
- Activity in Mag7 this week: Retail investors bought: NVDA (+\$644M), TSLA (+\$275M), GOOGL/GOOG (+\$215M), META (+\$21M), AMZN (+\$17M) and sold AAPL (-\$8M) and MSFT (-\$117M).   
- Outside of Mag7, retail investors favored Tech (+\$460M) and Staples (+\$126M) and were net sellers of Financials (-\$282M), Communications (-\$174M) and Energy (-\$172M).   
- Top 5 retail stocks last week: NVDA (+\$644M), TSLA (+\$275M), SNDK (+\$227M), GOOGL/GOOG (+\$215M) and ASML (+\$122M). Bottom 5 retail stocks: MSFT (-\$117M, -1.0z), QCOM (-\$88M, -2.8z), RKLB (-\$84M, -3.6z), PLTR (-\$82M) and NFLX (-\$46M).   
- In options, retail share is still at highs, driven by calls in Tech, Figure 61 and Figure 63. The most traded options were in the following names, echoing previous weeks: TSLA, MU, NVDA, AMD, INTC, SNDK, GOOGL/GOOG, META, AAPL, MSFT and AMZN. For the most bought/sold delta and gamma names, see Retail Activity in Options. Also see Retail Investors Options Activity by Sectors.   
- Futures Activity (Non Retail): Over the past week, Futures traders net sold \~\$0.8B, primarily driven by net sales in RTY (\~\$0.9B) and ES (\~\$0.2B) partially offset by net buys in NQ (\~\$0.3B).

11/12 - Bullion to Silicon: AI Gold Rush Resumes
11/5 - Skipping the Dip, Earnings Stock Picking
10/29 - Reaching Peak-Earnings, AI, FOMC
10/22 - Sold GLD, onto New Memes and Earnings
10/15 - Trading around Tariffs, AI and Earnings
10/8 - Back after Summer Break
10/1 - Back to Stocks, Thematic ETFs, GLD Rush
9/24 - Precious Metals, Cyclicals and Domestic
9/17 - FOMC, Herding in OPEN and GRAB

Figure 1: Overall Crowding in Software and Semis   
As of May 12 $^{th}$   
![](images/577640396c1838d9fd5e133e4c5d947d63871ca5fc3eeff1699d6d38a56911e1.jpg)

<details>
<summary>line</summary>

| Year | Crowding in Software (cap-norm.) | Crowding in Semis (cap-norm.) |
|------|----------------------------------|-------------------------------|
| '94  | ~0                               | ~-20                          |
| '96  | ~15                              | ~30                           |
| '98  | ~25                              | ~40                           |
| '00  | ~50                              | ~60                           |
| '02  | ~-60                             | ~-55                          |
| '04  | ~-20                             | ~-15                          |
| '06  | ~-10                             | ~-5                           |
| '08  | ~0                               | ~5                            |
| '10  | ~5                               | ~10                           |
| '12  | ~-5                              | ~-10                          |
| '14  | ~5                               | ~10                           |
| '16  | ~20                              | ~30                           |
| '18  | ~30                              | ~45                           |
| '20  | ~25                              | ~35                           |
| '22  | ~10                              | ~20                           |
| '24  | ~5                               | ~15                           |
</details>

Source: JPM Equity Strategy & Quantitative Research

Figure 2: Overall Crowding in Software and Semis   
![](images/afc75dca42636022ec061aef96c4da97df6023c759ead589ec35bb060bd06f16.jpg)

<details>
<summary>line</summary>

| Year | Crowding in Software (cap-norm.) | Crowding in Semis (cap-norm.) |
|------|----------------------------------|-------------------------------|
| '23  | ~0                               | ~0                            |
| '24  | ~10                              | ~15                           |
| '25  | ~5                               | ~10                           |
| '26  | ~-20                             | ~30                           |
</details>

Source: JPM Equity Strategy & Quantitative Research

Figure 3: Retail Crowding in Software and Semis   
![](images/b41092c98278366f80e0765ceea825d42acec8932d8e501bb8418c419445072d.jpg)

<details>
<summary>line</summary>

| Date       | Retail Software Crowding | Retail Semis Crowding |
| ---------- | ------------------------ | ---------------------- |
| 29-Apr-25  | 70                       | 69.6%                  |
| 30-Dec-25  | -30                      | -20                    |
| 11-Mar-26  | -40                      | -30                    |
</details>

Source: JPM Equity Strategy & Quantitative Research, S3 Partners

Figure 4: Shorts Herding in Software and Semis   
![](images/69848b9398d69cf86f6e44f3bf6e4f448e3973462e489ffd5e10194886f535c7.jpg)

<details>
<summary>line</summary>

| Year | Semis Shorts Herding (Squeeze Risk) | Software Shorts Herding (Squeeze Risk) |
|------|----------------------------------------|------------------------------------------|
| '23  | ~4                                     | ~12                                      |
| '24  | ~8                                     | ~16                                      |
| '25  | ~16                                    | ~8                                       |
| '26  | ~6                                     | ~20                                      |
</details>

Figure 5: Retail Investor Daily Purchases by Stocks and ETFs   
\$M, as of May 13 $^{th}$   
![](images/23583fb53423155a442caafa61aa6c7d36eae166f322c1a22e2cfa6e237381d2.jpg)

<details>
<summary>bar</summary>

| Date       | ETF   | Single Stocks |
| ---------- | ----- | ------------- |
| 13-Nov     | 1000  | -500          |
| 20-Nov     | 800   | -300          |
| 28-Nov     | 1300  | 2500          |
| 05-Dec     | 1400  | 1500          |
| 12-Dec     | 1300  | 1700          |
| 19-Dec     | 1600  | -800          |
| 29-Dec     | 1800  | 2000          |
| 06-Jan     | 1400  | -500          |
| 13-Jan     | 1700  | 2700          |
| 21-Jan     | 1600  | 4000          |
| 28-Jan     | 1500  | 2100          |
| 04-Feb     | 1400  | -500          |
| 11-Feb     | 1700  | 2600          |
| 19-Feb     | 1800  | 2100          |
| 26-Feb     | 1900  | 2800          |
| 05-Mar     | 1600  | -300          |
| 12-Mar     | 1500  | -500          |
| 19-Mar     | 1700  | -200          |
| 26-Mar     | 1500  | -800          |
| 02-Apr     | 1900  | -500          |
| 10-Apr     | 300   | -50           |
| 17-Apr     | 1100  | -50           |
| 24-Apr     | 1200  | -30           |
| 01-May     | 1600  | -10           |
| 08-May     | 1300  | -5            |
| Latest     | -    | -             |
</details>

Source: JPM Equity Strategy & Quantitative Research

Figure 6: Daily Retail Imbalance in DRAM   
As of May 13 $^{th}$   
![](images/940669fed1bcbebb0af76c5f5127ea6c06efbc15a816e219c38eb3f605579120.jpg)

<details>
<summary>bar_line</summary>

| Date     | Net Retail Imbalance ($M) | Price (RHS) |
| -------- | -------------------------- | ----------- |
| 07-Apr   | 0.0                        | 0.0         |
| 14-Apr   | 10.0                       | 30.0        |
| 21-Apr   | 5.0                        | 35.0        |
| 28-Apr   | 15.0                       | 40.0        |
| 05-May   | 65.0                       | 45.0        |
| 12-May   | 95.0                       | 55.0        |
</details>

Source: JPM Equity Strategy & Quantitative Research

Figure 7: Cumulative Retail Imbalance in DRAM   
As of May 13 $^{th}$   
![](images/f29535e71b5687279d68241e6debbaeab9ad29bf59a653ecd047a96725995782.jpg)

<details>
<summary>line</summary>

| Date     | Cum. Retail Imbalance ($M) | Price (RHS) |
| -------- | -------------------------- | ----------- |
| 07-Apr   | ~10                        | ~30         |
| 14-Apr   | ~50                        | ~35         |
| 21-Apr   | ~100                       | ~38         |
| 28-Apr   | ~150                       | ~42         |
| 05-May   | ~250                       | ~48         |
| 12-May   | ~500                       | ~55         |
</details>

Source: JPM Equity Strategy & Quantitative Research

Figure 8: Daily Retail Imbalance in KWEB   
![](images/870332948fcdc92893a92700197d3ee3ea6d8c66128cb41f800c73198c129505.jpg)

<details>
<summary>line</summary>

| Date   | Net Retail Imbalance ($M) | Price (RHS) |
|--------|---------------------------|-------------|
| Jun-25 | ~0                        | ~34         |
| Jul-25 | ~0                        | ~34         |
| Aug-25 | ~0                        | ~34         |
| Sep-25 | ~0                        | ~34         |
| Oct-25 | ~0                        | ~34         |
| Nov-25 | ~0                        | ~34         |
| Dec-25 | ~0                        | ~34         |
| Jan-26 | ~0                        | ~34         |
| Feb-26 | ~0                        | ~34         |
| Mar-26 | ~0                        | ~34         |
| Apr-26 | ~0                        | ~34         |
| May-26 | ~0                        | ~34         |
</details>

Source: JPM Equity Strategy & Quantitative Research

Figure 10: Daily Retail Imbalance in COPX   
![](images/1e3fce4176ce70b982f62b0dbf5ddec012c1f6c8311ea73c12e43087aac36d63.jpg)

<details>
<summary>line</summary>

| Date    | Net Retail Imbalance ($M) | Price ($RHS) |
|---------|---------------------------|--------------|
| Jun-25  | ~0                        | ~-18         |
| Jul-25  | ~0                        | ~-15         |
| Aug-25  | ~0                        | ~-12         |
| Sep-25  | ~0                        | ~-8          |
| Oct-25  | ~0                        | ~-5          |
| Nov-25  | ~0                        | ~0           |
| Dec-25  | ~0                        | ~5           |
| Jan-26  | ~0                        | ~10          |
| Feb-26  | ~30                       | ~25          |
| Mar-26  | ~30                       | ~30          |
| Apr-26  | ~0                        | ~70          |
| May-26  | ~0                        | ~90          |
</details>

Source: JPM Equity Strategy & Quantitative Research

Figure 9: Cumulative Retail Imbalance in KWEB   
![](images/e07b42b945767e55ccfd6764d5ed59594f3d891b81cb5ea945befcbe4c9d555d.jpg)

<details>
<summary>line</summary>

| Date   | Cum. Retail Imbalance ($M) | Short Interest (RHS) |
|--------|-----------------------------|----------------------|
| Jun-25 | ~0                          | ~80.00               |
| Jul-25 | ~10                         | ~30.00               |
| Aug-25 | ~30                         | ~15.00               |
| Sep-25 | ~70                         | ~45.00               |
| Oct-25 | ~100                        | ~180.00              |
| Nov-25 | ~110                        | ~150.00              |
| Dec-25 | ~120                        | ~120.00              |
| Jan-26 | ~130                        | ~10.00               |
| Feb-26 | ~140                        | ~30.00               |
| Mar-26 | ~135                        | ~40.00               |
| Apr-26 | ~145                        | ~35.00               |
| May-26 | ~175                        | ~35.00               |
</details>

Source: JPM Equity Strategy & Quantitative Research

Figure 11: Cumulative Retail Imbalance in COPX   
![](images/583db51a6ded194887d99b7601d67b23ce797c26def0f5f72cd9a3f3c920e96d.jpg)

<details>
<summary>line</summary>

| Date    | Cum. Retail Imbalance ($M) | Short Interest (RHS) |
|---------|-----------------------------|----------------------|
| Jun-25  | ~0                          | ~0                   |
| Jul-25  | ~0                          | ~1.0                 |
| Aug-25  | ~0                          | ~3.0                 |
| Sep-25  | ~0                          | ~4.0                 |
| Oct-25  | ~10                         | ~6.0                 |
| Nov-25  | ~20                         | ~3.0                 |
| Dec-25  | ~30                         | ~2.0                 |
| Jan-26  | ~100                        | ~4.0                 |
| Feb-26  | ~300                        | ~8.0                 |
| Mar-26  | ~350                        | ~7.0                 |
| Apr-26  | ~320                        | ~5.0                 |
| May-26  | ~330                        | ~4.0                 |
</details>

Source: JPM Equity Strategy & Quantitative Research

# Single Stock Stories with Elevated Retail Activity

# Hedge Funds vs. Retail: High Short Interest Meme Stocks

- KMB (\$5.4M bought last week, 0.3z, Figure 18): The company recently received approval from India's Competition Commission for its acquisition of sole control over Kenvue Inc. (link). Retail investors have shown interest in the stock since January 2026, with net purchases totaling \$181 million, alongside moderate short interest at 12%, which has increased by 5% since January 2026.   
- KLAR (\$3M bought last week, -0.1z, Figure 19): The company announced it will integrate its flexible payment options into Google's Gemini app and Google Search (including AI Mode) in the U.S. through Google Pay (link). YTD, the stock is down roughly 50%, yet retail investors have continued to accumulate shares, with net purchases totaling approximately \$53 million. Over the same period, short interest increased from about 9% to 17%.   
- RIVN (\$19M sold last week, 0.1z, Figure 20): The company introduced its AI voice assistant, expanding access to all compatible vehicles (link). Retail investors have been active since November 2025, with cumulative net purchases of approximately \$430 million. Short interest remains elevated at 19%, up about 2% since the start of this month.

# Earnings Stories:

- Software companies reported a broadly strong week of earnings: DDOG (\(40M sold on 5/7, -7.7z, Figure 35) had an exceptional quarter — revenue grew 32% y/y (4th con

[中间内容因长度限制已省略]

ates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its sUBSidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised April 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 14 May 2026 12:46 AM EDT

Disseminated 14 May 2026 01:07 AM EDT
"""
