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
![](images/77692e85b01d6664d44d8c8a313cef27f2c31a2899c586643cabbdb4706ae64b.jpg)

MARKETING AND SALES

# Patients Are Sending Digital Signals. Are Companies Listening?

By Alex Baxter, Ben Quirt, and Benjamin Smith

ARTICLE JUNE 18, 2026 8 MIN READ

As pharma and medtech brands expand their efforts to attract prospective patients, they are losing a substantial number of them. Not because they underinvest in media planning or creative design but because they miss the signals patients send through web visits, survey responses, hub activity, and call center interactions. Those messages and usage metrics land in separate systems that are never collected and tailored into actionable next steps. The result is outreach that is run on fixed calendars rather than adapted to real patient behavior: it is broad, mistimed, and increasingly expensive as privacy rules erode the third-party data that traditional patient acquisition has depended on.

The organizations that are pulling ahead are using agentic AI to connect those fragmented signals into a single patient view and build a decisioning layer that determines, in real time, the right next step for each patient. The economics of getting there are more accessible than most teams assume.

## Why Legacy Programs Keep Losing Prospective Patients

The majority of patients now begin their health care journey online, including many who are ultimately referred to a specialist. Direct-to-patient (DTP) programs are the front door, yet most of those programs are outdated. Three structural shifts explain why those legacy models continue to underperform even when underlying demand is strong.

\- Patients expect accessible, easy-to-use digital tools. Digital-native health brands have normalized experiences that feel personal and responsive. Patients now judge health care brands against the best digital interactions they have had anywhere, not against category peers.

\- Static programs miss the moment. Many DTP models still run on predetermined sequences and broad segments whose cadence never changes based on what the patient is actually doing. When web visits, survey responses, hub touchpoints, and call history remain disconnected, teams cannot answer the questions that matter most: Is this patient stuck or progressing? Do they need education, reassurance, or a live conversation? What should happen next—today, not next week?

\- Privacy concerns are reshaping acquisition economics. As data regulations tighten, the tools that depend on broad tracking signals become harder and more expensive to scale. First-party, consent-based data—built directly from patient engagement—is now the most defensible conversion asset a health care brand can develop, because it compounds over time rather than depreciating.

“ Technology investment consistently outpaces activation. The bottleneck is rarely the platform; it is the absence of a shared patient data model and a journey roadmap that connects capability to measurable outcomes.

The organizational dimension makes coordination harder. DTP programs typically span digital, marketing, and data & analytics—and without clear ownership, patient progress stalls. Industrywide, only about 2% of brands have reached a level of data-driven marketing where decisions are made at the individual customer level across channels. Technology investment consistently outpaces activation. The bottleneck is rarely the platform; it is the absence of a shared patient data model and a journey roadmap that connects capability to measurable outcomes. (See the sidebar, “To Convert Patients, Adopt the Right AI Tools.)

## - To Convert Patients, Adopt the Right AI Tools

AI in patient marketing is not a single tool. Three capabilities work together, and the distinction matters for understanding where the real value lies:

\- Predictive AI scores each patient's likelihood of converting, dropping out, or needing a direct conversation, and updates that likelihood continuously as new signals arrive. It tells the system who needs attention and when.

\- Generative AI produces content variants at scale (email copy, SMS prompts, hub materials, discussion guides) within the boundaries of the medical, legal, and regulatory (MLR) review process. It eliminates the bottleneck where personalization breaks down because the content pipeline cannot keep up with the journey.

\- Agentic AI is the execution layer. It observes real-time signals, decides the next best action for each patient (channel, timing, content variant, or escalation to a human) and acts. Critically, it feeds every outcome back into the patient profile, so the system improves with each interaction rather than running the same sequences indefinitely.

Most health care organizations today have predictive or generative AI somewhere in production. The conversion gains come when agentic AI ties them together into a system that continuously improves.

