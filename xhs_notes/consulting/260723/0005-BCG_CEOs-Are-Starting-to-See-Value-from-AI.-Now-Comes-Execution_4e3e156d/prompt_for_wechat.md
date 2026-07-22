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
CEOs Are Starting to
See Value from AI.
Now Comes Execution.

July 2026

By Tuukka Seppä, Matthieu Berthion, Dominic C. Klemmer, Tomas Nordahl, Nicolas de Bellefonds, and Kristine Buus

![](images/05ff1002aff67fca8327db17e36ae64420957a82347ccbe1a1e6c0ceb67d2b58.jpg)

After a huge wave of investment, AI initiatives are starting to pay off. In BCG's latest survey, nearly nine in ten CEOs say their companies now see some cost or revenue benefits from AI in targeted areas. That's just one snapshot of CEO sentiment, about a rapidly changing topic, but it's a clear positive sign. The opportunity now is to scale those early wins into bigger P&L impact.

To understand how companies can do that, our survey compared high-performing CEOs reporting significant cost or revenue impact from AI with lower performers. $^{1}$ The results, in line with our experience with clients, show that high performers focus on a clear set of measures that lead to better outcomes. Among other things, these CEOs set the overall ambition and oversight, put their best people on the highest-priority AI initiatives, and track financial value straight through to the bottom line.

Many CEOs already understand the importance of these moves—they are the transformation disciplines that companies have used to implement other large change programs. The challenge is executing them with the rigor, speed, and accountability that AI requires.

## A Gap in Execution

It’s tempting to assume the barriers to scaling AI are primarily technical: things like model performance, data architecture, tooling, or regulation. Those issues matter, but the CEOs in our survey were more likely to cite execution barriers inside the business, such as unclear links between AI initiatives and financial outcomes, and the difficulty of redesigning workflows, roles, and incentives. (See Exhibit 1.)

## EXHIBIT 1

# Organization Challenges Outweigh Technology Constraints in Limiting the Financial Impact from AI

"What limits turning AI into financial impact at scale?" (Share of CEOs, %)

![](images/88bd9fd4a7830d0b2feefbdab6f67011d79da08943c94d05be888cdeb6522a8f.jpg)  
Source: BCG AI Transformation CEO Survey, 2026 (n=152).

1. High performers report cost reductions of at least 10% or revenue growth of at least 5% from AI. Low performers report less than 5% cost reduction or less than 2% revenue growth. To make comparisons between the two groups explicit, we did not include results from the group of CEOs reporting intermediate gains.

These execution barriers are hardly surprising, but what is intriguing is that so few companies have acted on them. Many of the CEOs we surveyed recognize the need to link AI initiatives to the P&L, but only 14% clearly define the P&L impact for all AI initiatives. They understand that people and workflows must change, but less than one-third fund efforts to redesign processes and skills. They see the need for accountability, but leave ownership spread across functions. (See Exhibit 2.)

These gaps between what CEOs say and what they do reveal an uncomfortable truth: CEOs know what they need to do—transform the business with AI to create impact at scale—but most are struggling with how to accomplish that goal. Worse, many are currently managing AI in ways that almost guarantee they won’t succeed. (See “Why AI Transformations Are Challenging.”)

## What AI Transformation Leaders Do Differently

BCG's experience, reinforced by the practices of higher performers in our survey, points to four transformational moves that set apart companies scaling AI value from those still stuck in pilots. (See Exhibit 3.) Many CEOs know these moves. Too few are applying them with the rigor AI requires.

## MAKE THE CEO THE ORCHESTRATOR OF AI, BUT MAKE THE BUSINESS ACCOUNTABLE.

Nearly half of the CEOs in an earlier BCG survey say they are personally leading AI implementation, while fewer than 10% believe AI strategy should be outsourced to a chief AI officer. But ownership is not execution. A CEO who gets too directly involved in execution risks becoming a bottleneck rather than a catalyst. The work of delivery—the accountable, quarter-by-quarter grind of turning strategy into results—belongs to CXOs and P&L owners. The CEO sets direction and everyone else drives results.

