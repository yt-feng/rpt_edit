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
- 已识别机构名：`波士顿咨询`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份波士顿咨询研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
BCG

![](images/27989b80c5e868da8c91ff2b89127bfc06d8ae44c2555f5bb631f9096539b9fe.jpg)

ARTIFICIAL INTELLIGENCE

# Design Your Company for AI, Not AI for Your Company.

By Nina Kataeva, Vinciane Beauchene, Christoph Hilberath, Kevin Kelley, and Sophie Strelczyk

ARTICLE APRIL 23, 2026 8 MIN READ

AI has advanced at extraordinary speed, triggering a wave of experimentation and investment across industries. Yet the business impact remains limited. BCG research shows that while most organizations are piloting AI, only 5% are capturing meaningful value at scale. The challenge is that most organizations and operating models were built for a purely human workforce, with work structured around functional roles, handoffs, and decision bottlenecks. Simply inserting AI into this model will only deliver incremental gains.

In an AI-first organization, work is no longer organized primarily around human roles and hierarchies, but around connected systems of agents that dynamically coordinate work. Leaders define clear objectives and allow agentic networks to determine how those objectives are achieved. This requires a ground-up redesign of structure and processes, shifting from static, human-centered models to adaptive, AI-driven ways of operating. This allows organizations to create the conditions for AI to evolve and reach its full potential. Below, we outline what leaders need to do to develop an AI-first company and share real-world examples of organizations already delivering measurable impact.

## What It Really Means to Be AI-First

AI-first organizations are designed around a powerful shift: agents are central to how work gets done. That does not mean these companies are not still “people centric.” But while humans define outcomes and provide context, AI agents find the best way to achieve those outcomes via autonomous workflows.

Historically, operating models were designed around fairly unchanging coordination among human roles. Processes were predefined, decision rights were distributed across layers, and execution followed fixed paths. There was a set route to get from point A to point B, and any deviation slowed everything down.

In an AI-first model, humans step into higher-order roles: shaping strategy, setting intent, managing risk, and intervening when judgment, ethics, or accountability is needed. They drive strategic differentiation. And they set the destination, timing, and constraints (available resources, permissions, and the like). Within these parameters, agents continuously and dynamically determine the optimal path forward, adapting in real time while delivering consistent outcomes.

So how do companies become AI-first? The two case studies below show what an AI-first transformation looks like and how organizations are already translating AI-first ambition into measurable results.

## How a European Energy Leader Created an AI-First Operating

## Model

A leading European energy services provider began its AI journey with high levels of urgency and investment. Dozens of AI pilots were launched across customer service, operations, and support. Yet the business impact remained limited.

The operating model—built for a human workforce—included legacy processes and systems that weren’t adapting to AI, which led to fragmented customer journeys, unclear ownership, and a limited ability to scale. Intent on creating an AI-first organization, the company’s leaders made a deliberate shift: rather than inserting AI into existing workflows, they would redesign how work was structured, governed, staffed, and prioritized.

From Scattered Pilots to a Shared North Star. The company’s leaders anchored their AI transformation in a clear two-year vision: reimagining end-to-end customer journeys according to an AI-first model. The future state was made tangible through interactive prototypes and narrative videos that showed how customers would interact with the company in a redesigned, AI-enabled experience. This aligned the organization around an actionable, near-term vision linked to concrete business outcomes.

Organizing Around the Customer, Not Functions. The company's operating model put the customer at the center. Each customer journey determined where agents would be deployed, which AI skills and capabilities were needed, how humans would oversee outcomes or continue to add differentiated value, and how processes, data, and systems needed to evolve. This structure created clarity and cohesion across the company. AI became embedded in the flow of work, not layered on top of it.

Funding the Journey Quickly. The transformation was designed to fund itself. By prioritizing customer journeys that created value quickly, the company generated run-rate savings within the first three months. That early impact validated the approach, unlocked resources, and built confidence to expand the scope. Each redesigned journey generated momentum to fund the next one.

