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
![](images/f961a7e6f50ef207774856a9b62115c68a500dfec9c5764dfc8e3e55a80431d6.jpg)

INSURANCE INDUSTRY

# Are Insurers' Talent Models Ready for AI?

By Nathalia Bellizia, Isabelle Cox, Megan Mirabella, and Nadine Moore

ARTICLE JULY 22, 2026 15 MIN READ

Insurers have made real progress in deploying AI across distribution, underwriting, and claims functions—and many are seeing improvements in customer experience, speed, and operational efficiency. But as meaningful as these gains may be, they hide the opportunity for a deeper transformation.

Beyond making routine insurance work more efficient, AI will change the nature of talent within the industry, including such issues as what work will remain for people to perform, how companies will build human expertise, and where accountability will sit. The insurers that win will not be those that deploy AI fastest, but those that proactively redesign talent around it.

The ongoing incorporation of AI into insurance processes is exerting pressure on the traditional insurance talent model. Historically, insurers have built expertise through volume, exposure, and sequential, people-led workflows, with underwriters, claims professionals, distribution teams, managers, and risk leaders connecting fragmented processes.

AI-led workflows will challenge that system in multiple ways. Most notably, they will shift routine execution away from people and concentrate human work on the exceptions, including the judgment, calls, and decisions that demand human ownership. The result will need to be a fundamentally different approach to achieving high-quality decisions. Throughout the workflow, decisions will depend less on individual handling of routine files, and more on the system's built-in logic, controls, and accountability.

In dealing with this new environment, insurers face a choice. One option is to layer AI onto existing workflows and capture incremental efficiency. The other is to redesign the structure of work, the process of decision ownership, and the development and deployment of talent. The gap between those two paths is significant. By BCG's estimate, roughly 70% of AI's potential value comes from change management, adoption, and the redesign of talent and operating models, while only 30% comes from AI tools and technology itself. The implication, already validated by leading insurers, is clear: AI strategy cannot be separated from talent strategy.

## AI Is Replacing Work, Not Automating It

Most insurers currently treat AI as a tool to improve existing workflows—accelerating submission intake, improving claims triage, or guiding distribution decisions. But that view is too narrow. AI’s potential goes far beyond merely upgrading aspects of the current workflow. Increasingly, AI will be able to take over execution itself.

Straight-through processing will become the default method for clear, high-volume requests, with AI capturing and structuring data at the source and embedding guidance directly into decisions and workflows in real time. As a result, humans will largely be removed from routine execution. (See Exhibit 1.)

![](images/c45e35efd8d042d6705d833d68abeb6a05e6d2cbc8e95df11c2625a09d44e4eb.jpg)  
Source: BCG analysis.

## EXHIBIT 1

## How Employees and AI Agents Will Collaborate

## Preclaim

What AI agents do

Monitor risks, predict claims, and recommend mitigation

Engage with customers when risk potential is high, to encourage mitigation actions

Source: BCG analysis.
Note: FNOL = first notice of loss.

## FNOL

Respond to customers, capture key facts, validate coverage, and coordinate support

Provide empathy and validation during initial claim reporting, clarify details, and support intake in complex circumstances

## Triage

Route claims to the appropriate workflow, and improve routing through feedback

Validate AI classifications, and use judgment to route ambiguous or high-risk claims

## Investigation

![](images/1459b779979790aaa9dde665dd0f448082ff05e9480ed783c84cf174ac4d83aa.jpg)

Derive insights from data, estimate losses, and identify gaps for follow-up

Review recommendations, interpret policy in edge cases, and explain decisions to customers

## Negotiation

Support negotiation strategy by surfacing prior insights, and prepare for discussions

Lead complex negotiations with empathy, discretion, and sound judgment

## Resolution

Automate payments, prepare closing documents for approval, and identify next steps

Approve exceptions and escalated payouts to ensure accuracy, compliance, and fairness

## Postclaim

Update risk scores, tailor products, and recalibrate portfolio strategies

Interpret sentiment data, and follow up on dissatisfaction signals to build trust

## The Work That Remains

Human involvement is likely to become increasingly event-driven, focusing on exceptions, ambiguity, and high-stakes decisions. Work will shift away from completing specific tasks and toward owning outcomes, with people overseeing, validating, and intervening in decision systems that run continuously. AI won’t just make existing insurance work faster. It will change the kinds of work that people do. (See Exhibit 2.)

## EXHIBIT 2

How Employees and AI Agents Will Collaborate

Humans orchestrate, supervise, and improve AI agents
Their roles shift to monitoring performance and validating outputs
They manage decision systems rather than execute tasks

Humans intervene when AI cannot decide ...

In underwriting, the current model might require underwriters to review 200 straightforward submissions each month. The future model will have them focus instead on 10 or 15 edge cases that involve novel exposures and unusual characteristics. That work is likely to be more engaging, but also more cognitively demanding and operationally risky. This shift mirrors the difference between general practice and emergency medicine: a general practitioner performs routine check-ups and minor procedures, while the emergency room deals exclusively with high-risk, time-critical cases.

