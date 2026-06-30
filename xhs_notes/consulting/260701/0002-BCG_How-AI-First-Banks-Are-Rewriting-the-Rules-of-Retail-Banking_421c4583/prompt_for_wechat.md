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
BCG

Executive Perspectives

## How AI-First Banks Are Rewriting the Rules of Retail Banking

Banking

June 2026

## Introduction

Retail banks are poised to unlock significant value from GenAI and Agentic AI. They are best positioned with relatively higher levels of digitization, rich data (albeit legacy bound), and higher customer adoption of GenAI applications.

AI-first retail banks are driving transformation through decisive AI investments and are capturing value at scale across business functions. However, for other banks, value remains limited to select pockets.

In this edition, we explore the impact of GenAI and Agentic AI in retail banking and the approach followed to deliver impact. We address key questions faced by bank executives:

\- Why are GenAI and Agentic AI imperatives, yet why is at-scale value elusive?

\- Which functions are realizing measurable impact?

\- What approach are AI-first banks taking across customer discovery & onboarding, service & engagement, and fulfilment in ops, credit & collections?

• How are banks building an AI-first mindset across the organization?

In this BCG Executive Perspective, we articulate a vision for transformative GenAI and Agentic AI deployment in retail banking

![](images/e4185ea8e481f650eef4c96b58c263ad9cc9938f781bddb0aa4661cde79e0c4e.jpg)

## Executive summary | Retail banks are poised to derive significant value from GenAI and Agentic AI (1/2)

## WHY

GenAI and Agentic AI in retail banking are imperatives but with current under-realized value

\- Structurally primed for GenAI and Agentic AI: Retail banks have seen higher levels of digitization and a richer data repository (albeit, within legacy systems); they are more ready to augment intelligence and create new experiences for customers

\- Value scale-up has been limited: Six key challenges addressed by AI-first retail banks- a) Moving beyond micro use cases, b) Upfront linkage of initiatives with value metrics, c) CEO involvement to drive accountability, d) Lead with products, build for re-use, e) Building GenAI fluency for change-the-bank roles, f) Design risk controls and processes from Day 1

\- Direct comparison with other retail experiences: Retail consumers compare banking experiences with AI-native experiences in other sectors, such as shopping, travel, and digital media; with AI tech advancing ever more quickly, banks need to move faster

\- Step-change in marketing maturity with higher precision in acquisition: Over $40\%$ sales uplift in new-to-bank products

\- Synthetic customer personas created using GenAI to sharpen proposition design, targeting, and channel choices

\- Improved visibility in generative search engine and driving acquisition at lower CACs

## WHAT

key skills are being adopted by AI-first retail banks (1/2)

\- Agentic interventions in media allocation optimization to reduce the number of low and non-performing channels; high-velocity funnel experimentation to apply best CRO practices to improve journey conversions

\- Customer service is changing from reactive support to insight-driven, personalized & proactive engagement

\- Human-like conversational assistance in service, reminders, and collections by agentic bots; 70%+ of human call volumes are enabled with voice bots at about one-fifth the cost of traditional assistance

\- Always-on personal RM for every customer that captures context from every interaction, proactively engages customers, and provides contextual solutions; deepen customer relationships by 20%-40% through meaningful cross-sell

\- Step change in frontline RM productivity across cross-sell, upsell, engagement, and customer service. Bankers augmented with customer-level agenda, personalized pitches, and knowledge assistance have engaged 50% of clients weekly (from \~15% of clients). 5-6x conversions observed for select products

## Executive summary | Retail banks are poised to derive significant value from GenAI and Agentic AI (2/2)

## - Operating models and workflows are redefined in fulfillment channels between agentic bots and human experts:

\- Invisible operations or zero human-operations swim lane is increasing by enabling the processing of non-standard files. Partial STP and non-STP cases are handled differently, with human experts engaged only where needed, while agentic execution and monitoring help ensure guaranteed SLAs; observed impact includes 70% lower turnaround time

## WHAT

key skills are being adopted by AI-first retail banks (2/2)

\- Credit processing is becoming faster and smarter: Bot agent-enabled underwriting engine is compressing decision cycles and follow-up communication, delivering 5x-10x faster time to quote

