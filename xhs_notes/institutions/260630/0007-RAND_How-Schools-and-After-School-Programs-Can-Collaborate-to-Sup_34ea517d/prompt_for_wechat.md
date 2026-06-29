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
- 已识别机构名：`兰德公司`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份兰德公司研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
ASHLEY WOO, LAUREN COVELLI, SRIKANT KUMAR SAHOO, CATHERINE H. AUGUSTINE

# How Schools and After- School Programs Can Collaborate to Support Academic Alignment

Over recent decades, a heightened focus on standards-based accountability and the federal government's 21st Century Community Learning Centers (21st CCLC) initiative have highlighted the role that after-school programs (ASPs) play in supporting academic achievement (Granger, 2008; Simpson and Olkovsky, 2012). School systems' efforts to respond to pandemic learning losses have only intensified momentum toward leveraging ASPs as an avenue

## KEY FINDINGS

Just over half of surveyed principals with after-school programs (ASPs) agreed that their after-school programming was academically aligned to instruction provided during the school day.

When asked to describe efforts and strategies at their school or district to align school-day and after-school instruction, some principals said that their ASPs had a minimal focus on academics, while others said that their ASPs explicitly reinforced school-day learning through after-school activities.

■ Principals of secondary schools, urban schools, and high-poverty schools were more likely than their counterparts to report that their after-school programming aligned academically to school-day instruction.

■ Principals with school- or district-staff-provided ASPs more often reported that their ASPs academically aligned to school-day instruction than did principals with ASPs provided by an external partner.

■ Principals said that ASPs used tutoring, enrichment activities, and homework help sessions to deliver academic content, although the extent of academic alignment varied within and across these approaches.

Collaborative structures between schools and ASPs, such as shared resources, staff, and data, created conditions that facilitated academic alignment.

for improving academic outcomes (Arundel, 2022; Catolico, 2023; Covelli, Woo, and Augustine, 2026; Grant, 2023).

As schools seek opportunities to bolster student learning, fostering academic alignment between schools and their ASPs has emerged as a promising practice to extend students' learning opportunities. In this report, we define academic alignment as the degree to which after-school programming is coordinated with school-day instruction. We hypothesize that this alignment may manifest through coordination across learning goals, content, instructional strategies, or sequencing—although, in practice, schools may vary in their approaches to and definitions of academic alignment.

Despite a trend toward viewing after-school programming as a venue for academic improvement, studies on ASPs' impact on academic outcomes find mixed results. Some research shows that participation in structured ASPs is associated with small gains in reading and math (Lauer et al., 2006; Granger, 2008; Knopf et al., 2015; Shernoff, 2010; Yao et al., 2023). Other studies show weak or largely null average effects on academics (Zief, Lauver, and Maynard, 2006; Lester, Chow, and Melton, 2020).

Some strategies appear to work better than others. Research suggests that ASPs most effectively support academic achievement, particularly in math and literacy, when intentionally designed around academic goals rather than focused on general supervision, recreation, or homework completion without

## Abbreviations

21st CCLC 21st Century Community Learning Centers
AEP American Educator Panels
ASLP American School Leader Panel
ASP after-school program
CBO community-based organization
K-12 kindergarten through 12th grade
NGCS Next Generation Community Schools
NYC New York City
NYCPS New York City Public Schools
PD professional development
STEM science, technology, engineering, and math

structured support (Knopf et al., 2015; Lauer et al., 2006). Effective approaches include tutoring, targeted skill-building activities, and enrichment models that integrate academic content in engaging ways rather than replicating the school day (Knopf et al., 2015; Lauer et al., 2006; Nickow, Oreopoulos, and Quan, 2024). Student experience also matters: Programs that are engaging, appropriately challenging, and meaningful to students are more likely to lead to academic benefits (Shernoff, 2010). These findings point to the importance of intentional academic integration, in which ASP programming deliberately builds academic skills while leveraging the flexibility and engagement advantages of out-of-school-time settings (Beckett et al., 2009; Granger, 2008).

