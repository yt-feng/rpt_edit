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
# RECENT POLICY DEVELOPMENTS ON AI IN THE LABOUR MARKET

OECD ARTIFICIAL
INTELLIGENCE PAPERS
July 2026 No. 63

OECD Artificial Intelligence Papers

# Recent policy developments on AI in the labour market

## Disclaimers

This work is issued under the responsibility of the Secretary-General of the OECD and does not necessarily reflect the official views of OECD Member countries.

This document, as well as any data and map included herein, are without prejudice to the status of or sovereignty over any territory, to the delimitation of international frontiers and boundaries and to the name of any territory, city or area.

Cover image: © Kjpargeter/Shutterstock.com

© OECD 2026

![](images/ad729902a48894a7478f0bfb3204b7bccfd1fed27497dfc5834837649669eada.jpg)

## Attribution 4.0 International (CC BY 4.0)

This work is made available under the Creative Commons Attribution 4.0 International licence. By using this work, you accept to be bound by the terms of this licence (https://creativecommons.org/licenses/by/4.0).

Attribution – you must cite the work.

Translations – you must cite the original work, identify changes to the original and add the following text: In the event of any discrepancy between the original work and the translation, only the text of original work should be considered valid.

Adaptations – you must cite the original work and add the following text: This is an adaptation of an original work by the OECD. The opinions expressed and arguments employed in this adaptation should not be reported as representing the official views of the OECD or of its Member countries.

Third-party material – the licence does not apply to third-party material in the work. If using such material, you are responsible for obtaining permission from the third party and for any claims of infringement.

You must not use the OECD logo, visual identity or cover image without express permission or suggest the OECD endorses your use of the work.

Any dispute arising under this licence shall be settled by arbitration in accordance with the Permanent Court of Arbitration (PCA) Arbitration Rules 2012. The seat of arbitration shall be Paris (France). The number of arbitrators shall be one.

# Recent policy developments on AI in the labour market

Artificial intelligence (AI) is increasingly shaping labour markets, bringing both significant opportunities and risks for workers, firms and societies, and making it a growing policy priority. This publication reviews recent policy measures related to AI in the labour market in G7 countries, the European Union and selected Latin American economies across six policy areas: automation, productivity, skills and opportunities; privacy and data protection; non-discrimination; occupational safety and health; transparency, explainability and accountability; and social dialogue. Across most policy areas, AI-related issues are primarily addressed through existing labour market policy frameworks, rather than through stand-alone AI policies. Policies explicitly targeted at AI in the labour market are most developed for AI skills and adoption, while measures and guidance are still emerging in other policy areas, particularly privacy, transparency and accountability.

Keywords: Artificial Intelligence, Employment.
JEL Codes: J2, J5, J7, J8, M1, M5.

L'intelligence artificielle (IA) imprime de plus en plus fortement sa marque sur les marchés du travail, apportant des possibilités, mais aussi des risques, pour les travailleurs, les entreprises et les sociétés, et s'impose de ce fait comme une priorité pour les pouvoirs publics. La présente publication passe en revue les récentes mesures de politique publique en rapport avec l'IA sur le marché du travail que les pays du G7, l'Union européenne et quelques économies d'Amérique latine ont prises dernièrement dans six domaines, à savoir : l'automatisation, la productivité, les compétences et l'inclusivité ; la protection de la vie privée et des données ; la non-discrimination ; la sécurité et la santé au travail ; la transparence, l'explicabilité et la responsabilité ; le dialogue social. Dans la plupart de ces domaines, les questions touchant à l'IA sont traitées principalement dans le périmètre des cadres d'action applicables au marché du travail préexistants au lieu de faire l'objet de mesures spécifiques. Les dispositifs les plus aboutis visant explicitement l'IA sur le marché du travail ont trait aux compétences requises et à l'adoption de l'IA ; dans d'autres domaines, en particulier la protection de la vie privée, la transparence et la responsabilité, la définition de mesures reste à un stade plus précoce.

Künstliche Intelligenz (KI) prägt die Arbeitsmärkte zunehmend und bringt sowohl wichtige Chancen als auch Risiken für Arbeitnehmer, Unternehmen und die Gesellschaft insgesamt mit sich, und wird damit zu einer wachsenden politischen Priorität. Diese Veröffentlichung gibt einen Überblick über jüngste politische Maßnahmen im Zusammenhang mit KI auf den Arbeitsmärkten in den G7-Ländern, der Europäischen Union sowie ausgewählten lateinamerikanischen Volkswirtschaften in sechs Politikfeldern: Automatisierung, Produktivität, Kompetenzen und Inklusion; Privatsphäre und Datenschutz; Nichtdiskriminierung; Sicherheit und Gesundheitsschutz am Arbeitsplatz; Transparenz, Erklärbarkeit und Rechenschaftspflicht sowie Sozialdialog. In den meisten dieser Politikfelder werden KI-bezogene Themen statt durch eigenständige, KI-spezifische Strategien vorwiegend im Rahmen bestehender arbeitsmarktpolitischer Instrumente behandelt. Politische Maßnahmen, die sich ausdrücklich auf KI im Arbeitsmarkt beziehen, sind in den Bereichen Kompetenzen und Einführung von KI am weitesten fortgeschritten, während sich Maßnahmen und Leitlinien in anderen Bereichen – insbesondere hinsichtlich Datenschutz, Transparenz und Rechenschaftspflicht – noch in der Entwicklung befinden.

# Acknowledgements

This publication contributes to the OECD's Artificial Intelligence in Work, Innovation, Productivity and Skills (AI-WIPS) programme, which provides policymakers with new evidence and analysis to keep abreast of the fast-evolving changes in AI capabilities and diffusion and their implications for the world of work. The programme aims to help ensure that adoption of AI in the world of work is effective, beneficial to all, people-centred and accepted by the population at large. AI-WIPS is supported by the German Federal Ministry of Labour and Social Affairs (BMAS) and will complement the work of the German AI Observatory in the Ministry's Policy Lab Digital, Work & Society. For more information, visit https://oecd.ai/work-innovation-productivity-skills and https://denkfabrik-bmas.de/.

This work was carried out by Annikka Lemmens under the supervision of Angelica Salvi Del Pero in the OECD Directorate for Employment, Labour and Social Affairs. The report benefited from comments by colleagues in the Directorate for Employment, Labour and Social Affairs, including Glenda Quintini and Stijn Broecke from the Skills and Future Readiness Division, Sandrine Cazes from the Jobs and Income Division, as well as colleagues Giuseppe Bianco, Celine Caira, Sergi Gálvez Duran, Christina Michelakaki, Christian Reimsbach-Kounatze, and Limor Shmerling Magazanik in the Directorate for Science, Technology and Innovation.

The report also benefited from inputs provided by delegates to the OECD Employment, Labour and Social Affairs Committee (ELSAC) and by representatives of Business at OECD (BIAC) and the Trade Union Advisory Committee to the OECD (TUAC).

![](images/7cd6bdc60c646aad3bdf62aa7ad4fd426531b20a23c1ac3796863db74921b4cd.jpg)

Federal Ministry

of Labour and Social Affairs

## Table of contents

Résumé 4
Abstract 5
Acknowledgements 6
Executive summary 9
Synthèse 11
Zusammenfassung 13
1 Introduction 15
2 Automation, productivity, skills and opportunities 16
Monitoring the impact of AI on the labour market 17
Encouraging the use of AI 18
Skills development 20
Other types of support and AI in employment services 21
3 Privacy and data protection 23
Privacy and data protection frameworks 23
Assessments and certification 27
Security measures and privacy safeguards 27
Promoting compliance 28
4 Non-discrimination in the labour market 30
AI tools to prevent discrimination and promote accessibility 31
Non-discrimination frameworks 31
Assessments, audits, data quality management, certification and training 32
Promoting compliance 35
5 Occupational Safety and Health 36
Promoting the development of AI tools for OSH 36
Monitoring the impact of AI on OSH 37
OSH framework 37
Risk assessments, certification, and raising awareness 38
Promoting compliance 38

## 8

6 Transparency, explainability and accountability 39  
Transparency, explainability, accountability frameworks 39  
Human oversight, pathways for redress, and traceability 41  
Promoting compliance 43  

7 Social dialogue 44  
Promoting social dialogue 44  
Ensuring social partners' AI expertise 48  

8 Policy directions 50  

References 51  

Notes 63

## FIGURES

Figure 1. G7 countries use a range of policy measures to monitor AI's impacts, promote adoption, and support workers 17  
Figure 2. All G7 countries recommend or require measures to address bias and discrimination 30

## TABLES

Table 1. Common principles guiding the use of data in the workplace 25
Table 2. The involvement of workers in OSH is recommended or required in all jurisdictions, but their input is not always needed for the introduction of new technologies 47

# Executive summary

As artificial intelligence (AI) technologies become increasingly embedded in the workplace and labour markets, ensuring their trustworthy and responsible use so as to foster their benefits while addressing possible risks, is a policy priority for many countries. This paper provides a comparative review of policy measures recently adopted in G7 countries and at the EU level, as well as in some Latin American countries (Chile, Colombia, Costa Rica, and Mexico) combining information gathered through desk research, information collected through a dedicated questionnaire to G7 countries and the EU, and exploratory work using AI prompt engineering.

The review covers six broad policy areas that, in line with the OECD AI Principles, are identified as priority for the use of AI in the labour market in OECD work as well as by the G7 Action plan for a human-centred development and use of safe, secure and trustworthy AI in the World of Work. These areas are: (1) automation, productivity, skills and opportunities; (2) privacy and data protection; (3) non-discrimination; (4) occupational safety and health; (5) transparency, explainability and accountability; and (6) social dialogue.

The review finds that all surveyed countries promote AI adoption through broad national strategies, often complemented by research and experimental initiatives, including regulatory sandboxes, to build knowledge and test new approaches. Nearly all surveyed countries provide targeted support for small and medium-sized enterprises (SMEs), for example through financial incentives and training opportunities delivered at the national or regional level. Several countries have established observatories dedicated to AI in the workplace, providing targeted insights into emerging challenges and helping to identify trends at an early stage. To assist workers displaced by AI, countries tend to rely on standard employment support policies and social protection not targeted on AI. Relatively few measures are directed at workers who remain in employment but are at high risk of AI-related disruption, although some promising examples are emerging. All surveyed countries provide reskilling and upskilling programmes, sometimes developed in partnership with private sector actors. Most programmes focus on technical skills, not on general AI literacy. Governments are also increasingly using AI in public employment services to personalise assistance and improve job matching.

In the areas of privacy, data protection, non-discrimination and occupational safety and health, countries covered in this publication are, first of all, making use of existing frameworks to ensure that the adoption and use of AI in the labour market takes place in a trustworthy way. Many provide additional guidance and tools to clarify how these frameworks apply in practice, for example through workshops, guidelines or self-check instruments that help employers understand their obligations. In addition, some countries and jurisdictions are introducing new laws to address these issues. Across these areas, risk assessments are recommended or required by all countries surveyed, while certifications, audits and security measures are also widely recommended or required.

Surveyed countries are also advancing policies to promote transparency, explainability and accountability when AI systems are used in the workplace. In most surveyed countries, employers are required or encouraged to share information about the use of AI with workers, in others also with job applicants, and in a few cases, there are explicit rules for platform workers. Human oversight and traceability are other important accountability measures that are highlighted in the majority of frameworks that, in several countries, are supported by designated roles for oversight, clear pathways for contesting decisions, and documentation or logging requirements to enable review.

Surveyed countries promote social dialogue on AI in the labour market mainly through collaboration with social partners in shaping national policies, consultation and representation mechanisms at company level (especially on Occupational Safety and Health), and the negotiation of collective bargaining agreements. Relatively few countries are investing in building AI expertise among social partners.

Looking ahead, some policy areas could benefit from further development. For example, the implications of data protection and privacy frameworks for workers and for AI systems in the labour market are not always clearly defined or explained to employers. Transparency, explainability and accountability often remain at the level of broad principles in AI strategies. More detailed and practical guidance could help employers and workers apply these principles in practice, for instance through sector-specific examples, case studies or self-assessment tools. Social dialogue and collective bargaining can help address practical challenges linked to the use of AI in the labour market and support compliance. With time, countries will also benefit from evaluating existing policy measures and assessing whether existing government guidance is used effectively and succeeds in improving workplace outcomes.

À l'heure où les technologies d'intelligence artificielle (IA) tendent à se faire de plus en plus présentes sur les lieux de travail et sur les marchés du travail, veiller à ce qu'elles soient employées de manière responsable et digne de confiance afin d'en maximiser les avantages et d'en maîtriser les risques éventuels devient une priorité stratégique pour de nombreux pays. Le présent document contient une étude comparative des mesures prises dernièrement par les pays du G7 et par l'Union européenne, ainsi que par quelques pays d'Amérique latine (Chili, Colombie, Costa Rica et Mexique), à partir d'informations réunies dans le cadre de recherches documentaires, de renseignements recueillis à l'aide d'un questionnaire spécifique adressé aux pays du G7 et à l'UE et de travaux exploratoires ayant fait appel à l'ingénierie des requêtes.

L'étude porte sur six grands aspects intéressant l'action des pouvoirs publics et considérés comme prioritaires dans le cadre des travaux que l'OCDE consacre à l'utilisation de l'IA sur le marché du travail, conformément à ses Principes sur l'IA ainsi qu'au Plan d'action du G7 en faveur d'une IA centrée sur l'humain, sûre et digne de confiance dans le monde du travail. Ces aspects sont les suivants : 1) automatisation, productivité, compétences et inclusivité ; 2) protection de la vie privée et des données ; 3) non-discrimination ; 4) sécurité et santé au travail ; 5) transparence, explicabilité et responsabilité ; 6) dialogue social.

