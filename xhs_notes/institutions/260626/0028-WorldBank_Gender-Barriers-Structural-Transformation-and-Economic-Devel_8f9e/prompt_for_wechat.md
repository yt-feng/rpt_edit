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
# Gender Barriers, Structural Transformation, and Economic Development

Gaurav Chiplunkar
Tatjana Kleineberg

POLICY RESEARCH WORKING PAPER 11083

## Abstract

The representation and significance of women in the labor force have grown significantly over the past five decades around the globe. Using nationally representative data from more than 90 countries, this paper documents distinct gender patterns in employment transitions across both sectors and occupations during this period. Using a model of occupational and sectoral choice and focusing on six major economies, the paper finds that declining gender barriers—defined as gender-specific distortions in employment and wages—were a key driver of the observed rise in female labor force participation, expansion of the service sector, and increases in real GDP per capita from 1970 to 2018, but with substantial variation across countries.

# Gender Barriers, Structural Transformation, and Economic Development\*

Gaurav Chiplunkar
University of Virginia

Tatjana Kleineberg
World Bank

Keywords: Economic Growth, Structural Transformation, Gender, Misallocation

## 1 Introduction

The role of women in the labor force has undergone a profound transformation over the past century, evolving from a largely marginalized position (Boserup, 1975) to one of increasing representation, influence, and leadership in the global workforce (Goldin, 2024). In the 1970s, for instance, there were, on average, fewer than four women for every ten men in professional and managerial positions across a large cross-section of countries. By the 2010s, this number increased to more than eight women for every ten men. This growing representation of women in the labor market not only reflects progress toward gender equality, but also has significant implications for countries' aggregate employment structures, productivity, and economic growth. $^{1}$ Over the same period, economies around the world have undergone fundamental structural changes, with employment transitioning from agriculture to manufacturing and services (Kuznets, 1973).

In this paper, we study the evolution of gendered labor market opportunities, economic growth, and structural change empirically and theoretically. First, we use micro-data from 91 countries at different stages of development and over five decades to document new evidence on the link between economic development and gendered labor market outcomes. We then propose a model to study these patterns. Our framework integrates two broad explanations for the observed evolution of gendered labor market outcomes and economic growth: first, economic mechanisms such as sector- or occupation-specific technological change, income effects in consumption, and improved education; and second, gender-specific distortions arising from discrimination and social norms. We structurally estimate our model to six major economies, which offer high-quality gender-disaggregated data on both wages and employment over five decades. We then use the estimated model to study the effects of changing gender distortions on structural change and aggregate growth in these countries. We find that gender distortions are important and have declined in most countries. On average, the decline in gender distortions in our sample countries accounts for a substantial share of overall economic growth and reallocation of employment in the labor market.

We begin by providing new evidence on gendered employment patterns across occupations and sectors. Our analysis draws on censuses and nationally representative household and labor force surveys from 91 countries, spanning five decades (1970-2018) and covering over 300 country-years. Using these data, we first show that the canonical process of structural transformation – employment transitions from agriculture to manufacturing and services with economic development – is primarily driven by men. Women follow a different pattern: at low levels of development, they exit agriculture and primarily transition out of the labor force. At higher levels of development, women re-enter the labor force, primarily in the service sector. Unlike men, women’s representation in manufacturing remains low across all development levels. We further document gender differences in occupational choices within sectors, showing that men increasingly work in professional and industrial jobs in richer countries, while women’s employment (relative to men) expands faster in clerical jobs but slower in professional and industrial jobs.

In addition to gender employment gaps, we also analyze the evolution of gender wage gaps for a select set of countries which provide high-quality micro-data on hourly earnings. We find that wage gaps have narrowed over time across all occupation-sector pairs. However, women in the 2010s still earned, on average, only 70 cents for every dollar earned by men. Furthermore, we observe a weak correlation between gender wage gaps and countries' development levels – in contrast to gender employment gaps that tend to decrease in richer countries. Additionally, gender employment and wage gaps do not necessarily correlate across occupation-sector pairs.