\- Smart anti-financial crime processes reimagined with agentic bots driving customer identification and screening to onboarding and perpetual KYC monitoring; up to 50% financial crime cost savings observed

\- Smart collections: Unstructured interaction data leveraged to understand customers' reasons for bounce, to personalize outreach strategy, and enable higher resolution; \~50% reduction in collections operating costs

\- Harness engineering to accelerate product and software delivery; 50% faster time to market (BRD to deploy)

\- Employee alter-ego or bot agents to perform role-specific activities and other enabling tasks

## - Prioritize 3-4 chosen areas of transformation that amplify the bank's strategy in market with a focus on business outcomes, instead of chasing many micro use cases

## HOW

banks should set themselves up for a successful AI-led transformation

\- For each prioritized functional reimagination, identify opportunities by focusing on nature of job instead of number of people - structurally reallocating toil/repetitive tasks and reasoning tasks to AI and augmenting humans for expertise

\- Build reusable products while transforming business function, rather than adopting a GenAI platform-first approach

\- Design structured AI risk and compliance processes from Day 1, not as an afterthought during launches

\- At early-stage maturity, GenAI requires centralized focus; GenAI products can evolve to more federated structures in the future once core capabilities stabilize

\- Invest in GenAI upskilling across the org, spanning individual productivity improvements to building function-specific capabilities

## AI-first retail banks are addressing six key challenges to scaling GenAI initiatives

![](images/3d039f615a669f69b3d533c838b1737688eca7f6ebda2224b66081ed784dabe9.jpg)

## Approaching transformation through use cases

Isolated use cases with limited value; e.g., tool for branch staff to answer product FAQs, auto-generation of call summaries in contact centers, etc.

![](images/ce45b43e4185bab42828221389f48e8ecb772f1d1430341f0ab4dbcd84670cff.jpg)

## Building solutions, looking for problems

Insufficient focus on solving a real problem vs. just showcasing the art of the possible; e.g., in-call real-time nudges for human callers, video avatars for engagement, etc.

![](images/fb546626da4e6f772c394f8cdabf687b6cecff5d158cafab04950741f2fb9ff7.jpg)

## Creating clear accountability

Without clear ownership GenAI initiatives get lost in the complex coordination between business, channel, tech, AI, compliance, risk and third parties

![](images/8821ea4ce54d6432357abfbff13fb171c46f031009207c148d82048640059134.jpg)

## Balancing product vs. platform objectives

Pressure to deliver
immediate value leads
teams to build point
solutions that do not scale
horizontally, e.g., RM
intelligence that can not
scale to D2C

![](images/74fb4606c4d902923f7f8ad8b49cdae6defa3a925db3c7cfbaf06408fbe75a89.jpg)

## Slower adoption of GenAI fluency across teams

Concentration of
knowledge in specialist
teams including Data
Science and Engineering,
with checkered
understanding across
other functions

![](images/750dc928e123cee3bedb81d78ac05d742c1112eeb2373ccf53e1dde8b12e6050.jpg)

## Solving risk as an afterthought

Speed-to-market becomes unpredictable without institutional knowledge to navigate risk and compliance decisions

## What AI-first banks are doing differently

## Fewer but deeper functional reimaginations

Focus on a few priorities aligned with overall strategic agenda; e.g., reimagined frontline sales and customer service

## Upfront linkage of initiatives with value metrics

Embed targets in AOPs with clear value measurement and roadmap

CEO involvement to drive joint accountability

Note: FAQ = Frequently Asked Question; D2C = Direct to Customer; AOP = Annual Operating Plan

Drive GenAI agenda from the top of the house to eliminate ambiguous accountability, with strong execution discipline

## Lead with products, build for reuse

Banks that exercise patience to get foundations right, unlock exponentially faster value across initiatives through reuse

## Invest in GenAI upskilling for change- the-bank roles

Invest in upskilling, so that change can be driven bottom up as well; encourage organization-wide ideation

## Build in risk controls and processes

Build risk controls and new AI governance by design from day one to avoid retrofitting. Set up an accelerated approval committee to expedite decisions on architecture, security, risk, and compliance

