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
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`JPM`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
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
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JPM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# JPM

## Global Banks

## Mythos-class era: Cybersecurity a bigger concern than credit risk

Cybersecurity in Banks is currently one of the biggest undiscounted risks not reflected in Bank valuations in our view, partly due to the limited disclosure available which leads to a lack of comparability between banks on their preparedness or lack thereof to deal with emerging cybersecurity risk (pre-event and post-event processes), driven by advanced AI capabilities such as Frontier Models. While there is significant regulatory focus on capital ratios, we believe looking at cybersecurity risk through the lens of the capital framework is not the best approach. In our view, there should be an increased focus on cybersecurity driven liquidity risk and this should be tested through increased infrastructure resilience testing and through a deposit-run liquidity haircut test as we believe liquidity, not credit risk, could be the main trigger in a scenario of a potential banking crisis with social media likely to trigger unprecedented volatility in deposit flows as we witnessed at CS. In this changing environment, we are likely to see differentiation between players, based on: i.) Geopolitics - US players are likely at an advantage, having early access to the most sophisticated AI models, with the US being the epicenter of AI developments (e.g. Project Glasswing), followed by potentially China which also seems to be ahead of peers, while Rest of the World is likely at a disadvantage; ii.) Size and interconnectedness as G-SIB banks are likely to have early access to test out the latest developments compared to smaller banks. We also start to question whether, rather than focusing purely on earnings, we should look to assign a 1x higher multiple (i.e. lower implied CoE) for ‘sticky’ client deposit banks with material excess deposits, based on our view of their ability to manage through the next crisis scenario. We believe a degree of premium for US GSIBs (currently at avg. 12.5x P/E 2028E, BBG consensus) compared to their global counterparts (European Banks at 9x P/E 2028E and Japanese megabanks at 12x P/E 2028E) could be justified due to lower CoE as the market factors-in better cyber risk preparedness through higher absolute scalable tech spending and early access to latest frontier models.

Frontier models such as Mythos and GPT-5.5 significantly reduce the timeline for discovering previously unknown “Zero-day” vulnerabilities from months and years to hours. While these models highlight the exposure of all global banks to cyber risks, on a bottom-up basis the banks more exposed in our view would be those with old and multiple legacy infrastructure patched together and with ongoing underinvestments : i.) banks with legacy core banking systems which run on code that was written a few decades ago but do not show the necessary agility to fix identified vulnerabilities due to lack of resources or lack of infrastructure protocols; ii.) banks where core banking systems are vendor provided and the vendor does not show the necessary agility to release patches for identified vulnerabilities; iii.) banks with multiple legacy platforms, for example due to historical M&A, thus providing a bigger pool of potentially vulnerable points and iv.) banks which are not getting access to the latest developments in the field, leaving them potentially exposed to a “known threat” for a longer period of time than peers who have such access. As an external observer, it is difficult for us to differentiate between banks on this basis as: i) we do not have enough information around the IT main, back office infrastructure, middle office and external vendor reliance of individual banks and hence we look at IT spend as a barometer of banks

European Banks

Kian Abouhossein AC
(44-20) 7134-4575
kian.abouhossein@JPM.com

Amit Ranjan

(44-20) 7134-4576

amit.x.ranjan@JPM.com

JPM Securities plc

Specialist Sales contact details:

Gigi Sparling - Specialist Sales - European Financials

(44-20) 7134-0355

ghislaine.sparling@JPM.com

which at least have the resources to stay ahead of the curve and also fix these vulnerabilities as they arise. Based on Table 1, Tech costs averaged c.17% of Global Banks operating expenses in 2025 and while the definition of tech spend varies between players, making like-for-like comparison difficult, it provides a starting point for engaging in discussions with bank managements. As technology is scalable, we also focus on absolute spend, with US large cap banks well positioned with higher absolute spend on Tech compared to their global peers, while European banks generally operate with lower absolute tech budgets and face a delay in access to some of the latest developments, as evident, for example, in their absence from the April announcement on Project Glasswing by Anthropic.

Overall, we believe tech spend as well as cybersecurity specifically should be a bigger topic of discussion for Bank investors and managements, with a focus on developing a bottom-up understanding of the infrastructure that banks have. JPMC Chairman and CEO Jamie Dimon in his 2025 annual shareholder letter highlighted Cyber risk as one of the larger risks still in front of us that are multi-year and unresolved, “Cyber risk. I have to mention this because it remains one of our biggest risks, and this is probably true for many other major industries and corporations. AI will almost surely make this risk worse. We invest significantly to protect ourselves and stay vigilant.” Our current cost growth forecast of an average 1.8% p.a. over 2025-28E for European Banks could see upward pressure from increased need for tech investments; however, we would also expect cost savings from increased AI usage over time, thereby neutralising the impact to some extent. We also see the need for an increased pace of legislation to deal with cybersecurity issues as financial crime becomes increasingly sophisticated - not through bank regulatory capital or liquidity requirements, but back-testing of infrastructure and processes in the case of a cyber attack event.

