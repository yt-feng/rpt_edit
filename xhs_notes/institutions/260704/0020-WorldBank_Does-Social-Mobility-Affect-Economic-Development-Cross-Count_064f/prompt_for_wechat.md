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
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`世界银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
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
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：加入社群，领取完整研报解读与原始图表。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定套话。它需要自然包含这些信息：更多国际信源汇编&评论，扫码交流，每日更新，汇总国际主流叙事&数据&图表，观测边际变化；汇聚了头部券商、PE/VC、投行、并购、hedge fund、资管机构、战略咨询、智库等朋友，期待交流。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份世界银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Does Social Mobility Affect Economic Development?

Cross-Country Analysis Using Different Mobility Measures

Iván Torre

Michael Lokshin

James Foster

POLICY RESEARCH WORKING PAPER 11056

## Abstract

This paper analyzes the relationship between intergenerational educational mobility and long-term growth across the world using different mobility measures, comparing absolute mobility indicators with relative mobility indicators. The analysis is carried out across a panel of 68 countries over 2000–20. The results indicate that upward mobility in higher education is positively associated with gross domestic product per capita in Europe and Central Asia, but relative mobility indicators are uncorrelated with country income. In Latin America, higher relative mobility is associated with lower income, and higher absolute mobility is associated with higher income. The remaining regions of the world show a mix of these patterns.

# Does Social Mobility Affect Economic Development? Cross-Country Analysis Using Different Mobility Measures

Iván Torre, Michael Lokshin, and James Foster $^{1}$

Keywords: Intergenerational social mobility, education, economic growth

JEL: D63, I24, J62, O15, O52

## 1. Introduction

Technological progress is the primary driver of economic growth and improvements in living standards. However, higher spending on research and development alone may be insufficient to fuel breakthrough scientific innovations that require an increasing flow of talented, well-trained people (Romer 2000). When all the talents in society are fully realized, the labor markets become more efficient, and productivity grows at a faster rate. But only in socially mobile societies, where family circumstances do not matter in explaining educational outcomes, can talent be better allocated. Thus, it is expected that socially mobile societies may also be more prosperous. The extent to which this expectation is true remains unclear.

Complex interactions between inherited traits, social norms, the environment in which children are raised, labor markets, and public policies determine individuals' opportunities to reach their full potential. Education plays a major role in defining a person's career trajectory and lifetime earnings. The level of investment in a child's education strongly depends on parental income and human capital as well as on parental preferences and risk perceptions (Christoph et al. 2024). Better-educated parents not only earn more, but they are also more effective in producing human capital in their children. The complementarity between parental human capital and investments in children leads wealthier parents to invest more in their children's human capital than poor parents do (Heckman and Mosso 2014; Becker and others 2018). Without government involvement, the intergenerational persistence of education will perpetuate cross-generational income inequality, reducing the chances of talented children from poor families succeeding in life (Corak 2013; van der Weide and others 2023). By drawing such children into science and innovation, policies designed to improve intergenerational mobility could increase the number of inventors and boost economic growth (Bell and others 2019). In fact, as the social returns on discoveries usually greatly exceed the personal returns to innovators, the case for public policy interventions is strong.

A challenge in making policy inferences from the analysis of intergenerational educational mobility is the possibility that the observed immobility is a consequence of other economic failures in society. For example, the primogeniture that strongly suppresses social mobility could be a response to inefficient capital markets and the need to ensure a minimal firm size (Rodríguez 2009). Comparing intergenerational mobility across countries and relying on cross-country variations in educational and welfare policies and regulations could help (partially) disentangle the contributions of different correlates of social mobility.

This paper analyzes the link between changes in intergenerational mobility and long-term development. The paper combines data on intergenerational educational mobility from three rounds of the Life in Transition Survey (2010, 2016, and 2022–23) (EBRD 2024), which covers more than 30 countries in Europe and Central Asia, and data from the Global Database on Intergenerational Mobility (GDIM, Van der Weide and others 2023). Data on mobility is complemented by data on present and past economic outcomes to form a panel of 68 countries over the period 2000-2020. This paper contributes to the literature on intergenerational mobility and development in two ways. Our primary contribution is that, unlike existing studies that focus on subnational districts or specific regions, we carry out a worldwide cross-country analysis of the relationship between intergenerational mobility and country income. This allows us to provide evidence of the nature of this relationship across different development contexts. The second contribution of our paper is to introduce a new measure of intergenerational mobility in education—the mobility gap—and compare its performance with several existing mobility measures. This paper presents the first empirical application of this new measure.

The patterns of intergenerational mobility across countries and generations vary significantly depending on the mobility measure used. In Europe and Central Asia, upward absolute mobility has been declining across birth cohorts, while relative mobility has not changed significantly, suggesting that an absolute reduction in intergenerational mobility in education may be common across the entire education distribution. South Asia has seen increases in absolute and relative mobility, while Latin America has experienced little change in absolute mobility but increases in relative mobility.

The empirical analysis of the association between intergenerational mobility and country income levels shows a significant context-specific relationship. Indicators of relative mobility in Europe and Central Asia are not correlated with country income levels over time. Only a specific dimension of absolute mobility—upward mobility in higher education (the probability that an individual whose parents did not achieve higher education does so)—shows a positive and statistically significant association with country income. In Latin America and the Caribbean, higher relative mobility is associated with lower income, while higher absolute mobility is associated with higher income. This finding suggests that some aspects of mobility may be more relevant for development in some contexts than others.

The following section reviews relevant studies of intergenerational educational mobility. Section 3 examines measures of mobility. Section 4 describes the study's empirical methodology. Section 5 describes the data. Section 6 presents the main patterns of intergenerational educational mobility. Section 7 presents the main results of the empirical analysis and associated robustness tests. Section 8 concludes.

## 2. Literature review

Multiple studies carried out a descriptive exploration of the patterns of intergenerational educational mobility. Hertz et al. (2007) use data from 42 countries between 1992 and 2005 to measure the persistence of educational attainment across generations by birth cohort. They find significant variation in the cross-country levels of intergenerational educational mobility, with high persistence of educational attainment in Latin America and much higher educational mobility in countries of Northern Europe. Chevalier, Denny, and McMahon (2009) study the patterns of intergenerational educational mobility in 20 developed countries, including the United States, Canada, New Zealand, and 17 European countries, and find that expanding access to higher education is not always associated with increased mobility. Causa and Johanson (2010) find a positive and significant correlation between parental human capital and their children's educational and wage outcomes in countries of the Organisation for Economic Co-operation and Development (OECD).

Financial constraints may hold back high-ability individuals from disadvantaged backgrounds. Razzu and Wambile (2022) study intergenerational educational mobility in 34 countries of Sub-Saharan Africa for cohorts born in the 1960s–1990s. They find that children’s educational outcomes depend strongly on their parents’ educational status but that the strength of this association is weaker for younger generations. The authors point to high heterogeneity in educational mobility across African countries. Van der Weide and others (2023) compile a global database of intergenerational educational mobility in 153 countries and demonstrate that such mobility is estimated to be lower in the average developing country than in the average high-income country.

Among the few papers that study the link between social mobility and economic development, Aydemir and Yazici (2019) discover that regions of Türkiye with better school availability, greater social capital, higher home resources, and lower educational inequalities tend to have higher intergenerational mobility. Güell and others (2018) find similar results in Italy, where provinces with higher levels of economic activity, lower inequality, and higher social capital and educational attainment have greater intergenerational social mobility. Lee and Lee (2022) analyze the persistence of intergenerational education attainments by age cohorts in 30 developed economies and find that higher per capita GDP positively correlates with social mobility. Neidhofer and others (2023) estimate the relationship between changes in educational intergenerational mobility and regional economic indicators in a sample of 52 regions in six countries in Latin America. They report that increasing social mobility correlates with rising income per capita, income growth, and other development indicators.

A few studies reach different conclusions. Clark and others (2014) conduct a multi-country historical analysis of social mobility based on surnames. They argue that economic development, progressive income redistribution, and development of public education matter less than other studies suggest, claiming that mobility varies little across societies and is, therefore, uncorrelated with economic outcomes.

## 3. Measures of educational mobility

We use four measures to capture trends in intergenerational educational mobility across countries and generations.

## Oriented mobility measures

The new approach to measuring intergenerational mobility proposed by Foster and Rothbaum (2023, unpublished) addresses the shortcomings of many measures of intergenerational mobility and proposes new axiomatically sound, practical, simple-to-implement, and easy-to-communicate measures. This paper offers the first empirical application of this method.

The two most common approaches to measuring intergenerational mobility are to estimate correlations between and the elasticity (as a regression coefficient) of children's education with respect to their parents' education (see, for example, Aydemir and Yazici (2019)). Despite their popularity, both methods have shortcomings.

First, they may fail to register dynamic changes in educational structure. For example, increases in educational attainment by children of better-educated parents and stagnation or decline in the attainment of children from less-educated households could lead to an increase, a decrease, or no change in intergenerational mobility measured by the elasticity (Corak 2013).

Second, the approaches produce misleading subgroup comparisons because they measure regression to the subgroup mean rather than the population mean. As a result, two age cohorts could have the same intergenerational mobility even if the later cohort had much higher mean educational attainment.

Third, the correlation and elasticity measures are not decomposable by group, making it challenging to use them for targeting (e.g., Blyth 1972). $^{2}$

Transition matrices are another popular class of intergenerational mobility measures (Shorrocks 1978). The transition matrices define groups (such as primary, secondary, and higher education) and estimate the probability of transitioning from one group to another. The transition matrixes capture the distribution of movements across groups; they can separate outcomes for children from, for instance, households with low and high levels of education.

Although they yield richer policy implications than the elasticity and correlation-based measures, transition matrices have their own problems. Among them are data censoring and arbitrary thresholds, when only movements across these thresholds “count” as mobility and thus are amplified in the analysis, while movements not observed due to censoring are not counted. $^{3}$ As a result, it might be challenging to separate the effects on intergenerational mobility of the underlying fundamental changes in the educational structure from the effects of censoring and the choice of cutoffs. Transition matrices also produce no headline measures, which is crucial for the ability of policy makers to communicate their intentions to the public and, thus, for successful policy implementation.

Distance-based mobility measures, often used to analyze income mobility (see Cowell 1985; Field and Ok 1996; Batana and Duclos 2010; Corak, Lindquist, and Mazumder 2014; Bárcena-Martín and Cantó 2024), are seldom used to analyze educational intergenerational mobility. Unlike transition matrixes, distance-based measures require no arbitrary thresholds, and they capture the churning or flux of educational attainments across groups well. These measures can also be used to generate policy-relevant headline metrics. Distance-based mobility measures ignore the direction of change or the “quality” of mobility, however, and are not helpful for policy targeting or identifying groups that benefited most from mobility or suffered the most from lack of it.

The new oriented distance-based approach to measuring intergenerational mobility aims to assess whether children have greater educational attainment than their parents and, if so, by how much. Foster and Rothbaum (2023) discuss the axiomatics and theoretical considerations for the class of oriented mobility measures $M(p)$ . We summarize the theoretical results relevant to our empirical analysis. $^{4}$

Define the set of upward movers such that

$$
Q ^ {U} = Q ^ {U} (\boldsymbol {p}) = \bigl \{i \colon s _ {i} ^ {p} <   s _ {i} ^ {c} \bigr \},   p _ {i} = \binom{s _ {i} ^ {p}}{s _ {i} ^ {c}}, i = 1, \ldots n\tag{1}
$$

and a set of downward movers such that:

$$
Q ^ {D} = Q ^ {D} (\pmb {p}) = \{i \colon s _ {i} ^ {p} > s _ {i} ^ {c} \},\tag{2}
$$

where p is a vector of parent–child dyads $p_{i}$ , $s_{i}^{p}$ is the parent's years of education, $s_{i}^{c}$ is the child's years of education, and n is the number of dyads. Once dyads are categorized according to equations (1) and (2), they can be aggregated to obtain oriented measures of intergenerational mobility. The most straightforward metric is the oriented headcount ratio:

$$
H ^ {o} = \frac {q ^ {o}}{n} f o r O = U, D,\tag{3}
$$

where $q^{o} = |Q^{o}|$ is the number of movers.

The oriented headcount ratio conveys meaningful information about mobility. Like the headcount ratios in poverty analysis, however, it is a crude way of assessing the extent of mobility. This shortcoming could be remedied by incorporating the average educational gap between a parent and a child by defining the oriented educational gap $I^{o}$ as follows:

$$
I ^ {o} = \frac {1}{q ^ {o}} \sum_ {i \in Q ^ {o}} \left| s _ {i} ^ {c} - s _ {i} ^ {p} \right| \mathrm{and} G ^ {o} = H ^ {o} I ^ {o} \mathrm{tobetheOrientedmobilitygap.} ^ {5}\tag{4}
$$

## Absolute mobility measures

The oriented mobility gap captures broad movements of the education distribution across generations. Alternative absolute mobility measures focus on the movement of certain parts of the education distribution. A measure proposed by Alesina and others (2021) estimates the probability of completing primary education by children whose parents did not. Neidhofer and others (2023) used a similar measure, the probability of upward mobility, focusing on completing secondary school. These measures may not have adequate empirical support in higher-income countries, where primary education completion is almost universal and secondary education is increasingly so, as Van der Weide and others (2023) point out. Because our sample represents mostly a mix of high- and middle-income countries, we redefine this measure, which we denoted as upward mobility in higher education (UMHE), as the probability of completing higher education by children whose parents did not:

$$
U M H E = P r o b (s _ {i} ^ {c} \geq t e r t i a r y \mid s _ {i} ^ {p} <   t e r t i a r y)\tag{5}
$$

## Relative mobility measures

One of the common measures of relative mobility is intergenerational persistence (IP) in education, defined as the additional years of schooling of a child associated with one more year of schooling of his or her parents. This measure is derived from a multivariate model that is specified as

$$
s _ {i} ^ {c} = \beta s _ {i} ^ {p} + \gamma C _ {i} + \varepsilon_ {i},\tag{6}
$$

where $s_i^c$ is years of education of the child $i$ , $s_i^p$ is years of education of the child's parents, and $\beta$ is the degree of IP. $\beta = 0$ represents a case of complete mobility; the educational attainment of children is unrelated to the education of their parents; $\beta = 1$ represents the case in which the education of the children mirrors the education of the parents (an extra year of education of the parents results in one more year of child schooling). A higher value of $\beta$ represents a lower degree of mobility. $C_i$ is a vector of individual characteristics of the child, the child's parents, and the characteristics of the household when the child was young. However, following Van der Weide and others (2023) and to ensure consistency with the estimates of this measure coming from the

GDIM, we do not include in our specification any control variable other than a dummy indicator for the survey in which the data were collected (to control for differences in the data collection process). $^{6}$

An additional measure of relative mobility is the intergenerational correlation (IC) in education—the correlation between $s_i^c$ and $s_i^p$ . IC is defined similarly to IP but in terms of the standard deviation of

[中间内容因长度限制已省略]

></tr><tr><td>Horizon 2</td><td>-0.210***</td><td>0.041</td><td>-0.143***</td><td>0.053</td><td>-0.006</td><td>0.005</td><td>0.294***</td><td>0.092</td></tr><tr><td>Horizon 3</td><td>-0.249***</td><td>0.045</td><td>-0.164***</td><td>0.059</td><td>-0.008</td><td>0.005</td><td>0.355***</td><td>0.103</td></tr><tr><td>Horizon 4</td><td>-0.274***</td><td>0.048</td><td>-0.176***</td><td>0.063</td><td>-0.009</td><td>0.006</td><td>0.387***</td><td>0.110</td></tr><tr><td>Horizon 5</td><td>-0.290***</td><td>0.049</td><td>-0.183***</td><td>0.064</td><td>-0.009</td><td>0.006</td><td>0.408***</td><td>0.112</td></tr><tr><td>Horizon 6</td><td>-0.302***</td><td>0.048</td><td>-0.183***</td><td>0.064</td><td>-0.008</td><td>0.006</td><td>0.432***</td><td>0.113</td></tr><tr><td>Horizon 7</td><td>-0.330***</td><td>0.049</td><td>-0.200***</td><td>0.065</td><td>-0.008</td><td>0.006</td><td>0.441***</td><td>0.115</td></tr><tr><td>Horizon 8</td><td>-0.390***</td><td>0.052</td><td>-0.271***</td><td>0.069</td><td>-0.011*</td><td>0.006</td><td>0.362***</td><td>0.123</td></tr><tr><td>Other developing Contemporaneous effect</td><td>-0.130***</td><td>0.036</td><td>-0.102**</td><td>0.048</td><td>-0.003</td><td>0.003</td><td>0.059</td><td>0.065</td></tr><tr><td>Horizon 1</td><td>-0.208***</td><td>0.046</td><td>-0.156**</td><td>0.061</td><td>-0.006</td><td>0.004</td><td>0.138*</td><td>0.083</td></tr><tr><td>Horizon 2</td><td>-0.289***</td><td>0.054</td><td>-0.208***</td><td>0.072</td><td>-0.010*</td><td>0.005</td><td>0.186*</td><td>0.097</td></tr><tr><td>Horizon 3</td><td>-0.353***</td><td>0.060</td><td>-0.250***</td><td>0.080</td><td>-0.013**</td><td>0.006</td><td>0.207*</td><td>0.108</td></tr><tr><td>Horizon 4</td><td>-0.396***</td><td>0.063</td><td>-0.278***</td><td>0.085</td><td>-0.016***</td><td>0.006</td><td>0.206*</td><td>0.115</td></tr><tr><td>Horizon 5</td><td>-0.415***</td><td>0.064</td><td>-0.286***</td><td>0.086</td><td>-0.016***</td><td>0.006</td><td>0.221*</td><td>0.118</td></tr><tr><td>Horizon 6</td><td>-0.426***</td><td>0.064</td><td>-0.282***</td><td>0.087</td><td>-0.015**</td><td>0.006</td><td>0.263**</td><td>0.119</td></tr><tr><td>Horizon 7</td><td>-0.453***</td><td>0.065</td><td>-0.297***</td><td>0.088</td><td>-0.014**</td><td>0.006</td><td>0.318***</td><td>0.121</td></tr><tr><td>Horizon 8</td><td>-0.501***</td><td>0.069</td><td>-0.367***</td><td>0.094</td><td>-0.016**</td><td>0.007</td><td>0.299**</td><td>0.129</td></tr></table>

Note: Standard errors are calculated with a small-sample degrees-of-freedom adjustment. \*\*\* significant at the 1% level, \*\* significant at the 5% level, \* significant at the 10% level.

## a. Intergenerational persistence

![](images/877b6d2094099e07538aa223e09c3493f2a385fb6ed15498dea08cdc5b3ee8a0.jpg)

![](images/5d0b60f4cdb238a396c52d309ed57d1c62ee056add38d877357a0d7e87c6d837.jpg)

![](images/ede97ae1d81dbbe2921beef1633ee13352ac3eddc4bcf41f57180f275f9044f8.jpg)

![](images/8ff5c7252bd43f5dd97acec15315e9970e1916512d0ff56e7b71b959c554f0fd.jpg)  
b. Intergenerational correlation

![](images/38dd27cdb63b6f1baafb2e2b7067ce7d936fca9a412fa8e710624f2e0f472eb8.jpg)

![](images/8371444bfefa9e10701c438347397c78aa27a62bb3a4f0774c3873acf3c8161d.jpg)

![](images/ecb12a97741975a970d77c2522f5dfe210606d791061fbe1c598809b117ab1ad.jpg)

![](images/92c6ecfe186b3685090316da7b35b41c2f439adadb03f077b2b90e0c1856c80d.jpg)  
c. Upward mobility gap

![](images/f418d455e7147f9f4e0f1192915f3689f7575f97b2173b6f90e3d144d98e1510.jpg)

![](images/ef2b1e24da45d63f73208eed05907ed89ed5ca6493c1ee74576bb55884d64711.jpg)

![](images/c2570953e97f5a7b8d79c015aaa0096366ab8d850ac44932d145709ee75276d7.jpg)

![](images/4788e8dc49d66b9b5949ebecdfaafb2c443c345e46f17737649f6c5f69302c1d.jpg)  
d. Upward mobility in higher education

![](images/fe5337462fc3166ebd14ff3e3a6c8a8e0c0602cce3b62da8dd6b55fff446a221.jpg)

![](images/f6777e275c076e9c5e89c258772383d2514ce954bef6a3889f611722d495fde5.jpg)

![](images/6bea2177d20432c826e9ed8f3384af3b212a9014b9edbaec6bf8fe4827f8fd88.jpg)

![](images/a44c391e7d8df519878782021c46daa428a11cd606b41a4b7c5ccd2f6fac47f6.jpg)  
Note: The figure plots the distribution of the estimated coefficients for each of the four regions resulting from the model uncertainty analysis proposed by Young and Holsteen (2017). The distribution is derived from the estimation of 255 possible specifications of equation (7), reflecting all combinations of control variables.

Figure A.2 Posterior density plots of estimated coefficients in the Bayesian Model Averaging Analysis

## a. Intergenerational persistence

![](images/f171244bae7394ef8653b63e7fc861ff27030eacdd84f055740090a5c6c912ed.jpg)

![](images/2f96ca61e12823c9f6089c7241a97e6a31498425b2c41d5df9810a8c0d02d1cc.jpg)

![](images/e6a8c02bbfd1c8ba8892022df6786d15937eccab8eb4dcabd01251a8c6e3895b.jpg)

![](images/af08ac5a01af8186e3bc135a78f79638e105600d3bb2bbf8d9ac5022c0991480.jpg)

## b. Intergenerational correlation

![](images/e26ea2055c9f60b92a861d67496a650559a4ba02a6bd6a614a711ca3f20f3ada.jpg)

![](images/ecfc080e7c7c15326e6b494ce318ccd1049bd50235cd56ae3e13cb34f7576a03.jpg)

![](images/3ca9edac1fb4fc5e00670d193ca60f72d8242d3b48ba41819699662fb9f347d9.jpg)

![](images/50ff48f9be2b4057e10581b41b0f33dbc89a46fb3a3820132645c79cd69404c9.jpg)

![](images/c1305f8388e0bc945bdd08a60741c087a71799fd3eb81051b143a5a079c4918c.jpg)

## c. Upward mobility gap

![](images/e27aa7c78b22c7c46333e0a649f4cf3773abda01089196dab4e5d707bb1729d0.jpg)

## d. Upward mobility in higher education

![](images/7d9e4862cff917286a5d1de94f68ff2f783f5546933d2ddfc807525e88c8dfee.jpg)  
Note: The figure plots the posterior densities in the Bayesian Model Averaging linear regression for each of the four mobility indices.
"""
