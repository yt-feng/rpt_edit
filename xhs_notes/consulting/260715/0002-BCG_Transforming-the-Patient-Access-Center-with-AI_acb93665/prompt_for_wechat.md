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
![](images/f7494ca527f155ec6dd75d125c978849a7082afabeb5c0ec1b630a5767f17968.jpg)

HEALTH CARE PAYERS, PROVIDERS, SYSTEMS & SERVICES

# Transforming the Patient Access Center with AI

By Natasha Taylor, Matthew Huddle, MD, Luke Purcell, Ryan Shain, Scott Wilder, Kevin Fleming, and Michael Bernstein

ARTICLE JULY 14, 2026

The access center is both the front door and the beating heart of a patient-centric health system. AI stands to transform how patient access centers function, but not in the way many executives imagine.

Consumers call, chat, and text with access center agents to schedule appointments; manage referrals; navigate authorization, billing, and insurance topics; and seek answers to a multitude of questions. Despite this heavy use, a substantial share of patient demands slips away at the

access channel. Thousands of calls go unanswered or are abandoned due to long wait times, failed transfers, and limited after-hours coverage. Up to 40% of scheduling-related interactions go unresolved on first contact. Missed annual visits and vaccines are not systematically and proactively addressed, and specialty referrals are not aggressively tracked and converted.

AI can perform many of these basic tasks and augment the work of human agents for more complex issues. Yet when system leaders consider deploying AI in access centers, they view it merely as a way to reduce costs and increase efficiency. This perspective overlooks a significant opportunity to use AI to reshape the access function from end to end—shifting it from a cost center to a revenue engine.

Many of our clients are deploying AI to automate lower-complexity processes while reorienting hardworking human staff to high-value, high-impact consumer engagement. They understand that the access center of the future should be an AI-enabled platform to drive growth, manage consumer relationships, enable value-based care, and generate organizational intelligence. They also see the access center as a “proof case” for their broader enterprise AI ambitions.

# Opportunities to Transform the Access Center

We see three key opportunities for systems to pursue when transforming access through AI. Automate routine scheduling and referral workflows. Augment human agents during complex interactions. Amplify access-related revenue generation strategies. (See Exhibit 1.) Systems that pursue these three complementary strategies in parallel will see the greatest return on their AI investment through improved consumer experience; easier access; improved navigation, quality, and outcomes; and financial upside. Let’s look closely at each of these actions.

# Three Key Opportunities to Transform Access Centers with Agentic AI

![](images/3bb7a782ec6a9b606b4ddfaa2825f3788a96cb49536f949366c542ad1edb6277.jpg)

## Automate rote and routine scheduling processes

AI fully steers calls and chats from reaching a human agent, including routing to self-service channels (e.g., MyChart scheduling)

Example tasks:
Appointment scheduling,
confirmation, modification, and
cancellation

Status requests for referrals, prior authorizations, and waitlists

Pre-appointment preparation, including arrival time and dietary restrictions

General inquiries and wayfinding (hours, location, parking, and visiting hours)

![](images/724d15d1d7c05319266f6d39e29b5afed0e1140c0941274cb77df2a620a5007e.jpg)

## Augment human agents during complex interactions

AI enables a human agent before, during, and after a call to resolve a patient's issue in a complete and timely manner

Example tasks: Call intent identification and patient identity verification

Patient information gathering (e.g., relevant health and appointment history)

Call guidance, next-best-action recommendation, and agent assist

Post-call support, including QA and individual-level training and upskilling

![](images/c71fc22642c77c2a2e00ff98f92a8b56995d91c02e0f254deb68fcd53de4f71c.jpg)

## Amplify access-related revenue generation

AI extracts signals from large, unstructured datasets to create an intelligence layer and generate “segment of one” patient insights

Example tasks: Proactive outreach on common care gaps (e.g., overdue screenings and annual visits)

Referral management to stop patient leakage between front-door and specialty services

Automated follow-ups for dropped or unresolved calls to prevent lost demand

Business intelligence generation (e.g., emergent demand drivers and supply mismatches)

Source: BCG analysis.

# Automate and fully contain end-to-end access workflows.

