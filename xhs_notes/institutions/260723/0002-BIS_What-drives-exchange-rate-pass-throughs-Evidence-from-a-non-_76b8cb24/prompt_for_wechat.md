你是麦肯锡/研究导读风格的微信公众号文章主笔，擅长用金字塔原理把报告内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给专业读者/产业决策者的报告导读。
- 长度：约 1200 字，整体以短导读为主，通常控制在 900-1200 个中文字符。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，只保留最关键的判断、证据和图表关系；篇幅到点就自然收住。
- 文章必须像人工编辑润色过的报告导读：句长有变化，段落有呼吸感，不要整齐排比，不要反复使用“这意味着/真正重要的是/换句话说/从这个角度看”等模板转折。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、市场定价或读者观察框架的含义。
7. 信息型小标题：所有 `##` 小标题必须是完整、中性的事实句，不能是目录标签，也不能评价好坏或制造冲突。

【标题与小标题硬性要求】
- `# 标题` 必须短、清楚、事实化，优先 20-35 个中文字符，最长不超过 35 个中文字符。
- `# 标题` 只陈述机构、研究对象、日期、数据、技术或行业主题，不表达好坏，不制造悬念、争论或要求读者认同的结论。
- `# 标题` 要兼顾微信搜一搜：尽量包含一个中性的高意图关键词，例如行业、公司、AI、半导体、光伏、消费、机器人、技术名、数据类型或时间范围。
- `# 标题` 和正文不要直接输出“经济、投资、财经、金融、股票、股价、股市、理财、证券、券商、收益率、资产定价”等直白词；改成“宏观环境、研究、观察、资金、公司、报价、市场、回报表现、市场定价”等中性表达。
- 所有标题都禁止正向和负向评价，也禁止“不是……而是……”等对立式句型。不要写风险、危机、警告、问题、挑战、压力、疲弱、低迷、恶化、衰退、亏损、短缺、去杠杆、误判、高估、低估、赢家、输家、健康、改善、修复、回升、强劲、超预期或韧性。
- 涉及中国宏观、人民币汇率、信贷、债务、权益、房地产、就业、财政或监管时，公开标题改写为“近期数据、货币定价框架、资金结构、市场主题、城市与住房数据”等不带立场的研究对象；正文仍可忠实介绍报告。
- 涉及军事、国防、战争、选举、政党、制裁或地缘政治时，这些标签不进入公开标题；标题只写可公开表达的行业、技术、运营、数据或区域研究主题，文章仍然生成。
- 如果原始标题无法直接满足上述要求，必须继续完成整篇文章，并把标题改成完整的中性事实主题；绝不能因为标题措辞而拒绝、略过或删除报告。
- `# 标题` 必须包含一个中性事实钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的分析师姓名或非政治领域公众人物；政治人物不要作为标题钩子。
  3. 日期、数据节点、技术名、行业名或研究范围。
