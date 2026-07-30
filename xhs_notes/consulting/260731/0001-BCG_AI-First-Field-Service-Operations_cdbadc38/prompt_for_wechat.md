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
BCG

Executive Perspectives

## The Future of Field Service with Applied AI

Field Service Operations

June 2026

## Introduction

We meet often with CEOs to discuss AI—a topic that is both captivating and rapidly changing. After working with over 1,000 clients in the past year, we are sharing our most recent insights in a series designed to help CEOs navigate AI. With AI at an inflection point, the focus in 2026 is on turning AI’s potential into transformative impact through applied AI, with agents at the center.

In this edition, we discuss the future of field service and the role AI can play in turbocharging growth, productivity, and new business models. We address key questions on the minds of field service leaders:

\- What should my team look like? Will I need a different team or can I upskill my team?

• How has AI been evolving, and what role can AI agents play in field service?

\- How will the economics of field service change, and what’s the ROI on AI tools?

• How should the customer experience evolve as a result?

\- Which tools are best suited to my goals, how do I get started—and how do I get this right?

This document is a guide for CEOs and field service leaders to cut through the hype around AI and AI agents in field service and understand what creates value now and in the future.

In this BCG
Executive Perspective,
we articulate the vision
and value of the future
of field service with AI

![](images/6a8de41d2d2b18637c7694aa9e576b04fbebf5020d892b20d3f6b9af16fc4042.jpg)

Oil and gas

## Background | Field and aftermarket services

## Overview

The field and aftermarket service function consists of installation, repair, maintenance, and replacement services for high-value industrial equipment

Field and aftermarket services often require technicians with highly specialized skills, traditionally gained through experience

## Value chain

Service sales funnel

Service operations management

## A field service function has four parts of its value chain with various activities

Customer relationships

In-field repair and maintenance

## Key activities within key steps

\- Sales reps help generate and convert leads to repair, maintain, replace, and install high-value equipment, as well as help develop and negotiate contracts and pricing with potential and existing customers

\- Operations managers oversee the operations of a field service business and are responsible for ensuring smooth operations by monitoring

• Operations managers are also responsible for maintaining the financial health of field service units

• Service technicians perform diagnostics, repairs, maintenance, and installation services at customer facilities

• Service technicians are responsible for maintaining institutional technical knowledge and training newer employees

\- Customers reach out to solicit services from FSPs (field service and aftermarket providers)

• Sales reps engage with customers to ensure high-quality service is delivered

## Field and aftermarket asset examples

![](images/8f4f0316a6bf8b2b3f432d241e47a76e97235be48663fbb90d2916d0d3b8c77d.jpg)

Building services

3M+ HVAC units replaced in US annually

![](images/a1e74f70c9e5f7572eef41a2c33ebf58f3e4f0d0c052b1438106b055b8ce0d17.jpg)

![](images/d3adc16313cc18dcb6c7b811a1a499556fe94d899118d1482aebe160084e0964.jpg)

5,800+ aircraft in US commercial fleet

## Offroad heavy equipment

318,000 construction units sold in North America in 2022

![](images/5e85b8a58850e819788b1d149adbf744992e81cc85ec148f2284e0667acb7518.jpg)

19M barrels per day in US refining capacity

![](images/190fbb575da1b1ee1de6ac784b6a4647f5fa7169ec5102b540acf38c7b1f81c9.jpg)

70,000+ wind turbines and 5,000+ solar farms in US

![](images/9268636e13add3fce1ce373a674f1c3290cc00c9c148974885a22b99e25ea41d.jpg)  
Tech and telecom

![](images/d439550669f0a42e78d66e63fded9e4724981f64ea3686b483e2854fcd5b4bfd.jpg)

5,000+ data centers and 140,000+ cell towers in US

11,000+ MRI systems in US

![](images/c07ec69dcae8eaf95211344824f198c70f6cd68e59c0c403a4025f63e6d4b9cc.jpg)

40,000+ F&B processing plants in US

Note: F&B = Food & Beverage

## Executive summary | Transforming to an Applied AI-enabled field service organization

The time to act on applied AI and AI agents in field service is now

Field service functions are facing global challenges such as technician shortages (costing the trucking industry alone \$2.4 billion annually) and unplanned asset downtime (costing industrial manufacturers as much as \$50 billion annually)

There is an opportunity to drive 15%+ revenue impact and 5pp+ gross margin impact through applied AI and AI agents in field service

