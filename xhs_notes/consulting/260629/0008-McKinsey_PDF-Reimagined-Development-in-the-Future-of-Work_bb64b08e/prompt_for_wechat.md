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
- 已识别机构名：`麦肯锡`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份麦肯锡研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
Reimagined:

# Development in the Future of Work

2025 Perspective on Evolving Trends in L&D McKinsey's Research and Innovation Learning Lab

# A navigational tool for the trends of tomorrow

It is essential that organizations see development as an act of care, treat resilience and adaptability as a shared responsibility, and embrace transformation not as a future state but as a permanent and positive condition.

In a world defined by constant disruption – economic volatility, geopolitical tension, rapid technological advancement, and widespread organizational change, boundaries are rapidly blurring. Roles, systems, and scopes of influence that once seemed defined or distinct – learning vs operations, people vs technology, work vs life – are now interdependent, overlapping, and inextricably linked. To succeed in this new paradigm, the solutions too must be interdependent.

It’s no longer enough for organizations and individuals to simply bounce back from change or even to establish a new working order. Instead, they must learn to bounce forward, to reimagine how work gets done, how people learn and develop, and how organizations function as resilient, adaptive systems. Doing so requires more than trend-spotting; it requires a commitment to evolving the very models, tools, and mindsets we use to navigate the future of work.

For this reason, we have transitioned this document from a trends digest to a navigational tool. The three themes explored in this report – fluid development ecosystems, responsible AI adoption, and adaptability and resilience – are not standalone topics, nor are the sub-trends that we explore within each. These three macrotrend areas represent fundamental shifts in how people development is defined, delivered, and sustained across organizations.

These trends are mutually reinforcing and cannot succeed in isolation: resilient organizations are better equipped to adopt emerging technologies; technology used wisely can foster connection, creativity, and care; and integrated operating models break down silos to make all of this possible. Together, they demand a holistic, forward-looking approach, one that sees development as an act of care, treats resilience and adaptability as a shared responsibility, and embraces transformation not as a future state but as a permanent and positive condition.

![](images/a6e9feed5719581f030e8b94ad9eacff38b24c363c086d3d401642688d88d657.jpg)

# About the 2025 Learning Trends Perspective

Through an extensive
analysis of trends
disrupting the globe, we
develop a deep perspective
on how these trends will
impact the future of people
development.

The McKinsey Research and Innovation (R&I) Learning Lab reviewed 45+ global trend reports that transcend industries including learning, psychology, HR, tech, finance, geopolitics, travel, and design.

The research team consisted of senior leaders and experts in L&D, People Analytics, Talent Attraction, and McKinsey's People and Organization practice. Following our initial analyses, we clustered commonalities, summarized our detailed data, conducted debates, identified the impact to people development, and constructed our perspectives.

## AI Agent team members

The research team was assisted by AI agents throughout the process and helped in resource identification, clustering, and copy-editing. While the agents were considered thought partners, human team members were responsible for theme and trend selection, developing the perspectives, and writing.

## Our 2025 visuals represent an adaptive, living network

The flowing lines and interconnected spheres reflect the report's themes of integration and progress. The hero image and section dividers showcase dynamic pathways. They symbolize the fluid movement and synergy among people development professionals, as well as the seamless, effective journeys employees will experience when acquiring new skills and knowledge in the future.

This also represents the evolution of development, as it must be adaptive, continuous, and embedded “in the flow of work” to support a rapidly changing landscape.

## Section 2 Responsible AI adoption

# Reimagined development in the future of work

Acting on today's trends, tomorrow's people development organizations will feature fluid development ecosystems, adopt AI responsibly and build resilience and agility for individuals and organizations.

## 1 Fluid development ecosystems

In a world marked by constant change, blurred boundaries, and rising expectations, we must design work to be inherently developmental. Achieving this requires shifting from rigid structures to a dynamic, interconnected ecosystem that uses meaningful data and fosters continuous learning, adaptability, and collaboration. Leaders must:

— De-silo People functions

— Create data-driven development ecosystems

— Make strategic decisions based on meaningful foresight

## 2 Responsible AI adoption

This is a defining moment for the next era of work and learning. But trust is fragile, and mishandling this moment could erode confidence. The path to responsible AI adoption must send a clear message to employees that leaders care about their contributions and are committed to ensuring that AI will help them succeed. Leaders must:

