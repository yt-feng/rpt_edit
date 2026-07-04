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
# Effects of a Community-Driven Water, Sanitation, and Hygiene Intervention on Diarrhea, Child Growth, and Local Institutions

A Cluster-Randomized Controlled Trial in Rural Democratic Republic of Congo

John P Quattrochi

Kevin Croke

Caleb Dohou

Luca Stanus Ghib

Yannick Lokaya

Aidan Coville

Eric Mvukiyeh

POLICY RESEARCH WORKING PAPER 11070

## Abstract

Diarrhea and growth faltering in early childhood reduce survival and impair neurodevelopment. This paper assesses whether a national program in the Democratic Republic of Congo reduced diarrhea and stunting and strengthened local water and sanitation institutions. The program combined (i) funds for latrine and water upgrades, (ii) institutional strengthening activities, and (iii) behavior change campaigns. In 2018, the program was randomly assigned, after stratifying by province and cluster size, with 50 intervention and 71 control clusters. In 2022–23, 3,283 households were interviewed, at a median of 3.6 years post-intervention. The intervention had no effect on diarrhea and no effect on length-for-age Z-scores in children. Villages in the intervention group had a 0.40 higher score on the water, sanitation, and hygiene institutions index.

The percentage of villages in the intervention group with an active water, sanitation, and hygiene (or just water) committee was 21 percentage points higher than the control group. Households in the intervention group were 24 percentage points more likely to report using an improved water source, 18 percentage points more likely to report using an improved sanitation facility, and reported more positive perceptions of water governance. The Democratic Republic of Congo's national rural water, sanitation, and hygiene program increased access to improved water and sanitation infrastructure, and created new water, sanitation, and hygiene institutions, all of which persisted for more than three years. However, these effects were not sufficient to reduce diarrhea or growth faltering.

![](images/cf29be8d6ab5c85b29e85764fc394f7444cf3ab6027581c6cb3e85aeb218ba4c.jpg)

Effects of a Community-Driven Water, Sanitation, and Hygiene Intervention on Diarrhea, Child Growth, and Local Institutions: A Cluster-Randomized Controlled Trial in Rural Democratic Republic of Congo

John P Quattrochi $^{1}$ , Kevin Croke $^{2}$ , Caleb Dohou $^{3}$ , Luca Stanus Ghib $^{3}$ , Yannick Lokaya $^{3}$ , Aidan Coville $^{3}$ , Eric Mvukiyeh $^{4}$

## Introduction

The most recent estimates of the global burden of morbidity and mortality attributable to unsafe water, sanitation, and hygiene (WASH) are that 1.4 million deaths and 74 million disability-adjusted life years lost could have been prevented in 2019 [1]. People living with unsafe WASH have higher exposure to fecal-oral pathogens, resulting in enteric dysfunction, diarrheal illnesses, and, in children, growth faltering. Growth faltering, in turn, has long-term negative impacts on health, cognition, and human capital [2,3]. In 2020, 2.0 billion people did not have access to safely managed drinking water services, 3.6 billion did not have access to safely managed sanitation services, and 2.3 billion did not have access to handwashing facilities with soap and water at home [4,5]. While access has been increasing, progress will need to accelerate by three-to-six-fold to meet the Sustainable Development Goals for 2030 [6]. The challenge of increasing access is particularly acute for people living in or near armed conflict – one in six people worldwide – both through the direct effects of conflict and because violence and insecurity impede collective action to provide public goods like WASH [7,8]. In the Democratic Republic of Congo (DRC), as of 2020, 48 million people still lacked basic drinking water services, 11 million people still practiced open defecation, and 72 million people still lacked basic hygiene services [9].

To increase access to safe WASH, governments and donors have increasingly turned to community-led approaches. While WASH experts called for greater community participation for over 30 years [10], the sector did not fully embrace this approach until the late 1990s. Beginning with community-led total sanitation in Bangladesh in 1999, community-led WASH programs have been implemented in at least 60 countries, and 15 countries have incorporated them into national policy [11,12].

