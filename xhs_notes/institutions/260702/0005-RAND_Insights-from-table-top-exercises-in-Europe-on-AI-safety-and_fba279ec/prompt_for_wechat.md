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
- 已识别机构名：`兰德公司`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份兰德公司研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Insights from table-top exercises in Europe on AI safety and cyber misuse

Afek Shamir, Henri van Soest, Stephen Clare & Sana Zakaria

For more information on this publication, visit www.rand.org/t/RRA5082-1

## About RAND Europe

RAND Europe is a not-for-profit research organisation that helps improve policy and decision making through research and analysis. To learn more about RAND Europe, visit www.randeurope.org.

## Research Integrity

Our mission to help improve policy and decision making through research and analysis is enabled through our core values of quality and objectivity and our unwavering commitment to the highest level of integrity and ethical behaviour. To help ensure our research and analysis are rigorous, objective, and nonpartisan, we subject our research publications to a robust and exacting quality-assurance process; avoid both the appearance and reality of financial and other conflicts of interest through staff training, project screening, and a policy of mandatory disclosure; and pursue transparency in our research engagements through our commitment to the open publication of our research findings and recommendations, disclosure of the source of funding of published research, and policies to ensure intellectual independence. For more information, visit www.rand.org/about/research-integrity.

RAND's publications do not necessarily reflect the opinions of its research clients and sponsors.

Published by the RAND Corporation, Santa Monica, Calif., and Cambridge, UK

© 2026 RAND Corporation

RAND® is a registered trademark.

Cover: Adobe Stock

## Limited Print and Electronic Distribution Rights

This publication and trademark(s) contained herein are protected by law. This representation of RAND intellectual property is provided for noncommercial use only. Unauthorised posting of this publication online is prohibited; linking directly to its webpage on rand.org is encouraged. Permission is required from RAND to reproduce, or reuse in another form, any of its research products for commercial purposes. For information on reprint and reuse permissions, please visit www.rand.org/pubs/permissions.

RAND Europe, the UK AI Security Institute (UK AISI) and Mila – Quebec AI Institute developed a series of tabletop exercises (TTXs) to explore artificial intelligence (AI) risks. This report presents the design, execution and findings of three TTXs run for senior policymakers in Germany, the Netherlands and France. The exercises were developed to support European and global decision-makers as they engage pragmatically with the AI misuse and malfunction risks identified in the 2026 International AI Safety Report. The scenario detailed in this report focuses on the use of AI capabilities by criminal actors to conduct large-scale cyberattacks.

The TTXs utilise RAND's ‘Day After’ methodology: two-turn table-top simulations in which participants, playing the roles of Ministerial Cabinet members, confront a crisis scenario requiring their judgements and policy steer. After receiving a written and verbal brief, participants are asked to identify appropriate responses and develop compelling courses of action.

The crisis scenario centres on a domestic AI company, backed by the national government as a tech ‘champion’, which is ambiguously tied to a string of AI-enabled cyberattacks made possible by rapid advances in leading AI models’ coding capabilities. This report focuses on the design of this scenario and covers key issues shaping participant discussion and decision-making, as well as the capabilities and governance measures that participants identified as most urgently needed.

## Funding

This research was conducted by RAND Europe in collaboration with the UK AI Security Institute in its capacity as Secretariat to the International AI Safety Report. The TTXs were delivered jointly by RAND Europe and the Secretariat to the International AI Safety Report. Funding was also provided by the UK AI Security Institute. RAND donors and sponsors have no influence over research findings or recommendations.

This report presents the findings from three table-top exercises (TTXs) designed to help senior officials engage practically with the challenges posed by emerging AI risks. Knowing what the evidence says about AI risk is different from knowing how to use it to make effective decisions. Contextualising and adapting that evidence to a variety of different policy goals and institutional contexts is a challenging, and often neglected, task. This report presents results from a novel effort to bridge this gap: placing policymakers inside a simulated AI-driven cyber crisis, based on findings about capabilities and trends from the 2026 International AI Safety Report, and tasking them with developing practical policy responses.

