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
OECD Statistics Working Papers 2026/03

OECD methodology to estimate SEEA Air Emission Accounts: An update

Santaro Sakata,

Suyeon Hwang,

Roberto Astolfi,

Bram Edens

https://dx.doi.org/10.1787/6fc092d8-en

# OECD methodology to estimate SEEA Air Emission Accounts: an update

By Santaro Sakata, Suyeon Hwang, Roberto Astolfi and Bram Edens

# OECD Statistics Working Papers

See all the papers in the series

The OECD Statistics Working Paper Series – managed by the OECD Statistics and Data Directorate – is designed to make available in a timely fashion and to a wider readership selected studies prepared by OECD staff or by outside consultants working on OECD projects. The papers included are of a technical, methodological or statistical policy nature and relate to statistical work relevant to the Organisation. The Working Papers are generally available only in their original language – English or French – with a summary in the other.

This work is published under the responsibility of the Secretary-General of the OECD. The opinions expressed and arguments employed herein do not necessarily reflect the official views of the Member countries of the OECD.

Working Papers describe preliminary results or research in progress by the authors and are published to stimulate discussion on a broad range of issues on which the OECD works. Comments on Working Papers are welcomed and may be sent to the Statistics and Data Directorate, OECD, 2 rue André Pascal, 75775 Paris Cedex 16, France or by email to stat.contact@oecd.org.

This document, as well as any statistical data and map included herein, are without prejudice to the status of or sovereignty over any territory, to the delimitation of international frontiers and boundaries and to the name of any territory, city or area.

The release of this working paper has been authorised by Steve MacFeely, OECD Chief Statistician and Director of the OECD Statistics and Data Directorate.

© OECD (2026)

![](images/816aad35d924ba61a6fbd5e9692b60ec070f322595108efd941056a1cf234cc8.jpg)

## Attribution 4.0 International (CC BY 4.0)

This work is made available under the Creative Commons Attribution 4.0 International licence. By using this work, you accept to be bound by the terms of this licence https://creativecommons.org/licenses/by/4.0/).

Attribution – you must cite the work.

Translations – you must cite the original work, identify changes to the original and add the following text: In the event of any discrepancy between the original work and the translation, only the text of original work should be considered valid.

Adaptations – you must cite the original work and add the following text: This is an adaptation of an original work by the OECD. The opinions expressed and arguments employed in this adaptation should not be reported as representing the official views of the OECD or of its Member countries.

Third-party material – the licence does not apply to third-party material in the work. If using such material, you are responsible for obtaining permission from the third party and for any claims of infringement.

You must not use the OECD logo, visual identity or cover image without express permission or suggest the OECD endorses your use of the work.

Any dispute arising under this licence shall be settled by arbitration in accordance with the Permanent Court of Arbitration (PCA) Arbitration Rules 2012. The seat of arbitration shall be Paris (France). The number of arbitrators shall be one.

## Abstract

This working paper updates the existing OECD methodology for estimating Air Emission Accounts (AEAs) to enhance their comprehensiveness and international comparability. The new methodology draws primarily on data from national greenhouse gas emission inventories, a range of auxiliary data sources including Physical Energy Flow Accounts, as well as OECD experimental estimates of emissions from air and maritime transport.

It improves the quality and granularity of estimates by economic activity (A\*64 industry breakdown), expands the geographical coverage to all OECD countries, and extends the temporal scope of the estimates (1990 to year t-2). It also widens the emission coverage to include international air and maritime transport in line with emission boundaries of the System of Environmental Economic Accounting (SEEA), and incorporates the territory–residence adjustments to comply with the SEEA Central Framework (SEEA-CF).

These improvements complement ongoing international methodological efforts to refine AEA estimates, such as those developed by the IMF and Eurostat, by drawing more extensively on country-specific data and achieving closer alignment with the SEEA-CF.

JEL codes: C82, E01, Q53, Q54, Q56.

## Résumé

Ce document de travail actualise la méthodologie existante de l'OCDE pour l'estimation des comptes d'émissions atmosphériques (AEAs) afin d'en améliorer l'exhaustivité et la comparabilité internationale. La nouvelle méthodologie s'appuie principalement sur les données issues des inventaires nationaux d'émissions de gaz à effet de serre, sur un ensemble de sources de données auxiliaires, notamment les comptes des flux physiques d'énergie, ainsi que sur les estimations expérimentales de l'OCDE relatives aux émissions du transport aérien et maritime.

