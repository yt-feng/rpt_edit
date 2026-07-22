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
- 已识别机构名：`波士顿咨询`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份波士顿咨询研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# MEASURE WELL-BEING TO IMPROVE IT

THE 2019 SUSTAINABLE ECONOMIC DEVELOPMENT ASSESSMENT

![](images/2ad19cc9f926b4bbb00509f6de5f1ed15d5722b34fef125fbc6d7d1233a534ea.jpg)

BCG

Boston Consulting Group partners with leaders in business and society to tackle their most important challenges and capture their greatest opportunities. BCG was the pioneer in business strategy when it was founded in 1963. Today, we help clients with total transformation—inspiring complex change, enabling organizations to grow, building competitive advantage, and driving bottom-line impact.

To succeed, organizations must blend digital and human capabilities. Our diverse, global teams bring deep industry and functional expertise and a range of perspectives to spark change. BCG delivers solutions through leading-edge management consulting along with technology and design, corporate and digital ventures—and business purpose. We work in a uniquely collaborative model across the firm and throughout all levels of the client organization, generating results that allow our clients to thrive.

![](images/e1f04473e9069aa5a02107eebcb65c6e70e49afe3278eeec2af6319922481b15.jpg)

# MEASURE WELL-BEING TO IMPROVE IT

THE 2019 SUSTAINABLE ECONOMIC DEVELOPMENT ASSESSMENT

JOAO HROTKO

ENRIQUE RUEDA-SABATER

NIKOLAUS LANG

VINCENT CHIN

## CONTENTS

3 ACHIEVING PROGRESS THROUGH WELL-BEING

6 DRIVING ACTION

Designing a Government Dashboard

Identifying Best Practices

16 INSIGHTS FROM 2019 SEDA RESULTS

Change in SEDA Scores

Converting Wealth into Well-Being

21 FROM INSIGHT TO ACTION

22 APPENDIX

35 FOR FURTHER READING

36 NOTE TO THE READER

# ACHIEVING PROGRESS THROUGH WELL-BEING

MULTIPLE DISRUPTIVE FORCES—THE rapid pace of technological change and its potential contribution to inequality chief among them—pose critical challenges to governments around the world. It is more important than ever for governments to develop and implement strategies that take that disruption into account and aim to improve the lives of citizens.

Boston Consulting Group's Sustainable Economic Development Assessment (SEDA) can be a powerful tool in this effort. BCG created SEDA in 2012 to track the relative well-being of a country's citizens and to provide insight into how well a country converts its wealth into well-being. (See the sidebar “A Yardstick for Well-Being.”) The development of SEDA was a response to the growing consensus that gross domestic product (GDP) is a limited metric for assessing a country's performance; the tool built on the work of prominent economists and international organizations to broaden the lens beyond economic indicators.

SEDA provides valuable insight, but it can also help governments move from insight to action in two critical ways:

\- First, SEDA is not only a powerful metric on its own but also can be a key component of a high-level dashboard. We believe governments should develop a perfor-

mance dashboard that offers a three-pronged view comprising GDP, the objective measure of well-being offered by SEDA, and subjective measures of well-being available through happiness metrics. This sort of dashboard can provide timely and multifaceted information about how governments are faring in terms of sustainable development—and flag the need for course corrections.

\- Second, SEDA can be used to identify countries that outperform relative to peers or the rest of the world in certain dimensions, thus revealing best practices and lessons that can guide policies and programs in other countries.

In addition to discussing these important uses of SEDA, this report presents the SEDA results for the 143 countries in our 2019 data set. With 12 years of data, we can see how some countries, including China, Rwanda, and Vietnam, have enjoyed a meaningful improvement in relative well-being, while others, such as Greece, Egypt, and Mozambique, have lost ground. (For a full view of SEDA results, see the Appendix and the SEDA interactive.)

Understanding the progress countries make over time, both overall and at the level of specific dimensions, is critical to setting more-effective national priorities and strategies.

## A YARDSTICK FOR WELL-BEING

