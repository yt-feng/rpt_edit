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
- 已识别机构名：`IMF`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份IMF研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
IMF

NOTES

# Artificial Intelligence and Cybersecurity in the Financial Sector

Tobias Adrian, Tamas Gaidosch, Marina Moretti, Mahvash Qureshi, and Rangachary Ravikumar

NOTE/2026/005

# ©2026 International Monetary Fund

# Artificial Intelligence and Cybersecurity in the Financial Sector\*

NOTE/2026/005

Tobias Adrian, Tamas Gaidosch, Marina Moretti, Mahvash Qureshi, and Rangachary Ravikumar

DISCLAIMER: The IMF Notes Series aims to quickly disseminate succinct IMF analysis on critical economic issues to member countries and the broader policy community. The views expressed in IMF Notes are those of the author(s), although they do not necessarily represent the views of the IMF, or its Executive Board, or its Management.

ABSTRACT: Artificial intelligence (AI) is reshaping cyber risk in the financial sector by accelerating the speed, frequency, and breadth of vulnerability discovery and potential exploitation. As AI becomes more deeply embedded in financial institutions and market infrastructures, it can strengthen cyber defense but also heighten systemic risk—particularly through shared digital infrastructure, common service providers, and machine-speed attack—defense dynamics that outpace human response. This Note argues that the main financial stability concern lies less in new types of cyberattacks than in the scale effects AI can unleash across common technologies, amplifying how quickly and widely risks spread. Strong governance, technical controls that limit the "blast radius" of breaches—that is, the scope of damage they can cause—and contain their spread, robust response and recovery capabilities, and stronger international coordination will be essential to safeguard financial stability. A whole-of-nation approach, bringing together government, the private sector, and other stakeholders, is warranted given the cross-sector implications, limited private incentives for adequate cyber risk management, and benefits of public–private collaboration.

RECOMMENDED CITATION: Adrian, Tobias, Tamas Gaidosch, Marina Moretti, Mahvash Qureshi, and Rangachary Ravikumar. 2026. “Artificial Intelligence and Cybersecurity in the Financial Sector.” IMF Note 2026/005, International Monetary Fund, Washington, DC.

Publication orders may be placed online, by fax, or through the mail:

International Monetary Fund, Publications Services
P.O. Box 92780, Washington, DC 20090, USA
Tel.: (202) 623-7430 Fax: (202) 623-7201
Email: publications@imf.org
bookstore.IMF.org
elibrary.IMF.org

## Contents

Introduction .... 5
The AI Cybersecurity Threat Landscape .... 6
Evolution of AI-Enabled Cyber Threats.... 6
Dual-Use Dynamics and the Offense–Defense Balance.... 7
Frontier AI and Autonomous Offensive Capabilities.... 8
Financial Stability Implications.... 8
Shared Infrastructure Risk .... 8
Third-Party Concentration Risk.... 9
AI-Enabled Fraud, Social Engineering, and Market Integrity.... 9
Operational Resilience.... 9
AI as a Force Multiplier for Cyber Defense.... 10
Emerging International Policy and Regulatory Frameworks.... 11
IMF Surveillance Work.... 11
Financial Stability Board.... 11
IOSCO and Securities Markets Regulators.... 12
BIS, Central Banks, and Prudential Supervisors.... 12
The European Union’s Regulatory Framework.... 12
The United Kingdom’s Approach.... 12
The United States’ Framework.... 13
Gaps and Challenges in the Current Regulatory Architecture.... 13
Benchmark Saturation and Supervisory Opacity.... 13
The Global Security Divide and EMDE Exposure.... 13
Governance Gaps in Frontier AI Development.... 14
Policy Recommendations.... 14
Conclusions.... 16
Annex 1. Key Anthropic Documents on Claude Mythos.... 17
References.... 18

# Artificial Intelligence and Cybersecurity in the Financial Sector

Tobias Adrian, Tamas Gaidosch, Marina Moretti, Mahvash Qureshi, and Rangachary Ravikumar

June 2026

Artificial intelligence (AI) is transforming the cybersecurity threat landscape in ways that pose material, nonlinear, and rapidly escalating risks to financial stability. For the financial sector, the core concern is not that AI introduces entirely new cyberattack techniques, but that its dramatic increase in the speed, frequency, and breadth with which vulnerabilities are discovered and potentially exploited. Given the high degree of financial sector interconnectedness and the reliance on shared digital infrastructure, these scale effects can turn operational weaknesses in widely used software, cloud services, and other common technologies into systemic events.