This is because field service as a function is rapidly approaching an inflection point, with emerging technology trends and developments delivering transformative impact, including:

\- Connected equipment, which is becoming a new standard, as machinery data and analytics unlock value in operations

\- GenAI technician copilots, which are unleashing productivity and creating knowledge bases across technology generations

• AI agents, which are reshaping ecosystems for service execution and communication

These technology trends are enabling a step change from traditional field service to streamlined, expedited, and augmented offerings, increasing the value potential of the rapidly growing field service function

## Applied AI and AI agents can reshape field service teams

Sales (service lead generation): 30%-40% more leads from connected assets, AI-based monitoring, and proactive targeting using AI agents

Operations (productivity gain): Coupled with continuous operations improvements, AI drives a 20%-30% lift in productivity via smart dispatching and scheduling and in-field support tools (e.g., troubleshooting copilot)

New revenue streams: OEMs further develop offerings, including premium service contracts and outcomes as a service

Technician workforce: Institutional technical knowledge is maintained and easily shared, accelerating the training of junior mechanics

## Executing successfully requires a transformational mindset

To successfully deploy AI and AI agents in field services and drive outcomes at scale, organizations need to have a portfolio and transformational mindset; to combine GenAI, predictive AI, and AI agents within the technology stack to enable team members; and to rewire the operating model to focus 90% on people and process change

Field service leaders play a critical role in driving this change by sharing best practices, breaking down siloes between teams, and making bold investments in technology and upskilling

To get started, define your objectives and North Star, prioritize use cases, start with PoCs that demonstrate value, and scale up successive waves of capabilities while enabling the field service team

![](images/36d5e1b04b9301fc1b428b9103d24bf05a254a11f43c1a33fe2f698454a0d54a.jpg)

## Field service functions are fraught with pain points

## Service sales funnel

![](images/cc9e77a2416fb55553273181c76d37cb15fc20c662c1fa52ab276e953b61ed5b.jpg)

## Sales rep

Reactive selling limits
growth opportunities by
failing to anticipate
customer needs

Static pricing models and lack of customized services leave value on the table

![](images/d251d7cb7c7ebf88a10cb1e695af77491f6e3904d224ca409ffb3298fe7d6dfe.jpg)

## Service operations management

![](images/1066d748f4a67ecaa0542baab21d8708f866000547588811013f007ff70e9efa.jpg)

## Operations manager

Limited visibility into team productivity, effectiveness limits standard work implementation

High turnover leads to loss of critical expertise

Underutilization of IoT and connected data hampers operational efficiency

Note: IoT = Internet of Things.

## In-field repair and maintenance

## Service technician

Delays from unavailable parts and inefficient routing waste valuable time

Lengthy diagnostics and insufficient onsite support reduce technician effectiveness

![](images/d8a828a4b8b8962404a4408e44fc7d00dea27115bdb62e4cf9f74be44c98f9e5.jpg)

## Customer relationship

![](images/5331c3113055c3e23cb0572cb5d89141172af650d9ef86266519b44290dfe731.jpg)

## Customer

Reactive service leads to prolonged machine downtime and higher costs

Limited transparency into service progress frustrates customers and extends repair timelines

## Pain points continue to intensify due to a shortage of technician talent

## Example industries with a persisting, constrained supply of technicians

![](images/575212f51c66e8c46eb55909a7acf78aca66a68f5842c81c8a15ee34039aa710.jpg)

## Building services (HVAC)

![](images/e6efbd649a786953668b3c630881fb4cd3ff2f33d7c5a9e3e4126d2e7674ba25.jpg)

Aviation

![](images/b77f05366588ad3a87f07de95cfe013c905b72974efbd4810714120c6037d21f.jpg)

## 15%

![](images/215fc6e8821caaf284639f556c9407698599756a5302a65a37a6b3a36dcce0a6.jpg)

Greentech (wind power)

Growth in HVAC US technician demand, outstripping 6% growth

## 10%

Shortage of certified mechanics in 2025 (2036 gap only narrows to 7%)

## 124,000

Worker shortfall in wind energy sector projected for 2030

## Health care equipment

## 7,300

Biomedical technician openings added per year; only 400 graduates to fill them

## 40 years

Average technician age, implying high retirement age

## 54 years

Average aviation mechanic age in the US

## 42 years

Average age of wind-turbine technician in the US

## 45 years

Average age of biomedical technician, implying high retirement age

