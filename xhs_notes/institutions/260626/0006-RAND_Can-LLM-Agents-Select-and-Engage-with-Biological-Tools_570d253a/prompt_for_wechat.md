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
JEFFREY LEE, ALYSSA WORLAND, KYLE BRADY, GRANT ELLISON, HENRY ALEXANDER BRADLEY, CHRISTOPHER RODRIGUEZ, CASEY MICHAEL O'DAY BARKAN, SUNISHCHAL DEV, DAWID MACIOROWSKI, JORDAN DESPANIE, BARBARA DEL CASTELLO, BRIA PERSAUD, AMAR PANDYA, ELLA GUEST, STEPH GUERRA

# Can LLM Agents Select and Engage with Biological Tools?

An Initial Biosecurity Assessment

This publication has completed RAND's research quality-assurance process but was not professionally copyedited.

## For more information on this publication, visit www.rand.org/t/RRA4741-1.

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

Computational tools for biological research (biological tools, or BTs) are advancing rapidly in both quantity and demonstrated capability. While these technologies offer many benefits for scientific advancement, malicious actors may seek to exploit them to design and develop biological weapons (BWs). Generally, BTs require specialized expertise to operate successfully, presenting a barrier to nefarious use by nonexperts. Large language model (LLM) Agents may erode this barrier by enabling actors with limited domain expertise to successfully use BTs. Assessments of how AI could change bioweapons development pathways should examine how LLM Agents interact with BTs on relevant biological design tasks, but such assessments are limited.

In this report, we present an assessment of the abilities of LLM Agents in the early stages of interaction with BTs. First, we evaluate seven frontier LLM Agents on their ability to select appropriate BTs for a given task. Second, we assess how these LLM Agents engage with two BTs, EVEscape and ESM3, through targeted case studies. These case studies probe the enabling capabilities required for autonomous BT operation, a potential entry point to a wide range of risk pathways. We identify and assess technical barriers at the intersection of LLM Agents and BTs, offering the biosecurity community and AI developers a foundation for further risk and capability assessments as technologies progress.

## Center on AI, Security, and Technology

RAND Global and Emerging Risks is a division of RAND that delivers rigorous and objective public policy research on the most consequential challenges to civilization and global security. This work was undertaken by the division's Center on AI, Security, and Technology, which aims to examine the opportunities and risks of rapid technological change, focusing on artificial intelligence, security, and biotechnology. For more information, contact cast@rand.org.

## Funding

This research was independently initiated and conducted within the Center on AI, Security, and Technology using income from operations and gifts and grants from philanthropic supporters. It was made possible thanks to generous contributions from Chris Anderson and Jacqueline Novogratz, Coefficient Giving, High Tide Foundation, The Pew Charitable Trusts, Sea Grape Foundation, Jaan Tallinn, and Valhalla Foundation as part of The Audacious Project.

A complete list of donors and funders is available at www.rand.org/CAST. RAND clients, donors, and grantors have no influence over research findings or recommendations.

## Acknowledgments

The authors thank Lee Nilsson, Brittany Thomas, Henry Willis, Liisa Ecola, and Alex Kiepert for providing operational support throughout this project. We thank Gary Cecchine, Jason Etchegaray, and Paige Smith for quality assurance, Allison Kerns, Blair Smith, and Rebecca Fowler for their role in organizing our references and citations, Ian Haydon for providing suggestions, Chandra Garber for assistance with figure design, Toby Webster for evaluation review, Gary Abel and SecureBio for insightful discussions on evaluations, and Sara Duhachek Muggy and Taylor Frey for project proposal review. We also thank Adrian Salas, Dave Nguyen, Jay Liu, and Anthony Hakim for infrastructure and research programming support. We would also like to thank Sana Zakaria and Lorenzo Pacchiardi for their peer review.

Advancements in artificial intelligence (AI) offer immense potential for scientific discovery but may also pose significant biosecurity risks. $^{1}$ While there is much focus on the potential for large language models (LLMs) to enable both beneficial and malicious activities, biological tools (BTs), and particularly AI-enabled BTs, are also growing in number and sophistication. Though they are intended for disease treatment and other beneficial purposes, some have the potential to be misused. Concerningly, they could facilitate the development of biological weapons (BWs), such as protein toxins or pathogens with enhanced or targeted effects. Although the successful use of BTs in complex scientific workflows is widely understood to require deep domain expertise, LLM Agents $^{2}$ with access to tooling, databases, and the ability to complete tasks may lower expertise barriers for malicious actors who wish to use BTs in BW design. Benchmarks exist to assess LLMs and LLM Agents on biological tasks, but few examine the ability of LLM Agents to select and deploy specialized BTs for sophisticated biological design tasks. $^{3}$