The TTXs highlighted significant gaps in AI incident response plans, including difficulties in gathering reliable evidence on AI capabilities and risks and coordinating across institutions to grapple with a highly capable, general-purpose technology. But they also surfaced a range of promising response possibilities, including leveraging existing incident response protocols and deploying AI systems to accelerate defensive efforts.

Three discrete exercises were conducted in Berlin, The Hague and Paris under a programme developed jointly by RAND Europe and the UK AI Security Institute. Using RAND's ‘Day After’ methodology, each session placed 15 to 20 senior officials in the role of Ministerial Cabinet members confronting a dramatic increase in cyberattacks driven by improving AI capabilities. The exercises were built to answer three questions:

1. What information do policymakers need when an AI crisis is underway?

2. What preparatory measures would governments have found helpful?

3. What immediate policy responses would they judge most urgent?

Participants encountered multiple difficulties, including persistent evidence gaps, trade-offs between acting more quickly or waiting for more information, and coordination challenges among the range of actors involved. Seven discussion topics recurred across the exercises:

\- Defining the crisis threshold. When does the pace and scale of AI-enabled cyberattacks amount to a national crisis rather than a more routine operational problem?

\- Engaging a national AI champion. In the exercise, the state had publicly backed and funded the problematic model's developer. Acting against its interests meant admitting a governance failure and absorbing the political and economic cost of turning on a strategic asset.

\- Calibrating risk management when capabilities cannot be reliably evaluated. With no trustworthy way to assess the model's risks independently, government was left relying on the developer's voluntary – and potentially biased – risk assessments.

\- Preventing open-weight misuse. The diffusion of a highly-capable open-weight model in Turn 2 raised new challenges, as it is harder to monitor and implement safeguards on open-weight models.

\- Hardening critical infrastructure. Proposals for protecting vulnerable systems ranged from restricting access to the AI model to simulating attacks against critical systems.

\- Utilising this crisis as a catalyst for positive institutional change. The crisis brought attention, resources and political will that could be used to invest in durable preparedness measures.

\- Cooperating with allies. Whether to restrict threat intelligence to trusted minilateral networks or share information broadly, including with potential adversaries.

Participants also identified several priorities for crisis preparation. These centred on proactively generating evidence about AI capabilities and crisis response plans and creating communication channels and institutions to coordinate government response. Specifically, discussions surfaced the following priorities:

\- Pre-agreed escalation thresholds. Without clear triggers for when an AI incident becomes a national crisis, participants spent time debating what they were facing rather than responding to it.

\- Systematic cyberdefence reviews. National agencies lacked a baseline assessment of how exposed critical infrastructure and government systems were to AI-enabled attacks, and so could not triage during the crisis.

\- Independent technical capacity to evaluate AI risks. Relying on the developer's own account of its model's risks left government unable to confidently assess the risk level.

\- Targeted crisis communications strategies. Specific, practical information for the most-exposed actors was more useful than broad warnings or silence.

\- Multilateral governance frameworks that can activate quickly. International cooperation was needed to manage risks and models that cross borders, but negotiations were too slow during the crisis.

\- Structured information flows between developers and government. In the crisis, governments were reliant on what information the developer chose to share. Public funding and procurement measures would provide leverage to obtain more information.

Beyond the substantive findings, the exercises show how rigorous risk assessment can be turned into practical policy preparation. Grounding the scenario in the 2026 International AI Safety Report's assessment of capabilities and trends made it realistic and evidence based rather than speculative; and dramatising findings as a live policy challenge made them concrete and actionable for the officials who must prepare for real events.

Preface ....i
Executive summary ....ii
Glossary ....v
Acknowledgements....vi
1. Scenario design....1
2. Scenario summary....4
3. Key discussion themes....5
4. Capabilities to invest in....10
5. Limitations....13
6. Conclusion and next steps....14
References....15