We then propose a model of occupational and sectoral choice that can speak to these empirical findings and that builds on Hsieh et al. (2019). The documented changes in gendered employment and wage patterns – both across countries and within countries over time – can be partly driven by previously studied economic channels, such as income effects in consumption, sector- or factor-specific technological change, or shifts in the supply of, or returns to human capital. $^{2}$ Specifically, technological change and income effects can increase labor demand in the “female-gendered” service sector, disproportionately benefiting women (Ngai and Petrongolo, 2017; Fan et al., 2023). Additionally, the narrowing of gender education gaps has expanded the supply of women’s human capital (Evans et al., 2021; Feng et al., 2023). On the other hand, the documented changes in gendered labor market outcomes can also be driven by a decline in barriers that women face in certain occupations and sectors, which would increase women’s labor supply in them. $^{3}$

Our model enables us to disentangle the effects of economic mechanisms from those of changing gender barriers. In the model, individuals differ by gender and ability, while occupation-sector pairs differ in wage rates per unit of human capital, returns to ability, and costs or barriers that men and women face when working in them. Individuals receive idiosyncratic preference shocks across occupation-sector pairs and then choose their occupation and sector. We model the option of not participating in the labor force as an additional choice, which we call the “home sector” (Hsieh et al., 2019; Ngai and Petrongolo, 2017). On the demand side, consumers have non-homothetic preferences, allowing them to shift consumption away from agriculture and toward services as their income rises – a key driver of structural transformation emphasized in the literature. $^{4}$ Wage rates per human capital unit in each occupation-sector and prices in each sector are endogenously determined in equilibrium.

Following Hsieh et al. (2019), we define two types of gender barriers: first, “gender norms” which capture the excess utility costs that women incur relative to men when working in a given occupation-sector pair; and second, female “wage discrimination”, which captures differences in remuneration that women receive per human capital unit relative to men. In the absence of distortions, an efficient allocation of talent ensures that high-ability workers sort into sectors and occupations that offer the highest returns to their ability. However, gender barriers distort these choices, shifting workers away from the jobs where they have a comparative advantage. For instance, high-ability women may opt out of the labor market or work in clerical jobs with low returns to their ability rather than pursuing professional or managerial jobs with higher returns. Such distortions therefore lead to a misallocation of talent, reducing aggregate productivity and output.

We estimate the model to a core sample of six large economies – India, Indonesia, Brazil, Mexico, Canada and the United States – for which we have employment and hourly wage data spanning four to five decades. Gender barriers in each occupation-sector and country-year are quantified as “wedges” which ensure that our model equations precisely match the data on gender employment and wage gaps after accounting for economic fundamentals and individuals’ employment and consumption choices in equilibrium. For example, the model expresses the observed gender wage gap in each occupation-sector as a function of a model-implied gender gap in human capital and the wage discrimination women face relative to men. To measure gender barriers, we assume that men and women have the same productivity within each occupation-sector, conditional on their model-implied human capital levels. $^{5}$

Our estimates of gender barriers reveal three main findings. First, gender norms have declined significantly over time, particularly in the service sector and in professional, managerial, and clerical jobs. Second, wage discrimination has also declined across all sectors and occupations, but relatively less in professional jobs. Third, trends in gender barriers vary considerably across countries: they worsened in India, showed little improvement in Indonesia, and declined substantially in Brazil, Mexico, Canada, and the United States. As a validation, we show that our estimated gender barriers strongly correlate across countries and over time with empirically measured gender norms and labor market constraints.

Using our estimated model, we then quantify the contribution of changing gender barriers to countries' structural transformation and economic growth over the past five decades, in the spirit of a growth accounting exercise. To do so, we simulate counterfactual employment and growth paths for each country while holding gender barriers in each occupation-sector fixed at their calibrated values from the 1970s but allowing all other variables, such as technologies and skill distributions, to evolve over time. We find that declining gender barriers had large effects on female labor force participation, structural transformation, and economic growth in all countries of our sample, except India. Averaging across countries, we find that changes in gender barriers between 1970 and the 2010s accounted for $40\% - 45\%$ of employment growth and $20\% - 35\%$ of output growth in the manufacturing and service sectors. Declining gender barriers particularly contributed to the rapid rise of the service sector, revealing a novel channel for explaining the premature deindustrialization observed in developing countries in recent decades (Rodrik, 2016; Huneeus and Rogerson, 2024). On average, changes in gender barriers accounted for $28\%$ of observed real GDP per capita growth in our sample, with significant heterogeneity across countries – ranging from $10\%$ in Indonesia and $28\%$ in the United States to $40\%$ in Canada and Mexico, and over $50\%$ in Brazil. In contrast, worsening gender barriers in India imply that economic growth would have been higher if these barriers had not changed.

