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
BCG

Executive Perspectives

## Driving Sustained Structural Cost Advantage with Applied AI

Cost Management

July 2026

## Introduction

The performance gap between AI leaders and everyone else is widening — and it is now visible in the P&L.

Companies at the forefront achieve three times greater cost reductions, 1.6 times higher EBIT margins, and 2.7 times the return on invested capital relative to peers. Yet only 5% of companies are generating AI value at scale, and 60% report no material gains despite substantial investment.

Depth of commitment to applied AI — the deliberate deployment of AI into core operations at scale — is what separates companies capturing structural value from those running disconnected pilots.

The firms pulling ahead concentrate Applied AI investment in their core, redesign processes from the ground up, and hold themselves to hard P&L targets — managing both the cost AI takes out and the cost it puts in.

This guide draws on BCG's work with clients across industries to help CFOs, CIOs, and CTOs cut through the noise on three questions:

\- Where and how should you invest in AI to realize value and reduce costs?

• What differentiates successful AI programs from those falling short?

• What does it take to activate change at scale and cash the check?

In this BCG Executive Perspective, we show how leaders achieve three times greater cost-out than peers, and reshape the P&L with applied AI.

![](images/0d9229ac56bc4f3899ab240d0eae6838ac030598d6eb63e7d4073b9bb24df00b.jpg)

## Executive summary | Drive sustained structural cost advantage with applied AI

## The performance gap is widening, and now visible in the P&L

While 82% of CEOs are more optimistic about AI's ROI than a year ago, only 5% of companies are generating AI value at scale, and 60% report no material gains despite substantial investment. Future-built companies achieve three times greater cost reductions, 1.6 times higher EBIT margins, and 2.7 times the return on invested capital relative to peers.

The pattern reflects a fundamental challenge. AI's primary impact is on productivity, an output concept, and translating productivity into cost requires deliberate action.

Five traps prevent most companies from making the translation: fragmented initiatives at insufficient scale, AI grafted onto existing processes amplifying low-value work, deep programs losing momentum without early proof points, investment stalling while waiting for certainty, and productivity targets set without matching cost targets.

## Depth of integration determines who wins — and reshapes the P&L along the way

Firms capturing structural value share one trait: they have embedded applied AI deeper into their operations. Value compounds as firms move from chatbots and copilots, which assist individuals on tasks through AI-powered workflows that automate predefined steps, to autonomous agents that complete full tasks end-to-end, and finally to multi-agent systems that run entire processes across functions.

Each wave shifts more deciding and acting from humans to AI, and cost-out compounds in the later waves as AI moves from executing steps to running decisions. Many firms remain in the first two waves and capture only a fraction of the available value.

Applied AI also reshapes the cost base. Labor and external spend decline as tech and consumption costs rise. CFOs who shape this shift deliberately turn applied AI into lasting advantage, those who do not, see savings on one line quietly absorbed by rising costs on another. Cost performance is now a function of applied AI maturity, and the gap between leaders and the rest is becoming structural.

BCG's experience with AI leaders across industries and functions reveals five management actions behind successful cost transformation:

## Five management actions translate applied AI into sustained structural cost advantage

\- Scale the core: Concentrate AI investment in your core capabilities. Scattered pilots across the periphery rarely reach the P&L.

\- Redesign processes around decisions, not tasks: Map decisions first, then automate around them—grafting AI onto existing task flows captures a fraction of the value

\- Fund the journey with traditional levers: Early wins from traditional levers, amplified by AI, create financial runway for deeper investment

\- Commit and accelerate: Have a clear business case, not a precise one. Waiting for full ROI certainty costs more than the tokens you save

\- Set hard targets and enforce them: Productivity gains do not reduce cost on their own. Set hard headcount targets and make new behaviors unavoidable.

## AI adoption and managing costs remain top priorities for CEOs, yet many companies are failing to translate investment into value

Top strategic priorities for 2026
Share of CEO responses

Manage costs and operational efficiency

65%

Accelerate AI, digital transformation, and innovation

62%

Drive growth and market expansion

59%

## CEO conviction on AI is rising ...

82% of CEOs are more optimistic about AI's potential for ROI than a year ago

