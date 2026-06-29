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
![](images/d4265b0b6e4a7995ecb7a10aac8064c5d3a76d66cfbe5f3e4e3c9809c3fe1312.jpg)

## The State of Organizations 2026

1 Introduction
2 Three tectonic forces that are reshaping organizations
6 Nine shifts transforming organizations
7 Unlocking the AI-enabled organization
14 Humans and AI agents: Building a new world of collaboration
22 Leveraging AI to rewrite the future of shared services
27 Finding value in a new geopolitical context
35 From structure to flow: Reaching the next productivity frontier
41 Focusing on the core: Doing the right thing with more intensity
46 Aiming higher with a new performance edge
53 Sharpening the focus on diversity and inclusion
57 Reinventing leadership: Leading from the inside out
64 Business as change: Managing continuous transformation in the organization
69 Appendix
71 Authors
72 Acknowledgments

## Contents

![](images/ff643cb876bdcf9ab3ed3b995bae9ac060b85c2e8ca31a49af1879d6477a3603.jpg)

# Three tectonic forces that are reshaping organizations

These are challenging times for organizations everywhere. Continuous disruption is in the air, with forces ranging from artificial intelligence, economic uncertainty, and geopolitical fragmentation to evolving workforce expectations, increasing customer demands, and tougher competitive dynamics redefining how leaders create value and sustain performance.

This report, the second edition of McKinsey's State of Organizations research initiative, seeks to help leaders better understand these dynamics and address them effectively.

The first edition, published in 2023, kicked off our exploration of the most significant people and organizational shifts, including leadership, resilience, talent and resource allocation, and diversity and inclusion (D&I) strategies. This second edition updates our findings to reflect the evolving needs and priorities of organizations. Postpandemic questions about balancing in-person and remote work as well as attracting and retaining talent have given way to a sharper focus on reestablishing high performance and aligning talent around a few bold strategic priorities and must-win battles.

As with the first edition, this latest research draws on a large-scale survey of leaders around the world. In all, we received responses from more than 10,000 senior executives across 15 countries and 16 industries. While leaders remain focused on driving performance, as in the 2023 report, the emphasis has moved from short-term resilience to sustained productivity and long-term impact, powered by technology and AI at the core of organizational transformation.

The survey responses inform our conviction that three tectonic forces are reshaping organizations and will continue to define their success in the years ahead.

The first force is the infusion of technology as automation and data analytics are joined by the burgeoning of AI, both the large language models underpinning generative AI and the advent of AI agents that can be inserted into company workflows. Collectively, these technologies amount to a paradigm shift that promises significant benefits, including productivity gains, faster speed to market, and cost reductions. They are leading organizations to reimagine how work gets done, redefine domains and end-to-end processes, and rethink traditional structures. To harness AI's potential, organizations need to embrace transformative dynamics, seize emerging opportunities—and test, test, test.

The second tectonic force is characterized by the economic disruptions and geopolitical uncertainty that are intensifying as the world becomes more fragmented. To thrive in this evolving landscape, organizations need to adapt swiftly yet sustainably to cope with increasing complexity and potentially rethink their location strategies.

The third tectonic force stems from workforce shifts. Evolving employee expectations, shifting demographics, and new tech-driven working models are transforming the workforce. To remain competitive, organizations need to transcend traditional structures, redefine leadership, and refocus on performance to navigate ongoing disruption.

Our research suggests that these forces are not temporary fluctuations but deep structural transformations that will test how organizations grow, operate, and lead. They are interdependent: AI could liberate organizations from some of the physical location and geopolitical constraints associated with human workers, but it will raise other dimensions of complexity, including how humans and AI agents will collaborate. Their impact is only beginning to unfold: Technology, particularly AI, will accelerate the reorganization of work and value creation; economic disruptions will keep redefining global resilience and competitiveness; and workforce shifts will challenge leadership models and talent systems in new ways.

This report is organized into three sections that reflect these disruptions. In all, we examine nine organizational themes across the three categories of technological, economic, and workforce shifts.

The survey results highlight some important divisions and dichotomies. Just over half of respondents expect changes in the environment to have at least a somewhat positive impact on their organizations in the next one to two years. Leaders with this positive outlook also see their workforce as being energized. Yet 72 percent of leaders tell us that their organizations are not fully ready to face upcoming changes. Even among leaders who are optimistic, only one-third feel prepared.

Overall, the survey shows that leaders are under pressure to achieve further productivity gains. Their primary metrics now are revenue growth or stabilization, cost reduction, and customer satisfaction, rather than cash flow improvement, speed to market, or employee satisfaction and engagement. They need to ensure sustained performance and long-term resilience, including a flexible operating model and the capability to build for the future.