\- Focus on the big picture. The CEO's primary job is to answer foundational questions: how AI directly supports the company's strategy, what it should deliver, and how success will be measured. Those answers should inform the more tactical decisions about structuring the effort, who leads it, or how much to invest.

\- Hold CXOs and P&L owners accountable for outcomes. Accountability must then cascade downwards. Individual projects need individual owners: CXOs and P&L leaders with performance metrics tied to outcomes, not activity. Our survey shows that the companies reporting the highest cost or revenue impact from AI are twice as likely to restructure accountability as part of their AI program compared to lower performing peers.

EXHIBIT 2

## Many CEOs Recognize the Gaps in Scaling Value from AI, But Fewer Have Taken the Steps to Address Them

Share of CEO respondents (%)

![](images/fd347ce04437942afe1e68cb5db9f08b687c98d48a4cb6118053b248a1e3a5f7.jpg)

People redesign—funding
Fully fund people and change

Source: BCG AI Transformation CEO Survey, 2026 (n=152).

# Why AI Transformations Are Challenging

If these execution barriers are so familiar, why have few companies closed them? Because AI makes the familiar work of transformation harder.

The top- and bottom-line disciplines used in traditional transformations still matter. But AI raises the stakes on both sides: the upside is bigger, and so is the cost of weak execution. AI does not change the fundamentals of transformation. It magnifies them.

## The impact on people is greater.

Every transformation carries people implications, but AI does more than simply change the tasks that employees perform—it also replaces the skills needed to complete many tasks, potentially eroding attributes like critical thinking, judgment, curiosity, and originality. More fundamentally, AI changes how teams work together, reshaping their ways of working and operating models. As a result, HR now has a much bigger role in anticipating the workforce implications of AI, reshaping organizations, and changing employee behaviors.

## The plan has to change as the technology changes.

Transformation plans always require course corrections. With AI, those corrections come more often because the technology is evolving while the program is underway. Companies designing a two- to three-year transformation plan will need to adjust multiple times based on developments in AI that are impossible to predict today.

## Risks grow before companies fully understand them.

Traditional transformations carry execution and operational risk. AI adds new failure modes that can scale quickly—from cyber and operational vulnerabilities to unpredictable consumption costs and vendor lock-in. Companies need to manage these risks before they have a full view of how they will show up at scale.

## The value case is harder to prove upfront.

Traditional top- and bottom-line transformations often have a clear path to value, with known baselines and predictable timing. Modeling the financial impact of AI is more difficult. The benefits can be larger, but they may take longer to show up and be harder to attribute, requiring companies to make significant investments against more uncertain returns. As a result, companies need to continuously reassess priorities and redirect investments toward the initiatives delivering the greatest value.

![](images/f58b1a0928464418f2597f7d93981710a979902cf486b8d062a97614312a36e4.jpg)

CEOs of Companies Capturing Significant Value from AI Are Far More Likely Than Peers to Put the Right Foundation in Place, in Four Key Areas

Set clear accountability for results $^{1}$

![](images/50e849c497c9f39ddc4bdb36dfff5fa9c6daf3505c417b109fdf3b6fa8d8aa6a.jpg)  
Reshape the business to capitalize on AI $^{2}$

![](images/889b083218f6d3d36ab5d300bafe981a5fbaed00f09c04b1311ca7a43b181a0e.jpg)  
Track financial value directly to the P&L $^{3}$

![](images/c97ac10ace005ff4d7cea8e1030032b2598cad00eb8d6327f74bebeda2a42075.jpg)  
Invest in people and change management $^{4}$

![](images/393c19e148fb836c76c8ed1d35a78f539a062d5cfbee65cbde4be33a3f899f3b.jpg)  
Lower performers  
Source: BCG AI Transformation CEO Survey, 2026 (n=152).  
$^{1}$ Question: “What has your company done as part of its AI program?”  
$^{2}$ Question: “How is AI structured in your company?”  
$^{3}$ Question: “How many AI initiatives have a clearly defined P&L line impact?” $^{4}$ Question: “How rigorously is each area funded?”

