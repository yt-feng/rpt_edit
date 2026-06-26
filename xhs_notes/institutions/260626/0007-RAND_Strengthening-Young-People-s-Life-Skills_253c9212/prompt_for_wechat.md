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
# Strengthening Young People's Life Skills

# Practical Guidance and Resources for Intermediaries Supporting Out-of-School-Time Programs

JENNIFER T. LESCHITZ, ALICE HUGUET, CATHERINE H. AUGUSTINE, KATIE TOSH, AND LAURA S. HAMILTON

![](images/8b62ece526eaad2a28beb602378f9ddca960332eaf785f0ff11a29ff9c8e94fb.jpg)

For more information on this publication, visit www.rand.org/t/TLA4416-1.

## About RAND

RAND is a research organization that develops solutions to public policy challenges to help make communities throughout the world safer and more secure, healthier and more prosperous. RAND is nonprofit, nonpartisan, and committed to the public interest. To learn more about RAND, visit www.rand.org.

## Research Integrity

Our research integrity is grounded in RAND's core values of quality and objectivity. Rigorous quality assurance procedures, conflict of interest screening, and transparency in funding ensure that every study is objective and nonpartisan. Learn more at www.rand.org/integrity.

RAND's publications do not necessarily reflect the opinions of its research clients and sponsors.

Published by the RAND Corporation, Santa Monica, Calif.

© 2026 RAND Corporation

RAND $^{®}$ is a registered trademark.

Library of Congress Cataloging-in-Publication Data is available for this publication.

ISBN: 978-1-9774-1610-0

Cover: Photo provided by Monkey Business/Adobe Stock, Eva Kali/Adobe Stock

Interior: page iv-WavebreakMediaMicro/Adobe Stock, page 4-SDI Productions/Getty Images, page 8-Monkey Business/Adobe Stock, page 22-Halfpoint/Adobe Stock, page 24-AnnaStills/Adobe Stock, page 27-Monkey Business/Adobe Stock, page 31-Monkey Business/Adobe Stock, page 36-insta\_photos/Adobe Stock.

Limited Print and Electronic Distribution Rights

This publication and trademark(s) contained herein are protected by law. This representation of RAND intellectual property is provided for noncommercial use only. Unauthorized posting of this publication online is prohibited; linking directly to its webpage on rand.org is encouraged. Permission is required from RAND to reproduce, or reuse in another form, any of its research products for commercial purposes. For information on reprint and reuse permissions, please visit www.rand.org/about/publishing/permissions.

We developed this guide for organizations that support out-of-school-time (OST) providers. In it, we share practical guidance and resources to help OST programs support young people's life skills development.

The Wallace Foundation designed the Partnerships for Social and Emotional Learning Initiative (PSELI) to explore whether and how young people benefit when schools and OST programs partner to improve and coordinate life skills programming, as well as what it takes to do this work. Six communities participated in PSELI: Boston, Massachusetts; Dallas, Texas; Denver, Colorado; Palm Beach County, Florida; Tacoma, Washington; and Tulsa, Oklahoma. We derived the lessons in this guide from our study of more than 100 afterschool programs across these six communities. A companion resource with five editable planning templates is available at www.rand.org/t/TLA4416-1.

## RAND Education, Employment, and Infrastructure

RAND Education, Employment, and Infrastructure, a division of RAND that aims to improve educational opportunity, economic prosperity, and civic life for all, conducted this study in its Education and Employment Program. For more information, visit www.rand.org/eei or email EEI@rand.org.

## Funding

The Wallace Foundation sponsored this research. The Foundation seeks to help all communities build a more vibrant and just future by fostering advances in the arts, education leadership, and youth development. For more information and research on these and other related topics, please visit www.wallacefoundation.org.

## Acknowledgments

We thank the OST program and OST intermediary staff in the six PSELI communities who generously spent their time providing us information about their work. We also thank The Wallace Foundation staff, as well as intermediary organizations in Arizona, Connecticut, Oregon, Pennsylvania, Tennessee, Texas, and Vermont, for carefully reviewing drafts of this guide and helping improve it. We are especially grateful to Ann Stone at The Wallace Foundation for her support and guidance throughout this project. Michelle Bongard contributed to data analysis for this guide. This guide benefited substantively from the careful reviews and constructive feedback provided by our quality assurance manager, Elaine Wang, reviewers Joie Acosta and Anamarie Whitaker, and colleague Andrea Phillips. Finally, we appreciate the Research Editorial and Production team at RAND, including Stephanie Lonsinger, who edited this guide; Katherine Wu, who designed it; and Monette Velasco, who oversaw its production. Any flaws that remain are solely the authors' responsibility.