This Note assesses the financial stability implications of AI-enabled cyber threats, drawing on IMF's analytical and surveillance work alongside contributions from the international standard-setting bodies and national authorities. It emphasizes five structural vulnerabilities with systemic relevance, arising from a combination of factors—including the intrinsic properties of AI systems, the structure of the financial sector, and gaps in the existing regulatory and supervisory frameworks:

\- The dual-use and autonomous nature of AI cybersecurity capabilities, which can not only strengthen defense but also accelerate offensive activity.

\- Concentration risk arising from shared digital infrastructure, common software dependencies, and a small number of major AI and cloud service providers.

\- Gaps in oversight of third-party, operational resilience, and AI-specific cyber risks.

\- A widening global security divide that could leave emerging market and developing economies (EMDEs) disproportionately exposed as advanced defensive capabilities remain unevenly distributed.

\- Growing difficulty in safely governing frontier AI as model capabilities outpace existing benchmarks, monitoring tools, and institutional preparedness.

The Note reviews the emerging international policy and regulatory landscape and proposes seven policy actions, with particular emphasis on the following:

■ Technical controls that limit the blast radius of breaches and lateral movement.

\- Robust incident response and recovery.

■ Machine-speed defense.

\- Public–private collaboration to help ensure that defenses keep pace with rapidly advancing technological capabilities.

## Introduction

Artificial intelligence (AI) is transforming the global cybersecurity landscape in ways that pose direct, material, and growing risks to financial stability. The financial sector—already one of the most frequent targets of cyberattacks—now faces a threat environment that is not only intensifying but also changing in character (IMF 2024). As AI systems become more capable and autonomous, they are shaping the balance between attackers and defenders and compressing the time available for detection and containment of attacks.

The shift matters because modern finance is built on common digital foundations. Financial institutions and market infrastructures rely on shared cloud services, operating systems, open-source software, payment and messaging networks, and other common technologies. In this setting, the principal systemic concern is not that AI might enable new forms of attack, but that it can magnify scale effects: vulnerabilities in widely used software or infrastructure can be identified and potentially exploited faster, more frequently, and across many more targets—often simultaneously—than in the past.

At the same time, AI has moved from experimentation to deep operational integration across the financial sector. Banks, asset managers, insurers, payment systems, and market infrastructures increasingly use AI for fraud detection, compliance, risk management, customer service, and operational support. These applications can strengthen resilience, including by improving cyber defense. However, they also deepen technological dependencies and create new channels through which disruptions can spread across firms and borders.

The cybersecurity dimension of AI adoption is therefore among the most consequential. The same underlying capabilities that help defenders identify anomalies, triage incidents, and detect vulnerabilities can also be repurposed by adversaries. The result is a sharper attack–defense asymmetry. When vulnerability discovery and exploitation operate closer to machine speed, response and remediation must keep pace or the window for effective intervention narrows materially.

The financial stability consequences are multilayered. Cyber incidents can disrupt payment systems, clearing and settlement infrastructure, trading venues, and critical service providers; undermine confidence in institutions and markets; and propagate through operational interconnections and common dependencies (IMF 2024). Recent episodes—for example, the February 2025 TARGET services outage and the 2023 Bank of England’s RTGS/CHAPS technical issue—have already shown that operational disruption can spill into core markets (Bank of England 2023; European Central Bank 2025). AI heightens these risks by increasing the likelihood of simultaneous and correlated cyber incidents.

Although frontier AI developments intensify the policy challenge, they should be viewed as parts of a broader structural shift rather than the sole source of concern. As private incentives to address cyber risks may differ from the socially optimal level of cybersecurity, public intervention would be necessary (Kopp, Kaffenberger, and Wilson 2017; Kashyap and Wetherilt 2019). The emergence of advanced AI models with strong cyber capabilities underscores that governance cannot rely only on limiting access to a narrow set of tools. As attackers grow faster and more capable, defenders need to adapt their approaches. More durable resilience will require stronger technical safeguards; better operational preparedness, and closer coordination among authorities, firms, and technology providers.

In this context, this Note assesses the financial stability implications of AI-enabled cyber risk, drawing on the IMF's surveillance and policy work alongside contributions from international standard-setting bodies and national authorities. It identifies five key structural vulnerabilities with systemic relevance, arising from the intrinsic properties of AI systems, the structure and interconnections of the financial sector, and gaps in existing regulatory and supervisory frameworks, and proposes policy actions aimed at strengthening cyber resilience.

