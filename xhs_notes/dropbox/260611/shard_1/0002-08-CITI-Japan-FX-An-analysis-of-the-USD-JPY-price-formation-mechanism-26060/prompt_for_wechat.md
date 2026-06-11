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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`Citi`。标题格式建议：`# Citi：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Citi研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
09 Jun 2026 04:41:47 ET | 15 pages

## Japan FX

An analysis of the USD/JPY price formation mechanism

## CITI'S TAKE

The US-Japan long-term interest rate spread has narrowed to an extent that clearly favors JPY appreciation against the USD. At the same time the significance of narrowing of the short-term interest rate spread should also not be ignored. The ongoing strength of the USDJPY despite this appears to be strongly affected by JPY-sell hedging demand that results from the historically high levels for Japanese equities. As a result, the estimate yielded by our multiple regression model also justifies the current level of the USDJPY. We see no need to change our bearish medium- to long-term view on the USDJPY. In our view, around ¥160/\$ will be the ceiling for the pair and it will correct lower to below ¥155/\$ by year-end. However, controlling occasional JPY weakness in the short run would require the normalization of monetary policy by the BoJ as well as JPY-selling intervention by the Japanese authorities.

## Osamu Takashima $^{AC}$

+81-3-6776-3251

osamu.takashima@citi.com

## Daniel Tobon

+1-212-816-8340

daniel.tobon@citi.com

## Brian Levine

+1-212-816-6896

brian.levine@citi.com

## Our fundamental view on USDJPY

Our fundamental view is that the USDJPY is strongly affected by 1) the monetary policy gap between the US and Japan, 2) overall market risk preferences, and 3) Japan's balance of payments (BoP), while price formation takes place within the overarching framework provided by the overall direction of the USD, for example against the EUR in particular.

If a fair value estimate is possible based on these four elements, then the fifth factor would be the daily deviation of the actual price from this estimate. This residual is normally seen as mispricing due to short-term speculative activities in the market, but forecasting this mispricing is in fact the most difficult task at the same time as being very important for market participants.

## Limits to market model

To analyze these five factors in real time requires the market data that makes available immediate prices rather than the monthly data that make up many economic statistics.

However, price formation for the USDJPY, Japanese equities, and JPY interest rates occurs as each of these market prices mutually affects the others. In other words, the independent variables in a market model analysis have significant characteristics of endogeneity and coinstantaneity, making it more difficult to identify relationships that are statistically significant in the strict sense.

It is possible to partly address this problem using a methodology such as vector autoregression (VAR), but there are internal limitations when applied to the analysis of market prices given that they are subject to the mutual influence of a large number of factors. In a market model that uses market prices, it will be practically impossible to make omitted variables equal zero, while it is only natural to assume that the problem of multicollinearity cannot ultimately be solved.

Even so, we find practical utility in the analysis to identify what factors do in reality affect changes in the USDJPY while recognizing these difficulties.

## Basic policy of practical model analysis

Normally the analysis of financial and economic time-series data requires breaking it down into 1) the trend component, 2) the cyclical component, and 3) the irregular component. When analyzing market data, if there is no notable seasonality successful detrending will enable the identification of stochastic variation.

However, in actual market operation identifying the trend is one of the most important tasks. If it cannot be identified accurately, what in terms of stochastic variation appears to be irregular change in market pricing simply becomes noise. At the same time, eliminating this noise should make identifying the long-term trend somewhat easier.

## Two-tiered (double decker) model for USDJPY

While keeping the above in mind, Figure 1 shows the multiple regression of a range of independent variables for the deviation of the USDJPY from its 200-day moving average. The purpose of finding the deviation from the 200-day moving average is to detrend the data, while it is only a very simple way.

The USDJPY and other exchange rates are generally seen as a random walk process (first-order integrated process or I(1) process), so it cannot be converted into a stationary process by detrending. Even so, understanding what type of variables accurately explain the deviation from the moving average is practically beneficial, and cyclical movement can be identified to some degree.

On the other hand, there is also the benefit that eliminating noise helps in the analysis of the medium- to long-term trend as typified by the 200-day moving average.

Our two-tiered model (double decker model) analyzes the data from 2017 through 2025, and we add dummy variables for 2022 while also adding the cross terms (interaction terms) to the analysis (we estimated both the intercept dummy and the slope dummy for 2022). During 2022 there was a great deal of change in market prices that was not normal due to the turmoil in global markets caused by the start of the Ukraine war and the resulting dramatic monetary tightening by the Fed and other central banks around the world.

The current estimate of this two-tiered model is around ¥161/\$, so the actual USDJPY looks slightly undervalued, perhaps because of intervention to buy the JPY by Japanese authorities. Even so, the extent of this undervaluation is currently very small, and there is no major distortion in the USDJPY relative to the model estimate (Figure 2).

As we discuss below, the USDJPY estimate has remained high despite the contraction in the US-Japan interest rate spread due in large part to the historically high levels for Japanese equities.

Figure 1. USD/JPY: Double decker model (estimate)  
![](images/745dfe0a652a109d8a583c9f9f9feabd5723104783052fb395230cec95e4e23e.jpg)

<details>
<summary>line chart</summary>

| Date       | Actual USD/JPY (USD/JPY) | Single Deck Model (USD/JPY) | Double Deck Model (USD/JPY) |
|------------|--------------------------|-----------------------------|-----------------------------|
| Jan-14     | ~105                     | ~103                        | ~104                        |
| Jan-16     | ~120                     | ~118                        | ~119                        |
| Jan-18     | ~115                     | ~113                        | ~114                        |
| Jan-20     | ~108                     | ~106                        | ~107                        |
| Jan-22     | ~130                     | ~128                        | ~129                        |
| Jan-24     | ~155                     | ~153                        | ~154                        |
| Jan-26     | ~160                     | ~158                        | ~159                        |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Note: The deviation from the 200-day MA is based on the actual 200-day MA in the single deck model and on our 200-day MA estimate in the double decker model.  
Source: Bloomberg, CitiFX, Citi

Figure 2. USD/JPY: Double decker model (deviation)  
![](images/dd816dd4181ac7cb7f8c5ec74b8449e1a3eab27319076a8fa64e6fc8eacc0a9e.jpg)

<details>
<summary>line chart</summary>

| Date       | Deviation from Single deck model | Deviation from Double deck model | USD/JPY (actual) [Rhs] |
|------------|----------------------------------|----------------------------------|------------------------|
| Jan-14     | ~3                               | ~5                               | ~-10                   |
| Jan-16     | ~-2                              | ~7                               | ~-10                   |
| Jan-18     | ~-1                              | ~5                               | ~-10                   |
| Jan-20     | ~0                               | ~7                               | ~-10                   |
| Jan-22     | ~-5                              | ~10                              | ~-10                   |
| Jan-24     | ~5                               | ~7                               | ~10                    |
| Jan-26     | ~10                              | ~5                               | ~10                    |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Note: The deviation from the 200-day MA is based on the actual 200-day MA in the single deck model and on our 200-day MA estimate in the double decker model.  
Source: Bloomberg, CitiFX, Citi

## Observation of the upper tier (superstructure)

Figure 3 shows the upper structure (superstructure) of the two-tier model, or in other words the percentage deviation of the USDJPY from its 200-day moving average and our estimate. Currently the estimate is some +4%, compared with the actual deviation of around +3%, so there is no particular disparity to the estimate.

Figure 4 outlines the structure of the upper tier. The independent variables are the deviation of 1) the US-Japan 10y government bond yield differential (nominal long-term interest rate spread), 2) Japanese equities (TOPIX), 3) the CitiFX commodity terms of trade (ToT) indices (spread between US and Japan), and 4) the USD index (DXY) from its 200-day moving average.

The two variables with by far the greatest explanatory power are 2) Japanese equities and 4) the USD index, while 1) the long-term interest rate spread and 3) the ToT index spread appear to have little explanatory power. However, simply accepting this interpretation is risky.

One reason is that for the USDJPY and Japanese equities, the former also has a strong influence on the latter (they have strong coinstantaneity). On the other hand, regarding the rate spread, change in USD interest rates is much larger than that in JPY interest rates, while normally the effect of the USDJPY on US interest rates is small. It is also possible that the direction of US interest rates has a strong impact on the model estimate even if only indirectly via change in the USD index.

Our daily analysis also indicates that the direction of the US-Japan interest rate spread, to which the USDJPY is highly sensitive, is a very important factor. While we do not incorporate it into this model, the short-term interest rate spread can on occasion have a greater impact than the long-term interest rate spread via hedging activity and carry trades by market participants.

Ultimately, this model analysis is not aimed at accurately identifying causal relationships, but rather to best explain actual movements in the USDJPY using a limited number of variables, so it is no more than a simplified market model.

Figure 3. USD/JPY: Double decker model (superstructure)  
![](images/ec962f78291bdbb9528c1d707e148ebc02d30be67c66cc37d7ff84ddb76b4997.jpg)

<details>
<summary>line chart</summary>

| Date       | Actual (% deviation from 200d MA) | Estimate (% deviation from 200d MA) | USD/JPY (Actual) [Rhs] |
|------------|-----------------------------------|-------------------------------------|------------------------|
| Jan-14     | ~0                                | ~0                                  | ~100                   |
| Jan-16     | ~15                               | ~15                                 | ~100                   |
| Jan-18     | ~0                                | ~0                                  | ~100                   |
| Jan-20     | ~0                                | ~0                                  | ~100                   |
| Jan-22     | ~15                               | ~15                                 | ~100                   |
| Jan-24     | ~10                               | ~10                                 | ~150                   |
| Jan-26     | ~5                                | ~5                                  | ~160                   |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Note: Deviation from 200-day MA.  
Source: Bloomberg, CitiFX, Citi

Figure 4. USD/JPY: Double decker model (outline for the superstructure)

<table><tr><td colspan="8">Regression Statistics</td></tr><tr><td>Multiple R</td><td>R Square</td><td>Adjusted R Square</td><td>Standard Error</td><td>Observations</td><td colspan="2">Estimate period</td><td>Dummy year</td></tr><tr><td>0.921</td><td>0.848</td><td>0.848</td><td>1.615</td><td>2,348</td><td colspan="2">Jan 2017 - Dec 2025</td><td>2022</td></tr><tr><td>Independent variables</td><td>Coefficients</td><td>Standard Error</td><td>t Stat</td><td>P-value</td><td>Lower 95%</td><td>Upper 95%</td><td>Coefficients (Standardized)</td></tr><tr><td>Intercept</td><td>-0.29</td><td>0.07</td><td>-4.27</td><td>0.00</td><td>-0.42</td><td>-0.16</td><td>1.64</td></tr><tr><td>Nominal 10y yield spread</td><td>0.32</td><td>0.12</td><td>2.69</td><td>0.01</td><td>0.09</td><td>0.56</td><td>0.13</td></tr><tr><td>TOPIX</td><td>0.28</td><td>0.01</td><td>45.89</td><td>0.00</td><td>0.27</td><td>0.29</td><td>2.06</td></tr><tr><td>CitiFX Commodity ToT Index spread</td><td>0.02</td><td>0.01</td><td>4.54</td><td>0.00</td><td>0.01</td><td>0.03</td><td>0.33</td></tr><tr><td>DXY</td><td>0.80</td><td>0.01</td><td>57.98</td><td>0.00</td><td>0.77</td><td>0.82</td><td>2.95</td></tr><tr><td>2022 Dummy</td><td>-0.67</td><td>0.54</td><td>-1.26</td><td>0.21</td><td>-1.72</td><td>0.38</td><td>-0.19</td></tr><tr><td>Interaction term (Nominal yield spread)</td><td>5.10</td><td>0.43</td><td>11.93</td><td>0.00</td><td>4.26</td><td>5.94</td><td>1.15</td></tr><tr><td>Interaction term (TOPIX)</td><td>-0.12</td><td>0.04</td><td>-3.09</td><td>0.00</td><td>-0.19</td><td>-0.04</td><td>-0.11</td></tr><tr><td>Interaction term (ToT Index spread)</td><td>-0.02</td><td>0.01</td><td>-1.34</td><td>0.18</td><td>-0.04</td><td>0.01</td><td>-0.25</td></tr><tr><td>Interaction term (DXY)</td><td>0.26</td><td>0.06</td><td>4.47</td><td>0.00</td><td>0.14</td><td>0.37</td><td>0.46</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Note: Deviation from 200-day MA.  
Source: Bloomberg, CitiFX, Citi

## Observation of lower tier (base structure)

Figure 5 shows the lower structure (base) of the two-tier model, or the 200-day average of the USDJPY and our estimate. Currently, the estimate is around ¥154/\$ and the actual 200-day moving average is about ¥155/\$, so the two are largely in line.

Figure 6 summarizes the lower structure of the model, and the independent variables are the 200-day moving averages of 1) the US-Japan 10-year inflation-linked bond yield differential (real long-term interest rate spread), 2) Japanese equities (log), 3) the Bloomberg Commodity Index (log), and 4) the USD index. The variables with by far the most explanatory power are again 2) Japanese equities and 4) the USD index, and we think the reasons are the same as those we note above for the upper structure.

The lower structure has a much higher coefficient of determination and t-value (the p-value is very low) so we suspect some type of spurious correlation. In other words, during this period the fundamental environment could have generated confounding factors that are simultaneously affecting all of forex rates, interest rates, equities, and resource prices.

One future task will be to identify economic indicators that have external explanatory power such as equity prices, real interest rates, and resource prices, and to use them as instrumental variables to increase the reliability of the analysis based on the lower structure of the USDJPY model.

Figure 5. USD/JPY: Double decker model (base)  
![](images/1a55293b41767267491ef1f979cb9d31c6b913ba21fa626a36e08d30447d32bc.jpg)

<details>
<summary>line chart</summary>

| Date Range           | Actual USD/JPY (USD/JPY) | 200d MA USD/JPY (USD/JPY) | 200d MA Estimate USD/JPY (USD/JPY) |
|----------------------|--------------------------|---------------------------|------------------------------------|
| Jan 2017- Dec 2025   | ~115                     | ~118                      | ~115                               |
| Jan 2022- Dec 2022   | ~150                     | ~145                      | ~148                               |
| Jan 2026- Dec 2026   | ~160                     | ~155                      | ~158                               |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Note: 200-day moving average (MA).  
Source: Bloomberg, Citi

Figure 6. USD/JPY: Double decker model (outline for the base)

<table><tr><td colspan="8">Regression Statistics</td></tr><tr><td>Multiple R</td><td>R Square</td><td>Adjusted R Square</td><td>Standard Error</td><td>Observations</td><td colspan="2">Estimate period</td><td>Dummy year</td></tr><tr><td>0.997</td><td>0.994</td><td>0.994</td><td>1.294</td><td>2,348</td><td colspan="2">Jan 2017 - Dec 2025</td><td>2022</td></tr><tr><td>Independent variables</td><td>Coefficients</td><td>Standard Error</td><td>t Stat</td><td>P-value</td><td>Lower 95%</td><td>Upper 95%</td><td>Coefficients (Standardized)</td></tr><tr><td>Intercept</td><td>-411.49</td><td>1.72</td><td>-238.83</td><td>0.00</td><td>-414.87</td><td>-408.11</td><td>122.76</td></tr><tr><td>Real 10y yield spread</td><td>2.24</td><td>0.05</td><td>45.67</td><td>0.00</td><td>2.15</td><td>2.34</td><td>2.44</td></tr><tr><td>TOPIX (log)</td><td>48.87</td><td>0.20</td><td>242.04</td><td>0.00</td><td>48.48</td><td>49.27</td><td>9.90</td></tr><tr><td>Bloomberg Com-modity Index (log)</td><td>4.83</td><td>0.37</td><td>13.06</td><td>0.00</td><td>4.11</td><td>5.56</td><td>0.72</td></tr><tr><td>DXY</td><td>1.43</td><td>0.01</td><td>146.74</td><td>0.00</td><td>1.41</td><td>1.45</td><td>6.64</td></tr><tr><td>2022 Dummy</td><td>555.52</td><td>243.61</td><td>2.28</td><td>0.02</td><td>77.82</td><td>1,033.23</td><td>174.36</td></tr><tr><td>Interaction term (Real yield spread)</td><td>5.42</td><td>2.61</td><td>2.08</td><td>0.04</td><td>0.30</td><td>10.53</td><td>1.23</td></tr><tr><td>Interaction term (TOPIX)</td><td>-59.34</td><td>29.55</td><td>-2.01</td><td>0.04</td><td>-117.29</td><td>-1.40</td><td>-141.01</td></tr><tr><td>Interaction term (Commodity Index)</td><td>-8.22</td><td>5.58</td><td>-1.47</td><td>0.14</td><td>-19.16</td><td>2.72</td><td>-12.15</td></tr><tr><td>Interaction term (DXY)</td><td>-0.71</td><td>0.50</td><td>-1.41</td><td>0.16</td><td>-1.69</td><td>0.28</td><td>-21.97</td></tr

[中间内容因长度限制已省略]

lar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
