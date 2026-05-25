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
    "title": "中国真正的叙事切换：不是增长，是资产定价的锚在变",
    "digest": "[wechat_article.md]\n# 中国真正的叙事切换：不是增长，是资产定价的锚在变\n\n过去几个月，围绕中国资产的讨论高度撕裂。看多者看到AI突破、外交回暖、出口强劲；看空者盯着地产收缩、消费疲软、通缩惯性。两派观点似乎都能自洽，但谁也说服不了谁。这不是噪声，而是市场正在经历一次定价锚的切换。\n\n某外资投行近期组织了一场横跨北京和上海的投资者调研，与政策制定者、学者、市场参与者、智库、商会以及科技行业从业者进行了密集交流。其核心结论值得每一位关注中国资产配置的人认真对待：**中国的地缘政治环境正在比国内经济更快地趋于稳定。** 这句话的潜台词是，此前压制中国资产估值的一个核心变量——地缘风险溢价——正在被快速压缩，而驱动资产价格的底层逻辑，正在从“增长斜率”转向“结构稳定性”。\n\n这篇研报解析将提炼这一判断的五个关键层次，并在最后提出一个报告尚未完全回答的问题，供读者进一步思考。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 外交回暖正在成为一个被低估的定价因子\n\n市场习惯于将中美关系视为一个“要么交易、要么对抗”的二元变量。但本次调研传递出的信号更为微妙：外交层面的“稳定”正在获得独立于经贸谈判的价值。\n\n报告指出，近期的高层会晤实现了其预期的目标——它不是一个交易性的协议，而是一次关键的基调设定。更重要的是，2026年还有三场高级别会议（APEC、G20以及可能的华盛顿访问）已经排上日程。这意味着，对话的连续性本身就在创造一种可预见性。报告特别提到，国会层面的重新接触正在恢复，这是一个“被低估的积极因素”。\n\n对于资产定价而言，这意味着什么？地缘政治风险的边际下降，会直接降低海外资金对中国资产的“不确定性折价”。过去几年，许多全球投资者因为无法评估中美关系的尾部风险，选择系统性低配中国。如果外交框架从“对抗-谈判”切换为“竞争-对话”，那么\n\n[... middle omitted ...]\n\n论，我们可以一起拆解这些尚未被市场充分定价的结构性变量。**\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国经济的AB面：一边AI出口翻倍，一边消费难抬头\n\n中国经济的“K型”分化\n\n最近读了一份外资投行的中国调研笔记，走访了北京和上海，和决策层、学者、企业聊了一圈。最大的感受是：中国的地缘环境比国内经济稳得更快。\n\n1. 中美关系在回暖，但关税风险还在\n   - 最近的元首峰会定下了“稳定基调”的基调，不是交易性协议。\n   - 今年还有APEC、G20等高层会面，对话会继续。\n   - 关键风险：7月24日301关税到期，美方倾向延期，可能让有效关税再上升。\n\n2. 经济是“K型”复苏——新经济扛着旧经济\n   - 新经济（可贸易品、AI设备、新能源）增速强劲，AI相关设备出口同比接近翻倍。\n   - 旧经济（消费、地产、服务业）仍然疲弱，4月数据继续分化。\n   - 好消息是新经济的增长目前能抵消旧经济的拖累，暂时不会出现急剧放缓。\n\n3. 消费不振的核心：信心和收入\n   - 老百姓不是没钱——2021年以来居民存款积累约50-60万亿，但不敢花。\n   - 原因：失业担忧、工资增长弱、地产财富缩水。\n   - 关键：消费反弹需要名义工资增长，但结构性障碍很深。\n   - AI还在“补刀”——服务业岗位\n\n[... middle omitted ...]\n\nd. Consumption remains structurally impaired, the property sector is in a permanent retreat, and the labour market is weak. Consequently, the bull and bear cases for China are both clearly vis\n\n[... middle omitted ...]\n\nk, NY 10019</td><td>Tower,</td><td></td></tr><tr><td>Tel: (44) 20 7545 8000</td><td>Tel: (1) 212 250 2500</td><td>Singapore 048583</td><td></td></tr><tr><td></td><td></td><td>Tel: +65 6423 8001</td><td></td></tr></table>"
  },
  {
    "id": "R002",
    "title": "市场真正低估的不是需求，而是供给侧的再定价",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是需求，而是供给侧的再定价\n\n2026年5月，某外资投行在年度全球汽车、出行与机器人大会上与数十家欧美汽车零部件企业的一对一交流，释放了一个值得产业决策者认真对待的信号。\n\n这份报告的核心判断不是“汽车销量还能撑多久”，而是：**全球汽车供应链正在经历一轮被市场低估的供给侧再定价**。这种再定价由三个力量同时驱动——地缘冲突带来的隐性成本上升、非汽车业务对传统产能的争夺、以及中国产能外溢对全球定价体系的重构。而大多数投资者和产业规划者，仍然只盯着终端需求曲线。\n\n报告明确指出，欧美汽车市场在短期内“出人意料地坚挺”，中国本土市场偏软但出口强劲。然而，真正决定未来两年利润分配格局的，不是销量本身，而是供给端正在发生的结构性变化。这些变化不会出现在IHS的产量预测里，却会在2027年之后逐步显现在每一家公司的利润表中。\n\n以下是这份报告中最值得关注的五个结构性判断。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 地缘冲突的影响正在从“可对冲”转向“不可对冲”，2027年是真正的分水岭\n\n报告中最容易被忽略但最重要的一个信号是：地缘冲突对汽车供应链的成本冲击，在2026年看起来“可控”，但正在向2027年累积。\n\n当前多数零部件企业通过套期保值和成本转嫁机制，将能源和原材料的涨价压力控制在可承受范围内。但报告明确指出，随着套期保值头寸逐步到期，2027年的成本暴露将显著上升。物流和海运成本已经开始上涨，部分企业反映低层级供应商的涨价压力正在向一级供应商传导，而一级供应商向OEM的转嫁通常有3到6个月的时滞。\n\n这意味着，2026年的利润表可能并未真实反映地缘冲突的成本冲击。如果冲突持续，2027年的利润率压力将远大于当前市场的预期。报告中的公司交流也印证了这一点：多家企业表示，2026年的成本冲击已\n\n[... middle omitted ...]\n\n承受成本压力？这些问题的答案，可能就藏在这份报告的字里行间。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球车市暗流涌动，一份关键研报拆解\n\n车市，正站在拐点\n\n---\n\n最近看了一份某外资投行的全球车市研报，信息量很大，分享几个核心洞察。🧐\n\n**1/ 销量比想象中“扛揍”，但能撑多久？**\n\n欧洲和北美市场目前意外地有韧性，订单流也不错。但矛盾点在于：IHS（一家数据机构）在5月的最新预测里，因为考虑到高油价可能持续，直接下调了未来几年的产量预期——2026年砍了50万辆，2027年砍了120万辆，2028年砍了80万辆。\n\n这就很微妙了。一边是车企和供应商说“还行”，另一边是第三方机构开始计入更差的情景。谁的视角更准？研报认为，近端能见度大概只有10-12周，所以第二季度大概率是稳的，真正的风险可能要等到下半年甚至2027年。🤔\n\n**2/ 定价权：消费者能消化多少？**\n\n在美国，想通过涨价完全覆盖关税成本，基本不可能。欧洲也很难。中国这边，价格战似乎有企稳迹象。\n\n所以车企在干嘛？它们不直接涨价，而是通过“车型换代”和“优化产品组合”来自然拉高平均售价（ASP）。同时，库存和优惠都在精细化管理。利润的增量，反而越来越靠软件和服务贡献了。思路很清晰。\n\n**3/ 中东冲突：成本冲击正在显现**\n\n虽然大\n\n[... middle omitted ...]\n\n thus far by existing hedging and passthrough strategies on oil and raw materials, suppliers recognize that prolonged geopolitical friction has the potential to impact volume and profit. Separ\n\n[... middle omitted ...]\n\nk, NY 10019</td><td>Tower,</td><td></td></tr><tr><td>Tel: (44) 20 7545 8000</td><td>Tel: (1) 212 250 2500</td><td>Singapore 048583</td><td></td></tr><tr><td></td><td></td><td>Tel: +65 6423 8001</td><td></td></tr></table>"
  },
  {
    "id": "R003",
    "title": "人民币国际化真正的瓶颈不在贸易结算，而在资产端的深度",
    "digest": "[wechat_article.md]\n# 人民币国际化真正的瓶颈不在贸易结算，而在资产端的深度\n\n人民币国际化的话题每隔几年就会重新升温。这一次的催化剂看起来颇为密集：政策表述进一步明确，CIPS日均交易量在3月创下历史新高，“石油人民币”的讨论在地缘冲突背景下重新浮现，离岸人民币债券发行在2026年前四个月几乎翻倍。人民币对美元年内已升值约3%，足以覆盖中美利差所隐含的持有成本。\n\n但这些信号叠加在一起，是否意味着人民币国际化已经进入一个新阶段？某外资投行最新发布的研报给出了一个值得认真对待的判断：进步确实存在，但高度不均衡，而且几乎全部集中在与中国相关的贸易结算领域。真正决定下一阶段走向的，不是结算通道还能扩多大，而是境外参与者能否方便地获得人民币流动性、有效地对冲风险、以及找到足够多有吸引力的资产。\n\n这个判断的底层逻辑是清晰的。人民币跨境交易的结构已经发生了根本性变化——资本和金融账户交易占比已达75%，债券投资是最大的单一用途，占比46%。这意味着，推动人民币国际化的主要动力已经从贸易结算转向了投资驱动。而投资驱动的逻辑与贸易结算完全不同：它要求的是一个能够自我循环的生态系统，而不是一条单向的结算管道。\n\n以下是我们从这份研报中提炼出的几个关键层次。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 人民币的跨境使用已经跨越了“贸易结算”阶段，但资产端的配套远远落后于交易量的增长\n\n从总量看，人民币跨境交易从2017年的9万亿元跃升至2024年的64万亿元，这个数字本身是惊人的。但更值得关注的是结构：货物贸易在跨境人民币交易中的占比已降至19%，而债券投资占比高达46%，直接投资的13%和合格境外投资者(QFI)的7%紧随其后。\n\n这一结构变化意味着，境外参与者持有和使用人民币的原因正在发生根本性转变。过去，企业用人民币结算是为了降低汇率风险和\n\n[... middle omitted ...]\n\n围绕这份报告未完全展开的几个关键问题，做更深入的拆解和推演。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n人民币国际化，不止于贸易结算\n\n投研笔记\n\n人民币如何从贸易结算走向全球\n\n---\n\n人民币国际化的故事，正在从“贸易结算”切换到“投资驱动”的新阶段。\n\n某外资投行最新研报指出，人民币在三大国际货币职能（计价、支付、储值）上的进展并不均衡，目前最亮眼的部分集中在与中国的贸易结算领域。但真正让人民币“出圈”的下一步，需要更多基础设施支撑。\n\n**1/ 进展在哪？中国贸易结算领跑**\n\n- 2025年，中国货物贸易中用人民币结算的比例已从2019年的13%上升到30%\n- 但在全球范围内，人民币在进口计价中的份额仅约1.5%（2023年），全球支付份额约3-4%，官方储备份额约2%，国际债券份额仅0.9%\n- 对比中国占全球GDP约19%、贸易约12%的体量，人民币国际化空间依然很大\n\n**2/ 关键转折：跨境使用转向投资驱动**\n\n- 2024年，中国跨境人民币交易总额达64万亿元，是2017年的7倍\n- 资本和金融账户交易已占75%，其中债券投资占跨境人民币支付的46%，而货物贸易仅占19%\n- 这意味着，下一阶段的核心不再是“怎么结算”，而是：外资能否方便地获取人民币流动性、有效对冲风险、找到有吸引力的资\n\n[... middle omitted ...]\n\nmple countries has roughly doubled since 2020 but remained only around $1.5\\%$ in 2023; the RMB's share in global payments was around $3 - 4\\%$ over the past two years; and the RMB accounted f\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R004",
    "title": "市场真正低估的不是需求，而是供给侧的再定价",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是需求，而是供给侧的再定价\n\n过去几周，30年期美债收益率突破5%，全球利率波动重新成为市场焦点。但如果你只把注意力放在利率上，可能错过了这份研报中最值得关注的信号：市场正在经历一次供给侧的结构性再定价，而这轮再定价的驱动力，远比需求端的波动更持久、更深刻。\n\n某外资投行本周发布的跨资产研究汇总，表面上是每周例行的工作梳理，但仔细拆解后会发现，它揭示了一个正在加速形成的核心判断——**全球资产定价的锚点正在从需求侧转向供给侧，而这将重塑从AI投资到能源资本开支、从利率传导到行业竞争格局的几乎所有关键变量。**\n\n这不是一个短期交易机会，而是一个可能持续数年的结构性变化。以下是我们从这份研报中提炼出的五个关键洞察，以及它们对投资决策的含义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 利率波动暴露了旧框架的失效，防御股不再防御是第一个信号\n\n研报明确指出，股票与债券收益率的相关性已经转为负值——当美债收益率上升时，股市反而创出新高。这在历史上并不常见。更值得警惕的是，传统的防御性板块已经不再具备防御属性。\n\n这意味着什么？过去几十年形成的“利率上升买防御、利率下降买成长”的简单框架正在失效。彼得·奥本海默在报告中提到，他多年来第一次看到成长板块中出现了价值洼地，而价值板块中也出现了成长机会。这是一个对选股者极为有趣、但也极为复杂的背景。\n\n这里的核心含义是：**利率本身不再是单一的风险因子，它正在通过供给侧渠道（而非传统的需求渠道）重新传导到资产价格中。** 如果你还在用旧框架判断利率对组合的影响，可能已经落后于市场。\n\n## 2. AI投资的真正瓶颈不是技术，而是欧洲的电网和数据中心供给\n\n研报透露了一个重要信号：本周举行的欧洲公用事业和清洁能源会议、以及EMEA基础设施会议上，数据中心和A\n\n[... middle omitted ...]\n\n报中更多未被充分讨论的图表和数据，以及它们对具体标的的含义。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n利率波动加剧，AI投资与纪律如何平衡？\n\n利率冲击波下的投资逻辑\n\n最近市场被利率波动刷屏了。30年期美债收益率突破5%，全球利率同步上行，股债相关性从正转负。这意味着什么？如果下半年石油供应问题持续，市场可能会面临一个急刹车。\n\n不过别慌，某外资投行策略师认为，这反而是主动选股的好时机——多年来第一次，成长股里出现了价值洼地，价值股里也冒出了成长机会。传统的防御板块不再管用，很大一部分原因是AI及其相关投资的崛起。\n\n1/ AI投资：欧洲的“刚需”与争议\n欧洲数据中心建设是硬需求。近期两场会议都聚焦于此：欧洲公用事业会议和EMEA基础设施会议。核心瓶颈是电力和电网，这利好电气化相关标的，比如Enel、Naturgy，以及提供表后解决方案的西门子能源。\n\n但AI到底怎么用，争议很大。某投行分析师直言：目前大多数企业用AI是亏钱的，这种模式不可持续。Token增长的速度、使用是否盲目，都是关键观察点。\n\n2/ 石油资本开支：勘探周期启动\n石油巨头财报电话会上，“地震勘探、发现、区块”等关键词已经开始明显增加。最先受益的是地震勘探服务商TGS。行业整合后，活跃船舶从2013年的约60艘降至目前的17-30艘，且2\n\n[... middle omitted ...]\n\ns sees emerging pockets of value in the growth space and emerging pockets of growth in the value parts of the market, which is an interesting backdrop for stock-pickers. Many tried and tested \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R005",
    "title": "市场真正低估的不是地缘风险，而是欧洲通胀的二次定价",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是地缘风险，而是欧洲通胀的二次定价\n\n过去两个月，中东局势的升级让全球投资者的目光再次聚焦欧洲。然而，市场上大多数讨论仍停留在“冲突会持续多久”或“能源价格还会涨多少”这类短期博弈层面。一份来自某外资投行的最新研报，通过其高频追踪模型和金融条件指数，提供了一个截然不同的判断框架：\n\n**当前冲击对欧洲经济的真正威胁，并非2022年乌克兰危机式的增长断崖，而是一次更持久、更难消退的供给侧通胀重定价。**\n\n这份报告的核心结论是：欧洲天然气市场的反应比2022年温和得多，但石油和成品油价格的预期路径却显示出更强的粘性。与此同时，消费者信心和企业调查的跌幅仅为2022年的一半左右，但价格预期相关指标却出现了显著攀升。这意味着，欧洲央行面临的“增长 vs 通胀”权衡，正在从“先救增长”转向“被迫接受更高通胀更久”。\n\n以下是我们基于该报告数据与逻辑的深度解读，共五个层次。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 天然气冲击已大幅缓和，但石油端的溢价正在从“脉冲”变为“平台”\n\n2022年3月，欧洲TTF天然气期货在冲突爆发当天飙升至约230欧元/兆瓦时，远期曲线极度陡峭。而本轮冲突中，TTF现货价格在105欧元附近触顶，远期合约价格在95欧元左右，两者均显著低于2022年峰值。更关键的是，该投行的基线预测显示，TTF将在未来12个月内逐步回落至85欧元附近，与远期曲线基本吻合。\n\n这意味着，市场并不认为本轮冲突会造成类似2022年的天然气供应危机。欧洲的储气设施、LNG进口能力和需求侧管理机制，已经为“中度紧张”情景做好了准备。\n\n但石油端的信号恰恰相反。报告中的Exhibit 2显示，汽油和柴油的现货价格自冲突以来持续攀升，且远期曲线并未像天然气那样快速下行。柴油价格在2026年5月的远期合约\n\n[... middle omitted ...]\n\n欧洲的绿色转型是否会加速？欢迎加入，一起跟踪这些数据的演变。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中东局势冲击欧洲经济，这次和2022年有什么不同？\n\n欧洲经济，这次冲击不一样\n\n最近中东局势持续发酵，某外资投行出了一份欧洲经济影响追踪报告。我仔细拆解了一下，发现这次的情况和2022年俄乌冲突时有几个关键差异。\n\n**1/ 能源冲击更温和，但更持久**\n\n和2022年天然气价格飙到230欧元/兆瓦时不同，这次TTF天然气期货价格只到了105左右。市场定价显示，能源冲击的烈度明显下降。\n\n但有意思的是，远期曲线比2022年更陡——市场预期未来5年天然气价格都会维持在较高水平，而不是像2022年那样快速回落。这说明市场认为这次的结构性影响更深远。\n\n**2/ 通胀预期在悄悄爬升**\n\n报告跟踪的欧洲央行消费者调查显示，1年期通胀预期已经上升到4.0%。EC调查的售价预期指标也在4月份大幅走强——制造业+1.5个标准差，零售+1.3个标准差。\n\n某外资投行已经把欧元区2026年底通胀预测上调了约2个百分点，英国上调了1.7个百分点。这个幅度不小。\n\n**3/ 经济增长预期被持续下调**\n\n从1月到5月，欧元区2026年GDP增速预测从1.4%一路砍到0.5%。同期Bloomberg共识也从1.4%降到0.8%。\n\n[... middle omitted ...]\n\nent Shock is Seen as More Contained for European Natural Gas Than in 2022; Oil Shock Expected to Be More Persistent   \n![](images/a68ff4abd6fbddceeea17dd90a4f50bb26c5feeed120750717990b428b8560\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R006",
    "title": "美债长端的“稳定”是喘息，不是反转",
    "digest": "[wechat_article.md]\n# 美债长端的“稳定”是喘息，不是反转\n\n全球利率市场在过去一周经历了从剧烈抛售到暂时企稳的切换。长端美债收益率在突破关键区间后，因能源价格回落以及来自英国和日本市场的正面消息而获得喘息。然而，这份来自某外资投行的最新研报传递的核心判断是：**市场当前的平静更多是技术性修复和外部噪音的暂时消退，而非基本面矛盾的解决。** 长端美债估值仅略低于公允水平，并未进入“便宜到足以吸引大规模抄底”的区间。对于资产配置者和利率交易者而言，真正的挑战在于识别哪些市场的“稳定”具备可持续性，哪些只是暴风雨前的宁静。\n\n报告的核心价值不在于罗列各国利率的短期走势，而在于它提供了一个区分“结构性支撑”与“周期性波动”的分析框架。欧洲利率的持续跑赢、英国国债的估值吸引力、以及日本长端利率对政策路径的依赖，这三个逻辑链条构成了当前全球利率市场最具操作性的三条主线。与此同时，报告也坦诚地指出了那些尚未被定价的风险——尤其是美国利率市场的“凸性幽灵”和澳大利亚的加息风险。本文基于该研报解析，提炼出对产业决策者和高净值投资者最有价值的五个洞察，并保留报告中最值得深入阅读的未尽问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 美债的“稳定”缺乏宏观催化剂，估值尚未到“便宜就买”的临界点\n\n研报明确指出，上周美债长端收益率的回落，主要驱动力并非美国自身基本面改善，而是外部因素的暂时缓和。能源价格下跌、英国和日本国内政治噪音的平息，这些“进口的利好”并不能替代美国本土的通胀和就业数据走弱。报告用估值模型给出了一个关键判断：当前长端远期利率（如5y5y）仅略高于模型公允值，并未出现显著偏离。这意味着，如果缺乏新的宏观催化剂（如能源供应真正恢复、或劳动力市场超预期降温），仅凭当前估值水平难以支撑一轮更深的反弹。\n\n对于投资者而言，这里的“所以呢”是\n\n[... middle omitted ...]\n\n这里，我们不仅解读报告说了什么，更关注它“还没说透”的地方。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美债波动暂歇，但真正的反转还没来\n\n美债暂稳，反转还早\n\n能源回落+英日利好，长端美债压力暂缓\n\n最近长端美债的波动稍微喘了口气。能源价格回落，加上英国和日本那边传来一些偏正面的消息，让利率从高位回落了一点。但别急着觉得反转来了——基础问题还在。\n\n1️⃣ 美债：估值还不够“便宜”\n- 虽然收益率从近期高点（30年期是周期高点）下来了，但依然处于区间上沿，缺少持续下行的催化剂。\n- 长期远期利率只比宏观框架的合理估值高一点点，不算特别便宜。\n- 能源恢复、通胀/就业数据偏鸽、或者收益率高到冲击风险资产，才是真正让利率下行的三条路。目前看，哪条都不太成熟。\n\n2️⃣ 凸性风险：波动被放大了\n- 美债10年和30年分别突破4.5%和5.0%，引发了波动率上升的讨论。\n- 但隐含波动率的反应其实比收益率跳动的幅度要温和。\n- 抵押贷款机构的对冲行为不透明，但估计此轮抛售带来的久期延长，相当于约400亿美元10年期国债等价物。不过由于它们对利率风险容忍度提高，实际对冲了多少不好说。\n- 往后看，抛售带来的延伸风险会减弱，反弹反而会修复累积的久期缺口。\n\n3️⃣ 欧洲：利率多头性价比更高\n- 欧洲央行走在前面，5y5y\n\n[... middle omitted ...]\n\nn credit may have less room to tighten but still offers reasonable carry that should be insulated from front-end rates volatility. There is a growing valuation case for long Gilts, assisted by\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R007",
    "title": "美元正在被重新定价，但市场可能低估了“能源溢价”的持久性",
    "digest": "[wechat_article.md]\n# 美元正在被重新定价，但市场可能低估了“能源溢价”的持久性\n\n过去一个月，全球外汇市场出现了一个值得产业决策者和资产配置者认真对待的信号：美元重新走强，而这一轮走强的驱动力并非来自美国自身数据的超预期，而是来自一个更结构性的变量——能源流动受限对全球贸易条件的重塑。\n\n某外资投行在最新一期全球外汇策略报告中提出一个核心判断：只要能源流动仍受限制，美元就面临持续且不断扩大的升值压力。这句话的分量，在于它挑战了过去两年市场习惯的叙事——即美国经济“不再例外”意味着美元将趋势性走弱。\n\n报告通过一系列交叉验证的数据和模型，揭示了一个正在发生的结构性转变。理解这个转变，比预测下周的利率决议更重要。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 贸易条件冲击正在取代利率差异，成为外汇定价的主导力量\n\n报告开篇就点出了一个被许多投资者忽视的现象：过去几个月，外汇市场的回报更多由“贸易条件”的变动驱动，而非传统的利差逻辑。所谓贸易条件，简单说就是一个国家出口价格相对于进口价格的变化。当能源出口国因价格上涨而获益、能源进口国因成本上升而承压时，汇率就会做出相应调整。\n\n某外资投行指出，这些贸易条件的变化已经开始在实体经济数据中显现——中国4月经济活动数据大幅低于预期，欧洲5月PMI初值放缓，而美国在AI热潮和能源价格高企的双重作用下，再次展现出相对优势。报告中的Exhibit 1清晰展示了这一趋势：美国经济表现相对于全球其他地区的差距正在重新拉大。\n\n这意味着什么？意味着投资者不能再简单用“美国利率见顶”来推断美元走弱。当贸易条件冲击成为主导变量时，美元的定价逻辑已经改变。那些仍然基于利差交易框架做外汇配置的投资者，可能正在错过这轮结构性变化。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n#\n\n[... middle omitted ...]\n\n里，我们可以更充分地展开那些在公开文章中只能点到为止的讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美元重新走强，市场逻辑正在切换\n\n美元正在变强\n\n最近全球外汇市场出现了一个明显变化：美元重新站住了脚跟。\n\n背后的逻辑是经济数据的分化。4月中国数据低于预期，欧洲PMI也在放缓，而美国在AI热潮和能源价格高企的环境下，反而展现出相对优势。这种分化正在强化美元的支撑。\n\n1/ 美元的“例外论”回归\n\n之前市场认为美国经济没那么特别，美元会走弱。但现在情况变了——只要能源流动受限持续，美元就会持续受益。最近欧洲货币表现疲软，不仅仅是相对价值问题，而是市场开始认真考虑长期冲击对区域经济的制约。\n\n2/ 英镑：风险溢价在波动\n\n英镑最近经历了一次完整的“风险溢价过山车”。虽然英国数据疲软、利差不利，但英镑反而走强了。关键原因是英国政治不确定性有所缓解，债券市场也企稳了。\n\n不过这种缓解可能是暂时的。结构性估值偏高、英国央行加息预期已经充分定价，加上能源冲击，中期英镑仍面临下行压力。\n\n3/ 新兴市场：高利率冲击\n\n美国长端利率快速上行对新兴市场货币构成压力。研究显示，如果10年期美债收益率月度涨幅超过20-30bp，新兴市场货币很难不承压。\n\n其中，南非兰特、哥伦比亚比索、波兰兹罗提对美债收益率最敏感。墨西哥比索相\n\n[... middle omitted ...]\n\nleration in the May flash PMIs for Europe. Prior to the conflict, we argued that less exceptional US performance should lead to a less-strong Dollar over time, but we now think Dollar performa\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R008",
    "title": "欧洲正在重新买入美国资产，但真正的结构性分歧藏在资金流向的细节里",
    "digest": "[wechat_article.md]\n# 欧洲正在重新买入美国资产，但真正的结构性分歧藏在资金流向的细节里\n\n全球资本流动正在发生一个值得注意的转向。在截至5月20日的一周内，欧洲资金重新净流入美国国债基金，而亚洲资金则持续流出。这一现象看似是风险偏好的简单修复，但某外资投行最新发布的全球基金流动周报揭示了一个更复杂的结构：资金并非均匀地回归美国，而是在资产类别、地区和行业之间展现出高度分化的选择。\n\n这份报告的核心判断是：市场当前真正低估的不是整体风险偏好的回升，而是资金流向背后反映出的“美元区间震荡预期”与“全球利率分化交易”之间的结构性张力。理解这一张力，比猜测下一个宏观数据点更能帮助投资者建立对二季度资产定价的观察框架。\n\n报告中最引人注目的图表是“本周图表”——欧元区与亚洲对美债基金的累计资金流向。自年初以来，欧元区资金持续净买入美国国债，累计流入规模已超过110亿美元；而亚洲资金则持续净流出，累计流出超过50亿美元。这一剪刀差在5月进一步扩大。\n\n报告将这一现象归结为“美元在能源冲击期间维持区间震荡，部分归因于更严格的外汇管理”。这本质上是在说：欧元区资金买入美债，并非因为看好美国经济基本面，而是在对冲欧元区自身的利率风险和汇率风险。亚洲资金的流出，则反映了不同的外汇管理压力和资产配置逻辑。\n\n这一判断如果成立，那么当前美债市场的定价就不仅仅是“降息预期”的函数，更是全球央行外汇管理策略的函数。投资者需要警惕的是，当市场将美债视为全球无风险锚定时，欧元区与亚洲资金的分化行为实际上在挑战这一锚定的稳定性。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 全球股票基金整体净流入，但结构上“科技吸金、金融失血”的格局在强化\n\n截至5月20日当周，全球股票基金净流入约24亿美元，虽然较前一周的200亿美元大幅回落，但仍保持正值。从区域来看，全球基准\n\n[... middle omitted ...]\n\n的微信群，与更多产业决策者和专业投资者一起讨论这些未解问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n欧洲资金正在回流美国\n\n📈 欧洲买家回来了\n\n全球资金流向透露了什么信号\n\n最近翻到一份投行研报，里面有个很有意思的观察：欧洲资金正在重新买入美国资产，而且力度不小。\n\n1⃣ 股票和债券都在吸金\n截至5月20日当周，全球股票基金净流入约20亿美元（前一周是20亿），虽然环比略降，但依然保持正值。美国基金需求最旺，成为全球基准基金的主要流入方向。债券基金更猛，单周净流入约32亿美元，主要靠国债和综合型债券基金撑着。\n\n2⃣ 欧洲在疯狂买美债\n研报里的“本周图表”很关键：从年初到现在，欧元区累计流入美国国债基金的资金已经超过110亿美元，而亚洲地区却是净流出约50亿美元。研报认为，这跟美元在能源冲击期间保持区间震荡有关——背后是更严格的外汇管理。短久期债券和通胀保护债券也在持续吸金。\n\n3⃣ 行业分化明显\n科技板块成为资金最爱，单周净流入规模最大。金融板块则遭遇最大净流出。从年初至今的累计数据看，工业、能源、基础设施板块资金流入最多，消费、金融、医疗板块相对疲软。\n\n4⃣ 新兴市场内部在“换仓”\n全球新兴市场基准基金和A股基金出现净流出，但韩国基金重新获得净流入。新兴市场本币债券基金净流入，而硬通货债券基金净流出\n\n[... middle omitted ...]\n\nchnology sector funds saw the largest net inflows across sectors.   \nFlows into global fixed income funds were well-supported from inflows into government and agg-type bond funds. US Treasury \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R009",
    "title": "中国车市真正的分水岭：不是需求疲软，而是内外市场正在走向“脱钩”",
    "digest": "[wechat_article.md]\n# 中国车市真正的分水岭：不是需求疲软，而是内外市场正在走向“脱钩”\n\n过去几个月，市场对中国汽车行业的讨论始终围绕一个主题：需求何时见底。补贴退坡、消费信心不足、价格战持续，这些因素叠加在一起，让投资者对国内汽车销量的判断几乎形成了一致预期——短期很难好转。但某外资投行最新发布的亚洲经济图表速览却揭示了一个更值得关注的信号：真正的结构性变化，不在于国内需求的下滑幅度，而在于国内与出口市场之间正在形成的、难以弥合的“增长裂痕”。\n\n这份报告的核心判断是：国内汽车销量在5月可能继续加速下滑至-21.6%，而出口增速却从Q1的60.7%飙升至4月的84.1%。这两个数字放在一起，不只是“内冷外热”的简单描述，而是意味着中国汽车产业的增长逻辑正在发生根本性切换——从依靠内需驱动，转向由出口和海外市场定价。对于产业链上的每一家公司，以及关注中国资产的投资者来说，这个裂痕的持续扩大，将重新定义竞争格局、利润分配和估值逻辑。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 国内需求的下滑不是周期性波动，而是政策红利退潮后的“真实水位”\n\n报告数据显示，国内乘用车零售销量增速从Q1的-17.0%进一步恶化至4月的-20.0%，5月预计降至-21.6%。表面上看，这似乎是消费疲软的延续，但仔细拆解驱动因素会发现，真正起作用的不是宏观经济的边际变化，而是两个政策的叠加效应：以旧换新补贴的收缩，以及新能源车购置税率从0%恢复到5%。\n\n这两个政策调整的共同点是：它们都在去年和今年年初人为地抬高了需求基数。当政策红利消退，市场自然会经历一个“补偿性回落”。从这个角度看，当前的下滑并不完全是坏事——它让车企和投资者看到了在没有强力刺激的情况下，中国汽车消费的“真实水位”。报告没有直接给出这个“真实水位”是多少，但如果我们对比2023年和2\n\n[... middle omitted ...]\n\n这些数据背后的二阶影响，探讨哪些公司真正具备穿越周期的能力。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月国内车市，冰火两重天\n\n国内降温，出口升温\n\n内外市场分化正在加剧\n\n最近看了份关于中国汽车市场的研报，5月的数据挺有意思的，分享几个关键点👇\n\n1️⃣ 国内销量持续走低\n5月国内汽车零售销量同比预计下降21.6%，比4月的-20%和Q1的-17%还要差。背后原因主要有两个：一是以旧换新补贴退坡后的“透支效应”，二是电动车购置税从0%恢复到5%，直接推高了购车成本。\n\n2️⃣ 出口反而加速增长\n4月汽车出口量同比暴增84.1%，比Q1的60.7%还要猛。原因是全球油气价格上涨，让中国电动车的性价比优势更突出了。能源供应链的波动，反而给中国车企创造了独特的窗口期。\n\n3️⃣ 出口救不了国内\n虽然出口增速亮眼，但出口只占中国汽车市场总量的19%（按量）和15%（按值）。出口的增量，远远填不上国内需求的缺口。\n\n4️⃣ 2026年分化只会更大\n研报判断，国内和海外市场的“温差”在2026年还会持续拉大。国内需求疲软+出口强劲，这个剪刀差大概率会越走越宽。\n\n汽车行业占GDP的3.2%，国内销量的持续下滑，对整体经济的拖累不容小觑。\n\n你觉得这波“内冷外热”会持续多久？欢迎一起讨论。\n\n#学习笔记\n\n[sourc\n\n[... middle omitted ...]\n\n-----|------|------|------|\n| Jan   | 1.8  | 1.85 | 1.65 | 1.35 | 1.75 | 1.6  | 1.3  |\n| Feb   | 1.8  | 1.85 | 1.65 | 1.35 | 1.75 | 1.6  | 1.3  |\n| Mar   | 1.85 | 1.95 | 1.75 | 1.6  | 1.8  | 1\n\n[... middle omitted ...]\n\nable upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R010",
    "title": "市场真正低估的不是降息时点，而是美联储“无限期按兵不动”的定价",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是降息时点，而是美联储“无限期按兵不动”的定价\n\n过去几个月，市场参与者始终在争论美联储会在9月还是12月降息。但某外资投行最新发布的研报做出了一个更为激进的判断：美联储将无限期维持利率不变。这不是一个关于降息时点推迟的判断，而是一个关于政策框架切换的判断。如果这一情景成立，当前资产定价中隐含的降息预期将面临系统性重估。\n\n报告的核心逻辑并不复杂，但支撑这一判断的数据信号和内部博弈细节，值得每一位关注宏观资产配置的读者仔细拆解。我们接下来将逐一展开。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 政治压力退潮后，美联储内部的鹰派共识正在加速形成\n\n市场此前对降息的期待，很大程度上建立在一个假设之上：新上任的美联储主席Kevin Warsh倾向于宽松，而特朗普政府会持续施压。但报告揭示了两个关键变化。\n\n第一个变化来自白宫。根据《财富》杂志本周一刊发的专访，特朗普对短期内降息的态度已明显软化。他的原话是：“在战争结束之前，你无法真正看数据。”更值得注意的是，他明确表示不会给新任美联储主席施压，称“我打算让他做他想做的事”。这意味着，过去一年多来支撑市场降息预期的政治压力正在系统性消退。\n\n第二个变化更为关键：美联储内部，即便是此前被认为偏鸽派的官员，也不再主张降息或保留宽松倾向。Governor Waller在近期讲话中明确表示，降息的可能性并不高于加息。他甚至呼吁从政策声明中移除所有关于宽松倾向的措辞。Philadelphia联储主席Paulson则直接表态，市场当前定价的“长时间暂停甚至加息”是健康的。\n\n这种从“鸽派官员仍在呼吁降息”到“鸽派官员也开始转向”的转变，是判断政策框架切换的核心信号。报告特别对比了1月、3月和4月三次FOMC会议的会议纪要措辞：支持保留宽松倾向的官员从“多数”退\n\n[... middle omitted ...]\n\n流。我们将基于本周的数据发布，持续更新对这一判断的验证进度。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美联储暂停降息，通胀压力仍存\n\n美联储暂停降息\n\n未来利率路径怎么看？\n\n最近某外资投行发布了一份美国经济周报，核心观点是：美联储可能无限期暂停降息。这跟之前市场普遍预期的年内两次降息（9月和12月）完全不同。\n\n为什么会出现这种转变？我梳理了三个关键原因👇\n\n1️⃣ 政治压力减弱\n特朗普最近接受采访时表示“在战争结束前不能真正看数据”，而且明确说会让新任美联储主席沃什“做他想做的事”。这意味着白宫对降息的施压明显降温。\n\n2️⃣ 通胀压力持续攀升\n虽然关税带来的通胀影响在消退，但新的涨价因素正在出现：伊朗战争推高能源价格、全球存储芯片短缺推高电子产品价格。更关键的是，S&P制造业PMI的投入价格指数从68.4飙升至79.5，创下历史最大月度涨幅。密歇根大学长期通胀预期也从3.4%跳升至3.9%。\n\n3️⃣ 经济数据依然强劲\n制造业和商业投资持续加速，GDP追踪显示Q2增速仍在2.6%左右。就业市场也在改善，ADP数据显示私人部门就业增速创系列新高。房地产市场也表现出韧性。\n\n最值得关注的是核心PCE通胀：预计4月环比上涨0.300%，同比从3.2%升至3.3%。这已经是连续第五个月上涨，而且前瞻指标显示未来\n\n[... middle omitted ...]\n\nprice pressures.\n\nWe now expect the Fed to keep policy rates unchanged indefinitely, versus our previous forecast for two cuts in September and December (Fig. 1 & 2).\n\nPolitical pressure for n\n\n[... middle omitted ...]\n\ns available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Securities International, Inc., US. All rights reserved."
  },
  {
    "id": "R011",
    "title": "欧洲医疗科技板块的估值底部已经出现，但市场需要的不只是一个好季度",
    "digest": "[wechat_article.md]\n# 欧洲医疗科技板块的估值底部已经出现，但市场需要的不只是一个好季度\n\n过去一个季度，欧洲医疗科技与生命科学板块的财报表现可以用一个词概括：勉强及格。营收大致符合预期，调整后每股收益多数超预期，但这背后有大量非经营性项目的功劳——更低的利息支出和税率在帮忙。与此同时，2026年和2027年的全年盈利预测仍在被下调，板块估值持续承压。\n\n但某外资投行最新发布的行业更新报告，提出了一个值得认真对待的判断：正因为预期已经低到极致、投资者持仓极轻，任何一点盈利修正的上行，都可能触发一轮估值修复。报告认为，板块估值可能已经触及本轮周期的底部。\n\n这不是一个激进的看多信号，而是一个基于概率和结构的判断。它不依赖需求端的强劲复苏，而是建立在“利空已基本定价、边际改善足以改变叙事”的逻辑上。对于关注欧洲医疗科技资产的投资者来说，这份报告提供了一个关键的观察框架：市场真正在等待的，不是奇迹，而是几个季度的稳定。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 盈利预期持续下修，但下修速度正在收窄，这本身就是信号\n\n报告中最直观的一张图，是覆盖范围内公司2026年和2027年调整后净利润预期的走势。自2025年初以来，两条曲线几乎同步、持续地向下倾斜，没有出现过一次像样的反弹。到2026年4月，预期水平已较2025年初下降了约15%。\n\n这种持续下修，反映了过去一年多重压力的叠加：后疫情时代的去库存、中国市场的结构性放缓、中东冲突带来的供应链扰动，以及美国医保报销政策的调整。每一轮财报季后，分析师都在下调数字。\n\n但报告隐含了一个重要观察：下修的斜率正在变缓。从2025年下半年的快速下调，到2026年第一季度末的趋稳，预期调整的节奏本身在发生变化。对于经验丰富的投资者来说，盈利预测从“加速下修”转为“减速下修”，往往是估值筑底的前奏。\n\n[... middle omitted ...]\n\n群内持续跟踪这些动态，并分享更完整的原始报告解读与数据图表。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n欧洲医疗科技Q1复盘：低预期下的反弹机会\n\n📉 低预期，反而有看点\n\n欧洲医疗科技与生命科学板块Q1财报季，整体表现可以用“平淡中带点惊喜”来形容。大多数公司营收符合预期或略低，但调整后EPS却普遍超预期（平均高出7%）。不过，这背后有“水分”——主要靠利息和税负降低等非经营性项目撑起来的。\n\n更值得关注的是，尽管季度数据不错，市场对2026和2027全年的盈利预测却在持续下调。板块估值也处于低位。但换个角度看，正因为预期很低、投资者持仓也轻，只要盈利预期稍微改善，就有可能触发一轮反弹。\n\n1️⃣ 盈利预测持续下修，但底部或已不远\n\n研报数据显示，自2025年初以来，覆盖公司的2026/2027年盈利预测指数一路下滑，从1.0降至约0.85（见研报Figure 1）。与此同时，板块远期市盈率（P/E）从2021年高峰的38倍，已压缩至2026年初的18倍左右（Figure 2）。估值已回到历史较低区间。\n\n研报认为，估值低谷可能已经出现。但投资者可能需要看到不止一个季度的企稳信号，才会真正重新入场。中东冲突若持续并推高通胀，仍是潜在风险。\n\n2️⃣ 子板块分化明显，CDMO和生命科学工具相对稳健\n\n- **C\n\n[... middle omitted ...]\n\nespite these quarterly beats, aggregate full-year consensus adjusted EPS estimates for 2026 and 2027 continued to decline across our coverage, and sector valuation levels remain depressed.\n\nGi\n\n[... middle omitted ...]\n\nk, NY 10019</td><td>Tower,</td><td></td></tr><tr><td>Tel: (44) 20 7545 8000</td><td>Tel: (1) 212 250 2500</td><td>Singapore 048583</td><td></td></tr><tr><td></td><td></td><td>Tel: +65 6423 8001</td><td></td></tr></table>"
  },
  {
    "id": "R012",
    "title": "市场共识的裂缝：机构正在从软件转向半导体，但真正的分歧藏在金融与消费里",
    "digest": "[wechat_article.md]\n# 市场共识的裂缝：机构正在从软件转向半导体，但真正的分歧藏在金融与消费里\n\n2026年第二季度刚刚过去一个多月，某外资投行追踪的1,059只对冲基金与509只大型主动管理共同基金，合计管理着约9万亿美元股票仓位。这些资金的最新持仓数据揭示了一个清晰但容易被简化的信号：机构投资者正在集体撤离软件，涌入半导体。但这只是表象。真正值得关注的，不是这个方向本身，而是共识之下那些尚未被定价的分歧——尤其是在金融和可选消费这两个板块上，对冲基金与共同基金的方向截然相反。这些分歧，可能才是下一阶段超额收益的真正来源。\n\n这份报告最核心的判断是：市场当前对“板块轮动”的叙事过于线性，而低估了不同资金性质对同一信号的解读差异。这种差异正在制造新的定价错位。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 对冲基金与共同基金的业绩分化，本质是杠杆和动量偏好的结构性差异\n\n截至5月下旬，美国股票多空对冲基金年初至今回报约7%，基本与等权标普500持平。看起来并不突出。但如果拆开来看，支撑其收益的主要是Beta和长期多头Alpha——对冲基金重仓篮子（GSTHHVIP）回报达到13%，而做空最集中的股票篮子回报高达27%。换言之，对冲基金的收益更多来自选股的两端：押注共识龙头，同时做空极端脆弱标的。\n\n共同基金的表现则更为分化。大型核心共同基金平均回报也是7%，但只有26%的基金跑赢基准，远低于32%的历史均值。在大型价值型基金中，这一比例更是跌至15%。这意味着，在当前的宏观环境下，传统选股框架的有效性正在下降。\n\n一个关键的结构性差异在于杠杆。对冲基金在3月地缘紧张初期降低了净杠杆，但随后迅速加回，目前净杠杆率已升至近五年第85百分位。总杠杆率仍然处于历史高位。而共同基金虽然将现金占比从1.1%的历史低点小幅提升至1.4%，但整体仓\n\n[... middle omitted ...]\n\n动率的联动关系。这些内容，欢迎来我们的星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n大资金正在从软件转向半导体\n\n大资金正在从软件转向半导体\n\n对冲基金与公募基金的最新动向\n\n最近读了某外资投行的研报，分析了Q2初持仓数据（覆盖约9万亿美元权益仓位），有几个有意思的发现，值得记下来。\n\n1/ 对冲基金今年表现优于公募基金\n- 对冲基金YTD回报约7%，受益于市场反弹\n- 只有30%的大盘公募基金跑赢基准，低于历史均值37%\n- 公募基金在3月地缘紧张时增持了现金，虽然现金占比仍处历史低位\n\n2/ 杠杆与做空情绪在升温\n- 对冲基金净杠杆率已回升至近5年85%分位\n- 标普500中位数个股的空头比例占市值3%，是2011年以来最高\n- 研报未给出具体做空逻辑，推测与市场不确定性有关\n\n3/ 行业偏好：共识与分歧并存\n- 共识：两者都超配工业、低配信息技术\n- 分歧：公募超配金融、低配可选消费；对冲基金正好相反\n- 方向相反：对冲基金Q1大幅加仓科技（+853bp），减仓工业；公募则小幅加工业、减科技\n\n4/ 最核心的轮动：软件→半导体\n- 对冲基金：半导体持仓创历史新高，软件持仓是2019年以来最低\n- 公募基金：剔除微软后，软件低配幅度是2012年以来最大\n- 两者都在Q2净减持微软\n- 半\n\n[... middle omitted ...]\n\nons. Hedge funds cut net leverage initially but have since lifted net exposure to a one-year high. Hedge fund gross leverage remains elevated relative to history and the median S&P 500 stocks \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R003",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Average daily RMB transaction volume of CIPS spiked in March Average daily RMB transaction volume of CIPS"
  },
  {
    "figure_id": "F002",
    "report_id": "R003",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Dim sum bond issuance nearly doubled from a year ago in Jan-Apr 2026 Dim Sum Gross Issuance (cumulative)"
  },
  {
    "figure_id": "F003",
    "report_id": "R003",
    "label": "Exhibit 3",
    "context": "Exhibit 3: RMB international use has improved, but still trails China's global GDP and trade shares"
  },
  {
    "figure_id": "F004",
    "report_id": "R003",
    "label": "Exhibit 4",
    "context": "Exhibit 4: RMB settlement leads invoicing, especially in China-related trade Share of RMB in..."
  },
  {
    "figure_id": "F005",
    "report_id": "R003",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Financial flows have become the main driver of cross-border RMB transactions Cross-border RMB transaction volume"
  },
  {
    "figure_id": "F006",
    "report_id": "R003",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Bond investment accounted for nearly half of cross-border RMB transactions in 2024 Cross-border RMB transactions by usage (2024)"
  },
  {
    "figure_id": "F007",
    "report_id": "R003",
    "label": "Exhibit 7",
    "context": "Exhibit 7: A framework for offshore RMB liquidity in Hong Kong ```mermaid graph TD"
  },
  {
    "figure_id": "F008",
    "report_id": "R003",
    "label": "Exhibit 8",
    "context": "Exhibit 8: CNH-CNY funding spreads have narrowed and stabilized since April 2025"
  },
  {
    "figure_id": "F009",
    "report_id": "R003",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Hong Kong RMB deposits tend to rise during RMB appreciation cycles"
  },
  {
    "figure_id": "F010",
    "report_id": "R003",
    "label": "Exhibit 10",
    "context": "Exhibit 10: PBOC RMB swap lines have expanded in coverage and capacity, while utilization remains low"
  },
  {
    "figure_id": "F011",
    "report_id": "R003",
    "label": "Exhibit 11",
    "context": "Exhibit 11: RMB's footprint in global derivatives markets is much larger in FX than in rates Share of RMB in global FX/rates derivatives turnover"
  },
  {
    "figure_id": "F012",
    "report_id": "R003",
    "label": "Exhibit 12",
    "context": "Exhibit 12: The onshore-offshore spread of FX forward points remains significant, while the basis risk for FX spot is limited"
  },
  {
    "figure_id": "F013",
    "report_id": "R003",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Market-maker incentives helped lift USD/CNH futures turnover in Hong Kong"
  },
  {
    "figure_id": "F014",
    "report_id": "R003",
    "label": "Exhibit 14",
    "context": "Exhibit 14: CGB futures trading is concentrated in 10y and 30y tenors, while IRS trading is mostly at the frond end Trading volume of onshore CGB futures by tenor (2025)"
  },
  {
    "figure_id": "F015",
    "report_id": "R003",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Longer-dated CGB futures provide a better hedge for long-end CGBs"
  },
  {
    "figure_id": "F016",
    "report_id": "R003",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Foreign investors have increased their holdings of RMB equities but reduced holdings of RMB bonds over the past few months"
  },
  {
    "figure_id": "F017",
    "report_id": "R005",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Current Shock is Seen as More Contained for European Natural Gas Than in 2022; Oil Shock Expected to Be More Persistent"
  },
  {
    "figure_id": "F018",
    "report_id": "R005",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Spot Gasoline Prices and Electricity Forward Prices Have Risen Since the Onset of the Conflict But Are Below Their Recent Peaks"
  },
  {
    "figure_id": "F019",
    "report_id": "R005",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Consumer Confidence Stabilised in May"
  },
  {
    "figure_id": "F020",
    "report_id": "R005",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Euro Area GSFCIs Have Tightened by Around 15bp Since the Start of the War"
  },
  {
    "figure_id": "F021",
    "report_id": "R005",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Some Relief From the Recent Easing in the GS FCI"
  },
  {
    "figure_id": "F022",
    "report_id": "R005",
    "label": "Exhibit 6",
    "context": "Exhibit 6: We Have Downgraded GDP Growth in 2026 by Around 0.8pp in the Euro Area; Pre-War Data Surprised to the Upside in the UK Q4/Q4 2026 Real GDP Growth in the Euro Area"
  },
  {
    "figure_id": "F023",
    "report_id": "R005",
    "label": "Exhibit 7",
    "context": "Exhibit 7: We Have Raised Our End-2026 Inflation Forecast By Around 2.0pp in the Euro Area and 1.7pp in the UK"
  },
  {
    "figure_id": "F024",
    "report_id": "R005",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Investor and Consumer Sentiment and Business Surveys Have Softened on Net, Price-Related Surveys Have Risen Euro Area EC Consumer Confidence: Deviations from Previous 6m Average"
  },
  {
    "figure_id": "F025",
    "report_id": "R006",
    "label": "Exhibit 2",
    "context": "Exhibit 1: Longer term UST forwards are only modestly cheap to our macro framework's estimate of fair value 5y5y UST yield vs model fair value with $+/-1$ standard deviation bands"
  },
  {
    "figure_id": "F026",
    "report_id": "R006",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Implied vol has lagged the magnitude of the rate shift 1m trailing range on 10y swap vs 1m10y implied vol"
  },
  {
    "figure_id": "F027",
    "report_id": "R006",
    "label": "Exhibit 4",
    "context": "Exhibit 3: The reduction in levered fund shorts in Treasury futures may in part reflect the diminished carry in Treasury basis Leveraged fund net UST futures position (notional, adjusted for valuation changes)"
  },
  {
    "figure_id": "F028",
    "report_id": "R006",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Bunds have been a receiver rather than provider of bearish shocks G4 yields decomposition following our spillover framework"
  },
  {
    "figure_id": "F029",
    "report_id": "R006",
    "label": "Exhibit 5",
    "context": "Exhibit 5: In the EMU-4, Italian bonds look best placed to benefit from potential oil price relief Using GS fitted yields. Credit curve = 5s10s Country XX – Germany. Beta computed since the start of the Iran conflict."
  },
  {
    "figure_id": "F030",
    "report_id": "R006",
    "label": "Exhibit 6",
    "context": "Exhibit 6: UK 5y5y levels look stretched from a macro perspective"
  },
  {
    "figure_id": "F031",
    "report_id": "R007",
    "label": "Exhibit 1",
    "context": "Exhibit 1: The net effect of the AI boom and higher-for-longer energy prices leaves the US looking like a relative outperformer"
  },
  {
    "figure_id": "F032",
    "report_id": "R007",
    "label": "Exhibit 2",
    "context": "Exhibit 2: EUR/GBP reset lower this week despite our GSBEER model implying upward pressure from shifting rate differentials amid a weaker set of UK data"
  },
  {
    "figure_id": "F033",
    "report_id": "R007",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Our model interprets this gap between actual and implied performance as relaxation in Sterling risk premium"
  },
  {
    "figure_id": "F034",
    "report_id": "R007",
    "label": "Exhibit 4",
    "context": "Exhibit 4: EM currencies depreciated between May 14 and 19, but most outperformed what shifts in rates, equities and commodities would have implied. % Actual spot return between 14 May 2026 close and 19 May 2026 close"
  },
  {
    "figure_id": "F035",
    "report_id": "R007",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Long NOK/SEK has been on par with long July Brent for vol-adjusted returns in the energy shock Vol-Adjusted Move Since Feb 27"
  },
  {
    "figure_id": "F036",
    "report_id": "R007",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Norway's fiscal mechanism reduces NOK's sensitivity to daily oil returns FX Beta to Oil vs Net Energy Exports"
  },
  {
    "figure_id": "F037",
    "report_id": "R007",
    "label": "Exhibit 7",
    "context": "Exhibit 7: The pace of monthly TRY depreciation has accelerated slightly from -1.1/1.2% to -1.5/1.6% since start of May"
  },
  {
    "figure_id": "F038",
    "report_id": "R007",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Turkiye's core trade balance (i.e. excluding energy) has been deteriorating in recent quarters"
  },
  {
    "figure_id": "F039",
    "report_id": "R011",
    "label": "Figure 1",
    "context": "Figure 1: DB EU MedTech & Life Sciences coverage BBG earnings revisions (indexed)"
  },
  {
    "figure_id": "F040",
    "report_id": "R011",
    "label": "Figure 2",
    "context": "Figure 2: DB EU MedTech & Life Sciences next FY P/E estimates"
  },
  {
    "figure_id": "F041",
    "report_id": "R012",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Equity hedge funds have returned $7\\%$ YTD"
  },
  {
    "figure_id": "F042",
    "report_id": "R012",
    "label": "Exhibit 2",
    "context": "Exhibit 2: $30\\%$ of large-cap mutual funds have outperformed benchmarks Share of mutual funds outperforming benchmarks"
  },
  {
    "figure_id": "F043",
    "report_id": "R012",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Hedge fund and mutual fund exposure to equities hedge fund data as of May 21, 2026; mutual fund data as of March 31, 2026"
  },
  {
    "figure_id": "F044",
    "report_id": "R012",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Hedge fund vs. mutual fund sector positions Sector tilts of large-cap mutual funds and hedge funds"
  },
  {
    "figure_id": "F045",
    "report_id": "R012",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Mutual funds and hedge funds have rotated from Software to Semis"
  },
  {
    "figure_id": "F046",
    "report_id": "R012",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Overlap between our mutual fund and hedge fund baskets ```mermaid graph TD"
  },
  {
    "figure_id": "F047",
    "report_id": "R012",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Mutual fund and hedge fund “shared favorites” have returned 10% YTD"
  },
  {
    "figure_id": "F048",
    "report_id": "R012",
    "label": "Exhibit 9",
    "context": "Exhibit 9: GS top-down S&P 500 forecasts"
  },
  {
    "figure_id": "F049",
    "report_id": "R012",
    "label": "Exhibit 12",
    "context": "Exhibit 12: YTD asset returns and return/volatility ratios Total return (%)"
  },
  {
    "figure_id": "F050",
    "report_id": "R012",
    "label": "Exhibit 13",
    "context": "Exhibit 13: GS US Equity Sentiment Indicator of investor positioning as of May 22, 2026"
  },
  {
    "figure_id": "F051",
    "report_id": "R012",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Recent mutual fund and ETF flows"
  },
  {
    "figure_id": "F052",
    "report_id": "R012",
    "label": "Exhibit 15",
    "context": "Exhibit 15: US equity market internal pricing of economic growth"
  },
  {
    "figure_id": "F053",
    "report_id": "R012",
    "label": "Exhibit 16",
    "context": "Exhibit 16: GS and consensus forecasts for US real GDP growth US real GDP growth"
  },
  {
    "figure_id": "F054",
    "report_id": "R012",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Market pricing of near-term and long-term interest rate outlook"
  },
  {
    "figure_id": "F055",
    "report_id": "R012",
    "label": "Exhibit 18",
    "context": "Exhibit 18: GS Financial Conditions Index"
  },
  {
    "figure_id": "F056",
    "report_id": "R012",
    "label": "Exhibit 19",
    "context": "Exhibit 19: S&P 500 52-week market breadth"
  },
  {
    "figure_id": "F057",
    "report_id": "R012",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Concentration of S&P 500 market cap and earnings in the 10 largest index constituents"
  },
  {
    "figure_id": "F058",
    "report_id": "R012",
    "label": "Exhibit 21",
    "context": "Exhibit 21: S&P 500 realized average stock correlation"
  },
  {
    "figure_id": "F059",
    "report_id": "R012",
    "label": "Exhibit 22",
    "context": "Exhibit 22: S&P 500 implied volatility"
  },
  {
    "figure_id": "F060",
    "report_id": "R012",
    "label": "Exhibit 23",
    "context": "Exhibit 23: GS IPO Barometer"
  },
  {
    "figure_id": "F061",
    "report_id": "R012",
    "label": "Exhibit 24",
    "context": "Exhibit 24: US equity mutual fund returns relative to benchmarks Exhibit 25: Realized and consensus EPS growth for select US equity indices Annual realized and bottom-up consensus EPS growth estimates"
  },
  {
    "figure_id": "F062",
    "report_id": "R012",
    "label": "Exhibit 26",
    "context": "Exhibit 26: Realized and consensus year/year S&P 500 EPS growth"
  },
  {
    "figure_id": "F063",
    "report_id": "R012",
    "label": "Exhibit 27",
    "context": "Exhibit 27: S&P 500 FY2 earnings revision breadth"
  },
  {
    "figure_id": "F064",
    "report_id": "R012",
    "label": "Exhibit 28",
    "context": "Exhibit 28: US equity index P/E valuations vs. history"
  },
  {
    "figure_id": "F065",
    "report_id": "R012",
    "label": "Exhibit 29",
    "context": "Exhibit 29: S&P 500 consensus forward 12-month P/E"
  },
  {
    "figure_id": "F066",
    "report_id": "R012",
    "label": "Exhibit 30",
    "context": "Exhibit 30: S&P 500 valuation relative to US Treasury yields"
  },
  {
    "figure_id": "F067",
    "report_id": "R012",
    "label": "Exhibit 35",
    "context": "Exhibit 35: Indexed return of select equity factors"
  },
  {
    "figure_id": "F068",
    "report_id": "R012",
    "label": "Exhibit 36",
    "context": "Exhibit 36: Equity factor valuations relative to history"
  }
]