The big takeaway from our latest report, then, is that in an uncertain world, sustained performance and value creation are the priority, ahead of short-term gains.

# While leaders remain focused on driving performance, the emphasis has moved from short-term resilience to sustained productivity and long-term impact, powered by technology and AI at the core of organizational transformation.

## The nine most significant shifts transforming organizations today

## TECHNOLOGY DISRUPTION

## ECONOMIC DISRUPTION

![](images/3ae57aa66e1a02d2a85fc713c90517f21d44df6fb2d99ba2ba52e71eb10a6602.jpg)

## Unlocking the AI-enabled organization

The promise of AI-first operating models is vast, but creating these models can be difficult. While 88 percent of organizations are now experimenting with AI, 81 percent do not report any meaningful bottom-line gains. $^{1}$ To capture the full value, organizations need to go beyond a piecemeal approach and push for a double transformation, both technical and organizational, that includes reimagining how work gets done across functions and workflows.

86% of leaders feel their organizations are not very prepared to adopt AI in day-to-day operations

![](images/8412f7e0f106ef4132bf478aa615916342535e30dfd3a9ae4dbe7d02019ba71e.jpg)

![](images/d067a0d438960b5f3eef923083e89945b4fce2882877729a598189d656295b4d.jpg)

## Humans and AI agents: Building a new world of collaboration

To work well, AI needs to be much more than a plug-and-play tool. AI agents and human employees need to collaborate. That means redefining capability requirements and building human engagement with the technology. The upside: 55 percent of leaders say successfully building AI capabilities of employees will bring exponential productivity gains.

Only one in four leaders expect that AI agents will act as autonomous teammates to employees in the short term

![](images/3a3aede450bcbd8497eada363e22dba1d77dac4380e568be03f06a39b5b0b71e.jpg)

## Leveraging AI to rewrite the future of shared services

As technology reshapes work, shared-services centers are evolving from transactional process hubs into global business-services centers. AI-first by design, these virtual rather than physical centers will orchestrate work between humans and AI agents, unlocking end-to-end automation and driving innovation and insight at scale. The question for leaders is no longer whether to transform but how fast to pivot.

![](images/3d2d29c9cfecb3349d636b37e74b2acd6956264db6dbfe5f1e4e41a366f48d1e.jpg)

84% of leaders plan to expand the scope of their shared-services centers within the next 1–2 years, but more than 40% have yet to start systematically adopting the technologies needed

84%  
![](images/540995bd26f92d493284e718f9edb2ebe1511a484470d0a1f91d9fcfab8c66dc.jpg)

![](images/52a41abd1abdd0633578230b84c224297adb2f6ef54931ff464a238e9293aa93.jpg)

## Finding value in a new geopolitical context

Almost three in four respondents reported that geopolitical uncertainties have had a notable impact on their organizations. As trade shifts to partners in closer proximity, it's more important than ever to build resilient structures and balance global scale with regional adaptability. Organizations need to develop deep-seated flexibility that enables them to bounce forward. Technology—including digital platforms, data analytics, and AI—can help anticipate risks, reallocate resources, and maintain operational agility.

43% of leaders say they divested assets too late or failed to do so when they should have

![](images/10b8603bce2b646f150ac796377ec70c3c36e5226980a91323b87e7162165496.jpg)

![](images/c3e085ed73411bed7c719754513ca34c8d9f5dd678bf8a8f4c45c7c8be53b563.jpg)

## From structure to flow: Reaching the next productivity frontier

Breaking through the productivity ceiling has become a top priority for leaders. To do so means shifting attention away from structure and toward how work gets done. The biggest payoff lies in radically simplifying and unifying processes across the enterprise. That means eliminating duplication, synchronizing information flows, streamlining decision routines, and automating where possible.

Two-thirds of leaders think their organizations are overly complex and inefficient, but traditional remedies relying on structural redesigns, cost cuts, and flatter hierarchies are achieving diminishing returns

![](images/0457c9a7b392b62edb4f2430369bd68d5946f1ef23babb29b4a18a1448ab220c.jpg)

## The nine most significant shifts transforming organizations today

## ECONOMIC DISRUPTION

![](images/98a833b74a298b4cd0f47633739f6ac7280123dbe7d9a0d10e839a420fcf053d.jpg)

## Focusing on the core: Doing the right thing with more intensity

