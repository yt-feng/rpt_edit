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
- 已识别机构名：`麦肯锡`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份麦肯锡研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# McKinsey on Risk & Resilience

Special edition: The new frontiers of AI in risk management

![](images/2beaecffb4b228356bb5b8864555b7217595f64a347eb02d4d68cc7159db44fc.jpg)

The articles in McKinsey on Risk & Resilience are written by risk experts and practitioners from McKinsey's Risk & Resilience Practice and other firm practices. This publication offers readers insights into value-creating strategies and the translation of those strategies into company performance.

Editorial board:  
Andreas Kremer, Bob Bartels, Charlie Lewis, Daniela Gius, Diana Urieta, Joseba Eceiza, Lorenzo Serino, Marco Vettori, Mihir Mysore, Oliver Bevan, Sebastian Schneider, Thomas Poppensieker, Will Humphrey

McKinsey global publications

Publisher: Raju Narisetti

Global editorial director and deputy publisher: Lucia Rahilly

This issue, and future issues, are available to registered users online at McKinsey.com. Comments and requests for copies or for permissions to republish an article can be sent via email to McKinsey\_Risk@McKinsey.com.

External relations,
Global Risk & Resilience Practice:
Bob Bartels

Global Publishing board of editors: Lucia Rahilly, Mark Staples, Monica Toriello, Rick Tetzeli, Roberta Fusaro

Editor: Roberta Fusaro

Contributing editor: Joanna Pachner

Copyright © 2025 McKinsey & Company. All rights reserved.

Cover image: © Eugene Mymrin/Getty Images

Art direction and design: LEFF

Data visualization: Jessica Wang, Jonathon Rivait, Matt Perry, Richard Johnson

This publication is not intended to be used as the basis for trading in the shares of any company or for undertaking any other complex or significant financial transaction without consulting appropriate professional advisers.

Managing editor: Heather Byer

Editorial production:   
Charmaine Rice, Dana Sand, Drew Holzfeind, Kanika Punwani, Katie Shearer, Katrina Parker, LaShon Malone, Maegan Smith, Mark Cajigao, Mary Gayen, Nancy Cohn, Pamela Norton, Pooja Yadav, Ramya D'Rozario, Regina Small, Roger Draper, Sarah Thuerk, Sneha Vats

No part of this publication may be copied or redistributed in any form without the prior written consent of McKinsey & Company.

![](images/9264625b524201bd48ea7e02f3916711ea61d887cf5bb74300023690b4066c0d.jpg)

## 3 Banking on gen AI in the credit business: The route to value creation

Banks have taken steps to accelerate the adoption of gen AI in the credit business, but most remain on a long-term journey, according to a recent survey.

![](images/1c300eee20c4a8f6fbf6ad490e406854f314521768f0e2beb357f3066a7f5261.jpg)

## 21 How financial institutions can improve their governance of gen AI

A comprehensive scorecard can help companies redesign their risk governance frameworks and practices for gen AI and harness the power of this transformative technology.

![](images/97f815d36b5cc4c00bb8073d00531d22637d7fd6150e0909d8e9982db51634e8.jpg)

## 35 Implementing generative AI with speed and safety Generative AI poses both risks and opportunities. Here's a road map to mitigate the former while moving to capture the latter from day one.

![](images/f6bd025a7b83e97ba7cceaf33ab67b83afe4cf4e2a64c14a0eb5bdbc54225195.jpg)

## 13 How agentic AI can change the way banks fight financial crime

Financial institutions are allocating significant resources to fighting financial crime, but they are generally making little progress. AI-based solutions may be an accelerator.

![](images/39ef2f16cbaf9985c2204e01eafdc38305026fee62b2ac0fa79b6e3cafb73377.jpg)

## 27 Deploying agentic AI with safety and security: A playbook for tech leaders

Autonomous AI agents present a new world of opportunity—and an array of novel and complex risks and vulnerabilities that require attention and action now.

# Introduction

Artificial intelligence, specifically agentic AI, is having a transformative impact on both financial institutions and corporate entities, bringing the role of the chief risk officer (CRO) and the risk management function front and center.