We have previously discussed the impact of increased usage of digital money and the development of DeFi market as being the next frontier for Global Banks (see Global Banks: The Next Frontier: Future of Global Banking to be defined by Digital Money) and developments in the cybersecurity space are expected to impact the DeFi market as well. The increased use of Agentic AI in financial services is also bringing in new risks and further expanding the attack surface. While the possibility of using cold wallets offers a limited degree of protection, in an era of rapid developments in Quantum Computing, DeFi markets remain vulnerable to cyber attacks as well. However, the Ethereum Foundation indicates that, while quantum computers will eventually threaten the cryptography Ethereum uses today, it has a dedicated post-quantum research team, and a structured “Lean Ethereum” roadmap targeting 2029 for full post-quantum protection. Standards such as EIP-8141 for account signatures, quantum-resistant application layer Zero Knowledge proofs and lean consensus roadmap are part of the developments in some of the areas which Ethereum Foundation sees as vulnerable to quantum attack.

Ironically, while digital-first authentication is the trend, as cyberattacks become more sophisticated, especially those enabled by AI plus device compromise, there is a possibility that banks may re-emphasize physical possession factors (hard tokens/security keys) because they are generally more resistant to remote theft, phishing, and some forms of spoofing. However, if such a scenario does develop, banks would need to do a balancing act between convenience for customers, which is disrupted by the need to carry physical devices vs. the safety offered by such a move. We could potentially also see scenarios where circuit breakers are increasingly deployed, for example, to limit the chain reaction damage from a cybersecurity incident. We have seen banks in Singapore, for example, deploy cooling-off periods for selected digital bank transactions with the objective of providing a window to the impacted user to detect and report any suspicious activity relating to their account, such as adding a new transfer recipient. We also see the pace of roll-out of Agentic AI for external use by banks being slowed down as the growing attack surface provided by the agentic ecosystem with third-party linkages could lead to caution with frontier models

highlighting vulnerabilities.

Anthropic's Claude Mythos Preview (Mythos, released in April 2026) under controlled evaluation by various authorised agencies (such as AI Security Institute in the UK) has been reported to demonstrate significantly more advanced AI cyber capabilities than any other models. These evaluations have demonstrated that Mythos could autonomously discover and exploit vulnerabilities on exposed networks, executing multi-stage attacks, work that would typically take human professionals days to complete. Mythos is just one example of future AI capabilities, with other models such as GPT-5.5 also demonstrating similar levels of performance (see Figure 1) on cyber evaluations by agencies, and we would expect more sophisticated models to be developed over time, meaning banks and regulators would need to be dynamic in their approach to dealing with the evolving cybersecurity landscape. While projects like Glasswing also demonstrate the power of collaboration between firms and authorities to use these models to strengthen cyber defences, with restrictions on general availability of these models, we believe the speed at which vulnerabilities are discovered is increasing and the reaction time between the identification of vulnerabilities and their patching is getting compressed, which should continue to pose a challenge.

With an increase in cybersecurity related incidents, we believe cyber insurance will become increasingly relevant for banks to avoid situations like Jaguar Land Rover (JLR) which, based on press reports (Source: FT) had to shoulder the full bill from a damaging cyber attack in 2025 due to a lack of cyber insurance. Munich Re estimates that the global cyber insurance market premium totaled nearly US\$15bn in 2025 and Munich Re experts anticipate the global premium volume to expand to around US\$28bn by 2030, representing an average annual global growth rate of 15% between 2020 and 2030. We note that the Financial Services industry is amongst the biggest payers of cyber premiums globally and in an era of increased cybersecurity risk, we would expect regulators to be increasingly focused on cyber insurance protection availed by banks. In our view, regulators should also look to incorporate cyber risk insurance into the operational capital profile for banks to incentivise the purchase of appropriate protection through cyber insurance.

In our view, the advancement of AI-led cyber threats means it would be difficult to make a system 100% safe with vulnerabilities in codes more easily exploitable. However, cyber threats are “institutionalized” with measures such as ROI being used by cyberattackers to measure the potential return against the investment needed to execute a cyberattack, banks which make this ROI hurdle rate higher by making the necessary upfront investments would be better placed than peers. At the same time, the AI-led developments potentially lower the cost to carry out a sophisticated cyber attack for bad actors, and hence it would be interesting to see where the 2 curves of AI-led enhancements through patching of vulnerabilities and the ease of carrying out AI-led attacks intersect in the future.

## Step up in cyber performance in frontier models increases cybersecurity risks for Banks...

Frontier models are the most advanced AI models available at a given moment, trained on massive datasets to deliver state-of-the-art performance across many tasks, representing the leading edge of AI capability. They typically power advanced reasoning, image and text generation, and agentic workflows. (source: Nvidia) Both Mythos Preview and GPT-5.5 are examples of Frontier Models.

Anthropic's Claude Mythos Preview, disclosed in April 2026 is such a Frontier Model which according to the company revealed the fact that “AI models have reached a level of coding capability where they can surpass all but the most skilled humans at finding and exploiting software vulnerabilities.” Anthropic also announced Project Glasswing, which it said was a new initiative that brings together Amazon Web Services, Anthropic, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMChase, the Linux Foundation, Microsoft, NVIDIA, and Palo Alto Networks in an effort to secure the world’s most critical software.

