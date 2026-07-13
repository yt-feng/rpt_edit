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
- 已识别机构名：`亚洲开发银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份亚洲开发银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
![](images/087689e2ceb8801920d5a501dabd18b3bf5298e6723e0c05b946df6af97ada93.jpg)

ADVANCING DIGITAL PAYMENTS
IN NEPAL

INFRASTRUCTURE UPGRADES AND POLICY
DEVELOPMENT FOR ENHANCED TRADE FACILITATION

JULY 2026

ADVANCING DIGITAL PAYMENTS
IN NEPAL

INFRASTRUCTURE UPGRADES AND POLICY
DEVELOPMENT FOR ENHANCED TRADE FACILITATION

JULY 2026

© 2026 Asian Development Bank

6 ADB Avenue, Mandaluyong City, 1550 Metro Manila, Philippines

Tel +63 2 8632 4444; Fax +63 2 8636 2444

www.adb.org

Some rights reserved. Published in 2026.

ISBN 978-92-9277-849-1 (print); 978-92-9277-850-7 (PDF); 978-92-9277-851-4 (e-book)

Publication Stock No. TCS260271-2

DOI: http://dx.doi.org/10.22617/TCS260271-2

The views expressed in this publication are those of the authors and do not necessarily reflect the views and policies of the Asian Development Bank (ADB) or its Board of Governors or the governments they represent.

ADB does not guarantee the accuracy of the data included in this publication and accepts no responsibility for any consequence of their use. The mention of specific companies or products of manufacturers does not imply that they are endorsed or recommended by ADB in preference to others of a similar nature that are not mentioned.

By making any designation of or reference to a particular territory or geographic area in this document, ADB does not intend to make any judgments as to the legal or other status of any territory or area.

This publication is available under the Creative Commons Attribution 3.0 IGO license (CC BY 3.0 IGO) https://creativecommons.org/licenses/by/3.0/igo/. By using the content of this publication, you agree to be bound by the terms of this license. For attribution, translations, adaptations, and permissions, please read the provisions and terms of use at https://www.adb.org/terms-use#openaccess.

This CC license does not apply to non-ADB copyright materials in this publication. If the material is attributed to another source, please contact the copyright owner or publisher of that source for permission to reproduce it. ADB cannot be held liable for any claims that arise as a result of your use of the material.

Please contact pubsmarketing@adb.org if you have questions or comments with respect to content, or if you wish to obtain copyright permission for your intended use that does not fall within these terms, or for permission to use the ADB logo.

Corrigenda to ADB publications may be found at http://www.adb.org/publications/corrigenda.

## Notes:

In this publication, “\$” refers to United States dollars, “₹” refers to Indian rupees, “NRs” refers to Nepalese rupees, and “B” refers to baht.

ADB recognizes “China” as the People’s Republic of China.

Cover design by Ingrid Schroder.

## Contents

Tables, Figures, and Boxes iv
Acknowledgments v
Abbreviations vi
Executive Summary vii
I. Introduction 1
Country Context 1
Report Objectives, Structure, and Methodology 2
II. The State of Nepal's Digital Payment Ecosystem 4
The Financial Landscape 4
The Payments Landscape 7
The Digital Landscape: Connectivity, Access, and Affordability 13
The Digital Readiness of Businesses 15
Policies and Regulations for Digital Financial Services 16
Key Challenges 22
III. Learnings from Country-Level Digital Finance Initiatives 24
Highlights from Digital Payments Implementations Across the Globe 24
Analysis of Success Factors and Challenges: Lessons for Nepal 31
IV. Recommendations 34
Trade Facilitation Priorities 34
Broader Digital Payment System Recommendations 35
High-Level Implementation Road Map 36
Stakeholder Coordination and Monitoring 38
Success Metrics for Trade Facilitation 39
Appendixes
1 Stakeholder Interviews 40
2 Primary Stakeholders in Nepal's Digital Payment Ecosystem 41

# Tables, Figures, and Boxes

Tables
1 Summary of Key Challenges 23
2 Summary of Critical Success Factors 33
3 High-Level Implementation Road Map 36
A1 List of Stakeholder Interviews 40
A2 List of Primary Stakeholders in Nepal's Digital Payment Ecosystem 41
Figures
1 High-Level Architecture of the Retail Payment Switch 11
2 Number of Firms by Size 15
Boxes
1 Formalizing Remittances Through Digital Wallets 8
2 The Nepal Clearing House Limited's Approach to Payment System Interoperability 9
3 Technical Integration Challenges in Nepal's Digital Payment Ecosystem 10
4 Diverging Perspectives on Payment System Interoperability in Nepal 12
5 The India-Nepal Payment Corridor Opportunity 13

# Acknowledgments

This publication was prepared under the Asian Development Bank (ADB) regional technical assistance project on Innovative Knowledge Solutions in South Asia. The work was developed under the guidance of the ADB project team, with Amit Tendulkar, Finance Sector Department of the Singapore Office leading content review and development; the South Asia Operations Coordination Unit responsible for administrative management, publication production, and dissemination; and the South Asia Subregional Economic Cooperation Secretariat supporting stakeholder engagement.

The project team acknowledges the contributions of consultants and subject matter experts from Access Partnership Ltd., who undertook the research and analytical work supporting the preparation of this study. The team would like to acknowledge the contribution of government counterparts, regulators, private sector representatives, and other stakeholders who provided inputs through interviews, consultations, and validation discussions.

Comments and guidance from ADB's Digital Sector Office, the South Asia Department, and the Nepal Resident Mission strengthened the drafting and peer review process. Editorial and production support are gratefully acknowledged.

## Abbreviations

<table><tr><td>ADB</td><td>Asian Development Bank</td></tr><tr><td>AML</td><td>anti-money laundering</td></tr><tr><td>API</td><td>application programming interface</td></tr><tr><td>BIMSTEC</td><td>Bay of Bengal Initiative for Multi-Sectoral Technical and Economic Cooperation</td></tr><tr><td>CBDC</td><td>Central Bank Digital Currency</td></tr><tr><td>CFT</td><td>combating the financing of terrorism</td></tr><tr><td>COVID-19</td><td>coronavirus disease</td></tr><tr><td>DOCSCP</td><td>Department of Commerce, Supplies, and Consumer Protection</td></tr><tr><td>DPI</td><td>digital public infrastructure</td></tr><tr><td>FATF</td><td>Financial Action Task Force</td></tr><tr><td>GDP</td><td>gross domestic product</td></tr><tr><td>GNI</td><td>gross national income</td></tr><tr><td>ISO</td><td>International Organization for Standardization</td></tr><tr><td>KYC</td><td>know your customer</td></tr><tr><td>MNO</td><td>mobile network operator</td></tr><tr><td>MOCIT</td><td>Ministry of Communications and Information Technology</td></tr><tr><td>MOF</td><td>Ministry of Finance</td></tr><tr><td>MOICS</td><td>Ministry of Industry, Commerce, and Supplies</td></tr><tr><td>MSMEs</td><td>micro, small, and medium-sized enterprises</td></tr><tr><td>NBSM</td><td>Nepal Bureau of Standards and Metrology</td></tr><tr><td>NCHL</td><td>Nepal Clearing House Limited</td></tr><tr><td>NPCI</td><td>National Payments Corporation of India</td></tr><tr><td>NRB</td><td>Nepal Rastra Bank</td></tr><tr><td>PSO</td><td>payment system operator</td></tr><tr><td>PSP</td><td>payment service provider</td></tr><tr><td>QR</td><td>Quick Response</td></tr><tr><td>SASEC</td><td>South Asia Subregional Economic Cooperation</td></tr><tr><td>SMS</td><td>short message service</td></tr><tr><td>UPI</td><td>Unified Payments Interface</td></tr><tr><td>USSD</td><td>Unstructured Supplementary Service Data</td></tr></table>

# Executive Summary

This report has been produced as part of the South Asia Subregional Economic Cooperation (SASEC) program, with support from the Asian Development Bank, to strengthen cross-border trade. Digital payment is globally recognized as a key enabler of cross-border trade, facilitating faster, more secure transactions, and expanding opportunities for businesses to participate in regional and global markets.

Nepal's 16th Five-Year Periodic Plan 2024–2029 identifies digital transformation—implemented through the Digital Nepal Framework—as a key strategy to enhance economic competitiveness and productivity. The Plan aims to expand internet access to 90% of the population by 2029 and transition all public sector payments to digital formats. Nepal is making a concerted push to build a digital public infrastructure (DPI) that will serve as the backbone for its digital economy. Elaborated in the forthcoming Digital Nepal Framework 2.0, the government envisions a unified architecture comprising interoperable digital payment systems, digital national identification, and secure data exchange, designed to enable economic transformation and inclusive growth across sectors, and support cross-border trade.

This report has been developed in alignment with the goals of Nepal's 16th Five-Year Periodic Plan and the Digital Nepal Framework, and supports the country's commitment to building secure and interoperable digital payment systems as part of its DPI. The report assesses Nepal's digital payment ecosystem, a complex network of stakeholders, technologies, processes, and regulations that facilitate the exchange of monetary value for goods and services, domestically and internationally. The report identifies key challenges affecting the adoption and growth of digital payment in Nepal. Subsequently, drawing on lessons from other countries' experiences, the report offers strategic recommendations to strengthen Nepal's digital payment ecosystem.

## Key Findings

Nepal, through a program of work under the leadership of Nepal Rastra Bank (NRB), has made significant progress in advancing the digital payment ecosystem, rapidly expanding adoption of mobile and internet banking, and Quick Response (QR) payments among its population. Integration efforts with India's Unified Payments Interface have enabled cross-border payments, demonstrating early success in regional digital payment connectivity. These developments mark a major step forward in digitalizing Nepal's payment infrastructure and laying the foundation for cross-border digital trade.

A feature of Nepal's digital payment landscape is the presence of multiple payment system operators with distinct systems that payment service providers (PSPs) need to individually connect to. This has resulted in varying levels of interoperability, often requiring merchants and consumers to use different apps or platforms depending on the service. In recognition of this challenge, NRB published the National Payment Switch and the National Payment Ecosystem Master Reference Document 2025, which lays out a blueprint for interoperability standards and shared infrastructure. This initiative signals an important shift from disparate systems toward a shared DPI model to support seamless domestic and cross-border payment flows.

Digital payments have served as an entry point for innovation and growth in digital financial services in Nepal, such as digital lending to increase access to finance for micro, small, and medium-sized enterprises (MSMEs), and the exploration of a Central Bank Digital Currency to facilitate cross-border trade. The Government of Nepal is also developing the digital national identification system and promoting its integration into public services and payment platforms for know-your-customer (KYC) verification.

Digital payment adoption remains uneven among individuals and MSMEs. While the use of digital payment systems has grown in recent years, rural populations and smaller businesses have progressed at a different pace due to varying levels of connectivity and digital and financial literacy. To support more inclusive uptake, some PSPs have introduced offline payment innovations, demonstrating how technological innovation can extend the reach of digital payments in areas with unreliable connectivity.

Continued innovation in payment processing systems and infrastructure will require investments in nurturing a skilled, future-ready workforce—developing talent in multidisciplinary areas such as digital finance, payments technology, cybersecurity, data governance and protection, and interoperability. Beyond technical expertise, strategic leadership and policy capacity are needed in both the public and private sectors to guide innovation and manage emerging risks. Strengthening these capacities will be critical for unlocking new economic opportunities, including in tourism and remittances.

## Key Recommendations

To strengthen Nepal's digital payment ecosystem and enhance its role in trade facilitation, a set of recommendations has been developed. They are organized into three interrelated areas: (i) trade facilitation priorities, which focus on strengthening cross-border payment infrastructure, regulatory alignment, payment system interoperability, and market integration; (ii) broader digital payment system development, which outlines measures to enhance the domestic infrastructure and capacity; and (iii) an implementation framework that emphasizes coordinated governance and stakeholder engagement. The report outlines a multiyear road map to guide the phased implementation of these recommendations.

## Trade Facilitation Priorities

## 1. Cross-Border Payment Infrastructure

\- Expedite the resolution of commission structure issues for Nepal–India QR payments to enable the already-developed reciprocal functionality for Nepalis in India.

\- Implement dedicated payment corridors with key trading partners featuring enhanced reliability and pursuing regional standardization through SASEC.

\- Deploy specialized payment solutions for the economically vital tourism and remittance sectors with multicurrency capabilities and streamlined onboarding.

\- Enhance reliability of international payment gateways by addressing middleware issues and establishing redundant infrastructure with automatic failover capabilities.

## 2. Regulatory Alignment and Compliance

\- Strengthen anti-money laundering/combating the financing of terrorism frameworks to address Financial Action Task Force requirements.

\- Implement risk-based KYC procedures that balance financial inclusion with appropriate safeguards, building on the existing tiered model.

\- Harmonize foreign exchange regulations with trading partners and address challenges posed by Nepal's currency peg with the Indian rupee.

• Develop and enact a comprehensive Personal Data Protection Act aligned with international standards.

\- Establish clear consumer protection regulations for digital financial services, especially for cross-border transactions.

• Create a regulatory framework for e-commerce transactions.

## 3. Payment System Interoperability

\- Finalize and mandate the planned open application programming interface rule book to create standardized interfaces connecting banks, businesses, and government agencies.

\- Drive market-wide adoption of the unified NEPALPAY QR standard to address current fragmentation and enable cross-border QR payments with key trading partners.

\- Establish interoperability between mobile wallets and banking systems to improve routing and reduce transaction costs.

## 4. Trade-Focused Market Development

\- Introduce incentive programs for export-oriented businesses.

• Develop specialized digital solutions for informal sector integration.

\- Implement digital documentation solutions for cross-border trade.

\- Establish cross-border fintech partnerships between Nepali PSPs and international fintech companies to adapt proven global solutions to Nepal's needs.

## Broader Digital Payment System Development

## 5. Digital Infrastructure Enhancement

\- Deploy low-bandwidth and offline-capable payment solutions for areas with limited connectivity.

\- Implement hybrid connectivity models combining fiber-optic networks with alternative technologies to reach rural areas.

\- Support the effective implementation of the Cyber Resilience Guidelines and establish a national Financial Sector-Computer Security Incident Response Team.

\- Establish monitoring systems with real-time visibility and automated alerts to track and improve system performance.

## 6. Market Development and Capacity Initiatives

\- Launch targeted merchant adoption programs with subsidized equipment, fee waivers, and training resources, particularly for MSMEs.

• Develop a nationwide network of cash-in/cash-out agents to ensure last-mile financial inclusion.

\- Create a public-private partnership framework to incentivize private sector investment in expanding access to digital financial services and agent networks in underserved regions.

\- Develop comprehensive digital and financial literacy programs with specialized modules for different user groups, including hands-on training and multilingual materials.

\- Address skill shortages through partnerships with educational and training institutions to develop specialized fintech curriculum and certification programs.

• Create a formal regulatory sandbox, as planned by NRB, to foster controlled innovation.

\- Clarify regulatory rules for different providers of digital payments, and ensure fair infrastructure access for licensed nonbank PSPs.

## Implementation Framework

The analysis emphasizes the need for careful sequencing of initiatives, with infrastructure reliability and regulatory clarity as foundational requirements. Achieving success requires a balanced attention to both trade facilitation and domestic system development. Implementation needs to be guided by regular stakeholder feedback and adaptive management approaches to ensure sustainable progress toward a resilient digital payment ecosystem that supports both domestic and international transactions. Central to this effort is strong coordination among stakeholders, including NRB, financial institutions, technology providers, and the business community.

# I. Introduction

## Country Context

Nepal is a country in South Asia with a diverse topography encompassing the Himalayan mountains, hills, and the fertile plains of the Terai region. Its population of 29.65 million people $^{1}$ is equally diverse, comprising numerous indigenous and linguistic communities.

Nepal's economy is predominantly agrarian, with agriculture, forestry, and fishing employing about 60% of the population and contributing to 21% of the country's gross domestic product (GDP). $^{2}$ However, the service sector has been expanding, driven by tourism and remittances from Nepalese working abroad. In 2023, around 55% of Nepal's GDP came from its service sector. $^{3}$

Overall, Nepal's economy continues to recover from the coronaviru

[中间内容因长度限制已省略]

mary Stakeholders in Nepal's Digital Payment Ecosystem

<table><tr><td>Category</td><td>Stakeholder</td><td>Roles</td></tr><tr><td rowspan="4">Ministries</td><td>Ministry of Industry, Commerce, and Supplies (MOICS)</td><td>Sets national trade policy, leads negotiations under frameworks such as the World Trade Organization, South Asian Free Trade Area, and Bay of Bengal Initiative for Multi-Sectoral Technical and Economic Cooperation, and oversees export schemes. Its role is key for aligning e-trade documentation with cross-border payment systemsThe Department of Commerce, Supplies, and Consumer Protection enforces consumer protection and competition rules in e-commerce and digital payments</td></tr><tr><td>Ministry of Finance (MOF)</td><td>Sets tariff policies and fiscal incentives, implemented by the Department of CustomsThe Department of Customs operates the ASYCUDA World system, sets customs procedures, and collects duties</td></tr><tr><td>Ministry of Communications and Information Technology (MOCIT)</td><td>Leads the Digital Nepal Framework, spectrum policy, and government data center strategy—critical for the connectivity and cloud hosting that digital payment systems needThe Department of Information Technology oversees government cloud and data center operations, and manages the digital infrastructure and application programming interface (API) gateways</td></tr><tr><td>National Planning Commission</td><td>Incorporates digital payment and trade facilitation targets into five-year plans, allocates budget ceilings, and monitors alignment with the Sustainable Development Goals</td></tr><tr><td rowspan="2">Regulatory Bodies and Authorities</td><td>Payment Systems Department of Nepal Rastra Bank (NRB)</td><td>Licenses payment system operators and payment service providers (PSPs), sets payment system policies and standards, and oversees cross-border payment corridors and Central Bank Digital Currency pilots</td></tr><tr><td>Financial Intelligence Unit (FIU-Nepal)Nepal Telecommunications Authority</td><td>Serves as the national authority for anti-money laundering and combating the financing of terrorism oversight, and liaises with the Financial Action Task ForceRegulates telecommunication operators, universal service obligations, and know-your-customer (KYC) process for subscriber identity module cards, and promotes last-mile connectivity to enable digital payments</td></tr><tr><td></td><td>Nepal Bureau of Standards and Metrology (NBSM)</td><td>Issues national technical specifications for Quick Response (QR) code, ISO 20022 message profiles, and point-of-sale security</td></tr><tr><td rowspan="3">Implementing Agencies</td><td>Nepal Clearing House Limited (NCHL)</td><td>Operates the national payment infrastructure such as the National Payment Switch, real-time and batch automated clearing house systems, and National Payments Interface Exchange. It serves as the technical backbone for API-based trade payments</td></tr><tr><td>Nepal National Single Window Secretariat</td><td>Coordinates over 40 border agencies via a unified portal</td></tr><tr><td>Department of National Identification and Civil Registration</td><td>Issues biometric national identification cards, and provides digital identification verification and KYC services through APIs for licensed banks, financial institutions, and PSPs</td></tr><tr><td rowspan="4">Private Sector and Financial Partners</td><td>Commercial banks and PSPs (eSewa, Khalti, etc.)</td><td>Drive front-end digital payment innovation, merchant onboarding, and user adoption of QR and wallet-based payment</td></tr><tr><td>Telecommunication operators (Nepal Telecom, Ncell)</td><td>Provides mobile connectivity and SMS and Unstructured Supplementary Service Data (USSD) channels, and supports nationwide QR payment acceptance</td></tr><tr><td>NPCI International Payments Limited</td><td>Works with NRB and NCHL to enable QR code reciprocity and fast, low-cost Nepal-India payments</td></tr><tr><td>Asian Development Bank and South Asia Subregional Economic Cooperation (SASEC)</td><td>Supply technical assistance and concessional finance for backbone upgrades, regulatory harmonization, and trade facilitation pilots SASEC brings together Bangladesh, Bhutan, India, Maldives, Myanmar, Nepal, and Sri Lanka to promote trade and cooperation</td></tr></table>

Source: Authors.

## Advancing Digital Payments in Nepal Infrastructure Upgrades and Policy Development for Enhanced Trade Facilitation

This report explores Nepal's evolving digital payment ecosystem as a driver of cross-border trade and economic growth and has been developed under the South Asia Subregional Economic Cooperation program with support from the Asian Development Bank. Aligned with Nepal's 16th Five-Year Plan and the Digital Nepal Framework, it highlights ongoing efforts to strengthen digital public infrastructure, including interoperable payment systems and digital identification. The report reviews existing developments and adoption trends, draws on relevant international experiences, and presents practical recommendations to support the continued development of secure, inclusive, and efficient digital payment systems that can facilitate Nepal's integration into regional and global markets.

## About the Asian Development Bank

ADB is a leading multilateral development bank supporting inclusive, resilient, and sustainable growth across Asia and the Pacific. Working with its members and partners to solve complex challenges together, ADB harnesses innovative financial tools and strategic partnerships to transform lives, build quality infrastructure, and safeguard our planet. Founded in 1966, ADB is owned by 69 members—50 from the region.
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
