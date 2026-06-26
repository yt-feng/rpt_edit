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
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

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
# Rapid Economic Growth but Rising Poverty Segregation

# Will Viet Nam Meet the SDGs for Equitable Development?

Hai-Anh H. Dang

Shatakshee Dhongde

Minh Do

Cuong Viet Nguyen

Obert Pimhidzai

POLICY RESEARCH WORKING PAPER 11067

## Abstract

Viet Nam is widely regarded as a success story for its impressive economic growth and poverty reduction in the last few decades. Yet, recent evidence indicates that the country's economic growth has not been uniform. Compiling and analyzing new, extensive province-level data from the Vietnam Household Living Standards Surveys spanning 2002 to 2020 and other data sources, this paper finds within-province inequality to be much larger than between-province inequality. Furthermore, this inequality gap has been rising over time. Despite the country's fast poverty reduction, the poor were increasingly segregated in certain provinces, particularly those with a larger ethnic minority population. The analysis finds a beneficial impact of economic growth on poverty reduction, but this can depend on inequality levels. It also finds that greater inequality has had negative effects on economic growth but varying negative effects on different poverty indicators. The paper provides supportive evidence of the beneficial impact of economic transitions from agriculture to non-agriculture. The results suggest that policy makers in Viet Nam should focus on reducing spatial disparities and income inequality to attain sustainable economic development.

# Rapid Economic Growth but Rising Poverty Segregation: Will Viet Nam Meet the SDGs for Equitable Development?

Hai-Anh H. Dang, Shatakshee Dhongde, Minh Do, Cuong Viet Nguyen, and Obert Pimhidzai\*

JEL: C15, D31, I31, O10, O57

Keywords: poverty, inequality, pro-poor growth, convergence, household surveys, Viet Nam

## 1. Introduction

Poverty and inequality provide two closely related, but different, measures of household welfare. As rising global living standards have led to less poverty, increasingly more attention has been placed on whether the fruits of economic growth are equally distributed to different population groups in a society. The Sustainable Development Goals (SDGs) adopted by the United Nations (UN) offer a most notable example where the needs to reduce both poverty (SDG number 1) and inequality (SDG number 10) are emphasized by the international community. Indeed, a country with good economic growth but a (highly) unequal income distribution may neither be able to shrink its poor nor narrow the undesirable gaps between its population segments.

Viet Nam is widely regarded as a success story for its impressive economic growth and poverty reduction in the last few decades. Its growth has been found to be pro-poor since the early 1990s (Glewwe and Dang, 2011; Nguyen and Pham, 2018; Pimhidzai and Niu, 2021). Yet, recent evidence indicates that the country's economic growth was not uniform: while inequality gaps between urban and rural areas have been found to narrow over time, they have widened within urban and rural areas (Bui and Imai, 2019). Furthermore, poverty rates became concentrated spatially (Lanjouw, Marra, and Nguyen, 2017) and among ethnic minority groups (Benjamin, Brandt, and McCaig, 2017), suggesting that attention can be focused on these particular groups for more effective poverty amelioration.

In this paper, we aim to provide a long-term (and mostly descriptive) review of trends in poverty, inequality, and economic growth in Viet Nam. We contribute to the existing literature in several ways. First, we offer a broad but early assessment of the intertwined relationship between poverty, inequality, and economic growth for the country over the past 20 years. Recent review studies suggest that there is an intricate and complex relationship between these three development outcomes, which require further evidence for better understanding (Cerra et al., 2022; Ferreira et al., 2022). In fact, we offer the first study to investigate all three development outcomes of poverty, inequality, and economic growth for Viet Nam.

Specifically, we investigate several research questions that are highly relevant to policy. Have average incomes across provinces converged (or diverged) over time? If yes, how were the poor segregated? Why were the poor spatially concentrated in some provinces and not others? Did factors such as inequality, urbanization, investment, and volume of government spending play a role in determining poverty reduction? Furthermore, what could we tell about the relationship between economic growth, inequality, and (different measures of) poverty?

Second, our analysis spans the period 2002-2020, which represents the longest-running period for the country that has been examined in an academic study. We complete this task by analyzing 10 rounds of the nationally representative Vietnam Household Living Standards Surveys (VHLSS). Our findings on the trends of poverty, inequality and economic growth, which are further disaggregated into between-province and within-province and regional variations, offer a nuanced picture of the evolution of these outcomes over time. To our knowledge, these findings are new and not available in previous studies. $^{1}$

