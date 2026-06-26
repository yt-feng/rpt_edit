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
ISMAEL ARCINIEGAS RUEDA, RAHIM ALI, FRANK ANDUJAR LUGO, KARISHMA V. PATEL, ROBIN WANG

# Supply Chain, Energy, and AI Nexus

Evaluating AI Energy Supply Chain Vulnerabilities

For more information on this publication, visit www.rand.org/t/RRA4707-1.

## About RAND

RAND is a research organization that develops solutions to public policy challenges to help make communities throughout the world safer and more secure, healthier and more prosperous. RAND is nonprofit, nonpartisan, and committed to the public interest. To learn more about RAND, visit www.rand.org.

## Research Integrity

Our research integrity is grounded in RAND's core values of quality and objectivity. Rigorous quality assurance procedures, conflict of interest screening, and transparency in funding ensure that every study is objective and nonpartisan. Learn more at www.rand.org/integrity.

RAND's publications do not necessarily reflect the opinions of its research clients and sponsors.

Published by the RAND Corporation, Santa Monica, Calif.

© 2026 RAND Corporation

RAND $^{®}$ is a registered trademark.

## Limited Print and Electronic Distribution Rights

This publication and trademark(s) contained herein are protected by law. This representation of RAND intellectual property is provided for noncommercial use only. Unauthorized posting of this publication online is prohibited; linking directly to its webpage on rand.org is encouraged. Permission is required from RAND to reproduce, or reuse in another form, any of its research products for commercial purposes. For information on reprint and reuse permissions, visit www.rand.org/about/publishing/permissions.

The past few years have seen rapid advances in the capabilities of artificial intelligence (AI) models and increasingly widespread use of such models. The resulting increase in demand for AI computational resources is already posing challenges for data center construction in the United States, primarily because it is difficult to find and access reliable power grid capacity. To anticipate the constraints these challenges may place on future AI growth, we seek to answer the following questions in a series of RAND reports:

• What will the U.S. additional power capacity be by 2030?

\- What are the key constraints to scaling the U.S. power grid to meet additional demand?

\- What sites or regions in the United States have favorable or unfavorable characteristics for maximizing available energy capacity for AI data centers? What is an estimate of the maximum amount of power available for AI data centers at a single site by 2030?

\- What are the existing electrical equipment supply chain vulnerabilities that may constrain frontier AI data center development?

In this report, we first provide an inventory of critical electrical equipment required for frontier AI data center operations, in which we define frontier AI data centers as a subset of hyperscale data centers that are designed to consume over 100 megawatts (MW) and are used primarily for AI training and operation. $^{1}$ The inventory of equipment includes components at the front of the meter, behind the meter, and off-grid operations equipment, commonly referred to as bridge power. $^{2}$ Next, we introduce a methodology to estimate supply chain vulnerabilities using open-source data, which we used to identify the most vulnerable electric equipment. With this methodology, we develop a ranking of supply chain vulnerabilities across the inventory. Then, we quantitatively evaluate the impact of these vulnerabilities by examining supply chain risks in the context of the inability of the United States to meet frontier AI energy demand using case studies of different supply chain threats. $^{3}$ Finally, we conclude with policy recommendations.

## Center on AI, Security, and Technology

RAND Global and Emerging Risks is a division of RAND that delivers rigorous and objective public policy research on the most consequential challenges to civilization and global security. This work was undertaken by the division's Center on AI, Security, and Technology, which aims to examine the opportunities and risks of rapid technological change, focusing on artificial intelligence, security, and biotechnology. For more information, contact cast@rand.org.

## Funding

This research was independently initiated and conducted within the Center on AI, Security, and Technology using income from operations and gifts from philanthropic supporters. A complete list of donors and funders is available at www.rand.org/CAST. RAND donors and grantors have no influence over research findings or recommendations.

## Acknowledgments

We would like to thank the leadership of the RAND Center on AI, Security, and Technology—Sella Nevo, Jeff Alstott, and Kyle Evans—for their guidance on this publication; Jason Etchegaray for managing the quality assurance process; and our reviewers Toby Sytsma, Konstantin Pilz, and David Rode for their thoughtful feedback. We are also thankful to several industry stakeholders with whom we held discussions about the topic for their insights.

## Issue

