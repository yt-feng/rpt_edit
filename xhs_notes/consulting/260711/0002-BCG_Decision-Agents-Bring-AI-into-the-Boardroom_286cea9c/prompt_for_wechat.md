你是麦肯锡/研究导读风格的微信公众号文章主笔，擅长用金字塔原理把报告内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给专业读者/产业决策者的报告导读。
- 长度：约 1200 字，整体以短导读为主，通常控制在 900-1200 个中文字符。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，只讲最关键的判断、图表和未解问题，让读者有动力去看原文。
- 文章必须像人工编辑润色过的报告导读：句长有变化，段落有呼吸感，不要整齐排比，不要反复使用“这意味着/真正重要的是/换句话说/从这个角度看”等模板转折。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、市场定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 20-35 个中文字符，最长不超过 35 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 要兼顾微信搜一搜：尽量包含一个高意图关键词，例如行业/公司/政策/AI/房地产/半导体/光伏/消费/美联储/利率/通胀/机器人/比特币等。
- `# 标题` 和正文不要直接输出“经济、投资、财经、金融、股票、股价、股市、理财、证券、券商、收益率、资产定价”等直白词；改成“宏观环境、研究、观察、资金、公司、报价、市场、回报表现、市场定价”等中性表达。
- 涉及中国、国内、内地、大陆、人民币、A股、港股时，必须使用中性客观表达；不要写“不好、不行、疲弱、低迷、恶化、危机、衰退、崩盘、放缓、压力、拖累、唱衰”等负面判断。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`波士顿咨询`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
- 标题禁止出现 GS、JPM、JEF、NOM、BARC、MS、DB、Citi、Ticker、文件编号；如果原文只有英文机构名，请翻译为中文机构名。
- 标题冒号后不要重复机构或来源类型，禁止“联合国贸发会议：联合国贸发报告，……”“麦肯锡：麦肯锡报告称，……”这类写法；冒号后直接写判断或变量。
- 标题只能保留一层信息，不要把多个长分句全部塞进标题；如果原始标题有三段以上信息，只取最有传播性的主判断，其余放在正文第一段自然展开。
- 如果报告是单一公司/个股报告，标题和正文只能写公司情况、行业变化、业务进展、竞争格局和报告里的事实；禁止出现目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO 等任何卖方操作口径。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
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
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，20-35 个中文字符。
2. 开头 2-3 段：直接给出主判断、为什么现在重要、报告提供了什么新信号；自然带出 4-6 个长尾关键词，覆盖国家/行业/公司/政策/数据/技术词，但不要写成关键词堆砌。
3. 3-4 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 1-2 个 `> **KC评论：** ...` 引用块，每个 1-2 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，不要夹带任何推广话术。
5. 正文中间禁止插入 CTA、广告、扫码、社群、知识星球、每日汇编、喂给 AI 等表达；中间只允许出现分析正文、图表占位和 `KC评论`。
6. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
7. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
8. 不要写任何 CTA、广告、扫码、社群、知识星球、网站、域名或关注引导；系统会在最结尾统一插入固定信息。
9. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
10. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>`

【CTA 要求】
- 不要输出任何 CTA。不要写“加入社群”“扫码”“星球”“完整报告领取”“网站”“域名”“关注”“星标”“更多查看”等表达。
- 文末也不要写 CTA；系统会在最结尾统一插入固定信息。
- 正文中间不要出现“如果你从某些关键词搜到这里”“单篇文章只能解决一个切片”“我每天会把……”“这篇可以沿着……”这类表达。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
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
![](images/b8bf56d258fd1c59e1e57921fc96ae1f188764ce8826f7a7cd608fd22910a611.jpg)

AI AGENTS

# Decision Agents Bring AI into the Boardroom

By Tobias Schmidt, Christoph Heuser, Nino Mori, and Luis Jäger

ARTICLE JULY 07, 2026 12 MIN READ

How familiar is this? Your executive committee discussions routinely hit a wall. Someone asks a seemingly straightforward question: “What happens if demand softens in Q3?” Or “What if our main supplier in Asia suddenly hikes its prices?” Or “What’s our real exposure if this regulation lands?” Everyone knows the data exists. It’s just never in the room at the time. Or else it arrives later, after a week of follow-ups, reconciled spreadsheets, and debates over whose numbers are “right”—and considerable effort that drains precious energy and resources. This gap quickly becomes overlooked in AI investment discussion.

Most AI programs target productivity and process improvements—faster closes, cleaner handoffs, better throughput. But they’ve largely ignored the most consequential area: the strategic decisions that span functions, deploy capital, and set enterprise priorities.

Closing that gap will be the source of the next competitive advantage, and that's where decision agents come into play. This new class of AI agent assembles cross-functional evidence, tests scenarios in real time, and supports leaders in their most complex and most consequential work: strategic decision making. Decision agents are truly transformational, providing unprecedented clarity and transparency, elevating the quality of information inputs, and leading to faster, sharper decisions that can have tangible, powerful impact.

# AI Remains Under the Radar for Major Decisions

AI investment is accelerating: companies expect to double their AI investment this year to $1.7\%$ of revenues, according to BCG's AI Radar 2026 survey of some 2,400 executives around the world. And it delivers value in execution. But while it has improved how work gets done, it hasn't yet improved how critical decisions get made.

Most of the investment continues to be directed toward operations, process, and task automation. Fewer than one-fifth of leaders ranked decision making among their top AI investment priorities. The issue isn't that executives are resistant to using AI agents; some $42\%$ of CEOs report they're now personally using agents weekly according BCG's AI Radar 2026 survey. But even among those companies stating that they consider decision making a top strategic application for AI, the actual investment in AI agents is the lowest of any topic, at just $14\%$ .

# What Are Decision Agents—and What Makes Them Valuable?

There are essentially two basic types of AI agents. Execution agents, the first and most widely used today, automate complex operational tasks with little or no human intervention. Decision agents are far more sophisticated; they synthesize inputs, evaluate alternatives, and generate recommendations according to explicit business logic. Crucially, they operate not at the point of execution but at the point of choice.

Decision agents can support individual managers or entire functional teams, creating value in three ways:

They establish a common evidence base. They combine inputs from different departments and formats to create a single, consistent baseline. The formats include structured and unstructured data, encompassing everything from emails and spreadsheets to individuals' knowledge—which needs to be codified in order for the agents to perform most effectively. Instead of working with fragmented, function-specific information, leaders can start their deliberations with more comprehensive, better-quality information.

Instead of working with fragmented, function-specific information, leaders can start their deliberations with more comprehensive, better-quality information.

They develop scenarios and evaluate them in real time. After presenting an initial assessment, decision agents can test different scenarios, updating the implications immediately. Leaders can see in real time—mid-meeting—what happens when they change assumptions. This capability reduces the time it takes to cycle through questions, analysis, and decision making.

They limit bias. By grounding recommendations in shared data and explicit business logic, decision agents limit asymmetric preparation, unchallenged assumptions, and the introduction of selective inputs, thereby creating a more neutral foundation. They do not eliminate subjective views altogether, but they make tradeoffs more transparent, recommendations more objective, and outcomes easier to trace.

# Transforming Boardroom Decision Making

Perhaps the most underappreciated, yet most valuable, use of decision agents is in meetings of executive committees. Customized decision agents can help cross-functional, senior-level committees navigate the complex, high-stakes decisions they face: integrated business planning (where volume, capacity, and budgets must align across functions); portfolio investment allocation (where capital commitments depend on inputs from strategy, finance, and operations); and market-entry decisions (where risk, feasibility, and timing need to be assessed in integrated (fashion). Not only are the inputs complex, but the cost of misalignment is high, and speed in decision making is critical for informing business outcomes.

A custom-developed decision agent can serve as another team member in the boardroom—in effect, an omniscient chief of staff with supercomputing powers. Based on information provided ahead of time, the agent “arrives” at the meeting with a preliminary memo-level assessment that it updates as the discussion unfolds. It can gather and synthesize inputs, test different scenarios, and then formulate a recommendation and translate it into concrete follow-up actions. In this way, it helps coalesce and improve the decisions that govern all else.

A custom-developed decision agent can serve as another team member in the boardroom—in effect, an omniscient chief of staff with supercomputing powers.

Specifically, decision agents can best be put to use in three high-impact areas:

Supply Chain Management. In organizations with complex supply chains, the key functional areas operate on fundamentally different incentives. Sales, for instance, pushes volume growth, while manufacturing optimizes for utilization, and procurement seeks cost efficiency and supply continuity. None have a clear view of the others' constraints. On top of these differences is the added complexity of the external disruptions from growing geopolitical shifts (such as tariffs). In short, with so many inputs and variables, supply chain planning has become increasingly complicated. Executive committee meetings require intensive preparation that extends into weeks. Even then, leaders never get an integrated view of the options.

A decision agent, on the other hand, can act as a digital twin of the supply chain. It can assemble demand forecasts, data on suppliers' capacities, and information on the cost structures across the full set of components. It pinpoints information gaps and maps potential responses against the supplier cost curves. It then helps users assess the various scenarios and evaluate the tradeoffs, offering cost implications and feasibility. And all this analysis is performed on the spot: while they meet, leaders can adjust volume assumptions and supplier choices, and the agent recalculates immediately.

Rather than spend time arguing over conflicting inputs, leaders can focus the conversation on the pivotal strategic questions and arrive at decisions faster. Decision agents, then, allow leaders to save weeks while enjoying a structured, comprehensive, consistently maintained data foundation (with codified business logic).

“Rather than spend time arguing over conflicting inputs, leaders can focus the conversation on the pivotal strategic questions and arrive at decisions faster.

Product Innovation. Product committee leaders face a similar degree of complexity in deciding what features to develop, considering everything from customer feedback and development costs to competitor signals and margin impact. Moreover, these inputs extend across different functions, so gathering the necessary data manually is unwieldy enough. Ensuring a complete and up-to-date picture is a challenge, given the variation in the frequency of updates from different data sources and in the reporting schedules of the different functional areas.

A decision agent overcomes these limitations by combining external competitive intelligence with internal feasibility and financial data. It integrates this data into a recommendation that ranks the potential new features, providing the logic underpinning the tradeoffs. While they meet, leaders evaluate and adjust the criteria weightings, and the agent makes the associated updates.

Risk Intelligence Management. Every large organization faces a long list of risks, from demand volatility and supply chain disruption to geopolitical developments and regulatory changes. Different teams monitor these risks using different data. Rarely are the implications, financial and otherwise, translated into a common measure of business impact. Updates are fragmented, so leaders do not have a consolidated view of the organization’s exposure—or of the potential cost of that exposure.

With a customized decision agent, the risk management team can continuously obtain aggregated internal and external risk signals. The agent assesses each one's impact on business performance (relative to a common metric, such as contribution margin) and calculates the point at which active mitigation is worth the cost versus the cost of the impact if the risk materializes. Above the breakeven point, the agent can provide concrete mitigation options, including their costs and effectiveness.

With these costs spelled out, risk committee leaders get an integrated and more accurate picture of enterprise risks—staying ahead of possible events and making informed decisions on the totality of risks the organization faces.

## Getting Started

In working with clients to launch the Executive Decision Agent by BCG X, we’ve learned the importance of starting with a pilot. Companies should choose one cross-functional, high-friction decision process to test, such as integrated business planning, capex allocation, or new-market entry. Next, they define the key inputs needed, such as volumes, capacity, budget, and competitor metrics. The leaders of the relevant functions (typically sales, operations, and finance) work together to hammer out a single working version of key inputs, recognizing that it may not be perfect but can be refined. Companies then embed the agent in each of the steps involved in the decision-making process, from preparation to discussion to follow-through actions. In this way, agents are viewed not as a separate analytics layer but rather as a participant in the process end to end.

“Companies should choose one cross-functional, high-friction decision process to test, such as integrated business planning, capex allocation, or new-market entry.

Beyond these practical steps, companies should consider several important elements as they begin to use decision agents. They will need to:

Establish a governance system. While agents support judgment, they are no substitute for accountability. Leaders need to set guidelines that delineate which domain owners are responsible for each of the underlying data sets and business logic. They should also specify who has access to which data and set quality standards so agents can be monitored regularly.

Ensure the right data infrastructure is in place. The extraordinary value decision agents offer is their ability to integrate inputs from different functional areas. Those inputs, however, are rarely complete, consistent, or connected. Companies therefore need to develop a structured, cross-functional data layer—a shared data lake or consolidation layer to which agents have access. Without this foundational layer, even the most sophisticated agent logic will yield unreliable results. Semantic layers that sit on top of the data layer store the codified business logic and ontology that agents will tap.

Recognize the inherent constraints of data. Leaders must also be ready to interpret and even challenge agents' outputs. Data may be imperfect, but it is still usable. Moreover, the iterative ability of AI means that it is constantly improving over time, so there is no reason to wait for perfection.

Expect adoption to challenge existing processes and structures. Decision agents touch the very heart of organizational decision making, and in doing so, shine a light on how decisions are currently made. They also expose data and process gaps and reveal where accountability is

unclear. Companies should therefore be willing to address these realities rather than try to work around them.

Decision agents touch the very heart of organizational decision making, and in doing so, shine a light on how decisions are currently made.

Regard decision agents as a structural investment, not just another initiative. Unlike other types of agents, decision agents represent far more than operational improvements. They are a transformational tool—one that not only creates reusable foundations now but that will also make future generations of agents faster and cheaper. To that end, companies need to ensure their security architecture is sound, that systems are properly integrated, and that they have the right operational infrastructure. These elements are critical preconditions for deploying agents at scale.

Clients and other first movers have already experienced how decision agents create value. They recognize that decision agents move AI from the margins to the very heart of decision making, where the most consequential choices are made. This promise of AI, this transformative capability, is here. It’s time to capture the value—and build advantage that will only compound over time.

Managing Director & Partner
Stuttgart

## Authors

![](images/0b9ebc123e953a766d276b7d20f43587f28bca058bb75c3f09e9829aa8ba8377.jpg)  
Tobias Schmidt  
Managing Director & Partner
Hamburg

![](images/23613cd48ab99b2712ee4f458bfede50fe38fb17a43ad1c714d4356bba13f5cb.jpg)

![](images/6e91e9c67af73ecbf536df813f264f8198153bbb26752118c616859027973c72.jpg)

![](images/5c68b70107d1ec05f7daab7d7757c889bd9b6d6d53cc8e6ffad6d75e2b2803fb.jpg)  
Christoph Heuser

![](images/ea0a406426c16041018704f1a6dd431d8f387bd9ce4ba290f171ade73696d019.jpg)

## Nino Mori

Managing Director & Partner Vienna

![](images/c9997d24aca7a84485d3f3d4b4df9fa8453dba10db74b85aefde358408249190.jpg)

![](images/0e758f948b35a6c9298843a30c22f124ab0d47818d029439240b1530c996cd02.jpg)

## Luis Jäger

![](images/8ef6cd27a3bd64fa1b90128ba30ae7af31d6930584f8dd9e4c1fcab5a8aa7281.jpg)  
Associate Frankfurt

## ABOUT BOSTON CONSULTING GROUP

Boston Consulting Group bridges the gap between ambition and outcomes for the world's leading companies and organizations. We are built for this era of unprecedented change — bringing strategic clarity rooted in over 60 years of deep domain knowledge, combined with applied AI shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com.
"""