As organizations navigate complex threats and opportunities, leaders must ensure that their organizations adapt and evolve to remain resilient and competitive. Our experience has shown us that today's risk professionals are at the forefront of organizational and operational success.

In this special edition of McKinsey on Risk & Resilience, “The new frontiers of AI in risk management,” we discuss the results of a survey about gen AI’s impact on the credit business; share best practices for fighting financial crime with agentic AI; provide a comprehensive scorecard that can help companies redesign their risk governance frameworks; take a deep dive on securing agentic AI; and offer a road map to navigating the risks and opportunities of AI.

With AI, organizations understand the importance of leveraging risk management not just as a defensive measure but also as a strategic imperative. Our insights help chart a practical AI path—one that balances innovation with sound governance, transparency, and a commitment to ethical outcomes.

— The agentic approach in AI. The agentic approach in AI is revolutionizing productivity by using large language models (LLMs) for focused tasks and integrating them with tools and employees that interact with a company’s digital ecosystem. This method surpasses the gen AI approach by enabling faster and broader digitalization, including complex, unstructured processes that are still rule-based.

— Impact on financial institutions. For banks and financial-services companies, the agentic approach is a game changer. It enhances productivity by digitalizing complex processes, making them more cost-effective, faster, and more reliable. This is particularly significant for the CRO, who oversees risk management and compliance.

— The role of the CRO. The CRO's role is evolving in response to the integration of AI. CROs must now consider a broader spectrum of model risks, facilitated by new regulations, such as the EU Act. CROs' quantitative and technological expertise positions them as natural leaders in AI development and deployment, requiring collaboration across risk, IT, and business functions.

— Rapid development of AI tools. The pace of AI development is accelerating, with an influx of new tools and advanced LMMs. This rapid evolution requires organizations to adapt quickly and plan strategically to stay ahead.

McKinsey, through its Risk & Resilience Practice and QuantumBlack, AI by McKinsey, is at the forefront of innovation in these areas. We collaborate with clients to navigate the complexities of AI integration, and in this issue, we share key experiences and insights as a guide. We hope you find this content useful and look forward to publishing further deep dives on AI in the near future.

Thomas Popperiches

Thomas Poppensieker

Senior partner and chair,

Global Risk & Resilience Editorial Board

Copyright © 2025 McKinsey & Company. All rights reserved.

# Banking on gen AI in the credit business: The route to value creation

Banks have taken steps to accelerate the adoption of gen AI in the credit business, but most remain on a long-term journey, according to a recent survey.

This article is a collaborative effort by Arvind Govindarajan, Filippo Maggi, and Kevin Buehler, with Jania Kesarwani and Maria Acuna, representing views from McKinsey's Risk & Resilience Practice.

![](images/b302e91aafed6003a5e8454082065169ee60edbf389566a11a2d2a45c6e7139f.jpg)

Transformative technologies don't come along very often, so when they do it pays to act quickly. When gen AI algorithms were launched in 2022, banks wasted little time exploring their potential in core commercial credit activities. But three years later, the results are mixed, with some institutions making good progress in putting the technology to work while others lag behind, a new study from McKinsey and the International Association of Credit Portfolio Managers (IACPM) shows (see sidebar, “Our methodology”).

## Gen AI is now a priority for many banks

To gauge banks' progress in adopting gen AI in the credit business, we interviewed and surveyed senior executives at 44 financial institutions globally. Across banks ranging in size from megaplayers to regionals, we asked about the factors affecting their adoption of gen AI, their most promising use cases, and their approaches to managing risks associated with the technology.

The responses were unequivocal on one point: Gen AI is starting to break through, with about half of senior leaders identifying it as a priority. Indeed, in key applications such as credit decisioning and pricing, rising numbers of institutions are rolling out one or more use cases. Moreover, credit

applications often rank on a par or ahead of other applications, with executives seeing particular potential for gen AI in early-warning systems, credit memo drafting, and customer engagement activities.

That said, sentiment is not universally positive. Many banks are cautious about scaling amid continuing skepticism over the technology's financial benefits. As a result, only a few, mainly larger institutions are ahead of the curve, while most say progress has been slower than expected.

