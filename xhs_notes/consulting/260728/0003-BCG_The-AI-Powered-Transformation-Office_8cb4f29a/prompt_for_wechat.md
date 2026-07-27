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
![](images/a768b139a73306076b9f65c05c06f2e357aa74d7553b0c9e7ec42980efe09b05.jpg)

BUSINESS TRANSFORMATION

# The AI-Powered Transformation Office

By Simon Weinstein, Christian Gruß, Riddhish Dubal, Paul Catchlove, Emma McQueen, Justin Lim, Aman Chawla, and Natalia Pridacha

ARTICLE JULY 27, 2026 8 MIN READ

In a 1935 piece for science fiction magazine Wonder Stories, David H. Keller described a future in which daily life would be reshaped by technology, and where cars would drive themselves. A recent Wall Street Journal article stated that in 2026, an estimated 36 million driverless taxi rides will be conducted in the US alone. Bold visions may take time to become reality, but when they do, they quickly become part of everyday life.

Enterprise transformation is approaching a similar inflection point. As AI evolves from a productivity tool into an agentic engine capable of coordinating work, it will enable the reinvention of the transformation office. The new agentic TO will execute change faster, strengthen business ownership, and deliver stronger outcomes with greater precision. Forward-looking CEOs, chief transformation officers, and C-suite members should now be envisioning the agentic TO and plotting the steps required to build it.

Transformation offices are often resource-constrained, coordination-heavy, and slow to react. Teams spend significant time tracking progress, chasing updates, compiling reports, and manually identifying risks. In addition, many organizations lack a deep bench of experienced transformation practitioners, which means the TO staff often require upskilling in transformation methodologies and change delivery, lengthening the interval between the decision to transform and the realization of results.

Applying AI opens the way for rethinking the architecture of the TO, creating a stronger execution engine that amplifies human capability, surfaces insight in real time, and enables faster, more targeted interventions. The result is a model that remains firmly human-led and enables teams to work with greater speed, precision, and confidence.

## A Look into the (Very Near) Future of the TO

The agentic transformation office of 2030 will apply AI to governance, updates, issue detection, upskilling, and sentiment analysis, quickly identifying and resolving barriers. Over time, this engine will greatly reduce the need for routine human intervention, enabling transformation staff to take on strategic roles and engage more deeply on issues that move the needle. In other words, transformation team members can partner directly with workstream leaders and initiative owners to develop targeted interventions for the opportunities with the greatest value, rather than limiting their role to monitoring performance and flagging issues for the business to resolve.

Transformation offices vary by organization, but typically focus on three core areas: program management, financial and impact tracking, and change management. Add (See exhibit.) AI is fundamentally reshaping how each of these domains will operate by 2030.

The Agentic Transformation Office Will Mix AI-Led and Human Interventions to Empower Business Ownership  
![](images/079a50891cd9379b24db7e2a769e520e4e44c246056f87076f5bbf701224ceb1.jpg)

## Program Management

Once characterized by manual tracking and reactive reporting, this area will provide always-on detection led by AI. Transformation team members will have real-time visibility into risks, dependencies, and decisions, and AI will generate automated nudges to prompt action from workstream leaders and initiative owners. Actions, updates, and follow-ups will be sent automatically, reducing the effort TO team members spend on routine coordination. This will allow significant numbers of items to be resolved prior to meetings, leaving precious talk time for pressing matters while enabling team members to focus on higher value activities.

## Financial and Impact Tracking

This function will shift from periodic validation to ongoing transparency into value delivery, enabled by dynamic forecasting and rapid course correction. AI-based predictive modeling can forecast the likely trajectory of impact realization and identify potential gaps in value delivery early based on data patterns from the existing transformation portfolio, deeper integration with enterprise resource planning and core finance systems, as well as trends from external benchmarks. This will give executives line of sight into the transformation and highlight where business attention is most needed. Finance will continue to play a critical role in validating the impact, ensuring consistency with P&L reporting and performance. As data and insights make transformations more predictable, organizations will also be better positioned to substantiate value creation narratives with investors.

## Change Management

This aspect of transformation will no longer involve broad, generic interventions; instead it will focus on precision engagement, using real-time sentiment and targeted nudges to boost adoption and foster behavior change. The TO will leverage deeper insights to better manage change capacity, identifying where teams are overloaded, where fatigue is building, and where sequencing requires adjustment to protect adoption and momentum. It will develop and roll out rich, role-specific upskilling content and personalized coaching, and ensure that feedback loops are closed, building the institutional trust and resilience required to bring about real impact. This will make transformation outcomes deeply personal, motivating team members to push harder towards program objectives.

# AI Doesn’t Replace Humans; It Fosters Business Ownership

As leaders embed AI into their transformation offices, they should bear in mind that organizations positioning AI as a substitute for human roles risk diluting accountability, reducing review quality, and eroding trust, according to BCG research conducted with Harvard Business Review. AI adoption must be thoughtful, considered, and embedded within human-led systems, not positioned as a replacement for them.

