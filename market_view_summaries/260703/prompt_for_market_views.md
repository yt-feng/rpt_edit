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
  "战略咨询": 6,
  "智库/国际机构": 6
}

报告摘要：
[
  {
    "id": "R001",
    "title": "IMF报告：柬埔寨预算执行改革走到了哪一步，又卡在了哪里",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "IMF",
    "digest": "[wechat_article.md]\n# IMF报告：柬埔寨预算执行改革走到了哪一步，又卡在了哪里\n\n一份来自国际货币基金组织（IMF）技术援助团队的报告，在2025年10月对柬埔寨预算执行体系进行了为期两周的全面战略评估。结论是：柬埔寨在过去二十年取得了显著进展，但真正决定改革成败的，不是顶层设计，而是FMIS系统的最后一公里、现金垫款的灰色地带，以及国库单一账户的实质性落地。\n\n这份报告的价值不在于它告诉外界柬埔寨做得有多好，而在于它精准地指出了“从好到卓越”之间的结构性障碍。对于关注新兴市场财政改革、数字化转型或主权信用风险的读者来说，这是一份难得的“手术刀式”诊断。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 法律框架和数字化已经走在前列，但执行层存在系统性的“断点”\n\nIMF报告首先肯定了柬埔寨公共财政管理改革计划的成果。自2004年以来，柬埔寨政府持续推进改革，2023年通过的《公共财政体系法》及配套子法令，为预算执行提供了相对完善的法律基础。财政管理信息系统（FMIS）也已在大多数预算单位推广使用。\n\n但真正的挑战不在法律文本，而在执行链条的末梢。报告明确指出，尽管FMIS成为核心数字化工具，但仍有部分预算单位尚未被授权为“完全授权预算实体”。这意味着它们无法直接访问FMIS，也无法使用电子资金转账（EFT）完成支付。这种“授权不完整”的状态，直接导致预算执行效率参差不齐，部分单位仍依赖纸质流程，增加了时间成本和人为干预空间。\n\n> **KC评论：** 这其实是很多发展中国家数字化转型的典型困境——中央系统建好了，但基层单位要么没有权限，要么没有能力用。IMF建议在2027年前将所有未授权实体转化为完全授权实体，这个时间表本身就是一个关键观察点。完整报告里有详细的阶段性目标分解，值得细看。\n\n## 2. FMIS的“最后一公里”才是真正的瓶颈\n\n[... middle omitted ...]\n\n既方便喂给AI做进一步分析，也适合人工快速把握全球市场动态。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n柬埔寨预算执行改革，IMF给了一份路线图\n\n预算执行效率提升指南\n\nIMF技术援助报告核心发现\n\n📌 柬埔寨的预算执行改革已经走了20年，2023年新《公共财政法》+数字化推进，成果不小。但IMF最近的技术援助报告指出，还有几个关键短板需要补上。\n\n1️⃣ FMIS系统要升级\n核心数字工具FMIS已覆盖大部分单位，但e采购、e发票模块还没上线。到2027年把所有未授权预算单位转为全授权单位，能直接提升执行效率。同时打通银行和收入系统，让现金余额可视化、自动对账、承诺记录更顺畅。\n\n2️⃣ 现金垫款和欠款要严控\n欠款定义需要和国际接轨。可以考虑在财年开始前就完成内部承诺准备，分层次设置审批门槛，避免流程拖沓导致欠款堆积。\n\n3️⃣ 国库单一账户（TSA）要全面落地\n收入端整合已不错，但支出端账户的监管和对账仍需加强。法律框架要跟上，明确报告义务和违规问责，逐步扩大TSA覆盖范围。\n\n4️⃣ 现金管理要更主动\nFMIS对接债务系统，强化现金管理委员会职能，让闲置资金能安全做短期投资，优化资金使用效率。\n\n📌 报告还给了2026-28年优先行动计划和可量化指标，改革节奏很清晰。\n\n#学习笔记\n\n[source_mi\n\n[... middle omitted ...]\n\nsistance provided to IMF capacity development recipients, describing the high-level objectives, findings, and recommendations.\n\nABSTRACT: The technical assistance identifies strengths in budge\n\n[... middle omitted ...]\n\nsting quality and governance.\n\n\\- Active Cash Management. Linking FMIS with debt systems and strengthening the Cash Management Committee can improve planning and enable safe short-term investments to optimize idle funds."
  },
  {
    "id": "R002",
    "title": "IMF：Tokenization不会消灭金融基础设施，但会重新定义谁做什么",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "IMF",
    "digest": "[wechat_article.md]\n# IMF：Tokenization不会消灭金融基础设施，但会重新定义谁做什么\n\n金融市场的代币化浪潮正在从概念验证走向实际部署。从债券发行到衍生品清算，从资产托管到交易报告，几乎每一个环节都出现了“上链”的尝试。但一个根本问题始终悬而未决：如果资产在链上发行和交易，那么中央证券存管机构、中央对手方、交易报告库这些传统金融基础设施，还有存在的必要吗？\n\nIMF在2026年7月发布的工作论文给出了一个清晰而审慎的回答：代币化不会消灭金融基础设施，但会从根本上重新分配它们的功能。那些确定性、规则驱动、数据密集的流程——如记录保存、结算、抵押品转移和报告——可以迁移到智能合约上执行。但需要法律确定性、问责制、自由裁量权和压力下判断力的功能，仍然必须由机构来承担。\n\n这份报告的核心判断是：最可能的终局不是去中介化，而是混合模式。代码和机构将共同提供金融稳定所需的信任、韧性和监督。这不是一个技术替代制度的故事，而是一个技术和制度重新分工的故事。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 智能合约能做什么，不能做什么，边界比想象中更清晰\n\n报告对FMI功能的评估遵循一个简单但有力的框架：一项功能能否迁移到链上，取决于它是否满足三个条件——确定性、可自动化、不需要主观判断。\n\n按照这个标准，报告给出了明确的划分：\n\n**可以迁移到链上的功能**包括：资产发行和记录、所有权转移、结算中的交付对付款执行、抵押品估值和自动追缴、交易数据的标准化报告。这些功能的核心特征是规则明确、输入可验证、输出可预测。\n\n**不能完全迁移的功能**则集中在需要法律效力或主观判断的领域：新交易的法律确认、违约管理中的自由裁量、跨账本协调、监管机构的特殊数据访问、压力情景下的保证金参数调整。这些功能依赖机构的法律地位、监管授权和人类判断力。\n\n> **KC\n\n[... middle omitted ...]\n\n心机构的最新研究，帮你持续跟踪代币化金融基础设施的最新进展。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n代币化时代，金融基础设施怎么变？\n\n中间商的进化论\n\n代币化不会消灭中间商，但会重新定义它。\n\n刚读完IMF这篇研报，核心判断很清晰：智能合约能接管大部分确定性、规则型操作，但法律确定性、治理问责、压力下的裁量权，还得靠机构。\n\n1/ 哪些功能可以上链？\n- 记账、结算、抵押品转移、数据报告\n- 这些流程高度标准化，代码执行比人工更高效、更透明\n\n2/ 哪些必须留在线下？\n- 法律确权、合规审查、风险判断\n- 极端行情下的保证金调整、违约处理——这些需要人的判断力\n\n3/ 最可能的终局：混合模式\n- 不是区块链取代CSD/CCP/TR\n- 而是智能合约做操作层，机构做治理层\n- 代码+机构共同提供信任和韧性\n\n一个有趣的细节：研报提出了三种架构模型（单一账本、兼容账本、共同账本），不同模型下风险分布完全不同。单一账本效率最高但单点风险集中，兼容账本灵活性好但跨链协调成本高。\n\n对于从业者来说，这不是要不要拥抱区块链的问题，而是如何重新分配责任的问题。\n\n你觉得在代币化资产的世界里，哪些金融基础设施角色最可能被代码取代？\n\n#学习笔记\n\n[source_mineru.md]\n# The Evolution of\n\n[... middle omitted ...]\n\n12c27b9311808e34818b7599fe92da7e6c21a27acc4b6565bf9.jpg)\n\nIMF Working Paper\nMonetary and Capital Markets Department\n\nThe Evolution of Financial Market Infrastructures in a Tokenized Economy Pr\n\n[... middle omitted ...]\n\nized Finance.” Journal of Financial Regulation, Vol. 10, No. 2, pp. 213–242. Oxford University Press. https://doi.org/10.1093/jfr/fjad014.\n\n![](images/486b9fd2f43b8afcadc8d10d9af0c63e691b4c386774987c1d4df917da99f381.jpg)"
  },
  {
    "id": "R003",
    "title": "IMF：吉尔吉斯斯坦三年狂飙后，真正的考验是通胀与改革窗口",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "IMF",
    "digest": "[wechat_article.md]\n# IMF：吉尔吉斯斯坦三年狂飙后，真正的考验是通胀与改革窗口\n\n吉尔吉斯斯坦正在经历一个罕见的增长周期。2021年至2025年，该国实际GDP累计扩张47%，成为全球增长第三快的经济体。人均GDP在四年内翻倍，达到3100美元。对于一个正在从低收入向中等收入过渡的中亚国家而言，这样的成绩单足以让许多新兴市场羡慕。\n\n但IMF在2026年7月发布的第四条款磋商报告中，给出了一个清醒的判断：这轮高增长的主要驱动力——转口贸易、侨汇流入和大规模基建支出——正在接近天花板。2026年3月，通胀已攀升至11%，远超央行5-7%的目标区间。财政从连续三年的盈余转为赤字，信贷增速接近50%，银行体系与主权信用的关联度在加深。\n\n这份报告的核心信息可以概括为一句话：吉尔吉斯斯坦用四年时间跑出了加速度，但真正的考试才刚刚开始。问题不是增长是否可持续，而是能否在增长放缓之前，用改革建立起真正的韧性。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 增长引擎正在切换：从贸易红利到基建驱动，中间存在一个空档期\n\n过去四年的增长故事，本质上是一个地缘政治红利的故事。2022年以来，吉尔吉斯斯坦作为欧亚经济联盟成员，承接了大量因制裁而转移的贸易流。转口贸易、跨境支付和物流服务成为经济的主要拉动力。出口在2023年和2024年分别增长52%和53%，远超历史均值。\n\n但这份IMF报告明确指出，这些贸易相关的收益正在消退。2025年出口已经出现14.5%的下降，2026年预计因基数效应反弹至70%，但此后增速将迅速回落到个位数。报告使用的措辞是“reexport and trade-related activities plateau”——转口贸易进入平台期。\n\n> **KC评论：** 这不是一个短期的周期性调整，而是增长动力的结构性切换。过去四年吉尔\n\n[... middle omitted ...]\n\n的完整解读、原始图表和附录分析，欢迎加入我们的社群继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n吉尔吉斯经济连续4年高增长后，通胀开始冒头了\n\n中亚经济观察\n\n2026年IMF最新报告划重点\n\n投行研报刚更新了吉尔吉斯共和国的经济评估。这个中亚小国过去4年表现亮眼，2025年GDP增速达到11%，但2026年3月通胀已飙到11%，超出央行5-7%的目标区间。\n\n几个关键点值得关注：\n\n1️⃣ 增长引擎正在切换\n过去靠转口贸易、侨汇流入和基建投资拉动的模式，现在增长动力在减弱。2026年增速预计回落到6.1%，但中长期有大型基建项目托底。\n\n2️⃣ 财政从盈余转向赤字\n2023-2025年连续三年财政盈余后，2026年预计转为赤字，主要因为公共工资和资本支出增加。公共债务可持续，但融资需求不小。\n\n3️⃣ 货币政策面临两难\n通胀高企但增长放缓，央行需要平衡。IMF建议维持数据依赖的紧缩立场，直到通胀稳定回到目标区间。汇率需要更多弹性来应对外部冲击。\n\n4️⃣ 金融风险在积累\n信贷增速过快、不良贷款率偏高、银行与政府关联加深，这些都是需要警惕的信号。虚拟资产监管也是新课题。\n\n5️⃣ 结构性改革是关键\n国企改革、营商环境、反腐败、减少非正规经济，这些老问题依然是增长瓶颈。中小企业占GDP约50%，但能\n\n[... middle omitted ...]\n\nat concluded the Article IV consultation with the Kyrgyz Republic.\n\n\\- The Staff Report prepared by a staff team of the IMF for the Executive Board's consideration on June 3, 2026, following d\n\n[... middle omitted ...]\n\n applications to improve public service delivery and support broader socio-economic development. In this context, they plan to further strengthen the regulatory framework and continue investing in digital infrastructure."
  },
  {
    "id": "R004",
    "title": "IMF报告：吉尔吉斯共和国的真实货币政策远比政策利率宽松",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "IMF",
    "digest": "[wechat_article.md]\n# IMF报告：吉尔吉斯共和国的真实货币政策远比政策利率宽松\n\n当一家央行的政策利率传递紧缩信号，而市场利率、信贷增速和流动性状况却指向相反方向时，决策者该如何判断真实的经济温度？IMF最新发布的吉尔吉斯共和国国别报告，用一套完整的金融条件指数（FCI）框架回答了这个问题。结论明确：该国自2024年初以来，实际金融条件已显著宽松，而政策利率的紧缩信号在很大程度上被过剩流动性、快速信贷扩张和偏低的货币市场利率所抵消。\n\n这份报告的价值不仅在于其分析对象——一个中亚小型开放经济体——更在于它为所有面临“流动性过剩困境”的央行提供了一个可复用的诊断框架。当银行体系持续处于净盈余状态、央行沦为系统的净借款人时，政策利率的传导机制就会失灵。这一问题在全球许多新兴市场和发展中经济体普遍存在。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 过剩流动性正在瓦解政策利率的传导链条，央行需要重新审视自己的操作锚\n\n报告的核心发现之一是，吉尔吉斯国家银行（NBKR）虽然维持了相对较高的政策利率，但银行间市场利率持续低于政策利率，两者之间出现了一个持续存在的“楔子”。原因在于，该国的银行体系自2022年以来一直处于结构性流动性过剩状态——央行再也没有向银行提供过再融资，反而需要从银行吸收资金。\n\n这种局面下，利率走廊的“地板”取代了政策利率，成为货币市场利率的实际锚。当走廊地板被调低时，即便政策利率纹丝不动，银行间利率和短期收益率也会随之下行。这意味着，央行发出的紧缩信号在实际融资条件层面被“短路”了。\n\n> **KC评论：** 这不仅仅是吉尔吉斯的问题。任何面临持续资本流入、财政存款淤积或黄金购买等带来流动性过剩的央行，都会遇到同样的困境。报告中的这个分析框架，对于理解中国央行在2014-2016年以及2020年疫情期间的货币政策操作，同样具\n\n[... middle omitted ...]\n\n新数据图表合集，既方便喂给AI，也方便人工快速把握市场动态。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n利率信号失效？吉尔吉斯斯坦的货币政策困局\n\n货币政策信号失灵？\n\n政策利率≠真实融资条件，吉尔吉斯斯坦案例拆解\n\n---\n\n最近读到IMF一份关于吉尔吉斯斯坦的研报，很有意思。它讲了一个核心问题：**政策利率高≠市场真的紧。**\n\n1️⃣ **信号与现实的割裂**\n- 虽然央行维持了相对高的政策利率，但市场上实际利率（银行间拆借利率）一直低于政策利率，说明有效融资条件其实是宽松的。\n- 原因：银行系统流动性过剩（来自央行购金、国有银行注资、政府存款投放），银行不需要互相借钱，反而把多余的钱存在央行吃隔夜利息。\n- 结果：政策利率的传导失效，市场利率被走廊下限（存款便利利率）锚定，而不是政策利率。\n\n2️⃣ **信贷扩张与通胀压力**\n- 流动性宽松直接推动了信贷高速增长，尤其是居民短期消费贷和房贷。\n- 新增银行贷款占GDP比重已超25%，金融深化速度很快，但也积累了脆弱性。\n- 通胀压力从早期的外部成本推动，逐渐转向国内需求拉动，通胀率已高于央行5-7%的中期目标区间。\n\n3️⃣ **金融条件指数（FCI）的启示**\n- 研报构建了一个包含政策利率、市场利率、货币总量、信贷、汇率、外部因素的综合FCI。\n-\n\n[... middle omitted ...]\n\nMiddle East and\n\nCentral Asia\n\nDepartment\n\nPrepared By Nasir Rao, Anvar Muratkhanov, and Farid Talishli (all MCD)\n\n## CONTENTS\n\n## BEYOND THE POLICY RATE: A BROADER VIEW OF MONETARY AND FINAN\n\n[... middle omitted ...]\n\n2–2023. World Bank.\n\nWorld Bank (2024). Kyrgyz Republic Skills and Jobs Diagnostic. World Bank.\n\nNational Development Program of the Kyrgyz Republic (2030). National Development Program of the Kyrgyz Republic until 2030."
  },
  {
    "id": "R005",
    "title": "IMF：SDR新分配的门已经关上，但钥匙还在桌上",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "IMF",
    "digest": "[wechat_article.md]\n# IMF：SDR新分配的门已经关上，但钥匙还在桌上\n\n2026年6月26日，IMF总裁向理事会提交了一份报告。这份报告的结论并不复杂：在第十三次基本期内，IMF不会主动提议进行新一轮的特别提款权（SDR）普遍分配。上一次这样的分配发生在2021年，规模创历史之最，达到4565亿SDR，用于应对新冠疫情引发的全球流动性危机。再上一次是2009年，应对全球金融危机。再往前推，1981年之后整整28年没有过任何普遍分配。\n\n这份报告的核心判断是：**当前全球经济并不缺流动性，也不缺储备资产，因此SDR分配的经济理由不成立。同时，主要股东的政治支持也不到位。** 但报告留了一个明确的活口——总裁可以在基本期内任何时候，主动或应理事会请求，重新提出分配提案，前提是出现“意料之外的重大发展”。\n\n这不是一份宣告终结的文件，而是一份“暂停键”声明。它告诉市场：SDR作为全球储备资产的补充工具，其使用门槛极高，既需要经济危机级别的触发条件，也需要85%投票权的政治共识。这两个条件目前都不满足。\n\n> **KC评论：** 这份报告最值得读的不是结论本身，而是IMF如何定义“长期全球储备资产补充需求”。这个定义决定了未来什么级别的危机才能重新打开SDR分配的大门。完整报告中的图1和图2展示了全球储备资产、资本流动和贸易相对于SDR存量的历史变化，这些图表才是判断未来触发条件的分析工具。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 全球储备资产充裕到不需要SDR补充，这是当前最硬的否决理由\n\nIMF报告最核心的经济判断是：自2021年分配以来，全球储备资产增长了超过21%，新兴和发展中国家（不含中国）增长了超过22%。SDR存量相对于全球储备、资本流动和国际贸易的比例，都显著高于2021年分配前的水平，也高于历史均值。\n\n这意味着，即使存\n\n[... middle omitted ...]\n\n资产的结构性变化——你可以继续在完整报告中找到更完整的答案。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球央行储备够用了，SDR暂不增发\n\nIMF暂缓SDR增发\n\n全球储备充足，新SDR分配没戏\n\n📌 国际货币基金组织（IMF）刚刚发布了一份重磅政策文件——关于是否在下一个五年基本期（2027年起）启动新一轮SDR（特别提款权）增发。\n\n结论很明确：**暂时不搞了。**\n\n1️⃣ 为什么这次不增发？\n\n- 2021年那轮SDR增发是史上最大规模（4565亿SDR），当时是为了应对新冠危机。\n- 但自那以后，全球储备资产增长了超过21%，新兴市场（不含中国）更增长了22%以上。\n- SDR占全球储备、资本流动和贸易的比例，都远高于2021年增发前和历史均值。\n- 虽然中东战争有影响，但冲击不对称、持续时间不确定，目前还构不成\"长期全球储备不足\"的理由。\n\n2️⃣ 投票支持率不够\n\n- 新SDR分配需要获得85%的投票权支持。\n- IMF总裁与各执行董事沟通后，多数投票权代表明确表示**不支持**在当前背景下启动新分配。\n- 参考历史：2009年全球金融危机、2021年新冠危机，才是两次触发SDR增发的\"大事件\"。\n\n3️⃣ 但这不等于永远不搞\n\n- 文件明确说：在2027-2031年的第十三个基本期内，总裁可以\n\n[... middle omitted ...]\n\nallows for the deletion of market-sensitive information and premature disclosure of the authorities' policy intentions in published staff reports and other documents.\n\nElectronic copies of IMF\n\n[... middle omitted ...]\n\n3/\n\n![](images/8a5d5f257ae9a775547d50b1c2b76cc2a41b630a313d668f9969a60af137cf8e.jpg)  \nSource: IMF; World Economic Outlook; and Fund staff calculations.  \n1/ Including gold.  \n2/ Excluding China.  \n3/ Goods and services."
  },
  {
    "id": "R006",
    "title": "IMF报告：Tokenization正在重塑金融基础设施，但真正的赢家是“兼容者”",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "IMF",
    "digest": "[wechat_article.md]\n# IMF报告：Tokenization正在重塑金融基础设施，但真正的赢家是“兼容者”\n\n金融世界的底层架构正在经历一场静默但深远的变革。Tokenization——在区块链基础设施上发行和转移资产的过程——已经从技术实验阶段进入主流金融市场的核心讨论区。国际货币基金组织（IMF）在2026年7月发布的这份报告中，没有使用任何煽动性的语言，而是以一贯的克制和严谨，勾勒出一个正在快速成型的图景：传统银行、加密原生企业、公共部门正在围绕同一套技术栈展开博弈，而这场博弈的结果将决定未来十年金融市场的运行规则。\n\n这份报告最值得关注的判断并非某个具体技术路线会胜出，而是：**基础设施层正在发生的“混合治理”实验，将比资产层本身的产品创新更具决定性。** 谁能在开放性与合规性之间找到可持续的平衡点，谁就能在下一阶段的金融架构中占据枢纽位置。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 银行与加密企业正在走向“双向奔赴”，但动机截然不同\n\n过去几年，市场习惯于将传统银行与加密原生企业视为两个对立的阵营。银行偏爱许可链，强调隐私、可控性和监管合规；Circle、Coinbase等企业则押注无许可链，强调去中心化、全球可用性和开放性。IMF报告揭示了一个更微妙的现实：双方正在向对方的地盘移动，但背后的逻辑完全不同。\n\nJPM将其代表银行存款的JPM Coin部署在Coinbase的无许可链Base上；UBS加入了Tempo的公共测试网；法国兴业银行在以太坊、Solana、Stellar和XRP Ledger上发行欧元稳定币。这些传统金融机构并非抛弃了对合规的坚持，而是学会了在无许可链上叠加“许可控制”——通过白名单机制限制谁可以持有和交易代币，创造出所谓的“混合治理模型”。\n\n与此同时，Circle推出了Arc——一条许可的第一层区块\n\n[... middle omitted ...]\n\n，一起追踪tokenization从理论到实践的每一步演变。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n代币化金融，真的来了\n\n**代币化金融，正在重塑货币**\n\nIMF 最新研报（2026/006）指出，代币化——在区块链上发行和转移资产——正在金融体系内加速渗透，并将深刻影响市场结构、风险管理和金融稳定。传统“垂直整合”的银行模式正在被解构。\n\n**三个核心趋势值得关注👇**\n\n**1/ 基础设施层：公链 vs 联盟链，走向“混合治理”**\n\n过去，Circle、Coinbase 偏好以太坊等公链；银行则偏爱联盟链。但最近变化明显：\n\n- JPM Coin 已部署在 Coinbase 的 Base 公链上\n- UBS、SG也开始在 Solana、XRP 等公链上发行稳定币\n- Swift 正在构建 EVM 兼容的区块链基础设施，由自身运营\n\n关键点：**公链+白名单**的混合模型正在成为主流——既享受全球流动性和标准化，又保留合规控制。\n\n**2/ 资产层：代币化存款 vs 稳定币，谁更优？**\n\n| 维度 | 代币化存款 | 稳定币 |\n|------|-----------|--------|\n| 发行主体 | 银行 | 非银行实体 |\n| 法律地位 | 存款保险覆盖 | 依赖全额储备 |\n| 可编\n\n[... middle omitted ...]\n\noader policy community. The views expressed in IMF Notes are those of the author(s), although they do not necessarily represent the views of the IMF, or its Executive Board, or its Management.\n\n[... middle omitted ...]\n\n-blockchain-based-shared-ledger-progresses-mvp-implementation\n\nTempo Team. 2025. \"Tempo's Testnet Is Live.\" https://tempo.xyz/blog/testnet\n\n![](images/bcfea95179a52a8c74cb4c029ff87f3e60a5dbedf2c490153faacc46150d8a85.jpg)"
  },
  {
    "id": "R007",
    "title": "波士顿咨询：资管行业增长幻觉终结，净流入能力成为唯一护城河",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "波士顿咨询",
    "digest": "[wechat_article.md]\n# 波士顿咨询：资管行业增长幻觉终结，净流入能力成为唯一护城河\n\n全球资管规模在2025年突破了147万亿美元，利润率依旧保持在30%以上。表面看，这是一个欣欣向荣的行业。但波士顿咨询最新发布的《全球资管报告2026》给出了一个截然不同的判断：行业正在进入一个“增长不增收、规模不经济”的新阶段。超过80%的收入增长来自市场上涨本身，而非管理人的主动能力。当市场不再提供免费顺风车，资管行业的核心竞争逻辑正在被重写。\n\n这份报告的核心信号是：资管行业过去十五年依赖的“市场涨→规模涨→收入涨”的增长公式已经失效。未来五年，能够持续捕获净流入的机构，将占据行业利润的绝大部分。而捕获净流入的能力，正从“产品能力”转向“渠道嵌入能力”和“技术基础设施能力”。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 市场顺风不再普惠，净流入成为真正的分水岭\n\n波士顿咨询的数据显示，2024至2025年间，全球资管行业收入增长的80%以上由市场估值上升驱动。这意味着，如果市场进入震荡或下行周期，行业的收入基础将面临严重侵蚀。更值得关注的是，利润率在过去十五年间几乎原地踏步——2010年行业利润率约为30%，2025年仍接近这一水平。收入年增速5.1%，成本增速却达到5.4%，行业实际处于“负经营杠杆”状态。\n\n这背后的结构性原因有三个。第一，机构管理费以每年3%的速度下降。第二，被动产品和ETF持续主导净流入，而这些产品的费率远低于主动管理。第三，主动管理ETF虽然增长迅速，但其费率水平也低于传统共同基金。每新增一美元管理规模，带来的平均管理费都在降低。\n\n> **KC评论：** 很多从业者把“规模增长”等同于“竞争力增强”。但波士顿咨询的数据揭示了一个残酷事实：如果规模增长主要来自市场上涨而非净流入，那么规模越大，反而可能意味着更大的成本压力和\n\n[... middle omitted ...]\n\n投资机会——有更深入的兴趣，欢迎加入社群，我们一起继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n资管行业增长逻辑正在换挡\n\n增长逻辑在变了\n\n市场好不再是万能药\n\n---\n\n**BCG 2026全球资管报告的核心判断：**\n过去十年，市场涨 = 资管赚。但往后，这套逻辑行不通了。\n\n**几个关键变化：**\n\n**1️⃣ 增长来源变了**\n2025年全球资管规模达147万亿美元，但超80%的收入增长靠市场上涨，不是靠新钱流入。\n未来真正拉开差距的，是谁能持续吸引净流入，而不是搭市场顺风车。\n\n**2️⃣ 零售客户成为主力**\n2020-2025年，零售客户贡献了全球资管规模增长的61%。\n亚太地区增速最快，年增9%。\n新一代投资者（Gen Z、千禧一代）习惯通过数字平台、社交媒体做决策，传统资管在这些渠道几乎没存在感。\n\n**3️⃣ 资金越来越集中**\n美国被动基金前10家公司拿了超90%的净流入。\n私募市场前50家PE机构2024年募资占比37%，远超十年均值22%。\n渠道和平台成了新的“看门人”，能不能被放在货架上，决定了很多管理人的命运。\n\n**4️⃣ 规模增长≠利润增长**\n过去15年，资管规模翻了三倍，收入翻了两倍，但利润率一直卡在30%左右。\n原因：费率持续下降（被动产品、ETF占比提升）+ \n\n[... middle omitted ...]\n\n Source of Advantage in Asset Management\n19 Rebuilding Asset Management for an AI-First World\n25 Appendix\n29 About the Authors\n\n![](images/af9ad589acd8ad92c3f760759599cd9ba0d45fc3ded0543693462\n\n[... middle omitted ...]\n\nd register to receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on LinkedIn, Facebook, and X.\n\n![](images/b289ca9fabf62c91cf18a36dc7a4ba063c1dbc86b2cf0c1dc2636fb06ff44f71.jpg)"
  },
  {
    "id": "R008",
    "title": "波士顿咨询：营销的终极形态，不是“旅程”而是“原子动作”",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "波士顿咨询",
    "digest": "[wechat_article.md]\n# 波士顿咨询：营销的终极形态，不是“旅程”而是“原子动作”\n\n当一家企业还在为优化客户旅程而投入重金时，波士顿咨询（BCG）在最新研报中给出了一个颠覆性判断：**以“旅程”为核心的营销范式，其增长红利已经见顶。** 下一个十年的竞争，将围绕“原子动作”展开——由AI代理实时选择、排序和组合营销动作，而人类营销者的角色，将从旅程设计师转变为货架策展人。\n\n这不是渐进式改良。这是一次营销底层操作系统的切换。对于任何依赖客户生命周期管理的企业，理解这一转变的紧迫性，可能决定了未来18个月是领跑还是掉队。\n\n---\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 旅程模型的困境：规模不经济与响应滞后\n\n过去十年，“客户旅程”是营销组织最核心的构建块。它逻辑清晰、可执行，通过预设触点引导客户完成转化。但BCG指出，这套模型正在遭遇双重瓶颈。\n\n第一，规模不经济。每新增一个细分客群、一次产品发布或一个新渠道，都需要新建一条旅程。当旅程数量从几十条膨胀到几百甚至上千条时，团队的管理能力被迅速摊薄。每条旅程的边际收益在下降，而维护成本却在指数级上升。\n\n第二，响应滞后。旅程是预定义的。当客户在真实场景中遭遇意外事件——比如刚打完投诉电话，20分钟后打开App——旅程模型无法感知这种动态语境，仍会推送预设的促销信息。这不仅是体验的错配，更是信任的消耗。\n\nBCG的核心洞察在于：**旅程模型把“决策单元”设得太大了。** 它试图用一条固定的路线图去覆盖所有可能性，而现实中的客户信号是碎片化、实时变化的。当决策单元从“整条旅程”缩小到“单个动作”，新的可能性才会打开。\n\n> **KC评论：** 旅程模型的困境，本质上是“计划赶不上变化”。你花三个月设计了一条完美的旅程，但客户的行为在三个月里已经变了三次。BCG的建议看似技术化，实则是在问一个\n\n[... middle omitted ...]\n\n与数百位产业决策者和投资者一起，讨论这些研报背后的真实含义。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n个性化营销，进入AI代理时代\n\n**AI代理时代**\n\n**营销人从画流程图，变成管素材库**\n\n某外资投行最新研报指出，传统客户旅程模型的增长已触顶。核心矛盾是：渠道爆炸、信号实时、内容太多，人工画流程根本跟不上。\n\n下一代解决方案叫“AI代理驱动的行动”——不是让AI帮你跑完预设流程，而是让AI自己选动作、排顺序、组内容，实时响应每个客户。\n\n📌 三个进化阶段，你在哪一层？\n\n1️⃣ **第一代：人工编排旅程**\n营销人手动建受众、画流程图、定规则。每推一个新品、开一个新渠道，就要新建一条旅程。团队很快管不过来。\n\n2️⃣ **第二代：模型优化旅程**\n营销人定义组件和目标，AI在预设框架里选最优分支。决策单元从“整个旅程”变成“旅程的每一步”。效率提升，但底层逻辑没变。\n\n3️⃣ **第三代：AI代理自主行动**\n营销人不再画流程，而是搭建一个“可组合素材库”，设定目标。AI代理从库里实时挑选、排序、组合原子级动作（比如一条文案、一张图、一个优惠券），秒级响应客户。\n\n📌 这个“可组合素材库”长什么样？\n\n研报把它分成三个颗粒度：\n- **原子资产**：单条文案、单张图片、单个优惠模板——最基础积木\n-\n\n[... middle omitted ...]\n\npossible content, offers, and experiences has grown substantially.\n\nAs a result, the journey model's impact has plateaued. Personalization must evolve by changing its unit of decision from mar\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R009",
    "title": "波士顿咨询：BCG：Physical AI的回报周期已从5-7年缩至1-3年，CEO们还在等什么？",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "波士顿咨询",
    "digest": "[wechat_article.md]\n# 波士顿咨询：BCG：Physical AI的回报周期已从5-7年缩至1-3年，CEO们还在等什么？\n\n当波士顿咨询（BCG）在一份面向CEO的指南中写下“50%可自动化工作范围扩大、工程时间减少70%、投资回报周期从5-7年缩短到1-3年”这三个数字时，它传递的信号绝不仅仅是技术进步。它意味着，物理AI（Physical AI）正在跨越一个关键的临界点——从“值得关注”到“必须行动”。\n\n过去五年，多数产业决策者对工业自动化的认知还停留在“昂贵、僵化、只适合大规模重复生产”的传统机器人时代。但BCG这份报告的核心主张是：由于计算机视觉、虚拟训练环境和软件定义架构的突破，机器人正在变得“能看、能适应、能实时调整”。这直接降低了部署的复杂度和成本，也提高了不行动的机会成本。\n\n对于任何管理着制造、仓储、物流或任何涉及物理操作流程的决策者而言，这不再是一个“要不要拥抱未来”的问题，而是一个“如何在对手之前完成系统重构”的问题。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 这轮变化真正考验的是企业能否把规模转化为议价权\n\nBCG报告中最具冲击力的数字不是技术参数的提升，而是经济模型的改变。传统机器人投资回报周期通常在5到7年，而物理AI已将这一周期压缩至1到3年。这意味着，一个决定是否部署物理AI的决策，其财务影响在CEO的常规任期之内就会显现。\n\n更关键的是成本结构的重构。报告指出，传统机器人约75%的成本来自系统集成、安装和工程调试。而软件定义的物理AI可以将这部分成本削减超过一半。这个数字背后是一个根本性的转变：自动化不再只是资本密集型巨头的游戏，那些能够快速决策、灵活试错的中型企业，也获得了参与竞争的资格。\n\n> **KC评论：** 1-3年的回报周期意味着，即使一家企业现在才开始规划物理AI部署，在大多数CEO的\n\n[... middle omitted ...]\n\n的社群，与产业决策者一起持续追踪物理AI与自动化的最新趋势。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nCEO们，物理AI已进入部署期\n\n**物理AI，落地加速**\n\n别再以为机器人离你很远。某外资投行最新报告指出，物理AI正把自动化范围扩大50%，机器人能看、能适应、能实时调整，部署成本陡降。\n\n**核心数据：**\n- 自动化工作范围提升50%，传统机器人做不到的现在可以了\n- 训练机器人所需工程时间减少70%\n- 投资回收期从5-7年缩短到1-3年，快了3倍\n\n**为什么现在不一样？**\n1. 视觉感知：机器人能识别物体和位置，适应新环境\n2. 灵巧操作：可以处理可变形的物体，但还需针对性训练\n3. 工作流规划：告诉它“做什么”，它能自己拆解步骤（仍在开发中）\n4. 推理能力：最高目标，通用人形机器人还差得远\n\n**CEO应该做的五件事：**\n\n1. 重新评估运营效率\n别想C-3PO那种全能机器人，先看哪些环节现在就能用。视觉感知和部分灵巧操作已经成熟，其他还在路上。\n\n2. 整体设计工作流\n机器人能替代50%的任务，但不是全部。比如它能做重复装配，但做不了质检。需要重新设计流程，把任务重新分配。\n\n3. 先想好技术架构再找供应商\n别被供应商带着走。先规划好硬件、操作系统、模拟训练环境怎么整合，再谈购买。动\n\n[... middle omitted ...]\n\nnding still for companies that hesitate.\n\n## What the Numbers Say\n\n50%\n\nIncrease in the scope of work that can be automated compared to traditional robotics\n\n70%\n\nReduction in\nengineering time\n\n[... middle omitted ...]\n\nee in an unfamiliar real-world environment. It encapsulates the challenge of integrating perception, manipulation, planning, and adaptability in unstructured settings as a proxy for general-purpose embodied intelligence."
  },
  {
    "id": "R010",
    "title": "波士顿咨询：营销战役的终结，不是营销的终结",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "波士顿咨询",
    "digest": "[wechat_article.md]\n# 波士顿咨询：营销战役的终结，不是营销的终结\n\n当一家咨询公司用“终结”这个词来定义一场变革，它不是在制造恐慌，而是在划清时代。波士顿咨询（BCG）在2026年7月发布的最新系列报告第四部分中，给出了一个明确且尖锐的判断：以“战役”和“日历”为核心的传统营销组织方式，正在走向终结。取而代之的，是一个由AI代理（Agent）驱动的、以“下一最佳行动”为逻辑的实时决策体系。\n\n这不是一个渐进式的优化，而是一个结构性的替代。BCG的报告指出，在成熟模式下，70%到80%的客户触点将从预定义的营销战役，转向由AI代理从“可组合货架”上实时调取的个性化交互。这意味着，过去二十年里支撑品牌营销大厦的基石——从季度 campaign 规划、长周期创意制作，到层层审批的线性流程——都将被重新定义。\n\n对于正在试图理解AI如何真正重塑商业的决策者来说，这份报告的价值不在于罗列技术趋势，而在于它清晰地拆解了“从哪开始改”和“改成什么样”。它回答了一个所有营销负责人此刻都该追问的问题：如果AI代理已经能自主决策，那我的组织应该做什么，又不该做什么？\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 营销组织的核心单元，必须从“战役”切换为“货架”\n\nBCG报告最核心的洞察，是揭示了两种完全不同的营销组织逻辑。传统模式下，营销工作的基本单元是“战役”。一个战役对应一个目标、一个受众群体、一套创意素材，然后被排上日历，按部就班地执行。这种模式假设所有决策都由人类做出，并通过将客户分群来管理复杂性。\n\n而AI代理驱动的模式，将逻辑完全颠倒。系统不再从“我们要推什么”出发，而是从“这位客户此刻需要什么”出发。营销组织的核心任务，不再是规划下一个战役，而是持续构建、优化和填充一个“可组合货架”。货架上存放的不是完整的战役包，而是模块化的内容、优惠、体验片\n\n[... middle omitted ...]\n\n入我们的社群，与同行者一起，把这场变革的方向盘握在自己手中。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n70%营销触点即将告别传统campaign\n\n**告别campaign**\n\n当AI代理接管70%-80%的客户互动\n\n---\n\n最近看BCG一份研报，讲的是营销campaign的终结。不是标题党，是真的在发生。\n\n过去几十年，营销围绕“campaign”和“日历”运转：先定人群、做创意、排期、上线。这套逻辑假设人类处理所有决策，客户被分进segments，沟通按计划推送。\n\n但现在AI代理可以实时感知每个客户的上下文，从“可组合货架”上即时选取最优动作。日历不再是组织原则，预定义人群让位给实时情境。\n\n**核心变化：营销拆成“构建”和“交付”两件事**\n\n1️⃣ **构建端**：营销人+AI代理一起生产内容、offer、体验，存入“可组合货架”\n2️⃣ **交付端**：完全由自主代理执行1:1编排，在业务规则内做个性化\n\n成熟模式下，70%-80%的客户触点将从预定义campaign转向AI驱动的实时互动。\n\n**执行链的重塑**\n\n传统流程：60-90天，20+人，多次交接，产出单一campaign。\n\n新流程：营销人从做执行转向给战略方向——写brief、策展内容、验证品牌一致性。AI代理负责素材生成、\n\n[... middle omitted ...]\n\nving. Now comes the hardest part: changing the prevailing ways of working.\n\nCompanies need to address three key aspects of the broader marketing operating model. The first is a shift in how or\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R011",
    "title": "波士顿咨询：下一代个性化决策，关键不在算法而在组织架构",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "波士顿咨询",
    "digest": "[wechat_article.md]\n# 波士顿咨询：下一代个性化决策，关键不在算法而在组织架构\n\n当一家信用卡发卡机构用传统模型筛选出“高余额、长 tenure”的客户来推送余额转账优惠时，一个被历史数据掩盖的真相浮出水面：新激活的中等余额客户，配合特定创意素材，响应率反而更高。这个发现，不是分析师做出来的，而是“上下文老虎机”自己探索出来的。\n\n这份波士顿咨询（BCG）最新发布的系列报告第三部分，给出了一个对技术和商业决策者都极具冲击力的判断：下一代“最优下一步行动”（NBA）系统的科学基础已经就绪，但绝大多数企业连第一层都没用好。真正的瓶颈不是算法，而是组织架构和人才储备。\n\nBCG 将 NBA 的决策科学分为三个层次：倾向性与 uplift 评分、上下文老虎机、以及基于基础模型的智能体推理。这三个层次不是递进关系，而是叠加关系。最有效的系统需要同时运行所有三层。但现实是，绝大多数企业连第一层都没有做到位。\n\n> **KC评论：** 这份报告最值得读的部分，不是它描述了多么前沿的技术，而是它给出了一个非常务实的判断：先把自己的第一层做好，再谈升级。很多企业连“倾向性模型”和“uplift 模型”的区别都没搞清楚，就急着上大模型，这恰恰是 BCG 要纠正的误区。完整报告里有一张图清晰地展示了每一层能做什么、不能做什么，值得仔细看。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 第一层不是“能做就行”，而是“先做对”：20%到40%的营销预算正在被浪费\n\nBCG 毫不客气地指出，大多数企业目前停留在第一层——倾向性与 uplift 评分。但即便在这一层，也存在着结构性的缺陷。\n\n倾向性模型回答“这个客户有多大概率响应”，但回答不了“这个动作是否改变了客户的行为”。一个90%倾向性购买的人，可能本来就要买。如果此时推送折扣，等于白白牺牲利润。BCG 给出的数\n\n[... middle omitted ...]\n\n模型在营销场景中的真实价值，这份BCG系列报告值得完整阅读。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n你的个性化推荐，卡在哪一层？\n\n**三阶决策，从猜你到懂你**\n\n不是每个推荐系统，都配叫“懂你”\n\n**正文**\n\n最近读了一篇BCG的研报，讲的是个性化推荐的下一个范式：Next-Best Action。简单说，就是从“猜你喜欢什么”升级到“知道现在该给你什么”。\n\n报告把决策智能拆成三个层次，层层递进，但每一层都解决不同的问题。\n\n1️⃣ **第一层：倾向性评分**\n\n这是目前大多数平台在做的。模型根据你的历史行为，预测你对某个动作（比如点击、购买）的概率。比如，系统算出来你买咖啡的概率高，就给你推咖啡券。\n\n但有个坑：它只能告诉你“你会不会回应”，不能告诉你“这个动作有没有带来增量”。可能你本来就打算买，推券只是白白损失利润。\n\n2️⃣ **第二层：上下文多臂老虎机**\n\n这一层开始“主动学习”了。系统不再只依赖历史数据，而是主动分配一部分流量去尝试不确定的动作，实时观察效果。\n\n比如，一个信用卡发卡方想测试余额转账offer。传统模型只会给高余额、长账龄的客户推。但多臂老虎机发现：搭配特定创意，新激活的中等余额客户反应更好——这在历史数据里从未出现过。\n\n3️⃣ **第三层：基于大模型的推理**\n\n[... middle omitted ...]\n\nearning loops that compound without human intervention, and a layered architecture with different classes of algorithms.\n\nThis shift requires different applications and a fundamental evolution\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R012",
    "title": "麦肯锡：银行对AI的“谨慎”正在变成一种竞争劣势",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "麦肯锡",
    "digest": "[wechat_article.md]\n# 麦肯锡：银行对AI的“谨慎”正在变成一种竞争劣势\n\n银行对生成式AI的拥抱，看似热烈，实则克制。麦肯锡与IACPM联合对44家全球金融机构的最新调研揭示了一个反直觉的结论：大多数银行在信贷业务中的AI部署，正卡在“试点”与“规模”之间的无人区。这份报告的核心判断是——银行面临的真正挑战，不是技术成熟度，而是组织在战略层面将AI从“效率工具”升级为“竞争杠杆”的意愿和能力。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 过半银行已将其列为优先级，但行动却停留在“尝试”阶段\n\n调研显示，52%的金融机构已将生成式AI的采用列为首要任务，高层通过投资和招聘明确表达了对这一方向的承诺。这一数字本身并不令人意外。真正值得关注的是，即便有了顶层意志，实际落地进展依然缓慢。\n\n报告将银行对AI的应用能力归纳为三类：摘要能力、内容生成能力和客户交互能力。目前，大多数机构的进展集中在“摘要”这一相对低风险的领域——例如早期预警系统和信贷决策支持。只有少数大型机构开始触及更复杂的工作流改造。\n\n这种“高优先级、低执行力”的矛盾，反映出银行在AI战略上的结构性困境。高层喊话与一线落地之间，缺少一个能将战略意图转化为系统化行动的中层架构。\n\n> **KC评论：** 银行不是不想用AI，而是不知道怎么用。这恰恰是麦肯锡报告的洞察价值所在——它把“为什么卡住”拆解成了可诊断的问题：是缺技能、缺框架，还是缺对复杂工作流重构的勇气？完整报告中有更细的用例分级和机构类型对比，值得读者仔细对照自身情况。\n\n![研报图表 2](assets/xhs_card_02.png)\n\n## 2. 区域银行反而领先于大型银行，这背后是组织灵活性的胜利\n\n一个反直觉的数据是：在AI用例部署数量上，核心区域银行（资产1000-5000亿美元）居然领先于超大型银行。这打\n\n[... middle omitted ...]\n\neview，推送全球顶级投行和咨询机构的中文精华摘要，约10-40页，涵盖当天最新数据图表和深度解读。既适合喂给AI做二次分析，也适合决策者在15分钟内把握市场核心动态。我们在社群里继续讨论这些未解的问题。\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n银行AI落地：速度与安全如何兼得？\n\n🔍AI风控新前沿\n\n银行正在加速AI落地，但大部分还在路上\n\n---\n\n最近翻了麦肯锡新出的AI风险特刊，信息密度很高，分享几个核心发现👇\n\n1/ 银行AI进度：区域行反而领先\n- 44家全球金融机构调研显示，52%已将gen AI列为优先事项\n- 有意思的是，区域银行在部署进度上反超了巨型银行\n- 但真正全面落地的案例很少，多数还在试点阶段\n\n2/ 最实用的3个AI能力\n📍汇总能力：把海量数据提炼成要点\n📍内容生成：自动起草信贷备忘录\n📍客户互动：AI助手辅助客户经理\n\n3/ 银行为什么走得慢？\n- 决策者眼光太窄：只盯着简单用例，没去改造复杂流程\n- 代理AI刚起步：很多银行还没开始部署能跨部门协同的AI\n- ROI不好量化：一半机构认为没法早期算清收益\n\n4/ 风控新玩法：4种角色分工\n- 设计师：负责用例设计，懂业务也懂风险\n- 工程师：技术实现，写代码、做监控\n- 治理者：定规则、做红队测试\n- 用户：最终使用者，需要培训风险意识\n\n5/ 最关键的提醒\nAI不是一次性部署，是持续迭代的过程\n风控要“从第一天就嵌入”，而不是事后补救\n\n#学习笔记\n\n[source\n\n[... middle omitted ...]\n\nrco Vettori, Mihir Mysore, Oliver Bevan, Sebastian Schneider, Thomas Poppensieker, Will Humphrey\n\nMcKinsey global publications\n\nPublisher: Raju Narisetti\n\nGlobal editorial director and deputy \n\n[... middle omitted ...]\n\nbanks fight financial crime\n\nHow financial institutions can improve their governance of gen AI\n\nDeploying agentic AI with safety and security: A playbook for tech leaders\n\nImplementing generative AI with speed and safety"
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "IMF视觉摘要 1",
    "figure_type": "external_card",
    "context": "IMF｜IMF报告：柬埔寨预算执行改革走到了哪一步，又卡在了哪里｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F002",
    "report_id": "R002",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Tokenization does not imply disintermediation, but institutional redesign. The most plausible outcome is a hybrid FMI model, in which smart contracts perform a greater share of operational and transactional functions, while legal entities remain responsible fo"
  },
  {
    "figure_id": "F003",
    "report_id": "R002",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## Possible architectures The prior two sections discussed properties of blockchains in the abstract. In reality, the relationship between chains, assets, and owners – the architecture of the tokenized financial system – matters. Architecture encompasses the n"
  },
  {
    "figure_id": "F004",
    "report_id": "R002",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "The first model, called the single ledger model, entails all owners having access to the same ledger on which the assets being transacted are recorded (Figure 3). Two parties might exchange a bond for money on the same ledger, for instance. The simplicity of t"
  },
  {
    "figure_id": "F005",
    "report_id": "R002",
    "label": "IMF视觉摘要 1",
    "figure_type": "external_card",
    "context": "IMF｜IMF：Tokenization不会消灭金融基础设施，但会重新定义谁做什么｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F006",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "42. Staff recommends that the next Article IV consultation be held on a standard 12-month cycle. Sources: country authorities and IMF staff estimates. ## Figure 1. Kyrgyz Republic: Real Sector and Social Indicators Growth outpaced comparators for the past 4 ye"
  },
  {
    "figure_id": "F007",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## Figure 1. Kyrgyz Republic: Real Sector and Social Indicators Growth outpaced comparators for the past 4 years,... Inflation is above target... ...thanks to trade and construction. ...threatening recent poverty reduction. Poverty Headcount Ratio at \\$8.30 pe"
  },
  {
    "figure_id": "F008",
    "report_id": "R003",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "...threatening recent poverty reduction. Poverty Headcount Ratio at \\$8.30 per day $^{1}$ (2021 PPP, in percent of the population) 1/ \\$8.30 per day is a close approximation of the Kyrgyz national poverty rate. Sources: World Development Indicators, World Bank"
  },
  {
    "figure_id": "F009",
    "report_id": "R003",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Sources: World Development Indicators, World Bank, Country authorities, and IMF staff calculations. Per capita income rose sharply in recent years... Sources: Country authorities and IMF staff estimates. ...as income inequality remained comparable to peers. In"
  },
  {
    "figure_id": "F010",
    "report_id": "R003",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Income Inequality in Selected CIS and Baltic States, 2023 (Gini coefficient, 0=perfect equality, 100=highest inequality) ## Figure 2. Kyrgyz Republic: External and Monetary Sectors CA deficit remains sizable... Elements of the Current Account (In Percent of GD"
  },
  {
    "figure_id": "F011",
    "report_id": "R003",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## Figure 2. Kyrgyz Republic: External and Monetary Sectors CA deficit remains sizable... Elements of the Current Account (In Percent of GDP) ...offset by large errors and omissions. Higher gold prices and conversion of non-monetary to monetary gold boosted re"
  },
  {
    "figure_id": "F012",
    "report_id": "R003",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "...offset by large errors and omissions. Higher gold prices and conversion of non-monetary to monetary gold boosted reserves. The exchange rate appreciated in real effective terms... Nominal and Real Effective Exchange Rates (Base 100 - December 2009) ...while"
  },
  {
    "figure_id": "F013",
    "report_id": "R003",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "The exchange rate appreciated in real effective terms... Nominal and Real Effective Exchange Rates (Base 100 - December 2009) ...while interest rates remained subdued. Meanwhile, money and credit continued to grow. ## Figure 3. Kyrgyz Republic: Fiscal Sector R"
  },
  {
    "figure_id": "F014",
    "report_id": "R003",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Nominal and Real Effective Exchange Rates (Base 100 - December 2009) ...while interest rates remained subdued. Meanwhile, money and credit continued to grow. ## Figure 3. Kyrgyz Republic: Fiscal Sector Revenue is buoyed by non-tax proceeds,... Public Revenue -"
  },
  {
    "figure_id": "F015",
    "report_id": "R003",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "## Figure 3. Kyrgyz Republic: Fiscal Sector Revenue is buoyed by non-tax proceeds,... Public Revenue - General Government (In Percent of GDP) Sources: Country authorities; and IMF staff estimates. ...mainly current expenditure,... Public Expenditure - General "
  },
  {
    "figure_id": "F016",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "...due to a higher wage bill, which remains comparatively sizable. Despite the small fiscal deficit in 2025, below-the-line spending is driving sizable financing needs. Financing Needs vs. Fiscal Deficit Sources: Country authorities; and IMF staff estimates. T"
  },
  {
    "figure_id": "F017",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Despite the small fiscal deficit in 2025, below-the-line spending is driving sizable financing needs. Financing Needs vs. Fiscal Deficit Sources: Country authorities; and IMF staff estimates. Total public debt grew in line with nominal GDP. ## Figure 4. Kyrgyz"
  },
  {
    "figure_id": "F018",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Sources: Country authorities; and IMF staff estimates. Total public debt grew in line with nominal GDP. ## Figure 4. Kyrgyz Republic: Financial Soundness Indicators Kyrgyz banks are well capitalized... Profitability remains strong... ...and liquid. ...but NPLs"
  },
  {
    "figure_id": "F019",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "## Figure 4. Kyrgyz Republic: Financial Soundness Indicators Kyrgyz banks are well capitalized... Profitability remains strong... ...and liquid. ...but NPLs are elevated. ...while FX exposure stayed at a 10-year low."
  },
  {
    "figure_id": "F020",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## B. Comparative Landscape of Central Asian Pension Systems 5. A PAYGO framework remains the dominant pension model across the Central Asia region. The Kyrgyz Republic, together with Tajikistan, Turkmenistan, and Uzbekistan has conducted several reforms to mo"
  },
  {
    "figure_id": "F021",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "5. A PAYGO framework remains the dominant pension model across the Central Asia region. The Kyrgyz Republic, together with Tajikistan, Turkmenistan, and Uzbekistan has conducted several reforms to modify their Soviet-era pension model characterized by a PAYGO "
  },
  {
    "figure_id": "F022",
    "report_id": "R003",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "11. The demographics of the PPS are concerning, but stand to improve under a baseline scenario. The effective dependency ratio, i.e. total pensioners as shared of formal employment, is 70 percent in 2025, but improves to around 36 percent by 2065. This is due "
  },
  {
    "figure_id": "F023",
    "report_id": "R003",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "12. The financials of the PPS are under strain. Over the next ten years, the decreasing contribution rate will cause the deficit of the PPS to increase to over 3.3 percent of GDP by 2035. Overall contributions fall from 4.3 to 1.5 percent of GDP by 2035, while"
  },
  {
    "figure_id": "F024",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "## E. Challenges Facing the PPS ## 15. Specific stress tests indicate that the PPS is highly sensitive to economic and demographic developments. Moreover, the effects of such developments are difficult to counteract rapidly with PPS-specific policy measures. I"
  },
  {
    "figure_id": "F025",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "5. The share of employment exposed to generative AI in the Kyrgyz Republic is estimated to be moderate relative to the world average. About 7 percent of employment in the Kyrgyz Republic falls into one of the three highest exposure gradients (from moderate and"
  },
  {
    "figure_id": "F026",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## 6. Employment in the public sector has a larger potential exposure to generative AI. As of employment is in the public sector. Of these, 14 percent of jobs are in top three exposure risks, which is double the corresponding level for total employment (Figure"
  },
  {
    "figure_id": "F027",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "employment is in the public sector. Of these, 14 percent of jobs are in top three exposure risks, which is double the corresponding level for total employment (Figure 1, Panel 3), due to their concentration in administrative, data-processing, and cognitive tas"
  },
  {
    "figure_id": "F028",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "11. Digital infrastructure represents a structural impediment to technological diffusion in the Kyrgyz Republic. Digital infrastructure is one of the two foundational dimensions of AI preparedness, besides HC&LMP. While this measure is slightly higher than the"
  },
  {
    "figure_id": "F029",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "regarding HC&LMP. Despite relatively high public spending on education in the region, poor education quality—reflected in a narrow graduate skillset and below-average STEM graduation rates—limits human capital development (Figures 4 and 5, Panel 2). Moreover, "
  },
  {
    "figure_id": "F030",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## BACKGROUND ## 2. Public debt increased to 39.4 percent of GDP in 2025 from 36.2 percent of GDP in 2024 3. External debt continues to be predominantly denominated in US dollars and SDRs. These two currencies account for around 85 percent of nominal external "
  },
  {
    "figure_id": "F031",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "3. External debt continues to be predominantly denominated in US dollars and SDRs. These two currencies account for around 85 percent of nominal external debt at end-2025 (Text Figure 2). The euro accounts for less than 5 percent. 4. China remains the largest "
  },
  {
    "figure_id": "F032",
    "report_id": "R003",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "3. External debt continues to be predominantly denominated in US dollars and SDRs. These two currencies account for around 85 percent of nominal external debt at end-2025 (Text Figure 2). The euro accounts for less than 5 percent. 4. China remains the largest "
  },
  {
    "figure_id": "F033",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "\\- Consistency between fiscal adjustment and growth (Figure 4). The growth projection for 2026 is below the growth paths suggested by different fiscal multipliers, as recent growth performance is not expected to be sustained. The projected fiscal expansion for"
  },
  {
    "figure_id": "F034",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "1/ Coverage of debt: The central, state, and local governments, central bank, government-guaranteed debt. Definition of external debt is Residency-based. 2/ The underlying PV of external debt-to-GDP ratio under the public DSA differs from the external DSA with"
  },
  {
    "figure_id": "F035",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "3/ Debt service is defined as the sum of interest and amortization of medium and long-term, and short-term debt. 4/ Gross financing need is defined as the primary deficit plus debt service plus the stock of short-term debt at the end of the last period and oth"
  },
  {
    "figure_id": "F036",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "5/ Defined as a primary deficit minus a change in the public debt-to-GDP ratio ((-): a primary surplus), which would stabilize the debt ratio only in the year in question. 6/ Historical averages are generally derived over the past 10 years, subject to data ava"
  },
  {
    "figure_id": "F037",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1. Kyrgyz Republic: Indicators of Public and Publicly Guaranteed External Debt Under Alternative Scenarios, 2026–36 Note: \"Yes\" indicates any change to the size or interactions of the default settings for the stress tests. \"n.a.\" indicates that the stre"
  },
  {
    "figure_id": "F038",
    "report_id": "R003",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Sources: Country authorities; and staff estimates and projections. \\* Note: All the additional financing needs generated by the shocks under the stress tests are assumed to be covered by PPG external MLT debt in the external DSA. Default terms of marginal debt"
  },
  {
    "figure_id": "F039",
    "report_id": "R003",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Sources: Country authorities; and staff estimates and projections. \\* Note: All the additional financing needs generated by the shocks under the stress tests are assumed to be covered by PPG external MLT debt in the external DSA. Default terms of marginal debt"
  },
  {
    "figure_id": "F040",
    "report_id": "R003",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "1/ The most extreme stress test is the test that yields the highest ratio in or before 2036. The stress test with a one-off breach is also presented (if any), while the one-off breach is deemed away for mechanical signals. When a stress test with a one-off bre"
  },
  {
    "figure_id": "F041",
    "report_id": "R003",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "1/ A bold value indicates a breach of the benchmark. 2/ Variables include real GDP growth, GDP deflator and primary deficit in percent of GDP. 3/ Includes official and private transfers and FDI. ## Figure 3. Kyrgyz Republic: Drivers of Debt Dynamics—Baseline S"
  },
  {
    "figure_id": "F042",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Unexpected Changes in Debt 1/(past 5 years, percent of GDP) Gross Nominal Public Debt (in percent of GDP; DSA vintages) Debt-creating flows (percent of GDP) Unexpected Changes in Debt 1/(past 5 years, percent of GDP) 1/ Difference between anticipated and actua"
  },
  {
    "figure_id": "F043",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Gross Nominal Public Debt (in percent of GDP; DSA vintages) Debt-creating flows (percent of GDP) Unexpected Changes in Debt 1/(past 5 years, percent of GDP) 1/ Difference between anticipated and actual contributions on debt ratios. 2/ Distribution across LICs "
  },
  {
    "figure_id": "F044",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "1/ Difference between anticipated and actual contributions on debt ratios. 2/ Distribution across LICs for which LIC DSAs were produced. 3/ Given the relatively low private external debt for average low-income countries, a ppt change in PPG external debt shoul"
  },
  {
    "figure_id": "F045",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "3/ Given the relatively low private external debt for average low-income countries, a ppt change in PPG external debt should be largely explained by the drivers of the external debt dynamics equation. ## Figure 4. Kyrgyz Republic: Realism Tools 3-Year Adjustme"
  },
  {
    "figure_id": "F046",
    "report_id": "R003",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "3-Year Adjustment in Primary Balance (Percentage points of GDP) 1/ Data cover Fund-supported programs for LICs (excluding emergency financing) approved since 1990. The size of 3-year adjustment from program inception is found on the horizontal axis; the percen"
  },
  {
    "figure_id": "F047",
    "report_id": "R003",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "1/ Bars refer to annual projected fiscal adjustment (right-hand side scale) and lines show possible real GDP growth paths under different fiscal multipliers (left-hand side scale). Figure 5. Kyrgyz Republic: Qualification of the Moderate Category, 2026–36 1/"
  },
  {
    "figure_id": "F048",
    "report_id": "R003",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5. Kyrgyz Republic: Qualification of the Moderate Category, 2026–36 1/"
  },
  {
    "figure_id": "F049",
    "report_id": "R003",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5. Kyrgyz Republic: Qualification of the Moderate Category, 2026–36 1/ Sources: Country authorities; and staff estimates and projections. 1/ For the PV debt/GDP and PV debt/exports thresholds, x is 20 percent and y is 40 percent. For debt service/Export"
  },
  {
    "figure_id": "F050",
    "report_id": "R003",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5. Kyrgyz Republic: Qualification of the Moderate Category, 2026–36 1/ Sources: Country authorities; and staff estimates and projections. 1/ For the PV debt/GDP and PV debt/exports thresholds, x is 20 percent and y is 40 percent. For debt service/Export"
  },
  {
    "figure_id": "F051",
    "report_id": "R003",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5. Kyrgyz Republic: Qualification of the Moderate Category, 2026–36 1/ Sources: Country authorities; and staff estimates and projections. 1/ For the PV debt/GDP and PV debt/exports thresholds, x is 20 percent and y is 40 percent. For debt service/Export"
  },
  {
    "figure_id": "F052",
    "report_id": "R003",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Sources: Country authorities; and staff estimates and projections. 1/ For the PV debt/GDP and PV debt/exports thresholds, x is 20 percent and y is 40 percent. For debt service/Exports and debt service/revenue thresholds, x is 12 percent and y is 35 percent. Me"
  },
  {
    "figure_id": "F053",
    "report_id": "R003",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Sources: Country authorities; and staff estimates and projections. 1/ For the PV debt/GDP and PV debt/exports thresholds, x is 20 percent and y is 40 percent. For debt service/Exports and debt service/revenue thresholds, x is 12 percent and y is 35 percent. Me"
  },
  {
    "figure_id": "F054",
    "report_id": "R003",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Sources: Country authorities; and staff estimates and projections. 1/ For the PV debt/GDP and PV debt/exports thresholds, x is 20 percent and y is 40 percent. For debt service/Exports and debt service/revenue thresholds, x is 12 percent and y is 35 percent. Me"
  },
  {
    "figure_id": "F055",
    "report_id": "R003",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "1/ For the PV debt/GDP and PV debt/exports thresholds, x is 20 percent and y is 40 percent. For debt service/Exports and debt service/revenue thresholds, x is 12 percent and y is 35 percent. Median of average projected values over the first five years of the f"
  },
  {
    "figure_id": "F056",
    "report_id": "R003",
    "label": "IMF视觉摘要 1",
    "figure_type": "external_card",
    "context": "IMF｜IMF：吉尔吉斯斯坦三年狂飙后，真正的考验是通胀与改革窗口｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F057",
    "report_id": "R004",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "This study assesses the effective monetary stance in the Kyrgyz Republic amid persistent excess liquidity, rapid household credit growth, and elevated inflation pressures. It constructs a monthly Financial Conditions Index (FCI) that captures liquidity conditi"
  },
  {
    "figure_id": "F058",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "market rates (interbank rate) have stayed well below the policy rate, implying looser effective financing conditions despite a restrictive signal. This wedge weakens transmission and complicates interest-rate calibration amid strong domestic demand. 2. Easy li"
  },
  {
    "figure_id": "F059",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "2. Easy liquidity conditions have fueled rapid credit growth, sustaining demand and price pressures. Following the initial cost-push inflation surge triggered by external shocks in 2020–22, inflation dynamics increasingly reflects domestic demand pressures. Cr"
  },
  {
    "figure_id": "F060",
    "report_id": "R004",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "4. These developments highlight the limitations of using the policy rate alone to assess monetary stance. With a persistent structural liquidity surplus, the NBKR has effectively operated as a net borrower from banks, with no refinancing to banks since 2022, u"
  },
  {
    "figure_id": "F061",
    "report_id": "R004",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Text Figure 4. Composition of Net NBKR Liabilities to Banks (borrowing from banks minus lending to banks, KGS bn) Text Figure 5. NBKR Interest Rate Corridor (in percent) ## Box 1. Why the Policy Rate Loses Traction Under Surplus Liquidity In an interest rate c"
  },
  {
    "figure_id": "F062",
    "report_id": "R004",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "restrictive policy signal was partly offset by liquidity and credit dynamics, leaving overall financing conditions more accommodative than implied by the policy rate alone. Text Figure 7. FCI Decomposition (higher value = tighter financial conditions) 9. Lower"
  },
  {
    "figure_id": "F063",
    "report_id": "R004",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "restrictive policy signal was partly offset by liquidity and credit dynamics, leaving overall financing conditions more accommodative than implied by the policy rate alone. Text Figure 7. FCI Decomposition (higher value = tighter financial conditions) 9. Lower"
  },
  {
    "figure_id": "F064",
    "report_id": "R004",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "9. Lower FCI values – indicating looser financial conditions – are associated with higher subsequent inflation. With headline inflation already above the NBKR's medium-term target range of 5–7 percent, this pattern suggests that inflation persistence reflects "
  },
  {
    "figure_id": "F065",
    "report_id": "R004",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "pricing and borrowing conditions. The FCI therefore provides a useful leading indicator of inflationary pressures and complements the policy rate in assessing the effective monetary stance and near-term inflation risks. ## Real Neutral Rate 10. Rolling Taylor-"
  },
  {
    "figure_id": "F066",
    "report_id": "R004",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "## Real Neutral Rate 10. Rolling Taylor-rule estimates suggest that the current real neutral interest rate is around 2 percent. This estimation focuses on the period after the NBKR introduced its medium-term inflation objective of 5–7 percent and strengthened "
  },
  {
    "figure_id": "F067",
    "report_id": "R004",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "B. Labor Market and the Main Drivers of Informality in Kyrgyz Republic 5. Informality in Kyrgyzstan is a complex phenomenon driven by multiple, interrelated factors. As in many developing and transition economies, low educational attainment is strongly associa"
  },
  {
    "figure_id": "F068",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Note: Excluding 332 thousand workers abroad. 7. The Kyrgyz Republic has a young and growing population, with one of the highest shares of youth in the region (Text Figures 2-3). While this demographic trend represents potential for economic growth, most new en"
  },
  {
    "figure_id": "F069",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "7. The Kyrgyz Republic has a young and growing population, with one of the highest shares of youth in the region (Text Figures 2-3). While this demographic trend represents potential for economic growth, most new entrants to the labor market end up in the info"
  },
  {
    "figure_id": "F070",
    "report_id": "R004",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Text Figure 3. Share of Youth in Working Age Population, 2023. Note: Youth Age is 15-24 years, working age is 15-64. 8. The weak quality of education in Kyrgyz Republic limits human capital development and contributes to high informality in the labor market. A"
  },
  {
    "figure_id": "F071",
    "report_id": "R004",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "9. Many young people in the Kyrgyz Republic still face difficulties when moving from school to higher education and work because of weak learning outcomes. Although NEET rates have declined since 2021 and remain one of the lowest in the CCA region, it is still"
  },
  {
    "figure_id": "F072",
    "report_id": "R004",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "10. Weak education outcomes are also reflected in the Kyrgyz Republic's lower performance on the Human Development Index compared with both CCA and Emerging Europe countries (Text Figure 5). Low human development is strongly associated with high informality, a"
  },
  {
    "figure_id": "F073",
    "report_id": "R004",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "12. The Kyrgyz Republic's labor tax wedge – defined as the difference between the total cost of labor to employers and worker's after-tax earnings – is the lowest in the region (Text Figure 7). It indicates that compared to most neighboring countries, a smalle"
  },
  {
    "figure_id": "F074",
    "report_id": "R004",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "The Kyrgyz tax system is highly fragmented. In addition to the main national taxes—personal income tax, corporate income tax, VAT, excises, and the sales tax—there are numerous special tax regimes, including the patent regime, single tax regime, free economic "
  },
  {
    "figure_id": "F075",
    "report_id": "R004",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "## Box 1. Tax Fragmentation and Compliance Costs in the Kyrgyz Republic (concluded). In addition to fragmentation, the tax system is subject to frequent changes. The adoption of the new Tax Code in 2022 introduced important reforms, including expanded electron"
  },
  {
    "figure_id": "F076",
    "report_id": "R004",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "## Box 1. Tax Fragmentation and Compliance Costs in the Kyrgyz Republic (concluded). In addition to fragmentation, the tax system is subject to frequent changes. The adoption of the new Tax Code in 2022 introduced important reforms, including expanded electron"
  },
  {
    "figure_id": "F077",
    "report_id": "R004",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "automatically expand during economic shocks to stabilize household income and consumption, they are static in the Kyrgyz Republic $^{6}$ . 15. Labor market rigidity is another key factor increasing the incentives for informal work. Based on the World Economic "
  },
  {
    "figure_id": "F078",
    "report_id": "R004",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "informal employment. Weak governance, poor rule of law, low regulatory quality, and high corruption incentivize firms and workers to operate outside the formal sector. The Kyrgyz Republic performs below most of its CCA peers on governance indicators (Text Figu"
  },
  {
    "figure_id": "F079",
    "report_id": "R004",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "(higher value – better governance) Text Figure 10. Rule of Law. (Higher value – better governance) Text Figure 11. Regulatory Quality. (higher value – better governance) Text Figure 12. Control of Corruption."
  },
  {
    "figure_id": "F080",
    "report_id": "R004",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "(Higher value – better governance) Text Figure 11. Regulatory Quality. (higher value – better governance) Text Figure 12. Control of Corruption. (higher value – better governance) ## 17. Low affordability and limited accessibility of financing is important fac"
  },
  {
    "figure_id": "F081",
    "report_id": "R004",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "Text Figure 11. Regulatory Quality. (higher value – better governance) Text Figure 12. Control of Corruption. (higher value – better governance) ## 17. Low affordability and limited accessibility of financing is important factor of informality. Restricted acce"
  },
  {
    "figure_id": "F082",
    "report_id": "R004",
    "label": "Figure 13",
    "figure_type": "source_exhibit",
    "context": "## 17. Low affordability and limited accessibility of financing is important factor of informality. Restricted access to finance discourages business expansion, constrains productivity-enhancing investment, and reduces incentives for firms to formalize, as inf"
  },
  {
    "figure_id": "F083",
    "report_id": "R004",
    "label": "Figure 13",
    "figure_type": "source_exhibit",
    "context": "informality. Restricted access to finance discourages business expansion, constrains productivity-enhancing investment, and reduces incentives for firms to formalize, as informal operations often depend on alternative, non-bank financing arrangements that may "
  },
  {
    "figure_id": "F084",
    "report_id": "R004",
    "label": "Figure 14",
    "figure_type": "source_exhibit",
    "context": "Text Figure 14. Percent of Firms Identifying Access to Finance as a Major or Very Severe Constraint ## C. Discussion and Policy Recommendations $^{8}$ 18. Kyrgyz Republic is prone to informality due to a combination of weak human capital outcomes, institutiona"
  },
  {
    "figure_id": "F085",
    "report_id": "R004",
    "label": "Figure 14",
    "figure_type": "source_exhibit",
    "context": "Text Figure 14. Percent of Firms Identifying Access to Finance as a Major or Very Severe Constraint ## C. Discussion and Policy Recommendations $^{8}$ 18. Kyrgyz Republic is prone to informality due to a combination of weak human capital outcomes, institutiona"
  },
  {
    "figure_id": "F086",
    "report_id": "R004",
    "label": "IMF视觉摘要 1",
    "figure_type": "external_card",
    "context": "IMF｜IMF报告：吉尔吉斯共和国的真实货币政策远比政策利率宽松｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F087",
    "report_id": "R005",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## CONCLUSION 4. In light of the considerations above, the Managing Director does not plan to make a proposal by June 30 of this year. This conclusion is based on Article XVIII, Section 4, which requires that the Managing Director make a proposal only if, in h"
  },
  {
    "figure_id": "F088",
    "report_id": "R005",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "5. This conclusion does not preclude the Managing Director from making a proposal during the Thirteenth Basic Period. In accordance with Article XVIII, Section 4(c), the Managing Director can propose an allocation or cancellation, at her own initiative or at t"
  },
  {
    "figure_id": "F089",
    "report_id": "R005",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Sovereign Issuances, 2005–2025 (In billions of USD) Figure 2. Long-term Perspective of SDR Holdings, 1980–2025 (In percent of) Global Reserves 1/ Global Gross Capital Flows Global Trade 3/ 1/ Including gold."
  },
  {
    "figure_id": "F090",
    "report_id": "R005",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2. Long-term Perspective of SDR Holdings, 1980–2025 (In percent of) Global Reserves 1/ Global Gross Capital Flows Global Trade 3/ 1/ Including gold. 2/ Excluding China. 3/ Goods and services."
  },
  {
    "figure_id": "F091",
    "report_id": "R005",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2. Long-term Perspective of SDR Holdings, 1980–2025 (In percent of) Global Reserves 1/ Global Gross Capital Flows Global Trade 3/ 1/ Including gold. 2/ Excluding China. 3/ Goods and services."
  },
  {
    "figure_id": "F092",
    "report_id": "R005",
    "label": "IMF视觉摘要 1",
    "figure_type": "external_card",
    "context": "IMF｜IMF：SDR新分配的门已经关上，但钥匙还在桌上｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F093",
    "report_id": "R006",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "At the top of the stack is the services layer, comprising functions such as asset management, fraud detection, customer due diligence, and transaction monitoring. In a tokenized environment, the services layer consists of applications such as wallets and excha"
  },
  {
    "figure_id": "F094",
    "report_id": "R006",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## Architecture Design An important related question regarding infrastructure is what architecture will emerge—importantly, will owners of assets recorded on different chains be able to transact in an interoperable fashion? In practice, such transactions might"
  },
  {
    "figure_id": "F095",
    "report_id": "R006",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "The second is the compatible ledger model, relevant to assets being recorded on separate ledgers, with owners having access to both ledgers. For instance, money is on one ledger and bonds on another. An orchestrating entity can then pass transfer instructions "
  },
  {
    "figure_id": "F096",
    "report_id": "R006",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "The first model (A) replicates the traditional relationship between a bank and one of its retail clients, User A. In this case, User A holds a direct claim on the bank and trusts the bank to issue an asset it calls money. The bank has responsibility for the du"
  },
  {
    "figure_id": "F097",
    "report_id": "R006",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Note: The association of each model with announced central bank proposals and concepts is based on our own interpretation. CB = central bank; CBDC = central bank digital currency; Fed = Federal Reserve Board."
  },
  {
    "figure_id": "F098",
    "report_id": "R006",
    "label": "IMF视觉摘要 1",
    "figure_type": "external_card",
    "context": "IMF｜IMF报告：Tokenization正在重塑金融基础设施，但真正的赢家是“兼容者”｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F099",
    "report_id": "R007",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "## Contents 03 The New Economics of Asset Management 13 Distribution Is the New"
  },
  {
    "figure_id": "F100",
    "report_id": "R007",
    "label": "EXHIBIT 1",
    "figure_type": "source_exhibit",
    "context": "This will require asset managers to operate differently. Firms that align with the next sources of capital and adapt how they compete will capture a disproportionate share of future growth. ## EXHIBIT 1 # Market Performance Drove Over 80% of Gross Revenue Grow"
  },
  {
    "figure_id": "F101",
    "report_id": "R007",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "Sources: BCG EXPAND Global Asset Management Market Sizing 2026; BCG analysis. Note: AuM market sizing corresponds to assets sourced from each region and professionally managed in exchange for management fees. It includes captive AuM of insurance groups or pens"
  },
  {
    "figure_id": "F102",
    "report_id": "R007",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "Global AuM has more than tripled and revenue more than doubled over the past 15 years. Yet industry profit margins remain close to 30%, roughly where they stood in 2010. Between 2010 and 2025, revenues grew at 5.1% annually while costs rose slightly faster at "
  },
  {
    "figure_id": "F103",
    "report_id": "R007",
    "label": "Exhibit 4",
    "figure_type": "source_exhibit",
    "context": "The rise of digital-native investors is concentrating flows in a smaller set of platforms that act as gatekeepers to capital. For asset managers, success will depend on being embedded in these ecosystems, with products and capabilities designed for how capital"
  },
  {
    "figure_id": "F104",
    "report_id": "R007",
    "label": "Exhibit 6",
    "figure_type": "source_exhibit",
    "context": "Leading firms embed these changes across the distribution journey. (See Exhibit 6.) AI only delivers if the underlying model is sound. Asset managers need to get the four interlocking pillars of distribution right before deploying it. Layering AI on top of a b"
  },
  {
    "figure_id": "F105",
    "report_id": "R007",
    "label": "Exhibit 7",
    "figure_type": "source_exhibit",
    "context": "Deploy AI and widen the gap. Coverage can extend to clients that were previously uneconomical to serve, while preparation and targeting improve across accounts. Over time, this raises productivity and allows the model to scale more effectively. (See Exhibit 7."
  },
  {
    "figure_id": "F106",
    "report_id": "R007",
    "label": "EXHIBIT 8",
    "figure_type": "source_exhibit",
    "context": "\\- Go deep. Set a top-down ambition, but rewire the business bottom-up. Lasting agentic advantage primarily requires changes to the operating model, talent, and processes that embed AI into how work gets done, not by data and technology alone. Asset managers t"
  },
  {
    "figure_id": "F107",
    "report_id": "R007",
    "label": "波士顿咨询视觉摘要 1",
    "figure_type": "external_card",
    "context": "波士顿咨询｜波士顿咨询：资管行业增长幻觉终结，净流入能力成为唯一护城河｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F108",
    "report_id": "R008",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "As a result, the journey model's impact has plateaued. Personalization must evolve by changing its unit of decision from marketer-orchestrated journeys to agent-orchestrated actions, with AI agents selecting, sequencing, and composing interactions from a modul"
  },
  {
    "figure_id": "F109",
    "report_id": "R008",
    "label": "EXHIBIT 1",
    "figure_type": "source_exhibit",
    "context": "## EXHIBIT 1 AI-Native Marketing Drives More Efficient, More Effective Growth Across the Enterprise Savings from NBA Savings from AI Reduction in campaign cycle time More assets in market"
  },
  {
    "figure_id": "F110",
    "report_id": "R008",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "Savings from AI Reduction in campaign cycle time More assets in market Increase in addressable revenue ## How NBA Is Evolving Each new evolution of NBA is defined by a different unit of decision and a different role for the marketer. Understanding where an org"
  },
  {
    "figure_id": "F111",
    "report_id": "R008",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "Reduction in campaign cycle time More assets in market Increase in addressable revenue ## How NBA Is Evolving Each new evolution of NBA is defined by a different unit of decision and a different role for the marketer. Understanding where an organization sits o"
  },
  {
    "figure_id": "F112",
    "report_id": "R008",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "## How NBA Is Evolving Each new evolution of NBA is defined by a different unit of decision and a different role for the marketer. Understanding where an organization sits on this continuum is the first step toward preparing for what comes next. (See Exhibit 2"
  },
  {
    "figure_id": "F113",
    "report_id": "R008",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "# Four Capabilities of Agent-Native NBA Evolving to agent-native NBA requires building four interconnected capabilities: composable shelf, agent architecture, tools/state management, and learning and optimization. (See Exhibit 3.) These four capabilities const"
  },
  {
    "figure_id": "F114",
    "report_id": "R008",
    "label": "Exhibit 4",
    "figure_type": "source_exhibit",
    "context": "Learning and optimization Experimentation engine that measures every shelf asset and agent decision through causal testing, compounding performance over time ## Inside the Composable Shelf The composable shelf is the modular catalog of offers, creatives, and m"
  },
  {
    "figure_id": "F115",
    "report_id": "R008",
    "label": "EXHIBIT 6",
    "figure_type": "source_exhibit",
    "context": "# Building for Tomorrow's Agent Infrastructure The agent-native architecture does not require or assume a greenfield build. Every component that organizations build today for the second evolution of NBA will map directly to a capability that agents can use in "
  },
  {
    "figure_id": "F116",
    "report_id": "R008",
    "label": "波士顿咨询视觉摘要 1",
    "figure_type": "external_card",
    "context": "波士顿咨询｜波士顿咨询：营销的终极形态，不是“旅程”而是“原子动作”｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F117",
    "report_id": "R009",
    "label": "波士顿咨询视觉摘要 1",
    "figure_type": "external_card",
    "context": "波士顿咨询｜波士顿咨询：BCG：Physical AI的回报周期已从5-7年缩至1-3年，CEO们还在等什么？｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F118",
    "report_id": "R010",
    "label": "波士顿咨询视觉摘要 1",
    "figure_type": "external_card",
    "context": "波士顿咨询｜波士顿咨询：营销战役的终结，不是营销的终结｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F119",
    "report_id": "R011",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "NBA action selection occurs across three layers: propensity and uplift scoring, contextual bandits, and agent-based reasoning. These layers are additive, not alternative. Systems don't necessarily need to graduate from one to the next, however, as each layer h"
  },
  {
    "figure_id": "F120",
    "report_id": "R011",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "These limitations are not bugs. They are inherent to the paradigm. Moving past them requires both a different system architecture and an additional (not alternative) class of decisioning models. ## The Two-Track Architecture The production system that makes La"
  },
  {
    "figure_id": "F121",
    "report_id": "R011",
    "label": "波士顿咨询视觉摘要 1",
    "figure_type": "external_card",
    "context": "波士顿咨询｜波士顿咨询：下一代个性化决策，关键不在算法而在组织架构｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F122",
    "report_id": "R012",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "Commitment to implementation of gen AI, by type of institution, $^{1}$ number Adoption is a priority Interested, but not a clear priority Not a priority McKinsey & Company Gen AI offers financial institutions three highly useful capabilities: concision, meanin"
  },
  {
    "figure_id": "F123",
    "report_id": "R012",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "Adoption is a priority Interested, but not a clear priority Not a priority McKinsey & Company Gen AI offers financial institutions three highly useful capabilities: concision, meaning the ability to summarize large volumes of data into digestible nuggets; cont"
  },
  {
    "figure_id": "F124",
    "report_id": "R012",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "Gen AI offers financial institutions three highly useful capabilities: concision, meaning the ability to summarize large volumes of data into digestible nuggets; content generation; and customer engagement, mainly seen in the use of bots to support relationshi"
  },
  {
    "figure_id": "F125",
    "report_id": "R012",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "When initiating or developing use cases, 47 percent of institutions say the most important factor is the promise of uplifts in productivity, followed closely by business needs and regulatory compliance, cited by 44 percent and 25 percent of respondents, respec"
  },
  {
    "figure_id": "F126",
    "report_id": "R012",
    "label": "Exhibit 4",
    "figure_type": "source_exhibit",
    "context": "Somewhat surprisingly, the group most advanced in deployment is regional banks, which are ahead of megabanks in number of use cases (Exhibit 4). In addition, core regionals are most advanced on ideation and planning. Very few use cases have reached the stage o"
  },
  {
    "figure_id": "F127",
    "report_id": "R012",
    "label": "Exhibit 5",
    "figure_type": "source_exhibit",
    "context": "## McKinsey & Company ## Exhibit 5 Full deployment is rare across use cases. Gen AI use cases in commercial credit and their development stage, $^{1}$ % McKinsey & Company ## Why banks are taking a conservative approach Many senior bankers, especially at regio"
  },
  {
    "figure_id": "F128",
    "report_id": "R012",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "Copyright © 2025 McKinsey & Company. All rights reserved. # How agentic AI can change the way banks fight financial crime Financial institutions are allocating significant resources to fighting financial crime, but they are generally making little progress. AI"
  },
  {
    "figure_id": "F129",
    "report_id": "R012",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "# How agentic AI can change the way banks fight financial crime Financial institutions are allocating significant resources to fighting financial crime, but they are generally making little progress. AI-based solutions may be an accelerator. This article is a "
  },
  {
    "figure_id": "F130",
    "report_id": "R012",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "Generative AI (gen AI) learns from patterns in data sets and uses those learnings to generate original output. In KYC/AML, it can support human investigators across a number of use cases, including onboarding and in-life client reviews, based on analysis of st"
  },
  {
    "figure_id": "F131",
    "report_id": "R012",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "Agentic AI, by contrast, represents a paradigm shift, with banks employing a “workforce” of AI agents (or digital factories) that can collaborate to perform end-to-end tasks autonomously. In this context, humans are only required for exception handling, oversi"
  },
  {
    "figure_id": "F132",
    "report_id": "R012",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "$^{1}$ Generative AI. ## McKinsey & Company Different generative AI use cases are associated with different kinds of risk. McKinsey & Company treatment across groups (for example, by gender and race), privacy concerns from users inputting sensitive information"
  },
  {
    "figure_id": "F133",
    "report_id": "R012",
    "label": "Exhibit 4",
    "figure_type": "source_exhibit",
    "context": "McKinsey & Company Exhibit 4 Generative AI risk can be mitigated at multiple points across a user interaction. Sample HR chatbot interaction with built-in checkpoints to catch potential misfires and allow for fact-checking of its responses. Organizations imple"
  },
  {
    "figure_id": "F134",
    "report_id": "R012",
    "label": "Exhibit 5",
    "figure_type": "source_exhibit",
    "context": "## — Responsible AI guidelines and policies. \\- Responsible AI talent and culture. A commitment to responsible AI can't rest solely in the executive ranks. Instead, it needs to cascade throughout the organization, with accountability, capability building, and "
  },
  {
    "figure_id": "F135",
    "report_id": "R012",
    "label": "麦肯锡视觉摘要 1",
    "figure_type": "external_card",
    "context": "麦肯锡｜麦肯锡：银行对AI的“谨慎”正在变成一种竞争劣势｜用于快速识别该外部报告的核心问题和市场含义。"
  }
]