SEDA's design was inspired by the work of economists, such as Nobel Laureates Amartya Sen, Michael Spence, and Joseph Stiglitz, who argue that in order to provide a strong incentive for placing well-being at the center of policies and public investment priorities, we need a way to measure and—importantly—track progress over time in well-being. Our efforts have been further reinforced by the November 2018 OECD reports on the measurement of economic performance and social progress, which provided guidance on measuring people's well-being and societies' progress.

SEDA combines objective, factual data on outcomes, such as in health and education, with quasi-objective data, such as governance assessments. It is a relative measure, assessing how countries perform relative to the rest of the world or to individual peers or groups of countries.

SEDA defines well-being on the basis of ten dimensions that fall into three categories. (See the exhibit.)

• Economics looks at income levels, stability, and employment.

\- Investments focus on the key public investment areas of education, health, and infrastructure.

\- Sustainability considers social aspects (equality, governance, and civil society) and the environment.

Using indicators from publicly available sources, we assess country performance for each dimension. The assessment relies on a total of 40 indicators based on the most recently available data. (For our 2019 analysis, this is generally 2017 data—it is worth noting that very recent develop-

SEDA Assesses Relative Well-Being Across Ten Dimensions  
![](images/9b0a3d04212dd02d4e164003dea369dc294e99c5184bfcef8a41621ec2ce39b1.jpg)  
Source: BCG analysis.

ments will not be reflected in the analysis.) Each indicator's measure is normalized on a scale of 0 (the lowest score) to 100 (the highest). Based on those normalized indicators, a score is calculated for each of the ten dimensions. We can use these scores to look at well-being in three ways:

\- SEDA Score. We aggregate the scores for the ten SEDA dimensions to provide an overall score for each country. This score can be used to compare a country with any other country or group of countries. In general, wealthier countries tend to have higher scores than less wealthy countries. The ten dimensions are not only the building blocks for SEDA scores but also provide insight on a country’s strengths and weaknesses. Dimension scores (on a 0-100 scale) can be used to benchmark individual countries against the rest of the world or against relevant peer countries—individually or in groups.

\- Change in SEDA Score. With 12 years of data, we are able to track not only the change in SEDA score from 2008 to 2019 (based generally on data from 2006 through 2017), but also changes in each dimension of the SEDA score.

\- Wealth-to-Well-Being Coefficient. On the basis of SEDA scores, we can examine how effectively countries are able to convert their wealth (as reflected in income per capita) into well-being. We do this by using a measure called the wealth-to-well-being coefficient. This coefficient compares a country's SEDA score with the score that would be expected given the country's GNI (gross national income) per capita. The coefficient thus provides a relative indicator of how well a country has converted its wealth into the well-being of its population. Countries with a coefficient of 1.0 are generating well-being in line with what would be

expected given their income levels. Countries that have a coefficient greater than 1.0 deliver higher levels of well-being than would be expected given their GNI levels, while those below 1.0 deliver lower levels of well-being than would be expected.

The current SEDA database covers 143 countries, which represent $97\%$ of the world's population and $98\%$ of the global economy. While the analyses and charts cover all 143 countries, we place special focus (through chart labels and specific text references) on what we call the global powerhouses. These are countries that constitute the 25 largest economies and the 25 most populous countries. Because 15 countries fall in both categories, the result is a list of 36 global powerhouses. (See the Appendix exhibit for details on this group of countries.)

# DRIVING ACTION

T IS ONE THING to understand where a country's challenges lie—it is another to address them. To this end, governments should take a comprehensive view of performance, one that looks at metrics such as well-being and happiness, and they should identify countries that can serve as role models in key areas.

## Designing a Government Dashboard

Many successful companies are shifting their focus from products to the experiences of end users. Governments need to make a similar change—moving from a heavy reliance on GDP as a barometer of national performance to a broader view that captures the full experience of citizens. There is evidence that such a shift is under way. The most recent move: the announcement by the New Zealand government of its “well-being budget.” Under this process, the setting of all budget priorities will be informed by economic issues but will be driven primarily by the well-being of the population, including in areas such as mental health and the transition to a sustainable and low-emissions economy.

A national performance dashboard can help support governments in taking this more holistic view. Such dashboards can be an integral part of strategy implementation and an important source of signals to confirm strategic direction or to flag the need for change.

A high-level performance dashboard should capture economic performance, objective well-being, and subjective well-being—three lenses that offer distinct, complementary perspectives on national progress.