![](images/4733e6ac3c0227fef5e6d64cdf3eb3f2b2e0186e25122bd7e20a5e3fec342943.jpg)

## Contents

About This Guide....iii

CHAPTER ONE
Overview ....1
Where Life Skills Grow: The Power of OST Programs....2
Inside This Guide....6

CHAPTER TWO
Establishing a Life Skills Framework....9
Understanding Life Skills Frameworks and Their Importance....9
Laying the Groundwork....11
Choosing an Approach That Fits Your Conditions....13
Putting the Framework to Work....18
Planning Your Framework Launch....20
Anticipating Potential Barriers to Adapting or Developing a Framework....22

CHAPTER THREE
Connecting OST Providers to Evidence-Based Resources....25
Helping Providers Put Climate-Building Routines into Action....26
Showing Providers How Life Skills Connect to Program Activities....29
Offering Direct Instruction Resources Designed for the OST Setting....30
Sharing Tools to Measure Progress....33
Anticipating Potential Barriers to Connecting Providers to Resources....34

CHAPTER FOUR
Offering Opportunities for Professional Development....37
Creating a Purposeful Professional Development Sequence....37
Tailoring Professional Development Approaches to Meet Providers’ Needs....42
Ensuring Strong Facilitation....45
Anticipating Potential Barriers to Professional Development....45

## CHAPTER FIVE

Key Takeaways .... 47
Establishing a Life Skills Framework .... 48
Connecting OST Providers to Evidence-Based Resources.... 49
Offering Opportunities for Professional Development.... 50
Anticipating Barriers to Implementation.... 51

APPENDIX A
Featured Resources .... 53

APPENDIX B
Bringing Life Skills into OST Programming: Planning Tools and Samples.... 59
Notes .... 80
Abbreviations .... 83
References .... 84

## COMPANION RESOURCE

Bringing Life Skills into Out-of-School-Time Programming: Planning Tools and Templates
Available at www.rand.org/t/TLA4416-1

## Overview

Young people who have well-developed life skills—such as self-awareness, teamwork, perseverance, and responsible decisionmaking—tend to do better in school, have better health and relationships, and enjoy greater overall well-being than those who do not. $^{1}$ The World Health Organization defines life skills as the “abilities for adaptive and positive behaviour that enable individuals to deal effectively with the demands and challenges of everyday life.” $^{2}$ There is an evidence base for how to help young people develop these skills, and out-of-school-time (OST) programs can play a key role.

This guide aims to help you, as intermediaries—i.e., the organizations that coordinate and support OST programs—assist OST providers in building their capacity to strengthen young people’s life skills development. We offer practical, ready-to-use strategies to help you broaden your network’s impact and improve life skills outcomes for young people.

Building on the work that many intermediaries already do, this guide highlights three ways that you can help OST providers build young people's life skills:

\- Establish a life skills framework to guide programming and practice.

\- Connect providers to evidence-based resources that support effective skill development.

\- Offer opportunities for professional development (PD) to build staff capacity and confidence.

Figure 1.1 illustrates how a life skills framework, PD, and evidence-based resources interconnect to bring life skills into OST programming. The framework provides the foundation, guiding both PD and the selection of evidence-based resources. PD prepares OST providers to apply the framework in their practice. Evidence-based resources, such as practical tools and guides, support this application in everyday programming.

![](images/e4555dc4036982653563a7d92ead1485d57c59e47df62952a5c2b9507db2d2ac.jpg)

## Where Life Skills Grow: The Power of OST Programs

OST programs provide opportunities for fostering positive youth development. They offer young people safe and supportive environments where they can develop relationships with caring adults and peers and engage in activities that help to build important life skills, such as self-control, working in teams, solving problems collaboratively with peers, setting goals, and persisting toward completing them. $^{3}$ Research shows that OST programs can improve outcomes for young people by providing evidence-based life skills training that includes time for skill practice and clear learning objectives. $^{4}$ Parents seem to recognize the important function of life skills: In a 2021 nationally representative survey, parents and guardians ranked social skills, teamwork, and confidence as the three skills most important for their children to develop in OST programs. $^{5}$

