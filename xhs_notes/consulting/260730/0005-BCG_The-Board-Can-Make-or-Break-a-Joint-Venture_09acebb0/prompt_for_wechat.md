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
![](images/cb4032521050559ad7634530cd1e40a6d220642f8d07d7c3a2078f865071d822.jpg)

JOINT VENTURES

# The Board Can Make or Break a Joint Venture

By Edward Gore-Randall and Peter Daniel

ARTICLE JULY 29, 2026 12 MIN READ

Companies invest a great deal in the planning and expense of setting up joint ventures, and the results can be extraordinarily rewarding in terms of new value created. Leaders often pay less attention to matters of governance, however, believing that a sound business plan and proven managers and board directors assigned to run the new business are sufficient for success.

That's a mistake. According to a BCG survey, as many as one in three failed JVs across industries can trace at least part of their problems to boards that failed to maintain clear decision rights, disciplined governance processes, and a commitment to acting in the best interests of the JV rather than the parent companies. The survey also found that inefficient governance was the third most common reason JVs don't succeed.

The issue is a rising concern across sectors as more companies are setting up JVs as a path to create new value. JVs face the same pressures and challenges as their parent companies and the wider business environment, but their captive structure and comparative insulation from public scrutiny can mask the corrosive effects of conflicts of interest, management paralysis, and partner distrust that may arise.

With proper planning, JV stakeholders and leaders, especially heads of strategy and corporate development, newly appointed JV board directors and JV CEOs, can establish protocols and expectations that can make the difference between having a board of directors that propels the venture to success and one that is an anchor that drags it down.

In this article, we explore examples of best practices from other types of boards that JVs can adopt as a foundation for success.

# Why Ownership Structure Changes the Board's Job

Every board is expected to support long-term value creation, oversee risk, shape leadership decisions, and provide CEO oversight and strategic input. Ownership structure affects these tasks in five ways: who the owners are, what they want, how quickly they can decide, how patient they can be, and how directly they interact with the company.

Compared with public, private-equity-owned, or family-owned companies, a JV board sits in the middle of a more complicated equation, with different parent companies, overlapping but not identical objectives, and operational, financial, and talent links between the owners and the JV company.

For many ventures, success is not just a matter of earnings but includes objectives like capability development, market access, and cost reduction that the board must keep visible and prevent from becoming muddled or contradictory. These different dimensions and complexities demonstrate why value creation in JVs needs to be understood on its own terms.

# What Makes JV Boards Distinctive

Many JV boards are run with a focus more on limiting and managing downside risks than on creating value. For appointed JV directors and CEOs, the task is complicated by the absence of financial incentives, undefined roles, and the difficulty of achieving consensus between parent companies with competing interests. Without a playbook or guidance, it’s no wonder so few boards, despite good intentions, are up to the task of turning a shared-ownership arrangement into a productive enterprise.

JV boards do not need to force consensus with owners on every issue, but they must maintain clarity on strategic objectives, supporting the delivery of needed capabilities from the owners, identifying where the owners' interests converge or diverge, and making sure governance protocols and red lines are clear to management.

The task gets harder when owners provide technology, people, capital, or other ongoing contributions to the JV. Those interfaces are often critical to unlock the full value creation potential of the JV by providing access to the combined capabilities of the owners. But they can also create drag and value leakage if no one is governing them deliberately. In some cases, one owner provides the JV with services whose value is greater than that owner's share of the JV's profits, creating a conflict of interest most JV boards aren't built to handle.

Conflicting loyalties can also be a factor because appointed directors are often influenced by incentives, reporting lines, or career paths of the parent company that employs them. This can complicate board and CEO decisions that affect the management team and culture building.

Conflicting loyalties between the JV and parent company interests can complicate decisions that affect the management team and culture building.

JV boards tend to have lighter support structures and are often composed of senior executives from parent companies “volunteering” their time to the JV alongside their regular roles. Unlike professional directors who staff public company boards, they may have little or no board experience and may be stepping into a role they view as having more downside risk than upside incentives. That’s why JV board design is so important. Shareholders need to design for director engagement, selecting directors for fit and commitment, clarifying what good board service looks like, and providing enough onboarding and ongoing support to help directors contribute.

