你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
# Spring Series 2026

A Good Start with AI Tailwinds Ahead

Overweight: CLBT, CHKP, CRWD, ESTC, FROG, NTSK, OKTA, PANW, SAIL, TENB, VRNS, ZS

Neutral: GTLB, IBM, RPD, S

Underweight: AI, FTNT, QLYS

Software - Large Cap / Mid & Small Cap 

<table><tr><td>Brian Essex, CFA AC</td><td>John Lee</td><td>Alex Isaac</td></tr><tr><td>(1-212) 622-5990</td><td>(1-212) 622-6064</td><td>(1-212) 622-9159</td></tr><tr><td>brian.essex@jpmchase.com</td><td>john.h.lee@jpmchase.com</td><td>alex.isaac@JPM.com</td></tr><tr><td>JPM Securities LLC</td><td>JPM Securities LLC</td><td>JPM Securities LLC</td></tr></table>

# Executive Summary: Demand Poised to Accelerate

The most transformative technology shift of our lifetimes comes with a larger attack surface

The attack surface is evolving and expanding at an unprecedented pace: Agents can now find vulnerabilities in code at an unprecedented rate. This translates into an ability to engineer and execute exploits at a much faster rate. Exploits that AI models engineer can also be more complex and sophisticated. Meanwhile, some applications may not be patchable and AI introduces new attack vectors including logic, identity, and social engineering-based exploits.

Platforms are best positioned to address emerging AI threats: The enterprise remediation gap cannot keep pace with the speed of AI-enabled discovery. Mean time to exploit has collapsed. Platform vendors have already been leveraging access to AI with decades of domain expertise, proprietary data, and deep telemetry across Endpoint, Network, Identity, and Data estates to help protect customers.

Partnerships offer a lens into leadership: Anthropic's Glasswing, OpenAI's Trusted Access for Cyber, and CrowdStrike's Quiltworks illustrate the critical role security platforms will have to address the incremental threats foundation models introduce. Those leading the partnerships with insight from foundation model vendors have an evolutionary competitive advantage.

- Anthropic has restricted Mythos access to 52 vetted organizations for defensive use only, backed by \$100M in resources. The White House Office of Management and Budget is establishing guardrails for federal agency access.   
- OpenAI Daybreak and TAC more open than Anthropic's coalition, scaling toward automated verification rather than a curated partner list.   
- CrowdStrike Quiltworks is a coalition that includes Anthropic and OpenAI, GSIs and other partners focused on finding and mitigating vulnerabilities found in enterprise applications and networks.

CRWD and PANW are obvious beneficiaries but others also well positioned: CRWD and PANW have been the most promotional about their partner-led efforts but others within our coverage have been actively involved with the foundation model companies and some may be limited by agreements they have. We count CHKP, ZS, NTSK, FROG and S among them.

# Fast Followers Behind Mythos

Open-source model capabilities are also approaching levels that may outpace remediation capacity

Frontier AI models have reached autonomous offensive cybersecurity capability: Anthropic's Mythos Preview autonomously discovers zero-day vulnerabilities, develops working exploits, and completes full network penetration tests without human intervention.

"I found more bugs in the last couple of weeks than I found in the rest of my life combined." – Nicholas Carlini, Research Scientist, Anthropic

"I just spoke to one of our partners (re: Quiltworks) and 48 million vulnerabilities were found." – George Kurtz, CEO, CrowdStrike

This capability has already been used in real-world attacks: In September 2025, a Chinese state-sponsored group used less capable Claude models to autonomously conduct cyber espionage against approximately 30 entities including government agencies and financial institutions, with confirmed successful intrusions.

Underlying capabilities are proliferating through open-source models: Kimi K2.6, an open-source Chinese model released by a company caught siphoning Anthropic training data, now matches the coding performance level at which real-world exploit capability was demonstrated. Multiple other models are approaching the same threshold. Anthropic's own offensive cyber lead estimates broad availability within months, not years.

Autonomous defensive tools are becoming a necessary component of enterprise security: The speed of AI-enabled threats is outpacing what human-operated security teams can address. Industry leaders including CrowdStrike, Palo Alto Networks, and SentinelOne have already begun deploying autonomous defensive agents in production. The long-term outcome, if discovery is paired with accelerated remediation, could be more secure infrastructure.

Security budgets can account for over 10% of total IT spend $^{1}$ : If we apply the same proportion to expected AI infrastructure, services and software spending, we expect spending directed at AI systems could easily run into the billions of dollars with well positioned platform vendors.

# The Threat Landscape Was Accelerating

Cyber threats were compounding in volume, speed, and sophistication before latest frontier AI capabilities

