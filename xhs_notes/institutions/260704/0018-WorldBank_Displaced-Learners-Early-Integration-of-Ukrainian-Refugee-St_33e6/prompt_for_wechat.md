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
# Displaced Learners

# Early Integration of Ukrainian Refugee Students into Italy's Schools

Michela Carlana

Pauline Castaing

Mauro Testaverde

Marco Tiberti

POLICY RESEARCH WORKING PAPER 11055

## Abstract

The paper examines the early integration of Ukrainian refugee students into Italy's education system following the Russia's invasion of Ukraine in 2022. Using administrative and survey data, the study presents enrollment trends, academic performance, and barriers to educational integration. Findings from the analysis indicate that Ukrainian refugees face lower enrollment rates, higher absenteeism, and lower test scores than other students, particularly in subjects requiring language proficiency. Despite these challenges, teachers often recommend Ukrainian refugee students for advanced educational tracks, thus revealing their optimism about the potential of these students. Language barriers, mental health challenges, and uncertain futures are identified as major obstacles to integration. The study highlights the importance of tailored interventions, such as psychological support and more dedicated teaching time, to foster refugee students' academic and social inclusion.

# Displaced Learners: Early Integration of Ukrainian Refugee Students into Italy's Schools

Michela Carlana\*, Pauline Castaing $^{^}$ , Mauro Testaverde $^{^}$ , Marco Tiberti $^{^}$

JEL codes: I21, 015, R23
Keywords: Education, Forced Migration, Italy, Refugees, Ukraine

\# Harvard Kennedy School and Bocconi University

^ World Bank, Development Data Group

## Acknowledgments

This paper would have not been possible without the data access offered by the Italian Ministry of Education and INVALIDSI. Administrative data were elaborated by the LEAP-Bocconi team for this research project within the protocol “School system, educational choices and interventions to mitigate educational poverty in Italy”. The report team is grateful to the teams in the Italian Ministry of Education (Rita Angelini, Carla Borrini, Lucia De Fabrizio and Annarita Marzullo) and INVALIDSI (Patrizia Falzetti and Paola Giangiacomo) for sharing the data for this study and to Marta Magnani and Lucrezia Di Scanno for their research assistance. This paper was made possible by grants from the Knowledge for Change Program (KCP) and the Global Knowledge Partnership on Migration and Development (KNOMAD).

## 1. Introduction

Russia's invasion of Ukraine in 2022 led to the displacement of more than 6 million Ukrainians, predominantly women and children. By June 2024, data from UNHCR showed approximately 6.5 million refugees had fled Ukraine, with nearly 6 million seeking refuge in European Union (EU) countries. Germany hosted the largest number at 1.17 million, followed by Poland with 957,000, Czechia with 347,000, Spain with 202,000, and Italy with 170,000 (UNHCR, 2024). Due to conscription laws affecting men aged 18-60, around $79\%$ of refugees under temporary protection in Europe as of March 2024 were women and children. $^{1}$

The timing of the invasion and the demographic characteristics of the displaced population created severe challenges for young refugees' human capital formation. This study focuses on Ukrainian refugee students in Italy, the fifth largest host country of Ukrainian refugees within the EU, aiming to examine how Ukrainian refugee children are adapting to the Italian school system during early years of displacement and it investigates factors that may either hinder or support their integration.

Research shows that conflict and displacement adversely affect educational outcomes for children, with extensive evidence pointing to negative effects on both educational attainment and future earnings potential (see, among others, Ichino and Winter-Ebmer, 2004; Alderman et al., 2006: Agüero and Majid, 2014; Akresh and De Walque, 2008; Swee, 2009, 2015; Chamarbagwala and Morán, 2011; Shemyakina, 2011; Oyelere and Wharton, 2013; Rodríguez and Sánchez, 2012; León, 2012; Kecmanovic, 2013; Islam et al., 2016; Brück et al., 2019; Bertoni et al., 2019). These impacts translate into reduced schooling years, lower enrollment rates, decreased likelihood of passing exams, and diminished access to higher-tier academic tracks and institutions of higher education (Collier, 2003;

Gates et al., 2012). The factors driving these impacts are multifaceted, including the destruction of educational facilities, displacement from learning environments, economic shifts prioritizing wartime efforts, the loss of trained educational professionals, and the psychological toll on students exposed to violence (Justino, 2011).