— Preserve employee trust to accelerate AI adoption

— Foster collaboration between humans and AI

— Equip employees with higher-order skills

## 3 Resilient and adaptable individuals and organizations

The organizations that thrive will not be those that resist disruption or merely recover from setbacks, but the ones that anticipate challenges, adapt, and grow. To do this, they must reimagine work environments and build structural and cultural foundations that support adaptability and resilience for their employees. Leaders must:

— Unlock the potential of a diverse, multigenerational workforce

— Support recuperation to ensure sustained performance

— Enable organizational resilience at-scale through sustainable workflows

Section 1

# Fluid development ecosystems

The future of people development offers an opportunity to bring clarity, hope, and progress to the complexities employees and organizations face today.

Employees want a seamless development experience—one that feels natural, supports their growth, and helps them thrive in a rapidly changing world. Development is one of the greatest acts of care employers can provide. Year after year, evidence reinforces that leaders must demonstrate this care not just as an organizational value but as a strategic imperative for long-term success. To achieve this, learning and development must be woven into every aspect of the employee experience—from recruiting to daily work to feedback—transforming work itself into a catalyst for growth.

This requires more than new tools or programs. It demands breaking down silos across people functions, aligning on shared goals, and creating systems that feel frictionless and are integrated to the employee experience. When employees see that these efforts reduce complexity, foster collaboration, and prioritize their growth, they feel supported by their leaders. And when leaders get this right, they unlock resilience, innovation, and sustainable success for their organizations.

![](images/87f5a2bba91e940505b6735868789fb4c50edcc89040b8ad085c1b511e9d37d5.jpg)

## Today

## Real, but not radical, progress towards fluid development

Employees experience more in-the-moment learning support with AI agents playing a growing role - guiding practice, coaching through tasks, and supporting real-time reflection. Skills take center stage, and organizations are starting to move beyond self-reported data, toward a more complete picture of skill validation. Still, learning often feels like something you stop work to “go away and do,” rather than something that happens naturally in the flow of daily activities. Learning is closer to the workflow than it’s ever been before, but it’s not yet embedded.

People development professionals are feeling a growing momentum to break down silos. Teams spot more opportunities to collaborate across L&D, talent, HR, and other people functions, and that shared energy creates ideas for new possibilities.

Despite this progress, L&D still finds itself in a reactive stance, often treated more as a support function rather than a strategic partner. Structures and decision rights continue to reinforce old boundaries. The fences haven't fallen; they've just shifted.

AI augments work in powerful ways, but the real unlock — cohesive, strategic impact— still lies ahead.

## People functions operate as one. Silos dissolve

Growth is the shared purpose of all People functions. The boundary between learning and work has disappeared. The goal is no longer to add learning into the flow of work - it's to merge work and development. Daily work is now designed as a developmental engine. Instead of asking how to encourage employees to make time to learn, organizations are now asking: How do we make daily challenges catalysts for growth?

Employees rarely step away from work to upskill - they grow through the work itself. Tasks are designed to stretch employees, build new skills, and offer just enough challenge without overwhelm. AI copilots act as real-time mentors, adjusting their support based on performance, stress, and cognitive load. Learning is continuous, highly personal, and largely invisible.

Learning teams collaborate with product, operations, and talent to embed growth into workflows. Data and analytics play a central role, helping teams interpret individual performance and progression and adjust the systems and tools in real time. Foresight helps stretch today's work towards tomorrow's skill needs.

# De-siloed people functions

Organizations are striving to become skills-based—using skills as the foundation of talent processes to build a more agile, adaptive workforce. Achieving this vision requires embedding skills development into the flow of work and breaking down silos between HR, L&D, and other people functions to create a unified, skills-centric approach. Yet progress remains slow. A 2023 ATD survey found that while 72% of respondents recognize the importance of transforming HR into a cross-functional discipline, only 11% report meaningful progress. $^{1}$

Breaking these silos down is essential to merging learning and work. This will enable employees to develop skills dynamically as part of their roles. To move forward, organizations must replace fragmented, function-specific processes with cohesive systems that integrate learning, talent, and workforce planning.