Common Vulnerabilities and Exposures Reported by Quarter   
![](images/90ed7be7716c4402c067c4a8db0abcbf3175790fad06e4c2d62740c3d954d6c5.jpg)  
Source: MITRE cvelistV5   
Vulnerability disclosure volumes are compounding year over year, expanding the attack surface for defenders to monitor

Breakout time collapsing: Time from initial access to lateral movement now measured in minutes, compressing the window for detection and response.

Time-to-exploit has turned negative: Mean time-to-exploit is now negative 7 days, meaning adversaries are exploiting vulnerabilities before patches exist. Historical compression: 63 days (2018) to 32 days (2021) to 5 days (2023) to negative 7 days (2025). 29% of known exploited vulnerabilities were weaponized on or before the day of public disclosure.

Nation-state AI operations are scaling rapidly: Russia's FANCY BEAR has deployed malware that uses LLM APIs to dynamically generate reconnaissance commands, replacing human operators entirely. DPRK activity surged 130%, with operatives using AI for real-time deepfake video interviews in hiring fraud targeting financial institutions.

Complacency is a legacy issue: The 2007 Aurora Generator Test demonstrated cyberattacks could physically destroy critical infrastructure. The pace of defensive improvement has not matched threat acceleration.

Documented AI-orchestrated cyberattack (September 2025): A Chinese state-sponsored group used Claude Code to autonomously conduct cyber espionage against \~30 entities including government agencies, financial institutions, and major technology firms. AI performed 80-90% of tactical operations independently at rates physically impossible for human operators. A handful of high-value intrusions were confirmed successful, achieved using models less capable than currently publicly available as open-source.

# Agentic AI Is Expanding The Attack Surface

AI deployment introduces new vectors that didn't exist in the pre-AI enterprise

# Prompt Injection

Adversaries craft malicious inputs, directly or hidden in external data, to hijack LLM behavior, bypass safety controls, or exfiltrate data

![](images/687d8f45bb830dfdd7d2435b094b6f093c51fcb4415d8193fc42aa8ff43d77fd.jpg)

# Data & Model Poisoning

Attackers corrupt training data or model weights to embed backdoors, bias outputs, or degrade model integrity, often months before deployment

![](images/4c2e64b7a6ca4876060f4c9d833b9507b00c0814c0f35ad9918f9853fb6966f0.jpg)

# AI Supply Chain Compromise

Malicious third-party models, open-source packages, compromised plugins, and MCP servers introduce hidden threats

![](images/166f99950ac7e335ac33cc0611e9804d54c256ba63fa67adbf14acf69bb77598.jpg)

# Excessive Agent Authority

Agents granted overly-broad permissions can be tricked into executing unauthorized actions deleting data, sending funds, or escalating privileges

![](images/8263229866f43cd9a3f3a2210cfdafea6d0514422c13f1cd1d5267ce4c5c70bd.jpg)

# Shadow AI

Employees deploy
unsanctioned AI and agents
outside IT visibility, creating
data flows and unmanaged
endpoints.

![](images/151ab22451f41c0f83344b0ad97d1ba87f8a2d427f03208450b4bd6e40aa1dc5.jpg)

# AI-Generated Code Vulnerabilities

AI coding assistants produce insecure or exploitable code at production scale, and developers often trust it without adequate review.

![](images/bb406fce080238357915437b17c56cf5af6a55f655bea4e62718ed4e3d899625.jpg)

# Sensitive Data Exposure

LLMs leak PII, system prompts, proprietary data, or training-set contents through outputs, memory features, or retrieval pipelines.

![](images/19fc3d332f6e8c5a213b8f6f287fdd0a3941d6e048b27143d90d3f333dbaf2d1.jpg)

# Deepfakes & Synthetic Identity

AI-generated voice, video, and synthetic identities enable high-fidelity impersonation that bypasses identity verification

![](images/f2bd0fc5ed5d0de5a4cab1b4e1101831d1ab8ccc5596c659dd5e4cdbc445c519.jpg)

# Non-Human Identity Sprawl

AI agents create a surge of machine identities that operate continuously without human oversight, creating persistent and ungoverned access paths.

![](images/b1ce8cde72d0db630cefd456ee993e0e4f52bbb077c42056a563df2bc850e529.jpg)

AI adoption is expanding the enterprise attack surface at an unprecedented pace, introducing entirely new vulnerability classes from prompt injection to agentic identity sprawl. The challenge stems from these surfaces are not yet being attacked by serious adversaries at scale, creating a security risk overhang where the surface grows faster than defenders can empirically prioritize it. Organizations need dialable controls that are lightweight today but can be tightened as real threats materialize.