Yet, the research on academic alignment remains limited (Beckett et al., 2009). Most studies only indirectly address alignment, often pointing to the importance of partnerships, coherence, or intentional design without empirically examining how alignment is implemented or measured (Granger, 2008; Afterschool Alliance, 2014). One recent study, however, points to the potential promise of academic alignment: In this study, researchers found that tutoring aligned to core instruction had a greater positive impact on academic outcomes than non-aligned tutoring (Jackson and Shakeel, 2025), building on prior research demonstrating that strong instructional coherence can improve student achievement (Newmann et al., 2001). Anecdotal reports highlight practices likely to cultivate academic alignment, such as fostering communication between after-school staff and teachers, aligning instructional materials, and reinforcing school-day learning goals (Afterschool Alliance, 2011). Beyond this anecdotal data, we lack information about the extent to which schools are working toward academic alignment or the strategies and school structures that should be in place to better foster this alignment.

This report aims to fill these knowledge gaps by (1) providing national data about the state of academic alignment between school-day and after-school instruction, (2) illustrating at a national level how schools and ASPs put academic alignment into practice, and (3) identifying factors that enable or impede academic alignment. We anticipate that this report will be useful to school and district

leaders and ASP leaders seeking to leverage ASPs to strengthen academic learning, as well as community school leaders who often collaborate with community-based organizations (CBOs) to provide expanded learning opportunities to students.

## Purpose and Approach

During the 2023–2024 and 2024–2025 school years, RAND researchers evaluated the Next Generation Community Schools (NGCS) pilot program, an initiative to enhance academic instruction in 20 New York City (NYC) community schools (Covelli, Woo, and Augustine, 2026). One goal of this pilot program was to support academic alignment between school-day instruction and the after-school programming provided by partner CBOs. RAND's evaluation of this pilot highlighted promising strategies for enacting academic alignment, such as the use of a dedicated staff member responsible for liaising between the school and after-school setting. However, this study also exposed the challenges of putting such a broad concept into practice (Covelli, Woo, and Augustine, 2026).

In our study of the NGCS pilot, we surveyed NYC community school leaders about the extent to which their after-school programming aligned to school-day instruction. For this report, we administered the same survey item to a nationally representative sample of 1,038 kindergarten through 12th grade (K–12) public school principals, which allowed us to extend our prior work in NYC to a national scale.

In this report, we explore

1. the extent to which schools enact academic alignment

2. how principals' reports of academic alignment vary by school context and ASP type

3. how schools enact academic alignment in practice and the factors that support or hamper such alignment.

For the first two topics, we draw on data from closed-ended survey items. For the third topic, we draw on principals' open-ended responses (n = 753) about strategies or efforts at their school or district to align instruction between their school's after-school programming and school-day instruction. Impor-

tantly, we did not provide principals with a definition of academic alignment, which means that they could have interpreted the concept in different ways. For more information about our data and methods, see the “How This Analysis Was Conducted” section at the end of this report.

After presenting findings on whether and how schools enact academic alignment in practice, we provide recommendations on how education leaders can strengthen academic alignment in their contexts.

## Just over Half of Principals with ASPs Agreed That the Programming Aligned Academically to School-Day Instruction

We first asked principals whether after-school programming is available to students at their school and, if so, where it occurs (i.e., off-site or on-site) and who provides it (i.e., school or district staff or an external partner). Seventy-six percent of principals reported that some type of ASP is available to their students. $^{1}$ On-site, school- or district-staff-provided ASPs were most common: 94 percent of principals with ASPs reported the availability of on-site ASPs, and 71 percent reported the availability of school- or district-staff-provided ASPs. In contrast, only 19 percent reported off-site ASPs, and 56 percent reported external-partner-provided ASPs. Percentages sum to more than 100 because principals could report the availability of multiple ASPs.

Among principals with ASPs, about half (52 percent) either somewhat or strongly agreed that their after-school programming aligned to school-day academic instruction (Figure 1). Twenty percent were neutral, and 29 percent disagreed. Because only about three-fourths of principals reported the availability of after-school programming, our data suggest that fewer than half of schools nationally offer an ASP aligned academically to school-day instruction. More often, either schools do not provide an ASP or they provide after-school programming that does not align well to school-day instruction. In the sections that follow, we explore whether princi-

