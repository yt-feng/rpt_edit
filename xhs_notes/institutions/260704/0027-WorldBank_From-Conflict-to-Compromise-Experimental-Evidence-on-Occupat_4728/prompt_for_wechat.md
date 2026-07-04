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
# From Conflict to Compromise

Experimental Evidence on Occupational Downgrading in Migration from Myanmar

Yashodhan Ghorpade

Muhammad Saad Imtiaz

POLICY RESEARCH WORKING PAPER 11075

## Abstract

This paper examines the relationship between violent conflict and the willingness of potential migrants to accept lower skilled work (occupational downgrading). The paper develops a theoretical model of migration decisions and tests it using an innovative survey module administered to high-skilled youth in Myanmar. Consistent with the predictions of the model, the findings show that insecurity induced by conflict reduces the additional wage premium that individuals would typically demand for taking on lower skilled work, indicating greater amenability to occupational downgrading. These effects are particularly pronounced for disadvantaged groups, such as women, ethnic minorities, and those with weaker labor market networks or English language skills. The results are driven by respondents from areas under territorial contestation, and those interviewed after the sudden activation of a conscription law during the survey. This further confirms how security considerations may override the preference for skill-appropriate job matching, suggesting that conflict may worsen labor market outcomes and reduce potential gains from migration, especially for disadvantaged groups.

# From Conflict to Compromise: Experimental Evidence on Occupational Downgrading in Migration from Myanmar

Yashodhan Ghorpade and Muhammad Saad Imtiaz

## 1. Introduction

International migration can lead to workers taking on jobs that they are overqualified for, a phenomenon known as occupational downgrading (Kossoudji and Cobb-Clark, 2000; Borjas, 2003; Eckstein and Weiss, 2004). This can have important consequences for both labor market and welfare outcomes, as it represents an underutilization of human capital, and can also have detrimental effects on individual wellbeing (Devillanova et al. 2024), further aggravating the stress that migrants may already face (Garcini et al. 2021). The occurrence of occupational downgrading is symptomatic of labor market imperfections, indicating the likely presence of search frictions, and job-skill mismatches (Akresh et al., 2008; Nikolov et al., 2022). These negative effects may often persist across generations (Achard, 2024).

The literature postulates that occupational downgrading may be observed in the early stages of migrant life, with the expectation that migrants over time assimilate better in the labor market by acquiring destination-specific human capital and eventually finding work better suited to their qualifications (Chiswick, 1978; Zorlu, 2016). However, empirical evidence on the persistence of occupational downgrading is more mixed. On the one hand, Cortes (2004) finds that while refugees in the U.S. initially earn less than natives and economic migrants, by investing in U.S.-specific skills they catch up after a period of 10 years. On the other hand, Borjas (2015) finds only a minimal (2.5 percent) rate of wage growth among a cohort of migrants in the U.S. despite the large initial wage disadvantage (of 27 percent). Bell and Johnson (2023) find little evidence of any labor market improvements among a panel of migrants from the time they initially arrive in the UK and experience substantial occupational downgrading. These workers remained at the lower end of the wage distribution throughout the duration of their stay in the UK. Brell et al. (2020) and Ruiz and Vargas-Silva (2018) find similar results on the persistence of downgrading effects on wages.

The persistence of occupational downgrading depends on several factors such as the initial level of migrants' qualifications, transferability of these skills to the destination country (Akresh, 2008; Adversario, 2020; Evans, 1999; Zorlu, 2016), legal restrictions (World Bank, 2025), language barriers (Akresh, 2008; Adversario, 2020; Nikolov et al., 2022), social networks (Adversario, 2020), cultural similarity between origin and destination (Chiswick et al. 2002; Duleep and Regets 1999; Zorlu, 2016), and gender (Nikolov et al., 2022; Ruiz and Vargas-Silva, 2018). Migrants who face greater barriers in accessing suitable labor market opportunities at destination due to these factors are more likely to experience more severe and persistent downgrading than those better placed to assimilate. Occupational downgrading can be particularly pronounced in the case of refugees (Brell et al., 2020; Zorlu, 2016; Nikolov et al., 2022). Unlike economic migrants who move to leverage spatial disparities in wages (i.e., earn higher wages for work they are qualified to perform), refugee movements are driven primarily by fears of persecution.

