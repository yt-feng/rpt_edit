请基于下面每天新报告的摘要，写一份“市场最新观点汇总”的结构化 JSON，用于生成 PDF。

要求：
1. 观点要分门别类，例如：宏观与利率、AI/算力、能源与大宗、地产与消费、区域市场、风险偏好等。类别由内容决定，不要机械套模板。
2. 每个板块要综合多篇报告，不要逐篇复述。
3. 每个板块必须有 3-8 个要点，每个要点是可读的完整句子。
4. 每个板块末尾必须给 references，引用报告 ID，不要在正文每句后塞引用。
5. 可以使用所有 figure_ids，没有总数限制，但只选择真正支撑该板块观点且图表说明干净的图。
6. 投行名字必须脱敏：常见投行写 GS、JPM、MS、BofA、Citi、UBS、DB 等缩写，不确定就写“投行”。
7. 不要给投资建议，不要写买卖评级。
8. 输出必须是 JSON 对象，不要 Markdown 代码块。

JSON 格式：
{"title":"市场最新观点汇总","subtitle":"一句话说明今天的市场主线","executive_summary":["要点1"],"sections":[{"heading":"板块标题","thesis":"核心判断","bullets":["要点1"],"figure_ids":["F001"],"references":["R001"]}],"closing":"简短收束"}