The anticipated growth in artificial intelligence (AI) development requires additional power capacity. Data center operators often prefer that this additional capacity comes from connections to the grid because such connections offer improved reliability, resilience, and cost-effectiveness that is not available from on-site electricity generation. $^{4}$ However, stakeholders have identified major challenges facing the U.S. grid, especially concerning the integration of large volumes of energy resources. The North American Electric Reliability Corporation (NERC) $^{5}$ warns that more than half of North America faces a substantial risk of energy shortfalls within the next five to ten years, the result of increasing electricity demand from data centers, decarbonization through electrification, and industrial growth. $^{6}$ Although many initiatives to increase generation capacity are in progress, the pace of these efforts may pose challenges in terms of meeting future energy demands. And progress can be hindered by supply chain vulnerabilities in the procurement of critical electrical equipment for front-of-the-meter (FTM), behind-the-meter (BTM), and off-grid (usually referred to as bridge power [BP]) projects to supply AI energy demand. This report addresses the following research questions:

\- What is the critical equipment required for meeting frontier AI energy demand?

• What are the supply chain vulnerabilities of this equipment?

\- What could be the impact of those vulnerabilities on the U.S. power grid's ability to meet AI demand by 2030?

## Approach

We used a mixed-methods approach for this research, as follows:

\- We conducted a rapid literature review, which highlighted the existing major research gaps between (1) component-level needs for AI energy build-out and (2) supply chain analysis directly informing component-level assessments. This report provides contributions to closing those gaps.

\- We developed an inventory of critical equipment required for powering frontier AI data centers. Our analysis covered equipment not only for grid-connected data centers (FTM and BTM) but also for BP.

\- We developed a methodology to assess the supply chain vulnerabilities of the inventory of critical equipment by introducing a supply chain vulnerability index and visualization maps to rank the vulnerability of the equipment.

\- We developed a case-study approach to quantitatively evaluate the impact of vulnerabilities on the risk of not meeting AI demand using a framework based on examining supply chain risk as a function of the following three elements: threats, vulnerabilities, and consequences.

## Key Findings

\- We found that several pieces of equipment, such as natural gas turbines, that may be required for FTM installations are also required by off-grid BP installations, which indicates that data centers cannot eliminate supply chain constraints by moving off-grid.

\- We introduced a composite supply chain vulnerability score composed of several metrics, which allows for a ranking of the different equipment across several years. Using this score, we identified the following:

\- For the FTM generation category in 2025, steam turbines, geothermal production wells, and solar panel parts are at the top of the vulnerability ranking. Battery technologies and chemistries also show elevated 2025 composite vulnerability. See Table 4.2.

\- In the FTM transmission category, conductors and wires and reactive power compensators show the highest 2025 composite vulnerability. See Table 4.3.

\- For BTM, there is a concentration of backup power components at the top of the supply chain vulnerability ranking in 2025. See Table 4.4.

\- We found that generation components demonstrate systematically higher composite vulnerability scores in 2025 than transmission components do. This divergence likely reflects fundamental market structure differences. Transmission equipment represents more established, standardized technology, whereas generation components often involve specialized, technologically advancing systems with more limited production sources and higher barriers to entry for new manufacturers.

\- We identified that the main source of supply chain vulnerabilities varies significantly across equipment and time, which implies that effective supply chain resilience strategies must be tailored to the specific vulnerability profile of each equipment. For instance, turbine generators show a vulnerability mainly arising from market concentration; for transformers, the main source of vulnerability is volume volatility. Tables 4.2, 4.3, and 4.4 provide a deeper analysis of vulnerability profiles for transformers, natural gas turbines, and batteries.

\- We developed a decisionmaking framework that matches critical components to target policy interventions and therefore recognizes the heterogeneity in the supply chain vulnerabilities across components.

\- We developed case studies and sensitivity analysis to quantitatively estimate the impact of supply chain considerations on the ability of the U.S. power grid to meet AI frontier demand. We measured this case study against a base case in which there were supply chain delays similar to what is currently reported by stakeholders.

\- We estimate that supply chain–related threats to FTM components (natural gas generation, storage, transformers) have the potential to result in approximately a 7 percent to 31 percent decrease in available net capacity by 2030 in comparison with a base case of no additional delays in the procurement of natural gas turbines, batteries, and transformers.

\- We estimate that supply chain–related threats to BTM components (batteries) have the potential to result in approximately an 8 percent decrease in available net capacity by 2030 in comparison with a base case of no additional delays in the procurement of BTM batteries.

