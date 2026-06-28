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
![](images/c2fa9c1ae7d561bca334d9748898f2e48ee8ed35264ae803dc2c619f005d257e.jpg)

ARTIFICIAL INTELLIGENCE

# The CEO's Guide to Physical AI

ARTICLE MAY 12, 2026 5 MIN READ

## What's at Stake

CEOs who’ve never considered automation—or have yet to act on it—may be underestimating how much has changed in recent years. Thanks to advances in physical AI, robotics is entering a new era, expanding what can be automated across industries and supply chains. Robots can now see, adapt, and adjust in real time, reducing deployment costs and complexity, accelerating adoption, and raising the cost of standing still for companies that hesitate.

## What the Numbers Say

50%

Increase in the scope of work that can be automated compared to traditional robotics

70%

Reduction in
engineering time
needed to train robots

3x

Faster payback period for cutting-edge robotics investments (from 5–7 years to 1–3)

## What's Changed

Physical AI has rapidly become more flexible and capable as both the hardware and the AI have improved.

\- Tasks once seen as too variable or cost-prohibitive for automation are now in play.

\- Many robots can be trained in virtual, digital environments so they can “learn” how to do a job before being installed.

\- This accelerates deployment and eliminates the need for onsite training, which is often disruptive and expensive.

\- Upfront investment is falling fast: in traditional robotics, about 75% of costs come from system integration, setup, and engineering, but software-defined physical AI can cut those costs by more than half.

# Five CEO Moves to Capture Value from Physical AI

While some capabilities are improving quickly, such as perception powered by modern computer vision, other areas—like human-level dexterity and physical reasoning—remain stubbornly difficult for machines. For leaders, the opportunity lies in focusing on where physical AI can deliver value today. Here are five moves they can make now.

# Move #1: Assess Operational Inefficiencies with Next-Gen Physical AI in Mind

Leaders should know where physical AI is advancing—and where it still has a long way to go. The sci-fi vision of a do-it-all, C-3PO-style humanoid robot is still distant. And we are years away from machines that can reliably navigate new environments and pass the “coffee test.” $^{1}$ To clarify what’s newly deployable versus what’s still emerging, leaders can evaluate physical AI across four capabilities:

\- Visual Perception. These robots are enhanced with machine vision that enables them to recognize objects and positions, extending automation to new environments.

\- Dexterous Manipulation. Robots that unlock complex automation by fusing perception, understanding, and force to handle variable or deformed objects. The currently available models still require extensive training for specific tasks.

\- Workflow Planning. Still under development, these robots can be told what to achieve—not how—by interpreting human intent and generating the workflow to complete the task.

\- Reasoning. This is an envisioned future state of physical AI, characterized by robots that can reason how their actions will change their surrounding environment and then choose a path based on expected outcomes. It is the highest goal for humanoid-style consumer robots and remains elusive for now.

## Move #2: Think Holistically About How Workflows and Processes Must Evolve

Even state-of-the-art physical AI cannot replicate everything a human worker does. But it can often replace 50% of the tasks they perform and do them more efficiently and consistently. To maximize value, leaders can:

\- Define a value-chain-wide automation model guided by a holistic view of where automation makes the most impact. The most strategic deployments of physical AI will require a systemic revamp, where tasks that were previously done by one worker are redistributed across the line. For example, a robot may be able to complete the repetitive physical task of an individual worker on an assembly line but not the same worker's visual quality control.

Ensure every partial task that is automated has a corresponding process redesign to unlock measurable cost and productivity gains.

\- Design factories with robots in mind. While most companies are retrofitting human workspaces, the most significant gains will come from factories and warehouses designed and built for robots. Such factories never need to close. In some cases, the technology to achieve a robot-ready factory may not yet be available. But leaders who iterate and climb the innovation curve are more likely to unlock an advantage before their competitors.

## Move #3: Know Your Target Tech Architecture Before You Buy from Vendors

