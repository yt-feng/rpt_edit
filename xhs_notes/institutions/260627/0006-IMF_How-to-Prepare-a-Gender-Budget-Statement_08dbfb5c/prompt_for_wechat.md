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
- 已识别机构名：`国际货币基金组织`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份国际货币基金组织研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
![](images/e3bb9ceef161985ba17c5007f42079342647a7e0ced7ea6c2dfb15443c0e4960.jpg)

HOW TO

NOTES

# How to Prepare a Gender Budget Statement

Magdalena Tomczynska-Smith, Gemma Preston, Virginia Alonso Albarran, Laura Gores, Teresa Curristine, and Chloe Cho

HTN/2026/02

This page intentionally left blank

HOW-TO NOTE

# How to Prepare a Gender Budget Statement

Magdalena Tomczynska-Smith, Gemma Preston, Virginia Alonso Albarran, Laura Gores, Teresa Curristine, and Chloe Cho

# © 2026 International Monetary Fund Cover Design: IMF Creative Solutions

How to Prepare a Gender Budget Statement

Magdalena Tomczynska-Smith, Gemma Preston, Virginia Alonso Albarran, Laura Gores, Teresa Curristine, and Chloe Cho
HTN/2026/02

## DISCLAIMER:

How-To Notes offer practical advice from IMF staff members to policymakers on important issues. The views expressed in How-To Notes are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

## Abstract:

Gender budgeting integrates a gender perspective into the budget process by promoting gender equality through both fiscal policies and public financial management tools. A key public financial management tool specific to gender budgeting is the Gender Budget Statement. A government prepares the Gender Budget Statement as a transparency and accountability document to communicate how the budget aims to improve gender equality. Gender Budget Statements must be accessible to a wide audience and present information that is succinct and easily understood. Typically, these statements are summary documents that bring together a government's commitments, goals, priorities, plans, and strategies for addressing identified gaps in gender equality. They are prepared as part of the budget process, highlighting the programs and policies that have been designed to improve gender equality, along with the resources allocated. They are presented to the legislature with the budget documentation to support parliamentary scrutiny and debate. This Note provides guidance on how to prepare a Gender Budget Statement. It covers the content that a typical statement should include, suggests steps for developing a statement, highlights the benefit of a staged approach to implementation, and provides illustrative country examples.

## Recommended Citation:

Magdalena Tomczynska-Smith, Gemma Preston, Virginia Alonso Albarran, Laura Gores, Teresa Curristine, and Chloe Cho. 2026. "How to Prepare a Gender Budget Statement." IMF How-To Note 2026/02, International Monetary Fund, Washington, DC.

JEL Classification Numbers:
E60; H11; H5; H61; H83; J16; J38

ISBNs:
979-8-229-04018-1 (paper)
979-8-229-04094-5 (ePub)
979-8-229-04052-5 (web PDF)

## Contents

What Is a Gender Budget Statement?
1
Country Experience with Gender Budget Statements
3
What Should a Gender Budget Statement Include?
4
How to Start Preparing a Gender Budget Statement
11
Gender Budgeting PFM Tools Supporting the Development of a Gender Budget Statement
14
Organizational Arrangements to Support the Development of a Gender Budget Statement
16
Concluding Remarks
18
Annex 1. Suggested Outline for a Gender Budget Statement Following a Thematic Approach
19
Annex 2. Overview of Practices in Selected Countries
20
Annex 3. Initiating the Gender-Sensitive Budget Annex to the Budget Bill in Togo
22
Annex 4. The Evolution of Gender Budget Statements in Korea
25
Annex 5. Glossary of Gender-Related Terminology
26
Annex 6. Steps Supporting the Preparation of a Gender Budget Statement during the Budget Process
27
References
28
BOXES
Box 1. Definition and Key Features of a Gender Budget Statement
2
Box 2. Building Blocks for a Gender Budget Statement
6
Box 3. Examples of Data and Statistics That Can Demonstrate the State of Gender Equality
9
Annex Box 1.1. THEME 2: Achieving Economic Equality for Women
19
Annex Box 3.1. Outline of the Togolese Gender-Sensitive Budget Document 2024
22
FIGURES
Figure 1. Countries That Prepare a Gender Budget Statement
4
Figure 2. Country Examples: Key Components of Gender Budget Statements
7
Figure 3. Proposed Phases in Developing a Gender Budget Statement
13
Figure 4. Evolution of Features Contained within a Gender Budget Statement
14
Annex Figure 3.1. Steps in Developing the Gender-Sensitive Budget Document in Togo
24

