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
8. 文末自然承接未解问题，只写一段很短的轻 CTA。不要照抄固定话术，不要堆身份名单；语义可以参考但不必全塞：更多完整报告、中文摘要、KC评论和图表合集，会放进每日国际信源汇编。适合快速扫当天主流叙事，也方便后续追问和横向比较。。
9. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
10. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定套话。文末只保留 1-2 句，重点说“完整报告、中文摘要、KC评论和图表合集可以放回当天国际主线里继续看”，不要在正文中段出现。
- 严禁中段 CTA。正文中间不要出现“如果你从某些关键词搜到这里”“单篇文章只能解决一个切片”“我每天会把……”这类表达。

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
![](images/a36c663c0a212a2318492887f83a10614402ebeb9eb9f80944c60064dc273c42.jpg)

CLIMATE CHANGE AND SUSTAINABILITY

# Sustainability Reporting in Europe: From Compliance to Strategy

By Lorenzo Fantini, Vuk Trifkovic, Jannik Leiendecker, Eleonora Tieri, Solène Chataigné, and Julie Foucault

ARTICLE JULY 06, 2026 15 MIN READ

## Executive Summary

Sustainability reporting in Europe has reached a pivotal point. Following the first wave of Corporate Sustainability Reporting Directive (CSRD) disclosures for FY2024 and the subsequent FY2025 reporting cycle, companies are facing a great deal of complexity and significant cost, while displaying a tendency to overreport. Although the introduction of the European Sustainability Reporting Standards (ESRS) has significantly boosted transparency, it has also led many organizations to adopt a compliance-driven approach, often at the expense of strategic clarity and decision usefulness.

Indeed, our analysis of recent sustainability reporting practices reveals that most companies continue to operate within a compliance-oriented paradigm. Reports frequently cover a broad range of material topics, many of which are only loosely connected to the company's underlying business model or strategic priorities. This leads to lengthy disclosures, a heavy operational burden, and limited value for decision makers.

The forthcoming introduction of ESRS Set 2 is likely to change this dynamic. The revised standards—applicable from FY2026 onward—reduce the number of required data points by approximately 60% to 70% and place greater emphasis on materiality and decision usefulness. As a result, companies have an opportunity to fundamentally rethink their approach to sustainability reporting.

BCG's point of view is clear: companies can use this moment to make the transition from compliance-driven reporting to a strategy-led sustainability reporting model based on smart compliance. They have the opportunity not only to refine what they report, but also to redesign how they carry out sustainability reporting. To support this change, we envision an approach grounded on three core elements:

\- Sustainability Strategy. Reestablish the linkage between disclosure and strategic priorities.

\- Sustainability Reporting Process. Redesign reporting as an efficient, end-to-end process.

\- Enablers. Use AI, governance, and organizational capabilities to scale impact.

Companies that act now—using FY2026 as a reset point—can reduce their reporting costs, improve the clarity and relevance of their disclosures, and strengthen the connection between sustainability and business strategy. Inaction, on the other hand, could carry the risk of further entrenching inefficient processes, causing companies to miss a crucial opportunity to turn sustainability reporting into a source of competitive advantage.

## Seizing the Opportunity

Over the past decade, sustainability reporting has undergone a far-reaching transformation. What was once a largely voluntary exercise has evolved into a mandatory and increasingly complex regulatory requirement. Anchored in the European Green Deal, the EU’s policy framework seeks to guide capital allocation and corporate disclosures toward sustainability-related objectives.

The Corporate Sustainability Reporting Directive (CSRD), operationalized through the European Sustainability Reporting Standards (ESRS), represents one of the most comprehensive attempts to standardize sustainability disclosures globally. Its objective is to provide reliable, comparable, and decision-useful information across a range of environmental, social, and governance dimensions.

However, the early stages of its implementation have exposed significant challenges. The first wave of CSRD reports, for FY2024, and the subsequent FY2025 reporting cycle, have demonstrated that sustainability reporting under ESRS is both operationally demanding and costly. Companies must collect, validate, and disclose large volumes of data across multiple dimensions, often spanning complex value chains and involving numerous internal stakeholders.

As a result, sustainability reporting has evolved into a cross-functional process requiring input from sustainability, finance, risk, IT, and legal teams—frequently supported by external advisors and assurance providers. Recurring annual costs for large organizations exceed €1 million and can be significantly higher when taking into account the full scope of internal and external endeavors.

