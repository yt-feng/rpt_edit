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
Peer Review on Transparency and Exchange of Information on Request

TANZANIA

2026 (Second Round)

# Global Forum on Transparency and Exchange of Information for Tax Purposes: Tanzania 2026 (Second Round)

Peer Review on Transparency and Exchange of Information on Request

This peer review report was approved by the Peer Review and Monitoring Group of the Global Forum on Transparency and Exchange of Information for Tax Purposes (Global Forum) on 23 June 2026 and adopted by the Global Forum members on 23 July 2026. It was prepared for publication by the Global Forum Secretariat.

This document, as well as any data and map included herein, are without prejudice to the status of or sovereignty over any territory, to the delimitation of international frontiers and boundaries and to the name of any territory, city or area.

The statistical data for Israel are supplied by and under the responsibility of the relevant Israeli authorities. The use of such data by the OECD is without prejudice to the status of the Golan Heights, East Jerusalem and Israeli settlements in the West Bank under the terms of international law.

Note by the Republic of Türkiye

The information in this document with reference to “Cyprus” relates to the southern part of the Island. There is no single authority representing both Turkish and Greek Cypriot people on the Island. Türkiye recognises the Turkish Republic of Northern Cyprus (TRNC). Until a lasting and equitable solution is found within the context of the United Nations, Türkiye shall preserve its position concerning the “Cyprus issue”.

Note by all the European Union Member States of the OECD and the European Union

The Republic of Cyprus is recognised by all members of the United Nations with the exception of Türkiye. The information in this document relates to the area under the effective control of the Government of the Republic of Cyprus.

Please cite this publication as: OECD (2026), Global Forum on Transparency and Exchange of Information for Tax Purposes: Tanzania 2026 (Second Round): Peer Review on Transparency and Exchange of Information on Request, Global Forum on Transparency and Exchange of Information for Tax Purposes, OECD Publishing, Paris, https://doi.org/10.1787/55831c5b-en.

Global Forum on Transparency and Exchange of Information for Tax Purposes

ISSN 2219-469X (online)

Photo credits: OECD with cover illustration by Renaud Madignier.

Corrigenda to OECD publications may be found at:

https://www.oecd.org/en/publications/support/corrigenda.html.

© OECD 2026

![](images/4756cb76e4f166d2608a02feca699c1014d2312e9e462317da28dc93cb2faa87.jpg)

Attribution 4.0 International (CC BY 4.0)

