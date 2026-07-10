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
BCG

Executive Perspectives

## Applied AI at its most impactful with Agentic Enterprise Operations

Agentic Enterprise Operations

June 2026

## Introduction

Agentic AI is redefining how enterprises operate, and represents Applied AI at its most transformative. Many organizations have captured their first productivity gains from AI, deploying copilots, bots, and an automation layer, yet few companies have realized impact at scale. As with many general-purpose technologies, unlocking the full value requires structural reinvention of end-to-end (E2E) processes and their governance. AI-native pioneers demonstrate that completely different outcomes are possible when enterprise operations built or rebuilt for AI autonomy from the ground up.

Building agentic enterprise operations requires moving beyond individual AI use cases to AI-enabled processes E2E. To succeed, organizations need to shift their focus from tasks to outcomes, from improving individual efficiency by embedding AI in human-led workflows to redesigning entire processes for multistep AI autonomy. Organizations also need to rethink how decisions are governed and how risk and accountability are structured while building the underlying AI, data, and orchestration capabilities required to enable reliable multistep AI autonomy at scale.

This journey raises a new set of leadership questions that we address in this executive perspective:

• How will agentic enterprise operations disrupt and redefine workflows and business models?

• What will be needed to enable multistep AI autonomy at scale (e.g., process redesign)?

\- Which transformation path best fits the organization’s starting point and ambition?

While agentic AI is still maturing, its exponential trajectory leaves little room for delay: Now is the time to build the operational and technical foundations for near-term value realization and scale.

This document is a guide for CEOs, C-suite executives, and Operations leaders to rethink enterprise operations end-to-end in the light of agentic AI for true value unlock.

In this Executive Perspective, we explore how agentic AI reveals full value once redesigning enterprise operations E2E for AI autonomy and application at scale

![](images/1e55032f92648e686676d27ba98e5f39f4508f5ed01a84686a4674b8f815dcbe.jpg)

![](images/682d60a0a0dc602c1fd1b7389daee6a35db012a2414079e66743d9b8ff35ea60.jpg)

## Summary | Rethinking value creation with agentic enterprise operations

## Agentic enterprise operations rewrite the AI paradigm

![](images/3572c46e6c1c140533ed60aa3f31ea3798e129741f378eaec89c966bf9e300ad.jpg)

• AI has delivered measurable productivity gains, yet 60% of enterprises have not structurally unlocked value at scale

\- Most transformations left the operating system of work untouched: Limited E2E redesign, unclear process ownership, and tech constraints continue to cap impact, while AI-native companies operate at radically different FTE-to-revenue ratios owing to multistep autonomous agents embedded E2E

\- Building agentic enterprise operations – redesigning E2E processes for multistep autonomy that are managed by outcomes, not tasks – is the step change; first transformations are already targeting material impact (e.g., up to 80% straight-through processing, 60% cost-out, and 30% CLTV uplift)

## Focus shifts from optimizing tasks to designing autonomy

\- Traditional process optimization improved task efficiency in human-led systems; with agentic execution, capacity stops being scarce and the constraints shift toward control, integration, and reliability

\- Process steering evolves toward a unified process owner, accountable for E2E outcomes with system-embedded decision rights and coordination

\- Near-instant, capacity-elastic execution unlocks new value propositions and business models (e.g., real-time decisions or always-on operations)

1. Focus on outcomes: Review your processes focusing on the outcomes before optimizing your as-is operations

## Five elements to successfully build your agentic enterprise operations

![](images/2730a6b13d3913065df591bc2530e6cb36d44e7c8c128c1246d6d1fd51917ddd.jpg)

2. Build an "agentic process transformation factory": Centralize E2E process transformation and standardize embedding of AI agents

3. Make tech choices a C-level priority: Elevate ecosystem orchestration and build the AI layer for agentic scale

4. Place a platform bet: Pick one agentic platform and get started; portability is expected to increase as agentic AI matures

5. Start the journey early and evolve governance along the way: Pick 1 or 2 high-value domains while addressing the new challenges resulting from change

\- Since agentic AI is still maturing and key questions and tradeoffs remain, there is no single successful blueprint; choices such as a greenfield or brownfield transformation, a governance or ownership model, and autonomy boundaries will determine each organization’s transformation path

## D

## Different transformation paths can succeed