To drive growth, organizations need to identify the strategic portfolio and performance moves that deliver outsize impact. This means selecting a few areas in which to excel, building the governance and capabilities to execute on these priorities, and dynamically reallocating budget and talent to fuel them. Value creation depends on allocating assets across the enterprise. Leaders need the vision to innovate, the discipline to prioritize, and the courage to divest.

## Aiming higher with a new performance edge

## Only 30% of organizations reallocate resources enterprise-wide

![](images/254f1aa380700c955004a50d48290eaa16891f8bb660302039dc18a707e8c78e.jpg)

![](images/85b785231af1bedba5fd3ec88b16d9e6c3e98eb394c47ac01e76172ae7039056.jpg)

Unleashing the full potential of an organization's human capital by focusing on both people and performance can drive strong business results. While many organizations have set the ambition to improve their performance, less than 25 percent successfully achieve sustained impact. Improving over time requires a focus on distinctive organizational capital, including management practices, systems, culture, and, critically, investing in employee health and well-being.

Leaders are still missing the importance of intrinsic motivators, with only 20% believing nonfinancial rewards can instill performance in employees

![](images/6de8e92680dace8a617f3ec2d9c044bd970a77af32b7283e3c5f00e3e8b15979.jpg)

## WORKFORCE SHIFTS

![](images/8e027cbc0115a93c928ac5c3cd746ee3cd5bf9016cd41b558a6fe1da1bcb3498.jpg)

## Sharpening the focus on diversity and inclusion (D&I)

Four in five organizations are maintaining or expanding their D&I efforts despite the shifting landscape. Organizations continue to report their D&I initiatives as a strategic priority that improves outcomes for business, leads to better performance, and contributes to competitiveness. At the same time, they are sharpening their focus on assessing what is working and refining their approaches to deliver meaningful impact.

Nearly half the organizations that scaled back their D&I efforts expect to bring them back to at least some extent in the next 1–2 years

![](images/faf55b998b70a0772cdae201de4a1e5a41cfa957baf913f3f4b25199e92d2358.jpg)

![](images/546a8bf999eb2617bc60d5270ab4ed3874a383708427f7008f96553d507026de.jpg)

## Reinventing leadership: Leading from the inside out

As they seek to balance multiple pressures, leaders today need to take an “inside out” approach focusing on personal growth. That’s a reflection of the two intertwined dimensions of leadership in this age: the idea that leading others also means leading oneself. AI puts even greater emphasis on the human aspects of work and requires more of leaders. Individuals, teams, and organizations need to redefine leadership in more human-centric terms, with leaders reflecting on the “why” to inspire meaningful change.

30% of reflective leaders believe their organizations can quickly adapt to change, versus only 17 percent of non-reflective leaders

![](images/20d6fc6a39069746e795f0b33a445aa9e851eb2b3d3ecb94f666192f746979c7.jpg)

## Nine shifts transforming organizations

7

Unlocking the AI-enabled organization

14

Humans and AI agents: Building a new world of collaboration

22 Leveraging AI to rewrite the future of shared services

27 Finding value in a new geopolitical context

35 From structure to flow: Reaching the next productivity frontier

41 Focusing on the core: Doing the right thing with more intensity

46 Aiming higher with a new performance edge

Sharpening the focus on diversity and inclusion

53

57

Reinventing leadership: Leading from the inside out

![](images/3ef856aaba6aaf87bf88923edbd12b8a790b9ea25f3f4e089d6bfa510630c3a2.jpg)

# Unlocking the AI-enabled organization

While the promise of AI-first operating models is vast, creating these models can be tricky: Less than 20 percent of companies that have tried to adopt the technology have seen significant tangible impact on their bottom lines. Organizations need to go beyond a piecemeal approach to adoption and push for a double transformation: both technological and organizational. This approach means reimagining how work gets done across functions and workflows to shift collective performance and capture the full value.

## Survey highlights

Eighty-six percent of leaders feel that their organizations are not prepared to adopt AI in day-to-day operations.

One in six organizations have no clear C-level owner for AI adoption.

The top three barriers to AI adoption are concerns about AI itself (46 percent); regulatory, ethical, or legal concerns (44 percent); and organizational challenges, including change management (39 percent).

## What's changing?

Adoption of AI in some form is now widespread; McKinsey research suggests that 88 percent of organizations are deploying AI in at least parts of their organizations. However, just as many report no significant bottom-line impact. $^{2}$ In the United States alone, only 1 percent of C-suite respondents describe their generative AI rollouts as mature, and only 19 percent report AI-accelerated revenue increases of more than 5 percent. $^{3}$

