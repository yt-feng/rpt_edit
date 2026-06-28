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
BCG

![](images/f9b4d1fc1fb1a434881d3e8e1da5dbfab48b430a23f5d228dba1028c680a441a.jpg)

WHITE PAPER

# Navigating the Medtech GenAI Journey: A Policy Primer

October 10, 2023
By Nadya Bartol, Meghna Eichelberger, Peter Lawyer, Kirsten Rulf, Bradley Merrill Thompson $^{1}$ .

1. Bradley Merrill Thompson is an external author who is a Member of Epstein Becker & Green, P.C.

## Navigating the Medtech GenAI Journey: A Policy Primer

The road to successful Generative Artificial Intelligence (GenAI) deployment in medtech can draw parallels from classical literature and mythology. The hero (a medtech company) heeds a call to adventure in pursuit of some glorious proposition (the power of GenAI), embarking on a journey from the known world into the abyss, where they must contend with forbidding and frightening obstacles (incomplete and unclear regulations, potential legal consequences, unknown cyber threats) as well as individual temptation (violations of data privacy, copyright infringement) presenting clear and present danger (to the company and, potentially, to patients). In storybooks, the hero emerges triumphant after an epiphany—while quick thinking may dodge a threat, and great courage and skill may win a battle, it is the hero’s own moral compass that separates their tale from a tragedy. Will your medtech GenAI journey be a Hero’s Tale or a Tragedy?

Our previous articles have focused on the call to adventure (“Medtech Companies Must Move Faster on Generative AI”) as well as the tremendous potential for GenAI technology (“Medtech’s GenAI Opportunity”) and the building blocks required to field GenAI products and services (“Building A Medtech GenAI Platform”). This article focuses on the Policy aspects of your GenAI initiative, including the Responsible AI (RAI) Playbook that serves as a roadmap to ensure your medtech GenAI journey is a successful one.

This Article's Focus - Policy  
![](images/15222dfaf312df935b9ab5eecb815c6cfafd450d79539471d89691966f47a7f1.jpg)  
Source: BCG
Copyright 2023 by Boston Consulting Group. All rights reserved.

## Risks on Your Medtech Journey

Dangers such as leaking Protected Health Information (PHI), making false claims, releasing proprietary data, and infringing copyrights exist regardless of the underlying technology. GenAI heightens these latent risks and introduces others via the inner workings of Large Language Models (LLMs) that are not yet fully understood. These risks could have unpredictable consequences, including biased output (generally due to inadequate training data), so-called “hallucination” (confidently presenting an “answer” that is objectively wrong and often cartoonishly flawed), capability overhang (the propensity for probabilistic models and heuristics to reach a conclusion beyond the natural stopping point, leading to unexpected outcomes), and poor robustness, including false positives and negatives.

## Exhibit 1 – Generative AI Increases Some Existing LLM Risks

![](images/8b9a233b373707d625e21efc76d738712d533c4e2ea470438127b2bcb14db184.jpg)  
Copyright 2023 by Boston Consulting Group. All rights reserved.

AI cyberattacks, especially those involving data poisoning of the model's training data or hijacking the GenAI model itself, present another danger. Maintaining data privacy and safeguarding your model's training data will therefore be a paramount concern. Likewise, the algorithms and services that leverage patient data and your company's intellectual property must be both scrubbed for bias and battle-hardened to prevent unauthorized access and use. Simulated attacks on your GenAI products enable your company to devise response scenarios that help put regulators' minds at ease.

The vanguard protecting your medtech GenAI journey is your company's RAI framework. Simply put, it is an articulation of your company's intended use of AI, with clear guardrails to prevent the misuse and unintended consequences of deploying this technology. Your RAI framework should anticipate and accommodate key concerns of regulators, patients and providers, and other stakeholders, while upholding your company's own value system.

## The Evolving Regulatory Landscape

Regulators walk the highwire of managing risk while providing sufficient leeway for innovation. For Software as a Medical Device (SaMD) and many AI/Machine Learning (ML) products, regulators can simulate hundreds of thousands of real-world scenarios to stress the underlying logic and test the robustness of the code. However, GenAI technology asks regulators to weigh the safety and effectiveness of medical products that generate new information, reaching conclusions that—in clinical situations—could determine how a patient is treated. Hubris on the part of the medtech company or the regulator can lead to tragedy.

