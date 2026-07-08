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
![](images/46baaac5e168ec7b9b30ad90ba7b5c26d61ff3ba65bb982549ea2ae15e02c448.jpg)

ARTIFICIAL INTELLIGENCE

# The Agentic Leadership Playbook: A Scaling Strategy for CTOs and CIOs

A conversation with BCG's Mark Abraham and Neveen Awad

ARTICLE JULY 08, 2026 12 MIN READ

Two practitioners who've helped shape and implement agentic AI strategy for some of the world's largest companies share what's working—and what's stalling progress.

# Everyone's talking about agentic AI. What are CTOs, CIOs, and their teams asking when they first walk in the room?

Mark Abraham: First, there is a lot of confusion about agentic AI: where to deploy agents, how autonomous they should be, and what's real versus hype. Second, business unit leaders want to address cost pressures. They are looking at agents as a way to hit productivity targets, whether that's getting cost-per-asset down or finding headcount efficiencies. But what is often missed is that this is a three-part game. Speed first, growth second, and cost third—in that order. By setting the right agentic AI strategy, the boldest companies are already tripling campaign speed, tripling ROI on media budgets, and taking 15% to 20% out of total functional spend.

Neveen Awad: The starting question is the same for any transformation: Where is the value? Agents are an incredible technology and an expensive one. If a process is simple and rule-based, you don’t need an agent. Agents work best in situations with complexity—multiparty information exchange where interpretation is needed. That’s where an agent earns its keep. Procurement is a good example. Figuring out when and how much to renegotiate with suppliers, initiating that dialogue. Agents can do most of that, with humans handling only the final conversation.

# When it comes to agentic AI implementation, what assumptions do clients most often get wrong?

Neveen: At one end, you have the “agents are going to do everything, let’s go” camp. At the other end are clients who have stopped thinking about this as a technology play entirely. For them, it’s a business orchestration play. But the point is to use technology as the mechanism for redesigning how the whole organization thinks and works. The leaders don’t ask, “How do I deploy agents?” They ask, “How do we work differently?” And they’ve accepted that perfectionism is a liability now. You pilot, you measure, you iterate.

# How should CTOs and CIOs think about data readiness as part of their agentic AI strategy?

Mark: The stakes have gone up on data readiness because agents aren’t just generating recommendations, they’re taking action. A bad definition of “lapsed customer” can cause an entire campaign to go awry. At the same time, agents can now collapse what used to be an eight-week data gathering and cleaning process into a single week. What remains irreplaceable, though—and it’s the most underappreciated part of deploying agentic solutions—is what I call the intelligence layer. By that I mean mapping your actual business context onto the data, so agents understand the drivers of your business.

Neveen: What agents need isn’t perfect data, it’s honest data—data you trust. CTOs and CIOs should build and test agents against that core, see how they’re reasoning and making inferences, and then expand the data they’re working from as confidence grows. And don’t assume GenAI will just clean the data for you, so you don’t need to worry about it. There is still significant work to do on the underlying architecture. The agents can be far more accurate and efficient when you’ve pruned the context they’re working from.

# Say more about that intelligence layer. What role does it play in agentic AI architecture?

Mark: Every company has its own theory of the business—the KPIs it tracks, how those KPIs link together, the micro-segmentation that matters. For one of our retail clients, that means thinking about existing versus new customer traffic, seven specific segments, micro-geographic demand pockets, price competitiveness signals. When you map that onto the data, any agent you put on top, even an off-the-shelf insight tool, suddenly has the context within which your team thinks about performance. That’s how you get around hallucinations and inconsistent answers. We believe large companies should own this intelligence layer. Our BCG X team holds a patent on an approach to building this efficiently, which we call EnterpriseIQ. You can plug almost any agent workflow into it and get reliable results. And because the intelligence layer is separate from the agents themselves, you can swap models in and out as better ones emerge.

Neveen: I think of it as smart plumbing. You have data over here, people making decisions over there, systems elsewhere, and organizations are constantly synthesizing all of that to take action. The goal is to build the plumbing that gives agents enough context to make those same decisions, and eventually better ones. You’ve always had APIs. What’s new is the importance of context, and all the work that goes into context engineering: what’s relevant and what isn’t. The shortest path is to start with a specific problem you’re trying to solve. Build the knowledge graph around that. Get the agents working against it. Then look at where the answers are breaking down—is it the agent logic, the knowledge graph, the source data—and go up and down the stream until it’s right. Then expand.

# Enterprises run on their ERPs and CRMs. How does an agentic AI strategy change what CTOs and CIOs should ask of those systems?

Neveen: You want to separate agentic logic from core platforms entirely. Keep the core system minimalist and as close to out-of-the-box as possible and move all the custom logic into the agentic layer. That reduces your tech debt significantly, because your core platforms become easily upgradable. You may also find you don't need the top-tier, bells-and-whistles version of a system anymore because agents are handling the complexity that used to require it. Above the core platforms, you need a model gateway to function as a unified enterprise AI orchestration layer and the knowledge layer that handles shared context and memory. The key is modularity. You should be able to swap LLMs in and out as leading providers ship better versions, without having to rebuild your agent logic.