Effective JV boards ask: Are parent company support and capabilities being provided as promised? Are service agreements still fit for purpose? Is the board seeing the right information? Are seconded executives clear on whom they serve day to day? Is one parent extracting value that was meant to be shared? Are the owners still aligned on the strategic horizon for the venture?

The JV boards most likely to succeed are those that can answer these questions with a disciplined focus on issues that matter most: strategic alignment, CEO effectiveness, major investments, partner commitments, and the health of the partnership itself. Unfortunately, too many JV boards are unable to address them at all.

Three established models—public, private-equity-owned, and family-owned—are excellent sources for lessons that JV boards can use to eliminate many of the risks and put themselves on a path to success. (See Exhibit 1.)

EXHIBIT 1 Characteristics of Ownership Structures

<table><tr><td></td><td>Ownership</td><td>Special characteristics</td><td>Role</td></tr><tr><td>Public</td><td>Dispersed shareholders</td><td>Mature regulatory and disclosure protocols</td><td>Helps management create value under scrutiny of quarterly reporting, a broad shareholder base, and constant market pressure</td></tr><tr><td>Private equity</td><td>Concentrated</td><td>Incentives tightly aligned around specific investment thesis</td><td>Operates in a more concentrated setting with tighter alignment, faster decisions, and a clearer investment thesis</td></tr><tr><td>Family-owned or privately held</td><td>Stable</td><td>Relationships matter as much as quarterly outcomes</td><td>Leans on stable ownership, longer time horizons, and deeper relationship continuity</td></tr></table>

Source: BCG analysis.

# What Public Company Boards Can Teach JV Directors

Public companies provide the clearest example of what disciplined governance looks like. Their boards operate with broad shareholder scrutiny and a steady cadence of disclosures, meetings, and performance reviews. There are at least three practical lessons for JV boards.

A Consistent Strategic Narrative. Public company boards know that if management cannot explain where the company is headed and why, the market will fill the vacuum. JVs have different stakeholders, but the board and CEO also must be able to communicate a clear value-creation thesis to the parent companies.

Board Discipline. Public company boards must structure agendas, set annual calendars, and pre-wire key decisions to move at the pace shareholders expect. Shareholder expectations of JVs are often less clear, and many JV boards shift the burden to the JV CEO to create structure around agendas, information flows, and decision making. Yet for many JV CEOs, this is their first experience working with a board. In that setting, weak board discipline is rarely a matter of intent; it is the result of JV boards and JV CEOs failing to define what good board discipline entails.

Danaher's board has been an example of disciplined governance and operating cadence. It is known for maintaining rigorous performance metrics, regular strategic reviews and long planning horizons. The lesson for JVs is that repeatable routines and a commitment to continuous improvement elevate decision quality.

Leadership Stewardship. Public company boards think carefully about CEO development and fit as strategy evolves. More JV boards, especially those overseeing seconded management teams, need to manage CEO succession as a core responsibility.

A public company example of leadership stewardship and stakeholder communication is 3M, whose board carried out a well-planned CEO succession in 2024. In the transition, the board temporarily separated CEO and chairmanship roles and clearly explained the governance rationale for the move. The 3M example shows how boards can adapt governance structures when appropriate instead of adhering rigidly to a model and the importance of transparent and consistent messaging.

# What Private Equity Boards Can Teach JV Directors

Private-equity-backed companies offer a different model altogether. Ownership is more concentrated, boards are usually smaller, and there is typically much tighter alignment among owners, directors, and management regarding what success looks like.

PE boards tend to be clear about what they expect the company to accomplish over the next six, 12, and 24 months. They also are able to make decisions quickly or change posture when needed; for example, increasing meeting cadence when performance is below expectations. JV boards can benefit from the same instinct.

An example is Blackstone, whose boards are distinguished by capability-based composition, disciplined operating cadence, high-conviction strategy, leadership alignment, and early intervention. When Blackstone acquires a company, board members are typically appointed based on capabilities the company needs, and the board becomes a forum for solving the enterprise's highest-value decisions.