Leadership-Driven Prioritization. The CEO made AI-first one of the company's top strategic priorities. Lower-priority initiatives were paused or cancelled if any resource constraints arose. This made it clear that scaling AI required organizational tradeoffs, strict focus, and alignment.

Ways of Working. Three cross-functional teams worked in parallel, each focused on a high-impact journey. These teams were given a mandate to fully own and transform their portion of the customer journey, and they were equipped with the technical, business, and HR capabilities needed to execute. In this way, they could quickly address roadblocks without consulting with other units and be fully accountable for outcomes.

Results. AI-enabled journeys quickly matched—and are on track to exceed—human performance on customer satisfaction metrics. The company was able to reduce its dependence on external

service providers by more than 90% and free up cash flow that was reinvested in accelerating the AI-first journey. The CEO said that, based on the results of the transformation, “AI is going to be the next major driver of growth for us.”

# A Global Bank's Shift to Human-AI Collaboration at Scale

For a global financial institution, AI represented an opportunity to reinvent how it serves clients, manages talent, and creates value. Early AI pilots showed promise, but their impact was fragmented across functions and value did not materialize in the bottom line. To create impact at scale, leaders had to rethink how humans and agentic AI worked together across every part of the enterprise.

A Bold Vision. The company's leadership set a firm-wide ambition to automate $30\%$ to $50\%$ of workflows and shift human effort to higher-value decisions. This redesign resulted in a lean, intelligent organization where AI does the routine work and humans focus on strategy, orchestrating, and steering.

Central Governance as Anchor. To enable this shift, the organization established a central governance structure. A transformation office owns business alignment and prioritization, while a responsible AI center of excellence sets ethical and compliance standards. A journey-based operating model with cross-functional teams ensures that every initiative links to measurable outcomes. This governance structure ensures enterprise-level alignment and disciplined sequencing, avoiding fragmented experimentation.

Reimagining Core Workflows Along End-to-End Journeys. To reimagine core processes, the company began by redesigning its HR function around the full employee journey. For each stage, it identified more than 80 capabilities where agents could assume core tasks over time. These agents are being rolled out over a three-year timeline, prioritized around key moments in the employee journey and balanced between highest business value and greatest employee benefit. This ensures that automation is applied first to activities that deliver tangible improvements in experience, speed, value, and productivity. Underpinning the transformation is a vertically integrated GenAI platform that combines foundational models, orchestration layers, and specialized agents, all connected through shared data and governance. Digital employee twins enable more precise talent matching, targeted reskilling, and workforce planning.

Redefining the Operating Model and Organizational Structure. The organization redesigned its entire operating model. Work is now organized around small, cross-functional teams that integrate human talent, AI agents, data, and technology to deliver a specific outcome. These teams own employee and client processes end to end, balancing automation, human expertise, and AI-driven insight. Within this model, AI agents execute core tasks across HR and operations, including onboarding, policy support, travel, and learning. Employees are being reskilled to take on new roles—such as AI product owners, model governance managers, and talent data strategists—to ensure that AI capabilities are not layered on, but structurally embedded in the organization.

Results. The bank is on track to automate $30\%$ to $50\%$ of workflows, which will free about three million hours of human capacity—equivalent to 1,700 FTEs—for higher-value work. The program expects full payback within two years and a projected $150\%$ ROI over five years. With strong support from the bank's leadership, AI moved from experiment to everyday practice.

# How to Get Started: Decide Where AI Should and Shouldn't Lead

The fastest way to begin an AI-first transformation is not to launch more AI initiatives but to systematically determine which outcomes should remain human-led and which should be delivered by AI agents.

When setting the ambition, leaders must ask two questions: Could AI do this as well or better than humans? and Should AI do this? (See the exhibit.) The first is a question of performance. Can AI deliver the same level of accuracy, speed, and scale as humans—and is it technically feasible? The second is a question of judgment and strategic differentiation. Will this pose challenges around regulatory risk, customer trust, ethics, safety, and overall impact on the brand? Will this add unique and differentiated value? Together, these questions can help organizations target the right mode of human–AI collaboration.

Two Questions for Assessing Where AI Should and Shouldn't Lead