\- We estimate that a further move off-grid to meet the energy gap using BP would translate to an additional need for aeroderivative turbines of 91 to 123 110-MW turbines or 451 to 611 30-MW turbines by 2027, as well as 1,582 to 1,690 110-MW turbines or 7,909 to 8,449 30-MW turbines by 2030, which would further stress the supply chain.

## Policy Recommendations

## Our suggested recommendations are as follows:

\- Implement a decision framework for responding to observed supply chain vulnerabilities with proportionate policy actions. The metrics developed in this research can be used to systematically distinguish appropriate response options according to patterns observed in supply chain vulnerabilities by type, magnitude, and duration. As critical components meet distinguishing criteria, responses can move across different levels, such as routine monitoring, targeted resilience efforts, and proactive strategic intervention. The U.S. Department of Energy (DOE) should adopt a decision framework, such as the one provided in Table 6.1, to have a targeted approach to address supply chain issues.

\- The U.S. government should prioritize supply chain policy interventions in generation systems, given their more acute supply chain vulnerability with respect to transmission and critical impact across all supply options (FTM, BTM, and BP). Specifically, priority should be given to the most vulnerable generation components as listed in Table 4.2.

\- Consider improving the monitoring capabilities to inform intervention by increasing the granularity of trade data for certain electrical components, such as natural gas turbines and transformer types. The U.S. International Trade Commission and U.S. Customs and Border Protection should work together to increase the specificity of certain Harmonized Tariff Schedules and Schedule B codes, at the ten-digit level. This report provides Figures 4.7 (for transformers) and 4.8 (for turbines), the most supply chain-vulnerable components that could be targeted for additional trade data granularity.

\- Consider enhancing supply chain mapping capabilities by designing reasonable disclosure requirements for firms transacting or handling key critical components. The U.S. Securities and Exchange Commission and U.S. Department of Homeland Security should drive a consultative process with utilities, producers, and other

government partners to ensure a common language and understanding that leads to improved visibility and coordination around supply chain risks while calibrating the potential burden of additional reporting requirements against the perceived benefits of improving decisive insights. $^{7}$ The supply chain vulnerability heat maps in Figures 4.3 and 4.5 could be used to select the equipment that may merit additional reporting.

\- Consider developing a reserve of high-demand, low-supply electric grid components to proactively buffer against supply chain shocks. Building on proven models for strategic reserves across critical sectors for guidance on technical operations, $^{8}$ including GridAssurance for transmission equipment, the Strategic Petroleum Reserve for energy security, the National Defense Stockpile for critical minerals, and the Strategic National Stockpile for medical supplies, DOE and the Federal Energy Regulatory Commission (FERC) should coordinate with utilities and large loads, such as data centers, to identify and maintain reserves of the most-critical grid components. A transparent selection process and cost recovery mechanism would ensure that these reserves enhance resilience while remaining economically sustainable.

\- Consider developing incentives for utilities and large loads to adopt codes and standards that increase the standardization of critical equipment as a measure to mitigate supply chain constraints, such as market concentration. DOE and the U.S. Department of the Interior should work with consensus-driven organizations, such as the National Electric Code or the Institute of Electrical and Electronics Engineers, and utilities to develop codes and standards that encourage standardization and adoption. Figures 4.3 and 4.5 provide the critical components most likely to benefit from standardization because of their high market concentration.

\- Consider developing a mechanism for collaboration and transparency between utilities and large loads to improve load forecasting and therefore better manage the procurement of scarce equipment (e.g., turbines). DOE and FERC should facilitate the development of those collaborations to facilitate long-term partnerships that help mitigate supply chain issues.

\- Consider encouraging, whenever possible, the substitution of storage equipment with chemistries with high supply chain vulnerabilities (e.g., lithium) with chemistries of lower vulnerabilities (e.g., sodium). DOE should work with research organizations and utilities to develop potential commercialization opportunities for storage chemistries with lower vulnerability.

