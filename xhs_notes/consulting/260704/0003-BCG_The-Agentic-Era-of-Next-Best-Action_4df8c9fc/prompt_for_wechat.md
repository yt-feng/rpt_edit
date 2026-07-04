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
![](images/fbea93e072921d5c179f316a5d0a017b4d729a3b21157f8fdcf18e4110bf92fa.jpg)

PERSONALIZATION

# The Agentic Era of Next-Best Action

By Silvio Palumbo, Yun Lim, and Karl Johnson

ARTICLE MAY 29, 2026 12 MIN READ

This is Part 2 of a five-part series on next-best action.

Well-designed customer journeys unlock highly targeted audiences, and for over a decade they have been the organizing principle behind personalization strategies. But today the journey model operates in an increasingly dynamic environment: channels have multiplied; customer signals manifest in real time; and the shelf of possible content, offers, and experiences has grown substantially.

As a result, the journey model's impact has plateaued. Personalization must evolve by changing its unit of decision from marketer-orchestrated journeys to agent-orchestrated actions, with AI agents selecting, sequencing, and composing interactions from a modular shelf in real time. The marketer's role shifts, too, from designing journey flows to curating the shelf's content and setting the objectives that agents pursue.

The stakes of getting these shifts right are significant. Organizations that modernize their next-best action (NBA) architecture will compound value across both efficiency and growth: from dramatic reductions in campaign cycle time to step-change increases in addressable revenue. (See Exhibit 1.)

## EXHIBIT 1

AI-Native Marketing Drives More Efficient, More Effective Growth Across the Enterprise

![](images/0370145c73b0e72b2a8b55a9655433c38a09145b846fb70553a4f40296b439de.jpg)  
Savings from NBA

![](images/b24db0af884ff7071b967aad116e706816ef2a73e5d6bd473956b40a470accdd.jpg)  
Savings from AI  
Source: BCG analysis leveraging industry benchmarks and BCG research commissioned by Google. Note: NBA = next-best action.

![](images/c9fc8f68b9a43a95b2e67e0961bb8f8c32e283000bed0b8ab5f60b5ac48749d3.jpg)  
Reduction in campaign cycle time

![](images/2caabe0384baeaa02f1413cb35638682100ca97280b3a6da38c0207d790467bd.jpg)  
More assets in market

![](images/73fa2b3ea79fdb4f5af57c000002567260f6282fd9eb8f926c96f5c8c501d333.jpg)  
Increase in addressable revenue

## How NBA Is Evolving

Each new evolution of NBA is defined by a different unit of decision and a different role for the marketer. Understanding where an organization sits on this continuum is the first step toward preparing for what comes next. (See Exhibit 2.)

# What Companies Build for Evolution 2 Today Becomes the Foundation for Evolution 3

Each era changes the unit of decision and the role of marketer

![](images/eb64c9f8938fe4fecafb83a7709f2f8efcb4c9b1e6f7f64f09c8b13daac8999a.jpg)  
Source: BCG analysis.
Note: NBA = next-best action.

First Evolution. Today, most organizations operate marketer-orchestrated journeys, in which marketers manually build audiences, design journey flows, and define the rules governing which customers receive which communications. The unit of decision is the journey itself. A well-honed journey remains very effective, but it scales poorly because every new segment, product launch, or channel requires a new journey—and the number of journeys quickly increases beyond the team's ability to manage them.

Second Evolution. More and more organizations are moving to model-optimized journeys, in which marketers define the components, objectives, and guardrails, but machine learning models optimize within the prebuilt journey. The models choose the best branch, offer, or message to optimize an objective function, but they operate within boundaries set by the marketer.

The unit of decision in this evolution shifts from the journey to the journey step, as NBA embraces algorithmic optimization without disrupting the underlying approach. The architecture still rests on the assumption that journeys are the appropriate organizing construct and that humans should define the options and constraints.

Third Evolution. NBA is headed toward agent-composed actions, in which the marketer's role shifts from designing journeys to curating a shelf of composable assets and setting the objectives for AI agents. The agents select, sequence, and compose atomic actions from that shelf to suit the real-time context.

The unit of decision in the third evolution is the atomic action. The marketer governs the option space (which assets are available, which constraints apply), while agents determine the activation (what, when, and in what combination or sequence). In practice, this enables a marketing organization to launch personalized programs in hours rather than weeks. Every interaction

# Four Capabilities of Agent-Native NBA

Evolving to agent-native NBA requires building four interconnected capabilities: composable shelf, agent architecture, tools/state management, and learning and optimization. (See Exhibit 3.) These four capabilities constitute a system designed from the ground up to support AI agents in autonomously reasoning, selecting actions, and composing them, rather than operating as a retrofitted traditional stack with agent capabilities bolted on top.

## EXHIBIT 3

Four Capabilities Separate Agent-Native NBA from Traditional Decisioning Stacks

![](images/1046d50c7e686e0bb87a74533f0208a72595dc5b83d9c45316eaeae3c56f5729.jpg)

