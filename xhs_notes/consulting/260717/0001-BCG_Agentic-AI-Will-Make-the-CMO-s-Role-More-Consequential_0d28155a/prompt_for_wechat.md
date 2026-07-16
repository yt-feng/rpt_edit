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
![](images/9ade8831c01d75bf59c24821e4eb1e79551cf99d4991d20638526cbfa4fb606c.jpg)

MARKETING AND SALES

# Agentic AI Will Make the CMO's Role More Consequential

By Ravi Dhar, Jon Iwata, Jennie Liu, Lauren Taylor, and Janet Balis

ARTICLE JULY 16, 2026 15 MIN READ

Customers are increasingly turning to AI to discover products, evaluate options, make purchasing decisions, and complete transactions. These applications of AI mark the beginning of agentic commerce, where traditional commerce shifts to a model in which AI agents become additional and active participants in customers' journey from intent to purchase.

As AI increasingly intermediates between brands and customers, companies must increasingly account for two decision makers: humans and the AI models and interfaces that influence their choices. Through their AI interactions, customers not only reveal intent as they would in a search query but also their underlying motivations, goals, and preferences. For marketers, this dynamic creates a new class of customer intelligence that extends beyond traditional data sources and can help companies sharpen their value proposition. It also creates a new imperative to market to both AI and humans.

Unquestionably, AI raises the bar for end-to-end brand stewardship. AI systems can instantly aggregate and evaluate reviews, complaints, service interactions, and other signals from across the web, making gaps between a brand's promise and customers' experiences far more visible. As AI increasingly mediates decisions, brands must ensure that what they say, what they do, and what customers experience remain consistently aligned at scale.

CMOs who ensure that the brand promise is aligned and accountable with brand performance will be well positioned to drive significant growth. However, few are prepared to seize this opportunity today. CEOs already question marketing's contribution to growth: only 14% of CEOs and CFOs consider their CMO highly effective at driving market growth, according to Gartner. Even so, with CMOs now investing heavily in AI, they have an opportunity to demonstrate marketing's strategic value. In BCG's annual survey of nearly 300 global CMOs, 96% say AI is driving end-to-end transformation of their function, though only about a third have moved beyond the basics. (See Exhibit 1.)

## EXHIBIT 1

Although $96\%$ of CMOs Believe AI Is Driving End-to-End Marketing Transformation, Only $31\%$ Have Made Agentic Execution a Reality

Pressure $(\%)$

94% of CMOs highlight increased expectations

![](images/b8216b73e5ea18d52605cec986cfcce8b0ff39ee7cd24c8c562f2a2fe81d3d8a.jpg)  
Question: How have your CEO's/executive team's expectations changed over the past two years?  
Belief $(\%)$  
96% of CMOs agree GenAI is driving significant transformation

![](images/c95f65983c756f7f6d0ae31fab31bcd94ba32f27febd8c972859246c33b84b1a.jpg)  
Question: To what extent do you agree with the following statement: "The adoption of generative AI in marketing is driving significant end-to-end transformation within our organization, including redesigning organization structures and re-engineering processes."  
Reality $(\%)$  
31% of CMOs have reached true agentic execution

![](images/6836e0189122074e182c99eb3efe762261a90131d416dfbe68b73d04b1306a47.jpg)  
Question: In the areas where generative AI is deployed today, how would you best describe its role?  
Source: BCG CMO Survey 2026, n = 283.

While much of today's AI investment is aimed at making marketing more efficient, the larger opportunity is to make AI-driven marketing a powerful growth engine. To capture that opportunity,

# Brand Stewardship: From Narrative to Promise—Performance Alignment

When CMOs think about AI-driven discovery, they often focus first on visibility. They publish fact-based content, structure product data, and expose APIs so agents can “see” the brand. But being visible to AI is different from being credibly recommended by AI. AI agents do more than find brands; they evaluate them. They assess brands’ trustworthiness, compare alternatives, and make recommendations to consumers based on observable performance, not just persuasive messaging.

Thus, AI's role goes far beyond just answering the question the user asks. According to research from Profound, nearly half of responses from major AI platforms contain unsolicited information, such as additional rationale, comparisons, and recommendations that were never requested by the user. The competition is not just for brands to be included in the answer, but to be the option the AI chooses to endorse.

