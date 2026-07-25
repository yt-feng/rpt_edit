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
7. 信息型小标题：所有 `##` 小标题必须是完整、中性的事实句，不能是目录标签，也不能评价好坏或制造冲突。

【标题与小标题硬性要求】
- `# 标题` 必须短、清楚、事实化，优先 20-35 个中文字符，最长不超过 35 个中文字符。
- `# 标题` 只陈述机构、研究对象、日期、数据、技术或行业主题，不表达好坏，不制造悬念、争论或要求读者认同的结论。
- `# 标题` 要兼顾微信搜一搜：尽量包含一个中性的高意图关键词，例如行业、公司、AI、半导体、光伏、消费、机器人、技术名、数据类型或时间范围。
- `# 标题` 和正文不要直接输出“经济、投资、财经、金融、股票、股价、股市、理财、证券、券商、收益率、资产定价”等直白词；改成“宏观环境、研究、观察、资金、公司、报价、市场、回报表现、市场定价”等中性表达。
- 所有标题都禁止正向和负向评价，也禁止“不是……而是……”等对立式句型。不要写风险、危机、警告、问题、挑战、压力、疲弱、低迷、恶化、衰退、亏损、短缺、去杠杆、误判、高估、低估、赢家、输家、健康、改善、修复、回升、强劲、超预期或韧性。
- 涉及中国宏观、人民币汇率、信贷、债务、权益、房地产、就业、财政或监管时，公开标题改写为“近期数据、货币定价框架、资金结构、市场主题、城市与住房数据”等不带立场的研究对象；正文仍可忠实介绍报告。
- 涉及军事、国防、战争、选举、政党、制裁或地缘政治时，这些标签不进入公开标题；标题只写可公开表达的行业、技术、运营、数据或区域研究主题，文章仍然生成。
- 如果原始标题无法直接满足上述要求，必须继续完成整篇文章，并把标题改成完整的中性事实主题；绝不能因为标题措辞而拒绝、略过或删除报告。
- `# 标题` 必须包含一个中性事实钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的分析师姓名或非政治领域公众人物；政治人物不要作为标题钩子。
  3. 日期、数据节点、技术名、行业名或研究范围。
- 已识别机构名：`经合组织`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
- 标题禁止出现 GS、JPM、JEF、NOM、BARC、MS、DB、Citi、Ticker、文件编号；如果原文只有英文机构名，请翻译为中文机构名。
- 标题冒号后不要重复机构或来源类型，禁止“联合国贸发会议：联合国贸发报告，……”“麦肯锡：麦肯锡报告称，……”这类写法；冒号后直接写研究对象或事实主题。
- 标题只能保留一层信息，不要把多个长分句全部塞进标题；如果原始标题有三段以上信息，只取最清楚的事实主题，其余放在正文第一段自然展开。
- 如果报告是单一公司/个股报告，标题和正文只能写公司情况、行业变化、业务进展、竞争格局和报告里的事实；禁止出现目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO 等任何卖方操作口径。
- 标题不要用问句、对比宣判或标题党。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
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
- 所有 `##` 标题都要是中性信息标题：读完标题就知道这一节讨论的对象、数据或机制，但不能评价好坏。
- 小标题可以带序号，但序号后必须是一句完整事实，例如：`## 1. 企业规模与议价能力呈现不同变化`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一个中性事实主题，20-35 个中文字符。
2. 开头 2-3 段：直接给出主判断、为什么现在重要、报告提供了什么新信号；自然带出 4-6 个长尾关键词，覆盖国家/行业/公司/政策/数据/技术词，但不要写成关键词堆砌。
3. 3-4 个 `##` 小节：每个小节标题都是完整的中性事实句，不是栏目名。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份经合组织研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## OECD Health Working Papers No. 197

Interoperability in healthcare: Towards an interconnected future

OECD

https://dx.doi.org/10.1787/eb71b7be-en

