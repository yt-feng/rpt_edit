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
- 已识别机构名：`亚洲开发银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份亚洲开发银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
SOCIAL PROTECTION INDICATORS
OF COVERAGE AND EFFECTIVENESS
A TOOL FOR SOCIAL PROTECTION ASSESSMENT
JULY 2026

SOCIAL PROTECTION INDICATORS
OF COVERAGE AND EFFECTIVENESS
A TOOL FOR SOCIAL PROTECTION ASSESSMENT

JULY 2026

© 2026 Asian Development Bank

6 ADB Avenue, Mandaluyong City, 1550 Metro Manila, Philippines

Tel +63 2 8632 4444; Fax +63 2 8636 2444

www.adb.org

Some rights reserved. Published in 2026.

ISBN 978-92-9277-886-6 (print); 978-92-9277-887-3 (PDF); 978-92-9277-888-0 (ebook)

Publication Stock No. TCS260326-2

DOI: http://dx.doi.org/10.22617/TCS260326-2

The views expressed in this publication are those of the authors and do not necessarily reflect the views and policies of the Asian Development Bank (ADB) or its Board of Governors or the governments they represent.

ADB does not guarantee the accuracy of the data included in this publication and accepts no responsibility for any consequence of their use. The mention of specific companies or products of manufacturers does not imply that they are endorsed or recommended by ADB in preference to others of a similar nature that are not mentioned.

By making any designation of or reference to a particular territory or geographic area in this document, ADB does not intend to make any judgments as to the legal or other status of any territory or area.

This publication is available under the Creative Commons Attribution 3.0 IGO license (CC BY 3.0 IGO) https://creativecommons.org/licenses/by/3.0/igo/. By using the content of this publication, you agree to be bound by the terms of this license. For attribution, translations, adaptations, and permissions, please read the provisions and terms of use at https://www.adb.org/terms-use#openaccess.

This CC license does not apply to non-ADB copyright materials in this publication. If the material is attributed to another source, please contact the copyright owner or publisher of that source for permission to reproduce it. ADB cannot be held liable for any claims that arise as a result of your use of the material.

Please contact pubsmarketing@adb.org if you have questions or comments with respect to content, or if you wish to obtain copyright permission for your intended use that does not fall within these terms, or for permission to use the ADB logo.

Corrigenda to ADB publications may be found at http://www.adb.org/publications/corrigenda.

Cover design by Cleone Flores-Baradas.

TABLES, FIGURES, AND BOXES iv
FOREWORD v
ACKNOWLEDGMENTS vi
ABBREVIATIONS vii
EXECUTIVE SUMMARY viii
1 INTRODUCTION 1
2 SOCIAL PROTECTION AND ITS PROGRAMS 3
2.1 Defining Social Protection 3
2.2 The Classification of Social Protection Programs 4
3 THE SOCIAL PROTECTION INDICATORS OF COVERAGE AND EFFECTIVENESS FRAMEWORK OF SOCIAL PROTECTION ASSESSMENT 9
3.1 Inputs and Composition of Social Protection Expenditure 10
3.2 Outputs 10
3.3 Outcomes and Impacts 21
4 DATA REQUIREMENTS FOR SOCIAL PROTECTION INDICATORS OF COVERAGE AND EFFECTIVENESS 24
4.1 Policy Information and Documentation 24
4.2 Collection and Analysis of Administrative Data 31
4.3 The Analysis of Household Survey Data to Compute Outcome and Impact Indicators 40
5 REPORTING AND USE OF THE SOCIAL PROTECTION INDICATORS OF COVERAGE AND EFFECTIVENESS 45
5.1 Social Protection Country Report and Country Profile 45
5.2 Cross-Country Analysis and Regional Reports 46

# TABLES, FIGURES, AND BOXES

## TABLES

1 Typical Social Protection Programs by Addressed Needs 7
2 Intended Beneficiaries for Social Protection Needs 13
3 Social Protection Programs Classification by Category and Need 26
4 Basic Statistics for Computing Social Protection Indicators 32
5 Prevalence of Moderate/Severe Disability, Regional Estimates 35
6 Summary of Information Available from a Household Survey 41

## FIGURES

1 Classification of Social Protection Programs Based on Category, Need, and Other Main Characteristics 5
2 Areas of Need Requiring Social Protection 6
3 Social Protection Indicators of Coverage and Effectiveness Framework of Social Protection Assessment 9
4 Hypothetical Example of a Comprehensiveness Index of Social Protection in a Country 18

## BOXES

1 Analytical Value of the Social Protection Indicator: System-Level Comparison and Needs-Based Diagnostics 11
2 Summary of the Main Enhancements in the Social Protection Indicator 15
3 Example of the Analysis of the Impact of Social Protection on Poverty and Inequality 22

# FOREWORD

Social protection lies at the heart of inclusive and resilient development in Asia and the Pacific, but its effectiveness depends critically on the availability of reliable data and strong monitoring systems. In a region characterized by diverse and evolving risks—from demographic change to climate shocks—the ability to measure who is covered, how much support is provided, and the impact on people’s lives is essential for informed decision-making.

The Asian Development Bank (ADB) has therefore placed strengthening the evidence base for social protection at the center of its work. Since the early 2000s, ADB's Social Protection Indicator (SPI) initiative has played a pioneering role in measuring and tracking social protection performance, providing one of the first comparable frameworks to assess the scale, distribution, and adequacy of social protection expenditures across countries. The application of the SPI has also involved the systematic collection and consolidation of data across multiple areas of social protection. This process has resulted in a uniquely comprehensive and structured database for the region.

This publication represents the next step in that evolution. The Social Protection Indicators of Coverage and Effectiveness (SPICES) framework builds on the SPI by offering a more comprehensive and consistent approach to monitoring social protection systems. It brings together indicators of inputs, outputs, and outcomes, allowing countries to connect spending and program design with results such as coverage, adequacy, and impacts on poverty and inequality.

A key contribution of SPICES is its ability to generate more policy-relevant diagnostics. By organizing indicators around population needs—such as old age, children, disability, unemployment, poverty, and health—it provides a clearer picture of how resources are distributed and where gaps remain. This helps policymakers move from aggregate spending analysis to a more targeted understanding of who benefits and how effectively different needs are addressed.

SPICES is designed as a flexible framework and practical methodology that countries can adapt to their specific contexts and priorities. Developing member countries can apply the framework in ways that best suit their data availability, institutional arrangements, and policy priorities. It can be adapted and extended, for example, by adding new dimensions, introducing further disaggregation, or developing deeper narrative analysis around specific aspects of social protection.

This work reflects ADB's continued commitment to advancing practical analytical tools and knowledge solutions for its developing member countries. By strengthening the measurement and monitoring of social protection, the SPICES framework is expected to enhance evidence-based decision-making and policy dialogue across the region. As a flexible tool and methodology, it will support countries in generating better data, improving performance monitoring, and ultimately achieving more effective and inclusive social protection outcomes for their populations.

Albert Smith

Albert Francis Park

Chief Economist and Director General

Economic Research and Development Impact Department

Asian Development Bank

# ACKNOWLEDGMENTS

This report was prepared under the overall guidance of Babken Babajanian, senior social development specialist (Social Protection), Human and Social Development Sector Office, Sectors Department 3 (SD3-HSD), Asian Development Bank (ADB), who provided technical leadership and direction. This report is part of the implementation of the regional technical assistance for Developing Inclusive and Resilient Social Protection Systems in Asia and the Pacific.

The Social Protection Indicators of Coverage and Effectiveness methodology, which represents a major revision of the previous approach, was developed by consultants Ludovico Carraro (lead author), with technical assistance from Flordeliza Huelgas. Lydia Domingo, senior social development officer (Social Protection), SD3-HSD, supported the publication process through technical facilitation and served as the focal point for the technical assistance that underpinned this work. Imelda Marquez, former associate operations officer, SD3-HSD, provided operational support to the team. The development process benefited from early support provided by Oleksiy Ivaschenko, senior social protection and jobs specialist, SD3-HSD.

The team benefited from the guidance of Wendy Walker, former director (Social Development), SD3-HSD, and Shamit Chakravarti, director (Pacific and Social Protection), SD3-HSD, as well as from inputs provided by Eduardo Banzon, director (Health), SD3-HSD, and Nishant Jain, senior health specialist, SD3-HSD, on positioning the health sector dimensions of the methodology.

The authors are particularly grateful to peer reviewers Arturo Martinez, Jr., senior statistician, and Minhaj Mahmud, senior economist, both from the Economic Research and Development Impact Department, as well as external peer reviewers Keetie Roelen and Sebastian Silva Leander, whose comments and feedback significantly strengthened the methodology.

Additional inputs were received from HSD peer reviewers, including Louise Macsorley, senior operations specialist, Pacific Department; and Gohar Tadevosyan, senior social development specialist, Anand Ramesh Kumar, social development specialist (Social Protection), and Karin Schelzig, former director (Southeast Asia), SD3-HSD.

## ABBREVIATIONS

ADB Asian Development Bank

GDP gross domestic product

GNI gross national income

ILO International Labour Organization

SDG Sustainable Development Goal

SPI Social Protection Indicator

SPICES Social Protection Indicators of Coverage and Effectiveness

# EXECUTIVE SUMMARY

The Social Protection Indicators of Coverage and Effectiveness (SPICES) is the Asian Development Bank (ADB) standardized framework for assessing the status of a country social protection system.

SPICES provides a practical, country-oriented methodology that (i) maps social protection programs to needs; (ii) quantifies the level of support and coverage of different population subgroups, highlighting gaps or the comprehensiveness of the system; and (iii) links such outputs to their effects on inclusion and poverty reduction.

Indicators in SPICES are organized into three levels: inputs, outputs, and outcomes/impacts. The main inputs are the level and structure of government expenditure on social protection, whereas outputs consider the average expenditure per beneficiary and coverage. These dimensions are estimated using different measures and disaggregated by needs: old age, children/family, disability, unemployment/underemployment, poverty/vulnerability, and health. Outcomes indicators are obtained from household survey analysis and primarily focus on the simulated impact of social protection on reducing poverty and inequality.

The SPICES framework and indicators are designed to be intuitive for policymakers, comparable across countries and over time, and immediately usable for diagnostics and dialogue.

Many institutions provide data on social protection, including the International Labour Organization's Statistics on Social Protection and the World Bank's ASPIRE database, and the Sustainable Development Goals (SDGs) have catalyzed greater data availability. Nevertheless, significant regional gaps remain in the consistency of social protection measures across countries in Asia and the Pacific.

ADB's Social Protection Indicator (SPI) initiative—launched in 2004 and published for Asia in 2008—was one of the first attempts to systematically address these measurement challenges. This exercise predated the International Labour Organization's first World Social Protection Report (2010) and the World Bank's 2014 Safety Net Report. SPICES builds on and expands this earlier analytical effort.

The SPICES framework aims to provide such consistency. Without preset judgments about the type and composition of social protection instruments, it takes these into account as inputs and focuses on their outputs and outcomes. In doing so, SPICES extends the conceptual foundations of the original SPI exercise and broadens the analysis to systematically assess needs, outputs, and outcomes. Methodologically, SPICES represents a shift from the previous emphasis on disaggregating social protection by program category—social insurance, social assistance, and active labor market programs—toward an assessment organized around the types of needs that social protection addresses.

One of the key output indicators within the SPICES framework is the SPI. It is a specific quantitative indicator that captures the level of expenditure per intended beneficiary. It is derived by multiplying two components: the average expenditure per beneficiary and the potential coverage of intended beneficiaries.

Importantly, the SPI is disaggregated by needs. The SPI provides a clearer and more comparable measure of social protection performance than simple spending-to-gross domestic product ratios by showing the average support delivered per intended beneficiary, and—when disaggregated—revealing how resources are distributed across distinct needs and population groups.

Other important output indicators include a comprehensiveness index, which assesses the extent to which social protection programs address in a balanced way the different needs of the population, the focus on vulnerable groups, and the level of protection against risks.

The SPICES approach has the following strengths:

\- The development of a comprehensive framework for the assessment of social protection, looking at a set of indicators organized into three pillars: inputs, outputs, and outcomes/impacts of social protection.

\- An embedding of the SPI indicator within the SPICES output pillar, and a methodological revision so that the SPI can be disaggregated across needs for social protection interventions. This should provide relevant results for policymakers.

\- The calculation of a specific indicator of comprehensiveness of social protection, or to what extent social protection is developed to address social protection needs, both through visual representations and an actual numerical indicator.

• A rigorous assessment of health expenditure in reducing health-related financial risks.

\- An assessment of countries' development of shock-responsive social protection as part of the SPICES output pillar.

\- Whenever available and accessible, the use of household survey microdata to provide information on potential impacts. This constitutes the impact pillar and provides simulated effects of social protection on poverty and inequality, as well as measures of the reduced effect of risks.

This document describes the SPICES methodology and provides practical guidelines for conducting the SPICES assessment: identifying relevant social protection programs, collecting administrative data on expenditure and beneficiaries, and analyzing household survey data to compute outcome indicators.

The SPICES analysis can be used to produce country reports assessing the social protection system and short country profiles. It is also expected that once a set of country assessments is completed, the use of a common framework will enable regional analysis of the status of social protection in Asia and the Pacific, as well as ad hoc analysis of specific social protection issues emerging from cross-country comparisons.

The inclusion of social protection in the Sustainable Development Goals (SDGs) has been a substantial incentive for improving social protection statistics, including in Asia and the Pacific. However, gaps remain: There is a lack of consistent assessments and an emphasis on assessing social protection through specific programs and their delivery rather than focusing on needs.

The difficulty stems from the diverse level of development of social protection across countries in Asia and the Pacific, as well as different paradigms and understanding of social protection.

The development of the Social Protection Indicators of Coverage and Effectiveness (SPICES) aims to address gaps and inconsistencies by creating an intuitive, effective framework that looks at inputs, outputs, and outcomes of social protection. It examines expenditure on social protection, its composition as inputs, and then focuses on its outputs and impacts.

Such a framework allows the analyst to compare countries at different stages of development that adopt different instruments, focusing on the ultimate results and goals of social protection. The development of a consistent framework of assessment supports dialogue and comparisons across countries, creates learning opportunities, and provides a powerful diagnostic tool for each country's social protection system.

SPICES builds on 2 decades of work by the Asian Development Bank (ADB) with the Social Protection Indicator (SPI). While the earlier SPI provided a single, regionally comparable measure, SPICES embeds the revised SPI within its output pillar and extends the assessment to include inputs and outcomes, using a needs-based lens and clearer signposting for policy audiences. The SPI enhances cross-country and over-time analysis by capturing the average support provided per intended beneficiary relative to gross domestic product (GDP) per capita, and—when disaggregated—shows how resources are distributed across distinct needs and population groups.

ADB—through the SPI—has been a long-standing pioneer in assessing social protection development across Asia and the Pacific. The SPI origins date to 2004, when the social protection system of six Asian countries (Bangladesh, Indonesia, Mongolia, Nepal, Pakistan, and Viet Nam) was the focus of in-depth studies that became the basis of the creation of a social protection index $^{1}$ for Asia and the Pacific countries. $^{2}$

Subsequently, the approach was revised and improved, and since then, efforts have focused on improving data quality and analyzing different aspects of social protection, such as the inclusion of people with disabilities or the social protection response to the coronavirus disease (COVID-19) pandemic. $^{3}$

The development of

[中间内容因长度限制已省略]

lude estimates of the percentages of the population in different groups of interest, as well as key indicators describing the level of the country's development.

The section on input indicators should provide information on overall social protection expenditure and compare it with previous social protection assessments, with a breakdown of the share of different categories of social protection expenditure. It should also describe the most important social protection programs, provide a description of health protection, and provide detailed information on at least five main social protection programs.

A diagram showing the main agencies involved in social protection in the country would also be very useful, highlighting each agency's specific responsibilities. It would also be important to discuss the main changes in program design that have occurred in recent years and, possibly, institutional changes.

The output indicators section needs to present the following: (i) results on the SPI, disaggregating potential coverage (breadth) and average expenditure (depth) by need (excluding health); (ii) the relative focus of social protection expenditure on different vulnerable groups; (iii) the SPI including health and the estimate of population health coverage, based on social health insurance or alternative measures; and (iv) the social protection comprehensiveness measure/spider web. When available, potential coverage estimates from the SPI should be complemented by those obtained from household surveys, including information on population coverage for essential health services based on tracer interventions (SDG indicator 3.8.1) and information on trends in out-of-pocket health expenditure. A separate subsection should discuss social insurance protection among the employed population and whether the country has developed a shock-responsive social protection system.

Finally, the outcome section should summarize the results of the analysis of household survey data and, whenever available (at least for key indicators), provide information on how estimates have changed. The indicators could be organized into three subsections: (i) simulated impact of social protection on poverty and inequality, including for relevant subgroups of the population; (ii) impact on reduced risks; and (iii) comparison levels of participation and well-being indicators between vulnerable groups and the rest of the population.

From the country report, a more streamlined country profile could also be written, capturing only the key information, focusing on indicators, and referring to the country report for explanations and the more in-depth analysis.

The country analysis is independent of regional reports, which has the advantage that, as soon as a regional report is completed, data for the specific country and the related reports can be made available. This should ensure that information is more up to date and relevant for potential users.

## 5.2 Cross-Country Analysis and Regional Reports

Calculating SPICES indicators across a range of countries offers the opportunity to conduct subregional or regional comparisons, as well as comparative benchmarking across groups of countries. At the same time, SPICES supports thematic analysis, including needs-based assessments, analysis of coverage and effectiveness, distributional perspectives across population groups, and exploration of relationships between key indicators. Together, these applications allow SPICES to be used flexibly for descriptive and exploratory analysis to inform policy dialogue at national and regional levels.

There is a considerable advantage in conducting cross-country analysis when methodologies and frameworks are the same across countries. Therefore, once a certain number of country reports are completed, there is scope to compare and identify emerging regional patterns and more general lessons that can be drawn from the data. For example, it might be relevant to compare countries with similar levels of GDP per capita but very different social protection expenditure levels or compositions, and to assess the consequences on key outcome indicators.

When data allow, it will be possible to assess the relationships between social protection expenditure and poverty and inequality levels, and between social protection expenditure and population coverage, the extent of coverage, and the size of average expenditure.

Finally, if some countries achieve very good results in addressing specific social protection needs, this could trigger an in-depth analysis that provides lessons for other countries.

## Social Protection Indicators of Coverage and Effectiveness A Tool for Social Protection Assessment

The Social Protection Indicators of Coverage and Effectiveness (SPICES) is a methodology developed by the Asian Development Bank to assess social protection systems. SPICES provides a practical approach that links inputs, outputs, and outcomes to evaluate system performance. By organizing analysis around population needs—such as old age, disability, unemployment, and poverty—the SPICES framework enables policy-relevant diagnostics of coverage, adequacy, and impact on poverty and inequality, thereby supporting evidence-based decision-making.

## About the Asian Development Bank

ADB is a leading multilateral development bank supporting inclusive, resilient, and sustainable growth across Asia and the Pacific. Working with its members and partners to solve complex challenges together, ADB harnesses innovative financial tools and strategic partnerships to transform lives, build quality infrastructure, and safeguard our planet. Founded in 1966, ADB is owned by 69 members—50 from the region.
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
