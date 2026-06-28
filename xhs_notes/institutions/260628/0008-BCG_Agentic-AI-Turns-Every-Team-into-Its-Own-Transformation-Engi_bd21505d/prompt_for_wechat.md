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
- 已识别机构名：`波士顿咨询`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份波士顿咨询研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
![](images/739eb02fd553a34eda4a71c9a959b122b9e2a9334506cf30d8fc3a551657334e.jpg)

AI AGENTS

# Agentic AI Turns Every Team into Its Own Transformation Engine

By Gavin Parker, Caryn Katsikogianis, Alan Wong, Simon Murphy, and Nicole Sibilio

ARTICLE JUNE 19, 2026 12 MIN READ

Agentic AI is exposing an uncomfortable truth: the organisations getting value from it are not the ones with the best technology, but the ones working closely with their teams to redesign how they work.

Caryn Katsikogianis is the former Chief People Officer of Woolworths Group, capping a 25-year career in HR leadership across Australian retail. She reflects here on perspectives drawn from that journey, including conversations with other senior People leaders. Gavin Parker is a Managing Director and Senior Partner at Boston Consulting Group, and Alan Wong is a Partner at BCG, bringing BCG's global perspectives from

supporting clients across industries and geographies on AI transformation. Together, they explore how organisations are scaling agentic AI.

## Introduction

How organisations scale AI is changing how change itself happens. Transformation programs have traditionally been rolled out by a central team in steady, sequential phases. But with AI-led transformations, particularly those drawing on GenAI and agentic AI, many teams across the organisation are being asked to transform — often simultaneously. While it’s widely recognised that AI adoption will lead to some job displacement in the short term, it is also expected to drive net job creation and new forms of work in the near future, increasing the urgency for organisations to adapt how work is designed and delivered.

GenAI has reached 70% adoption in just three years. It’s high on the agenda at every boardroom and management meeting, yet only 16% of Australian executives report significant value from GenAI today. Discussion to date has focused on the technology, but experience shows that organisations derive value from AI only when it is deployed in service of strategic priorities — not treated as a tool confined to the CIO’s toolkit. That shift is already visible in the C-suite: more than 70% of CEOs state that they are now the primary decision-maker when it comes to AI, recognising AI’s role as an enabler of strategy rather than a purely technical capability.

The adoption-value constraint is no longer the technology, but whether teams have the confidence, capability and permission to change how they work to deliver organisational goals. In other words, the bottleneck in AI transformation has shifted from technology to organisational capability.

Generative AI (GenAI) refers to systems that generate outputs from prompts or data, including large language models (LLMs) such as ChatGPT and Claude. Agentic AI extends this capability by enabling systems to autonomously plan, decide and act across multiple steps to achieve an outcome.

While this article focuses on agentic AI, the implications apply to GenAI and even more traditional forms of AI (e.g. machine learning) which are reshaping how teams work.

# Agentic AI Is Changing the Nature of Transformation

Agentic AI is still emerging, but it is already changing how work gets done. Work is shifting from execution to orchestration. Teams are flattening into human-AI structures, changing what it means to ‘manage’. Organisational design, talent and governance are being reshaped in response.

Yet focusing on the adoption of AI is not enough to unlock the full potential of GenAI and agentic AI — what matters is quality adoption of AI to deliver a measurable business outcome. In three stages of AI adoption, Deploy can create immediate value in organisations, but most of the value will come from using AI to Reshape critical functions and to Invent new AI-led experiences.

## Organisations Need to Move Through Three Stages of AI Adoption to Generate Value From Agentic AI

![](images/b8bec31feb9585454ca42bc8ac4489ecc8d0899c0a2fb4e2748a762bc0450808.jpg)  
Incremental adoption to do the same, but better

What does ‘reshape’ look like in practice? A company sets a strategic objective to dramatically scale the volume and personalisation of its marketing. It deploys agentic AI to automate much of the campaign development process, from generating creative assets to tailoring messaging for different audiences and channels. The marketing function then reshapes itself around this new capability, redesigning workflows end-to-end and removing large amounts of manual work. Routine tasks are automated, allowing teams to focus on strategy, creativity and experimentation.

To drive effective, sustained adoption in this context, we need to understand how GenAI and agentic AI are changing how transformation occurs in organisations. Five structural shifts explain why transformation is becoming more distributed and team-led:

\- Work is changing faster than central programs can keep up: Agentic AI capabilities are evolving weekly, if not daily. Recent examples include Anthropic releasing the Mythos-class Claude Fable 5 in June 2026 and OpenAI releasing GPT-5.5 – rebuilt for agentic workflows – in April 2026.