<table><tr><td>Open-source / open-weight models</td><td>Models with publicly downloadable weights; ‘open-source’ further implies permissive code/licensing and sometimes broader transparency.</td></tr><tr><td>Agents / agentic AI</td><td>AI systems that can plan, act and adapt to pursue goals across multi-step tasks with limited human oversight.</td></tr><tr><td>Frontier AI models</td><td>The most capable models at the cutting edge of performance and potential risk.</td></tr><tr><td>General-purpose AI (GPAI) models</td><td>Broadly capable models designed to perform many tasks across domains rather than a single narrow use.</td></tr><tr><td>Distillation</td><td>A form of training in which a ‘student’ AI model learns by imitating the outputs of a more powerful ‘teacher’ system.</td></tr><tr><td>Red-teaming</td><td>A systematic process in which dedicated individuals or teams search for vulnerabilities, limitations or potential for misuse through various methods. In AI, red teams often search for inputs that induce undesirable behaviour in a model or system.</td></tr><tr><td>Evidence dilemma</td><td>The challenge that policymakers face when making decisions about a new technology before there is strong scientific evidence about its benefits or risks, forcing them to weigh the risk of creating ineffective or unnecessary regulations against the risk of allowing serious harms to occur without adequate safeguards.</td></tr><tr><td>Adversarial prompting / prompt injection</td><td>Techniques used to manipulate an AI model into producing outputs it was designed to refuse, either by crafting inputs that circumvent safety filters or by embedding malicious instructions within data the model is asked to process.</td></tr><tr><td>Weight exfiltration</td><td>The unauthorised copying or theft of a model’s trained parameters, which can be used to recreate the model’s capabilities outside the developer’s control and without any of its original safeguards.</td></tr><tr><td>Staged / staggered access</td><td>A model release approach in which access is granted incrementally to different user groups over time, allowing developers and regulators to monitor for misuse and intervene before capabilities are made widely available.</td></tr><tr><td>Minilateral network</td><td>A small coalition of like-minded states that coordinates on a specific issue outside larger multilateral bodies, typically enabling faster decision-making and higher levels of trust among participants.</td></tr></table>

We thank Patrick King, Samuel Kenny, Kat Lyness and Jai Sood at the UK AI Security Institute and Department for Science, Innovation and Technology (DSIT) for their partnership throughout the design and delivery of the exercises described in this report. We are grateful to the participants in Berlin, The Hague and Paris, who generously gave their time and engaged substantively with all sessions. We also thank Carina Prunkl for her support in developing the scenarios. We thank RAND's Geopolitics of AGI Center for training facilitators and for support throughout this project, particularly Rich Girven and Gregory Smith. Finally, we are grateful to our reviewers and the publications team at RAND Europe.

## 1. Scenario design

The table-top exercises (TTXs) covered in this report use RAND's ‘Day After’ methodology: a two-stage simulation in which participants, playing Ministerial Cabinet members, confront a crisis requiring their judgement and policy action. After a written and verbal brief, they identify appropriate responses and develop courses of action.

The scenario in the TTXs centres on a domestic artificial intelligence (AI) company, backed by the national government as a tech ‘champion’, that is ambiguously tied to a string of AI-enabled cyberattacks made possible by rapid advances in frontier models’ coding capabilities. This section sets out the scenario’s design and the questions it was designed to elicit.

## Building on the 2026 International AI Safety Report

The scenario translates the risks identified in the International AI Safety Report into operational challenges for political leaders. As the most comprehensive review of the science on general-purpose AI (GPAI), chaired by Dr. Yoshua Bengio with over 100 independent experts contributing and an Expert Advisory Panel representing more than 30 countries and intergovernmental organisations, the Report establishes a global baseline on AI capabilities and delineates three risk categories: malicious use, malfunction and systemic risk. The methodological aim of the TTXs was to operationalise the science: by dropping policymakers into a multi-turn crisis, the simulation forced them to confront a scenario in which technical risks compound into cascading national security, economic and diplomatic threats.