Percentage of Principals Agreeing or Disagreeing That Their After-School Programming Aligns to Academic Instruction Provided During the School Day

![](images/833bdcdf6a9bbc8ba056cb125f436056e8398a010f4b65e9c4347b1d6a4414d8.jpg)  
NOTE: This figure shows principals' responses to the following survey item: "Please specify the extent to which you agree with the following statement: Our afterschool programming is aligned to the academic instruction we provide during the school day." Only principals who had previously indicated that after-school programming was available to students at their school received this survey item. $N = 786$ .

pals' reports of academic alignment vary by school characteristics.

## Principals of Secondary Schools, Urban Schools, and High-Poverty Schools Were More Likely to Report Academic Alignment

Principals' reports of academic alignment increased with grade level (Figure 2). Elementary principals were least likely to agree that their ASP academically aligned with instruction provided during the school day (46 percent), while high school principals were most likely to agree (67 percent). We hypothesize that elementary ASPs may be more likely to focus on play or child care than academics—a point that is further supported by our qualitative data, as we describe

later. In comparison, older students may be more likely to stay after school to seek targeted academic support.

Principals serving high-poverty schools and urban schools were also more likely than their counterparts to agree that their school's ASP is academically aligned to school-day instruction. $^{2}$ Although higher rates of academic alignment may be considered a desirable feature of after-school programming, these patterns may reflect that ASPs for more-vulnerable populations focus more on academics, while ASPs for more-advantaged students may focus more on enrichment. Prior evidence suggesting that students from historically marginalized backgrounds have less access to extracurricular activities, such as art, music, and athletics, supports this hypothesis (Meier, Hartmann, and Larson, 2018; Snellman, Silva, and Putnam, 2015).

## Principals Reporting the Availability of School- or District-Provided After-School Programming Were More Likely to Report Academic Alignment

To determine whether academic alignment was related to (1) where an ASP occurs or (2) who provides the ASP, we explored principals' reports of alignment by ASP type. Principals most often agreed that after-school programming aligned with school-day instruction when their school had an on-site ASP provided by school or district staff (59 percent), followed by an off-site ASP provided by school or district staff (52 percent) (Figure 3). Fewer principals reported academic alignment when external partners staffed the ASP, regardless of whether it was offered on-site (45 percent) or off-site (41 percent). This suggests that staffing ASPs with school or district staff is a stronger predictor of principals' perceptions of academic alignment than location, although academic alignment may be boosted slightly when the ASP occurs on-site.

As we will discuss later, this finding is supported by our qualitative data. Principals' reports suggest that school staff inherently bring knowledge and skills from the school day to the after-school setting that foster academic alignment; conversely, principals may experience more difficulty in influencing an ASP run by an external organization.

Percentage of Principals Agreeing That Their After-School Programming Aligns to Academic Instruction Provided During the School Day, by School Characteristics  
![](images/1c71161e8cb82404f3990f2a051041453dfae54af8a4e6fbf54cdb71acc68c63.jpg)  
NOTE: This figure shows principals' responses to the following survey item: "Please specify the extent to which you agree with the following statement: Our afterschool programming is aligned to the academic instruction we provide during the school day." Data displayed show a sum of principals who responded either "Somewhat agree" or "Strongly agree." Only principals who had previously indicated that after-school programming was available to students at their school received this survey item. This item is shown alongside school characteristics merged in from the National Center for Education Statistics Common Core of Data. Asterisks indicate that the subgroup is significantly different from the reference category ("ref.") at the level of $p < 0.05$ . Black bars represent 95-percent confidence intervals. $N = 786$ .

## Some Principals Said That Their ASPs Have a Minimal Focus on Academics, While Others Said That Their ASPs Explicitly Reinforce School-Day Learning Through After-School Activities