For this reason, brand promise and brand performance must be fully aligned. The brand promise articulates emotional and functional benefits that distinguish a company from its competitors. Brand performance, by contrast, is how that promise is actually delivered through the product and the end-to-end customer experience across pricing, availability, fulfillment, service, and resolution. CMOs and marketers are typically responsible for defining and stewarding the brand promise, but they have historically not had full responsibility for brand performance. While narrative, storytelling, and positioning are important, they cannot bridge the gap between what customers expect and what the organization consistently delivers.

AI agents make these gaps far more visible. Agents can assess performance through data sources, such as service outcomes, product availability, pricing integrity, and customer reviews, then compare alternatives in real time. A financial services company may position itself on trust, for example, but if AI agents find a pattern of complaints about high claim rejection rates, slow

resolution times, or excessive documentation requirements, the brand's operational reality undermines its promise.

The same APIs and structured data feeds that make a brand findable will increasingly make its performance measurable—both within the company and against its competitors. This information may have a salutary effect on both brand promise and performance. The work of defining the brand promise becomes more rigorous, grounded in what the company can demonstrably deliver and where it is genuinely differentiated from competitors, rather than what it claims. Where gaps exist, CMOs will have stronger evidence to collaborate across product, operations, and service functions in order to successfully close these gaps. In this environment, brand stewardship becomes a discipline of ensuring that what the company says, what it does, and what customers experience remain consistently aligned at scale.

For CMOs, these are the implications:

\- Assess your brand the way AI agents will. Monitor how AI agents compare, rank, and recommend your offerings to identify where the brand promise breaks down and where competitors are gaining advantages.

\- Ensure your brand has a clearly differentiated and defensible brand promise. Clearly define what makes your brand superior and ensure the evidence supporting that claim is accessible to both customers and AI agents.

\- Integrate operational performance into marketing decisions. Systematically incorporate real-time signals, such as pricing integrity and customer satisfaction, into marketing decisions across paid media, owned media, and earned media teams.

\- Establish cross-enterprise governance to close promise-performance gaps. Establish shared metrics, joint accountability, regular reviews, and new incentives to ensure delivery fulfills the brand promise consistently over time.

# Market and Customer Intelligence: From Insight to Enterprise Value Creation

Theodore Levitt famously observed that customers don't want a quarter-inch drill; they want a quarter-inch hole. Despite that insight, the data most marketers use has remained stubbornly stuck at the drill level, tracking categories and clicks rather than the outcomes customers are trying to achieve.

Agents change that. When interacting with AI systems, people typically provide far richer context than they ever would in a search query. They express intent, needs, preferences, and tradeoffs. “Plan my ten-day anniversary celebration trip in Italy and remember I am pescatarian.” “Help me get a better deal on my utility payments since I am saving for retirement and my children are in college already.” These interactions reveal what customers are actually trying to accomplish by pinpointing their underlying needs rather than just product categories.

This creates two fundamental shifts. Because AI systems respond by combining products, services, and recommendations from multiple categories to address these expressed needs, they also reveal patterns of co-mingled demand that traditional research rarely uncovers. What appears as separate markets through the lens of products often emerges as a single customer outcome through the lens of intent. Competition now extends beyond traditional product silos as different technologies compete to meet the same underlying need.

What's more, consumers are using AI to help make decisions further upstream. Google's data on AI Mode shows that queries are now triple the length of traditional searches, and the fastest-growing query type contains decision-oriented language, such as “which one” and “which of.” (See Exhibit 2.) Consumers aren't just researching with AI; they're using AI to augment decision-making. The battle for influence is now won or lost across a fragmented decision journey that increasingly runs through channels the brand does not own or control.

## EXHIBIT 2

Agentic AI Prompts Unlock Richer Customer Intelligence than Traditional Keyword Search  
![](images/4c2a6aac85ab6b69bf82272ac5a8a8a9137e6f8a55a722b8812b741f15a60d1b.jpg)  
Source: Google AI Mode U.S. Insights (2026); BCG analysis.

What's new isn't simply more data. It's a fundamentally different type of customer intelligence that reveals both cross-category competitive dynamics and the contextual factors driving customer choices. When marketers can see the greater context around customer intent and decision making, they can identify where existing offerings fail to meet customer needs and where new value can be created. These insights inform not only positioning and go-to-market strategy but also product development, bundling, partnerships, and new business models. This new intelligence can directly influence what the company builds, not just how it markets what it already sells.