\- Five bets can anchor the path forward: Building muscle now is crucial, platforms will converge, integration efforts will become easier, an outcome-first redesign will unlock true value, and tailored pathways will be required

\- To get started, first sensible steps are assessing agentic maturity and value potential, defining transformation principles, and prioritizing process redesign domain; integrated into a holistic approach of strategic ambition, program orchestration, agentic operations design and agentic foundation

Note: FTE = full-time equivalent; CLTV = customer lifetime value.
Source: BCG research.

## Chapter A

## Agentic Enterprise Operations Rewrite the AI Paradigm

## AI has boosted task efficiency, yet 60% of companies still miss material value mainly due to unchanged work systems and persistent tech constraints

60% companies are not generating material value from previous AI waves focused on task efficiency $^{1}$

Task-focused AI use cases generated early enthusiasm (e.g., 10% to 20% productivity increases with copilots and isolated bots)

First AI waves left the operating system of work untouched
Limited structural gains given low E2E redesign and change management

Use case impact was limited by practical tech challenges (e.g., data fragmentation and quality, security issues, compliance risks)

## True value can be realized by embedding agents E2E in enterprise operations

Structural reinvention and E2E redesign of processes is needed to unlock full impact

First companies are redesigning processes and workflows for E2E agentic execution

AI-first pioneers achieve step-change impact (e.g., 3x productivity improvement, 80% cycle time reduction)

![](images/f19b3216528ebbdcd278e0b1373486e0b59f302367df379a9b80945a0b05fefa.jpg)

## At the same time, AI-native companies operate at structurally lower FTE-to-revenue ratios, enabled by autonomous agents embedded E2E

## Differentiators of AI-native companies

![](images/36b8d6ae9ee1d471564c5108285cddd88bc099e37fc38055a8bd9cabb6189e56.jpg)  
Operations are built for AI autonomy and scale by design, not superior LLMs  
Time to scale from \$1M to \$100M ARR (years)

![](images/a533187d415ddc3e66c52c34aa9c164bd55a02e46dfa5c03a456cbdefe0ea037.jpg)

Processes embed AI agents E2E who are led by outcomes

![](images/4ac4d782eb7bb3519e86befa3e7311fdd6d73cf164bafc8e4c81d2c9e6cd356d.jpg)

Agent-driven execution
(control flow) and
multiagent orchestration

Deep dive follows

Note: ARR = annual recurring revenue;
LLM = large language model.
Sources: BCG-conducted expert interviews; BCG analysis.

![](images/58fe5f28704d321861adbd38924aaec668fccd2f4b7ecf5eb229ecf3a3fa56c8.jpg)

Other notable companies

Together.ai | Sales force | Deel | Drop box | Okta | Servicenow

## ARR and FTEs

Lovable \$200M ARR

120 FTEs, 2025

Up to \$1M to \$5M ARR per employee

## Agentic enterprise operations, with multiagent systems, reinvent the entire operating system of work and unlock completely different AI value creation

![](images/40b04beb98a14eaf86bf60a5427752e081f6eea61505f3ac2e8c6189ce55c2db.jpg)

## Agentic enterprise Key characteristics

Redefined, amplified and outcome-led processes

## E2E processes run by reusable AI agents

## Decisions AI-driven by default across execution and control flow

## Multi-agent coordination across functions & systems

## The AI gap is massive – agent-native organizations largely run without humans, while most enterprises have <3% of the work run by agents

## What's happening now

![](images/d7abb7556aefa3fc9e1a67b58aaf5ca5c8b16870886c1ea12aebc73b2cbc8bd1.jpg)

## StrongDM Dark Factory

Three engineers, zero human code review. Shipping production security software with AI agents

![](images/e8031e9f2774351c21a89858fd98bb35c83ecf4e266bee6196fe02cb2a54b3d0.jpg)

## Goldman Sachs and Devin

\~12,000 developers from Goldman Sachs working alongside Cognition's Devin AI. Firm plans for thousands of agent instances.

![](images/9a2a346847475bb2d3a3ab2aa52f8f2338b33ad960906ae9c21ac41d38268b50.jpg)

## Anthropic internal

90% of Claude Code written by Claude Code itself. 4% of all GitHub commits written by Claude Code.

![](images/7162e85163b6e99e920b8a5828788bf4fb440fc488ced6615bcdc140685911ed.jpg)