Traditional measurements of occupational downgrading tend to focus on migrants' labor market trajectories and outcomes at destination, i.e., after migration. The level of downgrading thus observed is the aggregate effect of factors that operate before, during, and after relocation, and therefore cannot be attributed to pre-departure conditions of the areas of origin alone. We document another driver of migrant occupational-downgrading which has not yet been studied in the literature, which is the willingness of migrants to accept occupational downgrading in the destination because of desperate conditions at home. In other words, conflict induces migration among a group of people who, absent conflict in the origin country, would not otherwise migrate if it resulted in occupational downgrading. Moreover, while occupational downgrading has been studied in several cases of pure economic migration (Akresh, 2008; Adversario, 2020; Nikolov et al., 2022; Chiswick et al. 2002; Duleep and Regets 1999; Ruiz and Vargas-Silva, 2018; Zorlu, 2016; Lebow, 2024), and to some extent among refugees (Brell et al., 2020; Zorlu, 2016; Nikolov et al., 2022), it has not been specifically examined in the context of economic migration from conflict-affected settings.

As the incidence of wars and violent conflict increases globally, $^{1}$ it gives rise not only to refugee movements, but also distress-induced economic migration on a large scale. The effects of the latter on labor market outcomes need to be understood better. For instance, little is known about how exposure to conflict in the country of origin affects migrants' choice of occupation and wages in a safer destination country. Understanding this gap in the literature is critical for both academic and policy objectives. From an academic perspective, measuring the trade-off between physical security and the utility derived from job suitability is imperative to understanding the fuller effects of conflict on economic (especially labor market) outcomes. From a policy standpoint, such analysis can help design suitable policies in destination and origin countries, that can minimize the extent of such downgrading, and therefore maximize the gains from migration for those fleeing hardship. Disaggregating these effects can also help identify which groups of migrants are more likely to experience occupational downgrading, and tailor policy interventions to their needs.

In this paper, we seek to fill some of these gaps in the literature to explain how exposure to conflict affects the likely extent of occupational downgrading among potential migrants. We zoom in on Myanmar, in the aftermath of a military coup and subsequent escalation in conflict, insecurity, and economic hardship. In doing so, we posit migrants' acceptance of occupational downgrading as a trade-off between security and economic wellbeing. By studying the preferences and choices of such individuals before they migrate, we focus on how conflict in the country of origin affects migrants' propensity to accept occupational downgrading. In addition to the literature on occupational downgrading in migration (Leuven and Oosterbeek, 2011; Dustmann and Preston, 2012; Dustmann, Frattini, and Preston, 2013; Lebow, 2024; Brell et al., 2020; Zorlu, 2016; Nikolov et al., 2022), this paper contributes to the wider literature on individual and household decision-making under conditions of violent conflict (Justino et al., 2013; Brück et al., 2014; Justino, 2009) and duress, more generally.

We employ an innovative method to measure migration intentions among high-skilled youth residing and working in Myanmar (and constituting a pool of potential migrants) by analyzing survey respondents' take-up of migration at different wage premia. We examine this for two hypothetical work scenarios; one involves work that is similar to the respondents' current occupation, and another that represents work that the respondent would be overqualified for. A higher premium is generally expected for the lower-skilled job, with the excess of the premium required to take up the lower-skilled job over that for a similar job representing a compensating wage differential (CWD). The CWD can be thought of as the monetary value that compensates a worker for the loss of utility from working on a relatively lower-skilled job and is therefore a measure of the amenability to occupational downgrading. A higher CWD indicates lower amenability to occupational downgrading. Our paper explores how exposure to violent conflict affects the compensating wage differential, and therefore the likelihood of accepting occupational downgrading.