<table><tr><td rowspan="3">5</td><td colspan="2">Invisible Operations:</td></tr><tr><td colspan="2">• Instant and autonomous handling of nonstandard requests (no human touch or queue)• Full-context routing to right human skill; guaranteed SLAs</td></tr><tr><td>40% Higher operations efficiency</td><td>70% Lower turnaround time</td></tr><tr><td rowspan="3">6</td><td colspan="2">Smart Credit Engine:</td></tr><tr><td colspan="2">• Agentic underwriting to augment loan decision making• Iterative learning from portfolio outcomes; make policy smarter over time</td></tr><tr><td>100% Review coverage for all submissions</td><td>5x-10x Faster time to quote</td></tr><tr><td rowspan="2">7</td><td colspan="2">Smart Anti-Financial Crime: AI-led CDD/EDD, AML, screening, onboarding, and monitoring with humans as needed</td></tr><tr><td colspan="2">50% Lower financial crime costs</td></tr><tr><td rowspan="2">8</td><td colspan="2">Smart Collections: Boost share of digital collections using personalization and voice agents</td></tr><tr><td>~50% Reduction in collections operating costs</td><td>10%-20% Net charge-off reduction</td></tr></table>

# AI-first retail banks are investing in ten key skills

## Attract and Acquire

1 A. Customer Intelligence and Proposition Design: Persona agents built using real customer behavior data create a captive testing ground to validate propositions, sharpen customer targeting, and de-risk new product launches before spending even a dollar

B. Growth Marketing and Conversion:

\- AEO- and GEO-ready search: Optimized discovery across answer and generative search engines

\- Conversational Acquisition: Embedded chat in popular chat engine interfaces, e.g., ChatGPT and Claude

\- Agentic Media Optimization: Autonomous real-time media buying and targeting to maximize reach and ROI

\- Agentic CRO: Intense agent-driven customer journey funnel experimentation to boost conversions

## Serve and Engage

\- Agentic bot-led engagement, inbound service, outbound collections, and reminders (voice and chat)

\- Persuasion by agentic bots via customer-level contextual pitches and arguments

70%+ Human call volume handled by voice bot

1/5th Cost of assistance with human-like efficacy

## 3 Always-on Personal RM for Every Customer: Always-on agent that is proactive, provides contextual engagement, and is always available

+40% $^{1}$ Sales uplift in NTB products

60% Increase in activation rate for NTB customers

4 Banker Productivity: Augment bankers with contextual pitches, personalized collaterals, and process knowledge for cross-sell, upsell, and service

Wealth illustration

50% Clients engaged weekly \~20% Increase in AUM from 15% starting point

## Fulfill and Execute

<table><tr><td colspan="2">Harness Engineering</td><td>Employee Alter-Ego</td></tr><tr><td colspan="2">9 Using Harness Engineering across every stage of product and software delivery to accelerate idea to impact for business</td><td>10 Employee Alter-Ego to augment role-specific tasks, minimize toil for other enabling tasks, and provide personalized coaching</td></tr><tr><td>+50% Faster time to market (BRD to deploy)</td><td>3x Engineering throughput</td><td>Early adoption stage, at-scale impact to be realized</td></tr></table>

1. Up to three times digital sales uplift in early-maturity functions

![](images/35f8264b58f3bec4ba562d3ec1eeb6c09fc12b56bac6d28c317454ffd91d6a27.jpg)

## Brilliant Basics: Building the foundation for Agentic Implementation

Segment-centric beyond P&L

From contextual to data-driven decision-making

Close collaboration across teams $^{1}$

Test-and-learn mindset

Ownership of media channels

E2E measurement and tracking

## 1 A push toward advanced capabilities without core foundations sets banks back by \~15% in marketing maturity

![](images/2cea5237510d4cb4f280d0000abef048727135f356f966d37173ea71e1f4ccfc.jpg)

With GenAI, the time to build foundations is shrinking from about five years to under one year

![](images/d32cdc5b4e17a6629f64c1fb4ebe9e2e11f453a0b5069d2a96a1649e860acdfe.jpg)

Foundational capabilities