## A performance dashboard can help governments take a more holistic view of progress.

\- Subjective Well-Being Lens. The UN-sponsored World Happiness Report provides country averages on individuals' perceptions of their experiences related to well-being.

Each lens offers considerable potential for segmentation, which enables deep dives in areas of interest. But there is merit in using all three at a high level to create a cohesive and comprehensive view of national performance that can capture the attention of policymakers and the public.

To see how these measures complement one another, it helps to look at how their divergence can illuminate challenges and areas that require additional attention.

The Relationship Between Income and Objective Well-Being Measures. It is no surprise that there is a positive relationship between wealth, as reflected in per-capita income levels, and SEDA scores. After all, income affects well-being in many ways. But it is clear that well-being is not simply a function of income. After all, we see many countries at similar income levels that have quite different well-being levels. (See Exhibit 1.) Poland and Argentina, for example, have similar income levels, but Poland's well-being score is much higher.

We also see countries with higher income levels that lag behind in well-being compared with lower-income countries. The US, for example, has a higher per-capita income than the Netherlands but a significantly lower SEDA score. South Africa has a higher income level than Indonesia but a much lower well-being score.

This underscores that there are factors beyond economics that affect well-being—factors that manifest themselves in the varying levels of performance in converting wealth into well-being.

The Relationship Between Objective and Subjective Well-Being Measures. Contrary to what one might expect, subjective measures like scores from the World Happiness Report and objective SEDA measures are not always aligned. Countries can have relatively high well-being scores, for example, but relatively low happiness levels. In fact, a regression

EXHIBIT 1 | Countries at Similar Income Levels Have Different Well-Being Scores  
![](images/ed305c421fb1f5b4bf32d56f9b79ecda9c0f5ff284af6977d1dedca799c26d92.jpg)

Sources: World Development Indicators, World Bank; 2019 SEDA (scores mostly reflect 2017 data).
Note: The named countries are the 36 global powerhouses, derived from the 25 countries in our data set with the largest populations, accounting for 78% of the world population, and the 25 with the largest economies, accounting for 87% of global GDP; some countries are in both categories. Income per capita is based on GNI (Atlas method) and is limited to 65,000 for graphical reasons.

analysis shows that countries with higher well-being scores are more likely to have lower-than-expected happiness levels than countries with low well-being scores.

In some cases, the discrepancy between well-being and happiness seems to follow a regional pattern—while in other cases the differences are country specific.

While a number of factors may account for the divergence, our work highlights one possible significant driver: social inequality. Individuals in countries with relatively high levels of social inequality tend to report low levels of happiness. (See the sidebar “The Impact of Social Inequality.”)

## A difference between well-being and happiness measures can be a warning sign.

The dashboard we envision would use the wealth-to-well-being coefficient as the measure of objective well-being in order to strip out the effect of income on well-being levels. When we look at the relationship between the wealth-to-well-being coefficient and happiness, there is no significant evidence of correlation. (See Exhibit 2.) For instance, Switzerland, with a wealth-to-well-being coefficient well above par, also does well in terms of happiness, while Vietnam—with an even higher coefficient—does not.

What does this mean for governments trying to set national strategy? The divergence between the wealth-to-well-being coefficient and happiness can be a warning sign, indicating that even for countries that excel at harnessing their resources to deliver well-being for citizens, there remain factors that contribute to dissatisfaction. This divergence can be a result of government's inability to communicate a consistent narrative of progress that inspires citizens. Or it can reveal a more fundamental disconnect between the priorities of government and of citizens. It may also reflect the fact that citizens' happiness depends on dimensions that go beyond national

boundaries, such as regional and global insecurity or climate change, and include citizens' perspectives on those issues and others that have an impact on the future.

The Three-Pronged View. We can see the value of the three-pronged view by using it to assess the global powerhouse countries. We segmented those countries into two groups: those that grew faster from 2006 through 2017 than countries with a similar income level in 2007 and those that that grew more slowly. For each group, we then sorted countries on the basis of the positive or negative changes in their objective (wealth-to-well-being coefficient) and subjective (happiness score) well-being measures. (See Exhibit 3.)