Yet many companies have a customer-shaped hole at the center of their strategy, not because of a lack of data but because they lack the organizational wiring to translate consumer intelligence into decisions. BCG research shows a familiar set of barriers: siloed data and teams, disconnected incentives, technology gaps, and intelligence that reaches decision makers too late to matter.

With agentic AI data, marketing can become the system through which customer intent directly informs enterprise decision-making. For perhaps the first time, the customer can have a true seat at the table through continuously updated signals that shape what the organization builds, delivers, and prioritizes.

For CMOs, these are the implications:

\- Build a new market intelligence capability around customer jobs-to-be-done. Broaden the focus of marketing to track customer queries and needs that can inform R&D and operations adjustments.

\- Translate customer intent into enterprise strategy. Use these insights to design offering bundles, forge cross-category partnerships, and participate in ecosystems that address broader customer outcomes.

\- Move marketing upstream. Leverage new intelligence to identify unmet needs, operational gaps, and adjacent opportunities that can shape new products, services, and business models aligned with the outcomes customers are seeking—both within the enterprise and through external partnerships.

\- Reinvent your intelligence-to-action process. Many organizations capture enterprise data but fail to act on it. Use AI tools to democratize access to customer intelligence, synthesize customer insights, and connect decision makers across the enterprise to a shared view of customer needs.

# Customer Experience: Rethinking the Architecture of the Attention Economy

For the past two decades, marketing has been built around the logic of the “attention economy.” In this setting, companies compete to appear at the top of search results, reach consumers through advertising as they consume or stream, and refine customer journeys and behavioral nudges to capture attention and drive action. These practices share a common assumption: a human is on the other end, with a short attention span, limited patience for complexity, and susceptibility to well-crafted framing.

That assumption no longer holds uniformly. The customer influence pathway is still nonlinear, but it is increasingly agent-mediated or agent-enhanced, and the dynamic between people and AI varies by customer, market, and moment of demand.

BCG research underscores the scale of this shift: 43% of consumer journeys are now research-led, meaning consumers enter without a predetermined brand choice and actively compare products across an expanding ecosystem of touchpoints, from social media to AI-generated responses. The average consumer now encounters more than 15 touchpoints before purchasing, up from roughly 5 a decade ago. And among consumers who use AI tools in their research, 85% rank them among their top five most influential touchpoints in the purchase decision, on par with social media and significantly ahead of traditional media. BCG’s Global Consumer Radar shows overall GenAI usage up 40% in just over a year, with shopping-related use—including research into and recommendations for brands, products, and services—among the fastest-growing applications. (See Exhibit 3.)

## Consumers Are Using GenAI to Make Brand Choices—and the Trend Is Accelerating

% of consumers who have used GenAI tools for specific purposes

![](images/2ab0a52cc6cdc2028aac6fbc8b536d0a3a936046bcbf7df80f11c47cccfce095.jpg)  
Sources: BCG Global Consumer Radar Wave 6 (April 2026) n=12,117; markets covered are US, UK, India, China, Japan, France, Mexico, Brazil, and Germany. BCG Global Consumer Radar Wave 3 (February 2025) n=7,286; markets covered are US, UK, India, China, Japan, France, Brazil, and Germany. Questions used: T3. Which of the following statements apply to you regarding GenAI tools? T4. How have you personally used GenAI tools (e.g., ChatGPT, Microsoft Copilot, Google Gemini)?

As AI takes on a larger role in evaluating and recommending options, marketers face a new question: Who exactly are we designing for? When customers are making decisions on their own, traditional marketing strengths apply: clear value propositions, behavioral insights, and the trust that comes from a consistent brand experience. However, when decisions are heavily influenced by AI, evidence that the brand consistently delivers on its promise becomes increasingly important, with AI agents evaluating and comparing that evidence at a scale no human can match. In many cases, a customer and agent are working together, with the customer forming a view while the agent informs and tests it in real time. Each configuration demands different thinking.

In a world where AI increasingly mediates and expedites human decisions, many CMOs are also asking whether they should develop and deploy their own customer-facing agents. The temptation is real. A proprietary agent generates intelligence that belongs to the brand, not a third-party platform, and gives the brand control of the experience at the moment of interaction. But what makes an agent attractive to a brand does not necessarily make it attractive to a customer.