Composable shelf
Modular catalog of offers, creatives, and micro-journeys that agents select from and assemble on demand

Source: BCG analysis.
Note: NBA = next-best action.

## Agent architecture

Use of specialized agents to reason about customer context, collaborate across decisioning tasks, and orchestrate real-time actions

## Tools/state management

Exposure of every model, integration, and data source as a modular tool that agents invoke on demand, with persistent memory of customer state

## Learning and optimization

Learning and optimization
Experimentation engine that measures every shelf asset and agent decision through causal testing, compounding performance over time

## Inside the Composable Shelf

The composable shelf is the modular catalog of offers, creatives, and micro-journeys that agents select from and assemble on demand. It organizes everything that is available for an agent to deploy into three levels of granularity—atomic assets, compiled communications, and micro-journeys—each tagged with metadata that agents use to evaluate what to select and how to combine the selected items. (See Exhibit 4.)

The Composable Shelf Organizes Deployable Experiences into Three Levels  
![](images/3bc852da2b3de437c338371f8dbf395b139dbd1772969e3e7c8e2ceb3570cc9d.jpg)  
Source: BCG analysis.

If content, offers, and experiences are not tagged and modularized at the right level of granularity, agents will have nothing meaningful to work with. The shelf is not a static content library. It is a living inventory that agents continually tap, test, and learn from.

Atomic assets—copy variants, image assets, offer constructs, and content templates—are the most granular building blocks. They are individually reusable and are tagged with metadata such as channel compatibility, regulatory flags, and expiration dates. Marketers, designers, and generative AI contribute to building this layer. Drawing from the resulting pool of information, agents compose whatever combination the context demands.

Compiled communications bundle an offer with a creative treatment and a channel to form a single unit that is ready for delivery at a specific touchpoint. These communications are conceived as preassembled modules: each one is a unique email message with a specific offer and creative, approved and ready to deploy. Agents select the right compiled communication for the moment and determine the optimal timing and sequence of delivery.

Micro-journeys are precomposed sequences of communications (usually consisting of two to five steps) designed to address the reality that not every brand interaction needs to be decomposed into atomic parts. Unlike the sprawling journeys in the first evolution of NBA, micro-journeys are short, self-contained, and purpose-built: a product launch sequence, an onboarding welcome series, a loyalty tier celebration. They provide curated experiences in situations where the brand has a deliberate story to tell. Agents decide when to trigger them to deliver the sequence as a complete block, but they do not rearrange the internal structure.

## What the Agent Architecture Looks Like

Agent architecture is the hub-and-spoke system of specialized agents that reason, collaborate, and orchestrate decisions. (See Exhibit 5.) The key components are agents, tools, Model Context Protocol (MCP), and learning and optimization:

\- Agents are the reasoning layer. A central orchestrator responds to a trigger action (a customer event, a scheduled cadence, a real-time signal, or a long hiatus in activity) and routes them to specialized agents. Each agent is responsible for a distinct part of the decision process—assembling context, checking eligibility, selecting the best action, composing the final communication, or managing experimentation. Agents do not execute in a fixed sequence. Instead, they identify the information they need, decide which tools to invoke, and adapt their approach based on what they find. This flexible process is what separates an agent architecture from a traditional decisioning pipeline, in which the sequence is always the same: ingest data, score, select, and deliver.

\- Tools are the action layer. Every model, data source, channel integration, and business rule in the stack is exposed as a discrete, callable tool that agents can invoke on demand. An eligibility check is a tool. A propensity model is a tool. A channel application programming interface (API) is a tool. By modularizing the stack in this way, the system gains composability. Agents can combine tools in whatever sequence the context requires, rather than following a prewired pipeline. Tools also maintain a persistent state, giving agents memory of prior interactions, customer preferences, and in-flight communications.

\- MCP is the connective layer. This protocol is what makes the architecture modular rather than monolithic. Agents use MCP to discover and invoke tools through a shared interface. New models, channels, and data sources plug in as new tools without requiring architectural reworking.

\- Learning and optimization provide the measurement engine. Through continuous experimentation, they score every shelf asset and every agent decision, thereby improving performance over time. Causal measurement and incrementality testing are essential, not optional.

![](images/d99f9b88c1446ce196d3c8abec8e04ab9797300ff7d070512932e3ac1bdd10ae.jpg)  
Note: CDP = customer data platform; DAM = digital asset manager; DWH = data warehouse; ESP = email service provider; MCP = Model Context Protocol; ML = machine learning; SMS = short message service.

The power of this architecture will make agent-native NBA architectures far superior to today's systems. Consider a credit card customer who calls to dispute a fraudulent charge, gets it resolved, and then opens the issuer's app 20 minutes later. In the first evolution of NBA, the app displays a scheduled balance transfer promotion that had been queued before the call, misinterpreting a moment when trust was just tested. In the second evolution of NBA, a propensity model suppresses the promotion in response to a recency rule, but it can't recognize that the resolved fraud case is a moment to reinforce trust.