In the US, the Food and Drug Administration's (FDA's) Center for Device and Radiological Health (CDRH) acts as the principal regulator for GenAI-powered medical devices, though the Department of Health and Human Services Office of Civil Rights oversees the Health Insurance Portability and Accountability Act (HIPAA), which upholds privacy laws concerning PHI. The EU's FDA equivalent, the European Medicines Agency, bears specific responsibility for devices and equipment via its Medical Device Regulations (MDR), but laws concerning data privacy in AI and GenAI are embedded in the EU's General Data Protection Regulation (GDPR).

The EU’s pending Artificial Intelligence Act proposes a four-tiered risk framework that currently defines all GenAI-powered medical products as “high-risk,” imposing a set of preconditions for market release, facilities for monitoring performance and compliance, as well as significant fines of up to 6% of global revenue for violations. Any such penalties would be incremental to violations of GDPR. EU officials hope to ratify the Artificial Intelligence Act by the close of 2023, compelling all member states to implement its measures within a 20-month transitional period.

The FDA has led the International Medical Device Regulators Forum SaMD working group to agree upon key definitions, a framework for risk categorization, the Quality Management System, and practical ways to run clinical trials. The FDA's December 2019 discussion paper set forth a risk-based framework for AI/ML-enabled device software functions. Congress then authorized the use of Predetermined Change Control Plans (PCCP) for products that evolve within predetermined parameters, enabling applicants to submit for FDA approval their proposed process for validating the model. Low-risk products such as heart rate monitors would require only periodic retesting, while more critical GenAI applications—say, implantable cardiac defibrillators that refine their own parameters for when to fire—would need to undergo more continuous testing. In June, the National Institute of Standards and Technology (NIST) launched a public working group on AI to build on its existing Risk Management Framework. Existing HIPAA regulations would also extend to any new US GenAI offering—but these rules, launched in 2006 and last modified in 2009, are scheduled for an update, possibly before the end of 2023.

Exhibit 2 – Agility Needed to Respond to Existing & Upcoming Regulations (non-exhaustive, selection of key regulations)  
![](images/8b433da948344a809f64881c8f9495024c39e22aa51f78e895a7b0d7629ed9c3.jpg)  
Note: BCG does not provide legal advice  
Source: BCG  
Copyright 2023 by Boston Consulting Group. All rights reserved.

![](images/da1428f39e742f760993fca5bbb53edadc114095e90b0a5094c050a1fe6ac826.jpg)

## Functional and commercial use cases perceived as low-risk offer a safe pathway to gain GenAI experience

## A Closer Look at the US Regulatory Landscape

Functional and commercial use cases perceived as low-risk (for example, HR, IT, Finance, Customer Service) offer a safe pathway for medtech companies eager to gain GenAI experience. Still, customer-facing applications that govern patient access or customer support can come under Federal Trade Commission (FTC) scrutiny, given this agency's mission to uphold health equity across all patient segments.

All Gen AI use cases involving the diagnosis, mitigation, treatment, cure, or prevention of disease or other medical conditions fall directly under FDA jurisdiction. Since CDRH has yet to introduce specific requirements, medtech companies can leverage the existing SaMD frameworks as a guide, and follow some commonsense steps in their GenAI approval and compliance strategies, including the following:

\- Intended Use: The narrower the intended use, the clearer the clinical trial endpoints. Loading up a GenAI offering with a broad swath of clinical claims will create a series of hurdles for your proposed solution that may be difficult to overcome.

\- Human in the Loop. While the presence of a human in the loop can reduce risk, the innovator must note how and under what circumstances this interaction takes place. Companies must specify what happens if the human response is erroneous or if there is no human response at all.

\- Explainability and Transparency. Medtech companies can lower the regulatory bar by ensuring that their model output is transparent and fully explainable so that end users can compare the GenAI solution to the current standard of care.

\- GenAI Model—Locked or Adaptive? Running simulations on a locked model can provide a sense of comfort that the product will perform as expected, but quirks in an adaptive GenAI model can lead to hallucination, capability overhang, and unpredictable output. The regulator therefore needs to devise a means of assessing the potential for dangerous results, as well as a means of re-evaluating the solution once in the field.