## 72%

say they are the main decision maker on AI in their organization, twice that of last year

## ... but intent is not translating to value.

## 60%

of companies are not achieving material value from AI at all, despite significant investment

## Linking AI adoption to cost reduction is harder than it appears. Five traps prevent most companies from translating AI into structural cost advantage

In 2026, AI investment is projected to double $^{1}$ , yet 60% of companies are not achieving material value from AI $^{2}$

AI's primary impact is on productivity, enabling people to create more, faster. This is fundamentally an output concept, not a cost one

Translating productivity into savings requires deliberate, structural action

1. BCG Build for the Future 2025 Global Study (n=1250); 2. BCG AI Radar 2026 Survey (n=2360)

![](images/79ca317defef24b0ee3f55c7f2a8556f9c80750da3e4eb8af693ad00f37b591f.jpg)

![](images/1afebbed4cdb306dca49b96c17970e96f9a7fb23ba9cd50677f11af0187e0e6c.jpg)

![](images/5aa75c3c8ddf3b47284746fac3a267cbd8d7558c9f98f67c18e168bf9e80428f.jpg)

![](images/95c4b6f3d074950a651f5492cce4b49815b7df75cf9b5ae213c31f7d7c036ddc.jpg)

![](images/26f1c3a4e838850064ae83849aeb2732e1a7ce86498d498cae17a5b4a64d22bf.jpg)

## Too many fragmented initiatives, not enough scale

Siloed AI efforts with no path to enterprise-wide deployment means efficiency gains go unaccounted for and the business case quietly disappears

## AI grafted onto existing processes amplifies low-value work

Automating activities that should first be eliminated or consolidated makes the wrong work faster — output multiplies, but the cost structure stays intact

## Deep AI programs lose momentum without early proof points

Long-horizon efforts that take years to deliver lose support along the way. Skepticism builds, funding tightens, and programs are scaled back before they reach maturity

## Investment stalls waiting for certainty

Companies slow or defer AI investment until ROI is fully proven. By the time the business case is airtight, the gap with leaders has already widened

## Productivity targets are set, cost targets are not

AI programs are measured on efficiency and adoption rates, not on P&L outcomes. Without hard headcount targets and behavioral reinforcement, savings remain on paper

## Avoiding these traps is what defines the firms capturing structural value

## What was incremental is becoming structural.

By redesigning where and how cost is created, top adopters are building an advantage that compounds over time. Savings fund the next wave of capability, raising the bar for everyone else

Cost performance is now a function of AI maturity

What the top adopters are achieving versus peers  
![](images/81f923d8519e1ba550d058de8b8ca7e56997cf29bb33bff3307fb558d1df6623.jpg)

Greater cost reductions

Higher return on
invested capital

"Future-built" companies vs "stagnating" and "emerging" laggards $^{1}$

## The investment gap is widening. Future-built companies are doubling down and reaping compounding returns

## What an AI transformation costs Firms are exponentially expanding investments in AI...

Investment in AI as share of an organization's revenue $(\%)$

![](images/83d5d0ea16383c3ed568ab727713d97b7e25dcf9b168bfc530c440f8c8d6f0c9.jpg)

![](images/ff144a4f51d5a9a25693618708bbe415aec5fd06f37b010ac85a37f016d0a07a.jpg)

## What an AI transformation returns ...with trailblazers reaping outsized returns

2024 realized % gain in revenue/savings AI delivered, measured where AI investment is concentrated

![](images/91966db0d27b586cbf877e21d9b804c69bbef11245270942ba8440c62d2b2d25.jpg)

Future-built players deliberately allocate significant investments beyond technology toward structural elements, including talent, upskilling, org, etc.

Note: AI Investments refer to all investments needed to realize the benefits from AI, including but not limited to, technology and infrastructure, data and architecture enablement, talent and upskilling, external partners, etc.; Sources: BCG AI Radar 2026 Survey (n = 2,360), BCG AI Radar 2025 Survey (n = 1,803); BCG AI Radar 2024 Survey (n = 1,406), BCG Build for the Future 2025 Global Study (n = 1,250), BCG analysis, AI players defined as "Future-built" vs "stagnating" and "emerging" laggards across 41 AI maturity dimensions. Revenue increase and cost reduction are calculated as a percentage of annual revenue through AI efficiency gains in areas where AI is applied.

