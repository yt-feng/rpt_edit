请基于下面每天新报告的摘要，写一份“市场最新观点汇总”的结构化 JSON，用于生成 PDF。

要求：
1. 观点要分门别类，例如：宏观与利率、AI/算力、能源与大宗、地产与消费、区域市场、风险偏好等。类别由内容决定，不要机械套模板。
2. sections 建议 5-8 个，尽量覆盖所有报告 ID；references 合并后应覆盖大多数甚至全部报告。
3. 每个板块要综合多篇报告，不要逐篇复述，但不能只写高度抽象的空话。
4. 每个板块必须有 5-10 个要点，每个要点是可读的完整句子，保留关键数据、方向和分歧。
5. 每个板块末尾必须给 references，引用报告 ID，不要在正文每句后塞引用。
6. 可以使用所有 figure_ids，没有总数限制，但只选择真正支撑该板块观点且图表说明干净的图。
7. 投行名字必须脱敏：常见投行写 GS、JPM、MS、BofA、Citi、UBS、DB 等缩写，不确定就写“投行”。
8. 不要给投资建议，不要写买卖评级。
9. 输出必须是 JSON 对象，不要 Markdown 代码块。

JSON 格式：
{"title":"市场最新观点汇总","subtitle":"一句话说明今天的市场主线","executive_summary":["要点1"],"sections":[{"heading":"板块标题","thesis":"核心判断","bullets":["要点1"],"figure_ids":["F001"],"references":["R001"]}],"closing":"简短收束"}

