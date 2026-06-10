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
    "title": "Citi：市场低估了本轮对外投资收紧的结构性含义，而非资本外流风险",
    "digest": "[wechat_article.md]\n# Citi：市场低估了本轮对外投资收紧的结构性含义，而非资本外流风险\n\n过去一个月，中国多部委密集出台了一系列针对对外投资的收紧措施。从国务院发布新的境外投资条例，到证监会点名三家券商并处罚其境内业务，再到香港金管局与证监会同步发布开户指引，市场的第一反应往往是“资本管制又回来了”。但Citi近日发布的一份研报给出了一个完全不同的判断：**本轮收紧的核心不是堵资本外流，而是修补监管漏洞、强化国内政策有效性，其宏观影响有限，但对行业格局和资产定价的结构性含义，市场可能尚未充分定价。**\n\n这份报告的价值在于，它没有停留在“政策收紧”的表层叙事，而是区分了两种完全不同的政策逻辑——ODI（对外直接投资）层面是国家安全考量上升，组合投资层面则是执法行动而非新规出台。这两种逻辑的宏观影响不同，对企业和投资者的含义也截然不同。\n\n以下是我们从这份研报中提炼出的五个核心洞察，以及一个报告尚未完全回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这一轮收紧与2015年的本质区别在于汇率背景和资本外流压力完全不可同日而语\n\n市场对资本管制的记忆，很大程度上仍停留在2015-2016年。当时人民币贬值预期强烈，外汇储备大幅下降，资本外流压力巨大。但Citi研报明确指出，当前宏观环境与此截然不同。\n\n报告提供了两个关键数据支撑：第一，目前人民币处于升值周期，外汇结售汇数据呈现净流入态势；第二，从国际收支平衡表测算的“无法解释的资本外流”规模，远低于2015年时期。Citi的计算显示，当前资本外流的上限是可控的——更重要的是，中东资金正在流入香港市场，这在一定程度上可以对冲收紧带来的负面冲击。\n\n这意味着，本轮收紧的政策出发点并非应对汇率危机，而是主动的结构性调整。对于投资者而言，这是一个重要的信号：不要用2015年的\n\n[... middle omitted ...]\n\n边界、税收影响和官方渠道扩容节奏这三个核心问题展开专题讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n跨境投资收紧，别慌\n\n宏观影响有限\n\n最近境内对跨境投资的监管动作不少，但某外资投行的最新研报认为，这轮收紧的核心不是控制资本外流，而是堵监管漏洞、强化政策执行效果。\n\n**1/ 政策重点在哪？**\n- 对外直接投资（ODI）：国家安全考量上升，尤其在AI竞争背景下，技术、数据审查更严，监管范围也扩大到个人。\n- 证券投资：这次是执法行动，不是新规。被点名的三家券商早在2016年就被关注过，2022年也有过一轮收紧。\n\n**2/ 为啥宏观影响有限？**\n- 人民币目前处于升值周期，不像2015年那波有贬值压力。\n- 中东资金持续流入香港，能对冲部分负面影响。\n- 研报估算，被调查的三家券商代持内地客户资产约2500亿港元，即便整治范围扩大，影响也可控。\n\n**3/ 后续关注三点**\n- **执行细节**：三家券商只是第一批，可能扩大到其他券商、保险、私募、地产。\n- **税务问题**：资金回流内地可能触发个税追缴。今年前4月个税收入同比增12.2%，部分原因是加强海外收益征税。\n- **官方渠道开放**：QDII额度（目前1760亿美元）、跨境理财通扩围、保险通试点，都有可能推进。关后门不等于不开前门。\n\n*\n\n[... middle omitted ...]\n\nas we believe the backdrop of RMB appreciation and Middle East flows into Hong Kong could alleviate the negative impact. Implementation details, second-order taxation concerns, and further ope\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R002",
    "title": "GS：市场真正低估的不是IPO供给洪峰，而是企业回购与并购需求的结构性支撑",
    "digest": "[wechat_article.md]\n# GS：市场真正低估的不是IPO供给洪峰，而是企业回购与并购需求的结构性支撑\n\n上周全球股市下跌超过2%，美国市场领跌，动量因子跑输大盘。表面看，这是美国就业数据超预期后利率路径重新定价引发的调整。但GS在最新一期《Global Weekly Kickstart》中，围绕一个看似矛盾的命题给出了一个值得深思的判断：2026年美股IPO规模将创历史纪录，但企业股权需求仍将超过供给。这不是一个简单的“利好出尽”或“供给冲击”的故事。真正值得关注的，不是IPO数量本身，而是支撑需求端的结构性力量——回购、并购与资金流入——正在如何重塑市场的定价逻辑。\n\n这份报告的洞察力在于，它没有停留在“IPO多了会抽血”的直觉层面，而是将股权供需拆解为三个维度：历史规模的相对值、企业行为的结构性变化、以及投资者情绪的真实状态。当多数人盯着IPO的绝对金额时，GS提醒我们：规模本身不是风险，供需失衡的方向才是。而当前，需求端的力量远比市场预期的更持久、更系统。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 2026年IPO规模创纪录，但放在市值中只相当于历史平均水平的2/3\n\nGS美国团队预计，2026年将成为美股历史上美元计价的股权发行最高年份。但这份报告同时给出了三个被市场忽视的对比数据。\n\n第一，IPO数量本身并不夸张。今年预计的IPO数量大约在100家左右，仅与历史平均水平持平。这意味着单笔交易的规模更大，而不是市场在无差别地接纳大量小盘股。第二，也是更关键的一点：当发行规模与美股总市值相比时，2026年的发行额仅相当于市值的1.0%，而历史平均水平是1.5%。换句话说，即便创纪录，供给的相对强度仍然低于长期均值。第三，需求端的支撑并非空谈——回购、并购和投资者资金流入构成了一个远比IPO更庞大的资金池。\n\n这三个事实合在一\n\n[... middle omitted ...]\n\n法在公开文章中完全展开，但对理解当前市场的定价逻辑至关重要。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nIPO潮来了？但需求可能更猛\n\nIPO供应创纪录？需求更强\n\n今年IPO供应创新高，但需求可能更强劲\n\n📌 全球市场上周回调超2%，美国表现偏弱。但投行团队认为，这背后有个容易被忽略的结构性变化。\n\n📌 美国劳动力数据偏强，市场对加息的预期重新升温。某外资投行已将美联储降息时间点推迟到2027年6月和12月，并预测美国10年期收益率年底升至4.4%（之前4.1%）。\n\n📌 重点来了：2026年美股IPO规模可能创历史纪录。但这不一定是坏事。\n\n1️⃣ 今年IPO数量预计约100家，仅持平历史均值。\n2️⃣ 按市值比例看，发行额仅占美股市值1.0%，远低于历史均值1.5%。\n3️⃣ 需求端有回购、并购和资金流入支撑。\n\n📌 所以结论是：供应增加≠市场承压。IPO活跃本身说明投资者愿意接盘，公司只有在市场有吸收能力时才会选择上市。\n\n📌 本周关注美国CPI、欧央行利率决议、中国信贷和贸易数据。\n\n欢迎一起讨论，你觉得IPO密集期是机会还是风险？\n\n#学习笔记\n\n[source_mineru.md]\nGLOBAL WEEKLY KICKSTART\n\n## Equities Digest Higher Rates a\n\n[... middle omitted ...]\n\npected to comment on monetary policy this week, reflecting the blackout period ahead of the June FOMC meeting.\n\nEurope: ECB policy rate; Germany, France, Spain, Norway, Sweden Inflation; Germa\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R003",
    "title": "GS：金融条件收紧的定价信号远比市场想象得更复杂",
    "digest": "[wechat_article.md]\n# GS：金融条件收紧的定价信号远比市场想象得更复杂\n\n市场正在重新定价一个被许多人忽略的信号：金融条件正在收紧，而且速度比大多数人预期的要快。这份GS最新发布的全球经济指标更新，提供了一个关键观察窗口——美国金融条件指数（FCI）在就业数据超预期后，已经收紧至俄乌冲突前的水平。这不是一个简单的“加息预期升温”故事，而是一个关于增长、通胀和资产定价之间微妙平衡的重置。\n\n为什么现在重要？因为市场此前一直沉浸在“软着陆”叙事中，认为金融条件会维持宽松以支撑风险资产。但GS的数据显示，过去一周，全球（除俄罗斯）FCI收紧3.3个基点，美国FCI更大幅收紧22.9个基点，其中股票市场贡献了13.7个基点，汇率贡献了6.4个基点。这意味着，市场自身的力量——而非央行政策——正在成为收紧的主要驱动力。对于投资者而言，理解这一动态，比猜测下一次降息时点更为紧迫。\n\n这份报告提供了一个独特的数据框架：它不仅有FCI的周度变化，还有FCI脉冲（FCI Impulse）对GDP增长的前瞻影响，以及当前活动指标（CAI）对经济现状的实时追踪。但真正有价值的，不是这些数字本身，而是它们组合在一起所揭示的“增长-通胀-金融条件”三角关系正在发生结构性转变。以下是我们基于这份研报提炼出的五个核心洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 美国金融条件收紧并非央行主导，而是市场自身在重新定价风险\n\nGS的FCI数据显示，美国FCI上周收紧22.9个基点，其中股票市场贡献了13.7个基点，汇率贡献了6.4个基点，而短期利率的贡献几乎为零。这是一个值得深思的构成：收紧的主要驱动力来自风险资产价格下跌和美元走强，而非市场对美联储加息路径的重新定价。\n\n这意味着什么？意味着市场正在主动“收紧”自己，而不是被动等待央行的信号。这种自发的收紧\n\n[... middle omitted ...]\n\n下更具防御价值？以及GS报告中那些未被充分讨论的假设和风险。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美国金融状况指数重回战前水平\n\n📊 金融状况收紧\n\n最近美国就业数据超预期，金融状况指数（FCI）收紧至2022年俄乌冲突前水平。上周美国FCI上升了22.9个基点，主要由股市（+13.7bp）和汇率（+6.4bp）驱动。\n\n1️⃣ 全球动态\n- 除俄罗斯外的全球FCI上周收紧3.3bp，股市贡献最大（+4.7bp）\n- 美国FCI从年初宽松状态快速收紧，已接近2024年水平\n- 新兴市场整体变化不大，但印度FCI明显宽松（-19bp）\n\n2️⃣ 增长预期调整\n- 某外资投行上调印度2026年GDP预测0.3个百分点\n- 台湾、韩国经济增长预期也被上调\n- 但全球整体2026年GDP预测下调0.15个百分点\n\n3️⃣ 当前活动指标\n- 全球CAI仍高于潜在增速，5月为+3.0%（年化）\n- 美国5月CAI为+3.1%，略高于上月\n- 新兴市场表现强劲，中国+5.4%，印度+7.4%\n- 日本CAI下滑0.8个百分点至+1.0%\n\n4️⃣ 通胀与工资\n- 美国、欧元区、英国的工资跟踪指标均从高点回落\n- 核心通胀仍在逐步正常化过程中\n- 就业-工人缺口在主要经济体持续收窄\n\n全球经济增长动能分化明显：美国金融条\n\n[... middle omitted ...]\n\nn     | 98.5  |\n</details>\n\nSource: GS Global Investment Research\n\n## Jan Hatzius\n\n+1(212)902-0394 | jan.hatzius@gs.com\nGS & Co. LLC\n\n## Joseph Briggs\n\n+1(212)902-2163 | joseph.briggs@gs.com G\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R004",
    "title": "Citi：美国奢侈品消费的韧性被低估了，但结构分化才是真正的故事",
    "digest": "[wechat_article.md]\n# Citi：美国奢侈品消费的韧性被低估了，但结构分化才是真正的故事\n\n美国消费者还在买奢侈品。5月Citi信用卡数据显示，奢侈品品牌整体消费同比增长3%，已是连续第五个月正增长。更值得关注的是，两年叠加增速自2024年以来首次转正，从4月的-3%回升至+2%。\n\n这个数字本身并不惊人。但放在当前宏观背景下来看——中东冲突持续、通胀粘性未消、消费者信心指数连续三个月走弱——它传递的信号远比表面增速复杂。\n\n市场对奢侈品板块的定价已经反映了相当悲观的预期。年初至今，奢侈品股票跑输欧洲市场约26个百分点，估值回调约20%，当前约20倍远期市盈率较历史均值折价15-20%。问题在于，这种折价究竟是反映了基本面实质恶化，还是市场对“消费降级”叙事的过度反应？\n\nCiti这份基于超过1000万美国信用卡持卡人样本的报告，提供了一个关键视角：美国奢侈品消费并非铁板一块，高端客群与大众客群正在走向截然不同的消费路径。而真正决定未来12个月板块走向的，不是需求总量，而是供给侧的定价策略与客群结构能否匹配。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 消费总量企稳背后，是高端客群对中低端客群的“替代效应”\n\n5月数据最核心的结构性特征是：客单价（ASP）仍保持中双位数增长，但交易客户数（交易量）同比下降约10%。这意味着，支撑增长的并非更多人在买，而是更少的人在花更多的钱。\n\n这种“量缩价升”的组合，在过去两年中已经成为美国奢侈品消费的常态。Citi报告指出，2023年至2025年期间，高收入人群的消费韧性持续优于中低收入人群，客单价增长始终跑赢客群数量增长。\n\n这背后是一个正在固化的分层逻辑。疫情期间的大幅提价（部分品牌累计涨幅超过20%）将大量中产消费者挤出了核心奢侈品购买圈层，尤其是入门级产品线——小皮具、迷你包、帆布包、\n\n[... middle omitted ...]\n\n的核心研报解读，帮助你在信息过载的时代抓住真正有价值的信号。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美国富人还在买奢侈品\n\n消费韧性超预期\n\n5月奢侈品信用卡消费同比增长3%，连续5个月正增长。虽然比4月的4%略低，但两年复合增速转正至2%，说明基础在改善。\n\n📊 核心数据拆解\n\n1️⃣ 消费结构分化明显\n- 手表零售大涨7%（前值-4%）\n- 珠宝加速至6%（前值1%）\n- 皮具放缓至2%（前值6%）\n- 成衣维持2%增长\n\n2️⃣ 高端消费者撑场面\n富裕阶层受益于股市和房价上涨，消费能力依然强劲。但中低收入群体压力加大，储蓄率降至2.6%。\n\n3️⃣ 定价策略趋于谨慎\n2026年多数品牌仅小幅提价1-3%，只有爱马仕保持5-6%的涨幅。珠宝因贵金属成本上升，提价幅度略高。\n\n💡 值得关注的变化\n- 美国对欧盟商品关税从10%升至15%，瑞士奢侈品关税从31%降至15%\n- 日本因日元贬值，奢侈品价格比中国便宜20-25%，代购活动活跃\n- 日本计划2026年11月修改免税政策，可能影响代购\n\n行业整体估值已回落至20倍PE，比历史均值低15-20%。市场对高端消费的预期已经比较保守，但实际数据似乎比想象中好。\n\n#学习笔记\n\n[source_mineru.md]\n08 Jun 2026 00:00:11\n\n[... middle omitted ...]\n\nting-customer trends (volumes), down \\~10%. Inflationary pressures continued to weigh on consumer sentiment in May. The Conference Board index edged lower as weaker current business and labour\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R005",
    "title": "摩根斯坦利：全球信用市场正在经历一场“质量分化”而非方向性转折",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：全球信用市场正在经历一场“质量分化”而非方向性转折\n\n全球信用市场过去一周的表现，表面看是方向一致的波动，但仔细拆解后会发现，真正有意义的信息藏在结构里，而非方向里。\n\n摩根斯坦利最新一期全球信用策略周报提供了这样一个信号：美国投资级信用利差走阔1bp，欧洲投资级反而收窄3bp；美国高收益走阔7bp，欧洲高收益却收窄13bp。同一类资产，两个市场，走势截然相反。这不是简单的风险偏好波动，而是一场由资金流向、供给结构和评级分化共同驱动的“质量分化”。\n\n对于配置全球信用资产的决策者来说，理解这种分化的成因，比判断整体方向更重要。因为方向可能是噪音，结构才是信号。\n\n这份周报的框架覆盖了美国、欧洲、亚洲三大市场的投资级、高收益、贷款和信用衍生品，并附带了摩根斯坦利在年中展望中确立的行业配置建议。但报告最值得关注的，不是哪一类资产涨了或跌了，而是“资金流向与价格走势之间的错位”以及“同一市场内部评级梯度的断裂”。\n\n以下是我们从这份报告中提炼出的五个核心洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 美国信用市场正在承受“供给冲击”与“权益溢出”的双重压力，但资金仍在流入\n\n美国投资级信用利差走阔1bp，超额收益为-0.1%。表面看只是微幅调整，但结合以下两个数据，就能看出压力所在。\n\n第一，美国投资级债券上周定价规模高达470亿美元，年初至今累计发行1.095万亿美元，同比增长26%。这是供给端的历史性高水位。第二，权益市场回调直接拖累了信用市场，这是报告原话“the pullback in equities also weighed on credit”。信用与权益的联动在这一周重新变得紧密，而此前市场一度认为信用可以独立于权益走强。\n\n但值得注意的是，美国投资级基金上周仍有36亿美元的净流入\n\n[... middle omitted ...]\n\n读、关键图表的原始数据，以及针对不同资产配置场景的应对框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球信用市场这一周，分化明显\n\n🌍全球信用观察\n\n上周全球信用市场走势分化，欧洲跑赢美国，高收益跑赢投资级。\n\n**1/ 美国投资级：小幅承压**\n- 利差走阔1bp，超额收益-0.1%\n- 电信、科技、公用事业表现偏弱，基础工业和服务业相对抗跌\n- 资金面依然强劲：净流入36亿美元，年内累计690亿\n- 一级发行470亿，年内总供给达1.095万亿（同比+26%）\n\n**2/ 美国高收益：贷款优于债券**\n- 利差走阔7bp，超额收益-0.1%\n- 贷款录得正总回报+0.05%，跑赢高收益债（-0.4%）\n- 电信和消费品表现垫底，能源和科技相对坚挺\n- 高收益基金净流入8.8亿，贷款基金净流入7.6亿\n- 年内高收益债发行1600亿（+42%），贷款1880亿（-3%）\n\n**3/ 欧洲投资级：表现亮眼**\n- 利差收窄3bp，超额收益+0.1%\n- 曲线牛平，BBB级表现略优\n- 媒体板块领跑，交通运输和基础工业落后\n- 基金净流入约7亿美元（占AUM的0.1%），ETF为主要流入渠道\n- 一级发行120亿欧元，年内总量3780亿（同比持平）\n\n**4/ 欧洲高收益：全面领先**\n- 利差大幅收窄13b\n\n[... middle omitted ...]\n\n5bn (+26% YoY).\n\nUS Leveraged Credit: HY spreads widened by 7bp, translating into excess returns of -0.1%. Loans delivered positive total returns at 0.05% last week, outperforming HY (-0.4%). \n\n[... middle omitted ...]\n\nCanary Wharf\n\nLondon E14 4AD\n\nUnited Kingdom\n\n+44 (0)20 7425 8000\n\n## Japan\n\n1-9-7 Otemachi, Chiyoda-ku\n\nTokyo 100-8104\n\nJapan\n\n+81 (0) 3 6836 5000\n\n## Asia/Pacific\n\n1 Austin Road West\n\nKowloon\n\nHong Kong\n\n+852 2848 5200"
  },
  {
    "id": "R006",
    "title": "GS：市场低估的不是短期补库，而是关税博弈正从“一次性冲击”变为“结构性重塑”",
    "digest": "[wechat_article.md]\n# GS：市场低估的不是短期补库，而是关税博弈正从“一次性冲击”变为“结构性重塑”\n\n过去一周，从中国发往美国的重箱船舶数量环比微增1%，同比仍为正增长3%。洛杉矶港的TEU数据预测未来两周还将保持正增长——同比增幅分别达到21.5%和34%。这些数字本身并不令人意外，毕竟去年同期正是“解放日”关税生效的基数低点。\n\n但真正值得关注的，不是这些短期数字的高低，而是数字背后的行为逻辑正在发生根本性转变。GS最新一期《美国关税影响追踪》报告揭示了一个关键判断：市场当前看到的进口韧性，并非简单的“解放日效应”被消化，而是一种新的、由不确定性驱动的补库模式正在形成。\n\n这份报告的深层价值，不在于它告诉你下周的船运数据是涨是跌，而在于它提供了一个观察框架，帮助投资者把碎片化的周度数据拼成一幅可决策的图景。对于关注全球贸易、物流运输和制造业布局的决策者来说，理解这个框架，比预测任何单一数据点都更重要。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 补库行为正在从“一次性抢跑”转向“持续性的不确定性对冲”\n\nGS的数据显示，在“解放日”周年之后，进口流量并未如部分市场预期的那样大幅回落。相反，洛杉矶港的TEU预测显示，未来两周的同比增幅仍将维持在20%以上。如果仅仅是基数效应，这个数字应该会快速收窄。\n\n报告对此给出了一个审慎但有力的解释：当前进口的韧性，部分来自“在不确定的地缘政治背景下，以较低的有效关税税率进行补库”。这句话翻译过来就是，进口商不再把关税看作一个需要一次性规避的风险事件，而是将其内化为供应链规划中的常态化变量。\n\n这意味着什么？意味着过去那种“关税宣布-抢运-库存高企-需求断崖”的脉冲式周期，可能正在被一种更平滑、但持续时间更长的补库行为所取代。进口商不再赌关税会取消或降低，而是假设关税将长期存在，并据此调\n\n[... middle omitted ...]\n\n险偏好来判断。\n\n这正是我们希望在后续讨论中继续深化的议题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美国进口数据：5月底仍在补库存\n\n海运数据透露了什么？\n\n---\n\n最近看了一份某外资投行的美国关税影响追踪报告，数据挺有意思的，给大家拆解一下关键发现。\n\n**1/ 中国→美国货运量还在涨**\n\n截至6月4日这周，从中国出发的集装箱船数量环比+1%，同比+3%。虽然增速比前几周放缓了，但绝对量还是正的。洛杉矶港未来两周的进口量预计同比+21.5%到+34%，说明5月底的补库存效应还在持续。\n\n**2/ 关税不确定性影响供应链决策**\n\n报告提到两个关键影响：\n- 短期：关税较低的国家可能会增加对美出口（比如越南、韩国等亚洲国家）\n- 中长期：企业面临150天后的政策真空期，这会影响海运合同的长期规划\n\n**3/ 地缘冲突推高运价，但影响有限**\n\n霍尔木兹海峡不是主要航线，所以对集装箱运力的冲击不会像红海危机那么大。但燃料成本上涨会推高运价，船公司已经开始转嫁燃油附加费了。\n\n**4/ 2026年运输业复苏的几个信号**\n\n- 美联储预计在2026年12月再降息一次，这对运输股是利好\n- 苹果、英伟达等大公司宣布增加美国本土制造投资\n- 新的税收法案恢复奖金折旧，鼓励企业再投资\n- 企业正在推进“中国+1”\n\n[... middle omitted ...]\n\nin some cases lower effective tariff rates amidst an uncertain geopolitical backdrop—so far, there appears to be restocking in addition to lapping Liberation Day, given the double-digit YoY im\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R007",
    "title": "Citi：NVIDIA削减Rubin内存的真正信号，不是减产，而是存储需求的二次重塑",
    "digest": "[wechat_article.md]\n# Citi：NVIDIA削减Rubin内存的真正信号，不是减产，而是存储需求的二次重塑\n\n当市场看到“NVIDIA将Vera Rubin的SoCAMM2容量削减近50%”这条消息时，第一反应通常是“需求不行了”或“供应过剩了”。但Citi这份最新研报给出了一个完全相反的判断框架：削减容量的背后，是DRAM供应瓶颈倒逼的技术路线调整，而真正的需求不仅没有被削弱，反而在向一个新的存储层级——CMX技术——迁移。\n\n这不是一个关于“减少”的故事，而是一个关于“转移”的故事。理解这个转移，才能看懂未来两年AI基础设施的存储竞争格局。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 削减SoCAMM2容量不是需求疲软，而是DRAM产能瓶颈的被动选择\n\nCiti报告明确指出，NVIDIA将Vera Rubin NVL72服务器中每颗CPU的SoCAMM2容量从1,536GB（192GB x 8）降至768GB（96GB x 8），降幅达到50%。但真正驱动这一决策的，不是NVIDIA对AI推理需求的下调，而是全球DRAM产能的硬约束。\n\n报告估算，当前内存供应商只能满足SoCAMM2总需求的60%。这是一个极为关键的数字：即使NVIDIA不主动削减，供应链也无法支撑原定的192GB模块方案。60%的供应率意味着，即便需求不变，物理上的产能天花板也在迫使所有AI硬件厂商重新设计内存架构。\n\n这里需要特别注意一个容易被忽略的逻辑：Citi认为SoCAMM2的需求总量不会因为单模块容量下降而减少。为什么？因为AI工作负载对内存容量的需求是刚性的——更大的模型、更长的上下文窗口、更高的KV Cache要求，这些都不会因为NVIDIA换用了更小容量的模块就自动消失。需求只是被“挤压”到了另一个技术路径上。\n\n## 2. CMX技术才是\n\n[... middle omitted ...]\n\n要么需要结合多个数据源交叉验证，单独阅读很容易错过关键信号。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n英伟达砍了50%内存，但NAND反而受益？\n\nDRAM不够用，NVDA改方案了\n\n投行研报拆解了这次调整的真正逻辑\n\n1/ 英伟达把Vera Rubin服务器的SoCAMM2内存容量砍了一半\n从每台55TB降到28TB，96GB模块替代了原计划的192GB\n表面看是“降配”，但核心原因是全球DRAM产能跟不上\n\n2/ 内存供应商目前只能满足60%的SoCAMM2需求\n这不是NVDA想省成本，是被逼着改设计\n但有意思的是——研报认为SoCAMM2总需求不会减少\n\n3/ 真正的变化在NAND这边\n为了补上DRAM的缺口，NVDA会引入CMX技术\nCMX作为G3.5内存来应对KV Cache需求增长\n最终结果：NAND需求会被拉起来\n\n说白了，DRAM不够用→改用NAND方案\n这条传导链在AI服务器里越来越清晰\n\n你们觉得接下来存储芯片的产能分配会怎么调？\n欢迎一起讨论\n\n#学习笔记\n\n[source_mineru.md]\n07 Jun 2026 09:18:41 ET | 8 pages\n\n# Global Semiconductors\n\nAssessing the Impact of NVDA's Rubin \n\n[... middle omitted ...]\n\nReducing Vera Rubin's SoCAMM2 Memory Capacity — According to SemiAnalysis (4-5 June), Nvidia will reduce the total SoCAMM2(DRAM) capacity of each Vera Rubin NVL 72 server from 55TB to 28TB, wh\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R008",
    "title": "GS：5月中国贸易数据超预期，但真正值得关注的不是增速，而是价格信号",
    "digest": "[wechat_article.md]\n# GS：5月中国贸易数据超预期，但真正值得关注的不是增速，而是价格信号\n\n5月中国出口同比增长19.4%，进口同比增长27.5%，双双超出市场预期的15%和26%。贸易顺差从4月的848亿美元跃升至1054亿美元。这份数据表面上看是“量价齐升”的乐观图景，但GS这份报告揭示了一个更微妙的信号：进口增长的驱动力正在从“量”转向“价”，而出口的韧性背后，结构性分化远比总量数字重要。\n\n对于关注中国资产定价和全球供应链布局的决策者而言，5月数据最值得追问的不是“增速能持续多久”，而是“价格信号在告诉我们什么”。GS的团队在报告中给出了几个关键线索，但一些二阶影响并未完全展开——这正是我们需要深入讨论的地方。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 出口超预期主要靠美国订单拉动，但低基数效应可能掩盖了真实动能\n\n5月中国对美出口同比增速从4月的11.3%飙升至35.4%，这一数字看起来惊人，但GS明确指出，部分原因是去年同期的低基数。从环比看，经季节性调整后的对美出口仅增长1.5%，远低于4月的4.2%。这意味着，对美出口的“爆发式增长”更多是统计上的错觉，而非需求端的根本性改善。\n\n更值得关注的是区域分化。对欧盟出口增速从13.4%放缓至7.6%，对拉丁美洲出口甚至出现环比下降。与此同时，对东盟出口同比增长24.3%，对非洲和其他新兴市场保持18%-22%的增速。这个格局说明：中国出口的韧性并非来自单一市场的“补库存”，而是新兴市场多元化布局的持续深化。\n\n但这里有一个尚未完全回答的问题：新兴市场的需求是否可持续？GS的报告没有深入分析东盟和非洲国家的进口能力与债务压力，而这些恰恰是判断下半年出口动能的关键变量。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 进口的\n\n[... middle omitted ...]\n\n注中国出口相关资产，这些讨论可能比任何单一数据点都更有价值。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月出口数据再超预期，强在哪？\n\n出口加速，超出预期\n\n5月出口同比+19.4%，进口+27.5%，都高于市场预期。贸易顺差扩大到1054亿美元，比4月多了200多亿。\n\n1️⃣ 对美出口大幅回暖\n- 5月对美出口同比+35.4%（4月是+11.3%）\n- 部分原因是去年基数低\n- 对欧盟出口反而放缓到+7.6%\n- 对东盟出口保持强劲，同比+24.3%\n\n2️⃣ 科技产品是出口主力\n- 半导体出口同比暴涨110.9%\n- 但出口量只增长2.1%，主要是价格拉动的\n- 铝出口+38.5%，稀土+237.4%，也都是价格驱动\n\n3️⃣ 进口价格涨了，量没跟上\n- 半导体进口额+68%，但进口量反而下降1%\n- 原油进口额+15.3%，进口量却大跌29%\n- 天然气进口额+11%，量基本持平\n- 飞机进口暴增443%，可能和中美采购协议有关\n\n4️⃣ 贸易顺差持续扩大\n- 5月顺差1054亿美元，4月是848亿\n- 出口强、进口价格高但量弱，顺差自然走阔\n\n整体看，5月贸易数据反映的是价格效应和基数效应叠加，科技品出口是最大亮点，但量的增长还需观察。\n\n#学习笔记\n\n[source_mineru.md]\n# Ch\n\n[... middle omitted ...]\n\nost. Higher import value growth seems to be more price-driven than volume-led, as evidenced by the higher chip and energy prices. Overall, the trade surplus was US\\$105.4bn in May, up from US\\\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R009",
    "title": "GS：2026世界杯对美国经济的真实冲击远小于市场想象",
    "digest": "[wechat_article.md]\n# GS：2026世界杯对美国经济的真实冲击远小于市场想象\n\n一场在大半个美国土地上持续六周的体育盛事，5到6百万现场观众，11个覆盖美国GDP三分之一的都会区。当这些数字叠加，市场很容易产生一个直觉：2026年世界杯将给美国经济带来显著脉冲。但GS最新发布的这份研报给出了一个需要审慎对待的判断——世界杯的经济影响不仅规模有限，而且几乎会在赛事结束后完全逆转。\n\n这份报告的价值不在于它确认了世界杯会带来增长，而在于它提供了一个对冲市场过度乐观的量化框架。GS基于1994年美国世界杯、过去20年的超级碗以及洛杉矶、亚特兰Daiwa盐湖城奥运会的经验数据，对2026年世界杯的就业、GDP和通胀影响做了跨场景的严谨测算。结论是：市场真正需要关注的不是世界杯带来的短期增量，而是这些增量如何被后续的回落所抵消，以及由此产生的数据噪音对趋势判断的干扰。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 就业脉冲高度集中在六月，且以临时性岗位为主\n\nGS对就业影响的估计是整份报告中最具操作参考价值的部分。根据历史数据，1994年美国世界杯期间，主办城市的就业比趋势线高出约8万人，而历届夏季奥运会的平均提振幅度约为4万人。这些增量高度集中在休闲酒店、零售贸易和运输行业，而商业服务业的招聘则在赛前数月就已提前启动。\n\nGS将此规模放大约30%以匹配2026年世界杯更大的比赛场次和观众规模，并考虑已发生的提前招聘，最终估算：6月非农就业将获得约4万人的额外提振，7月降至约1万人，8月赛事结束后转为约1.5万人的拖累，随后数月持续缓慢回归趋势。\n\n这意味着，世界杯对就业的净影响接近于零。市场如果仅看到6月非农数据超预期而解读为经济动能增强，很可能在随后的数据修正中被迫调整预期。对于宏观交易者而言，这份报告提供了一个清晰的信号：6-7月的就\n\n[... middle omitted ...]\n\n续讨论。那里有更完整的原始图表和我们对关键假设的进一步拆解。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n2026世界杯对美国经济的影响\n\n世界杯经济效应解读\n\n2026世界杯6月11日—7月19日在美国、墨西哥、加拿大举办。美国11个大都会区承办78场比赛，预计500-600万球迷到场观赛。这11个地区贡献了美国约1/3的GDP和1/4的就业。\n\n**1. 就业：6月新增4万岗位，8月回落**\n- 参考1994年世界杯和历届奥运会数据，主办城市就业在赛事期间明显上升，集中在休闲酒店、零售、交通行业。\n- 专业和商业服务类岗位会在赛前几个月提前招聘，3-4月已增加约2万人。\n- 预计6月新增4万岗位，7月新增1万，8月减少1.5万，之后逐步回归正常。\n\n**2. GDP：Q2拉动0.1个百分点**\n- 外国游客增加50-100万人，加上国内观众消费，零售销售6月上升0.3%，7月上升0.1%。\n- 综合来看，Q2 GDP年化增速提高0.1%，Q3提高0.05%，Q4小幅回落。\n- 注意：部分比赛在工作日进行，可能影响工作效率，是下行风险。\n\n**3. 通胀：酒店价格已大幅上涨**\n- 主办城市比赛日酒店价格比平时高出31%-160%，预计6月全国酒店CPI上涨约1%。\n- 餐饮和交通价格也会上扬，但幅度较小。\n-\n\n[... middle omitted ...]\n\nrs of Super Bowls, and the Olympic Games in Los Angeles, Atlanta, and Salt Lake City to estimate the impact on upcoming economic data releases including payrolls, retail sales, consumer spendi\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R010",
    "title": "Bernstein：欧洲防务股的真正定价权不在乌克兰停火，而在各国预算的不可逆扩张",
    "digest": "[wechat_article.md]\n# Bernstein：欧洲防务股的真正定价权不在乌克兰停火，而在各国预算的不可逆扩张\n\n2026年第二季度以来，欧洲防务股经历了显著回调。自年初高点算起，莱茵金属回撤超过40%，泰雷兹跌幅超过20%，莱昂纳多也在15%左右。市场的主流叙事是：乌克兰停火预期升温、地缘溢价消退、资金正在撤出这个曾经最拥挤的板块。\n\n但这份Bernstein研报提出了一个与市场直觉相反的判断：停火本身并不是欧洲防务股的真正风险，真正决定这些公司长期价值的，是各国军事预算的扩张路径是否具有结构性、不可逆的特征。而恰恰在这个问题上，市场目前的定价存在系统性低估。\n\n报告的核心主张可以概括为一句话：欧洲防务股当前12.9倍的EV/EBITDA并不便宜，但如果预算扩张路径成立，这个估值水平反而提供了未来两到三年的安全边际。关键在于，投资者需要区分“冲突溢价”和“预算周期”——前者会随停火消退，后者不会。\n\n以下是我们从这份报告中提炼出的五个层次洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 市场对停火的定价逻辑存在根本性误判：停火反而可能强化预算扩张的合法性\n\n这是整份报告最具反直觉价值的判断。Bernstein并不否认，如果出现可持续的停火，欧洲防务股会出现显著估值收缩。但他们同时指出，停火对预算的影响并非单向的负面冲击。\n\n关键逻辑在于：欧洲各国当前的扩军承诺，其政治基础已经超越了“应对乌克兰危机”这一单一事件。德国将国防支出目标设定为GDP的3.7%，法国、意大利、波兰等国的预算增长路径也已写入中长期财政框架。这些承诺的合法性来源，已经从“应对紧急冲突”转向“重建欧洲自主防务能力”这一结构性命题。\n\n换句话说，即便乌克兰实现停火，欧洲各国也很难在政治上逆转已经启动的装备采购和产能扩张计划。原因很简单：这些计划涉及到的就业、工业基\n\n[... middle omitted ...]\n\n及每只股票的风险收益分析，这些细节无法在一篇导读中完整呈现。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n欧洲防务股的逻辑，藏在预算里\n\n预算说了算\n\n年初到现在，欧洲防务板块跌了快两成。估值回到年初水平，12.9x EV/EBITDA，不算便宜，也没看到短期反弹的明显催化剂。但研报认为，长期表现的核心驱动还是军费预算增长——这个趋势会持续到2030年，哪怕乌克兰停火。\n\n1️⃣ 美国：预算大，但难落地\n2027财年预算提案1.45万亿美元，创纪录。研报预计国会不会全批，但就算只批基础预算（1.1万亿），也比2026年增长22%。BAE Systems（45%收入来自美国）和Leonardo（25%）受益最大。\n\n2️⃣ 德国：欧洲最大市场\n德国2025年军费占欧洲17%，目标2030年达到GDP的3.7%。研报测算，到2030年德国军费从1000亿欧元增至1800亿欧元，装备支出CAGR达21%。本土龙头Rheinmetall最受益，弹药、地面车辆、海军都是强项。\n\n3️⃣ 法国：专注空中+太空\n法国市场到2030年CAGR约8%。Thales和Dassault Aviation在飞机、太空、弹药、防空领域有优势。\n\n💡 三家值得看，各有各的逻辑\n- Leonardo：盈利上调空间最大，CEO换人后的下跌是入场\n\n[... middle omitted ...]\n\nc34fd69317c0e315ca7adac9d8fc45f5d0c37016654678.jpg)  \nJames Brady\n\n+44 20 7762 5272\n\njames.brady@bernsteinsg.com\n\n2026 brought more wars and political instability, but Global Defense stocks re\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R011",
    "title": "Bernstein：AI浪潮不会托起所有欧洲软件股，分化已从预期走向现实",
    "digest": "[wechat_article.md]\n# Bernstein：AI浪潮不会托起所有欧洲软件股，分化已从预期走向现实\n\n市场正在犯一个典型的“beta思维错误”——把AI当作一个可以拉升整个软件板块的行业性催化剂。但Bernstein最新发布的欧洲软件与IT服务深度研报给出了一个截然不同的判断：AI不是潮水，而是一台分选机。它正在以比多数投资者预期的更快的速度，重塑商业模式、定价权和利润率结构，其结果不是整体水位上升，而是赢家与输家之间的鸿沟加速扩大。\n\n这份报告整合了该机构2025上半年在软件和IT服务领域的研究成果，核心结论简洁但尖锐：AI已经从一个“生产力叙事”演变为“经济模型重置”。那些能够将AI嵌入核心工作流、转化为定价权和留存率的平台型企业，正在进入一个正向循环；而那些依然依赖劳动力套利或浅层功能叠加的商业模式，则面临结构性定价压力。Bernstein的评级表清晰地反映了这一判断——Outperform集中在SAP、Dassault Systèmes、Capgemini、Indra等具备“AI经济学”捕获能力的标的，而低护城河、高自动化替代风险的模型则被标记为谨慎。\n\n这不仅仅是一份评级更新。它提供了一个完整的分析框架，用以理解AI如何重新定义软件和服务的价值分配。以下是我们从这份研报中提炼出的五个核心洞察，以及一个尚未被充分回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 软件的价值正从“记录系统”迁移到“行动系统”，货币化能力成为新的分水岭\n\nBernstein提出一个关键概念转换：AI正在推动企业软件从传统的“systems of record”（记录系统）进化为“systems of action”（行动系统）。前者负责记录发生了什么，后者则直接驱动决策和行动。这个转变看似抽象，但其经济含义非常具体——价值不再由功能广\n\n[... middle omitted ...]\n\nstein评级逻辑的细节，以及我们对AI成本曲线的初步判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI浪潮下，欧洲软件股要开始“分道扬镳”了\n\n**分化已至**\n**AI不再是概念，而是业绩分水岭**\n\n最近读了一份某外资投行的研报，核心观点很直接：AI不会让所有欧洲软件公司都受益，而是会加速分化。\n\n简单说，这是一场“赢家通吃”的游戏，但赢家是谁，要看商业模式。\n\n1️⃣ **从“记录系统”到“行动系统”**\n过去软件是帮你记东西的，现在AI让软件变成帮你做事的。能嵌入工作流、直接产生自动化价值的平台（比如ERP、数据库），才是价值高地。那些只做表面AI功能的，很快会被同质化。\n\n2️⃣ **“服务即软件”正在取代人力外包**\n一个关键数据：约60%的企业客户计划在2028年前用AI服务替代传统人力交付。这意味着，传统的按人头收费模式正在崩塌，转向“结果导向、AI驱动”的新模式。能结合咨询、AI和自有IP的公司，会吃掉更大的市场。\n\n3️⃣ **护城河决定一切**\n研报用“可自动化程度”和“可防御性”两个维度来评估。高防御性领域（ERP、嵌入式工作流）很稳，AI只是加了一层价值；高自动化领域（数据分析、业务流程外包）则面临定价压力。AI很少是“灭顶之灾”，但它会重新分配整个产业链的价值。\n\n4️⃣ **\n\n[... middle omitted ...]\n\nb17a7752ffcd0c733c42576a4fa7e0f197d50321a8466c.jpg)\n\nFiroz Valliji, CFA\n\n+1 917 344 8316\n\nfiroz.valliji@bernsteinsg.com\n\n![](images/a907b22ab54fa86520a92cabc1c5f507c28c5ed0542dacc0c1573ca2cf9a\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R012",
    "title": "Bernstein：广告市场真正被低估的不是总量增长，而是结构性再分配中的定价权迁移",
    "digest": "[wechat_article.md]\n# Bernstein：广告市场真正被低估的不是总量增长，而是结构性再分配中的定价权迁移\n\n全球广告市场正处在一个微妙的拐点。一方面，数字广告依然保持着两位数的增长，2024年全球数字广告支出预计将达到近7000亿美元。另一方面，传统媒体的广告收入增长几乎停滞，甚至在某些季度出现负增长。市场的主流叙事仍然聚焦于“数字化渗透率还有多少空间”这样的总量问题。\n\n但Bernstein这份最新研报提供了一个更具穿透力的结构性判断：广告增长的核心驱动力并非消费总量的扩张，而是注意力的再分配。全球媒体消费时间已经稳定在每天约11小时，这意味着总库存的增长空间极为有限。真正发生的是价值在不同格式、不同平台之间的系统性迁移。而这场迁移的赢家，将不是那些拥有最多用户的平台，而是那些能够将规模优势转化为不可替代的定价权的玩家。\n\n这份报告的价值不在于罗列数字广告的增长数据，而在于它提供了一个理解广告市场底层逻辑的分析框架。它揭示了两个截然不同的广告市场、两阶段增长模型，以及一个正在被市场低估的关键变量——碎片化带来的执行复杂性溢价。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 两个截然不同的广告市场，决定了完全不同的增长韧性与估值逻辑\n\nBernstein的核心洞见之一，是将全球广告市场拆分为两个本质上不同的市场。这不是一个简单的“线上vs线下”的二分法，而是一个基于客户结构、收入稳定性和增长驱动力的根本性区分。\n\n市场一由传统媒体和广告代理构成。这个市场的特点是高度集中、强周期性，收入高度依赖数千个大客户。在经济下行周期，广告支出往往成为企业最先削减的成本项。这种结构决定了其收入的波动性极高，且与宏观消费信心指数高度相关。Bernstein的数据显示，这类市场的收入在宏观压力下可能出现两位数的季度波动。\n\n市场二由数字平台主导。\n\n[... middle omitted ...]\n\n美欧市场的对比视角，这些内容对于形成自己的投资判断至关重要。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球广告市场，正在重新洗牌\n\n广告市场没有“必赢”\n\n全球广告市场规模约1万亿美元，但增长逻辑已经不是“总消费扩张”，而是“注意力的再分配”。\n每人每天媒介消费时间约11小时，基本见顶了——\n所以品牌要争夺的，不是更多时间，而是更精准的注意力。\n\n1/ 广告其实分两种市场\n市场#1：传统媒体+广告代理，依赖几千家大客户，经济一差最先被砍预算。\n市场#2：数字平台，靠数百万中小企业撑起2/3的收入，增长更稳、韧性更强。\n这解释了为什么数字平台总是跑赢传统玩家。\n\n2/ 数字广告进入第二阶段\n第一阶段（2010s）：中小企业上线，靠自助工具投放。\n第二阶段（2023起）：库存扩张（零售媒体、电商平台、流媒体）+ 规模化个性化。\n零售媒体尤其值得关注——高毛利、近乎零边际成本，还能精准触达。\nAI也在加速这一切：定向、创意、转化，全链路优化。\n\n3/ 传统玩家在变，但不够快\n电视台、户外广告、广告代理也在做数字化延伸（比如ITVx、VIOOH），增速不错。\n但这些新业务占集团收入比例太小，核心的线性广告还在下滑。\n客户集中+周期敏感，投资吸引力有限。\n\n4/ 关键指标看什么\n- 数字广告增长 = 用户量 × 竞价价\n\n[... middle omitted ...]\n\n8faa.jpg)  \nLaurent Yoon\n\n+1 917 344 8502\n\nlaurent.yoon@bernsteinsg.com\n\n![](images/ed382a0c394d98db8749613d0c2ee4d35c0eddc6fff8d63399243eebe16b72c3.jpg)  \nNikhil Devnani, CFA\n\n+1 917 344 8425\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R013",
    "title": "JPM：金属市场的真正拐点不在需求，而在供给成本的结构性重置",
    "digest": "[wechat_article.md]\n# JPM：金属市场的真正拐点不在需求，而在供给成本的结构性重置\n\n中国金属消费数据正在传递一个比表面数字更复杂的信号。JPM最新一期的中国金属活动追踪报告显示，铜的消费连续第六周趋弱，铝的去库存却在加速，而锌的库存已攀升至2022年以来同期最高水平。如果只看到“需求疲软”，就会错过这份报告真正想要表达的核心判断：大宗商品投资者面临的风险，已经从需求侧的周期性放缓，转向供给侧的持续性成本膨胀——而后者正在从根本上改变金属和采矿行业的估值锚点。\n\n这份于6月8日发布的周度追踪，覆盖截至6月5日的数据窗口。表面上看，它是一份常规的高频库存监测。但JPM的分析师团队在数据背后铺设了一条清晰的逻辑链：中国需求的确在放缓，但真正值得警惕的是，霍尔木兹海峡的持续关闭正在通过航运成本、能源价格和采矿耗材三个渠道，对金属供给端施加远超预期的压力。当需求侧的下行与供给侧的成本上行同时发生，市场的定价逻辑就必须被重新审视。\n\n报告的核心结论是：JPM正在系统性降低其对EMEA（欧洲、中东和非洲）金属与采矿板块的敞口，仅对挪威海德鲁（Norsk Hydro）维持超配评级，原因在于后者的铝业务和区域溢价暴露。这不是一个简单的周期判断，而是一个关于成本结构如何重塑竞争格局的战略论断。\n\n以下是对这份报告逻辑的深度拆解。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 铜的“弱”不是问题，问题的关键在于它为什么没有变得更弱\n\n铜库存数据确实指向需求走软。截至6月5日当周，中国铜显性库存（SHFE加保税区）净变动基本持平，这是连续第六周库存去化动力不足。与3至4月份异常强劲的消费相比，当前确实是一个明显的减速。但JPM分析师明确指出，这种减速符合正常的季节性规律，并预计这种趋势可能还会持续数周。\n\n真正值得关注的是库存的绝对水平。目前中国铜库存\n\n[... middle omitted ...]\n\nPDF，并就霍尔木兹海峡情景对金属定价的二阶影响做专题交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n铜铝走势分叉，锌库存创三年新高\n\n金属需求分化进行时\n\n最近一期外资投行的中国金属库存追踪数据出来了，几个关键发现值得关注👇\n\n**铜：需求连续六周走弱**\n铜库存去化速度明显放缓，过去一周库存基本没怎么动。虽然3-4月消费异常强劲，但5月后明显降温。目前铜库存约220kt，比去年同期高40kt左右。研报判断这符合季节性规律，预计未来几周还会延续。\n\n**铝：去库加速，表现亮眼**\n铝是这期唯一亮点。过去一周去库26kt，比同期季节性均值略强。总库存1.4Mt，虽然处于2019年以来同期最高，但去库趋势在改善。\n\n**锌：库存逆势累积**\n锌库存上周出现累库，总库存达到264kt，创2022年以来同期最高水平。这与铜铝形成鲜明对比。\n\n**宏观背景：需求偏弱+成本承压**\n5月官方PMI已经反映出制造业活动走弱，这是金属需求放缓的直接原因。更麻烦的是霍尔木兹海峡的持续关闭，推高了铁矿石运费——从澳大利亚、巴西、南非到中国的运费自冲突以来都涨了50%以上。油价、运费、采矿耗材成本都在涨，给金属企业带来双重压力。\n\n**机构策略：偏好铝，回避其他**\n基于以上判断，研报继续建议降低欧洲、中东和非洲的金属矿业敞口。\n\n[... middle omitted ...]\n\neeks. Aluminum's momentum has continued to pick up with another de-stocking in the past week of 26kt, which is slightly stronger vs seasonal average this time of the year.\n\nOverall, metals dra\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 07 Jun 2026 09:40 PM BST\n\nDisseminated 08 Jun 2026 03:10 AM BST"
  },
  {
    "id": "R014",
    "title": "GS：服务器市场的真正拐点不是AI，而是传统服务器被重新定价",
    "digest": "[wechat_article.md]\n# GS：服务器市场的真正拐点不是AI，而是传统服务器被重新定价\n\n当市场目光几乎完全锁定在AI服务器的爆发式增长时，一份来自GS的最新研报揭示了一个更具结构性的信号：传统服务器市场正在经历一次被严重低估的重新定价。\n\n这不是一个关于“AI还能涨多少”的故事。这是一个关于“非AI部分正在发生什么”的故事。GS援引650 Group的最新数据，将2026-2030年传统服务器市场的年均预测上调了约31%，预计到2030年市场规模将达到1640亿美元。相比之下，AI服务器市场的同期预测上调幅度为18%。数字本身已经说明问题：传统服务器的增速预期修正幅度，几乎是AI服务器的两倍。\n\n为什么这个信号重要？因为在过去两年里，几乎所有关于数据基础设施的讨论都被AI服务器垄断。传统服务器被视为“存量业务”甚至“夕阳业务”。但这份报告的核心判断是：市场可能低估了企业端和超大规模云厂商在非AI计算资源上的系统性投入。这不是周期性补货，而是由工作负载结构调整、安全合规需求以及AI推理链条中传统算力的“伴生需求”共同推动的结构性变化。\n\n报告发布的时间窗口也值得注意。C1Q26的数据显示，Dell Technologies在传统服务器市场的份额从一年前的20%跃升至30%，单季营收同比增长85%。这不仅仅是市场份额的转移，更意味着整个行业的需求基础正在发生质变。\n\n以下是我们从这份GS研报中提炼出的五个核心洞察，以及一个尚未被完全回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 传统服务器市场预期的大幅上修，揭示的不是补库存，而是企业IT支出的结构性重置\n\nGS在本次更新中，将2026-2030年传统服务器市场的年均预测上调了约31%，单位出货量预期上调19%，平均售价预期上调10%。这个修正幅度在过去的服务器周期中非常\n\n[... middle omitted ...]\n\n份报告的完整数据和图表，继续拆解这些关键问题。欢迎加入讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n服务器市场大洗牌，谁是赢家？\n\n📊 服务器格局剧变\n\n某外资投行最新研报更新了服务器市场数据，核心结论：整个服务器市场规模到2030年预计达1.4万亿美元，年复合增长率38%。\n\n1️⃣ AI服务器：2030年预计达1.24万亿美元\n- 比之前预测上调约18%\n- 增长主要来自Neocloud（上调22%）和Hyperscaler（上调17%）\n- 五年CAGR高达45%\n\n2️⃣ 传统服务器：2030年预计达1640亿美元\n- 比之前预测大幅上调约31%\n- 企业级和Hyperscaler各上调约48%和47%\n- 五年CAGR约13%\n\n3️⃣ 厂商份额变化（2026年Q1数据）\n- Dell：传统服务器份额从20%→30%，AI服务器从5%→17%\n- HPE：传统服务器份额持平在11%，AI服务器份额下滑\n- Super Micro：AI服务器份额从8%→11%，但Neocloud领域被Dell反超\n\n💡 有意思的细节：Dell在Neocloud AI服务器市场份额已到48%，企业级AI服务器更高达47%，成为最大赢家。\n\n从数据看，AI服务器市场增速远超传统服务器，但传统服务器也并未停滞。整个服务器\n\n[... middle omitted ...]\n\nutlook across units and +10% increased outlook across ASPs.  \nDELL's C1Q26 traditional server revenue was up +85% year-over-year, driven by a +24% year-over-year increase in units and a +49% y\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R015",
    "title": "摩根斯坦利：面板价格周期的高点已至，市场定价的乐观情绪正在透支未来",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：面板价格周期的高点已至，市场定价的乐观情绪正在透支未来\n\n这份摩根斯坦利在2026年6月发布的TFT-LCD面板价格展望报告，传递了一个清晰且克制的信号：面板价格在经历了一轮温和上涨后，正在接近本轮周期的顶部。对于关注面板行业的投资者而言，真正需要警惕的不是6月价格的短期波动，而是当前估值已经反映了太多尚未兑现的乐观预期。\n\n报告的核心判断可以概括为一句话：TV面板价格将从三季度开始转跌，IT面板价格将从四季度开始走弱，而市场对“新兴业务”的期待——尤其是玻璃基板在先进封装中的应用——短期内难以贡献实质性的业绩增量。这意味着，当前台湾面板厂商的股价，已经跑在了基本面之前。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. TV面板价格的红利期仅剩一个季度，供给纪律正在被需求走弱所抵消\n\n摩根斯坦利预计，6月主流TV面板尺寸的价格将环比持平。这一判断本身并不令人意外，真正值得注意的是报告对后续趋势的定性：从三季度开始，TV面板价格将进入下行通道。\n\n支撑这一判断的逻辑链条是清晰的。需求端，年初以来品牌厂商的提前备货正在退潮，面板订单动能明显放缓。供给端，尽管面板厂仍然展现出良好的产出控制纪律，但上半年强劲的出货量意味着下半年的出货量可能低于季节性水平，这将进一步削弱面板厂的议价能力。\n\n报告隐含的一个关键洞察是：供给纪律虽然能够为价格提供下行支撑，但无法阻止价格拐点的到来。在需求走弱和出货量低于季节性的双重压力下，面板厂“控产保价”的策略效果将逐步递减。这本质上是周期力量对人为干预的修正。\n\n从季度平均价格来看，报告预计2Q26 TV面板价格仍可实现低个位数的环比增长，但这已经是本轮上涨的尾声。对于投资者而言，三季度开始的价格下行预期，意味着当前估值中隐含的持续涨价假设需要被修正。\n\n![研报原图 2]\n\n[... middle omitted ...]\n\n们将结合更多行业数据，对报告中的关键假设进行持续跟踪与验证。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n面板价格走到拐点了？6月数据解析\n\nTV面板6月持平，IT面板微涨\n\n某外资投行最新研报拆了TFT-LCD面板6月价格展望，信息量挺大，直接上干货👇\n\n**1️⃣ TV面板：6月持平，但Q3可能转向**\n\n主流32\"到75\" TV面板6月价格环比持平。原因是：\n- 年初补库存高峰已过，订单动能放缓\n- 面板厂继续控制产出，供给端有支撑\n\n但研报判断：TV面板价格从Q3开始可能下行，不过跌幅不会太大。因为供给侧纪律还在，能给价格托底。Q2整体均价环比还是小幅上涨的。\n\n**2️⃣ IT面板：整体稳定，显示器微涨**\n\n- 显示器面板：环比+0.2%\n- 笔记本面板：环比持平\n\nIT面板未来几个季度会比TV面板更稳一些。\n\n**3️⃣ 玻璃基板先进封装：还要等**\n\n研报认为玻璃基板在先进封装里确实有优势（尺寸大、信号损耗低、热膨胀系数匹配好），但供应链还在优化工艺，2026-27年可能还看不到明显贡献。\n\n**4️⃣ 估值吸引力下降**\n\n随着面板价格可能从Q3开始走弱，研报认为目前估值吸引力不大。特别是台湾面板厂，市净率已经超过过去几年峰值。中国大陆面板厂中，更偏好京东方（规模优势+显示业务集中）。\n\n**5\n\n[... middle omitted ...]\n\npanel order momentum is slowing. On the supply side, panel makers continue to demonstrate good discipline in controlling output. We continue to believe that TV panel shipments could be below s\n\n[... middle omitted ...]\n\ny Co Ltd (6515.TW)</td><td>O (04/17/2026)</td><td>NT$8,425.00</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R016",
    "title": "摩根斯坦利：市场低估了这份利率新规对银行净息差的修复力度",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：市场低估了这份利率新规对银行净息差的修复力度\n\n6月5日，中国人民银行发布了《人民币存款和贷款利率管理规则》的征求意见稿。这份文件看似技术性极强，聚焦于利率计算、罚息规则和机构职责界定，但摩根斯坦利在第一时间发布的研报中给出了一个清晰且值得重视的判断：这是对银行净息差趋势的明确利好，且影响同时作用于资产端收益率和负债端成本。\n\n这不是一次简单的规则更新。1999年的旧框架运行了超过25年，期间中国利率市场化改革经历了贷款基础利率(LPR)形成机制、存款利率自律上限调整、以及近年来的多次降息周期。旧规则已经无法覆盖当前市场环境下的复杂定价行为。新规的核心意图，不是微调技术细节，而是为市场化的利率定价建立一套清晰的规则书，并明确传递出打击不公平、非法竞争的信号。\n\n对于关注中国银行业资产定价逻辑的投资者而言，这份征求意见稿的意义不在于它改变了什么短期数字，而在于它从制度层面为银行的收入恢复和利润稳定增长提供了支撑。市场当前的讨论多停留在“政策意图”层面，但摩根斯坦利的分析框架提示我们，真正需要被定价的，是这一规则对银行间竞争格局的结构性重塑。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 新规最直接的冲击是堵死了“高息揽储”的制度漏洞\n\n存款市场的无序竞争长期以来是中国银行业净息差压力的重要来源之一。部分银行，尤其是中小银行，为了争夺存款规模，采取了多种变相高息揽储的手段。新规明确禁止了这些行为，包括非法手工补息、突破自律机制上限、以及存贷挂钩等操作。\n\n这不仅仅是监管态度的重申。旧框架下，这些行为的界定和处罚缺乏明确的规则依据，导致监管执行存在灰色地带。新规将禁止性条款写入正式的《利率管理规定》，意味着从此有了清晰的执法标尺。摩根斯坦利在报告中指出，这对银行净息差在负债端成本上的改善是积极的。\n\n更\n\n[... middle omitted ...]\n\n完整数据表格、银行间的横向对比，以及后续政策落地的动态影响。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n央行出手，存款利率新规来了\n\n📌 银行定价新规则\n\n6月5日，央行发布《人民币存贷款利率管理规则》征求意见稿，核心是推动利率更市场化、更公平竞争。\n\n1/ 银行可以自主定价，但必须透明\n金融机构可根据央行规则和商业原则，自主设定存贷款利率。但贷款成本要包含利息和直接相关费用，且必须明示年化利率和罚息年化利率。\n\n2/ 高息揽储被明确禁止\n包括非法手工补息、突破自律上限、存贷挂钩等行为，统统被点名禁止。这能有效遏制存款市场的无序竞争。\n\n3/ 对银行净息差是利好\n研报认为，新规对银行资产端收益率和负债端成本都有正向影响，有助于银行收入持续修复和利润稳定增长。\n\n这次是1999年以来首次全面更新利率管理框架，把利率计算、结息规则、机构责任等统一规范，为市场化定价立下了明确规矩。\n\n大家觉得这对存款利率会有什么影响？欢迎一起讨论。\n\n#学习笔记\n\n[source_mineru.md]\n## China Financials | Asia Pacific\n\n# New Consultation Paper on RMB Deposit and Loan Interest Rate Management Rules t\n\n[... middle omitted ...]\n\nanism.  \nBanks are explicitly prohibited from high-interest deposit solicitation, as it could lead to disorder in deposit market competition.  \nLenders must clearly display annualized loan rat\n\n[... middle omitted ...]\n\npment Bank (600000.SS)</td><td>E (08/05/2025)</td><td>Rmb9.34</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R017",
    "title": "GS：新能源车市场真正的压力测试，不是销量，而是定价权的转移",
    "digest": "[wechat_article.md]\n# GS：新能源车市场真正的压力测试，不是销量，而是定价权的转移\n\n市场正在被一个被低估的信号重新定义。\n\n2026年5月，中国新能源车零售渗透率达到63%，批发渗透率突破61%。这两个数字看起来像是行业高歌猛进的注脚。但GS最新发布的周度图册（China New Energy Vehicle Weekly Chartbook, Week 23）揭示了一个更值得警惕的图景：在渗透率创新高的同时，终端折扣正在同步扩大，部分品牌的订单环比出现两位数下滑，而锂价在6月初一周内下跌超过6%。\n\n这不是一个简单的“需求好”或“需求差”的故事。GS这份报告的核心价值，在于它把订单、折扣、库存、原材料价格和事件日历编织在一起，指向一个正在成形的行业拐点：新能源车市场正在从“规模扩张竞赛”切换进入“盈利韧性考验”。而市场对这一切换的定价，可能仍然不够充分。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 渗透率新高背后，订单动能正在从“脉冲”回归“常态”\n\n5月新能源车零售渗透率63%，批发渗透率61.1%，相比4月的62.8%和57.3%均有提升。单看这个数字，很容易得出“电动化势不可挡”的判断。但GS跟踪的周度订单数据给出了一个更精细的叙事。\n\n2026年第23周（6月1日至6月7日），主要新能源品牌合计订单同比增长7%，但环比下降了15%。GS明确指出，这一环比下滑是“在新车型上市初期脉冲消退之后”发生的。这意味着，5月下旬新车发布带来的订单集中释放效应正在衰减，市场正在回归到更真实的周度需求水平。\n\n更值得关注的不是总量，而是结构。在环比维度上，吉利、特斯拉、比亚迪表现出“防御性增长”——环比分别增长12%、1%和下降2%。这三家头部企业的订单韧性，与行业内其他品牌形成了鲜明对比。而在累计同比维度上，蔚来以85%的同比增速\n\n[... middle omitted ...]\n\n论，我们一起跟踪这些关键变量的演变，在数据中找到真正的信号。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n新能源渗透率突破63%\n\n渗透率63%，新能源车真的站起来了\n\n刚翻完某外资投行最新周报，5月新能源车零售渗透率冲到63%，批发端也到了61.1%。\n\n几个关键数字拆开看👇\n\n1️⃣ 订单节奏：新车上市脉冲之后，W23周订单环比回落15%，但同比还有+7%。头部梯队里，吉利+12%、特斯拉+1%、比亚迪-2%，整体还算稳。\n\n2️⃣ 渗透率跳升：5月新能源零售974k辆，渗透率63%，比4月的62.8%微涨；批发端更猛，从57.3%跳到61.1%。燃油车压力继续加大。\n\n3️⃣ 价格战没停：新能源经销商平均折扣7.79% vs 官方指导价，比上周又宽了一点。燃油车更狠，折扣19.54%，还在加码。碳酸锂价格跌到16.85万/吨，周降6.1%，电池成本继续友好。\n\n4️⃣ 重点新车日历：6/11蔚来乐道L60改款发布，6/17比亚迪大唐上市，6月底理想L8改款，7/1各家月销数据出炉。\n\n5️⃣ 品牌分化：蔚来YTD订单同比+85%最猛，问界+29%，特斯拉+3%。小米、理想、小鹏的YTD同比还在负区间。\n\n简单说：新能源渗透率上去了，但折扣也在扩大，新车上市节奏密集，6月看点不少。\n\n你们觉得63%的渗透率还\n\n[... middle omitted ...]\n\nhlights:\n\n■ Key brand orders: Geely / Tesla / BYD showed defensive growth at +12%/+1%/-2% wow.  \n■ CPCA weekly trend: As of May 1-31, PV retail volume was 1,545k units (-20% yoy/+12% mom), whi\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R018",
    "title": "GS：公积金改革范围超预期，但市场真正低估的是供给侧的再定价信号",
    "digest": "[wechat_article.md]\n# GS：公积金改革范围超预期，但市场真正低估的是供给侧的再定价信号\n\n中国房地产市场的焦点正在从“成交量能走多远”转向“制度变量如何重塑行业定价逻辑”。GS在最新一期周报中给出了一个值得反复推敲的判断：公积金改革的范围超出了此前预期，但市场对这一变化的定价可能仍然偏保守。周度交易量虽然环比回落，但同比仍在扩张，更重要的是，情绪指标保持稳定——这不是典型的政策刺激后的快速衰减，而更像是一种新的稳态正在形成。\n\n这份报告的核心价值不在于周度数据本身，而在于它提示了一个正在发生的结构性变化：政策工具正在从单纯的“需求刺激”转向“制度优化+供给调控”的组合。公积金改革、新开工与竣工的持续分化、以及库存去化周期的微妙变化，这些信号叠加在一起，指向一个更深刻的命题——中国房地产市场的再平衡，可能比多数投资者预期的更早到来，但路径也将更加分化。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 公积金改革的制度红利被低估，其影响将超越短期的需求刺激\n\nGS在报告中明确指出，住建部最新发布的《住房公积金管理条例》修订征求意见稿，在三个维度上超出了市场预期。最值得关注的是两点：一是将自住住房装修和物业管理费纳入提取范围，二是明确将灵活就业人员纳入缴存体系。后者的潜在覆盖人群据估算超过2亿人。\n\n这不仅仅是扩大公积金的使用场景，更是一次制度性的“扩围”。过去市场对公积金改革的预期主要集中在贷款利率下调和使用门槛降低上，但这次修订触及了公积金作为“住房金融基础设施”的核心定位。当灵活就业人员能够合法、合规地参与公积金体系，意味着这部分此前被排除在正规住房金融之外的购买力，有了进入市场的通道。\n\n从时点上看，这一改革发生在市场情绪已经企稳、但交易量尚未显著回升的阶段。GS的数据显示，尽管第23周新房销售面积环比下降13%，但同比仍增长15\n\n[... middle omitted ...]\n\n下行空间、以及资产质量定价框架下哪些开发商最有可能获得重估。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n公积金改革超预期，扩围至装修和物业费\n\n🏠 楼市周报速览\n\n上周（第23周）新房成交环比-13%，同比+15%；二手房环比-7%，同比+31%。虽然成交量有所回落，但市场情绪保持稳定。\n\n**公积金改革三大亮点：**\n1️⃣ 提取范围扩大：自住住房装修（有额度限制）和物业管理费也可提取，未来还可能纳入更多住房消费场景\n2️⃣ 缴存范围扩容：个体工商户、灵活就业人员正式纳入全国范围，覆盖超2亿灵活就业人群\n3️⃣ 跨区域互认互贷：全国范围内实现公积金异地互认和贷款\n\n研报观点：装修和物业费的纳入超预期，后续关注公积金贷款利率进一步下调的可能性。\n\n**市场数据速览：**\n- 新房搜索量环比持平\n- 新挂牌速度与5月相当\n- 经纪人和购房者价格预期稳定\n- 库存月数27.8个月（5月均值28.5）\n\n**完工量预测：**\nGSPC跟踪指标显示5月完工量同比降幅约17-19%，全年预计同比-1%。\n\n**估值参考：**\n覆盖房企股价平均周跌7%，国企开发商表现相对抗跌。\n\n欢迎一起讨论你对公积金改革和楼市走势的看法。\n\n#学习笔记\n\n[source_mineru.md]\n## CHINA PROPERTY WEEK\n\n[... middle omitted ...]\n\n2) formalizing nationwide participation eligibility for individual business owners, part-time workers and flexible employees, broadening from the previous 36-city pilot scheme and targeting a \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R019",
    "title": "摩根斯坦利：工程机械的景气周期比市场想象的更强",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：工程机械的景气周期比市场想象的更强\n\n市场对5月中国挖掘机销量的预期是“增速放缓”，但实际数据给出了完全不同的信号。摩根斯坦利最新发布的5月挖掘机销售追踪报告显示，当月总销量同比增长36%，其中国内销量增长39%，出口增长34%。这三个数字都显著超出市场此前的悲观预期。\n\n更值得关注的是，这份增长不是靠低基数或政策脉冲的短期刺激。报告明确指出，5M26累计销量同比增长25%，国内和出口分别录得18%和33%的累计增速。这意味着，从年初至今的景气度是可持续的，而非单月波动。\n\n为什么这份报告值得产业决策者和投资者仔细阅读？因为它揭示了一个正在发生的结构性变化：中国工程机械行业正在经历从“国内周期驱动”向“全球竞争力驱动”的转变。摩根斯坦利在报告中不仅更新了数据，还提供了与三一重工、中联重科管理层交流后的最新判断——两家公司对2Q26的展望都偏向积极。\n\n以下是我们从这份报告中提炼出的四个关键洞察，以及一个报告尚未完全回答的核心问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 国内市场的韧性来自“提前发债”与“电动化替换”的双重支撑，而非地产复苏\n\n市场对中国工程机械国内需求的最大担忧，是房地产投资持续疲弱。但5月国内销量39%的同比增长，说明推动力来自其他方向。\n\n摩根斯坦利在报告中给出了两个核心驱动因素。第一是地方政府专项债券（LGSB）的提前发行。资金到位后，基建项目开工率提升，直接拉动了挖掘机的采购需求。第二是电动化挖掘机的替换需求。随着环保政策趋严和电动设备经济性改善，存量设备的更新换代正在形成独立的增量市场。\n\n这两个因素叠加，使得国内需求在当前宏观环境下依然保持了强劲增长。5月销量环比下降14%，这属于正常的季节性波动，不应被过度解读为趋势逆转。\n\n这里的含义非常明确：**国内工程机\n\n[... middle omitted ...]\n\n你希望获得更完整的视角，欢迎来我们的星球和微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月挖机销量，超预期36%\n\n超预期增长\n\n国内+39%，出口+34%\n\n5月挖掘机销量数据出来了，比大家担心的好很多。\n\n📊 整体销量24,794台，同比增长36%\n虽然环比降了14%，但同比增速很猛。\n\n📈 国内：11,628台，同比+39%\n两大驱动力：\n1️⃣ 地方政府专项债提前发行，资金到位\n2️⃣ 电动化替代需求释放，换机周期来了\n\n三一、徐工、柳工从5月中旬开始提价，利润端改善可期。\n\n🌍 出口：13,166台，同比+34%\n中东冲突+油价上涨背景下还能这么稳，主要是欧洲、拉美、非洲市场份额持续提升。\n\n📌 某外资投行调研反馈：\n- 三一预计二季度营收同比增~20%，海外需求+产品结构优化+定价稳定\n- 中联重科认为外汇拖累减弱后，海外增长会加速\n\n全球工程机械上行周期还在继续。\n\n#学习笔记\n\n[source_mineru.md]\n## China Industrials | Asia Pacific\n\n# May Excavator Sales: Growth Much Stronger than Feared\n\nMay-26 sales grew 36% YoY (-14% MoM, 5M\n\n[... middle omitted ...]\n\n Africa.\n\nWe remain positive on the global construction machinery upcycle. After meetings with Sany and Zoomlion last week, we came away positive on their 2Q26 outlook. Sany guides to c.20% Yo\n\n[... middle omitted ...]\n\nomlion Heavy Industry (000157.SZ)</td><td>O (09/08/2025)</td><td>Rmb7.52</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted."
  },
  {
    "id": "R020",
    "title": "摩根斯坦利：市场正在低估这一轮资本开支周期的宽度和持续性",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：市场正在低估这一轮资本开支周期的宽度和持续性\n\n这份报告的标题或许可以更直白：摩根斯坦利在近期对中国工业企业的调研后，得出的核心判断是，市场当前对AI驱动的资本开支周期的理解，仍然过于集中在半导体和算力硬件本身，而低估了这一轮周期向更广泛设备领域传导的力度、速度以及结构性含义。\n\n这不是一份关于“AI服务器出货量”或“GPU需求”的报告。这是一份关于“当AI开始重塑制造业的每一个环节，谁在真正获益”的调研记录。摩根斯坦利的分析师团队在近期密集走访了超过20家中国工业领域的头部公司，涵盖自动化、机器人、电池设备、工程机械、阀门等多个细分赛道。调研反馈的强度，甚至超过了他们自己在今年3月的前一次调研。\n\n报告传递的信号非常清晰：这一轮资本开支周期，正在从AI硬件设备，向通用设备、自动化、以及更广泛的先进制造领域扩散。而且，这种扩散不是线性、温和的，而是伴随着技术迭代、产品升级和供应链重构的复合型扩张。对于产业决策者和投资者而言，理解这一轮周期的宽度，比猜测某一季度的出货量数字重要得多。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI需求正在从“算力基建”向“设备升级”传导，且传导效率超出预期\n\n调研中最明确的信号来自AI设备供应链。摩根斯坦利发现，几乎所有与AI相关的设备供应商，对2026至2027年的订单和收入增长都给出了极为乐观的展望。这种乐观不是孤立的，而是基于三个结构性的驱动力。\n\n第一，AI直接推动了产品和设备的升级，带来更高的单价和利润率。报告中提到的案例非常具体：大族激光用于AI服务器、光模块和TGV的超快激光钻孔设备，单价和毛利率显著高于传统产品；麦格米特在Rubin电源架中的潜在机会，价值含量和利润率更高；GKG精密应用于AI服务器的锡膏设备，毛利率达到约65%，远高于其他下游应\n\n[... middle omitted ...]\n\n和投资领域的同行一起，持续跟踪这一轮超级资本开支周期的演变。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI拉动的设备升级周期，比想象中更强\n\n**超级资本开支周期已来**\n\n最近跟某外资投行的工业团队跑了趟调研，聊了30多家公司，回来感受很明确：这一轮AI驱动的设备资本开支，不只是AI服务器硬件，而是向更广泛的自动化、机器人、电池设备扩散，范围更广，节奏也更猛。\n\n**1/ AI设备需求是最大超预期项**\n\nMS团队认为，AI带来的设备升级有三个结构性变化：\n- 产品升级带来更高单价和毛利。比如大族激光的AI服务器超快激光钻孔设备，单台售价500-700万；GKG精密的AI服务器焊膏设备毛利率高达65%。\n- 技术迭代催生增量设备需求。光模块组装自动化、X-ray CT检测设备、AOI检测都在快速上量。\n- 国内企业在快速迭代中持续抢占份额，海外竞争对手产能瓶颈明显。\n\n**2/ 苹果供应链比预期更强劲**\n\n2026-27年的创新周期在支撑设备需求。苹果相关机会从传统3C自动化扩展到3D打印、均热板、摄像头模组、UTG玻璃。明年预计有6款新手机，包括一款纪念版机型。大族激光透露，苹果相关项目毛利率通常在40%以上。\n\n**3/ 自动化、机器人、工程机械基本面扎实**\n\n- 自动化：信捷电气5月订单同比增长3\n\n[... middle omitted ...]\n\nmbines massive scale with rapid technology iteration, driving continuous equipment upgrade demand.  \nMost of the companies we met are expanding capacity, widely passing on strong demand to ups\n\n[... middle omitted ...]\n\ny Industry (000157.SZ)</td><td>O (09/08/2025)</td><td>Rmb7.52</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R021",
    "title": "摩根斯坦利：市场低估的不是AI需求，而是“旧存储”的供给再定价",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：市场低估的不是AI需求，而是“旧存储”的供给再定价\n\nComputex 2026刚刚落幕，当绝大多数市场目光聚焦于Nvidia的Vera CPU、Agentic PC以及云端AI芯片的算力竞赛时，摩根斯坦利半导体团队发布了一份视角独特的会后总结。这份报告的核心判断，与市场主流叙事形成微妙但重要的错位：真正值得关注的超额收益机会，可能不在云端芯片，也不在AI PC，而在被多数人视为“过时”的旧存储领域。\n\n报告标题直接点明了这一排序——“Cloud, PC and old memory”，而最后的“old memory”恰恰是这份报告最想传达的增量信息。摩根斯坦利认为，市场对2027年CPU、GPU及周边芯片的强劲前景已有一定共识，对AI PC的谨慎也相对充分，但真正被低估的，是SLC NAND、高密度NOR等“旧存储”在AI推理时代的结构性短缺。这一判断，叠加近期板块股价波动，为投资者提供了一个具有吸引力的入场窗口。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 云端芯片的确定性来自供给约束，而非需求争议\n\n关于云端半导体，市场的主要分歧从来不是需求强弱。GPU服务器持续 ramp up，CPU服务器因AI与agentic应用而需求旺盛，这些已是共识。摩根斯坦利在Computex上获得的关键增量信息，更多集中在供给侧的细节变化。\n\nARM服务器DRAM含量偏低的问题，报告明确指出这本质上是“supply issue”——不是需求不足，而是供给端尚未充分适配。这一判断意味着，一旦供应链完成调整，相关内存接口芯片的需求弹性可能超出当前市场预期。与此同时，CXL（Compute Express Link）正在成为扩大x86 CPU中RDIMM使用的关键推动力，这直接利好全球内存接口芯片的领导者。\n\n更具\n\n[... middle omitted ...]\n\n的答案，可能就藏在报告的细节图表与未完全展开的分析框架之中。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nComputex 2026 云、PC、老内存的硬核观察\n\n云端需求强劲，PC 半导体现曙光\n\n1️⃣ **云端半导体：需求旺盛，供给是瓶颈**\n- GPU 服务器持续上量，规格微调\n- CPU 服务器需求强劲，主要由 AI 和智能体应用驱动\n- ARM 服务器 DRAM 含量较低，更多是供给问题\n- CXL 相关组件有望提前至 2026 年 Q4 导入，扩大 RDIMM 使用\n- 投行研报看好 Aspeed（BMC 内容）和 Montage（内存接口芯片）\n\n2️⃣ **PC 半导体：智能体 PC 有潜力，但价格不菲**\n- RTX Spark NB 升级 CPU、内存，部分品牌还升级到 4K 屏\n- 高端台式机配置：128GB DRAM + 4TB SSD，起售价约 1 万美元\n- 短期内 PC 半导体客户愿意接受涨价，毛利率有望保持稳定\n- 看好 Parade 和 Elan 的新成长驱动，Realtek、Novatek、Asmedia 相对谨慎\n\n3️⃣ **老内存：SLC NAND 需求飙升，NOR Flash 涨价**\n- 数据中心 NAND 需求 2025-2031 年 CAGR 达 34%，AI \n\n[... middle omitted ...]\n\n for strong demand: GPU servers continue to ramp up with some minor changes to specs. CPU servers see strong demand mainly on AI/agentic applications (link). The lower DRAM content on ARM serv\n\n[... middle omitted ...]\n\n5.TW)</td><td>O (04/17/2026)</td><td>NT$8,425.00</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\nTiffany Yeh\n\n© 2026 MS"
  },
  {
    "id": "R022",
    "title": "NOM：市场低估了中国造船的结构性护城河，真正的风险不在需求侧",
    "digest": "[wechat_article.md]\n# NOM：市场低估了中国造船的结构性护城河，真正的风险不在需求侧\n\n过去一年，关于中国造船业市场份额“腰斩”的叙事在媒体上反复出现。从2024年占全球新船订单约四分之三，到2025年中期一度被韩国反超，这组数据被广泛解读为华盛顿制裁政策的初步成效。然而，NOM最新发布的研报提出了一个更值得深思的判断：这种波动主要反映的是周期性因素和统计口径的扭曲，而非中国造船业竞争力的结构性衰退。真正需要关注的，不是中国份额的短期起伏，而是全球造船业供给格局正在经历的深层变化——以及美国在试图重建产能时所面临的硬约束。\n\n这份报告的核心洞察在于：市场将注意力过多放在了需求端的地缘政治扰动上，却低估了中国造船业在供给端已经建立的、由成本、规模和绿色转型共同构筑的护城河。同时，华盛顿的“盟友造船”战略虽然声势浩大，但其推进速度恰恰暴露了美国自身工业能力的瓶颈。理解这两条线的交汇，才是把握未来几年全球航运与造船资产定价的关键。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 中国份额的V型反弹揭示的是“统计幻觉”，而非竞争力衰退\n\nNOM的分析首先澄清了一个被广泛误读的关键事实。中国在全球新船订单中的份额确实经历了剧烈波动：从2024年的约70%（甚至更高）降至2025年中期的低点，彼时韩国在月度订单上短暂领先。但到2025年全年，中国份额已回升至约63%，并在2026年第一季度进一步恢复至接近70%的水平。如果看中国工信部按载重吨统计的数据，这一数字更高，达到69%。\n\n这个V型走势并非政策奏效的证据，而是三种力量交织的结果，其中两种是暂时的或统计性的。第一种力量是政策驱动的订单分流。在2025年4月至10月美国贸易代表办公室（USTR）301条款停泊费从公布到实施之间的窗口期，船东为了规避不确定性，确实有动机将涉及美国贸易航线的订\n\n[... middle omitted ...]\n\n，我们将基于这份报告和后续数据，持续跟踪这些关键变量的演变。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国造船，比你想的稳\n\n中国造船优势仍在\n\n全球订单波动，拆解后核心逻辑没变\n\n1/ 去年中国造船份额从75%跌到50%多，今年Q1又回到70%——这个V型反弹，不是政策转向，而是周期+情绪的双重修复。全球订单在2025年整体下滑27%，跌的主要是散货船和油轮，偏偏是中国最强的板块。分母变小，份额自然难看。\n\n2/ 政策扰动是真实的，但也是暂时的。去年美方301收费落地后，船东确实在避开中国船厂，韩国一度领先。但今年美中休战协议一出，份额立刻回升——说明不是竞争力问题，而是避险情绪。\n\n3/ 中国在绿色船舶上已经卡位。Q1 2026，80%的新订单是绿色燃料船，包括甲醇双燃料箱船和大型LNG船。这块是未来高价值赛道，中国正从跟跑变成领跑。\n\n4/ 韩国在帮美国造船，但日本基本退出了商业造船市场。Q1 2026日本份额只有1%，创30年新低。美国想靠盟友造船，实际上只能靠韩国。\n\n5/ 美国海军自己产能严重不足。攻击核潜艇年产量1.2-1.3艘，但AUKUS要求至少2.33艘。缺口只能靠盟友，但日本帮不上忙，韩国能帮多少也有限。\n\n6/ 未来最大的不确定不是竞争，而是周期。这一轮订单高峰过后，必然会有放缓阶段—\n\n[... middle omitted ...]\n\n, leaving the suspension set to expire on 10 November 2026, with no successor framework currently in place.\n\nOn the order book, the widely reported narrative of a decline in China's market sha\n\n[... middle omitted ...]\n\nable upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R023",
    "title": "NOM：工业AI的货币化，市场低估了2-3年过渡期的结构性摩擦",
    "digest": "[wechat_article.md]\n# NOM：工业AI的货币化，市场低估了2-3年过渡期的结构性摩擦\n\n市场对工业AI的讨论，大多集中在“谁先落地”、“谁有模型”、“谁拿到订单”这些叙事层面。但NOM在2026年6月发布的最新研报中，提出了一个更值得深思的框架性判断：工业AI在短期内不是独立的增长引擎，而是附着在存量DCS（分布式控制系统）基础上的收入放大器。真正决定胜负的，不是AI模型的能力，而是谁能把AI嵌入到已经存在的工业控制基础设施中。\n\n这份报告的核心洞察在于，它没有陷入“AI赋能一切”的乐观叙事，而是指出了市场普遍低估的一个关键变量——从当前状态到工业AI规模化落地，中间存在一个2到3年的“过渡痛苦期”。这不仅仅是技术成熟度的问题，而是涉及客户采购习惯、跨厂商兼容性、以及商业模式从项目制向订阅制切换的结构性障碍。\n\n对于关注中国自动化赛道的投资者和产业决策者来说，这份报告提供了一个难得的冷思考视角：在工业AI的宏大叙事背后，真正的货币化路径远比想象中曲折。以下是我们从报告中提炼出的五个关键层次，每一个都指向一个尚未被充分定价的判断。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 工业AI的竞争，不是模型之争，而是存量工业基础设施的“附着权”\n\n市场容易将工业AI与通用大模型混为一谈，认为谁的自然语言处理能力强、谁的参数规模大，谁就能在工业场景中胜出。NOM的调研给出了截然不同的结论：中国流程工业的AI堆栈建立在四个软件支柱之上——TPT（时序预训练Transformer）、UCS（通用控制系统）、AOP（自主运行工厂）和OMC（运营管理与控制系统），它们全部层叠在开源基础模型之上。这意味着，底层模型的同质化程度很高，真正的差异化来自垂直行业的工艺知识积累。\n\n报告清晰地绘制了国内OT（运营技术）厂商的定位地图：中控技术锚定石化化工，和\n\n[... middle omitted ...]\n\n那里会有更细致的拆解，以及来自不同产业背景的读者之间的碰撞。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n工业AI落地，还得再熬2-3年\n\n工业AI的真相\n\n不是软件革命，是硬件改造\n\n最近翻到一份外资投行的工厂自动化研报，核心观点很直接：工业AI短期内不是独立增长引擎，而是现有系统的“收入放大器”。\n\n1️⃣ AI落地靠的是“旧瓶装新酒”\n工业AI不是凭空出现的产品，而是捆绑在已有的DCS（分布式控制系统）上卖的。比如某石化自动化龙头，1Q26工业AI收入1.84亿，但其中≥20%是捆绑了DCS硬件。说白了，客户买的是升级版的老系统，不是全新的AI方案。\n\n2️⃣ 两条完全不同的变现路径\n- 软件派：把AI打包成TPT（时序预训练模型）+AOP（自主运营平台），按订阅制卖给化工客户。\n- 硬件派：比如汇川技术，把AI和算力直接塞进伺服驱动器、电机和专用PLC里，靠硬件拉动变现，而不是卖软件订阅。这种方式更“物理融合”——AI是附在设备上的，不是独立存在的。\n\n3️⃣ 为什么还要等2-3年？\n- 国企客户对订阅制有抵触，担心数据安全和国产替代问题。\n- 不同厂商的协议不兼容，比如西门子的Profinet和某国产厂商的Modbus桥接不了，项目卡壳半年以上。\n- 虽然工业AI软件毛利率（≥20%）远高于DCS（<1\n\n[... middle omitted ...]\n\nCS rollout, and a recent industry survey that reiterates the view that: monetisation remains anchored to the legacy DCS installed base, with the AI-led inflection still gated by a 2-3 year tra\n\n[... middle omitted ...]\n\nable upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R024",
    "title": "NOM：人民币中间价定价模型正在释放比市场预期更复杂的信号",
    "digest": "[wechat_article.md]\n# NOM：人民币中间价定价模型正在释放比市场预期更复杂的信号\n\n当多数市场参与者将注意力集中在人民币汇率的短期波动与政策干预时，一份来自NOM亚洲外汇策略团队的最新报告揭示了一个更值得关注的深层变化：人民币中间价的定价模型正在经历一次系统性的重新校准，而这种校准的幅度与方向，可能比任何一次单一的政策表态都更具长期含义。\n\n这份于2026年6月8日发布的报告，核心在于其提供了一个可量化的中间价预测模型。模型显示，在不包含逆周期因子的情况下，当日预测值为6.7921，较前值大幅调低236个基点，同时较前一交易日官方收盘价高出209个基点。而纳入逆周期因子调整后，预测值变为6.8109，较前次定盘价仅低48个基点。\n\n这组数字本身并不复杂，但它们叠加在一起，指向了一个关键的判断：市场对人民币汇率的定价逻辑，可能正在从“单边预期管理”转向“多目标动态平衡”。这不仅仅是技术层面的模型调整，更是政策框架演进的一个可观测窗口。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 模型误差的收敛，暗示着定价效率的结构性提升\n\nNOM报告中的第二张图表，展示了模型误差（不含逆周期因子调整）的长期趋势。从2025年初接近-1800个基点的巨大负向误差，到2026年4月已收窄至约600个基点。这条曲线的斜率变化，比任何绝对值都更有意义。\n\n误差的快速收敛，意味着市场力量与官方定价之间的背离正在系统性缩小。2025年初，模型系统性地高估了人民币的贬值压力，实际中间价远强于模型预测。而到了2026年，两者的差距已大幅收窄。这背后可能的原因有二：一是市场本身的预期变得更加理性，二是官方定价机制对市场信号的响应更加灵敏。\n\n对于投资者而言，这意味着过去依赖“中间价偏离度”来捕捉政策意图的策略，其有效性正在下降。当模型误差趋于零时，中间价本身所包含\n\n[... middle omitted ...]\n\n并组织专题讨论，共同拆解人民币定价背后的政策逻辑与市场博弈。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n人民币中间价怎么看？一个模型就够了\n\n📊 中间价模型解析\n\n某外资投行刚出了一份人民币中间价预测模型研报，几个关键信息值得一看：\n\n**1. 模型预测值**\n- 最新模型预测：6.7921（不含逆周期因子）\n- 加入逆周期因子后：6.8109\n- 相比前值下调236个基点，说明模型认为人民币有升值压力\n\n**2. 主要驱动因素**\n- 欧元贡献最大（+67个基点）\n- 韩元（+34）、澳元（+27）、墨西哥比索（+11）紧随其后\n- 一篮子货币的波动直接影响中间价定价\n\n**3. 模型误差在收敛**\n- 从年初的-1800基点逐步收窄至+600基点\n- 说明模型对央行行为的预测精度在提升\n\n**4. 近期重要事件**\n- 7月底政治局会议（经济工作定调）\n- 11月深圳APEC峰会\n- 12月中央经济工作会议\n- 年底习主席访美\n\n这些事件都可能影响汇率政策方向。\n\n**一点思考**：模型显示逆周期因子仍在发挥作用，说明央行对汇率预期管理态度明确。后续重点关注7月政治局会议对经济的表述。\n\n#学习笔记\n\n[source_mineru.md]\n## USD/CNY fix model\n\nGlobal Marke\n\n[... middle omitted ...]\n\nge (without counter-cyclical factor)  \n![](images/72e246005223017cba5d2edaa3c8d41e4066efa848aef05c4b4ba1486de72b13.jpg)\n\n<details>\n<summary>bar chart</summary>\n\nTop 4 weighted contribution to \n\n[... middle omitted ...]\n\nrmation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R025",
    "title": "NOM：人民币中间价模型正在释放一个被市场忽略的定价信号",
    "digest": "[wechat_article.md]\n# NOM：人民币中间价模型正在释放一个被市场忽略的定价信号\n\n市场对人民币汇率的讨论，大多集中在贸易摩擦、资本流动和央行意图上。但一份来自NOM亚洲外汇策略团队的模型报告，提供了一个更底层、更可量化的视角：**人民币中间价的定价机制，正在发生结构性偏移，而这种偏移的幅度和方向，可能被多数交易员低估了。**\n\n这份报告的核心工具是一个基于一篮子货币的中间价预测模型。模型显示，在剔除逆周期因子后，最新的中间价预测值为 6.7812，较前一日的官方收盘价低了 32 个基点。更重要的是，这一预测值较上一期模型结果大幅下调了 386 个基点。这不仅仅是日常波动，而是一个值得关注的信号。\n\n为什么现在重要？因为市场往往只关注最终公布的中间价，而忽略了模型本身所揭示的“无干预”状态下的均衡位置。当模型预测与官方定价之间的偏差持续扩大，或者模型本身出现趋势性偏移时，它往往意味着央行面临的定价压力正在积聚，也预示着未来政策调整的潜在方向。\n\nNOM这份报告的价值，不在于给出了一个具体的数字，而在于提供了一个可跟踪的、透明的分析框架。它让投资者能够从“猜测央行意图”转向“观测模型压力”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 模型预测的偏移，本质上是外部货币环境变化的映射\n\n这份NOM模型的预测逻辑，并不是基于对中国经济基本面的直接判断，而是基于一篮子货币的加权变动。这恰恰是理解人民币中间价定价机制的关键：**央行通过设定中间价，在管理预期和反映市场供求之间寻找平衡，而一篮子货币的波动是其中最重要的客观锚点。**\n\n报告中的图 1 清晰地展示了这一点。在贡献最大的四个货币中，韩元和欧元的权重贡献均为负的 13 个基点，而澳元为正的 3.5 个基点，俄罗斯卢布为负的 3.5 个基点。这种分布并非巧合。\n\n韩元的大幅走弱，反映\n\n[... middle omitted ...]\n\n的深层逻辑，分享如何将这些模型框架转化为实际的投资决策依据。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n人民币中间价，一个重要信号📊\n\n中间价模型指向6.78\n\n比前值低了近400点\n\n**正文**\n\n最近某外资投行更新了USD/CNY中间价预测模型，数据挺有意思，拆开看看：\n\n1️⃣ **模型指向6.78**\n最新预测6.7812，比前值6.8198低了386个点。如果加入逆周期因子，预测值落在6.8109，比前次低89个点。\n\n2️⃣ **谁在拉动变化？**\n从权重贡献看，欧元和韩元是主要拖累项（各贡献-13个点），澳元小幅正向拉动（+3.5个点），卢布则是微负（-3.5个点）。这些货币的隔夜波动，共同构成了中间价的调整参考。\n\n3️⃣ **模型误差在缩小**\n观察近一年模型误差：去年初误差高达-1800点，年中回归零附近，近期误差收窄至600点以内。说明模型对中间价的拟合精度在提升。\n\n4️⃣ **重要时间窗口**\n下半年国内事件密集：7月政治局经济会议、10月国庆假期、11月亚太经合组织会议（深圳）、12月中央经济工作会议。年底还有中美高层会晤安排。这些节点都会影响汇率预期。\n\n整体来看，中间价机制在维持“有管理的浮动”，逆周期因子仍在使用，说明政策端对汇率节奏有把控。误差收窄也意味着市场预期与官方定价\n\n[... middle omitted ...]\n\n)  \n![](images/fff8e90ae874167ec88c8ddb87ab8ddab6338e431f4ca818f22976f7ffe35625.jpg)\n\n<details>\n<summary>bar chart</summary>\n\n| Currency | Top 4 weighted contribution to projected change (pips\n\n[... middle omitted ...]\n\nrmation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R026",
    "title": "GS：美国供应链的“新常态”比市场预期的更早到来",
    "digest": "[wechat_article.md]\n# GS：美国供应链的“新常态”比市场预期的更早到来\n\n市场观察者仍在等待新一轮供应链危机的爆发信号——关税冲击、地缘冲突、港口劳资谈判，每一个变量都被视为潜在的导火索。但GS最新的供应链拥堵追踪报告给出了一个值得认真对待的判断：美国供应链的拥堵水平已经回落至疫情前基线附近，并且这种状态可能比大多数人预期的更具持续性。\n\n这份发布于6月初的报告显示，GS每周供应链拥堵指数在最近一周环比上升了7%，但瓶颈规模评分仍维持在“2”的水平。这个数字意味着什么？在2021年底至2022年初的供应链危机高峰期，该评分曾达到“10”的顶峰。而当前“2”的水平，已经与2020年疫情前的流动性水平基本一致。更重要的是，GS5月的周度平均拥堵评分同样录得“2.0”，这一结果不仅远低于2021年12月至2022年1月的峰值，而且与疫情前基线几乎完全对齐。\n\n这不是一个短期波动，而是一个结构性信号。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮变化真正考验的是企业能否把规模转化为议价权\n\nGS在报告中明确指出，如果供应链压力继续缓解，该指数有望在2026年更持续地停留在“1”的区间。这绝不是一句轻描淡写的预测。它意味着，过去三年驱动全球物流成本飙升、港口拥堵、运价暴涨的核心变量，正在从“供给不足”转向“需求正常化”。\n\n对于投资者和企业决策者来说，这一判断的含金量在于：它不是一个孤立的港口数据改善，而是整个物流体系的系统性恢复。从GS追踪的指标来看，西海岸集装箱船等待靠泊数量已经连续数周保持在“1”的水平，东海岸虽然从4上升至5，但相比2021年动辄数十艘的积压，已是天壤之别。铁路多式联运方面，西海岸一级铁路（联合太平洋和伯灵顿北方圣达菲）的周度平均运量增速从上周的+14%大幅放缓至-2%，这并非需求崩塌，而是高基数效应和正常化进\n\n[... middle omitted ...]\n\n继续讨论这些未解问题，以及GS原报告中的完整图表和数据逻辑。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美国港口不堵了？供应链回到疫情前\n\n📦 供应链大松绑\n\n某外资投行最新周度数据显示，美国供应链拥堵指数连续维持在低位，拥堵等级仅2级（满分10），已接近疫情前水平。\n\n1️⃣ 西海岸港口：等泊集装箱船数量维持在1艘，几乎无压港\n2️⃣ 东海岸港口：略有回升，从4艘增至5艘\n3️⃣ 铁路运输：西海岸联运量同比增速放缓至-2%（上周+14%）\n4️⃣ 海运价格：中国→美西航线运价同比+16%，增速小幅加快\n5️⃣ 底盘周转：全美港口平均停留时间微增，但整体可控\n\n📊 关键指标一览：\n- 月度拥堵评分：5月均值约2.0，较2021年底峰值（10.0）大幅回落\n- 集装箱平均停留时间：稳定在2.6-2.8天\n- 门到门运输时效：中国→美国约47天，波动不大\n\n如果关税和地缘冲突不引发新的需求冲击，供应链压力有望在2026年进一步降至“1”级区间。当前货运需求温和，运力供给充足，整体流动性已回到疫情前水平。\n\n大家觉得供应链恢复正常后，对出口和物流行业会有什么影响？欢迎一起讨论\n\n#学习笔记\n\n[source_mineru.md]\nTRACKING U.S. SUPPLY CHAIN CONGESTION\n\n## GS\n\n[... middle omitted ...]\n\nck scale remained at '2' this week, reflecting the absolute level of the congestion index increasing on a sequential basis (+7% w/w after last week's -5% move; Exhibit 2). For this week's scal\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R027",
    "title": "JPM：香港地产市场真正的考验不是政策阴云，而是数据能否持续验证复苏",
    "digest": "[wechat_article.md]\n# JPM：香港地产市场真正的考验不是政策阴云，而是数据能否持续验证复苏\n\n过去两周，香港地产股跑输恒生指数7%。一个旧隐忧尚未消散——内地资本外流管控可能收紧；一个新隐忧又浮出水面——美国强劲的就业数据重新点燃了加息预期。两个“悬顶之剑”同时压境，市场情绪迅速转冷。\n\n但JPM在这份最新研报中给出了一个值得细品的判断：这两个隐忧本身，都不足以推翻香港住宅市场的复苏趋势。房价年初至今已上涨9.6%，该机构维持2026财年全年10%-15%的涨幅预测。真正值得关注的，不是这些担忧会不会发生，而是市场需要什么样的证据才能重新建立信心。\n\n这份报告的价值不在于罗列风险，而在于它提供了一个清晰的框架：在不确定性中，哪些变量真正决定方向，哪些公司会在震荡中相对坚挺，以及投资者应该在什么位置重新入场。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 两个“悬顶之剑”都未落地，但市场已经提前定价\n\n第一个隐忧是内地资本外流管控可能收紧。市场担心这会切断来自内地买家的需求。JPM在5月底和6月初的两份报告中已经详细拆解过这个问题：截至目前，没有官方禁令禁止内地居民在香港购房；资本外流管控并非新政策，历史上已有先例；即使在最极端情景下——所有“基于内地的内地买家”完全退出市场——他们只占成交量的5%-10%，按金额计算也仅为10%-15%。更重要的是，报告中区分了“基于内地的内地买家”和“基于香港的内地买家”，后者受到的影响应该有限。香港楼市的绝大多数买家仍然是本地居民。\n\n第二个隐忧是加息预期重燃。美国劳动力数据超预期后，市场开始重新定价利率路径。JPM目前维持利率暂停至2027年一季度的预测。但如果美国真加息，香港最优惠利率可能跟随上调，按揭利率也会走高。不过报告指出一个关键细节：如果利率维持在现有水平，香港购房者仍然享有边际正\n\n[... middle omitted ...]\n\n。对于真正理解香港地产市场的人来说，这才是最稀缺的认知工具。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n香港楼市：一波未平，一波又起\n\n两个“阴云”，一个判断\n\n📌 过去两周，香港地产股跑输恒指7%，主因是市场担心内地收紧资本外流。上周末，新的担忧又来了：美国就业数据强劲，加息预期重燃。\n\n**1/ 两个担忧，哪个更值得留意？**\n\n- **资本外流管控**：目前没有官方禁止内地人买香港房产。最坏情况下，即使所有“内地居住的内地人”停止购买，他们只占成交量的5-10%（按金额算10-15%）。真正受影响的是启德高端盘，因为那里内地买家占比最高。\n- **加息重燃**：如果美国加息，香港最优惠利率可能跟随，按揭利率会上升。但研报指出，利率暂停在当前水平的话，香港购房者仍享受微弱的正利差（名义按揭利率3.25%，实际2.9-3.0%，而租金收益率约3.0%）。历史上2004-06和2016-18年，加息期间香港房价和地产股仍在涨。\n\n**2/ 两个担忧都还没落地**\n\n- 资本管控方面，即使国务院出台细则，研报推测可能不会明确提及香港购房（目前只针对非法跨境投资）。\n- 加息方面，JPM维持利率暂停至2027年一季度的预测。\n- 结论：只有持续坚挺的数据（房价、销售率、二手成交量）才能打消投资者疑虑。\n\n**3/ \n\n[... middle omitted ...]\n\nkely weigh on sentiment for a while, and thus we expect the sector to face some near-term pressure. However, we remain constructive on the HK housing market as we believe it is more driven by \n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 08 Jun 2026 08:25 AM HKT\n\nDisseminated 08 Jun 2026 08:26 AM HKT"
  },
  {
    "id": "R028",
    "title": "Bernstein：Medicare Advantage的利润率正在触底，但市场低估了“公用事业化”的长期定价逻辑",
    "digest": "[wechat_article.md]\n# Bernstein：Medicare Advantage的利润率正在触底，但市场低估了“公用事业化”的长期定价逻辑\n\n市场对Medicare Advantage（MA）的定价，长期以来被一个经典叙事主导：这是一个高增长、高利润、且受政策风险扰动的周期性赛道。投资者习惯于将MA计划视为保险周期的放大器——费率高时利润爆发，费率低时利润崩塌。这份Bernstein的暑期教学系列报告，提供了一个比周期判断更值得关注的框架：MA正在经历结构性转型，其终局不是利润率的均值回归，而是向“公用事业型”市场的收敛。这意味着，当前市场对MA相关股票的估值，可能既低估了利润率修复的幅度，也误读了长期稳态利润率的水平。\n\n报告的核心判断是，MA行业利润率已经在2023-2025年触底，预计2026年将回升约1个百分点，此后每年以约0.5个百分点的速度温和扩张，直到2030年。这一判断的基础，并非政策红利或需求爆发，而是竞争退出、费率改善和行业定价纪律的回归。但比短期复苏更重要的，是Bernstein提出的长期图景：MA和Medicaid市场都将趋于“公用事业化”，最终由4-5家规模化玩家主导，MA的稳态利润率维持在2-3%之间。如果这一判断成立，那么当前市场对头部MA企业的估值折扣，可能恰恰提供了逆向布局的机会。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 利润率危机并非系统性问题，而是传统保险周期的必然产物\n\n理解MA利润率为何在2023-2025年遭遇重创，是判断后续走势的前提。Bernstein的分析提供了一个清晰的周期框架：2005-2015年间，MA市场收入增速高达15-20%，利润率稳定在5%左右。这一高回报吸引了大量资本涌入，竞争加剧直接压低了利润率，也为后续的费率冲击埋下了伏笔。\n\n当CMS在2024年和2025\n\n[... middle omitted ...]\n\n社群中继续深入这些议题，欢迎你带着自己的观察和问题参与讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美国医保体系正在经历结构性变化，Medicare Advantage（MA）成为核心战场。\n\n封面：MA市场拐点已至\n\n封面副标题：行业利润率正从底部回升\n\n最近投行研报深入拆解了美国Medicare Advantage市场，核心逻辑值得关注：\n\n1️⃣ 行业周期触底反弹\n过去几年MA利润率承压，本质是传统保险周期——2005-2015年行业增速15-20%、利润率5%左右，吸引大量竞争者涌入，最终导致利润率危机。预计2026年行业利润率将回升约1%，此后每年增长约0.5%，驱动因素包括竞争退出、费率改善、行业聚焦盈利。\n\n2️⃣ 增长放缓但趋势不变\nMA enrollment增速将从高位回落至4-5%。核心价值主张依然成立：用户享受更多补充福利，政府端结构性成本低于传统Medicare。长期看，MA将几乎覆盖整个Medicare市场。\n\n3️⃣ 市场结构走向“公用事业化”\n未来MA和Medicaid市场将趋于寡头格局，约4-5家规模化玩家主导，利润率维持在较低水平（Medicaid约1.5%，MA约2-3%）。目前UNH、HUM、CVS三家占据约55%市场份额。\n\n4️⃣ 三大变量值得跟踪\nGLP-1药物：\n\n[... middle omitted ...]\n\nere to register);\n\nInsurance cycle - We see the recent negative margins in MA as having been the result of a traditional insurance cycle driven by excessive competition. Revenue growth rates i\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R029",
    "title": "摩根斯坦利：ASCO数据揭示中国创新药进入“化疗增敏”价值重估期",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：ASCO数据揭示中国创新药进入“化疗增敏”价值重估期\n\n这不是又一轮“me-too”分子的数据更新。摩根斯坦利在ASCO 2026最后两天的核心观察指向一个更具结构性的判断：中国生物科技公司的竞争逻辑，正在从“能否做出同类最佳”转向“能否在特定化疗骨架之上，做出可证明的、有临床意义的增量”。这份报告最值得关注的，不是AK112或mesutoclax的单组数据有多漂亮，而是这些数据背后，一个被低估的估值驱动因子正在浮现——化疗联合疗法的风险收益比重构。\n\n市场此前对中国创新药的定价，高度集中在PD-1/VEGF双抗这类大单品预期上。但摩根斯坦利分析师Jack Lin团队在ASCO现场捕捉到的信号是：真正可能改变竞争格局的，不是单一靶点的突破，而是“化疗增敏剂”这一临床策略的系统性验证。如果这一策略被证实，将直接改写多个大适应症的标准治疗路径，并对现有IO（免疫肿瘤）疗法的市场地位形成实质性冲击。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AK112在SCLC的数据挑战了IO联合化疗的既有天花板，但样本构成的差异仍是关键变量\n\n摩根斯坦利重点分析了AK112联合脂质体伊立替康（lipo-iri）在2L SCLC中的数据。ORR 61.7%、mPFS 8.1个月、6个月PFS率69.1%，这些数字在与BNT327联合紫杉醇的IO经治人群对比中显得突出——后者ORR仅37.2%、mPFS 5.4个月、6个月PFS率46.1%。更重要的是，≥3级TRAE发生率AK112组为36.7%，显著低于对照组的78.6%。\n\n但报告没有止步于“AK112更好”这个表层结论。分析师做了一个关键的数据拆解：单独使用lipo-iri的RESILIENT研究中，ORR为44.1%、mPFS为4.0个月。这意味着化疗本身已\n\n[... middle omitted ...]\n\n的报告解读、原始数据图表，以及对这些未解问题的后续跟踪分析。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nASCO第三天：两个靶点数据炸裂\n\nAK112 + 脂质体伊立替康 vs 小细胞肺癌\n\n**AK112组合：ORR 61.7%，mPFS 8.1个月，6个月PFS率69.1%**\n**对比同类方案：ORR 37.2%，mPFS 5.4个月，6个月PFS率46.1%**\n\n数据差异很明显，但有个细节值得注意：AK112组里CFI＜90天的难治患者比例是36.7%，而对照方案是50%。这个基线差异可能会影响横向对比的可靠性。\n\n脂质体伊立替康单药的历史数据ORR 44.1%、mPFS 4.0个月，说明化疗本身建立了疗效底线，AK112的关键加分项是持久性——即使在化疗耐药人群里，mPFS也能到6.7个月。\n\n不过出血事件发生率20%（≥3级未单独披露），QoL数据也需要持续跟踪，这是风险收益比的核心变量。\n\n**Mesutoclax：MDS/AML双线开花**\n\nHR-MDS初治队列（n=10）：ORR 100%，IWG23 compCR 90%\n对比同类BCL-2抑制剂：ORR 64-74%，compCR约70%\n\nAML初治队列（n=44）：cCR 81.8%，MRD阴性率86.5%\n对比同类：CR/CRi \n\n[... middle omitted ...]\n\n64-74% / \\~70%; needs durability data after VERONA.  \nAML screens well on efficacy/safety: mesu cCR 81.8% / MRD-neg 86.5% vs sonro CR/CRi 67.1% / MRD-neg 35.4% + G3+ inf 50.6% / TLS 5%; lisa C\n\n[... middle omitted ...]\n\n Co. Ltd. (600216.SS)</td><td>E (02/28/2025)</td><td>Rmb12.17</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R030",
    "title": "Citi：AI供应链的瓶颈正在从GPU转移到PCB和铜箔基板",
    "digest": "[wechat_article.md]\n# Citi：AI供应链的瓶颈正在从GPU转移到PCB和铜箔基板\n\n市场对AI硬件产业链的关注，长期以来集中在GPU供给、CoWoS封装产能、以及HBM存储器的供需缺口上。但一份来自Citi近期台湾科技大会的调研纪要，揭示了一个正在发生的结构性变化：**AI服务器产业链的瓶颈，正在从先进封装和晶圆制造，向下游的PCB和铜箔基板（CCL）环节转移。** 这不是一个短期扰动，而是供给端投资节奏长期错配的结果。\n\nCiti分析师Jack Chen及其团队在2026年6月初的台湾科技大会上，与三家核心PCB和CCL厂商——金像电子（GCE）、台光电（EMC）和联茂电子（TUC）进行了深度交流。三家公司的反馈高度一致：AI需求强劲，产能扩张速度跟不上客户需求，涨价正在成为行业共识。这份报告的价值，在于它不只是给出了一个“景气向好”的判断，而是系统性地拆解了三个不同环节（PCB、CCL、上游材料）各自的供需格局、定价策略和竞争分化。\n\n以下是这份报告的核心洞察与延伸分析。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. PCB与CCL的产能扩张正在出现不可忽视的“速度差”\n\nCiti报告中最具结构性意义的判断，来自于EMC和TUC两家CCL厂商的共同观察：CCL行业的产能扩张速度，系统性落后于PCB行业的扩张速度。这意味着，即便PCB厂有能力建新厂、扩产线，它们也可能面临上游CCL供应不足的瓶颈。\n\n这个判断的逻辑链条是清晰的。PCB厂商如金像电子计划在2027、2028、2029年每年新建一座工厂，扩产意愿强烈。但CCL厂商的扩产节奏更为谨慎。EMC明确表示其未来产能扩张将主要集中在中国，因为“产能部署更高效、客户需求更充足”。TUC的泰国新厂则因设备交付延迟，营收贡献时间点从预期推迟到了2026年三季度末。\n\n这两组信息合\n\n[... middle omitted ...]\n\n行对AI供应链的后续调研，并分享更详细的图表分析和估值对比。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nCCL 产能跟不上，PCB 厂开始抢料了\n\nAI 需求太猛，CCL 供不应求\n\n最近某外资投行的台湾科技会议上，几家 PCB 和 CCL 大厂都透露了同一个信号：AI 需求太强劲，产能扩得再快也追不上客户要货的速度。\n\n1️⃣ CCL 紧缺成定局，涨价已成共识\nEMC 和 TUC 都提到，CCL 的新产能扩张速度明显慢于 PCB 厂，导致 CCL 供应持续吃紧。两家公司都明确表示会继续涨价，而且客户基本都接受了。GCE（金像电）也确认，客户对 PCB 涨价没有异议。\n\n2️⃣ GCE 在 ASIC 客户中抢到更多份额\nGCE 正在从现有 ASIC 客户那里拿到更多订单，同时有较大概率在 4Q26 开始支持另一家新 ASIC 客户。公司计划 2027-2029 年每年新建一座工厂，但管理层坦言：就算这样扩产，可能还是不够满足需求。\n\n3️⃣ 泰国厂成为新增长点\nGCE 泰国厂的月营收预计从 2Q26 的 6 亿新台币，快速攀升到 3Q26 的 13 亿新台币。AI 服务器产品将在 2H26 开始生产，随着产能利用率提升，盈利也会逐步改善。\n\n4️⃣ 材料端也有看点\nEMC 认为铜箔可能在 2H26/2027 出\n\n[... middle omitted ...]\n\nd currently customers all agreed with the PCB price hike as well. GCE now sees m/s gain in its existing ASIC customer and sees good chance to support another new ASIC customer from 4Q26 onward\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R031",
    "title": "Bernstein：市场低估了支付网络的“量价分离”能力",
    "digest": "[wechat_article.md]\n# Bernstein：市场低估了支付网络的“量价分离”能力\n\n全球支付市场正在进入一个微妙的分水岭。过去十年，现金数字化是行业增长的核心叙事，卡支付渗透率从47%攀升至64%，Visa和Mastercard的股价也在这条曲线上获得了丰厚回报。但一个尖锐的问题正在浮现：当美国卡渗透率已达72%，当亚洲市场增长放缓，当稳定币和即时支付不断制造噪音——现金数字化的跑道究竟还剩多少？\n\nBernstein刚刚发布了第12版全球支付预测模型。这份报告的结论，比表面看起来要复杂得多。它没有简单地回答“增长还有多少”，而是揭示了一个更关键的判断：**支付网络的价值增长，正在从“量”的扩张转向“质”的变现。** 那些只盯着卡交易量增速放缓的投资者，很可能低估了网络效应在交易结构、增值服务和新兴流量的二次放大作用。\n\n我们仔细拆解了这份长达数十页的研报，提炼出五个核心洞察。它们不仅关乎Visa和Mastercard的投资逻辑，更指向整个支付产业链的定价权迁移。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 卡交易量增速确实在放缓，但交易笔数的增长更具韧性\n\nBernstein预测，2025-2030年全球卡交易量（C2B purchase volume）的复合年增长率约为8%（恒定汇率），低于2022-2025年的9%和2019-2022年的11%。减速的主要驱动力来自两个方向：美国市场的高渗透率（72%）导致增量空间收窄，以及亚太地区因本土支付生态的崛起而出现结构性放缓。\n\n但这里有一个容易被忽视的细节。当衡量标准从交易金额切换到交易笔数时，增长曲线明显更陡峭：Bernstein预测全球交易笔数在2025-2030年的复合增长率约为9%，仅比2022-2025年的10%略有下降。原因在于，卡渗透率在笔数维度上仍然偏低——很多低\n\n[... middle omitted ...]\n\n出现在任何一份公开研报里，但会在持续的讨论和碰撞中逐渐清晰。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球刷卡增长，还能跑多久？\n\n现金数字化还有空间吗？\n\n未来五年，刷卡量增速可能放缓，但别急着悲观\n\n刚读完某外资投行最新全球支付研报，第12版年度预测模型，干货满满，分享几个核心发现👇\n\n1️⃣ 全球刷卡量增速正在“降档”\n研报预测2025-2030年，全球卡交易额年复合增速约8%（恒定汇率），低于2022-2025年的9%。核心原因：美国渗透率已高达72%（10年前才58%），亚洲市场增长放缓。美国未来5年增速预计仅5-6%。\n\n2️⃣ 但交易笔数增速更高\n全球交易笔数预计2025-2030年增长9%（2022-2025年为10%）。为什么？因为渗透率按笔数算比按金额算更低。Visa和万事达超过1/3的收入来自交易笔数，笔数增速通常快于金额增速。\n\n3️⃣ 现金/支票存量还有11万亿美元\n全球C2B支付市场约40万亿美元，目前卡片渗透率64%（2019年仅47%）。研报预计到2030年渗透率可达71%，意味着还有约11万亿美元的现金/支票待转化。欧洲、亚太、拉美是主要机会区域。\n\n4️⃣ 新增长引擎已出现\n研报指出：代币化、增值服务渗透、新支付流（如稳定币）是未来收入增长的关键。即使卡交易额增速放缓，结合\n\n[... middle omitted ...]\n\n payments forecast model. A lot has changed in the last 10+ years - U.S. is now highly penetrated by cards (72% vs. 58% ten years ago), local payment methods have gained traction (e.g., in Asi\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R032",
    "title": "摩根斯坦利：亚洲市场真正的超额收益来自结构性的“非共识定价”",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：亚洲市场真正的超额收益来自结构性的“非共识定价”\n\n当多数投资者仍在为宏观数据的短期波动焦虑时，一份来自摩根斯坦利的最新研报揭示了一个更值得关注的事实：在过去一年里，其“三个可操作想法”组合累计获得了超过9,300个基点的相对超额收益，平均12个月总回报率达到16.0%，相对基准的超额回报为10.6%。这些数字并非来自某个单一主题的押注，而是来自对亚洲市场三类结构性力量的持续识别。\n\n这份报告的核心判断是：当前亚洲市场的超额收益机会，正从依赖宏观贝塔转向寻找微观层面的“非共识定价”。无论是日本光通信与水冷模块的爆发、澳大利亚住房信贷周期的拐点，还是印度能源安全政策的重塑，这些机会的共同特征在于——市场共识尚未充分定价供给端的结构性变化。\n\n以下是我们从这份研报中提炼的三个关键洞察，以及它们对投资者观察框架的启示。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 古河电工的利润新高路径揭示了一个被低估的产业逻辑：光通信与水冷模块的“双轮驱动”正在改写日本电子材料公司的盈利天花板\n\n摩根斯坦利对古河电工（5801.T）给出“超配”评级，并将其目标价上调至66,000日元。支撑这一判断的核心逻辑并非公司现有的光纤业务复苏，而是两个正在加速的结构性变量：光通信产品的需求升级，以及水冷模块在数据中心散热领域的渗透加速。\n\n报告明确指出，古河电工有望实现“新的创纪录利润且增长强劲”。这意味着，市场此前对这家公司的估值框架仍停留在传统光纤周期上，而忽略了其在AI算力基础设施配套中的新角色。水冷模块作为高功率数据中心散热的关键组件，其需求增速正在显著超越传统风冷方案。如果这一趋势持续，古河电工的盈利中枢将上移至历史高位之上。\n\n这一判断的隐含含义更为重要：在亚洲电子材料领域，那些能够同时受益于“光通信升级”与“散热\n\n[... middle omitted ...]\n\n、竞争格局以及潜在的风险因素，帮助您建立自己的投资决策框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n亚洲研报挖出3个核心逻辑\n\n三个方向，三个故事\n\n光通信+水冷双驱动，日本电线的盈利新高可能快到了\n\n1️⃣ Furukawa Electric（5801.T）\n光通信模块和水冷模块销售增速加快，研报认为盈利有望创历史新高。\n目标价上调至66000日元，评级维持OW。\n\n2️⃣ Westpac Banking（WBC.AX）\n澳洲住房和按揭市场前景转弱，研报下调了盈利预测和目标价。\n行业观点维持谨慎，评级为UW。\n\n3️⃣ Hindustan Petroleum（HPCL.NS）\n能源安全成为政策重心，印度燃料零售商受益于能源供应改善。\nHPCL被列为关键标的，评级OW。\n\n📌 投研笔记\n- 日本光通信产业链需求回暖，水冷方案在数据中心渗透率提升\n- 澳洲银行股受利率和房价双重压力，短期景气度偏弱\n- 印度能源政策超预期，燃料零售板块获得政策红利\n\n这三个方向分别对应科技、金融、能源，逻辑各自独立，可以分开研究。\n\n欢迎一起讨论你对哪个方向更感兴趣～\n\n#学习笔记\n\n[source_mineru.md]\n## Asia | Asia Pacific\n\n# Three Actionable Ideas\n\nFur\n\n[... middle omitted ...]\n\nolicymakers are acting in ways that surprised consensus. Indian fuel retailers are most levered plays to improving energy supplies beyond the oil shock. HPCL key pick.\n\n## Links to reports:\n\nF\n\n[... middle omitted ...]\n\narantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n© 2026 MS"
  },
  {
    "id": "R033",
    "title": "NOM：印度消费复苏并非全面开花，真正的结构性机会在组织化企业的份额掠夺",
    "digest": "[wechat_article.md]\n# NOM：印度消费复苏并非全面开花，真正的结构性机会在组织化企业的份额掠夺\n\n印度消费股在经历了一段时间的沉寂后，似乎正迎来一波新的关注。但这份NOM关于印度4QFY26（2026年第一季度）消费品行业的深度研报，揭示了一个比“复苏”二字更为复杂的图景。市场可能正在定价需求的回暖，但真正被低估的，是供给端正在发生的结构性洗牌。\n\n这份报告的核心判断是：印度消费行业的增长驱动力正在从“普惠式复苏”切换为“组织化企业的份额掠夺”。GST降税带来的短期价格红利固然重要，但更关键的长期变量是，在地缘政治引发的成本通胀和渠道变革中，拥有品牌、规模和供应链优势的组织化企业，正在系统性地从非组织化（unorganized）玩家和地方性品牌手中夺取市场份额。这并非一场所有船只都会水涨船高的行情，而是一场赢家通吃的淘汰赛。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 数据印证：组织化企业正在以两倍于行业的速度增长，这是最值得关注的信号\n\n研报中最具说服力的数据并非销售增速，而是组织化部门与非组织化部门之间的增速裂口。报告明确指出，虽然印度快速消费品（FMCG）行业的整体销量增长环比有所放缓，但组织化企业的销量增长却创下了过去四年来的最高纪录。在必需品（Staples）领域，组织化企业的4Q销量增速达到9%，是其过去八个季度均值（6.7%）的1.35倍；在食品领域，这一增速更是高达14%，远超行业平均水平。\n\n这意味着什么？这意味着在整体需求并未出现井喷式爆发的背景下，组织化企业正在以一种前所未有的速度“吃掉”非组织化玩家的市场。报告中的图表（Fig. 7和Fig. 17）清晰地展示了这一剪刀差。这并非简单的周期性回暖，而是一个结构性的市场份额再分配过程。对于投资者而言，关注的重点应从“消费行业好不好”转向“谁在吃谁的份额”。\n\n[... middle omitted ...]\n\n全展开的图表，探讨哪些公司最有可能在未来的份额争夺战中胜出。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n印度消费复苏：刚需品增长提速\n\n刚需品回暖信号明显\n\n刚需品（Staples）4Q营收同比增长10.5%，高于过去8季均值6.7%。组织化玩家增速（+9%）创4年新高，远超非组织化渠道。主要受益于GST税率下调带来的价格传导。\n\n食品与日化分化加剧\n1. 食品板块（Foods）：营收增速16%，组织化玩家量增14%。雀巢领跑，非组织化渠道份额持续流失。定价增长仅2%，但季末已开始提价至中个位数。\n2. 日化板块（HPC）：营收增速7.4%保持稳定，组织化玩家量增6.3%（均值3.2%）。但发油企业降价导致定价增长放缓至1.1%。\n\n利润端：结构性改善与短期压力并存\n- 刚需品毛利率区间波动，食品企业扩张被日化收缩抵消\n- OPM靠成本节约和稳定广告支出维持\n- 食品毛利率同比+55bp，OPM同比+86bp\n- 日化毛利率同比-70bp，OPM仅持平\n\n城乡分化：农村增速放缓\n- 农村量增从3Q开始降温，城乡差距收窄\n- 后续面临厄尔尼诺、季风偏弱、产品涨价三重压力\n- 但水库水位充足+粮食库存充裕可部分对冲\n\n投研观察\n1. 量价两阶段：GST降价推动量增→涨价接力支撑营收\n2. 组织化玩家更抗压：涨价能力弱\n\n[... middle omitted ...]\n\nd players grew faster than unorganized players. We note that almost all the staple companies under our coverage, except for Godrej Consumer, witnessed either sequentially stable or improved vo\n\n[... middle omitted ...]\n\nisclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Financial Advisory and Securities (India) Private Limited, India. All rights reserved."
  },
  {
    "id": "R034",
    "title": "NOM：韩国正极材料三巨头的分化，才是理解全球电池供应链重构的真正线索",
    "digest": "[wechat_article.md]\n# NOM：韩国正极材料三巨头的分化，才是理解全球电池供应链重构的真正线索\n\n市场对电池材料行业的关注，长期集中在“谁拿到了多少订单”和“产能扩张速度”这两个维度上。但NOM在2026年6月新加坡亚洲投资论坛上与韩国三大正极材料公司——LG化学、L&F和Ecopro BM——的交流揭示了一个更关键的信号：这三家公司在战略路径上出现了根本性的分化，而这种分化背后，是对全球电池供应链未来十年格局的不同押注。这份报告真正值得看的判断，不是某一家公司的出货量预测，而是这三家公司正在用完全不同的方式回答同一个问题：在欧美本土化生产、LFP与高镍路线并存、中国供应链主导地位被挑战的背景下，韩国正极材料企业的竞争优势究竟从哪里来？\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. Ecopro BM的战略锚点是欧洲高镍需求，但真正的胜负手在印尼镍矿整合\n\nEcopro BM是目前三家之中战略路径最清晰的一家。NOM报告显示，该公司现有正极材料产能244万吨，其中54万吨位于匈牙利，第一条产线计划于2026年6月投产，第二条在2026年下半年启动。更重要的是，Ecopro BM正将第三条产线转换为NCM生产，目标客户是欧洲的非韩国电池工厂。\n\n这一布局的逻辑非常清晰。欧洲正在重新启动电动汽车消费补贴，英国和德国的政策信号已经明确，同时监管要求供应链本土化。Ecopro BM的高镍正极产品组合——而非中镍或LFP——恰好切中了欧洲市场对续航里程和能量密度的优先需求。但这里有一个容易被忽略的关键点：Ecopro BM的竞争优势并不完全来自其产品本身，而来自Ecopro集团在印尼镍冶炼厂中约10%的持股，该冶炼厂总产能为15万吨，集团还在评估二期投资。\n\n这意味着什么？Ecopro BM的原材料成本结构将显著优于那些依赖外部镍供应的竞争对\n\n[... middle omitted ...]\n\n风险因素的完整清单。这些内容对于做出独立的投资判断至关重要。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n韩国正极三兄弟，谁在打明牌？\n\n三家韩国正极厂，三种打法\n\n最近某外资投行在新加坡办了场投资论坛，聊了韩国三家正极材料厂——Ecopro BM、L&F、LG Chem。它们都在往欧美跑，但策略完全不同。\n\n1️⃣ **Ecopro BM：押注欧洲，死磕高镍**\n- 匈牙利工厂6月投产，首条线已启动，第二条线今年下半年跟上。\n- 第三条线打算转产NCM，专供欧洲非韩国电池厂。\n- 欧洲补贴又回来了（英/德），本地化要求也推着供应链落地。\n- 集团还在印尼搞镍冶炼，持股约10%，二期在评估中。\n- 短期重点：匈牙利爬坡、2027年固态正极、印尼镍扩张——不做LFP。\n\n2️⃣ **L&F：韩国首个LFP正极，2026年3季度见**\n- 2026年出货量预计同比增19%到8万吨，其中约85%收入来自LG新能源（终端是特斯拉）。\n- 韩国LFP产能6万吨，3季度先跑3万吨，剩下1H27跑。\n- 初始客户是三星SDI的美国ESS业务（3月签了长单）。\n- LFP正极ASP假设11美元/kg，但盈利还是高镍更香。\n- 技术方向：无前驱体LFP（跳过混合环节，直接煅烧），还在做钠电池。\n\n3️⃣ **LG Chem：出货回\n\n[... middle omitted ...]\n\nxpected to start in 2H26E, according to the company. Meanwhile, EBM is working to convert the third line into NCM (nickel cobalt manganese) production with an aim to supply to non-Korea batter\n\n[... middle omitted ...]\n\n upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Financial Investment (Korea) Co., Ltd., Korea. All rights reserved."
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "Figure 1",
    "context": "Capital controls undermine RMB internationalization? — Curbs on illicit cross-border flows need not undermine the \"golden window\" for RMB internationalization, in our view. Flows associated with RMB internationalization run through official channels, including"
  },
  {
    "figure_id": "F002",
    "report_id": "R001",
    "label": "Figure 3",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 3. There is little RMB depreciation pressure now with FX settlement..."
  },
  {
    "figure_id": "F003",
    "report_id": "R001",
    "label": "Figure 5",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 5. The macro impact from this round of outbound investment tightening looks limited Potential Inflows from Mainland China to Hong Kong"
  },
  {
    "figure_id": "F004",
    "report_id": "R001",
    "label": "Figure 2",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 2. The capital outflow pressure could be smaller compared with the episode in 2015"
  },
  {
    "figure_id": "F005",
    "report_id": "R001",
    "label": "Figure 4",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 4. ... and exporters' conversion ratio both rising"
  },
  {
    "figure_id": "F006",
    "report_id": "R001",
    "label": "Figure 6",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 6. China's ODI could be on a structural upward trend as Chinese corporates search for growth engines"
  },
  {
    "figure_id": "F007",
    "report_id": "R001",
    "label": "Figure 7",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 7. Taxation concerns could follow the tightening on portfolio flows"
  },
  {
    "figure_id": "F008",
    "report_id": "R001",
    "label": "Figure 8",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 8. The expansion of official channels is one thing to watch, with Stock Connect showing need to diversify"
  },
  {
    "figure_id": "F009",
    "report_id": "R002",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Global market performance Price Return (USD, %)"
  },
  {
    "figure_id": "F010",
    "report_id": "R002",
    "label": "Exhibit 2",
    "context": "Exhibit 2: World equity indices USD, indexed price performance"
  },
  {
    "figure_id": "F011",
    "report_id": "R002",
    "label": "Exhibit 3",
    "context": "Exhibit 3: MSCI AC World sector performance Price Return (USD, %)"
  },
  {
    "figure_id": "F012",
    "report_id": "R002",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Cross-asset performance"
  },
  {
    "figure_id": "F013",
    "report_id": "R002",
    "label": "Exhibit 5",
    "context": "Exhibit 5: GDP growth, % yoy: GS vs. consensus \\* Bloomberg country and GS aggregate consensus Exhibit 7: GS top-down vs. consensus bottom-up estimates of 2026 EPS growth"
  },
  {
    "figure_id": "F014",
    "report_id": "R002",
    "label": "Exhibit 6",
    "context": "Exhibit 6: GS Macro 3-, 6- and 12-month forecasts Exhibit 8: GS top-down vs. consensus bottom-up estimates of 2027 EPS growth"
  },
  {
    "figure_id": "F015",
    "report_id": "R002",
    "label": "Exhibit 9",
    "context": "Exhibit 9: GS Bull/Bear Market Indicator (GSBLBR)"
  },
  {
    "figure_id": "F016",
    "report_id": "R002",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Risk Appetite Indicator (GSRAII)"
  },
  {
    "figure_id": "F017",
    "report_id": "R002",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Percentile of sentiment indicators Data since 2007"
  },
  {
    "figure_id": "F018",
    "report_id": "R002",
    "label": "Exhibit 16",
    "context": "Exhibit 16: 12m trailing return contribution 12m trailing return in local currency"
  },
  {
    "figure_id": "F019",
    "report_id": "R002",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Sales growth, EPS growth and net margins Consensus estimates Exhibit 17: MSCI AC World 12m trailing return contribution by sector/style 12m trailing return in USD"
  },
  {
    "figure_id": "F020",
    "report_id": "R002",
    "label": "Exhibit 19",
    "context": "Exhibit 19: MSCI AC World EPS Consensus estimates in USD"
  },
  {
    "figure_id": "F021",
    "report_id": "R002",
    "label": "Exhibit 20",
    "context": "Exhibit 20: 2026 EPS revisions Indexed to 100. Local currency"
  },
  {
    "figure_id": "F022",
    "report_id": "R002",
    "label": "Exhibit 22",
    "context": "Exhibit 22: 3-month EPS revision MSCI AC World sectors and Global Regions. Local currency"
  },
  {
    "figure_id": "F023",
    "report_id": "R002",
    "label": "Exhibit 21",
    "context": "Exhibit 21: 2026 Earnings Sentiment (nb upgrades - nb downgrades) / nb estimates over the past month"
  },
  {
    "figure_id": "F024",
    "report_id": "R002",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Year-to-date EPS revisions MSCI AC World sectors and Global Regions. Local currency"
  },
  {
    "figure_id": "F025",
    "report_id": "R002",
    "label": "Exhibit 24",
    "context": "Exhibit 24: 12m and 24m fwd MSCI AC World stock valuation 12m and 24m fwd P/E"
  },
  {
    "figure_id": "F026",
    "report_id": "R002",
    "label": "Exhibit 25",
    "context": "Exhibit 25: Global market implied ERP (%)"
  },
  {
    "figure_id": "F027",
    "report_id": "R002",
    "label": "Exhibit 26",
    "context": "Exhibit 26: MSCI Regions valuations 12-month forward P/Es relative to the last 20 years - STOXX 600 P/E for Europe"
  },
  {
    "figure_id": "F028",
    "report_id": "R002",
    "label": "Exhibit 27",
    "context": "Exhibit 27: MSCI World sector/style valuations 12-month forward P/Es relative to the last 20 years"
  },
  {
    "figure_id": "F029",
    "report_id": "R002",
    "label": "Exhibit 28",
    "context": "Exhibit 28: Value vs. Growth MSCI Indices relative price return (USD)"
  },
  {
    "figure_id": "F030",
    "report_id": "R002",
    "label": "Exhibit 29",
    "context": "Exhibit 29: Small-cap vs. Large-cap US: MSCI USA Small vs. MSCI USA Large; Europe: MSCI Europe Small vs. MSCI Europe Large; MSCI Japan Small vs. MSCI Japan Large; MSCI EM Small vs. MSCI EM Large"
  },
  {
    "figure_id": "F031",
    "report_id": "R002",
    "label": "Exhibit 30",
    "context": "Exhibit 30: Cyclicals vs. Defensives MSCI Indices relative price return (USD)"
  },
  {
    "figure_id": "F032",
    "report_id": "R002",
    "label": "Exhibit 31",
    "context": "Exhibit 31: Momentum vs. Market MSCI Momentum Indices relative price return (USD)"
  },
  {
    "figure_id": "F033",
    "report_id": "R002",
    "label": "Exhibit 32",
    "context": "Exhibit 32: Value vs. Growth 12m fwd P/E Premium (or Discount)"
  },
  {
    "figure_id": "F034",
    "report_id": "R002",
    "label": "Exhibit 33",
    "context": "Exhibit 33: Small vs. Large 12m fwd P/E Premium (or Discount)"
  },
  {
    "figure_id": "F035",
    "report_id": "R002",
    "label": "Exhibit 34",
    "context": "Exhibit 34: Cyclicals vs. Defensives 12m fwd P/E Premium (or Discount)"
  },
  {
    "figure_id": "F036",
    "report_id": "R002",
    "label": "Exhibit 35",
    "context": "Exhibit 35: Momentum vs. Market 12m fwd P/E Premium (or Discount)"
  },
  {
    "figure_id": "F037",
    "report_id": "R002",
    "label": "Exhibit 36",
    "context": "Exhibit 36: Index sector composition Exhibit 38: Geographical Sales Exposure MSCI Indices. See our Portfolio Passport 2024."
  },
  {
    "figure_id": "F038",
    "report_id": "R002",
    "label": "Exhibit 39",
    "context": "Exhibit 39: Country Composition MSCI AC World Index"
  },
  {
    "figure_id": "F039",
    "report_id": "R002",
    "label": "Exhibit 40",
    "context": "Exhibit 40: Performance of equities, bonds and commodities Indexed USD total returns, Equities refer to MSCI AC World, Commodities refer to S&P GSCI® & Bonds refer to US 10y Govt. bonds"
  },
  {
    "figure_id": "F040",
    "report_id": "R002",
    "label": "Exhibit 41",
    "context": "Exhibit 41: 3m rolling equity/bond correlation of weekly returns S&P 500 vs. US 10y Index; EURO STOXX 50 vs. Germany 10y Index; Topix vs. Japan 10y Index; MSCI EM vs. US 10y Index"
  },
  {
    "figure_id": "F041",
    "report_id": "R002",
    "label": "Exhibit 42",
    "context": "Exhibit 42: 3m correlation of weekly returns with GSCI Total Return Index Correlation vs. GSCI Commodities Total Return Index"
  },
  {
    "figure_id": "F042",
    "report_id": "R002",
    "label": "Exhibit 43",
    "context": "Exhibit 43: 3m rolling equity/FX correlation of weekly returns S&P 500 vs. GS USD TWI; EURO STOXX 50 vs. EUR/USD; Topix vs. JPY/USD; MSCI EM vs. GS USD TWI"
  },
  {
    "figure_id": "F043",
    "report_id": "R002",
    "label": "Exhibit 44",
    "context": "Exhibit 44: Monthly flows from Global investors into DM and EM equity funds In USD bn."
  },
  {
    "figure_id": "F044",
    "report_id": "R002",
    "label": "Exhibit 45",
    "context": "Exhibit 45: Cumulative flows into equity by regions Monthly flows, USD bn. EPFR Country Flows (weekly data for current month)."
  },
  {
    "figure_id": "F045",
    "report_id": "R002",
    "label": "Exhibit 46",
    "context": "Exhibit 46: Calendarised flows from Global investors into DM and EM equity funds"
  },
  {
    "figure_id": "F046",
    "report_id": "R002",
    "label": "Exhibit 47",
    "context": "Exhibit 47: Cumulative flows from Global investors into DM and EM funds Active and Passive funds. Monthly flows, USD bn. EPFR Country Flows (weekly data for current month)"
  },
  {
    "figure_id": "F047",
    "report_id": "R002",
    "label": "Exhibit 48",
    "context": "Exhibit 48: EM vs. DM performance Relative price performance, indexed to 100 from 1 year ago"
  },
  {
    "figure_id": "F048",
    "report_id": "R002",
    "label": "Exhibit 49",
    "context": "Exhibit 49: 2026 earnings sentiment % for MSCI The World and EM Earnings sentiment = (upgrades - downgrades) / total estimates on all stocks"
  },
  {
    "figure_id": "F049",
    "report_id": "R002",
    "label": "Exhibit 50",
    "context": "Exhibit 50: EM vs. DM valuation 12-month forward P/E Premium (Discount)"
  },
  {
    "figure_id": "F050",
    "report_id": "R002",
    "label": "Exhibit 51",
    "context": "Exhibit 51: EM vs. DM Cumulative flows (% Total Net Assets) Monthly flows, EPFR Country Flows (weekly data for current month)."
  },
  {
    "figure_id": "F051",
    "report_id": "R002",
    "label": "Exhibit 52",
    "context": "Exhibit 52: Implied volatility of 3-month atms"
  },
  {
    "figure_id": "F052",
    "report_id": "R002",
    "label": "Exhibit 53",
    "context": "Exhibit 53: 3-month normalised skew"
  },
  {
    "figure_id": "F053",
    "report_id": "R002",
    "label": "Exhibit 54",
    "context": "Exhibit 54: 2026 dividend markets, rebased to 100"
  },
  {
    "figure_id": "F054",
    "report_id": "R002",
    "label": "Exhibit 55",
    "context": "Exhibit 55: 2026 implied dividend yield"
  },
  {
    "figure_id": "F055",
    "report_id": "R003",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Our US FCI Tightened Back to Its Pre-War Level Following Better Than Expected Employment Data Last Friday"
  },
  {
    "figure_id": "F056",
    "report_id": "R003",
    "label": "Exhibit 2",
    "context": "Exhibit 2: The Global ex Russia FCI Tightened by +3.3bps Last Week Primarily on Equities"
  },
  {
    "figure_id": "F057",
    "report_id": "R003",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Higher 2026 Growth in India Change in GS GDP Forecast in 2026"
  },
  {
    "figure_id": "F058",
    "report_id": "R003",
    "label": "Exhibit 4",
    "context": "Exhibit 5: Our Global CAI Remains Above Potential"
  },
  {
    "figure_id": "F059",
    "report_id": "R003",
    "label": "Exhibit 6",
    "context": "Exhibit 6: GS Wage Trackers and Inflation Measures"
  },
  {
    "figure_id": "F060",
    "report_id": "R003",
    "label": "Exhibit 7",
    "context": "Exhibit 7: GS Jobs-Workers Gaps ## Detailed Indicators Update ## Financial Conditions Index (FCI) Exhibit 8: GS Global ex Russia FCI Level (Left) and Weekly Change With Contributions (Right)"
  },
  {
    "figure_id": "F061",
    "report_id": "R003",
    "label": "Exhibit 8",
    "context": "Exhibit 8: GS Global ex Russia FCI Level (Left) and Weekly Change With Contributions (Right) Exhibit 9: GS Global FCI Level (Left) and Weekly Change With Contributions (Right)"
  },
  {
    "figure_id": "F062",
    "report_id": "R003",
    "label": "Exhibit 8",
    "context": "Exhibit 8: GS Global ex Russia FCI Level (Left) and Weekly Change With Contributions (Right) Exhibit 9: GS Global FCI Level (Left) and Weekly Change With Contributions (Right)"
  },
  {
    "figure_id": "F063",
    "report_id": "R003",
    "label": "Exhibit 10",
    "context": "Exhibit 10: GS US FCI Level (Left) and Weekly Change With Contributions (Right)"
  },
  {
    "figure_id": "F064",
    "report_id": "R003",
    "label": "Exhibit 11",
    "context": "Exhibit 11: GS Euro Area FCI Level (Left) and Weekly Change With Contributions (Right)"
  },
  {
    "figure_id": "F065",
    "report_id": "R003",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Weekly Change in FCI Across Countries Weekly Change in GS FCI Basis points"
  },
  {
    "figure_id": "F066",
    "report_id": "R003",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Year-Over-Year Change in FCI Across Countries Yearly Change in GS FCI Basis points"
  },
  {
    "figure_id": "F067",
    "report_id": "R003",
    "label": "Exhibit 14",
    "context": "Exhibit 14: FCI Impulses Over the Next 4 Quarters (Left) and in the Euro Area, UK, and US (Right)"
  },
  {
    "figure_id": "F068",
    "report_id": "R003",
    "label": "Exhibit 15",
    "context": "Exhibit 15: FCI Impulses in the US, Euro Area, Japan, and UK"
  },
  {
    "figure_id": "F069",
    "report_id": "R003",
    "label": "Exhibit 16",
    "context": "Exhibit 16: CAI Aggregates"
  },
  {
    "figure_id": "F070",
    "report_id": "R003",
    "label": "Exhibit 17",
    "context": "Exhibit 17: CAI Heatmap CAI in countries with 0% of data released is forecasted. CAI aggregates for Global, Developed Markets, and Emerging Markets are GDP-weighted using market FX country weights. Exhibit 18: CAIs for Large DMs and"
  },
  {
    "figure_id": "F071",
    "report_id": "R003",
    "label": "Exhibit 19",
    "context": "Exhibit 19: GS MAP Surprise Index"
  },
  {
    "figure_id": "F072",
    "report_id": "R003",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Latest GS MAP Surprise Index GS MAP Surprise Index"
  },
  {
    "figure_id": "F073",
    "report_id": "R003",
    "label": "Exhibit 21",
    "context": "Exhibit 21: GS Trimmed Core Inflation ## Wage Trackers Exhibit 22: GS Wage Trackers \\*Australian recession shading. \\*Sweden recession shading."
  },
  {
    "figure_id": "F074",
    "report_id": "R003",
    "label": "Exhibit 21",
    "context": "Exhibit 21: GS Trimmed Core Inflation ## Wage Trackers Exhibit 22: GS Wage Trackers \\*Australian recession shading. \\*Sweden recession shading. Exhibit 23: GS Sequential Wage Trackers GS Sequential Wage Trackers"
  },
  {
    "figure_id": "F075",
    "report_id": "R003",
    "label": "Exhibit 22",
    "context": "Exhibit 22: GS Wage Trackers \\*Australian recession shading. \\*Sweden recession shading. Exhibit 23: GS Sequential Wage Trackers GS Sequential Wage Trackers"
  },
  {
    "figure_id": "F076",
    "report_id": "R003",
    "label": "Exhibit 24",
    "context": "Exhibit 24: GS Jobs-Workers Gaps Exhibit 25: Wage Survey Leading Indicators"
  },
  {
    "figure_id": "F077",
    "report_id": "R003",
    "label": "Exhibit 24",
    "context": "Exhibit 24: GS Jobs-Workers Gaps Exhibit 25: Wage Survey Leading Indicators"
  },
  {
    "figure_id": "F078",
    "report_id": "R003",
    "label": "Exhibit 26",
    "context": "Exhibit 26: Top-Down Fiscal Impulses Over the Next 4 Quarters (Left) and in the Euro Area, UK, and US (Right) Effect of Fiscal Policy on Real GDP Growth (3 Quarter Centered Moving Average)"
  },
  {
    "figure_id": "F079",
    "report_id": "R003",
    "label": "Exhibit 27",
    "context": "Exhibit 27: Top-Down Fiscal Impulses in the US, Euro Area, China, and UK Effect of Fiscal Policy on Real GDP Growth (3 Quarter Centered Moving Average)"
  },
  {
    "figure_id": "F080",
    "report_id": "R003",
    "label": "Exhibit 28",
    "context": "Exhibit 28: Latest Short-Run Utilization Scores Exhibit 29: Short-Run Utilization Scores Exhibit 30: Change in GS 2026 Inflation Forecasts"
  },
  {
    "figure_id": "F081",
    "report_id": "R003",
    "label": "Exhibit 29",
    "context": "Exhibit 29: Short-Run Utilization Scores Exhibit 30: Change in GS 2026 Inflation Forecasts"
  },
  {
    "figure_id": "F082",
    "report_id": "R003",
    "label": "Exhibit 31",
    "context": "Exhibit 31: Change in GS 2027 Inflation Forecasts Change in GS Inflation Forecast (Q4/Q4) in 2027 (Since 60 Days Ago)"
  },
  {
    "figure_id": "F083",
    "report_id": "R003",
    "label": "Exhibit 32",
    "context": "Exhibit 32: Change in GS 2026 GDP Forecasts Change in GS GDP Forecast in 2026"
  },
  {
    "figure_id": "F084",
    "report_id": "R003",
    "label": "Exhibit 33",
    "context": "Exhibit 33: Change in GS 2027 GDP Forecasts Change in GS GDP Forecast in 2027"
  },
  {
    "figure_id": "F085",
    "report_id": "R003",
    "label": "Exhibit 34",
    "context": "Exhibit 34: GS 2026 Global GDP Forecasts vs. Other Forecasters"
  },
  {
    "figure_id": "F086",
    "report_id": "R003",
    "label": "Exhibit 35",
    "context": "Exhibit 35: GS 2027 Global GDP Forecasts vs. Other Forecasters"
  },
  {
    "figure_id": "F087",
    "report_id": "R004",
    "label": "Figure 5",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 5. Luxury Top Brands, Total Luxury Brands, Total Luxury Market, Beauty/cosmetics and Sport brands/retailers – Monthly absolute credit card spend, 2019–2026 (US\\$ in millions)"
  },
  {
    "figure_id": "F088",
    "report_id": "R004",
    "label": "Figure 6",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 6. Luxury Top Brands, Total Luxury Brands, Total Luxury Market, Sport brands/retailers and Beauty/cosmetics – Monthly absolute credit card spend, 12M rolling average, 2019–2026 (US\\$ "
  },
  {
    "figure_id": "F089",
    "report_id": "R004",
    "label": "Figure 7",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 7. US credit card monthly spend for Luxury, Sport brands/retailers, and Beauty/cosmetics categories, 2022–2026 (YoY % chg)"
  },
  {
    "figure_id": "F090",
    "report_id": "R004",
    "label": "Figure 8",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 8. US credit card monthly spend for Luxury, Sport brands/retailers, and Beauty/cosmetics categories, 2022–2026 (2Y stack % chg)"
  },
  {
    "figure_id": "F091",
    "report_id": "R004",
    "label": "Figure 9",
    "context": "## US spend dashboards for Luxury, Sporting Goods, and Beauty In the following pages, we provide the detailed dashboards and analysis for the 8 sub-categories we track as well as their recently created derivative baskets (grey background). Figure 9. Luxury Lea"
  },
  {
    "figure_id": "F092",
    "report_id": "R004",
    "label": "Figure 10",
    "context": "Figure 10. Luxury RTW – Monthly US credit card spend dashboard Average spend per individual customer and Number of Individual customers - YoY % chg"
  },
  {
    "figure_id": "F093",
    "report_id": "R004",
    "label": "Figure 11",
    "context": "Figure 11. Luxury Jewellery – Monthly US credit card spend dashboard Average spend per individual customer and Number of Individual customers - YoY % chg"
  },
  {
    "figure_id": "F094",
    "report_id": "R004",
    "label": "Figure 12",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 12. Luxury Watch Brands & Retailers – Monthly US credit card spend dashboard Average spend per individual customer and Number of Individual customers - YoY % chg"
  },
  {
    "figure_id": "F095",
    "report_id": "R004",
    "label": "Figure 13",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 13. High-End Department Stores & Online Luxury platforms – Monthly US credit card spend dashboard"
  },
  {
    "figure_id": "F096",
    "report_id": "R004",
    "label": "Figure 15",
    "context": "Figure 15. Online Luxury & Luxury Resale – Monthly US credit card spend dashboard"
  },
  {
    "figure_id": "F097",
    "report_id": "R004",
    "label": "Figure 16",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 16. Online Off-Price & Luxury Resale platforms – Monthly US credit card spend dashboard"
  },
  {
    "figure_id": "F098",
    "report_id": "R004",
    "label": "Figure 17",
    "context": "Figure 17. Sport brands and retailers – Monthly US credit card spend dashboard Average spend per individual customer and Number of Individual customers - YoY % chg"
  },
  {
    "figure_id": "F099",
    "report_id": "R004",
    "label": "Figure 18",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 18. Athletic Apparel & Equipment Stores – Monthly US credit card spend dashboard"
  },
  {
    "figure_id": "F100",
    "report_id": "R004",
    "label": "Figure 19",
    "context": "Figure 19. Outdoor Sporting & Outdoor Apparel – Monthly US credit card spend dashboard Average spend per individual customer and Number of Individual customers - YoY % chg"
  },
  {
    "figure_id": "F101",
    "report_id": "R004",
    "label": "Figure 20",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 20. Beauty and Cosmetics – Monthly US credit card spend dashboard"
  },
  {
    "figure_id": "F102",
    "report_id": "R004",
    "label": "Figure 21",
    "context": "■ The blue dots denote historical US quarterly sales growth. ■ The red dot denotes the last published quarter. ■ The red star denotes the implied growth for the next quarter to be reported. Figure 21. LVMH vs. Citi credit card – US quarterly YoY sales growth"
  },
  {
    "figure_id": "F103",
    "report_id": "R004",
    "label": "Figure 23",
    "context": "Figure 23. Gucci vs. Citi credit card – US quarterly YoY sales growth"
  },
  {
    "figure_id": "F104",
    "report_id": "R004",
    "label": "Figure 22",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 22. LVMH vs. Citi credit card – US quarterly YoY sales growth"
  },
  {
    "figure_id": "F105",
    "report_id": "R004",
    "label": "Figure 24",
    "context": "Figure 24. Gucci – US quarterly YoY sales growth regression"
  },
  {
    "figure_id": "F106",
    "report_id": "R004",
    "label": "Figure 25",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 25. Hermes vs. Citi credit card – US quarterly YoY sales growth"
  },
  {
    "figure_id": "F107",
    "report_id": "R004",
    "label": "Figure 26",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 26. Hermes – US quarterly YoY sales growth regression"
  },
  {
    "figure_id": "F108",
    "report_id": "R004",
    "label": "Figure 27",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 27. Moncler vs. Citi credit card – US quarterly YoY sales growth"
  },
  {
    "figure_id": "F109",
    "report_id": "R004",
    "label": "Figure 28",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 28. Moncler – US quarterly YoY sales growth regression"
  },
  {
    "figure_id": "F110",
    "report_id": "R004",
    "label": "Figure 29",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 29. Richemont vs. Citi credit card – US quarterly YoY sales growth"
  },
  {
    "figure_id": "F111",
    "report_id": "R004",
    "label": "Figure 30",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 30. Richemont – US quarterly YoY sales growth regression"
  },
  {
    "figure_id": "F112",
    "report_id": "R004",
    "label": "Figure 31",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 31. Hugo Boss vs. Citi credit card – US quarterly YoY sales growth"
  },
  {
    "figure_id": "F113",
    "report_id": "R004",
    "label": "Figure 32",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 32. Hugo Boss – US quarterly YoY sales growth regression"
  },
  {
    "figure_id": "F114",
    "report_id": "R004",
    "label": "Figure 33",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 33. Ferragamo vs. Citi credit card – US quarterly YoY sales growth"
  },
  {
    "figure_id": "F115",
    "report_id": "R004",
    "label": "Figure 35",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 35. Pandora vs. Citi credit card – US quarterly YoY sales growth"
  },
  {
    "figure_id": "F116",
    "report_id": "R004",
    "label": "Figure 34",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 34. Ferragamo – US quarterly YoY sales growth regression"
  },
  {
    "figure_id": "F117",
    "report_id": "R004",
    "label": "Figure 36",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 36. Pandora – US quarterly YoY sales growth regression"
  },
  {
    "figure_id": "F118",
    "report_id": "R004",
    "label": "Figure 37",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 37. Adidas vs. Citi credit card – US quarterly YoY sales growth"
  },
  {
    "figure_id": "F119",
    "report_id": "R004",
    "label": "Figure 38",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 38. Adidas – US quarterly YoY sales growth regression"
  },
  {
    "figure_id": "F120",
    "report_id": "R004",
    "label": "Figure 39",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 39. Burberry vs. Citi credit card – US quarterly YoY sales growth"
  },
  {
    "figure_id": "F121",
    "report_id": "R004",
    "label": "Figure 40",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 40. Burberry – US quarterly YoY sales growth regression"
  },
  {
    "figure_id": "F122",
    "report_id": "R004",
    "label": "Figure 41",
    "context": "## Appendix 2 – Quarterly US luxury credit card spend dashboard Figure 41. US luxury spend – Quarterly credit card dashboard Luxury Brands, Total Luxury, Sport brands and Retailers and Beauty and Cosmetics - Total quarterly spend YoY % chg"
  },
  {
    "figure_id": "F123",
    "report_id": "R004",
    "label": "Figure 42",
    "context": "## Appendix 3 – North American luxury market snapshot Figure 42. North America accounted for just over 20% of the global luxury market in 2025"
  },
  {
    "figure_id": "F124",
    "report_id": "R004",
    "label": "Figure 44",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 44. US Luxury market – Revenue breakdown by product category, 2024 (retail values, RSP)"
  },
  {
    "figure_id": "F125",
    "report_id": "R004",
    "label": "Figure 46",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 46. US Luxury market – Revenue breakdown between brick-and-mortar and online, 2019"
  },
  {
    "figure_id": "F126",
    "report_id": "R004",
    "label": "Figure 43",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 43. The American cohort accounted for 25% of global luxury revenues in 2025"
  },
  {
    "figure_id": "F127",
    "report_id": "R004",
    "label": "Figure 45",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 45. Luxury & Sporting goods universe – Revenue exposure to the US, 1H25"
  },
  {
    "figure_id": "F128",
    "report_id": "R004",
    "label": "Figure 47",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 47. Luxury market – Revenue breakdown between brick-and-mortar and online, 2024"
  },
  {
    "figure_id": "F129",
    "report_id": "R004",
    "label": "Figure 48",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 48. Seasonality of US Luxury credit card spend – Share of annual spend by month, 2019–2024"
  },
  {
    "figure_id": "F130",
    "report_id": "R004",
    "label": "Figure 50",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 50. Total Luxury spend YoY growth slowed in 2022 and 2023 and recovered slightly in 2024 and 2025..."
  },
  {
    "figure_id": "F131",
    "report_id": "R004",
    "label": "Figure 49",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 49. US Luxury credit card spend – December accounting for over 40% of 4Q spend"
  },
  {
    "figure_id": "F132",
    "report_id": "R004",
    "label": "Figure 51",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 51. ...and below 2019 levels"
  },
  {
    "figure_id": "F133",
    "report_id": "R004",
    "label": "Figure 52",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. ## Appendix 4 – US consumption snapshot Figure 52. Share of US consumer expenditure by income quintile, 2023"
  },
  {
    "figure_id": "F134",
    "report_id": "R004",
    "label": "Figure 53",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 53. Share of US net worth by income quintile, 2023"
  },
  {
    "figure_id": "F135",
    "report_id": "R004",
    "label": "Figure 54",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 54. Share of US income by income quintile, 2023"
  },
  {
    "figure_id": "F136",
    "report_id": "R006",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Container ships to the US remain volatile; levels are still down from post-Liberation day increases Daily Laden Container Ship Vessels from China to US"
  },
  {
    "figure_id": "F137",
    "report_id": "R006",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Laden container ships from China to US have decelerated on a YoY basis in the most recent week Daily Laden Container Ship Vessels from China to US, YoY"
  },
  {
    "figure_id": "F138",
    "report_id": "R006",
    "label": "Exhibit 3",
    "context": "Exhibit 3: TEUs have remained volatile Daily TEU from China to the US"
  },
  {
    "figure_id": "F139",
    "report_id": "R006",
    "label": "Exhibit 4",
    "context": "Exhibit 4: TEU growth was decelerated in the most recent week Data as of 6/4/2026. Represents the aggregated container volume, measured in twenty-foot equivalent units (TEU), of vessels departing China for the United States over a"
  },
  {
    "figure_id": "F140",
    "report_id": "R006",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Mainland China and Asia-Ex Mainland: vessels were up YoY for Mainland China and Asia Ex Mainland China Daily Laden Container Ship Vessels from Asia ex-Mainland China and Mainland China to US, YoY"
  },
  {
    "figure_id": "F141",
    "report_id": "R006",
    "label": "Exhibit 7",
    "context": "Exhibit 7: TEU growth from Mainland China was down vs Asia-Ex Mainland China was up this past week Daily TEU from Asia ex-Mainland China and Mainland China to US, YoY"
  },
  {
    "figure_id": "F142",
    "report_id": "R006",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Chinese port activity was up +10% sequentially in the most recent week and up +7% YoY Chinese major port weekly container throughput"
  },
  {
    "figure_id": "F143",
    "report_id": "R006",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Ocean rates were up +51% WoW after remaining flat in the previous week China/East Asia to the North American West Coast, \\$/FEU"
  },
  {
    "figure_id": "F144",
    "report_id": "R006",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Planned TEUs are expected to increase sequentially next week and 2 weeks out Planned TEUs into the Port of LA"
  },
  {
    "figure_id": "F145",
    "report_id": "R006",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Trends for air cargo out of Asia Pacific to North America: weight and rate increased in the most recent week (+5% and +1% respectively) WorldACD Last Two Weeks Compared with the Preceding Two Weeks, Asia Pacific to North"
  },
  {
    "figure_id": "F146",
    "report_id": "R006",
    "label": "Exhibit 13",
    "context": "Exhibit 14: Rates were +32% YoY last week on the West Coast"
  },
  {
    "figure_id": "F147",
    "report_id": "R006",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Rates were +32% YoY last week on the West Coast Truckload Spot Rates ex-fuel West Coast"
  },
  {
    "figure_id": "F148",
    "report_id": "R006",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Truckload load availability was +42% YoY this past week on the West Coast Truckload Load Availability Index on the West Coast"
  },
  {
    "figure_id": "F149",
    "report_id": "R006",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Congestion remains fluid as per our supply chain congestion index, about in line with pre-Covid levels GS Weekly Supply Chain Congestion Index, Feb 2020 – May 2026"
  },
  {
    "figure_id": "F150",
    "report_id": "R006",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Imports into the West Coast were -1% YoY in March Big Three Volumes YoY"
  },
  {
    "figure_id": "F151",
    "report_id": "R006",
    "label": "Exhibit 19",
    "context": "Exhibit 19: April rates were up $25\\%$ from March Drewry Air Rates Shanghai to LA"
  },
  {
    "figure_id": "F152",
    "report_id": "R006",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Big Three growth tends to follow TEU growth out of Asia to the US Big Three YoY v. China/Asia/Asia ex-China to US TEU Monthly YoY"
  },
  {
    "figure_id": "F153",
    "report_id": "R006",
    "label": "Exhibit 21",
    "context": "Exhibit 21: We estimate that April levels were lower YoY Implied Trade Value Change YoY Based on YoY TEU Change and Estimated Value/TEU"
  },
  {
    "figure_id": "F154",
    "report_id": "R006",
    "label": "Exhibit 22",
    "context": "Exhibit 22: LMI has shown upstream and downstream expansion Logistics Manager Index – Inventory Level Expansion, Upstream (B2B) vs Downstream (Retail) Respondents"
  },
  {
    "figure_id": "F155",
    "report_id": "R006",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Inventory costs slowed in April LMI Inventory Cost Index"
  },
  {
    "figure_id": "F156",
    "report_id": "R006",
    "label": "Exhibit 24",
    "context": "Exhibit 24: Inventory to sales have not shown an increase like in Trump 1.0... Inventory to Sales Ratio: Retailers ex Motor Vehicle and Parts Dealers"
  },
  {
    "figure_id": "F157",
    "report_id": "R006",
    "label": "Exhibit 25",
    "context": "Exhibit 25: ...nor for manufacturers... Inventory to Sales Manufacturers"
  },
  {
    "figure_id": "F158",
    "report_id": "R006",
    "label": "Exhibit 26",
    "context": "Exhibit 26: ...while wholesalers were also unchanged Inventory to Sales Wholesalers"
  },
  {
    "figure_id": "F159",
    "report_id": "R008",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Year-over-year nominal trade growth accelerated in May"
  },
  {
    "figure_id": "F160",
    "report_id": "R008",
    "label": "Exhibit 2",
    "context": "Exhibit 2: China's trade surplus increased to US\\$105.4bn in May"
  },
  {
    "figure_id": "F161",
    "report_id": "R008",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Chinese nominal exports to major trading partners increased sequentially in May, except the EU and Latin America"
  },
  {
    "figure_id": "F162",
    "report_id": "R008",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Chinese imports from major trading partners fell sequentially in May, except the US and Japan"
  },
  {
    "figure_id": "F163",
    "report_id": "R009",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Payroll Employment Rose More Than 80k Above Trend in Host Cities During the 1994 World Cup, With Job Gains Largely Concentrated in the Leisure & Hospitality, Trade, and Business Services Sectors Deviation of Payrolls f"
  },
  {
    "figure_id": "F164",
    "report_id": "R009",
    "label": "Exhibit 3",
    "context": "Exhibit 3: The World Cup Should Provide a Tailwind to Foreign Tourism into the US in June and July"
  },
  {
    "figure_id": "F165",
    "report_id": "R009",
    "label": "Exhibit 4",
    "context": "Exhibit 4: We Estimate That Spending by Foreign and Domestic World Cup Fans Should Provide a Peak Boost to Retail Sales Growth of 0.3pp in June and to Consumer Spending of 0.05pp in Q2 Real Consumption Expenditure by Foreign Trav"
  },
  {
    "figure_id": "F166",
    "report_id": "R009",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Scaling Up the GDP Impact of Past Super Bowls Using the Estimated Effects on Employment Suggests That the 2026 World Cup Could Add 0.1pp to Annualized GDP Growth in 2026Q2"
  },
  {
    "figure_id": "F167",
    "report_id": "R009",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Sharply Higher Hotel Prices in Host Cities Around Match Days Imply a World Cup Boost to Average US Hotel Prices of About 1% in June Hotel Room Price Difference from Regular Prices on Match Nights in Host Cities in June"
  },
  {
    "figure_id": "F168",
    "report_id": "R009",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Past Sporting Events Drove Temporary Prices Hikes for Restaurants and Transportation Services Difference Between Food Away from Home CPI MoM Growth in Host MSAs vs. Rest of the US"
  },
  {
    "figure_id": "F169",
    "report_id": "R009",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Past Major Sporting Events Boosted Monthly CPI Inflation by 0.1-0.4pp in the Host Cities in Event Months; a Similar World Cup Impact Would Boost National June CPI Inflation by 0.03-0.1pp Difference Between Monthly Head"
  },
  {
    "figure_id": "F170",
    "report_id": "R010",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: European Defense stocks have been weak since Q2'26... European Defense Stocks YTD Performance Since Ukraine War, (base 100 from 1st Jan. 2026)"
  },
  {
    "figure_id": "F171",
    "report_id": "R010",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: ... But valuations are only back to the levels of January 2026 EU Defense - 12m fwd EV/EBITDA"
  },
  {
    "figure_id": "F172",
    "report_id": "R010",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Rheinmetall should significantly outgrow peers until 2030 EU Defense - 2025-30 Revenue CAGR"
  },
  {
    "figure_id": "F173",
    "report_id": "R010",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: Some European Defense companies have large exposure to the US market EU Defense Revenue Exposure to US (excluding civil sales when possible), 2024"
  },
  {
    "figure_id": "F174",
    "report_id": "R010",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: Total Defense Budget (\\$bn)"
  },
  {
    "figure_id": "F175",
    "report_id": "R010",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: Total Inv Account (RDT&E + Procurement) Budget (\\$bn)"
  },
  {
    "figure_id": "F176",
    "report_id": "R010",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: Germany is the largest Defense market in Europe ex. Russia"
  },
  {
    "figure_id": "F177",
    "report_id": "R010",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: Air is the largest spending segment among equipment spending over 2022-26... German Defense Equipment Budget Breakdown, (procurement + maintenance), 2022-26"
  },
  {
    "figure_id": "F178",
    "report_id": "R010",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: The German defense budget is expected to grow by 12% until 2030 German Defense Spending ex. Ukraine Support, in €bn"
  },
  {
    "figure_id": "F179",
    "report_id": "R010",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: The German addressable market should grow at a +20.5% CAGR until 2030"
  },
  {
    "figure_id": "F180",
    "report_id": "R010",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: France is the fourth-largest Defense market in Europe Europe ex. Russia Defense Expenditure, 2025"
  },
  {
    "figure_id": "F181",
    "report_id": "R010",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: ...and the second-largest exporter in the world Arm Exports by Country of Origin, 2020-25"
  },
  {
    "figure_id": "F182",
    "report_id": "R010",
    "label": "EXHIBIT 13",
    "context": "EXHIBIT 13: French defense spending is expected to grow by +7% annually until 2030"
  },
  {
    "figure_id": "F183",
    "report_id": "R010",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: The French addressable market is forecast to grow at an +8.4% CAGR until 2030"
  },
  {
    "figure_id": "F184",
    "report_id": "R010",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: The UK defense budget should grow slowly from current levels UK MoD Spending Plans, in £bn, in real terms (2024/25 prices)"
  },
  {
    "figure_id": "F185",
    "report_id": "R010",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 16: Poland, Romania and Hungary benefit the most from the SAFE fund"
  },
  {
    "figure_id": "F186",
    "report_id": "R012",
    "label": "EXHIBIT 1",
    "context": "Then there are the free riders. For example, the leading classified players, which can display cars for sale and have car dealers pay to be able to place these listings (the content in this case) on the website. These types of firms consistently exhibit very h"
  },
  {
    "figure_id": "F187",
    "report_id": "R012",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: Digital advertising spending worldwide from 2021 to 2026 (in billion U.S. dollars)"
  },
  {
    "figure_id": "F188",
    "report_id": "R012",
    "label": "EXHIBIT 3",
    "context": "includes advertising that appears on desktop and laptop computers as well as mobile phones connected devices, and includes all the various formats of advertising on those platforms \\* Forecast"
  },
  {
    "figure_id": "F189",
    "report_id": "R012",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: Only four of today's top 10 most valuable digital companies existed prior to 2000 We excluded all AI companies EXHIBIT 5: Global digital ad spend keeps on rising although slightly less strong than over the last decades"
  },
  {
    "figure_id": "F190",
    "report_id": "R012",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: In recent years, the media sector has been dominated by the transition from traditional media to digital Total Media Ad Spending in the US, by Media (Share; %)"
  },
  {
    "figure_id": "F191",
    "report_id": "R012",
    "label": "Exhibit 11",
    "context": "EXHIBIT 7: There are two structurally different advertising markets with one growing much more than the other one, which is reflective of and in the client base ```mermaid graph TD"
  },
  {
    "figure_id": "F192",
    "report_id": "R012",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: When Market 1 players adopt Market 2 practices they see good growth at least in line with players from Market 2 (2025 revenue growth)"
  },
  {
    "figure_id": "F193",
    "report_id": "R012",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: However, these business units are only making up a small part of total revenues of their respective groups (% of FY25 revenues)"
  },
  {
    "figure_id": "F194",
    "report_id": "R012",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: Advertising dynamics are different depending on who you look at - based on FY25 revenue growth (organic for the agencies)"
  },
  {
    "figure_id": "F195",
    "report_id": "R012",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: The advertising client pool of of agencies is dramatically different to the one of the major Internet platforms"
  },
  {
    "figure_id": "F196",
    "report_id": "R012",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: Client concentration is very high at the agencies (approximate revenues coming from top 10 clients)"
  },
  {
    "figure_id": "F197",
    "report_id": "R012",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: The advertising options have multiplied since the Mad Men days ```mermaid graph TD"
  },
  {
    "figure_id": "F198",
    "report_id": "R012",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: Today on instagram alone you can advertise in 8 formats but there are 1000s of other options in which one can advertise Discover the 8 Types of Instagram Ads (+ Inspiring Examples) TO ENJOY"
  },
  {
    "figure_id": "F199",
    "report_id": "R012",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 16: Among media access points, mobile devices dominate time spent, but CTV is Growing Faster"
  },
  {
    "figure_id": "F200",
    "report_id": "R012",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 17: US adults spend over eight hours per day with Digital Media via a multitude of disparate activities"
  },
  {
    "figure_id": "F201",
    "report_id": "R012",
    "label": "Exhibit 18",
    "context": "EXHIBIT 18: Brand-building and sales activation work over different timescales"
  },
  {
    "figure_id": "F202",
    "report_id": "R012",
    "label": "EXHIBIT 19",
    "context": "EXHIBIT 19: Digital advertising can reach the entire marketing funnel whereas traditional advertising was always limited to the top of the funnel. ```mermaid graph TD"
  },
  {
    "figure_id": "F203",
    "report_id": "R012",
    "label": "EXHIBIT 20",
    "context": "EXHIBIT 20: Particularly newer forms of Digital Advertising reduce the journey from awareness to POS ```mermaid graph LR"
  },
  {
    "figure_id": "F204",
    "report_id": "R012",
    "label": "Exhibit 22",
    "context": "EXHIBIT 22: Normalized linear advertising revenue continue to decline for all media companies except for Fox Normalized Linear Ad Revenue YoY Growth (Calendar Year)"
  },
  {
    "figure_id": "F205",
    "report_id": "R012",
    "label": "EXHIBIT 23",
    "context": "EXHIBIT 23: All DTC platforms had strong advertising revenue growth DTC Ad Revenue YoY Growth (Calendar Year)"
  },
  {
    "figure_id": "F206",
    "report_id": "R012",
    "label": "EXHIBIT 24",
    "context": "EXHIBIT 24: Industry total linear advertising revenue has continued to decline, Fox remains the only player with positive linear ad revenue growth"
  },
  {
    "figure_id": "F207",
    "report_id": "R012",
    "label": "EXHIBIT 25",
    "context": "EXHIBIT 25: While the growth in DTC advertising revenue offset some of the linear decline, the industry total ad revenue is still declining Implies Linear ad dollars not shifting fast enough to Streaming and/or new SVOD inventory (e"
  },
  {
    "figure_id": "F208",
    "report_id": "R013",
    "label": "Figure 1",
    "context": "Figure 1: Weekly change in China visible copper inventory (SHFE + Bonded). Net inventory movement broadly flat in week ended 5 Jun'26 x-axis = weeks post Chinese New Year (week 0 = week closest to start of CNY), y-axis = kt of cop"
  },
  {
    "figure_id": "F209",
    "report_id": "R013",
    "label": "Figure 2",
    "context": "\\*Build over first and second weeks post-CNY averaged due to lagged inventory reporting. US\\$/t"
  },
  {
    "figure_id": "F210",
    "report_id": "R013",
    "label": "Figure 3",
    "context": "Figure 3: FOB iron ore price from Australia to China at \\~\\$86/t, -\\$1/t vs end of Feb & -\\$6/t YTD \\$/t"
  },
  {
    "figure_id": "F211",
    "report_id": "R013",
    "label": "Figure 4",
    "context": "Figure 4: Weekly change in China visible copper inventory (SHFE + Bonded). Net inventory movement broadly flat in week ended 5 Jun'26 x-axis = weeks post Chinese New Year (week 0 = week closest to start of CNY), y-axis = kt of cop"
  },
  {
    "figure_id": "F212",
    "report_id": "R013",
    "label": "Figure 5",
    "context": "Figure 5: Total China visible copper inventory (SHFE + Bonded) week ended 5 Jun'26. Copper inventory (218kt) remains at bottom end of seasonal range but \\~40kt higher vs 2025 x-axis = weeks post Chinese New Year (week 0 = week clo"
  },
  {
    "figure_id": "F213",
    "report_id": "R013",
    "label": "Figure 6",
    "context": "Figure 6: Aluminum inventories movements in 2026 – weekly change in China visible aluminium inventory (SHFE + Bonded). Aluminum de-stocking stronger at -26kt last week x-axis = weeks post Chinese New Year (week 0 = week closest to"
  },
  {
    "figure_id": "F214",
    "report_id": "R013",
    "label": "Figure 7",
    "context": "Figure 7: Total China visible aluminum inventory (SHFE + Regional Warehouses) week ended 5 Jun'26. China aluminum inventory (1.4Mt) is at the highest level for this period since 2019 x-axis = weeks post Chinese New Year (week 0 ="
  },
  {
    "figure_id": "F215",
    "report_id": "R013",
    "label": "Figure 8",
    "context": "Figure 8: Zinc inventories movements in 2026 – weekly change in China visible zinc inventory (SHFE + Bonded). Zinc inventory restocking last week of 3kt x-axis = weeks post Chinese New Year (week 0 = week closest to start of CNY),"
  },
  {
    "figure_id": "F216",
    "report_id": "R013",
    "label": "Figure 9",
    "context": "Figure 9: Total China visible zinc inventory for week ended 5 Jun'26. Total inventory (264kt) is at the highest seasonal level since 2022 x-axis = weeks post Chinese New Year (week 0 = week closest to start of CNY), y-axis = kt of"
  },
  {
    "figure_id": "F217",
    "report_id": "R013",
    "label": "Figure 10",
    "context": "Figure 10: China Yangshan Copper Premium vs LME Copper Spot: Premium moderated to \\~\\$65/t as China copper buying slows down LHS: Yangshan Premium; RHS: LME Copper Spot; Unit: \\$/t"
  },
  {
    "figure_id": "F218",
    "report_id": "R013",
    "label": "Figure 11",
    "context": "Figure 11: China steel mill margins extend losses driven by higher coking coal prices"
  },
  {
    "figure_id": "F219",
    "report_id": "R013",
    "label": "Figure 12",
    "context": "Figure 12: China steel inventory week ending 5 Jun, flat WoW and +7% YoY; Inventory has remained relatively flat since late May"
  },
  {
    "figure_id": "F220",
    "report_id": "R013",
    "label": "Figure 13",
    "context": "Figure 13: Iron Ore inventory held at ports in China \\~159Mt is high vs history but has shown a drawdown trend in the past few weeks"
  },
  {
    "figure_id": "F221",
    "report_id": "R013",
    "label": "Figure 14",
    "context": "Figure 14: Global iron ore shipments - we are entering the seasonal period during which global iron ore shipments ramp up. Global shipments +6% MoM in April & +4% YoY"
  },
  {
    "figure_id": "F222",
    "report_id": "R013",
    "label": "Figure 15",
    "context": "Figure 15: Australia iron ore shipments - Latest data suggests Australian iron ore shipments +8% MoM in April & +3% YoY Mt iron ore exports, red bar = February, typical seasonal trough for shipments is Jan/Feb"
  },
  {
    "figure_id": "F223",
    "report_id": "R013",
    "label": "Figure 16",
    "context": "Figure 16: Brazil iron ore shipments +6% MoM in April, +6% YoY Mt iron ore exports, red bar = February, typical seasonal trough for shipments is Jan/Feb"
  },
  {
    "figure_id": "F224",
    "report_id": "R013",
    "label": "Figure 17",
    "context": "Figure 17: Chinese visible copper inventory (SHFE + Bonded) for week ended 5 Jun. Copper inventories flat in the past few weeks due to minimal net buying"
  },
  {
    "figure_id": "F225",
    "report_id": "R013",
    "label": "Figure 18",
    "context": "Figure 18: China visible aluminium inventory (SHFE + Regional Warehouses) for week ended 5 Jun. Aluminum inventories are still at the highest level vs 5-year range but de-stocking has begun in China kt of aluminium"
  },
  {
    "figure_id": "F226",
    "report_id": "R013",
    "label": "Figure 19",
    "context": "Figure 19: China visible zinc inventory (SHFE + Regional Warehouses) for week ended 5 Jun. Zinc inventories are still at the highest level vs 5-year range kt of zinc"
  },
  {
    "figure_id": "F227",
    "report_id": "R014",
    "label": "Exhibit 2",
    "context": "Global data center server by vertical and AI/traditional (\\$, mn) Industry AI server estimate revisions (\\$, mn)"
  },
  {
    "figure_id": "F228",
    "report_id": "R014",
    "label": "Exhibit 3",
    "context": "Industry traditional server estimate revisions (\\$, mn)"
  },
  {
    "figure_id": "F229",
    "report_id": "R014",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Nvidia leads the AI server market with 44% share as of 1Q26, followed by whitebox players (22%), Dell (17%), and Super Micro (11%) AI server revenue market share (%)"
  },
  {
    "figure_id": "F230",
    "report_id": "R014",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Neocloud AI server market share leadership oscillates between DELL and SMCI Neocloud AI server revenue market share (%)"
  },
  {
    "figure_id": "F231",
    "report_id": "R014",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Dell gained significant share in enterprise AI servers in 1Q26 (47%) Enterprise AI server revenue market share"
  },
  {
    "figure_id": "F232",
    "report_id": "R014",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Dell lead the traditional server market in 1Q26 (30% share), followed by white-box (24%), HPE (11%), Lenovo (7%), and IBM (6%). Traditional server revenue market share (%)"
  },
  {
    "figure_id": "F233",
    "report_id": "R014",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Neocloud traditional server market share is more mixed, with DELL and SMCI leading in 1Q26 Neocloud traditional server market share"
  },
  {
    "figure_id": "F234",
    "report_id": "R014",
    "label": "Exhibit 9",
    "context": "Exhibit 9: DELL leads the enterprise traditional server market with $38\\%$ share in 1Q26 Enterprise traditional server revenue market share"
  },
  {
    "figure_id": "F235",
    "report_id": "R015",
    "label": "Exhibit 1",
    "context": "Exhibit 1: TFT-LCD TV Panel Price Trends"
  },
  {
    "figure_id": "F236",
    "report_id": "R015",
    "label": "Exhibit 3",
    "context": "Exhibit 3: TV Panel Price Trend (QoQ) TV Panel Price QoQ"
  },
  {
    "figure_id": "F237",
    "report_id": "R015",
    "label": "Exhibit 4",
    "context": "Exhibit 4: IT Panel Price (QoQ)"
  },
  {
    "figure_id": "F238",
    "report_id": "R015",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Industry Average Utilization at Display Fabs"
  },
  {
    "figure_id": "F239",
    "report_id": "R015",
    "label": "Exhibit 6",
    "context": "Exhibit 6: AUO Share Price vs. Panel Price"
  },
  {
    "figure_id": "F240",
    "report_id": "R015",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Innolux Share Price vs. Panel Price"
  },
  {
    "figure_id": "F241",
    "report_id": "R015",
    "label": "Exhibit 8",
    "context": "Exhibit 8: BOE Share Price vs. Panel Price"
  },
  {
    "figure_id": "F242",
    "report_id": "R015",
    "label": "Exhibit 9",
    "context": "Exhibit 9: TCL Share Price vs. Panel Price"
  },
  {
    "figure_id": "F243",
    "report_id": "R015",
    "label": "Exhibit 10",
    "context": "Exhibit 10: GLW Display Volumes vs. Utilization"
  },
  {
    "figure_id": "F244",
    "report_id": "R015",
    "label": "Exhibit 11",
    "context": "Exhibit 11: GLW Display Revenue vs. Utilization"
  },
  {
    "figure_id": "F245",
    "report_id": "R017",
    "label": "Exhibit 2",
    "context": "Exhibit 2: NEV dealer discount trend"
  },
  {
    "figure_id": "F246",
    "report_id": "R017",
    "label": "Exhibit 3",
    "context": "Exhibit 3: ICE dealer discount trend"
  },
  {
    "figure_id": "F247",
    "report_id": "R018",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Primary GFA sold last week was -13% wow and +15% yoy in c.75 cities"
  },
  {
    "figure_id": "F248",
    "report_id": "R018",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Primary GFA sold YTD on average was -13% yoy in c.75 cities, and -13%/-44% vs. 2024/2023 level"
  },
  {
    "figure_id": "F249",
    "report_id": "R018",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Secondary GFA sold last week was -7% wow and +31% yoy in c.20 cities Average weekly volume of secondary property sales"
  },
  {
    "figure_id": "F250",
    "report_id": "R018",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Secondary GFA sold YTD was $+1\\%$ yoy in c.20 cities, while $+22\\% / +8\\%$ vs. 2024/ secondary volume sold vs. 2022-25"
  },
  {
    "figure_id": "F251",
    "report_id": "R018",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Average CSI was +0.4pp wow and +5.9pp yoy Weekly Centraline Salesman Index (CSI) tracker in 4 cities"
  },
  {
    "figure_id": "F252",
    "report_id": "R018",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Average CAI was flat wow and -3.9pp yoy Weekly Centraline Seller Asking Index (CAI) tracker in 6 cities"
  },
  {
    "figure_id": "F253",
    "report_id": "R018",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Inventory balance was $-0.2\\%$ wow, $-4.6\\%$ from end-25 levels c.20 cities' total inventory breakdown by city tier (Indexed to Jan 2013)"
  },
  {
    "figure_id": "F254",
    "report_id": "R018",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Inventory month was flat wow, representing $-0.6\\%$ from end-25 levels c.20 cities' inventory months (12mth rolling) breakdown by city tier"
  },
  {
    "figure_id": "F255",
    "report_id": "R018",
    "label": "Exhibit 9",
    "context": "Exhibit 9: GSPC tracker implied monthly completions... GSPC tracker implied monthly GFA completion - based on GS float glass S-D model"
  },
  {
    "figure_id": "F256",
    "report_id": "R018",
    "label": "Exhibit 10",
    "context": "Exhibit 10: ...suggesting completions at a high-teens % yoy decline for May-26 % yoy change of GSPC - based on GS float glass S-D model"
  },
  {
    "figure_id": "F257",
    "report_id": "R019",
    "label": "Exhibit 1",
    "context": "Exhibit 1: China excavator sales volume Exhibit 2: China's monthly excavator sales volume vs. Sany Heavy's share price"
  },
  {
    "figure_id": "F258",
    "report_id": "R021",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Nvidia Vera CPU specs NVIDIA Vera CPU for Agents NVIDIA-Custom Olympus Core 88-Core / 176-Threads"
  },
  {
    "figure_id": "F259",
    "report_id": "R021",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Close-up look of a Vera CPU tray Model of a satellite or spacecraft module with grid panels and labeled 'MEMSIA Hens CPU tray' (no readable text beyond label)"
  },
  {
    "figure_id": "F260",
    "report_id": "R021",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Nvidia RTX Spark Laptops with Blackwell RTX GPU, Grace CPU, and 128GB unified memory Announcing NVIDIA and Microsoft Reinvent PC Powered by RTX Spark"
  },
  {
    "figure_id": "F261",
    "report_id": "R021",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Nvidia's Nemotron Ultra 3 open model is cost effective and fast Announcing NVIDIA Nemotron 3 Ultra 30% Lower Cost"
  },
  {
    "figure_id": "F262",
    "report_id": "R021",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Integrated AI vision & camera system for drones will be a major growth driver for Elan LAN Integrated AI Vision & Camera System for Drones"
  },
  {
    "figure_id": "F263",
    "report_id": "R021",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Realtek's single-chip solution for ethernet and high-speed IO integration REALTEK RTL9151AS PCIe 60 Multi-IO Bridge Controller Single-Chip for Ethernet and"
  },
  {
    "figure_id": "F264",
    "report_id": "R021",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Agentic AI transforms inference ```mermaid graph TD"
  },
  {
    "figure_id": "F265",
    "report_id": "R021",
    "label": "Exhibit 8",
    "context": "Exhibit 8: GPU direct storage GPU Direct Storage ■ Expanding HBM capacity by GPU direct SSD access. GPU Server Direct GPU-to-SSD Access"
  },
  {
    "figure_id": "F266",
    "report_id": "R021",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Expansion of inference AI server system Expansion of Inference AI Server System - TOMORROW Storage Server Training & Inference Data Context Memory"
  },
  {
    "figure_id": "F267",
    "report_id": "R021",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Key directions for SSD products 3 Key Directions for SSD products Super High IOPS GPU Direct Storage High Performance"
  },
  {
    "figure_id": "F268",
    "report_id": "R022",
    "label": "Figure 5",
    "context": "The flagship project is Hanwha's planned investment of around USD5bn to expand the Philadelphia shipyard towards twenty vessels a year, and substantive contracts have begun to materialise. In early 2026, Hanwha won a subcontract for concept-design work on the "
  },
  {
    "figure_id": "F269",
    "report_id": "R026",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Our weekly composite index increased in the most recent week (+7% w/w); the bottleneck scale remained at '2'; overall bottleneck levels remain well below peak congestion levels when scale was at '10' and now imply levels"
  },
  {
    "figure_id": "F270",
    "report_id": "R026",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Our average weekly bottleneck score in May is tracking at 2.0; this result is down significantly from the Dec21/Jan22 peak of congestion and close to in line with the pre-Covid baseline GS Weekly Congestion Scale, Scored"
  },
  {
    "figure_id": "F271",
    "report_id": "R026",
    "label": "Exhibit 6",
    "context": "Exhibit 6: 5/1\\* container ships backed up this week on the East/West Coast West vs. East Coast Container Ship Backlog, Weekly Average, Feb 2020 - May 2026"
  },
  {
    "figure_id": "F272",
    "report_id": "R026",
    "label": "Exhibit 7",
    "context": "Exhibit 7: West Coast Class 1 Rails' Intermodal Volume Growth, Week 1 - Week 52 YoY % growth"
  },
  {
    "figure_id": "F273",
    "report_id": "R026",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Intermodal growth (UNP and BNSF) is up \\~6% YoY on average in May West Coast Class 1 Rail Intermodal Traffic YoY % Growth"
  },
  {
    "figure_id": "F274",
    "report_id": "R026",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Dwell for the more typical 20ft container chassis is well off peak congestion levels Chassis Street Dwell Time (20ft Containers)"
  },
  {
    "figure_id": "F275",
    "report_id": "R026",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Ocean Container Shipping Rates, China/East Asia to North America West Coast"
  },
  {
    "figure_id": "F276",
    "report_id": "R026",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Container Weighted Average Dwell Time at San Pedro's Bay, Days"
  },
  {
    "figure_id": "F277",
    "report_id": "R026",
    "label": "Exhibit 12",
    "context": "Exhibit 12: % of Containers Dwelling More than 5 Days"
  },
  {
    "figure_id": "F278",
    "report_id": "R026",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Rail Container Dwell Time, Days"
  },
  {
    "figure_id": "F279",
    "report_id": "R026",
    "label": "Exhibit 14",
    "context": "Exhibit 14: West Coast Ports' Inbound Loaded Containers -1.0% YoY in April"
  },
  {
    "figure_id": "F280",
    "report_id": "R026",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Door to Door Shipping Days, China to US"
  },
  {
    "figure_id": "F281",
    "report_id": "R026",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Total Truck Transportation Employee Count, Seasonally Adjusted"
  },
  {
    "figure_id": "F282",
    "report_id": "R026",
    "label": "Exhibit 17",
    "context": "Exhibit 17: PMI: Manufacturing Suppliers' Delivery Times, YoY, Seasonally Adjusted"
  },
  {
    "figure_id": "F283",
    "report_id": "R026",
    "label": "Exhibit 19",
    "context": "Exhibit 18: The weekly composite index (light blue) leads the monthly (dark blue); expect future monthly updates to confirm recent weekly trends"
  },
  {
    "figure_id": "F284",
    "report_id": "R026",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Our combined scale averaged '108' in April, indicating a bottleneck score of '2' but close to '1' when looking at all metrics (weekly and monthly combined) Weekly + Monthly Combined Congestion Scale\\*"
  },
  {
    "figure_id": "F285",
    "report_id": "R027",
    "label": "Figure 1",
    "context": "Figure 1: HK private residential market - % of Mainland Chinese buyers, defined by last name with Mandarin pinyin (by volume)"
  },
  {
    "figure_id": "F286",
    "report_id": "R027",
    "label": "Figure 2",
    "context": "Figure 2: HK private residential market - % of Mainland Chinese buyers, defined by last name with Mandarin pinyin (by volume)"
  },
  {
    "figure_id": "F287",
    "report_id": "R027",
    "label": "Figure 3",
    "context": "Note: “Mainland Chinese” is defined here using the Mandarin pinyin of the buyer’s last name and does not distinguish the buyer’s current residence or identity. As a result, “Mainland Chinese” who are residing in Hong Kong—as well as local Hong Kong residents w"
  },
  {
    "figure_id": "F288",
    "report_id": "R027",
    "label": "Figure 4",
    "context": "Figure 4: HK mortgage rate / 1M HIBOR / prime rate vs. U.S. Fed funds rate (long-dated)"
  },
  {
    "figure_id": "F289",
    "report_id": "R027",
    "label": "Figure 5",
    "context": "Figure 5: HK rental yield over mortgage rate vs. secondary home price"
  },
  {
    "figure_id": "F290",
    "report_id": "R027",
    "label": "Figure 6",
    "context": "Figure 6: Earnings impact of every 100bps increase in HIBOR (considering % of HKD floating debt)"
  },
  {
    "figure_id": "F291",
    "report_id": "R027",
    "label": "Figure 8",
    "context": "Figure 8: Earnings impact of every 100bps increase in overall effective borrowing cost (without considering floating debt ratio)"
  },
  {
    "figure_id": "F292",
    "report_id": "R027",
    "label": "Figure 7",
    "context": "Figure 7: Increase in financing cost for every 100bps increase in HIBOR (considering % of HKD floating debt)"
  },
  {
    "figure_id": "F293",
    "report_id": "R027",
    "label": "Figure 9",
    "context": "Figure 9: Increase in financing cost for every 100bps increase in overall effective borrowing cost (without considering floating debt ratio)"
  },
  {
    "figure_id": "F294",
    "report_id": "R027",
    "label": "Figure 10",
    "context": "Figure 10: Hong Kong secondary home price index (with key events) since 2024"
  },
  {
    "figure_id": "F295",
    "report_id": "R027",
    "label": "Figure 11",
    "context": "Figure 11: Correlation with HK home prices Y/Y"
  },
  {
    "figure_id": "F296",
    "report_id": "R027",
    "label": "Figure 12",
    "context": "Figure 12: HK Property - YTD share price performance"
  },
  {
    "figure_id": "F297",
    "report_id": "R027",
    "label": "Figure 13",
    "context": "Figure 13: 2026 year-to-date share price performance by company"
  },
  {
    "figure_id": "F298",
    "report_id": "R027",
    "label": "Figure 14",
    "context": "Figure 14: Hong Kong Property - NAV discount"
  },
  {
    "figure_id": "F299",
    "report_id": "R027",
    "label": "Figure 15",
    "context": "Figure 15: NAV discount vs. historical average by company"
  },
  {
    "figure_id": "F300",
    "report_id": "R027",
    "label": "Figure 16",
    "context": "Figure 16: Hong Kong Property - 12m forward dividend yield"
  },
  {
    "figure_id": "F301",
    "report_id": "R027",
    "label": "Figure 17",
    "context": "Figure 17: Dividend yield vs. historical average by company"
  },
  {
    "figure_id": "F302",
    "report_id": "R028",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: Where Medicare fits into health insurance coverage ## Major US Insurance Programs – Spends and Enrollments US Health Insurance - Spends National Health Expenditure By"
  },
  {
    "figure_id": "F303",
    "report_id": "R028",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Who are the major players in Medicare Advantage MA Membership of major MCOs"
  },
  {
    "figure_id": "F304",
    "report_id": "R028",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: MA go-to-market Distribution channels typically include a broker Estimated MA Plan Sales Distribution"
  },
  {
    "figure_id": "F305",
    "report_id": "R028",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: Extra benefits for seniors in MA In 2024, MA members received on average \\$194 per month in extra benefits MA Extra Benefits"
  },
  {
    "figure_id": "F306",
    "report_id": "R028",
    "label": "Exhibit 8",
    "context": "EXHIBIT 8: MA medical cost trend MA effective growth rate – this should represent trend MA Rate Effective growth rate as per final notice"
  },
  {
    "figure_id": "F307",
    "report_id": "R028",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: MA annual bid timeline ```mermaid graph LR"
  },
  {
    "figure_id": "F308",
    "report_id": "R028",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: How an MCO constructs a MA bid + Estimate required medical costs + Determine expected premium level + Forecast competitor offerings of supplemental benefits + Determine operating costs and targeted profit level"
  },
  {
    "figure_id": "F309",
    "report_id": "R028",
    "label": "EXHIBIT 13",
    "context": "EXHIBIT 13: MA membership growth MA had very strong growth in early years"
  },
  {
    "figure_id": "F310",
    "report_id": "R028",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: Medicare operating margin This growth and margin profile attracted competitors Number of MA plans available per senior"
  },
  {
    "figure_id": "F311",
    "report_id": "R028",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: MA membership growth MA membership continued to grow, but at a slower % rate given its larger base MA Growth, YoY %"
  },
  {
    "figure_id": "F312",
    "report_id": "R028",
    "label": "Exhibit 16",
    "context": "EXHIBIT 16: Medicare operating margin And margins compressed from around 5% to around 3%"
  },
  {
    "figure_id": "F313",
    "report_id": "R028",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 18: History of Medicare / MA reform Major legislation impacting Medicare and Medicare Advantage"
  },
  {
    "figure_id": "F314",
    "report_id": "R028",
    "label": "EXHIBIT 20",
    "context": "EXHIBIT 20: MA rates MA Final rates MA Final Rates, %"
  },
  {
    "figure_id": "F315",
    "report_id": "R028",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 21: Medicare operating margin Medicare Operating Margins"
  },
  {
    "figure_id": "F316",
    "report_id": "R028",
    "label": "EXHIBIT 22",
    "context": "EXHIBIT 22: Withdrawal of competition in MA Big 4 MA membership drops"
  },
  {
    "figure_id": "F317",
    "report_id": "R028",
    "label": "EXHIBIT 23",
    "context": "EXHIBIT 23: MA rates normalize in 26, 27 MA Final rates MA Final Rates, %"
  },
  {
    "figure_id": "F318",
    "report_id": "R028",
    "label": "EXHIBIT 26",
    "context": "EXHIBIT 26: Reserving UNH – Medical reserve levels UNH: Medical Costs Payable (end of period) as % Quarterly Premiums"
  },
  {
    "figure_id": "F319",
    "report_id": "R028",
    "label": "EXHIBIT 27",
    "context": "EXHIBIT 27: Bernstein industry estimates on MA margin recovery Expect company level MA margin improvements of 100 bps in 26, 50bps in 27 and beyond Medicare Operating Margins"
  },
  {
    "figure_id": "F320",
    "report_id": "R028",
    "label": "EXHIBIT 28",
    "context": "EXHIBIT 28: Bernstein estimates for industry growth We expect 4-5% LT growth rate for MA membership"
  },
  {
    "figure_id": "F321",
    "report_id": "R031",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: We expect card penetration to approach \\~71% by 2030, up from 64% in 2025 Card Penetration of Purchase PCE (Nominal and Adj. ex-China)"
  },
  {
    "figure_id": "F322",
    "report_id": "R031",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: Majority of card volume growth from 2025 to 2030E will still be driven by US and Europe"
  },
  {
    "figure_id": "F323",
    "report_id": "R031",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: On a cc basis, card volumes grew at \\~11% between 2019-22, \\~9% between 2022-25 and we forecast \\~8% growth between 2025-30. Global Card Purchase Volume Growth Drivers (ex. China)"
  },
  {
    "figure_id": "F324",
    "report_id": "R031",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: Card volumes grew at \\~8% on a nominal basis in 2025.. Global Card Purchase Volume Growth Drivers (ex. China)"
  },
  {
    "figure_id": "F325",
    "report_id": "R031",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: On a nominal basis, we forecast \\~7-8% card volume growth over 2025-30E globally. Global Card Purchase Volume Growth Drivers (ex. China)"
  },
  {
    "figure_id": "F326",
    "report_id": "R031",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: ..and also on cc basis Global Card Purchase Volume Growth Drivers (ex. China)"
  },
  {
    "figure_id": "F327",
    "report_id": "R031",
    "label": "Exhibit 9",
    "context": "EXHIBIT 7: Our growth forecast by region on cc basis - US - \\~5-6%, Europe - 11%, APAC - 5%, LATAM - 13%, Canada - 5%, MEA - 14% General Purpose Card Purchase Volume Growth Drivers by Region (CC, ex. China)"
  },
  {
    "figure_id": "F328",
    "report_id": "R031",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: Our nominal growth forecast by region - US - \\~5-6%, Europe - 10%, APAC - 4%, LATAM - 13%, Canada - 6%, MEA - 12% General Purpose Card Purchase Volume Growth Drivers by Region (Nominal, ex. China)"
  },
  {
    "figure_id": "F329",
    "report_id": "R031",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: We expect card penetration growth to be driven by Europe, Latam, and MEA Card Penetration of C2B Addressable PCE (Nominal, adjusted ex China)"
  },
  {
    "figure_id": "F330",
    "report_id": "R031",
    "label": "Exhibit 10",
    "context": "EXHIBIT 10: Although it sure feels like cards are everywhere, there is still a surprising amount of cash/check in existence globally Global Cash/Other volumes by region (2025E, Total \\$11T)"
  },
  {
    "figure_id": "F331",
    "report_id": "R031",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: Cash Usage varies widely by country; Mexico, Japan, Indonesia, Germany still have high amounts of cash.. Cash as a % of POS Transaction Value (Top 15 GDP Countries, 2025)"
  },
  {
    "figure_id": "F332",
    "report_id": "R031",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: Share of domestic schemes also varies widely by country.. Share of Domestic Schemes within Overall Network (%, 2024)"
  },
  {
    "figure_id": "F333",
    "report_id": "R031",
    "label": "EXHIBIT 13",
    "context": "EXHIBIT 13: How consumers 'pay' around the world ## HOW PENETRATED IS THE US (FOR CARDS)? We estimate US ‘consumer’ card penetration at 74% by 2030. We scrub the numbers a fair bit. Our numerator includes US card volumes (reported"
  },
  {
    "figure_id": "F334",
    "report_id": "R031",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: We estimate US ‘consumer’ card penetration at 72% in 2025 US Card Penetration of C2B Addressable PCE"
  },
  {
    "figure_id": "F335",
    "report_id": "R031",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: Card Penetration is higher at 83% using a more conservative definition of PCE US Card Penetration of C2B Addressable PCE (Conservative Definition)"
  },
  {
    "figure_id": "F336",
    "report_id": "R031",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 16: US card volume growth has been at \\~6% in the past 3 years; the growth mix has flipped with more of the growth coming from PCE growth (vs. card penetration increase historically) US Card Purchase Volume Growth Drivers (N"
  },
  {
    "figure_id": "F337",
    "report_id": "R031",
    "label": "Exhibit 20",
    "context": "EXHIBIT 17: From 25-30, we forecast \\~10% nominal.. Europe Card Purchase Volume Growth Drivers"
  },
  {
    "figure_id": "F338",
    "report_id": "R031",
    "label": "EXHIBIT 18",
    "context": "EXHIBIT 18: ..and \\~11% cc volume growth in Europe Europe Card Purchase Volume Growth Drivers"
  },
  {
    "figure_id": "F339",
    "report_id": "R031",
    "label": "EXHIBIT 19",
    "context": "EXHIBIT 19: In EU, there is still heavy cash usage in many countries EU: Share of Payment Instruments by Value of Payments (2024)"
  },
  {
    "figure_id": "F340",
    "report_id": "R031",
    "label": "EXHIBIT 20",
    "context": "EXHIBIT 20: Domestic schemes in select countries seem to be losing some share.. especially in Germany and France Market Share for Domestic Schemes in select EU countries (%, Mix)"
  },
  {
    "figure_id": "F341",
    "report_id": "R031",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 21: Even in mature markets such as the Nordics, Visa's overall net revenue grew \\~15% cc CAGR and 35% CAGR cc for CMS + VAS (2022-24) Visa in Continental Europe and the Nordics (Revenue Growth, %)"
  },
  {
    "figure_id": "F342",
    "report_id": "R031",
    "label": "EXHIBIT 22",
    "context": "EXHIBIT 22: Between CY20-23, Visa gained 7ppt share in the Nordics. Similarly in 2024, Visa has gained \\~6ppt market share vs. all card players in Continental Europe Visa in Continental Europe and the Nordics (Share gains vs Domesti"
  },
  {
    "figure_id": "F343",
    "report_id": "R031",
    "label": "EXHIBIT 23",
    "context": "EXHIBIT 23: APAC is a battleground region - where volume growth has been weak driven by unique dynamics in mainland China and some other local market nuances APAC Purchase Volume Growth (V/MA, CC %)"
  },
  {
    "figure_id": "F344",
    "report_id": "R031",
    "label": "EXHIBIT 25",
    "context": "EXHIBIT 25: APAC volumes ex-V/MA in China have been growing faster vs overall volumes.. Card Penetration of Purchase PCE in APAC (Nominal and Adj. ex-China)"
  },
  {
    "figure_id": "F345",
    "report_id": "R031",
    "label": "EXHIBIT 24",
    "context": "EXHIBIT 24: While overall card penetration has been declining in the region, ex-V/MA volumes in China, card penetration has been growing modestly.. Card Penetration of Purchase PCE in APAC (Nominal and Adj. ex-China)"
  },
  {
    "figure_id": "F346",
    "report_id": "R031",
    "label": "EXHIBIT 26",
    "context": "EXHIBIT 26: Our rough estimate of card volumes by market in Asia APAC Card Volume Mix by Market (~$4T, 2025)"
  },
  {
    "figure_id": "F347",
    "report_id": "R031",
    "label": "EXHIBIT 27",
    "context": "EXHIBIT 27: While debit cards are performing poorly in places such as India and Indonesia, credit cards growth has been strong Debit and Credit Volume Growth by Market (2025, % YoY CC)"
  },
  {
    "figure_id": "F348",
    "report_id": "R031",
    "label": "EXHIBIT 28",
    "context": "EXHIBIT 28: In places such as India, credit cards account for the vast majority of volumes APAC ex-Mainland China, Debit and Credit Mix (% , 2025)"
  },
  {
    "figure_id": "F349",
    "report_id": "R031",
    "label": "Exhibit 31",
    "context": "EXHIBIT 29: We forecast \\~9% global transactions growth, with 7% in the US, \\~11% in Europe, \\~7% in APAC, \\~13% in LATAM, \\~5% in Canada and \\~15% in MEA between 2025-30E General Purpose Card Transactions Growth Growth by Region (e"
  },
  {
    "figure_id": "F350",
    "report_id": "R031",
    "label": "EXHIBIT 30",
    "context": "Nilson, World Bank, IMF, Bernstein estimates and analysis Visa Gross Revenue Split FY25 (%)"
  },
  {
    "figure_id": "F351",
    "report_id": "R031",
    "label": "EXHIBIT 31",
    "context": "EXHIBIT 31: Processed transactions have historically grown faster vs. volumes V/MA Processed Transactions and Payment Volume Growth (% CAGR)"
  },
  {
    "figure_id": "F352",
    "report_id": "R031",
    "label": "EXHIBIT 32",
    "context": "EXHIBIT 32: Among the top 20 GDP countries, digital payments penetration varies widely.. Card and Other Digital Payment Method Penetration by Market (2025)"
  },
  {
    "figure_id": "F353",
    "report_id": "R031",
    "label": "EXHIBIT 33",
    "context": "EXHIBIT 33: Alternative ways-to-pay drive HSD-LDD% of C2B payments globally and have had successes in places such as India and Brazil Other Payments Penetration (%)"
  },
  {
    "figure_id": "F354",
    "report_id": "R031",
    "label": "EXHIBIT 34",
    "context": "EXHIBIT 34: Alternative ways-to-pay are not new, domestic schemes (often co-badged with V/ MA) already drive 20s% of global card volumes Domestic/Other Schemes Card Penetration (of C2B Payments) by market"
  },
  {
    "figure_id": "F355",
    "report_id": "R031",
    "label": "EXHIBIT 35",
    "context": "EXHIBIT 35: Even in countries where A2A payments have had success (e.g., India, Brazil), card volumes are still growing driven by credit Value of Transactions A2A vs Total Cards (\\$B and Growth in CC)"
  },
  {
    "figure_id": "F356",
    "report_id": "R031",
    "label": "EXHIBIT 35",
    "context": "EXHIBIT 35: Even in countries where A2A payments have had success (e.g., India, Brazil), card volumes are still growing driven by credit Value of Transactions A2A vs Total Cards (\\$B and Growth in CC)"
  },
  {
    "figure_id": "F357",
    "report_id": "R031",
    "label": "Exhibit 36",
    "context": "EXHIBIT 36: Value-added services and new flows, which are \\~40/\\~50% of V/MA's revenues and growing 1.5-2x the rate of core growth, will be incremental to growth. VAS and new flows can sustain MA's revenue growth in the LDD range ev"
  },
  {
    "figure_id": "F358",
    "report_id": "R031",
    "label": "EXHIBIT 37",
    "context": "EXHIBIT 37: Value-added services make up \\~40% of Mastercard's and \\~30% of Visa's net revenue Services share of net revenue for V/MA (%)"
  },
  {
    "figure_id": "F359",
    "report_id": "R031",
    "label": "EXHIBIT 38",
    "context": "EXHIBIT 38: Value-Added Services grew 25% for Visa and 21% for Mastercard in CY25 Value-Added Services Revenue Growth (% YoY, cc as per CY)"
  },
  {
    "figure_id": "F360",
    "report_id": "R031",
    "label": "EXHIBIT 39",
    "context": "EXHIBIT 39: \\~65% if Visa and \\~60% of Mastercard's VAS is network-linked; transactions are the primary driver of these services V/MA Network-Linked VAS (%)"
  },
  {
    "figure_id": "F361",
    "report_id": "R031",
    "label": "EXHIBIT 40",
    "context": "EXHIBIT 40: During its Investor Day, Visa broke down different components and sized the revenue TAM for Value-Added Services at \\$520B Target TAM of Value-Added Services ($B)"
  },
  {
    "figure_id": "F362",
    "report_id": "R031",
    "label": "EXHIBIT 41",
    "context": "EXHIBIT 41: Mastercard also provided a similar TAM sizing on Services Revenue at \\$490B, with \\$165B in SAM Total Services Revenue TAM ($B, 2024E)"
  },
  {
    "figure_id": "F363",
    "report_id": "R031",
    "label": "EXHIBIT 42",
    "context": "EXHIBIT 42: New flows revenues is likely growing faster vs. the core. Note: Visa numbers are for calendar year Visa Total and New Flows Revenue (yoy cc %)"
  },
  {
    "figure_id": "F364",
    "report_id": "R031",
    "label": "EXHIBIT 43",
    "context": "EXHIBIT 43: Growth of value-added services is one of the reasons why V and MA have sustained DD revenue growth outpacing the volume growth in recent years. Note: 2025 revenue growth likely benefited 1-2ppt from FX vol Overall Revenu"
  },
  {
    "figure_id": "F365",
    "report_id": "R031",
    "label": "EXHIBIT 44",
    "context": "EXHIBIT 44: Both Visa and Mastercard's commercial volume growth accelerated during the last year Visa, Mastercard Commercial Volume (Calendar Year, % YoY CC)"
  },
  {
    "figure_id": "F366",
    "report_id": "R031",
    "label": "EXHIBIT 45",
    "context": "EXHIBIT 45: Visa Direct Transactions Growth (% YoY, Fiscal Year) Visa Direct Transaction Growth (% YoY)"
  },
  {
    "figure_id": "F367",
    "report_id": "R031",
    "label": "Exhibit 46",
    "context": "EXHIBIT 46: We expect Visa and Mastercard's revenue growth algorithm to evolve from card penetration growth being the #1 growth driver to new flows and services combined being the dominant growth drivers in the future Visa and Maste"
  },
  {
    "figure_id": "F368",
    "report_id": "R032",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Cumulative outperformance"
  },
  {
    "figure_id": "F369",
    "report_id": "R032",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Weekly hit ratio"
  },
  {
    "figure_id": "F370",
    "report_id": "R032",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Number of ideas, by market No. of \"Three in Three\" Ideas by country"
  }
]