To accomplish this shift safely and responsibly, organizations must set in place minimum viable governance for AI tools: what they can draft and recommend, what requires human review, and what must remain a human decision. The transformation team can then focus on translating AI insights into action, nurturing change skills, and empowering sponsors, workstream leaders, and initiative owners to take greater ownership and make faster, better decisions.

# Getting Started with an Agentic Transformation Office

Like any high-performing TO, an agentic transformation office should begin with a clearly defined strategic vision, mandate, and scope. Before introducing agentic capabilities, organizations must establish the office's role, the value it is expected to deliver, and the decisions and outcomes it will enable. In an AI-enabled environment, leaders shouldn't shy away from setting lofty ambitions—rather, they should establish stretch targets by default, based on the understanding that technology will provide opportunity for achievement beyond current expectations.

With the objective established, leaders should design an operating model that includes team structure, governance, decision rights, and the roles that remain human-led versus those that will be augmented by AI. Clear ways of working, reporting cadences, and escalation pathways will ensure the discipline needed for effective execution. Identifying the right team is as critical as ever, because members will be responsible for blueprinting how to use technology to amplify impact. To succeed in this new context, transformation team members will need a combination of strategic vision and executional rigor that go beyond pure operational skills.

Finally, organizations should invest early in capability building. Equip program teams with the tools they need to succeed. Provide access to cutting-edge AI technology, backed by strong transformation and change principles. Empower them to take risks and disrupt business as usual. Establishing these foundations early enables agentic transformation offices to scale capabilities across increasingly complex portfolios with confidence.

By building on existing TO foundations and embedding agentic capabilities where they can have the biggest impact, organizations can reduce value leakage, improve decision velocity, deliver more consistent outcomes, and unlock greater value from their transformations. The strongest TOs will also set in motion learning loops between each chapter of the transformation journey, capturing what worked, what did not, and which interventions mattered.

In the same way that driverless cars moved from speculative fiction to everyday reality, the AI-powered transformation office will one day be an accepted part of the corporate landscape. Transformation teams will leverage technology to push the bounds of innovation and reach new horizons of capability. By embedding agentic AI into core transformation office activities, organizations will strengthen their capacity to change quickly and effectively.

## Authors

![](images/c1c151e9b1295f7d864e281963121d526ed7b635d38ed20f41c6aa64fa94aeab.jpg)

![](images/53d20699229a719d4d9ad61deff09f23c23ea677c33769d1005d955c6ff98281.jpg)

![](images/37db04a001f3646cade3eed7f459ce46318828f7c448bc4460029e047de36a96.jpg)

![](images/ab56c646fb559d6e7e0929dd9263e4b2139f5f4c60fe41fa9d5798f1471e1263.jpg)

## Simon Weinstein

Managing Director & Partner; Global Product Lead, BCG Transform
Seattle

![](images/799d4d698e87eeaf7824512431aae378d3e6c729e9017e2bf07a3bbb45627c65.jpg)

## Riddhish Dubal

Managing Director & Senior Partner
Detroit

![](images/8c8ea3b72e96b9cfa4bf33d34c384d2c1b304e78ed3ffa033724d80ca7e426a0.jpg)

## Emma McQueen

Director, BCG Vantage Dallas

![](images/949a65746296359f320cbd61e0e6d2aabc453b5f4cb26fd9e413c92a14a9e15c.jpg)

## Aman Chawla

Senior Manager
ACC – Gurugram

![](images/b03624b2b8952230da990e9fdeeceeda6c7021a2fc14a2d3e983d62736ff3590.jpg)

![](images/513bf382c9a0fc642b93989ffd386909387cbec4962084f1bced21e59a70f83b.jpg)

![](images/1b46cc3128251756863254feff19116ee4d77fbb7e2d78b66b2a6ab04a582f89.jpg)

![](images/cb3630857c60296bec06b0e0801c6c3b988d6a366d6169304a2bc458fa748836.jpg)

![](images/53047eb0c89877b70baea3e70e28195dc6c5b386ba60b61bd2b851aa16a83417.jpg)

## Christian Gruß

Managing Director & Senior Partner
Copenhagen

![](images/3821e5ab8771370047c503a34e159fe10283bf1c2bbc396fa50e073c0e414ea5.jpg)

## Paul Catchlove

Senior Director – BCG
Transform
ACC – Boston

![](images/58cc01ed360b144d538f54ce3fe6f4be4dd128c7830b5e525afc0cb57a615701.jpg)

![](images/fb7bc223e41b777684b624c57bfe3814a45982a39e3b03bd0aa2aa8e6e20b05d.jpg)

Director
London Canary Wharf

![](images/d253cf5219b973c243e17c084e0428d8f91abcd47b1ec1e130cc8e4925d32447.jpg)

## Natalia Pridacha

![](images/31031988036f31797175b5a3c9c2c6cbfbef50fee7b7620f43eb43c2fa26e694.jpg)

Global Practice Area Senior Manager
London Canary Wharf

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