## How Intermediaries and Other Coordinating Entities Strengthen the OST Field

We use the term intermediary to refer to any organization that connects and supports OST programs through networking and coordinating tasks. These organizations build the capacity of OST providers by bringing programs together around shared goals, connecting program staff to best practices and instructional resources, providing PD, supporting continuous quality improvement, facilitating partnerships with schools and districts (see the “Learn More: Schools as Partners in Strengthening Life Skills” box), and, in some cases, providing funding.

# A Note on Terminology: Why We Use the Terms “Life Skills” and “Young People”

We choose to use the term life skills in this guide because it encompasses a broad range of behavioral, cognitive, and inter- and intrapersonal competencies that are important for success across multiple domains in life, including school, home, and work. $^{a}$ Life skills include self-management, self-awareness, decisionmaking and problem solving, critical thinking, and communication skills. $^{b}$ Unlike such terms as character skills, workforce readiness skills, or 21st-century skills, which may imply narrower applications or specific contexts, the term life skills reflects the transferable nature of these competencies across settings and in everyday activities and challenges that young people face.

At the same time, we recognize that the definitions of such skills vary by community and professional context. In some places, the term life skills may carry a narrower or different meaning than our broad definition. Wherever possible, we encourage intermediaries to adapt language to the community context, so these concepts resonate with the young people, program staff, families, and other stakeholders with whom you work. Whatever terminology you use, the goal is the same: supporting young people in building skills that help them navigate life's challenges and thrive in the environments and relationships they encounter.

Throughout this guide, we use young people rather than youth because the term encompasses a broader age range, including elementary-aged children. In the literature, the word youth typically refers more narrowly to older adolescents. We still use youth in established phrases, such as youth voice and youth-serving programs. The strategies in this guide (i.e., establishing a life skills framework, connecting providers to evidence-based resources, and offering PD) are relevant for a range of age groups, even though specific examples often focus on elementary-aged children. These strategies can inform work in other youth-serving settings, including schools and community-based programs.

$^{a}$ Danish et al., “Enhancing Youth Development Through Sport.”

$^{b}$ World Health Organization, Department of Mental Health, “Partners in Life Skills Education.”

OST intermediaries can take many forms. These capacity-building roles are not limited to organizations that formally identify themselves as OST intermediaries. Many other youth-serving organizations carry out similar functions; examples include such organizations as the YMCA and the Boys & Girls Clubs of America that oversee multiple program sites or branches within a community; the United Way, which directly funds or partners with OST providers; and city departments that operate OST programs. Cities, municipalities, and school district departments are often essential partners in citywide efforts to strengthen OST programming, and in some cases, they also serve as intermediaries themselves. They can provide public spaces or staffing for programs, bring together stakeholders from different sectors to coordinate initiatives around shared goals, and set supportive policies that advance young people's development. $^{6}$ In addition to those at the local and regional levels, statewide intermediaries can serve as valuable resources, helping establish statewide quality standards and advocating for state-level funding for OST providers.

![](images/ee9782b00932c7b82d416159659a889c0885aa4a37c33d0972040774234e1619.jpg)

OST programs often collaborate directly with schools, and intermediaries can work with districts to facilitate such collaboration. The initiative that underpins this guide was rooted in a partnership-based approach, intentionally linking these two environments in its design and implementation. $^{a}$ Schools are often considered “anchor” institutions in the lives of young people, and collaboration between schools and OST programs can reinforce skills, providing consistent messaging about expectations and norms. $^{b}$ Learners are more likely to build and sustain life skills when they see and practice them in multiple contexts, $^{c}$ making these partnerships important bridges between learning environments.

Partnerships work best when you, as intermediaries, engage schools and districts early—ideally as stakeholders in defining your goals and approach to building life skills—so that priorities and strategies are coordinated from the start. Many districts operate their own OST programs or have existing partnerships, so doing your homework before approaching potential partners is important. Understanding the district’s and schools’ goals, structures, and existing resources can help you identify how your network’s capabilities can complement and extend theirs.

Effective strategies for building and sustaining partnerships include relationship building, learning about each other's organizations, and setting up formal collaboration activities and memorandums of understanding. For example, partnerships might establish committees and regular meetings in which district/school staff and intermediary/OST program staff plan together and agree on shared language and practices. Shared staff-onboarding materials can also help ensure day-to-day consistency across settings.

