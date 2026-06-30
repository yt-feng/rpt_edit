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
![](images/e163ebf3b8db155d3bf1b3db02d5836a8d8776f8926fc3fc0a31ca7a086b0f1a.jpg)

PROPERTY AND CASUALTY INSURANCE

# Always-On Portfolio Management: How Agentic AI Can Give a Lasting Edge to Commercial P&C Insurers

By Erdem Altay, Semih Durmus, Nadine Moore, Michael Schachtner, and Victor Zhou

ARTICLE JUNE 30, 2026 12 MIN READ

As property and casualty (P&C) insurers continue to invest in generative AI in areas such as underwriting and claims, an even bigger, unexplored opportunity sits at the top of the organization, in portfolio management. A new, agentic AI approach can unlock sustained competitive advantage for those who invest the time to build it.

P&C executives are under pressure to improve risk-adjusted return on equity while managing complex, multiline businesses in an increasingly uncertain global environment. They face a confluence of growing volatility, correlated risks, and data fragmentation. In this context, the gap between challenges and capabilities is widening as catastrophe exposure, claims severity, and competitive dynamics shift faster than teams can respond.

Many P&C commercial carriers face these challenges with outdated and fragmented systems, siloed data, and inconsistent definitions. While today's external environment necessitates agile, analytical steering of in-force portfolios, insurers struggle to unify data, assess potential steering actions, and make decisions in a timely manner. Where new demands must be met with rapid decision making, organizations are bound by inertia.

This capability gap offers a clear opportunity for early movers to gain a strong competitive advantage by embracing agentic AI for policy portfolio management. BCG estimates that those who do stand to improve gross premium written (GPW) growth by 1%-3%, combined ratios by 1%-2.5%, and return on equity by 1%-2%, based on a survey of more than 50 P&C commercial insurance executives. While companies are exploring these capabilities, the full potential has not yet been realized.

# Current Portfolio Management Challenges

A variety of challenges are holding P&C carriers back from conducting smoother portfolio operations. Four in particular stand out.

Visibility is fragmented and shallow. Underwriting, claims, risk engineering, and reinsurance data sits in separate systems, obstructing visibility into concentration risk. Reporting provides aggregated views by line and region, but lacks the granularity needed to detect early shifts in margin or exposure.

“ Without a clearer visibility into the trends and concentrations of the policy portfolio, insurers lack a systematic way to maximize risk-adjusted growth and returns.

Portfolio rebalancing looks backward. Portfolio management is typically retrospective and reactive, making it difficult to proactively steer the book of business toward desired segments (for example, geography, broker, or client type). CFOs and CROs can test major capital and reinsurance scenarios, but not the full set of tradeoffs across growth, exposure, and capital allocation. Without a clearer visibility into the trends and concentrations of the policy portfolio, insurers lack a systematic way to maximize risk-adjusted growth and returns.

Adjustments come too late to impact underwriting, if they come at all. Portfolio adjustments, set centrally by CROs and CUOs, lose speed and clarity as they move toward the frontline. As a result, underwriter tools, queues, and referral thresholds continue to reflect outdated risk appetites and guidelines. The result is inconsistent execution of portfolio strategy across regions, products, and lines of business.

Risk-quality issues are detected only when large losses occur. Audits catch process-related mistakes but rarely identify risk-related oversights (such as mispriced coverage, missed exclusions, or deteriorating exposure profiles). Without continuous monitoring, errors in risk selection, terms, or pricing compound unnoticed across the portfolio until they surface as losses.

# An Agentic AI Flywheel for Portfolio Management

Agentic AI presents the possibility of a granular, comprehensive, real-time, and continuously reinforcing portfolio management capability. These capabilities drive five steps of a continuous, AI-powered flywheel. (See Exhibits 1 and 2).

# The Future of Portfolio Steering Is Continuous and Agentic

![](images/34842ce53a3416fbdec751b8131e61b485247d5504b034dabceacff636de3a1d.jpg)  
Source: BCG analysis. $^{1}$ Quantum-inspired tensor networks are classical mathematical frameworks that use concepts from quantum mechanics—specifically quantum entanglement and state compression—to model, store, and process massive multidimensional data arrays on standard classical hardware like GPUs.

![](images/aa514c189f83d6f46101a8ab7e14c44c49bdcf5673340ced62dccece96a6b8a0.jpg)  
Source: BCG analysis.

## 1. Fix the book of business.

