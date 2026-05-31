你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  ✅ 三大情景框架：DCF、P/ARR、EV/Sales
  ✅ 关键变量分析
  ✅ 估值逻辑、假设、终值占比等核心内容覆盖
  ✅ 适合准备 AI 相关面试、研究 AI 估值的同学
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
# THE WORLD CUP AND ECONOMICS

# World Cup 2026: Predictions, Probabilities, and Paths to Victory

We present a model for predicting the outcome of the 2026 World Cup in the US, Canada and Mexico from June 11 to July 19. It is similar to our model for prior World Cups but extended along several dimensions.   
Historical performance data for each team—most importantly the Elo rating system originally devised to rank chess players—is the main determinant of the number of goals scored. But even for a given Elo rating, we show that scoring talent and team momentum matter, as well as several mentality and geographical factors.   
We then simulate a set of probabilities that a particular team will reach a particular round, up to winning the World Cup. We also provide a modal forecast for how the tournament will unfold. After each day of play, we will re-run the model using updated performance data in order to generate new probabilities and a new modal forecast.   
The model says that Spain has a 26% probability of winning the trophy, followed by France at 19%, Argentina at 14%, Brazil at 8% and England at 5%. Spain is predicted to win because it has the highest Elo ranking, supported by scoring talent and good momentum into the competition. Argentina is penalised by the “winner’s slump”, i.e. the statistical underperformance of reigning champions in the following World Cup; France suffers from likely facing top-ranked Spain in the semifinals; and England underperforms its Elo rating given historical tournament disappointment, geographical headwinds (likely facing Mexico in high-altitude Mexico City), and a slightly unlucky draw.   
How much faith should we have in these predictions? Our projections are not far from bookmakers' odds—except for a lower winning probability for England—and our model would have performed quite well at previous World Cups (for example, when measured with the goal difference). That said, the model's statistical power remains limited—not a surprise given football's inherent unpredictability.

# Jan Hatzius

+1(212)902-0394 | jan.hatzius@gs.com

GS & Co. LLC

# Giovanni Pierdomenico

+44(20)7051-6807

giovanni.pierdomenico@gs.com

GS International

# Sven Jari Stehn

+44(20)7774-8061 | jari.stehn@gs.com

GS International

# World Cup 2026: Predictions, Probabilities, and Paths to Victory

# "Football is the most important of the least important things in life" – Arrigo Sacchi, Italian former football manager

With two weeks to go, we introduce our statistical model for predicting the outcome of the 2026 World Cup. We proceed as follows.

# Our Statistical Model to Predict the Outcome of the World Cup

First, we estimate a regression model to predict the number of goals scored by a particular team (“team i”) against a particular opponent (“team j”) using the entire history of mandatory international matches since 1978 (a total of just under 20,000 matches). Following the literature on predicting football matches, we assume that the number of goals scored by team i is described by a so-called “Poisson” distribution (Exhibit 1).

Exhibit 1: The Number of Goals Score by a Football Team Broadly Follows a Poisson Distribution   
![](images/f167007a6ff1c2fa3a258a503fdb850a0c418dd13f4e188003c55e91ac9cd202.jpg)

<details>
<summary>line</summary>

| Decade | World Cup | Major Continental Championships* | Other Official Competitions** | Friendlies |
| ------ | --------- | --------------------------------- | ------------------------------ | ---------- |
| 1900   | 4.9       | 3.5                               | 4.9                            | 4.9        |
| 1920   | 4.2       | 3.5                               | 5.0                            | 4.1        |
| 1940   | 4.3       | 4.3                               | 5.2                            | 4.4        |
| 1960   | 2.7       | 3.7                               | 3.2                            | 3.0        |
| 1980   | 2.6       | 2.3                               | 2.5                            | 2.5        |
| 2000   | 2.5       | 2.7                               | 2.8                            | 2.6        |
| 2020   | 2.6       | 2.5                               | 2.8                            | 2.7        |
</details>

\*Major Continental Championships include European and South American championships. \*\*Other official competitions include other continental championships and all qualifiers. Note: WC 1940s are interpolated.