This work is made available under the Creative Commons Attribution 4.0 International licence. By using this work, you accept to be bound by the terms of this licence (https://creativecommons.org/licenses/by/4.0/).

Attribution – you must cite the work.

Translations – you must cite the original work, identify changes to the original and add the following text: In the event of any discrepancy between the original work and the translation, only the text of original work should be considered valid.

Adaptations – you must cite the original work and add the following text: This is an adaptation of an original work by the OECD. The opinions expressed and arguments employed in this adaptation should not be reported as representing the official views of the OECD or of its Member countries.

Third-party material – the licence does not apply to third-party material in the work. If using such material, you are responsible for obtaining permission from the third party and for any claims of infringement.

You must not use the OECD logo, visual identity or cover image without express permission or suggest the OECD endorses your use of the work.

Any dispute arising under this licence shall be settled by arbitration in accordance with the Permanent Court of Arbitration (PCA) Arbitration Rules 2012. The seat of arbitration shall be Paris (France). The number of arbitrators shall be one.

## Table of contents

Abbreviations and acronyms 4
Executive summary 5
Summary of determinations, ratings and recommendations 8
Overview of Tanzania 12
A Availability of information 17
A.1 Legal and beneficial ownership and identity information 17
A.2 Accounting records 56
A.3 Banking Information 69
B Access to information 76
B.1 Competent authority's ability to obtain and provide information 76
B.2 Notification requirements, rights and safeguards 80
C Exchange of information 82
C.1 Exchange of information mechanisms 82
C.2 Exchange of information mechanisms with all relevant partners 89
C.3 Confidentiality 90
C.4 Rights and safeguards of taxpayers and third parties 95
C.5 Requesting and providing information in an effective manner 95
Annex 1. List of in-text recommendations 102
Annex 2. List of Tanzania's EOI mechanisms 104
Annex 3. Methodology for the review 105
Annex 4. Tanzania's response to the review report 108

## Abbreviations and acronyms

<table><tr><td>Abbreviation</td><td>Definition</td></tr><tr><td>2016 Terms of Reference</td><td>Terms of Reference related to EOIR, as approved by the Global Forum on 29-30 October 2015</td></tr><tr><td>AML</td><td>Anti-Money Laundering</td></tr><tr><td>AML/CFT</td><td>Anti-Money Laundering / Countering the Financing of Terrorism</td></tr><tr><td>AMLPOCA</td><td>Anti-Money Laundering and Proceeds of Crime Act</td></tr><tr><td>BFIA</td><td>Banking and Financial Institutions Act</td></tr><tr><td>BOT</td><td>Bank of Tanzania</td></tr><tr><td>BPRA</td><td>Business and Property Registration Agency (Zanzibar)</td></tr><tr><td>BRELA</td><td>Business Registration and Licensing Agency (Tanzania Mainland)</td></tr><tr><td>CDD</td><td>Customer Due Diligence</td></tr><tr><td>CIN</td><td>Company Identification Number</td></tr><tr><td>DTC</td><td>Double Taxation Convention</td></tr><tr><td>EOI</td><td>Exchange of Information</td></tr><tr><td>EOIR</td><td>Exchange of Information on Request</td></tr><tr><td>EUR</td><td>Currency of the European Union</td></tr><tr><td>FATF</td><td>Financial Action Task Force</td></tr><tr><td>FIU</td><td>Financial Intelligence Unit</td></tr><tr><td>Global Forum</td><td>Global Forum on Transparency and Exchange of Information for Tax Purposes</td></tr><tr><td>IFRS</td><td>International Financial Reporting Standard</td></tr><tr><td>ITA</td><td>Income Tax Act</td></tr><tr><td>KYC</td><td>Know Your Customer</td></tr><tr><td>Multilateral Convention</td><td>Convention on Mutual Administrative Assistance in Tax Matters, as amended in 2010</td></tr><tr><td>NGO</td><td>Non-Governmental Organisation</td></tr><tr><td>ORS</td><td>Online Registration System</td></tr><tr><td>RITA</td><td>Registration, Insolvency and Trusteeship Agency</td></tr><tr><td>SADC</td><td>South African Development Community</td></tr><tr><td>TAA</td><td>Tax Administration Act (as revised in 2023)</td></tr><tr><td>TAPA</td><td>Tax Administration and Procedures Act (Zanzibar)</td></tr><tr><td>TIA</td><td>Trustees&#x27; Incorporation Act</td></tr><tr><td>TIEA</td><td>Tax Information Exchange Agreement</td></tr><tr><td>TIN</td><td>Taxpayer Identification Number</td></tr><tr><td>TRA</td><td>Tanzania Revenue Authority</td></tr><tr><td>TZS</td><td>Tanzanian Shilling</td></tr><tr><td>VAT</td><td>Value Added Tax</td></tr><tr><td>ZanID</td><td>Zanzibar Identification Number</td></tr><tr><td>ZRA</td><td>Zanzibar Revenue Authority</td></tr></table>

# Executive summary

1. This report analyses the implementation of the standard on transparency and exchange of information on request in the United Republic of Tanzania (Tanzania) in the second round of reviews conducted by the Global Forum. This review was carried out in two phases, with the adoption in 2021 of a report evaluating Tanzania's legal and regulatory framework (Phase 1). This report supplements the Phase 1 report with an evaluation of the legal and regulatory framework in force as of 13 May 2026, including changes since 2021, and the implementation of the standard in practice, particularly in respect of exchange of information (EOI) requests received and sent during the review period from 1 April 2022 to 31 March 2025 (see Annex 3).

2. This report concludes that Tanzania is rated overall Largely Compliant with the standard.

Summary table of determinations and ratings

<table><tr><td colspan="2">Element</td><td>Determinations</td><td>Ratings</td></tr><tr><td>A.1</td><td>Availability of ownership and identity information</td><td>Needs improvement</td><td>Partially Compliant</td></tr><tr><td>A.2</td><td>Availability of accounting information</td><td>Needs improvement</td><td>Largely Compliant</td></tr><tr><td>A.3</td><td>Availability of banking information</td><td>Needs improvement</td><td>Largely Compliant</td></tr><tr><td>B.1</td><td>Access to information</td><td>In place</td><td>Compliant</td></tr><tr><td>B.2</td><td>Notification and appeals</td><td>In place</td><td>Compliant</td></tr><tr><td>C.1</td><td>EOIR instruments</td><td>Needs improvement</td><td>Largely Compliant</td></tr><tr><td>C.2</td><td>Network of EOIR relationships</td><td>In place</td><td>Compliant</td></tr><tr><td>C.3</td><td>Confidentiality</td><td>In place</td><td>Compliant</td></tr><tr><td>C.4</td><td>Rights and safeguards</td><td>In place</td><td>Compliant</td></tr><tr><td>C.5</td><td>Effective exchange of information</td><td>Not applicable</td><td>Largely Compliant</td></tr><tr><td></td><td>Overall rating</td><td colspan="2">Largely Compliant</td></tr></table>

Note: The three-scale determinations for the legal and regulatory framework are In place, In place but needs improvement, Not in place. The four-scale ratings for the legal and regulatory framework and its implementation in practice are Compliant, Largely Compliant, Partially Compliant and Non-Compliant.

## Transparency framework

3. Tanzania joined the Global Forum in 2015 and since then has taken steps to comply with the standard. The company laws of Tanzania Mainland and Zanzibar provide for the availability of up-to-date and accurate legal ownership information and require its submission to the respective Registrars. Similarly, the respective business registration acts and the tax law obligations ensure availability of identity information on partnerships. Trusts are recognised only in Tanzania Mainland and the availability of identity information on trusts is provided through obligations in the Trustees' Incorporation Act.

4. For the availability of beneficial ownership information, Tanzania has improved its AML framework for Tanzania Mainland and Zanzibar and has introduced updated AML Regulations. In 2021, Tanzania introduced requirements under the Companies Act of Tanzania Mainland requiring companies to maintain beneficial ownership information and submit it to the Registrar. Tanzania has operationalised a new centralised beneficial ownership register for Tanzania Mainland maintained with the Registrar. Beneficial Ownership Regulations have been issued. The Companies Act of Zanzibar has been similarly amended and regulations for beneficial ownership issued, and a beneficial ownership register is being operationalised. Changes have also been introduced to the Business Names (Registration) Act and the Trustees' Incorporation Act to include obligations for availability of beneficial ownership information.

5. The availability of accounting information is ensured through the tax law obligations, and is further supported by relevant provisions in the respective governing laws of companies, partnerships and trusts. The tax administration's oversight is instrumental in effective implementation of the requirements in this regard.

6. Banking information is available primarily through the requirements under the anti-money laundering framework which requires identity, beneficial ownership and transactional information for all bank accounts. The Bank of Tanzania oversees these obligations.

## Key recommendations

7. The main recommendations pertain to the availability of legal and beneficial ownership information and the implementation and enforcement of the legal framework. Tanzania's legal framework permits nominee shareholdings in companies but does not have obligations for disclosing the nominee status to the company or any public authority. Additionally, Zanzibar's legal framework permits issuance of bearer share warrants by public companies. While Zanzibar amended its laws to address this issue, the amendments only allow the Registrar some oversight over issuance of bearer share warrants but will not ensure the availability of information on identity of holders of such warrants. Tanzania is recommended to address these issues.

8. While the definition of beneficial ownership was recently improved through amendments in the AML framework, some aspects of the definition should be clarified further to ensure identification of beneficial owners in line with the standard. Further, while the AML framework plays a central role in availability of beneficial ownership information in Tanzania for relevant entities and arrangements, there is no specified frequency for updating beneficial ownership information, which could result in beneficial ownership being out of date in some cases. This issue affects the availability of ownership information under Element A.1 and of banking information under Element A.3.

9. The centralised beneficial ownership register is still being populated in Tanzania Mainland and is yet to be operationalised in Zanzibar. There has been limited oversight on the availability of beneficial ownership by the Registrars in the two parts of Tanzania. Further, the supervision and oversight by AML authorities is uneven and needs to be strengthened.

10. The existence of companies that are non-compliant with various registration and filing requirements poses risks to the availability of legal, beneficial and accounting information (Elements A.1 and A.2) and Tanzania is recommended to take suitable supervisory steps to reduce their number and associated risks.

11. Until recently, Tanzania's legal framework did not provide clear retention requirements in respect of accounting records (including identifying a responsible person) when companies cease to exist. While Tanzania Mainland's laws were amended on this aspect, Zanzibar's legal framework continues to present this legal gap, and Tanzania is recommended to address it.

## Exchange of information

12. Tanzania's EOI network is small, with 13 Double Taxation Conventions (DTCs) of which 11 are in force. Five treaties are not in line with the standard, which could result in limiting the information that Tanzania can exchange. Tanzania also signed the Agreement on Assistance in Tax Matters of the Southern African Development Community in 2012. Tanzania has not taken steps to complete its ratification and notification process. Inordinate delay is noted in this regard, as several other parties to the agreement have already completed the steps needed at their end. Tanzania is therefore recommended to bring its EOI network to the standard.

13. During the review period, Tanzania received two EOI requests and sent four requests. Tanzania increased the resources available for EOI and put in place an updated EOI manual, but the effect of these improvements could not be fully assessed in practice and hence, Tanzania is recommended to monitor the implementation of its EOI function to ensure its effectiveness.

14. The two requests pertaining to the review period had to be resent by the treaty partner because the contact details available on the Competent Authority website were incorrect during the last six months of the review period due to the change in the Competent Authority official. Tanzania has been recommended to ensure that treaty partners always remain aware of the correct contact details of the Competent Authority.

## Overall rating

15. Tanzania is rated Compliant on Elements B.1, B.2, C.2, C.3 and C.4, Largely Compliant on Elements A.2, A.3, C.1 and C.5 and Partially Compliant on Element A.1. Tanzania is therefore rated overall Largely Compliant with the EOIR standard on a global consideration of its compliance with the individual Elements.

16. This report was approved at the Peer Review and Monitoring Group of the Global Forum on 23 June 2026 and was adopted by the Global Forum on 23 July 2026. A self-assessment report on the steps undertaken by Tanzania to address the recommendations made in this report should be provided to the Peer Review and Monitoring Group in accordance with the methodology for enhanced monitoring.

# Summary of determinations, ratings and recommendations

<table><tr><td>Determinations and ratings</td><td>Factors underlying Recommendations</td><td>Recommendations</td></tr><tr><td colspan="3">Jurisdictions should ensure that ownership and identity information, including information on legal and beneficial owners, for all relevant entities and arrangements is available to their competent authorities (Element A.1)</td></tr><tr><td rowspan="4">The legal and regulatory framework is in place but needs improvement</td><td>Nominee shareholding is possible under Tanzania's company laws in Tanzania Mainland and Zanzibar. The Anti-Money Laundering legal framework requires identification of persons acting on behalf of another person while entering into business relationships and identification of beneficial ownership. However, there is no requirement on nominees to disclose their nominee status to the companies or to any public authorities.</td><td>Tanzania is recommended to ensure that in all cases where nominee shareholding exists in companies, such nominee arrangements are known to the companies or to the authorities and identity information on the nominator is available in line with the standard.</td></tr><tr><td>In 2022, Tanzania updated its Anti-Money Laundering laws applicable to Tanzania Mainland and Zanzibar to provide a definition of beneficial owner generally in line with the standard. This same definition applies in the context of the governing laws for companies, partnerships and trusts, requiring them to keep information on their beneficial owners. However, for legal persons like companies, guidance is missing on the concept of “control by means other than ownership”. Similarly, guidance is missing on the “look through approach” where any of the partners of a partnership or parties to a trust are themselves legal persons or arrangements.</td><td>Tanzania is recommended to ensure that the definition of beneficial owner as it applies to companies, partnerships and trusts is sufficient

[中间内容因长度限制已省略]

ot take place. Consequently, the review of the Tanzania has been conducted in two phases, with a desk-based Phase 1 review leading to the adoption in November 2021 of the report assessing the legal and regulatory framework of the Tanzania against the 2016 Terms of Reference (Phase 1 report). The subsequent scheduling of the Phase 2 review with an on-site visit then took account of the limited experience of Tanzania in exchange of information (based on the new section V of the Methodology (as amended in 2021)).

The present review complements the first report with an assessment of the practical implementation of the standard, including in respect of exchange of information requests received and sent during the review period from 1 April 2022 to 31 March 2025. Changes made to the legal framework since the Phase 1 review as at 13 May 2022 have also been assessed.

The evaluation is based on information available to the assessment team, Tanzania's responses to the EOIR questionnaire, inputs from partner jurisdictions, as well as information provided by the Tanzanian authorities during the on-site visit that took place from 19 to 23 January 2026 in Dar es Salaam, Tanzania. Information on Tanzania's reviews is listed in the table below.

## Summary of reviews

<table><tr><td>Review</td><td>Assessment team</td><td>Period under Review</td><td>Legal Framework as on</td><td>Date of adoption by Global Forum</td></tr><tr><td>Round 2Phase 1</td><td>Mr Arief Syahriza (Indonesia),Mr Marcus Elizabeth (Seychelles) andMr Puneet Gulati (Global Forum Secretariat)</td><td>Not applicable</td><td>1 September 2021</td><td>18 November 2021</td></tr><tr><td>Round 2Phase 2</td><td>Ms Jolanda Roeloffs (the Netherlands),Mr Marcus Elizabeth (Seychelles) andMr Puneet Gulati (Global Forum Secretariat)</td><td>1 April 2022 to 31 March 2025</td><td>13 May 2026</td><td>23 July 2026</td></tr></table>

# Annex 4. Tanzania's response to the review report $^{47}$

This is the first Exchange of Information on Request (EOIR) peer review for Tanzania ever since joining the Global Forum in 2015 for which a compliance rating has been assigned. The current review is a follow up to the previous Phase 1 review completed in 2021 that was dedicated on assessing only the relevant EOIR legal framework. In this respect, Tanzania confirms that in the current review adequate consultations were made with the assessment team throughout the review process and therefore agrees that the report reflects the status of the EOIR legal framework and its implementation in practice. Accordingly, Tanzania genuinely appreciates the assessment team for their hard work and dedication, the Global Forum Secretariat for incredible technical support prior to the review and the PRMG for valuable comments and guidance.

Further, although the current review report identifies some gaps in the EOIR legal framework and practice, it however clearly demonstrates substantial progress made since completion of the Phase 1 review in 2021. In diverse fronts the report vividly demonstrates Tanzania's unwavering commitment to implement the international tax transparency and EOIR standard. Accordingly, in the same spirit, Tanzania would like to re-affirm its continued commitment to implement all the recommendations of the report to ensure full compliance with the standard. More specifically, Tanzania is committed to take the necessary steps to sign and ratify the Multilateral Convention on Mutual Administrative Assistance in Tax Matters to deliberately expand exchange of information relationship with all members of the Global Forum that are part to the convention.

# GLOBAL FORUM ON TRANSPARENCY AND EXCHANGE OF INFORMATION FOR TAX PURPOSES

# Peer Review on Transparency and Exchange of Information on Request TANZANIA 2026 (Second Round)

The Global Forum on Transparency and Exchange of Information for Tax Purposes is a multilateral framework within which over 170 jurisdictions participate on an equal footing.

The Global Forum monitors and peer reviews the implementation of the international standards on transparency and exchange of information on request (EOIR) and on automatic exchange of information. The EOIR provides for international exchange on request of information foreseeably relevant to the administration or enforcement of the tax laws of a requesting party. All Global Forum members have agreed to have their implementation of the EOIR standard assessed by peer review. In addition, non-members that are relevant to the Global Forum's work are also subject to review. The legal and regulatory framework of each jurisdiction is assessed, as is the implementation of that framework in practice. The final result is an overall rating of the compliance of the jurisdiction with the standard.

The first round of reviews was conducted from 2010 to 2016. A second round of reviews started in 2016. Peer reviews are generally conducted in one go, but they can be conducted in two separate reviews, with a Phase 1 reviewing the legal framework, followed by a Phase 2 focussing on practice. Reviews are phased when jurisdictions have limited EOIR experience or in exceptional circumstances, such as the COVID-19 pandemic. The review reports are published and assessed jurisdictions are expected to follow up on any recommendations made. The ultimate goal is to help jurisdictions to effectively implement the standard of transparency and exchange of information on request for tax purposes.

This peer review report analyses the practical implementation of the standard on transparency and exchange of information on request (EOIR) for Tanzania, as part of the second round of reviews conducted by the Global Forum since 2016.
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