# When built and maintained with care, partnerships with schools and districts can amplify your life skills work and strengthen a community-wide approach to supporting young people.

There are also challenges in forming and maintaining partnerships. As we found in our study, partnerships can be affected by such factors as leadership changes and differences in decisionmaking power. $^{a}$ Strategies for navigating these barriers include maintaining relationships with staff in various roles at the district, securing broad buy-in from staff, and offering clear value, such as access to quality programming, shared resources, or PD opportunities. When built and maintained with care, partnerships with schools and districts can amplify your life skills work and strengthen a community-wide approach to supporting young people.

We suggest two resources that may be useful to you and/or providers interested in collaborating with school partners:

\- Collaboration tools for schools and OST providers, developed by the Collaborative for Academic, Social, and Emotional Learning (CASEL), include tips for developing a shared vision and a roadmap for building social and emotional learning and for navigating difficult conversations, as well as templates for establishing working agreements. $^{d}$

\- Planning Tool 1: District-Intermediary Partners—Life Skills Coordination Form, created by a school district and intermediary partnership to coordinate their efforts to build young people's life skills, required these partners to define aspects of their work, such as key vocabulary terms, shared guiding principles, and the activities that school and OST program partners would engage in to reinforce the efforts of the other. You will find a completed example of this form in Appendix B and an editable template in the companion resource, Bringing Life Skills into Out-of-School-Time Programming: Planning Tools and Templates, available at www.rand.org/t/TLA4416-1.

## Inside This Guide

We organized this guide around three common functions that you, as intermediaries, can perform to support OST program providers: establishing a shared framework for life skills development (Chapter 2), linking providers to effective resources (Chapter 3), and offering PD opportunities (Chapter 4). We share suggestions and practical examples of intentional approaches to life skills development learned from intermediaries in the six communities where RAND conducted research on this topic: Boston, Massachusetts; Dallas, Texas; Denver, Colorado; Palm Beach County, Florida; Tacoma, Washington; and Tulsa, Oklahoma. Intermediaries in these communities helped OST program providers create high-quality, focused opportunities to foster life skills in elementary-aged children, working in partnership with schools and districts as part of The Wallace Foundation's Partnerships for Social and Emotional Learning Initiative (PSELI).

Using extensive data from our study of PSELI communities, we provide suggestions for how you can approach these three functions to help OST providers focus intentionally on life skills development. While intermediaries engage in many other functions, we highligh

[中间内容因长度限制已省略]

ool-Time Program Partners, Vol. 2, Part 4, RAND Corporation, RR-A379-7, 2022. As of May 1, 2026: https://www.rand.org/pubs/research\_reports/RRA379-7.html

Roeser, Robert W., Summer S. Braun, and Jaiya R. Choles, “Teacher Expertise and Contemplative SEL: Implications for Teacher Professional Development,” in Joseph A. Durlak, Celene E. Domitrovich, and Joseph L. Mahoney, eds., Handbook of Social and Emotional Learning, 2nd ed., Guilford Press, 2024.

Rychen, Dominique Simone, and Laura Hersh Salganik, eds., Defining and Selecting Key Competencies, Hogrefe & Huber Publishers, 2001.

Schwartz, Heather L., Laura S. Hamilton, Susannah Faxon-Mills, Celia J. Gomez, Alice Huguet, Lisa H. Jaycox, Jennifer T. Leschitz, Andrea Prado Tuma, Katie Tosh, Anamarie A. Whitaker, and Stephani L. Wrabel, Early Lessons from Schools and Out-of-School Time Programs Implementing Social and Emotional Learning, Vol. 1, RAND Corporation, RR-A379-1, 2020. As of May 1, 2026: https://www.rand.org/pubs/research\_reports/RRA379-1.html

SEL Dallas, “Find Somebody Who . . . Bingo!” appendix, undated. As of May 1, 2026: https://drive.google.com/file/d/1BGJk02x3D0iJ4DRL5uPz5jO12btVsGeF/view?pli=1

SEL Dallas, “Out of School Time Curriculum Guide,” webpage, undated. As of May 1, 2026:
https://seldallas.org/ost-curriculum/