This explains why DTP programs cannot be designed in isolation. For procedure-driven and prescription-led categories, patient demand and provider readiness are both necessary for a therapy to advance. The agentic infrastructure that improves patient conversion shares the same underlying signals that improve health care provider engagement—and they reinforce each other when they are built together.

# The Case for Investing in Personalization Now

The upside is visible in the results. A BCG analysis in health care provider systems benchmarked AI-driven personalized digital marketing at roughly six times return on marketing spend and a 20% incremental revenue lift when the underlying data and decisioning are in place.

At a major medtech company, an effort to convert leads into loyal customers using AI delivered in the first year a 10% reduction in cost per lead and a six-point lift in lead conversion rate.

Recent client engagements confirm the pattern. At a major medtech company, an effort to convert leads into loyal customers using AI delivered in the first year a 10% reduction in cost per lead and a six-point lift in lead conversion rate. In a separate engagement focused on cardiac monitoring-device adherence, an AI-powered activation program produced an 85% lift in patientreported activation and reversed a multiyear decline in 120-day device return rates. This translated directly to diagnostic yield and program economics.

These results reflect a different operating model, not a different budget. The organizations achieving them unified their signals, made real-time decisions about next steps, and reserved human capacity for the moments where a live conversation changes the outcome, such as when a patient is deciding, hesitating, or at risk of dropping out.

Outperforming health care and life sciences companies are already allocating more of their digital transformation budgets to these AI and data capabilities than their peers: the gap is widest precisely in the AI-adjacent capabilities that make agentic decisioning possible.

# A Practical Path: Diagnose, Unify, Then Deploy

The fastest route to better patient conversion is not rebuilding everything. It is identifying precisely where value is being lost today, then building only what is needed to activate the highest-impact patient journeys. The sequence is straightforward.

1. Conduct a focused diagnostic of current patient journeys.

Commercial and digital leaders do not need a month-long strategy exercise to get traction. A focused four-to-six-week diagnostic should do five things:

\- Quantify where patients drop out of the funnel and identify the behaviors that predict who will progress. This turns intuition into a prioritized backlog.

\- Map the patient journey across email, SMS, call center, and website. The gaps where patients disengage—because the next touchpoint does not match their intent—become obvious only when the full sequence is visible end-to-end.

\- Compare existing marketing technology with what the priority journeys actually require. The question is not what tools the organization owns, but what it can reliably trigger, personalize, and measure today.

\- Establish baseline funnel metrics and cross-channel visibility. Without these, automation will struggle to earn internal trust.

\- Align on two or three priority journeys, scored by impact versus effort. This forces discipline: the build follows value, not organizational politics.

The practical starting point is to bring together the signals that most consistently drive conversion decisions: hub activity, paid media engagement, survey responses and consent opt-ins, and call center interactions.

Once leaders agree on the priority journeys, unify first-party data signals into a single patient profile. At this point, the constraint shifts from ideas to data readiness. The practical starting point is to bring together the signals that most consistently drive conversion decisions: hub activity, paid media engagement, survey responses and consent opt-ins, and call center interactions. Selective enrichment with third-party data—claims data is usually the most valuable—improves decisioning where it can be clearly shown to do so.

The goal is one shared patient profile that every team can activate from, rather than each function maintaining its own version of the data. Perfection is not the standard; activation readiness is.

## 2. Deploy an agentic engine as the decisioning layer.

Unified data is necessary but does not execute the journey on its own. The agentic engine observes real-time patient signals (hub visits, device activation, survey completions, call center interactions, paid media engagement) and determines the next best action for each patient: which channel, what timing, which MLR-approved content variant, or whether to route to a human or agentic AI support. Every outcome feeds back into the patient profile, so the propensity scores and routing logic sharpen over time.

In practice, the three AI capabilities each carry a specific function:

\- Predictive AI for Patient Routing. Propensity models score patients continuously and reserve scarce hub resources (nurse educators, navigators, live representatives) for the patients and moments where human outreach changes the outcome.