The scenario models how the criminal exploitation of a commercial frontier system can overwhelm national defences. The International AI Safety Report finds that dual-use capabilities may significantly expand the scale and speed of cyberattacks. $^{1}$ The exercise operationalises this risk using a fictional AI model called ‘FlowGPT’, a state-backed domestic model with significant commercial value. In the scenario, criminal networks systematically exploit the model to automate phishing and data harvesting, causing a surge in cyber incidents. This forces participants to manage immediate financial and operational shocks, such as regional banking fraud and the targeting of public sector information.

The scenario integrates the ‘evaluation gap’ concept in the Report to test how governments handle imperfect information about technical risks during deployment. This evaluation gap highlights that pre-deployment testing cannot yet reliably quantify the misuse potential of dual-use models. $^{2}$ In Turn 1 of the exercise, participants face a developer whose internal safety tests have flagged potential risks but could not calculate their exact impact. This is paired with a regulator that authorised deployment because no explicit harm had yet been demonstrated. Participants must navigate the ‘evidence dilemma’: in particular, the political difficulty of acting on an anticipated threat before harm occurs. A national competitiveness element also becomes vivid in this scenario. Restricting a national AI champion based on potential risks creates immediate commercial and political blowback. However, waiting for clear evidence may leave the state in a reactive posture, forcing leaders to implement containment strategies after critical infrastructure and public trust are compromised.

The simulation also highlights the governance challenges of the open-weight ecosystem. Turn 2 introduces ‘PieAI’, a similarly capable model that may have been cloned via exfiltrated weights or student-teacher model distillation from FlowGPT. Misuse risks from this model exacerbate the threat landscape, because unlike FlowGPT, whose safeguards can be evaded but not removed, PieAI’s model can be downloaded and modified directly. This design choice forces participants to think beyond localised enforcement, examining what type of cooperation with other national and international bodies is necessary to address misuse risks from open-weight models.

## What the exercises were designed to address

The exercises were designed to generate structured insights on three categories of questions:

1. What information do key policymakers require when confronting AI-related crises?

2. What capabilities would policymakers wish their governments had developed in advance of such a crisis?

3. What governance measures and policy frameworks would participants identify as most urgently needed in light of this crisis?

## Exercise structure

Each TTX session ran for approximately two hours and followed a two-turn structure adapted from the Day After methodology developed by RAND. All three cohorts were faced with the same scenario. Each turn ran for approximately 50 minutes. The exercises were designed to require no advance preparation from participants and to be accessible to officials without robust AI or technical backgrounds. That said, the scenarios were more technically granular than some of RAND's other ‘Infinite Potential’ scenarios, which are often more strategic and geopolitical in nature. $^{3}$ This is largely because of this exercise's grounding in the technical, scientific and consensus-based nature of the International AI Safety Report.

Each session opened with brief scene-setting from the facilitator, establishing the exercise format and the participant role: each participant is a senior Cabinet official without a specifically assigned ministerial portfolio. An expert briefer, who plays the role of an intelligence analyst, was then introduced to brief the participants, and was available to answer factual questions about the crisis situation itself. This format is designed to addres

[中间内容因长度限制已省略]

ma that no governance framework currently addresses adequately.

## 5. Limitations

The insights generated from the TTXs are subject to several limitations inherent to the 'Day After' methodology. Firstly, a compressed two-hour simulation involving senior policymakers cannot wholly replicate the operational friction, information scarcity, or prolonged psychological toll of an unfolding, multi-week crisis. Secondly, the limited number of participants (3 exercises with \~55 players total) constitutes a small sample size, and we recognise a larger sample size may identify a wider or different collection of issues. Thirdly, the findings represent the qualitative judgments of a specific cohort of participants from select ministries and do not reflect official government policy or an exhaustive consensus. Fourthly, the findings reflect European governance contexts, institutional frameworks and policy cultures. Exercises with non-European participants – including from the global south and from states with different AI regulatory approaches – would likely produce different key issues and different proposed responses. While TTXs are highly effective at surfacing institutional blind spots, governance gaps and strategic friction points, they are designed to explore the spectrum of plausible decision-maker behaviours rather than to predict specific pathways or definitive policy outcomes.

