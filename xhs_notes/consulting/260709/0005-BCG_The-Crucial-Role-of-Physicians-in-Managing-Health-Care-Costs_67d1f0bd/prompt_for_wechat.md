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
![](images/4ac43706102bd07792119b0e3238b1584e1a446d5dd403e901619356eef8aebb.jpg)

HEALTH CARE PAYERS, PROVIDERS, SYSTEMS & SERVICES

# The Crucial Role of Physicians in Managing Health Care Costs

By Tom Rapp, Cate Wood, and Kalane Abbey

ARTICLE JULY 08, 2026 8 MIN READ

Health care providers have long faced the difficult balancing act of delivering high-quality patient care while simultaneously pursuing growth and innovation under persistent margin pressures. Many organizations have concentrated their cost-management efforts on the areas they perceive as most controllable, such as corporate overhead, nonclinical labor, and discretionary operating expenses. Yet some of the largest opportunities are often found elsewhere, in clinically sensitive domains. They are not pursued because value is absent, but because change is difficult to execute.

This constraint is particularly evident in clinically driven spending categories such as physician preference items (for example, surgical implants and biologics) and medical supplies. These areas that often remain under-addressed for three reasons: misplaced assumptions that best pricing has already been achieved, entrenched vendor relationships, and—most importantly—a lack of early and sustained physician engagement. Hospitals and health systems instead default to incremental, procurement-led efforts that deliver limited impact.

Achieving the full measure of cost control requires a different approach. Cost management must be treated as a clinical and strategic priority, and physician engagement must be embedded early and continuously through the process. Our experience with hospital systems demonstrates that real and durable value can be unlocked when these principles guide the effort.

# Why Value Often Remains Locked in Plain Sight

Third-party spending typically accounts for $30\%$ to $40\%$ of a provider's total operating expenses. This includes categories heavily affected by clinical practice patterns, vendor relationships, and historical norms. Too often, organizations do not engage clinicians fully in managing these costs, or they bring physicians in late in the process and without a member of the clinical staff who acts as a change champion. Instead, providers frame initiatives narrowly and rely on isolated sourcing events to deliver savings.

Moreover, when physicians are brought into the process after other options have already been developed, they tend to perceive the initiatives as administrative mandates rather than clinically informed decisions. Even compelling economic opportunities can stall as organizations struggle to build trust, establish shared objectives, and create alignment around change. The challenge is not simply identifying opportunities for improvement, but building the organizational capability required to capture them.

# Reframing Cost Transformation as a Clinical Endeavor

Leading organizations take a different approach. Rather than treating spending with third parties as a procurement challenge, they treat it as a clinical and strategic issue that requires alignment from the outset among clinical, operational, and executive stakeholders. The focus shifts from where to cut to how to lead change collectively and approaches cost management as a mechanism for reinvestment in strategic priorities.

Successful cost efforts begin not with negotiations or savings targets but with principles. Management makes clear that preserving excellent patient outcomes is nonnegotiable, that specialized and differentiated products will be maintained where they affect care, and that consolidation will occur only when products are clinically equivalent. Clinical leaders are engaged early to establish these shared principles, which then guide decision making throughout the transformation.

“ Successful cost efforts begin not with negotiations or savings targets but with principles. Preserving excellent patient outcomes is nonnegotiable.

Equally important, leadership explicitly positions the cost initiatives as supporting broader strategic goals, including growth, technology adoption, innovation, and clinical excellence. Cost improvement is pursued as an outcome that results from closer alignment and smarter decision making rather than as the primary objective. Cost savings become a means of expanding organizational capacity for funding innovation, supporting growth initiatives, strengthening clinical programs, and improving the patient experience.

By grounding decisions in outcomes, evidence, and long-term strategy, organizations can create the conditions for trust and avoid the defensive dynamics that often derail clinically sensitive initiatives.

# Sustained Physician Engagement as the Mechanism for Change

Early physician engagement is important, but sustained engagement is what ultimately determines the success of the effort. Physician involvement must extend beyond periodic consultation and become embedded in both decision making and vendor interactions.

## “Physician involvement must extend beyond periodic consultation and become embedded in both decision making and vendor interactions.

In many health systems, physicians maintain vendor relationships that can influence clinical procurement decisions. While these relationships are often viewed as barriers to change, they can become powerful assets when physicians are actively engaged. Once they are aligned around a shared vision, physicians can help evaluate alternatives, establish equivalency standards, provide clinical context, and reinforce expectations around partnership and value in vendor discussions.

This level of engagement does not happen automatically. Organizations must invest in building understanding, trust, and ownership among clinicians. Multiple actions consistently distinguish successful providers' efforts:

\- Identify respected physician champions who can serve as the “voice of the doctors” and help build broader clinical support. Transformation efforts are far more likely to succeed when messages come from trusted peers rather than administrative leaders alone. Influential physician champions can help translate objectives, reinforce agreed-upon principles, and build credibility across clinical teams.

\- Engage physicians early in defining equivalency standards, evaluating trade-offs, and shaping potential scenarios. Involving clinicians before decisions are made creates ownership of both the process and the outcome. Early engagement also helps distinguish where different products affect quality of care and where standardization can occur without compromising clinical outcomes.

\- Share benchmarking data and organizational context early and often. Many clinicians do not have visibility into how pricing compares across suppliers, the scale of purchasing decisions being made, or the broader financial realities facing the health system. Providing this context helps physicians evaluate alternatives through both a clinical and organizational lens and builds support for change.

\- Provide findings and updates to physician forums. Dedicated physician or physician-only discussions provide a venue for candid dialogue and peer-to-peer problem solving. Clinical staff can discuss objectives, review data, and address concerns. These forums can help surface concerns early, align stakeholders around shared principles, and create momentum for change before formal decisions are made.

