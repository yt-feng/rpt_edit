请基于下面每天新报告的摘要，写一份“市场最新观点汇总”的结构化 JSON，用于生成 PDF。

要求：
1. 观点要分门别类，例如：宏观与利率、AI/算力、能源与大宗、地产与消费、区域市场、风险偏好等。类别由内容决定，不要机械套模板。
2. sections 建议 8-12 个，尽量覆盖所有报告 ID；references 合并后应覆盖大多数甚至全部报告。
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
    "title": "摩根斯坦利：市场真正低估的不是需求疲软，而是政策转向“供给端投资”的结构性含义",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：市场真正低估的不是需求疲软，而是政策转向“供给端投资”的结构性含义\n\n5月的经济数据，表面上看是“出口强、内需弱”的老故事，但摩根斯坦利这份最新研报揭示了一个更深层的信号：中国经济正在从“消费刺激依赖”转向“供给端投资驱动”，而这一转向的资产定价含义，远未被市场充分消化。\n\n二季度GDP跟踪值降至4.4%，零售销售自2022年以来首次转负，固定资产投资单月同比跌幅扩大至10.7%——这些数字本身已经足够令人警惕。但报告真正值得关注的判断，并非这些疲软数据本身，而是它们共同指向的一个政策拐点：北京正在加速放弃“以消费拉动经济”的短期路径，转而将筹码押注在AI算力网络、数据中心、智能电网等“六网”基础设施投资上。\n\n这不是一次简单的财政加码，而是一次增长逻辑的切换。理解这一切换，比预测下个月的经济数据重要得多。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 消费刺激的“天花板”已经提前到来，内需疲软正在从短期波动变成结构性特征\n\n5月零售销售同比下滑0.6%，不仅低于市场预期的-0.5%，更是2022年以来首次跌入负值区间。摩根斯坦利的分析指出，这并非单一因素所致，而是“以旧换新”政策效果递减与就业市场持续疲弱叠加的结果。\n\n值得注意的一个细节是，5月的“618”电商促销提前了一天启动，但零售数据依然转负。这意味着消费的疲软已经超出了短期促销可以拉动的范围。政策工具对消费的边际效用正在快速递减。\n\n报告进一步拆解了零售数据的内部结构：汽车销售同比下滑16.1%，住房相关消费下滑14.1%，黄金珠宝下滑8.9%。剔除以旧换新相关商品和黄金后的“核心商品零售”同比增长3.5%，虽然相对稳定，但这一增速也低于4月的4.2%。\n\n这些数字合在一起意味着什么？消费疲软正在从“周期性波动”演变为“结构性特征”。就\n\n[... middle omitted ...]\n\n告的完整数据，进一步拆解供给端投资的具体受益链条和风险边界。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n出口与消费温差拉大，二季度GDP怎么看？\n\n📊 经济“K型”分化加剧\n\n5月数据显示，经济正从“双速”走向更极端的“K型”分化：出口端生产强劲，但国内消费和投资明显走弱。\n\n1️⃣ 生产端：出口拉动，但传导有限\n工业增加值同比4.5%，略超预期。中下游生产受出口支撑，高端制造和高技术领域尤其亮眼。但产能过剩问题依然突出，制造业资本开支并未明显扩张，仅计算机设备等少数领域有传导。\n\n2️⃣ 消费端：首次转负，压力加大\n社会消费品零售总额同比-0.6%，为2022年以来首次负增长。“以旧换新”政策效果边际递减，就业市场持续疲软，连618电商大促也未能扭转颓势。\n\n3️⃣ 投资端：基建与地产双拖累\n固定资产投资单月同比-10.7%，基建投资大幅放缓至-10.8%，地产投资仍处-24.3%的深度收缩区间。前期财政前置发力的项目空窗期明显。\n\n4️⃣ 地产：回暖信号有限\n部分一线城市二手房成交改善，但新房销售、按揭增长依然疲弱，地产投资持续下滑。回暖可能只是局部现象，整体趋势尚未逆转。\n\n5️⃣ 政策展望：三季度或加大财政支出\n当前约60%的政府债券额度尚未使用，研报预计7月政治局会议将敦促加快财政支出节奏，而非推出新\n\n[... middle omitted ...]\n\ne 2022 (-0.6%; Consensus: -0.5%), due to faded trade-in effectiveness and continued job market weakness.  \nWe thus see 2Q real GDP tracking slightly $< 4.5\\%$ Y, increasing Beijing's urgency t\n\n[... middle omitted ...]\n\narantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n© 2026 MS"
  },
  {
    "id": "R002",
    "title": "GS：消费的真正压力尚未到来，市场对能源冲击的滞后效应严重低估",
    "digest": "[wechat_article.md]\n# GS：消费的真正压力尚未到来，市场对能源冲击的滞后效应严重低估\n\n过去几周，能源市场的消息面似乎正在转好。美伊临时和平协议降低了油价的上行尾部风险，GS的大宗商品策略师已将2026年第四季度布伦特原油预期从此前的每桶90美元下调至80美元。与此同时，大西洋两岸的消费者支出数据至今表现出了令人意外的韧性。这些信号叠加在一起，很容易让市场参与者产生一种判断——能源冲击对增长的影响已经见顶，风险正在消退。\n\n但这份来自GS全球经济学团队的最新报告给出了一个截然不同的结论。报告的署名作者包括首席经济学家Jan Hatzius，其核心判断非常清晰：现在放松警惕为时过早。真正的消费压力尚未到来，甚至可以说，主要冲击波还没有真正进入经济数据。\n\n市场低估的不是能源价格本身，而是能源冲击向消费者现金流传导的机制、时间差和季节性放大效应。这不是一个线性过程，而是一个在第二、三季度才会集中释放的滞后冲击。对于关注宏观资产定价、行业盈利预期和消费类资产基本面的投资者而言，理解这个传导链条的节奏，比盯着油价短期走势更为重要。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 三条传导路径的共振窗口将在下半年开启，而非现在\n\nGS的分析框架建立在三个相互独立的机制之上，它们共同指向同一个结论：消费的实质性放缓还没有开始。\n\n第一条路径是批发价格向零售价格的传导延迟。汽油价格在冲突爆发后迅速跳升，但天然气和电力价格向消费者的传导更为缓慢。GS欧洲经济学家指出，固定合同和政府监管机制在历史上一直导致消费端价格调整滞后于批发价格。这意味着，相当一部分相关的消费品价格涨幅尚未实现。\n\n第二条路径是季节性需求对现金流的放大效应。能源价格上涨对家庭现金流的冲击，在冬季取暖需求高峰时会显著放大。GS的报告用了一个非常精巧的计算来展示这一点：在固定消费结\n\n[... middle omitted ...]\n\n微信群里继续讨论。那里有更完整的原始图表和更深入的交叉验证。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n能源账单还没涨完，消费要小心了\n\n📉消费还没到底\n\n虽然最近油价回落，但某外资投行认为：消费压力还没释放完，后面还有三波💨\n\n1️⃣ 能源涨价还没完全传导\n汽油价格涨得快，但天然气和电费涨价慢，很多家庭还没感受到账单压力。研报预测，天然气和电价还会继续涨，尤其欧洲，很多国家有固定合同和价格管制，涨价会滞后。\n\n2️⃣ 冬天取暖需求会放大冲击\n欧洲冬天能源需求大，实际现金流影响会比数据更明显。算上季节性因素，欧洲2027Q1的现金流失血会比单纯看价格多14bp，美国也有5bp。\n\n3️⃣ 美国退税红利结束\n美国上半年因为退税多，现金流转好（Q1+0.8%，Q2+1.2%），但下半年这个红利没了，Q3可能直接掉到-0.6%。一正一负，落差很大。\n\n📊 历史规律：能源冲击导致现金流失血1%，2个季度后消费会下滑0.6%。按这个模型，加拿大消费可能拖累0.5%，欧元区0.4%，美国英国0.3%。而且美国还没开始跌，欧洲英国加拿大也只跌了一半。\n\n消费者自己也在说：未来6-12个月会减少大额购物。美国5月消费意愿已经回落。\n\n一句话：数据看着还行，但压力在后面。\n\n你们觉得接下来消费会怎么走？欢迎一起讨论。\n\n#学习笔\n\n[... middle omitted ...]\n\nasons why it is too early for complacency on real income and consumer spending in the coming months.\n\nFirst, while gasoline prices jumped shortly after the start of the war (and may ease follo\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R003",
    "title": "GS：中国家庭资产正在经历从房产到金融资产的结构性迁移",
    "digest": "[wechat_article.md]\n# GS：中国家庭资产正在经历从房产到金融资产的结构性迁移\n\n中国家庭资产负债表正在经历一个过去二十年从未出现过的变化：房地产从财富增长的引擎变成了拖累，而金融资产正在接替这一角色。这并非一个短期波动，而是一个结构性转折的早期阶段。\n\nGS在最新发布的研报中构建了一个季度频率的家庭资产负债表追踪框架，填补了官方数据发布滞后的空白。根据这一框架，中国家庭总资产在2023年初见顶，经历了约六个季度的收缩后，目前在730万亿元人民币左右企稳。但比总量企稳更值得关注的，是资产构成正在发生的根本性变化。\n\n截至2026年第一季度，GS估算房地产在中国家庭总资产中的占比已从2021年中房地产市场高峰期的67%降至52%，而现金及存款从16%升至25%，其他金融资产（含股票、债券、基金、保险等）从15%升至20%。直接持有的股票在总资产中的占比也从5%微升至6%。\n\n这些数字本身已经说明问题，但真正重要的是它们背后的含义：中国家庭的储蓄和财富配置正在经历一个从“不动产信仰”到“金融资产再平衡”的早期阶段。这一过程才刚刚开始，其对消费、资本市场乃至宏观经济的影响，可能比多数投资者预期的更为深远。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 房地产从财富创造者变为财富拖累，这一转变尚未被市场充分定价\n\nGS的数据显示，在2021年房地产见顶之前，中国家庭资产负债表持续扩张的核心驱动力是房价上涨和房产购买积累。当房价从高点下跌约30%后，这一逻辑彻底逆转。过去几年，房价下跌造成的资产减值超过了金融资产的增值，导致家庭总资产在2023年至2024年持续收缩。\n\n这一转变的核心含义在于：房地产不再是中国家庭财富增长的稳定器。过去二十年，买房几乎等同于“储蓄+投资”的合一体，而现在，它变成了一个需要持续消耗现金流来维护的负债项。即使房价\n\n[... middle omitted ...]\n\n疑问，也欢迎在群里提出，我们可以一起从原始数据出发推演答案。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国家庭资产正在“换锚”\n\n房产缩水，金融资产崛起\n\n某外资投行最新研报拆解了一个关键趋势：中国家庭资产负债表的资产结构正在发生结构性转变——从房产主导，转向金融资产。\n\n1/ 房产不再是增长引擎\n- 2021年地产高峰时，房产占家庭总资产67%，现金/存款16%，其他金融资产15%\n- 到2026Q1，房产占比降至52%，现金/存款升至25%，金融资产升至20%\n- 研报估算：家庭总资产在2023年初见顶，经历约6个季度下滑后，近期稳定在约730万亿人民币\n\n2/ 去杠杆还在继续\n- 家庭负债端：房贷余额和短期消费贷都在下降\n- 虽然债务/GDP比率看着还行，但债务/收入比率仍然很高，还贷压力不小\n- 政策端降了房贷利率、推消费贷贴息，但效果有限——劳动力市场弱+信心脆弱\n\n3/ 金融资产成新增长点\n- 2024年9月政策转向后，股市对金融资产增长的贡献明显提升\n- 但研报提醒：房产财富效应远大于股市——90%家庭有房，仅25%成年人炒股\n- 房价止跌更关键：一线城市新房和二手房价格已现企稳信号\n\n4/ 储蓄搬家进行时\n- 随着房产财富积累功能减弱、存款利率走低\n- 储蓄正逐步向更广泛的金融资产迁移\n- 中\n\n[... middle omitted ...]\n\nlook. With property a shrinking, although still dominant store of wealth, shifts in household assets and liabilities are now a key driver of confidence, consumption, and capital market perform\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R004",
    "title": "GS：油价传导的真正压力不在五月，而在接下来的几个月",
    "digest": "[wechat_article.md]\n# GS：油价传导的真正压力不在五月，而在接下来的几个月\n\n通胀数据正在讲述一个比表面更复杂的故事。澳大利亚四月CPI同比降至4.2%，环比仅微增0.4%，看起来通胀压力在缓解。但这份GS研报的核心判断是：五月的数据很可能掩盖了一个正在积聚的结构性风险——油价下跌带来的短期通缩效应，恰好与成本端持续上升的传导压力形成错位，真正的通胀读数将在未来几个月重新显现。\n\n市场容易犯的错误是线性外推。看到汽油价格单月下跌12.5%，就认为通胀压力消退。但研报揭示的逻辑链条恰恰相反：油价下跌是一次性的政策与地缘因素叠加，而材料成本、化工品价格、燃料附加费的传导才刚刚进入企业定价决策的窗口。这才是真正需要关注的信号。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 五月通胀读数中的“假摔”比想象中更明显\n\nGS对五月澳大利亚CPI的预测是环比下跌0.4%，同比维持4.2%不变。这个看似温和的数字背后，是极为特殊的结构性因素在起作用。\n\n汽油价格预计单月暴跌12.5%，这并非需求疲软所致，而是三个月临时燃油消费税减免政策的效果集中释放。与此同时，国内机票价格在复活节后季节性回落7.2%。这两项合计足以把整体CPI拉低约0.5个百分点。\n\n但剔除这些一次性因素后，核心指标反而在走强。GS预计五月截尾均值CPI环比上涨0.3%，同比从3.4%升至3.5%。更重要的是，其偏好的三个月对三个月截尾均值指标将升至0.88%季度环比——这个数字已经接近RBA关注的门槛。\n\n这意味着，如果只看五月整体CPI，你会得出通胀继续放缓的结论。但拆解后会发现，内生的价格压力不仅没有减轻，反而在加速。这是典型的“数据假摔”，也是这份报告最值得警惕的判断。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 材料成本\n\n[... middle omitted ...]\n\n中还有更详细的敏感性分析和情景推演，我们可以在群里继续拆解。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n澳新通胀最新信号：油价冲击正在传导\n\n油价转涨，通胀拐点要来了？\n\n澳新5月通胀数据：油价传导效应开始显现\n\n最近读了某外资投行关于澳新通胀的最新报告，信息量很大，直接上干货。\n\n澳大利亚4月CPI同比4.2%，比3月降了0.4个百分点。但别急着松口气，油价的影响正在悄悄蔓延。\n\n1/ 油价直接拉低通胀，但间接推高成本\n4月燃油价格环比下降，主要因为临时减税和补贴。但5月情况变了——全球油价下跌+减税到期，燃油价格预计跌12.5%。然而，油价下跌的好处还没完全传导到消费端。\n\n2/ 真正要警惕的是“间接传导”\n报告特别提到，5月油价上涨的间接影响会加剧，尤其是：\n- 新房购买：预计环比涨0.9%\n- 餐厅/外卖：预计各涨0.7%\n- 建材成本：管道材料供应商涨价数量已超过疫情后峰值\n\n3/ 核心通胀反而在涨\n剔除波动后，5月核心CPI预计环比涨0.3%，同比从3.4%升至3.5%。也就是说，去掉油价波动，通胀压力其实在加大。\n\n4/ 新西兰那边也在同步\n5月数据覆盖CPI篮子约50%，燃油和机票下跌被食品涨价抵消，尤其餐厅开始加收燃油附加费。\n\n5/ 租金和房价压力不减\n广告租金增速继续上行，新房价格因材料成\n\n[... middle omitted ...]\n\n In underlying terms, we expect monthly trimmed mean CPI to increase $0.3\\%$ mom, taking the year-over-year rate 10bp higher to $3.5\\%$ yoy. We flag a higher-than-usual degree of uncertainty i\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R005",
    "title": "Citi：市场真正低估的不是AI需求，而是国内“滞胀”的定价权转移",
    "digest": "[wechat_article.md]\n# Citi：市场真正低估的不是AI需求，而是国内“滞胀”的定价权转移\n\n理解当前中国经济的核心框架，已经从“复苏还是放缓”切换到了“K型分化如何定价”。Citi这份5月经济指标解读报告给出了一个锋利但容易被忽视的判断：AI超周期与国内滞胀正在成为两条平行叙事，而市场对前者的关注度远高于后者，这恰恰可能隐藏着更大的预期差。\n\n这份报告的核心洞察在于，它没有停留在“外需强、内需弱”的简单二分法，而是明确指出，国内需求侧正在经历一个自疫情以来首次出现的名义收缩——零售销售转负、固定资产投资降幅扩大，而CPI与PPI的组合却指向了滞胀风险。这不是一个短期波动，而是一个结构性信号：中国经济的“K”字，正在被AI出口和国内滞胀这两股力量拉得更开。\n\n对于产业决策者和投资者而言，理解这个框架比预测下个月的GDP数字更重要。因为这意味着，资产的定价逻辑正在发生根本性迁移——过去几年“内需复苏”的交易逻辑正在失效，而“AI供给”和“滞胀防御”将成为新的主线。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI超周期对工业生产的拉动已经超过50%，但这是“有产量、无需求”的繁荣\n\nCiti报告中最值得关注的数据点之一，是高新技术产业增加值同比增速达到15.1%，创下五年新高。更关键的是，按照该机构的估算，高技术产业在整体工业增加值中的占比约为17%，却贡献了超过50%的工业增长。集成电路产量同比增长22.9%，工业机器人增长27.9%，新能源汽车增长17.8%。\n\n这些数字本身并不令人意外，市场对此已有充分预期。真正值得推敲的是，这种增长的质量和可持续性。Citi报告提供了一个被很多人忽略的视角：销售-生产比率。5月份这一比率为96.1%，低于2023年和2024年同期的96.6%和96.5%。换句话说，生产端在加速，但销售端的消\n\n[... middle omitted ...]\n\n利润的影响如何量化？如果你也在思考这些问题，欢迎来继续交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI狂潮 vs 内需疲软，经济K型分化加剧\n\nAI拉动出口，内需却创疫后新低\n\n5月经济数据出炉，K型分化越来越明显。一边是AI超级周期拉动高科技生产创新高，另一边是国内消费和投资双双走弱，甚至出现疫后首次零售负增长。\n\n1️⃣ AI超级周期持续发力\n- 高科技产业增加值同比+15.1%，创五年新高\n- 集成电路产量+22.9%，工业机器人+27.9%，新能源车+17.8%\n- 电信设备制造投资同比+10.4%，知识产权投资+9.3%\n- 工业增加值同比+4.5%，超半数增长来自高科技领域\n\n2️⃣ 内需疲软信号加剧\n- 零售额同比-0.6%，疫后首次转负\n- 固定资产投资累计同比-4.1%，单月估算-10.7%\n- 以旧换新补贴退坡拖累明显：汽车-16.1%，家电-15.6%\n- 房地产投资继续收缩-16.2%，新开工-24.6%\n\n3️⃣ 滞胀风险上升\n- CPI温和+1.2%，PPI持续回升\n- 实际零售和投资增速均转负，创疫后新低\n- 中东冲突影响减弱，但石化产品价格压力仍在\n\n4️⃣ 政策展望\n- 7月政治局会议或聚焦消费和居民收入\n- 六网基建投资已启动，但见效需时间\n- 全面刺激概率不大，降息空\n\n[... middle omitted ...]\n\n and 4.7% YoY for 2026E. On policies, we see an acceleration of targeted support for domestic demand but not broad-based stimulus ahead. Investment-stabilization measures such as the “Six Netw\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R006",
    "title": "UBS：航运市场的真正拐点不在运价，而在供给侧的不可逆重置",
    "digest": "[wechat_article.md]\n# UBS：航运市场的真正拐点不在运价，而在供给侧的不可逆重置\n\n这份最新发布的UBS航运供应链周报，覆盖了截至2026年6月12日的高频数据。表面上看，它是一份常规的周度数据更新，涵盖了VLCC油轮、集装箱、干散货和造船四大板块。但如果你只是把它当作运价追踪来看，就会错过一个更重要的信号：全球航运市场正在经历一轮结构性重置，而这个重置的驱动力，不是短期需求波动，而是供给端的多项不可逆变化正在同时发生。\n\n霍尔木兹海峡的重新开放预期、红海绕航的持续、造船订单的集中爆发、以及集装箱运价的连续跳升——这些事件在市场上被分别讨论，但UBS这份报告将它们放在一起，揭示了一个更完整的图景：航运市场的定价逻辑，正在从“需求驱动”转向“供给约束驱动”。对于产业决策者和投资者来说，这意味着过去几年建立的分析框架需要重新校准。\n\n以下是我们从这份报告中提炼出的五个关键洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 霍尔木兹海峡的“重启”已被定价，但真正影响运价的不是通航，而是船队效率的永久性损失\n\n报告中最引人注目的数据点之一，是美伊和平协议签署后，油轮和航运股的反应积极。市场显然在押注霍尔木兹海峡重新开放后，VLCC运价将回归正常。但UBS的高频数据揭示了一个不同的现实：截至6月初，霍尔木兹海峡的原油油轮通行量仍比冲突前水平低95%，几乎处于冻结状态。\n\n更值得关注的是，即便海峡完全重启，船队效率的损失可能已经不可逆。过去一年，大量油轮被迫绕行好望角，这不仅拉长了航程，还改变了全球油轮的调度节奏。船东为了应对不确定性，已经调整了航线规划、船员配置和保险安排。这些调整一旦固化，即便地缘政治风险消退，船队也不会立即回到原来的效率水平。\n\n报告显示，VLCC平均收益目前仍低于10万美元/天，中东/西非至中国的VLCC收益保持平稳\n\n[... middle omitted ...]\n\n群里分享这份报告的原始图表和数据，并持续跟踪后续的高频更新。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n航运供应链周报：三大信号值得关注\n\n航运正在经历什么？\n\n上周航运市场有3个关键变化，值得研究参考。\n\n1️⃣ 油轮：霍尔木兹海峡重开，但运价还没完全恢复\n\n美伊和平协议后，霍尔木兹海峡宣布重开。但6月初的日均通行量仍远低于冲突前水平。VLCC从中东/西非到中国的平均收益基本持平，仍低于10万美元/天。油轮和油运股短期情绪回暖，但基本面恢复需要时间。\n\n2️⃣ 集装箱：运量稳增，运费继续上行\n\n中国主要港口集装箱吞吐量上周环比-1%，同比+5%。需求回暖推动主干航线运费进一步上涨：SCFI综合指数上周环比+9%，同比+43%。上海-欧洲航线环比+18%，跨太平洋航线环比+10-12%。亚洲到美国的集装箱运量自5月以来同比增速强劲。\n\n3️⃣ 干散货：BDI回落，但年初至今仍涨61%\n\n好望角型散货船平均收益上周环比-18%，BDI指数环比-10%。不过年初至今BDI累计涨幅仍有61%。造船新船价格指数环比持平，保持高位。\n\n总结一下：集装箱和干散货景气度仍在，油轮受地缘影响波动较大。霍尔木兹的恢复节奏值得持续跟踪。\n\n大家觉得下半年哪条航线最值得关注？欢迎一起讨论。\n\n#学习笔记\n\n[source_miner\n\n[... middle omitted ...]\n\nel transits through the Strait of Hormuz remained constrained in early June. VLCC average earnings from Middle East/West Africa to China remained flattish while earnings from US Gulf to China \n\n[... middle omitted ...]\n\ncom/sa/en/cssa.html.\n\n© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.\n\n![](images/df5252019e4cbd9f8094849ecd702c520a6ecefd13ad0c2993bf33cc18ec8a6e.jpg)"
  },
  {
    "id": "R007",
    "title": "摩根斯坦利：欧洲车企最坏的时刻尚未到来，中国OEM的份额侵蚀才刚刚加速",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：欧洲车企最坏的时刻尚未到来，中国OEM的份额侵蚀才刚刚加速\n\n这份来自摩根斯坦利欧洲与亚洲汽车团队的联合报告，试图回答一个正在被市场低估的问题：中国车企进军欧洲，究竟会给欧洲传统车企的盈利带来多大冲击？结论是明确的——共识预期仍然过于乐观，欧洲车企FY27的盈利还有超过10%的下行风险。但更值得关注的，不是这个数字本身，而是报告揭示的结构性变化：市场份额的流失正在从个别车企扩散到全行业，而欧洲车企的防御工事，可能比它们自己想象的要脆弱。\n\n市场当前对欧洲汽车股的定价，隐含了一个关键假设：过去几年中国车企在欧洲的份额增长已经趋于平稳，最激烈的竞争阶段已经过去。摩根斯坦利认为，这个假设是错的。报告通过拆解中国车企的产品布局、渠道扩张、本地化策略，以及欧洲各国市场的差异化渗透节奏，得出了一个更令人不安的判断：最坏的时刻尚未到来，中国车企的攻势才刚刚进入加速期。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 共识预期与现实的脱节：市场低估了份额流失的速度和广度\n\n报告最核心的量化结论是：欧洲OEM在EU5（德国、英国、法国、意大利、西班牙）的市场份额，将从2025年的67%进一步下滑至2027年的62%。这个数字本身或许看起来不算剧烈——五年间仅下降5个百分点。但关键在于，此前的份额流失（2020-2025年下降5个百分点）主要集中在Stellantis一家身上，其他欧洲车企的份额基本保持稳定甚至有所增长。而摩根斯坦利认为，接下来的5个百分点流失将更具“普惠性”，波及几乎所有欧洲车企。\n\n这意味着什么？此前市场可以将Stellantis的困境视为“个案”——一家整合不利、产品线老化、在意大利和法国本土市场受到冲击的特定公司。但中国车企正在实现从“点状突破”到“面状渗透”的转变。它们在英国、意大利、西班牙的\n\n[... middle omitted ...]\n\n的研报原文与原始图表，以及我们基于报告逻辑所做的进一步推演。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国车企正在欧洲“攻城略地”\n\n中国车企加速入欧\n\n一场正在发生的份额转移\n\n1️⃣ 欧洲车企的份额保卫战并不乐观。投行研报显示，2020-2025年，欧洲本土车企在EU5（德英法意西）的市场份额已从72%降至67%，预计到2027年将进一步滑至62%。压力远未结束。\n\n2️⃣ 中国车企的进攻路径非常清晰：主攻SUV、电动车和插混车型，瞄准入门级市场。雷诺首当其冲，因为其产品定价最贴近中国品牌的主战场。大众在主流SUV领域也面临直接竞争。\n\n3️⃣ 奔驰和宝马虽然暂时受益于高端定位，但中国品牌正在向上突破D-SUV和C-SUV细分市场。研报因此下调了奔驰2027年EPS预期-6%，宝马2026年EPS预期-4%。高端市场的价格战可能先于份额战到来。\n\n4️⃣ 市场共识可能过于乐观。尽管欧洲车企已经在降本、电池本地化、软件能力上积极追赶，但中国车企的本土化生产、经销网络扩张和极具竞争力的定价，正在让欧洲市场的竞争格局发生结构性变化。\n\n5️⃣ 短期看，中东局势缓和或关税谈判可能带来战术性反弹。但长期看，中国车企的全球化扩张才是决定欧洲汽车股走势的核心变量。研报维持对欧洲汽车板块的“中性”观点，建议精选个股。\n\n[... middle omitted ...]\n\nment exposure and (iii) European OEMs' defensive features, in order to quantify additional share transfer going forward. In our view, the worst is yet to come, and we still see $>10\\%$ downsid\n\n[... middle omitted ...]\n\ntd>Volvo (VOLVb.ST)</td><td>E (01/13/2026)</td><td>SKr 320.20</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R008",
    "title": "JPM：铁矿石定价权正在向澳大利亚矿商倾斜，而非中国需求主导",
    "digest": "[wechat_article.md]\n# JPM：铁矿石定价权正在向澳大利亚矿商倾斜，而非中国需求主导\n\n这份来自JPMEMEA金属与采矿团队的周度渠道检查报告，表面上是在追踪中国钢铁产量的短期高频数据，但真正值得关注的信号隐藏在运费结构的变化之中。报告覆盖了截至6月10日的中国钢铁产出、铁矿石海运成本、港存变化以及钢厂利润动态，但其核心洞察并非关于中国需求是否疲软，而是关于全球铁矿石供给侧的竞争格局正在发生一次微妙但重要的再定价。\n\n过去一周，从澳大利亚到中国的铁矿石散货运费骤降22%，至每吨10.9美元。与此同时，巴西和南非至中国的运费虽然也录得周度环比下降，但依然高于冲突前水平超过50%。这两个事实放在一起，意味着澳大利亚矿商正在获得显著的物流成本优势，而巴西和南非的生产商则面临持续的利润率压力。JPM据此对英美资源集团和库博铁矿给出了明确的Underweight评级，对必和必拓的澳大利亚上市主体和力拓有限公司则维持Overweight。\n\n这不是一份关于中国钢铁需求触底的报告。这是一份关于全球铁矿石供应链如何在运费波动中重新分配利润的报告。市场如果仅仅关注中国产出数据，很可能低估了供给侧结构性差异对资产定价的影响。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 中国钢铁产出并未超预期，但市场对“需求见底”的叙事需要更谨慎\n\n报告最直观的数据是：截至6月10日的10天中国日均粗钢产量年化约10.18亿吨，较前一个10天周期环比增长4%，同比增长2%。这一水平处于过去五年区间的下沿。乍看之下，这似乎支持了“中国钢铁需求正在企稳”的判断，但JPM并没有给出乐观结论。\n\n关键问题在于，产出增长更多是季节性因素驱动，而非需求实质性复苏。报告提到，过去30天的滚动产量较前30天仍为环比下降1%，同比仅增长1%。更重要的是，中国钢铁出口在5月的年化运行率已\n\n[... middle omitted ...]\n\n和出口数据的边际变化，并分享更多来自全球投行的独家研报解读。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国钢铁产量微增，海运成本骤降\n\n钢铁产量微增，海运成本骤降\n\n6月数据透露了什么信号？\n\n---\n\n最近看到某外资投行一份中国钢铁行业研报，几个数据点很有意思，分享给大家一起看看。\n\n**1/ 产量小幅回升，但仍在低位**\n6月上旬中国粗钢产量年化约10.18亿吨，环比上旬+4%，同比+2%。不过近30天滚动产量环比-1%，整体处于5年区间下沿。说明钢厂复产节奏比较克制，没有大幅放量。\n\n**2/ 海运成本暴跌，澳大利亚到中国跌22%**\n本周最值得关注的数据：澳中航线散货运费降至10.9美元/吨，环比-22%（-3美元/吨）。巴西和南非到中国的运费也降了3%。这意味着澳大利亚FOB铁矿石价格约90美元/吨，比2月底（美伊冲突开始时）还高了4%。\n\n但注意：巴西和南非的运费仍比冲突前高出50%以上，这对澳大利亚矿商更有利。\n\n**3/ 矿石库存高位，但已从3月峰值回落**\n中国港口铁矿石库存约1.6亿吨，处于历史高位，但比3月峰值已减少700万吨。库存缓慢去化中。\n\n**4/ 钢厂利润承压，焦煤涨价是主因**\n最近几周中国钢厂利润继续收窄，主要因为焦煤价格上涨。热卷和螺纹钢的利润都在走低。\n\n**5/ 出口\n\n[... middle omitted ...]\n\nhipping costs; rates from Australia, Brazil and South Africa to China all saw declines week-on-week. Australia to China bulk freight rates are now quoted at \\$10.9/t, -22% WoW (-\\$3/t) and bot\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 16 Jun 2026 08:36 AM BST\n\nDisseminated 16 Jun 2026 08:36 AM BST"
  },
  {
    "id": "R009",
    "title": "Bernstein：SOCAMM2不会侵蚀内存接口芯片市场，市场高估了替代风险",
    "digest": "[wechat_article.md]\n# Bernstein：SOCAMM2不会侵蚀内存接口芯片市场，市场高估了替代风险\n\nNVIDIA最新发布的ARM架构服务器CPU Vera采用了名为SOCAMM2的新型内存封装格式。这一变化引发了一个关键问题：如果SOCAMM2成为主流，内存接口芯片的总可寻址市场将显著缩小，因为其每模块的接口芯片价值仅为数美元，远低于DDR5 MRDIMM的50至70美元。投资者对澜起科技和瑞萨电子的担忧并非没有道理。\n\n但Bernstein这份最新研报给出了一个清晰且反直觉的判断：SOCAMM2大概率将局限于NVIDIA自身生态，不会对更广泛的服务器内存接口芯片市场构成实质性威胁。市场真正需要关注的，不是SOCAMM2本身，而是它揭示的一个更深层结构性趋势——AI服务器架构正在从“通用标准”走向“垂直整合”，而这一变化对不同参与者的含义截然不同。\n\n这份报告的核心价值不在于技术细节的罗列，而在于它提供了一个区分“短期噪音”与“长期结构”的分析框架。对于持有或关注澜起科技、瑞萨电子的投资者而言，真正需要判断的不是SOCAMM2的技术优劣，而是它能否跨越NVIDIA的围墙，进入x86和其他ARM生态。Bernstein的答案是否定的，且给出了令人信服的论据。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. SOCAMM2本质上是NVIDIA的全栈优化工具，而非颠覆性的行业标准\n\nSOCAMM2并非凭空出现。它是NVIDIA从Grace到Vera架构演进中，为解决特定问题而设计的定制化方案。Grace CPU采用焊接式LPDDR5x，虽然能效出色，但无法现场升级或更换——一旦内存故障或容量需求变化，整块主板必须更换。SOCAMM2通过可拆卸的模块化设计解决了这一痛点。\n\n然而，这种设计的优势高度依赖于NVIDIA的机架级优化逻辑。在\n\n[... middle omitted ...]\n\n可能性。这些问题的答案，将直接影响你对这两个标的的估值判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nNVIDIA新内存包，影响有限\n\nSOCAMM2，别慌\n\n对内存接口芯片影响不大\n\n最近NVIDIA发布了新ARM服务器CPU Vera，搭载了新型内存封装SOCAMM2。这个新包用的内存接口芯片很少，所以有投资者担心会减少澜起科技和瑞萨的市场空间。\n\n1/ 先说结论：SOCAMM2大概率只是NVIDIA的专属方案，不会成为主流标准。它对整个内存接口芯片市场的影响，大概只有低个位数百分比，不用太紧张。\n\n2/ SOCAMM2本质是NVIDIA定制的DRAM封装，不是颠覆性标准。从Grace的焊接LPDDR5x到Vera的可插拔SOCAMM2，确实提升了灵活性和容量带宽。但它的优势主要服务于NVIDIA的机架级优化——追求每瓦性能最大化。\n\n3/ 和其他方案比，SOCAMM2有硬伤。对比MRDIMM，它在容量和带宽上都有差距（MRDIMM最高1.6TB/s带宽和16TB容量，SOCAMM2只有1.2TB/s和1.5TB）。x86和其他ARM CPU厂商已经深度绑定DDR生态，切换成本太高。\n\n4/ 对接口芯片供应商的经济影响有限。SOCAMM2每个模块的芯片价值只有几美元，远低于MRDIMM的50-70美元。但\n\n[... middle omitted ...]\n\n9766463803f75c6cc9eb15f348047f.jpg)\n\nKai Zhang\n\n+852 2123 2665\n\nkai.zhang@bernsteinsg.com\n\nNvidia recently released their latest ARM-based server CPU called Vera, in which they used a new memo\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R010",
    "title": "DB：市场低估了资本账户对人民币的支撑力",
    "digest": "[wechat_article.md]\n# DB：市场低估了资本账户对人民币的支撑力\n\n人民币汇率正在经历一个罕见的“结构分化”阶段。出口商结汇意愿连续三个月下降，但人民币并未因此走弱——真正支撑汇率的，是来自债券市场的资本账户流入。DB在6月16日发布的这份报告中，用一组数据揭示了这一变化：过去两个月，证券投资净流入增加了180亿美元，是2021年以来最大规模的连续流入。其中约72亿美元已在即期市场结汇，直接构成对人民币的买盘。\n\n这个信号之所以值得关注，是因为它指向一个正在发生的结构性切换：人民币汇率的定价逻辑，正在从“贸易顺差驱动”向“资本账户驱动”转变。而市场对人民币的定价，可能仍然停留在旧框架里。\n\n这份报告的核心价值，不在于预测人民币会涨到多少，而在于它提供了一个理解汇率的新坐标。当出口商开始囤积美元，而外资开始买入人民币债券，这两股力量同时作用，意味着什么？以下是我们从报告中提炼出的五个层次洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 出口商结汇意愿连续下降，但这不是人民币走弱的信号\n\n报告引用的国家外汇管理局数据显示，5月出口企业结汇比率降至62.6%，连续第三个月下滑，较3月的67.5%下降了近5个百分点。直观理解，出口商在持有更多美元而不愿结汇，通常意味着对人民币前景的谨慎。\n\n但DB的分析没有止步于此。他们注意到，尽管结汇率下降，客户端的美元净卖出量却连续三个月增加，累计约400亿美元。这说明，推动美元卖出的力量已经从出口商切换到了其他参与者。\n\n一个合理的推论是：出口商之所以犹豫，是因为全球不确定性上升和进口成本增加，使得他们更倾向于保留美元头寸以应对潜在风险。这不是对人民币的看空，而是一种防御性操作。如果未来不确定性消退，这部分被压抑的结汇需求可能成为人民币的额外支撑。\n\n这里的关键判断是：结汇率的下降本身，不等于人民\n\n[... middle omitted ...]\n\n人民币汇率的底层逻辑变化感兴趣，这里可能是最适合你的讨论场。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n人民币背后两股力量在切换\n\n出口商结汇减速\n资本账户却在回暖\n\n最近投行研报拆了5月外汇数据，发现一个有意思的切换。\n\n1️⃣ 出口商结汇意愿连续3个月下降\n5月出口商外汇结汇比例降到62.6%（3月是67.5%）。全球不确定性+进口成本上升，企业更愿意持有美元而不是换回人民币。\n\n2️⃣ 但资本账户开始发力\n资本账户连续第二个月净流入，5月增量180亿美元（2021年以来最大单月），其中约72亿在境内即期市场换成了人民币。\n\n3️⃣ 外资重新买入中国债券\n5月外资净买入约130亿美元中国债券，是2025年4月以来首次净买入。中债今年表现强势，全球配置对中国债券仍偏低，后续流入可能持续。\n\n4️⃣ 对人民币形成支撑\n资本账户流入+地缘风险潜在缓和，构成了人民币的正面逻辑。\n\n一边是出口商捂美元，一边是外资重新入场。这两股力量谁主导，决定了后续方向。\n\n#学习笔记\n\n[source_mineru.md]\n## Foreign Exchange\n\n## Asia Chart Alert\n\n# RMB: Exporters' FX conversion slowing but portfolio flows pic\n\n[... middle omitted ...]\n\ng import costs.\n\nThe real surprise comes from the capital account, which has experienced a return in portfolio inflows for the second consecutive month. SAFE's net FX receipt and payment data \n\n[... middle omitted ...]\n\n8000</td><td>DB Securities Inc.The DB Center1 Columbus CircleNew York, NY 10019Tel: (1) 212 250 2500</td><td>DB AGFiliale SingapurOne Raffles Quay, SouthTowerSingapore 048583Tel: (65) 6423 8001</td><td></td></tr></table>"
  },
  {
    "id": "R011",
    "title": "NOM：亚洲央行正在用外汇储备为货币信心买单，但印尼和印度的弹药已接近红线",
    "digest": "[wechat_article.md]\n# NOM：亚洲央行正在用外汇储备为货币信心买单，但印尼和印度的弹药已接近红线\n\n2026年5月的数据，揭示了一个被市场普遍忽视的结构性变化：亚洲新兴经济体的外汇储备消耗，已经从“周期性防御”转向“结构性失血”。\n\nNOM在6月17日发布的亚洲外汇策略报告中，给出了一个值得所有关注新兴市场资产定价的投资者认真审视的结论——印度尼西亚央行和印度储备银行在5月以极为激进的力度抛售美元以支撑本币，其外汇储备消耗速度已经触及甚至突破了IMF框架下的警戒线。与此同时，中国央行却在逆向买入美元，以阻止人民币过快升值。\n\n这不是一个关于“谁在贬值”的简单叙事。这是亚洲经济体在美元周期尾部出现的根本性分化：那些经常账户赤字、外资依赖度高、外债负担重的国家，正在用不可再生的储备资产为汇率稳定买单；而那些拥有庞大经常账户盈余和资本管制能力的国家，则拥有在美元走弱时主动管理汇率节奏的奢侈。\n\n这份报告最核心的洞察在于：市场对亚洲货币的定价，可能低估了“储备消耗”这一供给侧的硬约束。当印尼央行的外汇储备充足率在扣除短期负债后降至46%，当印度央行在2026年前五个月已经消耗了近9%的2025年末外汇储备，继续干预汇市的能力和意愿都将面临严峻考验。这不仅仅是汇率波动的问题，它可能倒逼出更激进的货币政策行动——就像印尼在4月的非周期加息，以及印度针对外币存款推出优惠掉期安排所预示的那样。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 印尼和印度在5月的干预力度远超市场感知，储备消耗已进入“不可持续”区间\n\nNOM通过拆解各国央行公布的储备变动、估值效应、远期头寸调整等复杂因素，估算出5月份各央行的实际外汇干预规模。结果呈现出一个清晰的“双峰”格局：印尼央行和印度央行是绝对的干预主力，而其他亚洲经济体则相对克制。\n\n印尼央行在5月份\n\n[... middle omitted ...]\n\n讨论。欢迎有兴趣的读者加入，一起推演这些关键变量的演变路径。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n📌亚洲央行外汇储备5月大分化\n\n谁在疯狂卖美元？\n\n---\n\n5月亚洲外汇市场很有意思，各国央行操作截然不同。\n\n1️⃣ **印尼央行和印度央行：猛卖美元**\n印尼央行5月卖出约48亿美元（占储备3.9%），印度央行卖出115亿美元（占储备2.1%）。两国的货币都创了历史新低——美元/印尼盾到17887，美元/卢比到96.97。卖得这么猛，储备够不够用？研报显示印尼储备充足率仅90%，扣除短期负债后只剩46%，压力不小。\n\n2️⃣ **韩国央行：相对克制**\n韩元贬值压力在增加，但韩国央行5月只卖了约14亿美元（占储备0.4%）。很有意思，压力大但干预少，可能是在等更好的时机。\n\n3️⃣ **中国央行：反向操作**\n人民币5月对美元升值约0.9%，是亚洲表现最好的货币之一。央行反而净买入约287亿美元外汇储备，加上国有银行又存了109亿美元，合计增持约396亿美元。这是在主动放缓人民币升值节奏。\n\n4️⃣ **其他央行：基本按兵不动**\n新加坡、泰国、台湾央行储备变化很小，因为它们的货币相对稳定。\n\n📊 一个关键观察：印尼央行今年以来已经用了15.7%的外汇储备来干预市场，印度央行用了8.9%。这种消耗速度能\n\n[... middle omitted ...]\n\nFX swap for FCNR(B) deposits, respectively.  \n- BOK's spot FX/USD selling intervention was rather limited, even as KRW depreciation pressures mounted.  \n- The PBoC, MAS, BOT and CBC accumulate\n\n[... middle omitted ...]\n\nrmation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R012",
    "title": "Bernstein：中国生物医药被低估的不是创新能力，而是“全球价值转化”面临的真实阻力",
    "digest": "[wechat_article.md]\n# Bernstein：中国生物医药被低估的不是创新能力，而是“全球价值转化”面临的真实阻力\n\n过去一个月，港股和A股生物医药板块经历了一轮显著回调。市场的主流解读是“政策恐慌”——美国《生物安全法》推进、COINS/BINSA法案提出、以及中国国内反腐行动重启，三重压力叠加。但Bernstein在最新发布的这份研报中提出了一个更值得深思的判断：**市场定价反映的并非政策恐慌本身，而是对“中国创新药全球价值转化路径”的一次根本性重估。**\n\n这轮下跌不是情绪驱动的短期波动，而是投资者在追问一个此前被忽视的问题——中国药企的早期研发优势，究竟有多少能真正转化为全球商业回报？答案取决于一整套正在收紧的制度安排，而市场目前可能定价了过于悲观的极端情景。\n\n这份研报的价值，不在于罗列政策清单，而在于它为这个问题搭建了一个分析框架：从研发管线、交易结构到情景假设，层层拆解“价值转化”这一核心变量。以下是我们从中提炼出的五个关键洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 中国在早期研发中的角色已不可逆，但“前重后轻”的结构性矛盾才是真正瓶颈\n\nBernstein的数据显示，中国在全球早期药物开发中的占比已经相当可观：约30%-40%的临床前项目、约50%的早期临床管线、以及2026年至今约55%的首次临床试验注册来自中国。这组数字直观地说明，中国生物医药的“创新供给”能力已经完成了质的跃迁。\n\n然而，这种增长并未等比转化为后期阶段的全球存在感。中国原研资产在美国三期临床试验中的占比仍低于10%，FDA批准占比不到5%，美国商业销售额仅约1%。报告将这一落差归结为两个因素：一是时间滞后——近年加速的对外授权交易才刚刚开始进入美国后期管线；二是竞争力差距——美国FDA的审评标准和全球竞争强度，意味着比国内市场环境更高的\n\n[... middle omitted ...]\n\n时可能被修正，比简单判断“该买还是该卖”更为重要。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国生物科技，被低估了吗？\n\n全球创新药，中国供应链\n\n中国占全球早期管线30-50%，但FDA获批不到5%\n\n最近某外资投行出了一份深度研报，把中国生物科技的政策环境和估值逻辑讲得很透。我帮你拆成3个核心点👇\n\n**1. 政策在收紧，但不是“一刀切”**\n美国那边，从Biosecure Act到BINSA法案，核心目标是限制资本流动和数据访问。但研报认为，完全封锁是低概率事件，更可能的是“摩擦增加但合作继续”。国内政策反而偏正面，比如新药定价允许更高、罕见病7年市场独占期。\n\n**2. 中国创新药的真实位置**\n中国现在占全球早期研发的30-50%（临床前到早期临床），但到美国三期临床的不到10%，FDA获批不到5%，美国销售额只有1%。研报说，这不是能力问题，是时间差和转化率问题——资产生成能力强，但全球价值转化能力还在爬坡。\n\n**3. 估值到底敏感在哪？**\n研报做了情景分析：\n- 间接进入（通过欧盟、日本合作）：BD收入跌50%，全球峰值销售跌20%\n- 完全封锁：BD收入跌80%，全球销售跌60%\n某些全球暴露度高的公司（信达、恒瑞、翰森）可能跌50%，但科伦博泰因为核心产品sac-TMT已在美国\n\n[... middle omitted ...]\n\n, COINS/BINSA) increasingly target the full stack: capital flows, data access, licensing, and supply chains. While implementation remains staged, the direction is unambiguous and calls for red\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R013",
    "title": "UBS：中东局势缓和下，化工板块的真正机会不在油价，而在成本端的重新定价",
    "digest": "[wechat_article.md]\n# UBS：中东局势缓和下，化工板块的真正机会不在油价，而在成本端的重新定价\n\n市场当前正在消化一个关键信号：美国与伊朗就霍尔木兹海峡重新开放达成协议。这一事件的影响远不止于油价本身。UBS最新发布的每周跟踪报告给出了一个值得产业决策者反复推敲的判断——如果局势快速缓和，布伦特原油价格在2026年第三季度平均可能回落至85美元/桶。但这份报告最有价值的洞察，并非油价预测，而是它揭示了化工板块内部正在发生的结构性分化：哪些公司会在成本端受益，哪些公司反而可能面临短期压力。\n\n对于化工行业投资者而言，当前需要回答的核心问题不是“油价会跌多少”，而是“当油价回归常态，哪些企业的盈利弹性被市场低估了”。UBS的报告为此提供了清晰的观察框架。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 成本端压力缓解带来的受益者，比市场想象的要更集中\n\nUBS在报告中明确列出了受益于地缘政治缓和的化工企业类型。第一类是受原材料价格影响较大的公司，包括涤纶长丝（桐昆）和磷化工企业。这背后的逻辑并不复杂：这些企业的成本结构中，原油或原油衍生物占比较高，油价回落直接意味着成本下降。\n\n但值得注意的，并非所有成本敏感型企业都会同等受益。报告给出了一组重要的运营数据作为参照：上周中国PTA开工率环比上升2个百分点至65%，而涤纶长丝开工率环比下降4个百分点至76%。这意味着下游需求端并未同步回暖。如果仅仅因为油价下跌就买入化工股，可能会忽略需求端的疲软。真正的受益者，必须是那些成本下降速度快于产品价格下降速度的企业。UBS的报告实际上在提醒：成本端受益，不等于利润端受益，中间还有一条“需求传导链条”需要验证。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 龙头企业的重新定价机会，可能被地缘政治噪音掩盖\n\n[... middle omitted ...]\n\n与产业界和投资界的同行一起，对这些关键问题进行更细致的拆解。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中东局势降温，化工板块怎么看\n\n**化工板块的潜在机会**\n\n中东局势出现缓和信号，美伊达成协议将重开霍尔木兹海峡。投行研报指出，若局势快速解决，Q326布伦特原油均价或回落至85美元/桶。这对化工板块意味着什么？👇\n\n1️⃣ **油价预期回落，成本端压力减轻**\n- 原油供应恢复预期下，油价可能先跌后稳，需求端支撑仍在\n- 国内炼厂开工率分化：国企降0.6ppt至67.18%，地炼降2.5ppt至48.6%\n- 原油库存下降1600万桶至12.8亿桶\n\n2️⃣ **化工品开工率涨跌互现**\n- MDI开工率周环比大涨9ppt至83%，表现亮眼\n- 聚酯长丝开工率降4ppt至76%，涤纶库存周环比降16%\n- PE/PVC库存周环比均降1%，去库趋势延续\n\n3️⃣ **哪些方向值得关注？**\n- 受益于原料降价：涤纶长丝、磷化工\n- 有估值修复潜力的龙头：MDI、农药相关企业\n- 替代工艺路线（如MTO制烯烃）短期或承压\n\n5月化工指数已跌9%，若局势持续缓和，成本压力缓解叠加库存去化，板块或迎来修复窗口。欢迎一起讨论后续节奏～\n\n#学习笔记\n\n[source_mineru.md]\n# China Oil, \n\n[... middle omitted ...]\n\nore the deal is signed and there is confirmation that the supply of oil has resumed, a rebound in crude demand should support prices. China refining: SOE refineries' average utilisation declin\n\n[... middle omitted ...]\n\ncom/sa/en/cssa.html.\n\n© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.\n\n![](images/731b4bf474440ea7586e02b4f548aa6131fa593de9e2478b86b51e4abf2d703d.jpg)"
  },
  {
    "id": "R014",
    "title": "GS：市场真正低估的不是需求崩塌，而是供给恢复的路径与节奏",
    "digest": "[wechat_article.md]\n# GS：市场真正低估的不是需求崩塌，而是供给恢复的路径与节奏\n\n布伦特原油现货价格本周跌破80美元/桶。触发因素是一次传闻中的美伊临时协议——如果协议落地，霍尔木兹海峡的封锁可能迅速解除，超过5000万桶伊朗海上浮仓原油将立即进入市场。GS在最新一期《石油追踪》报告中，用一个数字重新定义了市场正在定价的叙事：70%的战前霍尔木兹流量，可能成为新的“100%”。\n\n这个数字背后，不是简单的供需再平衡，而是一套关于供给恢复速度、库存真实消耗、以及需求结构性错位的全新框架。市场目前的下跌，更多是在定价“协议达成”这一事件本身，但GS的测算表明，真正决定中期价格中枢的，是协议达成后供给恢复的路径、节奏，以及隐藏在库存数据之下的结构性变化。\n\n这份报告的价值不在于给出一个方向性判断，而在于拆解了三个市场尚未充分定价的关键变量：霍尔木兹流量的实际恢复斜率、中国库存数据的“暗物质”缺口、以及IEA与GS在供需平衡表上的系统性分歧。理解这三个变量，比猜测油价下一个整数关口重要得多。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 霍尔木兹流量恢复至战前70%，可能就是一个新的供需平衡点\n\nGS的核心测算框架建立在一个反直觉的假设上：波斯湾出口恢复至战前水平，可能不需要霍尔木兹海峡流量回到100%。报告指出，通过现有绕行路线——包括沙特的东西管道（Yanbu）、阿联酋的阿布扎比原油管道（Fujairah）、以及土耳其的基尔库克-杰伊汉管道——已经形成了每日750万桶的替代流量。加上阿曼湾的“暗渡”流量，当前实际绕过霍尔木兹的总流量约为每日910万桶。\n\n这意味着，要让波斯湾总出口恢复到战前水平，霍尔木兹本身只需要额外增加每日1270万桶的流量，即恢复到战前约70%的水平。这个“70%即100%”的判断，直接降低了供给恢复的门槛。市\n\n[... middle omitted ...]\n\n论，一起跟踪这些变量的实际走向，而不是被每日价格波动牵着走。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n霍尔木兹恢复70%意味着什么\n\n全球油轮运力充足，但船东还在观望\n\n某外资投行最新研报拆解了几个关键点：\n\n1/ 霍尔木兹恢复近在眼前？\n美伊临时协议签署后，波斯湾出口可能在7月底恢复正常，产量10月恢复。预计霍尔木兹流量将从目前水平增加约13mb/d，达到战前水平的70%左右\n\n2/ 运力不是瓶颈\n目前海峡内或5天航程内的空油轮容量约8.6亿桶，足够支撑流量恢复。但船东仍在等明确过境指引，风险偏好是关键约束\n\n3/ 需求端分歧明显\nIEA预计Q2缺口3.1mb/d，低于投行的5.0mb/d。主要原因是IEA对需求破坏的估计更大（5.5mb/d vs 4.9mb/d），5月达到峰值6.1mb/d\n\n4/ 中国需求变化值得关注\nIEA下调中国石油需求2.2mb/d（-13%），但中国原油进口下降更猛（4.2mb/d同比）。5月隐含库存减少1.6mb/d，远超可见库存的0.3mb/d，暗示存在隐形去库存\n\n5/ 2027年供需展望\nIEA预计2027年全球日均过剩5.0mb/d，供应增长7.9mb/d。如果需求持续疲软，供应过剩压力会持续存在\n\n当前市场定价似乎已部分计入恢复预期，但船东行为、伊朗谈判进展仍是变数\n\n[... middle omitted ...]\n\nate delivery.  \n☐ We now assume that Persian Gulf exports normalize to pre-war levels by end of July and Persian Gulf crude production recover by October and see risks to the Mideast supply ou\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R015",
    "title": "JPM：中国楼市真正的分水岭不在价格，而在供给侧的“窄复苏”能否撑到政策显效",
    "digest": "[wechat_article.md]\n# JPM：中国楼市真正的分水岭不在价格，而在供给侧的“窄复苏”能否撑到政策显效\n\n市场正在被两个相互矛盾的现象拉扯。一方面，5月JPM住房活动指数小幅回升，一线城市二手房价格连续录得环比正增长，部分核心区甚至出现“抢房”传闻。另一方面，全国新房销售面积同比跌幅从-6.5%扩大至-8.6%，房地产开发投资跌幅进一步加深至-24.3%，低线城市量价齐跌的格局毫无松动迹象。\n\n这份由JPM中国房地产研究团队发布的月度跟踪报告，其核心判断并不复杂，但含义却比多数市场解读更为深远：当前中国楼市正在经历的，不是一轮周期性复苏的前夜，而是一场“窄基K型”的结构性再平衡。一线城市的回暖并非全国复苏的领先指标，而是政策资源、人口流动和存量资产重新定价的结果。真正决定行业走向的，不是房价何时见底，而是“十五五”城市更新规划能否在供给端建立起一个不同于过去二十年“卖地-开发-销售”循环的新均衡机制。\n\n报告用一个词概括了这种状态——“量价调整的长期化”。这不是悲观，而是一种必要的清醒。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 一线城市二手房回暖的真实驱动不是需求爆发，而是库存出清和供给结构切换\n\n市场最容易犯的错误，是把一线城市的局部量价改善直接等同于全国需求的底部确认。JPM的报告提供了两个关键数据，足以让这种乐观情绪降温。\n\n第一，5月70城新房价格环比跌幅稳定在-0.20%，但一线城市录得+0.2%的环比正增长。更值得关注的是二手房市场：全国二手房价格环比跌幅从-0.23%小幅扩大至-0.26%，而一线城市却维持了+0.4%的环比涨幅。这意味着，一线城市和低线城市之间的差距不仅没有收敛，反而在拉大。\n\n第二，报告指出，一线城市回暖的支撑因素并非居民购房意愿的全面回升，而是三个更具体的结构性条件：二手房市场库存较低、成交量\n\n[... middle omitted ...]\n\n整长期化”的背景下，哪些资产类别反而可能获得定价重估的机会。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n一线城市有点稳，但别急着乐观\n\n**分化还在继续**\n\n某外资投行最新研报拆了几个关键点，信息量挺大，我帮你翻译一下。\n\n---\n\n**1/ 5月数据：有改善，但整体偏弱**\n\n- 新开工面积降幅收窄（-22.9% vs -28.2%）\n- 竣工面积降幅也在收窄（-20.2% vs -22.5%）\n- 但房地产投资降幅扩大（-24.3%），新房销售降幅也扩大（-8.6%）\n\n简单说：供给端收缩速度放缓，但需求端还在下探。\n\n**2/ 房价：一线涨，低线跌**\n\n- 70城新房价格环比稳定在-0.2%\n- 一线城市环比+0.2%，低线城市继续拖后腿\n- 二手房价格跌幅略扩至-0.26%，一线仍+0.4%\n\n从峰值算起，新房已跌13.7%，二手房跌22.6%。这个幅度已经不小了。\n\n**3/ 政策端：15五城市更新规划升级**\n\n相比14五，这次更系统、更强调执行：\n- 旧改规模翻倍\n- 财政支持更明确（预算内投资、专项债、超长期特别国债、税收优惠）\n- 土地政策更灵活（闲置土地再利用、混合用途开发、临时用途）\n\n目标不是“救市”，而是“稳市”+“提升居住品质”。\n\n**4/ 核心判断：K型复苏，不是全面回暖**\n\n[... middle omitted ...]\n\nnged quantity adjustment.\n\nJPM's housing activity index ticked up in May but remained subdued. The mild uptick reflected a smaller contraction in floor space starts (-22.9% oya in May vs -28.2\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 16 Jun 2026 03:00 PM HKT\n\nDisseminated 16 Jun 2026 03:00 PM HKT"
  },
  {
    "id": "R016",
    "title": "GS：欧洲数据中心正在重塑电力行业的估值逻辑，而市场仍按旧地图定价",
    "digest": "[wechat_article.md]\n# GS：欧洲数据中心正在重塑电力行业的估值逻辑，而市场仍按旧地图定价\n\n欧洲的电网运营商正在收到一个前所未有的信号。截至2026年5月，GS追踪的欧洲数据中心并网申请总量已飙升至约480吉瓦，相当于整个欧洲当前电力需求的1.5倍。六个月前这个数字是290吉瓦，十二个月前是170吉瓦。\n\n这不是一个线性增长，而是一个指数级跳升。即便考虑到其中一部分申请可能带有投机性质，这个规模本身已经构成一个判断：欧洲正在进入一个数据中心大规模建设的物理阶段，而电力公用事业公司将成为这个阶段最核心的枢纽角色。\n\nGS在最新发布的这份研报中，给出了一个清晰的逻辑链条：数据中心建设拉动电力需求，电力需求拉动电网和发电投资，投资拉动公用事业公司的盈利增长。但真正值得关注的，不是这个链条本身，而是这个链条如何改变市场对这些公司的定价方式。\n\n当前GS筛选出的三大受益集群——变革性电气化故事、可再生能源、能源安全提供商——在2030年的平均市盈率仅为12倍，低于行业平均的12.9倍。这些公司拥有更高的增长前景，却以更低的估值在交易。这组数字指向一个核心问题：市场是否在用过去的框架，定价一个正在被数据中心重塑的未来？\n\n以下是对这份研报核心逻辑的拆解。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 480吉瓦的并网申请意味着电力需求增长可能比市场预期的快一倍\n\nGS的数据追踪方法比较直接：汇总欧洲主要电网运营商收到的数据中心并网请求。480吉瓦这个数字最惊人的地方不是它的大小，而是它的增速。从2025年1月的170吉瓦到2026年5月的480吉瓦，一年半时间增长了近两倍。\n\n这个数字意味着什么？欧洲电力消费在过去十年基本停滞，年均增速在零附近。而数据中心一个单一品类，就可能在2028至2029年间推动欧洲电力需求年增长1.5个百分点。这还没\n\n[... middle omitted ...]\n\n完整的研报解读和原始图表，也会定期组织对关键假设的专项讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n欧洲数据中心，正在吃掉整个电网\n\n📊 数据中心，把欧洲电网吃掉了\n\n一份最新的投行研报显示：\n欧洲数据中心向电网的接入请求量，已经飙到 **480 GW**。\n什么概念？等于 **1.5 倍** 整个欧洲目前的电力需求。\n\n半年之前这个数字还是 290 GW，一年前才 170 GW。\n增长速度快到离谱。\n\n---\n\n**为什么这么猛？**\n\n1️⃣ **AI 军备竞赛**\n五大云巨头（hyperscalers）的资本开支，2027 年预计接近 **1 万亿美元**。\n比 2023 年翻了接近 10 倍。\n这些钱，大部分要建数据中心、买芯片、拉电网。\n\n2️⃣ **欧洲不能掉队**\n研报认为，欧洲必须大搞 AI，原因三个：\n- 提升生产力\n- 国家安全\n- 数据主权（不想让美国云厂商全拿走）\n\n所以预计到 2035 年，欧洲数据中心 IT 容量会达到 **65-80 GW**。\n\n3️⃣ **AI Agent 是隐藏变量**\n研报测算：一次 Agentic AI 查询的能耗，是普通 AI 聊天的 **6-50 倍**。\n如果 Agent 普及率每提高 10 个百分点，数据中心需求就要额外涨 25-30%。\n\n-\n\n[... middle omitted ...]\n\nieve its growth and size may signal a major construction phase for datacenters. Further, we believe utilities will be pivotal to support the development of datacenters by: providing energy, sc\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R017",
    "title": "摩根斯坦利：市场低估了三季度销售二次探底的冲击力",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：市场低估了三季度销售二次探底的冲击力\n\n5月的房地产销售数据，打破了市场此前两个月的微弱乐观。摩根斯坦利最新发布的这份研报，用一组清晰的数字给出了一个明确的判断：5月销售跌幅重新扩大，而更值得警惕的是，三季度可能迎来年内第二轮深度下滑。这不是一次简单的数据波动，而是行业结构性压力的再次确认。\n\n这份报告的价值不在于告诉你“市场不好”——这已经是共识。它的核心洞察在于：市场正在低估两个关键变量——二手房销售从放缓转向负增长的传导效应，以及开发商在土地市场上近乎停摆的谨慎姿态。这两个因素叠加，正在重塑下半年的行业定价逻辑。\n\n为什么现在必须认真对待这份判断？因为5月的数据并非孤立事件。全国销售金额同比降幅从4月的-7.6%扩大到-9.3%，销售面积降幅从-9.5%扩大到-13.2%。更关键的是，二手房市场的实时高频数据在5月中旬开始走弱，且近几周减速明显加快。摩根斯坦利据此判断，三季度二手房销售将转为同比负增长，这将直接拖累新房价格和销售。\n\n这意味着什么？意味着此前市场期待的“政策底”到“市场底”的传导路径，可能比预期更长、更曲折。行业的出清过程，正在从“量”的收缩进入“价”的压力阶段。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 5月数据确认了复苏的脆弱性，而非趋势逆转\n\n4月的数据曾让部分投资者燃起希望。销售金额和面积的同比降幅双双收窄，市场开始讨论“触底”的可能性。但5月的数据无情地打破了这种预期。\n\n摩根斯坦利在报告中明确写道，5月销售跌幅的重新扩大“符合预期”。这个措辞本身就值得深思——这意味着该机构的预测模型早已将这种反复纳入考量。全国销售金额同比降幅从-7.6%扩大到-9.3%，销售面积从-9.5%扩大到-13.2%。累计来看，前5个月销售金额同比下降13.5%，销售面积下降10.8\n\n[... middle omitted ...]\n\n点与空间、一线城市分化的可持续性——进行更深度的拆解和推演。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月楼市再降温，3季度压力更大\n\n楼市降温，3季度更冷\n\n5月楼市数据出来了，销售改善趋势被打断，跌幅重新扩大。\n\n全国销售额同比下降9.3%，销售面积下降13.2%，比4月的-7.6%和-9.5%还要差。前5个月累计，销售额和面积分别跌了13.5%和10.8%。\n\n房价方面，70城指数继续微跌，新房环比-0.2%，二手房-0.3%。但一线城市是个例外，新房+0.2%，二手房+0.4%，二手房成交还挺活跃。\n\n施工端更弱了。5月新开工面积同比跌25%，竣工面积跌20%，前5个月累计跌幅都到了23%。开发商拿地也很谨慎，前100强房企土地购置同比跌超40%。\n\n1/ 3季度销售可能更差\n从5月中旬开始，高能级城市的二手房成交就在走弱，最近几周减速更快了。居民信心还是脆弱，政策效果和积压需求都在消退，新盘供应也在减少。研报判断，3季度二手房成交可能转负，新房跌幅会更深。\n\n2/ 房价可能出现K型分化\n大部分城市房价会环比下跌，但一些一线城市因为去库存进展好，可能还能温和上涨。整体看，房价压力还在。\n\n3/ 开发商策略要精挑细选\n虽然股价从5月中旬高点回调了约20%，但销售可持续性还是不确定。研报更看好那些既有行业\n\n[... middle omitted ...]\n\nrice index continued to edge down, at a slightly faster pace, falling 0.2% m-m in primary and 0.3% m-m in secondary markets in May (vs. -0.2% for both in April). In contrast, Tier-1 cities wit\n\n[... middle omitted ...]\n\nperty Co Ltd (0123.HK)</td><td>O (09/27/2024)</td><td>HK$4.36</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R018",
    "title": "Bernstein：亚洲硬件正在经历一轮由AI驱动的ROE结构性重定价",
    "digest": "[wechat_article.md]\n# Bernstein：亚洲硬件正在经历一轮由AI驱动的ROE结构性重定价\n\n这份Bernstein研报的核心判断并不复杂，但它的支撑框架值得产业决策者和投资者仔细推敲：亚洲科技硬件公司正在经历一轮由AI需求驱动的ROE（净资产收益率）结构性上升周期，而市场对这一变化的定价，可能才刚刚开始。报告通过长达15年的资产负债表与现金流分析，揭示了不同细分赛道在盈利能力、资本效率和财务稳健性上的根本差异——这些差异在AI浪潮下正在被急剧放大。\n\n报告覆盖的七家公司中，Chroma ATE、Delta Electronics、Unimicron等AI直接受益标的的ROE预计将在2026-2027年达到30%甚至40%以上，而消费电子相关公司（Luxshare、Largan、Sunny Optical）的改善则温和得多，仅能恢复到中双位数至低20%的水平。这不仅是增速差异，更是商业模式护城河的重新定价。\n\n以下是我们从这份研报中提炼出的五个结构性洞察，以及一个报告尚未完全回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮ROE上升不是周期性的，而是由AI需求驱动的商业模式质变\n\n报告最值得关注的一点，是它区分了“周期性反弹”和“结构性跃迁”。过去15年，亚洲硬件公司的ROE波动大多跟随全球PCB市场周期或消费电子换机周期。但当前这一轮上升，核心驱动力来自AI数据中心对测试设备、电源管理、散热方案和高端PCB的持续需求，而非库存回补或终端需求脉冲。\n\n以Chroma ATE为例，其ROE从2024年的25%左右跃升至2026年预计的45%以上，背后是AI芯片测试、光收发器测试、以及AI数据中心电源测试三大业务的同时爆发。报告预计其2025-2028年营收和营业利润的复合年增长率分别达到46%和65%——这不是\n\n[... middle omitted ...]\n\n解问题的深度拆解。这里没有标准答案，只有持续逼近真相的讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI带飞ROE，谁在起飞谁在追\n\nAI驱动ROE大分化\n\n某外资投行最新研报拆解了亚洲科技硬件公司15年资产负债表和现金流。核心结论：AI需求正在制造一场ROE的“阶层分化”。\n\n1️⃣ AI玩家赢麻了\nChroma、Delta、Quanta的ROE在2026年预计冲到30%+。Chroma最猛，2025年ROE已超40%，靠的是AI芯片测试设备和光收发器测试的爆发需求。研报预计其2025-28年营收和营业利润CAGR分别达46%和65%。\n\n2️⃣ 消费电子在爬坡\nLuxshare、Largan、Sunny Optical的ROE改善更慢，预计回到15-20%区间。AI业务贡献还在早期。Largan虽然净利率高达40%，但现金多、资产周转慢，拉低了ROE。\n\n3️⃣ PCB供应链的真相\n日本龙头虽然掌握原材料优势，但ROIC并不突出——AI收入占比有限。而服务器相关PCB公司（Elite、Gold Circuit等）ROIC更高，说明AI才是真引擎。\n\n4️⃣ 财务健康度\n覆盖公司普遍净现金，资产负债率稳定或下降。Quanta例外——AI服务器扩张导致杠杆上升。现金转换周期普遍低于120天，运营效率不错。C\n\n[... middle omitted ...]\n\net & cash flow deep dive, we update analysis across our coverage with a focus on business models, profitability, solvency, and efficiency.\n\nAI demand is driving a sharp ROE upcycle, with AI-ex\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R019",
    "title": "Citi：市场低估的不是需求疲软，而是供给端策略的结构性拐点",
    "digest": "[wechat_article.md]\n# Citi：市场低估的不是需求疲软，而是供给端策略的结构性拐点\n\n这份来自Citi的周度订单追踪报告，表面上是在讨论6月第二周电动车订单环比下降13%的短期波动。但如果只读到“需求不及预期”就停下，就错过了这份报告真正有价值的判断。\n\n真正值得关注的，不是订单数字本身，而是Citi在报告后半段提出的一个推演：如果中国政府满足于出口增长来对冲内需疲弱，不再加码消费刺激，那么车企将被迫放弃过去几年的激进策略——这意味着市场格局、价格战烈度、成本控制逻辑，都将进入一个与过去三年完全不同的阶段。\n\n订单波动是表象，供给端策略的系统性调整才是内核。而市场对这个内核的定价，目前仍不充分。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 周度订单的“不及预期”本身不是新闻，但结构信号值得拆解\n\nCiti数据显示，6月第二周（6月8日至14日）行业整体订单环比下降13%，半月累计环比增长仅4%，远低于历史同期10%的月环比增速。单独看这个数字，很容易得出“需求走弱”的简单结论。\n\n但Citi的观察框架不止于此。报告指出，4月燃油车销量崩盘之后，新能源车需求其实并未显著受益于燃油车用户转化，而是维持了自身相对平坦的节奏。换句话说，新能源车需求并没有变差，它只是没有变好——而市场此前隐含的预期是“应该变好”。\n\n更值得关注的是品牌间的分化。半月环比来看，小鹏（+52%）、蔚来（+52%）、吉利银河（+45%）、比亚迪（+11%）跑赢行业；但周度环比来看，只有比亚迪（-4%）和吉利银河（+16%）保持了相对稳定，其余品牌周度波动显著放大。\n\n这种分化意味着什么？订单的稳定性正在成为比订单绝对值更重要的竞争维度。比亚迪和吉利银河的订单波动最小，说明它们的用户心智占据和渠道效率已经形成了某种“抗干扰”能力。而蔚来、小鹏尽管半月环比亮眼，但\n\n[... middle omitted ...]\n\n个“温和整合”情景的置信度，以及哪些标的在这个情景下最受益。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n6月第二周新能源订单，低于预期\n\n订单周报：6月第二周降温\n\n6月第二周（8-14日）新能源车订单环比下滑13%，整体弱于市场预期。上半月累计订单月环比仅增长4%，明显低于历史平均10%的月度增速。\n\n几家品牌表现分化明显：\n1️⃣ 小鹏、蔚来、吉利银河、比亚迪在月环比上领先，分别增长52%、52%、45%和11%。\n2️⃣ 周环比稳定性上，比亚迪和吉利银河表现更稳健，分别下滑4%和增长16%。\n3️⃣ 理想、华为鸿蒙、零跑等品牌订单回落明显，周环比降幅在17%-25%之间。\n\n研报核心判断是：4月燃油车销量大幅下滑后，新能源车需求并未明显受益，整体维持平稳。如果下半年政策端没有额外刺激，汽车厂商可能调整此前激进策略——行业整合会更温和、降价节奏放缓、成本管控更严格。\n\n值得关注的是，在整体需求平淡的环境下，比亚迪和吉利银河的订单稳定性相对突出。小鹏和蔚来虽然月环比增速亮眼，但周环比仍有两位数的下滑，持续性有待观察。\n\n大家觉得下半年新能源车市场的价格战会缓和还是继续？欢迎一起讨论。\n\n`#学习笔记` `` `#研究笔记`\n\n#学习笔记\n\n[source_mineru.md]\n16 Jun 2026 00:0\n\n[... middle omitted ...]\n\nained at its own flattish pace without obvious benefits and incremental MoM improvements. If China's government is satisfied with strong PV export growth offsetting domestic demand weakness as\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R020",
    "title": "Citi：半导体设备市场真正被低估的，是2028年2500亿美元WFE背后的结构性需求切换",
    "digest": "[wechat_article.md]\n# Citi：半导体设备市场真正被低估的，是2028年2500亿美元WFE背后的结构性需求切换\n\n半导体设备投资者的注意力，长期集中在2026年和2027年。这可以理解：AI基建正在加速，台积电、三星和英特尔都在扩产，WFE（晶圆厂设备支出）的增长路径看起来足够清晰。但Citi这份6月17日发布的最新研报，提出了一个值得认真对待的判断：市场对2028年的WFE预期可能显著偏低，而且，真正驱动增长的逻辑正在发生变化——不是简单的AI需求延续，而是一种由DRAM瓶颈引发的、对NAND设备需求的系统性重估。\n\nCiti在报告中引入了2028年WFE的牛市预测——2500亿美元。这个数字本身并非关键，关键的是支撑它的两个结构变化：第一，AI基建的资本开支增速虽然会从2026年的84%放缓至2028年的38%，但绝对规模仍然巨大，且正在从训练侧转向推理侧；第二，也是更值得关注的，是DRAM供应瓶颈正在迫使产业链重新设计内存架构，从而为NAND设备打开了一个此前未被充分定价的需求空间。\n\n这不是一个“AI继续增长”的故事，而是一个“AI的增长形态正在改变，设备需求结构必须随之调整”的故事。\n\n这份报告的核心贡献，不是给出了三个目标价——AMAT 710美元、LRCX 450美元、KLAC 290美元——而是提供了一个新的分析框架：当市场开始以2028年的视角审视这些公司时，哪些假设需要被重新审视，哪些风险尚未被定价。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 2028年WFE达到2500亿美元，这个预测的底气来自哪里\n\nCiti基于其超大规模云服务商资本开支模型，给出了2026-2028年WFE的牛市路径：1450亿美元、2000亿美元、2500亿美元。2028年相对于2027年仍有25%的增长。在设备投资周期通常被认为\n\n[... middle omitted ...]\n\n备需求能否持续到2028年”这个核心问题，展开更深入的讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n芯片设备需求看到2500亿美金\n\n📊 设备需求大爆发\n\n某外资投行最新研报指出，半导体设备市场（WFE）在2026-2028年将持续高增长，乐观情景下2028年达到2500亿美元。\n\n1️⃣ 三大驱动力\n- AI算力需求爆发，超大规模云厂商资本开支增速84%/56%/38%\n- 台积电、三星、英特尔持续扩产\n- 中国设备需求稳定在360亿美元\n\n2️⃣ DRAM瓶颈利好NAND\nAgentic AI推动内存需求结构性增长。多步推理工作流大幅扩大KV缓存，DRAM供应紧张且成本高企，企业加速采用互补方案：\n- KV缓存卸载到NAND闪存\n- AMD收购MEXT开发预测性内存软件\n- 苹果AFM 3把大模型存在NAND而非DRAM\n\n3️⃣ 设备商估值\n三家核心设备商目标价上调，基于2028年盈利能力的PE倍数：\n- AMAT: 31x PE，目标价710美元\n- LRCX: 40x PE，目标价450美元\n- KLAC: 40x PE，目标价290美元\n\n当前估值低于历史峰值15-20%，但高于均值55-67%，反映AI重估和WFE长周期上行。\n\n4️⃣ NAND新机遇\nKioxia XL-Flash通过CXL\n\n[... middle omitted ...]\n\n250B — We update our top-down WFE analysis for 2026/2027, and introduce 2028 WFE forecasts based on Citi's updated hyperscaler capex model of 84%/56%/38% growth in CY26/27/28. We now see bull \n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R021",
    "title": "GS：香水市场的下一个增长波，不是品类红利，而是打造爆款的能力",
    "digest": "[wechat_article.md]\n# GS：香水市场的下一个增长波，不是品类红利，而是打造爆款的能力\n\n香水行业的增长正在回归常态。疫情后那波由消费者基数扩张和使用频率提升驱动的增长，已经让位于一个更考验内功的阶段。GS欧洲消费品团队在最新发布的研报中给出了一个清晰判断：当品类增速从2023年的8%回落至2025年的3.5%，竞争强度却从2019年的2500个新品翻倍至2025年的6000个时，香水品牌的价值分化将不再取决于“是否站在风口上”，而取决于能否持续创造出新的爆款支柱。\n\n这份报告的核心贡献，不是预测行业增速，而是提供了一个分析框架：在供给驱动的品类里，增长本质上是一场“新品转化率”的竞赛。谁能在未来三年内推出并规模化新的爆款，谁就能在估值中获得重新定价。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 品类增长正常化后，真正的变量从“需求扩张”转向“供给质量”\n\n疫情后的香水市场经历了一轮罕见的量价齐升。消费者首次购买香水的年龄提前了，使用频率也显著增加。GS引用的波士顿咨询数据显示，从2000年代到2020年代，美国消费者首次购买香水的平均年龄从13岁下降到了11.5岁。这个“年轻化+扩圈”的组合，是过去几年行业高增长的底层逻辑。\n\n但这一结构性红利正在边际递减。当渗透率已经提升、消费者基数不再快速扩大时，增长动力就必须从“让更多人买”转向“让更多人买我的产品”。这正是GS报告的核心逻辑切换点：当行业进入存量博弈阶段，供给质量——即新品能否成为爆款——将成为区分赢家与输家的关键。\n\n数据显示，2019年欧莱雅推出Libre等三款新品，当年香水销售增长8%。六年后，Libre成为全球女性香水第一品牌，超越香奈儿。这不是偶然。在2010年代中期，欧莱雅推出La Vie Est Belle，带动女性香水在2014年实现两位数增长，2015年\n\n[... middle omitted ...]\n\n当品类增速进一步放缓到3%以下时，这个分析框架是否仍然有效？\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n香水行业的下一个爆款在哪\n\n香水赛道，进入“爆款竞赛”模式\n\n香水增长回归常态后，品牌表现越来越依赖推出新爆款的能力，而非行业红利。投行研报指出，2025年行业增速约3.5%，但新品发布数量从2019年2500款激增至6000款，竞争白热化。\n\n1/ 爆款才是长期引擎\n- 欧莱雅旗下Libre上市6年成为全球女香第一，超越香奈儿\n- 普伊格Good Girl用6年拿下3%市场份额\n- Interparfums靠持续推出新支柱，将Jimmy Choo做到超2亿欧元营收\n\n2/ 未来三年谁有潜力\n- 普伊格：计划为Rabanne和Jean Paul Gaultier推新爆款，La Bomba搜索热度已超早期Good Girl\n- Interparfums：四大品牌加Longchamp首秀，预计带来新增长\n- 欧莱雅：可能为Armani推新支柱，同时发展Kering Beauty香水线\n\n3/ 估值有空间吗\n研报认为，普伊格和Interparfums目前估值未完全反映爆款潜力，若执行到位，存在重估空间。欧莱雅因多元化优势享有溢价，但历史估值差距仍明显。\n\n关键看点：普伊格10月28日投资者日将阐述女香策略，欧莱雅1\n\n[... middle omitted ...]\n\nill expect penetration gains, but as category growth normalises to $3.5\\%$ in Q1 and competition intensifies (6,000 launches in 2025 versus 2,500 in 2019), growth will increasingly depend on l\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R022",
    "title": "NOM：人民币中间价定价模型释放的信号比汇率本身更重要",
    "digest": "[wechat_article.md]\n# NOM：人民币中间价定价模型释放的信号比汇率本身更重要\n\n对于关注人民币汇率走势的投资者而言，盯住每日中间价的变化已经成为一种条件反射。但NOM最新发布的这份USD/CNY定价模型报告揭示了一个更深层的判断：真正重要的不是中间价在某个交易日调升或调降了多少个基点，而是定价模型本身的误差正在系统性收窄，以及逆周期因子正在扮演一个更微妙的角色。\n\n这份报告的核心主张是，人民币中间价的定价机制正在经历一个从“被动对冲”向“主动校准”的转变。市场习惯于将中间价视为政策意图的风向标，但NOM的模型拆解显示，当前定价的驱动力已经从单一的政策维稳转向了更为复杂的多因子均衡。这意味着，投资者需要更新自己的分析框架，不能再用过去的逻辑来解读中间价的每一个波动。\n\n为什么现在需要关注这个问题？因为2026年下半年中国将迎来一系列关键的政治和经济议程：7月底的政治局经济工作会议、11月在深圳举办的APEC领导人会议、以及年底的中央经济工作会议。在这些关键时点前后，中间价的定价逻辑可能会发生微妙但重要的切换。NOM的模型恰恰为提前捕捉这种切换提供了一个量化工具。\n\n以下是我们从这份报告中提炼出的四个关键洞察，以及一个报告尚未完全回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 定价模型的预测误差正在系统性收窄，这暗示市场定价与政策意图正在趋于一致\n\nNOM模型显示，在不考虑逆周期因子调整的情况下，其投影值为6.7761，较前一日的6.8096大幅调低了335个基点。但更值得关注的不是单日变化，而是图2中展示的模型误差走势。\n\n从2025年初到2026年初，模型的日度误差从约-1800个基点的高位持续收窄，到2026年一季度已经趋近于零，甚至在4月份出现了约+600个基点的正向误差。这种误差的系统性收敛，意味着NOM的定\n\n[... middle omitted ...]\n\n些讨论将帮助你把NOM的量化框架真正转化为可执行的交易逻辑。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n人民币中间价，模型在说什么\n\n模型测算：6.7761\n\n比上次低了335个点\n\n某外资投行最新的人民币中间价模型显示，今天预测值是6.7761，比上次的6.8096低了335个点。如果加上逆周期因子，预测值会到6.7992，比上次低104个点。\n\n1/ 四个主要贡献货币\n模型显示，对今天预测变化贡献最大的四个货币是：欧元（+60个点）、韩元（+46个点）、澳元（+13个点）、英镑（+9个点）。欧元和韩元的权重最大，说明隔夜这两个货币的波动对中间价影响最明显。\n\n2/ 模型误差在缩小\n从近期模型误差走势看，1月份误差还有-1800个点，到4月份已经缩到-600个点，7月-400个点，10月-200个点。误差在持续收窄，模型对中间价的拟合度在提升。\n\n3/ 中间价调整节奏\n从每日中间价变动看，去年11月到今年2月基本没动，3月中突然调了150个点，4-5月又回归平稳。这种“突调-维稳”的节奏值得关注。\n\n4/ 下半年关键事件\n研报列了几个下半年重要节点：7月底政治局会议、10月国庆假期、11月深圳APEC、12月中央经济工作会议，以及年底可能的中美领导人会面。这些事件可能会影响汇率政策节奏。\n\n模型只是参考，实际\n\n[... middle omitted ...]\n\nange (without counter-cyclical factor)  \n![](images/4d8d61037f3ea59d8e3cbad16d87d1ade1856c5183e185f802a78182d3239afa.jpg)\n\n<details>\n<summary>bar chart</summary>\n\nTop 4 weighted contribution t\n\n[... middle omitted ...]\n\nrmation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R023",
    "title": "GS：银行股真正的防御性，来自资产负债表结构而非规模",
    "digest": "[wechat_article.md]\n# GS：银行股真正的防御性，来自资产负债表结构而非规模\n\n陆家嘴论坛的监管信号，正在改写中国金融市场的定价逻辑。\n\n6月17日，国家金融监督管理总局、人民银行、证监会、外汇管理局等主要金融监管机构负责人在陆家嘴论坛上发表了系列讲话。GS在随后的研报中提炼了一个核心判断：市场对银行股的定价，可能正在经历从“规模溢价”向“结构溢价”的切换。\n\n这不是一次普通的政策解读。这份报告的价值在于，它把监管层释放的分散信号，拼成了一幅关于未来三到五年中国金融体系演变的结构性地图。对投资者而言，真正重要的不是某条政策是松是紧，而是这些政策共同指向了一个方向——银行资产负债表的“质量”和“结构”，正在取代“增速”和“规模”，成为决定估值分化的核心变量。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 信用增速放缓不是周期波动，而是融资结构不可逆的转型\n\nGS报告中最具穿透力的观察，是人民银行对融资结构变化的定量描述。\n\n数据显示，以贷款为主的间接融资在社融增量中的占比，已从超过80%降至2025年的45%；在社融存量中的占比，也从接近100%降至三分之二。这不是一个短期现象。新发放贷款的结构变化更为剧烈：投向房地产和基础设施领域的新增贷款占比，从超过60%骤降至当前的10%；而投向科技金融、绿色金融、普惠金融、养老金融、数字金融这“五篇大文章”的新增贷款占比，已跃升至70%以上。\n\n这意味着什么？GS援引人行的判断称，随着经济结构从依赖中长期贷款的重资产传统行业，转向依赖多元化融资方式的轻资产新兴行业，维持过去的信贷增速既困难也无必要。“更慢、更高质量的贷款增长”正在成为新常态。\n\n对投资者而言，这个判断的含金量在于：它把信用增速放缓从“周期性利空”重新定义为“结构性常态”。那些仍在押注信贷脉冲反弹来驱动银行股估值的逻辑，可能需要\n\n[... middle omitted ...]\n\n值表格、银行间负债结构对比图等核心数据，我们也会在群内分享。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n陆家嘴论坛划重点：银行新玩法\n\n信贷减速，银行更稳了\n\n读完某外资投行对陆家嘴论坛的解析，发现银行正在经历一场“减量提质”的转型。\n\n1/ 信贷增速放缓，但质量更高了\n以前贷款占比超80%，现在降到45%左右。新钱主要流向科技、绿色、普惠等五大领域，而不是地产和基建。央行明确说了：贷款增速下降是新常态，关键是提高效率。\n\n2/ 利率走廊收窄，银行负债成本更稳\n央行把短期利率波动区间从70bp缩到50bp，相当于给银行间市场上了个“稳定器”。中小银行（如某股份行）同业负债占比高，受益更明显。\n\n3/ 离岸人民币试点，但别太兴奋\n6家银行获批在上海自贸区做离岸人民币外汇交易。虽然能拓展国际业务，但参考某大行，国际结算收入占比不到1%，短期影响有限。\n\n4/ 非银流动性工具，防债市崩盘\n央行在研究给非银机构提供紧急流动性，避免2022年底理财赎回潮重演。这对银行债券投资收益是利好，尤其交易账户占比高的银行（如某股份行交易账户占67%）。\n\n研报认为，信贷减速环境下，资产负债表质量才是关键。大行和优质股份行更受青睐。\n\n欢迎一起讨论银行转型的逻辑～\n\n#学习笔记\n\n[source_mineru.md]\nCHINA F\n\n[... middle omitted ...]\n\nn-bank financial institutions under specific circumstances, are poised to stabilize short-term interest rates and reduce bond market liquidity risks. These measures are expected to help banks \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R024",
    "title": "摩根斯坦利：消费复苏的真正考验不在总量，而在结构分化的再定价",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：消费复苏的真正考验不在总量，而在结构分化的再定价\n\n2026年5月的中国零售数据，是疫后首个同比负增长的月份——同比下降0.6%，低于市场预期的-0.2%和4月的+0.2%。这个数字本身并不令人震惊，但它揭示了一个比“消费疲软”更值得深挖的结构性事实：总量数字掩盖了供给端和渠道端正在发生的重新定价，而市场对这一重新定价的认知仍停留在需求侧叙事上。\n\n这份摩根斯坦利研报的价值，不在于它告诉你消费不好，而在于它提供了足够精细的颗粒度，让读者看清“哪里在加速出清、哪里在积蓄动能、哪里只是暂时性扰动”。以下是我们从中提取的五个关键判断。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 总量负增长背后的真正信号：补贴退坡后的真实需求压力测试\n\n5月零售总额同比下降0.6%，但更值得关注的是扣除汽车后的同比增速仍为正（+1.1%），以及对比2019年的CAGR从4月的2.9%小幅回升至3.2%。这说明总量下滑的主因并非消费意愿全面崩塌，而是特定品类的基数效应和补贴政策到期产生了集中拖累。\n\n电子与家电品类同比-15.6%，与4月的-15.1%基本持平，连续多月处于深度负增长区间。这一品类的疲软可以追溯到两个叠加因素：一是2024-2025年以旧换新补贴的刺激效应正在快速衰减，二是房地产相关需求（装修、家电配套）尚未出现实质性回暖。汽车品类同比-16.1%，同样受到去年高基数和新一轮价格战的不确定性压制。\n\n从MECE的角度看，5月数据可以被拆解为三类：政策驱动型需求的退潮、房地产关联需求的持续低迷、以及日常消费的韧性测试。三者的分化程度远超市场此前预期。\n\n这意味着，对于投资者而言，盯住总量数字做判断的风险正在上升。真正重要的是识别哪些品类正在经历“真实需求支撑的调整”，哪些只是“政策退出的噪音”。\n\n![研报\n\n[... middle omitted ...]\n\n更完整的原始图表、数据拆解工具，以及每周的消费数据跟踪更新。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月消费数据，该盯什么？\n\n消费复苏，边走边看\n\n最近某外资投行出了份5月社零研报，几个数字挺有意思。\n\n整体零售同比-0.6%，低于预期的-0.2%，也是疫情后首次转负。但拉长到2019年看，CAGR是3.2%，比4月的2.9%反而在改善。\n\n拆开看几个关键点👇\n\n1️⃣ 线上依然扛把子\n网上零售同比+3.4%，比4月的2.3%提速。说明消费习惯还在往线上迁移，线下客流恢复还得等。\n\n2️⃣ 必需品分化，饮料是亮点\n食品饮料整体增速从5.4%滑到2.8%，但软饮逆势加速到+6.1%。可能是天气热+端午假期催化，这个趋势6月值得继续盯。\n\n3️⃣ 可选消费还在磨底\n金银珠宝跌幅从-21.3%收窄到-8.9%，家电-15.6%仍然疲软。补贴效应退坡后，地产相关需求还没起来。\n\n4️⃣ 餐饮有点冷\n五一假期消费情绪偏弱，餐饮增速从2.2%降到0.6%。\n\n研报判断：消费复苏会是渐进式、有波折的。目前关注三条线——供给调整+需求改善（乳业、饮料）、线下消费回暖（火锅、啤酒）、公司自身驱动反转（美妆、新茶饮）。\n\n你们觉得6月端午数据会带来惊喜吗？欢迎一起讨论。\n\n#学习笔记\n\n[source_mineru.md]\n\n[... middle omitted ...]\n\nn Apr, partly dragged by soft consumer sentiment during the May Labor Day holiday and calendar shift of the Dragon Boat holiday. Online retail sales growth picked up to 3.4% yoy (2.3% in Apr).\n\n[... middle omitted ...]\n\nstrial Hldg (0551.HK)</td><td>E (09/14/2021)</td><td>HK$14.15</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R025",
    "title": "摩根斯坦利：市场对“和平”的定价已经过头，但油价真正的支撑尚未被计入",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：市场对“和平”的定价已经过头，但油价真正的支撑尚未被计入\n\n这份摩根斯坦利研报的标题本身就是一句判断：“Is Peace Mispriced?”——和平是否被错误定价？在美伊谅解备忘录即将签署、WTI自4月初已下跌29%的背景下，市场似乎已经在为“和平溢价”买单。但摩根斯坦利的分析揭示了一个更微妙的图景：当前股价所隐含的油价预期（约66美元/桶WTI）已经显著低于12个月远期曲线（约75美元），而基本面——尤其是三季度仍将存在的供需缺口——并没有被充分反映。真正被市场低估的，不是冲突持续的概率，而是即便和平到来，供给恢复的速度与库存重建的规模。\n\n这份报告的核心价值不在于判断地缘政治走向，而在于提供了一个量化框架：把“和平”拆解为可追踪的变量——产量恢复节奏、库存回补需求、以及不同油价情景下的企业现金流。对于产业决策者和长期投资者而言，当前的回调可能不是风险出清，而是重新评估资产定价的窗口。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 和平协议签署只是第一步，供给恢复的物理约束才是三季度油价的真正支撑\n\n市场对美伊达成谅解备忘录的反应是直观的：油价下跌。但摩根斯坦利原油策略师Martijn Rats的假设条件值得仔细拆解。该机构预计，即便霍尔木兹海峡近期重新开放，油轮运输恢复正常需要数周时间；到9月伊朗产量恢复50%，到12月恢复80%。这意味着三季度全球原油市场仍将维持约340万桶/日的平均缺口（仅OECD国家看，缺口约110万桶/日）。\n\n这个测算的隐含意义是：和平协议本身并不等于供给立即释放。从协议签署到实际产量回流，中间存在一个数月的“真空期”。而在此期间，全球库存已经因冲突期间的大规模释放而处于低位。摩根斯坦利的图表显示，OECD原油库存已经跌至5年平均水平以下，且仍在加速去库。三季度\n\n[... middle omitted ...]\n\n？这些问题的答案，或许就藏在报告没有明确写出的那部分分析中。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n油价跌了30%，但市场可能过度悲观了\n\n**和平协议=油价暴跌？**\n\n**油价真的会一直跌吗？**\n\n最近美伊签署谅解备忘录的消息，让WTI油价从4月高点累计跌了29%，差不多30美元/桶。市场似乎在快速定价“和平红利”，但这份研报拆解了几个关键矛盾。\n\n1️⃣ **恢复生产没那么快**\n就算霍尔木兹海峡这周五重新开放，某外资投行分析师预计：到9月才能恢复50%产量，12月恢复80%。三季度全球原油仍面临约340万桶/日的供应缺口，OECD国家缺口约110万桶/日。夏天供需依然偏紧。\n\n2️⃣ **库存需要时间回补**\n冲突以来全球库存消耗巨大，即使四季度供需接近平衡，市场还需要大量补库。研报预计布伦特三季度在90美元附近有支撑，明年至少维持在80美元以上。\n\n3️⃣ **当前估值已隐含较低油价预期**\n按远期曲线（WTI约72美元），美国油气公司2027年自由现金流收益率中位数约13%。但估值本身反映的隐含油价只有约66美元/桶，比12个月远期曲线低约13%。换句话说，市场已经提前消化了相当程度的悲观预期。\n\n4️⃣ **敏感性分析**\nWTI每变动10美元/桶，油气公司自由现金流收益率大约变化3个百分点\n\n[... middle omitted ...]\n\nound \\$90 in 3Q and at or above \\$80 into next year.  \nAt strip (\\~\\$72 WTI), we estimate median 2027 FCF yield of 11% for our oil coverage (13% for US oil E&Ps, 8% for US Majors, and 9% for C\n\n[... middle omitted ...]\n\nnture Global Inc (VG.N)</td><td>O (03/23/2026)</td><td>$11.70</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R026",
    "title": "JPM：市场对内地资金买港楼的恐慌，可能高估了政策冲击",
    "digest": "[wechat_article.md]\n# JPM：市场对内地资金买港楼的恐慌，可能高估了政策冲击\n\n一份来自JPM的专家电话会纪要，正在香港地产投资圈内流传。触发点是中国国务院发布的《境外直接投资条例》（即“837号文”）。这份文件让不少投资者担忧：内地居民购买香港物业的通道是否会被彻底堵死？香港楼市刚刚开始的复苏周期，是否会被政策“截胡”？\n\nJPM在6月16日发布的这份研报，核心判断出乎许多人的意料：**837号文并非针对内地居民购买香港物业，现行监管框架实质上没有发生根本性变化。** 但报告同时指出，真正值得关注的，不是政策本身，而是执行层面可能带来的“寒蝉效应”——尤其是对“内地税务居民”的全球收入征税风险，以及CRS信息交换对资产透明度的潜在影响。\n\n这篇研报的价值，不在于它给出了一个简单的“利好”或“利空”结论，而在于它通过一场与北京律师的深度对话，拆解了一个高度模糊的监管灰色地带。本文尝试提炼这份报告中最具洞察力的六个层次，并留下一个关键问题供读者自行判断。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 837号文并非针对香港楼市，它的真正靶点是跨境科技并购与个人境外投资监管空白\n\n许多市场参与者将837号文直接解读为“打压内地人买港楼”，这可能是误读。JPM邀请的北京律师明确指出，这份文件的出台背景，源于一个标志性跨境案例：一家美国公司拟收购某中国AI公司，交易暴露出两个监管漏洞——个人境外持股的合规性，以及核心技术未经审批的跨境转移。\n\n837号文本质上是一次“顶层设计”的补丁。它首次在国家层面将个人境外投资纳入监管框架，并强化了技术出口管制。对于香港物业购买，该文件并未设置新的禁令。律师的观点很清晰：内地居民用境内资金购买境外房产，在现行外汇管制框架下“从未被允许过，未来也不太可能被允许”。837号文只是重申了现状，而非收紧。\n\n[... middle omitted ...]\n\n表。欢迎来星球微信群里继续讨论，一起追踪政策细则的落地节奏。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n内地人还能买香港房吗？投研解读\n\n**关键信息梳理**\n\n6个核心结论，来自北京律师的线上分享\n\n—\n\n1️⃣ 用境内资金买香港房，历来不被允许\n无论是5万美元换汇额度还是其他渠道，资本项下的海外购房一直受限。这不是新规，是长期规则。\n\n2️⃣ 但如果有合法境外资金，购房不禁止\n关键看资金来源。如果是境外工资、股票变现、IPO收益等，属于合规境外资金，买房没问题。\n\n3️⃣ 837号文不是专门针对内地人买香港房\n这个新规主要针对企业ODI和科技出口监管，个人境外投资首次被纳入框架，但并非针对香港购房。\n\n4️⃣ CRS纳入房产短期内不现实\n房产不属于金融资产，纳入CRS需要全球不动产登记协调，操作复杂。但通过银行账户流水、香港土地注册处数据，间接监控是可能的。\n\n5️⃣ 内地税务居民理论需缴20%税\n如果你仍持内地户籍，大概率被认定为内地税务居民，香港房产的租金/资本利得理论上需缴20%个税，但这不是新规。\n\n6️⃣ 违规用境内资金买房的，罚款为主，强卖概率低\n处罚通常为违规金额的5-10%，实践中很少要求强制处置房产或追回资金。\n\n—\n\n**市场影响怎么看？**\n\n内地买家占香港住宅交易约5-10%（按金额算1\n\n[... middle omitted ...]\n\nin Hong Kong if the funding source is offshore.  \n3. Document 837 does not appear to be targeted at curbing Mainland Chinese purchases of property in Hong Kong.  \n4. Including real estate in C\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 16 Jun 2026 12:23 PM HKT\n\nDisseminated 16 Jun 2026 12:23 PM HKT"
  },
  {
    "id": "R027",
    "title": "摩根斯坦利：中国材料工业的真正分化不在需求，而在供给侧的刚性约束",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：中国材料工业的真正分化不在需求，而在供给侧的刚性约束\n\n五月工业数据出炉，市场目光大多落在房地产的持续疲软上。新开工面积同比下滑24.7%，销售面积降幅扩大至14.1%，固定资产投资同比下跌12.5%——这些数字确实令人忧虑。但如果只盯着需求端的压力，就很可能错过这份摩根斯坦利研报中最具价值的信号：中国材料工业正在经历一场深刻的分化，而分水岭不在于谁的需求更好，而在于谁的供给已经触及天花板。\n\n摩根斯坦利的分析师团队在这份五月工业产出数据报告中，给出了一个清晰的图景：在粗钢、水泥、玻璃、煤炭产量普遍同比下滑的背景下，电解铝产量却实现了同比1.7%的增长，且环比仍在上升。这不是偶然的月度波动，而是结构性差异的体现。当多数材料行业还在为过剩产能和低迷需求挣扎时，铝行业已经走到了供给约束的临界点。\n\n这份报告值得深读的原因，不在于它披露了五月的生产数据，而在于它揭示了不同材料子行业在未来12个月将走向截然不同的定价逻辑。对于产业决策者和投资者而言，理解这种分化的根源，比跟踪月度数据波动重要得多。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 房地产的拖累仍在深化，但三季度可能比数据本身更值得警惕\n\n五月房地产数据延续了疲弱态势。新开工面积同比下滑24.7%，虽较四月27.1%的降幅略有收窄，但绝对水平依然处于深度收缩区间。销售面积同比下降14.1%，较四月10.3%的降幅进一步恶化。竣工面积同比下降19.6%，与四月的19%基本持平。\n\n摩根斯坦利的中国房地产团队给出了一个值得高度重视的判断：预计三季度将更加疲弱。这个判断基于三个因素的叠加——居民信心仍然脆弱、政策效应和积压需求正在消退、可售资源减少。团队进一步预测，二手房销售将在三季度转为同比负增长，新房销售则在低基数上继续恶化。\n\n这意味着什么？材\n\n[... middle omitted ...]\n\n资拐点的判断方法，这些内容在群内会有更深入的交流。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n建筑原材料，5月谁在涨谁在跌\n\n**5月工业数据：铝产量继续走高**\n\n某外资投行最新研报拆解了5月工业增加值数据，几个关键发现值得关注：\n\n1️⃣ **地产链还在探底**\n- 新开工面积同比-24.7%（4月-27.1%），降幅略有收窄\n- 销售面积同比-14.1%（4月-10.3%），反而走弱了\n- 竣工面积同比-19.6%，基本持平\n- 投行地产团队预计三季度会更弱：居民信心修复慢、政策效果递减、可售资源减少\n\n2️⃣ **基建投资也在减速**\n- 5月固定资产投资同比-12.5%（4月-9.4%）\n- 公路投资同比-13.8%，降幅比4月收窄但仍为负\n\n3️⃣ **粗钢、水泥、玻璃产量继续收缩**\n- 粗钢同比-2.7%，表观消费量估测-8.5%\n- 水泥同比-8.1%，降幅收窄因基数低，但华东价格6月初仍偏弱（雨季+高考影响）\n- 玻璃同比-6.3%，库存高、需求弱，供需压力持续\n\n4️⃣ **只有铝一枝独秀**\n- 5月产量390万吨，同比+1.7%，环比+0.5%\n- 前5个月累计同比+3.5%，主要靠辽宁复产和内蒙古新产能\n- 当前运行产能已接近天花板，但行业盈利不错，预计全年维持高位\n\n5️\n\n[... middle omitted ...]\n\nsidering the still-fragile resident sentiment, diminishing policy effects/pent-up demand, and reduced new saleable resources, the team estimates secondary home sales to turn negative y-y, and \n\n[... middle omitted ...]\n\nr><td>West China Cement (2233.HK)</td><td>U (04/20/2026)</td><td>HK$1.75</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted."
  },
  {
    "id": "R028",
    "title": "Citi：市场低估的不是需求疲软，而是供给端正在发生的结构性出清",
    "digest": "[wechat_article.md]\n# Citi：市场低估的不是需求疲软，而是供给端正在发生的结构性出清\n\n5月中国乘用车市场销量不及预期，燃油车大幅下滑，新能源车环比持平。如果只看这个表面数据，很容易得出“需求不行”的结论。但Citi在6月16日组织的一场产业专家电话会中，提供了一个更具穿透力的观察框架：真正值得关注的不是短期订单波动，而是供给端正在发生的几重结构性变化——合资品牌面临生存抉择、增程式电动车的技术天花板开始显现、以及头部企业正在通过海外渠道和成本优势重构竞争边界。\n\n这份研报的核心价值不在于给出了多少家车企的周度订单数据，而在于它揭示了这些数据背后的一个关键判断：中国汽车市场的竞争逻辑，正在从“谁能造出更好的车”转向“谁能把规模优势和成本优势转化为定价权和出清能力”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 豪华车市场正在经历的不是周期波动，而是份额的永久性转移\n\nCiti专家电话会披露的一组数据值得反复推敲：BBA（奔驰、宝马、奥迪）上周在华订单已降至不到7000台，而去年同期为11000-12000台。这意味着德系豪华品牌在一年内失去了超过三分之一的订单量。同期，蔚来ES9稳态周订单维持在2000台左右，问界系列周订单约7500台，理想L系列约2000台。\n\n这不是简单的“消费降级”或“观望情绪”。这是豪华车市场正在发生的一次结构性权力交接。BBA的订单下滑与国内高端新能源品牌订单的韧性同时发生，说明高端消费需求并未消失，只是转移了去向。过去支撑BBA溢价的品牌认知、经销商网络和服务体系，在电动化与智能化的双重冲击下，正在失去对消费者的说服力。\n\nCiti专家更指出，BBA的周订单已降至“低于7000台”的水平，且没有看到任何企稳迹象。这意味着德系三强在中国市场可能已经越过了某个临界点——当订单量持续低于某个阈值，经销商\n\n[... middle omitted ...]\n\n应？增程式技术路线的天花板何时会真正反映到相关公司的估值中？\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月车市有点冷，但分化很明显\n\n6月车市观察｜周订单变局\n\n新能源内卷加剧，BBA压力山大\n\n最近看了份外资投行6月中旬的行业专家纪要，聊了5-6月车市动态和各家品牌订单变化。信息量挺大，直接划重点：\n\n**1. 5月车市整体不及预期**\n燃油车销量大跌，但新能源环比也只是持平。消费者观望情绪浓，油车下滑的红利没完全转到新能源。进入6月，市场依然不温不火，分化明显：20万以下新能源还算坚挺，但豪华车（传统BBA和新能源旗舰SUV）订单下滑明显。\n\n**2. 政策刺激可能在后头**\n专家判断，如果市场持续疲软，7月后可能会出台刺激政策。历史规律看，汽车刺激通常也在7月后。市场越弱，政策落地概率越高。\n\n**3. 各品牌周订单速览（上周 vs 两周前）**\n- **比亚迪**：5万（含不到5千海外回购），略降。二代刀片电池产能每月爬坡2-3万，唐L上市有望拉动订单。\n- **理想**：4.5千，L系列贡献约2千。ES9和M9对L9有分流。\n- **蔚来（不含乐道）**：6.5千（ES9稳定2千，ES8 2.5千），略有回落。\n- **小鹏**：6千（GX 1-1.5千，M03 2千+），GX订单下滑因交付周期长。\n\n[... middle omitted ...]\n\nNEV brands) has seen a sharp order decline. (2) Potential stimulus rollout: Mr. Sun believes if the market remains sluggish, stimulus policy could be introduced for stabilization. Historical p\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R029",
    "title": "GS：AI基础设施定价权正在经历结构性重估，但企业级需求仍处于“等待爆发”的临界点",
    "digest": "[wechat_article.md]\n# GS：AI基础设施定价权正在经历结构性重估，但企业级需求仍处于“等待爆发”的临界点\n\n市场对AI基础设施的讨论，大多聚焦于GPU算力是否过剩、资本开支何时见顶。但一份来自GS的最新实地调研报告，给出了一个更具穿透力的判断：当前真正被低估的，不是需求总量，而是供给侧约束正在重塑的定价结构。\n\n这份报告基于GS在丹佛举办的第二届年度AI基础设施投资者之旅，核心内容包括对私有数据中心运营商Flexential的实地考察，以及对光纤网络运营商Lumen Technologies管理层的深度访谈。报告揭示了一个清晰但尚未被市场充分定价的信号：供给侧的物理瓶颈——从电力到设备到选址——正在将数据中心的定价权推向一个前所未有的水平，而这一趋势的持续性，可能远超市场预期。\n\n与此同时，企业级AI基础设施的规模化采用，仍然处于“早期乐观但尚未落地”的阶段。这构成了当前AI基础设施投资的核心张力：一边是供给侧驱动的定价重估，一边是需求侧的结构性等待。理解这两者之间的错位，才是理解未来12-18个月相关资产表现的关键。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 供给约束已从短期扰动演变为结构性壁垒，数据中心定价权进入加速上行通道\n\nGS调研中来自Flexential的信息，可能是这份报告最值得关注的信号。Flexential是一家专注于多租户和批发业务的数据中心运营商，其管理层的表述直接且具体：当前每千瓦的租赁价格已接近200美元，预计到今年晚些时候将向250美元迈进。作为对比，2021年这一价格仅为70美元左右。\n\n这意味着，在过去四年中，数据中心单位容量的租赁价格已经上涨了近两倍，且涨价仍在加速。这不是一个周期性的波动，而是一个由供给侧结构性变化驱动的趋势。\n\n核心的供给约束来自三个层面，且每一个都在恶化而非缓解：\n\n第一\n\n[... middle omitted ...]\n\n助你在当前AI基础设施投资的复杂叙事中，建立自己的分析锚点。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n数据中心定价飙涨，谁在受益？\n\n数据中心定价权持续增强\n\n跟着某外资投行去了趟丹佛，看了两家AI基建核心玩家\n\n1️⃣ **数据中心定价正在翻倍**\nFlexential透露：新租约每千瓦定价已接近$200，年内有望到$250\n对比2021年仅$70，翻了近3倍\n供需紧张是主因——新站点建设周期从2021年的1.5年拉长到3年，变电站要等4年，发电机要等2年\n\n2️⃣ **企业级AI需求刚起步，但预期升温**\nFlexential的Englewood数据中心里，AI工作负载占60%\n但更大机会在“东-西向流量”市场——Lumen测算这个市场有$580亿，年增速13%\n企业级AI应用仍处早期，但管理层认为随着AI规模扩大，增长潜力可观\n\n3️⃣ **Lumen的新打法：网络即服务**\n通过NaaS平台，企业可以直接接入云端，省掉数据中心交叉连接费\n1Q26新增客户中，超20%是新客户，超60%在扩大使用规模\n管理层强调：Lumen的物理光纤网络是护城河，尤其是靠近超大规模云厂商的线路\n\n4️⃣ **供应链约束短期无解**\nFlexential正在提前下单预购设备\n新项目从拿地到可租用要18个月，但完全建成要3年\n\n[... middle omitted ...]\n\ne growth. Please see our detailed takeaways within.\n\n## Flexential\n\nDuring our 2026 Denver data center bus tour, we toured Flexential's Englewood site, an 18 MW air-cooled facility with \\~150K\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R030",
    "title": "UBS：东南亚外卖与电商的增长故事并未结束，但竞争正在重新定价龙头门槛",
    "digest": "[wechat_article.md]\n# UBS：东南亚外卖与电商的增长故事并未结束，但竞争正在重新定价龙头门槛\n\n市场对东南亚互联网平台的担忧并非没有根据。宏观放缓、季节性退潮、以及折扣力度回升——这些信号叠加在一起，很容易让人产生“增长见顶”的直觉判断。但UBS最新发布的5月外卖与电商收据追踪数据，提供了一个截然不同的叙事框架：真正需要被关注的，不是增长是否在放缓，而是这种放缓的结构性含义——它正在检验哪些平台真正拥有定价权与用户粘性。\n\n这份基于UBS Evidence Lab高频数据的报告，覆盖Grab与Shopee在东盟六国的核心运营指标。结论简洁但有力：两家公司均维持了20%以上的同比GMV/订单增速，但竞争烈度确实在环比回升。市场低估的不是它们能否继续增长，而是它们在增长放缓时，能否将规模优势转化为不可逆的竞争壁垒。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 5月数据揭示了一个关键拐点：增长节奏从“爆发”切换为“韧性测试”\n\n5月历来是东南亚消费的季节性低点，叠加今年开斋节时间调整，同比基数效应更为复杂。但UBS数据表明，Grab的外卖订单量同比仍增长21%，虽然从3-4月的26%-28%有所回落。Shopee的GMV增速同样健康，同比+20.6%，较4月的33%和3月的23%有所放缓。\n\n这里需要区分两个概念：减速与恶化。减速是节奏调整，是季节性、基数效应和宏观噪音共同作用的结果；恶化则是结构性的需求崩塌或竞争失衡。UBS的数据支持前者。Grab的日均订单量环比仍增长2.8%，Shopee日均订单环比增长6%，说明用户活跃度并未出现断崖式下降。\n\n关键在于，这种韧性是否能持续。印尼市场是Grab唯一录得订单同比下滑（-2.6%）的地区，UBS将其归因于宏观疲软。如果印尼的疲软从个别市场扩散为东盟趋势，那么当前的韧性测试可能演变为真\n\n[... middle omitted ...]\n\n实冲击有更深入的兴趣，这些话题在社群中都有持续的讨论和更新。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n东南亚外卖和电商，5月还在涨\n\n📈 数据依然健康\n\n5月东南亚外卖和电商的单量增速，依然保持20%以上，虽然比3/4月高点回落，但整体还是稳的。\n\n1️⃣ 外卖：Grab单量同比+21%\n- 5月增速比3/4月的26-28%略降，主要受印尼拖累（印尼单量同比-2.6%）\n- 客单价环比持平，同比微降1.1%，Grab继续推平价策略拉新\n- 菲律宾和马来西亚市场份额继续提升，新加坡微降\n\n2️⃣ 电商：Shopee GMV同比+21%\n- 同样从3/4月的22%/33%回落，有开斋节季节性因素\n- 单量增速28%，但客单价同比降5.6%，大家更爱买便宜货了\n\n3️⃣ 竞争在升温\n- 外卖折扣力度环比加大，Grab在大部分市场提高了补贴\n- 电商端，平台和商家补贴都在增加，但印尼和菲律宾平台补贴反而下降\n\n整体来看，增长动能还在，但宏观疲软和竞争加剧是接下来要盯的两个点。\n\n欢迎一起讨论东南亚消费趋势～\n\n#学习笔记\n\n[source_mineru.md]\n# ASEAN Internet\n\n# Food delivery and e-commerce receipts continue to show heal\n\n[... middle omitted ...]\n\nompetitive intensity for both ASEAN food delivery and e-commerce sectors ticked up in May'26, with discounts trending up MoM. We attribute part of the slowdown to changing timing for Lebaran, \n\n[... middle omitted ...]\n\ncom/sa/en/cssa.html.\n\n© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.\n\n![](images/d8476cf39621eab9659d9b8cd95ea28ec260aaa4b7b2e7883c56ebd59c0bd26a.jpg)"
  },
  {
    "id": "R031",
    "title": "Bernstein：中国车市真正的考验不是需求萎缩，而是补贴退潮后供给侧的再定价",
    "digest": "[wechat_article.md]\n# Bernstein：中国车市真正的考验不是需求萎缩，而是补贴退潮后供给侧的再定价\n\n2026年5月的中国汽车零售数据，看起来像一份“软着陆”报告。Bernstein追踪的交强险数据显示，当月国内零售销量同比下滑20.0%，年化销量（SAAR）降至1920万辆，低于4月的1960万辆，更远低于该机构估算的2200万辆正常年需求水平。\n\n但问题不在于数字本身。这份报告真正值得关注的判断是：市场目前的定价框架仍然在沿用“周期波动”的逻辑，而实际上中国汽车产业正在经历一次由政策退出、成本上升和出口结构变化共同驱动的供给侧再定价。Bernstein在维持行业谨慎展望的同时，对BYD和Xiaomi给出了Outperform评级，却同步下调了XPeng和Li Auto的目标价——这种分化本身就是一个信号。\n\n我们逐层拆解，看看这轮调整的真正含义在哪里。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 补贴退潮暴露的不是需求缺口，而是过去两年被透支的购买力\n\n市场习惯用“需求疲软”来解释销量下滑，但Bernstein的数据指向了一个更结构性的问题。该机构估算，2024-2025年的补贴政策提前拉动了超过500万辆需求。这意味着5月的-20%零售同比，本质上是“借来的时间”到期后的正常化过程。\n\n更关键的是，在没有新政策支持的情况下，Bernstein判断国内需求将保持疲软，至少要到11-12月基数效应恢复正常。这不是消费者不愿意买车，而是他们已经在补贴窗口期把未来几个月的购买力提前释放了。\n\n这对投资框架的含义是：如果市场把当前的销量下滑解读为“需求基本面恶化”，那么当基数效应在年底逆转时，可能出现预期差。但前提是，企业能够在不依赖补贴的情况下维持定价能力。\n\n![研报原图 2](assets/source_image_02.\n\n[... middle omitted ...]\n\n论那些“报告没有说透”的部分——这些往往才是超额收益的来源。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月车市，踩了一脚刹车\n\n5月车市降温\n\n零售同比跌20%，渗透率仍在61%\n\n---\n\n5月国内车市有点冷。某外资投行追踪的交强险数据显示，国内乘用车零售151万辆，同比下滑20%。年化零售销量降至1920万辆，低于4月的1960万，也低于机构估算的正常年需求2200万辆。\n\n**为什么这么弱？核心是去年补贴透支了需求。** 研报估算，2024-2025年的补贴政策提前拉动了超过500万辆的需求。叠加高基数，5月继续消化这个“透支效应”。\n\n**1/ 燃油车是重灾区**\n燃油车需求同比暴跌35.8%。豪华品牌降13.5%，大众品牌降21.1%。补贴退坡后，燃油车压力最大。\n\n**2/ 新能源渗透率稳住61%**\n新能源车销量虽同比降5.1%，但渗透率从4月继续爬升至61%。纯电占41.9%，插混占19.1%。消费者正逐步适应购置税从0%升至5%的变化，加上新车型竞争力强，电车热度没散。\n\n**3/ 出口成为关键增长极**\n5月出口同比大增73%，占批发总量的35.9%。新能源出口贡献了约55%的量。奇瑞、比亚迪、吉利位列前三。\n\n**4/ 小鹏和理想被下调目标价**\n研报将小鹏美股目标价从22美元下调至20\n\n[... middle omitted ...]\n\nbelieve gives the most accurate read on retail sell-through. May retail passenger vehicle sales totaled 1.51mn units, -20.0% yoy. The May retail SAAR of 19.2mn units is lower than 19.6 mn in A\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "Exhibit 1",
    "context": "## Zhipeng Cai Economist Asia Summer School 2026"
  },
  {
    "figure_id": "F002",
    "report_id": "R002",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Consumer Spending Has Held Up So Far Despite the Surge in Energy Prices"
  },
  {
    "figure_id": "F003",
    "report_id": "R002",
    "label": "Exhibit 2",
    "context": "Exhibit 2: We Expect Backloaded Cash Flow Headwinds from Gas Price Increases in Europe Real Cashflow Hit from Energy Price Increases"
  },
  {
    "figure_id": "F004",
    "report_id": "R002",
    "label": "Exhibit 3",
    "context": "Exhibit 3: In the US, Larger Tax Refunds Boosted Real Cash Flow by $0.8\\%$ in Q1 and $1.2\\%$ in Q2"
  },
  {
    "figure_id": "F005",
    "report_id": "R002",
    "label": "Exhibit 4",
    "context": "Exhibit 4: We Estimate that the Spending Drag is Yet to Materialize in the US, While Only Half of the Peak Drag Has Been Realized in the Euro Area; Consumer Spending Intentions Also Suggest Further Spending Drags Remain in the Pipe"
  },
  {
    "figure_id": "F006",
    "report_id": "R003",
    "label": "Exhibit 2",
    "context": "Exhibit 1: From 1997 to 2022, the household sector's net worth as a percentage of GDP increased twofold"
  },
  {
    "figure_id": "F007",
    "report_id": "R003",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Both household asset and liability growth rates moderated over time Annualized growth of total asset, liability, and net worth"
  },
  {
    "figure_id": "F008",
    "report_id": "R003",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Composition of household assets in 2022"
  },
  {
    "figure_id": "F009",
    "report_id": "R003",
    "label": "Exhibit 4",
    "context": "On the asset side, Exhibit 4 suggests that household balance sheets expanded steadily before the property downturn, driven by rising home prices and rapid accumulation in property purchases. This dynamic reversed as the property correction deepened over the pa"
  },
  {
    "figure_id": "F010",
    "report_id": "R003",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Since the September 2024 policy pivot, equities have contributed more to financial asset growth Chinese households financial assets (GS estimate)"
  },
  {
    "figure_id": "F011",
    "report_id": "R003",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Household leverage has been drifting lower since mid-2024"
  },
  {
    "figure_id": "F012",
    "report_id": "R003",
    "label": "Exhibit 7",
    "context": "Exhibit 7: China's household debt to GDP ratio was high versus EM countries, but below DM countries"
  },
  {
    "figure_id": "F013",
    "report_id": "R003",
    "label": "Exhibit 8",
    "context": "Exhibit 8: China's household debt-to-income ratio is high relative to major economies Household debt to disposable income ratio"
  },
  {
    "figure_id": "F014",
    "report_id": "R003",
    "label": "Exhibit 9",
    "context": "Exhibit 10: An emerging trend of capital shifting from bank deposits into risky assets"
  },
  {
    "figure_id": "F015",
    "report_id": "R003",
    "label": "Exhibit 9",
    "context": "Exhibit 10: An emerging trend of capital shifting from bank deposits into risky assets"
  },
  {
    "figure_id": "F016",
    "report_id": "R003",
    "label": "Exhibit 11",
    "context": "Exhibit 11: China's household equity and insurance allocation still appears low relative to developed markets Composition of household total assets As of Mar 31, 2026"
  },
  {
    "figure_id": "F017",
    "report_id": "R003",
    "label": "Exhibit 12",
    "context": "Exhibit 12: China's insurance penetration remains low relative to OECD peers"
  },
  {
    "figure_id": "F018",
    "report_id": "R004",
    "label": "Exhibit 1",
    "context": "Exhibit 1: We expect headline CPI and trimmed mean to increase $4.2\\%$ yoy and $3.5\\%$ yoy respectively in May"
  },
  {
    "figure_id": "F019",
    "report_id": "R004",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Diesel and gasoline prices fell in May"
  },
  {
    "figure_id": "F020",
    "report_id": "R004",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Key building supply companies are announcing a greater number of, and larger, price increases Exhibit 5: Fertiliser prices remain somewhat elevated"
  },
  {
    "figure_id": "F021",
    "report_id": "R004",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Key building supply companies are announcing a greater number of, and larger, price increases Exhibit 5: Fertiliser prices remain somewhat elevated"
  },
  {
    "figure_id": "F022",
    "report_id": "R004",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Prices for food and housing are likely to be boosted by higher input costs Contribution to CPI from a 10% increase in material & chemical prices"
  },
  {
    "figure_id": "F023",
    "report_id": "R004",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Alternative data on airfares fell a little in May Exhibit 8: International air transport prices in New Zealand declined in May"
  },
  {
    "figure_id": "F024",
    "report_id": "R004",
    "label": "Exhibit 8",
    "context": "Exhibit 7: Alternative data on airfares fell a little in May Exhibit 8: International air transport prices in New Zealand declined in May International travel prices"
  },
  {
    "figure_id": "F025",
    "report_id": "R004",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Growth in advertised rents picked up further in May"
  },
  {
    "figure_id": "F026",
    "report_id": "R004",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Housing inflation picked up further in April"
  },
  {
    "figure_id": "F027",
    "report_id": "R004",
    "label": "Exhibit 11",
    "context": "Exhibit 11: The RBA's updated labour framework suggests to us that labour market conditions are close to balanced"
  },
  {
    "figure_id": "F028",
    "report_id": "R004",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Short-term inflation expectations have retraced from their peaks but remain elevated"
  },
  {
    "figure_id": "F029",
    "report_id": "R004",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Long-term inflation expectations generally remain anchored"
  },
  {
    "figure_id": "F030",
    "report_id": "R004",
    "label": "Exhibit 15",
    "context": "Exhibit 14: Growth in New Zealand monthly prices picked up in May"
  },
  {
    "figure_id": "F031",
    "report_id": "R004",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Restaurant meals rose at its fastest pace since mid-2023 in May"
  },
  {
    "figure_id": "F032",
    "report_id": "R004",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Measures of price pressures from business surveys remain elevated"
  },
  {
    "figure_id": "F033",
    "report_id": "R004",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Finding skilled labour has become more difficult, but wage expectations remain subdued"
  },
  {
    "figure_id": "F034",
    "report_id": "R004",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Short-term inflation expectations rose further in 2Q2026"
  },
  {
    "figure_id": "F035",
    "report_id": "R004",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Dairy prices have been little changed over recent weeks"
  },
  {
    "figure_id": "F036",
    "report_id": "R005",
    "label": "Figure 1",
    "context": "■ Stagflation risks on the domestic side rise further. Domestic demand indicators missed already subdued expectations. Retail sales contracted for the first time since Covid at -0.6%YoY (Citi/Mkt: 0.0/-0.2%YoY). Investment decline deepened to -4.1%YoY Ytd (Cit"
  },
  {
    "figure_id": "F037",
    "report_id": "R005",
    "label": "Figure 2",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 2. Stagflation risks on the domestic side rise with contractionary retail sales and investment in May"
  },
  {
    "figure_id": "F038",
    "report_id": "R005",
    "label": "Figure 3",
    "context": "Infrastructure investment dropped further to 0.6% YoY Ytd from previously 4.3% YoY Ytd. We estimate monthly contraction to have expanded to -9.1% YoY from -4.9% YoY, inching close to lowest readings excluding Covid disruptions. The Six Networks investment coul"
  },
  {
    "figure_id": "F039",
    "report_id": "R005",
    "label": "Figure 5",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 5. Output growth of new-economy items Output Growth, New Economy"
  },
  {
    "figure_id": "F040",
    "report_id": "R005",
    "label": "Figure 7",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 7. Exports growth and exports delivery growth"
  },
  {
    "figure_id": "F041",
    "report_id": "R005",
    "label": "Figure 4",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 4. Sales-to-production ratio by month Sales-to-Production Ratio"
  },
  {
    "figure_id": "F042",
    "report_id": "R005",
    "label": "Figure 6",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 6. Output growth petrochemical related products Output Change, Petrochemical Related"
  },
  {
    "figure_id": "F043",
    "report_id": "R005",
    "label": "Figure 8",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 8. Cargo throughput at ports Cargo Throughput at Ports"
  },
  {
    "figure_id": "F044",
    "report_id": "R005",
    "label": "Figure 9",
    "context": "Figure 9. Retail sales growth by major categories © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 10. Retail sales, goods and restaurants' revenue"
  },
  {
    "figure_id": "F045",
    "report_id": "R005",
    "label": "Figure 12",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 12. Contribution from trade-in related items"
  },
  {
    "figure_id": "F046",
    "report_id": "R005",
    "label": "Figure 11",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 11. Retail sales, by size of retailers"
  },
  {
    "figure_id": "F047",
    "report_id": "R005",
    "label": "Figure 13",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 13. Contribution from austerity rule related items"
  },
  {
    "figure_id": "F048",
    "report_id": "R005",
    "label": "Figure 14",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 14. Second-hand property prices"
  },
  {
    "figure_id": "F049",
    "report_id": "R005",
    "label": "Figure 16",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 16. Counts of cities by change in second-hand prices"
  },
  {
    "figure_id": "F050",
    "report_id": "R005",
    "label": "Figure 18",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 18. Fixed asset investment indices"
  },
  {
    "figure_id": "F051",
    "report_id": "R005",
    "label": "Figure 15",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 15. New home prices"
  },
  {
    "figure_id": "F052",
    "report_id": "R005",
    "label": "Figure 17",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 17. Second-hand home sales in Shanghai Second-hand Home Sales, Shanghai"
  },
  {
    "figure_id": "F053",
    "report_id": "R005",
    "label": "Figure 19",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 19. Growth of FAI growth by major sectors"
  },
  {
    "figure_id": "F054",
    "report_id": "R006",
    "label": "Figure 1",
    "context": "Figure 1: Middle East/US Gulf/West Africa-China VLCC TCE +99%/-17%/-49% vs. pre-conflict level"
  },
  {
    "figure_id": "F055",
    "report_id": "R006",
    "label": "Figure 3",
    "context": "Figure 3: Average earnings of Capesize dropped by 18% WoW last week"
  },
  {
    "figure_id": "F056",
    "report_id": "R006",
    "label": "Figure 4",
    "context": "Figure 4: Crude tanker passage at Hormuz remained 95% below pre-conflict level"
  },
  {
    "figure_id": "F057",
    "report_id": "R006",
    "label": "Figure 5",
    "context": "Figure 5: Container throughput at China's key ports -4% WoW, 5% YoY last week"
  },
  {
    "figure_id": "F058",
    "report_id": "R006",
    "label": "Figure 6",
    "context": "Figure 6: Container volume new in transit from Asia to US has been showing a front loading pattern"
  },
  {
    "figure_id": "F059",
    "report_id": "R006",
    "label": "Figure 7",
    "context": "Figure 7: SCFI +9% WoW and +43% YoY Figure 9: Container ships re-routing away from Red Sea still at high levels (+4-5% YoY)"
  },
  {
    "figure_id": "F060",
    "report_id": "R006",
    "label": "Figure 11",
    "context": "Figure 11: Strong VLCC demand drives up YTD strong global shipbuilding demand"
  },
  {
    "figure_id": "F061",
    "report_id": "R006",
    "label": "Figure 8",
    "context": "Figure 8: Container freight futures on Far East-Northern Europe fall back after US-Iran peace deal"
  },
  {
    "figure_id": "F062",
    "report_id": "R006",
    "label": "Figure 10",
    "context": "Figure 10: Intra-Asia chartering index recovered WoW last week"
  },
  {
    "figure_id": "F063",
    "report_id": "R006",
    "label": "Figure 12",
    "context": "Figure 12: Both Clarksons and CNPI indicate new build price continue to increase"
  },
  {
    "figure_id": "F064",
    "report_id": "R007",
    "label": "Exhibit 1",
    "context": "Exhibit 1: European OEMs have continued to see their market share in Europe decline – consensus, optimistically, assumes this ceases"
  },
  {
    "figure_id": "F065",
    "report_id": "R007",
    "label": "Exhibit 7",
    "context": "Exhibit 7: The B and C segments represent c. of the European light vehicle market"
  },
  {
    "figure_id": "F066",
    "report_id": "R007",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Other important segments include D and LCVs"
  },
  {
    "figure_id": "F067",
    "report_id": "R007",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Amongst sub-segments, the C-SUV and B-SUV are the most important"
  },
  {
    "figure_id": "F068",
    "report_id": "R007",
    "label": "Exhibit 10",
    "context": "Exhibit 10: C-SUV, B-SUV and B-Hatchbacks make up over half of the market"
  },
  {
    "figure_id": "F069",
    "report_id": "R007",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Most of the European market can be categorised as Mid category pricing"
  },
  {
    "figure_id": "F070",
    "report_id": "R007",
    "label": "Exhibit 12",
    "context": "Exhibit 12: The entry-level segment has been growing in recent years"
  },
  {
    "figure_id": "F071",
    "report_id": "R007",
    "label": "Exhibit 13",
    "context": "Exhibit 13: EU5 are the most important European car markets"
  },
  {
    "figure_id": "F072",
    "report_id": "R007",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Amongst the EU5, Germany and UK represents the largest markets"
  },
  {
    "figure_id": "F073",
    "report_id": "R007",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Market share in China by Region (e.g. EU OEMs, US OEMs, JP, SK, CH)"
  },
  {
    "figure_id": "F074",
    "report_id": "R007",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Market share in Brazil by Region (e.g. EU OEMs, US OEMs, JP, SK, CH)"
  },
  {
    "figure_id": "F075",
    "report_id": "R007",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Market share in EU5 by Region (e.g. EU OEMs, US OEMs, JP, SK, CH)"
  },
  {
    "figure_id": "F076",
    "report_id": "R007",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Market share in US by Region (e.g. EU OEMs, US OEMs, JP, SK, CH)"
  },
  {
    "figure_id": "F077",
    "report_id": "R007",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Global OEMs' market share in Europe (EU5) has been relatively constant, except for Chinese OEMs"
  },
  {
    "figure_id": "F078",
    "report_id": "R007",
    "label": "Exhibit 20",
    "context": "Exhibit 20: European OEMs have continued to see market share decline in the region as a result"
  },
  {
    "figure_id": "F079",
    "report_id": "R007",
    "label": "Exhibit 21",
    "context": "Exhibit 21: At EU5 level, Stellantis has lost the most share amongst European legacy OEMs"
  },
  {
    "figure_id": "F080",
    "report_id": "R007",
    "label": "Exhibit 22",
    "context": "Exhibit 22: European OEMs have lost more share vs Chinese OEMs than any other global group"
  },
  {
    "figure_id": "F081",
    "report_id": "R007",
    "label": "Exhibit 24",
    "context": "Exhibit 24: European OEM market share losses appear to have slowed down, with Japanese and US players losing share in recent years"
  },
  {
    "figure_id": "F082",
    "report_id": "R007",
    "label": "Exhibit 25",
    "context": "Exhibit 25: Key European market trends and OEM exposure"
  },
  {
    "figure_id": "F083",
    "report_id": "R007",
    "label": "Exhibit 33",
    "context": "Exhibit 33: Norway: European OEM market share started to decline post-covid, though it has improved recently"
  },
  {
    "figure_id": "F084",
    "report_id": "R007",
    "label": "Exhibit 34",
    "context": "Exhibit 34: Norway: Chinese and US OEMs have grown share whilst Japanese & Europe have ceded"
  },
  {
    "figure_id": "F085",
    "report_id": "R007",
    "label": "Exhibit 35",
    "context": "Exhibit 35: Norway: Amongst European OEMs, Stellantis has lost the most share"
  },
  {
    "figure_id": "F086",
    "report_id": "R007",
    "label": "Exhibit 36",
    "context": "Exhibit 36: Norway: Amongst Chinese OEMs, Geely has been the largest gainer"
  },
  {
    "figure_id": "F087",
    "report_id": "R007",
    "label": "Exhibit 38",
    "context": "Exhibit 38: On a YoY basis, EU OEM market share losses have been slowing down in recent years, whilst Japan accelerates"
  },
  {
    "figure_id": "F088",
    "report_id": "R007",
    "label": "Exhibit 40",
    "context": "Chinese brands are establishing a foothold at the expense of US players. Chinese OEM market share has increased by \\~3%pp since 2020, making them the largest share gainers among foreign manufacturers. Importantly, these gains do not appear to have come at the "
  },
  {
    "figure_id": "F089",
    "report_id": "R007",
    "label": "Exhibit 41",
    "context": "Exhibit 41: Germany: Chinese OEMs have grown share whilst US & SK have ceded"
  },
  {
    "figure_id": "F090",
    "report_id": "R007",
    "label": "Exhibit 42",
    "context": "Exhibit 42: Germany: Amongst European OEMs, Mercedes-Benz lost the most share, whilst VW has continued to gain"
  },
  {
    "figure_id": "F091",
    "report_id": "R007",
    "label": "Exhibit 43",
    "context": "Exhibit 43: Germany: Amongst Chinese OEMs, BYD has been the largest gainer, though Geely remains strong"
  },
  {
    "figure_id": "F092",
    "report_id": "R007",
    "label": "Exhibit 46",
    "context": "Exhibit 46: On a YoY basis, EU OEM market share gains are starting to slow down"
  },
  {
    "figure_id": "F093",
    "report_id": "R007",
    "label": "Exhibit 47",
    "context": "Exhibit 47: Italy: European OEM market share started to decline post-covid"
  },
  {
    "figure_id": "F094",
    "report_id": "R007",
    "label": "Exhibit 49",
    "context": "Exhibit 49: Italy: Amongst European OEMs, Stellantis has lost the most share"
  },
  {
    "figure_id": "F095",
    "report_id": "R007",
    "label": "Exhibit 49",
    "context": "Exhibit 49: Italy: Amongst European OEMs, Stellantis has lost the most share"
  },
  {
    "figure_id": "F096",
    "report_id": "R007",
    "label": "Exhibit 48",
    "context": "Exhibit 48: Italy: Chinese and Japanese OEMs have grown share whilst Europe, US & Other have ceded"
  },
  {
    "figure_id": "F097",
    "report_id": "R007",
    "label": "Exhibit 50",
    "context": "Exhibit 50: Italy: Amongst Chinese OEMs, SAIC have been the largest gainer"
  },
  {
    "figure_id": "F098",
    "report_id": "R007",
    "label": "Exhibit 50",
    "context": "Exhibit 50: Italy: Amongst Chinese OEMs, SAIC have been the largest gainer"
  },
  {
    "figure_id": "F099",
    "report_id": "R007",
    "label": "Exhibit 54",
    "context": "Exhibit 54: Spain: European OEM market share started to decline post-covid"
  },
  {
    "figure_id": "F100",
    "report_id": "R007",
    "label": "Exhibit 56",
    "context": "Exhibit 56: Spain: Amongst European OEMs, Stellantis has lost the most share Exhibit 55: Spain: Chinese and Japanese OEMs have grown share whilst Europe, SK, US & Other have ceded"
  },
  {
    "figure_id": "F101",
    "report_id": "R007",
    "label": "Exhibit 56",
    "context": "Exhibit 56: Spain: Amongst European OEMs, Stellantis has lost the most share Exhibit 55: Spain: Chinese and Japanese OEMs have grown share whilst Europe, SK, US & Other have ceded"
  },
  {
    "figure_id": "F102",
    "report_id": "R007",
    "label": "Exhibit 57",
    "context": "Exhibit 57: Spain: Amongst Chinese OEMs, Chery have been the largest gainer"
  },
  {
    "figure_id": "F103",
    "report_id": "R007",
    "label": "Exhibit 57",
    "context": "Exhibit 57: Spain: Amongst Chinese OEMs, Chery have been the largest gainer"
  },
  {
    "figure_id": "F104",
    "report_id": "R007",
    "label": "Exhibit 60",
    "context": "Exhibit 60: On a YoY basis, EU OEM market share losses appear to be accelerating"
  },
  {
    "figure_id": "F105",
    "report_id": "R007",
    "label": "Exhibit 61",
    "context": "Exhibit 61: UK: European OEM market share started to decline post-covid Exhibit 63: UK: Amongst European OEMs, Stellantis has lost the most share"
  },
  {
    "figure_id": "F106",
    "report_id": "R007",
    "label": "Exhibit 61",
    "context": "Exhibit 61: UK: European OEM market share started to decline post-covid Exhibit 63: UK: Amongst European OEMs, Stellantis has lost the most share"
  },
  {
    "figure_id": "F107",
    "report_id": "R007",
    "label": "Exhibit 63",
    "context": "Exhibit 63: UK: Amongst European OEMs, Stellantis has lost the most share"
  },
  {
    "figure_id": "F108",
    "report_id": "R007",
    "label": "Exhibit 62",
    "context": "Exhibit 62: UK: Chinese and SK OEMs have grown share whilst Europe, Japanese, & US have ceded"
  },
  {
    "figure_id": "F109",
    "report_id": "R007",
    "label": "Exhibit 64",
    "context": "Exhibit 64: UK: Amongst Chinese OEMs, Chery have been the largest gainer"
  },
  {
    "figure_id": "F110",
    "report_id": "R007",
    "label": "Exhibit 64",
    "context": "Exhibit 64: UK: Amongst Chinese OEMs, Chery have been the largest gainer"
  },
  {
    "figure_id": "F111",
    "report_id": "R007",
    "label": "Exhibit 67",
    "context": "Exhibit 67: On a YoY basis, EU OEM market share losses re-accelerated in 2025"
  },
  {
    "figure_id": "F112",
    "report_id": "R007",
    "label": "Exhibit 68",
    "context": "Exhibit 68: EU5 exposure: Chinese OEMs are much more exposed to the UK"
  },
  {
    "figure_id": "F113",
    "report_id": "R007",
    "label": "Exhibit 69",
    "context": "Exhibit 69: France: European OEM market share started to decline post-covid, though it has improved recently"
  },
  {
    "figure_id": "F114",
    "report_id": "R007",
    "label": "Exhibit 70",
    "context": "Exhibit 70: France: Chinese and Japanese OEMs have grown share whilst Europe, SK & Other have ceded"
  },
  {
    "figure_id": "F115",
    "report_id": "R007",
    "label": "Exhibit 71",
    "context": "Exhibit 71: France: Amongst European OEMs, Stellantis has lost the most share"
  },
  {
    "figure_id": "F116",
    "report_id": "R007",
    "label": "Exhibit 72",
    "context": "Exhibit 72: France: Amongst Chinese OEMs, SAIC have been the largest gainers"
  },
  {
    "figure_id": "F117",
    "report_id": "R007",
    "label": "Exhibit 75",
    "context": "Exhibit 75: On a YoY basis, EU OEM market share has been improving in recent years"
  },
  {
    "figure_id": "F118",
    "report_id": "R007",
    "label": "Exhibit 76",
    "context": "Exhibit 76: EU5 BEV penetration rate"
  },
  {
    "figure_id": "F119",
    "report_id": "R007",
    "label": "Exhibit 77",
    "context": "Exhibit 77: EU5 PHEV penetration rate"
  },
  {
    "figure_id": "F120",
    "report_id": "R007",
    "label": "Exhibit 78",
    "context": "Exhibit 78: EU5 HEV+MHEV penetration rate"
  },
  {
    "figure_id": "F121",
    "report_id": "R007",
    "label": "Exhibit 79",
    "context": "Exhibit 79: EU5 powertrain mix"
  },
  {
    "figure_id": "F122",
    "report_id": "R007",
    "label": "Exhibit 82",
    "context": "Exhibit 82: On a YoY basis, Chinese OEMs have consistently gained EV market share in EU5"
  },
  {
    "figure_id": "F123",
    "report_id": "R007",
    "label": "Exhibit 84",
    "context": "Exhibit 84: Chinese OEMs are significantly exposed to the C-SUV, D-SUV and B-SUV sub-segments Exhibit 85: Chinese OEM sub-segment exposure in Europe – sustained focus on D-SUV and C-SUV"
  },
  {
    "figure_id": "F124",
    "report_id": "R007",
    "label": "Exhibit 86",
    "context": "Exhibit 86: D-SUV and C-SUV segments: Renault and Stellantis less exposed than Volkswagen"
  },
  {
    "figure_id": "F125",
    "report_id": "R007",
    "label": "Exhibit 87",
    "context": "Exhibit 87: SUVs make up more than 70% of Chinese OEMs' EU unit sales"
  },
  {
    "figure_id": "F126",
    "report_id": "R007",
    "label": "Exhibit 88",
    "context": "Exhibit 88: The entry level segment represents half of Chinese OEM volumes Exhibit 89: BMW, Mercedes and Volkswagen have more exposure to C-SUV and D-SUV than the wider market"
  },
  {
    "figure_id": "F127",
    "report_id": "R007",
    "label": "Exhibit 90",
    "context": "Exhibit 90: Chinese OEMs have much more entry level exposure than their European peers Exhibit 91: Over the past few years, Chinese OEMs have grown exposure to the entry segment"
  },
  {
    "figure_id": "F128",
    "report_id": "R007",
    "label": "Exhibit 102",
    "context": "Exhibit 102: Chinese OEMs keep gaining share in China (12M rolling monthly market share)"
  },
  {
    "figure_id": "F129",
    "report_id": "R007",
    "label": "Exhibit 103",
    "context": "Exhibit 103: Chinese OEMs are also gaining share globally: China automobile export (USD)"
  },
  {
    "figure_id": "F130",
    "report_id": "R007",
    "label": "Exhibit 104",
    "context": "Exhibit 104: China Auto Market Forecast China - PV Wholesale Volume (mn units)"
  },
  {
    "figure_id": "F131",
    "report_id": "R007",
    "label": "Exhibit 105",
    "context": "Exhibit 105: Stimulus Policies: Nationwide NEV Purchase Tax Exemption Exhibit 106: Our China Auto team sees 8m units exported in 2026 PV export forecast (mn units)"
  },
  {
    "figure_id": "F132",
    "report_id": "R007",
    "label": "Exhibit 107",
    "context": "Exhibit 107: Competition in China remains fierce amongst local players, particularly in EVs 2026 NEV Wholesale Volume Share and 2026 vs 2025 Volume Share Change"
  },
  {
    "figure_id": "F133",
    "report_id": "R007",
    "label": "Exhibit 108",
    "context": "Exhibit 108: Global expansion plans are underway"
  },
  {
    "figure_id": "F134",
    "report_id": "R007",
    "label": "Exhibit 109",
    "context": "China – vehicle export units by region, 2025"
  },
  {
    "figure_id": "F135",
    "report_id": "R007",
    "label": "Exhibit 110",
    "context": "Exhibit 110: German OEMs in Germany"
  },
  {
    "figure_id": "F136",
    "report_id": "R007",
    "label": "Exhibit 111",
    "context": "Exhibit 111: French OEMs in France"
  },
  {
    "figure_id": "F137",
    "report_id": "R007",
    "label": "Exhibit 112",
    "context": "Exhibit 112: Premium OEMs see slightly higher loyalty rates in Europe, whereas brand loyalty is rare in China % would purchase brand currently owned as next car"
  },
  {
    "figure_id": "F138",
    "report_id": "R007",
    "label": "Exhibit 113",
    "context": "Exhibit 113: Globally, brand loyalty is much higher amongst older customers than younger customers % would purchase brand currently owned as next car"
  },
  {
    "figure_id": "F139",
    "report_id": "R007",
    "label": "Exhibit 114",
    "context": "Exhibit 114: Outside China, Brazil and Europe appear to be the next major markets for Chinese OEMs % would purchase vehicle made in China"
  },
  {
    "figure_id": "F140",
    "report_id": "R007",
    "label": "Exhibit 115",
    "context": "Exhibit 115: Chinese OEMs now dominate the Chinese market, whilst market share is low and growing in other markets Chinese OEM FY25 market share"
  },
  {
    "figure_id": "F141",
    "report_id": "R007",
    "label": "Exhibit 117",
    "context": "Exhibit 117: FY26 will be the year with the highest new model releases (since 2000)..."
  },
  {
    "figure_id": "F142",
    "report_id": "R007",
    "label": "Exhibit 118",
    "context": "Exhibit 118: ...Chinese OEMs still lead the charge globally (number of new launches)"
  },
  {
    "figure_id": "F143",
    "report_id": "R007",
    "label": "Exhibit 119",
    "context": "Exhibit 119: European OEMs' new model production is spread across B, C, and D segments"
  },
  {
    "figure_id": "F144",
    "report_id": "R007",
    "label": "Exhibit 121",
    "context": "Exhibit 121: Chinese OEMs are significantly focused on the C-SUV, D-SUV and B-SUV sub-segments Exhibit 120: Whereas Chinese OEMs' new model production is much more focused on the C-segment"
  },
  {
    "figure_id": "F145",
    "report_id": "R007",
    "label": "Exhibit 123",
    "context": "Exhibit 123: Benchmarking European OEMs Exhibit 124: European Autos P/E"
  },
  {
    "figure_id": "F146",
    "report_id": "R007",
    "label": "Exhibit 125",
    "context": "Exhibit 125: OEM share price performance is closely tied to earnings expectations"
  },
  {
    "figure_id": "F147",
    "report_id": "R007",
    "label": "Exhibit 126",
    "context": "Exhibit 126: NTM P/E: BMW"
  },
  {
    "figure_id": "F148",
    "report_id": "R007",
    "label": "Exhibit 127",
    "context": "Exhibit 127: NTM P/E: Mercedes"
  },
  {
    "figure_id": "F149",
    "report_id": "R007",
    "label": "Exhibit 128",
    "context": "Exhibit 128: NTM P/E: Porsche"
  },
  {
    "figure_id": "F150",
    "report_id": "R007",
    "label": "Exhibit 129",
    "context": "Exhibit 129: NTM P/E: Volkswagen"
  },
  {
    "figure_id": "F151",
    "report_id": "R007",
    "label": "Exhibit 130",
    "context": "Exhibit 130: NTM P/E: Stellantis"
  },
  {
    "figure_id": "F152",
    "report_id": "R007",
    "label": "Exhibit 131",
    "context": "Exhibit 131: NTM P/E: Renault"
  },
  {
    "figure_id": "F153",
    "report_id": "R008",
    "label": "Figure 1",
    "context": "Figure 1: Total China steel output 1,018Mt annualised run rate: daily CISA steel output for 10-days ended 10 Jun: +4% vs previous (+2% YoY), in line with seasonal trend"
  },
  {
    "figure_id": "F154",
    "report_id": "R008",
    "label": "Figure 2",
    "context": "Figure 2: FOB iron ore price from Australia to China at \\~\\$90/t, +\\$4/t vs end of Feb & -\\$1/t YTD LHS: Iron ore price \\$/mt; RHS: Shipping cost \\$/mt"
  },
  {
    "figure_id": "F155",
    "report_id": "R008",
    "label": "Figure 2",
    "context": "Figure 2: FOB iron ore price from Australia to China at \\~\\$90/t, +\\$4/t vs end of Feb & -\\$1/t YTD LHS: Iron ore price \\$/mt; RHS: Shipping cost \\$/mt"
  },
  {
    "figure_id": "F156",
    "report_id": "R008",
    "label": "Figure 3",
    "context": "Figure 3: Iron ore bulk shipping costs from Australia, Brazil and South Africa to China all recorded a decline in the past week with Australian bulk shipping rates -22% WoW to \\$10.9/t LHS: Iron ore price \\$/mt; RHS: Shipping cost"
  },
  {
    "figure_id": "F157",
    "report_id": "R008",
    "label": "Figure 4",
    "context": "Figure 4: China steel mill margins extend losses in the past few weeks on higher coking coal prices"
  },
  {
    "figure_id": "F158",
    "report_id": "R008",
    "label": "Figure 5",
    "context": "Figure 5: Total China Steel exports (seasonality): May'26 export run-rate of 122Mtpa at top end of historical average"
  },
  {
    "figure_id": "F159",
    "report_id": "R008",
    "label": "Figure 6",
    "context": "Figure 6: 5M'2026 China steel exports at 45Mt, tracking at \\~ 10% of total output"
  },
  {
    "figure_id": "F160",
    "report_id": "R008",
    "label": "Figure 7",
    "context": "Figure 7: Official NBS China steel output (annualised) – we estimate 2026 China steel production at \\~1,000Mt"
  },
  {
    "figure_id": "F161",
    "report_id": "R008",
    "label": "Figure 8",
    "context": "Figure 8: China steel inventory week ending 12 June, flat WoW and +7% YoY; total steel inventory tracking in line with seasonal level"
  },
  {
    "figure_id": "F162",
    "report_id": "R008",
    "label": "Figure 9",
    "context": "Figure 9: Iron Ore inventory held at ports in China at \\~160Mt, tracking at historical high but 7Mt down since peak inventory in March"
  },
  {
    "figure_id": "F163",
    "report_id": "R009",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: In the Grace generation, LPDDR5 is soldered directly onto the board, making it non-replaceable and preventing any changes to the memory configuration Blackwell Ultra GPU Blackwell Ultra GPU Grace CPU LPDDR5"
  },
  {
    "figure_id": "F164",
    "report_id": "R009",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: In the Vera generation, SOCAMM2 uses modular LPDDR5x connected to the board via a compression/ pressure connector, enabling a replaceable memory format Exploded view of a microchip module with visible internal componen"
  },
  {
    "figure_id": "F165",
    "report_id": "R009",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Diagram of NVIDIA Vera CPU and SOCAMM2 layout NVIDIA Vera CPU Monolithic Compute Die 88 NVIDIA Custom Olympus Cores with 176 threads 162MB L3 Cache 2nd Gen NVIDIA Scalable Coherency Fabric (SCF)"
  },
  {
    "figure_id": "F166",
    "report_id": "R009",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: Architecture comparison between SOCAMM2 and DDR5 RDIMM Close-up of a microcontroller DDR5 RDIMM 96GB, showing internal memory chips and RAM slots (no readable text beyond branding) - \\~133mm x \\~31mm x \\~2.5mm"
  },
  {
    "figure_id": "F167",
    "report_id": "R009",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: On x86 CPUs, DDR channels accommodate vertically inserted DIMM modules Close-up of an AMD7 EPYC processor on a computer motherboard with visible circuitry and components (no readable text beyond branding)"
  },
  {
    "figure_id": "F168",
    "report_id": "R009",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: In contrast, SOCAMM2 employs a horizontally compressed design, enabling a more space-efficient layout. Even the last generation LPCAMM2 saves 64% of space vs. DIMM module LPCAMM2 64% space savings 2xSODIMM 78.0mm"
  },
  {
    "figure_id": "F169",
    "report_id": "R009",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: We project that NVIDIA CPU shipment volume will account for only MSD to low teens in total server CPU shipment ## SOCAMM2'S IMPACTS ON MEMORY INTERFACE CHIP SUPPLIERS ## A) SOCAMM2 EXPANDS TAM VS. SOLDERED LPDDR ON GRA"
  },
  {
    "figure_id": "F170",
    "report_id": "R009",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: First to market: Rambus delivers SOCAMM2-compatible interface solution at current stage 3A Voltage Regulator 3A Voltage Regulator 12A Voltage Regulator SPD Hub"
  },
  {
    "figure_id": "F171",
    "report_id": "R010",
    "label": "Figure 1",
    "context": "Figure 1: Exporters' FX conversion slowing for the second consecutive month"
  },
  {
    "figure_id": "F172",
    "report_id": "R010",
    "label": "Figure 2",
    "context": "Figure 2: First net purchase of Chinese bonds by foreign investors since April 2025"
  },
  {
    "figure_id": "F173",
    "report_id": "R012",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Framework of the global drug discovery and development funnel EXHIBIT 4: As shown by first clinical trial registrations, China-origin assets now account for 55% of global total, up from 38% in 2021 Global first clinica"
  },
  {
    "figure_id": "F174",
    "report_id": "R012",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: China's participation in US licensing transactions has increased meaningfully since 2021"
  },
  {
    "figure_id": "F175",
    "report_id": "R012",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: Out-licensing momentum strong - total deal value over \\$90 Bn in 1H26, 70% of 2025 total; Upfront payment \\$4.8 Bn, 71% of 2025 total China out-licensing activity: deal count, total deal value, and total upfront paymen"
  },
  {
    "figure_id": "F176",
    "report_id": "R012",
    "label": "EXHIBIT 8",
    "context": "% of US-bound deals: 60%, Total deal value: 62%. Note: Deals involving biosimilars and incrementally modified drugs are excluded; data cut off date: June 16th, 2026"
  },
  {
    "figure_id": "F177",
    "report_id": "R012",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: No. of active interventional Ph3 trials in the US by region (2021 vs. 2026YTD)"
  },
  {
    "figure_id": "F178",
    "report_id": "R012",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: US innovative drug sales (\\$ Bn) and share by region"
  },
  {
    "figure_id": "F179",
    "report_id": "R013",
    "label": "Figure 1",
    "context": "Figure 1: China crude oil inventory"
  },
  {
    "figure_id": "F180",
    "report_id": "R013",
    "label": "Figure 2",
    "context": "Figure 2: Utilisation of China SOE/teapot refiners"
  },
  {
    "figure_id": "F181",
    "report_id": "R013",
    "label": "Figure 3",
    "context": "Figure 3: China ethylene (naphtha cracking) capacity utilisation"
  },
  {
    "figure_id": "F182",
    "report_id": "R013",
    "label": "Figure 4",
    "context": "Figure 4: China ethylene (MTO) capacity utilisation"
  },
  {
    "figure_id": "F183",
    "report_id": "R013",
    "label": "Figure 5",
    "context": "Figure 5: China PE capacity utilisation"
  },
  {
    "figure_id": "F184",
    "report_id": "R013",
    "label": "Figure 6",
    "context": "Figure 6: China PP capacity utilisation"
  },
  {
    "figure_id": "F185",
    "report_id": "R013",
    "label": "Figure 7",
    "context": "Figure 7: China PVC capacity utilisation"
  },
  {
    "figure_id": "F186",
    "report_id": "R013",
    "label": "Figure 8",
    "context": "Figure 8: China PDH capacity utilisation"
  },
  {
    "figure_id": "F187",
    "report_id": "R013",
    "label": "Figure 9",
    "context": "Figure 9: China PX capacity utilisation"
  },
  {
    "figure_id": "F188",
    "report_id": "R013",
    "label": "Figure 10",
    "context": "Figure 10: China PTA capacity utilisation"
  },
  {
    "figure_id": "F189",
    "report_id": "R013",
    "label": "Figure 11",
    "context": "Figure 11: China Polyester filament capacity utilisation"
  },
  {
    "figure_id": "F190",
    "report_id": "R013",
    "label": "Figure 12",
    "context": "Figure 12: China MDI capacity utilisation"
  },
  {
    "figure_id": "F191",
    "report_id": "R013",
    "label": "Figure 13",
    "context": "Figure 13: China TDI capacity utilisation"
  },
  {
    "figure_id": "F192",
    "report_id": "R013",
    "label": "Figure 14",
    "context": "Figure 14: China TiO2 capacity utilisation"
  },
  {
    "figure_id": "F193",
    "report_id": "R013",
    "label": "Figure 15",
    "context": "Figure 15: Sample factories' inventory of PP"
  },
  {
    "figure_id": "F194",
    "report_id": "R013",
    "label": "Figure 16",
    "context": "Figure 16: Sample factories' inventory of PE"
  },
  {
    "figure_id": "F195",
    "report_id": "R013",
    "label": "Figure 17",
    "context": "Figure 17: Sample factories' inventory of PVC"
  },
  {
    "figure_id": "F196",
    "report_id": "R013",
    "label": "Figure 18",
    "context": "Figure 18: Sample factories' inventory of TiO2"
  },
  {
    "figure_id": "F197",
    "report_id": "R013",
    "label": "Figure 19",
    "context": "Figure 19: Sample factories' inventory of polyester filament"
  },
  {
    "figure_id": "F198",
    "report_id": "R013",
    "label": "Figure 20",
    "context": "Figure 20: Sample factories' inventory of silicone DMC"
  },
  {
    "figure_id": "F199",
    "report_id": "R014",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Normalization in Oil Exports From Gulf Producers to Their Pre-War Level May Be Achieved With a 12.7mb/d Increase in Hormuz Flows From Current Levels Estimating Mid June Hit to Oil Flows from Persian Gulf Countries"
  },
  {
    "figure_id": "F200",
    "report_id": "R014",
    "label": "Exhibit 4",
    "context": "Exhibit 4: We Estimate That 1.3mb/d of Visible OECD SPR Releases Have Reduced the Estimated Hit to Global Commercial Oil Stocks Since March by 1.3mb/d to 4.3mb/d Average Hit to Global Commercial Oil Stocks Since March 1 mb/d"
  },
  {
    "figure_id": "F201",
    "report_id": "R014",
    "label": "Exhibit 5",
    "context": "Exhibit 5: The Estimated Total Hit to Oil Flows from the Persian Gulf Is Currently at 14.8mb/d (4-Day Moving Average) Estimated Oil Flows From Persian Gulf Countries Percent of Normal"
  },
  {
    "figure_id": "F202",
    "report_id": "R014",
    "label": "Exhibit 6",
    "context": "Exhibit 6: We Estimate That Empty Oil Tankers Within the Strait or Within 5 Days of Navigation Have the Capacity to Load 861 Million Barrels Oil Tanker Capacity on Both Sides of Hormuz"
  },
  {
    "figure_id": "F203",
    "report_id": "R014",
    "label": "Exhibit 7",
    "context": "Exhibit 7: 28% of the Hit to Persian Gulf Crude/Condensate Exports Is Currently Being Offset, With Contributions From Higher Exports from the US/Americas Ex US/Russia of 16pp/8pp/5pp Global Oil Exports vs. 2025 Average"
  },
  {
    "figure_id": "F204",
    "report_id": "R014",
    "label": "Exhibit 8",
    "context": "Exhibit 8: China Landed Visible Inventories Have Drawn by 0.5mb/d Over the Last 14 Days Global Visible Total Oil Inventories, Change Since Feb 27"
  },
  {
    "figure_id": "F205",
    "report_id": "R014",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Global Diesel and Gasoline High-Frequency Visible Stocks Decreased to the Bottom of Their Seasonal Range Global Visible High-Frequency Gasoline and Diesel Stocks"
  },
  {
    "figure_id": "F206",
    "report_id": "R014",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Estimated Chinese Refineries Runs Have Declined by 1.9mb/d Since End of February"
  },
  {
    "figure_id": "F207",
    "report_id": "R014",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Japanese Refineries Runs Are 0.5mb/d Lower Than Their End-of-February Levels"
  },
  {
    "figure_id": "F208",
    "report_id": "R014",
    "label": "Exhibit 13",
    "context": "Exhibit 13: The Utilization Rate of US Refineries Is Up 0.6pp Year-Over-Year as US Product Margins Remain High"
  },
  {
    "figure_id": "F209",
    "report_id": "R014",
    "label": "Exhibit 14",
    "context": "Exhibit 14: US Wholesale Gasoline Prices Outperform Regional Counterparts and Products Across the Barrel on Strong Summer Demand Change in Prices Since Feb 27 (As of Jun 16 Market Close)"
  },
  {
    "figure_id": "F210",
    "report_id": "R014",
    "label": "Exhibit 15",
    "context": "Exhibit 15: While Global Wholesale Refined Products Prices Continue to Normalize, Retail Prices Remain Elevated"
  },
  {
    "figure_id": "F211",
    "report_id": "R014",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Dubai Prompt Timespreads Fall in Contango Potentially Reflecting Rising Crude Exports From the Gulf, the Expectation of Hormuz Reopening, and Weak China Crude Imports"
  },
  {
    "figure_id": "F212",
    "report_id": "R014",
    "label": "Exhibit 17",
    "context": "Exhibit 17: We Estimate That Global Jet Fuel Demand in June Will be 110kb/d Softer Year-Over-Year, or 6% Below Trend"
  },
  {
    "figure_id": "F213",
    "report_id": "R014",
    "label": "Exhibit 18",
    "context": "Exhibit 18: China and European Road Fuels Retail Sales Decreased by $23.3\\%$ and $3.5\\%$ Respectively From Year-Ago Levels China and European Road Fuels: Real Retail Sales"
  },
  {
    "figure_id": "F214",
    "report_id": "R014",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Our US Gasoline Demand Nowcast Is Slightly Above Its Last Year Seasonal Levels"
  },
  {
    "figure_id": "F215",
    "report_id": "R014",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Global Crude/Condensate Imports Are Down 5.8mb/d from 2025 Average Levels, and Refined Products Imports Are Down 4.5mb/d Global Oil Imports vs. 2025 Average"
  },
  {
    "figure_id": "F216",
    "report_id": "R016",
    "label": "Exhibit 1",
    "context": "Exhibit 1: The EU DC pipeline has more than doubled in one year EU 28 GSe datacenter pipeline evolution, 2025-26 (GW)"
  },
  {
    "figure_id": "F217",
    "report_id": "R016",
    "label": "Exhibit 2",
    "context": "Exhibit 2: We estimate an EPS CAGR of $c. + 9\\%$ to the end of the decade for our key electrification compounders 2026-30E Clean EPS CAGR breakdown by company (percentage)"
  },
  {
    "figure_id": "F218",
    "report_id": "R016",
    "label": "Exhibit 3",
    "context": "Exhibit 3: We see three company clusters as the main beneficiaries Infographic ## We favour three company clusters: Transformative Electrification Stories: Naturgy, Enel, Engie Renewables: Developers (RWE, EDPR, Solaria, Orsted"
  },
  {
    "figure_id": "F219",
    "report_id": "R016",
    "label": "Exhibit 3",
    "context": "Exhibit 3: We see three company clusters as the main beneficiaries Infographic ## We favour three company clusters: Transformative Electrification Stories: Naturgy, Enel, Engie Renewables: Developers (RWE, EDPR, Solaria, Orsted"
  },
  {
    "figure_id": "F220",
    "report_id": "R016",
    "label": "Exhibit 4",
    "context": "Exhibit 4: The three clusters trade on an average P/E of c.12x by 2030E Key valuation metrics, 2026-30E (x)"
  },
  {
    "figure_id": "F221",
    "report_id": "R016",
    "label": "Exhibit 5",
    "context": "Exhibit 5: The european DC pipeline has reached c.480 GW European data center connection requests, by country (GW, percentage) Equivalent to c.1.5x of power demand (c.320 GW in 2025) DC Connection Requests EU-28"
  },
  {
    "figure_id": "F222",
    "report_id": "R016",
    "label": "Exhibit 6",
    "context": "Exhibit 6: The EU DC pipeline has more than doubled in one year EU 28 GSe datacenter pipeline evolution, 2025-26 (GW)"
  },
  {
    "figure_id": "F223",
    "report_id": "R016",
    "label": "Exhibit 7",
    "context": "Exhibit 7: The EUDCA forecasts +20 GW DC capacity additions by 2031 European datacenter evolution, 2025-31 (GW)"
  },
  {
    "figure_id": "F224",
    "report_id": "R016",
    "label": "Exhibit 8",
    "context": "Exhibit 8: DC capacity development to 2031 could drive +1.5% power demand growth pa, as of GW of DC capacity in 2031 would be equivalent to $10\\%$ of total EU power demand"
  },
  {
    "figure_id": "F225",
    "report_id": "R016",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Agentic AI queries are much more energy-intensive than traditional queries; we adopt a conservative approach Energy use of traditional vs. Agentic AI query (Wh/query)"
  },
  {
    "figure_id": "F226",
    "report_id": "R016",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Europe's datacenter market would reach c.80 GW total DC capacity by 2035 in our upside case, equivalent to c.25% of demand Breakdown of total DC capacity in our base and upside case, 2035 (GW)"
  },
  {
    "figure_id": "F227",
    "report_id": "R016",
    "label": "Exhibit 11",
    "context": "Exhibit 11: We expect power consumption to grow by 1.5-2% pa over 2025-29E, with growth rising to 2.5-3.5% pa as electrification and datacenter rollout accelerate EU 2025-32E power demand power evolution, breakdown by driver (TWh, p"
  },
  {
    "figure_id": "F228",
    "report_id": "R016",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Our “hyper-electrification” scenario sees power demand grow as much as +5% pa from 2030 EU 2026-32E power demand evolution across base case and different GS scenarios (percentage)"
  },
  {
    "figure_id": "F229",
    "report_id": "R016",
    "label": "Exhibit 13",
    "context": "Exhibit 13: The main five hyperscalers are set to invest c.\\$1 trn in 2027 Hyperscaler AI investment evolution, 2020-27E (\\$) +45% CAGR"
  },
  {
    "figure_id": "F230",
    "report_id": "R018",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: The trend of ROE among companies reflects broader sector trends and cycles, and individual company competitiveness in each market"
  },
  {
    "figure_id": "F231",
    "report_id": "R018",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: Global PCB market has been highly cyclical over the past 16 years and is now experiencing a strong upcycle Global PCB market size & YoY growth"
  },
  {
    "figure_id": "F232",
    "report_id": "R018",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: The DuPont analysis to break down the ROE drivers The future sales and profits are estimated by Bernstein EXHIBIT 4: Profitability along the tech supply chain follows a smile curve reflecting the varying value add of eac"
  },
  {
    "figure_id": "F233",
    "report_id": "R018",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: Our coverage companies exhibit similar level of sales volatility, except for Quanta"
  },
  {
    "figure_id": "F234",
    "report_id": "R018",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: Net profit volatility is highest at Sunny Optical, mainly due to GM swings, followed by Chroma, which is structurally more cyclical"
  },
  {
    "figure_id": "F235",
    "report_id": "R018",
    "label": "Exhibit 12",
    "context": "EXHIBIT 7: In general, the ROIC trend parallels the ROE trend, except that Quanta's ranking appears lower with its debts included in ROIC calculation Return on invested capital (ROIC)"
  },
  {
    "figure_id": "F236",
    "report_id": "R018",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: The overall PCB industry is capex-intensive as companies need to expand capacities to meet changing demand, often cyclical in nature Capex as % of revenue (5-year avg.)"
  },
  {
    "figure_id": "F237",
    "report_id": "R018",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: PCB in the server segment will likely grow faster than the overall market at a 17% CAGR in 2025-30E PCB Market Size by End Market"
  },
  {
    "figure_id": "F238",
    "report_id": "R018",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: PCB supply chain companies with higher exposure to server market would present better ROIC. ABF companies had relatively low ROIC last year as low-end product was still oversupplied 2025 ROIC (Y-axis) and Invested capita"
  },
  {
    "figure_id": "F239",
    "report_id": "R018",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: 5-year average ROIC reflects the last ABF upcycle during COVID 5-year avg. ROIC (Y-axis) and 2025 Invested capital (Bubble size) - PCB supply chain"
  },
  {
    "figure_id": "F240",
    "report_id": "R018",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: Testers' GPMs are relatively high, averaging c.56% in 2026E Testers' GP and GPM (CY2026E)"
  },
  {
    "figure_id": "F241",
    "report_id": "R018",
    "label": "EXHIBIT 13",
    "context": "EXHIBIT 13: In 2026E, testers' OPMs are typically $30\\%+$ with semi tester companies carry higher profitability comparing to power tester suppliers Testers' OP and OPM (CY2026E)"
  },
  {
    "figure_id": "F242",
    "report_id": "R018",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: ROIC shows greater dispersion, but overall follows a similar trend to GPM and OPM Testers' ROIC (CY2025)"
  },
  {
    "figure_id": "F243",
    "report_id": "R018",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: Quanta exhibits the highest D/E ratio within our coverage Debt to equity ratio"
  },
  {
    "figure_id": "F244",
    "report_id": "R018",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 16: Within our coverage, Quanta is the sole company with a notably high net debt-to-equity ratio Net debt to equity ratio"
  },
  {
    "figure_id": "F245",
    "report_id": "R018",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 17: Quanta incurred net interest expenses in 2025 for the first time since 2020, primarily due to increased working capital burden from its fast-growing AI server business Net interest expense as % of operating profit"
  },
  {
    "figure_id": "F246",
    "report_id": "R018",
    "label": "Exhibit 18",
    "context": "EXHIBIT 18: Chroma exhibits the longest cash conversion cycle within our Coverage"
  },
  {
    "figure_id": "F247",
    "report_id": "R018",
    "label": "EXHIBIT 19",
    "context": "EXHIBIT 19: Sunny Optical's lengthy account payable days and Chroma's long inventory turnover days result in the shortest and the longest cash conversion cycle within our Coverage respectively Cash conversion cycle breakdown in 2025"
  },
  {
    "figure_id": "F248",
    "report_id": "R018",
    "label": "EXHIBIT 20",
    "context": "EXHIBIT 20: Over the past decade, the accounts receivable turnover days of Luxshare have consistently declined and now become the shortest within our coverage, indicating its strong bargaining power against downstream customers Acco"
  },
  {
    "figure_id": "F249",
    "report_id": "R018",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 21: Chroma exhibits the longest inventory turnover days, which reflects the nature of the testing equipment industry characterized by infrequent purchases and prolonged inspection and trial processes Inventory turnover days"
  },
  {
    "figure_id": "F250",
    "report_id": "R018",
    "label": "EXHIBIT 22",
    "context": "EXHIBIT 22: Chroma's inventory turnover days in 2025 was below industry average Testors' inventory turnover days in 2025"
  },
  {
    "figure_id": "F251",
    "report_id": "R018",
    "label": "EXHIBIT 23",
    "context": "EXHIBIT 23: Largan and Chroma showcased the most robust cash flow generation ability despite the longer cash conversion cycle, thanks to their high NPM Free cash flow margin"
  },
  {
    "figure_id": "F252",
    "report_id": "R018",
    "label": "EXHIBIT 24",
    "context": "EXHIBIT 24: Unimicron and Largan are the most capital intensive companies with our coverage Capex as % of revenue"
  },
  {
    "figure_id": "F253",
    "report_id": "R018",
    "label": "EXHIBIT 25",
    "context": "EXHIBIT 25: Luxshare has the highest Capex in 2025 within our coverage, followed by Delta Capex in 2025"
  },
  {
    "figure_id": "F254",
    "report_id": "R018",
    "label": "EXHIBIT 26",
    "context": "EXHIBIT 26: Largan and Unimicron presented the highest D&A to revenue ratio as a result of substantial capex-intensity D&A as % of revenue in 2025"
  },
  {
    "figure_id": "F255",
    "report_id": "R018",
    "label": "EXHIBIT 27",
    "context": "EXHIBIT 27: The Lens sector demonstrates greater capex intensity compared to module sector, and Apple suppliers typically incur higher capex than Android suppliers Capex as % of revenue in 2025 across the camera supply chain"
  },
  {
    "figure_id": "F256",
    "report_id": "R018",
    "label": "Exhibit 28",
    "context": "EXHIBIT 28: Geologically, Taiwanese companies typically have higher dividend payout ratios than mainland China companies Dividend payout ratio"
  },
  {
    "figure_id": "F257",
    "report_id": "R018",
    "label": "EXHIBIT 29",
    "context": "Gross TTM dividend yield"
  },
  {
    "figure_id": "F258",
    "report_id": "R018",
    "label": "EXHIBIT 30",
    "context": "EXHIBIT 30: Semi/Photonics represents \\~40% of Chroma's revenue and Power tester represents \\~55% (incl. the part under overseas & subsidiaries and Turnkey) Chroma revenue breakdown (Bernstein est. 2026E)"
  },
  {
    "figure_id": "F259",
    "report_id": "R018",
    "label": "EXHIBIT 31",
    "context": "EXHIBIT 31: We expect Chroma's SLT revenue to grow by c.80% in 2026"
  },
  {
    "figure_id": "F260",
    "report_id": "R018",
    "label": "EXHIBIT 32",
    "context": "EXHIBIT 32: We expect robust demand from AI datacenter power and semi/photonic products will drive Chroma to grow topline at 46% in 2025-28 Chroma ATE Revenue Mix"
  },
  {
    "figure_id": "F261",
    "report_id": "R018",
    "label": "EXHIBIT 33",
    "context": "EXHIBIT 33: We project Chroma's revenue to grow at a 46% CAGR in 2025-28 Chroma ATE Revenue and YoY"
  },
  {
    "figure_id": "F262",
    "report_id": "R018",
    "label": "EXHIBIT 34",
    "context": "EXHIBIT 34: We model EPS to grow at 43% CAGR in 2025-28, driven by higher-margin AI related revenue Chroma ATE EPS and YoY"
  },
  {
    "figure_id": "F263",
    "report_id": "R018",
    "label": "EXHIBIT 35",
    "context": "EXHIBIT 35: We model Chroma's revenue / EPS to grow at 46%/43% CAGR from 2025-28 EXHIBIT 36: Chroma is trading at 45x P/E"
  },
  {
    "figure_id": "F264",
    "report_id": "R018",
    "label": "EXHIBIT 37",
    "context": "EXHIBIT 37: Chroma is valued at 2.3x against TWSE Chroma ATE Relative P/E"
  },
  {
    "figure_id": "F265",
    "report_id": "R018",
    "label": "EXHIBIT 38",
    "context": "EXHIBIT 38: Chroma is valued at relatively higher P/E multiple vs. other Taiwanese equipment companies 1BF P/E for Taiwanese Equipment Companies"
  },
  {
    "figure_id": "F266",
    "report_id": "R018",
    "label": "Exhibit 39",
    "context": "Exhibit 39 - Exhibit 46) EXHIBIT 39: We expect Sunny Optical to grow at 12% CAGR in 2025-28 Sunny Optical revenue by application"
  },
  {
    "figure_id": "F267",
    "report_id": "R018",
    "label": "EXHIBIT 40",
    "context": "EXHIBIT 40: We model Sunny Optical's GM to see slightly decline in 2026 due to memory price impact while to recover in 2027"
  },
  {
    "figure_id": "F268",
    "report_id": "R018",
    "label": "EXHIBIT 41",
    "context": "EXHIBIT 41: We expect Sunny Optical's handset module and overall GM to decline slightly in 2026 amid surging memory price, and to rebound in 2027 as memory price pressure easing GM by Segment"
  },
  {
    "figure_id": "F269",
    "report_id": "R018",
    "label": "EXHIBIT 42",
    "context": "EXHIBIT 42: Overall we estimate Sunny Optical will achieve 12% revenue CAGR from 2025 to 2028... Sunny Optical Revenue and YoY"
  },
  {
    "figure_id": "F270",
    "report_id": "R018",
    "label": "EXHIBIT 43",
    "context": "EXHIBIT 43: ... and have 10% EPS CAGR in EPS over the same period (2025 includes an one-off gain) Sunny Optical EPS and YoY"
  },
  {
    "figure_id": "F271",
    "report_id": "R018",
    "label": "EXHIBIT 44",
    "context": "EXHIBIT 44: We expect Sunny Optical's GM to decline slightly in 2026 and rebound in 2027, with strong recovery of EPS in next year EXHIBIT 45: We set Sunny's target P/E at 18x"
  },
  {
    "figure_id": "F272",
    "report_id": "R018",
    "label": "EXHIBIT 46",
    "context": "EXHIBIT 46: Relative P/E against HSI index is at the lowest range compared to past 5 years"
  },
  {
    "figure_id": "F273",
    "report_id": "R020",
    "label": "Figure 2",
    "context": "KV Cache offloading - KV cache offloading refers to the architectural technique of dynamically transferring intermediate attention states (key-value tensors) from HBM into lower-cost, higher-capacity tiers such as DRAM and, increasingly, NAND flash, effectivel"
  },
  {
    "figure_id": "F274",
    "report_id": "R020",
    "label": "Figure 3",
    "context": "AMAT – We model total revenue growth of 30%/22% Y/Y in CY27/28, including 35%/25% from Silicon, and 14%/13% from AGS. We lift our TP to \\$710 from \\$550 prior, based on 31x P/E applied to CY28 EPS. The 31x P/E is consistent with our prior valuation and 55% abo"
  },
  {
    "figure_id": "F275",
    "report_id": "R021",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Beauty market growth rate has accelerated post Covid L'Oréal estimate of global beauty industry sales growth, 2010-25"
  },
  {
    "figure_id": "F276",
    "report_id": "R021",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Premium fragrances gained share of beauty market post Covid"
  },
  {
    "figure_id": "F277",
    "report_id": "R021",
    "label": "Exhibit 3",
    "context": "Exhibit 3: We think cohort expansion drove beauty and fragrance growth acceleration Beauty: average entry age by category (USA)"
  },
  {
    "figure_id": "F278",
    "report_id": "R021",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Largest six players account for two-thirds of premium fragrance sales Global premium fragrances breakdown by company, 2025"
  },
  {
    "figure_id": "F279",
    "report_id": "R021",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Interparfums is only exposed to fragrances, while Puig and L'Oréal are more diversified Revenue mix from fragrances, FY25"
  },
  {
    "figure_id": "F280",
    "report_id": "R021",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Newness continues to resonate, with interest in fresh blockbusters tracking ahead of past launches Indexed searches for Good Girl vs La Bomba in first 12 months"
  },
  {
    "figure_id": "F281",
    "report_id": "R021",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Even before the recent fragrance supercycle blockbusters have long been a durable growth engine L'Oréal fragrance organic sales growth, FY10-25"
  },
  {
    "figure_id": "F282",
    "report_id": "R021",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Good Girl surpassed $3\\%$ share in six years Good Girl: women's fragrance market share, 2022 vs 2016"
  },
  {
    "figure_id": "F283",
    "report_id": "R021",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Jimmy Choo scaled through new pillars Jimmy Choo and Montblanc net sales in EURm, 2011-25 Jimmy Choo and Montblanc scaled through a disciplined pillar-and-flanker playbook"
  },
  {
    "figure_id": "F284",
    "report_id": "R023",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Indirect financing, predominantly loans, has seen its share in Total Social Financing (TSF) increments decline from over 80% to 45% by 2025"
  },
  {
    "figure_id": "F285",
    "report_id": "R023",
    "label": "Exhibit 2",
    "context": "Exhibit 2: The central bank emphasizes that enhancing the quality and efficiency of loans is paramount, suggesting that “slower, higher-quality loan growth” is likely to become a new normal for the economy"
  },
  {
    "figure_id": "F286",
    "report_id": "R023",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Among the banks we cover, Industrial Bank, Huaxia Bank, and BONB exhibit the highest interbank liability proportion, recorded at 29%, 26%, and 22% respectively in 2025, in contrast to 15% for the large four SOE banks As"
  },
  {
    "figure_id": "F287",
    "report_id": "R023",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Among the banks we cover, BONB, BONJ, and BOC exhibit the highest proportions of trading accounts within their investment assets, recorded at 67%, 67%, and 55% respectively As of 2025"
  },
  {
    "figure_id": "F288",
    "report_id": "R023",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Regulatory support for launching active ETFs on a pilot basis, alongside the listing of the first batch of C-REITs, is likely to increase on-exchange liquidity and stimulate associated market flows"
  },
  {
    "figure_id": "F289",
    "report_id": "R023",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Structural expansion of the listing ecosystem broadens the addressable deal universe"
  },
  {
    "figure_id": "F290",
    "report_id": "R024",
    "label": "Exhibit 2",
    "context": "Exhibit 3: MSCI China vs. Retail Sales"
  },
  {
    "figure_id": "F291",
    "report_id": "R024",
    "label": "Exhibit 4",
    "context": "Exhibit 4: China Retail Sales by Category"
  },
  {
    "figure_id": "F292",
    "report_id": "R024",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Online Retail Sales"
  },
  {
    "figure_id": "F293",
    "report_id": "R024",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Discretionary Categories"
  },
  {
    "figure_id": "F294",
    "report_id": "R024",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Retail Sales Growth"
  },
  {
    "figure_id": "F295",
    "report_id": "R024",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Restaurants & Dining"
  },
  {
    "figure_id": "F296",
    "report_id": "R024",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Staples Categories"
  },
  {
    "figure_id": "F297",
    "report_id": "R024",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Discretionary as a % of 2019"
  },
  {
    "figure_id": "F298",
    "report_id": "R024",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Staples as a % of 2019"
  },
  {
    "figure_id": "F299",
    "report_id": "R024",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Office & Mobile Categories"
  },
  {
    "figure_id": "F300",
    "report_id": "R024",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Other Categories"
  },
  {
    "figure_id": "F301",
    "report_id": "R025",
    "label": "Exhibit 1",
    "context": "Exhibit 1: We estimate that oil E&Ps currently discount an average WTI price of \\~\\$65/bbl, well below the current 12-month strip of \\~\\$75."
  },
  {
    "figure_id": "F302",
    "report_id": "R025",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Seaborne net exports from the US sit \\~4 mb/d higher than last year... United States Seaborne net exports (crude + products, 30-day avg, mb/d)"
  },
  {
    "figure_id": "F303",
    "report_id": "R025",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Based on known tanker movements, it appears net seaborne oil imports into China will be down even further in June vs May. China seaborne total-petroleum net imports: firming fan"
  },
  {
    "figure_id": "F304",
    "report_id": "R025",
    "label": "Exhibit 3",
    "context": "Exhibit 3: While net seaborne imports into China have maintained their downward trend. China"
  },
  {
    "figure_id": "F305",
    "report_id": "R025",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Global SPR releases are running at 2.5 mb/d during Apr-Jun, but are set to fall sharply to 0.7 mb/d in July and August. Global strategic stock draws by"
  },
  {
    "figure_id": "F306",
    "report_id": "R025",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Global oil and refined product inventories have been drawing rapidly since the start of the conflict. Observable crude oil and oil products inventories"
  },
  {
    "figure_id": "F307",
    "report_id": "R025",
    "label": "Exhibit 8",
    "context": "Exhibit 8: OECD oil stocks have fallen further below 5-year averages, driven by a large draw in the US... Total Crude Oil Inventories (mln bbls)"
  },
  {
    "figure_id": "F308",
    "report_id": "R025",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Implied US product demand has held up well so far..."
  },
  {
    "figure_id": "F309",
    "report_id": "R025",
    "label": "Exhibit 7",
    "context": "Exhibit 7: ...including large draws in commercial storage. Observable crude oil and oil products inventories"
  },
  {
    "figure_id": "F310",
    "report_id": "R025",
    "label": "Exhibit 9",
    "context": "Exhibit 9: ...While refined product stocks have continued to grind lower as well Total Refined Products Inventories (mln bbls)"
  },
  {
    "figure_id": "F311",
    "report_id": "R025",
    "label": "Exhibit 11",
    "context": "Exhibit 11: ...with gasoline consumption still within normal"
  },
  {
    "figure_id": "F312",
    "report_id": "R025",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Our oil-weighted coverage would offer an average 2027 FCF yield of 11% near the current strip (\\~\\$72), 13% looking just at E&Ps. This would rise to 19% at \\$105, and fall to 5% at \\$55."
  },
  {
    "figure_id": "F313",
    "report_id": "R025",
    "label": "Exhibit 14",
    "context": "Exhibit 14: We estimate total shareholder return yield of 8% at current strip for our oil-weighted coverage. This would increase to 13% at \\$105 WTI and decrease to 5% at \\$55."
  },
  {
    "figure_id": "F314",
    "report_id": "R025",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Gas E&Ps offer an average 2027 FCF yield of 9% at \\$3.50 (near the HH strip). This would rise to 14% at \\$4.50 and fall to 4% at \\$2.50."
  },
  {
    "figure_id": "F315",
    "report_id": "R025",
    "label": "Exhibit 13",
    "context": "Exhibit 13: We estimate consensus is currently pricing in \\~\\$72 WTI (near strip) in 2027 for our oil-weighted coverage. Oil-Weighted Upside/Downside to Consensus 2027 EBITDAX"
  },
  {
    "figure_id": "F316",
    "report_id": "R025",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Oil E&Ps have roughly 5% of their production hedged in 2027."
  },
  {
    "figure_id": "F317",
    "report_id": "R025",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Gas E&Ps have hedged \\~30% of estimated 2027 production on average. % of 2027 Production Hedged (Upside Limit)"
  },
  {
    "figure_id": "F318",
    "report_id": "R025",
    "label": "Exhibit 18",
    "context": "Exhibit 18: The US Oil E&P sector reflects an average WTI price of \\~\\$66/bbl, or \\~13% below 12-month strip of \\~\\$75/bbl."
  },
  {
    "figure_id": "F319",
    "report_id": "R025",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Gas E&Ps reflect a median Henry Hub price of \\~\\$3.38/mmbtu, in-line with 12-month strip."
  },
  {
    "figure_id": "F320",
    "report_id": "R025",
    "label": "Exhibit 20",
    "context": "Exhibit 20: We estimate a median 2026 FCF yield of 12% for oil producers."
  },
  {
    "figure_id": "F321",
    "report_id": "R025",
    "label": "Exhibit 22",
    "context": "Exhibit 22: The median EV/EBITDAX at \\$80 WTI is 4.7x."
  },
  {
    "figure_id": "F322",
    "report_id": "R025",
    "label": "Exhibit 21",
    "context": "Exhibit 21: The median for total shareholder return sits at 8%."
  },
  {
    "figure_id": "F323",
    "report_id": "R025",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Net leverage for the group sits at 0.5x."
  },
  {
    "figure_id": "F324",
    "report_id": "R025",
    "label": "Exhibit 24",
    "context": "Exhibit 24: We estimate median 2027 FCF yield of 11% for our oil producer coverage ( $\\sim$ 13% for just E&Ps), with the highest from PR, CHRD & DVN."
  },
  {
    "figure_id": "F325",
    "report_id": "R025",
    "label": "Exhibit 25",
    "context": "Exhibit 25: The median total shareholder return yield for the group sits at 8%."
  },
  {
    "figure_id": "F326",
    "report_id": "R025",
    "label": "Exhibit 26",
    "context": "Exhibit 26: We estimate EV/EBITDAX for oil producers next year at roughly 4.7x."
  },
  {
    "figure_id": "F327",
    "report_id": "R025",
    "label": "Exhibit 27",
    "context": "Exhibit 27: Net debt/EBITDAX sits at 0.5x, with the lowest from PR, CHRD and EOG."
  },
  {
    "figure_id": "F328",
    "report_id": "R025",
    "label": "Exhibit 32",
    "context": "Exhibit 32: At \\$3.50 Henry Hub in 2027 (near strip), our gas-weighted coverage would offer a median FCF/equity yield of 9%, with the highest for AR and EXE..."
  },
  {
    "figure_id": "F329",
    "report_id": "R025",
    "label": "Exhibit 33",
    "context": "Exhibit 33: ...with FCF/EV sitting at a median of \\~7%."
  },
  {
    "figure_id": "F330",
    "report_id": "R025",
    "label": "Exhibit 34",
    "context": "Exhibit 34: Net Debt/EBITDAX would sit at a median of 0.3x at \\$3.50..."
  },
  {
    "figure_id": "F331",
    "report_id": "R025",
    "label": "Exhibit 35",
    "context": "Exhibit 35: ...with EV/EBITDAX at 5.2x"
  },
  {
    "figure_id": "F332",
    "report_id": "R025",
    "label": "Exhibit 40",
    "context": "Exhibit 40: WoW Energy Subsector Performance WoW Performance"
  },
  {
    "figure_id": "F333",
    "report_id": "R025",
    "label": "Exhibit 41",
    "context": "Exhibit 41: YTD Energy Subsector Performance YTD Performance"
  },
  {
    "figure_id": "F334",
    "report_id": "R025",
    "label": "Exhibit 42",
    "context": "Exhibit 42: Best and Worst E&P WoW Performance Best and Worst WoW Performance"
  },
  {
    "figure_id": "F335",
    "report_id": "R025",
    "label": "Exhibit 43",
    "context": "Exhibit 43: WoW Performance by E&P Subsector WoW Performance"
  },
  {
    "figure_id": "F336",
    "report_id": "R025",
    "label": "Exhibit 44",
    "context": "Exhibit 44: At our price deck of \\~\\$88 WTI in 2026, we forecast a median realized price of \\~\\$85/bbl for our oil coverage. EOG, MUR and APA have the highest realized prices due to limited hedges and/or geographic mix. 2026 Reali"
  },
  {
    "figure_id": "F337",
    "report_id": "R026",
    "label": "Figure 1",
    "context": "Figure 1: HK private residential market – % of “Mainland Chinese” buyers with a last name in Mandarin pinyin (by volume)"
  },
  {
    "figure_id": "F338",
    "report_id": "R026",
    "label": "Figure 2",
    "context": "Figure 2: HK private residential market – % of “Mainland Chinese” buyers with a last name in Mandarin pinyin (by value)"
  },
  {
    "figure_id": "F339",
    "report_id": "R026",
    "label": "Figure 3",
    "context": "Note: “Mainland Chinese” is defined here using the Mandarin pinyin of the buyer’s last name and does not distinguish the buyer’s current residence or identity. As a result, “Mainland Chinese” who are residing in Hong Kong—as well as local Hong Kong residents w"
  },
  {
    "figure_id": "F340",
    "report_id": "R030",
    "label": "Figure 1",
    "context": "Figure 1: Grab ASEAN avg daily orders MoM %"
  },
  {
    "figure_id": "F341",
    "report_id": "R030",
    "label": "Figure 2",
    "context": "Figure 2: Grab ASEAN total orders YoY %"
  },
  {
    "figure_id": "F342",
    "report_id": "R030",
    "label": "Figure 3",
    "context": "Figure 3: Grab's MoM daily avg order volumes across markets Grab ASEAN avg daily order May-26 vs Apr-26 (MoM)"
  },
  {
    "figure_id": "F343",
    "report_id": "R030",
    "label": "Figure 4",
    "context": "Figure 4: Grab's YoY total orders across markets Grab ASEAN total order May-26 vs May-25 (YoY)"
  },
  {
    "figure_id": "F344",
    "report_id": "R030",
    "label": "Figure 5",
    "context": "Figure 5: Grab's MoM AOV across markets Grab ASEAN AOV May-26 vs Apr-26 (MoM)"
  },
  {
    "figure_id": "F345",
    "report_id": "R030",
    "label": "Figure 6",
    "context": "Figure 6: Grab's YoY AOV across markets Grab ASEAN AOV May-26 vs May-25 (YoY)"
  },
  {
    "figure_id": "F346",
    "report_id": "R030",
    "label": "Figure 7",
    "context": "Figure 7: Shopee's ASEAN avg daily GMV MoM %"
  },
  {
    "figure_id": "F347",
    "report_id": "R030",
    "label": "Figure 8",
    "context": "Figure 8: Shopee's ASEAN GMV YoY %"
  },
  {
    "figure_id": "F348",
    "report_id": "R030",
    "label": "Figure 9",
    "context": "Figure 9: Shopee's ASEAN avg daily orders MoM %"
  },
  {
    "figure_id": "F349",
    "report_id": "R030",
    "label": "Figure 10",
    "context": "Figure 10: Shopee's ASEAN total orders YoY %"
  },
  {
    "figure_id": "F350",
    "report_id": "R030",
    "label": "Figure 11",
    "context": "Figure 11: Shopee ASEAN AOV MoM %"
  },
  {
    "figure_id": "F351",
    "report_id": "R030",
    "label": "Figure 12",
    "context": "Figure 12: Shopee ASEAN AOV YoY %"
  },
  {
    "figure_id": "F352",
    "report_id": "R030",
    "label": "Figure 13",
    "context": "Figure 13: Shopee's ASEAN MoM GMV across countries Shopee GMV May-26 vs Apr-26 (MoM)"
  },
  {
    "figure_id": "F353",
    "report_id": "R030",
    "label": "Figure 14",
    "context": "Figure 14: Shopee's ASEAN YoY GMV across countries Shopee GMV May-26 vs May-25 (YoY)"
  },
  {
    "figure_id": "F354",
    "report_id": "R030",
    "label": "Figure 15",
    "context": "Figure 15: Shopee's ASEAN MoM avg daily volumes across countries Avg daily order MoM % (May-26 vs Apr-26)"
  },
  {
    "figure_id": "F355",
    "report_id": "R030",
    "label": "Figure 16",
    "context": "Figure 16: Shopee's ASEAN YoY total volumes across countries Total orders YoY % (May-26 vs May-25)"
  },
  {
    "figure_id": "F356",
    "report_id": "R030",
    "label": "Figure 17",
    "context": "Figure 17: Shopee's ASEAN AOV MoM across countries AOV MoM % (May-26 vs Apr-26)"
  },
  {
    "figure_id": "F357",
    "report_id": "R030",
    "label": "Figure 18",
    "context": "Figure 18: Shopee's ASEAN AOV YoY across countries AOV YoY (May-26 vs May-25)"
  },
  {
    "figure_id": "F358",
    "report_id": "R030",
    "label": "Figure 19",
    "context": "Figure 19: Food delivery market avg daily orders Indonesia: Average daily orders and YoY growth"
  },
  {
    "figure_id": "F359",
    "report_id": "R030",
    "label": "Figure 20",
    "context": "MoM change: 2026-05: +0%; MoM change: 2026-04: +7%; MoM change: +8%. The chart displays a single series of values for each month from Apr-26 to Apr-27, with the YoY% (RHS) axis ranging from -1% to +4%. The data is presented as a grouped bar chart with two dist"
  },
  {
    "figure_id": "F360",
    "report_id": "R030",
    "label": "Figure 22",
    "context": "Figure 22: Non-delivery fees as a % AOV"
  },
  {
    "figure_id": "F361",
    "report_id": "R030",
    "label": "Figure 21",
    "context": "Figure 21: Delivery fees as a % AOV"
  },
  {
    "figure_id": "F362",
    "report_id": "R030",
    "label": "Figure 23",
    "context": "Figure 23: Discounts as a % AOV"
  },
  {
    "figure_id": "F363",
    "report_id": "R030",
    "label": "Figure 24",
    "context": "Figure 24: Food delivery market avg daily orders Malaysia: Average daily orders and YoY growth"
  },
  {
    "figure_id": "F364",
    "report_id": "R030",
    "label": "Figure 25",
    "context": "Figure 25: Food delivery market share"
  },
  {
    "figure_id": "F365",
    "report_id": "R030",
    "label": "Figure 26",
    "context": "Figure 26: AOV"
  },
  {
    "figure_id": "F366",
    "report_id": "R030",
    "label": "Figure 27",
    "context": "Figure 27: Delivery fees as a % AOV"
  },
  {
    "figure_id": "F367",
    "report_id": "R030",
    "label": "Figure 28",
    "context": "Figure 28: Non-delivery fee as a % AOV"
  },
  {
    "figure_id": "F368",
    "report_id": "R030",
    "label": "Figure 29",
    "context": "Figure 29: Discounts as a % AOV"
  },
  {
    "figure_id": "F369",
    "report_id": "R030",
    "label": "Figure 30",
    "context": "Figure 30: Food delivery market avg daily orders Philippines: Average daily orders and YoY growth"
  },
  {
    "figure_id": "F370",
    "report_id": "R030",
    "label": "Figure 31",
    "context": "Figure 31: Food delivery market share"
  },
  {
    "figure_id": "F371",
    "report_id": "R030",
    "label": "Figure 32",
    "context": "Figure 32: AOV"
  },
  {
    "figure_id": "F372",
    "report_id": "R030",
    "label": "Figure 33",
    "context": "Figure 33: Delivery fees as a % AOV"
  },
  {
    "figure_id": "F373",
    "report_id": "R030",
    "label": "Figure 34",
    "context": "Figure 34: Non-delivery fee as a % AOV"
  },
  {
    "figure_id": "F374",
    "report_id": "R030",
    "label": "Figure 35",
    "context": "Figure 35: Discounts as a % AOV"
  },
  {
    "figure_id": "F375",
    "report_id": "R030",
    "label": "Figure 36",
    "context": "Figure 36: Food delivery market avg daily orders Singapore: Average daily orders and YoY growth"
  },
  {
    "figure_id": "F376",
    "report_id": "R030",
    "label": "Figure 37",
    "context": "Figure 37: Food delivery market share"
  },
  {
    "figure_id": "F377",
    "report_id": "R030",
    "label": "Figure 38",
    "context": "Figure 38: AOV"
  },
  {
    "figure_id": "F378",
    "report_id": "R030",
    "label": "Figure 39",
    "context": "Figure 39: Delivery fees as a % AOV"
  },
  {
    "figure_id": "F379",
    "report_id": "R030",
    "label": "Figure 40",
    "context": "Figure 40: Non-delivery fee as a % AOV"
  },
  {
    "figure_id": "F380",
    "report_id": "R030",
    "label": "Figure 41",
    "context": "Figure 41: Discounts as a % AOV"
  },
  {
    "figure_id": "F381",
    "report_id": "R030",
    "label": "Figure 42",
    "context": "Figure 42: Food delivery market avg daily orders Thailand: Average daily orders and YoY growth"
  },
  {
    "figure_id": "F382",
    "report_id": "R030",
    "label": "Figure 43",
    "context": "Figure 43: Food delivery market share"
  },
  {
    "figure_id": "F383",
    "report_id": "R030",
    "label": "Figure 44",
    "context": "Figure 44: AOV"
  },
  {
    "figure_id": "F384",
    "report_id": "R030",
    "label": "Figure 45",
    "context": "Figure 45: Delivery fees as a % AOV"
  },
  {
    "figure_id": "F385",
    "report_id": "R030",
    "label": "Figure 46",
    "context": "Figure 46: Non-delivery fee as a % AOV"
  },
  {
    "figure_id": "F386",
    "report_id": "R030",
    "label": "Figure 47",
    "context": "Figure 47: Discounts as a % AOV"
  },
  {
    "figure_id": "F387",
    "report_id": "R030",
    "label": "Figure 48",
    "context": "Figure 48: Food delivery market avg daily orders Vietnam: Average daily orders and YoY growth"
  },
  {
    "figure_id": "F388",
    "report_id": "R030",
    "label": "Figure 49",
    "context": "MoM change: 2026-05: 10%; 2026-04: 1%; 2026-03: 34% Figure 49: AOV"
  },
  {
    "figure_id": "F389",
    "report_id": "R030",
    "label": "Figure 51",
    "context": "Figure 51: Non-delivery fee as a % AOV"
  },
  {
    "figure_id": "F390",
    "report_id": "R030",
    "label": "Figure 50",
    "context": "Figure 50: Delivery fees as a % AOV"
  },
  {
    "figure_id": "F391",
    "report_id": "R030",
    "label": "Figure 52",
    "context": "Figure 52: Discounts as a % AOV"
  },
  {
    "figure_id": "F392",
    "report_id": "R030",
    "label": "Figure 53",
    "context": "Figure 53: Shopee Indonesia GMV"
  },
  {
    "figure_id": "F393",
    "report_id": "R030",
    "label": "Figure 54",
    "context": "Figure 54: Shopee Indonesia Order Volumes Indonesia - Average daily order and YoY growth"
  },
  {
    "figure_id": "F394",
    "report_id": "R030",
    "label": "Figure 55",
    "context": "Figure 55: Shopee Indonesia AOV"
  },
  {
    "figure_id": "F395",
    "report_id": "R030",
    "label": "Figure 56",
    "context": "Figure 56: Shopee Indonesia Delivery Fee as a % AOV"
  },
  {
    "figure_id": "F396",
    "report_id": "R030",
    "label": "Figure 57",
    "context": "Figure 57: Shopee Indonesia Promotions as a % AOV"
  },
  {
    "figure_id": "F397",
    "report_id": "R030",
    "label": "Figure 58",
    "context": "Figure 58: Shopee Indonesia Service Fee as a % AOV"
  },
  {
    "figure_id": "F398",
    "report_id": "R030",
    "label": "Figure 59",
    "context": "Figure 59: Shopee Malaysia GMV Malaysia - Average daily GMV and YoY growth"
  },
  {
    "figure_id": "F399",
    "report_id": "R030",
    "label": "Figure 60",
    "context": "Figure 60: Shopee Malaysia Order Volumes Malaysia - Average daily order and YoY growth"
  },
  {
    "figure_id": "F400",
    "report_id": "R030",
    "label": "Figure 61",
    "context": "Figure 61: Shopee Malaysia AOV"
  },
  {
    "figure_id": "F401",
    "report_id": "R030",
    "label": "Figure 62",
    "context": "Figure 62: Shopee Malaysia Delivery Fee as a % AOV"
  },
  {
    "figure_id": "F402",
    "report_id": "R030",
    "label": "Figure 63",
    "context": "Figure 63: Shopee Malaysia Promotions as a % AOV"
  },
  {
    "figure_id": "F403",
    "report_id": "R030",
    "label": "Figure 64",
    "context": "Figure 64: Shopee Philippines GMV Philippines - Average daily GMV and YoY growth"
  },
  {
    "figure_id": "F404",
    "report_id": "R030",
    "label": "Figure 65",
    "context": "Figure 65: Shopee Philippines Order Volumes Philippines - Average daily order and YoY growth"
  },
  {
    "figure_id": "F405",
    "report_id": "R030",
    "label": "Figure 66",
    "context": "Figure 66: Shopee Philippines AOV"
  },
  {
    "figure_id": "F406",
    "report_id": "R030",
    "label": "Figure 67",
    "context": "Figure 67: Shopee Philippines Delivery Fee as a % AOV"
  },
  {
    "figure_id": "F407",
    "report_id": "R030",
    "label": "Figure 68",
    "context": "Figure 68: Shopee Philippines Promotions as a % AOV"
  },
  {
    "figure_id": "F408",
    "report_id": "R030",
    "label": "Figure 69",
    "context": "Figure 69: Shopee Singapore GMV Singapore - Average daily GMV and YoY growth"
  },
  {
    "figure_id": "F409",
    "report_id": "R030",
    "label": "Figure 70",
    "context": "Figure 70: Shopee Singapore Order Volumes Singapore - Average daily order and YoY growth"
  },
  {
    "figure_id": "F410",
    "report_id": "R030",
    "label": "Figure 71",
    "context": "Figure 71: Shopee Singapore AOV"
  },
  {
    "figure_id": "F411",
    "report_id": "R030",
    "label": "Figure 72",
    "context": "Figure 72: Shopee Singapore Delivery Fee as a % AOV"
  },
  {
    "figure_id": "F412",
    "report_id": "R030",
    "label": "Figure 73",
    "context": "Figure 73: Shopee Singapore Promotions as a % AOV"
  },
  {
    "figure_id": "F413",
    "report_id": "R030",
    "label": "Figure 74",
    "context": "Figure 74: Shopee Thailand GMV Thailand - Average daily GMV and YoY growth"
  },
  {
    "figure_id": "F414",
    "report_id": "R030",
    "label": "Figure 75",
    "context": "Figure 75: Shopee Thailand Order Volumes Thailand - Average daily order and YoY growth"
  },
  {
    "figure_id": "F415",
    "report_id": "R030",
    "label": "Figure 76",
    "context": "Figure 76: Shopee Thailand AOV"
  },
  {
    "figure_id": "F416",
    "report_id": "R030",
    "label": "Figure 77",
    "context": "Figure 77: Shopee Thailand Delivery Fee as a % AOV"
  },
  {
    "figure_id": "F417",
    "report_id": "R030",
    "label": "Figure 78",
    "context": "Figure 78: Shopee Thailand Promotions as a % AOV"
  },
  {
    "figure_id": "F418",
    "report_id": "R030",
    "label": "Figure 79",
    "context": "Figure 79: Shopee Vietnam GMV Vietnam - Average daily GMV and YoY growth"
  },
  {
    "figure_id": "F419",
    "report_id": "R030",
    "label": "Figure 80",
    "context": "Figure 80: Shopee Vietnam Order Volumes Vietnam - Average daily order and YoY growth"
  },
  {
    "figure_id": "F420",
    "report_id": "R030",
    "label": "Figure 81",
    "context": "Figure 81: Shopee Vietnam AOV"
  },
  {
    "figure_id": "F421",
    "report_id": "R030",
    "label": "Figure 82",
    "context": "Figure 82: Shopee Vietnam Delivery Fee as a % AOV"
  },
  {
    "figure_id": "F422",
    "report_id": "R030",
    "label": "Figure 83",
    "context": "Figure 83: Shopee Vietnam Promotions as a % AOV"
  },
  {
    "figure_id": "F423",
    "report_id": "R031",
    "label": "Exhibit 2",
    "context": "Exhibit 3 - Exhibit 4) EXHIBIT 2: Chinese autos retail sales came in at 1.51mn units in May 2026, -20.0% yoy"
  },
  {
    "figure_id": "F424",
    "report_id": "R031",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: BYD Group (incl. BYD, Denza, Fangchengbao, and Yangwang) came back to the top with 186k units, 13.4% share, followed by Geely Group (incl. Galaxy, Geometry, Zeekr, and Lynk&Co) with 144k units, 10.4% PV market share, and"
  },
  {
    "figure_id": "F425",
    "report_id": "R031",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: BYD Group remained the largest EV seller in China with volume and share stabilizing to 198k units and 21.4%; Geely Group ranked second with 111k units and 12% share, followed by Leapmotor at 63k units (6.8%)"
  },
  {
    "figure_id": "F426",
    "report_id": "R031",
    "label": "Exhibit 5",
    "context": "EXHIBIT 5: After a sharp decline during COVID, China's PV SAAR rebounded strongly. However, growth has slowed in recent months, with April 2026 dropping to 19.6mn units, down from 20.7mn in March 2026 and well below 23.6mn in April"
  },
  {
    "figure_id": "F427",
    "report_id": "R031",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: Excluding both imports and exports, we estimate that the average of aggregate SAAR of cars produced and sold domestically in China reached 18.0mn units in May, lower than the domestic retail SAAR of 18.2mn units"
  },
  {
    "figure_id": "F428",
    "report_id": "R031",
    "label": "Exhibit 7",
    "context": "EXHIBIT 7: Retail volumes of premium market brand cars declined by -13.5% yoy for May"
  },
  {
    "figure_id": "F429",
    "report_id": "R031",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: Retail sales volume of mass market brand cars plunged -21.1% yoy in May"
  },
  {
    "figure_id": "F430",
    "report_id": "R031",
    "label": "Exhibit 9",
    "context": "EXHIBIT 9: Overall EV sales (BEV & PHEV) growth fell -5.8% YoY to 828k units in April, but improved from March (-17.7%), underpinned by the rollout of new models and rising oil prices"
  },
  {
    "figure_id": "F431",
    "report_id": "R031",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: By city tier, BEV penetration rates in Tier 1, 2, and 3 cities came at 42%, 37%, and 32% as of May 2026 EXHIBIT 11: PHEV penetration maintained 17% across Tier 1, 2, and 3 cities"
  },
  {
    "figure_id": "F432",
    "report_id": "R031",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: In May 2026, BEV sales grew +8.3% yoy and PHEV decelerated to -25.4% yoy"
  },
  {
    "figure_id": "F433",
    "report_id": "R031",
    "label": "Exhibit 13",
    "context": "EXHIBIT 13: There were 40k units of net channel inventory destocking in May, compared to 23k net destocking in April"
  },
  {
    "figure_id": "F434",
    "report_id": "R031",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: EV net channel inventory increased by 120k units in May and 87k units in April"
  },
  {
    "figure_id": "F435",
    "report_id": "R031",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: Retail pricing sees moderate pressure due to the weak end-market demand; like-for-like pricing was -1,114 basis points in May, vs. -1,020 basis points yoy in April 2026"
  },
  {
    "figure_id": "F436",
    "report_id": "R031",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 16: Both imported and domestic premium brand discounts increased moderately in May"
  },
  {
    "figure_id": "F437",
    "report_id": "R031",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 17: Mass market EV discounts declined moderately in April 2026, while IC discounts increased"
  },
  {
    "figure_id": "F438",
    "report_id": "R031",
    "label": "EXHIBIT 18",
    "context": "EXHIBIT 18: Dongfeng Nissan, SGM Wuling, and Geely have seen the most restocking on a cumulative LTM basis LTM inventory build vs. last 3 month retail sales rate"
  },
  {
    "figure_id": "F439",
    "report_id": "R031",
    "label": "EXHIBIT 19",
    "context": "EXHIBIT 19: Among EV pure players, Denza, Ora, BYD, Leapmotor and Zeeker's channel inventory levels are relatively high; conversely, Wey and Tesla destocked the most recently LTM: EV inventory build vs last 3 month retail sales ra"
  },
  {
    "figure_id": "F440",
    "report_id": "R031",
    "label": "Exhibit 20",
    "context": "EXHIBIT 20: Export volume in May 2026 grew +73% yoy – ICE +38%, EV +119%"
  },
  {
    "figure_id": "F441",
    "report_id": "R031",
    "label": "Exhibit 21",
    "context": "EXHIBIT 21: We estimate China's credit impulse was 20.2% in May 2026..."
  },
  {
    "figure_id": "F442",
    "report_id": "R031",
    "label": "EXHIBIT 22",
    "context": "EXHIBIT 22: ... declining from $21.7\\%$ a year ago. 12 month change in Bloomberg's credit impulse deteriorated further to $-2.3\\%$ this month, marking a continued downturn after its first negative print in March, which ended an 11-m"
  },
  {
    "figure_id": "F443",
    "report_id": "R031",
    "label": "EXHIBIT 23",
    "context": "EXHIBIT 23: Auto loan issuance volume rebounded in April 2026"
  }
]