Survey respondents tell us there are several reasons for the industry's incrementalist approach. Many banks, for example, are still missing the skills, frameworks, and operational architectures they need to implement gen AI successfully. Underlying these challenges, we see two structural constraints: First, decision-makers are focused too narrowly on simple use cases rather than seeking to transform more complex workflows and end-to-end journeys. Second, we find that most banks have only recently started to deploy agentic AI, a version of the technology that uses decisioning algorithms to create cross-cutting impacts, for example, in the middle and front offices across lines of business. Banks that address these underlying challenges are creating competitive impetus ahead of their peers.

## Our methodology

For the purposes of this article, McKinsey surveyed and interviewed decision-makers at 44 institutions globally in the second half of 2024. Our respondents included a roughly equal number of

executives across megabanks, super-regionals, and core regionals. Megabanks comprised institutions with more than \$1,000 billion in assets, super-regionals included institutions with \$500 billion to \$1,000 billion in assets, and core regionals were defined as having \$100 billion to \$500 billion in assets. We also connected with insurance companies/brokers and development banks.

Most institutions are testing credit use cases
Given a wide range of value creation opportunities, 52 percent of institutions have positioned gen AI adoption as a priority, our survey shows (Exhibit 1). That means senior leadership has prioritized developing gen AI use cases and backed that ambition through investment and hiring. Another 39 percent of institutions say they are interested in gen AI, but adoption is not yet a clear priority, and 9 percent admit that senior leaders are not actively engaged on the topic.

## Exhibit 1

## Leadership at a majority of institutions positions gen AI as a priority.

Leadership commitment to the adoption of gen AI, $^{1}$ % of respondents

Senior leadership promotes developing gen AI use cases as a priority and supports through investments and hiring and demonstrates through tone and actions that there will be setbacks given the technology is nascent

The organization is encouraged to learn about gen AI and is supportive of use case proofs of concept; however, there is less commitment to investments or hiring without a “proven” ROI and knowledge of potential setbacks

Senior leadership does not seem to proactively engage with the topic; the message is rather to approach with caution based on the associated risks

Commitment to implementation of gen AI, by type of institution, $^{1}$ number

Adoption is a priority

![](images/ca49cd7b53ee243ebdf73579f9d64a80b2585d760a8e0cbf8e5ed3ad08168661.jpg)  
Interested, but not a clear priority

![](images/b8d3681fcf1f6f601e3231e50aaf4d2a4d1b61d5decb2a643cf6f6da1242d604.jpg)  
Not a priority

![](images/869c19c9bf58b040c459004cc62774658533b785ff04ef3d086a10fdb841ba7a.jpg)  
$^{1}$ Question: How would you describe your institution's leadership commitment to the adoption of gen AI? (select one). Source: IACPM and McKinsey study on the use of generative AI in credit portfolio management

McKinsey & Company

Gen AI offers financial institutions three highly useful capabilities: concision, meaning the ability to summarize large volumes of data into digestible nuggets; content generation; and customer engagement, mainly seen in the use of bots to support relationship managers and others. Of the three, the largest number of institutions in our survey have made the most advances in concision, with the majority of institutions trying out gen AI applications in activities such as early-warning systems and credit decisioning (Exhibit 2). In one example, a multilateral development bank is exploring a gen AI tool to find the right credit-assessment documents, read and synthesize them, and draw conclusions.

## Exhibit 2

Gen AI use cases in commercial credit vary by the size of the institution.

Factors for prioritizing gen AI use cases, $^{1}$ % of respondents

![](images/581903ea979440aacd0d2fe4349e7a584701d1df94370c7784ea6f8144ed2c6c.jpg)  
$^{1}$ Question: Which gen AI use cases are your institution currently implementing in commercial credit and what are their development stages? (multiple choice). Source: IACPM and McKinsey study on the use of generative AI in credit portfolio management

McKinsey & Company

When initiating or developing use cases, 47 percent of institutions say the most important factor is the promise of uplifts in productivity, followed closely by business needs and regulatory compliance, cited by 44 percent and 25 percent of respondents, respectively (Exhibit 3). Notably, half of institutions do not see return on investment as a major consideration, ranking it as the least important factor in making prioritization decisions. One reason may be that there are no easy ways early in the process to quantify financial impacts.

