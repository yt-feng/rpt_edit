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
## Corporate Tax Statistics 2026

![](images/ca728e166836a7c9db400f39173a8683d2d28ef37d39025e7f7ea0e1afe22be1.jpg)

## Corporate Tax Statistics 2026

This work is issued under the responsibility of the Secretary-General of the OECD, and does not necessarily reflect the official views of OECD Member countries.

This document, as well as any data and map included herein, are without prejudice to the status of or sovereignty over any territory, to the delimitation of international frontiers and boundaries and to the name of any territory, city or area.

The statistical data for Israel are supplied by and under the responsibility of the relevant Israeli authorities. The use of such data by the OECD is without prejudice to the status of the Golan Heights, East Jerusalem and Israeli settlements in the West Bank under the terms of international law.

## Note by the Republic of Türkiye

The information in this document with reference to “Cyprus” relates to the southern part of the Island. There is no single authority representing both Turkish and Greek Cypriot people on the Island. Türkiye recognises the Turkish Republic of Northern Cyprus (TRNC). Until a lasting and equitable solution is found within the context of the United Nations, Türkiye shall preserve its position concerning the “Cyprus issue”.

Note by all the European Union Member States of the OECD and the European Union

The Republic of Cyprus is recognised by all members of the United Nations with the exception of Türkiye. The information in this document relates to the area under the effective control of the Government of the Republic of Cyprus.

Please cite this publication as:

OECD (2026), Corporate Tax Statistics 2026, OECD Publishing, Paris, https://doi.org/10.1787/73af6222-en.

ISBN 978-92-64-91313-4 (print)
ISBN 978-92-64-60844-3 (PDF)
ISBN 978-92-64-90043-1 (HTML)

Corporate Tax Statistics

ISSN 2958-485X (print)

ISSN 2958-4434 (online)

Photo credits: Cover © jean-marc payet/Getty images.

Corrigenda to OECD publications may be found at: https://www.oecd.org/en/publications/support/corrigenda.html.

![](images/69978fa42323d1ba8adb7ae3642e92495023b5502eeff16568c8a5d9c6985fe9.jpg)

## Attribution 4.0 International (CC BY 4.0)