Considering the challenges Ukrainian refugee students encounter abroad, it is essential to evaluate human capital losses and identify factors that can support their educational integration into host countries' systems, aiming to prevent potentially irreversible long-term impacts. Moreover, beginning just after the pandemic, when students could finally return to schools for in-person learning, the displacement may further worsen learning losses among Ukrainian refugee children (UN, 2023; Angrist et al., 2022). Research shows that students who speak a different language at home generally lag behind their peers by about one year of schooling on average (OECD, 2015). Additionally, studies have found that immigrant parents in OECD countries are notably less involved in their children's school communities, a factor associated with lower academic performance and a diminished sense of belonging among students (OECD, 2018). This lower parental engagement in educational settings is often linked to barriers like language and cultural differences, which can hinder students' social and academic integration (Friedberg and Hunt, 1995).

The long-term consequences of these trends are significant, as diminished educational outcomes and social isolation can hinder successful integration into host communities. Conversely, sustained social and educational integration efforts are vital for positive outcomes. For instance, studies indicate that long-term integration can be hampered by social, economic, and institutional barriers (Chiswick and Miller, 2014), while interventions focused on language support and community engagement can lower these barriers (Ozden and Wagner, 2020). Further, specific interventions aimed at removing obstacles to education for children on the move can contribute significantly to better integration outcomes (Schuettler and Caron, 2020).

This paper benefits from key information coming from administrative data on educational records of Ukrainian refugees in Italy for the academic years 2021-2022 to 2023-2024 for grades 6 to 13. This provides a unique opportunity to examine enrollment, attendance, test performance, and other indicators of integration into the Italian educational system. Supplemented by survey data collected in 2023-2024, this study offers an overview of the challenges and opportunities faced by Ukrainian students in secondary schools and highlights areas for potential policy development.

This study advances the literature by adding empirical evidence on the short- to medium-term educational impacts of displacement on young refugees within a European host country, offering insights into the role of education policy in mitigating human capital losses. It also contributes to discussions on human development by identifying factors that support or hinder integration, highlighting pathways for improving educational and social outcomes for refugee students.

Results highlight that despite gradual improvements, enrollment rates remain significantly lower among refugees compared to native and other foreign students. Ukrainian refugees also demonstrate higher absenteeism and lower academic performance, particularly in subjects requiring language proficiency such as Italian and English. However, good performance in mathematics suggests potential strengths linked to their prior educational backgrounds. Despite these challenges, teachers seem to be more inclined to recommend Ukrainian refugees for high-track education compared to other newly arrived foreigners, indicating potential optimism about their academic capabilities. The paper also examines possible barriers to the integration of Ukrainian refugee students into the Italian education system.

This paper contributes to several key areas of the literature. First, while previous studies (e.g., Ichino and Winter-Ebmer, 2004; Alderman et al., 2006) have focused on the broader educational impacts of conflict, this research identifies the specific challenges faced by Ukrainian refugee students, providing targeted insights into a unique and contemporary refugee situation of large-scale displacement in a European context. Second, this paper identifies the potential critical barriers—language proficiency, absenteeism, and psychological distress—that hinder the integration process. Unlike prior studies that generally highlight the effects of displacement (e.g., Justino, 2011; Brück et al., 2019), this paper provides actionable evidence on how these barriers manifest within the Italian context. Third, unlike previous research that aggregates migrant experiences, this study explicitly contrasts the experiences of Ukrainian refugees with other newly arrived migrants, demonstrating unique strengths (e.g., performance in mathematics) and challenges (e.g., Italian language proficiency).

The remainder of the paper is structured as follows. Section 2 presents the context and provides background information on the influx of Ukrainian refugees in Italy as well as on the Italian education system. Section 3 presents the data and the methodology used for the empirical analysis. Section 4 discusses the findings and explores possible barriers to the integration of Ukrainian refugee students into the Italian education system. Finally, Section 5 concludes the study.

## 2. Background and Context

## 2.1 Influx of Ukrainian refugee students in Italy

The massive influx of Ukrainian students into Italian schools following the invasion of their country, paired with the substantial presence of Ukrainian students in the Italian education system in previous years, makes Italy an ideal setting for the empirical analysis. Since February 2022, Italy has received around 190,000 temporary protection applications from Ukrainians, with approximately 170,000 still active as of June 2024. $^{2}$ $^{3}$ During the 2021-2022 school year, around 20,000 Ukrainian children enrolled in Italian schools within the final three months of classes. By May 2022, the Italian education system had registered 22,788 Ukrainian refugee students, as reported by the Ministry of Education (MoE, 2022a): approximately 46% of these students attended primary school, while around 9% were in high school. The proportions of pre-school and middle-school students were similar, each constituting about 22% (MoE, 2022a). The regional distribution of Ukrainian refugee students matched closely with the distribution of Ukrainian students that were attending schools in Italy before February 2022, with 56% of Ukrainian refugee students enrolled in schools in northern regions, while just 24% were in southern regions (MoE, 2022a).