## Zero Human Company

First autonomous company; the AI CEO, named Grok, and more than 30 agents handle all operations

![](images/b79a0c7b30dc3b4ca545dbcafa82a5c9fbf90e53f6f227f818f8931fd69a6c4b.jpg)

## Y Combinator Winter 2025 Startups

25% of startups have 95% AI-generated codebases; agent-native from day one

## What we typically see

![](images/851a5ddcdedc917d7de64820eee0216119885968a035c7704c7b4bfe1681f341.jpg)

![](images/b476128421b98c1e54c6fc93af29a7dafb355dd918a592755e5a3d34b40c7755.jpg)

Three pilots
approved

One copilot
deployed

\~2%

of work run by
autonomous
agents

![](images/b12206cbc4b32030fa19ae11262c60f239e0e00208ab45dc424f8f9bd616d8d1.jpg)

![](images/ef0c17a3049197695f636d02ade123a1f62f327e1b3ad64b523869915733b4bf.jpg)

Al roadmap for 2028

Governance
unclear

While competitors run 90%+ autonomous

## There are successful AI transformations - key ambitions we see on agentic

## Success stories of previous AI transformations

Reckitt

Foxconn

BMW

Alphabet

Capita

DKB

Merck

Amazon

Rio Tinto

DHL

Signal Iduna

Salesforce

\+ many more...

## Ambitions and impact we see at our clients for agentic transformations

![](images/e486ca0be4e8a6895169e401d97e62490db4888b762f7b4292305190e543ca1e.jpg)

![](images/2a5293689bca7f28386578cf5351caecb6d4622ba2689b32dde2772e3a1aabe5.jpg)

![](images/cf2be51601f72798dcabded1934526009e9d701b77d4a8da163cdb5d4673608a.jpg)

![](images/8b9e4962beb0cb0d697a9904b4c44f5b076f37cf2136c9e428cfb384935e9872.jpg)

Up to

80%

Straight-through processing

More than

60%

Cost reduction
long-term

Up to

20%

Short-term savings unlocked

Up to

30%

CLTV
improvement

## A global bank implemented an OpsAI agent in its retail lending processes and realized significant benefits in production

## Context

A global bank was experiencing rapid growth accompanied by a significant increase in operating costs and complexity. This was because of the limited scalability of its operations caused by heavily manual retail-lending processes:

\- Human agents manually screened, categorized, extracted, transferred, validated, and corrected information.

\- These tasks were repetitive, had limited complexity, and added minimal business value, but they consumed significant resources (FTEs).

The bank's ambition was to upscale operational excellence to cap operating costs while further pursuing an ambitious growth trajectory.

Note: OCR = optical character recognition.
Source: BCG experience.

## BCG's approach

To help the bank achieve its ambition, BCG recommended setting up a scalable operation and E2E processes. The bank deployed BCG's OpsAI agent as part of a holistic, zero-based process transformation. The OpsAI agent automates E2E retail-lending processes in a reliable fashion by replicating human processing. Combining LLMs, OCR and data synchronization, file splitting, and validation, the OpsAI agent leverages five key capabilities to automate unstructured data handling.

5 capabilities of the OpsAI Agent for significant productivity gains:

![](images/7e3bc03265ddc0761f26f8253e5a1fb7300993e3c5ae1f4e1172ae7d7e2ff6f6.jpg)

Document recognition and classification, incl. quality checks

![](images/175820ca39f846baff70ca8d1dce7db24acdc725cfe2c76c23225dab85d02453.jpg)

File splitting and data synchronization across systems

![](images/fa1fef5f558d67294cf3ea37dc9b9c9158b7ed35927e3bd945510005a94eb241.jpg)

Autonomous data extraction, interpretation, and correction

![](images/59dbf062faa3d13e5cf1cdd2633236d1fde3f0a5ef6813aced0997d1ecec86a9.jpg)

![](images/c952a6c4330382add3d1e8f7f005ea873ca5254bdd899b9ec82b3a8dad4efc07.jpg)

Integrated consistency, fraud, and plausibility checks

Signature recognition and contract validation

![](images/8d52b658d7392018c1ddbc6df2c79a930fa38e7a689a3d2d48f2357dcf27f6e9.jpg)

>90%

![](images/d895b11204f02f7aff9caeaeaf75713805d86d36f441e87a9e59b41598e7f097.jpg)