![](images/8aca025c77d7f1093ba6795b913a926c218dd5248435baadaeaf9d685deb2378.jpg)

<details>
<summary>bar</summary>

| Team | Frequency |
| ---- | --------- |
| 0    | 6500      |
| 1    | 6000      |
| 2    | 3700      |
| 3    | 1800      |
| 4    | 900       |
| 5    | 400       |
| 6    | 200       |
| 7    | 100       |
</details>

Sample: Mandatory international games since 1978.   
Source: eloratings.net, GS Global Investment Research

The main determinant of the number of goals scored is the difference in team performance as reflected in Elo ratings prior to the match. The Elo system was originally devised to rank chess players. It is a composite measure of national football team success that evolves depending on a team's results and the strength of its opponents. The Elo system ranks Spain first, followed by Argentina and France, and thus differs slightly from the FIFA men's world rankings (Exhibit 2).

Exhibit 2: Elo vs FIFA/Coca-Cola Rankings   
![](images/8c7e0f763f3d864cba88371c1f8fb2932fb90f268358827e9c6f19311fd1164f.jpg)

<details>
<summary>scatter</summary>

| Label | Elo Rating | FIFA/Coca Cola World Ranking Points |
|-------|------------|-------------------------------------|
| FRA-ARG | ~2100 | ~1880 |
| SPA | ~2170 | ~1870 |
| ENG | ~2030 | ~1830 |
| POR | ~2000 | ~1760 |
| NLD | ~1970 | ~1760 |
| BRA | ~1990 | ~1760 |
| GER | ~1930 | ~1730 |
| CRO | ~1920 | ~1720 |
| COL | ~1980 | ~1700 |
| ECU | ~1940 | ~1600 |
| NOR | ~1910 | ~1550 |
| Top 12 Elo-rating countries are labelled. | — | — |
</details>

Source: eloratings.net, FIFA, GS Global Investment Research

We then expand the model with several other explanatory variables:

■ Scoring talent: we gather data on top goal scorers in national leagues and international competitions for clubs and find that these matter for the number of goals scored by the team in a World Cup $^{1}$ .   
■ Momentum: we measure team momentum by including the number of goals scored by team i in the last 10 competitive matches, and the number of goals conceded by team j in the last 5 competitive matches.   
■ Mentality: we find that reigning world champions typically underperform (while teams at their first World Cup usually outperform) and that it is more difficult to score against European teams (all else equal). Furthermore, major footballing nations generally get a World Cup boost, with the notable exception of England.   
- Geography: we confirm a familiar “home effect” for games that are played at home. We also find that the number of goals scored is reduced: by the distance between the country’s capital and location of the game; when a low-altitude country plays in a high-altitude stadium (which is relevant for games played in Mexico in the upcoming World Cup); and by the absolute temperature difference between the average temperature of a country and the temperature of the venue in the month of the game.

Exhibit 3: Goal-Scoring Potential Matters; Some Signs of a “Winner’s Slump” Effect After Winning the World Cup   
![](images/e306b3d5039c183ac986af7b8ffeb10f7cdb7394fff8b12455d814be10de63c1.jpg)

<details>
<summary>line</summary>

| Year | Spain | France | Germany | Argentina | England | Brazil |
|------|-------|--------|---------|-----------|---------|--------|
| 1990 | 120   | 110    | 230     | 30        | 10      | 40     |
| 1995 | 50    | 100    | 130     | 60        | 270     | 120    |
| 2000 | 130   | 120    | 110     | 80        | 110     | 110    |
| 2005 | 120   | 150    | 50      | 40        | 80      | 160    |
| 2010 | 130   | 90     | 80      | 160       | 100     | 60     |
| 2015 | 150   | 190    | 90      | 170       | 70      | 30     |
| 2020 | 70    | 150    | 60      | 140       | 150     | 30     |
| 2025 | 90    | 160    | 40      | 60        | 140     | 80     |
</details>