In today's claims model, managers and employees handle every situation. The future model will leverage AI to manage triage and fraud detection in clear-cut cases, freeing employees to work on negotiated settlements, policy ambiguities, litigation scenarios, and cases where understanding the nuances of the claimant's situation is essential to resolution.

In distribution, employees in the future will no longer spend time on data entry. Instead, they will focus on understanding client objectives, anticipating needs before clients articulate them, and structuring solutions that AI-assisted tools can't deliver on their own.

These are not isolated workflow updates. Together, they will collapse the apprenticeship model, concentrate accountability, and make human intervention rarer but more consequential. Without deliberate redesign, the traditional talent model will break.

# Five Ways AI Breaks the Traditional Talent Model

As employees shift from processing routine tasks at volume to owning outcomes, AI will reshape the insurance talent model in five ways, each pulling at a different thread:

\- Expertise will erode. Insurance has long built judgment through repetition and volume. As routine work disappears, the route that junior staff traditionally take to become seasoned experts will vanish. The pipeline will breaks at its foundation: as AI removes routine work, entry-level roles will shrink, cutting off the earliest and most formative stage of judgment development. Insurance will no longer be able to rely on learning by doing, and this will create a structural paradox: expertise will become more valuable at the very time when it becomes harder to build. To act effectively on the decisions that remain, people will need to understand how AI systems reach their conclusions—not as a specialized skill, but as a baseline requirement of the role. Fewer people will handle high-stakes interventions, so the quality of talent will matter more, and the cost of a weak bench will rise with it.

\- Ownership will fragment. When human involvement becomes exception-based, accountability gaps will open quickly in the absence of clear decision rights. For instance, who will own the underwriting decisions that the system makes? Who will be responsible for automated claims outcomes? These questions call for the designation of well-defined owners before decision systems begin to operate continuously.

\- Human work will become more intense. As AI absorbs routine processing, the work that remains for people will grow more complex. It will often involve ambiguity, high stakes, and emotionally sensitive situations. Human involvement is likely to shift toward fewer but weightier moments such as negotiations, contested exceptions, and decisions that set precedents. These roles may be more engaging and have higher value, but they will also be more demanding. Cognitive load will rise as the routine repetitions that once helped people calibrate their judgment fall away. Accountability for a growing share of high-impact decisions will fall on a shrinking number of employees—a combination that, left unmanaged, can breed decision fatigue, judgment inconsistency, and burnout. It might also increase attrition and make roles harder to fill, accelerating the loss of critically important expertise.

\- Accountability will concentrate. As routine decisions become systemic, formal accountability for outcomes will land on a smaller set of workers, even though the decisions will come from models, data pipelines, and controls that no one person operates directly. The span of accountability will widen as direct control narrows. As AI amplifies the reach of individual decisions, human judgment will become a risk vector. Errors will occur less frequently, but their impact will be broader and harder to contain. This evolving situation will increase the importance of traceability. Decisions will need to be observable and explainable even when no individual human is directly executing them. And because each automated decision will scale across thousands of cases, the consequences of any single misjudgment will scale with it, resulting in a growing gap between who is answerable for outcomes and who can actually shape them in the moment.

\- Governance will need to move in real time. Most insurers still govern their performance via after-action review. As AI drives continuous and at scale decision making, however, after-the-fact reviews will not be enough. The lag between a flawed decision and its discovery will become a span across which thousands of cases end up mispriced or mishandled. Consequently, oversight must to move in line with the decisions themselves.

Of these five changes, expertise development matters most. Without a new way to build judgment, the other four will become even harder to manage.

# What Insurers Must Do to Redesign Their Talent

Reacting to these industry shifts in the nature of human work requires four moves: building expertise by design, establishing clear ownership of outcomes, supporting human work, and providing accountability and real-time governance.

Build expertise by design, not assumption. Future insurance professionals will develop their judgment less through volume and more through focused exposure to complex, nonstandard situations. Experience will have to come through a combination of structured mentoring, AI-assisted learning tools, and deliberate rotation across decision types.

Industries where mistakes can be catastrophic already work this way. At nuclear plants, operators may go years without facing a real emergency, so they train relentlessly on realistic simulators to keep their judgment sharp for the rare moment that demands it. This may prove to be the technique used to train new teams and roles in the insurance industry of the future, such as real-time monitoring teams; the deep judgment that these programs produce will provide the crucial—and critically scarce—input that governance will require.

Developing expertise will not be a matter of general upskilling. Rather, it will involve producing the few qualified people needed to sit in those seats. Insurers that invest early will build a sustainable advantage in decision making. Those that do not will find their human staff unprepared in the moments that matter most.

Clearly designate owners as coordination increases. Performance will depend more and more on how well different functions coordinate in real time, not on how well any one of them runs in isolation. Insurers that build tight, continuous coordination across groups will make faster and more consistent decisions at scale. Those that leave ownership ambiguous will see accountability gaps widen as decision volume grows. The key leadership challenge will be to define decision rights end-to-end across the system, not just within individual process steps. Without that clarity, inconsistent decisions and unmanaged exposure will proliferate.