# Economics of AI-Enabled Vulnerability Discovery

Cost collapse and autonomous operation make offensive capability broadly accessible

Autonomous operation: Anthropic disclosed that “engineers with no formal security training instructed [Mythos] to find attacks that give full remote access overnight and had complete, working attack tools by morning.” The model develops working attack tools end-to-end without human steering.

Speed compression: A corporate network penetration simulation estimated to take a human expert 10+ hours was completed autonomously by the model. Multi-step attack chains that required weeks of expert iteration now execute in hours.

Constraint shift: The threat landscape is no longer gated by attacker skill, only by access to the models, which now surpass all but the most skilled humans.

Commodity orchestration: Real-world attacks have already demonstrated that standard open-source security tools orchestrated by AI can replace entire teams of experienced hackers, with no custom malware or advanced exploit development required. The barrier to sophisticated offensive operations is no longer technical skill; instead, it is access to a capable model and harness.

<table><tr><td>Attack Type</td><td>AI Cost</td><td>Legacy</td></tr><tr><td>Scan an entire operating system for security flaws</td><td>&lt;$50</td><td>Expert Team, weeks</td></tr><tr><td>Develop a complete attack that gains full control of a computer</td><td>&lt;$1K over half a day</td><td>$500K-$2mm on the exploit black market</td></tr><tr><td>Run 1,000 automated security scans</td><td>&lt;$20K</td><td>Dedicated Research Teams</td></tr></table>

500-1,000x cost reduction makes offensive capability accessible to any organization with model access and compute.

Average eCrime breakout time: 29 minutes (fastest recorded: 27 seconds); Ransomware-to-data-exfiltration: 22 seconds (down from 8+ hours, 2022) - CrowdStrike 2026 Global Threat Report

Threat actors can now use agentic AI systems to do the work of entire teams of experienced hackers. - Anthropic threat intelligence disclosure, 2026

# Mythos Represents a Step Change in Autonomous Cybersecurity

Standardized benchmarks and real-world discoveries confirm performance beyond existing security tools and previous AI models

![](images/9638bfc667ac761960d66e4876ecd3842a48f6f5ce885e475b783a9b6b862d14.jpg)

<details>
<summary>bar</summary>

Advanced Software Problem Solving (SWE-bench Pro)
| Software Name | Percentage (%) |
| :--- | :--- |
| Mythos Preview (Restricted) | 77.8 |
| GPT-5.5 | 58.6 |
| Claude Opus 4.7 | 64.3 |
| Claude Opus 4.6 | 53.4 |
| GLM-5.1 (Open-Source, China) | 58.4 |
| Kimi K2.6 (Open-Source, China) | 58.6 |
| Gemini 3.1 Pro | 54.2 |
</details>

![](images/7c48abb5d51826f67104cf3dfc427876fef7d6fc1731ef11edc9c19d5744a0fd.jpg)

<details>
<summary>bar</summary>

| Model | Ability to Find & Reproduce Security Vulnerabilities (CyberGym) |
| --- | --- |
| Mythos Preview (Restricted) | 83.1% |
| GPT-5.5 | 81.8% |
| Claude Opus 4.7 | 73.1% |
| Claude Opus 4.6 | 73.8% |
| GLM-5.1 (Open-Source, China) | 68.7% |
| Kimi K2.6 (Open-Source, China) | Untested |
| Gemini 3.1 Pro | 38.8% |
</details>

Source: Hugging Face

Mythos outperforms all publicly available models across every security and coding benchmark tested

Existing security tools alone are insufficient: Mythos discovered critical vulnerabilities that survived decades of automated testing. Current industry-standard scanning does not provide adequate protection against AI-capable adversaries.

Current access constraints are temporary: Mythos is significantly larger than Opus 4.6 with enterprise-class pricing, limiting broad deployment today. Both cost and compute are expected to decline as future models gain efficiency. These constraints slow proliferation but do not prevent it.

# Discovery and exploitation are no longer separate

capabilities: Mythos does not simply identify vulnerabilities; it autonomously develops complete working attacks. The model collapses what previously required two different, expensive skillsets into a single automated process.

Anthropic deliberately reduced cyber capability in its public release: Opus 4.7 scores lower on cybersecurity despite scoring higher on coding. Anthropic actively decoupled the two capabilities for its public model. Open-source models don't have these constraints.

Current benchmarks cannot measure the upper bound: Mythos scores 100% on some of the most difficult cybersecurity evaluation available. Real-world results (27-year, 17-year, and 16-year undetected flaws) confirm performance beyond what benchmarks capture.

# Mythos Represents a Step Change in Autonomous Cybersecurity

