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
- 已识别机构名：`IMF`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份IMF研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# TECHNICAL ASSISTANCE REPORT

REPUBLIC OF AZERBAIJAN

Report on Government Finance Statistics and Public Sector Debt Statistics (November 24–28, 2025) and (February 23–27, 2026)

JULY 2026

PREPARED BY

Roderick O'Mahony (Expert)

Keywords:

JEL Classification Numbers:

H60, H83

Government finance statistics; public sector accounting

The contents of this document constitute technical advice provided by the staff of the International Monetary Fund to the authorities of Azerbaijan (the "CD recipient") in response to their request for technical assistance. Unless the CD recipient specifically objects to such disclosure, this document (in whole or in part) or summaries thereof may be disclosed by the IMF to the IMF Executive Director for Azerbaijan, to other IMF Executive Directors and members of their staff, as well as to other agencies or instrumentalities of the CD recipient, and upon their request, to World Bank staff, and other technical assistance providers and donors with legitimate interest, members of the Steering Committee of CCAMTAC (see Staff Operational Guidance on the Dissemination of Capacity Development Information). Publication or Disclosure of this report (in whole or in part) to parties outside the IMF other than agencies or instrumentalities of the CD recipient, World Bank staff, other technical assistance providers and donors with legitimate interest, members of the Steering Committee of CCAMTAC shall require the explicit consent of the CD recipient and the IMF's Statistics department.

The analysis and policy considerations expressed in this publication are those of the IMF Statistics Department.

International Monetary Fund, IMF Publications
P.O. Box 92780, Washington, DC 20090, U.S.A.
T. +(1) 202.623.7430 • F. +(1) 202.623.7201
publications@IMF.org
IMF.org/pubs

## Acknowledgments

## MEMBERS

![](images/3bc2c75e554d8bb33cc9e02fc905e80cdc87b1bca58f169e2ee824d60681ad38.jpg)  
Armenia

![](images/aab61a7876a13f6336001aaa91917d350ddf10cf6102db89956ae1548f8d0542.jpg)  
Azerbaijan

![](images/01e700865a405ec153e326d4873bd2b6c7b945df9e342ba6d7db6918dc8572fa.jpg)

![](images/8901276bb737bf34de9fad7ca772888626869be153ab2fbff4511533f702e3e8.jpg)

![](images/5080de564050bd4fad2832bf5797855cdc65f10603206c32f3a1c8d2ce4e4f3e.jpg)  
Tajikistan  
Georgia  
Mongolia

![](images/46b0a6eddb804771ab58388d9db0827fbf28120b4a7ebdc17b9389de9439caf4.jpg)  
Turkmenistan

![](images/220f0be12ed56898833dc51c34513047a972ddd51ef94118b3d6e530a1e34129.jpg)  
Kazakhstan

![](images/ecbf29fd94f99cf9fd4ac6d60a2f95cf1a1467d6b02f7f8b0e6cd5b87580afa3.jpg)

![](images/6faf2e774fd4d88cc48854f2f0e6a2a9ad0ffbabd5ece82c62ad3d8f9fe2d3f6.jpg)  
Kyrgyz Republic  
Uzbekistan

## DEVELOPMENT PARTNERS

![](images/357571c9a50d411692a757ba76e512bbc4c5da5d5046c9654ea4ccf7a22a9d11.jpg)  
Switzerland

![](images/e200e32c4eae1fe852b28f2364f83cd44b551fbb999a1105d27ba1da0be40cc2.jpg)  
Russia

![](images/9903794b04dc80a5ed72df2984aa9d36e7fc9844d675fd3c0d68d0105620bc43.jpg)  
China

![](images/1793f1931e3b872c77ab44cc33d7c132173ae2f36f2fa10ed17374c48fe613db.jpg)  
Ministry of Strategy and Finance
Republic of Korea

![](images/0520234d623909173c9acc5700bdbfb8e5e96cd31808af5f0904c244d97cefe5.jpg)  
United States of America

![](images/c1b651152f911c16a6a1a5812013c154e19492282c98b967a3e08fb6b9b9b33a.jpg)  
European Union