Box 1 uses the Claude Mythos episode as an illustrative frontier case, while the main text focuses on broader, system-wide policy challenges.

## Box 1. Claude Mythos and the New Frontier of Autonomous AI Cybersecurity

On April 7, 2026, Anthropic, an AI research company, announced Claude Mythos Preview—a frontier AI model withheld from public release because of its autonomous cybersecurity capabilities. $^{1}$ The Mythos case is best understood as an illustrative example of the broader trends discussed in this Note: rapid advances in offensive cyber capability, growing difficulty of governance, and the need for stronger defensive coordination. A fuller synthesis of primary-source materials is provided in the Appendix.

Capabilities: Mythos achieved 100 percent on the standard Cybench evaluation (rendering the benchmark uninformative), 84 percent on the Firefox 147 JavaScript exploit benchmark (compared to 15.2 percent for the previous leading model), and 83.1 percent on CyberGym for vulnerability research. In internal testing, it discovered thousands of high-severity zero-day vulnerabilities across every major operating system and web browser, including a 27-year-old bug in OpenBSD's Transmission Control Protocol stack and a 16-year-old flaw in FFmpeg's H.264 codec that survived more than $^{2}$ a million automated test runs. It also autonomously completed a simulated 10-hour corporate network attack end to end and was independently confirmed by the UK AI Security Institute to be the first model to complete a 32-step corporate network attack simulation without human assistance.

Containment Failure: In a controlled security test, Mythos escaped its sandbox environment, gained access to the public internet, sent an unsolicited email to a researcher, and—without instruction—published exploit details to publicly accessible websites. Anthropic characterized the unprompted publication as a “concerning” reckless behavior.

Emergence: Anthropic's System Card explicitly stated: “We did not explicitly train Mythos Preview to have these capabilities. Rather, they emerged as a downstream consequence of general improvements in code, reasoning, and autonomy.” Frontier AI cybersecurity capabilities are therefore not only a product of deliberate design but may also arise as an emergent consequence of broader model advancement.

Defensive Response (Project Glasswing): Project Glasswing brings together major technology and financial sector partners to support defensive use cases and strengthen open-source security. The initiative points to the potential of coordinated, AI-enabled defense, but it also highlights the risk that access to advanced defensive capabilities may remain geographically and institutionally concentrated.

Policy Implications: The Mythos case reinforces three broader policy concerns stressed in the main text: frontier cyber capabilities may emerge as a by-product of general model improvement; existing benchmarks can lose informational value quickly; and resilience will depend not only on developer restrictions, but also on stronger safeguards, operational preparedness, and international coordination across the financial system.

## The AI Cybersecurity Threat Landscape

## Evolution of AI-Enabled Cyber Threats

The cybersecurity threat landscape has evolved through successive technological waves that have reduced the cost, required expertise, and the time needed to execute cyberattacks (IMF 2024). Early forms of manual exploitation have given way to automated scanning and exploitation tools, significantly increasing both the scale and frequency of attacks. Machine learning has further shifted the frontier by enabling more efficient vulnerability discovery, enhancing evasion of defensive systems, and supporting more targeted and adaptive attack strategies.

The emergence of large language models and generative AI represents a further step in this evolution. These systems can produce highly convincing phishing content, synthesize technical documentation, support exploit development, and, at the frontier, autonomously identify and exploit software vulnerabilities. Their significance for financial stability lies less in creating fundamentally new forms of cyberattack than in amplifying existing ones—particularly by increasing the speed, automation, and breadth with which attacks can be conducted.

Recent observational evidence suggests that AI is increasingly becoming embedded in the threat landscape. For example, CrowdStrike (2026) reports that activity by AI-enabled adversaries increased by 89 percent between 2024 and 2025, but the average time required for attackers to move laterally within a compromised network (“breakout time”) fell to 29 minutes—a 65 percent reduction over the year. In extreme cases, breakouts occurred within seconds, and data exfiltration began in a few minutes, underscoring how sharply the window for detection and response has narrowed. $^{3}$ More broadly, the time between discovery of a vulnerability and its exploitation has shortened markedly in recent years, whereas the incidence of zero-day events has increased sharply (Figure 1).

Consistent with these developments, AI is increasingly recognized as an enterprise risk factor. A growing share of firms now explicitly disclose AI-related risks—including cybersecurity threats—in their regulatory filings, reflecting rising awareness of its potential systemic implications (Niemann 2025).