OECD Health Working Papers No. 197

# Interoperability in healthcare

# Towards an interconnected future

# OECD Health Working Papers

OECD Health Working Papers | OECD

This work is issued under the responsibility of the Secretary-General of the OECD and does not necessarily reflect the official views of OECD Member countries.

This document, as well as any data and map included herein, are without prejudice to the status of or sovereignty over any territory, to the delimitation of international frontiers and boundaries and to the name of any territory, city or area.

© OECD 2026

## Abstract

Interoperability in healthcare – the ability of health systems and stakeholders to securely exchange and use data – remains a longstanding yet underachieved goal in the digitalisation of health systems. This paper analyses international practices across OECD countries to support efficient, equitable, and impactful data use and sharing. Drawing on interviews, a survey, desk research, and expert consultations, the report highlights both the barriers and leading practices at the level of people, policy, processes, and technology. The report outlines opportunities at local, regional, national, and cross-border levels of health data exchange, focusing on stakeholder engagement, individual empowerment, global governance to guide interoperability efforts, collaboration, and the need for legislative foundations. The full value of interoperability is estimated to be between 2.7% and 6.6% of health expenditure annually as per OECD country estimates. Realising it requires a shift from implementation of health information systems to meet the needs of individual facilities towards implementation within an integrated digital health ecosystem centred around the patient. This shift can enable data to follow patients across the care continuum and allow for timelier reuse of data for public benefit, with protections. While technical challenges have historically been prioritised, findings suggest that interoperability is inherently a people (e.g. governance, trust, adoption) and leadership challenge and highlights an opportunity to rethink interoperability as a driver of economic growth and healthier populations. Keys to success are the establishment of trusted health data networks and sustained investment in standards, governance, and data quality to enable scalable and meaningful health system transformation.

## Résumé

L'interopérabilité en santé, c'est-à-dire la capacité des systèmes de santé et de leurs acteurs à échanger et à utiliser les données de manière sécurisée, constitue depuis longtemps un objectif majeur de la transformation numérique des systèmes de santé, mais elle n'a pas encore été pleinement réalisée. Ce document analyse les pratiques internationales au sein des pays de l'OCDE afin de soutenir une utilisation et un partage efficaces, équitables et à fort impact des données. S'appuyant sur des entretiens, une enquête, une recherche documentaire et des consultations d'experts, le rapport met en évidence les obstacles actuels, les pratiques de référence en matière de ressources humaines, de politiques publiques, de processus et de technologies, ainsi que les possibilités d'action. Le rapport présente des pistes d'action aux niveaux local, régional, national et transfrontalier pour l'échange de données de santé, en mettant l'accent sur l'implication des parties prenantes, le renforcement de leurs capacités, la gouvernance mondiale, la collaboration et la nécessité de disposer d'une base juridique solide. Réaliser pleinement la valeur de l'interopérabilité, estimée jusqu'à 6,6 % des dépenses annuelles de santé dans les pays de l'OCDE, nécessite un changement de paradigme : passer de modèles centrés sur les établissements à des systèmes centrés sur les patients. Dans ces systèmes, les données suivent le patient tout au long de son parcours et peuvent être réutilisées dans l'intérêt général, sous réserve de garanties de protection appropriées. Alors que les défis techniques et sémantiques ont historiquement été privilégiés, les résultats de ce rapport suggèrent que l'interopérabilité est intrinsèquement une question de personnes et de direction, tout en soulignant l'opportunité de la repenser comme un moteur de croissance économique et d'amélioration de la santé des populations. Les clés du succès résident dans la mise en place de réseaux de données de santé de confiance et dans des investissements durables en matière de normes, de gouvernance et de qualité des données afin de permettre une transformation des systèmes de santé à la fois évolutive et porteuse de sens.

## Acknowledgements