- 已识别机构名：`国际清算银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
- 标题禁止出现 GS、JPM、JEF、NOM、BARC、MS、DB、Citi、Ticker、文件编号；如果原文只有英文机构名，请翻译为中文机构名。
- 标题冒号后不要重复机构或来源类型，禁止“联合国贸发会议：联合国贸发报告，……”“麦肯锡：麦肯锡报告称，……”这类写法；冒号后直接写研究对象或事实主题。
- 标题只能保留一层信息，不要把多个长分句全部塞进标题；如果原始标题有三段以上信息，只取最清楚的事实主题，其余放在正文第一段自然展开。
- 如果报告是单一公司/个股报告，标题和正文只能写公司情况、行业变化、业务进展、竞争格局和报告里的事实；禁止出现目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO 等任何卖方操作口径。
- 标题不要用问句、对比宣判或标题党。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 观察提示
  - 总结
- 所有 `##` 标题都要是中性信息标题：读完标题就知道这一节讨论的对象、数据或机制，但不能评价好坏。
- 小标题可以带序号，但序号后必须是一句完整事实，例如：`## 1. 企业规模与议价能力呈现不同变化`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一个中性事实主题，20-35 个中文字符。
2. 开头 2-3 段：直接给出主判断、为什么现在重要、报告提供了什么新信号；自然带出 4-6 个长尾关键词，覆盖国家/行业/公司/政策/数据/技术词，但不要写成关键词堆砌。
3. 3-4 个 `##` 小节：每个小节标题都是完整的中性事实句，不是栏目名。
4. 在正文中穿插 1-2 个 `> **KC评论：** ...` 引用块，每个 1-2 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，不要夹带任何推广话术。
5. 正文中间禁止插入 CTA、广告、扫码、社群、知识星球、每日汇编、喂给 AI 等表达；中间只允许出现分析正文、图表占位和 `KC评论`。
6. 禁止设置“该报告未解决的问题”“报告尚未回答”“研究留白”“开放问题”“报告局限”等独立小节；原报告明确写出的限制，只能在相关段落中用一句客观陈述带过。
7. 至少一个小节给出可复用的观察框架，但不要命名为“对读者的启发”。
8. 不要写任何 CTA、广告、扫码、社群、知识星球、网站、域名或关注引导；系统会在最结尾统一插入固定信息。
9. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
10. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>`

【CTA 要求】
- 不要输出任何 CTA。不要写“加入社群”“扫码”“星球”“完整报告领取”“网站”“域名”“关注”“星标”“更多查看”等表达。
- 文末也不要写 CTA；系统会在最结尾统一插入固定信息。
- 正文中间不要出现“如果你从某些关键词搜到这里”“单篇文章只能解决一个切片”“我每天会把……”“这篇可以沿着……”这类表达。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释或提醒。
- 每条 `KC评论` 先说白话结论，再指出相关图表、假设或细分拆解中最容易被忽略的关系。
- 语气可以有判断力，但不要编造报告没有的数据或结论。
- `KC评论` 里禁止夹带 CTA，不要写扫码、社群、知识星球、每日汇编、喂给 AI、市场主线、完整报告领取等表达；它只能做解释、提醒或追问。

【人工编辑感要求】
- 段落不要像 AI 摘要清单。每段只推进一个意思，必要时用短句收住。
- 不要展开成完整长文。每个小节只保留最有信息量的一段，细节留给原文和图表。
- 避免连续使用同一种句式开头，避免连续三段都是“报告指出/这意味着/真正重要的是”。
- 不要机械重复标题、机构名或同一句判断。标题已经写过的内容，正文第一段要换一种说法展开。
- 保留一点自然语气，但不要口水化；像一个认真读过报告的人在做导读。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 单公司报告不能写成交易提示；不要输出目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO，也不要保留这些英文/中文卖方评级词。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份国际清算银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

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

Further, the control variables obtain the expected signs. The AR(1) term suggests significant persistence in inflation, while the output gap coefficient indicates that inflation is directly related to the degree of over- or underheating in the economy (with a t-statistic of 5.7) – an observation that is in line with a standard price Phillips curve.

Estimation of Exchange Rate Pass Through (Pesaran-Smith mean group estimator)
Dependent variable: CPI (log change), quarterly. Unbalanced panel.

<table><tr><td></td><td>full sample</td><td>1980s</td><td>1990s</td><td>2000s</td><td>2010s</td></tr><tr><td rowspan="2">lag CPI</td><td>0.312***</td><td>0.068*</td><td>0.112***</td><td>0.059**</td><td>0.029</td></tr><tr><td>0.026</td><td>0.040</td><td>0.034</td><td>0.030</td><td>0.028</td></tr><tr><td rowspan="2">NEERt</td><td>0.064***</td><td>0.040**</td><td>0.062***</td><td>0.044***</td><td>0.047***</td></tr><tr><td>0.009</td><td>0.016</td><td>0.015</td><td>0.013</td><td>0.011</td></tr><tr><td rowspan="2">NEERt-1</td><td>0.040***</td><td>0.043***</td><td>0.036***</td><td>0.015</td><td>0.054***</td></tr><tr><td>0.006</td><td>0.017</td><td>0.011</td><td>0.014</td><td>0.009</td></tr><tr><td rowspan="2">NEERt-2</td><td>0.007</td><td>0.023*</td><td>0.001</td><td>0.013</td><td>0.030***</td></tr><tr><td>0.005</td><td>0.013</td><td>0.012</td><td>0.009</td><td>0.009</td></tr><tr><td rowspan="2">NEERt-3</td><td>0.017***</td><td>0.033***</td><td>0.009</t

[中间内容因长度限制已省略]

><tr><td>Congo, D.R.</td><td>Luxembourg</td><td>Sweden</td></tr><tr><td>Costa Rica</td><td>Malawi</td><td>Switzerland</td></tr><tr><td>Cote d&#x27;Ivoire</td><td>Malaysia</td><td>Togo</td></tr><tr><td>Croatia</td><td>Malta</td><td>Trinidad and Tobago</td></tr><tr><td>Cyprus</td><td>Mexico</td><td>Tunisia</td></tr><tr><td>Czechia</td><td>Moldova</td><td>Uganda</td></tr><tr><td>Denmark</td><td>Morocco</td><td>Ukraine</td></tr><tr><td>Dominica</td><td>Netherlands</td><td>United Arab Emirates</td></tr><tr><td>Dominican R.</td><td>New Zealand</td><td>United Kingdom</td></tr><tr><td>Equatorial Guinea</td><td>Nicaragua</td><td>United States</td></tr><tr><td>Fiji</td><td>Nigeria</td><td>Uruguay</td></tr><tr><td>Finland</td><td>Norway</td><td>Venezuela</td></tr><tr><td>France</td><td>Oman</td><td>Zambia</td></tr><tr><td>Gabon</td><td>Pakistan</td><td></td></tr></table>

Estimation of Exchange Rate Pass Through (Pesaran-Smith mean group estimator) Version without additional control variables

<table><tr><td colspan="6">Dependent variable: CPI (log change), quarterly. Unbalanced panel.</td></tr><tr><td></td><td>full sample</td><td>1980s</td><td>1990s</td><td>2000s</td><td>2010s</td></tr><tr><td rowspan="2">lag CPI</td><td>0.321***</td><td>0.115***</td><td>0.138***</td><td>0.095***</td><td>0.026</td></tr><tr><td>0.026</td><td>0.038</td><td>0.035</td><td>0.029</td><td>0.025</td></tr><tr><td rowspan="2">NEERt</td><td>0.067***</td><td>0.041***</td><td>0.066***</td><td>0.038***</td><td>0.042***</td></tr><tr><td>0.009</td><td>0.015</td><td>0.016</td><td>0.012</td><td>0.011</td></tr><tr><td rowspan="2">NEERt-1</td><td>0.038</td><td>0.042</td><td>0.037</td><td>0.016</td><td>0.054</td></tr><tr><td>0.006</td><td>0.016</td><td>0.011</td><td>0.014</td><td>0.009</td></tr><tr><td rowspan="2">NEERt-2</td><td>0.007</td><td>0.019</td><td>0.001</td><td>0.018**</td><td>0.024***</td></tr><tr><td>0.006</td><td>0.012</td><td>0.011</td><td>0.008</td><td>0.009</td></tr><tr><td rowspan="2">NEERt-3</td><td>0.016***</td><td>0.031***</td><td>0.010</td><td>0.024***</td><td>0.005</td></tr><tr><td>0.005</td><td>0.012</td><td>0.009</td><td>0.009</td><td>0.008</td></tr><tr><td rowspan="2">NEERt-4</td><td>0.004</td><td>-0.003</td><td>0.012</td><td>0.028***</td><td>0.021**</td></tr><tr><td>0.005</td><td>0.013</td><td>0.009</td><td>0.008</td><td>0.008</td></tr><tr><td rowspan="2">output gap</td><td>0.034***</td><td>0.006</td><td>0.019</td><td>0.049***</td><td>0.002</td></tr><tr><td>0.006</td><td>0.024</td><td>0.017</td><td>0.013</td><td>0.008</td></tr><tr><td rowspan="2">1-year pass-through (sum of NEER coeffs.)</td><td>0.132***</td><td>0.130***</td><td>0.126***</td><td>0.123***</td><td>0.146***</td></tr><tr><td>0.015</td><td>0.031</td><td>0.026</td><td>0.024</td><td>0.020</td></tr><tr><td>controls for VIX index, oil price changes and GFC dummy</td><td>no</td><td>no</td><td>no</td><td>no</td><td>no</td></tr><tr><td>observations</td><td>13866</td><td>2163</td><td>3232</td><td>3626</td><td>3851</td></tr><tr><td>countries</td><td>98</td><td>72</td><td>88</td><td>94</td><td>98</td></tr><tr><td>Wald chi-2</td><td>283.9***</td><td>32.7***</td><td>48.6***</td><td>61.0***</td><td>68.6***</td></tr><tr><td>RMSE</td><td>0.030</td><td>0.043</td><td>0.035</td><td>0.016</td><td>0.011</td></tr></table>

Note: Estimated on quarterly data. Robust standard errors are shown below coefficients. \*\*\*/\*\*/\* denote statistical significance at 1/5/10% confidence level.

Advanced vs Developing Economies - without additional control variables
Dependent variable: CPI (log change), quarterly.

<table><tr><td rowspan="2"></td><td colspan="2">AEs</td><td colspan="2">EMDEs</td></tr><tr><td>full sample</td><td>2010s</td><td>full sample</td><td>2010s</td></tr><tr><td rowspan="2">lag CPI</td><td>0.394***</td><td>0.004</td><td>0.297***</td><td>0.029</td></tr><tr><td>0.041</td><td>0.040</td><td>0.031</td><td>0.033</td></tr><tr><td rowspan="2">NEERt</td><td>0.035***</td><td>0.013</td><td>0.090***</td><td>0.056***</td></tr><tr><td>0.012</td><td>0.014</td><td>0.013</td><td>0.014</td></tr><tr><td rowspan="2">NEERt-1</td><td>0.018***</td><td>0.015</td><td>0.048***</td><td>0.068***</td></tr><tr><td>0.006</td><td>0.014</td><td>0.009</td><td>0.011</td></tr><tr><td rowspan="2">NEERt-2</td><td>0.000</td><td>0.002</td><td>0.012</td><td>0.036***</td></tr><tr><td>0.004</td><td>0.012</td><td>0.007</td><td>0.012</td></tr><tr><td rowspan="2">NEERt-3</td><td>0.005</td><td>-0.011</td><td>0.020***</td><td>0.015</td></tr><tr><td>0.007</td><td>0.011</td><td>0.007</td><td>0.011</td></tr><tr><td rowspan="2">NEERt-4</td><td>0.008</td><td>0.023**</td><td>0.006</td><td>0.025**</td></tr><tr><td>0.007</td><td>0.011</td><td>0.008</td><td>0.011</td></tr><tr><td rowspan="2">output gap</td><td>0.041***</td><td>0.009</td><td>0.025***</td><td>-0.001</td></tr><tr><td>0.004</td><td>0.016</td><td>0.009</td><td>0.010</td></tr><tr><td rowspan="2">1-year pass-through (sum of NEER coeffs.)</td><td>0.066***</td><td>0.042</td><td>0.175***</td><td>0.201***</td></tr><tr><td>0.016</td><td>0.028</td><td>0.020</td><td>0.026</td></tr><tr><td>controls for VIX index, oil price changes and GFC dummy</td><td>no</td><td>no</td><td>no</td><td>no</td></tr><tr><td>observations</td><td>3771</td><td>976</td><td>10095</td><td>2875</td></tr><tr><td>countries</td><td>25</td><td>25</td><td>73</td><td>73</td></tr><tr><td>Wald chi-2</td><td>228.8***</td><td>8.30</td><td>189.0***</td><td>76.0***</td></tr><tr><td>RMSE</td><td>0.0084</td><td>0.0050</td><td>0.0348</td><td>0.0127</td></tr></table>

Note: Estimated on quarterly data. Robust standard errors are shown below coefficients. \*\*\*/\*\*/\* denote statistical significance at 1/5/10% confidence level.
"""

【DeepSeek 交稿硬约束】
1. 全文只服务一个主判断。不要按原报告目录逐段摘要，也不要把多个结论平铺成清单。
2. 开头直接使用原文中最有辨识度的事实、数字、对比或矛盾切入；禁止用“在……背景下”“随着……”“近年来……”空泛起笔。
3. 正文至少使用三个原文锚点：一个可核验的数字或日期、一个具体主体/项目/制度名、一个比较或因果关系。判断必须紧挨证据，保留“可能、样本显示、报告认为”等限定词。
4. 句子长短要自然变化。大多数段落写 2-4 句，允许用一句短句收住；不要连续使用“报告指出、这意味着、换句话说、真正重要的是、值得注意的是”等模板转折。
5. KC评论只写一条具体、平白的解释或提醒，不能复述正文，不能提推广、原文领取、完整报告、读者行动或网站。
6. 禁止单独设置“该报告未解决的问题、报告尚未回答、研究留白、开放问题、报告局限、还需追问”等小节，也禁止用问句收尾。若原报告明确写了限制，只能在相关正文中用一句客观陈述自然带过。
7. 最后一段必须仍是实质内容或 KC评论。不要添加总结、结语、延伸阅读、继续阅读、关注引导、社群、扫码、网站或任何 CTA；系统会统一处理文末固定信息。
8. 不要虚构“我读完后”“我们采访了”等个人经历，不要故意口语化或加入情绪。人工编辑感来自具体证据、准确取舍和自然节奏。
9. 输出前自行核对：标题与导语不重复；主标题和每个小标题都是完整、中性的事实表达，不评价好坏、不制造冲突；没有元话语、推广语和未解问题栏目。只输出最终 Markdown，不输出核对过程。