We find that in line with economic theory on compensating wage differentials, respondents demand a 20-percentage point higher wage premium to accept a lower skilled job than they would for a similar job. However, exposure to conflict reduces this incremental premium, suggesting that potential migrants exposed to conflict are more willing to compromise on the suitability of work to their skills when considering work opportunities abroad. These results are stronger for women, ethnic and linguistic minorities, those who are underpaid, have experienced income reductions recently, and lack access to social networks for migration. We argue that political instability and uncertainty makes residents of conflict-affected areas desperate, and more willing to compromise on work suitability. We find suggestive evidence for this mechanism; the effects of conflict on the amenability to occupational downgrading are driven by subgroups that face bleaker prospects and uncertainty at home: those living in areas experiencing territorial contestation and those eligible for military conscription interviewed after the sudden enactment of a conscription law in Myanmar during the rollout of our survey.

Our results contribute to the understanding of migration decisions of people living in fragile and conflict affected countries, where security concerns heavily impress upon the economic calculations that determine migratory flows. They also highlight the challenges distressed economic migrants are likely to face even before they migrate, which in turn should inform policy to minimize hardship and maximize potential gains from migration.

The remainder of this paper is organized as follows: section 2 presents a theoretical model that relates conflict with occupational downgrading considerations; section 3 provides an overview of the study design and the measurement of occupational downgrading; section 4 describes the empirical setting and data sources; section 5 presents results; and section 6 concludes with a discussion of the findings and their implications.

## 2. Theoretical Motivation

Occupational downgrading may arise due to mechanisms that operate at different stages of the migration process. First, conditions before departure can determine the acceptance of occupational downgrading. Those residing in conflict-affected areas may perceive a trade-off between the physical safety at their destination and economic security at home. A fear of persecution or exposure to violence at home may compel them to compromise on earnings and the desirability of a job abroad; a trade-off that those residing in peaceful areas do not have to consider. The imminent consideration to escape violence may also prevent them from taking more time to research more suitable and adequately remunerative jobs abroad. Consequently, adverse conditions before departure may predispose individuals to accept occupational downgrading more readily. Second, the conditions during departure may be markedly different in the case of pure economic migrants viz. refugees or distressed migrants. Unlike the former, the latter categories of migrants may be unable to plan adequately before migrating. Refugee movements typically occur suddenly, whereby movers have limited choice over their destination, and restricted ability to assess jobs or wages, or even to make adequate arrangements for housing and employment before migrating. Conditions of urgent, swift, and insufficiently planned relocation may compel migrants to accept any available work, including jobs they are overqualified for. Finally, conditions after departure, pertaining to destination country policies may limit labor market opportunities. Migrants and especially refugees may not always have access to the legal right to work, or to adequate opportunities for suitable work, especially in camp settings. This puts pressure on them to take up any available job, including those that imply significant downgrading. In the remainder of this paper, we focus exclusively on the first mechanism; i.e. the role of pre-departure conditions in the country of origin (chiefly exposure to violent conflict) in determining the proclivity for occupational downgrading.

## 2.1 Modeling Migration Decisions

Individuals base their decision to move abroad for prospective work, largely driven by wage differentials. Batista and McKenzie (2023) suggest that an individual will migrate to take up a job abroad if the utility from wages and non-wage amenities of working abroad ( $V^{A}(W^{A})$ ) exceed the sum of utility from wages and non-wage amenities of working at home ( $V^{H}(W^{H})$ ) and the cost of migration (C):

$$
V ^ {A} (W ^ {A}) - V ^ {H} (W ^ {H}) > C
$$