## Exhibit 3

# Productivity improvement is the most important factor when initiating or developing use cases.

Prioritization and importance in the initiation of gen AI use cases, $^{1}$ % of respondents

![](images/6666203e445f58309f033d821ca58972648f2eeddfe525b0176c1eef152874f4.jpg)  
$^{1}$ Question: How would you rank the following factors in terms of their prioritization/importance in the initiation/development of gen AI use cases in your institution? (rank order).

Source: IACPM and McKinsey study on the use of generative AI in credit portfolio management

McKinsey & Company

Somewhat surprisingly, the group most advanced in deployment is regional banks, which are ahead of megabanks in number of use cases (Exhibit 4). In addition, core regionals are most advanced on ideation and planning.

Very few use cases have reached the stage of full deployment, our survey shows. However, some are further advanced than others. For example, 24 percent of institutions have fully deployed use cases for “ad hoc” applications (Exhibit 5). In that context, several banks report having launched virtual LLM assistants to support use cases such as document processing (PDF conversion, digitizing) and quick QA. And while no bank has yet reached full deployment on synthesizing information for credit decisioning, 27 percent are at the piloting stage. Content generation use cases such as the drafting of credit memos and data assessment are also among the most piloted.

## Exhibit 4

Regional banks are leading deployment.  
![](images/0812b7221cc7b268402fb7ebfdd4f2818ff9eb2af433cf4e11aa89fb7da88770.jpg)  
$^{1}$ Question: Which gen AI use cases are your institution currently implementing in commercial credit, and what are their development stages? (multiple choice). $^{2}$ Megabank includes institutions with >\$1,000 billion in assets; super-regional includes institutions with \$500 billion to \$1,000 billion in assets; core regional includes institutions with \$100 billion to \$500 billion in assets; other includes insurance companies/brokers and development banks. $^{3}$ Includes optimization and maintenance and expansion and scaling  
Source: IACPM and McKinsey study on the use of generative AI in credit portfolio management

## McKinsey & Company

## Exhibit 5

Full deployment is rare across use cases.  
Gen AI use cases in commercial credit and their development stage, $^{1}$ %  
![](images/2124d2903ccf404ca159bf459f0dcdbbd193d4693bf51b5208760337762ac613.jpg)  
$^{1}$ Question: Which gen AI use cases are your institution currently implementing in commercial credit and what are their development stages? (multiple choice). Source: IACPM and McKinsey study on the use of generative AI in credit portfolio management  
McKinsey & Company

## Why banks are taking a conservative approach

Many senior bankers, especially at regionals, are convinced that gen AI applications can create efficiencies, but there is a common gap between attitudes and implementation. Indeed, just 12 percent of North American survey respondents have deployed any use case at all.

At a McKinsey-hosted chief risk officer roundtable in 2023, we asked decision-makers what was holding them back on gen AI adoption. Sixty-seven percent highlighted shortages of gen AI capabilities, while 50 percent pointed to difficulties including defining uses cases and value at stake. A related point was that institutions putting an emphasis on early ROI from the technology were in fact more likely to give up on it, while others that pushed on through had started to see success.

Over the interim period, not too much has changed. Caution is still widespread, reflecting concern over risks that include data security breaches, model hallucinations (faulty outputs), cost-related risks, lack of validation, model and data bias, and latency issues. More than two in five institutions say they have slowed use case development because of disappointing outcomes. Reasons include insufficient accuracy and a lack of articulation on benefits. Indeed, where business scenarios require close to 100 percent accuracy, hallucinations are seen as a significant issue, while some leaders are concerned about the amount of work required to marshal data.

Forty one percent of survey respondents say that model validation issues are holding them back; one reason cited for this is the lack of historical data to assess model performance. Other constraints include too many stakeholders 

[中间内容因长度限制已省略]

ons are increasingly linking their gen AI control framework to their underlying gen AI strategy, with an increasing focus on controls that sit at the infrastructure layer—for example, segregation of data sets that can be accessed by certain archetypes of agents but not others, access restrictions to agent archetype by employee organizational unit, and break-the-glass or kill switches for agents in case of poor performance. For established archetypes, this allows organizations to apply a standardized control set at scale without shouldering an intense burden of either compute or control design for each individual instance of AI usage.