Ukrainian students, both refugees and non-refugees, made up 4% (38,466) of foreign students in Italy's school system during the 2022-2023 academic year. The majority were in elementary school (39.1%), with 24.1% enrolled in lower secondary school and 23.4% in upper secondary school. Additionally, 13.3% of Ukrainian students attended pre-primary school. Data from the Ministry of Education highlights the significant number of unaccompanied minors from Ukraine in Italy since 2022; in the 2022-2023 school year, Ukrainian students represented the largest group of unaccompanied minors in the Italian school system, comprising 25.1% of this population. $^{4}$

Italy's response to the influx of Ukrainian refugees included a range of initiatives to support swift integration. Similarly to other EU countries, Italy activated the EU's Temporary Protection Directive, allowing Ukrainians to reside, work, and access health care and education. The Italian government streamlined temporary protection processes to prevent educational disruptions, enabling refugee children to enroll in local schools and recognize Ukrainian qualifications, allowing students and adults to pursue education and employment matching their skills (MoE, 2022b). The Ministry of Education issued guidelines to help schools support Ukrainian students, including individual education plans, language support, psychological aid, and intercultural activities. Additionally, the Cohesion's Action for Refugees in Europe (CARE) program was introduced to foster integration through digital and intercultural education, sports, artistic expression, and lifelong learning modules for both students and their families (MoE, 2023). $^{5}$

## 2.2 The Italian education system

The Italian education and training system is structured into three cycles, with an integrated system for children under six. The integrated system, lasting six years, is optional for children aged 0 to 6. The first cycle of education is mandatory, lasting eight years and divided into primary (from 6 to 11) and lower secondary schools (from 11 to 14). Transitioning between these stages does not require exams, but a final exam at the end of lower secondary school is needed to move on to the second cycle. The second cycle is divided into two paths: the High Secondary School path, a five-year program offering general, technical, and vocational education for students aged 14 to 19 who have completed the first cycle; and the professional education and training courses, which are three or four-year programs for students who have finished the first cycle. The third cycle comprises higher education, provided by universities, Higher Artistic, Musical, and Dance Education (AFAM), and Higher Technical Institutes (ITS). Compulsory education lasts for ten years, from ages 6 to 16, covering the eight years of the first cycle and the first two years of the second cycle. $^{6}$

## 3. Data Sources and Methods

## 3.1. Administrative data on educational outcomes in Italy

Two administrative data sources represent the backbone of this paper. These are the administrative data obtained from the Ministry of Education (MoE) for academic years 2021-22, 2022-23 and 2023-24, and standardized test score data from the Italian National Institute for the Evaluation of the Educational System (INVALSI) for the 2022-2023 academic year. These datasets offer valuable insights into the educational outcomes of students in Italy, including Ukrainian refugees who entered the Italian school system following the invasion in 2022.

Definitions. In both datasets, students are categorized into five demographic groups based on their nationality and timing of entry into the Italian educational system. These groups are Italian students, Ukrainian refugee students, non-refugee Ukrainian students, newly arrived foreign students, and other foreign students. Among Ukrainian students, the distinction between refugees and non-refugees is based on their enrollment date in the Italian education system. Ukrainian refugees are defined as Ukrainian students who enrolled in Italian schools after February 2022. In this paper, Ukrainian refugees are labeled “Ukr post-Feb 2022”, while non-refugee Ukrainians are labeled “Ukr pre-Feb 2022”. This distinction is also applied to foreign students, with those entering the system after February 2022 referred to as “Migrant post-Feb 2022” and others referred as “Migrant pre-Feb 2022”. $^{7}$

Administrative data from MoE. The Ministry data includes information for all students who enrolled at any point during the academic year. $^{8}$ This information covers academic year, grade, gender, birth date, birthplace, citizenship. They also include school-specific information such as the name and identifying code of the institution where the student is enrolled. Furthermore, the dataset includes a variety of school outcome variables, including grades in English, Italian, Mathematics, overall GPA calculated as the average across all subjects, behavior scores from grade 9 to grade 12, guidance council evaluations from lower secondary school, records of absences, late entries, and early exits.

Given the timing of this study, data for academic year 2022-23 are the most complete. For academic year 2022-2023, school enrollment data at the provincial level was provided for 4,269,348 enrolled students across the 8 years of Italian lower and upper secondary school, encompassing both public and private institutions. The dataset includes nearly all students in the country irrespective of their citizenship. $^{9}$ Table 1 shows the distribution of the different groups of students by grade. In the academic year 2022-2023, 0.2% of students enrolled in the Italian school system were Ukrainian refugees (this share slightly decreases from grade 10 and is negligible in grade 13).