More importantly, the structure of the current standards has led to unintended behaviors. Faced with a highly prescriptive framework, many companies opt for a broad interpretation of materiality, resulting in disclosures that cover a multitude of topics. This has led to a tendency toward overreporting, severing the envisioned linkage between disclosure and strategic priorities.

The result has been sustainability reports that may be lengthy, complex, and difficult to interpret —both for preparers and for users. Recognizing these challenges, European policymakers have initiated a process of regulatory simplification. The initial EU Omnibus Package, introduced in early 2025, extended implementation timelines and reduced the scope of the regulation. The subsequent development of ESRS Set 2 marked a further adjustment of the underlying regulatory intent. The revised standards reduce the number of mandatory data points by approximately 60% to 70% and eliminate certain voluntary disclosures. They also clarify the application of double materiality, which focuses on how sustainability issues affect the company’s position and how, in turn, the entity impacts the environment and society at large. More fundamentally, the revised standards signal a transition from a focus on completeness toward a stronger emphasis on decision usefulness. This change presents companies with a unique inflection point. For the first time since the introduction of CSRD, organizations are in a position to fundamentally reimagine their sustainability reporting. FY2026 will be the first reporting cycle that fully enables this new approach.

Nevertheless, realizing this opportunity calls for more than simply adjusting disclosures. Companies should rethink the design and execution of their sustainability reporting across

# Challenge: Sustainability Reporting Between Market Practice and Regulatory Intent

The latest State of Play study from the European Financial Reporting Advisory Group (EFRAG), published in early July 2026 and more than 900 reports for FY2025, summarizes how companies currently approach sustainability reporting. Because these reports were prepared under the existing ESRS Set 1, they strongly reflect current market practices rather than the intended future state under ESRS Set 2.

EFRAG's analysis is based on a structured framework of 18 key questions spanning areas such as materiality assessment, target setting, and report structure. (See Exhibit 1.) Building on their insights, BCG further established distinct archetypes that permitted the identification and classification of observed market practices.

Identification of Emerging Markets and Best Practices in the EFRAG State of Play 2026 Report

<table><tr><td rowspan="2" colspan="2">Standard/topics</td><td rowspan="2">Questions</td><td colspan="3">Archetypes</td></tr><tr><td>Type 1</td><td>Type 2</td><td>Type 3</td></tr><tr><td rowspan="10">General disclosures</td><td rowspan="4">DMA</td><td>1 What is the company&#x27;s DMA methodology?</td><td>Bottom-up</td><td>Hybrid</td><td>Top-down</td></tr><tr><td>2 How many IROs has the company identified?</td><td>&lt;25</td><td>25-31</td><td>&gt;31</td></tr><tr><td>3 How many material topics has the company identified (excluding entity-specific topics)?</td><td>&lt;5</td><td>5-7</td><td>&gt;7</td></tr><tr><td>4 How many material subtopics has the company identified (excluding entity-specific topics)?</td><td>&lt;12</td><td>12-16</td><td>&gt;16</td></tr><tr><td rowspan="2">Strategy</td><td>5 How many topics are covered by measurable and time-bound targets?</td><td>&lt;3</td><td>3-6</td><td>&gt;6</td></tr><tr><td>6 Are targets for material topics embedded into incentive schemes/remuneration?</td><td>No</td><td>-</td><td>Yes</td></tr><tr><td rowspan="4">Descriptive topics</td><td>7 What is the number of pages?</td><td>&lt;90</td><td>90-110</td><td>&gt;110</td></tr><tr><td>8 What is the number of characters?</td><td>&lt;200,000</td><td>200,000-350,000</td><td>&gt;350,000</td></tr><tr><td>9 What is the share of the annual/management report dedicated to the CSRD report?</td><td>&lt;20%</td><td>20-40%</td><td>&gt;40%</td></tr><tr><td>10 Does the company use an executive summary for its CSRD report?</td><td>No</td><td>-</td><td>Yes</td></tr><tr><td rowspan="3">E</td><td>Transition plan (CTP)</td><td>11 Has the company adopted a CTP?</td><td>No</td><td>-</td><td>Yes</td></tr><tr><td rowspan="2">Nonclimate metrics</td><td>12 Do companies state that near-term and long-term targets are compatible with 1.5°C?</td><td>No disclosure</td><td>No</td><td>Yes</td></tr><tr><td>13 What is the level of geographic disaggregation for E2-E5 metrics?</td><td>Global</td><td>Regional</td><td>Site</td></tr><tr><td rowspan="3">S</td><td rowspan="3">Own workforce and S2-S4</td><td>14 What is the company&#x27;s unadjusted gender pay gap?</td><td>&lt;10%</td><td>10-15%</td><td>&gt;15%</td></tr><tr><td>15 Do companies report on discrimination and human rights incidents?</td><td>No</td><td>-</td><td>Yes</td></tr><tr><td>16 Do companies have human rights policies covering ESR S2 and S3?</td><td>No</td><td>-</td><td>Yes</td></tr><tr><td rowspan="2">G</td><td>Supplier management</td><td>17 Do companies take into account ESG criteria in the selection of suppliers?</td><td>No</td><td>-</td><td>Yes</td></tr><tr><td>Payments</td><td>18 Do companies disclose an average payment term for SMEs?</td><td>No</td><td>-</td><td>Yes</td></tr></table>