![](images/d71573d48ca2b05c11380e68547ccefd2d20e2d81fc7e20d6f464373d1a2edf5.jpg)  
Asian Development Bank

![](images/bec182f7970e8a81b39690e41d1e397bffead75a72ff7e0d62e4a76888d6a4c4.jpg)

![](images/fbc29d5e9087b2e88c04373ff316756bb48206d4e97f4ef2cda991284551ecd9.jpg)  
Poland

## Contents

Acknowledgments....3   
Abbreviations and Acronyms....5   
Summary of Mission Outcomes and Priority Recommendations....6   
Detailed Technical Assessment and Recommendations....8   
A. Improving Quality of GFS....8   
B. Initiating Dissemination of PSDS....9   
C. Other Issues....10   
D. Officials Met During the Mission....11

## Abbreviations and Acronyms

<table><tr><td>AM</td><td>Azerbaijani Manat</td></tr><tr><td>BCG</td><td>Budgetary Central Government</td></tr><tr><td>CBA</td><td>Central Bank of the Republic of Azerbaijan</td></tr><tr><td>CCAMTAC</td><td>Caucasus, Central Asia, and Mongolia Regional Capacity Development Center</td></tr><tr><td>CG</td><td>Central Government</td></tr><tr><td>COFOG</td><td>Classification of Functions of Government</td></tr><tr><td>PDFLMA</td><td>Public Debt and Financial Liabilities Management Agency</td></tr><tr><td>EBF</td><td>Extrabudgetary Fund</td></tr><tr><td>GFS</td><td>Government Finance Statistics</td></tr><tr><td>GFSM 2014</td><td>Government Finance Statistics Manual 2014</td></tr><tr><td>IFRS</td><td>International Financial Reporting Standards</td></tr><tr><td>IPSAS</td><td>International Public Sector Accounting Standards</td></tr><tr><td>KRF</td><td>Karabakh Revival Fund</td></tr><tr><td>LEPL</td><td>Legal Entities of Public Law</td></tr><tr><td>MCD</td><td>Middle East and Central Asia Department</td></tr><tr><td>MOF</td><td>Ministry of Finance</td></tr><tr><td>MTEF</td><td>Medium-Term Expenditure Framework</td></tr><tr><td>PSDS</td><td>Public Sector Debt Statistics</td></tr><tr><td>QPSD</td><td>Quarterly Public Sector Debt (IMF-World Bank Database)</td></tr><tr><td>ROA</td><td>Republic of Azerbaijan</td></tr><tr><td>SB</td><td>State Budget</td></tr><tr><td>SOFAZ</td><td>State Oil Fund of the Republic of Azerbaijan</td></tr><tr><td>SSA</td><td>Social Services Agency</td></tr><tr><td>SAMHI</td><td>State Agency Mandatory Health Insurance</td></tr><tr><td>SSPF</td><td>State Social Protection Fund</td></tr><tr><td>TA</td><td>Technical Assistance</td></tr><tr><td>TD</td><td>Treasury Department</td></tr></table>

## Summary of Mission Outcomes and Priority Recommendations

1. In response to a request from the Ministry of Finance (MOF) of the Republic of Azerbaijan (ROA), and with the support of the IMF's Middle East and Central Asia Department (MCD), the Caucasus, Central Asia, and Mongolia Regional Capacity Development Center (CCAMTAC) conducted a hybrid Technical Assistance (TA) mission during November 2025 and February 2026 to assist the authorities in developing capacity to compile and disseminate quarterly and annual fiscal statistics that support policy-making and IMF surveillance. The mission consisted of (i) the remote segment which took place remotely via Zoom during November 24–28, 2025, and (ii) the in-person segment, which took place in Baku, Azerbaijan, during February 23–27, 2026.

2. The main objectives of the mission were to: (i) provide an outline of GFS concepts specifically targeted for source data providers; (ii) assist the Medium-Term Expenditure Framework (MTEF) Development Center staff in compiling annual GFS for the General Government (GG) for 2024; (iii) extend work on developing quarterly GFS and PSDS that support Fund surveillance; and (iv) review progress since the last TA mission in 2025. The mission also focused on further strengthening the capability and confidence of the compilers of fiscal statistics and the source data providers in addressing issues in the relevant data and the compilation processes, identifying areas for further improvement, assisting compilers in assigning appropriate COFOG codes and promoting collaboration among agencies involved in the fiscal statistics compilation.

