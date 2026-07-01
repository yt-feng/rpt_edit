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
![](images/cafd0274ec506a851dec70b154c742243c987d0d602f9d5fcf39209818118103.jpg)

ARTIFICIAL INTELLIGENCE

# Return on AI: How CFOs and CIOs Can Manage the Token Meter

By Joppe Bijlsma, Djon Kleine, and Filippo Scognamiglio

ARTICLE JULY 01, 2026 8 MIN READ

This is the second of two articles on the costs of AI tokens and how companies can manage them. The first article examined the true costs of AI. This article details the challenges of measuring them.

The first wave of AI governance was about access. The next wave will be about economics.

As AI moves into production, CFOs, CIOs, and CTOs inherit a big new cost to manage: the tokens consumed to produce business outcomes. To date, the costs associated with tokens, the basic units of data that AI models use, have been largely buried in the IT budget and mostly managed using the principles and procedures of FinOps. But as AI usage scales through the organization—from software development, where it is most advanced, to sales, marketing, operations and other functions—AI token bills are exploding. The rising use of AI agents, which consume tokens in quantity, pushes the meter into overdrive. FinOps cannot keep pace.

CEOs will expect their C-suite colleagues to rise to the challenge. Here's how they can control AI costs and focus the technology on driving outcomes rather than just activity.

# FinOps Is a Starting Point, Not an Answer

FinOps has real strengths. It is good at exposing infrastructure cost, assigning accountability, and optimizing usage. But AI works differently than traditional software as a service, and it changes the unit of management. A token bill depends on a host of factors, including the length of prompts, the context that needs to be retrieved, the quantity of output, choice of model, reasoning effort, choice of tools, cache behavior, and the number of loops an agent runs before it stops.

Token cost is not automatically exponential, and it can vary widely across platforms and models. The key metric to track is not simply cost but cost per outcome. A ratio that we call return on AI (RoAI) is a good way to capture the full cost of the AI being applied:

$$
R o A I = \frac {\text { Economic   return }}{\text { Cost   of   human   Intelligence } + \text { Cost   of   tokens }}
$$

In unmanaged agentic workflows, tokens consumed per useful outcome can compound sharply and invisibly, the result of four forces that interact in ways that traditional software and infrastructure forecasts miss.

The first force is breadth and depth of adoption. Token cost grows as users move from simple chats to multistep research, code generation, agent deployment, and workflow orchestration. The second is task intensity: a short answer, a document review, and a long-running agent session may all look like one request, but each has very different economics.

The third force is context and loops. Agents carry large volumes of information forward, including instructions, history, retrieved documents, and tool outputs, and often replicate them in each loop, which consumes lots of tokens. Fourth is model mix: defaulting to the newest frontier model, the highest reasoning setting, or the largest context window is a design choice with a big billing impact. The inverse can also be true. A weaker model that needs multiple retries to reach an answer can cost more per successful outcome than a stronger model that gets to the same place quickly.

Since unit costs rise linearly with tokens consumed, the right optimization target is cost per successful outcome at the required quality, latency, risk, and additional burden of human review. The challenge is to make this denominator visible and controllable.

# A New Cost Management Operating Model

Token costs do not belong in the IT budget, nor should they be assigned to a single line anywhere in the P&L. Token costs come in three types, and each should be accounted for differently. Tokens that build reusable capability are an investment, similar to capex. When AI is used to design agents, redesign workflows across functions, and—for those that run their own AI inference—provide execution at scale, AI infrastructure is capital expense. Tokens that run internal work are an operating expense. CFOs can set a sensible budget per function and per workflow and hold mangers accountable for the output. Tokens inside a product or customer interaction are cost of goods sold (COGS) and must be managed as part of gross margin, where they can have a significant impact and that impact is fully transparent.

Token cost transparency is especially important for AI-enabled products. The classic economics of software as a service benefited from scale because once the software was licensed, each new customer was added at virtually no cost. AI inference alters the cost curve: each customer interaction carries an associated cost from running the model. Management needs to be able to see the impact on gross margins of absorbing inference at scale, including price, usage, model architecture, caching, and routing.