## GenAI Initiatives: Early efforts that banks can start from Day 1

GenAI-powered process and knowledge base

GenAI content creation

Customer digital twin and synthetic persona

AEO/GEO-Ready Search

3 To unlock early value, invest in quick-win GenAI initiatives in parallel to building brilliant basics

Customer intelligence and proposition design

Growth marketing and conversion

## Agentic Capabilities

Deploy bank app in generative search engines

Agentic media optimization

Agentic experimentation and CRO

![](images/9b9c5cd26765b0e3d72ab5dab47187dc827e4d58b3ed6fa697bddb5b784edad1.jpg)

## Layer agentic capabilities once foundations are in place to sustain advantage as market rapidly evolves

## Attract and Acquire | Five key capabilities are providing significant sales uplift

<table><tr><td>Customer digital twin and synthetic persona</td><td>Learn fast without spending real resources or taking real riskValidate messaging with simulated buyers before spending a single dollar on mediaStress-test pricing and product features against real client profiles without real-world risk</td><td rowspan="5">40%</td><td rowspan="2">Sales uplift in NTB products(up to three times digital sales uplift in early-maturity functions)</td></tr><tr><td>AEO/ GEO-Ready Search</td><td>Be found where customers are already decidingGenerative search engine-based acquisition at lower CACs; 64% of users using AI for purchasing decisions. Companies with GEO see ~7x higher AI visibility, with users spending 30%+ more time on site with lower bounce from sites</td></tr><tr><td>Agentic media optimization</td><td>Always-on Agent that makes every ad dollar work harderDaily agentic optimizer to enforce cross-channel best practices and eliminates non-converting media spend. Marketers-in-the-loop steer strategy while the bot agents handle executionDelivering up to 20% revenue uplift and 25% efficiency gain</td><td>30%</td></tr><tr><td>Agentic experimentation and CRO</td><td>Scale experimentation from a handful of tests to hundredsAgents rapidly generate and test variants at volume while humans lead the &quot;big bets&quot; that reshape core journeys; a Latin American bank using this dual approach, scaled to 5x more experiments per month and delivered 20% sales uplift</td><td>60%</td></tr><tr><td>Deploy bank app in generative search engines</td><td>Improve funnel conversions in GEO-led acquisitionsConversational assistance of bank-specific information by integrating bank app/ website with generative search engines like ChatGPT. A European bank has implemented a highly integrated banking experience with personalized answers based on in-app information</td><td>40%</td></tr></table>

## Conversational Customer Assistance | Significant value is realized from relationship deepening, outbound reminders, and inbound customer service

## A

## Relationship deepening

Revenue lift: Increase in customer-to-RM ratio, at enhanced revenue per customer

![](images/92c656bb0ec1ea1e2eebb0c932ad72765ca45ee200d22108aeb6f67a8da21892.jpg)  
Intent and
readiness identified  
B

## Role of AI-enabled agent

• AI agents reach out to customers at scale to identify interest

\- Personalized bot-led engagement to validate customer intent

\- Qualify high-intent leads and schedule RM engagement to deepen relationship

## Outbound reminders

Higher resolutions with proactive outreach and higher NPS

![](images/9d02eb42563dc97fd939aba0a65c3ccd1d736cf199d476a5b7ec36e37292bf67.jpg)

![](images/a58394f2cf74c47720363798b5ac94d819dc07abfac982791459ff91bb846201.jpg)  
Conversational agents handle follow-ups and reminders

• AI agents proactively trigger service and payment reminders to drive timely customer action

\- Bot-led conversations convince customers and enable query resolution

• Human handoff is triggered only for true exceptions and escalations

## C

## Inbound customer service

Lower operating cost: Lower need for human higher NPS

![](images/fd795c8df53bdd2d92c5c8ea8dfbf3b131d9d2113c7b626dd43129a17c0c1adf.jpg)

![](images/233a601990f3dfa510fe1e52029d3a1b8187063b0d816789201a38143a0fc27e.jpg)  
Conversational agents resolve most queries

\- Chat & voice AI agents answer all inbound calls

\- Bot agents resolve most simple, complex, and routine queries