3. The mission noted that the annual GFS dataset for 2024 was submitted to the IMF in late 2025 and that the dataset for 2025 can be submitted by July 2026. The mission welcomed the improvement in timeliness for the annual datasets and continued to stress the importance of having timely data available for users. The mission noted that quarterly data was available for budgetary central government (BCG), the State Oil Fund of the Republic of Azerbaijan (SOFAZ) and the Karabakh Revival Fund (KRF) for Q1 and Q2 2025. The mission encouraged the authorities to commence disseminating quarterly GFS as soon as possible once the figures have been finalized for BCG.

4. The mission met with officials from the Public Debt and Financial Liabilities Management Agency (PDFLMA) who agreed to submit quarterly debt data. Officials from the PDFLMA noted that the BCG also included debt expenditure relating to public sector bodies where government undertook to pay loans. These transactions are included in total loan payment (both principal and interest) in BCG figures. To address this anomaly, the mission suggested that the PDFLMA simply report debt figures to the QPSD and analyze its alignment with the BCG data. Both teams agreed to examine this workaround.

5. To support progress in the above work areas, the mission recommended a detailed one-year action plan with the following priority recommendations to improve GFS and PSDS:

## Recommendations

<table><tr><td>Target Date</td><td>Priority Recommendation</td><td>Responsible Institution</td></tr><tr><td>May 2026</td><td>Submit quarterly GFS dataset for Q1 and Q2 2025 for BCG to IMF</td><td>MTEF</td></tr><tr><td>May 2026</td><td>Submit quarterly debt data to QPSD IMF/WB database</td><td>PDFLMA</td></tr><tr><td>July 2026</td><td>Submit annual dataset for 2025 to IMF</td><td>MTEF</td></tr></table>

Further details on the priority recommendations and the related actions/milestones can be found in the action plan under Detailed Technical Assessment and Recommendations.

# Detailed Technical Assessment and Recommendations

<table><tr><td>Priority</td><td>Action/Milestone</td><td>Target Completion Date</td></tr><tr><td colspan="3">Outcome: Further development of GFS data in Azerbaijan</td></tr><tr><td colspan="3">Outcome: Data is compiled and disseminated using the coverage and scope of the latest manual/guide.</td></tr><tr><td colspan="3">Outcome: Data are compiled and disseminated using the classification of the latest manual/guide</td></tr><tr><td>H</td><td>Increase capacity and efficiency of the GFS team.</td><td>Ongoing</td></tr><tr><td>M</td><td>Explore and use supplementary data sources for GFS and PSDS</td><td>Ongoing</td></tr><tr><td>H</td><td>Develop time series on quarterly BCG debt in conjunction with PDFLMA.</td><td>End May 2026</td></tr><tr><td>H</td><td>Finalize Q1 and Q2 2025 data for BCG, SOFAZ and KRF</td><td>End May 2026</td></tr><tr><td>H</td><td>Finalize and transmit the 2025 annual GFS questionnaire to IMF STA.</td><td>End July 2026</td></tr><tr><td>H</td><td>Provide GFS training to data providers to improve quality of GFS input.</td><td>End November 2026</td></tr><tr><td>H</td><td>Update COFOG Classification in new edition of Functional Classification</td><td>End December 2026</td></tr><tr><td>H</td><td>Develop updated PSIT to take account of LEPLs and other EBFs.</td><td>End December 2026</td></tr></table>

## A. Improving Quality of GFS

## Background