\- Generative AI for Content Production. MLR-approved content variants (email copy, SMS prompts, hub explainers, discussion guides) are produced at the pace the journey requires, rather than becoming the review-cycle bottleneck that forces teams back to one-size-fits-all messaging.

\- Agentic AI for Orchestration. The decisioning and agentic engagement layer selects channel, timing, and content for each patient based on current behavior—not on a fixed calendar or the segment they were assigned at enrollment. It also surfaces patient context to live representatives in real time, so conversations are higher quality without requiring agents to search across systems.

## 3. Build in measurement from the start.

Agentic journeys scale only when teams can prove they work. A central analytics view that brings together funnel metrics, cohort performance, and journey outcomes is not optional infrastructure; it is what turns an AI pilot into a repeatable performance improvement. Structured testing that compares results across control and test groups isolates what is actually driving lift, and iterates on the components, timing rules, channel switches, and escalation thresholds that determine it. When stakeholders can see the test design and the control group, the decisioning layer stops feeling like a black box and starts earning the trust needed to scale.

# Building a Unified Patient Conversion Engine: Where to Start

For chief medical officers who are deciding whether to begin the process now, the minimum viable foundation consists of five elements:

\- A consented identity spine (typically email or phone) with current consent status for most in-funnel leads;

\- Unified signals across more than one touchpoint so the journey can respond to real behavior;

\- At least one live activation surface such as email, SMS, or a triggerable call center workflow;

\- A small MLR-approved content library with multiple variants for key journey stages; and

\- Baseline funnel metrics with the discipline to hold out a control group.

Having three of those five elements in place is enough to begin with a focused pilot built around a single patient journey and a clearly defined patient cohort. A diagnostic typically identifies leakage and produces a prioritized build roadmap in four weeks. The first AI-led direct-to-patient journey is generally measurable within eight to twelve weeks of build kickoff—allowing the team to realize measurable progress inside a single quarter rather than at the end of a multiyear transformation.

If a leader can check only one or two elements, the right first move is the diagnostic itself: it sequences the data, content, and measurement work needed to make a pilot meaningful rather than premature.

The strategic implication is straightforward. Creativity and media spend still matter, but they no longer determine the ceiling on patient conversion. Fragmented signals do. Unifying those signals turns scattered interactions into conversion leverage. Once that foundation exists, an agentic decisioning layer can route each patient through the right channels at the right time, without requiring heroic manual effort from hub teams. And because this work surfaces the same signals that matter for health care provider engagement, the two actions become mutually reinforcing rather than sequential.

That is how a DTP program stops being a set of disconnected campaigns and becomes a conversion engine that improves as every patient interacts with it.

## Authors

![](images/9251c96d4cfe0cf882d182cf1fc518e0a2dfc013b810a1ff83ffa0960db73379.jpg)  
Alex Baxter

Managing Director & Partner, BCG X

New York

![](images/a716d6f01a6873dfdc5366b649b63144351ccb09518ffbe3f5df165431ed3a7e.jpg)

![](images/5e3726fc29dded95daf5655936b80f5e3554df1e4a2f06f76693e09618d43090.jpg)  
Ben Quirt

![](images/2e54a8ed36c2522e963dfa884e8ffe94406d6bfcbe2cb1744a009a97136944bf.jpg)

Vice President, Commercial Transformation, BCG X
Austin

![](images/c2f9fb03673e14051c541be27c4eda5ed5330aab1334301848bb43fe27b4eeef.jpg)

Benjamin Smith

![](images/aeeac8e06ac59844f025535ddd359b86265c3ec9b7b5991720aac8be561a057b.jpg)

Lead Growth Architect
New York

## ABOUT BOSTON CONSULTING GROUP

Boston Consulting Group bridges the gap between ambition and outcomes for the world's leading companies and organizations. We are built for this era of unprecedented change — bringing strategic clarity rooted in over 60 years of deep domain knowledge, combined with applied AI shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com.
"""