This approach translates well to JV boards, where governance often breaks down because directors protect the parent company's interests rather than the enterprise. When a venture is struggling to achieve objectives, the board needs responsive directors who can concentrate on critical issues that arise and are incentivized to do so.

This comparison is naturally limited. PE boards generally are nimbler because the ownership thesis is unified, compared with a JV board that cannot move until there is enough sponsor alignment. This is why pace alone is not a sufficient measure of success—but it is an important factor.

# What Family-Owned and Private Companies Can Teach JV Directors

Family-owned and privately held companies illustrate other governance advantages: continuity and trusted relationships. Continuity matters because many ventures require longer gestation periods than one or more parents initially expect before they reach their full potential. Boards that understand this are better able to resist two common traps: demanding proof too early or losing interest as founding board directors cycle out and new directors, with little context around the instigation of the JV, move in. Private companies such as Cargill, Koch Industries, and Mars have benefited from patient ownership, long planning horizons, and a relationship-based approach to stewardship.

When trust is present, boards and CEOs can address difficult issues earlier and with less defensiveness. The important lesson for JV directors to understand is that the board is not just a decision-making body but also a relationship system. Directors stand to create resilience and value by building relationships outside the boardroom, looking out for the JV's interests, compromising without keeping score, and behaving predictably enough that other directors know where they stand.

Directors create resilience and value by building relationships outside the boardroom, compromising without keeping score, and behaving predictably enough to establish trust.

# Lessons for Stakeholders

JV leaders and stakeholders can use the board model lessons (see Exhibit 2) to help understand their roles and embrace an appropriate governance mindset.

## EXHIBIT 2

## Lessons from Three Board Models

![](images/c75ec8d6f4a081c5b811f7789fcaf5e426815e75fe08b0b1f3da3038f0db7fd1.jpg)  
Source: BCG analysis.

Heads of Legal, Strategy, and Corporate Development. As the principal architects of the venture, these corporate leaders must treat JV governance as a strategic capability, not a compliance function. It is not enough to define the board size and owner rights. They need to build a board that can work: directors with the right mandate, a meeting cadence that matches the venture's complexity, protocols for surfacing and resolving conflict, incentives that reward productive participation, and practical support for the CEO and management team. In many JVs, those governance choices ultimately prove more consequential than the original business case assumptions.

JV Board Directors. The director's job is to help the board make high-quality decisions that preserve the health, value, and strategic purpose of the JV. Directors who adopt that mindset tend to become trusted contributors regardless of whether they arrived with prior board experience. Directors who remain in an operating or advocacy mindset often struggle, even if they are highly accomplished executives.

JV CEOs. JV CEOs succeed when they act as stewards of the venture, with a focus on creating long-term value. Their primary responsibility is to build trust across shareholders, management, employees, and customers while delivering results. Effective CEOs maintain neutrality, share information consistently, respect governance processes, and avoid becoming instruments of any single owner. This is especially important if they are seconded from one of the parent companies. In many joint ventures, the CEO's most important asset is not authority or expertise; it is the trust that all parties place in their independence.

Looking across ownership structures, the message is not that one model is superior. It is that each model creates a distinct context for value creation, and that context shapes the board environment. JV boards create value when they align multiple owners behind a workable strategy, govern the parent company interfaces that shape performance, and support a CEO who must lead across organizational boundaries. Given their special characteristics, JV boards cannot imitate other ownership structures. But by studying the relevant lessons from these models, they can adopt a governance approach that promotes professionalism, quality decision making, and organizational success.

## Authors

![](images/c23aa393f60280dd0ed9c009984488b88d083202823194ec83bce79777347dc3.jpg)

Edward Gore-
Randall

Managing Director & Partner London

![](images/ac400cfcebd3c02edf19441539d69043763564fb081dc70ac7095a805b66c2fb.jpg)

Peter Daniel

Partner and Director
Washington, DC

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
9. 输出前自行核对：标题与导语不重复；主标题和每个小标题都是完整、中性的事实表达，不评价好坏、不制造冲突；没有元话语、推广语和未解问题栏目。只输出最终 Markdown，不输出核对过程。
