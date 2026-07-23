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
July 2026

## 2026 GUIDANCE NOTE ON THE FUND'S TRANSPARENCY POLICY

IMF staff regularly produces papers proposing new IMF policies, exploring options for reform, or reviewing existing IMF policies and operations. The Report prepared by IMF staff and completed on July 1, 2026, has been released.

The staff report was issued to the Executive Board for information. The report was prepared by IMF staff. The views expressed in this paper are those of the IMF staff and do not necessarily represent the views of the IMF's Executive Board.

The IMF's transparency policy allows for the deletion of market-sensitive information and premature disclosure of the authorities' policy intentions in published staff reports and other documents.

Electronic copies of IMF Policy Papers are available to the public from http://www.imf.org/external/pp/ppindex.aspx

June 30, 2026

# 2026 GUIDANCE NOTE ON THE FUND'S TRANSPARENCY POLICY

Approved By Christian Mumssen (SPR) Prepared by the Strategy, Policy, and Review Department in consultation with the Legal and the Secretary's Departments

CONTENTS
Glossary 3
I. INTRODUCTION 4
II. COUNTRY DOCUMENTS 6
A. Publication Regime 8
B. Consent to Publication 9
C. Publication Timeline for Staff Reports 10
D. Publication Timeline for Press Releases 16
E. Factual Statements in Case of Delayed or Non-Publication of Country Press Releases and Staff Reports 18
F. Modifications of Country Documents and Press Releases 20
G. Handling and Protecting Confidential Information 28
H. Steps for Publication of Country Documents After Board Consideration 31
I. Communicating with Country Authorities about Publication and Modification of Board Documents 32
III. POLICY DOCUMENTS 33
A. Publication Regime 33
B. Publication Timeline for Policy Documents and Press Releases 34
C. Modifications of Policy Documents 34
D. Press Releases for Policy Documents 37
IV. MULTI-COUNTRY DOCUMENTS 37
A. Multilateral Policy Issues Documents 38

B. Country Background Pages 38
C. Cluster Documents 39

V. ADMINISTRATIVE ERRORS, MODIFICATIONS OF PUBLISHED DOCUMENTS, AND DOCUMENTS PREPARED BY OTHER INSTITUTIONS 41
A. Administrative Errors 41
B. Modification of Published Documents 41
C. Documents Prepared by Other Institutions 42

VI. RESOLVING DISPUTES ABOUT THE APPLICATION OF THE RULES TO MODIFY DOCUMENTS 43

BOXES
1. Main Changes to the Transparency Policy in the 2024 Policy Review 5
2. Guidelines to Prepare and Draft Country Documents 6
3. Steps for Publication of Country Documents After Board Consideration 31
4. Treatment of Multi-Country Documents 40

FIGURES
1. Timeline for Publication of Surveillance Country Documents 12
2. Timeline for Publication of Surveillance Country Documents: Opt-Outs of Non-Objection 14
3. Timeline for Publication of Surveillance Country Document Press Releases 17

APPENDICES
I. Indicative List of Board Documents Subject to the Transparency Policy 44
II. Publication Policies for TA Reports, Safeguards Assessments, IMF Assessment Letters, Misreporting, Overdue Financial Obligations, Delayed Article IV Consultations, and FSAP Documents 47
III. A Reference Guide on Publication Expectations and Timing for Board Documents 50
IV. Publication Timeline for Country Documents and Press Releases 53
V. Publication of PRGS, PRSP, JSAN and HIPC Documents 56
VI. Press Releases: Content and Processing 58
VII. Publication of Documents in Languages Other Than English 65
VIII. Factual Statements in Case of Delayed or Non-Publication of Country Press Releases or Staff Reports 66
IX. How to Submit and Process Requests to Modify Country Documents 74
X. Guidelines on the Treatment of Confidential Information 75
XI. Transparency Policy Information Sheet for Country Authorities 80
XII. The Administrative Errors Procedure 83

## Glossary

