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
![](images/5822402a353c45e5e206497f25883af3b2408041916a128d4134ceac0ddf764d.jpg)

ARTIFICIAL INTELLIGENCE

# The Era of Token-Based Competition Is Here. Is Your AI Strategy Ready?

By Matthew Kropp, Julie Bedard, Clark O'Niell, Sylvain Duranton, and Megan Hsu

ARTICLE JUNE 23, 2026 8 MIN READ

We have entered a new era of competition. When intelligence was the sole domain of humans, firms with a monopoly on scarce talent could sustain a clear advantage. But now, as AI models achieve PhD-level knowledge on nearly every topic, intelligence is becoming more scalable and accessible. When intelligence is abundant, advantage comes not from having it but from applying it to business problems more productively than competitors can do. Because that intelligence is deployed through the consumption of tokens—the language and currency of AI models—we call this “token-based competition.” The name is deliberate: it echoes time-based competition, the source of advantage BCG first introduced in 1988, when speed became a new basis for winning.

The advantage comes from putting AI at the center of how work gets done, both through automation and by augmenting the capabilities of human employees. Tokens multiply what knowledge workers can produce, much as the assembly line did for manufacturing. The firms pulling ahead are redesigning their processes around AI, with people applying expertise to direct and improve the system. These companies operate at a pace and scale that human-only organizations cannot match. Moreover, if the winners of token-based competition get it right, they’ll have created workflows that will improve organically over time as AI gets better, faster, and cheaper.

If the winners of token-based competition get it right, they'll have created workflows that will improve organically over time as AI gets better, faster, and cheaper.

The reward for this could be significant. We analyzed token consumption at 107 public technology companies with more than \$500 million in trailing 12-month revenue. In software engineering, roles and ways of working are already being reshaped to optimize human and AI skills. Token consumption can be measured consistently across companies through AI coding environments such as Cursor, making software engineering one of the first functions where token-based competition is observable in real usage data. Among our sample, the pattern is consistent with productive token use beginning to translate into advantage: companies in the highest token-use quintile had 16.5% median year-over-year revenue growth, compared with 5.1% in the lowest-usage group. (See the exhibit.)

## Higher AI Token Usage Is Associated with Stronger Revenue Growth

Median Year-Over-Year Revenue Growth by Token Usage Quintile (%)

![](images/e9d7da80f44f206b284995b660315b4116790dce4bea50e9d77ad0508d7a5a1f.jpg)  
Sources: Cursor; public financial and market data; BCG Institute analysis. Note: Analysis includes 107 public technology companies with annual revenues above \$500 million. Companies are grouped into quintiles based on monthly token consumption. The study period is April 2025 to March 2026. Named tools are illustrative, not endorsements.

We urge leaders to take four critical actions today to capitalize on this advantage in the era of the token-based competition.

Manage tokens like capital investment, tracking return on intelligence (ROInt) for all AI projects. When a firm has capital to deploy, it does not only ask how to minimize spending—it also asks where that capital can generate the highest return. Similarly, companies should direct token spending toward the highest-return opportunities across the business and where returns on that token spending will grow organically over time.

The ability of AI models to create competitive advantage is rooted in two properties. First, AI-enabled processes get smarter, faster, and cheaper as the underlying models improve and as systems learn from every interaction. This creates a flywheel for continuous growth. Second, because AI-powered systems can scale capacity up or down, companies can better align capacity to demand.

Capturing the value that these properties enable requires setting the right targets for tracking the value of deployed tokens. Companies that only measure labor savings will systematically favor narrower uses of AI—and leave significant value on the table. Conversely, companies that focus solely on maximizing AI token consumption (so-called “tokenmaxxing”) create perverse incentives for employees to game token metrics.

We suggest adopting ROInt (return on intelligence), a broader return metric that divides the value of output by the combined costs of labor and tokens. ROInt lets companies compare very different AI applications on the same basis: what value is the company getting from the combined use of people and tokens?

For example, in cases where AI is a substitute for traditional human labor, such as customer service automation, the value comes from delivering the same work at lower cost. ROInt captures efficiency. In augmentation cases, such as software engineering or R&D, ROInt measures the value that comes from greater output, faster innovation, or new revenue from the same or even more labor.

Move accountability for token spending to AI centers of excellence (CoEs) or business units for strategic planning. Leaders are grappling with big questions about how to manage AI spending. CFOs are asking where the funding for token consumption should come from. CTOs are worried about token “overages” causing significant budget disruptions. AI CoE leaders are tasked with budgeting for next year without insight on how token use or costs will evolve. Rather than address these questions piecemeal, we suggest moving AI accountability out of IT, where it is often viewed as a cost center, and into strategic planning, the AI CoE, or finance, where it can be integrated into the core of how work gets done.

The goal is to capitalize on the continuous growth flywheel that is triggered when AI is deployed strategically. As employees redesign entire workflows and build new tools, agents, and review mechanisms, the organization learns how to apply these advantages more effectively across the business. In token-based competition, the advantage will go to the firms that innovate and build the highest value systems that also learn and improve over time, aiming for the bets that have the potential to drive massive growth.

In token-based competition, the advantage will go to the firms that innovate and build the highest value systems that also learn and improve over time.

For example, a UK-based consumer goods company, Reckitt, has applied AI selectively across marketing, product development, and R&D. Leaders use AI to change ways of working in each of these functions, augmenting expert decision making and lowering costs of innovation through accelerated R&D. They found that by strategically applying AI to high-value processes, the company could accelerate its path from insight to earned revenue—at a lower cost. In fact, Reckitt has reported up to 60% faster content development, faster research cycles with fewer prototypes, and higher-quality marketing and innovation outputs.