How is Mythos more advanced than tools previously available? In simple terms, 1. Speed of discovering and subsequently exploiting vulnerabilities is much faster for Mythos than previous tools; 2. Minor vulnerabilities can be exploited by combining into serious attacks. Again, the speed of attack by Mythos is much faster than previous tools; and 3. Mythos can reverse engineer exploits on closed-source software, and turn known but not yet widely patched vulnerabilities into exploits.

The AI Security Institute (AISI) in the UK conducted evaluations of Anthropic's Claude Mythos Preview (announced on 7th April) to assess its cybersecurity capabilities and confirmed a significant increase in capability, with the system able to autonomously find and exploit vulnerabilities, execute multi-stage attack chains end to end, and achieved a $73\%$ success rate on expert-level hacking tasks which no model could complete before April 2025. The results from an early checkpoint of GPT-5.5 conducted by the Institute indicate that the GPT-5.5 model also reaches a similar level of performance on AISI's cyber evaluations, which suggests that this step up in cyber performance is a broader trend rather than being limited to one model alone.

The step up in cyber performance, while done in a controlled setup without taking into account potential defense mechanisms/security protocols in a real world environment, highlights the need for financial institutions to improve their cybersecurity defense setup.

The threat is becoming increasingly real, with Google in May 2026 indicating that for the first time, GTIG (Google Threat Intelligence Group) had identified a threat actor using a zero-day exploit that it believes was developed with AI. The criminal threat actor planned to use it in a mass exploitation event, but proactive counter discovery may have prevented its use.

In February 2026, AISI internally estimated that the length of cyber tasks AI models could complete had doubled every 4.7 months since late 2024 – already an acceleration from their November 2025 estimate of 8 months. Since then, AISI reported on two new models, Claude Mythos Preview and GPT-5.5, which substantially exceeded both doubling rate trends. AISI in May said that it is unclear whether this represents a new, faster trend.

Figure 1: Step up in cyber performance over previous frontier models with Mythos and GPT-5.5 Average success rate on advanced cyber tasks at a 50M token budget. 27 Practitioner tasks, 21 Expert tasks Advanced CTF Performance by Model (50M token budget)  
![](images/5207a6479e4289506528b54b15da8df57ca321ccc387648b068a0611a4f3ebbe.jpg)  
In CTF (capture-the-flag) challenges, AI models must identify and exploit weaknesses in target systems to retrieve hidden “flags”. Source: The AI Security Institute, UK (see here)

Anthropic has also noted that the number of vulnerabilities it has disclosed is a subset of the total number of vulnerabilities that Mythos Preview has found, since the process of independent human triage and review is the rate limiting step.

Figure 2: Anthropic dashboard of open-source vulnerabilities, showing vulnerabilities of all severities (rather than only those estimated high- or critical-severity by Mythos Preview).  
![](images/7e5c255121c8d463bfd543d9dce406c5f0d7e359755c670c0aab0739082eb6da.jpg)

## ...with different layers of banking infrastructure impacted by the threat of AI-led cyber attacks

Legacy core banking systems are the most vulnerable to this emerging threat from AI-led cyber attacks, as a portion of Banking platforms of Global banks still run on code which was written decades ago in languages such as COBOL and the current generation of coders may not be as familiar with the logic and comprehension of these codes written by their original coders. Frontier models such as Mythos are able to comprehend these code lines, enabling them to highlight potential vulnerabilities which until now were likely not detectable due to a lack of full comprehension.

Open Source Vulnerabilities can be particularly critical for banks' customer-facing platforms, and the widespread usage across banks of such open source libraries means a vulnerability could have material consequences if exploited by bad actors. Anthropic noted that One example of an open-source vulnerability that Mythos Preview detected was in wolfSSL, an open-source cryptography library that's known for its security and is used by billions of devices worldwide. Mythos Preview constructed an exploit that would let an attacker forge certificates that would (for instance) allow them to host a fake website for a bank or email provider. The website would look perfectly legitimate to an end user, despite being controlled by the attacker. wolfSSL indicates that over 5 billion applications and devices are secured with wolfSSL products, which in our view highlights the scope for potential disruption from exploitation of a vulnerability. In a May 2026 release, Anthropic indicated that it had used Mythos Preview to scan more than 1,000 open-source projects, which collectively underpin much of the internet, and that Mythos Preview had found what it estimates are 6,202 high- or critical-severity vulnerabilities in these projects (out of 23,019 in total, including those it estimates as medium- or low-severity).

Vendor firmware from third-parties is often used by banks and a delay or too long a patch cycle in firmware which cannot be remotely patched would expose the banks to cybersecurity risks. The G7 group of countries note that AI software supply chain security is becoming increasingly important, with several international initiatives underway. As one component of this effort, the Group published actionable guidelines for public and private sector stakeholders on what is reasonable

[中间内容因长度限制已省略]

dates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 28 Jun 2026 06:47 PM BST

Disseminated 29 Jun 2026 12:15 AM BST
"""