The process begins with agentic AI creating opportunities to drive new profitability by revealing pockets where better risk selection, assessment, pricing, and coverage can unlock value or recover premium leakage. AI agents achieve this by assessing policy data, in large volumes and in detail, across submissions, loss history, risk engineering, rater inputs, quotes, policies, and claims. In addition, agents can review declined business to identify missed opportunities that fit the organization's risk appetite.

\- In property, that means a detailed review of the schedule of values, limits, deductibles, occupancy, roof condition, and binder-to-policy consistency.

\- In casualty, it’s an assessment of claims, legal, and reserve patterns that point to a renewal action, tighter terms, or a different attachment point.

\- In workers' compensation, it compares declared payroll, class mix, field safety information, and true labor exposure.

Critically, humans are still in the loop. The diagnostic runs on demand with role-based controls that determine who can trigger reviews and at what level. For example, the CUO can initiate a review for the full portfolio, and underwriting leads review their respective lines. (See Exhibit 3.)

EXHIBIT 3 Scalable, Granular Policy Review  
![](images/b04ea5f556cb2d610a9535afd618f247c724c6fe5145f4d6a6419253ee917775.jpg)  
Source: BCG analysis.  
Note: FTE = full time equivalent; TIV = total insurable value.

## 2. Optimize capital and risk allocation.

In the next step, agents fine-tune capital allocation and risk-appetite setting. They look at signals from three sources: the live portfolio, competitor data from external sources, such as System for Electronic Rates & Forms filings, and leading indicators from third-party and internal risk data. The in-force book can be sliced across line of business, geography, broker, customer, and more with near real-time visibility into core metrics across top line (for example, GPW, net premiums written, sub-to-bind), bottom line (loss, expense, combined ratio), and return on equity. Leaders can test capital allocation, risk parameters, and reinsurance support through simulated impacts to portfolio KPIs. Agents enable robust, scenario-based simulations to forecast portfolio performance. CFOs, CROs, and CUOs review and rerun models to assess impact and tradeoffs of various portfolio steers, for example, line growth capital consumption. Informed by comprehensive signals and finely-tuned scenario models, leaders are empowered to make informed portfolio steers.

## 3. Automatically update guidelines.

Once portfolio steers and appetite adjustments are finalized, agents update underwriting guidelines with line-specific adjustments, including referral thresholds, deductible floors, attachment points, and documentation requirements. After the CUO and line underwriting leaders approve the changes, agents publish updates to the guideline repository, policy administration system, and other downstream systems of record and notify frontline underwriters via email, collaboration tools, and core underwriting applications. The result is more consistent, disciplined underwriting aligned with portfolio strategy.

## 4. Dynamically shape the book.

The flywheel continues with agents dynamically reshaping the book of business by refreshing prioritization and propensity-to-buy models, submission routing logic, renewal triage rules, referral matrices, and other business logic. Those insights are then used to adjust everyday rules (such as how submissions are routed, which new business gets attention, what qualifies as eligible, and how renewals are triaged) so decisions across the workflow consistently steer the portfolio toward better outcomes.

“New business submissions that fit the desired profile rise in underwriter queues, while risks that no longer match the target mix move into referral paths.

In practice, new business submissions that fit the desired profile rise in underwriter queues, while risks that no longer match the target mix move into referral paths. Renewal submissions are reevaluated against updated eligibility criteria and flagged for manual review where needed.

## 5. Monitor the landscape.

Agents continuously track salient external signals and compare portfolio performance against simulated outcomes from prior scenario modeling for early signs of trouble or drift. When agents spot negative trends or unusual patterns, they flag them and prompt a timely review by portfolio managers and leadership, depending on magnitude of variance. Instead of waiting for quarterly reports, decision makers get near-real-time visibility and context, allowing them to decide whether to stay the course, make a rapid adjustment, or rerun a fuller diagnostic from step one in the flywheel. The benefit is earlier intervention and less return-on-equity variability.

# The Path to Building an Agentic Portfolio Management Capability

To operationalize a differentiating agentic-portfolio management capability, P&C commercial insurers must undertake focused efforts to connect currently siloed systems, standardize data definitions, and codify business logic and rules for agents to replicate. Moreover, insurers will need to reassess how their portfolio management teams operate for an agentic AI paradigm.

We recommend a three-step approach to building the agentic portfolio management flywheel.

Start now: fix the book to fund the journey. The process begins with the foundational steps of connecting existing data across systems and establishing standard data definitions. This unified data layer merges data across submission flow, quotes, binders, policies, claims, reinsurance, risk engineering, underwriting guidelines, and exposure into a coherent view of the entire policy portfolio. This initial phase is not a multiyear data transformation; it is a focused effort to connect what already exists across systems.

