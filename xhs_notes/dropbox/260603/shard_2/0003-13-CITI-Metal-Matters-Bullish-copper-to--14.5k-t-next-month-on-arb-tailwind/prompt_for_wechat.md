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
01 Jun 2026 01:00:00 ET | 15 pages

# Metal Matters

Bullish copper to \$14.5k/t next month on arb tailwinds and growth resilience, \$15k/t within a year.

# CITI'S TAKE

We publish March data for our global copper end use consumption tracker and revise higher our copper price forecasts to \$14,500/t near-term and \$15k/t over 6-12 months. US copper tariff fears are likely to remain a price tailwind through June until tariff clarity emerges. We think global growth and risk-sentiment can hold up in the near-term even if the Strait of Hormuz remains closed through to July, while an earlier or eventual deal (base case) to reopen the Strait should be bullish for risk assets. We are now also more conservative on copper supply growth and assume scrap and mine output underperform through 2026 and 2027.

We turn bullish on copper to \$14,500/t over the next month (having been broadly neutral since January, and previously bullish from Sep-25) and expect copper to touch \$15k/t within a year — We think growth and risk assets will be resilient to Hormuz Strait closure impacts for at least the next few months while also exposed to eventual or swifter upside from a potential deal. US copper tariff fears can remain supportive through June, and risks skew more bullish medium-term with scrap and mine supply growth likely to underperform this year and next against resilient energy transition and AI demand, with a \~360kt forecast deficit in 2027.

Lingering fears of US tariffs on refined copper may support sentiment until at least the end-June review deadline — We anticipate further strategic ambiguity from US policymakers rather than a definitive announcement of a tariff and believe that the administration will not impose a refined copper tariff but will avoid stating this definitively to maximise incentives to maintain excess copper inventory in the US. Post-June, lack of tariff clarity could become a headwind if the market fades pricing of tariff risk, but a supportive physical outlook and our expectation for a Hormuz reopening by the summer could offset any bearish impact.

We caution that despite resilient growth and likely tighter physical balances copper, along with many risk assets, remains subject to bearish tail risks from a sustained and unstable Middle East situation. Copper inventory levels and end-use consumption remain sensitive to interest rates and expectations, even though physical demand appears far more cushioned today from a cyclical growth shock than in the past due to assumed structural resilience of AI and energy transition demand particularly if higher energy pricing drives the shock (read more here).

Our proprietary tracker implies subdued copper end use growth y/y as of March amid subdued cyclical demand growth but also due to a y/y decline in China reported renewable installations versus an temporary high base in 2025 — However, recent improvement in global PMI prints suggests upside for cyclical consumption, which implied softness in domestic China energy transition demand (and other segments like property) is being offset by strong export growth. The implied slowdown in China energy transition demand is largely a function of policy induced front-loading in solar and EVs last year and is/was anticipated.

Tom Mulqueen AC

+44-20-7986-4559

tom.mulqueen@citi.com

Shreyas Madabushi $^{AC}$

+91-22-4277-5048

shreyas.madabushi@citi.com

Maximilian J Layton $^{AC}$

+44-20-7986-4556

max.layton@citi.com

Wenyu Yao $^{AC}$

+44-20-7986-4551

wenyu.yao@citi.com

Kenny Hu, CFA $^{AC}$

+65-6657-3873

kenny.x.hu@citi.com

Viswanathrao Kintali $^{AC}$

+44-20-7986-4982

viswanathrao.kintali@citi.com

Ephrem Ravi $^{AC}$

+44-20-7986-2462

ephrem.ravi@citi.com

Jack Shang, CFA $^{AC}$

+852-2501-2441

jack.shang@citi.com

Alexander Hacking, CFA $^{AC}$

+1-212-816-6232

alex.hacking@citi.com

# Copper risks turn bullish on arb and supply tailwinds, growth resilience

Upward revisions to our copper price forecasts and scenarios are summarised in Fig.1 and 2. We turn bullish copper (previously neutral) to \$14,500/t through June amid more confidence in broader near-term global growth resilience, US-arb tailwinds, and physical supply constraints outweighing bearish tail risks from a broader risk-unwind on sustained Hormuz disruption and/or higher interest rate expectations. We also hike prices in our bull case price scenario (albeit reduce the probability to 20%) to reflect upside if cyclical growth outperforms, rate cuts are repriced, or we see bull fundamental outcomes (stronger copper structural demand growth, further supply underperformance from mine supply and/or scrap).