\- Bring the board along. Ensure that the board authorizes the ambition, approves the funding, and sets an overall risk appetite for AI across the enterprise. Too often, board involvement in transformations is passive: in a BCG survey, nearly two-thirds of chief transformation officers said their boards were mostly limited to status updates. That is not enough for AI, where directors need to help management make the big calls on investment, risk, and pace.

## FOCUS AI ON A FEW HIGH-VALUE AREAS THAT CAN CHANGE THE BUSINESS.

AI is relatively easy to deploy in pilots, because those narrowly tailored efforts avoid the bigger challenges of data gaps, legacy systems, and cross-functional dependencies. In our survey, 64% of CEOs say their company pursues AI pilots, but only 26% embed it as part of a broader business transformation. BCG experience shows that a properly funded, company-wide effort is the only way companies will capture real value from AI.

## - Identify where the most AI value will come from.

Rather than experimenting everywhere, identify the biggest opportunities from AI and focus the company's efforts and capital in those areas—with the goal of building capabilities through direct experience. For example, when a global industrial company implemented AI, it structured the program around a limited number of end-to-end business domains, such as supply chain planning, post-sale customer interactions, and productivity. Within each domain, the company prioritized individual use cases based on their time to value, potential impact, cross-domain synergies, and other factors. Within the first year, this focused approach delivered measurable P&L impact across multiple markets.

\- Redesign workflows end-to-end. High performers are roughly seven times more likely to redesign workflows and reshape the business end-to-end with AI. Use cross-functional teams that combine business, tech, and change management expertise, and give them the autonomy to move fast and make their own decisions with sufficient governance.

\- Ensure proper funding. Funding AI demands a longer investment horizon and deeper commitment than most organizations anticipate. Unlike traditional programs, AI rarely breaks even within a 12-month cycle. The cash curve dips before it rises, making short-term self-funding unrealistic. To overcome this, CEOs need to secure sufficient multi-year funding to cover technology and change management.

## SET UP AI PROJECTS SO VALUE CAN BE TRACKED.

AI introduces measurement challenges. Most initiatives streamline workflows, save time, or improve quality, and companies look at activity metrics. But tracking the number of AI users, the number of tasks automated, or even operational KPIs reveals little about whether AI is delivering financial value. Complicating the challenge is that many of AI's benefits are second-order effects, for example, increasing decision speed and accuracy through AI improves performance, but it's hard to predict exactly how. For these reasons, companies need a more deliberate approach to measuring financial value.

\- Define the value path for each AI initiative before it launches, and be flexible. Define the expected P&L impact, baseline, KPIs, owners, and value logic before a project goes live, and treat the business case as a living document. AI initiatives often begin with uncertain adoption rates, workflow changes, and productivity effects. Continuously test assumptions, measure outcomes, and refine the value estimate as evidence emerges. High-performers are about five times more likely to define a P&L line impact for all initiatives.

\- Stand up a transformation office to lead the effort:
AI initiatives fail when governance and accountability are unclear. Create a transformation office to prioritize initiatives, manage cross-functional dependencies, track risks, and resolve roadblocks. Led by the right chief transformation officer, the office can keep business, technology, and finance leaders aligned while ensuring that value is delivered, measured, and sustained at scale.

\- Ensure finance enforces P&L accountability from day one. Align finance on baselines, metric definitions, and impact rules before launch, but require ongoing validation of realized value as initiatives scale. High-performers are 1.4 times more likely to report having finance enforce accountability in AI programs. One company evaluates AI initiatives in 12-week cycles. Every project starts with a finance-reviewed business case and clearly defined success metrics. Funding decisions are revisited as results emerge, allowing the company to increase investment behind initiatives that are proving value while redirecting resources away from those that are not.

\- Maintain a single source of truth across the full program. Use a consolidated tool to track progress, forecast impact, and report financials across all use cases, giving leaders real-time visibility across the entire portfolio of AI-related projects.

