你是资深小红书内容策划 + 投研翻译官，擅长把英文/中文研报改写成高互动、可收藏、可转发的中文小红书笔记。

【目标】
- 把下面的研报解析内容，改写成一篇中文小红书笔记。
- 风格：投研博主风：信息密度高，但像给朋友讲逻辑
- 长度：不超过 1000 字，信息密度高但不要写长文。
- emoji 密度：中

【必须输出的结构】
1. 第一行：标题，20 字以内，不要像论文标题，也不要用夸张极限词。
2. 第二行：封面短标题，10 字以内，适合放在图中间。
3. 第三行：封面副标题，10-18 字，短句。
4. 正文分段清晰，每段不超过 3 行，可以用编号、小标题或加粗。
5. 正文要自然呈现观点，但不要暴露写作框架或思考过程。
6. 末尾可以保留 2-4 个相关标签，只允许从这些标签里选择：`#学习笔记`、`#研究笔记`、`#学习研究`、`#研报解读`。

【严禁输出】
- 不要出现这些栏目名或类似栏目名：`一句话结论`、`我最想提醒的一点`、`配图建议`、`免责声明`、`非投资建议`、`仅做学习交流`、`仅作学习交流`。
- 不要在正文最后追加配图建议，不要告诉我第 2/3/4 张图怎么配文。
- 不要输出任何包含“投资”的免责声明，也不要输出“非投资建议”这种表述。
- 不要输出财经敏感标签：`#投资学习`、`#财经`、`#金融`、`#股票`、`#基金`、`#理财`。
- 不要输出无关标签：`#小红书笔记`、`#笔记分享`、`#干货分享`。
- 不要写“关注”“点赞”“求关注”“评论区见”“评论区留言”等直接互动诱导；可以写“欢迎一起讨论”“可以继续交流”。

【平台发布合规要求】
- 不要写“爆款”“震惊”“必看”“必读”“最强”“最全”“唯一”“全网首发”等极限词或夸张词。
- 不要写“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要放在中性语境里。
- 不要承诺收益，不要引导交易，不要暗示确定性结果。

【内容要求】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 可以把专业表达翻成人话，但不能扭曲意思。
- 遇到不确定或缺失信息：用“研报未给出”或“这里是推测”明确标注。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【推荐写法】
- 开头直接给一个自然判断，不要加“结论：”标签。
- 中间用 1/2/3 拆逻辑，但小标题要像正常内容标题，不要像写作模板。
- 结尾可以留下一个自然讨论问题，但不要引导关注、点赞或评论。
- 最后一行输出 2-4 个标签，优先：`#学习笔记 #研究笔记 #学习研究 #研报解读`。

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

<table><tr><td colspan="8">Regression Statistics</td></tr><tr><td>Multiple R</td><td>R Square</td><td>Adjusted R Square</td><td>Standard Error</td><td>Observations</td><td colspan="2">Estimate period</td><td>Dummy year</td></tr><tr><td>0.997</td><td>0.994</td><td>0.994</td><td>1.294</td><td>2,348</td><td colspan="2">Jan 2017 - Dec 2025</td><td>2022</td></tr><tr><td>Independent variables</td><td>Coefficients</td><td>Standard Error</td><td>t Stat</td><

[中间内容因长度限制已省略]

ard Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