This report assesses the initial stages of interaction between LLM Agents and BTs. It is structured in two components. The first component is an Agent-driven knowledge benchmark designed to test the ability of LLMs to select appropriate BTs for specific tasks. This evaluation contains two question sets, one containing decontextualized questions and the other featuring specific biological design scenarios. Both sets were evaluated using multiple-choice and open-ended question formats. The second component of this report assesses the ability of LLM Agents to perform toy tasks with BTs. It is designed as a set of two case studies in which LLMs attempt to navigate a BT's code repository, recognize the need for certain pieces of information, and perform basic tool operations.

The BTs selected for these case studies are EVEscape, an immune evasion prediction tool, and ESM3, a protein design and prediction model. EVEscape operation was tested on two biological targets: influenza virus hemagglutinin (HA) protein and Lassa virus spike glycoprotein complex (GPC). ESM3 was tested with green fluorescent protein (GFP) and influenza virus HA protein. The BT selection evaluation was conducted with web-browsing ReAct Agents, while our BT operation case studies tested both ReAct and Cursor CLI Agents. $^{4}$ Both sets of tests were carried out using seven closed- and open-weight frontier LLMs $^{5}$

## Key Findings

\- We find that LLM Agents are capable of performing many initial interactions with BTs, suggesting that they may facilitate BT use by nonexpert actors, and that more targeted testing of LLM Agent design abilities is therefore warranted.

\- LLMs are highly capable of identifying BTs for specific functions but performed worse when required to map BT functions onto contextualized biological design scenarios. In the BT selection evaluation, all seven LLMs were able to identify BTs suitable for performing certain functions, such as designing a protein. Many LLMs scored at or near 80% on these questions in both multiple choice and open-ended response formats. However, accuracy for all models dropped when presented with a different set of questions that contained contextualized scenarios as part of a biological workflow. $^{6}$ Notably, denials $^{7}$ in closed-weight models were common in questions where potential risk was present.

\- The LLM Agents we assessed show some ability to operate BTs for biological design, but reliability was mixed. While Agents were able to operate BTs for predicting immune evasion (with EVEscape) and protein redesign (with ESM3), most were not able carry out these tasks with perfect consistency. The reliability with which a task was completed correctly was dependent on the specific protein being assessed. Where models failed at the task, this was frequently due to errors related to autonomous operation and missteps in data handling.

\- Providing more biological detail in user prompts for our BT operation case studies did not reliably improve performance across all model, task, and protein target combinations. Progressive prompt levels were designed to simulate increasing actor knowledge. While we found that prompting with more biological information could generally improve performance on some of our tasks, such as our GFP-targeted ESM3 case study, this was not the case across all combinations of task and target. $^{8}$ Thus, even actors with deep biological knowledge may find it difficult to predict, a priori, what kinds of information will enable an LLM Agent to effectively interact with particular BTs.

\- Frontier closed-weight models frequently denied requests to answer questions or perform tasks over the course of this work. For BT selection questions that involved dual-use tasks or high-risk biological targets, frontier, closed-weight models were largely prevented from engaging due to either their own refusals or content filter mechanisms. This frequently occurred with scenario questions, which were designed to include some degree of risk. BT operation case studies were also frequently denied, particularly when tasks involved viral proteins.

\- Further investigation into LLM Agent-BT interactions represents a valuable direction for future research. Across diverse models and scaffolding configurations, LLM Agents demonstrated an ability to identify BT functions, consistently engage with the BTs in our case studies, and access relevant biological domain knowledge. While performance varied with data complexity and other factors, a foundational Agent-BT interaction capability was established, warranting deeper investigations that can better address capability and risk.