![](images/b15ac861fec925d1119e92454dfc3bebfd36120b0394ebf3c71a7ff53612badd.jpg)

Beyond raw shortages, companies face an accelerating brain drain: Retiring technicians carry decades of tribal knowledge, while incoming junior technicians require rapid retraining, compounding the challenge

![](images/e718588172d213f58290b97de87789113aba4989ba898ee8d77a9d0f9fa29974.jpg)

## Successful companies overcome pain points through a set of AI solutions...

## Service sales funnel

## Hub performance, lead generation, and advanced pricing

AI agents identify opportunities and initiate actions (e.g., automatically generating work orders and conducting initial analytics) to triage and price opportunities; agents assign work orders to robots and humans

![](images/cbcc180180617188321c5adbcccbfe64e0508c97b35f865f79c31c6027746718.jpg)

## Service operations management

![](images/b2426c33bef6dca2153e6b660a988945514254363d1c12807b9b8d11b239cbc0.jpg)

## Real-time schedule rebalancing

AI agent rebalances schedules in real time based on routine tasks and emergencies, skill, capacity, and demand, autonomously adjusting assignments

Optimize schedules on the fly to manage robot and human dispatching

Part inventory and management
AI agents sense demand and autonomously replenish and allocate parts across the network

## Customer experience and support

Customer portal enabled by AI agents to provide equipment insights, coordinate maintenance, and, in some cases, to make remote fixes

![](images/34f6926c1ce186d45b6f6f77cd08e8d727c17f64222301fc6017bdd7a8fd063d.jpg)

![](images/210aabe618e5e40e26040c3721575b6db5c3f876a4cbff00966ae0d7e8dcdedd.jpg)  
Note: These solutions are examples and do not all have to be employed to see value. AR = augmented reality.

![](images/2988d92836ed7c0776c670857a5dc047c83abebcf41bd2b22bf050f615e03b87.jpg)

Illustrative

## In-field repair and maintenance

## Robot conducts initial imaging

Initial Imaging
Robot technicians (including drones) conducts onsite analysis (e.g., via thermal imaging) to better prep technician with right parts and context

![](images/d44ecb0b69b1106bf2cdf6ad6fbcb20379bc753b24e77428aae12e6e91191aeb.jpg)

![](images/2601c01a2cd187c3767762441e9cc2c8c5e30fe5636dd371f64e75a185385496.jpg)

## Technician completes first-time fix

Human technician with right qualifications arrives with right parts and context; receives remote guidance (enhanced by AR) to complete a first-time fix

![](images/21ba70ea2aad007f2139754d42b7d9ba8c2822edfd4d748abb7c0746fb6ec362.jpg)

Automatic job
summary
dramatically
reduces manual
data entry

![](images/7ed314c08900a016dce88c3dcc99ebe90c3ff5fbff0db21ae50a6a2534a07a0c.jpg)

Enhanced tools drive efficiency

## ...which impact their org but enable focus on highly complex activities

## Current Future Future-state focus

<table><tr><td>Persona</td><td>Key activities (examples)</td><td>Current</td><td>Future</td></tr><tr><td rowspan="4">Operations manager</td><td>Scheduling technicians and matching with appropriate jobs</td><td rowspan="17" colspan="2"><img src="images/0f94f0ec912f4495c9c6b1cccefbfc5136d19e94a31c4a8b5abf3eed004465d8.jpg"/></td></tr><tr><td>Inventory management and procurement (including parts stocking)</td></tr><tr><td>Customer relationship and consultative activities</td></tr><tr><td>Monitoring operational and financial health</td></tr><tr><td rowspan="7">Technician</td><td>“Wrench time” (repair, maintenance, and replacement activities)</td></tr><tr><td>Commuting between job sites and headquarters</td></tr><tr><td>Troubleshooting and identifying root cause of malfunctions</td></tr><tr><td>Looking up repair literature and identifying necessary parts</td></tr><tr><td>Recording field notes and documenting job performed</td></tr><tr><td>Customer relationship management and onsite sales</td></tr><tr><td>Training and assisting new technicians and apprentices</td></tr><tr><td rowspan="5">Back-office staff (including sales reps)</td><td>Creating proposals for quotes</td></tr><tr><td>Developing, pursuing, and converting leads</td></tr><tr><td>Administrative activities (e.g., invoicing and billing)</td></tr><tr><td>Customer relationship management</td></tr><tr><td>Warranty claims and registration</td></tr><tr><td>Customers</td><td>Waiting for assets to be repaired (downtime)</td></tr></table>