Across health systems, the interactions that consistently demonstrate the highest potential for end-to-end automation are appointment information and confirmation, scheduling and rescheduling, and cancellation, as well as requests for referral and authorization status and general wayfinding. These intents are high frequency, heavily scripted, have clear resolution pathways, require no clinical judgment—and they typically represent more than half of total inbound volume at large health systems. These are good targets for containment, in which AI manages the interactions independently, without human involvement.

No single vendor currently provides a full, end-to-end solution virtual agent, and no single “best” approach will work for every health system: each has distinct benefits and limitations. (See Exhibit 2.) Options include vendor solutions such as Hyro, Sierra, Decagon, and Avaamo—or building a custom product with in-house tech talent.

Buying vs. Building an AI-enabled Virtual Agent  
![](images/4c71e40ebed9b8f94b9c465959983779ba1b58fcc9f6684f97a205a38b154f4e.jpg)

Selecting the right implementation approach for a virtual agent is one of the most consequential decisions a health system will make. Leaders must weigh several factors, including speed to value, long-term flexibility, ability to integrate with custom business logic, total cost of ownership, and any potential trade-offs. This analysis requires a granular understanding of access center interactions and consumer intents, clarity on the enterprise's overall level of AI ambition and long-term strategic roadmap, and detailed modeling of financial implications, including potentially uncertain variables like future token cost. The right solution depends on a health system's priorities, existing technology infrastructure, the complexity of its scheduling business logic, its tolerance for vendor dependency, and its internal product and engineering depth.

## Augment and enable human agent efficiency and effectiveness.

While many patient access interactions can be automated, some will need escalation to a professional and well-trained human agent. Whether due to scheduling complexity, coordination of referrals and authorizations, sensitive topics, or consumer preference, about 40% to 50% of calls will still require human interaction in the near-term. For these calls, health systems should pursue agent-assist capabilities that augment the legacy tools that human agents have at their fingertips. Deploying AI tools that make every agent better, smarter, and faster at their jobs can drive meaningful enterprise value while maximizing job satisfaction for human agents.

Among our clients, up to 60% of human agent time is currently spent on tasks that could be augmented by AI. Agent-assist tools can drive reductions in average handle time (AHT) by 30% to 40% and dramatically improve patient experience by freeing the agent to focus on empathic

listening and creative problem solving rather than basic knowledge retrieval. Agent-assist tools deliver value across all steps of a consumer interaction, including:

\- Intent detection and identity verification. With or without a standalone virtual agent, a “narrow” agent-assist tool can confirm a patient’s reason for calling and conduct identity verification, handing off relevant context to the human agent.

\- Patient information gathering. Patient history, prior call reasons, open care gaps, and suggested next best actions are identified and displayed by the AI tool before the agent speaks a word, eliminating the need for manual electronic health record (EHR) lookup.

\- Call guidance and next best action. As the conversation unfolds, AI guidance surfaces relevant policy information, scheduling availability, and next-best-action recommendations, providing agents with real-time prompts to address queries instantly rather than placing callers on hold.

\- Handoff. When a call must be transferred, AI summarizes the full interaction history so the receiving agent or clinic is fully briefed, eliminating the need for patients to repeat information and reducing the AHT premium that transferred calls typically carry.

After a call, AI auto-generates call summaries, in-basket messages, e-mails, and any required downstream tickets, reducing after-call work by up to 2 minutes per interaction. AI can also support QA and training by analyzing calls to identify systemic and individual-level performance hotspots, such as workflow inconsistencies and off-script messaging, and develop personalized training for agents. (See “Spotlight on Access Center Quality Assurance and Training.”)

## - Spotlight on Access Center Quality Assurance and Training

One of the most underutilized levers in access center management is quality assurance. Most health systems sample fewer than 5% of interactions for manual review, meaning most agent behavior—including compliance gaps, patient safety escalations, and coaching opportunities—goes unobserved.

AI fundamentally changes this paradigm. Automated QA capabilities can evaluate significantly more interactions and provide real-time data on quality, compliance, resolution, and consumer satisfaction to both agents and their managers. Importantly, the architecture used to automate human-agent QA can be used to evaluate virtual agents, enabling access center leaders to compare outcomes across channels and prioritize areas for improvement.