Change management is critical: while 83% of leaders believe leadership is key to the skills-based transition, only 28% of employees feel the strategy is being clearly communicated. $^{2}$ Bridging this gap requires active engagement, transparency, and collaboration across all people functions. Ultimately, de-siloing people functions is more than a structural change—it's a mindset shift. By aligning around skills as the currency of the future, organizations can unlock the agility, innovation, and resilience needed to thrive in the rapidly evolving world of work.

![](images/cbd637d9824912bccb49f6f9e16f067a63a1d64070a56de09b462afda14d95e6.jpg)

# Create data-driven development ecosystems

As organizations rethink their operating models, people development must shift from a support function to a strategic business driver. Central to this change is the use of purposeful, actionable data - not just tracking course completions or attendance, but leveraging analytics to understand impact, track growth, and identify skill gaps and high-performing employees. $^{3}$ To stay relevant, L&D must adopt capabilities like predictive modelling and impact visualization, $^{4}$ offering employees personalized insights into their own development and tying learning more directly to business outcomes.

This evolution is powered by a convergence of new technologies (e.g., AI, LLMs), integrated systems (e.g., HRIS), and changing workforce expectations. Learning measurement must move beyond measuring events to becoming full data ecosystems that track what's being learned, how, and toward what goals. When data flows across functions and to the individual, it supports smarter talent decisions and continuous, in-the-flow-of-work development. As people data becomes more integrated, accessible, and reflective of all types of learning, it will help to support more resilient and agile organizations.

![](images/04af56e788253f5cdf1e3dd503c602c2272b6ce42f76a1f3ec70b4067e0c777d.jpg)

# Make strategic decisions based on meaningful foresight

According to the World Economic Forum's Future of Jobs report, 39% of existing skill sets will be transformed or become outdated between 2025 and 2030. $^{5}$ Talent and development professionals are already aware of this ongoing ‘skill instability,’ but the pressure has increased. They’re now responsible for finding, assessing, and validating talent and skills from broader, more complex candidate pools—while also defining the individual value of each new skill, technology, or change their organization adopts. $^{6,7}$ Yet despite this awareness, most organizations remain in a reactive state. 61% still plan their workforce strategy only one year out, $^{8}$ leaving little space for meaningful foresight.

The challenge isn't just predicting what's next, it's making sense of what's emerging and turning those insights into a long-term development strategy. This can no longer be done in silos. People development leaders across functions must collectively shift from short-term forecasting to collaborating based on meaningful foresight. Leaders and teams must build the capability to interpret signals from multiple sources—labor trends, technological shifts, economic changes, geopolitics—and use them to shape development ecosystems that flex, adapt, and grow.

![](images/4cb4d8e6d0db898b97213fa5116b363c99f78b609e38435360b57a305b2436aa.jpg)

"In a tech-powered future, people management will be much more proactive, data-driven, and fluid. Organizations will have the fact base they need to launch interventions such as hiring, insourcing, outsourcing, upskilling, or reskilling. And these interventions themselves will not be one-off activities—rather, the practice of adapting, reallocating, adjusting, and improving will become the norm." 9

McKinsey & Company, February 2025

# Additional evidence that supports the need to build development ecosystems

“Forward-thinking organizations are responding by creating skill-development ecosystems. These new approaches combine formal learning with experiential opportunities, creating more engaging and effective paths to mastery. We see a bright future for organizations that use advanced analytics to anticipate future skill needs. This predictive approach allows them to prepare their workforce proactively rather than reactively, ensuring they stay ahead of industry changes” $^{10}$

85% of people believe that businesses are obligated to “train or reskill” employees so people and societies remain competitive due to global uncertainty and impending AI tech disruptions. $^{11}$

Over the next five years, AI technology could create 11 million jobs globally while displacing 9 million. As technologies advance, similar shifts are likely, increasing the urgency for dynamic reskilling efforts and predictive measures to stay ahead of these changes. $^{12}$

Employees increasingly expect the ability to track their own skill development. Leveraging skill data can enable dynamic learning ecosystems that adapt in real time to both business needs and individual learner profiles. $^{13}$

Cross-border data flow policies can lead to disjointed employee experiences. When policies vary by country, establishing global standards becomes challenging, resulting in inconsistent technology usage and development experiences for employees. $^{14}$