\- Escalations and exceptions are routed to human agents

## Impact

2x-3x

Customers per field RM

8x-10x

Customers per virtual RM

Note: NPS = Net Promoter Score

1/5th

Cost to serve at human resolution efficiency

70%+

Conversation volumes handled by voice bots

Lower cost to serve

## 75%-90%

90%-95%

Lower wait time

## Conversational Customer Assistance | Investments in traditional call centers should be reconsidered, given high opportunity to reduce call volumes

![](images/19e688717e6b62886c41ac8fccdf2c129d787bdbad7322391d8f9606c241d45a.jpg)

## Additional enablers to realize value include improving agent utilization, demand forecasting, and scheduling and training

## Conversational Customer Assistance | Newer capabilities are required across the channel, experience, intelligence, and handling layers

![](images/ac58700af1ba460fc430ece15a888874e3aad87944c8548d3c649d9aa4f4b1d6.jpg)

## Traditional digital journeys

Assisted
journeys

IVR

Work apps and portals (RM, virtual RM)

DIY journeys

Field agent app

App

Website

Social media

![](images/d9176467f51dbe620a4952f34c43a72d6bf0e42052dd80f59b21

[中间内容因长度限制已省略]

8318cfb65482eba2d8f6ae932bd4a07ed7c44500305.jpg)

![](images/94652855e709e313070c226ec6da7a5d0d3cd137f9e8b3894f82c94700c1e400.jpg)

## Boost individual productivity metrics

## Capture usage data to power future function redesigns

## Few Builders

![](images/e006a892f916aa187b3d91221d0c878593457968eda3c4c3bb292f8e22afdca6.jpg)

![](images/644ce486a5f919adf8ca99cd99ef24e876a44a5efd29bad67fabc6b200bdf7bd.jpg)

![](images/67ccbe11786bf26a1d291bb22c8108544e6ee4e736a010e30e4a9f06b56a92a1.jpg)

## Higher no. of Builders

## Solve for smaller job functions via micro-utilities

![](images/aa2e2ff8cbed48726917ae76624cdbd05276b171b8bf56cea7b966970ea062ae.jpg)

## Users across select LoBs

![](images/c74ab2e41fc3041e46a1eed7d5eb2873f790fd72d15b65ed65433bc7105ddd8a.jpg)

![](images/08584880b4421118b0c8cec5653450da1405f20a22ba1010c82eccf3c61f5a14.jpg)

![](images/3a67974d3236be034d215e4728ab199de45d2711753ed96668f6d572a3445580.jpg)

## Function-specific skilling on refined roles post AI automation and augmentation

## Start with a centralized tech COE before moving to a more federated structure for function-specific transformations

![](images/d2663c70c3916fae2b13d0c311b96d9a28990b28e9bdf35b9e581676f74e3652.jpg)

## Owns HOW to deliver

• Makes build vs. buy decisions

\- Owns reusable foundational capabilities

\- Owns the model and vendor strategy

\- Ensures platform and model performance

![](images/4a4b4f3a5eea51f0a92476a01ebfbd0c77790e50491090153d09b5ca8af11f5d.jpg)

## Platform delivery

![](images/29e180dcaf8e78a0062cfdf347a2dc2ae7ac3bf3575539149cfb2d0a5922ea96.jpg)

Value delivery

Business and product Function 1

Business and product Function 2

Business and product Function 3

![](images/859c02d9978116f5f54fb475d0e299a8bcaa8c77d6fb257183455976fde48069.jpg)

## Owns WHAT to deliver

\- Defines priorities

\- Redesigns business function

\- Drives on-ground business value post implementation

Dedicated SPOCs
innovate and deliver
value

## At all points in time, both the GenAI platform and business function need to co-own the business impact

At early GenAI-maturity levels, centralizing GenAI tech is a good starting point:

\- Builds reusable GenAI capabilities in parallel, accelerating functional scale and overall maturity

![](images/8b5d3bfa14d7265b13329cc9158bfa3c3e185d5a581369508aaa50484c13763d.jpg)

\- Establishes enterprise-grade standards across models, security, and risk to enable safe scaling

• Concentrates scarce GenAI talent to drive depth, quality, and repeatable excellence