About This Report ....iii
Summary....v
Figures and Tables....x
Chapter 1. Introduction....1
Chapter 2. Designing and implementing the evaluation ....5
Biological Tool Selection....6
Biological Tool Operation....8
Models and Agent....12
Chapter 3. BT Selection Evaluation Results ....15
Non-scenario Questions....15
Scenario Questions....15
Potential Route to Harm Through LLM Denials....16
Conclusion....17
Chapter 4. BT Operation Case Studies....18
EVEscape....18
ESM3....23
Chapter 5. Conclusion....33
Biosecurity Considerations....34
Challenges and Effect on Risk....35
Potential Future Directions....36
Appendix A. BT Selection Evaluation Tool Categories....38
Appendix B. BT Selection Example Questions....39
Appendix C. EVEscape Threat Model Description....40
EVEscape – predicting viral variants that evade the immune system....40
Appendix D. ESM3 Threat Model Description....41
ESM3 – novel protein design for obfuscation....41
Appendix E. Grading Rubrics and Autograder Assessments....42
Autograder Prompt Categorization....42
Autograder Verdicts....45
Appendix F. Autograder Methodology and Validation....52
Autograder Validation....52
LLM Jury & Validation Details....53
Consistency Tests....54
Discussion....56
Prompt Template....56
ESM3 Rubrics....57
EVEscape Rubrics....58

Appendix G. Protein Sequence Alignment of Agent-ESM3 Generated GFPs .....59
Appendix H. ESM3 Scoring Details .....60
Sequence Alignment and Identity Scoring.....60
Normalized Identity.....60
Structural Alignment with TM-Score .....60
Abbreviations .....62
References .....63
About the Authors .....67

## Figures

Figure 2.1. Overview of the LLM Agent-BT Interaction Evaluations....6
Figure 3.1. Accuracy of LLMs on the Biological Tool Selection Evaluation....16
Figure 4.1. Lassa virus GPC Results for the EVEscape Case Study....20
Figure 4.2. Influenza virus HA Results for the EVEscape Case Study....21
Figure 4.3. GFP Results for the ESM3 Case Study....26
Figure 4.4. ESM3 GFP Case Study: Fraction of Critical Residues Preserved....27
Figure 4.5. Influenza HA Results for the ESM3 Case Study....28
Figure 4.6. LLM Agent-ESM3 Protein Designs....32
Figure E.1. EVEscape Autograder Results, Lassa GPC Base Prompt....45
Figure E.2. EVEscape Autograder Results, Lassa GPC Guiding Suggestions Prompt....46
Figure E.3. EVEscape Autograder Results, Lassa GPC All Bio Details Prompt....47
Figure E.4. ESM3 Autograder Results, GFP Base Prompt....48
Figure E.5. ESM3 Autograder Results, GFP Guiding Suggestions Prompt....49
Figure E.6. ESM3 Autograder Results, GFP Some Bio Details Prompt....50
Figure E.7. ESM3 Autograder Results, GFP All Bio Details Prompt....51
Figure G.1. Alignment of Agent-ESM3 Generated GFPs....59

## Tables

Table 2.1. BT Operation Case Study Targets....8
Table 2.2. Prompt Tiers Used in the BT Operation Case Studies....11
Table 2.3. List of the Closed- and Open-Weight Models Evaluated in This Report....12
Table A.1. BT Selection Evaluation Tool Categories....38
Table E.1. EVEscape BT Rubric....43
Table E.2. ESM3 BT Rubric....44
Table F.1. Autograder Validation Accuracy Rates (0-1.0 scale)....54
Table F.2. Intra-Model Consistency Metrics for Judge Models on Four Validation Datasets....55
Table F.3. Inter-Rater Reliability and Jury Performance Across Datasets....55

Advances in artificial intelligence (AI) offer immense potential for scientific progress but may also introduce biosecurity risks. Recent advances in AI have shown this technology to be beneficial across diverse scientific domains. For example, the large language model (LLM) GPT-5 has demonstrated potential as a collaborator across disciplines ranging from mathematics to biology. $^{9}$ An AI scientist, Kosmos, was reported to arrive at previously privately held findings from biological research and made several novel discoveries. $^{10}$ However, many of the same capabilities that make AI systems useful for advancing scientific research also carry the potential for misuse. In biology, this could translate into increased risk associated with the development of biological weapons (BWs). $^{11}$ Frontier LLMs now match or even outperform human subject matter experts in specialized areas such as virology troubleshooting and other biothreat-relevant subjects. $^{12}$ Consequently, the performance of certain models on these evaluations has led to the implementation of higher AI safety level protections. $^{13}$ As AI capabilities continue to advance, associated biosecurity risks may increase in parallel.