Table 1- Group of students by grade during the academic year 2022-2023 (Source: MoE)

<table><tr><td></td><td>Grade6</td><td>Grade7</td><td>Grade8</td><td>Grade9</td><td>Grade10</td><td>Grade11</td><td>Grade12</td><td>Grade13</td><td>Total</td></tr><tr><td>Ukr post Feb 2022</td><td>1,444</td><td>1,245</td><td>1,263</td><td>1,591</td><td>896</td><td>821</td><td>477</td><td>275</td><td>8,012</td></tr><tr><td>Ukr pre Feb 2022</td><td>1,429</td><td>1,670</td><td>1,757</td><td>1,372</td><td>1,273</td><td>1,160</td><td>995</td><td>900</td><td>10,556</td></tr><tr><td>Migrant post Feb 2022</td><td>10,725</td><td>8,207</td><td>6,871</td><td>16,660</td><td>9,891</td><td>8,859</td><td>6,365</td><td>4,900</td><td>72,478</td></tr><tr><td>Migrant pre Feb 2022</td><td>53,886</td><td>43,939</td><td>44,317</td><td>43,002</td><td>31,905</td><td>30,901</td><td>27,702</td><td>25,195</td><td>300,847</td></tr><tr><td>Italians</td><td>470,319</td><td>495,155</td><td>501,083</td><td>508,873</td><td>484,926</td><td>475,036</td><td>457,203</td><td>486,018</td><td>3,878,613</td></tr><tr><td>Total</td><td>537,803</td><td>550,216</td><td>555,291</td><td>571,498</td><td>528,891</td><td>516,777</td><td>492,742</td><td>517,288</td><td>4,270,506</td></tr><tr><td>Share of Ukr post Feb 2022 over total students</td><td>0.27%</td><td>0.23%</td><td>0.23%</td><td>0.28%</td><td>0.17%</td><td>0.16%</td><td>0.10%</td><td>0.06%</td><td>0.19%</td></tr></table>

Administrative data on enrollment for the academic years 2021-2022 and 2023-2024 are also used to examine the evolution of Ukrainian refugees' enrol

[中间内容因长度限制已省略]

.43</td><td>35.44</td><td>54.66</td><td>316.06</td></tr></table>

Table B7- Summary statistics of Ministry data by group of students (Source: All grades in upper secondary school, a.y. 2022-23)