Approaching potential vendors without a solid plan for how to integrate their technology into your planned architecture could land you with an approach that matches the vendor's priorities rather than your company's needs.

\- Have a plan for integrating potential vendor systems across hardware, operating backbone, simulation training environment, and applications. Decide whether and where to codevelop technology or buy existing models. Determine how a new vendor system will integrate into your company’s existing IT infrastructure before you reach out.

\- Don’t drag your feet. Physical AI is a rapidly emerging industry, and there will be competition for specific technologies. Vendors are more likely to engage with companies that have identified novel, rewarding challenges—so leaders with a systemic plan in place are more likely to attract the best in class.

# Move #4: Plan for How Jobs Will Change Before They Do

Just as designing a new tech architecture before implementation is a must, so is planning ahead for how the workforce will need to evolve.

\- Decide which human roles will shift from the factory floor to supervising, training, and integrating robots. Evaluate which workers are best positioned to be reskilled to supervise new robotic systems. Your existing workforce has the advantage of already understanding your specific needs and processes, and employees can often be transitioned to new robot-managing roles with the right upskilling. Some new talent will also be needed, so have a plan in place to secure the top candidates to fill these roles.

\- Tell your workforce how their roles will evolve. Be transparent about the coming transition, communicating how roles will change. Workers who don’t know how their role will be impacted could fill that gap with fear, which can hamper adoption. For some workers, the transition will be welcome; an assembly line worker could have the opportunity to transition from repetitive tasks to a more rewarding job designing and managing the new automation systems.

## Move #5: Institute Strong Governance for Physical AI Systems

As with other forms of artificial intelligence, physical AI comes with safety and security challenges that require vigilant governance. As they deploy the technology within their companies, CEOs must:

\- Ensure robots won’t malfunction in ways that endanger the safety of their workforce and their operations.

\- Fully understand the cybersecurity implications of integrating physical AI. As machines become more autonomous, intelligent, and connected, they can become ripe targets for hackers and other hostile actors. CEOs must have a robust plan to mitigate physical AI cybersecurity risks and recover quickly if a robot or system is hacked.

\- Remember that cybersecurity risks extend to third-party vendors. As your supply chain adds more third parties, it introduces potential new entry points for attackers looking for weak links into your network. Ensure your vendors are vigilant—otherwise your company could end up paying the price.

## Final Gut Check

![](images/31e3938f0c120f7abc9433b9c7981b3e86f793da120361484ba1ef76000d60be.jpg)

Physical AI has advanced significantly in recent years, and that momentum is likely to continue. CEOs who make smart choices now about where and when to deploy it, and do so responsibly, will not only be better positioned to unlock new levels of efficiency and value. They will also build scale and know-how that slower competitors will struggle to match.

## Featured Experts

![](images/71c68e860dcda2b0cfea43f89120cfc5c2210b209840b0ae34be4fd14aea6fba.jpg)  
Tilman Buchner  
Partner & Director
Munich

![](images/66253dc48d680caf6df1773db70d2b35ab6c2018d0160e5fedbf1dc596718959.jpg)  
Mei-Jung Chen

Managing Director & Partner
Taipei

![](images/6c2830d9424061293322a8e751636359184aa5b2a785729c78b348ccfaaab5f1.jpg)  
Daniel Küpper

Managing Director & Senior Partner
Cologne

[Non-textual symbol]

## ABOUT BOSTON CONSULTING GROUP

Boston Consulting Group bridges the gap between ambition and outcomes for the world's leading companies and organizations. We are built for this era of unprecedented change — bringing strategic clarity rooted in over 60 years of deep domain knowledge, combined with applied AI shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com.

1 The “coffee test” is an informal benchmark in physical AI that asks whether a robot can autonomously prepare and serve a cup of coffee in an unfamiliar real-world environment. It encapsulates the challenge of integrating perception, manipulation, planning, and adaptability in unstructured settings as a proxy for general-purpose embodied intelligence.
"""