The work presented here was undertaken by Rachel Fellner and co-written by Yunona L'Heureux, Alina Velazquez Pelaez, and Johannes Köhr. The authors would especially like to thank Eric Sutherland, Senior Health Economist at the OECD, for his guidance in writing this paper and providing valuable recommendations, and Isaura Gutierrez Vargas, Agata Bartkowska, and Morgan Lemin for their revisions of the report. The authors would also like to thank Francesca Colombo of the Employment, Labour and Social Affairs (ELS) Division of the OECD, as well as colleagues from the Science, Technology, and Innovation (STI) Directorate for their time and contribution in reviewing this work. The authors would like to extend their gratitude to the OECD Health Committee and the many government officials, policy and technical experts across the OECD and members of the Joint Initiative Council for Global Health Informatics Standardization who participated in the interviews, provided recent literature and studies, and reviewed draft chapters. In addition, a special thank you goes to the speakers in the OECD workshop on interoperability in healthcare, Jordi Piera-Jiménez, Helen Caton-Peters, Anderson Chuck, Rachel Dunscombe, Kate Ebrill, and Markus Kalliola, who also provided valuable input to this report.

## Table of contents

OECD Health Working Papers 2
Abstract 3
Résumé 4
Acknowledgements 5
Executive Summary 10
1 What is interoperability in healthcare? 12
What is interoperability in healthcare? 13
Why interoperability matters and the people behind it 16
Objectives of this paper 17
2 Economic promise of interoperability 20
Economic benefits from implementing interoperability 21
Costs of inaction in advancing and implementing interoperability 24
3 What is the current state of interoperability? 26
Health data standards 27
Barriers for interoperability 31
Policy enablers to address interoperability 34
4 Actions to move towards a more connected future 41
Learning from other industries 41
Opportunities for action in interoperability 43
5 Towards an interoperable future 47
References 48
FIGURES
Figure 1. The European Interoperability Framework for eHealth (EIF/eHDSI) 14
Figure 2. Health Data Lifecycle 15
Figure 3. The why of Interoperability 16
Figure 4. Interoperability Tower 18

Figure 5. Estimated economic value to the UK NHS and benefit to patients 23  
Figure 6. Common Interoperability Challenges Identified by Interviewees 27  
Figure 7. Illustrative Example: The Role of Standards in Interoperability 29  
Figure 8. Interoperability Challenges 31  
Figure 9. Functional requirements for the national dataset catalogue within EHDS 39  
Figure 10. Common Interoperability Opportunities Identified by Interviewees 43  
Figure 11. Opportunities for Interoperability in Healthcare 44

## TABLES

Table 1. Benefits attributable to investing into interoperability according to the analysed papers 22  
Table 2. Health Data Standards 30  
Table 3. Concentration of policy enablers across health data exchange 35

## Acronyms and abbreviations