In a series of additional analyses, we examine the mechanisms and robustness of our findings. First, we show in our baseline model that declining gender norms had a larger effect on economic growth than reductions in wage discrimination. Second, we show that our aggregate results are similar in a model where workers sort into occupations and sectors based on idiosyncratic talent shocks rather than preference shocks, as in the baseline model. Despite similar aggregate effects, the relative importance of wage discrimination and gender norms reverses in a model with talent shocks, which aligns with the findings from Hsieh et al. (2019) and is further discussed in Section 7.2. Third, we show that non-homothetic preferences amplify the effects of declining gender barriers on aggregate and sectoral outcomes because falling barriers make economies richer, shifting consumption and labor demand away from agriculture and toward manufacturing and services. Lastly, we perform a robustness check that accounts for gender-specific comparative advantage across occupation-sector pairs, which we quantify from a benchmark economy – the United States in 2015 – which we assume to have no wage discrimination, following Lee (2024). After adjusting for these estimated gender productivity differences in all country-years, changes in gender barriers remain relevant, accounting for 21% of observed growth in GDP per capita, compared to 28% in the baseline.

Related Literature. A large literature documents gender disparities in the labor market, but only a few recent studies provide cross-country comparisons and examine the macroeconomic implications of gender roles. Cuberes and Teignier (2014), Albanesi et al. (2023), and Olivetti et al. (2024) provide excellent reviews. Several papers study the link between gender roles and structural transformation in the United States, including Ngai and Petrongolo (2017), Ngai et al. (2024), Moro et al. (2017), and Rendall (2018). Across countries, Gottlieb et al. (2023), Bridgman et al. (2018) and Bick et al. (2022) use rich time-use surveys to examine the implications of gender differences in hours worked. Our quantitative approach – which measures gender barriers as wedges and quantifies their importance for aggregate outcomes – aligns most closely with Hsieh et al. (2019), Lee (2024), and Chiplunkar and Goldberg (2024). Hsieh et al. (2019) study the aggregate implications of talent misallocation due to gender and racial barriers in the United States. They find, similar to us, that a reduction in barriers explains 20-40% of US economic growth over the last decades. Lee (2024) documents that gender barriers in poor countries are higher in non-agriculture sectors, also aligning with our findings.

While the literature on structural transformation emphasizes sectoral employment transitions, we further document transitions across occupations within sectors, with a focus on gender. We find that gender differences across sectors are more important in poorer countries, while occupational differences matter more in richer countries, in line with recent work by Caunedo et al. (2023) and Bandiera et al. (2022). We therefore develop one consistent framework to jointly study the extensive margin of entering the labor force and the intensive margin of choosing a particular sector and occupation. The model incorporates the drivers of employment choices that have been emphasized in the macro-labor and structural transformation literature, which include heterogeneity in workers' ability and hence their comparative advantage, gender-specific barriers, differential returns to ability across occupation-sectors (Hsieh et al., 2019; Cassan et al., 2024), as well as non-homothetic demand, sector-specific technological change, and changing human capital supply (Ngai and Pissarides, 2007; Herrendorf et al., 2014; Boppart, 2014; Ngai and Petrongolo, 2017; Comin et al., 2021; Porzio et al., 2022; Feng et al., 2023).

The paper is organized as follows: Section 2 describes the data and provides new evidence on the link between economic development and gendered labor market outcomes. Section 3 presents the theoretical model and Section 4 describes the identification and model quantification. Sections 5 and 6 present the estimation results and the counterfactual simulations. Section 7 examines mechanisms and tests the robustness of our analysis. Section 8 concludes.

