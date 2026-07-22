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
- 默认避免出现具体投行品牌名，比如“高盛”“Goldman Sachs”，统一写作“某外资投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【推荐写法】
- 开头直接给一个自然判断，不要加“结论：”标签。
- 中间用 1/2/3 拆逻辑，但小标题要像正常内容标题，不要像写作模板。
- 结尾可以留下一个自然讨论问题，但不要引导关注、点赞或评论。
- 最后一行输出 2-4 个标签，优先：`#学习笔记 #研究笔记 #学习研究 #研报解读`。

【研报解析内容】
"""
![](images/d0df815bb140287c4b16eacb70b66c01d04417cccfe169bfe2817a04bdd92272.jpg)

## BIS Working Papers No 1371

What drives exchange rate pass-throughs? Evidence from a non-parametric method

by Emanuel Kohlscheen and Aaron Mehrotra

Monetary and Economic Department

July 2026

JEL classification: E30, E31, E58, F31, F41

Keywords: inflation, exchange rate pass-through, Phillips curve

BIS Working Papers are written by members of the Monetary and Economic Department of the Bank for International Settlements, and from time to time by other economists, and are published by the Bank. The papers are on subjects of topical interest and are technical in character. The views expressed in this publication are those of the authors and do not necessarily reflect the views of the BIS or its member central banks.

This publication is available on the BIS website (www.bis.org).

ISSN 1020-0959 (print)
ISSN 1682-7678 (online)

# What drives exchange rate pass-throughs? Evidence from a non-parametric method

Emanuel Kohlscheen and Aaron Mehrotra $^{1,2}$

## Abstract

We provide new evidence on the drivers of the pass-through of exchange rate movements into consumer prices across four decades and close to a hundred countries, combining econometrics and random forests. Random forests are particularly useful for modelling highly non-linear relationships, as well as for identifying the relative importance of the different theoretical factors that can affect the degree of pass-through. We find that the size of the economy, which tends to be related to the extent of pricing-to-market, and the level of inflation emerge as the factors most strongly associated with exchange rate pass-through, followed by product homogeneity and the volatility of the exchange rate. As we show, several of these covariates display a non-linear relation with exchange rate pass-throughs. We also document important implications of macroeconomic policy regimes and outcomes, including those related to fiscal policy, for exchange rate pass-through.

JEL Classification: E30; E31; E58; F31; F41.

Keywords: inflation; exchange rate pass-through; Phillips curve.

## 1. Introduction

The extent to which exchange rates affect CPI inflation typically varies a great deal between countries and time periods. At the country level, identifying the impact of the exchange rate on inflation often involves substantial uncertainty, owing to the small number of time series observations and, at times, regime changes. At the same time, while there is a large empirical literature on measuring exchange rate pass-through, much less is known about precisely which factors drive its magnitude and the relative contribution of the different drivers.

A better understanding of the relationship between exchange rate pass-through and the macroeconomic and structural characteristics of different economies is of particular interest post-pandemic. This stems from the sudden and largely unexpected return of higher inflation globally; the associated changes in pricing behaviour and the dramatic shift in the fiscal and monetary landscape; as well as the shifting patterns of trade and globalisation due to geopolitical fragmentation. This raises questions about how the relationship between exchange rates and consumer prices might change if macroeconomic or structural characteristics of the economies were to undergo persistent changes.

The present study throws new light on these issues. It does so by analysing a broad panel of countries over the last 40 years in an empirical framework that, while taking advantage of the larger precision brought about by the large number of observations, also allows for heterogeneous pass-through slopes across countries. Moreover, and in contrast to previous research on exchange rate pass-through, the study uses random forests to quantify precisely the relative contribution of the different economic factors to exchange rate pass-through. The non-parametric approach is particularly useful for modelling highly non-linear relationships. While non-linear effects have been noted in previous studies on exchange rate pass-through (see e.g. Jašová et al (2019)), our study is to our knowledge the first to employ such techniques to model them.

We first show that while the exchange rate pass-through is typically fast, its extent has declined over time. The first-stage Pesaran and Smith (1995) mean group estimators show a pass-through decline from 7.6% over the full sample to 4.4% during the last decade in advanced economies. The corresponding pass-through for a broad group of EMDEs has changed less over time, hovering at around 17–20%.

We then show how non-parametric methods can enrich the analysis and interpretation further. More specifically, in the second step, we rely on the well-established technique of random forests (Breiman (2001)) to link the estimated pass-throughs to the potential factors that have been highlighted in the theoretical literature. This method has the key advantage that it is relatively transparent and does not require subtle tuning of the parameters (Athey and Imbens (2019)). $^{3}$

The random forests approach pins down the size of the economy and the level of inflation as the factors most strongly associated with the extent of pass-through across countries and time. This is followed by the extent of product homogeneity and exchange rate volatility. Perhaps surprisingly, given its salience in the previous literature (e.g. Campa and Goldberg (2005, 2010) and Campa and Mínguez (2006)), the degree of trade openness emerges as the least important factor, among the key variables considered in this paper, in terms of its relationship with pass-through.

We also highlight a number of additional findings.

Interestingly, without imposing any prior or functional form, partial effects from our non-parametric method reveal that pass-throughs are modest as long as inflation stays below

5%. This suggests that a successful pursuit of stable prices is key to assure a limited degree of exchange rate pass-through.

Moreover, we find that the relationship between exchange rate volatility and pass-through is highly non-linear. The strength of the pass-through initially declines as exchange rate volatility rises from low levels, and it reaches a minimum for intermediate levels of exchange rate volatility. The degree of pass-through then increases again as exchange rate volatility rises further. The shape of this U-curve during the last 40 years, and its minimum, are precisely mapped by our data-driven method. Policymakers that wish to stabilise domestic inflation and/or better insulate their economies from global exchange rate movements could potentially assess FX market volatility against this benchmark.

Finally, we analyse the effects of policy regimes and outcomes on exchange rate pass-through. We document that the degree of pass-through is lowest for small deviations of inflation from its target, when the de facto exchange rate regime is either a managed or a free float, and when fiscal policy credibility – proxied here by sound fiscal accounts – is high. To our knowledge, our paper is the first to provide evidence that the degree of pass-through is related to the fiscal health of the sovereign.

Relation to the literature. As the extent of exchange rate pass-through is a central question in macroeconomics, both in open economy modelling and for policy making, the academic literature on the topic is very extensive. We do not aim to provide a full review of this literature here, but rather highlight a selection of papers which relate to ours more directly. $^{4}$

Empirical studies generally concur that exchange rate pass-through has fallen significantly across the world. These include for instance Marazzi and Sheets (2007), Gust el al (2010), Frankel et al (2012) and Jašová et al (2019), among others. Furthermore, most papers conjecture that the fall is related to the drop in average inflation. Alternatively, Bergin and Feenstra (2009) attribute a large share of the decline in pass-through in the United States to increased trade with fixed exchange rate countries, most notably China.

Relatedly, Devereux and Yetman (2010) show how the degree of exchange rate pass-through in an open economy is essentially driven by the speed of adjustment of prices. When the authors allow the frequency of price adjustments in their theoretical model to be endogenous, they find that pass-through is increasing in the average level of inflation. Also Taylor (2000), Choudhri et al. (2005) and Choudhri and Hakura (2006) reach similar conclusions using different methodologies. And, in the general equilibrium model of Devereux et al (2004), the degree of pass-through is tightly linked to monetary stability, with countries with lower money growth volatility featuring lower pass-throughs.

Another stand of the literature emphasises the relevance of exchange rate volatility. Among earlier studies, Krugman (1987) and Froot and Klemperer (1989) posit that the extent of pass-through is connected to the variability of the exchange rate. Following this rationale, Flodén and Wilander (2006) elaborate that if economic agents use (S,s) type price adjustment rules, higher exchange rate variability would mean more frequent touching of adjustment thresholds, implying a higher pass-through. Kohlscheen (2010) finds that emerging markets with higher exchange rate volatility indeed had higher pass-through coefficients in the years that followed the inception of a floating regime. That said, the sample was limited to only eight of the larger emerging markets. $^{5}$

On the other hand, Corsetti et al (2008) show within a theoretical model that even modest nominal frictions can generate stable local currency pricing, and thus a small pass-through coefficient. And Jiménez-Rodríguez and Morales-Zumaquero (2016) empirically document that – with the exception of Japan – larger exchange rate volatility reduced pass-throughs. Given these contrasting results, the effect of exchange rate volatility on pass-through remains a question of debate.

There have been fewer attempts to relate the degree of pass-through to the structural characteristics of economies. Dornbusch (1987) and Menon (1995) link it to country size, indicating that pass-throughs would be smaller in large countries. This is because pricing-to-market is more pervasive in these. Similarly, Goldberg and Tille (2008) argue that the share of invoicing in the currency of the destination country would be higher for larger (destination) countries. $^{6}$ Campa and Goldberg (2005) however find no significant effect of country size in their analysis of the pass-through to import prices in 23 OECD countries.

Further, Campa and Goldberg (2005) and Auer and Chaney (2009) point out that the pass-through coefficient should theoretically be lower if a large share of traded goods is differentiated, as opposed to homogeneous. Antoniades and Zaniboni (2016), and Chen and Juvenal (2016) indeed find a lower pass-through for higher quality goods in the cases of, respectively, retail prices in the United Arab Emirates and Argentine wine exports. On the other hand, Auer and Chaney (2009) report only weak empirical evidence for their theoretical prediction when analysing granular U.S. import data.

The novelty of the current study is twofold. First, we provide novel estimates of pass-throughs relying on a large number of countries and observations, while at the same time allowing for heterogeneous effects across countries. Second, we link the estimated pass-throughs to various macroeconomic and structural factors with precision, using a well-established non-parametric method.

While the random forest analysis confirms some of the findings from the previous literature, in particular the importance of the average level of inflation and country size for pass-throughs, it also provides a number of new findings. This stems from the ability of the method to pin down non-linear dependencies and minimums, for instance with respect to exchange rate variability. More specifically, we find an inflection point at an intermediate level of exchange rate volatility. For significantly lower or higher levels of volatility, the pass-through is found to be much higher. This finding enables the reconciliation of apparent contradictions in the previous literature regarding the relationship between exchange rate volatility and pass-through.

Outline. The article proceeds as follows. Section 2 gives the background and presents the data that were used. Section 3 shows the first-stage econometric estimates. Section 4 explains the random forest method and shows the relative importance of the various factors as well as the partial effects of the key drivers of pass-throughs. Section 5 delves further into the importance of policy related variables for exchange rate pass-through. Section 6 concludes.

## 2. Background and Data

The analysis that follows is based on a comprehensive sample of countries for which the CPI index, the nominal effective exchange rate (NEER) and the output gap are available from the IMF's International Financial Statistics. We also exclude countries where there are less than 20 quarters of data within a given decade. The resulting sample of 98 economies is shown in Table A1 in the Appendix. The data used for estimating exchange rate pass-through are quarterly. The IMF's annual output gap is linearly interpolated to match this frequency. $^{7}$

We classify all economies whose GDP in 2023 exceeded \$30,000 per capita as advanced economies. This group comprises 25 economies and includes countries whose income level is currently at or above those of Italy and South Korea. $^{8}$ The remaining countries are classified as emerging market and developing economies (EMDEs). $^{9}$

Inflation declined sharply in both income groups in the 1990s. Figure 1 shows the evolution of medians by country group and decade. Among EMDEs, the decline continued into the following decade, as more countries adopted inflation targeting regimes. During the 2010s, median inflation touched a low of 1.6% in advanced economies and 3.7% in EMDEs.

Figure 1 also shows corresponding evidence for nominal exchange rate volatility, measured by the average absolute log variation in the NEER. Exchange rate volatility has been low in advanced economies throughout the sample and declined further in the current millennium. By contrast, among EMDEs volatility increased during the crisis-prone 1990s. Since then, however, median exchange rate volatility has seen a sharp decline in this country group as well. While exchange rate volatility in EMEs was roughly double that of AEs in the 1980s and as much as 150% larger in the 1990s, the difference fell to 67% in the 2000s and then further to only 29% during the last decade.

Note that the country coverage underlying these trends increases over time. Whereas 72 countries are included in the 1980s, the coverage increases to 98 countries by the 2010s – as data availability for EMDEs improves.

![](images/e61e7008f14eb1d8928bad80f32bcb57e3b377c9431a2c7d0e5a4be9e285bd0c.jpg)

## 3. Econometric Estimation of Pass-Throughs

Pass-throughs are estimated using the Pesaran and Smith (1995) mean group estimator. This method has the key advantage that it allows for heterogeneity in the transmission of exchange rate changes to inflation across countries. In contrast, a typical panel data approach that imposes the same coefficient for every country would not allow us to explain heterogeneity in pass-throughs across countries in the second stage. To be more specific, our estimated equation is given by

$$
\pi_ {i, t} = \alpha^ {i} \cdot \pi_ {i, t - 1} + \beta^ {i} \cdot y g a p _ {i, t} + \sum_ {k = 0} ^ {4} \gamma_ {k} ^ {i} \cdot \varDelta e _ {i, t - k} + \theta_ {i} + \varepsilon_ {i, t},
$$

where $\pi_{i,t}$ is the log difference of the price level in country i at quarter t, $ygap_{i,t}$ is the output gap, $\Delta e_{i,t-k}$ is the log difference of the nominal effective exchange rate in country i at quarter t-k, $\theta_{i}$ is the country-specific intercept (i.e. country fixed effect) $^{10}$ and $\varepsilon_{i,t}$ the error term. The estimated coefficients are allowed to differ from country to country. That is, $\alpha^{i} = \alpha + \eta_{1i}$ , $\beta^{i} = \beta + \eta_{2i}$ and so on. We estimate the above relation with and without additional controls for the variation in Brent crude oil prices, the CBOE stock market volatility index and a dummy variable that takes the value one during the global financial crisis of 2008-09. $^{11}$

The full sample results show that exchange rate pass-through is typically quite fast. $^{12}$ Table 1 shows the estimated mean effects for the full sample and by decade, as well as the resulting exchange rate pass-throughs within a 1-year horizon. The coefficients are computed as outlier-robust means. What is clear is that the bulk of the impact on inflation occurs within the same quarter of the exchange rate change, or in the quarter immediately after. The average 1-year pass-through for this broad sample of 98 countries is 13.4%, with a t-statistic of 9.6.

Further, the contr

[中间内容因长度限制已省略]

nica</td><td>Netherlands</td><td>United Arab Emirates</td></tr><tr><td>Dominican R.</td><td>New Zealand</td><td>United Kingdom</td></tr><tr><td>Equatorial Guinea</td><td>Nicaragua</td><td>United States</td></tr><tr><td>Fiji</td><td>Nigeria</td><td>Uruguay</td></tr><tr><td>Finland</td><td>Norway</td><td>Venezuela</td></tr><tr><td>France</td><td>Oman</td><td>Zambia</td></tr><tr><td>Gabon</td><td>Pakistan</td><td></td></tr></table>

Estimation of Exchange Rate Pass Through (Pesaran-Smith mean group estimator) Version without additional control variables

<table><tr><td colspan="6">Dependent variable: CPI (log change), quarterly. Unbalanced panel.</td></tr><tr><td></td><td>full sample</td><td>1980s</td><td>1990s</td><td>2000s</td><td>2010s</td></tr><tr><td rowspan="2">lag CPI</td><td>0.321***</td><td>0.115***</td><td>0.138***</td><td>0.095***</td><td>0.026</td></tr><tr><td>0.026</td><td>0.038</td><td>0.035</td><td>0.029</td><td>0.025</td></tr><tr><td rowspan="2">NEERt</td><td>0.067***</td><td>0.041***</td><td>0.066***</td><td>0.038***</td><td>0.042***</td></tr><tr><td>0.009</td><td>0.015</td><td>0.016</td><td>0.012</td><td>0.011</td></tr><tr><td rowspan="2">NEERt-1</td><td>0.038</td><td>0.042</td><td>0.037</td><td>0.016</td><td>0.054</td></tr><tr><td>0.006</td><td>0.016</td><td>0.011</td><td>0.014</td><td>0.009</td></tr><tr><td rowspan="2">NEERt-2</td><td>0.007</td><td>0.019</td><td>0.001</td><td>0.018**</td><td>0.024***</td></tr><tr><td>0.006</td><td>0.012</td><td>0.011</td><td>0.008</td><td>0.009</td></tr><tr><td rowspan="2">NEERt-3</td><td>0.016***</td><td>0.031***</td><td>0.010</td><td>0.024***</td><td>0.005</td></tr><tr><td>0.005</td><td>0.012</td><td>0.009</td><td>0.009</td><td>0.008</td></tr><tr><td rowspan="2">NEERt-4</td><td>0.004</td><td>-0.003</td><td>0.012</td><td>0.028***</td><td>0.021**</td></tr><tr><td>0.005</td><td>0.013</td><td>0.009</td><td>0.008</td><td>0.008</td></tr><tr><td rowspan="2">output gap</td><td>0.034***</td><td>0.006</td><td>0.019</td><td>0.049***</td><td>0.002</td></tr><tr><td>0.006</td><td>0.024</td><td>0.017</td><td>0.013</td><td>0.008</td></tr><tr><td rowspan="2">1-year pass-through (sum of NEER coeffs.)</td><td>0.132***</td><td>0.130***</td><td>0.126***</td><td>0.123***</td><td>0.146***</td></tr><tr><td>0.015</td><td>0.031</td><td>0.026</td><td>0.024</td><td>0.020</td></tr><tr><td>controls for VIX index, oil price changes and GFC dummy</td><td>no</td><td>no</td><td>no</td><td>no</td><td>no</td></tr><tr><td>observations</td><td>13866</td><td>2163</td><td>3232</td><td>3626</td><td>3851</td></tr><tr><td>countries</td><td>98</td><td>72</td><td>88</td><td>94</td><td>98</td></tr><tr><td>Wald chi-2</td><td>283.9***</td><td>32.7***</td><td>48.6***</td><td>61.0***</td><td>68.6***</td></tr><tr><td>RMSE</td><td>0.030</td><td>0.043</td><td>0.035</td><td>0.016</td><td>0.011</td></tr></table>

Note: Estimated on quarterly data. Robust standard errors are shown below coefficients. \*\*\*/\*\*/\* denote statistical significance at 1/5/10% confidence level.

Advanced vs Developing Economies - without additional control variables
Dependent variable: CPI (log change), quarterly.

<table><tr><td rowspan="2"></td><td colspan="2">AEs</td><td colspan="2">EMDEs</td></tr><tr><td>full sample</td><td>2010s</td><td>full sample</td><td>2010s</td></tr><tr><td rowspan="2">lag CPI</td><td>0.394***</td><td>0.004</td><td>0.297***</td><td>0.029</td></tr><tr><td>0.041</td><td>0.040</td><td>0.031</td><td>0.033</td></tr><tr><td rowspan="2">NEERt</td><td>0.035***</td><td>0.013</td><td>0.090***</td><td>0.056***</td></tr><tr><td>0.012</td><td>0.014</td><td>0.013</td><td>0.014</td></tr><tr><td rowspan="2">NEERt-1</td><td>0.018***</td><td>0.015</td><td>0.048***</td><td>0.068***</td></tr><tr><td>0.006</td><td>0.014</td><td>0.009</td><td>0.011</td></tr><tr><td rowspan="2">NEERt-2</td><td>0.000</td><td>0.002</td><td>0.012</td><td>0.036***</td></tr><tr><td>0.004</td><td>0.012</td><td>0.007</td><td>0.012</td></tr><tr><td rowspan="2">NEERt-3</td><td>0.005</td><td>-0.011</td><td>0.020***</td><td>0.015</td></tr><tr><td>0.007</td><td>0.011</td><td>0.007</td><td>0.011</td></tr><tr><td rowspan="2">NEERt-4</td><td>0.008</td><td>0.023**</td><td>0.006</td><td>0.025**</td></tr><tr><td>0.007</td><td>0.011</td><td>0.008</td><td>0.011</td></tr><tr><td rowspan="2">output gap</td><td>0.041***</td><td>0.009</td><td>0.025***</td><td>-0.001</td></tr><tr><td>0.004</td><td>0.016</td><td>0.009</td><td>0.010</td></tr><tr><td rowspan="2">1-year pass-through (sum of NEER coeffs.)</td><td>0.066***</td><td>0.042</td><td>0.175***</td><td>0.201***</td></tr><tr><td>0.016</td><td>0.028</td><td>0.020</td><td>0.026</td></tr><tr><td>controls for VIX index, oil price changes and GFC dummy</td><td>no</td><td>no</td><td>no</td><td>no</td></tr><tr><td>observations</td><td>3771</td><td>976</td><td>10095</td><td>2875</td></tr><tr><td>countries</td><td>25</td><td>25</td><td>73</td><td>73</td></tr><tr><td>Wald chi-2</td><td>228.8***</td><td>8.30</td><td>189.0***</td><td>76.0***</td></tr><tr><td>RMSE</td><td>0.0084</td><td>0.0050</td><td>0.0348</td><td>0.0127</td></tr></table>

Note: Estimated on quarterly data. Robust standard errors are shown below coefficients. \*\*\*/\*\*/\* denote statistical significance at 1/5/10% confidence level.
"""