## PRIORITIZE PEOPLE AND CHANGE MANAGEMENT.

Most leaders assume AI transformations are hard because the technology is complex. In reality, the primary obstacles are organizational. In BCG's experience, just $10\%$ of the value from AI comes from algorithms, $20\%$ from data, and the remaining $70\%$ from changes to the operating model and new ways of working. Companies should focus their resources accordingly.

\- Assign your best people to AI projects. Signal that AI is a strategic priority by putting your best people—process owners with P&L accountability, top functional operators, and credible change leads—on these projects, not whoever happens to be available. High performers are 2.4 times more likely to assign their best talent to AI workstreams.

\- Rethink decision rights and incentives. Define explicitly how behaviors need to change, for whom, and how incentives will reinforce those changes. High-performers are roughly two times more likely to adapt incentives and change how decisions are made in the organization.

\- Redesign roles as AI reshapes work. AI will take on a growing share of routine tasks, so employees will be required to exercise more judgment, analysis, and higher-value decision making. Companies should use each AI initiative to redefine how work gets done, clarify new roles and accountabilities, and embed new ways of working into daily operations. Training remains important, but its purpose is to help people succeed in redesigned roles, not simply to teach them new tools. Overall, funding for people, leadership, and change is vital to ensure success. High performers are roughly two times more likely to fully fund these critical components.

The positive message from our CEO survey is clear: Companies are starting to see the financial gains from AI. What's more, our experience working with companies offers a clear blueprint for building on that momentum, grounded in the core disciplines of traditional transformation. Organizations where CEOs set clear priorities, hold leaders accountable, track value, and devote sufficient focus to change management can turn their early AI momentum into a lasting advantage.

## About the Authors

![](images/7d4cfbd06091dc5ad022a71294d20f44ab93da1d548884f41b925f7bbe72b8a1.jpg)  
Tuukka Seppä
Managing Director & Senior Partner;
Global Leader, BCG Transform Practice
Helsinki
seppa.tuukka@bcg.com

![](images/10f98d1b3a1b954e2b209badd5b00be0fc47528beca5d4286fbac1da4ffe2a48.jpg)  
Matthieu Berthion
Managing Director & Partner
Copenhagen
berthion.matthieu@bcg.com

![](images/8beb76bdb942ce4841f2d4f5d8a9e8b0e159131036429da8573b4e072553a7fe.jpg)  
Dominic C. Klemmer
Managing Director & Partner
Cologne
klemmer.dominic@bcg.com

![](images/8f59d0d941c1f4c29de467ee25ba4f7253e63d7c3762699f5886cb1dd72523c5.jpg)  
Tomas Nordahl
Managing Director & Senior Partner
Stockholm
nordahl.tomas@bcg.com

![](images/e2716d78d439fe702b62c8829822fd58e705216f2ec17a7e011044bd5bf40b98.jpg)  
Nicolas de Bellefonds
Managing Director & Senior Partner
Paris
debellefonds.nicolas@bcg.com

![](images/d6619eabe0c2264a9435eb8cda3d22b0304588579b691fcf39e0c3d8d1459ba5.jpg)  
Kristine Buus
Project Leader
Copenhagen
buus.kristine@bcg.com

## BCG

## Where Strategic Clarity Meets Applied AI

We are navigating an era of unprecedented change and disruption—powered by technology, marked by complexity, where change amplifies at scale. To lead, companies need a partner that can bridge the gap between ambition and outcomes. BCG is built for this moment. We bring strategic clarity, rooted in over 60 years of deep domain knowledge, to ensure leaders make the right choices. We combine it with applied AI, shaped and wielded by our practitioners, teaming shoulder-to-shoulder with your teams to deliver transformative impact at scale. The result? Stronger returns, transferred capabilities, and change that sticks. We are BCG.

For information or permission to reprint, please contact BCG at permissions@bcg.com. To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on LinkedIn, Instagram, Facebook, and X.

![](images/008930c06a08525e58cd640e53c38ff727a66c4dfba925a801507b1099a5a290.jpg)
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