The capabilities of biological tools (BTs) are advancing rapidly and could be misused to design BWs. BTs are models trained on large biological datasets to assist with tasks such as protein and genome design, vaccine development, and other analysis and prediction activities. AI-enabled BTs are a particular area of concern because of their enhanced predictive and generative capabilities. A recent report, “Global Risk Index for AI-enabled Biological Tools” (henceforth referred to as the BT Risk Index), introduced a framework for assessing AI-enabled biological tools. $^{14}$ The report identified more than 1,100 BTs that have been released globally since 2019, many with demonstrable evidence of sophisticated biological capabilities. For example, AlphaFold 2, published in 2021, was a critical advancement in protein structure predictions. $^{15}$ In 2024, AlphaFold 3 expanded these predictions to include complexes consisting of nucleic acids, ions, other proteins, and small molecules. $^{16}$ A 2025 threat assessment further

noted that new open-source, AI-enabled BTs have been released that could increase dual-use capabilities. $^{17}$ Although AI-enabled BTs hold significant potential to accelerate beneficial research such as therapeutics development, the same BTs could also be misused to create enhanced or novel BWs. For instance, researchers have demonstrated that fine-tuned versions of the genome language models Evo 1 and 2 can generate genomes encoding novel, functional phages. $^{18}$ Furthermore, researchers have shown that BTs can be used to design proteins of concern capable of bypassing biosecurity screening methods. $^{19}$ Although some studies suggest that BTs are still limited in generating both evasive and functional protein sequences, $^{20}$ these barriers may erode as BT capabilities advance. The misuse potential, maturity, and accessibility of BTs collectively contribute to their risk profile. $^{21}$ At a minimum, it is evident that there is clear global interest among researchers and organizations in developing increasingly capable BTs to drive advancements in scientific discovery. However, the inherent dual-use risks of those advanced BTs should not be overlooked.

Sufficiently capable LLM Agents could lower barriers to entry and facilitate the use of BTs for beneficial or nefarious purposes. Many BTs lack readily accessible interfaces to guide unfamiliar users. Even when such interfaces exist, challenges such as parameter selection, data formatting, and error troubleshooting can be potential bottlenecks. LLM Agents capable of autonomous planning, decision-making, and action execution may enable misuse by actors lacking domain expertise through natural language control of BTs. $^{22}$ Thus, LLMs proficient in engaging with BTs may heighten misuse risks by lowering technical barriers that currently limit non-expert use. The threat model underpinning the assessment in this report is detailed in the box at the end of this chapter.

Task-based Agent biology evaluati

[中间内容因长度限制已省略]

ol. 302, No. 1, September 2000.

OpenAI, OpenAI o1 System Card, December 5, 2024. As of January 23, 2026: https://openai.com/index/openai-o1-system-card/

Pannu, Jaspreet, Sarah L. Gebauer, Henry Alexander Bradley, Dulani Woods, Doni Bloomfield, Allison Berke, Greg McKelvey, Jr., Anita Cicero, and Tom Inglesby, Defining Hazardous Capabilities of Biological AI Models: Expert Convening to Inform Future Risk Assessment, RAND Corporation, CF-A3649-1, 2025. As of January 20, 2026: https://www.rand.org/pubs/conf\_proceedings/CFA3649-1.html

Paskov, Patricia, Jeffrey Lee, Kyle Brady, and Alyssa Worland, Measuring Biological Capabilities and Risks of AI Agents: Generating and Interpreting Evidence from Agentic Evaluations, RAND Corporation, PE-A4710-1, February 2026. As of March 4, 2026: https://www.rand.org/pubs/perspectives/PEA4710-1.html

Rein, David, Betty Li Hou, Asa Cooper Stickland, Jackson Petty, Richard Yuanzhe Pang, Julien Dirani, Julian Michael, and Samuel R. Bowman, “GPQA: A Graduate-Level Google-Proof Q&A Benchmark,” COLM, arXiv:2311.12022, November 20, 2023.

Thadani, Nicole N., Sarah Gurev, Pascal Notin, Noor Youssef, Nathan J. Rollins, Daniel Ritter, Chris Sander, Yarin Gal, and Debora S. Marks, “Learning from Prepandemic Data to Forecast Viral Escape,” Nature, Vol. 622, October 11, 2023.