Il ressort de cette étude que tous les pays étudiés soutiennent l'adoption de l'IA au moyen de vastes stratégies nationales souvent complétées par des travaux de recherche et des initiatives expérimentales, notamment des bacs à sable réglementaires, pour réunir de nouvelles connaissances et tester de nouvelles approches. Pratiquement tous les pays étudiés ont apporté une aide ciblée aux petites et moyennes entreprises (PME), sous forme, par exemple, d'incitations financières et de formations proposées à l'échelon national ou régional. Plusieurs pays ont créé un observatoire de l'IA sur le lieu de travail, qui apporte des éclairages précis sur les nouveaux enjeux qui se profilent et aide à déceler les nouvelles tendances dès un stade précoce. Pour accompagner les travailleurs que l'IA remplace, les pays tendent à faire appel à des mesures classiques de soutien à l'emploi et de protection sociale qui ne sont pas spécifiques à l'IA. Il existe relativement peu de dispositifs à l'intention des travailleurs qui ont conservé leur emploi, mais demeurent fortement exposés aux perturbations causées par l'IA, même si quelques exemples prometteurs commencent à venir au jour. Tous les pays étudiés disposent de programmes de reconversion et de perfectionnement des compétences, définis parfois en partenariat avec des acteurs du secteur privé. La plupart de ces programmes s'articulent autour de compétences techniques et non sur la maîtrise de l'IA de manière générale. Les pouvoirs publics font par ailleurs un usage croissant de l'IA dans le cadre des services publics de l'emploi afin de personnaliser l'accompagnement et d'améliorer l'adéquation entre l'offre et la demande d'emploi.