Customers making decisions across multiple categories will have more trust in agents that can compare options broadly rather than those tied to a single provider. Customers seeking neutral guidance may be skeptical of an agent with a stake in the outcome. Branded agents are most likely to earn genuine customer preference in categories where trust and privacy matter deeply, or long-term relationships create meaningful advantages. A bank that knows a customer's financial history, for example, may be well positioned to provide advice that a general-purpose agent cannot. For most companies, the strategic question is whether they have already earned the kind of relationship that would make customers want to start there.

For CMOs, these are the implications:

\- Map how your customers interact with AI agents. Build the analytical capability to understand what customers delegate, what they decide themselves, and what they do in collaboration—by product category, decision type, and customer segment.

\- Redesign customer influence pathways for agent mediation. Adapt the sequence, timing, and content of the customer journey, designing for human attention where customers are the decision makers and for machine evaluation where agents shape decisions. The two influence pathways—humans and agents—must always be considered in parallel.

\- Measure outcomes with agents. Track visibility, evaluation, and credibility with AI agents through monitoring share of mentions for relevant needs, share of citations, recommendation rates, and other emerging indicators of agent-mediated influence.

\- Consider whether and how to deploy a branded agent. The formidable technical, financial, and competitive implications, including the risk of disintermediating existing channels and relationships, make this a decision that warrants careful deliberation at the highest levels of the enterprise. Key contributions of the CMO include determining whether the brand has earned the trust and relationship depth that would make customers genuinely prefer a branded agent over a neutral alternative. Further, if an agent is deployed, CMOs can help determine how to best design it to reflect its role as a trusted decision maker or key influencer in augmented decision-making.

# Building the Marketing Operating Model for the Agentic Era

None of the opportunities discussed above can be executed effectively within the existing operating models for marketing, and none is an end in itself. Paid, owned, and earned often sit in different parts of the marketing structure and beg to be reimagined to capitalize on these new dynamics. The purpose of any redesign is to unlock the power of new data and turn it into growth. The larger opportunity lies in redesigning how the business operates: how work is organized, how people and AI share responsibility, how opportunities flow across functions, and how performance is defined and measured.

The marketing organizations best positioned to win in the agentic era are those that have deliberately redesigned their operating models to turn AI-enabled marketing intelligence into profitable growth. That means moving from channel-based structures optimized for campaign execution to intelligence-led operating models where insight flows seamlessly across functional areas to enable smart handoffs in decisions focused on the singular outcome of growth. The aim is to direct scarce resources—people and budget—toward the areas where value is created more effectively and efficiently.

## Imperative and Opportunity

Most CMOs, like most business leaders, are currently focused on applying AI to improve productivity. That goal is necessary and challenging in its own right, but it is not where the greatest opportunity lies.

The interaction between customers and AI will generate a new class of data that is richer and more revealing than anything traditional marketing analytics has produced. For CMOs who move quickly, this data becomes a strategic advantage that can be used to build stronger brands, identify where new value can be created, and design experiences that better serve customers.

In doing so, they can establish marketing as essential to enterprise strategy. It becomes not only the function that shapes how the company goes to market but also a critical source of insight into what the company brings to market and how it should compete. The CMOs who seize this opportunity will play a critical role in defining the agentic era.

The authors thank Katie Ioas and Rob Derow at BCG for their research, perspectives, and other work that went into producing this article.

## Authors

## Ravi Dhar

George Rogers Clark Professor of Management and Marketing; Director of the Yale Center for Customer Insights and Co-Faculty Leader, Yale Program on Stakeholder Innovation and Management

## Jennie Liu

Lecturer in the Practice of Management at the Yale School of Management; Executive Director, Yale Center for Customer Insights

## Janet Balis

Managing Director & Partner
New York

## Jon Iwata

Lecturer in the Practice of Management, Yale School of Management; Practice Leader, Yale Program on Stakeholder Innovation & Management; former IBM Senior Vice President and Chief Brand Officer

## Lauren Taylor

Managing Director & Senior Partner; Global Leader, Center for Customer Insight
Dallas

![](images/f7979fd750fe6b121310567c32a32585ff1bbeec1e6f5e0a311446eb3b7fc70b.jpg)

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
9. 输出前自行核对：标题与导语不重复；每个小标题都是完整判断；没有元话语、推广语和未解问题栏目。只输出最终 Markdown，不输出核对过程。