## Winning with applied AI goes beyond productivity. The structural prize lies in reshaping your core, not just deploying AI at the edges

![](images/a0f159f5cbdc8e426d746ad1e353986284fb3eca30e44f988d8af7439dde3ee9.jpg)

## DEPLOY off-the-shelf AI solutions in everyday tasks to realize 10% to 20% individual productivity gains

Broad enterprise-wise productivity:

\- Meeting summary

\- Notes drafting

\- Dashboarding

\- Calendar management

\- Data wrangling

![](images/5e997d4693ccc020302d0d9c454d9488e5078a1282978963676d9111a5d84e53.jpg)

## RESHAPE critical functions for 30% to 50% enhancement in efficiency and effectiveness

E2E process and workflow reinvention for productivity/quality improvement:

\- Marketing

\- Customer Service

\- Field Technicians

• Tech/Software Development

• R&D

\- Back-office operations

Critical for sustained
structural cost advantage

![](images/5a15e21de46905bf58641f8b1369141ebd4cb6ff1dd79b8247097cb6a271c8a9.jpg)

## INVENT new products and services to build long-term competitive advantage

New value propositions, revenue streams:

• Reinvented customer experience

\- Data monetization

\- AI-powered services

\- AI in products

\- Hardware to software

![](images/1ab4070999431266658fcb3e58cb78e54f3b952b1fb61df6bebc77fd1e665dc7.jpg)

![](images/44fa5b45841a220b47a71c735cc00584244cd4e78e1a1db7271d06d097a05c1b.jpg)

## How deeply you reshape your core offerings drives structural cost advantage. Most firms remain far from the frontier

Each wave shifts more deciding and acting from humans to AI:

\- Chatbots and copilots: AI assists; humans do the work

• AI-powered workflows: AI executes predefined steps

• Autonomous agents: AI chooses its own path within set boundaries

\- Multi-agent systems: multiple agents coordinate to run entire processes

Cost-out compounds in Waves 3 and 4, as AI moves from executing steps to running decisions

Value disruption

Majority of players operate here

Majority of value captured here

![](images/e3705dec361b2d4a4a0bcc713a143f55589328ec8dadfda653d0d89bc1d8f23f.jpg)

Wave 1 Chatbots

![](images/cf8a6a5262acf0dc6f02c2e54e609f1b35472c35a5d9f7a4f8940437266aba5e.jpg)

![](images/69b1390bde4b6dfb330cf4303f0c30fda0297294a949107ee4a2b27378584321.jpg)

![](images/e0b8191d3f9d26f07cd76be33aedb210d25679082fc7364e4459d106c83da55c.jpg)

Span of technology

<table><tr><td>Technology</td><td>Chatbots/Copilots</td><td>AI-powered workflows</td><td>Autonomous Agents</td><td>Multi-Agent Systems</td></tr><tr><td>Scope</td><td>Single task for individual users</td><td>Single function, select process segment</td><td>Single function, end-to-end process</td><td>Entire operating system enterprise wide</td></tr><tr><td>Organizational change</td><td>Minimal, same roles, new tools</td><td>Moderate, some changes to roles</td><td>Significant, new roles and governance</td><td>Full redesign</td></tr><tr><td>Advantage Type</td><td>Individual productivity</td><td>Speed and quality in a process</td><td>Process automation and cost-out</td><td>Structural cost advantage</td></tr></table>

Magnitude of Value

![](images/06a8ffe2d31757661a985378783c8a7db2c2fbcf00ae78a9b4ea517b08d4adc7.jpg)

![](images/122240f2cf04ba3ada9271ed8caee4806f209ce3e54b6c3ec3d2ccb5afb1132d.jpg)

![](images/9bca85f5ee0a7c92f5c339730d6073e9d99c6ec4475579b169f8eaaa0028bb4c.jpg)

![](images/ae3e27a1b3fdae79d26d79e7abed89f5edbdb88ec604da395b92f6988d3c5f93.jpg)