Figure 1. Citi copper price summary of base case forecast revisions 

<table><tr><td>Base Metals</td><td>Unit</td><td>0-3 mth pt price</td><td>6-12 mth pt price</td><td>2025f</td><td>1Q26</td><td>2Q26f</td><td>3Q26f</td><td>4Q26f</td><td>2026f</td><td>1Q27f</td><td>2Q27f</td><td>3Q27f</td><td>4Q27f</td><td>2027f</td><td>2028f</td></tr><tr><td>Copper NEW</td><td>$/t</td><td>14500</td><td>15000</td><td>9950</td><td>12818</td><td>13500</td><td>14000</td><td>14500</td><td>13700</td><td>14500</td><td>14500</td><td>14000</td><td>14000</td><td>14250</td><td>14000</td></tr><tr><td>Copper (OLD)</td><td></td><td>13000</td><td>12000</td><td>9950</td><td>12818</td><td>13000</td><td>12500</td><td>12000</td><td>12600</td><td>12000</td><td>12000</td><td>12000</td><td>12000</td><td>12000</td><td>12000</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: Citi, Bloomberg, LME

Figure 2. Citi copper price forecast revised scenarios (ex-US pricing) 

<table><tr><td>Price Forecasts</td><td>Scenario Weight</td><td>Unit</td><td>0-3 mth pt price</td><td>6-12 mth pt price</td><td>1Q26</td><td>2Q26f</td><td>3Q26f</td><td>4Q26f</td><td>2026f</td><td>1Q27f</td><td>2Q27f</td><td>3Q27f</td><td>4Q27f</td><td>2027f</td><td>2028f</td></tr><tr><td>Copper (Bull)</td><td>20%</td><td>$/t</td><td></td><td></td><td>12818</td><td>14000</td><td>15000</td><td>16000</td><td>14455</td><td>17000</td><td>17000</td><td>17000</td><td>17000</td><td>17000</td><td>17000</td></tr><tr><td>Copper (Base)</td><td>60%</td><td>$/t</td><td>14500</td><td>15000</td><td>12818</td><td>13500</td><td>14000</td><td>14500</td><td>13700</td><td>14500</td><td>14500</td><td>14000</td><td>14000</td><td>14250</td><td>14000</td></tr><tr><td>Copper (Bear)</td><td>20%</td><td>$/t</td><td></td><td></td><td></td><td>12500</td><td>12000</td><td>12000</td><td>12330</td><td>11000</td><td>11000</td><td>11000</td><td>11000</td><td>11000</td><td>11000</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: Citi, Bloomberg, LME

Net long copper positioning is now relatively elevated but remains below the highs of late 2025 and 2024. Funds gross short positions remain subdued on COMEX, likely partly due to lingering tariff risk and this is unlikely to change ahead of market anticipation of further tariff clarity by end-June.

Figure 3. Investor net long copper positioning has climbed in recent weeks alongside stronger PMI readings and broader risk asset strength (e.g. US equities)   
![](images/c6556ce2eddfbcbecacb256ffb4014a50f4409c9636f16402e03b1a66570fc8a.jpg)

<details>
<summary>line</summary>

| Year | Citi Global Copper Cyclical Demand PMI | Copper net spec positioning (Mt Cu Comex and LME) |
|------|------------------------------------------|--------------------------------------------------|
| 2018 | 53.5                                     | 1.5                                              |
| 2019 | 50.5                                     | -0.5                                             |
| 2020 | 49.0                                     | -1.0                                             |
| 2021 | 54.0                                     | 2.0                                              |
| 2022 | 52.0                                     | 1.0                                              |
| 2023 | 48.0                                     | -0.5                                             |
| 2024 | 51.0                                     | 2.5                                              |
| 2025 | 50.0                                     | 1.5                                              |
| 2026 | 52.0                                     | 2.0                                              |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: Citi, LME, Bloomberg, CME Group

Figure 4. Funds are reluctant to be short copper, particularly on COMEX likely given lingering tariff risk, this could shift post June.   
![](images/16dca69b107f605ac74d0f0b9a58c23145e95df732a25009d010923d240ea62f.jpg)