To accurately account for costs and assess RoAI, companies need a workflow-level operating model that enables management to do three things: see what is happening, shape the cost, and either prove value or stop (or minimize) the activity.

# See: Build Attribution Before Optimization

The quickest path is to start with budget-owner attribution and move toward outcome-level attribution. Every material workflow should be assigned to an owner, function, product-versus-internal use, P&L line, model, provider, and intended outcome. Design a dashboard to track what is happening. The first version can be simple: separate workspaces or projects for each initiative, disciplined API keys, clear product-versus-internal tags, and provider identification.

The dashboard should feature questions that leaders can act on, such as the following:

\- Which workflows consume the most tokens, and what outcomes do they produce?

• What is the cost per successful outcome?

• What share of spending has an assigned owner?

• What is internal opex versus product COGS?

• What percentage of input tokens is cached?

• How much work defaults to frontier models?

Spending without an owner is ungoverned. Spending without a defined outcome is unproven. Spending without an assigned P&L line invites mismanagement.

# Shape: Four Technical and Behavioral Levers

Organizations need to learn how to manage AI and its associated costs, which is probably a joint responsibility of the CIO or CTO and functional and business unit leaders. They should focus on four areas.

Eliminate unnecessary model use. Many early agents exist because they were fast to build, not because a model was the right tool. Structured lookups, rules-based routing, arithmetic, and deterministic policy checks are tasks for software, APIs, or reusable skills, not AI. Routing work to traditional software is itself an effective cost lever, and it often improves reliability as well.

Route by task complexity. Match low-complexity work with lighter or open-weight models, and reserve frontier models for genuinely hard reasoning. Include reasoning effort settings and context window choices in the dashboard, since default settings often overprovide. Let systems autoroute on quality, confidence, latency, and cost rather than sending everything to the strongest model.

Reuse context and components. Prompt caching and batch processing can materially reduce repeated-context and asynchronous workload costs when designed into the workflow. Widely used policies and procedures, such as standard instructions, brand rules, compliance requirements, and common workflows, should become stable, cache-friendly prompt prefixes. They can be included in curated knowledge packs, approved templates, and skill libraries for easy access.

Train for token discipline. Good behavior and discipline lower token costs. Users should learn to ask for the smallest useful answer, constrain output length, avoid pasting unnecessary documents, and distinguish exploration from execution. Interfaces should default to concise outputs, retrieval discipline, and clear stopping rules. Brevity becomes a valuable cost control lever in a metered system.

# Prove, Stop, or Minimize: Govern Return, Not Activity

Leaders should establish a standing review process for the highest-token-consuming workflows. Each review should assess the business numerator (outcome) against the full denominator: token cost plus the human time to initiate, review, correct, approve, and operate the workflow. They can then decide whether to scale up, optimize, rescope, or stop the workflow.

Software engineering shows why this type of review matters. An agentic coding workflow can create a large amount of output at a small token cost, but lines of code are an activity metric. The numerator should count code that is actually shipped and survives review. The denominator should include specification, review, correction, testing, and approval time. The same workflow can be a large positive return or a negative return, depending on how much useful, accepted output it produces and how much human effort it consumes.

The same logic applies outside of engineering. A service agent who closes more tickets but drives more escalations is producing activity rather than return. So is a marketing agent who generates assets that no one uses. The key governance question is not whether AI is busy. It is whether the outcome improved after counting the full cost.

# Savings Can Start Now and Build Over 12 Months

We estimate that companies can substantially improve the efficiency of their AI spending over 12 months by both reducing token costs and achieving more bang from each token, although the range of savings will vary from firm to firm. (See the exhibit.) The key areas of savings opportunity are:

\- Stopping or minimizing avoidable spending

\- Routing work to the right workhorse

\- Caching content to avoid repetitious AI activity

\- Applying the right controls

\- Training staff to increase AI literacy

Companies Can Manage the Cost of Each Successful Outcome