A robust AI-driven QA capability can feed directly into personalized training tools that human agents can use to improve performance. Rather than generic group training sessions, the AI identifies the specific call types and interaction phases where each individual agent underperforms and generates targeted learning plans with constructive feedback. With new “synthetic” calling capabilities, these learning plans can be used to develop mock calls that human agents can have with virtual, but highly realistic, callers, reinforcing training with real-world, human-to-AI conversations.

Together, automated QA and personalized training co-pilots create a continuous improvement loop that compounds over time: better data on agent performance drives more targeted coaching, which in turn lifts performance and generates better outcomes.

To get the most from AI augmentation, systems must have a detailed understanding of how agents spend their time and adopt a human-centered design approach to developing agent-assist tools. Introducing another tool or interface to an agent's workflow is only valuable if it addresses existing pain points, enables agents to better address patients' needs, and improves the overall consumer experience.

# Amplify access-related revenue generation strategies.

Reconceptualizing the patient access function as a dynamic growth engine means treating each call not as a low-value interaction to resolve quickly and inexpensively but as a demand signal to convert, a relationship to deepen, and a care gap to close. Key growth levers include:

\- Demand capture. AI-powered 24/7 coverage and automated follow-up on unanswered and unresolved calls converts demand currently lost to staffing limits, after-hours gaps, and failed callbacks.

\- Ancillary attachment. AI surfaces relevant imaging, lab, pharmacy, and preventive care opportunities in real time during every interaction, enabling agents to offer appropriate ancillary services, providing new opportunities to meet patient needs and helping patients access required services.

\- Referral management. AI tracks referral status and triggers follow-up, reducing leakage within the network and improving closed-loop visibility for care teams (especially critical for high-margin commercial patients and specialty procedures).

\- Proactive outreach. AI-powered outbound agents can engage patients who have known care gaps, overdue screenings, or post-discharge needs, converting latent demand into scheduled visits.

\- “Segments of one”. AI can analyze a vast array of data to develop personalized, 360-degree patient profiles and create differentiated pathways for high-need and high-value patients, enabling systems to better guide patients to the appropriate level of care and provide enhanced service levels in strategically important service lines.

For our clients, incorporating growth-related strategies into their roadmap increases the projected margin uplift of AI-driven access center optimization by 3–5x versus focusing on cost alone. It also provides consumers with a seamless access experience, supports providers in seeing more patients, and improves the timeliness and responsiveness of care.

# The Critical Enabler: Clinical Operations and Change Management

Technology models, vendors, architecture, and infrastructure represent only about 30% of an AI transformation. People and change management account for 70%—but are often overlooked and underinvested.

Attempting to transform the access function with AI will fail without active partnership from the clinical and operational teams who control the inputs that the technology needs to perform. At most health systems, the scheduling rules, booking constraints, visit type configurations, and provider-level directives that govern access are neither centrally managed, consistently documented, nor designed for scale. At the same time, health systems often have unique provider-and clinic-specific business logic that is not codified in any system of record—from shared Excel trackers to unwritten knowledge that agents learn over time.

Because AI will only be as good as the foundation upon which it is built, systems must codify the formal and informal business logic that sits with human agents, MAs, and providers into structured inputs for AI to consume. This is often one of the most challenging tasks we support our clients in undertaking. Executives and function leaders consistently underestimate the operational effort required to execute a successful AI-enabled access center transformation, including:

\- Expansion of agent booking authority. In many systems, contact center agents are prohibited from booking directly into a significant share of visit types—not because the interactions are clinically complex, but because practices have historically preferred to control their own schedules. Relaxing these restrictions is one of the highest-leverage operational fixes available, and one that AI alone cannot unlock.

\- Accessibility of practices. Even with expanded booking permissions, human agents will need to contact clinics in certain instances. While there is often a phone number, e-mail, or EHR message channel available, clinics do not always answer calls, respond to messages, or address the needs of access center agents. Improving the clinic–access center relationship and committing to increased responsiveness is critical.