报告摘要：
[
  {
    "id": "R001",
    "title": "JPM：市场低估的不是贸易摩擦，而是中国电池产能管控的结构性红利",
    "digest": "[wechat_article.md]\n# JPM：市场低估的不是贸易摩擦，而是中国电池产能管控的结构性红利\n\n过去六周，中国电池供应链相关股票从5月初高点回调了15%至40%，而同期沪深300指数仅下跌5%。市场习惯性地将这一轮调整归因于中欧贸易摩擦升级、锂价波动以及资金流向AI科技板块。但JPM最新发布的电池行业深度报告提出了一个根本不同的判断：市场真正忽略的，是中国正在推进的产能管控政策——这并非一次临时性干预，而是电池行业供给侧改革的正式启动。\n\n这份由Rebecca Wen领衔的研报，系统梳理了四条影响电池行业格局的关键线索：国内产能审批收紧、对外投资新规、中欧贸易摩擦以及美国关税与实体清单。其中，国内产能管控被明确标记为“正面影响”，其他三项则被评估为“中性”。这一定位本身就值得产业决策者认真思考——当市场的注意力被贸易摩擦吸引时，真正改变行业基本面的力量正在国内政策端悄然成型。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 产能审批权的上收，正在从根本上改变中国电池行业的竞争规则\n\nJPM报告揭示了一个关键的制度变化：电池产能项目的审批权限正在从省级政府向更高层级集中。过去，地方政府在审批电池产能项目时拥有相当程度的自由裁量权，这在一定程度上推动了产能的快速扩张，但也导致了大量低端同质化产能的涌入。新规的核心变化在于，大型电池项目和跨省投资可能需要更高层级的审查与批准，整体产能增量甚至可能纳入配额管理。\n\n这意味着地方政府独立批准新项目的灵活性将大幅降低。报告特别指出，这一政策采用了明确的“老项目老办法”原则——已获批、已完成备案或已开工的项目不受影响。大多数计划在2026年投产的扩产项目已经完成了相关审批程序，因此能够正常推进。政策的实际效果将主要体现在2027年下半年之后的新增产能上。\n\n这一制度设计的精妙之处在于，它没有采取行政命令\n\n[... middle omitted ...]\n\n结构性机会的读者，这些细节可能比市场共识更有价值。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n电池行业的关键拐点来了\n\n产能管控，行业洗牌\n\n中国电池行业迎来真正的供给侧改革\n\n最近电池板块回调不少，但别光盯着贸易摩擦。真正改变行业格局的，是国内正在收紧的产能审批政策。\n\n1️⃣ 产能审批全面收紧\n过去地方政府可以批项目，现在大型电池项目要报更高层级审批。新增产能可能实行配额制，政策资源优先给头部企业。小厂想扩产？难度大增。\n\n2️⃣ 2027年后供给增速才会放缓\n现有项目不受影响（2026年计划已获批），新规主要影响2027年下半年后的新增产能。研报测算，行业有效供给增速从2027年开始放缓，2028年供需格局改善会更明显。\n\n3️⃣ 头部玩家更受益\n宁德时代被列为行业首选——唯一穿越周期的复合增长型公司。中创新航、璞泰来近期被上调评级。逻辑很清晰：技术强、资金足、运营好的企业，在产能管控时代会拿到更多市场份额。\n\n4️⃣ 补贴退坡+绿色信贷降温\n过去很多二线电池厂70%以上利润来自政府补贴，现在地方财政吃紧，绿色贷款增速放缓，A股再融资收紧，小厂融资越来越难。行业正从“拼规模”转向“拼技术”。\n\n5️⃣ 出海门槛提高\n2026年6月发布的《对外投资条例》将技术、数据、人员输出纳入监管框架。海外项目\n\n[... middle omitted ...]\n\n The market's focus on EU-China trade tensions is warranted, but we believe China's recent capacity control policies are the true catalysts reshaping the sector's supply-demand dynamics. We su\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 12 Jun 2026 06:25 AM HKT\n\nDisseminated 12 Jun 2026 10:33 PM HKT"
  },
  {
    "id": "R002",
    "title": "NOM：中国信贷收缩的“新常态”正在重塑资产定价逻辑",
    "digest": "[wechat_article.md]\n# NOM：中国信贷收缩的“新常态”正在重塑资产定价逻辑\n\n这份NOM研报的核心判断并不复杂，但它的冲击力在于数据背后的结构性含义：中国5月信贷增速降至7.7%，创历史新低，且这种放缓并非短期波动，而是需求端结构性收缩与供给端政策主动调控共同作用的结果。市场如果只将其解读为“经济复苏乏力”的又一个证据，可能低估了这场信贷收缩对资产定价、企业盈利与政策框架的深远影响。\n\nNOM的数据显示，5月新增社融2.03万亿元，远低于市场预期的2.32万亿元，也低于去年同期的2.29万亿元。人民币贷款余额增速降至5.5%，同样是历史最低。但真正值得注意的是，这些数字背后隐藏着三个相互关联的结构性变化：居民部门持续去杠杆、企业贷款依赖票据融资“注水”、以及央行主动收紧流动性以修复利率信号机制。\n\n这不是一次简单的周期性放缓。它可能标志着中国信用扩张模式正在从“量宽价低”转向“量稳价韧”，而这一转变对股票、债券和房地产的定价含义，远比表面数据更深远。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 居民部门去杠杆已从“短期波动”演变为“长期趋势”\n\nNOM报告中最令人不安的数据来自居民贷款。5月新增居民贷款为负1410亿元，而去年同期为正值540亿元。更关键的是，无论是短期贷款还是中长期贷款，双双录得负增长：短期贷款减少840亿元，中长期贷款减少570亿元。这在历史上极为罕见。\n\n这意味着居民部门不仅在减少借贷，还在主动偿还存量债务。居民存款数据同样印证了这一点：5月新增居民存款为负1100亿元，而去年同期为4700亿元。这是自2015年以来首次出现5月居民存款负增长。居民并非没有钱，而是钱正在从银行体系流向其他领域——可能是消费、可能是理财，也可能是偿还负债。\n\n对投资者而言，居民去杠杆意味着什么？它直接抑制了消费类资产的盈利预期\n\n[... middle omitted ...]\n\n构对同一数据的交叉验证，以及我们基于这些数据构建的观察框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n社融增速新低，钱去哪了？\n\n📉 5月数据怎么看\n\n社融增速又创历史新低，5月存量增速降到7.7%。不是偶然，是连续三个月走弱。\n\n1️⃣ 信贷结构很“虚”\n- 企业贷款表面还行，但全靠票据融资撑——票据新增5570亿，同比多增近5000亿。\n- 去掉票据，企业实际贷款需求比数字看起来弱很多。\n- 居民贷款继续负增长，短期和中长期都在缩，说明家庭还在主动去杠杆。\n\n2️⃣ 政府债发行意外偏慢\n- 政府债券净融资同比少增2370亿，拖累社融。\n- 研报推测后续会加速，因为基建投资需要支撑。\n\n3️⃣ 央行在主动收紧流动性\n- 银行间利率持续低于政策利率（DR007一度到1.3%以下），资金淤积在金融体系。\n- 央行缩OMO规模+窗口指导银行减少同业拆借，把利率拉回1.4%以上。\n- 意图不是为降息降准留空间，而是修复利率信号功能、防范债市风险。\n\n4️⃣ 居民存款罕见负增长\n- 5月居民存款减少1100亿，是2015年以来首次5月负值。\n- 可能反映消费或理财搬家，但非银存款变化不大，说明不是单纯转去买理财。\n\n💡 几个值得观察的点\n- 政府债发行提速能不能稳住社融\n- 企业中长期贷款何时转正（目前-200亿）\n\n[... middle omitted ...]\n\nighed down mainly by the household sector. As in April, May new loans in the corporate sector appear to be adequate on the surface, as they exceeded year earlier levels, but this was primarily\n\n[... middle omitted ...]\n\nable upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R003",
    "title": "JPM：市场低估的不是AI算力需求，而是数据中心现场供电的结构性缺口",
    "digest": "[wechat_article.md]\n# JPM：市场低估的不是AI算力需求，而是数据中心现场供电的结构性缺口\n\n数据中心缺电这件事，大多数人还停留在“算力增长快，所以电力需求大”的线性理解上。但JPM近期组织的一场专家电话会，揭示了一个更深刻的判断：全球数据中心真正的瓶颈不是GPU供应，也不是芯片算力，而是电网根本接不上。这个缺口正在推动一个全新的现场供电产业链崛起，其市场空间和利润结构，远未被当前股价充分定价。\n\n这份研报的核心信号是：美国约60%的数据中心仍依赖电网供电，但超过20%已经开始使用燃气轮机作为主电源，燃气发动机和固体氧化物燃料电池（SOFC）的占比正在快速上升。这不是备用电源的补充逻辑，而是主电源的结构性替代。当电网的互联延迟和电力短缺直接拖累项目时间表时，数据中心运营商被迫自建发电设施，这正在重塑整个电力供应链的竞争格局。\n\nJPM对潍柴动力和应流股份均维持超配评级，但比评级更值得关注的，是报告中关于SOFC技术路线、供应链壁垒、以及中国企业在全球扩张中真实竞争优势的细节。这些判断如果成立，意味着AIDC电源供应链的估值框架需要被重新定义——不是周期性的资本开支脉冲，而是持续多年的结构性增长。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 电网瓶颈不再是背景噪音，而是现场供电需求的直接推手\n\n多数投资者关注AI数据中心时，讨论焦点集中在算力芯片、液冷散热、或者光模块的速率升级。但JPM专家电话会的第一层判断非常直接：电网互联延迟和电力短缺，已经取代了“算力增长”本身，成为驱动现场供电解决方案需求的最主要因素。\n\n这个“所以呢”的推论是：数据中心运营商不再把现场供电视为备用选项，而是将其作为项目能否按时上线的关键路径。在美国，电网审批周期动辄三到五年，而数据中心从决策到投运的时间窗口正在被压缩到18个月以内。这种时间错配意味着，那\n\n[... middle omitted ...]\n\n价值，往往不在研报本身，而在不同视角的碰撞中产生的二阶洞察。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAIDC电源链的新增长点\n\n**电网瓶颈，催生新赛道**\n\n最近读了份某外资投行的研报，聊的是AI数据中心（AIDC）的现场电源方案。核心逻辑很清晰：电网跟不上AI的用电需求，数据中心开始自己搞发电了。\n\n1/ **电网瓶颈成了最大推手**\n美国60%的数据中心还在用市电，但电网审批慢、供电不稳，项目经常延期。现在超过20%的数据中心直接上了燃气轮机当主力电源，燃气发电机和SOFC（固体氧化物燃料电池）的渗透率也在快速提升。中国玩家在产能和交付速度上有明显优势。\n\n2/ **SOFC是下一个爆发点**\n研报预测，到2030年全球SOFC需求将达到20-30GW。中国的政策支持很像当年扶持锂电池和光伏——给产能、给补贴、帮降本。目前SOFC全生命周期成本约0.08-0.15美元/kWh（按8-10年算），随着国产化推进，成本还会继续下探。数据中心看中它的灵活性：低温运行、快速启停，很适合做综合电源方案的一部分。\n\n3/ **谁在卡位？**\n- 某动力龙头：2026年AIDC发动机出货目标3500-4000台；SOFC产能规划很激进——2026年30MW、2027年200MW、2028年600MW、2030年1G\n\n[... middle omitted ...]\n\noth government policy and private sector investment in AI and data centers is accelerating in China, the US, and globally, with no signs of slowing down. This is driving a new wave of demand f\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R004",
    "title": "摩根斯坦利：市场真正低估的不是通胀，而是美联储转向加息的路径",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：市场真正低估的不是通胀，而是美联储转向加息的路径\n\n当绝大多数市场参与者还在讨论“通胀何时回落、降息何时到来”时，摩根斯坦利最新一期美国经济周报发出了一个信号，其含义远比表面数据复杂：美联储的风险天平正在从“就业下行”重新摆向“通胀上行”，而且这种摆动的速度可能比市场定价所反映的更快。\n\n这不是一个关于数据小幅超预期的讨论。这是一份关于美联储政策框架可能发生结构性转变的报告。去年，美联储因为担忧就业下行而降息75个基点。但今天，摩根斯坦利的经济学家团队在首席美国经济学家Michael Gapen的带领下，提出了一个让市场必须重新审视的命题：我们可能同时面临两个导致美联储无法降息、甚至需要加息的场景——需求拉动型通胀和持续性石油溢价。\n\n这份报告的核心贡献不在于它预测了哪一组数据，而在于它构建了一个清晰的决策框架：当前的数据正在同时向这两个场景靠拢。就业市场在走强，关税脉冲接近尾声，但石油价格通过机票等核心服务渠道的传导才刚刚开始被市场定价。报告中最值得关注的判断是：如果中东冲突不能短期内解决，核心PCE在2026年底前低于3%的可能性正在快速下降，这意味着2027年快速降息的预期可能建立在错误的前提上。\n\n以下是我们从这份报告中提炼出的五个关键洞察，以及一个报告尚未完全回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 就业市场的重新走强正在改变美联储的风险计算，而市场对此定价不足\n\n摩根斯坦利的分析显示，过去三个月的平均新增就业已回升至约18.8万人，这明显高于去年水平，也高于美联储和市场的普遍预期。更重要的是，这一数字远高于该机构估算的维持失业率稳定所需的约5万人的盈亏平衡线。\n\n这里的关键不是就业数字本身，而是它对美联储政策框架的冲击。一年前，美联储认为就业下行风险大于通胀风险，\n\n[... middle omitted ...]\n\n场景的叠加效应，以及它们对各类资产定价的潜在含义。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美联储的平衡木：通胀风险正在重新抬头\n\n通胀风险 > 就业风险\n\n就业数据持续走强，通胀压力意外上行\n\n最新数据显示，美联储的风险天平正在倾斜。📊\n\n几个关键点：\n\n1️⃣ 就业市场比预期更热\n近三个月新增就业均值约18.8万，显著高于去年水平。失业率稳定在4.3%左右。问题是：能源价格上涨是否会抑制就业？如果就业继续强劲，失业率可能进一步下行，这会推高美联储转向加息的概率。\n\n2️⃣ 通胀数据出现意外\n5月核心CPI符合预期（0.21%），但PPI传导至核心PCE时超预期。核心PCE预计5月环比0.36%，同比3.4%。机票价格尤其值得关注——石油相关压力仍在传导。\n\n3️⃣ 两个风险情景正在叠加\n研报提到两个推高通胀的情景正在同时发生：一是需求推动（消费和投资强劲），二是石油溢价持续（中东冲突延长）。如果冲突不解决，到年底核心PCE可能难以跌破3%。\n\n4️⃣ 消费有支撑但有限\n实际消费增速放缓，1Q26仅1.4%。工资增长不错，但通胀侵蚀购买力。财富效应显示消费已经高于财富隐含水平，储蓄率有上行风险。\n\n5️⃣ 原油库存持续下降\n美国原油库存（含战略储备）每天减少约200万桶。虽然期货价格因谈判预期下跌\n\n[... middle omitted ...]\n\nnderway.  \nHowever, a strong core PCE translation following PPI (0.36% m/m in May) indicates that the oil impulse to core persists—primarily through airfares.  \nThe extent of airfare payback—a\n\n[... middle omitted ...]\n\narantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n© 2026 MS"
  },
  {
    "id": "R005",
    "title": "JPM：MLCC市场低估的不是需求增长，而是有效供给的结构性收缩",
    "digest": "[wechat_article.md]\n# JPM：MLCC市场低估的不是需求增长，而是有效供给的结构性收缩\n\n这份JPM的最新研报做了一件多数投资者尚未完成的事：它不仅给出了一个MLCC（多层陶瓷电容）行业到2028年的供需模型，更在模型背后揭示了一个被忽视的底层逻辑——真正驱动行业进入新一轮上行周期的，不是AI服务器带来的需求增量本身，而是需求结构变化引发的有效供给收缩。当市场还在用“周期品”的框架审视这些被动元件厂商时，供给端的结构性变化正在重塑整个行业的盈利曲线。\n\n报告的核心判断清晰而有力：MLCC行业将从2025年的10%供给过剩，在2028年转为6%的供给短缺。这个转折的力度，按报告作者的测算，将超过2017-2018年的超级周期。而更值得深思的是，这份判断背后的逻辑链条，指向了一个与市场共识截然不同的方向。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 真正改变供给曲线的不是产能扩张，而是产品结构升级带来的“有效产能”损耗\n\n理解这份报告，首先要理解一个关键概念：有效产能。MLCC行业的名义产能过去十年保持了约10%的年增长，但这份研报明确指出，真正决定市场供需平衡的，是经过生产损耗和良率调整后的有效产能。而后者正在经历一个加速下滑的过程。\n\n原因在于AI服务器和汽车电子所需的MLCC，与消费电子所用的产品有本质区别。AI服务器需要的是大尺寸、高电容、高电压规格的MLCC，例如1005-47uf这类超高容值产品。这些产品的制造工艺要求使用侧隙构造法，其装配良率比普通MLCC低3到6倍。报告估计，这种产能惩罚对名义产能增长的负面冲击，在未来三年将从过去五年的低至中个位数百分比，加速至双位数百分比。\n\n这意味着什么？当市场看到MLCC厂商宣布扩产计划时，实际可用的产能增量可能远低于预期。这不是一个临时性的良率爬坡问题，而是由产品结构永久性升\n\n[... middle omitted ...]\n\n哪些关键假设可能被打破？哪些未被定价的二阶效应值得深入拆解？\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nMLCC 可能要缺货到 2028\n\nMLCC 供需拐点\n\n未来三年供给缺口持续扩大\n\n某外资投行最新研报指出，MLCC（多层陶瓷电容）行业正进入一个持续多年的供需紧张周期，预计到 2028 年会出现 6% 的供给缺口。核心驱动力来自 AI 服务器需求爆发。\n\n几个关键逻辑值得关注：\n\n1️⃣ **服务器是最大变量**\n单台 AI 服务器的 MLCC 用量是普通服务器的 6 倍以上，且仍在快速攀升。研报预测，服务器 MLCC 需求将从 2025 年的约 1500 亿颗增长到 2028 年的近 6300 亿颗，是行业增长的最大引擎。汽车和消费电子需求相对稳定，但整体采购节奏会因供给收紧而提前。\n\n2️⃣ **有效产能比名义产能更紧**\n行业名义产能过去十年年均增长约 10%，但实际有效产能增速远低于此。AI 服务器需要更高规格的 MLCC（如 1005-47uf 超高压产品），良率仅为常规产品的 1/3 到 1/6，导致产能“折扣”越来越大。研报认为，这个产能损耗因素被市场低估了。\n\n3️⃣ **价格和利润率有望提升**\n行业预计从 2025 年的 10% 供过于求，转向 2028 年的 6% 供不应求。类似 2\n\n[... middle omitted ...]\n\nife program led a procurement demand spike amid first cloud capex and then first-gen EV demand take-off cycle) and estimate high- $50\\%$ ASP growth during the same period (similar range of gro\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 12 Jun 2026 07:29 PM HKT\n\nDisseminated 12 Jun 2026 10:21 PM HKT"
  },
  {
    "id": "R006",
    "title": "NOM：3.5D封装竞争序幕拉开，真正的赢家不是台积电或英特尔，而是供应链的再组织者",
    "digest": "[wechat_article.md]\n# NOM：3.5D封装竞争序幕拉开，真正的赢家不是台积电或英特尔，而是供应链的再组织者\n\n这份NOM研报的核心判断，并非关于某个季度出货量的波动，而是指向一个更根本的结构性变化：半导体先进封装正在从“台积电主导的单一技术路线”转向“多技术路线竞争”格局。报告以4月封装基板出货数据为引子，但真正的洞察在于2028年将启动的3.5D封装量产竞争，以及这一竞争对供应链权力格局的深层含义。\n\n对于关注半导体产业链的投资者而言，当前市场可能过度聚焦于AI芯片本身的算力竞赛，而低估了后端封装技术路线分化所带来的供应链重构机会。NOM这份报告提供了一个关键的观察框架：谁能在3.5D封装时代成为供应链的再组织者，谁就将获得这一轮技术升级中最大的价值增量。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 4月封装基板出货回落是暂时扰动，暑期的真正放量才是观察窗口\n\nNOM报告披露的4月数据看似矛盾：出货金额同比增20%，但环比从3月的273亿日元降至233亿日元。按面积计算，出货量仅同比增1%，而每平米均价同比大涨19%至122.6万日元的历史新高。\n\n这一组合信号指向两个关键点：其一，价格持续上行说明高端封装基板的供需依然紧张；其二，量的环比回落可能与Rubin处理器的封装出货节奏有关——NOM判断，由于服务器生产被推迟，Rubin封装出货暂时放缓。报告明确指出，2025年4月正是Blackwell封装进入全速生产的时期，基数效应明显。\n\n更值得关注的是NOM对时间节点的判断：Rubin封装出货将在2026年夏季进入全速期，最早6月，最晚8月。这意味着当前的市场预期可能尚未充分计入这一轮放量带来的供应链压力。对于关注Ibiden等封装基板供应商的投资者，二季度末到三季度初的数据将是验证这一判断的关键窗口。\n\n![研报原图 2](\n\n[... middle omitted ...]\n\n和我们的详细解读，也期待听到你对3.5D封装竞争格局的判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n3.5D封装大战，2028见分晓\n\n封装赛道升温\n\n某外资投行最新研报显示，4月封装基板出货量同比增长20%，达到233亿日元。虽然环比3月有所回落，但每平米均价却创下历史新高——122.6万日元/平米。\n\n背后的逻辑很直接：Rubin处理器的封装出货暂时放缓，跟服务器生产推迟有关。但研报判断，Rubin封装将在2026年夏季（最早6月，最晚8月）进入全面放量阶段。\n\n1/ 3.5D封装将成为下一个战场\n\n2028年才是重头戏。台积电在股东大会上透露了两个关键时间点：\n- 2026年6月：面板级封装（CoPoS）试产线启动\n- 2028年：CoPoS量产，同时玻璃核心基板也开始准备量产\n\n3.5D封装本质上就是把加速器、HBM和小型推理芯片通过混合键合技术贴在一起。台积电的方案是SoIC+CoPoS+玻璃基板FC-BGA的组合拳。\n\n2/ Intel正在抢单\n\n有意思的是，Intel的EMIB-T技术也被用于3.5D封装。据The Information报道，Google已向Intel下单，计划2028年用EMIB-T封装至少300万颗TPU。Nvidia也在评估这项技术。\n\n不过研报也提醒：Ibiden目前\n\n[... middle omitted ...]\n\nm-m, to a record high of ¥1.226mn. Based on conditions in other supply chains, we think shipments of packaging for Rubin processors may have been temporarily sluggish because of the pushing ba\n\n[... middle omitted ...]\n\nation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Securities Co., Ltd., Japan. All rights reserved."
  },
  {
    "id": "R007",
    "title": "摩根斯坦利：MLCC市场真正被低估的不是需求总量，而是AI驱动下的价值迁移速度",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MLCC市场真正被低估的不是需求总量，而是AI驱动下的价值迁移速度\n\n这份来自摩根斯坦利日本电子元件团队的研报，在4月经济产业省数据公布后，做出了一个大胆的修正。它上调了2026至2028年全球MLCC出货金额预测，幅度之大值得每一位关注半导体供应链和AI硬件投资的读者停下来仔细推敲。\n\n报告的核心判断并非简单的“AI需要更多电容”，而是指向一个更结构性的变化：**小型大容量MLCC在AI/数据中心场景中的渗透，正在重塑整个行业的定价逻辑和竞争格局**。市场此前可能只看到了量的增长，却低估了价值迁移的速度和深度。\n\n这不仅仅是一份数据更新。它揭示了日本头部MLCC厂商（尤其是村田）如何在看似温和的单价下行趋势中，通过产品组合的跃迁，实现利润率的差异化。对于产业决策者和投资者而言，理解这一层“有量更有价”的叙事，远比跟踪月度出货数字重要。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 4月数据揭示了一个关键信号：出口金额增速远超产量，产品组合正在剧烈改善\n\n4月的数据本身存在一个有趣的矛盾。日本国内MLCC产值按美元计算同比下降了10.4%，但财务省的贸易统计却显示出口金额同比增长了16.0%。摩根斯坦利的分析师坦承，尚不完全清楚这一差异的原因。但更值得关注的是出口端的内在结构。\n\n出口金额的增长并非由数量驱动。4月MLCC出口数量同比增长10.4%，金额增速却高出近6个百分点。这意味着平均售价（ASP）在上升。以美元计，出口ASP同比上涨了5.0%，环比上涨了2.4%。在大中华区（占4月出口的57.7%），出口数量仅环比微增0.1%，但美元出口金额却增长了7.5%，ASP环比飙升了7.4%。\n\n这些数字合在一起，指向一个清晰的结论：**日本MLCC厂商正在向客户交付更贵的产品**。这不是涨价，而是\n\n[... middle omitted ...]\n\n里，我们可以基于这份报告的完整图表和假设，进行更深度的推演。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nMLCC需求正在悄悄转向\n\n小MLCC，大需求\n\nAI/DC正在拉动高端MLCC需求\n\n---\n\n最近看了某外资投行关于日本MLCC的最新研报，4月数据很有意思。\n\n4月日本MLCC出口金额同比+16%、环比+9.1%，但国内生产金额却同比-10.4%。一涨一跌的背后，是需求结构在变。\n\n1️⃣ AI/DC是主推手\n研报上调了2026年全球MLCC出货金额预测，从164.8亿→174.3亿美元（同比+18.8%）。核心原因是AI服务器和数据中心对小型大容量MLCC的需求持续扩张。新一代GPU需要更多大容量MLCC来应对空间限制。\n\n2️⃣ 产品组合在升级\n虽然同产品ASP还在温和下降，但整体ASP却因为高端产品占比提升而上涨。4月MLCC出口ASP同比+5.0%，环比+2.4%。大中华区（占出口57.7%）的ASP环比还涨了7.4%。\n\n3️⃣ 村田是领跑者\n研报特别提到村田在小尺寸大容量MLCC上的优势：DC电压下电容衰减小、高频稳定性好。这些特性让客户愿意为高品质产品付溢价。但风险在于，如果产能跟不上AI服务器需求的爆发，可能会丢失份额。\n\n4️⃣ 全球MLCC市场正在复苏\n从2021年174.7亿美元的\n\n[... middle omitted ...]\n\n7.43bn (+18.8% YoY).  \nDemand for small, large-capacity MLCCs for AI/DC use seems likely to continue expanding.\n\nCeramic capacitors (MLCCs): Apr output ¥70.9bn (-1.1% YoY, +12.0% MoM), with av\n\n[... middle omitted ...]\n\n><tr><td>Nippon Chemi-Con (6997.T)</td><td>U (09/20/2024)</td><td>¥4,175</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted."
  },
  {
    "id": "R008",
    "title": "JPM：铝市场的真正拐点不是霍尔木兹重启，而是“隐形库存”耗尽的那一刻",
    "digest": "[wechat_article.md]\n# JPM：铝市场的真正拐点不是霍尔木兹重启，而是“隐形库存”耗尽的那一刻\n\n这份JPM最新发布的铝业研报，读起来像一部悬念小说。市场普遍在等待霍尔木兹海峡重启，认为那将是铝价回归理性的转折点。但JPM大宗商品研究团队给出的判断恰恰相反：即便海峡在6月如期开放，中东冶炼厂恢复生产也需要一到两个季度，而在此期间，全球铝市场将经历一个从“隐形短缺”到“显性短缺”的质变过程。\n\n报告的核心主张是：铝市场真正的价格催化剂，不是供应中断本身，而是支撑市场至今的“隐形库存”正在耗尽。当这些藏在生产者、贸易商和消费者手中的库存再也无法填补供需缺口时，中国占全球75%的显性库存将成为下一个被消耗的对象。而这一过程，将推动LME铝价向4000美元/吨迈进。\n\n这不是一个简单的供需缺口故事。它涉及供应链的传导机制、套利窗口的动态博弈，以及一个正在发生的结构性变化——中国资本驱动的海外铝产能扩张，正在终结全球铝供应的长期纪律。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 市场的真实缺口比显性数据大得多，隐形库存正在充当缓冲垫\n\n当前全球铝市场的核心矛盾，存在于两组数据之间。JPM的供需平衡表显示，2026年全球原铝缺口高达170万吨，其中第二季度到第四季度累计隐含库存消耗达230万吨。但与此同时，全球显性铝库存——包括LME、COMEX、SHFE及中国社会库存——基本与2月底水平持平。\n\n这种“数据打架”的背后，是一个被市场低估的缓冲机制：隐形库存。这些库存包括中东生产商存放在亚洲、欧洲和美国的金属，也包括贸易商为避免LME高额仓租而持有的场外库存，以及消费者自身为应对供应链不确定性而保有的缓冲库存。\n\nJPM通过行业会议交流获得的关键反馈是：这些隐形库存目前仅剩约两个月的消耗能力。换句话说，市场正在用“看不见的粮食”度过最艰难的时\n\n[... middle omitted ...]\n\n对关键变量的更新跟踪，以及对报告完整图表和数据集的深度解读。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n铝的“隐形缺口”正在变成明牌\n\n铝缺口浮出水面\n\n某外资投行最新研报指出，全球铝市场正经历一个关键转折——过去靠“隐形库存”填补的供应缺口，接下来将逐步变成看得见的库存下降。\n\n1/ 缺口有多大？\n- 即便上调了中国供应预测，也假设中东铝厂下季度复产，研报仍预计2026年二季度到四季度出现超200万吨的铝缺口\n- 当前供应缺口靠“隐形库存”填补（包括生产商、贸易商和下游持有的未计入交易所的库存）\n- 但行业反馈显示，这些隐形库存只剩约2个月的缓冲空间\n\n2/ 为什么说缺口要“显形”？\n- 下半年还有近100万吨的缺口需要填补\n- 隐形库存见底后，缺口会传导至“可见库存”（全球约170万吨，中国占75%）\n- 中国社会库存本周已出现63万吨的周度降幅，为2023年12月以来最大\n\n3/ 对价格的传导逻辑\n- 中国库存持续下降 → 支撑沪铝价格走高\n- 海外需要中国铝产品出口来填补缺口 → LME价格必须维持高位，保持出口套利窗口打开\n- 这个套利博弈是下一阶段铝价的核心驱动\n\n4/ 关于中东复产\n- 即使霍尔木兹海峡重新开放，中东铝厂复产仍需数季度才能恢复正常\n- 这意味着缺口不会因为海峡开放而迅速消失\n\n5/\n\n[... middle omitted ...]\n\n 1 mmt that still needs to be covered in 2H26, the deficit should increasingly transmit into draws in visible inventory, which are heavily concentrated (75%) in China.  \n- A sustained, materia\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 12 Jun 2026 01:50 AM BST\n\nDisseminated 12 Jun 2026 08:30 AM BST"
  },
  {
    "id": "R009",
    "title": "摩根斯坦利：市场误读了2万亿数据中心投资，真正的瓶颈在芯片而非基建",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：市场误读了2万亿数据中心投资，真正的瓶颈在芯片而非基建\n\n一份未经官方确认的媒体报道，在6月9日引发了市场对国内数据中心和公有云板块的剧烈担忧。Bloomberg报道称，中国政府计划通过发改委在未来五年投入2万亿元人民币建设数据中心，并由电信运营商主导建设和运营。市场的第一反应是：供给过剩、竞争格局恶化、公有云厂商市场份额将被国企侵蚀。\n\n但摩根斯坦利在第一时间发布的这份研报，给出了一个与市场直觉完全不同的判断框架。我们仔细拆解了这份报告的核心逻辑后认为，市场真正需要关注的，不是2万亿数字本身，而是这个数字背后被误读的政策意图，以及中国AI产业链上真正卡脖子的环节。\n\n这份报告的结论值得每一位关注中国科技基础设施投资的读者认真对待：市场低估了政策文件的真实指向，高估了政府主导投资的规模，同时严重忽略了芯片供给才是中国AI发展的真正瓶颈。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 2万亿的出处并非数据中心建设，而是网络互联互通\n\n这份报告最关键的贡献，是厘清了媒体报道中那个2万亿数字的真实来源。摩根斯坦利团队明确指出，这个数字很可能指向的是2025年1月一份官方政策文件中的表述。该文件提到的是“数据基础设施建设将带动网络、算力和安全设施的建设和升级，预计五年内吸引投资2万亿元”。注意这里的用词是“吸引投资”，而非“政府直接投入”；是“带动网络和算力设施”，而非“数据中心建设”。\n\n更关键的是，这份政策文件所指向的投资方向，是数据中心之间的网络互联，而不是数据中心本身的物理建设。这意味着，2万亿这个数字如果确实存在，它的去向是光纤网络、高速互联、算力调度系统等基础设施，而不是新建大量的数据中心机房。\n\n从产业链角度看，这两者的含义截然不同。数据中心建设投资直接增加机柜供给，可能导致供过于求；而网络\n\n[... middle omitted ...]\n\n定义。只有把这些变量拆开来看，才能形成真正有意义的投资判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n2万亿数据中心投资传闻，真相是什么？\n\n数据中心投资传闻解析\n\n最近有个2万亿的新闻，我帮你拆清楚。\n\n某外资投行最新研报分析了6月9日彭博社报道——中国计划5年内投入2万亿建设数据中心。但研报指出几个关键点：\n\n1️⃣ 这个数字可能来自2025年1月的官方政策文件，但原文说的是“吸引投资”，不是政府直接投资。而且资金主要用于数据中心之间的网络连接，不是建数据中心本身。\n\n2️⃣ 中国AI发展的真正瓶颈是芯片设计和制造，不是数据中心基础设施。缺芯比缺机房更紧迫。\n\n3️⃣ 如果传闻属实，让三大运营商来建2万亿数据中心，反而会造成严重供给过剩，对现有数据中心玩家是重大利空。\n\n研报还提到，像阿里巴巴、字节跳动这类云厂商，靠供应链优势、自研芯片和模型能力，一直在从运营商手里抢市场份额。这个趋势不太可能逆转。\n\n说白了，传闻真假未定，但即使是真的，也未必是数据中心行业的好消息。\n\n欢迎一起讨论你对数据中心行业的看法。\n\n#学习笔记\n\n[source_mineru.md]\n## China Cloud and Data Centers | Asia Pacific\n\n# Our thoughts on potenti\n\n[... middle omitted ...]\n\nupply and market share loss to SOE telcos for both data centers and public clouds. However, to our knowledge, there has been no confirmation of this report from official channels yet.\n\nOur tho\n\n[... middle omitted ...]\n\n><tr><td>GDS Holdings Ltd (GDS.O)</td><td>++</td><td>US$33.76</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R010",
    "title": "摩根斯坦利：市场低估的不是CPO时间表，而是光学内容正在进入不可逆的倍增通道",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：市场低估的不是CPO时间表，而是光学内容正在进入不可逆的倍增通道\n\n最近几周，围绕共封装光学（CPO）与近封装光学（NPO）的讨论，让Lumentum、Coherent、Corning等光学标的经历了显著波动。市场似乎将注意力过度集中在“CPO何时量产”这一时间问题上，从而忽视了更根本的结构性事实：无论最终采用哪种架构，每颗GPU所需的光学引擎数量都在以数量级的方式增长。\n\n摩根斯坦利在6月12日发布的最新研报中，给出了一个清晰但被市场低估的核心判断——光学内容的增长与带宽需求强相关，与封装架构的选择无关。这意味着，即便CPO的规模化量产时间表存在不确定性，光学供应链的确定性需求依然在快速上升。对于正在经历回调的这些光学供应商而言，这恰恰是一个需要重新审视的窗口。\n\n这份报告的价值不在于它给出了CPO的精确时间表，而在于它提供了一个更底层的分析框架：把“架构之争”放在一边，先看“带宽需求”这条不可逆的主线。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 从每颗GPU 2个光学引擎到35个以上，增长路径已经清晰\n\n摩根斯坦利在报告中给出了一组极具说服力的数据对比。在当前基于可插拔收发器的架构中，每颗GPU仅配置2到4个光学引擎，主要用于scale-out网络。而在NVL576的混合架构中，当CPO被引入用于inter-rack scale-up流量时，每颗GPU的光学引擎附着率跃升至17个左右。若进一步演进到全光学配置，即GPU与网络交换机的连接也转向光子学，这一数字将升至35个。\n\n这还不是终点。报告指出，在未来的Feynman架构和Keyber机架架构中，如果SerDes速度提升至400G，光学引擎数量可维持在35个左右；但如果SerDes停留在200G，这一数字将可能翻倍至70个。换句话说，光\n\n[... middle omitted ...]\n\n的朋友一起，围绕这些尚未完全解答的关键变量，持续追踪和碰撞。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n光模块需求，不看架构看带宽\n\n**光模块需求，只看带宽**\n\n**不管CPO还是NPO，光模块需求都在涨**\n\n最近市场一直在争论近封装（NPO）和共封装（CPO）谁才是未来，但投行研报认为大家可能跑偏了。\n\n核心逻辑很直接：**光模块需求的核心驱动力是带宽，不是封装形式**。\n\n1️⃣ **数字不会说谎**\n- 当前：每GPU配2个光引擎\n- NVL576混合架构：17个/GPU\n- 全光CPO架构：35个/GPU\n- 远期Feynman架构（200G SerDes）：可能到70个/GPU\n每代架构升级，光引擎数量都是翻倍增长。\n\n2️⃣ **时间争议≠需求消失**\n现在市场纠结CPO量产时间（预计2028-2029年才大规模采用），导致相关公司股价波动。但研报认为这是暂时性问题——只要带宽需求在涨，光模块用量就在涨，只是时间早晚。\n\n3️⃣ **NPO是过渡，但不是终点**\nNPO把光模块放在封装外，良率更高、维护更容易，但长期看还是会走向CPO甚至片上光学。因为只有CPO才能解决I/O瓶颈和功耗问题。\n\n4️⃣ **当前CPO四大挑战**\n- 良率低：SoIC良率50-60%，组装良率20-50%\n- \n\n[... middle omitted ...]\n\njust NPO or OBO, the increase in optical content / lasers is driven by the need for more bandwidth.  \n■ More conservative assumptions on CPO adoption in 2028 likely keep stocks away from bull \n\n[... middle omitted ...]\n\ns Corporation (ZBRA.O)</td><td>E (12/02/2024)</td><td>$222.44</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "Figure 1",
    "context": "Figure 1: China green loans growth (y/y)"
  },
  {
    "figure_id": "F002",
    "report_id": "R001",
    "label": "Figure 2",
    "context": "Figure 2: China EV and ESS battery industry capacity utilization rate (based on designed capacity)"
  },
  {
    "figure_id": "F003",
    "report_id": "R001",
    "label": "Figure 3",
    "context": "Figure 3: China EV and ESS battery industry capacity utilization rate of the top 8 players"
  },
  {
    "figure_id": "F004",
    "report_id": "R004",
    "label": "Exhibit 1",
    "context": "Exhibit 1: The longer oil prices remain elevated, the greater the risk of second-round effects on core inflation."
  },
  {
    "figure_id": "F005",
    "report_id": "R004",
    "label": "Exhibit 2",
    "context": "Exhibit 2: A broad-based acceleration in payrolls so far this year Payrolls change, 000s"
  },
  {
    "figure_id": "F006",
    "report_id": "R004",
    "label": "Exhibit 3",
    "context": "Exhibit 3: The tariff pass-through may be near completion, but a prolonged conflict adds upside risks PCE cumulative tariff pass-through (pp)"
  },
  {
    "figure_id": "F007",
    "report_id": "R004",
    "label": "Exhibit 4",
    "context": "Exhibit 4: The pace of net wealth gains for households have slowed, and nominal consumption has been overshooting wealth-implied target levels Nominal consumption relative to model-implied target level (Bil $)"
  },
  {
    "figure_id": "F008",
    "report_id": "R004",
    "label": "Exhibit 5",
    "context": "Exhibit 5: There could be some upside risk to the saving rate, if the cyclical factors in the economy turn less supportive in 2H26"
  },
  {
    "figure_id": "F009",
    "report_id": "R004",
    "label": "Exhibit 6",
    "context": "Exhibit 6: US ending stocks of crude oil continue to move lower US Ending Stocks of Crude Oil and Petroleum Products, Thousands.Barrels"
  },
  {
    "figure_id": "F010",
    "report_id": "R004",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Prices of oil in the physical market remain elevated Crude Oil Spot Price FOB (US$ per Barrel)"
  },
  {
    "figure_id": "F011",
    "report_id": "R004",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Including the SPR, US oil stocks are falling about 2mn barrels per day"
  },
  {
    "figure_id": "F012",
    "report_id": "R004",
    "label": "Exhibit 10",
    "context": "Exhibit 10: US exports of oil and petroleum products have risen, pushing down net imports of these energy goods"
  },
  {
    "figure_id": "F013",
    "report_id": "R004",
    "label": "Exhibit 9",
    "context": "Exhibit 9: US domestic oil production remains broadly unchanged US Domestic Production of Crude Oil (Thous.Barrels per Day)"
  },
  {
    "figure_id": "F014",
    "report_id": "R004",
    "label": "Exhibit 11",
    "context": "Exhibit 11: US imports of oil have decelerated a little while exports have picked up"
  },
  {
    "figure_id": "F015",
    "report_id": "R004",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Financial conditions have tightened following the conflict in the Middle East MS FCI (Change since February 25, federal funds equivalent, bp)"
  },
  {
    "figure_id": "F016",
    "report_id": "R004",
    "label": "Exhibit 13",
    "context": "Exhibit 13: US effective tariff rate Spot Estimates of Tariff Announcements"
  },
  {
    "figure_id": "F017",
    "report_id": "R004",
    "label": "Exhibit 14",
    "context": "Exhibit 14: US Treasury: Customs and excise deposits from tariffs"
  },
  {
    "figure_id": "F018",
    "report_id": "R004",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Cash withdrawals from the DHS - CBP, as a proxy for tariff refunds Cash Withdrawals from DHS, CBP (Fiscal YTD, Bil $; 4-wk avg ann)"
  },
  {
    "figure_id": "F019",
    "report_id": "R004",
    "label": "Exhibit 16",
    "context": "Exhibit 16: The effect of incoming data on our US GDP tracking estimate Exhibit 17: GDP nowcasts"
  },
  {
    "figure_id": "F020",
    "report_id": "R005",
    "label": "Figure 1",
    "context": "Figure 1: MLCC industry revenue and y-y"
  },
  {
    "figure_id": "F021",
    "report_id": "R005",
    "label": "Figure 3",
    "context": "Figure 3: MLCC industry pricing and y-y"
  },
  {
    "figure_id": "F022",
    "report_id": "R005",
    "label": "Figure 5",
    "context": "Figure 5: MLCC industry revenue vs volume CAGR comparison ASP start to move up upon mix improvement and tightening S-D"
  },
  {
    "figure_id": "F023",
    "report_id": "R005",
    "label": "Figure 2",
    "context": "Figure 2: MLCC industry volume and y-y"
  },
  {
    "figure_id": "F024",
    "report_id": "R005",
    "label": "Figure 4",
    "context": "Figure 4: MLCC Revenue and OPM trend for the top 5 players"
  },
  {
    "figure_id": "F025",
    "report_id": "R005",
    "label": "Figure 6",
    "context": "Figure 6: MLCC content comparison by application"
  },
  {
    "figure_id": "F026",
    "report_id": "R005",
    "label": "Figure 7",
    "context": "Figure 7: MLCC content comparison by application for 2025E"
  },
  {
    "figure_id": "F027",
    "report_id": "R005",
    "label": "Figure 9",
    "context": "Figure 9: MLCC player's UTR trend"
  },
  {
    "figure_id": "F028",
    "report_id": "R005",
    "label": "Figure 8",
    "context": "Figure 8: MLCC industry bottoms-up OPM trend"
  },
  {
    "figure_id": "F029",
    "report_id": "R005",
    "label": "Figure 10",
    "context": "Figure 10: MLCC players' inventory days outstanding"
  },
  {
    "figure_id": "F030",
    "report_id": "R005",
    "label": "Figure 11",
    "context": "Figure 11: Long Term MLCC Supply-Procurement Gap trend"
  },
  {
    "figure_id": "F031",
    "report_id": "R005",
    "label": "Figure 12",
    "context": "Figure 12: MLCC industry bottom-up revenue and y-y trend US\\$bn"
  },
  {
    "figure_id": "F032",
    "report_id": "R005",
    "label": "Figure 14",
    "context": "Figure 14: MLCC Industry Bottom-up Wallet Share Comparison (Value) %"
  },
  {
    "figure_id": "F033",
    "report_id": "R005",
    "label": "Figure 13",
    "context": "Figure 13: MLCC industry bottom-up revenue y-y comparison for individual players"
  },
  {
    "figure_id": "F034",
    "report_id": "R005",
    "label": "Figure 15",
    "context": "Figure 15: MLCC top 5 auto MLCC sales mix (%) and Global auto MLCC unit sales mix (%) comparison"
  },
  {
    "figure_id": "F035",
    "report_id": "R005",
    "label": "Figure 16",
    "context": "Figure 16: OPM comparison between DRAM, NAND, MLCC and Substrate"
  },
  {
    "figure_id": "F036",
    "report_id": "R005",
    "label": "Figure 18",
    "context": "Figure 18: OPM comparison between MLCC players (2018 vs 2028E)"
  },
  {
    "figure_id": "F037",
    "report_id": "R005",
    "label": "Figure 17",
    "context": "Figure 17: Auto sales CAGR by MLCC players (22-25')"
  },
  {
    "figure_id": "F038",
    "report_id": "R005",
    "label": "Figure 19",
    "context": "Figure 19: MLCC OPM trends by players"
  },
  {
    "figure_id": "F039",
    "report_id": "R005",
    "label": "Figure 20",
    "context": "Figure 20: Past 3M Price Performance – SEMCO vs. MLCC Peers"
  },
  {
    "figure_id": "F040",
    "report_id": "R005",
    "label": "Figure 21",
    "context": "Figure 21: Past 12M Price Performance – SEMCO vs. MLCC Peers"
  },
  {
    "figure_id": "F041",
    "report_id": "R005",
    "label": "Figure 22",
    "context": "Figure 22: FTM P/B for MLCC peers over the past 15 years"
  },
  {
    "figure_id": "F042",
    "report_id": "R005",
    "label": "Figure 23",
    "context": "Figure 23: Average FTM P/B for MLCC peers over the past 15 years"
  },
  {
    "figure_id": "F043",
    "report_id": "R005",
    "label": "Figure 24",
    "context": "Figure 24: MLCC industry combined revenue vs. market cap trend"
  },
  {
    "figure_id": "F044",
    "report_id": "R005",
    "label": "Figure 25",
    "context": "Figure 25: MLCC industry combined OP vs market cap trend Mcap in US\\$bn, OP in US\\$mn"
  },
  {
    "figure_id": "F045",
    "report_id": "R005",
    "label": "Figure 26",
    "context": "Figure 26: MLCC industry combined OPM vs market cap trend Mcap in US\\$bn, % - RHS"
  },
  {
    "figure_id": "F046",
    "report_id": "R005",
    "label": "Figure 27",
    "context": "Figure 27: Murata market cap vs revenue trend Yen bn, Yen mn"
  },
  {
    "figure_id": "F047",
    "report_id": "R005",
    "label": "Figure 28",
    "context": "Figure 28: Taiyo Yuden market cap vs revenue trend Yen bn, Yen mn"
  },
  {
    "figure_id": "F048",
    "report_id": "R005",
    "label": "Figure 29",
    "context": "Figure 29: SEMCO market cap vs revenue trend"
  },
  {
    "figure_id": "F049",
    "report_id": "R005",
    "label": "Figure 30",
    "context": "Figure 30: Yageo market cap vs revenue trend"
  },
  {
    "figure_id": "F050",
    "report_id": "R005",
    "label": "Figure 31",
    "context": "Figure 31: Murata market cap vs MLCC OP trend"
  },
  {
    "figure_id": "F051",
    "report_id": "R005",
    "label": "Figure 33",
    "context": "Figure 33: SEMCO market cap vs MLCC OP trend"
  },
  {
    "figure_id": "F052",
    "report_id": "R005",
    "label": "Figure 32",
    "context": "Figure 32: Taiyo Yuden market cap vs MLCC OP trend"
  },
  {
    "figure_id": "F053",
    "report_id": "R005",
    "label": "Figure 34",
    "context": "Figure 34: Yageo market cap vs MLCC OP trend"
  },
  {
    "figure_id": "F054",
    "report_id": "R005",
    "label": "Figure 35",
    "context": "Figure 35: Murata market cap vs MLCC OPM trend"
  },
  {
    "figure_id": "F055",
    "report_id": "R005",
    "label": "Figure 36",
    "context": "Figure 36: Taiyo Yuden market cap vs MLCC OPM trend"
  },
  {
    "figure_id": "F056",
    "report_id": "R005",
    "label": "Figure 37",
    "context": "Figure 37: SEMCO market cap vs MLCC OPM trend"
  },
  {
    "figure_id": "F057",
    "report_id": "R005",
    "label": "Figure 38",
    "context": "Figure 38: Yageo market cap vs MLCC OPM trend"
  },
  {
    "figure_id": "F058",
    "report_id": "R007",
    "label": "Exhibit 2",
    "context": "Exhibit 2: MLCC export value and ASP"
  },
  {
    "figure_id": "F059",
    "report_id": "R007",
    "label": "Exhibit 3",
    "context": "Exhibit 3: MLCC export value and ASP (Narita)"
  },
  {
    "figure_id": "F060",
    "report_id": "R007",
    "label": "Exhibit 4",
    "context": "Exhibit 4: MLCC export value and ASP (Osaka)"
  },
  {
    "figure_id": "F061",
    "report_id": "R007",
    "label": "Exhibit 5",
    "context": "Exhibit 5: MLCC export value and ASP (KIX)"
  },
  {
    "figure_id": "F062",
    "report_id": "R007",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Major electric device shipments (annual) Note: $e =$ MS estimates Exhibit 8: Murata Mfg: Total production and inventories"
  },
  {
    "figure_id": "F063",
    "report_id": "R007",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Murata Mfg: Total production and inventories"
  },
  {
    "figure_id": "F064",
    "report_id": "R007",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Taiyo Yuden: Capacitor output and consol. inventories"
  },
  {
    "figure_id": "F065",
    "report_id": "R007",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Taiyo Yuden: Capacitor output and consol. inventories"
  },
  {
    "figure_id": "F066",
    "report_id": "R007",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Yageo monthly sales"
  },
  {
    "figure_id": "F067",
    "report_id": "R007",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Walsin monthly sales"
  },
  {
    "figure_id": "F068",
    "report_id": "R007",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Number of MLCCs per vehicle Exhibit 16: MLCC sales"
  },
  {
    "figure_id": "F069",
    "report_id": "R007",
    "label": "Exhibit 17",
    "context": "Exhibit 17: MLCC global market share"
  },
  {
    "figure_id": "F070",
    "report_id": "R007",
    "label": "Exhibit 18",
    "context": "Exhibit 18: MLCC global shipment value and volume"
  },
  {
    "figure_id": "F071",
    "report_id": "R007",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Nippon Chemi-Con & Nichicon aluminum capacitor sales"
  },
  {
    "figure_id": "F072",
    "report_id": "R007",
    "label": "Exhibit 20",
    "context": "Exhibit 20 Capacitor supply chain ```mermaid graph TD"
  },
  {
    "figure_id": "F073",
    "report_id": "R008",
    "label": "Figure 1",
    "context": "Figure 1: Global primary aluminum balance, quarterly"
  },
  {
    "figure_id": "F074",
    "report_id": "R008",
    "label": "Figure 2",
    "context": "Figure 2: JPM estimates for Middle East primary aluminum production, quarterly"
  },
  {
    "figure_id": "F075",
    "report_id": "R008",
    "label": "Figure 3",
    "context": "Figure 3: Regional aluminum ingot premiums"
  },
  {
    "figure_id": "F076",
    "report_id": "R008",
    "label": "Figure 4",
    "context": "Figure 4: Global visible aluminum inventories"
  },
  {
    "figure_id": "F077",
    "report_id": "R008",
    "label": "Figure 5",
    "context": "Figure 5: Chinese unwrought aluminum and aluminum product exports LHS: Thousand mt; RHS: Percent change, yoy"
  },
  {
    "figure_id": "F078",
    "report_id": "R008",
    "label": "Figure 6",
    "context": "Figure 6: Weekly change in China visible aluminum inventory (SHFE + regional warehouses). X-axis = weeks post Chinese New Year (week 0 = week closest to start of CNY), Y-axis = kt of aluminum increase / (decrease)"
  },
  {
    "figure_id": "F079",
    "report_id": "R008",
    "label": "Figure 8",
    "context": "Figure 7: Annualized Chinese quarterly primary aluminum production estimates"
  },
  {
    "figure_id": "F080",
    "report_id": "R008",
    "label": "Figure 8",
    "context": "Figure 8: Total visible China aluminum inventory (SHFE + regional warehouses) Y-axis: Thousand mt; X-axis: Weeks around Chinese New Year (0 = week closest to start of CNY)"
  },
  {
    "figure_id": "F081",
    "report_id": "R008",
    "label": "Figure 10",
    "context": "Figure 10: China aluminum semis & products export arb proxy (China to rest of Asia)"
  },
  {
    "figure_id": "F082",
    "report_id": "R008",
    "label": "Figure 11",
    "context": "Figure 11: Primary aluminium demand growth forecasts by region Percent change yoy"
  },
  {
    "figure_id": "F083",
    "report_id": "R008",
    "label": "Figure 12",
    "context": "Figure 12: Indonesian primary aluminium production by smelter, quarterly Thousand mt, annualised"
  },
  {
    "figure_id": "F084",
    "report_id": "R008",
    "label": "Figure 13",
    "context": "Figure 13: Global primary aluminum balance and supply and demand growth LHS: Thousand mt; RHS: Percent change, yoy"
  },
  {
    "figure_id": "F085",
    "report_id": "R010",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Optical Content Increasing, Discussion Is More Around Timing"
  },
  {
    "figure_id": "F086",
    "report_id": "R010",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Our CPO Forecast Was Short of Bullish Expectations, but Still Points to Meaningful Growth Opportunity"
  },
  {
    "figure_id": "F087",
    "report_id": "R010",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Preliminary Expectations from 650 Group Put Larger Opportunity as Scale-Up"
  },
  {
    "figure_id": "F088",
    "report_id": "R010",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Market Missing That Regardless of Timing, Optical Content Increasing"
  },
  {
    "figure_id": "F089",
    "report_id": "R010",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Assumptions and Calculations of Optical Engines (OEs) per Rack Architecture Exhibit 6: 6-7mm Optical Engines of Demand From 59K Switches in Model"
  },
  {
    "figure_id": "F090",
    "report_id": "R010",
    "label": "Exhibit 7",
    "context": "Exhibit 7: CPO Challenges CPO Market Trends & Challenges 2025 nVIDIA: First 1.6T CPO switch"
  },
  {
    "figure_id": "F091",
    "report_id": "R010",
    "label": "Exhibit 8",
    "context": "Exhibit 8: NPO Is Just a Path Towards Eventual CPO or Interposers Transition to Co-Packaged Optics Gen I: Pluggable Optics Chip-to-Module Links Pluggable Modules"
  }
]