S'agissant de la protection de la vie privée et des données, de la non-discrimination et de la sécurité et santé au travail, pour faire en sorte que l'adoption et l'utilisation de l'IA sur le marché du travail se déroulent d'une manière qui inspire confiance, les pays étudiés dans la présente publication ont recours, en premier lieu, aux cadres existants. Beaucoup fournissent des directives et des outils supplémentaires afin de préciser comment appliquer ces cadres en pratique, par exemple à l'occasion d'ateliers ou sous forme de lignes directrices et d'instruments d'autoévaluation aidant les employeurs à comprendre quelles sont leurs obligations. Quelques pays et territoires adoptent en outre de nouvelles lois pour s'o

[中间内容因长度限制已省略]

s”, OECD Artificial Intelligence Papers, No. 38, OECD Publishing, Paris, https://doi.org/10.1787/a266160b-en.

OECD (2024), Algorithm and Eve: How AI will impact women at work, OECD Publishing, Paris, [12] https://doi.org/10.1787/a1603510-en.

OECD (2024), Recommendation of the Council on Artificial Intelligence, https://legalinstruments.oecd.org/en/instruments/oecd-legal-0449 (accessed on 2025).

OECD (2024), Training Supply for the Green and AI Transitions: Equipping Workers with the Right Skills, Getting Skills Right, OECD Publishing, Paris, https://doi.org/10.1787/7600d16d-en. [60]