This page intentionally left blank

# What Is a Gender Budget Statement?

The budget is one of the government's most important policy documents. It communicates to citizens and the legislature the government's fiscal strategy, its key policy priorities, and the resources allocated to achieving them. Gender budgeting recognizes that government budgets affects men and women differently and calls on governments to present and explain the implications of their policy choices—and therefore budgets—on gender equality.

A Gender Budget Statement is primarily a transparency and accountability document that a government prepares to communicate how the budget aims to improve gender equality. It highlights relevant policies and the resources allocated to address gender equality gaps (see Box 1). Widely accepted standards of fiscal transparency $^{1}$ require that the budget documentation provides a comprehensive, timely, and credible view of the government’s plans for raising and spending public resources, including a clear statement of the fiscal objectives and policy intentions together with their intended results (IMF 2019). The Gender Budget Statement is well aligned with these same standards of fiscal transparency.

To effectively serve as an accountability instrument, a Gender Budget Statement is publicly available and tabled in the legislature, alongside the annual budget. Communicating the government's efforts to promote gender equality through the budget allows the legislature and the public to engage in an informed dialogue on the status of gender equality, the supporting economic and fiscal initiatives underway, their estimated cost, and the progress made over time. A transparent and comprehensive Gender Budget Statement can also help the government to ensure a consensus understanding of gender equality gaps, and in doing so improve the cohesion of efforts to address them across the public sector.

## A Gender Budget Statement is important for:

\- Improving the transparency of the budget’s expected impact on gender equality.

\- Raising the awareness of the status of gender equality.

\- Strengthening accountability for the delivery of policies and programs designed to bridge gender equality gaps.

\- Encouraging systems for measuring and monitoring the results of policies targeted at improving gender equality.

Box 1. Definition and Key Features of a Gender Budget Statement  
![](images/40747ef27b3ecad818e5b53d89de8458eb20601c8ddc7e4473d0b55822275386.jpg)  
Source: Alonso-Albarran and others 2021.  
Note: GB = gender budgeting; SDGs = Sustainable Development Goals.

Definition: A Gender Budget Statement $^{1}$ is an essential gender-specific public financial management tool. $^{2}$ It aims to provide an overview of the major initiatives that inform a whole-of-government $^{3}$ approach to improving gender equality. $^{4}$ As a transparency and accountability document, it is prepared as part of the budget documentation, in the form of an annex to the budget or supplementary budget paper, and it is tabled in the legislature together with the draft budget for information.

Features: In terms of the key features, the Gender Budget Statement should be:

\- comprehensive by providing an overview of the major policy measures expected to affect gender equality and their allocated financial resources planned in the budget.

\- published and accessible to the wider public, providing clear and relevant information and explanations and by supporting parliamentary oversight and scrutiny.

\- timely to be able to support decision making at the budget approval stage.

1 The term "Gender Budget Statement" is sometimes used in countries to describe various types of gender-specific documents produced during the budget process. Some of these documents remain internal to the government and are mainly prepared to inform the processes of strategic planning and budget prioritization. For the purposes of this Note, such intermediate and internal documents are not classified as Gender Budget Statements. However, they can be important instruments for aligning the budgets with medium-term strategic goals and as an interim step leading to the preparation and publication of the Gender Budget Statement. The following documents fall into this category:

\- Gender pre budget statement—It reflects decisions made in the strategic planning phase of the budget process on the alignment of policy goals with resources available under the budget fiscal constraints. It sets out gender equality policy context and direction for spending plans by articulating the government's broad policy priorities and by establishing the parameters of the budget before detailed funding decisions are made.

\- Gender budget declarations/statements—These are prepared by individual line ministries as part of their budget submissions and designed to provide information on gender analysis and assessment of the proposed budget initiatives. For example, Rwanda's budget call circular required all ministries to prepare and submit a gender statement (which demonstrated how the budget proposal intended to respond to the specific gender needs) to accompany their budget submissions—these statements formed part of the criteria on which budget submission were evaluated; in Australia, new policy proposals were required to include a "statement" (description) of the effect on gender to inform decision making.

$^{2}$ See Alonso-Albarran and others 2021, for a discussion of the IMF gender budgeting framework, which encourages the holistic integration of a gender perspective across each phase of the budget cycle through gender-responsive fiscal policies and gender-specific public financial management practices.

