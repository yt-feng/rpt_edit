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
# How to Build a Reader

# Evidence from a Scalable Literacy Intervention in Ghana

Erik T. J. Andersen

Simon Graffy

Jason T. Kerwin

Monica Lambon-Quayefio

Development Economics
Development Research Group
July 2026

Policy Research Working Paper 11433

## Abstract

Addressing the massive test score gaps between rich and poor countries will require programs that are both high-impact and scalable. This study uses the results of a randomized controlled trial in low-fee private schools in Ghana to study a program that meets both needs. The Tools for Foundational Learning Improvement program increased test scores by 0.5 standard deviation after just nine months of intervention. A machine learning method decomposes the effects by predicted test scores if the students did not receive the treatment, and the findings show that the gains were larger for weaker students. Moreover, the program's impacts scale roughly linearly with time compared to a shorter-term, smaller-scale pilot randomized controlled trial. The program's developers used generative artificial intelligence to accelerate lesson plan development and adaptation to new settings. An observational pilot test of this adaptation in Uganda yielded comparable results to those of this study's randomized controlled trial. The study developed a model in which basic skills constrain the development of advanced skills, which predicts the pattern of effects observed across early reading capabilities, and it makes forecasts about the future impacts of the program as it continues into second grade.

# How to Build a Reader: Evidence from a Scalable Literacy Intervention in Ghana

Erik T. J. Andersen, Simon Graffy, Jason T. Kerwin, and Monica Lambon-Quayefio\*

Authorized for distribution by Sergio Schmukler, Lead Economist, Development Research Group, World Bank Group

JEL Codes: I21, I25, O15

Keywords: Economics of Education, The Learning Crisis, Structured Pedagogy, Differentiated Instruction, Human Capital, Generative AI, Development Economics

The learning gaps between the world's poorest and richest countries are staggering. In 2021, South African fourth-graders scored 2.99 standard deviations (SDs) lower on reading than their counterparts in Singapore (PIRLS 2021). This gap is almost four times as large as the black-white test score gap for fourth graders in the United States (NAEP 2022). Indeed, these gaps are so massive that it is rare to even measure the richest and poorest countries using the same exam: South Africa is the only country in Sub-Saharan Africa that participated in the PIRLS, and it is one of the richest countries on the continent. A 3-SD gap between the poorest and richest countries is therefore likely to be a lower bound.

Addressing these gaps will require changes that are far more ambitious than the ones that governments have typically tried in the past. The average education program raises reading test scores by just 0.20 SD (Evans and Yuan 2022); we would have to repeat such a program more than 15 times to bring African reading scores up to rich-country levels. Whether these gains are cost-effective in dollar terms matters very little, as it is logistically impossible to actually run one of these programs over a dozen times.

We present the initial results from a promising approach to this challenge. Our data comes from a randomized trial we conducted with the education non-profit Inspiring Teachers, in which we evaluated their program, Tools for Foundational Learning Improvement (TFLI). TFLI is a smartphone-enhanced structured pedagogy program where teachers are given upfront training on the science of reading, and equipped with high-quality, semi-scripted lesson plans linked with student workbooks, to run daily literacy lessons and given coaching. The program incorporates a digital layer; teachers and coaches assess children's literacy skills and are provided with integrated student tracking, coaching management tools, and training videos through a mobile app called SmartCoach. We study the effects of the program's literacy model, Inspiring Reading, on first-grade students in low-fee private schools in the Central Region of Ghana. We randomly assigned 80 schools to either the Inspiring Reading program or a control group during the 2024-25 school year, and measured outcomes using end-of-year Early Grade Reading Assessments (EGRAs). We complement the data from the assessments with the survey data. The Inspiring Reading program will continue for the same cohort of students for two additional years, until the end of grade 3.

The program causes large increases in student learning: our pre-specified primary outcome, overall EGRA reading scores, increases by 0.504 SDs ( $p = 0.011$ ) which is the equivalent of more than two years of progress under the status quo. This puts TFLI at the $91^{\text{st}}$ percentile of all reading interventions within the first of what will be three years of the program. The effects on individual components of the reading score are consistent with the program's theory of change. The largest effects are on mapping letters to sounds ( $d = 0.764$ , $p < 0.001$ ) and phonemic awareness ( $d = 0.712$ , $p < 0.001$ ), which are the key skills targeted by the program in grade 1. The impacts on oral reading fluency and reading comprehension are smaller and do not reach conventional levels of statistical significance, although they are quite large relative to typical impacts in the literature ( $d > 0.2$ ). These are downstream skills that the program is building toward, and where effects are more likely as students progress through the program in grades 2-3.