Support human work. As workers shift from executing individual tasks to overseeing systems of decisions, organizations should invest in them accordingly. This means providing them with better tools, stronger decision support, clearer escalation paths, and active management of workloads.

Insurers should also assemble talent and capabilities into integrated decision systems that span functions. When underwriting insights inform distribution, claims patterns improve pricing, and customer interactions shape product design in real time, value will multiply.

Firms that build these systems will move faster, deliver better risk-adjusted outcomes, and achieve a level of responsiveness that fragmented competitors cannot match. However, integration alone will not create that value. Connected systems pay off only when the company has organized people in the right roles to govern them, improve them, and step in when they go wrong.

Promote accountability and real-time governance. Future AI-driven systems will operate continuously and at scale, and governance must evolve with them. The answer is to move from after-the-fact review to continuous, in-line control of decision quality. The most forward-thinking insurers will stand up small, senior, business-owned teams and embed them in each domain to monitor decisions as they occur.

An air traffic control tower offers a useful model. Aircraft follow established routes largely on their own, while controllers watch the whole field from their tower, catching conflicts early and stepping in only when conditions require their intervention.

In the insurance version of this model, each team would combine three roles: a senior business owner who is accountable for outcomes and is empowered to intervene; a domain expert who recognizes when results deviate from expected patterns and decides how to respond; and a data and technology lead who can trace a problem to its root and fix it in the system. The result is governance that can identify and intercept problems in the moment of the decision, rather than reconstructing what went wrong after a flaw has already spread across innumerable cases.

## A Narrowing Window to Act

The window to act is narrowing as AI scales the speed, volume, and complexity of decisions and as the pipelines for experienced underwriting and claims talent weaken. These changes will produce a clear divergence: some insurers will use AI to improve existing models incrementally while others will redesign how they make, own, and govern decisions. Inevitably, the value creation gap between those two groups will compound over time. In many functions, a large share of the workforce is nearing retirement, and insurance is struggling to compete for next-generation talent against industries with stronger pull. Few insurers are thinking about this today—but those that wait will be forced to rebuild expertise in an environment where the apprenticeship model that once fed it is obsolescent.

Leading deliberately means treating talent redesign as a core element of AI strategy, not as a downstream change-management task. Four priorities deserve action now before the constraint becomes a crisis:

\- Redesign how to develop expertise once routine work disappears, using structured exposure, simulation, mentoring, and deliberate rotation across decision types.

\- Define decision ownership across business, technology, and risk, so that accountability remains clear as decisions become continuous and cross-functional.

\- Invest in the sustainability of human work, giving employees the tools, support, and workload management they need to keep their high-strain, high-stakes roles viable.

\- Build real-time, business-owned governance teams to monitor outcomes, diagnose issues, and intervene before flawed decisions can scale.

How a company allocates resources across these priorities will determine how well it competes with its industry peers.

In the near future, the constraint will no longer be what AI can do. It will be whether an organization has a talent model capable of leveraging AI effectively and at scale. Every insurer will have access to powerful AI models and platforms—but how these elements structure work, develop expertise, define decision rights, and govern decisions as human intervention becomes rarer and the stakes of each intervention rise will separate the winners from the also-rans.

Insurers that act early can redesign their talent models with intent. Those that delay will continue to layer powerful technology onto talent structures built for a different era, and they will fall behind faster-moving competitors. In an AI-led insurance model, talent is not merely a supporting capability. Instead, it is the constraint, the risk control, and the source of advantage.

## Authors

![](images/12fe4ec52a09e6a638074c778b4bc64f5e7da2ef45ab331ba0b7e8f305ea8e42.jpg)  
Nathalia Bellizia  
Managing Director & Partner
New York

![](images/a46c5a44e2a9db0a224a8ce852a5ea8fc2a5921121ae7633d3a07895478c6d27.jpg)

![](images/c65d0ae7ff8b5efcfa6eee53c32af4695000dc4be19a2f7bd8dcbf286a97d135.jpg)  
Isabelle Cox

![](images/65a3dbdd1ff3052e233047ca1190743da254d8a36a7b05fc8682dcce25653b36.jpg)  
Managing Director & Partner
New York

![](images/11b5753f2619ab2a4ebe46a1ebff57aa3f66f088f756cd2c9c9ef0a3a7909a26.jpg)  
Megan Mirabella

Consultant
New York

![](images/6a67aec4792c0ba73308a2ce84c734cf69edee263b1f29ad876454002220b8bb.jpg)

![](images/fb70231623215d0fe21287b84c775ca2f50855ad39e4fb734198e1c4f69ac8ff.jpg)

## Nadine Moore

![](images/424704f8d9fa3b89c763225c361378ae756c39297bb4c95724ac004597d30122.jpg)

Managing Director & Senior Partner
Chicago

## ABOUT BOSTON CONSULTING GROUP

Boston Consulting Group bridges the gap between ambition and outcomes for the world's leading companies and organizations. We are built for this era of unprecedented change — bringing strategic clarity rooted in over 60 years of deep domain knowledge, combined with applied AI shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com.
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