OECD (2024), “Using AI in the workplace: Opportunities, risks and policy responses”, OECD Artificial Intelligence Papers, No. 11, OECD Publishing, Paris, https://doi.org/10.1787/73d417f9-en.

OECD (2023), “Emerging privacy-enhancing technologies: Current regulatory and policy approaches”, OECD Digital Economy Papers, No. 351, OECD Publishing, Paris, https://doi.org/10.1787/bf121be4-en.

OECD (2023), OECD Employment Outlook 2023: Artificial Intelligence and the Labour Market, OECD Publishing, Paris, https://doi.org/10.1787/08785bba-en. [3]

OECD (2023), OECD Privacy Guidelines Implementation Guidance: Foreword and Chapter on Accountability, https://one.oecd.org/document/DSTI/CDEP/DGP(2022)8/FINAL/en/pdf. [105]

OECD (2023), OECD Science, Technology and Innovation Outlook 2023: Enabling Transitions in Times of Disruption, OECD Publishing, Paris, https://doi.org/10.1787/0b55736e-en.

OPC (2025), OPC's Guide to the Privacy Impact Assessment Process, https://www.priv.gc.ca.

OPC (2025), Privacy in the Workplace, https://www.priv.gc.ca/.

OPC (2023), Protecting Employee Privacy in the Modern Workplace, https://www.priv.gc.ca.