$^{3}$ All ministries and agencies within the general government.

4 Consistent with OECD (2023), which highlights best practices and core features common to the successful implementation of gender budgeting in OECD countries.

# Country Experience with Gender Budget Statements

Over time, Gender Budget Statements have gained traction and visibility across the world. As of 2024, according to a sample of over 100 countries surveyed by the IMF (Figure 1), the Gender Budget Statement is one of the public financial management (PFM) tools mostly used for gender budgeting. Roughly one-third of the sampled countries declared that they produce some form of a Gender Budget Statement and more than three-quarters of these are also published. Of those countries that reported publishing one, Asian and African countries are more represented: 32 percent were in the Asia Pacific region (for example, Australia, Bangladesh, India, Republic of Korea) and 28 percent were in Africa (for example, Togo and Zimbabwe). North and South America represented 20 percent, Europe 16 represented percent, and Middle East and Central Asia constituted 4 percent.

Gender Budget Statements vary considerably across countries in many aspects such as the processes by which they are produced, their scope and depth, and the quality and detail of the contents presented. Countries also use different terminology to name the document such as "Women's Budget Statement" (Australia), "Report on Gender Budgeting and Children Rights, Annex to Budget Bill" (Burkina Faso), "Cross-Cutting Policy Document on Gender Equality" (France), and "Gender Impact Report" (Spain).

The first Gender Budget Statements were pioneered by the Australian Government in the mid-1980s $^{2}$ (although temporarily stopped during the period 2014–21), and since then, many other countries have embarked on similar initiatives. Many countries commenced their publication on a pilot basis. For example, Gender Budget Statements were first piloted with selected ministries in Indonesia (2010), Republic of Korea (2006–10), and Togo (2021) before moving to full implementation.

Like other gender budgeting PFM tools (see Box 1), the preparation of a Gender Budget Statement does not necessitate a radical reform of existing budgetary procedures. Rather, it involves integrating a gender perspective into the existing budget process to demonstrate how budget resources are being used to support the policies designed to tackle gender equality gaps.

Figure 1. Countries That Prepare a Gender Budget Statement  
![](images/6b29efdd5ea729f11c81fdf61f415095c165775d987424aa390b49e616317c19.jpg)

Source: IMF Gender Budget Survey Database has coverage of over 100 countries based on a self-assessment and is updated periodically (as of June 2024).

Note: GBS = Gender Budget Statement. The boundaries, colors, denominations, and any other information shown on the maps do not imply, on the part of the International Monetary Fund, any judgment on the legal status of any territory or any endorsement or acceptance of such boundaries.

## What Should a Gender Budget Statement Include?

Broadly, a Gender Budget Statement should do the following:

\- Set out the government's commitments and goals for improving gender equality.

\- Contextualize and communicate the identified gender equality gaps.

\- Identify strategies and plans for achieving gender equality goals.

\- Showcase the fiscal policies and programs designed to address gender gaps, along with the public resources devoted to do so.

In a few country cases, the information in the Gender Budget Statement goes even further than these steps, to include an assessment as to the expected impact of proposed policies (ex ante) or an assessment as to whether policies in place have been effective in improving gender equality (ex post). In some countries, ex ante and ex post assessments are also published. In practice, not all these features are required, especially not initially, to commence the production of an informative Gender Budget Statement.

The approach to the development of a Gender Budget Statement is country specific and reflects numerous factors such as political commitment, strength of the existing budget system and procedures, maturity of gender budgeting implementation, the availability of gender-specific data, and the available time and resources dedicated to the compilation of the document.

## Format

Countries follow different formats for preparing Gender Budget Statements. Regardless of the format, they should be accessible to a wide range of stakeholders, should be succinct, and should convey key messages. Typically, Gender Budget Statements are either a budget annex or a standalone budget document. The advantage of a separate budget document is that an in-depth presentation of gender issues can be included in a way that is easier to understand for the wider public, who might not be familiar with interpretation of technical budget schedules (Southern African Development Community 2014). UN Women (2015) recommends considering the following useful principles with respect to the size and scope of the Gender Budget Statement:

• Balance the burden placed on government officials who produce the statement and the benefits to those who read them.

\- Provide concise narratives to avoid unnecessarily long descriptions.

\- Use standardized formats to make the preparation easier and enable comparative assessment of the contents across agencies and years.

## Components