We present extensive evidence that these impacts are real and not artifacts of our research design. We pre-specified a single primary outcome and the exact data analysis that we would run, so the p-value for that main test can be interpreted literally. Our findings are also robust to a wide range of robustness checks that vary the controls and address the small level of school-level non-compliance with treatment assignments, with point estimates ranging from 0.44 to 0.52 SDs. $^{1}$ The attrition rate was just 20%, nearly identical across study arms, and not differentially correlated with covariates by treatment status; we nevertheless compute Lee bounds and find a treatment effect range of 0.40 to 0.54 SDs, with both ends being statistically significant. Our exam scores come from an internationally standardized test (the Early Grade Reading Assessment); the NGO was blinded to the content of the test until the exams began, and the tests were administered by external contractors. We ran a separate experiment to estimate potential demand effects, randomizing whether each student was tested by an enumerator who was from the teaching profession. Assessor type matters for average scores but has no differential effects by study arm.

To understand how TFLI achieved such large effects so quickly, we develop a model of skill formation in which basic skills constrain the development of advanced skills. The model predicts that it is optimal to differentiate instruction: we should teach the basics to children with lower skills and advanced materials to children who are higher-skilled. It also predicts that high teaching quality and targeted instruction are complements, so that programs that combine the two approaches (structured pedagogy and targeted instruction) will have particularly large impact. TFLI operationalizes this approach, providing scripted lesson plans and workbooks (to improve teaching quality) along with regularly-scheduled targeted instruction (for differentiation of instruction). Moreover, the SmartCoach app helps to enhance both components, easing the management of program adherence for coaches and also the process of assessment and differentiation for teachers.

Consistent with the model, we see the largest impacts on the most basic skills: letter sound knowledge and initial sound identification. More advanced skills progress by less. We also see stark variation in the effects of the program across the distribution of test scores. In particular, there are large and statistically significant reductions in the fraction of students who cannot recognize words or read any words in a passage, both of which fall by over 40%. Impacts at the higher end are smaller, which is consistent with the program building basic skills more at this grade level. The effects also appear to be larger for male students; control-group girls are ahead by 0.26 SDs, and the treatment closes two-thirds of this gender gap. More broadly, the program appears to be most beneficial for weaker students, consistent with its design focus on supporting teachers in using assessment-informed instruction and in-classroom remediation.

We cannot decompose our treatment effects by students' initial test scores because there were no baseline exams. Instead, we use machine learning methods to predict the endline test scores for the control group, and then generate these predictions for the treatment group as well. We test for treatment effect heterogeneity by these counterfactual untreated outcomes. We see consistent increases across the ability distribution for most skills, with stronger treatment effects for initial sound identification among students we predict would perform worse without treatment. There are also distinctly lower treatment effects for the strongest students on the reading speed tasks, as well as for our overall reading score index. This and our other analyses are consistent with the prediction that weaker students and weaker skills are targeted more by the intervention.

We see evidence for a number of potential mechanisms for the treatment effects. A pre-specified index of teaching quality improves by nearly 2 SDs, with notable gains in key phonics activities such as having learners say the same correct sounds as the teacher and blending sounds to make words. Classroom observations also reveal increases in the teacher moving around the room and in student engagement with the workbooks. Student self-perceptions appear to improve, with statistically significant reductions in students thinking they are at the bottom of the class. Students are also more likely to practice reading at home, in line with previous evidence on shifting beliefs about relative performance (Dizon Ross 2020).