Automation rate of E2E processing of consumer loans

>70%

Automation rate of E2E processing of mortgage loans

>50%

![](images/88508e2dcc5d5c39031ccf05d1a8bd79c62b67ad38a8a2817ac796b4d73a0829.jpg)

Productivity gains
across retail lending
processes

![](images/36c57e88383da087d74159750935d8aaf0433eb2f2ee6cd041d865935ea9ee76.jpg)

## A global technology company redesigned E2E processes across support functions, realizing significant cost reductions

## Context

A global tech company started a transformation in the context of a structural cost gap and a high-complexity operating and technology footprint:

• Support-function expense to revenue in 3rd quartile

\- \~5% incremental annual targets delivered marginal impact

\- Process and system complexity from M&A and fragmented ERP and application landscape (incl. over 5,000 IT back-office apps)

\- Stranded cost following major portfolio moves (e.g., spin-offs)

The ambition was to deliver a step change in productivity and cost transformation to move support functions to first-quartile expense to revenue, as well as to increase free cash flow to fund strategic pivot to hybrid cloud and AI to fuel growth

## BCG's approach

As part of the broader transformation roadmap, the tech company followed a three-step approach to drive productivity and ensure value realization across all prioritized processes

![](images/335541f5a2fc3716a859c9740d06deebc30c136f70370233ecc7506c2fa02f14.jpg)

## Eliminate

Detailed, critical evaluation of every process (no protected processes or functions) to identify opportunities to eliminate superfluous processes that did not add value

## 2 Simplify

Identification of opportunities to remove complexity, minimize process steps, and handoffs between teams and systems; Put focus on designing simple workflows to reduce touch and cycle time

## 3 Agentification

Infusion of agentic AI throughout the redesigned processes to automate activities in areas with more subjectivity, enable self-service, and leverage unstructured data in analysis (e.g., summarization of tax documents with an inconsistent format)

![](images/9b1015e11c99084106743a7093d099d46654c97074560fee7f867708bb8646be.jpg)

Savings delivered in the first 18 months

![](images/e6e45110c6e83782a71198d9dd0e2d4316f7bf6a1cb1720d6a314f7b93832e44.jpg)

## Annual savings delivered

![](images/5f2aafe225ec4c062c5697c23868e39a866aedcfe91c0e2cdd4adf8505f55985.jpg)

## Activities automated

## Chapter B

## Focus Shifts From Optimizing Tasks to Designing Autonomy

## Agentic AI is radically changing the way processes are designed and governed by shifting focus from optimizing flow to business outcomes

## Traditional process optimization

![](images/1aa7a595a59a31e344f36c713aeff37f50ee9cc96ce4e92288cb9ac5c98e2eec.jpg)

Optimization for availability and cost of human capacity

![](images/ce1786889687491a472e9f098717d59fac02eaefc8263d8f8058dd76d08432dd.jpg)

## Tedious standardization of process

variants to generate automation at scale

![](images/a557710676cde4be571da6d542d2a78bfde14bf1d800bbe8960092ffece74944.jpg)

Reduction of unhappy-path deviations with predefined breakouts

New opportunities with agentic enterprise ops

Abundant, scalable execution capacity with completely revised economics

Decoupling of bespoke processes from standard business outcomes through agentic flexibility

Process deviation as part of core design of agentic systems

## Agentic enterprise operations shift process steering from multiple owners to a single agentic process owner

## Traditional, distributed process ownership up to wave 3 Wave 3: AI agents

![](images/97643524a201721b9929bed16237d128d97dbcf87f8c5137e01133e9582148d8.jpg)  
Business process owners leading E2E process oversight and continues improvement  
Technical Owners leading individual use cases (e.g., bots and AI tools)  
Singular process ownership in wave 4
Wave 4: Agentic enterprise

\- Multiple partial owners, each owning separately functional P&L, business process, and technical dimension

\- As ownership is distributed across different aspects of the process, a significant coordination effort is needed to steer and optimize for outcomes with often diverging KPIs and targets - Single steering logic, with agentic process owner having E2E accountability for the redesigned process

![](images/6a2ca91cf8bd150c5366bfca060466b7f255d61b5da69c2546225ab859a18bcc.jpg)  
Agentic process owner, accountable E2E for all steering dimensions  
Enabling teams such as the responsible AI or data infrastructure team