Elle améliore la qualité et le niveau de détail des estimations par activité économique (ventilation des branches d'activité A\*64), étend la couverture géographique à l'ensemble des pays de l'OCDE et élargit la couverture temporelle des estimations (de 1990 à l'année t - 2). Elle étend également le champ des émissions afin d'inclure le transport aérien et maritime international, conformément aux frontières d'émissions définies par le Système de comptabilité économique et environnementale (SCEE), et intègre les ajustements entre les principes du territoire et de la résidence afin d'assurer la conformité avec le Cadre central du SCEE.

Ces améliorations complètent les travaux méthodologiques internationaux en cours visant à affiner les estimations des comptes d'émissions atmosphériques, notamment ceux menés par le FMI et Eurostat, en recourant plus largement à des données propres à chaque pays et en renforçant l'alignement sur le Cadre central du SCEE.

Classification JEL : C82, E01, Q53, Q54, Q56.

# Acknowledgements

This paper was drafted by Santaro Sakata, Suyeon Hwang, Roberto Astolfi, and Bram Edens from the Statistics and Data Directorate. The authors would like to express their particular gratitude to Manon Roth for her substantial contributions to the project, including the analysis of correspondence tables and the development of the foundational code used to estimate AEAs.

The work was carried out under the supervision of Jorrit Zwijnenburg, Head of Division of the National Accounts Division at the OECD Statistics and Data Directorate.

The authors are particularly grateful to Amanda Penistone (Statistics and Data Directorate) for her thorough review and insightful comments on drafts of this paper. The authors would also like to thank various OECD colleagues for their helpful comments during discussions or on earlier versions of this paper, including Karine Tremblay, Matthew de Queljoe and Pearl Herrero (Statistics and Data Directorate), as well as Norihiko Yamano and Michel Lioussis (Directorate for Science, Technology and Innovation).

The authors are grateful to Australia and Korea for their exchanges and feedback on the updated methodology and/or preliminary results. The authors thank country representatives and international organisations for their review of earlier versions of this paper and for their helpful comments and constructive suggestions provided through the Joint UNECE/OECD Expert Meeting on Implementation of SEEA (March 2026), the OECD Working Party on Environmental Information (WPEI) (March 2026), and the SEEA Central Framework Technical Committee (May 2026).

## Table of contents

OECD Statistics Working Papers 2   
Acknowledgements 5   
1 Introduction 8   
2 Updated methodology 10 General approach 10 Allocation 13 Air and maritime transport emissions 17   
3 Data sources 18 Inventories 18 Auxiliary data sources 20 OECD estimates on $\mathrm{CO}_{2}$ emissions from air and maritime transport 23   
4 Preliminary results 24   
5 Discussion and plausibility checks 27 Key improvements 27 Plausibility checks: Approach 27 Plausibility checks: Results 31   
6 Dissemination Strategy 41   
7 Next steps 43   
References 45   
Annex A. Correspondence table 50   
Annex B. Distribution of misallocated emissions excluding air transport, maritime/fishing, and road transport 56   
Annex C. Plausibility of allocation of road transport emissions 58 Notes 61

## FIGURES

Figure 1. CO₂ emissions with industry/household breakdown 24
Figure 2. Total CO₂ emissions: AEA, CRT/PRIMAP and IEA 25
Figure 3. Industry and household CO₂ emissions share in 2022 26
Figure 4. Comparison between OECD AEA estimates and official AEAs, Country Group 1, 2014-2023 31
Figure 5. Mean Absolute Percentage Error (MAPE) of total CO₂ emissions (excluding air transport, maritime/fishing and road transport), Country Group 1, 2014-2023 33
Figure 6. Correlation coefficients of growth rates between official and estimated AEAs, 2014-2023 34
Figure 7. Mean Absolute Percentage Error (MAPE) of road transport emissions, Country Group 1, 2014-2023 35
Figure 8. Mean Absolute Percentage Error (MAPE) of total CO₂ emissions, Country Group 2, 2014-2023 36
Figure 9. Misallocation share of total CO₂ emissions (excluding air transport, maritime/fishing, and road transport), Country Group 1, 2014-2023 37
Figure 10. Misallocation share by level of industry breakdown and allocation basis (excluding air transport, maritime/fishing, and road transport), Country Group 1, 2014-2023 38
Figure 11. Comparison of misallocation shares under the 2018 and updated methodology, Country Group 1, 2014-2023 39
Figure 12. Misallocation share, Country Group 2, 2014-2023 40
Figure 13. Comparison of industry and household emissions between OECD CO₂ estimates and official GHG total of Australia, 2004/05-2016/17 40
Figure 14. Industry and household distribution of misallocated emissions (excluding air transport, maritime/fishing and road transport), Country Group 1 57
Figure 15. Misallocation share of road transport CO₂ emissions, Country Group 1 58
Figure 16. Misallocation shares, across different auxiliary data 59
Figure 17. Industry and household distribution of misallocated road transport emissions, Country Group 1 60