Completed steps on "The Last Ones" per spent tokens   
AISI | AI SECURITY INSTITUTE   
![](images/f43e32bc78b7dfef16886575158682eff7fc53f6051c6b137909b02e4199c475.jpg)

<details>
<summary>line</summary>

| Model | Cumulative Tokens (log) | Avg. steps Completed |
| --- | --- | --- |
| M9: Full network takeover | ~10k | ~32 |
| M8: Infrastructure compromise | ~10k | ~32 |
| M7: Advanced persistence | ~10k | ~32 |
| M6: C2 reverse engineering and crypto analysis | ~10k | ~32 |
| M5: Web app exploit and privilege escalation | ~10k | ~32 |
| M4: Wiki exploit and credential replay | ~10k | ~32 |
| M3: Browser credential theft | ~10k | ~32 |
| M2: Lateral movement and credential extraction | ~10k | ~32 |
| M1: Initial reconnaissance | ~10k | ~32 |
| Mythos Preview (new) (best attempt) | ~10M | ~25 |
| GPT-5.5-Cyber (best attempt) | ~10M | ~25 |
| GPT-5.5 (best) | ~10M | ~25 |
| Mythos Preview (early) (best attempt) | ~10M | ~25 |
| Claude Opus 4.6 (10×100M) | ~10M | ~25 |
| GPT-5.4 (10×100M) | ~10M | ~25 |
| Claude Opus 4.7 (10×100M) | ~10M | ~25 |
| Codex-5.3-Codex (5×100M) | ~10M | ~25 |
| Claude Opus 4.5 (5×100M) | ~10M | ~25 |
| GPT-5.1-Codex (5×100M) | ~10M | ~25 |
| Claude Sonnet 4.5 (5×100M) | ~10M | ~25 |
| Claude Sonnet 3.7 (10×10M) | ~10M | ~25 |
| GPT-4o (10×10M) | ~10M | ~25 |
</details>

Source: AISI

# Glasswing Limits Mythos Access to Vetted Defensive Partners

Controlled coalition for defensive cybersecurity

Project Glasswing is a controlled initiative launched by Anthropic on April 7, 2026 that gives select organizations access to Claude Mythos Preview exclusively for defensive cybersecurity purposes. Mythos is not a commercial product, has no public release timeline, and Glasswing is the only authorized channel for accessing its capabilities.

Defensive vulnerability scanning: Vetted coalition partners use Mythos to scan their own systems for security vulnerabilities that conventional tools cannot find.

Coordinated public disclosure: All vulnerabilities discovered are reported through a 90-day coordinated disclosure process, creating predictable patch requirements for the broader ecosystem.

Restricted by design: Anthropic determined the capabilities were too powerful to release broadly but too valuable to withhold entirely. The restricted coalition model allows defenders a head start before the underlying capability proliferates through competing models.

![](images/84684e0594d8516c57dc030467c93a7aea5d3c2c49bffd7a2befa615cff2006b.jpg)

<details>
<summary>text_image</summary>

aws
ANTHROP\C
BROADCOM
CISCO
CROWDSTRIKE
Google
JPMChase
THE
LINUX
FOUNDATION
Microsoft
NVIDIA
paloalto
NETWORKS
</details>

52 vetted organizations including 12 founding partners (CrowdStrike, Palo Alto Networks, AWS, Apple, Broadcom, Cisco, Google, JPM Chase, Linux Foundation, Microsoft, NVIDIA) plus 40+ additional organizations granted access.

\$100M in model usage credits distributed to coalition members for defensive scanning

US government moving toward access: White House OMB is establishing guardrails for federal agency use of Mythos. Anthropic confirmed discussions with the Trump administration.

Less than 1% of discovered vulnerabilities have been repaired to date: Mythos has found thousands of critical flaws across major operating systems, browsers, and infrastructure software. Remediation has barely begun. The disclosure pipeline will pressure enterprise patching capacity for months.

# Frontier Cybersecurity Capability Quickly Evolving

Open-source Chinese models already match coding levels with demonstrated cyber capability

Cybersecurity capability emerges naturally from coding ability: Improving a model's coding performance generally produces offensive security capability as a byproduct

An open-source model has already crossed the exploit threshold: Kimi K2.6 (Moonshot AI, open-source, Chinese) scores 80.2% on SWE-bench Verified, matching Opus 4.6 coding today. Opus 4.6 at that level demonstrated real cyber capability (66.6% CyberGym, Firefox exploits). Anthropic's offensive cyber lead estimates only months remain until competing systems reach Mythos-comparable 

[中间内容因长度限制已省略]

rial only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by

changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised April 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
