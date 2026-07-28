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
Educational Research and Innovation

# A Conceptual Foundation for the Development of a Lifelong Learning Measurement Framework

![](images/f0e391a50e0e17077b1cb6e5865528008af238867dcc8440b680a5091429cbfc.jpg)

## A Conceptual Foundation for the Development of a Lifelong Learning Measurement Framework

This work is issued under the responsibility of the Secretary-General of the OECD, and does not necessarily reflect the official views of OECD Member countries.

This document, as well as any data and map included herein, are without prejudice to the status of or sovereignty over any territory, to the delimitation of international frontiers and boundaries and to the name of any territory, city or area.

Please cite this publication as:
OECD (2026), A Conceptual Foundation for the Development of a Lifelong Learning Measurement Framework, Educational Research and Innovation, OECD Publishing, Paris, https://doi.org/10.1787/27e5a619-en.

ISBN 978-92-64-87701-6 (print)
ISBN 978-92-64-94405-3 (PDF)
ISBN 978-92-64-66732-7 (HTML)

Educational Research and Innovation
ISSN 2076-9660 (print)
ISSN 2076-9679 (online)

Photo credits: Cover © ESB Professional/Shutterstock.com.

Corrigenda to OECD publications may be found at: https://www.oecd.org/en/publications/support/corrigenda.html.
© OECD 2026

![](images/c0f16efe63c642ba6628ca60ce37ad575ffb93134db7156374632e5d55092b2c.jpg)

## Attribution 4.0 International (CC BY 4.0)