Time spent performing activity

![](images/3998ed24302cb1d9d196ff219e3b4ec19d8729d2a6bd7ecea90b7d13da557c83.jpg)

Low complexity

![](images/6e89ead7784b3fe8e2a98850c26373b372d4e96a447df45c4615a7697a209126.jpg)

Moderate complexity

![](images/6119b8c00cefce344ea6a44c36c99b4fbffadd79a6c2596d51992de3d6f74e26.jpg)

High complexity

Time spent on nonrevenue-generating activity is repurposed, allowing managers to increase focus on operational and financial health of business

Reduced time spent commuting, preparing for jobs, and other nonrevenue-generating activities; that time is repurposed to allow technicians to increase “wrench time,” leading to more jobs completed and, in turn, increased revenue

Sales reps and back-office staff improve efficiency, reducing total amount of labor required to perform same volume of tasks and, in turn, decreasing operational costs while allowing sales reps to provide a superior customer experience

Superior customer experience

![](images/4a3cbb71c4ea723aa2b993a78e4c960809c86ba3436a38c094c62af214e6e89a.jpg)

Increase in time spent

Decrease in time spent

## Long-term impacts

## \~20%-50%

Increase in
management spans $^{1}$

## 1.5x-2x

Boost in productivity
of technician
workforces

## \~30%-50%

Increase in
management spans of
back-office teams $^{1}$

## As a result, successful companies see significant value

## Revenue and profitability unlocked in parallel to improve efficiency in future state

Illustrative example: HVAC field service technician Joe doubled his profit index by leveraging the various digital tools implemented at his field service company

![](images/3d470fa571b585a5a6af38c31449e2721558b70b494872dfbdf1493db6ffe27c.jpg)

Commercial growth

![](images/a49eefe563571274665cb9e3d813e837edaaed38a2b5ccb4e4bbfa3f0a9cdd36.jpg)

Elevated service

## 15%+

Revenue growth

## 20pp+

On-time maintenance
completion uplift

## 5pp+

Service gross margin uplift

## 15%+

Average Job duration decrease

## 1.0x profit index

Examples of AI changes

Parts look-up platform helps technicians identify components for jobs quickly

## 1.8x profit index

Automated warranty software assists with warranty activities and registration

![](images/feb2ad9cc0be47e963dd203aa04756a1c487b3d399a58c33af04593cf9624b13.jpg)

Automated-configuration tool expedites configuration process for technicians

Higher value per customer

Reduce commute time

Increased technician productivity

## Key insights

![](images/985b84d13f6186920657e727c7200d68e2aae3fc851ba6664ab6cc381287eb7e.jpg)

## Every company starts somewhere:

Tailor your approach to your current technology stack and organization readiness; generic blueprints do not work

![](images/5a79f785eb424b439d43400b738f268f95639164bedc9d8c1645396e1e25f622.jpg)

## Recognize long-term teaming

impacts: Anticipate how team composition shifts as AI matures, and drive adoption through change management

![](images/3021d8a911241ade2f3710ccb9fade058c10007afc7788636b739ca1fc875e09.jpg)

## Get to value fast and scale

smartly: Identify high-ROI use cases first and build a roadmap that proves value before full deployment

![](images/94f61903d9aefcbef75038335a46a7c189fa0918064840a7f14b1ed5080f2429.jpg)

## The adoption of AI is accelerating, especially with the advent of AI agents

## AI adoption is accelerating...

Millions of field workers vital to the global economy will quit by 2030: here's how AI can solve that problem. - TechRadar, July 2025

AI-Powered Dispatching Gains
Momentum as Field Service Companies
Seek Operational Efficiency
- Analytics Insight, March 2026

iOPEX Unveils 'FieldPilot', Bringing Agentic AI to Field Engineering Services - Business Wire, March 2026

Miele Deploys IFS.ai Globally to Transform Field Service Management Across 25+ Countries
- PR Newswire, February 2026

![](images/7c0c01574d3c861758a7c76f67412f2ae3d82b48329d4c492f12498d5e0e2324.jpg)

## ...and heading to the next frontier: AI agents

FRONTAL CORTEX
ABDUCTIVE REASONING

Observes, plans, and acts autonomously
Leverages both predictive and GenAI

AI agents

## LEFT BRAIN DEDUCTIVE REASONING