Sources: EFRAG State of Play 2026; BCG analysis.
Note: CSRD = Corporate Sustainability Reporting Directive; CTP = climate transition plan; DG Clima = Directorate-General for Climate Action; DMA = double materiality assessment; E = environmental; ESG = environmental, social, and governance; ESRS = European Sustainability Reporting Standards; G = governance; IRO = impact, risk, and opportunity; S = social; SME = small or medium-size enterprise.

## A Compliance-Driven Equilibrium

Across different industries, a consistent pattern emerges. Most companies approach sustainability reporting primarily as a compliance exercise. Although there are some notable exceptions, the dominant pattern involves fulfilling regulatory requirements rather than using sustainability reporting as a strategic tool.

This is particularly apparent from the number of material sustainability topics that companies cover in their reporting that are only partially covered by concrete targets or incentive schemes.

This broken connection between strategic priorities and disclosures has several undesirable consequences. The large number of material topics increases the amount of required disclosures, intensifies data collection efforts, and ultimately drives up the cost and complexity of reporting. And crucially, it diverts the report's focus away from the issues that matter most.

# AI as a Promised Step Change, but One That Has Yet to Materialize

Across the sustainability reporting ecosystem, software providers and advisors increasingly characterize AI as a potential game changer. The promise is compelling: faster data processing, reduced manual effort, improved report quality, and more decision-useful disclosures.

In principle, a wide range of AI use cases could arise along the end-to-end sustainability reporting cycle. (See Exhibit 2.)

## EXHIBIT 2

Existence of Various AI Use Cases Across the End-to-End ESG Reporting Journey

![](images/634194edee9ce9ffd656ebcd69985c75423d22108914b501052a128bf49f6972.jpg)  
Sources: News reports and industry publications; BCG analysis.
Note: EFRAG = European Financial Reporting Advisory Group; ESG = environmental, social, and governance; ESRS = European Sustainability Reporting Standards; IFRS = International Financial Reporting Standards; KPI = key performance indicator; PCF = product carbon footprint.

These include applications focused on three elements:

\- Automation of repetitive tasks such as data collection and validation

\- Advanced analytics and interpretation of sustainability data

\- More recent agentic solutions that aim to orchestrate workflows and support end-to-end reporting processes with limited human intervention

However, discussions with reporting teams and preparers point to a growing disconnect between ambition and reality. While expectations—often reinforced by vendor narratives and internal management pressure—are rising rapidly, actual deployment of AI in sustainability reporting remains limited in both scope and impact. Many current applications fail to achieve anticipated efficiency gains or quality improvements.

Several underlying factors help explain this gap between vision and results. First, use cases often lack sufficient alignment with specific pain points of the reporting process, leading to solutions that are technically feasible but operationally irrelevant. Second, fragmented data landscapes and weak data governance can limit the effectiveness of AI models. Third, the implementation process may not be properly integrated into broader reporting workflows, resulting in isolated pilots rather than scalable solutions. And finally, organizational readiness—incorporating skills, processes, and a general confidence in what AI can achieve—may lag behind the technological ambition.

As a result, AI in sustainability reporting today contributes less to transformation at scale and more to experimentation at the margins. Realizing its full potential will require a more disciplined focus on high-impact use cases, stronger data foundations, and a systematic integration of AI into the end-to-end reporting process.

# Proposed Solution: A Strategy-Led Sustainability Reporting Model Based on Smart Compliance