\- Innovation becomes grassroots: Teams can often access generative AI tools themselves, meaning that pockets of innovation are occurring regardless of company guidance. These green shoots can lead to uplifts in effectiveness and efficiency, but also introduce organisational risk if left unaddressed.

\- Transformation multiplies: When nearly every team is affected by agentic AI, transformation no longer scales through a handful of large programs. It scales through hundreds of small, local reinventions happening in parallel.

\- Teams become the engine of change: As agentic transformation starts with rethinking end-to-end workflows in prioritised business domains, change has to run through the teams that hold the expertise. The leadership task is to channel that capability towards the organisation’s key strategic priorities.

\- Roles are re-shaped in real time: Each team is effectively being asked to redesign how work gets done, while still delivering day-to-day outcomes and navigating uncertainty about the future – leading to resistance to change.

Agentic AI does more than improve productivity; it brings transformation closer to teams. Organisations that recognise that teams need to be involved in redesigning their own workflows in pursuit of business outcomes are the ones driving sustainable change. Distributed change does not mean undirected change. The organisations getting real value are not letting every team experiment at once; they are pointing this team-led energy at the two or three domains that move a business metric, and reshaping these domains end to end.

# Agentic in Practice: Insights from an Industry Leader

To close the adoption-value gap, focus on teams before technology and understand how to empower teams to drive change. Bringing this to life is a case study of one global industry leader's journey.

## - Case Study: AWS Software Development Lifecycle Transformation

AWS used GenAI to reshape how software engineering work gets done. The starting point was a familiar challenge: organisations had introduced AI tools to engineers, but usage alone was not changing how work was performed or improving outcomes. Recognising that GenAI can pose a threat to the identity of team members, a core focus of the transformation was helping teams to understand that AI is there to enhance their work by enabling them to spend more time creating and building.

Firstly, AWS linked GenAI adoption directly to business outcomes. “It's not just about the adoption, it's about meaningful usage. Are you deploying code to production and is it making it to customers in the form of features?” This reframed success around impact, rather than simply adoption of tools.

Secondly, the transformation was explicitly team-led, with capability built inside engineering teams by focusing on changing habits, not just enabling access. AWS embedded experienced peer engineers into teams to model new ways of working and reset day-to-day practices, accelerating adoption within the workflow itself.

Finally, AWS is extending this reshape across the full lifecycle. With “about a third of the work due to coding,” the focus is shifting to the processes before and after the coding – the design and the maintenance and ops reinforcing that most of the value will come from using AI to reshape critical functions.

These changes reshaped the role of the developer, reducing manual effort, increasing time spent creating and building, and resulting in 27% more features shipped.

# An Executive Checklist for Empowering Your Teams to Scale AI

Realising value from AI requires a reshape of organisations as transformation shifts from central programs to guided change that unfolds team-by-team. While no silver bullet change playbook exists to navigate transformation with new technologies, a people-led approach can close the gap between adoption and value. Drawing on Caryn's experience as a senior People leader in Australian retail and BCG's global perspectives, we have created a checklist to guide organisations to align agentic AI use cases with business priorities and empower their teams to deliver.

## - 1. Be honest about whether AI actually serves your strategy, or just decorates it

Have you identified the 2–3 domains where AI will move a business metric, not just add activity?

AI is not your strategy, and a wide portfolio of pilots is not a transformation. Your data and AI strategy exists to serve your business strategy. The discipline lies in choosing the two or three domains where AI can materially accelerate a priority, and reshaping those domains end to end. Take a retailer whose priority is getting the right assortment in every store. The place to start is merchandising: take customer data and demand signals, reimagine the workflow from end to end alongside the team, and generate the localised ranges and planograms that store operations will execute. Critically, do this with the team, from category managers through to customer insights and store operations. One domain reshaped properly creates more value than ten explored at the surface.

## 2. Put your CHRO at the centre of the AI agenda,

# as Chief Transformation and Capability Officer

Is there a clear mandate to translate strategy into integrated human–AI structures, or are you relying on technology adoption alone?

Context and culture matter, but they are not enough on their own. Agentic AI puts organisation design at the centre of the AI agenda, and the CHRO is best placed to lead it: actively partnering with business leaders to translate strategy into how teams are structured, flattening hierarchies and orienting these hierarchies around human-AI workflows.

Technology will not do all the heavy lifting; the CHRO's job is to make sure teams are ready, driving the reskilling that reshapes roles as the work changes. This is where HR acts as capability and organisational design architects, helping teams navigate the shift to new ways of working.