Focuses on
structured tasks

Solutions are highly explainable

## Predictive AI

![](images/05ed7d3dd71cd59700a29a7da01c524dda993a0f7459570a2b791a4a36bbd4f4.jpg)

## RIGHT BRAIN INDUCTIVE REASONING

Tackles unstructured problems
Focuses on creative,
imaginative, associative, and
open-minded solutions

GenAI

Note: GenAI = generative AI.

Accepts
result

## AI agents have enabled more effective workflow execution

## Agentic AI

## Predictive AI

![](images/49f85e2e7e964a04b78ec176f1f33e263db50db73f78d87c6a0c43daa4ff5d02.jpg)

## AI first (2026)

Predictive AI,
GenAI, and AI
agents more
effectively execute
workflows, which
are being reshaped
around AI
capabilities;
humans supervise
operations and
safeguard quality
of outcomes

## Agent led

Agent acts without any explicit human oversight

## Agent orchestrat

[中间内容因长度限制已省略]

ng agents into processes (e.g., dispatching and diagnostics)

\- Ensure ethical and governed agent autonomy

![](images/ae7e637d2d661b979b89b91ede57399a12646ae6d3a9f7cc6605ed72b00d2637.jpg)

## Culture and effectiveness

\- Deploy modern collaboration and communication tools to support human-agent interaction

\- Refine KPIs to reflect human-agent productivity gains

\- Introduce incentives to accelerate adoption

\- Apply user-level monitoring to track agent performance

![](images/32b6a4680bd9e22069ed7190b0fd4c8c7f28d3f4d80b65700d4c2e88234d3fb0.jpg)

## Training and enablement

\- Implement rapid training for field service teams

• Develop AI and AI agent champions to act as multipliers

\- Activate AI and AI agent leaders and champions in service teams via train-the-trainer initiatives

## To begin unlocking value in field service with applied AI and AI agents, three main steps are required

![](images/32559ab533a9f6a45cd1f7c7d4170ce71104656bd377c139116f581cc32fe08c.jpg)

![](images/ade52bf234784ddfb64bede37a6d2131eb532c38aab44df5649ac07bbebe7fea.jpg)

## Execute rapid diagnostics

![](images/2fcb66836c45876216e33c2900df4483f5382203c2a57a4c8b77eb507d32d6b3.jpg)

## Conduct PoCs exercise

\- Rapidly identify pain points within the core service business

\- Prioritize field service AI modules across value potential and relevance and ROI and draft a roadmap for design, business case development, and feasibility testing

\- Design pilots and PoCs for relevant field service AI modules and identify implementation challenges

\- Reimagine the future with product strategy, vision, and scope; leverage these inputs to finalize a business case to drive initiatives

• Prove and test feasibility of solutions via digital and AI PoCs and transformation pilots

\- Complete roadmap for the build phase (which includes resourcing and governance)

![](images/629b87436cd9a5b503ff2e7ab2f7dbf51f471bb856a0f9593a3efd8d8cc06235.jpg)

## Build, pilot, and iterate

\- Iteratively build digital AI solutions and deploy in market to test and learn, while maximizing the near-term value captured

\- Enable core capabilities, such as user testing, technology enablers, and agile methodology

Julia
Dhar

## BCG experts | Key contacts for the future of field service with applied AI and AI agents

![](images/c6ffc8f43839e25555c99b42b80054fa3274af303778c80a33e18e5f1c16805e.jpg)  
Decker
Walker

![](images/c3176a9655d1a36ecf96417ca05d757d2f734049be0d25dbb1eaaccdb7d21fed.jpg)  
Andy Lin

![](images/859020f2f6a282e2725f65a0a706a9225f94c87952e939a7e642faf1241dd58b.jpg)  
Hunkar Toyoglu

![](images/3fde39317ee4440341b2ccd1d0f86c93cce91e82e04bd2bafe4fee10a3bf53bf.jpg)  
Justin
Rodriguez

![](images/34447359e0cd1dc7eeee688cbb7bf346f0f73b7f973658345bce414e3555291e.jpg)  
Tibor
Mérey

![](images/43d34cee7aae1dfa3e793e9230096c411c4f5d7c17ce804fbda6f7046bfaca6d.jpg)

![](images/a1d1fcffdccbdb7c432914d5889688f374b655bbf5531cb6c96a2e2628aa6f13.jpg)  
Martin Fink