Most current efforts to integrate AI focus on fragmented use cases that augment the efficiency of individual contributors. More substantial efforts to embed AI agents to drive productivity in parts of existing processes are either still in the planning stage or being tested in pilot projects. Operational fixes are just the start, however: The future is an AI-enabled operating model design. Enterprise-wide rewiring of companies to become agentic organizations remains a challenge.

Indeed, 86 percent of survey respondents feel that their organizations are not very prepared to adopt AI in day-to-day operations. This is critical considering that one in six organizations we surveyed have no clear C-level owner for AI adoption. Only 14 percent of organizations see leaders consistently championing AI adoption and experimentation with clear strategies and action.

## The benefits of getting it right

The winners will be organizations that think big and transform themselves into agentic enterprises by adopting advanced technology across entire business functions and processes. $^{4}$ The potential is significant: According to the McKinsey State of AI 2025 report, organizations that redesign end-to-end workflows and reimagine entire domains such as marketing and operations see the greatest EBIT impact from their use of generative AI. $^{5}$ But capturing this value depends as much on people as on technology investments—one executive noted that for

Most current efforts to integrate AI focus on fragmented use cases that augment the efficiency of individual contributors. More substantial efforts to drive productivity are either still in the planning stage or being tested.

every \$1 spent on technology, \$5 should be spent on people. $^{6}$

AI agents deliver more than efficiency. They supercharge operational agility and unlock new revenue opportunities, bringing resilience, speed, elasticity, personalization, and adaptability to operations. When they coordinate across multiple agents, they can form a team, and in the future, they

could potentially even design their own workstreams. One example of agentic AI's uses comes from a telecommunications company that created a “next best experience” engine. AI models identified when customers might need help or a better offer and then delivered personalized messages through preferred channels. Human outreach was triggered when needed.

This reduced churn, improved margins, and significantly lifted engagement.

Stakeholders now expect such features. Customers see AI as the new service standard, and employees increasingly expect to experience its benefits in how they work and receive support. Organizations that delay risk falling behind in ways that may be hard to recover from.

Taking these potential benefits into account, leaders in organizations that pioneer AI adopt

[中间内容因长度限制已省略]

eport using data from the latest global McKinsey State of Organizations Survey and interviews with executives at leading organizations. Expert contributors have supplemented that information with existing McKinsey research and insights.

## Methodology

The State of Organizations Survey was conducted from June to September 2025 and received responses from more than 10,000 organizational leaders worldwide. The respondents were leaders and managers from organizations with at least 1,000 employees, spanning 16 countries (Exhibit A1) and representing 17 industries (Exhibit A2).

Exhibit A1

Survey respondents spanned 16 countries.

![](images/49188f28856edbfd28717eec842dbc9d0ea8034a2680d7658a9da596338e7b90.jpg)  
Source: McKinsey State of Organizations 2026 Survey, June to September 2025, n = 10,018  
Exhibit A2  
Survey respondents represented 17 industries.

McKinsey & Company

![](images/eac322a80fafdab66171adf79e47368505c272bafba0a6afa5d542eb2fac2297.jpg)  
Source: McKinsey State of Organizations 2026 Survey, June to September 2025, n = 10,018

McKinsey & Company

We also asked respondents about the themes that are top of mind for them (Exhibit A3).

The data revealed a broad spectrum of top-of-mind themes among today's leaders, with technology disruptions, economic disruptions, and workforce shifts emerging as the top three. Themes centered on performance enhancement were particularly prominent—nearly half (43 percent) of leaders reported focusing on driving performance and creating value within their organizations.

Organization size:

— 1,001–5,000 people: 4,467

— 5,001–10,000 people: 2,011

— 10,001–30,000 people: 1,536

— 30,001–50,000 people: 574

— 50,001 or more people: 1,430

Seniority of respondents:

— Middle management: 5,703

Age group:

— Gen Z (18–26): 270

— Millennial (27–42): 4,740

— Gen X (43–62): 4,765

— Baby boomer (63+): 243

Gender:
— Male: 7,180

— Female: 2,822

— Top management (for example, directors or VPs): 3,250

— Executive team (for example, C-suite): 1,065

— Nonbinary: 6

— Prefer not to say: 10

Tenure in current organization (starting year): — Prepandemic (before 2020): 6,186

— Pandemic (2020–22): 2,238

— Postpandemic (after 2023): 1,594

## Exhibit A3

Survey respondents identified value creation, sustained excellence, and AI-enabled unlocks as top priorities for 2025.

Top organizational priorities for 2025, % of leaders identifying each organizational theme as a top priority (n = 10,018)

