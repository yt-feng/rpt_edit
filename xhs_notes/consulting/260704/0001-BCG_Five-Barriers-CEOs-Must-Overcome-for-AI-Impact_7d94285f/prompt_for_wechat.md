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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份波士顿咨询研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
![](images/ce0206988f53f78c22179da766225df5542a4e0965f95daf32c043cd4d2eca6e.jpg)

BUSINESS TRANSFORMATION

# Five Barriers CEOs Must Overcome for AI Impact

By Matthieu Berthion

ARTICLE MARCH 26, 2026 8 MIN READ

AI's capabilities are inestimable, its transformative potential seemingly limitless. Unfortunately, few CEOs are getting AI transformation right. Recent BCG research shows that only $5\%$ of companies are generating sustained P&L impact while roughly $60\%$ have seen little or no material benefits.

AI initiatives fail not because of technology but because leaders apply weak transformation discipline. At the same time, AI transformations differ from other transformations in two ways.

\- AI delivers visible results quickly, creating the impression of fast progress. However, the deeper work—rewiring decision rights, reshaping how expertise is applied, and realigning incentives across the value chain—is obscure, more difficult, and often missed.

\- Much of AI's impact is indirect. It improves judgment, productivity, and insight, but the financial effects are second-order and fragile unless deliberately captured.

This combination of early visibility, systemic disruption, and indirect value makes AI uniquely prone to underperformance.

CEOs who stand to turn AI into financial value are those who apply proven, if unglamorous, transformation discipline. They can start with steering their organizations past five common barriers to AI success.

## Barrier #1: Piecemeal Poking at the Problem

AI is nearly everywhere now, with 90% of companies experimenting with it at a minimum, according to various reports. The problem is that companies stay too long in the experimental stage, taking baby steps with limited productivity gains. While many are intimidated by AI because of cost, complexity, and potential risk, fragmented efforts lack the scope and level of integration to provide lasting P&L impact.

The companies that are achieving value are the ones that embrace the need for bold reinvention. According to BCG estimates, roughly 70% of AI's value potential is concentrated in core business process workflows, where decisions, costs, and outcomes intersect. One way around the small-scope barrier is for the CEO to drive the organization's AI efforts, seeking deliberate and deep ways to reinvent areas of the business. CEOs can also use AI agents to help move beyond automation of isolated steps and instead rebuild value chains around business outcomes, from the ground up, allowing systems to adapt dynamically to achieve business goals. Without this AI-first orientation, AI remains incremental rather than transformative.

# Barrier #2: Underfunding Means Underachievement

Corporations expect to nearly double AI spending in 2026, yet many CEOs underestimate the scope of the investment required. AI's impact is cross-functional by nature. Its reach extends well beyond the technology function to data foundations, integration, operating model changes, and workforce enablement.

The illusion of early success often causes leaders to limit funding before the transformation is complete. Getting from 70% performance to 95%—the last mile, where impact becomes structural—is critical. That requires a disproportionate effort and investment to strengthen data foundations, industrialize processes, resolve cross-functional interdependencies, and embed responsible AI and risk controls. The impressive results obscure the scale of the real investment required. The result is a broken cash flow curve that deprives the effort of financial fuel before impact is realized.

CEOs can help overcome this by enabling financial support for the profound reinvention of workflows that is needed. It’s a commitment that requires a greater level of effort, time, hard trade-offs, and investment than many leaders anticipate.

## Barrier #3: No Value-First Blueprint

AI initiatives often fall short because leaders do not define, from the outset, how value will be created. Instead, they focus on visible productivity improvements within functional or process silos. While these gains may be real, they are not the same as revenue growth, structural cost reduction, margin expansion, or balance sheet impact. Without a clear economic blueprint, operational improvements remain disconnected from financial performance.

In practice, when no explicit value logic has been defined, 10%–20% of anticipated value typically erodes before reaching the P&L. The issue is not that AI lacks potential, but that the pathway from local efficiency to enterprise-level impact has not been designed.