To further test these mechanisms we run an A/B test to examine how further enhancements to teaching quality affect test scores. A/B tests are rapid randomized experiments that allow organizations to improve their operations (Angrist, Cullen, and Magat 2025). We tested an intervention in which school leaders (principals) were trained to provide additional coaching to teachers on their implementation of the program, with the goal of improving teaching quality. Using a lower bar for statistical significance (which is standard in A/B testing (Azevedo et al., 2020)), we see evidence of gains in quality from this intervention. The effects on learning are not yet distinguishable from zero, but based on these findings Inspiring Teachers is continuing the intervention in the 2025-26 school year. Moreover, the impacts on learning are quantitatively consistent with our model: we see larger relative effects on more-advanced skills, with the impact on reading speed being $70\%$ of the main treatment effect, while the impact on letter sound recognition is just $10\%$ of the main effect.

Our model makes specific predictions about the program impacts we expect to see in second grade, which we will test in future data collection for the project. Specifically, we expect to see larger gains in more advanced skills now that students have developed the basic reading skills that constrain them. We also expect to see higher gains in advanced skills for students who are further up the skill distribution at the end of grade one, and lower gains for those who are at lower levels.

The impressive gains achieved by TFLI have important policy implications because the intervention is scalable both over time and across space. We conducted a previous small-scale pilot RCT during the 2023-24 school year; the intervention ran in four randomly-assigned treatment schools that year for just four months. Comparing those treatment schools to four randomized control schools, we see gains of 0.25 SDs, with the impacts distinguishable from zero despite the small sample size. Moreover, the actual RCT results in 2024-25 are very close to what we would have extrapolated from this pilot based on the additional time spent in the program: the program ran for 2.25 times as long and had effects that were nearly 2.25 times larger. This suggests that continued exposure to the program may raise test scores almost linearly, so we can expect gains of over 1 SD by the time the program finishes at the end of grade three.

The intervention is also designed to be scaled across space, not just within Ghana but also across Africa. Within Ghana, Inspiring Teachers is already scaling up the program to more of the country and to different kinds of school. It is currently running in 139 schools in the 2025-26 academic year, including in 80 government schools. The organization has been invited to expand to 400 government schools and 100 low-fee private schools in 2026-27, and is collaborating with the national and regional offices of the Ghana Education Service to roll out TFLI in all 1,638 government schools in the Central Region by 2029-30. This expansion is slated to be highly cost-effective: the current marginal cost of the program is \$48 per student, and so the cost per 1-SD gain is \$96, which already makes the program competitive with existing interventions. By 2029, Inspiring Teachers' budget model predicts the cost will drop to \$6 per student, which would make it extremely cost-effective if its current effectiveness can be sustained.

Scaling TFLI across Africa more broadly will require adapting the materials to other local contexts, education systems, and languages of instruction. It has two key advantages on that front. First, TFLI is currently English-language-first, which means that it can in principle be used across all of Anglophone Africa. It works even though English is not the native language of our study sample: TFLI has achieved significant gains in learning despite just 15% of our sample speaking English at home. This means it can serve as a complement to existing mother-tongue-first instruction programs. Second, TFLI's lesson plan developers use a component-based design system (where lessons are assembled from a common pool of adaptable components) and generative AI tools to accelerate lesson guide and workbook development. This allows Inspiring Teachers to efficiently leverage a highly scarce talent pool—highly-skilled instructional designers, which are rare not just in Africa but around the

world.

The organization is already using this tool to adapt the program to Uganda. They ran a preliminary pilot test of the program in Kanungu District during the 2025 school year, covering grade 1 classrooms. The pilot was not randomized, but they did post-intervention tests in both the program schools and in similar nearby schools. A regression-adjusted comparison of the mean test scores, following our specification for the main RCT, yields a difference of 0.514 SDs. These results suggest that the genAI-assisted curriculum adaptation approach can help the program scale to other countries with different early-grade reading curricula. Inspiring Teachers is in talks to do this in Zambia. TFLI has the potential to substantially narrow the learning gap between schools in Africa and those in the developed world.