![](images/a69f4f8c7e445c6f1cb34d795b14eaee7297ba75676538b0dbd71a4d105862af.jpg)

Human executing

AI supported

Data flow

Data

AI augmented

![](images/7a16bf814c323c8384275031fef59cb3a453129622665468357e15413a9a1659.jpg)

AI agent executing #

Human-led / oversight

## AI's integration in an organization and impact on the P&L is determined by how it reshapes work and demand for labor

## Productivity gains expand labor demand $^{1}$

AI replaces core task execution and unlocks talent demand

Insurance sales agents,
IT support technicians

## AI Substitutes Human Labor

## AI substitutes for routine work while demand remains bounded

Call center representatives,
financial analysts

Future
cost base

AI augments human capabilities, lowered costs expand market demand
Software engineers, lawyers, procurement teams

![](images/c47fbabc3be378bf3b2cae407cc2e94291e8c63fb75f92bbc4498af337851194.jpg)

## AI Augments Human Labor

AI augments work, but demand is bounded by budgets or other constraints
Content marketers,
academic researchers

As AI improves productivity and substitutes routine human labor at scale, companies' cost base will shift toward supporting high productivity, high value work where AI augments human labor

Productivity gains saturate labor demand $^{1}$

1. Measured by whether AI-driven reductions in unit cost or cycle time (industry-level price elasticity) unlock additional output (US job openings and turnover)
Note: For BCG's latest perspective on how AI will reshape the job market, refer to https://www.bcg.com/publications/2026/ai-will-reshape-more-jobs-than-it-replaces?

## AI unlocks cost reduction across every P&L line. Quick wins in Wave 1 and 2 can help fund the journey

![](images/b1b74039248aae26ffc8384abfd95f2309eb0dcd89ae20506472829ceb033239.jpg)

Quick wins start in Wave 1 and 2 — procurement spend visibility, marketing content, help desk automation, and engineering productivity typically deliver value in under six months and fund the deeper journey

<table><tr><td rowspan="2">Exemplary high impact workflows (Non-exhaustive)</td><td>Content creation and localization pipelineAI drafts, adapts, and localizes campaign content across markets, replacing agency production</td><td>Finance transaction processingAI automates invoice matching, duplicate-payment checks, reconciliations—driving zero-touch transaction processing</td><td rowspan="2">Spend-baseline and category strategyAI structures PO data into full category transparency. Balances forecast and inventory to avoid stock-outsSupplier negotiation at scaleAI generates and runs negotiation letters across the long-tail supply base</td><td rowspan="2">Drug candidate screening and library expansionAI screens over a billion compounds, expanding the viable drug library 100xR&amp;D portfolio and spec rationalizationAI surfaces highest-confidence modifications, eliminating manual search and GTM effort</td></tr><tr><td>Campaign analytics and lead qualificationAI sets targeting, allocates media spend, and qualifies leads in-flight</td><td>HR and IT help desk resolutionAI agents resolve tier 1 tickets end-to-end—access, payroll, and benefits queries</td></tr><tr><td>Value lever</td><td>Staff productivity, campaign ROIExternal (agency) spend</td><td>Process throughput/accuracyLabor spend (back-office FTE)</td><td>Negotiation coverage, wastage reduction↓Inventory and landed cost</td><td>Throughput/drug library breadthCycle time and trial cost</td></tr><tr><td>Tangible impact1</td><td>20%-40% time savings in brand performance reporting2x quality uplift on concept designs</td><td>~15%-30% of OPEX cost-out using AI</td><td>2%-3% additional savings through AI-assisted negotiations3x-4x faster processes and decision cycles</td><td>40%-50% faster cycle time20% molecular synthesis cost-out</td></tr></table>

## AI-native workflows are the primary cost-out drivers across the P&L

## Sales & Marketing

## G&A

## COGS

## R&D

Redesign, not retrofit: AI-native workflows deliver cost-out and free capacity for higher value judgment-led work.

## At maturity, the value at stake is significant and delivers structural cost advantage but demands sustained commitment

At maturity, the north star is a step-change cost-out across every P&L line.