Finally, we construct a database of panel data at the province level, which allows us to offer more granular analysis than the urban-rural dichotomy analyzed in previous studies. We further supplement this database with data on government spending that we collect from the central government and different provincial government websites. As a result, we can zoom in on provinces that are good (or bad) performers. Furthermore, this rich panel database also allows us to employ rigorous econometric modeling techniques to investigate the channels affecting the province-level income distributions.

Our estimation results suggest that within-province inequality has steadily increased over time. Within-province inequality is also much larger than between-province inequality, with the former type of inequality being almost three times the latter type of inequality in 2020. Average incomes and expenditures appear to converge across provinces, while poverty significantly declines during this period. The remaining poor seem to be regionally segregated among provinces with a greater share of ethnic minority population. We find beneficial impact of economic growth on poverty reduction. While the relationship of inequality with headcount poverty appears weak and not statistically significant, inequality is positively and strongly statistically correlated with poverty gap and poverty severity and might impede economic growth. Provinces with greater population density and a larger share of urban population have faster growth, whereas the opposite result holds for those with a greater share of ethnic minority groups. The transitions from an agriculture-based economy toward wage-based and services-based economy could be beneficial for the country's economic growth and poverty reduction.

This paper consists of four sections. In the next section, we describe the data (Section 2.1), discuss the overall trends in economic growth, inequality, and poverty at the country level (Section 2.2) and at the regional level as well as analyze poverty segregation across provinces (Section 2.3). We subsequently investigate in Section 3 the relationship between economic growth, inequality, and poverty, including convergence in inequality. We finally conclude in Section 4.

## 2. Trends in economic growth, inequality, and poverty

## 2.1. Data

We compile data from the Vietnam Household Living Standards Surveys (VHLSSs), which has been widely employed by the government, the international community, and academic researchers for poverty and inequality analysis for the country. The VHLSSs have been conducted by the General Statistics Office of Vietnam with technical support from the World Bank every two years since 2002. We compile data on all 58 provinces and five centrally controlled municipalities and supplement this data with other data that we collected. $^{2}$ In particular, provincial government spending data for the period 2018-2020 is currently unavailable for all the 63 provinces in any official document. To get the most updated data, we manually collected the state spending and investment spending data for 2018-2020 from several sources including the Ministry of Finance's website, provincial finance departments' websites, and relevant official documents.

The VHLSSs contain detailed data on individuals and households. Household-level data are collected on durables, assets, production, income, and participation in government programs. Individual-level data are collected on demographics, education, employment, health, and migration. The 1999 Population and Housing Census was used as the sampling frame of the VHLSSs during 2002-2008, while the 2009 and 2019 Population and Housing Censuses were used as the sampling frame of the VHLSSs respectively for 2010-2016 and 2018-2020. Around 3,100 communes were chosen as the primary sampling units out of the list of 10,000 communes for the whole country. A village was randomly selected from each commune, and about 15 households were selected randomly from the village.

The large-sample VHLSSs have a sample size of about 46,000 households that are designed to be representative at the provincial level. While these large-sample surveys only collect income data, a sub-sample of the VHLSSs (the small-sample VHLSSs of around 9,000 households) collect data on both income and expenditure. Since policy discourse in the country is typically based on poverty and inequality analysis using expenditure data, we mostly analyze such data in this paper. We obtain the province-level expenditure using Elbers et al.'s (2003) small area (poverty-map) estimation method (see Appendix B for more detailed description for the data). For robustness checks, we also provide some alternate estimates using per capita income in Appendix A, which offer qualitatively similar results.

## 2.2. Overall trends in economic growth, inequality, and poverty

We provide in Table 1 the country trends in (real) per capita income, expenditure, poverty, and inequality. Between 2002 and 2020, per capita incomes increased significantly from 4,565 thousand (Vietnamese) dong to 15,156 thousand dong. $^{3}$ Similarly, real per capita expenditure more than tripled from 3,476 thousand dong in 2002 to 14,251 thousand dong in 2020. $^{4}$ This rapid economic growth has been widely attributed to important policy changes that took place in Viet Nam in the last two decades (see, e.g., Justino and Litchfield, 2014, Benjamin et al., 2017 for a review). Specifically, the “Doi Moi” (renovation) policies introduced in 1986 helped transform Viet Nam from a centrally planned economy to an open, export-oriented economy with high volume of trade and foreign direct investment. In 2001, the United States and Viet Nam signed a Bilateral Trade Agreement, in which the United States granted Viet Nam the status of the Most Favored Nations. As a result, tariffs on Vietnamese exports to the U.S. reduced significantly, triggering export-led economic growth.