\- Leverage physicians’ expertise and vendor relationships. Physicians often have long-standing relationships with suppliers and deep knowledge of the products being evaluated.

When appropriately engaged, they can help shape vendor behavior, reinforce expectations around partnership and value, and strengthen the organization's negotiating position.

\- Maintain a consistent cadence of engagement through meetings, workshops, and one-on-one discussions. Physician change management is not a single event but an ongoing process. Regular touchpoints help sustain alignment, reinforce objectives, communicate progress, and prevent previously resolved issues from resurfacing later in the transformation.

# Two Paths to Value Enabled by Physician Change Management

Engaging physicians in the change process creates value through two distinct avenues. The first is value from external partners. Physician involvement reshapes vendor behavior, strengthens negotiations, supports item-specific and volume-based pricing discussions, and reinforces the organization’s position as a strategic partner rather than a transactional buyer.

The second is internal value. With clinical alignment in place, organizations can establish clearer utilization guardrails that preserve access to specialized options while reducing unwarranted variation among clinically equivalent products. These changes improve transparency, enhance operational efficiency, and support consistent and cost-effective delivery of high-quality care.

Broader operational benefits accrue as well. Consolidating to a smaller set of core suppliers can simplify contracting, reduce operational complexity, improve inventory management, and strengthen clinical support models. At the same time, maintaining a limited number of smaller or emerging suppliers helps preserve competitive pressure on larger vendors and ensures continued access to differentiated innovation and future value creation. These levers deliver significant, sustainable impact and establish a repeatable model for future initiatives.

# An RFP as a Proof Point of Physician-Led Change

One recent provider transformation illustrates these principles in practice. A structured RFP for physician preference items served not simply as a sourcing exercise, but as a vehicle for

physician-led change management. The process was deliberately designed around principles established with clinical leadership at the outset, including preserving clinical excellence, maintaining appropriate supplier choice, and ensuring access to differentiated products where clinically necessary.

Negotiation teams paired clinicians with supply chain and operational leaders to balance the clinical perspective with commercial rigor. Strategies for vendor contracts avoided sole-sourcing approaches, preserving choice and supply resilience while enabling significant consolidation. Price was evaluated alongside other issues such as broader vendor partnership considerations, technology enablement, operational support, innovation, and long-term strategic alignment.

Physician engagement did not diminish once the RFP launched. Clinical teams remained actively involved across multiple negotiation rounds, providing input on evolving scenarios and participating directly in discussions as competitive dynamics intensified. Vendors received consistent signals not only about pricing expectations, but about what it meant to be a long-term partner to the organization.

While prior cost-focused efforts targeting the same spending categories had delivered only marginal savings, this process provided a different level of impact. (See the exhibit.) Vendor behavior shifted materially, generating significant savings and operational improvements while preserving clinical outcomes.

## Physician Engagement Is Essential to Reducing Clinical Procurement Costs

Prior cost-focused efforts delivered limited results ...

SUBSET OF VENDOR SPENDING

![](images/92b671038fcea643d3d98efd55c3b0e2e261d66741df18a5f39d926fa7dac167.jpg)  
Source: BCG case experience.  
... while early and sustained physician-based change management led to significant savings  
SUBSET OF VENDOR SPENDING

![](images/39d939f82e81bb439e17469fad3c5e69bcb4813823e099446b2b39469dcb72fa.jpg)  
Actual health system example

![](images/9ca7828d21e94ef5d350b9e31ca336dc518fe59ae86c3e6cb5d65c3adf8347da.jpg)

Even more important, the effort established a replicable model for future transformations. By demonstrating that physicians could serve as active partners in driving change rather than blocking it, the organization created a foundation for tackling other clinically sensitive opportunities. The lasting value was not only the savings achieved, but the capability developed.

# The Broader Lesson for Providers

The most important takeaway is not about any single cost category. It is about how providers can lead change when clinical autonomy, trust, and outcomes matter deeply. Physician change management is more than a communications exercise or a late-stage validation step. It is a strategic capability that unlocks value in clinically sensitive domains while preserving clinical excellence and strengthening organizational performance.

For providers facing ongoing margin pressures alongside rising expectations for quality and innovation, the message is clear. Sustainable economics are built not just through analytics or negotiation but through physician-led change. The challenge is no longer identifying opportunities for improvement but building the organizational capabilities necessary to capture them.

## Authors

![](images/f0c2b46ff414c7ca81bac93648942401471db2dbe8ea597c410e6aa151dbb7a0.jpg)  
Tom Rapp  
Managing Director & Partner
Seattle

![](images/679b241ff6d0b0dfeb38a1572d0934d203f3de155eda43e217f9cdb13b6f8568.jpg)

![](images/993f539c5e64fccdfd4cf28bd257c36530b740722d9c24546df4ed9b46928a13.jpg)  
Cate Wood

![](images/f4d6c120ad93424bad84900adcaec051d5b5d68924d9b803d9b2f02c691a1982.jpg)  
Partner
Minneapolis

![](images/d8464cba06ef961d806c50bfe8fae7f30a73db168f44ed98417cb079cb3e74ac.jpg)  
Kalane Abbey

![](images/0d33291b16254dfa163d60c34c9b6bc29a0e42b57759724f792c86d8218bec9a.jpg)

Principal
Washington, DC

## ABOUT BOSTON CONSULTING GROUP

Boston Consulting Group bridges the gap between ambition and outcomes for the world's leading companies and organizations. We are built for this era of unprecedented change — bringing strategic clarity rooted in over 60 years of deep domain knowledge, combined with applied AI shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com.
"""