Despite this broad adoption, the health effects of community-led WASH interventions – and of many WASH interventions in general – remain poorly understood. The accumulation of evidence has accelerated in recent years, but the length of the causal chain from the intervention to the outcome, and the vast design space for WASH interventions (which can incorporate behavior change campaigns, infrastructure, institutions, and/or new technologies), means that many fundamental questions remain unanswered. A meta-analysis of 13 randomized WASH trials found no effect on child length-for-age, but a meta-analysis of 124 WASH studies (randomized and observational) found a protective effect against diarrhea [11,13–24]. There is a great deal of heterogeneity in effect size across studies, likely due to variation in intervention components and intensity, and to the influence of contextual factors such as baseline exposure to fecal matter.

To our knowledge, this is the first trial of an intervention that combines the creation of new institutions, funding for new or improved infrastructure, and a behavior change campaign, all within a locally-led process of targeting and implementation. We study this complex intervention as it is implemented at scale, providing a realistic estimate of effectiveness for policy makers in similar contexts. Our follow-up period is unusually long (3.6 years), enabling us to address the question of sustainability. We also provide evidence in a conflict-affected setting, where WASH interventions have rarely been evaluated using experimental designs.

The intervention is the ‘healthy villages’ component of the DRC’s Healthy Villages & Schools program, co-led by the Ministries of Public Health, and of Primary, Secondary, and Professional Education, with support from the United Nations Children’s Fund (UNICEF). Since 2008, nearly 9 million people in almost 11,000 villages have been reached with WASH services through the program. Healthy Villages & Schools was the largest WASH program implemented by UNICEF globally and comprised 90% of total external funding committed to rural WASH in the DRC from 2005 to 2020 [25]. Our goal was to estimate the effect of Healthy Villages & Schools on diarrhea prevalence, child length-for-age, and WASH institutions.

## Methods

## Study design and participants

The intervention of interest is a DRC government-run program that began several years before our study. For our study, the government agreed to randomly assign the next phase of the program (i.e. the next group of villages to receive the intervention). In 2018, we randomly assigned groups of villages to intervention or control (details below). Since we did not collect any data prior to randomization, we did not yet register the study. We collected the first round of data in late 2019, about 5 months after the intervention was implemented (implementation took about one year in each group of villages) [26].