CEOs must articulate a value-first blueprint before developing any AI initiative. This means identifying the precise P&L and balance sheet lines that will be impacted, quantifying targets, and assigning clear ownership for each source of value. To achieve expected financial benefits, leaders must map the steps and interdependencies—including adjacent functions and processes—from each impacted workflow to the P&L lines where value is realized.

This is a matter of financial architecture, not technology deployment. The CFO, the finance function, and the transformation office should play a central role in defining the value logic and embedding economic rigor from day one. AI does not create value by default. It creates potential. Converting that potential into measurable financial performance requires deliberate design.

# Barrier #4: Tracking Motion, Not Results

Even when a value-first blueprint exists, many leaders fail to install the mechanisms required to deliver and protect that value over time. Initial ambitions are clear, but the execution discipline is not. Without rigorous tracking, forecasting, and accountability embedded in performance management, value erodes quietly.

The most common failure is an overreliance on operational indicators. Tracking dashboards fill with impressive activity metrics, productivity measures, and tool adoption rates. Yet these do not automatically translate into economic outcomes. When KPIs are not explicitly linked to P&L impact, leaders gain visibility into motion rather than performance.

The consequences are predictable. Baselines remain unclear. Metrics shift over time. One-off improvements are mistaken for structural gains. Without forward-looking forecasts tied to financial lines, management cannot distinguish temporary uplift from sustainable impact. Confidence declines, and course correction becomes reactive rather than deliberate.

A value protection system requires more than reporting. It requires governance. This governance must sit within a formal, multidisciplinary transformation office—bringing together finance, technology, operations, HR, and risk—to coordinate execution, resolve trade-offs, and maintain accountability across functions. P&L-connected KPIs must be defined and reviewed at the appropriate level of leadership. Clear accountability for each value lever must be embedded in incentives and operating reviews. Stage gates should act as decision checkpoints to enforce the quality of business cases and operational plans and confirm that operational improvements are converting into financial results before additional capital is deployed.

AI transformations are no different from other enterprise transformations in this respect. Value must be protected during execution. Without systematic tracking, disciplined governance, and economic accountability, even well-designed initiatives drift.

# Barrier #5: Not Focusing on How People Use the Technology

Many leaders assume that AI transformations are difficult because the technology is sophisticated. In reality, the primary obstacles are organizational. Across industries, the most significant barriers to sustained impact are rooted in roles, incentives, decision rights, and culture rather than algorithms or infrastructure.

AI changes how work is performed, how decisions are made, and how accountability is structured. Its greatest impact is not in automating isolated tasks but in reshaping workflows. This requires deliberate redesign of roles, processes, and performance expectations. BCG's 10-20-70 principle reflects this reality: only a small portion of effort lies in the algorithm and technology; the majority lies in enabling people and the organization to operate differently.

Training and communication are necessary but insufficient. The deeper challenge is to move beyond incremental tool adoption toward an AI-first way of working. Individual usage does not guarantee enterprise impact. Meaningful results come when workflows are fundamentally redesigned, management layers adapt, and incentives reinforce new behaviors. Without these structural adjustments, organizations revert to legacy habits and AI remains an add-on rather than a performance engine.

## What AI Leaders Do Right

Companies that consistently generate AI value treat it as a CEO-led performance transformation, supported by a multidisciplinary transformation office, not as a technology or innovation program delegated to IT or strategy. They focus on a small set of high-impact priorities, define explicit economic ambition, fund the journey with intent, and embed value accountability into governance from the outset.

Sustained impact requires organizational follow-through. Roles, workflows, and decision rights are redesigned, not merely adjusted. Incentives and performance management reinforce new behaviors. The CFO, CHRO, and business unit leaders align behind a single business roadmap tied directly to EBIT outcomes.

AI will not transform your company. Your ability to run a disciplined transformation will.

## Authors

![](images/d018c589a2bc46681baed868026412d2562e726faf0c620614071accd63467f9.jpg)

Matthieu Berthion

Managing Director & Partner
Copenhagen

## ABOUT BOSTON CONSULTING GROUP

Boston Consulting Group bridges the gap between ambition and outcomes for the world's leading companies and organizations. We are built for this era of unprecedented change — bringing strategic clarity rooted in over 60 years of deep domain knowledge, combined with applied AI shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com.
"""