Figure 1 plots the distribution of log of per capita expenditure over time. Between 2004 and 2020, the distribution shifted significantly to the right, indicating a rise in average per capita expenditures. $^{5}$ However there is not a marked decrease in the variance of the distribution, indicating that inequality did not change rapidly during this period. We estimate three different measures of inequality, namely the Gini index and the Theil L and T indices and show the results in Table 1. All the three measures show steady levels of inequality in per capita expenditure. The average value of the Gini index was 0.37 and close to the lower side of the typical range of 0.3-0.5 for Gini values for per capita expenditures in developing countries (World Bank, 2005).

The Gini index is derived from the Lorenz curve and cannot be written as the sum of a term summarizing within-group inequality and a term summarizing between-group inequality (Bourguignon, 1979). Unlike the Gini index, the Theil index is a generalized entropy (GE) measure, and it can be decomposed into within and between components. Table 2 shows the decomposition of the Theil L index (GE 0; also known as the mean log deviation) and the Theil T index (GE 1). We find that within-province inequality increased over time. Within-province inequality explained about $66\%$ of total inequality in 2002, but more than $70\%$ in 2020. This translates into within-province inequality increasing from about twice higher than between-province inequality in the early 2000s, to about three times higher than between-province inequality in the late 2010s. Thus, within-province inequality has become much more significant over time than between-province inequality. $^{6}$

There were significant differences in inequality levels within the provinces (Appendix A, Table A.1). Compared with the national average of 0.37, the Gini index was greater than 0.40 in Lao Cai, Dien Bien, and Lai Chau in the northern mountain region. In 2020, these provinces still had some of the remarkably high poverty rates (Lao Cai: 21.5%, Dien Bien 46% and Lai Chau: 36%). Inequality and poverty levels were similarly high in the central highlands region (e.g., Kom Tum and Gia Lai had Gini values of 0.41 and 0.39 and poverty rates of 17% and 27% respectively). On the other hand, inequality was lower in Mekong River delta with a Gini index of about 0.31 in Long An and Tien Giang (where poverty rates hover around 1%) and 0.28 in Hung Yen and Thai Binh in the Red river delta (where poverty rates range around 1%).

Finally, we also show in Table 1 the estimates of three Foster-Greer-Thorbecke (FGT) indices of poverty (Foster et al., 1984). The poverty rate (i.e., the headcount ratio) measures the incidence or the proportion of the poor in the population, the poverty gap measures the depth of poverty (i.e., the average income shortfall of the poor), whereas the poverty severity index (i.e., the squared poverty gap) takes into account inequality of the income distribution among the poor. All three measures are estimated using the national (expenditure-based) poverty line as well as the World Bank’s PPP \$3.1 per day poverty line. In tandem with the rapid economic growth, we find that poverty rates declined significantly. Nationwide, the headcount poverty rate decreased from 29% in 2002 to less than 10% and 5% in 2016 and 2020, respectively. Notably, the first goal of the United Nations’ Millennium Development Goals was to reduce extreme poverty rates by half between 1990 and 2015 but Viet Nam appears to have well exceeded the target. $^{7}$ More summary statistics are provided in Appendix A, Table A.2.

## 2.3. Regional distribution of poverty

The country-level trends in economic growth, poverty and inequality do not reflect the regional variation in these indicators. In Table A.1 in the Appendix, we present the estimates for each of these indicators in 2020, for all 63 provinces. In the last two decades, although overall poverty declined rapidly in Viet Nam, poverty rates varied significantly across provinces. Poverty rates were lowest in Ho Chi Minh City (1.8% average over time) and neighboring Binh Duong province (3.2% average). Ho Chi Minh City is the largest city and the prime economic center in Viet Nam. The city has numerous export processing zones, industrial parks, colleges, and universities, as well as the largest international airport in the country. After Ho Chi Minh City, Binh Duong is the second highest recipient of foreign direct investment. Both Ho Chi Minh City and Binh Duong province are in the southeast region. Poverty was also lower in the Red River Delta, for instance in the capital city of Hanoi (5.4% average) and the port city of Hai Phong (5% average). $^{8}$ On the other hand, poverty rates were very high in northwest provinces of Son La (50% average), Dien Bien (62% average), Lai Chau (60% average) and Ha Giang (56% average) in the northeast. These provinces lie in the inland, mountainous regions, bordering China and the Lao People's Democratic Republic and have more than $80\%$ of their population residing in rural areas. Furthermore, more than $70\%$ of their population consists of ethnic minorities.