About This Report ....iii
Summary....v
Figures and Tables....xi
Chapter 1. Introduction....1
Background and Motivation....1
Key Assumptions and Limitations....2
Report Outline....4
Chapter 2. Literature Review ....5
General Findings: Persistent Gaps in Component-Level Detail and Quantitative Analysis....6
Critical Electric Power Components Required by AI Data Centers....8
Projected Equipment Requirements....9
Supply Chain Vulnerabilities for AI-Critical Electrical Equipment....9
Chapter 3. Inventory of Critical Electric Power Components....11
Approach to Developing Inventory....11
Front-of-the-Meter Systems and Components....14
Behind-the-Meter Systems and Components....16
Bridge Power Systems and Components....17
Benefits of Inventory Development....18
Chapter 4. Supply Chain Vulnerability Estimation....19
Methods for Examining Supply Chain Vulnerability....20
Results and Findings....28
Chapter 5. Assessing Supply Chain Risks for Frontier AI Data Center Expansion Using Case Studies....48
Estimating Consequences for Frontier AI Data Center Expansion....49
Threat Scenarios Affecting Frontier AI Data Center Expansion....51
Supply Chain Impact....56
Impact for Off-Grid Systems....57
Chapter 6. Policy Recommendations....60
Recommendations....60
Appendix A. Literature Review Methodology....70
Seed Literature....70
Key Words for Source Identification....71
Search Protocols....75
Structured Queries for Evidence Extraction....75
Synthesis....76
Appendix B. Inventory of Critical Components....78
Appendix C. Example of Supply Chain Vulnerability Assessment Calculation....90

Example Vulnerability Calculation....90
Sensitivity Analysis....92
Appendix D. Supply Chain Vulnerability Assessment....93
Abbreviations....100
Glossary....101
References....103
About the Authors....109

## Figures

Figure 2.1. Literature Review Workflow ....5
Figure 3.1. Schematic of the General Energy Infrastructure Categories....13
Figure 4.1. Process for Matching HTS Codes to Critical Components....22
Figure 4.2. Composite Vulnerability Indicator Calculation....26
Figure 4.3. Vulnerability Map for FTM Components....30
Figure 4.4. Aggregate Trends in Vulnerability for FTM Components....33
Figure 4.5. Vulnerability Map for BTM Components....36
Figure 4.6. Aggregate Trends in Vulnerability for BTM Components....38
Figure 4.7. Vulnerabilities for Transformer-Related Components for FTM and BTM....41
Figure 4.8. Vulnerabilities for Turbine-Related Components for FTM and BTM....44
Figure 4.9. Vulnerabilities for Battery-Related Components for FTM and BTM....47
Figure 5.1. Approach to Measure Supply Chain Risk....49
Figure D.1. Vulnerability Scores for FTM Systems.

[中间内容因长度限制已省略]

ssessment, December 2024.

Ontiveros, Jeremie Eliahou, Dylan Patel, and Daniel Nishball, “Datacenter Anatomy Part 1: Electrical Systems,” SemiAnalysis, Substack, October 14, 2024.

Pandey, Ajey, Jeremie Eliahou Ontiveros, and Dylan Patel, “How AI Labs Are Solving the Power Gap Crisis: The Onsite Gas Deep Dive,” SemiAnalysis, Substack, December 30, 2025.

Peivandizadeh, Ali, “A Theoretical Framework for Virtual Power Plant Integration with Gigawatt-Scale AI Data Centers: Multi-Timescale Control and Stability Analysis,” arXiv, arXiv:2506.17284, June 14, 2025.

Peng, Peng, Man Chen, Yuxuan Li, Yuxin Zhao, Ningning Li, Hao Liu, Bing Wang, Yushu Sun, and Xisheng Tang, “Research on Energy Storage Type of Uninterruptible Power Supply Technology in Internet Data Center,” Proceedings of the 2022 12th International Conference on Power and Energy Systems, December 2022.

Pesin, Michael, “DOE and Industry Team Up to Keep the Lights on for America,” Office of Electricity, U.S. Department of Energy, February 22, 2024.

Pilz, Konstantin F., Yusuf Mahmood, and Lennart Heim, AI's Power Requirements Under Exponential Growth: Extrapolating AI Data Center Power Demand and Assessing Its Potential Impact on U.S. Competitiveness, RAND Corporation, RR-A3572-1, 2025. As of May 14, 2026: https://www.rand.org/pubs/research\_reports/RRA3572-1.html

Pinto, Alisha, “Transformers Are Facing Major Cost, Supply Chain Pressures,” National Rural Utilities Cooperative Finance Corporation, March 24, 2025.