<table><tr><td>World Cup</td><td>Winner</td><td>Outcome in the Following World Cup</td></tr><tr><td>1978</td><td>Argentina</td><td>2nd Round</td></tr><tr><td>1982</td><td>Italy</td><td>Round of 16</td></tr><tr><td>1986</td><td>Argentina</td><td>2nd Place</td></tr><tr><td>1990</td><td>Germany</td><td>Quarter Finals</td></tr><tr><td>1994</td><td>Brazil</td><td>2nd Place</td></tr><tr><td>1998</td><td>France</td><td>Group Stage</td></tr><tr><td>2002</td><td>Brazil</td><td>Quarter Finals</td></tr><tr><td>2006</td><td>Italy</td><td>Group Stage</td></tr><tr><td>2010</td><td>Spain</td><td>Group Stage</td></tr><tr><td>2014</td><td>Germany</td><td>Group Stage</td></tr><tr><td>2018</td><td>France</td><td>2nd Place</td></tr><tr><td>2022</td><td>Argentina</td><td>TBC</td></tr></table>

Source: Transfermarkt, FIFA, GS Global Investment Research

Exhibit 4 summarises the marginal effect of some of the key variables in our model on the predicted number of goals scored in a World Cup game.

Exhibit 4: What Matters in Our Model   
![](images/aeaebd112ef4f6d5b23afc15542f1d19044ff3bc430999f0de27ee52ee912764.jpg)

<details>
<summary>bar</summary>

| Variable | Expected Nr of Goals |
| --- | --- |
| Home Advant. | 0.38 |
| Elo Diff. (+200pt) | 0.21 |
| Talent Effect (+2 top scorers) | 0.10 |
| Oppon. Goals Conced. (+1) | 0.07 |
| Recent Goals Scored (+1) | 0.05 |
| Winner's Slump | -0.12 |
| High Altitude Malus | -0.18 |
</details>

\*Evaluated at average values.

![](images/4b64e514a4f5f152e403a7ed03da926c741c2c43ab74ef89d981cf08b2069b98.jpg)

<details>
<summary>bar</summary>

| Team | Expected Nr of Goals |
| ---- | ------------------- |
| ARG  | 0.35                |
| GER  | 0.30                |
| BRA  | 0.29                |
| FRA  | 0.27                |
| NET  | 0.26                |
| POR  | 0.23                |
| SPA  | 0.18                |
| ENG  | 0.06                |
</details>

\*Boost for big teams when they play in the WC, evaluated at average values.   
Source: GS Global Investment Research

Second, we apply this regression-based model to the upcoming World Cup. This entails simulating the group-stage games and the resulting bracket of the knock-out stage up to the final held on July 19 in New York. Our model updates Elo ratings and momentum variables recursively over the course of the tournament, according to model-based or, later, actual scores. We apply official FIFA rules for the tie-breakers in the group stage and account for all 495 possible pairings in the round of 32, which will depend on which third-placed teams qualify for the knock-out stage. We use the rounded prediction of the goals scored to determine the outcome of each match during the group stage and

the unrounded prediction to pick the winner in the knockout stage $^{2}$ .

The model thus generates the single most likely prediction for each of the 104 games in the World Cup up to the final. We can also leverage the Poisson distribution underlying our model to run a Monte Carlo simulation with 50,000 draws, which yields a set of probabilities that a particular team wins the tournament or reaches a particular stage of the tournament. In each of the simulations, the outcome of a game is given by a random draw (as opposed to the most likely) from the team- and game-specific Poisson distribution of goals scored $^{3}$ .

# A Summary of the Predictions

Exhibit 5 and Exhibit 6 show the most likely development of the tournament according to our model.

We expect major teams and all three hosts to advance from the expanded 48-team group stage to the round of 32. Groups D and G are expected to be the tightest ones, with our model unable to clearly differentiate (on a rounded basis) between the teams on the basis of the statistical factors considered. Exhibit 12 in the Appendix shows the predicted standings at the group stage.

We expect the round of 32 to offer a few interesting games, including the US vs. Iran and a clásico Argentina vs. Uruguay. That said, the first “big matches” should be featured in the round of 16, with Germany projected to be eliminated by France. England vs. Brazil and Argentina vs. Portugal (which could be the last match-up between Lionel Messi and Cristiano Ronaldo) should be the most exciting quarter-finals, with the Seleção and the Selección advancing to the next stage. The Netherlands and the tournament surprise Türkiye are also expected to end their run in the quarter-finals.