We found that 23 countries had faster economic growth than the group with a similar income level—but only 5 of them saw improvements in both the wealth-to-well-being coefficient and the happiness score. Another 4 backtracked in terms of both objective and subjective well-being measures. Most countries—including the majority of those that grew faster than economic peers and the 13 that grew more slowly—had a negative signal from either the objective or the subjective measure. $^{1}$

Digging into these results highlights that economic and well-being measures are often unaligned. Among countries that were growing quickly, nearly as many were doing poorly in both the objective and subjective measures of well-being as were doing well in both—with most somewhere in the middle.

The US falls into the first camp, with declines in the wealth-to-well-being coefficient, which slipped from 0.92 in 2008 to 0.90 in 2019, and the happiness score, which fell from 7.32 to 6.89. $^{2}$ The decline in both measures appears to be connected, in part, to challenges related to health. The World Happiness Report 2019 links the decline in the happiness score to weak policy responses to health and addiction issues. And for a wealthy country, the US has relatively weak performance in the SEDA health dimension, in part because of high obesity rates and declining life expectancy.

# THE IMPACT OF SOCIAL INEQUALITY

There is much concern and debate about income inequality—rightfully so. But social inequality—which we assess by looking at inequality in health outcomes and access to education—gets less attention. The problem: our research finds that social inequality is a more significant success factor for well-being than income inequality.

Income inequality has increased in most countries as higher-income segments of the population benefit disproportionately from economic growth. Our previous work has shown, not surprisingly, that income inequality is negatively correlated with well-being. In addition, income inequality is significantly correlated with the gap between subjective measures (happiness) and objective measures (SEDA). In other words, countries with higher levels of income inequality tend to have lower levels of happiness than one would expect given their overall level of well-being.

But income inequality hardly tells the full story. Just as we have argued that GDP alone does not fully reflect country performance, we also believe income equality alone does not adequately capture overall inequality in a society. As a result, starting in 2018 we expanded SEDA's equality measure by adding a social equality measure to our income inequality measure (which is based on Gini coefficients).\* The social equality measure is based on a simple average of health and education inequality measures.

Looking at country positions on income and social inequality measures, we find significant differences:

Among our global powerhouse countries, for instance, some, such as the Netherlands and Sweden, have comparably low levels of both social and income inequality. At the other end of the spectrum are countries like Nigeria and the Democratic Republic of the Congo, which have very high inequality in both areas.

In between, we find countries with high income inequality and lower social inequality, such as China, Argentina, and the US; and countries with high levels of income inequality and eve

[中间内容因长度限制已省略]

0.81</td><td>0.79</td><td>0.79</td></tr><tr><td>Vietnam</td><td>1.16</td><td>1.18</td><td>1.21</td><td>1.19</td><td>1.19</td><td>1.34</td><td>1.32</td><td>1.34</td><td>1.33</td><td>1.32</td><td>1.34</td><td>1.35</td></tr><tr><td>Yemen</td><td>0.75</td><td>0.71</td><td>0.71</td><td>0.67</td><td>0.64</td><td>0.63</td><td>0.63</td><td>0.60</td><td>0.56</td><td>0.57</td><td>0.51</td><td>0.48</td></tr><tr><td>Zambia</td><td>0.81</td><td>0.83</td><td>0.79</td><td>0.79</td><td>0.80</td><td>0.82</td><td>0.82</td><td>0.81</td><td>0.83</td><td>0.83</td><td>0.86</td><td>0.82</td></tr><tr><td>Zimbabwe</td><td>0.69</td><td>0.66</td><td>0.69</td><td>0.70</td><td>0.69</td><td>0.72</td><td>0.73</td><td>0.74</td><td>0.75</td><td>0.77</td><td>0.76</td><td>0.77</td></tr></table>

The Global Powerhouses

25 LARGEST ECONOMIES (GDP, \$TRILLIONS)

![](images/4f407e4a7d4fcf1a05167278c7f9cc1c1854f5804de535fdc849394b69abf8aa.jpg)  
Source: World Bank 2017.  
25 MOST POPULOUS COUNTRIES (MILLIONS)