Given the large variance in poverty levels across provinces, there is evidence suggesting that poverty has become spatially concentrated over time (Lanjouw et al., 2017). We measure disparity in the regional distribution of poverty by estimating a poverty segregation curve (Dhongde, 2017). $^{9}$ The poverty segregation curve is a useful graphical tool to analyze how the regional distribution of the poor changed over time. The curve compares a province's share of the poor population with its share of the overall population. The poor are segregated when provinces' share of the poor does not resemble their share in the overall population. Perfect integration (zero segregation) implies that each province has the same share in the poor and the overall population (poor and non-poor combined). Figure 2 plots the poverty segregation curve for 2002 and 2020. The diagonal line of equality shows that there is zero segregation of the poor. The 2002 curve lies above the 2020 curve and hence dominates the 2020 curve. In other words, there was unambiguous increase in the segregation of the poor in Viet Nam.

Poverty segregation curves may often intersect or overlap, and thus fail to provide a complete rank ordering of inequality. In Table 3, we calculate two indices of segregation, namely the Dissimilarity index and the Gini index. The Dissimilarity index is equal to one-half the sum of the absolute difference between the proportion of the poor and the proportion of the population across provinces. The Gini index is equal to twice the area between the segregation curve and the diagonal of equality. $^{10}$ Between 2002 and 2010, there was not a marked increase in segregation. However, since 2012, there was a steady rise in the spatial inequality in the distribution of the poor. Provinces with a cumulative share of about 50% of the total population had about 30% of the poor population in 2002, whereas only about 3% of the poor population in 2020. Over the years, poor provinces such as Dien Bien and Lai Chau saw their share of the poor population increase disproportionately. Despite a rapid decline in average poverty levels, we find that the remaining poor were increasingly segregated in certain provinces in the cou

[中间内容因长度限制已省略]

.042***</td></tr><tr><td></td><td>(0.010)</td><td>(0.009)</td><td>(0.112)</td><td>(0.012)</td><td>(0.011)</td><td>(0.010)</td><td>(0.012)</td><td>(0.009)</td></tr><tr><td>Lagged share of urban population</td><td>0.002***(0.001)</td><td>0.002***(0.001)</td><td>0.002***(0.001)</td><td>0.034***(0.009)</td><td>0.002***(0.001)</td><td>0.002***(0.001)</td><td>0.003***(0.001)</td><td>0.002***(0.001)</td></tr><tr><td>Lagged share of population with high-school diploma</td><td>0.111(0.192)</td><td>0.100(0.176)</td><td>0.105(0.188)</td><td>0.067(0.177)</td><td>3.171(3.373)</td><td>0.108(0.205)</td><td>0.071(0.166)</td><td>0.152(0.213)</td></tr><tr><td>Lagged share of ethnic minority population</td><td>-0.001**(0.000)</td><td>-0.000(0.000)</td><td>-0.001*(0.000)</td><td>-0.000(0.000)</td><td>-0.001**(0.000)</td><td>0.000(0.004)</td><td>-0.000(0.000)</td><td>-0.000(0.000)</td></tr><tr><td>Lagged Gini index</td><td>-0.409**(0.188)</td><td>-0.390**(0.171)</td><td>-0.419**(0.201)</td><td>-0.574***(0.122)</td><td>-0.460**(0.183)</td><td>-0.432**(0.202)</td><td>-0.192(0.208)</td><td>-0.421**(0.208)</td></tr><tr><td>Lagged poverty rate</td><td>-0.074(0.096)</td><td>-0.056(0.121)</td><td>-0.047(0.106)</td><td>0.091(0.083)</td><td>-0.032(0.115)</td><td>-0.117(0.111)</td><td>-0.098(0.091)</td><td>0.148(0.149)</td></tr><tr><td>Lagged share of wage income</td><td>0.091(0.108)</td><td>0.116(0.100)</td><td>0.095(0.105)</td><td>0.034(0.110)</td><td>0.079(0.106)</td><td>0.088(0.108)</td><td>0.209**(0.099)</td><td>0.037(0.099)</td></tr><tr><td>Lagged share of non-farm income</td><td>-0.223*(0.122)</td><td>-0.221(0.139)</td><td>-0.258**(0.131)</td><td>-0.260**(0.131)</td><td>-0.202(0.147)</td><td>-0.227*(0.137)</td><td>-0.224(0.142)</td><td>-0.254**(0.129)</td></tr><tr><td>Constant</td><td>3.750***(0.904)</td><td>1.794(2.396)</td><td>3.011***(0.536)</td><td>2.487***(0.434)</td><td>3.224***(0.784)</td><td>3.544***(0.578)</td><td>3.529***(0.551)</td><td>3.273***(0.456)</td></tr><tr><td>Year FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Province FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>567</td><td>567</td><td>567</td><td>567</td><td>567</td><td>567</td><td>567</td><td>567</td></tr><tr><td>R2/ Chi2</td><td>3446</td><td>3460</td><td>3666</td><td>3055</td><td>3255</td><td>3335</td><td>3043</td><td>2985</td></tr><tr><td>Number of provinces</td><td>63</td><td>63</td><td>63</td><td>63</td><td>63</td><td>63</td><td>63</td><td>63</td></tr><tr><td>Arellano-Bond test for AR(1)</td><td>-4.913</td><td>-4.915</td><td>-4.998</td><td>-5.048</td><td>-5.176</td><td>-5.363</td><td>-4.898</td><td>-5.006</td></tr><tr><td>Arellano-Bond test for AR(2)</td><td>1.172</td><td>1.243</td><td>1.234</td><td>1.131</td><td>1.193</td><td>1.031</td><td>1.402</td><td>1.503</td></tr><tr><td>Sargan test</td><td>173.5</td><td>175.8</td><td>195.9</td><td>151.5</td><td>161.6</td><td>147.5</td><td>174.1</td><td>194.9</td></tr></table>