<table><tr><td>Acronym</td><td>Abbreviation</td></tr><tr><td>ADS-B</td><td>Automatic Dependent Surveillance - Broadcast</td></tr><tr><td>AI</td><td>Artificial Intelligence</td></tr><tr><td>APIs</td><td>Application Programming Interfaces</td></tr><tr><td>ASTM</td><td>American Society for Testing and Materials</td></tr><tr><td>C-CDA</td><td>Consolidated CDA</td></tr><tr><td>CDA</td><td>Clinical Document Architecture</td></tr><tr><td>CDIS</td><td>Clinical Data Integration Standards</td></tr><tr><td>CDISC</td><td>Clinical Data Interchange Standards Consortium</td></tr><tr><td>CDM</td><td>Common Data Model</td></tr><tr><td>CIDH</td><td>Centre for Clinical Innovation in Digital Health</td></tr><tr><td>CPR</td><td>Central Person Registry</td></tr><tr><td>CPT</td><td>Current Procedural Terminology</td></tr><tr><td>DGA</td><td>Data Governance Act</td></tr><tr><td>DICOM</td><td>Digital Imaging and Communications in Medicine</td></tr><tr><td>EDiTHA</td><td>European Digital Health Technology Assessment</td></tr><tr><td>eHDSI</td><td>eHealth Digital Service Infrastructure</td></tr><tr><td>EHDS</td><td>European Health Data Space</td></tr><tr><td>EHRs</td><td>Electronic Health Records</td></tr><tr><td>EIF</td><td>European Interoperability Framework</td></tr><tr><td>ELGA</td><td>Elektronische Gesundheitsakte</td></tr><tr><td>EMPI</td><td>Enterprise Master Patients Index</td></tr><tr><td>EMRs</td><td>Electronic Medical Records</td></tr><tr><td>EY</td><td>Ernst and Young</td></tr><tr><td>FAA</td><td>Federal Aviation Administration</td></tr><tr><td>FAFT</td><td>Financial Action Task Force</td></tr><tr><td>FAIR</td><td>Findable, Accessible, Interoperable, and Reusable</td></tr><tr><td>FHIR</td><td>Fast Healthcare Interoperability Resources</td></tr><tr><td>GDP</td><td>Gross Domestic Product</td></tr><tr><td>GDPR</td><td>European General Data Protection Regulation</td></tr><tr><td>GMDN</td><td>Global Medical Device Nomenclature</td></tr><tr><td>GNSS</td><td>Global Navigation Satellite System</td></tr><tr><td>GS1</td><td>GS1 Global Identifiers</td></tr><tr><td>HDA</td><td>Health Data Agency</td></tr><tr><td>HDRN</td><td>Health Data Research Network Canada</td></tr><tr><td>HealthDCAT-AP</td><td>Health Data Catalogue Application Profile</td></tr><tr><td>HIE</td><td>Health Information Exchange</td></tr><tr><td>HIMSS</td><td>Health Information and Management Systems Society</td></tr><tr><td>HIPAA</td><td>Health Insurance Portability and Accountability Act</td></tr><tr><td>HIS</td><td>Health Information System</td></tr><tr><td>HL7</td><td>Health Level Seven</td></tr><tr><td>ICAO</td><td>International Civil Aviation Organisation</td></tr><tr><td>ICCBBA</td><td>International Council for Commonality in Blood Banking Automation</td></tr><tr><td>ICD-10</td><td>International Statistical Classification of Diseases and Related Health Problems, 10th Edition</td></tr><tr><td>ICD-11</td><td>International Statistical Classification of Diseases and Related Health Problems, 11th Edition</td></tr><tr><td>IDEAHL</td><td>Improving Digital Empowerment for Active Healthy Living</td></tr><tr><td>IHE</td><td>Integrating the Healthcare Enterprise</td></tr><tr><td>IPS</td><td>International Patient Summary</td></tr><tr><td>ISO</td><td>International Organisation for Standardisation</td></tr><tr><td>ITU</td><td>International Telecommunication Union</td></tr><tr><td>LOINC</td><td>Logical Observation Identifier Names &amp; Codes</td></tr><tr><td>MT</td><td>Message Type</td></tr><tr><td>NDC</td><td>National Drug Code</td></tr><tr><td>NHS</td><td>National Health Services</td></tr><tr><td>NPI</td><td>National Provider ID</td></tr><tr><td>OBIE</td><td>Open Banking Implementation Entity</td></tr><tr><td>OHDSI</td><td>Observational Health Data Sciences and Informatics</td></tr><tr><td>OMOP</td><td>Observational Medical Outcomes Partnership</td></tr><tr><td>openEHR</td><td>Open Electronic Health Records</td></tr><tr><td>PaRIS</td><td>Patient-Reported Indicator Surveys</td></tr><tr><td>PGHD</td><td>Patient Generated Health Data</td></tr><tr><td>PIN</td><td>Personal Identify Number</td></tr><tr><td>R&amp;D</td><td>Research and Development</td></tr><tr><td>RxNorm</td><td>Standardized Nomenclature for Clinical Drugs</td></tr><tr><td>SDO</td><td>Standards Development Organisation</td></tr><tr><td>SDoH</td><td>Social Determinants of Health</td></tr><tr><td>SNOMED CT</td><td>Systematized Nomenclature of Medicine-Clinical Terms</td></tr><tr><td>SWIFT</td><td>Society for Worldwide Interbank Financial Telecommunication</td></tr><tr><td>TEFCA</td><td>Trusted Exchange Framework and Common Agreement</td></tr><tr><td>TEHDAS2</td><td>Second Joint Action Towards the European Health Data Space</td></tr><tr><td>UUID</td><td>Universally Unique Identifier</td></tr><tr><td>XDM</td><td>Cross-Enterprise Document Media Interchange</td></tr><tr><td>XDS</td><td>Cross-Enterprise Document Sharing</td></tr></table>

