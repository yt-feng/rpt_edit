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
    "title": "GS：印度30年国债的买入窗口已经打开",
    "digest": "[wechat_article.md]\n# GS：印度30年国债的买入窗口已经打开\n\n印度国债市场正在经历一个罕见的“三重共振”：宏观基本面改善、央行政策转向友好、全球指数纳入预期升温。GS最新发布的亚洲汇率与利率策略报告明确建议做多印度30年期国债，目标收益率从当前的7.34%下行至6.90%。这一判断并非孤立的交易建议，而是对印度主权债市场结构性重估的押注——其背后的逻辑链条，值得所有关注新兴市场资产配置的决策者认真审视。\n\n这份报告的发布时点耐人寻味。就在几周前，印度央行与财政部联合推出了一系列资本流入便利化措施，包括取消外国机构投资者买卖政府债券的利息和资本利得税、扩大完全可进入路径债券的发行范围至30年和40年期。市场对此已有初步反应，但GS认为，真正的结构性利好尚未被充分定价。\n\n**KC评论：** GS的这个推荐不是短线交易，而是基于印度债券市场“可投资性”的系统性提升。如果你只看收益率数字，可能觉得44个基点的下行空间并不惊人。但关键是，这个判断背后隐含的是印度国债从“边缘资产”向“核心配置”的跃迁——这才是真正的alpha来源。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 宏观叙事已经转向：通胀和财政的双重压力正在消退\n\n今年一季度，印度国债收益率曾大幅上行50-70个基点，市场对能源和化肥价格上涨的担忧是主要推手。但GS指出，实际冲击远小于最初的恐慌预期。一季度实际GDP同比增长7.8%，比GS自己的预测还高出约50个基点，投资和服务业活动是主要支撑。\n\n更关键的是，随着美伊临时协议的达成，全球油价预期显著下修。GS据此将印度2026日历年的实际GDP预测上调0.3个百分点至6.8%，2027财年预测上调0.4个百分点至6.5%。油价下跌不仅直接改善贸易条件，还降低了政府上调零售燃料价格的压力——尽管此前泵价上调的滞后效应仍会在未\n\n[... middle omitted ...]\n\nmarket dynamics。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n印度30年国债，逻辑变了\n\n📉 宏观改善 + 政策助攻\n\n印度30年国债的叙事正在切换。\n\n年初受能源冲击，10Y收益率一度飙升50-70bp，但实际影响低于预期。Q1实际GDP同比7.8%，超预期50bp，投资和服务强劲。油价回落+美伊协议预期，让通胀和财政压力同步降温。\n\n1️⃣ 通胀+财政双改善\n\n某外资投行最新预测：将CY26核心通胀下调至4.2%，CY27降至4.0%。全球尿素价格大跌，肥料补贴账单好于预期。更低的通胀路径+更轻的财政负担，为长端利率下行打开空间。\n\n2️⃣ RBI的“引流”操作\n\n6月5日，印度央行和政府推出多项资本流入措施：\n- 新NRE存款可全额外汇对冲\n- 准主权机构可获优惠掉期利率\n- 关键：取消FII投资国债的利息和资本利得税（大幅降低操作摩擦）\n- 扩大“完全准入路径”至所有新发15/30/40年期国债\n\n这些措施不仅吸引外资，更扫清了彭博全球综合指数纳入的障碍。\n\n3️⃣ 指数纳入只是时间问题\n\n彭博1月推迟纳入决定至2026年中，但印度已成功纳入JPMGBI-EM指数并触及9%权重上限。RBI新政后，纳入全球综合指数“方向确定，时间待定”。若纳入，预计权重约0.7%\n\n[... middle omitted ...]\n\nices activity. With Q2 growth tracking above earlier expectations and oil forecasts now revised lower, we recently raised our CY26 real GDP forecast by 0.3pp to $6.8\\%$ and our FY27 forecast b\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R002",
    "title": "摩根斯坦利：MS：美联储今年加息的“数据路线图”已经画好",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：美联储今年加息的“数据路线图”已经画好\n\n这份报告最值得看的判断，并非美联储今年加不加息，而是MS首席美国经济学家Michael Gapen团队为“加息”画出了一条清晰的数据触发路径。在多数市场参与者仍在争论通胀是否见顶时，这家华尔街顶级投行已经提前设定了“如果数据这样走，我们就改变观点”的具体条件。这不是一份预测报告，而是一份决策地图。\n\n为什么现在重要？因为6月美联储会议后，有9位FOMC参与者提交了至少一次加息的预测，而市场对“暂停”的定价可能过度乐观。MS虽然维持“全年按兵不动”的基准判断，但坦承这一判断高度依赖几项正在快速变化的假设。换句话说，当前市场的平静，可能只是数据尚未触发警报。\n\n报告的核心逻辑是：通胀和就业数据在未来三个月的走向，将决定美联储9月会议是“继续观望”还是“重新扣动扳机”。这份报告的价值不在于结论，而在于它给出了一个可验证、可跟踪的观察框架。\n\n> **KC评论：** 这份报告最值得细读的不是结论，而是MS设定的“触发条件”。它就像一张地图，标出了哪些数据点位会让美联储从“按兵不动”转向“加息”。对于关注利率敏感资产的读者，理解这些条件比猜测加息概率更有用。完整报告中包含了每个触发条件的量化阈值和对应的资产价格影响测算。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 通胀的“0.2%分水岭”决定了美联储的耐心能持续多久\n\nMS的核心通胀预测比FOMC中位数更为乐观。他们预计核心PCE和核心CPI的月度环比增速将维持在0.2%或以下。这一判断建立在三个关键假设上：关税传导效应正在结束、美伊谅解备忘录推动油价回落、以及住房通胀将继续放缓。\n\n但如果月度核心通胀持续保持在0.3%或更高，MS就会改变看法。0.3%这个数字不是随意设定的——它对应的是FOMC参与者预测\n\n[... middle omitted ...]\n\nmarket dynamics。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美联储今年真会加息？数据说了算\n\n**加息路线图**\n\n**关键数据决定，不是猜测**\n\n某外资投行最新研报解析，美联储6月会议后，9位官员预测今年至少加息一次。但投行自己维持“全年按兵不动”的判断。这背后是4个核心逻辑，今天拆给你看。\n\n1/ **通胀没那么可怕**\n投行认为关税传导已近尾声，核心商品将明显降温。加上美伊谅解备忘录推动油价回落，住房通胀也在放缓。预测今年Q4核心PCE仅3.0%，远低于美联储官员的普遍预期。\n\n2/ **美联储可能高估了通胀**\n3月官员们做预测时，中东冲突刚爆发，他们可能低估了短期通胀压力。6月做预测时，油价还没跌。投行认为官员们的预测“偏高了”。\n\n3/ **投票权是关键**\n9个“鹰派”点大多是地方联储主席，今年没有投票权。投行推测，有投票权的委员更倾向于维持现状。\n\n4/ **消费正在降温**\n一季度消费增速从1.4%下调至0.5%，二季度跟踪也明显走软。投行认为，如果美联储有耐心，多数委员不会选择更紧的政策。\n\n但数据如果这样走，投行会改口——\n\n**通胀触发条件**：6-8月核心CPI/PCE月率持续高于0.3%（投行预测是0.2%以下）；美伊协议破裂，油价反弹。\n\n[... middle omitted ...]\n\nmist</td></tr><tr><td>Sam.Coffin@morganstanley.com</td><td>+1 212 761-4630</td></tr><tr><td colspan=\"2\">Diego Anzoategui</td></tr><tr><td colspan=\"2\">Economist</td></tr><tr><td>Diego.Anzoategu\n\n[... middle omitted ...]\n\nntee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n## © 2026 MS"
  },
  {
    "id": "R003",
    "title": "摩根斯坦利：MS：美元兑日元接近公允价值，但真正的机会在“跌出来的买点”",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：美元兑日元接近公允价值，但真正的机会在“跌出来的买点”\n\n美元兑日元正在逼近2024年7月161.95的高点，但这一次的驱动力已经悄然改变。MS最新发布的日本外汇策略报告指出，此轮日元走弱并非源于日元自身的抛售，而更多是美元全面走强的结果。这一判断直接影响了市场最关心的两个问题：日本财务省何时会出手干预？以及，现在是否值得入场？\n\n这份报告的结论是：美元兑日元已接近公允价值，MS维持中性立场，正在等待一个更清晰的“逢低买入”机会。这听起来像是一份谨慎的观望报告，但仔细拆解其逻辑框架，你会发现它实际上为投资者划定了一个非常明确的行动边界。\n\n**KC评论：** 这份报告的核心判断不是“看多”或“看空”，而是“等待”。它告诉读者，当前价格已经充分反映了已知信息。真正的利润空间，来自于市场对某些关键假设的误判，或者来自于日本财务省干预制造的短期超调。完整报告中用三因素模型精确定义了“公允价值”的边界，并给出了触发“超调”的具体条件，这些是普通行情软件无法提供的分析框架。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 驱动力切换：从“做空日元”到“做多美元”，这改变了干预的触发逻辑\n\n报告最关键的洞察在于区分了美元兑日元上涨的两种驱动力。2024年2月底至5月初，上涨主要由日元走弱驱动，这符合典型的“套息交易”环境。但自5月中旬以来，市场环境切换为“美元看涨环境”，其标志是美国实际利率上升而盈亏平衡通胀率下降。\n\n这一切换的宏观背景是：中东局势缓和导致油价下跌，通胀担忧缓解；同时美联储立场偏鹰，AI相关股票疲软压制了风险偏好。在这种环境下，日元虽然对美元走弱，但相对于其他G10货币反而表现更好。\n\n这个区别对日本财务省的干预判断至关重要。历史经验表明，日本当局更倾向于在确认“投机性日元头寸”变得极端\n\n[... middle omitted ...]\n\n迎来到我们的星球微信群继续讨论，共同跟踪这些关键变量的变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美元兑日元逼近前高，但这次不一样\n\n📊 等一个回调买点\n\n美元走强才是主因，日元没那么弱\n\n最近美元/日元（USD/JPY）又摸到去年7月的高点附近，但仔细看，这轮上涨的驱动力变了——不是日元在跌，是美元在涨。\n\n某外资投行最新研报的核心逻辑，我帮你拆成3点：\n\n1️⃣ 驱动力切换，干预风险降低\n之前日元走弱时，日本财务省（MoF）很容易出手干预。但这次是美元全面走强，日元相对其他货币其实表现不错。MoF对“投机性日元抛售”更敏感，对“美元走强”容忍度更高。虽然口头警告升级了，但实际干预还没到眼前。\n\n2️⃣ 当前汇率接近“公允值”\n研报用三个因子定价：美国终端利率定价、全球风险情绪、日本贸易条件。目前USD/JPY基本就在这个模型算出的合理区间附近。油价比之前低，日本贸易条件改善，对日元形成支撑。\n\n3️⃣ 等一个更清晰的买入点\n研报维持中性，不追高、不抄底。想入场，需要等一个更明确的机会——比如MoF真的动手干预了，或者风险情绪大幅恶化。目前美国经济数据还稳，AI板块的盈利担忧可能是潜在的下行风险。\n\n📌 简单说：现在不是追涨的时候，也不是恐慌的时候。保持观察，等回调。\n\n欢迎一起讨论你对日元走势的看法。\n\n[... middle omitted ...]\n\nIntervention risk has increased, but imminent action does not yet appear likely. The MoF has stepped up verbal warnings, but has not yet characterized recent FX moves as clearly “speculative.”\n\n[... middle omitted ...]\n\n are Fixed Income Research Analysts/Strategists and are not opining on or expressing recommendations on equity securities: Molly Nickolin; David S. Adams, CFA; Andrew M Watrous; Koichi Sugisaki; Hiromu Uezato.\n\n© 2026 MS"
  },
  {
    "id": "R004",
    "title": "JPM：人民币正在成为全球波动中的“安全锚”",
    "digest": "[wechat_article.md]\n# JPM：人民币正在成为全球波动中的“安全锚”\n\n2026年上半年，全球金融市场在贸易摩擦、地缘冲突与货币政策分化中剧烈震荡。多数新兴市场货币承压，全球债券市场遭遇抛售。但有一个资产类别走出了独立行情：人民币。\n\n截至6月底，美元兑离岸人民币（USD/CNH）年内再跌2.4%，中国国债（CGB）总回报约5%。在全球资产普遍波动的背景下，人民币汇率与利率双双展现出罕见的韧性。JPM在最新发布的《中国本地市场2026年中展望》中，明确给出了一个核心判断：人民币正在成为全球高波动环境下的相对安全港，且这一趋势在下半年仍将持续。\n\n这不是一个基于国内经济强劲复苏的乐观叙事。恰恰相反，这份报告承认国内需求依然疲弱、数据超预期下行。但正是这种“基本面偏弱、资产偏强”的背离，揭示了中国市场当前最值得关注的结构性变化。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 人民币的强势正在脱离利率和基本面，但这恰恰是它最值得关注的特征\n\n传统外汇分析框架中，汇率强弱通常与利差、经济数据周期高度相关。但JPM的数据显示，2026年上半年，美元兑人民币与中美利差的关联度正在显著下降。按照利差定价模型，当前USD/CNH的“公允值”应远高于实际交易水平——也就是说，人民币比模型预测的要强得多。\n\n与此同时，中国经济数据意外指数在二季度大幅转负，投资与内需全面走弱。按照常规逻辑，这应该对汇率形成压力。但人民币不仅没有走弱，反而在二季度加速升值。\n\n这种背离让很多投资者感到困惑。但JPM的研究指出，这恰恰是人民币市场的历史常态。从2018年到2022年，人民币曾长期与利差脱钩运行，且并未出现均值回归。根本原因在于：中国以贸易主导的国际收支结构、严格管理的资本账户以及有限的外资参与，使得宏观与周期条件的波动难以迅速传导为资本流动——尤其是资本外流\n\n[... middle omitted ...]\n\n，也方便人工快速把握市场动态。欢迎在星球和微信群中继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n人民币的“安全港湾”逻辑\n\n人民币汇率：为何能持续走强\n\n某外资投行最新研报指出，人民币正成为全球波动中的“避风港”📊\n\n1️⃣ 出口韧性是核心支撑\n尽管国内需求偏弱，但出口持续超预期，尤其科技类出口商（光伏、电动车、电池）提价能力增强，带动名义出口增长。企业结汇意愿回升，2025年以来中国企业从净购汇转为净结汇，累计净卖出美元约5430亿美元。\n\n2️⃣ 服务贸易逆差收窄\n免签政策扩容后，入境旅游强劲反弹，已超疫情前水平，而出境游趋于平稳，每年帮助缩小服务贸易逆差约500-600亿美元。\n\n3️⃣ 外资流入回暖\n外资买入A股节奏为近年最快，全球主动基金仍低配中国，后续有补仓空间。债券方面，人民币资产与全球利率低相关性，正被视作分散配置的选项。\n\n4️⃣ 企业仍有大量“美元储备”\n2022年以来中国企业积累的超额美元储蓄约5500-9150亿美元，即使部分结汇，也会对汇率形成支撑。\n\n5️⃣ 政策面友好\n中美利差虽走阔，但高层互动预期下，央行可能维持偏宽松的汇率管理姿态。\n\n⚠️ 研报也提示：当前人民币定价已偏“贵”，与基本面有脱节，但历史表明这种脱节可能持续较长时间。\n\n你觉得人民币这轮走强能持续到年底吗？\n\n[... middle omitted ...]\n\n shifting USD backdrop, lifted the CNY TWI by 4.5% and drove outperformance versus Asia and major G10 FX. Meanwhile, CNY rates remained insulated from the global rates sell-off, with yields lo\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R005",
    "title": "GS：工业利润环比转负，但这不是最值得关注的事",
    "digest": "[wechat_article.md]\n# GS：工业利润环比转负，但这不是最值得关注的事\n\n5月中国工业利润数据出炉，同比增长21.0%，看似不差。但GS团队在最新报告中指出的核心信号恰恰藏在同比数字背后：经季节调整后，工业利润环比下降8.4%，而4月为环比增长7.9%。一正一负之间，才是当前经济修复成色的真实写照。\n\n这份报告最值得读的判断不是“利润还在增长”，而是“增长动能在5月出现边际放缓，且结构分化比总量更值得警惕”。GS没有用“复苏”或“放缓”这样的大词，而是用环比数据说话——利润环比转负的同时，营收仍在环比正增长（+0.4%），这意味着什么？利润率的压力正在从上游向中下游传导，而产业链不同环节的议价能力差异正在成为决定企业盈利前景的关键变量。\n\n对于关注中国资产配置的投资者而言，这份报告提供了一个重要的观察窗口：总量数据已经不够用了，必须拆开看结构。而结构里藏着的，可能是机会，也可能是陷阱。\n\n> **KC评论：** GS这组数据最值得关注的不是同比，而是环比。同比21%的增长里有明显的低基数效应，环比转负才是当前真实动能的信号。完整报告里有两张关键图表——利润和营收的环比走势对比、以及分上下游的利润率变化拆解——这两张图合在一起看，才能理解为什么GS团队认为“利润率的改善主要来自上游”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 利润环比转负，但营收韧性仍在，说明企业正在“以价换量”\n\n5月工业利润环比下降8.4%，营收环比增长0.4%。营收还在扩张，利润却在收缩，最直接的解读就是利润率在恶化。\n\nGS的数据进一步印证了这一点：12个月平均利润率仍在缓慢上行，但驱动因素几乎全部来自上游。换句话说，下游企业正在用更低的利润率换取市场份额或订单量，而上游企业则凭借资源或原材料端的定价权继续享受利润扩张。\n\n这种“上游吃肉、下游喝汤”的格\n\n[... middle omitted ...]\n\n里，我们可以继续拆解这份报告里没有完全展开的关键图表和假设。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月工业利润：环比降了，但别慌\n\n📊 利润增速放缓，但结构在变好\n\n5月工业利润同比+21.0%，比4月的+26.0%有所回落。更关键的是环比——经季调后环比下降8.4%，而4月是+7.9%。\n\n收入端相对稳：同比+6.7%（4月+5.8%），环比+0.4%（4月+0.7%）。\n\n1️⃣ 上游利润依然猛，但增速收窄\n上游利润同比+58.3%（4月+83.5%），贡献主要来自化学原料、煤炭采选、有色金属。统计局说，原材料制造贡献了1-5月工业利润增长的10.2个百分点。\n\n2️⃣ 下游利润小幅提速\n下游利润同比+10.2%（4月+9.0%），不算惊艳但方向不错。\n\n3️⃣ AI浪潮带飞电子+有色\n全球AI投资热支撑了电子行业利润，也拉动了铝、铜等有色金属。高技术制造和装备制造分别贡献了8pp和5.2pp的增长。\n\n4️⃣ 利润率继续微升\n12个月平均利润率在5月继续小幅上行，主要靠上游拉动。\n\n一句话总结：5月利润环比回落，但收入还在增长，利润率也在改善。上游强、下游弱的结构没变，但AI相关链条的支撑在增强。\n\n#学习笔记\n\n[source_mineru.md]\n# China: Industrial prof\n\n[... middle omitted ...]\n\n26.0% yoy (sequential growth: +7.9% sa non-annualized).\n\nIndustrial revenue: +6.7% yoy in May (sequential growth: +0.4% non-annualized, seasonally adjusted by GS); April: +5.8% yoy (sequential\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R006",
    "title": "摩根斯坦利：MS：能源股跌过头了，但真正的机会不在油价反弹",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：能源股跌过头了，但真正的机会不在油价反弹\n\nWTI从冲突高点回落至72美元，能源股却跌回了冲突前的水平。美股油气勘探与生产公司（E&Ps）已回到地缘冲突爆发前的价位，而大型综合石油公司（Majors）甚至比那个水平还低了9%。MS在最新研报中更新了价格假设和估值模型，核心判断是：这轮回调创造了买入窗口，但理由不是油价会涨，而是当前股价已经计入了比期货更悲观的价格预期。\n\n报告最值得关注的判断不是油价预测，而是估值信号。MS测算，覆盖的石油公司当前股价隐含的长期WTI价格仅为每桶64美元，比12个月期货低约6%，也低于该行长期假设的70美元。这意味着，即便油价不再上涨，仅靠估值回归，这些公司也有可观的修复空间。\n\n在70美元WTI的价格附近，摩根士坦利覆盖的石油公司2027年自由现金流收益率中位数达到10%，其中美国E&Ps为12%，大型综合石油公司为9%，加拿大公司为10%。天然气公司也达到了9%。这些数字在宏观不确定性笼罩的当下，显得格外突出。\n\n> **KC评论：** 10%的自由现金流收益率意味着什么？简单说，如果一家公司维持当前产量和成本结构，以现价买入，大约10年能通过自由现金流收回投资。在标普500整体自由现金流收益率不到4%的背景下，这确实是一个结构性差异。但关键在于，这些收益率是在MS自己的价格假设下算出来的，而不是市场共识。完整报告里有详细的敏感性分析，可以看看油价每变动10美元，收益率会如何摆动。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 股价回调幅度已经超过了油价回调的合理反映\n\n自6月14日美伊达成谅解备忘录以来，WTI下跌约15%至72美元，仅略高于冲突前水平。但能源股的反应更为剧烈：E&Ps完全跌回冲突前价格，美国大型综合石油公司更是跌至冲突前水平以下9%。\n\n[... middle omitted ...]\n\n迎来星球和微信群里继续讨论，一起拆解这些研报背后的投资逻辑。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n油价跌了15%，能源股还值得看吗？\n\n能源板块回调，机会在哪？\n\nWTI回到$72，能源股跌回冲突前水平\n\n某外资投行最新研报更新了价格预测，核心逻辑分享👇\n\n1️⃣ **油价跌了，但公司质地没变**\nWTI从高点回落约15%，现在$72/桶。能源股同步回调，油气勘探公司回到冲突前水平，大型油企甚至跌了9%。研报认为回调后风险回报比改善。\n\n2️⃣ **自由现金流依然能打**\n按当前$70油价估算，2027年油气公司自由现金流收益率中位数达10%。其中美国油气勘探公司12%，大型油企9%，加拿大公司10%。内在估值只反映$64油价，比当前价格保守。\n\n3️⃣ **研报调整了价格预期**\n2026年WTI预期从$88下调至$78，2027年维持$70不变。目标价平均下调5-8%，但依然隐含约25%上行空间。\n\n4️⃣ **天然气和LNG也有看点**\n亚洲LNG价格仍同比涨超50%，卡塔尔出口逐步恢复。美国Henry Hub天然气短期有支撑，但2027年展望偏软。\n\n5️⃣ **研报偏好哪些方向？**\n偏好大型油企和正向变化率的油气勘探公司，以及LNG生产商。整体看，回调后估值更有吸引力。\n\n💡 核心逻辑：油价跌了\n\n[... middle omitted ...]\n\nys at \\$70. Our EBITDA ests are -7% vs consensus for FY26 and -6% for '27\n\nFor 2Q, our EBITDA ests are in-line with consensus for oil producers and 8% below for gas. We also forecast above con\n\n[... middle omitted ...]\n\nr Energy Inc (SU.TO)</td><td>E (12/16/2024)</td><td>C$77.10</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.\n\n\\* Historical prices are not split adjusted.\n\n## © 2026 MS"
  },
  {
    "id": "R007",
    "title": "NOM：AI Agent正引爆一场被低估的元器件短缺",
    "digest": "[wechat_article.md]\n# NOM：AI Agent正引爆一场被低估的元器件短缺\n\nAI模型迭代的速度，正在系统性快于企业系统的部署能力。这个差距，正是当前半导体与电子元器件行业最核心的供需矛盾所在。\n\nNOM在最新发布的日本电子行业深度报告中，给出了一个清晰且值得警惕的判断：AI带来的需求冲击，已从GPU、HBM蔓延至ASIC、SSD，而现在，它正抵达CPU、模拟芯片和MLCC——这些是过去被认为“AI受益有限”的品类。更关键的是，NOM认为，这一轮供需紧张可能比市场预期的更持久，因为AI服务器市场对价格完全不敏感，供应商反而因涨价而加大资本开支，形成自我强化的正向循环。\n\n这不是一篇简单的行业景气度追踪。NOM的核心洞察在于：AI Agent的规模化部署，正在从“技术验证”阶段进入“工程落地”阶段，而日本电子产业链——从半导体设备、电子元器件到IT服务商——恰好卡在最关键的基础设施交付环节。\n\n以下是我们从这份报告中提炼的五个核心判断，以及它们对产业决策和投资框架的启示。\n\n> **KC评论：** 市场习惯把AI受益者分为“英伟达和其他”。但NOM的报告提醒我们，当AI Agent从训练走向推理、从云端走向边缘，受益链条会显著拉长。模拟芯片、被动元件、甚至传统的CPU，都可能成为下一个供不应求的品类。这份报告最值得看的部分，是它如何拆解“AI Agent阶段”的硬件需求图谱——这是目前多数研报尚未系统覆盖的盲区。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI Agent的落地瓶颈，正从模型能力转向工程部署能力\n\n报告开篇就点出了一个反直觉的现象：AI模型的进步速度，持续快于系统部署速度。换句话说，企业不是不知道AI有用，而是不知道如何用、谁来帮他们用。\n\nNOM观察到，大型IT公司和私募股权基金正在加强“前向部署工程”能力。所\n\n[... middle omitted ...]\n\n司拆解和供需模型感兴趣，欢迎来我们的知识星球微信群继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI投研｜日本电子业正在“抢人”部署Agent\n\nAI加速，日本电子业进入“FDE时代”\n\n最近读某外资投行的日本电子研报，发现一个有趣信号：AI Agent的落地速度，正在倒逼整个产业链的供需逻辑发生变化。不仅是GPU/HBM，连传统模拟芯片、MLCC的交付周期都在拉长。这背后，是头部IT公司和PE在疯狂部署“前场工程团队”（FDE）。\n\n1/ AI需求从训练转向推理，再蔓延到Agent阶段，带动CPU、模拟芯片、MLCC供应吃紧。研报认为，这不再是短期波动，结构性短缺可能持续。\n\n2/ 日本IT巨头的中期计划是利润年增15%以上，但研报判断，AI Agent的渗透会让增速更快。不是威胁，而是机会。\n\n3/ 记忆体方面，DDR5现货价5月环比涨3.1%，NAND合约价动能强劲。虽然近期有负面消息（客户联名信、NVIDIA减配计划），但研报未看到需求放缓，反而认为是结构性供应短缺。\n\n4/ 重点提了两个公司：Hitachi在组建“Physical AI FDE团队”，Fujitsu也在强化自家Takane AI模型的FDE团队。这些团队直接驻场客户，解决部署痛点，再反哺产品迭代。\n\n5/ 电子零件板块，10家\n\n[... middle omitted ...]\n\n agents. We think AI represents substantial business opportunities rather than a threat. Shipments of servers and networking equipment for AI have also been rising sharply as companies increas\n\n[... middle omitted ...]\n\n listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nCopyright © 2026 NOM Securities Co., Ltd., Japan. All rights reserved."
  },
  {
    "id": "R008",
    "title": "波士顿咨询：金融科技的下一个关口不是增长，是“审慎经营”",
    "digest": "[wechat_article.md]\n# 波士顿咨询：金融科技的下一个关口不是增长，是“审慎经营”\n\n当一家金融科技公司从“不计成本的增长”转向“盈利性增长”，它面临的最大挑战往往不是融资环境，而是内部能力结构的重塑。波士顿咨询（BCG）与QED Investors联合发布的《2024年全球金融科技报告》给出了一个核心判断：金融科技行业正在从“增长优先”转向“审慎经营优先”，这一转变的深度和速度，将决定哪些公司能够穿越周期，进入下一个十年。\n\n这份报告的一个核心数字值得反复咀嚼：到2030年，全球金融科技市场规模将从目前的3200亿美元增长至1.5万亿美元，接近五倍。但通往这个规模的道路，不再由“烧钱换用户”铺就，而是由“合规能力+单位经济模型+盈利性增长”三重门槛构成。\n\n报告采访了60多位全球金融科技CEO和投资者，梳理出九大趋势、四大发展主题和五项行动呼吁。但最让人印象深刻的，不是这些框架本身，而是报告反复强调的一个看似朴素却极具杀伤力的结论：**审慎经营，即将成为金融科技公司的核心竞争力。**\n\n这意味着什么？意味着过去十年里，金融科技公司赖以生存的“监管套利”窗口正在关闭。监管环境正在趋同，银行与金融科技公司之间的竞争规则正在拉平。当所有人都必须在同样的合规框架下竞争，那些提前把合规能力建造成护城河的公司，将获得结构性优势。\n\n> **KC评论：** 对于关注金融科技赛道的投资者和从业者来说，这份报告最值得记住的不是1.5万亿的远期规模，而是“审慎经营”这四个字背后隐含的竞争逻辑。过去大家比的是谁跑得快，未来比的是谁在合规框架下跑得稳。这意味着，合规部门将从成本中心变成战略部门。完整报告里有大量关于如何构建合规优势的具体案例和框架，包括银行与金融科技公司合作的最佳实践，值得细读。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 融资寒冬没有杀死金融科\n\n[... middle omitted ...]\n\n趋势和议题，欢迎加入我们的社群，领取完整研报解读与原始图表。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n金融科技进入“审慎增长”阶段\n\n审慎经营，盈利提升\n\n金融科技的下一个关键词：稳\n\n金融科技行业正在经历一场“降温”后的理性回归。某外资投行最新研报指出，行业融资规模较2021年高点骤减约70%，市销率也从20倍降至4倍。但别急着悲观——行业营收依然保持14%的年增长，剔除加密和中国市场后，增速甚至达到21%。\n\n1️⃣ 告别“烧钱换增长”\n过去“不计成本增长”的模式已行不通。2023年，上市金融科技公司EBITDA利润率平均提升9个百分点，但多数仍未达到“40法则”（营收增速+利润率≥40%）。新口号很清晰：在维持正现金流的前提下，尽可能快地增长。\n\n2️⃣ 四大主题重塑格局\n🔹 嵌入式金融：到2030年市场规模将达3200亿美元，中小企业市场占半壁江山\n🔹 互联商务：银行终于开始用客户数据做精准广告，大通、Citi已率先布局\n🔹 开放银行：影响有限，英国月活用户率仅12%，但对广告业可能产生更大冲击\n🔹 生成式AI：短期最大价值在提效——代码编写、客户支持、数字营销\n\n3️⃣ 挑战者银行证明了自己\nNubank用户破1亿，Monzo实现经营盈利，Revolut营收达20亿美元。它们没有统一成功路径，但都扎根市\n\n[... middle omitted ...]\n\n难行。\n\n我们采访了60多位全球金融科技公司的CEO和投资者，了解他们对行业未来发展的看法，同时结合我们的行业经验，撰写了本报告。我们认为，九大趋势正在塑造当前金融科技市场格局，其中有些是新近出现的趋势，有些趋势则由来已久。透过上述发展趋势，我们看到四大核心议题的重要性日益凸显，金融科技公司和传统银行需要正视和应对这些变化和挑战。最后，我们将探讨新兴金融科技生态中的参与者需要践行的\n\n[... middle omitted ...]\n\n<td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>"
  },
  {
    "id": "R009",
    "title": "波士顿咨询：全球财富正在重新“扎堆”，香港首次超越瑞士",
    "digest": "[wechat_article.md]\n# 波士顿咨询：全球财富正在重新“扎堆”，香港首次超越瑞士\n\n全球金融财富在2025年增长了10.7%，达到333万亿美元，创下2021年以来最快增速。但这份由波士顿咨询（BCG）发布的《2026全球财富报告》真正值得关注的，不是总量数字，而是四个正在同时发生的结构性变化。这些变化正在重新定义财富的流向、持有者、服务模式，以及行业竞争的底层逻辑。\n\n报告的核心判断是：财富管理行业正在进入一个“大重组”时期。那些在过去十年被视为理所当然的竞争位置，正在被不可逆的力量侵蚀。而最大的机会，恰恰藏在行业最不擅长服务的角落。\n\n如果你只读一份关于全球财富趋势的报告，今年应该是这一份。以下是我们从报告中提炼出的四个关键洞察。\n\n> **KC评论：** 这份报告的价值不在于预测，而在于它画出了一张“正在发生的地图”。读完你会发现，很多你以为是“未来趋势”的东西，其实已经在数据里了。完整报告里有大量按地区、按资产类别、按渠道拆分的图表，这些细节才是判断自己所在市场是否被高估或低估的关键。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 财富增长正在向两个核心“枢纽”集中，香港与瑞士构成新的双极格局\n\n报告最引人注目的发现之一，是跨境财富的集中度正在加速提升。2025年，全球跨境财富增长了8.4%，达到15.7万亿美元，而排名前十的记账中心拿走了近90%的新增跨境资金，并持有超过80%的存量。\n\n更关键的变化在于：香港首次以微弱优势超越瑞士，成为全球最大的跨境财富记账中心。香港的跨境财富在2025年增长了10.7%，达到2.9万亿美元，主要驱动力来自中国大陆的资金流入和活跃的IPO市场。瑞士同样达到2.9万亿美元，但增速为7.6%，其客户基础更偏向西欧市场。\n\n新加坡则扮演了“亚洲最多元化财富枢纽”的角色，成为中美紧张局势下的避险资金受益者\n\n[... middle omitted ...]\n\n便喂给AI进行二次分析，也方便你快速把握全球市场的动态变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球财富版图，正在经历一次大洗牌\n\n全球财富加速向少数地区集中\n\n2025年全球金融财富增长10.7%，达到333万亿美元，创2021年以来最快增速。但增长的分布很不均匀。\n\n1️⃣ 财富流向正在“双中心化”\n香港首次超越瑞士，成为全球最大跨境财富中心，规模达2.9万亿美元。新加坡凭借中立定位，吸引了超2000家单一家族办公室。这两个亚洲枢纽正在主导跨境资金流向。\n\n2️⃣ 新兴市场是下一个增长极\n除中国外，印度、巴西、墨西哥三国将贡献全球金融财富增长的约10%。这些市场的富裕人群和中产上层，是目前行业服务最薄弱的群体，也是最大的机会窗口。\n\n3️⃣ 亚洲迎来首次大规模代际财富转移\n未来十年，亚洲家族将面临治理、领导权、所有权和传承目标的重大决策。能帮家族理清这些复杂议题的财富管理机构，将定义行业的下一个十年。\n\n4️⃣ AI正在重塑财富管理\nAI已经从辅助工具变成核心引擎。研报指出，那些只在现有流程上叠加AI工具的公司，与真正围绕AI重构业务的公司，差距会迅速拉大。顾问不学会与AI协作，将越来越被动。\n\n独立财富管理公司正在崛起。在美国，它们控制了约25%的高净值资产；在新加坡、印度、阿联酋，增速高达12%\n\n[... middle omitted ...]\n\n, who holds it, and what it will take to serve clients well are changing rapidly.\n\nThis report examines four dimensions of that change. The first is geographic. Wealth creation continues to co\n\n[... middle omitted ...]\n\nd register to receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on LinkedIn, Facebook, and X.\n\n![](images/7cae113a411c1eee30d5fe2bd5fa20d9019d781637a6fb5ed948d0741043d3ba.jpg)"
  },
  {
    "id": "R010",
    "title": "波士顿咨询：新能源公司AI投入翻三倍，但多数人正在浪费钱",
    "digest": "[wechat_article.md]\n# 波士顿咨询：新能源公司AI投入翻三倍，但多数人正在浪费钱\n\n几乎所有大型企业都在加大AI投入，但能源与公用事业公司的扩张速度远超多数行业。波士顿咨询（BCG）最新AI雷达调查显示，这些公司计划2026年的AI支出较2025年翻三倍，增幅仅次于保险业。\n\n然而，一个残酷的现实正在浮现：尽管热情高涨，综合性能源公司和纯可再生能源玩家，在利用AI创造实际价值方面普遍举步维艰。\n\n这不是技术问题，而是方法问题。BCG基于与多家客户的深度合作，提炼出六条经验教训，核心指向一个判断：**可再生能源企业若不能将AI投入与具体运营指标严格挂钩，并解决真实世界的操作瓶颈，这轮高达数倍的投资浪潮很可能变成一场昂贵的实验。**\n\n这份报告的价值不在于罗列AI能做什么，而在于它揭示了“为什么大多数AI项目在新能源领域无法落地”的结构性原因。对于正在制定AI战略的产业决策者而言，这六条教训中的每一条，都可能是避免数千万资金浪费的关键。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 不要在“用AI做什么”上浪费时间，先回答“要改哪个KPI”\n\n大多数新能源公司的AI项目启动方式错了。它们往往从宏大愿景或端到端转型开始，而不是从“未来6到12个月内，能否让某个关键指标有实质性改善”出发。\n\nBCG给出了一个极其尖锐的判断标准：**如果你在项目启动第一周内，不能清晰说出要测量哪些KPI，并解释这个用例如何影响资产层面的损益表，那你不是在运行AI项目，你是在做研究。**\n\n可再生能源领域的价值创造，最终要落到几个硬指标上：能量产出、设备可用率、每兆瓦时运营成本、每千瓦时建设成本。AI项目必须直接挂钩其中之一。\n\n报告提供了一个令人振奋的数据：通过构建10到15个用例，企业通常能实现整体价值潜力的60%到70%。但这建立在一个前提上——每个用例都指向一\n\n[... middle omitted ...]\n\n法，以及如何建立“中心-辐射”式AI治理结构的具体操作指南。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI搞新能源，这6步走对了\n\n**别急着上大模型**\n\n能源公司今年AI投入要翻三倍，但很多砸了钱却没看到实际效果。BCG这篇研报给出了6条实操建议，帮你在新能源领域真正用AI创造价值。\n\n**1. 先盯死一个KPI**\n不要一上来就想搞“全面转型”。先选一个能显著提升的关键指标，比如能源产出或设备可用率。6-12个月内做出可量化的改进，再考虑推广。\n\n**2. 解决最卡脖子的环节**\n别想着把所有流程都重做一遍。找到当前最拖后腿的瓶颈（比如维修零件订购、排班），用AI精准解决。一个瓶颈打通了，其他环节自然跟着受益。\n\n**3. 跟着一线员工干活**\nAI工具的设计不能靠理论。去现场观察调度员和技师怎么工作，他们用哪些系统，卡在哪里。只有贴合真实操作流程的方案，才不会被员工“束之高阁”。\n\n**4. 快，但要有纪律**\n新能源企业不能“先跑再修”。先用小范围测试，快速淘汰无效方案。同时设定安全边界和人工干预机制，确保不会影响运营稳定性。\n\n**5. MVP直接嵌入工作流**\n最小可行产品别只做演示，要真正用起来。可能需要强制关停旧系统，避免新旧并行。让用户成为方案的主人，推动真正的行为改变。\n\n**6. 靠组\n\n[... middle omitted ...]\n\nor all other sectors except insurers.\n\nDespite the growing enthusiasm, integrated energy companies and pure players are struggling to create tangible value from AI in their renewables business\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R011",
    "title": "波士顿咨询：AI重塑的岗位远超它消灭的岗位，但CEO的决策窗口只有两年",
    "digest": "[wechat_article.md]\n# 波士顿咨询：AI重塑的岗位远超它消灭的岗位，但CEO的决策窗口只有两年\n\n未来两到三年内，美国50%到55%的岗位将被AI重塑。这不是一个遥远的预言，而是波士顿咨询公司（BCG）最新研报给出的量化判断。\n\n这份报告最值得关注的核心结论，不是AI会消灭多少工作，而是它如何改变工作的本质。报告明确指出，未来四到五年内，美国只有10%到15%的岗位可能被AI完全替代。真正的大潮，是剩下那超过一半的岗位——从业者可能保留同样的职位头衔，但工作方式、产出标准和能力要求将发生根本性变化。\n\n对于企业决策者而言，这个时间窗口意味着什么？BCG给出的答案是：今天做出的关于自动化、技能提升和人才规划的选择，将直接决定企业在AI时代是变得更强大，还是被竞争对手甩开。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 43%的岗位面临高自动化风险，但“替代”不是唯一结局\n\nBCG的分析框架打破了一个常见误区：高自动化潜力不等于高失业风险。报告首先识别出，美国43%的岗位中，超过40%的任务可以被当前AI能力自动化。这个比例看起来惊人，但真正的分野在于，这些岗位中的任务是被AI“替代”还是被“增强”。\n\n以呼叫中心代表和软件工程师这两个已经大规模部署AI的岗位为例，两者的命运截然不同。\n\n呼叫中心代表的工作高度结构化：账户查询、政策解释、脚本化故障排除。当AI系统能端到端处理这些重复性问询时，企业对人工代表的需求必然下降。即使部分代表可以转型为更高价值的客户关系维护角色，整体岗位数量仍将收缩。\n\n软件工程师则完全不同。虽然编码包含常规元素，但角色的核心价值在于系统设计、架构判断、性能与成本的权衡、以及将业务需求转化为技术方案。AI可以极大加速代码生成和测试，但无法替代端到端拥有成果所需的系统级判断。软件开发变成人与AI的持续互动，工程师定义目标\n\n[... middle omitted ...]\n\n据图表合集，既方便喂给AI快速分析，也方便人工把握市场动态。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI不会让工作消失，而是重塑工作\n\n**AI重塑工作**\n\n**50%到55%的工作将在2-3年内被AI重塑**\n\n最近读了一份某外资投行的研报，核心结论让人安心又警醒：AI不是来抢饭碗的，是来改工作方式的。\n\n1️⃣ **关键数字**\n- 未来2-3年，美国50%-55%的工作会被AI重塑\n- 5年后，只有10%-15%的工作可能被替代\n- 43%的工作任务自动化潜力超过40%\n\n2️⃣ **替代vs增强**\n- 呼叫中心代表：结构化工作多，AI更容易替代\n- 软件工程师：需要系统判断和设计思维，AI更多是增强\n- 关键区别：工作能不能被清晰拆分成AI和人类部分\n\n3️⃣ **需求弹性决定就业**\n- 软件需求弹性大：AI降低成本后，企业建更多软件，就业反而增长\n- 呼叫中心需求固定：效率提升后，需要的代表反而减少\n- 这就是\"杰文斯悖论\"：效率提升可能增加总消费\n\n4️⃣ **六类工作命运**\n- 增强型（5%）：AI增强+需求扩张，就业稳定或增长\n- 替代型：结构化工作+需求固定，就业会减少\n- 大部分工作属于中间地带：需要重新设计工作流程\n\n5️⃣ **对个人的启示**\n- 需要持续学习新技能\n- 从\n\n[... middle omitted ...]\n\near vision for how the transformation is managed, including a scaled, strategic approach to upskilling and reskilling and the restructuring of career ladders.\n\nThis shift is already happening—\n\n[... middle omitted ...]\n\nease contact BCG at permissions@bcg.com. To find the latest BCG content and register to receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on Facebook and X (formerly Twitter)."
  },
  {
    "id": "R012",
    "title": "波士顿咨询：AI的“蜜月期”即将结束，战略清晰度才是分水岭",
    "digest": "[wechat_article.md]\n# 波士顿咨询：AI的“蜜月期”即将结束，战略清晰度才是分水岭\n\n2025年，波士顿咨询（BCG）的《AI at Work》报告第一次揭示了一个让许多管理者意外的现象：员工用AI省下的时间，并没有自动转化为战略价值。一年后，2026年的报告给出了更尖锐的判断——这个问题不仅没有解决，反而在恶化。\n\n这份基于全球11,749名受访者的最新调研，核心发现可以浓缩为一句话：**AI的普及已经跨过“硅天花板”，但组织的管理能力远未跟上。** 如果企业继续把AI当作工具来部署，而不是当作工作方式来重构，那么省下的时间越多，浪费的机会成本也越大。\n\n更值得警惕的是，报告揭示了一个“甜蜜陷阱”：员工在初次接触AI时会因为认知新鲜感而享受工作，但这种愉悦感会在6-12个月内消退。唯一能够维持长期员工满意度和业务价值的，不是更先进的模型，而是来自高层的战略清晰度。\n\n这不是一份关于技术趋势的报告，而是一份关于管理短板的诊断书。以下是我们从这份报告中提炼出的五个核心洞察。\n\n> **KC评论：** 这份报告最反常识的发现是：拥有明确AI战略但工具受限的员工，其产出结果反而优于拥有顶级工具但缺乏方向指引的员工。这意味着，在AI时代，“做什么”比“用什么做”重要得多。完整报告中对这一结论的量化拆解，值得每一位高管仔细阅读。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 一线员工已全面拥抱AI，但管理层尚未准备好迎接这一现实\n\n2026年，74%的一线员工已成为AI的常规使用者，相比2025年大幅上升了23个百分点。印度和中东地区领跑，而美国、法国和意大利则落后于平均水平。\n\n这一数据打破了此前一个流行的担忧——“硅天花板”，即技术精英与普通员工之间的AI使用鸿沟。事实上，一线员工在AI采纳上已经追平甚至超越了部分中层管理者。支持性职能部门（如法\n\n[... middle omitted ...]\n\n图表、投行观点和实战案例，帮助你避免“蜜月期”后的管理困境。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI省下时间，然后呢？\n\n省下的时间去哪了\n\nBCG最新调研：42%的AI用户每周省出整整一天，但66%的人没收到任何时间再分配指导，超半数人没把时间用回战略工作上。\n\n1/ 一线员工AI渗透率达74%\n比去年飙升23个百分点。印度和中东领跑，美国、法国、意大利反而落后。支持部门普及最快，销售和运营还在追赶。\n\n2/ 真正的瓶颈在管理和组织\n72%的人说技能要求变了，近半数岗位从“做事”转向“管理AI做事”。省时间≠创造价值，关键在怎么重新设计工作流。\n\n3/ 商业价值和员工快乐不矛盾\n67%的AI用户更享受工作。那些商业价值抓得好的公司，员工幸福感也最高。核心杠杆：战略清晰度、流程再设计、技能投资。\n\n4/ AI蜜月期会结束\n刚开始的新鲜感和认知挑战让人兴奋。但持续快乐来自战略清晰——CEO亲自站台、方向明确、信息传达到一线。\n\n5/ AI Agent从概念到落地\n工作流集成度比去年翻倍，61%的人认为3年内Agent能完成自己一半工作。但治理框架严重滞后，半数人表示公司没建立人×AI团队的管理规则。\n\nCEO五大行动：亲自定战略、改衡量指标（别只看使用率）、重新设计端到端流程、把人放进设计里、把治理当动态\n\n[... middle omitted ...]\n\nrway, and Finland. Middle East includes UAE, Saudi Arabia, Kuwait, and Qatar. Benelux includes Belgium and the Netherlands.\n\n## New findings reinforce trends observed in 2025\n\n![](images/828ab\n\n[... middle omitted ...]\n\nmething you keep steering, not a program with a finish line. Put a light, standing governance in place that rechecks what works, remeasures the value, and adjusts as the models and agents evolve.\n\n## BCG X | BCG\n\nbcg.com"
  },
  {
    "id": "R013",
    "title": "波士顿咨询：CEO用AI的真正红利，不是效率，是判断力",
    "digest": "[wechat_article.md]\n# 波士顿咨询：CEO用AI的真正红利，不是效率，是判断力\n\n当一家公司谈论AI转型时，最诚实的信号不是它的战略文件，而是CEO本人如何使用AI。波士顿咨询在2026年6月发布的一份面向CEO群体的研究报告，提出了一个正在被多数企业忽视的核心判断：AI目前主要被部署在组织中下层，用于优化流程和提升生产率，但真正的价值前沿在顶层——在那里，CEO和核心团队的判断力是公司最稀缺、最昂贵的资源。\n\n这份报告的数据揭示了一个鲜明的反差：72%的CEO现在直接负责公司内部的AI决策，但只有15%正在从中产生有意义的商业价值。造成这一差距的关键变量，不是技术投入的规模，而是CEO个人是否愿意每周至少投入8小时去“自建”AI能力。不是把AI交给CIO或CDO，而是自己动手，亲自使用，亲自感受边界。\n\n这意味着什么？意味着AI在CEO层面的价值，不是靠“部署”完成的，而是靠“使用”完成的。而使用的目标，不是更快地完成任务，而是做出更好的判断。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 15%的领先者与72%的责任者之间，隔着一个“亲自用”的距离\n\n波士顿咨询的调研结果值得所有企业决策者反复琢磨。七成以上的CEO已经把自己放在了AI决策的第一责任人位置上，但真正跑出价值的只有不到两成。这种落差不能用技术成熟度来解释，因为所有公司面对的技术供给是一样的。\n\n报告给出的解释直指一个管理痛点：多数CEO把AI当作一个“需要管理的项目”，而不是一个“需要亲自使用的工具”。他们批准预算、任命负责人、听取汇报，但自己不碰。而那些创造价值的15%，恰恰是那些每周花至少8小时自己使用AI的CEO。他们用AI快速学习新领域、准备关键对话、压缩复杂信息、压力测试自己的判断、优化表达方式，甚至用它来复盘自己的时间分配是否匹配战略优先级。\n\n这不是一个技术问\n\n[... middle omitted ...]\n\n合集。既方便喂给AI做二次分析，也方便人工快速把握市场动态。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nCEO用AI，决定了公司AI转型成败\n\n**CEO的AI实验**\n\n**用好AI，是CEO自己的事**\n\n---\n\n某外资投行最新研报发现：72%的CEO直接负责公司AI决策，但只有15%真正从AI中获得了价值。\n\n差距在哪？不是战略，而是CEO自己怎么用AI。\n\n那些跑得快的CEO，每周至少花8小时亲自用AI，不是甩给团队。\n\n他们主要做这6件事：\n\n1️⃣ **快速上手新领域**\n把AI当私人导师，快速建立陌生领域的知识框架，准备高难度对话。\n\n2️⃣ **当辩论对手**\n让AI挑战自己的假设、给概率、指出风险——那些人类顾问不好意思说或没看到的问题。\n\n3️⃣ **把模糊想法变清晰**\n用AI把粗糙思路写成股东信、梳理表达逻辑。甚至让AI回顾日历和邮件，看自己时间分配和优先级是否一致。\n\n4️⃣ **压缩信息，提炼要点**\n开会前让AI整合矛盾的备忘录、暴露权衡、标记风险。目标是“进会议室时已经准备好决策，而不是等着被 briefing”。\n\n5️⃣ **做情景推演**\n用AI模拟与不同利益相关者的对话走向，提前预警业务中断信号。\n\n6️⃣ **发现被忽略的声音**\nAI能放大那些可能永远到不了CEO案\n\n[... middle omitted ...]\n\nnior team may be reluctant to raise, and manage their schedules more strategically.\n\nWhile early AI use cases like these confer real benefits for an organization by expanding a CEO's understan\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R014",
    "title": "波士顿咨询：快消与零售的AI竞赛，赢家不是技术最强者",
    "digest": "[wechat_article.md]\n# 波士顿咨询：快消与零售的AI竞赛，赢家不是技术最强者\n\n消费品和零售行业正在经历一场由AI驱动的竞争格局重塑，但波士顿咨询与消费品论坛联合发布的最新报告揭示了一个反直觉的判断：当前行业的AI竞赛，决定胜负的不是技术能力，而是战略聚焦能力。报告调查了39位全球CPG和零售高管，发现75%的CPG企业仍停留在试点探索阶段，而零售行业则呈现出明显的两极分化——45%的企业已实现规模化影响，但另有40%几乎尚未起步。这种分化背后，是赢家与追赶者之间一套截然不同的决策逻辑。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 规模化AI应用的真正瓶颈不在技术，而在战略聚焦\n\n大多数CPG企业陷入了所谓的“试点陷阱”。波士顿咨询的报告显示，约四分之三的受访企业仍处于试点和探索模式，只有18%实现了规模化影响。问题不在于技术方案不够成熟，而在于这些企业未能将AI活动与核心商业优先级对齐。\n\n报告指出一个关键矛盾：近半数CPG受访者将“从创意到上市”视为最具战略意义的流程，但只有11%在创新领域部署了AI。零售商也呈现类似模式：46%认为“从选品到品类规划”最重要，但仅有34%在该领域实现了AI规模化。\n\n赢家的做法是“先收窄再加速”。他们不会同时铺开几十个AI试点，而是将AI集中在少数几个企业选择要赢的核心商业流程上——更快的创新、更精准的需求感知、更好的货架可得性或更相关的品类规划。这种聚焦本身就是一个战略决策，它要求CEO和领导团队有勇气说“不”。\n\n> **KC评论：** 这份报告揭示了一个行业通病：AI活动与战略重点的错位。许多企业忙于追逐AI的热点应用，却忽视了最需要AI赋能的战略环节。如果你正在评估企业的AI投资组合，不妨先问自己：我们的AI项目是在解决最重要的问题，还是在做最容易做的事？完整报告中的Exhibit 5提供了\n\n[... middle omitted ...]\n\n详细图表、案例分析和落地框架，这些在本文中只能呈现冰山一角。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI在快消零售的真实战况\n\nAI落地，谁在赚钱？\n\n赢家的逻辑：先聚焦，再加速\n\n最近读了一份BCG和CGF的联合研报，讲AI在CPG（快消）和零售业的应用现状。信息密度很高，挑几个有意思的点分享👇\n\n1️⃣ **大部分公司还卡在试点阶段**\n- 约75%的CPG公司仍在探索和试水，只有18%真正规模化落地\n- 零售业两极分化：45%在规模化，40%几乎没开始\n- 差距不是技术，而是“怎么把试点跑通到全链路”\n\n2️⃣ **赢家不贪多，先聚焦核心流程**\n- 很多公司AI活动分散，跟战略重点不匹配\n- 比如近一半CPG公司说“从创意到上市”最重要，但只有11%在创新环节部署了AI\n- 头部玩家做法：先砍掉一堆项目，集中火力在1-2个核心商业流程（如需求预测、补货优化）\n\n3️⃣ **价值池真的不小**\n- 如果全链路规模化，CPG公司EBIT可提升220-350个基点，零售商180-360个基点\n- 未来随着AI从“副驾驶”走向“自动驾驶”，机会可能再扩大1.7倍\n- 但前提是：得先解决测量问题——超过一半公司根本没正式衡量AI投资ROI\n\n4️⃣ **从copilot到autopilot是分水岭**\n- 6\n\n[... middle omitted ...]\n\ned in over 60 years of deep domain knowledge, to ensure leaders make the right choices. We combine it with applied AI, shaped and wielded by our practitioners, teaming shoulder-to-shoulder wit\n\n[... middle omitted ...]\n\nsit bcg.com. Follow Boston Consulting Group on LinkedIn, Instagram, Facebook, and X.\n\n© Boston Consulting Group 2026. All rights reserved.\n\n![](images/393cf78540024fd65398c9dc43a8044708373b99b3ce606ce1793ce362eb210b.jpg)"
  },
  {
    "id": "R015",
    "title": "波士顿咨询：AI转型的瓶颈不是技术，是团队有没有被允许重新设计工作",
    "digest": "[wechat_article.md]\n# 波士顿咨询：AI转型的瓶颈不是技术，是团队有没有被允许重新设计工作\n\n当一家市值千亿的零售企业将AI工具分发到每个工程师手中，结果却发现代码部署效率几乎没有提升时，它意识到一个比技术更棘手的问题：团队不知道如何用这些工具重新思考自己的工作方式。\n\n这不是个例。波士顿咨询在2026年6月发布的一份深度报告揭示了一个正在被大量企业忽视的真相。报告指出，生成式AI在三年内已达到70%的企业采用率，但只有16%的澳大利亚高管报告说他们从GenAI中获得了显著价值。这个巨大的落差，正在成为董事会和管理层最焦虑的议题。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n![研报图表 2](assets/xhs_card_02.png)\n\n![研报图表 3](assets/xhs_card_03.png)\n\n这份来自波士顿咨询的报告，由前Woolworths集团首席人力官与BCG多位合伙人联合撰写，提出了一个核心判断：Agentic AI（智能体AI）正在从根本上改变组织变革的方式，而大多数企业的变革逻辑还停留在上一个时代。真正获得价值的组织，不是那些拥有最好技术的，而是那些让团队深度参与重新设计自身工作流程的。\n\n> **KC评论：** 波士顿咨询的这份报告没有把重点放在AI技术选型或架构上，而是聚焦在“组织能力”这个更软、却更关键的变量上。对于正在推动AI落地的决策者来说，这意味着需要把注意力从“如何买工具”转向“如何让团队愿意且有能力使用工具”。完整报告里包含了AWS软件开发生命周期转型的详细案例，以及一个五步执行清单，这些实操细节是这篇文章无法完全展开的。\n\n### 1. 五个结构性变化正在让传统变革模式失效\n\n波士顿咨询的报告识别出五个正在改变组织变革逻辑的结构性变化，它们共同指向一个结论：传统的中央集权式、分阶段推进的转型模式，在Ag\n\n[... middle omitted ...]\n\n据图表合集，既方便喂给AI，也方便人工快速把握市场动态。**\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI转型的瓶颈不是技术，是团队\n\n**团队驱动的AI变革**\n\n别让技术成为你公司AI转型的唯一焦点\n\n最近读了一份BCG的研报，核心观点很直接：AI转型的瓶颈已经从技术转移到了组织能力。真正拿到价值的公司，不是技术最强的，而是能让团队重新设计工作方式的。\n\n1/ **5个结构性变化**\n- 工作变化太快，中央项目根本追不上（AI能力每周都在进化）\n- 创新开始自下而上，团队自己就能用AI工具\n- 转型不再靠几个大项目，而是靠成百上千个小改进\n- 团队成了变革的发动机，领导要做的只是引导方向\n- 每个团队都在实时重新定义自己的角色\n\n2/ **AWS的实战案例**\nAWS用GenAI重塑软件开发流程，不是简单发工具，而是：\n- 把AI采用和业务结果直接挂钩（代码是否真正上线）\n- 让有经验的同事嵌入团队，示范新工作方式\n- 聚焦全生命周期，不只看编码环节\n- 结果：功能交付量提升27%\n\n3/ **给团队的5个检查项**\n- 先想清楚AI到底服务哪个战略目标，别为了用AI而用AI\n- 让CHRO主导AI议程，组织设计比技术部署更重要\n- 关注“高质量采用”，不是“有权限使用”\n- 把转型和日常运营分开，给团队\n\n[... middle omitted ...]\n\ncross Australian retail. She reflects here on perspectives drawn from that journey, including conversations with other senior People leaders. Gavin Parker is a Managing Director and Senior Par\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R016",
    "title": "波士顿咨询：农业的“氮时刻”重演，但这次赢家不是化肥厂",
    "digest": "[wechat_article.md]\n# 波士顿咨询：农业的“氮时刻”重演，但这次赢家不是化肥厂\n\n1898年，英国科学家威廉·克鲁克斯爵士发出警告：地球的氮肥即将耗尽，除非能从空气中合成氮，否则饥荒将不可避免。十一年后，哈伯-博世法诞生，人类突破了自然的硬约束。此后一个多世纪，种子革命、机械化、化学投入品层层叠加，重塑了全球食物体系。今天，全球农业养活的人口是当时的五倍。\n\n但波士顿咨询（BCG）在2025年6月发布的一份报告中指出，农业正面临三重结构性威胁：气候波动、地缘政治重组、以及监管范式迁移。而一个正在加速的第四股力量——农业智能（Agricultural Intelligence）——既是应对这些威胁的手段，也是新一轮价值重分配的开始。\n\n今天，这份报告的核心判断是：AI正在侵蚀农业价值链中几乎所有基于信息不对称和专业知识溢价建立的竞争壁垒。赢家不会是那些把AI当“功能”加上去的公司，而是那些敢于重新定义自己商业模式的企业。就像哈伯-博世法没有拯救化肥厂，而是催生了整个现代农业体系一样，农业智能的窗口已经打开，但它不会一直敞开。\n\n> **KC评论：** 报告的标题很直接——“农业智能如何重塑全球食物体系”。但它的真正判断是：AI不只是让农业更精准，而是让过去几十年农业公司赖以赚钱的“我知道你不知道”的模式失效。这意味着，从种子公司到贸易商，从农机厂到食品零售商，几乎所有玩家的护城河都需要重新审视。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 三重威胁正在迫使农业从“靠天吃饭”转向“靠数据吃饭”\n\nBCG指出，全球农业食物体系正承受三重压力的叠加。第一是气候波动。降水、温度、季节变化这三个农业的基础输入，正在从“可靠的前提”变成“系统性的风险源”。当天气不再是可预测的常数，农业就需要更精细的监测和更快速的响应。\n\n第二是地缘政治重组。中美关税的\n\n[... middle omitted ...]\n\n可能成为新的赢家，欢迎加入社群，领取完整研报解读与原始图表。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI正在吃掉农业，但农民可能赢最大\n\n农业正在被AI重写\n\n某外资投行最新研报指出：AI在农业的价值链上，正在压缩三类人的利润空间，同时让另一群人拿到主动权。\n\n1️⃣ 三个威胁，一个机会\n- 气候波动：降雨、温度、季节变得不可预测\n- 地缘重组：供应链冲击已成常态，谁先读信号谁赢\n- 监管转型：欧盟要求可验证的产地数据，农业从未有过这种数据基础设施\n\n2️⃣ AI的四个能力维度\n- 感知：把物理世界变成数据——卫星、无人机、传感器，成本比十年前低太多\n- 决策：把数据变成建议——FarmerChat已覆盖83万农民，每次咨询从35美元降到35美分\n- 行动：不用人干预——John Deere的See & Spray能识别杂草，用药量减半，2025年覆盖500万英亩\n- 创造：设计新种子和新分子——Bayer用AI开发了首个除草剂，不再筛几万个化合物\n\n3️⃣ 谁会被重塑？\n- 农资零售商：靠关系卖产品的模式要变，AI会透明比价\n- 农机厂商：硬件壁垒正在被AI软件替代\n- 贸易商：信息不对称的优势在压缩，卫星+AI让谁有粮一目了然\n- 农民：最危险也最有机会——他们手握数据，现在可以直接用AI工具理解数据价\n\n[... middle omitted ...]\n\neiling; after that, its decline would be simple arithmetic. His appeal was direct: unless chemistry could produce nitrogen from the atmosphere itself, mass starvation would follow.\n\nEleven yea\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R017",
    "title": "波士顿咨询：CEO亲自下场，AI投资翻倍但真正的分化才刚刚开始",
    "digest": "[wechat_article.md]\n# 波士顿咨询：CEO亲自下场，AI投资翻倍但真正的分化才刚刚开始\n\n2025年，全球企业AI投资占营收比例翻倍至1.7%。这组来自波士顿咨询（BCG）最新AI雷达报告的数据，本身并不令人意外。真正值得关注的判断是：企业AI转型的主导权，正在从CIO办公室转移到CEO办公室，这一权力转移将从根本上改变AI投资的逻辑、节奏和胜败格局。\n\nBCG在2026年AI雷达报告中调查了2360位全球企业高管，其中640位是CEO。结论清晰：72%的CEO表示自己是所在组织AI决策的第一责任人，这一比例是去年的两倍。更关键的是，50%的CEO认为自己的职位稳定性取决于能否把AI战略做对。\n\n这不是一个关于技术选择的报告，而是一个关于组织权力、战略决心和资本配置的报告。对于那些还在把AI当作IT项目来管理的企业，这份报告释放了一个明确的信号：窗口期正在关闭。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 94%的企业不会因短期回报不达预期而削减AI投资，这轮投入具有刚性\n\nBCG报告中最反直觉的数据是：94%的受访企业表示，即使AI投资在2026年没有产生预期的财务回报，他们仍将继续投入。只有6%的企业计划在短期效果不理想时撤回投资。\n\n这一数据打破了过去企业数字化转型中常见的“试点-观望-收缩”循环。当AI投资从CIO的预算项目变成CEO的战略承诺，退出成本就不再是财务上的沉没成本，而是组织层面的战略失信。\n\n从投资强度看，2026年全球企业AI投资占营收比例预计达到1.7%，较2025年翻倍。横向看，所有行业都在加码。金融和科技行业依然领先，但工业和消费品行业的增速更快。这意味着，AI投入不再是少数领先者的差异化动作，而是全行业的基准配置。\n\n> **KC评论：** 1.7%的营收占比看似不高，但考虑到全球企业营收基数，这是一笔极其\n\n[... middle omitted ...]\n\n要与KC评论，约10-40页，既方便喂给AI，也方便人工快速把握市场动态。如果你希望获取BCG这份报告的完整图表和更细致的行业拆解，可以加入社群，每天收到更新，与同样关注AI转型的决策者一起讨论。\n\n---\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nCEO亲自上阵，AI投资翻倍\n\nAI投资翻倍，CEO亲自带队\n\nBCG 2026 AI雷达报告出炉，核心发现很直接：AI投资不再是IT部门的事，CEO们已经亲自下场了。\n\n1️⃣ **投资翻倍，不达预期也不停**\n- 2026年企业AI投资预计翻倍，占营收比例升至1.7%\n- 94%的CEO表示，即使2026年没有看到回报，也会继续投\n- 只有6%的企业会因短期效果不佳而缩减AI预算\n\n2️⃣ **AI转型从CIO主导变为CEO主导**\n- 72%的CEO表示自己是组织内AI决策的第一责任人，是去年的2倍\n- 50%的CEO认为，自己的职位稳定性取决于AI战略是否做对\n- 82%的CEO比去年更看好AI的投资回报潜力\n\n3️⃣ **三种CEO类型，只有15%是“拓荒者”**\n- 拓荒者型（15%）：果断投资、快速培训、全链条推进，60%的AI预算花在智能体上\n- 务实者型（70%）：有信心但只投看得见回报的\n- 跟随者型（15%）：有意识但缺信念，投资谨慎\n- 拓荒者投入员工AI培训的费用是务实者的2倍多，已有70%的员工完成AI技能提升\n\n4️⃣ **智能体AI成为新焦点**\n- 90%的CEO认为智能体A\n\n[... middle omitted ...]\n\nfbc3.jpg)\n\n## Key takeaways\n\n1\n\nCorporate investments in AI have doubled since last year and are here to stay\n\n94%\n\nof CEOs say they will continue to invest even if it does not pay off in 2026\n\n[... middle omitted ...]\n\n2%\n\nof CEOs say they are the main decision maker on AI, 2x last year\n\n50%\n\nof CEOs believe their job depends on getting AI right\n\n90%\n\nof CEOs believe AI agents will enable their companies to see measurable ROI this year"
  },
  {
    "id": "R018",
    "title": "波士顿咨询：印度BFSI的网络安全缺口正在加速扩大，AI攻击者已领先12-18个月",
    "digest": "[wechat_article.md]\n# 波士顿咨询：印度BFSI的网络安全缺口正在加速扩大，AI攻击者已领先12-18个月\n\n这份报告来自波士顿咨询（BCG）与印度数据安全委员会（DSCI）的联合调研，核心判断只有一个：印度金融业的网络安全防线正在被AI加速撕开，而且这个缺口还在以季度为单位扩大。\n\n报告的数据触目惊心。印度BFSI（银行、金融服务与保险）遭受的网络攻击强度是全球平均水平的1.6倍。网络安全事件从2021年的140万起翻倍到2025年的290万起。数据泄露的平均成本以每年7%的速度攀升，达到250万美元。而更令人不安的是，从发现到控制一次数据泄露的平均时间长达263天——比全球平均水平还要多出22天。\n\n但真正让这份报告值得认真研读的，不是这些数字本身，而是波士顿咨询提出的一个根本性判断：AI已经彻底改写了网络攻击的经济学。攻击者的时间成本被压缩了94%，攻击成本下降了70%以上。这意味着，过去只有国家级行为体或顶级黑客组织才能发动的攻击，现在几乎任何有动机的对手都能以极低成本实现。\n\n这不仅仅是威胁升级。这是一场结构性不对称的重新洗牌。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 攻击者的速度已经超过防御者的响应周期，这是体系性问题而非技术缺口\n\n波士顿咨询的数据显示，AI工具将一次攻击从策划到利用的时间窗口从745天压缩到了44天。而印度BFSI机构平均需要263天才能识别并控制一次数据泄露。\n\n这个数字对比本身就说明了一切。当攻击者以天为单位行动时，防御者仍然以月为单位响应。这不是某个安全产品配置不当的问题，而是整个安全运营体系的节奏已经跟不上对手。\n\n报告特别指出，印度BFSI中76%的CISO将AI驱动的攻击列为2026年的前四大优先事项，69%的人认为AI威胁将在12个月内产生重大影响。但与之形成鲜明对比的是，调查中没有任何一\n\n[... middle omitted ...]\n\n集。既方便喂给AI进行二次分析，也方便人工快速把握市场动态。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n印度BFSI正在经历一场AI驱动的安全拐点\n\n**攻防速度已反转**\n\n76%的印度BFSI安全负责人把AI攻击列为前三优先级，69%认为12个月内会显著受影响。但没有任何一个安全控制领域，对AI攻击的防御自信度超过50%。\n\n---\n\n**1/ 攻击者已领先一个身位**\n\nAI把攻击成本砍了70%+，漏洞利用窗口从745天压缩到44天（-94%）。印度BFSI遭受的攻击强度是全球平均的1.6倍，安全事件4年翻了一倍（140万→290万起）。\n\n最危险的是中腰部机构——数字化做得快、数据有价值、深度互联，但安全预算只有大玩家的零头。\n\n**2/ 防御端还没跟上**\n\n71%的印度BFSI已经部署了AI辅助安全运营中心，但只有38%把IT预算的10%以上投给安全——全球这个比例是76%。\n\n43%的CISO说攻击者已经跑得比防御快，但只有19%的机构因此大幅增加安全预算。\n\n**3/ 三个关键缺口**\n\n- **投资有空间**：60%+的印度BFSI安全支出不到IT预算的10%\n- **第三方风险治理不足**：55%认为是头号风险，但只有49%有成熟管控\n- **AI治理滞后**：仅29%同时有AI安全负责人和\n\n[... middle omitted ...]\n\nal expertise and a range of perspectives that question the status quo and spark change. BCG delivers solutions through leading-edge management consulting, technology and design, and corporate \n\n[... middle omitted ...]\n\n or electronic media without permission. Any reproduction, distribution, or reuse of this material requires prior consent from DSCI and, where applicable, Boston Consulting Group.\n\n## BCG | DSCI PROMOTING DATA PROTECTION"
  },
  {
    "id": "R019",
    "title": "波士顿咨询：欧洲消费者削减的不是预算，是品牌忠诚度",
    "digest": "[wechat_article.md]\n# 波士顿咨询：欧洲消费者削减的不是预算，是品牌忠诚度\n\n欧洲消费者的钱包正在收紧，但这份来自波士顿咨询（BCG）的2026年消费者调研揭示了一个更深层的信号：消费者削减的不是花销本身，而是对品牌的忠诚。超过六成的欧洲消费者表示愿意为更好的价格更换品牌，44%的人在最近一次购买中已经转向了一个他们从未买过的品牌。这不是一次简单的消费降级，而是一次结构性的消费行为重塑——价格成为唯一的信息，健康成为新的刚需，而品牌曾经的护城河正在被折扣和社交媒体同时瓦解。\n\n这份基于对11个欧洲国家超过20000名消费者的年度调研，在2026年4月完成。它告诉我们，消费者悲观情绪仍在加深——对经济感到悲观的消费者比例从2025年的54%上升至56%。但真正值得关注的不是情绪本身，而是情绪如何转化为行为，以及这些行为对产业格局意味着什么。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 金融压力已成为欧洲消费者的默认状态，而非偶发事件\n\n超过半数的欧洲消费者（53%）表示对日常个人财务状况感到担忧，这一比例较2024年的40%大幅上升。六成消费者担心退休后资金不足。这些数字背后是一个更关键的判断：消费者已经将“财务紧张”内化为一种常态化的生活状态，而非等待经济好转的临时反应。\n\nBCG的调研设计了一个巧妙的思想实验：如果消费者突然获得10%到15%的额外收入，他们会做什么？近半数受访者的首选是增加储蓄，而非消费。这意味着，即便经济出现边际改善，消费反弹的力度也可能远低于市场预期。消费者的第一反应是修补资产负债表，而不是打开钱包。\n\n> **KC评论：** 这张图的价值在于它推翻了“压抑需求终将释放”的乐观假设。完整报告中包含按国家和年龄组细分的储蓄意愿数据，这些细节对于判断不同品类的复苏时序至关重要。一位德国中年消费者和一位西班牙年轻消费者的\n\n[... middle omitted ...]\n\n重塑的当下，这些第一手的调研数据可能是你做出正确判断的基础。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n欧洲人正在偷偷“省”掉什么\n\n消费降级？不，是结构变了\n\n最近读了一份欧洲消费者调研，数据挺有意思，分享几个关键发现👇\n\n1️⃣ 消费转向“刚需”和“健康”\n过去6个月，只有食品杂货和宠物用品是正增长，且主要是涨价拉动的。其他品类都在缩，尤其是时尚、酒类、零食。\n\n2️⃣ 健康成了新“硬通货”\n66%的人把健康放在极重要位置。46%在少喝酒或考虑少喝。功能零食、补剂在涨，而巧克力、冰淇淋这类纯享受品在跌。\n\n3️⃣ 代际差异比收入更大\n年轻人（Z世代+千禧一代）净支出只降2个点，但X世代和婴儿潮一代降了13个点。年轻人还在买家具、时尚，但更爱二手、更不认品牌。\n\n4️⃣ 折扣才是第一购买力\n63%的人只买打折或主动找优惠。62%愿意为更好价格换品牌。品牌忠诚？排第五。折扣和店内陈列才是转化关键。\n\n5️⃣ 可持续性在退潮\n考虑可持续因素的比例在降，但17%的人愿意为绿色溢价。二手市场增长，更多是省钱驱动，不是环保。\n\n6️⃣ 社交+AI正在抢搜索的饭碗\n社交平台（尤其ins、tiktok）成为年轻人发现产品的主要渠道。ChatGPT这类工具在产品发现上的使用量一年翻4倍，传统搜索在缩。\n\n7️⃣ GLP-1药\n\n[... middle omitted ...]\n\nare impacting them. Consumers also show growing pessimism about politics and their personal finances. (See Exhibit 1.)\n\nEconomic situation\n\nSources: 2026 BCG European Consumer Sentiment Survey\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R020",
    "title": "波士顿咨询：金融科技只啃下3%的蛋糕，但赢家已不是初创公司",
    "digest": "[wechat_article.md]\n# 波士顿咨询：金融科技只啃下3%的蛋糕，但赢家已不是初创公司\n\n全球金融科技行业正在经历一场静默的“成年礼”。波士顿咨询（BCG）与QED Investors联合发布的《2025全球金融科技报告》给出了一个既令人振奋又充满挑战的核心判断：行业基本面已经显著改善，但未来的竞争逻辑与过去十年截然不同。\n\n2024年，全球金融科技收入同比增长21%，远超2023年的13%和传统金融服务业整体的6%。公开市场金融科技公司的平均EBITDA利润率提升了25%，达到16%，69%的公开金融科技公司实现盈利。这些数字指向一个明确的信号：行业已经走出了“烧钱换增长”的青春期，进入了“可持续增长”的成熟阶段。\n\n但这份报告最有价值的洞察，不在于行业复苏本身，而在于它对“谁在赢、赢在哪里、下一轮机会在哪”的冷静拆解。金融科技仅渗透了全球银行与保险收入池的3%，渗透率分布如同瑞士奶酪——某些区域密集，但绝大多数地方仍是空白。而真正值得关注的，是那些已经跑出来的“规模化赢家”将如何定义下一个十年的竞争规则。\n\n> **KC评论：** 这份报告最反常识的一点是，它并不认为金融科技的下一章属于更多的新创公司。相反，它指出，未来将是少数“规模化赢家”与“新兴颠覆者”之间的博弈。对于投资者和产业决策者而言，理解这两类玩家的边界在哪里，比追逐下一个热点更重要。完整报告中对“赢家”的财务特征和扩张路径有更细致的拆解，这是无法在一篇导读中完全展开的。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 全球只有不到100家金融科技公司算得上“规模化赢家”，它们贡献了60%的收入\n\n波士顿咨询将“规模化金融科技”定义为年收入超过5亿美元的公司。在全世界约3.7万家金融科技公司中，达到这一门槛的不足100家。但这不到0.3%的群体，在2024年创造了约2310亿美元\n\n[... middle omitted ...]\n\n的内容感兴趣，欢迎加入社群，领取完整研报解读与原始图表。**\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n金融科技的下一个章节，赢家已浮现\n\n赢家与新兴颠覆者\n\n全球金融科技在2024年交出了一份扎实的成绩单。某外资投行与QED联合发布的报告显示，行业收入增长21%，达到3780亿美元，其中年收入超5亿美元的“规模化赢家”贡献了约60%。这些赢家集中在五个领域：数字钱包、收单与垂直SaaS、挑战者银行、加密货币交易和BNPL。\n\n1/ 渗透率只有3%，像瑞士奶酪一样有洞\n金融科技只渗透了全球银行与保险收入池的3%，增长却是传统机构的3倍。赢家之所以赢，是因为它们精准攻入了银行“不擅长、不愿意、不敢去”的领域——比如为低收入人群提供银行服务，或切入加密货币等监管禁区。\n\n2/ 从“增长不惜代价”到“可持续盈利”\n2024年，69%的上市金融科技公司实现盈利，平均EBITDA利润率提升25%至16%。资本市场的估值逻辑也变了：未来收入增长和盈利能力解释了50%的估值差异，规模和研发支出紧随其后。IPO窗口虽然因宏观波动暂时冻结，但全球有150家2016年前成立的金融科技公司手握超5亿美元融资仍未上市，它们正等待时机。\n\n3/ 未来增长靠B2B、基础设施和AI\n报告预测，下一阶段增长将由B2B（2倍于消费端）、金融基础\n\n[... middle omitted ...]\n\nintech revenues grew robustly at 21% in 2024 (versus 13% in 2023), driven by impressive results from challenger banks and trading and investment fintechs.\n\n\\$231B\n\nTotal revenue generated by f\n\n[... middle omitted ...]\n\n on this topic or others, please visit bcg.com. Follow Boston Consulting Group on LinkedIn, Facebook, and X (formerly Twitter).\n\n![](images/27f9d78a9536dc10c6c75dfedb67be7e70469e8a8f3a4ffe9bd4a4e55f1bc488.jpg)\n\nBCG + QED"
  },
  {
    "id": "R021",
    "title": "波士顿咨询：金融科技进入“精选式复苏”，规模不再自动等于护城河",
    "digest": "[wechat_article.md]\n# 波士顿咨询：金融科技进入“精选式复苏”，规模不再自动等于护城河\n\n金融科技行业正在经历一场“无声的升级”。2025年，全球金融科技总收入突破5000亿美元，同比增长22%，增速是传统金融机构的四倍以上。但这份来自波士顿咨询（BCG）与FT Partners联合发布的《2026全球金融科技报告》传递的核心信号，并非简单的“行业回暖”。\n\n真正值得关注的判断是：这轮增长不是普惠性的水涨船高，而是一场高度分化的“精选式复苏”。资本回来了，但只愿意流向那些已经证明自己能够将规模转化为利润、将技术转化为运营效率的公司。行业已经从“证明自己属于这里”的阶段，进入“证明自己能持续创造价值”的阶段。\n\n这份报告对产业决策者的意义在于：它系统性地拆解了金融科技进入新竞争周期的底层逻辑，并给出了七个塑造未来格局的趋势框架。以下是我们从中提炼的核心洞察。\n\n> **KC评论：** 报告最值得先看的一张图是“全球金融科技营收分布”。你会发现，支付依然是绝对主力，但增速最快的是交易与投资（38%）以及存款（30%）。这意味着行业的增长引擎正在从“管道型”业务转向“资产型”业务，这对估值逻辑和竞争壁垒都有根本性影响。完整报告里还附带了按地区、按垂直领域的详细拆解图，值得仔细对照。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 这轮复苏的真正驱动力不是资本回流，而是运营效率的质变\n\n报告中最具说服力的数据来自公开金融科技公司的利润表。2025年，全球最大的85家上市金融科技公司平均EBITDA利润率提升了4个百分点至20%，盈利公司占比从68%上升至74%。同时，达到“40法则”（营收增速+利润率之和超过40%）的公司比例也从2024年的约三分之一提升至2025年的接近一半。\n\n这些数字说明，行业已经走出了“烧钱换增长”的粗放阶段。资本流入确实在\n\n[... middle omitted ...]\n\n，帮你持续跟踪金融科技、数字资产与全球金融市场的结构性变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球金融科技，真的回来了\n\n2026全球金融科技全景\n\n复苏不是反弹，是结构性升级\n\n📊 全球金融科技收入2025年突破5000亿美元，同比增长22%——增速是传统金融机构的4倍以上。这不是简单的“回暖”，是行业真正站稳了。\n\n📈 几个关键信号值得关注：\n1/ 交易与投资、存款两大板块增速最快，分别达38%和30%。支付依然是最大赛道，但“赚钱能力”正在向其他领域扩散。\n2/ 全球85家头部金融科技公司中，74%已实现盈利，平均EBITDA利润率提升4个百分点至20%。资本不再盲目追增长，而是奖励“能赚钱的规模”。\n3/ 2025年金融科技IPO数量42起，同比增长50%；并购交易额达2510亿美元，比2023年翻了一倍多。\n\n🌍 区域亮点：\n- 亚太增速最快（25%），日韩的数字银行和加密平台是主要驱动力\n- 欧洲（24%）受益于更清晰的监管环境和跨境扩张\n- 巴西的Pix、印度的UPI、肯尼亚的M-PESA——金融科技正在新兴市场真正实现“普惠”\n\n🤖 关于AI：别被炒作带偏\n- 目前AI价值最明确的落地点是“运营+工作流优化”，不是颠覆性创新\n- AI原生公司与“传统公司+AI”之间存在明显的应用成熟度\n\n[... middle omitted ...]\n\n trading and investments and deposits leading the pack with about 38% and 30% YoY growth, respectively\n\n400bps\n\nAverage EBITDA margin improvement for the largest public fintechs from 2024 to 2\n\n[... middle omitted ...]\n\nbillion valuation.\n\n![](images/5208938f8aac64690ee682cdf49cfa96b3939091639a16bfe9980e8ccf39088f.jpg)\n\nBCG +\n\nFINANCIAL TECHNOLOGY PARTNERS\n\n![](images/b3e517083cc6425278ea17bb2538e0b674db9c9074c0172d5cbc3260759a241a.jpg)"
  },
  {
    "id": "R022",
    "title": "波士顿咨询：医疗科技公司的GenAI征途，成败取决于“责任AI”框架",
    "digest": "[wechat_article.md]\n# 波士顿咨询：医疗科技公司的GenAI征途，成败取决于“责任AI”框架\n\n当医疗科技公司争相将生成式AI嵌入从药物发现到患者监护的每一个环节时，一个被严重低估的风险正在浮出水面：监管的不确定性并非最大障碍，真正的分水岭在于企业能否在技术狂奔之前，先建立一套可执行的“负责任AI”框架。\n\n波士顿咨询（BCG）在2023年10月发布的白皮书中，用了一个颇具文学色彩的比喻：医疗科技公司的GenAI之旅，就像英雄踏上征途，从已知世界进入未知深渊，在那里必须应对不完整且模糊的法规、潜在的法律后果、未知的网络安全威胁，以及数据隐私和版权侵权的诱惑。而最终决定这个故事是英雄史诗还是悲剧的，不是技术能力，而是企业的“道德指南针”——也就是BCG反复强调的Responsible AI (RAI) 框架。\n\n这份报告的核心判断非常清晰：GenAI在医疗科技领域的落地，技术门槛不是最大的瓶颈，政策与治理框架的成熟度才是。那些急于推出产品、却忽视了RAI框架建设的公司，很可能在监管审查、患者安全或知识产权诉讼中遭遇重大挫折。\n\n> **KC评论：** 这不仅仅是合规问题。BCG实际上在暗示，RAI框架将成为医疗科技公司GenAI能力的竞争壁垒。谁先建立起系统化的RAI体系，谁就能在监管博弈中占据主动权，从而获得更快的审批速度和更广的市场准入。完整报告中详细拆解了RAI框架的构建步骤和关键决策点，这些细节对于正在制定AI战略的决策者来说，是必须掌握的实操指南。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 现有风险被GenAI急剧放大，但最致命的威胁来自模型内部的“黑箱”\n\nBCG明确指出，保护健康信息泄露、虚假声明、专有数据流出和版权侵权这些风险，在传统技术环境下同样存在。但GenAI通过大型语言模型（LLM）的内部工作机制，将这些潜在风险急\n\n[... middle omitted ...]\n\n探索。\n\n如果你想深入了解BCG提出的RAI行动手册完整框架、各风险类型的详细缓解策略，以及全球主要市场的最新监管动态，欢迎加入我们的社群。每天，我们的AI agent和人工团队会从国际投行和咨询机构的最新报告中提炼精华，生成10-40页的中文摘要与解读，包含关键数据图表合集，既方便你快速把握市场动态，也便于喂给AI工具进行二次分析。在这里，我们可以继续讨论：你的公司目前处于GenAI征程的哪个阶段？RAI框架的哪个环节最让你感到棘手？\n\n[note.md]\n医疗AI的“英雄之旅”，合规是必修课\n\n医疗AI的合规指南\n\n某外资投行近期发布了一份关于医疗科技GenAI的研报，把企业部署GenAI比作“英雄之旅”。我提炼了核心逻辑，和你分享。\n\n**1. 风险不只是技术问题，更是合规红线**\nGenAI放大了传统AI的隐患：幻觉、偏见、数据泄露。尤其医疗场景，患者隐私（PHI）、算法鲁棒性、版权问题都会被放大。研报特别提到，数据投毒、模型劫持这类AI攻击是新的威胁。\n\n**2. 监管正在加速，但框架不清晰**\n- 美国：FDA的CDRH是主要监管者，但尚未出台GenAI专项规定。现有框架（如SaMD、PCCP）可作为参考。\n- 欧盟：AI法案即将落地，医疗GenAI被划为“高风险”，违规罚款可达全球营收的6%。GDPR的合规要求也会叠加。\n- 关键动作：缩小“预期用途”范围、保留“人在回路”、确保模型可解释性。\n\n**3. 低风险场景是练手的好起点**\n非临床场景（如HR、客服、财务）风险较低，适合团队先积累GenAI经验。但即使是这类应用，若涉及患者访问或客户支持，也可能被FTC盯上。\n\n**4. 建立“负责任AI”框架是企业的护城河**\n研报建议CEO亲自挂帅，任\n\n[... middle omitted ...]\n\ncompany) heeds a call to adventure in pursuit of some glorious proposition (the power of GenAI), embarking on a journey from the known world into the abyss, where they must contend with forbid\n\n[... middle omitted ...]\n\nsible fashion and avoid turning their Hero's Tale into a Tragedy.\n\n## Acknowledgments\n\nThe authors would like to thank the following for their contributions to this article: Stuart John, Tad Roselund, and Gunnar Trommer."
  },
  {
    "id": "R023",
    "title": "波士顿咨询：资管行业增长公式已失效，净流入才是新护城河",
    "digest": "[wechat_article.md]\n# 波士顿咨询：资管行业增长公式已失效，净流入才是新护城河\n\n全球资产管理行业正站在一个微妙的转折点上。147万亿美元的资产管理规模，超过30%的利润率，11%的年度增长——这些数字看起来仍然健康，但波士顿咨询（BCG）最新发布的《2026年全球资产管理报告》却发出了一个与表面繁荣截然不同的信号：行业增长的核心公式已经失效。\n\n报告的核心判断只有一个，但足够尖锐：过去十五年，市场上涨替资管公司做了大部分工作；未来，这种“搭便车”式的增长将不再可靠。超过80%的2025年收入增长来自市场升值，而非管理人的主动能力。当贝塔不再慷慨，谁还能持续捕获净流入，谁才是真正的赢家。\n\n这份报告并非危言耸听。它用大量数据证明，资管行业的成本增速已连续多年超过收入增速，利润率在2010年的水平上原地踏步。更关键的是，资本正在重新分配——流向新的地区、新的客户群体、新的产品形态，以及新的渠道“守门人”。这些结构性变化正在改写竞争规则。\n\n---\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 这轮变化真正考验的是企业能否把规模转化为议价权\n\n全球资管规模在十五年间增长了三倍，收入翻了一番，但利润率始终卡在30%左右。BCG的基准研究覆盖了管理着86万亿美元资产的98家头部机构，得出的结论是：收入年增5.1%，成本却以5.4%的速度更快爬升。负运营杠杆正在侵蚀每一分增量收入。\n\n问题出在增量资金的质量上。机构端的费率以每年3%的速度下滑，被动产品和ETF持续吞噬净流入，就连主动ETF也在以低于传统产品的费率扩张。每一美元新增资产贡献的平均管理费，都在下降。\n\n成本端同样不容乐观。投资管理本身确实存在规模效应，但技术投入正在快速膨胀——构建可扩展的AI基础设施、数据平台和数字化分销体系，这些支出正在抵消规模带来的成本优势。\n\n> **KC评论：*\n\n[... middle omitted ...]\n\n动态变化。这些未解问题的后续讨论，我们也会在社群中持续展开。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n资管行业新逻辑：增长不再靠市场\n\n增长逻辑变了\n\n某外资投行最新研报显示，2025年全球资管规模达$147万亿，但超80%的收入增长靠市场上涨驱动。更关键的变化是——钱从哪里来、流向哪里、谁在拦截。\n\n1️⃣ 零售投资者成主力\n2020-2025年，零售贡献了61%的全球资管规模增长。亚太地区年增速9%，领跑全球。产品也分化了：零售主导主动权益、固收、ETF；机构主投另类资产。\n\n2️⃣ 捕获增长更难了\n美国被动产品前10家公司拿走90%+净流入。但主动管理前10家份额从63%降到56%，竞争更分散。私募市场更集中，前50家PE在2024年募资占比37%，远高于十年均值22%。\n\n3️⃣ 规模增长≠利润增长\n15年间资管规模翻3倍，收入翻2倍，利润率却卡在30%。收入年增5.1%，成本增5.4%，负经营杠杆。费用在降，科技投入在涨，规模红利被吃掉了。\n\n4️⃣ 三个结构性机会\n- 代际转移：到2048年，美国约$124万亿将传给数字原生代，他们30%在成年早期就开始投资\n- 养老体系转型：欧洲养老金资产/GDP仅33%，荷兰2028年前要从DB转DC\n- 全球分散化：近半数投资者计划增加地域配置，欧洲、亚太、\n\n[... middle omitted ...]\n\n Source of Advantage in Asset Management\n19 Rebuilding Asset Management for an AI-First World\n25 Appendix\n29 About the Authors\n\n![](images/af9ad589acd8ad92c3f760759599cd9ba0d45fc3ded0543693462\n\n[... middle omitted ...]\n\nd register to receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on LinkedIn, Facebook, and X.\n\n![](images/b289ca9fabf62c91cf18a36dc7a4ba063c1dbc86b2cf0c1dc2636fb06ff44f71.jpg)"
  },
  {
    "id": "R024",
    "title": "波士顿咨询：资管行业增长逻辑已变，未来赢家靠的是“嵌入”而非“规模”",
    "digest": "[wechat_article.md]\n# 波士顿咨询：资管行业增长逻辑已变，未来赢家靠的是“嵌入”而非“规模”\n\n全球资产管理行业正站在一个微妙的十字路口。2025年，全行业管理资产规模（AuM）达到147万亿美元，同比增长11%，利润率维持在30%以上。从表面数字看，行业依然健康。但波士顿咨询（BCG）最新发布的《2026年全球资产管理报告》给出了一个令人不安的判断：超过80%的营收增长来自市场上涨本身，而非管理人的主动能力。这意味着，过去十五年“市场涨、资产涨、收入涨”的自动增长模式，正在失效。\n\n这份报告的核心洞察不是“行业面临挑战”这种泛泛之谈，而是指出了一个更具体、也更残酷的结构性变化：**资本正在重新分配，新的资金流向、新的客户行为、新的技术力量，正在把“捕获净流入”变成资管公司最核心的竞争能力。** 谁跟不上这个变化，即使规模再大，也可能在下一轮增长中被边缘化。\n\n我们拆解了这份长达50页的报告，提炼出几个值得产业决策者和高净值投资者认真对待的判断。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 市场上涨不再是行业增长的万能解药，净流入能力才是真正的分水岭\n\n报告最核心的发现，是行业正在经历“增长公式”的根本性转变。2025年，全球AuM增长了11%，但其中超过80%的营收增长来自市场上涨带来的资产升值，而非管理人吸引的新资金。这听起来像是老问题，但BCG用数据揭示了一个更深层的矛盾：过去15年，AuM增长了两倍，收入翻了一番，但行业的利润率始终徘徊在30%左右，几乎没有变化。\n\n原因在于，收入和成本在同步攀升，且成本增速（5.4%）甚至略快于收入增速（5.1%）。这意味着行业整体在“挣辛苦钱”——每多管理一美元资产，带来的边际收入在下降，而边际成本却没有同步下降。\n\n> **KC评论：** 许多投资者习惯用“规模增长”来衡量一家资管公司的竞争\n\n[... middle omitted ...]\n\n份报告背后的图表、假设和细分拆解感兴趣，欢迎加入我们的讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n资管行业，不能再靠市场吃饭了\n\n增长逻辑变了\n\n全球资管规模2025年达147万亿美元，增速11%。但80%以上的收入增长靠市场上涨驱动，不是靠主动管理。\n\n**1/ 零售投资者成为主角**\n2020-2025年全球资管规模增长中，零售投资者贡献了61%。亚太地区增速最快，年增9%。\n数字原生代（Gen Z）30%在成年早期就开始投资，而婴儿潮一代只有6%。\n\n**2/ 资金集中度在提升**\n美国被动基金前10家公司拿走了90%以上的净流入。\n私募股权前50家公司在2024年拿走了全球募资的37%，远高于十年均值22%。\n渠道成为新的守门人。\n\n**3/ 规模不必然带来利润**\n全球资管规模15年翻了3倍，收入翻倍，但利润率仍卡在30%左右。\n收入年增5.1%，成本却年增5.4%。技术投入在涨，管理费在降。\n\n**4/ 保险渠道是下一个蓝海**\n私人信贷与保险的匹配度很高。保险公司需要资产配置能力，资管公司需要稳定资本。\n早期布局的资管公司一旦嵌入保险公司的产品架构，很难被替换。\n\n**5/ 养老金转型带来结构性机会**\n美国DC计划已占养老金资产50%以上。欧洲大陆养老金资产/GDP仅33%，荷兰正在从DB\n\n[... middle omitted ...]\n\n Source of Advantage in Asset Management\n19 Rebuilding Asset Management for an AI-First World\n25 Appendix\n29 About the Authors\n\n![](images/af9ad589acd8ad92c3f760759599cd9ba0d45fc3ded0543693462\n\n[... middle omitted ...]\n\nd register to receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on LinkedIn, Facebook, and X.\n\n![](images/b289ca9fabf62c91cf18a36dc7a4ba063c1dbc86b2cf0c1dc2636fb06ff44f71.jpg)"
  },
  {
    "id": "R025",
    "title": "波士顿咨询：金融科技没有泡沫，只有一场必要的出清",
    "digest": "[wechat_article.md]\n# 波士顿咨询：金融科技没有泡沫，只有一场必要的出清\n\n2021年，一家公开上市的金融科技公司，估值可以达到其年收入的20倍。今天，这个数字跌到了6倍以下。超过60%的市值在不到两年内蒸发，后期融资骤降43%，CEO们的头号议题从“增长”变成了“盈利”。\n\n如果你只看这些新闻标题，很容易得出一个结论：金融科技泡沫破了。\n\n但波士顿咨询（BCG）与QED Investors联合发布的这份《Global Fintech 2023》报告，给出了一个截然不同的判断。报告的核心主张是：**金融科技行业的基本面没有变差，2022年以来的估值回调是一次必要的短期出清，而非长期趋势的逆转。** 支撑这一判断的，不是对未来的乐观想象，而是对行业收入池、客户渗透率、以及技术渗透阶段的结构性测算。\n\n这份报告值得细读，不仅因为它来自全球最顶级的咨询机构之一，更因为它提供了一个在恐慌中保持冷静的分析框架。以下是我们从报告中提炼出的五个核心洞察。\n\n> **KC评论：** 这篇报告发布在2023年5月，当时市场情绪正处于低谷。BCG的判断之所以值得重视，不是因为它喊“抄底”，而是因为它用数据和逻辑回答了“为什么金融科技的长期价值没有消失”。完整报告里有大量分区域、分赛道的收入预测和估值模型，这些图表是判断具体赛道机会的基础。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 金融科技只渗透了全球金融收入的2%，剩下的98%才是真正的战场\n\n报告开篇就点出了一个被估值暴跌掩盖的事实：全球金融服务业每年产生约12.5万亿美元的收入，净利润率高达18%，是所有行业中最高的之一。而所有金融科技公司加在一起，只吃到了其中的约2450亿美元，占比不到2%。\n\n这个数字意味着什么？意味着即便金融科技的收入在未来十年增长六倍，达到1.5万亿美元，它在整个金融服务业中\n\n[... middle omitted ...]\n\n细分赛道最值得跟踪？金融科技公司的单位经济模型应该如何拆解？\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球80%成年人仍缺金融服务\n\n金融科技的下半场\n\n未来十年收入将增长6倍\n\n---\n\n最近读了一份BCG和QED联合发布的全球金融科技研报，信息量很大，帮你提炼几个核心判断：\n\n1️⃣ 行业正在经历“去泡沫”调整\n2020-2022年，头部金融科技公司估值一度冲到20倍收入，现在平均回落超60%。但这其实是健康的洗牌——那些没有清晰产品市场匹配的公司会被淘汰，留下的会更扎实。\n\n2️⃣ 基本面依然强劲\n全球金融服务年收入池高达12.5万亿美元，利润率18%。而金融科技目前只占不到2%——也就是说，98%的市场还在传统玩家手里。加上全球80%成年人仍处于“银行服务不足”或“无银行账户”状态，增长空间巨大。\n\n3️⃣ 下一个增长引擎：B2B和B2B2X\n过去十年支付领域领跑，但未来十年，面向企业的服务和“企业对企业对消费者”模式会成为主力。这些模式能帮传统机构快速补齐数字化能力，同时比纯C端模式更可持续。\n\n4️⃣ 新兴市场是最大变量\n亚太地区年增速27%，预计2030年将成为全球最大金融科技市场。这里的关键逻辑：智能手机普及率高、传统银行覆盖低、年轻人口基数大。\n\n5️⃣ 盈利才是真本事\n研报分析了85家上市\n\n[... middle omitted ...]\n\n15 Fintech Revenues Are Projected to Grow Sixfold by 2030 31 The Path Toward Growth Still Carries Risks, and Requires Action\n20 While Payments Led the Last Era, B2B2X and B2b Are Expected to \n\n[... middle omitted ...]\n\n Credit Karma, Flywire, Greensky, Kavak, Klarna, Konfio, Loft, Mission Lane, Nubank, QuintoAndar, Remitly, SoFi, Wagestream, and Wayflyer.\n\n![](images/249b59a7b18857e62313700e25affe0db17ac9ef102e2d1f69a00347930b2729.jpg)"
  },
  {
    "id": "R026",
    "title": "波士顿咨询：金融科技不是缺钱，是缺“审慎”",
    "digest": "[wechat_article.md]\n# 波士顿咨询：金融科技不是缺钱，是缺“审慎”\n\n金融科技行业过去三年经历了一场残酷的估值回调。2021年，一家中等规模的金融科技公司可以轻松拿到20倍收入的估值；今天，这个数字已经跌到4倍。全球融资额下降了70%，晚期融资更是暴跌超过八成。如果只看这些数字，你可能会认为这个行业正在走向寒冬的尾声，甚至已经进入冰河期。\n\n但波士顿咨询（BCG）与QED Investors联合发布的这份最新报告，给出了一个截然不同的判断：金融科技的增长从未停止，行业正在经历的不是衰退，而是规则的重写。全球金融科技收入在过去两年保持了14%的年复合增长率，如果剔除加密货币和中国市场，这一数字更高达21%。报告预测，到2030年，全球金融科技市场规模将从现在的3200亿美元增长到1.5万亿美元。\n\n真正值得关注的信号不是融资下降，而是行业内部正在发生的结构性分化。这份报告访谈了超过60位全球金融科技CEO和投资人，得出了一个核心判断：未来金融科技公司的生存法则，将从“增长优先”转向“审慎增长”。审慎——即避免给金融系统增加风险的能力——将与盈利能力同等重要。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 这轮调整的真正赢家不是融资最多的公司，而是最快实现盈利的公司\n\n报告中最引人注目的数据，不是融资额的下降，而是头部和尾部公司之间巨大的业绩差距。在几乎所有细分领域，前25%的金融科技公司收入增速都显著高于后25%。以支付领域为例，头部公司2021-2023年的收入年复合增长率接近40%，而尾部公司几乎停滞不前。\n\n更关键的是，行业正在从“不惜一切代价增长”的模式转向“盈利性增长”。过去两年，全球前70家上市金融科技公司的EBITDA利润率平均提升了9个百分点。但报告同时指出，这个转变仍处于早期阶段——绝大多数公司仍然低于“40法则”（即收入增\n\n[... middle omitted ...]\n\n图表以及更多投行对金融科技行业的最新判断，持续更新在社群中。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n# 金融科技的下一个增长逻辑\n\n**审慎增长，才是真本事**\n\n**盈利与合规，缺一不可**\n\n---\n\nBCG最新研报说，金融科技（Fintech）的“烧钱换增长”时代彻底结束了。\n\n新规则只有四个字：**审慎增长**。\n\n怎么理解？我拆成3个重点👇\n\n**1. 市场还在涨，但逻辑变了**\n\n全球Fintech收入仍在以14%的年增速增长，预计2030年市场规模能达到1.5万亿美元。\n\n但资本已经不再为“故事”买单。融资额下降了70%，估值倍数从20倍跌到4倍。\n\n现在投资人只问一个问题：**你什么时候能赚钱？**\n\n**2. 头部效应越来越明显**\n\n最值得关注的不是行业平均，而是头部和尾部的差距。\n\n以收入增速来看，前25%的Fintech和后25%的差距，比不同国家、不同赛道的差距都大。\n\n简单说：**赢家通吃，弱者出局。**\n\n**3. 三条新护城河**\n\n研报认为，接下来Fintech必须同时做好三件事：\n\n- **合规优先**：监管正在收紧，合规不再是成本，而是竞争力\n- **盈利优先**：EBITDA利润率需要提升超过25个百分点\n- **技术优先**：GenAI正在重塑客服、编码、数字营销的\n\n[... middle omitted ...]\n\nial services, but the true lasting legacy of fintech is the staggering impact on our day-to-day lives and our financial systems.\n\nAnd there is so much more room for growth. With the advent of \n\n[... middle omitted ...]\n\n<td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>"
  },
  {
    "id": "R027",
    "title": "波士顿咨询：零售银行AI转型的“价值鸿沟”正在被AI先行者填平",
    "digest": "[wechat_article.md]\n# 波士顿咨询：零售银行AI转型的“价值鸿沟”正在被AI先行者填平\n\n零售银行正站在一个微妙的分水岭上。一方面，GenAI和Agentic AI的技术潜力已被广泛认知，几乎所有银行都在谈论AI转型；另一方面，真正将AI转化为规模化业务价值的银行却寥寥无几。波士顿咨询（BCG）在2026年6月发布的这份报告揭示了一个核心判断：**AI先行者正在通过“更少但更深”的转型策略，系统性填平从概念验证到规模化价值的鸿沟，而跟随者的差距正在加速拉大。**\n\n这份报告的价值不在于罗列AI能做什么——那是共识——而在于回答了银行高管最焦虑的问题：为什么我的AI投入没有产生可衡量的回报？为什么别人的AI能提升40%的销售和降低70%的运营成本？\n\n答案指向六个结构性挑战，以及AI先行者截然不同的应对逻辑。\n\n> **KC评论：** 很多银行在AI上的投入是“点状”的——一个客服机器人、一个营销文案工具。BCG报告的核心洞察是，价值来自“面状”的、业务功能级的重新设计，而不是孤立工具的堆砌。完整报告里有一张图清晰展示了“从微用例到功能重想象”的路径差异，值得细看。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 零售银行天生适合AI，但规模化价值被六重障碍锁死\n\nBCG的判断很明确：零售银行在结构上比其他行业更适合GenAI和Agentic AI。理由有三：数字化程度相对较高、数据积淀丰富（尽管困在旧系统中）、客户对AI应用的接受度正在快速提升。\n\n但现实是，大多数银行的价值仍然停留在“口袋化”的阶段——某些场景有效果，但无法复制、无法规模化。报告识别了六个关键障碍：\n\n- 无法跳出微用例思维，停留在“小打小闹”\n- 没有在启动阶段就将项目与可衡量的价值指标挂钩\n- 缺乏CEO级别的直接问责，AI项目在业务、渠道、技术、合规之间迷失\n- 急于\n\n[... middle omitted ...]\n\n图表与深度评论，既适合AI辅助分析，也适合快速把握行业趋势。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n零售银行AI转型，这次是来真的\n\n**AI-first银行，正在改写规则**\n\n某外资投行最新报告显示，零售银行正处在GenAI和Agentic AI的价值爆发前夜。但有意思的是，真正吃到红利的，只有那些“AI优先”的银行。\n\n**为什么大部分银行还在“小打小闹”？**\n\n报告指出了6个关键卡点：只做微用例、没绑定价值指标、CEO参与度不够、只建点方案不建可复用产品、团队AI素养断层、风控流程后置。\n\nAI优先的银行，做法完全不同——聚焦3-4个战略方向，从第一天就设计风控，而且CEO亲自带队。\n\n**哪些环节已经跑出效果？**\n\n1. **获客端**：用GenAI生成合成客户画像，精准设计产品和渠道。新客销售提升超40%，获客成本明显下降。\n\n2. **服务端**：AI语音机器人处理70%+人工电话量，成本只有传统方式1/5。每个客户都有一个“永远在线”的AI客户经理，主动识别意图、给出方案，关系深度提升20%-40%。\n\n3. **运营端**：信贷审批5-10倍提速，反洗钱成本降50%，催收运营成本降约50%，周转时间降70%。\n\n**AI优先银行在押注的10项能力**\n\n获客侧：合成客户画像、生成式搜索\n\n[... middle omitted ...]\n\nlore the impact of GenAI and Agentic AI in retail banking and the approach followed to deliver impact. We address key questions faced by bank executives:\n\n\\- Why are GenAI and Agentic AI imper\n\n[... middle omitted ...]\n\nholesale Banking\nMunich\n\n## Javier Perez Moino\n\nMD & Partner\nAI in Customer Acquisition\nMadrid\n\n## Matthew Barton\n\nMD & Partner\nAI in Collections\nPhiladelphia\n\n## Yogesh Mishra\n\nMD & Sr. Partner\nAI in Tech\nDallas\n\n## BOG"
  },
  {
    "id": "R028",
    "title": "波士顿咨询：BCG：制造业回流不再是口号，AI正在改写全球工厂的选址逻辑",
    "digest": "[wechat_article.md]\n# 波士顿咨询：BCG：制造业回流不再是口号，AI正在改写全球工厂的选址逻辑\n\n过去十年，全球制造业CEO们最常问的问题是：哪里劳动力成本最低？但波士顿咨询（BCG）在2026年6月发布的最新研报中给出了一个颠覆性的答案：这个问题已经过时了。\n\n真正的新问题是：你的工厂能否被改造成“未来工厂”（Factory of the Future）？以及，在哪里改造，才能让这笔投资的经济回报最大化？\n\n这份报告的核心判断是：AI驱动的生产系统正在从根本上改变制造业的竞争经济学。它不再只是关于自动化某个环节，而是关于对整个生产流程进行端到端的重新设计。其结果，是让高达60%的生产成本节约成为可能，并使得约1.03万亿美元原本位于西欧和北欧的制造业价值面临重新选址的压力，另有4400亿美元位于美国的制造价值也同样面临风险。\n\n这意味着，过去几十年支撑全球供应链布局的“低成本劳动力”逻辑，正在被“高生产率系统”逻辑所取代。对于产业决策者而言，理解这一转变，比追逐任何单一的技术趋势都更为紧迫。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 未来工厂不是“升级”，而是对生产成本的“重构”\n\n许多制造企业认为，引入几台机器人、部署一套MES系统，就是在迈向未来工厂。但BCG的报告明确指出，这种零敲碎打的自动化，只能带来局部、渐进的改善。真正的未来工厂，是对整个生产流程进行“重构”。\n\n报告通过三个不同行业的模拟案例，清晰地展示了这种“重构”的威力。一家德国的咖啡烘焙和包装公司，通过整合自动化、智能过程控制、预测性维护和中央数据协调，实现了近60%的劳动力节省，总转换成本下降了超过40个百分点。一家美国的制药公司，通过数字孪生、物联网追踪和高级分析，同样将劳动力成本降低了超过60%，总转换成本下降了30个百分点。一家韩国的电池制造公司，通过连续\n\n[... middle omitted ...]\n\n盖最新的数据图表合集，帮助您和您的团队始终走在信息的最前沿。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n工厂选址逻辑变了，AI正在改写成本公式\n\n工厂选址的新逻辑\n\n投行研报指出，AI正在快速改变制造业的成本结构。到2026年，西欧美约1.03万亿、美国约4400亿美元的制造价值面临重新配置。\n\n核心变量不再是劳动力成本，而是能否把工厂改造成“未来工厂”。\n\n1/ 成本差距在缩小\n- 德国食品工厂升级后，比迁到中国有14个百分点的成本优势\n- 电池制造即使全面升级，仍比中国贵15个百分点\n- 不同行业差异巨大，不能一概而论\n\n2/ 三个技术突破\n- 智能体系统、物理+虚拟AI、计算能力\n- 让端到端生产流程重构在经济上可行\n- 不是单点自动化，而是系统性再造\n\n3/ 实际效果很具体\n- 德国咖啡烘焙厂：劳动力省60%，总成本降40%\n- 美国制药厂：劳动力省60%，总成本降30%\n- 韩国电池厂：劳动力省30%，总成本降25%\n\n4/ 六个决策维度\n- 本地化战略重要性\n- 未来工厂对成本的影响\n- 实际获得生产力提升的能力\n- 行业关税影响\n- 当地基础设施和人才准备\n- 是改造还是新建工厂\n\n5/ 投资回收期差异大\n- 美国做自动化：回收期基准为1\n- 德国接近美国水平\n- 低成本地区回收期要长2-8\n\n[... middle omitted ...]\n\non costs and unlocking productivity savings of up to 60%. And the stakes extend beyond the factory floor: roughly \\$1.03 trillion of manufacturing value is at risk of relocation out of Western\n\n[... middle omitted ...]\n\nto receive e-alerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on LinkedIn, Instagram, Facebook, and X.\n\n![](images/c15d76c3c79ea815b6de791771c2af1ee6009da44e8c911ee9f367e6d60810a0.jpg)"
  },
  {
    "id": "R029",
    "title": "波士顿咨询：BCG：中国IP崛起的“黄金窗口”已经打开，但企业还没准备好",
    "digest": "[wechat_article.md]\n# 波士顿咨询：BCG：中国IP崛起的“黄金窗口”已经打开，但企业还没准备好\n\n中国IP正在经历一次系统性的崛起。这不是一个令人振奋的口号，而是波士顿咨询（BCG）在一份最新研报中给出的结构性判断。\n\n这份报告的核心主张值得每一位关注文化消费、内容产业和全球化战略的决策者认真对待：中国IP崛起的三重宏观驱动——经济基础、社会结构与政策支持——已经同时进入共振期。这种“三重共振”在美、日、韩的历史上从未同时出现过，中国IP正站在一个历史先例清晰、现实条件充分、政策方向明确的“黄金窗口期”。\n\n但窗口期不等于必然成功。BCG的调研数据揭示了一个更微妙的现实：中国IP的全球认知度已达到74%，但海外消费者的整体兴趣评分仅为2.6分（满分5分）。换句话说，世界知道中国IP的存在，但还没有真正被吸引。\n\n这中间的落差，正是中国IP企业需要系统性回答的问题。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 人均GDP突破1万美元后的“双驱动”正在同时发力\n\nBCG报告的一个关键洞察是，中国IP崛起的宏观条件并非单一因素推动，而是两个力量在同时发挥作用。\n\n一方面，中国在2019年迈过人均GDP 1万美元这一关键节点，并保持约5%的稳健GDP增速。全球经验显示，当一个国家的人均GDP超过1万美元时，居民的消费结构会从“满足生存需求”转向“追求精神价值”。美国、日本、韩国均在跨过这一门槛后，迎来各自IP文化的黄金期——日本在1980年突破1万美元后，迎来了“动漫黄金时代”；韩国在1994年突破后，K-pop产业随之崛起。\n\n另一方面，中国正在经历的“口红效应”正在为IP消费提供额外的推动力。当经济承压时，消费者反而会增加低成本、高情绪价值的支出。日本“失落的三十年”期间，GDP增速不足1%，但动画产业规模仍保持着约5%的年增速。过去五年，\n\n[... middle omitted ...]\n\n便人工快速把握市场动态。\n\n顺着这些未解问题，我们继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国IP出海，到了什么阶段？\n\n认知度74%，兴趣度2.6/5\n\n中国IP正站在全球化窗口期。\n\n某外资咨询最新研报拆解：\n\n1️⃣ 为什么是现在？\n- 人均GDP超1万美元后，精神消费进入上升期\n- 城镇化率逼近70%，粉丝经济有了线下土壤\n- 社交媒体提供线上爆发力，双引擎驱动\n- 政策从“文化立国”到系统化支持\n\n2️⃣ 海外怎么看我们？\n- 认知度74%，潮玩（91%）和游戏（60%）领先\n- 兴趣度2.6/5，文化独特性是核心溢价\n- 70%消费者愿意未来购买，高收入市场增长快\n- 东南亚是第一落点，日韩门槛最高\n\n3️⃣ 产业链要补什么？\n- 创意阶段缺低成本试错机制\n- 衍生变现需前置规划，和内容同步设计\n- 长期运营缺“IP经纪人”角色\n- AI正在全链路赋能，从剧本到营销\n\n4️⃣ 全球化路径怎么走？\n- 短剧/网文/游戏：可同步出海\n- 长剧/电影：先国内成熟，再逐步向外\n- Labubu和《黑神话》证明，中国IP能打\n\n你最看好哪个中国IP走向全球？\n\n#学习笔记\n\n[source_mineru.md]\n## 破浪前行：中国IP的全球崛起之路\n\n2026年6月\n\n阮芳、俞晨骜、蔡菁容、唐\n\n[... middle omitted ...]\n\n产业链核心优势与跃迁路径\n\n![](images/786db6cc86ef337e688ac3598103383ffc9d7772423ebf259561a0fb7d7dd871.jpg)\n\n## 前言\n\n# 在全球文化竞争日益加剧的背景下，我们为何关注中国IP崛起？\n\nIP产业不仅是重要的经济增长引擎，更是国家软实力的核心载体。美国漫威、迪士尼，日本动漫游戏，以及韩国K-pop与\n\n[... middle omitted ...]\n\n14.jpg)  \nBCG洞察\n\n![](images/07e00d4b210b9a65f7c16a3c634263f42d227ba1e8f59e9ceae179ff918893b3.jpg)  \nBCG微信视频号  \n© 波士顿咨询公司 2026 年版权所有。\n06/26\n\n![](images/99fa1215f597aff7a455678cc594cd8ebc67b3fa5cc99378d79f788f3586b467.jpg)"
  },
  {
    "id": "R030",
    "title": "波士顿咨询：BCG报告：马来西亚家庭比你以为的更脆弱，也比你以为的更抱团",
    "digest": "[wechat_article.md]\n# 波士顿咨询：BCG报告：马来西亚家庭比你以为的更脆弱，也比你以为的更抱团\n\n这份由波士顿咨询（BCG）在2026年6月发布的《MY Family》报告，回答了一个几乎所有面向消费者和公共服务的机构都该问、却很少认真回答的问题：马来西亚家庭作为一个决策单位，到底是如何运作的？\n\n答案并不温情。报告描绘的画面是：一个高度集体化、异常自律、但几乎没有容错空间的家庭系统。丈夫是名义上的“支柱”，妻子是实际运转的“引擎”，老人是正在从安全网变成负担的过渡体，孩子是影响力不断上升但尚未贡献收入的“未来投票人”。\n\n这不是一篇关于“家庭价值观”的软文。这是一份关于家庭经济学、代际资源转移和消费决策权力的硬核解剖。以下是我们从中提炼出的五个核心洞察。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 马来西亚家庭比市场以为的更“集权”——但集权在丈夫手里，运转却在妻子手里\n\n报告最反直觉的发现之一，是马来西亚家庭的决策模式。表面上，73%的丈夫参与所有家庭决策，而妻子只有56%。丈夫主导长期资本支出——房产、汽车、投资、教育和医疗。妻子负责日常消费——食品杂货、外出就餐、婴儿用品和旅行。\n\n但“主导”不等于“控制”。当妻子有收入时（约60%的家庭），她的收入几乎与丈夫持平（在双收入核心家庭中，丈夫占52%，妻子占48%）。这意味着，妻子在贡献了几乎一半的家庭收入的同时，还承担了日常支出的全部管理责任。\n\n> **KC评论：** 这份报告揭示了一个对消费品公司和金融机构都很关键的结构性事实——如果你只针对“家庭决策者”做营销，你很可能只打中了丈夫，但错过了真正执行日常消费决策的妻子。更值得注意的问题是：当妻子贡献了接近一半的收入、却只主导约30%的预算支出时，这个家庭内部的“权力-责任”匹配是否可持续？报告没有直接回答，但数据暗示了潜在的\n\n[... middle omitted ...]\n\n庭医疗支出压力的详细数据拆解——这些在公开摘要里看不到。**\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n马来西亚家庭，比你想象的更“团结”\n\n谁是家里管钱的？\n\n最近BCG发了份马来西亚家庭决策研究，看完发现——我们对自己家的了解可能只停留在表面。\n\n1️⃣ 谁在赚钱？\n- 丈夫是收入主力，约80%家庭靠他\n- 但超过一半的妻子也在赚钱，而且收入几乎和丈夫持平\n- 在双职工家庭，夫妻收入比接近1:1\n\n2️⃣ 谁在花钱？\n- 丈夫管大钱：车房、投资、教育、医疗\n- 妻子管日常：买菜、吃饭、宝宝用品、旅行\n- 丈夫管约60%预算，妻子管约30%\n\n3️⃣ 家庭结构变了\n- 73%的家庭有18岁以下孩子\n- 一半家庭和长辈同住\n- 多代同堂不是文化选择，越来越是经济必需\n\n4️⃣ 最戳心的发现\n- 46%的父母愿意为子女教育放弃养老金\n- 37%愿意为此举债\n- 只有27%家庭能拿出5000令吉应急\n\n5️⃣ 决策是集体的\n- 58%家庭收入共用\n- 57%家庭一起存钱\n- 旅行是最“民主”的开支\n\n💡 给品牌/政策制定者的提醒：\n别只盯着“家庭”这个标签，要看清楚谁在哪个环节说了算。\n\n#学习笔记\n\n[source_mineru.md]\nBCG\n\n# MY Family\n\n## Understanding How\n\n[... middle omitted ...]\n\n shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, \n\n[... middle omitted ...]\n\nb2d639a03e6b0890023b9d5047cbafb20d6fee2ecb41.jpg)  \nHaris Mohd Zukki\nConsultant\nCore Member of Kuala Lumpur Office\nMohdZukki.Haris@bcg.com\n\n![](images/7516226f6bde51729582c90100319676723d552955dc35d5e6ab49ee5acd62d2.jpg)"
  },
  {
    "id": "R031",
    "title": "波士顿咨询：药企正在浪费患者发来的数字信号",
    "digest": "[wechat_article.md]\n# 波士顿咨询：药企正在浪费患者发来的数字信号\n\n中国医药行业每年在直接触达患者（DTP）上投入数百亿元，但绝大部分投入正在被浪费。不是创意不够好，不是预算不够多，而是患者通过网页浏览、问卷填写、呼叫中心交互发出的数字信号，散落在十几个互不相通的系统里，从未被整合成可执行的下一步行动。\n\n波士顿咨询（BCG）在2026年6月发布的这份报告点出了一个反常识的判断：患者获取的瓶颈，不是流量，不是内容，而是信号整合。当行业还在争论“私域流量”“精准投放”时，领先机构已经开始用Agentic AI（代理型人工智能）实时捕捉并响应患者行为信号，把一次性获客转化为持续优化的转化引擎。\n\n报告给出了一个让多数团队意外的结论：实现这一目标的经济门槛，远低于大多数人的假设。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 传统DTP模式的三个结构性困境，每个都在加剧\n\n患者旅程的起点已经永久改变。绝大多数患者从线上开始他们的健康决策，包括最终被推荐给专科医生的那一批。但大多数医药企业的直接触达患者（DTP）项目，仍然运行在十年前的设计逻辑上。\n\n第一个困境是患者期望值的结构性跃升。数字原生的健康品牌已经让患者习惯了“像电商一样”的个人化体验。患者不再拿药企品牌和同行比较，而是拿他们最好的数字交互体验作为基准。这意味着，一个响应迟缓、内容通用的DTP项目，在患者打开第一封邮件时就已经输了。\n\n第二个困境是静态程序与动态行为的错配。多数DTP模型仍然运行在预设的时间序列和宽泛的人群分组上。患者访问了网站、填写了问卷、拨打了呼叫中心，但这些行为信号从未被实时整合。团队无法回答最核心的问题：这个患者是卡住了还是正在推进？他需要的是教育、 reassurance，还是一次真人对话？今天，而不是下周，应该做什么？\n\n第三个困境是隐私监管正在重塑获客经济\n\n[... middle omitted ...]\n\n取完整研报解读与原始图表，一起讨论从试点到规模化的实操路径。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n患者发信号了，药企还在等日历？\n\n📌 别再错过患者信号\n\n📌 当AI读懂患者行为，转化率飙升\n\n---\n\n以前药企做患者触达，靠的是固定日历和广撒网。现在患者早就在网上留下了大量行为信号——网页浏览、问卷反馈、呼叫中心互动——但这些数据散落在不同系统里，没人串联起来。\n\n结果是：你花大价钱投广告，患者来了又走，因为你根本不知道他此刻需要什么。\n\n投行研报指出，那些跑在前面的公司，已经在用AI把碎片信号拼成完整的患者画像，然后实时决策下一步动作。\n\n1️⃣ **传统模式为什么失效？**\n- 患者习惯了数字原生品牌的个性化体验，拿药企跟同行比？不，他们跟最好的互联网产品比。\n- 固定序列的触达，永远跟不上患者真实行为的变化。他卡住了还是往前走了？需要教育还是直接对话？没人知道。\n- 隐私法规收紧，靠第三方数据获客越来越贵。第一方、经患者同意的数据，才是未来最值钱的资产。\n\n2️⃣ **三种AI能力，各司其职**\n- 预测AI：持续评估每个患者的转化概率、流失风险，告诉系统谁需要关注。\n- 生成AI：批量产出经法务审核的个性化内容，打破内容生产瓶颈。\n- 代理AI：实时观察信号，决定下一步动作（渠道、时机、内\n\n[... middle omitted ...]\n\nmetrics land in separate systems that are never collected and tailored into actionable next steps. The result is outreach that is run on fixed calendars rather than adapted to real patient beh\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R032",
    "title": "波士顿咨询：CPG巨头失去的十年，研发欠账正在到期",
    "digest": "[wechat_article.md]\n# 波士顿咨询：CPG巨头失去的十年，研发欠账正在到期\n\n这份波士顿咨询的报告，讲了一个听起来反常识但数据上极其扎实的判断：全球最大的食品饮料公司，过去十年一直在“假装创新”。它们把收入的6%到15%砸在广告和促销上，研发投入却只有可怜的1.5%。这个策略曾经奏效，但今天正在全面瓦解。报告用了一个非常精准的词——the bill is coming due，欠账要还了。\n\n为什么现在重要？因为市场已经给出了判决。过去三年，大型食品饮料公司的股东总回报中位数约为-5%，而同期标普500累计回报接近90%。最差的公司甚至跌了20%以上。这不是周期性问题，这是结构性问题。消费者正在以前所未有的速度转向更健康、更简单的产品，而巨头们的产品组合还停留在十年前。\n\n这份报告最有价值的地方，不是重复“健康化趋势”这个老生常谈，而是用数据和框架证明了：研发欠账已经转化为市场份额的持续流失，而且流失速度在加快。它没有停留在诊断，还给出了一个清晰的行动路线图——从SKU级别的暴露度诊断开始。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 1.5%的研发投入，撑不起一个“创新”的故事\n\n波士顿咨询的数据很直白：2015年到2025年，全球大型食品饮料公司的研发投入仅占收入的1.5%。作为对比，制药业是21%，消费电子是18%，软件是16%到20%。行业之间直接对比或许不完全公平，但量级的差距已经说明一切。\n\n更值得关注的是资金流向的对比。同期，这些公司花在广告和促销上的费用占收入的6%到15%，研发投入的年增速只有1.2%，而广告费的增速是2.6%，是研发的两倍多。这不是一个短期波动，而是一个持续二十年的战略选择。\n\n这个选择背后的逻辑曾经成立：用规模和营销肌肉维持老品牌的生命力，不需要突破性的产品创新。但今天，这个逻辑正在被三重力量打破——\n\n[... middle omitted ...]\n\n据图表合集，既方便喂给AI，也方便人工快速把握市场动态。**\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n大牌零食巨头，正在失去未来\n\n食品巨头的“创新债”\n\n投行研报揭示了一个扎心事实：过去十年，全球大型食品饮料公司平均只把1.5%的收入投入研发，却把6%-15%砸在广告上。结果呢？消费者对健康、简单、透明成分的需求，正让这些巨头们措手不及。\n\n1/ 研发欠账，股价买单\n2015-2025年，巨头们研发投入年均只涨1.2%，广告费却涨了2.6%。同期，标普500涨了近90%，但大型食品饮料公司三年平均股东回报竟然是-5%。研发落后的代价，直接写在了股价上。\n\n2/ 新品牌正在“偷家”\n益生元汽水、植物基乳品、GLP-1友好零食……这些爆款几乎都来自挑战者，不是老牌巨头。2021-2025年，麦片和谷物棒品类里，大品牌丢了12.4%的份额，小品牌却抢了10.8%。零售商自有品牌也在猛追，靠的是更贴近消费者和社交媒体沟通。\n\n3/ GLP-1带来的结构性冲击\n美国GLP-1药物用户已从2022年的600万涨到1600万，预计2030年超3000万。用户热量摄入减少30%，零食消费降40%，约1/3食物支出转向营养补剂和健身。更关键的是，70%的GLP-1用户家庭也跟风改变饮食，影响范围是用户数的1.5倍。\n\n[... middle omitted ...]\n\nuctural shift that many big CPG manufacturers have so far failed to navigate is consumers' growing preference for healthier and simpler products and for greater transparency about ingredients,\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R033",
    "title": "波士顿咨询：保险业价值创造正经历一个关键拐点",
    "digest": "[wechat_article.md]\n# 波士顿咨询：保险业价值创造正经历一个关键拐点\n\n过去五年，全球保险业的股东总回报（TSR）首次系统性超过了其资本成本。这不是一个周期性脉冲，而是一个结构性变化的早期信号。波士顿咨询在2026年4月发布的《保险价值创造报告》中，用15%的五年年化TSR数据，宣告了行业自2017年以来首次真正意义上的价值创造拐点。\n\n这份报告的特殊之处在于，它采取了“提前发布”的新策略——在全年数据尚未完全到位时，就给出了方向性判断。这意味着，报告的核心价值不在于精确的数字，而在于它捕捉到的三个正在发生的结构性转移：投资者偏好从财险向寿险与健康险迁移、地域焦点从美国向欧洲和亚太迁移、以及竞争逻辑从承保周期管理向技术驱动的效率竞争迁移。\n\n对于保险公司的CEO、投资者以及关注金融行业趋势的决策者来说，理解这些转移的底层逻辑，比关注任何单季度的保费增速都更重要。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 行业终于跑赢了资本成本，但这个窗口期可能并不长\n\n保险业长期面临一个尴尬的现实：尽管保费规模巨大，但股东回报长期徘徊在资本成本附近。波士顿咨询的数据显示，过去五年行业年化TSR达到15%，首次系统性超过资本成本。这个拐点的直接驱动力有两个：疫情影响的消退和当前盈利的改善。\n\n但这里的关键洞察在于，这个窗口期可能并不稳定。财险业务的费率动能已经出现放缓迹象，尤其是在商业财产险领域。2025年的TSR数据已经显示，费率软化正在侵蚀承保利润率。这意味着，行业跑赢资本成本的状态，更多是过去几年硬市场环境的滞后反映，而非结构性的盈利能力提升。\n\n> **KC评论：** 对于投资者而言，真正需要关注的不是15%这个数字本身，而是它能否持续。波士顿咨询报告隐含的判断是，如果费率继续软化，行业TSR可能在未来1-2年内重新向资本成本回归。完整报告中包含\n\n[... middle omitted ...]\n\n加入我们的社群，与更多关注全球金融行业趋势的决策者一起讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n保险业的回报，正悄悄换挡\n\n**回报回暖，格局在变**\n\n过去五年，保险业的股东回报其实一直不温不火。但去年，一个关键信号出现了：行业五年年化股东总回报（TSR）达到了15%，这是自2017年以来，首次跑赢资本成本。背后两个推力：疫情影响的消退，加上当期业绩确实在改善。\n\n**1. 资金在“搬家”**\n投资者正在悄悄调整偏好。过去几年，财险和再保险因为费率上涨，TSR表现最强。但2025年开始，风向变了——寿险健康和综合险反而跑赢了。原因是高利率环境带来了投资收入顺风，利润和回报都被拉了一把。\n\n**2. 区域也在“换仓”**\n欧洲成了五年期的回报之王，年化TSR达到20.3%，远超去年。亚太和欧洲在一年期表现也很猛，分别达到35.3%和39.8%。背后的逻辑是：美国宏观和市场不确定性高，投资者在找“避风港”，资金流向了更稳定的市场。\n\n**3. 未来三大趋势**\n- **AI渗透**：从核保理赔到人才管理，AI代理的应用会重塑整个行业。\n- **财险承压**：费率在部分领域（如商业财产）开始软化，美国车险竞争加剧。长期看，贸易流变化带来的结构性风险也不容忽视。\n- **寿险需求升级**：老龄化叠加客户偏好变\n\n[... middle omitted ...]\n\n on available—but not yet complete for the full year—data. Subsequent installments will provide a more detailed segment- and region-specific analysis as well as offer deep dives into the prope\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R034",
    "title": "波士顿咨询：美国财险市场最危险的信号，不是费率走软",
    "digest": "[wechat_article.md]\n# 波士顿咨询：美国财险市场最危险的信号，不是费率走软\n\n美国财产与意外险（P&C）市场正在经历一个罕见的转折点：在连续数年强劲表现之后，市场的基本面正在发生结构性分化。波士顿咨询（BCG）最新发布的《2026保险价值创造者报告》揭示了一个核心判断——行业领导者与落后者之间的差距正在以过去十年未见的幅度拉大，而这一差距的根源，并非市场周期本身，而是对结构性风险的反应速度与能力。\n\n这份报告的数据窗口覆盖了2021年至2025年，正是美国财险市场从硬市场转向软市场、从利率上升周期转向常态化、从传统承保模式转向AI驱动模式的关键五年。BCG的分析显示，尽管行业整体五年年均股东总回报（TSR）仍维持在约18%的高位，但2025年单年数据已明显减速。更值得关注的是，头部与尾部公司在承保利润率上的鸿沟，已经达到了难以用投资收入弥补的程度。\n\n对于产业决策者和高净值投资者而言，这份报告的价值不在于它确认了“好公司继续好”的常识，而在于它用数据揭示了“什么构成了好公司”的新定义。在费率走软、损失成本持续上升、气候风险与诉讼环境恶化的三重挤压下，传统的规模优势正在被更精细的能力优势所取代。\n\n> **KC评论：** 这份报告最重要的判断是——美国财险市场正在从“靠天吃饭”的周期游戏，转向“靠能力吃饭”的结构性竞争。对于关注保险板块资产配置的读者，这意味着过去那种“买龙头、等周期”的策略可能不再奏效。完整报告中有详细的分组数据对比，展示了头部与尾部公司在承保、投资、费用结构上的具体差异，这些数据在公开市场上并不容易获取。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 承保能力已取代投资收入，成为利润分化的唯一标准\n\nBCG的长期追踪数据呈现出一个清晰的规律：在每一个五年周期中，承保利润率都是区分领导者和落后者最稳定的指标。2021至202\n\n[... middle omitted ...]\n\n果你希望看到完整报告的解读和原始图表，欢迎加入社群继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美国财险市场正在分化，好公司越来越赚钱\n\n中间断层，头部赢家通吃\n\n保险业正在从“靠涨价”转向“靠技术”\n\n某外资投行最新研报拆解了2021-2025年美国财险市场的变化，信息量很大，但逻辑很清晰👇\n\n**1. 市场从“硬”转“软”，涨不动了**\n过去几年保费持续上涨，但2025年开始费率走软。个人车险和商业财产险首当其冲。靠涨价改善盈利的路走不通了，接下来得靠数据、细分和费用控制。\n\n**2. 承保质量决定一切**\n研报数据显示，2021-2025年，头部公司的承保ROTE贡献约11个百分点，而尾部公司是负值。差距在拉大，且投资收入一旦回落，承保质量就是唯一的护城河。\n\n**3. 个人车险恢复，但竞争加剧**\n2025年个人车险综合成本率降到92%（2022年是112%）。但恢复不均匀——先行者Progressive降到88%并成为市场第一，其他公司还在补课。现在大家开始“从防守转进攻”，重新抢市场，但理赔频率和严重度还在上升，利润率可能被压缩。\n\n**4. 房屋险：表面风光，暗藏风险**\n2025年房屋险综合成本率88%，是2006年以来最佳，但主要靠没有大飓风。气候风险、再保险成本、监管变化都在施压。中\n\n[... middle omitted ...]\n\ne cost of losses, driven by such factors as social inflation, severe convective storms (SCSs), and elevated claims severity, remains high. The result is a more complex operating\n\nenvironment i\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R035",
    "title": "波士顿咨询：Physical AI的回报周期已从5-7年缩短至1-3年，CEO们不能再等了",
    "digest": "[wechat_article.md]\n# 波士顿咨询：Physical AI的回报周期已从5-7年缩短至1-3年，CEO们不能再等了\n\n当大多数CEO还在把机器人自动化视为“未来议题”时，一项关键指标已经发生了质变。\n\n波士顿咨询（BCG）最新发布的Physical AI报告给出了一个足以改变企业投资决策的数字：前沿机器人投资的回报周期已从此前的5-7年，骤降至1-3年。这不是渐进式改善，而是数量级的跃迁。\n\n与此同时，可自动化的工作范围扩大了50%，训练机器人所需的工程时间减少了70%。这三个数字叠加在一起，指向一个清晰的结论：Physical AI已经从“值得关注”进入了“必须行动”的阶段。\n\n对于产业决策者而言，真正的问题不再是“要不要投”，而是“如果不投，竞争对手用更快的速度、更低的成本追上来时，你的护城河还剩多少”。\n\n> **KC评论：** 这份报告的核心价值不在于列举技术趋势，而在于给出了一个CEO可以立即用来评估自身处境的分析框架。1-3年的回报周期意味着，Physical AI已经从资本支出决策变成了运营效率决策。完整报告中还包含了传统机器人与Physical AI在成本结构上的详细对比，以及不同行业的部署优先级分析，这些图表对制定具体投资计划至关重要。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 这轮变化真正考验的是企业能否把规模转化为议价权\n\nPhysical AI的进步不是单一技术的突破，而是硬件、软件和训练方式三个维度的协同演进。\n\n报告指出，传统机器人约75%的成本来自系统集成、安装和工程调试。而软件定义的Physical AI可以将这部分成本削减一半以上。关键变化在于：机器人可以在虚拟数字环境中完成训练，在“学会”如何执行任务后再被部署到真实场景。这意味着现场调试这一最昂贵、最耗时的环节被大幅压缩。\n\n但这里有一个容易被忽视的\n\n[... middle omitted ...]\n\n图表合集，既方便喂给AI做分析，也方便人工快速把握市场动态。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n机器人进化了，你的工作还扛得住吗？\n\n**物理AI时代，CEO必看的5个动作**\n\n物理AI正在改写自动化规则。机器人能看、能适应、能实时调整，部署成本大降。以前觉得太复杂、太贵的活儿，现在都成了可能。\n\n1️⃣ **重新评估你的运营痛点**\n别盯着科幻电影里的全能机器人。现实中，物理AI有四大能力梯队：\n- 视觉感知：机器视觉让机器人能认出物体和位置\n- 灵巧操控：能处理变形、不规则的物件，但还需大量训练\n- 工作流规划：告诉它“做什么”，它自己规划“怎么做”\n- 推理能力：最高阶，能预判动作后果，目前还很遥远\n\n2️⃣ **别只替换人，要重新设计流程**\n物理AI通常只能替代一个岗位50%的任务，但效率更高。关键是把任务重新分配：机器人做重复性体力活，人去做视觉质检。工厂和仓库要按机器人逻辑来设计，才能做到全天候运转。\n\n3️⃣ **先想好技术架构，再找供应商**\n别被供应商带着节奏走。先规划好硬件、操作系统、仿真训练环境和应用层怎么整合。物理AI行业竞争激烈，带着系统性方案去找供应商，才容易拿到顶尖技术。\n\n4️⃣ **提前告诉员工，工作会怎么变**\n从产线工人变成机器人主管，很多人其实是欢迎的。尽早沟\n\n[... middle omitted ...]\n\nnding still for companies that hesitate.\n\n## What the Numbers Say\n\n50%\n\nIncrease in the scope of work that can be automated compared to traditional robotics\n\n70%\n\nReduction in\nengineering time\n\n[... middle omitted ...]\n\nee in an unfamiliar real-world environment. It encapsulates the challenge of integrating perception, manipulation, planning, and adaptability in unstructured settings as a proxy for general-purpose embodied intelligence."
  },
  {
    "id": "R036",
    "title": "波士顿咨询：菲律宾数字金融的“供给缺口”才是真正的入场信号",
    "digest": "[wechat_article.md]\n# 波士顿咨询：菲律宾数字金融的“供给缺口”才是真正的入场信号\n\n当多数投资者还在关注东南亚数字金融的渗透率故事时，波士顿咨询这份受Maya委托、基于一手定性和定量研究的报告，给出了一个更微妙的判断：菲律宾的吸引力不在于“还有多少人没用上手机银行”，而在于“供给端的结构性约束正在系统性松绑”。\n\n报告指出，菲律宾拥有超过1亿人口、未来五年约6%的GDP增长、年轻且高度数字化的消费者群体——这些基本面并不新鲜。真正值得关注的，是报告揭示的一个核心矛盾：金融服务的低渗透率并非需求不足，而是历史形成的运营模式、分销经济和风险评估手段长期压制了供给。如今，数字基础设施和监管框架正在同时解除这三重约束。\n\n这意味着，菲律宾数字金融的下一个增长阶段，将不是简单的“从0到1”的获客故事，而是“从交易到关系”的价值深挖。对于已经布局或正在评估东南亚市场的机构而言，这份报告提供了一个关键的观察框架：谁能在支付规模的基础上，把交易数据转化为存款和信贷的定价权，谁就能在下一轮竞争中占据主动。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 菲律宾的宏观基本面，比多数东南亚同行更接近“消费驱动型经济体”\n\n波士顿咨询的报告开篇就用一组对比数据，重新定位了菲律宾在全球新兴市场中的独特位置。在人口过亿的七个新兴经济体中，菲律宾与越南、印尼同属东盟增长市场，但它的增长模式更接近墨西哥和美国——私人消费占GDP的比重高达约76%，远高于东南亚平均水平。\n\n这种消费驱动结构的背后，是两股结构性力量。第一，海外劳工汇款持续稳定在GDP的8-9%，形成了可预测的国内需求底座。第二，中产阶级家庭数量预计从2025年的580万户增长到2035年的880万户，这意味着未来十年将有超过50%的增量家庭进入消费升级通道。\n\n报告据此预测，2025-2030年间菲律宾人均\n\n[... middle omitted ...]\n\n群。每天，我们都会推送经过筛选和解读的全球顶级机构研报精华。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n菲律宾：下一个数字金融的蓝海市场\n\n**菲律宾：数字金融新机遇**\n\n**1.17亿人口 + 6% GDP增速，数字金融基础已就位**\n\n最近读了一份某外资投行关于菲律宾数字金融的报告，信息量很大，跟大家分享几个关键点。\n\n菲律宾正处在数字金融爆发的临界点。有1.17亿人口，未来5年GDP增速预计在6%左右，但金融服务的渗透率却很低——一半成年人没有银行账户，家庭和中小企业的信贷渗透率也落后于同类国家。\n\n**为什么说现在是好时机？**\n\n1️⃣ **宏观基础扎实**\n- 消费驱动型经济，私人消费占GDP的76%\n- 海外劳工汇款稳定在GDP的8-9%，为消费提供支撑\n- 中产家庭预计从2025年的580万增长到2035年的880万\n\n2️⃣ **数字基础设施正在完善**\n- 支付已经规模化\n- 身份识别和信用数据系统在改善\n- 数字优先的平台能把交易行为转化为存款和信贷\n\n3️⃣ **政策环境友好**\n- 菲律宾采取市场主导的经济模式\n- 政府干预少，私营企业主导资本配置\n- 主权信用评级已提升至投资级\n\n**核心机会：**\n下一阶段的增长将来自两方面：一是让剩余的无银行账户人群首次获得金融服务，二是让现有\n\n[... middle omitted ...]\n\ns usefulness in achieving any purpose. Readers are responsible for assessing the relevance and accuracy of the content of this document. It is unreasonable for any party to rely on this docume\n\n[... middle omitted ...]\n\nnsformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com.\n\n![](images/63d4b7a21b24f48d0ba97d4413cb1443e05f17871790fb46e664917d8a4e94cb.jpg)\n\nBCG"
  },
  {
    "id": "R037",
    "title": "波士顿咨询：AI竞争已进入“Token时代”，赢家通吃的规则变了",
    "digest": "[wechat_article.md]\n# 波士顿咨询：AI竞争已进入“Token时代”，赢家通吃的规则变了\n\n当智能不再是稀缺资源，企业竞争的底层逻辑正在被重写。波士顿咨询（BCG）在最新发布的报告中提出一个核心判断：我们已进入“基于Token的竞争”时代。Token是AI模型的语言和货币，也是企业将智能转化为商业价值的计量单位。这份报告通过对107家上市科技公司Token消耗量的实证分析发现，最高Token使用组的企业营收中位数增长率为16.5%，而最低组仅为5.1%。差距不是偶然，而是新竞争规则的先兆。\n\n报告的核心主张是：当智能变得可规模化、可获取，竞争优势不再来自拥有智能，而来自比竞争对手更高效地将智能应用于业务问题。这意味着，企业需要像管理资本投资一样管理Token支出，并建立全新的衡量体系——ROInt（智能投资回报率）。这不是一份关于AI趋势的泛泛讨论，而是一份关于如何将AI从成本中心转化为战略引擎的操作指南。\n\n但报告的真正价值不在于它给出的答案，而在于它揭示了一个尚未被充分讨论的问题：Token竞争的本质是“速度”还是“系统”？波士顿咨询在1988年首次提出“基于时间的竞争”，如今他们用“基于Token的竞争”与之呼应。但Token竞争是否只是时间竞争的AI版本？还是存在更深层的结构性差异？这些追问，正是我们需要在完整报告中寻找的答案。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. Token消耗量与企业增长之间存在强相关，但因果链条仍需拆解\n\n波士顿咨询的实证分析提供了最直观的证据：在107家年营收超过5亿美元的上市科技公司中，Token消耗量最高的五分之一企业，营收中位数增长率为16.5%，而最低的五分之一仅为5.1%。这个数据本身具有冲击力，但更重要的是理解背后的机制。\n\n报告指出，Token消耗量可以被一致地衡量，尤其是在软件工程领\n\n[... middle omitted ...]\n\n能力有进一步兴趣，欢迎加入社群，领取完整研报解读与原始图表。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI红利，拼的是“token”使用效率\n\nToken时代，拼的不是谁家AI更聪明\n\n当AI模型已经拥有博士级知识，智力不再稀缺，竞争的核心就变了。优势不再来自“拥有智能”，而来自“如何更高效地应用智能”——这就是BCG提出的“Token竞争”时代。\n\n1/ 用Token衡量AI产出效率\n某外资投行研究了107家科技公司，发现高Token使用组的收入增速（16.5%）是低使用组（5.1%）的3倍多。Token就像AI时代的“工业用电”，谁用得有效率，谁就领先。\n\n2/ 别只盯着省钱，要算ROInt\n建议用“智能投资回报率”（ROInt）来评估AI项目。这个指标把人和Token的成本都算进去，能帮你比较不同AI应用的真实价值。比如客服自动化看降本，研发创新看增量产出。\n\n3/ Token要像资本一样管理\n别把AI预算扔给IT当成本中心。建议由AI卓越中心或业务部门主导，把它们当作战略投资来规划。比如Reckitt把AI用在营销、研发等环节，内容开发提速60%，研发周期缩短，创新质量还更高。\n\n4/ 人是Token的“放大器”\n别急着用AI替代人。Gartner预测，一半因AI削减客服的公司2027年前得重新招人。\n\n[... middle omitted ...]\n\nusiness problems more productively than competitors can do. Because that intelligence is deployed through the consumption of tokens—the language and currency of AI models—we call this “token-b\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R038",
    "title": "波士顿咨询：数字资产不是产品创新，是银行基础设施的换轨",
    "digest": "[wechat_article.md]\n# 波士顿咨询：数字资产不是产品创新，是银行基础设施的换轨\n\n2026年5月，波士顿咨询（BCG）发布了其旗舰报告《数字资产的未来》。这份长达65页的报告，从董事会视角、执行委员会视角、CRO视角和CTO视角，系统拆解了数字资产对银行业的结构性影响。它的核心判断值得每一位金融机构决策者认真对待：**数字资产不是下一个产品线，而是银行核心基础设施的一次换轨——就像从模拟通信切换到数字通信，银行必须同时运营两套铁路，直到新轨道的规模经济让旧轨道无以为继。**\n\n报告明确指出，当前市场格局中，加密资产市值约3万亿美元，稳定币约3000亿美元，而数字化的真实世界资产（RWA）虽仅有约300亿美元的公开规模，却是对银行业长期战略意义最大的类别。BCG的渐进情景预测，到2035年，数字RWA可能达到全球可投资资产的约16%。而在快速扩张情景下，银行可能面临约10%的资产负债表缩减、约14%的收入下降以及约30%的利润下滑。\n\n这不是一份“要不要做”的报告，而是一份“不做会怎样、做了怎么做”的战略框架。以下是我们从这份报告中提炼的八个核心洞察。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 银行的收入池正在被数字资产从三个方向同时挤压\n\nBCG的报告没有把数字资产视为单一威胁，而是拆解出三条并行作用于银行盈利能力的结构性力量。\n\n第一条力量来自代币化本身。当资产可以在分布式账本上直接发行、交易和结算，传统中介的角色就被压缩了。报告指出，代币化减少了中介需求，价值从银行向非银行平台和资产管理公司转移。第二条力量是客户界面的迁移。当钱包和加密平台成为数字原生客户的主要入口，银行的存款基础和对客户关系的控制权都在流失。第三条力量是成本的双轨运行。在旧轨道和新轨道并行运营期间，银行不得不承担临时的成本重复——既要维护传统清算系统，又要投资数字\n\n[... middle omitted ...]\n\n案，欢迎加入社群，与我们一同追踪数字资产对银行业的真实影响。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n数字资产不是产品，是基础设施转型\n\n银行必须面对的下一场结构变革\n\n某外资投行最新研报核心观点拆解👇\n\n1️⃣ 当前市场格局\n- 加密市场已约3万亿美元，稳定币约3000亿\n- 数字RWA（真实资产）目前仅约300亿，但潜力最大\n- 稳定币约2/3用于加密交易，1/4用于新兴市场储值，仅1/10用于实体经济\n\n2️⃣ 银行面临的三重压力\n- 代币化减少中介需求\n- 价值从银行流向非银平台\n- 新旧系统并行运营导致成本翻倍\n\n3️⃣ 各业务线影响速览\n- 零售/财富：存款流失风险，但钱包+托管可带来年3.4-6亿美元增量\n- 企业银行：跨境支付承压，但可做稳定币+可编程财资\n- 资管：费率透明化压缩利润，代币化基金可提升15-30%收入\n- 资本市场：结算加速压缩传统收入，但RoE可提升4%\n\n4️⃣ 关键判断\n- 数字RWA虽小，但战略意义最重\n- 最需警惕的是失去客户界面和基础设施控制权\n- CEO任务不是预测赢家，而是保持系统相关性\n\n5️⃣ 行动框架（十步中的核心）\n- 前12个月：建立统一治理，加入机构网络\n- 12-36个月：规模化托管和抵押品用例\n- 3-5年：优化资产负债表，整合遗留系统\n\n#学\n\n[... middle omitted ...]\n\nout this collective depth of knowledge and the group's extensive work across the ecosystem, including Global Systemically Important Banks (G-SIBs), regional banks, fintechs, industry associati\n\n[... middle omitted ...]\n\nll levels of the client organization, fueled by the goal of helping our clients thrive and enabling them to make the world a better place.\n\n![](images/33ba8eed6213e5d6aa854c48ade4a2af13dccb9c3bd4f0827cbc9db27c6cfb63.jpg)"
  },
  {
    "id": "R039",
    "title": "波士顿咨询：AI价值鸿沟正在撕裂企业，只有5%的公司真正赢",
    "digest": "[wechat_article.md]\n# 波士顿咨询：AI价值鸿沟正在撕裂企业，只有5%的公司真正赢\n\n过去两年，几乎所有CEO都在追问同一个问题：AI投资到底带来了多少实际回报？大多数人的回答并不令人鼓舞。\n\n波士顿咨询（BCG）最新发布的《Build for the Future 2025》报告，基于对全球超过1250家企业的系统研究，给出了一个尖锐的实证结论：AI正在制造一场企业间的结构性分裂，而不是普惠性升级。只有5%的企业真正从AI中获得了规模化价值，而60%的企业尽管投入巨大，却几乎没有看到实质性回报。\n\n这不仅仅是一份关于AI采用率的报告。它揭示了一个正在加速的反馈循环：领先者正在用AI创造的利润反哺AI能力建设，差距每季度都在拉大。而落后者，如果不在12-18个月内做出根本性调整，可能永远追不上。\n\n这份报告最值得关注的核心判断是：AI的价值鸿沟不是暂时的技术差距，而是由组织战略、运营模式、人才体系共同决定的系统性分化。它不会自然弥合，只会越拉越大。\n\n---\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 5%的企业已经跑通AI的价值闭环，而60%还在原地打转\n\nBCG将企业AI成熟度分为四档：未来型（Future-Built）、成长型（Emerging）、停滞型（Stagnating）、以及尚未启动型。未来型企业仅占5%，但它们已经跑通了从投入到回报再到再投资的完整闭环。\n\n数据支撑了这一判断。未来型企业在收入增长上是落后企业的1.7倍，EBIT利润率高出1.6倍，三年股东总回报达到3.6倍，投入资本回报率则高达2.7倍。这不是未来预期，而是已经实现的财务表现。\n\n这些企业并非靠AI做边缘优化。它们将AI嵌入核心业务流程——研发、销售与营销、制造、供应链——并实现了端到端的重塑。报告特别指出，70%的AI价值集中在这些核心职能中，而非后台支\n\n[... middle omitted ...]\n\n天最新的数据图表合集，帮助你持续跟踪AI价值鸿沟的演变趋势。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI价值鸿沟正在扩大\n\n只有5%的公司真正赚到AI的钱\n\n未来已来，但只有少数人抓住了机会\n\n---\n\n某外资投行最新报告显示，AI的价值鸿沟正在加速扩大。\n\n1️⃣ 只有5%的公司是真正的赢家\n全球1250家企业的调研数据显示，只有5%的公司从AI中获得了规模化价值。这些公司收入增长是其他公司的1.7倍，股东回报是3.6倍，EBIT利润率高出1.6倍。\n\n2️⃣ 60%的公司还在原地踏步\n尽管投入了大量资金，60%的公司几乎没有从AI中获得实质性回报。很多公司高管口头支持，但没有明确的战略目标，把AI推给中层管理，结果就是一堆零散的试点项目。\n\n3️⃣ 核心业务才是AI的主战场\n70%的AI价值集中在核心业务：销售、市场、供应链、研发。IT部门的AI价值占比从2024年的7%跃升到2025年的13%。\n\n4️⃣ Agentic AI正在成为加速器\n2024年几乎没人讨论的AI Agent，2025年已经贡献了17%的AI价值，预计到2028年将达到29%。但部署AI Agent需要先打好数据基础、建立治理框架。\n\n5️⃣ 赢家在做5件不同的事\n- 制定多年AI战略，自上而下推动\n- 重塑核心工作流，不只是自\n\n[... middle omitted ...]\n\nctor and Region\n\n11 What Value Generators Do Differently\n• Pursue a Multiyear Strategic AI Ambition\n• Reshape and Invent with Impact\n• Adopt an AI-First Operating Model\n• Secure and Enable the\n\n[... middle omitted ...]\n\nalerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on LinkedIn, Facebook, and X (formerly Twitter).\n\n![](images/1d7bfc57d3a1e9ad701ad9cbe653c75cfee078efb6aa3451e45868acc2c36836.jpg)\n\nBCG"
  },
  {
    "id": "R040",
    "title": "波士顿咨询：游戏行业“冬季”结束，但增长逻辑已彻底更换",
    "digest": "[wechat_article.md]\n# 波士顿咨询：游戏行业“冬季”结束，但增长逻辑已彻底更换\n\n游戏行业正在走出为期三年的“视频游戏冬季”，但复苏的方式与过去十年完全不同。波士顿咨询在2025年底发布的这份《视频游戏报告2026》给出了一个核心判断：行业增长将重新加速，但驱动引擎已不再是硬件换代或爆款单机，而是四个正在碰撞的结构性趋势——生成式AI、用户生成内容、云游戏和开放应用商店。这四股力量单独看都足够重要，但真正让BCG给出“乐观”评级的原因，是它们正在同时发生，并且相互催化。\n\n这意味着，过去围绕主机战争、独占内容和发行窗口建立起来的竞争规则，将在未来五到十年内被重新书写。对于产业决策者而言，现在需要回答的问题不是“下一款爆款在哪里”，而是“我的公司在这套新规则下还有没有位置”。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 这轮复苏不会回到2010年代的增长速度，但结构更健康\n\nBCG基于对约3000名玩家的全球调查和行业访谈，认为行业即将走出2022年以来的低迷期。但报告明确强调，增长不会回到2010年代“十年翻倍”的速度。这不是悲观，而是现实——2010年代的增长很大程度上来自移动游戏用户的爆发式扩张，而那个红利已经基本兑现。\n\n真正值得关注的信号来自需求端。报告显示，约55%的玩家在过去六个月内增加了游戏时间。更关键的是代际传递：44%的玩家父母表示，他们的孩子在五岁前就开始玩电子游戏，而孩子最早接触的三款游戏中有两款是包含大量用户生成内容的《我的世界》和《Roblox》。这意味着UGC正在成为新一代玩家的“入门语言”，而不是成年后才接触的高级玩法。\n\n> **KC评论：** 代际数据往往被低估。当一代人在五岁前就通过UGC游戏建立游戏习惯，他们对“什么是好游戏”的定义会和上一代完全不同。这对所有面向未来五到十年的游戏公司来说，意味着产品\n\n[... middle omitted ...]\n\n你希望获取完整报告原文和更多深度解读，欢迎加入社群继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n游戏行业正在经历一场静悄悄的地壳运动\n\n游戏行业寒冬结束\n\n四个趋势正在重塑未来五到十年的游戏版图\n\nBCG 最新研报，采访了 3000 名玩家后，发现游戏行业正在从“后疫情低谷”里爬出来。增长虽然回不到 2010 年代翻倍的速度，但这次复苏的驱动力很不一样——不是靠单一爆款，而是四个趋势在同时发力，而且它们正在互相碰撞。\n\n1. GenAI 不是来降成本的，是来造洪水的\n研报数据显示，Steam 上已有约 20% 的新游戏标注用了 AI，一年前这个数字只有 10%。但关键不是省了多少钱（虽然 AAA 开发成本能到 3 亿美元），而是 AI 会引发内容大爆发。大量低质量“游戏垃圾”会涌入市场，让“发现好游戏”这件事变得比做游戏本身还重要。\n\n2. UGC 正在从小孩玩具变成主流引擎\n仅 Fortnite 和 Roblox 的创作者生态，2025 年分成就超过 15 亿美元。40% 的玩家说他们比一年前消费了更多 UGC 内容。更值得注意：44% 的玩家父母说，孩子 5 岁就开始玩游戏，而最常玩的前三个游戏里，有两个是 UGC 游戏（Minecraft 和 Roblox）。这等于在给未来十年培养用户习惯。\n\n3\n\n[... middle omitted ...]\n\nGrowth Through Disruption\n24 About the Global Gaming Survey\n24 About the Authors\n\n![](images/12e49fe0b84197cccc04469010a548bda429f8c83ec7d9eaef57bc6e6b7b21fa.jpg)\n\n## Introduction\n\nAs 2025 com\n\n[... middle omitted ...]\n\nvels of the client organization, fueled by the goal of helping our clients thrive and enabling them to make the world a better place.\n\n![](images/5222010d510a5e95ab69501cb00afaa75c4150e60b107da1dc41914c29120e1f.jpg)\n\nBCG"
  },
  {
    "id": "R041",
    "title": "麦肯锡：美国250岁，但真正的考验才刚刚开始",
    "digest": "[wechat_article.md]\n# 麦肯锡：美国250岁，但真正的考验才刚刚开始\n\n美国建国250周年之际，麦肯锡全球研究院发布了一份罕见的长篇报告。这份报告没有停留在庆祝，而是提出了一个让产业决策者必须正视的判断：美国当前的经济竞争力优势，正面临历史性的结构性挑战，而AI时代的到来让这场竞赛的胜负远未落定。\n\n报告的核心主张可以用一句话概括：美国今天仍是全球最具竞争力的经济体，但支撑其250年领先地位的两大基石——创新文化与自然资源禀赋——正在遭遇前所未有的压力。如果美国不能像历史上四次成功转型那样完成第五次自我重塑，其经济领先地位将面临实质性风险。\n\n这并非危言耸听。麦肯锡的数据显示，美国以全球4%的人口创造了26%的GDP，拥有全球市值前100强公司中的59家，贡献了全球27%的研发支出。但与此同时，国家债务持续攀升、基础设施老化、基础教育水平下滑、制造业技能流失、收入与财富差距扩大——这些曾经的优势正在变成负担。\n\n更关键的是，AI正在重塑全球竞争格局。美国目前拥有全球最引人注目的AI模型中的48个，遥遥领先于其他经济体。但报告提醒：技术领先并不自动等于经济竞争力。当中国在制造业产出和出口份额上已经大幅超越美国，当全球供应链正在经历新一轮重构，技术优势能否转化为持续的经济领先，取决于美国能否在能源、基础设施、教育和财政四个维度上同时取得突破。\n\n这份报告的价值不在于告诉读者美国很强——这已是共识。它的真正洞察在于：美国历史上的每一次竞争力跃迁，都不是靠维持现状实现的，而是通过主动打破旧模式、建立新制度完成的。从农业国到工业国，从工业国到科技大国，从科技大国到数字强国，每一次转型都伴随着痛苦的结构性调整。今天，美国正站在第五次转型的起点上。\n\n> **KC评论：** 麦肯锡这份报告最值得关注的不是它对美国现状的肯定，而是它对“优势如何变成负担”的分析。比如，美国过去依赖的廉价能源和广\n\n[... middle omitted ...]\n\n。所有内容都附带原始图表和关键数据，确保信息可追溯、可验证。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n🇺🇸 美国250年：凭什么还是全球第一？\n\n**封面：** 经济霸主炼成记\n\n**副标题：** 4%人口，26%GDP的秘密\n\n---\n\n美国建国250年，今天依然是全球最具竞争力的经济体。\n\n4%的全球人口，创造了26%的全球GDP。全球市值前100的公司，59家在美国。过去几年，美国的生产率加速增长，吸引的绿地外商直接投资比疫情前翻了一倍。\n\n但这份研报的视角很有意思：**它不只是在庆祝，而是在问——下一个250年，还能不能守住？**\n\n**1️⃣ 美国靠什么赢到今天？**\n\n研报给出了两个核心基础：\n- **创新文化**：过去250年全球最重要的100项发明，76项来自美国（从蒸汽船到智能手机，再到生成式AI）\n- **自然资源禀赋**：人均农业用地是其他大经济体的两倍，能源基本自给自足\n\n这两个优势，让美国在不同时代总能找到新的增长方式。\n\n**2️⃣ 但历史优势正在变成包袱**\n\n研报指出几个正在恶化的结构性问题：\n- 财政健康度下滑（国家债务）\n- 基础设施老化\n- 教育成就下降（考试成绩）\n- 制造业技能流失\n- 收入和财富差距持续存在\n\n换句话说，过去帮你赢的东西，如果不管，可能变成拖累。\n\n[... middle omitted ...]\n\nnsey Global Institute was established in 1990. Our mission is to provide a fact base to aid decision making on the economic and business issues most critical to the world's companies and polic\n\n[... middle omitted ...]\n\nany\n\nDesigned by the McKinsey Global Institute\n\nmckinsey.com/mgi\n\nX @McKinsey\\_MGI\n\n@McKinseyGlobalInstitute\n\nin @McKinseyGlobalInstitute\n\nSubscribe to MGI's LinkedIn newsletter,\n\nForward Thinking: mck.co/forwardthinking"
  },
  {
    "id": "R042",
    "title": "麦肯锡：企业最大的风险，是把人才培养当成HR的事",
    "digest": "[wechat_article.md]\n# 麦肯锡：企业最大的风险，是把人才培养当成HR的事\n\n2025年的组织发展正面临一个根本性悖论。一方面，几乎所有CEO都在强调“人才是核心竞争力”；另一方面，当麦肯锡研究团队梳理全球45+份趋势报告后，得出的核心判断却相当尖锐：**大多数企业的学习发展体系仍然停留在“支持功能”层面，而非“战略驱动引擎”。**\n\n这份由麦肯锡研发与创新学习实验室发布的2025年趋势报告，给出了一个值得所有决策者反复咀嚼的结论——在不确定性成为常态的当下，组织真正的竞争优势不在于拥有多少人才，而在于能否构建一个让人才持续生长的“生态系统”。而构建这一生态系统的核心障碍，恰恰是企业内部那些看似合理、实则僵化的部门壁垒。\n\n报告提出了三个相互支撑的宏观趋势：流动的发展生态系统、负责任的人工智能采用、以及个体与组织的韧性与适应力。这三个趋势不是孤立的清单，而是一个必须同时推进的联动系统。其中任何一个环节的缺失，都会导致整体失效。\n\n> **KC评论：** 这份报告最值得关注的不是趋势本身，而是趋势之间的“互锁关系”。很多企业已经在单点发力——有的在推AI学习工具，有的在搞跨部门轮岗，但麦肯锡的研究表明，这些孤立动作的效果有限，因为真正的变革需要学习、技术、文化三条线同时推进。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 72%的企业知道要打破壁垒，但只有11%真正做到了\n\n报告引用了ATD 2023年的一项调查数据：72%的受访者承认，将人力资源转化为跨职能学科至关重要，但只有11%的人表示取得了实质性进展。这个数字本身就是一个值得深思的管理寓言——知道该做什么和真正去做之间，横亘着一道巨大的组织惯性鸿沟。\n\n麦肯锡将这种状态描述为“真实但非根本性的进步”。当前，AI代理正在越来越多地介入即时学习支持——引导实践、辅导任务、支持实时反思。技能\n\n[... middle omitted ...]\n\nAI分析的数据输入，帮助你在第一时间把握全球市场的关键变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n2025职场发展三大关键趋势\n\n职场发展新逻辑\n\n未来工作不再是“培训+干活”两张皮\n\n📌 某外资投行最新研报指出，到2025年，组织发展必须从“反弹”转向“向前跳跃”。核心逻辑是：边界在消失——学习与运营、人与技术、工作与生活，已经无法割裂。\n\n1️⃣ 流动的发展生态\n- 打破HR、L&D、人才管理之间的部门墙\n- 用数据驱动发展决策，不只是追踪课程完成率\n- 72%的企业知道要转型，但只有11%真正在推进\n- 关键：把成长嵌入日常工作，而不是让人停下工作去学习\n\n2️⃣ 负责任地拥抱AI\n- 信任很脆弱，用错AI会毁掉员工信心\n- AI应该做实时导师，而不是替代人类\n- 重点培养员工的高阶技能（批判思维、创造力）\n- 预测：未来5年AI将创造1100万新岗位，同时替代900万\n\n3️⃣ 组织韧性与适应性\n- 不是抵抗变化，而是提前预判、主动适应\n- 多代际员工（Z世代到婴儿潮）的潜力需要被释放\n- 66%的员工正在经历职业倦怠——恢复力=持续竞争力\n- 韧性不是个人责任，而是组织必须共建的系统能力\n\n💡 最打动我的一句话：发展是组织对员工最大的关怀。不是口号，是战略。\n\n欢迎一起讨论——你们公司2025在\n\n[... middle omitted ...]\n\nurring. Roles, systems, and scopes of influence that once seemed defined or distinct – learning vs operations, people vs technology, work vs life – are now interdependent, overlapping, and ine\n\n[... middle omitted ...]\n\npany\n\nLearning Lab By McKinsey 2025\n\nCopyright © McKinsey & Company\n\nDesigned by SJO Design Center\n\nwww.mckinsey.com\n\n@McKinsey\n\n@McKinsey\n\n![](images/d30c7201c6e9cbbc44b1449d1ba7a2d858d1569ee12796967c7c773cf08f8691.jpg)"
  },
  {
    "id": "R043",
    "title": "麦肯锡：2025年最该关注的不是AI本身，而是AI如何让其他技术“活”起来",
    "digest": "[wechat_article.md]\n# 麦肯锡：2025年最该关注的不是AI本身，而是AI如何让其他技术“活”起来\n\n当所有人都在追问“AI还能做什么”的时候，麦肯锡全球研究院在2025年7月发布的《技术趋势展望2025》中给出了一个更值得思考的回答：AI的真正价值不在于它自身的能力边界，而在于它如何成为其他12项前沿技术的“赋能放大器”。这份覆盖13项前沿技术的年度报告传递了一个核心判断——技术竞争已经从“单项突破”进入“组合创新”时代，而AI是那个让组合发生化学反应的催化剂。\n\n报告开篇就亮出了一个反直觉的观察：2024年，尽管宏观环境波动，但13项技术趋势中有10项的股权投资实现了同比增长。更值得注意的是，那些看似“独立”的技术领域——从机器人到生物工程，从能源到空间技术——正在通过AI的嵌入产生前所未有的协同效应。这不是一个关于技术趋势的简单罗列，而是一份关于“技术如何相互赋能”的战略地图。\n\n对于产业决策者而言，真正的挑战不是判断哪项技术最有前景，而是理解这些技术如何组合、在什么场景下产生最大价值、以及自己的企业应该在哪个生态位上布局。麦肯锡报告的价值，恰恰在于提供了这样一个系统性的分析框架。\n\n---\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 股权投资全面回暖，但资金流向揭示了“技术分层”\n\n报告展示了一组关键数据：2024年，13项技术趋势中有10项吸引了比2023年更多的股权投资。其中，能源与可持续发展技术、未来出行两大领域的累计投资额最高，而代理式AI虽然绝对投资额仅为11亿美元，但同比增长了985%，成为增速最快的细分方向。\n\n> **KC评论：** 股权投资数据是判断技术成熟度的“温度计”。2024年的回暖不是简单反弹，而是资金在经历2023年的“挤泡沫”后，开始更有选择地流向两类技术：一类是已经证明有规模化潜力的领域（如清洁能源\n\n[... middle omitted ...]\n\n评分体系和行业案例，是比任何“技术热词”都更有用的决策工具。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI 正在吃掉所有科技趋势\n\n2025 科技趋势全景图\n\n今年某外资投行发布了第五版年度科技趋势报告，覆盖13个前沿技术领域。看完最大的感受：AI不再是单点突破，而是成了所有技术的“放大器”。\n\n几个核心判断值得关注：\n\n1️⃣ AI + 一切 = 新常态\nAI正通过组合其他技术加速落地：训练机器人、推动生物工程发现、优化能源系统。研报明确指出，AI的影响力越来越体现在“与其他趋势的结合”上。\n\n2️⃣ Agentic AI 是最大黑马\n2024年股权融资1.1亿美元，职位需求同比暴增985%。它能自主规划并执行多步骤工作流，像“虚拟同事”一样工作。量级虽小，但增长最快。\n\n3️⃣ 专用芯片迎来爆发\nAI训练和推理对算力、存储、网络的需求呈指数级增长。专利数量激增，新产品和新竞争格局正在形成。\n\n4️⃣ 三大主题贯穿所有趋势\n- 自主系统从试点走向实用\n- 人机协作进入新阶段（从替代到增强）\n- 算力扩张遭遇基础设施瓶颈（电网、供应链、人才）\n\n5️⃣ 投资回暖\n2024年13个趋势中有10个股权融资实现增长。能源与可持续、云与边缘计算、生物工程等领域表现突出。\n\n研报给出三个技术组合案例：\n- 工厂维修：A\n\n[... middle omitted ...]\n\ng)\n\nCompute and connectivity frontiers 26\n03 Application-specific semiconductors 27\n04 Advanced connectivity 34\n05 Cloud and edge computing 41\n06 Immersive-reality technologies 48\n07 Digital t\n\n[... middle omitted ...]\n\nock the investment and coordination required to scale next-generation energy technologies while maintaining affordability and reliability?\n\n![](images/8d8b8ab4e0f252bf0b1a8762dd24679e26276db08f1ecd44793275fca56533c7.jpg)"
  },
  {
    "id": "R044",
    "title": "麦肯锡：88%的企业已在用AI，但81%没看到利润",
    "digest": "[wechat_article.md]\n# 麦肯锡：88%的企业已在用AI，但81%没看到利润\n\n当一家全球咨询巨头在2026年的旗舰报告中，用“双转型”来定义AI时代的组织变革时，它实际上在说一件事：过去三年企业围绕AI的所有碎片化努力，大概率已经走错了方向。\n\n麦肯锡在2026年2月发布的《The State of Organizations 2026》中，基于对超过10,000名全球高管的调研，给出了一个既令人振奋又令人不安的判断。振奋在于，88%的组织已经在至少部分业务中部署AI；不安在于，81%的组织报告称没有看到任何有意义的利润改善。\n\n这不是技术问题。这是组织问题。\n\n这份报告的核心主张是：AI不是插上电源就能用的工具，它要求企业同时完成技术转型和组织转型。而大多数企业只做了前者，忽略了后者。这正是麦肯锡所说的“双转型”命题——企业需要重新想象工作如何完成，重新定义岗位和端到端流程，重新思考传统的组织结构。\n\n> **KC评论：** 88% vs 81% 这个剪刀差是整份报告最值得关注的数字。它意味着AI普及率已经很高，但价值转化率极低。这不仅是技术落地的问题，更指向一个更深层的结构性矛盾：企业的组织形态还没有为AI做好准备。麦肯锡的报告试图回答的就是这个问题——什么变了，以及应该怎么变。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 86%的领导者承认组织对AI准备不足，但只有14%的企业有明确的AI战略\n\n这份报告最反常识的发现之一，是AI采纳率的“虚假繁荣”。表面上，88%的组织在用AI，但深入数据后，麦肯锡发现只有14%的组织有领导者持续推动AI采纳和实验，并配有清晰的战略和行动。更令人担忧的是，每六家组织中就有一家没有明确的C级负责人来推动AI采纳。\n\n这意味着什么？意味着大多数组织的AI部署是分散的、自下而上的、缺乏统一协调的。团队各\n\n[... middle omitted ...]\n\n新数据图表合集，既方便喂给AI，也方便人工快速把握市场动态。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n组织正在被三股力量重塑\n\nAI、地缘、人，都在变\n\n这三股力量正在改写组织规则\n\n某顶级咨询机构最新研报《2026组织现状》显示，全球超10000名高管调研后发现，组织正被三大结构性力量重塑，而且这不是短期波动，是深层次转型。\n\n1️⃣ 技术渗透：AI不是插件，是范式转换\n- 88%的组织已在尝试AI，但81%没看到实质性利润提升\n- 86%的高管觉得自家组织根本没准备好日常用AI\n- 关键卡点：46%担心AI本身，44%顾虑监管/伦理/法律，39%是组织变革管理\n- 真正能赢的组织，会做“双重转型”：技术+组织，重新设计全流程\n\n2️⃣ 经济与地缘不确定性加剧\n- 近3/4受访者表示地缘不确定性已显著影响组织\n- 贸易正向近岸伙伴转移，需构建“弹跳向前”的灵活结构\n- 43%的领导者承认自己资产剥离太晚或该做没做\n- 技术（数字平台、数据分析、AI）可帮助预判风险、重新配置资源\n\n3️⃣ 劳动力格局在变\n- 员工期望、人口结构、技术驱动的工作模式都在变化\n- 领导者需要超越传统结构，重新定义领导力，聚焦绩效\n- 有意思的是：只有20%的领导者认为非金钱激励能驱动员工绩效\n\n📊 几个扎心数据：\n- 72%的领\n\n[... middle omitted ...]\n\n performance edge\n53 Sharpening the focus on diversity and inclusion\n57 Reinventing leadership: Leading from the inside out\n64 Business as change: Managing continuous transformation in the org\n\n[... middle omitted ...]\n\nro, Sasha Goluskin, Scott Brugmans, Tarek Bakali, Tristan Allen, Yueyang Chen, and Zoe Fox.\n\nState of Organizations 2026\nBy McKinsey\nFebruary 2026\nCopyright © McKinsey & Company\n\nwww.McKinsey.com\n\nX @McKinsey\nf @McKinsey"
  },
  {
    "id": "R045",
    "title": "麦肯锡：AI投入的“回报临界点”还没到，但CEO亲自下场是信号",
    "digest": "[wechat_article.md]\n# 麦肯锡：AI投入的“回报临界点”还没到，但CEO亲自下场是信号\n\n这份刚刚发布的麦肯锡全球AI调研报告，覆盖了1491位来自101个国家、全行业、全规模的企业受访者。如果你只记住一个结论，那应该是：**AI真正产生企业级利润影响的比例，至今仍低于20%**。但报告同时释放了一个清晰的信号——那些正在跨越“实验期”、开始看到财务回报的公司，并不是因为技术选对了，而是因为组织方式变了。\n\n这份报告最值得看的判断，不是“AI使用率突破了77%”，而是“CEO亲自监管AI治理，被证明是与利润影响最相关的单一组织变量”。这意味着，AI的竞争已经从技术军备赛，进入到了“组织能力竞赛”阶段。\n\n---\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 真正的分水岭不是技术选型，而是工作流是否被重新设计\n\n麦肯锡在本次调研中测试了25个与AI采用相关的组织属性，并逐一衡量它们与EBIT影响的相关性。结果排在第一位的，不是数据基础设施，不是模型精度，而是**工作流的重新设计**。\n\n报告原文指出：“the redesign of workflows has the biggest effect on an organization's ability to see EBIT impact from its use of gen AI。” 但现实是，只有21%的受访者表示其组织已经从根本上重新设计了至少部分工作流。\n\n这意味着什么？大多数企业仍然在用“旧流程跑新工具”。他们把生成式AI当作一个附加层，贴在原有的营销、客服或研发流程上，而没有去追问：“如果AI可以自动完成这个环节，整个流程应该长什么样？” 这恰恰解释了为什么那么多POC（概念验证）项目做了，但ROI迟迟出不来。\n\n> **KC评论：** 工作流重设计是“组织级AI”与“工具级\n\n[... middle omitted ...]\n\n与原始图表，欢迎加入社群，与我们一同跟踪AI竞争的真实脉搏。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI落地，CEO亲自管才有效\n\nAI落地关键：CEO亲自管\n\n麦肯锡最新调研：大公司AI价值缺口在哪\n\n---\n\n最近读了一份麦肯锡2025年3月发布的AI调研报告，核心发现挺有意思。\n\n**1. 谁在管AI？CEO亲自上阵效果最好**\n\n调研显示，CEO直接负责AI治理的公司，AI带来的EBIT（息税前利润）影响最显著。28%的受访公司由CEO负责AI治理，17%由董事会负责。大公司更倾向让CEO亲自管。\n\n但别误会，AI治理通常是“双领导制”——平均有两位高管共同负责。\n\n**2. 工作流重构比技术更重要**\n\n在所有25个影响AI价值的因素中，工作流重构（重新设计业务流程）对EBIT影响最大。但只有21%的公司真正做到了至少部分工作流重构。\n\n换句话说：很多公司只是买工具，没改流程，价值自然出不来。\n\n**3. 大公司动作更快，但小公司更灵活**\n\n年收入5亿美元以上的大公司，在AI治理、风险缓解、人才招聘上动作更快。但小公司在某些环节（如技术人才集中管理）反而更倾向于完全集中化。\n\n**4. 风险管控在升级**\n\n相比2024年初，更多公司开始主动管理AI风险，尤其是：\n- 不准确性（AI胡说八道）\n\n[... middle omitted ...]\n\nf555ae093dc404956428b0.jpg)\n\norganizations are starting to make organizational changes designed to generate future value from gen AI, and large companies are leading the way. The latest McKins\n\n[... middle omitted ...]\n\nh 2025  \nCopyright © McKinsey & Company  \nDesigned by McKinsey Global Publishing\n\nFind more content like this on the McKinsey Insights App\n\n![](images/0458fb11ffa1d85bf517ff96c548eb51a4025c0b79a6af63c0bcb79633e51bd1.jpg)"
  },
  {
    "id": "R046",
    "title": "波士顿咨询：CEO的AI使用方式，正在成为公司竞争力的分水岭",
    "digest": "[wechat_article.md]\n# 波士顿咨询：CEO的AI使用方式，正在成为公司竞争力的分水岭\n\n大部分CEO已经意识到AI的重要性，但真正从中获得价值的比例低得惊人。波士顿咨询（BCG）在2026年6月发布的一份面向CEO群体的研究报告，给出了一个看似反直觉的核心判断：**决定一家公司AI转型成败的关键，不是战略文件写了什么，而是CEO本人每天如何使用AI。** 这份报告基于对15位高知名度CEO的公开案例研究，以及一项覆盖1488名美国全职工作者的调查，揭示了CEO个人AI使用习惯与公司整体AI价值创造之间的强关联——但结论远比“多用AI”复杂得多。在72%的CEO已直接负责公司AI决策的今天，只有15%的人正在从AI中创造有意义的商业价值。这中间的巨大落差，恰恰是这份报告最值得深挖的地方。\n\n报告抛出的核心洞察是：**当AI被设计用于放大CEO本人最稀缺的两种资源——时间和判断力时，其价值回报远高于仅将其部署在组织中下层提升效率。** 这意味着，CEO对AI的认知与使用方式，正在从“个人效率工具”升级为“最高决策质量的放大器”，而这将直接决定公司在不确定性中的战略敏捷度。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. CEO亲自使用AI的信号价值，远超任何战略文件\n\nBCG的研究发现，当CEO本人公开、高频地使用AI时，这本身就是一个强大的组织信号。它比任何演讲或战略文件都更有效：它激励管理层和员工更大胆地尝试AI，明确告诉整个高管团队AI是每个人的职责，而非某个部门的项目。报告提供的数据支撑了这一判断：在识别出的“先行者”CEO群体中，一个显著特征是**他们每周至少花8小时构建自身的AI能力**——不是监督别人用AI，而是自己动手。\n\n但BCG特别强调，时间本身不是价值创造的原因。真正重要的是CEO如何使用AI。在分析了15位高知名度CEO的\n\n[... middle omitted ...]\n\n与数据图表的每日简报，帮助决策者快速把握市场动态与前沿趋势。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nCEO如何让AI放大判断力，而非替代自己\n\nAI放大CEO判断力\n\n投行研报指出，CEO们已开始用AI来快速掌握新领域、处理信息洪流、测试假设、发现团队不敢说的风险。但真正的高手，是用AI放大自己最稀缺的资源：时间和判断力。\n\n1/ 真正用AI的CEO，只有15%创造了价值\n研究显示，72%的CEO直接负责AI决策，但仅15%从中获得显著价值。这些先锋CEO每周至少花8小时打磨自己的AI能力。关键不是时长，而是如何用、用来做什么。\n\n2/ CEO用AI的6种常见方式\n- 快速学习新领域，准备高难度对话\n- 压缩信息、挑战假设、指出风险（AI可以当“魔鬼代言人”）\n- 把模糊想法变成清晰表达，比如起草股东信\n- 用AI回顾日程和邮件，看时间是否花在重点上\n- 测试战略决策，给不同方案分配概率\n- 发现团队不敢提的问题，打破信息茧房\n\n3/ 前沿趋势：定制化AI代理系统\n通用工具只是起步。未来属于为CEO量身打造的AI代理系统，能根据其决策模式、战略背景、沟通风格来工作。比如，在会议前就完成信息整合、风险预警、方案推演，让CEO进会议室时已准备好做决策，而不是刚被“科普”。\n\n4/ 4个CEO必须警惕的AI\n\n[... middle omitted ...]\n\nnior team may be reluctant to raise, and manage their schedules more strategically.\n\nWhile early AI use cases like these confer real benefits for an organization by expanding a CEO's understan\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R047",
    "title": "波士顿咨询：Fintech已过“幸存者考验”，下一轮赢家靠的是“规模议价权”",
    "digest": "[wechat_article.md]\n# 波士顿咨询：Fintech已过“幸存者考验”，下一轮赢家靠的是“规模议价权”\n\n全球金融科技行业在经历了2023至2024年的估值修正与资本寒冬之后，于2025年交出了一份令市场重新审视其价值的答卷。波士顿咨询与FT Partners联合发布的《2026全球金融科技报告》明确指出，这个行业已经完成了从“恢复”到“复兴”的切换。但这份报告最值得关注的判断，并非简单的营收数字回暖，而是一个更深层的结构性信号：行业增长的动力源正在发生根本性迁移。过去，增长靠的是“数字原生”对“传统低效”的替代红利；现在，增长的门槛已经抬高到“能否将规模转化为系统性的议价权”。这不是一场所有参与者都能共享的复苏。\n\n这份报告的核心论据是，2025年全球金融科技总收入突破5000亿美元，同比增长22%，增速是传统金融机构的4倍以上。然而，在这些光鲜的平均数之下，隐藏着一个正在加速分化的行业格局。头部玩家的盈利能力正在显著改善，而中尾部公司面临的资本筛选却比以往任何时候都更加严酷。这意味着，金融科技行业正从一个“由资本驱动的增长故事”，转向一个“由运营效率和规模壁垒定义的成熟市场”。对于产业决策者和高净值投资者而言，理解这种分化的内在逻辑，远比关注行业总规模的增长数字更具战略价值。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 资本不再“普惠”，而是向“确定性”集中，这重塑了竞争格局\n\n报告中最具说服力的证据之一，是资本流向的结构性变化。2025年全球金融科技股权融资总额达到580亿美元，同比增长53%，看似市场热情回归。但深入观察融资轮次分布，会发现一个截然不同的故事：从2023年到2025年，E轮及以后的晚期融资增长了超过210%，而种子轮和天使轮融资却收缩了约10%。A轮和B轮的增长也仅为15%和30%，远不及晚期阶段的爆发力。\n\n这意味\n\n[... middle omitted ...]\n\nAI模型，也方便你快速把握市场脉动，做出更有信息支撑的决策。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球金融科技，正在经历一场硬核复苏\n\n金融科技，走出低谷\n\n2025年全球金融科技收入首次突破5000亿美元，增速是传统金融机构的4倍多。\n\n1️⃣ 规模与盈利双升\n全球金融科技收入达5040亿美元，同比增长22%。头部85家上市金融科技公司中，74%已实现盈利，平均EBITDA利润率提升4个百分点至20%。这不是靠烧钱换增长，是实打实的运营改善。\n\n2️⃣ 资本回归但更挑剔\n2025年金融科技股权融资580亿美元，同比增长53%。但资金集中流向交易与投资板块，占总额约1/3。IPO数量从28家增至42家，M&A交易规模达2510亿美元。投资者不再追逐故事，只奖励有清晰盈利路径的公司。\n\n3️⃣ 区域分化明显\n亚太增长最快（25%），日本、韩国、东南亚的加密和数字银行是主要推手。欧洲（24%）受益于更清晰的监管环境。拉美虽增速15%但自2021年起复合增长率达44%，后劲十足。\n\n4️⃣ 金融普惠是真实战场\n巴西Pix推出一年后覆盖67%成人，印度UPI月交易量超200亿笔，肯尼亚M-PESA服务约80%适龄人口。金融科技在新兴市场正从边缘工具变成基础设施。\n\n5️⃣ AI落地还需时间\nAI是当前最重要技术主\n\n[... middle omitted ...]\n\n trading and investments and deposits leading the pack with about 38% and 30% YoY growth, respectively\n\n400bps\n\nAverage EBITDA margin improvement for the largest public fintechs from 2024 to 2\n\n[... middle omitted ...]\n\nbillion valuation.\n\n![](images/5208938f8aac64690ee682cdf49cfa96b3939091639a16bfe9980e8ccf39088f.jpg)\n\nBCG +\n\nFINANCIAL TECHNOLOGY PARTNERS\n\n![](images/b3e517083cc6425278ea17bb2538e0b674db9c9074c0172d5cbc3260759a241a.jpg)"
  },
  {
    "id": "R048",
    "title": "波士顿咨询：BCG：美国财险市场最危险的信号不是费率走软，而是承保能力断层",
    "digest": "[wechat_article.md]\n# 波士顿咨询：BCG：美国财险市场最危险的信号不是费率走软，而是承保能力断层\n\n美国财产与 casualty 保险市场正在经历一个微妙的转折点。波士顿咨询在最新发布的《2026年保险价值创造者报告》中给出了一组值得认真拆解的数据：2021至2025年间，美国财险公司的五年平均年度总股东回报率约为18%，跑赢全球保险业均值15%，也跑赢了大多数其他行业。但2025年的单年数据已经显露出明显的减速迹象——美国保险公司的TSR正在被欧洲和亚太同行追赶。\n\n这份报告的真正价值不在于这些数字本身，而在于它揭示了一个正在加速的结构性分化：行业头部与尾部的差距正在拉大，而且这一次的分化逻辑与过去几轮周期有本质区别。\n\n最直接的主判断是：美国财险市场已经告别了单纯靠费率上涨就能改善承保结果的时代。那些在硬市场中依赖提价来维持盈利的保险公司，现在必须用数据、细分和费用纪律来证明自己的承保能力。这不是一个周期性的调整，而是一个能力门槛的系统性抬升。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 承保利润才是真正的分水岭，投资收入正在掩盖一个危险的假象\n\n波士顿咨询的分析跨越了多个五年周期，结论始终一致：承保业绩是区分领先者和落后者的核心指标。在2021至2025年这个周期里，表现最好的四分之一财险公司，其承保业务对有形股本回报率的贡献约为11个百分点；而表现最差的四分之一公司，承保贡献为负值。\n\n这个差距本身并不令人意外。真正值得关注的是：2024至2025年间，较高的净投资收益部分掩盖了弱势保险公司的承保恶化。换句话说，当利率正常化、投资收益回落之后，承保质量将成为区分盈利能力的唯一变量。\n\n> **KC评论：** 这意味着，当前很多保险公司的财报数字可能比实际经营状况更好看。投资者如果只看ROE而不拆解承保和投资的贡献比例，很容易高估\n\n[... middle omitted ...]\n\n以及更多未在本文中展开的二阶判断感兴趣，欢迎加入我们的讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美国财险：好日子结束了？\n\n市场正在切换，赢家通吃\n\n正文👇\n\n某外资投行刚发了2026年保险价值创造报告，核心判断：美国财险市场正在从“硬市场”转向“软市场”，保费增速放缓，但成本压力没降。\n\n1/ 定价红利在退潮\n过去几年靠连续涨保费改善承保结果的公司，现在必须靠数据、细分和费用管控来赚钱。费率上涨的空间正在收窄，尤其是个人车险和商业财产险。\n\n2/ 承保能力才是分水岭\n报告分析2021-2025年数据，前25%的公司承保端贡献了约11%的有形股本回报率，后25%是负贡献。投资收入高的时候还能掩盖差距，等利率正常化，承保质量就是唯一的分水岭。\n\n3/ 个人车险已从防守转进攻\n到2025年，个人车险综合成本率从2022年的112%降到92%，是2004年以来最好水平。但恢复不均衡——Progressive率先调价，2025年综合成本率约88%，已做到全美第一。其他公司还在修补期。\n\n4/ 屋主险是下一个主战场\n2025年屋主险综合成本率88%，是2006年以来最好。但主要原因是没大飓风，不是结构性改善。野火、强对流风暴（SCS）损失已超飓风，2023-2025年每年SCS保险损失超500亿美元（之前十年年均\n\n[... middle omitted ...]\n\ne cost of losses, driven by such factors as social inflation, severe convective storms (SCSs), and elevated claims severity, remains high. The result is a more complex operating\n\nenvironment i\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R049",
    "title": "波士顿咨询：5%的公司正在拉大AI价值鸿沟，其余95%面临被锁定的风险",
    "digest": "[wechat_article.md]\n# 波士顿咨询：5%的公司正在拉大AI价值鸿沟，其余95%面临被锁定的风险\n\nAI投资的回报正在出现一个令人不安的分化。波士顿咨询公司（BCG）在2025年对全球超过1250家企业的研究显示，只有5%的公司真正从AI中获得了可观的商业价值。这5%的企业，BCG称之为“未来构建者”，不仅在营收增长和EBIT利润率上显著领先，更关键的是，他们正在利用AI回报进行再投资，形成一个加速的价值创造循环。而其余95%的公司，尤其是60%几乎没有看到任何实质性回报的企业，正面临被锁定在“落后循环”中的风险。\n\n这份报告最值得关注的判断不是AI是否有价值，而是价值正在被极少数公司加速收割。这种差距不是线性的，而是指数级的。它意味着，对于大多数企业决策者而言，现在的核心问题已经不是“要不要投AI”，而是“如何避免被越甩越远”。\n\nBCG的报告提供了一个清晰的路线图，但同时也提出了一个尖锐的问题：在AI技术，特别是代理型AI加速迭代的当下，你的组织是否有能力在12-18个月内完成从“实验”到“重塑”的跨越？\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 真正的价值鸿沟不在技术，而在“未来构建者”的五项战略能力\n\nBCG将企业AI成熟度划分为四个层次：未来构建者（5%）、扩展者（35%）、新兴者（46%）和停滞者（14%）。未来构建者与其他企业的差距是全方位的：营收增长是后者的1.7倍，三年股东总回报是3.6倍，已动用资本回报率是2.7倍。这些数字不是来自某个AI试点项目，而是来自整体业务运营的系统性改变。\n\n这些领先企业并非拥有更先进的算法或更多的GPU。他们的优势在于五项相互关联的战略能力：清晰的多年期AI愿景、以冲击力为导向的业务重塑、AI优先的运营模式、人才保障策略，以及灵活的技术与数据架构。这五项能力共同构成了一个飞轮：愿景驱动资源\n\n[... middle omitted ...]\n\n方便喂给AI模型，也方便人工快速把握市场动态。欢迎加入讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI价值差距正在拉大\n\n只有5%的公司真正赚到钱\n\n你还在AI上烧钱吗？BCG最新报告说真相了\n\n最近读了BCG的2025年AI价值报告，发现一个扎心的现实：AI的价值差距正在急剧拉大。\n\n1️⃣ 只有5%的公司真正赚到了钱\n- 60%的公司投入了大量资金，但几乎没看到回报\n- 35%的公司正在努力追赶，但很多承认自己“走得太慢”\n- 只有5%的“未来型”公司实现了AI规模化价值\n\n2️⃣ 未来型公司到底做对了什么？\n- 收入增长是普通公司的1.7倍\n- 息税前利润率是1.6倍\n- 三年股东总回报是3.6倍\n- 专利数量是3.5倍\n\n3️⃣ 70%的价值集中在核心业务\n- 销售、制造、供应链、定价这些核心职能\n- R&D和创新的潜力占15%\n- IT部门的价值占比从2024年的7%飙升至13%\n\n4️⃣ AI代理正在加速差距\n- 2024年几乎没人谈代理型AI\n- 2025年已占AI总价值的17%\n- 预计2028年将达到29%\n\n5️⃣ 领先公司的5个关键策略\n- 制定多年战略愿景\n- 重塑核心流程而非小打小闹\n- 建立AI优先的运营模式\n- 大规模培训员工（超过50%的员工）\n- 构建灵活的技术栈和数据基\n\n[... middle omitted ...]\n\nctor and Region\n\n11 What Value Generators Do Differently\n• Pursue a Multiyear Strategic AI Ambition\n• Reshape and Invent with Impact\n• Adopt an AI-First Operating Model\n• Secure and Enable the\n\n[... middle omitted ...]\n\nalerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on LinkedIn, Facebook, and X (formerly Twitter).\n\n![](images/1d7bfc57d3a1e9ad701ad9cbe653c75cfee078efb6aa3451e45868acc2c36836.jpg)\n\nBCG"
  },
  {
    "id": "R050",
    "title": "波士顿咨询：游戏行业“冬季”结束，但增长逻辑已彻底改变",
    "digest": "[wechat_article.md]\n# 波士顿咨询：游戏行业“冬季”结束，但增长逻辑已彻底改变\n\n2025年底，游戏行业终于可以松一口气。波士顿咨询（BCG）在其最新发布的《视频游戏报告2026》中给出了一个明确的判断：持续三年的“游戏寒冬”即将结束，行业正进入一个更加乐观的新阶段。但这份报告真正值得关注的，不是复苏本身，而是复苏背后的结构性变化——旧有的平台战争、开发规则和分发模式正在失效，游戏行业即将迎来一次彻底的洗牌。\n\n这份基于近3000名玩家调研和大量行业访谈的报告，提出了一个核心主张：未来五到十年，四大趋势将同时发力，推动游戏行业进入一个“平台碰撞”的新时代。增长会回来，但不会回到2010年代翻倍的速度。真正的问题在于，谁能在新规则下重新定义自己的位置。\n\n> **KC评论：** 报告的核心洞察不是“行业回暖”，而是“回暖的方式和过去完全不同”。如果你是产业决策者或投资者，关注点应该从“行业增速多少”转向“价值池如何重新分配”。这份报告最值得细读的部分，是它对四个趋势如何互相叠加、改变竞争格局的分析。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 云游戏不再是概念，而是引爆平台战争的导火索\n\nBCG报告中最具冲击力的判断之一，是“主机战争正在变得无关紧要”。当云游戏走向主流，硬件不再是竞争壁垒，真正的战场将转移到“生态系统”层面——谁能提供跨屏幕、跨设备的无缝体验，谁就能赢。\n\n数据支撑了这一判断：60%的受访玩家尝试过云游戏，其中80%给出了正面评价。报告预测，云游戏收入将从2025年的约15亿美元，以超过60%的年复合增长率在2030年达到一个完全不同的量级。这意味着，玩家将不再受限于PlayStation、Xbox或Switch的硬件绑定，而是可以在电视、手机、平板甚至浏览器上自由切换。\n\n对主机厂商而言，这是一个严峻的挑战。硬件销售本身\n\n[... middle omitted ...]\n\n或消费行业的结构性变化，欢迎加入社群，一起讨论这些未解问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n游戏行业正迎来下一波增长\n\n游戏行业加速回暖\n\n刚刚读完BCG最新的游戏行业报告，几个核心发现值得关注。\n\n游戏行业正从三年寒冬中复苏，增长开始回暖。虽然不会回到2010年代翻倍的高增速，但方向已经明确。\n\n1️⃣ 玩家基本盘在扩大\n约55%的玩家过去半年游戏时间增加。\n更有意思的是，44%的家长会在孩子5岁前就让他们接触游戏，且最受欢迎的前三款入门游戏中有两款是UGC游戏：Minecraft和Roblox。\n这直接说明下一代玩家正在被培养。\n\n2️⃣ 四大趋势正在重塑行业\n- 生成式AI：25年约20%的新游戏披露使用AI，比前一年翻倍。AI不仅能降本，还能催生新玩法。\n- UGC创作者经济：仅Fortnite和Roblox两个平台，25年对创作者的支付将超15亿美元。\n- 云游戏：60%的玩家尝试过云游戏，80%体验正面。\n- 应用商店开放：开发者将拥有更低的抽成和更大的分发自主权。\n\n3️⃣ 平台战争正在转移\n从原来的主机大战，转向基于云游戏技术的生态系统竞争。\n玩家越来越不在乎设备，只在乎体验能否跨屏延续。\n谁能做好社区运营、算法推荐和订阅/内购模式，谁就能胜出。\n\n4️⃣ 关于AI的一点观察\n虽然玩\n\n[... middle omitted ...]\n\nGrowth Through Disruption\n24 About the Global Gaming Survey\n24 About the Authors\n\n![](images/12e49fe0b84197cccc04469010a548bda429f8c83ec7d9eaef57bc6e6b7b21fa.jpg)\n\n## Introduction\n\nAs 2025 com\n\n[... middle omitted ...]\n\nvels of the client organization, fueled by the goal of helping our clients thrive and enabling them to make the world a better place.\n\n![](images/5222010d510a5e95ab69501cb00afaa75c4150e60b107da1dc41914c29120e1f.jpg)\n\nBCG"
  },
  {
    "id": "R051",
    "title": "麦肯锡：美国250年的竞争力，正被三个“历史负债”侵蚀",
    "digest": "[wechat_article.md]\n# 麦肯锡：美国250年的竞争力，正被三个“历史负债”侵蚀\n\n美国建国250年，至今仍是全球最具竞争力的经济体。它拥有全球26%的GDP，59家全球百强企业，以及超过一半的全球市值。在AI、生物科技、半导体设计等前沿领域，美国依然牢牢占据制高点。过去几年，美国的生产率增速和宣布的外国直接投资（FDI）流入量，甚至拉大了与其他发达经济体的差距。\n\n这份来自麦肯锡全球研究院（MGI）的250周年纪念报告，本可以是一场盛大的自我庆祝。但它选择了一条更诚实也更尖锐的路径：在肯定成就的同时，明确指出美国正站在一个必须“再次进化”的十字路口。\n\n报告的核心判断是：美国历史上赖以成功的两项基石——创新文化与自然资源禀赋——依然存在，但支撑这些基石的制度、基础设施和人力资本正在老化。一些曾经的竞争优势，正在变成结构性负债。如果美国不能像过去四次那样（农业、工业、科学、数字时代）完成经济模式的又一次转型，其全球竞争力将面临实质性侵蚀。\n\n这不是一个关于“美国衰落”的叙事。这是一份关于“领先者如何失去领先”的冷静预警。\n\n> **KC评论：** 麦肯锡这份报告最有价值的部分，不是它证明了美国有多强，而是它量化了“保持领先需要付出多大代价”。它提出了一个对全球投资者和产业决策者都至关重要的框架：一个经济体的竞争力，不是静态的排名，而是动态的“适应能力”。当AI、地缘冲突和人口结构同时发生巨变时，美国过去四次的成功转型，恰恰是它未来最大的不确定性来源。完整报告里有一张关于“四次历史转型”的详细图表，非常值得仔细看。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 这轮变化真正考验的是企业能否把规模转化为议价权\n\n美国企业的全球领先地位，是报告首先确认的事实。在全球百强企业（按市值计）中，美国占据了59席。在AI私人投资总额上，美国2024年达到1\n\n[... middle omitted ...]\n\n。\n\n你可以在这里，和我们一起，追踪美国竞争力的下一个拐点。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美国经济250年：凭什么一直领先？\n\n美国经济竞争力密码\n\n4%人口，26%全球GDP，59%全球百强企业\n\n你猜美国用了什么魔法，250年还能保持全球竞争力？\n\n上周读了麦肯锡全球研究院的最新报告，越来越觉得美国经济模式值得研究。来拆解一下核心逻辑👇\n\n**1/ 创新是超强引擎**\n- 过去250年，全球100项最重要发明中，76项由美国人创造或支持\n- 从蒸汽船到智能手机，从电网到生成式AI\n- 美国研发支出占全球27%，AI私人投资1091亿美元（2024年）\n\n**2/ 资源禀赋得天独厚**\n- 人均农业用地是其他大经济体的2倍\n- 能源自给自足长达200年（2019年后再次实现）\n- 这些“家底”让美国在危机中更有韧性\n\n**3/ 但历史优势正在变成包袱**\n- 财政健康状况恶化，国家债务持续攀升\n- 基础设施老化，教育成绩下滑\n- 制造业技能流失，收入与财富差距扩大\n- 这些“遗产”如果不解决，会拖累未来竞争力\n\n**4/ 下一个篇章怎么走？**\n报告认为美国需要集体行动：\n- 确保能源充足\n- 重建基础设施\n- 教育要匹配新技术\n- 财政要有可持续性\n\n美国历史上已经经历了农业、工业、科学、数字\n\n[... middle omitted ...]\n\nnsey Global Institute was established in 1990. Our mission is to provide a fact base to aid decision making on the economic and business issues most critical to the world's companies and polic\n\n[... middle omitted ...]\n\nany\n\nDesigned by the McKinsey Global Institute\n\nmckinsey.com/mgi\n\nX @McKinsey\\_MGI\n\n@McKinseyGlobalInstitute\n\nin @McKinseyGlobalInstitute\n\nSubscribe to MGI's LinkedIn newsletter,\n\nForward Thinking: mck.co/forwardthinking"
  },
  {
    "id": "R052",
    "title": "麦肯锡：2025年，企业最大的风险不是AI，而是把学习当作“福利”",
    "digest": "[wechat_article.md]\n# 麦肯锡：2025年，企业最大的风险不是AI，而是把学习当作“福利”\n\n**主判断：** 麦肯锡最新研报指出，全球企业的学习与发展（L&D）正站在一个“从支持功能到战略引擎”的转折点上。但真正的危机不是技术追赶不上，而是绝大多数组织仍然用过去20年的框架来应对未来5年的变化。报告提出的“流体发展生态系统”不是又一个HR概念，而是决定组织能否在AI时代留住核心人才、实现韧性增长的关键变量。\n\n这份由麦肯锡研究与创新学习实验室发布的2025年趋势报告，基于对45+全球趋势报告的系统分析，给出了一个反直觉的判断：**当AI代理开始扮演实时导师、当技能半衰期缩短至2-3年，企业最大的瓶颈不是技术采购，而是组织内部根深蒂固的职能孤岛和短视的规划周期。**\n\n以下是我们从这份报告中提炼的五个核心洞察，以及它们对产业决策者的实际含义。\n\n> **KC评论：** 很多企业老板现在焦虑的是“AI会不会取代我的员工”，但麦肯锡的结论更尖锐——问题不是AI取代人，而是你的组织根本没有准备好让员工在AI时代持续成长。61%的企业只做一年的人力规划，这本质上是在用“打补丁”的方式应对“换系统”的挑战。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 学习与工作的边界正在消失，但多数企业还停留在“脱产培训”的旧模式\n\n报告提出了一个关键概念：“流体发展生态系统”。这不是一个学术术语，而是一个操作框架。它的核心主张是：**未来的发展不应该让员工“停下工作去学习”，而是让工作本身成为发展的引擎。**\n\n当前阶段，报告称之为“真实但非激进的进步”。AI代理开始扮演实时指导角色，技能验证正在从自我报告转向更完整的数据画像。但学习仍然被感知为“需要专门抽时间去做的事”，而非自然嵌入工作流的一部分。\n\n真正的问题在于组织结构的惯性。报告引用ATD 2023年调\n\n[... middle omitted ...]\n\n既方便喂给AI进行二次分析，也适合人工快速把握全球市场动态。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n2025人才发展三大趋势，HR必看\n\n人才发展新逻辑\n\n未来工作不是“学完再做”，而是“边做边学”\n\n某外资投行2025研报指出，全球人才发展正在经历根本性转变，三大趋势互相强化、缺一不可👇\n\n1️⃣ 流动式发展生态\n- 学习与工作不再分家，AI教练实时指导\n- 72%企业知道要打破HR/L&D部门墙，但仅11%有实质进展\n- 数据驱动决策：从追踪课程完成率→预测技能缺口\n\n2️⃣ 负责任AI采纳\n- 信任是核心资产，用错AI会摧毁员工信心\n- 人类+AI协作：不是替代，是升级高阶技能\n- 75%员工已在工作中使用AI（LinkedIn 2024数据）\n\n3️⃣ 组织韧性与适应力\n- 不是“反弹回原状”，而是“弹向更高处”\n- 39%现有技能将在2025-2030年被淘汰或重构（WEF报告）\n- 代际差异≠问题，多样性能解锁更大潜力\n\n💡 关键启示：把员工发展看作“关怀行为”，韧性与适应力是共同责任，变革不是未来状态而是永久常态。\n\n#学习笔记\n\n[source_mineru.md]\nReimagined:\n\n# Development in the Future of Work\n\n2025 Perspect\n\n[... middle omitted ...]\n\nurring. Roles, systems, and scopes of influence that once seemed defined or distinct – learning vs operations, people vs technology, work vs life – are now interdependent, overlapping, and ine\n\n[... middle omitted ...]\n\npany\n\nLearning Lab By McKinsey 2025\n\nCopyright © McKinsey & Company\n\nDesigned by SJO Design Center\n\nwww.mckinsey.com\n\n@McKinsey\n\n@McKinsey\n\n![](images/d30c7201c6e9cbbc44b1449d1ba7a2d858d1569ee12796967c7c773cf08f8691.jpg)"
  },
  {
    "id": "R053",
    "title": "麦肯锡：AI不再独自奔跑，2025年最值得关注的不是大模型本身",
    "digest": "[wechat_article.md]\n# 麦肯锡：AI不再独自奔跑，2025年最值得关注的不是大模型本身\n\n当全球科技圈还在为GPT-5的参数规模争论不休时，麦肯锡2025年技术趋势报告给出了一个更冷静的判断：**AI的价值正在从“模型有多大”转向“系统有多聪明”。**\n\n这不是一份罗列13项技术的清单。它的核心主张是：2025年，技术竞争的本质不再是单项技术的突破速度，而是不同技术之间的“组合能力”。AI不再是孤立的浪潮，而是成为所有前沿技术的“放大器”——它加速机器人训练、推动生物工程科学发现、优化能源系统，甚至在改变半导体设计的底层逻辑。\n\n这份报告最值得留意的信号，不是哪项技术排名上升，而是**一个全新的技术趋势首次进入麦肯锡的视野，并以“增长最快”的姿态出现**。这个趋势的量化指标在2023到2024年间增长了985%，但很多人对它还停留在概念阶段。\n\n---\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 985%的增长背后，一个“虚拟同事”时代正在开启\n\n2024年，全球对“Agentic AI”的股权投资达到11亿美元。这个数字放在AI领域并不算大——与通用AI动辄数百亿美元的投资相比，它只是冰山一角。但真正值得注意的，是它的增长速度：**同比增长985%**。\n\n麦肯锡将Agentic AI定义为“结合了AI基础模型的灵活性与通用性，同时具备在现实世界中行动能力”的技术。它的核心产品形态是“虚拟同事”——能够自主规划并执行多步骤工作流的AI代理。\n\n这意味着什么？传统的AI应用是“你问它答”，即便是最先进的ChatGPT，本质上也是被动响应。而Agentic AI的突破在于，它开始具备“主动规划”的能力：当一个工厂机器出现故障，AI代理可以自主诊断问题、制定维修计划、协调零部件采购，并监督质量检查——整个过程几乎不需要人类介入。\n\n> **K\n\n[... middle omitted ...]\n\n方便你在30分钟内把握全球资本市场的技术投资动向。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n2025科技趋势：AI正成为“超级放大器”\n\nAI革命才刚刚开始\n\n某外资投行刚发布了2025科技趋势报告，看完只想说：AI正在重塑一切。\n\n1/ AI不只是趋势，它是所有趋势的“加速器”\n- AI+机器人 = 更聪明的工厂\n- AI+生物工程 = 加速新药研发\n- AI+能源 = 优化电网调度\nAI正在从“独立技术”变成“基础能力”，渗透到每个领域。\n\n2/ 智能体AI正在崛起\n2024年智能体AI的股权投资已达11亿美元\n岗位招聘量同比暴增985%\n它能自主规划、执行多步骤任务，相当于有了“虚拟同事”\n\n3/ 芯片需求暴涨\nAI训练需要海量算力，催生专用芯片爆发\n专利数量激增，新玩家、新生态正在形成\n\n4/ 三大关键趋势值得关注\n- 自主系统从试点走向落地\n- 人机协作从替代转向增强\n- 基础设施面临算力、电力、供应链三重挑战\n\n5/ 投资回暖明显\n2024年，13个科技趋势中有10个股权投资增长\n能源与可持续、云计算、生物工程领跑\n\n最让我兴奋的是：这些技术的组合效应远大于单个技术。比如工厂维修=AI诊断+智能体规划+机器人执行，三者协同，效率翻倍。\n\n你们觉得哪个组合最值得关注？欢迎一起讨论\n\n#学习\n\n[... middle omitted ...]\n\ng)\n\nCompute and connectivity frontiers 26\n03 Application-specific semiconductors 27\n04 Advanced connectivity 34\n05 Cloud and edge computing 41\n06 Immersive-reality technologies 48\n07 Digital t\n\n[... middle omitted ...]\n\nock the investment and coordination required to scale next-generation energy technologies while maintaining affordability and reliability?\n\n![](images/8d8b8ab4e0f252bf0b1a8762dd24679e26276db08f1ecd44793275fca56533c7.jpg)"
  },
  {
    "id": "R054",
    "title": "麦肯锡：88%企业在试AI，但81%没赚到钱",
    "digest": "[wechat_article.md]\n# 麦肯锡：88%企业在试AI，但81%没赚到钱\n\n当全球超过一万名企业高管被问及“你的组织准备好迎接未来变化了吗”，72%的回答是“没有完全准备好”。即使在那些对未来持乐观态度的领导者中，也只有三分之一认为自己做好了准备。\n\n这是麦肯锡在2026年2月发布的《组织现状》报告中揭示的核心矛盾。这份基于15个国家、16个行业、超过10,000名高管反馈的第二版研究，试图回答一个根本问题：在AI、地缘裂变和劳动力结构三重巨变同时发生的时代，什么样的组织才能真正持续创造价值？\n\n答案并不令人意外，但执行路径远比想象中复杂。报告的核心判断是：组织的重心已从短期韧性转向长期生产力与持续价值创造，而AI是这场转型的技术底座。但真正值得关注的不是这个结论本身，而是麦肯锡在数据中发现的巨大落差——88%的组织在尝试AI，81%没有看到有意义的利润改善。这中间的7个百分点，正是当下最值得拆解的谜题。\n\n---\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 技术投入与组织能力之间的错配，才是AI落地最大的隐形障碍\n\n麦肯锡的调查揭示了一个反直觉的现象：AI落地的头号障碍并非技术本身，而是组织层面的挑战。当被问及采用AI的主要障碍时，46%的高管提到对AI本身的担忧，44%提到监管、伦理或法律问题，39%指向包括变革管理在内的组织挑战。\n\n但更深层的数据是：86%的领导者认为自己的组织对在日常运营中采用AI“没有准备好”。更值得注意的是，六分之一的组织没有明确的C级负责人来推动AI采用。只有14%的组织有领导者持续倡导AI采用和实验，并制定了清晰的策略和行动。\n\n这意味着，大多数组织的AI战略停留在“有想法、缺执行”的阶段。技术采购可能已经完成，但谁来推动、如何推动、推动后如何评估效果，这些最基本的组织问题尚未解决。\n\n> **KC评论：**\n\n[... middle omitted ...]\n\n们也会围绕这份报告中未完全解答的变革节奏问题，组织专题讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n组织正在经历三股重塑力量，你的公司准备好了吗？\n\n**组织变革进行时**\n\n某外资投行最新研报显示，超过10,000名全球高管反馈，组织正在被三股力量重塑，而72%的领导者承认组织尚未完全准备好应对变化。\n\n**三大重塑力量**\n\n1️⃣ **技术变革**\n88%的组织已在尝试AI，但81%尚未看到实际收益。86%的领导者认为组织尚未准备好将AI融入日常运营。真正的机会在于“双重转型”——技术转型+组织转型并行。\n\n2️⃣ **经济不确定**\n近3/4受访者表示地缘政治不确定性已显著影响组织。43%的领导者承认资产剥离过晚或未及时行动。组织需要建立深层灵活性，从“反弹”到“向前弹”。\n\n3️⃣ **劳动力变化**\n员工期望、人口结构、技术驱动的工作模式正在重塑劳动力。只有20%的领导者认为非金钱激励能激发员工表现。重新定义领导力，从“指挥”到“由内而外”。\n\n**关键发现**\n- 66%的领导者认为组织过于复杂且低效\n- 只有30%的组织能实现全企业资源再分配\n- 不到25%的组织能成功实现持续绩效提升\n\n**核心洞察**\n在不确定的世界里，持续绩效和价值创造才是优先项，而不是短期收益。组织需要从短期韧性转向\n\n[... middle omitted ...]\n\n performance edge\n53 Sharpening the focus on diversity and inclusion\n57 Reinventing leadership: Leading from the inside out\n64 Business as change: Managing continuous transformation in the org\n\n[... middle omitted ...]\n\nro, Sasha Goluskin, Scott Brugmans, Tarek Bakali, Tristan Allen, Yueyang Chen, and Zoe Fox.\n\nState of Organizations 2026\nBy McKinsey\nFebruary 2026\nCopyright © McKinsey & Company\n\nwww.McKinsey.com\n\nX @McKinsey\nf @McKinsey"
  },
  {
    "id": "R055",
    "title": "麦肯锡：AI不缺技术，缺的是CEO亲自下场",
    "digest": "[wechat_article.md]\n# 麦肯锡：AI不缺技术，缺的是CEO亲自下场\n\n这份2025年3月发布的麦肯锡全球AI调研报告，覆盖1491位来自101个国家的企业管理者，揭示了一个反直觉的核心判断：AI价值落地的最大瓶颈从来不是技术，而是组织治理与流程重构。CEO亲自监督AI治理，是影响企业AI收益的最强单一变量。报告同时指出，超过80%的企业尚未看到AI对整体EBIT的实质性影响——这不是技术问题，是管理问题。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. CEO亲自管AI治理，比任何技术投入都更影响利润\n\n麦肯锡在调研中测试了25项组织属性与AI对EBIT影响的关联度。结果清晰：CEO是否亲自负责AI治理，是企业能否从AI中获取利润的最强预测因子。在年收入超过5亿美元的大型企业中，这一关联度甚至更高。\n\n报告显示，28%的受访者表示其CEO负责AI治理，17%由董事会负责。但多数情况下，AI治理是联合负责——平均两位高管共同承担。这意味着，不少企业仍在将AI治理“外包”给IT或数字化部门，而这恰恰是麦肯锡合伙人Alexander Sukharevsky在评论中明确指出的“失败配方”。\n\n> **KC评论：** 这里的关键不是CEO“挂名”，而是CEO需要真正介入数据治理、风险合规、资源分配等决策。报告没有展开的是：CEO的时间成本极高，如何在不牺牲日常运营的前提下有效监管AI？这需要一套新的治理节奏和汇报机制。完整报告中对25项属性的详细对比表，值得仔细拆解。\n\n![研报图表 2](assets/xhs_card_02.png)\n\n## 2. 流程重构比技术部署更值钱，但只有21%的企业做到了\n\n麦肯锡发现，在25项组织属性中，“工作流重新设计”对AI收益的影响最大。然而，仅有21%的受访者表示其企业已对至少部分工作流进行了根本性重构。\n\n这一\n\n[... middle omitted ...]\n\n些企业最有可能率先跨越“部门级收益”到“企业级收益”的鸿沟。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI落地，关键看“一把手”工程\n\nCEO亲自抓AI\n\n企业正在为AI价值做组织准备\n\n最近读了麦肯锡2025年3月发布的全球AI调研报告，信息密度很高，直接划重点。\n\n1️⃣ CEO必须亲自管AI治理\n- 调研显示，企业AI治理由CEO亲自负责的，与EBIT正相关性最强\n- 28%的受访企业由CEO管AI治理，17%由董事会负责\n- 大公司（年收入5亿美金以上）更倾向CEO直接管\n- 报告提到：AI落地本质是“变革管理”，不是IT项目，所以必须一把手牵头\n\n2️⃣ 流程重塑 > 技术本身\n- 在25个影响AI价值的因素中，“重新设计工作流”效果最显著\n- 21%的企业已开始根本性调整部分工作流\n- 大公司在这方面动作更快，小公司相对滞后\n\n3️⃣ 风险管控在升级\n- 企业正在主动管理三类风险：准确性、网络安全、知识产权侵权\n- 相比2024年初，主动管控风险的企业比例明显上升\n- 大公司更关注网络安全和隐私，但对AI输出的准确性关注度与中小企业持平\n\n4️⃣ 落地仍处早期\n- 只有1%的企业认为AI部署“成熟”\n- 超过80%的企业尚未看到AI对整体EBIT的实质性影响\n- 但在具体业务单元，更多人开始看到收\n\n[... middle omitted ...]\n\nf555ae093dc404956428b0.jpg)\n\norganizations are starting to make organizational changes designed to generate future value from gen AI, and large companies are leading the way. The latest McKins\n\n[... middle omitted ...]\n\nh 2025  \nCopyright © McKinsey & Company  \nDesigned by McKinsey Global Publishing\n\nFind more content like this on the McKinsey Insights App\n\n![](images/0458fb11ffa1d85bf517ff96c548eb51a4025c0b79a6af63c0bcb79633e51bd1.jpg)"
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "Exhibit 1",
    "context": "Exhibit 3: The RBI recently expanded the universe of Fully Accessible Bonds (FAR) bonds to include the ultra-long end"
  },
  {
    "figure_id": "F002",
    "report_id": "R001",
    "label": "Exhibit 1",
    "context": "Exhibit 3: The RBI recently expanded the universe of Fully Accessible Bonds (FAR) bonds to include the ultra-long end"
  },
  {
    "figure_id": "F003",
    "report_id": "R002",
    "label": "Exhibit 1",
    "context": "Exhibit 1: We expect deceleration in both headline and core PCE inflation... Exhibit 2: ...and forecast payroll growth slows this summer ## The Data Road Map to Rate Hikes"
  },
  {
    "figure_id": "F004",
    "report_id": "R002",
    "label": "Exhibit 1",
    "context": "Exhibit 1: We expect deceleration in both headline and core PCE inflation... Exhibit 2: ...and forecast payroll growth slows this summer ## The Data Road Map to Rate Hikes ## We expect a Fed-on-hold through year-end Following t"
  },
  {
    "figure_id": "F005",
    "report_id": "R002",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Oil prices came down since mid-June Exhibit 4: FOMC participants' projections may be overstating inflation pressures ## The Road Map to Rate Hikes"
  },
  {
    "figure_id": "F006",
    "report_id": "R002",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Oil prices came down since mid-June Exhibit 4: FOMC participants' projections may be overstating inflation pressures ## The Road Map to Rate Hikes That said, our outlook for monetary policy in 2026 is depending on se"
  },
  {
    "figure_id": "F007",
    "report_id": "R002",
    "label": "Exhibit 5",
    "context": "Exhibit 5: We forecast deceleration in both headline and core PCE inflation Exhibit 6: We forecast slower payroll growth # Oil Tracker: US ending stocks of crude oil edge lower amid increased exports and unchanged production"
  },
  {
    "figure_id": "F008",
    "report_id": "R002",
    "label": "Exhibit 5",
    "context": "Exhibit 5: We forecast deceleration in both headline and core PCE inflation Exhibit 6: We forecast slower payroll growth # Oil Tracker: US ending stocks of crude oil edge lower amid increased exports and unchanged production We"
  },
  {
    "figure_id": "F009",
    "report_id": "R002",
    "label": "Exhibit 7",
    "context": "Exhibit 7: US ending stocks of crude oil continue to move lower Exhibit 8: Prices of oil in the physical market have eased but remain higher than before the Iran conflict Exhibit 9: Including the SPR, US oil stocks are falling"
  },
  {
    "figure_id": "F010",
    "report_id": "R002",
    "label": "Exhibit 7",
    "context": "Exhibit 10: US domestic oil production remains broadly unchanged Exhibit 11: US exports of oil and petroleum products have risen, pushing down net imports of these energy goods"
  },
  {
    "figure_id": "F011",
    "report_id": "R002",
    "label": "Exhibit 8",
    "context": "Exhibit 11: US exports of oil and petroleum products have risen, pushing down net imports of these energy goods US Net Imports of Crude Oil and Petroleum Products (Thous.Barrels per Day)"
  },
  {
    "figure_id": "F012",
    "report_id": "R002",
    "label": "Exhibit 9",
    "context": "Exhibit 12: US imports of oil have decelerated a little while exports have picked up"
  },
  {
    "figure_id": "F013",
    "report_id": "R002",
    "label": "Exhibit 10",
    "context": "Exhibit 12: US imports of oil have decelerated a little while exports have picked up # Financial Conditions: A near-reversal following the April 7 ceasefire Following the conflict in the Middle East and the uncertainty it brings"
  },
  {
    "figure_id": "F014",
    "report_id": "R002",
    "label": "Exhibit 12",
    "context": "Exhibit 12: US imports of oil have decelerated a little while exports have picked up # Financial Conditions: A near-reversal following the April 7 ceasefire Following the conflict in the Middle East and the uncertainty it brings"
  },
  {
    "figure_id": "F015",
    "report_id": "R002",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Financial conditions have tightened following the conflict in the Middle East # The effective tariff rate, tariff receipts and refunds ## The tariff rate on US imports has fallen to 8.3% in 1Q26 data On February 20, 20"
  },
  {
    "figure_id": "F016",
    "report_id": "R002",
    "label": "Exhibit 14",
    "context": "Exhibit 14: US effective tariff rate Exhibit 16: Cash withdrawals from the DHS - CBP, as a proxy for tariff refunds Exhibit 15: US Treasury: Customs and excise deposits from tariffs"
  },
  {
    "figure_id": "F017",
    "report_id": "R002",
    "label": "Exhibit 14",
    "context": "Exhibit 14: US effective tariff rate Exhibit 16: Cash withdrawals from the DHS - CBP, as a proxy for tariff refunds Exhibit 15: US Treasury: Customs and excise deposits from tariffs Tariff refunds represent cash returned to im"
  },
  {
    "figure_id": "F018",
    "report_id": "R002",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Cash withdrawals from the DHS - CBP, as a proxy for tariff refunds Exhibit 15: US Treasury: Customs and excise deposits from tariffs Tariff refunds represent cash returned to importers when customs duties were previo"
  },
  {
    "figure_id": "F019",
    "report_id": "R002",
    "label": "Exhibit 17",
    "context": "Exhibit 17: The effect of incoming data on our US GDP tracking estimate Exhibit 18: GDP nowcasts Real GDP tracking, Q/Q % change, a.r. Exhibit 19: Our tracking vs. the Atlanta Fed tracking"
  },
  {
    "figure_id": "F020",
    "report_id": "R003",
    "label": "Exhibit 2",
    "context": "Exhibit 1: G10 FX spot performance: From Middle East tension to MoF's intervention versus after MoF's intervention to date Exhibit 2: US breakeven versus real yield In the former regime, JPY tends to underperform the most, give"
  },
  {
    "figure_id": "F021",
    "report_id": "R003",
    "label": "Exhibit 1",
    "context": "Exhibit 1: G10 FX spot performance: From Middle East tension to MoF's intervention versus after MoF's intervention to date Exhibit 2: US breakeven versus real yield In the former regime, JPY tends to underperform the most, give"
  },
  {
    "figure_id": "F022",
    "report_id": "R003",
    "label": "Exhibit 4",
    "context": "Exhibit 3: Japan's terms of trade versus energy prices Exhibit 4: USD/JPY versus its fair value (US terminal rate pricing, global risk sentiment, and Japan's terms of trade) As discussed below, the MoF has strengthened its verb"
  },
  {
    "figure_id": "F023",
    "report_id": "R003",
    "label": "Exhibit 4",
    "context": "Exhibit 3: Japan's terms of trade versus energy prices Exhibit 4: USD/JPY versus its fair value (US terminal rate pricing, global risk sentiment, and Japan's terms of trade) As discussed below, the MoF has strengthened its verb"
  },
  {
    "figure_id": "F024",
    "report_id": "R003",
    "label": "Exhibit 7",
    "context": "Exhibit 8: Funding needs for JPY via offshore non-bank financial sectors - Fx swap/forward notional amount (JPY, with non-Bank sector) - JPY loan to overseas non-Bank sector,RHS"
  },
  {
    "figure_id": "F025",
    "report_id": "R003",
    "label": "Exhibit 1",
    "context": "Exhibit 8: Funding needs for JPY via offshore non-bank financial sectors - Fx swap/forward notional amount (JPY, with non-Bank sector) - JPY loan to overseas non-Bank sector,RHS Important note regarding economic sanctions. This r"
  },
  {
    "figure_id": "F026",
    "report_id": "R004",
    "label": "Figure 1",
    "context": "Figure 1: USD/CNH is becoming incrementally disconnected with rate fundamentals, ... contribution to 6m change in USD/CNH Figure 2: , ... with US-China yield differentials pointing to a much higher fair value for USD/CNH Figur"
  },
  {
    "figure_id": "F027",
    "report_id": "R004",
    "label": "Figure 1",
    "context": "Figure 1: USD/CNH is becoming incrementally disconnected with rate fundamentals, ... contribution to 6m change in USD/CNH Figure 2: , ... with US-China yield differentials pointing to a much higher fair value for USD/CNH Figur"
  },
  {
    "figure_id": "F028",
    "report_id": "R004",
    "label": "Figure 2",
    "context": "Figure 4: , ... with CNY FX standing out as notably more bullish than other China-linked assets s.d., misalignment between different asset returns vs market-implied China risk premium, +ve indicate bullish market pricing For CNY"
  },
  {
    "figure_id": "F029",
    "report_id": "R004",
    "label": "Figure 4",
    "context": "Figure 5: CNY FX can decouple from rate fundamentals for extended periods R-square of out-of-sample regressions of USD/CNH vs US-China yield differentials"
  },
  {
    "figure_id": "F030",
    "report_id": "R004",
    "label": "Figure 5",
    "context": "Figure 7: China's export performance has consistently surprised to the upside in recent years"
  },
  {
    "figure_id": "F031",
    "report_id": "R004",
    "label": "Figure 5",
    "context": "Figure 7: China's export performance has consistently surprised to the upside in recent years Figure 8: Chinese tech exporters have managed to raise prices, contributing to headline export strength"
  },
  {
    "figure_id": "F032",
    "report_id": "R004",
    "label": "Figure 6",
    "context": "Figure 6: CNY's disconnect with cyclical fundamentals is not indicative of reversal risks Figure 7: China's export performance has consistently surprised to the upside in recent years Figure 8: Chinese tech exporters have mana"
  },
  {
    "figure_id": "F033",
    "report_id": "R004",
    "label": "Figure 7",
    "context": "Figure 9: Chinese corporates have turned into net dollar sellers since 2H25, ... 12m sum, \\$bn, corporates net FX settlement"
  },
  {
    "figure_id": "F034",
    "report_id": "R004",
    "label": "Figure 9",
    "context": "Figure 9: Chinese corporates have turned into net dollar sellers since 2H25, ... 12m sum, \\$bn, corporates net FX settlement Figure 10: , ... although FX conversion appears to be limited to incremental trade income, with the out"
  },
  {
    "figure_id": "F035",
    "report_id": "R004",
    "label": "Figure 9",
    "context": "Figure 9: Chinese corporates have turned into net dollar sellers since 2H25, ... 12m sum, \\$bn, corporates net FX settlement Figure 10: , ... although FX conversion appears to be limited to incremental trade income, with the out"
  },
  {
    "figure_id": "F036",
    "report_id": "R004",
    "label": "Figure 11",
    "context": "Figure 13: Active global funds remain UW China, preserving room for more inflows"
  },
  {
    "figure_id": "F037",
    "report_id": "R004",
    "label": "Figure 14",
    "context": "Figure 13: Active global funds remain UW China, preserving room for more inflows Figure 14: Foreign demand in Chinese bonds has shown tentative recovery"
  },
  {
    "figure_id": "F038",
    "report_id": "R004",
    "label": "Figure 12",
    "context": "Figure 12: Foreign inflows to onshore Chinese stocks have picked up Figure 13: Active global funds remain UW China, preserving room for more inflows Figure 14: Foreign demand in Chinese bonds has shown tentative recovery 2021"
  },
  {
    "figure_id": "F039",
    "report_id": "R004",
    "label": "Figure 12",
    "context": "Figure 15: China's consumer confidence has yet to recover consumer confidence index"
  },
  {
    "figure_id": "F040",
    "report_id": "R004",
    "label": "Figure 15",
    "context": "Figure 15: China's consumer confidence has yet to recover consumer confidence index Figure 16: The external backdrop was more favorable for CNY FX in 2021, with low global yields underpinning CNY's positive carry back then PBoC"
  },
  {
    "figure_id": "F041",
    "report_id": "R004",
    "label": "Figure 15",
    "context": "Figure 15: China's consumer confidence has yet to recover consumer confidence index Figure 16: The external backdrop was more favorable for CNY FX in 2021, with low global yields underpinning CNY's positive carry back then PBoC"
  },
  {
    "figure_id": "F042",
    "report_id": "R004",
    "label": "Figure 19",
    "context": "Figure 17: A managed appreciation has limited the total return from CNY longs Figure 19: CNY NEER looks still far from previous cycle extremes Figure 18: Speculative positioning appears materially lighter than in prior cycles, as"
  },
  {
    "figure_id": "F043",
    "report_id": "R004",
    "label": "Figure 17",
    "context": "Figure 20: The PBoC tends to maintain a supportive FX stance around presidential summits cumulative change in CNY fix, T indicates the date of presidential summits"
  },
  {
    "figure_id": "F044",
    "report_id": "R004",
    "label": "Figure 19",
    "context": "Figure 19: CNY NEER looks still far from previous cycle extremes Figure 18: Speculative positioning appears materially lighter than in prior cycles, as reflected in a relatively contained CNH–CNY basis Figure 20: The PBoC tends"
  },
  {
    "figure_id": "F045",
    "report_id": "R004",
    "label": "Figure 20",
    "context": "Figure 21: Chinese bonds have emerged as a relative safe haven amid recent global rate sell-offs"
  },
  {
    "figure_id": "F046",
    "report_id": "R004",
    "label": "Figure 21",
    "context": "Figure 21: Chinese bonds have emerged as a relative safe haven amid recent global rate sell-offs Figure 22: Bond yields have fallen across the curve Figure 23: Liquidity conditions eased to the most accommodative level since 20"
  },
  {
    "figure_id": "F047",
    "report_id": "R004",
    "label": "Figure 21",
    "context": "Figure 24: , ... before PBoC's liquidity drains leading to marginal tightness"
  },
  {
    "figure_id": "F048",
    "report_id": "R004",
    "label": "Figure 22",
    "context": "Figure 22: Bond yields have fallen across the curve Figure 23: Liquidity conditions eased to the most accommodative level since 2022, ... Figure 24: , ... before PBoC's liquidity drains leading to marginal tightness The yield"
  },
  {
    "figure_id": "F049",
    "report_id": "R004",
    "label": "Figure 23",
    "context": "Figure 25: Deposit growth has far outpaced loan growth, ..."
  },
  {
    "figure_id": "F050",
    "report_id": "R004",
    "label": "Figure 24",
    "context": "Figure 25: Deposit growth has far outpaced loan growth, ... Figure 26: , ... against a backdrop of softening domestic investment activities Figure 27: Expanding AuMs in domestic bond funds and wealth management products undersc"
  },
  {
    "figure_id": "F051",
    "report_id": "R004",
    "label": "Figure 25",
    "context": "Figure 28: The intensified yield hunt from domestic Chinese investors has driven onshore credit spread to historical tights"
  },
  {
    "figure_id": "F052",
    "report_id": "R004",
    "label": "Figure 26",
    "context": "Figure 26: , ... against a backdrop of softening domestic investment activities Figure 27: Expanding AuMs in domestic bond funds and wealth management products underscores robust flow support for Chinese bonds Figure 28: The in"
  },
  {
    "figure_id": "F053",
    "report_id": "R004",
    "label": "Figure 27",
    "context": "Figure 29: While turnover of CGB trading has picked up, it remains well below previous extremes"
  },
  {
    "figure_id": "F054",
    "report_id": "R004",
    "label": "Figure 28",
    "context": "Figure 29: While turnover of CGB trading has picked up, it remains well below previous extremes Figure 30: The overnight repo rate is now re-anchored to PBoC's policy rate, reducing near-term risks of further policy-engineered ti"
  },
  {
    "figure_id": "F055",
    "report_id": "R004",
    "label": "Figure 29",
    "context": "Figure 31: Liquidity conditions tend to ease into mid year before tightening from late 3Q onwards"
  },
  {
    "figure_id": "F056",
    "report_id": "R004",
    "label": "Figure 30",
    "context": "Figure 31: Liquidity conditions tend to ease into mid year before tightening from late 3Q onwards Figure 32: Government bond issuance this year has trailed last year's pace We remain MW in CNY rates, expecting yields to stay br"
  },
  {
    "figure_id": "F057",
    "report_id": "R004",
    "label": "Figure 31",
    "context": "Figure 33: 10y CGB yields are trading slightly rich vs our model, though the misalignment is not large enough to suggest meaningful risks of trend reversal"
  },
  {
    "figure_id": "F058",
    "report_id": "R004",
    "label": "Figure 33",
    "context": "Figure 33: 10y CGB yields are trading slightly rich vs our model, though the misalignment is not large enough to suggest meaningful risks of trend reversal Figure 34: CNY rates have low expectations of further PBoC rate cut ##"
  },
  {
    "figure_id": "F059",
    "report_id": "R004",
    "label": "Figure 34",
    "context": "Figure 33: 10y CGB yields are trading slightly rich vs our model, though the misalignment is not large enough to suggest meaningful risks of trend reversal Figure 34: CNY rates have low expectations of further PBoC rate cut ##"
  },
  {
    "figure_id": "F060",
    "report_id": "R005",
    "label": "Exhibit 2",
    "context": "Exhibit 1: Industrial profits fell sequentially in May while revenue rose Exhibit 2: Total profit margins continued to edge up in May on a 12-month average basis, led by upstream sectors ## The China Economics Team"
  },
  {
    "figure_id": "F061",
    "report_id": "R005",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Industrial profits fell sequentially in May while revenue rose Exhibit 2: Total profit margins continued to edge up in May on a 12-month average basis, led by upstream sectors ## The China Economics Team Andrew Tilto"
  },
  {
    "figure_id": "F062",
    "report_id": "R006",
    "label": "Exhibit 2",
    "context": "Exhibit 4: The median 2027 FCF yield for our oil coverage is 10% near strip (\\~\\$70 WTI), 12% looking just at oil E&Ps. This would move by \\~3% for every \\$10 change in oil."
  },
  {
    "figure_id": "F063",
    "report_id": "R006",
    "label": "Exhibit 2",
    "context": "Exhibit 4: The median 2027 FCF yield for our oil coverage is 10% near strip (\\~\\$70 WTI), 12% looking just at oil E&Ps. This would move by \\~3% for every \\$10 change in oil. Exhibit 5: At \\$70 WTI, near strip, our oil coverage ha"
  },
  {
    "figure_id": "F064",
    "report_id": "R006",
    "label": "Exhibit 3",
    "context": "Exhibit 5: At \\$70 WTI, near strip, our oil coverage has 5% downside vs consensus estimates (7% downside for just oil E&Ps). Exhibit 6: Our 2027 FCF estimates are \\~11% below consensus..."
  },
  {
    "figure_id": "F065",
    "report_id": "R006",
    "label": "Exhibit 4",
    "context": "Exhibit 6: Our 2027 FCF estimates are \\~11% below consensus... Exhibit 7: ...with 2027 EBITDA 6% below consensus."
  },
  {
    "figure_id": "F066",
    "report_id": "R006",
    "label": "Exhibit 5",
    "context": "Exhibit 8: Our oil coverage has hedged $\\sim 5\\%$ of 2027 production on average..."
  },
  {
    "figure_id": "F067",
    "report_id": "R006",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Our 2027 FCF estimates are \\~11% below consensus... Exhibit 7: ...with 2027 EBITDA 6% below consensus. Exhibit 8: Our oil coverage has hedged $\\sim 5\\%$ of 2027 production on average... Exhibit 9: ...and \\~30% for"
  },
  {
    "figure_id": "F068",
    "report_id": "R006",
    "label": "Exhibit 7",
    "context": "Exhibit 7: ...with 2027 EBITDA 6% below consensus. Exhibit 8: Our oil coverage has hedged $\\sim 5\\%$ of 2027 production on average... Exhibit 9: ...and \\~30% for gas E&Ps Exhibit 10: Our oil coverage is pricing an average WTI"
  },
  {
    "figure_id": "F069",
    "report_id": "R006",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Our oil coverage has hedged $\\sim 5\\%$ of 2027 production on average... Exhibit 9: ...and \\~30% for gas E&Ps Exhibit 10: Our oil coverage is pricing an average WTI price of \\~\\$64, \\~6% below 12-month strip. Exhibi"
  },
  {
    "figure_id": "F070",
    "report_id": "R006",
    "label": "Exhibit 9",
    "context": "Exhibit 9: ...and \\~30% for gas E&Ps Exhibit 10: Our oil coverage is pricing an average WTI price of \\~\\$64, \\~6% below 12-month strip. Exhibit 11: Gas E&Ps reflect an average Henry Hub price of \\~\\$3.50, at the 12 month strip."
  },
  {
    "figure_id": "F071",
    "report_id": "R006",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Our oil coverage is pricing an average WTI price of \\~\\$64, \\~6% below 12-month strip. Exhibit 11: Gas E&Ps reflect an average Henry Hub price of \\~\\$3.50, at the 12 month strip. ## Price Target Changes Exhibit 12: M"
  },
  {
    "figure_id": "F072",
    "report_id": "R006",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Price Target Changes Exhibit 14: Bear/Bull Cases ## Performance & Key Industry Metrics Exhibit 15: WoW Energy Sub-sector Performance WoW Performance"
  },
  {
    "figure_id": "F073",
    "report_id": "R006",
    "label": "Exhibit 15",
    "context": "Exhibit 15: WoW Energy Sub-sector Performance WoW Performance Exhibit 16: YTD Energy Sub-sector Performance YTD Performance Exhibit 17: Top E&P WoW Performance"
  },
  {
    "figure_id": "F074",
    "report_id": "R006",
    "label": "Exhibit 16",
    "context": "Exhibit 16: YTD Energy Sub-sector Performance YTD Performance Exhibit 17: Top E&P WoW Performance Exhibit 18: WoW Performance by E&P Subsector"
  },
  {
    "figure_id": "F075",
    "report_id": "R006",
    "label": "Exhibit 16",
    "context": "Exhibit 16: YTD Energy Sub-sector Performance YTD Performance Exhibit 17: Top E&P WoW Performance Exhibit 18: WoW Performance by E&P Subsector Exhibit 19: NAV implied oil prices discount vs strip prices has narrowed in recent"
  },
  {
    "figure_id": "F076",
    "report_id": "R006",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Top E&P WoW Performance Exhibit 18: WoW Performance by E&P Subsector Exhibit 19: NAV implied oil prices discount vs strip prices has narrowed in recent weeks driven by geopolitical risk. Exhibit 20: At our price de"
  },
  {
    "figure_id": "F077",
    "report_id": "R006",
    "label": "Exhibit 18",
    "context": "Exhibit 18: WoW Performance by E&P Subsector Exhibit 19: NAV implied oil prices discount vs strip prices has narrowed in recent weeks driven by geopolitical risk. Exhibit 20: At our price deck of \\~\\$70 WTI in 2027, we forecast"
  },
  {
    "figure_id": "F078",
    "report_id": "R006",
    "label": "Exhibit 19",
    "context": "Exhibit 21: Comp Sheet"
  },
  {
    "figure_id": "F079",
    "report_id": "R007",
    "label": "Figure 9",
    "context": "SIA/WSTS data for April show a 106.3% y-y rise in global semiconductor shipment value (three-month moving average up 94.0%). AI and data center-related demand has remained strong, and sales growth has been particularly strong for memory, partly thanks to price"
  },
  {
    "figure_id": "F080",
    "report_id": "R007",
    "label": "Figure 9",
    "context": "## Japanese semiconductor shipments and inventories ## Japanese semiconductor shipments up 8.1% y-y in April 2026 According to METI's industrial production statistics, the value of semiconductor shipments in Japan was up 8.1% y-y in April 2026 (down 10.8% in M"
  },
  {
    "figure_id": "F081",
    "report_id": "R007",
    "label": "Figure 10",
    "context": "Note: (1) Data for discrete semiconductors exclude rectifiers and memory. (2) Data retroactively adjusted from the July 2023 NOM Tech Monthly with 2020 as base year. ## April 2026 inventory turnover In April 2026, the inventory turnover period was 39.9 days fo"
  },
  {
    "figure_id": "F082",
    "report_id": "R009",
    "label": "Exhibit 1",
    "context": "16 The Succession Reckoning 20 AI and the New Economics of Wealth Management 24 About the Authors # The Great Reshuffling of Financial Wealth Against a backdrop of trade wars, tariff brinkmanship, and escalating geopolitical tension, global financial wealth ro"
  },
  {
    "figure_id": "F083",
    "report_id": "R009",
    "label": "Exhibit 2",
    "context": "## From Concentration to Clustering Cross-border wealth rose 8.4% to \\$15.7 trillion in 2025, lifted by strong market performance and heightened demand for geographical diversification. The top ten booking centers took almost 90% of new cross-border flows. (Se"
  },
  {
    "figure_id": "F084",
    "report_id": "R009",
    "label": "EXHIBIT 3",
    "context": "Singapore is positioned as the most diversified wealth hub in Asia, serving as a neutral conduit between Asian and Western capital markets. That role has made it a beneficiary of safe-haven flows amid US-China tensions. Regulatory stability, institutional cred"
  },
  {
    "figure_id": "F085",
    "report_id": "R009",
    "label": "Exhibit 4",
    "context": "All told, emerging markets will add \\$12 trillion of financial wealth and account for roughly 10% of global wealth growth between now and the end of the decade. The affluent-and-above segment—individuals with over \\$250,000 in financial wealth—is forecast to g"
  },
  {
    "figure_id": "F086",
    "report_id": "R009",
    "label": "Exhibit 5",
    "context": "Plotted against projected wealth growth, that spectrum shows that high-growth, low-maturity markets such as Vietnam offer the greatest potential to build new capabilities, while more developed markets like Brazil and Malaysia offer greater scale but demand mor"
  },
  {
    "figure_id": "F087",
    "report_id": "R009",
    "label": "Exhibit 7",
    "context": "\\- Define the target segment sharply. Upper affluent and HNW clients want something meaningfully different from standard retail banking. The proposition needs to reflect that clearly, built around converting the existing client base rather than chasing new rel"
  },
  {
    "figure_id": "F088",
    "report_id": "R009",
    "label": "Exhibit 7",
    "context": "Succession is becoming more complex across wealth markets, as larger, more dispersed fortunes force families to make explicit choices about how wealth will be owned, governed, and carried forward. Across Asia, an unprecedented generational transition is now un"
  },
  {
    "figure_id": "F089",
    "report_id": "R009",
    "label": "EXHIBIT 8",
    "context": "It’s important also to segregate responsibilities. Family businesses are typically founded on a model in which ownership, control, and management are held by the same individuals. As businesses grow in scale and complexity, that model becomes harder to sustain"
  },
  {
    "figure_id": "F090",
    "report_id": "R009",
    "label": "Exhibit 10",
    "context": "Advisor as strategist ## Structurally lower costs Planning and portfolio mgmt (25%–30% of costs) plus servicing (10%–15%) are dramatically compressed Cost advantage optionality The compounding flywheel: Better efficiency enables better client experiences, whic"
  },
  {
    "figure_id": "F091",
    "report_id": "R009",
    "label": "EXHIBIT 10",
    "context": "Firms that layer AI tactically on existing processes will see moderate near-term benefits. But the biggest payoff will go to true AI-first organizations, those that redesign workflows and processes around AI agents end to end. That effort takes more upfront in"
  },
  {
    "figure_id": "F092",
    "report_id": "R010",
    "label": "Exhibit 1",
    "context": "# The Value Creation Potential from Scaling AI in Renewable Energy Using AI-enabled solutions in renewables creates substantial value across the business, from operations and site selection to support functions like procurement. For example, we estimate that w"
  },
  {
    "figure_id": "F093",
    "report_id": "R010",
    "label": "EXHIBIT 1",
    "context": "## EXHIBIT 1 Deploying AI in Renewables Can Boost Productivity and Increase Energy Yield ## EXHIBIT 2 However, renewable energy companies must act with care and determination when implementing AI. Rising costs and policy headwinds have contributed to margin co"
  },
  {
    "figure_id": "F094",
    "report_id": "R011",
    "label": "Exhibit 1",
    "context": "Over the next two to three years, 50% to 55% of jobs in the US will be reshaped by AI. For many employees, this will mean that they retain the same or a similar role but face radically new expectations for how they work and what they produce. For company leade"
  },
  {
    "figure_id": "F095",
    "report_id": "R011",
    "label": "Exhibit 2",
    "context": "# Task Automation Doesn't Have to Mean Job Loss ## EXHIBIT 2 Agentic AI May Drive High Levels of Task Automation in 43% of Jobs Sources: Revelio Labs; O\\*NET; US Bureau of Labor Statistics; BCG Henderson Institute analysis. Substitution Versus Augmentation. To"
  },
  {
    "figure_id": "F096",
    "report_id": "R011",
    "label": "Exhibit 3",
    "context": "This dynamic is not new. Economists have long observed that efficiency improvements can increase total consumption rather than reduce it, a phenomenon often referred to as Jevons Paradox. When the cost of a resource falls, usage can rise. The same logic applie"
  },
  {
    "figure_id": "F097",
    "report_id": "R011",
    "label": "Exhibit 4",
    "context": "Call center representatives illustrate bounded demand. The volume of inbound interactions is largely determined by the size of the customer base and the frequency of service needs. When AI reduces the cost of handling routine inquiries, the number of interacti"
  },
  {
    "figure_id": "F098",
    "report_id": "R011",
    "label": "Exhibit 7",
    "context": "Third, skill thresholds will rise. Redesigned roles will demand that employees demonstrate greater expertise, oversight, and accountability, increasing the premium on domain knowledge and sound judgment. As Exhibit 7 illustrates, the more durable roles tend to"
  },
  {
    "figure_id": "F099",
    "report_id": "R011",
    "label": "Exhibit 8",
    "context": "Scaling agentic systems requires specialized integration talent, including forward-deployed engineers, systems integrators, and project managers who tailor systems to enterprise-specific contexts. These technical experts are embedded directly with business tea"
  },
  {
    "figure_id": "F100",
    "report_id": "R014",
    "label": "Exhibit 1",
    "context": "The next competitive separation will not come from adding more solutions, nor from building more sophisticated models. It will come from applying AI more deeply to the core commercial initiatives that build sustainable advantage: faster innovation, higher-fide"
  },
  {
    "figure_id": "F101",
    "report_id": "R014",
    "label": "Exhibit 1",
    "context": "AI's impact is expanding across the demand value chain. CPG companies and retailers have long used analytics and machine learning in areas such as product recommendations, pricing, and demand forecasting. What has changed is the range of work that AI can now a"
  },
  {
    "figure_id": "F102",
    "report_id": "R014",
    "label": "Exhibit 2",
    "context": "So far, companies have moved fastest where the economics are clearest. In CPG, that movement has occurred in demand and supply forecasting and revenue growth management optimization. Retailers have advanced furthest in how they manage availability, forecasting"
  },
  {
    "figure_id": "F103",
    "report_id": "R014",
    "label": "Exhibit 2",
    "context": "So far, companies have moved fastest where the economics are clearest. In CPG, that movement has occurred in demand and supply forecasting and revenue growth management optimization. Retailers have advanced furthest in how they manage availability, forecasting"
  },
  {
    "figure_id": "F104",
    "report_id": "R014",
    "label": "Exhibit 3",
    "context": "For the leaders, the value pool is material and likely to grow. BCG experience with clients in scaling individual initiatives suggests that scaling the full set of relevant AI initiatives across the demand value chain can deliver 220 to 350 basis points of cum"
  },
  {
    "figure_id": "F105",
    "report_id": "R014",
    "label": "EXHIBIT 3",
    "context": "## EXHIBIT 3 ## Potential Value Today Total prize at scale today Note: Numbers may not add up due to rounding Total prize at scale today We do not formally measure ROI of AI investments"
  },
  {
    "figure_id": "F106",
    "report_id": "R014",
    "label": "Exhibit 4",
    "context": "Total prize at scale today Note: Numbers may not add up due to rounding Total prize at scale today We do not formally measure ROI of AI investments As agentic capabilities mature and as AI moves from decision support to workflow orchestration, the full-scale o"
  },
  {
    "figure_id": "F107",
    "report_id": "R014",
    "label": "EXHIBIT 4",
    "context": "This is where the pilot trap becomes real. A pilot can succeed in a controlled environment where it operates with selected data, dedicated teams, simplified workflows, and limited integration. At scale, the same initiative must handle live data, legacy systems"
  },
  {
    "figure_id": "F108",
    "report_id": "R014",
    "label": "Exhibit 5",
    "context": "2x to 5x ROI for Best in Class, but the Rest Rarely Measure It Note: Numbers may not add up to 100% due to rounding. Respondents were asked, “What was the realized ROI of your Consumer AI investments targeted in 2025?” # Recommended CEO Considerations: Six que"
  },
  {
    "figure_id": "F109",
    "report_id": "R014",
    "label": "Exhibit 6",
    "context": "The shift is already visible. Leading CPGs are integrating real-time consumer sentiment analysis into concept design and building cross-functional teams from the start of the innovation process, reducing handoff friction that slows development downstream. In r"
  },
  {
    "figure_id": "F110",
    "report_id": "R014",
    "label": "EXHIBIT 7",
    "context": "Agents optimize across all levers, making cross functional trade-offs within guardrails Agents continuously filter data and signal, and surface prioritized actions that replace the fixed cadence 3 Agents follow guardrails; humans intervene on the basis of risk"
  },
  {
    "figure_id": "F111",
    "report_id": "R014",
    "label": "Exhibit 8",
    "context": "Companies should monitor cost inflation. As AI scales, token spending and model usage can become a significant recurring operating cost. The risk profile, however, is not uniform across AI transformations. At the deploy level, broad workforce access can create"
  },
  {
    "figure_id": "F112",
    "report_id": "R016",
    "label": "Exhibit 1",
    "context": "## Three Threats Three of Four Structural Drivers Are Reshaping the Global Agrifood System, and One—Agricultural Intelligence—Offers a Response ## Climate volatility ## Regulatory paradigm shift ## Agricultural intelligence ## Geopolitical realignment"
  },
  {
    "figure_id": "F113",
    "report_id": "R016",
    "label": "Exhibit 2",
    "context": "# The Role of Agricultural Intelligence Agricultural intelligence uses agentic AI to sequence decisions and act autonomously, with minimal human handoff at each step. Going beyond the precision agriculture of the past two decades, it acts on behalf of humans i"
  },
  {
    "figure_id": "F114",
    "report_id": "R019",
    "label": "Exhibit 2",
    "context": "# Financial Stress Is the Default This pessimism is causing financial distress. More than half, or 53%, of European consumers are worried about their daily personal finances, up from 40% in 2024. Six in ten are concerned about having enough money in retirement"
  },
  {
    "figure_id": "F115",
    "report_id": "R019",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3 Consumers Continue to Prioritize Essentials ## A Big Leap Toward Essentials The shift to essentials has continued and deepened. The survey captures consumer sentiment by looking at net spending—the percentage difference between the share of consumers"
  },
  {
    "figure_id": "F116",
    "report_id": "R019",
    "label": "Exhibit 4",
    "context": "There are age-related nuances to this overall picture. Younger consumers report cutting less relative to older cohorts. Over the next six months, reported net spending among Gen X and Baby Boomers is -13 points, and for Gen Z and Millennials it is -2 points. T"
  },
  {
    "figure_id": "F117",
    "report_id": "R019",
    "label": "Exhibit 5",
    "context": "The younger generation are less loyal to brands, with only 28% reporting they usually buy the same brand, compared with 44% of older consumers. They are also more than twice as likely to buy second-hand goods. ## Health Is the New Wealth Against a backdrop of "
  },
  {
    "figure_id": "F118",
    "report_id": "R019",
    "label": "Exhibit 5",
    "context": "Against a backdrop of broad spending cuts, health and well-being are becoming essentials in consumers' minds. Two-thirds of European consumers say health and wellness are extremely important to their lifestyle. Their actions reflect this conviction. Nearly hal"
  },
  {
    "figure_id": "F119",
    "report_id": "R019",
    "label": "Exhibit 6",
    "context": "Brand loyalty is on a decline, with 62% of consumers reporting that they are willing to switch brands for better offers. The willingness exceeds 70% in categories such as furniture and fashion. This translates into reported purchasing behavior. A significant s"
  },
  {
    "figure_id": "F120",
    "report_id": "R019",
    "label": "Exhibit 7",
    "context": "RESPONDENTS WILLING TO SWITCH BRANDS IF VS. 2025 THERE ARE BETTER OFFERS $^{1}$ (%) (PP) TOP FACTORS INFLUENCING PURCHASE DECISIONS FOR CONSUMERS $^{2}$ WHAT BEST DESCRIBES THE CHOICE OF 44% OF CONSUMERS WHO REPORTEDLY CHANGED BRAND IN THEIR RECENT PURCHASE? $"
  },
  {
    "figure_id": "F121",
    "report_id": "R019",
    "label": "Exhibit 7",
    "context": "¹Question: “To what extent do you agree with the following statement: I rarely switch brands for the [category] I buy, even if there were better offers for other brands.” (Results shown for all who do not “Disagree.”) ²Question: “What were the reasons that inf"
  },
  {
    "figure_id": "F122",
    "report_id": "R019",
    "label": "Exhibit 8",
    "context": "personal care versus 3% for older generations. Both GenAI and social media are growing at the direct expense of general internet search, which is flat to declining across every category. Stores remain significant for closing the sale, with 40% of consumers ran"
  },
  {
    "figure_id": "F123",
    "report_id": "R020",
    "label": "Exhibit 1",
    "context": "In many respects, there has never been a better time to be a fintech founder or investor. Only 3% of global banking and insurance revenue pools have been penetrated by fintechs. Many holes remain, and emerging technologies and business models will empower fint"
  },
  {
    "figure_id": "F124",
    "report_id": "R020",
    "label": "EXHIBIT 1",
    "context": "Fintechs also endured increased regulatory scrutiny in 2024. Examples include fines for Chime (\\$2.5 million for failing to return customer funds in a timely manner) and Block (\\$86 million for anti-money laundering (AML) failures). And April saw the collapse "
  },
  {
    "figure_id": "F125",
    "report_id": "R020",
    "label": "EXHIBIT 1",
    "context": "The last quarter of 2024 did bring cause for more optimism, and this has continued into 2025, with equity funding in Q1 increasing 34% versus the previous year and revenue multiples up 10%. ## EXHIBIT 1 Funding and Valuations Have Stabilized, While Revenue Gro"
  },
  {
    "figure_id": "F126",
    "report_id": "R020",
    "label": "Exhibit 3",
    "context": "\"It is hard to read the tea leaves on IPOs. Everyone wants the market to open, but tariffs are roiling the market . . . We really won't know until after the summer. The best candidates are happy and able to sit on the sidelines until there is more certainty.\" "
  },
  {
    "figure_id": "F127",
    "report_id": "R020",
    "label": "Exhibit 3",
    "context": "JAMES LOFTUS Managing Partner, Paypal Ventures Sources: S&P Capital IQ; PitchBook; BCG FinTech Control Tower; BCG analysis. Note: The rule of 40 is a financial metric measuring whether the sum of revenue growth (%) and EBITDA margin (%) is greater than 40. We "
  },
  {
    "figure_id": "F128",
    "report_id": "R020",
    "label": "Exhibit 3",
    "context": "Managing Partner, Paypal Ventures Sources: S&P Capital IQ; PitchBook; BCG FinTech Control Tower; BCG analysis. Note: The rule of 40 is a financial metric measuring whether the sum of revenue growth (%) and EBITDA margin (%) is greater than 40. We also expect a"
  },
  {
    "figure_id": "F129",
    "report_id": "R020",
    "label": "EXHIBIT 3",
    "context": "SVP, Mercado Pago ## EXHIBIT 3 Revenue Growth, Size, R&D Spend, and Profitability Drive Variation in Public Fintech Valuations Relative contribution of the different drivers of valuation among public fintechs (%) Sources: S&P Capital IQ; BCG ValueScience Cente"
  },
  {
    "figure_id": "F130",
    "report_id": "R020",
    "label": "Exhibit 4",
    "context": "Revenue Growth, Size, R&D Spend, and Profitability Drive Variation in Public Fintech Valuations Relative contribution of the different drivers of valuation among public fintechs (%) Sources: S&P Capital IQ; BCG ValueScience Center. Note: Outliers removed or no"
  },
  {
    "figure_id": "F131",
    "report_id": "R020",
    "label": "EXHIBIT 4",
    "context": "## EXHIBIT 4 # Fintech Penetrates About 3% of Banking and Insurance Revenues but Is Growing Approximately 3x More Quickly \\_ FINTECHS ACCOUNT FOR \\~3% OF FINANCIAL SERVICES REVENUES TOTAL REVENUE, 2024 (\\$) FINTECH PENETRATION OF INCUMBENT FINANCIAL SERVICES R"
  },
  {
    "figure_id": "F132",
    "report_id": "R020",
    "label": "Exhibit 6",
    "context": "\\- Banks have been unwilling to go. Fintechs have thrived by targeting opportunities where either regulatory risk or strategic constraints limit banks from competing. For example, regulations have made crypto off-limits for banks. Banks have also been unable t"
  },
  {
    "figure_id": "F133",
    "report_id": "R020",
    "label": "Exhibit 6",
    "context": "Looking at where scaled fintechs have succeeded by geography provides another perspective. (See Exhibit 6.) The US accounts for about 52% (or \\~\\$120 billion) of scaled revenues, thanks to its large addressable market and easy access to capital. Again, payment"
  },
  {
    "figure_id": "F134",
    "report_id": "R020",
    "label": "EXHIBIT 7",
    "context": "## EXHIBIT 7 ## Example Agentic AI Use Cases in Financial Services Proactive financial agents monitor a customer's income, behavior, and goals, then take actions like auto-moving funds and adjusting savings goals Goal-driven portfolio agents monitor the market"
  },
  {
    "figure_id": "F135",
    "report_id": "R020",
    "label": "EXHIBIT 8",
    "context": "## EXHIBIT 8 ## Potential Inflection Point Ahead for Onchain Finance ## Required Enablers Technological scalability"
  },
  {
    "figure_id": "F136",
    "report_id": "R020",
    "label": "EXHIBIT 8",
    "context": "## EXHIBIT 8 ## Potential Inflection Point Ahead for Onchain Finance ## Required Enablers Technological scalability Regulatory clarity"
  },
  {
    "figure_id": "F137",
    "report_id": "R020",
    "label": "EXHIBIT 9",
    "context": "\\- Slow Settlement Times. Intermediaries add not only cost but also friction, slowing settlement times as assets move across multiple parties and ledgers. Tokenization promises flexible, instant, 24/7/365 settlement. This has the double benefit of enhancing li"
  },
  {
    "figure_id": "F138",
    "report_id": "R020",
    "label": "Exhibit 10",
    "context": "# European DLT Trials with CBDCs In November 2024, the European Investment Bank issued a €100 million bond on HSBC's Orion platform that used Banque de France's experimental wholesale CBDC to settle. SG also entered into a repurchasing agreement with Banque de"
  },
  {
    "figure_id": "F139",
    "report_id": "R020",
    "label": "EXHIBIT 10",
    "context": "Historically, global expansion has proven difficult, even for traditional banking giants such as Citi. (See Spotlight 3.) Yet challenger banks possess some advantages over incumbents in this scenario, including leaner operating models, cloud-native technology "
  },
  {
    "figure_id": "F140",
    "report_id": "R020",
    "label": "Exhibit 12",
    "context": "Sources: Federal Reserve; Reserve Bank of India; UK Parliament; OECD; BCG analysis. # Private Credit Funds Have a Roughly \\$280 Billion Whitespace Opportunity in Fintech Total outstanding fintech-originated loan balances GLOBAL MARKET, 2024 Sources: S&P Capita"
  },
  {
    "figure_id": "F141",
    "report_id": "R021",
    "label": "Exhibit 1",
    "context": "Investors are placing more emphasis on which business models can capture the next wave of value, which technologies can create durable advantage, and how far players can extend into adjacent products, geographies, and infrastructure layers while navigating a m"
  },
  {
    "figure_id": "F142",
    "report_id": "R021",
    "label": "Exhibit 1",
    "context": "There has been a striking reversal of mood within the global fintech sector. Two years ago, the sector was still working through the aftershocks of the 2021 reset, a period during which capital was scarce, valuations compressed sharply, and questions about the"
  },
  {
    "figure_id": "F143",
    "report_id": "R021",
    "label": "Exhibit 2",
    "context": "# Global Fintech Revenues Break Half a Trillion Dollars in 2025 Global fintech revenue by vertical (2021–2025, \\$B) Global fintech revenue by region (2021–2025, \\$B) Sources: S&P Capital IQ; BCG FinTech Control Tower; BCG Banking and Insurance Revenue Pools; B"
  },
  {
    "figure_id": "F144",
    "report_id": "R021",
    "label": "EXHIBIT 3",
    "context": "Fintechs account for \\~4% of global financial services revenues TOTAL GLOBAL REVENUE, 2025 (\\$) Fintech revenue growth outpaced incumbents across all verticals FINTECH VS. INCUMBENT REVENUE GROWTH YOY, 2024–2025 (%) $^{1}$ Sources: S&P Capital IQ; Pitchbook; B"
  },
  {
    "figure_id": "F145",
    "report_id": "R021",
    "label": "EXHIBIT 3",
    "context": "Sources: S&P Capital IQ; Pitchbook; BCG FinTech Control Tower; BCG Banking and Insurance Revenue Pools; BCG analysis. $^{1}$ Excludes “financial infrastructure,” as the category is not relevant for incumbent financial institutions. ## EXHIBIT 3 Payments Remain"
  },
  {
    "figure_id": "F146",
    "report_id": "R021",
    "label": "Exhibit 5",
    "context": "Since GCash's explosive growth starting in 2015, the financially excluded population in the Philippines declined from \\~70% to \\~20% Brazil Kenya Philippines Sources: World Bank; UN World Population Prospects; Kenya National Bureau of Statistics; Central Bank "
  },
  {
    "figure_id": "F147",
    "report_id": "R021",
    "label": "Exhibit 5",
    "context": "Brazil Kenya Philippines Sources: World Bank; UN World Population Prospects; Kenya National Bureau of Statistics; Central Bank of Kenya; Safaricom Reports; Philippine Statistics Authority, Bangko Sentral ng Pilipinas FIS, Globe Telecom/Mynt/Gcash Reports; BCG "
  },
  {
    "figure_id": "F148",
    "report_id": "R021",
    "label": "Exhibit 6",
    "context": "Maturation is also evident in where capital is going. Equity funding rose 53% to \\$58 billion in 2025, but funding growth was not evenly distributed. (See Exhibit 6.) Trading and investment fintechs captured roughly one-third of all funding, up from about one-"
  },
  {
    "figure_id": "F149",
    "report_id": "R021",
    "label": "EXHIBIT 6",
    "context": "AVERAGE EBITDA MARGIN (%) SHARE OF FINTECHS ABOVE THE RULE OF $40^{2}$ (\\%) Sources: Financial analysis of the top 85 fintechs, S&P Capital IQ; Pitchbook; BCG FinTech Control Tower; BCG analysis. $^{1}$ Profitability defined as EBITDA or EBT. $^{2}$ Rule of 40"
  },
  {
    "figure_id": "F150",
    "report_id": "R021",
    "label": "EXHIBIT 6",
    "context": "REVENUE MULTIPLE FOR PUBLIC FINTECHS ## EXHIBIT 6 Equity Funding and IPO Activity Have Accelerated, While Valuations Have Grown Moderately FINTECH EQUITY FINANCING (\\$B) 2025 funding rebound has continued into 2026, with Q1 equity funding reaching \\$14.8B, sur"
  },
  {
    "figure_id": "F151",
    "report_id": "R021",
    "label": "EXHIBIT 7",
    "context": "GS Growth Equity ## EXHIBIT 7 AI Is More Than a Tool Upgrade, It Is an Organizational Transformation In a digitally enhanced model, people are the core drivers, with AI tools to boost efficiency Core processes built around people Supplemented by digital tools "
  },
  {
    "figure_id": "F152",
    "report_id": "R021",
    "label": "Exhibit 8",
    "context": "While many of the narratives around consumer-facing autonomous agents still feel premature, some do present glimpses of a potential agentic future. A few AI-native fintechs at the bleeding edge of agentic AI adoption have incorporated agentic AI into everythin"
  },
  {
    "figure_id": "F153",
    "report_id": "R021",
    "label": "EXHIBIT 9",
    "context": "How far can fintech penetrate B2B, and what it will take to win? The answer will depend as much on trust as on product quality. To displace entrenched systems, fintechs must convince clients that the operational risk and complexity of unwinding existing workfl"
  },
  {
    "figure_id": "F154",
    "report_id": "R021",
    "label": "Exhibit 10",
    "context": "We believe that autonomous agentic commerce has a reasonably long path to scale, and may only get there in certain cases. The reasons exist on both the demand side and the supply side. On the former, consumers are more likely to adopt agents where they create "
  },
  {
    "figure_id": "F155",
    "report_id": "R021",
    "label": "Exhibit 11",
    "context": "Trust is a foundational issue across all of these categories, not an isolated problem in any one vertical. Consumers need confidence that the agent is acting within clear boundaries, that mistakes can be corrected easily, and that the downside of delegation is"
  },
  {
    "figure_id": "F156",
    "report_id": "R021",
    "label": "Exhibit 12",
    "context": "# Google Staking a Position in Agentic Commerce The next phase of fintech will not be confined to fintechs themselves. As AI changes how consumers discover, compare, and buy, Google is moving to defend discovery—but its response goes beyond preserving search t"
  },
  {
    "figure_id": "F157",
    "report_id": "R021",
    "label": "EXHIBIT 12",
    "context": "## EXHIBIT 12 # About 7,000 Fintechs Are Building the Digital Asset Ecosystem and Comprise an Increasing Share of Fintech Equity Funding and Revenue SHARE OF ACTIVE FINTECHS, BY DIGITAL ASSETS (COMPANY COUNT) Sources: S&P Capital IQ; Pitchbook; BCG FinTech Con"
  },
  {
    "figure_id": "F158",
    "report_id": "R021",
    "label": "EXHIBIT 14",
    "context": "Sources: BCG FinTech Control Tower. $^{1}$ Cumulative number of digital asset fintech and equity funding attracted from 2000 to 2025 inclusive. ## EXHIBIT 14 ## The Asset Tokenization Flywheel Is Starting to Spin Sources: RWA.xyz; BCG analysis. Note: CBDC = ce"
  },
  {
    "figure_id": "F159",
    "report_id": "R021",
    "label": "EXHIBIT 16",
    "context": "## EXHIBIT 16 Federal Bank Charters and Depository Institution Applications Increased Over 5x from 2024 to 2025 Federal bank charter and new-bank application volume $^{1}$ (2021–2026 Q1) Sources: OCC; FDIC. $^{1}$ Includes OCC national bank / national trust ch"
  },
  {
    "figure_id": "F160",
    "report_id": "R021",
    "label": "Exhibit 18",
    "context": "Despite continued public-market volatility and investor selectivity, IPO and M&A activity are likely to continue at their current levels. Scaled fintechs still need paths to liquidity, and strategic urgency across the sector remains high. But the composition o"
  },
  {
    "figure_id": "F161",
    "report_id": "R021",
    "label": "EXHIBIT 18",
    "context": "## EXHIBIT 18 2025 Saw the Highest Number of M&A Deals and Second-Highest Amount; Scaled Fintechs Were the Most Active Acquirers Scaled fintechs were the most active acquirers in 2025 (COUNT BY ACQUIRER TYPE $^{1}$ ) $^{1}$ Analysis by acquirer type only inclu"
  },
  {
    "figure_id": "F162",
    "report_id": "R022",
    "label": "Exhibit 1",
    "context": "## Navigating the Medtech GenAI Journey: A Policy Primer The road to successful Generative Artificial Intelligence (GenAI) deployment in medtech can draw parallels from classical literature and mythology. The hero (a medtech company) heeds a call to adventure "
  },
  {
    "figure_id": "F163",
    "report_id": "R022",
    "label": "Exhibit 1",
    "context": "Copyright 2023 by Boston Consulting Group. All rights reserved. ## Risks on Your Medtech Journey ## Exhibit 1 – Generative AI Increases Some Existing LLM Risks Copyright 2023 by Boston Consulting Group. All rights reserved. AI cyberattacks, especially those in"
  },
  {
    "figure_id": "F164",
    "report_id": "R022",
    "label": "Exhibit 2",
    "context": "In the US, the Food and Drug Administration's (FDA's) Center for Device and Radiological Health (CDRH) acts as the principal regulator for GenAI-powered medical devices, though the Department of Health and Human Services Office of Civil Rights oversees the Hea"
  },
  {
    "figure_id": "F165",
    "report_id": "R022",
    "label": "Exhibit 2",
    "context": "Exhibit 2 – Agility Needed to Respond to Existing & Upcoming Regulations (non-exhaustive, selection of key regulations) Note: BCG does not provide legal advice Copyright 2023 by Boston Consulting Group. All rights reserved. ## Functional and commercial use cas"
  },
  {
    "figure_id": "F166",
    "report_id": "R022",
    "label": "Exhibit 3",
    "context": "Exhibit 3 - Clinical Use Cases Have the Most Risks to Proactively Mitigate Copyright 2023 by Boston Consulting Group. All rights reserved. ## Developing a Responsible AI Playbook BCG recommends a centralized approach to developing"
  },
  {
    "figure_id": "F167",
    "report_id": "R023",
    "label": "Exhibit 1",
    "context": "## Contents 03 The New Economics of Asset Management 13 Distribution Is the New"
  },
  {
    "figure_id": "F168",
    "report_id": "R023",
    "label": "EXHIBIT 1",
    "context": "This will require asset managers to operate differently. Firms that align with the next sources of capital and adapt how they compete will capture a disproportionate share of future growth. ## EXHIBIT 1 # Market Performance Drove Over 80% of Gross Revenue Grow"
  },
  {
    "figure_id": "F169",
    "report_id": "R023",
    "label": "Exhibit 3",
    "context": "Sources: BCG EXPAND Global Asset Management Market Sizing 2026; BCG analysis. Note: AuM market sizing corresponds to assets sourced from each region and professionally managed in exchange for management fees. It includes captive AuM of insurance groups or pens"
  },
  {
    "figure_id": "F170",
    "report_id": "R023",
    "label": "Exhibit 3",
    "context": "Global AuM has more than tripled and revenue more than doubled over the past 15 years. Yet industry profit margins remain close to 30%, roughly where they stood in 2010. Between 2010 and 2025, revenues grew at 5.1% annually while costs rose slightly faster at "
  },
  {
    "figure_id": "F171",
    "report_id": "R023",
    "label": "Exhibit 4",
    "context": "The rise of digital-native investors is concentrating flows in a smaller set of platforms that act as gatekeepers to capital. For asset managers, success will depend on being embedded in these ecosystems, with products and capabilities designed for how capital"
  },
  {
    "figure_id": "F172",
    "report_id": "R023",
    "label": "Exhibit 6",
    "context": "Leading firms embed these changes across the distribution journey. (See Exhibit 6.) AI only delivers if the underlying model is sound. Asset managers need to get the four interlocking pillars of distribution right before deploying it. Layering AI on top of a b"
  },
  {
    "figure_id": "F173",
    "report_id": "R023",
    "label": "Exhibit 7",
    "context": "Deploy AI and widen the gap. Coverage can extend to clients that were previously uneconomical to serve, while preparation and targeting improve across accounts. Over time, this raises productivity and allows the model to scale more effectively. (See Exhibit 7."
  },
  {
    "figure_id": "F174",
    "report_id": "R023",
    "label": "EXHIBIT 8",
    "context": "\\- Go deep. Set a top-down ambition, but rewire the business bottom-up. Lasting agentic advantage primarily requires changes to the operating model, talent, and processes that embed AI into how work gets done, not by data and technology alone. Asset managers t"
  },
  {
    "figure_id": "F175",
    "report_id": "R024",
    "label": "Exhibit 1",
    "context": "## Contents 03 The New Economics of Asset Management 13 Distribution Is the New"
  },
  {
    "figure_id": "F176",
    "report_id": "R024",
    "label": "EXHIBIT 1",
    "context": "This will require asset managers to operate differently. Firms that align with the next sources of capital and adapt how they compete will capture a disproportionate share of future growth. ## EXHIBIT 1 # Market Performance Drove Over 80% of Gross Revenue Grow"
  },
  {
    "figure_id": "F177",
    "report_id": "R024",
    "label": "Exhibit 3",
    "context": "Sources: BCG EXPAND Global Asset Management Market Sizing 2026; BCG analysis. Note: AuM market sizing corresponds to assets sourced from each region and professionally managed in exchange for management fees. It includes captive AuM of insurance groups or pens"
  },
  {
    "figure_id": "F178",
    "report_id": "R024",
    "label": "Exhibit 3",
    "context": "Global AuM has more than tripled and revenue more than doubled over the past 15 years. Yet industry profit margins remain close to 30%, roughly where they stood in 2010. Between 2010 and 2025, revenues grew at 5.1% annually while costs rose slightly faster at "
  },
  {
    "figure_id": "F179",
    "report_id": "R024",
    "label": "Exhibit 4",
    "context": "The rise of digital-native investors is concentrating flows in a smaller set of platforms that act as gatekeepers to capital. For asset managers, success will depend on being embedded in these ecosystems, with products and capabilities designed for how capital"
  },
  {
    "figure_id": "F180",
    "report_id": "R024",
    "label": "Exhibit 6",
    "context": "Leading firms embed these changes across the distribution journey. (See Exhibit 6.) AI only delivers if the underlying model is sound. Asset managers need to get the four interlocking pillars of distribution right before deploying it. Layering AI on top of a b"
  },
  {
    "figure_id": "F181",
    "report_id": "R024",
    "label": "Exhibit 7",
    "context": "Deploy AI and widen the gap. Coverage can extend to clients that were previously uneconomical to serve, while preparation and targeting improve across accounts. Over time, this raises productivity and allows the model to scale more effectively. (See Exhibit 7."
  },
  {
    "figure_id": "F182",
    "report_id": "R024",
    "label": "EXHIBIT 8",
    "context": "\\- Go deep. Set a top-down ambition, but rewire the business bottom-up. Lasting agentic advantage primarily requires changes to the operating model, talent, and processes that embed AI into how work gets done, not by data and technology alone. Asset managers t"
  },
  {
    "figure_id": "F183",
    "report_id": "R025",
    "label": "Exhibit 1",
    "context": "Spread businesses such as neobanks and lending platforms will face challenges in the developed world while playing a critical role in emerging markets. The time for stakeholders to act is now: Fintechs must play offense, incumbents need to accelerate their own"
  },
  {
    "figure_id": "F184",
    "report_id": "R025",
    "label": "Exhibit 1",
    "context": "Exhibit 1 - In Q2 2021, Peak Valuations Reached an Inflated 20x Revenue Multiple Q4 2017 – Q4 2022, average revenue multiples for public fintechs (simple average, market Cap/LTM revenues) Sources: Fintech Control Tower, Capital IQ"
  },
  {
    "figure_id": "F185",
    "report_id": "R025",
    "label": "Exhibit 2",
    "context": "Exhibit 2 - Since 2021, Funding Levels for Later Stages (Series C+) Have Dropped More Drastically Than for Earlier Stages (Seed/Series A/B) 2021–2022, Average Funding (\\$B) by Stage Sources: Fintech Control Tower, BCG analysis. ##"
  },
  {
    "figure_id": "F186",
    "report_id": "R025",
    "label": "Exhibit 4",
    "context": "Partnerships Hiring/Talent Sources: BCG/QED Future of Fintech survey (N=81), conducted across fintech CEOs and C-Suite leaders in February 2023; BCG analysis. Q. What are the top 3 challenges facing your company in the next 12–18 months? Q. What are the top ac"
  },
  {
    "figure_id": "F187",
    "report_id": "R025",
    "label": "Exhibit 5",
    "context": "Another factor is the overall customer experience in financial services (including the insurance sector) has historically been among the lowest-ranked compared with other industries. Although incumbents have made progress over the past few years, they still si"
  },
  {
    "figure_id": "F188",
    "report_id": "R025",
    "label": "Exhibit 5",
    "context": "Exhibit 5 - Customer Experience Across Value Chains Is Relatively Poor for Incumbent Financial Institutions Customer loyalty scores aggregates, major U.S. financial institutions Customer loyalty scores, Major Fintechs with U.S."
  },
  {
    "figure_id": "F189",
    "report_id": "R025",
    "label": "Exhibit 5",
    "context": "Exhibit 5 - Customer Experience Across Value Chains Is Relatively Poor for Incumbent Financial Institutions Customer loyalty scores aggregates, major U.S. financial institutions Customer loyalty scores, Major Fintechs with U.S."
  },
  {
    "figure_id": "F190",
    "report_id": "R025",
    "label": "Exhibit 8",
    "context": "Customer loyalty scores aggregates, major U.S. financial institutions Customer loyalty scores, Major Fintechs with U.S. Operations Sources: Forrester - The US Net Promoter Rankings, 2022/Customer Gauge Benchmarks in Financial Services 2022. Phase Three: Releva"
  },
  {
    "figure_id": "F191",
    "report_id": "R025",
    "label": "Exhibit 7",
    "context": "Exhibit 7 - There Is High Potential to Increase Digital Banking Adoption, Especially in Emerging Markets 2021, Share of Digital Engagement by Category $^{1}$ Sources: Forrester Research, World Bank, BCG analysis. Note: Consumer ba"
  },
  {
    "figure_id": "F192",
    "report_id": "R025",
    "label": "EXHIBIT 8",
    "context": "Nonetheless, taking all of the above into consideration, how is the fintech sector likely to evolve in the remaining part of Phase Four and beyond? EXHIBIT 8/SURVEY .02 ## Fintech CEOs Wary in the Short Term, Optimistic in the Longer Term, as Fundamentals Rema"
  },
  {
    "figure_id": "F193",
    "report_id": "R025",
    "label": "EXHIBIT 8",
    "context": "Nonetheless, taking all of the above into consideration, how is the fintech sector likely to evolve in the remaining part of Phase Four and beyond? EXHIBIT 8/SURVEY .02 ## Fintech CEOs Wary in the Short Term, Optimistic in the Longer Term, as Fundamentals Rema"
  },
  {
    "figure_id": "F194",
    "report_id": "R025",
    "label": "Exhibit 10",
    "context": "Average +/- 5% 5–10% above average Sources: BCG/QED Future of Fintech survey (N=81), conducted across fintech CEOs and C-Suite leaders in February 2023; BCG analysis. Q. How optimistic are you about the future prospects of your company in the next 12 months? Q"
  },
  {
    "figure_id": "F195",
    "report_id": "R025",
    "label": "Exhibit 10",
    "context": "Exhibit 9 - Global Financial Services Revenues Will Reach \\$22 Trillion by 2030, With a Relatively Even Split Between Banking and Insurance Global Financial Services Revenues (\\$T), split by Banking and Insurance, 2021 to 2030 Sou"
  },
  {
    "figure_id": "F196",
    "report_id": "R025",
    "label": "Exhibit 10",
    "context": "Exhibit 11 - Asia-Pacific Will Be the Largest Fintech Market by 2030, and Latin America and Africa Will Be the Fastest-Growing Regions"
  },
  {
    "figure_id": "F197",
    "report_id": "R025",
    "label": "Exhibit 11",
    "context": "Exhibit 11 - Asia-Pacific Will Be the Largest Fintech Market by 2030, and Latin America and Africa Will Be the Fastest-Growing Regions Global Fintech Revenue Growth by Region, 2021 to 2030 Sources: Capital IQ, Pitchbook, Company's"
  },
  {
    "figure_id": "F198",
    "report_id": "R025",
    "label": "Exhibit 12",
    "context": "Looking ahead, in a global sense, we expect a geographic expansion of fintech ideas to develop mainly through three models: the emergence of local champions, the rise of multinational fintechs, and the expanding role of big techs. The Emergence of Local Champi"
  },
  {
    "figure_id": "F199",
    "report_id": "R025",
    "label": "Exhibit 12",
    "context": "The first part of the fintech journey was led by payments, representing 40% of all fintech revenue in 2021. Since 2000, payments fintechs have accounted for roughly 25% of cumulative equity funding (\\$120 billion). Yet, this is still a story with significant r"
  },
  {
    "figure_id": "F200",
    "report_id": "R025",
    "label": "Exhibit 12",
    "context": "Exhibit 12 - Payments Will Remain the Largest Fintech Segment in 2030 Sources: Capital IQ, Pitchbook, Company's investor presentations, desktop research, BCG analysis."
  },
  {
    "figure_id": "F201",
    "report_id": "R025",
    "label": "Exhibit 12",
    "context": "Exhibit 12 - Payments Will Remain the Largest Fintech Segment in 2030 Sources: Capital IQ, Pitchbook, Company's investor presentations, desktop research, BCG analysis. A2A RTPs, facilitated by infrastructure enhancements, will lead"
  },
  {
    "figure_id": "F202",
    "report_id": "R025",
    "label": "Exhibit 13",
    "context": "B2B2X comprises B2B2C (enabling other players to better serve consumers), B2B2B (enabling other players to better serve businesses), and financial infrastructure players. The latter provide customer-segment-agnostic technology solutions that support the operat"
  },
  {
    "figure_id": "F203",
    "report_id": "R025",
    "label": "Exhibit 13",
    "context": "Exhibit 13 - B2B2x and B2b Will Be the Fastest Growing End Customers Global Fintech Revenue Growth by Space, 2021 to 2030 Growth multiple (X) Sources: Capital IQ, Pitchbook, company's investor presentations, desktop research, BCG a"
  },
  {
    "figure_id": "F204",
    "report_id": "R025",
    "label": "Exhibit 14",
    "context": "Exhibit 14 - Large Banks Realize the Importance of Investing in Tech, as IT Spend (as % of Opex) for Some Is at Par with Major Fintechs"
  },
  {
    "figure_id": "F205",
    "report_id": "R025",
    "label": "Exhibit 14",
    "context": "Exhibit 14 - Large Banks Realize the Importance of Investing in Tech, as IT Spend (as % of Opex) for Some Is at Par with Major Fintechs IT spend in 2022 (as % of operating costs), major banks, big-tech and fintechs Range of display"
  },
  {
    "figure_id": "F206",
    "report_id": "R025",
    "label": "Exhibit 15",
    "context": "Another challenge is neobanks are typically attracting lower-LTV customers with their “no fees” or “lower fees” value propositions, which are harder to monetize and require a significant volume of transactions and customers in order to generate profits. In eme"
  },
  {
    "figure_id": "F207",
    "report_id": "R025",
    "label": "Exhibit 15",
    "context": "## SPOTLIGHT #3 ## Nubank Founded in 2013 in Brazil $^{5}$ , Nubank started as a no-fee credit card provider but has expanded to a variety of new customer-centric financial offerings—such as easy-to-use mobile banking, personal loans, and insurance. At the end"
  },
  {
    "figure_id": "F208",
    "report_id": "R025",
    "label": "Exhibit 15",
    "context": "Founded in 2013 in Brazil $^{5}$ , Nubank started as a no-fee credit card provider but has expanded to a variety of new customer-centric financial offerings—such as easy-to-use mobile banking, personal loans, and insurance. At the end of 2022, Nubank had 75 mi"
  },
  {
    "figure_id": "F209",
    "report_id": "R026",
    "label": "Exhibit 1",
    "context": "The fintech IPO market will eventually bounce back, but fintechs must now tell a comprehensive equity story about how they will attract users at sustainable costs, grow profitably, and meet increasing regulatory requirements. \\$320B By 2030, embedded finance w"
  },
  {
    "figure_id": "F210",
    "report_id": "R026",
    "label": "Exhibit 1",
    "context": "It has been a sobering three years for fintechs. Coming off the highs of 2021, revenue multiples have fallen from 20 times to 4 times on average, and funding is down by 70%—and almost 50% in the last year. (See Exhibit 1.) The declines are heavier in some area"
  },
  {
    "figure_id": "F211",
    "report_id": "R026",
    "label": "Exhibit 1",
    "context": "Revenue growth was strong PUBLIC AND PRIVATE FINTECH REVENUE (\\$BILLION) ## Exhibit 1 Funding and Valuations Still Down but Revenues Are Thriving Revenue multiples stabilized but are still low REVENUE MULTIPLE FOR PUBLIC FINTECHS $^{1}$ Sources: Capital IQ; Pi"
  },
  {
    "figure_id": "F212",
    "report_id": "R026",
    "label": "Exhibit 1",
    "context": "## Exhibit 1 Funding and Valuations Still Down but Revenues Are Thriving Revenue multiples stabilized but are still low REVENUE MULTIPLE FOR PUBLIC FINTECHS $^{1}$ Sources: Capital IQ; Pitchbook; companies' investor presentations; desktop research; BCG Fintech"
  },
  {
    "figure_id": "F213",
    "report_id": "R026",
    "label": "Exhibit 2",
    "context": "Simultaneously, global fintech revenues have continued to grow at a robust clip—14% over the past two years across the board, and 21% when crypto- and China-exposed fintechs are excluded. Growth during the two-year period comprising 2022 and 2023, in fact, com"
  },
  {
    "figure_id": "F214",
    "report_id": "R026",
    "label": "Exhibit 2",
    "context": "Exhibit 2 The Starkest Revenue Growth Gaps Are Between Top- and Bottom-Quartile Fintechs Difference across select sectors and geographies REVENUE CAGR, 2021–2023 Difference between top and bottom quartiles CAGR FOR TOP AND BOTTOM QUARTILE, 2021–2023 Sources: C"
  },
  {
    "figure_id": "F215",
    "report_id": "R026",
    "label": "Exhibit 3",
    "context": "REVENUE CAGR, 2021–2023 Difference between top and bottom quartiles CAGR FOR TOP AND BOTTOM QUARTILE, 2021–2023 Sources: Capital IQ; Pitchbook; companies' investor presentations; desktop research; BCG Fintech Control Tower; BCG analysis."
  },
  {
    "figure_id": "F216",
    "report_id": "R026",
    "label": "Exhibit 3",
    "context": "Difference between top and bottom quartiles CAGR FOR TOP AND BOTTOM QUARTILE, 2021–2023 Sources: Capital IQ; Pitchbook; companies' investor presentations; desktop research; BCG Fintech Control Tower; BCG analysis. Sources: Capital IQ; Pitchbook; companies' inv"
  },
  {
    "figure_id": "F217",
    "report_id": "R026",
    "label": "Exhibit 3",
    "context": "CAGR FOR TOP AND BOTTOM QUARTILE, 2021–2023 Sources: Capital IQ; Pitchbook; companies' investor presentations; desktop research; BCG Fintech Control Tower; BCG analysis. Sources: Capital IQ; Pitchbook; companies' investor presentations; desktop research; BCG F"
  },
  {
    "figure_id": "F218",
    "report_id": "R026",
    "label": "Exhibit 3",
    "context": "Sources: Capital IQ; Pitchbook; companies' investor presentations; desktop research; BCG Fintech Control Tower; BCG analysis. Sources: Capital IQ; Pitchbook; companies' investor presentations; desktop research; BCG Fintech Control Tower; BCG analysis. Note: Da"
  },
  {
    "figure_id": "F219",
    "report_id": "R026",
    "label": "Exhibit 4",
    "context": "Despite all of the investments and changes underway, the jury is still out in terms of near-term impact and whether “this time it’s different” for digital assets. # Exhibit 4 The Embedded Finance Market Will Be Worth More Than \\$320 Billion in Revenues by 2030"
  },
  {
    "figure_id": "F220",
    "report_id": "R026",
    "label": "Exhibit 5",
    "context": "## Exhibit 5 GenAI Will Be a Game-Changer for Enhanced Productivity GenAI is already being rolled out at scale with huge productivity benefits GENAI USE CASES AND INDUSTRY EXAMPLES Fintechs will see more near-term benefits from GenAI given their “digital first"
  },
  {
    "figure_id": "F221",
    "report_id": "R026",
    "label": "Exhibit 6",
    "context": "\\- Build compliance muscle. In addition to the cost and revenue levers detailed earlier, fintechs can prepare for a successful IPO and beyond by taking a robust, end-to-end view of compliance to mitigate the risk and impact of future regulatory actions and giv"
  },
  {
    "figure_id": "F222",
    "report_id": "R026",
    "label": "Exhibit 8",
    "context": "Where RTP has taken off is in markets where DPI has been comprehensively implemented. In India, the number of monthly real-time payments has grown by five times in the last three years, from 2.6 billion to 13.3 billion. $^{5}$ The availability of an alias dire"
  },
  {
    "figure_id": "F223",
    "report_id": "R026",
    "label": "Exhibit 8",
    "context": "## Exhibit 8 How a Digital Public Infrastructure Enables Private Creators to Innovate India's DPI stack has government-defined protocols throughout three layers, which in turn enable private innovation Sources: Companies' investor presentations; desktop resear"
  },
  {
    "figure_id": "F224",
    "report_id": "R028",
    "label": "EXHIBIT 1",
    "context": "## EXHIBIT 1 How the Factory of the Future Significantly Lowers Conversion Costs Coffee roasting and packaging company Germany Note: FoF = Factory of the Future. Other conversion costs include cost of energy, depreciation costs, and other operational expenditu"
  },
  {
    "figure_id": "F225",
    "report_id": "R028",
    "label": "EXHIBIT 2",
    "context": "## EXHIBIT 2 # FoF Impact Is Greater in High-Cost Regions but Varies by Sector FoF impact on production costs in China and Germany to serve the German market Food processing Note: FoF = Factory of the Future. Cost includes conversion costs (cost of energy, lab"
  },
  {
    "figure_id": "F226",
    "report_id": "R028",
    "label": "Exhibit 4",
    "context": "global manufacturing survey, 87% of respondents indicated that access to talent and skills becomes more critical to sustaining a FoF deployment. And 69% said the same of infrastructure—with digital infrastructure ranking as the most critical component within i"
  },
  {
    "figure_id": "F227",
    "report_id": "R028",
    "label": "Exhibit 5",
    "context": "6. Business Context. This includes brownfield versus greenfield investment and other decisions that influence which production locations are most competitive. To capture how business context interacts with the five factors above, we built a Manufacturing Compe"
  },
  {
    "figure_id": "F228",
    "report_id": "R028",
    "label": "Exhibit 6",
    "context": "\\- Infrastructure and utilities (access to electricity, access to water and utilities, digital and tech infrastructure, logistics providers, road conditions) \\- Market and supply chain (market size, market growth, presence of competitors, availability of raw m"
  },
  {
    "figure_id": "F229",
    "report_id": "R028",
    "label": "Exhibit 7",
    "context": "In greenfield settings, by contrast, FoF capabilities can be embedded from the outset, making site selection more responsive to underlying differences in operating cost and initial one-offs (cost of land and factory building). Here, the Germany-versus-China co"
  },
  {
    "figure_id": "F230",
    "report_id": "R028",
    "label": "EXHIBIT 7",
    "context": "Americas. Tariff-driven trade realignments are creating short-term uncertainty—most companies have deferred strategic decisions on production location waiting for clarity that has yet to materialize. Beyond these immediate dynamics, investing in the FoF and it"
  },
  {
    "figure_id": "F231",
    "report_id": "R030",
    "label": "Exhibit 1",
    "context": "The MY Family study is based on a nationally representative survey of over 1,500 Malaysian citizen households, conducted in April 2026. [Exhibit 1]. ## EXHIBIT 1 ## Survey sample composition Location $^{2,3}$ Urban/Rural $^{3}$ Monthly Household Income $^{2}$ "
  },
  {
    "figure_id": "F232",
    "report_id": "R030",
    "label": "Exhibit 2",
    "context": "## Four family structures, each member with a role to play Malaysia's families are broadly characterized across four family structures of (1) multigenerational, (2) nuclear, (3) nested, and (4) independent, where each member has their own role to play. [Exhibi"
  },
  {
    "figure_id": "F233",
    "report_id": "R030",
    "label": "EXHIBIT 3",
    "context": "## EXHIBIT 3 and support—regardless of which way the age gap leans. Together, these form four primary structures of the Malaysian family. [Exhibit 3.] ## Four Malaysian family structures ## Not with elders Children No Kids"
  },
  {
    "figure_id": "F234",
    "report_id": "R030",
    "label": "Exhibit 4",
    "context": "## Together with elders 14% Nested ## Decision-making roles While earnings may be equal, the guiding factors for family decisions are less evenly split [Exhibit 4]. 73% of husbands are involved in all decision making for families. On the other hand, only 56% o"
  },
  {
    "figure_id": "F235",
    "report_id": "R030",
    "label": "Exhibit 4",
    "context": "14% Nested ## Decision-making roles While earnings may be equal, the guiding factors for family decisions are less evenly split [Exhibit 4]. 73% of husbands are involved in all decision making for families. On the other hand, only 56% of wives are involved in "
  },
  {
    "figure_id": "F236",
    "report_id": "R030",
    "label": "EXHIBIT 4",
    "context": "However, patriarchal does not mean unilateral. Our findings show that Malaysian families often act in consensus, with the majority of decisions made by many, not by one. ## EXHIBIT 4 ## Involvement in household decision-making \\~70% of husbands are involved in"
  },
  {
    "figure_id": "F237",
    "report_id": "R030",
    "label": "EXHIBIT 5",
    "context": "## EXHIBIT 5 ## Primary decision-maker by spending category While husband or wife is the primary decision maker, decision-making still takes consideration from multiple family members Primary decision maker and number of people involved in the decision Two imp"
  },
  {
    "figure_id": "F238",
    "report_id": "R030",
    "label": "Exhibit 6",
    "context": "Two important family dynamics shift over time—children gain more say as they grow older, while elders gradually cede ground. In multigenerational households, elders and husbands compete for influence at early stages, but in a familiar pattern, elders step back"
  },
  {
    "figure_id": "F239",
    "report_id": "R030",
    "label": "EXHIBIT 7",
    "context": "## EXHIBIT 7 ## Who are the earners in the household ## Husbands earn in \\~80% of families, wives earn in \\~60% ## Who are the income earners by family structure (% of families) ## “ He is still the breadwinner. I feel a man, a father, a husband should take th"
  },
  {
    "figure_id": "F240",
    "report_id": "R030",
    "label": "Exhibit 8",
    "context": "## “ He is still the breadwinner. I feel a man, a father, a husband should take that role. [But when it comes to the day-to-day, groceries, bills], Usually I handle it. If I do not handle it, someone will forget to pay, especially my husband. ALIA Mother, Mult"
  },
  {
    "figure_id": "F241",
    "report_id": "R030",
    "label": "Exhibit 8",
    "context": "He is still the breadwinner. I feel a man, a father, a husband should take that role. [But when it comes to the day-to-day, groceries, bills], Usually I handle it. If I do not handle it, someone will forget to pay, especially my husband. ALIA Mother, Multigene"
  },
  {
    "figure_id": "F242",
    "report_id": "R030",
    "label": "Exhibit 8",
    "context": "If wives contribute nearly half of household income but remain largely invisible in labor force statistics, what are we missing about women's economic participation? When both spouses work, the split of earnings is equal. That's shown in the fact that dual-inc"
  },
  {
    "figure_id": "F243",
    "report_id": "R030",
    "label": "EXHIBIT 8",
    "context": "## EXHIBIT 8 ## Income split in dual and multi-earner households Income is almost a 50/50 split in dual income families; in 3 income families the load is partially redistributed to elders ## What is the median income split among income earners? Earns \\~50% of "
  },
  {
    "figure_id": "F244",
    "report_id": "R030",
    "label": "Exhibit 9",
    "context": "Who controls the purse strings is an important consideration in any family. Our research shows that this is often shaped by the income and decision-making dynamics outlined earlier. The husband directs the majority of family expenditures, managing larger capit"
  },
  {
    "figure_id": "F245",
    "report_id": "R030",
    "label": "Exhibit 9",
    "context": "managing larger capital expenses such as housing and vehicle financing. The wife follows closely, spending on day-to-day consumption such as groceries. In multigenerational families, elders spend less than 4% of household spending. [Exhibit 9.] ## EXHIBIT 9 ##"
  },
  {
    "figure_id": "F246",
    "report_id": "R030",
    "label": "EXHIBIT 9",
    "context": "## EXHIBIT 9 ## Expenditure patterns by family structure"
  },
  {
    "figure_id": "F247",
    "report_id": "R030",
    "label": "Exhibit 10",
    "context": "## Urban versus rural We've talked about the division in families, but what about the differentiation of where families live? Life in a kampung has different needs and demands than life in a city like KL. The share of family structure is one prominent example—"
  },
  {
    "figure_id": "F248",
    "report_id": "R030",
    "label": "Exhibit 10",
    "context": "## Urban versus rural We've talked about the division in families, but what about the differentiation of where families live? Life in a kampung has different needs and demands than life in a city like KL. The share of family structure is one prominent example—"
  },
  {
    "figure_id": "F249",
    "report_id": "R030",
    "label": "Exhibit 10",
    "context": "## Urban versus rural We've talked about the division in families, but what about the differentiation of where families live? Life in a kampung has different needs and demands than life in a city like KL. The share of family structure is one prominent example—"
  },
  {
    "figure_id": "F250",
    "report_id": "R030",
    "label": "EXHIBIT 10",
    "context": "## EXHIBIT 10 ## Urban versus rural family dynamics Urban families pool together, with more multigenerational families... Family structure ...and more earners in the same family... No. of earners ...to make \\~2x a typical rural family Median income"
  },
  {
    "figure_id": "F251",
    "report_id": "R030",
    "label": "Exhibit 11",
    "context": "Foundations first, discretionary deferred First one would be healthcare, in the sense of insurance. Secondly, the education. RAJ Father, Nuclear Family ## EXHIBIT 11 ## Top household priorities ranked by significance"
  },
  {
    "figure_id": "F252",
    "report_id": "R030",
    "label": "Exhibit 11",
    "context": "## EXHIBIT 11 ## Top household priorities ranked by significance Looking at how Malaysian families group similar dreams provides an illustration of this sentiment. [Exhibit 12.] Foundational priorities are highly significant and largely shared. Discretionary p"
  },
  {
    "figure_id": "F253",
    "report_id": "R030",
    "label": "EXHIBIT 11",
    "context": "## EXHIBIT 11 ## Top household priorities ranked by significance Looking at how Malaysian families group similar dreams provides an illustration of this sentiment. [Exhibit 12.] Foundational priorities are highly significant and largely shared. Discretionary p"
  },
  {
    "figure_id": "F254",
    "report_id": "R030",
    "label": "Exhibit 12",
    "context": "Looking at how Malaysian families group similar dreams provides an illustration of this sentiment. [Exhibit 12.] Foundational priorities are highly significant and largely shared. Discretionary priorities are less significant and more likely to diverge. The ga"
  },
  {
    "figure_id": "F255",
    "report_id": "R030",
    "label": "Exhibit 13",
    "context": "If two-thirds of Malaysian families are still in survival mode, is the high-income nation agenda reaching households or only headlines? ## A generational divide If income barely shifts priority orientation but children shift it dramatically, does Malaysia's de"
  },
  {
    "figure_id": "F256",
    "report_id": "R030",
    "label": "EXHIBIT 13",
    "context": "Children are the second most powerful factor influencing the divide between a focus on stability and a dream of more discretionary delights. There is an 11-percentage-point gap between families with and without children. Income, surprisingly, shifts orientatio"
  },
  {
    "figure_id": "F257",
    "report_id": "R030",
    "label": "Exhibit 14",
    "context": "## Determinants of foundational versus discretionary orientation Priority leaning (more foundational vs more discretionary) ## How do Families Spend? ## Healthcare: the vulnerable come first borrowing. [Exhibit 14.] This fragility extends well into the M40 gro"
  },
  {
    "figure_id": "F258",
    "report_id": "R030",
    "label": "Exhibit 14",
    "context": "borrowing. [Exhibit 14.] This fragility extends well into the M40 group. The stark reality is that many Malaysian families are one medical emergency away from financial distress. ## EXHIBIT 14 ## Capacity to cover healthcare emergencies % of families who could"
  },
  {
    "figure_id": "F259",
    "report_id": "R030",
    "label": "EXHIBIT 15",
    "context": "## Capacity to cover healthcare emergencies % of families who could cover a healthcare expense without borrowing or using private health insurance If a single medical bill can financially destabilize three in four Malaysian families, is the current mix of publ"
  },
  {
    "figure_id": "F260",
    "report_id": "R030",
    "label": "EXHIBIT 15",
    "context": "Most families satisfied with govt. healthcare ## EXHIBIT 15 # Satisfaction for government and private healthcare ## However, this is driven primarily by cost-savings; private wins on other metrics The age of a patient also impacts healthcare decisions. [Exhibi"
  },
  {
    "figure_id": "F261",
    "report_id": "R030",
    "label": "EXHIBIT 15",
    "context": "## EXHIBIT 15 # Satisfaction for government and private healthcare ## However, this is driven primarily by cost-savings; private wins on other metrics The age of a patient also impacts healthcare decisions. [Exhibit 16.] Children and elders are the cause of mo"
  },
  {
    "figure_id": "F262",
    "report_id": "R030",
    "label": "Exhibit 16",
    "context": "The age of a patient also impacts healthcare decisions. [Exhibit 16.] Children and elders are the cause of most concern, with half of families going straight to the doctor when these cohorts are ill. For adults it's just $19\\%$ , instead choosing to observe, s"
  },
  {
    "figure_id": "F263",
    "report_id": "R030",
    "label": "Exhibit 17",
    "context": "## We spend the most time and money to secure health, especially for my parents and our children. I've had insurance for my children from when he was 1 month old. GARY Father, Multigenerational Family Health insurance provides another opportunity for stability"
  },
  {
    "figure_id": "F264",
    "report_id": "R030",
    "label": "EXHIBIT 17",
    "context": "## EXHIBIT 17 ## Children's impact on insurance attitudes ## Parents are willing to sacrifice to protect their children Perceptions on insurance (% of families) ## Savings: Pooled together to enjoy together Families are fundamentally a support mechanism, and t"
  },
  {
    "figure_id": "F265",
    "report_id": "R030",
    "label": "Exhibit 18",
    "context": "## Savings: Pooled together to enjoy together Families are fundamentally a support mechanism, and that's clearly true in how Malaysian families treat their finances. [Exhibit 18.] With only \\~20% of their income available to save, families opt to pool their re"
  },
  {
    "figure_id": "F266",
    "report_id": "R030",
    "label": "EXHIBIT 18",
    "context": "## EXHIBIT 18 ## Savings behavior and banking patterns Families can only save between 15-20% of their income... ...so they choose to pool their income and save together... Income management and savings style ...through instruments provided by a single bank Que"
  },
  {
    "figure_id": "F267",
    "report_id": "R030",
    "label": "Exhibit 19",
    "context": "Families can only save between 15-20% of their income... ...so they choose to pool their income and save together... Income management and savings style ...through instruments provided by a single bank Question: How much is spent across the following categorie"
  },
  {
    "figure_id": "F268",
    "report_id": "R030",
    "label": "Exhibit 19",
    "context": "...so they choose to pool their income and save together... Income management and savings style ...through instruments provided by a single bank Question: How much is spent across the following categories (e.g., food, housing, groceries, savings, etc); Do you "
  },
  {
    "figure_id": "F269",
    "report_id": "R030",
    "label": "Exhibit 19",
    "context": "So just how do Malaysian families direct those savings? Most families rely on conservative, safe and liquid instruments: ASB/ASNB, EPF top ups, fixed deposits, Tabung Haji, gold. [Exhibit 19.] Higher-income families diversify into equities and real estate, but"
  },
  {
    "figure_id": "F270",
    "report_id": "R030",
    "label": "Exhibit 21",
    "context": "Which of the below big events are likely to take place in the family in the next 12 months? (% of respondents) ## % of families When family savings are structured around life events, and not life itself, what does this mean for long-term wealth building and wh"
  },
  {
    "figure_id": "F271",
    "report_id": "R030",
    "label": "Exhibit 21",
    "context": "Individual activities rank as less prominent priorities. [Exhibit 21.] Malaysian families clearly want to enjoy their time together. ## EXHIBIT 21 ## Unmet leisure aspirations Top unmet leisure aspirations are activities the family can do together such as geta"
  },
  {
    "figure_id": "F272",
    "report_id": "R030",
    "label": "EXHIBIT 22",
    "context": "## EXHIBIT 22 ## Mall outings are a family experience ## Top 6 reasons to go to the mall can be shared family experiences What are the top reasons your family visits a mall? (% of respondents) Question: What are the top reasons your household visits a mall? Tr"
  },
  {
    "figure_id": "F273",
    "report_id": "R030",
    "label": "EXHIBIT 23",
    "context": "EXHIBIT 23 # Travel as a collectively decided expense Travel is the most collectively decided expense among families \\# of family members involved in decisions \\~40% of families plan ahead and save for travel We decide where to travel to together, but the ulti"
  },
  {
    "figure_id": "F274",
    "report_id": "R030",
    "label": "Exhibit 24",
    "context": "We decide where to travel to together, but the ultimate decision is made by mom. The most important thing is a new experience where we get to sleep somewhere other than our own home. YAYA Daughter, Multigenerational Family ## Education: investing in the next g"
  },
  {
    "figure_id": "F275",
    "report_id": "R030",
    "label": "Exhibit 24",
    "context": "Daughter, Multigenerational Family ## Education: investing in the next generation There is no stronger parental desire than to see your children succeed. That is reflected in family education decisions. While 55% of parents hold a bachelor's degree and just 7%"
  },
  {
    "figure_id": "F276",
    "report_id": "R030",
    "label": "EXHIBIT 24",
    "context": "When $46 \\%$ of parents are willing to sacrifice their retirement for their children’s education, who supports those parents in their old age? With increasing prominence of lifelong learning, how do we shift towards a more dual-priority mindset to upskill both"
  },
  {
    "figure_id": "F277",
    "report_id": "R030",
    "label": "Exhibit 25",
    "context": "## ...and are willing to sacrifice for education Financial sacrifices for education Enhancing educational opportunities is also a priority. [Exhibit 25.] Three-quarters (77%) of families invest in supplementary education. Only 36% believe school alone is suffi"
  },
  {
    "figure_id": "F278",
    "report_id": "R030",
    "label": "EXHIBIT 25",
    "context": "EXHIBIT 25 ## Additional educational activities and trust in the system Only 23% of families have no form of additional educational activities... ## % of families with additional activities Perception of education system ...as less than half of families trust "
  },
  {
    "figure_id": "F279",
    "report_id": "R030",
    "label": "Exhibit 26",
    "context": "...as less than half of families trust the system of families believe that the govt. can make the right education reforms Question: Which of the following additional activities or enrichment programmes do your children participate in? (multi-select); To what e"
  },
  {
    "figure_id": "F280",
    "report_id": "R030",
    "label": "EXHIBIT 26",
    "context": "EXHIBIT 26 # Telco usage and switching factors Families don't consolidate, they use whatever each person signed up with \\# of providers per family Price would be the main factor to switch to another provider, not convenience Reasons to potentially switch telco"
  },
  {
    "figure_id": "F281",
    "report_id": "R030",
    "label": "Exhibit 27",
    "context": "Price would be the main factor to switch to another provider, not convenience Reasons to potentially switch telco providers Question: Mobile service provider per household member; Please rank the following factors in order of importance when considering switch"
  },
  {
    "figure_id": "F282",
    "report_id": "R030",
    "label": "Exhibit 27",
    "context": "# How are Trade-offs Made? ## Income determines progress How do Malaysian families achieve progress towards their dreams? Higher-income households work on more priorities simultaneously and progress faster on each one. [Exhibit 27.] The financial differences m"
  },
  {
    "figure_id": "F283",
    "report_id": "R030",
    "label": "EXHIBIT 27",
    "context": "If B40, M40, and T20 families share the same priorities, but only income separates their outcomes, are the barriers primarily about earnings, or about the cost of the products and services families need? ## EXHIBIT 27 ## Activity and progress on priorities by "
  },
  {
    "figure_id": "F284",
    "report_id": "R030",
    "label": "EXHIBIT 28",
    "context": "## Activity and progress on priorities by income Higher-income families are actively working on more priorities and progressing faster Question: Please describe your household's current progress on its top 5 priorities ## Four archetypes of the Malaysian famil"
  },
  {
    "figure_id": "F285",
    "report_id": "R030",
    "label": "Exhibit 28",
    "context": "a view into four main archetypes split by demographics, financial resources, and proximity to achieving their dreams. [Exhibit 28.] ## Four archetypes of the Malaysian family ## Foundations 24% Firefighters Focused on core pillars but still building the founda"
  },
  {
    "figure_id": "F286",
    "report_id": "R030",
    "label": "Exhibit 29",
    "context": "Foundations in place and actively building beyond, each pillar reinforced, each aspiration within reach Younger T20 families, with no kids with support from elders Discretionary ## Firefighters (24%) Firefighters are fighting to build solid foundations. They t"
  },
  {
    "figure_id": "F287",
    "report_id": "R030",
    "label": "EXHIBIT 29",
    "context": "“We live moderately, not extravagantly, but we still have what we need. We pool money together, and when we have extra money we try to set it aside. The most important thing is that the children are happy and have enough education and knowledge.” Mother, Firef"
  },
  {
    "figure_id": "F288",
    "report_id": "R030",
    "label": "EXHIBIT 29",
    "context": "Mother, Firefighter Family ## EXHIBIT 29 Understanding Firefighters ## Builders (44%) Builders reflect the Malaysian middle class in its most recognizable form. This archetype skews urban, M40 and T20, with millennial and Gen X heads of family. [Exhibit 30.] T"
  },
  {
    "figure_id": "F289",
    "report_id": "R030",
    "label": "EXHIBIT 29",
    "context": "## EXHIBIT 29 Understanding Firefighters ## Builders (44%) Builders reflect the Malaysian middle class in its most recognizable form. This archetype skews urban, M40 and T20, with millennial and Gen X heads of family. [Exhibit 30.] They are predominantly nucle"
  },
  {
    "figure_id": "F290",
    "report_id": "R030",
    "label": "EXHIBIT 30",
    "context": "“Me and my wife contribute the income and manage it together. We have had savings for a while now. We spend most the time and money in securing health, so that we can travel to more places in the future.” ## Father, Builder Family ## EXHIBIT 30 ## Understandin"
  },
  {
    "figure_id": "F291",
    "report_id": "R030",
    "label": "EXHIBIT 30",
    "context": "## Father, Builder Family ## EXHIBIT 30 ## Understanding Builders Father, Aspirant Family"
  },
  {
    "figure_id": "F292",
    "report_id": "R030",
    "label": "EXHIBIT 30",
    "context": "## EXHIBIT 30 ## Understanding Builders Father, Aspirant Family"
  },
  {
    "figure_id": "F293",
    "report_id": "R030",
    "label": "Exhibit 31",
    "context": "Father, Aspirant Family ## Aspirants (19%) Aspirants are the big city dreamers. They are disproportionately urban, B40, and led by a Gen Z heads of household. [Exhibit 31.] They are not typically nuclear families—they skew towards nested and independent struct"
  },
  {
    "figure_id": "F294",
    "report_id": "R030",
    "label": "Exhibit 31",
    "context": "Father, Aspirant Family ## Aspirants (19%) Aspirants are the big city dreamers. They are disproportionately urban, B40, and led by a Gen Z heads of household. [Exhibit 31.] They are not typically nuclear families—they skew towards nested and independent struct"
  },
  {
    "figure_id": "F295",
    "report_id": "R030",
    "label": "Exhibit 31",
    "context": "Aspirants are the big city dreamers. They are disproportionately urban, B40, and led by a Gen Z heads of household. [Exhibit 31.] They are not typically nuclear families—they skew towards nested and independent structures, suggesting households still in format"
  },
  {
    "figure_id": "F296",
    "report_id": "R030",
    "label": "EXHIBIT 31",
    "context": "“Sometimes when I get back home early, I will go to gym for workout, and sometimes will play football. We try to travel and spend time together, usually go to hike, short stay near mountain, and have road trips. At least we make sure we go to restaurants and e"
  },
  {
    "figure_id": "F297",
    "report_id": "R030",
    "label": "EXHIBIT 32",
    "context": "\"The focus is on health, travel and future business ownership. Savings is important, but its also important to enjoy time together. We are looking for opportunities to purchase land, but at the same time we are very excited and planning for travelling to Italy"
  },
  {
    "figure_id": "F298",
    "report_id": "R030",
    "label": "Exhibit 33",
    "context": "## Income trade-offs The four archetypes do not just differ in what they prioritize. They differ in how they respond when life gets expensive. [Exhibit 33.] The same pressures—rising cost of living, a medical bill, a child’s school fees—produce fundamentally d"
  },
  {
    "figure_id": "F299",
    "report_id": "R030",
    "label": "EXHIBIT 34",
    "context": "savings, protecting their consumption in the short term at the expense of long-term financial security. The trade-off reveals the archetype: when squeezed, do you protect your lifestyle or protect your savings? ## EXHIBIT 34 ## Expense trade-offs Up to 72% of "
  },
  {
    "figure_id": "F300",
    "report_id": "R030",
    "label": "Exhibit 35",
    "context": "In healthcare, the divide follows income, not priorities. [Exhibit 35.] Firefighters and Aspirants, both primarily B40, default to government facilities first. Builders and Trailblazers, with more financial room, consider private for convenience. Cost is the u"
  },
  {
    "figure_id": "F301",
    "report_id": "R030",
    "label": "EXHIBIT 36",
    "context": "prioritize higher returns, and can afford to. Aspirants sit in the middle with no clear preference, pulled between the caution their income demands and the ambition their mindset craves. ## EXHIBIT 36 ## Savings trade-offs ## Family archetypes spike on differe"
  },
  {
    "figure_id": "F302",
    "report_id": "R030",
    "label": "EXHIBIT 37",
    "context": "## EXHIBIT 37 ## Travel and Leisure trade-offs ## Firefighters barely spend on leisure, builders are most proactive in saving Approach to leisure by archetype (% of families) Aspirants and trailblazers find a way to make travel still work at an affordable pric"
  },
  {
    "figure_id": "F303",
    "report_id": "R030",
    "label": "Exhibit 38",
    "context": "How families make trade-offs for travel (% of families) Education requires a more nuanced view. Since most Aspirants and Trailblazers do not have children, our focus narrows to Firefighters and Builders. Both want to invest in the next generation, but the impa"
  },
  {
    "figure_id": "F304",
    "report_id": "R030",
    "label": "EXHIBIT 38",
    "context": "supplementary activities, structured savings through the National Education Savings Scheme (SSPN), and private tuition. Firefighters share the same ambitions but are cost-constrained at every turn. The gap between these two is not one of values—both dream of a"
  },
  {
    "figure_id": "F305",
    "report_id": "R032",
    "label": "Exhibit 1",
    "context": "Most food and beverage companies have long pursued a strategy that prioritized scale and marketing muscle. The bet was that size and strength could keep heritage brands relevant without breakthrough product and ingredient innovation. These companies put their "
  },
  {
    "figure_id": "F306",
    "report_id": "R032",
    "label": "Exhibit 2",
    "context": "\\- An increasing array of digital- and AI-enabled shopping apps and interfaces These trends are not abating; in fact, they are picking up speed and catalyzing other market forces. UPF categories, which play an outsized role for most major CPG manufacturers, ha"
  },
  {
    "figure_id": "F307",
    "report_id": "R032",
    "label": "Exhibit 3",
    "context": "Sources: NielsenIQ data; Babak Ravandi et al., \"Prevalence of processed foods in major US grocery stores,\" Nature Food, January 13, 2025; BCG analysis. Note: Highly processed according to FPro (Food Processing) score. Across multiple categories, large brands c"
  },
  {
    "figure_id": "F308",
    "report_id": "R032",
    "label": "Exhibit 4",
    "context": "## How Companies Can Adapt The big strategic question involves capital allocation. For the past decade, returning free cash flow to shareholders through dividends and buybacks has been the default value creation tool for many large CPG companies. This model wo"
  },
  {
    "figure_id": "F309",
    "report_id": "R034",
    "label": "Exhibit 1",
    "context": "The primary engine of value creation over the 2021–2025 period remains growth in tangible book value (TBV), the result of strong underwriting income. (See Exhibit 1.) Cash flow contribution (dividends and buybacks) remains the second major lever, while multipl"
  },
  {
    "figure_id": "F310",
    "report_id": "R034",
    "label": "EXHIBIT 2",
    "context": "Top quartile ## EXHIBIT 2 Underwriting Results Drove Performance of Top-Quartile Companies CONTRIBUTION TO RETURN ON TANGIBLE EQUITY, 2021–2025 (PP) Sources: S&P Capital IQ; BCG ValueScience Center; BCG analysis. Note: PP = percentage points; RoTE = return on "
  },
  {
    "figure_id": "F311",
    "report_id": "R034",
    "label": "Exhibit 3",
    "context": "Sources: S&P Capital IQ; BCG ValueScience Center; BCG analysis. Note: PP = percentage points; RoTE = return on tangible equity. RoTE is calculated as pretax operating income gross of interest expenses, as a percentage of year-end tangible book value of equity "
  },
  {
    "figure_id": "F312",
    "report_id": "R034",
    "label": "Exhibit 4",
    "context": "The subsegments of US P&C performed similarly from 2021 through 2025, with TSRs of 17% and 18% for personal and commercial lines, respectively. Behind these figures, however, are signs of diverging markets. (See Exhibit 4.) Commercial lines benefited from a pr"
  },
  {
    "figure_id": "F313",
    "report_id": "R034",
    "label": "Exhibit 5",
    "context": "Sources: S&P Capital IQ; BCG ValueScience Center; BCG analysis. Note: TSRs are weighted by market cap as of January 1, 2021. P&C = property and casualty; PP = percentage point; P/TBV = price to TBV; TBV = tangible book value; TSR = total shareholder return. $^"
  },
  {
    "figure_id": "F314",
    "report_id": "R036",
    "label": "Exhibit 2",
    "context": "The Philippines is one of the fastest-growing large economies with a large population globally, with its attractiveness anchored in four key factors: large scale with strong private institutions and a laissez-faire approach to the market, consumption-led growt"
  },
  {
    "figure_id": "F315",
    "report_id": "R036",
    "label": "Exhibit 2",
    "context": "## Large economic scale supported by macro stability and market-oriented institutions Philippines is one of the fastest growing large economies globally Projected growth vs economic size, 50 largest economies (by nominal GDP) The Philippines sits within a defi"
  },
  {
    "figure_id": "F316",
    "report_id": "R036",
    "label": "EXHIBIT 2",
    "context": "## EXHIBIT 2 Among 100 million+ population emerging markets, the Philippines stands out for growth and stability Peer countries with comparable population scale, income levels, and macroeconomic performance over the last decade This institutional and market-le"
  },
  {
    "figure_id": "F317",
    "report_id": "R036",
    "label": "EXHIBIT 3",
    "context": "## EXHIBIT 3 # Philippines has a more laissez-faire approach to business compared to similarly sized Southeast Asia peers, Vietnam and Indonesia ## State ownership & market presence ## Limited state footprint; market-led delivery State ownership is largely con"
  },
  {
    "figure_id": "F318",
    "report_id": "R036",
    "label": "EXHIBIT 4",
    "context": "## EXHIBIT 4 ## A consumption-led model differentiates the Philippines from Southeast Asia peers PH is a highly consumption-oriented economy relative to peers, similar to Mexico... population and steady household income support from remittances. Over time, ins"
  },
  {
    "figure_id": "F319",
    "report_id": "R036",
    "label": "EXHIBIT 5",
    "context": "## EXHIBIT 5 Remittances to the Philippines continue to grow and exceed peers as a share of GDP ...with a consistent flow of remittances, contributing meaningfully to domestic consumption Remittances to Philippines per year (USD bn) Remittances as share of GDP"
  },
  {
    "figure_id": "F320",
    "report_id": "R036",
    "label": "Exhibit 5",
    "context": "Remittances to the Philippines continue to grow and exceed peers as a share of GDP ...with a consistent flow of remittances, contributing meaningfully to domestic consumption Remittances to Philippines per year (USD bn) Remittances as share of GDP (%) Remittan"
  },
  {
    "figure_id": "F321",
    "report_id": "R036",
    "label": "Exhibit 5",
    "context": "Remittances to Philippines per year (USD bn) Remittances as share of GDP (%) Remittances to PH by"
  },
  {
    "figure_id": "F322",
    "report_id": "R036",
    "label": "Exhibit 7",
    "context": "Rising incomes are further broadening the spending base. Middle-class households are projected to reach 8.8 million by 2035, up from 5.8 million in 2025 $^{6}$ , growing the middle-class share of households by over 50%. This expansion is already reshaping cons"
  },
  {
    "figure_id": "F323",
    "report_id": "R036",
    "label": "EXHIBIT 7",
    "context": "## EXHIBIT 7 # Larger middle class and rising affluence expected to drive continued consumer spending growth Consumer spending growth in the Philippines is expected to outpace major regional peers, supported by rising incomes, a young demographic profile, and "
  },
  {
    "figure_id": "F324",
    "report_id": "R036",
    "label": "Exhibit 8",
    "context": "population growth of approximately 0.8% CAGR through 2030, the country benefits from a structurally expanding labor force and consumer base [Exhibit 8]. EXHIBIT 8 Philippines has the second largest and the youngest population in Southeast Asia, with $\\sim 50\\%"
  },
  {
    "figure_id": "F325",
    "report_id": "R036",
    "label": "EXHIBIT 9",
    "context": "This scale and intensity of engagement signal that digital applications are deeply embedded in everyday behavior in the Philippines, shaping discovery, engagement, and transactions across consumer journeys. As the digital economy approaches US36B in GMV by 202"
  },
  {
    "figure_id": "F326",
    "report_id": "R036",
    "label": "Exhibit 10",
    "context": "## Key historical frictions ## Constrained consumer banking access beyond urban cores Despite rapid growth in digital payments and e-money, the Philippines remains structurally underbanked by regional and global standards. As of 2024, around 50% of adults rema"
  },
  {
    "figure_id": "F327",
    "report_id": "R036",
    "label": "Exhibit 10",
    "context": "Headline improvements in inclusion have been driven primarily by e-money and wallet adoption, rather than the formation of full-service banking relationships. The unbanked share has declined from 69% in 2014 to 50% in 2024 as mobile money expanded, but many us"
  },
  {
    "figure_id": "F328",
    "report_id": "R036",
    "label": "Exhibit 12",
    "context": "## EXHIBIT 12 MSMEs make up the largest share of businesses; access to loans and business services highly constrained vs peer countries Limited access to financial products driven by But loans to MSMEs remain low at 2%, vs. peers \\- the lack of required docume"
  },
  {
    "figure_id": "F329",
    "report_id": "R036",
    "label": "EXHIBIT 15",
    "context": "Underlying payment volumes are supported by strong macroeconomic momentum, with nominal GDP growth of \\~9–10% directly expanding transaction activity. On the consumer side, essential consumption and e-commerce anchor growth, while gradual credit deepening—part"
  },
  {
    "figure_id": "F330",
    "report_id": "R036",
    "label": "EXHIBIT 16",
    "context": "MSME payment flows are expected to see a material increase in digital penetration from a lower base, largely tracking the digitization of consumer commerce payments. As merchants increasingly receive inflows electronically, operational incentives emerge to dig"
  },
  {
    "figure_id": "F331",
    "report_id": "R036",
    "label": "EXHIBIT 17",
    "context": "Universal and commercial banks anchor the formal lending system, concentrating on larger-ticket and secured products and credit cards, typically at lower pricing. Their digital-first counterparts have focused more on lower-ticket, higher-yield products such as"
  },
  {
    "figure_id": "F332",
    "report_id": "R036",
    "label": "EXHIBIT 18",
    "context": "EXHIBIT 18 \\~\\$90 billion in consumer loan balance per 2025, expected to grow to \\~\\$170 billion by 2030 at \\~13% CAGR Consumer outstanding loan balance 2020-30, US\\$ Bn ## Share of digital CAGR Note: Assume constant FX using 2020 exchange rates. Credit card a"
  },
  {
    "figure_id": "F333",
    "report_id": "R036",
    "label": "Exhibit 22",
    "context": "The Philippine financial services landscape spans a wide range of physical-first incumbents alongside an emerging set of digital-first financial institutions [Exhibit 22]. Universal and commercial banks maintain the broadest product and segment coverage, while"
  },
  {
    "figure_id": "F334",
    "report_id": "R036",
    "label": "Exhibit 23",
    "context": "Digital-first financial institutions have stepped in to serve other segments—namely consumer and MSME [Exhibit 23]. Their operating models are especially geared toward smaller, underbanked, and thin-file consumers/MSMEs who historically had limited access to f"
  },
  {
    "figure_id": "F335",
    "report_id": "R036",
    "label": "Exhibit 24",
    "context": "This model has enabled rapid balance sheet growth in the sector's first 4-5 years of operation. Deposits have grown by $\\sim 57\\%$ , and loans by $\\sim 107\\%$ per annum, driven primarily by consumer deposits and unsecured lending alongside a growing base of MS"
  },
  {
    "figure_id": "F336",
    "report_id": "R036",
    "label": "Exhibit 25",
    "context": "## Digital banks have built strong franchises in 4 years of operations Deposit balance among digital banks (PHP Bn) Loan balance among digital banks (PHP Bn) 2025 deposit market share (%) 2025 loan market share (%) # Philippines digital financial services deve"
  },
  {
    "figure_id": "F337",
    "report_id": "R036",
    "label": "Exhibit 25",
    "context": "Loan balance among digital banks (PHP Bn) 2025 deposit market share (%) 2025 loan market share (%) # Philippines digital financial services development vs. global peers Across consumer, MSME, and enterprise segments, digital financial services players in the P"
  },
  {
    "figure_id": "F338",
    "report_id": "R036",
    "label": "Exhibit 25",
    "context": "# Philippines digital financial services development vs. global peers Across consumer, MSME, and enterprise segments, digital financial services players in the Philippines exhibit markedly different breadth and depth of presence [Exhibit 25]. Some platforms ha"
  },
  {
    "figure_id": "F339",
    "report_id": "R036",
    "label": "EXHIBIT 26",
    "context": "In payments, player strategies diverge between generalist platforms and those anchored to specific ecosystems. ## EXHIBIT 26 Overall, maturity of Philippines fintech ecosystem indicated by parity of offerings from Maya as a leading player vs major global peers"
  },
  {
    "figure_id": "F340",
    "report_id": "R038",
    "label": "EXHIBIT 1",
    "context": "The impact on banks is twofold: On the one hand, digital assets question many business models and even the current monetary system, with profound adverse impacts on bank financials and up to 15% of revenues and 30% of profits at risk by 2035. On the other hand"
  },
  {
    "figure_id": "F341",
    "report_id": "R038",
    "label": "EXHIBIT 1",
    "context": "## EXHIBIT 1 Digital Assets Context: Volumes and Growth of the Three Major Asset Classes Sources: rwa.xyz; cryptopolitan; BCG analysis. $^{1}$ Just net inflows, before asset performance. # Framing: Digital Asset Classes and Market Sizing # When financial indus"
  },
  {
    "figure_id": "F342",
    "report_id": "R038",
    "label": "Exhibit 4",
    "context": "Scenario 2 implies digital adoption in a fragmented multi-track system, with prolonged regulatory fragmentation that slows adoption and limits interoperability. Finally, scenario 4 represents a backlash in which digital assets are constrained: in short, a base"
  },
  {
    "figure_id": "F343",
    "report_id": "R038",
    "label": "Exhibit 5",
    "context": "\\- Up to 4% higher RoE for trading businesses, translating into a \\$1+ billion profit opportunity, driven by higher asset turnover, materially lower capital intensity from faster settlement and netting, and structural cost reductions through automation, despit"
  },
  {
    "figure_id": "F344",
    "report_id": "R038",
    "label": "EXHIBIT 7",
    "context": "Importantly, digital RWA is not a single product category, but an infrastructure transition. Adoption is already clustering where there is economic value (collateral mobility, repo settlement, tokenized funds), while more complex asset classes (notably public "
  },
  {
    "figure_id": "F345",
    "report_id": "R038",
    "label": "Exhibit 8",
    "context": "\\- Private Credit, Private Equity • Real Estate Collateral & Repo: Already live and adoption growing • JPM and Broadridge have live platforms for tokenized repos ## Poised for growth Three forces are shaping this trajectory:"
  },
  {
    "figure_id": "F346",
    "report_id": "R038",
    "label": "EXHIBIT 8",
    "context": "## EXHIBIT 8 Digital RWAs Are Expected To Experience Very Strong Growth Progressive scenarios mounting to 16% of total RWAs by 2035 Digital RWA projection (In USD trillion) \"I do believe we're just at the beginning of the tokenization of all assets, from real "
  },
  {
    "figure_id": "F347",
    "report_id": "R038",
    "label": "EXHIBIT 10",
    "context": "$^{1}$ Digital Twin use cases. ## EXHIBIT 10 Digital RWA Use Cases Along the Capital Markets Value Chain ## Real value delivered today Tokenization is already delivering measurable value in high-ROI use cases, where the asset is standardized, the life cycle is"
  },
  {
    "figure_id": "F348",
    "report_id": "R038",
    "label": "EXHIBIT 12",
    "context": "## Personal banking for retail and wealth: Facilitating secure access In Europe, digital assets are no longer peripheral. In many cases, they are already embedded in client portfolios. For example, a BlackRock October 2025 survey (“The next wave of crypto inve"
  },
  {
    "figure_id": "F349",
    "report_id": "R038",
    "label": "Exhibit 17",
    "context": "## Model Risk ## Compliance Risk Reflects programmability and automation, with AML, sanctions, and conduct requirements embedded in transaction logic Discretion decreases while scale/speed increase—raising both the likelihood and severity of control failures F"
  },
  {
    "figure_id": "F350",
    "report_id": "R038",
    "label": "Exhibit 17",
    "context": "Digital assets introduce new categories of risk that arise from technological features without close analogues in traditional finance. (See Exhibit 17.) These risks are new because they reflect structural shifts in how control is exercised and enforced. One su"
  },
  {
    "figure_id": "F351",
    "report_id": "R038",
    "label": "Exhibit 18",
    "context": "US Department of the Treasury. (2023, August 23). Treasury sanctions Tornado Cash for facilitating illicit finance. https://home.treasury.gov/news/press-releases/jy0916 This distinction fundamentally alters how AML must be conducted. (See Exhibit 18.) Risk is "
  },
  {
    "figure_id": "F352",
    "report_id": "R038",
    "label": "Exhibit 19",
    "context": "Digital assets do not require a new philosophy of risk and compliance. But they do require a new operating discipline. Institutions that succeed will be those in which governance, escalation, and intervention mechanisms function under speed and uncertainty. Ul"
  },
  {
    "figure_id": "F353",
    "report_id": "R038",
    "label": "EXHIBIT 20",
    "context": "## Resilience: DLT nodes are critical infrastructure with the same standards as payment systems ## EXHIBIT 20 ## Comparison of Governance Options ## Build vs. Partner vs. Buy: The Need for a Clear Decision Framework Most leading banks should see reuse of core "
  },
  {
    "figure_id": "F354",
    "report_id": "R039",
    "label": "Exhibit 1",
    "context": "• Use Fit-for-Purpose Technology and Data 17 How to Accelerate AI Value Creation 19 Appendix • AI Definitions • Survey Methodology # Are You Generating Value from AI? How much value is your company generating from your investments in AI? It’s a question more C"
  },
  {
    "figure_id": "F355",
    "report_id": "R039",
    "label": "Exhibit 2",
    "context": "AI-driven value accrues over time, creating a compounding effect. (See Exhibit 2.) Future-built companies that moved early enjoy outsized benefits across financial and operational fronts, and this performance gap is widening. Future-built firms plan to spend 2"
  },
  {
    "figure_id": "F356",
    "report_id": "R039",
    "label": "Exhibit 3",
    "context": "Our research has found that 70% of potential value from AI is concentrated in core business functions such as sales and marketing, manufacturing, supply chain, and pricing. R&D and innovation alone account for 15% of the total potential value. This continues a"
  },
  {
    "figure_id": "F357",
    "report_id": "R039",
    "label": "EXHIBIT 5",
    "context": "Agents do not operate without humans. Their performance depends on strong human orchestration in redesigned roles. The best companies reconfigure workflows to combine autonomous agents with human oversight, maximizing value and adoption. ## EXHIBIT 5 ## Value "
  },
  {
    "figure_id": "F358",
    "report_id": "R039",
    "label": "Exhibit 6",
    "context": "...Thanks to budget allocation 30% Of companies are spending over 15% of their AI budget on agents Top 5 functions prioritized for agentic AI usage $(\\%)^{2}$ Note: Because of rounding, not all bar segment totals equal 100%. # What Value Generators Do Differen"
  },
  {
    "figure_id": "F359",
    "report_id": "R039",
    "label": "Exhibit 6",
    "context": "Of companies are spending over 15% of their AI budget on agents Top 5 functions prioritized for agentic AI usage $(\\%)^{2}$ Note: Because of rounding, not all bar segment totals equal 100%. # What Value Generators Do Differently Our research shows that regardl"
  },
  {
    "figure_id": "F360",
    "report_id": "R039",
    "label": "EXHIBIT 6",
    "context": "## Pursue a Multiyear Strategic AI Ambition Future-built companies approach AI as board- and CEO-sponsored programs, thereby elevating the agenda above isolated experiments or pilots. Top management translates overall business goals into a multiyear, fully fun"
  },
  {
    "figure_id": "F361",
    "report_id": "R039",
    "label": "EXHIBIT 8",
    "context": "Future-built companies understand the need to move fast, but they are equally attentive to evolving their operating model over time along multiple dimensions. An effective AI operating model does not focus on replacing people with technology; it entails reimag"
  },
  {
    "figure_id": "F362",
    "report_id": "R039",
    "label": "EXHIBIT 8",
    "context": "## EXHIBIT 8 Efficient Prioritization Enables Future-Built Companies to Deploy and Scale More Workflows Faster Future-built companies have over 5x the AI workflows in deployment (\\%)... ... and are up to 2x faster Average number of months required to fully dep"
  },
  {
    "figure_id": "F363",
    "report_id": "R039",
    "label": "Exhibit 9",
    "context": "Clear principles guide the hybrid portfolio strategy. Smart companies focus on core enablers such as data readiness and internal skills—platform-agnostic investments that deliver sustained value. It is also essential to treat the ownership of models and prompt"
  },
  {
    "figure_id": "F364",
    "report_id": "R039",
    "label": "Exhibit 10",
    "context": "(See Exhibit 10.) Our research shows that most roadblocks involve people, organization, and processes. In 2024, companies struggled with aligning AI to the overall strategy and establishing a business case, but now the priority has shifted to more concrete imp"
  },
  {
    "figure_id": "F365",
    "report_id": "R039",
    "label": "EXHIBIT 10",
    "context": "Future-built ## EXHIBIT 10 ## Most AI Roadblocks Involve People, Organization, and Processes BCG's 10-20-70 model Key challenges named by respondents (%) Significantly higher for laggards versus future-built ## Appendix ## AI Definitions"
  },
  {
    "figure_id": "F366",
    "report_id": "R040",
    "label": "Exhibit 1",
    "context": "10 Platform Evolution: From Console Wars to Cloud Wars 13 UGC: Welcome to the New Creator Economy 16 App Stores Opening Up: A Revolution for Distribution 19 Improving Monetization: The New Math of Game Pricing 23 Growth Through Disruption 24 About the Global G"
  },
  {
    "figure_id": "F367",
    "report_id": "R040",
    "label": "Exhibit 2",
    "context": "One ground for optimism is that gamers remain passionate about gaming. Around 55% of gamers in our survey have increased their gaming time over the past six months. In addition, gaming parents told us they are introducing the children to the activity early, cr"
  },
  {
    "figure_id": "F368",
    "report_id": "R040",
    "label": "Exhibit 3",
    "context": "Almost Half of All Gamer Parents' Kids Start Playing Video Games by Age 5, and Two of Their Most Common First Games Contain UGC Today, more than 50% of respondents' children began their digital journey by age 5, and about 77% began playing video games by age 7"
  },
  {
    "figure_id": "F369",
    "report_id": "R040",
    "label": "Exhibit 3",
    "context": "Q: How old was your child when they had their first digital experience? (%) Q: How old was your child when they first started playing video games? (%) Two of the three most popular first games for kids are UGC games: Minecraft and Roblox Q: What was the first "
  },
  {
    "figure_id": "F370",
    "report_id": "R040",
    "label": "EXHIBIT 3",
    "context": "## EXHIBIT 3 Adults Are Driving Growth at Both Ends by Introducing the Next Generation to Gaming and Remaining Engaged Well into Retirement Most children are introduced to gaming by their parents, making adults the primary onboarding channel Q: How was your ch"
  },
  {
    "figure_id": "F371",
    "report_id": "R040",
    "label": "EXHIBIT 4",
    "context": "Q: How was your child first introduced to video games? (%) Sources: BCG Global Gaming Survey (N = 2,972); BCG analysis. Note: Because of rounding not all bar chart totals add up to 100%. Boomers continue gaming into retirement, signaling long-term engagement Q"
  },
  {
    "figure_id": "F372",
    "report_id": "R040",
    "label": "EXHIBIT 4",
    "context": "## EXHIBIT 4 # Younger Gamers Prefer Consoles, Particularly PlayStation and Switch, While Gen X and Boomers Spend More Time Gaming on Mobile ## RESPONDENT'S PRIMARY GAMING PLATFORM, BY GENERATION (%) \\- Console gamers tend to be younger, as consoles—Xbox, Swit"
  },
  {
    "figure_id": "F373",
    "report_id": "R040",
    "label": "EXHIBIT 5",
    "context": "Players, however, are generally not concerned. In our Global Gaming Survey, the most significant point of resistance involved adult gamers reacting to AI for generating art/animation; but even there, only 10% had a negative view. Likewise, just 7% of adult gam"
  },
  {
    "figure_id": "F374",
    "report_id": "R040",
    "label": "EXHIBIT 5",
    "context": "## EXHIBIT 5 ## GenAI Is Becoming More Common in Game Development ## Approximately one-fifth of titles released in Q3 2025 disclosed AI integration The top three genres disclosing AI use are casual (20%), adventure (16%), and action (14%) Note: NPC = nonplayer"
  },
  {
    "figure_id": "F375",
    "report_id": "R040",
    "label": "EXHIBIT 6",
    "context": "## Approximately one-fifth of titles released in Q3 2025 disclosed AI integration The top three genres disclosing AI use are casual (20%), adventure (16%), and action (14%) Note: NPC = nonplayer character. Asset creation is the main use; narrative, audio, and "
  },
  {
    "figure_id": "F376",
    "report_id": "R040",
    "label": "EXHIBIT 6",
    "context": "The top three genres disclosing AI use are casual (20%), adventure (16%), and action (14%) Note: NPC = nonplayer character. Asset creation is the main use; narrative, audio, and user experience are secondary ## EXHIBIT 6 ## How GenAI Is Changing the Games Indu"
  },
  {
    "figure_id": "F377",
    "report_id": "R040",
    "label": "EXHIBIT 6",
    "context": "Asset creation is the main use; narrative, audio, and user experience are secondary ## EXHIBIT 6 ## How GenAI Is Changing the Games Industry ## Driving efficiency Modl.AI and Mighty Build & Test are complementary AI platforms that automate QA, representing the"
  },
  {
    "figure_id": "F378",
    "report_id": "R040",
    "label": "Exhibit 7",
    "context": "Significantly, the gamers in our survey were reacting to features they have not yet experienced. A tsunami of low-grade AI-created games could quickly sour their views. Data from our survey of developers reveals that some are moving fast while many others are "
  },
  {
    "figure_id": "F379",
    "report_id": "R040",
    "label": "EXHIBIT 9",
    "context": "of gamers who tried it reported an overall positive experience However, gamers who use cloud gaming also play on other platforms HOW CLOUD GAMERS APPORTION THEIR GAMING TIME (%) TIME DEVOTED TO CLOUD GAMING (%) Sources: BCG Global Gaming Survey (N = 2,972); BC"
  },
  {
    "figure_id": "F380",
    "report_id": "R040",
    "label": "EXHIBIT 9",
    "context": "Sources: BCG Global Gaming Survey (N = 2,972); BCG analysis. ## EXHIBIT 9 Cloud Gaming Is Ready for Liftoff as the Gaming Experience Improves CLOUD GAMING USERS (MILLIONS) Note: CAGR = compound annual growth rate. CLOUD GAMING MARKET (\\$BILLIONS) ## Seizing th"
  },
  {
    "figure_id": "F381",
    "report_id": "R040",
    "label": "EXHIBIT 10",
    "context": "## EXHIBIT 10 ## Gamers Are Interacting With UGC, but Creators Are Still a Minority More than 40% of gamers are consuming more UGC than they did a year ago... Q: Select how much you agree/disagree with the following statement: I consume more UGC now than I did"
  },
  {
    "figure_id": "F382",
    "report_id": "R040",
    "label": "EXHIBIT 11",
    "context": "Developers that want to harness UGC's power should prioritize building an ecosystem that fits the game and offers the right incentives. ## EXHIBIT 11 Gen Z and Millennials Are Interacting More With UGC; Older Gamers Show Potential Q: Select all the ways you ha"
  },
  {
    "figure_id": "F383",
    "report_id": "R040",
    "label": "Exhibit 13",
    "context": "In addition paying lower fees, developers will gain a range of opportunities through new distribution channels, including the ability to build cross-platform ecosystems that were impossible just a few years ago, deepening player engagement without the need to "
  },
  {
    "figure_id": "F384",
    "report_id": "R040",
    "label": "EXHIBIT 14",
    "context": "## EXHIBIT 14 ## Most Gamers Are Price-Conscious and Are Prepared to Wait for Discounts More than 75% of gamers say prices will heavily impact their purchase choices Q: Please select how much you agree with the following statements: Price significantly influen"
  },
  {
    "figure_id": "F385",
    "report_id": "R040",
    "label": "EXHIBIT 15",
    "context": "Q: Please select how much you agree with the following statements: Price significantly influences my choice of brand/product/service (%) Sources: BCG Global Gaming Survey 2025 (N = 2,972); BCG analysis. About 65% of gamers have tactics to limit their spending "
  },
  {
    "figure_id": "F386",
    "report_id": "R040",
    "label": "EXHIBIT 15",
    "context": "Q: When multiple games in the same franchise are released in the same year, which of the following do you do? (%) ## EXHIBIT 15 Premium Games Are a Good Value, and the Average Launch Price of AAA Games Has Declined When Adjusted for Inflation Consumer cost per"
  },
  {
    "figure_id": "F387",
    "report_id": "R040",
    "label": "EXHIBIT 15",
    "context": "## EXHIBIT 15 Premium Games Are a Good Value, and the Average Launch Price of AAA Games Has Declined When Adjusted for Inflation Consumer cost per hour of entertainment by medium and format for major categories, as of 2025 (\\$) $^{1}$ Sources: BCG GEMS; PQ Med"
  },
  {
    "figure_id": "F388",
    "report_id": "R040",
    "label": "Exhibit 16",
    "context": "## • Alternative monetization will expand rapidly. Many free-to-play games on mobile already deploy these strategies to great effect. As strategies such as in-game transactions and downloadable content increase, the proportion of gamers' spending that goes to "
  },
  {
    "figure_id": "F389",
    "report_id": "R040",
    "label": "EXHIBIT 16",
    "context": "## EXHIBIT 16 Gaming Preferences Reveal Generational Divides in Format and Monetization Models, Including Access-Based Models I prefer live-service games to single-player games (%) I prefer accessing games via subscription over buying individual games (%) \\- I"
  },
  {
    "figure_id": "F390",
    "report_id": "R040",
    "label": "Exhibit 17",
    "context": "Gaming Preferences Reveal Generational Divides in Format and Monetization Models, Including Access-Based Models I prefer live-service games to single-player games (%) I prefer accessing games via subscription over buying individual games (%) \\- In-game adverti"
  },
  {
    "figure_id": "F391",
    "report_id": "R040",
    "label": "Exhibit 17",
    "context": "I prefer live-service games to single-player games (%) I prefer accessing games via subscription over buying individual games (%) \\- In-game advertising will emerge as a stronger revenue stream. Mobile games typically earn 20% of their revenue from advertising"
  },
  {
    "figure_id": "F392",
    "report_id": "R040",
    "label": "EXHIBIT 17",
    "context": "For the money, gaming delivers more value than many other hobbies. This is a sign that the industry needs to work harder on pricing, not just to raise revenue but also to protect the scarcity and visibility that make big games significant events in popular cul"
  },
  {
    "figure_id": "F393",
    "report_id": "R040",
    "label": "Exhibit 18",
    "context": "Gaming accounts for 12.5% of gamers' time spent with media, but only around 3% of media ad spending Sources: BCG GEMS; PQ Media; BCG Global Gaming Survey 2025 (N = 2,972). Around $30\\%$ of gamers wouldn't mind sponsored listings in a games store; hardcore game"
  },
  {
    "figure_id": "F394",
    "report_id": "R040",
    "label": "Exhibit 18",
    "context": "Sources: BCG GEMS; PQ Media; BCG Global Gaming Survey 2025 (N = 2,972). Around $30\\%$ of gamers wouldn't mind sponsored listings in a games store; hardcore gamers are most open to this Q: Agreement with “I don’t mind sponsored listings within my gaming store” "
  },
  {
    "figure_id": "F395",
    "report_id": "R040",
    "label": "EXHIBIT 18",
    "context": "By 2030, we should see an explosion of gaming content, an expansion of the global audience for games, and broadening expectations for omniplatform gaming. We anticipate a healthy, growing market, although there will be on the AAA business model will experience"
  },
  {
    "figure_id": "F396",
    "report_id": "R041",
    "label": "Exhibit 1",
    "context": "Through every chapter of the past 250 years, the United States has harnessed these foundations, not in a fixed economic model but through flexible institutions that have made the next adaptation possible. And it has done so collectively. “We the people”—farmer"
  },
  {
    "figure_id": "F397",
    "report_id": "R041",
    "label": "Exhibit 1",
    "context": "# The United States has cause for celebration. But there are also reasons for reflection. ## Exhibit 1 ## By 1900, the United States had the world's leading economy by size and individual incomes. Real gross domestic product, $^{1}$ 1820–2024, \\$ trillion in 2"
  },
  {
    "figure_id": "F398",
    "report_id": "R041",
    "label": "Exhibit 1",
    "context": "## Exhibit 1 ## By 1900, the United States had the world's leading economy by size and individual incomes. Real gross domestic product, $^{1}$ 1820–2024, \\$ trillion in 2024 Real gross domestic product per capita, $^{2}$ purchasing power parity, 1800–2024 $^{1"
  },
  {
    "figure_id": "F399",
    "report_id": "R041",
    "label": "Exhibit 3",
    "context": "American companies make up more than half of the top 100 firms globally by market capitalization and revenue (Exhibit 3). From start-ups to large corporations, they attract an outsize share of capital from global markets. US firms hold more than half of global"
  },
  {
    "figure_id": "F400",
    "report_id": "R041",
    "label": "Exhibit 4",
    "context": "To be sure, a sizable share of US market capitalization is connected to the technology sector. Yet US firms lead across a range of sectors and are present in the upper echelons of all of them. $^{10}$ US market leadership is not a recent development: The Unite"
  },
  {
    "figure_id": "F401",
    "report_id": "R041",
    "label": "Exhibit 5",
    "context": "McKinsey & Company Fundamentally, US firms' outperformance is rooted in greater dynamism: They exhibit higher rates of labor reallocation, market entry and exit, and growth of young firms. $^{11}$ That dynamism translates to higher national productivity growth"
  },
  {
    "figure_id": "F402",
    "report_id": "R041",
    "label": "Exhibit 6",
    "context": "## The US lead in technology is narrowing as China becomes more competitive. ## Exhibit 6 ## Large US firms lead on investment, outpacing their European counterparts. Capital expenditure and R&D spending of large $^{1}$ US and European $^{2}$ companies, $^{3}$"
  },
  {
    "figure_id": "F403",
    "report_id": "R041",
    "label": "Exhibit 7",
    "context": "This gap in income levels has grown over the past 50 years. Although all income segments have seen real growth, market incomes (wages and asset flows) have grown the most for the top two quintiles. For the bottom 60 percent of the population, more income growt"
  },
  {
    "figure_id": "F404",
    "report_id": "R041",
    "label": "Exhibit 9",
    "context": "McKinsey & Company The United States remains the most competitive economy in the world on a multitude of fronts. Getting to this point has not been a straight path. There were twists and turns, transformations and reinventions. Before contemplating the future,"
  },
  {
    "figure_id": "F405",
    "report_id": "R041",
    "label": "Exhibit 9",
    "context": "# Looking back: Four chapters As we have seen, the United States has been the world's largest economy for more than a century. The rise of American competitiveness did not follow a linear or clear trajectory. Growth and innovation often happened in bursts, aft"
  },
  {
    "figure_id": "F406",
    "report_id": "R041",
    "label": "Exhibit 10",
    "context": "## 1. Agricultural abundance ## American Revolution to the Civil War In its first century-plus, the United States was a predominantly agrarian society. In the South, cotton boomed, making up most of the world market by 1820 and meeting strong demand from the b"
  },
  {
    "figure_id": "F407",
    "report_id": "R041",
    "label": "Exhibit 10",
    "context": "The United States had another natural advantage: navigable waterways. Coastal passages with barrier islands and inland rivers made long-distance shipping efficient. The Mississippi River system alone, made fully accessible by the Louisiana Purchase of 1803, in"
  },
  {
    "figure_id": "F408",
    "report_id": "R041",
    "label": "Exhibit 11",
    "context": "## The Apotheosis of Washington and American innovation circa 1865 The Apotheosis of Washington—a grand fresco depicting George Washington “rising to the heavens in glory” flanked by figures of Liberty and Victory—dominates the US Capitol rotunda ceiling. Comp"
  },
  {
    "figure_id": "F409",
    "report_id": "R041",
    "label": "Exhibit 11",
    "context": "Following the Civil War, the US-led Second Industrial Revolution gained full force, and America emerged as the world's preeminent industrial economy. Society grew more connected, shifting away from its agrarian and relatively isolated beginnings. Agricultural "
  },
  {
    "figure_id": "F410",
    "report_id": "R041",
    "label": "Exhibit 12",
    "context": "By 1832, the United States had more railroad miles than any European country, and by 1870, a larger population. The rapid expansion of railroads was fueled by capital expenditure, which at its height topped 4 percent of GDP annually. This played a critical rol"
  },
  {
    "figure_id": "F411",
    "report_id": "R041",
    "label": "Exhibit 13",
    "context": "Perhaps the single most visible token of US scientific leadership was its rise to dominance in Nobel Prizes. The country surpassed the United Kingdom and Germany in annual science-based prizes in the lead-up to World War II and took the lead on cumulative priz"
  },
  {
    "figure_id": "F412",
    "report_id": "R041",
    "label": "Exhibit 11",
    "context": "## Economic disruptions marked a transition The 1970s saw slowing productivity growth, energy crises, and double-digit rates of inflation. Just as the Great Depression provided a tectonic shift in favor of stronger government involvement, the 1970s economic tu"
  },
  {
    "figure_id": "F413",
    "report_id": "R041",
    "label": "Exhibit 14",
    "context": "Demand for a growing pool of US financial assets grew, attracting capital from a globalizing world. $^{96}$ In the years since 1990, foreign investment in US equities and debt has grown substantially, from the equivalent of 11 percent of GDP in each category t"
  },
  {
    "figure_id": "F414",
    "report_id": "R041",
    "label": "Exhibit 15",
    "context": "Productivity growth has been most concentrated in cities with some of the most flourishing knowledge ecosystems. These “superstar” cities have anchoring sectors and, often, universities. Their productivity has continued to push them ahead of the pack. The thre"
  },
  {
    "figure_id": "F415",
    "report_id": "R041",
    "label": "Exhibit 16",
    "context": "In 1767, Benjamin Franklin wrote: \"America, an immense Territory, favour'd by Nature with all Advantages of Climate, Soil, great navigable Rivers and Lakes, &c. must become a great Country, populous and mighty.\" $^{107}$ He was prescient. Over time, the countr"
  },
  {
    "figure_id": "F416",
    "report_id": "R041",
    "label": "Exhibit 17",
    "context": "Reliable and affordable energy has been an enduring"
  },
  {
    "figure_id": "F417",
    "report_id": "R041",
    "label": "Exhibit 19",
    "context": "The entrepreneurial spirit of the United States was not limited to tech visionaries. It was also embedded in the American people and business community, who have long had the appetite (and means) to adopt and scale new technologies, including those invented el"
  },
  {
    "figure_id": "F418",
    "report_id": "R041",
    "label": "Exhibit 20",
    "context": "## Exhibit 20 Demand for AI fluency and technical AI skills rose between 2023 and 2025. Employees in jobs demanding AI-related skills AI fluency skills, calling for people to use or manage AI Technical AI skills, calling for people to develop or govern AI STEM"
  },
  {
    "figure_id": "F419",
    "report_id": "R041",
    "label": "Exhibit 21",
    "context": "Worker shortages across a range of high- and low-skill occupations are already a concern. Many of the sectors experiencing recent shortages have historically been harder to automate and have seen stubbornly low rates of productivity growth. Healthcare, for exa"
  },
  {
    "figure_id": "F420",
    "report_id": "R041",
    "label": "Exhibit 22",
    "context": "## About half of outstanding Treasuries are set to roll over this year and next. Will demand match supply? ## Exhibit 22 ## US fiscal deficits, including net interest payments, are historically elevated. US federal deficits and defense spending, FY 1975–2035E,"
  },
  {
    "figure_id": "F421",
    "report_id": "R041",
    "label": "Exhibit 23",
    "context": "In the coming era, when technologies such as AI become integral to work and society, power demand is likely to surge further. Growing geopolitical competition also means a likely push to build more domestic manufacturing for critical products like semiconducto"
  },
  {
    "figure_id": "F422",
    "report_id": "R041",
    "label": "Exhibit 24",
    "context": "Geopolitics deepens the conundrum. A total of \\$160 billion of US imports are critical, concentrated, and come from geopolitically distant trading partners (see sidebar “Defining geopolitical distance”). This bull’s-eye of potential exposure may seem small, bu"
  },
  {
    "figure_id": "F423",
    "report_id": "R041",
    "label": "Exhibit 25",
    "context": "By this measure, Europe, Japan, South Korea, and the United States sit near one end of a spectrum, while China and Russia sit closer to the other end (Exhibit 25). Most emerging markets sit somewhere in the middle. Of course, relations between countries are dy"
  },
  {
    "figure_id": "F424",
    "report_id": "R043",
    "label": "Exhibit 1",
    "context": "## Wind farm maintenance crew Energy and sustainability Wind farms need to maintain peak efficiency year-round, maximizing clean-energy output while minimizing downtime and operational costs Immersive reality Technicians use augmented reality goggles that prov"
  },
  {
    "figure_id": "F425",
    "report_id": "R043",
    "label": "Exhibit 1",
    "context": "Immersive reality Technicians use augmented reality goggles that provide visual guidance to help them maintain and repair complex turbine systems safely Advanced connectivity Low-Earth-orbit satellites provide technicians with access to real-time data and clou"
  },
  {
    "figure_id": "F426",
    "report_id": "R043",
    "label": "Exhibit 2",
    "context": "McKinsey & Company Note: Data includes private-market and public-market capital raises across venture capital and corporate and strategic M&A (including joint ventures), private equity investments (including buyouts and private investment in public equity), an"
  },
  {
    "figure_id": "F427",
    "report_id": "R043",
    "label": "Exhibit 2",
    "context": "This report lays out considerations for all 13 technology trends. For easier consideration of related trends, we grouped them into three broader categories: the AI revolution, compute and connectivity frontiers, and cutting-edge engineering. Of course, there's"
  },
  {
    "figure_id": "F428",
    "report_id": "R044",
    "label": "Exhibit 1",
    "context": "These findings raise questions about how organizations can build a “test, learn, and adapt” mindset and a culture of continuous improvement, and about how leaders redefine roles and responsibilities in a world in which machines can think, orchestrate, decide, "
  },
  {
    "figure_id": "F429",
    "report_id": "R044",
    "label": "Exhibit 2",
    "context": "One way to tackle such concerns is to build a responsive risk framework that proactively addresses both technical and ethical challenges. Winning employees' buy-in is another path to accelerating adoption at scale. This can be done by identifying high-impact A"
  },
  {
    "figure_id": "F430",
    "report_id": "R044",
    "label": "Exhibit 3",
    "context": "## Exhibit 3 A majority of survey respondents agreed that AI capabilities will bring exponential productivity gains. Organizations' desired outcomes of developing an Al-savvy workforce, % of respondents (n = 7,904) Faster and widespread access to information"
  },
  {
    "figure_id": "F431",
    "report_id": "R044",
    "label": "Exhibit 3",
    "context": "Faster and widespread access to information Note: Respondents were asked to identify their desired outcomes in developing an Al-savvy workforce. ## Benefits of getting it right Leaders see multiple and significant benefits from successfully developing an AI-sa"
  },
  {
    "figure_id": "F432",
    "report_id": "R044",
    "label": "Exhibit 3",
    "context": "Faster and widespread access to information Note: Respondents were asked to identify their desired outcomes in developing an Al-savvy workforce. ## Benefits of getting it right Leaders see multiple and significant benefits from successfully developing an AI-sa"
  },
  {
    "figure_id": "F433",
    "report_id": "R044",
    "label": "Exhibit 6",
    "context": "Finally, regulatory and geopolitical complexities can impede progress. As AI-native GBS drives cross-border data flows, companies need to navigate data privacy, local AI regulations, and geopolitical risk. These factors now shape GBS footprint strategy, determ"
  },
  {
    "figure_id": "F434",
    "report_id": "R044",
    "label": "Exhibit 8",
    "context": "This obstacle is more pronounced in North America (32 percent) and Europe (29 percent) than in the Asia-Pacific region (23 percent). Cultural resistance hits hardest where energy runs low: 45 percent of employees in fatigued organizations see it as a barrier, "
  },
  {
    "figure_id": "F435",
    "report_id": "R044",
    "label": "Exhibit 9",
    "context": "When it comes to workflow redesign, our surveys suggest that resource allocation is often neglected. While a lack of resources and insufficient investment in change are sometimes cited as obstacles to process optimization, the respondents to our survey downpla"
  },
  {
    "figure_id": "F436",
    "report_id": "R044",
    "label": "Exhibit 10",
    "context": "Longer-term impact can be achieved by prioritizing workflows with the highest strategic impact. For example, for product development, this can entail better product–market fit, faster launch cycles, and an optimized innovation pipeline. For integrated planning"
  },
  {
    "figure_id": "F437",
    "report_id": "R044",
    "label": "Exhibit 11",
    "context": "Effective portfolio management requires frequent divestitures of underperforming businesses. Organizations can free up capacity to take bold bets by shedding areas where they are no longer the best owner or letting go of activities that are no longer core to s"
  },
  {
    "figure_id": "F438",
    "report_id": "R044",
    "label": "Exhibit 11",
    "context": "Exhibit 11 The majority of survey respondents, particularly executives, said they are clear about their organization's must-win battles. Organizations' visibility on must-win battles, % of respondents (n = 10,018) McKinsey & Company Organizations that make por"
  },
  {
    "figure_id": "F439",
    "report_id": "R044",
    "label": "Exhibit 12",
    "context": "The priorities can be new geographic markets, products and services, innovation, customer engagement, or price positioning. Leaders then need to ensure that resources are reallocated decisively and identify low-impact and noncore activities for divestment to f"
  },
  {
    "figure_id": "F440",
    "report_id": "R044",
    "label": "Exhibit 13",
    "context": "Build a culture that puts equal weight on employee performance and well-being The goal here is to ensure employees feel energized rather than contained. High performers who sustain their performance over time are driven by purpose, adaptability, and recovery r"
  },
  {
    "figure_id": "F441",
    "report_id": "R044",
    "label": "Exhibit 14",
    "context": "There are stakeholder benefits, too, including for customers and investors. One in four organizations (24 percent) report that prioritizing D&I initiatives leads to broader customer and market appeal, while 31 percent say these initiatives enhance corporate re"
  },
  {
    "figure_id": "F442",
    "report_id": "R044",
    "label": "Exhibit 15",
    "context": "Specifically, reflective leaders are more attuned to external forces and feel stronger performance pressure. More than one in five (22 percent) say that geopolitical shifts are significantly affecting their organizations, compared with 10 percent of leaders wh"
  },
  {
    "figure_id": "F443",
    "report_id": "R045",
    "label": "Exhibit 1",
    "context": "The survey findings also shed light on how organizations are structuring their AI deployment efforts. Some essential elements for deploying AI tend to be fully or partially centralized (Exhibit 1). For risk and compliance, as well as data governance, organizat"
  },
  {
    "figure_id": "F444",
    "report_id": "R045",
    "label": "Exhibit 2",
    "context": "Organizations have employees overseeing the quality of gen AI outputs, though the extent of that oversight varies widely. Twenty-seven percent of respondents whose organizations use gen AI say that employees review all content created by gen AI before it is us"
  },
  {
    "figure_id": "F445",
    "report_id": "R045",
    "label": "Exhibit 3",
    "context": "## Exhibit 3 Respondents report increasing mitigation of inaccuracy, intellectual property infringement, and privacy risks related to use of gen AI. Gen-AI-related risks that organizations are working to mitigate, $^{1}$ % of respondents Intellectual property "
  },
  {
    "figure_id": "F446",
    "report_id": "R045",
    "label": "Exhibit 5",
    "context": "Respondents continue to see these roles as largely challenging to fill, though a smaller share of respondents than in the past two years describe hiring for many roles as “difficult” or “very difficult” (Exhibit 5). One exception is AI data scientists, who wil"
  },
  {
    "figure_id": "F447",
    "report_id": "R045",
    "label": "Exhibit 6",
    "context": "Many respondents also say that their organizations have reskilled portions of their workforces as part of their AI deployment over the past year and that they expect to undertake more reskilling in the years ahead (Exhibit 6). Our latest survey also shows how "
  },
  {
    "figure_id": "F448",
    "report_id": "R045",
    "label": "Exhibit 7",
    "context": "Looking at the expected effects of gen AI deployment by business function, respondents most often predict decreasing head count in service operations, such as customer care and field services, as well as in supply chain and inventory management (Exhibit 7). In"
  },
  {
    "figure_id": "F449",
    "report_id": "R045",
    "label": "Exhibit 9",
    "context": "Organizations are also using AI in more business functions than in the previous State of AI survey. For the first time, most survey respondents report the use of AI in more than one business function (Exhibit 9). Responses show organizations using AI in an ave"
  },
  {
    "figure_id": "F450",
    "report_id": "R045",
    "label": "Exhibit 10",
    "context": "While organizations in all sectors are most likely to use gen AI in marketing and sales, deployment within other functions varies greatly according to industry (Exhibit 10). Organizations are applying the technology where it can generate the most value—for exa"
  },
  {
    "figure_id": "F451",
    "report_id": "R045",
    "label": "Exhibit 11",
    "context": "Note: Figures may not sum to 100%, because of rounding. # More than one-third of respondents say their organizations use gen AI to create images, and more than one-quarter use it to create computer code. Most respondents reporting use of gen AI—63 percent—say "
  },
  {
    "figure_id": "F452",
    "report_id": "R045",
    "label": "Exhibit 11",
    "context": "Note: Figures may not sum to 100%, because of rounding. # More than one-third of respondents say their organizations use gen AI to create images, and more than one-quarter use it to create computer code. Most respondents reporting use of gen AI—63 percent—say "
  },
  {
    "figure_id": "F453",
    "report_id": "R045",
    "label": "Exhibit 11",
    "context": "Most respondents reporting use of gen AI—63 percent—say that their organizations are using gen AI to create text outputs, but organizations are also experimenting with other modalities. More than one-third of respondents say their organizations are generating "
  },
  {
    "figure_id": "F454",
    "report_id": "R045",
    "label": "Exhibit 12",
    "context": "An increasing share of respondents report value creation within the business units using gen AI. Compared with early 2024, larger shares of respondents say that their organizations' gen AI use cases have increased revenue within the business units deploying th"
  },
  {
    "figure_id": "F455",
    "report_id": "R045",
    "label": "Exhibit 12",
    "context": "Exhibit 12 Organizations increasingly see gen AI's effects on revenues in the business units using the technology. Revenue increase within business units from gen AI use, past 12 months, by function, $^{1}$ % of respondents $^{1}$ Questions were asked only of "
  },
  {
    "figure_id": "F456",
    "report_id": "R045",
    "label": "Exhibit 13",
    "context": "McKinsey & Company Overall, respondents are also more likely than in the previous survey to say they are seeing meaningful cost reductions within the business units using gen AI (Exhibit 13). In early 2024, among respondents reporting use of gen AI in specific"
  },
  {
    "figure_id": "F457",
    "report_id": "R045",
    "label": "Exhibit 13",
    "context": "Overall, respondents are also more likely than in the previous survey to say they are seeing meaningful cost reductions within the business units using gen AI (Exhibit 13). In early 2024, among respondents reporting use of gen AI in specific business functions"
  },
  {
    "figure_id": "F458",
    "report_id": "R047",
    "label": "Exhibit 1",
    "context": "Investors are placing more emphasis on which business models can capture the next wave of value, which technologies can create durable advantage, and how far players can extend into adjacent products, geographies, and infrastructure layers while navigating a m"
  },
  {
    "figure_id": "F459",
    "report_id": "R047",
    "label": "Exhibit 1",
    "context": "There has been a striking reversal of mood within the global fintech sector. Two years ago, the sector was still working through the aftershocks of the 2021 reset, a period during which capital was scarce, valuations compressed sharply, and questions about the"
  },
  {
    "figure_id": "F460",
    "report_id": "R047",
    "label": "Exhibit 2",
    "context": "# Global Fintech Revenues Break Half a Trillion Dollars in 2025 Global fintech revenue by vertical (2021–2025, \\$B) Global fintech revenue by region (2021–2025, \\$B) Sources: S&P Capital IQ; BCG FinTech Control Tower; BCG Banking and Insurance Revenue Pools; B"
  },
  {
    "figure_id": "F461",
    "report_id": "R047",
    "label": "EXHIBIT 3",
    "context": "Fintechs account for \\~4% of global financial services revenues TOTAL GLOBAL REVENUE, 2025 (\\$) Fintech revenue growth outpaced incumbents across all verticals FINTECH VS. INCUMBENT REVENUE GROWTH YOY, 2024–2025 (%) $^{1}$ Sources: S&P Capital IQ; Pitchbook; B"
  },
  {
    "figure_id": "F462",
    "report_id": "R047",
    "label": "EXHIBIT 3",
    "context": "Sources: S&P Capital IQ; Pitchbook; BCG FinTech Control Tower; BCG Banking and Insurance Revenue Pools; BCG analysis. $^{1}$ Excludes “financial infrastructure,” as the category is not relevant for incumbent financial institutions. ## EXHIBIT 3 Payments Remain"
  },
  {
    "figure_id": "F463",
    "report_id": "R047",
    "label": "Exhibit 5",
    "context": "Since GCash's explosive growth starting in 2015, the financially excluded population in the Philippines declined from \\~70% to \\~20% Brazil Kenya Philippines Sources: World Bank; UN World Population Prospects; Kenya National Bureau of Statistics; Central Bank "
  },
  {
    "figure_id": "F464",
    "report_id": "R047",
    "label": "Exhibit 5",
    "context": "Brazil Kenya Philippines Sources: World Bank; UN World Population Prospects; Kenya National Bureau of Statistics; Central Bank of Kenya; Safaricom Reports; Philippine Statistics Authority, Bangko Sentral ng Pilipinas FIS, Globe Telecom/Mynt/Gcash Reports; BCG "
  },
  {
    "figure_id": "F465",
    "report_id": "R047",
    "label": "Exhibit 6",
    "context": "Maturation is also evident in where capital is going. Equity funding rose 53% to \\$58 billion in 2025, but funding growth was not evenly distributed. (See Exhibit 6.) Trading and investment fintechs captured roughly one-third of all funding, up from about one-"
  },
  {
    "figure_id": "F466",
    "report_id": "R047",
    "label": "EXHIBIT 6",
    "context": "AVERAGE EBITDA MARGIN (%) SHARE OF FINTECHS ABOVE THE RULE OF $40^{2}$ (\\%) Sources: Financial analysis of the top 85 fintechs, S&P Capital IQ; Pitchbook; BCG FinTech Control Tower; BCG analysis. $^{1}$ Profitability defined as EBITDA or EBT. $^{2}$ Rule of 40"
  },
  {
    "figure_id": "F467",
    "report_id": "R047",
    "label": "EXHIBIT 6",
    "context": "REVENUE MULTIPLE FOR PUBLIC FINTECHS ## EXHIBIT 6 Equity Funding and IPO Activity Have Accelerated, While Valuations Have Grown Moderately FINTECH EQUITY FINANCING (\\$B) 2025 funding rebound has continued into 2026, with Q1 equity funding reaching \\$14.8B, sur"
  },
  {
    "figure_id": "F468",
    "report_id": "R047",
    "label": "EXHIBIT 7",
    "context": "GS Growth Equity ## EXHIBIT 7 AI Is More Than a Tool Upgrade, It Is an Organizational Transformation In a digitally enhanced model, people are the core drivers, with AI tools to boost efficiency Core processes built around people Supplemented by digital tools "
  },
  {
    "figure_id": "F469",
    "report_id": "R047",
    "label": "Exhibit 8",
    "context": "While many of the narratives around consumer-facing autonomous agents still feel premature, some do present glimpses of a potential agentic future. A few AI-native fintechs at the bleeding edge of agentic AI adoption have incorporated agentic AI into everythin"
  },
  {
    "figure_id": "F470",
    "report_id": "R047",
    "label": "EXHIBIT 9",
    "context": "How far can fintech penetrate B2B, and what it will take to win? The answer will depend as much on trust as on product quality. To displace entrenched systems, fintechs must convince clients that the operational risk and complexity of unwinding existing workfl"
  },
  {
    "figure_id": "F471",
    "report_id": "R047",
    "label": "Exhibit 10",
    "context": "We believe that autonomous agentic commerce has a reasonably long path to scale, and may only get there in certain cases. The reasons exist on both the demand side and the supply side. On the former, consumers are more likely to adopt agents where they create "
  },
  {
    "figure_id": "F472",
    "report_id": "R047",
    "label": "Exhibit 11",
    "context": "Trust is a foundational issue across all of these categories, not an isolated problem in any one vertical. Consumers need confidence that the agent is acting within clear boundaries, that mistakes can be corrected easily, and that the downside of delegation is"
  },
  {
    "figure_id": "F473",
    "report_id": "R047",
    "label": "Exhibit 12",
    "context": "# Google Staking a Position in Agentic Commerce The next phase of fintech will not be confined to fintechs themselves. As AI changes how consumers discover, compare, and buy, Google is moving to defend discovery—but its response goes beyond preserving search t"
  },
  {
    "figure_id": "F474",
    "report_id": "R047",
    "label": "EXHIBIT 12",
    "context": "## EXHIBIT 12 # About 7,000 Fintechs Are Building the Digital Asset Ecosystem and Comprise an Increasing Share of Fintech Equity Funding and Revenue SHARE OF ACTIVE FINTECHS, BY DIGITAL ASSETS (COMPANY COUNT) Sources: S&P Capital IQ; Pitchbook; BCG FinTech Con"
  },
  {
    "figure_id": "F475",
    "report_id": "R047",
    "label": "EXHIBIT 14",
    "context": "Sources: BCG FinTech Control Tower. $^{1}$ Cumulative number of digital asset fintech and equity funding attracted from 2000 to 2025 inclusive. ## EXHIBIT 14 ## The Asset Tokenization Flywheel Is Starting to Spin Sources: RWA.xyz; BCG analysis. Note: CBDC = ce"
  },
  {
    "figure_id": "F476",
    "report_id": "R047",
    "label": "EXHIBIT 16",
    "context": "## EXHIBIT 16 Federal Bank Charters and Depository Institution Applications Increased Over 5x from 2024 to 2025 Federal bank charter and new-bank application volume $^{1}$ (2021–2026 Q1) Sources: OCC; FDIC. $^{1}$ Includes OCC national bank / national trust ch"
  },
  {
    "figure_id": "F477",
    "report_id": "R047",
    "label": "Exhibit 18",
    "context": "Despite continued public-market volatility and investor selectivity, IPO and M&A activity are likely to continue at their current levels. Scaled fintechs still need paths to liquidity, and strategic urgency across the sector remains high. But the composition o"
  },
  {
    "figure_id": "F478",
    "report_id": "R047",
    "label": "EXHIBIT 18",
    "context": "## EXHIBIT 18 2025 Saw the Highest Number of M&A Deals and Second-Highest Amount; Scaled Fintechs Were the Most Active Acquirers Scaled fintechs were the most active acquirers in 2025 (COUNT BY ACQUIRER TYPE $^{1}$ ) $^{1}$ Analysis by acquirer type only inclu"
  },
  {
    "figure_id": "F479",
    "report_id": "R048",
    "label": "Exhibit 1",
    "context": "The primary engine of value creation over the 2021–2025 period remains growth in tangible book value (TBV), the result of strong underwriting income. (See Exhibit 1.) Cash flow contribution (dividends and buybacks) remains the second major lever, while multipl"
  },
  {
    "figure_id": "F480",
    "report_id": "R048",
    "label": "EXHIBIT 2",
    "context": "Top quartile ## EXHIBIT 2 Underwriting Results Drove Performance of Top-Quartile Companies CONTRIBUTION TO RETURN ON TANGIBLE EQUITY, 2021–2025 (PP) Sources: S&P Capital IQ; BCG ValueScience Center; BCG analysis. Note: PP = percentage points; RoTE = return on "
  },
  {
    "figure_id": "F481",
    "report_id": "R048",
    "label": "Exhibit 3",
    "context": "Sources: S&P Capital IQ; BCG ValueScience Center; BCG analysis. Note: PP = percentage points; RoTE = return on tangible equity. RoTE is calculated as pretax operating income gross of interest expenses, as a percentage of year-end tangible book value of equity "
  },
  {
    "figure_id": "F482",
    "report_id": "R048",
    "label": "Exhibit 4",
    "context": "The subsegments of US P&C performed similarly from 2021 through 2025, with TSRs of 17% and 18% for personal and commercial lines, respectively. Behind these figures, however, are signs of diverging markets. (See Exhibit 4.) Commercial lines benefited from a pr"
  },
  {
    "figure_id": "F483",
    "report_id": "R048",
    "label": "Exhibit 5",
    "context": "Sources: S&P Capital IQ; BCG ValueScience Center; BCG analysis. Note: TSRs are weighted by market cap as of January 1, 2021. P&C = property and casualty; PP = percentage point; P/TBV = price to TBV; TBV = tangible book value; TSR = total shareholder return. $^"
  },
  {
    "figure_id": "F484",
    "report_id": "R049",
    "label": "Exhibit 1",
    "context": "• Use Fit-for-Purpose Technology and Data 17 How to Accelerate AI Value Creation 19 Appendix • AI Definitions • Survey Methodology # Are You Generating Value from AI? How much value is your company generating from your investments in AI? It’s a question more C"
  },
  {
    "figure_id": "F485",
    "report_id": "R049",
    "label": "Exhibit 2",
    "context": "AI-driven value accrues over time, creating a compounding effect. (See Exhibit 2.) Future-built companies that moved early enjoy outsized benefits across financial and operational fronts, and this performance gap is widening. Future-built firms plan to spend 2"
  },
  {
    "figure_id": "F486",
    "report_id": "R049",
    "label": "Exhibit 3",
    "context": "Our research has found that 70% of potential value from AI is concentrated in core business functions such as sales and marketing, manufacturing, supply chain, and pricing. R&D and innovation alone account for 15% of the total potential value. This continues a"
  },
  {
    "figure_id": "F487",
    "report_id": "R049",
    "label": "EXHIBIT 5",
    "context": "Agents do not operate without humans. Their performance depends on strong human orchestration in redesigned roles. The best companies reconfigure workflows to combine autonomous agents with human oversight, maximizing value and adoption. ## EXHIBIT 5 ## Value "
  },
  {
    "figure_id": "F488",
    "report_id": "R049",
    "label": "Exhibit 6",
    "context": "...Thanks to budget allocation 30% Of companies are spending over 15% of their AI budget on agents Top 5 functions prioritized for agentic AI usage $(\\%)^{2}$ Note: Because of rounding, not all bar segment totals equal 100%. # What Value Generators Do Differen"
  },
  {
    "figure_id": "F489",
    "report_id": "R049",
    "label": "Exhibit 6",
    "context": "Of companies are spending over 15% of their AI budget on agents Top 5 functions prioritized for agentic AI usage $(\\%)^{2}$ Note: Because of rounding, not all bar segment totals equal 100%. # What Value Generators Do Differently Our research shows that regardl"
  },
  {
    "figure_id": "F490",
    "report_id": "R049",
    "label": "EXHIBIT 6",
    "context": "## Pursue a Multiyear Strategic AI Ambition Future-built companies approach AI as board- and CEO-sponsored programs, thereby elevating the agenda above isolated experiments or pilots. Top management translates overall business goals into a multiyear, fully fun"
  },
  {
    "figure_id": "F491",
    "report_id": "R049",
    "label": "EXHIBIT 8",
    "context": "Future-built companies understand the need to move fast, but they are equally attentive to evolving their operating model over time along multiple dimensions. An effective AI operating model does not focus on replacing people with technology; it entails reimag"
  },
  {
    "figure_id": "F492",
    "report_id": "R049",
    "label": "EXHIBIT 8",
    "context": "## EXHIBIT 8 Efficient Prioritization Enables Future-Built Companies to Deploy and Scale More Workflows Faster Future-built companies have over 5x the AI workflows in deployment (\\%)... ... and are up to 2x faster Average number of months required to fully dep"
  },
  {
    "figure_id": "F493",
    "report_id": "R049",
    "label": "Exhibit 9",
    "context": "Clear principles guide the hybrid portfolio strategy. Smart companies focus on core enablers such as data readiness and internal skills—platform-agnostic investments that deliver sustained value. It is also essential to treat the ownership of models and prompt"
  },
  {
    "figure_id": "F494",
    "report_id": "R049",
    "label": "Exhibit 10",
    "context": "(See Exhibit 10.) Our research shows that most roadblocks involve people, organization, and processes. In 2024, companies struggled with aligning AI to the overall strategy and establishing a business case, but now the priority has shifted to more concrete imp"
  },
  {
    "figure_id": "F495",
    "report_id": "R049",
    "label": "EXHIBIT 10",
    "context": "Future-built ## EXHIBIT 10 ## Most AI Roadblocks Involve People, Organization, and Processes BCG's 10-20-70 model Key challenges named by respondents (%) Significantly higher for laggards versus future-built ## Appendix ## AI Definitions"
  },
  {
    "figure_id": "F496",
    "report_id": "R050",
    "label": "Exhibit 1",
    "context": "10 Platform Evolution: From Console Wars to Cloud Wars 13 UGC: Welcome to the New Creator Economy 16 App Stores Opening Up: A Revolution for Distribution 19 Improving Monetization: The New Math of Game Pricing 23 Growth Through Disruption 24 About the Global G"
  },
  {
    "figure_id": "F497",
    "report_id": "R050",
    "label": "Exhibit 2",
    "context": "One ground for optimism is that gamers remain passionate about gaming. Around 55% of gamers in our survey have increased their gaming time over the past six months. In addition, gaming parents told us they are introducing the children to the activity early, cr"
  },
  {
    "figure_id": "F498",
    "report_id": "R050",
    "label": "Exhibit 3",
    "context": "Almost Half of All Gamer Parents' Kids Start Playing Video Games by Age 5, and Two of Their Most Common First Games Contain UGC Today, more than 50% of respondents' children began their digital journey by age 5, and about 77% began playing video games by age 7"
  },
  {
    "figure_id": "F499",
    "report_id": "R050",
    "label": "Exhibit 3",
    "context": "Q: How old was your child when they had their first digital experience? (%) Q: How old was your child when they first started playing video games? (%) Two of the three most popular first games for kids are UGC games: Minecraft and Roblox Q: What was the first "
  },
  {
    "figure_id": "F500",
    "report_id": "R050",
    "label": "EXHIBIT 3",
    "context": "## EXHIBIT 3 Adults Are Driving Growth at Both Ends by Introducing the Next Generation to Gaming and Remaining Engaged Well into Retirement Most children are introduced to gaming by their parents, making adults the primary onboarding channel Q: How was your ch"
  },
  {
    "figure_id": "F501",
    "report_id": "R050",
    "label": "EXHIBIT 4",
    "context": "Q: How was your child first introduced to video games? (%) Sources: BCG Global Gaming Survey (N = 2,972); BCG analysis. Note: Because of rounding not all bar chart totals add up to 100%. Boomers continue gaming into retirement, signaling long-term engagement Q"
  },
  {
    "figure_id": "F502",
    "report_id": "R050",
    "label": "EXHIBIT 4",
    "context": "## EXHIBIT 4 # Younger Gamers Prefer Consoles, Particularly PlayStation and Switch, While Gen X and Boomers Spend More Time Gaming on Mobile ## RESPONDENT'S PRIMARY GAMING PLATFORM, BY GENERATION (%) \\- Console gamers tend to be younger, as consoles—Xbox, Swit"
  },
  {
    "figure_id": "F503",
    "report_id": "R050",
    "label": "EXHIBIT 5",
    "context": "Players, however, are generally not concerned. In our Global Gaming Survey, the most significant point of resistance involved adult gamers reacting to AI for generating art/animation; but even there, only 10% had a negative view. Likewise, just 7% of adult gam"
  },
  {
    "figure_id": "F504",
    "report_id": "R050",
    "label": "EXHIBIT 5",
    "context": "## EXHIBIT 5 ## GenAI Is Becoming More Common in Game Development ## Approximately one-fifth of titles released in Q3 2025 disclosed AI integration The top three genres disclosing AI use are casual (20%), adventure (16%), and action (14%) Note: NPC = nonplayer"
  },
  {
    "figure_id": "F505",
    "report_id": "R050",
    "label": "EXHIBIT 6",
    "context": "## Approximately one-fifth of titles released in Q3 2025 disclosed AI integration The top three genres disclosing AI use are casual (20%), adventure (16%), and action (14%) Note: NPC = nonplayer character. Asset creation is the main use; narrative, audio, and "
  },
  {
    "figure_id": "F506",
    "report_id": "R050",
    "label": "EXHIBIT 6",
    "context": "The top three genres disclosing AI use are casual (20%), adventure (16%), and action (14%) Note: NPC = nonplayer character. Asset creation is the main use; narrative, audio, and user experience are secondary ## EXHIBIT 6 ## How GenAI Is Changing the Games Indu"
  },
  {
    "figure_id": "F507",
    "report_id": "R050",
    "label": "EXHIBIT 6",
    "context": "Asset creation is the main use; narrative, audio, and user experience are secondary ## EXHIBIT 6 ## How GenAI Is Changing the Games Industry ## Driving efficiency Modl.AI and Mighty Build & Test are complementary AI platforms that automate QA, representing the"
  },
  {
    "figure_id": "F508",
    "report_id": "R050",
    "label": "Exhibit 7",
    "context": "Significantly, the gamers in our survey were reacting to features they have not yet experienced. A tsunami of low-grade AI-created games could quickly sour their views. Data from our survey of developers reveals that some are moving fast while many others are "
  },
  {
    "figure_id": "F509",
    "report_id": "R050",
    "label": "EXHIBIT 9",
    "context": "of gamers who tried it reported an overall positive experience However, gamers who use cloud gaming also play on other platforms HOW CLOUD GAMERS APPORTION THEIR GAMING TIME (%) TIME DEVOTED TO CLOUD GAMING (%) Sources: BCG Global Gaming Survey (N = 2,972); BC"
  },
  {
    "figure_id": "F510",
    "report_id": "R050",
    "label": "EXHIBIT 9",
    "context": "Sources: BCG Global Gaming Survey (N = 2,972); BCG analysis. ## EXHIBIT 9 Cloud Gaming Is Ready for Liftoff as the Gaming Experience Improves CLOUD GAMING USERS (MILLIONS) Note: CAGR = compound annual growth rate. CLOUD GAMING MARKET (\\$BILLIONS) ## Seizing th"
  },
  {
    "figure_id": "F511",
    "report_id": "R050",
    "label": "EXHIBIT 10",
    "context": "## EXHIBIT 10 ## Gamers Are Interacting With UGC, but Creators Are Still a Minority More than 40% of gamers are consuming more UGC than they did a year ago... Q: Select how much you agree/disagree with the following statement: I consume more UGC now than I did"
  },
  {
    "figure_id": "F512",
    "report_id": "R050",
    "label": "EXHIBIT 11",
    "context": "Developers that want to harness UGC's power should prioritize building an ecosystem that fits the game and offers the right incentives. ## EXHIBIT 11 Gen Z and Millennials Are Interacting More With UGC; Older Gamers Show Potential Q: Select all the ways you ha"
  },
  {
    "figure_id": "F513",
    "report_id": "R050",
    "label": "Exhibit 13",
    "context": "In addition paying lower fees, developers will gain a range of opportunities through new distribution channels, including the ability to build cross-platform ecosystems that were impossible just a few years ago, deepening player engagement without the need to "
  },
  {
    "figure_id": "F514",
    "report_id": "R050",
    "label": "EXHIBIT 14",
    "context": "## EXHIBIT 14 ## Most Gamers Are Price-Conscious and Are Prepared to Wait for Discounts More than 75% of gamers say prices will heavily impact their purchase choices Q: Please select how much you agree with the following statements: Price significantly influen"
  },
  {
    "figure_id": "F515",
    "report_id": "R050",
    "label": "EXHIBIT 15",
    "context": "Q: Please select how much you agree with the following statements: Price significantly influences my choice of brand/product/service (%) Sources: BCG Global Gaming Survey 2025 (N = 2,972); BCG analysis. About 65% of gamers have tactics to limit their spending "
  },
  {
    "figure_id": "F516",
    "report_id": "R050",
    "label": "EXHIBIT 15",
    "context": "Q: When multiple games in the same franchise are released in the same year, which of the following do you do? (%) ## EXHIBIT 15 Premium Games Are a Good Value, and the Average Launch Price of AAA Games Has Declined When Adjusted for Inflation Consumer cost per"
  },
  {
    "figure_id": "F517",
    "report_id": "R050",
    "label": "EXHIBIT 15",
    "context": "## EXHIBIT 15 Premium Games Are a Good Value, and the Average Launch Price of AAA Games Has Declined When Adjusted for Inflation Consumer cost per hour of entertainment by medium and format for major categories, as of 2025 (\\$) $^{1}$ Sources: BCG GEMS; PQ Med"
  },
  {
    "figure_id": "F518",
    "report_id": "R050",
    "label": "Exhibit 16",
    "context": "## • Alternative monetization will expand rapidly. Many free-to-play games on mobile already deploy these strategies to great effect. As strategies such as in-game transactions and downloadable content increase, the proportion of gamers' spending that goes to "
  },
  {
    "figure_id": "F519",
    "report_id": "R050",
    "label": "EXHIBIT 16",
    "context": "## EXHIBIT 16 Gaming Preferences Reveal Generational Divides in Format and Monetization Models, Including Access-Based Models I prefer live-service games to single-player games (%) I prefer accessing games via subscription over buying individual games (%) \\- I"
  },
  {
    "figure_id": "F520",
    "report_id": "R050",
    "label": "Exhibit 17",
    "context": "Gaming Preferences Reveal Generational Divides in Format and Monetization Models, Including Access-Based Models I prefer live-service games to single-player games (%) I prefer accessing games via subscription over buying individual games (%) \\- In-game adverti"
  },
  {
    "figure_id": "F521",
    "report_id": "R050",
    "label": "Exhibit 17",
    "context": "I prefer live-service games to single-player games (%) I prefer accessing games via subscription over buying individual games (%) \\- In-game advertising will emerge as a stronger revenue stream. Mobile games typically earn 20% of their revenue from advertising"
  },
  {
    "figure_id": "F522",
    "report_id": "R050",
    "label": "EXHIBIT 17",
    "context": "For the money, gaming delivers more value than many other hobbies. This is a sign that the industry needs to work harder on pricing, not just to raise revenue but also to protect the scarcity and visibility that make big games significant events in popular cul"
  },
  {
    "figure_id": "F523",
    "report_id": "R050",
    "label": "Exhibit 18",
    "context": "Gaming accounts for 12.5% of gamers' time spent with media, but only around 3% of media ad spending Sources: BCG GEMS; PQ Media; BCG Global Gaming Survey 2025 (N = 2,972). Around $30\\%$ of gamers wouldn't mind sponsored listings in a games store; hardcore game"
  },
  {
    "figure_id": "F524",
    "report_id": "R050",
    "label": "Exhibit 18",
    "context": "Sources: BCG GEMS; PQ Media; BCG Global Gaming Survey 2025 (N = 2,972). Around $30\\%$ of gamers wouldn't mind sponsored listings in a games store; hardcore gamers are most open to this Q: Agreement with “I don’t mind sponsored listings within my gaming store” "
  },
  {
    "figure_id": "F525",
    "report_id": "R050",
    "label": "EXHIBIT 18",
    "context": "By 2030, we should see an explosion of gaming content, an expansion of the global audience for games, and broadening expectations for omniplatform gaming. We anticipate a healthy, growing market, although there will be on the AAA business model will experience"
  },
  {
    "figure_id": "F526",
    "report_id": "R051",
    "label": "Exhibit 1",
    "context": "Through every chapter of the past 250 years, the United States has harnessed these foundations, not in a fixed economic model but through flexible institutions that have made the next adaptation possible. And it has done so collectively. “We the people”—farmer"
  },
  {
    "figure_id": "F527",
    "report_id": "R051",
    "label": "Exhibit 1",
    "context": "# The United States has cause for celebration. But there are also reasons for reflection. ## Exhibit 1 ## By 1900, the United States had the world's leading economy by size and individual incomes. Real gross domestic product, $^{1}$ 1820–2024, \\$ trillion in 2"
  },
  {
    "figure_id": "F528",
    "report_id": "R051",
    "label": "Exhibit 1",
    "context": "## Exhibit 1 ## By 1900, the United States had the world's leading economy by size and individual incomes. Real gross domestic product, $^{1}$ 1820–2024, \\$ trillion in 2024 Real gross domestic product per capita, $^{2}$ purchasing power parity, 1800–2024 $^{1"
  },
  {
    "figure_id": "F529",
    "report_id": "R051",
    "label": "Exhibit 3",
    "context": "American companies make up more than half of the top 100 firms globally by market capitalization and revenue (Exhibit 3). From start-ups to large corporations, they attract an outsize share of capital from global markets. US firms hold more than half of global"
  },
  {
    "figure_id": "F530",
    "report_id": "R051",
    "label": "Exhibit 4",
    "context": "To be sure, a sizable share of US market capitalization is connected to the technology sector. Yet US firms lead across a range of sectors and are present in the upper echelons of all of them. $^{10}$ US market leadership is not a recent development: The Unite"
  },
  {
    "figure_id": "F531",
    "report_id": "R051",
    "label": "Exhibit 5",
    "context": "McKinsey & Company Fundamentally, US firms' outperformance is rooted in greater dynamism: They exhibit higher rates of labor reallocation, market entry and exit, and growth of young firms. $^{11}$ That dynamism translates to higher national productivity growth"
  },
  {
    "figure_id": "F532",
    "report_id": "R051",
    "label": "Exhibit 6",
    "context": "## The US lead in technology is narrowing as China becomes more competitive. ## Exhibit 6 ## Large US firms lead on investment, outpacing their European counterparts. Capital expenditure and R&D spending of large $^{1}$ US and European $^{2}$ companies, $^{3}$"
  },
  {
    "figure_id": "F533",
    "report_id": "R051",
    "label": "Exhibit 7",
    "context": "This gap in income levels has grown over the past 50 years. Although all income segments have seen real growth, market incomes (wages and asset flows) have grown the most for the top two quintiles. For the bottom 60 percent of the population, more income growt"
  },
  {
    "figure_id": "F534",
    "report_id": "R051",
    "label": "Exhibit 9",
    "context": "McKinsey & Company The United States remains the most competitive economy in the world on a multitude of fronts. Getting to this point has not been a straight path. There were twists and turns, transformations and reinventions. Before contemplating the future,"
  },
  {
    "figure_id": "F535",
    "report_id": "R051",
    "label": "Exhibit 9",
    "context": "# Looking back: Four chapters As we have seen, the United States has been the world's largest economy for more than a century. The rise of American competitiveness did not follow a linear or clear trajectory. Growth and innovation often happened in bursts, aft"
  },
  {
    "figure_id": "F536",
    "report_id": "R051",
    "label": "Exhibit 10",
    "context": "## 1. Agricultural abundance ## American Revolution to the Civil War In its first century-plus, the United States was a predominantly agrarian society. In the South, cotton boomed, making up most of the world market by 1820 and meeting strong demand from the b"
  },
  {
    "figure_id": "F537",
    "report_id": "R051",
    "label": "Exhibit 10",
    "context": "The United States had another natural advantage: navigable waterways. Coastal passages with barrier islands and inland rivers made long-distance shipping efficient. The Mississippi River system alone, made fully accessible by the Louisiana Purchase of 1803, in"
  },
  {
    "figure_id": "F538",
    "report_id": "R051",
    "label": "Exhibit 11",
    "context": "## The Apotheosis of Washington and American innovation circa 1865 The Apotheosis of Washington—a grand fresco depicting George Washington “rising to the heavens in glory” flanked by figures of Liberty and Victory—dominates the US Capitol rotunda ceiling. Comp"
  },
  {
    "figure_id": "F539",
    "report_id": "R051",
    "label": "Exhibit 11",
    "context": "Following the Civil War, the US-led Second Industrial Revolution gained full force, and America emerged as the world's preeminent industrial economy. Society grew more connected, shifting away from its agrarian and relatively isolated beginnings. Agricultural "
  },
  {
    "figure_id": "F540",
    "report_id": "R051",
    "label": "Exhibit 12",
    "context": "By 1832, the United States had more railroad miles than any European country, and by 1870, a larger population. The rapid expansion of railroads was fueled by capital expenditure, which at its height topped 4 percent of GDP annually. This played a critical rol"
  },
  {
    "figure_id": "F541",
    "report_id": "R051",
    "label": "Exhibit 13",
    "context": "Perhaps the single most visible token of US scientific leadership was its rise to dominance in Nobel Prizes. The country surpassed the United Kingdom and Germany in annual science-based prizes in the lead-up to World War II and took the lead on cumulative priz"
  },
  {
    "figure_id": "F542",
    "report_id": "R051",
    "label": "Exhibit 11",
    "context": "## Economic disruptions marked a transition The 1970s saw slowing productivity growth, energy crises, and double-digit rates of inflation. Just as the Great Depression provided a tectonic shift in favor of stronger government involvement, the 1970s economic tu"
  },
  {
    "figure_id": "F543",
    "report_id": "R051",
    "label": "Exhibit 14",
    "context": "Demand for a growing pool of US financial assets grew, attracting capital from a globalizing world. $^{96}$ In the years since 1990, foreign investment in US equities and debt has grown substantially, from the equivalent of 11 percent of GDP in each category t"
  },
  {
    "figure_id": "F544",
    "report_id": "R051",
    "label": "Exhibit 15",
    "context": "Productivity growth has been most concentrated in cities with some of the most flourishing knowledge ecosystems. These “superstar” cities have anchoring sectors and, often, universities. Their productivity has continued to push them ahead of the pack. The thre"
  },
  {
    "figure_id": "F545",
    "report_id": "R051",
    "label": "Exhibit 16",
    "context": "In 1767, Benjamin Franklin wrote: \"America, an immense Territory, favour'd by Nature with all Advantages of Climate, Soil, great navigable Rivers and Lakes, &c. must become a great Country, populous and mighty.\" $^{107}$ He was prescient. Over time, the countr"
  },
  {
    "figure_id": "F546",
    "report_id": "R051",
    "label": "Exhibit 17",
    "context": "Reliable and affordable energy has been an enduring"
  },
  {
    "figure_id": "F547",
    "report_id": "R051",
    "label": "Exhibit 19",
    "context": "The entrepreneurial spirit of the United States was not limited to tech visionaries. It was also embedded in the American people and business community, who have long had the appetite (and means) to adopt and scale new technologies, including those invented el"
  },
  {
    "figure_id": "F548",
    "report_id": "R051",
    "label": "Exhibit 20",
    "context": "## Exhibit 20 Demand for AI fluency and technical AI skills rose between 2023 and 2025. Employees in jobs demanding AI-related skills AI fluency skills, calling for people to use or manage AI Technical AI skills, calling for people to develop or govern AI STEM"
  },
  {
    "figure_id": "F549",
    "report_id": "R051",
    "label": "Exhibit 21",
    "context": "Worker shortages across a range of high- and low-skill occupations are already a concern. Many of the sectors experiencing recent shortages have historically been harder to automate and have seen stubbornly low rates of productivity growth. Healthcare, for exa"
  },
  {
    "figure_id": "F550",
    "report_id": "R051",
    "label": "Exhibit 22",
    "context": "## About half of outstanding Treasuries are set to roll over this year and next. Will demand match supply? ## Exhibit 22 ## US fiscal deficits, including net interest payments, are historically elevated. US federal deficits and defense spending, FY 1975–2035E,"
  },
  {
    "figure_id": "F551",
    "report_id": "R051",
    "label": "Exhibit 23",
    "context": "In the coming era, when technologies such as AI become integral to work and society, power demand is likely to surge further. Growing geopolitical competition also means a likely push to build more domestic manufacturing for critical products like semiconducto"
  },
  {
    "figure_id": "F552",
    "report_id": "R051",
    "label": "Exhibit 24",
    "context": "Geopolitics deepens the conundrum. A total of \\$160 billion of US imports are critical, concentrated, and come from geopolitically distant trading partners (see sidebar “Defining geopolitical distance”). This bull’s-eye of potential exposure may seem small, bu"
  },
  {
    "figure_id": "F553",
    "report_id": "R051",
    "label": "Exhibit 25",
    "context": "By this measure, Europe, Japan, South Korea, and the United States sit near one end of a spectrum, while China and Russia sit closer to the other end (Exhibit 25). Most emerging markets sit somewhere in the middle. Of course, relations between countries are dy"
  },
  {
    "figure_id": "F554",
    "report_id": "R053",
    "label": "Exhibit 1",
    "context": "## Wind farm maintenance crew Energy and sustainability Wind farms need to maintain peak efficiency year-round, maximizing clean-energy output while minimizing downtime and operational costs Immersive reality Technicians use augmented reality goggles that prov"
  },
  {
    "figure_id": "F555",
    "report_id": "R053",
    "label": "Exhibit 1",
    "context": "Immersive reality Technicians use augmented reality goggles that provide visual guidance to help them maintain and repair complex turbine systems safely Advanced connectivity Low-Earth-orbit satellites provide technicians with access to real-time data and clou"
  },
  {
    "figure_id": "F556",
    "report_id": "R053",
    "label": "Exhibit 2",
    "context": "McKinsey & Company Note: Data includes private-market and public-market capital raises across venture capital and corporate and strategic M&A (including joint ventures), private equity investments (including buyouts and private investment in public equity), an"
  },
  {
    "figure_id": "F557",
    "report_id": "R053",
    "label": "Exhibit 2",
    "context": "This report lays out considerations for all 13 technology trends. For easier consideration of related trends, we grouped them into three broader categories: the AI revolution, compute and connectivity frontiers, and cutting-edge engineering. Of course, there's"
  },
  {
    "figure_id": "F558",
    "report_id": "R054",
    "label": "Exhibit 1",
    "context": "These findings raise questions about how organizations can build a “test, learn, and adapt” mindset and a culture of continuous improvement, and about how leaders redefine roles and responsibilities in a world in which machines can think, orchestrate, decide, "
  },
  {
    "figure_id": "F559",
    "report_id": "R054",
    "label": "Exhibit 2",
    "context": "One way to tackle such concerns is to build a responsive risk framework that proactively addresses both technical and ethical challenges. Winning employees' buy-in is another path to accelerating adoption at scale. This can be done by identifying high-impact A"
  },
  {
    "figure_id": "F560",
    "report_id": "R054",
    "label": "Exhibit 3",
    "context": "## Exhibit 3 A majority of survey respondents agreed that AI capabilities will bring exponential productivity gains. Organizations' desired outcomes of developing an Al-savvy workforce, % of respondents (n = 7,904) Faster and widespread access to information"
  },
  {
    "figure_id": "F561",
    "report_id": "R054",
    "label": "Exhibit 3",
    "context": "Faster and widespread access to information Note: Respondents were asked to identify their desired outcomes in developing an Al-savvy workforce. ## Benefits of getting it right Leaders see multiple and significant benefits from successfully developing an AI-sa"
  },
  {
    "figure_id": "F562",
    "report_id": "R054",
    "label": "Exhibit 3",
    "context": "Faster and widespread access to information Note: Respondents were asked to identify their desired outcomes in developing an Al-savvy workforce. ## Benefits of getting it right Leaders see multiple and significant benefits from successfully developing an AI-sa"
  },
  {
    "figure_id": "F563",
    "report_id": "R054",
    "label": "Exhibit 6",
    "context": "Finally, regulatory and geopolitical complexities can impede progress. As AI-native GBS drives cross-border data flows, companies need to navigate data privacy, local AI regulations, and geopolitical risk. These factors now shape GBS footprint strategy, determ"
  },
  {
    "figure_id": "F564",
    "report_id": "R054",
    "label": "Exhibit 8",
    "context": "This obstacle is more pronounced in North America (32 percent) and Europe (29 percent) than in the Asia-Pacific region (23 percent). Cultural resistance hits hardest where energy runs low: 45 percent of employees in fatigued organizations see it as a barrier, "
  },
  {
    "figure_id": "F565",
    "report_id": "R054",
    "label": "Exhibit 9",
    "context": "When it comes to workflow redesign, our surveys suggest that resource allocation is often neglected. While a lack of resources and insufficient investment in change are sometimes cited as obstacles to process optimization, the respondents to our survey downpla"
  },
  {
    "figure_id": "F566",
    "report_id": "R054",
    "label": "Exhibit 10",
    "context": "Longer-term impact can be achieved by prioritizing workflows with the highest strategic impact. For example, for product development, this can entail better product–market fit, faster launch cycles, and an optimized innovation pipeline. For integrated planning"
  },
  {
    "figure_id": "F567",
    "report_id": "R054",
    "label": "Exhibit 11",
    "context": "Effective portfolio management requires frequent divestitures of underperforming businesses. Organizations can free up capacity to take bold bets by shedding areas where they are no longer the best owner or letting go of activities that are no longer core to s"
  },
  {
    "figure_id": "F568",
    "report_id": "R054",
    "label": "Exhibit 11",
    "context": "Exhibit 11 The majority of survey respondents, particularly executives, said they are clear about their organization's must-win battles. Organizations' visibility on must-win battles, % of respondents (n = 10,018) McKinsey & Company Organizations that make por"
  },
  {
    "figure_id": "F569",
    "report_id": "R054",
    "label": "Exhibit 12",
    "context": "The priorities can be new geographic markets, products and services, innovation, customer engagement, or price positioning. Leaders then need to ensure that resources are reallocated decisively and identify low-impact and noncore activities for divestment to f"
  },
  {
    "figure_id": "F570",
    "report_id": "R054",
    "label": "Exhibit 13",
    "context": "Build a culture that puts equal weight on employee performance and well-being The goal here is to ensure employees feel energized rather than contained. High performers who sustain their performance over time are driven by purpose, adaptability, and recovery r"
  },
  {
    "figure_id": "F571",
    "report_id": "R054",
    "label": "Exhibit 14",
    "context": "There are stakeholder benefits, too, including for customers and investors. One in four organizations (24 percent) report that prioritizing D&I initiatives leads to broader customer and market appeal, while 31 percent say these initiatives enhance corporate re"
  },
  {
    "figure_id": "F572",
    "report_id": "R054",
    "label": "Exhibit 15",
    "context": "Specifically, reflective leaders are more attuned to external forces and feel stronger performance pressure. More than one in five (22 percent) say that geopolitical shifts are significantly affecting their organizations, compared with 10 percent of leaders wh"
  },
  {
    "figure_id": "F573",
    "report_id": "R055",
    "label": "Exhibit 1",
    "context": "The survey findings also shed light on how organizations are structuring their AI deployment efforts. Some essential elements for deploying AI tend to be fully or partially centralized (Exhibit 1). For risk and compliance, as well as data governance, organizat"
  },
  {
    "figure_id": "F574",
    "report_id": "R055",
    "label": "Exhibit 2",
    "context": "Organizations have employees overseeing the quality of gen AI outputs, though the extent of that oversight varies widely. Twenty-seven percent of respondents whose organizations use gen AI say that employees review all content created by gen AI before it is us"
  },
  {
    "figure_id": "F575",
    "report_id": "R055",
    "label": "Exhibit 3",
    "context": "## Exhibit 3 Respondents report increasing mitigation of inaccuracy, intellectual property infringement, and privacy risks related to use of gen AI. Gen-AI-related risks that organizations are working to mitigate, $^{1}$ % of respondents Intellectual property "
  },
  {
    "figure_id": "F576",
    "report_id": "R055",
    "label": "Exhibit 5",
    "context": "Respondents continue to see these roles as largely challenging to fill, though a smaller share of respondents than in the past two years describe hiring for many roles as “difficult” or “very difficult” (Exhibit 5). One exception is AI data scientists, who wil"
  },
  {
    "figure_id": "F577",
    "report_id": "R055",
    "label": "Exhibit 6",
    "context": "Many respondents also say that their organizations have reskilled portions of their workforces as part of their AI deployment over the past year and that they expect to undertake more reskilling in the years ahead (Exhibit 6). Our latest survey also shows how "
  },
  {
    "figure_id": "F578",
    "report_id": "R055",
    "label": "Exhibit 7",
    "context": "Looking at the expected effects of gen AI deployment by business function, respondents most often predict decreasing head count in service operations, such as customer care and field services, as well as in supply chain and inventory management (Exhibit 7). In"
  },
  {
    "figure_id": "F579",
    "report_id": "R055",
    "label": "Exhibit 9",
    "context": "Organizations are also using AI in more business functions than in the previous State of AI survey. For the first time, most survey respondents report the use of AI in more than one business function (Exhibit 9). Responses show organizations using AI in an ave"
  },
  {
    "figure_id": "F580",
    "report_id": "R055",
    "label": "Exhibit 10",
    "context": "While organizations in all sectors are most likely to use gen AI in marketing and sales, deployment within other functions varies greatly according to industry (Exhibit 10). Organizations are applying the technology where it can generate the most value—for exa"
  },
  {
    "figure_id": "F581",
    "report_id": "R055",
    "label": "Exhibit 11",
    "context": "Note: Figures may not sum to 100%, because of rounding. # More than one-third of respondents say their organizations use gen AI to create images, and more than one-quarter use it to create computer code. Most respondents reporting use of gen AI—63 percent—say "
  },
  {
    "figure_id": "F582",
    "report_id": "R055",
    "label": "Exhibit 11",
    "context": "Note: Figures may not sum to 100%, because of rounding. # More than one-third of respondents say their organizations use gen AI to create images, and more than one-quarter use it to create computer code. Most respondents reporting use of gen AI—63 percent—say "
  },
  {
    "figure_id": "F583",
    "report_id": "R055",
    "label": "Exhibit 11",
    "context": "Most respondents reporting use of gen AI—63 percent—say that their organizations are using gen AI to create text outputs, but organizations are also experimenting with other modalities. More than one-third of respondents say their organizations are generating "
  },
  {
    "figure_id": "F584",
    "report_id": "R055",
    "label": "Exhibit 12",
    "context": "An increasing share of respondents report value creation within the business units using gen AI. Compared with early 2024, larger shares of respondents say that their organizations' gen AI use cases have increased revenue within the business units deploying th"
  },
  {
    "figure_id": "F585",
    "report_id": "R055",
    "label": "Exhibit 12",
    "context": "Exhibit 12 Organizations increasingly see gen AI's effects on revenues in the business units using the technology. Revenue increase within business units from gen AI use, past 12 months, by function, $^{1}$ % of respondents $^{1}$ Questions were asked only of "
  },
  {
    "figure_id": "F586",
    "report_id": "R055",
    "label": "Exhibit 13",
    "context": "McKinsey & Company Overall, respondents are also more likely than in the previous survey to say they are seeing meaningful cost reductions within the business units using gen AI (Exhibit 13). In early 2024, among respondents reporting use of gen AI in specific"
  },
  {
    "figure_id": "F587",
    "report_id": "R055",
    "label": "Exhibit 13",
    "context": "Overall, respondents are also more likely than in the previous survey to say they are seeing meaningful cost reductions within the business units using gen AI (Exhibit 13). In early 2024, among respondents reporting use of gen AI in specific business functions"
  }
]