Popik, Thomas, “Ukraine’s Coming Electricity Crisis,” Foreign Affairs, February 3, 2023.

Powell, Phill, and Ian Smalley, “What Is Hyperscale?” IBM, undated. As of June 16, 2026: https://www.ibm.com/think/topics/hyperscale

Quint, Ryan, Kyle Thomas, Jiecheng Zhao, Andrew Isaacs, and Casey Baker, Practical Guidance and Considerations for Large Load Interconnections, Elevate Energy Consulting and GridLab, May 2025.

Rider, Darryl, “Winning the Race to Revenue—Bridge Power Solutions for Data Centers,” Caterpillar, April 2025.

S, Hrishikesh, “A New Semiconductor Tug of War: AI Data Centers vs. Automakers,” S&P Global, October 10, 2025.

Stansbury, Martin, Kelly Marchese, Kate Hardin, and Carolyn Amon, “Can US Infrastructure Keep Up with the AI Economy?” Deloitte, June 24, 2025.

Thomson, Jim, Marlene Motyka, Kate Hardin, and Jaya Nagdeo, Electric Power Supply Chains: Achieving Security, Sustainability, and Resilience, Deloitte, 2022.

Trabish, Herman K., “Utilities, Regulators, Look to Accelerate Pilots to Achieve Speed-to-Innovation,” Utility Dive, December 1, 2025.

U.S. Customs and Border Protection, “Customs Rulings Online Search System (CROSS),” webpage, undated. As of May 19, 2026: https://rulings.cbp.gov/home

U.S. Department of Energy, “How Gas Turbine Power Plants Work,” webpage, undated. As of May 14, 2026:
https://www.energy.gov/fecm/how-gas-turbine-power-plants-work

U.S. Department of Homeland Security, Risk Management Fundamentals: Homeland Security Risk Management Doctrine, April 2011.

U.S. Energy Information Administration, “U.S. Electric System Is Made Up of Interconnections and Balancing Authorities,” July 20, 2016.

U.S. International Trade Commission, “Harmonized Tariff Schedule,” webpage, undated. As of May 19, 2026: https://hts.usitc.gov

Voltage Voyager, “Understanding Microgrid Components and Topology: A Comprehensive Guide,” Electrical Blog, June 28, 2025. As of November 18, 2025: https://www.electrical-blog.com/microgrid-components-topology/

Wilson, John D., Sophie Meyer, Zach Zimmerman, and Rob Gramlich, “Power Demand Forecasts Revised Up for Third Year Running, Led by Data Centers,” Grid Strategies, November 2025.

Wood Mackenzie, “Power Transformers and Distribution Transformers Will Face Supply Deficits of 30% and 10% in 2025,” press release, August 14, 2025.

Xiong, Ding, and Yao Sun, “The Rising Cost of Turmoil: Geopolitical Crises and Supply Chain Risk,” Economic Letters, Vol. 255, September 2025.

Yuksel, Aytek, “Components of Microgrids,” Cummins, October 4, 2021.

Ismael Arciniegas Rueda is a senior economist at RAND and AI Energy Cluster Lead at the RAND Center on AI, Security, and Technology, where he applies quantitative methods to energy markets. His work has included providing input on where to locate AI data centers, exploring the use of AI to improve energy security, and examining the security implications of a power grid developed and governed by China. Arciniegas Rueda holds a Ph.D. in economics.

Rahim Ali is a senior technical analyst at RAND. His research interests include critical infrastructure protection and resilience planning, disaster preparedness and recovery, and infrastructure risk analysis. Ali holds an M.S. in civil and environmental engineering with a focus in advanced infrastructure systems.

Frank Andujar Lugo is a technical analyst at RAND. His research interests include energy security, climate trends adaptation and mitigation, disaster preparedness and recovery, analysis of alternatives for systems and force architecture design and optimization, and emerging technologies. Lugo holds an M.S. in mechanical engineering.

Karishma V. Patel is an adjunct policy researcher at RAND. Her work spans risk assessment and response design across public investment and project portfolios, supply chains, and critical infrastructure systems. Patel holds an M.P.A. in public administration.

Robin Wang is an assistant policy researcher at RAND. His research focuses on AI and energy infrastructure build-out, the systemic risks emerging from recent development, and government finance and equity implications of adaptation interventions. He holds an M.P.A. with a concentration in economic and public policy.
"""