Mark: I’d add the layer that I don’t see enough companies invest in is a marketer-facing UI, a single pane of glass that sits above all of it. The technology is moving so fast that you don’t want to train people on specific tools that will change in six months anyway. A well-designed interface abstracts all of that and makes the stack composable without burdening users with its complexity. It also becomes your single point of control and security. You can program different access levels, different authorities for different user types, and make agentic AI governance practical.

# Enterprise AI governance is not new. What does agentic AI governance require once agents start acting on their own?

Neveen: The answer is graduated autonomy: shadow mode, supervised mode, guided autonomy, full autonomy. Each tier is earned through demonstrated performance, each requiring clear measurement of the outcome you’re shooting for and the risks you’re trying to mitigate. The harder ongoing work is that every time you upgrade a model, agent behavior will likely change. You need continuous evaluation pipelines, and you need to require agents to report their journey. Many leaders are also standing up red teams whose job is to make agents behave badly before you find out at scale.

Mark: You have to define the guardrails with the business before you start. If a marketing function doesn’t have clearly defined brand standards, you cannot have a conversation about autonomous campaigns. When we built a briefing agent for a beauty company, we found it was agreeing with users and flattering their initial drafts rather than pushing back on weak briefs. We reprogrammed it to be “Socratic,” to always ask the ten questions that the best marketers would subconsciously ask themselves when writing a brief. Companies are competing not just on data but on their ability to codify the best practices of their best talent into the tools.

# The BCG AI Radar data shows a stark gap between executives

# who think agents will deliver real value this year and those who believe true transformation is still three-plus years away. What's your read?

Neveen: What struck me most in that report wasn't the transformation timeline. It was the gap between how much the executive level was being trained and engaging with GenAI and how much the working level was. Transformation happens where the work happens. The only way you can truly enable it is to go value stream by value stream and really think about what it would look like to reimagine each one. That will create massive business transformation, but the people who own those end-to-end processes have to be a big part of the change. The trailblazer organizations are also the ones who had trained more than half their workforce. Agentic AI adoption and transformation are the same track.

Mark: Only 5% of companies are truly agent-first. And it’s not a spectrum, it’s two clusters. The AI-first companies have driven adoption above 80% of basic LLM tools across their organizations. The other 95% haven’t given employees the latitude to even experiment. Agentic AI adoption rates sit at around 30% or less for even the basic tools and are often patchy at that. What separates the two clusters comes down to co-creation. The companies at the forefront build their agentic solutions with their best people around their real day-to-day challenges. A media company I work with took five members from different entertainment teams and involved them in shaping what the agent solution should look like. They iterated on these versions weekly until they could react quickly with targeted campaigns. From there, the company changed its processes and built an adoption approach that scaled to thousands of teams.

# What kills momentum in moving agentic AI implementation from pilot to scale?

Neveen: The momentum killer is forgetting that 70% of getting to scale is people and change, 20% is data and technology, and only 10% is the algorithms. Top-down leadership has to really believe and say we’re doing this, it’s going to be hard, there will be waste, but we’re doing it. People want to be part of winning teams. Start small, show real change, celebrate it, and others want in. The second killer is giving up too early when getting agents to communicate and share context gets hard. When a multi-agent network hits a context gap, that’s not a failure. It’s just something to build. The third is agentic AI governance chaos—unclear ownership creates a lot of “I own that, no I own that” confusion that stops everything.

Mark: I’d add: not moving from pilot to scale fast enough once the initial deployment works. There’s a massive difference between a use case that works in an isolated environment and one that reshapes a function. Scaling involves changing incentives, changing processes, serious training—and it requires sustainment. The C-suite churns a lot. New leaders come in with new visions and don’t build on what was learned. If the strategy only lives in the heads of the current leadership team, it’s not a strategy, it’s a bet on continuity. Boards are increasingly demanding a real AI roadmap with a portfolio view, and that accountability at the board level is one of the things that protects against momentum loss.

## What do you most want CTOs and CIOs to take away from this?

Neveen: Value-driven intellectual honesty. We are in a period where there is an enormous amount we don’t know. The leaders who acknowledge that openly—who say, “Here’s what we think, here’s what we’re going to try, here’s how we’ll know if it’s working”—will build the trust that makes these transformations succeed.

Mark: When it comes to agentic AI, bring together your best people across the relevant functions from day one. Let them shape the solutions and define what “good” looks like. Ways of working are critical and more than just agile. The use cases have to be big enough to unlock real value but small enough that nimble teams across business, tech, and data can deliver.

## Featured Experts

![](images/68c31bafaf838e82c8b3f373cce57bdc7595466555b366ac5f1661568edfb602.jpg)  
Mark Abraham  
Managing Director & Senior Partner; Global Leader, Marketing, Sales & Pricing Practice
Seattle

![](images/7a7810f18545fba90ebaceac2ba2fb2242bde2c74e45b200c7acee2927432ca2.jpg)  
Neveen Awad  
Managing Director & Senior Partner
Detroit

## ABOUT BOSTON CONSULTING GROUP

Boston Consulting Group bridges the gap between ambition and outcomes for the world's leading companies and organizations. We are built for this era of unprecedented change — bringing strategic clarity rooted in over 60 years of deep domain knowledge, combined with applied AI shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com.
"""