<details>
<summary>line</summary>

| Year | LME Investment Fund Short (MT) | Comex Money Manager Short (Mt) |
|------|----------------------------------|--------------------------------|
| 2023 | ~0.7                             | ~0.5                           |
| 2024 | ~1.3                             | ~1.1                           |
| 2025 | ~0.9                             | ~0.6                           |
| 2026 | ~0.7                             | ~0.1                           |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: Citi, Bloomberg, LME, CME Group

We think lingering fears of a potential US tariff on refined copper can support sentiment until July, beyond which inventory draws/reduced incentive to finance metal domestically can act as a headwind. Our base case remains that no tariff will be announced, but that US policymakers may opt to maintain strategic ambiguity rather announcing anything definitive to support continued storage of inventory within the US. This may weigh somewhat through 3Q'26, but our base case of a Hormuz reopening in 3Q'26 may offset downside, and any eventual inventory draws are likely to be gradual rather than sudden. In the tail risk scenario that tariffs are announced and phased from 2027, this would be incrementally price supportive, particularly for COMEX-prices that would reflect most of the tariff rate, and LME spreads given the prospect of further shipments of metal to the US ahead of tariff implementation.

Figure 5. The COMEX-LME arb has rewidened ahead of an anticipated review of US S232 tariffs on refined imports by end-June, combined with recent builds in fund length.   
![](images/2078318da726045bfde4b04ed1cba1113d901fc997553ebdc981310e37d20f2a.jpg)

<details>
<summary>line</summary>

| Date       | Jul 26 | Sep 26 | Dec 26 | Mar 27 | May 27 | JUL 27 |
|------------|--------|--------|--------|--------|--------|--------|
| Latest data |        |        |        |        |        |        |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: Citi, Bloomberg, LME, CME Group

Figure 6. US imports have matched typical import requirements for the last month or so, but widening of arb could incentivise a reacceleration of US-bound shipments   
![](images/c62e422863b68eb5e90fea490b6ff9aec06e5afdb203685356230c689613b6eb.jpg)

<details>
<summary>line</summary>

| Month   | 4-week rolling US refined copper cathode imports | Typical US imports for consumption |
|---------|--------------------------------------------------|-------------------------------------|
| Jan-25  | 30                                               | 70                                  |
| Feb-25  | 60                                               | 70                                  |
| Mar-25  | 50                                               | 70                                  |
| Apr-25  | 140                                              | 70                                  |
| May-25  | 190                                              | 70                                  |
| Jun-25  | 180                                              | 70                                  |
| Jul-25  | 160                                              | 70                                  |
| Aug-25  | 190                                              | 70                                  |
| Sep-25  | 100                                              | 70                                  |
| Oct-25  | 60                                               | 70                                  |
| Nov-25  | 10                                               | 70                                  |
| Dec-25  | 40                                               | 70                                  |
| Jan-26  | 160                                              | 70                                  |
| Feb-26  | 180                                              | 70                                  |
| Mar-26  | 140                                              | 70                                  |
| Apr-26  | 120                                              | 70                                  |
| May-26  | 70                                               | 70                                  |
| Jun-26  | 60                                               | 70                                  |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: Citi, Bloomberg, US BOL

Figure 4 shows our tighter copper physical balance expectation for 2027 with an anticipated deficit of \~350kt basis current spot prices. On paper this would equate to roughly a \$1,500/t higher price to drive additional scrap recovery and substitution sufficient to clear the market, although we acknowledge some potential for a drawdown in excess US inventory that could absorb some or all this modelled deficit.

Figure 7. Revised copper supply and demand balance 