To gain a more concrete understanding of how schools are—or are not—enacting academic alignment in practice, we asked principals to describe strategies or efforts at their school or district to align instruction during the school day and in ASPs. Principals' open-ended responses ( $n = 753$ ) suggest that schools work toward academic alignment to varying degrees, with some principals reporting no efforts

and others reporting extensive efforts to explicitly use ASPs to reinforce school-day learning (Figure 4).

On one end of the spectrum, about one-fifth of principals reported that there were no efforts to align learning occurring during the school day and in ASPs. In most of these cases, principals said that their ASPs were not academic in nature. Notably, three-fourths of these principals were elementary principals, which could explain why, in their closed-ended responses, elementary principals were less likely to report the presence of academic alignment. These principals stated that the ASPs were designed for “child care,” “babysitting,” or play time. Or they said that ASPs included enrichment activities that were meant to be “taken for fun” or that principals perceived as non-academic in nature, such as athletics or art. Some principals (about 45 of them) also noted that their ASPs operate autonomously from their school, meaning that they had no influence over the content of the program. These principals—nearly all of whom indicated the availability of a CBO-run ASP

FIGURE 3

Percentage of Principals Agreeing or Disagreeing That Their After-School Programming Is Aligned to Academic Instruction Provided During the School Day, by Type of ASP Provided

FIGURE 4  
![](images/6f325487daff707161a7ed17b15a978cfcee4c9f37d8ab089c5a35e7036bf1fd.jpg)  
Percentage of principals

NOTE: This figure shows principals' responses to the following survey item: "Please specify the extent to which you agree with the following statement: Our afterschool programming is aligned to the academic instruction we provide during the school day." Only principals who had previously indicated that after-school programming was available to students at their school received this survey item. This item is shown alongside principal responses to the following survey item: "During the 2025-2026 school year, which of the following after-school programming is available for students at your school? Select all that apply." $N = 786$ .

Illustrative Examples of Degrees of Academic Alignment Between Schools and Their ASPs

![](images/4718783bc3f7d6a47c974e23616d615fbaf5dd280cdb635c05022f47e33a0dd7.jpg)

in their closed-ended survey response $^{3}$ —sometimes noted that the organizations running their ASPs had their own curricula and activities. A very small number of principals indicated that, even if the ASP were to integrate an academic focus into its programming, the level of academic rigor would not match that of the school day. Unsurprisingly, most of these principals also disagreed that their ASPs aligned academically to school-day instruction. Overall, principals’ responses indicate a few key barriers to academic alignment, including principals’ attitudes toward the role of ASPs in supporting academics and principals’ lack of influence over the content of after-school programming.

On the other end of the spectrum, other principals described explicit efforts to reinforce school-day learning through after-school opportunities. About one-fourth of responding principals described efforts to use after-school programming as an extension of the school day. These principals said that their ASPs offered students additional opportunities to preview, learn, and practice skills and concepts learned during the school day. A few principals also noted that after-scho

[中间内容因长度限制已省略]

ogram Coherence: What It Is and Why It Should Guide School Improvement Policy,” Educational Evaluation and Policy Analysis, Vol. 23, No. 4, Winter 2001.

Nickow, Andre, Philip Oreopoulos, and Vincent Quan, “The Promise of Tutoring for PreK–12 Learning: A Systematic Review and Meta-Analysis of the Experimental Evidence,” American Educational Research Journal, Vol. 61, No. 1, February 2024.

Shernoff, David J., “Engagement in After-School Programs as a Predictor of Social Competence and Academic Performance,” American Journal of Community Psychology, Vol. 45, 2010.

Simpson, Sarah, and Anna Olkovsky, “A Brief History of 21st Century Community Learning Centers,” Afterschool Alliance, webpage, June 25, 2012. As of April 23, 2026: https://www.afterschoolalliance.org/afterschoolSnack/A-Brief-History-of-21st-Century-Community-Learning-Centers\_06-25-2012.cfm