![](images/580fc22bd0708d6bf1c8415b8a24e08572d3b0945b17767d0d642bc32bb28a5c.jpg)  
Christopher
Spafford

![](images/671de9cfd95a9330f6f0da13359e45c0bf5332594bb6ef5cd66db073268aa7ad.jpg)  
Ben
Vermeer

![](images/c4874451e0672e86b6d61095438bd67c3645cb5c67617187f782cc3192556e03.jpg)

Nico
Geisel

![](images/955a7e75f86b66b4fe6b063bedb5090653c3ba61201edf4dd85c175cb65154ec.jpg)  
Sebastian Köcher

![](images/d2a9c5c0b80aa087fedb43f606783b4878110eb137c5b79ec26845f7b87f1f53.jpg)

Ashkan
Afkhami

![](images/05ca25a06de85a2b2977361a037dbe48f4cfc4ce865f00cc756ffcfb68a98803.jpg)  
Tristan Mallet

![](images/0b2f5cf3dcaf5fa8548aad0cc6dfb263346b672a83500f07f9bf716e2c3e3d25.jpg)  
Ramsey Baker

![](images/3b528521d5e82879f35502ebeb3817f12ae8d9d11317e2788e29a41de1ff4616.jpg)  
Rachel
Stanford

![](images/27c7a16a976b25c8a82ac413ed54f43171565f63f3b57ab894f831399a39262e.jpg)

Michael Troisi

![](images/f02c61345f5f87ce51621399cb285868139cb73e4f9556b518a3895bd31b6219.jpg)

John Snipes

![](images/96a87240da14a3dcc498f31c8187c342418b7bcb8ca5135387992ff133077ac5.jpg)

Guillaume
Coiraton

![](images/bf8d42059a0cc49ee0fd2c146e176b62a0180acaf8eb55943b86cc953234ba85.jpg)

Ian
Stuart-Hoff

![](images/c5e0a919fa80a17cf9d383802f6cf6b0b11cc7e20b9de5b2dfbb88f44e0561d9.jpg)  
Laura
Juliano

![](images/cdad12d3f5502d50baa689a51320440b0087099856a78f316479c9e9468b77cf.jpg)  
Mike Quinn

![](images/c38647dfa575df8c777ef3aacc223fc41f681061ac8ee8b3c09700cfda9c2f96.jpg)

Vivian Lee

![](images/19f9f8be38f1f5ea8eedeb8533fb1bd3d6ecf5f3cf8b15768503c1167f2401cd.jpg)

Brian
Hirshman

Charles
Gildehaus

![](images/52b5c9ca89b368bfd90f35661c2675ec286bf4a28e607c7ec1caea3777a9c731.jpg)

![](images/e96c486077b5de14689ae6a0ccef83baa7f04d8e7aac677b825975ad9d3770ac.jpg)

![](images/647e29c6c1d0d2410e2db87d8f6eab5ede0c375c1075eced2821bbd27fb18499.jpg)

Marcus Wittig

![](images/6a82e2284729246df4c4179d7602cffbc1ced51871f2200bbfca6f25573be238.jpg)  
Andrew
Beir

![](images/921e87854392d6e35c3c9ace9e8d454a64430d144ba7b499a681a825b001b04f.jpg)

Aisha
Taylor

![](images/fb62d113a6de2f339dcae7854788c00ee2c2bbc082bad63a59c540a4a8bb98d6.jpg)  
Dutch
MacDonald

Lacy
Ketzner

![](images/d9899688f7bbcfa55e279e73ced0a09b927172440e5705b6d59a840d2fe885d0.jpg)  
Mohammed
Omar

Dominik
Deradjat

![](images/097ff0c17991a957c6571bf7c5762eca5e3e526b295021a0a33784b3506d5555.jpg)

![](images/ad9349adeb7f3124991b074c61b27db8384e08d469cc3c07a0af6f5c82296d6a.jpg)  
Jeff
Ahlquist

Shashank Modi

![](images/25c4dc06117d6bda868e38e8dcd3bb2d0f1e4513ca9ca3c3ecbaef0b73ff8184.jpg)

![](images/d726878e2a9493954b901495dd6f4cdbd80a08febd0060dc5bdf1f513eb0179e.jpg)

Michael
Dahle

![](images/ccf9d12d5aa35c42857f1c9705754a6a83311703baf806b5d09ecacadee3d394.jpg)  
Mike
Dahlmeier

## BOG
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