OSHA (n.d.), Recommended Practices for Safety and Health Programs, https://www.osha.gov/safety-management/worker-participation (accessed on January 2026).

Pattison Media and Unifor (2024), Collective Agreement, https://negotech.service.canada.ca/eng/agreements/03/0396613a.pdf.

Prefina (2025), Bando ISI INAIL: Incentivi per Sicurezza e Innovazione delle Imprese, https://www.prefina.it/bando-isi-inail/ (accessed on September 2025).

Research Impact Canada (2023), "FSC Community of Practice", https://researchimpact.ca/about-us/future-skills-cop/.

Salvi Del Pero, A., P. Wyckoff and A. Vourc'h (2022), "Using Artificial Intelligence in the workplace: What are the main ethical risks?", OECD Social, Employment and Migration Working Papers, No. 273, OECD Publishing, Paris, https://doi.org/10.1787/840a2d9f-en.

Scale AI (2025), Who we are, http://scaleai.ca/about-us/.

SIC (2024), Circular Externa 2 de la Superintendencia de Industria y Comercio "Lineamientos sobre el Tratamiento de Datos personales en Sistemas de Inteligencia Artificial".

Soler Garrido, J. et al. (2024), Harmonised Standards for the European AI Act, https://ideas.repec.org/p/ipt/iptwpa/jrc139430.html.

Subsidy and Grant Adoption Support (2025), 4 Recommended Subsidies for Small and Medium-Sized Enterprises to Implement AI, https://hojokin-joseikin.com.

The Alan Turing Institute (2024), AI Standards Hub, https://aistandardshub.org/.

The Labour Party (2024), Labour's plan to make work pay - Delivering a new deal for working people, https://labour.org.uk.

Todolí-Signes, A. (2021), "Making algorithms safe for workers: occupational risks associated with work managed by artificial intelligence", Transfer: European Review of Labour and Research, Vol. 27/4, pp. 433-452, https://doi.org/10.1177/10242589211035040.

Touzet, C. (2023), "Using AI to support people with disability in the labour market: Opportunities and challenges", OECD Artificial Intelligence Papers, No. 7, OECD Publishing, Paris, https://doi.org/10.1787/008b32b7-en.

UK Government (2025), Guidance Data (Use and Access) Act factsheet: UK GDPR and DPA, https://www.gov.uk.

UK Government (2025), Tech giants join government to kick off plans to boost British worker AI skills, https://www.gov.uk.

UK Government (2025), Unit for Future Skills, https://www.gov.uk. [24]
UK Government (2024), £1.5 Million investment to improve in-work health services, https://www.gov.uk/. [159]
UK Government (2024), AI Management Essentials tool, https://www.gov.uk. [194]
UK Government (2024), Introduction to AI assurance, https://www.gov.uk/. [139]
UK Government (2024), Responsible AI in Recruitment guide, https://www.gov.uk. [89]
UK government (2024), AI Upskilling fund: (closed to applications), https://www.gov.uk/government/publications/flexible-ai-upskilling-fund. [45]
US Department of Labor (2025), America's Talent Strategy: Building the Workforce for the Golden Age, https://www.dol.gov. [64]
US Department of Labor (2025), US Department of Labor awards \$86 million to 14 states for investment in skills training programs for critical in-demand, emerging industries, https://www.dol.gov. [63]
WEC Europe (2025), Artificial Intelligence and algorithmic management, https://wecglobal.org/uploads/2025/09/WEC-Europe-position-paper-on-AI-at-Work.pdf. [202]
Whincup, D. (2017), Practical Guide to the GDPR - Part 6, https://www.employmentlawworldview.com. [99]
Yo, O. (2023), Japan's Regulatory Sandbox, https://www.cas.go.jp. [32]
Zimmermann, A. and L. Kalhoff (2017), Germany: Employee Monitoring by Keylogger Permitted only in Exceptional Cases, https://blogs.orrick.com. [97] $^{1}$ Electronic monitoring refers for example to the use of digital tools to track workers' activities or performance, for example through keylogging (recording all keys struck on a keyboard), screen capture, internet or email monitoring, or location tracking. Biometric tools draw on inputs such as fingerprints, iris, voice, face, or even walking style.
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