# Executive Summary

1. Interoperability – the ability of different health systems, devices, applications, or organisations to securely exchange, interpret, and use data in a coordinated and meaningful way – has been a central objective of health system digitalisation. The costs of poor interoperability are significant: diagnostic errors account for an estimated 17.5% of healthcare costs (with a proportion attributable to poor interoperability), patients report a 15% reduction in trust in the health system when asked to repeat their information, and 81.5% of physicians believe that inadequate interoperability poses a potential risk to patient safety.

2. Effective interoperability represents the opportunity to counteract these costs and support an integrated digital health infrastructure built on trusted health data networks. According to reports from Canada, Finland and the United Kingdom, the potential value of enabling health data interoperability is between 2.7% to 6.6% of health system expenditure. Value is generated through optimised service delivery, a reduction in errors, more timely treatment, faster research and development, and prevention. Despite the potential, OECD countries face systemic barriers to their realisation, including inconsistent adoption of compatible systems and standards, a lack of data stewardship, and complex processes for accessing health data.

3. The OECD conducted 41 interviews with OECD country experts and health data standards organisations, received 22 survey responses from OECD countries, performed desk research, and held a workshop to understand the enablers to the efficient, effective, and equitable sharing of quality health data. The results establish 26 policy enablers across four main areas (1) people, (2) processes, (3) policy, and (4) technology. These areas are evaluated across the layers of health data exchange: local health facilities, regional (sub-national) groups, national practices, and cross-border collaboration. These collectively are referenced as the Tower of Interoperability.

4. A key finding highlights efforts to date in technical and semantic areas have failed to address legal and operational barriers. The opportunity to achieve interoperability is to focus on people-centred actions that can facilitate a culture of interoperable health data use and re-use to drive activities toward interoperable systems. Actions can start with a progression from a shared mindset to the development of the necessary skillset, followed by the deployment of appropriate toolsets.

## Current state of interoperability

5. While countries have reached varying levels of health data exchange capability, barriers persist. The most prevalent barriers mentioned by interviewees were incompatible data sharing practices and inconsistent practices for de-identification (70.59%), infrastructure and technical fragmentation across regions (66.67%), and fragmented governance and institutional coordination (60.78%). Other themes also emerged:

\- Insufficient buy-in for a unified framework for interoperability due to unaddressed concerns, inconsistent legislation, fragmented governance, and varying mandates influenced by industry interests.

\- A gap between vision and implementation, with too much emphasis on theory over practical action.

\- Cultural hesitancy and limited trust in the effectiveness, return on investment (ROI), and scalability of digital health investments.

\- Inconsistent workforce capacity, literacy, and buy-in to effectively adopt interoperability initiatives.

6. OECD member countries are advancing practices to address these challenges.

\- People: Efforts focus on educating, engaging, and empowering stakeholders, including healthcare providers, industry, policymakers, and patients, to understand their role in ensuring quality health data. France and Denmark are enhancing public trust through transparent citizen engagement and data-use practices, while Australia is investing in a people-centred approach to national standards development and adoption.