Note: i) Authors' estimation from VHLSSs using province GMM models, ii) Robust standard errors in parentheses clustered at the province level, iii)\*\*\* p<0.01, \*\* p<0.05, \* p<0.1.

Figure A.1: Growth of per capita expenditure and initial expenditure level  
Panel A. Two-year growth of per capita expenditure  
![](images/7d3481883683e164319a7980df66c8dc41e91652e3f759e6b2b34650a717fae0.jpg)  
Panel C. Ten-year growth of per capita expenditure

Panel B. Four-year growth of per capita expenditure  
![](images/e460c2aecfdc478e2336ed5b4556d488010ebe227eef87635401d1b77bacf926.jpg)  
Panel D. 18-year growth of per capita expenditure

![](images/c18dfaee6467466ca2bee26bd30f8f19950f4871c7f8f30ff9627903bd0f0baa.jpg)

![](images/1bca2c1dc85ac359993fe810e846c83c658e118032726b70aa96a23e0a404f73.jpg)  
Note: i) Authors' estimation using VHLSSs data

## Appendix B: Further data description

The Vietnam Household Living Standard Surveys (VHLSS) are conducted biennially, covering approximately 45,000 households in each survey round. The VHLSSs are designed to be representative at the provincial level (63 provinces). Within the VHLSSs, a sub-sample of around 9,000 households is selected to collect expenditure data. However, this smaller sample is only representative at the regional level (6 regions). To obtain estimates that are representative at the provincial level, the full sample of 45,000 households should be utilized. Thus, we estimate per capita expenditure of households in the sample of 36,000 households using the “poverty mapping” imputation method (Elbers et al., 2003). Estimating per capita expenditure consists of two steps. First, we estimate an expenditure model using the small-sample VHLSs (9,000 households). The dependent variable is the per capita expenditure, and the explanatory variables consist of household characteristics including demographics, ethnicity, education of household heads and household members, durables, housing conditions, and region dummies. We estimate separate models for urban and rural areas. The variables are selected using stepwise regressions. Only variables that are statistically significant at the 1% level and demonstrate reasonable signs are used in the final models. Second, we apply this expenditure model to the sample of 36,000 households (using the same variables that were employed in the expenditure model based on the small-sample VHLSSs) and predict per capita expenditure for these households. As a result, we have per capita expenditure data for the full sample of 45,000 households, and we use this data to estimate the per capita expenditure of provinces.
"""