This report presents findings from three TTXs run with senior government policymakers in Germany, the Netherlands and France. The exercises were designed in collaboration between RAND, the UK AI Security Institute, and Mila – Quebec AI Institute, and grounded in the 2026 International AI Safety Report. We attempted to place senior policymakers inside an unfolding AI crisis and observe what governance and policy mechanisms become pivotal during the response to the event. Across sessions, participants wrestled with a consistent set of challenges: how to define and respond to a new category of AI-enabled threat, how to govern a developer the state had publicly championed, how to act on evaluation uncertainty, and how to build international responses that move faster than multilateral diplomacy typically allows. From those discussions, a shared set of capability priorities emerged, which included: AI incident escalation thresholds, hardened cyberdefences, independent technical capacity at the heart of government, targeted crisis communications, multilateral governance and enforcement, and increased information flows between AI companies and government.

Our next steps are to repeat this scenario with other audiences, not solely in government, and to run several of our other scenarios developed jointly with UK AISI. Future exercises could pursue several directions. Firstly, wider geographical reach: for instance, sessions in Asia are already scheduled and will begin to test whether the governance challenges identified in European sessions hold across different regulatory cultures, state-developer relationships, and levels of AI maturity. Secondly, future scenarios should engage more directly with questions of technological sovereignty and geopolitical positioning. The current scenario surfaces these tensions but does not force participants to resolve them, and a more geopolitically explicit design would generate richer findings on how middle powers navigate strategic dependence on foreign frontier AI providers and companies across the AI supply chain. Thirdly, the governance landscape has shifted since our scenarios were designed: staggered and staged access regimes are increasingly becoming standard practice, with developers and regulators regarding controlled rollouts as increasingly necessary to give defenders an edge. Future scenario design should reflect this development, testing how staged access frameworks perform under adversarial pressure and what governance architecture is needed to make them effective.

Anthropic. 2026. ‘Project Glasswing: Securing Critical Software for the AI Era.’ As of 22 June 2026: https://www.anthropic.com/glasswing

Bengio, Yoshua, et al. 2026. International AI Safety Report 2026. ArXiv. As of 22 June 2026: https://arxiv.org/abs/2602.21012

European Commission. 2025. ‘The General-Purpose AI Code of Practice.’ Shaping Europe’s Digital Future. As of 22 June 2026: https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai

Millot, Marc Dean, et al. 1993. “The Day After…” Study: Nuclear Proliferation in the Post-Cold War World. Volume II, Main Report. Santa Monica, Calif.: RAND Corporation. MR-253-AF. As of 22 June 2026: https://www.rand.org/pubs/monograph\_reports/MR253.html

Paskov, Patricia, et al. 2026. Open-Weight AI Models Require Proportional Evaluation Approaches. Santa Monica, Calif.: RAND Corporation. PE-A4886-1. As of 22 June 2026: https://www.rand.org/pubs/perspectives/PEA4886-1.html

Predd, Joel B., et al. 2025. Infinite Potential—Insights from the Two Moonshots Scenario: After-Action Report from a Sequence of Day after Artificial General Intelligence Exercises. Santa Monica, Calif.: RAND Corporation. RR-A4230-1. As of 22 June 2026: https://www.rand.org/pubs/research\_reports/RRA4230-1.html

Smith, Gregory, et al. 2025. Infinite Potential—Insights from the Robot Insurgency Scenario: After-Action Report from a Sequence of Day after Artificial General Intelligence Exercises. Santa Monica, Calif.: RAND Corporation. RR-A4231-1. As of 22 June 2026: https://www.rand.org/pubs/research\_reports/RRA4231-1.html

UK AISI. 2025. ‘Managing Risks from Increasingly Capable Open-Weight AI Systems.’ As of 22 June 2026:
https://www.aisi.gov.uk/blog/managing-risks-from-increasingly-capable-open-weight-ai-systems
"""