The transition to ESRS Set 2 offers companies a unique opportunity to redefine their sustainability reporting. However, capturing this opportunity requires more than piecemeal adjustments. It calls for a shift from compliance-driven reporting to a strategy-led model grounded in what BCG refers to as smart compliance. Smart compliance does not entail less rigor. Rather, it reflects a more focused and structured approach that prioritizes material, decision-useful disclosures while minimizing unnecessary complexity and effort. To effect this change, we propose a three-layer approach involving strategy, the reporting process, and enablers. (See Exhibit 3.)

EXHIBIT 3 Proposal to Approach Sustainability Reporting Holistically  
![](images/af8afe880892171b9fe80ad40446bac0a8bec73cc6c3fe73d214884db2fc10e2.jpg)  
Source: BCG analysis.
Note: ESG = environmental, social, and governance; KPI = key performance indicator.

# Sustainability Strategy: Reestablishing the Linkage Between Materiality and Strategic Priorities

A refined approach to double materiality lies at the core of the framework, moving away from a purely bottom-up, compliance-driven exercise. Although this orientation has always been permissible, ESRS Set 2 places stronger emphasis on a more explicit top-down perspective, allowing companies to use their strategic understanding of the business as a starting point to identify material topics.

This strategic approach helps reduce the complexity and burden of the assessment. Rather than cataloging an exhaustive list of potential sustainability topics, companies can apply a more sharply focused lens, guided by their business model and peer practices. The end result is a more disciplined and prioritized set of material issues.

At the same time, any top-down perspective need not merely reflect the status quo. Existing strategies may themselves be incomplete or evolving, and external stakeholder perspectives—including those from civil society and NGOs—offer a critical counterbalance. A robust double materiality assessment therefore supports strategic judgment with structured bottom-up validation, ensuring identification and assessment of sometimes overlooked but relevant topics.

The objective is to reestablish a clear and credible linkage between material topics and strategic priorities. Companies should explicitly connect material sustainability issues to their strategic agenda, supported by defined targets and embedded in management processes. This strengthens the internal relevance of sustainability and boosts the external credibility of disclosures.

Double materiality should serve not merely as a reporting requirement, but also as a tool to forge a stronger and more responsive sustainability strategy. When applied effectively, it can help companies concentrate on what really matters in terms of impact and financial relevance, enabling them to build a foundation for more decision-useful, strategically aligned reporting.

# Smart Compliance and the Sustainability Reporting Process: Designing How Reporting Works End- to-End

Building on a clear strategic foundation, companies should design sustainability reporting as an end-to-end process. Unfortunately, in practice, many organizations still suffer from fragmented setups characterized by siloed responsibilities, multiple handovers, and a large amount of manual intervention. This not only increases cost and effort, but also introduces inconsistencies, weakens controls, and complicates assurance.

A smart compliance approach tackles these challenges by structuring sustainability reporting across seven clearly defined and interconnected steps, from initial scoping to final publication and subsequent continuous improvement:

1. Scope and Governance—Define Scope and Decision Logic. The first step in the process involves defining the reporting boundary—covering legal entities, sites, and joint ventures—and establishing a suitable approach to consolidation (that is, financial versus operational control). This approach enables companies to translate regulatory requirements such as

CSRD/ESRS into an organization-specific framework, supported by clear governance structures, roles, timelines, and sign-off processes.

2. Materiality and Sustainability Scoping—Minimize Scope with a Defensible Rationale. A structured double materiality assessment identifies and prioritizes impacts, risks, and opportunities throughout the value chain, including upstream activities, own operations, and downstream activi

[中间内容因长度限制已省略]

tion of repetitive and rules-based tasks such as data collection, validation, and reconciliation

\- Advanced analytics to derive insights, identify anomalies, and strengthen management decision making

\- Emerging agentic solutions that orchestrate workflows and support the drafting and refinement of disclosures

Crucially, the effectiveness of these applications depends on their integration into existing processes and control frameworks, as well as on the availability of reliable, well-structured data. In parallel, organizations need to invest in targeted capability building, equipping sustainability, finance, and data teams with the skills necessary to interpret, challenge, and continually improve

AI-driven outputs. In this way, AI can cease to be merely a technology experiment and instead become a core operational capability within reporting.