We are starting to see increasing prevalence of agentic deployments in the risk function that will facilitate faster review and performance monitoring to identify and triage unexpected agentic behavior—much as we have sophisticated employee surveillance of higher-risk roles today. This will likely resolve some of the tensions identified above, but we expect organizations to retain a robust challenge role for the risk function that has a clear view of where higher-risk pockets of deployments are most likely to occur and how best to anticipate and resolve these.

new use cases with an awareness of how they fit into the organization's overall gen AI strategy and road map. They're typically drawn from within the businesses and functions for which the organization has the most conviction that gen AI can have significant impact. The product managers should be accountable for identifying and mitigating relevant risks. They will have an important role in driving the cultural changes required to adopt gen AI, including building trust in the proposition that business value can be achieved responsibly and safely for employees and customers.

— Engineers. Engineers are technical experts who understand the mechanics of gen AI. They develop or customize the technology to support the gen AI use cases. Just as important, they're responsible for guiding on the technical feasibility of mitigations and ultimately coding the mitigations to limit risk, as well as developing technical-monitoring strategies.

\- Governors. Governors make up the teams that help establish the necessary governance, processes, and capabilities to drive responsible and safe implementation practices for gen AI. These include establishing the core risk frameworks, guardrails, and principles to guide the work of designers and engineers and challenging risk evaluation and mitigation effectiveness (especially for higher-risk use cases). The AI governance officer is a prime example of this persona, although the role will need to be complemented with others, given the range of potential risks. These roles will ideally cover data risk, data privacy, cybersecurity, regulatory compliance, and technology risk. Given the nascency of gen AI, governors will often need to coordinate with engineers to launch “red team” tests of emerging use cases built on gen AI models to identify and mitigate potential challenges.

\- Users. Users represent the end users of new gen AI tools or use cases. They will need to be trained and acculturated to the dynamics and potential risks of the technology (including their role in responsible usage). They also play a critical role in helping identify risks from gen AI use cases, as they may experience problematic outputs in their interactions with the model.

An operating model should account for how the different personas will interact at different stages of the gen AI life cycle. There will be natural variations for each organization, depending on the specific capabilities embedded in each of the personas. For example, some organizations will have more technical capabilities in designers, meaning they may have a more active delivery role. But the intent of the operating model is to show how engagement varies at each stage of deployment.

Gen AI has the potential to redefine how people work and live. While the technology is fast developing, it comes with risks that range from concerns over the completeness of the training data to the potential of generating inaccurate or malicious outputs. Business leaders need to revise their technology playbooks and drive the integration of effective risk management from the start of their engagement with gen AI. This will allow for the application of this exciting new technology in a safe and responsible way, helping companies manage known risks (including inbound risks) while building the muscles to adapt to unanticipated risks as the capabilities and use cases of the technology expand. With major potential uplift in productivity at stake, working to scale gen AI sustainably and responsibly is essential in capturing its full benefits.

McKinsey Risk & Resilience Practice

Global coleader and North America
Ida Kristensen
Ida\_Kristensen@McKinsey.com

Global coleader and Europe  
Cristina Catania  
Cristina\_Catania@McKinsey.com

Asia-Pacific
Akash Lal
Akash\_Lal@McKinsey.com

Eastern Europe, Middle East, and North Africa  
Elias Hajj  
Elias\_Hajj@McKinsey.com

Theodore Pepanides
Theodore\_Pepanides@McKinsey.com

Latin America
Cristian Berner
Cristian\_Berner@McKinsey.com

Chair, Risk & Resilience Editorial Board

Thomas Poppensieker

Thomas\_Poppensieker@McKinsey.com

Leader, Risk Knowledge

Lorenzo Serino

Lorenzo\_Serino@McKinsey.com

## In this issue

Banking on gen AI in the credit business: The route to value creation

How agentic AI can change the way banks fight financial crime

How financial institutions can improve their governance of gen AI

Deploying agentic AI with safety and security: A playbook for tech leaders

Implementing generative AI with speed and safety
"""
