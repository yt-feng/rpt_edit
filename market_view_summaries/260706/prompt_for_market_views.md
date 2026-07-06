请基于下面每天新报告的摘要，写一份“Market Views / 国际信源汇编&评论”的结构化 JSON，用于生成 PDF。

目标读者：
关注每日更新的国际信源汇编&评论，希望快速看到国际主流叙事、数据、图表和边际变化。读者来自头部券商、PE/VC、投行、并购、hedge fund、资管机构、战略咨询、智库等。

要求：
1. 严格按来源拆成三个并列板块，不要混在一起：投行/券商（source_group=bank_research）、战略咨询（source_group=consulting）、智库/国际机构（source_group=institution）。
2. 三个板块篇幅要尽量接近。即使某一类报告更多，也要压缩成和另外两类相近的阅读体量；不要让世界银行/智库报告把 PDF 撑成长篇翻译。
3. 每个来源板块内部再按主题归纳 2-4 个 themes，例如宏观与利率、AI/算力、能源与大宗、地缘政治、企业战略、发展经济等。主题由内容决定，不要机械套模板。
4. 每个 theme 综合多篇报告，写 3-5 个 bullets；每条必须是可读完整句，保留关键数据、方向、分歧和边际变化，不要逐篇复述。
5. 每个 theme 必须给 references，引用报告 ID；三个来源板块合计 references 应覆盖全部或绝大多数报告。覆盖清单会展示这些 references，所以不要漏。
6. 可以使用所有 figure_ids，没有总数限制，但只选择真正支撑该板块观点且图表说明干净的图。
7. 投行名字必须脱敏：常见投行写 GS、JPM、MS、BofA、Citi、UBS、DB 等缩写，不确定就写“投行”。
8. 不要给投资建议，不要写买卖评级。
9. 不要输出“逐篇报告摘录”；正文只需要整合后的信号、评论、数据和图表。
10. source_roundups 必须按 source_group 输出三个对象，顺序为 bank_research、consulting、institution；如果某类当天没有报告，仍输出空 themes，并在 summary 写“今日暂无新增”。
11. 输出必须是 JSON 对象，不要 Markdown 代码块。

JSON 格式：
{"title":"市场最新观点汇总","subtitle":"一句话说明今天国际信源的共同主线","executive_summary":["全局要点1"],"source_roundups":[{"source_group":"bank_research","title":"投行/券商","summary":"本来源板块一句话摘要","themes":[{"heading":"主题标题","thesis":"核心判断","bullets":["要点1"],"figure_ids":["F001"],"references":["R001","R002"]}]},{"source_group":"consulting","title":"战略咨询","summary":"本来源板块一句话摘要","themes":[]},{"source_group":"institution","title":"智库/国际机构","summary":"本来源板块一句话摘要","themes":[]}],"closing":"简短收束"}

来源数量：
{
  "投行/券商": 0,
  "战略咨询": 0,
  "智库/国际机构": 36
}

报告摘要：
[
  {
    "id": "R001",
    "title": "亚洲开发银行：亚洲开发银行撬动60亿美元私人资本，2025年操作答卷解读",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "亚洲开发银行",
    "digest": "[wechat_article.md]\n# 亚洲开发银行：亚洲开发银行撬动60亿美元私人资本，2025年操作答卷解读\n\n2025年，亚洲开发银行（ADB）交出了一份总额293亿美元的操作答卷，其中联合融资贡献了147亿美元。但比这些数字更值得关注的，是这家多边开发银行正在发生的一系列制度性变化——这些变化正在重新定义它未来十年在亚太地区的发展角色。如果你仍然把亚行仅仅视为一个“基础设施贷款机构”，那么这份2025年成员概况报告可能会让你重新思考。\n\n报告的核心判断是：亚行正在从传统的“项目贷款银行”转向一个更灵活、更强调私人资本撬动、甚至敢于触碰核能等敏感领域的“发展解决方案平台”。这并非一次简单的业务调整，而是在全球地缘政治不确定性、发展中国家债务压力上升、以及气候融资需求爆发的多重背景下，亚行对自身生存和发展逻辑的一次深刻重构。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 修宪级变革：解除贷款限制，为未来十年扩张铺路\n\n2025年，亚行完成了一项看似技术性、实则影响深远的制度变革：修改了创始章程，移除了一项贷款限制条款。这项修改的核心意义在于，亚行可以在不要求股东进行普遍增资的情况下，扩大对发展中国家的支持规模。\n\n这意味着什么？在过去，多边开发银行的贷款能力受到其资本基数的严格约束。要扩大贷款规模，通常需要成员国同意增资，这是一个漫长且充满政治博弈的过程。而此次修宪，相当于为亚行“松绑”，使其能够更灵活地利用现有资本，去应对气候变化、疫后复苏等紧迫议题。\n\n> **KC评论：** 这可以理解为亚行给自己的资产负债表加了一个“杠杆”。它不要求成员国立刻多掏钱，但允许银行在风险可控的前提下，更高效地使用现有资本金。对于关注亚太基础设施和绿色转型的读者来说，这意味着未来几年亚行的项目审批速度和规模可能会超出市场预期。完整报告中对这一修宪的具体条款和风险控制机\n\n[... middle omitted ...]\n\nC评论和图表合集，便于喂给AI，也便于人工快速扫描市场动态。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n亚行2025年干了什么？一张表看懂\n\n亚行2025年操作全景\n\n全年承诺293亿美元，合融资147亿。机构改革、能源政策更新、结果导向贷款升级。\n\n1️⃣ 机构改革：修宪取消贷款上限，不增资也能扩大对发展中国家的支持。私营部门方案嵌入项目全周期，政策改革+可融资项目+撬动私人资本三管齐下。\n\n2️⃣ 能源政策更新：继续强推可再生能源，新增核能支持（需严格安全评估和全生命周期成本测算）。能源安全和普及两手抓。\n\n3️⃣ 结果导向贷款升级：可与其他融资工具（如投资贷款）组合使用，帮助政府强化制度、配套项目落地。\n\n4️⃣ 私营部门成增长引擎：2025年自有资金投了31亿美元（49笔交易），贸易和供应链金融项目24亿。直接撬动私人资本60亿，贸易项目另撬37亿。\n\n5️⃣ 采购数据：2025年货物/工程采购149亿美元，咨询服务7.59亿。累计采购超2923亿美元。\n\n文莱2006年加入亚行，截至2025年底认购资本5.12亿美元，贡献特别基金2231万。\n\n#学习笔记\n\n[source_mineru.md]\n## ASIAN DEVELOPMENT BANK MEMBER FACT SHEET\n\n![](imag\n\n[... middle omitted ...]\n\nSSALAM\n\nThe Asian Development Bank (ADB) works alongside governments, development partners, and other stakeholders to confront the complex challenges presented by persistent poverty, geopoliti\n\n[... middle omitted ...]\n\nian Development Blog https://blogs.adb.org/\n\nNotes: (i) Figures are estimated by ADB unless otherwise stated. \"\\$\" refers to United States dollars. (ii) Data are updated as of 31 December 2025 unless otherwise indicated."
  },
  {
    "id": "R002",
    "title": "亚洲开发银行：中国A股数据揭示，制造端数字化对环保拉动效果最显著",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "亚洲开发银行",
    "digest": "[wechat_article.md]\n# 亚洲开发银行：中国A股数据揭示，制造端数字化对环保拉动效果最显著\n\n企业数字化转型究竟能带来多少环境绩效的提升？当大多数讨论还停留在“数字化是否增加能耗”的争议时，一份来自亚洲开发银行的工作论文给出了一个值得产业决策者认真对待的量化结论：数字化转型每提升一个标准差，企业环境绩效改善1.34%。这个数字看似不大，但放在中国A股上市公司2009至2022年的长周期样本里，它意味着一个结构性的、可验证的因果关系正在形成。\n\n这份报告最值得关注的判断不是“数字化有利于环保”这个常识性结论，而是它对作用机制的拆解：在绿色创新、环境监测、信息透明度和外部关注这四个传导路径中，环境信息透明度被证明是最强的作用因子，其影响力甚至超过了绿色创新本身。这个发现挑战了业界长期以来“先创新、后治理”的惯性思维——在数字化语境下，透明本身就是一种治理能力。\n\n更关键的是，报告将数字化转型拆解为技术、业务、制造、运营四个维度，并发现制造端的数字化对环保的拉动效果最为显著，其次是运营和技术维度，而单纯改变商业模式（业务数字化）的效果反而最弱。这意味着：那些只在电商、营销、CRM层面做数字化的企业，可能错失了最核心的绿色红利；真正能带来环境绩效跃升的，是发生在工厂车间、供应链管理和生产流程里的数字化改造。\n\n> **KC评论：** 这份报告最实用的价值在于，它给出了一个可操作的优先级排序。如果你是企业管理者，资源有限的情况下，应该优先把数字化投入放在制造环节和运营环节，而不是先去做数字营销或线上渠道。完整报告里还包含了对四个维度各自贡献度的具体数据对比，以及一个“赛马分析”的计量框架，这些细节对制定数字化预算和KPI很有参考意义。继续看原文，真正有价值的是图表、假设和验证路径；完整报告与KC评论在每日汇编。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## \n\n[... middle omitted ...]\n\n管机构、战略咨询、智库等领域的专业人士，期待与大家深入交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n数字化转型，真的能让企业更环保吗？\n\n🌱数字转型×绿色成绩单\n\n一份来自亚洲开发银行的研究，用中国A股上市公司数据告诉你答案。\n\n最近读到一篇超扎实的研报，来自亚开行和复旦学者，研究的是 **“企业数字化转型 vs 环境表现”** 的关系。数据跨度2009-2022，样本覆盖中国A股上市公司，结论很清晰：\n\n**数字化转型做得好，环境表现确实更优。**\n\n具体逻辑拆开来，有4条关键路径👇\n\n1️⃣ **绿色创新**：数字技术（AI、大数据、工业互联网）让研发更高效，知识流动更快，企业更容易搞出绿色技术。\n\n2️⃣ **环境监控与沟通**：数字化让企业对环境数据的收集、监控、应急响应更及时，管理决策更有依据。\n\n3️⃣ **环境信息透明**：数字化披露让外部看得更清楚，倒逼企业不敢“装睡”，主动改善环境表现。\n\n4️⃣ **外部关注**：数字化让企业更容易被政府、媒体、投资者盯上，外部压力变成绿色动力。\n\n有意思的是，这四条路径里，**环境信息透明**的作用最强，其次是绿色创新和外部关注。\n\n再拆一个细节：数字化转型的四个维度——技术、业务、制造、运营——都对环境有正向影响，但**制造端数字化**的拉动力最大，\n\n[... middle omitted ...]\n\ne views and policies of ADB or its Board of Governors or the governments they represent.\n\nYan Luo (luoyan@fudan.edu.cn) is a professor and Shula Wu (shula\\_wu@163.com) is a PhD student at the \n\n[... middle omitted ...]\n\nes together, ADB harnesses innovative financial tools and strategic partnerships to transform lives, build quality infrastructure, and safeguard our planet. Founded in 1966, ADB is owned by 69 members—50 from the region."
  },
  {
    "id": "R003",
    "title": "亚洲开发银行：碳定价在交通领域真正机会，不是征税，而是循环投资",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "亚洲开发银行",
    "digest": "[wechat_article.md]\n# 亚洲开发银行：碳定价在交通领域真正机会，不是征税，而是循环投资\n\n交通领域是全球温室气体排放增长最快的板块之一。在亚洲开发银行覆盖的中亚区域经济合作（CAREC）11个成员国中，交通排放占各国总排放的比例从蒙古的5%到格鲁吉亚的23%不等，但一个更值得关注的信号是：所有CAREC国家的交通排放增速都明显快于整体排放增速。\n\n亚洲开发银行这份2026年发布的报告，核心判断并非“碳税最重要”，而是揭示了一个反直觉的杠杆效应——碳税收入如果用于投资减排项目，间接减排效果是直接效果的50到100倍。这意味着，一个极低的碳税（每升燃料征收0.01美元），如果设计为“气候分币基金”并回流到交通减排项目，就能实现各国自主贡献目标中交通领域减排量的75%。\n\n这不仅仅是政策设计问题。对于关注全球碳市场、交通电动化、以及新兴市场基础设施投资的读者而言，这份报告提供了一个可操作的观察框架：碳定价的真正价值，不在于惩罚排放，而在于创造可循环的财政工具，撬动那些原本缺乏商业可行性的低碳交通项目。\n\n> **KC评论：** 报告的核心洞察是“碳税收入再投资”的乘数效应。如果你关心的是碳信用项目的开发时机、各国家庭的减排潜力排序，或者哪些交通项目类型还能在碳市场注册，完整报告里的图表和分国家测算才是真正的干货。继续看原文，真正有价值的是图表、假设和验证路径；完整报告与KC评论在每日汇编。\n\n---\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 碳税的直接效果被高估，但间接效果被严重低估\n\n报告明确指出一个经济学常识：短期内，燃料需求的价格弹性极低。这意味着，即便大幅提高燃油税，消费者也不会立刻减少开车或改用公共交通。2024年，CAREC国家汽油的隐含碳税（即通过增值税、消费税等嵌入燃油价格的税收）从每吨二氧化碳4美元到145美元不等，柴油从4\n\n[... middle omitted ...]\n\ndge fund、资管机构、战略咨询、智库等朋友，期待交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n交通碳定价，一次说清逻辑\n\n交通碳定价怎么玩？\n\nCAREC国家如何用碳市场降交通排放\n\n最近翻到一份亚开行的CAREC区域交通碳定价报告，信息量很大。分享几个核心观察：\n\n1️⃣ 交通排放增速远超整体\nCAREC国家交通排放占总量5%-23%，但增速明显快于其他行业。电动化、低碳燃料、公交优化是目前主流方向。\n\n2️⃣ 碳税vs碳市场\n报告明确：短期燃油需求缺乏弹性，碳税直接减排效果有限。但如果把碳税收入投到减排项目，间接效果是直接效果的50-100倍。一个“气候分基金”（每升油收1分钱）就能覆盖大部分国家NDC目标。\n\n3️⃣ ETS怎么接入交通？\n三种方式：纳入大型运输企业、纳入运输燃料、或设车辆碳排放配额。加州模式是把燃料分销商纳入，特斯拉靠碳积分每年赚几十亿。\n\n4️⃣ 碳市场窗口在收窄\n电动出行碳项目有“临界点”——纯电新车占比超过2.5%或保有量超过一定比例后，就不再被视为“额外减排”。中国多数车型已过线，其他国家也在快速接近。\n\n5️⃣ 公交和铁路项目门槛高\n公交项目需要新基础设施，不能只换车；铁路项目缺少通用方法论。大项目才值得开发，小城市难做。\n\n6️⃣ 目前CAREC国家\n中国有地方ET\n\n[... middle omitted ...]\n\nck No. TCS260282-2\n\nDOI: http://dx.doi.org/10.22617/TCS260282-2\n\nThe views expressed in this publication are those of the authors and do not necessarily reflect the views and policies of the A\n\n[... middle omitted ...]\n\n](images/1bfb289f2d52162972ae821557793f2acd3b7ae20031603d1fc3ee7e8c1911b2.jpg)\n\nCAREC Secretariat\n\nwww.carecprogram.org\n\nASIAN DEVELOPMENT BANK\n\n6 ADB Avenue, Mandaluyong City\n\nwww.adb.org\n\n1550 Metro Manila, Philippines"
  },
  {
    "id": "R004",
    "title": "亚洲开发银行：去美元化不是选择题，而是基础设施竞赛",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "亚洲开发银行",
    "digest": "[wechat_article.md]\n# 亚洲开发银行：去美元化不是选择题，而是基础设施竞赛\n\n全球货币体系正在经历一场静水流深的底层重组。自2010年代末以来，地缘政治紧张——尤其是中美之间的结构性博弈——已经开始实质性地影响亚洲贸易和投资中的货币选择。美元依然是主导性国际货币，但一个不容忽视的趋势正在加速：新兴经济体正越来越多地推动本币计价交易。\n\n亚洲开发银行研究所（ADBI）在2026年7月发布的第1540号工作论文，提供了一个难得的系统性视角。这份报告没有停留在“去美元化”的口号层面，而是深入拆解了中国人民币、泰铢、印尼盾、马来西亚林吉特等亚洲货币在本币结算中的真实进展、结构性瓶颈和政策边界。\n\n核心判断是：去美元化的可持续扩张，不取决于政治意愿，而取决于外汇市场的深度、双边和多边政策框架的可信度，以及资本账户开放的节奏。那些在放松管制上走得最快的经济体——如泰国——正在收获实实在在的结算份额增长；而那些试图通过管制来推动本币使用的经济体，反而陷入了停滞。\n\n这不仅是央行官员和交易员需要理解的变化。对于任何在亚洲供应链中配置资产、管理外汇风险、或评估区域贸易格局的决策者而言，理解本币结算的真实边界，是判断未来五年贸易金融成本和区域货币格局的前提。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 本币结算的真实进展比媒体报道温和得多，但结构性拐点已经出现\n\n报告最值得关注的一点，是它对“去美元化”进展的诚实评估。SWIFT数据显示，人民币在国际支付中的占比仅为2.74%，很难将其视为真正的国际结算货币。但报告同时指出，SWIFT统计存在天然盲区——它无法捕捉通过人民币跨境支付系统（CIPS）完成的交易。\n\nCIPS是中国央行主导建立的替代性金融基础设施。报告虽然没有给出CIPS的精确交易量，但明确指出，人民币的使用路径已经呈现出清晰的阶段性：从最初的人\n\n[... middle omitted ...]\n\n金、对冲基金、资管机构、战略咨询和智库的朋友，期待与你交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n亚洲货币的“去美元化”到底走到哪了？\n\n🌏 去美元化，真实进度如何？\n\n最近某外资投行发布了一篇关于亚洲本地货币交易的长篇研究，核心观点很直接：**美元还是老大，但“去美元化”确实在悄悄推进**，尤其是在亚洲。\n\n这篇笔记帮你拆解几个关键发现👇\n\n1️⃣ **人民币国际化：数据之外有另一条路**\n- 在SWIFT系统里，人民币国际支付份额只有2.74%（截至2026年2月），看起来很小。\n- 但注意，SWIFT只统计通过它的交易。中国自己建的CIPS系统（人民币跨境支付系统）正在绕开SWIFT，这才是人民币国际化的“暗线”。\n- 另外，人民币的使用路径很清晰：先从进口端开始（付人民币买货），再到出口端（收人民币），最后扩展到资本交易（直接投资、证券）。\n- 地理上也不再只限于香港，东南亚、欧洲的贸易伙伴也开始用人民币结算。\n\n2️⃣ **泰国是个“模范生”，马来西亚和印尼却卡住了**\n- 泰国、马来西亚、印尼都签了“本地货币结算框架”，但结果差异很大。\n- 泰铢的本地结算份额明显上升，因为泰国放松了外汇管制。\n- 马来西亚和印尼反而在2010年代后期收紧了非居民持有本币和外币兑换的规定，导致本地货币交易增长停\n\n[... middle omitted ...]\n\nthe views or policies of ADBI, ADB, its Board of Directors, or the governments they represent. ADBI does not guarantee the accuracy of the data included in this paper and accepts no responsibi\n\n[... middle omitted ...]\n\npan=\"2\">Australia</td><td>Exports</td><td>30%</td><td>40%</td><td>38%</td><td>29%</td><td>36%</td><td>35%</td></tr><tr><td>Imports</td><td>18%</td><td>29%</td><td>28%</td><td>27%</td><td>25%</td><td>26%</td></tr></table>"
  },
  {
    "id": "R005",
    "title": "亚洲开发银行：不是卫星数量，而是数据应用，亚洲发展的新测量逻辑",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "亚洲开发银行",
    "digest": "[wechat_article.md]\n# 亚洲开发银行：不是卫星数量，而是数据应用，亚洲发展的新测量逻辑\n\n一份来自亚洲开发银行（ADB）的详细技术报告，其核心判断并非关于某项技术突破，而是关于一个正在发生的结构性转变：**卫星地球观测（EO）正从科研工具演变为亚洲发展中国家基础设施投资、气候行动和项目评估的“基线数据基础设施”**。这份报告的价值在于，它系统性地展示了EO如何从“可选的补充信息”变成“决策链条中不可替代的一环”。\n\n这并非一篇关于太空竞赛的报道。它讨论的是，当多边开发银行和各国政府开始将卫星数据嵌入项目全生命周期——从规划、监测到灾后评估——时，整个发展项目的效率、透明度和可问责性将发生怎样的变化。对于关注亚洲基础设施、气候风险、农业和城市化的决策者而言，这份报告提供了一个理解“数据如何重塑发展金融”的观测框架。\n\n报告指出，亚洲和太平洋地区预计将成为未来十年全球EO领域增长最快的区域。这背后是多重动力的汇合：更低的卫星发射成本、AI分析能力的成熟、以及发展中国家日益增长的环境监测需求。但真正值得关注的，不是卫星的数量，而是这些数据如何被转化为可操作的决策信息。\n\n> **KC评论：** 如果你只关心卫星技术本身，可能会错过报告的核心主张。ADB的视角是“应用驱动的投资回报”。它关心的不是卫星能拍多清楚，而是这些图像能否帮助一个道路项目避开未来20年的洪水风险，或者能否以更低的成本完成一个国家的森林碳汇核算。这才是发展金融机构和主权政府真正买单的理由。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 市场增长的核心驱动力不是技术，是“可验证的需求”\n\n报告给出了清晰的市场数据：EO数据市场在2022年达到17.8亿美元，年复合增长率约6%；而下游的EO服务和数据分析市场已达28.6亿美元，年增长率达9%。预计到2032年，两个市场的总和将超过\n\n[... middle omitted ...]\n\n购、对冲基金、资管机构、战略咨询和智库的朋友，期待与你交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n卫星遥感，不只是看地图\n\n🌍 卫星视角下的发展密码\n\n上个月翻到一份亚开行的技术报告，讲卫星地球观测（EO）如何用在发展项目里。信息量很大，挑几个有意思的点分享。\n\n1️⃣ 市场在悄悄长大\nEO数据市场2022年17.8亿美元，年增6%。服务和分析市场规模28.6亿，年增9%。预计到2032年，两个市场加起来能到76亿。亚太地区增速最快。\n\n2️⃣ 不光是大国游戏\n以前EO是政府和大机构的专属，现在“新太空”运动来了。小卫星、低成本、高频率重访，让更多玩家能进场。很多公司开始提供“即服务”模式，数据成本在快速下降。\n\n3️⃣ 六个应用场景\n报告详细拆了6个方向：地表覆盖制图、灾害风险管理、气候韧性、海岸带管理、森林监测、温室气体监测。每个都有真实案例。\n\n4️⃣ AI+云计算是加速器\nEO数据量太大，传统方法处理不了。高性能云计算和AI分析正在解决复杂的环境监测问题。数据立方体、数字孪生这些新工具是关键。\n\n5️⃣ 对发展项目的真实价值\nEO能提供全球一致、可重复、及时的环境信息。在灾害评估（比如2022年巴基斯坦洪水）、城市规划（马尼拉非正式定居点分布）、森林退化监测等场景，已经证明了自己的价值。\n\n6️⃣\n\n[... middle omitted ...]\n\nI: http://dx.doi.org/10.22617/TCS260092-2\n\nThe views expressed in this publication are those of the authors and do not necessarily reflect the views and policies of the Asian Development Bank \n\n[... middle omitted ...]\n\nes together, ADB harnesses innovative financial tools and strategic partnerships to transform lives, build quality infrastructure, and safeguard our planet. Founded in 1966, ADB is owned by 69 members—50 from the region."
  },
  {
    "id": "R006",
    "title": "亚洲开发银行：高温导致2.4万亿美元生产力损失，亚洲开发银行警告东南亚风险",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "亚洲开发银行",
    "digest": "[wechat_article.md]\n# 亚洲开发银行：高温导致2.4万亿美元生产力损失，亚洲开发银行警告东南亚风险\n\n2024年成为有记录以来最热的一年，全球平均气温较1850-1900年基准高出1.45至1.60摄氏度。这个数字本身已经足够惊人，但真正值得关注的不是温度本身，而是温度背后正在发生的变化：极端高温不再是一个季节性的不适，它正在变成一场持续、全面、且影响深远的危机。\n\n亚洲开发银行最新发布的这份报告，核心判断可以用一句话概括：极端高温正在从“气候问题”演变为“治理问题”，而东南亚——尤其是泰国——正处在这场转变的前沿。报告指出，到2048年，极端高温可能导致泰国GDP损失高达45%。这个数字的冲击力在于，它不是在讨论一个遥远的气候情景，而是在描述一个已经启动的经济结构性调整。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 高温的经济代价已经大到保险公司不再称之为“隐形风险”\n\n报告中最值得注意的一个信号是：保险行业已经不再将极端高温视为“隐形风险”，而是开始系统性地评估其投资风险和连锁成本。这意味着高温的影响已经从物理层面穿透到了金融定价层面。\n\n2025年，极端高温预计将造成2.4万亿美元的生产力损失，以及上市公司4480亿美元的固定资产损失。这两个数字放在一起看，传递的信息非常明确：高温正在同时侵蚀两个最核心的经济变量——人的产出能力和资本的价值。\n\n对于东南亚而言，问题更加严峻。该地区高度依赖户外劳动密集型产业（农业、建筑业、旅游业），同时又面临大规模的非正规就业。报告指出，对于依赖非正规劳动力的经济体，生产力损失可能变成结构性嵌入——也就是说，即使经济总量在增长，人均产出效率也可能因为高温持续下降。\n\n> **KC评论：** 这份报告最有价值的洞察之一，是把高温的影响从“人道主义关切”拉到了“资产负债表”层面。当保险行业开始重新定价，\n\n[... middle omitted ...]\n\n fund、资管机构、战略咨询、智库等朋友，期待与各位交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n热浪正在重塑东南亚的经济版图\n\n热不是暂时的，是长期的\n\n泰国GDP或损失45%，不是危言耸听\n\n---\n\n如果你以为极端高温只是“今年特别热”，那这篇研报会刷新你的认知。\n\n亚洲开发银行刚出了一份泰国和东南亚高温专题报告，信息量很大，我用3个点帮你拆解。\n\n1️⃣ 热浪正在变成系统性危机\n- 2024年是史上最热年份，2028年全球气温或比工业化前高1.9°C\n- 极端高温已不再是季节性不适，而是威胁生命、经济、生态的持续危机\n- 全球因热应激导致的劳动生产力损失，预计2025年达2.4万亿美元\n\n2️⃣ 泰国是重灾区中的重灾区\n- 到2048年，泰国GDP可能损失高达45%\n- 农业、渔业、旅游业——经济支柱全在高温和沿海侵蚀的夹击中\n- 曼谷等大城市可能突破人类生存的临界温度阈值\n\n3️⃣ 解决方案其实有章可循\n- 研报给出了一套完整的国家热行动计划框架\n- 核心思路：跨部门协作 + 创新融资 + 保护最脆弱群体\n- 具体措施包括：城市绿化、冷屋顶、工作休息周期调整、社区冷却中心\n\n最让我触动的一句话：\n“降温不是奢侈品，而是与水电同等重要的基础设施。”\n\n你觉得国内哪些城市最需要这样的热行动计划？欢迎\n\n[... middle omitted ...]\n\nublication are those of the authors and do not necessarily reflect the views and policies of the Asian Development Bank (ADB) or its Board of Governors or the governments they represent.\n\nADB \n\n[... middle omitted ...]\n\n](images/e11a31a4ee4905289ea06582ae7e5b3402b800e29b729a9403d515e6f9a87a8f.jpg)\n\nKOREA e-Asia Fund\n\nOPEC FUND for International Development\n\n![](images/f577441a507763a5628f34e0c10caf6278bc66b0f529fef772af060c2ecf43ac.jpg)"
  },
  {
    "id": "R007",
    "title": "布鲁盖尔研究所：数字市场法案要求谷歌开放系统，第三方AI服务迎来转机",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "布鲁盖尔研究所",
    "digest": "[wechat_article.md]\n# 布鲁盖尔研究所：数字市场法案要求谷歌开放系统，第三方AI服务迎来转机\n\n欧洲AI竞争格局正站在一个关键转折点上。2026年4月，欧盟委员会发布了针对Google Android系统的《数字市场法案》第6条第7款的首份规范草案，要求Google向第三方AI服务提供商开放操作系统核心接入点。这不仅仅是一次监管行动，更是一个信号：欧盟正在用一套事前干预机制，试图避免AI服务市场重蹈搜索市场被一家企业垄断的覆辙。布鲁盖尔研究所（Bruegel）高级研究员Fiona Scott Morton在这份研报中系统论证了为什么这项规范是“正确的工具、正确的时机”，以及为什么它可能比美国耗时十年的反垄断诉讼更有效。\n\n> **KC评论：** 这篇报告的核心判断值得所有关注AI产业竞争格局的人仔细读一遍——欧盟正在做的不是“监管AI”，而是用互操作性条款维护AI服务市场的可竞争性。报告里最关键的图表是第3节对四个接入点的拆解图，以及第4节对Google搜索垄断历史的对比分析。这些图表和假设路径在完整报告中才能看到全貌。\n\n继续看原文，真正有价值的是图表、假设和验证路径；完整报告与KC评论在每日汇编。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 这轮AI竞争的关键瓶颈不在技术，而在手机操作系统对第三方AI服务的接入控制\n\n报告指出，AI助手要真正有用，必须依赖四个核心功能：调用（invocation）、上下文（context）、动作（actions）和资源访问（resources）。所有这四个功能都需要通过设备的操作系统实现。以Google Android为例，长按Home键调用搜索功能、始终在线的热词检测“Hey Google”、AppSearch集中式设备数据API、App Actions和App Functions等结构化集成通道、\n\n[... middle omitted ...]\n\n购、对冲基金、资管机构、战略咨询、智库等朋友，期待与你交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI竞争的关键一步：安卓开放AI接口\n\n开放AI接口\n\n欧盟如何防止AI市场一家独大\n\n最近读到一篇很有启发的研报，讲的是欧盟《数字市场法案》如何用第6(7)条，阻止AI市场被单一巨头垄断。\n\n核心逻辑很简单：谁控制了手机操作系统，谁就能决定AI助手能不能好好用。\n\n1/ 手机就是AI的“入场券”\n用户只用一台手机，AI助手必须装在这台设备上才能服务你。如果操作系统只给自己的AI开放全部功能，第三方AI永远体验差一截。\n\n2/ 谷歌安卓把住了4个关键入口\n- **唤醒**：长按Home键、语音唤醒“Hey Google”的硬件通道，目前只有Gemini能用\n- **上下文**：读取你的日历、地图、邮件数据，只给“默认助手”权限\n- **操作**：帮你订餐厅、发消息的系统级接口，也仅限自家AI\n- **算力**：手机上的AI芯片和基础模型，同样只服务内部\n\n3/ 欧盟的解法很直接\n要求谷歌把这些入口，以同等条件开放给所有合规的第三方AI服务。不是要求改产品设计，而是确保竞争机会平等。\n\n4/ 一个意想不到的效果\n研报指出，这项规定可能让欧洲成为AI创新的热土。因为创业者知道，在这里做AI，用户触达不会被平台卡住\n\n[... middle omitted ...]\n\nequivalent to those Google's own services receive. If the specification is finalised and enforced as drafted, it will prevent monopolisation of AI services and shortcut the need for a long and\n\n[... middle omitted ...]\n\niews expressed are the researchers' own.\n\n![](images/f6a05ec295bf4038993e462d7f43befd44fdbcc223b7c9ae7a42e53d2cb645f9.jpg)\n\nBruegel, Rue de la Charité 33, B-1210 Brussels (+32) 2 227 4210\ninfo@bruegel.org\nwww.bruegel.org"
  },
  {
    "id": "R008",
    "title": "布鲁盖尔研究所：五角大楼用十年验证，硅谷创新如何真正融入国防",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "布鲁盖尔研究所",
    "digest": "[wechat_article.md]\n# 布鲁盖尔研究所：五角大楼用十年验证，硅谷创新如何真正融入国防\n\n美国国防部在2015年成立了一个名为“国防创新单元”（Defense Innovation Unit,DIU）的机构，旨在打破传统军工巨头的垄断，让硅谷的商业科技公司也能参与国防采购。十年后，布鲁盖尔研究所（Bruegel）发布了一份实证评估报告，首次用因果识别方法验证了这一改革的效果。结论清晰：DIU不仅显著提高了商业科技公司获得国防合同的可能性，还大幅增加了合同金额。这一发现对正在效仿美国模式推进国防创新改革的欧洲、印度和加拿大等国，具有直接的决策参考意义。\n\n这份报告的核心判断是：通过降低信息不对称和交易成本，专门的国防创新机构可以系统性地扩Daiwa深化国防供应商基础。这不是一个“锦上添花”的增量改革，而是对传统国防采购“锁定效应”的结构性突破。\n\n> **KC评论：** 传统国防采购的逻辑是“大而全”——只有那些能承受漫长合规流程、熟悉官僚体系、拥有政府关系的大型承包商才能生存。DIU的逻辑是“快而专”——它用商业解决方案开放（CSO）机制，让企业主动提出技术方案，而不是被动响应军方写好的技术规格。这看似只是流程变化，实则是对国防创新生态的根本重构。\n\n继续看原文，真正有价值的是布鲁盖尔研究所如何构建反事实对照组、如何剥离其他政策干扰（如SBIR改革），以及那些图表背后的二阶影响——比如DIU对合同金额的拉动效应是否集中在少数明星公司身上，还是广泛分布于整个供应商网络。完整报告与KC评论在每日汇编。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. DIU的机制设计精准回应了“为什么硅谷不愿为五角大楼打工”\n\n传统国防采购的最大问题不是技术缺口，而是制度摩擦。联邦采购条例（FAR）设计的初衷是确保大规模采购的合规性和公平性，但这对于小型商业科技公司而言，\n\n[... middle omitted ...]\n\ne fund、资管机构、战略咨询、智库等朋友，期待与你交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美军采购改革，到底有没有用？\n\n**国防采购新打法**\n\n**DIU真的能让科技公司进五角大楼吗？**\n\n最近读了一篇某外资投行的研报，用数据拆解了美国国防创新单元（DIU）的实战效果。结论明确：**DIU真的管用。**\n\n1️⃣ **DIU是干嘛的？**\n五角大楼的传统采购流程又长又复杂，小科技公司根本玩不转。2015年成立的DIU，专门充当“翻译官”和“桥梁”——帮硅谷公司理解军方需求，同时帮军方降低找新供应商的成本。核心动作是发布“商业解决方案公开征询”，让公司提方案，选中的做原型，进目录，然后军方直接采购。\n\n2️⃣ **效果如何？有数据支撑**\n- 研究用了2017-2025年美军采购数据，对比了进入DIU目录的公司和没进的同类公司。\n- **签约概率显著提升**：进入DIU目录后，拿到五角大楼合同的概率明显增加。\n- **合同金额也变大**：不仅更容易中标，订单规模也更大。\n- 结论：DIU确实拓宽了国防供应商基础，让更多创新公司进了“圈子”。\n\n3️⃣ **为什么能行？**\n核心解决了两个老问题：\n- **信息不对称**：军方不知道有什么新技术可用，公司不知道军方具体要什么。\n- **交易成本高\n\n[... middle omitted ...]\n\nccessful has this new unit been in achieving its mission? We provide the first causal evaluation of the DIU's effects on defence procurement. Using administrative procurement data and a firm-l\n\n[... middle omitted ...]\n\niews expressed are the researchers' own.\n\n![](images/08afdfb80e8004990cd9577446a13f548ea6b0755e8eba7b45f91ac7ecf26596.jpg)\n\nBruegel, Rue de la Charité 33, B-1210 Brussels (+32) 2 227 4210\ninfo@bruegel.org\nwww.bruegel.org"
  },
  {
    "id": "R009",
    "title": "布鲁盖尔研究所：欧盟银行业政策碎片化才是真正挑战，而非美国监管竞争",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "布鲁盖尔研究所",
    "digest": "[wechat_article.md]\n# 布鲁盖尔研究所：欧盟银行业政策碎片化才是真正挑战，而非美国监管竞争\n\n全球银行业监管正在经历一场静默的分岔。当美国在第二任特朗普政府治下加速放松金融监管、削减大型银行资本要求时，欧盟正站在一个关键的十字路口：是追随美国走“低路”，以放松管制换取短期竞争力，还是坚持“高路”，维持巴塞尔框架的纪律并完成银行业联盟的未竟改革？\n\n布鲁盖尔研究所（Bruegel）近期发布的一份深度报告，系统梳理了这一跨大西洋的监管博弈。报告的核心判断是：美国当前的政策转向并非源于对欧盟的竞争压力，而是一种增加系统性风险的“低路”选择。历史反复证明，低路终将通向危机。对于欧盟而言，真正的挑战不在于与美国比谁更松，而在于解决自身银行业政策碎片化的根本顽疾。\n\n这份报告的价值在于，它不仅用详实的数据对比了美欧大型银行的资本要求，更从历史和政治经济学的视角，揭示了监管放松背后的逻辑与风险。对于关注全球金融格局、跨境资本流动以及系统性风险的读者而言，这是一份不可多得的分析框架。\n\n> **KC评论：** 这份报告最值得关注的点在于，它明确指出美国当前的放松并非“竞争性放松”，而是一种缺乏远见的短期行为。对于投资者而言，这意味着需要重新评估欧美大型银行的系统性风险溢价，而非简单认为美国银行因此更具投资价值。报告中对美欧资本要求的具体拆解和图表，是理解这一判断的关键。\n\n继续看原文，真正有价值的是报告中对“资本堆叠”（capital stack）的逐层拆解、美欧监管框架差异的图表对比，以及作者对巴塞尔框架未来走向的推演。这些细节和图表，以及KC评论的进一步解读，在每日汇编中都有完整呈现。\n\n---\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 美国监管转向的本质：不是竞争，是“低路”冒险\n\n报告用大量篇幅论证了一个反直觉的结论：美国当前的政策调整，并非为\n\n[... middle omitted ...]\n\n待与您交流。更多国际信源汇编与评论，欢迎扫码交流，每日更新。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n欧洲大行资本新规，看懂这一篇就够了\n\n欧洲大行 vs 美国大行，谁更安全？\n\n从2024年底到2025年底的跨大西洋银行资本要求对比\n\n---\n\n最近某外资投行出了一份重磅研报，把欧盟和美国超级大行的资本要求从头到尾扒了一遍。\n\n1/ 什么叫“超级大行”？全球系统重要性银行（G-SIB）里资产过万亿的才算。欧盟目前7家：BNPP、法农、桑坦德、BPCE、SG、DB、ING。美国6家：JPM、BofA、Citi、富国、GS、MS。\n\n2/ 2024年底的数据显示，美国对大行的资本要求普遍比欧盟更严格，也高于巴塞尔框架的最低标准。这是美国长期以来的做法。\n\n3/ 但到了2025年底，特朗普第二任期的政策让这个差距大幅缩小。不是欧盟加码了，是美国在降。\n\n4/ 不过研报判断：美国目前并没有“低于”欧盟要求，还没构成对欧盟大行的致命竞争压力。\n\n5/ 真正值得警惕的是美国正在走“低路”——放松监管+弱化监督。短期看似提升竞争力，长期只会增加系统性风险。\n\n6/ 历史一再证明：低路通向灾难。欧盟应该坚持“高路”——维持与巴塞尔框架一致的资本要求，同时解决内部碎片化问题。\n\n7/ 欧元区的微观审慎监管（SSM）已经做得很成功\n\n[... middle omitted ...]\n\negabanks were generally stricter than requirements on EU megabanks and the minimum levels under the Basel Framework, in line with longstanding US practice.\n\nWe also find a marked change by end\n\n[... middle omitted ...]\n\niews expressed are the researchers' own.\n\n![](images/68bd75d7161565dc6debc7c8b5e5e83a217d8ec767f3203e0494289e3265c2d8.jpg)\n\nBruegel, Rue de la Charité 33, B-1210 Brussels (+32) 2 227 4210\ninfo@bruegel.org\nwww.bruegel.org"
  },
  {
    "id": "R010",
    "title": "布鲁盖尔研究所：不是规则太少，而是规则太复杂，欧盟绿色金融的结构性矛盾",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "布鲁盖尔研究所",
    "digest": "[wechat_article.md]\n# 布鲁盖尔研究所：不是规则太少，而是规则太复杂，欧盟绿色金融的结构性矛盾\n\n欧盟在绿色金融领域的雄心壮志，正在被自身复杂的规则体系所拖累。这份来自布鲁盖尔研究所的最新研报，揭示了一个正在发生的结构性矛盾：欧盟试图通过信息披露来引导资本流向绿色项目，但其规则设计的过度复杂化，不仅未能有效撬动市场，反而可能成为资本流动的障碍。报告的核心判断是，欧盟必须将可持续金融政策与资本市场发展真正融合，否则绿色转型的融资缺口将难以弥合。\n\n这不仅仅是一份关于监管的讨论。它触及了欧洲当前最核心的竞争力和增长命题。欧洲央行行长拉加德在2021年就曾指出，绿色转型是构建真正欧洲资本市场的历史性机遇。然而，五年过去了，欧盟的可持续金融规则与资本市场政策仍处于“各自为政”的状态。这种割裂，使得欧洲在需要大规模动员资本的时代，反而制造了额外的摩擦成本。\n\n报告指出，欧盟的可持续金融框架根植于2020年的《欧洲绿色协议》，其核心目标是2050年实现气候中性。这本身没有问题。问题在于，政策制定者将“偏好”直接嵌入到了信息披露过程中，期望通过强制要求企业披露更多信息，来迫使资本做出“正确”的选择。这种“自上而下”的监管思路，与资本市场“自下而上”的定价逻辑之间存在根本性冲突。\n\n**KC评论：** 这份报告最犀利的地方在于，它直接点出了欧盟可持续金融政策的“致命伤”——用信息披露替代了市场激励。企业花费大量资源编制报告，但84%的受访者认为这些披露对投资者“没有显著用处”，83%的人认为披露被用作营销工具而非决策依据。这提醒我们，在评估任何绿色金融政策时，不能只看“有没有规则”，更要看规则是否真正改变了资金流向。\n\n继续看原文，真正有价值的是报告对欧盟“双重重要性”（double materiality）原则的剖析，以及它与全球主流标准（ISSB）之间的结构性差异。完整报告与KC评论在每日\n\n[... middle omitted ...]\n\n购、对冲基金、资管机构、战略咨询、智库等业界朋友，期待交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n欧盟的绿色金融，卡在哪儿了？\n\n绿色金融 vs 金融绿色\n\n欧盟的绿色金融框架，有点“两张皮”\n\n投行研报指出，欧盟的绿色金融政策和资本市场建设一直是两条平行线，没有真正融合。绿色项目需要钱，但光靠信息披露和标签，很难拉动资本流入。\n\n1/ 信息披露多，但实际用处有限\n- 欧盟要求企业披露大量可持续信息，但调查显示，84%的受访者认为这些披露对投资者“不太有用”\n- 企业花大量精力做合规报告，但数据可能没人看，反而成了负担\n- 如果披露变成“为了披露而披露”，就偏离了推动绿色转型的初衷\n\n2/ 欧盟标准和全球标准“打架”\n- 欧盟采用“双重重要性”原则，要求企业同时评估自身对气候的影响和气候对自身的影响\n- 而全球主流标准（如ISSB）只关注“财务重要性”——气候如何影响公司\n- 两者不互通，企业若想同时满足，得看两套规则，成本翻倍\n\n3/ 资本市场没跟上绿色金融的节奏\n- 欧盟的资本市场联盟进展缓慢，碎片化严重，制约了绿色项目的融资效率\n- 绿色债券市场虽在增长，但EU taxonomy认证的债券占比不到10%\n- 股权、风投等资产类别在绿色金融中参与度低，绿色金融仍偏“债”\n\n4/ 未来方向：简化+\n\n[... middle omitted ...]\n\nntials. Connecting market and green-finance policies would help.\n\nAT THEIR BEST, sustainable finance disclosures are used by companies for self-assessment, peer comparison and aligning busines\n\n[... middle omitted ...]\n\ngel.org. Publication of altered content (for example, translated content) is allowed only with Bruegel's explicit written approval. Bruegel takes no institutional standpoint. All views expressed are the researchers' own."
  },
  {
    "id": "R011",
    "title": "布鲁盖尔研究所：世界银行数据之外，欧盟候选国法治改革才是入盟关键",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "布鲁盖尔研究所",
    "digest": "[wechat_article.md]\n# 布鲁盖尔研究所：世界银行数据之外，欧盟候选国法治改革才是入盟关键\n\n欧盟东扩进程正处于一个微妙时刻。地缘政治冲击——俄罗斯全面入侵乌克兰、美国战略重心转向印太、中国在全球南方影响力上升——本应成为加速扩员的催化剂。然而，布鲁盖尔研究所一份最新的工作论文通过量化欧盟委员会年度评估报告，揭示了一个令人警醒的现实：候选国在采纳欧盟法律体系方面的进展参差不齐，且改革进度与谈判进程之间出现了系统性脱节。这份报告的核心判断是：**政治因素正在系统性地扭曲基于功绩的扩员原则，而解决这一问题的钥匙不在于候选国，而在于欧盟自身决策机制的改革。**\n\n这份报告的价值不仅在于它提供了一套可量化的评估框架，更在于它揭示了“谈判政治化”这一制度性障碍。对于关注欧洲地缘经济格局变迁的读者而言，理解这些候选国的真实改革进度，是判断欧盟未来边界、内部市场扩大以及地缘政治影响力延伸的关键前提。报告覆盖了西巴尔干五国（阿尔巴尼亚、波黑、黑山、北马其顿、塞尔维亚）以及东欧三国（格鲁吉亚、摩尔多瓦、乌克兰），时间跨度从2020年至2025年。\n\n> **KC评论：** 这份报告最值得关注的不是单个国家的分数，而是它建立了一套“改革难度权重”体系。它将欧盟谈判的35个章节按实施难度分为1-4级，其中第23章（司法与基本权利）和第24章（司法、自由与安全）权重最高，达到4。这意味着，即便一个国家在低权重章节上得分很高，如果在核心法治领域进展缓慢，其整体“入盟准备度”仍然存疑。这对于理解欧盟扩员谈判的真实瓶颈至关重要——不是农业补贴或关税同盟，而是法治与司法独立。完整报告中的权重表格和评分方法值得仔细研读，它直接决定了我们如何解读每个国家的分数。继续看原文，真正有价值的是图表、假设和验证路径；完整报告与KC评论在每日汇编。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n##\n\n[... middle omitted ...]\n\nC评论和图表合集，便于喂给AI，也便于人工快速扫描市场动态。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n欧盟候选国改革进度大拆解\n\n谁最接近入盟？\n\n欧盟扩张是政治驱动+实绩考核的双轨制。候选国要啃下35个谈判章节（分6大集群），从司法独立到农业政策全面对齐欧盟标准。\n\n1/ 黑山领跑，有望2026-2027年完成谈判。2024-2025年改革明显提速，尤其在最难啃的“司法与基本权利”和“公正自由安全”章节拿到“良好”评级。\n\n2/ 塞尔维亚和北马其顿虽然总分不低，但改革停滞。特别是北马其顿，改革分数不错却因政治原因谈判卡壳——欧盟现有成员国的一票否决权和双边争端经常压倒实绩评估。\n\n3/ 波黑和格鲁吉亚分数垫底且停滞。格鲁吉亚2024年因民主倒退被冻结入盟进程。\n\n4/ 乌克兰、摩尔多瓦2023年才获候选国地位，基础弱但改革动力强。不过乌克兰战时状态让全面对齐欧盟法律变得极其困难。\n\n有意思的是，研究团队给33个章节按改革难度打权重分（1-4分），最难的“司法与基本权利”和“公正自由安全”权重最高。加权后，黑山还是第一，但塞尔维亚和北马其顿的差距更明显了。\n\n入盟这事儿，改革进度≠谈判进度。政治意愿才是真正的加速器。\n\n#学习笔记\n\n[source_mineru.md]\n# Progress made by \n\n[... middle omitted ...]\n\nndidate countries on accession-related reforms using a novel method involving the quantification of the European Commission's annual qualitative assessment of countries' preparedness. The resu\n\n[... middle omitted ...]\n\niews expressed are the researchers' own.\n\n![](images/d0347b2678ccd8c1053b0ba5acc67060052fed9e90d1cd03e198e6bcab127b9c.jpg)\n\nBruegel, Rue de la Charité 33, B-1210 Brussels (+32) 2 227 4210\ninfo@bruegel.org\nwww.bruegel.org"
  },
  {
    "id": "R012",
    "title": "布鲁盖尔研究所：中国光伏行业利润率转负，布鲁盖尔研究所警告产能过剩是结构性的",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "布鲁盖尔研究所",
    "digest": "[wechat_article.md]\n# 布鲁盖尔研究所：中国光伏行业利润率转负，布鲁盖尔研究所警告产能过剩是结构性的\n\n中国在太阳能板、风机等可再生能源制造领域已占据全球主导地位，但这种成功付出了产能严重过剩的代价——全行业利润率正在被压缩至负值。市场普遍期待国家电网40%的资本支出扩张计划能成为解药。但布鲁盖尔研究所在最新发布的研报中给出了一个反直觉的判断：电网投资是必要但不充分的方案。即便在最乐观的基础设施投资假设下，太阳能制造产能利用率在2031-2035年间仍将降至29%-35%，远低于财务可持续的阈值。中国绿能制造业的产能过剩是结构性的，而非周期性的。\n\n这份报告的核心价值在于，它没有停留在“产能过剩”这个已经被广泛讨论的结论上，而是用量化情景分析回答了“如果加大电网投资，到底能吸收多少过剩产能”。结果并不乐观。对于关注中国新能源产业链、全球能源转型投资逻辑以及中美欧贸易博弈的读者来说，这份报告提供了一个关键的分析框架：区分“需求侧缓解”和“供给侧出清”是两个完全不同的命题。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 中国的绿能制造业已经进入“内卷”式亏损，财务指标恶化速度超预期\n\n报告用一组数据清晰地展示了问题的严重性。2020年至2024年间，中国太阳能制造总产能扩张了6至7倍，达到全球年安装需求的两倍。与此同时，2023年至2025年间，中国太阳能组件出口额下降超过40%，但出口量却上升约60%——这意味着出口价格被砍掉了约三分之二。\n\n价格战迅速从出口市场蔓延至国内市场，演变为中国语境下的“内卷”。财务后果是残酷的：中国太阳能制造商的行业平均净资产收益率从2022年的约25%骤降至2024年的-5%，意味着全行业陷入亏损。EBITDA对利息支出的覆盖倍数从约34倍恶化至8倍，债务偿付能力正在快速削弱。\n\n> **KC评论：** 8倍的\n\n[... middle omitted ...]\n\n、并购、对冲基金、资管机构、战略咨询、智库等朋友，期待交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n电网扩容能救光伏过剩吗？🧐\n\n电网投资，产能解药？\n\n别只盯着制造端，消纳才是关键\n\n---\n\n最近读到某外资投行一篇有意思的研报，讲中国清洁能源的产能过剩问题。核心观点很清晰：**光靠电网投资，救不了光伏和风机的产能过剩。**\n\n1️⃣ **产能过剩有多严重？**\n中国现在生产了全球92%的太阳能组件、82%的风机。但全球实际需求远低于净零排放所需水平。结果是价格暴跌，行业利润被压到地板甚至亏损。光伏制造产能是全世界年安装量的两倍。\n\n2️⃣ **问题根源在“重制造、轻电网”**\n2020年“双碳”目标后，大量资本涌入发电端，但电网投资相对滞后。西部风光大基地建好了，电却送不出去，弃风弃光率飙升。这种投资错配，直接导致了“内卷”——企业为了抢市场份额，不惜亏本降价，行业整体被拖垮。\n\n3️⃣ **电网扩容是解药吗？**\n国网已承诺未来五年资本支出增加40%，2026年一季度电网投资同比暴增43%，重点建特高压。这能短期刺激能源需求、缓解弃电问题。但研报做了情景分析：**即使电网投资到位，也只能提供近期的需求缓解，无法根本吸收现有的产能过剩。**\n\n4️⃣ **真正需要什么？**\n结论是：**基础设施投资是必\n\n[... middle omitted ...]\n\nysis, we show that grid expansion provides meaningful near-term demand relief, though supply-side consolidation remains necessary to restore durable market equilibrium.\n\nAlicia García-Herrero \n\n[... middle omitted ...]\n\niews expressed are the researchers' own.\n\n![](images/64598e0fe98ac2dec0c04fe19cd775874edd541a895d257cf28946d123956eba.jpg)\n\nBruegel, Rue de la Charité 33, B-1210 Brussels (+32) 2 227 4210\ninfo@bruegel.org\nwww.bruegel.org"
  },
  {
    "id": "R013",
    "title": "经合组织：希腊人才外流真相，不是流失，而是待激活的全球网络",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "经合组织",
    "digest": "[wechat_article.md]\n# 经合组织：希腊人才外流真相，不是流失，而是待激活的全球网络\n\n希腊过去二十年经历了深刻的经济调整与复苏周期，伴随而来的是持续且规模可观的人才外流。当外界习惯性地将“人才流失”视为一个国家竞争力的负面信号时，经合组织（OECD）最新发布的《海外人才：希腊移民回顾》报告却提供了一个截然不同的分析框架：希腊海外侨民并非单纯的“流失”，而是一个规模庞大、教育水平高、且与本土经济存在持续互动潜力的“未激活资产”。报告的核心判断是，希腊面临的真正挑战不是如何阻止人才离开，而是如何通过制度设计，将海外人才的知识、网络和资本转化为国内经济增长的动力。\n\n这份报告并非简单的数据罗列，它整合了OECD移民数据库、人口普查、希腊科学家全球分布图谱以及多项调查数据，首次对希腊侨民的人口结构、教育水平、劳动力市场表现、回流趋势以及政策框架进行了系统性的全景扫描。其结论对于任何一个面临人口结构转型和全球人才竞争的经济体，都具有参照价值。\n\n> **KC评论：** 我们通常关注“人才流失”对母国的负面影响，但这份报告提醒我们，在全球化时代，人才流动的收益并非单向。关键问题在于母国是否具备“激活”海外人才网络的能力。报告中的图表和细分数据，恰恰揭示了哪些国家、哪些行业的人才回流潜力最大，这些细节比宏观结论更有价值。\n>\n> 继续看原文，真正有价值的是图表、假设和验证路径；完整报告与KC评论在每日汇编。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 海外希腊侨民规模持续扩大，但增速已放缓，结构性特征正在转变\n\n报告数据显示，截至2020/21年，生活在OECD国家的希腊裔人口已超过110万，占希腊本土人口的约10%。这一数字自2005年以来持续上升，但增速在近十年已明显放缓。与许多欧洲国家相比，希腊的移民率（侨民占本土人口比例）处于较高水平，但并非最\n\n[... middle omitted ...]\n\n购、对冲基金、资管机构、战略咨询和智库的朋友，期待与您交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n希腊人为什么离开，又为什么回来\n\n📊 研报拆解：海外希腊人全景\n\n---\n\n最近读了一份OECD关于希腊移民的深度报告，信息量很大，直接上干货👇\n\n**1. 海外希腊人画像**\n- 约一半在德国、美国、英国\n- 男性略多（53%），但女性受教育程度更高\n- 超过60%是中等以上学历，高学历比例持续上升\n- 主要做专业类工作：医生、工程师、IT、教育等\n\n**2. 移民潮的节奏**\n- 2010-2015年债务危机期间，移民人数激增\n- 2015年后开始回落，2020年以来显著下降\n- 德国是最热门目的地，但近年净流入已转负\n- 荷兰、瑞士、北欧国家增速最快\n\n**3. 回流的信号**\n- 2010年后回希腊的人数在增加\n- 主要原因：家庭因素（43%）、工作机会（30%）\n- 回流的年轻人比例高，但就业率低于从未离开的群体\n- 高学历者回流后更容易找到对口工作\n\n**4. 人才流动的特点**\n- 希腊博士生中，超过40%在海外工作\n- 主要研究领域：医学、工程、物理\n- 海外希腊科学家发表论文数量是国内的2倍\n- 但回国意愿在上升，尤其是年轻一代\n\n**5. 政策在跟进**\n- 希腊政府近年推出“Rebrai\n\n[... middle omitted ...]\n\nre supplied by and under the responsibility of the relevant Israeli authorities. The use of such data by the OECD is without prejudice to the status of the Golan Heights, East Jerusalem and Is\n\n[... middle omitted ...]\n\nd labour market outcomes, this review aims to strengthen the evidence base on Greeks abroad and support the design, refinement and consolidation of policies aligned with Greece's evolving approach to diaspora engagement."
  },
  {
    "id": "R014",
    "title": "经合组织：拉脱维亚地方经济，真正的隐形资产，不是GDP而是森林和博物馆",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "经合组织",
    "digest": "[wechat_article.md]\n# 经合组织：拉脱维亚地方经济，真正的隐形资产，不是GDP而是森林和博物馆\n\n拉脱维亚的地方经济正面临一个看似矛盾的局面：大量自然与文化资产并未转化为经济增长动力，而传统经济指标——GDP、就业率、人口——又无法捕捉这一结构性错配。经合组织（OECD）最新发布的拉脱维亚区域吸引力报告，首次在OECD国家中将“区域吸引力框架”下沉至市级层面，为42个市镇绘制了六维度的竞争力与生活质量诊断图。结论清晰：拉脱维亚最需要关注的，不是里加还能增长多少，而是那些拥有森林、博物馆、可再生能源，却留不住人、招不来游客的地区，到底缺什么。\n\n这份报告的价值不在于描述“城乡差距大”这一已知事实，而在于提供了一个可横向比较、可纵向追踪的系统性诊断工具。它揭示了三层此前未被量化的结构性矛盾：第一，经济吸引力高度集中于里加及周边少数市镇，拉特加尔地区的人均产出甚至低于欧盟最落后地区的基准；第二，自然与文化资产是拉脱维亚多数地区真正的“隐形优势”，但从旅游收入、绿色产业到人才吸引，这些优势几乎没有转化为经济结果；第三，数字与物理连接性不足，是比经济差距更普遍、更基础的限制因素，它削弱了所有地区——无论经济强弱——利用自身资产的能力。\n\n> **KC评论：** 这份报告最值钱的地方，不是它告诉你拉脱维亚有区域差距——这谁都知道。它真正做的是把“差距”拆解成了可操作的问题：哪些资产被浪费了？哪些连接断了？哪些市镇之间可以互补而不是竞争？完整报告里有一张“吸引力罗盘”图表，把每个市镇在六个维度上的表现画成一个雷达图，一眼就能看出哪个维度是短板。这种可视化工具，对地方政府制定优先级、对投资者判断选址，都比看GDP数据有用得多。\n\n继续看原文，真正有价值的是这些图表背后的假设和验证路径——比如为什么有些市镇森林覆盖率远超欧盟均值，但旅游人数只有可比较地区的零头；为什么里加周边的市镇并没有享受到预\n\n[... middle omitted ...]\n\ndge fund、资管机构、战略咨询、智库等朋友，期待交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n拉脱维亚地区，藏着多少被低估的潜力？\n\n**封面短标题：**\n拉脱维亚地区潜力\n\n**封面副标题：**\nOECD框架揭示的隐藏资产与挑战\n\n---\n\n最近读了一份OECD的区域发展报告，专门分析拉脱维亚的地区吸引力。信息量很大，但逻辑很清晰，分享几个有意思的发现。\n\n1️⃣ **经济高度集中，但“穷地方”也有亮点**\n拉脱维亚的经济活力基本集中在首都里加和周边几个市。大多数地区的GDP、生产率都远低于欧盟中位数。但有意思的是，一些经济最边缘的地区，房价增速反而最快——说明住房压力正在从核心区向外蔓延。\n\n2️⃣ **自然文化资产丰富，却转化不出经济价值**\n很多地区拥有超强的文化设施（博物馆、剧院密度高）、接近100%的可再生能源发电、远超欧盟平均的森林覆盖率。但游客数量只有欧盟同类地区的零头。资产和结果之间，存在明显断层。\n\n3️⃣ **连接性是最大的“隐形短板”**\n无论是数字网络还是交通基础设施，拉脱维亚很多地区的通达性都远低于区域平均水平。比如，部分市镇到学校和医院的通勤时间，是欧盟中位数的好几倍。这直接限制了人才和资本的流入。\n\n4️⃣ **OECD框架首次下沉到市级，提供五个实用场景**\n这次分析\n\n[... middle omitted ...]\n\ndice to the status of or sovereignty over any territory, to the delimitation of international frontiers and boundaries and to the name of any territory, city or area.\n\nPlease cite this publica\n\n[... middle omitted ...]\n\ner governance frameworks, better-resourced subnational institutions, and systematic use of multidimensional territorial data reinforce each other in support of more attractive, competitive, and resilient Latvian regions."
  },
  {
    "id": "R015",
    "title": "经合组织：5万亿美元欺诈损失背后，经合组织揭示战略评估缺失",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "经合组织",
    "digest": "[wechat_article.md]\n# 经合组织：5万亿美元欺诈损失背后，经合组织揭示战略评估缺失\n\n全球欺诈规模正在以惊人的速度膨胀。根据注册舞弊审查师协会（ACFE）的全球调查，各类组织每年因职业欺诈损失的金额约占其总收入的5%，折合超过5万亿美元。欧洲检察官办公室（EPPO）2025年年度报告显示，欺诈及其他损害欧盟预算的犯罪所造成的损失估计约为250亿欧元，同比激增22.5%，其中超过一半与跨境增值税欺诈相关，且系统性涉及有组织犯罪。\n\n面对这一趋势，各国政府并非毫无作为。越来越多的国家已采纳国家反欺诈战略（NAFS），试图从碎片化的机构干预转向“全政府”协同应对。然而，经合组织（OECD）最新发布的《评估、更新与监测反欺诈策略：方法论》报告揭示了一个尴尬的现实：大多数国家的反欺诈努力，卡在了“如何证明自己有效”这一环节。\n\n这份报告的核心判断是：当前反欺诈战略的最大短板，并非技术能力不足或法律框架缺失，而是缺乏一套设计严谨、嵌入战略周期、能够产生可验证证据的监测与评估（M&E）体系。没有这套体系，战略更新就只能依赖直觉而非证据，资源分配就难以优先排序，而公众信任也将因无法看见结果而持续流失。\n\n> **KC评论：** 如果用一个词概括这份报告的核心主张，那就是“证据链”。报告提供的不是一本反欺诈操作手册，而是一套方法论——如何设计指标、如何评估影响、如何将评估结果反馈到下一轮战略制定。对于任何一个正在制定或更新反欺诈战略的国家或机构，这套框架的价值不在于告诉你“该做什么”，而在于告诉你“如何知道自己做得对不对”。继续看原文，真正有价值的是图表、假设和验证路径；完整报告与KC评论在每日汇编。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 反欺诈战略的M&E体系，最晚应在战略设计阶段就嵌入\n\n报告明确指出，监测与评估体系最有效的设计时机，是在战略周期\n\n[... middle omitted ...]\n\ndge fund、资管机构、战略咨询、智库等朋友，期待交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n反欺诈策略，如何做到真有效？\n\n📌 防欺诈，不能只靠“查”\n\n很多国家都制定了反欺诈策略，但问题是：怎么知道这些策略真的有用？\n\n某国际组织最新发布的方法论，专门讲如何科学地评估、更新和监控反欺诈策略。核心逻辑超简单：**不能只盯着“做了多少事”，更要看“有没有用”**。\n\n1️⃣ **监控≠记流水账**\n- 很多监控系统只统计“开了多少会、出了多少文件”\n- 真正有效的监控，要看：欺诈风险有没有降低？控制措施有没有堵住漏洞？\n- 需要定性和定量指标结合，还要有独立验证机制\n\n2️⃣ **评估要分阶段**\n- 中期评估：及时发现问题，调整方向\n- 终期评估：总结教训，为下一轮策略提供依据\n- 评估标准：相关性、一致性、有效性、效率、影响力和可持续性\n\n3️⃣ **谁来干？**\n- 需要一个中央协调机构（比如AFCOS或类似部门）\n- 负责收集数据、验证信息、写报告、推动策略更新\n- 但具体执行部门要保留日常实施和汇报的主动权\n\n4️⃣ **别让公众“看热闹”**\n- 过度宣传欺诈有多严重，反而可能让人麻木或觉得“大家都这样”\n- 沟通要清晰、可信、建设性，和具体改革措施挂钩\n- 可以引入公民、学术机构、媒体参\n\n[... middle omitted ...]\n\nein, are without prejudice to the status of or sovereignty over any territory, to the delimitation of international frontiers and boundaries and to the name of any territory, city or area.\n\n##\n\n[... middle omitted ...]\n\nicipatory approaches, transparent communication and structured learning to strengthen resilience against fraud. It is complemented by practical tools designed to help countries build strong M&E frameworks for anti-fraud."
  },
  {
    "id": "R016",
    "title": "经合组织：中国城镇化启示，服务公平不是缩短距离，而是匹配容量",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "经合组织",
    "digest": "[wechat_article.md]\n# 经合组织：中国城镇化启示，服务公平不是缩短距离，而是匹配容量\n\n这份来自经合组织（OECD）的工作论文，表面上是在比较爱沙尼亚和荷兰两个小国的服务可及性，但它提出的核心判断，对任何一个关注人口流动、劳动力市场与社会公平的经济体都有深刻的政策含义：**“近”不等于“易得”，“远”不等于“不可达”。** 当我们将“竞争性可及性”（competitive accessibility）——即考虑了服务容量和本地需求压力的指标——纳入分析框架时，传统“城乡二元论”的结论被显著修正。城市居民享受短途通勤的便利，但往往面临更激烈的学位、名额或服务供给竞争；农村居民虽然需要更长的通勤时间，但一旦到达，其获得服务的实际概率可能更高。这一发现，直接挑战了当前许多国家在公共服务均等化政策中单纯追求“缩短物理距离”的路径依赖。\n\n**这篇报告的核心价值不在于它的具体数据，而在于它提供了一个可复制的分析框架：如何用“时间+容量+竞争”三个维度，重新定义“公平”。** 对于中国这样正在经历城镇化后期、面临人口收缩与公共服务布局调整的决策者与产业观察者而言，这个框架远比具体的爱沙尼亚或荷兰案例更具启发性。\n\n> **KC评论：** 如果你只关心“我家附近有没有学校/医院”，那你看的是最浅层的服务地图。这篇报告告诉你，更关键的问题是：这所学校有多少名额？有多少人同时在抢？你的通勤时间是否换来了更高的录取概率？这才是真实的“可及性”。\n\n继续看原文，真正有价值的是报告中对“双重重罚”群体的识别方法、分交通模式的可及性对比（步行、骑行、驾车、公共交通），以及“交通贫困”指标的构建逻辑。这些方法论和图表，在完整报告中均有详细拆解和可视化呈现。完整报告与KC评论在每日汇编中更新。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 物理距离只是冰山一角：竞争性可\n\n[... middle omitted ...]\n\ndge fund、资管机构、战略咨询、智库等朋友，期待交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n城市vs乡村：谁离服务更近？不一定\n\n服务可及性真相\n\n城市≠服务一定更易得，乡村≠处处是盲区。\n\n最近读OECD关于爱沙尼亚和荷兰服务可及性的研报，发现一个有意思的结论：**近≠容易进**。\n\n1/ 城市居民的通勤时间确实短，但竞争也激烈\n- 城市里幼儿园、小学的步行/公交时间比乡村短很多\n- 但！城市学位/名额有限，人多竞争大，“能进入”的概率反而可能低于乡村\n- 比如爱沙尼亚，城市里短途通勤的竞争可及性远高于乡村，但一旦通勤时间拉长，差距迅速缩小\n\n2/ 乡村的“双重劣势”人群值得关注\n- 约13-14%的小学生同时面临：通勤时间较长 + 竞争可及性较低\n- 爱沙尼亚乡村这一比例更高，空间差异明显\n- 荷兰因为人口密度高、设施布局均衡，情况相对好\n\n3/ 公共交通是关键变量\n- 没车的人，在乡村去公共就业服务中心（PES），公交时间经常超过40分钟\n- 即使在城市，最低可及性的20%人群，公交也未必是可行选项\n- 研报特别指出：**不能只靠距离判断“是否可及”，交通方式和容量限制同样重要**\n\n4/ 两国对比给我们的启发\n- 爱沙尼亚：人口分散、设施分散，乡村劣势更突出\n- 荷兰：密度高、设施集中，但城\n\n[... middle omitted ...]\n\nsification: I24, J13, O18, R23, R53\n\nVanda ALMEIDA (ELS/JAI; vanda.almeida@oecd.org);\n\nFilippo BRUNELLI (EC DG JRC; filippo.brunelli@ec.europa.eu);\n\nJakub CAISL (EC DG EMPL; jakub.caisl@ec.eur\n\n[... middle omitted ...]\n\n>4</td><td>4</td><td>-</td><td>5</td></tr></table>\n\nSource: Based on service data specified in Annex A, Eurostat (2025[33]) population grids and the Eurostat (2024[34]) degree of urbanisation classification at LAU level."
  },
  {
    "id": "R017",
    "title": "经合组织：科特迪瓦数据颠覆认知，年轻男性反而更支持传统性别角色",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "经合组织",
    "digest": "[wechat_article.md]\n# 经合组织：科特迪瓦数据颠覆认知，年轻男性反而更支持传统性别角色\n\n理解性别不平等，传统上我们关注的是女性在教育、就业、健康等领域的可观测差距。但一份来自经合组织的最新深度报告，将矛头指向了一个更根本、也更隐蔽的结构性变量：**社会如何定义“做一个男人”**。\n\n这份针对科特迪瓦和塞内加尔的实证研究揭示了一个核心判断：西非国家性别平等的真正瓶颈，不在于法律条文或资源分配，而在于一套根深蒂固的、关于男性角色的“限制性男性气质规范”。这些规范——包括“男性必须是养家糊口者”、“男性拥有最终决策权”、“男性应当控制家庭资源”——不仅直接限制了女性的经济赋权，构成了家庭暴力的深层土壤，也反过来伤害着男性自身的身心健康。\n\n报告明确指出，这些规范并非不可改变。一个关键的发现是，在科特迪瓦，存在一个“沉默的差距”：个人的真实信念与社会感知到的“别人怎么想”之间存在巨大错位。人们普遍高估了男性对限制性规范的支持度，同时低估了女性的支持度。这意味着，推动变革的社会基础可能比我们想象的更坚实，关键在于如何打破这种“误解的囚笼”。\n\n这份报告的价值不在于重复“性别不平等是个问题”，而在于提供了一个可量化、可追踪的“男性气质指数”，将模糊的文化概念转化为诊断工具。它让政策制定者和投资者看到，如果不触及这些底层规范，单纯增加女性信贷、培训或法律保护，其效果都将被文化惯性所侵蚀。\n\n> **KC评论：** 这份报告的核心洞察在于，它把“男性气质”从一个社会学议题，变成了一个可测量的发展指标。对于关注非洲市场、尤其是西非消费和劳动力市场的读者来说，这提供了一个理解社会变迁的底层框架。真正的机会不在于等待规范改变，而在于识别出那些正在松动、可以被“推一把”的节点。继续看原文，真正有价值的是它构建的“十项规范框架”和“男性气质指数”的计算方法，以及每个国家的具体数据分布。\n\n---\n\n!\n\n[... middle omitted ...]\n\n给AI、也可人工快速扫描的“市场情报流”。我们期待与你交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n男人不一定要“扛一切”\n科特迪瓦与塞内加尔的真相\n\n📌 为什么聊男性气质？因为它直接决定了女性能不能平等工作、安全生活。\n\n最近读了OECD一份关于科特迪瓦和塞内加尔的研究报告，讲的是“限制性男性气质”如何影响性别平等。简单说，就是社会对“男人该怎样”的刻板期待，其实也绑住了女性。\n\n1️⃣ **“养家”和“做主”是核心**\n研究提炼了10条“男人准则”，最核心的两条是：\n- 男人必须是经济支柱\n- 男人应该做家庭决策者\n这两条在科特迪瓦和塞内加尔都特别强。\n\n2️⃣ **一个“沉默的鸿沟”**\n有意思的是，人们普遍高估了男人对“传统男人形象”的支持度，也低估了女性的支持度。也就是说，很多人其实没那么保守，但以为别人都很保守——这种“误解”反而让改变更难。\n\n3️⃣ **家务是女性的“第二份工”**\n绝大多数人认为家务和育儿是女人的事。结果女性一边做大量无酬劳动，一边更难进入或留在好工作里。在科特迪瓦和塞内加尔，性别职业隔离非常明显。\n\n4️⃣ **暴力不是“个人问题”**\n报告发现，支持“男人养家”这个观念越强的男性，越容易实施亲密伴侣暴力。而且，很多人觉得“女人被打”在某些情况下可以接受——比如她没做好饭\n\n[... middle omitted ...]\n\ne to the status of or sovereignty over any territory, to the delimitation of international frontiers and boundaries and to the name of any territory, city or area.\n\nOECD (2026), Masculinity an\n\n[... middle omitted ...]\n\ne to better understand and measure these norms. In doing so, it will support their efforts to promote positive, gender-equitable masculinities as a way of advancing gender equality and addressing structural inequalities."
  },
  {
    "id": "R018",
    "title": "经合组织：未来十年全球农业增长的真正瓶颈不是土地，是劳动力",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "经合组织",
    "digest": "[wechat_article.md]\n# 经合组织：未来十年全球农业增长的真正瓶颈不是土地，是劳动力\n\n全球农业正在经历一个被低估的结构性拐点。经合组织与联合国粮农组织联合发布的《Agricultural Outlook 2026-2035》给出了一个看似温和、实则深刻的核心判断：未来十年全球农产品产量将增长13%，但这个数字背后的驱动力正在从面积扩张转向生产率提升，而生产率提升的最大制约因素并非技术或资本，而是农业劳动力的老龄化与收入波动性。这份报告第一次系统性地将“农业劳动生产率”和“农业工人收入波动”纳入十年展望的核心分析框架，其隐含的逻辑链条值得每一位关注大宗商品、全球供应链和新兴市场发展的决策者仔细拆解。\n\n报告开篇就用数据点明了这个趋势。全球农业直接温室气体排放预计仅增长6%，远低于产量增速，说明集约化而非粗放扩张是主旋律。但真正值得关注的，是报告首次引入的农业劳动生产率指标：到2035年，全球农业工人人均毛收入预计增长9%。这个数字听起来不算差，但报告随后揭示了一个令人不安的波动性——即使在基准情景下，仍有25%的概率出现农业工人收入下降3%的情况。这意味着，全球农业增产的收益分配将比以往更加不均匀，而那些依赖小农经济的低收入国家，可能成为这一轮生产率竞赛中的输家。\n\n> **KC评论：** 这份报告的核心价值不在于预测玉米或大豆的价格，而在于它把“人”的因素重新放回了农业分析的中心。过去十年，市场讨论农业问题时，焦点几乎都在天气、政策补贴和贸易摩擦上。但经合组织这次明确告诉你：劳动力老化、生产率差异和收入波动，正在成为比土地更稀缺的约束条件。完整报告里有一整节专门拆解不同国家农业劳动生产率的结构性差异，以及这些差异如何影响未来十年的贸易格局——这些图表和假设才是真正值得花时间细读的部分。\n\n继续看原文，真正有价值的是图表、假设和验证路径；完整报告与KC评论在每日汇编。\n\n![研报\n\n[... middle omitted ...]\n\ndge fund、资管机构、战略咨询、智库等朋友，期待交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球粮食未来十年，这份报告讲透了\n\n🌾 未来十年，粮食怎么变？\n\nOECD和FAO联合发布的《农业展望2026-2035》来了，信息量很大，挑重点讲。\n\n1️⃣ 产量增长靠效率，不是靠地\n- 全球农业产量预计增长13%\n- 主要靠技术进步和集约化，不是开荒\n- 增长主力在亚洲、撒哈拉以南非洲和拉美\n\n2️⃣ 碳排放增速远低于产量\n- 直接农业温室气体排放只增6%\n- 说明生产效率在提升，单位产品碳排下降\n\n3️⃣ 农民收入有隐忧\n- 到2035年，全球农业劳动收入预计增9%\n- 但仍有25%概率出现3%的下降\n- 自然灾害、市场波动影响很大\n\n4️⃣ 地缘冲突冲击粮食安全\n- 报告特别分析了中东冲突影响\n- 化肥使用受限→低收国家谷物减产\n- 国际贸易成为关键缓冲\n\n5️⃣ 劳动力老龄化是隐形成本\n- 很多地区农业从业者超55岁比例上升\n- 年轻劳动力流失，影响长期产出\n\n📌 总体判断：未来十年农业靠效率驱动，但地缘风险和气候波动仍是最大变量。贸易体系能否稳定运行，直接决定粮食安全。\n\n#学习笔记\n\n[source_mineru.md]\n# OECD-FAO Agricultural Outlook 2026\n\n[... middle omitted ...]\n\n9614c1a988355538e0efc835ce2138.jpg)\n\n## Attribution 3.0 IGO (CC BY 3.0 IGO)\n\nThis work is made available under the Creative Commons Attribution 3.0 IGO licence. By using this work, you accept \n\n[... middle omitted ...]\n\nncome countries. In this context, international agricultural trade remains critical to balance supply and demand and mitigate adverse food security impacts.\n\nMore information is available at https://www.agri-outlook.org."
  },
  {
    "id": "R019",
    "title": "经合组织：不是口号而是规则，经合组织指出84%成员国已立法推动企业尽责管理",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "经合组织",
    "digest": "[wechat_article.md]\n# 经合组织：不是口号而是规则，经合组织指出84%成员国已立法推动企业尽责管理\n\n全球最大的一万家上市公司中，超过三分之二已经公开做出了负责任商业行为的承诺。但这份由经合组织在2026年发布的《负责任商业展望》揭示了一个比承诺本身更值得关注的信号：承诺与执行之间的差距，不是简单的“说得多做得少”，而是正在重塑全球供应链的竞争规则。那些能够将承诺转化为可验证执行力的企业，正在获得政策红利和资本信任；而那些停留在口号层面的公司，将面临越来越高的合规成本与声誉风险。\n\n这份报告首次系统评估了全球大型上市公司的环境与社会尽责管理实践，并同步审视了52个经合组织成员国政府如何通过公共政策推动这一进程。它给出的核心判断是：负责任商业行为已经从“自愿倡议”阶段，进入“政策驱动+市场筛选”的新周期。对于中国出海企业、跨国供应链管理者以及关注ESG投资的机构而言，理解这一转变的底层逻辑，比追踪任何单一政策条款都更重要。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 承诺覆盖率高，但尽责管理深度不足——这才是真正的结构性风险\n\n报告数据显示，69%的全球大型上市公司在至少一个议题上做出了负责任商业行为的公开承诺。其中，反腐败和温室气体排放是最常见的承诺领域，其次是强迫劳动、童工和人权。然而，当报告将这些承诺与实际的尽责管理流程进行对比时，差距立刻显现。\n\n企业平均在“政策和管理系统”维度的披露率达到45%，但在“识别和评估影响”维度骤降至不足20%，在“预防、减缓与补救”维度更是低于20%。这意味着，大量企业建立了制度框架，却没有真正运行风险识别和问题解决的闭环。\n\n> **KC评论：** 对投资者而言，承诺率高不等于风险低。真正需要关注的不是企业说了什么，而是它有没有建立“识别-评估-应对-补救”的完整链条。报告中的图表提供了分行业、分地\n\n[... middle omitted ...]\n\n购、对冲基金、资管机构、战略咨询和智库的朋友，期待与你交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n69%公司承诺了，但只有少数在行动\n\n**封面短标题：**\n承诺vs现实\n\n**封面副标题：**\nOECD首份责任商业报告解析\n\n---\n\n最近看了一份OECD的报告，讲的是全球大公司在“负责任商业行为”上的真实表现。\n\n结论有点扎心：**说得多，做得少。**\n\n1️⃣ **承诺很普遍，但执行跟不上**\n全球前1万家上市公司里，69%都公开承诺了至少一项责任商业议题（比如减碳、反强迫劳动）。\n但真正把承诺落到实处的公司，比例不到20%。\n——报告里有个数据很直观：45%的公司有制度框架，但真正采取措施去识别和解决问题的，不到20%。\n\n2️⃣ **供应链是最大盲区**\n很多公司对自家工厂管得还行，但一涉及供应商就松散。\n比如：一半公司有供应商筛选标准，但只有不到20%会真的去评估供应商风险。\n更夸张的是，只有少数公司知道自己原材料从哪来——尤其是矿产这类高风险行业。\n\n3️⃣ **政府也在推，但力度不一**\n52个OECD成员国中，84%已经出台了环境/社会尽责管理法规。\n但各国政策成熟度差异很大，有些只是“有”，有些已经细化到执行指南。\n报告特别提到：政府自己作为采购方、国企股东、出口信贷机构，也应该带头示\n\n[... middle omitted ...]\n\nterritory, city or area.\n\nThe statistical data for Israel are supplied by and under the responsibility of the relevant Israeli authorities. The use of such data by the OECD is without prejudic\n\n[... middle omitted ...]\n\nnts are promoting responsible business conduct across the 52 countries adhering to the OECD Guidelines for Multinational Enterprises for Responsible Business Conduct, drawing on desk research and a survey of governments."
  },
  {
    "id": "R020",
    "title": "经合组织：不是意识形态而是治理能力，经合组织揭示政府信任的真正驱动力",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "经合组织",
    "digest": "[wechat_article.md]\n# 经合组织：不是意识形态而是治理能力，经合组织揭示政府信任的真正驱动力\n\n过去三年，从新冠疫情到通胀冲击，从地缘冲突到AI治理，全球公众对政府的信任似乎经历了前所未有的压力测试。市场普遍担忧“信任崩溃”正在侵蚀民主制度的合法性，甚至成为长期经济增长的隐形税负。\n\n但经合组织（OECD）刚刚发布的第三轮《公共机构信任驱动因素调查》（2025年结果）给出了一个更微妙的判断：**全球平均信任水平并未出现断崖式下跌，但信任的结构正在发生根本性转移**。那些决定“谁信任政府、为何信任政府”的底层因素，正在被新的力量重塑——日常服务体验、复杂决策能力、以及AI治理的透明度，正在取代传统的政治意识形态，成为信任的新锚点。\n\n这份覆盖33个OECD成员国和5个候选国的调查，不仅是全球最系统的政府信任度测量，更是一个关于“现代治理能力如何被公众定价”的晴雨表。对于关注长期政策环境、跨境投资和公共治理质量的读者来说，这组数据比任何宏观经济指标都更接近“制度溢价”的真实刻度。\n\n> **KC评论：** 这份报告最值得关注的不是“信任率上升还是下降”这个总量问题，而是“信任的驱动力正在从意识形态转向治理能力”这个结构变化。如果过去信任取决于“你支持哪个政党”，未来信任将取决于“政府能不能让AI审批不出错、能不能让社保申请三天内办完”。这对企业意味着：政策环境的可预测性，正在被具体行政能力重新定义。\n\n继续看原文，真正有价值的是图表的分解逻辑、不同机构信任驱动因素的对比，以及AI治理这个全新维度如何嵌入传统信任框架。完整报告与KC评论在每日汇编。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 信任水平没有崩溃，但“信任的分布”正在剧烈分化\n\n调查显示，OECD国家中约40%的受访者对本国政府持有“高”或“中高”信任度。这一比例与2023年调查结\n\n[... middle omitted ...]\n\ndge fund、资管机构、战略咨询、智库等朋友，期待交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nOECD信任调查2026：政府信任度全景\n\n**信任是门科学**\n\n**3大维度拆解公众对政府的真实看法**\n\n---\n\n最近看了OECD 2026年发布的《公共机构信任驱动因素调查》，覆盖33个OECD成员国+5个候选国，样本量巨大。几个核心发现值得记录：\n\n**1/ 信任水平：整体稳定，但分化明显**\n- 约四成受访者对本国政府有“高”或“中高”信任度\n- 2023到2025年，OECD平均信任水平基本持平\n- 但希腊等国的信任波动在加剧——从2010年代初开始，信任的涨跌幅度越来越大\n\n**2/ 信任的三大驱动因子**\n- **可靠性**：多数人相信政府在重大紧急情况下能保护民众，但对经济危机中的保护能力信心不足\n- **回应性**：仅三分之一的人认为“像我这样的人”对政府决策有发言权，或政府能超越特殊利益\n- **公平性**：对行政服务和数据保护满意度较高，但腐败感知是信任的“杀手”——认为腐败是主要问题的人群，信任度明显低于整体\n\n**3/ 谁更信任政府？**\n- 有“政治能动感”（觉得能影响决策）的人信任度更高\n- 执政党支持者信任度更高，且这种“党派信任差距”在扩大\n- 教育程度低、有财务压力、\n\n[... middle omitted ...]\n\noundaries and to the name of any territory, city or area.\n\nPlease cite this publication as:\nOECD (2026), OECD Survey on Drivers of Trust in Public Institutions 2026 Results: Navigating Rising \n\n[... middle omitted ...]\n\nures, people's views on the potential effects of government use of artificial intelligence, and the perceived barriers to and impacts of political participation provide novel insights based on newly introduced questions."
  },
  {
    "id": "R021",
    "title": "经合组织：不是地方税而是转移支付，经合组织重审92国财政分权数据",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "经合组织",
    "digest": "[wechat_article.md]\n# 经合组织：不是地方税而是转移支付，经合组织重审92国财政分权数据\n\n地方税占财政收入的比例，长期以来被视为衡量一国财政分权程度的核心指标。学术界用它来检验分权与经济增长的关系，政策制定者用它来评估地方政府的财政自主权。但一份来自经合组织（OECD）的最新工作论文，对这些数据的底层逻辑提出了根本性质疑。\n\n这份由Junghun Kim撰写的报告，系统性地梳理了全球92个国家的数据，并得出一个令人不安的结论：按照国际通行的国民账户体系（SNA 2008）标准，许多国家上报的“地方税”收入，实际上更接近中央政府的转移支付。在75%的样本国家中，真实的地方税占比低于10%。真正拥有实质性地方税收自主权的国家，可能只有加拿大、德国、瑞士、美国、西班牙和瑞典六个。\n\n这不是一个关于统计口径的学术争论。它直接关系到我们如何理解中央与地方的财政关系，如何评估分权改革的成效，以及如何解读以此为基础的学术研究。如果底层数据就存在系统性偏差，那么建立在这一基础之上的政策讨论，很可能是空中楼阁。\n\n> **KC评论：** 这不是一个冷门的会计问题。它意味着，我们平时看到的“中国地方税占比”“日本地方税占比”等数据，可能严重高估了地方政府的实际征税权力。报告的核心贡献在于，它提供了一个重新审视这些数据的框架。继续看原文，真正有价值的是对德国和日本两个典型案例长达百年的制度演变分析，以及据此提出的再分类标准。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 地方税的定义，在2008年经历了一次“范式转换”\n\n要理解当前数据的问题，必须先回到国际统计标准的演变。在2008年之前，联合国、OECD和IMF对“地方税”的定义相对宽泛。根据1993年的国民账户体系（SNA 1993），只要一个税种的收入是“自动且无条件地”基于来源地原则划归地方政府，就可\n\n[... middle omitted ...]\n\ne fund、资管机构、战略咨询、智库等朋友，期待与你交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n地方税数据，可能全是假象？\n\n地方税 ≠ 地方说了算\n\n某外资投行最新研报拆解了一个被忽视的问题：很多国家报给OECD的“地方税”数据，其实根本不是地方自己定的税。\n\n1️⃣ 标准怎么定的？\nSNA 2008明确：一项税收要算作地方税，地方必须有实际的税率或税基决定权。不是中央收完分给你就叫地方税。\n\n2️⃣ 德国和日本是典型案例\n- 德国：很多是“联合税制”，州和联邦共同决定，不是地方自主\n- 日本：地方税税率由中央立法统一规定，地方基本没选择权\n结论：这些税按标准该算中央税或转移支付，不是地方税。\n\n3️⃣ 数据偏差有多大？\n研报分析了92个国家，75%的地方税份额低于10%。按标准重新归类后，只有6个国家地方税份额超30%：加拿大、德国、瑞士、美国（都是联邦制）+ 西班牙（区域制）+ 瑞典。\n\n4️⃣ 法国是个有趣的反转\n法国地方税从“中央定地方税”演变成“中央定分成制”，现在地方拿的VAT份额占地方总收入近30%，但地方对VAT税率和税基零控制权。\n\n所以，下次看到“地方税占比”指标，记得问一句：到底谁说了算？\n\n#学习笔记\n\n[source_mineru.md]\n# Revisiting local\n\n[... middle omitted ...]\n\nsarily reflect the official views of the Member countries of the OECD. Working Papers describe preliminary results or research in progress by the author(s) and are published to stimulate discu\n\n[... middle omitted ...]\n\nntina, the Bahamas, Barbados, Belize, Bolivia, Brazil, the Dominican Republic, Ecuador, El Salvador, Guatemala, Guyana, Honduras, Jamaica, Nicaragua, Panama, Paraguay, Peru, Saint Lucia, Trinidad and Tobago, and Uruguay."
  },
  {
    "id": "R022",
    "title": "经合组织：住房支出挤压消费，经合组织给出一个被低估的政策工具",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "经合组织",
    "digest": "[wechat_article.md]\n# 经合组织：住房支出挤压消费，经合组织给出一个被低估的政策工具\n\n过去三十年，经合组织国家的实际房价几乎无一例外地上涨。与此同时，住房支出在家庭总消费中的占比持续攀升，挤压了其他消费空间。这场危机最直接的受害者是低收入家庭和年轻人——在经合组织国家中，约五分之二的低收入租户将其可支配收入的40%以上用于支付房租，而在超过一半的成员国中，多数20至29岁的年轻人仍与父母同住。市场自身已无法解决这一困境。\n\n但经合组织最新发布的这份报告，提出了一个与多数政策讨论方向不同的核心判断：缓解住房可负担性危机的关键，并非大规模新建住房，而在于更聪明地激活存量住房，并设计可持续的融资机制。这个判断背后，是对过去三十年住房政策逻辑的深刻反思——长期依赖支持自有住房的政策，可能恰恰加剧了当前的困境。\n\n报告指出，在约三分之二的经合组织国家中，社会保障性租赁住房仅占住房总量的不到5%。自2010年以来，几乎所有有数据可查的国家中，这一比例都在下降。供给不足的同时，需求侧的压力却在持续累积——人口老龄化、移民流动、家庭规模缩小等结构性因素，使得住房需求的结构发生了根本性变化。\n\n> **KC评论：** 这份报告最有价值的地方，在于它没有简单地把问题归咎于“盖得不够多”，而是系统性地拆解了供给端和需求端的多重错配。对于关注房地产市场的读者来说，报告中的图表数据——尤其是各国空置率与社保住房占比的对比——才是真正值得细读的资产。继续看原文，真正有价值的是这些跨国数据背后的政策实验和效果验证路径；完整报告与KC评论在每日汇编。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 激活存量住房，比新建更紧迫、也更现实\n\n报告明确给出了一个优先级判断：在财政和环境资源都受限的背景下，首先应该考虑的是激活现有存量住房，而非大规模新建。这不仅是短期缓解市场压力\n\n[... middle omitted ...]\n\n表合集，便于您快速扫描市场动态，也便于喂给AI进行后续分析。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n住房危机，关键在供给端\n\n激活存量+撬动资金\n\n住房可负担性问题的根源，是供给跟不上需求\n\n翻了一篇OECD研报，核心逻辑很清晰。为什么房价租金涨得比工资快？因为建房子变贵了、建筑工人缺、贷款利息高、土地政策严、公共投入少。结果就是：年轻人买房越来越难，租客租金负担越来越重。\n\n怎么解？两条腿走路。\n\n1️⃣ 激活存量房：别只盯着“新建”，先看存量\n\nOECD数据显示，21个国家里，空置房至少占总存量的7%。法国有9.3万套通过“租赁中介计划”以低于市场价出租。核心做法：\n\n- 给房东好处（稳定租金、管理服务、税收优惠），让他们把房子以低于市场价出租\n- 政府或社会租赁机构做中间人，分担房东风险\n- 同时配合空置税或税收减免，提高存量利用效率\n\n但注意，不是所有空置房都能用。位置差、条件烂的，激活成本可能高于收益。需要先做详细评估。\n\n2️⃣ 撬动公私资金建新房：公共资金做杠杆，吸引私人资本\n\n核心逻辑：公共资金不是全包，而是“撬动”。方法包括：\n\n- 建立专项融资机制，定期评估住房需求来确定资金规模\n- 租金设定要覆盖开发成本，同时保持可负担\n- 密切监控建筑成本和借贷利率变化，动态调整租金和补贴\n\n关键是\n\n[... middle omitted ...]\n\nis insufficient to meet demand.\n\n\\- Expanding the supply of affordable and social rental housing is a key part of the policy solution. This has the dual benefit of protecting low-income and vu\n\n[... middle omitted ...]\n\ner this licence shall be settled by arbitration in accordance with the Permanent Court of Arbitration (PCA) Arbitration Rules 2012. The seat of arbitration shall be Paris (France). The number of arbitrators shall be one."
  },
  {
    "id": "R023",
    "title": "经合组织：不是援助故事，经合组织十年帮发展中国家增收27亿美元",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "经合组织",
    "digest": "[wechat_article.md]\n# 经合组织：不是援助故事，经合组织十年帮发展中国家增收27亿美元\n\n全球发展融资正经历一场静默的转向。当官方发展援助（ODA）面临越来越大的预算约束，发展中国家如何在不依赖外部赠款的前提下，为基础设施、教育和公共卫生筹集可持续的财政收入？一份由经合组织（OECD）与联合国开发计划署（UNDP）联合发布的年度报告，提供了一个被长期低估的答案：税务稽查能力建设。\n\n这份名为《无国界税务稽查员（TIWB）2026年度报告》的文件，系统回顾了该倡议自2015年启动以来十年的成果。截至2025年底，TIWB已在71个发展中国家实施了165个援助项目，帮助这些国家额外征收了27.2亿美元的税收，并确认了76.7亿美元的税务评估，同时拒绝了25.3亿美元的亏损结转。更引人注目的是其投入产出比——每投入1美元，就能带来125美元的额外税收。\n\n这不是一个关于“援助”的故事，而是一个关于“能力转移”的叙事。在主权债务压力上升、全球最低税规则落地、数字经济征税需求激增的背景下，TIWB 2.0版本在2025年第四次发展筹资国际会议（FFD4）上正式发布。其核心逻辑正在改变：从发达国家单向“教”发展中国家如何查税，转向构建一个南南合作与三角合作的可持续技术转移网络。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 这轮变化真正考验的是企业能否把规模转化为议价权\n\nTIWB的起点并不宏大。2015年，OECD和UNDP联合发起这一倡议时，核心想法很简单：把有经验的税务稽查员派到发展中国家，让他们和当地官员一起处理真实的审计案件。不是讲课，不是写报告，而是手把手地查案子。\n\n十年后，这一模式被证明有效。报告显示，TIWB的援助范围已经从最初的转让定价和国际税务审计，扩展到刑事税务调查、金融账户信息自动交换（AEOI）的有效利用、国别报告（CbCR\n\n[... middle omitted ...]\n\n fund、资管机构、战略咨询、智库等机构，期待与你的交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n跨境征税神队友：TIWB十年成绩单\n\n💰 一个国际组织，帮发展中国家多收了27亿美元税款\n\n**十年，71国，165个项目**\n\nTIWB（跨境税务无国界）是OECD和UNDP的联合项目，核心操作：派资深税务专家到发展中国家，手把手带当地官员做真实审计案件。\n\n数据很扎实：\n- 累计增收：27.2亿美元\n- 额外评估税款：76.7亿美元\n- 阻止亏损结转：25.3亿美元\n- 每投入1美元，回报125美元\n\n1️⃣ **非洲是最大受益区**\n与非洲税务管理论坛（ATAF）合作，96个项目落地，贡献了22亿美元增收。不是纸上谈兵，是真刀真枪的实战带教。\n\n2️⃣ **从单一到多元**\n最初只做转让定价审计，现在覆盖：税务犯罪调查、金融账户信息自动交换、国别报告、数字化税务管理。2025年新增全球最低税实施支持，即将拓展数字贸易增值税审计。\n\n3️⃣ **不止是收钱**\n洪都拉斯、埃及、秘鲁的案例显示，项目还推动了税务机构改革、提升技术能力、促进纳税人自愿合规。能力建设效果比账面数字更持久。\n\n4️⃣ **升级版2.0启动**\n2025年FFD4大会推出TIWB 2.0，强化南南合作和三角合作，让全球南方国家之间也\n\n[... middle omitted ...]\n\nation follow the practice of OECD.\n\nThis document, as well as any data and map included herein, are without prejudice to the status of or sovereignty over any territory, to the delimitation of\n\n[... middle omitted ...]\n\n 2025 to refresh and strengthen the initiative. Chapter 7 reviews the objectives established for 2025 and presents the objectives for 2026, aligned with strategic targets and resource availability.\n\nFor more information:"
  },
  {
    "id": "R024",
    "title": "经合组织：全球竞业限制法规的隐性成本与政策拐点",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "经合组织",
    "digest": "[wechat_article.md]\n# 经合组织：全球竞业限制法规的隐性成本与政策拐点\n\n竞业限制条款正在全球范围内经历一场前所未有的政策审视。经合组织（OECD）最新发布的工作论文，首次系统性地构建了覆盖38个成员国的竞业限制监管严格度指数，揭示了一个被长期忽视的结构性问题：多数国家的法律框架在保护企业正当利益与维护劳动力市场活力之间，存在系统性失衡。\n\n这份报告的核心判断是：当前竞业限制条款的监管体系普遍偏弱，尤其是在执行机制和补偿要求上存在显著漏洞，导致这些条款被过度使用，甚至延伸至低技能劳动者群体，最终抑制了工资增长、劳动力流动和创新活力。这不是一个仅仅关乎法律技术细节的议题，而是直接影响经济动态效率的结构性变量。\n\n> **KC评论：** 竞业限制条款的监管，本质上是在“企业保护商业秘密的合理诉求”与“劳动者自由择业的基本权利”之间寻找平衡点。OECD这份报告的意义在于，它用一套统一的框架，让我们第一次看清不同国家在这个天平上的位置差异，以及这些差异背后隐藏的经济代价。\n\n继续看原文，真正有价值的是OECD构建的指数框架、各国评分背后的具体法律设计差异，以及这些差异如何与劳动力市场表现产生关联。完整报告与KC评论在每日汇编。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 竞业限制的“双面性”决定了监管必须精细化\n\n报告开篇就点明了竞业限制条款的两个截然不同的功能面向。从正面看，它可以保护企业的商业秘密、客户关系以及针对员工的培训投资，解决所谓的“敲竹杠”问题——即企业担心员工带着投入的知识和客户关系跳槽或创业，从而不敢进行长期、不可逆的投资。从这个逻辑出发，竞业限制应当只适用于掌握敏感信息的高技能员工，并伴随相应的经济补偿。\n\n但从反面看，竞业限制条款可以被用作限制劳动力市场竞争的工具。通过削弱员工的外部选择权，企业可以压低工资水平，不仅影响跳槽\n\n[... middle omitted ...]\n\ndge fund、资管机构、战略咨询、智库等朋友，期待交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n竞业协议，真的合理吗？\n\n全球竞业监管地图\n\n从打工人的角度看这份研报\n\n最近读到一份OECD的竞业协议研究报告，发现几个有意思的点，分享给大家一起思考。\n\n1️⃣ 竞业协议的“双面性”\n- 初衷：保护企业商业秘密、客户资源、培训投入\n- 现实：很多企业用它来限制员工跳槽、压低工资\n- 关键问题：大量低技能、无核心信息的员工也被要求签\n\n2️⃣ 全球监管差异巨大\n- 严格型：加州、智利、墨西哥等，基本不执行\n- 温和型：大部分欧盟国家、日本，有一定限制\n- 宽松型：以色列、佛罗里达等，企业说了算\n\n3️⃣ 监管的9个关键维度\n① 是否有专门法律规范\n② 集体协议是否参与\n③ 企业保护利益是否明确\n④ 是否需要额外补偿\n⑤ 续签是否算新的对价\n⑥ 举证责任在谁\n⑦ 法院能否修改条款\n⑧ 被解雇后是否仍有效\n⑨ 违规使用是否有惩罚\n\n4️⃣ 值得关注的趋势\n- 美国FTC正在推动全面禁止\n- 澳大利亚、加拿大、芬兰都在收紧\n- 补偿要求和工资门槛成为主流\n\n5️⃣ 个人思考\n竞业协议本质是保护企业利益，但当它被滥用到清洁工、收银员身上时，是否已经偏离了初衷？\n\n大家觉得竞业协议合理吗？欢迎一起讨论。\n\n#学习笔记\n\n[... middle omitted ...]\n\nsibility of the Secretary-General of the OECD and does not necessarily reflect the official views of OECD Member countries.\n\nThis document, as well as any data and map included herein, are wit\n\n[... middle omitted ...]\n\nginal Bishara index  \n![](images/da4f23ab7153fde8a829d1a1c30f511db5e7951381415dc39355a46eec4ec8f9.jpg)\n\nFigure B.2. OECD index unweighted  \n![](images/7eb6530a01172e9dce4bdefe464c8b3dd828678610edd8113eb44f7db8f897cb.jpg)"
  },
  {
    "id": "R025",
    "title": "联合国贸发会议：联合国贸发报告，发展中国家每流入1美元，72美分流回境外",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "联合国贸发会议",
    "digest": "[wechat_article.md]\n# 联合国贸发会议：联合国贸发报告，发展中国家每流入1美元，72美分流回境外\n\n2024年，流向发展中国家的外部金融资本接近1.5万亿美元，几乎与发达国家当年获得的规模相当。但有一个数字让这个表面乐观的总量失去了光彩：同年，发展中国家为偿还这些外部负债所支付的利润、股息和利息，相当于新流入资金的72%。换句话说，每流入1美元，就有0.72美元以回报形式流回境外。\n\n这不是一个简单的“借新还旧”故事。联合国贸发会议（UNCTAD）最新发布的《融资发展：发展中国家外部资本流动及其成本》技术报告揭示了一个更令人不安的结构性事实：发展中国家的外部融资成本不仅高于发达国家，而且其增长速度正在系统性侵蚀本就有限的财政空间。2018年至2024年间，99个发展中国家——覆盖55亿人口——因公共部门利息支出上升，导致可用于其他事项（包括可持续发展目标）的政府收入份额持续下降。\n\n这份报告的价值不在于它发现了“发展中国家融资贵”这个常识，而在于它用长达十年的数据完整绘制了“成本如何吞噬发展空间”的传导链条。对于关注全球资本流动、主权债务风险以及新兴市场资产定价的决策者和投资者而言，这些数字背后隐藏着对未来数年全球资金配置格局的重要暗示。\n\n> **KC评论：** 72%这个比例意味着，发展中国家从国际资本市场获得的资金，大部分并未真正转化为国内投资或消费，而是以利息和利润的形式回流。这本质上是一种“金融漏斗”。完整报告用更细致的图表拆解了这个漏斗在不同国家组别（新兴市场、前沿市场、其他发展中经济体）的差异——这些差异恰恰是理解主权信用分化趋势的关键。\n\n继续看原文，真正有价值的是报告中的图表、假设和验证路径。完整报告与KC评论在每日汇编中持续更新。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 外部融资的波动性主要由债务流动驱动，而非股权\n\n[... middle omitted ...]\n\n金、资管机构、战略咨询、智库等领域的专业人士，期待与你交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n发展中国家借钱越来越贵了｜投研笔记\n\n封面：借钱成本在飙升\n\n副标题：UN报告拆解外部融资真相\n\n---\n\n看了一份联合国贸发会议的报告，讲的是发展中国家外部融资的现状，数据很扎实，分享几个关键点。\n\n1️⃣ 融资缺口巨大\n2024年，发展中国家从境外获得的资金约1.5万亿美元。但要实现可持续发展目标，每年还需要额外4.3万亿美元。内外融资都得再涨三分之一才能补上。\n\n2️⃣ 外部融资依赖度在下降\n2024年，发展中国家只有11%的资本形成来自外部融资，发达国家是38%。十年前这个数字更高，国内融资正在成为主角。\n\n3️⃣ 波动大，债务是主因\n外部资金流入非常不稳定，波动主要来自债券和贷款这类债务工具。股权类投资反而相对平稳。\n\n4️⃣ 还钱压力在加大\n2024年，发展中国家每收到100美元外部资金，就要还回去72美元。还债增速是股权回报增速的3倍。前沿市场国家（FMEs）的偿债成本最高。\n\n5️⃣ 利率高，期限短\n新发行债券的票面利率居高不下，贷款利息也在涨。而且债券期限在缩短，意味着再融资压力更大。发展中国家借钱的溢价一直没降下来。\n\n6️⃣ 政策建议\n报告提到，降低融资成本需要国家层面和市场层面的共同努\n\n[... middle omitted ...]\n\nright.com.\n\nAll other queries on rights and licences, including subsidiary rights, should be addressed to:\n\nUnited Nations Publications\n\n405 East 42nd Street\n\nNew York, New York 10017\n\nUnited \n\n[... middle omitted ...]\n\n7600.jpg)\n\nSource: UNCTAD calculations based on World Bank data.\nNote: Maturities are weighted by value of new commitments.\n\n![](images/a8a17eddf8e8be4ad6ba6db9e19b66087af1a236a218b802aa61b96224cbfd69.jpg)\n\n## unctad.org"
  },
  {
    "id": "R026",
    "title": "联合国贸发会议：从17万亿到27万亿美元，电商增长背后，环境账本敲响警钟",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "联合国贸发会议",
    "digest": "[wechat_article.md]\n# 联合国贸发会议：从17万亿到27万亿美元，电商增长背后，环境账本敲响警钟\n\n这份来自联合国贸发会议的最新报告，给出了一组值得所有产业决策者警惕的数字：全球43个主要经济体的电商销售额，从2016年的约17万亿美元飙升至2022年的近27万亿美元。增长背后，一个被高速增长掩盖的核心矛盾正在浮现——电商的便利性、低价和规模效应，正在以远超传统零售的速度消耗环境资源。报告的核心判断是：如果不对电商的物流、包装、退货和消费行为进行系统性干预，其环境成本将抵消甚至超过数字化带来的效率红利。\n\n这不是一份简单的环保倡议书。它从数据出发，拆解了B2C电商从仓库、配送、包装到退货的全链条环境影响，并与传统实体零售做了定量比较。更重要的是，报告提出了一个尖锐的追问：当电商平台占据全球约80%的交易额时，它们是否承担起了相应的环境责任？\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 电商的规模红利正在被物流与退货的“环境税”吞噬\n\n电商的快速增长带来了规模效应，但这份效用在环境维度上正在递减。报告指出，B2C电商的物流模式天然具有高环境成本：与B2B的大宗、集中配送不同，B2C需要将单个包裹分送到千家万户，这意味着更频繁的车辆出行、更分散的配送路线，以及更高的单位商品碳排放。\n\n更值得关注的是退货率。在线购物的退货率远高于实体店，部分品类甚至超过30%。每一件退货商品，不仅要经历逆向物流的运输和分拣，还常常因为包装损坏或轻微瑕疵而被直接丢弃。报告直言，高退货率意味着能源和材料的双重浪费，是当前电商环境账本中最大的“黑洞”。\n\n> **KC评论：** 很多人只看到电商减少了开车去商场的需求，却忽略了它催生了更分散、更频繁的配送网络。真正值得追问的是：当退货被“免费”承诺所鼓励时，消费者是否承担了这笔环境成本？完整报告中的图V.2和图V.3\n\n[... middle omitted ...]\n\n、并购、对冲基金、资管机构、战略咨询、智库等朋友，期待交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n网购的环保账，比你想的更复杂\n\n**网购环保账**\n\n**电商增长快，但环境代价也不小**\n\n最近读了一份关于电商与环保的研报，感觉信息量很大，分享给大家一起研究。\n\n1/ 电商规模增长惊人\n数据显示，43个国家的企业电商销售额从2016年的约17万亿美元增长到2022年的近27万亿美元。中国销售额从1.6万亿增长到4.5万亿，美国从7万亿增长到11万亿。全球约23亿人在2021年曾在线购物。\n\n2/ 环保影响是双刃剑\n- 积极面：在线购物可能比开车去实体店更节能，减少碳排放；数字产品（电影、音乐）实现了去物质化\n- 消极面：低价和便利刺激消费，导致更多生产和运输；高退货率造成商品被丢弃，浪费能源和材料\n\n3/ 最关键的三个环保痛点\n① 物流运输：从仓库到配送中心到最后一公里，碳排放和能源消耗巨大\n② 过度包装：大量一次性包装、纸箱和塑料填充物\n③ 高退货率：退回商品常被直接丢弃，资源浪费严重\n\n4/ 大平台责任重大\n研报指出，仅6家头部平台就占据了约80%的交易额。这些平台在推动环保方面应当发挥领导作用。\n\n5/ 政策建议值得关注\n- 禁止免费退货，减少不必要的退货行为\n- 立法规范过度包装，推广可重复使用\n\n[... middle omitted ...]\n\ne, and explores how it can be as sustainable as possible.\n\n## 27 trillion \\$\n\n17 trillion \\$\n\n## E-commerce sales\n\nby businesses in 43 developed and developing economies surged between 2016–20\n\n[... middle omitted ...]\n\nerce and digital companies should be fostered to drive investment in digital innovations that prioritize environmental and social sustainability, thereby advancing a more responsible and sustainable e-commerce ecosystem."
  },
  {
    "id": "R027",
    "title": "联合国贸发会议：小岛国灾害后增长损失被系统性低估",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "联合国贸发会议",
    "digest": "[wechat_article.md]\n# 联合国贸发会议：小岛国灾害后增长损失被系统性低估\n\n当全球气候谈判陷入大国博弈的泥潭，一个被长期忽视的经济学问题正在浮出水面：对于那些国土面积狭小、经济结构单一、高度依赖外部市场的小岛发展中国家（SIDS）来说，一场台风或一次洪水，究竟会如何改写它们未来三到五年的增长轨迹？\n\n联合国贸发会议（UNCTAD）最新发布的第12号工作论文，直接回应了这个看似具体、实则关乎全球气候融资与债务可持续性核心的问题。报告的标题本身就说明了一切——“脆弱的繁荣”。这份研究并非简单地重复“气候变化对穷国打击更大”的常识，而是首次通过严格的计量方法，系统论证了一个此前被数据噪音掩盖的事实：小岛国遭受气候灾害后的中期增长损失，系统性、显著地高于其他发展中国家。这不是一个关于短期冲击的故事，而是一个关于增长路径被永久性改变的故事。\n\n这篇研报的价值，不在于它给出了某个惊世骇俗的结论，而在于它用扎实的数据和模型，把“脆弱性”从一个抽象的政治口号，变成了一个可以被衡量、被定价、被纳入增长模型的经济变量。\n\n> **KC评论：**\n> 这份报告真正有意思的地方，不在于它证实了“灾害伤害增长”，而在于它量化了“伤害的差异”。对于关注新兴市场债务、主权信用评级、或气候债券定价的读者来说，这个“差异”可能就是关键的风险溢价因子。完整报告中的图表和回归系数，提供了可以直接用于情景分析的基准。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 为什么小岛国的“脆弱繁荣”是一个被低估的宏观风险\n\n报告的切入点是文献综述中一个长期存在的困惑：自然灾害对经济增长的影响，在理论上和实证上都没有定论。有的研究发现灾害后投资加速、技术更新，甚至出现“创造性破坏”的正向效应；另一些研究则发现系统性负向冲击。这种结论的混乱，很大程度上源于两个问题：一是灾害的度量方式不统一，二\n\n[... middle omitted ...]\n\ndge fund、资管机构、战略咨询、智库等朋友，期待交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n小岛国的增长，为何总被风暴打断？\n\n小岛国的增长困局\n\n气候灾害对经济的影响，小岛国比想象中更脆弱\n\n最近读到一份联合国贸发会议（UNCTAD）的工作论文，专门研究了小岛屿发展中国家（SIDS）在气候灾害下的经济增长表现。结论很直接：**SIDS 遭受的冲击，比其他发展中国家更严重、更持久。**\n\n1️⃣ **数据口径是关键**\n论文指出，过去很多研究结论不一致，部分原因在于对“灾害”的定义不同。只看灾害频率，可能忽略强度；只看经济损失，又受限于数据缺失（70% 的灾害事件没有经济损失记录）。作者采用了**频率 + 强度双指标**，更全面捕捉 SIDS 的真实风险。\n\n2️⃣ **SIDS 的“结构性脆弱”**\n使用系统 GMM 方法，控制常规增长因素后，SIDS 的灾害冲击系数显著为负。这意味着即使同等规模的灾害，SIDS 的 GDP 增长会比其他发展中国家多下滑好几个百分点。原因在于：经济结构单一、基础设施集中、债务压力大，恢复能力天生不足。\n\n3️⃣ **不同灾害，不同打击路径**\n- **风暴**：对服务业增长影响最大（旅游业直接停摆）\n- **洪水**：对工业增加值冲击更突出（工厂、供应链中断）\n-\n\n[... middle omitted ...]\n\nbilities of Small Island Developing States (SIDS). It underscores the importance of combining diverse disaster metrics to fully capture the risks faced by SIDS. Using system GMM estimation, th\n\n[... middle omitted ...]\n\nrd errors in parentheses  \n\\*\\*\\* p<0.01, \\*\\* p<0.05, \\* p<0.1\n\nPeriod fixed effects are included (coefficients not reported)\n\n@UNCTAD\n@UNCTAD\nunctad.org/facebook\nunctad.org/youtube\nunctad.org/flickr\nunctad.org/linkedin"
  },
  {
    "id": "R028",
    "title": "联合国贸发会议：联合国报告，AI或侵蚀发展中国家廉价劳动力优势",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "联合国贸发会议",
    "digest": "[wechat_article.md]\n# 联合国贸发会议：联合国报告，AI或侵蚀发展中国家廉价劳动力优势\n\n全球前沿技术市场正以惊人的速度膨胀。根据联合国贸发会议（UNCTAD）最新发布的《2025年技术与创新报告》，这一市场在2023年已达到2.5万亿美元的规模，并预计在未来十年内增长六倍，至2033年达到16.4万亿美元。其中，人工智能（AI）将成为绝对的王者，届时独占近三分之一的市场份额，达到约4.8万亿美元。\n\n这份报告的价值不在于重复“AI很重要”这个共识，而在于它揭示了繁荣背后一个日益尖锐的结构性矛盾：技术市场的增长红利，正在被极少数头部公司和国家高度集中。这不仅仅是商业竞争的问题，更可能重塑全球发展格局，让发展中国家陷入新的追赶困境。对于产业决策者和投资者而言，理解这种“赢家通吃”的动力机制，远比预测下一个AI应用风口更为关键。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 全球AI研发投入的“金字塔尖”：100家公司掌控四成江山\n\n报告的核心洞察之一，是研发投入的极端集中化。数据显示，全球企业研发投入中，超过80%由2500家公司贡献，而其中仅100家公司就占据了超过40%的份额。这意味着，决定AI未来走向的核心技术和算法，正被一个极其狭窄的“精英俱乐部”所掌握。\n\n从国别看，美国是当之无愧的霸主。在全球前100大企业研发投资者中，约一半总部位于美国，包括Alphabet、Meta、微软和苹果。中国紧随其后，占比约13%，以华为和腾讯为代表，在十年间从2%跃升至13%，超越了德国、日本等传统研发强国。但除此之外，前100名中几乎看不到其他发展中国家的身影。这清晰地描绘出一幅“双头垄断”的图景，而其他国家，尤其是全球南方国家，正在被边缘化。\n\n> **KC评论：** 这份数据揭示了一个残酷的现实：AI竞赛的本质是“资本竞赛”。对于大多数企业来说\n\n[... middle omitted ...]\n\n购、对冲基金、资管机构、战略咨询和智库的朋友，期待与您交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI前沿技术：市场6年翻6倍\n\nAI市场爆发前夜\n\n前沿技术市场预计2033年达16.4万亿美元，AI将占30%份额，成为最大单一市场。\n\n1/ 市场格局：高度集中\n全球仅100家公司贡献了40%+的企业研发投入。美国、中国主导知识产出——占全球1/3论文和2/3专利。其他发展中国家几乎缺席。\n\n2/ 巨头垄断：赢家通吃\n苹果、英伟达、微软市值均超3万亿美元。前5大都是美国公司。科技巨头正掌控技术方向，但商业动机≠公共利益——更倾向用AI替代人力而非增强人类能力。\n\n3/ 研发投资：两极分化\n2022年AI投资约2000亿美元，预计2030年达GDP的2%。但80%+的企业研发集中在2500家公司，发展中国家只有中国挤进前100研发投资者。\n\n4/ 关键杠杆点\nAI落地依赖三个核心：基础设施（算力+宽带）、数据、技能。发展中国家在这三方面都处于早期阶段，缺乏专门战略。\n\n一个值得思考的问题：当AI替代低成本劳动力优势，发展中国家的追赶窗口还在吗？\n\n#学习笔记\n\n[source_mineru.md]\nChapter I\n\nAI at the\ntechnology\nfrontier\n\nFrontier tech\n\n[... middle omitted ...]\n\nirds of patents. Similarly, there is a significant AI-related divide between developed and developing countries. This could widen existing inequalities and hinder efforts by developing countri\n\n[... middle omitted ...]\n\ntelligent Connectivity: AI, IoT, and 5G. Wiley.\n\nZewe A (2023). AI-driven tool makes it easy to personalize 3D-printable models. Available at https://news.mit.edu/2023/ai-driven-tool-personalize-3d-printable-models-0915."
  },
  {
    "id": "R029",
    "title": "联合国贸发会议：绿色转型不是市场能解决的，联合国贸发会议谈拉美产业政策",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "联合国贸发会议",
    "digest": "[wechat_article.md]\n# 联合国贸发会议：绿色转型不是市场能解决的，联合国贸发会议谈拉美产业政策\n\n这份来自联合国贸发会议的简报，没有把拉丁美洲的绿色潜力讲成一个乐观的故事。它提出了一个更尖锐的判断：如果拉美国家只是继续开采锂、铜、银，而不主动设计产业政策来推动经济多元化，那么绿色转型很可能复制过去资源依赖型经济的失败——增长昙花一现，财富分配不均，工业基础进一步萎缩。\n\n对于关注全球供应链重构、关键矿产博弈和新兴市场产业政策的读者来说，这份报告提供了一个非常及时的观察框架。它不只是在讲拉美，而是在讲一个更普遍的问题：当全球都在谈绿色转型时，资源富集国如何避免成为新一轮“绿色殖民地”？\n\n报告的核心主张是：拉美需要一套“主动的绿色产业政策”，而不仅仅是减排目标。这套政策的核心，不是降低营商成本，而是有意识地改变国家与企业的结构和行为。而实现这一目标，单靠任何一个国家都做不到，必须依靠区域整合和南南合作。\n\n> **KC评论：** 这份报告最值得关注的地方，不是它罗列了拉美有多少锂矿或可再生能源，而是它明确指出“市场无法以所需规模和速度内化环境成本”。这意味着，单纯依靠碳定价或绿色补贴，无法驱动结构性转型。真正需要的是国家主导的产业规划、融资和技术转移。报告后面附有详细的政策工具清单和区域合作案例，这些图表和假设路径才是完整报告的核心价值。继续看原文，真正有价值的是图表、假设和验证路径；完整报告与 KC评论 在每日汇编。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 拉美面临的双重危机：结构性脆弱叠加气候脆弱，工业能力正在提前流失\n\n报告开篇就点出了拉美当前最棘手的问题：经济增速放缓已经导致许多国家出现“失去的十年”，工业能力正在提前丧失。这种衰退不是周期性的，而是结构性的——经济多元化不足导致反复的繁荣-萧条循环。\n\n与此同时，气候变化的冲击\n\n[... middle omitted ...]\n\ndge fund、资管机构、战略咨询、智库等朋友，期待交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n拉美绿色转型：资源诅咒还是机遇？\n\n封面标题：拉美绿色转型\n封面副标题：资源诅咒还是新工业机遇？\n\n拉美手握全球过半锂矿、1/3铜矿，还有33%的可再生能源占比（全球平均只有13%）。但这份外资投行报告提醒：别只卖资源，得搞战略多元化。\n\n1. 资源陷阱要警惕\n过去拉美经济常陷“繁荣-萧条”循环，靠资源出口却难建完整产业链。现在绿色转型若只卖锂和铜，可能复制历史——资源依赖型经济，收益分配不均，环境成本还高。\n\n2. 两条腿走路：产业+区域\n报告建议：\n- 先选赛道：基于本国能力+全球技术趋势，挑出高优先级新产业（如低碳技术制造）。\n- 再出政策：工业、贸易、创新、教育、金融多管齐下，不是简单补贴，而是主动调整产业结构和企业行为。\n\n区域层面，拉美各国可互补——矿藏、制造经验、贸易路线，共同构建区域低碳工业生态系统。比如区域内容政策、研发支持、绿色技能培训。\n\n3. 钱和技术是硬约束\n全球每年需要1.7万亿美元可再生能源投资，但2022年拉美只拿到5440亿美元清洁能源外资。报告认为，开发银行有独特作用——能混合融资+公共政策。同时，南南合作（如中国-印尼镍案例）和全球技术转让是关键。\n\n4. 政治意愿与现有\n\n[... middle omitted ...]\n\ndiversification should be a central pillar of this approach. This entails first identifying sectors for diversification based on defined national development criteria and global markets and te\n\n[... middle omitted ...]\n\nity in providing the support needed for green industrial policies in developing countries to succeed.\n\nContact\nPress Office\n41 22 917 5828\nunctadpress@unctad.org\nunctad.org\nX\nInstagram\nf\nYouTube\nin\nUN\ntrade & development"
  },
  {
    "id": "R030",
    "title": "联合国贸发会议：贝宁经济韧性背后，中小企业出口附加值为何没跟上基础设施投资",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "联合国贸发会议",
    "digest": "[wechat_article.md]\n# 联合国贸发会议：贝宁经济韧性背后，中小企业出口附加值为何没跟上基础设施投资\n\n西非国家贝宁正站在一个关键的十字路口。过去十年，凭借港口升级和基础设施投资，这个国家成功将自己定位为区域物流枢纽，经济增长稳健，韧性超出预期。然而，联合国贸易和发展会议（UNCTAD）一份最新研报揭示了一个令人警醒的现实：宏观经济的亮眼表现，尚未转化为本土中小企业（PME）的产能升级和区域价值链深度参与。数据显示，贝宁对非洲市场的出口占比已从2008年的约40%骤降至2024年的约15%。这份报告的核心判断是：贝宁中小企业的真正机会，不在于继续做“过路经济”的搬运工，而在于抓住菠萝加工和钢铁下游制造两个具体赛道，实现从“物流型整合”向“生产型整合”的跃迁。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 贝宁的区域贸易失衡揭示了一个深层问题：出口附加值没有跟上基础设施投资\n\n报告首先勾勒了一个矛盾图景。贝宁经济在新冠疫情、地缘政治紧张和大宗商品价格波动中展现出显著韧性，2020年短暂放缓后迅速反弹，农业、农产品加工业、建筑业和服务业均表现强劲。科托努港的现代化扩建，以及连接萨赫勒内陆国家的运输走廊改善，进一步强化了贝宁作为区域中转和贸易平台的角色。\n\n但贸易数据暴露了结构性失衡。虽然总体贸易量自2010年代中期以来恢复，贝宁对非洲市场的出口份额却大幅萎缩，从2008年的约40%降至2024年的约15%。与此同时，从非洲伙伴的进口持续增长，反映出区域内对中间品和消费品的需求在扩大。这种“进口增、出口降”的剪刀差，意味着贝宁并未充分抓住西非经济共同体（CEDEAO）内部的市场机遇。\n\n> **KC评论：** 基础设施投资改善了“路”，但没有自动解决“货”的问题。贝宁的出口仍然高度集中在少数初级产品，尤其是棉花。2014-2016年间棉花价格暴跌和\n\n[... middle omitted ...]\n\ndge fund、资管机构、战略咨询、智库等朋友，期待交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n贝宁中小企业，如何切入区域产业链？\n\n中小企业如何切入区域产业链？\n\n西非小国贝宁，坐拥科托努港，是区域贸易的天然枢纽。但一份联合国贸发会议的最新研报指出：这个国家的经济“骨架”长好了，“肌肉”还没跟上——大量中小企业仍困在本地市场，缺乏进入区域产业链的能力。\n\n研报锁定两个极具潜力的突破口：菠萝（农产品加工）和钢铁（下游制造）。逻辑很清晰，值得研究参考。\n\n**1️⃣ 菠萝产业链：从卖果汁到卖“标准”**\n贝宁的“糖面包”菠萝品质很好，出口优势集中在低糖果汁（≤20°Brix），占出口收入96%以上。但问题很典型：\n- **上游卡脖子**：优质菠萝种苗（吸芽）严重短缺，影响种植面积和工厂原料稳定供应。\n- **下游被锁死**：包装罐几乎全靠进口，成本高、利润薄。\n\n**机会点**：中小企业可以切入两个“高门槛”环节：\n- **种苗生产**：做认证种苗供应商，不仅卖给本地农户，还能出口到周边国家（多哥、尼日尔等）。\n- **本地包装制造**：建一个易拉罐或纸箱厂，直接服务整个西非的果汁加工集群。研报认为，这是“最直接的升级路径”。\n\n**2️⃣ 钢铁产业链：不做炼钢，做“服务”**\n贝宁没有铁矿，但它是区域钢\n\n[... middle omitted ...]\n\nant au statut juridique des pays, territoires, villes ou zones, ou de leurs autorités, ni quant au tracé de leurs frontières ou limites.\n\nLa mention d'une entreprise ou d'un procédé breveté n'\n\n[... middle omitted ...]\n\négration des PME béninoises dans les chaînes de valeur régionales : Opportunités sectorielles et leviers d'action\n\nand opportunities. Bioresource Technology, 247, 1047-1058. https://doi.org/10.1016/j.biortech.2017.09.020"
  },
  {
    "id": "R031",
    "title": "联合国贸发会议：非洲残疾与贫困循环，数据揭示被低估的结构性挑战",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "联合国贸发会议",
    "digest": "[wechat_article.md]\n# 联合国贸发会议：非洲残疾与贫困循环，数据揭示被低估的结构性挑战\n\n全球极端贫困的下降趋势在过去十年明显放缓。新冠疫情只是部分解释，更深层的原因在于，极端贫困正日益集中在脆弱、受冲突影响的国家，以及那些最容易被政策忽视的群体身上。联合国贸发会议（UNCTAD）最新发布的工作论文，将镜头对准了非洲大陆，聚焦于一个长期被数据盲区覆盖的交叉议题：残疾与贫困之间的双向强化关系。\n\n这份基于27个非洲国家、覆盖该大陆57%人口的全国代表性调查数据的研究，给出了一个核心判断：残疾在非洲并非边缘现象，而是与性别、城乡、年龄结构深度绑定，并且与贫困之间存在稳健的、即使控制社会人口特征后依然显著的正相关关系。这并非一个单纯的福利议题，而是关乎非洲未来人力资本积累、劳动力市场效率以及减贫政策有效性的关键变量。\n\n对于关注全球发展、新兴市场投资以及长期结构性风险的读者而言，这份报告的价值不在于揭示“残疾导致贫困”这一常识，而在于提供了迄今为止最全面的量化证据，揭示了这一关联在不同维度上的具体强度、分布特征，以及现有政策框架的盲区。\n\n> **KC评论：** 许多宏观叙事关注非洲的人口红利和经济增长潜力，但这份报告提醒我们，增长的质量和包容性同样重要。如果减贫进程无法有效覆盖残疾人群体，那么非洲的“人口红利”可能部分被“残疾负担”所抵消。这份报告的价值在于，它用数据把“包容性增长”这个抽象概念，变成了可衡量、可追踪、可比较的国别指标。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 残疾在非洲并非随机分布，而是性别、地域与年龄的结构性投射\n\n报告首先通过描述性统计，描绘了非洲残疾人口的基本画像。研究发现，残疾在女性、农村居民和年长成年人中更为普遍。具体数据如下：女性残疾患病率为3.6%，男性为2.3%；农村地区为3.4%，城市地区为2.6%；3\n\n[... middle omitted ...]\n\ndge fund、资管机构、战略咨询、智库等朋友，期待交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n非洲27国数据：残疾与贫困的强关联\n\n非洲27国研究揭示\n\n最近读了一份联合国贸发会议的工作论文，关于非洲残疾与贫困的关系，数据很扎实。\n\n这篇研究覆盖了非洲27个国家，样本占非洲总人口的57%，用的是国际通用的华盛顿组短问卷，数据质量有保障。\n\n核心发现：\n\n1⃣ 残疾率差异明显\n- 女性残疾率3.6%，男性2.3%\n- 农村地区3.4%，城市2.6%\n- 34-49岁人群4.4%，18-33岁仅2.3%\n\n2⃣ 残疾与贫困高度关联\n在大多数国家，即使控制年龄、性别、城乡等变量，残疾人群的资产贫困和多维贫困风险依然显著更高。\n\n3⃣ 贫困的双重维度\n研究用了两种贫困度量：资产贫困（看家庭拥有什么）和多维贫困（看教育、健康、生活条件）。残疾人群在这两方面都更脆弱。\n\n4⃣ 非洲的贫困挑战\n撒哈拉以南非洲贫困率超37%，2024年贫困人口达4.64亿。如果趋势不变，2030年仍将有5.75亿人生活在极端贫困中。\n\n研究提醒我们，减贫策略必须系统性纳入残疾包容视角，不能只泛泛谈“消除贫困”。\n\n#学习笔记\n\n[source_mineru.md]\n| Working paper\n\n#11\n\nNovember 202\n\n[... middle omitted ...]\n\naphic patterns, and the association between disability and poverty at both national and regional levels. Results show that disability is more common among women, rural residents, and older adu\n\n[... middle omitted ...]\n\nphic-social/sconcerns/disability/statistics.\n\n![](images/432ab7c150a7f542bb785ef63ce592d0fd0730472a31c22f6b936fcaa169aae2.jpg)\n\n@UNCTAD\n@UNCTAD\nunctad.org/facebook\nunctad.org/youtube\nunctad.org/flickr\nunctad.org/linkedin"
  },
  {
    "id": "R032",
    "title": "联合国贸发会议：AI竞赛中，中国和印度不是追赶者，而是结构性例外者",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "联合国贸发会议",
    "digest": "[wechat_article.md]\n# 联合国贸发会议：AI竞赛中，中国和印度不是追赶者，而是结构性例外者\n\n全球经济的价值重心正在从廉价劳动力和实物资产，转向知识密集型服务和无形资产。这一转变在人工智能领域表现得尤为剧烈。联合国贸发会议（UNCTAD）在最新发布的第120号政策简报中，提出了一个与市场主流叙事存在微妙差别的判断：发展中国家在AI浪潮中并非注定落后，部分国家已经展现出超越其收入水平的结构性潜力。报告明确指出，巴西、中国、印度和菲律宾是“在技术准备度上表现超出预期的国家”。\n\n这份报告的核心主张并非简单的“发展中国家要追赶AI”，而是给出了一个更具操作性的框架：国家AI战略必须同时回答“如何采用”与“如何发展”两个问题，并且需要根据自身在基础设施、数据、技能这三个杠杆点上的具体短板，设计差异化的追赶路径。那些试图复制发达国家路径的国家，可能反而会陷入更深的被动。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 技术准备度的“超预期者”揭示了一个反常识：人口规模可以成为AI战略的独立变量\n\nUNCTAD构建的前沿技术准备度指数，将国家表现与人均GDP进行相关性分析。绝大多数国家落在正相关趋势线附近，但少数国家的表现显著高于其收入水平所对应的预期值。报告特别点名了巴西、中国、印度和菲律宾。\n\n这组名单背后的共同特征是更强的研发活动和工业能力。但真正值得推敲的，是人口规模在其中的作用机制。报告在分析AI技能准备度时，使用了两个代理指标：拥有高等学历的劳动年龄人口占比，以及GitHub开发者占劳动年龄人口的比例。在开发者占比这一指标上，发达国家整体领先，但报告给出了一个重要的修正性判断：中国和印度的开发者占比虽然不高，却拥有全球第二和第三大的开发者社区。\n\n> **KC评论：** 这意味着，对于人口大国而言，“绝对人才池”可能比“人均技能密度”更具战略\n\n[... middle omitted ...]\n\ndge fund、资管机构、战略咨询、智库等朋友，期待交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n发展中国家如何抓住AI机会？一份实用框架\n\n🌍 全球价值正在向知识密集型活动转移\n\n最近读了UNCTAD的政策简报，发现一个关键判断：AI时代，发展中国家如果不及时制定战略，可能会被甩得更远。\n\n1️⃣ 先看现状\n- 发达国家的AI政策数量遥遥领先，到2023年底约2/3已出台国家AI政策\n- 全球89项国家AI政策中，只有6项来自最不发达国家\n- 好消息是：巴西、中国、印度、菲律宾在技术准备度上表现超出收入水平预期\n\n2️⃣ 核心框架：三个关键支点\nUNCTAD提出了一个清晰的评估框架，判断一个国家AI准备度要看三个维度：\n\n📍基础设施：从基础电力、ICT设备，到数据中心、高速网络\n📍数据：从领域数据获取，到大规模、高质量、可互操作的数据集\n📍技能：从基础数字素养，到数据科学、机器学习等高级能力\n\n三个要素要协同发展，才能催化AI扩散。\n\n3️⃣ 国家分类：你在哪个位置？\n报告把国家分为四类：落后者、实践者、领导者等\n重要的是找到适合自己的追赶路径，而不是照搬别人模式\n\n4️⃣ 政策建议\n- 评估自身在基础设施、数据、技能方面的差距\n- 加强创新生态系统\n- 跨部门协调行动，政策要超越税收激励\n- 优先升级\n\n[... middle omitted ...]\n\nable development, developing countries risk falling behind\n\n\\- Successful national artificial intelligence policies combine high-level direction with concrete actions across key sectors; drawi\n\n[... middle omitted ...]\n\nrg\n\nAngel Gonzalez Sanz\nOfficer-In-Charge, Division on Technology and Logistics, UNCTAD\n41 22 917 5508\nAngel.Gonzalez-Sanz@unctad.org\n\nPress Office\n41 22 917 5828\nunctadpress@unctad.org\nunctad.org\n\nUN trade & development"
  },
  {
    "id": "R033",
    "title": "联合国贸发会议：不是关税，基础设施和政策不确定性才是巴新企业真正瓶颈",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "联合国贸发会议",
    "digest": "[wechat_article.md]\n# 联合国贸发会议：不是关税，基础设施和政策不确定性才是巴新企业真正瓶颈\n\n巴布亚新几内亚过去二十年经历了一场罕见的贸易政策实验：从主动削减关税到突然转向保护主义，再到如今站在十字路口。联合国贸发会议一份最新技术合作报告，系统评估了这一“关税削减计划”的得失。报告的结论清晰且反直觉：关税削减并未引发进口激增，也未造成财政收入塌陷；真正拖累竞争力的，是基础设施、物流成本和政策不确定性，而非进口竞争。\n\n这份报告的价值不仅在于评估巴新的贸易政策，更在于它为所有面临“开放还是保护”抉择的发展中经济体，提供了一组基于证据的决策参考。当全球贸易体系面临碎片化压力，当产业政策重新成为主流叙事，巴新案例提醒我们：关税工具的实际效果，往往与政策制定者的直觉相去甚远。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 关税削减的十年，巴新并未经历“进口冲击”\n\n报告将评估分为两个阶段：2012至2017年的关税削减期，以及2018至2023年的关税回调期。在削减阶段，巴新将平均最惠国关税降至约3.2%，成为区域内最开放的经济体之一。按照传统贸易理论的预期，大幅降低关税应当刺激进口增长，对国内产业形成竞争压力。\n\n但实际数据并未支持这一假设。报告指出，关税削减期恰逢巴新进口需求整体偏弱，因此并未出现所谓的“进口激增”。当巴新在2018年后提高部分产品关税时，进口水平已经处于低位且稳定，关税上调对进口的额外抑制效应十分有限。这意味着，决定巴新进口规模的主要因素并非关税，而是国内需求基本面、大宗商品周期以及大型资源项目的开发节奏。\n\n> **KC评论：** 这组数据打破了“降关税=进口暴增”的简单叙事。对于政策制定者而言，真正的风险不在于关税水平本身，而在于关税政策的频繁变动所制造的商业不确定性。报告调查显示，61%的受访企业认为2018至2020\n\n[... middle omitted ...]\n\n、并购、对冲基金、资管机构、战略咨询、智库等朋友，期待交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n巴新关税改革，十年复盘\n\n关税改革十年，效果如何？\n\n巴布亚新几内亚的关税减让计划（TRP）在2018年暂停了。这份来自某国际组织的研报，正好帮我们复盘了这段经历。\n\n1/ 核心变化：从开放到保护\n- TRP期间（2012-2017），平均关税降到约3.2%，是区域最开放的经济体之一\n- 2018年后，为了保护本土产业和增加收入，关税开始回升\n- 这种政策波动让企业很困惑：61%的受访企业说，2018-2020年的关税调整影响了它们的投资决策\n\n2/ 经济表现：开放期更优\n- TRP期间GDP年均增长6.3%，暂停后降到2%\n- 但要注意：开放期赶上全球大宗商品牛市，暂停期撞上疫情，不能简单归因于关税政策\n- 关税每提高1%，进口额平均减少约2.1%（引力模型测算）\n\n3/ 关税收入：不是主要来源\n- 关税收入从2010年的7150万美元涨到2023年的1.12亿美元\n- 但占总税收比例在下降，因为销售税等其他税种更突出了\n- 烟草关税大幅下调后，反而让关税收入减少了约1560万美元\n\n4/ 对消费者的影响\n- TRP期间，消费品关税从6.4%降到5.2%，进口消费品占比稳步增长\n- 暂停后，消费品关税回升到\n\n[... middle omitted ...]\n\ning the legal status of any country, territory, city or area or of its authorities, or concerning the delimitation of its frontiers or boundaries.\n\nMention of any firm or licensed process does\n\n[... middle omitted ...]\n\nies 0.48\n940600 Buildings; prefabricated 0.14\n950691 Athletics and gymnastics equipment 0.16\n\nNote: Reported export lines where the value of exports was above \\$100,000 in 2018; Source: UNCTAD based on data from COMTRADE"
  },
  {
    "id": "R034",
    "title": "联合国贸发会议：从非洲悖论看全球供应链，贸易红利如何才能真正落地？",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "联合国贸发会议",
    "digest": "[wechat_article.md]\n# 联合国贸发会议：从非洲悖论看全球供应链，贸易红利如何才能真正落地？\n\n全球化的批评者与拥护者之间，长期存在一个核心争论：开放贸易究竟能否帮助最贫困的人口摆脱贫困？对于许多发展中国家，尤其是非洲国家，答案远非“是”或“否”那么简单。联合国贸发会议（UNCTAD）最新发布的工作论文《Revisiting the Trade-Poverty Nexus in Developing Countries》，利用前沿的计量方法，给出了一个严谨但令人不安的答案：贸易是减贫的必要条件，但绝非充分条件。这份报告的核心发现是，更高的贸易依存度在统计学上显著降低了发展中国家的贫困率，但在非洲，这一效应却消失了。更值得警惕的是，单纯的关税削减，无论在全球南方还是非洲，都没有系统性地影响贫困水平。这意味着，过去二十年被视为“标准药方”的贸易自由化，其减贫效果高度依赖于被长期忽视的国内结构性条件。\n\n这不仅仅是一份学术论文。对于关注全球供应链布局、新兴市场消费潜力以及地缘经济格局的决策者而言，它提供了一个重新评估“开放红利”的框架。当贸易的潮水无法自动托起所有船只时，哪些国家正在构建能让“涓滴效应”生效的制度与产业基础？哪些国家则可能陷入“开放式贫困陷阱”？本文将梳理报告的核心逻辑，并探讨那些尚未被完全回答的关键问题。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 贸易总量与贫困的脱钩：非洲的统计显著性消失\n\n报告首先通过面板数据和后双选择（PDS）Lasso估计方法，试图解决以往研究中因变量遗漏导致的偏误。结论非常清晰：对于整个发展中国家样本，以贸易占GDP比重衡量的贸易开放度，与贫困率呈显著的负相关。然而，当样本聚焦于非洲国家时，这一统计显著性完全消失。报告原文指出，贸易开放度对非洲贫困“没有统计上显著的影响”。\n\n这意味着什么？简单来说，\n\n[... middle omitted ...]\n\n咨询和智库的朋友，期待与您共同探讨贸易、贫困与增长的真问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n贸易减贫，为什么非洲效果不佳？\n\n贸易≠自动减贫\n\n最近读到UNCTAD一份研报，关于贸易与贫困的关系，结论很清晰：贸易开放能减贫，但不是万能药。\n\n1/ 贸易依赖度（贸易/GDP）越高，发展中国家贫困率越低。但这一规律在非洲失灵——非洲的贸易开放与贫困之间没有统计上的显著关系。\n\n2/ 关税改革（降低关税）对减贫没有系统性影响。无论是发展中国家整体，还是非洲单独看，关税变化与贫困率之间都没有稳定关联。\n\n3/ 关键变量来了：贸易是减贫的必要条件，但不是充分条件。国家特征（金融深度、教育水平、制度质量、人口结构等）决定了贸易能否真正惠及穷人。\n\n4/ 研报用了一种叫“PDS lasso”的计量方法，避免传统研究中的遗漏变量偏差。结论更可靠。\n\n5/ 具体到非洲，贸易开放与贫困的关系取决于：预期寿命、气候变化脆弱性、矿产资源依赖、政府效能、城市化水平、私人信贷可得性、工资劳动者占比、收入不平等、人口增长等。\n\n6/ 简单说：光开放市场不够，配套条件要跟上。基础设施、教育、金融包容、制度质量，这些“土壤”决定了贸易这颗“种子”能否生根发芽。\n\n贸易是工具，不是终点。怎样让贸易真正服务于减贫，需要更精细的政策设计。\n\n[... middle omitted ...]\n\nn developing countries but has no statistically significant effect on poverty in Africa. It also finds that trade reforms (as measured by changes in tariffs) have no systematic effect on pover\n\n[... middle omitted ...]\n\nned controls are available from the authors.\n\n![](images/f0f4b634c1894c85548ab32cd25ce9a22a81fb346bc764127a1a4da5fd45a944.jpg)\n\n@UNCTAD\n@UNCTAD\nunctad.org/facebook\nunctad.org/youtube\nunctad.org/flickr\nunctad.org/linkedin"
  },
  {
    "id": "R035",
    "title": "联合国贸发会议：发展中国家面临AI研发重构，不是追赶权而是参与权问题",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "联合国贸发会议",
    "digest": "[wechat_article.md]\n# 联合国贸发会议：发展中国家面临AI研发重构，不是追赶权而是参与权问题\n\n一份来自联合国贸发会议的深度技术报告，揭示了一个正在发生的结构性变化：AI不再只是研发的工具箱，而是正在重塑研发本身的运行逻辑。如果只看算力竞赛或大模型参数，可能错过了更本质的变量——AI正在让“发现、实验、开发、部署”这四个传统上按顺序推进的环节，变成一个可以实时反馈、自我加速的闭环系统。\n\n这份报告的核心判断是：AI对研发的渗透，正在从“提效”走向“重构”。它带来的不是单点效率提升，而是研发范式的整体迁移。对于企业、科研机构和国家创新体系而言，真正的挑战不是要不要用AI，而是能否建立适应“闭环加速”新型研发模式的组织能力和政策框架。\n\n> **KC评论：**\n> 这份报告的价值不在于告诉你AI多重要——那已经是共识。它真正值得读的是：AI通过哪四个具体渠道改变研发？每个渠道如何影响研发的不同阶段？这些机制对发展中国家意味着什么？完整报告中包含了详细的机制拆解图和行业案例，这些是判断自己所在行业是否会被“重构”的关键分析框架。\n>\n> 继续看原文，真正有价值的是图表、假设和验证路径；完整报告与KC评论在每日汇编。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 这轮变化真正考验的是企业能否把规模转化为议价权\n\n报告开篇就指出，AI已经确立为“通用目的技术”，具备三个关键特征：普遍性、动态性和创新互补性。这意味着AI不是某个垂直领域的专用工具，而是可以渗透到几乎所有经济活动中，并且能够持续自我改进，同时催生大量互补性创新。\n\n对于研发而言，这意味着什么？报告给出了一个清晰的框架：AI通过四个渠道影响研发——数据采集与整理、数据分析、假设生成、实验与模拟。这四个渠道覆盖了从“提出问题”到“验证答案”的全过程。\n\n关键洞察在于：AI不是简单地把每个环节\n\n[... middle omitted ...]\n\ndge fund、资管机构、战略咨询、智库等朋友，期待交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI正在重塑科研的底层逻辑\n\n科研范式正在被改写\n\n最近联合国贸发会议出了一份关于AI时代科技创新的报告，核心观点很清晰：AI已经不只是工具，它正在变成重塑研发流程的基础技术。\n\n1/ 加速研发的四个通道\nAI不是只帮科学家跑数据，而是从数据采集、数据分析、假设生成到实验模拟，全面介入研发流程。比如AlphaFold2预测了2亿种蛋白质结构，直接拿了诺贝尔化学奖。\n\n2/ 让研发从线性变循环\n传统研发是“想法→研究→开发→落地”的线性流程。AI让这个流程变成闭环——落地后的用户数据能直接反馈回早期研究阶段，形成持续优化的正循环。\n\n3/ 政策也要跟上节奏\n报告特别提醒：发展中国家要抓住这波机会，需要重新设计创新政策。不能只盯着AI应用，更要关注开放科学、全球合作、伦理框架这些基础设施。\n\n4/ 最值得关注的趋势\nAI在生物科学、材料科学、气候建模等领域已经展现出惊人的加速能力。未来5年，哪些国家能建好AI驱动的研发体系，哪些就可能在下一轮科技竞赛中领先。\n\n欢迎一起讨论AI对科研生态的深层影响。\n\n#学习笔记\n\n[source_mineru.md]\n## UNITED NATIONS CONFERENCE O\n\n[... middle omitted ...]\n\ne Center at copyright.com.\n\nAll other queries on rights and licences, including subsidiary rights, should be addressed to:\n\nUnited Nations Publications\n\n405 East 42nd Street\n\nNew York, New Yor\n\n[... middle omitted ...]\n\ns a QR code. It does not contain any text, mathematical formulas, tables, or figures that can be processed according to the OCR instructions. Therefore, no textual content can be extracted from this image.\n\n## unctad.org"
  },
  {
    "id": "R036",
    "title": "联合国贸发会议：联合国报告，全球经济增长反而加深资源依赖国困境",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "联合国贸发会议",
    "digest": "[wechat_article.md]\n# 联合国贸发会议：联合国报告，全球经济增长反而加深资源依赖国困境\n\n全球101个经济体仍深陷大宗商品依赖陷阱——出口收入的60%以上来自初级产品。过去二十年，许多国家尝试通过出口多元化来降低这种依赖，但结果往往令人失望：出口种类增加了，大宗商品出口占比却没有下降，甚至反而上升。\n\n联合国贸发会议（UNCTAD）2026年3月发布的工作论文《战略多元化：利用经济复杂性摆脱大宗商品依赖的实证洞见》给出了一个关键判断：问题不在于出口了多少种产品，而在于出口了什么样的产品。传统多元化指标关注的是出口篮子的大小，而真正决定一个国家能否摆脱资源诅咒的，是其出口产品的技术复杂度和生产能力的精密度。\n\n这份基于183个国家、1995年至2019年面板数据的研究，首次从理论上构建了经济复杂性与大宗商品依赖之间的因果框架，并量化了二者关系的异质性。结论清晰：向高复杂度部门多元化，能显著降低大宗商品依赖；但全球平均收入增长反而会加深依赖国的资源出口结构，强化发展中国家出口原材料、发达国家出口高附加值产品的全球分工格局。\n\n---\n\n> **KC评论：** 这篇报告的价值不在于重复“资源诅咒”的老生常谈，而在于提供了一个可操作的政策诊断工具——不是告诉你要多元化，而是告诉你应该往哪个方向多元化。完整报告中的图表和计量模型，展示了不同依赖程度国家的差异化路径，以及如何利用单位价格分层的贸易数据来精确定位产业目标。继续看原文，真正有价值的是图表、假设和验证路径；完整报告与KC评论在每日汇编。\n\n---\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 出口多元化不等于摆脱资源依赖，真正的变量是“经济复杂性”\n\n传统上，政策制定者将出口多元化视为降低大宗商品依赖的直接手段——增加出口产品种类，分散收入来源。但这份报告揭示了一个反直觉的事实：多元化本身并\n\n[... middle omitted ...]\n\n、资管机构、战略咨询、智库等机构的朋友，期待交流。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n出口多元化≠去依赖，复杂才是关键\n\n复杂才是真解药\n\n别光想着出口更多品类\n\n⸻\n\n**1. 为什么出口多了，依赖还在？**\n\n传统思路：只要出口的产品种类变多，就能降低对大宗商品的依赖。\n\n但这份UNCTAD研报用183国25年数据告诉我们：**不一定**。\n\n比如，从出口棉花变成“棉花+竹子”，还是没跳出大宗商品圈。甚至可能因为大宗商品卖得更多，依赖度反而上升。\n\n⸻\n\n**2. 真正的解药：经济复杂度**\n\n研报的核心概念——**经济复杂度**，不是看出口了多少种产品，而是看这些产品有多“难做”。\n\n- 复杂度高：需要多种高技能、高技术才能生产（比如芯片、精密仪器）\n- 复杂度低：谁都能搞（比如原油、矿石）\n\n结论很直接：**往高复杂度方向多元化，才能有效降低大宗商品依赖。** 尤其对依赖度在60%-80%的国家，效果最明显。\n\n⸻\n\n**3. 一个反常识的发现**\n\n全球平均收入增长，反而会**加深**大宗商品出口国的依赖。\n\n说明现有的全球分工体系，把发展中国家锁在了“卖原料”的角色里。光靠市场自然演化，很难跳出来。\n\n⸻\n\n**4. 对政策制定者的启发**\n\n- 复杂度是个“诊断工具”，帮你找到可\n\n[... middle omitted ...]\n\nirical relationship with commodity dependence may be more complex than traditionally understood. Using data from 183 countries between 1995 and 2019, this paper explores how economic complexit\n\n[... middle omitted ...]\n\na749f0c8358d5372a0017318de52efd485424e7.jpg)\n\n@UNCTAD\n@UNCTAD\nunctad.org/facebook\nunctad.org/youtube\nunctad.org/flickr\nunctad.org/linkedin\n\n![](images/97d62bbd847723cab001cd2b052b9ee7f5b164e34ee9d1b476d35e770180e911.jpg)"
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "亚洲开发银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "亚洲开发银行｜亚洲开发银行：亚洲开发银行撬动60亿美元私人资本，2025年操作答卷解读｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F002",
    "report_id": "R002",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Mechanism Analysis of Corporate Digital Transformation and Environmental Performance Our paper makes several contributions to the growing literature on the impact of digitalization on sustainability. Previous studies h"
  },
  {
    "figure_id": "F003",
    "report_id": "R002",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Structured Keyword Dictionary of Corporate Digital Transformation Notes: This figure illustrates the sub-dimensions associated with corporate digital transformation and their corresponding common keywords. We classify"
  },
  {
    "figure_id": "F004",
    "report_id": "R002",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Average Overall Digital Transformation Levels Across Sectors Notes: This figure illustrates the yearly average overall digital transformation levels (LnDT) across sectors from 2000 to 2023. The construction of these me"
  },
  {
    "figure_id": "F005",
    "report_id": "R002",
    "label": "亚洲开发银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "亚洲开发银行｜亚洲开发银行：中国A股数据揭示，制造端数字化对环保拉动效果最显著｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F006",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Mongolian Domestic Carbon Market Management Structure AFOLU = agriculture, forestry, and other land use; IPPU = industrial processes and product use. ## 2.7. Pakistan Pakistan's engagement with carbon market mechanisms"
  },
  {
    "figure_id": "F007",
    "report_id": "R003",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Carbon Tax per Country, 1 April 2025 $tCO_{2}$ = tons of carbon dioxide, UK = United Kingdom. Note: Orange refers to carbon tax not levied on transport fuels; blue refers to carbon tax levied on transport fuels plus (w"
  },
  {
    "figure_id": "F008",
    "report_id": "R003",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Gasoline Explicit Subsidy or Tax in CAREC Countries, 2024 CAREC = Central Asia Regional Economic Cooperation, PRC = People's Republic of China. Note: “Explicit subsidy” is the consumer price minus fuel cost; “tax” is t"
  },
  {
    "figure_id": "F009",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Diesel Explicit Subsidy or Tax in CAREC Countries, 2024 CAREC = Central Asia Regional Economic Cooperation, PRC = People's Republic of China. Note: “Explicit subsidy” is the consumer price minus fuel cost; “tax” is the"
  },
  {
    "figure_id": "F010",
    "report_id": "R003",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5: Emissions Trading Systems Compliance Price per Country/Region, 1 April 2025 CaT = cap-and-trade, PRC = People's Republic of China, ETS = emissions trading system, EU = European Union, OBPS = output-based pricing system"
  },
  {
    "figure_id": "F011",
    "report_id": "R003",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 6: Tesla's Regulatory Credits Revenue FY = fiscal year (ending 31 December). While absolute revenue figures have grown for Tesla, the share of revenues generated by credits dropped over time from around 10% in 2012 to aro"
  },
  {
    "figure_id": "F012",
    "report_id": "R003",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 7: Tesla's Regulatory Credits to Total Revenue Ratio FY = fiscal year (ending 31 December). Figure 8: Tesla's Regulatory Credits per Car FY = fiscal year (ending 31 December)."
  },
  {
    "figure_id": "F013",
    "report_id": "R003",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 7: Tesla's Regulatory Credits to Total Revenue Ratio FY = fiscal year (ending 31 December). Figure 8: Tesla's Regulatory Credits per Car FY = fiscal year (ending 31 December). ## 5.3. Opportunities in CAREC Countries Wi"
  },
  {
    "figure_id": "F014",
    "report_id": "R003",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "• domestic carbon credit markets (voluntary and compliance), • voluntary international carbon markets, and • international compliance markets under bilateral or multilateral schemes. Procedures for all carbon markets are very similar, involving a methodology t"
  },
  {
    "figure_id": "F015",
    "report_id": "R003",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "Figure 10: Volumes and Prices of Voluntary Carbon Markets, 2020–2024 $\\mathrm{MtCO}_{2}\\mathrm{e} =$ million tons of carbon dioxide equivalent, RHS $=$ right-hand side. Multiple carbon market standards exist, the most used by far"
  },
  {
    "figure_id": "F016",
    "report_id": "R003",
    "label": "亚洲开发银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "亚洲开发银行｜亚洲开发银行：碳定价在交通领域真正机会，不是征税，而是循环投资｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F017",
    "report_id": "R004",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Growth Rate of Trade in Goods Settled in RMB (Year-on-Year) and its Relationship with the USD/RMB Exchange Rate"
  },
  {
    "figure_id": "F018",
    "report_id": "R004",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Growth Rate of Trade in Goods Settled in RMB (Year-on-Year) and its Relationship with the USD/RMB Exchange Rate Figure 3: RMB Settlement for Receipt and Payment in the Current Account Furthermore, as shown in Figure"
  },
  {
    "figure_id": "F019",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Share of RMB in Cross-Border Receipts and Payments Under Current Transactions (RMB + Foreign Currencies)"
  },
  {
    "figure_id": "F020",
    "report_id": "R004",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 5: Overseas Transaction Data via Banks on Behalf of Clients (Share of Foreign Currency and RMB)"
  },
  {
    "figure_id": "F021",
    "report_id": "R004",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 6: External Receipts and Payments Balance Data via Banks on Behalf of Clients (Combined Current and Capital Account, by Currency)"
  },
  {
    "figure_id": "F022",
    "report_id": "R004",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 6: External Receipts and Payments Balance Data via Banks on Behalf of Clients (Combined Current and Capital Account, by Currency) In regard to the increase in the PRC's transactions settled in RMB, when examining the shar"
  },
  {
    "figure_id": "F023",
    "report_id": "R004",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 7: Cross-Border Renminbi Receipts and Payments by Economy/Region (Share)"
  },
  {
    "figure_id": "F024",
    "report_id": "R004",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure 9: Holdings of Renminbi Assets by Nonresident Entities In the PRC's foreign exchange market spot transactions, the US dollar continues to account for over 95% of all RMB trading (exchange) counterpart currencies. Even as"
  },
  {
    "figure_id": "F025",
    "report_id": "R004",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 11: Thailand's Import Value Share by Origin (2011–2024)"
  },
  {
    "figure_id": "F026",
    "report_id": "R004",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 11: Thailand's Import Value Share by Origin (2011–2024) Figure 12: Thailand's Export Receipt Share Figure 13: Thailand's Export Receipt by Currency (1993–2024) (Type of Management)"
  },
  {
    "figure_id": "F027",
    "report_id": "R004",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "Figure 11: Thailand's Import Value Share by Origin (2011–2024) Figure 12: Thailand's Export Receipt Share Figure 13: Thailand's Export Receipt by Currency (1993–2024) (Type of Management) Looking at trends in currencies in Th"
  },
  {
    "figure_id": "F028",
    "report_id": "R004",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "Figure 12: Thailand's Export Receipt Share Figure 13: Thailand's Export Receipt by Currency (1993–2024) (Type of Management) Looking at trends in currencies in Thailand's export receipts, as published by the Bank of Thailand $^"
  },
  {
    "figure_id": "F029",
    "report_id": "R004",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "Figure 14: Thailand's Import Payment Share Figure 15: Thailand's Import Payment by Currency (1993–2024) (Type of Management) Furthermore, as regards the financing of import payments, the proportion of payments made using foreig"
  },
  {
    "figure_id": "F030",
    "report_id": "R004",
    "label": "Figure 14",
    "figure_type": "source_exhibit",
    "context": "Figure 16: Thailand's Trade with ASEAN 9 Economies: Share by Invoice Currency"
  },
  {
    "figure_id": "F031",
    "report_id": "R004",
    "label": "Figure 15",
    "figure_type": "source_exhibit",
    "context": "Figure 17: Thailand's Trade with Malaysia: Share by Invoice Currency"
  },
  {
    "figure_id": "F032",
    "report_id": "R004",
    "label": "Figure 15",
    "figure_type": "source_exhibit",
    "context": "Figure 17: Thailand's Trade with Malaysia: Share by Invoice Currency"
  },
  {
    "figure_id": "F033",
    "report_id": "R004",
    "label": "Figure 17",
    "figure_type": "source_exhibit",
    "context": "Figure 17: Thailand's Trade with Malaysia: Share by Invoice Currency Next, looking at bilateral trade between Thailand and Indonesia (Figure 18), baht-invoiced exports have been on an upward trend (except in 2020), while baht-i"
  },
  {
    "figure_id": "F034",
    "report_id": "R004",
    "label": "Figure 17",
    "figure_type": "source_exhibit",
    "context": "Figure 18: Thailand's Trade with Indonesia: Share by Invoice Currency"
  },
  {
    "figure_id": "F035",
    "report_id": "R004",
    "label": "Figure 18",
    "figure_type": "source_exhibit",
    "context": "Figure 18: Thailand's Trade with Indonesia: Share by Invoice Currency Figure 19: Thailand's Trade with Viet Nam: Share by Invoice Currency"
  },
  {
    "figure_id": "F036",
    "report_id": "R004",
    "label": "Figure 18",
    "figure_type": "source_exhibit",
    "context": "Figure 18: Thailand's Trade with Indonesia: Share by Invoice Currency Figure 19: Thailand's Trade with Viet Nam: Share by Invoice Currency In bilateral trade between Thailand and the Mekong region—including Cambodia, the La"
  },
  {
    "figure_id": "F037",
    "report_id": "R004",
    "label": "Figure 18",
    "figure_type": "source_exhibit",
    "context": "Figure 20: Thailand's Trade with Cambodia: Share by Invoice Currency"
  },
  {
    "figure_id": "F038",
    "report_id": "R004",
    "label": "Figure 19",
    "figure_type": "source_exhibit",
    "context": "Figure 20: Thailand's Trade with Cambodia: Share by Invoice Currency"
  },
  {
    "figure_id": "F039",
    "report_id": "R004",
    "label": "Figure 20",
    "figure_type": "source_exhibit",
    "context": "Figure 20: Thailand's Trade with Cambodia: Share by Invoice Currency Figure 21: Thailand's Trade with Lao PDR: Share by Invoice Currency"
  },
  {
    "figure_id": "F040",
    "report_id": "R004",
    "label": "Figure 20",
    "figure_type": "source_exhibit",
    "context": "Figure 20: Thailand's Trade with Cambodia: Share by Invoice Currency Figure 21: Thailand's Trade with Lao PDR: Share by Invoice Currency"
  },
  {
    "figure_id": "F041",
    "report_id": "R004",
    "label": "Figure 20",
    "figure_type": "source_exhibit",
    "context": "Figure 20: Thailand's Trade with Cambodia: Share by Invoice Currency Figure 21: Thailand's Trade with Lao PDR: Share by Invoice Currency Figure 22: Thailand's Trade with Myanmar: Share by Invoice Currency"
  },
  {
    "figure_id": "F042",
    "report_id": "R004",
    "label": "Figure 21",
    "figure_type": "source_exhibit",
    "context": "Figure 21: Thailand's Trade with Lao PDR: Share by Invoice Currency Figure 22: Thailand's Trade with Myanmar: Share by Invoice Currency When we reexamine the growing prominence of the local currency (the Thai baht) in settl"
  },
  {
    "figure_id": "F043",
    "report_id": "R004",
    "label": "Figure 21",
    "figure_type": "source_exhibit",
    "context": "Figure 23: Thailand's International Investment Position"
  },
  {
    "figure_id": "F044",
    "report_id": "R004",
    "label": "Figure 22",
    "figure_type": "source_exhibit",
    "context": "Figure 23: Thailand's International Investment Position ## 3.3 Indonesian Rupiah"
  },
  {
    "figure_id": "F045",
    "report_id": "R004",
    "label": "Figure 23",
    "figure_type": "source_exhibit",
    "context": "Figure 24: Indonesia's Trade Share by Destination Economy (2024)"
  },
  {
    "figure_id": "F046",
    "report_id": "R004",
    "label": "Figure 24",
    "figure_type": "source_exhibit",
    "context": "Figure 25: Indonesia's Trade Share by Currency"
  },
  {
    "figure_id": "F047",
    "report_id": "R004",
    "label": "Figure 24",
    "figure_type": "source_exhibit",
    "context": "Figure 25: Indonesia's Trade Share by Currency"
  },
  {
    "figure_id": "F048",
    "report_id": "R004",
    "label": "Figure 25",
    "figure_type": "source_exhibit",
    "context": "Figure 26: Indonesia's Export by Product (2023)"
  },
  {
    "figure_id": "F049",
    "report_id": "R004",
    "label": "Figure 25",
    "figure_type": "source_exhibit",
    "context": "Figure 26: Indonesia's Export by Product (2023) According to Indonesian statistics, a breakdown of exported goods shows that more than 70% are manufactured) goods, while nearly a quarter are mineral products (Figure 26). In terms"
  },
  {
    "figure_id": "F050",
    "report_id": "R004",
    "label": "Figure 26",
    "figure_type": "source_exhibit",
    "context": "Figure 27: Indonesia's Oil and Gas Export by Economy (2023)"
  },
  {
    "figure_id": "F051",
    "report_id": "R004",
    "label": "Figure 26",
    "figure_type": "source_exhibit",
    "context": "Figure 28: Indonesia's Import of Oil and Gas from the PRC and RMB Invoice Transactions"
  },
  {
    "figure_id": "F052",
    "report_id": "R004",
    "label": "Figure 26",
    "figure_type": "source_exhibit",
    "context": "Figure 28: Indonesia's Import of Oil and Gas from the PRC and RMB Invoice Transactions"
  },
  {
    "figure_id": "F053",
    "report_id": "R004",
    "label": "Figure 27",
    "figure_type": "source_exhibit",
    "context": "Figure 28: Indonesia's Import of Oil and Gas from the PRC and RMB Invoice Transactions Since the mid-2010s, amid changes on the Indonesian side, the central bank has adopted policies prohibiting foreign currency settlements domes"
  },
  {
    "figure_id": "F054",
    "report_id": "R004",
    "label": "Figure 29",
    "figure_type": "source_exhibit",
    "context": "Figure 30: Changes in the Share of Baht-Denominated Bilateral Trade Between Thailand and LCSF Partner Economies (2015 and 2024) Note: Since the share of Indonesian rupiah in bilateral trade between Thailand and Indonesia is not d"
  },
  {
    "figure_id": "F055",
    "report_id": "R004",
    "label": "Figure 31",
    "figure_type": "source_exhibit",
    "context": "Figure 32: Export Invoice Currencies for Selected SITC rev. 4 Divisions, Contributions – 2020–2021"
  },
  {
    "figure_id": "F056",
    "report_id": "R004",
    "label": "Figure 32",
    "figure_type": "source_exhibit",
    "context": "Figure 33: Australia's Import Value Share by Invoice Currencies (2000–2024) Figure 34: Import Invoice Currencies for Selected SITC rev. 4 Divisions, Contributions – 2020–2021"
  },
  {
    "figure_id": "F057",
    "report_id": "R004",
    "label": "Figure 35",
    "figure_type": "source_exhibit",
    "context": "Figure 35: Australian Trade with the PRC by Invoice Currency (%) ## 3.6 Taipei, China/NT Dollar Like Australia, Taipei, China is one of the regions whose foreign and economic relations with the PRC have changed significantly over"
  },
  {
    "figure_id": "F058",
    "report_id": "R004",
    "label": "Figure 37",
    "figure_type": "source_exhibit",
    "context": "Figure 37: Taipei, China's Trade Share by Currency (2019–2024) Taipei, China's Single Window Service Center publishes the share of 28 currencies invoiced for both exports and imports based on customs-declared values on a quarte"
  },
  {
    "figure_id": "F059",
    "report_id": "R004",
    "label": "Figure 37",
    "figure_type": "source_exhibit",
    "context": "Figure 37: Taipei, China's Trade Share by Currency (2019–2024) Taipei, China's Single Window Service Center publishes the share of 28 currencies invoiced for both exports and imports based on customs-declared values on a quarte"
  },
  {
    "figure_id": "F060",
    "report_id": "R004",
    "label": "Figure 38",
    "figure_type": "source_exhibit",
    "context": "Figure 39: EU Trade with the PRC by Product Group, 2014 and 2024"
  },
  {
    "figure_id": "F061",
    "report_id": "R004",
    "label": "Figure 38",
    "figure_type": "source_exhibit",
    "context": "Figure 39: EU Trade with the PRC by Product Group, 2014 and 2024"
  },
  {
    "figure_id": "F062",
    "report_id": "R004",
    "label": "Figure 39",
    "figure_type": "source_exhibit",
    "context": "Figure 40: EU Exports of Goods to the PRC, 2024"
  },
  {
    "figure_id": "F063",
    "report_id": "R004",
    "label": "Figure 42",
    "figure_type": "source_exhibit",
    "context": "Figure 43: Extra-EU Exports by Currency (2024, %)"
  },
  {
    "figure_id": "F064",
    "report_id": "R004",
    "label": "Figure 43",
    "figure_type": "source_exhibit",
    "context": "Figure 44: Extra-EU Imports by Currency (2024, %)"
  },
  {
    "figure_id": "F065",
    "report_id": "R004",
    "label": "Figure 43",
    "figure_type": "source_exhibit",
    "context": "Figure 44: Extra-EU Imports by Currency (2024, %) With respect to imports, only two economies—the Czech Republic (24%) and Denmark (12%)—have a share of non-euro EU member state currencies exceeding 10% (in other economies, the f"
  },
  {
    "figure_id": "F066",
    "report_id": "R004",
    "label": "Figure 52",
    "figure_type": "source_exhibit",
    "context": "Figure 49: Brazil Exports by Currency (1997–2023) Figure 50: Brazil Imports by Currency (1997–2023) Figure 51: Totals Traded by Major Currencies"
  },
  {
    "figure_id": "F067",
    "report_id": "R004",
    "label": "Figure 52",
    "figure_type": "source_exhibit",
    "context": "Figure 49: Brazil Exports by Currency (1997–2023) Figure 50: Brazil Imports by Currency (1997–2023) Figure 51: Totals Traded by Major Currencies Figure 52: Share of Major Currencies by Trade Flow"
  },
  {
    "figure_id": "F068",
    "report_id": "R004",
    "label": "Figure 51",
    "figure_type": "source_exhibit",
    "context": "Figure 53: Renminbi Usage for Brazilian Imports (2023 and 2024)"
  },
  {
    "figure_id": "F069",
    "report_id": "R004",
    "label": "亚洲开发银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "亚洲开发银行｜亚洲开发银行：去美元化不是选择题，而是基础设施竞赛｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F070",
    "report_id": "R005",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Evolution in Time of Commercial Satellites in Operation As of November 2024, EO data was being sold commercially from more than 800 satellites. $^{2}$ This is forecasted to grow to almost 1,500 satellites in 2033, with"
  },
  {
    "figure_id": "F071",
    "report_id": "R005",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Examples of Earth Observation Companies Organized Based on Their Primary Function"
  },
  {
    "figure_id": "F072",
    "report_id": "R005",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Examples of Earth Observation Companies Organized Based on Their Primary Function ## EARTH OBSERVATION OPERATING STACK"
  },
  {
    "figure_id": "F073",
    "report_id": "R005",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Examples of Earth Observation Companies Organized Based on Their Primary Function ## EARTH OBSERVATION OPERATING STACK ## ACQUISITION"
  },
  {
    "figure_id": "F074",
    "report_id": "R005",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Examples of Earth Observation Companies Organized Based on Their Primary Function ## EARTH OBSERVATION OPERATING STACK ## ACQUISITION"
  },
  {
    "figure_id": "F075",
    "report_id": "R005",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Examples of Earth Observation Companies Organized Based on Their Primary Function ## EARTH OBSERVATION OPERATING STACK ## ACQUISITION DATA Build and launch satellites with different sensors to collect data from space a"
  },
  {
    "figure_id": "F076",
    "report_id": "R005",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5: Mapping of Main Earth Observation Companies for Data Dissemination Based on Their Primary Function ## 2.3 NewSpace Sector Over the past decade, a disruptive and highly innovative trend known as “NewSpace” has emerged,"
  },
  {
    "figure_id": "F077",
    "report_id": "R005",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 6: New Commercial Earth Observation Constellation Companies and Operators New constellations may offer different services, but they all focus on one theme: the ability to offer new services and better meet market needs ba"
  },
  {
    "figure_id": "F078",
    "report_id": "R005",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "Figure 8: Evolution Over Time of Earth Observation Data Volumes for Missions Operated and Handled by the European Space Agency Through the full, free, and open (FFO) data policy of the EU EO program, the data coming from the Sen"
  },
  {
    "figure_id": "F079",
    "report_id": "R005",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure 9: Seven European Space Agency Thematic Exploitation Platforms ## EO Data Cubes Data cubes are multidimensional arrays of stacked, EO image data, aggregated from a variety of sources but standardized and harmonized to be"
  },
  {
    "figure_id": "F080",
    "report_id": "R005",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 10: Results of a Survey on How Data Scientists Spend Their Time Data preparation accounts for about 80% of the work of EO scientists and 76% of them consider this arduous task as the least enjoyable part of their work. $^{"
  },
  {
    "figure_id": "F081",
    "report_id": "R005",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 10: Results of a Survey on How Data Scientists Spend Their Time Data preparation accounts for about 80% of the work of EO scientists and 76% of them consider this arduous task as the least enjoyable part of their work. $^{"
  },
  {
    "figure_id": "F082",
    "report_id": "R005",
    "label": "Figure 13",
    "figure_type": "source_exhibit",
    "context": "Figure 13: Examples of Global Satellite-Derived Climate Datasets from the European Space Agency's Climate Change Initiative ## NOAA National Centers for Environmental Information The US National Oceanic and Atmospheric Administra"
  },
  {
    "figure_id": "F083",
    "report_id": "R005",
    "label": "Figure 13",
    "figure_type": "source_exhibit",
    "context": "Figure 13: Examples of Global Satellite-Derived Climate Datasets from the European Space Agency's Climate Change Initiative ## NOAA National Centers for Environmental Information The US National Oceanic and Atmospheric Administra"
  },
  {
    "figure_id": "F084",
    "report_id": "R005",
    "label": "Figure 14",
    "figure_type": "source_exhibit",
    "context": "Figure 14: Earth Observation Data and Services Market, 2022 In terms of geographic distribution, North America retains its position as the market leader in EO, comprising nearly 45% of total global revenue. Europe, accounting for"
  },
  {
    "figure_id": "F085",
    "report_id": "R005",
    "label": "Figure 15",
    "figure_type": "source_exhibit",
    "context": "Figure 15: Distribution of Earth Observation Market Revenue by Market Segment, 2023 In terms of geographic distribution, Europe and the US generate the bulk of revenues from both EO data and value-added services. Collectively, Eu"
  },
  {
    "figure_id": "F086",
    "report_id": "R005",
    "label": "Figure 16",
    "figure_type": "source_exhibit",
    "context": "Figure 16: Geographic Distribution of Earth Observation Market Revenue, 2023 PRC = People's Republic of China. (2) Insurance and finance market segment serving insurers (and re-insurers), and international and local financial ins"
  },
  {
    "figure_id": "F087",
    "report_id": "R005",
    "label": "Figure 18",
    "figure_type": "source_exhibit",
    "context": "## 2.7.2 Bottom-Up Benefits Estimation Methods A good example of a systematic approach and definition of a detailed bottom-up methodology in estimating the benefits of using satellite EO information is that of the Sentinels Benefits Study, carried out by the E"
  },
  {
    "figure_id": "F088",
    "report_id": "R005",
    "label": "Figure 18",
    "figure_type": "source_exhibit",
    "context": "The core of the Sentinels Benefits Study is to understand how a specific EO-derived service is being used by an organization, and how the integration of EO into activities of the organization are benefiting third parties that they deal with, and ultimately soc"
  },
  {
    "figure_id": "F089",
    "report_id": "R005",
    "label": "Figure 19",
    "figure_type": "source_exhibit",
    "context": "Figure 19: Total Estimated Volume of Earth Observation Benefits for Sustainable Palm Oil Production in Southeast Asia via the SeBS Methodology An example of a non-monetized benefit in the regulatory dimension is that of the Europ"
  },
  {
    "figure_id": "F090",
    "report_id": "R005",
    "label": "Figure 20",
    "figure_type": "source_exhibit",
    "context": "Figure 20: Earth Observation ‘Stack’ with ‘As-a-Service’ Business Models Identified In broader geospatial information context, the United Nations Committee of Experts on Global Geospatial Information Management (UN-GGIM) publishe"
  },
  {
    "figure_id": "F091",
    "report_id": "R005",
    "label": "Figure 21",
    "figure_type": "source_exhibit",
    "context": "Figure 21: Chart of the Predictability and Impact of Future Prevailing Drivers and Underlying Trends in the Geospatial Information Industry Across the broader geospatial industry, the next 5 to 10 years will see significant devel"
  },
  {
    "figure_id": "F092",
    "report_id": "R005",
    "label": "Figure 22",
    "figure_type": "source_exhibit",
    "context": "Figure 22: Damage-and-Loss Assessment for the Flood Event in Pakistan, Summer 2022"
  },
  {
    "figure_id": "F093",
    "report_id": "R005",
    "label": "Figure 22",
    "figure_type": "source_exhibit",
    "context": "Figure 22: Damage-and-Loss Assessment for the Flood Event in Pakistan, Summer 2022 Map 18: Example of Land Use Classification Maps for Artificial Surfaces (Transport-Related) and Waterways, near the City of Mendi, Central Papua N"
  },
  {
    "figure_id": "F094",
    "report_id": "R005",
    "label": "Figure 22",
    "figure_type": "source_exhibit",
    "context": "Figure 22: Damage-and-Loss Assessment for the Flood Event in Pakistan, Summer 2022 Map 18: Example of Land Use Classification Maps for Artificial Surfaces (Transport-Related) and Waterways, near the City of Mendi, Central Papua N"
  },
  {
    "figure_id": "F095",
    "report_id": "R005",
    "label": "Figure 25",
    "figure_type": "source_exhibit",
    "context": "Figure 25: Satellite Data Record of Atmospheric Carbon Dioxide Sources: C3S, CCI, CAMS, University of Bremen, and SRON. https://atmosphere.copernicus.eu/cop26-cams-help-measure-progress-towards-co2-goals."
  },
  {
    "figure_id": "F096",
    "report_id": "R005",
    "label": "Figure 25",
    "figure_type": "source_exhibit",
    "context": "Figure 26: Annual Mean Carbon Dioxide Exchange Between Land and Atmosphere for Agricultural, Forestry, and Other Land Use Sector"
  },
  {
    "figure_id": "F097",
    "report_id": "R005",
    "label": "Figure 25",
    "figure_type": "source_exhibit",
    "context": "Figure 26: Annual Mean Carbon Dioxide Exchange Between Land and Atmosphere for Agricultural, Forestry, and Other Land Use Sector PRC = People's Republic of China."
  },
  {
    "figure_id": "F098",
    "report_id": "R005",
    "label": "Figure 26",
    "figure_type": "source_exhibit",
    "context": "Figure 26: Annual Mean Carbon Dioxide Exchange Between Land and Atmosphere for Agricultural, Forestry, and Other Land Use Sector PRC = People's Republic of China. The annual mean $CO_{2}$ exchange between land and atmosphere for"
  },
  {
    "figure_id": "F099",
    "report_id": "R005",
    "label": "Figure 28",
    "figure_type": "source_exhibit",
    "context": "Figure 28: Satellite Data Record of Atmospheric Methane"
  },
  {
    "figure_id": "F100",
    "report_id": "R005",
    "label": "Figure 28",
    "figure_type": "source_exhibit",
    "context": "Figure 28: Satellite Data Record of Atmospheric Methane Map 68: Global Methane Forecast Total Column, 3 November 2022 An example of a methane total column forecasting global distribution. $^{161}$ This map imagery was produced"
  },
  {
    "figure_id": "F101",
    "report_id": "R005",
    "label": "Figure 28",
    "figure_type": "source_exhibit",
    "context": "Figure 28: Satellite Data Record of Atmospheric Methane Map 68: Global Methane Forecast Total Column, 3 November 2022 An example of a methane total column forecasting global distribution. $^{161}$ This map imagery was produced"
  },
  {
    "figure_id": "F102",
    "report_id": "R005",
    "label": "Figure 29",
    "figure_type": "source_exhibit",
    "context": "Figure 29: Breakdown of 2022 Global Methane Emissions by Main Emitter Type"
  },
  {
    "figure_id": "F103",
    "report_id": "R005",
    "label": "Figure 29",
    "figure_type": "source_exhibit",
    "context": "Figure 29: Breakdown of 2022 Global Methane Emissions by Main Emitter Type Oil & Gas Facility - Asia GHGSat-C2 - CH4 Measurement Map 71: An Example of a Landfill Methane Emission from a Location in India India has the most indi"
  },
  {
    "figure_id": "F104",
    "report_id": "R005",
    "label": "Figure 29",
    "figure_type": "source_exhibit",
    "context": "Figure 29: Breakdown of 2022 Global Methane Emissions by Main Emitter Type Oil & Gas Facility - Asia GHGSat-C2 - CH4 Measurement Map 71: An Example of a Landfill Methane Emission from a Location in India India has the most indi"
  },
  {
    "figure_id": "F105",
    "report_id": "R005",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "This global map was produced by inverting surface fluxes from $N_{2}O$ space-borne measurements (IASI on Metop-A) sensitive to the lowermost atmospheric layers. $^{167}$ For anthropogenic emissions, East and South Asia, Europe, and North America are the most-e"
  },
  {
    "figure_id": "F106",
    "report_id": "R005",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "For anthropogenic emissions, East and South Asia, Europe, and North America are the most-emitting regions, while for natural soil emissions, Equatorial and South Africa and South America are the most-emitting regions. For the ocean, the Eastern Equatorial Paci"
  },
  {
    "figure_id": "F107",
    "report_id": "R005",
    "label": "Figure 30",
    "figure_type": "source_exhibit",
    "context": "Figure 30: Example Output Information from an ADB Digital Platform for Carbon Dioxide Emissions Analytics Different transport options accompanied by investments can lead to lower emissions. Long-term development plans that affect"
  },
  {
    "figure_id": "F108",
    "report_id": "R005",
    "label": "Figure 31",
    "figure_type": "source_exhibit",
    "context": "These types of urban information require the use of multispectral satellite imagery. The main sources of data used was from the French national missions of high-resolution (HR, 20 m) SPOT-1, SPOT-2, SPOT-4, and very-high-resolution (VHR, 0.5 m) Pléiades-1A sat"
  },
  {
    "figure_id": "F109",
    "report_id": "R005",
    "label": "Figure 31",
    "figure_type": "source_exhibit",
    "context": "Figure 31: Land Use Land Cover Distribution of Aggregated Classes in Caloocan City"
  },
  {
    "figure_id": "F110",
    "report_id": "R005",
    "label": "Figure 31",
    "figure_type": "source_exhibit",
    "context": "Figure 31: Land Use Land Cover Distribution of Aggregated Classes in Caloocan City Sources: GIM and ESA. https://eo4society.esa.int/wp-content/uploads/2021/11/EOSD\\_160905-V2-FINAL.pdf. For the period 1990–2000, the expansion of"
  },
  {
    "figure_id": "F111",
    "report_id": "R005",
    "label": "Figure 32",
    "figure_type": "source_exhibit",
    "context": "Figure 32: Informal Settlement Families Distribution per Slum Type for Metro Manila, 2014 (%) Sources: GIM and ESA. https://eo4society.esa.int/wp-content/uploads/2021/11/EOSD\\_160905-V2-FINAL.pdf."
  },
  {
    "figure_id": "F112",
    "report_id": "R005",
    "label": "Figure 32",
    "figure_type": "source_exhibit",
    "context": "Figure 32: Informal Settlement Families Distribution per Slum Type for Metro Manila, 2014 (%) Sources: GIM and ESA. https://eo4society.esa.int/wp-content/uploads/2021/11/EOSD\\_160905-V2-FINAL.pdf. Calculating the ratio of area"
  },
  {
    "figure_id": "F113",
    "report_id": "R005",
    "label": "Figure 32",
    "figure_type": "source_exhibit",
    "context": "Figure 32: Informal Settlement Families Distribution per Slum Type for Metro Manila, 2014 (%) Sources: GIM and ESA. https://eo4society.esa.int/wp-content/uploads/2021/11/EOSD\\_160905-V2-FINAL.pdf. Calculating the ratio of area"
  },
  {
    "figure_id": "F114",
    "report_id": "R005",
    "label": "Figure 33",
    "figure_type": "source_exhibit",
    "context": "Figure 33: Proportion of Informal Settlement Family Areas That Are Flood Prone (%) Sources: GIM, ESA (Note: For an event with a return period of 50 years; only the municipalities for which data was available were considered). Fig"
  },
  {
    "figure_id": "F115",
    "report_id": "R005",
    "label": "Figure 33",
    "figure_type": "source_exhibit",
    "context": "Figure 35: Proportion of Informal Settlements Within 1-Kilometer Distance from a School (%) Sources: GIM, ESA."
  },
  {
    "figure_id": "F116",
    "report_id": "R005",
    "label": "Figure 34",
    "figure_type": "source_exhibit",
    "context": "Figure 35: Proportion of Informal Settlements Within 1-Kilometer Distance from a School (%) Sources: GIM, ESA. The main conclusions arising from the materials presented in this technical study are as follows: (1) The most compreh"
  },
  {
    "figure_id": "F117",
    "report_id": "R005",
    "label": "亚洲开发银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "亚洲开发银行｜亚洲开发银行：不是卫星数量，而是数据应用，亚洲发展的新测量逻辑｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F118",
    "report_id": "R006",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Abnormal Global Warming, 1880–2024 A recent report by the World Meteorological Organization has shown 2024 as the warmest year on record globally. $^{2}$ The report highlights that global warming is accelerating expone"
  },
  {
    "figure_id": "F119",
    "report_id": "R006",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Prolonged extreme heat also undermines human nutrition and food security by reducing the nutritional value of cereal grains and decreasing livestock productivity, including the production of eggs, milk, and meat. Furthermore, it adversely affects human product"
  },
  {
    "figure_id": "F120",
    "report_id": "R006",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Temperatures in Asia Exceeding the Wet-Bulb Temperature of $35^{\\circ}$ C PRC = People's Republic of China, ROK = Republic of Korea, Lao PDR = Lao People's Democratic Republic. Sources: (i) Left graph: Authors, using d"
  },
  {
    "figure_id": "F121",
    "report_id": "R006",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "# THAILAND: VULNERABILITY TO EXTREME HEAT ## Heat Trends and Projections Thailand's average maximum temperatures have risen by $\\sim 1.0^{\\circ}\\mathrm{C}$ since the early 1980s (Figure 4), with more frequent and intense heat waves. The country ranked among th"
  },
  {
    "figure_id": "F122",
    "report_id": "R006",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Several barriers hinder efforts to scale up adaptation and mitigation activities to quickly meet the challenges of a heating planet. These barriers, illustrated in Figure 6, fall under three broad areas: (i) lack of awareness at the policy and institutional le"
  },
  {
    "figure_id": "F123",
    "report_id": "R006",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 7: The Urban Heat Island Effect ## Energy Demand and Energy Loop Similarly, the development of buildings is generally not integrated with the impact heat can have. Buildings are not designed for passive cooling or ventila"
  },
  {
    "figure_id": "F124",
    "report_id": "R006",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure 8: Available Financial Resources for Project Heat Derisking ## Figure 9: SDG Indonesia One: Green Finance Facility Under-utilization of capital markets and innovative mechanisms for accessing private financing sources"
  },
  {
    "figure_id": "F125",
    "report_id": "R006",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure 8: Available Financial Resources for Project Heat Derisking ## Figure 9: SDG Indonesia One: Green Finance Facility Under-utilization of capital markets and innovative mechanisms for accessing private financing sources U"
  },
  {
    "figure_id": "F126",
    "report_id": "R006",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "## Scaling Up Action Nationally While the country has broader climate and health frameworks in place—such as the Climate Change Master Plan (2015–2050), the National Climate Change Adaptation Plan, and various environmental health strategic plans—these primari"
  },
  {
    "figure_id": "F127",
    "report_id": "R006",
    "label": "亚洲开发银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "亚洲开发银行｜亚洲开发银行：高温导致2.4万亿美元生产力损失，亚洲开发银行警告东南亚风险｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F128",
    "report_id": "R007",
    "label": "布鲁盖尔研究所视觉摘要 1",
    "figure_type": "external_card",
    "context": "布鲁盖尔研究所｜布鲁盖尔研究所：数字市场法案要求谷歌开放系统，第三方AI服务迎来转机｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F129",
    "report_id": "R008",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Number of products published in the DIU's catalogue by technological area"
  },
  {
    "figure_id": "F130",
    "report_id": "R008",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Number of products published in the DIU's catalogue by technological area ## 3 Data collection and descriptive statistics To evaluate the effectiveness of the DIU, we first constructed a novel dataset of DoD procuremen"
  },
  {
    "figure_id": "F131",
    "report_id": "R008",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Location of treated and untreated DoD vendors by US metropolitan area ## 4 Data matching To ensure comparability between treated and untreated firms, we use propensity score matching to identify within the large pool o"
  },
  {
    "figure_id": "F132",
    "report_id": "R008",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: Absolute SMD before and after propensity score matching After constructing a matched sample that resembles the treated firms in terms of industry, location and products sold, we compare the two groups' other characteri"
  },
  {
    "figure_id": "F133",
    "report_id": "R008",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5: Dynamic effects of the augmented specification, awarded contracts ## 7 Robustness checks Second, we consider unit placebo tests, in which 'fake' treatment is assigned at random to untreated firms. We repeat this proced"
  },
  {
    "figure_id": "F134",
    "report_id": "R008",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Distribution of unit-placebo tests, extensive margin of awarded contracts Figures 3 and 4 show that the resulting leave-one-out estimates are clustered around the original estimated effects for both specifications and"
  },
  {
    "figure_id": "F135",
    "report_id": "R008",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Distribution of unit-placebo tests, extensive margin of awarded contracts Figures 3 and 4 show that the resulting leave-one-out estimates are clustered around the original estimated effects for both specifications and"
  },
  {
    "figure_id": "F136",
    "report_id": "R008",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Distribution of unit-placebo tests, extensive margin of awarded contracts Figures 3 and 4 show that the resulting leave-one-out estimates are clustered around the original estimated effects for both specifications and"
  },
  {
    "figure_id": "F137",
    "report_id": "R008",
    "label": "布鲁盖尔研究所视觉摘要 1",
    "figure_type": "external_card",
    "context": "布鲁盖尔研究所｜布鲁盖尔研究所：五角大楼用十年验证，硅谷创新如何真正融入国防｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F138",
    "report_id": "R009",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Minimum requirements and observed levels, EU/US megabanks, end-2024 Figure 1a: Solvency ratio (%) Figure 1b: Leverage ratio (%) Sources and notes: see appendix. (\\*) In the US stack the ‘stress capital buffer’ in the"
  },
  {
    "figure_id": "F139",
    "report_id": "R009",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1: Minimum requirements and observed levels, EU/US megabanks, end-2024 Figure 1a: Solvency ratio (%) Figure 1b: Leverage ratio (%) Sources and notes: see appendix. (\\*) In the US stack the ‘stress capital buffer’ in the"
  },
  {
    "figure_id": "F140",
    "report_id": "R009",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Minimum requirements and observed levels, EU/US megabanks, end-2025 Figure 2a: Solvency ratio (%) Figure 2b: Leverage ratio (%) Sources and notes: see appendix. (\\*) In the US stack the 'stress capital buffer' in the"
  },
  {
    "figure_id": "F141",
    "report_id": "R009",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Minimum requirements and observed levels, EU/US megabanks, end-2025 Figure 2a: Solvency ratio (%) Figure 2b: Leverage ratio (%) Sources and notes: see appendix. (\\*) In the US stack the 'stress capital buffer' in the"
  },
  {
    "figure_id": "F142",
    "report_id": "R009",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## Actual capital levels and ratios For EU megabanks, Figure 1 shows capital ratios at end-2024 (triangles) from the EBA transparency exercise $^{80}$ . As end-2025 data was unavailable from that"
  },
  {
    "figure_id": "F143",
    "report_id": "R009",
    "label": "布鲁盖尔研究所视觉摘要 1",
    "figure_type": "external_card",
    "context": "布鲁盖尔研究所｜布鲁盖尔研究所：欧盟银行业政策碎片化才是真正挑战，而非美国监管竞争｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F144",
    "report_id": "R010",
    "label": "布鲁盖尔研究所视觉摘要 1",
    "figure_type": "external_card",
    "context": "布鲁盖尔研究所｜布鲁盖尔研究所：不是规则太少，而是规则太复杂，欧盟绿色金融的结构性矛盾｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F145",
    "report_id": "R011",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "However, these are unweighted averages, which do not reflect the difficulty of completing individual chapters and their relative importance for the accession process. For example, looking at chapters 23 and 24, considered as the most difficult to adopt (and su"
  },
  {
    "figure_id": "F146",
    "report_id": "R011",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "However, these are unweighted averages, which do not reflect the difficulty of completing individual chapters and their relative importance for the accession process. For example, looking at chapters 23 and 24, considered as the most difficult to adopt (and su"
  },
  {
    "figure_id": "F147",
    "report_id": "R011",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Montenegro recorded in 2025 a 'good' level of preparation (Figure 1). Other candidates recorded either a 'moderate' (Albania, North Macedonia, Serbia in Chapter 24) or 'some' level of preparation."
  },
  {
    "figure_id": "F148",
    "report_id": "R011",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2: Evolution of overall weighted and unweighted preparedness scores, 2020–2025"
  },
  {
    "figure_id": "F149",
    "report_id": "R011",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "The ranking of individual countries in adoption of the acquis and the speed of accession-related reforms looks similar when one uses the weighted and unweighted averages. Montenegro is the undisputed leader, followed by Serbia, North Macedonia and Albania. The"
  },
  {
    "figure_id": "F150",
    "report_id": "R011",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3 shows an even larger gap between the Western Balkan candidates and the Eastern European ones – plus Bosnia and Herzegovina – than in the overall scores (Figure 2). However, two of four leaders suffered substantial reform reversals in 2023 (North Maced"
  },
  {
    "figure_id": "F151",
    "report_id": "R011",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 6: Evolution of weighted preparedness scores in the Cluster 4 'Green agenda & sustainable connectivity', 2020–2025"
  },
  {
    "figure_id": "F152",
    "report_id": "R011",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 6: Evolution of weighted preparedness scores in the Cluster 4 'Green agenda & sustainable connectivity', 2020–2025 A similar picture can be obtained in the Cluster 5 'Resources, agriculture & cohesion' (Figure 7): moderat"
  },
  {
    "figure_id": "F153",
    "report_id": "R011",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "A similar picture can be obtained in the Cluster 5 'Resources, agriculture & cohesion' (Figure 7): moderate levels of advancement, smaller interregional differences, but more progress in the analysed period. Moldova recorded rapid progress from a very low leve"
  },
  {
    "figure_id": "F154",
    "report_id": "R011",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 9: Decomposition of weighted preparedness scores by cluster, 2025"
  },
  {
    "figure_id": "F155",
    "report_id": "R011",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "Figure 9: Decomposition of weighted preparedness scores by cluster, 2025 ## 5 Comparison with other surveys Changes in economic, political and institutional systems are the subject of many global surveys. For a comparison with t"
  },
  {
    "figure_id": "F156",
    "report_id": "R011",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 11: Cluster 1 performance vs the average WGIs (2024)"
  },
  {
    "figure_id": "F157",
    "report_id": "R011",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "Figure 11: Cluster 1 performance vs the average WGIs (2024) ■ WGI: average of six selected indicators ■ Weighted average of Cluster 1: Fundamentals"
  },
  {
    "figure_id": "F158",
    "report_id": "R011",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "Figure 11: Cluster 1 performance vs the average WGIs (2024) ■ WGI: average of six selected indicators ■ Weighted average of Cluster 1: Fundamentals By contrast, its Cluster 1 'Fundamentals' preparedness scores were lower in 202"
  },
  {
    "figure_id": "F159",
    "report_id": "R011",
    "label": "Figure 13",
    "figure_type": "source_exhibit",
    "context": "By contrast, its Cluster 1 'Fundamentals' preparedness scores were lower in 2024 (Figures 3 and 11), suggesting that the Commission's accession-related assessments have become increasingly critical regarding democratic governance, judicial independence and ins"
  },
  {
    "figure_id": "F160",
    "report_id": "R011",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "Figure 14: Cluster 1 performance vs the EBRD 'well-governed' score (2025) This measure covers public economic governance – including the rule of law, control of corruption and institutional quality – as well as corporate governan"
  },
  {
    "figure_id": "F161",
    "report_id": "R011",
    "label": "Figure 15",
    "figure_type": "source_exhibit",
    "context": "Figure 15: Status of EU accession negotiations by a candidate country (10 June 2026) Similarly to North Macedonia, Albania $^{21}$ (a candidate from June 2014) opened accession negotiations in March 2020, held the First ICG in Ju"
  },
  {
    "figure_id": "F162",
    "report_id": "R011",
    "label": "布鲁盖尔研究所视觉摘要 1",
    "figure_type": "external_card",
    "context": "布鲁盖尔研究所｜布鲁盖尔研究所：世界银行数据之外，欧盟候选国法治改革才是入盟关键｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F163",
    "report_id": "R012",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 1: China's share of global emissions and energy (%) Figure 2: Chinese domestic energy production as a share of demand (%)"
  },
  {
    "figure_id": "F164",
    "report_id": "R012",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 1: China's share of global emissions and energy (%) Figure 2: Chinese domestic energy production as a share of demand (%)"
  },
  {
    "figure_id": "F165",
    "report_id": "R012",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3: Levelised cost of power generation by energy"
  },
  {
    "figure_id": "F166",
    "report_id": "R012",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4: China on-grid power price\\* by energy"
  },
  {
    "figure_id": "F167",
    "report_id": "R012",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 6: Chinese solar manufacturing capacity (GW)"
  },
  {
    "figure_id": "F168",
    "report_id": "R012",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 6: Chinese solar manufacturing capacity (GW) Figure 7: Solar product prices (indexed, 3 November 2020 = 100) The surge in capacity proved poorly calibrated to demand. Overseas demand for Chinese renewable equipment dece"
  },
  {
    "figure_id": "F169",
    "report_id": "R012",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 6: Chinese solar manufacturing capacity (GW) Figure 7: Solar product prices (indexed, 3 November 2020 = 100) The surge in capacity proved poorly calibrated to demand. Overseas demand for Chinese renewable equipment dece"
  },
  {
    "figure_id": "F170",
    "report_id": "R012",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 8: Renewable sector financial health ## 5 Infrastructure as a demand-side solution ## 5.1 The grid-generation gap"
  },
  {
    "figure_id": "F171",
    "report_id": "R012",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure 10: Chinese power investment by category (RMB billions)"
  },
  {
    "figure_id": "F172",
    "report_id": "R012",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure 10: Chinese power investment by category (RMB billions) Figure 11: Power supply surplus/deficit by region (TWh) ## 5.2 The east-west dimension"
  },
  {
    "figure_id": "F173",
    "report_id": "R012",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 10: Chinese power investment by category (RMB billions) Figure 11: Power supply surplus/deficit by region (TWh) ## 5.2 The east-west dimension The geography of China's energy system imposes another fundamental structural"
  },
  {
    "figure_id": "F174",
    "report_id": "R012",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "Figure 12: Annual power demand forecast for China (TWh) The two scenarios are defined by contrasting assumptions about the demand effect of grid improvements, drawing on the theoretical dichotomy between demand frontloading and p"
  },
  {
    "figure_id": "F175",
    "report_id": "R012",
    "label": "Figure 13",
    "figure_type": "source_exhibit",
    "context": "Figure 13: Scenario 1, five-year demand frontloading The near-term relief is significant: wind equipment manufacturing utilisation rates would recover from approximately 53 percent in 2021–2025 to 85 percent in 2026–2030. However"
  },
  {
    "figure_id": "F176",
    "report_id": "R012",
    "label": "Figure 14",
    "figure_type": "source_exhibit",
    "context": "The near-term relief is significant: wind equipment manufacturing utilisation rates would recover from approximately 53 percent in 2021–2025 to 85 percent in 2026–2030. However, after 2030, annual installation would fall sharply, pushing manufacturing utilisat"
  },
  {
    "figure_id": "F177",
    "report_id": "R012",
    "label": "布鲁盖尔研究所视觉摘要 1",
    "figure_type": "external_card",
    "context": "布鲁盖尔研究所｜布鲁盖尔研究所：中国光伏行业利润率转负，布鲁盖尔研究所警告产能过剩是结构性的｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F178",
    "report_id": "R013",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## The majority of Greek emigrants are located in OECD countries The distribution of Greek emigrants across destination regions has remained highly concentrated in OECD countries over the past three decades. According to UNDESA data, OECD destinations have con"
  },
  {
    "figure_id": "F179",
    "report_id": "R013",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "“Diaspora” is a broader concept that also lacks a single definition. Unlike definitions based strictly on birthplace or citizenship, “diaspora” refers to populations that maintain real or perceived connections to a country of origin across multiple generations"
  },
  {
    "figure_id": "F180",
    "report_id": "R013",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Greece's emigrant population in OECD countries increased from about 707 000 nationals in 2010/11 to 811 000 in 2020/21, a rise of $15\\%$ . This places Greece in the mid-range of European countries: the growth is significantly lower than in countries such as Po"
  },
  {
    "figure_id": "F181",
    "report_id": "R013",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Stock of emigrant population from selected OECD countries (left scale), growth 2010/11 to 2020/21 in percentages (right scale), all ages While Greece has a relatively small Greek-born population in OECD countries in absolute numbers, its rate of emigration is "
  },
  {
    "figure_id": "F182",
    "report_id": "R013",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## More than half of Greek emigrants are of working age Among Greek emigrants in the OECD area in 2020/21, men (approximately 419 000 or 52%) slightly outnumbered women (approximately 392 000 or 48%) (see Figure 1.5). This gender pattern was already present in"
  },
  {
    "figure_id": "F183",
    "report_id": "R013",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "In 2020/21, individuals of working age made up nearly 59% of all Greek emigrants in the OECD area: 8% were aged 15-24, while 51% were between 25 and 64 years old (see Figure 1.6). Greek emigrants aged 0-14 represented 8%, and those aged 65 and over made up a n"
  },
  {
    "figure_id": "F184",
    "report_id": "R013",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "The age composition of Greek emigrants of working age in the OECD area has shifted gradually over the past two decades. In 2000/01, the majority of emigrants were of working age (25-64), accounting for 70% of the total, while younger adults aged 15-24 made up "
  },
  {
    "figure_id": "F185",
    "report_id": "R013",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1.8. Most Greek emigrants are married, but men are more likely to be single Stock of Greek emigrants in OECD countries by marital status, ages 15 and above, 2020/21 ## Destination patterns of Greek emigrants: Stability and new growth corridors According"
  },
  {
    "figure_id": "F186",
    "report_id": "R013",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## Twelve countries hosted 93% of Greece's emigrants in the OECD area in 2020/21 From a regional perspective, the data indicate that in 2020/21, two-thirds of all Greek emigrants (64%) were concentrated within Europe. Among the remaining 36% living outside Eur"
  },
  {
    "figure_id": "F187",
    "report_id": "R013",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## The number of Greek emigrants in Germany has risen over the past two decades Long-term trends across the five largest destination countries underscore both the persistence of established migration corridors and the gradual reshaping of Greece's diaspora lan"
  },
  {
    "figure_id": "F188",
    "report_id": "R013",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "This section draws on OECD DIOC data to examine the distribution of Greek emigrants across key OECD destination countries, focussing on variations in their gender, age and regional settlement patterns. Based on national data sources, it further provides a brie"
  },
  {
    "figure_id": "F189",
    "report_id": "R013",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Intermediate patterns emerge in Germany and Sweden, where the working-age population remains the largest group, around 57-62%, but older adults also represent a meaningful share, at 19-25%. Children and young adults are present in modest numbers, with 8-14% in"
  },
  {
    "figure_id": "F190",
    "report_id": "R013",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## About half of all Greek-born emigrants in Sweden live in the Stockholm region Figure 1.13. Greek emigrants to Sweden are highly concentrated in the Stockholm region Distribution of Greek-born individuals in Sweden by region, 2024 Note: This map is for illus"
  },
  {
    "figure_id": "F191",
    "report_id": "R013",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "In Canada, Greek-born emigrants are highly concentrated in just two provinces. Ontario and Quebec together account for 87% of all Greek-born residents, with Ontario hosting around 31 650 individuals and Quebec a further 16 130 (see Figure 1.14). These two prov"
  },
  {
    "figure_id": "F192",
    "report_id": "R013",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "South Australia hosts the third-largest Greek-born population, with over 8 100 residents. Other states and territories, including Queensland, Western Australia, the Northern Territory, Tasmania and the Australian Capital Territory, host smaller Greek-born popu"
  },
  {
    "figure_id": "F193",
    "report_id": "R013",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Beyond these states, Greek-born residents are present in smaller but still substantial numbers across several midsized and economically diverse states. These include Pennsylvania (5 438) and Connecticut (4 063), which are also neighbours to New York, and Texas"
  },
  {
    "figure_id": "F194",
    "report_id": "R013",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## About half of the Greek-born emigrants in OECD countries have acquired citizenship of the host country According to DIOC data for 2020/21, about half of all Greek emigrants (49%) were citizens of the OECD country in which they reside. In historically popula"
  },
  {
    "figure_id": "F195",
    "report_id": "R013",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Many countries show a rise in citizenship acquisition between 2012 and 2024. The selection of countries in this section captures a range of migration contexts: post-Brexit dynamics in the United Kingdom, the long-established Greek diaspora in the United States"
  },
  {
    "figure_id": "F196",
    "report_id": "R013",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1.18. Acquisition of nationality in the United Kingdom has been increasing over the past decade Figure 1.19. Acquisitions of nationality in Switzerland and Belgium have increased since 2020 In settlement countries such as Australia and Canada, the numbe"
  },
  {
    "figure_id": "F197",
    "report_id": "R013",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1.19. Acquisitions of nationality in Switzerland and Belgium have increased since 2020 In settlement countries such as Australia and Canada, the numbers are smaller, but naturalisation numbers have generally trended upward as well. Australia experienced"
  },
  {
    "figure_id": "F198",
    "report_id": "R013",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Estimates of total emigration from Greece to all destination countries, based on calculations by the national statistical office (ELSTAT), display that outflows of Greek citizens rose sharply in the aftermath of the global financial and sovereign debt crises, "
  },
  {
    "figure_id": "F199",
    "report_id": "R013",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## The economic crisis marked a turning point in recent Greek emigration patterns After peaking at 55 760 in 2019, migration flows from Greece to OECD countries declined sharply to 32 543 in 2020, likely reflecting the widespread mobility restrictions and econ"
  },
  {
    "figure_id": "F200",
    "report_id": "R013",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "An examination of flows to long-distance English-speaking destinations shows how mobility patterns have evolved outside Europe over the past two decades. $^{1}$ Across these countries, the United States consistently receives the largest number of Greek emigran"
  },
  {
    "figure_id": "F201",
    "report_id": "R013",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## With about 16 500 Greek emigrants arriving in 2024, Germany has remained a major destination for Greek emigrants While inflows gradually declined after 2014, they have remained well above pre-crisis levels, indicating that Germany continues to play a signif"
  },
  {
    "figure_id": "F202",
    "report_id": "R013",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "These findings are consistent with Eurostat data on EU free movement which shows that in recent years the Netherlands consistently ranks among the top destinations for intra-EU movers. In fact, in 2021, the Netherlands accounted for around 8% of all intra-EU m"
  },
  {
    "figure_id": "F203",
    "report_id": "R013",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Historical migration links and sustained institutional co-operation may help explain the relatively high and persistent emigration from Greece to Sweden. Labour migration flows in the 1960s and 1970s established strong bilateral ties, resulting in a pool of Gr"
  },
  {
    "figure_id": "F204",
    "report_id": "R013",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## Net migration has remained positive in many major European destinations Among major destination countries, patterns vary, but overall trends point to sustained Greek populations. Net migration to the Netherlands has grown markedly over the past two decades,"
  },
  {
    "figure_id": "F205",
    "report_id": "R013",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Note: Countries were selected based on major destination countries from Greece with available inflow and outflow data. Figures refer to the difference between the annual gross inflow and the annual gross outflow of Greek citizens of all ages from each destinat"
  },
  {
    "figure_id": "F206",
    "report_id": "R013",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## Greek emigration between 2005 and 2023 has largely remained male-dominated Across long-standing destinations such as the United States, Australia and Canada, Greek emigration between 2005 and 2023 has consistently remained male-dominated, although the degre"
  },
  {
    "figure_id": "F207",
    "report_id": "R013",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Note: The OECD International Migration Database captures annual legal migration flows of both permanent and temporary entries, except for the United States, Canada and Australia where only permanent migrants are recorded. Figure 2.10. The share of women among "
  },
  {
    "figure_id": "F208",
    "report_id": "R013",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2.11. Women remain a minority among Greek emigrant inflows to most Western and Central European destinations ##"
  },
  {
    "figure_id": "F209",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "The educational profile of Greek-born migrants varies substantially across destination countries, reflecting both the selectivity of migration flows and the characteristics of host-country labour markets. It is important to note that across all destinations, d"
  },
  {
    "figure_id": "F210",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "## A larger share of Greek-born emigrants has achieved high educational attainment in most destination countries when compared with the native-born populations In Germany, Belgium, Sweden, Canada and Australia, Greek-born adults are more likely than the native"
  },
  {
    "figure_id": "F211",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Educational attainment of Greek-born and native-born populations in selected OECD countries, ages 15-64, 2020/21 Across OECD countries, Greek-born women and men display broadly similar levels of educational attainment. Shares with low education are identical f"
  },
  {
    "figure_id": "F212",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Note: For Belgium, Australia, the United Kingdom, Sweden and the United States, educational attainment is not fully available, as a non-negligible share of the population is classified as having unknown educational attainment. As a result, those who are unknow"
  },
  {
    "figure_id": "F213",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Employment rates follow a broadly comparable pattern, though with narrower differences. Among all individuals aged 15-64, 69% of Greek-born persons in OECD countries are employed, compared with 68% of the native-born persons. Among men, the employment rate is "
  },
  {
    "figure_id": "F214",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "In contrast, the United Kingdom stands out as a case where Greek-born migrants perform strongly relative to the native-born. Both men and women born in Greece have higher or comparable participation and employment rates, with Greek-born men participating at ar"
  },
  {
    "figure_id": "F215",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "The United States presents a mixed picture that combines elements from both groups. Greek-born men show high labour market participation, over 80%, similar to Germany and higher than among US-born men and show similarly high employment rates. Among women, part"
  },
  {
    "figure_id": "F216",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Labour market participation and employment rates by country of birth, gender, and country of residence, ages 15-64, 2020/21 Note: LMP denotes labour market participation. Labour market participation and employment rates of Greek-born emigrants by country of re"
  },
  {
    "figure_id": "F217",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Labour market participation and employment rates by country of birth, gender, and country of residence, ages 15-64, 2020/21 Note: LMP denotes labour market participation. Labour market participation and employment rates of Greek-born emigrants by country of re"
  },
  {
    "figure_id": "F218",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Note: LMP denotes labour market participation. Labour market participation and employment rates of Greek-born emigrants by country of residence, ages 15-64, 2010/11 and 2015/16 Figure 3.7. Employment rates of Greek-born emigrants are the highest in the United "
  },
  {
    "figure_id": "F219",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Labour market participation and employment rates of Greek-born emigrants by country of residence, ages 15-64, 2010/11 and 2015/16 Figure 3.7. Employment rates of Greek-born emigrants are the highest in the United Kingdom and Switzerland ## Higher levels of edu"
  },
  {
    "figure_id": "F220",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "## Higher levels of educational attainment are associated with stronger employment outcomes among Greek-born migrants Across major destination countries, employment rates among Greek-born individuals vary markedly by educational attainment, though the overall "
  },
  {
    "figure_id": "F221",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "As shown in Figure 3.9, the unemployment rate of Greek-born individuals in 2020/21 varied across OECD destination countries and, in every case aside from the United States, exceeded that of the native-born population in 2020/21. On average, unemployment among "
  },
  {
    "figure_id": "F222",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "The labour market outcomes of Greek-born migrants were generally more reflective of the native-born population or the foreign-born population in 2020/21. Among men, unemployment rates in 2020/21 for Greek-born individuals were generally closer to those of nati"
  },
  {
    "figure_id": "F223",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3.10. Greek-born women experienced substantially higher unemployment than their native-born peers in Canada, Germany and Switzerland in 2020/21 Unemployment rate of Greek-born and native-born persons in selected OECD countries by gender, ages 15-64, 202"
  },
  {
    "figure_id": "F224",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "## Greek emigrants tend to be concentrated in medium- and high-skilled jobs Job quality is a central dimension of integration, as it shapes earnings prospects, career progression, job stability, and overall well-being. Across the OECD, Greek-born workers are p"
  },
  {
    "figure_id": "F225",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Distribution of Greek-born workers by occupation, ages 15 and above, OECD, 2015/16 and 2010/11 Note: Among the top ten destination countries for Greek emigrants in the OECD, only those with available data are included. Similarly, the OECD-wide analysis is rest"
  },
  {
    "figure_id": "F226",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "By contrast, in Belgium, Switzerland and France, Greek-born emigrants are more likely than natives to be employed in highly skilled occupations. In Belgium, 57% of Greek-born workers are in high-skilled roles compared with 47% of native-born workers, while in "
  },
  {
    "figure_id": "F227",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3.13. Greek-born emigrants are often underrepresented in medium skilled positions when compared with their native-born counterparts Distribution of Greek-born and native-born workers by occupation, ages 15 and above, selected OECD countries, 2020/21 Fra"
  },
  {
    "figure_id": "F228",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Australia Belgium To examine occupational outcomes in greater detail, employment can be analysed using the International Standard Classification of Occupations (ISCO), which categorises jobs into major groups ranging from ISCO 0 to ISCO 9. These groups disting"
  },
  {
    "figure_id": "F229",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Australia Belgium To examine occupational outcomes in greater detail, employment can be analysed using the International Standard Classification of Occupations (ISCO), which categorises jobs into major groups ranging from ISCO 0 to ISCO 9. These groups disting"
  },
  {
    "figure_id": "F230",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "To examine occupational outcomes in greater detail, employment can be analysed using the International Standard Classification of Occupations (ISCO), which categorises jobs into major groups ranging from ISCO 0 to ISCO 9. These groups distinguish occupations b"
  },
  {
    "figure_id": "F231",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Note: Analysis are restricted to top destination countries with available data. professionals (ISCO 5), which together employ 44% of Greek-born women, compared with around 36% of men. By contrast, men are more frequently employed in craft-related and machine-o"
  },
  {
    "figure_id": "F232",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "In addition, Greek-born workers show higher shares than the native-born in food preparation assistants (2.1% compared with 0.5%), hospitality, retail and other services managers (2.4% versus 0.9%), and drivers and mobile plant operators (5.7% versus 3.4%). The"
  },
  {
    "figure_id": "F233",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Overqualification occurs when an individual's level of formal education exceeds the requirements of their occupation. It is measured as the share of tertiary-educated individuals employed in low- or medium-skilled jobs. Among migrants, qualifications, work exp"
  },
  {
    "figure_id": "F234",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "## Greece has the highest share of foreign-trained, native-born doctors in the OECD However, not all foreign-trained doctors are foreign-born. Many of these are in fact native-born citizens who obtained their first medical degree abroad before returning home f"
  },
  {
    "figure_id": "F235",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "There is also an important number of Greek-born doctors, whether trained in Greece or abroad, working in other OECD countries. The number of Greek-born migrant doctors has more than threefold since 2000/01, from about 2900 in 2000/01 to almost 10000 in 2020/21"
  },
  {
    "figure_id": "F236",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Note: Emigration rates are calculated as the number of migrant doctors in relation to the total number of doctors in the workforce of the origin country (residing abroad and in the country of origin). Intra-OECD migration patterns of doctors are complex. Figur"
  },
  {
    "figure_id": "F237",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "In line with the geographical distribution of the Greek diaspora, according to Eurostat data, over two-thirds of remittances originated from OECD countries in 2024. Over the past decade, remittances peaked in 2013, reaching EUR 607 million, likely in response "
  },
  {
    "figure_id": "F238",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3.22. In 2024, about two-thirds of all remittances to Greece originating from OECD countries came from the United States, the United Kingdom and Germany Note: Remittances include workers remittances and compensation of employees. Data for remittances fr"
  },
  {
    "figure_id": "F239",
    "report_id": "R013",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Note: Remittances include workers remittances and compensation of employees. Data for remittances from the United States are shown from 2016 onwards. Earlier years are not included due to methodological revisions and/or reporting inconsistencies in Eurostat's "
  },
  {
    "figure_id": "F240",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "## A brief overview of return migration in the post-war period Return migration has been a defining feature of Greece's modern migration history. After Greece recorded a net outflow of over 600 000 Greek citizens between 1951 and 1970, the following decade was"
  },
  {
    "figure_id": "F241",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "## Inflows of Greek citizens exceeded outflows in 2023 Since 2010, Greece has experienced significant net emigration of its citizens. According to Hellenic Statistical Authority (ELSTAT) estimates, annual outflows of Greek citizens consistently exceeded inflow"
  },
  {
    "figure_id": "F242",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "## Characteristics of return migrants The analysis in the following section draws on data from the Greek Population and Housing Censuses to examine the characteristics of return migration to Greece. The main reference point is the most recent census conducted "
  },
  {
    "figure_id": "F243",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "The analysis in the following section draws on data from the Greek Population and Housing Censuses to examine the characteristics of return migration to Greece. The main reference point is the most recent census conducted in 2021, which provides detailed infor"
  },
  {
    "figure_id": "F244",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Note: The bars for 2006, 2011, 2016, and 2021 are shown in grey because they do not represent full calendar years. In the 2011 Census, the reference window includes only arrivals from 10 May–31 December 2006 and 1 January–9 May 2011, while in the 2021 Census i"
  },
  {
    "figure_id": "F245",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "## Return migration is concentrated among younger adults Figure 4.4. A larger share of return migrants are men Greek return migrants by age and gender, 2021 and 2011 census The concentration of return migrants in the age group 20-39 captured in the 2021 data i"
  },
  {
    "figure_id": "F246",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "The concentration of return migrants in the age group 20-39 captured in the 2021 data is largely driven by returns reported as having occurred in the years immediately preceding enumeration, with especially strong representation of those aged 20-29. This marks"
  },
  {
    "figure_id": "F247",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "## Three in five return migrants have completed tertiary education Return migrants tend to be highly educated, with three in five (60%) having completed tertiary education (see Figure 4.6). This share exceeds that observed among Greek emigrants currently abroa"
  },
  {
    "figure_id": "F248",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Return migrants to Greece in the 2021 census were more highly educated than those arriving in earlier periods and captured in the 2011 census. Around $60\\%$ of returnees in the 2021 census held tertiary level degree, compared to around $45\\%$ among return migr"
  },
  {
    "figure_id": "F249",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Note: Primary education includes those who have started primary education but not completed it (ISCED 0-1). Similarly, secondary education includes those who have started secondary education but not completed it, as well as those who have completed post-second"
  },
  {
    "figure_id": "F250",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4.9. The most common countries of previous residence are Germany and the United Kingdom Country of previous residence of Greek return migrants, 2011 census and 2021 census ## Three in five return migrants settled in the regions of Attica and Central Mac"
  },
  {
    "figure_id": "F251",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Taken together, these findings highlight how return migration to Greece reflects both metropolitan concentration and diverse regional linkages. The growing share of returnees settling in the Athens metropolitan area suggests a strengthening pull toward the cou"
  },
  {
    "figure_id": "F252",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Return migrants in Greece overwhelmingly tend to resettle in the region in which they were born, and this tendency is more pronounced among more recently settled return migrants across all regions. Nationwide in 2021, the share of returnees living in their reg"
  },
  {
    "figure_id": "F253",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Understanding why Greek emigrants choose to return can help with interpreting broader mobility patterns and designing policies that effectively support reintegration. Return decisions often reflect a combination of personal, economic, and family considerations"
  },
  {
    "figure_id": "F254",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Across different regions of previous residence, the motivations for return reveal distinct patterns. Repatriation remains the predominant driver everywhere, but it is especially pronounced among returnees from Oceania (66%) and North America (65%), where long-"
  },
  {
    "figure_id": "F255",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4.13. Returns for work play a less prominent role among those returning from North America and Oceania Greek return migrants by reason for return migration and region of previous residence, 2021 census Figure 4.14. Repatriation was the most commonly cit"
  },
  {
    "figure_id": "F256",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Return migrants who arrived more recently are less likely to be economically active than those who returned earlier. Those who returned in 2016 show the highest level of labour force participation, at 70%, while labour force participation falls with year since"
  },
  {
    "figure_id": "F257",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "## Unemployment was most pronounced during the economic crisis Employment outcomes among Greek return migrants display clear cohort patterns that reflect both broader economic conditions and the time required for reintegration into the labour market. Earlier c"
  },
  {
    "figure_id": "F258",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Comparing return migrants with non-migrants provides important insight into how effectively returnees re-enter the Greek labour market and how this process evolves across the life course. The data show that return migrants are slightly more likely to be employ"
  },
  {
    "figure_id": "F259",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "## Educational attainment is a key determinant of labour market integration for Greek return migrants Figure 4.18. Unemployment rates are most pronounced among those returning during the onset of the economic crisis Unemployment rates of Greek return migrants,"
  },
  {
    "figure_id": "F260",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Note: Year since return to Greece is captured retrospectively in the 2011 and 2021 censuses. Upon a closer look at all returnees captured in the 2021 census, educational differentials are also evident across the broader population of economically active return"
  },
  {
    "figure_id": "F261",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4.20. Higher unemployment among more recent returnees suggests gradual labour market integration, with doctoral graduates experiencing the lowest adjustment barriers Unemployment rates of economically active Greek tertiary educated return migrants, ages"
  },
  {
    "figure_id": "F262",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "## Nearly half of all returnees work as professionals, while fewer than one in five non-migrants occupy professional roles Nearly half of all returnees work as professionals (47%), far exceeding the share among non-migrants (18%), reflecting the strong tertiar"
  },
  {
    "figure_id": "F263",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "## Almost half of return migrants in professional occupations are working in health, science, and engineering Among those employed in professional roles, return migrants are particularly concentrated in science and engineering (22%) and health professions (23%"
  },
  {
    "figure_id": "F264",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Note: For the purposes of this analysis, non-migrants are defined as Greek-born Greek citizens who reported never having lived abroad at the time of the census. Figure 4.23. Professional specialisation among return migrants differs slightly by time since retur"
  },
  {
    "figure_id": "F265",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Among Greek returnees recorded in the 2021 census, self-employment remains a relatively limited mode of labour-market engagement (see Figure 4.24). Return migrants who had been back in Greece for 3 to 5 years are more likely to be self-employed with personnel "
  },
  {
    "figure_id": "F266",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Note: The share of self employment is calculated as the number of self employed individuals divided by the total number of individuals in employment. The 2021 census period covers 23 October–31 December 2016 and 1 January–22 October 2021. As a result, 2016 and"
  },
  {
    "figure_id": "F267",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "## Among the inactive, return migrants are more likely to be students than those who never migrated Economic inactivity among return migrants provides additional insight into how their circumstances differ from those of non-migrants. Among inactive returnees, "
  },
  {
    "figure_id": "F268",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Only 55% view Greece positively or somewhat positively as a place to live. When asked what would encourage return, respondents emphasised more effective institutions, stronger labour-market meritocracy, and the modernisation of state structures, factors ranked"
  },
  {
    "figure_id": "F269",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Greece exhibits one of the highest rates of higher education enrolment among OECD and EU countries. More than half (51%) of young adults aged 20 to 24 in Greece are enrolled in tertiary education programmes, a figure significantly above the OECD average of jus"
  },
  {
    "figure_id": "F270",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5.2. Overqualification and unemployment rates of young professionals in Greece are above the EU/OECD averages Unemployment rate (Panel A) and overqualification among young tertiary educated (Panel B) (%), Greece and EU 27, 2024 A. Unemployment among ter"
  },
  {
    "figure_id": "F271",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Unemployment rate (Panel A) and overqualification among young tertiary educated (Panel B) (%), Greece and EU 27, 2024 A. Unemployment among tertiary educated, aged 25-34 B. Overqualification among youth aged 20-34 ## Greek students' enrolment in higher educati"
  },
  {
    "figure_id": "F272",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "When it comes to international student mobility, data show that among all tertiary students from Greece, the share of Greek students enrolled in higher education abroad has consistently remained above the OECD average and slightly above the EU averaged over th"
  },
  {
    "figure_id": "F273",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "The United Kingdom remains the leading destination country for Greek students, but other European countries are becoming increasingly attractive. Figure 5.4. The United Kingdom remains the leading destination country for Greeks undertaking tertiary studies abr"
  },
  {
    "figure_id": "F274",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Number of mobile students of Greek origin enrolled in tertiary education abroad, 2022 Figure 5.5. The United Kingdom experienced a sharp decline in Greek student enrolment in 2022 According to the National Statistical Institute of Bulgaria (2024[9]), Greece wa"
  },
  {
    "figure_id": "F275",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "According to the National Statistical Institute of Bulgaria (2024[9]), Greece was the leading country of origin among foreign students in Bulgarian higher education in the 2023/24 academic year, accounting for $21\\%$ of all international students, with most en"
  },
  {
    "figure_id": "F276",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5.7. Greek students' enrolment in bachelor's degrees has increased modestly in recent years At the bachelor's level, the United Kingdom dominates as the primary destination, hosting nearly one in three Greek undergraduates abroad (32%), followed by Türk"
  },
  {
    "figure_id": "F277",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "At the bachelor's level, the United Kingdom dominates as the primary destination, hosting nearly one in three Greek undergraduates abroad (32%), followed by Türkiye (12%) and the Netherlands (10%) (see Figure 5.8). For master's programmes, the pattern becomes "
  },
  {
    "figure_id": "F278",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5.9. Greek enrolment in bachelor's programmes abroad has been rising in the Netherlands and declining in the United Kingdom Figure 5.10. Bulgaria and the Netherlands are emerging as primary destinations for Greek students completing their master's degre"
  },
  {
    "figure_id": "F279",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5.9. Greek enrolment in bachelor's programmes abroad has been rising in the Netherlands and declining in the United Kingdom Figure 5.10. Bulgaria and the Netherlands are emerging as primary destinations for Greek students completing their master's degre"
  },
  {
    "figure_id": "F280",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5.10. Bulgaria and the Netherlands are emerging as primary destinations for Greek students completing their master's degree abroad ## The emigration of Greek doctoral holders In the absence of a single dataset that comprehensively tracks Greek researche"
  },
  {
    "figure_id": "F281",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "## The United States, the United Kingdom and Germany are the top destinations of Greek doctoral holders Based on DIOC 2020/21, more than 17 200 Greek doctorate holders were identified across OECD countries, not including the United Kingdom, for which a compara"
  },
  {
    "figure_id": "F282",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "The number of Greek PhD holders and the share of PhD holders as percentage (%) of total emigrants in destination countries hosting more than 150 Greek PhD holders, 2020/21 The age distribution of Greek PhD-holder emigrants shows a broad spread across the life "
  },
  {
    "figure_id": "F283",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "International mobility intentions are strongest among recent PhD graduates in science and technology Figure 5.13. About one in seven new Greek PhD holders intend to settle abroad Among PhD holders considering permanent settlement abroad, the largest shares are"
  },
  {
    "figure_id": "F284",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Among PhD holders considering permanent settlement abroad, the largest shares are found among those with degrees in natural sciences and engineering and technology, suggesting strong international mobility potential in science and technology fields (see Figure"
  },
  {
    "figure_id": "F285",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5.15. Continuation of research activity and pursuing one's academic career are the leading reasons for Greek PhD holders to settling abroad Figure 5.16. The United States, the United Kingdom, and Germany are the leading destinations of interest for Gree"
  },
  {
    "figure_id": "F286",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5.16. The United States, the United Kingdom, and Germany are the leading destinations of interest for Greek PhD holders intending to settle abroad Percentage distribution of new PhD holders by country of potential permanent settlement (as percentage of "
  },
  {
    "figure_id": "F287",
    "report_id": "R013",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Chapter 4, Figure 4.4), doctoral degree holders form a comparatively older return cohort reflecting the fact that highly educated emigrants tend to come back later in their careers, particularly given that many PhD students studying abroad are less likely to c"
  },
  {
    "figure_id": "F288",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Returns from other world regions were comparatively limited: 3% came from countries in Asia, 1% from Africa, and 1% from the Caribbean, Central, and South America, while returns from Oceania accounted for virtually none. ## Figure 5.18. Over four in five retur"
  },
  {
    "figure_id": "F289",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Among returning emigrants in 2021 with doctoral degrees, repatriation emerges as the predominant driver of return, accounting for 47% of all cases (see Figure 5.19). A further 29% cited work-related reasons, indicating that professional opportunities in Greece"
  },
  {
    "figure_id": "F290",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "The latter is particularly relevant for Greece, where reforms introduced after 2019 expanded the possibility for researchers to maintain foreign affiliations while being employed domestically, including dual or visiting appointments. As a result, affiliation-b"
  },
  {
    "figure_id": "F291",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Greek-origin scientists show some variation in their fields of work depending on whether they are based in Greece or abroad, although the overall disciplinary distribution remains broadly similar. Biomedical research is the most common field in both groups, bu"
  },
  {
    "figure_id": "F292",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "## Top-impact Greek-origin scientists are predominantly based abroad The authors also assign each scientist to a “subfield ranking” based on normalised citation counts (or citation impact measures) relative to peers within the same scientific domain. In practi"
  },
  {
    "figure_id": "F293",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "According to the survey, 28% of respondents rated the situation in Greece as “fair,” while the remainder were almost evenly split between more positive and more negative evaluations (Figure 5.23). Only around one in ten respondents viewed conditions as either "
  },
  {
    "figure_id": "F294",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5.23. A majority of surveyed Greek academics abroad have poor perceptions of Greek universities Respondents' aggregate perceptions of Greece and of Greek universities, 2024 Despite the concerns about the quality of the higher education sector in Greece,"
  },
  {
    "figure_id": "F295",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Despite the concerns about the quality of the higher education sector in Greece, a majority of respondents (59%) would consider working at a university in Greece in the next five years. Respondents in medicine (78%), arts (71%), and business (66%) were most li"
  },
  {
    "figure_id": "F296",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Note: The figure shows the share of respondents that answered “yes” to the question: “Would you consider working at a university in Greece in the next five years?” Share of respondents interested in moving to Greece in the next five years by current academic p"
  },
  {
    "figure_id": "F297",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Note: The figure shows the share of respondents that answered “yes” to the question: “Would you consider working at a university in Greece in the next five years?” Those in arts report the highest propensity to consider relocating, with 86% expressing interest"
  },
  {
    "figure_id": "F298",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "A closer examination of return intentions by location of undergraduate and graduate studies reveals that the proportion of individuals expressing a desire to return to Greece varies according to the country in which their degree was completed: 53% of those who"
  },
  {
    "figure_id": "F299",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "A closer examination of return intentions by location of undergraduate and graduate studies reveals that the proportion of individuals expressing a desire to return to Greece varies according to the country in which their degree was completed: 53% of those who"
  },
  {
    "figure_id": "F300",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "These findings of who leaves, who returns and under what conditions form the analytical basis for Chapter 6, which examines the policy tools available to Greece to enhance retention, strengthen engagement with the scientific diaspora and encourage the return o"
  },
  {
    "figure_id": "F301",
    "report_id": "R013",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5.28. Higher salaries are the top recommendation to incentivise the return of Greek academics from abroad Reservations and recommended changes for Greek universities by academics abroad, 2024 Recommendations for incentivising the return of Greek academi"
  },
  {
    "figure_id": "F302",
    "report_id": "R013",
    "label": "经合组织视觉摘要 1",
    "figure_type": "external_card",
    "context": "经合组织｜经合组织：希腊人才外流真相，不是流失，而是待激活的全球网络｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F303",
    "report_id": "R014",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Latvia is the first OECD country to adopt municipal-level attractiveness indicators to reinforce local development policy. While the OECD regional attractiveness framework was originally developed at the regional level, analysing development trajectories at a "
  },
  {
    "figure_id": "F304",
    "report_id": "R014",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## Box 2.1. Developing the attractiveness framework for Latvian regions and municipalities The OECD regional attractiveness framework $^{1}$ provides a comprehensive, systemic lens to help policymakers understand a territory's competitive position and resilien"
  },
  {
    "figure_id": "F305",
    "report_id": "R014",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## Box 2.2. Identifying territorial strengths, constraints and policy trade-offs: The case of Saldus Municipality Saldus municipality performs strongly in environmental and cultural dimensions, with a tree cover rate of 67% (EU median of 32%) and strong perfor"
  },
  {
    "figure_id": "F306",
    "report_id": "R014",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "A common pattern in Latvia is the presence of strong natural and cultural assets that are not yet fully converted into tourism demand and wider local value. This is particularly important for regions with more limited economic performance, as OECD evidence ind"
  },
  {
    "figure_id": "F307",
    "report_id": "R014",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## Box 2.3. Leveraging territorial complementarities through inter-municipal co-operation: The case of Jelgava and Bauska municipalities Differences in multidimensional measures help highlight potential complementarities between the two municipalities. Strengt"
  },
  {
    "figure_id": "F308",
    "report_id": "R014",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Differences in multidimensional measures help highlight potential complementarities between the two municipalities. Strengthening co-ordination between Jelgava and Bauska, particularly in areas such as transport connectivity, spatial planning and housing devel"
  },
  {
    "figure_id": "F309",
    "report_id": "R014",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Analysis of the education sector in Latvia exemplifies the use of the attractiveness framework to monitor development trajectories. In particular, education indicators within the framework reveal an absolute improvement in tertiary (higher-level) education att"
  },
  {
    "figure_id": "F310",
    "report_id": "R014",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## Box 2.5. Monitoring regions' progress over time: Example from educational indicators The analysis of education indicators highlights the importance of combining temporal and comparative perspectives when assessing territorial performance. As shown in Figure"
  },
  {
    "figure_id": "F311",
    "report_id": "R014",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Indicators on access to schools have deteriorated over time. As shown in Figure 2.8.A, all municipalities have experienced increases in their average travel time to the primary schools between 2020 and 2023, with particularly high increments in the easternmost"
  },
  {
    "figure_id": "F312",
    "report_id": "R014",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2.9. Travel times to nearest schools B. Relative to EU median 2023 (Times) Note: Data are provided at a 1 km × 1 km grid resolution and were aggregated by municipality using population weights. This provides the possibility of compare updated boundaries"
  },
  {
    "figure_id": "F313",
    "report_id": "R014",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "At the subnational level, regional and local development programmes are prepared by planning regions and municipal governments, respectively. They are required to demonstrate clear alignment with national-level strategic priorities, and set out region or munic"
  },
  {
    "figure_id": "F314",
    "report_id": "R014",
    "label": "经合组织视觉摘要 1",
    "figure_type": "external_card",
    "context": "经合组织｜经合组织：拉脱维亚地方经济，真正的隐形资产，不是GDP而是森林和博物馆｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F315",
    "report_id": "R015",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "\\- Implementing, monitoring, evaluating and communicating the results: finally, the anti-fraud strategy should include a robust monitoring and evaluation framework to assess progress to achieving strategic objectives and inform updates or revisions to the anti"
  },
  {
    "figure_id": "F316",
    "report_id": "R015",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "The 2026 OECD Anti-Corruption and Integrity Outlook shows that countries are increasingly adopting dedicated frameworks to fight fraud, with approaches varying from integrating anti-fraud objectives in existing anti-corruption and integrity frameworks to adopt"
  },
  {
    "figure_id": "F317",
    "report_id": "R015",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "The 2026 OECD Anti-Corruption and Integrity Outlook shows that countries are increasingly adopting dedicated frameworks to fight fraud, with approaches varying from integrating anti-fraud objectives in existing anti-corruption and integrity frameworks to adopt"
  },
  {
    "figure_id": "F318",
    "report_id": "R015",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1.1. Anti-fraud strategies in OECD Members/Partners & EU Members and candidate countries Note: Underlined countries in “EU Members and EU candidate countries” are candidates for membership to the European Union. The OECD Secretariat conducted research o"
  },
  {
    "figure_id": "F319",
    "report_id": "R015",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## 1.2.1. Embedding M&E in the strategy cycle: objectives, implementation planning, and intervention logic Monitoring and evaluation are most effective when they are embedded in the design phase of an anti-fraud strategy, rather than introduced at implementati"
  },
  {
    "figure_id": "F320",
    "report_id": "R015",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "\\- Outcome indicators measure the extent to which actions under an anti-fraud strategy are having the desired short- and medium-term effects, such as improved inter-institutional co-operation or increased use of whistleblowing channels. Outcome indicators shou"
  },
  {
    "figure_id": "F321",
    "report_id": "R015",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "\\- scheduling the mid-term evaluation at a time when it will still be possible to make a course correction if the strategy is not meeting its targets and/or broader objectives • ensuring that there will be enough funds at the end of the project to conduct the "
  },
  {
    "figure_id": "F322",
    "report_id": "R015",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Monitoring is most likely to be useful and effective when it is prioritised early and embedded in a strategy cycle from the beginning (Johnsøn and Søreide, 2013[4]). Early planning supports the development of effective baselines (before implementation) assessm"
  },
  {
    "figure_id": "F323",
    "report_id": "R015",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "This is applied to their national instruments, including the National anti-corruption policy. CONVEAL has a monitoring sheet which includes various sections such as the programme's description, results, coverage and industry analysis. Specifically, the results"
  },
  {
    "figure_id": "F324",
    "report_id": "R015",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Taking into consideration the comments from the respective programme, the CONEVAL will finalise the report is issued. The evaluation unit will publish the monitoring and evaluation report. They will also send it to the corresponding bodies included in the repo"
  },
  {
    "figure_id": "F325",
    "report_id": "R015",
    "label": "经合组织视觉摘要 1",
    "figure_type": "external_card",
    "context": "经合组织｜经合组织：5万亿美元欺诈损失背后，经合组织揭示战略评估缺失｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F326",
    "report_id": "R016",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "\\- In Estonia, the number of ECEC facilities per 1 000 children of ECEC age is similar to that of primary care facilities per 1 000 children of primary-school age, with figures ranging from 5.1 to 9.2 facilities per 1 000 children for ECEC and from 3.0 to 9.5 "
  },
  {
    "figure_id": "F327",
    "report_id": "R016",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "\\- Estonia, as a sparsely populated country, has a relatively high number of PES centres per capita, counting around 3 centres per 100 000 working-age individuals. These centres are spread relatively evenly across the different types of territories, with $26\\%"
  },
  {
    "figure_id": "F328",
    "report_id": "R016",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "## Figure 3. Travel times to the nearest ECEC facility and primary school are longer in rural areas than in cities and towns by walking and public transport, but similar by driving Travel times to the nearest ECEC facility and primary school for the median use"
  },
  {
    "figure_id": "F329",
    "report_id": "R016",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "## Figure 3. Travel times to the nearest ECEC facility and primary school are longer in rural areas than in cities and towns by walking and public transport, but similar by driving Travel times to the nearest ECEC facility and primary school for the median use"
  },
  {
    "figure_id": "F330",
    "report_id": "R016",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Travel times to the nearest ECEC facility and primary school for the median user by transport mode and degree of urbanisation, in Estonia and the Netherlands Panel A: Estonia Panel B: The Netherlands Note: For the Netherlands, results are not reported for rura"
  },
  {
    "figure_id": "F331",
    "report_id": "R016",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Panel A: Estonia Panel B: The Netherlands Note: For the Netherlands, results are not reported for rural areas far from cities because only a very small share of the population lives in areas of this this category. ## 4.1.2. For short travel times, competitive "
  },
  {
    "figure_id": "F332",
    "report_id": "R016",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Disparities in competitive accessibility depend on the travel time considered. At very short travel times, the indicator is zero, indicating that no facility can be reached (see Figure 4). Once users reach the median travel times shown in Figure 3 for every se"
  },
  {
    "figure_id": "F333",
    "report_id": "R016",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4. In Estonia, competitive accessibility levels are much higher in cities at short travel times, but converge across area types at longer travel times Variation in competitive accessibility by travel time across degrees of urbanisation, service type and"
  },
  {
    "figure_id": "F334",
    "report_id": "R016",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Variation in competitive accessibility by travel time across degrees of urbanisation, service type and transport mode, in Estonia. Panel A: Walking Panel B: Public transport ## 4.1.3. The case for applying travel time thresholds that vary by the degree of urba"
  },
  {
    "figure_id": "F335",
    "report_id": "R016",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Panel A: Walking Panel B: Public transport ## 4.1.3. The case for applying travel time thresholds that vary by the degree of urbanisation A key take-away from these results is that disparities in competitive accessibility across areas with different degrees of"
  },
  {
    "figure_id": "F336",
    "report_id": "R016",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "In both countries, the effect of public transport on accessibility differs across types of areas: in cities and towns and semi-dense areas, public transport has the effect of reducing the share of children in a situation of double penalty, indicating that it c"
  },
  {
    "figure_id": "F337",
    "report_id": "R016",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5. In the accessibility to primary schools, many children in cities face short travel times but lower competitive accessibility Share of primary school children facing a double reward, trade-off, or double penalty in their access to primary schools, by "
  },
  {
    "figure_id": "F338",
    "report_id": "R016",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Panel A: Estonia Panel B: The Netherlands From a policy perspective, children who face a double penalty deserve particular attention, and LAUs with high shares of children facing a double penalty may be considered as offering relatively poor service accessibil"
  },
  {
    "figure_id": "F339",
    "report_id": "R016",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Panel A: Estonia Panel B: The Netherlands From a policy perspective, children who face a double penalty deserve particular attention, and LAUs with high shares of children facing a double penalty may be considered as offering relatively poor service accessibil"
  },
  {
    "figure_id": "F340",
    "report_id": "R016",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "\\- In the Netherlands, spatial variation in the share of children facing a double penalty is much lower, and the shares are lower throughout (Figure 6, Panel B). In most of the country, less than $15\\%$ of children in a LAU face a double penalty, though the va"
  },
  {
    "figure_id": "F341",
    "report_id": "R016",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Figure 6. In Estonia, spatial variation is large in the share of children facing a double penalty of above-median travel times and below-median competitive accessibility Percentage of children facing a double penalty of above-median travel times and below-medi"
  },
  {
    "figure_id": "F342",
    "report_id": "R016",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "## In rural Estonia, a sizeable share of children does not achieve good competitive accessibility within a 40-50-minute walk or public transport journey Estonia displays a strong urban-rural gradient in its transport poverty measure. In cities, practically eve"
  },
  {
    "figure_id": "F343",
    "report_id": "R016",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "Figure 8. In most LAUs, driving times to the closest PES facility are shorter than 30 minutes for the median person, both in Estonia and the Netherlands Travel times to the closest PES facility by motor vehicle for the median person, by LAU, in Estonia and the"
  },
  {
    "figure_id": "F344",
    "report_id": "R016",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Looking beyond the median user and considering the entire distribution of travel times, Estonia reveals persistently shorter driving times than the Netherlands across all types of LAUs. This is illustrated, for example, by comparing the shares of people who ca"
  },
  {
    "figure_id": "F345",
    "report_id": "R016",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure 9. Only few people in Estonia and the Netherlands are located further than a 20-minute drive from a PES centre in cities, or a 40-minute drive in rural areas Share of population with access to a PES facility by motor vehicle, by degree of urbanisation a"
  },
  {
    "figure_id": "F346",
    "report_id": "R016",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "The travel time gap between driving and public transport closely relates to the degree of urbanisation. In rural areas, sparse networks and infrequent service typically imply long public transport journeys. As a result, the time “penalty” from using public tra"
  },
  {
    "figure_id": "F347",
    "report_id": "R016",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "Looking beyond the median user, public transport is often not a viable option for those with relatively lower accessibility even outside of rural areas. Within cities, the large majority of users are within a 40-minute journey to the closest PES centre by publ"
  },
  {
    "figure_id": "F348",
    "report_id": "R016",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "For people with the lowest service accessibility, access to a motor vehicle consequently cuts travel times by a substantial margin relative to the use of public transport. This is illustrated in Figure 11, which directly compares travel times by motor vehicle "
  },
  {
    "figure_id": "F349",
    "report_id": "R016",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure C.2. Accessibility by walking is similar across area types, but for public transport disparities arise between cities and towns and rural areas at longer travel times Variation in competitive accessibility by travel time for the median child across LAUs"
  },
  {
    "figure_id": "F350",
    "report_id": "R016",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Variation in competitive accessibility by travel time for the median child across LAUs with a certain degree of urbanisation, by service type and transport mode, in the Netherlands Panel A: Walking Panel B: Public transport Note: The lines show the competitive"
  },
  {
    "figure_id": "F351",
    "report_id": "R016",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Panel A: Walking Panel B: Public transport Note: The lines show the competitive accessibility for ECEC and primary schools for the median child across areas with a certain degree of urbanisation for walking and public transportation and various travel time thr"
  },
  {
    "figure_id": "F352",
    "report_id": "R016",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Note: The lines show the competitive accessibility for ECEC and primary schools for the median child across areas with a certain degree of urbanisation for walking and public transportation and various travel time thresholds. For comparable results for Estonia"
  },
  {
    "figure_id": "F353",
    "report_id": "R016",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure C.3. In the accessibility of ECEC, many children in cities face short travel times but lower competitive accessibility Share of ECEC-aged children facing a double reward, trade-off, or double penalty in their access to ECEC facilities, by country, degre"
  },
  {
    "figure_id": "F354",
    "report_id": "R016",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Share of ECEC-aged children facing a double reward, trade-off, or double penalty in their access to ECEC facilities, by country, degree of urbanisation, and transport mode Panel A: Estonia Panel B: The Netherlands Note: The bars show the percentage of children"
  },
  {
    "figure_id": "F355",
    "report_id": "R016",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Panel A: Estonia Panel B: The Netherlands Note: The bars show the percentage of children who face a double reward, a trade-off or a double penalty situation in access to ECEC facilities across degrees of urbanisation. The classification compares each child's t"
  },
  {
    "figure_id": "F356",
    "report_id": "R016",
    "label": "经合组织视觉摘要 1",
    "figure_type": "external_card",
    "context": "经合组织｜经合组织：中国城镇化启示，服务公平不是缩短距离，而是匹配容量｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F357",
    "report_id": "R017",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "This report builds on the OECD Development Centre's Man Enough? Measuring Masculine Norms to Promote Women's Empowerment, which proposed a unique framework for identifying and measuring norms of restrictive masculinities across countries at different levels of"
  },
  {
    "figure_id": "F358",
    "report_id": "R017",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "One of the report's most policy-relevant findings is that restrictive norms of masculinities are sustained not only by what individuals believe, but also by what they think others believe. In Côte d'Ivoire, respondents systematically overestimate men's support"
  },
  {
    "figure_id": "F359",
    "report_id": "R017",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "The report shows that restrictive masculinities are a key, yet often overlooked, constraint on women's economic empowerment. Norms that position men as primary breadwinners, protectors and decision makers, and women as dependants responsible for unpaid care an"
  },
  {
    "figure_id": "F360",
    "report_id": "R017",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Panel B. Reason why men should not do UCDW This dynamic is visible in unpaid care and domestic work, where women perform most of the work and many people continue to view it as women's responsibility (Figure 1.3). Figure 1.3. Women do most unpaid care and dome"
  },
  {
    "figure_id": "F361",
    "report_id": "R017",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Gender based violence remains widespread, recurrent and largely underreported in both Côte d'Ivoire and Senegal, despite progress in legal frameworks and in holistic service provision for survivors, including shelters, legal aid and medical care. Available dat"
  },
  {
    "figure_id": "F362",
    "report_id": "R017",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## Box 2.1. Data collection and analysis on masculinities in Côte d'Ivoire Data were collected through a nationally representative household survey conducted by Côte d'Ivoire's National Statistics Office (ANStat) between September and October 2025. The survey "
  },
  {
    "figure_id": "F363",
    "report_id": "R017",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "The OECD's Masculinities Index offers unique insights into the state of masculine norms. Developed based on the OECD ten-norm framework on restrictive masculinities (OECD, 2021[6]), it has been calculated for the first time for Côte d'lvoire. The index is a us"
  },
  {
    "figure_id": "F364",
    "report_id": "R017",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## Restrictive masculinities are widespread – but they are neither uniform nor fully uncontested General support for gender norms that enshrine men's dominant position over women remains high in Côte d'Ivoire. In other words, restrictive masculinities are deep"
  },
  {
    "figure_id": "F365",
    "report_id": "R017",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Differences in index scores by gender are relatively small. Men consistently express higher levels of acceptance of restrictive norms than women, but such norms are upheld by both men and women, with Masculinities Index scores of 59 and 54, respectively. $^{1}"
  },
  {
    "figure_id": "F366",
    "report_id": "R017",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Norms positioning men as breadwinners and household decision-makers are the most prevalent forms of restrictive masculinities in Côte d'Ivoire. For instance, 96% of the population agree that men's most important role is to meet the family's financial needs, an"
  },
  {
    "figure_id": "F367",
    "report_id": "R017",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## Support for restrictive masculinities follows educational inequalities and longstanding value systems This section examines how individual characteristics – such as education, age, religion, ethnicity or economic situation – help explain differences in adhe"
  },
  {
    "figure_id": "F368",
    "report_id": "R017",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## A “silent gap” between personal beliefs and social expectations creates space for change Data from Côte d'Ivoire reveal widespread misperceptions about masculinities. Most strikingly, people systematically overestimate both men's support for and women's opp"
  },
  {
    "figure_id": "F369",
    "report_id": "R017",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Restrictive masculinity norms can generate significant psychological pressure, particularly when men feel unable to meet entrenched expectations such as providing financially for their families. Research shows that perceived threats to masculinity can increase"
  },
  {
    "figure_id": "F370",
    "report_id": "R017",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Evidence from Côte d'Ivoire aligns with these findings and highlights the central role of the breadwinner norm in shaping men's well-being. More than 90% of men report that they would feel stressed or anxious if they were unable to provide financially for thei"
  },
  {
    "figure_id": "F371",
    "report_id": "R017",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Stakeholders also described the role of religious and cultural frames in legitimising male dominance, not necessarily through religion itself, but through selective interpretations and the blending of discriminatory traditions with religious principles. Respon"
  },
  {
    "figure_id": "F372",
    "report_id": "R017",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Structural factors can also reinforce restrictive masculine norms and hinder change. Economic insecurity, unemployment and rising living costs in urban centres were identified as factors that heighten men's, and particularly young men's, anxiety about meeting "
  },
  {
    "figure_id": "F373",
    "report_id": "R017",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "As highlighted in Chapter 2, social norms depend not only on personal beliefs but also on what people think others believe and expect. Senegal's workshop-based evidence suggests that participants often perceive wider society as more supportive of restrictive n"
  },
  {
    "figure_id": "F374",
    "report_id": "R017",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "These data are complementary but not fully comparable. Differences in methodology, definitions, indicators, and reference periods mean that certain estimates, e.g. time spent on unpaid care and domestic work, may not be fully comparable based on survey design "
  },
  {
    "figure_id": "F375",
    "report_id": "R017",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "## Women continue to face major barriers to full economic empowerment Côte d'Ivoire and Senegal both face persistent gender gaps in labour force participation. At 15 percentage points in Côte d'Ivoire and 28 percentage points in Senegal, gender gaps are among "
  },
  {
    "figure_id": "F376",
    "report_id": "R017",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Despite formal equal pay provisions in the Labour Codes of both Côte d'Ivoire and Senegal, which mandate equal remuneration for work of equal value regardless of gender, women also continue to face substantial wage disparities. Gender pay gaps are estimated at"
  },
  {
    "figure_id": "F377",
    "report_id": "R017",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4.2. A large share of women in Côte d'Ivoire and Senegal is employed in vulnerable forms of employment Panel A. Type of employment among those working in Côte d'Ivoire Panel B. Type of employment among those working in Senegal Note: Responses in Panels "
  },
  {
    "figure_id": "F378",
    "report_id": "R017",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Restrictive masculinities can also shape the type of work considered appropriate for women and men. Norms that associate leadership with masculine traits may bias hiring and promotion in favour of men, discourage women from pursuing positions of authority, and"
  },
  {
    "figure_id": "F379",
    "report_id": "R017",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Restrictive masculinities can also shape the type of work considered appropriate for women and men. Norms that associate leadership with masculine traits may bias hiring and promotion in favour of men, discourage women from pursuing positions of authority, and"
  },
  {
    "figure_id": "F380",
    "report_id": "R017",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "## Women continue to bear a disproportionate share of unpaid care and domestic work Mirroring global patterns, women in Côte d'Ivoire and Senegal spend significantly more time than men on unpaid care and domestic tasks. Globally, women spend on average 2.6 tim"
  },
  {
    "figure_id": "F381",
    "report_id": "R017",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4.5. There are significant gender gaps in unpaid care and domestic work in all regions of Côte d'Ivoire Panel A. Regional distribution of household tasks and care in Côte d'Ivoire in terms of hours spent Panel B. Regional variation in the time women spe"
  },
  {
    "figure_id": "F382",
    "report_id": "R017",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4.5. There are significant gender gaps in unpaid care and domestic work in all regions of Côte d'Ivoire Panel A. Regional distribution of household tasks and care in Côte d'Ivoire in terms of hours spent Panel B. Regional variation in the time women spe"
  },
  {
    "figure_id": "F383",
    "report_id": "R017",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Panel B. Regional variation in the time women spend on household tasks and care relative to men in Côte d'Ivoire Note: In Côte d'Ivoire, household tasks (HH tasks) include activities such as cooking, cleaning, house repairs, laundry, and the collection of wate"
  },
  {
    "figure_id": "F384",
    "report_id": "R017",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "## Restrictive gender norms reinforce the unequal distribution of unpaid care and domestic work The unequal distribution of unpaid care and domestic work is not only a matter of household arrangements or service provision; it is also sustained by restrictive n"
  },
  {
    "figure_id": "F385",
    "report_id": "R017",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Social expectations regarding men's contribution vary considerably by task. Men in Côte d'Ivoire are expected to contribute most regularly to supervising children's homework, with $43\\%$ of respondents saying men should do this every day and a further $37\\%$ s"
  },
  {
    "figure_id": "F386",
    "report_id": "R017",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "empowerment if women cannot decide how resources are used or benefit from them. In Côte d'Ivoire and Senegal, restrictive masculinities can limit this agency by reinforcing men's authority as household heads, final decision makers and primary controllers of in"
  },
  {
    "figure_id": "F387",
    "report_id": "R017",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Gender gaps in decision-making persist in Côte d'Ivoire and Senegal, particularly within the household. Survey data from Côte d'Ivoire show that around 60% of employed women report being able to take important decisions in their work, compared with 69% of men "
  },
  {
    "figure_id": "F388",
    "report_id": "R017",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Significant gender gaps in asset ownership persist in Côte d'Ivoire and in Senegal, particularly in relation to land. In Côte d'Ivoire, 25% of men report owning or co-owning land, compared with 9% of women. In Senegal, the corresponding shares are 23% of men a"
  },
  {
    "figure_id": "F389",
    "report_id": "R017",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Nationally representative data from Côte d'Ivoire show that GBV is widespread and follows clear gendered patterns. While both women and men report experiencing violence, women are more frequently reported as victims, whereas men are more frequently reported as"
  },
  {
    "figure_id": "F390",
    "report_id": "R017",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5.1. Prevalence of intimate-partner violence varies by region and type of abuse in Côte d'Ivoire Panel A. IPV lifetime prevalence by region and gender Panel B. Types of IPV experienced among victims/survivors over lifetime Note: Gender differences by re"
  },
  {
    "figure_id": "F391",
    "report_id": "R017",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Information on perpetrators of violence further underscores the gendered nature of GBV. In Côte d'Ivoire, 20% of men and 15% of women report having committed some form of violence against a spouse or partner in the past 12 months. While both women and men repo"
  },
  {
    "figure_id": "F392",
    "report_id": "R017",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Available data from Senegal also point to high levels of violence against women, although the estimates are not directly comparable with those from Côte d'Ivoire or latest available SDG data because of differences in data sources, definitions and reference per"
  },
  {
    "figure_id": "F393",
    "report_id": "R017",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Comparable patterns are observed in Côte d'Ivoire. Afrobarometer data indicate that the main perceived reasons for not reporting violence are a preference for amicable settlement (34%), fear of retaliation in case of reporting (26%), shame (17%), lack of knowl"
  },
  {
    "figure_id": "F394",
    "report_id": "R017",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Acceptance of physical IPV also varies across regions, suggesting that violence is embedded in local normative environments and that the social tolerance of abuse is stronger in some settings than in others. For instance, in Côte d'Ivoire regional rates range "
  },
  {
    "figure_id": "F395",
    "report_id": "R017",
    "label": "经合组织视觉摘要 1",
    "figure_type": "external_card",
    "context": "经合组织｜经合组织：科特迪瓦数据颠覆认知，年轻男性反而更支持传统性别角色｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F396",
    "report_id": "R018",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## Box 1.1. Macroeconomic assumptions and policy environment Projections of economic indicators are based on the latest forecasts published by the IMF World Economic Outlook from October 2025, complemented by longer-term projections from Oxford Economics and t"
  },
  {
    "figure_id": "F397",
    "report_id": "R018",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Real global reference prices increase across all major commodities, reflecting higher production costs, particularly for energy, fertilisers, and feed, combined with persistently inelastic food demand. While price increases are already projected for 2026, they"
  },
  {
    "figure_id": "F398",
    "report_id": "R018",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Relative to the baseline, the scenario implies a marked slowdown in economic activity. This affects agrifood systems through two principal channels: reduced demand growth and higher production costs. Elevated energy prices increase fertiliser costs, reducing i"
  },
  {
    "figure_id": "F399",
    "report_id": "R018",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## Production impacts: Concentration of losses in crops Across income groups, the adverse scenario reduces cereal production most sharply in low-income countries, where output declines by about 2.3% in 2026 and 1.7% in 2027 (Figure 1.4 panel b). These losses r"
  },
  {
    "figure_id": "F400",
    "report_id": "R018",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "The scenario leads to declining or stagnating food consumption across all income groups, but the nature of the adjustment differs markedly. In low-income countries, reduced income growth and higher food prices drive broad consumption declines, with larger redu"
  },
  {
    "figure_id": "F401",
    "report_id": "R018",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## 1.2.1. Continued long-term decline in real global agricultural commodity prices hinges on sustained investments into productivity improvements Agricultural commodity markets remain inherently uncertain given their dependency on natural production conditions"
  },
  {
    "figure_id": "F402",
    "report_id": "R018",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "It is important to recognise that the transmission of price signals between international markets and local producers and consumers varies widely across countries. Factors such as transport and logistics costs, exchange rate movements, trade policies, and the "
  },
  {
    "figure_id": "F403",
    "report_id": "R018",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "The constructed agricultural labour productivity is a gross measure of value added per worker and does not distinguish between skilled and unskilled workers. As a result, it may mask important compositional differences in the workforce and may not necessarily "
  },
  {
    "figure_id": "F404",
    "report_id": "R018",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Agricultural labour productivity exhibits the widest cross-country differences of any economic sector, making it a central factor in understanding global income inequality (Gollin, Lagakos and Waugh, 2014[10]). In the base period, real agricultural GDP per sec"
  },
  {
    "figure_id": "F405",
    "report_id": "R018",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Recent analytical work also suggests that productivity growth alone is unlikely to deliver inclusive rural transformation. A broader agrifood systems perspective is needed, one that considers the diversity of employment opportunities beyond primary agriculture"
  },
  {
    "figure_id": "F406",
    "report_id": "R018",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "The analysis indicates that variability is more pronounced in low-income countries compared to other country. If historical variability were to persist over the projection period, at the global level there would be a 25% probability that income per worker fall"
  },
  {
    "figure_id": "F407",
    "report_id": "R018",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Over the next decade, the gross value of agricultural production (in constant USD) for commodities covered in the Outlook is projected to increase by 13.3%, reaching USD 4.01 trillion by 2035. Livestock production is expected to lead this growth, expanding by "
  },
  {
    "figure_id": "F408",
    "report_id": "R018",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Ruminant and other livestock production are projected to account for 76.6% of the global increase in direct agricultural GHG emissions, while application of synthetic fertilisers, another significant"
  },
  {
    "figure_id": "F409",
    "report_id": "R018",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "As diets evolve in these regions, demand for food is shifting beyond staples toward more livestock and fish-based products. Growing domestic production of these commodities is expected to significantly boost demand for feed crops. As a result, a growing share "
  },
  {
    "figure_id": "F410",
    "report_id": "R018",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## 1.3.2. As incomes grow, dietary patterns are expected to further diversify in middle-income countries over the next decade Figure 1.15. Projected evolution of dietary patterns While these projections point to continued average consumption growth, they large"
  },
  {
    "figure_id": "F411",
    "report_id": "R018",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "While these projections point to continued average consumption growth, they largely reflect aggregate developments and may mask important distributional challenges, particularly in urban and peri-urban settings. A growing share of the population in low- and mi"
  },
  {
    "figure_id": "F412",
    "report_id": "R018",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Agricultural commodities are used beyond traditional food and feed purposes, with biofuels representing the most widespread non-food application. The value of global biofuel use is projected to grow at an average 1.3% p.a., driven by rising demand for transpor"
  },
  {
    "figure_id": "F413",
    "report_id": "R018",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## 1.4.1. Trade flows between surplus and deficit regions are projected to grow Global agri-food trade has expanded significantly over recent decades, particularly following the WTO Agreement on Agriculture (1995) and China's accession to the WTO (2001). The s"
  },
  {
    "figure_id": "F414",
    "report_id": "R018",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1.19 shows the share of exports in total production, and the share of imports in total consumption for selected regions. These indicators reveal important differences in the role of trade between regions. Major producing regions such as North America, a"
  },
  {
    "figure_id": "F415",
    "report_id": "R018",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "In Near East and North Africa, where population is growing strongly but where limited resources are an obstacle to production expansion, imports play a significant role in complementing domestic food and feed production. The share of imports in total consumpti"
  },
  {
    "figure_id": "F416",
    "report_id": "R018",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "In Figure 1.20, trade intensity is measured as the ratio of total trade (imports plus exports) to overall market size, defined as the sum of production and total domestic use. This captures the degree to which a country is integrated into global agri-food mark"
  },
  {
    "figure_id": "F417",
    "report_id": "R018",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## 2.3.1. Consumption ## Asian countries will lead consumption growth Global cereal consumption is projected to continue expanding over the coming decade driven by population growth, rising per-capita food demand, and increasing feed demand for livestock produ"
  },
  {
    "figure_id": "F418",
    "report_id": "R018",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## Asian countries will lead consumption growth Global cereal consumption is projected to continue expanding over the coming decade driven by population growth, rising per-capita food demand, and increasing feed demand for livestock production. Food use will r"
  },
  {
    "figure_id": "F419",
    "report_id": "R018",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Between 49% and 64% of global cereal consumption is projected to occur in the five largest consuming countries for each commodity by 2035 (Figure 2.2), indicating a lower degree of concentration than for production. Total cereal use is projected to increase by"
  },
  {
    "figure_id": "F420",
    "report_id": "R018",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## 2.3.2. Production ## Yield improvements sustain production growth Figure 2.3. Regional cereal yields Note: The presented yields were calculated as total production divided by total harvested area in the corresponding region. In the rice panel, \"Oceania\" ref"
  },
  {
    "figure_id": "F421",
    "report_id": "R018",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Global average yields are projected to grow by around 0.9% p.a. in the next decade, slightly faster than in the previous decade, reaching 4.2 t/ha by 2035. Continued advances in crop genetics, improved farm management practices and more efficient input use are"
  },
  {
    "figure_id": "F422",
    "report_id": "R018",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "International trade plays an important role in balancing regional differences between cereal production and consumption. During the base period, global cereal trade accounted for 17% of total production. This share is projected to increase to 18% by 2035 as de"
  },
  {
    "figure_id": "F423",
    "report_id": "R018",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2.5. Cereal trade as a percentage of production and consumption Note: The presented estimates include intra-trade except for the European Union. Export markets remain partially segmented by wheat quality. The United States, Canada, Australia and the Eur"
  },
  {
    "figure_id": "F424",
    "report_id": "R018",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## 2.3.4. Prices Nominal prices for cereals are projected to continue their upward medium-term trends (Figure 2.7). Wheat prices are expected to reach about 307 USD/t by 2035. Maize and other coarse grain prices are projected to reach around 236 USD/t and 256 "
  },
  {
    "figure_id": "F425",
    "report_id": "R018",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "## Slowing global oilseed crush and limited growth in palm oil production Globally, the crushing of soybeans and other oilseeds into meal (cake) and oil dominates their total usage at around 90%. The demand for crush will increase slightly faster than that for"
  },
  {
    "figure_id": "F426",
    "report_id": "R018",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Note: LDC: least developed country."
  },
  {
    "figure_id": "F427",
    "report_id": "R018",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "## Feed demand is slowing, shaped by developments in China The protein meal content of soybeans is about 80% while for other oilseeds this share is 50-60%. Protein meal is almost exclusively used as feed and its consumption is projected to continue to grow at "
  },
  {
    "figure_id": "F428",
    "report_id": "R018",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "The production of soybeans is projected to grow by 0.9% p.a., compared to 2.3% p.a. over the last decade. Growth will be dominated by yield increases, accounting for about 70% of production growth. Soybeans have the advantage of growing fast, which allows for "
  },
  {
    "figure_id": "F429",
    "report_id": "R018",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Exports of soybeans originate predominately from Brazil and the United States. Brazil is the largest global exporter of soybeans, with steady growth in its export capacity, and is projected to account for 61% of total global exports of soybean by 2035 (Figure "
  },
  {
    "figure_id": "F430",
    "report_id": "R018",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "## 3.3.6. Prices Real prices will remain under pressure over the next decade Figure 3.6. Evolution of world oilseed prices ## 3.4. Risks and uncertainties ## Environmental concerns influence global oilseed supply chains"
  },
  {
    "figure_id": "F431",
    "report_id": "R018",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "## Environmental concerns influence global oilseed supply chains Yields for major producers of palm oil and for some major suppliers of rapeseed have fallen or grown slowly during the last decade (Figure 3.7). There are many reasons for this development: a sig"
  },
  {
    "figure_id": "F432",
    "report_id": "R018",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "With the projected rapid growth in population and income in Asia, and in population in Africa, the two regions are expected to account for virtually all of the increase in global demand compared to the reference period (October 2023-September 2025), at 76% and"
  },
  {
    "figure_id": "F433",
    "report_id": "R018",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "## Expanded processing capacity underpins production growth Global sugar production is expected to grow from 181 Mt during the base period to 203 Mt by 2035, 60% of the growth will come from Asia and 30% from Latin America (Figure 4.2). Asia will remain the le"
  },
  {
    "figure_id": "F434",
    "report_id": "R018",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "## Biofuel expansion intensifies competition for sugarcane During the last decade, 81% of world sugar crops were used to produce sugar, but this share is expected to decline slightly to 80% by 2035. In the major sugarcane-producing countries, support for biofu"
  },
  {
    "figure_id": "F435",
    "report_id": "R018",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "During the last decade, imports supplied 36% of global sugar consumption. This share is expected to decline marginally by 2035 to 34%, reflecting strong demand but slightly improved domestic supply in some regions. Asia and Africa are remaining the major impor"
  },
  {
    "figure_id": "F436",
    "report_id": "R018",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "## Prices will likely recover in the next few years then drop in real terms Figure 4.5. Evolution of world sugar prices Note: raw sugar nearby futures price, Intercontinental Exchange (ICE) contract No.11; white (refined) sugar nearby futures price, Interconti"
  },
  {
    "figure_id": "F437",
    "report_id": "R018",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "## 5.3.1. Consumption Global meat consumption continues to grow but at a slower pace Global meat consumption is projected to reach around 412 Mt by 2035, a 12% increase from the base period. This growth reflects continued population growth, rising incomes and,"
  },
  {
    "figure_id": "F438",
    "report_id": "R018",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Sheep meat production is projected to increase 17%, reaching nearly 22 Mt cwe. This increase reflects gradual flock rebuilding and improvements in lambing rates supported by favourable price conditions. China is projected to account for around 15% of the globa"
  },
  {
    "figure_id": "F439",
    "report_id": "R018",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Livestock producers face rising input costs, volatile markets, disease risks and tightening environmental requirements. Many producers respond by improving productivity, diversifying income sources and adopting new technologies. Improvements in slaughter yield"
  },
  {
    "figure_id": "F440",
    "report_id": "R018",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Artificial intelligence (AI), automation and imaging systems are increasingly used across the meat value chain, from farm management, to processing and logistics supporting grading, food safety and automation. In this context, automation refers to machines per"
  },
  {
    "figure_id": "F441",
    "report_id": "R018",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Global meat trade expands amid shifting supply and demand regional dynamics Global meat trade is projected to expand at a slower pace than in the previous decade, reflecting production recoveries and more balanced consumption growth (Figure 5.5). Structural ch"
  },
  {
    "figure_id": "F442",
    "report_id": "R018",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "These projections extend the longer-term divergence observed between ruminant and non-ruminant meat prices. Slower productivity gains, greater land requirements, and biological constraints in cattle and sheep production contribute to relatively higher producti"
  },
  {
    "figure_id": "F443",
    "report_id": "R018",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "## Strong demand in India and Pakistan is leading increased global dairy consumption Although milk is a highly perishable product which must be processed shortly after collection, most milk is consumed in the form of fresh dairy products, $^{1}$ including thos"
  },
  {
    "figure_id": "F444",
    "report_id": "R018",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "In high-income countries, overall per capita demand for fresh dairy products is declining but the composition of demand has been shifting over recent years in favour of dairy fat such as full-fat drinking milk and cream. Plant-based dairy replacements are avai"
  },
  {
    "figure_id": "F445",
    "report_id": "R018",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "## Greater efficiency in milk production through yield improvements World milk production is projected to grow at 2.0% p.a. (to 1 223 Mt by 2035) over the next decade, faster than most other major agricultural commodities. Growth in the number of cows is expec"
  },
  {
    "figure_id": "F446",
    "report_id": "R018",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "The average yield per cow in North America is the highest in the world, as their share of grass-based production is low, and feeding is focused on achieving high yields from specialised dairy herds. Dairy herds in Canada and the United States are expected to r"
  },
  {
    "figure_id": "F447",
    "report_id": "R018",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Most dairy products are domestically consumed. Only a small share (less than 7%) of world milk production is traded internationally, primarily due to its perishability and high water content (more than 85%). Around 50% of world production of WMP and SMP is tra"
  },
  {
    "figure_id": "F448",
    "report_id": "R018",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "New Zealand remains the primary"
  },
  {
    "figure_id": "F449",
    "report_id": "R018",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "## Nominal international dairy prices will gradually and slightly increase International dairy prices are prices of processed products from the main exporters in Oceania and Europe. The two main reference prices are butter and SMP, where butter is the referenc"
  },
  {
    "figure_id": "F450",
    "report_id": "R018",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Focusing on food uses, global demand for aquatic animal foods is projected to increase by 12% over the next decade, largely driven by population growth. Total apparent consumption is expected to reach 194 Mt lwe by 2035, an increase of 20 Mt compared with the "
  },
  {
    "figure_id": "F451",
    "report_id": "R018",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "## 7.3.2. Production Aquaculture continues to drive global fisheries and aquaculture production growth despite slowing expansion Global fisheries and aquaculture production is projected to increase from 194 Mt lwe in the base period to 216 Mt by 2035. Although"
  },
  {
    "figure_id": "F452",
    "report_id": "R018",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 7.2. World capture fisheries and aquaculture production of aquatic animals Note: Expressed in live weight equivalent. Global aquaculture production is projected to reach 121 Mt by 2035, a 18% increase from the base period, compared with 51% growth in th"
  },
  {
    "figure_id": "F453",
    "report_id": "R018",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "International trade will continue to play a critical role in the sector, however growth in aquatic trade has been slower than the expansion of fisheries and aquaculture production over the last two decades and is projected to remain so over the coming decade. "
  },
  {
    "figure_id": "F454",
    "report_id": "R018",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Overall, real prices of all fish and other aquatic products are expected to decline over the projection period, even where nominal prices are broadly flat or still edging up. Moreover, the decline in real prices is expected to be larger in the projection perio"
  },
  {
    "figure_id": "F455",
    "report_id": "R018",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "## Bulk of additional biofuel supply and demand located in Asian countries Biofuel supply and demand projections are largely influenced by the future trajectory of overall fuel consumption, particularly because many biofuel mandates are set as a percentage of "
  },
  {
    "figure_id": "F456",
    "report_id": "R018",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "This Outlook expects a slower growth rate of biofuel consumption and production globally, both projected at 1.4% p.a. during the projection period. This is three fifth of the growth observed in the previous decade, primarily as a result of declining total fuel"
  },
  {
    "figure_id": "F457",
    "report_id": "R018",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "Figure 8.1. Biofuel demand trends in major regions, 2035 vs. base period 2023-25 Note: Shares calculated on demand quantities expressed in volume. The size of each bubble relates to the consumption volume of the respective biofuel in the base period. Change in"
  },
  {
    "figure_id": "F458",
    "report_id": "R018",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "StatLink https://stat.link/gus10i Despite the increasing scrutiny of the sustainability of biofuel production witnessed in many countries, and notwithstanding significant variations in feedstock composition, conventional (or food-related) feedstocks are expect"
  },
  {
    "figure_id": "F459",
    "report_id": "R018",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "## 8.3.2. Trade ## Global biofuel trade is expected to remain constant World ethanol trade is projected to marginally decrease from 12.8 bln L to 12.3 bln L by 2035, with total share of production decreasing from 8.9% to 7.6% by the end of the projection perio"
  },
  {
    "figure_id": "F460",
    "report_id": "R018",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "## 8.3.3. Prices ## Prices in real terms are expected to decrease Following their peak in 2022, nominal prices for biomass-based diesel and ethanol declined through 2023 and 2024, primarily attributed to lower feedstock and oil prices. In 2025, both prices rec"
  },
  {
    "figure_id": "F461",
    "report_id": "R018",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Cotton consumption refers to the transformation of cotton fibres by mills into yarn. Cotton mill use depends largely on two major drivers: global textile demand and competition from synthetic fibres. Over the past decades, global demand for textile fibres has "
  },
  {
    "figure_id": "F462",
    "report_id": "R018",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Higher labour costs and more stringent labour and environmental regulations have led to a gradual decrease in China's cotton mill consumption since 2010. This decline was further exacerbated by the abolishment of the support price system in 2014. This contribu"
  },
  {
    "figure_id": "F463",
    "report_id": "R018",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "## Global production to grow with improved yields, notably in Brazil Cotton is grown in subtropical and seasonally dry tropical areas in the northern and southern hemispheres, although most of the world's production takes place north of the equator. The leadin"
  },
  {
    "figure_id": "F464",
    "report_id": "R018",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Average global yields are projected to increase by 15% compared to the base period. Factors such as improvements in genetics, better agricultural practices and digitalisation supporting precision agriculture will contribute significantly to enhancing productiv"
  },
  {
    "figure_id": "F465",
    "report_id": "R018",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "In Brazil, cotton is grown in part as a second crop in rotation with soybeans or maize. Recently, output has strongly grown in the main cultivation areas such as Mato Grosso, where 72% of Brazilian cotton is currently harvested. Cotton output is foreseen to in"
  },
  {
    "figure_id": "F466",
    "report_id": "R018",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "World cotton trade is projected to expand steadily over the next decade by $2.4\\%$ p.a. to reach 12 Mt in 2035. This growth will be driven by the increasing demand for textiles in Asian countries, particularly Bangladesh, Viet Nam and Pakistan, where mill use "
  },
  {
    "figure_id": "F467",
    "report_id": "R018",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "International cotton prices to decline in real terms over the medium term Figure 9.7. World cotton price and stock-to-use ratio Note: Real prices are nominal world prices deflated by the US GDP deflator (2025=1). The reference cotton price is the Cotlook price"
  },
  {
    "figure_id": "F468",
    "report_id": "R018",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Global sweet potato production has shown a declining trend in recent years, largely reflecting reductions in harvested area in China, the world's leading producer. Demand for sweet potatoes and other roots and tubers remains primarily food-driven, with limited"
  },
  {
    "figure_id": "F469",
    "report_id": "R018",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Pulse cultivation has long been integrated into agricultural systems across many regions. Leguminous crops play an important role in improving soil fertility through biological nitrogen fixation and can contribute to higher soil organic matter when included in"
  },
  {
    "figure_id": "F470",
    "report_id": "R018",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "## Projection highlights Assuming normal weather conditions and no further spread of banana plant diseases, global banana production is expected to reach 168 Mt by 2035, from 140 Mt in the base period. As per capita demand for bananas is becoming increasingly "
  },
  {
    "figure_id": "F471",
    "report_id": "R018",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "## Projection highlights Global papaya production is projected to rise by 2.1% p.a., to 18 Mt in 2035, from 15 Mt in the base period. As the share of exports in production is particularly low for papayas, at some 3% in the base period, production of this fruit"
  },
  {
    "figure_id": "F472",
    "report_id": "R018",
    "label": "经合组织视觉摘要 1",
    "figure_type": "external_card",
    "context": "经合组织｜经合组织：未来十年全球农业增长的真正瓶颈不是土地，是劳动力｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F473",
    "report_id": "R019",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "As a framework for analysis this report draws on the OECD Guidelines for Multinational Enterprises on Responsible Business Conduct (MNE Guidelines) (OECD, 2023[2]) and the OECD Recommendation on the Role of Government in Promoting Responsible Business Conduct "
  },
  {
    "figure_id": "F474",
    "report_id": "R019",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1.1. OECD six-step due diligence framework for responsible business conduct The RBC Recommendation lays out a single comprehensive set of principles and policy recommendations for how governments can enable and promote RBC (see Figure 1.2). Figure 1.2. "
  },
  {
    "figure_id": "F475",
    "report_id": "R019",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Around 40% of large listed companies have disclosed commitments on RBC in their supply chains (Figure 2.2). Respectively, 39% of companies commit to environmental standards and 43% to social standards in their supply chain. Adoption of these commitments is hig"
  },
  {
    "figure_id": "F476",
    "report_id": "R019",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "One way to measure a company's commitment to RBC is whether it commits explicitly to the MNE Guidelines or the UN Guiding Principles on Business and Human Rights – two of the main international instruments on RBC. Only one in three (32%) of large listed compan"
  },
  {
    "figure_id": "F477",
    "report_id": "R019",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "One way to measure a company's commitment to RBC is whether it commits explicitly to the MNE Guidelines or the UN Guiding Principles on Business and Human Rights – two of the main international instruments on RBC. Only one in three (32%) of large listed compan"
  },
  {
    "figure_id": "F478",
    "report_id": "R019",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## Box 2.2. Gaps in materiality assessment of financial risk and adverse environmental and social impacts The OECD has reviewed a sample of approximately 140 double materiality assessments disclosed in 2025 as part of the first wave of corporate disclosures al"
  },
  {
    "figure_id": "F479",
    "report_id": "R019",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Companies in the financial sector identify substantially fewer topics as material than in the non-financial sectors, both in terms of negative impacts and financial risks (see Figure 2.4, Panel B). Key material topics in the financial sector include climate ch"
  },
  {
    "figure_id": "F480",
    "report_id": "R019",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "This section examines how companies identify and assess risks and impacts in their supply chains, drawing on two sets of indicators: 1) whether companies disclose that they use human rights or environmental criteria for selecting suppliers, $^{6}$ which might "
  },
  {
    "figure_id": "F481",
    "report_id": "R019",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## Figure 2.6. Environmental and social expectations of suppliers versus evaluation of supplier risk While nearly half of large listed companies report using environmental or human rights criteria to select their suppliers, fewer than 20% report that they eval"
  },
  {
    "figure_id": "F482",
    "report_id": "R019",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## Figure 2.6. Environmental and social expectations of suppliers versus evaluation of supplier risk While nearly half of large listed companies report using environmental or human rights criteria to select their suppliers, fewer than 20% report that they eval"
  },
  {
    "figure_id": "F483",
    "report_id": "R019",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## Many companies face challenges in extending due diligence beyond tier-1 suppliers To understand the extent to which companies have visibility and extend their due diligence beyond tier-1, this section uses indicators on the coverage of different supply chai"
  },
  {
    "figure_id": "F484",
    "report_id": "R019",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Note: This figure is based on three indicators with different coverage (up to \\~450 large listed companies). Given the lower coverage of this data, for each indicator, the rate of uptake was expressed as a percentage of companies in the sub-sample for which da"
  },
  {
    "figure_id": "F485",
    "report_id": "R019",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## Box 2.3. Sustainability initiatives as multipliers of supply chain due diligence ## Figure 2.9. Number of sustainability initiatives over time, by function The landscape has broadened and diversified since the early 2000s, with many initiatives undertaking "
  },
  {
    "figure_id": "F486",
    "report_id": "R019",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Over half of large listed companies (52%) report conducting some form of stakeholder engagement, however, only very few (8%) state that they engage stakeholders on human rights issues specifically (Figure 2.10). Reported evidence of stakeholder engagement is m"
  },
  {
    "figure_id": "F487",
    "report_id": "R019",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "In the context of health and safety, there seems to be a substantial gap between companies reporting on their adoption of management systems (46%), and on the participation of staff in safety improvement initiatives (18%) (Figure 2.11). Disclosure of health an"
  },
  {
    "figure_id": "F488",
    "report_id": "R019",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Disclosure of health and safety management systems is most prevalent in Emerging Asia excluding China, followed by Europe and Latin America, and lowest in China. The share of companies reporting on staff participation in health and safety improvement initiativ"
  },
  {
    "figure_id": "F489",
    "report_id": "R019",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "While these indicators are specific to the topic of health and safety, they signal a potential under-use of stakeholder engagement as part of prevention and mitigation activities. Figure 2.11. Health and safety impact prevention and mitigation measures in own "
  },
  {
    "figure_id": "F490",
    "report_id": "R019",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2.11. Health and safety impact prevention and mitigation measures in own operations While more than 45% of companies have established health and safety management systems, fewer than 20% involve employees in safety improvement initiatives. ## Uptake of "
  },
  {
    "figure_id": "F491",
    "report_id": "R019",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## Uptake of prevention and mitigation measures in the supply chain is low across the board Disclosure of prevention and mitigation measures in the supply chain is generally low. One-quarter of companies report providing training or collaborating with supplier"
  },
  {
    "figure_id": "F492",
    "report_id": "R019",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## Uptake of remediation measures is limited, with higher rates of implementation amongst larger companies The reported prevalence of remediation practices is limited. Globally, 17% of companies report having a formal grievance mechanism on human rights, while"
  },
  {
    "figure_id": "F493",
    "report_id": "R019",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "According to OECD standards on RBC, disengagement from a business relationship may be appropriate either after failed attempts at mitigation, or where the enterprise deems mitigation not feasible, or because of the severity of the adverse impact. However, wher"
  },
  {
    "figure_id": "F494",
    "report_id": "R019",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## There is a marked discrepancy between the uptake of policies and actions to address impacts Figure 2.15 summarises the average company's disclosure on due diligence, measured as the percentage of practices disclosed by each company for different areas of du"
  },
  {
    "figure_id": "F495",
    "report_id": "R019",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## Figure 2.15. Uptake of due diligence policies and management systems versus measures to identify and address adverse environmental and social impacts Disclosure of due diligence uptake displays stronger regional than sectoral variation. However, regions wit"
  },
  {
    "figure_id": "F496",
    "report_id": "R019",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "In most regions, SOEs report higher uptake of due diligence than non-SOEs including with respect to prevention, mitigation and remediation measures. In most regions, reported uptake of prevention, mitigation and remediation measures is higher among SOEs $^{1}$"
  },
  {
    "figure_id": "F497",
    "report_id": "R019",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "In most regions, reported uptake of prevention, mitigation and remediation measures is higher among SOEs $^{1}$ than non-SOEs (Figure 2.16). In Europe, the difference in reported uptake of prevention, mitigation and remediation practices between SOEs and non-S"
  },
  {
    "figure_id": "F498",
    "report_id": "R019",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## Figure 2.16. Uptake of responsible business conduct due diligence: SOEs and non-SOEs In most regions, due diligence uptake by large listed SOEs is similar to or higher than that of non-SOEs. However, SOEs are concentrated in China, where uptake is generally"
  },
  {
    "figure_id": "F499",
    "report_id": "R019",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Reporting on certain aspects of due diligence is increasingly common but reporting on actual impacts and outcomes remains rare Only 7% of large listed companies disclose salient human rights issues (which can be either at sector or business-level) and only 6% "
  },
  {
    "figure_id": "F500",
    "report_id": "R019",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "\\- Leading by example – governments as economic and commercial actors: use public procurement as a strategic tool for RBC, set clear expectations for state-owned enterprises to follow RBC standards, and integrate RBC considerations in government financial inst"
  },
  {
    "figure_id": "F501",
    "report_id": "R019",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "\\- promoting access to remedy: measures to enhance the access to remedy for affected persons \\- co-ordinating on RBC: efforts to co-ordinate RBC through government bodies, reviews or other approaches. Figure 3.2. Responsible business conduct policies across co"
  },
  {
    "figure_id": "F502",
    "report_id": "R019",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "No measures EU measures National measures Figure 3.3. Due diligence legislative measures across countries adhering to the OECD Guidelines for Multinational Enterprises on Responsible Business Conduct Note: This figure shows the number of countries adhering to "
  },
  {
    "figure_id": "F503",
    "report_id": "R019",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Note: This figure shows the number of countries adhering to the MNE Guidelines with at least one due diligence measure in each category, and the share of GDP of these countries. “Any due diligence measure” refers to the presence of at least one measure across "
  },
  {
    "figure_id": "F504",
    "report_id": "R019",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "The shift towards systematically integrating RBC considerations in trade and investment agreements has been accompanied by the gradual development of mechanisms to support their implementation. For example, allowing for public submissions on the implementation"
  },
  {
    "figure_id": "F505",
    "report_id": "R019",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3.5. Responsible business conduct clauses in agreements signed by countries adhering to the OECD Guidelines for Multinational Enterprises on Responsible Business Conduct Note: This figure shows the number of international trade and investment agreements"
  },
  {
    "figure_id": "F506",
    "report_id": "R019",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Development co-operation in support of RBC helps to maximise the private sector's contribution to sustainable development and enables companies in developing countries to meet the expectations of their international business partners. Development co-operation "
  },
  {
    "figure_id": "F507",
    "report_id": "R019",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Note: This figure shows the number of countries adhering to the MNE Guidelines as well as the European Union that reported integrating RBC in development co-operation across different channels. Based on 45 responses to the survey question: \"Has your government"
  },
  {
    "figure_id": "F508",
    "report_id": "R019",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "## Responsible business conduct considerations are commonly integrated into public procurement frameworks and processes RBC considerations commonly feature in public procurement frameworks, with 32 countries adhering to the MNE Guidelines (73% of respondents) "
  },
  {
    "figure_id": "F509",
    "report_id": "R019",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Requirements for public institutions, and more specifically on public procurement have been included in some recent regulation on due diligence. (See Due diligence policy). Due diligence laws with explicit requirements for public institutions state that public"
  },
  {
    "figure_id": "F510",
    "report_id": "R019",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Countries adhering to the MNE Guidelines have begun to establish responsible business conduct expectations for SOEs through a range of different approaches Most countries adhering to the MNE Guidelines have established and disclosed expectations for SOEs to ob"
  },
  {
    "figure_id": "F511",
    "report_id": "R019",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "State-based export credit agencies (ECAs) can play an important role in promoting RBC as ECAs represent the largest public"
  },
  {
    "figure_id": "F512",
    "report_id": "R019",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "In 2024, over $70\\%$ of ECAs of countries adhering to the Common Approaches reported having formal mandates or policy statements related to climate change and related issues. Human rights is less reflected as a focus in mandates and policy statements (just ove"
  },
  {
    "figure_id": "F513",
    "report_id": "R019",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Remedy is a key element of the OECD due diligence framework. However, as indicated in the previous chapter, global uptake is much weaker than for other due diligence steps, with only 17% of companies reporting having a formal grievance mechanism on human right"
  },
  {
    "figure_id": "F514",
    "report_id": "R019",
    "label": "经合组织视觉摘要 1",
    "figure_type": "external_card",
    "context": "经合组织｜经合组织：不是口号而是规则，经合组织指出84%成员国已立法推动企业尽责管理｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F515",
    "report_id": "R020",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1.1. A majority across the OECD view the cost of living as among the three most important issues facing their country, while more than a quarter are concerned about crime or poverty Share of population who view policy issue as among the three most impor"
  },
  {
    "figure_id": "F516",
    "report_id": "R020",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "With the exception of Brazil, the share with high or moderately high trust in the national government in the OECD accession countries is substantially lower than the OECD average. The distribution of trust levels varies across countries, owing to a mixture of "
  },
  {
    "figure_id": "F517",
    "report_id": "R020",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Across 18 $^{4}$ countries with available data, the share of people reporting high or moderately high trust fell by an average of 2 percentage points between 2021 and 2023 (OECD, 2024 $^{[8]}$ ). Trust levels in many countries appeared buoyed by the COVID cris"
  },
  {
    "figure_id": "F518",
    "report_id": "R020",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "The Covid-19 pandemic in 2020 interrupted the slow economic recovery that had followed Greece's post-2009 Great Depression. In contrast to the slow recovery in the 2010s, per capita GDP returned to the pre-2020 level much more quickly – by the third quarter of"
  },
  {
    "figure_id": "F519",
    "report_id": "R020",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Findings from the 2025 OECD Trust Survey indicate that there is an association between the issues respondents indicate are important for their country and their reported trust in their national government. These differences remain after accounting for country "
  },
  {
    "figure_id": "F520",
    "report_id": "R020",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Neutral economic crisis (41%), and are confident that their country will reduce GhG emissions in the coming decade (38%) (Figure 1.6). While views of emergency preparedness and technology regulation have remained largely constant relative to 2023, with shifts "
  },
  {
    "figure_id": "F521",
    "report_id": "R020",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1.6. A slight majority is confident that government institutions are prepared to protect people's lives in a major emergency, while fewer expect to be protected during an economic crisis Share of population reporting different levels of confidence in th"
  },
  {
    "figure_id": "F522",
    "report_id": "R020",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Share of population reporting different levels of confidence in the capabilities of government institutions to achieve policy objective, OECD average (%), 2025 Likely/Confident Unlikely/Not confident Do not know StatLink https://stat.link/0bsmxt Beyond the out"
  },
  {
    "figure_id": "F523",
    "report_id": "R020",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Likely/Confident Unlikely/Not confident Do not know StatLink https://stat.link/0bsmxt Beyond the outcomes of policy actions, people also care about how governments arrive at their decisions. They expect policymakers to be open and responsive to feedback from t"
  },
  {
    "figure_id": "F524",
    "report_id": "R020",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "StatLink https://stat.link/0bsmxt Beyond the outcomes of policy actions, people also care about how governments arrive at their decisions. They expect policymakers to be open and responsive to feedback from the public and different stakeholders, and yet to wit"
  },
  {
    "figure_id": "F525",
    "report_id": "R020",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Beyond the outcomes of policy actions, people also care about how governments arrive at their decisions. They expect policymakers to be open and responsive to feedback from the public and different stakeholders, and yet to withstand pressure from special inter"
  },
  {
    "figure_id": "F526",
    "report_id": "R020",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Unlikely/Not confident Do not know Note: The figure presents the unweighted OECD averages for responses to the following questions: (1) \"If the federal/central/national government takes a decision, how likely do you think it is that it will draw on the best av"
  },
  {
    "figure_id": "F527",
    "report_id": "R020",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "StatLink https://stat.link/6wtnrd A majority of people across the OECD are satisfied with administrative services and with the data protection provided by government institutions. Among recent service users, 68% across the OECD and 48% across the participating"
  },
  {
    "figure_id": "F528",
    "report_id": "R020",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "\\- People who feel their government makes decisions based on the best available evidence, and balances needs of current and future generations, are particularly more likely to have high or moderately high trust in the government. Improvements in the perception"
  },
  {
    "figure_id": "F529",
    "report_id": "R020",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "A decomposition analysis of the survey data – carried out within each country – helps explain how changes in trust levels relate to shifts in perceptions of public governance. This analysis (Figure 1.10), which was run separately for each country, is illustrat"
  },
  {
    "figure_id": "F530",
    "report_id": "R020",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Evidence from the OECD Trust Survey over time suggests that across democratic countries, people tend to trust institutions responsible for upholding security and the law the most. Conversely, they trust political institutions the least, especially political pa"
  },
  {
    "figure_id": "F531",
    "report_id": "R020",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Trust in the courts and judicial system is substantially lower, albeit higher than other public institutions, and displays a higher variability across countries. On average, 54% across the OECD have high or moderately high trust in the courts (Figure 1.12). In"
  },
  {
    "figure_id": "F532",
    "report_id": "R020",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## Figure 1.13. Local governments and the national civil service are usually trusted more than national governments Share of population with high or moderately high trust in the respective institution, 2025 Trust in National Government Trust in Local Governmen"
  },
  {
    "figure_id": "F533",
    "report_id": "R020",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "StatLink https://stat.link/eqvwcn Distribution of levels of trust in local government and the national civil service, OECD-20 Note: The figure presents the share who provided a response of 6 to 10 to the question \"On a scale of 0 to 10, where 0 is not at all a"
  },
  {
    "figure_id": "F534",
    "report_id": "R020",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Distribution of levels of trust in local government and the national civil service, OECD-20 Note: The figure presents the share who provided a response of 6 to 10 to the question \"On a scale of 0 to 10, where 0 is not at all and 10 is completely, how much do y"
  },
  {
    "figure_id": "F535",
    "report_id": "R020",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "\\- People who have a particularly positive view of the quality of administrative services, and who find it more likely than average that data are used for legitimate purposes only, that applications for government benefits or services are treated fairly, that "
  },
  {
    "figure_id": "F536",
    "report_id": "R020",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## 2.2. DIFFERENCES IN TRUST LEVELS BETWEEN POPULATION GROUPS Findings from the OECD Trust Survey 2025 indicate that the largest trust gaps are found along political dimensions, namely partisanship and political agency (Figure 2.1). Gaps across socio-economic "
  },
  {
    "figure_id": "F537",
    "report_id": "R020",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Findings from the OECD Trust Survey 2025 indicate that the largest trust gaps are found along political dimensions, namely partisanship and political agency (Figure 2.1). Gaps across socio-economic characteristics, including perceived discrimination, education"
  },
  {
    "figure_id": "F538",
    "report_id": "R020",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2.1. Trust in the national government varies more strongly along perceived political agency and partisan lines than across socio-economic or demographic groups Share of population with high or moderately high trust in the national government by level of"
  },
  {
    "figure_id": "F539",
    "report_id": "R020",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "These trust gaps related to political agency—namely, the perceived ability to have a say in government decision-making and confidence in participating in politics—are substantial. Of particular concern is that a large share of people across OECD countries repo"
  },
  {
    "figure_id": "F540",
    "report_id": "R020",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "StatLink https://stat.link/tnev2f minority feel they have a say or are confident to participate in politics. Among government supporters, 38% report believing that people like them have a say in government decision-making, compared to 25% of non-supporters. Si"
  },
  {
    "figure_id": "F541",
    "report_id": "R020",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## StatLink https://stat.link/zcp9m0 gaps are less anticipated for administrative institutions such as the police or civil service, which are designed to operate on a non-partisan basis. Figure 2.4 shows that partisan trust gaps are present across all public i"
  },
  {
    "figure_id": "F542",
    "report_id": "R020",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## Box 2.1. Do partisan differences in trust extend beyond political institutions? Beyond identifying support for the current government in the most recent election, the OECD Trust Survey does not include measures of broader political preferences, such as resp"
  },
  {
    "figure_id": "F543",
    "report_id": "R020",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Socio-economic characteristics are associated with smaller trust gaps in national government than those linked to political agency and partisanship. The most pronounced disparities refer to financial concerns, while differences related to self-identified membe"
  },
  {
    "figure_id": "F544",
    "report_id": "R020",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "gap of 14 percentage points. The education trust gap varies substantially across countries and is particularly large in Switzerland (35 percentage points), Portugal and the United Kingdom (both 31 percentage points). By contrast, trust in the national governme"
  },
  {
    "figure_id": "F545",
    "report_id": "R020",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "StatLink https://stat.link/7dts5h However, there is considerable cross-country variation in the magnitude of this gap. The gap is particularly large in Estonia (24 percentage points) and Luxembourg (26 percentage points), while it is negligible in Brazil (two "
  },
  {
    "figure_id": "F546",
    "report_id": "R020",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## Box 2.2. Institutional trust varies substantially by levels of interpersonal trust Across the OECD, respondents with low levels of interpersonal trust – i.e., trust in other people – report substantially lower confidence in all public institutions. However,"
  },
  {
    "figure_id": "F547",
    "report_id": "R020",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## 2.2.3. The smallest trust gaps are associated with demographic characteristics Looking more closely at demographic differences, trust in national government varies to a comparatively small extent between men and women. 44% of men in OECD countries place hig"
  },
  {
    "figure_id": "F548",
    "report_id": "R020",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "StatLink https://stat.link/a06lyr Age likewise is associated with a modest trust gap. Across OECD countries, 43% of respondents aged 50 and above report trusting the national government, compared with 37% among those aged 30–49 and 38% among those aged 18–29 ("
  },
  {
    "figure_id": "F549",
    "report_id": "R020",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Differences between population groups often reflect enduring predispositions shaped through early socialization processes (van der Meer, la Roi and van Alebeek, 2025[9]). While individuals' trust may increase or decrease later in life in response to political "
  },
  {
    "figure_id": "F550",
    "report_id": "R020",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "There is, nonetheless, considerable cross-country variation in this gap (Figure 2.13). In Portugal, for example, the education-related trust gap increased steadily, from 11% in 2021 to 14% in 2023 and 31% in 2025. By contrast, the gap decreased in Norway, fall"
  },
  {
    "figure_id": "F551",
    "report_id": "R020",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Across the OECD, six in ten (60%) people who had recent contact with the education system, either because they were enrolled themselves in the past two years or someone in their household was, are satisfied with it (Figure 3.1, Panel A). This is nine percentag"
  },
  {
    "figure_id": "F552",
    "report_id": "R020",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Satisfaction with the healthcare system is lower than with education, but the gap between recent users (within the last year) and others is also smaller. On average across the OECD, 54% of people who used healthcare services in the past year are satisfied (Fig"
  },
  {
    "figure_id": "F553",
    "report_id": "R020",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Following a drop in satisfaction with education and health systems across OECD countries between 2021 and 2023, satisfaction with both systems has risen again between 2023 and 2025. In the 19 $^{1}$ OECD countries with available data on this indicator for all "
  },
  {
    "figure_id": "F554",
    "report_id": "R020",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Trust in the healthcare system has likewise increased between 2023 and 2025, although it remains below 2021 levels. In the 19 countries with data for all three years, satisfaction among recent users fell from 63% to 55% and then returned to 58% in 2025 (Figure"
  },
  {
    "figure_id": "F555",
    "report_id": "R020",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "## 3.1.2. Satisfaction with administrative services is generally high and rising Figure 3.3. In each OECD country, a majority of recent administrative services users are satisfied with these services Share of recent users reporting different levels of satisfac"
  },
  {
    "figure_id": "F556",
    "report_id": "R020",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "The data gathered through the Survey shows that while users are, overall, satisfied with public services they used in the last 12 months, the overall level of satisfaction varies depending on the Life Event experienced. For instance, in one participating count"
  },
  {
    "figure_id": "F557",
    "report_id": "R020",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "The share who are satisfied with several important quality aspects exceeds 70% in OECD and 50% in OECD accession candidate countries. 74% are satisfied with the courtesy of public employees during their most recent interaction with an administrative public ser"
  },
  {
    "figure_id": "F558",
    "report_id": "R020",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "The relative stability in the evaluation of individual quality aspects between 2023 and 2025 is mirrored in a large stability in the relationship of these evaluations and overall satisfaction with administrative services. The differences in the point estimates"
  },
  {
    "figure_id": "F559",
    "report_id": "R020",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Before seeking a public service or benefit, or completing a required administrative task, people typically look for information on the steps they need to take. Clear, accessible information about administrative services is thus an important prerequisite for a "
  },
  {
    "figure_id": "F560",
    "report_id": "R020",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "## StatLink https://stat.link/09o4vz These results correspond well with the findings of the OECD's cross-national Risks that Matter (RTM) Survey on perceptions of social services and benefits (OECD, 2025[1]). RTM respondents are most confident in their knowled"
  },
  {
    "figure_id": "F561",
    "report_id": "R020",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "StatLink https://stat.link/9vf0tu Figure 3.9. In OECD and OECD accession countries, more people find it unlikely than find it likely that a government employee would turn down an offer of money to speed up access to a service Share of population who find it li"
  },
  {
    "figure_id": "F562",
    "report_id": "R020",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Direct experience with civil servants can improve how people perceive the openness, fairness and integrity of public institutions. In 2025, among people in OECD countries who had recently used an administrative service, the share who thought that government em"
  },
  {
    "figure_id": "F563",
    "report_id": "R020",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "On average across the OECD, four in ten (39%) find it likely that if they committed an error, a public employee would help them correct it rather than sanction them (Figure 3.11). In contrast, 42% find it unlikely. The share who find it likely can be as low as"
  },
  {
    "figure_id": "F564",
    "report_id": "R020",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "France and the experience of individuals yet relatively limited. As expected, the relationship between the perception of the prevalence of ‘right to make an error’ and trust in public institutions is somewhat ambiguous. At the country level, there is a positiv"
  },
  {
    "figure_id": "F565",
    "report_id": "R020",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "50%; and in Brazil, both are above the OECD averages. More positive perceptions of responsiveness in day-to-day interactions are associated with modest increases, around 1–1.5 percentage points, in the likelihood of reporting high or moderately high trust in l"
  },
  {
    "figure_id": "F566",
    "report_id": "R020",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "StatLink https://stat.link/hfy4g9 Figure 3.13. The share who view public services as responsive across OECD countries has slightly risen since 2021 Share of population who find it likely that innovative ideas that could improve them are adopted or that that pu"
  },
  {
    "figure_id": "F567",
    "report_id": "R020",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3.13. The share who view public services as responsive across OECD countries has slightly risen since 2021 Share of population who find it likely that innovative ideas that could improve them are adopted or that that public services improve in response "
  },
  {
    "figure_id": "F568",
    "report_id": "R020",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "People's confidence in their government's ability to plan for and address policy challenges varies with their associated complexity and time horizon. People's confidence in the ability of institutions to protect them during large scale emergencies is generally"
  },
  {
    "figure_id": "F569",
    "report_id": "R020",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4.1. A majority is confident in the ability of government to protect lives in emergencies, larger than the share who believe government balances intergenerational interests Share of population reporting different levels of confidence in achieving stated"
  },
  {
    "figure_id": "F570",
    "report_id": "R020",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Fewer than four in ten people across the OECD are confident that their country can reduce GhG emissions and that their government adequately balances the interests of current and future generations. The share who find it likely that government appropriately re"
  },
  {
    "figure_id": "F571",
    "report_id": "R020",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "At the country level, the proportion of the population who believe governments make use of relevant evidence and who find it likely that public services adapt to changing societal needs – 40% on average across the OECD - are highly correlated (with an $R^{2}$ "
  },
  {
    "figure_id": "F572",
    "report_id": "R020",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Close to four in ten people (39%) across the OECD and more than one third across the participating OECD accession countries find it likely that a policy would be changed if a majority of people are against it, while a similar share (41%) find it unlikely (Figu"
  },
  {
    "figure_id": "F573",
    "report_id": "R020",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "StatLink https://stat.link/3waqjs organisations and trade unions, to better tackle long-term challenges (Figure 4.6). $18\\%$ provide a neutral response and $38\\%$ find it unlikely. Switzerland and Brazil are the only countries where a majority believes in gove"
  },
  {
    "figure_id": "F574",
    "report_id": "R020",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "StatLink https://stat.link/2kujba Only around one third of people across the OECD and the participating OECD accession candidate countries find it likely that a politician would refuse to grant a political favour in return for a lucrative private-sector job. S"
  },
  {
    "figure_id": "F575",
    "report_id": "R020",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "StatLink https://stat.link/d7vtac is likely to refuse, and in Peru, 39% do. Positively, in the 29 OECD countries with available data for 2023 and 2025, the share who find it likely has increased by 3 percentage points. In fact, the share with an optimistic ass"
  },
  {
    "figure_id": "F576",
    "report_id": "R020",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Norway, the Slovak Republic and the United Kingdom, as well as in Bulgaria, express low confidence in their governments' (potential) use of AI. By contrast, Korea and Switzerland have notably higher shares of respondents expressing positive expectations. These"
  },
  {
    "figure_id": "F577",
    "report_id": "R020",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5.1. Around four in ten people have moderately or very positive views about the potential of AI use by government institutions Panel A. OECD average distribution OECD average share of respondents by number of expectations they feel confident in Panel B."
  },
  {
    "figure_id": "F578",
    "report_id": "R020",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "This aligns closely with findings from the 2024 Risks That Matter Survey (OECD, 2025[3]). For example, $40\\%$ consider the use of AI to help process and approve social programme applications to be good for users, while $30\\%$ report uncertainty and $25\\%$ beli"
  },
  {
    "figure_id": "F579",
    "report_id": "R020",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "## 5.2. AI HAS THE POTENTIAL TO BECOME A TRUST-ENHANCING FORCE DEPENDING ON PUBLIC GOVERNANCE CHOICES To better understand how AI might affect public trust, it is helpful to compare what the public expects with the way in which government agencies use AI in pr"
  },
  {
    "figure_id": "F580",
    "report_id": "R020",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Finally, it is worth noting that the previously explained finding that people are more optimistic about AI's potential responsiveness and efficiency benefits in government (more tailored services and lower costs) than about value-based aspects (privacy, transp"
  },
  {
    "figure_id": "F581",
    "report_id": "R020",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Panel B. Pessimism Index (Confident in 0 outcomes) Panel A. Optimism Index (Confident in 5 to 6 outcomes) Figure 5.4. Socio-economic and demographic characteristics are associated with varying levels of optimism/pessimism towards AI use in the public sector No"
  },
  {
    "figure_id": "F582",
    "report_id": "R020",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Panel A. Optimism Index (Confident in 5 to 6 outcomes) Figure 5.4. Socio-economic and demographic characteristics are associated with varying levels of optimism/pessimism towards AI use in the public sector Note: The figure shows the OECD average for the share"
  },
  {
    "figure_id": "F583",
    "report_id": "R020",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5.4. Socio-economic and demographic characteristics are associated with varying levels of optimism/pessimism towards AI use in the public sector Note: The figure shows the OECD average for the share who have a very positive (panel A) or very skeptical ("
  },
  {
    "figure_id": "F584",
    "report_id": "R020",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "public understanding of AI and its implications for governance (OECD, 2025[1]). Individual interests and experiences with AI are increasingly seen as potential predictors of AI attitudes (Kanzola, Papaioannou and Petrakis, 2024[8]). On average across the OECD,"
  },
  {
    "figure_id": "F585",
    "report_id": "R020",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5.6. Familiarity with AI is associated with more positive expectations towards AI use in the public sector Share of respondents who are confident that AI use by government agencies can fulfil positive expectations for the respective item, by their self-"
  },
  {
    "figure_id": "F586",
    "report_id": "R020",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Regression analysis of the 2025 Trust Survey results points to several consistent governance drivers of optimism about AI in the public sector (Figure 5.7). $^{4}$ Importantly, the model includes all public governance dimensions measured in the survey, allowin"
  },
  {
    "figure_id": "F587",
    "report_id": "R020",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "In the face of this developing architecture, across the OECD, 42% of people believe it is likely that ## Figure 5.8. Around four in ten find it likely that government adequately regulates new technologies Share of the population who find it likely that their g"
  },
  {
    "figure_id": "F588",
    "report_id": "R020",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Public perception of government use of personal data remains moderately positive across OECD member countries. In 2025, 52% of people found it likely that government agencies use personal data only for legitimate purposes (see Figure 5.9). This share is 20 per"
  },
  {
    "figure_id": "F589",
    "report_id": "R020",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "\\- In Ireland (53%), Iceland (49%), and – to a lesser extent -- Luxembourg (39%), a relatively higher share of the population signed a petition in the past year. Irish and Icelandic people also more frequently posted political content on social media or boycot"
  },
  {
    "figure_id": "F590",
    "report_id": "R020",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "## 6.2.2. Most say voting has an impact on government actions Voting is seen as the key tool to influence policy (Chapter 7). A majority across the OECD believe that when people like them vote in elections or in a referendum, this can influence the policy deci"
  },
  {
    "figure_id": "F591",
    "report_id": "R020",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Confidence in one's own ability to participate in politics is also relatively low. Four in ten individuals are confident in their own ability to participate in politics, on average across OECD countries, with rates exceeding 50% in only Ireland, Mexico and Swi"
  },
  {
    "figure_id": "F592",
    "report_id": "R020",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Different types of in-person participation are perceived as less impactful than voting but still noteworthy. Volunteering (47% across the OECD and 45% across the European OECD accession candidate countries), striking (43% and 42%) and taking part in a protest "
  },
  {
    "figure_id": "F593",
    "report_id": "R020",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "## Around one-third choose to abstain from political activities Putting aside the sizeable shares who had no possibility to participate because of the absence of activities, the most common explanation for non-participation is “I chose not to participate”, sel"
  },
  {
    "figure_id": "F594",
    "report_id": "R020",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "## 6.3.3. Socioeconomic factors, like financial insecurity, influence ability to participate A second set of barriers is socioeconomic. Around 21% of people, on average across OECD countries, say that a barrier to political voice is having no time to engage in"
  },
  {
    "figure_id": "F595",
    "report_id": "R020",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Share that uses the respective media as a"
  },
  {
    "figure_id": "F596",
    "report_id": "R020",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "StatLink https://stat.link/d05hqz than the gap identified between people who feel like the political system lets people like them have a say and those who do not (see Chapter 2). In contrast, the gap in trust between individuals who identify a lack of engageme"
  },
  {
    "figure_id": "F597",
    "report_id": "R020",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "## 7.2.1. Trust in the national legislature is relatively low in OECD and participating OECD accession candidate countries Fewer than four in ten people (37%) across OECD countries report high or moderately high trust in the national legislature. A larger shar"
  },
  {
    "figure_id": "F598",
    "report_id": "R020",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 7.2. On average and in many individual countries, fewer people have high or moderately high trust in the national legislature than in national government Share of population with high or moderately high trust in the national legislature, government and "
  },
  {
    "figure_id": "F599",
    "report_id": "R020",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Share of population with high or moderately high trust in the national legislature, 2021, 2023 and 2025 Note: The figure presents the share who provided a response of 6 to 10 to the question \"On a scale of 0 to 10, where 0 is not at all and 10 is completely, h"
  },
  {
    "figure_id": "F600",
    "report_id": "R020",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "StatLink https://stat.link/8l9rdy Among individual characteristics, people's sense of political agency and their partisanship are the most relevant factors explaining variations in trust in national legislatures across OECD and accession candidate countries. B"
  },
  {
    "figure_id": "F601",
    "report_id": "R020",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Among individual characteristics, people's sense of political agency and their partisanship are the most relevant factors explaining variations in trust in national legislatures across OECD and accession candidate countries. By contrast, socioeconomic and demo"
  },
  {
    "figure_id": "F602",
    "report_id": "R020",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "## Figure 7.4. The share with high or moderately high trust in the national legislature is particularly low among individuals who do not believe people like them have a say in what government does Share of population with high or moderately high trust in the n"
  },
  {
    "figure_id": "F603",
    "report_id": "R020",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Costa Rica as well as Bulgaria, where the share of people reporting high trust is lower overall, regardless of respondents' sense of political voice. Likewise, trust in the legislature is also associated with people's confidence in their ability to participate"
  },
  {
    "figure_id": "F604",
    "report_id": "R020",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "## StatLink https://stat.link/lg7543 that individuals tend to report higher levels of trust when the party they voted for is in government or holds a larger share of seats in the legislature. $^{2}$ On average, the partisanship gap is substantially smaller for"
  },
  {
    "figure_id": "F605",
    "report_id": "R020",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "StatLink https://stat.link/lo94jt ## Figure 7.7. Feeling economically insecure is generally associated with lower trust in national legislatures Share of population with high or moderately high trust in the national legislature by financial concerns, 2025 Note"
  },
  {
    "figure_id": "F606",
    "report_id": "R020",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "This gap is substantially larger in New Zealand, as well as in Ireland and Sweden. By contrast, in Iceland, Korea, and Norway (and Brazil among accession candidate countries), women report higher levels of trust in legislatures than men do (Figure 7.8). Finall"
  },
  {
    "figure_id": "F607",
    "report_id": "R020",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "The education trust gap widened considerably, increasing by 7 percentage points, and representing the largest rise among all individual-level trust gaps (Figure 7.9). This increase is basically on part with the rise in the education trust gap with respect to t"
  },
  {
    "figure_id": "F608",
    "report_id": "R020",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "\\- People's perceptions of the responsiveness of the system, that is, their sense of whether they can influence what government does, are equally important for trust in the national legislature and the national government \\- At the same time, several other fac"
  },
  {
    "figure_id": "F609",
    "report_id": "R020",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Across OECD countries, the public governance variable most strongly associated with trust in national legislatures today is, by far, the perception that they adequately balance the needs of different regions and groups in society when discussing new policies. "
  },
  {
    "figure_id": "F610",
    "report_id": "R020",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "While receiving a meaningful reply from elected representatives is only one of many elements that can contribute to shaping people's perceptions of their representatives and legislatures, it is nonetheless important. In representative democracies, the very ide"
  },
  {
    "figure_id": "F611",
    "report_id": "R020",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "StatLink https://stat.link/v3iwmj ## 7.3.4. The relationship ## between most perceptions of day-to-day interactions and trust in legislature is relatively limited"
  },
  {
    "figure_id": "F612",
    "report_id": "R020",
    "label": "经合组织视觉摘要 1",
    "figure_type": "external_card",
    "context": "经合组织｜经合组织：不是意识形态而是治理能力，经合组织揭示政府信任的真正驱动力｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F613",
    "report_id": "R021",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "In Figure 1, the distribution of local tax shares of 92 countries in the OECD Global Revenue Statistics Database is shown. Out of 92 countries, the local tax share of 51 countries (56%) is less than 5 per cent, and in 68 countries (75%) the share is less than "
  },
  {
    "figure_id": "F614",
    "report_id": "R021",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Germany's model suggests that the binary choice between fiscal decentralisation and fiscal centralisation is a false one. What matters is not whether tax revenue is formally classified as local or central, but whether the institutional framework assigns revenu"
  },
  {
    "figure_id": "F615",
    "report_id": "R021",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "This challenge, however, is not confined to CDLT countries. Even in the LDLT (Tiebout Local Tax) countries, ensuring fiscal balance between central and subnational government is challenging. In LDLT countries, the responsibility to maintain a fair fiscal balan"
  },
  {
    "figure_id": "F616",
    "report_id": "R021",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "In Figure 2, where the trends of government debt of the eight selected OECD countries are shown, only Germany and Sweden show a stabilised government debt trend – the rising trajectory eventually curved – over the period 1995 to 2024 while the other six countr"
  },
  {
    "figure_id": "F617",
    "report_id": "R021",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2. Trend of government debt across levels of government (% of GDP)"
  },
  {
    "figure_id": "F618",
    "report_id": "R021",
    "label": "经合组织视觉摘要 1",
    "figure_type": "external_card",
    "context": "经合组织｜经合组织：不是地方税而是转移支付，经合组织重审92国财政分权数据｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F619",
    "report_id": "R022",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "\\- Supporting the role and emergence of specialised providers of affordable and social housing – whether public, semi-public, or private non- or limited-profit actors – to ensure the take up of funding and the effective delivery and management of affordable an"
  },
  {
    "figure_id": "F620",
    "report_id": "R022",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## What's the issue? Over the past three decades, real house prices have increased in nearly all OECD countries (Figure 1, Panel A), and the share of housing-related spending in total consumption spending has been on the rise, raising concerns about housing af"
  },
  {
    "figure_id": "F621",
    "report_id": "R022",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## Enable the development and funding of affordable and social housing One key driver of the housing affordability crisis is that housing investment has been uneven, with several shocks, including the Global Financial Crisis, the COVID-19 pandemic and the rise"
  },
  {
    "figure_id": "F622",
    "report_id": "R022",
    "label": "经合组织视觉摘要 1",
    "figure_type": "external_card",
    "context": "经合组织｜经合组织：住房支出挤压消费，经合组织给出一个被低估的政策工具｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F623",
    "report_id": "R023",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "## Revenue impact Since its inception, TIWB has supported 71 developing country tax administrations in raising an additional USD 2.72 billion in tax revenue collected, an additional USD 7.67 billion in tax assessed and disallowed USD 2.53 billion in carry forw"
  },
  {
    "figure_id": "F624",
    "report_id": "R023",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Total tax collected: USD 2.72 billion Total tax assessed: USD 7.67 billion Carry forward losses offset: USD 2.53 billion Note: The figures reflect results (in USD) of TIWB programmes from 2012 to 31 December 2025. All reported figures are generated through the"
  },
  {
    "figure_id": "F625",
    "report_id": "R023",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Note: The figures reflect results (in USD) of TIWB programmes from 2012 to 31 December 2025. All reported figures are generated through the collective work of TIWB and its partners, including ATAF. Figure 3.2. Geographical distribution of TIWB programmes Note:"
  },
  {
    "figure_id": "F626",
    "report_id": "R023",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "covers all aspects of the criminal case lifecycle, including intelligence gathering, evidence collection, analysis of large quantities of digital and physical evidence and identification of the ‘controlling minds’ behind Ugandan entities implicated in suspecte"
  },
  {
    "figure_id": "F627",
    "report_id": "R023",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Donor contributions play a pivotal role in ensuring the success, sustainability, and growth of the initiative. These generous financial and in-kind commitments empower TIWB to deliver specialised, hands-on assistance without any costs to tax administrations in"
  },
  {
    "figure_id": "F628",
    "report_id": "R023",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4.1. Countries and organisations supporting the TIWB initiative Canada Co-funded by the European Union SUOMI FINLAND Federal Ministry for Economic Cooperation and Development"
  },
  {
    "figure_id": "F629",
    "report_id": "R023",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "experiences, share practical insights, and benefit from diverse perspectives. This process enriches both sides, creating a spirit of mutual trust and co-operation that extends beyond individual missions. Equally important is the programme's emphasis on sustain"
  },
  {
    "figure_id": "F630",
    "report_id": "R023",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Türkiye remains committed to supporting TIWB and its objectives. As this is our first participation in the TIWB programme, we are particularly excited and eager to contribute actively, and we look forward to engaging in future missions as well. We are confiden"
  },
  {
    "figure_id": "F631",
    "report_id": "R023",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Additionally, TIWB welcomes the FTA's commitment to scale up its collective efforts in tax capacity building, including through strengthened support for the TIWB initiative (OECD Forum on Tax Administration, 2025 $^{[9]}$ ). France: Figure 4.2. TIWB partner ad"
  },
  {
    "figure_id": "F632",
    "report_id": "R023",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "France: Figure 4.2. TIWB partner administrations Australia: Belgium: Federal Public Service FINANCE Canada: Chile:"
  },
  {
    "figure_id": "F633",
    "report_id": "R023",
    "label": "经合组织视觉摘要 1",
    "figure_type": "external_card",
    "context": "经合组织｜经合组织：不是援助故事，经合组织十年帮发展中国家增收27亿美元｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F634",
    "report_id": "R024",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## 3.3 Overview of country scores Figure 2 shows the country scores for all OECD countries in 2025 – the rationale behind the scoring for each country is available in Annex A. The United States is represented by three states $^{2}$ : Florida (the least regulat"
  },
  {
    "figure_id": "F635",
    "report_id": "R024",
    "label": "经合组织视觉摘要 1",
    "figure_type": "external_card",
    "context": "经合组织｜经合组织：全球竞业限制法规的隐性成本与政策拐点｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F636",
    "report_id": "R025",
    "label": "Figure 29",
    "figure_type": "source_exhibit",
    "context": "Figure 30 Addressing external debt challenges....46 Annex 1 Developing countries by region and level of integration into global capital markets....53 Annex 2 Coupon rates on new bond issuances....54 Annex 3 Maturities on new bond issuances....55 Annex 4 Intere"
  },
  {
    "figure_id": "F637",
    "report_id": "R025",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "External inflows of financial capital reflect the money and liquid assets that are sourced from non-residents and used by companies, individuals and governments to finance operations and activities, invest and generate future streams of revenue. These inflows "
  },
  {
    "figure_id": "F638",
    "report_id": "R025",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "A significant and growing financing gap – estimated at around \\$4.3 trillion per year (UNCTAD, 2023b) – exists between the domestic and external financing resources that developing countries can access, and what they need to finance the investments required to"
  },
  {
    "figure_id": "F639",
    "report_id": "R025",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Collectively, developing countries need to increase their investment from \\$13.4 trillion to around \\$17.7 trillion annually to achieve their SDG targets Figure 2 Closing the SDG financing gap Implications of closing the annual financing gap from external and "
  },
  {
    "figure_id": "F640",
    "report_id": "R025",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Note: \\*It has been assumed that the financing gap is financed in proportion to the average contributions of domestic financing and the composition of external financing between 2014 and 2024. However, there was significant variation in the degree to which dif"
  },
  {
    "figure_id": "F641",
    "report_id": "R025",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "However, there was significant variation in the degree to which different country groups accessed external financing sources to finance their gross capital formation in 2024 (Figure 3). Developed countries received the equivalent of 38 per cent of the financin"
  },
  {
    "figure_id": "F642",
    "report_id": "R025",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "significant declines in the contribution of external financing to gross capital formation Relative trends in gross capital formation and external and domestic financing in developing countries ## Figure 4"
  },
  {
    "figure_id": "F643",
    "report_id": "R025",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "gross capital formation Relative trends in gross capital formation and external and domestic financing in developing countries ## Figure 4 Non-resident financial flows to developing countries by type (Billions of dollars) ## Figure 5"
  },
  {
    "figure_id": "F644",
    "report_id": "R025",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Relative trends in gross capital formation and external and domestic financing in developing countries ## Figure 4 Non-resident financial flows to developing countries by type (Billions of dollars) ## Figure 5 Note: In 2015 there was a net withdrawal of other "
  },
  {
    "figure_id": "F645",
    "report_id": "R025",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Non-resident financial flows to developing countries by type (Billions of dollars) ## Figure 5 Note: In 2015 there was a net withdrawal of other investment and in 2022 a net withdrawal of portfolio investment in developing countries by non-residents. This vola"
  },
  {
    "figure_id": "F646",
    "report_id": "R025",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "This volatility in external flows is highly synchronized with the global economic cycle and creates specific challenges for developing countries that exacerbate exchange rate volatility, amplify the counter-cyclical nature of debt servicing costs and necessita"
  },
  {
    "figure_id": "F647",
    "report_id": "R025",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "Since few ODEs have functioning securities markets, they are more dependent on direct and other investment inflows, with the latter comprised largely of loan instruments. In contrast to this, EMEs have securities markets integrated into global financial market"
  },
  {
    "figure_id": "F648",
    "report_id": "R025",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "Regionally, transfers from other governments were more important for Africa than for Asia and the Pacific but were also higher for developed countries than for developing ones. Direct investment was a larger"
  },
  {
    "figure_id": "F649",
    "report_id": "R025",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Average composition of external non-resident financial flows to countries from 2014 to 2024 ## Figure 7 ## Direct investment has mattered more to developing countries ## Figure 8 ## Financial flows give rise to stocks of liabilities"
  },
  {
    "figure_id": "F650",
    "report_id": "R025",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "## Figure 7 ## Direct investment has mattered more to developing countries ## Figure 8 ## Financial flows give rise to stocks of liabilities The composition of accumulated stocks of external liabilities of developing countries in 2024 (Trillions of dollars)"
  },
  {
    "figure_id": "F651",
    "report_id": "R025",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "## Figure 8 ## Financial flows give rise to stocks of liabilities The composition of accumulated stocks of external liabilities of developing countries in 2024 (Trillions of dollars) The servicing of these stocks through the payment of profits, royalties and i"
  },
  {
    "figure_id": "F652",
    "report_id": "R025",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Primary income outflows from developing countries to service their external liabilities are matched in scale by the investment returns received by non-residents (Figure 9). ## 2.3 Costs of servicing the accumulated stocks of foreign liabilities The costs of se"
  },
  {
    "figure_id": "F653",
    "report_id": "R025",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "The costs paid by recipient countries to service their external liabilities also represent the returns earned by non-resident investors Figure 9 Servicing costs paid and returns received Primary income payments from developing countries in 2024 (Billions of do"
  },
  {
    "figure_id": "F654",
    "report_id": "R025",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Comparative costs of servicing external liabilities Median annual cost (Per cent per annum) - Developed countries - Developing countries Figure 10 Direct Investment"
  },
  {
    "figure_id": "F655",
    "report_id": "R025",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "- Developed countries - Developing countries Figure 10 Direct Investment Portfolio Investment"
  },
  {
    "figure_id": "F656",
    "report_id": "R025",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Figure 10 Direct Investment Portfolio Investment"
  },
  {
    "figure_id": "F657",
    "report_id": "R025",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "## Different costs in developing and developed countries Median costs of servicing direct, portfolio and other investment in developed and developing countries (Per cent per annum) Other Investment ## Figure 12"
  },
  {
    "figure_id": "F658",
    "report_id": "R025",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "## Different costs in developing and developed countries Median costs of servicing direct, portfolio and other investment in developed and developing countries (Per cent per annum) Other Investment ## Figure 12 ## Costs differ depending on levels of financial "
  },
  {
    "figure_id": "F659",
    "report_id": "R025",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "(Per cent per annum) Other Investment ## Figure 12 ## Costs differ depending on levels of financial integration Comparative median annual costs of servicing direct, portfolio and other investment in EMEs, FMEs and ODEs"
  },
  {
    "figure_id": "F660",
    "report_id": "R025",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "## Figure 12 ## Costs differ depending on levels of financial integration Comparative median annual costs of servicing direct, portfolio and other investment in EMEs, FMEs and ODEs Other Investment Other Investment"
  },
  {
    "figure_id": "F661",
    "report_id": "R025",
    "label": "Figure 13",
    "figure_type": "source_exhibit",
    "context": "Comparative median annual costs of servicing direct, portfolio and other investment in EMEs, FMEs and ODEs Other Investment Other Investment ## Figure 13 There are also regional variations in costs Comparative median costs of direct, portfolio and other invest"
  },
  {
    "figure_id": "F662",
    "report_id": "R025",
    "label": "Figure 13",
    "figure_type": "source_exhibit",
    "context": "Other Investment Other Investment ## Figure 13 There are also regional variations in costs Comparative median costs of direct, portfolio and other investment in developing regions (Per cent per annum) Asia and the Pacific Latin America and the Caribbean Africa"
  },
  {
    "figure_id": "F663",
    "report_id": "R025",
    "label": "Figure 13",
    "figure_type": "source_exhibit",
    "context": "## Figure 13 There are also regional variations in costs Comparative median costs of direct, portfolio and other investment in developing regions (Per cent per annum) Asia and the Pacific Latin America and the Caribbean Africa ## 2.4 Costs of equity and debt f"
  },
  {
    "figure_id": "F664",
    "report_id": "R025",
    "label": "Figure 14",
    "figure_type": "source_exhibit",
    "context": "Comparative median costs of direct, portfolio and other investment in developing regions (Per cent per annum) Asia and the Pacific Latin America and the Caribbean Africa ## 2.4 Costs of equity and debt financing instruments When viewed through the lens of thei"
  },
  {
    "figure_id": "F665",
    "report_id": "R025",
    "label": "Figure 14",
    "figure_type": "source_exhibit",
    "context": "Asia and the Pacific Latin America and the Caribbean Africa ## 2.4 Costs of equity and debt financing instruments When viewed through the lens of their type of instrument, rather than their functional category, equity and debt have followed different trajector"
  },
  {
    "figure_id": "F666",
    "report_id": "R025",
    "label": "Figure 14",
    "figure_type": "source_exhibit",
    "context": "When viewed through the lens of their type of instrument, rather than their functional category, equity and debt have followed different trajectories. Whereas the stock of equity increased faster than the cost between 2014 and 2024, debt servicing costs increa"
  },
  {
    "figure_id": "F667",
    "report_id": "R025",
    "label": "Figure 15",
    "figure_type": "source_exhibit",
    "context": "countries The significant increase in the cost of external debt financing is more problematic for the many developing countries that have low domestic savings rates, shallow domestic capital markets and a reliance on the public sector to undertake the necessar"
  },
  {
    "figure_id": "F668",
    "report_id": "R025",
    "label": "Figure 16",
    "figure_type": "source_exhibit",
    "context": "A counter-factual experiment reveals that if 94 developing countries could borrow at the same rates as developed countries, they would collectively save around \\$500 billion per year in interest payments. Each year, these savings could finance the construction"
  },
  {
    "figure_id": "F669",
    "report_id": "R025",
    "label": "Figure 17",
    "figure_type": "source_exhibit",
    "context": "The need to devote an increasing share of government revenues to interest payments reduces fiscal space and crowds out other public spending, including that required to achieve the SDG targets. Seventy-three per cent of developing countries experienced a decli"
  },
  {
    "figure_id": "F670",
    "report_id": "R025",
    "label": "Figure 16",
    "figure_type": "source_exhibit",
    "context": "## Figure 16 Trends in general government interest costs and government revenue in developing countries ## Figure 17 Most developing countries have lost fiscal space due to rising interest costs Share of developing countries that have lost (-) or gained (+) fi"
  },
  {
    "figure_id": "F671",
    "report_id": "R025",
    "label": "Figure 17",
    "figure_type": "source_exhibit",
    "context": "## Figure 17 Most developing countries have lost fiscal space due to rising interest costs Share of developing countries that have lost (-) or gained (+) fiscal space, measured as interest payments as a share of government revenue ## Box 2"
  },
  {
    "figure_id": "F672",
    "report_id": "R025",
    "label": "Figure 17",
    "figure_type": "source_exhibit",
    "context": "## Figure 17 Most developing countries have lost fiscal space due to rising interest costs Share of developing countries that have lost (-) or gained (+) fiscal space, measured as interest payments as a share of government revenue ## Box 2 ## The development i"
  },
  {
    "figure_id": "F673",
    "report_id": "R025",
    "label": "Figure 18",
    "figure_type": "source_exhibit",
    "context": "Even as monetary policy in advanced economies has begun to ease, borrowing contracted during the tightening phase is locking in higher costs, constraining fiscal space and risking the crowding out of development spending in the years ahead. External sovereign "
  },
  {
    "figure_id": "F674",
    "report_id": "R025",
    "label": "Figure 18",
    "figure_type": "source_exhibit",
    "context": "## Figure 18 ## Bonds and multilateral loans dominate external debt financing Composition of external PPG debt in developing countries (Trillions of dollars) Note: Multilateral loans include the use of IMF credits and SDR allocations. Private loans include cre"
  },
  {
    "figure_id": "F675",
    "report_id": "R025",
    "label": "Figure 19",
    "figure_type": "source_exhibit",
    "context": "## 4.1 Debt securities Debt securities have become an increasingly important"
  },
  {
    "figure_id": "F676",
    "report_id": "R025",
    "label": "Figure 19",
    "figure_type": "source_exhibit",
    "context": "In 2024, external issuance started to regain momentum and in 2025 developing countries issued a record amount of fixed coupon bonds worth \\$164 billion (Figure 19) $^{8}$ . While the number of transactions remained below previous annual records, issuances were"
  },
  {
    "figure_id": "F677",
    "report_id": "R025",
    "label": "Figure 20",
    "figure_type": "source_exhibit",
    "context": "Sovereign bond issuance rebounded in 2025 Annual value (Billions of dollars) and number of issuances Amount issued Note: Includes all fixed-coupon bonds issued by developing countries since 2010 in dollars, euros, and yen available through LSEG Data & Analytic"
  },
  {
    "figure_id": "F678",
    "report_id": "R025",
    "label": "Figure 20",
    "figure_type": "source_exhibit",
    "context": "Note: Includes all fixed-coupon bonds issued by developing countries since 2010 in dollars, euros, and yen available through LSEG Data & Analytics. Although financial integration has been progressing in recent decades, not all developing countries enjoy equal "
  },
  {
    "figure_id": "F679",
    "report_id": "R025",
    "label": "Figure 20",
    "figure_type": "source_exhibit",
    "context": "Issuance is also highly unequal across regions, with most developing countries' foreign currency bonds having been issued in Asia and the Pacific and in Latin America and the Caribbean (Figure 20). Only 14 per cent of issuances originated in Africa since 1990,"
  },
  {
    "figure_id": "F680",
    "report_id": "R025",
    "label": "Figure 20",
    "figure_type": "source_exhibit",
    "context": "## Figure 20 Access to international bond markets remains uneven Share of issuance value by EME, FME and ODE (Per cent) Share of issuance value by developing regions (Per cent) Note: Includes all fixed-coupon bonds issued by developing countries since 2010 in "
  },
  {
    "figure_id": "F681",
    "report_id": "R025",
    "label": "Figure 21",
    "figure_type": "source_exhibit",
    "context": "The prices at which developing countries can borrow – as indicated by secondary market yields – reflect the evolving cost of debt in international bond markets. Starting in 2010, increasing investor risk appetite and low global interest rates generated large-s"
  },
  {
    "figure_id": "F682",
    "report_id": "R025",
    "label": "Figure 23",
    "figure_type": "source_exhibit",
    "context": "Note: Includes all fixed-coupon bonds issued by developing countries since 1990 in dollars, euros, and yen available through LSEG Data & Analytics. Defaulted bonds are excluded. Bonds are weighted by market value and excluded within one year of maturity. All d"
  },
  {
    "figure_id": "F683",
    "report_id": "R025",
    "label": "Figure 23",
    "figure_type": "source_exhibit",
    "context": "-- All developing countries Asia and the Pacific Latin America and the Caribbean Borrowing conditions improved in 2024 and 2025, with average yields in developing countries declining from their peak of 7.3 per cent in 2023 to 5.7 per cent in 2025. Fuelled by a"
  },
  {
    "figure_id": "F684",
    "report_id": "R025",
    "label": "Figure 23",
    "figure_type": "source_exhibit",
    "context": "Sovereign spreads – the premium demanded by investors over safe assets such as United States Treasuries, German Bunds, and Japanese government bonds – also narrowed substantially during 2024 and 2025 (Figure 23). In 2025 the average spread of developing countr"
  },
  {
    "figure_id": "F685",
    "report_id": "R025",
    "label": "Figure 22",
    "figure_type": "source_exhibit",
    "context": "Figure 22 ## Borrowing conditions in FMEs and Africa remained tight at the end of 2025 Note: Includes all fixed-coupon bonds issued by developing countries since 1990 in dollars, euros, and yen available through LSEG Data & Analytics. Defaulted bonds are exclu"
  },
  {
    "figure_id": "F686",
    "report_id": "R025",
    "label": "Figure 22",
    "figure_type": "source_exhibit",
    "context": "Figure 22 ## Borrowing conditions in FMEs and Africa remained tight at the end of 2025 Note: Includes all fixed-coupon bonds issued by developing countries since 1990 in dollars, euros, and yen available through LSEG Data & Analytics. Defaulted bonds are exclu"
  },
  {
    "figure_id": "F687",
    "report_id": "R025",
    "label": "Figure 23",
    "figure_type": "source_exhibit",
    "context": "Note: Includes all fixed-coupon bonds issued by developing countries since 1990 in dollars, euros, and yen available through LSEG Data & Analytics. Defaulted bonds are excluded. Bonds are weighted by market value and excluded within one year of maturity. Sprea"
  },
  {
    "figure_id": "F688",
    "report_id": "R025",
    "label": "Figure 23",
    "figure_type": "source_exhibit",
    "context": "## Figure 23 ## Sovereign spreads have narrowed to historic lows Yearly average spreads of developing country bonds relative to the benchmark rates (Basis points) Note: Includes all fixed-coupon bonds issued by developing countries since 1990 in dollars, euros"
  },
  {
    "figure_id": "F689",
    "report_id": "R025",
    "label": "Figure 24",
    "figure_type": "source_exhibit",
    "context": "Yearly average spreads of developing country bonds relative to the benchmark rates (Basis points) Note: Includes all fixed-coupon bonds issued by developing countries since 1990 in dollars, euros, and yen available through LSEG Data & Analytics. Defaulted bond"
  },
  {
    "figure_id": "F690",
    "report_id": "R025",
    "label": "Figure 24",
    "figure_type": "source_exhibit",
    "context": "Note: Includes all fixed-coupon bonds issued by developing countries since 1990 in dollars, euros, and yen available through LSEG Data & Analytics. Defaulted bonds are excluded. Bonds are weighted by market value and excluded within one year of maturity. Matur"
  },
  {
    "figure_id": "F691",
    "report_id": "R025",
    "label": "Figure 24",
    "figure_type": "source_exhibit",
    "context": "## Figure 24 ## Borrowing premia remained significant in some countries Yearly average spreads of developing country bonds relative to the benchmark rates (Basis points) -- All developing countries Asia and the Pacific"
  },
  {
    "figure_id": "F692",
    "report_id": "R025",
    "label": "Figure 24",
    "figure_type": "source_exhibit",
    "context": "Note: Includes all fixed-coupon bonds issued by developing countries since 1990 in dollars, euros, and yen available through LSEG Data & Analytics. Defaulted bonds are excluded. Bonds are weighted by market value and excluded within one year of maturity. Matur"
  },
  {
    "figure_id": "F693",
    "report_id": "R025",
    "label": "Figure 25",
    "figure_type": "source_exhibit",
    "context": "## Coupon rates and maturities Although borrowing conditions improved, coupon rates on new bond issues remained high in 2025 (Figure 25). Coupon rates, the contractual interest rates set at issuance, do not adjust after issuance and therefore lock countries in"
  },
  {
    "figure_id": "F694",
    "report_id": "R025",
    "label": "Figure 26",
    "figure_type": "source_exhibit",
    "context": "In 2025, the average coupon rate for all developing countries stood at 5.8 per cent, with significantly higher rates – close to 8 per cent – for FMEs and African sovereigns. EMEs and borrowers in Asia and the Pacific and Latin America and the Caribbean faced m"
  },
  {
    "figure_id": "F695",
    "report_id": "R025",
    "label": "Figure 26",
    "figure_type": "source_exhibit",
    "context": "access. Consequently, the easing of market conditions is not always fully reflected in the observed coupon rates. Borrowing conditions depend not only on interest rates but also on the maturity of debt contracts. Long-term finance is essential for funding inve"
  },
  {
    "figure_id": "F696",
    "report_id": "R025",
    "label": "Figure 27",
    "figure_type": "source_exhibit",
    "context": "Note: The secondary market yield is calculated as the market-value-weighted average yield-to-maturity of all outstanding bonds of the same country on the date before a new bond's issuance. Includes all fixed-coupon bonds issued by developing countries since 19"
  },
  {
    "figure_id": "F697",
    "report_id": "R025",
    "label": "Figure 27",
    "figure_type": "source_exhibit",
    "context": "## Figure 27 ## Long-term borrowing carries a cost premium Average maturity and coupon rate on bonds in developing countries (Per cent) Note: Short-term bonds are bonds with a maturity lower than 5 years, medium-term are between 5 and 10 years, long-term inclu"
  },
  {
    "figure_id": "F698",
    "report_id": "R025",
    "label": "Figure 28",
    "figure_type": "source_exhibit",
    "context": "## Figure 28 Interest rates on loans have soared Average interest rate on new external loan commitments to developing countries by creditor type (Per cent per annum) ••• Average across creditor type Note: Interest rates are weighted by value of new commitments"
  },
  {
    "figure_id": "F699",
    "report_id": "R025",
    "label": "Figure 30",
    "figure_type": "source_exhibit",
    "context": "While the scale and servicing costs associated with equity flows are considerable, the analysis highlights that the principal drivers of increased costs and volatility arise from external debt dynamics. The policy proposals that follow address these challenges"
  },
  {
    "figure_id": "F700",
    "report_id": "R025",
    "label": "Figure 30",
    "figure_type": "source_exhibit",
    "context": "## Figure 30 ## Addressing external debt challenges The Theory of Change as it relates to external debt flows to developing countries ## Policies"
  },
  {
    "figure_id": "F701",
    "report_id": "R025",
    "label": "Figure 30",
    "figure_type": "source_exhibit",
    "context": "## Figure 30 ## Addressing external debt challenges The Theory of Change as it relates to external debt flows to developing countries ## Policies • National-level measures"
  },
  {
    "figure_id": "F702",
    "report_id": "R025",
    "label": "联合国贸发会议视觉摘要 1",
    "figure_type": "external_card",
    "context": "联合国贸发会议｜联合国贸发会议：联合国贸发报告，发展中国家每流入1美元，72美分流回境外｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F703",
    "report_id": "R026",
    "label": "联合国贸发会议视觉摘要 1",
    "figure_type": "external_card",
    "context": "联合国贸发会议｜联合国贸发会议：从17万亿到27万亿美元，电商增长背后，环境账本敲响警钟｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F704",
    "report_id": "R027",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "$^{5}$ The coefficient of variation reaches 23 in the case of number of deaths, nine and four for affected population and total damage respectively. Figure 1 Looking at the evolution of climate-related disasters over time, EM-DAT data portend a substantial inc"
  },
  {
    "figure_id": "F705",
    "report_id": "R027",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1 Looking at the evolution of climate-related disasters over time, EM-DAT data portend a substantial increase in the average frequency of climate-related disasters in developing countries, particularly between the early-1980s and the early 2000s (Figure"
  },
  {
    "figure_id": "F706",
    "report_id": "R027",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "excludes outside values Based on the granular data described above, the rest of the paper uses four complementary measures to gauge countries' exposure to – or intensity of – natural disasters over a given period T. The first measure is the frequency of disast"
  },
  {
    "figure_id": "F707",
    "report_id": "R027",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "excludes outside values Based on the granular data described above, the rest of the paper uses four complementary measures to gauge countries' exposure to – or intensity of – natural disasters over a given period T. The first measure is the frequency of disast"
  },
  {
    "figure_id": "F708",
    "report_id": "R027",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Similarly to the normalized frequency, the normalized intensity is expressed as a share of the total population thereby accounting for countries' size. Subsequent sections of the paper will employ the above metrics both in aggregate form – that is, by aggregat"
  },
  {
    "figure_id": "F709",
    "report_id": "R027",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3 Frequency, intensity and normalized frequency of natural disasters in developing countries (2021–2023) SIDS OTHERS Droughts Floods Storms Other Climate-Related Disasters Normalized intensity Second, compared to other developing countries SIDS tend to "
  },
  {
    "figure_id": "F710",
    "report_id": "R027",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Frequency, intensity and normalized frequency of natural disasters in developing countries (2021–2023) SIDS OTHERS Droughts Floods Storms Other Climate-Related Disasters Normalized intensity Second, compared to other developing countries SIDS tend to be more e"
  },
  {
    "figure_id": "F711",
    "report_id": "R027",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Second, compared to other developing countries SIDS tend to be more exposed to certain types of disasters and less exposed to others (Figure 4). Between 1979 and 2023, storms accounted for nearly 71 per cent of all recorded disasters in SIDS, in contrast to th"
  },
  {
    "figure_id": "F712",
    "report_id": "R027",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4 Incidence of natural disasters, by region and type (1979–2023) Percentage of missing data for socio-economic impacts of disasters, by type, metrics and region, (1979–2023) The bottom line is that triangulating metrics and exploiting their complementar"
  },
  {
    "figure_id": "F713",
    "report_id": "R027",
    "label": "联合国贸发会议视觉摘要 1",
    "figure_type": "external_card",
    "context": "联合国贸发会议｜联合国贸发会议：小岛国灾害后增长损失被系统性低估｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F714",
    "report_id": "R028",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "The software and computer services, technology hardware and equipment and pharmaceuticals and biotechnology industries are largely headquartered in the United States, which accounts for more than 80 per cent of the corporate R&D investment in software and comp"
  },
  {
    "figure_id": "F715",
    "report_id": "R028",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## Significant concentration of research and development in a few countries (Share of investment by global top 100 corporate R&D investors, by country; percentage) ## Figure 1.5 The share of R&D in software and computer services has increased sharply (Share of"
  },
  {
    "figure_id": "F716",
    "report_id": "R028",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## Figure 1.5 The share of R&D in software and computer services has increased sharply (Share of investment by global top 100 corporate R&D investors, by industry; percentage) ## C. Asymmetries in knowledge creation China and the United States lead in knowledg"
  },
  {
    "figure_id": "F717",
    "report_id": "R028",
    "label": "联合国贸发会议视觉摘要 1",
    "figure_type": "external_card",
    "context": "联合国贸发会议｜联合国贸发会议：联合国报告，AI或侵蚀发展中国家廉价劳动力优势｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F718",
    "report_id": "R029",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## An opportunity for Latin America. Against the backdrop of a (still uneven) global push toward decarbonization, Latin American countries are well positioned to embark on a green transition and accelerate progress on the SDGs. As reported by the UNFCCC, $^{3}"
  },
  {
    "figure_id": "F719",
    "report_id": "R029",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "IRENA, 33% of its total energy supply currently comes from renewable sources compared to only 13% globally. $^{4}$ ## Figure 1. Renewable Energy Production as a Share of Total Energy Generation and Type of Specialization by Country. According to USGS's Mineral"
  },
  {
    "figure_id": "F720",
    "report_id": "R029",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "According to USGS's Mineral Commodity Summaries, the region is also home to important reserves of critical minerals: more than half the world's lithium, used in electric-vehicle batteries; over a third of its copper, for electrical wiring; and more than half i"
  },
  {
    "figure_id": "F721",
    "report_id": "R029",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "According to USGS's Mineral Commodity Summaries, the region is also home to important reserves of critical minerals: more than half the world's lithium, used in electric-vehicle batteries; over a third of its copper, for electrical wiring; and more than half i"
  },
  {
    "figure_id": "F722",
    "report_id": "R029",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2. Selected Critical Minerals Production in Latin American Countries as percentage of total World Production Lithium, mine production Copper There are, however, challenges in the horizon. Beyond the environmental risks of mining in terms of deforestatio"
  },
  {
    "figure_id": "F723",
    "report_id": "R029",
    "label": "联合国贸发会议视觉摘要 1",
    "figure_type": "external_card",
    "context": "联合国贸发会议｜联合国贸发会议：绿色转型不是市场能解决的，联合国贸发会议谈拉美产业政策｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F724",
    "report_id": "R030",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "L'objectif de la présente étude est d'apporter un éclairage stratégique sur la situation et les perspectives de développement des PME béninoises dans un contexte d'intégration économique régionale accrue, en particulier au sein des marchés intra-africains. Ell"
  },
  {
    "figure_id": "F725",
    "report_id": "R030",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Le dynamisme du secteur primaire, la resilience du secteur secondaire et la consolidation du secteur tertiaire ont également contribué à une amélioration progressive du niveau de vie, avec le revenu par habitant passant de 973 dollars en 2010 à 1 485 dollars e"
  },
  {
    "figure_id": "F726",
    "report_id": "R030",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "L'orientation des ressources empruntées vers des projets structurants (infrastructures, énergie, zones industrielles) assure une meilleure soutenabilité à long terme. ## Figure 1 Évolution du taux de croissance annuel du PIB entre 2010 et 2024 En pourcentage s"
  },
  {
    "figure_id": "F727",
    "report_id": "R030",
    "label": "figure 2",
    "figure_type": "source_exhibit",
    "context": "La loi 2020-03 élargit la catégorie PME aux entités n'excédant pas 200 salariés, avec un chiffre d'affaires annuelmaximal de 2 milliards FCFA et un investissement inférieur ou égal à 1 milliard FCFA. Cette clarification normative a permis une meilleure identif"
  },
  {
    "figure_id": "F728",
    "report_id": "R030",
    "label": "figure 2",
    "figure_type": "source_exhibit",
    "context": "Le développement des PME est identifié comme un levier clé pour créer des emplois productifs et décents. Elles génèrent les deux tiers des nouveaux emplois et constituent un moteur pour une croissance durable. Voir figure 2. ## Figure 2 Nombre d'emplois créés "
  },
  {
    "figure_id": "F729",
    "report_id": "R030",
    "label": "figure 3",
    "figure_type": "source_exhibit",
    "context": "## 1.3.1. L'évolution des échanges extérieures avec une croissance de 92,95 %, s'élevant à 643 millions de dollars en 2024 (voir figure 3). La part des exportations béninoises vers l'Afrique, dans les exportations totales, connaît une évolution décroissante, p"
  },
  {
    "figure_id": "F730",
    "report_id": "R030",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Exportations totales du Bénin (en millions de dollars) ## Figure 3 Évolution des exportations et importations du Bénin (partenaire : Afrique vs le monde) Importations totales du Bénin (en millions de dollars)"
  },
  {
    "figure_id": "F731",
    "report_id": "R030",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "## Figure 3 Évolution des exportations et importations du Bénin (partenaire : Afrique vs le monde) Importations totales du Bénin (en millions de dollars)"
  },
  {
    "figure_id": "F732",
    "report_id": "R030",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "le Togo, le Ghana et la Côte d'Ivoire, constitue le levier essentiel pour consolider la résilience du commerce extérieur béninois et inscrire les PME dans une dynamique durable d'intégration régionale ## 1.3.2. Structure des filières exportatrices et potentiel"
  },
  {
    "figure_id": "F733",
    "report_id": "R030",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "## 1.3.2. Structure des filières exportatrices et potentiel de montée en valeur. La structure des exportations béninoises vers l'Afrique repose sur trois filières majeures (Figure 4), qui définissent le profil compétitif du pays et offrent des leviers concrets"
  },
  {
    "figure_id": "F734",
    "report_id": "R030",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Toutefois, à partir de 2016, les exportateurs béninois ont amorcé une stratégie de diversification géographique. Le double choc de 2014–2016 (effondrement des cours du coton et récession nigériane) a totalement réconfiguré les débouchés africains du Bénin. La "
  },
  {
    "figure_id": "F735",
    "report_id": "R030",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "## Figure 5 Top des destinations des exportations béninoises en 2008, 2016 et 2024 Top destination des exportations béninoises en 2008 Top destination des exportations béninoises en 2016 Top destination des exportations béninoises en 2024"
  },
  {
    "figure_id": "F736",
    "report_id": "R030",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "## Figure 5 Top des destinations des exportations béninoises en 2008, 2016 et 2024 Top destination des exportations béninoises en 2008 Top destination des exportations béninoises en 2016 Top destination des exportations béninoises en 2024"
  },
  {
    "figure_id": "F737",
    "report_id": "R030",
    "label": "figure 6",
    "figure_type": "source_exhibit",
    "context": "Ce segment regroupe les fruits entiers, frais ou déshydratés. Il s'agit du produit le moins transformé, nécessitant néanmoins des infrastructures logistiques adaptées (chaîne du froid, conditionnement) et une standardisation stricte des calibres pour accéder a"
  },
  {
    "figure_id": "F738",
    "report_id": "R030",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "En 2022, la filière entre dans une nouvelle dynamique ascendante avec une croissance de plus de 246 % pour atteinre un record historique de 40 286 dollars en 2024. Cette relance témoigne d'un regain de demande impulsé par des efforts combinés d'investissements"
  },
  {
    "figure_id": "F739",
    "report_id": "R030",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "partagent près de 88 % des échanges intra africains (voir Figure 7). Le Kenya et la Tanzanie, bien que plus éloignés, affichent respectivement 480 635 et 169 031 dollars. Ces cinq pays bénéficient d'infrastructures logistiques performantes (ports, plateformes "
  },
  {
    "figure_id": "F740",
    "report_id": "R030",
    "label": "figure 8",
    "figure_type": "source_exhibit",
    "context": "## 2.1.2 Jus d'ananas frais (≤ 20°Brix) observée confirme que le Bénin a développé un avantage comparatif dynamique fondé sur une combinaison de compétitivité-prix et de proximité géographique des marchés. ## Figure 8 Évolution des exportations de Jus d'ananas"
  },
  {
    "figure_id": "F741",
    "report_id": "R030",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "observée confirme que le Bénin a développé un avantage comparatif dynamique fondé sur une combinaison de compétitivité-prix et de proximité géographique des marchés. ## Figure 8 Évolution des exportations de Jus d'ananas frais du Bénin vers l'Afrique En millie"
  },
  {
    "figure_id": "F742",
    "report_id": "R030",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "## Figure 9 Principaux pays exportateurs Jus d'ananas frais en Afrique en 2024"
  },
  {
    "figure_id": "F743",
    "report_id": "R030",
    "label": "figure 10",
    "figure_type": "source_exhibit",
    "context": "L'année 2020 a cristallisé l'impact des chocs externes : les exportations sont ## Figure 10 En milliers de Dollars"
  },
  {
    "figure_id": "F744",
    "report_id": "R030",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "## Figure 10 En milliers de Dollars"
  },
  {
    "figure_id": "F745",
    "report_id": "R030",
    "label": "Figure\n\n11",
    "figure_type": "source_exhibit",
    "context": "Sur le marché continental du jus d'ananas concentré, le Bénin reste un acteur marginal. En 2024, la part du Bénin sur le marché intra-africain des jus d'ananas concentrés est inférieure à 1 % (voir Figure Principaux pays exportateurs de Jus d'ananas concentré "
  },
  {
    "figure_id": "F746",
    "report_id": "R030",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "Selon les données de l'Observatoire de la complexité économique $^{24}$ , le commerce international du fer et de l'acier (SH-72) a atteint environ 477 milliards de dollars en 2023, soit une baisse de 17,2 % par rapport à 2022. Cette categorie représente enviro"
  },
  {
    "figure_id": "F747",
    "report_id": "R030",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "## Figure 12 Part des exportations et importations du fer et de l'acier dans le total des exportations africaines vers le monde (top 10) Exportations Importations"
  },
  {
    "figure_id": "F748",
    "report_id": "R030",
    "label": "Figure 13",
    "figure_type": "source_exhibit",
    "context": "L'ensemble de ces capacités industrielles reflète une diversification avancée dans les maillons aval de la chaîne de valeur. La demande intérieure en fer à béton est tirée par une activité soutenue dans le secteur du Bâtiment et Travaux Publics : urbanisation "
  },
  {
    "figure_id": "F749",
    "report_id": "R030",
    "label": "Figure 13",
    "figure_type": "source_exhibit",
    "context": "La chaîne de valeur du fer et de l'acier débute par l'identification et le développement de ressources minérales et énergétiques. Les principaux gisements (notamment les formations riches en hématite ou en magnétite) sont évalués selon leur teneur en fer, la p"
  },
  {
    "figure_id": "F750",
    "report_id": "R030",
    "label": "Figure 15",
    "figure_type": "source_exhibit",
    "context": "automobiles désaffectés, ou encore des zones artisanales (menuiseries métalliques, soudeurs, etc.). Des centres semi-industriels de tri peuvent être installés le long des axes Cotonou–Parakou ou Cotonou–Malanville, en articulation avec les collectivités locale"
  },
  {
    "figure_id": "F751",
    "report_id": "R030",
    "label": "Figure 15",
    "figure_type": "source_exhibit",
    "context": "Évolution des exportations des produits de l'acier et l'acier inoxydable En Dollars"
  },
  {
    "figure_id": "F752",
    "report_id": "R030",
    "label": "Figure 17",
    "figure_type": "source_exhibit",
    "context": "Cette dualité forte – exportations très concentrées sur quelques gros clients et importations dominées par un nombre restreint de fournisseurs – illustre la structure incomplète de la chaîne locale de valeur : le Bénin assemble et transforme en majorité des tô"
  },
  {
    "figure_id": "F753",
    "report_id": "R030",
    "label": "Figure 16",
    "figure_type": "source_exhibit",
    "context": "Cette orientation est d'autant plus porteuse que des réseaux de formation technique (CFP, écoles industrielles régionales) $^{38}$ ont été renforcés depuis 2016 par l'État et les partenaires techniques. Les PME peuvent ainsi recruter une main-d'œuvre progressi"
  },
  {
    "figure_id": "F754",
    "report_id": "R030",
    "label": "Figure 17",
    "figure_type": "source_exhibit",
    "context": "Évolution des exportations des produits semi-finis et produits sidérurgiques primaires du Bénin En Dollars"
  },
  {
    "figure_id": "F755",
    "report_id": "R030",
    "label": "Figure 17",
    "figure_type": "source_exhibit",
    "context": "37 https://fabrimetal-Bénin.com/le-marche-du-fer-a-beton-au-Bénin-tendances-et-opportunities/ $^{38}$ https://www.gouv.bj/article/2291/formations-professionnelles-duales-soutenues-projet-profop-centres-formation-recoivent-materiels-equipements Figure 17 Évolut"
  },
  {
    "figure_id": "F756",
    "report_id": "R030",
    "label": "Figure 19",
    "figure_type": "source_exhibit",
    "context": "Concernant les produits importés, on note plus de 230 produits importés du marché africain. En termes de valeur, on peut observer une domination d'une dizaine de produits. Le SH 721391 constitue le poste principal, avec 93,44 millions dollars (20,63 % du total"
  },
  {
    "figure_id": "F757",
    "report_id": "R030",
    "label": "Figure 18",
    "figure_type": "source_exhibit",
    "context": "Concernant les produits importés, on note plus de 230 produits importés du marché africain. En termes de valeur, on peut observer une domination d'une dizaine de produits. Le SH 721391 constitue le poste principal, avec 93,44 millions dollars (20,63 % du total"
  },
  {
    "figure_id": "F758",
    "report_id": "R030",
    "label": "Figure 18",
    "figure_type": "source_exhibit",
    "context": "## Figure 18 Évolution des exportations du Bénin de produits finis sidérurgiques En Dollars"
  },
  {
    "figure_id": "F759",
    "report_id": "R030",
    "label": "Figure 19",
    "figure_type": "source_exhibit",
    "context": "Liste des pays africains vers lesquels le Bénin exporte les produits finis"
  },
  {
    "figure_id": "F760",
    "report_id": "R030",
    "label": "Figure 19",
    "figure_type": "source_exhibit",
    "context": "## Figure 19 Évolution des importations du Bénin en produits finis sidérurgiques En Dollars"
  },
  {
    "figure_id": "F761",
    "report_id": "R030",
    "label": "Figure 19",
    "figure_type": "source_exhibit",
    "context": "## Figure 19 Évolution des importations du Bénin en produits finis sidérurgiques En Dollars"
  },
  {
    "figure_id": "F762",
    "report_id": "R030",
    "label": "Figure 20",
    "figure_type": "source_exhibit",
    "context": "Comparatif des prix/Kwh dans l'espace UEMOA"
  },
  {
    "figure_id": "F763",
    "report_id": "R030",
    "label": "Figure 21",
    "figure_type": "source_exhibit",
    "context": "\\- Au niveau du Coton et tissus : le manque d'électricité régulière affecte l'égrenage et la transformation locale, ce qui peut ralentir la chaîne logistique et limiter la valeur ajoutée nationale. Ainsi, la polarisation observée dans l'accès à l'électricité c"
  },
  {
    "figure_id": "F764",
    "report_id": "R030",
    "label": "Figure 21",
    "figure_type": "source_exhibit",
    "context": "## L'accès à l'eau ## Figure 21 Distribution du niveau d'accès à l'eau"
  },
  {
    "figure_id": "F765",
    "report_id": "R030",
    "label": "Figure 22",
    "figure_type": "source_exhibit",
    "context": "Dans le contexte sectoriel, cette situation freine considérablement les performances des chaînes de valeur. Pour l'ananas et le coton, la maîtrise de l'eau est essentielle pour garantir des rendements élevés et résister aux périodes de sécheresse. Le problème "
  },
  {
    "figure_id": "F766",
    "report_id": "R030",
    "label": "Figure 22",
    "figure_type": "source_exhibit",
    "context": "désormais en aire couverte par la 4G. Malgré ce résultat éloquent, l'utilisation de l'internet mobile reste faible au Bénin dû aux difficultés d'accès liées au coût de la connexion internet qui est classé parmi les plus chers de la sous-région. ## Figure 22 Di"
  },
  {
    "figure_id": "F767",
    "report_id": "R030",
    "label": "Figure 22",
    "figure_type": "source_exhibit",
    "context": "## Figure 22 Distribution du niveau d'accès à internet"
  },
  {
    "figure_id": "F768",
    "report_id": "R030",
    "label": "联合国贸发会议视觉摘要 1",
    "figure_type": "external_card",
    "context": "联合国贸发会议｜联合国贸发会议：贝宁经济韧性背后，中小企业出口附加值为何没跟上基础设施投资｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F769",
    "report_id": "R031",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "4. Conclusions and policy discussion......28"
  },
  {
    "figure_id": "F770",
    "report_id": "R031",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Well-being and development are inextricably linked to poverty eradication. Over the past three decades, significant progress has been made in reducing extreme poverty, which has fallen from around 40 per cent to less than 10 per cent globally. However, in the "
  },
  {
    "figure_id": "F771",
    "report_id": "R031",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## Figure 1. Evolution of extreme poverty A. Poverty headcount ratio at \\$2.15 a day (% of population) B. Number of poor people at \\$2.15 a day (mln) Quantitative studies on the link between poverty and disability based on representative samples or censuses ar"
  },
  {
    "figure_id": "F772",
    "report_id": "R031",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "The second objective is to shed further light on the disability-poverty relationship in Africa through econometric analysis permitting to control for confounding factors such as sociodemographic characteristics. Furthermore, in this paper, poverty is measured "
  },
  {
    "figure_id": "F773",
    "report_id": "R031",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "The multidimensional poverty measures capture the complexity of poverty by considering multiple dimensions of deprivation, such as education, health, and living conditions. This is crucial for studying disability, as individuals with disabilities may have inco"
  },
  {
    "figure_id": "F774",
    "report_id": "R031",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "# Disability prevalence ## 2.1 Concepts, data and definitions This paper follows the UNCRPD, which defines persons with disabilities as those who have “long-term physical, mental, intellectual or sensory impairments which in interaction with various barriers m"
  },
  {
    "figure_id": "F775",
    "report_id": "R031",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "This paper follows the UNCRPD, which defines persons with disabilities as those who have “long-term physical, mental, intellectual or sensory impairments which in interaction with various barriers may hinder their full and effective participation in society on"
  },
  {
    "figure_id": "F776",
    "report_id": "R031",
    "label": "联合国贸发会议视觉摘要 1",
    "figure_type": "external_card",
    "context": "联合国贸发会议｜联合国贸发会议：非洲残疾与贫困循环，数据揭示被低估的结构性挑战｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F777",
    "report_id": "R032",
    "label": "figure 1",
    "figure_type": "source_exhibit",
    "context": "# Preparing to seize artificial intelligence opportunities with strategic national policies Developing countries need to strengthen national readiness and design targeted policies in order to prepare for a world rapidly being reshaped by artificial intelligenc"
  },
  {
    "figure_id": "F778",
    "report_id": "R032",
    "label": "figure 1",
    "figure_type": "source_exhibit",
    "context": "## Preparing to seize artificial intelligence opportunities Developing countries need to prepare for a world rapidly transformed by artificial intelligence and other frontier technologies. UNCTAD has devised the frontier technologies readiness index, to offer "
  },
  {
    "figure_id": "F779",
    "report_id": "R032",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1 Brazil, China, India and the Philippines: Developing countries outperforming in technology readiness (Correlation between frontier technologies readiness index score and GDP per capita) Note: GDP per capita is in current international dollars, purchas"
  },
  {
    "figure_id": "F780",
    "report_id": "R032",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1 Brazil, China, India and the Philippines: Developing countries outperforming in technology readiness (Correlation between frontier technologies readiness index score and GDP per capita) Note: GDP per capita is in current international dollars, purchas"
  },
  {
    "figure_id": "F781",
    "report_id": "R032",
    "label": "figure 2",
    "figure_type": "source_exhibit",
    "context": "Key elements of artificial intelligence adoption and development Countries may be considered under four categories of artificial intelligence adoption and development capacity (figure 2). This serves to identify the current position of a country according to r"
  },
  {
    "figure_id": "F782",
    "report_id": "R032",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2 Four categories of artificial intelligence adoption and development capacity The comparative assessment of country preparedness relies on selected proxy indicators that have wide country coverage. The assessment may be further refined through detailed"
  },
  {
    "figure_id": "F783",
    "report_id": "R032",
    "label": "figure 4",
    "figure_type": "source_exhibit",
    "context": "## Designing national policies for artificial intelligence Over the last few decades, the increase in ICTs has been accompanied by decreasing costs, improved reliability and advancements in information management. Automation and capital-deepening are eroding t"
  },
  {
    "figure_id": "F784",
    "report_id": "R032",
    "label": "figure 4",
    "figure_type": "source_exhibit",
    "context": "Most artificial intelligence policies have originated in developed countries. By end-2023, about two thirds of developed countries had adopted a national artificial intelligence policy; of 89 national policies worldwide, only six were from the least developed "
  },
  {
    "figure_id": "F785",
    "report_id": "R032",
    "label": "联合国贸发会议视觉摘要 1",
    "figure_type": "external_card",
    "context": "联合国贸发会议｜联合国贸发会议：AI竞赛中，中国和印度不是追赶者，而是结构性例外者｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F786",
    "report_id": "R033",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "The review provides a set of conclusions and recommendations in order to guide the development of a future coherent, transparent, and development-friendly import tariff policy that supports the government's overarching objectives of promoting value addition, i"
  },
  {
    "figure_id": "F787",
    "report_id": "R033",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## A. Macroeconomic overview Papua New Guinea is a lower-middle-income economy with a Gross Domestic Product (GDP) of \\$32.8 billion and GDP per capita of \\$2.6 thousand in 2025 (IMF, 2025). This income level is modest by global standards and also below the Ea"
  },
  {
    "figure_id": "F788",
    "report_id": "R033",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "The Papua New Guinea economy has been on a positive growth trajectory since 2000 ## Figure 1. Papua New Guinea has experienced steady economic growth GDP in current prices (US\\$ billion) and growth (per cent) Extractive industries (minerals, petroleum) and agr"
  },
  {
    "figure_id": "F789",
    "report_id": "R033",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Extractive industries (minerals, petroleum) and agriculture form the backbone of Papua New Guinea's economy. According to data from the Papua New Guinea National Statistical Office (2025), Mining and Quarrying contributed to 27 per cent of the national gross o"
  },
  {
    "figure_id": "F790",
    "report_id": "R033",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Mining, after an initial decline from 2010 to 2012, saw a significant surge from 2014 to 2019, followed by a further surge in 2021–22, in line with the global commodity boom and Papua New Guinea's increased mineral exports. Manufacturing, on the other hand, di"
  },
  {
    "figure_id": "F791",
    "report_id": "R033",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## Figure 2. Note: Real effective exchange rate is the nominal effective exchange rate (a measure of the value of a currency against a weighted average of several foreign currencies) divided by a price deflator or index of costs. Based on the level of diversif"
  },
  {
    "figure_id": "F792",
    "report_id": "R033",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "## Figure 3. ## Papua New Guinea ranks low on economic complexity Comparison of Papua New Guinea's economic complexity index and GDP per capita (US\\$ PPP) with other economies, 2023 (ECI trade), patent data (ECI technology), and research publication data (ECI "
  },
  {
    "figure_id": "F793",
    "report_id": "R033",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "The concentration in low- to moderate-complexity commodities gives Papua New Guinea certain characteristics –namely, vulnerability to commodity price swings, but also strong export revenues when prices rise. However, this structure limits Papua New Guinea's ab"
  },
  {
    "figure_id": "F794",
    "report_id": "R033",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "In August 2017, the government formally suspended the TRP before the final 2018 cuts could be implemented. Instead of reducing the remaining tariffs to 10 per cent as planned, Papua New Guinea moved to raise many tariffs in order to shelter domestic producers."
  },
  {
    "figure_id": "F795",
    "report_id": "R033",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "## Figure 5. Tariff levels vary across products in Papua New Guinea Tariffs at the harmonized system 2 level, 2018 (per cent). This reversal of past policies marked a new protectionist chapter in Papua New Guinea's trade policy. After nearly two decades of fal"
  },
  {
    "figure_id": "F796",
    "report_id": "R033",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "## E. Multilateral and regional trade agreements breaches: WTO data indicate that on 23 tariff lines, Papua New Guinea's applied tariffs now exceed the bound levels committed at the WTO (see Figure 6) (WTO, 2019). At the regional level, Papua New Guinea is par"
  },
  {
    "figure_id": "F797",
    "report_id": "R033",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "## Figure 6. Average applied MFN tariff rates differ across products in Papua New Guinea Average applied MFN tariff rates by category, 2019 (per cent) Papua New Guinea's network of FTAs (PICTA), for example, Papua New Guinea has pledged to reduce or eliminate "
  },
  {
    "figure_id": "F798",
    "report_id": "R033",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "A tariff comparison between 2010 and 2023 indicates a shift in Papua New Guinea's trade protection policies over time. In 2010, after the first phase of the TRP, ad valorem equivalent (AVE) tariffs were relatively high and more dispersed across various product"
  },
  {
    "figure_id": "F799",
    "report_id": "R033",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "## Figure 7. MFN AVE tariffs have changed since 2010 MFN AVE tariffs in Papua New Guinea, 2010 and 2018 (percentage) ## Figure 8. MFN AVE tariffs in Papua New Guinea changed over the 2018–2023 period MFN AVE tariffs in Papua New Guinea, 2018 and 2023 (percenta"
  },
  {
    "figure_id": "F800",
    "report_id": "R033",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "## Figure 7. MFN AVE tariffs have changed since 2010 MFN AVE tariffs in Papua New Guinea, 2010 and 2018 (percentage) ## Figure 8. MFN AVE tariffs in Papua New Guinea changed over the 2018–2023 period MFN AVE tariffs in Papua New Guinea, 2018 and 2023 (percenta"
  },
  {
    "figure_id": "F801",
    "report_id": "R033",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "## Figure 8. MFN AVE tariffs in Papua New Guinea changed over the 2018–2023 period MFN AVE tariffs in Papua New Guinea, 2018 and 2023 (percentage) ## Figure 9. Simple average AVE tariffs of Papua New Guinea Simple average AVE tariffs by product category, 2010–"
  },
  {
    "figure_id": "F802",
    "report_id": "R033",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "## Figure 8. MFN AVE tariffs in Papua New Guinea changed over the 2018–2023 period MFN AVE tariffs in Papua New Guinea, 2018 and 2023 (percentage) ## Figure 9. Simple average AVE tariffs of Papua New Guinea Simple average AVE tariffs by product category, 2010–"
  },
  {
    "figure_id": "F803",
    "report_id": "R033",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "## Figure 9. Simple average AVE tariffs of Papua New Guinea Simple average AVE tariffs by product category, 2010–2023 (percentage) The distribution of tariff levels across categories of products affects raw materials, consumer products and intermediary product"
  },
  {
    "figure_id": "F804",
    "report_id": "R033",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "policy unpredictability in long-term financial commitments. Meanwhile, a quarter of firms stated that tariff revisions did not impact their investment choices. This suggests that either their operations were less exposed to tariff-sensitive sectors or they had"
  },
  {
    "figure_id": "F805",
    "report_id": "R033",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "## Figure 10. ## Impact of tariff policy on investment decisions Has the ad-hoc nature of tariff revisions (2018–2020) affected your investment decisions? ## Figure 11. Tariff levels by product category changed during and after the TRP Minimum tariff applied b"
  },
  {
    "figure_id": "F806",
    "report_id": "R033",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "## Impact of tariff policy on investment decisions Has the ad-hoc nature of tariff revisions (2018–2020) affected your investment decisions? ## Figure 11. Tariff levels by product category changed during and after the TRP Minimum tariff applied by product cate"
  },
  {
    "figure_id": "F807",
    "report_id": "R033",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "## Figure 11. Tariff levels by product category changed during and after the TRP Minimum tariff applied by product category, 2010, 2017, 2018 and 2023 (percentage) Figure 12. Tariff dispersions across HS 2 sectors Tariff applied, 2010, 2018 and 2023 (percentag"
  },
  {
    "figure_id": "F808",
    "report_id": "R033",
    "label": "Figure 12",
    "figure_type": "source_exhibit",
    "context": "Minimum tariff applied by product category, 2010, 2017, 2018 and 2023 (percentage) Figure 12. Tariff dispersions across HS 2 sectors Tariff applied, 2010, 2018 and 2023 (percentage) Note: Each square represents an HS6 product within its corresponding HS2 secto"
  },
  {
    "figure_id": "F809",
    "report_id": "R033",
    "label": "Figure 13",
    "figure_type": "source_exhibit",
    "context": "## B. Economic outcomes and sector performance ## Overall observations Trade trends in Papua New Guinea suggest a robust growth in exports and a decline in imports between 2010 to 2024. Imports declined significantly, from a high of \\$8 billion in 2012, despit"
  },
  {
    "figure_id": "F810",
    "report_id": "R033",
    "label": "Figure 13",
    "figure_type": "source_exhibit",
    "context": "afterwards as exports surged (Figure 13). The factors behind the improved performance in the trade balance reflect less the tariff policy and more other external factors, including the thriving mining sector. Following the suspension of TRP in 2018, import lev"
  },
  {
    "figure_id": "F811",
    "report_id": "R033",
    "label": "Figure 14",
    "figure_type": "source_exhibit",
    "context": "## A number of factors explain why Papua New Guinea's imports fell during 2012–2017 despite tariff cuts. One likely factor was broader economic conditions: Papua New Guinea was completing a large LNG investment project around 2014 and then faced a downturn in "
  },
  {
    "figure_id": "F812",
    "report_id": "R033",
    "label": "Figure 14",
    "figure_type": "source_exhibit",
    "context": "GDP (US\\$ Billions) GDP Growth (yoy) ## Figure 14. Growth has slowed after the TRP suspension GDP in Papua New Guinea, 2010–2024 (US\\$ billion) Current Account Balance to GDP (%) Purchasing power showed a similar growth pattern over the same period. GDP per ca"
  },
  {
    "figure_id": "F813",
    "report_id": "R033",
    "label": "Figure 14",
    "figure_type": "source_exhibit",
    "context": "## Figure 14. Growth has slowed after the TRP suspension GDP in Papua New Guinea, 2010–2024 (US\\$ billion) Current Account Balance to GDP (%) Purchasing power showed a similar growth pattern over the same period. GDP per capita at Purchasing Power Parity (PPP)"
  },
  {
    "figure_id": "F814",
    "report_id": "R033",
    "label": "Figure 15",
    "figure_type": "source_exhibit",
    "context": "Current Account Balance to GDP (%) Purchasing power showed a similar growth pattern over the same period. GDP per capita at Purchasing Power Parity (PPP) increased by 4.4 per cent annually between 2010 and 2017 and moderated to 3.8 per cent between 2018 and 20"
  },
  {
    "figure_id": "F815",
    "report_id": "R033",
    "label": "Figure 15",
    "figure_type": "source_exhibit",
    "context": "Purchasing power showed a similar growth pattern over the same period. GDP per capita at Purchasing Power Parity (PPP) increased by 4.4 per cent annually between 2010 and 2017 and moderated to 3.8 per cent between 2018 and 2024 (Figure 15). This sustained impr"
  },
  {
    "figure_id": "F816",
    "report_id": "R033",
    "label": "Figure 16",
    "figure_type": "source_exhibit",
    "context": "Import composition showed a strong shift towards consumer goods during the liberalization period. From 2012 to 2017, the share of consumer goods in total imports increased from 28 per cent to 41 per cent during the TRP, eventually reaching 46 per cent by 2023 "
  },
  {
    "figure_id": "F817",
    "report_id": "R033",
    "label": "Figure 17",
    "figure_type": "source_exhibit",
    "context": "Consumer goods as a share of imports have grown steadily Structure of Papua New Guinea's imports during and after TRP phase 2, by type of goods (share, percentage) ## Figure 17. Intermediate, consumer and capital goods returned to modest positive growth Import"
  },
  {
    "figure_id": "F818",
    "report_id": "R033",
    "label": "Figure 17",
    "figure_type": "source_exhibit",
    "context": "## Figure 17. Intermediate, consumer and capital goods returned to modest positive growth Import value during and after TRP phase 2, by product category, 2010–2023 (US\\$ billion) ## Impact by sector Examination of agriculture, mining, and manufacturing perform"
  },
  {
    "figure_id": "F819",
    "report_id": "R033",
    "label": "Figure 18",
    "figure_type": "source_exhibit",
    "context": "## Impact by sector Examination of agriculture, mining, and manufacturing performance, using the gross value added (GVA) index over the past two decades, reveals that the tariff policy alone did not generate much change to the performance of major sectors of t"
  },
  {
    "figure_id": "F820",
    "report_id": "R033",
    "label": "Figure 18",
    "figure_type": "source_exhibit",
    "context": "## Figure 18. Manufacturing has stagnated - AGRICULTURE, FORESTRY AND FISHING - MINING AND QUARRYING - MANUFACTURING The above evidence suggests that tariff liberalization did not affect agriculture, as the sector continued to grow – possibly benefiting from c"
  },
  {
    "figure_id": "F821",
    "report_id": "R033",
    "label": "Figure 27",
    "figure_type": "source_exhibit",
    "context": "The above evidence suggests that tariff liberalization did not affect agriculture, as the sector continued to grow – possibly benefiting from cheaper imported farm inputs like machinery or fertilizer, and facing little direct competition since Papua New Guinea"
  },
  {
    "figure_id": "F822",
    "report_id": "R033",
    "label": "Figure 19",
    "figure_type": "source_exhibit",
    "context": "## C. Tariff revenue A critical aspect of tariff policy is its impact on government revenue. The tax-to-GDP ratio in Papua New Guinea has fallen between 2010 and 2023, reaching 15.8 per cent in 2023 (Figure 19). During the same period, tax revenue has increase"
  },
  {
    "figure_id": "F823",
    "report_id": "R033",
    "label": "Figure 19",
    "figure_type": "source_exhibit",
    "context": "## Figure 19. Tax-to-GDP ratio has fallen in Papua New Guinea ## Figure 20. Total tax revenue has increased in Papua New Guinea"
  },
  {
    "figure_id": "F824",
    "report_id": "R033",
    "label": "Figure 19",
    "figure_type": "source_exhibit",
    "context": "## Figure 19. Tax-to-GDP ratio has fallen in Papua New Guinea ## Figure 20. Total tax revenue has increased in Papua New Guinea"
  },
  {
    "figure_id": "F825",
    "report_id": "R033",
    "label": "Figure 20",
    "figure_type": "source_exhibit",
    "context": "## Figure 20. Total tax revenue has increased in Papua New Guinea The analysis of tariff revenue by product category revealed that consumer goods produced the bulk of Papua New Guinea's tariff revenue. The fact that consumer products generate most revenue (Fig"
  },
  {
    "figure_id": "F826",
    "report_id": "R033",
    "label": "Figure 20",
    "figure_type": "source_exhibit",
    "context": "## Figure 20. Total tax revenue has increased in Papua New Guinea The analysis of tariff revenue by product category revealed that consumer goods produced the bulk of Papua New Guinea's tariff revenue. The fact that consumer products generate most revenue (Fig"
  },
  {
    "figure_id": "F827",
    "report_id": "R033",
    "label": "Figure 22",
    "figure_type": "source_exhibit",
    "context": "Lowering tariff rates may reduce tariff revenue collection or increase it, depending on the elasticities of demand. Despite the evidence, holding all factors constant, it is interesting to simulate the expected changes in revenue from tariff changes. During th"
  },
  {
    "figure_id": "F828",
    "report_id": "R033",
    "label": "Figure 21",
    "figure_type": "source_exhibit",
    "context": "Figure 21. ## Figure 22. Results from tariff revenue simulations Change in tariff revenue during and after the TRP (Millions of dollars), overall and by sector"
  },
  {
    "figure_id": "F829",
    "report_id": "R033",
    "label": "Figure 21",
    "figure_type": "source_exhibit",
    "context": "Figure 21. ## Figure 22. Results from tariff revenue simulations Change in tariff revenue during and after the TRP (Millions of dollars), overall and by sector"
  },
  {
    "figure_id": "F830",
    "report_id": "R033",
    "label": "Figure 22",
    "figure_type": "source_exhibit",
    "context": "## Figure 22. Results from tariff revenue simulations Change in tariff revenue during and after the TRP (Millions of dollars), overall and by sector Tariff revenue effects by sectors After 2018, with the TRP suspension, the expectation was that fiscal revenue "
  },
  {
    "figure_id": "F831",
    "report_id": "R033",
    "label": "Figure 23",
    "figure_type": "source_exhibit",
    "context": "border trade (e.g. along the Indonesian border or via sea routes) could become a channel for tariff evasion when rates rise too steeply (Conroy, 2021). This suggests Papua New Guinea's optimal tariff (for revenue purposes) on many goods might be at a relativel"
  },
  {
    "figure_id": "F832",
    "report_id": "R033",
    "label": "Figure 23",
    "figure_type": "source_exhibit",
    "context": "## Figure 23. Did your business benefit from tariff reductions in the 2012–2017 period? Specific competition impacts from imported products ## Figure 24. Perceived impacts of the tariff increases post-2018 Has your firm been affected by tariff increases post-2"
  },
  {
    "figure_id": "F833",
    "report_id": "R033",
    "label": "Figure 24",
    "figure_type": "source_exhibit",
    "context": "Did your business benefit from tariff reductions in the 2012–2017 period? Specific competition impacts from imported products ## Figure 24. Perceived impacts of the tariff increases post-2018 Has your firm been affected by tariff increases post-2018?"
  },
  {
    "figure_id": "F834",
    "report_id": "R033",
    "label": "Figure 24",
    "figure_type": "source_exhibit",
    "context": "Specific competition impacts from imported products ## Figure 24. Perceived impacts of the tariff increases post-2018 Has your firm been affected by tariff increases post-2018? ## Figure 25. ## Perceived level of competition linked to the TRP"
  },
  {
    "figure_id": "F835",
    "report_id": "R033",
    "label": "Figure 24",
    "figure_type": "source_exhibit",
    "context": "## Figure 24. Perceived impacts of the tariff increases post-2018 Has your firm been affected by tariff increases post-2018? ## Figure 25. ## Perceived level of competition linked to the TRP Has your company experienced increased competition from imported prod"
  },
  {
    "figure_id": "F836",
    "report_id": "R033",
    "label": "Figure 25",
    "figure_type": "source_exhibit",
    "context": "## Figure 25. ## Perceived level of competition linked to the TRP Has your company experienced increased competition from imported products? Did tariff reductions lead to perceived unfair competition from imports? Perceived competition was increasing, in line "
  },
  {
    "figure_id": "F837",
    "report_id": "R033",
    "label": "Figure 25",
    "figure_type": "source_exhibit",
    "context": "electricity, inputs) were too high. since TRP implementation, with this competition affecting sales volumes, pricing strategies, and fundamental business models. Interestingly, 40 per cent of firms characterized this import competition as “unfair” (Figure 25)."
  },
  {
    "figure_id": "F838",
    "report_id": "R033",
    "label": "Figure 27",
    "figure_type": "source_exhibit",
    "context": "Several structural challenges were shown as major hurdles for domestic production capacity and competitiveness. According to the survey results, transport and logistics costs emerged as overwhelming challenges for business operations, with 94 per cent of surve"
  },
  {
    "figure_id": "F839",
    "report_id": "R033",
    "label": "Figure 27",
    "figure_type": "source_exhibit",
    "context": "unpredictability and regulatory burdens as major concerns, respectively (Figure 27). These results suggest that Papua New Guinea's competitiveness challenges stem from fundamental structural issues beyond trade policy choices, and that ## Figure 27. Main const"
  },
  {
    "figure_id": "F840",
    "report_id": "R033",
    "label": "Figure 28",
    "figure_type": "source_exhibit",
    "context": "## E. Innovation with only 465 products (35 per cent of the total) surviving the full TRP period. The figure indicates that cost advantages from input tariff reductions, while helpful for market entry, proved insufficient for sustained international competitiv"
  },
  {
    "figure_id": "F841",
    "report_id": "R033",
    "label": "Figure 28",
    "figure_type": "source_exhibit",
    "context": "One key observation during the TRP was its association with export diversification and an entrepreneurial response by Papua New Guinea's private sector, followed by a setback once tariffs were raised. ## Figure 28. Innovation and decay in the export portfolio "
  },
  {
    "figure_id": "F842",
    "report_id": "R033",
    "label": "Figure 28",
    "figure_type": "source_exhibit",
    "context": "## Figure 28. Innovation and decay in the export portfolio Birth and death of products during TRP Birth and death of products post TRP Birth and death of products during TRP Birth and death of products post TRP"
  },
  {
    "figure_id": "F843",
    "report_id": "R033",
    "label": "Figure 29",
    "figure_type": "source_exhibit",
    "context": "meet international standards. Additionally, the TRP signalled a commitment to open trade, possibly encouraging investment (domestic or foreign) in new ventures oriented towards export markets, knowing that inputs could be sourced at world prices. After 2018, t"
  },
  {
    "figure_id": "F844",
    "report_id": "R033",
    "label": "Figure 29",
    "figure_type": "source_exhibit",
    "context": "## Figure 29. Reported innovation attempts: introducing new products Has your company introduced new products or exports in the last 5 years? ## F. Consumer welfare Trade policy has direct consequences for consumer welfare through its impact on prices and prod"
  },
  {
    "figure_id": "F845",
    "report_id": "R033",
    "label": "Figure 30",
    "figure_type": "source_exhibit",
    "context": "Trade policy has direct consequences for consumer welfare through its impact on prices and product availability. The welfare effects of the TRP can be assessed using consumer surplus, a measure of the benefit consumers obtain from being able to purchase goods "
  },
  {
    "figure_id": "F846",
    "report_id": "R033",
    "label": "Figure 30",
    "figure_type": "source_exhibit",
    "context": "## Figure 30. ## Welfare implications of the TRP Change in welfare during and after the TRP overall and by sector, (millions of dollars) A critical observation is that conventional consumer welfare calculations from tariff reduction often assume that greater c"
  },
  {
    "figure_id": "F847",
    "report_id": "R033",
    "label": "Figure 31",
    "figure_type": "source_exhibit",
    "context": "A critical observation is that conventional consumer welfare calculations from tariff reduction often assume that greater consumption, driven by lower prices, translates into higher welfare. However, this overlooks the negative externalities of harmful goods. "
  },
  {
    "figure_id": "F848",
    "report_id": "R033",
    "label": "Figure 31",
    "figure_type": "source_exhibit",
    "context": "## Figure 31. Perceived price sensitivity of Papua New Guinea consumers Do Papua New Guinea consumers appear willing to pay more for local products if protected from cheap imports? Consumer welfare in Papua New Guinea suffered during the tariff reductions phas"
  },
  {
    "figure_id": "F849",
    "report_id": "R033",
    "label": "Figure 32",
    "figure_type": "source_exhibit",
    "context": "## 2. Focus on fostering a competitive business environment The government should pivot from protecting industries as a framework to enable them to compete. While adding additional layers of costs will undoubtedly provide some shielding from competition, this "
  },
  {
    "figure_id": "F850",
    "report_id": "R033",
    "label": "Figure 32",
    "figure_type": "source_exhibit",
    "context": "## Figure 32. Recommended areas of support for competitiveness What are your top 3 policy recommendations to strengthen your industry's competitiveness? \\- Industry development programs: Build foundation for competitiveness, such as infrastructure (roads, port"
  },
  {
    "figure_id": "F851",
    "report_id": "R033",
    "label": "Figure 33",
    "figure_type": "source_exhibit",
    "context": "## Annex 2. Methodology ## Background There are several channels through which tariff changes may alter consumers' consumption (and by default welfare), government spending and revenue, and enterprises' production and investment decisions. Most directly, tarif"
  },
  {
    "figure_id": "F852",
    "report_id": "R033",
    "label": "Figure 33",
    "figure_type": "source_exhibit",
    "context": "There are several channels through which tariff changes may alter consumers' consumption (and by default welfare), government spending and revenue, and enterprises' production and investment decisions. Most directly, tariff change can lead to increased costs f"
  },
  {
    "figure_id": "F853",
    "report_id": "R033",
    "label": "Figure 34",
    "figure_type": "source_exhibit",
    "context": "In reality, the effects are more complicated owing to the nonlinear nature of effects, the lags in response (also affected by accumulated inventories) and a series of unknowns such as the propensity for consumers to pay a higher price (modelled through price e"
  },
  {
    "figure_id": "F854",
    "report_id": "R033",
    "label": "Figure 34",
    "figure_type": "source_exhibit",
    "context": "The simple method for calculating the impact of tariffs on consumers, government revenue and businesses is to adopt a partial equilibrium model. In such a model, the increase in a tariff adds a premium on price over the world price of a commodity. This leads t"
  },
  {
    "figure_id": "F855",
    "report_id": "R033",
    "label": "Figure 34",
    "figure_type": "source_exhibit",
    "context": "This leads to a reduction in demand from consumers, which is illustrated in Figure 34, as increase price increases from \\$400 to \\$800 (a 100 per cent tariff is applied). Producers will be willing to supply more products at that price and will make up for some"
  },
  {
    "figure_id": "F856",
    "report_id": "R033",
    "label": "Figure 35",
    "figure_type": "source_exhibit",
    "context": "## Data choices Figure 35. PNGCS and UNDS data for Papua New Guinea imports Yearly imports in US\\$ millions, 2010–2023. PNGCS and UNDS import data for Papua New Guinea"
  },
  {
    "figure_id": "F857",
    "report_id": "R033",
    "label": "Figure 35",
    "figure_type": "source_exhibit",
    "context": "Figure 35. PNGCS and UNDS data for Papua New Guinea imports Yearly imports in US\\$ millions, 2010–2023. PNGCS and UNDS import data for Papua New Guinea"
  },
  {
    "figure_id": "F858",
    "report_id": "R033",
    "label": "联合国贸发会议视觉摘要 1",
    "figure_type": "external_card",
    "context": "联合国贸发会议｜联合国贸发会议：不是关税，基础设施和政策不确定性才是巴新企业真正瓶颈｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F859",
    "report_id": "R034",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Number and share of countries where trade or tariff reduce poverty (Negative correlation)"
  },
  {
    "figure_id": "F860",
    "report_id": "R034",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## Figure 1 ## Correlation of poverty with trade indicators, by country group"
  },
  {
    "figure_id": "F861",
    "report_id": "R034",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## Figure 1 ## Correlation of poverty with trade indicators, by country group"
  },
  {
    "figure_id": "F862",
    "report_id": "R034",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## Figure 1 ## Correlation of poverty with trade indicators, by country group"
  },
  {
    "figure_id": "F863",
    "report_id": "R034",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## Figure 1 ## Correlation of poverty with trade indicators, by country group # Empirical approach and data"
  },
  {
    "figure_id": "F864",
    "report_id": "R034",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## ...... In traditional trade models, such as the Heckscher-Ohlin model and the associated Stolper-Samuelson theorem, with full factor mobility trade liberalization can affect poverty in a labour-abundant developing country through two main channels: a redist"
  },
  {
    "figure_id": "F865",
    "report_id": "R034",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Theoretically, the impact of trade on poverty may depend on domestic policies and conditions (or country characteristics). To identify the role that country characteristics play in the effect of trade on poverty, we continue with our data-driven approach to se"
  },
  {
    "figure_id": "F866",
    "report_id": "R034",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2 Effect on poverty of each variable interacted with trade openness (Developing countries) Figure 3 presents the results for the African sample, depicting the coefficients of the PDS lasso estimations of the effect of trade and the control variables int"
  },
  {
    "figure_id": "F867",
    "report_id": "R034",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3 presents the results for the African sample, depicting the coefficients of the PDS lasso estimations of the effect of trade and the control variables interacted with trade, on poverty. As expected, considering interactions of trade with country charac"
  },
  {
    "figure_id": "F868",
    "report_id": "R034",
    "label": "联合国贸发会议视觉摘要 1",
    "figure_type": "external_card",
    "context": "联合国贸发会议｜联合国贸发会议：从非洲悖论看全球供应链，贸易红利如何才能真正落地？｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F869",
    "report_id": "R035",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1 Key channels through which AI influences R&D .... 3 Figure 2 AI applications in bioscience, materials science and climate science.... 6 Figure 3 Key challenges of using AI in R&D.... 9 Figure 4 The shift from traditional to transformative innovation p"
  },
  {
    "figure_id": "F870",
    "report_id": "R035",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "R&D is a multifaceted process that typically comprises four interconnected and iterative stages: (i) conceptualization, (ii) research, (iii) development and (iv) deployment. The conceptualization stage involves generating ideas, identifying problems or recogni"
  },
  {
    "figure_id": "F871",
    "report_id": "R035",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "AI is set to transform R&D by advancing progress across all four stages through several key channels: (i) data collection and curation, (ii) data analysis, (iii) hypotheses generation and (iv) experimentation and simulation (Figure 1) (Krenn et al., 2022; Euro"
  },
  {
    "figure_id": "F872",
    "report_id": "R035",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Another study identified two key factors influencing AI adoption: researcher age and prior familiarity with AI models. Younger researchers are more likely to adopt AI models, while those with prior knowledge are 17 times more likely to integrate AI into their "
  },
  {
    "figure_id": "F873",
    "report_id": "R035",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## B. Examples of AI applications in R&D With the key mechanisms through which AI influences R&D explained, it is useful to examine concrete examples of its application. Three distinct branches of science: (i) bioscience, (ii) materials science and (iii) clima"
  },
  {
    "figure_id": "F874",
    "report_id": "R035",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## Figure 2 AI applications in bioscience, materials science and climate science Bioscience ## Materials science Climate science \\- Predict protein folding"
  },
  {
    "figure_id": "F875",
    "report_id": "R035",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "AI models are growing rapidly in scale and are being trained on increasingly massive data sets, raising concerns that high-quality, human-generated public data may be exhausted within a few years (Villalobos et al., 2024). In cutting-edge research areas, the l"
  },
  {
    "figure_id": "F876",
    "report_id": "R035",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "## Figure 3 ## Key challenges of using AI in R&D ## Technical challenges Data availability and quality Explainability"
  },
  {
    "figure_id": "F877",
    "report_id": "R035",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "is also key in this regard to ensure that innovation policies effectively achieve their intended goals while remaining responsive to changing contexts. As the view of innovation shifted, policy priorities broadened beyond funding basic research to include: (i)"
  },
  {
    "figure_id": "F878",
    "report_id": "R035",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4 The shift from traditional to transformative innovation policy ## Traditional innovation policy Linear, science-push approach ## Transformative innovation policy Top-down, rigid regulatory frameworks Disconnected disciplines Narrow focus on promoting "
  },
  {
    "figure_id": "F879",
    "report_id": "R035",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Empirical evidence shows that countries are substantially adapting their innovation policy to incorporate transformative measures. For example, a study of 24 OECD countries revealed a clear shift among policymakers from traditional innovation policy objectives"
  },
  {
    "figure_id": "F880",
    "report_id": "R035",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Transitions in the framing and goals of innovation policy have coincided with rapid digitalization. Since the onset of the Fourth Industrial Revolution, marked by the integration of cyber-physical systems, advanced data processing and enhanced connectivity, th"
  },
  {
    "figure_id": "F881",
    "report_id": "R035",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "To foster innovation while prioritizing responsible AI and data governance, governments can consider: \\- Promoting ethics, accountability and cultural alignment in AI: Governments can develop tools and metrics to identify, measure and address AI-related risks,"
  },
  {
    "figure_id": "F882",
    "report_id": "R035",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "through global cooperation based on openness, capacity- building and ethical principles ## Figure 6 Key areas of collaboration for inclusive AI ## Promoting open science and open innovation"
  },
  {
    "figure_id": "F883",
    "report_id": "R035",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "capacity- building and ethical principles ## Figure 6 Key areas of collaboration for inclusive AI ## Promoting open science and open innovation \\- Foster knowledge exchange and interdisciplinary research through open science • Accelerate partnerships for real-"
  },
  {
    "figure_id": "F884",
    "report_id": "R035",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "ethical principles ## Figure 6 Key areas of collaboration for inclusive AI ## Promoting open science and open innovation \\- Foster knowledge exchange and interdisciplinary research through open science • Accelerate partnerships for real-world solutions via ope"
  },
  {
    "figure_id": "F885",
    "report_id": "R035",
    "label": "联合国贸发会议视觉摘要 1",
    "figure_type": "external_card",
    "context": "联合国贸发会议｜联合国贸发会议：发展中国家面临AI研发重构，不是追赶权而是参与权问题｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F886",
    "report_id": "R036",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Contrary to these findings, Canh et al. (2020) report a linear negative association between economic complexity and natural resource rents. When disaggregating by income group, the authors find that the relationship holds true in two out of three subsamples, c"
  },
  {
    "figure_id": "F887",
    "report_id": "R036",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "The empirical investigation of this relationship is analytically valuable despite the definitional observation that commodities are inherently less sophisticated products. While product complexity indices assign lower scores to primary commodities than to manu"
  },
  {
    "figure_id": "F888",
    "report_id": "R036",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1 # Estimation approach To empirically explore the relationship between economic complexity and commodity dependence, we first need a theoretical model to guide the analysis and interpretation of results. The objective is to integrate these concepts and"
  },
  {
    "figure_id": "F889",
    "report_id": "R036",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Note: This scatter plot illustrates the average values of economic complexity and commodity dependence for each economy over the 25-year period between 1995 and 2020. This plot excludes commodity-dependent developed countries Australia, Iceland, New Zealand an"
  },
  {
    "figure_id": "F890",
    "report_id": "R036",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Note: This scatter plot illustrates the average values of economic complexity and commodity dependence for each economy over the 25-year period between 1995 and 2020. This plot excludes commodity-dependent developed countries Australia, Iceland, New Zealand an"
  },
  {
    "figure_id": "F891",
    "report_id": "R036",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Note: The graphs illustrate the average values of economic complexity and commodity dependence by commodity dependence ranges over the 25-year period between 1995 and 2020. This plot excludes commodity-dependent developed countries Australia, Iceland, New Zeal"
  },
  {
    "figure_id": "F892",
    "report_id": "R036",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "When disaggregating countries by levels of commodity dependence, a more distinct pattern emerges (Figure 3). While non-commodity-dependent countries maintain an average index of 0.58, this decreases to -0.26 for countries with commodity export ratios between 6"
  },
  {
    "figure_id": "F893",
    "report_id": "R036",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "## Figure 3 Note: The graphs illustrate the average values of economic complexity and commodity dependence by commodity dependence ranges over the 25-year period between 1995 and 2020. This plot excludes commodity-dependent developed countries Australia, Icela"
  },
  {
    "figure_id": "F894",
    "report_id": "R036",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Note: The graphs illustrate the average values of economic complexity and commodity dependence by commodity dependence ranges over the 25-year period between 1995 and 2020. This plot excludes commodity-dependent developed countries Australia, Iceland, New Zeal"
  },
  {
    "figure_id": "F895",
    "report_id": "R036",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4 offers insights into the average complexity and its association with commodity dependence for CDDCs, categorised by the sectors on which they rely on. Albeit small, there are some differences in the average complexity across groups. All groups exhibit"
  },
  {
    "figure_id": "F896",
    "report_id": "R036",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "## Figure 4 Economic complexity index Note: The graphs illustrate the average values of economic complexity and commodity dependence by commodity dependence group over the 25-year period between 1995 and 2020. This plot excludes commodity-dependent developed c"
  },
  {
    "figure_id": "F897",
    "report_id": "R036",
    "label": "联合国贸发会议视觉摘要 1",
    "figure_type": "external_card",
    "context": "联合国贸发会议｜联合国贸发会议：联合国报告，全球经济增长反而加深资源依赖国困境｜用于快速识别该外部报告的核心问题和市场含义。"
  }
]