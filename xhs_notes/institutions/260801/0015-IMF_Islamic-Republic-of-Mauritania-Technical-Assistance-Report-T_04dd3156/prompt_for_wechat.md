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
- 已识别机构名：`IMF`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份IMF研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
REPORT

ISLAMIC REPUBLIC OF

MAURITANIA

Technical Assistance in Public Debt

Projections and Analysis

MAY 2026

Prepared by

Marie Pierre Aquino Coste, Ha Minh Nguyen, and Naomitsu Yashiro

Authoring Department:

Institute for Capacity Development, IMF

©2026 International Monetary Fund

## Disclaimer

The contents of this report constitute technical advice provided by the staff of the International Monetary Fund (IMF) to the authorities of Mauritania (the "TA recipient") in response to their request for technical assistance. This report (in whole or in part) or summaries thereof may be disclosed by the IMF to IMF Executive Directors and members of their staff, as well as to other agencies or instrumentalities of the TA recipient, and upon their request, to World Bank staff and other technical assistance providers and donors with legitimate interest, including the members of the AFRITAC West Steering Committee, unless the TA recipient specifically objects to such disclosure (see Operational Guidelines for the Dissemination of Technical Assistance Information: http://www.imf.org/external/np/pp/eng/2013/061013.pdf). Publication or Disclosure of this report (in whole or in part) or summaries thereof to parties outside the IMF other than agencies or instrumentalities of the TA recipient, World Bank staff, other technical assistance providers and donors with legitimate interest, including members of the AFRITAC West Steering Committee, requires the explicit consent of the TA recipient and the IMF's Institute for Capacity Development.

The analysis and policy considerations expressed in this report are those of the IMF's Institute for Capacity Development (ICD) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

This technical assistance was provided with financial support from the Government of Japan.

International Monetary Fund, IMF Publications.
B.P. 92780, Washington, DC 20090, U.S.A.
Tel. +(1) 202.623.7430 • Fax +(1) 202.623.7201
publications@IMF.org
IMF.org/pubs

![](images/f33efbaf7359c502941819c05222b467da8a47c3db961aa4e58184b69274bd53.jpg)

JAPANGOV
THE GOVERNMENT OF JAPAN

This Technical Assistance was financed by the Government of Japan.

# TABLE OF CONTENTS

ACRONYMS AND ABBREVIATIONS 6
PREFACE 7
SECTION I. GENERAL INFORMATION 10
A. Mauritania's Macroeconomic Background 10
B. Authorities' request for technical assistance from ICD 10
SECTION II. PROJECT ACHIEVEMENTS 13
A. Public Debt Dynamics Tool (DDT) 13
B. Public Debt Dynamics Tool for Resource-Rich Countries (DDT RRC) 14
C. Natural Disasters Public Debt Dynamics Tools (ND DDT) 15
D. Apply the DDT for public debt projections after a commodity price shock 18
SECTION III. PROJECT RESULTS AND FUTURE CHALLENGES 21
A. Understanding the DDT and ND DDT tools 21
B. DDT Customization 22
C. Integration of tools into CNDP policies 22
D. Results from the perspective of the project objectives framework 23
E. Authorities' Views 23
F. Country team views 24
SECTION IV. RECOMMENDATIONS 25
A. Recommendations to strengthen the integration of tools into CNDP policies 25
ANNEX I. GUIDE TO PUBLIC DEBT REPORT 27
ANNEX II. INDICATIVE SCHEDULE FOR PUBLIC DEBT PROJECTION 32
ANNEX III. USER MANUAL: PUBLIC DEBT DYNAMICS TOOL FOR RESOURCE RICH COUNTRIES 33
ANNEX IV. USER MANUAL: NATURAL DISASTERS PUBLIC DEBT DYNAMICS TOOL 43
ANNEX V. USER MANUAL: PUBLIC DEBT PROJECTIONS FOLLOWING A SHOCK TO MAURITANIA'S COMMODITY EXPORT PRICES 50
ANNEX VI. PROJECT FRAMEWORK 56
ANNEX VII. PROJECT TEAM 59
FIGURES
Figure 1: List of DDT variables 13

Figure 2 : List of variables under DDT RRC \_\_\_\_ 15
Figure 3: Contributors to Changes in Public Debt \_\_\_\_ 15
Figure 4: Deviations of macroeconomic outcomes from pre-drought averages, 1969 drought event \_\_\_\_ 16
Figure 5: Inputs for country characteristics and disasters using the econometric approach \_\_\_\_ 17
Figure 6: Impacts over a three-year horizon obtained \_\_\_\_ 17
Figure 7: Calibrated final shocks of a natural disaster \_\_\_\_ 17
Figure 8: Calibrated Post-disaster Debt Projections \_\_\_\_ 18
Figure 9: Previous commodity shocks in Mauritania. \_\_\_\_ 18
Figure 10: Final calibrated shocks after -5% commodity shock \_\_\_\_ 19
Figure 11: Debt projections after calibrated commodity shock \_\_\_\_ 20
Figure 12: Public debt projections under alternative scenarios. \_\_\_\_ 20

## ACRONYMS AND ABBREVIATIONS

<table><tr><td>BCM</td><td>Central Bank of Mauritania</td></tr><tr><td>DSA</td><td>Debt Sustainability Analysis</td></tr><tr><td>LIC DSA</td><td>Debt Sustainability Analysis for Low-Income Countries</td></tr><tr><td>TA</td><td>Technical assistance</td></tr><tr><td>CD</td><td>Capacity Development</td></tr><tr><td>CNDP</td><td>National Public Debt Committee</td></tr><tr><td>CT</td><td>Technical Committee</td></tr><tr><td>DCCGT</td><td>Centralized Accounting and Cash Management Directorate</td></tr><tr><td>DDE</td><td>Directorate of External Debt</td></tr><tr><td>DDT</td><td>Public Debt Dynamics Tool (DDT)</td></tr><tr><td>DDTx</td><td>Public Debt Dynamics Tool (online course offered by IMF and EDx)</td></tr><tr><td>DDT GFN</td><td>Public debt dynamics and gross financing needs projection tool</td></tr><tr><td>DDT RRC</td><td>Public Debt Dynamics Tool (DDT) for Resource Rich Countries</td></tr><tr><td>DPAE</td><td>Directorate of Economic Forecasting and Analysis</td></tr><tr><td>FAD</td><td>Fiscal Affairs Department</td></tr><tr><td>ICD</td><td>Institute for Capacity Development</td></tr><tr><td>IMF</td><td>International Monetary Fund</td></tr><tr><td>MEF</td><td>Ministry of Economy and Finance</td></tr><tr><td>MF</td><td>Ministry of Finance</td></tr><tr><td>MEDD</td><td>Ministry of Economy and Sustainable Development</td></tr><tr><td>MCM</td><td>Monetary and Capital Markets Department</td></tr><tr><td>MTDS</td><td>Medium-term Debt Strategy</td></tr><tr><td>ND_DDT</td><td>Natural Disaster Module of the Public Debt Dynamics Project Tool</td></tr><tr><td>SPR</td><td>Strategy, Policy, and Review Department</td></tr><tr><td>WB</td><td>World Bank</td></tr></table>

## PREFACE

This report concludes the technical assistance project to develop a Public Debt Dynamics Tool (DDT) to be used in the public debt projections and analyses of the National Public Debt Committee (CNDP) of the Islamic Republic of Mauritania. Initiated in January 2024, this project included three missions; this report presents the main progress made and recommendations for integrating the tool into CNDP policies.

The last project mission, conducted from January 9 to 15, 2025, as well as the preparatory work in November and December 2024, focused on two key pillars for effective integration of the tool into policy decisions: (i) strengthening the capacity of the CNDP technical team to use the DDT and (ii) developing a manual on how to use the tool in collaboration with the authorities. The mission was led by Marie Pierre Aquino Coste (Head of Mission and Project Manager) and included Naomitsu Yashiro (Senior Economist) and Ha Minh Nguyen (Economist).

During the mission, the team worked closely with the staff of the CNDP technical committee, providing hands-on sessions to build capacity to operate the tool independently and facilitate coordination across institutions. These sessions allowed the participants to master the tool, especially its operational mechanisms. They also helped strengthen their skills to perform the routine tasks associated with public debt projections.

The mission team expresses its sincere gratitude to the Mauritanian authorities for their warm hospitality and productive collaboration. We would especially like to thank Director General Niang Idrissa of the Directorate General of Public Debt of the Ministry of Finance for his exceptional support, Deputy Director Houcein Mejdoub for the logistics, as well as the members of the CNDP for their committed participation in the workshops.

The team also benefited from close collaboration with the MCD Mission Chief for Mauritania, Mr. Felix Fisher, and his team, as well as with Mr. Oumar Dissou, FAD resident advisor for AFRITAC West. The team would like to thank Ms. Riham Yousif (ICDMF) for her outstanding administrative support and for her excellent technical contributions. The mission would also like to thank the IMF Resident Representative, Mr. Younes Zuhar, and staff from his office for their assistance, as well as the former IMF Resident Representative, Ms. Anta Ndoye, for their collaboration. The team is also deeply grateful to colleagues in the Fiscal Affairs Department (FAD) for their invaluable and constant collaboration throughout the project.

## SUMMARY

In response to a request by the Ministry of Finance (MoF) of Mauritania, the Institute for Capacity Development (ICD) of the International Monetary Fund (IMF) conducted a technical assistance (TA) project to strengthen the country's capacity in public debt analysis and projections. The initiative aimed to strengthen the analytical capacity of the National Public Debt Committee (CNDP), an inter-agency body in charge of debt policymaking, sustainability assessments, and inter-institutional coordination. A scoping mission conducted in January 2024 assessed the authorities' CD needs and led to the implementation of a TA plan based on the adoption and customization of the DDT.

The CNDP, which includes representatives from the Ministry of Finance, the Ministry of Economy and Sustainable Development (MEDD), and the Central Bank of Mauritania (BCM), plays a crucial role in shaping public debt policy but lacked the necessary tools to produce consistent debt projections and assess macroeconomic impacts. To address these gaps, the TA project introduced the Debt Dynamics Tool, a framework to project debt trajectories under different scenarios, and developed a customized version for resource-rich countries (DDT RRC) to account for Mauritania's dependence on extractive revenues. In addition, the Natural Disasters Public Debt Dynamics Tool (ND DDT) was integrated to assess the impact of climate shocks and commodity price fluctuations on debt sustainability.

The project revolved around three missions, supported by remote training sessions, in-person workshops, and continuous technical exchanges. By the end of the TA, the Mauritanian authorities have successfully implemented the DDT and produced a comprehensive report on public debt that incorporates baseline projections, risk scenarios, and policy recommendations. The core technical team demonstrated the ability to conduct independent assessments of debt sustainability, which now allows for the systematic integration of public debt analyses into policy making. In addition, user manuals have been developed to ensure the continued use of these tools, thus ensuring the retention and continuity of knowledge within the CNDP.

The TA project improved Mauritania's public debt projection and analytical capacity, equipping fiscal policymakers with tools to deal with economic and environmental uncertainties. By strengthening inter-institutional collaboration and analytical capacity, the project has laid the foundation for more resilient public debt management in Mauritania.

<table><tr><td colspan="3">Summary of Final Project Recommendations</td></tr><tr><td colspan="2">Recommendation</td><td>Indicative horizon</td></tr><tr><td>1</td><td>Integrate public debt projections and analyses using the DDT into CNDP policymaking on a regular and more comprehensive basis.</td><td>December 2026</td></tr><tr><td>2</td><td>Establish a clear division of tasks and deadlines, congruent with the overall policy planning process, among the public stakeholders involved in the projection of public debt and the drafting of the report on public debt.</td><td>December 2026</td></tr><tr><td>3</td><td>Provide regular training to new technical team members on the public debt projection tool.</td><td>Twice a year</td></tr></table>

# SECTION I. GENERAL INFORMATION

## A. Mauritania's Macroeconomic Background

1. Mauritania is highly exposed to commodity price fluctuations and natural disasters, which have significant impacts on its economic and social stability. The country's vulnerability has recently been exacerbated after the war in Ukraine, which has led to a surge in food prices and increased food insecurity for 20 percent of the population. Higher global food and energy prices, combined with lower iron ore prices, contributed to a widening trade deficit and declining external reserves in 2022. Since then, commodity prices have partially stabilized, though Mauritania's fiscal position and external buffers remain under pressure, as recurrent droughts and floods, which pose risks to macroeconomic stability and growth, while also requiring significant adaptation measures.

2. These external and climate shocks weighed on the fiscal balance and contributed to a rise in fiscal risks. To address these challenges, Mauritania secured the Extended Credit Facility (ECF) and the Extended Fund Facility (EFF) from the International Monetary Fund (IMF), for a total amount of US\$ 86.9 million, in February 2022 to support a program to maintain macroeconomic stability and improve the fiscal and monetary policy frameworks. A key objective of the program is to strengthen medium-term fiscal policy to ensure long-term fiscal sustainability. Furthermore, Mauritania obtained in December 2023 US\$258.21 million under the Resilience and Sustainability Facility (RSF) to finance climate adaptation investments and promote the green transition.

## B. Authorities' request for technical assistance from ICD

3. The Ministry of Finance requested technical assistance from the Institute for Capacity Development (ICD) to strengthen the capacity of the National Public Debt Committee (CNDP) in public debt projection and analysis. $^{1}$ The main objective of the request was to improve coordination and communication between the institutions responsible for formulating and monitoring the country's debt policy.

4. At the request of the Ministry of Finance (MoF), an exploratory TA mission visited Nouakchott from January 8 to January 19, 2024. The mission assessed the authorities' capacity to project public debt and identified the capacity development needs of institutions involved in debt projections.

5. A second technical assistance mission, which took place from August 26 to September 4, 2024, focused on strengthening Mauritania's capacity to project and analyze public debt. The main objective was to implement the Public Debt Dynamics Tool (DDT) within the CNDP technical support committee. The adoption of the DDT represents an important milestone in improving Mauritania's macroeconomic management, especially in addressing challenges to develop consistent debt projections and MTDS.

6. Given Mauritania's status as a resource-rich country, a customized version of the DDT was developed during the second mission to better capture the country's economic characteristics. This customization incorporated the non-extractive primary balance — the fiscal policy instrument used by the Mauritanian authorities — enabling the CNDP to analyze debt sustainability in a way that reflects the country's resource-dependent fiscal structure.

7. The mission also presented alternative scenarios modelling the impact of commodity price shocks and natural disaster shocks on public debt sustainability using the Natural Disaster-based Public Debt Dynamics Tool (ND\_DDT). Given Mauritania's high dependence on commodities such as iron ore, gas, and gold, the economy is highly exposed to global commodity price fluctuations and environmental risks. In addition, the country is frequently hit by natural disasters, including droughts and floods, which can have a severe impact on economic stability and debt levels. This ND\_DDT enables policymakers to design scenarios in which these adverse shocks affect those variables that define public debt trajectories. These shock scenarios provide valuable information for planning fiscal adjustment paths to restore debt sustainability after such events.

8. To complement these efforts, the CNDP technical team has prepared a public debt report that presents baseline public debt projections and alternative scenarios. The report presents fiscal paths congruent with the achievement of debt objectives, while considering the impact of natural disasters and commodity price shocks, which are particularly relevant given Mauritania's economic vulnerability. These alternative scenarios provide a critical analysis of how such shocks might affect public debt sustainability and lay the ground for the analysis of measures to reduce these vulnerabilities.

9. The most recent technical assistance mission took place in Nouakchott from January 9 to 15, 2025, and helped strengthen the technical capacities and the ownership of the DDT by the Mauritanian authorities. Representatives from various institutions collaborated on an exercise to produce a revised report on public debt. First, they defined roles and responsibilities for timely data provision and improved coordination among agencies. They then worked across institutions to harmonize data assumptions and reconcile inputs. Finally, the participants collaborated to complete the structure of the public debt report, integrating baseline projections and alternative scenarios using the most recent data.

10. The mission also conducted an exhaustive review of all project documents, tools, and customizations, thereby strengthening the understanding and capacity to make effective use of the tools developed. Participants were provided with a set of user manuals on how to calibrate natural disaster shocks and commodity price shocks using the ND\_DDT, the public debt dynamics tool corresponding to a natural disaster. In addition, the team will also provide the user manual of the Public Debt Dynamics Tool for RRCs.

11. The mission helped enhance the knowledge and skills acquired by the Mauritanian authorities in the institutions concerned. A key priority is to integrate the DDT and Public Debt Report into the country's public debt policies. The mission encouraged the CNDP technical committee to conduct independent debt sustainability analyses and effectively manage public debt. This last phase also involved creating protocols and procedures for consistent use of these tools, as well as training additional staff to ensure continuity. Over the medium term, these efforts will focus on strengthening Mauritania's capacity to manage public debt by producing periodic public debt projections as part of its macroeconomic policy formulation and to more strongly ada

[中间内容因长度限制已省略]

minus Baseline (% of GDP)  
![](images/8dd06e023c6e8620dd8bbda23cb9e520286deca26ee615bc781faddf8f77ce24.jpg)

Tab export\_DDT also shows the difference in factors contributing to the debt-creating flows between the customized scenario and the baseline scenario, as shown in the chart below. For this shock, by 2025 the figure shows that the primary deficit and lower real GDP growth contribute to the higher public debt-to-GDP ratio under the customized scenario (the one with a commodity shock) relative to the baseline. The increase in 2025 amounts to 1.5 percent of GDP. In 2026, the persistent deterioration in the primary balance contributes to an additional 0.5 percent of GDP debt increase.

## ANNEX VI. PROJECT FRAMEWORK

## Objective:

Develop capacity in macroeconomic forecasting and policy analysis to support policy decision-making and communication - MFR

Outcome:

Analytical models and forecasting tools are developed and operational

Annual Assessment Rating: 4 fully achieved

Annual Assessment Narrative: The core team leverages the customized Debt Dynamics Tool (DDT) specifically designed for Resource Rich Countries to generate accurate and comprehensive public debt projections. This specialized tool enables the team to account for the unique economic characteristics and challenges faced by Mauritania, ensuring tailored and relevant analyses. Furthermore, the integration of the ND-DDT enhances their capabilities by allowing them to simulate and analyze alternative scenarios. This includes assessing the potential impacts of climate-related shocks and fluctuations in commodity prices, providing critical insights into how such shocks could influence debt sustainability. By combining these tools, the core team is well equipped to offer robust, scenario-based forecasting and risk assessment for informed decision-making.

Outcome Rating Date: 1/28/2025

<table><tr><td>Outcome Indicator</td><td>Baseline Value</td><td>Target Value</td><td>Current Assessment Value</td></tr><tr><td>Macroeconomic Projection Tool (MPT) is developed in the form of a fiscal/debt sustainability tool, e.g. public Debt Dynamic Tool (DDT)</td><td>No</td><td>Yes</td><td>4 Fully Achieved as of 9/23/2024</td></tr><tr><td>Milestone Name</td><td>Target Completion Date</td><td>Milestone Actual Completion Date</td><td>Milestone Rating</td></tr><tr><td>The core team produces a draft Public Debt Report using the DDT.</td><td>8/30/2024</td><td>12/31/2024</td><td>4 Fully Achieved as of 1/28/2025</td></tr></table>

Outcome:

Improved analytical skills, better macroeconomic forecasting and policy analysis capacity

Annual Assessment Rating: 4 fully achieved

Annual Assessment Narrative: The core team benefitted from virtual asynchronous training on DDTx and an in-person workshop on the DDT. Throughout the project, multiple refreshment sessions were conducted to reinforce learning and address any new challenges, ensuring a thorough understanding of the tools. In addition, a comprehensive user manual was developed to serve as an ongoing reference for the team. As a result, the core team has demonstrated significantly improved analytical skills and has started effectively using the DDT to produce public debt projections and gain a deeper understanding of debt dynamics.

Outcome Rating Date: 1/28/2025

<table><tr><td>Outcome Indicator</td><td>Baseline Value</td><td>Target Value</td><td>Current Assessment Value</td></tr><tr><td>Participants have successfully completed the accredited training delivered through various modalities (online, classroom courses, workshops).</td><td>0</td><td>100</td><td>4 Fully Achieved as of 1/23/2024</td></tr><tr><td>Analytical framework centered around the MPT is used to produce medium-term forecasts, scenarios as well as risk and policy analysis</td><td>To be assessed during Pre-Scoping Meetings</td><td>Équipe Core is able to produce Debt/GDP projections by means of the DDT.</td><td>4 Fully Achieved as of 9/23/2024</td></tr><tr><td>Milestone Name</td><td>Target Completion Date</td><td>Milestone Actual Completion Date</td><td>Milestone Rating</td></tr><tr><td>Core team finished asynchronous training of the DDT (through EdX) with virtual follow-ups.</td><td>1/5/2024</td><td>12/29/2023</td><td>4 Fully Achieved as of 1/22/2024</td></tr><tr><td>Équipe Core is able to produce baseline medium-term projections of the Debt/GDP path using the DDT.</td><td>1/31/2024</td><td>1/19/2024</td><td>4 Fully Achieved as of 1/28/2025</td></tr><tr><td>Core team produced a risk matrix for the Mauritanian economy, included climate-related risks, and is capable of including climate-related risks by means of the ND DDT.</td><td>12/31/2024</td><td>09/04/2024</td><td>4 Fully Achieved as of 9/23/2024</td></tr></table>

## ANNEX VII. PROJECT TEAM

<table><tr><td>1. Abdel Baghi</td><td>14. Muhammad Abad Yah</td></tr><tr><td>2. Azza Abdallahay Haballa</td><td>15. Mohamed Abdel Kader</td></tr><tr><td>3. Bacar Khayar</td><td>16. Mohamed Didi Taleb</td></tr><tr><td>4. Baham Ahmed Benane</td><td>17. Mohamed El Yezid</td></tr><tr><td>5. Bakary Gandega</td><td>18. Mohamed Khlil</td></tr><tr><td>6. Didi Sid&#x27;ahmed</td><td>19. Mohamed Yahya Cheikh Mohamed El Mokhtar</td></tr><tr><td>7. El Hadj Cheikh-Abdallahi</td><td>20. Mohamed Yahya Mohamed El Moustapha</td></tr><tr><td>8. El hadj Dembele</td><td>21. Niang Idrissa</td></tr><tr><td>9. Fatma Abdelkader</td><td>22. Sarra Mohamed Cheikh Sidiya</td></tr><tr><td>10. Hamoud MICHEL</td><td>23. Sarre Adama Souleymane</td></tr><tr><td>11. Houcein Mejdoub</td><td>24. Sidi Lemrabott</td></tr><tr><td>12. Jemila Abdarrahmane Emir</td><td>25. Youssouf Cheikh Sidiya</td></tr><tr><td>13. Mariem Zeidane</td><td></td></tr></table>
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