Our results make contributions to four strands of the economics literature. First, we provide additional evidence that it is possible to drastically improve test-scores in learning-impoverished contexts. Previous work has shown that two types of intervention are capable of achieving impacts larger than half a standard deviation. The first is targeted instruction, which has proven benefits in a number of contexts (Duflo, Dupas, and Kremer 2011, Banerjee et al. 2007, Muralidharan, Singh, and Ganimian 2019) including in Ghana (Beg, Fitzpatrick, and Lucas 2023) and has been successfully scaled up (Banerjee et al. 2017). Angrist and Meager (2023) argue that targeted instruction has impacts of 0.9 SDs when implemented with high fidelity; fidelity (and, concomitantly, impacts) vary substantially across studies. The second is structured pedagogy, which has achieved large impacts in both local-level randomized trials (Piper et al. 2018c, Eble et al. 2021, Buhl-Wiggers et al. 2024) and at national scale (Piper et al. 2018a). It is also a key component of the extremely high-impact programs studied in Gray-Lobe et al. (2022) and Fazzio et al. 2021. We contribute to these existing findings by showing that large gains are achievable after just one grade of exposure, and using English-first instruction, despite most students speaking a different language at home.

Second, we show that targeted instruction and structured pedagogy can be combined successfully. While these two types of intervention are proven to have large impacts on their own, they have rarely been combined. Existing work on combining the two approaches uses observational data to show large impacts that are plausibly causal (Ibrahim et al. 2024). We build on this earlier work by randomizing the roll-out of an intervention that combines structured pedagogy and differentiated instruction, and we show that this combination works in a totally different context. These findings are part of a literature that studies complementarities between educational interventions (Mbiti et al. 2019, Kerwin and Thornton 2021, List, Livingston, and Neckermann 2011). We do not explicitly randomize the two aspects of the program, but our results, complemented by our theoretical framework, suggest that the two aspects of the intervention are complementary rather than substitutes.

Third, we contribute to the theory of how differentiated instruction works. This is part of a broader literature about dynamic complementarities (Cunha and Heckman 2007, Heckman et al. 2026). That literature has the feature that skills beget skills, sometimes called the “Matthew Effect”. We build on this idea to develop a model in which basic skills constrain the development of more-advanced skills, which is a key assumption underlying the literature on “teaching at the right level”, or TaRL (see e.g. Banerjee et al. (2017)). We build on this literature in two ways. First, we link it to work on

[中间内容因长度限制已省略]

/td><td>ten</td><td>sent</td><td>bed</td></tr><tr><td colspan="4">He gets ten pens.</td></tr></table>

Now, read the words and sentence again quietly in your pairs.

Move around the room listening to pairs reading.

## 3 Reading

## 15 min

For our reading today, we are going to practise blending and review our sight words.

## Blending Drill

8 min

Turn to page 100 in your workbook. Put your finger on the first word chain. Let's read together...

![](images/971147bea87cca3c3c47de0d02622b35ea2bd26b808c2ec9c03fe9872c9bf690.jpg)

## Word Chains

den > hen > ten > pen

fin > fig > fog > frog

Ted > bed > bend > send

Next, I would like you to read them through again quietly in your pairs...

![](images/35021f8ed52c3e406f17de87fd3bab2b621ece1fa6408a5e4a9241bf4fb0ff35.jpg)

## Review Sight Words

7 min

![](images/65cc809648e788ada021eeb0abf98c432dfc9e5115c874c27f61d68ef1a909e8.jpg)

Let's practise reading the new sight words we learnt yesterday and remind ourselves of how they sound, and what they mean...

![](images/29502257c0fd4cb5c9b2f37e05d064fa4738b065d45eea34b5605879ec17fbd7.jpg)

Recent Sight Words

she

of

❤️

Turn to page 100 in your workbook.

We are going to read through some sight words we've learnt recently together.

![](images/e49506471e27a2332e384b56b37f172a5c352a1e09d3c86622b9a74387abc4f4.jpg)

## Sight Word Practice

<table><tr><td>so</td><td>of</td><td>by</td><td>on</td></tr><tr><td>for</td><td>can</td><td>not</td><td>she</td></tr></table>

Now I want you to read them again, quietly with your partner.

## Writing

15 min

For our writing session today we are going to learn about full stops.

![](images/49af2fd1934ecb8103107e34de5dc8a9ac6abcd0732a1d1137f91c4d78182af6.jpg)

## Teach Full Stops

5 min

We have learnt that sentences start with a capital letter.

Today we will learn what sentences end with.

![](images/d1d3618488743e0d15c960cfb0b101eac2f2f82a6fb37f40afaf563713e157cf.jpg)

Show & explain a full stop

I pat the mat.