<table><tr><td></td><td>Obs</td><td>Mean</td><td>Median</td><td>S.D.</td><td>Min</td><td>Max</td></tr><tr><td colspan="7">Group: Ukr pre Feb 2022</td></tr><tr><td>Total absences (days)</td><td>4235</td><td>29.92</td><td>22</td><td>31.15</td><td>0</td><td>203</td></tr><tr><td>Class size &gt; median</td><td>4800</td><td>0.21</td><td>0</td><td>0.41</td><td>0</td><td>1</td></tr><tr><td>Track choice: Professional</td><td>4800</td><td>0.18</td><td>0</td><td>0.39</td><td>0</td><td>1</td></tr><tr><td>Track choice: Technical</td><td>4800</td><td>0.39</td><td>0</td><td>0.49</td><td>0</td><td>1</td></tr><tr><td>Track choice: Lyceum (University-oriented)</td><td>4800</td><td>0.42</td><td>0</td><td>0.49</td><td>0</td><td>1</td></tr><tr><td colspan="7">Group: Ukr post Feb 2022</td></tr><tr><td>Total absences (days)</td><td>2632</td><td>46.13</td><td>30.5</td><td>44.29</td><td>0</td><td>208</td></tr><tr><td>Class size &gt; median</td><td>3785</td><td>0.18</td><td>0</td><td>0.39</td><td>0</td><td>1</td></tr><tr><td>Track choice: Professional</td><td>3784</td><td>0.26</td><td>0</td><td>0.44</td><td>0</td><td>1</td></tr><tr><td>Track choice: Technical</td><td>3784</td><td>0.39</td><td>0</td><td>0.49</td><td>0</td><td>1</td></tr><tr><td>Track choice: Lyceum (University-oriented)</td><td>3784</td><td>0.35</td><td>0</td><td>0.48</td><td>0</td><td>1</td></tr><tr><td colspan="7">Group: Migrant post Feb 2022</td></tr><tr><td>Total absences (days)</td><td>24833</td><td>48.64</td><td>28</td><td>52.55</td><td>0</td><td>212</td></tr><tr><td>Class size &gt; median</td><td>41775</td><td>0.23</td><td>0</td><td>0.42</td><td>0</td><td>1</td></tr><tr><td>Track choice: Professional</td><td>41751</td><td>0.39</td><td>0</td><td>0.49</td><td>0</td><td>1</td></tr><tr><td>Track choice: Technical</td><td>41751</td><td>0.40</td><td>0</td><td>0.49</td><td>0</td><td>1</td></tr><tr><td>Track choice: Lyceum (University-oriented)</td><td>41751</td><td>0.21</td><td>0</td><td>0.41</td><td>0</td><td>1</td></tr><tr><td colspan="7">Group: Migrant pre Feb 2022</td></tr><tr><td>Total absences (days)</td><td>116121</td><td>23.11</td><td>18</td><td>22.71</td><td>0</td><td>271</td></tr><tr><td>Class size &gt; median</td><td>133510</td><td>0.21</td><td>0</td><td>0.41</td><td>0</td><td>1</td></tr><tr><td>Track choice: Professional</td><td>133508</td><td>0.26</td><td>0</td><td>0.44</td><td>0</td><td>1</td></tr><tr><td>Track choice: Technical</td><td>133508</td><td>0.38</td><td>0</td><td>0.49</td><td>0</td><td>1</td></tr><tr><td>Track choice: Lyceum (University-oriented)</td><td>133508</td><td>0.36</td><td>0</td><td>0.48</td><td>0</td><td>1</td></tr><tr><td colspan="7">Group: Italian</td></tr><tr><td>Total absences (days)</td><td>1625408</td><td>23.23</td><td>18</td><td>23.52</td><td>0</td><td>271</td></tr><tr><td>Class size &gt; median</td><td>1926038</td><td>0.21</td><td>0</td><td>0.41</td><td>0</td><td>1</td></tr><tr><td>Track choice: Professional</td><td>1925650</td><td>0.16</td><td>0</td><td>0.36</td><td>0</td><td>1</td></tr><tr><td>Track choice: Technical</td><td>1925650</td><td>0.30</td><td>0</td><td>0.46</td><td>0</td><td>1</td></tr><tr><td>Track choice: Lyceum (University-oriented)</td><td>1925650</td><td>0.54</td><td>1</td><td>0.50</td><td>0</td><td>1</td></tr></table>

Table B8- Main Results for Ukrainian refugees and Newly Arrived students from the current Schengen Area member countries and Western Balkan countries

<table><tr><td rowspan="2"></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td><td>(7)</td></tr><tr><td>INVALSI Maths</td><td>INVALSI English</td><td>INVALSI Italian</td><td>INVALSI Average</td><td>Number of Absences</td><td>Number of Absences</td><td>Recommended for High Track</td></tr><tr><td>Ukrainian Refugee</td><td>-4.479(4.768)</td><td>-16.360*(9.003)</td><td>-11.699***(4.295)</td><td>-9.685**(3.888)</td><td>2.838***(1.083)</td><td>2.034(2.646)</td><td>0.117(0.099)</td></tr><tr><td>Female</td><td>-0.881(2.553)</td><td>5.567(4.086)</td><td>1.787(2.278)</td><td>1.270(2.074)</td><td>-2.947***(0.927)</td><td>-0.322(1.418)</td><td>0.226***(0.043)</td></tr><tr><td>ESCS controls</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>NO</td><td>YES</td><td>YES</td></tr><tr><td>School FE</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>Grade FE</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>NO</td></tr><tr><td>Language</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>NO</td><td>YES</td><td>YES</td></tr></table>

spoken FE

<table><tr><td>INVALSI avg</td><td>NO</td><td>NO</td><td>NO</td><td>NO</td><td>NO</td><td>NO</td><td>YES</td></tr><tr><td>Mean Y</td><td>167.102</td><td>189.005</td><td>147.810</td><td>165.593</td><td>39.264</td><td>24.397</td><td>0.373</td></tr><tr><td>R-square</td><td>0.803</td><td>0.802</td><td>0.825</td><td>0.804</td><td>0.523</td><td>0.851</td><td>0.828</td></tr><tr><td>Obs</td><td>2873</td><td>1851</td><td>2880</td><td>2890</td><td>13242</td><td>2073</td><td>1500</td></tr></table>

Standard errors in parentheses. \* p < 0.05, \*\* p < 0.01, \*\*\* p < 0.001. The models use administrative data from INVALSI and the Ministry of Education for the 2022-23 academic year, including Ukrainian refugees and foreigners arrived in the country after February 2022 and enrolled in Grades 8 through 13. “Ukr Post Feb 2022 is a variable identifying Ukrainian refugees. The “recommended for high-track” variable is relevant for grade 8 only.
"""