As GenAI maturity increases, the product tech must progressively evolve toward a more federated structure, with stronger functional domain autonomy

![](images/280eef5225fb7a747946aec8aee187dd975b35c99bcd17c83508cb19dab4464a.jpg)

## Set up a GenAI COE for three key purposes

## Augment priority business functions with GenAI to deliver value

## Build reusable capabilities to accelerate enterprise-wide scale

## Translate frontier AI innovations into relevant business solutions

## GenAI-skilled product owners

\- Deep GenAI literacy required on the art of the possible to redesign business functions

• Product owners need to drive value on-ground

## Data-Tech co-ownership

\- CAIO owns AI intelligence and model performance, e.g., model choices, agentic orchestration, prompt optimization

\- CTO owns platform engineering and performance, e.g., integrations layer/ tooling, product development

Dedicated
innovation
hub

• Proactively track frontier AI advances and operationalize them where they create business value

## BCG experts Key contacts for AI-First Retail Banks

![](images/df71d5d45db97acaa75c8036356ea6aeb8d45de073cb8a810d054f98987e4376.jpg)

## Key BCG experts for AI in Financial Institutions

![](images/4587f5a065a941f439d76249f7f2047c0ca736b5691a415cc7c2d645ecfa264c.jpg)

## Bharat Poddar

MD & Sr. Partner
Retail Banking
Global Lead
New York

![](images/5eb2241ef475b9779bae1092a138bbaf8853050b407774317c928fcd27996b44.jpg)

## Aparna Kapoor

MD & Partner
AI in Wealth
Singapore

![](images/340f74c1b646c717f17c69ce15438ffa06b6cd7346092bff8e9b8a5763f9b875.jpg)

## Lorenzo Fantini

MD & Sr. Partner
Al in Fin Crime
Milan

![](images/c639096ef47481e3c5201c5baa2973fd547ff61d00bbc7fdeb10c2e57b8e164b.jpg)

## Peshotan Kapadia

MD & Partner
Conversational Banking
Mumbai

## Author Team

![](images/41c781405b48d6056548be821a29355986ad13fb3d7729f3ee28879c1a1d3227.jpg)

Nipun Kalra
Kalra.Nipun@bcg.com

![](images/ad6b335bfa299825231d5acee5e85f2356f5d0bd0bd916149c72834c22122599.jpg)

![](images/00d3419a78e42c40a08aab3f676769459c2aa4f84aa239bdc2d0f84ba06d643b.jpg)

![](images/45f9768adcd6bc8180d1cb6fe7a36e1c509158c2368a37e79b78aa957f711ef0.jpg)

![](images/447a25aee75accc012435d1f45ef8c0b4852304b5e7ba3239171409b1769babd.jpg)

## Nipun Kalra

MD & Sr. Partner,
AI @ FI Global Lead-
Retail Banking
Mumbai

![](images/376d79c779b6e327a64e1225c89932a1fab38cc831cd173a820aa8a5003eabe2.jpg)

## Anne Kleppe

MD & Partner
AI in Compliance
Berlin

## Lukas Haider

MD & Sr. Partner
AI in Operations
Vienna

## Semih Durmus

MD & Partner
AI in Credit
Minneapolis

![](images/62b2c93a997b9187f36190bc4b17ecd27169e25b2f5a7e3a4440fb5206259824.jpg)

![](images/ceb720a00a2a8a6c91fa3a51f366ef53f993b95d8d4a5bb479a6581dfdb32b27.jpg)

![](images/c7015d26fd003597868e8df47ff75b327f380620c999fde12a4cb7eb32f5056a.jpg)

![](images/6c3011dd96f6af228493471c20a57043ae5b25c3a67abb8ba5280d806ec3bd53.jpg)

## Stiene Riemer

MD & Partner
AI @ FI Global Lead-
Wholesale Banking
Munich

## Javier Perez Moino

MD & Partner
AI in Customer Acquisition
Madrid

## Matthew Barton

MD & Partner
AI in Collections
Philadelphia

## Yogesh Mishra

MD & Sr. Partner
AI in Tech
Dallas

## BOG
"""