<table><tr><td>kt Cu</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026f</td><td>2027f</td><td>2028f</td></tr><tr><td>Mine Production</td><td>20,752</td><td>21,179</td><td>21,808</td><td>22,395</td><td>23,128</td><td>23,398</td><td>23,352</td><td>23,789</td><td>24,542</td></tr><tr><td>% Change</td><td>0.7%</td><td>2.1%</td><td>3.0%</td><td>2.7%</td><td>3.3%</td><td>1.2%</td><td>-0.2%</td><td>1.9%</td><td>3.2%</td></tr><tr><td>Of Which Disr. Allowance (t)</td><td></td><td></td><td></td><td></td><td></td><td></td><td>977</td><td>1,818</td><td>1,942</td></tr><tr><td>Of Which Disr. Allowance (%)</td><td></td><td></td><td></td><td></td><td></td><td></td><td>4.0%</td><td>7.1%</td><td>7.3%</td></tr><tr><td>Refined Production</td><td>23,591</td><td>24,374</td><td>25,067</td><td>25,561</td><td>26,450</td><td>27,300</td><td>27,423</td><td>27,816</td><td>28,649</td></tr><tr><td>% Change</td><td>-0.3%</td><td>3.3%</td><td>2.8%</td><td>2.0%</td><td>3.5%</td><td>3.2%</td><td>0.5%</td><td>1.4%</td><td>3.0%</td></tr><tr><td>Refined Consumption</td><td>23,006</td><td>24,664</td><td>24,735</td><td>25,596</td><td>26,202</td><td>26,834</td><td>27,424</td><td>28,179</td><td>28,801</td></tr><tr><td>% Change</td><td>-3.6%</td><td>7.2%</td><td>0.3%</td><td>3.5%</td><td>2.4%</td><td>2.4%</td><td>2.2%</td><td>2.8%</td><td>2.2%</td></tr><tr><td>End-Use Consumption</td><td>24,110</td><td>25,848</td><td>25,922</td><td>26,824</td><td>27,460</td><td>28,122</td><td>28,741</td><td>29,531</td><td>30,184</td></tr><tr><td>Surplus/Deficit</td><td>585</td><td>-290</td><td>332</td><td>-35</td><td>247</td><td>466</td><td>-1</td><td>-363</td><td>-152</td></tr><tr><td>Av. Price (US$/t ex-US)</td><td>6,183</td><td>9,318</td><td>8,830</td><td>8,485</td><td>9,145</td><td>9,950</td><td>13,600</td><td>14,000</td><td>14,000</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: Citi, Bloomberg, Wood Mackenzie, ICSG, IWCC, LME, BGRIMM

Our mine supply growth assumptions are now weaker having applied a higher global disruption allowance of 7% for 2027 and 2028, while still expecting zero growth in 2026. We think a higher disruption allowance risk is warranted given increased execution and ramp-up risk across key mines (e.g. Grasberg, El Teniente, Kamoa, Cobre Panama) and a less certain path for sustained elevated production growth in the DR Congo given current sulfur market constraints and broader elevated supply risks associated with the current environment of less geopolitical stability and greater reliance on share copper supply from less stable jurisdictions.

The global copper market is reliant on rising scrap supply (acknowledging 2025 surplus base) to meet structural demand growth in 2026 (Fig.8) given flat anticipated mine output. We now assume that scrap recovery will not rise proportionally to higher 2026 prices and will meet less than half this demand. China scrap import data (Fig 10 and 11) shows only a modest y/y uptick despite much higher copper prices of >30% y/y for Jan-Apr. Underperformance relative to price could be justified by the recent hikes to energy and fuel costs, softer goods trade-in-support in China relative to last year, and our belief in a generally depleted global scrap supply chain given broader shortages of raw materials for smelters in recent years.

Figure 8. Scrap and mine supply growth expected to fail to match AI and energy transition demand growth this year and next (if we assume any cyclical demand recovery the gap becomes more severe)   
![](images/4b1fc59526531b94b31ff301eee4450b967725151c959f4ab7063a1520b264db.jpg)

<details>
<summary>bar</summary>

| Year   | Energy transition demand | Mine supply | Smelter and refinery scrap | Datacentre demand |
|--------|--------------------------|-------------|----------------------------|-------------------|
| 2019   | -200                     | -50         | 50                         | 0                 |
| 2020   | 350                      | 150         | -200                       | 0                 |
| 2021   | 400                      | 400         | 800                        | 0                 |
| 2022   | 300                      | 600         | -50                        | 0                 |
| 2023   | 900                      | 600         | 600                        | 0                 |
| 2024   | 550                      | 750         | 1,050                      | 50                |
| 2025   | 600                      | 250         | 700                        | 50                |
| 2026f  | 600                      | -50         | 250                        | 50                |
| 2027f  | 450                      | 450     

[中间内容因长度限制已省略]

lar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