![](images/be608bc3f53aa59ee8a8bae754c50bbe174bdeaf8dc90583d4f0cd8d4951e3ec.jpg)  
Source: BCG analysis.

Some activities, where trust, empathy, or accountability dominate, will remain human-led. Others will be AI-assisted, accelerating human decision making. And in some cases, AI will lead end to end, executing workflows at scale under human supervision.

The ultimate goal is to rethink end-to-end business outcomes with a focus on autonomous execution (rather than automation layered onto existing work). By making the human–agent collaboration model explicit from the outset, organizations avoid over-automation and under-utilization. They create operating models where humans focus on intent, judgment, and risk, intelligent agents are trusted to deliver outcomes at speed, and the organization is fully aligned around AI-first principles.

From our work across industries, it’s clear that becoming AI-first involves 30% technology and 70% people and organization. If AI is not delivering impact, it is rarely because the technology is not delivering. It is because most organizations have not made the shift from deploying isolated AI tools to redesigning their operating model around human–agent collaboration.

Becoming AI-first is a leadership choice that will redefine competitive advantage across industries. Boards and executive teams must treat this as a strategic redesign of how outcomes are delivered across the enterprise. The first step is deciding where AI should lead, where human judgment creates differentiation, and where human–AI collaboration generates structural advantage.

AI will not wait for your organization to catch up. The gap between leaders and laggards is already widening, driven by operating model decisions rather than technology choices. The leaders in this era won't be those with the best AI tools but those willing to redesign their organizations around an AI-first operating model.

![](images/1543cac2cacab1238a8d950a1ba294ce68c881021914996aa40fe31b27fcca60.jpg)

## Authors

![](images/ff51429d71e704d8c703377595ae10ce2fa89cb5d7d451d797c529071a682f9c.jpg)

![](images/f6bce7d2c8e73a82e080eabe732a72d6da09ebae2f69b899abaf270e7ea4eb3c.jpg)

![](images/9918c08bbabf19b1c1226a18a073f8555ec77996f394ece05bbe6cb2e343f6e9.jpg)  
Nina Kataeva

![](images/6872735b8c3ec985850c054cbfd49f163f97df024b727598f5c295120cbfee62.jpg)  
Managing Director & Partner Zurich

## Christoph Hilberath

Managing Director & Partner Munich

![](images/450c43d8a89e5951b6656308207fd5e92b9ed88ce4df5a4f6d221a59d486c770.jpg)  
Sophie Strelczyk

![](images/6344e92f57116ce8efafac4663d246bfa4c28807532f6a3465d9bd9e9bf50907.jpg)

Principal Hamburg

![](images/efac0888648a963714407ac90c6dbebf87d7f566673224526df2bec152bf3f09.jpg)  
Vinciane
Beauchene

Managing Director & Partner Paris

![](images/7218fa07183de356cf4d342d0eea10bc3ba884f096f75434357f947b7411fec4.jpg)

## Kevin Kelley

Managing Director & Senior Partner, Global Lead for Operating Model, Organization, and Cost
Dallas

![](images/6824fc5a2530ac0dfca0e0ebb4bc0ba23996db8d29901fc4abdc9af3bd43467c.jpg)

## ABOUT BOSTON CONSULTING GROUP

Boston Consulting Group partners with leaders in business and society to tackle their most important challenges and capture their greatest opportunities. BCG was the pioneer in business strategy when it was founded in 1963. Today, we work closely with clients to embrace a transformational approach aimed at benefiting all stakeholders—empowering organizations to grow, build sustainable competitive advantage, and drive positive societal impact.

Our diverse, global teams bring deep industry and functional expertise and a range of perspectives that question the status quo and spark change. BCG delivers solutions through leading-edge management consulting, technology and design, and corporate and digital ventures. We work in a uniquely collaborative model across the firm and throughout all levels of the client organization, fueled by the goal of helping our clients thrive and enabling them to make the world a better place.

© Boston Consulting Group 2026. All rights reserved.

For information or permission to reprint, please contact BCG at permissions@bcg.com. To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on Facebook and X (formerly Twitter).
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