![](images/fa98d43ea153fe99ba242f37075c877a8c4061d8aa5fe36851a9f8eede30562c.jpg)  
Because some countries fall into both categories, there are a total of 36 global powerhouses

# FOR FURTHER READING

Boston Consulting Group has published reports on related subjects that may be of interest to senior executives. Examples include those listed here.

Striking a Balance Between Well-Being and Growth: The 2019 Sustainable Economic Development Assessment
A report by Boston Consulting Group, July 2018

Governing in the Age of Disruption
An article by Boston Consulting Group,
January 2018

The Challenge of Converting Wealth into Well-Being: The 2017 Sustainable Economic Development Assessment
A report by Boston Consulting Group, June 2017

The Private Sector Opportunity to Improve Well-Being: The 2016 Sustainable Economic Development Assessment
A report by Boston Consulting Group, July 2016

Why Well-Being Should Drive Growth Strategies: The 2015 Sustainable Economic Development Assessment
A report by Boston Consulting Group, May 2015

Building Well-Being into National Strategies: The 2014 Sustainable Economic Development Assessment
A report by Boston Consulting Group, February 2014

From Wealth to Well-Being: Introducing the Sustainable Economic Development Assessment
A report by Boston Consulting Group, November 2012

# NOTE TO THE READER

## About the Authors

Joao Hrotko is a managing director and partner in the Lagos office of Boston Consulting Group. He is a core member of the Energy, Financial Institutions, Global Advantage, and Public Sector practices. Since joining BCG, in 2012, he has focused his client work on organization and strategy across an array of sectors, in particular public sector, and oil and gas. Previously, he was a professor at the University of Chicago and the Catholic University in Lisbon.

Enrique Rueda-Sabater has been a senior advisor in BCG's Washington, DC office since 2011. He works with the firm's Public Sector, Global Advantage, and Strategy practices. He had a long career at the World Bank, where his last role was as director of corporate strategy. He has also been director of strategy for emerging markets at Cisco and a visiting fellow at the Center for Global Development.

Nikolaus Lang is a managing director and senior partner in the firm's Munich office and the leader of the firm's Global Advantage practice. He is also the firm's topic leader for mobility, connectivity, and self-driving vehicles; a core member of the firm's Industrial Goods practice, specializing in automotive; and a BCG Fellow whose research focuses on collaboration in the digital age.

Vincent Chin is a managing director and senior partner in BCG's Singapore office. He leads the firm's Public Sector practice globally and has led projects in the economic and social development of countries, including work with their sovereign wealth funds. In the private sector, he specializes in large-scale transformation and business model innovation.

## Acknowledgments

This report was produced by experts in BCG's economic development topic area, and it represents the continuing collaborative efforts of BCG staff from our offices around the world. The authors would like to thank Ruth Chiah for her extensive work in preparing the analysis for this report. They would also like to acknowledge the contributions of Tolu Oyekan, Rasheed Sarumi, and Oluwapelumi Bamgbala, and Doaa Osman, as well as the assistance of BCG Omnia in managing the SEDA model and supporting tailored assessments.

The authors also thank Amy Barrett for writing assistance and Katherine Andrews, Kim Friedman, Abby Garland, Amy Halliday, Frank Müller-Pierstorff, Shannon Nardi, and Deepti Pathak for editing, design, production, and marketing support.

For Further Contact
Tailored assessments using our SEDA methodology can be produced for specific regions or countries and for specific dimensions of economic development. To discuss SEDA and our findings in greater detail, please contact one of the authors.

Joao Hrotko
Managing Director and Partner
BCG Lagos
+ 234 908 707 3300
hrotko.joao@bcg.com

Enrique Rueda-Sabater
Senior Advisor
BCG Washington
rueda-sabater.enrique@advisor.bcg.com

Nikolaus Lang
Managing Director and Senior Partner
BCG Munich
+49 89 2317 4459
lang.nikolaus@bcg.com

Vincent Chin
Managing Director and Senior Partner
BCG Singapore
+65 6429 2688
chin.vincent@bcg.com

© Boston Consulting Group 2019. All rights reserved.

For information or permission to reprint, please contact BCG at permissions@bcg.com.

To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcg.com.

Follow Boston Consulting Group on Facebook and Twitter. 7/19

## BCG
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