\- Processes: A focus on governance, with 32% of survey countries having implemented a national strategy or roadmap for health data standards adoption, 50% having national bodies responsible for standards adoption and use, and 55% using national processes or legislation to influence vendor compliance with interoperability requirements. Cross-border data exchange is increasing, with 45% of countries engaged in bilateral international collaborations and 75% having established trusted health data networks.

\- Policies: Regulatory frameworks and legislation are a foundation to successful interoperability efforts; however, only 23% of surveyed countries report legislation mandating standards-based health data exchange. Countries are strengthening enablers, including cross-border data sharing (e.g. the European Health Data Space), the secondary use of health data (e.g. Finland's Act on the Secondary Use of Health and Social Data), and prevention of data blocking (e.g. the United States' 21st Century Cures Act).

\- Technology: All countries surveyed are using health data standards, with 41% relying exclusively on international standards. The standards landscape is extensive, with 28 standards identified, spanning vocabulary, content structure, communication, privacy and security, and identifiers. Implementation gaps remain, with 27% of respondents having fully implemented a set of procedures to assess and ensure the quality of health data collection, and 23% having fully implemented procedures for cataloguing significant health data assets.

7. These measures support the ability to incentivise interoperable health systems and highlight trends in the application of relevant processes – but do not account for the use of personal health data for appropriate purposes with necessary protections. Future work will be to evaluate the legitim

[中间内容因长度限制已省略]

itra (2025), VALO – Value from Nordic health data, https://www.sitra.fi/en/projects/valo-value-from-nordic-health-data/ (accessed on 1 December 2025). [70]

Slawomirski, L. et al. (2025), “The economics of diagnostic safety”, OECD Health Working Papers, No. 176, OECD Publishing, Paris, https://doi.org/10.1787/fc61057a-en. [30]

SNOMED (2025), What is SNOMED CT | SNOMED International, https://www.snomed.org/what-is-snomed-ct (accessed on 25 August 2025).

Sosiaali- ja terveysministerio (2019), Act on the Processing of Client Data in Social and Health Care, https://stm.fi/-/sosiaali-ja-terveydenhuollon-toimijoita-ohjeistetaan-kyberturvallisuudesta (accessed on 1 July 2025).

Sparked (2026), Shaping the future of Australian healthcare, https://sparked.csiro.au/, https://sparked.csiro.au/ (accessed on 12 January 2026).

Sparked (2025), Sparked, https://sparked.csiro.au/ (accessed on 6 May 2025).

sundhed.dk (2026), Background, https://www.sundhed.dk/borger/service/om-sundheddk/om-organisationen/ehealth-in-denmark/background/ (accessed on 12 January 2026). [115]

Sutherland, E. et al. (2023), “Fast-Track on digital security in health”, OECD Health Working Papers, No. 164, OECD Publishing, Paris, https://doi.org/10.1787/c3357f9f-en. [171]

Tamayo-Sarver, J. (2025), From Chaos to Clarity: Solving Interoperability Challenges at the Front End, Medium, https://inflecthealth.medium.com/from-chaos-to-clarity-solving-interoperability-challenges-at-the-front-end-bf7e1276ddf1 (accessed on 19 December 2025).

TEHDAS2 (2025), TEHDAS2 publishes a technical blueprint for national metadata catalogues to power EHDS - Tehdas, https://tehdas.eu/results/tehdas2-publishes-technical-blueprint-for-national-metadata-catalogues-to-power-ehds/ (accessed on 28 May 2026).

The Canadian Medical Protective Association (2022), Managing access to electronic health records, https://www.cmpa-acpm.ca/en/advice-publications/browse-articles/2013/managing-access-to-electronic-health-records (accessed on 16 January 2026). [172]

The Commonwealth Fund (2025), Denmark | International Health Care System Profiles | Commonwealth Fund, https://www.commonwealthfund.org/international-health-policy-center/countries/denmark (accessed on 18 August 2025).