Looking at the characteristics of different country approaches, Gender Budget Statements should be designed to help governments articulate the following:

\- Country's socio economic situation from a gender perspective, including presentation of key gap in gender equality.

\- Government's gender equality commitments, goals, strategies, and priorities.

\- Fiscal policies and programs (including new budget measures) targeted to address identified gender gaps, together with their financial implications.

\- The estimated impact of the proposed policies on gender equality outcomes and performance indicators to measure progress over time (more advanced characteristics). A summary of gender impact assessments, if carried out.

Box 2 presents components or building blocks for inclusion in a Gender Budget Statement. There is no single model to present this information, and not all features are required, or sometimes even possible, when starting out. An outline for a well-structured thematic statement is proposed in Annex 1.

## Box 2. Building Blocks for a Gender Budget Statement

## Introduction

\- A statement of political commitment to achieving gender equality (ideally co-signed by the Minister for Finance and the Minister for Women). $^{1}$

\- Motivation for presenting the Gender Budget Statement, including references to the legal and constitutional basis for gender budgeting and gender equality, if any.

\- Outline of high-level approach and methodology to tackling gender inequality—including identifying key issues or themes—for example, women's economic participation, women's safety, or women's leadership potential.

\- Future plans and ambitions for gender budgeting reforms to support gender equality.

## Component 1: Analysis of the Status of Gender Equality and Gender Gaps

• Status of gender equality and recent trends.

• Identification of key gender gaps.

## Component 2: Gender Equality Goals, Commitments, and Strategies to Promote Gender Equality

\- Identification of the government's key priority areas or themes in addressing gender equality

• High-level gender equality commitments, including those made internationally

\- Reference or connection to the government's gender equality goals and strategies for different priorities

\- Approaches to enhance gender equality and eliminate gender gaps

## Component 3: Major Budget Measures Aimed at Promoting Gender Equality in Priority Areas

• Description of each measure

\- Rationale

\- Objectives

• Associated budget allocation

## Component 4: The Impact of Major Budget Measures on Gender Equality

\- Presentation of planned outputs, outcomes, and performance targets for each major budget measure (linked to performance-based budgeting)

\- Assessment of the expected impact on gender equality (link to gender impact assessment), intended and unintended.

## Source: Authors.

Notes: These four components may be repeated on a thematic basis: for example, a country would likely choose to group together all the analysis of the status of gender equality, goals, and policies (Components 1-4) relating to wome

[中间内容因长度限制已省略]

tional Monetary Fund (IMF). 2019. "Fiscal Transparency Code." https://www.imf.org/external/np/fad/trans/Code2019.pdf

Organisation for Economic Co-operation and Development (OECD). "Designing and Implementing Gender Budgeting. A Path to Action." https://www.oecd.org/gov/budgeting/designing-and-implementing-gender-budgeting-a-path-to-action.pdf

Organisation for Economic Co-operation and Development (OECD). 2016a. "Gender Budgeting in OECD Countries: Results of the 2016 OECD Survey of Gender Budgeting Practices."

Organisation for Economic Co-operation and Development (OECD). 2016b. "Handbook on the OECD-DAC Gender Equality Policy Marker." https://www.oecd.org/dac/gender-development/Handbook-OECD-DAC-Gender-Equality-Policy-Marker.pdf

Organisation for Economic Co-operation and Development (OECD). 2017. "OECD Budget Transparency Toolkit: Practical Steps for Supporting Openness, Integrity and Accountability in Public Financial Management." https://www.oecd.org/content/dam/oecd/en/publications/reports/2017/10/oecd-budget-transparency-toolkit\_g1g82a3c/9789264282070-en.pdf

Organisation for Economic Co-operation and Development (OECD). 2018. "Gender Equality in Canada: Mainstreaming, Governance and Budgeting." https://www.oecd-ilibrary.org/governance/gender-equality-in-canada\_9789264301108-en

Organisation for Economic Co-operation and Development (OECD). 2023. "OECD Best Practices for Gender Budgeting" https://one.oecd.org/document/gov/sbo(2023)2/en/pdf

Public Expenditure and Finance Accountability Secretariat. 2016. "Framework for Assessing Public Financial Management." https://www.pefa.org/resources/pefa-2016-framework

Public Expenditure and Finance Accountability Secretariat. 2020. "Supplementary Framework for Assessing Gender Responsive Public Financial Management. Guidance for Assessment Teams." https://www.pefa.org/resources/supplementary-framework-assessing-gender-responsive-public-financial-management-0

