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
- 已识别机构名：`世界银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份世界银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Consequences of Growing Up Displaced Evidence from Displaced Children in Colombia

Tatiana Hiller

Andrés Moya

Sandra V. Rozo

POLICY RESEARCH WORKING PAPER 11429

## Abstract

This paper examines how forced displacement shapes child development beyond socioeconomic disadvantage. The paper uses original data on roughly 1,600 Venezuelan refugees, Colombian internally displaced individuals, and nondisplaced children in Medellín, Colombia. The analysis adapts rank-rank regressions from the intergenerational mobility literature to a forced displacement setting, ranking each child's developmental outcomes against household wealth. The paper documents substantial gaps that persist after holding wealth and parental background fixed. It also shows that the cause of displacement shapes the nature of the gaps. Venezuelan refugees displaced by acute material deprivation fall 19 and 13 rank points behind in cognitive and physical development, respectively. Colombian children displaced by armed conflict fall 12 rank points behind in depression and exhibit elevated trauma. Access to regularization and social services is associated with narrower gaps.

# Consequences of Growing Up Displaced: Evidence from Displaced Children in Colombia \*

Tatiana Hiller $^{\dagger}$ Andrés Moya $^{\ddagger}$ Sandra V. Rozo $^{\S}$

Authorized for distribution by Dean Jolliffe, Research Manager, Development Research Group, Development Economics, World Bank Group

JEL Classification: F22, J13, O15

Keywords: Forced Displacement, Children development, Colombia.

## I INTRODUCTION

Forced displacement is one of the defining crises of our time. Driven by armed conflict, political instability, and humanitarian collapse, the global displaced population has more than quintupled in the last fifty years, reaching 123 million people in 2025 (UNHCR, 2024b). Children account for nearly 45 percent of this population, yet they remain largely invisible in both policy and empirical research (UNHCR, 2024a). Displaced children face the trauma of forced migration, family disruption, prolonged legal uncertainty, interrupted schooling, the loss of social networks, and discrimination in host communities, during the years when the returns to human capital investment are highest (Heckman, 2006). These stressors can permanently impair cognitive, physical, and socioemotional trajectories in ways that general poverty alone does not predict. Whether the developmental deficits these children exhibit reflect displacement-specific mechanisms or simply socioeconomic disadvantage carries direct implications for how social protection systems should respond.

We examine three questions. First, we ask whether displaced children exhibit developmental gaps relative to non-displaced peers, and whether the cause of displacement shapes the dimensions in which those gaps appear. Children displaced by armed conflict face trauma exposure and elevated mental health risks, while those fleeing a humanitarian and economic crisis face more acute material deprivation. Second, we ask whether these gaps can be accounted for by socioeconomic status or parental background. We approach this in two steps. We first condition on household wealth (and parental background) to ask whether gaps remain at the same average level of resources. We then adapt the rank-rank regression framework of Chetty et al. (2014) and Jensen and Manning (2025) to ask whether gaps fade across the wealth distribution. In the voluntary migration literature, developmental differences among children of immigrants largely disappear once parental socioeconomic status is held fixed (Abramitzky et al., 2021a; Jensen and Manning, 2025). If the same pattern holds for forcibly displaced children, standard poverty-targeting policies may suffice; if gaps persist at equivalent levels of household wealth, targeted integration and mental health interventions may be necessary. Third, for refugee children, we ask whether access to legal status, health care, education, and social services is associated with narrower gaps.

We examine these questions in Colombia, where forcibly displaced people, including IDPs and refugees, account for 21 percent of the population and 9.6 percent of the world's displaced. The country has experienced decades of protracted internal conflict and currently hosts 8.4 million Internally Displaced Persons (IDPs) legally recognized by the state (Unidad para las Víctimas, 2024). It is also the primary destination for refugees fleeing the Venezuelan crisis. $^{1}$ Since 2015, around three million Venezuelans have crossed into Colombia, fleeing acute food shortages and the collapse of public services (UNHCR, 2024a). The Colombian government responded with one of the most inclusive regularization programs in the developing world, granting roughly two million refugees temporary legal status and access to the social protection system. Colombia is therefore one of the few middle-income countries where IDPs displaced by armed conflict and refugees displaced by humanitarian collapse coexist at scale within the same institutional environment.

The two displaced populations face distinct conditions, both before and after arrival. Venezuelan refugees flee acute material deprivation (Cabra-Ruiz, Rozo and Sviatschi, 2024) and arrive in Medellín without productive or social assets, but typically without direct exposure to armed conflict (Moya and Rozo, 2025). Colombian IDPs are entitled to the same social protection benefits as non-displaced Colombians in principle, but their effective access remains lower, and they carry the burden of conflict exposure, transmitted directly or across generations (Ibáñez and Moya, 2010; Moya and Carter, 2019). These contrasts shape the developmental dimensions in which gaps are likely to appear.

Our analysis draws on the Venezuelan Refugee Panel Survey for Kids (VenReps Kids), a representative survey of children in Medellín that we designed and fielded for this study. Medellín is one of the Colombian cities with the highest concentrations of both Venezuelan refugees and Colombian IDPs. The survey covers Venezuelan refugee, Colombian IDP, and non-displaced Colombian children aged 5 to 10, and includes harmonized measures of cognitive, physical, socioemotional, and mental health development. To our knowledge, it is the first dataset to collect comparable developmental information on these three populations within a single host setting in a developing country.

Our analysis proceeds in three steps, one for each question. First, we document gaps in each developmental domain between displaced and non-displaced children. Second, we ask how much of each gap is accounted for by household wealth and parental background. We begin with unconditional differences, then condition on average household wealth, and then adapt the rank-rank framework of Chetty et al. (2014) and Jensen and Manning (2025) to characterize the relationship between household wealth rank and child developmental rank separately for refugees, IDPs, and non-displaced children. This framework distinguishes two features of the wealth-development relationship: the rank gap between displaced and non-displaced children at equivalent points in the wealth distribution, and the wealth-development gradient within each group, which captures how strongly household resources map into children's outcomes. Third, we ask whether, among refugee children, access to legal residence through regularization and other dimensions of service access is associated with narrower gaps. The main analysis centers on the first survey wave, which is representative and unaffected by differential attrition.

We document three key results. First, displaced children exhibit substantial developmental gaps relative to non-displaced peers, and the developmental domains in which gaps appear depend on the cause of displacement. Venezuelan refugee children show the largest gaps in cognitive development and physical health, scoring 0.34 standard deviations below non-displaced peers on receptive vocabulary and 0.50 standard deviations below on age-standardized Body Mass Index. These patterns are consistent with the material deprivation and limited access to services that characterize deprivation-driven displacement. Colombian IDP children, by contrast, show gaps concentrated in mental health and socioemotional development, scoring 0.25 standard deviations below non-displaced peers on depression, 0.21 on socioemotional functioning, and 0.18 on trauma symptoms, consistent with conflict exposure (Sánchez-Ariza, Cuartas and Moya, 2023). The IDP pattern holds for children directly affected by displacement and for those affected indirectly through their parents, pointing to both direct exposure and intergenerational transmission as plausible channels. The coefficients differ between IDPs and refugees in five of the six outcomes we examine, indicating that the two types of displacement are associated with distinct developmental patterns rather than a single uniform displacement experience.

Second, the gaps cannot be accounted for by socioeconomic disadvantage. Conditioning on parental and grandparental education leaves the gaps essentially unchanged. Further conditioning on household wealth attenuates the refugee gaps in cognitive development and physical health but does not close them, and the IDP gaps in mental health remain largely unchanged. The rank-rank analysis delivers the same message with sharper detail. At equivalent points in the wealth distribution, refugee children rank 18 percentile points below non-displaced peers in cognitive development and 13 points below in physical health, and IDP children rank 10 and 12 points below in cognitive development and depression. Household wealth narrows only the refugee cognitive gap. For IDPs, gaps are flat across the wealth distribution in every domain we examine, and the refugee physical health gap is similarly flat. The developmental disadvantages associated with displacement therefore do not respond to material resources in the way that ordinary socioeconomic gaps do.

Third, access to Colombia's regularization program, which grants refugees the right to work and access to the social protection system, is associated with substantially narrower gaps among refugee children. Undocumented refugee children score 0.77 standard deviations below non-displaced peers in receptive vocabulary, compared with 0.24 standard deviations for regularized refugees, and we observe a similar pattern for physical health. The association extends to other dimensions of service access, including social registry enrollment, education, and health insurance. Regularized refugees nonetheless retain gaps in cognitive development and physical health, indicating that institutional access narrows but does not eliminate the developmental disadvantages associated with displacement.

Our paper contributes to three groups of literature. First, we contribute to the literature on forced migration (Card, 1990; Foged and Peri, 2016; Dustmann, Vasiljeva and Piil Damm, 2019; Steinmayr, 2021; Michalopoulos et al., 2025; Chiovelli et al., 2021; Rozo, 2025; Moya and Rozo, 2025) by providing the first representative, longitudinal dataset on the holistic development of forcibly displaced children in a low- and middle-income host country. Over three-quarters of the world's displaced populations are hosted in settings comparable to ours, yet the existing evidence on displaced youth relies almost entirely on clinical samples, cross-sectional surveys, or data from high-income resettlement countries where selection into arrival may differ systematically from the broader displaced population (Fazel et al., 2012; Draper et al., 2022). We assemble a representative sample of Venezuelan forced migrants and Colombian internally displaced persons aged 5 to 10 in Medellín, combining snowball sampling with satellite imagery of informal settlements and administrative records from NGOs to reach a population for which no census exists. Critically, we measure development across four domains simultaneously, spanning cognitive functioning, socioemotional development, physical health, and mental health outcomes, allowing us to document how displacement-related deficits compound across developmental domains and stages in ways the existing literature, which concentrates disproportionately on a single outcome in isolation, has not addressed (Choudhary et al.,

2023; Bernhardt et al., 2024).

Second, we extend the intergenerational mobility literature to the context of forced displacement (Borjas, 1993; Card, DiNardo and Estes, 2000; Abramitzky et al., 2021a; Jensen and Manning, 2025). A central finding of this literature is that worse outcomes among migrants are largely explained by parental socioeconomic disadvantage rather than by migration status itself. We extend this question to a South-to-South forced displacement outflows, where there is genuine scope for a different conclusion. Unlike voluntary economic migrants, forcibly displaced people are more likely to have suffered trauma, asset losses, chronic poverty, and ongoing rights uncertainty that economic vulnerability by itself does not capture. We adapt the rank-rank regression framework of Chetty et al. (2014) and Jensen and Manning (2025) to ask whether developmental gaps between displaced and non-displaced children persist after accounting for household wealth or whether they can be fully attributed to socioeconomic disadvantage, and we exploit variation in the cause of displacement to assess whether conflict-induced and crisis-induced displacement differ in this respect. By focusing on child development outcomes rather than adult wages, our analysis speaks directly to the timing of policy intervention, given the substantially higher returns to investment in early life (Heckman and Mosso, 2014).

Finally, we contribute to the literature linking forced displacement to mental health outcomes for children in two distinct ways (Pluess, Brown and Panter-Brick, 2025). First, we document evidence for internally displaced persons and displacement in Latin America, which has received far less attention than refugee displacement in developed countries, the Middle East, or sub-Saharan Africa (Chen et al., 2019; Salami et al., 2020; Hazer and Gredebäck, 2023; Popham et al., 2022; McEwen et al., 2023). Second, by comparing Venezuelan forced migrants and Colombian IDPs within the same institutional setting in a middle income country where full mobility is allowed and displaced populations have legal support, we contribute direct evidence on both gaps and document patterns consistent with the intergenerational transmission of conflict-related trauma and its interactions with service access, building on prior evidence of how political violence shapes mental health and economic outcomes in Colombia (Ibáñez and Moya, 2010; Moya and Carter, 2019; Marroquín Rivera et al., 2020; Sánchez-Ariza, Cuartas and Moya, 2023).

## II THE COLOMBIAN DISPLACEMENT CONTEXT

Colombia hosts 9.8 percent of the forcibly displaced populations in the world, encompassing Venezuelan refugees displaced by an extreme economic and humanitarian crisis and internally displaced Colombians uprooted by decades of armed conflict. The Colombian government's policy response toward both groups ranks among the most comprehensive globally (Ibáñez, Moya and Velásquez, 2022; Moya and Rozo, 2025). Below we briefly describe each crisis and refer readers to Appendix A for additional institutional and contextual detail, including the scale and geographic distribution of Venezuelan migration to Colombia, the policy response and resulting rights and service access available to Venezuelan refugees, key differences in access to services such as education between Colombians and Venezuelans, and a brief overview of the geography and historical trends of internal displacement within Colombia.

II.A Refugees in Colombia: humanitarian crisis-driven displacement from Venezuela

Over the past decade, more than 7.7 million Venezuelans have been forced to flee their country due to service collapse and severe material deprivation (Cabra-Ruiz, Rozo and Sviatschi, 2024). The majority sought refuge in Latin American countries, with Colombia becoming the primary destination. By 2023, Colombia hosted approximately 2.8 million Venezuelan refugees, representing 5.8 percent of the country's population relative to the 2018 census (Migración Colombia, 2023). Venezuelan refugees settled primarily in border areas and major cities, including Bogotá, Medellín, Cúcuta, and Barranquilla.

Colombia's policy response expanded considerably in response to the massive inflows of Venezuelan refugees. Regularization programs, initially limited to better-educated refugees, broadened significantly in 2018 and 2021, culminating in the Permiso por Protección Temporal (PPT), which granted legal status to over 1.8 million refugees by 2023 (including anyone who had arrived to Colombia by 2021). Research shows that these programs improved refugees' labor market outcomes, income, and consumption (Ibáñez et al., 2024). Regardless of legal status, Venezuelan refugee children and adolescents are entitled to basic education and emergency healthcare. However, access to graduation credentials, full subsidized health insurance, and eligibility for social programs through Sisbén remains restricted to regularized refugees. $^{2}$

## II.B IDPs in Colombia: conflict-driven displacement from rural areas

Colombia hosts the largest population of internally displaced persons (IDPs) in the world. By 2025, the country had registered more than 8.8 million internally displaced individuals, equivalent to 18 percent of the national population according to the 2018 census (UN-HCR, 2025). Internal displacement has been driven primarily by a protracted armed conflict involving the Colombian government, nonstate armed groups including the FARC and ELN, and organized criminal organizations (de Memoria Histórica et al., 2021). Displacement intensified sharply over the last three decades, reaching a peak in 2003.

Colombia has developed one of the world's most comprehensive legal frameworks for internally displaced persons, combining victim recognition, land restitution, psychosocial support, and financial compensation (Ibáñez, Moya and Velásquez, 2022). $^{3}$ Evidence suggests these reparations programs improved housing, education, and health outcomes for recipients, though effects on labor market integration have been more limited (Guarin, Vélez and Posso, 2023). Despite persistent challenges in implementation capacity 

[中间内容因长度限制已省略]

.

Dustmann, Christian, Kristine Vasiljeva and Anna Piil Damm. 2019. “Refugee Migration and Electoral Outcomes.” The Review of Economic Studies 86(5):2035–2091.

Evans, David K. and Fei Yuan. 2022. “How Big Are Effect Sizes in International Education Studies?” Educational Evaluation and Policy Analysis 44(3):532–540.

Fazel, Mina, Ruth V. Reed, Catherine Panter-Brick and Alan Stein. 2012. “Mental health of displaced and refugee children resettled in high-income countries: risk and protective factors.” The Lancet 379(9812):266–282.

Foged, Mette and Giovanni Peri. 2016. “Immigrants’ Effect on Native Workers: New Analysis on Longitudinal Data.” American Economic Journal: Applied Economics 8(2):1–34.

Guarin, Arlen, Juliana Londono Vélez and Christian Posso. 2023. Reparations as Development?: Evidence from Victims of the Colombian Armed Conflict. Banco de la Republica Colombia.

Hazer, Livia and Gustaf Gredebäck. 2023. “The effects of war, displacement, and trauma on child development.” Humanities and Social Sciences Communications 10:909.

Heckman, James J. 2006. “Skill Formation and the Economics of Investing in Disadvantaged Children.” Science 312(5782):1900–1902.

Heckman, James J. and Stefano Mosso. 2014. “The Economics of Human Development and Social Mobility.” Annual Review of Economics 6(1):689–733.

Ibáñez, Ana María and Andrés Moya. 2010. “Vulnerability of victims of civil conflicts: empirical evidence for the displaced population in Colombia.” World Development 38(4):647–663.

Ibáñez, Ana María, Andrés Moya and Andrea Velásquez. 2022. “Promoting recovery and resilience for internally displaced persons: lessons from Colombia.” Oxford Review of Economic Policy 38(3):595–624.

Ibáñez, Ana María, Andrés Moya, María Adelaida Ortega, Sandra V Rozo and Maria José Urbina. 2022. “Life out of the Shadows.”

Ibáñez, Ana María, Andrés Moya, María Adelaida Ortega, Sandra V Rozo and Maria José Urbina. 2024. “Life out of the Shadows.”

Jensen, Mathias Fjællegaard and Alan Manning. 2025. “Background Matters, but Not Whether Parents Are Immigrants: Outcomes of Children Born in Denmark.” American Economic Journal: Applied Economics 17(3):347–379.

Lee, David S. 2005. “Training, wages, and sample selection: Estimating sharp bounds on treatment effects.”

Marroquín Rivera, Arturo, Carlos Javier Rincón Rodríguez, Andrea Padilla-Muñoz and Carlos Gómez-Restrepo. 2020. “Mental health in adolescents displaced by the armed conflict: findings from the Colombian national mental health survey.” Child and Adolescent Psychiatry and Mental Health 14:23.

McEwen, Fiona S., Claudinei E. Biazoli, Cassandra M. Popham et al. 2023. “Prevalence and predictors of mental health problems in refugee children living in informal settlements in Lebanon.” Nature Mental Health 1:135–144.

Medellín Cómo Vamos. 2024. “Integración socioeconómica de la población migrante venezolana en Medellín.” Informe de política. Proyecto realizado en alianza con Cuso International, Fundación Santo Domingo y las iniciativas Bogotá, Cali y Barranquilla Cómo Vamos.
URL: https://www.medellincomovamos.org

Michalopoulos, Stelios, Elie Murard, Elias Papaioannou and Seyhun Orcan Sakalli. 2025. Uprootedness, human capital, and skill transferability. Technical report National Bureau of Economic Research.

Migración Colombia. 2023. “Distribución de Migrantes Venezolanas(os) agosto 2023.”
Migración Colombia.
URL: https://www.migracioncolombia.gov.co/infografias-migracion-colombia/distribucion-demigrantes-agosto-2023

Moya, Andrés and Michael R. Carter. 2019. “Violence and the formation of hopelessness: evidence from internally displaced persons in Colombia.” World Development 113:100–115.

Moya, Andrés and Sandra V. Rozo. 2025. Refugees and Social Protection. In Handbook of Social Protection, ed. Rema Hanna and Benjamin Olken. MIT Press.

Pluess, Michael, Felicity L. Brown and Catherine Panter-Brick. 2025. “Supporting the mental health of forcibly displaced children.” Nature Reviews Psychology 4:370–387.

Popham, Cassandra M., Fiona S. McEwen, Elie Karam et al. 2022. “The dynamic nature of refugee children’s resilience: a cohort study of Syrian refugees in Lebanon.” Epidemiology and Psychiatric Sciences 31:e41.

Rozo, Sandra V. 2025. “Refugees and Other Forcibly Displaced Populations.” VoxDevLit 14(1).

Rubio-Codina, Marta, Orazio Attanasio, Costas Meghir, Natalia Varela and Sally Grantham-McGregor. 2015. “The Socioeconomic Gradient of Child Development: Cross-Sectional Evidence from Children 6–42 Months in Bogota.” Journal of Human Resources 50(2):464–483.

Salami, Bukola, Stella Iwuagwu, Oluwakemi Amodu et al. 2020. “The health of internally displaced children in sub-Saharan Africa: a scoping review.” BMJ Global Health 5(8):e002584.

Sánchez-Ariza, Juliana, Jorge Cuartas and Andrés Moya. 2023. The mental health of caregivers and young children in conflict-affected settings. In AEA Papers and Proceedings. Vol. 113 American Economic Association 2014 Broadway, Suite 305, Nashville, TN 37203 pp. 336–341.

Steinmayr, Andreas. 2021. “Contact versus Exposure: Refugee Presence and Voting for the Far Right.” Review of Economics and Statistics 103(2):310–327.

UNHCR. 2024a. Global Trends: Forced Displacement in 2023. Technical report United Nations High Commissioner for Refugees.
URL: https://www.unhcr.org/global-trends

UNHCR. 2024b. “Global Trends Report.” https://www.unhcr.org/us/global-trends. Accessed: 2026-04-26.

UNHCR. 2025. “It Is Time to Act Together: Durable Solutions for Internally Displaced Persons – February 2025.” https://www.unhcr.org/sites/default/files/2025-05/IDSF%20-%20Feb%202025.pdf. Accessed: YYYY-MM-DD.

Unidad para las Víctimas. 2024. "Registro Único de Víctimas."
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