Verga, Pat, Sebastian Hofstatter, Sophia Althammer, Yixuan Su, Aleksandra Piktus, Arkady Arkhangorodsky, Minjie Xu, Naomi White, and Patrick Lewis, “Replacing Judges with Juries: Evaluating LLM Generations with a Panel of Diverse Models,” arXiv, arXiv:2404.18796, May 1, 2024.

Webster, Toby, Richard Moulange, Barbara Del Castello, James Walker, Sana Zakaria, and Cassidy Nelson, Global Risk Index for AI-Enabled Biological Tools: Summary Assessment & Methods Report, Centre for Long-Term Resilience and RAND Europe, 2025. As of January 23, 2026: https://www.longtermresilience.org/reports/global-risk-index-for-ai-enabled-biological-tools/

Wittmann, Bruce J., Tessa Alexanian, Craig Bartling, Jacob Beal, Adam Clore, James Diggans, Kevin Flyangolts, Bryan T. Gemler, Tom Mitchell, Steven T. Murphy, et al., “Strengthening Nucleic Acid Biosecurity Screening Against Generative Protein Design Tools,” Science, Vol. 390, No. 6768, October 2025.

Yao, Shunyu, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao, "ReAct: Synergizing Reasoning and Acting in Language Models," ICLR 2023, arXiv:2210.03629, March 10, 2023.

Zhang, Zaixi, Souradip Chakraborty, Amrit Singh Bedi, Emilin Mathew, Varsha Saravanan, Le Cong, Alvaro Velasquez, Sheng Lin-Gibson, Megan Blewett, Dan Hendrycks, et al., "Generative AI for Biosciences: Emerging Threats and Roadmap to Biosecurity," arXiv, arXiv:2510.15975, November 4, 2025.

Jeffrey Lee is a biosecurity evaluations research scientist at RAND. He conducts research on biosecurity and AI capabilities. Lee holds a Ph.D. in molecular biology.

Alyssa Worland is a research adjunct at RAND. She conducts technical and policy research on the intersection of AI and biosecurity. Worland holds a Ph.D. in chemical engineering.

Kyle Brady is an AI evaluations research scientist at RAND. He holds a Ph.D. in electrical engineering.

Grant Ellison is a research assistant at RAND. He conducts technical research on AI capability, AI supply chains, and AI safety. Ellison holds a B.S in economics.

Henry Alexander Bradley is a research assistant at RAND. He conducts technical and policy research on such topics as AI capability evaluations and AI security. Bradley holds a B.S. in computer science.

Christopher Rodriguez is a biosecurity research scientist at RAND. He conducts research on biosecurity and AI capabilities. Rodriguez holds a Ph.D. in computational biology.

Casey Michael O'Day Barkan is an associate physical scientist at RAND. He conducts research on AI security and biosecurity. Barkan holds a Ph.D. in physics.

Sunishchal Dev is an AI Evaluations Research Scientist at RAND. He conducts technical and policy research on such topics as artificial intelligence (AI) capability evaluations and AI's implications on national security. Dev holds a B.A. in technology and innovation management.

Dawid Maciorowski is a technical analyst-adjunct at RAND and a M.D.-Ph.D. candidate studying protein design and virology. He conducts technical and policy research on such topics as AI and biology. Maciorowski holds a B.S. in molecular biology.

Jordan Despanie is an adjunct physical scientist at RAND. He conducts technical and policy research on such topics as biosecurity and AI capabilities. Despanie holds a Ph.D. in pharmaceutical sciences.

Barbara Del Castello is an associate physical scientist at RAND. Her work focuses on biosecurity, examining how emerging technologies impact biological risk and bioterrorism, and science diplomacy. Del Castello holds a Ph.D. in genetics.

Bria Persaud is an adjunct analyst at RAND. She conducts technical and policy research on such topics as biosecurity and AI capabilities. She holds a master's degree in national security policy.

Amar Pandya is a Technical Analyst at RAND and an M.S. candidate in National Security Policy at the RAND School of Public Policy. He conducts research on biosecurity and AI capabilities. He also holds a master's degree in biomedical sciences.

Ella Guest was an associate policy researcher at RAND during the execution of this project. She led AI capability evaluations in the Technology and Security Policy Center. Guest holds a Ph.D. in social statistics.

Steph Guerra is a Senior Research Resident at RAND leading research at the intersection of AI, biotechnology, and national security. Guerra holds a Ph.D. in Biological and Biomedical Sciences.
"""
