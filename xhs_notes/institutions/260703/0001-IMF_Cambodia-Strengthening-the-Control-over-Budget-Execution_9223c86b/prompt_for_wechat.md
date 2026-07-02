你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`IMF`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：加入社群，领取完整研报解读与原始图表。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份IMF研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
HIGH-LEVEL SUMMARY
TECHNICAL ASSISTANCE
REPORT

CAMBODIA
STRENGTHENING THE CONTROL
OVER BUDGET EXECUTION

March 2026

Prepared By Jean-Luc Helis, Sha Wen, Davit Gamkrelidze, Anupam Raj

Authoring Departments/Institutions:

Fiscal Affairs Department (FAD)

IMF Capacity Development Office in Thailand (CDOT)

# High-Level Summary Technical Assistance Report Fiscal Affairs Department

Strengthening the Control Over Budget Execution
Prepared by Jean-Luc Helis, Sha Wen, Davit Gamkrelidze and Anupam Raj

The High-Level Summary Technical Assistance Report series provides high-level summaries of the assistance provided to IMF capacity development recipients, describing the high-level objectives, findings, and recommendations.

ABSTRACT: The technical assistance identifies strengths in budget execution – including in the legal framework, digitalization, cash management and implementation of the Treasury Single Account (TSA) – and in fiscal responsibility and upstream investment planning but also highlights the need to continue reforms in these areas. The report emphasizes the need to extend and enhance the FMIS to improve cash balance visibility, automatic reconciliation and commitment recording; strengthen the identification and management of cash advances and public arrears; fully implement the TSA system; and develop a more active cash management.

JEL Classification Numbers H61, H63, H83

Keywords: Budget execution, FMIS, cash advances, arrears, cash management and TSA

The contents of this document constitute a high-level summary of technical advice provided by the staff of the International Monetary Fund (IMF) to the authorities of Cambodia (the "CD recipient") in response to their request for capacity development. Unless the CD recipient specifically objects within 30 business days of its transmittal, the IMF will publish this high-level summary on IMF.org (see Staff Operational Guidance on the Dissemination of Capacity Development Information).

International Monetary Fund, IMF Publications
P.O. Box 92780, Washington, DC 20090, U.S.A.
T. +(1) 202.623.7430 • F. +(1) 202.623.7201
publications@IMF.org
IMF.org/pubs

## Background

Upon the request of the Ministry of Finance and Economics (MEF) of Cambodia, a two-week in-country technical assistance (TA) mission was conducted in Phnom Penh on October 15–29, 2025. The TA aimed to undertake a comprehensive strategic review of the budget execution processes, managed by the General Department of Budgeting (GDB) and the General Department of National Treasury (GDNT), looking at areas to strengthen and automate processes and controls, including through the FMIS, to improve the efficiency of expenditure execution. Additionally, at GDNT's request, the mission provided a three-day training on cash forecasting.

## Summary of Findings

Since 2004, the Royal Government of Cambodia (RGC) has been carrying out an ambitious and sequenced Public Financial Management Reform Program (PFMRP) to modernize its public financial management (PFM) systems and practices. Various policies and strategies, including the updated Budget System Reform Strategy (BSRS) 2025-28 and the recently adopted Road Map for Managing Public Arrears 2025–2028 ("the Roadmap") accompany the implementation of the reform program.

Significant progress has been made over the last two decades on budget execution. Recent progress includes: a strengthened legal framework for PFM, with the 2023 Law on Public Finance System and Sub-Decree on Budget and Public Accounting Management, and two new sub-Decrees concerning the Budget Control Units within line ministries (LMs) and the Authority and Responsibilities of Budget Controllers; improved fiscal and budget management; and enhanced digital transformation. An important achievement has been the sustainability of the reform process over the years, with strong political commitment and ownership, and continuous support and involvement of the General Secretariat of the Public Financial Management Reform Steering Committee (GSC) and the main General Departments of the MEF.

The authorities, however, recognize that important efforts are still needed to fully implement priority reforms in the area of budget execution. These reforms, also identified in the roadmap, include the full implementation and use of the FMIS, speeding up business process streamlining for the remaining LMs to improve timeliness of financial transactions, efficiently closing the budget process at the end of the fiscal year, and effective delegation of budget management authority to budget entities. Other key reforms include strengthening public investment management, progressively decentralizing public procurement, better managing fiscal risks and cash advances, improving fiscal reporting, enhancing cash management, and developing a sound treasury single account (TSA) system.

## Summary of Recommendations

The mission assisted the authorities in developing a priority action plan to operationalize the implementation of the reform roadmap for the period 2026-28. Measurables performance indicators have been proposed to monitor the implementation of the priority measures and ensure rigorous implementation of the expected results. The priority recommendations concern the following:

\- FMIS Expansion and Enhancement. While the FMIS is the central digital tool for PFM with most entities adopting it, new modules like e-Procurement and e-Invoice need to be finalized and implemented. Converting all remaining unauthorized budget entities into fully authorized budget entities by 2027 should boost budget execution efficiency by giving them direct access to FMIS and ability to use electronic funds transfer (EFT). Expanding FMIS linkage with banks and revenue systems will give a better view into balances of all non-TSA government accounts such as cash advance accounts and project accounts, and improve balance visibility, automatic reconciliation, and commitment recording. The FMIS functionality to record multi-year commitments can also be used to record recurrent commitments for a budget year in its preceding year to allow the procurement process to start early, making the expenditure more even across the quarters of the fiscal year.

\- Cash Advances and Arrears Control. To ensure the full implementation of the Roadmap, the MEF should develop and adopt the necessary legal framework and further align the definition of expenditure arrears with international practices. In addition, to mitigate the impact of lengthy budget execution processes on the accumulation of arrears, the MEF could consider allowing the internal preparation and clearance of commitment requests before the start of the fiscal year and introducing tiered approval thresholds for commitment controls.

\- Treasury Single Account (TSA) and Cash Flow Forecasting. While revenue consolidation under TSA is strong, oversight and reconciliation of expenditure accounts outside TSA should be strengthened. Enhancing the legal framework is critical to provide clear monitoring rules, reporting obligations, and accountability for non-compliance, account visibility, phased TSA expansion, and improving cash forecasting quality and governance.

\- Active Cash Management. Linking FMIS with debt systems and strengthening the Cash Management Committee can improve planning and enable safe short-term investments to optimize idle funds.
"""