The model projects semi-finals of France vs. Spain, and Brazil vs. Argentina, with la Roja and la Albiceleste (reigning continental champions respectively in Europe and South America) facing off in a Finalissima. We expect Spain to win its second World Cup on July 19, with Messi (who turns 39 during the tournament) passing on the torch to Lamine Yamal (who will celebrate his $19^{\text{th}}$ birthday just a few days before the New York final). Our prediction aligns with the historical pattern that the World Cup almost always comes back to Europe after having been won by a South American team (with the only exception being the consecutive Brazilian wins in 1958 and 1962).

# Exhibit 5: Most Likely Predicted Group Stage Results

FIFA World Cup 2026 - Group Stage: Prediction as of 29 May 2026

Played (final score) Predicted score

<table><tr><td colspan="5">Group A Mexico | South Korea | Czechia | South Africa</td></tr><tr><td>MD</td><td>Date</td><td>Team 1</td><td>Score</td><td>Team 2</td></tr><tr><td>1</td><td>11-Jun</td><td>Mexico</td><td>2-0</td><td>South Africa</td></tr><tr><td>1</td><td>11-Jun</td><td>South Korea</td><td>1-1</td><td>Czechia</td></tr><tr><td>2</td><td>18-Jun</td><td>Czechia</td><td>1-1</td><td>South Africa</td></tr><tr><td>2</td><td>18-Jun</td><td>Mexico</td><td>2-1</td><td>South Korea</td></tr><tr><td>3</td><td>24-Jun</td><td>Czechia</td><td>1-2</td><td>Mexico</td></tr><tr><td>3</td><td>24-Jun</td><td>South Africa</td><td>1-1</td><td>South Korea</td></tr></table>

<table><tr><td colspan="5">Group B Canada | Qatar | Switzerland | Bosnia and H.</td></tr><tr><td>MD</td><td>Date</td><td>Team 1</td><td>Score</td><td>Team 2</td></tr><tr><td>1</td><td>12-Jun</td><td>Canada</td><td>2-1</td><td>Bosnia and H.</td></tr><tr><td>1</td><td>13-Jun</td><td>Qatar</td><td>0-2</td><td>Switzerland</td></tr><tr><td>2</td><td>18-Jun</td><td>Switzerland</td><td>1-1</td><td>Bosnia and H.</td></tr><tr><td>2</td><td>18-Jun</td><td>Canada</td><td>2-1</td><td>Qatar</td></tr><tr><td>3</td><td>24-Jun</td><td>Switzerland</td><td>1-1</td><td>Canada</td></tr><tr><td>3</td><td>24-Jun</td><td>Bosnia and H.</td><td>1-1</td><td>Qatar</td></tr></table>

<table><tr><td colspan="5">Group C Brazil | Haiti | Scotland | Morocco</td></tr><tr><td>MD</td><td>Date</td><td>Team 1</td><td>Score</td><td>Team 2</td></tr><tr><td>1</td><td>13-Jun</td><td>Brazil</td><td>2-1</td><td>Morocco</td></tr><tr><td>1</td><td>13-Jun</td><td>Haiti</td><td>1-1</td><td>Scotland</td></tr><tr><td>2</td><td>19-Jun</td><td>Scotland</td><td>1-1</td><td>Morocco</td></tr><tr><td>2</td><td>19-Jun</td><td>Brazil</td><td>2-1</td><td>Haiti</td></tr><tr><td>3</td><td>24-Jun</td><td>Scotland</td><td>1-2</td><td>Brazil</td></tr><tr><td>3</td><td>24-Jun</td><td>Morocco</td><td>1-1</td><td>Haiti</td></tr></table>

<table><tr><td colspan="5">Group D USA | Australia | Turkiye | Paraguay</td></tr><tr><td>MD</td><td>Date</td><td>Team 1</td><td>Score</td><td>Team 2</td></tr><tr><td>1</td><td>12-Jun</td><td>USA</td><td>1-1</td><td>Paraguay</td></tr><tr><td>1</td><td>13-Jun</td><td>Australia</td><t

[中间内容因长度限制已省略]

 attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