\- Provider alert and exception management. Dynamic information, such as a provider on leave, a practice that has closed, or a change in insurance acceptance, is often currently communicated on an ad hoc basis. Operational teams must formalize how this information flows into the access center for new AI solutions to operate reliably.

\- Template and visit type rationalization. Visit type mappings between what agents see and what lives in the EHR are frequently misaligned or incomplete. Rationalizing templates and establishing clean EHR-to-access center linkages is a prerequisite for reliable automation.

\- Insurance rule documentation. Insurance acceptance rules are often missing, inconsistent, or buried in free text. Closing these gaps requires direct engagement with clinic managers and revenue cycle teams to ensure appropriate routing of patients to providers.

Health systems that underinvest in clinical and operational change management will see their AI capabilities and financial ROI underperform relative to its technical potential. The systems that succeed treat access center transformation as a cross-functional program of highest strategic importance, not an IT project akin to a vendor migration. Senior executive and clinical sponsorship, shoulder-to-shoulder engagement with practice leaders, and clear accountability for the operational changes that AI enablement require is critical.

## A Call to Act—Now.

The access function is the primary interface between the system and its patients, the key channel to capture demand, and an underappreciated platform for growth. In an age of rapidly advancing AI, systems that view the technology as merely a means to reduce labor cost will quickly fall behind those that recognize it as tool to supercharge a key strategic asset.

AI capabilities are changing at breathtaking speed and scale. Systems must be prepared. Clear sequencing, strong governance, discipline to build required technical and organizational capabilities, and buy-in from clinical operations leaders are critical. The organizations that capture this value will be those who fund their journey through quick-win automation plays but don’t stop there. Instead, leaders that set their sights on transforming the access center as a means of growing and reaching patients in new ways will realize outsized value.

![](images/b6d4894b0c302c004baa09021d4181ddcb58ad2f76dd36332756caf2e20e72d8.jpg)

## Authors

![](images/524175f29e451cc74bdeeaada1fc882a66dccde7ca4d80a85e3ea4330409d3a7.jpg)

![](images/d64c66b60737c580dedcbb4cc85b1665e0bd0be5da20fe51a71634cb0aa8388e.jpg)

![](images/f4f3deb9d98ea65a0d02d0b78f663449e821cd4a30e8adbf073f0006b854e538.jpg)

![](images/15259bdc7640a589b4dfbdefa9dd8f4b67befe8eaa3099623f8ae1aa9022b33c.jpg)  
Natasha Taylor

Managing Director & Senior Partner
Denver

![](images/2c25259b36ce80a664f9e43c5625f03eaf91d416bae3060d9308bfa7059feb4a.jpg)  
Luke Purcell

Managing Director & Partner
New York

![](images/d3f9c637904491cb3d288f3fba895b35e0eeb8eaf446e8e87786963037764914.jpg)  
Scott Wilder

Managing Director & Partner Dallas

![](images/09d371746a3a3150edf56edc4c91181cad7e54b77c80a1fb070a6e6550c850f0.jpg)  
Michael Bernstein

Principal New York

![](images/03d798750c313e68b1b6afbc637962758dc61152a20d1e506379ac6f6d058242.jpg)

![](images/14b6d4e26ae661b4b8cb1f77219b9c9be5151023bc1a3ce6cd040c8fc615c9ee.jpg)

![](images/a60761b718790e6617ca0a5647fb7a039f0ed43553f6e62821e6bfb3141c481e.jpg)

![](images/0e16dfb199d7dc7329871a7144d5ac58563c2c2264d6629667e197569fd04847.jpg)

Managing Director & Partner
New York

![](images/b87707d6c8fecb0c91deb5119bb9f2a96a7cb39682aacd032d8c9db0027790e5.jpg)

![](images/b47398f404b0534378082d275a325058911b7155416d78f07e8ed31185fc9886.jpg)

Managing Director & Partner
Chicago

## Kevin Fleming

Partner
Denver

![](images/a287a6623236a55b903c4b8a896b609af1471c4eaa39e44d67dec4b7d1b40849.jpg)

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
9. 输出前自行核对：标题与导语不重复；每个小标题都是完整判断；没有元话语、推广语和未解问题栏目。只输出最终 Markdown，不输出核对过程。