Organizations need a unified data and innovation strategy. As pressure mounts to identify meaningful use cases for AI and other emerging technologies, leaders must avoid impulsive adoption. Instead, they should align a broad set of stakeholders and continuously monitor and identify future tech opportunities that deliver meaningful value. $^{15}$

## How to take action

## People leadership

— Intentionally form cross-functional working teams to solve organization-wide people challenges

— Establish strategic groups to regularly monitor and track labor trends, technological shifts, economic changes, geopolitical strategies, and internal needs

— Develop a collective vision on how aggregating development data (e.g., feedback, skill levels, evaluations) may benefit team staffing, individualized learning opportunities, and systemic workstreams

— Adopt capabilities like predictive modelling and impact visualization for skill development and learning needs

— Champion a skills-first mindset shift across leadership—not just a structural reorganization

## Managers

— Bridge gaps between organizational strategy and employee awareness, as well as between leadership goals and employee sentiment and readiness

— Develop rotational apprenticeship programs so employees can work across functions and build adjacent skills

— Collaborate with formal L&D teams to integrate learning into daily tasks and team interactions

— Provide employees with regular access to their development data and support them in creating personalized plans

## Individual contributors

— Request access to meaningful employment data and seek mentorship—formal or informal—for guidance on building future-focused skills

— Use development insights to make informed decisions about areas to prioritize for future skills growth

— Engage in feedback processes following learning programs or performance evaluation interventions

Section 2

# Responsible AI adoption

This is a defining moment for the next era of how work and learning will be done in an organization.

For years, we’ve been promised personalized learning, curated expertise, and simplified support structures. Yet, employees are still feeling overwhelmed, fatigued by constant change, and unsupported in their development. While people leaders are actively experimenting with AI—building AI agents, forming partnerships, and piloting new features—these efforts may create more complexity for employees rather than delivering clear value.

At its best, AI has the potential to transform people development: streamlining operations, enabling personalized learning at scale, and unlocking higher-order skills. But trust is fragile, and mishandling this moment could erode employee confide

[中间内容因长度限制已省略]

ttps://www.dol.gov/sites/dolgov/files/ETA/opder/DASP/Trendlines/posts/2024\_08/Trendlines\_August\_2024.html#changes-in-the-generational-composition-of-the-labor-force

7. Roy Maurer. "Managing Multi-Generational Communication in the Workplace." January 2, 2025. https://www.shrm.org/topics-tools/flagships/all-things-work/managing-multi-generational-communication-workplace

8. Kate Rockwood. "7 Trends That Will Shape HR in 2025." January 14, 2025. https://www.shrm.org/topics-tools/news/hr-quarterly/7-trends-that-will-shape-hr-in-2025

9. Ellen Bailey and Cevin Owens. "Unlocking the Benefits of the Multigenerational Workplace." 2020. https://www.harvardbusiness.org/wp-content/uploads/2020/08/Unlocking-the-Benefits-of-Multigenerational-Workforces\_Aug-2020.pdf

10. Kelly Pledger Weeks. “Every Generation Wants Meaningful Work — But Thinks Other Age Groups Are in It for the Money.” July 31, 2017. https://hbr.org/2017/07/every-generation-wants-meaningful-work-but-thinks-other-age-groups-are-in-it-for-the-money

11. Hannah Mayer, Lareina Yee, Michael Chui, and Roger Roberts. “Superagency in the Workplace.” January 28, 2025. https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/superagency-in-the-workplace-empowering-people-to-unlock-ais-full-potential-at-work

12. Adam Zaki. "75% of Employees Use AI at Work: Report." May 15, 2024. https://www.cfo.com/news/artificial-intelligence-work-linkedin-microsoft-sap/716095/

13. Ken Taylor and Michelle Eggleston Schwartz. “Trends 2025: Fostering Growth, Resilience and Adaptability.” 2024. https://assets.trainingindustry.com/content/uploads/2024/11/Trends-2025-1.pdf

14. Qualtrics. “2025 Employee Experience Trends.” 2025. https://success.qualtrics.com/rs/542-FMF-412/images/Qualtrics%202025%20Employee%20Experience%20Trends%20Report.pdf

15. Natasha Mutebi and Abbi Hobbs. "The Impact of Remote and Hybrid Working on Workers and Organisations." October 17, 2022. https://post.parliament.uk/research-briefings/post-pb-0049/