![](images/6d0da88b1569839a48a51f01a0683491da77e246e86db586924dd14bef22736c.jpg)

I have circled the full stop. It is at the end of my sentence.

Full stops are very important. They tell us when a sentence has ended.

This helps to separate our sentences so that we can understand them.

![](images/e300e7e74f98e054ce1999d06df2950cc790c65e33a2e69be7f30730a32097f4.jpg)

## Shared Writing Practice

5 min

> Write out the sentences without full stops.

![](images/73db09c8f84b71544b36317be1593625b51bde8a2fa11b340f3ab52a8c3f3648.jpg)

Example (without full stops)

Sam is a man Pat is an ant

Let's read these sentences together.

It is hard to understand the sentences because the full stop is missing.

I know we start a sentence with a capital letter so my full stop must go before it.

Example (with full stops)

Sam is a man. Pat is an ant.

Let's read the sentences again and add the full stops together. "Sam is a man, Pat is an ant"
Where do the full stops need to go?

Yes, that's right. One after man. And another at the end, after ant. Why is that?

<table><tr><td colspan="2">Lesson Recap 2 min</td></tr><tr><td colspan="2">&gt; Ask the class these questions to recap the lesson.</td></tr><tr><td colspan="2">Let&#x27;s review what we&#x27;ve learnt today...</td></tr><tr><td>Oral</td><td>Have you seen someone building a house? What did you see?</td></tr><tr><td>Phonics</td><td>Is there an /e/ sound in the word &#x27;net&#x27;?</td></tr><tr><td>Reading</td><td>We read a story. What happened in the village?</td></tr><tr><td>Writing</td><td>How do you know a sentence is finished?</td></tr></table>

## 4.3 Independent Writing

Now, turn to page 101 in your workbook.

I want you to read the text and circle all the full stops you can see.

Check all learners are circling the full stops.

Now, look at the next text in your workbook.

![](images/6461decf2669d8729c4d911ce267d2a99daf62fa7b57f297ac4eeea33abddbf5.jpg)

What do you think is missing?

That's right, full stops.

I want you to spend 3 minutes adding in all the missing full stops.

Use the capital letters to help you.

√ End of lesson

## Sam and the Dog

Sam is on a mat

A dog is on a log Dad pats the dog

The dog did a spin Sam pats dog

Dad and Sam sit on the mat

Check all learners are circling the full stops.

What do you notice comes after a full stop?

# Week 7 | Day 2 Our Community

![](images/a3efc642822bc5dc1268ae22aa89a8bfbe46cd8786adaf60e53bcd6f5c7defae.jpg)

# Activities in our Community

## Oral Language

1. Talk about the new vocabulary:

![](images/cfbd1011b308c7f0dc718695f89571d3577d3557d6678627b13d175c1433fdc8.jpg)  
building

![](images/37902a914952a24f2720bc5d64fd014571e3faa173bf5fe7f071edc30f70b6e6.jpg)  
trading

![](images/1b3d4f42656206cb65385a15889b5f665aedaa1e454f9a1d8ab38ddb8d3c7990.jpg)  
teaching  
2. Read Aloud - Talk about the picture:

![](images/381137c2301f4b234cf7ecd96984cabe034b4a2dc24a7d06593fa7b460d5ab7d.jpg)

# Figure I6 Workbook Example Page 2

## Phonics

1. Write the letter sound you hear:

2. Write e:

3. Read words with e:

<table><tr><td>bet</td><td>ten</td><td>sent</td><td>bed</td></tr></table>

He gets ten pens.

## Reading

1. Read the word chains:

den > hen > ten > pen

fin > fig > fog > frog

Ted > bed > bend > send

2. Read recent Sight Words:

<table><tr><td>so</td><td>of</td><td>by</td><td>on</td></tr><tr><td>for</td><td>can</td><td>not</td><td>she</td></tr></table>

## Writing

1. Circle the full stops:

Sam is a man. Pat is an ant.

"It is my pan. It is a tin pan."

Pat is in the pan . "Spin me," said Pat .

Sam spins Pat in the pan .

2. Add the missing full stops:

Sam is on a mat

A dog is on a log Dad pats the dog

The dog did a spin Sam pats dog

Dad and Sam sit on the mat
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
