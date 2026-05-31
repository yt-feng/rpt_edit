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

<table><tr><td colspan="5">Group D USA | Australia | Turkiye | Paraguay</td></tr><tr><td>MD</td><td>Date</td><td>Team 1</td><td>Score</td><td>Team 2</td></tr><tr><td>1</td><td>12-Jun</td><td>USA</td><td>1-1</td><td>Paraguay</td></tr><tr><td>1</td><td>13-Jun</td><td>Australia</td><td>1-1</td><td>Turkiye</td></tr><tr><td>2</td><td>19-Jun</td><td>USA</td><td>1-1</td><td>Australia</td></tr><tr><td>2</td><td>19-Jun</td><td>Turkiye</td><td>1-1</td><td>Paraguay</td></tr><tr><td>3</td><td>25-Jun</td><td>Turkiye</td><td>1-1</td><td>USA</td></tr><tr><td>3</td><td>25-Jun</td><td>Paraguay</td><td>1-1</td><td>Australia</td></tr></table>

<table><tr><td colspan="5">Group E Germany | Ivory Coast | Ecuador | Curacao</td></tr><tr><td>MD</td><td>Date</td><td>Team 1</td><td>Score</td><td>Team 2</td></tr><tr><td>1</td><td>14-Jun</td><td>Germany</td><td>2-1</td><td>Curacao</td></tr><tr><td>1</td><td>14-Jun</td><td>Ivory Coast</td><td>1-1</td><td>Ecuador</td></tr><tr><td>2</td><td>20-Jun</td><td>Germany</td><td>2-1</td><td>Ivory Coast</td></tr><tr><td>2</td><td>20-Jun</td><td>Ecuador</td><td>2-1</td><td>Curacao</td></tr><tr><td>3</td><td>25-Jun</td><td>Curacao</td><td>1-1</td><td>Ivory Coast</td></tr><tr><td>3</td><td>25-Jun</td><td>Ecuador</td><td>1-2</td><td>Germany</td></tr></table>

<table><tr><td colspan="5">Group F Netherlands | Sweden | Tunisia | Japan</td></tr><tr><td>MD</td><td>Date</td><td>Team 1</td><td>Score</td><td>Team 2</td></tr><tr><td>1</td><td>14-Jun</td><td>Netherlands</td><td>1-1</td><td>Japan</td></tr><tr><td>1</td><td>14-Jun</td><td>Sweden</td><td>1-1</td><td>Tunisia</td></tr><tr><td>2</td><td>20-Jun</td><td>Netherlands</td><td>2-1</td><td>Sweden</td></tr><tr><td>2</td><td>20-Jun</td><td>Tunisia</td><td>1-1</td><td>Japan</td></tr><tr><td>3</td><td>25-Jun</td><td>Japan</td><td>1-1</td><td>Sweden</td></tr><tr><td>3</td><td>25-Jun</td><td>Tunisia</td><td>1-2</td><td>Netherlands</td></tr></table>

<table><tr><td colspan="5">Group G Belgium | Iran | New Zealand | Egypt</td></tr><tr><td>MD</td><td>Date</td><td>Team 1</td><td>Score</td><td>Team 2</td></tr><tr><td>1</td><td>15-Jun</td><td>Belgium</td><td>1-1</td><td>Egypt</td></tr><tr><td>1</td><td>15-Jun</td><td>Iran</td><td>1-1</td><td>New Zealand</td></tr><tr><td>2</td><td>21-Jun</td><td>Belgium</td><td>1-1</td><td>Iran</td></tr><tr><td>2</td><td>21-Jun</td><td>New Zealand</td><td>1-1</td><td>Egypt</td></tr><tr><td>3</td><td>26-Jun</td><td>Egypt</td><td>1-1</td><td>Iran</td></tr><tr><td>3</td><td>26-Jun</td><td>New Zealand</td><td>1-1</td><td>Belgium</td></tr></table>

<table><tr><td colspan="5">Group H Spain | Saudi Arabia | Uruguay | Cape Verde</td></tr><tr><td>MD</td><td>Date</td><td>Team 1</td><td>Score</td><td>Team 2</td></tr><tr><td>1</td><td>15-Jun</td><td>Spain</td><td>3-0</td><td>Cape Verde</td></tr><tr><td>1</td><td>15-Jun</td><td>Saudi Arabia</td><td>1-1</td><td>Uruguay</td></tr><tr><td>2</td><td>21-Jun</td><td>Spain</td><td>3-0</td><td>Saudi Arabia</td></tr><tr><td>2</td><td>21-Jun</td><td>Uruguay</td><td>1-1</td><td>Cape Verde</td></tr><tr><td>3</td><td>26-Jun</td><td>Uru

[中间内容因长度限制已省略]

me have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