We pre-registered the analysis of that first round of data collection (5 month follow-up), before any of the authors saw the data, in the American Economics Association (AEA) Registry (AEARCTR-0004648) (https://www.socialscienceregistry.org/trials/4648).

In Feb 2021, we registered plans for additional data collection in the Pan-African Clinical Trials Registry (PACTR202102616421588; https://pactr.samrc.ac.za/TrialDisplay.aspx?TrialID=14670). In April 2023, before the PIs had seen any data for the 3.6-year follow-up (i.e., the data for the current manuscript), we updated the registration with our primary and secondary outcomes. In April 2023, we also posted our pre-analysis plan for the 3.6 year follow up on the AEA Registry (see "Three Year Follow up Pre-Analysis Plan" at https://www.socialscienceregistry.org/trials/4648). All planned studies from this project are now registered and any future work will be registered prospectively.

This study is reported as per CONSORT guideline (S1 Text).

We worked with intervention implementers to design a cluster-randomized trial in rural villages in five DRC provinces: Kongo Central, Kasai, Kasai Central, North Kivu, and South Kivu. The implementers identified 403 candidate villages in which the intervention could be launched during the study period, based on the established criteria for the intervention: that the village was located in a secure and accessible Health Area that was not already served by the WASH Consortium, the Health Area staff were dynamic and interested in participating, and there was a problem of diarrhea, cholera, and/or malnutrition. Among these villages, 34 already had program activities in process before research activities began, leaving 369 eligible villages.

To avoid spillover effects from treatment villages to control villages, we grouped those villages into clusters. We considered any villages within 2.5 km of each other (using Euclidean distance between village centroids) to be part of the same cluster. Therefore, all clusters have at least 2.5 km between them. We relax this rule in South Kivu, where density is greater, and use a minimum distance of 1km. In total, this resulted in 124 clusters. North Kivu had only three clusters (covering 30 villages); as a result, it was not logistically feasible to include these villages in the trial. That left 121 clusters (339 villages) in four provinces.

Each village in the intervention clusters received the intervention, as described above. Villages in control clusters did not receive any intervention. Data collection procedures were identical in the two groups.

The study protocol was approved by the Institutional Ethics Committee of the Institut Superieur des Techniques Médicales de Bukavu (DRC) (#001/2019 & #008/2022) and by Solutions IRB (USA) (#2019/10/20). With direction from the study investigators, Innovative Hub for Research in Africa (IHfRA) was responsible for data collection. No study data was collected by intervention implementers.

All residents of the targeted villages who had lived in the village for at least four years (i.e., moved to the village prior to the intervention) were eligible to participate in the study. Two groups of households were interviewed: households that were interviewed at 5 months post-intervention (4 per village) and households that had not been previously interviewed (6 per village). Both groups were randomly selected (at their respective entries into the study) as follows: from the center of the village, interviewers went in opposite directions to the nth household, where n was a randomly selected number between 1 and 20. We interviewed the head woman of the household. We also asked to measure the height and weight of the youngest child aged 2-5 years, or, if none, the oldest child aged 0-2 years. Adult participants provided informed consent verbally, which was recorded electronically.

## Randomization and masking

A total of 339 villages in 121 clusters were eligible for randomization. In all provinces except Kasai Central, each cluster was given equal probability of being selected for treatment or control. In Kasai Central, due to budget constraints, we increased the probability of being selected into the control group to 75%, to reflect the fact that only 16 out of 81 villages could receive the intervention. Thus the allocation probability for the intervention group was 25%.

We block randomized by province and number-of-villages-per-cluster (12 blocks total; see S1 Table). Since randomization was based on clusters but the implementing organization's operational targets were based on villages, it was not possible to force the randomization to select the exact number of villages targeted without introducing potential bias. Instead, we compared the number of target villages per province to the number of treatment villages selected after randomization. In cases where the number of intervention villages was larger than the operational target, we randomly dropped an equal number of intervention villages from the largest control and intervention clusters until operational targets were met. We dropped 2 villages in Kongo Central and 4 villages in Kasai. We also dropped one control village in Kasai due to a coding error. This left 146 villages in 50 clusters in the intervention group, and 186 villages in 71 clusters in the control group. S1 Table shows how intervention and control villages and clusters are distributed across provinces. Randomization was done by the research team in Stata.

Due to the participatory and visible nature of the intervention, neither participants nor data collectors were masked to treatment status. However, data collectors did not participate in intervention implementation and were employed by a separate, independent organization.

## Procedures

The intervention, “Healthy Villages & Schools”, was developed by the DRC government and UNICEF. We focused on the village rather than the school component. This program mobilizes communities to become a “Healthy Village” with 3-6 months of support from government health officials and local NGOs, including approximately \$2,000 of financing for new or improved water infrastructure, \$2,000 for new or improved sanitation infrastructure, and \$3,000 for personnel costs, per village. The mean village size in the intervention group was 456 people (median 400; IQR 502). The seven norms to become a Healthy Village are:

1. There is a dynamic village WASH committee.

2. At least 80% of the population has access to safe drinking water.

3. At least 80% of households use a hygienic latrine.

4. At least 80% of households dispose of their household waste hygienically.

5. At least 60% of the population washes their hands before eating and after going to the latrine.

6. At least 70% of the population is aware of fecal-oral disease transmission and how to prevent this.

7. The village is cleaned at least once a month.

The program is implemented in nine steps (Table 1) [27].

Table 1. The Healthy Village and Schools Program's Nine Steps

<table><tr><td>Step</td><td>Description</td></tr><tr><td>0</td><td>The community learns about the program and collectively decides to adopt it before submitting a formal request to the relevant Health Zone. (A Health Zone is a geographic unit of the Congolese health system that contains roughly ten Health Areas and 100,000 residents, run by a Chief Medical Officer (CMO)). Program protocols state that the entire community should be involved in the decision to participate.</td></tr><tr><td>1</td><td>A statement of agreement between the community and the Health Zone is signed.</td></tr><tr><td>2</td><td>Health Zone officials survey 19 households on knowledge, attitudes, and practices (KAP). The community self-evaluates on eight practices, including handwashing, water use, and sanitation.</td></tr><tr><td>3</td><td>The community spends about 11 hours over five days creating calendars and maps, visiting water points, classifying hygienic practices as healthy or unhealthy, discussing fecal-oral disease transmission, calculating medical costs, and assessing which individuals and organizations influence sanitation and hygiene in the community. This includes 1.5-2 hours in a facilitated activity around the question, “What are the hygiene practices that we want to change in our village?”</td></tr><tr><td>4</td><td>The Health Zone provides training for 20 volunteers on maintenance of latrines, water supply systems, and sanitation, conflict management, and petty cash management. The community elects a village WASH committee.</td></tr><tr><td>5</td><td>The community spends ten hours over three days describing a community vision, analyzing the barriers to reducing diarrheal diseases, choosing improvements to drinking water, sanitation, and hygiene, and formulating an action plan. The community is asked to identify practical, low-cost solutions with a minimum of outside assistance. New infrastructure is evaluated in terms of accessibility, technical feasibility, and technical capacity.</td></tr><tr><td>6</td><td>The community builds new infrastructure over 90-180 days, supported by project funds. Key messages about sanitation and hygiene are discussed during sensibilization meetings or during visits to families by the WASH committee, community health workers, or other volunteers. Health Zone staff are expected to visit the community monthly during this time; Health Area staff weekly.</td></tr><tr><td>7</td><td>The community self-evaluates again, to measure progress since Step 2. The Health Zone conducts additional KAP surveys and hosts three hours of meetings to assess the findings and make a plan to maintain progress.</td></tr><tr><td>8</td><td>The CMO spends one day in the community to assess whether or not the community has completed its action plan and achieved the seven norms. If they have, a certification ceremony is held. The CMO and the village WASH committee develop a Community Action Plan for Maintenance so that the changes achieved through the program can be sustained over time.</td></tr></table>

The IHfRA data collection team used electronic tablets and transmitted data to a cloud-based server, allowing the research team to conduct quality control measures in real-time, checking for consistency and errors. Additionally, IHfRA randomly selected 15% of villages for a second round of interviews, by different interviewers, with a shorter questionnaire, to check consistency across key variables. Separately, children from two households per village had their height and weight re-measured by an IHfRA supervisor, as a quality check.

## Outcomes

Primary outcomes were caregiver-reported diarrhea in the last seven days among all children who were under 5 years old at the time of the survey, length-for-age Z score for a randomly selected child in each household, and a WASH governance index. If the household had one child between age 2 and 5, we measured the length and weight of that child. If the household had more than one child between age 2 and 5, we randomly selected one child. If the household had no children between ages 2 and 5, but one or more children between ages 0 and 2, we measured length and weight of one of those children (randomly selected). Salter scale (Model 235 6S) and wall-mounted measuring rods (portable b

[中间内容因长度限制已省略]

eria), with reasons</td><td>NA</td></tr><tr><td rowspan="2">Participants</td><td>4a</td><td>Eligibility criteria for participants</td><td>Study design, 9th paragraph</td></tr><tr><td>4b</td><td>Settings and locations where the data were collected</td><td>Study design, 5th paragraph</td></tr><tr><td>Interventions</td><td>5</td><td>The interventions for each group with sufficient details to allow replication, including how and when they were actually administered</td><td>Procedures</td></tr><tr><td rowspan="2">Outcomes</td><td>6a</td><td>Completely defined pre-specified primary and secondary outcome measures, including how and when they were assessed</td><td>Outcomes</td></tr><tr><td>6b</td><td>Any changes to trial outcomes after the trial commenced, with reasons</td><td>NA</td></tr><tr><td rowspan="2">Sample size</td><td>7a</td><td>How sample size was determined</td><td>Statistical analysis</td></tr><tr><td>7b</td><td>When applicable, explanation of any interim analyses and stopping guidelines</td><td>NA</td></tr><tr><td colspan="4">Randomization:</td></tr><tr><td>Sequence generation</td><td>8a8b</td><td>Method used to generate the random allocation sequenceType of randomization; details of any restriction (such as blocking and block size)</td><td>Randomization and maskingRandomization and masking</td></tr><tr><td>Allocation concealment mechanism</td><td>9</td><td>Mechanism used to implement the random allocation sequence (such as sequentially numbered containers), describing any steps taken to conceal the sequence until interventions were assigned</td><td>Randomization and masking</td></tr><tr><td>Implementation</td><td>10</td><td>Who generated the random allocation sequence, who enrolled participants, and who assigned participants to interventions</td><td>Randomization and masking</td></tr><tr><td rowspan="2">Blinding</td><td>11a</td><td>If done, who was blinded after assignment to interventions (for example, participants, care providers, those assessing outcomes) and how</td><td>NA</td></tr><tr><td>11b</td><td>If relevant, description of the similarity of interventions</td><td>NA</td></tr><tr><td rowspan="2">Statistical methods</td><td>12a</td><td>Statistical methods used to compare groups for primary and secondary outcomes</td><td>Statistical analysis</td></tr><tr><td>12b</td><td>Methods for additional analyses, such as subgroup analyses and adjusted analyses</td><td>Statistical analysis</td></tr><tr><td colspan="4">Results</td></tr><tr><td rowspan="2">Participant flow (a diagram is strongly recommended)</td><td>13a</td><td>For each group, the numbers of participants who were randomly assigned, received intended treatment, and were analyzed for the primary outcome</td><td>Study design</td></tr><tr><td>13b</td><td>For each group, losses and exclusions after randomization, together with reasons</td><td>Study design</td></tr><tr><td rowspan="2">Recruitment</td><td>14a</td><td>Dates defining the periods of recruitment and follow-up</td><td>Results</td></tr><tr><td>14b</td><td>Why the trial ended or was stopped</td><td>NA</td></tr><tr><td>Baseline data</td><td>15</td><td>A table showing baseline demographic and clinical characteristics for each group</td><td>Table 2</td></tr><tr><td>Numbers analysed</td><td>16</td><td>For each group, number of participants (denominator) included in each analysis and whether the analysis was by original assigned groups</td><td>Tables 3-4</td></tr><tr><td rowspan="2">Outcomes and estimation</td><td>17a</td><td>For each primary and secondary outcome, results for each group, and the estimated effect size and its precision (such as 95% confidence interval)</td><td>Results, Tables 3-4</td></tr><tr><td>17b</td><td>For binary outcomes, presentation of both absolute and relative effect sizes is recommended</td><td>Tables 3-4</td></tr><tr><td>Ancillary analyses</td><td>18</td><td>Results of any other analyses performed, including subgroup analyses and adjusted analyses, distinguishing pre-specified from exploratory</td><td>Results; Supp Info</td></tr><tr><td>Harms</td><td>19</td><td>All important harms or unintended effects in each group (for specific guidance see CONSORT for harms)</td><td>NA</td></tr><tr><td colspan="4">Discussion</td></tr><tr><td>Limitations</td><td>20</td><td>Trial limitations, addressing sources of potential bias, imprecision, and, if relevant, multiplicity of analyses</td><td>Discussion,  $2^{nd}$  to last paragraph</td></tr><tr><td>Generalizability</td><td>21</td><td>Generalizability (external validity, applicability) of the trial findings</td><td>Discussion</td></tr><tr><td>Interpretation</td><td>22</td><td>Interpretation consistent with results, balancing benefits and harms, and considering other relevant evidence</td><td>Discussion</td></tr><tr><td colspan="4">Other information</td></tr><tr><td>Registration</td><td>23</td><td>Registration number and name of trial registry</td><td>Study design</td></tr><tr><td>Protocol</td><td>24</td><td>Where the full trial protocol can be accessed, if available</td><td>Study design</td></tr><tr><td>Funding</td><td>25</td><td>Sources of funding and other support (such as supply of drugs), role of funders</td><td>Abstract</td></tr></table>

\*We strongly recommend reading this statement in conjunction with the CONSORT 2010 Explanation and Elaboration for important clarifications on all the items. If relevant, we also recommend reading CONSORT extensions for cluster randomized trials, non-inferiority and equivalence trials, non-pharmacological treatments, herbal interventions, and pragmatic trials. Additional extensions are forthcoming: for those and for up-to-date references relevant to this checklist, see www.consort-statement.org.
"""