The European Medical Device Regulation (2017), “REGULATION (EU) 2017/ 745 OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL - of 5 April 2017 - on medical devices, amending Directive 2001/ 83/ EC, Regulation (EC) No 178/ 2002 and Regulation (EC) No 1223/ 2009 and repealing Council Directives 90/ 385/ EEC and 93/ 42/ EEC”, https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32017R0745 (accessed on 8 July 2025).

The International Patient Summary (2025), The International Patient Summary – key health data, worldwide, https://international-patient-summary.net/ (accessed on 7 May 2025). [5]

Touré, V. et al. (2023), “FAIRification of health-related data using semantic web technologies in the Swiss Personalized Health Network”, Scientific Data, Vol. 10/1, https://doi.org/10.1038/s41597-023-02028-y.

Tsafnat, G. et al. (2024), “Converge or Collide? Making Sense of a Plethora of Open Data Standards in Health Care”, Journal of Medical Internet Research, Vol. 26, https://doi.org/10.2196/55779 (accessed on 19 December 2025).

U.S. Congress (2016), “H.R.34 - 114th Congress (2015-2016): 21st Century Cures Act”, https://www.congress.gov/bill/114th-congress/house-bill/34 (accessed on 4 February 2026).

U.S. Space Force (2025), GPS.gov: International Cooperation, https://www.gps.gov/policy/cooperation/ (accessed on 4 August 2025).

United Nations Office for Outer Space Affairs (2026), Global Navigation Satellite Systems, [65] https://www.unoosa.org/oosa/en/ourwork/topics/gnss.html (accessed on 4 February 2026).

University of Eastern Finland (2025), Cross-border ePrescription is perceived to improve access to medicines, https://medicalxpress.com/news/2025-04-border-eprescription-access-medicines.html, https://medicalxpress.com/news/2025-04-border-eprescription-access-medicines.html. [100]

van Drumpt, S. et al. (2025), “Secondary use under the European Health Data Space: setting the scene and towards a research agenda on privacy-enhancing technologies”, Frontiers in Digital Health, Vol. 7, p. 1602101, https://doi.org/10.3389/FDGTH.2025.1602101/FULL.

Volg je zorg (2025), About permissions, https://www.volqjezorg.nl/en (accessed on 15 January 2026). [116]

Wamala Andersson, S. and M. Gonzalez (2025), “Digital health literacy—a key factor in realizing the value of digital transformation in healthcare”, Frontiers in Digital Health, Vol. 7, p. 1461342, https://doi.org/10.3389/FDGTH.2025.1461342/BIBTEX.

Ward, C. (2023), Physician Burnout is a Data Problem, https://www.particlehealth.com/blog/physician-burnout-is-a-data-problem, https://www.particlehealth.com/blog/physician-burnout-is-a-data-problem (accessed on 19 January 2026).

Wayman, C. and N. Hunerlach (2019), Realising the value of health care data: a framework for the future, EY, https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/insights/life-sciences/documents/ey-value-of-health-care-data-v20-final.pdf (accessed on 20 January 2026).

WHO (2022), Regional digital health action plan for the WHO European Region 2023–2030 [83] (RC72), https://www.who.int/europe/publications/i/item/EUR-RC72-5 (accessed on 14 December 2025).

World Economic Forum (2024), Data and trust: the two pillars of value-based healthcare | World Economic Forum, https://www.weforum.org/stories/2024/01/value-based-healthcare-data-trust/ (accessed on 11 March 2026).

Xpanding innovative Alliance (2025), XiA, a groundbreaking initiative in digital health!, https://xia-project.iscte-iul.pt/. [117]
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
9. 输出前自行核对：标题与导语不重复；主标题和每个小标题都是完整、中性的事实表达，不评价好坏、不制造冲突；没有元话语、推广语和未解问题栏目。只输出最终 Markdown，不输出核对过程。