Treat tokens as talent enhancers, not just as labor substitutes. In most workflows that integrate AI, humans start, guide, and finish the work. They decide which problems are worth solving, shape the prompt or workflow, evaluate the output, apply judgment, and take accountability for the result (it's why the ROInt metric includes both human intelligence cost and token cost). This argument flips the conventional wisdom on headcount. Cutting people does not just reduce cost. It may also reduce the organization's capacity to convert AI output into trusted, deployable value.

Companies that over index on substitution could end up backtracking when they realize that the strategy has left them with a dearth of critical human skills. For example, Gartner predicts that half of companies that cut customer service staff due to AI will rehire by 2027. In its survey of 321 customer service and support leaders, only 20% have legitimately reduced their staffing due to AI. This is a reminder that AI capability is jagged: it can automate some tasks, while many roles still rely on human context, relationships, and physical presence, which are all harder to substitute.

On the other hand, at connectivity cloud company Cloudflare, CEO Matthew Prince recently shared the organization's approach to the optimization problem in a viral Wall Street Journal op-ed. He argued that AI would reduce the need for “measuring” roles, including middle management and operations, while increasing the value of employees focused on building products and engaging with customers. While Cloudfare reduced headcount in measuring roles, it accelerated hiring in engineering and customer-facing functions.

Organizational change is your enabler. Be direct and honest. In our previous study, we found that 50% to 55% of jobs will be reshaped by AI, compared with 10% to 15% of jobs that are likely to be displaced by AI. This means that token-based competition will be won by companies that reject the false choice between investing in AI and investing in people. As jobs evolve, leaders can’t overlook the role of culture, behavior change, and deliberate work design to help employees know how to use AI in core workflows. This requires treating change management as part of the strategy rather than as an afterthought.

“ Token-based competition will be won by companies that reject the false choice between investing in AI and investing in people.

We know that fewer than 10% of employees use AI in an agentic way, delegating multistep work to AI agents that can plan and execute on their behalf rather than just prompting for answers or help with discrete tasks. In our experience, adoption often stalls for human reasons: employees may not know where AI can create value, may fall back on familiar routines instead of redesigning the work, or may resist using AI where they feel it threatens their core expertise or identity. Leaders need to address these barriers directly and honestly. Otherwise, token consumption may rise without building the behaviors that turn tokens into value.

For example, when JPMorgan Chase launched its Coach AI platform, it rolled out the tool in phases, proving the value of the technology and allowing advisors to learn in the context of their day-to-day work. As asset and wealth management CEO Mary Callahan Erdoes put it during the bank’s 2026 company update, the goal is to “eliminate the no-joy work in our employees’ daily lives, so that they can get on to higher-level added value.” Advisors now use AI to research content and find client information up to 95% faster and, as a result, spend more time engaging in meaningful conversations with clients.

The message for company leaders is clear: start building the organizational capability to apply intelligence productively now. That capability comes from activation: leaders reinventing work with AI as part of core workflows, managers reinforcing new behaviors, teams building new habits, and employees learning how to direct, review, and improve AI output. Adoption is the entry point, but the deeper goal is building an organization that knows how to turn tokens into value.

The BCG Institute is Boston Consulting Group's strategy think tank, dedicated to exploring and developing valuable new insights from business, technology, and science by embracing the powerful technology of ideas. The Institute engages leaders in provocative discussion and experimentation to expand the boundaries of business theory and practice and to translate innovative ideas from within and beyond business. For more ideas and inspiration from the Institute, please visit our website and follow us on LinkedIn and X (formerly Twitter).

## Authors

![](images/70a65d4e928d01fee5be0bb40c3e7a376e78df27187eea540d2da1eeaa5da222.jpg)

![](images/468d2283bb58e536c7d0296fa065813b233c82df4c075f273fddea17261c711a.jpg)  
Matthew Kropp

![](images/e9142810e5e791d02bdb203da5e7b9f98db25d12524e2f60d68e10a78142e90a.jpg)  
Managing Director & Senior Partner; BCG Henderson Institute Fellow
San Francisco - Bay Area  
Managing Director & Partner
San Francisco - Bay Area

![](images/be74e38f7f35111370ea0d5549d37c211475ea1183ec88894a5fc324b61a559c.jpg)

## Clark O'Niell

![](images/8311d748024cbe21b8ed88bf8c5e49318c14ea7d44171ca3c0e8a484f82d2872.jpg)  
Megan Hsu

Project Leader
San Diego

![](images/faed3957a93b7f49a165457fddb082f0cfac164bfa3bf63642623c8452d14ad4.jpg)

![](images/99825ed63a9a91bd34d32135247f38a785129bdef4630099f548fe101fc01e7f.jpg)

![](images/440ced44d5fa50addea43bb1f6fb4c0dd30f8c98cc11a13ce873d89ca5b30463.jpg)  
Julie Bedard

![](images/10b371016adfaf955a96e2dc1463f41debe3411cce2f47f4fe573515df66ef2d.jpg)

Managing Director & Partner; BCG Institute Fellow
Boston

## Sylvain Duranton

![](images/906ba0e6efe7b60b900170d29aafecc540875bdb9f5b9fa8077cb5e5320dbd08.jpg)

Managing Director & Senior Partner; Global Leader, BCG X Paris

## ABOUT BOSTON CONSULTING GROUP

Boston Consulting Group bridges the gap between ambition and outcomes for the world's leading companies and organizations. We are built for this era of unprecedented change — bringing strategic clarity rooted in over 60 years of deep domain knowledge, combined with applied AI shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com.
"""
