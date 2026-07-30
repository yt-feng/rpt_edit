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
## OECD Education Working Papers No. 348

An AI-enhanced granular analysis of Thailand's mathematics performance

https://dx.doi.org/10.1787/e26ed12c-en

An AI-Enhanced Granular Analysis of Thailand's Mathematics Performance

OECD Education Working Paper No. 348

# OECD EDUCATION WORKING PAPERS SERIES

This work is issued under the responsibility of the Secretary-General of the OECD, and does not necessarily reflect the official views of OECD Member countries.

Comments on Working Papers are welcome and may be sent to edu.contact@oecd.org or the Directorate for Education and Skills, OECD, 2 rue André-Pascal, 75775 Paris Cedex 16, France.

This document, as well as any data and map included herein, are without prejudice to the status of or sovereignty over any territory, to the delimitation of international frontiers and boundaries and to the name of any territory, city or area.

![](images/0e8e4863766345a69b727275d5552f9298193d4738da635ee6c4d0b218259998.jpg)

## Attribution 4.0 International (CC BY 4.0)

This work is made available under the Creative Commons Attribution 4.0 International licence. By using this work, you accept to be bound by the terms of this license (https://creativecommons.org/licenses/by/4.0/).

Attribution – you must cite the work.

Translations – you must cite the original work, identify changes to the original and add the following text: In the event of any discrepancy between the original work and the translation, only the text of original work should be considered valid.

Adaptations – you must cite the original work and add the following text: This is an adaptation of an original work by the OECD. The opinions expressed and arguments employed in this adaptation should not be reported as representing the official views of the OECD or of its Member countries.

Third-party material – the licence does not apply to third-party material in the work. If using such material, you are responsible for obtaining permission from the third party and for any claims of infringement.

You must not use the OECD logo, visual identity or cover image without express permission or suggest the OECD endorses your use of the work.

Any dispute arising under this licence shall be settled by arbitration in accordance with the Permanent Court of Arbitration (PCA) Arbitration Rules 2012. The seat of arbitration shall be Paris (France). The number of arbitrators shall be one.

## Abstract

This paper applies the Collective Intelligence Model for Education (CIME) to Thailand's Programme for International Student Assessment (PISA) 2022 mathematics data and assessment materials to generate fine-grained diagnostic evidence for curriculum review and instructional support. The study combines AI-assisted scoring, expert review and psychometric scaling, using bilingual item-facet rubrics with Thai serving as the operational scoring language. The resulting profiles examine student performance across 12 content topics and 17 cognitive operators. Findings indicate relative strengths in geometry-related content, measurement, estimation, Chance and probability, and selected procedural tasks. More demanding areas include Formulating situations mathematically, interpreting results in context, recognising functional relationships, and working with algebraic, functional and data-representation content. The analysis also identifies limited gender differences in most areas, alongside substantial variation by economic, social and cultural status. Overall, the paper shows how large-scale assessment data can be translated into competency-oriented evidence for Thailand's ongoing education reform.

## Acknowledgements

This paper was prepared by Tomoya Okubo (OECD) and Fabrice Blais-Savoie (OECD) as part of the project Developing an International Large-Scale AI Tool for Educational Assessment and Personalised Learning, undertaken within the Programme of Work of the OECD Centre for Educational Research and Innovation (CERI). The authors are grateful to their OECD colleagues Elizabeth Fordham, Caitlyn Guthrie and Lucia Alonso for their insightful contributions and discussions. They also thank Masaki Uto and Yoshimitsu Miyazawa for their valuable expert feedback and comments. The authors would further like to thank officials at Thailand's Institute for the Promotion of Teaching Science and Technology for their feedback on earlier versions of this paper. Finally, they wish to thank Rachel Linden for editorial and publication support.

## Table of contents

OECD EDUCATION WORKING PAPERS SERIES 2
Abstract 3
Acknowledgements 4
1 Introduction 7
Background and rationale 7
Study objectives and analytical focus 7
Thailand in PISA 2022 mathematics 8
2 Methodological framework and study design 10
Analytical foundations of the CIME model 10
Adaptation of the framework to Thai-language assessment materials 11
Construct specification and rubric development 11
Scoring procedures, scaling and profile estimation 12
3 Profile analysis of mathematics in Thailand: PISA 2022 14
Structural dimensions of the mathematics profile 14
Patterns of performance across cognitive operators 14
Patterns of performance across content topics 19
4 Variation in mathematics performance profiles by gender and ESCS 22
Differential performance by gender in cognitive operators 22
Differential performance by gender in content topics 24
Differential performance by ESCS in cognitive operators 25
Differential performance by ESCS in content topics 28
5 Discussion and policy-relevant implications 30
Substantive insights from the Thai-language application of CIME 30
Implications for curriculum design and implementation 31
Analytical boundaries with respect to curriculum and policy evaluation 32
6 Conclusion 34
References 35
Annex A. Cognitive operators and content topics 38

## FIGURES

Figure 1. Performance across Formulating situations mathematically 16  
Figure 2. Performance across Employing mathematical concepts, facts and procedures 17  
Figure 3. Performance across Interpreting, applying and evaluating mathematical outcomes 18  
Figure 4. Performance across Mathematical reasoning 19  
Figure 5. Performance across content topics 21  
Figure 6. Gender differences in score across cognitive operators 23  
Figure 7. Gender differences in score across content topics 25  
Figure 8. Score differences between $1^{\text{st}}$ and $4^{\text{th}}$ quartile ESCS groups across cognitive operators 27  
Figure 9. Score differences between $1^{\text{st}}$ and $4^{\text{th}}$ quartile ESCS groups across content topics. 29

## TABLES

Table 1. Mathematics and subdomain scores for Thailand and the OECD average in PISA 2022 9  
Table 2. Scores by Cognitive operator and the difference from overall mathematics score 15  
Table 3. Scores by content topic and differences from overall mathematics score 20  
Table 4. Scores by cognitive operator and gender 23  
Table 5. Scores by content topic and gender 24  
Table 6. Scores by cognitive operator and ESCS group 27  
Table 7. Scores by content topic and ESCS group 28  
Table 8. Cognitive operators in Formulating situations mathematically 38  
Table 9. Cognitive operators in Employing mathematical concepts, facts and procedures 38  
Table 10. Cognitive operators in Interpreting, applying and evaluating mathematical outcomes 39  
Table 11. Cognitive operators in Mathematical reasoning 39  
Table 12. Content topics in Mathematical literacy 40

# 1 Introduction

## Background and rationale

Since enshrining access to education in its 1997 constitution and implementing compulsory education in its 1999 National Education Act, Thailand has transformed its education system into a regional paragon of education access (Das and Narayanan, 2023[1]; OECD and UNESCO, 2016[2]). As access has expanded, policy attention has increasingly focused on the quality, relevance and equity of learning opportunities. Previous studies and policy reviews have identified several areas that are central to this agenda, including curriculum design, student assessment, teacher preparation and school leadership (Fry and Bi, 2013[3]; OECD and UNESCO, 2016[2]; World Bank, 2024[4]; OECD, 2025[5]). These areas are closely related to Thailand's broader skills agenda, as initial education plays an important role in helping young people acquire foundational skills, develop higher-level competencies and build positive attitudes towards lifelong learning (OECD, 2025[5]). Recent evidence on foundational skills among youth and adults also underlines the importance of strengthening reading literacy, digital skills and socio-emotional skills as part of a broader learning agenda (World Bank, 2024[4]).

The National Scheme of Education B.E. 2560–2579 (2017–2036) has aimed to provide a long-term framework for education development in preparation for “Thailand 4.0”, taking into account rapid technological change, socio-economic transformation, demographic change and evolving skill requirements (Office of the Education Council, n.d.[6]; OECD, 2025[5]). Within this context, Thailand has been working towards a stronger competency orientation in basic education, placing emphasis on competencies such as critical thinking, creativity, collaboration, digital literacy, citizenship and other skills associated with learning and participation in the 21st century (Sangwanglao, 2024[7]; OECD, 2025[5]; Office of the Education Council, n.d.[6])

This analysis comes at an important moment for Thailand's education system, around the midpoint of the National Scheme of Education and during an ongoing period of curriculum review. In line with recent OECD analytical work, the study uses more granular assessment information to complement aggregate performance indicators and examine students' mathematical proficiency in relation to specific content areas and cognitive processes. By providing diagnostic evidence closer to curriculum design and classroom practice, the analysis can support Thailand's ongoing work on competency-based education and contribute to the evidence base for monitoring future curriculum implementation.

## Study objectives and analytical focus

This study aims to provide Thailand's policymakers, curriculum developers, assessment specialists and teachers with diagnostic evidence that can inform curriculum review, instructional planning and targeted student support. Building on the Collective Intelligence Model for Education (CIME) approach applied in the analysis of Ireland's PISA 2022 mathematics profile, this study uses student item-response data and assessment materials to translate large-scale assessment data into multidimensional competency profiles (Okubo and Reinertsen, 2025[8]). In the Ireland application, CIME (Okubo, 2025[9])

complemented within-country analysis with more granular learning progressions analysis and generated fine-grained, policy-relevant diagnostics. In the Thai context, a similar approach can help identify mathematical content areas, cognitive processes and transversal competencies in which students show relative strengths, as well as areas where additional instructional support may be beneficial. It complements conventional analysis with an educationally interpretable framework that is more closely aligned with curriculum design and classroom practice.

This paper analyses Thailand's PISA 2022 mathematics data and assessment materials to provide system-level, competency-specific insights into students' mathematical proficiency. The analysis builds on the PISA 2022 assessment and sampling design, which provides comparable information on 15-year-old students' knowledge and skills and is accompanied by technical procedures intended to support the validity and reliability of the results (OECD, 2024[10]). Since mathematics was the major domain of PISA 2022, the assessment provides a particularly rich basis for examining students' mathematical literacy across content areas, processes and contexts. By linking these data to the CIME analytical framework, the study seeks to make visible patterns of proficiency that may not be apparent from overall mathematics scores alone.

This type of diagnostic evidence is particularly relevant to Thailand's current reform context. Curriculum design in Thailand is guided at the national level, while curriculum implementation, assessment practices and teacher professional learning involve multiple administrative levels and institutional actors (OECD and UNESCO, 2016[2]). A competency-oriented analysis of large-scale assessment (LSA) data and materials can therefore provide a shared evidence base for dialogue among national agencies, education service areas, schools and teachers. It can also support the use of large-scale assessment evidence for more targeted purposes, including the refinement of curriculum materials, the development of teacher guidance, the design of formative assessment resources and the prioritisation of professional learning.

The study also has an equity-oriented analytical focus. By translating large-scale assessment results from international scores into competency-oriented profiles, the analysis can examine whether patterns of mathematical proficiency vary across students and help inform differentiated support, moving beyond broad performance categories. More generally, the study aims to make LSA evidence more actionable for educators by presenting results in an educational language linked to competencies, learning progressions and classroom practice. In this way, it contributes to Thailand's ongoing work on competency-based education by providing a bridge between international assessment data, curriculum priorities and the instructional decisions that shape students' learning opportunities.

## Thailand in PISA 2022 mathematics

In Thailand, 8 495 students from 279 schools completed the PISA 2022 assessment, representing approximately 604 600 15-year-old students, or an estimated $75\%$ of the total population of 15-year-olds (OECD, 2023[11]). Trend results indicate that Thailand's average performance in mathematics, reading and science in 2022 was lower than in previous PISA cycles. While the aggregate trends are useful, specific action to support improvement can be assisted by complementing headline scores with more diagnostic evidence.

Table 1 provides a more detailed view of Thailand's mathematics profile in PISA 2022, as presented in OECD (2023[12]). Thailand's overall mathematical literacy score was 393.9 points, compared with the OECD average of 472.4 points. Across the Cognitive Processes, Thailand's scores were relatively closely clustered around the overall mathematics score, suggesting a broadly balanced mathematical profile. As for content areas, Uncertainty and data appears as a content area that may merit closer examination, particularly in relation to students' opportunities to work with data, probability, variation and statistical reasoning.

Table 1. Mathematics and subdomain scores for Thailand and the OECD average in PISA 2022

<table><tr><td colspan="2">Subdomain</td><td>OECD</td><td>Thailand</td></tr><tr><td colspan="2">Mathematical literacy</td><td>472.4 (0.4)</td><td>393.9 (2.7)</td></tr><tr><td rowspan="4">Content area</td><td>Change and relationships</td><td>469.8 (0.5)</td><td>393.8 (3.6)</td></tr><tr><td>Quantity</td><td>472.4 (0.4)</td><td>392.2 (2.8)</td></tr><tr><td>Space and shape</td><td>470.5 (0.5)</td><td>392.6 (4.3)</td></tr><tr><td>Uncertainty and data</td><td>473.7 (0.5)</td><td>385.5 (2.8)</td></tr><tr><td rowspan="4">Cognitive process</td><td>Formulating situations mathematically</td><td>468.6 (0.5)</td><td>390.3 (3.0)</td></tr><tr><td>Employing mathematical concepts, facts and procedures</td><td>471.8 (0.4)</td><td>393.9 (2.8)</td></tr><tr><td>Interpreting, applying and evaluating mathematical outcomes</td><td>474.4 (0.5)</td><td>391.5 (4.8)</td></tr><tr><td>Mathematical reasoning</td><td>472.7 (0.4)</td><td>390.8 (4.5)</td></tr></table>

Source: OECD (2023), PISA 2022 Results (Volume I), https://doi.org/10.1787/53f23881-en. Table I.2.7. Comparing countries and economies on the mathematics-process subscales

Between 2018 and 2022, the performance gap between students at the higher and lower ends of Thailand's mathematics performance distribution narrowed (OECD, $2023_{[12]}$ ). However, the underlying trend suggests declining performance by high-performers, while low-performers remained resilient. Nevertheless, over the same period, the proportion of students performing below Level 2, the PISA baseline proficiency level, increased by 19 percentage points in mathematics and science, and by 32 percentage points in reading (OECD, $2023_{[12]}$ ). These developments have contributed to wider scholarly and policy discussions on how large-scale assessment evidence can be interpreted and used to support education improvement (Rowley et al., $2019_{[13]}$ ; OECD, $2023_{[11]}$ ; UNESCO, $2023_{[14]}$ ; Alali and Wardat, $2024_{[15]}$ ). For Thailand, the relatively even profile across most mathematics subdomains, together with the descriptive difference observed in Uncertainty and data, points to the potential value of a more granular competency analysis to obtain insights more relevant to curriculum design, teacher professional learning and targeted support for students.

# 2 Methodological framework and study design

## Analytical foundations of the CIME model

This section describes the analytical framework used to generate fine-grained profiles of mathematics performance in Thailand using PISA 2022 response data and assessment materials. The analysis applies the Collective Intelligence Model for Education (CIME), an AI-enhanced assessment modelling framework that combines expert judgement, large language models (LLMs) and psychometric scaling to extract multidimensional evidence from student responses and assessment materials (Okubo, 2025[9]). The objective is to complement the assessment reports that focus on overall scores with more detailed diagnostic information on the mathematical content and cognitive operations reflected in students' responses.

CIME treats each item response as potential evidence of multiple underlying competencies. Rather than assigning a response only to a single overall correctness category, the framework decomposes assessment items into item-facet rubrics. Each rubric corresponds to a specific construct, such as a mathematical content topic or a cognitive operator, and specifies the observable evidence required to infer different levels of achievement for that construct. In this way, a single response can contribute evidence to several proficiency dimensions. In this study, some cognitive operators are more frequent

[中间内容因长度限制已省略]

 make sense given the context of a problem (Explaining result validity in context)</td></tr><tr><td>Understanding the extent and limits of mathematical concepts and mathematical solutions (Understanding limits of concepts/solutions)</td></tr><tr><td>Critiquing and identifying the limits of the model used to solve a problem (Critiquing/identifying limits of model used)</td></tr><tr><td>Using mathematical thinking and computational thinking to make predictions, to provide evidence for arguments, to test and compare proposed solutions (Using maths &amp; computational thinking to predict/argue)</td></tr></table>

Table 11. Cognitive operators in Mathematical reasoning

<table><tr><td>Cognitive process</td><td>Cognitive operators in Mathematical reasoning</td></tr><tr><td rowspan="6">Mathematical reasoning</td><td>Understanding quantity, number systems and their algebraic properties (Understanding quantity &amp; number systems)</td></tr><tr><td>Appreciating the power of abstraction and symbolic representation (Appreciating abstraction &amp; symbols)</td></tr><tr><td>Seeing mathematical structures and their regularities (Seeing structures &amp; regularities)</td></tr><tr><td>Recognising functional relationships between quantities (Recognising functional relationships)</td></tr><tr><td>Using mathematical modelling as a lens onto the real world (e.g. those arising in the physical, biological, social, economic, and behavioural sciences) (Using modelling as real-world lens)</td></tr><tr><td>Understanding variation as the heart of statistics (Understanding variation in statistics)</td></tr></table>

Table 12. Content topics in Mathematical literacy

<table><tr><td>Content topic</td><td>Brief description</td></tr><tr><td>Growth phenomena</td><td>Different types of linear and non-linear growth.</td></tr><tr><td>Geometric approximation</td><td>Approximating the attributes and properties of irregular or unfamiliar shapes and objects by breaking these shapes and objects up into more familiar shapes and objects for which there are formulae and tools.</td></tr><tr><td>Computer simulations</td><td>Exploring situations (that may include budgeting, planning, population distribution, disease spread, experimental probability, reaction time modelling etc.) in terms of the variables and the impact that these have on the outcome.</td></tr><tr><td>Conditional decision making</td><td>Using basic principles of combinatorics and an understanding of inter-relationships between variables to interpret situations and make predictions.</td></tr><tr><td>Functions</td><td>The concept of function, emphasising but not limited to linear functions, their properties, and a variety of descriptions and representations of them. Commonly used representations are verbal, symbolic, tabular and graphical.</td></tr><tr><td>Algebraic expressions</td><td>Verbal interpretation of and manipulation with Algebraic expressions, involving numbers, symbols, arithmetic operations, powers and simple roots.</td></tr><tr><td>Equations and inequalities</td><td>Linear and related Equations and inequalities, simple second-degree equations, and analytic and non-analytic solution methods.</td></tr><tr><td>Co-ordinate systems</td><td>Representation and description of data, position and relationships.</td></tr><tr><td>Relationships within and among geometrical objects in two and three dimensions</td><td>Static relationships such as algebraic connections among elements of figures (e.g. the Pythagorean theorem as defining the relationship between the lengths of the sides of a right triangle), relative position, similarity and congruence, and dynamic relationships involving transformation and motion of objects, as well as correspondences between two- and three-dimensional objects.</td></tr><tr><td>Measurement</td><td>Quantification of features of and among shapes and objects, such as angle measures, distance, length, perimeter, circumference, area and volume.</td></tr><tr><td>Numbers and units</td><td>Concepts, representations of numbers and number systems (including converting between number systems), including properties of integer and rational numbers, as well as quantities and units referring to phenomena such as time, money, weight, temperature, distance, area and volume, and derived quantities and their numerical description.</td></tr><tr><td>Arithmetic operations</td><td>The nature and properties of these operations and related notational conventions.</td></tr><tr><td>Percents, ratios and proportions</td><td>Numerical description of relative magnitude and the application of proportions and proportional reasoning to solve problems.</td></tr><tr><td>Counting principles</td><td>Simple combinations.</td></tr><tr><td>Estimation</td><td>Purpose-driven approximation of quantities and numerical expressions, including significant digits and rounding.</td></tr><tr><td>Data collection, representation and interpretation</td><td>Nature, genesis and collection of various types of data, and the different ways to analyse, represent and interpret them.</td></tr><tr><td>Data variability and its description</td><td>Concepts such as variability, distribution and central tendency of data sets, and ways to describe and interpret these in quantitative and graphical terms.</td></tr><tr><td>Samples and sampling</td><td>Concepts of sampling and sampling from data populations, including simple inferences based on properties of samples including accuracy and precision.</td></tr><tr><td>Chance and probability</td><td>Notion of random events, random variation and its representation, chance and frequency of events, and basic aspects of the concept of probability and conditional probability.</td></tr></table>
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