SEL Dallas, “SEL Dallas Virtual Learning Resources,” webpage, undated. As of May 1, 2026:
https://seldallas.org/sel-dallas-virtual-learning-resources/

SEL Dallas, SEL Dallas Implementation Guidebook, 2020–2021. As of May 1, 2026: https://seldallas.org/wp-content/uploads/2021/04/ SEL-Dallas-Guidebook-2020\_FINAL.pdf

Sheldon, Jessica, Amy Arbreton, Leigh Hopkins, and Jean Baldwin Grossman, "Investing in Success: Key Strategies for Building Quality in After-School Programs," American Journal of Community Psychology, Vol. 45, No. 3, 2010.

Smith, Charles, Tom Akiva, Samantha Sugar, Yun-Jai Lo, Kenneth Frank, Stephen C. Peck, Kai S. Cortina, and Thomas Devaney, Continuous Quality Improvement in Afterschool Settings: Impact Findings from the Youth Program Quality Intervention Study, Forum for Youth Investment, 2012.

Smith, Charles, Gina McGovern, Reed Larson, Barbara Hillaker, and Stephen C. Peck, Preparing Youth to Thrive: Promising Practices for Social & Emotional Learning, Forum for Youth Investment, January 2016.

Stockman, Brandis, “Municipal Support of Out of School Time Programs,” National League of Cities, 2024.

Tosh, Katie, Catherine H. Augustine, and Heather L. Schwartz, Expanding Social and Emotional Learning Beyond the School Walls in Boston: One of Six Case Studies of Schools and Out-of-School-Time Program Partners, Vol. 2, Part 2, RAND Corporation, RR-A379-5, 2022. As of May 1, 2026: https://www.rand.org/pubs/research\_reports/RRA379-5.html

Tosh, Katie, Heather L. Schwartz, and Catherine H. Augustine, Strengthening Students' Social and Emotional Skills: Lessons from Six Case Studies of Schools and Their Out-of-School-Time Program Partners, Vol. 2, Part 1, RAND Corporation, RR-A379-4, 2022. As of May 1, 2026: https://www.rand.org/pubs/research\_reports/RRA379-4.html

Voogt, Joke, and Natalie Pareja Roblin, “A Comparative Analysis of International Frameworks for 21st Century Competences: Implications for National Curriculum Policies,” Journal of Curriculum Studies, Vol. 44, No. 3, 2012.

Weare, Katherine, and Melanie Nind, “Mental Health Promotion and Problem Prevention in Schools: What Does the Evidence Say?” Health Promotion International, Vol. 26, Suppl. 1, December 2011.

World Health Organization, Skills for Health: Skills-Based Health Education Including Life Skills: An Important Component of a Child-Friendly/Health-Promoting School, WHO Information Series on School Health, Document 9, 2003.

World Health Organization, Department of Mental Health, “Partners in Life Skills Education: Conclusions from a United Nations Inter-Agency Meeting,” WHO/MNH/NHP/99.2, 1999.

Young people who have well-developed life skills—such as self-awareness, teamwork, perseverance, and responsible decisionmaking—tend to do better in school, have better health and relationships, and enjoy greater overall well-being than those who do not. There is an evidence base for how

to help young people develop these skills, and out-of-school-time (OST) programs can play a key role.

This guide (and its companion resource) aims to help OST intermediaries, the organizations that coordinate and support OST programs, build OST providers' capacity to strengthen young people's life skills development. It contains practical, ready-to-use strategies and resources to help broaden the impact of OST programs and improve life skills outcomes for young people.

Building on the work that many intermediaries already do, this guide highlights three key ways that intermediary organizations can help OST providers bring life skills into everyday OST programming: (1) establish a life skills framework to guide programming and practice, (2) connect providers to evidence-based resources that support effective skill development, and (3) offer opportunities for professional development to build staff capacity and confidence. The guide also addresses several common challenges raised by intermediaries engaged in this important work.

Whether just beginning to think about a framework or looking to strengthen existing supports, OST intermediaries can use the strategies and resources provided in this guide and adapt them over time to meet evolving needs.

Commissioned by
The Wallace Foundation

www.rand.org

![](images/0d33abe634a1b7652729700cbdabf849131146819b87ee51be479849953c5f7c.jpg)

\$44.00

![](images/3c1797454d550c987d68e9cdb3d9b6a65c41ea0ffa35e9526091223497eb0b74.jpg)
"""