Snellman, Kaisa, Jennifer M. Silva, and Robert D. Putnam, "Inequity Outside the Classroom: Growing Class Differences in Participation in Extracurricular Activities," Voices in Urban Education, No. 40, 2015.

Yao, Jing, Jijun Yao, Peixuan Li, Yifan Xu, and Lai Wei, “Effects of After-School Programs on Student Cognitive and Non-Cognitive Abilities: A Meta-Analysis Based on 37 Experimental and Quasi-Experimental Studies,” Science Insights Education Frontiers, Vol. 17, No. 1, 2023.

Zief, Susan Goerlich, Sherri Lauver, and Rebecca A. Maynard, "Impacts of After-School Programs on Student Outcomes," Campbell Systematic Reviews, Vol. 2, No. 1, 2006.

## Acknowledgments

We are grateful to the principals who agreed to participate in the panels. We thank Vanessa Miller for serving as the survey manager and Daniel Wang for serving as the data manager for this survey, and we thank Tim Colvin for programming the survey. Thanks to Dorothy Seaman for producing the sampling and weighting for these analyses. We also greatly appreciate the administrative support provided by Tina Petrossian. We are grateful to our partners at the New York City Public Schools Office of Community Schools and the NYC Mayor's Office for Economic Opportunity for supporting this work on academic alignment. We thank Ben Master, Jennifer Leschitz, and Nikki Yamashiro for helpful feedback that greatly improved this report. We thank Nora Spiering for her editorial expertise and Monette Velasco for overseeing the publication process.

## About This Report

In this report, we provide national data about the state of academic alignment between school-day and after-school learning and illustrate at a national level how schools put academic alignment into practice.

We drew on a survey of principals from the American School Leader Panel (ASLP), a nationally representative sample of more than 8,000 principals across the United States. The ASLP is one of three survey panels that compose the American Educator Panels (AEP), which are nationally representative samples of teachers, school leaders, and district leaders across the country. The panels are a proud member of the American Association for Public Opinion Research's Transparency Initiative. If you are interested in using AEP data for your own surveys or analysis or in reading publications using AEP data, please email aep@rand.org or visit www.rand.org/aep.

## RAND Education, Employment, and Infrastructure

This work was conducted in the Education and Employment Program of RAND Education, Employment, and Infrastructure, a division of RAND that aims to improve educational opportunity, economic prosperity, and civic life for all. For more information, visit www.rand.org/eei or email EEI@rand.org.

## Funding

This research was sponsored by New York City's Mayor's Office for Economic Opportunity, in partnership with New York City Public Schools (NYCPS), the Fund for NYCPS, and Robin Hood.

The findings and recommendations we present are solely attributable to us and do not necessarily reflect the opinions of our funders or partners.

For more information on our partners, see the following:

\- New York City's Mayor's Office for Economic Opportunity: https://www.nyc.gov/site/opportunity/index.page

• New York City Public Schools: https://www.schools.nyc.gov/

• Fund for New York City Public Schools: https://www.fundfornycps.org/

• Robin Hood: https://robinhood.org/

RAND is a research organization that develops solutions to public policy challenges to help make communities throughout the world safer and more secure, healthier and more prosperous. RAND is nonprofit, nonpartisan, and committed to the public interest.

## Research Integrity

Our mission to help improve policy and decisionmaking through research and analysis is enabled through our core values of quality and objectivity and our unwavering commitment to the highest level of integrity and ethical behavior. To help ensure our research and analysis are rigorous, objective, and nonpartisan, we subject our research publications to a robust and exacting quality-assurance process; avoid both the appearance and reality of financial and other conflicts of interest through staff training, project screening, and a policy of mandatory disclosure; and pursue transparency in our research engagements through our commitment to the open publication of our research findings and recommendations, disclosure of the source of funding of published research, and policies to ensure intellectual independence. For more information, visit www.rand.org/about/research-integrity.

RAND's publications do not necessarily reflect the opinions of its research clients and sponsors. RAND® is a registered trademark.

For more information on this publication, visit www.rand.org/t/RRA4386-2.

© 2026 The Fund for Public Schools

## www.rand.org
"""