This work is made available under the Creative Commons Attribution 4.0 International licence. By using this work, you accept to be bound by the terms of this licence (https://creativecommons.org/licenses/by/4.0/).

Attribution – you must cite the work.

Translations – you must cite the original work, identify changes to the original and add the following text: In the event of any discrepancy between the original work and the translation, only the text of the original work should be considered valid.

Adaptations – you must cite the original work and add the following text: This is an adaptation of an original work by the OECD. The opinions expressed and arguments employed in this adaptation should not be reported as representing the official views of the OECD or of its Member countries.

Third-party material – the licence does not apply to third-party material in the work. If using such material, you are responsible for obtaining permission from the third party and for any claims of infringement.

You must not use the OECD logo, visual identity or cover image without express permission or suggest the OECD endorses your use of the work.

Any dispute arising under this licence shall be settled by arbitration in accordance with the Permanent Court of Arbitration (PCA) Arbitration Rules 2012. The seat of arbitration shall be Paris (France). The number of arbitrators shall be one.

## Foreword

This is the eighth edition of Corporate Tax Statistics, an annual publication that brings together information on corporate taxation and base erosion and profit shifting (BEPS) practices that previously were unavailable to tax policy researchers and policymakers. This includes data on corporate tax rates, revenues, effective tax rates (ETR), tax incentives for research and development (R&D) and innovation, and withholding taxes amongst other data series. Corporate Tax Statistics also includes anonymised and aggregated Country-by-Country Reporting (CbCR) data providing an overview on the global tax and economic activities of thousands of large multinational enterprise groups operating worldwide. Corporate Tax Statistics follows on from the OECD/G20 BEPS Project and its package of fifteen measures adopted in 2015 to address tax avoidance. The project's Action 11 noted that the lack of available and high-quality data on corporate taxation is a major limitation to the measurement and monitoring of the scale of BEPS and the impact of the measures agreed to be implemented under the OECD/G20 BEPS Project.

The report is structured as follows. Chapter 1 presents internationally comparable data on the tax revenues of OECD, Latin American and the Caribbean (LAC), African, and Asian and Pacific jurisdictions. Chapter 2 contains information on the headline tax rate faced by corporations and can be used to compare the standard tax rate on corporations across jurisdictions and over time. Chapter 3 presents information on standard and treaty-based withholding taxes (WHTs) which are levied on businesses when they make payments to other foreign or domestic business entities or individuals, e.g., in the form of dividends, interest, and royalties. Chapter 4 presents “forward-looking” ETRs, which are synthetic tax policy indicators calculated using information about specific tax policy rules to assess the impact of taxation on returns to a hypothetical investment project. Chapter 5 describes several indicators of R&D tax incentives that offer a complementary view to the standard ETRs in Chapter 4 with a focus on tax support provided through expenditure- and income-based R&D tax incentives. Chapter 6 contains information on several BEPS actions, notably Action 3 relating to Controlled Foreign Company rules, Action 4 relating to interest limitation rules, Action 5 relating to intellectual property regimes and Action 13, relating to CbCR. As part of BEPS Action 13, CbCR was introduced to support jurisdictions in combating BEPS. An overview of the anonymised and aggregated CbCR data is provided in Chapter 7, including general data characteristics and some general observations from the CbCR data.

This publication was prepared under the auspices of the Working Party No. 2 on Tax Policy and Statistics of the Inclusive Framework (IF) on BEPS. The authors wish to thank delegates of Working Party No 2 for their time in preparing the statistics for publication. The publication is led by Ruairi Sugrue, under the supervision of Pierce O'Reilly. Chapters 1, 2 and 3 were prepared by Ruairi Sugrue. Chapter 4 was prepared by Clara Gascon, Ana Cinta Gonzalez Cabral and Yunis Griebenow. Chapter 5 was prepared by Ana Cinta Gonzalez Cabral, with input from Silvia Appelt and Fernando Galindo-Rueda. Chapter 6 was prepared by Ruairi Sugrue with input from Jessica De Vries and the Forum for Harmful Tax Practices (FHTP). Chapter 7 was prepared by Ruairi Sugrue and Felix Hugger.

## Table of contents

Foreword 3   
Reader's guide 7   
Abbreviations, acronyms and jurisdiction names 9   
Executive summary 12   
1 Corporate tax revenues 14   
Introduction 14   
Data characteristics 14   
Corporate income tax revenues in 2023 15   
Corporate income tax revenues trends 19   
Notes 21   
2 Statutory corporate income tax rates 22   
Introduction 22   
Data characteristics 22   
Statutory corporate income tax rates in 2026 23   
Corporate income tax rate trends 25   
References 27   
Notes 27   
3 Withholding tax rates and tax treaties 28   
Introduction 28   
Data characteristics 29   
Withholding tax rates in 2026 29   
References 36   
Note 36   
4 Corporate effective tax rates 37   
Introduction 38   
Data characteristics 38   
Forward-looking corporate effective tax rates in 2025 38   
Corporate effective tax rate trends 45   
Note 49

5 Tax incentives for research and development 50
Introduction 51
Data Characteristics 51
Indicators of R&D tax incentives 2025 (or latest available year) 52
R&D tax incentives trends 59
References 64
Note 64
6 BEPS Actions 65
Introduction 65
References 76
Note 76
7 Country-by-country reporting statistics 77
Introduction 77
Data characteristics 78
CbCR statistics for financial year (FY) 2023 79
Insights on BEPS from CbCR data 89
References 92
Notes 92

## FIGURES

Figure 1.1. Corporate income tax revenues as a percentage of GDP, 2023 16
Figure 1.2. Corporate income tax revenues as a percentage of total tax revenues, 2023 18
Figure 1.3. Average corporate income tax revenues as a percentage of total tax and as a percentage of GDP 19
Figure 1.4. Average corporate income tax revenues as a percentage of GDP by income group 20
Figure 1.5. Average corporate income tax revenues as a percentage of total tax revenues by income group 20
Figure 2.1. Statutory corporate income tax rates, 2026 24
Figure 2.2. Average statutory corporate income tax rates by region 25
Figure 2.3. Average statutory corporate income tax rates by income group 26
Figure 2.4. Changing distribution of statutory corporate income tax rates 26
Figure 3.1. Statutory withholding tax rates, 2026 31
Figure 3.2. Average withholding tax rates by income groups, 2026 32
Figure 3.3. Average treaty-based withholding tax rates, 2026 33
Figure 3.4. Number of bilateral treaties, 1990-2026 34
Figure 3.5. Average number of bilateral tax treaties by region 34
Figure 3.6. Average number of bilateral tax treaties by income group 35
Figure 4.1. Effective average tax rates, 2025 40
Figure 4.2. Effective marginal tax rate, 2025 42
Figure 4.3. EATR and EMTR: Variation across jurisdictions and assets, 2025 44
Figure 4.4. Changing distribution of corporate effective average tax rates, 2017-2025 45
Figure 4.5. Changing distribution of EATRs by assets, 2017-2025 46
Figure 4.6. Changing distribution of corporate effective marginal tax rates, 2017-2025 47
Figure 4.7. Changing distribution of EMTRs by assets, 2017-2025 48
Figure 5.1. Direct government funding and expenditure-based tax support for business R&D (BERD), 2024 53
Figure 5.2. The effective average tax rate for R&D including expenditure-based tax incentives, 2025 54
Figure 5.3. The cost of capital for R&D, 2025 55
Figure 5.4. Implied marginal tax subsidy rates on business R&D expenditures, 2025 56
Figure 5.5. EATR for internally generated R&D intangibles, 2025 57
Figure 5.6. The cost of capital for internally generated R&D intangibles, 2025 58
Figure 5.7. Changing distribution of the average EATR for R&D, 2019-2025 59
Figure 5.8. Changing distribution of the average cost of R&D capital, 2019-2025 60
Figure 5.9. Evolution of the implied marginal tax subsidy rates R&D, 2000-2025 61

Figure 5.10. EATR and implied tax subsidies for internally generated R&D intangibles, OECD countries, 2000-2025
62
Figure 5.11. Cost of capital of R&D intangibles, OECD countries, 2000-2025
63
Figure 6.1. Rules neutralising hybrid mismatch arrangements, 2026
68
Figure 6.2. Controlled Foreign Company Rules, 2026
69
Figure 6.3. Interest Limitation Rule types, 2026
70
Figure 6.4. Status of intellectual property regimes in place in 2026
72
Figure 6.5. Reduced rates under non-harmful intellectual property regimes, 2026
73
Figure 6.6. Reduced rates under non-harmful (amended) intellectual property regimes, 2026
73
Figure 6.7. Mandatory disclosure rules, 2026
74
Figure 6.8. Number of jurisdictions implementing mandatory CbCR filing
75
Figure 7.1. The evolution of CbCR coverage
80
Figure 7.2. Distribution of MNEs
81
Figure 7.3. MNEs' contribution to total CIT Revenues, 2023
84
Figure 7.4. Jurisdiction groups' shares of foreign MNEs' activities
86
Figure 7.5. Business activities
87
Figure 7.6. Business activities by income group
88
Figure 7.7. Median profits per employee: distribution within income groups
89
Figure 7.8. Median total revenues per employee: Distribution within income groups
90
Figure 7.9. Median related party revenues shares: Distribution within jurisdiction groups
91

## TABLES

Table 7.1. Content of anonymised and aggregated CbCR statistics 79  
Table 7.2. Sample composition and average values for key financial variables 81

# Reader's guide

## Overview

In developing this 2026 edition of the Corporate Tax Statistics database, the OECD has worked closely with members of the Inclusive Framework (IF) on base erosion and profit shifting (BEPS) and other jurisdictions willing to participate in the collection and compilation of statistics relevant to corporate taxation.

This database is intended to assist in the study of corporate tax policy and expand the quality and range of data available for the analysis of base erosion and profit shifting. The Measuring and Monitoring BEPS, Action 11 - 2015 Final Report highlighted that the lack of quality data on corporate taxation is a major limitation to the measurement and monitoring of the scale of BEPS and the impact of the OECD/G20 BEPS project. While this database is of interest to policy makers from the perspective of BEPS, its scope is much broader. Apart from BEPS, corporate tax systems are important more generally in terms of the revenue that they raise and the incentives for investment and innovation that they create. The Corporate Tax Statistics database brings together a range of information to support the analysis of corporate taxation, in general, and of BEPS, in particular.

The database compiles new data items as well as statistics in various existing data sets held by the OECD. The eighth edition of the database contains the following categories of data:

## Corporate tax revenues:

data are from the OECD's Global Revenue Statistics Database; $^{1}$

\- covers 135 jurisdictions from 1965-2023 (for OECD members) and 1990-2023 (for non-OECD members);

## Statutory CIT rates:

• covers all IF jurisdictions $^{2}$ from 2000-2026;

## Standard withholding tax rates:

• data covering all IF jurisdictions from 2022 – 2026;

## Bilateral tax treaties:

• data covering all IF jurisdictions;

Corporate effective tax rates:

• covers 105 jurisdictions for 2017-2025;

## Tax incentives for R&D:

\- four indicators produced by the OECD Centre for Tax Policy and Administration and the OECD Directorate for Science, Technology and Innovation;

\- covers 55 jurisdictions for 2019-2025 (for preferential tax treatment for R&D, based on effective average tax rates and cost of capital for R&D, including income-based and expenditure-based tax incentives);

\- data are from the OECD R&D Tax Incentive Database $^{4}$ produced by the OECD Directorate for Science, Technology and Innovation;

\- covers 46 jurisdictions for 2000-2024 (for expenditure-based tax and direct government support as a percentage of R&D);

• covers 46 jurisdictions for 2000-2025 (for implied subsidy rates for R&D, based on the B-Index);

## BEPS actions:

• Action 2: Data on hybrid mismatch rules;

• Action 3: Data on controlled foreign company rules;

• Action 4: Data on interest limitation rules;

\- Action 5: IP regimes - data collected for 2018-2026 by the OECD's Forum on Harmful Tax Practices, which covers 65 regimes in 50 jurisdictions for 2026;

• Action 12: Data on mandatory disclosure rules;

\- Action 13: Information on the implementation of the minimum standard on Country-by-Country Reporting

## Anonymised and aggregated CbCR statistics:

\- data are from anonymised and aggregated CbCR statistics prepared by OECD Inclusive Framework members and submitted to the OECD;

• covers up to 60 headquarter jurisdictions and up to 233 affiliate jurisdictions for 2016-2023.

# Abbreviations, acronyms and jurisdiction names

ACE Allowance For Corporate Equity  
BEPS Base Erosion and Profit Shifting  
BERD Business Expenditure On R&D  
CbCR Country-By-Country Reporting  
CFC Controlled Foreign Company  
CIT Corporate Income Tax  
CTPA OECD Centre for Tax Policy and Administration  
DSTI OECD Directorate for Science, Technology and Innovation  
ETR Effective Tax Rate  
EATR Effective Average Tax Rate  
EMTR Effective Marginal Tax Rate  
FDI Foreign Direct Investment  
FHTP Forum On Harmful Tax Practices  
GDP Gross Domestic Product  
GTARD Government Tax Relief for Business R&D  
ICAP International Compliance Assurance Programme  
IF Inclusive Framework On BEPS  
IP Intellectual Property  
ILR Interest Limitation Rule  
LAC Latin American and The Caribbean  
MDR Mandatory Disclosure Rule  
MNE Multinational Enterprise  
NPV Net Present Value  
R&D Research And Development  
RPR Related Party Revenues  
SMEs Small And Medium-Sized Enterprises  
STR Statutory Tax Rate

TREAT CbCR Tax Risk Evaluation and Assessment Tool

UPE Ultimate Parent Entity

UPR Unrelated Party Revenues

VAT Value Added Tax

WHTs    Withholding Taxes

Names and ISO codes of jurisdictions covered

<table><tr><td>ISO Code</td><td>Name</td><td>ISO Code</td><td>Name</td><td>ISO Code</td><td>Name</td></tr><tr><td>ABW</td><td>Aruba</td><td>GLP</td><td>Guadeloupe</td><td>NLD</td><td>Netherlands</td></tr><tr><td>AFG</td><td>Afghanistan</td><td>GMB</td><td>Gambia</td><td>NOR</td><td>Norway</td></tr><tr><td>AGO</td><td>Angola</td><td>GNB</td><td>Guinea-Bissau</td><td>NPL</td><td>Nepal</td></tr><tr><td>AIA</td><td>Anguilla</td><td>GNQ</td><td>Equatorial Guinea</td><td>NRU</td><td>Nauru</td></tr><tr><td>ALB</td><td>Albania</td><td>GRC</td><td>Greece</td><td>NZL</td><td>New Zealand</td></tr><tr><td>AND</td><td>Andorra</td><td>GRD</td><td>Grenada</td><td>OMN</td><td>Oman</td></tr><tr><td>ANT_F</td><td>Former Netherlands Antilles</td><td>GRL</td><td>Greenland</td><td>PAK</td><td>Pakistan</td></tr><tr><td>ARE</td><td>United Arab Emirates</td><td>GTM</td><td>Guatemala</td><td>PAN</td><td>Panama</td></tr><tr><td>ARG</td><td>Argentina</td><td>GUF</td><td>French Guiana</td><td>PER</td><td>Peru</td></tr><tr><td>ARM</td><td>Armenia</td><td>GUM</td><td>Guam</td><td>PHL</td><td>Philippines</td></tr><tr><td>ASM</td><td>American Samoa</td><td>GUY</td><td>Guyana</td><td>PLW</td><td>Palau</td></tr><tr><td>ATG</td><td>Antigua and Barbuda</td><td>HKG</td><td>Hong Kong (China)</td><td>PNG</td><td>Papua New Guinea</td></tr><tr><td>AUS</td><td>Australia</td><td>HND</td><td>Honduras</td><td>POL</td><td>Poland</td></tr><tr><td>AUT</td><td>Austria</td><td>HRV</td><td>Croatia</td><td>PRI</td><td>Puerto Rico</td></tr><tr><td>AZE</td><td>Azerbaijan</td><td>HTI</td><td>Haiti</td><td>PRK</td><td>Democratic People's Republic of Korea</td></tr><tr><td>BDI</td><td>Burundi</td><td>HUN</td><td>Hungary</td><td>PRT</td><td>Portugal</td></tr><tr><td>BEL</td><td>Belgium</td><td>IDN</td><td>Indonesia</td><td>P

[中间内容因长度限制已省略]

its per employee tend to be higher in investment hubs. Figure 7.7 and Figure 7.8 shows that the ratio of total revenues and profits to the number of employees is higher in investment hubs. In investment hubs, median revenues per employee are USD 1 811 000 while in high-, middle- and low-income jurisdictions median revenues per employee are USD 477 000, USD 211 000 and USD 153 000 respectively. While this may reflect differences in capital intensity or in worker productivity, it is likely also at least partially an indicator of BEPS.

Figure 7.7. Median profits per employee: distribution within income groups  
![](images/e023d26e3727366ded3056dfe5a6d2593c53ee31e9de19b9a97d543f8cb36b91.jpg)  
Note: “Other” reflects aggregate geographic groupings and Stateless entities. Source: Anonymised and Aggregated CbCR statistics.

Figure 7.8. Median total revenues per employee: Distribution within income groups  
![](images/1cd79c8eaa48a2b3dd302cbd02d2d62ccff4089c42e7dafdd7e96170214c9bdb.jpg)  
Note: “Other” reflects aggregate geographic groupings and Stateless entities. Source: Anonymised and Aggregated CbCR statistics.  
StatLink https://stat.link/spick0

On average, the share of related party revenues in total revenues is higher for MNEs in certain jurisdictions. Figure 7.9 plots the distribution of related party revenues as a share of total revenues, by income group. On average, the share of related party revenues in total revenues is higher in investment hubs than in high-, middle- and low-income jurisdictions. In investment hubs, related party revenues account for over 30% of total revenues, whereas the median share of related party revenues in high-, and middle-income jurisdictions is 20% and 14% respectively. The median share of related party revenues in low-income jurisdictions is much lower at just 7%. While high levels of related party revenues may be commercially motivated, they are also a high-level risk assessment factor and could be evidence of tax planning.

Figure 7.9. Median related party revenues shares: Distribution within jurisdiction groups  
![](images/21b1505760a362699ea9921bdf6404d4580355f4c6148be1198c89fb4322c378.jpg)  
Note: “Other” reflects aggregate geographic groupings and Stateless entities. Source: Anonymised and Aggregated CbCR statistics.

StatLink https://stat.link/rcx2bz

OECD (2015), Measuring and Monitoring BEPS, Action 11 - 2015 Final Report, OECD/G20 Base Erosion and Profit Shifting Project, OECD Publishing, Paris, https://doi.org/10.1787/9789264241343-en.

## Notes

$^{1}$ In the case of the United States, CbCR data are less granular than Inland Revenue Service (IRS) Form 5471, 8865, and 8858 data.

$^{2}$ With the exception of stateless income, which could relate to either domestic or foreign activities.

$^{3}$ The total number of MNEs covered in the 2023 CbCR statistics is 9400. This includes all headquarter MNEs, MNEs that provide foreign information only and MNEs that have chosen surrogate filing.

$^{4}$ Foreign MNEs' contributions might be understated for two main reasons: first, some jurisdictions provided limited geographical disaggregation; second, the contributions of MNEs with parents headquartered in jurisdictions that did not provide data are missing.

$^{5}$ Profits may be overestimated due to the inclusion of intra-company dividends as described in the CbCR disclaimer available in the Corporate Tax Statistics Explanatory Annex. To evaluate the potential magnitude of included dividends country specific analyses are available at: Netherlands: https://www.oecd.org/content/dam/oecd/en/topics/policy-sub-issues/corporate-taxation/netherlands-cbcr-country-specific-analysis.pdf; Ireland: https://www.oecd.org/content/dam/oecd/en/topics/policy-sub-issues/corporate-taxation/ireland-cbcr-country-specific-analysis.pdf; Italy: https://www.oecd.org/content/dam/oecd/en/topics/policy-sub-issues/corporate-taxation/italy-cbcr-country-specific-analysis.pdf; Sweden: https://www.oecd.org/content/dam/oecd/en/topics/policy-sub-issues/corporate-taxation/sweden-cbcr-country-specific-analysis.pdf; United Kingdom: https://www.oecd.org/content/dam/oecd/en/topics/policy-sub-issues/corporate-taxation/united-kingdom-cbcr-country-specific-analysis.pdf.

$^{6}$ Jurisdiction groups (high-, middle- and low-income) are based on the World Bank classification resulting in 63 high-income jurisdictions, 101 middle-income jurisdictions, and 24 low-income jurisdictions. The 29 investment hubs are defined as those jurisdictions with a total inward Foreign Direct Investment (FDI) position above 150% of gross domestic product (GDP).

## Corporate Tax Statistics 2026

Corporate Tax Statistics is an OECD flagship publication on corporate income tax, providing comprehensive data on corporate taxation, multinational enterprise group (MNE) activity, and base erosion and profit shifting (BEPS) practices. It supports the measurement and monitoring of tax avoidance through a wide range of indicators, including data on corporate income taxes, corporate tax rates, revenues, effective tax rates, and tax incentives for research and development (R&D) and innovation. The publication also includes anonymised and aggregated country-by-country reporting (CbCR) data providing an overview on the global tax and economic activities of thousands of MNEs. The 2026 edition covers anonymised and aggregated CbCR data on the activities of almost 9 400 MNEs headquartered in over 60 jurisdictions and includes improved geographical breakdowns for many jurisdictions. These continuing improvements allow for a more detailed and robust analysis of the distribution of key financial variables, such as profits, revenues and taxes across jurisdictions.
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