AI agents run a diagnostic across the portfolio, identifying mispriced coverage, terms leakage, concentration risk, and renewal optimization opportunities. This step already captures significant value by improving rate adequacy, correcting exposures, and tightening terms, generating measurable P&L impact that funds the next phase.

Once this begins, the organization adds layers of internal and external data (for example, broker submissions, market pricing signals, and third-party risk scores), building toward a knowledge graph that deepens with every cycle. With this foundation, AI agents run a diagnostic across the portfolio, identifying mispriced coverage, terms leakage, concentration risk, and renewal optimization opportunities. This step already captures significant value by improving rate adequacy, correcting exposures, and tightening terms, generating measurable P&L impact that funds the next phase.

Win in the near term: connect strategy to execution in real time. The next step builds on the data foundation by establishing a process pipeline that translates portfolio strategy into underwriting outcomes. Leaders build in protocols that determine, for example, how a change in risk appetite or capital allocation cascades into updated guidelines, referral thresholds, submission routing, and renewal triage. Agents draft the guideline changes, CUOs and line

leaders review and approve, and the updates are published directly to underwriting systems and workflows. This enables leaders to close the gap between a portfolio steer and its execution and do it in near-real-time rather than in weeks or months.

Win in the long term: monitor, model, and adapt continuously. The full flywheel effect is achieved by AI agents continuously tracking an insurer's portfolio data, while simultaneously monitoring external signals like economic trends, natural catastrophe risk, and competitor rate plans. Leaders can run scenario models on demand to test tradeoffs, exploring how certain capital allocation, risk appetite, and reinsurance moves might play out before committing to specific course corrections. AI agents can compare outcomes against predictions, learning from gaps and refining future recommendations. Over time, this creates a self-improving management capability that evolves from reactive reporting to predictive insight and ultimately to adaptive, forward-looking decision making.

Agentic AI translates portfolio objectives into actionable guidance, enabling CFOs, CUOs, and CROs to consistently fix the book of business, optimize portfolio actions, and steer underwriting. The result is a shift from reactive portfolio management to proactive, data-driven, and continuous portfolio optimization. P&C commercial insurers that embrace this capability stand to reap gains through lower combined ratios and higher, more stable return on equity. As advancements in AI continue, it is imperative that P&C carriers experiment and invest in agentic portfolio management capabilities to capture the competitive advantage for first movers.

Acknowledgments: Special thanks to Raphael Troitzsch, Terri Brown, Jacob Palmer, Karl Werner, and Nathalia Bellizia.

## Authors

![](images/8c43b54046a20fd98222ea0556d2f7cbd47b50db2c9b188ef4d6b3ea97c7742f.jpg)  
Erdem Altay

Managing Director & Partner
New York

![](images/c12a8cdee4ed0d1d3cba80e0e85d857eee887894b47eae1c2cd20dd6226abf9a.jpg)

![](images/508630e927bd99beb22f7429d66dbefa802c1c2561dc1b43379a776664f327c3.jpg)

![](images/dc580b2414c0a08898e72ab3b29ea3b621c5bc7bde4e5a88f8870b723a02993f.jpg)  
Nadine Moore

Managing Director & Senior Partner
Chicago

![](images/ac19feec460a58e0f22cba8077c3e7f2a64cc73b17dd1ba3146e56e5726cbd72.jpg)  
Victor Zhou

![](images/49243ec19743eddff5a4ca1db8486e56968ef30cd82a1a3949995c254a70f855.jpg)

Project Leader
New York

![](images/5d4eb340f930808a248f4eca9c133d175a8774a3bd801211359838d58f219aed.jpg)  
Semih Durmus

![](images/675a262590f9ff6b98f4155454f25923b0b657f93794cdff93b34b9482c53574.jpg)  
Managing Director & Partner
Minneapolis

![](images/66c6da9cbc6c0b1b89e0e8321acadf32acdc6cba79127770eb1a1ea319a5233d.jpg)

## Michael Schachtner

![](images/99f06aceba854887868ab054c54147848d9dcba440451030bff74cdc6171f3b8.jpg)

Managing Director & Senior Partner
New York

## ABOUT BOSTON CONSULTING GROUP

Boston Consulting Group bridges the gap between ambition and outcomes for the world's leading companies and organizations. We are built for this era of unprecedented change — bringing strategic clarity rooted in over 60 years of deep domain knowledge, combined with applied AI shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com.
"""