AFSSR Assessment of Financial Sector Supervision and Regulation
APR Annual Progress Reports
COM Communications Department on the Observance of Standards and Codes
CRS Common Review System
DAR Detailed Assessment Report
DSA Debt Sustainability Analysis
ECF Extended Credit Facility
ED IMF Executive Director
EPE Ex-Post Evaluation
ERA Enterprise Risk Assessment
ESR External Sector Report
FM Fiscal Monitor
FSAP Financial Sector Assessment Program
FSSA Financial System Stability Assessments
GFSR Global Financial Stability Report
GRA General Resources Account
HIPC Heavily Indebted Poor Countries
IEO Independent Evaluation Office
I-PRSP Interim Poverty Reduction Strategy Papers
JSAN Joint Fund/World Bank Staff Advisory Notes
LEG Legal Department
LICs Low-Income Countries
LOI Letter of Intent
LOT Lapse of Time
MEFP Memorandum of Economic and Financial Policies
PCI Policy Coordination Instrument
PFA Post-Financing Assessment
PMB Program Monitoring with Board Involvement
PRA Ex-Post Peer Reviewed Assessment
PRGT Poverty Reduction and Growth Trust
PRSP Poverty Reduction Strategy Paper
PRGS Poverty Reduction Growth Strategy
ROSC Reports on Observance of Standards and Codes
RSF Resilience and Sustainability Facility
SEC Secretary's Department
SIP Selected Issues Paper
SLL Short-term Liquidity Line
SMP Staff-Monitored Program
SRDSF Sovereign Risk and Debt Sustainability Framework
SPR Strategy, Policy and Review Department
TMU Technical Memorandum of Understanding
UFR Use of Fund Resources
WEO World Economic Outlook

## I. INTRODUCTION

1. The Fund has adopted an overarching principle of transparency as set forth in the preamble to the Fund's Transparency Policy Decision ("Decision" or "Policy"). $^{1}$ The preamble states that the Fund will "strive to disclose documents and information on a timely basis unless strong and specific reasons argue against such disclosure." The preamble further emphasizes that in modifying documents covered by the Decision, the Fund will give due regard to protecting the independence and candor of staff analysis, while recognizing the necessity of modifications of such documents under some limited and defined circumstances.

2. To implement this principle, the Transparency Policy establishes a general presumption of publication and sets out the rules to modify Board documents. These documents include: (i) country documents, (ii) Fund policy documents, and (iii) multi-country documents prepared by staff for consideration or information of the IMF Executive Board (the "Board"). $^{2}$ The specific rules set by the Policy for the publication of these documents and their modification balance the different roles the Fund plays in fulfilling its mandate as both trusted advisor and global economic watchdog. As a trusted advisor, the Fund needs to protect the candor, openness, and confidentiality of its conversations with members. To be a credible advisor and economic watchdog, the Fund and its staff need to be (and be seen as) transparent, independent and candid in their advice, and staff analysis needs to be protected from undue pressures.

3. This note provides guidance to staff to implement the Fund's Transparency Policy. It updates, and replaces, the 2014 Transparency Policy Guidance Note to reflect the recent changes to the Transparency Policy Decision adopted in November 2024 (Box 1). This Guidance Note is organized as follows: section II provides guidance on the publication and the modification of country documents, including press releases, prior to publication, and on the treatment of confidential information; section III covers the publication and modification of policy documents prior to their publication; section IV addresses the procedures to modify and publish multi-country documents; section V covers provisions for rectifying administrative errors and modifying published documents. Finally, section VI considers the process for addressing disagreements about the application of the rules to modify Board documents.

## Box 1. Main Changes to the Transparency Policy in the 2024 Policy Review

## Reinforce the Policy's Principles and Ensure Adequate Coverage of the Policy

\- The Decision now includes, as one of the principles of the Policy, the objective of preserving the independence and candor of staff's views.

\- The Policy incorporates the principle that no changes to published documents should be permitted except under very limited circumstances.