Quinn, Sheila. 2016. "Europe: A Survey of Gender Budgeting Efforts." IMF Working Paper 2016/155, International Monetary Fund. https://www.imf.org/en/Publications/WP/Issues/2016/12/31/Europe-A-Survey-of-Gender-Budgeting-Efforts-44148

Southern African Development Community (SADC). 2014. "Guidelines on Gender Responsive Budgeting." https://www.sadc.int/sites/default/files/2021-08/SADC\_GUIDELINES\_ON\_GENDER\_RESPONSIVE\_BUDGETING.pdf

State Government of Victoria. 2022. "Victoria Budget 2022/23 - Gender Equality Budget Statement." https://s3.ap-southeast-2.amazonaws.com/budgetfiles202223.budget.vic.gov.au/2022-23+State+Budget+-+Gender+Equality+Budget+Statement.pdf

Stotsky, Janet Gale, Lisa L. Kolovich, and Suhaib Kebhaj. 2016. "Sub-Saharan Africa: A Survey of Gender Budgeting Efforts." IMF Working Paper 2016/152, International Monetary Fund. https://www.imf.org/en/Publications/WP/Issues/2016/12/31/Sub-Saharan-Africa-A-Survey-of-Gender-Budgeting-Efforts-44145

The Commonwealth Secretariat. 2013. "A Case Study of Gender Responsive Budgeting in Australia." https://australianwomenshealth.org/wp-content/uploads/2023/11/apo-nid395001.pdf

United Nations Development Group. 2013a. "Gender Equality Marker. Guidance Note." https://unsdg.un.org/resources/gender-equality-marker-guidance-note

United Nations Development Group. 2013b. "Steps to Develop a Gender Equality Marker." https://unsdg.un.org/resources/steps-develop-gender-equality-marker

UNIFEM. 2002. "Gender Budget Initiatives. Strategies, Concepts and Experiences." Papers from a High Level International Conference Strengthening Economic and Financial Governance Through Gender Responsive Budgeting, Brussels, October 16-18 2001. https://iknowpolitics.org/sites/default/files/genderbudgetinitiatives\_eng.pdf

UN Women. "Gender Responsive Budgets - Case of Morocco." https://gender-financing.unwomen.org/en/highlights/gender-responsive-budgets-case-of-morocco

UN Women. 2015. "Budget Call Circulars and Gender Budget Statements in the Asia Pacific: A Review." https://asiapacific.unwomen.org/sites/default/files/Field%20Office%20ESEAsia/Docs/Publications/2016/05/UN-Women-CCBGS.pdf

UN Women. 2018. "Sustainable Development Goal Indicator 5c1." https://gender-financing.unwomen.org/en/highlights/sustainable-development-goal-indicator-5c1

UN Women. 2022. "Action Kit. Engaging Parliaments in Gender Responsive Budgeting." https://www.unwomen.org/en/digital-library/publications/2022/11/action-kit-engaging-parliaments-in-gender-responsive-budgeting

UN Women, Women Count, and UN Department of Economic and Social Affairs. 2022. "Progress on the Sustainable Development Goals. The Gender Snapshot 2022." https://data.unwomen.org/publications/progress-sustainable-development-goals-gender-snapshot-2022

UN Women/DFID. 2016. "How Can PFM Reforms Contribute to Gender Equality Outcomes?" Working Paper. https://gender-financing.unwomen.org/en/resources/h/o/w/how-can-pfm-reforms-contribute-to-gender-equality-outcomes

USAID. 2022. "Improving Gender Budgeting in Indonesia." Report by USAID Economic Growth Support Activity (EGSA). https://devtechsys.com/insights/2022/05/03/improving-national-gender-responsive-planning-and-budgeting-for-a-better-tomorrow-for-indonesian-women/

Women's Agenda. 2020. "Each Budget Used to Have a Gender Impact Statement. We Need It Back, Especially Now." Women's Agenda, September 29. https://womensagenda.com.au/latest/each-budget-used-to-have-a-gender-impact-statement-we-need-it-back-especially-now/

World Economic Forum. 2022. "Global Gender Gap Report 2022." https://www3.weforum.org/docs/WEF\_GGGR\_2022.pdf

This page intentionally left blank

This page intentionally left blank

![](images/f3c83800c512ce13f77d170746497ebf6783fdc96fcd3ae8a671a62bc6e6c799.jpg)
"""