6. Azerbaijan is a regular provider of annual GFS for GG and its subsectors to the IMF's GFS database. GFS are compiled using an Excel file which contains the source data, bridging sheets, and output tables. The IMF's annual GFS database (managed by STA's Government Finance Division) contains Azerbaijan's time series data for 2008–2024 for GG and its subsectors (central government, social security funds, state government and local government). Staff of the MTEF Development Centre are currently compiling GFS for 2025 and will submit data for 2025 before the end of July 2026.

7. The source data for GFS is a mixture of IFRS and IPSAS-based annual financial statements which are sufficiently comprehensive and detailed to compile annual GFS. The GFS team in the MTEF Development Center continues to have a good working knowledge of the source data as well as the framework, principles, concepts, and classification system of GFS. It also has access to qualitative information from the sources, which enables them to understand and explain fiscal events underlying the reported numbers.

8. Data provided to the IMF Area Department for surveillance should be consistent with the data submitted to Parliament and those published in the IMF GFS database. Nevertheless, when taking into account the methodological requirements of the Government Finance Statistics Manual 2014 (GFSM 2014) and the prevailing national legal framework, notable discrepancies remain between the GFS reports submitted to the IMF and the annual budget execution reports presented to Parliament. As emphasized in previous technical assistance missions, multiple and parallel data dissemination streams continue to operate within the Ministry of Finance, which undermines data consistency and transparency. In particular, the State Treasury Agency prepares the annual budget execution report on a cash basis, thereby limiting alignment with GFS reporting standards. In this context, the mission reiterated its recommendation that the authorities—specifically the staff of the MTEF Development Center—systematically utilize available accrual-based data as the primary source for IMF reporting. Furthermore, it was advised that such accrual-based information be shared with the IMF’s Area Department to enhance the quality and consistency of fiscal surveillance.

9. As part of the remote mission, the team reviewed the significant discrepancies that arose from the GFS source annual data for 2024 at individual entity level and reduced them significantly to near zero in all cases. A common issue the mission noted was the continued misclassification of net acquisition of non-financial assets by the receiving entities, which were transferred from BCG. These should be classified as other ‘change in volume in assets and liabilities’, and source data providers must be familiar with the understanding of the above the line and below the line items.

10. The mission also examined quarterly data for Q1 and Q2 2025 for BCG, SOFAZ and KRF. While the KRF compilation exercise produced an essentially balanced set of accounts, significant discrepancies were found for BCG and SOFAZ. The mission recommended to staff that they examine the financial assets side of the accounts for BCG (specifically Currency and Deposits, for example assets held in the Central Bank of Azerbaijan (CBA)). For example, if the non-financial accounts showed a surplus or deficit, data users would expect to see some movement in the currency and deposit assets.

## Recommendations:

Submit GFS dataset for 2025 by end July 2026 to the IMF's Statistics Department.

Consult (on an ongoing basis) with STA, including the CCAMTAC GFS-PSDS resident advisor, on specific source data and compilation issues as they arise.

Review existing quarterly data for BCG and SOFAZ for Q1 and Q2 2025 to further reduce the statistical discrepancy and submit the data to the IMF.

\- Continue developing quarterly data for other entities such as LEPLs to improve coverage to Central Government (CG) level.

## B. Initiating Dissemination of PSDS

## Background

11. The quarterly debt securities and loans for BCG statistics are readily available for dissemination from PDFLMA. However, final agreement is required as to which agency should take responsibility for publishing the data and submit it to the joint IMF/WB Quarterly Public Sector Debt (QPSD) database pending the approval of the MOF management.

12. The main issue to address is that there is a difference in the total debt payments that is shown for PDFLMA and that of the MOF. The difference can be explained by the inclusion of loans of public corporations that the MOF agrees to finance although some of the loans are repaid in full by the

Public Corporations, while others will be repaid by Government once it becomes clear that the Public Corporations are unable to pay (which then move onto the Government's balance sheet). The matter is further complicated by the fact that the GFS team are legally required not to split total debt figures between interest payments and transaction in liabilities for public corporations and normal BCG debt operations.

13. The PDFLMA agreed to submit the quarterly debt figures for BCG to the IMF/WB QPSD. The mission further requested that the PDFLMA also provide a breakdown to include long-term debt liabilities that have less than one year to maturity (initially long-term debt but reclassified as short-term debt on a remaining maturity basis). The GFS team agreed to consider appropriate methods to reconcile the difference between the totals provided by each agency.

Recommendations:

The PDFLMA to contact the World Bank to initiate reporting to the QPSD database.

■ Establish a PSDS working group to discuss and report on debt issues to the GFS working group.

## C. Other Issues

14. Further progress in the compilation of sound fiscal statistics continues to depend on the political support and effective building capacities. The Director of MTEF Development Center confirmed interest in further development of GFS, focusing on expanding sector coverage. The mission continued to emphasize that the pace of future developments depends purely on capacity and recommended that the MOF senior staff ensure adequate resources be allocated to the MTEF Development Center. The authorities were encouraged to continue engaging with the CCAMTAC GFS-PSDS resident advisor on the necessary follow-up actions. The Director of MTEF also expressed an interest in hosting a training course for data providers of GFS as part of any subsequent TA.

15. Besides the staff capacity and training issues, consideration should be given to collecting comprehensive source data needed to develop GFS data for entities to be included in the Central Government (CG) sector (e.g., Legal entities of Public Law or LEPLs). It is important to develop an updated Public Sector Institutional Table (PSIT) to ensure consistent classification of public sector entities by the various data compiling and source data providing agencies. In addition, to strengthen the institutional foundation for collaboration among compilers and users of fiscal and debt data for policy making, a technical working group comprising MTEF Development Center, Budget Department, Treasury Agency (TA) and PDFLMA should be established with support from the MOF and management from other government departments.

16. The authorities requested the assistance of the mission to recommend the appropriate COFOG code for several Departments. The mission met with senior officials in the Departments of Finance of Social Sector, Finance of Military Institutions and Law Enforcement Bodies, and Accounting Policy to agree appropriate COFOG codes. In addition, the mission also assisted staff from the MTEF in this regard. The process of aligning the national functional classification with the COFOG is ongoing and is currently being prepared by the authorities. The finalized classification codes will be shared with the mission team and CCAMTAC GFS-PSDS resident advisor once they have been formally approved. The mission encouraged the authorities to reach out to the CCAMTAC GFS-PSDS resident advisor with any subsequent queries as required.

17. It should be noted that the authorities are also interested in developing a new Chart of Accounts system which will result in several significant improvements in GFS reporting. A request for TA, in coordination with PFM, may emerge soon.

18. The mission also provided basic GFS training to members of the State Employment Agency. This was done to facilitate new members on the reporting team.

## D. Officials Met During the Mission

<table><tr><td>Name</td><td>Institution</td></tr><tr><td>Ilham Karimov</td><td>Director of the MTEF Development Centre</td></tr><tr><td>Elnare Kazimova</td><td>Head of the Finance Statistics and Budget Classification Division</td></tr><tr><td>Gunel Aliyeva</td><td>Leading advisor, MTEF Development Centre</td></tr><tr><td>Anar Mehdiyev</td><td>Advisor, MTEF Development Centre</td></tr><tr><td>Firuze Abdullayeva</td><td>Head of the Accounting Policy Department</td></tr><tr><td>Ramiz Garayev</td><td>Deputy Head of the Accounting Policy Department</td></tr><tr><td>Zakir Hajiyev</td><td>Deputy Head of the Social Sector Finance Department</td></tr><tr><td>Nargiz Habibova</td><td>Deputy Head of the Social Sector Finance Department</td></tr><tr><td>Etibar Karimov</td><td>Head of the Department of Finance of Military Institutions and Law Enforcement Bodies</td></tr><tr><td>Sabuhi Jafarov</td><td>Head of the Reporting, Analysis and Risk Management Department, Public Debt and Financial Liabilities Management Agency</td></tr><tr><td>Jala Ahmadova</td><td>Chief advisor, Reporting, Analysis and Risk Management Department, Public Debt and Financial Liabilities Management Agency</td></tr><tr><td>Shams Gasimzadeh</td><td>Head of the Finance Department, State Employment Agency</td></tr><tr><td>Nurlan Tahmazli</td><td>Head of the Accounting Division, State Employment Agency</td></tr><tr><td>Rashad Farzalizadeh</td><td>Head of the Investment and Revenue Division, State Employment Agency</td></tr><tr><td>Naila Dlatova</td><td>Chief specialist - Finance Department, State Employment Agency</td></tr></table>
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