\- Documents received from other institutions, required for Board consideration, are published together with the related staff report, unless the authoring institution requests or the Fund's Board decides otherwise; modifications by the authoring institution are only allowed prior to Board consideration.

## Support Faster Communication of the Board's Activities and Publication of Country Documents

## Press Releases

\- Consent for the publication of press releases is deemed to be provided unless, prior to the conclusion of the Board's consideration, the member explicitly objects or indicates that it requires more time to decide.

\- Any country document press release published separately from the staff report shall indicate the member's publication intention for the staff report.

\- Surveillance country document press releases should be issued no later than two business days after Board consideration. The member can request to postpone their publication up to 7 calendar days after Board consideration if it consents to publish the relevant staff report.

## Staff Reports

\- Consent to publication is deemed to be provided through non-objection unless, prior to the conclusion of Board consideration, the member objects to publication, requests additional time, or consents to publication subject to reaching agreement with the Fund on deletions.

\- If the member requests more time to decide on the publication of a country document, consent is deemed provided after 14 calendar days from Board consideration, unless the member objects to publication or requests additional time. In this latter case, consent is deemed provided 28 calendar days after Board consideration, unless the member objects to publication.

\- If a member objects to publication, a factual statement (or the press release) is issued providing notification that the member does not intend to publish the country report.

## Strengthen and Clarify the Rules and Processes to Modify Board Documents Prior to Publication

\- Limited additions to the authorities' views in surveillance country reports are allowed, subject to safeguards. Such additions should be issued to the Board not later than 2 business days before Board consideration of the relevant document.

\- Limited additions and revisions are allowed to the background section of surveillance document press releases to better reflect wording used in the related staff report and associated documents or to include information discussed during Board consideration and not included in the above-referenced documents; these revisions are in addition to the existing modification categories.

\- Requests to modify Board documents should be normally submitted no later than 7 calendar days after Board consideration. Requests received after 28 calendar days from Board consideration will not be considered.

\- The Policy now incorporates the process to remove confidential information from staff reports.

\- The Policy now incorporates the process for rectifying "administrative errors."

## Widen the Application of Procedures for Resolving Disputes About Modification Rules

\- The existing procedures for resolving disagreements between Management and a member (or between staff and the authorities) on the application of deletion rules would apply to disagreements on any type of modification.

## II. COUNTRY DOCUMENTS

This section provides guidance on the publication of country documents (including staff reports and press releases), their modification prior to publication, as well as the use of factual statements by staff. In addition, it offers practical guidance on preparing and submitting these documents for publication.

4. The Transparency Policy covers the publication of country documents prepared for Board meetings or lapse-of-time (LOT) consideration (“Board consideration”) or issued to the Board for information. $^{3}$ These documents pertain to individual countries and include documents (typically staff reports and press releases) related to surveillance, the use of Fund resources (UFR), and the Policy Coordination Instrument (PCI). They also include documents pertaining to regional surveillance discussions on common policies of a currency union and certain reports arising from Fund technical assistance (Appendix I).

5. Some country-related documents routinely circulated to the Board are not Board documents and are not covered by the Policy. These typically include country-related documents prepared by staff for audiences other than the Board. These documents can be published if both the country's authorities and Management consent to their publication or according to their own policies, when existing. $^{4}$ In addition, documents prepared by other institutions and required for consideration by the Board (e.g., Resilience and Sustainability Facility (RSF) Assessment Letters) are subject to different treatment (see section V.C).

6. In drafting country documents, staff should adhere to specific guidelines to safeguard staff independence and avoid undue pressures (Box 2).

## Box 2. Guidelines to Prepare and Draft Country Documents

\- Non-negotiation of documents. It is a paramount principle of the Fund, aimed at safeguarding the candor and independence of staff views, that staff reports must not be negotiated with country authorities or IMF Executive Directors (EDs). $^{1}$

\- No sharing of draft country documents or parts thereof, with the exceptions listed below. To buttress the prohibition on negotiation, staff may not share draft country documents or portions thereof (e.g., material that will appear in annexes) with country authorities or IMF Executive Directors (EDs). $^{2}$ However, the following can be shared:

Draft of the background section of press releases;

\- Selected Issues Papers (SIP) that do not contain staff advice; if they contain policy advice, only the factual parts can be shared; $^{3}$

Debt Sustainability Analysis (DSA) output (charts, tables, mechanical signal, risk and sustainability assessment), but the write-up, including text in the commentary boxes, should not be shared;

Reports on Observance of Standards and Codes (ROSCs) modules, Ex-Post Peer Reviewed Assessment (PRA) and Ex-Post Evaluation (EPE) reports, Financial Sector Assessment Program (FSAP) aide-mémoires and Technical Notes, Detailed Assessment Reports (DARs), and TA reports.

## Box 2. Guidelines to Prepare and Draft Country Documents (concluded)

In addition, staff is expected to share with the authorities:

The wording describing the authorities' views and to confirm their understanding of the authorities' views.

\- Avoid surprises. To ensure there are no surprises for the authorities when they see the country document, staff should ensure that all major issues covered in the staff report and accompanying documents have been discussed with the authorities and that they are aware of staff's positions. This is especially relevant in cases of combined Article IVs and UFR/PCI reports, given the different presumption of publication for these two types of documents (paragraphs 7–9).

\- Inform the authorities of their right of reply. When there are major differences in views, staff should remind the authorities that they can issue a statement to be published alongside the staff report as part of the document bundle. This “right of reply” statement can be the original ED’s BUFF statement, a revised BUFF statement, a separate statement from the authorities. $^{4}$

\- Provide candid and comprehensive assessments. The authorities' publication intentions should not affect the candor and comprehensiveness of staff reports.

\- Accurately characterize counterparts' views. Counterparts' views should be properly characterized and clearly identified and presented as official views of authorities, institutions, or personal views. When reporting third-party views, staff should identify their source (to the extent permitted by confidentiality needs).

\- Avoid politically charged language. While not shying away from candid assessments of relevant political economy issues, staff should avoid formulations that may be considered insulting or divisive in the member country.

\- Do not include in Board documents information provided by the member based on the understanding that it will remain confidential. In case of doubt, staff should clarify with the authorities whether the information is meant to remain confidential within staff/Management, or whether it can be shared with the Board and/or the public. While certain information cannot be withheld from the Board, (e.g., information required to be reported to the Fund under the Articles of Agreement or that staff considers necessary for the Board to make a decision), there are other modalities for sharing confidential information with the Board (see Section II.G).

\- Use internal services for the translation of documents to be transmitted to Management or the Board. To avoid inaccuracies and reputational risks to the Fund, official documents transmitted to Management and the Board should be based on translations by the Fund's internal services. Machine translated documents not certified by the Fund's services cannot be considered official documents and will not be modified to address translation mistakes unless these fall under the Policy's correction and deletion categories.

$^{1}$ Staff reports present the staff's independent and candid views, and staff should use its independent judgment to decide whether specific issues should be part of a staff report.

$^{2}$ For HIPC documents, this excludes the sections of the DSA that are a tripartite exercise between the Fund, the World Bank, and country authorities. Staff should be aware that the World Bank allows its staff to discuss draft HIPC documents with the authorities. This practice does not extend to Fund staff.

$^{3}$ In general, SIPs are not expected to contain policy advice.

$^{4}$ In addition, consistent with the Decision, the Board's internal work procedures (last updated in January 2026) indicate that a member country that has agreed to publication of a staff report may provide a statement regarding the staff report and the Executive Board's assessment. The statement is published together with the staff report and the press release summarizing the Board's assessment.

## A. Publication Regime

## "Voluntary but Presumed" Publication

## 7. The publication of country documents covered

[中间内容因长度限制已省略]

d will issue an FS stating that the member has objected to the publication of the staff report.

B. Modification of Country Documents and Protection of Confidential Information

## Modifications

\- There are strict rules for modifying country documents after they have been issued to the Board and before publication. Modifications are only allowed for:

➢ Corrections to rectify (i) typographical errors, (ii) data and factual mistakes, (iii) evident ambiguity, and (iv) mischaracterization of the authorities' views.

Deletions of (i) "highly market-sensitive" material that has a clear risk of triggering a disruptive market reaction in the near term, and (ii) premature disclosure of the authorities' policy intentions that could undermine policy implementation. Politically sensitive information that does not meet either of the above criteria shall not be deleted.

Additions to the authorities' views in surveillance staff reports on main issues or policy recommendations covered in the staff report on which the report includes no views. Such additions are limited to an indicative limit of no more than 30–40 words per section.

\- Requests for corrections and deletions are expected to be submitted no later than two business days before the date of the Board's consideration and normally no later than 7 calendar days from Board consideration. However, correction requests received after Board consideration will only be made if the failure to make the correction would undermine the overall value of the publication. In any case, requests for modifications (corrections and deletions) submitted more than 28 days after Board consideration will not be considered.

\- Additions to the authorities' views need to be issued to the Board at least two business days ahead of the Board's consideration.

\- Modifications to published documents are generally not allowed, with very few exceptions.

## Resolving disagreements

\- In case of disagreement between staff and the member about the application of the rules to modify Board documents, the member may request that their requests be considered by Management. Any disagreements will be resolved in accordance with the provisions of the Transparency Policy.

## Confidential information

\- The authorities should communicate clearly to staff if they wish to keep certain information confidential. The Fund has a comprehensive legal framework for safeguarding confidential information (see 2026 Transparency Policy Guidance Note).

## Appendix XII. The Administrative Errors Procedure $^{1}$

This Appendix provides the procedure to rectify administrative errors that occurred in the process of submitting documents to the Board (section V.1). This procedure is expected to be rarely used.

The rectification of administrative errors is only allowed for the specific cases set forth under the Transparency Policy. Administrative errors include cases when staff circulates to the Board:

(i) A document in which key elements necessary for Board consideration are missing or incomplete (e.g., Debt Sustainability Analysis tables and charts, External Sector Assessment, or structural benchmarks tables);

(ii) A document with an entirely wrong attachment (e.g., LOI for a different country or program review);

(iii) An earlier version of a document (i.e., an early draft) that was not approved by Management, instead of the finalized version that existed at the time of the initial Board circulation, or an entirely wrong document (e.g., a document not pertaining to the specific topic under Board consideration).

Rectifying an administrative error requires reissuing to the Board the specific pages of the original document or, in rare cases, the full document. If the administrative error is limited (e.g., cases (i)-(ii) above) and specific tables, figures, attachments, or a few pages are missing or incomplete or wrong, a supplement to the main document will be issued to the Board indicating that the original page(s) containing the identified errors are replaced. $^{2}$ The rectification of errors like in example (iii) above would require the reissuance of the full document. In all cases, the Board will be informed of the administrative error, which will be identified in the Secretary's cover issued to the Board, as well as its rectification.

The rectification of administrative errors follows specific procedures. As a first step, the authoring department should consult with SPR and SEC (SECDO@imf.org) to determine whether an administrative error has occurred under the rules of the Policy. If SEC, in consultation with SPR, determines that the error qualifies as an administrative error, the authoring departments will:

• Prepare the redlined pages or paper to rectify the error, in consultation with SEC;

\- Notify Management (e.g., via email or memorandum copied to SEC and SPR) explaining the administrative error and providing details on the implications of rectifying the error for the thrust of the document.

\- Inform the ED(s) concerned of the administrative error prior to the issuance of the corrected documents to the Board.

\- Submit to SEC the correct version of the pages or the modified document with rectified errors for circulation to the Board (no redlined version). $^{3}$

Administrative errors should be rectified at least two business days before the date of Board consideration or the deadline to request a Board meeting for LOT cases. This timeline, specified in the Policy, aims to ensure that the Board discussion is based on the correct version of the documents. If the error is discovered too close to the Board meeting date or the LOT object by date, the date of Board consideration will need to be adjusted.
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