16. Anna Medaris. "Work is Reaching a Boiling Point." January 1, 2025. https://www.apa.org/monitor/2025/01/trends-workplace-tensions

## Endnotes

17. Edward Segal. "How Gen Z's Impact on the Workplace Continues to Grow." May 24, 2023. https://www.forbes.com/sites/edwardsegal/2023/05/24/how-gen-zs-impact-on-the-workplace-continues-to-grow/

18. Bryan Robinson. "Job Burnout At 66% In 2025, New Study Shows." February 08, 2025. https://www.forbes.com/sites/bryanrobinson/2025/02/08/job-burnout-at-66-in-2025-new-study-shows/

19. Deloitte. "Workplace Burnout Survey." https://www2.deloitte.com/us/en/pages/about-deloitte/articles/burnout-survey.html

20. Morgan Smith. “Burnout is on the rise worldwide—and Gen Z, young millennials and women are the most stressed.” March 14, 2023. https://www.cnbc.com/2023/03/14/burnout-is-on-the-rise-gen-z-millennials-and-women-are-the-most-stressed.html

21. Dana Maor, Michael Park, and Brooke Weddle. "Raising the Resilience of Your Organization." October 12, 2022. https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/raising-the-resilience-of-your-organization

22. Mike Hesch. "Do Employee Wellness Apps Really Work?" February 11, 2025. https://www.benefitnews.com/opinion/do-employee-wellness-apps-really-work

23. Hamid Biouaraine, Nabil Ridoini, and Benabdelhadi Abdelhay. "Employee Wellbeing in the Workplace: The Role of HR in Mental Health and Wellness Initiatives." October 2024. https://www.researchgate.net/publication/385037597\_Employee\_Wellbeing\_in\_the\_Workplace\_The\_Role\_of\_HR\_in\_Mental\_Health\_and\_Wellness\_Initiatives

24. Chris Mosunic. "Do Workplace Wellness Programs Work? Here's What to Know." February 2025. https://www.calm.com/blog/do-workplace-wellness-programs-work

25. Jacqueline Brassey, Aaron de Smet, and Dana Maor with Sheida Rabipour. “Developing a resilient, adaptable workforce for an uncertain future.” December 6, 2024. https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/developing-a-resilient-adaptable-workforce-for-an-uncertain-future

26. Janelle Beck and Tracey Carney. "The Human Side of Artificial Intelligence: 3 Tips for Navigating the AI Era." September 19, 2024. https://www.everythingdisc.com/blogs/the-human-side-of-artificial-intelligence/

27. Kandi Wein. "How Burnout Became Normal — and How to Push Back Against It" April 23, 2024. https://hbr.org/2024/04/how-burnout-became-normal-and-how-to-push-back-against-it

28. Sarah Barrell and Orla Thomas. "Destination Dupes and Cowboy Core—How Travel Will Look In 2025." December 18, 2024. https://www.nationalgeographic.com/travel/article/2025-travel-trends

29. Workday, Inc. "Workday Global Workforce Report: Restoring Trust Before Your Top People Leave." 2024. https://forms.workday.com/en-us/reports/workday-global-workforce-report/form.html

30. World Economic Forum. "Future of Jobs Report 2025." January 2025. https://reports.weforum.org/docs/WEF\_Future\_of\_Jobs\_Report\_2025.pdf

31. Courtney Rickert McCaffrey, Oliver Jones, and Famke Krumbmüller. “2025 Geostrategic Outlook: How Geopolitics is Driving Global Transformation.” December 12, 2024. https://www.ey.com/en\_us/insights/geostrategy/2025-geostrategic-outlook

32. Jacqueline Brassey, “Thriving Workplaces: How Employers Can Improve Productivity and Change Lives.” https://www.mckinsey.com/mhi/our-insights/thriving-workplaces-how-employers-can-improve-productivity-and-change-lives

## McKinsey & Company

Learning Lab By McKinsey 2025

Copyright © McKinsey & Company

Designed by SJO Design Center

www.mckinsey.com

@McKinsey

@McKinsey

![](images/d30c7201c6e9cbbc44b1449d1ba7a2d858d1569ee12796967c7c773cf08f8691.jpg)
"""