![](images/dedd4c4adf52849c59d52d6a50b68f4ad6ae442cb3eca469f2022fe7a12a16c9.jpg)  
Sources: BCG POP.X Bionic Workforce Analysis estimated FTE cost-out potential; ranges reflect weighted average across functions mapped to each P&L line. Non-FTE cost-out per BCG case experience across procurement, supply chain, agency spend, and external R&D. Savings apply to addressable spend categories within each P&L line and results vary significantly by industry and cost structure. Ranges reflect full-maturity potential; few firms have yet captured the full value.

## Applied AI structurally reshapes the P&L. Deliberate management determines whether total cost falls

## Example P&L impact

## Consumer Packaged Goods

![](images/8536401de9634033c93b2111fc92020156a6ee7d85f72ff94fa74f147e5aa9ef.jpg)

## Illustrative and directional

## \~25%-45%

decline in labor spending as AI reduces reliance on people-driven processes

## up to 1x

increase in tech spending as technology shifts from support role to strategic core

![](images/dd7dead11587be50836558f887387b8734c2e0322587ed98a8fc64c844fa4418.jpg)

## COST-DOWN

## Cost-down requires headcount discipline

Productivity gains do not reduce cost on their own. A directional FTE or role-count target, tracked through the transformation, is what converts efficiency into P&L impact.

![](images/c39807ba033f631f89ee8110c89855b48473a31412077e7dd007f6797c8ae998.jpg)

## COST-UP

Forecast and budget consumption before i

[中间内容因长度限制已省略]

 up to find efficiencies to reinvest in brands, products, and innovations.

AI was deployed as the key accelerator to unlock savings that would have been too time-consuming or low-ROI to pursue manually.

![](images/fc8a376f549ea390d26df1a249745d301c932a500b822a6ac6e11cc6860fb294.jpg)

## Actions taken

## Deployed AI across the source-to-pay process to unlock savings at speed and scale:

\- Applied AI to build and analyze spend baseline of unstructured purchase order data to establish full category transparency.

\- Long-tail supplier value captured through AI-generated negotiation letters at scale.

\- Leveraged AI to identify historical overpayments, early payments, and working capital leakage across supplier contracts.

\- Used AI to consolidate 100,000+ line items of technical specifications across manufacturing, enabling large-scale rationalization.

![](images/07f827bcd38aac2598782c69947af9b919e2ff33c8c88102f3f73aa177a99063.jpg)

## Impact

## \$900M

Total cost-out
delivered

## 3,500+

Supplier negotiations
completed in <100 days

## \~2%-3%

Average savings per AI-assisted negotiation

## Case Example 4 – Research and Development | A global pharma company used AI to reimagine its small-molecule drug discovery workflow

![](images/11f1c0029fb27b101e74efbb06f51a4155ba842238257d862863ecf2ed924523.jpg)

## Context

A global pharma company faced mounting pressure to reduce R&D costs and accelerate time to market across its small-molecule pipeline.

The classic process was slow and manual, given data and capacity constraints, extending optimization cycles.

The company partnered with BCG to redesign its drug discovery workflow end to end, deploying AI at every stage from candidate identification through lead optimization.

![](images/172d01c0c52476cd169bd65382985c6a30a76e731a019c0764bbfbfcbc6026d7.jpg)

## Actions taken

## Deployed AI across the drug discovery workflow to replace manual processes and compress cycle times:

\- Used AI to screen over 1 billion compounds, focusing investment on core drug discovery, and expanding the viable library 100x.

\- Applied AI to analyze over 500 million molecule modifications, surfacing highest-confidence changes and eliminating manual search time.

\- Built end-to-end pipeline with AI-powered algorithms to optimize drug candidates across efficacy and safety properties and reduce cycle time.

\- Deployed AI-integrated lab robotics to redesign the discovery loop, feeding experimental results back into the model with minimal manual intervention.

![](images/c46671a08be81cfde226a9754648c8b805a81e825189d7b72bbbca5c6e6b7beb.jpg)

## Impact

## 40-50%

Cycle time
acceleration across
discovery

## 20%

Molecular synthesis reduction for cost-out

100x

Expansion of viable drug candidate library

## BCG experts | Key contacts for driving sustained structural cost advantage with AI