![](images/c1d4a4ed098498a44ed02c7dff45ca3f11f06f372e1e279c6a0b273a32599e48.jpg)  
Note: Respondents were asked to select which themes are currently top of mind for them. Source: McKinsey State of Organizations 2026 Survey, June to September 2025, n = 10,018

McKinsey & Company

![](images/15de8cd75a26d057b2c6d28693208b3ed2654b4ce3d0f0681b79fe23884ab641.jpg)

![](images/4093ead301399da9302269d946cf96ed2e196e449128bff431b76abd5317f58a.jpg)  
Amadeo Di Lodovico
Senior Partner, Dubai

![](images/a5a26eca3e1fdf05ce3259d2d593205db57d4aae044e3af525555af5c32e928b.jpg)  
Diana Ellsworth
Partner, Atlanta

![](images/a2275138e8ee4f936ef54167b0e600ee770b23ebc616a31c8cb372f7246e7d30.jpg)  
Dana Maor
Senior Partner, Tel Aviv

![](images/2424bbedae088d3e13775de384f69204c98fc5456dbfa48cbc43b41920a74f1c.jpg)  
Arne Gast
Senior Partner, Amsterdam

![](images/0077d918419eeacae2cdf746b26324445da940a3b14ea7897c5d39ae5ec1e66d.jpg)  
Heiko Heimes
Partner, Cologne

![](images/b20d453fe1b55451e9d050768cb2a8d9bf47c9ffe78fbe5b716a3ef4d97538dc.jpg)  
Alexis Krivkovich
Senior Partner, San Francisco

![](images/97a7cef69de852f2d6d63afc725e2affa05e61d10de56e489f1b1b9493b2889b.jpg)  
Barbara Jeffery
Partner, London

![](images/48ad6edfb6407b93c936d5c1d4629fa2d2556a7e9b144af51a3598c3d19db32b.jpg)  
Liesje Meijknecht
Partner, Amsterdam

![](images/c86777917b11c66e264092259213f78608d793a31bff3b8ed5cf514c4bcb6e4e.jpg)  
Patrick Guggenberger
Partner, Vienna

![](images/21c1d7e93f6aaa85f730542c8a90eac094db5ad1ffd7df7f60c61a6b5829b06c.jpg)  
Brooke Weddle
Senior Partner, Washington, DC

![](images/01d9e8786942be67e8d1a49d0cf982337ee10498e4d35bbbdc060c750986e946.jpg)  
Ramesh Srinivasan
Senior Partner, New York

![](images/708b38e6f837dcd0a4497cde850bc539d0979893e52c349df53840739cd55001.jpg)  
Damian Klingler
Partner, Frankfurt

![](images/cac077b065c8631dbcc1253a2ec4b6aa729b2eeb35c79e2dabcaa80454e9996c.jpg)  
Bryan Hancock
Partner, Washington, DC

![](images/443497d364e33ad2a2511103067fa2885b04645b0f45e1c243ba47a2a5e8a268.jpg)  
Michael Anzenhofer
Associate Partner, Munich

![](images/591dde4f736afcdaf05b42425a28c058a0805bfb385221eead25edb8cc43b5ce.jpg)  
Deepak Mahadevan
Partner, Brussels

![](images/692980854e1b363778ad5cb3b0829fd53125b58fd5ac191329731faac9965348.jpg)  
Sandra Durth
Partner, Cologne

![](images/802d69d577e2ade09dd0a03d610c48050a3ad53fbd4e5230d747974b11b359bf.jpg)  
Ulf Schrader
Senior Partner, Hamburg

![](images/a0ff6150d664866de467612c2f8107130e15c31cb180c7e1c7ec566c0b449f4f.jpg)

## Acknowledgments

The authors wish to thank the following people for their contributions to this report: Alexander Veldhuijzen, Bao Ho, Christen Hammersley, Danny Buchanan, Hiren Chheda, Isabella Lee, Karolina Rosa, Katie Ratcliffe, Kevin Ren, Léo Cornut, Levent Yer, Lisa Paulsen, Logan Luangrath, Malgorzata Kmicinska, Marino Mugayar-Baldocchi, Matt Watters, Max Gleischman, Michelle Kerner, Michelle Lyons, Myriam Nitsche, Natacha Catalino, Nicholle Romero, Nora Fietze, Ola Rusin, Rick Tetzeli, Robert Tesoriero, Sasha Goluskin, Scott Brugmans, Tarek Bakali, Tristan Allen, Yueyang Chen, and Zoe Fox.

State of Organizations 2026
By McKinsey
February 2026
Copyright © McKinsey & Company

www.McKinsey.com

X @McKinsey
f @McKinsey
"""