It is equally important to establish robust governance and an organizational setup that enables cross-functional interoperability. Sustainability reporting naturally sits at the intersection of sustainability, finance, risk, and IT. In many organizations, however, responsibilities remain fragmented and the decision-making process is unclear. To resolve this issue, companies need to clearly define roles and accountability across the end-to-end process, supported by governance mechanisms that ensure consistency, escalation pathways, and alignment with financial reporting standards.

Effective models typically combine centralized coordination (such as through a dedicated sustainability reporting function or steering body) with distributed ownership of data and content across business units. At the same time, governance must evolve to accommodate AI-enabled processes, including oversight of model use, validation of outputs, and alignment with assurance requirements. Working together, a fit-for-purpose organizational model and strong governance structures provide a firm foundation for scaling sustainability reporting in a manner that is controlled, efficient, and audit-ready.

# Conclusion: What Should Happen Now

The evolution of sustainability reporting in Europe has reached a pivotal moment. The introduction of ESRS Set 2 gives companies a unique opportunity to reset their approach and move beyond compliance-driven reporting. FY2026 will be the first reporting cycle that fully incorporates this new direction. Organizations that take advantage of this moment to rethink their reporting model can achieve significant benefits—reducing cost, improving clarity, and strengthening the link between sustainability and business strategy.

On the other hand, companies that persist in following the approaches of the past may find themselves locked into inefficient processes that burden them with continuing cost pressure and prevent them from deriving full value from their reporting efforts.

To navigate this essential transition, organizations should prioritize three actions:

\- Revisit double materiality as a strategic lens. Reduce and prioritize material topics to ensure alignment with business strategy and stakeholder relevance.

\- Implement smart compliance through process redesign. Transform sustainability reporting into an integrated, end-to-end process that focuses on efficiency and decision usefulness.

\- Strengthen AI, governance, and organizational capabilities. Build the necessary foundation to scale reporting effectively and sustainably.

Companies should view sustainability reporting not as a regulatory imposition, but as a strategic capability. Companies that embrace this perspective and act decisively will be in a good position to create value, manage risk, and compete in an economy that increasingly focuses on sustainability.

Thank you to Constantine Karlis, LuAnn Buck, Anas El Baghdadi and Bianca Catricalà.

## Authors

![](images/67ada05b1c2ce050ac57a183e0c02b78e60aa659aa9d513e6a062770eee8fbb0.jpg)

![](images/771c88f52c163ba21045d7a119a1a2567e60c7c6b0c429ec567ad959d46307ad.jpg)  
Lorenzo Fantini  
Managing Director & Senior Partner
Milan

![](images/1da369678360c8893f3891ce04b6f61bf864d8d7f2fe6306962d21c8ea1878f5.jpg)

![](images/aa20f1eef893783169dc308b09621a727c0ce46cd0e2b39b044e81b054d06ee0.jpg)  
Vuk Trifkovic  
Managing Director & Partner,
BCG X
Berlin

![](images/65b0b7115649bf4220d9f7cb841b8187446fe548ce1706af2fc6ec9118661ed5.jpg)

## Jannik Leiendecker

Partner and Associate Director
Munich

![](images/e0487436a91aba39d9604c56134b4a79c763df1086e1359ffd4828175e02f119.jpg)

![](images/725551b46b515a75f7f531856bd60e9645acb4764a69831583d939810cb848c5.jpg)  
Eleonora Tieri

![](images/604623431683d14854a237e9753e3552ac0349122782d18e67125f387e356baa.jpg)

![](images/5922fdad42cc6fbfcf64bbd0b006408e6b5855d91201d3fc81c8fab8d24dd292.jpg)  
Project Leader
Milan  
Solène Chataigné

![](images/32ef1495ae6085481e3a6b39e97dfaf9f7672c6da78b084b1983a5e072518785.jpg)  
Manager - BCG Vantage
London Canary Wharf

![](images/e7e74baa5ed160287b4abc8f30281e969ca99ec4dccc187f99e6ac9f68925ff9.jpg)  
Julie Foucault

![](images/e1a9f5f5c2ef093e9b62ddd8aae20151b90cf656d588b7ca4693333affbdd354.jpg)  
Manager - BCG Vantage Paris

## ABOUT BOSTON CONSULTING GROUP

Boston Consulting Group bridges the gap between ambition and outcomes for the world's leading companies and organizations. We are built for this era of unprecedented change — bringing strategic clarity rooted in over 60 years of deep domain knowledge, combined with applied AI shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com.
"""