## TABLES

Table 1. CRT and ISIC classification systems 11  
Table 2. Availability of inventory data after 1990 19  
Table 3. Energy use data availability at the OECD/IEA Data Explorer after 1990 21  
Table 4. Data availability of STAN Database for Structural analysis after 1990 22  
Table 5. Data availability on supply tables 22  
Table 6. Availability of official $\mathrm{CO}_{2}$ AEAs 28  
Table 7. Industry breakdown for misallocation assessment 30

Table A.1. Information related to correspondence between inventory categories and economic and household activities 51
Table A.2. Reference Correspondence Table for CO₂ emissions 53

## 1 Introduction

1. Building on the 2018 OECD methodology (Flachenecker, Guidetti and Pionnier, 2018[1]), this working paper presents an updated approach for estimating Air Emission Accounts (AEAs) in line with the System of Environmental-Economic Accounting (SEEA). The updated methodology improves upon the existing 2018 approach by: (1) enhancing quality and granularity of estimates by economic activity (industry) incorporating additional data sources, (2) extending geographical and temporal coverage; (3) including previously excluded international transport emissions and territory-residence adjustments for mobile sources of emissions to comply with the SEEA Central Framework (SEEA-CF). Together, these improvements strengthen conceptual consistency with SEEA principles, international comparability, and the policy relevance of the resulting AEA estimates. At present, the gas coverage is limited to carbon dioxide $(\mathrm{CO}_{2})$ , and no estimates of total greenhouse gas (GHG) emissions are included. However, the methodology is designed to allow future extensions to other GHGs.

2. This work contributes to international efforts to expand and harmonise the availability of AEA estimates by improving the existing methodology to estimate the AEAs for countries that do not regularly compile official AEAs. Relevant initiatives to date include: (i) the OECD methodology for estimating AEAs (Flachenecker, Guidetti and Pionnier, 2018[1]), which this paper builds upon and updates; (ii) production-based emissions estimates by economic activity developed by the OECD Directorate for Science, Technology and Innovation (STI) in the framework of carbon-footprint calculations (Yamano, Lioussis and Cimper, 2024[2]); (iii) Eurostat's AEA estimates for non-European countries used as inputs to their footprint analysis (Eurostat, 2025[3]); and (iv) the AEA estimation tool developed by the International Monetary Fund (IMF) within the context of the G20 Data Gaps Initiative (DGI) (IMF, 2025[4]).

3. While the 2018 OECD methodology represented a milestone in filling gaps for countries not compiling AEAs, it exhibited several limitations:

\- its geographical coverage was restricted to United Nations Framework Convention on Climate Change (UNFCCC) Annex I countries $^{1}$ ,

• GHG coverage excluded fluorinated greenhouse gases,

\- time coverage and industry disaggregation was constrained by the availability of official inventory and output data,

• estimates were not fully aligned with SEEA boundaries, notably omitting international air and maritime transport,

\- it included no adjustments from territory- to residence-principles (see Box 1),

• output data were the sole auxiliary information used to allocate inventories to industries, and

\- road-transport allocations relied on allocation ratios derived from a narrow sample of European countries. $^{2}$

4. Similarly, the IMF and Eurostat estimation approaches do not implement territory–residence adjustments and rely on unvarying parameters across countries and/or years. The present methodology update addresses these limitations.