## 2 Empirical Facts

## 2.1 Data

Data Sources and Sample Description. We use data from the Integrated Public Use Microdata Series (IPUMS International, 2020), which provides harmonized individual-level data on demographic and employment variables from nationally representative censuses, and household and labor force surveys for many countries and years. We extract employment information by occupation, sector, and gender for 91 countries and 305 country-years. The time coverage ranges from 1960 to 2020 and includes, on average, 3-4 rounds of data for each country. Online Appendix C shows that the data has good coverage over the time period and the entire development spectrum. We complement the IPUMS data with labor force surveys from the World Bank Global Labor Database (GLD) and the World Bank i2d2 database. $^{6}$

For our quantitative exercise, we use a core sample of six large economies – India, Indonesia, Mexico, Brazil, Canada, and the United States – which additionally offer high-quality micro data on hours worked and compensation, enabling us to calculate workers' hourly wages. In addition, these countries provide data for more than four decades, allowing us to study the process of structural transformation and the evolution of gendered labor market outcomes over a long period of time. The six economies span a wide income spectrum (Figure OA.7 in the Online Appendix) and cover around 25-30% of the world population. For Indonesia, we complement the IPUMS census data with the SAKERNAS labor force survey to extend the time coverage of wage data to 2018. For India, we use survey data from the National Sample Surveys (NSS), the Employment-Unemployment Survey (EUS), and the Periodic Labor Force Survey (PLFS) up to 2018.

Sector and Occupation Classification. We define three market sectors – agriculture, manufacturing, and services – by assigning the more detailed industry codes from IPUMS and the labor force surveys to these three categories. The categorization follows the literature (Herrendorf et al. (2013); Herrendorf and Schoellman (2018)) and is outlined in Online Appendix C, Table OA.6. We define a fourth sector as the “home sector” to which we attribute unemployed and inactive individuals, following Hsieh et al. (2019).

At the occupation level, we use 1-digit ISCO codes. We aggregate the top three ISCO codes, which results in the following seven occupation categories: (1) professionals, (2) clerks, (3) service workers, (4) skilled agricultural workers, (5) crafts and trades workers, (6) plant and machine operators, and (7) elementary occupation workers. To minimize measurement errors arising from small sample sizes in specific occupation-sector-gender cells, we impose two restrictions. First, we consider only two occupations within the agriculture sector: skilled agricultural workers and el

[中间内容因长度限制已省略]

s from Mexico 1990) and Mexico 2015 (for which we use the ratios from Mexico 2010).

## C.3.3 Measuring Income

IPUMS provides three main income variables:

1. INCTOT: reports the person's total personal income from all sources in the previous month or year.

2. INCEARN: reports the person's total income from their labor (wages, business, or farm) in the previous month or year.

3. INCWAGE: reports the person's weekly, monthly or annual wage or salary income.

The labor force surveys provide the equivalent of INCWAGE. Each country-year differs in the availability of these variables. When possible, we try to use the same income measure for a given country over time. More specifically, countries have the following availability:

1. Brazil: 1970, 1980, 1991, 2000, 2010

\- INCTOT for the previous month is available and used for all sample years.

\- Hours Worked per Week: HRSWORK1 available for 1991, 2000 and 2010. HRSWORK2 available for 1980. For 1970 we use the gender-sector-occupation average from the 1980 data.

\- Earnings per hour = INCTOT/(4.33\*Hrs Worked per Week).

## 2. Canada: 1971, 1981, 1991, 2001, 2011

\- INCTOT for the previous year is available and used for all sample years.

\- Hours Worked per Week: HRSWORK1 available 1981 onwards, HRSUSUAL2 available for 1971.

\- Months Worked per Year: MONTHSWRK is available and used to convert annual income to hourly income.

\- Earnings per hour = INCTOT/(4.33\*Hrs Worked per Week\*Months Worked).

## 3. India: 1983, 1987, 1993, 1999, 2004, 2009, 2011, 2018