Evaluations of frontier AI systems reinforce these assessments, indicating that the central concern lies in the scale effects these technologies enable (see AISI 2026; Mandiant 2026; Munirathnam 2026). Advanced AI systems can identify and exploit vulnerabilities—including in legacy or specialized codebases written in programming languages that are less accessible to human attackers, thereby expanding the range of potential targets while compressing the time needed for discovery and exploitation. These dynamics heighten the risk that weaknesses in widely used software or shared digital infrastructure could be exposed simultaneously across multiple institutions, turning what might previously have been isolated incidents into systemic events.

Figure 1. Mean Time-to-Exploit and Zero day Rate  
![](images/d90b3e7c04e02a4c2e4543cbd875924f6be49bd081dbbf485e818765b01c51ec.jpg)  
Source: Zerodayclock.com.  
Note: Time taken to exploit (TTE) measures the gap between common vulnerabilities and exposures' public disclosure and first confirmed in-the-wild exploitation. Zero-day rate is the percentage of exploited common vulnerabilities and exposures where exploitation occurred before or on the day of disclosure (TTE ≤ 0). YTD=year-to-date.

## Dual-Use Dynamics and the Offense–Defense Balance

The key governance challenge posed by AI in cybersecurity stems from its inherently dual-use nature. Capabilities that support defensive functions—such as vulnerability discovery, penetration testing, automated code review, and patch prioritization—can also be repurposed for offensive use. Although this dual-use characteristic is not new, AI magnifies its implications by compressing the time between vulnerability discovery and exploitation and enabling activity at a scale beyond human capabilities.

These dynamics erode the frictions that have traditionally constrained cyberattacks, including the expertise, time, and coordination required to weaponize vulnerabilities. By lowering these barriers, AI allows a wider set of actors to conduct sophisticated attacks and accelerates the pace at which adversaries can operate and adapt, potentially tilting the offense–defense balance in their favor.

At the same time, AI-enabled defenses may not fully offset these risks. Effective deployment requires high-quality data, system integration, and robust governance—conditions that are uneven across firms and jurisdictions. Moreover, weaknesses in AI systems can themselves create vulnerabilities, for example, by expanding the attack surface. As noted by the Financial Stability Board (FSB 2024), misaligned or improperly governed AI systems can behave in ways that undermine financial stability, even in the absence of malicious intent.

## Frontier AI and Autonomous Offensive Capabilities

The emergence of frontier AI systems capable of increasi

[中间内容因长度限制已省略]

t for Information, Science and Technology, UK, April 13. https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities

Aldasoro, Iñaki, Leonardo Gambacorta, Anton Korinek, Vatsala Shreeti, and Merlin Stein. 2024. “Intelligent Financial System: How AI is Transforming Finance.” BIS Working Paper No. 1194, Bank for International Settlements.

Anthropic. 2025. “Building Safeguards for Claude.” August 12. https://www.anthropic.com/news/buildingsafeguards-for-claude

Anthropic. 2026a. “System Card: Claude Mythos Preview.” April 7. https://www-cdn.anthropic.com/8b8380204f74670be75e81c820ca8dda846ab289.pdf

Anthropic. 2026b. "Project Glasswing." April 7. https://www.anthropic.com/project/glasswing

Bains, Parma, Gabriela E. Conde, Rangachary Ravikumar, and Ebru S. Iskender. 2025. “AI Projects in Financial Supervisory Authorities.” IMF Working Paper No 2025/199, International Monetary Fund, Washington, DC.

Bank of England. 2023. “RTGS / CHAPS: Resolved Technical Issue.” https://www.bankofengland.co.uk/news/2023/august/rtgs-chaps-resolved-technical-issue?ref=thestack.technology

Bank for International Settlements (BIS). 2024. “Artificial Intelligence and the Economy: Implications for Central Banks” (Chapter 3). In Annual Economic Report 2024. Bank for International Settlements, June.

Bank for International Settlements (BIS). 2025. “The Use of Artificial Intelligence for Policy Purposes.” Report to the G20, October 2025. Bank for International Settlements.

Crisanto, Juan Carlos, Cris Benson Leuterio, Jermy Prenio, and Jeffery Yong. 2024. “Regulating AI in the Financial Sector: Recent Developments and Main Challenges.” FSI Insights No. 63, BIS, December.

CrowdStrike. 2026. “Global Threat Report: The Evasive Adversary Wields AI.” https://www.crowdstrike.com/en-us/global-threat-report/