5. Despite the ongoing international efforts to expand the AEA coverage, including the launch of a global data collection by the OECD and the UN Statistics Division in 2023, major gaps in the availability of official AEAs persist, although it is mandatory to compile AEAs in the European Union (European Union, 2011[5]). According to the 2025 Global Assessment conducted by the United Nations, only 53 countries have compiled AEAs over the past five years, including non-disseminated pilot compilations (UNCEEA, 2026[6]). Beyond the limited geographical coverage, important differences in gas scope, time-series length, and level of detail by industry further constrain the comparability of the AEAs and hence their analytical and policy use. The updated methodology helps broaden the availability of information by providing granular estimates with the A\*64 industry breakdown, a standard aggregation of economic activities into 64 industries (European Union, 2010[7]), and extending the temporal scope to the period from 1990 to year t-2. It also improves international comparability by aligning with the emissions coverage and principles of the SEEA. It is in principle suitable for all OECD countries, owing to the availability of the required input data. In this research, however, it has been applied to non-EU OECD countries that do not currently report official AEA estimates, and to European countries to support plausibility checks.

6. The resulting AEA estimates can support a wide range of analytical and policy applications. They enable emissions to be analysed within the framework and perimeter of national accounts, i.e. alongside macroeconomic variables such as gross domestic product (GDP), value added, and output. This facilitates assessments of emissions intensity and thus analysis of decoupling between environmental pressures and economic growth. When combined with macroeconomic projections, AEAs can also support estimates of future emissions and monitoring of progress towards emission-reduction targets. Finally, AEAs provide essential inputs for carbon-footprint calculations.

7. This paper is organised as follows. Section 2 describes the updated methodology for estimating AEAs. Section 3 outlines the data sources used and explains how time series gaps are addressed. Section 4 presents preliminary results, and Section 5 assesses their plausibility across different country groups. Section 6 discusses a possible dissemination strategy. Section 7 concludes with next steps. The Annexes provide additional technical detail, including the correspondence table used to allocate emissions from inventories to economic activities (industries) and households, and detailed plausibility checks.

# 2 Updated methodology

## General approach

8. The proposed methodology update maintains the widely applied practice of allocating national inventory emissions to economic activities (classified by the International Standard Industrial Classification of All Economic Activities (ISIC) or its regional equivalents) and households, the so-called “inventory-first” approach (Eurostat, 2015[8]) (see Box 1 for key differences between emission inventories and accounts). This approach helps preserve consistency between emission inventories and accounts and is consistent with the 2018 OECD methodology, as well as with methods used by the IMF, Eurostat, and many national statistical offices. It also offers practical advantages for extending the geographical coverage of AEA estimates compared with the alternative “energy-first” approach, given the limited availability of Physical Energy Flow Accounts (PEFA) data (see Section 3).

9. Under this approach, national inventory data $^{3}$ serve as the starting point, but several adjustments are made. First, system boundaries are adjusted to go from the territory to the residence principle by deducting emissions generated by non-residents on the territory (e.g. domestic aviation by non-resident airlines bunkering at airports of the reporting country) and adding emissions from international transport by residents as well as domestic transport by residents fuelling abroad. Hereto, OECD experimental estimates of $CO_{2}$ emissions from air and maritime transport are applied. Second, GHG inventory emission source categories are mapped to ISIC economic activities and households using a correspondence table. Where an emis

[中间内容因长度限制已省略]

d 80% in Sweden (Flachenecker, Guidetti and Pionnier, 2018 $^{[1]}$ ). Moreover, CO $_{2}$ emissions from motorcycles account for approximately 0.15% of total emissions and 0.7% of road transport emissions for Annex I countries, suggesting that the impact of this assumption on overall allocation results is negligible.

$^{12}$ Fuel breakdowns such as gasoline and diesel oil in the CRT are reported within the road transportation category and therefore refer specifically to transport-related fuel use. Other fuel categories in CRT (i.e. “liquefied petroleum gases (LPG)”, “other liquid fuels”, “gaseous fuels”, and “other fossil fuels”) account for a minor share of total road transport emissions. Road transport emissions are therefore divided only between “diesel oil” and “gasoline” using the shares of these two fuel types (i.e. the sum of adjusted emissions from diesel oil and gasoline matches the category total).

$^{13}$ If P17 is not reported, allocation is performed using the allocation coefficient derived only from P14.

$^{14}$ For instance, in case of Latin American countries UN ECLAC (UN ECLAC, 2026 $^{[52]}$ ).