\- There is no information on hours worked provided in IPUMS, so we instead rely on data from the labor force surveys, in particular the Indian Employment-Unemployment Survey (EUS) from 1983-2009 and the Periodic Labor Force Survey (PLFS) for 2011-2018. Both surveys have been harmonized in the World Bank's Global Labor Database (GLD).

\- Income is measured as "Last wage payment, primary job, excl. bonuses, etc. (7-day ref period)". An additional variable records the frequency of payment for each survey.

\- Hours Worked per Week: The variable records the hours of work last week for the individual's main job.

\- Wages per hour: We convert weekly wages to hourly wages using hours worked per week.

## 4. Indonesia: 1976, 1995, 2015, 2018

\- Income: In IPUMS, the only available income measure is INCWAGE of the previous month, which is available only for the years 1976 and 1995.

\- Hours worked: HRSWORKED1 is available for 1995 and HRSACTUAL1 is available for 1976.

\- For 1976 and 1995, we compute wages per hour = INCWAGE/(4.333\*Hrs Worked per Week).

\- For the time period from 1994 to 2019, we complement the IPUMS data for Indonesia with data from the SAKERNAS labor force survey.

\- Wage income is available in the SAKERNAS survey for most years and is defined as "Last wage payment, primary job, excl. bonuses, etc. (7-day ref period)".

\- Hours worked in the last week is available in the SAKERNAS survey.

\- For 1994-2018, we compute hourly wages by dividing weekly wage income by weekly hours worked.

## 5. Mexico: 1970, 1990, 1995, 2000, 2005, 2010, 2015

• INCTOT of the previous month is available in 1970, 1995, and 2000.

• INCEARN of the previous month is available in 1990, 1995, 2000, and 2015.

• We use the variable INCTOT in 1970 and INCEARN in 2015.

\- Hours worked: HRSWORKED1 is available for 1990, 1995, 2000, and 2010. For 1970 we use the gender-sector-occupation averages of the 1990 survey. For 2015 we use the gender-sector-occupation average of the 2010 survey.

\- Earnings per hour = INCTOT or INCEARN / (4.33\*Hrs Worked per Week)

## 6. United States: 1970, 1980, 1990, 2000, 2005, 2010, 2015

\- INCTOT in the previous year is available and used in all sample years.

\- Hours worked: HRSWORK1 is available from 1980 onwards. HRSWORK2 is available for 1970. MONTHSWRK is available for all years.

\- Earnings per hour = INCTOT/(4.33\*Hrs Worked per Week\*Months Worked).

## C.3.4 Measuring Income: Data Cleaning and Aggregation

We first clean the data on hourly wages and then compute men and women's aggregate and average wages for all occupation-sector pairs. We do the cleaning separately for each country year.

We trim hourly wages at the 99th percentile for each occupation-sector-gender cell. If workers' income is missing, we impute it by estimating the following Mincer regression:

$$
\ln (\mathrm{wage} _ {i}) = \alpha * \mathrm{YrsSchool} _ {i} + \beta * \mathrm{Exp} _ {i} + \gamma * \mathrm{Exp} _ {i} ^ {2} + u _ {o j g} + \epsilon_ {i},\tag{OA.7}
$$

which regresses the log of hourly wages of individuals i on their years of schooling, experience, experience squared, and gender, sector, and occupation fixed effects. We then use the predicted values from the Mincer regression to impute hourly income for all employed individuals for which income data is missing.

We compute annual total earnings for each individual by multiplying reported monthly income times 12 (Brazil, Mexico, Indonesia IPUMS), reported weekly income times 52 (India and Indonesia labor force surveys) or by simply using reported annual income (Canada and US IPUMS). We then aggregate income across individuals to the occupation-sector-and-gender level after adjusting individuals' survey weights for part-time employment as described above. Average earnings in each occupation-sector-gender cell is then equal to annual aggregate earnings divided by the number of “effective workers” | which again adjusts for part-time workers as described above.

Earnings in Home Sector: For each country-year, we set earnings in the Home Sector equal to the measured earnings of women who work in “elementary occupations” in the service sector.
"""