报告摘要：
[
  {
    "id": "R001",
    "title": "中国WFE进口的真正信号：不是需求放缓，而是供给瓶颈下的结构性分化",
    "digest": "[wechat_article.md]\n# 中国WFE进口的真正信号：不是需求放缓，而是供给瓶颈下的结构性分化\n\n2026年4月中国WFE进口数据出炉，单月27亿美元，同比下降3%，年初至今累计同比下降13%。表面上看，这是一组“降温”的数字。但深入拆解后会发现，真正驱动下行的并非中国半导体设备需求转弱，而是光刻机供给侧的硬约束——而这恰好揭示了当前中国半导体设备市场的结构性真相：非光刻设备仍在增长，海外设备商的收入结构正在经历一次深度再定价。\n\n这份来自某外资投行的月度进口追踪报告，为我们提供了比市场共识更精细的观察框架。它告诉我们：不要被总量数字迷惑，真正的投资信号藏在设备类型、进口来源和公司层面的回归分析里。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 光刻机进口的断崖式下滑是供给问题，不是需求问题\n\n4月光刻机进口仅有1.42亿美元，同比下滑60%，创下2022年7月以来的最低月度纪录。从荷兰进口的光刻机金额环比骤降87%，同比下滑65%。这一数字如此极端，以至于报告直接用“extremely low”来描述。\n\n但关键判断在于：报告明确指出，这并非需求萎缩，而是供给受限。某荷兰光刻机巨头在Q1业绩会上已重申，2026年中国收入占比将从2025年的33%降至20%。报告的分析师进一步指出，如果该公司的DUV产能供给改善，中国收入存在超出指引的上行空间。\n\n这意味着什么？当前市场对光刻机进口数据的解读，很可能高估了中国半导体产能扩张放缓的程度，而低估了供给端约束的暂时性。一旦供给瓶颈缓解，被压抑的需求可能集中释放。对于投资者而言，真正需要关注的不是光刻机进口的月度波动，而是中国晶圆厂在非光刻设备上的持续投入——这部分数据才是需求韧性的真实映射。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 排除光刻\n\n[... middle omitted ...]\n\n度收入跟踪。欢迎加入，一起拆解中国半导体设备市场的真实图景。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国半导体设备进口，4月数据怎么看？\n\n📊 进口数据：表面冷，内里热\n\n4月中国半导体设备进口27亿美元，环比下降12%，同比下降3%。年初至今累计100亿美元，同比下滑13%。但别急着下结论——这主要是光刻机供给受限拖的。\n\n📉 光刻机：拖后腿的主力\n\n4月光刻机进口仅1.42亿美元，同比暴跌60%，创下近两年最低。从荷兰进口的光刻机只有8700万欧元，环比骤降87%。这直接导致ASML中国区Q1系统销售预计仅4.4亿欧元，环比跌64%，同比跌71%。中国区收入占比预计从去年的33%降到今年20%左右。\n\n但ASML管理层也说了，中国需求依然强劲，只是供给端受限。如果DUV产能改善，存在上调指引的可能。\n\n📈 其他设备：悄悄在涨\n\n去除光刻机后，其他设备进口环比增长15%，同比增长5%。沉积设备4月进口8.68亿美元，同比增长36%，环比增长56%。从新加坡和马来西亚的进口同比增长28%，显示供应链正在重新布局。\n\n🔍 各家设备商的中国收入推演\n\n基于4月进口数据，各家Q2中国区收入走向分化：\n- 泛林：中国收入预计环比降28%，占比约22%\n- 应用材料：刚公布的Q1中国收入占比26.4%，与模型吻合\n-\n\n[... middle omitted ...]\n\nges/d465a89c1f3ab586280c46033bfd4fea9779be3907fd2feb6839cef3714a425a.jpg)\n\nZheng Cui\n\n+852 2123 2694\n\nzheng.cui@bernsteinsg.com\n\n![](images/d9d8ed37e3ea8b075395f8180ef0263818dffe32721ae45394a9\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R002",
    "title": "中国出口的真相：不是全面复苏，而是“AI+能源”的窄脉冲",
    "digest": "[wechat_article.md]\n# 中国出口的真相：不是全面复苏，而是“AI+能源”的窄脉冲\n\n年初的时候，市场对中国出口的预期普遍偏谨慎。贸易壁垒在升高，转口贸易的审查在收紧，怎么看都不是一个乐观的起点。\n\n但今年前四个月的实际数据，让所有人都需要重新校准预期。以美元计，出口同比增长了14.5%。这个数字放在任何年份都算得上强劲，更不用说是在一个充满政策不确定性的年份。\n\n不过，真正值得追问的不是“有多强”，而是“强在哪里”。如果把这14.5%的增长拆开来看，会发现一个与市场直觉截然不同的画面：出口的强势并非全面开花，而是高度集中在少数几个赛道上。这背后，是截然不同的驱动力，以及截然不同的可持续性。\n\n这份研报的核心判断是：市场可能正在误读本轮贸易反弹的性质。它不是国内需求复苏的映射，也不是中国制造竞争力的全面回归。它更像是一个由AI硬件周期和地缘政治驱动的能源安全焦虑共同制造的“窄脉冲”。这个脉冲的受益者非常集中，而它对GDP增长和就业的拉动，将远不如去年那种由出口量驱动的全面增长。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 58%的出口增量来自三个板块，但驱动力完全不同\n\n今年1-4月，出口增长的最大贡献者，既不是传统的纺织服装，也不是普通的机电产品，而是三个高度聚焦的领域：与AI相关的存储模组和芯片、以及被统称为“新三样”的电动汽车、光伏和锂电池。\n\n这三个板块加起来，贡献了全部出口增量的58%。其中，仅AI相关的存储模组和芯片，在4月份就占到了中国总出口的11.3%。这个数字令人印象深刻，但更重要的是理解其背后的驱动力。\n\n存储芯片和模组的出口暴涨，核心驱动力是价格，而非数量。以ADP模组为例，其美元计价的出口单价同比飙升了近200%。集成电路的出口价格也上涨了92.4%。换句话说，中国在这个领域的出口增长，主要是在“卖得更贵”，\n\n[... middle omitted ...]\n\n绕“如何从出口数据中提前识别下一轮产业趋势”做更深度的交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国出口数据炸了，但结构很“挑食”\n\n出口强在哪？\n\n今年前4个月出口同比+14.5%，远超年初预期。但仔细拆结构会发现，增长不是雨露均沾，而是高度集中在三个领域：\n\n1. 存储芯片和模组（AI相关）\n2. 集成电路（主要是成熟制程存储芯片）\n3. “新三样”：电动车、光伏、锂电池\n\n这三个板块贡献了总出口增量的58%。单是AI相关的存储模组和芯片，4月就占到总出口的12.4%。\n\n价格把量给“藏”了\n\n更关键的是，这波出口增长很大程度上是价格撑起来的，不是量。\n\n- 存储模组出口价格同比暴涨近200%\n- 存储芯片价格同比上涨92.4%\n- 价格对存储类出口增长的贡献率从去年的6%飙到4月的85%\n\n相比之下，“新三样”的价格虽然也在涨，但量的贡献更大。\n\n而除了这三个板块，其他产品的出口价格还在跌，出口量也只是温和增长。\n\n进口：AI供应链+囤货，不是内需\n\n进口端的情况也很说明问题。进口反弹主要靠两股力量：\n\n1. AI供应链需求：存储芯片进口价格4月同比暴涨359%，主要来自韩国\n2. 大宗商品囤货：地缘冲突加剧能源安全担忧，中国在持续增加原油、矿产等战略物资储备\n\n但剔除这些，其他品类进口增长非常疲\n\n[... middle omitted ...]\n\ntious view on China trade, expecting headwinds from rising trade barriers and stricter enforcement against transshipment. Setting aside the usual year-start seasonal distortions, the trade dat\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 22 May 2026 12:43 AM HKT\n\nDisseminated 22 May 2026 12:43 AM HKT"
  },
  {
    "id": "R003",
    "title": "日本股市真正的考验不是3%利率，而是谁能在利率上升中重新定价",
    "digest": "[wechat_article.md]\n# 日本股市真正的考验不是3%利率，而是谁能在利率上升中重新定价\n\n过去一周，日本长期利率的急速攀升引发了AI半导体板块的明显回调。10年期日本国债收益率一度突破2.8%，逼近3%这一被市场视为关键心理关口的位置。油价持续高企、政府补充预算传闻、以及消费者信心指标的快速恶化，共同构成了这场利率冲击的叙事背景。\n\n但这份来自某外资投行日本权益策略团队的最新报告，给出了一个与市场直觉相反的判断：日本股市在3%利率环境下仍能维持上升趋势，真正需要关注的不是利率本身，而是利率上升过程中不同板块的结构性分化。金融股相对受益，AI半导体不会因此终结，而地产、电力和航空则面临实质性压力。\n\n这个判断的核心逻辑建立在三个支柱之上：日元快速升值的风险已经消退、区域金融体系通过加速整合提升了韧性、以及外资和日本个人投资者仍有充足的买入空间。报告同时明确指出，3.0%-3.5%的利率水平仍然是日本区域金融体系的警戒线，这一判断从年初至今并未改变。\n\n以下是我们对这份报告的深度解析。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 利率上升的真正触发因素不是财政，而是结构性通胀预期\n\n市场普遍将上周利率急升归因于政府补充预算的传闻，但报告对此提出了重要修正。补充预算预计将基础收支/GDP比率压低约0.5个百分点，将基础收支盈余的实现时间从2026财年推迟至2027-28财年。单独来看，这个规模不足以触发日本资产的\"三重抛售\"（债券、日元、股票同时下跌）。\n\n真正值得关注的，是利率上升背后的结构性因素。报告指出，自2026年初以来，日本10年期盈亏平衡通胀率持续走高，进口价格指数在日元贬值的放大效应下重回上升通道。这意味着当前的利率上升并非单纯的财政恐慌，而是市场对日本通胀持续性的一次重新定价。\n\n从更宏观的视角看，日本政府设定的2030年\n\n[... middle omitted ...]\n\n者和机构投资者一起，继续深入讨论这些尚未完全回答的关键问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本利率3%时代来临，市场会怎么走？\n\n日本股市，利率破3%怎么看\n\nAI和金融股，谁更扛得住？\n\n最近日本长期利率快速攀升，10年期国债收益率一度突破2.8%，向3%迈进。很多人担心，这对股市是不是个坏消息？\n\n投行研报做了详细推演，核心结论是：日本股市在3%利率环境下依然可以维持上行趋势，不需要过度恐慌。\n\n1️⃣ 利率为什么突然涨了？\n- 高油价持续，日本作为石油进口国，通胀压力加大\n- 政府补充预算传闻引发市场对财政可持续性的担忧\n- 但研报认为，补充预算只是把财政平衡目标从2026财年推迟到2027-28年，不会引发“债市、日元、股市”三重抛售\n\n2️⃣ 为什么3%利率下股市还能涨？\n三个支撑因素：\n① 日元快速升值风险减弱，利率上升对盈利和股价的冲击不会被放大\n② 区域金融体系韧性增强，行业重组加速\n③ 外资仍有买入空间，日本个人投资者持有2200万亿日元资产，也在增加股票配置\n\n3️⃣ 哪些板块更受益？\n- 金融股：利率上升环境下有相对优势\n- AI半导体：虽然短期承压，但AI增长由全球供应链驱动，只要美国利率不快速飙升，AI行情不会结束\n- 注意：房地产、电力和燃气、航空运输受利率上升负面影响\n\n[... middle omitted ...]\n\ngger a triple sell-off in Japan. We argued in January that a 10-year JGB yield of 3.0–3.5% is a warning level for the regional financial system (report). We think this level remains largely un\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 21 May 2026 06:27 PM JST\n\nDisseminated 21 May 2026 06:34 PM JST"
  },
  {
    "id": "R004",
    "title": "人民币走强的逻辑，市场可能低估了供给侧的支撑力",
    "digest": "[wechat_article.md]\n# 人民币走强的逻辑，市场可能低估了供给侧的支撑力\n\n市场对人民币汇率的讨论，过去几个月几乎都集中在两个变量上：美元的强弱，以及中美关系的冷暖。这两个变量当然重要，但它们更像是“情绪开关”，而非“基本面引擎”。某外资投行最新发布的亚洲外汇策略报告，提出一个值得认真对待的判断：当前人民币的强势，根植于中国外部部门的结构性改善，包括持续的贸易顺差、企业结汇行为的韧性，以及地缘政治风险暴露度的不对称性。这些因素叠加在一起，意味着即使美元阶段性反弹，人民币的贬值空间也极为有限，而一旦外部环境改善，升值的弹性可能超出市场预期。\n\n这份报告的核心推荐是做空美元/离岸人民币，目标价6.60，时间窗口是2026年8月底。推荐信心评级为3/5。这个评级本身就是一个信号——它不是那种“确定性极高”的交易，而是“逻辑清晰、但需要催化剂配合”的布局。真正值得关注的，不是这个交易本身，而是支撑这个交易的底层逻辑：中国的外部资产负债表，正在经历一轮市场尚未充分定价的再平衡。\n\n以下是我们从这份报告中提炼出的五个关键洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 美元走强时人民币抗跌，美元走弱时人民币弹性更高，这种不对称性正在被市场验证\n\n报告给出了一个非常具体的数据：自2026年2月28日伊朗局势升级至5月21日，美元指数上涨了1.7%，而美元/离岸人民币反而下跌了0.9%。这意味着人民币在这一时期对美元实现了相对强势。更关键的是，报告量化了美元/离岸人民币对美元指数变动的敏感度：当美元指数上行时，离岸人民币的敏感度只有约28%；但当美元指数下行时，敏感度跃升至约62%。\n\n这里有一个重要的含义。市场通常会把人民币视为“美元弱则涨、美元强则跌”的对称资产。但数据表明，人民币在美元走强时表现出显著的抗跌性，而在美元走弱时则能更充分地释放\n\n[... middle omitted ...]\n\n况下可能转向？这些问题的答案，可能决定了当前交易的真正赔率。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n人民币正在悄悄变强，这几个信号值得关注\n\n人民币走强进行时\n\n五个信号告诉你，人民币为什么可能比想象中更坚挺\n\n最近人民币的走势其实挺有意思的。你可能没注意到，在中东局势紧张、美元整体走强的背景下，人民币反而表现得相当抗跌，甚至还小幅升值了。这背后有几个逻辑值得拆开来看看。\n\n1️⃣ 人民币对美元的反应不太对称\n\n这段时间美元指数涨了1.7%，但人民币对美元不仅没跌，反而还涨了0.9%。一个有意思的细节是：当美元上涨时，人民币的敏感度只有28%左右；但当美元下跌时，人民币的敏感度会飙升到62%。换句话说，人民币在美元走强时抗跌，在美元走弱时会加速走强。这种不对称性本身就是一种强势信号。\n\n2️⃣ 企业结汇意愿依然强劲\n\n4月份最新的外汇结算数据显示，净结汇盈余达到477亿美元，相当于调整后贸易顺差的82%。虽然出口企业结汇比例从一季度的55.8%小幅回落到50.1%，但绝对值依然很高。出口持续强劲（一季度净贸易顺差2470亿美元）加上市场对人民币升值的预期，企业手里的美元更愿意换成人民币，这为汇率提供了实打实的支撑。\n\n3️⃣ 中美关系出现阶段性缓和\n\n前阵子的中美领导人会晤后，气氛明显改善。中国商务部确认了\n\n[... middle omitted ...]\n\nd amid the ongoing US-Iran stalemate. While we see a risk of the stronger USD backdrop temporarily slowing the downtrend in USD/CNH, it remains clear that the upside in USD/CNH remains limited\n\n[... middle omitted ...]\n\nrmation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R005",
    "title": "人民币中间价模型正在发出一个被市场低估的信号",
    "digest": "[wechat_article.md]\n# 人民币中间价模型正在发出一个被市场低估的信号\n\n当市场多数参与者还在争论中美利差、关税周期或资本流动方向时，一份来自某外资投行的最新USD/CNY定盘价模型，揭示了一个更直接、更短期的定价逻辑。这份报告的核心判断是：模型预测的中间价较前一日下降了370个基点，即便计入逆周期因子，降幅也达到211个基点。这不仅仅是数字的变动，而是对当前政策意图的一次量化解读。\n\n为什么这个信号值得关注？因为中间价是人民币汇率定价的“锚”，而模型预测的偏离幅度，往往比实际定盘价更能反映政策层的容忍边界。当模型预测与实际定盘之间的误差持续扩大时，通常意味着市场定价与政策意图之间正在积累张力。这份报告恰好提供了这种张力的最新读数。\n\n报告提供的核心新信号在于：它不仅仅给出了一个预测值，还拆解了不同货币对定盘价的贡献权重，以及模型误差的历史轨迹。这些数据合在一起，指向一个结论——当前人民币中间价的设定逻辑，正在从被动跟随市场转向主动管理预期。理解这一转变，对任何持有人民币资产或参与跨境交易的决策者而言，都不是可有可无的背景知识。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 模型预测的370个基点降幅，本质是“一篮子压力”的集中释放\n\n这份模型的核心机制并不复杂：它通过追踪一篮子货币的隔夜变动，来预测第二天的人民币中间价。报告显示，模型预测值为6.7979，较前一日6.8349下降了370个基点。这个降幅本身已经足够显著，但更有价值的是其构成。\n\n报告拆解了前四大贡献货币：俄罗斯卢布贡献了18个基点，欧元贡献了11个基点，韩元贡献了3.5个基点，而澳元则拖累了8个基点。这组数据揭示了两个关键事实。第一，人民币中间价的定价并非单纯盯住美元，而是对一篮子货币的综合反应。第二，在当前的全球宏观环境下，非美货币的波动正在通过这个传导机制，对人\n\n[... middle omitted ...]\n\n这个模型信号的变化，并在关键事件节点前提供更具体的应对思路。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n人民币中间价模型给出新信号\n\n6.79 vs 6.83\n\n关键点位差370个基点\n\n最近看了一份外资投行的研报，讲的是人民币对美元中间价的测算模型，信息量挺大，拆开来分享给大家👇\n\n**1/ 模型算出的新点位**\n模型预测的中间价是6.7979，比上一次的6.8349低了370个基点。如果加入逆周期因子，预测值是6.8138，比上次低211个基点。简单说，模型认为中间价有调低的倾向。\n\n**2/ 主要贡献来自哪些货币**\n模型里影响最大的四个货币对：俄罗斯卢布贡献了18个基点（正面），欧元贡献了11个基点，韩元贡献了3.5个基点，澳元则是-8个基点（拖后腿）。可以看出卢布和欧元是主要推手。\n\n**3/ 模型误差在缩小**\n研报里还展示了模型误差的历史走势。2025年初误差很大（-1800个基点），之后快速收窄。到2025年下半年，误差基本在0附近波动，2026年误差稳定在600个基点左右。这说明模型准确性在提升。\n\n**4/ 下半年重要事件值得关注**\n研报列出几个关键节点：7月底的政治局会议（定调经济工作）、10月国庆黄金周、11月在深圳举办的APEC会议、12月中旬的中央经济工作会议，以及年底可能的中美领\n\n[... middle omitted ...]\n\n (without counter-cyclical factor)   \n![](images/3bb972466a48e1f8ed9e16286bd39977a5c542d4404aa71535b0376cdecf9a28.jpg)\n\n<details>\n<summary>bar</summary>\n\n| Currency Pair | Top 4 weighted contr\n\n[... middle omitted ...]\n\nrmation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R006",
    "title": "会计标准也能让人“爱上”？IFRS 18的真正影响，市场还远未定价",
    "digest": "[wechat_article.md]\n# 会计标准也能让人“爱上”？IFRS 18的真正影响，市场还远未定价\n\n一份来自某外资投行能源团队的研报，开篇提出了一个看似荒诞的问题：一家公司，能否像爱上一个人一样，爱上一项会计标准？\n\n答案也许是“能”。2018年，Technip Energies就“爱上”了IFRS 15。而2027年1月，当新标准IFRS 18生效时，市场可能将再次目睹类似的“爱恋”——但这一次，谁是受益者，谁又是被蒙蔽者，远没有表面那么简单。\n\n这并非会计学家的自娱自乐。对于产业决策者和高净值投资者而言，会计准则的迭代从来不只是财务部门的合规工作。它直接重塑了利润表的呈现逻辑、现金流的口径、以及管理层与市场之间信息博弈的规则。看懂IFRS 18，就是看懂2027年之后，哪些公司的“底牌”将被翻出，哪些公司的“面具”将被摘下。\n\n这份报告的核心判断是：**IFRS 18的真正价值，不在于它改变了什么数字，而在于它强制改变了“谁先看到数字”的权力结构。** 市场目前对它的讨论，大多停留在合规层面，而低估了其对行业竞争格局和资产定价的深远影响。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 新标准的“甜点”：强制间接法现金流表，将终结信息不对称\n\nIFRS 18最令人兴奋的变化，绝非那些复杂的五类科目和五个小计，而是它对现金流量表的强制要求：**所有企业必须使用间接法编制现金流量表，并且必须从营业利润（Operating Profit）开始。**\n\n这听起来像是技术细节，但其影响是颠覆性的。\n\n在现行IAS 7下，企业可以选择从净利润开始编制间接法现金流表。这意味着，管理层可以将非现金项目、投资收益、甚至一次性损益全部混杂其中，使得从净利润到经营现金流的“调节过程”变得极其不透明。投资者看到的，往往是一个被精心“化妆”后的现金流数字。\n\n而\n\n[... middle omitted ...]\n\n，我们将基于这份报告，进一步拆解其背后的投资逻辑与交易信号。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n投研人最该学的：IFRS 18新规全拆解\n\n📖 会计新规，读懂它\n\n2027年1月，IFRS 18要来了。\n这不是会计圈的自嗨，是每个看报表的人都该提前搞明白的变化。\n\n投行研报把这件事讲得特别通透，我帮你翻译成人话。\n\n**1️⃣ 最大的亮点：现金流表终于“对味”了**\n\n以前公司做现金流表，可以从净利润开始编。\n新规强制要求：必须从营业利润/EBITDA开始编。\n\n这意味着什么？\n- 投资者终于能看清：钱到底是怎么赚出来的\n- 公司以前不喜欢这个做法，因为太透明了\n- 对分析师来说，这是个“大礼包”\n\n另外，利息收支、股息收支的归类也统一了：\n- 利息支付 → 融资活动\n- 利息收入 → 投资活动\n- 股息收入 → 投资活动\n- 股息支付 → 融资活动\n\n再也不用猜来猜去了。\n\n**2️⃣ 利润表：5个类别 + 5个小计**\n\n三个新类别：\n- 营业\n- 投资\n- 融资\n\n两个老类别：\n- 所得税\n- 终止经营\n\n五个必报小计：\n- 营业利润\n- 融资和税前利润\n- 净利润\n- 其他综合收益合计\n- 综合收益合计\n\n还可以自己加两个：\n- 毛利润\n- OPDAI（其实就是EBITDA的替身）\n\n**3️⃣\n\n[... middle omitted ...]\n\nis is foolish. While ‘super financiers’ may not always be ‘super accountants’, ‘super-accountants’ can often be ‘super financiers’.\n\n'Super accountants' are like sommeliers, musicians, polyglo\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R007",
    "title": "中国半导体设备市场正在经历的不是周期，而是供给侧的重新定价",
    "digest": "[wechat_article.md]\n# 中国半导体设备市场正在经历的不是周期，而是供给侧的重新定价\n\n过去几个月，市场对中国半导体设备板块的关注点主要集中在两个问题上：美国出口管制升级会带来多大冲击？以及，国内设备厂商的订单增长是否已经见顶？某外资投行最新发布的深度研报给出了一个与市场共识不同的判断——中国WFE（晶圆制造设备）市场正在进入一个由AI和存储器超级周期共同驱动的结构性增长阶段，而市场真正低估的，不是需求本身，而是中国本土设备商在供给端替代的速度和持续性。\n\n这份研报的核心修正在于：将2026至2028年中国WFE市场规模预测分别上调至580亿、670亿和770亿美元，较此前预测累计上调超过260亿美元。上调的主要驱动力来自存储器领域的资本开支加速，而非此前市场预期的逻辑芯片扩产。这一调整背后，是两个正在发生但尚未被充分定价的结构性变化。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 存储器扩产正在成为中国WFE增长的新引擎，其速度和规模超出多数投资者预期\n\n过去两年，中国WFE市场的增长主要由逻辑芯片领域的国产替代驱动。但根据该投行最新的渠道调研，中国存储器IDM厂商——主要是长鑫存储（CXMT）和长江存储（YMTC）——正在显著加快未来几年的产能扩张计划。具体而言，报告预计两家公司将在2026年各新增一座晶圆厂，2027年再各新增两座，2028年还有更多扩产计划。\n\n这一判断的支撑逻辑值得仔细拆解。首先，AI驱动的存储器超级周期正在造成DRAM和NAND的供应短缺，这使得下游客户更愿意接受国产存储器芯片，尤其是在技术追赶较晚的DRAM领域。其次，两家存储器厂商的盈利能力改善，预计将在2026年各自产生数百亿人民币的经营现金流，叠加IPO募资，它们拥有充足的资本来支撑大规模扩产。第三，一个被市场低估的运营效率差异：中国存储器厂商从洁净\n\n[... middle omitted ...]\n\n里分享原始研报的PDF版本，并定期组织对关键假设的跟踪复盘。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国芯片设备：存储扩产正在加速\n\n存储扩产，远超预期\n\n最近看了一份某外资投行关于中国半导体设备的深度研报，信息量很大。核心观点是：中国存储芯片（DRAM/NAND）的产能扩张正在显著加速，带动整个设备市场预期大幅上调。\n\n研报主要讲了这几个关键变化：\n\n**1/ 存储扩产是最大变量**\n\n- 2026-2028年中国WFE（晶圆制造设备）支出预计为580/670/770亿美元，大幅高于之前预测的550/590/610亿\n- 主要上调来自存储领域：长鑫存储（CXMT）和长江存储（YMTC）计划2026年各新增1座晶圆厂，2027年再各增2座\n- 原因：AI带来的存储超级周期导致DRAM/NAND供应紧张，加上这两家公司盈利能力改善，有充足资金支持扩产\n- 中国存储厂建洁净室只需1年（全球同行需2-3年），扩产速度更快\n\n**2/ AI可能给先进逻辑带来额外惊喜**\n\n- 研报暂时维持逻辑芯片资本支出持平判断，但认为存在上行风险\n- 随着英伟达被中美双方限制对华出口，国内先进逻辑扩产可能进一步加速\n- AI相关周边芯片需求也在推动成熟逻辑产能扩张\n- 中国需要自研HBM和eSSD来支撑本土AI数据中心，这会进一\n\n[... middle omitted ...]\n\npg)\n\nZheng Cui\n\n+852 2123 2694\n\nzheng.cui@bernsteinsg.com\n\n![](images/c034b3d62bc70850453fd760de4d31484684b3228772bea5561f2d465f185865.jpg)\n\nFrancis Ma\n\n+852 2123 2626\n\nfrancis.ma@bernsteinsg.\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R008",
    "title": "美国变压器缺口收窄的速度，比市场想象的要慢",
    "digest": "[wechat_article.md]\n# 美国变压器缺口收窄的速度，比市场想象的要慢\n\n全球电力设备市场正在经历一轮罕见的供需错配。当大多数投资者还在讨论“AI数据中心驱动需求”这一老生常谈的叙事时，一份来自某外资投行的最新出口追踪数据揭示了一个更微妙的信号：中国变压器出口增速在4月明显放缓，但开关柜出口却突然加速至77%的同比增长。这组看似矛盾的数据背后，隐藏着全球电网设备供应链正在发生的结构性重塑——美国本土产能扩张的速度，远不足以填补其巨大的供需缺口。\n\n这份报告的核心判断是：美国电力变压器市场“需求-本地供给”的缺口，将从当前的72%逐步收窄至2028年的60%。这个数字意味着什么？即使考虑到所有已宣布的本地扩产计划，到2028年，美国市场仍有六成的变压器需求需要依赖进口。全球供应链的紧张状态，远未到可以松懈的时刻。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 中国出口增速放缓不是需求见顶，而是结构性换挡\n\n4月中国变压器总出口额同比增长27%，较3月的56%明显回落。单看这个数字，很容易得出“需求降温”的结论。但深入拆解就会发现，这更像是出口结构的主动调整，而非需求的系统性下滑。\n\n真正值得关注的是区域分化：非洲市场出口暴增681%，贡献了总出口的23%；北美市场增长66%，贡献了19%；亚洲市场增长38%，贡献了30%。而欧洲仅增长9%，中东和拉美则分别下滑26%和63%。这种剧烈的区域分化，说明中国变压器出口正在从“全面铺开”转向“重点突破”——资源正在向需求最紧迫、支付能力最强的市场集中。\n\n对投资者而言，这意味着不能再用“中国变压器出口总量”这个单一指标来判断景气度。需要关注的是：哪些市场在持续增长，哪些市场的增长是由一次性项目驱动，以及不同市场的定价能力差异。非洲681%的增长背后，是基数效应还是长期趋势，这里仍需验证。\n\n![\n\n[... middle omitted ...]\n\n信群里继续交流。我们会在群内分享更完整的解读笔记和讨论纪要。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美国变压器缺口，可能比你想的久\n\n🔍 供需缺口仍在\n\n**全球变压器供需，4月更新**\n\n刚刷到某外资投行的最新变压器出口追踪报告，信息量很大，帮大家拆解一下关键点👇\n\n**1/ 出口增速放缓，但绝对值不弱**\n- 4月中国变压器（>10MVA）出口总值同比+27%，相比3月的+56%有所回落\n- 但开关设备出口加速到+77%（3月仅+5%），说明下游需求其实很强\n\n**2/ 美国市场：缺口短期难补**\n- 4月对美变压器出口同比+95%（3月+118%）\n- 研报估算：美国电力变压器供需缺口将从目前的72%，到2028年收窄至60%\n- 即便本土扩产计划落地，短缺仍会持续，给中国供应商留了空间\n\n**3/ 价格信号分化**\n- 美国变压器PPI高位稳定，但220-330MVA段的中国出口价4月环比降了14%\n- 不过近3个月滚动均价仍同比+23%\n- 原材料方面：取向硅钢价格小幅回落，铜价在去年四季度冲高后3月回调\n\n**4/ 机构关注方向**\n- 思源电气：变压器出口+开关设备双受益\n- 国电南瑞：国内电网投资+换流阀出口潜力\n- 华明装备：变压器组件出口，但增长已反映在股价中\n\n**一点思考**：全球电\n\n[... middle omitted ...]\n\nApril, from $5\\%$ in March (indicating underlying demand strength combined with stronger PPI print for switchgear in the US at $14\\%$ yoy). In particular, transformer exports to the US deliver\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R009",
    "title": "股份制银行的分化时刻：利润增速从1%到高单位数意味着什么",
    "digest": "[wechat_article.md]\n# 股份制银行的分化时刻：利润增速从1%到高单位数意味着什么\n\n当市场还在争论银行净息差是否已经见底时，一份来自近期外资投行金融调研的研报揭示了一个更值得关注的信号：股份制银行正在经历一场根本性的业绩分化，而这种分化并非简单的“好银行”与“坏银行”的二分法，而是关于资产质量出清节奏、零售风险暴露阶段以及管理层战略执行力的三重检验。\n\n这份研报的核心判断是：2026年将成为股份制银行利润增速差距拉大的一年。以某股份制银行为代表的银行已经敢于给出高单位数的利润增长指引，而另一家银行却坦承仍处于零售资产质量恶化的早期识别阶段。两者之间的差距，不是季度波动，而是结构性拐点的时差。\n\n对于投资者和产业决策者而言，理解这种分化的底层逻辑，远比判断行业整体趋势更重要。因为当行业整体增速放缓时，个股的选择就变成了对管理层判断力和风险定价能力的赌注。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 利润增速的裂口：从1%到高单位数的背后是资产质量出清节奏的差异\n\n2026年一季度，某股份制银行（以下称A银行）的利润增速仅为1%，但管理层给出的全年指引却是高单位数增长。表面上看，这是一个保守开局与乐观全年的矛盾组合。但研报揭示了一个关键细节：A银行在2025年一季度贡献了全年利润的35%，而2026年正在主动降低一季度利润占比，试图让利润分布更加均匀。\n\n这种主动调节行为本身就是一个信号：管理层对全年利润增长有足够的信心，以至于愿意牺牲一季度的报表表现。信心来源是什么？研报提到，该银行的不良贷款生成率将同比下降，信用成本处于改善趋势，且其不良贷款覆盖率在2026年一季度已超过200%。资产质量“处于过去10年最好的水平”——这是管理层自己的判断。\n\n与之形成鲜明对比的是另一家股份制银行（以下称B银行）。该银行管理层坦言“没有信心判断零\n\n[... middle omitted ...]\n\n据和更完整的分析框架，一起探讨股份制银行的投资逻辑和风险点。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n银行股走到哪了？四家股份行内部逻辑分化\n\n股份行 分化加剧\n\n某外资投行刚开完中国峰会+银行调研，和四家股份行管理层深聊后，发现内部格局相当分化。\n\n**1/ 贷款需求：零售凉，对公热**\n- 4月信贷收缩部分源于季节性，央行没给硬指标，只说要平滑节奏\n- 零售需求普遍疲软，房贷问题不在公积金，而可能是首付比例在上升（现金支付增多）\n- 中信对公贷款强劲，1Q26新增约2300亿，聚焦大湾区+长三角\n- 浦发2026年目标新增约3000亿（vs 2025年约3200亿），增速从5.8%放缓至5.3%\n- 民生1Q26对公超预期，但4月回落，5月仍弱；零售贷款从2025年中开始全线收缩\n- 平安1Q26零售贷款正增长（行业少数），但全年只有低个位数增速，结构“对公为主、零售为辅”\n\n**2/ 净息差：普遍看到企稳信号**\n- 中信预计全年息差收窄3-5bps（vs 2025年收窄13bps），后续季度环比持平\n- 浦发1Q26净息差环比改善2bps至1.44%，目标全年同比稳定或微升\n- 民生预计2026年净息差同比反弹（即使考虑一次对称降息）\n- 平安预计全年仅低个位数bps收窄，重点做结构优化（多放贷款、少\n\n[... middle omitted ...]\n\nry, stable fee income growth, and a continuing drag from retail asset quality. At the individual bank level, however, our views are mixed. We turn more positive on SPDB (OW): the bank guided f\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R010",
    "title": "铝的供给侧拐点被低估，这才是大宗商品当前最被忽视的结构性机会",
    "digest": "[wechat_article.md]\n# 铝的供给侧拐点被低估，这才是大宗商品当前最被忽视的结构性机会\n\n市场正在关注中国资产的整体重估，但一个更具体、更迫切的信号正在被宏观叙事淹没：铝的供需格局正在发生根本性转变，而大多数投资者仍将其视为周期波动。某外资投行在中国峰会第二日的交流中，从中国宏桥等核心企业获得的信息指向一个清晰的判断——铝价的上行并非短期情绪驱动，而是供给侧结构性收紧的必然结果。与此同时，铜钴市场的成本压力正在从“会不会短缺”转向“愿意付多高的溢价”，而印尼的反复政策扰动则让资源国风险重新成为定价因子。\n\n这份报告的真正价值不在于罗列数据，而在于它揭示了三个相互独立但又共同指向“资源定价权正在从需求端向供给端转移”的底层逻辑。以下是我们提炼的核心洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 铝的供需错配远比市场认知的更深，印尼产能释放的时间差是关键变量\n\n市场对铝价的担忧主要集中在两点：一是中国45Mt产能天花板是否会被突破，二是印尼大规模新建产能是否会在短期内冲击全球供应。中国宏桥在峰会上的回应直接而有力——他们用自己耗时2.5年才在印尼建成1Mt氧化铝精炼厂的经验，质疑市场对“2年内投产2Mt电解铝”的乐观预期。电力配套的瓶颈不是靠规划文件能解决的。\n\n更关键的是，LME库存已降至300kt的临界水平，其中约200kt为俄罗斯货源。中国出口月均550kt的规模，意味着国内库存的消耗速度将在1-2个月内对全球市场产生实质性影响。宏桥的判断是，铝价在未来12-18个月将维持高位甚至进一步上行，且目前尚未看到来自客户的需求破坏。\n\n这意味着什么？市场当前对铝价的定价仍然隐含了“供应会很快跟上”的假设。但这个假设在缺乏电力基础设施和建设周期的约束下，很可能被证伪。对于持有铝相关资产的投资者而言，供给侧的确定性比需求侧的预测更有价值\n\n[... middle omitted ...]\n\n踪这些关键变量的变化，而不是等到市场已经定价完毕才后知后觉。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国峰会第二天，矿业在聊什么\n\n投研笔记\n\n拆解铝、刚果金与印尼的新变量\n\n---\n\n**1. 刚果金：没有硫磺和柴油短缺，但成本在涨**\n\nCMOC 的会议信息量很大。最核心的一点：刚果金并没有出现市场担心的硫酸短缺。区域内大部分矿企都有自己的酸厂，库存足够覆盖到三季度。柴油也一样，只要愿意付高价就不存在真短缺。\n\n但这两项成本都在涨——硫酸占现金成本的比例从 10% 涨到了 20%，柴油从低个位数涨到了高个位数。成本压力是实打实的。\n\n另一个焦点是刚果金的地缘风险。2027 年起，LME 铜价超过 11500 美元的部分要征收 50% 暴利税，本地员工持股也有小幅稀释，钴配额已经落地。投资者还在担心刚果金近期转向亲美政策，可能限制后续扩产。\n\n公司层面，2026 年 79 万吨铜产量指引不变，2028 年目标 80-100 万吨。钴价目前没有看到客户端的需求破坏，钨矿出口限制下依然稳定生产。铜和金被明确列为并购战略的两大支柱。\n\n**2. 铝：中国宏桥很乐观，LME 库存快见底了**\n\n这次会议上最 bullish 的可能是铝。宏桥认为铝价还会继续走高，并保持高位 12-18 个月。\n\n逻辑很清晰：LME\n\n[... middle omitted ...]\n\nor higher rates & inflation much quicker (like they did when Powell turned Dovish last July). A large camp, however, was MUCH more constructive, arguing multiples are now very reasonable for s\n\n[... middle omitted ...]\n\nww.JPM.com/disclosures.\n\nAnmol Mehta - Specialist Sales - APAC Energy & Mining AC\n\nAsia Pacific Specialist Sales 22 May 2026\n\nanmol.mehta@JPM.com\n\nCompleted 22 May 2026 08:34 AM HKT\n\nDisseminated 22 May 2026 08:34 AM HKT"
  },
  {
    "id": "R011",
    "title": "储能与新能源车的真正分水岭：成本通胀正在重新定义赢家",
    "digest": "[wechat_article.md]\n# 储能与新能源车的真正分水岭：成本通胀正在重新定义赢家\n\n中国市场的beta依然低迷，但结构性机会从未如此清晰。这是某外资投行在中国投资峰会第二天结束后，传递给产业决策者的核心信号。\n\n投资者对中国市场的态度可以用一句话概括：审慎但挑剔。国内需求疲软、房地产问题悬而未决，这些宏观因素压制了整体市场的弹性。但在AI、科技和供应链龙头领域，尽管估值和拥挤度引发担忧，共识依然稳固。而在工业板块，投资者正在将筹码集中在那些具备全球竞争力、出口导向和规模优势的玩家身上——机械、机器人和电池，被视为中国制造优势的关键受益者。\n\n汽车板块的看法则更加分化。国内需求疲软是共识，但强劲的海外需求和国内竞争格局的边际缓和——零跑汽车在峰会上明确表示国内竞争压力正在缓解——正在为市场提供一些支撑。\n\n但储能和电池领域，才是本次峰会最值得深挖的信号。长期结构性需求已被广泛认可——AI算力驱动和能源转型是两大引擎。然而，投资者对中期风险的警觉正在上升。未来12个月内激进的产能扩张、锂价上涨带来的利润率压力，正在让市场重新聚焦于那些真正的龙头。\n\n**市场真正低估的不是需求，而是成本通胀对竞争格局的重新洗牌。**\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 储能需求增速放缓的信号被误读：关键在于成本弹性而非需求总量\n\n全球储能出货量在2026年前四个月同比增长109%，这是一个令人瞩目的数字。但投资者开始质疑：这样的增速能持续吗？\n\n国轩高科在峰会上给出了一个关键数据：公司预计2026年全年行业需求增速将超过60%。这确实低于前四个月的109%，但问题不在于增速放缓本身——任何高基数行业都会经历增速的正常化。真正值得关注的是，国轩高科同时强调，国内储能需求虽然结构性强劲，但项目经济性的纪律正在加强。\n\n这意味着什么？需求总量不\n\n[... middle omitted ...]\n\n会纪要和更多一手数据，持续追踪这些关键变量的变化。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n储能与新能源车：热度不减，谨慎前行\n\n**储能市场，冷热交织**\n\n某外资投行峰会第二天的反馈，信息量不小。\n\n投资者对中国市场整体偏谨慎，但AI、科技和供应链龙头依然是焦点。工业领域情绪相对积极，尤其看好有全球竞争力的出口导向型玩家，比如机械、机器人和电池。\n\n储能（ESS）的逻辑很清晰：AI用电和能源转型驱动长期结构性需求。但短期风险也在浮现——未来12个月产能扩张太猛，加上锂价上涨带来的成本压力，让投资者开始警惕“中期周期风险”。\n\n1️⃣ **需求强劲但增速放缓**\n全球储能出货量前4个月同比+109%，但某头部企业预测全年行业需求增速可能降到60%以上。这意味着下半年可能明显减速，投资者开始担心需求能否支撑当前产能规划。\n\n2️⃣ **成本压力传导**\n锂价上涨让原材料成本占到电池成本的约50%，对国内储能项目利润率的冲击最敏感。企业应对策略是出海+新产品路线——钠离子电池和固态电池成为技术储备的重点方向。\n\n3️⃣ **龙头更受青睐**\n这种环境下，规模优势和成本控制能力突出的企业（如CATL）反而更受关注。市场份额集中度可能进一步提升。\n\n**新能源车：出海是最大变量**\n\n乘用车板块的讨论更分\n\n[... middle omitted ...]\n\ns—seen as key beneficiaries of China’s manufacturing edge. In autos, views are more mixed due to weak domestic demand, while strong overseas demand and a slightly easing competition landscape \n\n[... middle omitted ...]\n\nww.JPM.com/disclosures.\n\nJoann Kim - Specialist Sales - APAC Industrials & Autos AC\n\nAsia Pacific Specialist Sales 22 May 2026\n\njoann.kim@JPM.com\n\nCompleted 22 May 2026 07:31 AM HKT\n\nDisseminated 22 May 2026 07:31 AM HKT"
  },
  {
    "id": "R012",
    "title": "市场真正低估的不是油价，而是供给纪律的持续性",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是油价，而是供给纪律的持续性\n\n这份来自某外资投行的北美能源研报，在5月下旬更新了覆盖公司的盈利预测和估值敏感性。表面看，它只是在1Q业绩和最新油价曲线基础上做了一次常规调整。但仔细读下来，真正值得关注的不是油价本身涨了多少，而是整个供给端正在发生一个被低估的结构性变化：即便油价上涨，美国页岩油生产商依然选择维持资本纪律，而不是像过去那样加速增产。\n\n这个信号，比油价数字重要得多。\n\n报告覆盖的美国石油E&P公司，2026年产量指引平均仅上调0.6%，资本开支几乎不变。在WTI已经站上88美元的背景下，这种克制不是偶然的。它是过去几年行业反复教训后形成的集体理性，也是当前能源股估值折价的根本原因——市场在用70美元的长期油价给这些公司定价，而不是用88美元的现货。\n\n这种折价，既是风险，也是机会。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 产量只增长0.6%，资本开支纹丝不动，这才是最硬的供给纪律\n\n报告最核心的数据点，藏在产量和资本开支的修订表格里。\n\n覆盖的美国石油E&P公司，2026年产量指引平均上调0.6%。这个数字本身并不惊人，但结合油价背景看，就非常说明问题：1Q业绩发布以来，WTI现货价格已经从年初的70美元区间攀升至接近90美元，而几乎所有运营商都表示2026年活动计划不变。只有FANG、COP和PR少数几家公司做了调整，而且幅度非常有限。\n\n与此同时，资本开支估算几乎没有任何变化。报告中的Exhibit 8显示，绝大多数公司的2026年capex修订幅度在正负1%以内，中位数接近零。这意味着，油价上涨带来的额外现金流，并没有被重新投入钻探活动，而是流向了股东回报。\n\n这就是过去两年市场一直在期待的“资本纪律”，现在它变成了现实。而且，它不是靠管理层口头承诺维持的，而是被1\n\n[... middle omitted ...]\n\n可以一起拆解这些未解问题，并分享完整的原始图表和敏感性分析。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n石油公司2026年：产量微增，现金流转好\n\n能源股的逻辑，其实没那么复杂\n\n最近某外资投行更新了北美能源板块的模型，核心信息很清晰：产量微增、资本纪律依然严格、油价预期上调后自由现金流明显改善。\n\n1️⃣ 产量小幅增长，资本支出基本不动\n- 2026年石油产量平均上调0.6%，主要来自效率提升而非增加投资\n- 大多数公司维持原有资本支出计划，说明行业仍在克制\n- 美国页岩油全年净增量约4万桶/天（含大型油企约18万桶/天）\n\n2️⃣ 现金流回报亮眼\n- 按最新油价曲线（WTI约88美元），油企2026年自由现金流收益率中位数达15%\n- 天然气公司约9%（亨利港约3.67美元）\n- 油价每变动10美元，自由现金流收益率变动约2个百分点\n\n3️⃣ 估值隐含的长期油价\n- 当前股价隐含的长期WTI油价约70美元，比12个月远期低约16%\n- 天然气股隐含约3.50美元/百万英热，基本接近远期曲线\n\n4️⃣ 地缘因素怎么看？\n- 尽管近期油价高位，行业股价月内反而下跌约3%\n- 即便达成和平协议，恢复产量和补充库存仍需时间，油价可能维持高位\n- 建议在局势缓和带来的回调中，关注大型油企和高质量独立油企\n\n5️⃣ 哪\n\n[... middle omitted ...]\n\n consensus). Guidance implies \\~40 kb/d exit-exit US shale growth for E&Ps (\\~180 kb/d incl. majors).   \nWe estimate a median 2026 FCF yield of 15% for our oil E&P coverage at latest strip (fu\n\n[... middle omitted ...]\n\nor Energy Inc (SU.TO)</td><td>E (12/16/2024)</td><td>C$93.30</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.   \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R013",
    "title": "市场真正低估的不是需求，而是供给侧的再定价",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是需求，而是供给侧的再定价\n\n过去几周，中国钢铁市场出现了一个看似矛盾的信号：钢材表观消费量环比回落，但钢厂产量却在增加，库存从贸易商向钢厂端转移。如果你只看需求侧，很容易得出“行业仍在探底”的结论。但某外资投行最新一期周报揭示了一个更值得关注的叙事：市场正在经历的，不是需求的二次探底，而是供给侧的再定价。\n\n这份报告的核心判断并不复杂，但它的含义远比表面数字深远。当长材表观消费环比下降3.8%、扁平材下降3.1%的同时，长材产量却环比增长了7.5%，电炉开工率也小幅回升。这不是供需失衡的简单重复，而是行业结构正在发生一次静默的重组。理解这个重组，比争论需求何时见底更重要。\n\n为什么现在要关注这件事？因为过去三年，中国钢铁行业的每一次价格波动都被归结为“需求不行”。但这一次，需求侧的变化已经不再是唯一的解释变量。供给侧的调整方式、库存的分布结构、以及不同工艺路线的成本曲线，正在共同塑造一个新的定价框架。这个框架一旦确立，将直接影响未来12-18个月钢铁股的估值逻辑。\n\n报告中最值得注意的信号，不是需求的下滑幅度，而是供给端正在发生的几件“小事”：电炉利用率在上升、钢厂库存开始累积、而贸易商库存却在下降。这三件事放在一起，指向一个被多数人忽略的结论——行业正在从“被动去库存”转向“主动补库存”的前夜。但这个过程并不平坦，它伴随着利润的重新分配和竞争格局的洗牌。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 产量与消费背离的背后，是钢厂正在主动调整产品结构\n\n本周数据中最引人注目的矛盾在于：长材表观消费环比下降3.8%，但长材产量却环比增长7.5%。这不是统计口径的误差，而是钢厂正在主动调整产品结构的明确信号。\n\n报告显示，长材的库存周转正在加速，但方向是从贸易商向钢厂转移。贸易商库存环比下降2.\n\n[... middle omitted ...]\n\n键变量做周度跟踪，并在关键拐点出现时第一时间分享我们的判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n钢材市场周报：供需错配，库存悄然转移\n\n供需两端，谁在悄悄变化？\n\n最近看了某外资投行关于中国钢铁和铁矿石市场的周度更新，数据挺有意思，简单拆解一下逻辑。\n\n**1. 需求端：长材和板材都在降温**\n本周的表观消费量，长材环比下降3.8%，板材环比下降3.1%。同比来看，长材比去年低了6%，板材也微降0.6%。整体需求端呈现季节性偏弱的状态，没有看到明显的超预期提振。\n\n**2. 供给端：长材产量主动增加，板材基本持平**\n有意思的是，在需求收缩的背景下，长材产量环比增长了7.5%，板材产量微增0.1%。钢厂整体的产能利用率小幅提升0.2个百分点至89.7%，其中电炉的开工率环比提升0.8个百分点至60.8%。供给端没有随需求同步收缩，反而在主动加量。\n\n**3. 库存结构：贸易商在去库，钢厂在累库**\n从库存数据看，贸易商库存环比下降2.7%，但钢厂库存环比增加3.0%。这反映出下游拿货意愿一般，库存压力从贸易商向钢厂转移。同时，钢厂端的铁矿石库存也在小幅攀升（环比+2.6%），港口库存基本持平，说明钢厂采购节奏尚可，但原料囤积意愿不强。\n\n**4. 铁矿石供给侧：发运量明显回升**\n5月11-17日，澳洲\n\n[... middle omitted ...]\n\noW for the period 11th May to 17th May. Shipments from Australia were up by 1.08 Mt WoW. Shipments from Brazil were up by 3.16 Mt WoW.\n\nExhibit 1: Weekly data summary \n\n<table><tr><td rowspan=\n\n[... middle omitted ...]\n\n/td><td>HK$137.80</td></tr><tr><td>Zijin Mining Group (2899.HK)</td><td>O (11/06/2025)</td><td>HK$32.48</td></tr><tr><td>Zijin Mining Group (601899.SS)</td><td>O (11/06/2025)</td><td>Rmb29.99</td></tr></table>\n\n© 2026 MS"
  },
  {
    "id": "R014",
    "title": "中国创新药在ASCO 2026的真正信号：Keytruda的“最佳助推器”已经出现，但I/O 2.0的赢家尚未确定",
    "digest": "[wechat_article.md]\n# 中国创新药在ASCO 2026的真正信号：Keytruda的“最佳助推器”已经出现，但I/O 2.0的赢家尚未确定\n\n每年ASCO（美国临床肿瘤学会）的摘要发布，都会引发一轮对中国创新药企临床数据的密集解读。今年的第一波非小细胞肺癌（NSCLC）数据，表面上呈现的是几家公司的各自突破，但将它们放在同一张竞争格局图上，一个更清晰的判断浮现出来：**市场正在讨论的“谁能替代Keytruda”可能是一个错误的问题，真正值得追问的是“谁能成为Keytruda的最佳搭档”。**\n\n某外资投行最新发布的研报，通过对ASCO 2026首批摘要的梳理，给出了一个既克制又富有穿透力的框架。它没有陷入对中国Biotech的简单吹捧，而是将数据放在历史对照中，揭示了两个核心信号：第一，科伦博泰的Sac-TMT联合Keytruda在1L PD-L1阳性NSCLC中展现的数据，可能是目前所见最强的“Keytruda增强剂”；第二，信达生物的IBI363在后线治疗中提供了有希望的生存信号，但其在1L的野心仍需等待全球III期临床的验证。\n\n以下是我们基于这份研报的解读与推导。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 科伦博泰的OptiTROP-Lung05：PFS HR 0.35意味着什么，以及它为什么不是“Keytruda杀手”\n\n研报的核心看点集中在科伦博泰的III期OptiTROP-Lung05试验。在1L PD-L1阳性NSCLC患者中，Sac-TMT联合Keytruda对比Keytruda单药，中位无进展生存期（mPFS）在10.5个月的中位随访时仍未达到，而对照组为5.7个月，风险比（HR）为0.35。总生存期（OS）数据尚未成熟，但HR为0.55。\n\n这些数字单独看已经很亮眼，但研报通过横向对比赋予了它们更深的含义。\n\n[... middle omitted ...]\n\n合更多原始图表和交叉验证，拆解这些关键假设背后的逻辑与风险。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nKeytruda的最佳搭档找到了？🔬\n\n封面：NSCLC新数据拆解\nASCO 2026最值得关注的肺癌数据\n\n---\n\n刚刷完ASCO第一批摘要，有两个中国biotech的数据特别值得拿出来讲讲。\n\n先看科伦博泰的Sac-TMT。这个TROP2 ADC联合K药，在一线PD-L1阳性NSCLC里，PFS HR做到了0.35，OS HR 0.55。虽然数据还不成熟，但这个趋势是目前看到最好的。\n\n1️⃣ 横向对比一下\nK药单药mPFS大概5-6个月，AK112单药11个月，K药+化疗8-11个月，其他TROP2 ADC+K药9-13个月。Sac-TMT这个组合，mPFS推算下来16个月以上。之前二期OptiTROP-Lung01也报告过15.4个月，方向一致。\n\n2️⃣ OS HR 0.55\n这个早期趋势是目前同类试验里最强信号。亚组分析里，PD-L1 1-49%的患者获益比高表达组更明显，非鳞癌比鳞癌效果更好——两个都是更大的患者群体。\n\n所以问题不是“谁能取代K药”，而是“谁是最佳K药搭档”。Sac-TMT目前来看最有希望。\n\n再看信达的IBI363。在2L+免疫经治的NSCLC里，更新了数据。\n\n1️⃣ 后\n\n[... middle omitted ...]\n\nOptiTROP-Lung05): despite low data maturity, we found them strongly positive.\n\nMedian PFS not reached at median follow-up 10.5m vs. 5.7m, HR 0.35; OS not mature, HR 0.55. 1) Stretching the mPF\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R015",
    "title": "韩国外卖市场的稳定只是表象，真正的变局来自监管与所有权重构",
    "digest": "[wechat_article.md]\n# 韩国外卖市场的稳定只是表象，真正的变局来自监管与所有权重构\n\n韩国外卖市场正在经历一个看似平静但实则暗流涌动的阶段。经过数年的补贴大战与市场份额拉锯，Baemin与Coupang Eats的GTV份额稳定在65:35的格局。但这并非一个终局。某外资投行最新研报的核心判断是：当前的市场稳定建立在脆弱的平衡之上，真正的结构性变量——监管对Coupang的制约、Baemin所有权的潜在变动——才是决定未来三到五年竞争格局的关键。\n\n这份报告的价值不在于复述“市场正在稳定”这一表层叙事，而在于它揭示了一个容易被忽略的事实：韩国外卖市场的利润池并非由需求决定，而是由竞争结构决定。当补贴退潮，真正考验的是平台能否将用户规模转化为可持续的议价权。而这一点，恰恰是当前市场尚未定价的风险。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 补贴退潮后的稳定是真实的，但利润修复的路径比想象中更窄\n\n2025年底Coupang数据泄露事件后，外卖市场的竞争烈度显著下降。Coupang Eats的骑手补贴从峰值每单4000-10000韩元回落至2000-4000韩元，Wow会员对外卖订单的经济支持也在收缩。结果是，Baemin与Coupang Eats的GTV份额稳定在65:35。\n\n从利润端看，Baemin的营业利润率从2023年3.3%的高点逐步下滑至2025年的2.9%，而Coupang Eats则从亏损状态改善至0.7%的正利润率。表面上看，这是一个双赢的修复——行业不再烧钱，两家都在向盈利靠拢。\n\n但这里有一个关键问题：利润修复的来源是什么？报告显示，Coupang Eats的利润改善主要来自平台费用、配送费贡献和广告收入，而非来自规模效应或运营效率提升。这种修复的可持续性存疑——一旦竞争重新激化，这些利润项都可能被侵蚀。\n\n[... middle omitted ...]\n\n微信群里继续讨论，我们会基于完整报告进行更深度的拆解和推演。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n韩国外卖双雄：稳定但脆弱\n\n外卖格局趋稳，暗流涌动\n\n韩国外卖市场，Baemin 和 Coupang Eats 的 GTV 份额稳定在 65:35 左右，告别了烧钱补贴抢份额的“血拼时代”🛵。但这份稳定，真的牢靠吗？\n\n1️⃣ 补贴战熄火，转向精细化运营\n从 2023 年开始的骑手补贴大战，让每单利润被压缩到极致。现在双方都开始收手：Baemin 专注付费功能和广告变现，Coupang Eats 也在缩减 Wow 会员的补贴支持，把重心转向广告业务，利用自身电商生态做推广。行业正从“烧钱换增长”切换到“精耕细作”模式。\n\n2️⃣ 下一站：即时零售\n首尔以外的外卖市场空间有限，Coupang 把目光投向即时零售。Baemin 在疫情期间已抢先布局，目前约 15% 的收入来自这一板块（约 7800 亿韩元）。Coupang 则联手便利店推出 24 小时配送服务。未来，外卖平台和电商平台的合作，将成为即时零售增长的关键引擎。\n\n3️⃣ 政府补贴成变数\n韩国政府发放的 3.7 万亿韩元燃油补贴（可线下使用），将在 5-8 月显著利好 Baemin。关键点是：这笔补贴只适用于 Baemin，Coupang Eats 无法享\n\n[... middle omitted ...]\n\n2c775.jpg)\n\nWilliam Woods\n\n+44 20 7676 6806\n\nwilliam.woods@bernsteinsg.com\n\n![](images/fac80c839e532d189ee5e4b12aac495504542be2949988ba182c08631e5ffe09.jpg)\n\nChristophe Cherblanc\n\n+41 582 723 \n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R016",
    "title": "618首日直播GMV的真正信号：不是大盘回暖，而是品牌分层正在加速固化",
    "digest": "[wechat_article.md]\n# 618首日直播GMV的真正信号：不是大盘回暖，而是品牌分层正在加速固化\n\n618大促的首日头部主播直播数据已经出炉。这份来自某外资投行的最新快报，提供了一个比市场直觉更微妙的判断：整体GMV增速并不令人兴奋，但在这组平淡的数字之下，一个更关键的结构性变化正在发生——品牌之间的“增长分层”已经不再是季度性的业绩波动，而是演变为一种可预测的竞争格局固化。\n\n报告覆盖的十余个美妆品牌中，只有毛戈平实现了10%以上的同比增长，而巨子生物同比下滑约72%，华熙生物下滑约68%，贝泰妮和上海家化各下滑约20%。这些数字不是偶然的月度波动，它们指向一个更深层的行业逻辑：618大促正在从“所有品牌的增长引擎”转变为“头部品牌的压力测试器”。\n\n为什么这么说？因为大促的本质正在发生变化。过去，大促是品牌获取增量用户的杠杆；今天，当折扣力度趋于平稳、平台促销周期缩短、流量成本持续攀升时，大促反而成为检验品牌真实定价能力和用户粘性的试金石。那些在首日直播中还能实现正增长的品牌，其竞争优势已经不只是在产品力或营销效率层面，而是在品牌资产的复利效应上。\n\n以下，我们基于这份报告的详细数据，拆解四个关键洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 毛戈平的增长不是偶然，而是“高端国货”赛道定价权正在兑现的信号\n\n在几乎所有跟踪品牌中，毛戈平是唯一实现两位数同比增长的标的。其核心单品鱼子酱气垫GMV同比增长50%，新推出的妆前防晒隔离乳销量达到2万件。更值得注意的是，毛戈平在首日直播中的折扣率同比基本持平，并未通过加大促销力度换取增长。\n\n这意味着什么？毛戈平的GMV增长是“量价齐稳”甚至“量价齐升”的结果。在行业普遍通过增加SKU数量和捆绑销售来维持GMV的背景下，毛戈平仅以5-7个SKU就实现了超越同行的增长。这背后反映的是一\n\n[... middle omitted ...]\n\n现？毛戈平的增长能否持续？SKU扩张与利润率的权衡如何量化？\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n618美妆大促首日，谁在领跑？\n\n美妆618首轮战报\n\n头部主播直播间，国货与外资分化明显\n\n某外资投行刚出了618美妆第一波数据，我帮大家把核心看点拆出来了👇\n\n这次618大促，天猫和抖音的折扣力度和去年比基本持平，但活动周期缩短了。天猫折扣在15%off左右，抖音从15%off缩到13%off，京东也从17%off缩到10%off。平台整体更克制，不再卷“史上最大力度”。\n\n首日头部主播直播间，重点品牌表现分化很大：\n\n1️⃣ 毛戈平是最大赢家\nGMV同比增长10%+，核心单品鱼子酱气垫继续爆发（+50%），新出的妆前防晒隔离乳卖了2万件。折扣维持稳定，没有靠降价换量。\n\n2️⃣ 珀莱雅开局不错\n整体GMV只微降1%，其中主品牌增长4%，但彩棠下降43%（修容盘和遮瑕盘拖累）。这次上了21个SKU，比去年多5个，靠堆SKU和套装组合稳住了大盘。\n\n3️⃣ 巨子生物压力最大\nGMV同比下滑约72%，去年基数太高。公司策略转向自营店和中腰部主播，头部直播间投入减少。\n\n4️⃣ 贝泰妮/上海家化各下滑约20%\n薇诺娜和玉泽表现一般，但核心单品价格体系还稳。家化方面太极露相对坚挺，Vive面霜拖了后腿。\n\n5️⃣\n\n[... middle omitted ...]\n\n Per Exhibit 6 and Exhibit 7, Tmall promotions were stable vs. last 618 at $15\\%$ off. JD is offering 4 consumption coupons at up to $10\\%$ off, narrowed vs. last 618 with 2 coupons at up to $\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R017",
    "title": "中国医疗设备市场的真实分化：部分触底，但IVD的定价风险才刚刚开始",
    "digest": "[wechat_article.md]\n# 中国医疗设备市场的真实分化：部分触底，但IVD的定价风险才刚刚开始\n\n过去两年，外资医疗设备企业在中国经历了一场“集体降温”。从集采扩面到国产替代加速，从耗材降价到试剂控费，几乎每个细分赛道都感受到政策寒意的渗透。但进入2026年第一季度，情况出现了微妙的分化——不是全面复苏，而是一种“结构性触底”的信号。\n\n某外资投行最新发布的日本及全球医疗设备企业季报解析显示，中国市场的故事正在从“一刀切的政策冲击”演变为“按业务线、按产品、按定价模式的分化”。有的企业已经看到销量反弹，有的企业仍在深水区挣扎，而最值得警惕的信号，出现在体外诊断（IVD）这个此前被认为“相对安全”的领域。\n\n这份报告的核心判断是：市场对IVD领域的定价重构风险严重估计不足，而对部分已触底赛道的复苏弹性可能也低估了。真正值得关注的，不是“中国医疗市场好不好”，而是“你的业务组合是否落在政策余震的路径上”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 中国医疗设备市场的“触底”信号并非普适，而是高度依赖业务组合\n\n从多家企业的季报表述来看，“触底”一词的出现频率在上升，但这并不意味着全行业的拐点。真正触底的企业，往往具备两个特征：一是产品线已经经历过一轮集采冲击，二是销量增长开始弥补价格下滑。\n\n奥林巴斯在胃肠镜解决方案（GIS）业务上的表现就是一个典型案例。其中国业务在2025年第四季度同比下滑19%，但相比2025年第一季度的-16%、第二季度的-15%，下滑幅度并未显著恶化。更重要的是，管理层明确预期在2027财年实现复苏，部分驱动力来自本地化生产产品的增长。这暗示，对于已经完成本土化生产布局的企业，政策冲击的边际效应正在递减。\n\n泰尔茂的神经血管业务则展示了另一种“触底”路径：集采导致价格下降，但通过销售渠道扩展实现了量增，且量增幅\n\n[... middle omitted ...]\n\n包括我们对关键假设的验证思路，以及不同场景下的投资框架调整。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n医疗器械中国区，冰火两重天\n\n中国医械市场分化\n\n有的触底反弹，有的还在承压\n\n最近集中看了好几家全球医械巨头的一季报电话会，聊到中国区业务，状态真的不太一样。\n\n先划重点：整体看，中国医械市场有回暖信号，但成本控费政策和国产替代依然是主旋律。\n\n1️⃣ 日本厂商：分化明显\n- Olympus：中国区消化内镜业务4季度同比下滑19%，但3季度曾短暂转正（+6%）。公司预期要到2027财年才能恢复增长，靠的是国产化产品放量。\n- Sysmex：体外诊断业务受集采和渠道去库存双重暴击，4季度销售额暴跌38.5%。管理层对未来的价格统一政策（统一检测定价）充满不确定性，认为会给盈利带来波动。\n- Terumo：神经血管业务反而因集采放量，渠道扩张带来的销量增长覆盖了价格下降。\n- 朝日英特科：导丝价格下降的影响基本消化完毕（除了上海），未来靠量补价。\n\n2️⃣ 欧美巨头：冷暖自知\n- 强生：手术业务中国区1季度微增1.2%，但电生理产品2季度起将面临集采压力。\n- 雅培：核心实验室业务1季度中国区同比持平，相比去年每季下滑15-30%已是明显进步。管理层谨慎乐观，但指出80%的业务已纳入集采。\n- 波士顿科学：中国\n\n[... middle omitted ...]\n\nocused on progress in discussions on unifying test prices at Sysmex (link) and the contribution of locally manufactured products at Olympus.\n\nKey points from medtech company comments\n\nIn China\n\n[... middle omitted ...]\n\nhis information, in whole or in part, to train or\n\nfinetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R018",
    "title": "中国医药行业正在经历的不是周期反弹，而是商业模式的结构性重写",
    "digest": "[wechat_article.md]\n# 中国医药行业正在经历的不是周期反弹，而是商业模式的结构性重写\n\n中国医药行业正在经历一场被市场低估的底层逻辑切换。过去两年，投资者习惯于用“政策扰动”“集采压力”“地缘风险”这些标签来理解这个板块的波动。但某外资投行在近期全球中国峰会上的第二天纪要揭示了一个更值得认真对待的信号：中国医药公司正在从“成本优势驱动的外包服务商”和“仿制药跟随者”，转向“具备全球定价权的创新资产持有者”和“AI驱动的效率重构者”。\n\n这份报告的核心价值不在于它覆盖了多少家公司，而在于它串联起了一条清晰的逻辑线——从药明康德的产能扩张决心，到晶泰科技的AI实验室自动化，到泰格医药的AI临床运营降本，再到信达生物对2030年增长路径的明确规划，以及恒瑞和金赛在全球化BD中展现出的成熟策略。把这些信息放在一起看，得出的判断是：中国医药行业正在进入一个“供给端再定价”的阶段，而市场目前的讨论仍然停留在需求端。\n\n以下是我们从这份报告中提炼出的五个结构性判断，以及一个报告尚未完全回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 药明康德重申指引的真正信号不是保守，而是产能扩张的底层信心\n\n药明康德在全球中国峰会第二天重申了其2026财年指引，这本身并不令人意外。真正值得关注的是管理层对资本开支的表态：未来资本开支将增加，用于国内外产能扩张，且国内外投入基本对等。公司近期发行了67.8亿元人民币的可转债，目的正是为产能扩张储备现金。\n\n这里有一个容易被忽略的细节。报告提到，在小组会议中，许多投资者对药明康德的故事显得陌生。这意味着什么？意味着过去两年美国《生物安全法案》的地缘政治噪音，实际上把一批新的、对CXO行业缺乏深度理解的投资者带入了这个标的。他们关注的是“法案会不会通过”，而忽视了一个更基本的商业逻辑：药明康德的“R、D\n\n[... middle omitted ...]\n\n过跟踪BD交易结构的变化来提前判断中国医药公司的全球化进程。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国医药投研：AI 重塑研发，创新加速出海\n\n投研视角｜中国医药新趋势\n\n---\n\n最近看了一份外资投行的中国医药行业研报，信息量很大。核心逻辑很清晰：**AI 正在渗透研发全链条，而中国药企的全球化步伐比想象中更快**。\n\n几个关键看点，整理给大家参考。\n\n**1️⃣ 药明康德：TIDES 业务继续高增长**\n\n公司重申了 2026 年的业绩指引，增长驱动力来自“R、D、M”三大业务板块。其中 TIDES（寡核苷酸和多肽）业务预计 2026 年增长 40%，国内和海外需求都很强劲。虽然美国 BIOSECURE 法案仍是潜在的扰动因素，但管理层表示客户并未主动询问该法案，也未看到执行层面的更新。值得注意的是，公司近期发行了 67.8 亿元人民币用于产能扩张，国内和海外投入基本对半。\n\n**2️⃣ 晶泰科技：AI 驱动的药物发现生态**\n\n晶泰科技正在通过灵活的合作模式和自动化实验室能力，扩展 AI 驱动的药物发现生态。商业模式多元化，既有服务费也有特许权使用费，业务已拓展至 siRNA 和多肽等新领域。公司宣称，借助 24/7 自动化实验室和 METiS 递送平台，从靶点发现到临床前候选化合物的时间已缩短至 \n\n[... middle omitted ...]\n\n; 5) Innovent's management expressed confidence in achieving a CAGR of $15\\% \\sim 20\\%$ from 2027-2030.\n\n\\- WuXi AppTec reiterated its FY2026 guidance, driving growth through its “R”, “D”, and\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 22 May 2026 02:09 AM HKT\n\nDisseminated 22 May 2026 02:09 AM HKT"
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "Exhibit 1",
    "context": "EXHIBIT 1: April import was \\$2.7 billion"
  },
  {
    "figure_id": "F002",
    "report_id": "R001",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: Month-over-month showed 12% decline, mostly dragged down by lithography import. Total WFE imports to China MoM growth by segment (monthly) (USDmn)"
  },
  {
    "figure_id": "F003",
    "report_id": "R001",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: The year-over-year figures only show a modest decline, given that weak lithography imports were offset by stronger deposition imports. Total WFE imports to China YoY growth by segment (monthly) (USDmn)"
  },
  {
    "figure_id": "F004",
    "report_id": "R001",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: The lithography import was \\$142mn in Apr 2026, much weaker than last year Lithography imports to China (monthly) (USDmn)"
  },
  {
    "figure_id": "F005",
    "report_id": "R001",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: 2026 YTD import -13% YoY Total WFE imports to China by year"
  },
  {
    "figure_id": "F006",
    "report_id": "R001",
    "label": "Exhibit 7",
    "context": "EXHIBIT 6: U.S. import share & U.S. + Singapore + Malaysia import share"
  },
  {
    "figure_id": "F007",
    "report_id": "R001",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: Netherlands' share was flattish, Japan decreased by 3ppt, US+Singapore+Malaysia in aggregate grew slightly Total WFE imports to China by region EXHIBIT 8: Excluding lithography, there has been a gradual uptick in impor"
  },
  {
    "figure_id": "F008",
    "report_id": "R001",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: Netherlands' share was flattish, Japan decreased by 3ppt, US+Singapore+Malaysia in aggregate grew slightly Total WFE imports to China by region EXHIBIT 8: Excluding lithography, there has been a gradual uptick in impor"
  },
  {
    "figure_id": "F009",
    "report_id": "R001",
    "label": "Exhibit 9",
    "context": "EXHIBIT 9: In 2025, imported Lithography intensity just slightly dropped by 1ppt, further declined in 2026 Total WFE imports to China market share by equipment type"
  },
  {
    "figure_id": "F010",
    "report_id": "R001",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: The share of lithography imports was only 5%, hitting a record low Share of lithograph of total WFE import to China by month"
  },
  {
    "figure_id": "F011",
    "report_id": "R001",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: Share of lithography imports from Japan has decreased since Aug 2023 and remains relatively low. Lithography imports to China - share by region (monthly)"
  },
  {
    "figure_id": "F012",
    "report_id": "R001",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: Netherlands' lithography imports share increased materially after 2022 and is still increasing in 2025 Lighography imports to China - share by region (yearly)"
  },
  {
    "figure_id": "F013",
    "report_id": "R001",
    "label": "Exhibit 13",
    "context": "EXHIBIT 13: The correlation between monthly China litho imports and ASML's quarterly China systems revenue (divided by 3) is fairly solid. April imports of EUR 87Mnwere down 87% MoM and 65% YoY, marking the lowest datapoint since Ju"
  },
  {
    "figure_id": "F014",
    "report_id": "R001",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: Our regression yields an R2 of 0.79 indicating robust predictive power using 1 month of data. The implied China revenue for 2Q26 is EUR 0.44Bn due to weak litho imports in April. ASML Quarterly PRC Sales vs. 1M PRC Impor"
  },
  {
    "figure_id": "F015",
    "report_id": "R001",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: The predicted systems sales from China at EUR 0.44Bn represents a 71% decline QoQ. This implies China revenue representing only 7% of Q2 total system sales. EXHIBIT 16: Our estimate for ASML's China system sales in Q2 im"
  },
  {
    "figure_id": "F016",
    "report_id": "R001",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 17: Based on our estimate of ASML's China system sales, we expect China's contribution to decline to $7\\%$ of total system sales, the lowest level in over five years China as % of ASML's Quarterly System Sales"
  },
  {
    "figure_id": "F017",
    "report_id": "R001",
    "label": "Exhibit 18",
    "context": "EXHIBIT 18: LRCX 1-month regression yields R2 of 0.83 and should have decent predictive power..."
  },
  {
    "figure_id": "F018",
    "report_id": "R001",
    "label": "EXHIBIT 19",
    "context": "EXHIBIT 19: ...with our analysis suggesting China revenues for LRCX down \\~28% sequentially in Jun-Q... EXHIBIT 20: ...with overall Jun-Q China exposure predicted at \\~22% vs Mar-Q exposure of \\~34% LRCX China WFE Revenue as % of To"
  },
  {
    "figure_id": "F019",
    "report_id": "R001",
    "label": "Exhibit 21",
    "context": "EXHIBIT 21: The AMAT 3-month regression yield R2 of 0.87 and hence should have solid predictive power... AMAT Quarterly China Sales vs Relevant Semicap Imports to China in Quarterly Billings of Q115-Q126"
  },
  {
    "figure_id": "F020",
    "report_id": "R001",
    "label": "EXHIBIT 22",
    "context": "EXHIBIT 22: The regression predicted AMAT's China revenue would be flattish in the April quarter vs the actual flattish growth reported by the company last week, in-line with results EXHIBIT 23: AMAT's China exposure fell to \\~26.4%"
  },
  {
    "figure_id": "F021",
    "report_id": "R001",
    "label": "Exhibit 25",
    "context": "EXHIBIT 24: The KLAC 1-month regression yields R2 of 0.84 and hence should have decent predictive power... KLAC Quarterly China Sales vs Relevant Semicap Imports to China in 1st Month of Q115-Q226E"
  },
  {
    "figure_id": "F022",
    "report_id": "R001",
    "label": "EXHIBIT 25",
    "context": "EXHIBIT 25: ...with our analysis suggesting China revenues for KLAC up \\~17% sequentially in the Jun-Q... EXHIBIT 26: ...with overall Jun-Q China exposure predicted at \\~27% vs Mar-Q exposure of \\~24% KLAC China WFE Revenue as % of"
  },
  {
    "figure_id": "F023",
    "report_id": "R001",
    "label": "Exhibit 27",
    "context": "Exhibit 27-Exhibit 30)."
  },
  {
    "figure_id": "F024",
    "report_id": "R001",
    "label": "EXHIBIT 28",
    "context": "EXHIBIT 28: China import yields decent correlation with TEL's China revenue."
  },
  {
    "figure_id": "F025",
    "report_id": "R001",
    "label": "EXHIBIT 29",
    "context": "EXHIBIT 29: The regression suggests TEL's revenue from China to be +14% QoQ in JunQ. EXHIBIT 30: ...with implied China exposure of 32% vs MarQ exposure of 27% China as % of TEL's Quarterly SPE Revenue"
  },
  {
    "figure_id": "F026",
    "report_id": "R001",
    "label": "Exhibit 31",
    "context": "Exhibit 31-Exhibit 33). EXHIBIT 31: Kokusai's Quarterly China sales shows decent correlation with monthly import. Kokusai Quarterly PRC Sales vs. 1M PRC Import: 2QCY22-1QCY26"
  },
  {
    "figure_id": "F027",
    "report_id": "R001",
    "label": "EXHIBIT 33",
    "context": "EXHIBIT 33: ...with implied China exposure at 51% vs MarQ exposure of 28% China as % of Kokusai's Quarterly SPE Revenue"
  },
  {
    "figure_id": "F028",
    "report_id": "R001",
    "label": "Exhibit 34",
    "context": "Exhibit 34-Exhibit 36). EXHIBIT 34: Screen's Quarterly China sales shows some correlation with monthly import. Screen Quarterly PRC Sales vs. 1M PRC Import: 2QCY18-1QCY26"
  },
  {
    "figure_id": "F029",
    "report_id": "R001",
    "label": "EXHIBIT 35",
    "context": "EXHIBIT 35: The regression suggests Screen's revenue from China to be -73% QoQ in JunQ. EXHIBIT 36: ...with overall China exposure predicted at 12% vs DecQ exposure of 46% China as % of Screen's Quarterly SPE Revenue"
  },
  {
    "figure_id": "F030",
    "report_id": "R001",
    "label": "Exhibit 37",
    "context": "Exhibit 37-Exhibit 39) EXHIBIT 37: Advantest's Quarterly China sales shows decent correlation with monthly import."
  },
  {
    "figure_id": "F031",
    "report_id": "R001",
    "label": "EXHIBIT 38",
    "context": "EXHIBIT 38: Our regression suggests Advantest's China sales to be -7% QoQ in MarQ. EXHIBIT 39: ...with overall China exposure predicted at 17% vs SepQ exposure of 15% China as % of Advantest's Quarterly SPE Revenue"
  },
  {
    "figure_id": "F032",
    "report_id": "R002",
    "label": "Figure 1",
    "context": "Figure 1: New drivers of China exports %pts contribution to total exports (US\\$) %oya growth"
  },
  {
    "figure_id": "F033",
    "report_id": "R002",
    "label": "Figure 2",
    "context": "Figure 2: Export growth of selected products"
  },
  {
    "figure_id": "F034",
    "report_id": "R002",
    "label": "Figure 3",
    "context": "Figure 3: China export growth breakdown"
  },
  {
    "figure_id": "F035",
    "report_id": "R002",
    "label": "Figure 4",
    "context": "Figure 4: Exports of new-three products %pts contribution to total exports %oya growth"
  },
  {
    "figure_id": "F036",
    "report_id": "R002",
    "label": "Figure 5",
    "context": "Figure 5: Export decomposition %pts contribution to value %oya growth"
  },
  {
    "figure_id": "F037",
    "report_id": "R002",
    "label": "Figure 6",
    "context": "Figure 6: Export price breakdown (in US\\$ terms)"
  },
  {
    "figure_id": "F038",
    "report_id": "R002",
    "label": "Figure 7",
    "context": "Figure 7: China imports from Korea breakdown %pts contr. to %oya growth, both scales"
  },
  {
    "figure_id": "F039",
    "report_id": "R002",
    "label": "Figure 8",
    "context": "Figure 8: Net trade of selected tech products"
  },
  {
    "figure_id": "F040",
    "report_id": "R002",
    "label": "Figure 9",
    "context": "Figure 9: China commodity import volume growth decomposition"
  },
  {
    "figure_id": "F041",
    "report_id": "R002",
    "label": "Figure 10",
    "context": "Figure 10: China imports breakdown"
  },
  {
    "figure_id": "F042",
    "report_id": "R002",
    "label": "Figure 11",
    "context": "Figure 11: Trade volume growth"
  },
  {
    "figure_id": "F043",
    "report_id": "R003",
    "label": "Figure 3",
    "context": "Figure 1: Japan and US 10Y Interest Rates"
  },
  {
    "figure_id": "F044",
    "report_id": "R003",
    "label": "Figure 2",
    "context": "Figure 2: 2026 YTD Trend in Japan-US 10-Year Interest Rates (2026/1=100)"
  },
  {
    "figure_id": "F045",
    "report_id": "R003",
    "label": "Figure 3",
    "context": "Figure 3: JGB 10Y Yield and USDJPY Since 1995"
  },
  {
    "figure_id": "F046",
    "report_id": "R003",
    "label": "Figure 4",
    "context": "Figure 4: Japan 10Y Breakeven Inflation Rate (BEI)"
  },
  {
    "figure_id": "F047",
    "report_id": "R003",
    "label": "Figure 5",
    "context": "Figure 5: Japan Import Price Index"
  },
  {
    "figure_id": "F048",
    "report_id": "R003",
    "label": "Figure 6",
    "context": "Figure 6: Economic Surprise Index"
  },
  {
    "figure_id": "F049",
    "report_id": "R003",
    "label": "Figure 7",
    "context": "Figure 7: Consumer Confidence Index"
  },
  {
    "figure_id": "F050",
    "report_id": "R003",
    "label": "Figure 8",
    "context": "Figure 8: Fiscal Impact of Key Policy Measures Figure 10: General Government Debt-to-GDP Ratio General Government Debt-to-GDP Ratio"
  },
  {
    "figure_id": "F051",
    "report_id": "R003",
    "label": "Figure 9",
    "context": "Figure 9: Japan Primary Balance"
  },
  {
    "figure_id": "F052",
    "report_id": "R003",
    "label": "Figure 11",
    "context": "Figure 11: General Government PB-to-GDP Ratio General Government PB-to-GDP Ratio"
  },
  {
    "figure_id": "F053",
    "report_id": "R003",
    "label": "Figure 12",
    "context": "Figure 12: Capital Adequacy Ratios of Regional Banks and Shinkin Banks vs. JGB 10Y Yield"
  },
  {
    "figure_id": "F054",
    "report_id": "R003",
    "label": "Figure 14",
    "context": "Figure 14: Borrowing Ratio by Sector"
  },
  {
    "figure_id": "F055",
    "report_id": "R003",
    "label": "Figure 16",
    "context": "Figure 16: Semiconductor Stock Price Performance During Periods of Sharp Rate Increases"
  },
  {
    "figure_id": "F056",
    "report_id": "R003",
    "label": "Figure 17",
    "context": "Figure 17: Electric Appliances Stock Valuation During Periods of Sharp Rate Increases"
  },
  {
    "figure_id": "F057",
    "report_id": "R006",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: Accountants see what is visible (e.g. IFRS vs GAAP). IFRS vs GAAP International accounting"
  },
  {
    "figure_id": "F058",
    "report_id": "R006",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: Super-accountants - like sommeliers - can see what is invisible PARKER 98°/100 VINOUS 97°/100"
  },
  {
    "figure_id": "F059",
    "report_id": "R006",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: Falling in love with IFRS 18? It's the requirement to present the cash flow statement using the indirect method (i.e. starting with operating income rather than net income) that makes it attractive! Silhouette of a cou"
  },
  {
    "figure_id": "F060",
    "report_id": "R006",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: Contract assets & contract liabilities ```mermaid graph LR"
  },
  {
    "figure_id": "F061",
    "report_id": "R006",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: There is a significant portion (c.45%) of net cash within the €2.7bn NCL"
  },
  {
    "figure_id": "F062",
    "report_id": "R007",
    "label": "Exhibit 1",
    "context": "EXHIBIT 1: Global WFE: China demand expected to be continue strong while non-China will grow stronger going forward"
  },
  {
    "figure_id": "F063",
    "report_id": "R007",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: China WFE: Acceleration in domestic substitution continues, expect the self-sufficiency to reach 43% by 2028 A few highlights to the industry model update (Exhibit 3): # From a supply side perspective: - For 2025 China"
  },
  {
    "figure_id": "F064",
    "report_id": "R007",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: We revised up 2026E/2027E/2028E by \\$2.9/\\$7.3/\\$16.4 bn"
  },
  {
    "figure_id": "F065",
    "report_id": "R007",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: We revised up our numbers mostly due to stronger CapEx in memory China WFE Market Share by End Market (USD bn)"
  },
  {
    "figure_id": "F066",
    "report_id": "R007",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: All five companies expect China WFE to be roughly flat YoY but China as a percentage of revenue to normalize lower in 2026 vs. the elevated 2024–2025 levels EXHIBIT 6: Apr 2026 WFE import was USD 2,737 mn, YoY -12% & MoM"
  },
  {
    "figure_id": "F067",
    "report_id": "R007",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: Apr 2026 YTD import YoY -13%, mainly due to weak Lithography & Process Control import Total WFE imports to China by year"
  },
  {
    "figure_id": "F068",
    "report_id": "R007",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: 1Q26 import data was below historical trendline. We suspect this is mostly due to the time windows difference between shipment & reveneu. Top 5 China Systems Rev. vs. Import Data (Calendar Quarter)"
  },
  {
    "figure_id": "F069",
    "report_id": "R008",
    "label": "Exhibit 1",
    "context": "Exhibit 1: We continue to estimate that US power transformer demand/local supply gap would narrow from $72\\%$ to $60\\%$ in 2028E; while US PPI has stabilized at a high level, China export price is up $+23\\%$ yoy (Feb-Apr avg, for 2"
  },
  {
    "figure_id": "F070",
    "report_id": "R008",
    "label": "Exhibit 2",
    "context": "Exhibit 2: China total transformer export value grew $27\\%$ in April (slowing vs $56\\%$ in March) Exhibit 3: China transformer export value to the US grew +95% yoy in April (vs 118% yoy in March)"
  },
  {
    "figure_id": "F071",
    "report_id": "R008",
    "label": "Exhibit 2",
    "context": "Exhibit 2: China total transformer export value grew $27\\%$ in April (slowing vs $56\\%$ in March) Exhibit 3: China transformer export value to the US grew +95% yoy in April (vs 118% yoy in March) Transformer export value to US"
  },
  {
    "figure_id": "F072",
    "report_id": "R008",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Export transformer to the US market has seen a relatively volatile ASP in 10-220MVA due to volatile mix change..."
  },
  {
    "figure_id": "F073",
    "report_id": "R008",
    "label": "Exhibit 6",
    "context": "US PPI for Electric Power and Specialty Transformer vs CPI (Jan 2018 indexed to 100)"
  },
  {
    "figure_id": "F074",
    "report_id": "R008",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Key raw materials for transformer, GOES, saw prices inch down, while copper price had a sharp increase in 4Q25, and dipped in March 2026"
  },
  {
    "figure_id": "F075",
    "report_id": "R008",
    "label": "Exhibit 5",
    "context": "Exhibit 5: ...but transformer in the 220-330MVA category saw pricing decline by 14% yoy in April, with Feb-April rolling average pricing still up 23% yoy"
  },
  {
    "figure_id": "F076",
    "report_id": "R008",
    "label": "Exhibit 7",
    "context": "Exhibit 7: US power and specialty transformers' PPI rose earlier than other product categories, while switchgear pricing has caught up in recent months (+14% yoy in April)"
  },
  {
    "figure_id": "F077",
    "report_id": "R008",
    "label": "Exhibit 9",
    "context": "Exhibit 9: China total transformer export value grew $27\\%$ in April (slowing vs $56\\%$ in March)"
  },
  {
    "figure_id": "F078",
    "report_id": "R008",
    "label": "Exhibit 10",
    "context": "Exhibit 10: China transformer export value to the US grew +95% yoy in April (vs 118% yoy in March) Exhibit 11: China electronic meter export value was flat at $0\\%$ in April (vs. $-6\\%$ yoy in March)"
  },
  {
    "figure_id": "F079",
    "report_id": "R008",
    "label": "Exhibit 10",
    "context": "Exhibit 10: China transformer export value to the US grew +95% yoy in April (vs 118% yoy in March) Exhibit 11: China electronic meter export value was flat at $0\\%$ in April (vs. $-6\\%$ yoy in March) Electronic meter export valu"
  },
  {
    "figure_id": "F080",
    "report_id": "R008",
    "label": "Exhibit 12",
    "context": "The author would like to thank Zhou Li, Hao Chen, Zhihan Ye, and Junfang Zhang for their contributions to this report. # Disclosure Appendix # Reg AC"
  },
  {
    "figure_id": "F081",
    "report_id": "R012",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Looking ahead to 2027, oil E&Ps offer a median FCF yield of 12% at strip (\\~\\$75 WTI). US Majors and Canadian oil sands producers sit closer to 8% 2027 FCF Yield Sensitivity"
  },
  {
    "figure_id": "F082",
    "report_id": "R012",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Since the start of the Iran conflict, E&Ps have risen 7%, underperforming the broader market by \\~1% Performance"
  },
  {
    "figure_id": "F083",
    "report_id": "R012",
    "label": "Exhibit 4",
    "context": "Exhibit 4: The median FCF yield for our oil coverage is 12% at \\~\\$88 WTI (near FY26 avg implied by bal-year strip). This would move by \\~2% for every \\$10 change in oil. CHRD, NOG & APA all screen particularly well across a range"
  },
  {
    "figure_id": "F084",
    "report_id": "R012",
    "label": "Exhibit 3",
    "context": "Exhibit 3: We estimate consensus is currently pricing in \\~\\$80 WTI based on 2026 EBITDAX estimates, lower than the full-year average of \\$88 implied by the latest strip Oil-Weighted Upside/Downside to Consensus 2026 EBITDAX"
  },
  {
    "figure_id": "F085",
    "report_id": "R012",
    "label": "Exhibit 5",
    "context": "Exhibit 5: At prices near strip, we see about 10% upside to FY26 consensus EBITDA, rising to 30% at \\$105. We also see significant upside to estimates for the US majors, supported by strong downstream margins Exhibit 6: Our 2026"
  },
  {
    "figure_id": "F086",
    "report_id": "R012",
    "label": "Exhibit 5",
    "context": "Exhibit 5: At prices near strip, we see about 10% upside to FY26 consensus EBITDA, rising to 30% at \\$105. We also see significant upside to estimates for the US majors, supported by strong downstream margins Exhibit 6: Our 2026"
  },
  {
    "figure_id": "F087",
    "report_id": "R012",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Our 2026 capex estimates remain roughly unchanged on average as most operators maintained their activity plans..."
  },
  {
    "figure_id": "F088",
    "report_id": "R012",
    "label": "Exhibit 7",
    "context": "Exhibit 7: MSe roughly in line with consensus on average"
  },
  {
    "figure_id": "F089",
    "report_id": "R012",
    "label": "Exhibit 9",
    "context": "Exhibit 9: ... with MSe \\~1% above consensus on average"
  },
  {
    "figure_id": "F090",
    "report_id": "R012",
    "label": "Exhibit 10",
    "context": "Exhibit 10: The E&P sector reflects long-term WTI price of \\~\\$70, \\~16% below 12-month strip prices of \\~\\$83"
  },
  {
    "figure_id": "F091",
    "report_id": "R012",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Gas E&Ps reflect a median Henry Hub price of \\~\\$3.50, \\~3% above 12-month future prices"
  },
  {
    "figure_id": "F092",
    "report_id": "R012",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Price Target Changes Exhibit13: Total Coverage Bull/Bear/Base Upside & Downside"
  },
  {
    "figure_id": "F093",
    "report_id": "R012",
    "label": "Exhibit 44",
    "context": "Exhibit 44: WoW Energy Sub-sector Performance WoW Performance"
  },
  {
    "figure_id": "F094",
    "report_id": "R012",
    "label": "Exhibit 45",
    "context": "Exhibit 45: YTD Energy Sub-sector Performance YTD Performance"
  },
  {
    "figure_id": "F095",
    "report_id": "R012",
    "label": "Exhibit 46",
    "context": "Exhibit 46: Best & Worst E&P WoW Performance WoW Performance"
  },
  {
    "figure_id": "F096",
    "report_id": "R012",
    "label": "Exhibit 47",
    "context": "Exhibit 47: WoW Performance by E&P Sub-sector WoW Performance"
  },
  {
    "figure_id": "F097",
    "report_id": "R012",
    "label": "Exhibit 48",
    "context": "Exhibit 48: NAV implied oil prices in our coverage now sit $\\sim 16\\%$ below the 12-month strip price"
  },
  {
    "figure_id": "F098",
    "report_id": "R012",
    "label": "Exhibit 49",
    "context": "Exhibit 49: Our oil coverage has an average of $\\sim 20\\%$ of 2026 production hedged % of 2026 Oil Production Hedged (Upside Limit)"
  },
  {
    "figure_id": "F099",
    "report_id": "R012",
    "label": "Exhibit 50",
    "context": "Exhibit 50: Gas E&Ps have hedged \\~53% of estimated 2026 production on average % of 2026 Gas Production Hedged (Upside Limit)"
  },
  {
    "figure_id": "F100",
    "report_id": "R012",
    "label": "Exhibit 51",
    "context": "Exhibit 51: At our price deck of \\~\\$88 WTI in 2026, we forecast a median realized price of \\~\\$85/bbl for our oil coverage. EOG, MUR, and APA have the highest realized prices due to limited hedges and/or geographic mix 2026 Realize"
  },
  {
    "figure_id": "F101",
    "report_id": "R013",
    "label": "Exhibit 1",
    "context": "Exhibit 2: Weekly steel demand Weekly Steel Demand"
  },
  {
    "figure_id": "F102",
    "report_id": "R015",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: Korea's food delivery market is stabilizing, but regulatory risks around Coupang and any shift in Baemin's ownership could still reshape competition. Korea FD Market Evolution"
  },
  {
    "figure_id": "F103",
    "report_id": "R015",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Intense rider subsidy competition has compressed per-order profitability in Korea's food delivery market from 2023."
  },
  {
    "figure_id": "F104",
    "report_id": "R015",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: Coupang Eats' subsidy-driven share gains are fading as support from Wow membership - once key to per-order economics - is scaled back. Coupang Eats: Unit economics per order"
  },
  {
    "figure_id": "F105",
    "report_id": "R015",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 6: Baemin's revenue growth rate has been decelerated..."
  },
  {
    "figure_id": "F106",
    "report_id": "R015",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 6: Baemin's revenue growth rate has been decelerated..."
  },
  {
    "figure_id": "F107",
    "report_id": "R015",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: ... Baemin margin has been under pressure with the Coupang competition."
  },
  {
    "figure_id": "F108",
    "report_id": "R015",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: Baemin, an early mover since COVID, already generates about 15% of revenue from quick commerce."
  },
  {
    "figure_id": "F109",
    "report_id": "R015",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: We see potential for quick commerce to regain growth momentum as the focus of food delivery shifts."
  },
  {
    "figure_id": "F110",
    "report_id": "R015",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: Coupang Eats has gained revenue momentum by capturing incremental share from Baemin."
  },
  {
    "figure_id": "F111",
    "report_id": "R015",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: Coupang Eats' margins improved in 2025, supported by a period of subdued competition."
  },
  {
    "figure_id": "F112",
    "report_id": "R015",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: Looking ahead, partnerships across food delivery and product commerce platforms could become a key lever in capturing the next wave of quick commerce growth. Domestic E-Commerce Players"
  },
  {
    "figure_id": "F113",
    "report_id": "R015",
    "label": "EXHIBIT 13",
    "context": "EXHIBIT 13: The Korean FTC's designation of founder Bom Kim as the \"same person\" for Coupang, announced on April 29, 2026 Coupang's shareholding structure ```mermaid graph TD"
  },
  {
    "figure_id": "F114",
    "report_id": "R015",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: The ongoing KFTC investigation into Coupang's Wow membership bundling, especially the tie between core Product Commerce and Coupang Eats, is a central regulatory swing factor."
  },
  {
    "figure_id": "F115",
    "report_id": "R016",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Proya/MAOGEPING/Shiseido/Winona/Comfy/Herborist introduced more SKUs yoy, while QuadHA/Collgene/Biohyalux/Timage cut back in listings Number of SKUs in the top tier KOLs' beauty presale livestreaming Number of SKUs in"
  }
]