\- Agentic process owner can become central supervisor for steering AI-executed process flows by outcomes, with respective accountability and decision rights

Shifting processes
to agentic AI E2E
allows an evolution
of business models
and a GTM approach

![](images/8e574acab3b56f347c35cb6d772e3ed1d636346742a4e2fff99932556aa26574.jpg)

![](images/c757ada933f569688ae02a82cea7345fbf885dd3acf3d8dea6e5fad70aa9aaf4.jpg)

Outcome-based offerings are enabled by full process-control and highly decreased incremental cost (e.g., for optimization)

Truly tailored offerings and services are delivered at scale due to a low marginal cost of changes, regardless of complexity

![](images/a880934da86ff7406388a1f980c6c1db80eaa4413a2b769958e6a43d2cc89257.jpg)

Monetization shifts from static offerings to dynamic value-capture models as processes continuously optimize

## Chapter C

## Five Elements to Successfully Build Your Agentic Enterprise Operations

![](images/77fdf7850c957b56db97c7c698779c8d4ca2e32230a937cdab510d

[中间内容因长度限制已省略]

## FULL VS. PARTIAL SHIFT TO AGENTIC AI

\- The key decision is whether to partially phase toward full autonomy or commit to an all-in redesign from the start

\- Partially shifting to agentic AI doesn’t unlock the full value, but it allows less disruption, higher speed, and lower investment, while preserving human-agent models where judgment remains critical

\- Fully shifting to agentic AI E2E unlocks the full structural value by redesigning entire processes for autonomous execution

## AGENTIC FOUNDATION

• Strategic design decisions should align with foundational readiness across technology, data, processes, governance, and talent

\- For a brownfield approach, a maturity assessment helps to prioritize a foundational buildup, while a greenfield approach demands a deliberate focus on tech and people strategy; the speed and scope of a transformation remain separate design choices

## An agentic enterprise transformation requires a holistic approach including Strategic Clarity and Applied AI – beginning with these first steps

## Strategic ambition

Define the value ambition, transformation principles, and governance philosophy

## Program orchestration

Set up transformation governance, roadmap sequencing, value assurance, and change management

## Agentic operations design

Redesign E2E processes (starting with target outcomes), deploy agentic workflows, and establish continuous monitoring and new agentic governance

## Agentic foundation

Build the enabling AI capabilities across tech, data, processes, talent, and governance

## First steps to get started

![](images/47432d58fc33f93414f8729dedf5835eaa91b745f00ebebfc205503ae694d3f1.jpg)

Assess agentic maturity and value potential across key E2E processes

![](images/f87e3e2acbdc70289797959d9130f1fe62acf82d72853961e0409896f4c7d1ba.jpg)

Define transformation principles (e.g., brownfield or greenfield approach)

![](images/416ff1046ccbe00068339d1e34c8d16b00b20287c366e9ebe143d8e799110d3b.jpg)

Select 1 or 2 priority domains for process prioritization, redesign and the target state definition

## BCG experts | Key contacts for Agentic Enterprise Operations

## Global Leadership

![](images/c1703fea1c59da4732e1b86245f07b30341f54c8a98c134010001408747991bc.jpg)  
Marcus
Wittig

![](images/a349179164806ab91a0a3e743486705e846d705eb478670bb79fdcc6ae99b6ad.jpg)  
Alfonso
Abella

![](images/44a6ec672d0827ffa864f9cc9700d7254f469d42bff26fe4d4d12cf75f4cd3bb.jpg)  
Nicolas de Bellefonds

## Europe, Middle East, and South America

![](images/5afbb8ff8a59e842d7a25bb7ae9cd999c3ec9036db01a0e5bf84c4a1ab17a84b.jpg)  
Hrvoje Jenkač

![](images/d69446d06462c6f5b88c5b4de5ca8fa6813cc127a3e9df012837cb847a316172.jpg)  
Sebastian
Schmöger

![](images/7974af57947523d418f383c247e8c5397876d118b5a9fd28cb40934900680791.jpg)  
Alexander
Noßmann

![](images/9f2e47b9b83328830aa1325512a72a3ca8e20206884279dea31f67eba8b840f9.jpg)  
Tamsin
Hirson

![](images/c89b3f732ecd97f9091adb3762b1bc45393686cfd3040f1cb1b37e34f551a85d.jpg)  
Michael Engels

![](images/2cef17eb8871ec874b8bfb537379d9d3a44b466d239965690c9c3d88dc6b9082.jpg)  
Ignacio
Hafner

![](images/f61fcb9df2932b215275283d1080c4c51c0a17b073a71e0dec87732b360a38fd.jpg)  
Lukas
Haider

![](images/df46a432f2d80ea2f8961a9471d3c1566a255b91541e116cd8d0069309b75850.jpg)

![](images/9255becd63b3edfe8db1210a0bbc9d70bdc2f21f661c3d77dd04676084814b30.jpg)  
Juan Martin
Maglione  
Salvatore Cali  
Christoph Schmitt

![](images/33cd36336be6bbf316afa8ce42ffc8cf606d4612f8a28cf3d79b9b8642a48c87.jpg)

![](images/c792496c5d668dddce418cb9f8c65b52fd4f80d0d8eaf787acb6f98b549895d1.jpg)  
Yann
Letourneux

![](images/0927a03ca557a4d79325c89b5e7cabe317f1f6769630c95e44e0b10e41bb3f92.jpg)  
Melih
Yener

![](images/36afc68307f24650fcbaccae2fc407474a033576c09094108df0a28069100b0f.jpg)  
Guillem
Borrell

![](images/e7312a6e0f82114f86fad31643910f91395e70c22915553e20e5346e90fa3544.jpg)  
Robin
Anders

![](images/a60d45a2d11ec9dc18d22ffeef204c96f45e9cb273e5333870f4ea1b461ab4b7.jpg)  
Carolin
Bimmermann

![](images/b9fa826880768e7e7e1f30fb0d871d76493b15c297957dc45d4a43844e5a616f.jpg)  
Olivier
Bouffault

![](images/1db2b4999ef3983ac90adb435bce87e5a7a0b6722301b4af43b10f6cee4d96ef.jpg)  
Matthew Marchingo

## North America

![](images/c3e02a356fe5f3773335a9aec07e7dd8f9cba6ea52a9e5bc112c6686e13c7f77.jpg)  
Simon
Bamberger  
Samir
Kapur

![](images/10d7df73de066efe8a0fa3a2c8a975ea5419443d35d13b106ce7fe3e2a5f6288.jpg)  
Luke
Purcell

![](images/f7c3c2719d6062e95a01be60761ecc985edc9c65fd285152d0458dc772f05778.jpg)  
Haytham
Yassine

![](images/514c8d46a851cdd2293e8b214a2ef6cbb89a4978e7a96c315008b67a7cc542b0.jpg)

![](images/eb3d30bafdee73723ad9ee91859c3fb70dfa460f788e9ced4a9215ad58cf08f1.jpg)  
Amit Kumar

![](images/25ccee314a257f5e8346b8320167fef0be1a7c26b654117f9b14e9b29090e9da.jpg)  
Shervin
Khodabandeh

![](images/4fe9231cd5deb9dff834cf3411d413171b4b77eaea09aafac8577fbd8b1f8d40.jpg)  
Angad
Grewal

![](images/dbf1d4074ab7342cdbd37f94ad149d53349bd20415a5378fd78928a7bb5fd734.jpg)  
Lingqiao Li

![](images/ebee2cdfce9282f55354d4815923cfa9863ac4c64e9a6cdf60115ef1fdf6d7d1.jpg)  
Stephen Robnett

![](images/cc568d1ce0d3377e2da778123dc1b391ab782506bd06a7a906d1fac65b29a6be.jpg)  
Uche
Monu

![](images/2e4692813aaaeeddaef0cdcd6f0b8307c17948b2269187a038ad51828b8e4765.jpg)  
Alexander
Duerloo

## Asia-Pacific

![](images/830fb7ae484a526ca0361f52f74bac3600d66a4345a6503e81333e3dd7feb665.jpg)  
Johannes
Goltsche

![](images/1301e286d8675335b6e365423524836880b20067c372ce28217442401f409d6f.jpg)  
Manish
Chandra

![](images/62165f19bfac17ebc49f6aa907621527fd7489ad1e3f7aea7f169a967f9275ff.jpg)  
Tarandeep
Singh

![](images/ac650aaa49662f5259e3bf62a346324dd69c667b6670d92b0c9a61f90c753810.jpg)

## BOG
"""