<table><tr><td>Opportunity area</td><td>Lever/What changes</td><td>Impact (improved efficiency of AI bill)</td><td>Pricing mechanic exploited</td></tr><tr><td rowspan="2">Stop or minimizePrevent avoidable spending</td><td>Revisit low-ROI usageReduce avoidable spending by stoppingunnecessary agentic loops</td><td>~5%</td><td>No price change;eliminates unnecessary usage</td></tr><tr><td>Push work out of AI modelsUse deterministic code,rules, and APIs instead</td><td>~2%-5%</td><td>Rules and lookupsreplace billed calls</td></tr><tr><td rowspan="3">RoutePick the right workhorse</td><td>Rightsize and route the modelSend each task to the cheapest modelthat meets the intelligence required</td><td>~3%-8%</td><td>Tiered per-token rate cards</td></tr><tr><td>Rightsize GPUs and self-hostingSelf-host only when usageis steady and high</td><td>~2%-3%</td><td>GPUs bill hourly;APIs bill per use</td></tr><tr><td>Budget output and reasoningCap session length; use frontierreasoning only when needed</td><td>~5%-10%</td><td>Output costs 3x-5x input;reasoning bills as output</td></tr><tr><td>CacheAsk the right questions</td><td>Cache and compact the contextReuse stable openings,system prompts, policies, and knowledge bases</td><td>~3%-12%</td><td>Cached text billsat a fraction</td></tr><tr><td rowspan="3">GovernApply the right controls</td><td>Govern to cost per outcomeAssign every workflow an owner,P&amp;L line, and decision threshold</td><td>~5%-10%</td><td>No price change;enforces spending accountability</td></tr><tr><td>Re-architect the agent flowShare a workspace; pass goals,not full logs</td><td>~5%-10%</td><td>Fewer calls and retries,not a lower price</td></tr><tr><td>Buy at the right rateBatch nonurgent work;commit when steady</td><td>~3%-6%</td><td>Batch ~50% off on-demand;volume discounts</td></tr><tr><td>TrainIncrease AI literacy</td><td>Better use of routing and cachingTrain employees to understandwhat they are trying to achieve</td><td>Drives rapid adoptionof levers above</td><td>Levers covered above</td></tr></table>

Sources: Published cloud and model provider rate cards; Gen AI pricing data; BCG analysis.
Note: Per-token mechanics are based on list prices and do not take into account negotiated discounts; share-of-bill figures are scored estimates that depend on workload mix and are not additive.

Managing Director & Partner
San Francisco - Bay Area

It helps to think in terms of three phases: quick wins (months 1 to 3), big rocks (months 3 to 6), and the longer tail (months 6 to 12). The quick wins fund the big rocks, whose impact is compounded by a longer tail of savings. Companies can gain control over the RoAI denominator with financial impact that accumulates over time.

Token costs are real and growing fast. They are attracting CEO and board-level attention. CFOs, CIOs, and CTOs need to be ready with answers when those leaders start asking questions.

The authors are grateful to these BCG colleagues for their ideas and input: Nicolas De Bellefonds, Abhinav Gupta, Steven Kok, Matthew Kropp, Vladimir Lukic, Clark O'Niell, Rohan Panjwani, and Vikram Srikumar.

## Authors

![](images/b032a03a2a684ed51f32b944c476ccc572a9f0f69aae5c7053e3f4b7d8d6991c.jpg)  
Joppe Bijlsma  
Managing Director & Partner
New York

![](images/6dc0cc475e004ba9d882024922c7ea5640049d1c6687e265b9d507a3c7879e35.jpg)

![](images/21ed207f24fffffd4b9558f30a61b41f6e817f0c6c905a6669b9bb27d1071f50.jpg)  
Djon Kleine

![](images/51c0e7085f05ac6e1baaa082806e9cd06aeb274d8d24a9e96516d5630c246a4b.jpg)

![](images/958f2f22b3ef2dbe784436db8a69df94c82f2186f4441e677881678d283711ac.jpg)

## Filippo Scognamiglio

Managing Director & Partner; BCG Henderson Institute Functional Leader; Global Cloud Advisory Business Leader New York

![](images/7324c5ccd8078edb4f38b7520006800cc3ecf160a137f41a228015ff90655106.jpg)

## ABOUT BOSTON CONSULTING GROUP

Boston Consulting Group bridges the gap between ambition and outcomes for the world's leading companies and organizations. We are built for this era of unprecedented change — bringing strategic clarity rooted in over 60 years of deep domain knowledge, combined with applied AI shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com.
"""