We further propose that the utility a person derives from a potential job abroad ( $V^{A}$ ) likely depends not only on wages and non-wage amenities of working abroad ( $W^{A}$ ), but also on qualitative factors related to the nature of the work, such as the individual's perceived relative suitability for the position abroad ( $S^{A}$ ). The total utility that a worker finds abroad is therefore:

$$
V ^ {A} = U (W ^ {A}) + \gamma (S ^ {A})
$$

Where $U(W^{A})$ is the utility from wages and non-wage amenities, and $\gamma(S^{A})$ is the additional utility a worker enjoys from the relative suitability of the prospective job abroad, assumed independent of the former. We conjecture that generally individuals derive higher total utility from work that they perceive is more suitable to them $\left(\frac{\partial\gamma(S^{A})}{\partial S}>0\right)$ . If $\Delta W$ is some wage premium added to the wage earned abroad. Then $\Delta\overline{W}$ is the break-even wage premium, one that makes the individual indifferent between staying home and moving abroad. This indifference condition is given by:

$$
V ^ {A} (W ^ {A} + \Delta \overline {{W}}) = V ^ {H} (W ^ {H}) + C
$$

Solving for $\Delta\overline{W}$ gets us this break-even wage premium over the wage abroad, such that it makes a prospective migrant indifferent between remaining home and migrating abroad: $^{2}$

$$
\Delta \overline {{W}} = \frac {V ^ {H} + C - V ^ {A}}{V ^ {A ^ {\prime}}}
$$