## - 3. Treat adoption quality, not access, as the goal

You've handed out the tools; what are you doing to turn adoption into measurable value?

Giving teams a licence is the start of transformation, not the substance of it. Access without governance reliably produces ungoverned workarounds and little measurable value. So roll out productivity tools that let teams experiment, and pair them with AI risk governance strong enough to contain the unauthorised solutions that otherwise accumulate in the gaps. Invest in curated content and genuine AI literacy so people understand what the tools can do and where the risks sit. And build standard, reusable foundations, from identity and access to safe sandboxes, connectors and observability, so teams are not each rebuilding the same plumbing.

## - 4. Separate how you transform from how you run, and protect the difference

Have you invested in the capacity and capability for teams to reinvent their own work, or are you expecting them to innovate in the gaps of the day job?

Transformation bolted onto teams already at capacity tends to fail quietly. But agentic AI means rethinking workflows end to end, so change cannot be handed to a detached central program; it has to run through the teams that hold the domain expertise. The fix is to draw a clear line between running the business and transforming it, and to protect the teams leading that change.

Leadership's job is to give those teams a clear mandate, tie their work to a specific outcome and business metric, and fund the capacity – by backfilling roles or bringing in temporary support – so people can step out of the daily run. That gives them a dedicated build space to focus on reinventing the work.

None of this lands unless leadership frames it as an opportunity, not a burden. For the business, protecting that capacity is an investment in transformation, not an operational cost. For teams, it is an exciting chance to build new skills and design their own future human-AI structures. Framed that way, change becomes not just another tool to adopt, but rather a way for teams to set themselves apart and gain agency in their actions.

## - 5. Make build, buy or partner a deliberate decision, not a default

Do you have a framework for build/buy/partner, or does 'we'll build it ourselves' win by default?

The instinct to build everything internally is often the slowest and most expensive route to value. Better to define an explicit framework for build, buy and

# Close the Adoption-Value Gap with a Team-Led Approach to Agentic AI

If organisations see AI only as a tool to increase productivity, they will miss its full potential. The real value in agentic AI isn't about removing humans from the equation; it's about changing how we work.

Most of the work required to scale agentic AI still lies ahead. Agentic AI will create significant value, but success requires a fundamental evolution in how organisations approach change. Organisations often have deep expertise in programs such as reviewing your customer offer or assessing a new market; rethinking how you embed and transform your organisation with AI will feel a bit like stepping into the unknown for many executives. The only way that executives can address this uncertainty is to allocate sufficient time, resources, and focus to this critical strategic agenda. Organisations that succeed will not just deploy AI; they will institutionalise the capability for teams to continuously redesign how work gets done.

We’ve provided our reflections on how the transformation and change journey needs to evolve with agentic AI; let us know yours.

## Authors

![](images/f55d33fa430f1219aa11be8feb09dc7f168d1810e868bd37d521d449809d7f3c.jpg)

![](images/b5f533f1a95d586513613904772b40f16246cff64b5fecf90469801703260a56.jpg)  
Gavin Parker  
Managing Director & Senior Partner
Sydney

![](images/037664e8f1f3a6d609f237959573ed3d94be7355194d498f496eff7528228b3f.jpg)  
Alan Wong

Partner
Sydney

![](images/c0330288201bd5d7e70f244e279ed7a419412a453e9f81312b976944c0baf65a.jpg)

![](images/98b49fa1544de9cbb5f4240bd8dad0d4f3f4c8a544c615cd6968686d365820c1.jpg)  
Caryn Katsikogianis  
Former Chief People Officer,
Woolworths Group
Sydney

![](images/0acfde5ac1d45ba289e34da39b47b0392aa60251ccb8d5db40059581adea2ff8.jpg)

## Simon Murphy

![](images/308be2646b220910ee7065439b3d5e5753146f1684054f2b842173391703b719.jpg)

Managing Director & Senior Partner
Sydney

![](images/99f82d44881bdd646f2507b77d637d3215d699297e2330fcd278a97b637a8ed7.jpg)

## Nicole Sibilio

![](images/54807e3a3204068c64b95700fd8c9d00d3bb3b6ec2fc448bb695f7d5d1b8f334.jpg)

Managing Director & Partner
Sydney

## ABOUT BOSTON CONSULTING GROUP

Boston Consulting Group bridges the gap between ambition and outcomes for the world's leading companies and organizations. We are built for this era of unprecedented change — bringing strategic clarity rooted in over 60 years of deep domain knowledge, combined with applied AI shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com.
"""