This work is made available under the Creative Commons Attribution 4.0 International licence. By using this work, you accept to be bound by the terms of this licence (https://creativecommons.org/licenses/by/4.0/).

Attribution – you must cite the work.

Translations – you must cite the original work, identify changes to the original and add the following text: In the event of any discrepancy between the original work and the translation, only the text of the original work should be considered valid.

Adaptations – you must cite the original work and add the following text: This is an adaptation of an original work by the OECD. The opinions expressed and arguments employed in this adaptation should not be reported as representing the official views of the OECD or of its Member countries.

Third-party material – the licence does not apply to third-party material in the work. If using such material, you are responsible for obtaining permission from the third party and for any claims of infringement.

You must not use the OECD logo, visual identity or cover image without express permission or suggest the OECD endorses your use of the work.

Any dispute arising under this licence shall be settled by arbitration in accordance with the Permanent Court of Arbitration (PCA) Arbitration Rules 2012. The seat of arbitration shall be Paris (France). The number of arbitrators shall be one.

# Foreword

Today's policy challenges – from AI-driven labour market change to demographic ageing and social cohesion – depend on people's capacity to learn continuously. Yet our international data collections on lifelong learning still provide only fragmented snapshots. Educational surveys rarely follow learners across the life course or connect with adult learning surveys. As for adult learning surveys, they concentrate on certain age groups, particularly adults between 25 and 64, overlook learning before and after those years, rely largely on cross-sectional surveys, and privilege labour-market outcomes over broader benefits such as health, civic participation and wellbeing. Most importantly, they struggle to capture where learning increasingly takes place: in workplaces, families, communities and digital environments.

The instinctive response is often to ask for better surveys or more indicators. That is necessary, but insufficient. What is needed is a different conceptual lens. Rather than treating lifelong learning as an extension of formal education, we should start from the premise that learning occurs across the life course and across many contexts, only some of which are institutionalised. Schools and universities remain important, but they are only one part of a much larger learning ecosystem.

This is why the conceptual framework proposed in this report deserves attention even beyond its immediate recommendations. It reframes lifelong learning around learning systems rather than education systems, and argues that measurement should follow this broader perspective. By organising analysis around the interaction between the demand for learning, the supply of learning opportunities and the mechanisms that coordinate the two, it shifts the focus from educational participation and its learning outcomes to understanding how societies enable people to keep learning throughout their lives.

Such a shift stretches beyond what current statistical systems can readily deliver. But that should not be seen as a weakness. Blue-sky thinking has an important role in public policy: conceptual frameworks often shape what becomes measurable tomorrow. International statistics have repeatedly evolved by first redefining what matters before building the instruments to observe it. This report seeks to do the same for lifelong learning.

It offers practical directions rather than a fixed blueprint. Extending surveys across the full life course, linking longitudinal datasets, integrating administrative records, developing portable learning records and exploiting new analytical techniques all represent plausible pathways towards a richer evidence base. None will be straightforward. But feasibility should not constrain the underlying vision of what societies need to know if they are to govern learning effectively. Only by making learning visible across the life course can countries know whether they are truly becoming lifelong learning societies.

## Abstract

This report proposes a conceptual framework for measuring lifelong learning (LLL) understood as learning across the life course and diverse contexts, aimed at improving policy design and evaluation. It identifies key limitations in current data systems, including narrow age coverage, lack of longitudinal tracking, overemphasis on labour-market outcomes, and insufficient measurement of informal learning. To address these gaps, the framework is structured around three interconnected pillars: demand, supply, and coordination. Demand captures learning needs at individual, organisational, and societal levels; supply maps opportunities across formal education, workplaces, welfare systems, and communities; and coordination focuses on mechanisms that align needs with provision. The framework also redefines learning by introducing a two-dimensional model based on formalisation and digitalisation, better capturing hybrid and emerging forms. Finally, it outlines practical steps for implementation, including improved surveys, longitudinal data linkages, administrative data integration, skills passports, and advanced analytics to support more comprehensive and effective lifelong learning systems.

# Acknowledgments

Richard Desjardins (University of California, Los Angeles, United States) and Jan Kalenda (Tomas Bata University, Czechia) authored this report. It is an output of a Center for Educational Research and Innovation (CERI) “Agility and Innovation” project. Stéphan Vincent-Lancrin, Senior Education Economist and Deputy Head of the Innovation and Measuring Progress division at the OECD Directorate for Education and Skills, led the project and edited the report.

The topic of the project was selected by the CERI Governing Board upon the proposition of a member country. Agility and innovation projects are requested to come up with a report that cast initial light on the topic in a short period of time.

The development of the report benefited from two expert meetings that were held on 23 May and 19 September: the first one provided advice on the scope of the work while the second one discussed an initial version of the report. The following experts are thankfully acknowledged for their contributions to defining the scope of the paper and for providing oral and written feedback on its first draft: Ellen Boeren (University of Glasgow, United Kingdom); Satya Brink (Jönköping University, Sweden); Francesca Borgonovi (OECD); Alex Gordon (Australia); Petya Illieva (Bulgarian Academy of Science, Bulgaria); Hyerim Kim (OECD); Ann-Charlott Larsson (Statistics Sweden, Sweden); Alexandra Loannidou (German Institute for Adult Learning, Germany); Marco Paccagnella (OECD); Teresa Parsons (Canada); Glenda Quintini (OECD); Gara Rojas Gonzalez (OECD); Josef Schrader (German Institute for Adult Learning, Germany); Thomas Schuller (Independent scholar, former Head of CERI); Bart Staats (OECD); Claudia Tamassia (OECD); Quentin Vidal (OECD); Emanuel Von Erlach (Office fédéral de la statistique, Switzerland); Yixi Wang (OECD).

A revised draft was then commented at the November 2025 meeting of the CERI Governing Board. CERI GB members are thanked for their insightful comments.

Edmund Misson, Head of the Innovation and Measuring Progress (IMEP) division is thanked for providing very helpful comments on the different versions of the document.

Chloe Acas, Jennifer O'Brien, and Brianna Jesme provided excellent assistance to the project and prepared the document for publication with the support of Rachel Linden (OECD).

## Table of contents

Foreword 3   
Abstract 4   
Acknowledgments 5   
Executive Summary 9   
1 Introduction 12   
1.1. Multidimensional data space of LLL 13   
1.2. From conceptual framework to data framework 15   
1.3. Distinguishing data to inform research, policy design, and coordination 16   
1.4. Organisation of the report 17   
References 17   
2 Enabling societal coordination and interactions between citizens' needs and structures 19   
2.1. History and accumulation of interactions: educational careers and pathways 20   
2.2. Co-ordination of learning needs: optics on who and what decides the learning needs 21   
2.3. Coordination of current and future learning needs: navigating life transitions and aspirations 23   
2.4. Skills surplus, deficits, and shortages: impacts on organisations and communities 23   
2.5. Policy instruments for effective coordination in LLL 24   
References 26   
3 Conceptualising the learning needs, and demand of stakeholders 28   
3.1. Learning needs and demands of citizens, organisations, communities, and nations 29   
References 32   
4 Understanding the prevalence and diversity of supply of learning opportunities 36   
4.1. Traditional understandings of learning activities 37   
4.1.1. Flexibilisation of formal education 38   
4.1.2. Hybridisation of non-formal education and informal learning 39   
4.2. Towards a revised conceptual framework of learning categories 40   
4.3. Situated provisions across institutional clusters 41   
4.3.1. Formal education cluster 43   
4.3.2. Employer cluster 44   
4.3.3. Welfare policy cluster 44   
4.3.4. Civic cluster 45

## References

5 Accounting for learning outcomes as key drivers of coordination, demand and supply 52
5.1. Setting, valuing, and researching learning objectives and outcomes for effective coordination 53
5.2. Approaches to understanding and assessing learning needs and outcomes 55

6 Distinguishing data purposes and needs: informing research, policy design, and coordination needs 57
6.1. Research: uncovering patterns, relationships, insights and nuances 58
6.2. Policy design: informing the policy process 58
6.3. Coordination: aligning needs and opportunities 59
References 60

7 Toward furthering data and indicator development 61
7.1. Cross-sectional surveys development 62
7.2. Longitudinal survey development 63
7.3. Administrative data development in international contexts: negotiations, concepts, and comparative indicators 64
7.4. Cumulative records of qualifications and capabilities: managing transitions 64
7.5. Data integration: combining survey, administrative, and big data sources 66
7.6. References 67

8 Conclusion and recommendations 69
8.1. Summary of framework 70
8.1.1. Bridging conceptual foundations to data focus: methods, tools, and examples 70
8.1.2. Key insights from the framework 71
8.2. Suggestions for implementation 72
8.2.1. Demand: enhancing needs assessment 72
8.2.2. Supply: expanding provision mapping 73
8.2.3. Coordination: strengthening systemic alignment 73
8.2.4. Cross-cutting: building resilient LLL ecosystems 74
8.3. Next steps 74
8.4. References 75

Annex A. Theoretical foundations of the LLL conceptual framework 76

Annex B. Approaches to understanding and assessing learning needs and outcomes 79
B.1 Qualification approach: individual, organisational, and collective perspectives 79
B.2 Direct skills assessment approach 80
B.3 Skills use and mismatch approach 81
B.4 Understanding dispositions to participation approach: motivations, attitudes, and barriers 82
B.5 Workplace and organisational learning and needs approach 83
B.6 Desirable outcomes approach: individual and family level 84
B.7 Desirable outcomes approach: public and collective level 84

Annex C. Suggested indicators and questions to explore within the framework 86
C.1 Core data and information for learning needs and demand 86
Addressing data gaps 87

Innovative data solutions 88  
Key indicators, research questions, and policy questions 88  
C.2 Core data and information for learning opportunities 89  
Core data and indicators 89  
Addressing data gaps 89  
Innovative data solutions 90  
Key indicators, research questions, and policy questions 90  
C.3 Core data and information for coordinating lifelong learning 91  
Core data and indicators 91  
Addressing data gaps 92  
Innovative data solutions 92  
Key indicators, research questions, and policy questions 92  
C.4 Summary boxes 93  
C.4.1 Demand: measuring capability gaps 93  
C.4.2 Supply: Mapping Diverse Provisions 95  
C.4.3 Coordination: Aligning pathways and policies 96  
References 97

## Tables

Table A C.1. Key data and indicators focused on LLL needs 86  
Table A C.2. Core Data and Indicators 89  
Table A C.3. Key data and indicators focused on LLL coordination 91

## Figures

Figure 1.1. Multidimensional space of LLL 14  
Figure 1.2. LLL conceptual framework 15  
Figure 3.1. The Multi-Level Ecology of LLL Needs 31  
Figure 4.1. Flexibilisation and hybridisation of learning activities 39  
Figure 4.2. Revised conceptualisation of LLL activities with examples of various types of learning 40  
Figure 4.3. Embeddedness of learning activities in institutional clusters 42  
Figure 5.1. Learning data points to learning outcomes 54

## Boxes

Box A C.1. Demand Indicators 94  
Box A C.2. Supply Indicators 95  
Box A C.3. Coordination Indicators 96  
Box A C.4. Resilient Data Ecosystems Indicator 97

# Executive Summary

Building a conceptual foundation for a lifelong learning measurement framework

This report develops a conceptual foundation for a measurement framework that captures learning trajectories across the life course and diverse contexts, and enables systematic assessment of how policies shape participation and outcomes. It provides policymakers with a comprehensive approach to understanding how lifelong learning (LLL) systems function, where gaps exist, and how interventions can strengthen opportunities across populations.

LLL has become a central policy lever for productivity, inclusion, and resilience in the face of demographic ageing, technological change, and evolving skill demands. Yet existing data systems were designed mainly to measure educational attainment and training participation at specific life stages. They do not adequately capture learning as a lifelong and life-wide phenomenon, creating four major limitations that constrain policy design and evaluation.

First, coverage is too narrow across the life course. Most international measurement focuses on adults aged 25-64, offering limited visibility into learning outside formal schooling in childhood and excluding adults over 64. Learning through families, communities, and digital environments is largely invisible, despite its growing importance. As a result, critical phases of human development, skill maintenance, and the links between them remain poorly understood.

Second, measurement is largely cross-sectional, providing static snapshots rather than tracking learning over time. Current instruments do not follow how skills evolve through key life transitions such as entering the workforce, changing occupations, forming families, or retiring. The absence of systematic longitudinal linkages between surveys like the Programme for International Student Assessment (PISA) and Programme for the International Assessment Competencies (PIAAC) prevents a coherent view of skill development across decades. Policymakers cannot assess whether early investments yield long-term returns or identify where trajectories diverge.

Third, outcomes are too focused on the labour market. While employability and earnings matter, learning also produces broader social benefits, including civic participation, health literacy, social cohesion, personal agency, and wellbeing. These wider returns are largely absent from current metrics, limiting understanding of the full value of LLL and narrowing policy debates to economic productivity alone.

Fourth, informal learning is insufficiently captured. Much skill development occurs through everyday activities in workplaces, families, communities, and increasingly through digital resources such as online tutorials and platforms. These forms of learning remain weakly measured, creating blind spots precisely where learning is expanding most rapidly.

## A three-pillar framework for measuring lifelong learning systems

The proposed framework organises measurement around three interconnected pillars: demand, supply, and coordination. Together they provide a system-level perspective for monitoring and policy analysis, recognising that LLL systems depend not only on provision but also on how well supply aligns with needs and how effectively individuals are connected to opportunities.

Demand captures learning needs at three levels. At the individual level, it refers to skill gaps and capabilities required for work and daily life. At the organisational and community level, it reflects skill requirements within firms, sectors, and public services. At the societal level, it encompasses system-wide pressures such as demographic ageing or technological change that generate population-wide learning needs.

Supply maps learning opportunities across four institutional clusters: formal education systems; employers and workplace learning; welfare and 

[中间内容因长度限制已省略]

nd D. Stolle (2008), “The State and Social Capital: An Institutional Theory of Generalized Trust”, The State and Social Capital: An Institutional Theory of Generalized Trust. Comparative Politics, Vol. 40/4, pp. 441–459, http://www.jstor.org/stable/20434095.

Rubenson, K. (2018), Conceptualising participation in adult learning and education: Equity issues, In M. Milana, S. Webb, J. Holford, R. Waller, & P. Jarvis (Eds.), The Palgrave international handbook on adult and lifelong education and learning (pp. 337–357). Palgrave Macmillan.

Rubenson, K. and R. Desjardins (2009), “The Impact of Welfare State Regimes on Barriers to Participation in Adult Education”, Adult Education Quarterly, Vol. 59/3, pp. 187-207, https://doi.org/10.1177/0741713609331548.

Salling Olesen, H. (2001), “Professional identity as learning processes in life histories”, Journal of Workplace Learning, Vol. 13/7/8, pp. 290-298, https://doi.org/10.1108/13665620110411076.

Schuller, T. et al. (2004), The benefits of learning: The impact of education on health, family life and social capital, Routledge. [24]

Schultheiss, T. and U. Backes-Gellner (2023), “Different degrees of skill obsolescence across hard and soft skills and the role of lifelong learning for labor market outcomes”, Industrial Relations: A Journal of Economy and Society, Vol. 62/3, pp. 257-287, https://doi.org/10.1111/irel.12325.

Schultz, T. (1959), “Investment in Man: An Economist’s View”, Social Service Review, Vol. 33/2, pp. 109-117, https://doi.org/10.1086/640656. [36]

Scott, A. (2024), The Longevity Imperative, Basic. [14]

Sekmokas, M. et al. (2024), “Updated Framework for Monitoring Adult Learning: Enhancing Data Identification and Indicator Selection”, OECD Education Working Paper No. 317. [93]

Sen, A. (1999), Development as freedom, Oxford University Press.

Spence, M. (1973), “Job Market Signaling”, The Quarterly Journal of Economics, Vol. 87/3, pp. 355-374, https://doi.org/10.2307/1882010. [29]

Steindórsdóttir, B. et al. (2023), “Career transitions and career success from a lifespan developmental perspective: A 15-year longitudinal study”, Journal of Vocational Behavior, Vol. 140, p. 103809, https://doi.org/10.1016/j.jvb.2022.103809. [100]

Stiglitz, J. and B. Greenwald (2014), Creating a learning society: A new approach to growth, development, and social progress, Columbia University Press. [81]

Suleyman, M. and M. Bhaskar (2024), The Coming Wave. AI, Power and our Future, Vintage. [13]

UNESCO (2019), Global report on adult learning and education, UNESCO Institute for Lifelong Learning. [91]

UNESCO (1996), “Learning: The treasure within”, Report to UNESCO of the International Commission on Education for the Twenty-first Century. UNESCO, https://unesdoc.unesco.org/ark:/48223/pf0000109590.

van der Velden, R. and I. Bijlsma (2019), “Effective skill: A new theoretical perspective on the relation between skills, skill use, mismatches, and wages”, Effective skill: A new theoretical perspective on the relation between skills, skill use, mismatches, and wages. Oxford Economic Papers, Vol. 71/1, pp. 145–165.

van Dijck, J., T. Poell and M. De Waal (2018), The Platform Society: Public Values in a Connective World, Oxford University Press.

Van Nieuwenhove, L. and B. De Wever (2023), “Psychosocial Barriers to Adult Learning and the Role of Prior Learning Experiences: A Comparison Based on Educational Level”, Adult Education Quarterly, Vol. 74/1, pp. 62-87, https://doi.org/10.1177/07417136231147491.

Vignoles, A., F. Galindo-Rueda and L. Feinstein (2004), “The Labour Market Impact of Adult Education and Training: A Cohort Analysis”, Scottish Journal of Political Economy, Vol. 51/2, pp. 266-280, https://doi.org/10.1111/j.0036-9292.2004.00306.x.

Wasson, B. et al. (2024), “Implementing Learning Analytics in Norway”, Journal of Learning Analytics, Vol. 11/2, pp. 268-280, https://doi.org/10.18608/jla.2024.8241.

West, R. and S. Michie (2020), A brief introduction to the COM-B model of behaviour and the PRIME Theory of motivation, Qeios.

World Bank (2016), Snapshot. Investing in the early years for growth and productivity, Washington DC. World Bank Group, https://www.worlddata.info/life-expectancy.php.

# A Conceptual Foundation for the Development of a Lifelong Learning Measurement Framework

This report proposes a conceptual framework for measuring lifelong learning (LLL) aimed at improving policy design and evaluation. Lifelong learning is understood as learning across the life course and diverse contexts. The report identifies key limitations in current data systems, including narrow age coverage, lack of longitudinal tracking, overemphasis on labour-market outcomes, and insufficient measurement of informal learning.

To address these gaps, the framework is structured around three interconnected pillars: demand, supply, and coordination. Demand captures learning needs at individual, organisational, and societal levels; supply maps opportunities across formal education, workplaces, welfare systems, and communities; and coordination focuses on mechanisms that align needs with provision. The framework also redefines learning by introducing a two-dimensional model based on formalisation and digitalisation, better capturing hybrid and emerging forms.

Finally, it outlines practical steps for implementation, including improved surveys, longitudinal data linkages, administrative data integration, skills passports, and advanced analytics to support more comprehensive and effective lifelong learning systems.

The report will be of interest to education policy makers, whether interested in formal education or adult learning, to statisticians as well as other education stakeholders.
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