In third evolution of NBA, the orchestrator routes the app-open event to a context agent, which assembles the full picture: fraud dispute resolved favorably, long-tenure cardholder, high monthly spending, no prior fraud incidents. An action selection agent evaluates available options and selects a security reassurance message paired with a complimentary credit monitoring upgrade. A composition agent assembles the in-app card from atomic assets on the shelf in seconds, with no human intervention. The experimentation layer records the outcome to improve the next similar moment.

# Building for Tomorrow's Agent Infrastructure

The agent-native architecture does not require or assume a greenfield build. Every component that organizations build today for the second evolution of NBA will map directly to a capability that agents can use in the third evolution of NBA. (See Exhibits 6 and 7.) The investment path is cumulative, not sequential. There is no throwaway work, and no replatforming is required.

## EXHIBIT 6

Key Parts of the Agent Architecture Are Built in Evolution 2

![](images/525cc51b9e5d9fc90c31bc4c52349fe7eb2bf79cc3734c640b2f6232df13ea5d.jpg)  
Source: BCG analysis.
Note: AWS = Amazon Web Services; CLV = customer lifetime value; DAM = digital asset manager; ESP = Email Service Provider; MCP = Model Context Protocol; SMS = short message service.

The key design principle is modularity. Every component built today should be designed as a modular tool that agents can invoke autonomously in the future. This means creating API-first interfaces, clean metadata, and well-defined inputs and outputs. The difference between an organization that can adopt agent-native NBA in 12 months and one that requires multiyear replatforming is whether it designs today's build with modularity in mind.

# The Path Forward: How to Get Started

Building these capabilities in the correct sequence ensures that every investment dollar delivers value today while building toward the third evolution of NBA. The steps are as follows:

\- Start with the composable shelf. Build a modular, metadata-rich catalog of creative, offer, product, and action assets. This work delivers immediate value by reducing content redundancy and improving reuse. Over time, it becomes the library that agents will leverage in real time.

\- Modularize the tools layer. Replatform every model and integration as a modular, API-first component. This action delivers near-term efficiency gains. Each model and integration exposed as a tool becomes a capability that agents can invoke autonomously.

\- Stand up experimentation to learn and optimize. Build causal measurement and incrementality testing to start compounding performance gains. This practice creates continuous experimentation and feedback loops that agents will eventually use for self-optimization.

\- Pilot agent use cases to build the architecture. Start with a single, bounded use case to build organizational confidence and track the rapidly evolving vendor landscape. The agent architecture is the orchestration layer that connects the other capabilities, but it benefits from the maturity of the components it orchestrates. Sequencing matters: the capabilities must be in place for an agentic approach to perform the orchestration role.

# From Campaign Operator to System Architect

The technology to build toward agent-native NBA is already widely available. The challenge lies in reinventing the marketing operating model—defining which decisions agents should make autonomously, which require human oversight, and how governance should scale as the system matures. Organizations that begin piloting single-agent use cases early will build the muscle and technical intuition they need to expand in scope over time. As the scope expands, the marketer will become the architect of the system rather than a campaign operator.

Organizations that delay adopting agentic approaches face a self-reinforcing disadvantage. Their campaign cycles will take weeks while competitors' take hours, they will assemble content manually while competitors compose dynamically from thousands of tested assets, and their experimentation will run in quarterly cycles while competitors will get smarter with every customer touchpoint. For many companies, the next 12 to 18 months will determine which side of that divide it falls on.

This is Part 2 of a five-part series on the future of next-best action. Part 1 explores why most NBA programs underdeliver and identifies four structural gaps. Part 3 unpacks the decisioning science, from propensity models to contextual bandits to foundation model reasoning. Part 4 examines how marketing organizations can

restructure around the new operating model. Part 5 addresses measurement: from campaign-level attribution to agentic measurement.

## Authors

![](images/f7e89c8b74f20b9609e7d499a11abcf3c7d11edafdf23d3c807fc8a1529f3b98.jpg)

## Silvio Palumbo

Managing Director & Senior Partner
New York

![](images/83a034b568a175b89a6fd965ca5f4a9e58a91f960f5b89da4e2f6eac5f45daa9.jpg)

![](images/39afd4721142a0224b455e59887b7314ead2bf4cd4222235c5669d1b4d9b436e.jpg)  
Yun Lim  
Associate Director Chicago

![](images/d336f2bfd3f9a703208e6c0de7acc119ad3c508637d7a5b101b2a932bbf51b2f.jpg)

## Karl Johnson

![](images/8574eeca329ef9c7a29cde90b7d2bcd0c7257b1b1f910af9171865ee848957f3.jpg)

Managing Director & Partner
Washington, DC

## ABOUT BOSTON CONSULTING GROUP

Boston Consulting Group bridges the gap between ambition and outcomes for the world's leading companies and organizations. We are built for this era of unprecedented change — bringing strategic clarity rooted in over 60 years of deep domain knowledge, combined with applied AI shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com.
"""