$^{15}$ The subcategory “Off-road vehicles and other machinery” also appears under 1.A.4.a “Commercial/Institutional”, 1.A.4.b “Residential”, and 1.A.4.c “Agriculture/Forestry/Fishing”. For 1.A.4.a.ii, emissions from Off-road vehicles and other machinery are allocated across the relevant service industries together with the other subcategories under 1.A.4.a, following the standard hierarchy of auxiliary data. Emissions under 1.A.4.b.ii are allocated entirely to “Households, other” (1:1 mapping). Emissions under 1.A.4.c.ii are split between ISIC A01 and A02 using the standard hierarchy of auxiliary data.

$^{16}$ This may introduce a slight error in case of aviation and water activities (e.g. private jets or speedboats) undertaken by activities outside of transport, however this error is expected to be quite small. In addition, emissions figures for fishing can be considered a lower-bound estimate, as a large share of industrial fishing vessels are not captured by publicly available Automatic Identification System (AIS) data (Paolo et al., 2024 $^{[60]}$ ). For countries that do not separately report CRT 1.A.4.c.iii. “Fishing”, emissions are allocated from the parent category 1.A.4.c “Agriculture/Forestry/Fishing” using the standard hierarchy of auxiliary data. In this case, only emissions from vessels excluding fishing are taken from the OECD maritime transport emissions database to avoid potential double-counting.

$^{17}$ The 2018 OECD methodology for estimating AEAs used the CRF as the primary source of inventory data. Consequently, the coverage of the 2018 approach was restricted to the Annex I countries.

$^{18}$ As of February 2026, not all CRT subcategories under CRT 2 IPPU have been extracted by the OECD, but work is ongoing. When all data have been extracted, the calculations will be updated.

$^{19}$ CRT submissions are available from https://unfccc.int/reports?f%5B0%5D=document\_type%3A4593

$^{20}$ National dissemination with longer time series of PEFA is available for Australia, Colombia, and Costa Rica from the following links. https://www.abs.gov.au/statistics/industry/energy/energy-account-australia https://www.dane.gov.co/index.php/estadisticas-por-tema/ambientales/cuenta-satellite-ambiental-csa#cuenta-ambiental-y-economica-de-flujos-de-energia-cae-fe and https://www.bccr.fi.cr/en/Economic-Indicators/environmental-accounts

$^{21}$ Contribution-based methods are not used, unlike the extrapolation of CRT data, as alignment between PEFA and Energy Balances totals is less certain due to differences in accounting principles and the non-identical mapping of products and industries/flows. Under these conditions, changes observed in Energy Balances may not directly correspond to changes in PEFA. Aggregate total growth rates are not applied, as the extrapolated PEFA data are used solely to derive industry allocation coefficients, which require consistency at the industry level rather than at the aggregate level.

$^{22}$ Examples of country-specific road transport statistics that could support such refinements include vehicle-kilometre-travelled data for Korea (Korea Transportation Safety Authority, 2021 $^{[56]}$ ), vehicle registration statistics for Mexico (INEGI, 2026 $^{[54]}$ ), and traffic statistics compiled by the International Road Federation (International Road Federation, 2026 $^{[55]}$ ).

$^{23}$ ISIC U “Activities of extraterritorial organizations and bodies” such as activities of international organisations and diplomatic missions, is considered negligible in terms of $CO_{2}$ emissions and is not included in the correspondence table presented in Annex A. Therefore, the effective number of industries is 63.

$^{24}$ Note that possible inclusion of LULUCF in AEAs is currently discussed under the update of the SEEA Central Framework (Schenau, 2025 $^{[59]}$ ).

$^{25}$ The 2019 Refinement to the 2006 IPCC Guidelines indicates no refinement for the uncertainty range related to the emission factors for $CO_{2}$ (IPCC, 2019 $^{[17]}$ ).

$^{26}$ With a few exceptions including Israel which reports inventory emissions for consecutive years only from 2003 and Sweden which reports confidential values in the key CRT categories such as 1.A.1.b “Petroleum refining” for some years.

$^{27}$ The 2019 Refinement to the 2006 IPCC Guidelines does not introduce any updates to the correspondence between IPCC categories and ISIC economic activities (IPCC, 2019 $^{[17]}$ ).

$^{28}$ ISIC B accounts for about half of energy use of coastal shipping based on the UK's energy data (UK ONS, 2025[53]).
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