![](images/bf17247643a2241a370ea8613025001f599b87cfdfcf42ee9237e0a1e104ae55.jpg)

## Americas

![](images/9df61ffedcd2b72bc6f0133f185b77d4a97a662209c6242d7732c7b99ffe09de.jpg)  
Managing Director and Senior Partner Washington D.C.

![](images/915666de877955e4082e85e9809387205b1afdb06b68bb0b7053bd5c1b7fd003.jpg)

![](images/7a38536f32584de940aee452ff07ef4cf9a6ddad184c3cf9a1d9258dd1b29140.jpg)  
Kevin Kelley
Managing Director
and Senior Partner
Dallas

Paari Rajendran
Managing Director
and Partner
San Francisco

![](images/187c22a45a70ce21c67d5f9472e800c78a8475ef312cf7216d7e12557fdf99f7.jpg)  
Geraldine Rhodes
Managing Director
and Partner
Washington D.C.

![](images/6a8771d79183c1a50a871a3efd5f4ce9ee928c67161ae85f3cd9b286eba88542.jpg)  
Laverdiere
Managing Director
and Partner Houston

![](images/d53f6af44feb973754f190e239e940df4638c1ab5ea74651e4477e6c7fd9e7c4.jpg)  
Paul Goydan
Managing Director
and Senior Partner
Houston

![](images/baed5901c108124c4b0d80b14cd519d69d8e96c4083676715294acf51b2df70e.jpg)  
Dylan Bolden
Managing Director
and Senior Partner
Dallas

![](images/21e9c0f9c0772f108cda6398242ac99d2f3e637c0365d07a17e8337d2a082b32.jpg)  
Matt Marchingo
Managing Director
and Partner
Houston

![](images/f04ada93f36585b5fee50939b76755ed971e436c943c98a39ab73b41a8022a74.jpg)

![](images/52988689fe9c1d7fd8d8605fc0ae12ea7fb5588eed4085f6b55de48d6dcab23c.jpg)  
David Martin
Managing Director
and Senior Partner
Dallas  
Abhinav Verma
Managing Director
and Partner
San Francisco

![](images/9462535f1266e286cda52794f749e61965328ab54867f966645bd1c20b923480.jpg)  
Paolo Vicino
Managing Director
and Partner
New Jersey

## Europe, Middle East, and Africa

![](images/15d1110ea50c31c9b17cb9e8e88d9696ba000f5cee624a63856dc6e6ebcac1e0.jpg)  
Nicolas De Bellefonds
Managing Director
and Senior Partner
Paris

## Asia-Pacific

![](images/ab012ef0541d379009f393c6216f5ed220905caec19f720bf7882dd559834e7a.jpg)  
Kosuke Uchida
Managing Director and
Senior Partner
Nagoya

![](images/c3cb0353c7d471ac3076f8a0ade88fee71fcbc47d44b7d7c4e73318e4c275c50.jpg)  
Olivier Bouffault
Managing Director and
Senior Partner
Paris

![](images/f923e2df15ca398ebc7d850051a85a37a985c743243f8fe27a0d8f26df5aeae6.jpg)  
Romain de Laubier
Managing Director and
Senior Partner
Singapore

![](images/1db8c3eba426f8559079a200cfff323c47c37c3657e49d7347d0898cd329cda4.jpg)  
Jacopo Brunelli
Managing Director and
Senior Partner
Milan

![](images/1c25bc6ef7937401d6e1185e1540590baed930834a1532bccce2b79a0395e832.jpg)  
Michael Grebe
Managing Director and
Senior Partner
Munich

![](images/ecbef1e22a35e49a0d16cf6b506066556b592acdb24cbe206e29ddba4c2869b5.jpg)  
Jeff Walters
Managing Director and
Senior Partner
Singapore

![](images/68b6be13ed6c327aceffcc49deb87fb02bc99a5886f9c484f16e08b27d7512d4.jpg)  
Alex Dolya
Managing Director and
Senior Partner
Singapore

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
9. 输出前自行核对：标题与导语不重复；每个小标题都是完整判断；没有元话语、推广语和未解问题栏目。只输出最终 Markdown，不输出核对过程。