\- Data Inputs. GenAI models are trained with defined data sets, which serve as the basis for inferred and suggested solutions as well as guardrails to ensure that cold logic does not lead to extreme and unacceptable answers. So-called “constitutional” models embed human values into the model, permitting an intuitive user interface and more acceptable outputs. However, if new inputs render the model obsolete (“model drift”), the system’s guardrails and solutions can be altered. Moreover, data inputs acquired by the model may be subject to privacy and copyright laws.

\- Algorithm Change Protocol. When seeking clearance or approval from the FDA for products that evolve over time, companies can submit a PCCP to allow the model to change within constraints.

\- Edge Cases. During the clearance or approval process, the FDA may be concerned about so-called “edge cases,” or rare circumstances that may not present themselves in a trial setting but which are fully expected in the field. While humans may recognize the specific circumstances, machines may not—and the potential for adverse consequences must be mitigated.

\- Post-Approval Controls. The FDA will almost certainly seek policy changes that require more stringent post-approval controls to monitor and report on real-world input data validation, intended use, algorithm validation, as well as the safety and effectiveness of your GenAI products and services as they evolve.

\- Secure by Design. GenAI models must be designed with security in mind to resist subversion. Medtech companies should use cybersecurity experts to determine what security controls are required and the types of testing the applications should undergo.

## Exhibit 3 - Clinical Use Cases Have the Most Risks to Proactively Mitigate

![](images/d6b7d8cf4167e4cb0fcf1abae4072c1adb5991484ae4a4009bc29ffa6f715aa8.jpg)  
Copyright 2023 by Boston Consulting Group. All rights reserved.  
Source: BCG

## Developing a Responsible AI Playbook

BCG recommends a centralized approach to developing your RAI playbook at the outset of your GenAI journey to both ensure more control over technology applications and enable rapid iteration. As an initial step, your CEO should sponsor and designate an AI leader within the organization. This leader, who acts as your company's primary GenAI business strategist, should assemble key business sponsors and a cross-functional and cross-organizational team with experts in IT, legal, regulatory, HR, cybersecurity, and privacy to provide the necessary policies and guardrails for your AI solutions. Each potential use case that addresses an internal and external customer pain point requires a business sponsor who approves the investment and takes responsibility for the solution's performance in the field.

The leadership team develops a holistic AI risk assessment for your medtech business, detailing which areas are considered “safe” and which pose potential risk. Informed by this heat map, the team prepares 5–10 guiding principles for GenAI that are consistent with your medtech company’s mission and value statement. These principles underpin your clear and consistent RAI framework, which spells out how, when, and where your company will employ GenAI—as well as where and how it will not. Business sponsors serve as a advocates and missionaries for GenAI, taking the lead from your corporate policy and adapting it to specific use cases. Each use case should be mapped and characterized by your Compliance and IT functions to enable ongoing maintenance and monitoring.

Historically, AI was the province of a select group of technically skilled individuals designing black box solutions that users did not need to understand. However, as GenAI has democratized technology with exciting innovative solutions such as ChatGPT and Bard, your company's approach to managing GenAI technology must also change. Your RAI framework places the onus of managing GenAI solutions at the feet of business leaders, with the IT and Compliance organizations providing necessary support. With your framework and AI leadership team in place, the next step is to create a corporate culture that supports RAI. This may be the trickiest aspect of fielding RAI solutions, and it will be the subject of our next and final article in the medtech GenAI series (Putting Medtech People and Processes to Work With GenAI).

To recap, your medtech company's GenAI journey involves a quest for massive improvements in efficiency in the short term, and personalized and improved patient outcomes over time. Medtech companies will need to experiment safely, learn and iterate quickly, and scale up their capabilities for maximum impact. It will require intellect and determination to take on the known challenges posed by GenAI—and courage and resilience to slay the unknown beasts lurking in the shadows. Medtech leaders must possess all these qualities and one more—humility—to approach the GenAI opportunity in a responsible fashion and avoid turning their Hero's Tale into a Tragedy.

## Acknowledgments

The authors would like to thank the following for their contributions to this article: Stuart John, Tad Roselund, and Gunnar Trommer.
"""