Where $V^{A'}$ measures how utility abroad changes with respect to wages abroad.

## 2.1.1 Compensating Wage Differential

Let $A^{+}$ represent a job abroad that is relatively more suitable to a prospective migrant, perhaps because it is similar in nature to the job at home and let A- represent a less suitable job, perhaps one the individual is overqualified for. We define the compensating wage differential, $\Delta\overline{W}^{D}$ , as the difference between the wage premiums required for the less suitable job, A-, and the more suitable job, $A^{+}$ , which will be given as: $^{3}$

$$
\Delta \overline {{W}} ^ {D} = \Delta \overline {{W}} ^ {-} - \Delta \overline {{W}} ^ {+} = \frac {\gamma (S ^ {A +}) - \gamma (S ^ {A -})}{V ^ {A ^ {\prime}}}
$$

The above expression shows that the compensating wage differential constitutes the loss of utility from job suitability – how much a worker seeks to offset the mismatch of being in a less suitable job by demanding a higher wage premium. Since $\gamma(S^{A+}) > \gamma(S^{A-})$ , we hypothesize:

$$
\Delta \bar {W} ^ {D} > 0
$$

[Hypothesis 1]

As long as a worker derives positive utility from job suitability ( $\frac{\partial\gamma(S^{A})}{\partial S}>0$ ), the break-even wage premium for a less suitable job will likely be higher, resulting in a positive compensating wage differential.

## 2.1.2 The Effects of Conflict

In the presence of adverse conditions at home such as ongoing conflict (F), we argue that an individual's utility depends relatively lesser on wages and job suitability and more on the risks to life, property, and psychological wellbeing. This shift varies continuously with changing conflict, as outlined in the framework that we introduce below. The new utility at home and abroad, in the presence of conflict, are given by:

$$
V ^ {H} (W ^ {H}, F) = U (W ^ {H}) - \psi (F) R ^ {H} (F)
$$

$$
\begin{array}{c} \text {and} \\ V ^ {A} (W ^ {A}, S ^ {A}, F) = (1 - \psi (F)) [ U (W ^ {A}) + \gamma (S ^ {A}) ] \end{array}
$$

Where $-R^{H}(F)$ is the disutility at home due to threat of conflict (F), and $\psi(F) \in [0,1]$ represents the individual's exposure to conflict, with $\psi(F) \to 1$ suggesting that as conflict intensifies, the individual's utility decreases. The term $(1-\psi)$ shows the decreasing weight individuals place on the economic utility of work abroad (e.g., wages and job suitability) as conflict intensity increases at home. This is based on the assumption that as conflict increases, individuals will prioritize minimizing threats to life and property over economic considerations such as wages because survival and safety are now the main motivators under intensified conflict. It also follows that when F = 0 (i.e. in no-conflict areas), the individual's utility depends entirely on wages and job suitability. As conflict escalates, wages and job suitability abroad become less important in determining overall utility. Reflecting these changes, the break-even wage premium in the presence of conflict is given as:

$$
\Delta \bar {W} (F) = \frac {U (W ^ {H}) - \psi (F) R ^ {H} (

[中间内容因长度限制已省略]

lled Occupations</td></tr><tr><td>Conflict Fatalities in Township: log(1+n)</td><td>-17.55**(8.409)</td><td>-5.56*(3.248)</td></tr><tr><td>N</td><td>412</td><td>1218</td></tr></table>

Table A4.5 Heterogeneous Effects: By English Language Skills

<table><tr><td rowspan="2"></td><td colspan="2">English (speaking)</td><td colspan="2">English (Reading/ Writing)</td></tr><tr><td>Less than good</td><td>Good</td><td>Less than good</td><td>Good</td></tr><tr><td rowspan="2">Conflict Fatalities in Township: log(1+n)</td><td>-7.17**</td><td>-17.95</td><td>-9.34***</td><td>-0.41</td></tr><tr><td>(3.121)</td><td>(15.220)</td><td>(3.067)</td><td>(9.626)</td></tr><tr><td>N</td><td>1510</td><td>120</td><td>1381</td><td>249</td></tr></table>

Table A4.6 Heterogeneous Effects: By Household Migration Status, Gender

<table><tr><td rowspan="2"></td><td rowspan="2">No HH member migrated recently</td><td rowspan="2">Some HH member migrated recently</td><td colspan="2">No HH member migrated recently</td><td colspan="2">Some HH member migrated recently</td></tr><tr><td>Women</td><td>Men</td><td>Women</td><td>Men</td></tr><tr><td rowspan="2">Conflict Fatalities in Township: log(1+n)</td><td>-9.81***</td><td>15.35</td><td>-11.69***</td><td>-7.65</td><td>7.88</td><td>30.69</td></tr><tr><td>(3.249)</td><td>(10.193)</td><td>(3.682)</td><td>(5.752)</td><td>(12.388)</td><td>(37.478)</td></tr><tr><td>N</td><td>1476</td><td>148</td><td>888</td><td>588</td><td>93</td><td>55</td></tr></table>

Table A4.7 Heterogeneous Effects: By Access to Social Networks for Migration

<table><tr><td rowspan="2"></td><td colspan="2">HH received remittances</td><td colspan="2">HH has job search contact abroad</td><td colspan="2">HH has foreign job search contact in Myanmar</td><td colspan="2">HH knows someone who can host members abroad</td></tr><tr><td>No</td><td>Yes</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr><tr><td rowspan="2">Conflict Fatalities in Township: log(1+n)</td><td>-7.36**</td><td>-8.10</td><td>-9.99**</td><td>-5.89</td><td>-11.55***</td><td>-1.39</td><td>-8.45*</td><td>-7.20</td></tr><tr><td>(3.514)</td><td>(5.919)</td><td>(4.439)</td><td>(4.684)</td><td>(3.582)</td><td>(5.293)</td><td>(4.310)</td><td>(5.366)</td></tr><tr><td>N</td><td>1354</td><td>276</td><td>999</td><td>631</td><td>1015</td><td>615</td><td>1014</td><td>616</td></tr></table>

Table A4.8 Heterogeneous Effects: By extent of labor market match (current), Gender

<table><tr><td rowspan="2"></td><td rowspan="2">Job not related to field of study</td><td rowspan="2">Job somewhat related to field of study</td><td rowspan="2">Job closely related to field of study</td><td colspan="2">Job not related to field of study</td><td colspan="2">Job somewhat related to field of study</td><td colspan="2">Job closely related to field of study</td></tr><tr><td>Women</td><td>Men</td><td>Women</td><td>Men</td><td>Women</td><td>Men</td></tr><tr><td rowspan="2">Conflict Fatalities in Township: log(1+n)</td><td>-9.97**</td><td>-6.71*</td><td>-3.84</td><td>-8.10</td><td>-11.97</td><td>-11.10**</td><td>4.52</td><td>-6.01</td><td>-6.00</td></tr><tr><td>(4.367)</td><td>(47)</td><td>(8.226)</td><td>(5.909)</td><td>(8.616)</td><td>(51)</td><td>(8.883)</td><td>(13.304)</td><td>(10.174)</td></tr><tr><td>N</td><td>617</td><td>697</td><td>316</td><td>361</td><td>256</td><td>435</td><td>262</td><td>188</td><td>128</td></tr></table>

Table A4.9 Heterogeneous Effects: By Relative Income, Gender

<table><tr><td rowspan="2"></td><td rowspan="2">Paid on par/ above peers (perceived)</td><td rowspan="2">Underpaid (perceived)</td><td colspan="2">Paid on par/ above peers (perceived)</td><td colspan="2">Underpaid (perceived)</td></tr><tr><td>Women</td><td>Men</td><td>Women</td><td>Men</td></tr><tr><td rowspan="2">Conflict Fatalities in Township: log(1+n)</td><td>-4.51</td><td>-10.72**</td><td>-9.21*</td><td>1.14</td><td>-10.97**</td><td>-7.18</td></tr><tr><td>(3.553)</td><td>(4.165)</td><td>(4.731)</td><td>(7.106)</td><td>(5.261)</td><td>(7.241)</td></tr><tr><td>N</td><td>869</td><td>761</td><td>506</td><td>363</td><td>478</td><td>283</td></tr></table>

Table A4.10 Heterogeneous Effects: By Income changes, Gender

<table><tr><td rowspan="2"></td><td colspan="2">Income Change in past Year</td><td colspan="2">Income Same/ Increased since last year</td><td colspan="2">Income decreased since last year</td></tr><tr><td>Same/ Increase</td><td>Decrease</td><td>Women</td><td>Men</td><td>Women</td><td>Men</td></tr><tr><td rowspan="2">Conflict Fatalities in Township: log(1+n)</td><td>-4.81</td><td>-20.87**</td><td>-7.59*</td><td>-0.74</td><td>-25.71**</td><td>-16.24</td></tr><tr><td>(3.493)</td><td>(8.173)</td><td>(4.055)</td><td>(5.170)</td><td>(11.269)</td><td>(18.327)</td></tr><tr><td>N</td><td>1272</td><td>358</td><td>777</td><td>495</td><td>207</td><td>151</td></tr></table>

Table A4.11 Heterogeneous Effects: By Household Characteristics

<table><tr><td rowspan="2"></td><td colspan="2">HH income per capita</td><td colspan="2">HH income relative to needs</td><td colspan="2">Outstanding household debt?</td></tr><tr><td>Low</td><td>High</td><td>Insufficient</td><td>Sufficient</td><td>No</td><td>Yes</td></tr><tr><td rowspan="2">Conflict Fatalities in Township: log(1+n)</td><td>-7.08*</td><td>-8.06**</td><td>-10.76**</td><td>-8.01**</td><td>-7.07**</td><td>-11.86**</td></tr><tr><td>(4.277)</td><td>(3.674)</td><td>(5.148)</td><td>(3.632)</td><td>(3.309)</td><td>(5.929)</td></tr><tr><td>N</td><td>762</td><td>868</td><td>614</td><td>1016</td><td>1098</td><td>454</td></tr></table>

For all tables: Standard errors clustered at the township level and indicated in parentheses. Controls as indicated in Table 2.
"""
