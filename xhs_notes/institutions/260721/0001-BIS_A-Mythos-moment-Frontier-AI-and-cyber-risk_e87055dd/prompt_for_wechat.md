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
- 已识别机构名：`国际清算银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份国际清算银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## BIS Bulletin

## No 129

# A Mythos moment? Frontier AI and cyber risk

Iñaki Aldasoro, Raphael Auer, Jon Frost, Fernando Pérez-Cruz

July 2026

BIS Bulletins are written by staff members of the Bank for International Settlements, and from time to time by other economists, and are published by the Bank. The papers are on subjects of topical interest and are technical in character. The views expressed in this publication are those of the authors and do not necessarily reflect the views of the BIS or its member central banks. The authors thank Pablo Hernández de Cos, Byeungchun Kwon, Ulf Lewrick, Randy Miskanic, Vasily Pozdyshev, Kumar Rishabh, Vatsala Shreeti, Andras Valko and Leanne Zhang for helpful comments and suggestions, and Rudraksh Kansal, Byeungchun Kwon and Vivekananda Allam for excellent statistical assistance. They thank Nicola Faessler for administrative support.

The editors of the BIS Bulletin series are Gaston Gelos and Frank Smets.

This publication is available on the BIS website (www.bis.org).

ISSN: 2708-0420 (online)
ISBN: 978-92-9259-970-6 (online)

# A Mythos moment? Frontier AI and cyber risk

## Key takeaways

\- Frontier artificial intelligence (AI) models increase the speed, scale and complexity of cyber attacks, and they also strengthen cyber defence. But the costs are asymmetric and may favour attackers.

\- The medium-term impact on systemic cyber risk depends on the various actors' access to the most advanced tools, on compute power to run the tools and on economic incentives.

\- Given the pace of recent developments, swift adoption of frontier AI models to review code bases and fix vulnerabilities is essential. International coordination can support authorities in addressing these issues.

Among the most notable capabilities of frontier artificial intelligence (AI) models is their capacity to find vulnerabilities in software and hardware systems. Anthropic's Mythos, announced on 7 April 2026 and released only to select partners, is a case in point (Carlini et al (2026)). Mythos – and soon thereafter other frontier AI models, such as OpenAI's GPT-5.5 – is able to not only identify cyber vulnerabilities but also develop exploits to take advantage of them, and to autonomously carry out sophisticated multi-step, multi-vulnerability cyber attacks. Does this represent a "Mythos moment" – a wake-up call that requires a fundamental reconsideration of views on the robustness and resilience of financial market infrastructures?

The financial system is an obvious place of concern for information technology vulnerabilities. Banks, payment systems and other market infrastructures are among the most heavily targeted and most densely interconnected parts of the economy. They depend on long, complex chains of proprietary and open source software as well as third-party suppliers. A step change in attackers' capabilities could therefore have consequences that extend well beyond any single institution and bear directly on financial stability.

This Bulletin sets out potential channels through which frontier AI models can affect cyber security risk at scale. It discusses the impact of new tools on the capabilities and incentives of both attackers and defenders and draws on available data. Finally, it discusses potential public policy responses to support financial stability.

## Performance of frontier AI models on cyber security tasks

Frontier AI models have significantly advanced cyber offensive capabilities. For instance, recent evaluations by the UK government's AI Security Institute (AISI) suggest that frontier models are improving cyber-relevant offensive tasks. AISI tests models on a suite of 95 narrow cyber tasks across four difficulty tiers in a “capture-the-flag” benchmark setting, in which a model must find and exploit a deliberately planted vulnerability to retrieve a hidden token. Mythos achieved a 68.6% pass rate for expert-level tasks – higher than any model before (AISI (2026a); Folkerts et al (2026)). Yet these capabilities do not appear to be unique to Mythos. OpenAI’s GPT-5.5, released just weeks after Mythos, performed even better, with a 71.4% pass rate (Graph 1.A; AISI (2026b)). Moreover, in a cyber range, ie long multi-step attack simulations, both Mythos and GPT-5.5 were able to achieve a full network takeover in some attempts (Graph 1.B).

Cyber offence is unusually well suited for frontier AI tools. Unlike many tasks in which an AI system must navigate open-ended ambiguity, an attack unfolds as a structured, sequential workflow, codified in widely used industry frameworks (Hutchins et al (2011); Strom et al (2020)). Each stage generates machine-readable outputs (system logs, error messages, code, catalogued vulnerabilities) that a model can parse, reason over and act upon, with the success or failure of one step furnishing immediate feedback for the next. These tight feedback loops, comparatively rare in less structured domains, are precisely the conditions under which such models learn and improve most rapidly. The inflection point, which Mythos was the first model to reach, arrives not when a model can identify a single exploit, but when it can reliably link steps and adapt them to targets with limited human oversight. Encouragingly, the same properties operate in reverse: defenders can apply identical reasoning to anticipate, detect and remediate intrusions, so advances in model capabilities need not accrue to attackers alone.

## Frontier AI models show impressive cyber capabilities

![](images/b778bfe935b0cedfc2c98a5614e01d2233b48be845d1ce0fc4c027c68851acc8.jpg)

Graph 1

B. Mythos was the first model to complete all steps in a cyber range, and GPT-5.5 showed similar performance $^{3}$  
![](images/ae44c3971285eb0b344012c554884638f74d53a802ce288e5246c02f792b81e0.jpg)  
$^{1}$ Measured pass rate (y-axis) of selected models on an advanced capture-the-flag challenge with a 50 million token budget, by date (x-axis). $^{2}$ GPT-5, Claude Sonnet 4.5, Codex 5.2, Claude Opus 4.6, Codex 5.3, GPT-5.4, GPT-5.4 Cyber, Opus-4.7. Dashed lines are a least-square fit for the expert and practitioner tasks, respectively $^{3}$ Mean number of steps completed in the 32-step corporate network attack simulation "The Last Ones", over 10 attempts, with a 100 million token budget per attempt. "M3", "M5", etc refer to selected milestones in the attack chain. The dashed lines represent the outcome of the best attempt (ie a full network takeover succeeded).  
Source: AI Security Institute (2026b).

There are costs to mounting such an attack, but they are not prohibitive. A full attack chain consumes approximately 100 million tokens (a unit of input or output data). At current cloud prices, running such an attack on Claude Mythos Preview would cost some \$5,000–\$10,000, depending on the balance between input tokens (the code and data supplied to the model) and the more expensive output and reasoning tokens used to plan and execute it. Other frontier models such as Claude Opus 4.8, Gemini 3.5 and GPT 5.5 would cost about a fifth as much, and cheaper models such as Grok or DeepSeek can cost as little as \$50–\$100 per attack. As these costs fall, it becomes easier for less sophisticated actors to mount attacks.

These developments have renewed public concern and policy discussions around cyber risk. Supervisors and banks have aired these concerns publicly: some central banks are reported to have questioned banks about their exposure to new models, and senior bank executives have described them as a serious threat while warning that more threats will follow (see eg Canepa (2026)).

## Incentives of attackers and defenders

Whether frontier AI tools raise or lower systemic cyber risk depends on who gains access to them and the economic incentives they face. Cyber attackers are a heterogeneous group. State and state-sponsored actors pursue espionage, disruption (eg cyber warfare) or strategic advantage. Organised criminal groups seek financial gain, eg through ransomware and fraud. Firms may engage in industrial espionage. And individuals act for profit, notoriety or ideology. Alongside this sits a black market in which zero-day vulnerabilities (ie hidden flaws or bugs in a system that are unknown to the developer), stolen credentials and ready-made hacking tools are traded. At the same time, a sizeable and entirely legal market exists for cyber security and vulnerability discovery. In this latter market, firms seeking to defend themselves run bug bounty programmes that pay researchers to find and disclose flaws so that they can be fixed. $^{1}$

Frontier AI models are being adopted by both attackers and defenders. These models can lower the cost of finding and exploiting vulnerabilities for attackers but can also help defenders discover and fix them. $^{2}$ The economic costs are, nonetheless, asymmetric: a defender must protect every system continuously, whereas an attacker needs only one viable route in. Tools that cut the cost to find and exploit that route can therefore shift the balance towards offence even when both sides adopt frontier AI models at the same pace. Market intelligence also suggests that cyber defence strategies may increasingly imply larger costs for compute, given the need to detect and respond to (cheaper and more frequent) attacks.

The cyber defence response is already visible in the data. The release of ever more capable AI tools has coincided with a marked increase in security bug fixes. For example, monthly bug fixes by Firefox jumped sixfold after the announcement of Mythos Preview (Graph 2.A). It is an open question whether the pace of fixes will remain structurally higher or will fall again as bugs are found and remedied. This will depend on the capacity of new models to find new bugs or alternatives for attacks.

More generally, the pace at which new vulnerabilities are discovered and catalogued has been rising steadily for years and is now accelerating. This fits a longer-run pattern in the development of cyber tools. The number of critical common vulnerabilities and exposures (CVEs) published has been rising each year (Graph 2.B). $^{3}$ A CVE is an identifier for each vulnerability discovered in a software system; each is assigned a Common Vulnerability Scoring System (CVSS) score that indicates its severity. A score climbs toward 10 when a flaw is easy to exploit, requires no special access and would cause severe damage, such as allowing full remote control of a machine. CVEs with a CVSS score of nine or higher are deemed critical. The number of critical CVEs reported has risen from about seven per day over 2018–21 to 10 per day in 2022–25, to almost 20 per day after 1 April 2026.

Broadly speaking, data on CVEs fall into three distinct periods, each coinciding with a wave of AI-assisted coding tools. Between the first two periods (2018–21, 2022–25), the discrete jump in the number of CVEs may relate to the availability of GitHub Copilot (released in June 2021) or OpenAI's GPT application programming interface (API) (first available in June 2020). $^{4}$ Over 2022–25, the annual count was broadly stable, as developers became accustomed to coding-assistant tools. The jump in reported CVEs in the second quarter of 2026 may relate to Mythos and other models for coding becoming available. But these counts should be interpreted with care: the number of published CVEs also reflects the growing size and reach of the software industry and the size of the security research community, not AI capabilities alone.

## Security bug fixes and capabilities to identify vulnerabilities are growing

![](images/517af3bc3c95ee2d68af6b10be6355302cb7e942488d38d5ec12eada185a2cef.jpg)  
CVEs = common vulnerabilities and exposures

B. Mean of daily critical CVEs (CVSS >= 9.0) reported was stable in 2022–25, but jumped up in 2026 $^{4}$  
![](images/58f500e246b4d602ea9c8fae4e227dcc977ee90a0bc191773d58e604aebf63c2.jpg)  
$^{1}$ Firefox security bug fixes by month (all sources, all severities). $^{2}$ Mean of daily critical CVEs (ie those with a Common Vulnerability Scoring System (CVSS) score > = 9.0) per calendar year.  
Sources: NIST National Vulnerability Database API (accessed 18 May 2026), BIS calculations.

Reported data breaches have risen in step and a growing share are fully automated. By a global estimate, 2025 recorded a significant jump (Graph 3.A), and breaches attributed to automated rather than human action became more common. These data are incomplete, however, and tend to reveal more about the type of incident than about the specific tools used, not least because attackers do not self-report.

## Data breaches have been rising; since Mythos, market expectations have shifted

![](images/6cb008cd6cd6eb582fa497b1b5961a309bcea19ba845a77dad7c8b4d9c66298f.jpg)  
$^{1}$ Based on global data breaches collected from domestic and international law enforcement, forensic firms, law firms, cyber insurers, cyber security industry sharing groups and the Verizon Threat Research Advisory Center caseload. $^{2}$ Cumulative abnormal returns (CARs) are computed from a market model regression of each stock's daily log returns on Nasdaq 100 log returns, estimated over 2 December 2025 to 20 March 2026 (ie preceding the initial leak of information about Mythos). Abnormal returns are the residuals from this model evaluated over the event window; CARs are daily and are normalised to zero on 6 April 2026, so values from 7 April onwards measure cumulative abnormal performance since the eve of the announcement. "Glasswing partners" refers to selected known companies that were granted access to Mythos (Crowd Strike (CRWD) and Palo Alto (PANW)).

Sources: Verizon; LSEG Datastream.

Market reactions provide a complementary, forward-looking signal. The cumulative abnormal stock returns of a number of cyber security firms fell sharply with the announcement of Mythos (Graph 3.B). This was widely interpreted as a reflection of investor concerns about obsolescence of existing cyber security products and services. $^{5}$ This is a notable reaction, given that a more dangerous threat environment might instead be expected to raise demand for such products.

## Potential public policy responses

The rapid evolution of AI-driven cyber attack capabilities calls for coordinated public policy responses. The private return to finding and disclosing a vulnerability may be smaller than its system-wide benefit, especially when many institutions share the same code or supplier. Firms may therefore underinvest in discovery and disclosure. This externality provides a direct rationale for coordinated scanning and information-sharing. In both the short and medium term, domestic and international coordination can mitigate risks to critical infrastructure and sustain trust in the stability of the financial system.

An initial safeguard is domestic cooperation, not least to ensure that defenders gain access to frontier models before attackers. The financial industry, central banks and financial supervisors can collaborate with national security agencies and other stakeholders to accelerate vulnerability remediation, strengthen core cyber hygiene practices and address exposures from in-house software dependencies, legacy systems, open source code, third parties and internet-facing assets. The same tools that lower costs for attackers can be used defensively, to find and fix flaws in firms' own systems before others do. Engaging critical suppliers, including cloud providers, and updating exercises to simulate third-party software compromises and compressed attacker timelines are also important.

Given the global nature of the risks involved and the interconnected nature of the global financial system, cross-border information-sharing is indispensable. Of course, there can be geopolitical constraints to cooperation in some areas, eg threat intelligence. Still, global forums can build on existing operational resilience frameworks, such as the Principles for Operational Resilience and Effective Practices for Cyber Incident Response and Recovery (FSB (2020, 2021)), or discuss AI-related operational risks reflected in risk identification, scenario analysis and resilience planning (BCBS (2021)). For financial market infrastructures, AI-driven threats can be mapped across the pillars to identify, protect, detect, respond and recover in the CPMI–IOSCO cyber resilience guidance (CPMI–IOSCO (2016)). The G7 (2026) already made a commitment to enhance information-sharing and identify best practices. It has also undertaken to reinforce the preparedness of the financial sector and to map the cyber security risks related to AI models. The cyber security agencies of the Five Eyes (2026) have also urged leaders to reduce attack surfaces and accelerate patching processes.

In the medium term, resilience frameworks must adapt to the evolving threat environment shaped by AI. Regulators and standard-setting bodies can translate existing principles into practical toolkits for extreme scenario design, such as AI-enabled attack paths, and update them as threats evolve. Strengthened oversight of third-party and supply-chain risk is increasingly important as digital dependencies deepen. Operators of systemic infrastructures could be encouraged to participate in pretesting of new AI models, while volunteer pilots and shared assessments can accelerate collective learning. Demand for capacity building is likely to rise; $^{6}$ international initiatives can prototype AI-enhanced resilience tools and support jurisdictions with varying resources. Information-sharing arrangements may need recalibration to improve timeliness, reciprocity and legal protections, supported by interoperable taxonomies and secure channels.

The stakes for the financial system are especially high. Payment, trading and post-trade platforms operate at a very large scale and are tightly interconnected with billions of firms and individuals. Complex software stacks and intricate supply chains complicate patching and monitoring, and disruptions can be hard to detect and unwind. These same infrastructures are an attractive target for actors seeking to inflict large-scale economic damage. By learning, adapting and communicating effectively, authorities and the financial industry can turn this pivotal moment into durable gains in global cyber resilience.

## References

AI Security Institute (AISI) (2026a): "Our evaluation of Claude Mythos Preview's cyber capabilities," 13 April. —— (2026b): "Our evaluation of OpenAI's GPT-5.5 cyber capabilities", 30 April.

Aldasoro, I, S Doerr, L Gambacorta, S Notra, T Oliviero and D Whyte (2024): "Generative artificial intelligence and cyber security in central banking", BIS Papers, no 145.

Aldasoro, I, L Gambacorta, A Korinek, V Shreeti and M Stein (2025): "Intelligent financial system: how AI is transforming finance", Journal of Financial Stability, vol 81, 101472.

Basel Committee on Banking Supervision (BCBS) (2021): Principles for operational resilience.

Canepa, F (2026): "ECB to quiz bankers about risks of Anthropic's new AI model, source says", Reuters, 15 April.

Carlini, N, N Cheng, K Lucas, M Moore, M Nasr, V Prabhushankar, W Xiao et al (2026): "Assessing Claude Mythos Preview's cybersecurity capabilities", Anthropic, 7 April.

Committee on Payments and Market Infrastructures–International Organization of Securities Commissions (CPMI–IOSCO) (2016): "Guidance on cyber resilience for financial market infrastructures", CPMI Papers, no 146.

Financial Stability Board (FSB) (2020): Effective practices for cyber incident response and recovery.

(2021): "Principles for operational resilience", Compendium of Standards.

Five Eyes (2026): "Five Eyes cyber security agencies statement", 22 June.

Folkerts, L, W Payne, S Inman, P Giavridis, J Skinner, S Deverett, J Aung, E Zorer, M Schmatz, M Ghanem, J Wilkinson, A Steer, V Hong and J Wang (2026): "Measuring AI agents' progress on multi-step cyber attack scenarios", arXiv, 10.48550/arXiv.2603.11214.

G7 (2026): "G7 Finance Ministers' and Central Bank Governors' Communiqué", 19 May.

Hutchins, E, M Cloppert and R Amin (2011): "Intelligence-driven computer network defense informed by analysis of adversary campaigns and intrusion kill chains", in J Ryan (ed), Leading issues in information warfare and security research, vol 1. Potter, Y, W Guo, Z Wang, T Shi, H Li, A Zhang, P G Kelley, K Thomas and D Song (2025): "Frontier AI's impact on the cybersecurity landscape", arXiv, 10.48550/arXiv.2504.05408.

Rishabh, K, R Mihet and J Jang-Jaccard (2026): "Cyberrisk and AI Firms", Review of Corporate Finance Studies, cfag018.

Strom, B, A Applebaum, D Miller, K Nickels, A Pennington and C Thomas (2020): "MITRE ATT&CK: design and philosophy", MITRE Corporation technical report, no MP180360R1.
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