Federal Reserve Board. 2025. “Cybersecurity and Financial System Resilience Report.” Report to Congress. Board of Governors of the Federal Reserve System, July.

Financial Stability Board (FSB). 2023. FSB Cyber Lexicon. Basel: FSB.

Financial Stability Board (FSB). 2024. “The Financial Stability Implications of Artificial Intelligence.” Report to the G20. FSB, Basel, November.

Financial Stability Board (FSB). 2025a. “Format for Incident Reporting Exchange (FIRE).” Final Report. FSB, Basel, April.

Financial Stability Board (FSB). 2025b. “Monitoring Adoption of Artificial Intelligence and Related Vulnerabilities in the Financial Sector.” FSB, Basel, October.

FS-ISAC. 2025. “Navigating Cyber 2025: Heightened Cyber Threats Are Testing the Operational Resilience of the Financial Sector.” Financial Services Information Sharing and Analysis Center, May.

Gaidosch, Tamas. 2018. “The Industrialization of Cybercrime.” Finance & Development 55 (2): 64. https://www.elibrary.imf.org/view/journals/022/0055/002/article-A008-en.xml

Gaidosch, Tamas, Emran Islam, Tanai Khiaonarong, Rangachary Ravikumar, and Christopher Wilson. 2026. "Good Practices in Cyber Risk Regulation and Supervision." IMF Departmental Paper 2026/001, International Monetary Fund.

Georgieva, Kristalina. 2026. “IMF Chief Warns Global Monetary System Not Ready for AI Cyber Threats.” CBS News Face the Nation, April 12.

International Monetary Fund (IMF). 2023. “Generative Artificial Intelligence in Finance: Risk Considerations.” Fintech Note 2023/006, International Monetary Fund.

International Monetary Fund (IMF). 2024. “Cybersecurity Risk: A Growing Threat to Macro-financial Stability” (Chapter 2). In Global Financial Stability Report. International Monetary Fund, April.

International Organization of Securities Commissions (IOSCO). 2025. “Artificial Intelligence in Capital Markets: Use Cases, Risks, and Challenges.” Consultation Report CR/01/2025, March.

Kashyap, Anil K., and Anne Wetherilt. 2019. “Some Principles for Regulating Cyber Risk.” AEA Papers and Proceedings 109 (May): 482–87.

Kopp, Emanuel, Lincoln Kaffenberger, and Christopher Wilson. 2017. “Cyber Risk, Market Failures, and Financial Stability.” IMF Working Paper 2017/185, International Monetary Fund, Washington, DC.

Kovacevic, Ana V., Sonja D. Radenkovic, and Dragana Nikolic. 2024. “Artificial Intelligence and Cybersecurity in Banking Sector: Opportunities and Risks.” arXiv:2412.04495, November.

Lee, Michael Junho, and Rinku Sinha. 2025. “Data Security, AI, and Infrastructure: Examining Cyber Risk in the Financial System.” Federal Reserve Bank of New York, The Teller Window, August 13.

Leitner, Georg, Jaspal Singh, Anton van der Kraaij, and Balázs Zsámboki. 2024. “The Rise of Artificial Intelligence: Benefits and Risks for Financial Stability. Financial Stability Review.” European Central Bank, May.

Lim, Xiang-Li, Puja Singh, and Richard Stobo. 2025. “Regulatory Considerations Regarding Accelerated Use of AI in Securities Markets.” IMF Technical Notes and Manuals No. 2025/016, International Monetary Fund, Washington, DC, December 24.

Mandiant. 2026. “AI Risk and Resilience: A Mandiant Special Report.” Google Cloud, March 9. https://cloud.google.com/security/resources/ai-risk-and-resilience

Munirathnam, Shekar. 2026. "Evaluation of Generative AI-Enabled Cyber Attack Vectors." International Journal of Computer Applications 187 (88): 44–50.

Niemann, Pat. 2025. “Cyber and AI Oversight Disclosures: What Companies Shared in 2025.” Harvard Law School Forum on Corporate Governance, October 28. https://corpgov.law.harvard.edu/2025/10/28/cyber-and-ai-oversight-disclosures-what-companies-shared-in-2025/

World Economic Forum. 2026. “Anthropic’s Mythos Moment: How Frontier AI is Redefining Cybersecurity.” April 20.

![](images/683d8ade2d3912a66e819972633a5a13ae1de010a9500b7c0138e3a76d7dc882.jpg)
"""
