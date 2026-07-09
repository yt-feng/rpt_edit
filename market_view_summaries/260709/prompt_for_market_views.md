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
  "智库/国际机构": 11
}

报告摘要：
[
  {
    "id": "R001",
    "title": "亚洲开发银行：中国出口韧性背后，亚太区域增长分化加剧",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "亚洲开发银行",
    "digest": "[wechat_article.md]\n# 亚洲开发银行：中国出口韧性背后，亚太区域增长分化加剧\n\n亚洲开发银行在7月发布的《亚洲发展展望》更新中，将2026年亚太发展中地区增长预测从4月的5.1%下调至4.9%，同时将通胀预期从3.0%大幅上修至4.3%。这份报告的核心判断是：中东冲突已演变为现代史上最大规模的石油供应冲击之一，峰值时期日均超过1000万桶的供应中断。更值得关注的不是油价本身，而是冲击的滞后效应——能源成本正在通过供应链、化肥价格和核心通胀缓慢渗透，而这些传导尚未完全体现在宏观环境数据中。\n\n报告将2027年增长预测维持在5.1%，隐含的假设是能源市场能够逐步正常化。但报告同时承认，物理层面的恢复速度可能慢于市场预期：霍尔木兹海峡的排雷、战争险保险费的回归、改道油轮的重新部署，以及长期关井可能造成的油层损害，都会延长恢复周期。液化天然气的恢复可能比原油更慢。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 通胀的传导链条比市场预期的更长\n\n报告提出的一个关键观察是，能源冲击的影响正在从生产者价格向食品和核心通胀扩散。5月，亚太地区除中国以外的通胀率达到7.6%，土耳其的持续高物价和超过半数地区的广泛价格上涨是主要推手。中国5月生产者价格指数升至46个月高点的3.8%，印度批发价格通胀更达到9.7%的43个月峰值。\n\n化肥价格的上涨尤其值得警惕。报告通过国际水稻研究所的全球大米模型模拟了三种情景：如果2026年原油价格分别比基准水平（每桶69美元）上涨25%、50%和75%，南亚和东南亚部分地区的大米产量将分别下降0.4%、1.1%和2.1%。考虑到化肥价格对食品供应的传导通常需要6-12个月，2027年初的食品通胀不确定性可能被当前市场低估。\n\n> **KC评论：** 市场往往关注油价本身的涨跌，但这份报告提醒我们，能源冲击的二次效应——通过化\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n亚洲经济，正被能源冲击重塑\n\n全球能源供应链的余震，正在改写亚洲的增长剧本。\n\n📉 增长预期下调\n某外资投行最新报告将发展中亚洲2026年增速预测从5.1%下调至4.9%。中东冲突引发的能源供应链中断，推高了生产成本，抑制了经济活动。2027年预计回升至5.1%。\n\n1️⃣ 各区域分化明显\n- 东亚靠中国出口韧性和基建投资维持稳定（2026年4.6%）\n- 南亚受油价和运费上涨拖累，下调至6.0%\n- 东南亚小幅下调至4.6%，外部需求转弱\n- 中亚和太平洋地区也面临贸易中断压力\n\n2️⃣ 通胀压力在蔓延\n全球能源冲击推高区域通胀至4.3%（2025年仅3.0%）。更棘手的是，影响已从能源扩散到食品和核心通胀。5月中国PPI创46个月新高（3.8%），印度更达9.7%。\n\n3️⃣ 货币政策两难\n通胀超目标的经济体达10个。央行们正在增长和通胀间走钢丝——印尼、巴基斯坦加息100个基点，菲律宾加50个基点。但哈萨克斯坦反其道降息，因为食品价格在回落。\n\n4️⃣ 出口结构在变\n电子产品撑起Q1出口增长，AI投资热潮是主要推手。但美国关税政策变化增加了不确定性，其他行业出口仍在挣扎。\n\n最值得关注的，是能源冲击的滞\n\n[... middle omitted ...]\n\n6 and $4.5\\%$ in 2027 on the strength of resilient exports and continued infrastructure investment in the People's Republic of China (PRC), despite weak private consumption and rising geopolit\n\n[... middle omitted ...]\n\npublication. Please contact pubsmarketing@adb.org if you have questions or comments with respect to content or permission to use. Corrigenda to ADB publications may be found at http://www.adb.org/publications/corrigenda."
  },
  {
    "id": "R002",
    "title": "国际清算银行：7个司法管辖区GSIB资本要求差异，不是标准而是操作",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "国际清算银行",
    "digest": "[wechat_article.md]\n# 国际清算银行：7个司法管辖区GSIB资本要求差异，不是标准而是操作\n\n全球系统重要性银行（G-SIB）的资本要求，表面看是同一套巴塞尔III框架，实际执行中却像七种不同的语言。国际清算银行资金稳定研究所（FSI）在2026年7月发布的一份报告中，基于29家G-SIB从2014到2025年的手工整理数据，给出了一个关键判断：**不同司法管辖区在资本要求上的差异，其核心来源不是最低标准，而是各国在缓冲、附加要求和监管指引上的“超额”操作**。\n\n这份报告的价值在于，它把资本要求这个高度技术化的话题，还原为一个关于竞争公平性和监管可信度的现实问题。当一家美国银行和一家欧洲银行坐在同一张谈判桌上，它们的资本成本可能相差数个基点，而这与不确定性无关，与监管架构有关。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 资本堆叠层的数量差异，从4层到8层不等\n\n巴塞尔III的资本要求由多个层次构成：最低资本要求、资本保存缓冲、逆周期资本缓冲、G-SIB附加缓冲、系统性不确定性缓冲，以及各司法管辖区特有的附加项。报告发现，在七个主要司法管辖区中，G-SIB的资本堆叠层数从4层到8层不等。\n\n这种差异不是形式上的。报告数据显示，2025年，某些司法管辖区仅“非最低要求”部分（即缓冲和附加项）的贡献，平均高达3个百分点，而另一些地区仅有0.1个百分点。这直接导致核心一级资本（CET1）要求在各司法管辖区平均值从约8%到11%不等，而总资本要求的差距更大，从接近12%到接近17%。\n\n> **KC评论：** 这意味着，判断一家G-SIB的资本充足率是否足够，不能只看其总资本比率数值，而要看其背后的堆叠结构。一家总资本比率15%的银行，如果其堆叠层数少、缓冲要求低，其实际抗不确定性能力可能弱于一家总资本比率13%但堆叠层数多的银行。报告中的图表\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n全球大行资本要求，差距到底在哪\n\n全球大行资本要求差距\n\n不同国家监管差异影响银行竞争力\n\n最近读了一篇BIS的研报，专门对比全球系统重要性银行（G-SIBs）的资本要求，信息量很大，简单拆解下核心逻辑。\n\n1️⃣ 资本要求不是一刀切的\nBasel III设的是最低标准，但各国监管可以往上加码。比如有的国家要求银行用更高质量的资本（CET1）来满足要求，有的则额外加了一堆缓冲和附加要求。2025年数据里，不同国家银行的总资本要求范围从12%到17%不等，差别不小。\n\n2️⃣ 系统重要性越高，要求越严\nG-SIB的附加缓冲从1%到2.5%都有，但有个国家直接加到4.5%，用了一套更激进的算法。这导致不同银行的实际“资本堆栈”组成差异很大——有的只4个组件，有的多达8个。\n\n3️⃣ 风险权重计算也有猫腻\n风险密度（风险加权资产/总资产）在不同国家差异巨大。这不一定是因为资产风险本身不同，更多是因为计算方式——有的允许用内部模型，有的更保守。有意思的是，风险密度低的银行，往往资本要求反而更高，监管似乎在“补偿”测量上的宽松。\n\n4️⃣ 杠杆率要求同样不统一\n除了风险加权资本要求，杠杆率（不按风险加权）也各有各的玩法\n\n[... middle omitted ...]\n\nbers of the Financial Stability Institute (FSI) of the Bank for International Settlements (BIS), often in collaboration with staff from supervisory agencies and central banks. The papers aim t\n\n[... middle omitted ...]\n\ness capital buffer</td></tr><tr><td>SFT</td><td>securities financing transactions</td></tr><tr><td>SyRB</td><td>systemic risk buffer</td></tr><tr><td>T1</td><td>Tier 1</td></tr><tr><td>T2</td><td>Tier 2</td></tr></table>"
  },
  {
    "id": "R003",
    "title": "IMF：铜价支撑难抵油价冲击，智利通胀再破3%目标",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "IMF",
    "digest": "[wechat_article.md]\n# IMF：铜价支撑难抵油价冲击，智利通胀再破3%目标\n\n智利正在经历一场典型的“好消息与坏消息并存”的宏观叙事。2025年GDP增长2.5%，国内非矿业需求强劲，铜价高企为财政提供了缓冲。但进入2026年，中东冲突推高能源价格，通胀再度突破3%目标，增长预期节奏变化至1.8%。这份IMF第四条款磋商报告的核心判断是：智利宏观环境基本面依然稳健，但外部不确定性与内部结构性挑战的叠加，正在考验其政策框架的灵活性与财政纪律的可持续性。对于关注新兴市场宏观环境的读者而言，智利案例提供了一个观察“资源型地区如何在高波动环境中管理预期”的窗口。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 铜价是短期支撑，但油价才是决定通胀路径的关键变量\n\n报告最值得关注的判断，在于对通胀前景的重新定位。智利央行曾成功将通胀引导回目标区间，但2026年5月，受能源价格冲击，CPI已升至3.9%，核心通胀也达到3.2%。IMF预计全年通胀将收于4.2%，高于目标，且要到2027年初才能回归。\n\n这里的核心张力在于：铜价上涨为宏观环境增长和财政收入提供了正面支撑，但油价上涨的成本传导更为直接。报告明确指出，如果油价在更长时间内维持高位，并触发工资和其他价格的第二轮效应，央行必须准备好收紧货币政策。这意味着，智利央行的政策路径将不再单纯由国内需求决定，而是被外部能源成本绑架。\n\n> **KC评论：** 对于关注新兴市场央行政策的读者，智利案例的关键在于“通胀预期是否脱锚”。目前两年期通胀预期仍锚定在3%，这给了央行观察空间。但如果油价持续超预期，央行从“按兵不动”转向“被迫加息”的窗口期可能比市场想象的要短。完整报告中关于油价不同情景下的通胀路径推演，值得细读。\n\n![研报图表 2](assets/xhs_card_02.png)\n\n## 2. 财政整\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n智利经济还能撑多久？IMF最新诊断\n\n智利经济韧性\n\nIMF最新国别评估：铜价托底，油价拖后腿\n\n最近翻到一份IMF对智利的2026年第四条款磋商报告，信息量很大，简单梳理一下核心逻辑。\n\n1️⃣ 经济现状：韧性强，但增速放缓\n- 2025年GDP增长2.5%，主要靠非矿业内需拉动\n- 2026年预计放缓至1.8%，2027年回升到2.6%\n- 铜价高企是主要支撑，但中东冲突推高油价，通胀暂时超标\n\n2️⃣ 财政：目标明确，执行有挑战\n- 政府目标：2030年实现结构平衡，债务/GDP控制在45%以下\n- 2026年中央财政赤字预计2.5%，结构赤字3.1%\n- 关键矛盾：支出压力大，收入表现不佳，需要额外增收节支措施\n\n3️⃣ 货币政策：保持警惕\n- 央行通胀目标制运作良好，但需要防范油价持续高位带来的第二轮通胀效应\n- 建议继续积累国际储备，增强外部缓冲\n\n4️⃣ 结构性改革：核心看点\n- 国家重建计划（NRP）包含减税、放松管制等措施\n- 目标：中期将经济增速提升至4%\n- 劳动市场改革、资本市场监管、女性就业都是重点方向\n\n5️⃣ 金融体系：整体稳健\n- 银行业资本充足率符合Basel标准\n- 房地产\n\n[... middle omitted ...]\n\non with Chile.\n\n\\- The Staff Report prepared by a staff team of the IMF for the Executive Board's consideration on July 6, following discussions that ended on April 29, 2026, with the official\n\n[... middle omitted ...]\n\nthe technical support of the Capital Markets Advisory Council to ensure efficient public-private coordination, aligning with structural benchmarks to mitigate macro-financial risks and foster sustainable domestic growth."
  },
  {
    "id": "R004",
    "title": "IMF：IMF模拟智利养老金改革，指数化规则是财政可持续性的分水岭",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "IMF",
    "digest": "[wechat_article.md]\n# IMF：IMF模拟智利养老金改革，指数化规则是财政可持续性的分水岭\n\n智利2025年通过的综合养老金改革，被市场视为提升替代率的关键一步。但IMF一份基于微观数据的模拟报告揭示了一个容易被忽视的结构性问题：改革的核心组成部分——最低保障养老金（PGU），其当前的设计形式在财政上不可持续。报告的核心判断是，由于PGU的“阶梯式递减”机制在实践中几乎失效，超过九成的退休人员实际领取的是全额补贴，这意味着PGU的财政支出将随老年人口线性增长，而非随养老金储蓄改善而收敛。\n\n这份报告的重要性在于，它把讨论焦点从“改革是否足够”引向“改革的设计细节是否经得起长期推演”。对于关注新兴市场财政可持续性和社保体系改革的读者，这是一个必须仔细审视的案例。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. PGU的“阶梯递减”形同虚设，九成以上退休者拿全额\n\nPGU的设计初衷是通过收入测试实现精准补贴。其机制是：自筹养老金低于下限（约79万智利比索/月）者领取全额；介于上下限之间者，补贴逐步递减；超过上限则完全退出。然而，IMF基于智利社会保障调查（EPS）的微观数据分析显示，2024年96%的65岁以上退休人员的自筹养老金低于这一下限。即便考虑到改革后缴费率的大幅提升，模拟至2050年，仍有超过92%的退休人员处于“全额领取”区间。\n\n这意味着，PGU在实际运行中已退化为一种接近“全民普发”的待遇。其财政成本不再与个人储蓄能力挂钩，而是直接与老年人口规模挂钩。在智利人口快速老龄化的背景下，这一设计将构成持续的财政不确定性。\n\n> **KC评论：** 这里的关键不在于PGU本身的好坏，而在于其“靶向机制”完全失效。对于政策制定者，这提示了一个普遍困境：名义上的“精准补贴”如果门槛设置过高或调整不及时，会迅速变成一项无差别的福利支出。报告中的\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n智利养老金改革：钱从哪里来？\n\n**封面标题：**\n钱从哪里来？\n\n**封面副标题：**\n养老金改革背后的财政账本\n\n---\n\n最近看了一份关于智利2025年养老金改革的研究，核心是讨论一个现实问题：**钱从哪里来，以及怎么花得更聪明。**\n\n1️⃣ **改革动了什么**\n2025年智利通过了一项大改革，核心是大幅提高雇主缴费率（逐步加7个百分点），同时扩大“最低保障养老金”（PGU）的覆盖面。PGU是一项政府掏钱给退休人员的补贴，目标是让更多人退休后能有基本收入。但问题来了——这项补贴的财政成本，占了改革总成本的1/3。\n\n2️⃣ **设计的“小漏洞”**\nPGU本意是按需分配：养老金储蓄少的拿全额，多的逐步减少，到一定上限后取消。但现实是，**96%的退休人员储蓄水平都低于“开始减少”的阈值**（2024年数据）。也就是说，绝大多数人实际拿到的都是全额补贴，根本没有“精准投放”。到2050年，这个比例依然超过92%。\n\n3️⃣ **指数化方式决定成本高低**\n研究模拟了两种挂钩方式：\n- 按CPI通胀调整：PGU支出从GDP的2.2%涨到2.5%（2040年）。\n- 按工资增长调整：成本会再高出0.5个百\n\n[... middle omitted ...]\n\nund\nWashington, D.C.\n\n# CHILE\n\n## SELECTED ISSUES\n\nJune 18, 2026\n\nApproved By\n\nWestern Hemisphere\n\nDepartment\n\nPrepared by Francisco Cabezon (RES), Kazuhiro Hiraki (MCM), and Myrto Oikonomou (\n\n[... middle omitted ...]\n\ninancial Theory and Evidence to Pension Fund Design in Developing Economies,\" in Evaluating the Financial Performance of Pension Funds, edited by Hinz, R., Rudolph, H., Antolin, P. and Yermo. J., pp. 203–242, World Bank."
  },
  {
    "id": "R005",
    "title": "IMF：IMF评估乌干达债务数据，统计口径之外的真实负债被低估",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "IMF",
    "digest": "[wechat_article.md]\n# IMF：IMF评估乌干达债务数据，统计口径之外的真实负债被低估\n\n2025年底，IMF技术援助团完成了一项对乌干达公共部门债务统计（PSDS）的数据质量评估。结果并不令人意外：乌干达的债务数据在准确性和及时性上基本达标，但真正的问题藏在数据边界之外——大量实际负债未被纳入官方统计口径。\n\n这份评估报告的价值，不在于它确认了乌干达当前处于“中等债务困境不确定性”，而在于它揭示了发展中国家债务统计中普遍存在但常被忽略的结构性缺陷：法律框架的授权模糊、统计范围的人为调整、以及跨部门数据协调的深层障碍。对于关注新兴市场债务不确定性的研究者和政策制定者来说，这些发现远比一个评级数字更有参考意义。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 统计口径的边界在哪里，债务不确定性就在哪里\n\n乌干达当前的公共债务统计主要覆盖预算中央政府（BCG）的贷款和债务标的。这看上去很清晰，但问题在于，大量实际存在的政府负债被排除在外。\n\n报告明确指出，非预算单位、地方政府和国有企业的非担保负债，目前仅被报告为BCG的“或有负债”，而非纳入广义公共部门债务。截至2024年6月，仅国内欠款（包括与乌干达银行的透支）就达到14.6万亿乌干达先令。这些数字没有被计入核心债务统计。\n\n更值得关注的是，IMF评估发现乌干达的债务报告目前排除了养老金义务、应付账款、透支、公私合营相关负债和融资租赁等关键负债类别。这意味着，官方公布的债务数字可能低估了政府实际承担的财务义务。对于外部观察者而言，仅凭现有公开数据判断乌干达的债务可持续性，可能得出偏乐观的结论。\n\n> **KC评论：** 这一点对任何研究新兴市场债务的人都是提醒——不能只依赖官方公布的债务/GDP比率。统计口径的宽窄，直接影响你对不确定性的真实判断。完整的债务画像需要包括那些“尚未被确认为债务”\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n乌干达债务数据，值得关注\n\n数据质量大检查\n\n这份IMF报告揭示了什么？\n\n1️⃣ 乌干达债务风险评级中等，但有个隐患\n\n2025年评估显示，乌干达目前债务风险中等。问题在于：债务可持续性分析没有纳入预算外实体和国企的非担保债务。如果把这些都算进去，整体风险评级可能会变。\n\n简单说：现在报的数字可能偏乐观。\n\n2️⃣ 数据口径跟国际标准有差距\n\n目前乌干达的外债/内债是按货币种类划分的，不是按债权人居住地。国际标准要求两者都要报。\n\n更关键的是，大量负债没被计入：养老金义务、国内欠款、透支、PPP相关负债、融资租赁。截至2024年6月，仅国内欠款（含央行透支）就达14.6万亿乌干达先令。\n\n3️⃣ 系统该升级了\n\n债务管理系统还是DMFAS 6版本，升级到7版本后可以覆盖透支、SDR分配、本币存款、国内欠款、贸易信贷这些现在被遗漏的科目。\n\n4️⃣ 数据发布流程可以更透明\n\n用户反映：方法论变更前没被告知；数据有时延迟发布；没有正式的修订政策，早期数据不更新，导致前后难以对比。\n\n5️⃣ 优先建议清单\n\n- 把国内欠款和央行透支先纳入统计，再逐步扩到其他科目\n- 审查所有期票和类似安排（包括预融资），识别出的\n\n[... middle omitted ...]\n\nment recipients, describing the high-level objectives, findings, and recommendations.\n\nABSTRACT: In November–December 2025, an assessment was undertaken of the data quality of the public secto\n\n[... middle omitted ...]\n\nerved; LO = Practice Largely Observed; LNO = Practice Largely Not Observed; NO = Practice Not Observed</td></tr></table>\n\n\\* DQAF August 2024 Public Sector Debt Statistics https://dsbb.imf.org/content/pdfs/dqrs\\_psds.pdf"
  },
  {
    "id": "R006",
    "title": "IMF：发展中国家债务统计困境，乌干达欠款和透支远高于表面数据",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "IMF",
    "digest": "[wechat_article.md]\n# IMF：发展中国家债务统计困境，乌干达欠款和透支远高于表面数据\n\nIMF在2026年6月发布的技术援助报告中，对乌干达公共部门债务统计数据质量进行了全面评估。结论并不意外：数据基本准确、发布及时，但真正值得关注的是那些被排除在官方统计之外的债务——国内欠款、央行透支、国有企业非担保负债，以及尚未被纳入的养老金义务和公私合作项目相关负债。截至2024年6月，仅国内欠款和央行透支两项就达到14.6万亿乌干达先令。这个数字意味着，如果按国际标准重新计算，乌干达的实际公共债务负担可能显著高于官方披露的水平。\n\n这份报告的价值不在于否定现有数据，而在于指出了一个发展中国家普遍面临的结构性困境：债务统计的覆盖边界，往往比政策制定者希望看到的要窄得多。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 统计口径的差异，可能改变债务不确定性评估\n\n乌干达目前被评估为中等债务困境不确定性。债务可持续性分析显示，在基准情景下，多数外部和公共债务指标低于临界值。但IMF团队明确指出，这一评估并未包含预算外实体和国有企业的非担保债务。\n\n问题出在统计口径的错位。乌干达的主要债务指标仅覆盖预算中央政府，而预算外单位、地方政府和国有企业的负债被单独列示在债务公报中，作为“隐性或有负债”处理。按照国际标准——GFSM 2014和PSDSG 2013——这些应当纳入广义公共部门债务统计。\n\n一个具体的案例是SDR的处理。2021年8月SDR分配后，乌干达将部分SDR转换为本币，但在统计中仍将其列为对IMF的外部债务。IMF建议，这笔负债应被记录为财政部与央行之间的国内债务。这种分类调整不只是技术细节，它会直接影响外部债务与国内债务的比例，进而影响债务可持续性分析的结论。\n\n![研报图表 2](assets/xhs_card_02.png)\n\n## 2.\n\n[... middle omitted ...]\n\n、国家水务公司等实体的体量，这一缺口可能相当可观。\n\n第三，统计口径调整的节奏是什么？IMF给出了优先级建议，但乌干达当局在立法和系统升级上的实际推进速度，将决定数据质量改善的时间表。\n\n对于关注非洲主权信用和债务可持续性的研究者、读者和政策制定者，这份报告提供了一个难得的窗口：它不只是一次技术评估，更像一面镜子，照出了发展中国家债务统计中那些“看不见的角落”。完整报告中的用户调查结果、标准化债务表格以及当局的详细回应，值得进一步细读。\n\n[note.md]\n外汇研报拆解：乌干达公共债务数据质量评估\n\n数据背后的逻辑\n\n某外资投行最新技术援助报告，分析了乌干达公共债务统计的质量。结论是：数据整体准确，但透明度有提升空间。\n\n1/ 债务边界问题\n乌干达目前只统计中央政府的债务，地方政府、国企、预算外单位的负债被单独列出。按国际标准，这些都应纳入“公共部门债务”口径。报告指出，仅国内欠款和央行透支就达14.6万亿先令（截至2024年6月），但未被计入主要债务指标。\n\n2/ 分类标准差异\n外部/国内债务按币种划分，而非债权人的居住地。IMF建议两种口径都报。SDR分配后，乌干达把部分SDR换成本币，目前记为对IMF的外债，实际上应算作财政部与央行间的国内债务。\n\n3/ 数据系统短板\n债务管理系统DMFAS 6不支持透支、SDR分配、贸易信贷等新工具，计划升级到7版。同时，财政部和央行两套数据库并行，存在重复记录问题。\n\n4/ 透明度改进方向\n报告建议纳入养老金负债、PPP相关负债、金融租赁等。国内欠款经核实后应加入债务统计。目前债务可持续性分析（DSA）不包括国企无担保负债，可能低估债务风险。\n\n整体来看，统计框架扎实，但与国际标准的差距主要在覆盖范围和分类细节上。\n\n[... middle omitted ...]\n\ne IMF Executive Director for Uganda, to other IMF Executive Directors and members of their staff, as well as to other agencies or instrumentalities of the CD recipient, and upon their request,\n\n[... middle omitted ...]\n\nn nominal value, present value and at cost value.</td></tr><tr><td>DDCP has not changed methodology or sources and hence the statement that users are not informed ahead of these changes is not accurate.</td></tr></table>"
  },
  {
    "id": "R007",
    "title": "IMF：全球通胀停滞在4.7%，美联储降息窗口被技术红利与战争冲击压缩",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "IMF",
    "digest": "[wechat_article.md]\n# IMF：全球通胀停滞在4.7%，美联储降息窗口被技术红利与战争冲击压缩\n\n全球宏观环境增长正在经历一场罕见的“结构性撕裂”。IMF在2026年7月发布的《全球宏观环境展望》更新报告中，将2026年全球增速预测下调至3.0%，2027年回升至3.4%。这个数字本身并不惊人，真正值得关注的是它的构成：中东战争带来的供给冲击，与人工智能驱动的技术正周期，正在以截然相反的方向重塑各国增长轨迹。报告的核心判断是，全球宏观环境已经不再是一个“同涨同跌”的系统，而是分裂为三类地区——能源出口受益者、技术链深度参与者、以及两头不占的“夹心层”。这个分类，比任何总量数字都更能解释未来两年的研究与政策逻辑。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 战争冲击被技术周期对冲，但红利分配极不均匀\n\n报告最引人注目的发现是，全球增长在2026年第一季度表现远超预期。IMF原本预计当季年化增速为2.7%，实际录得3.0%。但“超预期”几乎完全集中在少数几个地区：全球前四大AI硬件净出口地区（韩国、马来西亚、中国台湾、泰国）的平均增速意外高达4.4个百分点，而全球其余国家的平均意外为-0.3个百分点。\n\n韩国的案例尤其典型。尽管高度依赖中东能源进口，韩国一季度增速达到7.5%，是4月预测值1.8%的四倍多。驱动引擎是半导体和AI硬件出口的爆发。中国增速达到8.1%（基于IMF季调估计），同样由高技术制造业和出口拉动，而国内消费仍偏弱。美国2.1%的增速略低于预期，但企业设备与知识产权研究依然强劲。\n\n> **KC评论：** 这张图揭示了2026年最重要的宏观线索——技术周期对增长的拉动，已经大到足以对冲一场区域性战争的谨慎冲击。但前提是，地区必须身处技术价值链内部。对于不在其中的国家，战争的影响几乎是净负的。\n\n![研报图表 2](asset\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n全球经济的“双面剧本”\n\n战争与AI，谁才是主角？\n\n最近翻到投行研报，全球经济的走势像被两股力量拉扯——一边是地缘冲突带来的供给冲击，另一边是AI驱动的技术周期加速。2026年全球增速预计3.0%，2027年回升到3.4%，但背后的故事可比数字精彩。\n\n1/ 战争冲击：没那么可怕？\n中东冲突推高了能源价格，但全球经济比预期“扛打”。原因有三：一是可再生能源占比提升，二是经济体能源强度下降（比几年前更节能），三是库存释放缓解了短期短缺。不过，天然气价格在亚洲涨了50%，欧洲25%，美国只涨了10%——全球市场“分层”明显。\n\n2/ AI是隐藏的“增长加速器”\n技术周期成了最大变量。韩国、马来西亚等AI硬件出口大户，一季度增速超出预期4.4个百分点。韩国依赖中东能源进口，但靠半导体和AI出口逆势增长7.5%（预期只有1.8%）。中国一季度8.1%的增速，也靠高技术制造业和出口拉动。\n\n3/ 通胀：暂时“卡住”了\n全球通胀从2025年的4.1%升到2026年的4.7%，但核心通胀还算稳定。能源涨价推高了短期预期，但长期预期没怎么动。政策利率短期难降，欧洲和美国大概率按兵不动。\n\n4/ 分化是关键词\n赢家：能\n\n[... middle omitted ...]\n\nand-driven momentum in the global technology cycle thanks to advances in artificial intelligence (AI) and its adoption. The impact varies widely based on countries' exposure to the war and pos\n\n[... middle omitted ...]\n\ngures for the current and April 2026 WEO forecasts.  \n2/ Data and forecasts are presented on a fiscal year basis.  \n3/ The Iran forecast is subject to unusually high uncertainty given geopolitical and sanctions dynamics."
  },
  {
    "id": "R008",
    "title": "经合组织：不是焦虑，是内收，经合组织揭示男孩女孩福祉差异的真正原因",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "经合组织",
    "digest": "[wechat_article.md]\n# 经合组织：不是焦虑，是内收，经合组织揭示男孩女孩福祉差异的真正原因\n\n全球青少年福祉正在经历一场无声但深刻的出现变化。经合组织最新发布的政策报告基于跨国数据揭示了一个关键事实：男孩与女孩在社会情绪福祉上的下降路径截然不同，而当前的政策框架往往用同一套方案应对两种本质迥异的问题。\n\n报告的核心判断是：女孩的困境更多表现为内在化——焦虑、身体意象困扰、自伤行为；男孩的困境则更多表现为外在化——学业脱钩、攻击性行为、不确定性偏好上升。两者都指向同一个结论——我们需要为不同性别的青少年设计差异化的支持体系，而不是继续用“一刀切”的方式回应正在扩大的福祉缺口。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 女孩的焦虑是内收的，男孩的不确定性是外放的\n\n数据呈现的性别差异非常清晰。在11至15岁青少年中，女孩报告低生活满意度的概率是男孩的1.65至2.5倍。抑郁不确定性在女孩群体中更为集中，而男孩则更容易被诊断为行为障碍。这种分化不是偶然的——它反映了两种不同的应对模式。\n\n女孩倾向于将不确定性内化。她们更频繁地报告身体意象困扰，对自己外貌的不满程度显著高于同龄男孩。报告特别指出，在几乎所有经合组织国家，女孩对身体的不满比例都高于男孩，且这一差距在社交媒体使用更频繁的群体中进一步扩大。\n\n男孩则更多通过外在行为表达困境。他们参与肢体冲突的比例更高，学业脱钩现象更为普遍。报告引用的数据显示，男孩在学业投入度上的下降幅度大于女孩，且更倾向于回避寻求帮助——这与传统的男性气质规范密切相关。\n\n> **KC评论：** 这不是说男孩比女孩“更健康”或“问题更少”。两者的不确定性类型不同，但结果同样严重。女孩的焦虑更容易被识别，因为她们更愿意表达；男孩的问题往往在行为爆发或学业明显波动时才被注意到，那时干预窗口已经收窄。\n\n![研报图表 2\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n当青春期男孩女孩的幸福感，差距大到值得每个人关注\n\n青春期幸福感差距在拉大\n\nOECD最新研报揭示：11-15岁青少年，女孩低生活满意度的概率是男孩的1.65-2.5倍。\n\n这不是简单的情绪波动，而是系统性的性别差异。\n\n1/ 女孩vs男孩：完全不同的脆弱模式\n- 女孩：内化问题为主。焦虑、抑郁、身体形象困扰、自伤行为显著更高\n- 男孩：外化问题为主。品行障碍、攻击行为、冒险行为更常见，自杀死亡风险更高\n\n2/ 性别规范在悄悄起作用\n社会对\"男孩该怎样\"\"女孩该怎样\"的期待，成了隐形的压力源：\n- 女孩承受更多外貌压力，社交媒体加剧身体不满\n- 男孩被要求\"坚强\"，更难开口求助，更容易学业脱节\n\n3/ 四大环境缺一不可\n家庭、学校、社区、数字空间——每个环境都在塑造青少年的情绪健康。\n报告特别指出：约1/3OECD国家青少年反映与父母沟通困难。\n\n4/ 预防比干预更重要\n低门槛的早期识别和支持体系，能防止小问题变成大问题。\n学校+社区+家庭三方联动，才能形成真正的保护网。\n\n一个值得思考的问题：当我们说\"支持青少年心理健康\"，是否常常忽略了男孩女孩完全不同的需求？\n\n#学习笔记\n\n[source_mineru\n\n[... middle omitted ...]\n\nn the understanding of the drivers of these issues, the ways in which they interact and how they evolve. These papers are prepared by OECD staff, external experts or by outside consultants wor\n\n[... middle omitted ...]\n\ns – such as boys' higher academic disengagement and involvement in physical fighting, and girls' greater body image concerns and vulnerability to online harms – while strengthening protective factors for all adolescents."
  },
  {
    "id": "R009",
    "title": "经合组织：AI技能人才仅占劳动力1%，政策制定者真正该焦虑的不是失业",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "经合组织",
    "digest": "[wechat_article.md]\n# 经合组织：AI技能人才仅占劳动力1%，政策制定者真正该焦虑的不是失业\n\nOECD一份新报告给出了一个反直觉的判断：AI对就业的真正冲击，不是来自自动化，而是来自技能需求的系统性重组。报告追踪了2021至2025年间OECD国家企业AI采用率从约7%跃升至约20%的过程，但更值得关注的发现是——高技能岗位反而是AI暴露度最高的群体，而自动化不确定性最集中的却是中低技能岗位。这意味着，AI时代的赢家与输家，并不按传统“高技能安全、低技能危险”的剧本走。\n\n报告的核心变量是“暴露度”与“自动化不确定性”的分离。这两个概念长期被混用，但OECD用数据证明，它们指向完全不同的职业群。管理者、专业人士、工程师的AI暴露度最高，但他们的工作依赖非程式化的认知与社交技能，自动化不确定性反而较低。而从事常规体力和认知任务的中低技能岗位，自动化不确定性更高，但AI直接暴露度并不突出。\n\n> **KC评论：** 这张图是整份报告最有价值的分析框架。它提醒读者，讨论AI对就业的影响时，首先要区分“被AI增强”和“被AI替代”。前者是白领的现实，后者是蓝领和行政岗位的潜在不确定性。报告里关于O*NET职业数据的交叉分析值得仔细看。\n\n报告进一步指出，到2022至2024年，已有约四分之一的劳动者暴露于生成式AI，这一比例预计将大幅上升。但AI技能人才目前仅占劳动力总量的约1%，供需缺口巨大。这才是政策制定者真正需要焦虑的地方——不是AI消灭了多少工作，而是当AI增强高技能岗位时，中低技能劳动者能否及时补上新的技能组合。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 技能短缺已成为企业采用AI的首要障碍\n\n报告明确将技能短缺列为AI扩散的关键瓶颈。企业调研中，成本、基础设施和熟练工人短缺是中小企业采用AI的三大障碍。大企业和初创公司更有能力跨越\n\n[... middle omitted ...]\n\n的衡量标准。第三，职业转换的微观成本未被量化。从高自动化不确定性岗位转向AI增强型岗位，需要多长时间、多少投入、哪些支持最有效，都需要更细颗粒度的研究。\n\n对于关注产业政策、教育研究和劳动力市场的读者，这份报告提供了一个清晰的诊断框架。AI时代的技能挑战不是“更多人学编程”就能解决的，而是需要政府、企业和教育机构在基础能力、技术技能和软技能三条线上同时推进。真正的政策难点，不在于知道该做什么，而在于如何在资源有限的情况下做出优先级排序。\n\n[note.md]\nAI时代，拼的是这3种能力\n\n**AI时代的生存技能清单**\n\n别只盯着代码，底层逻辑变了\n\n最近读了一份OECD最新研报，讲AI时代到底需要什么技能。结论很清晰：AI不会直接淘汰人，但“不会用AI的人”会被淘汰。\n\n1️⃣ **AI不是替代人，是重新定义工作**\n- 高技能岗位（经理、工程师、医生）反而是AI“暴露度”最高的\n- 但暴露≠被替代，这些岗位依赖的是非重复性认知和社交技能\n- 真正危险的是低技能重复性工作，自动化风险更高\n\n2️⃣ **三种技能缺一不可**\n🔹 **基础能力**：读写算、科学素养——这是数字社会的入场券\n🔹 **ICT技能**：从基础电脑操作到AI编程，都算。但全球有AI工程能力的人只占劳动力的1%\n🔹 **互补技能**：批判性思维、创造力、协作能力——这些反而是AI最难替代的\n\n3️⃣ **政策在做什么？**\n- 韩国“AI+数字30+”项目：培养AI专业人才\n- 德国：补贴企业搞在职培训\n- 爱沙尼亚“AI Leap”：全民AI素养计划\n- 加拿大“AI4Good Lab”：专门培养女性AI人才\n\n💡 **个人能做什么？**\n与其焦虑被替代，不如主动补上“互补技能”这块短板。\n\n[... middle omitted ...]\n\n are supplied by and under the responsibility of the relevant Israeli authorities. The use of such data by the OECD is without prejudice to the status of the Golan Heights, East Jerusalem and \n\n[... middle omitted ...]\n\nven economy. This paper examines how AI is transforming labour markets, shifting skill requirements and the policy responses needed to harness AI's transformative potential while mitigating its social and economic risks."
  },
  {
    "id": "R010",
    "title": "经合组织：波黑资本市场缺的不是资金，是信任和整合",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "经合组织",
    "digest": "[wechat_article.md]\n# 经合组织：波黑资本市场缺的不是资金，是信任和整合\n\n波黑的企业融资结构有一个典型矛盾：银行信贷占资金体系资产超过90%，但国内私人部门信贷占GDP比重从2014年的约60%降至2024年的48%，远低于欧盟平均的76%。与此同时，居民存款却创下新高。经合组织这份政策报告的核心判断是：波黑资本市场的问题不在于资金总量不足，而在于制度碎片化、企业端需求与市场供给之间的结构性错配，以及战后私有化遗留的信任赤字。\n\n报告提出，资本市场发展对波黑不仅是资金部门议题，更是私营部门尤其是中小企业能否获得成长所需长期资金的前提。在欧盟一体化进程中，更深、更规范的市场也是波黑融入欧盟单一市场、吸引研究、维持竞争力的必要条件。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 两个交易所、三个监管框架，市场深度被制度切割稀释\n\n波黑资本市场最突出的结构问题是分裂。萨拉热窝标的交易所和巴尼亚卢卡标的交易所各自运作，2024年两市总市值分别约占实体GDP的22%和30.6%。表面上有565只上市标的，但多数是战后私有化遗留的产物，而非企业主动融资的结果。退市速度持续快于新上市，大量挂牌公司几乎没有交易量。\n\n更值得关注的是，布尔奇科特区计划设立第三家交易所。经合组织的措辞克制但态度明确：在没有强有力的协调与统一规则的前提下，这一举措只会进一步分散本已稀薄的流动性。报告引用西班牙整合交易所基础设施的案例，暗示波黑应当考虑的方向是合并而非增设。\n\n> **KC评论：** 对于读者而言，一个分裂的小市场意味着定价效率低、退出通道窄。报告没有明说，但逻辑指向一个结论：波黑资本市场改革的第一优先级不是新建平台，而是消除制度性的交易成本。\n\n![研报图表 2](assets/xhs_card_02.png)\n\n## 2. 公司债市场有需求，但供给端被结构性\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n银行太强势，企业融资卡在哪\n\n融资瓶颈怎么破\n\n中小企业更需要资本市场\n\n最近读到OECD一份关于波黑资本市场的报告，发现他们的困境其实很有代表性——银行占金融资产90%以上，但企业融资越来越难。\n\n波黑国内信贷占GDP比重从2014年的60%降到2024年的48%，而欧盟平均是76%。与此同时，家庭存款却在创新高——钱没流到实体经济里。\n\n1️⃣ 资本市场碎片化是核心问题\n两个实体各有自己的证券交易所，总共有565只上市股票，但多数是当年私有化遗留产物，真正活跃交易的不多。退市速度比上市快，流动性极差。\n\n2️⃣ 企业债市场也偏科\n发债主体集中在小部分非银行金融机构，规模不大。中小企业想发债？门槛高、流程复杂、券商网络窄。\n\n3️⃣ 老百姓不愿进场\n战后私有化让很多人拿到股票却亏了钱，加上金融素养不够、社保缴费率高（17-18.5% vs OECD平均7.2%），大家对资本市场信任度低。\n\n4️⃣ 风投生态几乎为零\n2024年波黑风投总额仅260万欧元，2025年零记录。天使投资还没起步，而海外160万 diaspora 的资金也没被有效利用。\n\n报告提出的改革方向挺实在：\n- 统一交易所规则，别让第三个交\n\n[... middle omitted ...]\n\nscale. However, capital markets in Bosnia and Herzegovina remain shallow and fragmented, limiting their ability to effectively serve the needs of a modern, growth-oriented private sector. This\n\n[... middle omitted ...]\n\nnisms of concentrating ownership of investment funds in privatized companies in Bosnia-Herzegovina, http://documents1.worldbank.org/curated/en/191911468222561736/pdf/700090ESW0P1100ship0in0PIFs000final.pdf. [26]\n\n## Note"
  },
  {
    "id": "R011",
    "title": "世界贸易组织：世界贸易组织裁决，欧盟对印尼反倾销案汇率计算违规",
    "source_group": "institution",
    "source_label": "智库/国际机构",
    "institution": "世界贸易组织",
    "digest": "[wechat_article.md]\n# 世界贸易组织：世界贸易组织裁决，欧盟对印尼反倾销案汇率计算违规\n\n世界贸易组织专家组近日就印尼诉欧盟脂肪酸反倾销措施一案发布裁决报告。这份超过300页的法律文件在技术细节之外，传递了一个对全球贸易参与者都值得关注的信号：反倾销调查的程序合规性正在被更严格地审视，但挑战调查机关实体裁量的门槛依然很高。印尼在汇率计算和征税幅度上赢了关键一局，却在产业损害认定、程序中止等核心抗辩上全面落败。这起案件不是简单的胜负判定，而是为全球贸易救济规则的执行边界提供了一个新的观察样本。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 汇率计算错误成为欧盟违规的突破口，但影响范围有限\n\n专家组认定，欧盟委员会在计算印尼出口商Musim Mas的倾销幅度时，未能按照《反倾销协定》第2.4.1条的要求使用销售当日的汇率，而是采用了其他汇率基准。这一操作直接导致倾销幅度被高估，进而使最终征收的反倾销税超过了依法应计算的倾销幅度，违反了第9.3条和GATT 1994第6:2条。\n\n这个结论的法律意义大于商业意义。它确认了反倾销调查中汇率计算必须严格遵守“销售当日”原则，不能以操作便利为由进行调整。对于正在或即将接受反倾销调查的出口企业来说，这意味着核查阶段对汇率数据的记录和举证变得至关重要。但也要看到，这只是一个技术性违规，并不否定欧盟发起调查的正当性或产业损害的认定逻辑。欧盟只需在后续程序中修正汇率计算方法，即可恢复合规状态。\n\n> **KC评论：** 汇率争议是反倾销案件中常见的攻防点，但能像本案这样被专家组明确认定为违规的并不多。出口企业应当把汇率数据的完整记录从“合规加分项”升级为“法律防御的必选项”。不过，这个胜利的辐射范围有限——它只影响Musim Mas一家的税率，不会动摇整个案件的基础。\n\n## 2. 产业损害认定的抗辩几乎全面失\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n欧盟对印尼脂肪酸反倾销案，WTO裁决出炉\n\n**WTO裁决：欧盟违规**\n\n欧盟反倾销调查部分违规，印尼未全胜\n\n---\n\n1️⃣ **核心结论**\nWTO裁定欧盟在脂肪酸反倾销案中部分违规——未正确使用汇率计算倾销幅度，导致对印尼Musim Mas公司征收的关税偏高。但印尼的多数主张被驳回。\n\n2️⃣ **欧盟违规点**\n- 汇率计算错误：未按“销售当日汇率”折算，违反《反倾销协定》第2.4.1条\n- 关税超标：基于错误倾销幅度征税，违反第9.3条和GATT第VI:2条\n- 连带违规：上述问题导致欧盟违反第1条\n\n3️⃣ **印尼未胜诉项**\n- 继续调查：欧盟在申请方撤回申请后仍继续调查，不违规\n- 损害分析：印尼称欧盟未恰当评估积极指标，WTO认为欧盟整体分析没问题\n- 其他程序性主张：如正常价值构建、行政程序等，均未获支持\n\n4️⃣ **后续影响**\nWTO建议欧盟调整措施以符合规定。但印尼整体指控成功率低，仅汇率问题获支持。此案显示反倾销诉讼中程序细节（如汇率时点）的杀伤力。\n\n#学习笔记\n\n[source_mineru.md]\nsubstantiate its submission by expl\n\n[... middle omitted ...]\n\nend.\n\n7.6 Indonesia's consequential claims under Article 1 of the Anti-Dumping Agreement and Article VI of the GATT 1994\n\n7.278. Indonesia contends that as a consequence of the substantive vio\n\n[... middle omitted ...]\n\nndonesia under these agreements.\n\n8.4. Pursuant to Article 19.1 of the DSU, we recommend that the European Union bring its measures into conformity with its obligations under the Anti-Dumping Agreement and the GATT 1994."
  },
  {
    "id": "R012",
    "title": "波士顿咨询：D2D的‘韧性溢价’到底值多少钱",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "波士顿咨询",
    "digest": "[wechat_article.md]\n# 波士顿咨询：D2D的‘韧性溢价’到底值多少钱\n\n直连卫星（D2D）正在成为全球通信行业最受关注的技术方向之一。2026年世界移动通信大会上，Starlink高调推出Starlink Mobile，宣称已支持超过1000万活跃用户，并计划在年底前达到2600万。但波士顿咨询（BCG）最新报告给出了一个更冷静的判断：D2D不是“太空5G”，它在物理覆盖、宏观环境模型和监管层面都面临结构性约束，而中东和北非（MENA）地区不同国家将分化出三种截然不同的采用路径。\n\n这份报告的核心价值不在于罗列技术参数，而在于它提供了一个决策框架：当一项技术同时具备“弥补数字鸿沟”“增强通信韧性”和“商业附加服务”三种潜力时，政府和运营商究竟该优先押注哪一个场景？\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 物理天花板比想象中更近：室内覆盖和人口密度是硬伤\n\n报告明确指出，D2D只能提供室外覆盖，而全球50%至90%的移动流量发生在室内。更关键的是容量密度问题。GSMA的测算显示，假设一个拥有15000颗卫星的星座并占用全部移动卫星服务频谱，D2D只能在每平方公里人口密度低于40人的区域提供2Mbps的速率。对比之下，迪拜的人口密度超过每平方公里700人——差距不是一个数量级。\n\n> **KC评论：** 这意味着D2D从一开始就不是为了替代城市5G而设计的。它真正能发挥作用的地方是沙漠、山区、海上和偏远农村。对于已经在城市部署了大量基站的运营商来说，D2D更像是一张“补丁”，而不是升级。\n\n报告还指出，目前全球96%的人口已经被地面移动网络覆盖。T-Mobile的CEO已经承认，其T-Satellite D2D服务的实际付费使用量低于预期，原因很简单——地面网络留下的覆盖盲区远比想象中少。\n\n![研报图表 2](assets/xhs_ca\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n手机直连卫星，是未来还是噱头？\n\n📡 太空信号塔来了\n\n最近某外资投行出了一份关于“手机直连卫星”（D2D）的深度报告，核心逻辑很清晰：它不是5G的替代品，而是一个“补充网络”。\n\n1️⃣ D2D到底是什么？\n简单说，就是普通手机直接连卫星，不需要换设备。Starlink Mobile已经在全球有10M+用户，目标2026年底到26M。重点是——它能覆盖极地、沙漠、海洋这些“信号死角”。\n\n2️⃣ 但它不是“太空5G”\n报告明确指出三大限制：\n- 物理限制：只能室外用，但50%-90%的流量发生在室内\n- 经济限制：卫星寿命5年，成本2-3M美元/颗，用户月费7-10美元，目前定位是“高端补充”\n- 频谱限制：需要和运营商合作或高价买频谱\n\n3️⃣ 对中东北非意味着什么？\n报告把国家分成三类：\n- 网络覆盖差、农村人口多的国家 → D2D可能成为主要连接方式\n- 中等覆盖的国家 → 作为商业补充\n- 海湾国家（如阿联酋） → 只是锦上添花，用于旅游、工业物联网\n\n4️⃣ 政府和企业该怎么做？\n- 政府：快速调整监管框架，让D2D成为韧性基础设施\n- 运营商：主动和D2D公司合作，别被绕开\n\n💡 一句话总结：D\n\n[... middle omitted ...]\n\n applied AI, shaped and wielded by our practitioners, teaming shoulder-to-shoulder with your teams to deliver transformative impact at scale. The result? Stronger returns, transferred capabili\n\n[... middle omitted ...]\n\n(images/997658af186ffeda81ca5d2d4b9d149bbcb6c27e3aadc8cfcf1f1f7b3a2c5acc.jpg)  \nHamza Najmi\nPrincipal\nNajmi.Hamza@bcg.com\n\nAcknowledgments\n\n![](images/ce2f6d0591dd4c8308708abcaf98f687d1a9efdf6dd4f89d9e351ad8ea4d4ccb.jpg)"
  },
  {
    "id": "R013",
    "title": "波士顿咨询：报告揭示，超六成消费者期待AI参与奢侈品购买",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "波士顿咨询",
    "digest": "[wechat_article.md]\n# 波士顿咨询：报告揭示，超六成消费者期待AI参与奢侈品购买\n\n经历了过去几年的波动，全球个人奢侈品市场正在以接近疫情前的增速重新起步。波士顿咨询与Altagamma联合发布的第12期《True-Luxury全球消费者洞察》给出了一个值得关注的判断：市场增长的底层逻辑已经切换——从依赖“渴望型消费者”的扩张，转向由顶级客群和价值观变迁共同支撑的更稳定结构。\n\n这份覆盖11个市场、超过1万名受访者的报告，核心信号是：奢侈品消费正在从“展示身份”转向“自我感受”，而这一转变将深刻重塑品牌的定价策略、沟通方式和AI应用优先级。\n\n---\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 增长引擎已从“渴望型”切换为“顶级客群”，结构更健康但更考验品牌\n\n过去十年，奢侈品的增长故事很大程度上由“渴望型消费者”——那些年支出在2000至5000欧元之间的群体——驱动。但这份报告的数据显示，情况已发生根本性变化。\n\n从2015年到2025年，顶级客群（年奢侈品支出超过2万欧元）在总消费中的占比从14%跃升至24%，而渴望型消费者的份额则在调整。更关键的是，顶级客群对宏观宏观环境周期几乎“免疫”，其消费行为稳定且持续增长。与此同时，渴望型消费者的购买意愿波动剧烈，成为市场不确定性的主要来源。\n\n报告明确指出，市场正从“渴望型驱动”走向“消费群体更平衡”的状态。这意味着，品牌不能再依赖中产阶层的购买力扩张来拉动增长，而必须围绕高净值人群的偏好重构产品组合和服务体系。\n\n> **KC评论：** 这不是一个“消费降级”的故事，而是一个“消费结构分化”的故事。顶级客群在买更多，渴望型在买更少。对品牌来说，关键不再是“如何让更多人买得起”，而是“如何让买得起的人愿意持续买单”。完整报告中对不同层级消费者的支出分布和迁徙路径，值得细看。\n\n---\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n奢侈品市场回暖，消费者变了\n\n市场正在悄悄换血\n\n某外资投行最新发布《True-Luxury全球消费者洞察2026》，跑了1万+消费者调研，覆盖11个市场。结论很明确：奢侈品行业回到增长轨道，但驱动逻辑已经变了。\n\n1/ 谁在花钱？不再是“咬牙买”的人撑场\n\n过去10年，Top Tier客户（年均消费42万欧元）的支出占比从14%涨到24%，且完全不受经济周期影响。而“Aspirational”（中产向上消费）群体一直是市场波动源——经济好时冲进来，不好就撤。\n\n但报告发现，Aspirational的消费意愿正在企稳，不再自由落体。市场从“靠中产撑”变成了“金字塔各层均衡发力”。\n\n2/ 为什么买？炫耀退场，自我感受优先\n\n消费者对“奢侈品”的定义，9年间发生了明显位移。“身份象征”和“归属感”选项权重下降，“自我奖励”“时间”“健康”成为新关键词。\n\n产品本身依然重要——品质、长期价值这些核心指标没变。但“为了让别人看到”的动机，正在被“为了让自己更好”取代。\n\n3/ AI正在成为新变量\n\nAI不是又一个会退潮的科技噱头。报告对比了VR、元宇宙、游戏化等前几年的“创新”，发现多数已降温，但AI正在跨越消费者接受\n\n[... middle omitted ...]\n\n美国\n\n![](images/344d9c77382e6f46772b748658d8196b21ebdd4a9eb891add3a0501d16ecb998.jpg)\n\nQualitative Consumer survey, with 100+ luxury clients interviewed through AI-powered interviews on their\n\n[... middle omitted ...]\n\nages/df83e5f57d997d8ccf01138e76e22ae269aa2862190932e8739a6f67fc963245.jpg)  \nSimone Gentili\nBCG Managing Director & Partner\n\n## Thank you.\n\n![](images/ef3bc1b6bbdf1cb555d362fd9cef56b0928a2f0b68a50a5e8a9f6aa1692ac3a2.jpg)"
  },
  {
    "id": "R014",
    "title": "波士顿咨询：气候韧性最大误判，物理不确定性低的地方，资金更脆弱",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "波士顿咨询",
    "digest": "[wechat_article.md]\n# 波士顿咨询：气候韧性最大误判，物理不确定性低的地方，资金更脆弱\n\n传统的气候韧性战略只盯着物理损失：洪水淹没了几栋楼、飓风刮坏了多少屋顶、干旱毁掉了多少亩农田。波士顿咨询这份2026年7月发布的报告提出了一个更值得产业决策者关注的判断——气候不确定性的真正引爆点，正在从物理世界转移到资金系统。当保险、再保险、市政债券、大宗商品对冲这些“资金减震器”开始失灵，一次区域性的气候事件就可能触发连锁反应，造成比物理损失大得多的资金冲击。\n\n报告的核心信号是：全球气候损失在以非线性方式增长，但吸收和分散这些损失的资金机制却在调整。这不是一个渐进出现变化的问题，而是一个接近临界点的问题。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 再保险和资本市场这两大“不确定性分散器”正在失效\n\n过去二十年，全球自然灾害的保险损失翻了四倍。但同期，再保险资本和巨灾债券相对于这些损失的比例却下降了近三分之二。这意味着保险公司正在承担越来越多原本可以分散出去的不确定性。当一场特大灾害到来时，保险公司自身的偿付能力可能成为下一个引爆点。\n\n> **KC评论：** 这张图值得仔细看。它说明的不是“保险不够用”，而是“分担不确定性的机制在调整”。读者可以追问：如果再保险和巨灾债券都跟不上，下一个不确定性承接方是谁？政府？还是最终落到家庭和企业头上？\n\n报告没有完全展开的是，这种机制性调整对不同行业的影响差异很大。对于房地产、公用事业、农业和物流这类高暴露行业，保险公司调整承保范围或提高保费，会直接改变其成本结构和资产估值。\n\n![研报图表 2](assets/xhs_card_02.png)\n\n## 2. 物理不确定性低的地区，资金脆弱性可能更高\n\n波士顿咨询的分析发现了一个反直觉的现象：在美国，五个接收最多联邦灾害资金的州（如佛罗里达、路易斯安那、\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n气候风险正在改写金融规则\n\n金融韧性，不止物理防御\n\n极端天气的损失，正在通过金融系统连环传导\n\n某外资投行最新研报指出：传统保险、再保险、信用市场等机制，已跟不上气候危机的频率和规模。\n\n1️⃣ 物理韧性 ≠ 全部\n- 过去只盯着洪水、野火风险\n- 现在需要加入“金融压力指标”：保费飙升、拒保率上升、按揭违约趋势\n- 美国5个州拿了80%的防灾资金，但另一批低风险州拒保率已很高——一次灾难就可能引爆金融断层\n\n2️⃣ 金融韧性：减震器在失灵\n- 全球气候损失中，保险只覆盖约40%\n- 再保险和巨灾债的覆盖能力，20年来下降了60%\n- 保险公司自己扛的越来越多\n- 案例：澳大利亚飓风再保险池让高风险区保费降了11%；加勒比海参数保险在飓风后14天赔付9200万美元\n\n3️⃣ 社会韧性：别让普通人扛\n- 保费上涨→按揭违约→地方财政恶化→下一场灾难更难扛\n- 达拉斯联储发现：2022-2023年保费上涨导致近15万笔房贷违约\n- 高风险区保费涨幅是低风险区的3-5倍\n- 不同分摊方式（风险定价 vs 收入定价）对家庭负担差异巨大\n\n4️⃣ 谁该行动\n- 政府：做更全面的风险评估，建立兜底机制\n- 保险公司：创\n\n[... middle omitted ...]\n\npacts of climate events through our financial and social infrastructure—insurance, reinsurance, credit, commodity hedging, municipal and sovereign debt—are struggling to keep up with a world o\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R015",
    "title": "波士顿咨询：AgenticAI的真正瓶颈不是技术，而是智能层",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "波士顿咨询",
    "digest": "[wechat_article.md]\n# 波士顿咨询：AgenticAI的真正瓶颈不是技术，而是智能层\n\n当大多数企业还在争论“该不该用Agent”时，波士顿咨询（BCG）的两位资深合伙人Mark Abraham和Neveen Awad直接给出了一个反直觉的判断：速度第一，增长第二，成本第三。这个顺序决定了谁能真正从Agentic AI中拿到回报。\n\n这不是一份罗列技术趋势的报告。它更像是一份给CTO和CIO的行动手册，核心回答了一个问题：为什么95%的公司还在原地踏步，而5%的先行者已经跑通了从试点到规模化的路径？\n\n答案藏在两个关键变量里：一个是大多数公司忽略的“智能层”，另一个是更棘手的组织惯性。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 数据就绪的旧标准已经失效，真正的护城河是“智能层”\n\n很多企业认为，部署Agentic AI的前提是把数据清洗到完美。BCG的观点恰恰相反：Agent需要的不是完美数据，而是可信数据。更关键的是，数据本身并不构成壁垒。\n\n报告提出了一个核心概念——“智能层”。它不是数据湖，也不是API接口，而是企业将自己独特的业务逻辑、KPI关联、客户微观分群等“生意理论”映射到数据上的那一层。当这个层被构建好，即使是现成的Agent框架也能输出可靠的判断。BCG甚至为此申请了专利，称为EnterpriseIQ。\n\n> **KC评论：** 这意味着，未来企业之间在Agentic AI上的差距，将不再是技术栈的先进程度，而是它们能否清晰、结构化地将内部最佳实践转化为机器可理解的上下文。报告认为，大型公司应该自己拥有这个层，而不是依赖外部模型。这个判断值得所有CIO重新审视自己的数据架构优先级。\n\n![研报图表 2](assets/xhs_card_02.png)\n\n## 2. 架构设计的关键：把核心系统变“笨”，让Agent层变“\n\n[... middle omitted ...]\n\ntranslated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>\n\n[note.md]\n智能体AI落地，别再踩这5个坑\n\n**封面：** 智能体AI实战指南\n**副标题：** CTO/CIO最该知道的5件事\n\nBCG两位专家聊透了智能体AI的落地真相，我提炼了最干的5条：\n\n1️⃣ **速度优先于成本**\n别只盯着降本。真正领先的公司用智能体AI让营销速度翻3倍，ROI翻3倍，总成本还能降15-20%。顺序是：速度→增长→成本。\n\n2️⃣ **复杂场景才是主场**\n简单规则流程不需要智能体。它最值钱的地方在多方信息交换、需要判断的复杂场景。比如采购：自动谈判、发起对话，人类只负责最后拍板。\n\n3️⃣ **数据要诚实不要完美**\n智能体不是生成建议，是直接行动。数据错了全盘皆输。关键是“诚实数据”——你信得过的数据。先在小范围验证推理能力，再逐步扩展。\n\n4️⃣ **构建“智能层”**\n这是最被低估的部分。把公司业务逻辑（KPI怎么关联、用户怎么细分）映射到数据上，智能体才能真正理解业务。这个层独立于模型，未来换模型不用重做。\n\n5️⃣ **分阶段放权**\n影子模式→监督模式→引导自主→完全自主。每升一级都要用实际表现说话。每次升级模型都要重新评估，因为智能体行为可能变。\n\n**最有价值的提醒：*\n\n[... middle omitted ...]\n\nion about agentic AI: where to deploy agents, how autonomous they should be, and what's real versus hype. Second, business unit leaders want to address cost pressures. They are looking at agen\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R016",
    "title": "波士顿咨询：医生不是成本难题，而是医院控费真正引擎，波士顿咨询",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "波士顿咨询",
    "digest": "[wechat_article.md]\n# 波士顿咨询：医生不是成本难题，而是医院控费真正引擎，波士顿咨询\n\n医院管理者习惯将成本控制的焦点放在行政开支、非临床人员薪酬和可自由支配的运营费用上。波士顿咨询最新报告指出，这些努力方向虽然直观，却往往绕过了真正的大头——临床驱动的采购支出，尤其是医生偏好类物品，如外科植入物和生物制剂。\n\n这份报告的核心判断是：医院最大的成本改善空间不在财务办公室，而在手术室和临床科室。但绝大多数机构并未触及这一领域，不是因为价值不存在，而是因为改变临床行为极其困难。波士顿咨询基于其与多家医疗系统的合作经验，提出了一条被证明有效的路径：将成本管理重新定义为临床优先事项，并在整个过程中嵌入医生的持续参与。\n\n> **KC评论：** 这份报告的价值不在于告诉管理者“要省钱”，而在于指出“为什么过去省不下来”。许多医院在采购环节反复谈判却收效甚微，根源在于医生没有被真正纳入决策过程。当医生在方案成型后才被通知，他们自然把成本倡议视为行政指令而非临床共识。完整报告中包含一个关键案例对比，展示了同一个支出类别，在传统采购模式下与医生主导变革模式下，节约效果的天壤之别。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 临床采购中最大的成本陷阱，是“默认已经拿到了最优价”\n\n第三方支出通常占医院运营总费用的30%至40%。其中相当比例与临床实践模式、历史供应商关系和科室习惯深度绑定。波士顿咨询观察到，许多机构对这部分支出存在三个误判：一是认为最佳价格已经谈妥；二是与供应商的关系根深蒂固，难以撼动；三是缺乏早期且持续的医生参与。\n\n结果就是，成本改善努力沦为采购部门主导的零散招标，每年只能挤出边际收益。真正的结构性改善从未发生。报告明确指出，问题不在于识别机会，而在于建立抓住机会的组织能力。\n\n![研报图表 2](assets/xhs_card_02\n\n[... middle omitted ...]\n\n场景下的适用边界\n\n波士顿咨询的分析基于美国医疗系统，其医生关系、支付体系和医院治理结构与国内有显著差异。报告没有讨论的核心问题是：当医生薪酬结构不同、医院采购决策链条更长、供应商关系更复杂时，医生主导的成本变革是否依然有效？中国公立医院在耗材集采政策下，供应商议价空间已被大幅压缩，此时医生的角色更多转向“合理使用”而非“价格谈判”，波士顿咨询的方法论需要做哪些本地化调整？\n\n这些问题报告没有展开，但恰恰是国内读者需要自己思考的下一步。\n\n[note.md]\n医生才是控费的关键变量\n\n医生主导，成本自然降\n\n以前总觉得控费是采购的事，看完这篇研报才发现，真正的成本大头藏在医生手里，而且越早让医生参与，效果越好。\n\n1/ 为什么医生是关键？\n- 医院30%-40%的开销来自第三方采购（手术耗材、生物制剂等）\n- 这些领域长期被忽视，原因有三：以为已经拿到最低价、供应商关系固化、医生参与太晚\n- 传统做法：采购部门单干，效果有限\n\n2/ 怎么让医生真正参与？\n- 不是开会通知，而是从定原则开始：临床效果优先、差异化产品保留、等效产品才整合\n- 找医生领袖当“代言人”，比行政命令管用10倍\n- 给医生看真实数据：供应商报价对比、采购规模、医院财务现状\n- 定期开医生专属讨论会，不是走过场\n\n3/ 效果有多明显？\n- 之前同样品类控费只省了毛毛雨\n- 医生全程参与后：供应商态度大变，节约显著，临床质量没降\n- 更关键的是：建立了可复制的模式，下次直接套用\n\n4/ 底层逻辑\n- 成本管理不是采购问题，是临床战略问题\n- 省下来的钱不是利润，是再投资的能力（新技术、新项目、患者体验）\n- 医生不是阻力，是最大杠杆\n\n一个真实案例：某医院用RFP流程做耗材采购，不是单纯比价，而\n\n[... middle omitted ...]\n\noverhead, nonclinical labor, and discretionary operating expenses. Yet some of the largest opportunities are often found elsewhere, in clinically sensitive domains. They are not pursued becaus\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R017",
    "title": "麦肯锡：AI时代银行不能只等对手出局，客户正绕过银行完成资金服务",
    "source_group": "consulting",
    "source_label": "战略咨询",
    "institution": "麦肯锡",
    "digest": "[wechat_article.md]\n# 麦肯锡：AI时代银行不能只等对手出局，客户正绕过银行完成资金服务\n\n2025年全球银行业净利润达到1.3万亿美元，同比增长7%，再次成为所有行业中盈利最高的板块。但这份麦肯锡《2026全球银行业年度报告》的核心判断并不在此：银行业的市场定价（P/B和P/E）依然是所有行业中最低的，读者享受了短期回报，却并未押注长期增长。报告认为，银行面临的真正挑战不是利润增速，而是“客户关系”这一核心资产正在被四股力量同时侵蚀，而银行过去赖以自保的“等对手出局”策略，在AI时代已不再有效。\n\n这份报告是麦肯锡资金服务团队的最新成果，由Klaus Dallerup、Miklós Dietz、Pradip Patiath和Vik Sohoni领衔撰写。以下是我们提炼的三个核心观察。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 利润新高背后，银行赚钱的方式正在不可逆地改变\n\n2025年全球资金系统管理的资金规模达到468万亿美元，但银行资产负债表上的份额从2022年的44%降至40%。这意味着银行越来越不靠“存贷差”赚钱，而是靠交易银行和分销业务——这两项业务现在贡献了47%的收入和57%的利润。\n\n> **KC评论：** 资产负债表不再是银行的护城河。当收入和利润更多来自手续费和交易服务时，竞争门槛大幅降低，新进入者（尤其是fintech）的攻击面也更大。报告里那张“全球收入利润率从0.97降至0.94”的图表值得细看，它暗示银行必须在成本端更激进。\n\n区域模型的分化也在加速。北BofA行受益于财富管理流入，ROE达到12%；欧洲银行通过运营改善将ROE从10.7%提升至11.6%。但最值得注意的是，麦肯锡绘制了一张“新世界银行地图”，发现瑞典和芬兰的银行在“脱离资产负债表”和“成本效率”两个维度上同时做到了最优，为全球同行提供了可参照的\n\n[... middle omitted ...]\n\n本调整——更高的失败率、更大的不确定性、新的绩效预期。但这是银行“在技术变革和客户争夺战中保持相关性”的唯一路径。对最传统的银行和中小型机构来说，这反而是一个历史性机会：AI和数字资产允许后来者实现跨越式竞争。\n\n**报告尚未完全回答的关键问题：** 银行如何在维持监管合规的同时，真正实现“三速”运转？目前多数银行的多速架构在激励机制和治理上仍不清晰。另外，地缘政治摩擦对银行资产负债表和跨境业务的长期影响，报告仅点到为止，值得持续跟踪。\n\n[note.md]\n2025全球银行利润新高，但隐忧在哪？\n\n银行利润新高背后\n\n2025年全球银行业净利润达1.3万亿美元，同比增7%，再次成为最赚钱行业。但资本市场并不买账——银行股P/B和P/E仍垫底所有行业，投资者对长期增长存疑。\n\n1/ 区域模式大分化\n北美靠财富管理拉动ROE至12%，欧洲靠运营改善从10.7%升至11.6%。但拉BofA行净息差从3.55%骤降至2.93%，新兴市场压力不小。\n\n2/ 客户正在流失\n成熟金融科技已拿下17%行业收入，Revolut、Nubank等挑战者正改写游戏规则。AI采用速度史上最快，老中青用户几乎同步迁移，银行以往靠“老客户慢转移”的优势失效。\n\n3/ 收入结构在变\n银行表内资产占比从44%降至40%，交易银行和分销贡献47%收入和57%利润。这意味着竞争更激烈，传统息差模式正在被颠覆。\n\n4/ 三速组织成关键\n某外资投行建议银行建立“三速组织”：基础业务维持合规速度，创新业务加速试错，前沿探索用科技速度在监管边界外孵化。AI不会等人，速度就是护城河。\n\n银行不缺现金，但缺重新定义自己的勇气。你觉得传统银行最该先改哪块业务？\n\n#学习笔记\n\n[source_mineru.md]\n!\n\n[... middle omitted ...]\n\nSohoni, with Valeria Laszlo, representing views from McKinsey's Financial Services Practice.\n\nIn 2025, the global banking industry outdid itself—again. Net income rose to \\$1.3 trillion, up 7 \n\n[... middle omitted ...]\n\neir contributions to this report.\n\nThis report was edited by Mark Staples, an editorial director in the New York office.\n\n![](images/7cb34647a0e08ebfe18bf6231d8451531f90237718d8bc32383074c533eff9fb.jpg)\n\nwww.mckinsey.com"
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Growth dynamics varied substantially across the region's largest economies in the first quarter (Q1) of 2026. Growth remained resilient in Q1, buoyed by solid pre-conflict activity and strong domestic demand, even as momentum varied across economies. In the PR"
  },
  {
    "figure_id": "F002",
    "report_id": "R001",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Global commodity price increases are lifting inflation across developing Asia and the Pacific, as energy costs gradually spill over into food and core inflation. Energy-related Food Core Headline, % B. DAP Excluding the PRC C. DAP Excluding the PRC and Türkiye"
  },
  {
    "figure_id": "F003",
    "report_id": "R001",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "B. DAP Excluding the PRC C. DAP Excluding the PRC and Türkiye Percentage points, year on year elevated borrowing costs. Net exports contributed less than in previous quarters as rising imports of capital goods and components weighed on external balances, as di"
  },
  {
    "figure_id": "F004",
    "report_id": "R001",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## Figure 2 Contributions to GDP Growth A. Demand-Side Growth momentum remained firm in Q1 2026, largely reflecting solid pre-conflict activity and robust domestic demand. ## B. Supply-Side Percentage points, year on year"
  },
  {
    "figure_id": "F005",
    "report_id": "R001",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "## B. Supply-Side Percentage points, year on year DAP = developing Asia and the Pacific, GDP = gross domestic product, H = half, PRC = People's Republic of China, Q = quarter. Sources: Asian Development Bank estimates using data from Haver Analytics, CEIC Data"
  },
  {
    "figure_id": "F006",
    "report_id": "R001",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "## B. Supply-Side Percentage points, year on year DAP = developing Asia and the Pacific, GDP = gross domestic product, H = half, PRC = People's Republic of China, Q = quarter. Sources: Asian Development Bank estimates using data from Haver Analytics, CEIC Data"
  },
  {
    "figure_id": "F007",
    "report_id": "R001",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Percentage points, year on year DAP = developing Asia and the Pacific, GDP = gross domestic product, H = half, PRC = People's Republic of China, Q = quarter. Sources: Asian Development Bank estimates using data from Haver Analytics, CEIC Data Company, and offi"
  },
  {
    "figure_id": "F008",
    "report_id": "R001",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "performance across the region, albeit to varying degrees. Delivery times lengthened in all economies apart from India, where precautionary stockpiling also increased. In services, PMIs point to strengthening activity, supported by AI-driven demand in the PRC, "
  },
  {
    "figure_id": "F009",
    "report_id": "R001",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "New orders index Stocks of purchases index Suppliers' delivery times Employment index Output index Headline PMI target ranges in early 2026 in Armenia, Georgia, Mongolia, Nepal, Pakistan, the Philippines, and Viet Nam, and remained above target. In response, m"
  },
  {
    "figure_id": "F010",
    "report_id": "R001",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4 Purchasing Managers' Index, Selected DAP Economies PMI readings in May signal firmer manufacturing activity, though conditions remain uneven across economies. B. Breakdown of Manufacturing PMI, by Components, May 2026 Distance from the 50-point thresh"
  },
  {
    "figure_id": "F011",
    "report_id": "R001",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Despite a more cautious policy stance, real monetary conditions have loosened across many economies this year, while policy-rate expectations have moved higher. In most regional economies, upward revisions to 2026 inflation expectations have more than offset m"
  },
  {
    "figure_id": "F012",
    "report_id": "R001",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "ADO = Asian Development Outlook, ARM = Armenia, AZE = Azerbaijan, BAN = Bangladesh, DAP = developing Asia and the Pacific, GEO = Georgia, IND = India, INO = Indonesia, KAZ = Kazakhstan, KGZ = Kyrgyz Republic, LAO = Lao People's Democratic Republic, MAL = Malay"
  },
  {
    "figure_id": "F013",
    "report_id": "R001",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "AAP = advanced Asia and the Pacific, DAP = developing Asia and the Pacific, PRC = People's Republic of China, ROK = Republic of Korea. Notes: Revisions are changes in consensus forecasts for policy rates from April to May 2026. Positive values indicate upward "
  },
  {
    "figure_id": "F014",
    "report_id": "R001",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "By contrast, the 2026 growth forecast for AAP is raised by 0.4 percentage points (pps) to $2.6\\%$ , on stronger-than-expected AI-driven demand for semiconductors. The upgrade reflects higher growth projections for Hong Kong, China by 0.4 pps; the Republic of K"
  },
  {
    "figure_id": "F015",
    "report_id": "R001",
    "label": "figure 1",
    "figure_type": "source_exhibit",
    "context": "The conflict that began on 28 February 2026 triggered an unprecedented shock to global oil supply (IEA 2026a). The disruption stemmed from severe restrictions on shipping through the Strait of Hormuz, a critical chokepoint that normally carries about 25% of gl"
  },
  {
    "figure_id": "F016",
    "report_id": "R001",
    "label": "figure 3",
    "figure_type": "source_exhibit",
    "context": "Oil supply losses during the 2026 Middle East conflict surpassed those observed during earlier major oil crises. Sources: IEA. 2007. Oil Supply Security; Escribano, G. 2011. The International Energy Agency Responds to the Libyan Crisis; Mearns, E. 2014. The Ar"
  },
  {
    "figure_id": "F017",
    "report_id": "R001",
    "label": "figure 4",
    "figure_type": "source_exhibit",
    "context": "Market expectations also helped contain price pressures. While spot prices surged as refiners competed for immediate supplies, longer-dated futures rose by far less. Through April and May, Brent spot prices remained above \\$100/barrel, yet futures contracts fo"
  },
  {
    "figure_id": "F018",
    "report_id": "R001",
    "label": "figure 1",
    "figure_type": "source_exhibit",
    "context": "Supply chain disruptions from the conflict in the Middle East have added to inflation in developing Asia and the Pacific (DAP). The most immediate effects from the conflict have been felt through higher energy import prices, which, given the region's heavy rel"
  },
  {
    "figure_id": "F019",
    "report_id": "R001",
    "label": "figure 3",
    "figure_type": "source_exhibit",
    "context": "Note: The Baltic Dirty Tanker Index measures freight rates for unrefined petroleum products such as crude oil, while the Baltic Clean Tanker Index measures freight rates for refined petroleum products such as gasoline, diesel, jet fuel, and naphtha. The Baltic"
  },
  {
    "figure_id": "F020",
    "report_id": "R001",
    "label": "figure 3",
    "figure_type": "source_exhibit",
    "context": "surveys shows that global delivery times lengthened from February to April and remained elevated in May (box figure 3). Similarly, the Global Supply Chain Stress Index, which measures stalled shipping capacity across major maritime routes, has risen by about 1"
  },
  {
    "figure_id": "F021",
    "report_id": "R001",
    "label": "figure 4",
    "figure_type": "source_exhibit",
    "context": "Sources: Haver Analytics; Arvis J. et al. 2026. A Metric of Global Maritime Supply Chain Disruptions: The Global Supply Chain Stress Index (GSCSI). World Bank. Supply chain friction and precautionary stockpiling have induced shortages of raw materials and inte"
  },
  {
    "figure_id": "F022",
    "report_id": "R001",
    "label": "figure 1",
    "figure_type": "source_exhibit",
    "context": "The region remains disproportionately exposed to elevated US tariffs. The effective tariff rate for developing Asia and the Pacific (DAP) stands at 24.8%, nearly double the rate before the April 2025 tariff announcements (box figure 1). By subregion, developin"
  },
  {
    "figure_id": "F023",
    "report_id": "R001",
    "label": "figure 1",
    "figure_type": "source_exhibit",
    "context": "Rising fuel costs could place substantial fiscal burdens on governments in developing Asia and the Pacific (DAP). Measures such as energy price caps or fuel subsidies offer immediate relief to households and firms, but they tend to be regressive and fiscally c"
  },
  {
    "figure_id": "F024",
    "report_id": "R001",
    "label": "figure 1",
    "figure_type": "source_exhibit",
    "context": "## Box 6 Higher Energy and Fertilizer Costs Threaten Food Security Energy market disruptions have driven up fertilizer costs through several channels. Modern agriculture depends heavily on fertilizers derived from fossil fuels, which have boosted productivity "
  },
  {
    "figure_id": "F025",
    "report_id": "R001",
    "label": "figure 2",
    "figure_type": "source_exhibit",
    "context": "In developing Asia and the Pacific, low fertilizer self-sufficiency leaves several economies vulnerable to price volatility and supply chain disruptions. Several major crop-producing economies in the region remain dependent on fertilizer imports, including key"
  },
  {
    "figure_id": "F026",
    "report_id": "R001",
    "label": "亚洲开发银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "亚洲开发银行｜亚洲开发银行：中国出口韧性背后，亚太区域增长分化加剧｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F027",
    "report_id": "R002",
    "label": "国际清算银行视觉摘要 1",
    "figure_type": "external_card",
    "context": "国际清算银行｜国际清算银行：7个司法管辖区GSIB资本要求差异，不是标准而是操作｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F028",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "X. Data Issues \\_\\_\\_\\_ 71 ## CONTEXT 1. Amid heightened global uncertainty, the Chilean economy remains resilient as it confronts long-term challenges. Domestic demand has picked up, export growth is robust, and the current oil price shock is thus far managea"
  },
  {
    "figure_id": "F029",
    "report_id": "R003",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Sources: Haver and IMF staff calculations. ## 4. Labor market slack persists. The seasonally adjusted unemployment rate has fluctuated 19 average of around 7 percent. Recently, employment growth in the formal sector has lagged that in the informal sector, with"
  },
  {
    "figure_id": "F030",
    "report_id": "R003",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "19 average of around 7 percent. Recently, employment growth in the formal sector has lagged that in the informal sector, with female unemployment rising more than male. The slack reflects, inter alia, sizable minimum wage hikes and other regulatory changes (su"
  },
  {
    "figure_id": "F031",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "6. At 2.8 percent of GDP, the headline fiscal deficit in 2025 was broadly similar to that in 2024, though 1.8 percentage points higher than budgeted. Revenue underperformance was the key driver, as higher mining-related revenue did not fully offset weaker-than"
  },
  {
    "figure_id": "F032",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "6. At 2.8 percent of GDP, the headline fiscal deficit in 2025 was broadly similar to that in 2024, though 1.8 percentage points higher than budgeted. Revenue underperformance was the key driver, as higher mining-related revenue did not fully offset weaker-than"
  },
  {
    "figure_id": "F033",
    "report_id": "R003",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "25. The central bank remains committed to its mandate. The BCCh underscored that its future monetary policy decisions would be made on a meeting-by-meeting basis, recognizing the high uncertainty around the war in the Middle East that has unfolded more adverse"
  },
  {
    "figure_id": "F034",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "48. Staff recommends that the next Article IV consultation take place on the standard 12-month cycle. Exports and Imports of Goods and Services (S.A. - 2019Q3=100) ## Figure 1. Chile: Economic Activity Growth has moderated since the second half of 2025... Weak"
  },
  {
    "figure_id": "F035",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## Figure 1. Chile: Economic Activity Growth has moderated since the second half of 2025... Weaker exports largely reflect a decline in mining activity following an accident in July 2025... ... mostly driven by smaller contributions from net exports. ...while "
  },
  {
    "figure_id": "F036",
    "report_id": "R003",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "GDP Growth Composition (In percent of GDP) Real Gross Fixed Capital Formation (Index, 2019Q4 = 100) ... and still-robust consumption growth. Business confidence improved through 2025 and early 2026 but has softened since the Middle East conflict. Sources: Cent"
  },
  {
    "figure_id": "F037",
    "report_id": "R003",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Real Gross Fixed Capital Formation (Index, 2019Q4 = 100) ... and still-robust consumption growth. Business confidence improved through 2025 and early 2026 but has softened since the Middle East conflict. Sources: Central Bank of Chile, Ministry of Finance, INE"
  },
  {
    "figure_id": "F038",
    "report_id": "R003",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Business confidence improved through 2025 and early 2026 but has softened since the Middle East conflict. Sources: Central Bank of Chile, Ministry of Finance, INE, Haver Analytics, and IMF staff calculations. ## Figure 2. Chile: External Sector The current acc"
  },
  {
    "figure_id": "F039",
    "report_id": "R003",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Chile: Exchange Rate and Copper Price (CLP/USD - LHS; USD per pound - RHS) Gross international reserves increased in 2025 but are below 100% of the ARA metric. Gross Reserves and Reserve Adequacy Metric 1/ (In billions of U.S. dollars) FX buffers held by the g"
  },
  {
    "figure_id": "F040",
    "report_id": "R003",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Gross international reserves increased in 2025 but are below 100% of the ARA metric. Gross Reserves and Reserve Adequacy Metric 1/ (In billions of U.S. dollars) FX buffers held by the government (not counted as international reserves) have stabilized at a low "
  },
  {
    "figure_id": "F041",
    "report_id": "R003",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "FX buffers held by the government (not counted as international reserves) have stabilized at a low level. Government Liquid FX Assets (In billions of U.S. dollars) Sources: Central Bank of Chile, DIPRES, Haver Analytics, and IMF staff calculations. 1/ As perce"
  },
  {
    "figure_id": "F042",
    "report_id": "R003",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Sources: Central Bank of Chile, DIPRES, Haver Analytics, and IMF staff calculations. 1/ As percent of the IMF reserve adequacy metric. See Assessing Reserve Adequacy, IMF. Figure 3. Chile: Inflation 1/ After briefly falling below target, headline inflation has"
  },
  {
    "figure_id": "F043",
    "report_id": "R003",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Figure 3. Chile: Inflation 1/ After briefly falling below target, headline inflation has picked up following the conflict in the Middle East. Prior to the war, disinflation was led by tradable prices, reflecting falling import prices, and peso appreciation... "
  },
  {
    "figure_id": "F044",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "The rise in inflation since March is driven by fuel and transportation prices, with limited second-round effects. Two-year inflation expectations remain close to the target. Inflation Expectations at 1 and 2 Years (In percent) Sources: Central Bank of Chile, H"
  },
  {
    "figure_id": "F045",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "2/ LA7 group includes seven Latin American countries: Brazil, Chile, Colombia, Mexico, Paraguay, Peru, and Uruguay. Average LA inflation is calculated as the PPP-GDP-weighted average inflation rate across these countries. The fiscal deficit was unchanged in 20"
  },
  {
    "figure_id": "F046",
    "report_id": "R003",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Fiscal Balance, Expenditure and Revenue ## Figure 4. Chile: Public Finances Capital spending execution increased somewhat in 2025 but remained below pre-pandemic levels. ... which is linked to the persistently low non-mining tax revenue-to-GDP ratio. Chile's g"
  },
  {
    "figure_id": "F047",
    "report_id": "R003",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Capital Spending Execution (Percent of budgeted amount) General Government Gross Debt 1/ (In percent of GDP) ...the government continues to borrow at favorable rates, EMBI Spreads (Basis points) ... while Treasury assets have not recovered. Sources: Ministry o"
  },
  {
    "figure_id": "F048",
    "report_id": "R003",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "General Government Gross Debt 1/ (In percent of GDP) ...the government continues to borrow at favorable rates, EMBI Spreads (Basis points) ... while Treasury assets have not recovered. Sources: Ministry of Finance, Dipres, Central Bank of Chile, Bloomberg, and"
  },
  {
    "figure_id": "F049",
    "report_id": "R003",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Sources: Ministry of Finance, Dipres, Central Bank of Chile, Bloomberg, and IMF staff calculations and projections. 1/ AE = Advance Economies; EM = Emerging and Developing Economies; LAC = Latin America and the Caribbean, excluding Venezuela; SA = South Americ"
  },
  {
    "figure_id": "F050",
    "report_id": "R003",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "1/ The solid line represents the banking system series, and the dashed lines represent the maximum and minimum values among the six D-SIBs. Data prior to December 2020 is based on the Basel I regulations. Figure 5. Chile: Financial Sector NPL ratios stabilized"
  },
  {
    "figure_id": "F051",
    "report_id": "R003",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Figure 5. Chile: Financial Sector NPL ratios stabilized at a level slightly above the pre-pandemic average... Credit growth was sluggish, with a mild recovery in the second half of 2025. ... with provision coverage ratios similar to the pre-pandemic levels. Le"
  },
  {
    "figure_id": "F052",
    "report_id": "R003",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Peso Interest Rates (Swap Rates) Dollar Funding Premium in the Local Markets Sources: BCCh, Bloomberg, CEIC, Haver Analytics, and IMF staff calculations. Figure 6. Chile: Financial Markets The equity index remains close to its 2025 historical highs, while the "
  },
  {
    "figure_id": "F053",
    "report_id": "R003",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Sources: BCCh, Bloomberg, CEIC, Haver Analytics, and IMF staff calculations. Figure 6. Chile: Financial Markets The equity index remains close to its 2025 historical highs, while the price-to-earnings ratio is below its past average. After a gradual decline fo"
  },
  {
    "figure_id": "F054",
    "report_id": "R003",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Domestic non-financial corporate bond issuance has seen some dynamism in recent quarters. After experiencing robust inflows, equity and bond funds inflows have softened since the War. 1/ The index measures the performance of some of the largest and most liquid"
  },
  {
    "figure_id": "F055",
    "report_id": "R003",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "4/ ETFs: Exchange traded funds; MFs: Mutual funds. ## Figure 7. Chile: Pension Fund Sector The pension fund assets-to-GDP ratio is projected to increase thanks to the increased contribution rate. Pension funds' U.S. interest rate swaps by term Pension funds ar"
  },
  {
    "figure_id": "F056",
    "report_id": "R003",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## 6. The analysis also clearly identifies contributions to variations in the exchange rate: Sources: Central Bank of Chile, Haver Analytics, and IMF staff calculations. Notes: Exchange rate in Chilean peso per U.S dollar. # Annex III. External Sector Assessme"
  },
  {
    "figure_id": "F057",
    "report_id": "R003",
    "label": "IMF视觉摘要 1",
    "figure_type": "external_card",
    "context": "IMF｜IMF：铜价支撑难抵油价冲击，智利通胀再破3%目标｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F058",
    "report_id": "R004",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "for men and 60 for women), accumulated balances can be converted into an annuity, a programmed withdrawal, or a combination of both. 5. The approval of the reform reflected a broad political consensus. The reform, approved by Congress on January 29, 2025, envi"
  },
  {
    "figure_id": "F059",
    "report_id": "R004",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "7. Microdata analysis points to substantial heterogeneity in individual accumulated balances at retirement. The analysis draws on micro-level data from the Encuesta de Protección Social (EPS), which provides a representative sample of the adult population comp"
  },
  {
    "figure_id": "F060",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "based on a number of criteria, which include residency and age (individuals should be at least 65 years of age) as well as income criteria (individuals should be at the lowest 90 percent of the income distribution). Additionally, the PGU features a tapered ben"
  },
  {
    "figure_id": "F061",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Sources: Encuesta de Protección Social and IMF staff calculations. Note: The Unidad de Fomento (UF) is an inflation-indexed unit of account used in Chile to preserve the real value of financial transactions, contracts, and obligations over time. The value of t"
  },
  {
    "figure_id": "F062",
    "report_id": "R004",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Sources: Encuesta de Protección Social and IMF staff calculations. ## D. Baseline Scenario and the Role of Indexation 12. The type of indexation plays an important role for the evolution of the PGU's fiscal costs. For these estimations, we apply the projected "
  },
  {
    "figure_id": "F063",
    "report_id": "R004",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "on income whereby coverage of the PGU is reduced to the bottom 60 percent of the distribution, and one based on age, in which retirement and PGU eligibility age is increased to 67 for men and women. savings. This reform scenario considers gradually reducing el"
  },
  {
    "figure_id": "F064",
    "report_id": "R004",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "men, for whom the retirement age increases from 65 to 67, this increase would be around 13 percent. At the same time, the number of recipients of PGU would drop by about 11 percent by 2040, thereby reducing the total PGU expenditure by 0.3 percent of GDP relat"
  },
  {
    "figure_id": "F065",
    "report_id": "R004",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "men, for whom the retirement age increases from 65 to 67, this increase would be around 13 percent. At the same time, the number of recipients of PGU would drop by about 11 percent by 2040, thereby reducing the total PGU expenditure by 0.3 percent of GDP relat"
  },
  {
    "figure_id": "F066",
    "report_id": "R004",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## B. Overall Spending Trends 2. The size of total government spending in Chile is small relative to LA7 and OECD peers, and below cross-country averages for most economic spending categories. $^{2}$ \\- Total public expenditure in Chile reached 26.7 percent of"
  },
  {
    "figure_id": "F067",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "3. A longer-term perspective shows a gradual increase in Chile's size of government, at a slightly higher pace than among OECD peers. Over the past 12 years, total public spending (relative to GDP) in Chile rose by about 3.6 pps while average OECD spending inc"
  },
  {
    "figure_id": "F068",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2. Selected Expenditure Categories by Economic Transaction, Chile & OECD General Government Expenditure (In percent of GDP) General Government Expenditure (In USD PPP adjusted constant 2020, per capita) General Government Goods and Services (In percent "
  },
  {
    "figure_id": "F069",
    "report_id": "R004",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "General Government Employee Compensation (In percent of GDP) General Government Other Expenses (In percent of GDP) General Government Social Benefits (In percent of GDP) General Government Interest Payments (In percent of GDP) Sources: WEO and IMF staff calcul"
  },
  {
    "figure_id": "F070",
    "report_id": "R004",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "General Government Social Benefits (In percent of GDP) General Government Interest Payments (In percent of GDP) Sources: WEO and IMF staff calculations. Note: OECD average refers to the PPP GDP weighted average of OECD countries. 4. Chile's public spending-to-"
  },
  {
    "figure_id": "F071",
    "report_id": "R004",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "General Government Interest Payments (In percent of GDP) Sources: WEO and IMF staff calculations. Note: OECD average refers to the PPP GDP weighted average of OECD countries. 4. Chile's public spending-to-GDP ratios are below OECD averages across most economic"
  },
  {
    "figure_id": "F072",
    "report_id": "R004",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Sources: OECD, WEO and IMF staff calculations. Note: OECD average refers to the PPP GDP weighted average of OECD countries. 5. Chile's public expenditure is mainly concentrated in social functions. Examining the functional or sectoral composition as a share of"
  },
  {
    "figure_id": "F073",
    "report_id": "R004",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "5. Chile's public expenditure is mainly concentrated in social functions. Examining the functional or sectoral composition as a share of total government expenditure rather than GDP offers a clearer view of policy priorities as it enables abstracting from diff"
  },
  {
    "figure_id": "F074",
    "report_id": "R004",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "General Public Services Expenditure (In percent of total expenditure) Figure 4. Expenditure Ratios by Economic Function Over Time, Chile & OECD Economic Affairs Expenditure (In percent of total expenditure) Public Order and Safety Expenditure (In percent of to"
  },
  {
    "figure_id": "F075",
    "report_id": "R004",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Figure 4. Expenditure Ratios by Economic Function Over Time, Chile & OECD Economic Affairs Expenditure (In percent of total expenditure) Public Order and Safety Expenditure (In percent of total expenditure) Housing and Community Amenities Expenditure (In perce"
  },
  {
    "figure_id": "F076",
    "report_id": "R004",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "## C. Efficiency in Health and Education Spending 6. The relative efficiency of Chile's public expenditure in health and education can be assessed using Data Envelopment Analysis (DEA), with OECD economies as a reference group. Comparisons could be drawn with "
  },
  {
    "figure_id": "F077",
    "report_id": "R004",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "## Health Sector 7. Chile's healthcare sector operates as a mixed system, combining both public and private provision of health services as well as financing and insurance. Health services are delivered through a public network of hospitals and primary care ce"
  },
  {
    "figure_id": "F078",
    "report_id": "R004",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "8. The Chilean public health system has been facing persistent capacity constraints. Chile has one of the highest Intensive Care Unit (ICU) occupancy rates in the OECD, with utilization at 84 percent in 2023 (Figure 5). $^{10}$ Although the gap with the OECD a"
  },
  {
    "figure_id": "F079",
    "report_id": "R004",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Note: OECD averages are unweighted. The ICU occupancy rates refer to total adult ICUs. Data on ICU occupancy rate for Chile, Austria and Canada exclude private hospitals, whereas for the remaining countries coverage is either unspecified or includes private an"
  },
  {
    "figure_id": "F080",
    "report_id": "R004",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Note: OECD averages are unweighted. The ICU occupancy rates refer to total adult ICUs. Data on ICU occupancy rate for Chile, Austria and Canada exclude private hospitals, whereas for the remaining countries coverage is either unspecified or includes private an"
  },
  {
    "figure_id": "F081",
    "report_id": "R004",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "## 9. Chile generally performs well in terms of health outcomes, with significant Note: OECD averages are unweighted. Mortality rates are age-standardized to account for differences in population structures across countries. 10. Even though public spending on "
  },
  {
    "figure_id": "F082",
    "report_id": "R004",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "Note: OECD averages are unweighted. Mortality rates are age-standardized to account for differences in population structures across countries. 10. Even though public spending on healthcare has increased over time, it remains relatively low compared to OECD cou"
  },
  {
    "figure_id": "F083",
    "report_id": "R004",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Health Spending Composition (In percent GDP) per-capita public health spending (in PPP-adjusted terms) in 2023 exceeded its pre-pandemic level only slightly. Figure 7. Selected Public Healthcare Spending Indicators Government Health Spending (US dollars per pe"
  },
  {
    "figure_id": "F084",
    "report_id": "R004",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Figure 7. Selected Public Healthcare Spending Indicators Government Health Spending (US dollars per person, PPP constant prices 2020) General Government Spending on Health (In percent of GDP) Chile: Composition of Central Government Healthcare Expenditure (In "
  },
  {
    "figure_id": "F085",
    "report_id": "R004",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "Government Health Spending (US dollars per person, PPP constant prices 2020) General Government Spending on Health (In percent of GDP) Chile: Composition of Central Government Healthcare Expenditure (In percent of total) Sources: OECD, GFS, DIPRES and IMF staf"
  },
  {
    "figure_id": "F086",
    "report_id": "R004",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "General Government Spending on Health (In percent of GDP) Chile: Composition of Central Government Healthcare Expenditure (In percent of total) Sources: OECD, GFS, DIPRES and IMF staff calculations. Note: OECD average refers to the PPP GDP weighted average of "
  },
  {
    "figure_id": "F087",
    "report_id": "R004",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "Sources: OECD, GFS, DIPRES and IMF staff calculations. Note: OECD average refers to the PPP GDP weighted average of OECD countries. GFS data for Chile include spending at the central government level. 11. At the central government level, the composition of hea"
  },
  {
    "figure_id": "F088",
    "report_id": "R004",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "11. At the central government level, the composition of healthcare spending has remained broadly unchanged relative to pre-pandemic years in terms of economic transactions. The largest component remains employees' compensation, at 35.6 percent of total spendin"
  },
  {
    "figure_id": "F089",
    "report_id": "R004",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "higher education, the Gratuidad reform (2016) substantially expanded tuition-free access for eligible students, while the Local Public Education Services (SLEP) reform is gradually transferring public school management from municipalities to the central govern"
  },
  {
    "figure_id": "F090",
    "report_id": "R004",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "## 14. Chile's educational performance is above regional peers but below OECD averages. Student performance measured by PISA scores in different test domains is higher in Chile relative to LA7 comparators (Figure 9). However, there are still significant gaps w"
  },
  {
    "figure_id": "F091",
    "report_id": "R004",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Figure 9. Selected Education Outcomes 15. Chile's level of public education spending is similar to the OECD average when measured relative to GDP. Over the past decade, government education expenditure increased from 3.8 percent of GDP to 4.5 percent in 2023, "
  },
  {
    "figure_id": "F092",
    "report_id": "R004",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "Note: OECD average refers to the PPP GDP weighted average of OECD countries. The increase in employee compensation as a share of total central government education spending is linked to the Local Public Education Services (SLEP) reform. $^{15}$ A breakdown of "
  },
  {
    "figure_id": "F093",
    "report_id": "R004",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "Note: OECD average refers to the PPP GDP weighted average of OECD countries. The increase in employee compensation as a share of total central government education spending is linked to the Local Public Education Services (SLEP) reform. $^{15}$ A breakdown of "
  },
  {
    "figure_id": "F094",
    "report_id": "R004",
    "label": "Figure 11",
    "figure_type": "source_exhibit",
    "context": "Note: OECD average refers to the PPP GDP weighted average of OECD countries. The increase in employee compensation as a share of total central government education spending is linked to the Local Public Education Services (SLEP) reform. $^{15}$ A breakdown of "
  },
  {
    "figure_id": "F095",
    "report_id": "R004",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "incorporates key parameters such as risk aversion, correlation between income risk and risky asset returns, and social security benefits after retirement. ## 22. Life-cycle optimal portfolio models tend to recommend large allocations weights on the risky asset"
  },
  {
    "figure_id": "F096",
    "report_id": "R004",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "the risky asset during younger-age periods. The intuition behind this result is as follows: In a simple mean-variance portfolio model, the optimal risky asset allocation for a constant relative risk-aversion investor does not depend on the level of the wealth "
  },
  {
    "figure_id": "F097",
    "report_id": "R004",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Although it is not a financial asset, human capital should be considered as a part of the investor's wealth as it yields a stream of cashflows (i.e., labor income) like fixed income assets. In fact, the literature shows that the ratio of the optimal risky asse"
  },
  {
    "figure_id": "F098",
    "report_id": "R004",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Although it is not a financial asset, human capital should be considered as a part of the investor's wealth as it yields a stream of cashflows (i.e., labor income) like fixed income assets. In fact, the literature shows that the ratio of the optimal risky asse"
  },
  {
    "figure_id": "F099",
    "report_id": "R004",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "Figure 1. Asset Reallocations under the Multi-fund-based Example Glide Paths Notes: The estimation is based on the average allocations in 2024, combined with the estimated pension account balance by cohort in June 2024. \"D\" and \"F\" in the parentheses in the le"
  },
  {
    "figure_id": "F100",
    "report_id": "R004",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "\\- Risk-return profile of the risky asset. For the baseline estimation, the risk premium (expected excess return) and the volatility of the risky asset are calibrated to the historical average of the Santiago Stock Exchange's blue-chip IPSA index during 2016 a"
  },
  {
    "figure_id": "F101",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "\\- Relative risk aversion parameter. When the relative risk-aversion parameter—one of the most influential parameters—is changed from the baseline value of $\\gamma = 5$ to a less risk-averse level of $\\gamma = 3$ , the glide path dramatically shifts to an aggr"
  },
  {
    "figure_id": "F102",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "\\- Correlation between income risk and risky asset return. Following the literature, the baseline estimation sets the correlation between persistent shocks to income and risky asset return to zero. However, workers in cyclical sectors may be subject to a posit"
  },
  {
    "figure_id": "F103",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2. Asset Reallocations under the Model-based Example Glide Paths Baseline estimation PGU-like retirement income Notes: The top row reports the optimal risky asset weight path of the median investors calculated based on 10,000 simulations. The middle row"
  },
  {
    "figure_id": "F104",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Notes: The top row reports the optimal risky asset weight path of the median investors calculated based on 10,000 simulations. The middle row reports the glide path mapped from the optimal risky asset weight path by assuming that domestic-to-foreign asset allo"
  },
  {
    "figure_id": "F105",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Notes: The top row reports the optimal risky asset weight path of the median investors calculated based on 10,000 simulations. The middle row reports the glide path mapped from the optimal risky asset weight path by assuming that domestic-to-foreign asset allo"
  },
  {
    "figure_id": "F106",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Notes: The top row reports the optimal risky asset weight path of the median investors calculated based on 10,000 simulations. The middle row reports the glide path mapped from the optimal risky asset weight path by assuming that domestic-to-foreign asset allo"
  },
  {
    "figure_id": "F107",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Notes: The top row reports the optimal risky asset weight path of the median investors calculated based on 10,000 simulations. The middle row reports the glide path mapped from the optimal risky asset weight path by assuming that domestic-to-foreign asset allo"
  },
  {
    "figure_id": "F108",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Risk aversion ( $\\gamma$ ) and income-return correlation ( $\\rho$ ) Figure 2. Asset Reallocations under the Alternative risk-return profile (S&P 500 with partially hedged FX risk) Sources: SP and IMF staff calculations."
  },
  {
    "figure_id": "F109",
    "report_id": "R004",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2. Asset Reallocations under the Alternative risk-return profile (S&P 500 with partially hedged FX risk) Sources: SP and IMF staff calculations. Notes: The top row reports the optimal risky asset weight path of the median investors calculated based on 1"
  },
  {
    "figure_id": "F110",
    "report_id": "R004",
    "label": "IMF视觉摘要 1",
    "figure_type": "external_card",
    "context": "IMF｜IMF：IMF模拟智利养老金改革，指数化规则是财政可持续性的分水岭｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F111",
    "report_id": "R005",
    "label": "IMF视觉摘要 1",
    "figure_type": "external_card",
    "context": "IMF｜IMF：IMF评估乌干达债务数据，统计口径之外的真实负债被低估｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F112",
    "report_id": "R006",
    "label": "IMF视觉摘要 1",
    "figure_type": "external_card",
    "context": "IMF｜IMF：发展中国家债务统计困境，乌干达欠款和透支远高于表面数据｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F113",
    "report_id": "R007",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "The global economy as a whole has, so far, weathered the shock from the war better than feared. Movements in and repercussions from the main channels of transmission—commodity prices, inflation expectations, and financial conditions—have been relatively limite"
  },
  {
    "figure_id": "F114",
    "report_id": "R007",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "\\- Global financial conditions have eased since their peaks in early April and continue to be accommodative by historical standards (Box 1). The easing trend has been accompanied by bouts of volatility, and markets are pricing in higher nominal policy rates in"
  },
  {
    "figure_id": "F115",
    "report_id": "R007",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "On the back of these developments, global growth in the first quarter of 2026 turned out to be stronger than expected, slowing from 3.8 percent in the fourth quarter of 2025 to 3.0 percent on a quarter-over-quarter annualized basis, instead of the 2.7 percent "
  },
  {
    "figure_id": "F116",
    "report_id": "R007",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "That said, much of the positive surprise was concentrated in a few economies that are well integrated into the global technology value chain, even though some of these economies also had exposure to commodity market disruptions originating from the war: For in"
  },
  {
    "figure_id": "F117",
    "report_id": "R007",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Figure 2. Inflation Expectations Rise, but Mostly in the Short Term (Density) Sources: Consensus Economics; and IMF staff calculations. Note: Dashed vertical lines mark the cross-country simple means per vintage. The sample includes 34 AEs and 33 EMDEs in the "
  },
  {
    "figure_id": "F118",
    "report_id": "R007",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "private consumption. In Germany, GDP expanded by 1.4 percent, twice the April 2026 WEO projection of 0.7 percent, driven by net exports. In the United States, GDP increased at an annualized rate of 2.1 percent in the first quarter of 2026, slower than the 2.5 "
  },
  {
    "figure_id": "F119",
    "report_id": "R007",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "\\- Policy and geopolitical uncertainty are assumed to remain elevated through 2027. The AI-driven global technology cycle is assumed to moderate, and there is no exogenous boost to productivity growth. Figure 4. Growth Revisions Vary by Exposures to the War an"
  },
  {
    "figure_id": "F120",
    "report_id": "R007",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Maintaining orderly adjustment and financial stability amid the ongoing large shocks is essential. For countries with inflation targets or other domestic nominal anchors, exchange rates should generally remain the preferred option, helping economies absorb ext"
  },
  {
    "figure_id": "F121",
    "report_id": "R007",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "system from the effects of the Middle East conflict. Financial conditions remain accommodative and have eased further on prospects of conflict de-escalation, as corporate bond spreads remain historically tight and equity markets have strengthened since the Apr"
  },
  {
    "figure_id": "F122",
    "report_id": "R007",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "dependence highlighted in the April 2026 GFSR. In crude-oil-importing Asian emerging markets, deterioration in the terms of trade has worsened the inflation outlook and put pressure on exchange rates, prompting a sharper upward repricing of expected policy pat"
  },
  {
    "figure_id": "F123",
    "report_id": "R007",
    "label": "IMF视觉摘要 1",
    "figure_type": "external_card",
    "context": "IMF｜IMF：全球通胀停滞在4.7%，美联储降息窗口被技术红利与战争冲击压缩｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F124",
    "report_id": "R008",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## Box 1. What environments shape adolescents' social and emotional well-being? Research on child well-being increasingly recognises the importance of the environments and settings in which children and adolescents grow up, requiring a multi-level or “ecologic"
  },
  {
    "figure_id": "F125",
    "report_id": "R008",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "OECD countries with available data (see Figure A.2 in the additional data that can be found clicking on the Support materials tab of the paper at this link: https://doi.org/10.1787/00ebd3dd-en). Girls also feel lonelier than boys: in all 28 OECD countries with"
  },
  {
    "figure_id": "F126",
    "report_id": "R008",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Adolescents are also experiencing worsening mental health and increasing signs of ill-being, including elevated levels of stress, trauma, anxiety, and depression, with again significant differences between boys and girls observed across several indicators (OEC"
  },
  {
    "figure_id": "F127",
    "report_id": "R008",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Risk-taking behaviours also differ between boys and girls, but the patterns are nuanced and vary across activities, so it cannot be assumed that boys are systematically more likely than girls to engage in such behaviours (Molinaro et al., 2024[23]). For exampl"
  },
  {
    "figure_id": "F128",
    "report_id": "R008",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Adolescent girls are less likely to report high levels of self-efficacy, i.e. to have high confidence in their capacity to exercise control over important things in their lives. For example, on average across the OECD, 53% of 11-, 13- and 15-year-old girls rep"
  },
  {
    "figure_id": "F129",
    "report_id": "R008",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "It should be noted that femininity and masculinity norms and stereotypes are not the sole drivers of gaps in adolescent boys' and girls' social and emotional well-being, nor are they homogeneous across the OECD. Firstly, while general trends emerge in the avai"
  },
  {
    "figure_id": "F130",
    "report_id": "R008",
    "label": "Figure 7",
    "figure_type": "source_exhibit",
    "context": "Strict adherence to restrictive masculine norms in adolescence can also undermine boys' engagement in academic learning and contribute to lower academic performance. Boys – and, to a lesser extent, girls – who conform rigidly to norms emphasising emotional det"
  },
  {
    "figure_id": "F131",
    "report_id": "R008",
    "label": "Figure 8",
    "figure_type": "source_exhibit",
    "context": "## 4.1. Ensuring adolescents feel supported in the family and home environment Supportive family and home environments are needed as they initially shape children's and adolescents' beliefs and behaviours and are a strong predictor of adolescent life satisfact"
  },
  {
    "figure_id": "F132",
    "report_id": "R008",
    "label": "Figure 9",
    "figure_type": "source_exhibit",
    "context": "Ensuring that the school environment provides adequate support for children's flourishing – through strong school belonging, an inclusive climate, and positive peer and student-teacher relationships – while avoiding becoming a"
  },
  {
    "figure_id": "F133",
    "report_id": "R008",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "Supporting positive online experiences for adolescent girls and boys requires a multifaceted approach (OECD, 2025[169]). Adolescents' safety must primarily be ensured through robust regulatory frameworks and the widespread adoption of safe technologies and ser"
  },
  {
    "figure_id": "F134",
    "report_id": "R008",
    "label": "Figure 10",
    "figure_type": "source_exhibit",
    "context": "## Figure 10. Girls are more likely than boys to have gotten upset the last time they encountered negative content online 15-year-old students who report getting upset the last time they... (2022) Panel A: .... encountered content online that was inappropriate"
  },
  {
    "figure_id": "F135",
    "report_id": "R008",
    "label": "经合组织视觉摘要 1",
    "figure_type": "external_card",
    "context": "经合组织｜经合组织：不是焦虑，是内收，经合组织揭示男孩女孩福祉差异的真正原因｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F136",
    "report_id": "R009",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "AI can also help companies improve product or service quality (OECD, 2023[2]), enabling workers to benefit simultaneously through improved job quality and satisfaction. Indeed, AI could reduce or eliminate dangerous or tedious tasks, and create more complex an"
  },
  {
    "figure_id": "F137",
    "report_id": "R009",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Finally, in addition to the displacement effect, the automation channel can give rise to a productivity effect. This can result in increases in labour demand for tasks or jobs not automated by AI, such as packers and forklift operators. The productivity effect"
  },
  {
    "figure_id": "F138",
    "report_id": "R009",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "## Jobs with greatest exposure to AI are not necessarily those with a high risk of automation Using data from labour force surveys, Lane (2024[16]) shows that on average across OECD Member countries, “IT professionals”, “Business professionals”, “Managers”, “C"
  },
  {
    "figure_id": "F139",
    "report_id": "R009",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "In an OECD study to reflect advancements in automation technologies, Lassébie and Quintini (2022[18]) re-evaluates how various occupations are exposed to automation. This assessment, which draws on a unique survey measuring the automatability of around 100 dis"
  },
  {
    "figure_id": "F140",
    "report_id": "R009",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "While AI has made some high-skill job requirements more susceptible to automation, many critical skills in these roles remain difficult to automate. As a result, despite greater exposure to recent AI advancements, high-skill jobs generally continue to be among"
  },
  {
    "figure_id": "F141",
    "report_id": "R009",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Despite increased AI adoption by firms, workers with AI skills represent a small share of the overall workforce (about 1%). While workers with AI skills are relatively rare, their share in the workforce has almost tripled from less than a decade ago (Green and"
  },
  {
    "figure_id": "F142",
    "report_id": "R009",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Between-country AI skills migration, 2019 and 2024 Note: Vacancies with high exposure to artificial intelligence have an occupational artificial exposure measure one standard deviation greater than the mean according to Felten, Raj and Seamans (2021 $^{[33]}$ "
  },
  {
    "figure_id": "F143",
    "report_id": "R009",
    "label": "经合组织视觉摘要 1",
    "figure_type": "external_card",
    "context": "经合组织｜经合组织：AI技能人才仅占劳动力1%，政策制定者真正该焦虑的不是失业｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F144",
    "report_id": "R010",
    "label": "Figure 1",
    "figure_type": "source_exhibit",
    "context": "## Why are capital markets important for businesses in Bosnia and Herzegovina? Creating conditions for businesses to use capital markets is crucial for Bosnia and Herzegovina, where the bank-dominated financial system does not adequately meet the financing nee"
  },
  {
    "figure_id": "F145",
    "report_id": "R010",
    "label": "Figure 2",
    "figure_type": "source_exhibit",
    "context": "Sources: (World Bank, 2024[12]; Eurostat, 2024[13]). Percentage of total outstanding loans Note: WB6 data refers to the unweighted average of all six Western Balkan economies. Sources: (IMF, 2025[14]); data for Serbia from (National Bank of Serbia, 2024[15]) C"
  },
  {
    "figure_id": "F146",
    "report_id": "R010",
    "label": "Figure 3",
    "figure_type": "source_exhibit",
    "context": "Percentage of total outstanding loans Note: WB6 data refers to the unweighted average of all six Western Balkan economies. Sources: (IMF, 2025[14]); data for Serbia from (National Bank of Serbia, 2024[15]) Challenges in accessing external finance are most acut"
  },
  {
    "figure_id": "F147",
    "report_id": "R010",
    "label": "Figure 4",
    "figure_type": "source_exhibit",
    "context": "Notes: Data do not include unincorporated enterprises. Value added is calculated at factoring cost. 2024 data are preliminary. Enterprise size classifications follow the EU definition: small enterprises employ fewer than 50 persons, medium-sized enterprises em"
  },
  {
    "figure_id": "F148",
    "report_id": "R010",
    "label": "Figure 5",
    "figure_type": "source_exhibit",
    "context": "Capital markets in Bosnia and Herzegovina are underdeveloped and fragmented. Despite their potential to diversify financing sources, they currently constitute only a small part of the overall financial system. According to the OECD Western Balkans Competitiven"
  },
  {
    "figure_id": "F149",
    "report_id": "R010",
    "label": "Figure 6",
    "figure_type": "source_exhibit",
    "context": "## Corporate bond market The corporate bond market has generally been shallow in both entities, with activity largely confined to the financial sector rather than supporting productive investment. In RS, approvals by the Securities Commission indicate visible "
  },
  {
    "figure_id": "F150",
    "report_id": "R010",
    "label": "经合组织视觉摘要 1",
    "figure_type": "external_card",
    "context": "经合组织｜经合组织：波黑资本市场缺的不是资金，是信任和整合｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F151",
    "report_id": "R011",
    "label": "世界贸易组织视觉摘要 1",
    "figure_type": "external_card",
    "context": "世界贸易组织｜世界贸易组织：世界贸易组织裁决，欧盟对印尼反倾销案汇率计算违规｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F152",
    "report_id": "R012",
    "label": "EXHIBIT 1",
    "figure_type": "source_exhibit",
    "context": "## EXHIBIT 1 # Three MENA D2D uptake archetypes are expected to emerge ## MENA network coverage score (GSMA) vs. rural population Comparing mobile connectivity coverage with rural population across MENA countries D2D also has the potential to become a key resi"
  },
  {
    "figure_id": "F153",
    "report_id": "R012",
    "label": "波士顿咨询视觉摘要 1",
    "figure_type": "external_card",
    "context": "波士顿咨询｜波士顿咨询：D2D的‘韧性溢价’到底值多少钱｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F154",
    "report_id": "R013",
    "label": "波士顿咨询视觉摘要 1",
    "figure_type": "external_card",
    "context": "波士顿咨询｜波士顿咨询：报告揭示，超六成消费者期待AI参与奢侈品购买｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F155",
    "report_id": "R014",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "For example, in the US, five states receive roughly 80% of combined federal and state disaster-mitigation funding. These include the most disaster-prone states in the country, such as Florida, Louisiana, and California. But a second group—Mississippi, North Ca"
  },
  {
    "figure_id": "F156",
    "report_id": "R014",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "Financial resilience is the capacity of financial systems to absorb climate-driven losses, keep capital flowing, and continue pricing and sharing risk after a shock. Insurance covers roughly 40% of global climate losses—a share that has doubled in two decades."
  },
  {
    "figure_id": "F157",
    "report_id": "R014",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "In fact, we found reinsurance and capital-market coverage had decreased relative to the rise in insured natural disaster losses by 60% in the last 20 years, meaning insurers are carrying more risk from climate-related losses that in the past had been syndicate"
  },
  {
    "figure_id": "F158",
    "report_id": "R014",
    "label": "Exhibit 4",
    "figure_type": "source_exhibit",
    "context": "The Federal Reserve Bank of Dallas found that an average homeowner's insurance premium increase between June 2022 and 2023 was associated with nearly 150,000 mortgages becoming delinquent within a year. Our own analysis shows that real insurance premiums in th"
  },
  {
    "figure_id": "F159",
    "report_id": "R014",
    "label": "Exhibit 5",
    "figure_type": "source_exhibit",
    "context": "Sources: “Property insurance and disaster risk: New evidence from mortgage escrow data,” Keys & Mulder, National Bureau of Economic Research, 2025; Federal Emergency Management Agency; American Community Survey, US Census Bureau; BCG analysis. $^{1}$ Risk cate"
  },
  {
    "figure_id": "F160",
    "report_id": "R014",
    "label": "波士顿咨询视觉摘要 1",
    "figure_type": "external_card",
    "context": "波士顿咨询｜波士顿咨询：气候韧性最大误判，物理不确定性低的地方，资金更脆弱｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F161",
    "report_id": "R015",
    "label": "波士顿咨询视觉摘要 1",
    "figure_type": "external_card",
    "context": "波士顿咨询｜波士顿咨询：AgenticAI的真正瓶颈不是技术，而是智能层｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F162",
    "report_id": "R016",
    "label": "波士顿咨询视觉摘要 1",
    "figure_type": "external_card",
    "context": "波士顿咨询｜波士顿咨询：医生不是成本难题，而是医院控费真正引擎，波士顿咨询｜用于快速识别该外部报告的核心问题和市场含义。"
  },
  {
    "figure_id": "F163",
    "report_id": "R017",
    "label": "Exhibit 1",
    "figure_type": "source_exhibit",
    "context": "## Exhibit 1 Financial assets are mounting quickly; wealth accumulation is outpacing the real economy. Intermediated funds in global financial system, 2020–25 Share of intermediated funds, \\$ trillion Note: Figures may not sum to 100%, because of rounding. $^{"
  },
  {
    "figure_id": "F164",
    "report_id": "R017",
    "label": "Exhibit 2",
    "figure_type": "source_exhibit",
    "context": "Margins remained consistent. By our measure, $^{2}$ revenue margins declined slightly from 0.97 in 2024 to 0.94 in 2025 (Exhibit 2). Costs also improved, dropping from 1.31 percent of assets in 2024 to 1.23 percent in 2025. While both stories are positive, it "
  },
  {
    "figure_id": "F165",
    "report_id": "R017",
    "label": "Exhibit 3",
    "figure_type": "source_exhibit",
    "context": "A greater share of wealth management revenues benefited the US banking industry (and other financial institutions), lifting ROEs to 12 percent. European banks also improved, from 10.7 percent in 2024 to 11.6 percent in 2025—but this was mainly the result of op"
  },
  {
    "figure_id": "F166",
    "report_id": "R017",
    "label": "Exhibit 6",
    "figure_type": "source_exhibit",
    "context": "Banks in Southeast Europe, South Asia, and Africa have the potential to leapfrog other regions by building digital and AI infrastructure from scratch. It's an opportunity to develop highly innovative, next-generation banking models. Low-cost structures enable "
  },
  {
    "figure_id": "F167",
    "report_id": "R017",
    "label": "Exhibit 9",
    "figure_type": "source_exhibit",
    "context": "# Neobanks are achieving significantly faster growth in both scale and profitability than traditional players. Leading banks, by number of customers and ROE, 2021–25 2021 ○—● 2025 Europe McKinsey & Company These two neobanks, along with Robinhood and Wise, hav"
  },
  {
    "figure_id": "F168",
    "report_id": "R017",
    "label": "Exhibit 9",
    "figure_type": "source_exhibit",
    "context": "2021 ○—● 2025 Europe McKinsey & Company These two neobanks, along with Robinhood and Wise, have likewise broken through traditional barriers on growth and profitability (Exhibit 9). As they've grown, neobanks have developed a full suite of banking products and"
  },
  {
    "figure_id": "F169",
    "report_id": "R017",
    "label": "Exhibit 10",
    "figure_type": "source_exhibit",
    "context": "Banking relies on older customers for an outsize share of revenues and profits. That's becoming a problem, as younger customers are revealing quite different preferences for how they want to bank. These customers are more highly engaged and expect services tha"
  },
  {
    "figure_id": "F170",
    "report_id": "R017",
    "label": "Exhibit 10",
    "figure_type": "source_exhibit",
    "context": "Perhaps the starkest view of customers' shifting allegiance is shown in Exhibit 10. Not only are fintechs and neobanks delivering greater satisfaction, they are also now leading on trust, the long-time privilege of traditional, high-street banks. # Customer-ce"
  },
  {
    "figure_id": "F171",
    "report_id": "R017",
    "label": "Exhibit 12",
    "figure_type": "source_exhibit",
    "context": "This drag on productivity was not fatal, of course. The traditional banking strategy for new technologies, call it “smart followership,” worked reasonably well, for one reason. Banks’ high-value customer segments (aged 55 and up) were also slow to adopt digita"
  },
  {
    "figure_id": "F172",
    "report_id": "R017",
    "label": "Exhibit 13",
    "figure_type": "source_exhibit",
    "context": "McKinsey & Company High-value customer segments were slow to adopt digital, creating a technology ‘grace period’ that protected revenue despite slow change. Revenue and level of adoption, US mobile banking, by age cohort, 2023 $^{1}$ McKinsey & Company Custome"
  },
  {
    "figure_id": "F173",
    "report_id": "R017",
    "label": "Exhibit 13",
    "figure_type": "source_exhibit",
    "context": "Customers' rapid AI adoption across age groups signals that this time there will be no grace period for banks (Exhibit 13). ChatGPT launched in November 2022; by 2024, fully 45 percent of US working-age adults were using gen AI, rising to 55 percent by 2025. T"
  },
  {
    "figure_id": "F174",
    "report_id": "R017",
    "label": "麦肯锡视觉摘要 1",
    "figure_type": "external_card",
    "context": "麦肯锡｜麦肯锡：AI时代银行不能只等对手出局，客户正绕过银行完成资金服务｜用于快速识别该外部报告的核心问题和市场含义。"
  }
]