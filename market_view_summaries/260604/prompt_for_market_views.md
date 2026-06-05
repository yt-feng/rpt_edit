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
    "title": "信用市场真正低估的不是地缘风险，而是利率从“调整”到“体制切换”的跳跃",
    "digest": "[wechat_article.md]\n# 信用市场真正低估的不是地缘风险，而是利率从“调整”到“体制切换”的跳跃\n\n过去两个月，全球信用市场经历了一轮令人瞩目的反弹。美国投资级和高收益利差分别收窄17个基点和60个基点，欧洲市场的收窄幅度甚至更大。这似乎印证了一个月前某外资投行提出的判断：“利率在走高，但还不足以实质性破坏固定利率信用市场。”\n\n这个判断至今仍然成立。但真正的问题不是它还能成立多久，而是当它不再成立时，市场会以何种方式、在什么触发条件下完成定价调整。\n\n这份最新发布的全球策略研报提供了一个关键框架：信用利差对利率的免疫不是无限的，它有一个清晰的阈值。而在阈值之外，市场还面临一个更根本的结构性问题——当前利差的压缩已经接近极限，即使利率回落，利差也难以进一步收窄。\n\n这意味着，未来几个月的核心交易不是“赌方向”，而是理解三种不同情景下的不对称性。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 利差对利率的免疫不是永久的，关键阈值在2.65%-2.75%的盈亏平衡通胀率\n\n信用市场之所以能在利率上行中保持韧性，核心原因在于利率上行的“成分”此前是良性的。最初美国10年期收益率的上升主要由实际利率和期限溢价驱动，而非通胀预期或政策前景的根本性转变。这种成分差异解释了为什么利差没有同步走阔。\n\n但研报的数据显示，这一成分正在发生变化。长期通胀预期在经历了短暂回落后，开始重新走高。虽然目前仍低于2.5%，但方向性的转变值得警惕。\n\n报告提出了一个清晰的量化门槛：当美国5年期盈亏平衡通胀率进入2.65%-2.75%区间时，投资者将开始质疑通胀控制的有效性，进而质疑当前政策路径的可信度。这个阈值之所以重要，不是因为它是某个统计上的极端值，而是因为它代表了一个心理拐点——市场会从“通胀可控”的叙事切换到“政策可能落后于曲线”的叙事。\n\n这一判断的深层\n\n[... middle omitted ...]\n\n详细的数据图表、行业层面的利差分析、以及具体的交易执行建议。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n利率涨了，信用利差为何不慌？\n\n利差还能收窄吗？\n\n三个场景，三种应对思路\n\n最近利率上行不少，但信用利差（IG/HY）反而在收窄，美、欧分别收窄了17-69bp。很多人问：为什么利率涨了，信用市场没反应？\n\n背后的逻辑其实不复杂👇\n\n1️⃣ 涨的是“实际利率”，不是“通胀预期”\n早期这波利率上行，主要由实际利率和期限溢价驱动，不是市场在担心通胀失控。只要通胀预期还在2.5%以下，对信用市场的冲击就有限。\n\n2️⃣ 基本面+技术面撑住了\n“不太热也不太冷”的通胀环境，支撑了名义盈利增长。同时系统流动性充裕，海外资金还在持续买入高收益率的信用债，形成买盘支撑。\n\n3️⃣ 但拐点可能不远了\n供应链压力指标在3-4月飙升1.2个标准差，是2020年7月以来最大涨幅。如果通胀预期突破2.65-2.75%，市场可能开始质疑政策可信度，信用利差会非线性走阔。\n\n4️⃣ 利率如果回落，利差还能再收窄吗？\n研报判断：空间有限。原因：\n- 美国IG/HY利差已处于近10年2%-3%分位\n- 机构持仓接近历史高位（标普500期货多头在95%分位）\n- CTA也已做多信用，历史上这类位置后续收窄空间不大\n\n5️⃣ 三个场景，三种应\n\n[... middle omitted ...]\n\ns rallied 18/69bp in Europe, rates volatility still remains elevated at \\~1.5std above its 1y avg. Despite renewed headlines of a US-Iran deal (echoing March), we see risks in rates as two-sid\n\n[... middle omitted ...]\n\nperty rights. © UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.\n\n![](images/3e72da55dee36c3d8d686dce6df0643027af10429a933e5a46a1fe0bb9882146.jpg)\n\n## UBS"
  },
  {
    "id": "R002",
    "title": "市场真正低估的不是风险，而是风险定价的切换时机",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是风险，而是风险定价的切换时机\n\n过去几个月，全球风险资产在伊朗冲突持续悬而未决、地缘溢价反复波动的背景下，依然走出了令人意外的韧性。AI资本开支周期、能源库存管理的超预期表现、以及市场对霍尔木兹海峡问题最终解决的乐观预期，共同支撑了高贝塔、高利差货币和权益资产的强势。然而，一份来自某外资投行外汇策略团队的最新报告，正在向市场传递一个微妙但重要的信号：风险情绪已经从“绿灯”转向“黄灯”。\n\n这份报告的核心判断并非看空风险资产，而是认为当前低波动率的环境，恰恰是加仓下行保护的战术窗口。真正值得关注的，不是市场是否即将崩盘，而是风险定价的结构正在发生变化——那些在上涨周期中被视为理所当然的“好交易”，在情绪切换后可能呈现出完全不同的损益特征。报告特别指出，近期频繁出现的“股跌债也跌”场景，正在改变外汇市场的传统避险逻辑，而这一点，大多数投资者尚未充分定价。\n\n以下是对这份报告核心逻辑的拆解与延伸。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 情绪指标集群闪烁，但尚未构成趋势反转的充分条件\n\n报告通过多个独立维度的指标，描绘了一个正在从“积极”转向“脆弱”的风险环境。这些指标各自都不足以单独触发卖出信号，但它们的同步出现，大幅提高了市场脆弱性的概率。\n\n首先是Citi内部开发的POLLS指标——一个综合了仓位、乐观情绪、流动性、杠杆和压力五个维度的情绪监测工具。该指标上周触及18，这一数值在历史经验中通常出现在市场修正之前。量化全球宏观团队的分析显示，在POLLS触发这一阈值后，标普500指数未来30至50个交易日的回报分布明显偏弱。\n\n其次是期权市场的极端信号。CBOE股票看跌/看涨比率跌至过去十年罕见低位，标普500指数一个月的偏斜度同样显示出强烈的看涨期权需求。这意味着市场已经通过期权建立了\n\n[... middle omitted ...]\n\n会持续跟踪这些关键变量的变化，并在第一时间分享更新后的判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n风险信号从绿转黄\n\n⚠️ 风险预警\n\n市场情绪正在微妙变化，短期修正概率上升\n\n某外资投行最新研报指出，虽然全球风险资产过去几个月表现强劲（AI资本开支、伊朗冲突预期缓和等支撑），但多个信号显示市场正从“积极风险偏好”转向“修正脆弱性增加”。这不是说要立刻看空，而是波动率低位时值得加一点防御。\n\n1/ 为什么情绪在转黄？\n\n- **权益策略团队**：Q1财报季涨幅已定价了“狂热预期”，建议止盈动量因子，转向盈利改善和高质量标的。\n\n- **POLLS风险指标**（仓位、乐观度、流动性、杠杆、压力）上周触及18，历史上前几次触发后30-50个交易日标普500表现偏弱。\n\n- **财报季结束**：等权标普500在非财报季几乎没涨，宽基涨幅全靠财报季推动。这个“顺风”刚消失。\n\n- **成分股波动极端分化**：个股vs指数波动率比值超过2.5，历史经验是市场随后横盘或走低。\n\n- **AI叙事有裂痕**？研报仍看好AI资本开支，但近期企业AI成本相关新闻（5/28）可能影响终端支出节奏。\n\n- **看跌期权持仓极低**：CBOE看跌/看涨比率创近十年低点，市场过于乐观。一旦转向，追买看跌期权会放大波动。\n\n- **\n\n[... middle omitted ...]\n\n produces very different FX behavior compared to equities down with yields down. We like JPY strangles for that uncertainty. Another complication is that historic risk currencies tend to also \n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R003",
    "title": "世界杯的真正经济账：情绪溢价远超GDP脉冲",
    "digest": "[wechat_article.md]\n# 世界杯的真正经济账：情绪溢价远超GDP脉冲\n\n如果你只关注世界杯对东道国GDP的拉动，你可能已经错过了这份报告最核心的判断。\n\n某外资投行在最新发布的研报中，用严谨的计量经济学方法，拆解了一个困扰产业界和投资者多年的问题：世界杯这样的超级商业事件，到底能为东道国带来多少真实的经济增量？结论相当克制——甚至可以说，是给所有期待“赛事经济”带来结构性增长的人泼了一盆冷水。\n\n报告分析了1982年以来11届世界杯东道国的GDP表现，使用双重差分法对比了50个发达和新兴经济体。结果发现：世界杯举办当年，东道国实际GDP确实出现了一个边际正效应，但这一效应在统计上并不显著。更关键的是，长期效应几乎为零。\n\n这不是说世界杯没有经济价值。恰恰相反，报告揭示的真正价值，藏在另一个更难以量化的维度里——人们愿意为“赢”和“参与”支付的溢价，远远超过那些被反复计算的基础设施和旅游收入。\n\n对于正在为2026年美加墨世界杯做准备的企业决策者和投资者而言，真正需要思考的问题不是“赛事能带来多少GDP”，而是“哪些商业价值被GDP统计遗漏了，而这些遗漏恰恰是超额收益的来源”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 东道国的GDP“脉冲”更像一场统计幻觉\n\n历届世界杯东道国的经济表现，揭示了一个令人不安但必须面对的事实：GDP数据上的“世界杯效应”极不稳定，且无法被系统性验证。\n\n报告使用的样本涵盖了从1982年西班牙到2022年卡塔尔的11届赛事。东道国的GDP表现呈现巨大的离散度——1998年法国世界杯期间经济强劲，但1986年墨西哥世界杯期间经济疲弱，2022年卡塔尔则因为能源价格波动出现极端波动。这种高度异质性意味着，很难将GDP波动归因于世界杯本身。\n\n更深层的原因在于三个结构性限制。\n\n第一，只有很小一部分经济收益会\n\n[... middle omitted ...]\n\n是一笔带过，但在深度讨论中，它们往往才是真正的超额收益来源。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n世界杯的经济账：生意很大，宏观很小\n\n🌍 世界杯≠经济强心针\n\n世界杯确实是全球最大的商业赛事。2026年将有48支球队、104场比赛，北美三国的总场馆容量达720万。但投行研报发现：它对东道国经济的拉动，远没有想象中那么大。\n\n1/ 商业效应≠宏观效应\n- 啤酒、球衣确实卖得更好，但大部分消费发生在非东道国\n- 即使在美国买，很多也是进口商品，利润流向海外\n- 游客消费可能只是替代了其他支出，并非增量\n\n2/ 历史数据怎么说？\n研究对比了1982年以来11届世界杯东道国的GDP表现：\n- 赛事当年GDP有微弱正向影响，但统计上不显著\n- 长期来看，影响几乎为零\n- 获胜国的短期提振稍强（平均跑赢全球市场3.5%），但三个月后明显消退\n\n3/ 为什么？三个关键原因\n- 经济规模越大，赛事冲击越小（美国GDP占全球26%，而卡塔尔仅0.2%）\n- 支出可能只是“今天花明天省”\n- 普通游客可能因拥挤和涨价而避开主办城市\n\n4/ 换个角度看价值\n如果算“心理账”呢？调查显示：\n- 2014年世界杯期间，德国人平均愿意支付23欧元让国家队夺冠\n- 美国人愿意为提升国家队实力的项目多交税\n- 这种“愿意支付”的金额，\n\n[... middle omitted ...]\n\nitality, and beverages. Our Equity analysts expect that the main sector beneficiaries will include European and US Consumer Staples, European Consumer Discretionary, US Retail, US Lodging and \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R004",
    "title": "美国投资级债券市场真正被低估的，是AI基建融资的“再定价效应”",
    "digest": "[wechat_article.md]\n# 美国投资级债券市场真正被低估的，是AI基建融资的“再定价效应”\n\n当前市场对投资级信用债的判断，普遍陷入一个误区：认为利差已处于历史低位，上行空间有限，风险回报不佳。但这份来自某外资投行的最新研报揭示了一个被广泛忽视的结构性力量——AI基础设施的融资需求正在从根本上重塑投资级债券市场的供需格局。报告的核心判断是：**利差仍有压缩空间，不是因为宏观风险被低估，而是因为供给端的结构性变化正在改变定价机制。** 这一判断，对于所有配置固定收益资产的决策者而言，都值得重新审视。\n\n为什么现在重要？2026年初，美国投资级债券利差约为96个基点，收益率在5.4%附近。从历史看，这个利差水平确实不便宜。但研报指出，市场忽略了三个正在发生的深层变化：投资级市场的存量增速正处在20年来的最低点；AI相关债务已占整个指数的14.8%，成为事实上最大的“单一行业”；而未来五年到期的债券规模处于高位，再融资需求与新增融资需求叠加，将产生一个前所未有的供给冲击。这不是周期性的波动，而是结构性的重置。\n\n以下，我们从这份报告中提炼出五个关键洞察，并逐一展开其含义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 利差压缩的真正驱动力不是宏观乐观，而是供给侧的“被动收紧”\n\n很多投资者将当前利差偏紧归因于对经济软着陆的过度乐观。但研报的数据提供了另一种解释：投资级债券市场的存量增速正在显著放缓。过去二十年中，市场规模的年化增速通常在5%至15%之间波动，而当前这一增速已降至接近零的水平。换句话说，不是需求太强，而是新增供给太少。\n\n同时，研报显示，美国国债在彭博综合指数中的占比持续上升，这本身就在压低公司债的相对利差。因为指数投资者必须被动配置更多国债，而对公司债的需求相对减少，但公司债的净供给却在下降——这两个力量共同作用，使得现有的公\n\n[... middle omitted ...]\n\n研报的原始图表和关键数据点，并围绕这些未解问题进行深度推演。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美国高评级债还能更紧吗？\n\n📌 信用利差还有压缩空间\n\n某外资投行最新研报给2026年底高评级债（HG）的信用利差预测是85bp，比当前96bp收窄11bp，总回报预计+4.5%。\n\n**1/ 基本面强，但不确定性挡了“动物精神”**\n美国经济仍在超预期增长，但政策不确定性指数飙升。这种矛盾导致企业高管不敢大举扩张，反而强化了信用基本面。\n\n**2/ 利差虽紧，但收益率依然有吸引力**\n当前HG债收益率约5.4%，历史上这个水平往往能吸引强劲需求。利差从年初85bp低位反弹到96bp，但研报认为会重新收窄。\n\n**3/ AI数据中心是“超大融资事件”**\nAI相关债务已占整个HG指数的14.8%，超过美国银行板块。预计2026-2030年数据中心年资本支出从600亿增至1400亿美元，其中很大比例通过债券市场融资。\n\n**4/ 地缘冲突影响有限，除非美联储加息**\n历史复盘显示，地缘事件对信用利差的影响取决于当时联储的政策方向。联储降息/暂停时，冲突后利差平均收窄；加息时则走阔。\n\n**5/ 国债占比上升，压缩了信用利差**\n美国综合债券指数中国债占比持续提高（目前约45%），这从结构上压低了企业债利差。\n\n[... middle omitted ...]\n\nty lights and a distant skyline (no visible text or symbols)\n</details>\n\n# HG Forecast: Expecting spreads to tighten with moderate total and excess returns\n\nOur spread forecast is 85bp, return\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R005",
    "title": "中国智能手机市场真正超预期的不是需求下滑，而是涨价传导的断裂",
    "digest": "[wechat_article.md]\n# 中国智能手机市场真正超预期的不是需求下滑，而是涨价传导的断裂\n\n2026年4月，中国智能手机出货量跌至16M台，创下2021年9月以来的最低点。这份来自某外资投行的月度追踪报告，数据本身并不出人意料——市场对需求疲软已有预期。真正需要投资者重新校准认知的，是报告揭示的一个结构性信号：内存成本上涨的压力正在从低端市场向中端市场蔓延，而终端涨价策略遭遇了明显的市场抵抗。这不是一次简单的周期波动，而是产业链定价权的重新分配。\n\n四月数据中，中端市场出货量从三月的同比增长16%骤降至同比下滑16%，这一剧烈反转的时间点，恰好与三月下旬终端提价的时间窗口重合。低价市场继续萎缩，同比下滑22%；唯有高端市场保持23%的增长。市场的分层不再是简单的消费降级故事，而是成本压力下，不同价格带的消费者对涨价的接受度出现了根本性分化。\n\n更值得关注的是，部分代工厂和元器件供应商在四月却交出了好于预期的业绩。这份报告提出了一个关键的假设：这可能是渠道补库存带来的短期数据扭曲，真正的压力可能推迟到2026年下半年或2027年上半年才会在供应链上游显现。如果这一判断成立，那么当前市场上对某些半导体标的的乐观情绪，可能建立在一个尚未被验证的时间差之上。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 中端市场的突然崩塌是验证涨价阻力的关键信号，而非需求本身的恶化\n\n四月数据中最值得拆解的结构性变化，是中端市场（人民币2000-5000元价位段）的出货量走势。该市场在三月还录得16%的同比增长，四月却急转直下至同比下滑16%。这一反转的幅度和速度，在近年来的月度数据中极为罕见。\n\n报告指出，这一变化“likely reflecting the impact of handset price increases implemented in l\n\n[... middle omitted ...]\n\n在群内分享完整的报告原文，并定期组织对关键假设的拆解和辩论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n手机涨价潮，中端先扛不住了\n\n**中端失守**\n\n4月中国手机出货创近6年新低\n\n---\n\n某外资投行最新研报显示，4月中国手机出货量环比跌15%、同比跌10%，仅1600万台，是2021年9月以来的最低点。1-4月累计出货同比缩水7%。\n\n核心原因：存储芯片涨价开始传导至中端机型。\n\n**三个关键信号👇**\n\n1️⃣ **涨价传导路径清晰**\n- 低端机（<2000元）：同比跌22%，持续疲软\n- 中端机（2000-5000元）：从3月的+16%急转直下到-16%\n- 高端机（>5000元）：依然涨23%，受影响最小\n\n研报判断，3月底开始执行的涨价是导致中端断崖的主因。\n\n2️⃣ **涨价不被市场接受**\n4月手机均价同比涨16%，但出货量明显落后于厂商出货量，说明消费者对涨价不买账。马上\"618\"大促，研报预期涨价势头会放缓，厂商要在价格和销量之间找平衡。\n\n3️⃣ **华为的\"黑科技\"能破局吗？**\n华为Mate 80 Pro Max用上SMIC N+3工艺的麒麟9030，但高端出货量没明显提升。5月底华为发布\"LogicFolding\"和\"Tau Scaling Law\"，号称2031年将差距缩小到\n\n[... middle omitted ...]\n\n33ab3565d0b9f5099184a35b2d5c2dc54478390.jpg)\n\nAlex Wang, CFA\n\n+852 2123 2613\n\nalex.wang@bernsteinsg.com\n\n![](images/43ab484b407fc0c8348935481e45dd3c1a808bf5ef03c205bde16f92d9762d74.jpg)\n\nEunic\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R006",
    "title": "美国经济正在经历一场“数据悲观、基本面不差”的罕见错位",
    "digest": "[wechat_article.md]\n# 美国经济正在经历一场“数据悲观、基本面不差”的罕见错位\n\n如果你只读新闻标题，2026年的美国经济几乎无可救药——政策不确定性指数飙升至540，消费者信心跌至半个世纪以来的最低点附近，专业预测者认为衰退的概率持续高企。然而，某外资投行最新发布的这份经济展望报告，却给出了一个与市场情绪几乎相反的核心判断：美国经济仍在增长，企业利润创下历史新高，而真正的结构性变量——生产率——正在经历互联网时代以来最好的表现。\n\n这不是一个简单的“市场悲观过度”的故事。报告揭示了一个更深层的错位：宏观情绪指标与微观经济基本面之间的裂痕，正在重塑资产定价的逻辑。理解这个裂痕，比判断下一次降息时点更重要。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 消费者信心与真实支出之间的鸿沟，是2026年最被低估的宏观特征\n\n报告用三张图表清晰地展示了这个矛盾。密歇根大学消费者信心指数在2024年调整了调查方法后，读数已跌至接近疫情初期的水平。Conference Board的消费者信心指数虽然相对温和，但整体方向同样指向悲观。与此同时，经济政策不确定性指数在2025年飙升至540，远超2020年疫情冲击时的500。\n\n但报告紧接着展示了一个关键事实：实际GDP和国内私人最终销售（domestic private final sales）在过去两年持续正增长，且某外资投行预测这一趋势将继续，尽管同时承认衰退风险偏高。\n\n这意味着什么？消费者“感觉”到的经济，与消费者“实际在做”的经济，出现了罕见的分裂。这种分裂不能简单用“统计滞后”来解释。更合理的解读是：消费者的悲观情绪主要来自对政策不确定性和通胀粘性的焦虑，而非实际收入或就业状况的恶化。报告中的就业成本指数（ECI）显示，工资增速虽然从2023年的5.1%高点回落至3.2%，但仍高于201\n\n[... middle omitted ...]\n\n始图表和更多维度的交叉分析，也会持续跟踪这些关键假设的变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美国经济到底还行不行？看这份拆解\n\n封面：经济韧性背后的真相\n\n副标题：就业慢、通胀黏，但AI撑住增长\n\n📌 最近新闻都在说政策不确定性飙升，消费者信心也跌到历史低位附近。但实际数据告诉我们：经济还在走，只是节奏变了。\n\n1️⃣ 就业市场：慢但稳\n- 人口增长放缓+移民减少，导致私人部门就业增速很慢。2025年同比仅增0.5%左右。\n- 好消息是：失业率可能已经见顶，工资增速放缓幅度有限。研报预计后续就业成本指数（ECI）维持在3%上下。\n\n2️⃣ 生产力爆发是隐藏王牌\n- 当前非农企业生产率增速是互联网普及以来最好的一轮，12个季度年化增速接近2.5%。\n- 这意味着：即使就业增长慢，经济产出仍能靠效率提升来支撑。\n\n3️⃣ 企业盈利依然强劲\n- 国内非金融企业税前利润率维持在18%左右，处于历史高位。\n- 2026年标普500盈利预期从年初至今已上修约7.5%。\n\n4️⃣ 通胀回落慢，美联储转向谨慎\n- 核心PCE通胀还在3%以上，PPI和进口价格也在反弹。\n- 市场目前预期：首次加息可能在2027年9月——比年初时的降息预期大幅逆转。\n\n5️⃣ AI是资本开支的最大推手\n- 全球半导体销售2026年预计\n\n[... middle omitted ...]\n\nIndex; last point is April 2026   \n![](images/ed96e7b0de8256fc7e1ddc7945af0e07214219573376f1b554ad0997e10b0c79.jpg)\n\n<details>\n<summary>line</summary>\n\n| x    | y     |\n| ---- | ----- |\n| 85\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R007",
    "title": "瑞士手表出口的-17%不是需求危机，而是全球定价体系的一次压力测试",
    "digest": "[wechat_article.md]\n# 瑞士手表出口的-17%不是需求危机，而是全球定价体系的一次压力测试\n\n四月瑞士手表出口同比下滑17%，这个数字看上去像一记重拳。但真正值得关注的不是这个两位数跌幅，而是它背后的结构性分化。某外资投行的最新研报提供了一个关键视角：剔除美国和中东市场后，世界其他地区的出口实际增长了5%。换句话说，全球高端腕表的需求并没有崩塌，只是贸易政策、地缘政治和渠道库存的叠加效应，正在对品牌定价权和区域战略进行一次残酷的分层检验。\n\n这份报告的价值不在于告诉你4月数据有多差，而在于它拆解了“17%”这个数字里哪些是噪音，哪些是信号。对于关注奢侈品行业和高端消费的决策者来说，当前最需要回答的问题已经不是“需求到底还在不在”，而是“你的定价权能否扛过这一轮区域重构”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 真正的需求底色比表面数字健康得多，但前提是你知道如何剥离关税噪音\n\n4月-17%的同比数据，放在任何语境下都足够引起警觉。但报告明确指出，这个数字被一个巨大的基数效应扭曲了。2025年4月，美国在关税政策宣布后出现了约150%的异常出口增长，导致今年4月的比较基数被严重抬高。剔除这个因素后，美国市场实际同比下滑56%，这当然不是好消息，但已经不是一个体系性崩塌的信号。\n\n更关键的是，除去美国和中东，世界其他地区在4月实现了5%的同比增长，而3月这个数字只有1%。这组对比说明，全球高端腕表的消费基础并没有被削弱，只是资金流向和渠道库存正在被政策扰动重新分配。对于品牌而言，这意味着你的全球布局是否足够分散，直接决定了你在宏观波动中的韧性。\n\n这里需要特别关注的是中东市场。报告提到中东出口同比下降11%，但相比3月的-21%已有明显改善。然而研报同时提醒，中东地缘政治风险对欧洲旅游消费的溢出效应仍不可忽视。换句话说，中东的改\n\n[... middle omitted ...]\n\n其他行业研究者的交叉验证。这里不做广告，只做深度讨论的延伸。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n4月瑞士表出口大跌17%？别急，拆开看有彩蛋\n\n📉 数字吓人？先看原因\n\n4月瑞士手表出口同比-17%，比3月的-1%大幅恶化。但别被表面数字吓到——这主要是2025年4月美国宣布关税后，对美出口暴增约150%带来的高基数效应（约16个百分点的拖累）。\n\n📊 拆开看，真实需求其实在回暖\n\n1️⃣ 剔除美国（-56%，占出口约17%）和中东（-11%，占约10%），全球其他地区4月同比增长+5%，比3月的+1%明显改善。两年复合增速-3%，也比3月的+2%略弱，但整体趋势向好。\n\n2️⃣ 大中华区表现亮眼：4月同比增长+15%（3月仅+2%），其中中国大陆+17%，香港+14%，主要得益于低基数效应。\n\n3️⃣ 日本依旧疲软（-12%），本地和游客需求都偏弱。\n\n4️⃣ 欧洲（-2%）较2月的+7%有所回落，法国市场仍受平行渠道（代购等）影响，数据有失真。\n\n⚠️ 需要关注的潜在风险\n\n研报提示：中东局势可能溢出影响欧洲旅游客流，进而波及欧美消费者信心。这是后续观察的重点。\n\n💡 一点思考\n\n奢侈品行业数据波动大，单月解读需要结合基数和区域结构。4月看似惨淡，但剔除扰动项后，核心市场（除美国、中东）其实在温和复\n\n[... middle omitted ...]\n\ns.+2% in March). Greater China improved further (+15% YoY vs.+2% in March/-2% in Jan+Feb) in both Mainland China (+17% vs. +4% March/-3% Jan+Feb) and Hong Kong (+14% vs.+1% in March/-1% Jan+Fe\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R008",
    "title": "香港零售复苏的真正信号：不是奢侈品反弹，而是超市租金企稳",
    "digest": "[wechat_article.md]\n# 香港零售复苏的真正信号：不是奢侈品反弹，而是超市租金企稳\n\n四月香港零售数据出炉，同比增长8.6%，延续了一季度以来的复苏态势。表面上看，这组数字延续了3月13%和一季度12%的强劲增长。但真正值得决策者关注的，不是整体数字的亮眼，而是结构内部正在发生的两个重要变化：奢侈品增速从28%回落至20%，而超市品类从几乎零增长回升至3%的正增长。\n\n某外资投行最新发布的香港地产研报，通过四月的零售细分数据，揭示了一个容易被市场忽略的判断：香港零售物业的定价逻辑正在发生切换。过去两年，市场围绕“高端消费回流”定价奢侈零售物业；而现在，非必需消费的增速放缓与必需消费的企稳，正在重塑不同类别零售资产的投资价值。\n\n这份报告的核心贡献不在于给出了四月数据，而在于它把零售销售额的变化，转化为对具体地产公司资产价值的重新评估。对于持有香港零售物业的投资者而言，这组数据意味着资产定价的锚点正在移动。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 奢侈品增速放缓不是疲态信号，而是基数效应的正常回归\n\n四月珠宝钟表及贵重礼品类别同比增长20%，相比一季度的28%有所回落。这一变化很容易被解读为消费信心转弱，但报告中的历史数据提供了更准确的参照系。\n\n从2025年全年走势来看，奢侈品零售在2025年上半年仍处于同比负增长区间，直至2025年6月才转正。从2025年6月的6.9%起步，逐月攀升至2026年2月的高点31.1%。因此，进入2026年二季度后，同比基数显著抬升。四月20%的增速，放在这个基期背景下，实际上是增长动能的延续，而非逆转。\n\n更值得关注的变量是港币兑人民币汇率。报告指出，2026年前五个月港币兑人民币已贬值约4%。从历史相关性来看，港币贬值与香港零售销售额之间存在显著的正向关系。这意味着汇率因素仍在为香港零售提供结\n\n[... middle omitted ...]\n\n报告的原始图表、估值模型，以及我们对后续数据的持续跟踪解读。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n香港零售4月增速放缓，超市露出企稳信号\n\n封面：零售增速放缓\n封面副标题：超市租金开始企稳\n\n📊 香港4月零售数据出炉：同比+8.6%，虽然还是正增长，但比3月的+13%和Q1的+12%明显降温。\n\n奢侈品增速回落至+20%（Q1是+28%），主要受高基数效应和金价下行影响。超市反而开始企稳，同比+3%（Q1是+2%），部分靠运营商加大促销支撑。\n\n线上零售维持强劲势头，同比+31%，占整体零售额比重已升至10%。\n\n1️⃣ 5月展望：黄金周游客同比+8%，其中内地游客+10%，加上港币对人民币年内贬值约4%，对零售有一定支撑。但考虑到去年5-6月市场情绪回暖带来的高基数，预计5月零售增速将放缓至5-8%。\n\n2️⃣ 值得关注的信号：非必需消费零售的租金开始企稳（比如超市），这可能是行业触底的早期指标。\n\n3️⃣ 对零售地产的观察：\n- 某REIT近期因租金企稳和转向“卖出回购”模式被上调评级\n- 高端零售面临下半年同店销售增速回落压力，但部分标的6.5%的股息率开始吸引收益型资金\n- 核心商场的租户销售表现优于整体市场\n\n整体来看，香港零售正在经历从高速复苏向温和增长的过渡期，分化在加剧——线上跑赢线下，必\n\n[... middle omitted ...]\n\n+31%yoy, now accounting for 10% of total retail sales value amid shifted purchasing habit.\n\nMay data supported by Golden Week tourism (+8%yoy); beware of upcoming higher comparable base — We e\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R009",
    "title": "日经年底突破70000点：市场低估的不是需求，而是日本企业定价权的结构性转折",
    "digest": "[wechat_article.md]\n# 日经年底突破70000点：市场低估的不是需求，而是日本企业定价权的结构性转折\n\n过去一个月，日本股市在短期调整中保持了韧性。日经225与TOPIX先后创下年内新高。但真正值得关注的，不是指数还能涨多少，而是支撑这一轮上涨的底层逻辑正在发生变化。\n\n某外资投行最新发布的日本权益策略报告，给出了一个看似矛盾但逻辑自洽的判断：短期见顶，年底前日经225将突破70000点。这并非简单的看多口号，而是一个基于企业盈利韧性、估值重构和资金流向的结构性叙事。报告的核心主张是：市场尚未充分定价日本企业从“通缩生存模式”向“通胀定价模式”转换过程中，ROE中枢上移对估值的系统性拉动。\n\n这不是一个关于周期复苏的故事。这是一个关于企业行为范式转移的故事。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 企业盈利指引的“保守”本身就是乐观信号\n\n每年财报季，市场习惯性地将公司指引与共识预期之间的差距解读为“低于预期”或“高于预期”。但这份报告提供了一个更精细的观察框架：指引的“保守程度”本身就是一个关键信号。\n\n数据显示，在FY2026（截至2027年3月）的公司计划中，TOPIX成分股营收增长目标为4.2%，净利润增长目标为7.6%。这些数字乍看并不惊艳。但放在当前宏观背景下——中东局势不确定、成本广泛上升——这样的指引实际上相当强劲。\n\n更关键的发现藏在细节里。公司计划与共识预期之间的差距，无论是营收、营业利润还是净利润，都处于历史平均水平附近。这意味着，在高度不确定的宏观环境下，企业并没有采取比以往更保守的指引策略。这本身就暗示企业管理层对自身盈利能力的信心。\n\n报告还揭示了一个重要结构：62%的公司营收指引超过了此前市场共识。这组数据直接指向一个判断——日本企业正在系统性地将成本上涨转嫁给下游客户。这不是个别行业的定价行为，\n\n[... middle omitted ...]\n\n善和资金流向的变化，并在群内分享更详细的图表分析与情景推演。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日股还能不能追？外资投行最新判断来了\n\n📈短期有回调，年内仍看多\n\n最近日股表现挺稳，虽然中间有调整，但外资投行认为：\n1️⃣ 市场在等中东停火+原油见顶\n2️⃣ AI和半导体全球热浪持续\n3️⃣ 企业发布的FY26指引整体偏保守但合理\n\n👉 短期可能高位震荡，但年内日经有望突破70000点\n\n📊 企业盈利韧性比想象中强\n\nTOPIX企业FY26计划：\n- 营收增长 +4.2%\n- 净利润增长 +7.6%\n\n在中东不确定性和成本上涨背景下，这个数字算不错了。\n尤其AI/半导体利润增长突出，是整体盈利的“发动机”。\n\n📌 估值还有空间\n\n当前TOPIX 12个月远期PE约16.8倍，接近过去十年高位。\n但研报认为PE还能继续扩张，原因：\n- 通胀环境下利润率改善→ROE有望升至11-12%\n- 全球流动性宽松\n- 低ROE公司减少，市场结构变好\n- 日股相对全球仍偏便宜\n\n目标：TOPIX 4500点（对应FY27 EPS ¥258.4 × PE 17.5倍）\n\n⚠️ 短期注意两点\n\n1️⃣ 利率上升风险：如果长期利率因财政担忧快速上行，可能变成“坏利率上涨”\n2️⃣ 市场风格：目前动量股集中在科技，后续可能扩\n\n[... middle omitted ...]\n\nboom, but also TOPIX recently hit YTD highs, and that earnings revision deterioration is expected in the immediate future, Japanese equities may peak for a while in the short term. However, we\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R010",
    "title": "服务业的真实扩张信号，被市场低估了",
    "digest": "[wechat_article.md]\n# 服务业的真实扩张信号，被市场低估了\n\n五月的经济数据陆续出炉，市场目光仍高度聚焦在制造业和出口的边际变化上。然而，一份来自某外资投行最新发布的研报，揭示了一个更值得关注的信号：中国服务业PMI在5月出现明显跃升，且其改善的广度正在扩大。这不是一次简单的季节性反弹，而是可能在为下半年的经济结构再平衡埋下伏笔。\n\n这份研报的核心判断是：服务业活动正在加速，且新订单、就业、新出口业务等多个分项同步改善。市场当前的讨论焦点，或许低估了这一轮服务业扩张的持续性和对整体经济的支撑意义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 五月服务业PMI的跃升，并非孤立的数字跳动\n\n研报数据显示，5月中国服务业PMI从4月的52.6上升至54.4，不仅高于某外资投行预测的52.8，也显著超出彭博共识预期的52.2。54.4这个读数，是过去几个月以来的高位。\n\n更关键的是，这不是一个孤立的头部数据。新业务指数从52.6升至53.3，就业分项从49.7的收缩区间重返50.4的扩张区间，积压业务指数从50.3升至51.8，新出口订单指数更是从49.7跃升至51.5。这些分项的同时改善，意味着服务业的回暖并非仅仅来自个别行业的拉动，而是呈现出广泛的、需求驱动的特征。\n\n对于产业决策者而言，这意味着消费服务领域的内生动力正在增强，而非依赖政策刺激的短期脉冲。如果这一趋势延续，服务业将成为对冲制造业外需波动的重要稳定器。\n\n## 2. 就业分项重返扩张，是当前最具意义的信号\n\n在所有分项中，就业指数从49.7回升至50.4，值得单独讨论。服务业是中国吸纳就业的最大容器，其就业指数的扩张，直接关系到居民收入预期和消费信心的修复。\n\n过去几个季度，市场对“就业压力”的讨论从未停歇。服务业PMI就业分项长期处于50的荣枯线附近徘徊，令市场对消费\n\n[... middle omitted ...]\n\n时会传导至终端价格？这些问题的答案，可能比你想象的更早揭晓。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月服务业PMI踩了脚油门\n\n服务业回暖了\n\n读数升至54.4，比上月高\n\n---\n\n最近某外资投行发布了5月中国服务业PMI数据，简单拆解一下，信息量还挺大。\n\n1️⃣ 整体数据明显回暖\n5月服务业PMI录得54.4，高于4月的52.6，也超过了市场预期的52.2。说明服务业活动在加速扩张，不是小幅修复，是踩了脚油门。\n\n2️⃣ 新订单和就业都在改善\n新业务指数从52.6升至53.3，就业指数从49.7回到50.4，重新回到扩张区间。积压业务量也在上升，说明需求确实在走强。出口新订单指数从49.7跳升至51.5，海外需求也在恢复。\n\n3️⃣ 成本涨了，但售价没涨\n投入价格指数从51.1升至52.0，企业提到油价、采购成本和工资都在涨。但产出价格指数只从49.7微升至49.9，依然低于50。说明企业选择了自己扛成本，利润空间还在被压缩。\n\n4️⃣ 企业怎么说的？\n受访公司提到，新业务增长主要来自客户需求增加、业务创新和扩张、新客户获取、市场环境改善以及新项目开发。整体态度偏积极。\n\n服务业在5月确实有一波加速，但成本压力没完全传导出去，利润端还需要继续观察。\n\n你们觉得下半年服务业能维持这个节奏吗？欢迎一起讨\n\n[... middle omitted ...]\n\n to 50.4 in May (vs. 49.7 in April), and the outstanding business index rose to 51.8 in May (vs. 50.3 in April). The new export orders sub-index rose to 51.5 in May (vs. 49.7 in April). Survey\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R011",
    "title": "2026年软件与AI市场的真正主线：不是模型竞赛，而是“Token路径”上的基础设施定价权",
    "digest": "[wechat_article.md]\n# 2026年软件与AI市场的真正主线：不是模型竞赛，而是“Token路径”上的基础设施定价权\n\n市场正在经历一场静默但深刻的结构性转移。过去两年，围绕大语言模型的讨论集中在参数规模、训练成本和能力边界上。但2026年第一季度的产业信号表明，价值创造的重心正在从“谁有更好的模型”转向“谁能承载和管控模型运行产生的Token洪流”。某外资投行在最新的软件、互联网与AI大会纪要中，提炼出一个关键判断：赢家是那些处在“Token路径”上的公司。这一判断并非简单的行业观察，而是对资产定价逻辑的重构。\n\n这份报告覆盖了超过十家核心上市公司和多家私有企业的管理层交流。我们从中提取了五个值得产业决策者和投资者认真对待的洞察。它们共同指向一个结论：市场当前对AI的定价，可能低估了基础设施层企业的盈利韧性和应用层企业所面临的“定价权真空”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 推理需求的崛起正在重塑基础设施公司的盈利模型，而市场仍以训练周期框架来定价\n\n报告中最具说服力的信号来自一家AI计算基础设施公司。管理层明确表示，当前大部分需求已转向推理工作负载，而非训练。这一转变的意义在于：推理需求具有更强的持续性和更低的波动性。当企业客户看到AI项目产生可量化的回报后，他们更倾向于持续采购推理算力，而非一次性训练算力。\n\n这意味着，市场此前担忧的“训练资本开支见顶”叙事，可能忽视了推理需求的长期支撑。更关键的是，这家公司通过合同签署时锁定收入和大部分成本结构，建立了高度可预测的贡献利润率。每份新合同都基于当前容量成本定价，使得公司能够将投入成本变化传导给客户，从而保持各笔交易的利润率一致性。\n\n报告中提到，该公司的EBIT利润率预计将在2026年底达到低双位数，而成本端的改善——包括加权平均资本成本在过去几年下降约600个基点\n\n[... middle omitted ...]\n\n的原始报告图表和纪要原文，并持续跟踪这些公司的季度业绩验证。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI 公司都聊了啥？投行会重点笔记\n\nAI 是主线\n\n最近某外资投行开了场软件、互联网和 AI 的年度大会，聊的全是 AI 怎么落地。我整理了几个关键公司的核心逻辑，一起看看。\n\n**1. 赢家都在“算力路径”上**\n- 主题就是 AI 带来的增长。那些走在“token 路径”上的公司，比如 SNOW 和 DDOG，已经体现在业绩里了。\n- 长期看好超大规模云厂商。有建筑专家透露，数据中心订单已经排到 2027 年了。\n- 对应用层要非常挑剔。很多应用还在纠结定价、新方向，以及抢 AI 人才的问题。但垂直领域（比如 PCOR）和让程序员更高效的工具（TEAM）有机会。\n\n**2. 几家公司的看点**\n- **CRWV（AI 算力）**：推理需求撑起增长，客户回报明显。自建数据中心马上到位，2026 年利润率会迎来拐点。新业务线（网络、CPU、软件）年底前 ARR 都能过 1 亿美元。\n- **U（Unity，增长引擎）**：Vector 业务同比增长 80%，快接近 10 亿美元的运营规模了。利润率下半年会改善。用户生命周期价值在提升，平台也在向游戏外的行业扩展。\n- **TEAM（企业协作）**：用户多样性\n\n[... middle omitted ...]\n\nill\nVote S Stars in Extel for:\n→ Software Largecap\n→ Software Small & Midcap\n→ Internet Largecap\n→ Internet Small & Midcap\nJEF\n</details>\n\n![](images/310a296f9196ce1f6fcab40c12d472d9379e151297\n\n[... middle omitted ...]\n\nrd\\_iapd\\_Brochure.aspx?BRCHR\\_VRSN\\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://avatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.\n\n© 2026 JEF"
  },
  {
    "id": "R012",
    "title": "个人AI PC正在重塑存储器需求结构，而市场仍在用旧框架定价",
    "digest": "[wechat_article.md]\n# 个人AI PC正在重塑存储器需求结构，而市场仍在用旧框架定价\n\nComputex 2026 的展台上，英伟达没有发布新的数据中心GPU，却拿出了三款针对“个人”场景的AI硬件：RTX Spark迷你工作站、N1X芯片驱动的AI PC、以及搭载748GB内存的DGX Station桌面电脑。这些产品的共同点不是算力，而是内存容量——RTX Spark的128GB LPDDR5X内存，是传统笔记本电脑平均12GB的10倍以上；DGX Station的748GB总内存，甚至超过了普通服务器的600GB平均内存配置。\n\n某外资投行在Computex后的第一时间发布了研判。这份报告的核心判断值得产业决策者认真对待：AI推理需求正从集中式数据中心向分布式终端扩散，而这一扩散的物理载体，不是算力芯片，而是存储器。市场当前对存储器板块的定价，仍然停留在“数据中心HBM驱动周期”的旧框架中，忽略了个人AI设备带来的结构性增量。\n\n这不是一个简单的“量价齐升”故事。个人AI设备的DRAM含量是传统终端的10倍以上，但更大的变量在于，AI推理从GPU向CPU的扩展，正在创造一个新的服务器内存需求品类——SoCAMM2和服务器DDR5。这两个市场，此前几乎不在主流存储器分析框架的讨论范围内。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 个人AI终端的DRAM含量跃迁，正在改写存储器需求的基数\n\n传统PC和笔记本电脑的DRAM含量在过去十年里增长缓慢，平均维持在12GB左右。即便是在高端游戏本上，32GB也已经是天花板。但英伟达在Computex上展示的RTX Spark，直接搭载了128GB LPDDR5X内存，是传统PC的10倍以上。\n\n这个数字的意义需要放在一个更大的背景下来理解。RTX Spark的定位是“本地运行大模型和A\n\n[... middle omitted ...]\n\n整的研报原文、估值模型拆解，以及更多产业一线的交叉验证信息。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n个人AI电脑，内存需求暴增10倍\n\nPC AI化，内存需求爆发\n\nComputex 2026刚结束，某外资投行连夜出了份研报，核心逻辑很清晰：AI正从云端走向个人设备，内存（DRAM）成了最大受益方。\n\n**1. 个人AI电脑：内存需求直接翻10倍**\n- NVIDIA发布了RTX Spark（配128GB LPDDR5X）和DGX Station（最高748GB内存）\n- 对比传统笔记本平均12GB DRAM，AI PC的内存装载量直接**超过10倍**\n- DGX Station的内存甚至超过普通服务器（600GB），说明AI推理正在“下放”到桌面\n\n**2. AI CPU：Vera芯片量产，拉动服务器内存**\n- Vera CPU采用自研Olympus核心（88核），LPDDR5X带宽达1.2TB/s\n- 在智能体AI、强化学习等任务中，比x86处理器快1.8倍\n- 预计会带动服务器DDR5和SoCAMM2需求进一步上升\n\n**3. 物理AI：Cosmos 3模型发布，训练周期从月缩到天**\n- 这是全球首个全开放“全能模型”，能理解文本、图像、视频、声音和动作\n- 三个版本：Super（机器人/自动驾\n\n[... middle omitted ...]\n\nindustry.\n\nPersonal AI: RTX Spark, N1X chip, and DGX Station — Nvidia introduced Windows AI PC products during its GTC Taipei keynote, aimed at running large AI models and agents locally rathe\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R013",
    "title": "市场真正低估的不是需求，而是供给侧的再定价",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是需求，而是供给侧的再定价\n\n中国半导体设备进口数据在4月呈现出一幅看似矛盾的图景：WFE（晶圆制造设备）进口同比下降6%，延续了年初以来的弱势；但测试和封装设备进口却分别飙升21%和42%。这份来自某外资投行的研报揭示了一个容易被忽视的关键信号——中国半导体贸易逆差在4M26期间扩大了17%，逆转了自2021年以来持续收窄的趋势。真正值得关注的不是短期设备进口的波动，而是这一结构性变化对中国半导体资本开支和WFE需求的深远影响。\n\n为什么现在重要？因为市场普遍将注意力集中在WFE进口的负增长上，却忽略了背后正在发生的两件事：一是中国半导体整体进口增速创下2018年1月以来新高（4月同比增长58%），这主要受AI驱动的内存、CPU、GPU等芯片价格上涨推动；二是设备进口的结构性分化正在暴露中国在先进制程领域的真实瓶颈——光刻和刻蚀设备进口分别暴跌60%和28%，而沉积和离子注入设备却实现36%和20%的增长。这不是需求疲软，而是供给侧正在被迫重新定价。\n\n报告提供的核心判断是：WFE的弱势可能已经触底。三个驱动因素正在汇聚——美国限制政策未见变化、AI驱动的需求持续强劲、以及即将到来的大型内存IPO。这意味着未来3年中国半导体资本开支将加速增长，而外国WFE供应商将在这一过程中扮演关键角色。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 设备进口的结构性分化揭示了产能扩张的真实方向\n\n4月数据最引人注目的特征不是总量下降，而是品类之间的剧烈分化。WFE进口下降6%，但测试和封装工具分别增长21%和42%。这一分化与华为近期公布的“Tau”缩放定律不谋而合——该技术需要芯片间混合键合和TSV设备来实现其“逻辑折叠”技术。虽然单月数据不足以代表趋势，但这一巧合值得密切关注。\n\n在WFE内部，分化同\n\n[... middle omitted ...]\n\n内分享完整的研报原文和原始图表，以及每周更新的进口数据跟踪。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国半导体设备进口，正在悄悄换挡\n\n📉 下滑见底，回暖前兆\n\n4月中国半导体设备进口数据出炉，整体同比降4%，其中晶圆制造设备（WFE）下滑6%。但仔细看结构，有意思的变化已经在发生。\n\n**1/ 设备进口结构在变**\n- 光刻/刻蚀设备进口分别下滑60%/28%\n- 沉积/离子注入设备逆势增长36%/20%\n- 封装测试设备暴涨21%/42%\n\n这里有个信号：华为上周发布的“Tau”缩放定律，需要芯片间混合键合和TSV设备来实现“逻辑折叠”技术。虽然单月数据不能说明趋势，但方向值得关注。\n\n**2/ 进口来源地重新洗牌**\n今年前4个月，新加坡成为中国WFE进口最大来源地之一，占比24%，与日本并列第一，超越荷兰的19%。2025年新加坡占比才16%，一年内快速上升。马来西亚的份额也从10%涨到12%。\n\n**3/ 半导体贸易逆差在扩大**\n4月中国半导体进口同比增长58%，创2018年以来新高。AI驱动的存储、CPU、GPU等芯片价格上涨是主要推手。前4个月半导体贸易逆差扩大17%，逆转了2021年以来收窄的趋势。\n\n**4/ 为什么说底部可能已过**\n研报认为：1）特朗普访问后美国限制政策未变；2）AI\n\n[... middle omitted ...]\n\noderation relative to DD declines in Nov-Feb, but imports of packaging tools rose sharply. Apr SPE imports fell 4% YY, same as in Mar, a big moderation of double-digit declines in the prior th\n\n[... middle omitted ...]\n\nd\\_iapd\\_Brochure.aspx?BRCHR\\_VRSN\\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://javatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.\n\n© 2026 JEF"
  },
  {
    "id": "R014",
    "title": "日本股市的真正分歧不在AI与非AI，而在利率能否容忍估值分化",
    "digest": "[wechat_article.md]\n# 日本股市的真正分歧不在AI与非AI，而在利率能否容忍估值分化\n\n五月日本股市创下历史新高，日经225单月上涨11.9%，TOPIX上涨6.2%，双双突破此前高点。表面上看，这是一次由AI半导体驱动的普涨行情。但某外资投行最新发布的月度策略报告揭示了一个更值得关注的信号：AI与非AI股票之间的价格和盈利差距正在以不可持续的速度扩大，而真正决定市场走向的变量，可能不是AI叙事本身，而是日本长期利率的重新定价。\n\n这份报告的核心判断并不复杂：AI半导体股票的盈利预测在5月被快速上修，但估值却在下降——PE回到了2025年11月市场担忧AI投资过热的水平。这意味着，AI板块的上涨并非由估值扩张驱动，而是由盈利增长支撑。与此同时，非AI股票、内需板块的盈利预测却在被下调。市场正在形成一种“单向分化”的结构：AI越涨，非AI越跌，而利率的上升可能成为打破这一格局的关键变量。\n\n为什么现在重要？因为日本10年期国债收益率在5月中旬一度突破2.8%，创下29年新高。这与日本政府补充预算的传闻直接相关，而政府将在7月初公布经济财政管理基本方针。市场正在定价6月日本央行加息80个基点的概率。如果利率继续上行，AI板块的高估值将面临压力，而内需板块可能迎来修复机会。这份报告的价值，恰恰在于它提供了一个清晰的观察框架，帮助投资者判断这一转折点何时到来。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI板块的“盈利扩张-估值收缩”悖论暴露了市场最深的焦虑\n\n5月日本AI半导体相关股票的表现令人瞩目。日经半导体指数单月上涨23.5%，远超大盘。但报告中的一个关键数据值得反复推敲：TOPIX的12个月前瞻PE在5月底为16.9倍，已经回到了日本2月大选后快速上涨前的区间中部。而AI半导体股票的PE甚至出现了下降。\n\n这意味着什么？AI板\n\n[... middle omitted ...]\n\n流向的变化。完整的中文研报解读和原始图表，也将在社群内分享。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日股AI与非AI板块 正在加速分化\n\n📊 AI行情加速分化\n\n5月日股涨声一片：日经225涨11.9%，TOPIX涨6.2%，双双创历史新高。但背后是AI与非AI板块的严重分化。\n\n1️⃣ AI半导体一枝独秀\n- 半导体指数单月暴涨23.5%\n- 内存、线缆股是盈利上修主力\n- 日经225突破66000点，一度触及67000\n- 盈利贡献占涨幅的4.1个百分点（估值贡献2.7个百分点）\n\n2️⃣ 内需板块持续承压\n- 内需指数5月微跌0.9%\n- 地产、能源、食品、交运、公用事业集体走弱\n- 长端利率飙升到2.8%，创29年新高，压制情绪\n- 中间有过短暂轮动到银行和内需，但很快结束\n\n3️⃣ 估值怎么看？\n- TOPIX 12个月前瞻PE在16.9倍，处于2月大选后新中枢\n- AI半导体股盈利快速上修，PE反而回落（类似11月市场担忧过度时水平）\n- 材料、化工、商社估值偏高；IT服务、零售、食品、地产偏低\n\n4️⃣ 资金面：外资持续流入\n- 5月外资净买入日股约0.8万亿日元\n- 年内累计净买入6.24万亿日元（现货净买10.9万亿 vs 期货净卖4.6万亿）\n- 信托、投信、散户小幅净卖出\n\n5️⃣ 宏\n\n[... middle omitted ...]\n\nened the gap in share price performance between AI and non-AI stocks. Meanwhile, as earnings forecasts for AI semiconductor companies were quickly revised upward in May, P/E ratios declined (t\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 02 Jun 2026 09:50 PM JST\n\nDisseminated 02 Jun 2026 09:52 PM JST"
  },
  {
    "id": "R015",
    "title": "市场真正低估的不是房价，而是K型分化正在重塑估值逻辑",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是房价，而是K型分化正在重塑估值逻辑\n\n某外资投行在5月发布的这份中国房地产研报，表面在讲二手房价跌幅扩大，但真正值得关注的信号藏在标题里：**“Diverging Home Price Trends Continued in May”**。\n\n这不是一篇简单的“楼市又跌了”的悲观报告。它揭示了一个正在加速的结构性现象——城市之间、产品之间、甚至同一城市内部不同板块之间，价格走势正在从普跌走向K型分化。而这种分化，恰恰是判断2026-2027年房地产投资机会的核心锚点。\n\n报告的核心判断可以浓缩为一句话：**全国二手房价格仍在温和下行，但一线城市已经出现企稳苗头；真正决定未来走势的，不是政策刺激力度，而是供给侧的出清速度与需求的结构性转移。**\n\n以下，我们拆解这份研报的五个关键洞察，并探讨那些报告尚未完全回答、但值得持续追踪的问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 全国二手房价格跌幅在扩大，但一线城市已企稳——这背后是“K型复苏”的早期信号\n\n5月数据显示，85个样本城市二手房挂牌价环比下跌0.5%，较4月的-0.4%有所扩大，同比跌幅已深至-11.3%。93%的城市录得环比下跌，其中64%的城市跌幅在加速——这个数字在4月仅为19%。\n\n表面看，数据在恶化。但真正有趣的结构性差异在于：**一线城市二手房价格环比仅下跌0.1%，基本持平。**\n\n这意味着什么？\n\n报告将其归因于一线城市更强的二手房成交——尤其是深圳、广州在4月底政策放松后的销售回暖。但更深层的含义是：在整体需求疲软的环境中，高能级城市凭借其人口流入、就业机会和相对有限的供给，正在成为唯一的“价格锚点”。\n\n这不是一个普涨的信号，而是“K型分化”的早期形态——一线城市可能率先触底，而低能级城市仍在寻底过程中。对于\n\n[... middle omitted ...]\n\n据，并围绕这些未解问题进行讨论。欢迎来星球微信群里继续交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n二手房市场：5月数据里的K型分化\n\n房价还在分化\n\n5月二手房数据出来了，趋势很清晰——城市之间的分化在加剧。一线城市相对稳，但整体还在往下走。\n\n1️⃣ 挂牌价跌幅扩大\n85个样本城市二手房挂牌价环比跌0.5%（4月是-0.4%），同比跌11.3%。93%的城市都在跌，其中64%的城市跌幅比上月更大。一线城市相对坚挺，环比只跌0.1%，主要是因为深圳、广州4月底政策放松后，二手房成交回暖。\n\n2️⃣ 挂牌量在涨，但新增挂牌在降\n约50个样本城市的总挂牌量环比微增0.1%，约60%的城市在增加。但新增挂牌量环比降4%，同比降10%，说明业主惜售心态在变强。不过，51%的城市总挂牌量比去年底还高，31%创了历史新高。\n\n3️⃣ 看房热度降温\n5月中介门店看房量环比降2%，但同比还涨12%。3-4月成交高峰后，需求在自然回落。二手房凭借价格优势和低总价房源，正在抢占更多市场份额。\n\n4️⃣ 房价可能继续软着陆\n研报判断，6月二手房成交可能进一步放缓，三季度同比可能转负。新房因为开发商推盘减少，同比继续下滑。2026-27年房价整体仍将温和下行，但部分一线城市可能因去库存效果更好而小幅回升。\n\n5️⃣ 关注这些指标\n\n[... middle omitted ...]\n\neclines, with 64% seeing faster declines (vs. 91% and 19% in April, respectively). In contrast, Tier 1 cities remained stable at -0.1% m/m, which we attribute to stronger secondary home sales,\n\n[... middle omitted ...]\n\nperty Co Ltd (0123.HK)</td><td>O (09/27/2024)</td><td>HK$4.56</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R016",
    "title": "香港楼市的真正拐点，不是利率，是跨境资金监管的落地",
    "digest": "[wechat_article.md]\n# 香港楼市的真正拐点，不是利率，是跨境资金监管的落地\n\n2026年6月1日，中国国务院正式发布《对外投资管理规定》，其中第32条明确将香港相关交易纳入监管范围。这份文件在市场预期中酝酿已久，但真正落地时，绝大多数关注香港楼市的投资者仍然低估了它的分量。\n\n某外资投行在报告发布当天迅速做出判断：这项新规可能对香港开发商构成负面传导，原因不在于需求端的大幅萎缩，而在于供给侧的再定价逻辑正在被改写。市场此前习惯于将香港住宅市场的波动归因于利率周期、供应节奏或政策刺激，但这一次，真正需要被重新定价的变量，是资金结构本身。\n\n报告的核心判断可以用一句话概括：**内地购房者占香港新房市场交易金额已接近50%，而新规将显著提高其中非永久居民部分的资金审查门槛，进而改变开发商对“量价恢复”的预期。** 这个判断不是简单的需求减少故事，而是资金结构变化如何倒逼开发商资产负债表策略调整的推演。\n\n以下，我们从五个层次展开这份报告的洞察链条。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 内地购房者占比已经越过临界点，但市场仍用“边际变量”来理解它\n\n根据报告引用的中原地产数据，2026年第一季度，内地购房者（以拼音姓氏识别）占香港整体住宅交易金额的33%，但在新房市场，这一比例高达53%。如果回溯历史，这个数字在2011年三季度曾触及51%的高点，随后在2013至2019年间回落至15%-25%的区间，直到2022年后再度攀升。\n\n关键变化发生在2024年——内地购房者在新房市场的占比从2023年的45%跃升至54%，并在2025至2026年维持在43%至53%的高位。报告特别指出，这一轮增长与香港撤销买家印花税（BSD）有直接关系：此前非永久居民购房需缴纳15%的BSD，而该税项取消后，内地非永久居民购房的边际成本大幅降低。\n\n[... middle omitted ...]\n\n多历史案例和市场动态，持续跟踪新规对香港楼市的实际影响路径。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n香港买房，钱从哪里来？\n\n跨境资金收紧\n\n新规如何影响香港楼市？\n\n上周某外资投行出了份研报，专门聊中国新发布的《对外投资条例》对香港楼市的影响，信息量很大。我帮你拆解一下核心逻辑👇\n\n**1️⃣ 新规到底说了啥？**\n- 2026年7月1日生效，覆盖内地企业、机构和居民\n- 第32条明确：香港相关交易也在监管范围内\n- 第12条要求：事前审批/备案、持续信息报告、跨境资金登记\n- 第27条处罚：违法投资可没收违法所得+罚款投资额的0.1%-0.5%，拒不改正可罚0.5%-1%，并限制1-3年境外投资\n\n**2️⃣ 对香港楼市意味着什么？**\n- 内地买家占2026年Q1一手市场成交额的49%，总成交额的32%\n- 但并非所有内地买家都受影响：已拿永居+放弃内地户口的不算；有合法资金来源（如香港工资收入）的也没问题\n- 2017-2019年约62%的内地买家交易需交买家印花税（BSD），说明这些是非永居购买\n- 现在BSD已取消，研报推测：非永居内地买家比例可能高于62%\n\n**3️⃣ 开发商怎么看？**\n- 研报认为新规对住宅价格和成交量恢复是负面信号\n- 新鸿基和恒基可能表现最差\n- 净现金开发商（如长实、信\n\n[... middle omitted ...]\n\nre-approval or filing, ongoing information reporting, and comprehensive cross-border capital registration for outbound investments. On enforcement, Article 27 sets out stringent penalties. Ill\n\n[... middle omitted ...]\n\ncom/sa/en/cssa.html.\n\n© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.\n\n![](images/c1ba03d6605ac637782690f4f328bd781583666e9b44a8d1ec07483e6da89fa2.jpg)"
  },
  {
    "id": "R017",
    "title": "存储市场真正被低估的不是需求，而是供给侧的再定价能力",
    "digest": "[wechat_article.md]\n# 存储市场真正被低估的不是需求，而是供给侧的再定价能力\n\n2026年4月的存储产业链数据，看起来只是月度例行更新，但背后隐藏着一个对产业决策者和投资者都至关重要的信号：这轮存储扩张的驱动力，正在从“量”转向“质”，而市场对这一结构性变化的定价，可能才刚刚开始。\n\n某外资投行最新发布的电子元器件行业研报，基于TechnoSystems Research（TSR）的4月出货数据，揭示了几个容易被忽视的趋势。近线HDD（近线硬盘）容量出货同比仍增长31%，企业级SSD容量出货同比暴增117%，这些数字本身并不令人意外。真正值得关注的，是这些增长背后的结构性变化——平均单盘容量持续攀升、高容量型号加速导入、以及供应链上“产能主动控制”与“需求被动旺盛”之间的微妙张力。\n\n这些信号叠加在一起，指向一个核心判断：存储产业链的价值分配正在发生转移，而市场目前更多在追逐需求端的弹性，却低估了供给端结构性变化带来的定价权重塑。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮扩张的核心不是出货量，而是单盘容量的持续上移\n\n4月HDD总出货量1120万台，同比仅增长8%，环比甚至下降2%。但同期HDD容量出货达到168.5EB，同比增长30%。拆开来看，近线HDD出货量610万台，同比增14%，但容量出货154.8EB，同比增31%。关键数字在于平均单盘容量：4月近线HDD平均容量达到22.8TB，同比提升15%，环比继续上行2%。\n\n企业级SSD的对比更为鲜明。4月SSD总出货量2920万台，同比仅增3%，但容量出货56.2EB，同比增64%。其中企业级SSD出货量570万台，同比增42%，容量出货37.7EB，同比增117%。企业级SSD平均单盘容量已达到6.6TB，同比增53%。\n\n这意味着什么？存储需求的增长逻辑正在发生\n\n[... middle omitted ...]\n\n在群内分享完整研报原文，并围绕这些未解问题展开更深入的交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n数据中心存储，谁在悄悄加单？\n\n📊 存储芯片需求新信号\n\n**4月存储出货数据出炉**\n某外资投行刚更新了4月HDD和SSD的出货数据，整体趋势很清晰：**大容量存储仍在加速**。\n\n**1️⃣ HDD：大容量近线盘持续走强**\n- 4月HDD总出货1120万块（同比+8%），其中近线HDD占680万块（同比+14%）\n- 容量产出168.5EB（同比+30%），近线HDD贡献154.8EB（同比+31%）\n- 26TB/28TB/32TB等高容量型号产量逐步爬坡，单盘平均容量达22.8TB（同比+15%）\n- 厂商在积极锁定近线组件，生产计划偏乐观\n\n**2️⃣ SSD：企业级容量爆发式增长**\n- 总出货2920万块（同比+3%），但企业级SSD出货570万块（同比+42%）\n- 容量产出56.2EB（同比+64%），企业级SSD贡献37.7EB（同比+117%）\n- 单盘平均容量达6.6TB（同比+53%），高端型号已出现122.88TB和245.76TB\n- 总出货量趋稳，但容量在快速膨胀，企业级是主推手\n\n**3️⃣ 存储结构正在变化**\n- 企业级HDD+近线HDD+企业SSD合计容量产出192.\n\n[... middle omitted ...]\n\npidly, at 117% YoY. In nearline HDDs, demand remained solid for models with capacity of 26TB or more in April 2026. In enterprise SSDs, the maximum capacity was 61.44TB for a long time, but TS\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 02 Jun 2026 04:37 PM JST\n\nDisseminated 02 Jun 2026 04:37 PM JST"
  },
  {
    "id": "R018",
    "title": "市场真正低估的不是AI需求，而是CPU在Agentic时代的重新定价",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是AI需求，而是CPU在Agentic时代的重新定价\n\n过去六个月，几乎所有关于AI基础设施的讨论都围绕一个核心叙事：GPU供不应求，算力军备竞赛持续升级。这个叙事本身没有错，但它正在遮蔽一个更为深刻的结构性变化——CPU正在从AI工作负载中的“配角”重新回到“中枢”位置，而这一轮重新定价的力度，可能远超大多数投资者的预期。\n\n某外资投行在近期硅谷巴士之旅后发布的研报，提供了一个难得的全景视角。该团队在一天内密集走访了AMD、AMAT、ALAB、NVMI、STX、WDC和SMCI七家公司，覆盖了从芯片设计、设备制造到系统集成的完整产业链。将这些分散的会议纪要串联起来，一个清晰的主判断浮现出来：Agentic AI的爆发正在重塑整个计算架构的价值分配，CPU、互联芯片和先进封装设备将成为下一个阶段最具定价权的环节，而市场目前对这些结构性变化的定价仍然不足。\n\n这不是一个关于“AI需求是否真实”的讨论——这个问题已经被反复验证。真正值得深入推敲的问题是：当AI从聊天机器人走向自主代理，从单一推理走向多任务编排，计算架构的瓶颈和赢家将会发生怎样的位移？以下五个层次的分析，尝试回答这个核心问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. Agentic AI正在将CPU从“配角”推回“中枢”，AMD的份额拐点可能被低估\n\nAgentic AI是这份研报中反复出现的主题词，而且不是概念层面的讨论。AMD管理层在会议中明确表示，Agentic AI的采用在今年2月出现了一个陡峭的拐点——当模型能力达到某个临界值后，所有主要超大规模云厂商在1月份就显著增加了对CPU的需求。这个时间节点非常值得注意：它发生在DeepSeek引发市场对算力需求担忧之前，说明这不是短期情绪波动，而是底层工作负载结构的真实变化\n\n[... middle omitted ...]\n\n司的季度更新和产业链调研，并在第一时间分享我们的分析和判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAgentic AI 正在重塑芯片需求格局\n\nAI推理爆发，CPU需求猛增\n\n最近参加了一场外资投行的硅谷巴士巡回路演，和AMD、AMAT、ALAB、NVMI、SMCI等公司聊了聊，信息量很大，来分享几个核心判断👇\n\n**1. Agentic AI 是真正的需求推手**\n\nAMD明确表示，Agentic AI的采用速度远超预期。今年1月，所有大型云厂商大幅提升了CPU侧需求。AMD的服务器收入Q1增长超过50%。\n\n关键逻辑：Agentic AI需要大量CPU来做编排、执行、数据库检索——这些都不是GPU的强项。AMD认为自己在Agentic领域的份额可能超过通用服务器CPU份额。\n\n**2. 英伟达的CUDA护城河在变薄**\n\nAMD观察到，前沿AI公司同时在用英伟达、AMD和不同的ASIC。随着软件生态加速，CUDA的壁垒正在被削弱。Claude code已经在内部帮助缩短软件部署周期。\n\n**3. 服务器CPU的三大战场**\n\nAMD把服务器CPU分为三类：通用CPU、AI头节点、Agentic。Turin系列覆盖8核到192核，Venice将是Helios的头节点CPU。值得注意的是，Verano是专\n\n[... middle omitted ...]\n\n, CVP Financial Strategy & IR | Prabh Gowrisankaran, Director, IR\n\n■ Server growth. Inflection of Agentic AI and rise of CPU demand was noticeable last year. AMD articulated the 3 segments of \n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R019",
    "title": "Computex 2026 最核心的信号：Agentic AI 正在重构半导体价值链，而台积电产能不再是瓶颈",
    "digest": "[wechat_article.md]\n# Computex 2026 最核心的信号：Agentic AI 正在重构半导体价值链，而台积电产能不再是瓶颈\n\n每年 Computex 的 keynote 都会释放出一些信号，但今年的信号密度明显高于以往。在 Nvidia、Arm 和 Qualcomm 的演讲中，一个共同的叙事主线浮出水面：Agentic AI 正在从云端向边缘侧渗透，而支撑这一轮计算需求扩张的芯片架构、产能分配和竞争格局，正在发生结构性变化。\n\n某外资投行在 Computex 首日发布的研报，捕捉到了几个容易被市场忽略的关键点。这些点不是简单的产品发布回顾，而是对产业逻辑的重新锚定。\n\n市场此前最担心的两个问题是：第一，台积电的产能能否支撑 Nvidia 在 2027 年的增长；第二，AI PC 到底是不是一个被过度炒作的伪需求。这份研报给出的答案，比预期更为清晰。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 台积电产能不再是 Nvidia 的增长约束，2027 年供需仍将偏紧\n\n过去两年，市场对 AI 芯片供应链的最大焦虑，始终围绕台积电的 CoWoS 产能分配。每一次 Nvidia 与竞争对手之间的产能博弈，都会引发股价波动。但今年的 Computex 上，Nvidia 管理层给出了一个明确的信号：公司已经说服台积电及其他供应商，需求端的强劲增长是可持续的。\n\n这意味着什么？第一，Nvidia 对 2027 年的增长预期已经得到了供应链的认可。第二，即使供给端在持续扩张，需求仍然可能超过供给。第三，Nvidia 明确表示，AI 半导体市场并非零和博弈，市场份额竞争不是核心矛盾。\n\n从投研视角看，这一表态至少消解了两个不确定性：一是 Nvidia 的产能安全边际，二是市场对“竞争对手抢产能”的担忧。当龙头公司能够锁定足够的先进制程产能时\n\n[... middle omitted ...]\n\n欢迎来我们的星球微信群里，和更多产业研究者一起追踪后续变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nComputex 2026 关键信号解读\n\nAgentic AI 是主角\n\n这次 Computex 的 keynote 基本被 Agentic AI 和 CPU 服务器承包了。\nNvidia、Arm、高通都在强调 Arm 架构的服务器 CPU 是未来 Agentic AI 的核心支撑，跟之前某外资投行报告的观点一致。\n\nNvidia 的 Vera CPU 值得关注，性能是最高端 x86 的 1.8 倍。分析师直接问了 CEO 关于 200 亿美元营收的假设，管理层的回应很直接：需求来自 AI 服务器和独立 CPU 服务器两个方向。供应链信息显示正在准备 250-400 万颗的量。\n\n台积电产能够用吗？Nvidia 说 2027 年的产能足够支撑稳健增长，而且已经说服台积电和其他供应商需求依然强劲。即使供给扩大，2027 年大概率还是供不应求。管理层特别强调 AI 芯片市场是在增长，不是零和游戏。\n\n联发科的 AI PC 芯片终于来了\nNvidia 和联发科联合设计的 RTX Sparks 在 keynote 上正式发布，这其实 9 个月前就被预测到了。PC 品牌给出的价格：N1X 约 2899 美元，N1 约\n\n[... middle omitted ...]\n\nlished NVIDIA's Vera CPU and Rubin GPU seen as the main show (27 May 2026). At today's investor luncheon, our Nvidia analyst Joe Moore asked CEO Jensen Huang the first question about the US\\$2\n\n[... middle omitted ...]\n\n5.TW)</td><td>O (04/17/2026)</td><td>NT$8,080.00</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\nTiffany Yeh\n\n© 2026 MS"
  },
  {
    "id": "R020",
    "title": "市场低估了资本管制对香港楼市的真正影响范围",
    "digest": "[wechat_article.md]\n# 市场低估了资本管制对香港楼市的真正影响范围\n\n中国在5月下旬和6月初连续出台两项针对跨境资本流动的监管措施——先是收紧对未授权离岸券商的审查，随后发布新的对外投资规则。香港地产股当天即出现波动。市场的第一反应是担忧内地买家购买香港住宅的渠道被压缩，进而拖累成交量与房价。\n\n但这份来自某外资投行的报告给出了一个值得认真推敲的判断：**真正受影响的内地买家群体，远没有市场想象的那么大。** 报告的核心理据来自香港税务局的数据——在2025财年，所有非香港身份证持有者购买的住宅单位仅占整体成交量的5.5%，成交金额占比7.2%。而市场上广泛引用的“拼音姓名买家占比26%”的数据，之所以高出数倍，是因为其中包含了大量已经持有香港身份证的居民——他们要么是通过人才计划或留学途径获得非永久居民身份的内地人士，要么是原籍内地的永久居民。\n\n这两类人都有香港本地工资收入和离岸银行账户，受资本管制的影响要小得多。换句话说，市场恐慌的焦点——内地买家大规模撤离——实际上只涉及一个很小的交易群体。报告的结论是，当前股价的下跌反而可能是一个入场窗口。\n\n但真正值得深入推敲的，不是“影响有多大”，而是**资本管制与香港楼市之间的作用机制正在发生结构性变化**。这份报告提供了一些容易被忽略的信号，值得逐层拆解。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 真正敏感的指标不是拼音买家占比，而是非香港身份证持有者的交易量\n\n市场上关于“内地买家占比”的讨论长期存在两个口径的混淆。一个口径来自税务局，统计的是非香港身份证持有者的交易；另一个口径来自中原地产，统计的是以拼音姓名登记的交易。2025年，拼音买家在整体成交量中占26%，在一手住宅中甚至高达41%。这两个数字之间的差距，正是理解本次政策冲击真实范围的钥匙。\n\n报告明确指出，拼音买家\n\n[... middle omitted ...]\n\n群里继续讨论。我们会持续跟踪这些变量，并在关键节点更新判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n大陆收紧资金出海，香港楼市影响多大？\n\n封面：香港楼市冲击波\n\n副标题：5.5%的数据，别慌\n\n最近内地收紧了对跨境投资的监管，很多人担心：大陆人还能去香港买房吗？投行研报做了详细拆解，结论是——别自己吓自己。\n\n先说关键数据：2025财年，非香港身份证买家买了2997套住宅，占总量5.5%，金额313亿港币，占7.2%。这个群体最直接受影响。\n\n但更常被引用的“拼音名买家”占比26%，这里面其实包含两类人：\n1. 通过人才计划/留学拿到的非永久居民\n2. 内地出身的永久居民\n这两类人赚港币、有离岸账户，影响其实有限。\n\n**真正会被卡的是谁？**\n- 买普通住宅的单套买家，没有港币收入，靠离岸证券账户或保险产品积累资金，受外汇额度限制。\n- 买豪宅或批量买楼的高净值买家反而不太受影响——他们可以通过股息、家族生意、私行结构获得离岸资金。\n\n**看看2016-17年的经验**：当时内地收紧资本管制，非居民买房比例从4.5%微降到4.5%，2017年反而升到6.2%，直到2019年社会事件才降到3.6%。资本管制单打独斗，效果有限。\n\n**还有两个潜在利好**：\n1. 强制卖出规则下，部分资金无法再投股市，香港\n\n[... middle omitted ...]\n\n— Per data from the Inland Revenue Department (link), in financial year 2025, individual buyers not holding a Hong Kong Identity Card (HKID) purchased 2,997 residential units (equals 5.5% of t\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R021",
    "title": "市场真正低估的不是房价下跌，而是成交量萎缩对消费的连锁反应",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是房价下跌，而是成交量萎缩对消费的连锁反应\n\n当一家外资投行的宏观团队预测全国房价将下跌5%至10%，成交量萎缩20%至30%时，大多数投资者的第一反应是：房地产股承压。但这份研报的核心判断远比这更尖锐——真正需要警惕的，是住房市场下行对消费行业的二次冲击，尤其是那些看似与房地产“不直接相关”的零售品类。\n\n该投行刚刚将澳大利亚消费行业评级从“与大盘持平”下调至“谨慎”。这不是一个轻率的判断。它基于一个正在快速成型的逻辑链：税收政策变化叠加高利率环境，正在从根本上改变住房市场的供需结构，而这种结构性变化将通过两条清晰的传导路径，冲击消费行业的盈利预测。\n\n第一条路径是财富效应。房价下跌直接侵蚀家庭资产负债表，压低消费者信心和支出意愿。第二条路径更隐蔽但更具破坏力——成交量萎缩。历史数据表明，房价每下跌5%至10%，成交量往往下降20%至30%。更少的交易意味着更少的装修、更少的搬家、更少的大件商品采购。这条路径直接穿透到硬件零售商、家电卖场和家具品牌。\n\n更值得关注的是，当前市场共识尚未充分反映这一风险。研报对覆盖标的的FY27盈利预测进行了系统性下调，但即便下调后，部分公司的EPS仍高于市场共识。这意味着，如果住房市场的下行比预期更陡峭，当前估值所隐含的盈利假设将面临进一步修正。\n\n这不是一个关于“房地产何时见底”的问题。这是一个关于“消费行业哪些环节的盈利预期尚未充分定价住房风险”的问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 成交量而非价格，才是消费行业最直接的传导变量\n\n市场习惯于将房价涨跌等同于消费信心强弱。但研报提供了一个更精细的分析框架：成交量变化才是消费行业更直接的传导变量。\n\n历史数据显示，房价与成交量之间存在稳定的联动关系。当房价下跌5%至10%，成交量通常下降20\n\n[... middle omitted ...]\n\n如何调整，以及哪些细分品类在防御性配置中真正具备结构性优势。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n澳洲房市降温，消费股要小心了\n\n房市下行冲击消费\n\n房价预计跌5-10%，成交量降20-30%\n某外资投行最新研报把澳洲消费行业评级下调至“谨慎”\n\n1/ 房市从支撑变成拖累\n过去房价涨，大家敢花钱装修、换家电\n现在房价跌，财富效应消失，消费信心跟着走弱\n成交量下降更直接——没人搬家，就不买新家电、不搞翻新\n\n2/ 哪些板块最受伤？\n五金建材首当其冲\nBunnings和IHG这类零售商最敏感\n其中面向建筑商的业务比DIY更脆弱\n因为开发商减少开工，建筑需求直接萎缩\n\n大家电、地板、户外用品同样面临需求下滑\nJB Hi-Fi和Harvey Norman都受影响\n消费者信心弱，大件消费自然推迟\n\n3/ 历史数据怎么说？\n上次房价调整期，五金店同店销售增速从8%降到3.9%\n再上次从10%降到1.8%\n这次研报预计FY27盈利存在下行风险\n已下调多家公司的同店销售和利润率假设\n\n4/ 什么在驱动这轮调整？\n利率维持高位 + 税收政策变化抑制投资需求\n研报预计调整需要时间，不是短期现象\n建筑审批、房屋销售这些先行指标已经走弱\n\n5/ 防御性消费相对更稳\n研报更看好必需消费品\n比如超市、食品这类需求刚性更强的板块\n非必\n\n[... middle omitted ...]\n\nvation and move-related demand.   \nHardware has the most direct exposure, with MTS more sensitive than WES to trade and renovation softness.   \n- Big-ticket consumer electronics and housing-re\n\n[... middle omitted ...]\n\nhs Group Ltd (WOW.AX)</td><td>E (08/28/2025)</td><td>A$35.06</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.   \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R022",
    "title": "市场真正低估的不是需求，而是供给侧的再定价",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是需求，而是供给侧的再定价\n\n过去六个月，全球功率半导体股票平均上涨了135%。中国功率半导体公司同期仅上涨34%，其中华润微、士兰微等功率IDM的涨幅更是只有15%-24%。这不是中国公司基本面更差，而是市场正在用一个过时的框架来定价这个周期。\n\n某外资投行最新发布的China Power Semiconductor研报提出一个核心判断：本轮功率半导体周期与以往最大的不同，在于供给侧的结构性收紧。这不是一个短期的供需错配，而是一个“tighter-for-longer”的格局——供给将比市场预期的更长时间处于紧张状态。报告因此上调了多家中国功率IDM的盈利预测和目标价，并将士兰微从中性上调至买入。\n\n这个判断的关键在于，市场习惯性地将功率半导体的周期视为需求驱动的，但这一次，真正驱动利润率扩张和估值重估的变量在供给侧。如果这一框架成立，那么当前中国功率IDM的估值折价，就不是一个简单的“补涨”机会，而是一个系统性重估的开始。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 供给收紧不是短期现象，而是结构性变化的结果\n\n报告指出，全球功率半导体供应链正在经历一个“tighter-for-longer”的供给格局，背后有两个相互强化的驱动力。\n\n第一个是资本开支的纪律性。功率IDM在2023-2025年显著放缓了资本开支。这不是因为企业对需求悲观，而是在经历了上一轮产能过剩的教训后，整个行业对扩产变得更加谨慎。这种资本纪律在全球范围内是一致的——从英飞凌到TI，从台积电到中国IDM，扩产节奏都在放缓。\n\n第二个是产能的结构性转移。台积电宣布将逐步把部分8英寸和12英寸晶圆产能转换为先进封装，英飞凌也在将部分闲置的IGBT产能转向领先制程的MOSFET。这意味着，即使总晶圆产能没有减少，可用于传统功\n\n[... middle omitted ...]\n\n群讨论可以帮助我们更深入地理解这个正在发生结构性变化的行业。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n功率半导体：供给偏紧，SiC起飞\n\n供给偏紧 + SiC加速渗透\n\n某外资投行最新研报指出，中国功率半导体行业正进入一个“供给持续偏紧+SiC渗透率加速提升”的新阶段。全球功率半导体供应链已释放明确信号：产能扩张依旧克制，而新能源、电网、AI等下游需求韧性十足，供给偏紧格局可能比市场预期的更持久。\n\n1️⃣ 供给端：为什么“紧”是主旋律？\n- 全球功率IDM的资本开支在2023-2025年明显放缓\n- 部分产能被转用于先进封装或高性能MOSFET\n- 2026年初，全球多家功率器件厂商已宣布涨价，英飞凌甚至年内第二次提价\n- 国内功率IDM（如华润微、士兰微）产能利用率已接近满载\n\n2️⃣ 需求端：哪些赛道在发力？\n- 新能源车、储能、AI数据中心是三大增长引擎\n- 研报预计，覆盖的功率半导体公司2026-2028年收入CAGR将从2023-2025年的11%加速至18%\n- SiC（碳化硅）凭借更好的性价比，正在EV、ESS、AIDC等领域加速替代传统硅基器件\n\n3️⃣ 谁最受益？IDM vs Fabless\n- 供给偏紧对IDM更有利——产能自给，利润率弹性更大\n- 研报预计华润微、士兰微的净利率在202\n\n[... middle omitted ...]\n\nration across various end-markets, including EV, ESS and AIDC, benefiting suppliers with SiC R&D capabilities, such as Silan Micro and StarPower. Reflecting this better-than-expected cycle rec\n\n[... middle omitted ...]\n\ncom/sa/en/cssa.html.\n\n© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.\n\n![](images/6caedf422103648342d50c8c02aaeb3f9efeda1d87f88473a458e65c47c78e5c.jpg)"
  },
  {
    "id": "R023",
    "title": "AI冲击保险分销：市场低估的不是需求，而是分销成本的重新定价",
    "digest": "[wechat_article.md]\n# AI冲击保险分销：市场低估的不是需求，而是分销成本的重新定价\n\n印度保险科技行业正在经历一个被多数投资者忽视的结构性拐点。过去十年，线上保险分销的竞争格局一直由PB Fintech（PolicyBazaar的母公司）主导，其核心壁垒是品牌信任与一支庞大的电话顾问团队。但一份来自某外资投行的最新研报揭示了一个正在逼近的变量：AI语音代理正在改变“人”这个环节的成本结构与可复制性。\n\n这份报告的核心判断并非“AI将颠覆保险分销”，这过于简单。真正值得关注的信号是：AI正在同时从两个方向挤压PB Fintech的护城河——一方面降低了挑战者建立分销能力的门槛，另一方面又给PB Fintech自身提供了大幅改善单位经济模型的机会。市场目前对这两个方向的定价都不充分。\n\n报告以PB Fintech为分析样本，但其结论的适用范围远超单一公司。它实际上在回答一个更根本的问题：当“人工顾问”这个金融分销中最昂贵、最难规模化的环节，开始被AI解构时，哪些商业模式会受益，哪些会受损？\n\n以下是我们从这份研报中提炼出的五个层次洞察，以及一个尚未完全解答的关键追问。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 保险分销的真正护城河不是技术，而是“人+信任”的运营飞轮\n\n理解AI冲击的前提，是理解PB Fintech现有模式为何难以复制。报告明确指出，过去挑战者未能撼动其地位，原因不在于技术差距，而在于两个进入壁垒：品牌信任的建立成本极高，以及管理一支大规模电话顾问团队的运营复杂度。\n\nPB Fintech的模式本质上是“线上获客+人工成交”。其网站生成大量“温线索”（warm leads），然后由训练有素的电话顾问完成从产品选择、文档填写到理赔咨询的全流程服务。这个“人”的环节，恰恰是保险这类复杂金融产品区别于标准化产品（如定期存\n\n[... middle omitted ...]\n\n分享完整的研报解读，以及更多关于金融科技AI应用的深度分析。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI进攻保险分销，人机谁赢？\n\n📌 AI vs 人，保险销售怎么选\n\nAI语音成本4-5卢比/分钟，人类10.5卢比/分钟，但转化率差很多\n\n---\n\n1️⃣ 为什么保险是AI最难攻克的领域？\n保险销售需要大量“手把手”指导，从选品、填表到理赔，客户都需要真人协助。投行研报指出，PB Fin靠品牌+电话顾问团队建起护城河，过去竞争对手都没能复制这套模式，因为管理大规模电话团队太难了。\n\n2️⃣ AI创业公司的进攻策略\n新玩家想用AI语音/聊天机器人替代人类顾问。比如Zyra AI（未上市公司）就在做这件事。虽然过去没人成功，但AI降低了搭建电话销售团队的门槛，挑战者会不断尝试。研报判断：他们可能失败，但一定会试。\n\n3️⃣ 单位经济模型对比\nPB Fin的顾问每分钟人力成本约10.5卢比（按月薪5万卢比、40%时间用于通话计算）。AI机器人用前沿模型成本仅4-5卢比/分钟。但成本/销售额上，人类仍然占优——因为AI转化率目前远低于人类。不过随着模型进步，这个差距可能缩小。\n\n4️⃣ PB Fin自己的AI机会\nPB Fin顾问只有40%时间在跟客户说话，其余60%都在整理数据、走流程。公司计划用AI把通话时间\n\n[... middle omitted ...]\n\n products. PB Fin has a strong brand & an army of tele-advisors that service warm leads from the website, and close sales over a call (selection, documentation, claims). They have a dominant p\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R024",
    "title": "全球智能手机市场正在经历一场非对称收缩，苹果的韧性比表面数据更值得深挖",
    "digest": "[wechat_article.md]\n# 全球智能手机市场正在经历一场非对称收缩，苹果的韧性比表面数据更值得深挖\n\n全球智能手机市场正在经历一轮罕见的收缩。某外资投行最新研报援引Counterpoint数据指出，2026年全球智能手机出货量预计同比下降13.9%至10.8亿部，较2月预测的12.4%降幅进一步恶化。在这一片寒意中，苹果4月全球iPhone收入同比增长5.6%，出货量增长2.5%，均价提升3%。市场容易将这一数据解读为“苹果抗跌”，但真正值得关注的不是抗跌本身，而是抗跌背后的结构性驱动力——以及这些驱动力正在如何重塑供应链竞争格局。\n\n这份研报的核心判断是：苹果正在通过产品组合的主动上调而非被动涨价来维持收入增长，而这一策略正在对供应链产生分层影响。部分供应商将受益于苹果的份额集中，另一些则面临被替代或份额流失的风险。市场的定价尚未充分反映这种分化的持续性。\n\n以下是我们从这份研报中提炼出的五个关键洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 苹果的增长不是靠提价，而是靠把消费者“推”向更贵的配置\n\n在整体市场萎缩的背景下，苹果4月收入增长5.6%的数据看似稳健，但更值得拆解的是增长来源。研报明确指出，苹果并未像部分安卓竞争对手那样在周期内直接提价，而是通过产品组合的持续上移——即推动消费者选择Pro、Pro Max机型以及更大存储容量——来实现均价提升。4月均价同比提升3%，单位出货量增长2.5%，这意味着收入增长中约一半来自结构升级，而非需求扩张。\n\n这一策略的可持续性值得关注。在中国市场，iPhone 4月销量同比增长5.6%，但全部来自均价提升，出货量基本持平。这意味着苹果在中国市场已经进入“存量提价”阶段，而非增量扩张。在美国市场，iPhone出货量同比下降13%，但均价提升6%，收入仅下降7%。这进一步印证了苹果正在\n\n[... middle omitted ...]\n\n业链数据和历史对比，进一步拆解这些尚未完全定价的风险与机会。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\niPhone 四月成绩单：在萎缩市场里涨了 6%\n\n逆势增长\n\n全球智能手机市场预计全年萎缩 14%，但 iPhone 四月全球收入同比+5.6%，销量+2.5%，均价+3%。这份成绩单背后有几点值得关注。\n\n1/ 苹果不跟风涨价，靠高端机型拉均价\n同行在提价，但苹果选择通过 Pro/Pro Max 和大容量版本的结构升级来推高均价。美国市场销量虽跌 7%，但均价涨了 6%——主要是去年同期关税消息刺激了提前购买，基数太高。\n\n2/ 中国区全靠均价撑场面\n四月 iPhone 在中国销量同比+5.6%，销量几乎持平，增长完全来自更高的售价。没有苹果官方大促，但国家以旧换新补贴还在。618 期间京东和天猫已经给出 iPhone 17 Pro 千元降价。\n\n3/ 17e 表现不如 16e，但整体 e 系列在增长\n17e 上市前 7 周的销量落后于 16e 同期，主因是北美运营商促销力度减弱、预付费渠道仍集中在 16e。但要算总账：16e+17e 的合计销量，比去年同期 e 系列卖得好。\n\n4/ 对供应链的影响\n台积电：17e 偏弱拖累 N3P 产能，但 AI 应用会补上缺口，台积电不会损失收入。\n存储：四月 iPh\n\n[... middle omitted ...]\n\n Rasgon, Ph.D.\n\n+1 213 559 5917\n\nstacy.rasgon@bernsteinsg.com\n\n![](images/99a50f4c2fc93481814782297fe814a6b2a84954288aeaeb62cf3b4a9469f0b0.jpg)\n\nDavid Dai, CFA\n\n+852 2918 5704\n\ndavid.dai@berns\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R025",
    "title": "韩国科技供应链的真正拐点：从GPU算力竞赛转向Agentic AI的全面落地",
    "digest": "[wechat_article.md]\n# 韩国科技供应链的真正拐点：从GPU算力竞赛转向Agentic AI的全面落地\n\n市场对AI基础设施的讨论，大多仍停留在“算力需求持续增长”这一层面。但某外资投行最新发布的韩国科技产业链调研报告，揭示了一个更为关键的转折：AI的投资逻辑正在从“训练更大的模型”转向“运行更多的智能体”。这一转变对产业链的影响，远比单纯增加算力投入更为深远。\n\n报告基于2026年5月底对14家韩国科技公司的实地调研，覆盖存储器、半导体设备与材料、技术硬件供应链。这些公司的共同判断是：CSP（云服务提供商）的资本开支正在加速向Agentic AI倾斜，而这一趋势正在重塑整个供应链的定价权、需求结构和利润分配。\n\n真正重要的不是AI需求会不会继续增长，而是增长的结构性变化如何重新定义谁在产业链中拥有议价权。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 存储器市场的最大变量不是HBM，而是CPU驱动的服务器DRAM重新定价\n\n市场对存储器的关注长期集中在HBM（高带宽存储器）上，但报告揭示了一个被低估的结构性变化：CPU客户正在成为新的需求驱动力。\n\n核心逻辑在于，Agentic AI的部署比单纯的大模型训练更依赖CPU集群。x86和ARM架构的CPU需求强劲增长，直接推高了服务器DRAM和移动DRAM的价格。报告预计，ARM CPU在整体CPU市场的渗透率将从2025年的13%快速攀升至2028年的40%，这意味着服务器DRAM的单机容量将同步增长。\n\n更值得关注的信号是HBM3e的定价走势。报告指出，HBM3e价格将上涨，以缩小与普通DRAM的价差。这听起来反直觉——通常HBM作为高端产品，价格应该远高于普通DRAM。但这里的逻辑是：普通DRAM因CPU需求激增而涨价更快，导致两者价差收窄。这意味着存储器厂商的利润结构正在发生变化\n\n[... middle omitted ...]\n\n继续讨论，我们会定期分享更多产业链调研的原始数据和深度分析。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n韩国科技供应链正在爆发\n\nAI供应链，两条腿走路\n\n一边是agentic AI催热存储/载板，一边是物理AI还在等风来\n\n1/ 存储最稳，HBM3e价格还在涨。某外资投行韩国科技调研发现，CSP资本支出猛增，CPU客户正在成为新需求引擎。x86和ARM服务器CPU需求旺盛，带动服务器和手机DRAM涨价。HBM3e价格也继续收窄与普通DRAM的价差。存储厂下半年产出增加，加上更多长期协议锁定利润，盈利趋势更稳了。\n\n2/ 硬件里，FC-BGA载板供不应求。高端FC-BGA需求跑在供给前面，利用率高、交期拉长，客户开始签长期协议甚至联合投资来抢产能。更大的封装尺寸、更多层数、硅电容嵌入、玻璃基板这些结构性升级，也在拉高单机价值，支撑多年增长。\n\n3/ 设备和材料才刚起飞。激光切割开始替代HBM里的机械切割，PCB钻孔需求猛增，某设备商还在和头部晶圆厂合作开发去胶机。高压炉管设备拿到新DRAM客户，NAND客户也在接洽。原子力显微镜在混合键合和先进封装检测上打开新场景。前驱体材料也有机会，高K前驱体专利2026年底到期，新玩家可以卡位。这些公司不靠芯片出货量增长，靠的是内容渗透和新客户拓展。\n\n4/ 三星电子被看好\n\n[... middle omitted ...]\n\nMost companies expressed an upbeat outlook: 1) memory/substrate/ MLCC are benefiting from CSP capex increases for agentic AI and tech upgrades to CPUs, optical interconnect and 800v power shif\n\n[... middle omitted ...]\n\n32b803af82f4699c0fda84.jpg)\n\n# Newsletters\n\nSubscribe to our monthly collection of free to view reports and interviews in Open Pass or read our bite-sized round up of research covering our nine key themes, Talking Points"
  },
  {
    "id": "R026",
    "title": "新能源车市的关键分水岭：新车型红利正在取代品牌忠诚度",
    "digest": "[wechat_article.md]\n# 新能源车市的关键分水岭：新车型红利正在取代品牌忠诚度\n\n市场正在经历一个被大多数人低估的结构性转变。某外资投行最新发布的周度订单追踪报告揭示了一个清晰的信号：中国新能源乘用车市场的竞争逻辑，已经从“谁的品牌更强”转向了“谁的新车更能打”。这份覆盖5月最后一周订单数据的报告显示，头部车企的订单表现呈现出前所未有的分化——而这种分化的核心驱动力，几乎完全系于新车型的上市节奏与转化效率。\n\n这不仅仅是月度数据的正常波动。它意味着，过去几年市场习惯用来评估车企竞争力的框架——品牌认知、渠道密度、产能规模——正在失效。取而代之的，是一个更残酷、也更透明的评判标准：你的新车能否在上市首月就转化为可观的订单增量。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 新车型订单转化率正在成为衡量车企竞争力的核心指标，而非品牌惯性\n\n报告中最引人注目的数据，来自蔚来和问界。蔚来在5月最后一周录得47.5-47.7k的周度订单，环比暴增419%，同比飙升705%。问界同期订单为28-28.2k，环比增长419%，同比增长268%。两家公司的订单爆发，背后都有一个共同的驱动因素：新车型的预订单转化。\n\n蔚来的ES9和问界的M9，分别成为各自品牌的订单引擎。这一现象并非偶然。报告同时指出，其他车企的“老款”车型需求普遍疲软，季节性回暖力度有限。这意味着，消费者对新能源车的购买决策，越来越依赖于“最新产品”的吸引力，而非对品牌的长期忠诚度。\n\n这个趋势的深层含义在于：车企不能再依赖过去积累的品牌资产来维持订单流。每一款新车都是一次重新证明自己的机会，而一旦产品节奏出现空档，订单的下滑将是迅速且无情的。对于投资者而言，评估一家车企的价值，需要从“品牌溢价”转向“产品管线迭代能力”。\n\n![研报原图 2](assets/source_image\n\n[... middle omitted ...]\n\n信群里继续讨论，我们会在那里分享更详细的图表解读和行业洞察。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n新能源车周订单大洗牌，新车型才是胜负手\n\n新车型撑起一片天\n\n5月最后一周，新能源车市迎来一轮订单分化。新车型依然是拉动需求的核心引擎，老款车型表现普遍平淡。\n\n1/ 蔚来与问界领跑\n蔚来周订单约4.75万台，环比暴增392%，主要得益于ES9预订单转化。问界同样表现亮眼，周订单约2.8万台，环比增长419%，M9车型贡献显著。两家品牌的新车型投放效果立竿见影。\n\n2/ 比亚迪稳中有升\n比亚迪周订单约7.6万台，环比增长35%，同比微降11%。作为行业龙头，其订单量级依然领先，但增速相对温和。\n\n3/ 理想与小米表现分化\n理想周订单约7900台，环比下滑10%，L8新车型预计6月底上市，后续表现值得关注。小米周订单约1万台，环比增长25%，保持稳健增长。\n\n4/ 小鹏与极氪回调\n小鹏周订单约1.88万台，环比下滑34%，GX车型上市热度逐渐消退。极氪周订单约8400台，环比下降9%，同样处于正常回调阶段。\n\n5/ 行业整体趋势\n研报指出，5月销量环比回升主要受新车型上市和海外市场拓展支撑，二季度业绩有望超预期。但市场对政策刺激的期待，研报认为可能性较低。\n\n这一轮订单分化，核心逻辑很清晰：新车型才是拉动需求的\n\n[... middle omitted ...]\n\nrted by model launches and overseas exposure, making 2Q results likely beat guidance.  \nSome investors have speculated about potential additional policy stimulus, which we view as less likely.\n\n[... middle omitted ...]\n\nd>XPeng Inc. (XPEV.N)</td><td>O (01/29/2021)</td><td>US$17.20</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R027",
    "title": "半导体材料正在经历一场被市场低估的“材料替代”博弈",
    "digest": "[wechat_article.md]\n# 半导体材料正在经历一场被市场低估的“材料替代”博弈\n\n某外资投行近期发布了一份关于AGC半导体业务策略的简报，并在市场引发了一个值得关注的现象：当市场传出PTFE可能替代低介电玻璃用于下一代芯片背板的消息后，AGC股价单日上涨9%，而低介电玻璃相关公司股价同步下跌约10%。这一涨一跌背后，隐藏的不仅是技术路线的选择，更是整个半导体材料供应链正在经历的、被多数投资者低估的“材料替代”结构性博弈。\n\n这份报告的核心判断是：AGC的五年营收翻倍目标并非空谈，而是建立在明确的三大结构性支撑之上——EUV光罩基板的技术壁垒、CCL材料在高速传输领域的差异化竞争，以及氟化产品在先进制程中不可替代的消耗品属性。但真正值得关注的，是市场对PTFE与低介电玻璃之间替代关系的过度简化解读，以及报告尚未完全展开的、关于材料性能测试周期与最终决策时间窗口的关键信息。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 五年营收翻倍的目标背后，是三大业务板块的差异化增长逻辑\n\nAGC计划将半导体相关营收从2025财年的约1000亿日元提升至2030财年的2000亿日元，年复合增长率约15%。这一目标并非笼统的“行业增长”驱动，而是由三个明确的业务板块各自形成独立的增长引擎。\n\n在电子业务板块，EUV光罩基板是当前最大的收入贡献者，2024财年已突破400亿日元，且公司预计2026财年将再次刷新历史纪录。这一增长不仅来自关键客户的复苏，更来自于客户群的扩大——这是一个典型的“存量客户恢复+增量客户拓展”的双轮驱动。CCL（覆铜板）则是另一个值得关注的细分领域，AGC利用自研树脂与玻璃布的组合，实现了“用低一等级的玻璃布达到与竞争对手相同性能”的效果，这是一种典型的材料组合创新，而非单纯的参数竞赛。\n\n在功能化学品板块，FFKM（用于CVD/刻\n\n[... middle omitted ...]\n\n竞争对手分析以及估值框架，这些内容在本篇导读中无法一一展开。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n半导体材料迎来新变数\n\nPTFE vs 低介电玻璃\n\n一场关于背板材料的暗战\n\n最近某外资投行的一份研报，把半导体材料圈的小众玩家推到了台前。简单拆解几个关键点👇\n\n1️⃣ 一家日企的五年翻倍计划\nAGC（AGC株式会社）在半导体相关业务的营收，从FY2020的约500亿日元，到FY2025预计达到1000亿，目标FY2030冲到2000亿——相当于每五年翻一番。目前约65%收入来自电子板块（EUV光罩基板、CCL等），35%来自化学品（氟化产品为主）。考虑到高壁垒，利润贡献可能比营收增长更可观。\n\n2️⃣ 电子板块：EUV光罩基板是现金牛\nEUV光罩基板FY2024已创纪录超400亿日元，FY2026有望再创新高，得益于核心客户恢复和客户群扩大。CCL方面，新ELL系列用自研树脂+低一档的玻璃布，就能达到同行高一档的性能，目前在攻224G应用（交换机/路由器）。如果玻璃核心、光电共封装等后端工艺材料提前放量，可能成为超预期变量。\n\n3️⃣ 化学品：氟化产品是护城河\nFFKM（CVD/刻蚀设备密封件，每季度更换）、ETFE（脱模膜，全球份额第一）、CYTOP（光刻胶保护膜原料）、PTFE。随着芯片层数增加，沉\n\n[... middle omitted ...]\n\n drivers, while within Performance Chemicals, expansion in process materials is expected to lead growth. On the same day, following some market views that PTFE could be considered an alternati\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 03 Jun 2026 04:15 AM JST\n\nDisseminated 03 Jun 2026 04:15 AM JST"
  },
  {
    "id": "R028",
    "title": "中国软件行业真正的拐点，不是AI故事，而是供给结构正在被重新定价",
    "digest": "[wechat_article.md]\n# 中国软件行业真正的拐点，不是AI故事，而是供给结构正在被重新定价\n\n过去两年，围绕中国软件与IT服务行业的讨论，几乎都指向同一个方向：AI能否成为下一轮增长的引擎。市场在等待一个“杀手级应用”，等待企业客户大规模采购AI软件，等待收入曲线像美国同行那样陡峭上扬。\n\n但这份来自某外资投行2026年亚洲暑期学校的研报，给出了一个更冷静、也更值得深思的判断框架。\n\n报告的核心信号可以浓缩为一句话：中国软件行业当前面临的根本问题，不是需求不足，而是供给端的结构性错配。AI带来的增量机会真实存在，但它正在被一个更底层的力量重新分配——谁能在硬件、云基础设施和软件应用之间，建立起真正的议价权，谁才能吃到这轮周期的红利。\n\n换句话说，市场低估了“供给结构再定价”的长期影响，而高估了AI需求爆发的短期弹性。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 企业IT支出预期正在经历“软着陆”，但结构性放缓的信号比表面数字更值得警惕\n\n报告中最直观的数据来自中国CIO调研。2026年上半年，企业外部IT支出增长预期仅为4.8%，相比2025年下半年的12.6%出现了明显回落。更值得注意的是，预期上调预算的企业比例从48%降至38%，而预期下调的比例从15%升至27%。\n\n这不是一个短期波动。回顾过去六年的调研轨迹，2021年上半年曾出现62%的企业计划上调IT预算的峰值，此后这一比例整体呈下行趋势。2024年下半年甚至跌至31%。虽然2025年下半年因AI主题短暂反弹至48%，但2026年上半年再次回落。\n\n这意味着什么？企业IT采购的“冲动期”已经过去。在宏观经济名义GDP增速放缓、企业利润承压的背景下，CIO们正在回归理性。他们不再因为“AI来了”就盲目扩张预算，而是更务实地评估：这笔投入能否在12-18个月内带来可量化的效率\n\n[... middle omitted ...]\n\n结合最新的一手调研数据，一起拆解中国软件行业的真实投资机会。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国软件市场：增长在哪儿？\n\n📊 投研拆解\n\n某外资投行近期更新了中国软件与IT服务行业研报，核心观点很清晰：中国软件市场正在经历结构性变化，但增长路径和全球不太一样。\n\n1️⃣ 供需两端都在变\n- 供给端：技术驱动从云转向AI，软件必须跑在硬件上\n- 需求端：名义GDP增长+劳动力成本上升倒逼效率提升，政府推动数字化和IT国产化\n\n2️⃣ 增长数据怎么说？\n- 2023-2025年行业收入增速基本在0-5%区间，明显低于2019-2021年20-50%的高增长\n- 但2026年预期回升到~5%，拐点信号值得关注\n\n3️⃣ 中美对比：差距也是空间\n- 中国软件+IT服务占IT总支出仅22%，美国是59%\n- 中国软件+IT服务占GDP仅0.6%，美国是3.6%\n- 中国软件市场规模在全球占比仅4.9%，美国是47.7%\n\n4️⃣ 哪些细分赛道在跑？\n- 最高增速：AI平台（CAGR 42%）、协同办公（24%）、CRM（22%）、应用开发平台（20%）\n- 软件市场整体CAGR 13.9%到2028年，从2025年53.6亿美元到2028年83.2亿美元\n\n5️⃣ AI的五层蛋糕理论\n- 从能源→芯片→云基础\n\n[... middle omitted ...]\n\nAND SOFTWARE\n\nAsia Pacific\n\nIndustry View\n\nIn-Line\n\nMS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of i\n\n[... middle omitted ...]\n\ny Co Ltd (600588.SS)</td><td>U (11/12/2024)</td><td>Rmb11.28</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.   \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R029",
    "title": "市场低估的不是AI算力，而是成熟制程存储的AI化重估",
    "digest": "[wechat_article.md]\n# 市场低估的不是AI算力，而是成熟制程存储的AI化重估\n\n当市场还在为HBM和DDR5的供需缺口焦虑时，一个更隐蔽、却可能更具弹性的结构性变化正在发生：那些被认为“过时”的成熟制程存储芯片，正在被重新定义。\n\n某外资投行最新发布的半导体研报中，一个被多数投资者忽略的信号值得认真审视。Kioxia在其投资者日上展示了一款基于SLC NAND的高性能SSD产品，其IOPS超过一亿，延迟极低，且明确兼容Nvidia的Storage-Next解决方案。这款产品的核心用途，是作为GPU内存的扩展，解决系统内存瓶颈。\n\n这不是一个孤立的产品发布。它揭示了一个正在成型的逻辑链条：当AI推理和数据库加速场景对“读速”和“延迟”的敏感度超过对“存储密度”的追求时，那些被主流叙事抛弃的SLC NAND、MLC NAND等“旧”技术，反而找到了新的、高价值的应用场景。\n\n这份报告的核心判断是：**成熟制程存储（Legacy NAND/NOR）的AI化应用，正在打开一个被市场忽视的增量市场，其影响可能不亚于HBM的爆发，但对受益标的的选择逻辑完全不同。** 真正值得关注的，不是那些追逐先进制程的厂商，而是那些在成熟制程上拥有产能、客户关系和成本优势的“隐形冠军”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI对存储的需求正在从“大容量”转向“低延迟+高IOPS”\n\n过去两年，市场对AI存储的讨论几乎完全被HBM和GDDR所占据。逻辑很简单：大模型训练需要海量带宽，HBM是唯一选择。但这一叙事忽略了一个关键转折点——AI正从训练阶段加速进入推理和部署阶段。\n\n推理场景对存储的需求与训练截然不同。训练追求的是“吞吐量”，而推理追求的是“响应速度”。当一个AI模型需要实时处理用户查询、在数据库中快速检索、或执行大规模图计算时，存储的延\n\n[... middle omitted ...]\n\n有更详细的模型和图表。这些细节，欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nNAND闪存的新战场：AI存储需求爆发\n\n旧存储，新使命\n\n某外资投行最新研报指出，传统NAND技术正在AI数据中心找到全新应用场景，这个转变值得关注。\n\n1/ 老技术的新角色\n铠侠在IR Day上展示的GP系列SSD，采用传统SLC NAND芯片，却能实现1亿+IOPS的超高性能。关键在于它专门用来扩展GPU内存，解决系统内存瓶颈，加速AI推理和数据库处理。\n\n2/ 为什么是旧技术？\n传统NAND虽然密度不如3D NAND，但读写速度极快、延迟极低。研报认为，数据中心对快速存储的需求正在扩大这类芯片的市场空间，这是此前被低估的增量。\n\n3/ 国内存储厂商的机会\n研报覆盖的兆易创新、华邦电、旺宏都是传统NAND供应商。铠侠的验证信号，意味着这三家厂商可能受益于AI数据中心对高性能存储的需求扩张。\n\n4/ 供给端也在收紧\n旺宏方面，研报判断MLC和传统TLC NAND在2026下半年可能出现短缺，缺口可达40%，而能填补这个缺口的只有旺宏。\n\n**一点思考**\nAI浪潮不仅带动HBM等先进存储，传统NAND也在边缘找到新定位。当市场都在追逐最新技术时，成熟工艺的差异化价值反而被重新发现。\n\n#学习笔记\n\n[so\n\n[... middle omitted ...]\n\n Kioxia's proprietary SLC chip.\n\nImplications for Greater China memory stocks: We mentioned in our note, Old Memory: Upside Surprise Ahead, that legacy NAND technology could be ideal for fast \n\n[... middle omitted ...]\n\n2026)</td><td>NT$5,515.00</td></tr><tr><td>Silicon Motion (SIMO.O)</td><td>O (05/06/2024)</td><td>US$301.27</td></tr><tr><td>WinWay Technology Co Ltd (6515.TW)</td><td>O (04/17/2026)</td><td>NT$8,080.00</td></tr></table>"
  },
  {
    "id": "R030",
    "title": "AI正在重写澳洲零售业的竞争规则，但市场可能低估了数据资产的价值",
    "digest": "[wechat_article.md]\n# AI正在重写澳洲零售业的竞争规则，但市场可能低估了数据资产的价值\n\n当一家超市巨头的AI助手为门店员工节省了10万小时的重复劳动，当另一家零售商的AI系统让80%的员工开始主动选择班次，当一家百货公司用AI驱动的库存系统让缺货率降至历史最低——这些不是未来愿景，而是澳大利亚零售与消费品行业正在发生的真实变化。\n\n某外资投行最新发布的研报，首次对覆盖的18家澳大利亚零售与消费品公司进行了系统性的AI采用率基准评估。这份分析的价值不在于告诉市场“AI很重要”——这已经是共识。它的真正贡献在于：用量化的方式揭示了不同企业在AI竞赛中的真实位置，并提出了一个关键判断——AI正在成为改写行业竞争格局的结构性变量，而市场可能低估了数据资产和全链条AI整合带来的长期价值。\n\n报告的核心发现是：AI采用率的差异已经清晰可见，且呈现出明显的“规模效应”和“数据禀赋效应”。在满分为1.0的评分体系中，只有Wesfarmers获得了1.0的满分，Coles、Woolworths、Endeavour Group和Briscoe Group紧随其后，得分在0.80-0.83之间。而一些知名零售商如Premier Investments仅得0.08，Universal Store得0.17，Lovisa得0.33。这种分化不是偶然的，它指向了行业分水岭的形成。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI采用率的差距正在转化为运营效率的结构性差异\n\n评分体系覆盖了六个维度：供应链与物流、市场营销、销售与客户体验、门店运营、组织与支持职能、产品开发与创新。每个维度得分为0（无证据）、0.5（部分或初步证据）或1（明确采用）。整体得分是各维度平均分。\n\n这个评分方法的精妙之处在于，它不仅衡量“是否在用AI”，更衡量“AI渗透的广度”。\n\n[... middle omitted ...]\n\n些问题的答案，可能隐藏在这份报告没有完全展开的细节和图表中。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n澳洲零售AI布局，谁跑在最前面？\n\nAI落地全景图\n\n澳洲零售巨头AI应用深度拆解\n\n某外资投行刚出了一份澳洲零售消费板块的AI应用研报，我帮你把核心逻辑扒出来了👇\n\n**1. 六大维度打分**\n研报用6个维度给18家公司做了AI采用评分：供应链物流、营销、销售客户体验、门店运营、组织支持、产品创新。每项0/0.5/1分，取平均。\n\n**2. 头部选手很集中**\nWesfarmers满分1.0，AI渗透到每个环节。Coles和Woolworths都是0.83，短板都在产品创新（未公开披露）。Endeavour Group也是0.83，但供应链物流没得分。\n\n**3. 优势企业的共同点**\n- 拥有大规模高质量一手数据（长期会员计划积累）\n- AI应用从数量转向质量，覆盖全业务而非单点\n- 内部AI组织能力强，有完善治理架构\n\n**4. 重点看Wesfarmers**\nKmart用AI做需求预测+RFID库存可见性，Bunnings的AI助手帮员工实时查产品信息，价格标记工具省了10万小时人工。OneData数据资产有1250万用户记录，支撑精准营销。\n\n**5. Coles的亮点**\nOcado驱动的客户履行\n\n[... middle omitted ...]\n\nStore Operations; (5) Organization & Support Functions; and (6) Product Development & Innovation. This data is based on publicly available information, which may not incorporate all progress i\n\n[... middle omitted ...]\n\ncom/sa/en/cssa.html.\n\n© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.\n\n![](images/c68bf75c9351f76c2c0507357127c6995e99fab4a34d6d6422ee46f48bf2d2ef.jpg)"
  },
  {
    "id": "R031",
    "title": "人民币中间价的真实信号，市场可能低估了",
    "digest": "[wechat_article.md]\n# 人民币中间价的真实信号，市场可能低估了\n\n在人民币汇率讨论几乎被贸易摩擦和资本流动叙事主导的当下，一份来自某外资投行的每日中间价模型报告，往往被市场视为短期交易噪音。但如果我们把时间线拉长，把模型输出的数字与政策日历、历史误差模式放在一起看，一个更关键的判断正在浮现：**人民币中间价的定价逻辑，正在经历一次从“被动跟随”到“主动校准”的微妙切换，而市场对此的定价远不充分。**\n\n这份于2026年6月4日发布的模型报告，其核心输出——6.7773的模型投影——本身并不令人震惊。真正值得关注的，是模型投影较前值大幅下移411个基点，以及计入逆周期因子后的6.7971。这两个数字之间的差值，以及模型在过去一年中持续出现的系统性误差，共同指向了一个尚未被广泛讨论的结论：当前人民币中间价的定价机制，已经不再是简单的“一篮子货币+逆周期因子”公式，而是正在成为一个更具前瞻性的政策信号工具。市场如果仍然用旧框架去理解中间价，就会持续误判政策意图，进而错失资产定价的关键拐点。\n\n以下，我们将基于这份研报的模型输出与数据细节，拆解这一判断背后的五个核心层次。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 模型投影的骤降不是技术修正，而是政策意图的前置表达\n\n报告显示，6月4日的模型投影为6.7773，较前值6.8184大幅下移411个基点。即便计入逆周期因子，投影值仍为6.7971，较前次定价低213个基点。这个幅度的变化，绝非简单的隔夜市场波动所能解释。\n\n我们需要理解模型的工作原理。这类模型通常基于一篮子货币的隔夜变动、利差、以及市场情绪指标，来估算次日中间价的“无干预”水平。411个基点的单日变动，意味着模型捕捉到了来自多个币种的显著贡献。报告中的“Top 4 weighted contribution”图表显示，俄罗斯\n\n[... middle omitted ...]\n\n，并定期组织闭门讨论，拆解这些尚未被市场充分定价的关键变量。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n人民币中间价，盯住这个数字就够了\n\n6.7971\n\n一个关键参考点，看懂汇率风向\n\n最近在看一份外资投行的汇率研报，核心逻辑很清晰，分享给大家参考。\n\n1/ 模型预测了一个关键数字：6.7971\n这是考虑了逆周期因子后的中间价预测值，比之前的定价低了213个基点。简单说，模型认为人民币有升值空间。\n\n2/ 四个货币是主要驱动力\n卢布（+15.5个基点）、澳元（+15.0）、日元（+7.0）贡献了升值压力，韩元（-10.5）则拖后腿。汇率不是单一因素决定的，是多个货币的博弈结果。\n\n3/ 模型误差在收窄\n从年初的-1800个基点，到近期稳定在600左右，模型预测的准确度在提升。研报未给出具体原因，推测是市场波动趋于平稳。\n\n4/ 下半年有几个关键时间点\n7月底的政治局会议、10月国庆长假、11月APEC会议、12月的中央经济工作会议。这些节点都可能影响汇率走势。\n\n研报还提到年底可能有重要外交事件，不过具体影响需要观察。\n\n大家觉得6.80这个位置，是短期支撑还是压力位？欢迎一起讨论。\n\n#学习笔记\n\n[source_mineru.md]\n# USD/CNY fix model\n\nGlobal Markets \n\n[... middle omitted ...]\n\ne (without counter-cyclical factor)  \n![](images/a753b66ecd31548d9e36207a12729a671cd4de59a2fe923cd49b00cca006b4a2.jpg)\n\n<details>\n<summary>bar chart</summary>\n\nTop 4 weighted contribution to p\n\n[... middle omitted ...]\n\nrmation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R032",
    "title": "日本汽车股的分化才刚刚开始：HEV能力正在重新定义竞争壁垒",
    "digest": "[wechat_article.md]\n# 日本汽车股的分化才刚刚开始：HEV能力正在重新定义竞争壁垒\n\n2026年5月的日本和美国汽车销量数据，表面上看只是月度波动的常规更新。日本市场同比增长2.8%，美国市场微增0.4%，这样的数字很难激起投资者的兴奋。但这份来自某外资投行的月度追踪报告揭示了一个更重要的结构性信号：在看似平稳的行业总量背后，各家公司的竞争地位正在发生根本性位移。真正值得关注的不是销量本身，而是谁在HEV（混合动力）产品线上拥有真正的护城河，以及这种能力如何转化为定价权、库存管理和利润质量。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 日本本土市场的增长掩盖了丰田与日产之间日益扩大的鸿沟\n\n日本市场5月销量同比增长2.8%，连续两个月实现同比正增长。注册车辆（非轻自动车）增长5.6%，轻自动车下降2.1%，这种结构性分化本身就值得解读。报告明确指出，税收政策调整对注册车辆的利好更明显，这意味着政策红利并非均匀分布。\n\n但更关键的是主要厂商的表现分化。丰田同比增长8.3%，得益于畅销MPV车型Noah和Voxy的改款，以及Land Cruiser FJ的推出。本田也实现了4%的同比增长，新BEV车型Super ONE和2月推出的CR-V HEV贡献明显。而日产则同比下降6%，注册车辆更是大跌16%。\n\n这种分化不是偶然的月度波动，而是产品周期和战略执行力的系统性差异。丰田和本田正在收获前几年产品规划的红利，而日产在经历转型阵痛。对于投资者来说，这意味着日本本土市场不再是“一荣俱荣”的beta游戏，而是越来越考验各家产品竞争力的alpha战场。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 美国市场的HEV渗透率正在重塑竞争格局，丰田和本田是最大赢家\n\n美国市场5月销量1,480千辆，同比\n\n[... middle omitted ...]\n\n策略和估值隐含假设，帮助你在分化中找到真正的alpha机会。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日系车5月销量：HEV才是真正的胜负手\n\nHEV才是关键\n\n5月日系车在日美两大市场表现分化，但共同点是：HEV（混动）车型正在主导增长逻辑。\n\n**日本市场：丰田强势，日产承压**\n- 5月日本零售33.3万辆，同比+2.8%，连续两月正增长\n- 丰田+8.3%，靠的是Noah/Voxy改款和Land Cruiser FJ\n- 本田+4%，受益于新BEV Super-ONE和CR-V HEV\n- 日产-6%，注册车辆销量下滑16%，压力不小\n\n**美国市场：HEV需求撑起半边天**\n- 5月美国零售148万辆，同比+0.4%，SAAR回升至1620万辆\n- HEV销量25.6万辆，同比+33%——油价高企，省油才是硬道理\n- 丰田基本持平（-0.6%），靠Camry和新RAV4的HEV稳住\n- 本田+10%，CR-V HEV创纪录\n- 日产+11%，靠美国本土生产的Rogue/Pathfinder/Frontier\n- 马自达+35%，CX-50 HEV和低价Mazda3拉动\n\n**关键看点**\n1. 丰田和本田的HEV阵容让它们几乎不需要降价促销——丰田激励仅1843美元，本田2747美元，远低于行业均值\n\n[... middle omitted ...]\n\nMay-2026 Japan sales +2.8% YoY: May-2026 Japan retail sales totaled 333 thousand units, up 2.8% YoY, marking two consecutive months of YoY increase. By segment, registered vehicles totaled 21\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R033",
    "title": "印度数据中心：市场真正低估的不是需求，而是电力基础设施的再定价",
    "digest": "[wechat_article.md]\n# 印度数据中心：市场真正低估的不是需求，而是电力基础设施的再定价\n\n当外资在2025年初新加坡与香港的路演中反复追问“印度数据中心如何布局”时，一个被忽视的事实已经浮出水面：印度数据中心容量预计将从当前的1.5GW增长至2030年的5-8GW，而中东局势的持续紧张正在将这一数字推向区间上沿。某外资投行最新发布的研报指出，这一轮增长的核心驱动力并非AI算力的爆发性需求，而是电力基础设施的稀缺性正在成为整个产业链的定价锚。\n\n这份报告的价值不在于它确认了数据中心建设的热度，而在于它揭示了一个关键的结构性转变：在印度，谁掌握“土地+电力”的稀缺组合，谁就掌握了数据中心产业链中最不可替代的议价权。对于投资者而言，这意味着传统的“买设备、卖设备”逻辑正在让位于“买电力、买土地”的资产重仓逻辑。\n\n报告的核心判断是：印度数据中心产业链的价值分配正在从轻资产的运营服务向重资产的电力基础设施倾斜。这一判断的支撑来自三个层次：美国市场的经验验证、印度本地竞争格局的独特性、以及电力资产定价模型的根本性变化。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 美国市场的教训：真正跑赢的不是技术玩家，而是拥有“可调度电力”的公用事业公司\n\n报告对美国数据中心市场的回顾提供了一个极具说服力的参照系。在美国，数据中心需求增长最快的两个区域是PJM（东部）和ERCOT（德州），2015-2025年间这两个区域的电力需求因数据中心而分别实现了23%和26%的年复合增长率。但真正值得关注的是，在这两个区域中表现最好的股票并非数据中心运营商，而是那些拥有天然气和核电机组的公用事业公司。\n\nVistra、Constellation Energy和NRG Energy在过去四年中股价上涨了4-8倍，而NextEra和Dominion等同行则表现平平。报告\n\n[... middle omitted ...]\n\n，值得在更深入的讨论中继续推敲。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n印度数据中心：资产重玩法正在成型\n\n数据中心不只是科技故事\n\n最近和外资机构聊了一圈，大家共识很明确：印度数据中心这波还没走完。但怎么投？有三种路径——设备商（发电机、光纤、电气设备）、公用事业、以及建+持有数据中心的重资产公司。这篇重点聊后两种。\n\n🔌 印度数据中心到底能长多大？\n行业讨论显示，受中东局势影响，印度DC容量到2030年可能从现在的1.5GW冲到5-8GW的上沿。Nav-Mumbai的地价已经炒到比上一轮还高。资本开支方面，不含计算硬件，每MW大约50 Cr卢比，比美国低。\n\n🏢 资产拥有者：两种模式\n1️⃣ 地产房东模式（Colocation）\n建好数据中心租给超大规模云厂商/企业，客户自带GPU。典型玩家是Digital Realty、Equinix。回报周期约5年，资本效率高，技术过时风险由客户承担。\n\n2️⃣ 云服务商模式（Neocloud）\n自己买GPU，可能租也可能自建机房。每IT MW收入是Colocation的8-10倍，但资本开支也高得多（~4500万美元 vs 800-1500万），合同期更短，技术淘汰风险更大。\n\n美国市场上，Colocation玩家如Equinix、Di\n\n[... middle omitted ...]\n\nre-Hong Kong in Feb, foreign investors were clear that one has to position for data-centers even within India and the wave is yet to hit (they have been right till now!). One can invest via i)\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R034",
    "title": "重卡市场的真正拐点不在总量，而在动力系统的加速切换",
    "digest": "[wechat_article.md]\n# 重卡市场的真正拐点不在总量，而在动力系统的加速切换\n\n某外资投行在5月重卡销售数据更新报告中，揭示了一个被市场低估的结构性变化。2025年5月，中国重卡批发量约10.3万辆，同比增长16%，但环比下降12%。这个数字本身并不算惊艳——市场对“基建刺激”和“国四淘汰”的预期已经消化了相当一部分。真正值得关注的是隐藏在总量数据之下的动力系统裂变：新能源重卡渗透率逼近40%，而LNG重卡销量却环比暴跌55%。\n\n这份报告的核心判断是：重卡市场的竞争逻辑正在从“总量周期博弈”转向“动力系统结构性定价”。柴油、LNG、纯电三条技术路线的此消彼长，将重新定义主机厂、零部件供应商和运营商的利润分配格局。投资者过去习惯用“重卡销量同比增速”来锚定行业景气度，但接下来的关键变量不再是卖了多少辆车，而是这些车用什么动力系统在跑。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 新能源重卡正在跨越“渗透率临界点”，但市场仍用传统周期框架来定价\n\n5月新能源重卡零售销量达到2.87万辆，同比增长90%，环比增长3%，渗透率已接近40%。这个数字意味着什么？在任何一个工业品市场中，当渗透率突破30%之后，往往意味着从“政策驱动”进入“经济性驱动”阶段。新能源重卡的全生命周期成本（TCO）优势，在特定场景（港口、矿山、短途运输）中已经可以覆盖初始购置成本溢价。\n\n然而，大多数行业分析仍将重卡视为“基建投资的滞后指标”，用固定资产投资增速来预测销量。这种框架忽略了动力系统切换带来的“换购需求”——车队运营者不是因为业务扩张而买车，而是因为运营成本优势而主动替换存量柴油车。报告指出，5月柴油重卡零售销量约为2.1万辆（推算值），而新能源重卡已经达到2.87万辆。这意味着在零售端，新能源重卡已经超越柴油重卡成为主力车型。\n\n这个变化对主机厂的意\n\n[... middle omitted ...]\n\n信群里继续探讨这些结构性变量，以及它们对不同标的的定价含义。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n重卡五月数据出炉，EV渗透率逼近40%\n\n🚛重卡市场在分化\n\n5月国内重卡批发约10.3万辆，同比+16%，但环比-12%。环比走弱的核心原因：LNG重卡卖不动了。\n\n1️⃣ 柴油-LNG价差收窄，LNG经济性优势下降，加上主要主机厂去库存，LNG重卡零售仅1.38万辆，环比暴跌55%，同比也下滑2%。\n\n2️⃣ 新能源重卡是最大亮点。5月销量2.87万辆，同比+90%，环比+3%，月度渗透率已接近40%。电动化在重卡领域的替代速度比很多人想象的要快。\n\n3️⃣ 出口端保持稳定，约3.4万辆，同比+28%，环比微降2%。\n\n整体来看，重卡市场正在经历结构性切换：传统柴油+LNG需求疲软，但EV重卡正在快速补位。如果价差持续不利于LNG，下半年EV渗透率可能还会继续走高。\n\n重卡电动化的节奏，值得持续跟踪。\n\n#学习笔记\n\n[source_mineru.md]\n02 Jun 2026 00:07:09 ET | 8 pages\n\n## China HDT\n\nMay HDT Sales Update; Strong EV Growth Offset by Weak LNG Demand\n\n## CITI'S TA\n\n[... middle omitted ...]\n\nrrowed spread of diesel-LNG price gap. The export number was in-line at around 34k units (+28% YoY/-2% MoM).\n\nJeff Chung $^{AC}$\n\n+852-2501-2787\n\njeff.m.chung@citi.com\n\nKyle Wu\n\n+852-2501-8483\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R035",
    "title": "欧洲电力需求的结构性拐点：市场低估的不是复苏，而是电气化的二阶效应",
    "digest": "[wechat_article.md]\n# 欧洲电力需求的结构性拐点：市场低估的不是复苏，而是电气化的二阶效应\n\n过去十年，欧洲电力需求几乎在原地踏步。2010年至2023年间，年均增速不足0.5%，光伏和风电的大规模并网甚至让部分时段出现负电价。市场习惯了“电力需求无增长”的假设，所有资产定价模型都建立在低增长、高波动的基础上。\n\n但这一假设正在被打破。根据某外资投行最新研报，2025年欧洲电力需求同比增长约1.5%，而2026年至今增速已进一步攀升至约2%。西班牙、德国、意大利、英国和葡萄牙均录得正增长。这不是一次性的气候扰动，也不是短期的经济复苏脉冲——驱动因素来自三个结构性力量：热泵、电动汽车和工业电气化。这三者叠加，正在从根本上改变欧洲电力需求曲线的斜率。\n\n报告的核心判断是：电气化与AI数据中心需求的共振，将催生一代人级别的盈利超级周期。我们的分析进一步认为，市场目前定价的仍是“温和增长”，而非“结构性加速”。这意味着，公用事业、可再生能源设备商和电网基础设施提供商的估值，存在系统性重估的空间。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 热泵与电动汽车正在将家庭用电量翻倍，而市场将其视为边缘变量\n\n电气化的微观逻辑远比宏观数据更有说服力。报告提供了一组关键数字：2025年欧洲安装了约250万台热泵，如果将家庭供暖从燃气转换为热泵，典型家庭的用电量将直接翻倍。同一时期，欧洲电动汽车销量超过200万辆，占据新车销售约20%的份额，将家庭主力车型替换为电动车同样意味着家庭用电量翻倍。\n\n这两个数字单独看并不惊人，但它们的叠加效应正在改变电力需求的结构性底座。传统上，欧洲电力需求的主要波动源是工业和商业活动，居民用电相对稳定。而热泵和EV的普及，意味着居民部门正在从“刚性需求”转向“增长引擎”。更关键的是，这两项技术的渗透率仍处于早期阶段。热泵\n\n[... middle omitted ...]\n\n多细节数据，逐一拆解这些公司的竞争壁垒与风险敞口。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n欧洲用电量悄悄涨了2%，背后藏着什么？\n\n📈 电力需求回暖\n\n欧洲用电量正在加速增长。今年前几个月，西班牙、德国、意大利、英国和葡萄牙的平均用电量同比上升约2%，比去年1.5%的增速更快。这不是短期波动，而是电气化进程在推着需求往上走。\n\n🔌 三大驱动力\n\n1️⃣ 热泵加速普及。去年欧洲安装了约250万台热泵，一户家庭改用热泵供暖，用电量直接翻倍。\n\n2️⃣ 电动车渗透率提升。去年欧洲卖出超200万辆电动车，占新车销量近20%。一辆家庭主力车换成电车，用电量同样翻倍。\n\n3️⃣ 工业电气化。电锅炉制蒸汽（可达400°C），经济性已经优于燃气锅炉，工厂正在加速替换。\n\n⚡️ 电气化+AI=超级需求周期\n\n电气化叠加AI应用爆发和数据中心建设，电力消费将大幅攀升。某外资投行给出的激进情景是：到2029-2030年，电力需求年增速达到5%。这意味着未来几年需要投入约3.5万亿欧元用于发电（主要是可再生能源）和电网建设。\n\n🧭 值得关注的三大方向\n\n1️⃣ 正在加速电气化转型的公司（如Naturgy、Enel、Engie），未来3-5年资本开支将显著增长。\n\n2️⃣ 可再生能源开发商（如RWE、Orsted）和设备制\n\n[... middle omitted ...]\n\nbles the consumption of a typical household. (2) Electric cars: in Europe more than 2 mn EVs were sold last year (representing a near 20% share of new car sales); switching a family’s primary \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R036",
    "title": "市场真正低估的不是需求，而是供给侧信心的重建",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是需求，而是供给侧信心的重建\n\n过去两个月，中国房地产市场的叙事正在发生一次不易察觉但意义深远的切换。\n\n2025年四季度到2026年初，市场关注的焦点几乎全部集中在需求端：政策还能不能进一步松绑、居民购房意愿何时触底、二手房成交量能否持续。但5月的数据揭示出一个更值得关注的变化——供给侧的信心正在重建。开发商开始愿意以更高的溢价拿地，而这一行为背后隐含的判断，比任何单月销售数字都更具结构性意义。\n\n某外资投行最新发布的研报明确指出，5月土地市场出现早期复苏信号，全国土地出让降幅收窄，平均溢价率从4月的6%回升至10%。上海、苏州、南京等地出现多宗高溢价成交，其中中海在苏州以高出底价30%的价格获取一幅住宅地块，创下该省单价纪录。这不是孤例。5月29日上海出让的五幅地块中，四幅溢价率在17%至40%之间。\n\n这些数字放在一起，指向一个被市场普遍低估的结论：开发商正在用真金白银投票，重新相信这个市场有定价权、有利润空间、有可持续的需求。而这一信心的重建，才是支撑后续股价和估值修复的真正底层变量。\n\n报告同时覆盖了5月销售数据、二手房市场表现以及个股偏好，但其最核心的洞察，并不是“销售回暖”，而是“开发商行为正在从防御转向主动”。这一转变的可持续性，将决定未来6至12个月板块的投资逻辑是否能够从“政策博弈”切换为“基本面驱动”。\n\n以下是我们从这份报告中提炼出的五个关键层次。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 5月销售的分化不是周期性的，而是结构性的：优质国企正在与行业脱钩\n\n5月六家优质国企开发商平均实现同比正增长，其中华润置地增长28%，越秀增长18%，中海增长14%。而同期民营开发商的平均同比跌幅为40%。这一分化不是简单的“国企比民企好”，而是反映了两个根本性的差异：一是可售资\n\n[... middle omitted ...]\n\n地溢价率和高端项目去化率的变化，帮助大家建立自己的决策框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月楼市，国企领跑信号明确\n\n**楼市正在悄悄分化**\n\n5月销售数据出来了，几家头部国企交出了不错的成绩单。某外资投行最新研报显示，覆盖的6家高质量国企开发商5月销售额平均同比增长转正，华润置地+28%、越秀+18%、中海+14%领跑。这些公司的股价在5月平均涨了7%，而恒指是-2%。\n\n**三个关键信号值得关注**\n\n1/ **土拍市场开始回暖**\n5月29日上海5块地卖了约110亿，其中4块溢价17%-40%成交。苏州、南京也出现高溢价地块——中海在苏州拿了块地，溢价30%，创下省单价纪录。全国土地出让跌幅从4月的41%收窄到5月的36%，平均溢价率从6%升到10%。开发商开始敢拿地了，说明信心在重建。\n\n2/ **上海二手房创5年新高**\n5月上海二手房成交量突破2.8万套，达到5年最高水平。国家统计局数据显示，二手房价格已连续3个月环比上涨。研报认为这不是短期政策刺激的反弹，而是购买力改善和财富效应带来的结构性支撑。\n\n3/ **高端改善需求依然坚挺**\n深圳高端项目持续热销，杭州几个单价10万+的豪宅项目也备受关注。这说明改善型需求没有消失，只是在向优质产品集中。\n\n**值得持续观察的方向**\n研\n\n[... middle omitted ...]\n\ne prices rose on average by 7% (vs HSI: -2%) in May, primarily reflecting their improving fundamentals, although a recent pause indicates market concern over the sustainability of the rebound \n\n[... middle omitted ...]\n\nb07e6e7656fbfe475cb50f.jpg)\n\n# Newsletters\n\nSubscribe to our monthly collection of free to view reports and interviews in Open Pass or read our bite-sized round up of research covering our nine key themes, Talking Points"
  },
  {
    "id": "R037",
    "title": "市场真正低估的不是需求，而是供给侧的再定价",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是需求，而是供给侧的再定价\n\n中国自动化与机器人行业正在经历一个被多数投资者误读的周期。2026年开局，MIR数据显示工厂自动化销售额同比增长7%，创下2022年四季度以来最强单季表现。投行研报同步上调全年展望，从之前的10%增长修正至13%。这些数字本身并不令人震惊——真正值得关注的，是数字背后正在发生的结构性变化：市场已经从“需求是否在复苏”的争论，转向了“谁能将强劲的订单流转化为可盈利的发货”这一更尖锐的问题。\n\n这个转变意味着什么？意味着过去两年依赖行业beta的简单投资逻辑正在失效。2025年，大多数自动化股票完成了一次轻松的估值重评。但进入2026年，市场奖励的不再是“谁站在风口上”，而是“谁能在成本波动、供应链紧张和竞争加剧的三重压力下，依然保持利润率的稳定甚至扩张”。换句话说，供给侧的再定价——而不是需求的边际改善——正在成为决定胜负的关键变量。\n\n这份研报的核心贡献，不在于它确认了复苏，而在于它揭示了复苏的“质量差异”。它给出了一个清晰的框架：当订单不再是瓶颈、交付能力成为新约束时，行业的分化将从“谁增长更快”演变为“谁的增长更有质量”。以下是我们从报告中提炼出的五个核心洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮复苏的真正瓶颈不是需求，而是交付能力和供应链韧性\n\n报告中最值得注意的信号，并非需求数据本身，而是供给侧正在形成的约束。多家头部企业在近期交流中一致表示，“订单不是瓶颈，交付才是”。一家大型自动化平台计划在2026年二季度将产能提升约30%，以消化一季度的订单积压。这种产能扩张的紧迫感，暗示着当前需求强度已经超出了行业此前的预期。\n\n更关键的是，这种供给约束并非均匀分布。在PLC和伺服系统等核心品类中，头部企业凭借更强的供应链韧性和产品组合优势，正在获\n\n[... middle omitted ...]\n\n。我们将基于这份研报的完整内容，提供更深入的拆解和持续跟踪。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n制造业回暖，谁是赢家？\n\n订单回暖，分化加剧\n\n某外资投行最新研报指出，中国制造业自动化（FA）市场进入2026年态势更稳，一季度销售额同比+7%，是2022年四季度以来最强表现。但复苏并非雨露均沾——赢家正加速分化。\n\n1/ 复苏结构变了\n- 电子、半导体、机器人、新能源车相关资本开支仍是增长主力\n- 传统项目（油气、冶金、石化）需求依然偏弱\n- 一句话：市场奖励“对的方向+对的执行”，而非普涨\n\n2/ 龙头加速收割份额\n- 汇川技术在小PLC/中大PLC/伺服领域份额分别同比+6/2/2个百分点\n- 埃斯顿在工业机器人领域巩固头部地位，与汇川、KUKA并列9.7%份额\n- 外资品牌如三菱电机在伺服领域丢失2个百分点份额\n- 赢家通吃格局强化\n\n3/ 交付能力成新瓶颈\n- 订单不是问题，交付才是\n- 某头部企业计划二季度提升约30%产能以消化积压订单\n- 标准产品订单到交付通常1-3个月\n\n4/ 人形机器人：远期期权，但已影响供应链\n- 2026年业绩仍以工业自动化和机器人为核心\n- 人形机器人需求加剧精密零部件产能紧张\n- 绿的谐波作为谐波减速器供应商，是更明确的受益方\n\n5/ 定价权成为分水岭\n- 原材\n\n[... middle omitted ...]\n\nh players can convert robust order flow into profitable shipments.” MIR’s 1Q26 review shows FA sales up 7% Y/Y—the strongest since 4Q22—while IA and PA rose 2% Y/Y and 1% Y/Y, respectively. MI\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R038",
    "title": "香港零售复苏的真正瓶颈不在游客，而在拼多多",
    "digest": "[wechat_article.md]\n# 香港零售复苏的真正瓶颈不在游客，而在拼多多\n\n香港4月零售数据同比增长9%，相比3月的13%有所放缓。表面上看，这不过是基数效应下的温和正常化。但这份研报揭示了一个更值得关注的信号：剔除汽车和电器两个异常高增长品类后，整体零售增速从8%进一步降至6%，而可选消费增速更是从14%腰斩至8%。更关键的是，与2015-2018年平均值相比，4月零售额仍低15%，比3月的9%差距进一步扩大。\n\n市场可能将注意力集中在游客恢复节奏上——5月游客同比增长9%，与4月的10%基本持平，并未出现明显恶化。但真正值得追问的问题是：为什么游客回来了，零售却回不去？\n\n答案隐藏在另一张图表里。拼多多在香港的月活跃用户从2024年4月的65万飙升至2026年4月的215万，两年翻了3.3倍。这才是结构性变量——跨境电商正在重塑香港零售的定价权和客流分配逻辑。市场低估的不是需求恢复的速度，而是供给端竞争格局的不可逆变化。\n\n以下五个层次，帮你拆解这份报告的核心判断框架。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 可选消费增速首次放缓，但真正的拐点信号来自“剔除异常值之后”\n\n4月可选消费同比增长13%，是自2025年二季度以来首次出现增速回落。表面看，珠宝钟表仍录得20%的同比增长，似乎不算差。但报告特意做了两个剔除操作：一是剔除汽车和电器，增速从13%降至8%；二是对比2015-2018年基准，可选消费销售额仍低27%，比3月的22%差距进一步扩大。\n\n这意味着什么？珠宝的高增长可能更多受金价波动影响，而非消费意愿的真实回升。当金价回调，珠宝增速从3月的28%降至4月的20%，就是一个佐证。而汽车和电器的异常高增长——分别达到46%和22%——显然不可持续，可能反映的是特定促销或换购周期的脉冲性需求。\n\n真正值得关注的是百货商店\n\n[... middle omitted ...]\n\n未解问题，结合更多行业数据和公司调研，做进一步的推演和验证。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n香港零售回暖，但房东还在等风来\n\n零售回暖，房东还在等\n\n4月香港零售额同比+9%，比3月的13%小幅回落。与2015-18年均值比，4月仍低15%，比3月的-9%更差一些。\n\n去掉汽车(+46%)和电器(+22%)两个异常值，整体零售增速回落到+6%，比3月的+8%继续放缓。\n\n1️⃣ 弹性消费 vs 必需消费\n\n弹性消费继续跑赢必需消费：+13% vs +5%。去掉汽车和电器后，弹性消费从+14%降到+8%。\n\n珠宝首饰增速从3月+28%放缓到+20%，研报推测跟金价回落有关。\n\n必需消费连续两个月+5%，与2015-18年均值持平，说明基本盘还算稳。\n\n2️⃣ 未来怎么看？\n\n游客增量有限：5月到港游客同比+9%，跟4月的+10%差不多，没明显改善。\n\n接下来几个月零售增速预计维持在5-10%，但下半年基数会变高。\n\n⚠️ 拼多多在香港的月活用户从去年4月的65万暴涨到今年4月的215万，跨境电商渗透正在挤压本地零售。\n\n3️⃣ 房东的困境\n\n零售数据回暖还没传导到租金端。某外资投行对两大零售房东保持中性看法，认为租金重签还没转正。\n\n不过其中一只房东（股息率>6%+有资本循环潜力）的上行风险更大——这\n\n[... middle omitted ...]\n\narrivals not seeing a particularly notable improvement (+9% Y/Y in May vs. +10% Y/Y in April) (Figure 9), we expect retail sales to stay at 5-10% Y/Y growth over the next few months (but the b\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 02 Jun 2026 11:36 PM HKT\n\nDisseminated 03 Jun 2026 04:00 AM HKT"
  },
  {
    "id": "R039",
    "title": "香港零售增速放缓背后：市场真正低估的不是消费降级，而是供给侧的再定价",
    "digest": "[wechat_article.md]\n# 香港零售增速放缓背后：市场真正低估的不是消费降级，而是供给侧的再定价\n\n四月香港零售销售数据出炉，同比增长8.6%，低于彭博预期的13.7%，也较三月的12.8%明显回落。表面上看，这是一份“不及预期”的报告。但如果只读到“放缓”两个字，就可能错过这份研报最值得关注的判断：香港零售的结构性分化正在加速，而市场对资产价格的影响尚未充分定价。\n\n这份来自某外资投行的研报，真正有价值的洞察不在于数据本身，而在于它揭示了一个正在发生的转折——消费行为的分层正在从“周期性波动”演变为“结构性重塑”。奢侈品和电器销售依然强劲，但百货公司和超市正在被电商和跨境消费侵蚀。这不仅仅是消费信心的波动，更是零售资产估值逻辑的重构。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 奢侈品与必需品的背离不是短期现象，而是消费分层正在固化\n\n四月数据中最值得关注的不是总量放缓，而是品类之间的分化。珠宝钟表等奢侈品销售同比增长19.8%，电器类增长21.9%，两者均保持两位数增长。但与此同时，百货公司销售下滑6.7%，超市虽然恢复正增长（+3%），但增速远低于整体水平。\n\n这种分化并非四月独有。回溯过去几个季度的数据，奢侈品和耐用消费品一直领跑，而大众零售持续承压。研报给出的解释是财富效应和活跃的住宅市场仍在支撑高端消费。但更深层的含义是：香港消费市场正在从“共同富裕”走向“两极分化”。高端消费者受益于资产价格回升和人民币走强，而中低收入群体的实际购买力并未同步改善。\n\n这意味着，零售资产的估值逻辑需要重新审视。高端零售物业的租金议价能力可能比市场预期的更持久，而大众零售物业的租金下行周期可能比市场预期的更长。研报提到，Link REIT的香港零售组合租金正在趋于稳定，但租金调整指引仍然保守（FY27E预计同比下降8%）。这恰恰印证了我们的\n\n[... middle omitted ...]\n\n标的（如Link REIT、香港本地REITs）的定价含义。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n香港四月零售数据，透露了哪些信号？\n\n香港零售回暖，但节奏在变\n\n四月香港零售销售同比+8.6%，低于市场预期的13.7%，但和机构预测一致。整体来看，前四个月累计增长11.3%，消费复苏还在继续，只是速度在放缓。\n\n1. 奢侈品和电器依然强，但环比降温\n珠宝钟表等奢侈品同比+19.8%，电器+21.9%，延续了年初以来的强劲。但和三月相比，增速都在回落。财富效应和活跃的楼市依然在支撑，但边际动能减弱。\n\n2. 超市回暖，百货承压\n超市重回正增长（+3%），但百货商店继续下滑（-6.7%）。耐用消费品整体增长19.8%，比三月的28.2%明显放缓。消费结构在变化，线上渠道正在挤压传统零售。\n\n3. 汽车销售“末班车”效应\n汽车销售同比+46.1%，但远低于三月的81%。原因是“OfO换车计划”到期前的集中购买。燃油销售则因成本上升而下滑。\n\n4. 线上零售加速渗透\n四月线上零售同比+30.6%，前四个月累计+30.2%。研报认为，随着内地电商进一步渗透，香港大众零售可能继续承压。\n\n5. 内地游客回归成亮点\n五一黄金周期间内地访港游客同比+11.5%，整个五月访港游客增长9.5%。人民币走强也提升了内地游客的\n\n[... middle omitted ...]\n\n YoY (Mar:+81%) on last-minute purchase due to expiry of 'OfO replacement scheme'. Fuel sales dropped on rising cost.  \n(-) But online retail sales jumped 30.6% YoY (4M26: +30.2%). Mass retail\n\n[... middle omitted ...]\n\n/tr><tr><td>Wharf REIC (1997.HK)</td><td>U (12/13/2024)</td><td>HK$24.10</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted."
  },
  {
    "id": "R040",
    "title": "香港零售增速放缓背后，真正值得关注的不是需求，而是结构分化",
    "digest": "[wechat_article.md]\n# 香港零售增速放缓背后，真正值得关注的不是需求，而是结构分化\n\n2026年4月香港零售数据出炉，整体同比增长9%，符合市场预期，但相比3月的13%和2M26的12%明显减速。表面看，这是一次温和的正常化回调。但如果把数据拆开，你会发现一个更值得警惕的信号：驱动增长的三大引擎——黄金、iPhone、电动车——都在同步降温。剔除消费电子和汽车后，4月零售增速已降至6%，低于3月的8%和2M26的9%。这意味着香港零售的“底色”不仅没有加速，反而在边际走弱。\n\n这份来自某外资投行的研报，虽然聚焦于月度零售数据跟踪，但其背后揭示的，是香港消费生态正在经历一次结构性的再平衡：游客结构变了、消费场景变了、本地居民的支出流向变了。对于持有香港零售物业的投资者来说，真正需要回答的问题不是“下个月增速是5%还是7%”，而是“当前的增长质量是否可持续”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 奢侈品增速放缓但量价关系出现关键分化，真正考验的是品牌定价权\n\n4月奢侈品销售同比增长20%，较3月的28%明显回落。但更值得拆解的是量价关系。报告特别指出，剔除价格影响后，奢侈品销量同比增速为6.5%，与3月的6.4%基本持平。这意味着奢侈品的减速完全来自价格效应，而非需求萎缩。\n\n这个分化的含义是什么？一方面，金价走弱正在拖累以珠宝为主的奢侈品销售金额，但实际购买量并未下降。另一方面，这也说明奢侈品的“量”已经稳定在一个平台上，未来增速能否回升，取决于品牌能否在价格端重新找到上涨动能。但考虑到当前香港与内地价差收窄、内地免税渠道持续扩张，品牌在香港市场的定价权正在被动削弱。\n\n报告没有完全展开的是：如果金价继续回落，奢侈品销售金额增速可能进一步承压，而如果品牌选择降价促销来保量，则利润率将面临侵蚀。这对以奢侈品为主要租户的零售房东\n\n[... middle omitted ...]\n\n口的驱动因素，以及不同零售物业标的在这个框架下的相对吸引力。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n香港零售四月遇冷，黄金iPhone撑场\n\n📉 四月零售放缓\n\n4月香港零售额同比+9%，低于3月的+13%和2月的+12%，增速连续两个月下滑。三大增长引擎——黄金珠宝、新iPhone和电动车——都出现边际减弱。\n\n剔除电子产品（+22%）和汽车（+46%），4月零售实际增速只有+6%，比3月的+8%更低，说明基础消费在降温。\n\n💎 奢侈品：量稳价跌\n\n奢侈品4月同比+20%，比3月的+28%明显回落。但剔除价格因素后，销量同比+6.5%，跟3月的+6.4%基本持平。金价高位拉高了名义销售额，但实际卖出去的数量变化不大。\n\n超市倒是回暖了，4月同比+3%，之前几个月一直在0附近徘徊。\n\n🧭 五月展望\n\n研报预测5月零售增速在5-8%之间。几个支撑点：\n- 大陆游客4月同比+12%，海外游客+3%，客流还在恢复\n- 香港居民北上趋势稳定在+10%左右，没有进一步加速\n- 金价如果走弱，可能会拖累奢侈品增速\n\n🎯 关注方向\n\n奢侈品增速放缓对高端零售地产（如海港城、时代广场）不是好消息。超市回暖则对民生类REITs有正面意义。\n\n#学习笔记\n\n[source_mineru.md]\n# First Read\n\n# \n\n[... middle omitted ...]\n\nall three key categories have seen a moderation in growth. Excluding consumer electronics (+22% YoY in April) and motor vehicles and parts (+46% YoY in April), April retail sales growth would \n\n[... middle omitted ...]\n\ncom/sa/en/cssa.html.\n\n© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.\n\n![](images/f7c23a9f411f54fa2c28fa2656856125f1dc72493a950fad154989ae365f17ff.jpg)"
  },
  {
    "id": "R041",
    "title": "618大促揭示的真正信号：国货美妆的份额增长已从“故事”变为“结构”",
    "digest": "[wechat_article.md]\n# 618大促揭示的真正信号：国货美妆的份额增长已从“故事”变为“结构”\n\n如果你只看了今年618第一阶段的天猫榜单，可能会得出一个模糊的结论：国货品牌表现“稳住了”。珀莱雅继续第一，可复美和薇诺娜维持了去年的排位。\n\n但这份稳定，恰恰是市场最容易误读的信号。\n\n某外资投行在最新发布的研报中，系统拆解了天猫618第一阶段（5月21日至30日）以及抖音5月全月的销售排名数据。对比去年同一时期，真正值得关注的不是“谁还在前十”，而是“谁在往上走、谁在往下掉”，以及这些位移背后所折射出的行业竞争结构变化。\n\n报告的核心判断是：中国化妆品行业整体延续了自去年双十一和今年女神节以来的温和改善趋势。但在这个“温和”的表象之下，国货品牌与国际品牌之间正在发生一次非对称的格局重塑。而毛戈平，是这一轮结构性变化中最具代表性的标的。\n\n这不是一次简单的促销周期波动。它涉及品牌定价权、渠道效率、消费者心智迁移等多个层面的深层变量。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 天猫榜单的“稳定”只是表象，真正的位移发生在高端价格带\n\n从天猫618第一阶段的排名来看，国货品牌整体表现稳健。珀莱雅蝉联第一，可复美、薇诺娜分别守住第12和第14位。表面上看，国货似乎只是在原地踏步。\n\n但把目光转向国际品牌，变化就剧烈得多。修丽可从第5跃升至第2，SK-II从第7升至第4，而巴黎欧莱雅从第3跌至第8，兰蔻从第2滑至第5。赫莲娜也后退了两位。\n\n这意味着什么？国际品牌内部正在发生一次“高端化再排序”。排名上升的品牌，无一例外都是客单价更高、品牌溢价更强的奢侈或专业级品牌。排名下滑的，则是那些过去依靠大众市场放量的品牌。\n\n这背后的含义是：在天猫这个以品牌心智为主导的平台上，消费者的购买决策正在向更高价格带集中。而在这个价格带里，国货品牌长期缺席\n\n[... middle omitted ...]\n\n继续讨论，我们会持续跟踪这些变量，并在关键节点分享更新判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n618国货美妆成绩单，谁在悄悄升咖？\n\n国货稳住，毛戈平升咖\n\n618第一阶段（5/21-5/30）和抖音5月销售数据出炉，整体美妆行业延续了双11和女神节的温和回暖趋势。天猫上国货品牌排名基本稳住了，但国际品牌排名洗牌更猛。\n\n1️⃣ 天猫618第一阶段：国货守位，毛戈平突围\n- 珀莱雅稳坐#1，Comfy和薇诺娜分别守住#12和#14\n- 毛戈平从去年的#17升到#15，是国货里唯一在高端线有存在感的品牌\n- 国际品牌变动大：修丽可从#5→#2，雅诗兰黛#4→#3，SK-II#7→#4，兰蔻从#2跌到#5，欧莱雅从#3跌到#8\n- 前20依然被国际高端品牌主导，但大众市场国货明显领先\n\n2️⃣ 抖音5月：国货全面碾压，新品牌崛起\n- 抖音榜单变化比天猫剧烈得多，国货占12席（天猫只有4席）\n- 珀莱雅从去年618的#2升到#1\n- 谷雨从#12跳到#5，百雀羚从#14到#9，林清轩新进前20\n- 国际品牌多数持平或下滑：赫莲娜#3不变，雅诗兰黛#5→#8，兰蔻#7→#10，SK-II#9→#12\n- 只有CPB从#20微升到#18\n\n3️⃣ 毛戈平为什么值得关注？\n- 它是天猫前20里唯一的高端国货，也是\n\n[... middle omitted ...]\n\nomestic brands improved while international brands declined in rankings. Mao Geping remains our top Buy in the China cosmetics sector.\n\nTmall's 618 sales results in stage 1 — The stage 1 of Tm\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R042",
    "title": "AI Agent不是概念，是硬件架构的重新定价",
    "digest": "[wechat_article.md]\n# AI Agent不是概念，是硬件架构的重新定价\n\n2026年的Computex，表面上看新品寥寥，但真正值得关注的信号藏在两场keynote的细节里。NVIDIA和Qualcomm不约而同地将大量时间花在同一个主题上：Agentic AI。这不是概念宣讲，而是对整个计算架构的一次重新定义。\n\n某外资投行在最新发布的Computex takeaways中，给出了一个值得产业决策者反复推敲的判断：Agentic AI正在从云端走向边缘，而这一过程将触发硬件供应链的深层重构。市场目前关注的仍是GPU的供需缺口，但报告暗示，真正被低估的变量，是CPU在AI时代重新获得定价权，以及由此带来的整个半导体生态的新TAM。\n\n以下是这份报告的核心逻辑拆解，以及那些报告没有完全展开、但值得你持续追踪的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. NVIDIA的Windows PC芯片不只是产品发布，而是对x86兼容性的一次压力测试\n\nNVIDIA在Computex上发布了与联发科合作的首款Windows PC处理器N1X（RTX Spark）。这颗芯片筹划了约两年，覆盖桌面、笔记本和工作站，目标是将1 petaflops的AI能力和120B参数大模型运行能力带到终端设备。从技术参数看，这无疑是边缘AI的重要里程碑。\n\n但报告特别点出了一个关键制约：x86应用的兼容性问题。这正是此前Qualcomm ARM PC增长受阻的核心原因。NVIDIA的N1X能否成功，不仅取决于硬件性能，更取决于应用生态的重构速度——尤其是传统x86应用能否在ARM架构下无缝运行。\n\n这里的产业含义是：PC换机周期的到来，并不取决于AI芯片的发布，而取决于用户是否真的需要本地AI Agent来替代现有的应用工作流。如果Agentic AI的\n\n[... middle omitted ...]\n\n感兴趣，欢迎加入，我们可以一起把这些问题拆得更细、聊得更透。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nNVIDIA 和联发科联手做了颗 PC 芯片\n\nAI PC 新变量\n\nN1X 芯片能把智能体带到你的笔记本上\n\n---\n\nComputex 2026 刚结束，某外资投行出了一份深度解析。我挑几个关键点，帮你快速看懂这波 AI 硬件的新趋势。\n\n1/ NVIDIA 终于出了 PC 芯片，叫 N1X\n- 这颗芯片是 NVIDIA 和联发科合作了约 2 年的成果，覆盖台式机、笔记本和工作站。\n- 算力达到 1 petaflops，能跑 1200 亿参数的大模型，上下文窗口高达 100 万 token。\n- 目标是把 AI Agent 直接带到你的设备上，不再依赖云端。\n- 对联发科来说，这大概只贡献 1-2% 的收入（主要是 ARM CPU 授权和连接芯片），但帮它打开了计算市场的大门。\n\n2/ 两大巨头都在押注“智能体 AI”\n- NVIDIA 把智能体拆成 4 个部分：大脑（LLM）、身体（编排层）、工具、运行环境。GPU、CPU、DPU 全都要用上。\n- 高通 CEO 预测，到 2030 年 token 消耗量将增长 40 倍。智能体工作负载会逐渐从云端分散到设备端，可能触发一波换机潮。\n- 研报特别提到：苹\n\n[... middle omitted ...]\n\nng high-end token processing capabilities to the PC. NVIDIA envisions this to become a key enabler in bringing AI Agents to client devices with 1 petaflops of AI capability, and the ability to\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 02 Jun 2026 10:50 AM HKT\n\nDisseminated 02 Jun 2026 10:50 AM HKT"
  },
  {
    "id": "R043",
    "title": "市场真正低估的不是电动车需求，而是汽车供应商的800V技术迁移能力",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是电动车需求，而是汽车供应商的800V技术迁移能力\n\n当投资者仍在争论电动车渗透率何时见顶时，一份来自某外资投行的研报提出了一个截然不同的叙事框架：汽车供应商真正的增长期权，可能不在四轮上，而在AI数据中心和电池储能系统里。\n\n这份研报的核心判断非常直接——汽车零部件公司为800V电动车架构积累的技术能力，恰好是下一代AI数据中心和储能系统最稀缺的基础设施组件。这不是一个“可能有机会”的模糊判断，而是一个有产品、有路径、有时钟的增量市场迁移。\n\n更关键的是，这份报告指出，当前市场对这些公司的估值，几乎完全没有反映这一增量。换句话说，如果这个判断成立，部分汽车供应商正在被市场以“传统周期股”的框架定价，而它们实际上拥有一个几乎纯增量的、与AI基础设施挂钩的增长期权。\n\n为什么这件事现在变得重要？因为2025年的市场环境与2018年截然不同。当时市场对自动驾驶和电动车的狂热，更多建立在消费者接受度、监管推动和远期技术上。而今天AI数据中心的资本开支和储能需求，背后是真实的经济回报和明确的电力基础设施升级路径。报告特别指出，当前来自汽车和非汽车投资者对AI相关机会的兴趣，已经达到2018年自动驾驶/电动车狂热时期的高点，但这一次的底层逻辑更扎实。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 800V架构迁移正在创造一个新的电力基础设施供应链\n\n理解这个机会，首先要理解一个技术事实：下一代AI数据中心正在从传统的400V架构转向800V直流电架构。\n\n原因并不复杂。随着GPU集群密度持续提升，传统的电力输送方式遇到了物理瓶颈。在更低电压下，要传输相同功率需要更大的电流，这意味着更粗的电缆、更多的热量、更高的能量损耗。800V架构的核心优势在于，通过提高电压来降低电流，从而在同样的功率下大幅减少热损耗\n\n[... middle omitted ...]\n\n着什么，以及市场何时会开始重新定价这些“隐藏的AI供应商”。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n800V技术，从电动车杀入AI数据中心\n\n800V新战场\n\n汽车零部件的新增长曲线在哪？\n\n最近读了一份某外资投行的研报，聊的是汽车零部件公司的新机会。核心观点很明确：800V高压技术正在从电动车领域，向AI数据中心和储能系统延伸。\n\n这意味着什么？👇\n\n**1/ 为什么是800V**\n传统数据中心用400V，随着GPU集群密度提升，散热、效率、成本都面临瓶颈。800V架构能减少能量损耗，缩小电缆尺寸，支持更高密度的算力部署。NVIDIA预计2027年将首次部署800V架构。\n\n**2/ 汽车公司的独特优势**\n汽车零部件企业早已为800V电动车投资了相关技术，尤其是在功率电子领域。他们擅长管理复杂供应链、大规模制造、高精度生产。这些能力在数据中心和储能领域几乎是100%增量机会。\n\n**3/ 哪些公司最受益**\n研报认为，BWA、APTV、ST这三家定位最清晰：\n- BWA已推出TurboCell产品、储能系统和双向微电网逆变器\n- APTV的高压连接器和汇流排能力，使其非汽车业务年增长目标8-10%更可信\n- ST的传感器和接触器在液冷方案中有新应用场景\n\n**4/ 市场规模有多大**\nUBS数据显示，全\n\n[... middle omitted ...]\n\nuto companies have deep specialization skills (many with relevance to other areas), run lean manufacturing, and manage complex supply chains. These skills can lead to opportunities in energy g\n\n[... middle omitted ...]\n\ncom/sa/en/cssa.html.\n\n© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.\n\n![](images/4d62d32ca05b9729e2d90a5cc438c16d97c2ffd53922f522855669d87513ddb2.jpg)"
  },
  {
    "id": "R044",
    "title": "世界杯对啤酒销量的拉动，被市场高估了",
    "digest": "[wechat_article.md]\n# 世界杯对啤酒销量的拉动，被市场高估了\n\n过去几个季度，几乎每一场北美饮料公司的业绩会，管理层都会主动提及2026年世界杯。从Molson Coors到Constellation Brands，再到Boston Beer，大家不约而同地将这场赛事描述为“重要的啤酒时刻”。市场情绪也随之升温，投资者开始提前定价一个“世界杯行情”。\n\n但在这份由某外资投行发布的研报中，分析师基于历史数据和公司高管真实表态，给出了一个与市场直觉相悖的判断：世界杯对啤酒销量的年度拉动幅度，很可能不到1%。\n\n这不是一个令人兴奋的数字。但恰恰是这种克制，才值得认真对待。当所有人都在谈论“催化剂”时，真正需要回答的问题是：这个催化剂到底能催化多少？以及，它催化的是销量，还是别的什么？\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 历史数据揭示的真相：世界杯的销量拉动远低于市场直觉\n\n研报系统梳理了最近三届世界杯——2014年巴西、2018年俄罗斯、2022年卡塔尔——在主办国的啤酒销量变化。结果很清晰：世界杯年份确实有增量，但幅度远非“爆发式”。\n\n巴西2014年，啤酒总销量同比增长3.5%。俄罗斯2018年，增长3.2%。卡塔尔2022年增长32.1%，但卡塔尔的啤酒市场体量极小，年均销量仅为巴西或俄罗斯的约千分之一，这个数字不具备可比性。\n\n更关键的是，分析师将世界杯效应与北美本土的超级碗进行对比。Nielsen数据显示，超级碗当周能为啤酒销量带来约7%的季节性提振。但世界杯是持续数周的赛事，如果把超级碗的周度效应换算成年化影响，再结合世界杯的比赛密度和消费场景，最终得出的年度拉动幅度不足1%。\n\n这个数字意味着什么？对于年收入数十亿美元的啤酒公司来说，世界杯带来的增量可能只相当于一到两周的正常销量。它不足以扭转行业的下行趋势，更不足\n\n[... middle omitted ...]\n\n多数据分析框架，帮助你在市场情绪之外，建立更扎实的判断依据。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n2026世界杯，啤酒能多卖多少？\n\n世界杯能救啤酒吗？\n\n某外资投行出了一份测算，结论挺有意思：世界杯对啤酒确实是好事，但别指望它翻盘。\n\n1/ 啤酒这几年确实不太好过\n消费者口味变了，健康意识上来了，整个酒精饮料行业都偏冷。啤酒尤其明显，销量一直在负区间晃悠。行业自己也知道，所以把2026世界杯当成了一个难得的催化剂。\n\n2/ 公司们怎么看？\n几家大啤酒公司（Molson Coors、Constellation、Boston Beer）口径很一致：世界杯是重要事件，能拉动社交场景和线下消费，但没人把它当成销量核弹。更多是把它看作一个超长营销窗口，而不是需求拐点。有家公司原话是“如果销量能涨1%就算大件事了”。\n\n3/ 历史数据怎么说？\n- 过去三届世界杯：德国（2006）啤酒月销量涨了约9%，巴西（2014）涨3.5%，俄罗斯（2018）涨3.2%，卡塔尔（2022）涨32%（基数小）\n- 美国本土参照：超级碗期间啤酒销量比季节性趋势高约7%\n- 但放到全年来看，世界杯给美国啤酒的增量可能不到1%\n\n4/ 2026年能指望什么？\n研报判断：在美加墨这三个啤酒主战场，预计会有低个位数（LSD）的销量和销售额提\n\n[... middle omitted ...]\n\nevent that could provide incremental uplift to volumes. Against this backdrop, we thought it would be interesting to examine the event's potential impact on beer and the broader Beverage Alcoh\n\n[... middle omitted ...]\n\ncom/sa/en/cssa.html.\n\n© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.\n\n![](images/cc32bece69c8ba7850c4f8410e00d26fea899f4cba52cbf9f9dba667d47cf895.jpg)"
  },
  {
    "id": "R045",
    "title": "市场真正低估的不是需求，而是华为LogicFolding的供给端突破",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是需求，而是华为LogicFolding的供给端突破\n\n半导体行业从来不缺宏大叙事，但真正能改变产业底层逻辑的突破，往往在初期被市场以“不过是另一种封装方案”的轻率判断所低估。某外资投行最新研报指出，华为在ISCAS 2026上披露的LogicFolding技术，极有可能成为继DeepSeek之后中国半导体产业又一个被低估的结构性转折点。\n\n市场当前的质疑集中在三个层面：认为LogicFolding不过是现有3DIC方案的翻版、认为该技术仍停留在论文阶段、以及认为全球领先企业可以快速复制。但研报通过技术细节拆解和商业化时间表验证，给出了截然不同的判断：这或许是中国半导体在缺乏EUV光刻机条件下，实现芯片性能持续提升的最重要路径之一。\n\n这份报告的价值不在于罗列技术参数，而在于它揭示了一个被忽视的事实——当外部限制迫使企业在基础设施层面进行创新时，往往会催生出传统路径依赖下不可能出现的突破。正如DeepSeek在算力受限时倒逼出推理成本数量级下降，华为在光刻机受限时，正在封装和设计协同优化上开辟一条新路。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 核心质疑的底层逻辑错误：LogicFolding不是堆叠芯片，而是重构芯片\n\n市场最常见的误解，是将LogicFolding等同于TSMC的SoIC、Intel的Foveros Direct或Samsung的3D Cube。如果只是堆叠两个独立设计的芯片，那么晶体管密度提升的同时，功耗和发热也将翻倍，最终导致频率下降而非提升。但华为Kirin 2026芯片的实际数据给出了相反的结果：能效提升41%，频率提升13%。\n\n这个矛盾本身就说明，LogicFolding不是传统意义上的封装技术。它的核心差异在于：不是把两个已经设计好的独立芯片（通常是逻辑+\n\n[... middle omitted ...]\n\n在社群中分享完整的原始研报、技术细节图表以及后续的跟踪框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n华为的芯片突破，被低估了\n\nLogicFolding，不只是堆叠\n\n华为的Tau Scaling Law，可能又是一个DeepSeek时刻\n\n最近某外资投行发了一篇研报，专门拆解华为在ISCAS 2026上发布的“Tau Scaling Law”里的核心技术——LogicFolding。市场质疑很多，但这份报告认为，它可能被严重低估了。\n\n1/ 为什么不是简单的3D堆叠？\n很多人说LogicFolding和台积电SoIC、英特尔Foveros没区别。但华为Kirin 2026芯片的数据打了脸：功耗效率提升41%，频率提升13%。如果是简单堆叠，发热会导致降频，不可能同时做到这两点。\n\n2/ 真正的杀手锏：从设计阶段就开始“折叠”\nLogicFolding不是把两个做好的芯片叠在一起，而是在设计阶段就把一个逻辑电路拆开，分配到两个垂直堆叠的晶圆层上。这样晶体管之间的连线大幅缩短，功耗和延迟自然下降。Kirin 2026一个核心的线长减少了30%。\n\n3/ 为什么别人很难复制？\n要实现这种效果，需要同时搞定三件事：新的EDA工具、新的电路设计方法、先进封装。全球大部分芯片设计公司不会为了一项未成熟的技术去改整个流\n\n[... middle omitted ...]\n\n improve chip performance through stacking. Recent market feedback remains skeptical, but the skepticism appears to underappreciate how different LogicFolding is from existing 3DIC packaging s\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R046",
    "title": "市场低估的不是中国创新药的短期回调，而是结构性定价重置的起点",
    "digest": "[wechat_article.md]\n# 市场低估的不是中国创新药的短期回调，而是结构性定价重置的起点\n\nASCO 2026 落幕后的两周，中国医药板块经历了一场罕见的集体杀跌。恒生医疗保健指数自 2025 年高点已回撤超过 30%，部分创新药公司的 1 年远期市销率已经跌至甚至低于 2024 年 4 月的底部。某外资投行的最新研报直接点出了一个令产业决策者无法回避的问题：在基本面没有出现任何实质性负面变化的情况下，资本为何如此决绝地离场？\n\n这份报告的核心判断并非简单的“超跌反弹”。它提出了一个更有张力的叙事：当前中国医药资产正在经历一次被动的“去杠杆式”定价重置，而这一过程恰好掩盖了 ASCO 上涌现出的几个真正具有结构性意义的信号——某些公司的临床数据，已经不再是“追赶”，而是在特定治疗领域开始定义新的标准。\n\n对于持有或关注中国医药资产的投资者而言，真正需要回答的问题不是“市场什么时候见底”，而是“当资金回流时，哪些资产会最先被重新定价”。这份研报给出了三个明确的候选者，而它们背后的逻辑，远比股价波动本身更值得深挖。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 当前估值已无法用基本面解释，但市场需要一个新的锚点\n\n研报中展示的估值图表令人警觉。以 1 年远期市盈率衡量，恒瑞医药从 2025 年 10 月峰值的 50 倍跌至当前的 31 倍，已低于 2024 年 4 月低点的 47 倍。翰森制药从 38 倍降至 26 倍，接近其 2024 年低点。更令人不安的是生物科技板块：科伦博泰的市销率从峰值的 39 倍压缩至 25 倍，而 2026-2029 年其收入复合增长率预计高达 66%；信达生物从 10 倍降至 6 倍，同期收入复合增长预期为 26%。\n\n这是一个典型的“增长溢价消失”场景。当宏观不确定性上升、全球资金从新兴市场回流美元资产时，\n\n[... middle omitted ...]\n\n整报告的解读版本，并定期组织对关键资产的跟踪讨论。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nASCO 后医药股跌惨了，但基本面没变差\n\n📉 跌出来的机会？\n\nASCO 刚结束，港股医药板块就迎来一波猛烈回调，估值已回到甚至低于 2024 年 4 月的低点。某外资投行指出，这次下跌并非基本面恶化，更像是资金面情绪驱动。当潮水退去，哪些公司值得关注？\n\n---\n\n**1️⃣ 科伦博泰：被低估的 ADC 龙头**\n\n- sac-TMT 在 1L PD-L1+ NSCLC 中展现出“最佳搭档”潜力：联合 K 药后，ORR 更高、肿瘤缩小更深、应答更持久，OS 获益趋势明确。\n- 在 2L+ EGFR 突变 NSCLC 中，它是唯一一个实现 OS 统计学显著改善的药物。\n- 全球首个 III 期胜利（晚期子宫内膜癌）由合作伙伴默沙东拿下，海外验证力很强。\n- 股价自 ASCO 后跌了 15%，但基本面在持续改善，属于“情绪杀”品种。\n\n**2️⃣ 信达生物：IBI363 是下一个重磅炸弹**\n\n- 在 2L+ 经 I/O 治疗的患者中，IBI363 展现了惊人的生存尾巴：鳞癌 24 个月 OS 48%，腺癌 43%，远超化疗和多西他赛。\n- 1L 患者中，ORR 高达 86%，是目前所有试验中最高的。\n- P\n\n[... middle omitted ...]\n\nital outflow, and at this point it's certainly beyond fundamentals. Nonetheless, here is a summary of post-ASCO views while waiting for the tide to turn.\n\nKelun-Biotech (O): sac-TMT emerges as\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R047",
    "title": "软件行业的真正拐点不在需求回暖，而在商业模型与AI落地的结构性重构",
    "digest": "[wechat_article.md]\n# 软件行业的真正拐点不在需求回暖，而在商业模型与AI落地的结构性重构\n\n过去几年，市场对欧洲软件与支付行业的关注，往往停留在宏观利率变化、估值震荡、以及需求周期的起落上。这些视角不是错的，但它们越来越不足以解释正在发生的深层变化。\n\n刚刚结束的某外资投行欧洲金融业年度会议上，来自Capgemini、Temenos、Wise、Zopa、Raisin以及该行数字资产与投行部门高管的密集对话，揭示了一个更值得关注的结构性信号：软件行业的竞争逻辑正在从“卖席位、卖订阅”转向“卖结果、卖消费”，而AI的落地方式正在决定谁能从这一轮转型中真正获利。\n\n这不是一个关于“行业是否复苏”的判断，而是一个关于“行业如何被重新定价”的判断。报告中的关键对话，指向了三个彼此独立却又彼此强化的趋势：商业模型从订阅转向基于token的消费定价，AI部署从概念验证进入生产阶段后对成本结构的重塑，以及支付与数字资产领域竞争壁垒的迁移。它们合在一起，意味着投资者评估软件公司时所用的框架，可能需要一次系统性更新。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 商业模型正在经历一次“从订阅到消费”的底层切换，这比任何需求变化都更深刻\n\nCapgemini的CTO在对话中提出了一个看似技术细节、实则影响深远的判断：企业软件的定价模型正在从以订阅为主，转向“订阅+基于token的消费”混合模式。推动这一变化的直接原因，是Agentic AI的兴起——当AI代理执行任务时，每次调用都会消耗token，而token成本会随任务复杂度非线性膨胀。\n\n这不是一个边际调整。如果token成为新的计价单位，那么软件公司的收入可预测性、毛利率结构、客户生命周期价值的计算方式，都将面临重构。对于CFO而言，IT预算正在被token消耗快速侵蚀，而企业需要决定是继续增加\n\n[... middle omitted ...]\n\n们如何基于这些结构性变化调整对欧洲软件与支付板块的观察视角。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n欧洲软件支付圈，最近在聊什么？\n\n欧洲金融会议上的关键发现\n\n这几天在苏黎世参加了欧洲金融会议，和几家软件支付公司聊完，几个趋势值得关注。\n\n**1. AI 从“有多少用例”转向“怎么用出价值”**\n某头部IT服务商CTO提到，过去一年大厂推出1200-1500个新AI服务，开源大模型200万个。企业不再数用例，而是聚焦怎么在业务场景里搭好语义层，让agentic AI真正产生价值。客户服务和风控是落地最密集的领域。\n\n**2. 定价模式在变：从订阅到订阅+消耗**\ntoken化AI让成本结构变了。任务越复杂，token成本越高，CFO们的IT预算压力山大。一些公司开始转向小模型/领域模型，用更少的token达成目标。\n\n**3. 银行核心系统替换，还有很大空间**\n某银行软件商坦言，目前核心银行软件渗透率仅35%（对比ERP/HR软件的80-90%）。银行过去抵触升级是因为周期太长，现在AI有望压缩实施时间。美国市场尤其活跃，已有20位销售人员在盯160家区域性银行。\n\n**4. 跨境支付：稳定币不是威胁**\n某跨境支付平台表示，客户目前更看重“能用、好用的余额”，稳定币还没形成实质替代。他们更关注通过平台\n\n[... middle omitted ...]\n\ntic layers around business context to leverage Agentic AI; 3) Optimisation of the cost base as a business model evolves towards consumption-based tokens; 4) Increased investment in marketing a\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R048",
    "title": "市场低估的不是AI概念，而是催化剂事件对盈利拐点的确认",
    "digest": "[wechat_article.md]\n# 市场低估的不是AI概念，而是催化剂事件对盈利拐点的确认\n\n过去六个月，中国互联网板块经历了一轮由AI叙事驱动的估值修复。但真正值得关注的信号，不是大模型发布会上的参数竞赛，而是一系列正在逼近的、可验证的盈利催化剂。某外资投行刚刚发布的催化剂预览报告，系统梳理了2026年三季度至四季度影响中国互联网、软件及数据中心公司股价的关键事件。这份报告的核心判断值得认真对待：市场正在从“相信故事”转向“验证数字”，而三季度将集中出现一批足以改变盈利预期的硬数据点。\n\n报告覆盖的催化剂事件横跨游戏、AI应用、在线旅游、数据中心等多个子行业，但贯穿其中的主线非常清晰——每一家公司的股价催化，都指向同一个问题：AI和宏观改善能否在财务上落地。这不再是概念炒作阶段，而是业绩兑现的检验期。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 游戏板块正在进入“爆款验证窗口”，三季度是关键分水岭\n\n报告中最引人注目的催化剂，集中在游戏公司的产品上线节点。网易的《Sea of Reminants》定档三季度，报告给出的年化流水预期是30亿元人民币，被定义为“网易2026年最重要的新游发布之一”。这个数字本身已经不小，但更值得关注的是它的战略意义——它将是网易在MMO品类上的一次集中火力检验，直接关系到市场对网易游戏管线价值的重估。\n\nBilibili的《三国：王霸天下》同样定档四季度，报告给出的年化流水预期是20亿元。对于Bilibili这样一家仍在探索游戏业务盈利模式的公司来说，这款产品能否达到甚至超越预期，将直接影响市场对其游戏业务是否具备“第二增长曲线”的判断。Bilibili的投资者日可能同期举行，如果游戏数据向好，叠加新回购计划，公司估值逻辑可能发生系统性变化。\n\n这里的关键洞察在于：游戏行业已经告别了“立项即涨”的阶段。现在市场\n\n[... middle omitted ...]\n\n微信群里继续讨论，我们可以基于报告原文做更深入的拆解和推演。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n下半年中概催化事件，提前划重点\n\n**催化剂密集期来了**\n\n6-9月是中概公司事件密集窗口，某外资投行梳理了多个潜在催化节点，挑几个值得留意的。\n\n**1/ 北森控股：FY26年报（6月22日）**\n重要性极高，研报预期AI ARR和收入端有望超预期。HR SaaS赛道，AI落地进度是核心看点。\n\n**2/ 美图：美图视觉节（6月17日）**\n重要性极高，预期会发布新AI产品、AI商业化进展及海外生产力工具更新。作为AI应用层标的，这波产品节奏值得跟踪。\n\n**3/ B站：Bilibili World（7月）+ 新游《三国：望天下》（Q4）**\nB站World可能配合投资者日，新游预期年化流水20亿。此外3Q可能推出新回购计划，上一轮额度已在2Q用完。\n\n**4/ 网易：《无限大》暑期上线 + 《逆水寒》手游大版本更新**\n《无限大》是网易2026年最重要的新游之一，预期年化流水30亿。6月26日《逆水寒》手游重大更新，参考去年《繁花》版效果，有望重新拉动这款长青产品。\n\n**5/ 快手：可灵等视频模型迭代（3Q）**\n可灵、SeeDance等模型迭代+ARR数据披露，若可灵有分拆动作，可能成为更强催化剂。\n\n[... middle omitted ...]\n\n2 2848-6918\n\n![](images/9e5dcc2f8863632785d449bcf0b9f19e8e5fc049ccd09f99ddac7014d964a8cf.jpg)\n\n<details>\n<summary>text_image</summary>\n\nAsia Summer School 2026\n</details>\n\n![](images/3789cfee5\n\n[... middle omitted ...]\n\nom Group Ltd (TCOM.O)</td><td>O (05/17/2021)</td><td>US$48.29</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R049",
    "title": "市场低估的不是AI数据中心是否需要储能，而是储能订单正在从“是否”转向“何时”",
    "digest": "[wechat_article.md]\n# 市场低估的不是AI数据中心是否需要储能，而是储能订单正在从“是否”转向“何时”\n\n过去半年，围绕AI数据中心（AIDC）是否需要配套储能系统（ESS），市场始终存在一个悬而未决的争论。怀疑者认为，AI负载的高波动性和不间断供电要求，本质上更适合依赖燃气轮机或传统UPS，电池储能不过是锦上添花。乐观者则押注，电力瓶颈将是AI算力扩张的最大约束，而储能恰恰是解锁这一约束的关键杠杆。\n\n这份来自某外资投行在2026年6月初发布的最新研报，提供了几个关键信号，足以让这场争论的天平发生倾斜。报告的核心判断并不复杂：AIDC对ESS的需求已经不再是“要不要”的问题，而是“什么时候大规模落地”的问题。而报告给出的时间表，比市场普遍预期的更近、更集中。\n\n真正值得关注的，不是需求本身，而是需求结构正在发生的变化——储能将从数据中心的后备角色，升级为电力架构的核心组件。这一变化将重新定义整个储能产业链的价值分配。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 三份公告正在重塑市场对AIDC ESS的认知框架\n\n研报引用了三个几乎前后脚发生的事件，它们共同指向一个方向：主流玩家已经用行动给出了答案。\n\n首先，西门子宣布与英伟达合作，并联合Fluence Energy开发面向下一代AIDC的参考电源与控制架构。在这个架构中，Fluence Energy贡献的是电池储能系统。这不是一个简单的产品供应协议，而是将储能写入AI工厂的电气蓝图——储能不再是可选项，而是模块化部署方案的标准组成部分。\n\n其次，Fluence Energy在2026年5月初宣布，已与两家超大规模云服务商签署了主供应协议（MAS），并预计在F3Q获得首批订单。超大规模客户是AIDC需求最集中、决策最审慎的群体。他们愿意签署MAS，意味着储能方案已经通过了内部的技\n\n[... middle omitted ...]\n\n提前捕捉信号？我们会在社群中分享更多来自产业一线的交叉验证。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAIDC配储，需求正在确认\n\nAI数据中心真的需要储能\n\n之前市场有疑虑，AI数据中心（AIDC）到底要不要配储能？最近几个信号表明，需求正在被验证。\n\n**1. 巨头联手，定义AIDC储能架构**\n西门子联合英伟达，与Fluence Energy合作，为下一代AIDC开发了标准化电力控制架构。Fluence提供电池储能系统，解决电力受限环境下的弹性与灵活性需求，支持黑启动、负荷平滑等功能。\n\n**2. 超大规模客户已签协议**\nFluence Energy已与两家超大规模云厂商签订主供应协议，首批订单预计在2026财年Q3落地。这说明AIDC储能的商业化正在加速。\n\n**3. 供应链已有订单落地**\n- 阳光电源在调研中透露，已收到来自数据中心电力开发商的储能订单\n- LG新能源与DTE Energy签署16亿美元合同，供应6GWh储能电池\n\n**4. 为什么现在才看到订单？**\n某外资投行组织的专家电话会指出：AIDC储能的安装顺序靠后，要等土建、发电、机房都建好才轮到。所以不是没需求，是节奏问题。真正的大规模采购还在后面。\n\n**5. 储能类型有讲究**\nAIDC储能和电网级储能是两回事。AIDC要求高\n\n[... middle omitted ...]\n\nnt visit to Sungrow, management shared a similar view that ESS is a major solution to AIDC power constraints and they have already received ESS orders from datacenter power developers. Meanwhi\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 02 Jun 2026 09:25 PM HKT\n\nDisseminated 02 Jun 2026 09:25 PM HKT"
  },
  {
    "id": "R050",
    "title": "日本游戏股被低估的不是业绩，而是AI带来的供给侧重塑",
    "digest": "[wechat_article.md]\n# 日本游戏股被低估的不是业绩，而是AI带来的供给侧重塑\n\n2026年过半，日本游戏板块的投资者正经历一种罕见的情绪：公司基本面强劲，但股价却持续承压。某外资投行最新发布的日本游戏行业季度报告直言，这是一个“令人沮丧的年份”。AI资本开支主题的资金虹吸效应，导致优质游戏公司的估值倍数持续压缩，即便那些盈利增速有望达到双位数的企业，当前PE也已显著低于多年均值。\n\n但这份报告真正值得关注的判断，并非“估值便宜”，而是：**市场正在用旧框架定价新逻辑**。\n\n投资者将日本游戏公司简单归入“消费者可选”或“内容制造”类别，忽视了AI正在从供给侧重塑游戏开发的成本结构、产能上限和竞争门槛。当Capcom将3,000-5,000小时的人工测试压缩至72小时，当月度自动化测试量达到3万小时，这不是成本节约的故事，而是产能释放的拐点。\n\n报告的核心张力在于：一边是AI带来的供给侧革命，另一边是市场因AI主题而忽视这些公司。这种错位，恰恰是当前最值得关注的定价机会。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. Capcom和Konami处于“业绩超预期、估值低水位”的罕见交集\n\n报告中最清晰的信号来自两家公司：Capcom和Konami。它们不是AI资本开支的直接受益者，但它们在执行层面几乎没有瑕疵。\n\nCapcom的新作Pragmata销量已超过公司计入FY3/27E指引的预期，而《怪物猎人：荒野》资料片的宣布概率正在上升。更关键的是，Capcom正在将AI工具嵌入核心开发流程：与Google合作，将人工测试时间从数千小时压缩至72小时，每月运行3万小时的AI辅助测试。报告认为，这正在帮助Capcom实现更密集的发布节奏，中型IP的产出能力明显提升。\n\nKonami方面，eFootball在4-5月的增长数据非常强劲，Sen\n\n[... middle omitted ...]\n\n”区间？这些讨论将帮助你把研报的洞察转化为可操作的观察框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本游戏股，被AI挤到了角落\n\n🎮 便宜的游戏公司\n\n2026年对日本游戏股来说有点难熬。AI资本开支吸走了大量资金，游戏公司即使基本面不错，估值也被压得很低。\n\n**Capcom和Konami是亮点**\n- Capcom的《Pragmata》销量超预期，《怪物猎人：荒野》资料片大概率明年2-3月上线\n- Konami的eFootball在4-5月增长强劲，Q1很可能大超预期\n- 两家公司PE都低于历史均值，但盈利增长确定性高\n\n**AI正在改变游戏开发**\nCapcom和谷歌合作AI，把人工测试从3000-5000小时压缩到72小时，每月还能跑3万小时自动化测试。AI在概念设计、本地化、社区反馈分析上已经普及。\n\n**GTA6会是个转折点？**\n全球游戏公司Q1收入增长11.3%，市场预期下半年加速主要靠GTA6。但日本厂商大多刻意避开了这个档期，GTA6发布后资金流向的变化反而可能利好它们。\n\n**几家值得关注的公司**\n- 任天堂：Switch 2和重制版计划让2027年更值得期待\n- Square Enix：老游戏销量稳住基本盘，但《勇者斗恶龙12》又延期了\n- Nexon：估值跌到地板价，但中国市场\n\n[... middle omitted ...]\n\n1 3 6777 6979\n\nhyrum.caesar@bernsteinsg.com\n\nA year of extremes. 2026 has continued to be a frustrating year for our Japan Video Gaming coverage. While the companies we like continue to do wel\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R051",
    "title": "日本网络安全赛道的真正分水岭：需求确认，但竞争格局正在被重写",
    "digest": "[wechat_article.md]\n# 日本网络安全赛道的真正分水岭：需求确认，但竞争格局正在被重写\n\n当市场还在为日本IT服务板块的景气度争论不休时，一份来自某外资投行对两家未覆盖网络安全公司的调研，揭示了一个远比“需求增长”更复杂的真相：网络安全需求确实强劲，但真正决定赢家的，不再是技术领先，而是能否在价格战、政策变化和云转型三重压力下，守住利润底线。\n\n这份报告走访了Techmatrix和Digital Arts两家公司。前者聚焦网络防火墙、医疗云和AI病理诊断，后者专注Web过滤和GIGA学校项目。两家公司都发布了低于中期计划的目标，但原因截然不同。放在一起看，它们恰好构成了日本网络安全市场“需求确认但利润承压”的完整拼图。\n\n对于关注日本科技板块的投资者而言，这组数据传递的信号远比表面复杂。以下是我们从中提炼的五个核心洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 网络安全基础设施业务正在成为利润引擎，但增长质量取决于能否维持88%的经常性收入占比\n\nTechmatrix的信息基础设施业务（以网络安全为主）在FY3/26第四季度实现了48%的营业利润同比增长，即便剔除一次性销售记账遗漏的影响，核心增速仍达35%。驱动因素来自三个方面：Palo Alto Networks的下一代防火墙、SOC自动化解决方案，以及Proofpoint的邮件安全产品。第四季度订单价值同比增长10%。\n\n更值得关注的是经常性收入占比。管理层披露，该业务的独立经常性销售比率在FY3/26达到88%。这意味着即使宏观经济波动，公司仍有稳定的收入底座。对于一家系统集成商而言，这是向SaaS化转型的重要标志。\n\n但这里有一个未被完全验证的假设：88%的经常性收入占比能否在价格竞争加剧的环境中维持？Techmatrix目前的主要产品多为云原生，受内存价格上涨和零部件\n\n[... middle omitted ...]\n\n的压力？以及，哪些公司更可能在云转型中建立可持续的竞争优势。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本网安双雄：谁在涨，谁在亏\n\n🔐 日本网安分化局\n\n某外资投行走访了两家网安公司，结论：安全需求整体强劲，但公司之间差距很大。\n\n1️⃣ Techmatrix：安全扛旗，医疗拖后\n- 信息安全业务FY3/27利润指引+10% yoy，下一代防火墙、邮件安全、SOC自动化是增长主力\n- 但医疗系统业务因合并AI病理诊断公司Medmain，利润指引-43% yoy，预计约5年才能盈利\n- 信息基础设施业务88%是经常性收入，抗周期能力强\n\n2️⃣ Digital Arts：份额被抢，利润承压\n- FY3/26营业利润4.79bn日元，大幅miss指引（5.61bn）\n- GIGA学校项目市场份额从95%跌到70%，对手价格砍到一半\n- 企业业务增长仅+1% yoy，新Z-FILTER产品单价是i-FILTER的3-4倍，但比外资便宜\n\n3️⃣ 两个有意思的看点\n- 经济产业省即将推行的安全措施评估体系，可能给整个网安行业带来需求增量\n- 两家公司都提到云化趋势在加速，但短期会压利润（上云初期投入大）\n\n整体来看，网安赛道景气度没问题，但个股分化明显。安全主业扎实的公司更抗跌，靠补贴项目冲量的要小心。\n\n欢迎一起\n\n[... middle omitted ...]\n\nthe medium-term plan, and once the amortization of its intangible fixed assets is finalized, the company expects the consolidation to depress near-term earnings. While security in the informat\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "Figure 1",
    "context": "Figure 1: Our supply chain stress indicator is surging again. The index rose 1.2 standard deviations in March–April; the second largest two-month increase since the pandemic induced increase in July 2020"
  },
  {
    "figure_id": "F002",
    "report_id": "R001",
    "label": "Figure 2",
    "context": "Figure 2: Initially\\*, the rise in US 10yr yields was driven predominantly by higher real rates rather than a more destabilising shift in inflation expectations or the policy outlook, which limited the transmission to spreads"
  },
  {
    "figure_id": "F003",
    "report_id": "R001",
    "label": "Figure 3",
    "context": "Figure 3: Oil & gas tankers passing through the Strait of Hormuz, in number of ships entering and exiting the Gulf. We saw some optimism in early April but negotiations are stalling"
  },
  {
    "figure_id": "F004",
    "report_id": "R001",
    "label": "Figure 4",
    "context": "Figure 4: Weak May PMIs suggest clear downside risk to Eurozone GDP growth in Q2. We see signs of inventory build up as companies try and anticipate further supply chain disruption"
  },
  {
    "figure_id": "F005",
    "report_id": "R001",
    "label": "Figure 5",
    "context": "Figure 5: From a monetary policy perspective, we see materially higher risks of multiple ECB hikes (UBSe +50bp in 2026) relative to the Fed (UBSe -25bp in 2026), which has effectively never reached neutral"
  },
  {
    "figure_id": "F006",
    "report_id": "R001",
    "label": "Figure 7",
    "context": "Figure 7: Asset manager S&P 500 futures positioning, which we use as a proxy for broader risk positioning, currently sits near 10-year highs. We therefore see limited room for additional institutional buying in credit from here, e"
  },
  {
    "figure_id": "F007",
    "report_id": "R001",
    "label": "Figure 8",
    "context": "Figure 8: Historically, the largest spread tightening following geopolitical resolutions has occurred when CTAs had previously been short credit. Current CTA longs in credit suggest limited tightening ahead, even if we see a resol"
  },
  {
    "figure_id": "F008",
    "report_id": "R002",
    "label": "Figure 1",
    "context": "\\- Equity Strategy is cautious: Citi's US Equity Strategy team has flagged that the Q1 earnings blowout has led to an equity rally that now appears to have priced euphoric expectations. Thematically, they prefer taking profit on price momentum – a factor that "
  },
  {
    "figure_id": "F009",
    "report_id": "R002",
    "label": "Figure 2",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. We define “earnings season” from the 10 $^{th}$ (or closest trading day) of the month following quarter-end to NVDA earnings +3 days. Figure 2. The equally-weighted S&P 500 is more sensitive"
  },
  {
    "figure_id": "F010",
    "report_id": "R002",
    "label": "Figure 3",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. We define “earnings season” from the 10 $^{th}$ (or closest trading day) of the month following quarter-end to NVDA earnings +3 days. Figure 3. Constituent vol vs index vol is at extreme lev"
  },
  {
    "figure_id": "F011",
    "report_id": "R002",
    "label": "Figure 4",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 4. This generally sees equities sideways/lower"
  },
  {
    "figure_id": "F012",
    "report_id": "R002",
    "label": "Figure 6",
    "context": "- Low put ownership could see chasing of put buying in risk-off, which is positive for vol. Vol squeezes fuel VAR-driven unwinds. ☐ Dealers may be long equities to hedge skewed positioning (they are the net call sellers to the market). Should equities start to"
  },
  {
    "figure_id": "F013",
    "report_id": "R002",
    "label": "Figure 6",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 6. Equities underperform in midterm years"
  },
  {
    "figure_id": "F014",
    "report_id": "R002",
    "label": "Figure 7",
    "context": "We reiterate the above factors suggest the distribution of outcomes for risk assets over the short-term has shifted to balanced/slightly bearish (compared to skewed positive over earnings). However, we still do not see an immediate trigger to suggest positioni"
  },
  {
    "figure_id": "F015",
    "report_id": "R002",
    "label": "Figure 8",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 8. Front-end risk curves remain steep; flattening into inversion is risk-negative"
  },
  {
    "figure_id": "F016",
    "report_id": "R002",
    "label": "Figure 8",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. - Vol curve flattening/vol of vol outperforming: We look at the shape of the front-end of the VIX curve, with quick flattening into inversion as an early/ coincidental signal (Figure 8). We "
  },
  {
    "figure_id": "F017",
    "report_id": "R002",
    "label": "Figure 10",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 10. S&P 500 trend higher remains intact; mild momentum divergence hints at correction risk"
  },
  {
    "figure_id": "F018",
    "report_id": "R002",
    "label": "Figure 11",
    "context": "- Strait closure exacerbates/yields surge: Markets are optimistic on the prospects of a deal that re-opens the Strait of Hormuz, with progress seemingly being made towards a deal. Should market expectations shift to a long closure, commodity prices could spike"
  },
  {
    "figure_id": "F019",
    "report_id": "R002",
    "label": "Figure 12",
    "context": "This is not necessarily a comprehensive checklist, simply some items we are closely watching. Narratives can often be applied retroactively to price action, though, so we watch for both the market reaction to events as well as the events themselves # Implicati"
  },
  {
    "figure_id": "F020",
    "report_id": "R002",
    "label": "Figure 13",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 13. G10 FX performance – equities down, yields up (2021–present, based on US 10y and S&P 500)"
  },
  {
    "figure_id": "F021",
    "report_id": "R002",
    "label": "Figure 15",
    "context": "As we’ve been noting, we are not necessarily outright bearish risk. Rather, we see increased potential for a correction – though timing and catalyst are uncertain. Pre-COVID, it was easier to think about FX hedges as the equities down/yields down regime was mo"
  },
  {
    "figure_id": "F022",
    "report_id": "R002",
    "label": "Figure 15",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 15. USDJPY implied vol is historically low and also below realized vol"
  },
  {
    "figure_id": "F023",
    "report_id": "R002",
    "label": "Figure 16",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. The other common theme when equities head lower is consistent underperformance by high beta/risk currencies. In light of the current backdrop (Figure 16), we would be hesitant to hedge risk-"
  },
  {
    "figure_id": "F024",
    "report_id": "R002",
    "label": "Figure 17",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 17. FX vol tends to drop into the World Cup"
  },
  {
    "figure_id": "F025",
    "report_id": "R003",
    "label": "Exhibit 2",
    "context": "Exhibit 2: We Find Slightly Stronger Evidence of a Short-term Increase in GDP for the Winning Nation Relative to Hosts, But Results are not Statistically Significant"
  },
  {
    "figure_id": "F026",
    "report_id": "R005",
    "label": "Exhibit 1",
    "context": "EXHIBIT 1: China smartphone sell-through shipment in April was down 15% MoM and 10% YoY. EXHIBIT 2: Low-tier smartphone shipment declined by 22% YoY in April, followed by mid-tier segment (-16% YoY). In comparison, high-tier segm"
  },
  {
    "figure_id": "F027",
    "report_id": "R005",
    "label": "Exhibit 4",
    "context": "EXHIBIT 1: China smartphone sell-through shipment in April was down 15% MoM and 10% YoY. EXHIBIT 2: Low-tier smartphone shipment declined by 22% YoY in April, followed by mid-tier segment (-16% YoY). In comparison, high-tier segm"
  },
  {
    "figure_id": "F028",
    "report_id": "R005",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: ...likely due to the launch of Huawei Enjoy 90 series, which led to a spike in Huawei's low-tier shipment."
  },
  {
    "figure_id": "F029",
    "report_id": "R005",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: The contribution from low-end segment in the overall sales mix inched up slightly in April..."
  },
  {
    "figure_id": "F030",
    "report_id": "R005",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: Apple has no exposure to low-end market, and thus best positioned among all brands."
  },
  {
    "figure_id": "F031",
    "report_id": "R005",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: Other OEMs collectively shipped 22% less smartphones in April 2026 vs. April 2025 ... Non-Apple/Huawei Shipment in China & YoY Growth"
  },
  {
    "figure_id": "F032",
    "report_id": "R005",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: ...and they collectively lost 9.8pts unit share YoY, mostly burdened by the drop of low-end segment shipment. Non-Apple/Huawei Market Share in China"
  },
  {
    "figure_id": "F033",
    "report_id": "R005",
    "label": "EXHIBIT 8",
    "context": "Exhibit 9 - Exhibit 11). - Apple then has responded with more flexible pricing. At the iPhone 17 launch in September 2025, Apple priced the devices below RMB 6,000 & made them eligible for subsidies. The prices of the iPhone 16 seri"
  },
  {
    "figure_id": "F034",
    "report_id": "R005",
    "label": "Exhibit 9",
    "context": "EXHIBIT 9: Apple focuses on flagship segment but the size of this segment hardly expanded."
  },
  {
    "figure_id": "F035",
    "report_id": "R005",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: In comparison, sub-flagship segment has been growing gradually. China Sub-Flagship Smartphones (RMB4,000 - 5,999) Shipment by OEM"
  },
  {
    "figure_id": "F036",
    "report_id": "R005",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: Apple was challenged by Huawei in the flagship segment & by other Chinese OEMs in the sub-flagship segment. Smartphone Shipment in China by Brand"
  },
  {
    "figure_id": "F037",
    "report_id": "R005",
    "label": "EXHIBIT 13",
    "context": "EXHIBIT 13: ...but that was primarily driven by the strong shipment in RMB2,000 and below segment, thanks to recent launch of Enjoy 90 series. Huawei Shipment by RMB Price Band (M units)"
  },
  {
    "figure_id": "F038",
    "report_id": "R005",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: Huawei's unit share jumped to c. $25\\%$ in April and the lead over Apple's share widened to almost 10pts... Apple & Huawei Market Share in China"
  },
  {
    "figure_id": "F039",
    "report_id": "R005",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: Though the wait time for the Pro Max model has become shorter, Huawei's premium segment volume however didn't improve."
  },
  {
    "figure_id": "F040",
    "report_id": "R005",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: Huawei's shipment increased by $28\\%$ YoY in April... EXHIBIT 16: ... while Apple's shipment grew 9% YoY. Apple Shipment in China & YoY Growth"
  },
  {
    "figure_id": "F041",
    "report_id": "R005",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: Huawei's shipment increased by $28\\%$ YoY in April... EXHIBIT 16: ... while Apple's shipment grew 9% YoY. Apple Shipment in China & YoY Growth"
  },
  {
    "figure_id": "F042",
    "report_id": "R005",
    "label": "Exhibit 17",
    "context": "EXHIBIT 17: Adjusting the sell-in data from CATR for possible obsolescence, we find sell-in was notably higher than sell-through in April..."
  },
  {
    "figure_id": "F043",
    "report_id": "R005",
    "label": "EXHIBIT 18",
    "context": "EXHIBIT 18: ...especially for non-Apple brands likely due to their recent price adjustments."
  },
  {
    "figure_id": "F044",
    "report_id": "R005",
    "label": "EXHIBIT 19",
    "context": "EXHIBIT 19: iPhone also saw some inventory restocking, but at a relatively healthy level."
  },
  {
    "figure_id": "F045",
    "report_id": "R005",
    "label": "Exhibit 20",
    "context": "EXHIBIT 20: 5G penetration has reached almost 100% in new smartphone sales in China. Smartphone Shipment & 5G Penetration"
  },
  {
    "figure_id": "F046",
    "report_id": "R005",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 21: Smartphone ASP increased by 16% YoY even without including subsidies. Smartphone Blended ASP in China (RMB)"
  },
  {
    "figure_id": "F047",
    "report_id": "R005",
    "label": "EXHIBIT 22",
    "context": "EXHIBIT 22: Non-Apple/Huawei sub-flagship shipment was down 20% YoY in April. Shipment of Non-Apple/Huawei Sub-Flagship Smartphones (RMB4,000-5,999) in China"
  },
  {
    "figure_id": "F048",
    "report_id": "R005",
    "label": "EXHIBIT 23",
    "context": "EXHIBIT 23: Sub-flagship segment took up 16% of non-Apple/Huawei shipment, flat YoY."
  },
  {
    "figure_id": "F049",
    "report_id": "R005",
    "label": "EXHIBIT 24",
    "context": "EXHIBIT 24: Non-Apple/Huawei flagship shipment was up 14% YoY. Shipment of Non-Apple/Huawei Flagship Smartphones (≥RMB6,000) in China"
  },
  {
    "figure_id": "F050",
    "report_id": "R005",
    "label": "EXHIBIT 25",
    "context": "EXHIBIT 25: Flagship segment accounted for 7% of total non-Apple/Huawei shipment, vs. c. 5% one year ago."
  },
  {
    "figure_id": "F051",
    "report_id": "R005",
    "label": "EXHIBIT 26",
    "context": "EXHIBIT 26: The share of Xiaomi's shipments priced above RMB 4k increased MoM to 21%, though modestly below the 22% in Apr 2025; Shipments in the RMB 2k-4k range reached 28%, vs. 37% in Mar 2026 and 25% in Apr 2025. Xiaomi Smartph"
  },
  {
    "figure_id": "F052",
    "report_id": "R005",
    "label": "EXHIBIT 27",
    "context": "EXHIBIT 27: In Apr 2026, Xiaomi's market share declined to $14.6\\%$ from $15.6\\%$ in Mar 2026 and $17.0\\%$ in Apr 2025."
  },
  {
    "figure_id": "F053",
    "report_id": "R005",
    "label": "EXHIBIT 28",
    "context": "EXHIBIT 28: Xiaomi's yoy growth fell -23% YoY. Xiaomi: China smartphone shipment & growth"
  },
  {
    "figure_id": "F054",
    "report_id": "R005",
    "label": "Exhibit 29",
    "context": "EXHIBIT 29: In April, unit share of Qualcomm and MediaTek decreased by 2.8pts and 2.9pts QoQ, respectively... MediaTek & Qualcomm Unit Share in China"
  },
  {
    "figure_id": "F055",
    "report_id": "R005",
    "label": "EXHIBIT 30",
    "context": "EXHIBIT 30: ...primarily due to weaker share among non-Apple/Huawei OEMs. China Smartphone Shipment by Brand"
  },
  {
    "figure_id": "F056",
    "report_id": "R005",
    "label": "EXHIBIT 31",
    "context": "EXHIBIT 31: MediaTek's shipment mix continued to improve after plateauing for a while. MediaTek SoC Shipment Breakdown by Price Band (in RMB)"
  },
  {
    "figure_id": "F057",
    "report_id": "R005",
    "label": "EXHIBIT 32",
    "context": "EXHIBIT 32: UNISOC's share remained very small in China, indicating UNISOC is not competitive in 5G."
  },
  {
    "figure_id": "F058",
    "report_id": "R005",
    "label": "Exhibit 33",
    "context": "EXHIBIT 33: The OLED penetration stood at c. 90% in April. China Smartphone Shipment Breakdown by Display Technology"
  },
  {
    "figure_id": "F059",
    "report_id": "R005",
    "label": "EXHIBIT 34",
    "context": "EXHIBIT 34: OLED penetration in non-Apple/Huawei smartphones remained at 88%. OLED Penetration in Non-Apple/Huawei Smartphones Shipment in China"
  },
  {
    "figure_id": "F060",
    "report_id": "R005",
    "label": "EXHIBIT 35",
    "context": "EXHIBIT 35: All OEMs shipped less OLED YoY in April except for Huawei and Apple. EXHIBIT 36: The adoption rate of foldable panel dropped to below 5% in April."
  },
  {
    "figure_id": "F061",
    "report_id": "R005",
    "label": "EXHIBIT 35",
    "context": "EXHIBIT 35: All OEMs shipped less OLED YoY in April except for Huawei and Apple. EXHIBIT 36: The adoption rate of foldable panel dropped to below 5% in April."
  },
  {
    "figure_id": "F062",
    "report_id": "R008",
    "label": "Figure 1",
    "context": "Cindy Li $^{AC}$ Figure 1. HK Retail Sales Value: +8.6% in Apr'26 YoY Change in Retail Sales Value"
  },
  {
    "figure_id": "F063",
    "report_id": "R008",
    "label": "Figure 2",
    "context": "Figure 2. HK Retail Sales Value YoY Change by Category Retail Sales YoY Change by Category (%)"
  },
  {
    "figure_id": "F064",
    "report_id": "R008",
    "label": "Figure 3",
    "context": "Figure 3. HKD Depreciated 4% vs. Rmb in 5M26 HKD/RMB Exchange Rate"
  },
  {
    "figure_id": "F065",
    "report_id": "R008",
    "label": "Figure 4",
    "context": "Figure 4. HK Retail Sales Correlates with HKD/Rmb Forex CNY/HKD YoY and Retail Sales Value YoY Since 2006"
  },
  {
    "figure_id": "F066",
    "report_id": "R008",
    "label": "Figure 5",
    "context": "Figure 5. HK Luxury Goods: accelerate in Apr'26 YoY Change in Retail Sales Value - Luxury Goods"
  },
  {
    "figure_id": "F067",
    "report_id": "R008",
    "label": "Figure 6",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Note: Luxury goods refer to retail sales under the category of “Jewelry, Watches, Clocks & Valuable Gifts Figure 6. HK Supermarket Retail: stabilizing YoY Change in Retail Sales Value - Supe"
  },
  {
    "figure_id": "F068",
    "report_id": "R008",
    "label": "Figure 7",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 7. HK Online Retail Sales Value: strong yoy surge YoY Change in Online Retail Sales Value"
  },
  {
    "figure_id": "F069",
    "report_id": "R008",
    "label": "Figure 8",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 8. HK Online Retail Sales Value: 10% mix % of Online Retail Sales"
  },
  {
    "figure_id": "F070",
    "report_id": "R009",
    "label": "Figure 2",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Note: Universe is TOPIX companies with February or March FY year-ends. Figure 2. Corporate guidance vs results / prior consensus (OP basis)"
  },
  {
    "figure_id": "F071",
    "report_id": "R009",
    "label": "Figure 3",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Note: Universe is TOPIX companies with February or March FY year-ends. Figure 3. MSCI Japan IT 12mf EPS and world semiconductor sales"
  },
  {
    "figure_id": "F072",
    "report_id": "R009",
    "label": "Figure 4",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 4. FY3/26 and FY3/27 breakdown of net income growth by sector (¥trn)"
  },
  {
    "figure_id": "F073",
    "report_id": "R009",
    "label": "Figure 8",
    "context": "Note: Universe is TOPIX companies with February or March FY year-ends. # Near-term risk of revision deterioration exists but is not enough to change the Japanese equity trend Downside to profit plans may lead to deterioration in earnings forecast revisions in "
  },
  {
    "figure_id": "F074",
    "report_id": "R009",
    "label": "Figure 7",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Note: Universe is TOPIX companies with February or March FY year-ends. Figure 7. TOPIX revision index and TOPIX returns vs 2y average"
  },
  {
    "figure_id": "F075",
    "report_id": "R009",
    "label": "Figure 8",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 8. MSCI Japan and MSCI Japan IT earnings revision indexes"
  },
  {
    "figure_id": "F076",
    "report_id": "R009",
    "label": "Figure 9",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 9. TOPIX earnings revision index and the positive earnings surprise ratio (OP basis)"
  },
  {
    "figure_id": "F077",
    "report_id": "R009",
    "label": "Figure 10",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. # Japanese firms strengthening their ability to smoothly implement price pass-throughs The company plans presented at full-year results saw a relatively high frequency of sales plan beats an"
  },
  {
    "figure_id": "F078",
    "report_id": "R009",
    "label": "Figure 11",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Note: Universe is TOPIX companies with February or March year-ends. Beat is defined as when revenue guidance vs prior consensus is over 0%, while a miss is seen if OP guidance vs prior conse"
  },
  {
    "figure_id": "F079",
    "report_id": "R009",
    "label": "Figure 12",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 12. Large enterprises: OPM and output prices"
  },
  {
    "figure_id": "F080",
    "report_id": "R009",
    "label": "Figure 13",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 13. TOPIX margin revision index and import prices"
  },
  {
    "figure_id": "F081",
    "report_id": "R009",
    "label": "Figure 15",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. # Japanese stocks still have upside valuation potential Figure 15. TOPIX 12m and 24m forward PERs"
  },
  {
    "figure_id": "F082",
    "report_id": "R009",
    "label": "Figure 16",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 16. TOPIX PBR and RoE distribution"
  },
  {
    "figure_id": "F083",
    "report_id": "R009",
    "label": "Figure 17",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 17. Trend in global money supply"
  },
  {
    "figure_id": "F084",
    "report_id": "R009",
    "label": "Figure 18",
    "context": "The chart displays a stacked area chart with the x-axis labeled 'Year' and y-axis labeled 'Money Supply (tn USD)'. The legend indicates six categories: US, Japan, Eurozone, UK, China, and M2 money supply. The data is extracted from the image and presented in C"
  },
  {
    "figure_id": "F085",
    "report_id": "R009",
    "label": "Figure 19",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Note: FY3/26 numbers are based on actual results + consensus estimates; numbers for FY3/27 on are consensus estimates. Figure 19. Yield spread in major markets"
  },
  {
    "figure_id": "F086",
    "report_id": "R009",
    "label": "Figure 20",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 20. Global money supply and 12mf PER"
  },
  {
    "figure_id": "F087",
    "report_id": "R009",
    "label": "Figure 21",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. # We expect the N/T ratio to remain high The N/T ratio (Nikkei 225 to TOPIX ratio) is marking record highs due to substantial gains by Al/semiconductor-related sectors and stocks (Figures 21"
  },
  {
    "figure_id": "F088",
    "report_id": "R009",
    "label": "Figure 22",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 22. N/T ratio and electric appliance TOPIX relative share price"
  },
  {
    "figure_id": "F089",
    "report_id": "R009",
    "label": "Figure 23",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 23. Trend in PEG ratio for major markets and indexes"
  },
  {
    "figure_id": "F090",
    "report_id": "R009",
    "label": "Figure 25",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. # \"Bad rate rises\" are less likely to materialize in Japan Figure 25. US 10y yield and S&P500 12mf P/E"
  },
  {
    "figure_id": "F091",
    "report_id": "R009",
    "label": "Figure 26",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 26. Japan 10y yield and TOPIX 12mf P/E"
  },
  {
    "figure_id": "F092",
    "report_id": "R009",
    "label": "Figure 27",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 27. Distribution of PBRs in Japan/US/Europe major equity indexes (left: number of companies; right: market cap weight) (# of company)"
  },
  {
    "figure_id": "F093",
    "report_id": "R009",
    "label": "Figure 28",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 28. Japan 10y BEI and CPI"
  },
  {
    "figure_id": "F094",
    "report_id": "R009",
    "label": "Figure 29",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 29. US 10y BEI and CPI"
  },
  {
    "figure_id": "F095",
    "report_id": "R009",
    "label": "Figure 30",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 30. Japan 10y yield, BEI and real yield"
  },
  {
    "figure_id": "F096",
    "report_id": "R009",
    "label": "Figure 31",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 31. US 10y yield, BEI and real yield"
  },
  {
    "figure_id": "F097",
    "report_id": "R009",
    "label": "Figure 32",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 32. Japan potential growth rate and real yield"
  },
  {
    "figure_id": "F098",
    "report_id": "R009",
    "label": "Figure 33",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 33. US potential growth rate and real yield"
  },
  {
    "figure_id": "F099",
    "report_id": "R009",
    "label": "Figure 36",
    "context": "involve the 10y Japanese government bond yield rising above 3% due to an increase in real interest rates. However, the government is currently taking a cautious fiscal approach, for example, by limiting the supplementary budget to the amount available in conti"
  },
  {
    "figure_id": "F100",
    "report_id": "R009",
    "label": "Figure 35",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 35. Japan composite leading index (CLI) and BEI"
  },
  {
    "figure_id": "F101",
    "report_id": "R009",
    "label": "Figure 37",
    "context": "Note: Universe is TOPIX constituents with 1) market caps over ¥100bn, 2) that are in the top 20% based on 3y momentum, 3) have current vs February-end returns below -5%. # Focus on companies with sales plan beats and profit plan misses versus consensus While m"
  },
  {
    "figure_id": "F102",
    "report_id": "R009",
    "label": "Figure 38",
    "context": "Figure 38. Time-lag correlations of Brent crude, import, corporate and consumer prices © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 39. Correlation and lag (by quarter) of industry level output price DI vs all industry output pr"
  },
  {
    "figure_id": "F103",
    "report_id": "R014",
    "label": "Figure 1",
    "context": "Figure 1: Equities, rates, and FX movement Note: Flow is in tril JPY Figure 2: Global equity performance (since 2025)"
  },
  {
    "figure_id": "F104",
    "report_id": "R014",
    "label": "Figure 3",
    "context": "Figure 3: Japan, US rates, and USDJPY movement"
  },
  {
    "figure_id": "F105",
    "report_id": "R014",
    "label": "Figure 4",
    "context": "Figure 4: Nikkei vs. TOPIX share price ratio (NT ratio)"
  },
  {
    "figure_id": "F106",
    "report_id": "R014",
    "label": "Figure 5",
    "context": "Figure 5: Trend of share price volatility index"
  },
  {
    "figure_id": "F107",
    "report_id": "R014",
    "label": "Figure 7",
    "context": "Figure 7: Share price performance by region and sector Note: By sector is MSCI sector index basis. Figure 8: Breakdown of TOPIX sector returns"
  },
  {
    "figure_id": "F108",
    "report_id": "R014",
    "label": "Figure 9",
    "context": "Figure 9: Cyclical versus defensive sectors"
  },
  {
    "figure_id": "F109",
    "report_id": "R014",
    "label": "Figure 11",
    "context": "Figure 11: 1M return and valuation by TOPIX 17 sectors"
  },
  {
    "figure_id": "F110",
    "report_id": "R014",
    "label": "Figure 10",
    "context": "Figure 10: Overseas versus domestic demand-related sectors"
  },
  {
    "figure_id": "F111",
    "report_id": "R014",
    "label": "Figure 12",
    "context": "Figure 12: Japan versus US performance for major sectors"
  },
  {
    "figure_id": "F112",
    "report_id": "R014",
    "label": "Figure 13",
    "context": "Figure 13: Major factor performance in Japan and the US Figure 15: MSCI value/growth index EPS and performance gap"
  },
  {
    "figure_id": "F113",
    "report_id": "R014",
    "label": "Figure 14",
    "context": "Figure 14: MSCI Japan style index"
  },
  {
    "figure_id": "F114",
    "report_id": "R014",
    "label": "Figure 16",
    "context": "Figure 16: Growth vs. value P/B gap"
  },
  {
    "figure_id": "F115",
    "report_id": "R014",
    "label": "Figure 19",
    "context": "Figure 19: EPS consensus estimates and JPM price targets vs. consensus Figure 20: TOPIX EPS revisions vs. PMI"
  },
  {
    "figure_id": "F116",
    "report_id": "R014",
    "label": "Figure 22",
    "context": "Figure 22: TOPIX FY2025 and FY2026 estimated EPS"
  },
  {
    "figure_id": "F117",
    "report_id": "R014",
    "label": "Figure 24",
    "context": "Figure 24: Overseas and domestic demand-related names' actual net profit and USDJPY rate"
  },
  {
    "figure_id": "F118",
    "report_id": "R014",
    "label": "Figure 21",
    "context": "Figure 21: EPS revision index"
  },
  {
    "figure_id": "F119",
    "report_id": "R014",
    "label": "Figure 23",
    "context": "Figure 23: TOPIX 12M forward EPS and USD/JPY sensitivity"
  },
  {
    "figure_id": "F120",
    "report_id": "R014",
    "label": "Figure 25",
    "context": "Figure 25: Amount of share buyback announcements for TOPIX stocks"
  },
  {
    "figure_id": "F121",
    "report_id": "R014",
    "label": "Figure 28",
    "context": "Figure 28: TOPIX 33 sector EPS and valuation Note: Estimates are IBES consensus estimates. Figure 29: TOPIX 12-month forward PER"
  },
  {
    "figure_id": "F122",
    "report_id": "R014",
    "label": "Figure 30",
    "context": "Figure 30: TOPIX 12-month forward PER versus S&P 500, MSCI World"
  },
  {
    "figure_id": "F123",
    "report_id": "R014",
    "label": "Figure 31",
    "context": "Figure 31: TOPIX 12-month forward PER and revision index"
  },
  {
    "figure_id": "F124",
    "report_id": "R014",
    "label": "Figure 33",
    "context": "Figure 33: TOPIX 12-month forward P/B"
  },
  {
    "figure_id": "F125",
    "report_id": "R014",
    "label": "Figure 35",
    "context": "Figure 35: Ratio of companies with P/B above 1x in Japan, US, Europe"
  },
  {
    "figure_id": "F126",
    "report_id": "R014",
    "label": "Figure 32",
    "context": "Figure 32: Correlation between TOPIX PER and JGB 10Y nominal yield"
  },
  {
    "figure_id": "F127",
    "report_id": "R014",
    "label": "Figure 34",
    "context": "Figure 34: Distribution of TOPIX P/B and ROE (Since 2005)"
  },
  {
    "figure_id": "F128",
    "report_id": "R014",
    "label": "Figure 36",
    "context": "Figure 36: Japan/US stock yield gaps and TOPIX vs. S&P performance"
  },
  {
    "figure_id": "F129",
    "report_id": "R014",
    "label": "Figure 37",
    "context": "Figure 37: Stock trading flow by entity (weekly) Figure 39: Cumulative stock trading flow from foreigners YTD"
  },
  {
    "figure_id": "F130",
    "report_id": "R014",
    "label": "Figure 37",
    "context": "Figure 37: Stock trading flow by entity (weekly) Figure 39: Cumulative stock trading flow from foreigners YTD"
  },
  {
    "figure_id": "F131",
    "report_id": "R014",
    "label": "Figure 41",
    "context": "Figure 41: Major stock ETF cumulative flow by region"
  },
  {
    "figure_id": "F132",
    "report_id": "R014",
    "label": "Figure 38",
    "context": "Figure 38: Stock trading flow by entity (monthly)"
  },
  {
    "figure_id": "F133",
    "report_id": "R014",
    "label": "Figure 40",
    "context": "Figure 40: Monthly NISA flow from individuals"
  },
  {
    "figure_id": "F134",
    "report_id": "R014",
    "label": "Figure 42",
    "context": "Figure 42: Foreign investor flows to equity investment trusts"
  },
  {
    "figure_id": "F135",
    "report_id": "R014",
    "label": "Figure 43",
    "context": "Figure 43: Investor flows into global developed market equity funds"
  },
  {
    "figure_id": "F136",
    "report_id": "R014",
    "label": "Figure 45",
    "context": "Figure 45: Allocation to Japan equities by global active equity funds"
  },
  {
    "figure_id": "F137",
    "report_id": "R014",
    "label": "Figure 47",
    "context": "Figure 47: Investors' sentiment by sector (QUICK survey: overseas demand/financials)"
  },
  {
    "figure_id": "F138",
    "report_id": "R014",
    "label": "Figure 44",
    "context": "Figure 44: Investor flows into global emerging market equity funds"
  },
  {
    "figure_id": "F139",
    "report_id": "R014",
    "label": "Figure 46",
    "context": "Figure 46: Stock performance and domestic institutional investors' Japanese stock weight"
  },
  {
    "figure_id": "F140",
    "report_id": "R014",
    "label": "Figure 48",
    "context": "Figure 48: Investors' sentiment by sector (QUICK survey: domestic demand/other)"
  },
  {
    "figure_id": "F141",
    "report_id": "R015",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Secondary listing home prices trended down 0.5% m-m in May (vs. -0.4% in April)..."
  },
  {
    "figure_id": "F142",
    "report_id": "R015",
    "label": "Exhibit 2",
    "context": "Exhibit 2: ...with 93% of sample cities recording m-m decreases (vs. 91% in April)"
  },
  {
    "figure_id": "F143",
    "report_id": "R015",
    "label": "Exhibit 3",
    "context": "Exhibit 3: New secondary listings continued to decrease m-m in May"
  },
  {
    "figure_id": "F144",
    "report_id": "R015",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Visits to agents decreased m-m in May post-strong sales in March-April"
  },
  {
    "figure_id": "F145",
    "report_id": "R016",
    "label": "Figure 1",
    "context": "Figure 1: Mainland homebuyers now accounted \\~50% of primary market transaction value Chinese buyers (include new HKPR) as % of overall HK property transaction value"
  },
  {
    "figure_id": "F146",
    "report_id": "R016",
    "label": "Figure 2",
    "context": "Figure 2: ..., or 36% in terms of primary market transaction (in units) # Valuation Method and Risk Statement We believe the key risks related to the Hong Kong property sector include: 1) weakening macroeconomic conditions; 2) a"
  },
  {
    "figure_id": "F147",
    "report_id": "R017",
    "label": "Figure 3",
    "context": "Figure 3: HDD production volume"
  },
  {
    "figure_id": "F148",
    "report_id": "R017",
    "label": "Figure 4",
    "context": "Figure 4: HDD capacity output"
  },
  {
    "figure_id": "F149",
    "report_id": "R017",
    "label": "Figure 5",
    "context": "Figure 5: Nearline HDD production volume"
  },
  {
    "figure_id": "F150",
    "report_id": "R017",
    "label": "Figure 6",
    "context": "Figure 6: Nearline HDD capacity output"
  },
  {
    "figure_id": "F151",
    "report_id": "R017",
    "label": "Figure 7",
    "context": "Figure 7: SSD production volume"
  },
  {
    "figure_id": "F152",
    "report_id": "R017",
    "label": "Figure 8",
    "context": "Figure 8: SSD capacity output"
  },
  {
    "figure_id": "F153",
    "report_id": "R017",
    "label": "Figure 9",
    "context": "Figure 9: Enterprise/Datacenter-Storage production volume"
  },
  {
    "figure_id": "F154",
    "report_id": "R017",
    "label": "Figure 10",
    "context": "Figure 10: Enterprise/Datacenter-Storage capacity output"
  },
  {
    "figure_id": "F155",
    "report_id": "R017",
    "label": "Figure 11",
    "context": "Figure 11: Enterprise/Datacenter-Storage production volume"
  },
  {
    "figure_id": "F156",
    "report_id": "R017",
    "label": "Figure 12",
    "context": "Figure 12: Enterprise/Datacenter-Storage capacity output"
  },
  {
    "figure_id": "F157",
    "report_id": "R017",
    "label": "Figure 13",
    "context": "Figure 13: Enterprise/Datacenter-production volume (SSD/HDD ratio)"
  },
  {
    "figure_id": "F158",
    "report_id": "R017",
    "label": "Figure 14",
    "context": "Figure 14: Enterprise/Datacenter-production capacity (SSD/HDD ratio)"
  },
  {
    "figure_id": "F159",
    "report_id": "R019",
    "label": "Exhibit 1",
    "context": "Exhibit 1: New AI PC announced by Nvidia (N1X) Announcing NVIDIA and Microsoft Reinvent PC Powered by RTX Spark"
  },
  {
    "figure_id": "F160",
    "report_id": "R019",
    "label": "Exhibit 2",
    "context": "Exhibit 2: MediaTek provides 20-core customized Grace CPU for N1X 20-Core Grace CPU Custom Built With MediaTek"
  },
  {
    "figure_id": "F161",
    "report_id": "R019",
    "label": "Exhibit 3",
    "context": "Exhibit 3: RTX Spark (N1X) provided by MSI (available in 3Q26) MSI MSI Prestige N16 Flip AI NVIDIA RTX Spark"
  },
  {
    "figure_id": "F162",
    "report_id": "R019",
    "label": "Exhibit 4",
    "context": "Exhibit 4: RTX Spark (N1X) provided by ASUS (available in 3Q26) ProArt ASUS RIGHT P14 December 19th December 20th"
  },
  {
    "figure_id": "F163",
    "report_id": "R019",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Vera performance could be 1.8x that of highest-performance x86 CPU"
  },
  {
    "figure_id": "F164",
    "report_id": "R019",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Vera CPU cores are not split across chiplets, enabling faster core-to-core connection 88 NVIDIA Custom Olympus Core With Spatial Multithreading PCIe Gen 6 CXL 3.1 164 MB L3 Cache"
  },
  {
    "figure_id": "F165",
    "report_id": "R020",
    "label": "Figure 1",
    "context": "The bottom line: (1) unwavering Central govt support to HK; (2) global demand meets local supply — We believe national support for HK will remain intact amid global geopolitical uncertainties, underpinning HK's status as a premier international financial cente"
  },
  {
    "figure_id": "F166",
    "report_id": "R020",
    "label": "Figure 2",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 2. Residential Purchases by Non-HKID Holders Individual Buyers Not Holding HK Identity Card"
  },
  {
    "figure_id": "F167",
    "report_id": "R020",
    "label": "Figure 4",
    "context": "Figure 4. HK Property Sector — Valuations (1-Jun-2026 close) Citi Rating: 1 – Buy; 2 – Neutral; 3 – Sell; H – High Risk © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 5. HK Property Sector — Quant Screen on Investor Position (1-we"
  },
  {
    "figure_id": "F168",
    "report_id": "R020",
    "label": "Figure 6",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Note: week on week change, latest week in green dots, previous week in red dots Figure 6. HK Property Sector — Quant Screen on Investor Position (1-month change by 22-May-2026)"
  },
  {
    "figure_id": "F169",
    "report_id": "R021",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Driven by recent tax changes we expect national house prices to come under pressures largest national house price declines (peak-to-trough %)"
  },
  {
    "figure_id": "F170",
    "report_id": "R021",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Adjustment will take time - housing sales and building approvals typically lead changes in price growth, while credit growth is a laggard"
  },
  {
    "figure_id": "F171",
    "report_id": "R021",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Falling house prices will have significant wealth effects on households – an important channel to slow demand Household assets (% of Income)"
  },
  {
    "figure_id": "F172",
    "report_id": "R021",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Our expectation of a decline in housing prices suggests that a sharp near-term slowing in turnover is likely, even before direct policy impacts"
  },
  {
    "figure_id": "F173",
    "report_id": "R021",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Even before these tax changes, forward housing indicators were pointing to price declines in response to rate hikes"
  },
  {
    "figure_id": "F174",
    "report_id": "R021",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Lower asset prices will put upward pressure on savings rates and thus spending"
  },
  {
    "figure_id": "F175",
    "report_id": "R021",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Bunning SSSg (FY17-27e)"
  },
  {
    "figure_id": "F176",
    "report_id": "R021",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Hardware Category Spending vs. National House Value Growth (Fiscal Half YoY %) # WES: EW rated; PT A\\$78.70/shr Earnings changes: Given our expectation for house prices and housing-related activity (i.e. turnover, appr"
  },
  {
    "figure_id": "F177",
    "report_id": "R021",
    "label": "Exhibit 11",
    "context": "Exhibit 11: WES 10 year DCF valuation Exhibit 12: WES 12M Fwd Cons P/E of 29x, is +1Std above mid-cycle"
  },
  {
    "figure_id": "F178",
    "report_id": "R021",
    "label": "Exhibit 13",
    "context": "Exhibit 13: WES 12M Fwd Cons ASX200 Index Financial relative P/E is 143%, greater than +1 Std above mid-cycle"
  },
  {
    "figure_id": "F179",
    "report_id": "R021",
    "label": "Exhibit 15",
    "context": "Exhibit 15: MTS 10 year DCF valuation Exhibit 16: MTS 12M Fwd Cons P/E of 11.8x, is -1Std above mid-cycle"
  },
  {
    "figure_id": "F180",
    "report_id": "R021",
    "label": "Exhibit 17",
    "context": "Exhibit 17: MTS 12M Fwd Cons ASX200 Ind ex Financial relative P/E is 58%, in-line with mid-cycle"
  },
  {
    "figure_id": "F181",
    "report_id": "R021",
    "label": "Exhibit 18",
    "context": "Exhibit 18: JBH Australia; TGG and HVN SSS growth"
  },
  {
    "figure_id": "F182",
    "report_id": "R021",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Discretionary Category Spending vs. National House Value Growth (Fiscal Half YoY %)"
  },
  {
    "figure_id": "F183",
    "report_id": "R021",
    "label": "Exhibit 21",
    "context": "Exhibit 21: JBH 10 year DCF valuation Exhibit 22: JBH 12M Fwd Cons P/E of 16.1x, is +1Std above mid-cycle"
  },
  {
    "figure_id": "F184",
    "report_id": "R021",
    "label": "Exhibit 23",
    "context": "Exhibit 23: JBH 12M Fwd Cons ASX200 Ind ex Financial relative P/E is 79%, +1Std above mid-cycle"
  },
  {
    "figure_id": "F185",
    "report_id": "R021",
    "label": "Exhibit 25",
    "context": "Exhibit 25: HVN 10 year DCF valuation Exhibit 26: HVN 12M Fwd Cons P/E of 12.1x, is -1Std above mid-cycle"
  },
  {
    "figure_id": "F186",
    "report_id": "R021",
    "label": "Exhibit 27",
    "context": "Exhibit 27: HVN 12M Fwd Cons ASX200 Ind ex Financial relative P/E is 60%, between +1Std and mid-cycle"
  },
  {
    "figure_id": "F187",
    "report_id": "R022",
    "label": "Figure 6",
    "context": "Figure 6: Cost of SiC substrates, the main production input, has fallen significantly since 2020"
  },
  {
    "figure_id": "F188",
    "report_id": "R022",
    "label": "Figure 8",
    "context": "Figure 8: Benefits of 800V transition in xEVs Battery Power=Voltage x Current At given power, at higher voltage the current is significantly reduced 800V"
  },
  {
    "figure_id": "F189",
    "report_id": "R022",
    "label": "Figure 9",
    "context": "Figure 9: SiC penetration in low-price EV models"
  },
  {
    "figure_id": "F190",
    "report_id": "R022",
    "label": "Figure 15",
    "context": "Figure 15: Silan Micro – NTM PB band"
  },
  {
    "figure_id": "F191",
    "report_id": "R022",
    "label": "Figure 16",
    "context": "Figure 16: CR Micro – NTM PB band"
  },
  {
    "figure_id": "F192",
    "report_id": "R022",
    "label": "Figure 17",
    "context": "Figure 17: NCE Power – NTM PE band"
  },
  {
    "figure_id": "F193",
    "report_id": "R022",
    "label": "Figure 18",
    "context": "Figure 18: StarPower – NTM PE band"
  },
  {
    "figure_id": "F194",
    "report_id": "R023",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: PB Fin: AI implementation aims to drive tele-advisor productivity from \\~40% to \\~90% AI IN SALES A UNIFIED AI-POWERED SALES STACK ACROSS THE LIFECYCLE Smarter conversations, higher conversions 01"
  },
  {
    "figure_id": "F195",
    "report_id": "R023",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Salary costs for PB Fin's call-center operations can be much lower from AI productivity boost (higher customer talk-time per advisor) Salary cost/ minute of customer talk-time (est.)"
  },
  {
    "figure_id": "F196",
    "report_id": "R024",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: Sell-thru Units (mn) in the first 8 months of launch - iPhone 17 vs. Past Cycles"
  },
  {
    "figure_id": "F197",
    "report_id": "R024",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: Global iPhone revenue, units, ASP Revenue ($mn)"
  },
  {
    "figure_id": "F198",
    "report_id": "R024",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Global ASP % Change YoY"
  },
  {
    "figure_id": "F199",
    "report_id": "R024",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: ASP % Change YoY By Region"
  },
  {
    "figure_id": "F200",
    "report_id": "R024",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: Sell-thru units % chg by region"
  },
  {
    "figure_id": "F201",
    "report_id": "R024",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: iPhone 17e vs iPhone 16e Sell-Through in M iPhone 17e vs iPhone 16e Sell-Through in M"
  },
  {
    "figure_id": "F202",
    "report_id": "R024",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: iPhone 17e vs iPhone 16e Daily units in K iPhone 17e vs iPhone 16e Daily units in K"
  },
  {
    "figure_id": "F203",
    "report_id": "R024",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: Across March and April, the iPhone e-series had a total of 4.2m units in 2026 and 3.7m units in 2025, with 2026 outperforming Mar-Apr 2026 vs 2025 Units for iPhone e-series"
  },
  {
    "figure_id": "F204",
    "report_id": "R024",
    "label": "Exhibit 9",
    "context": "EXHIBIT 9: Channel Inventory mn Units Channel Inventory (mn Units)"
  },
  {
    "figure_id": "F205",
    "report_id": "R024",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: Global Sell-in vs Sell-thru (mn Units)"
  },
  {
    "figure_id": "F206",
    "report_id": "R024",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: Global Sell-in vs. Sell-thru (mn Units)"
  },
  {
    "figure_id": "F207",
    "report_id": "R024",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: Inventory Weeks"
  },
  {
    "figure_id": "F208",
    "report_id": "R024",
    "label": "Exhibit 18",
    "context": "EXHIBIT 13: Weak sales performance of iPhone 17e dragged the shipment of N3P."
  },
  {
    "figure_id": "F209",
    "report_id": "R024",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: A similar comparison on iPhone mobile processors shows that the weakness mainly came from A19, while A19 Pro for Pro SKU remained resilient."
  },
  {
    "figure_id": "F210",
    "report_id": "R024",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 16: Most of iPhone 17 models feature 12GB DRAM vs. 8GB for iPhone 16 series, likely to better support on-device AI. iPhone DRAM Size (GB)"
  },
  {
    "figure_id": "F211",
    "report_id": "R024",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 17: iPhone models with 12GB DRAM improved slightly MoM to 42% of the overall shipment. iPhone Shipment Mix by DRAM Size EXHIBIT 18: The average DRAM content per phone still remained largely steady MoM at 9.5GB in Apr, stil"
  },
  {
    "figure_id": "F212",
    "report_id": "R024",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 17: iPhone models with 12GB DRAM improved slightly MoM to 42% of the overall shipment. iPhone Shipment Mix by DRAM Size EXHIBIT 18: The average DRAM content per phone still remained largely steady MoM at 9.5GB in Apr, stil"
  },
  {
    "figure_id": "F213",
    "report_id": "R024",
    "label": "EXHIBIT 19",
    "context": "EXHIBIT 19: Americas iPhone total revenue, units and ASP Revenue ($mn)"
  },
  {
    "figure_id": "F214",
    "report_id": "R024",
    "label": "EXHIBIT 20",
    "context": "EXHIBIT 20: Europe iPhone revenue, units and ASP Revenue ($mn)"
  },
  {
    "figure_id": "F215",
    "report_id": "R024",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 21: China iPhone revenue, units and ASP Revenue ($mn)"
  },
  {
    "figure_id": "F216",
    "report_id": "R024",
    "label": "EXHIBIT 22",
    "context": "EXHIBIT 22: Rest of Apac iPhone revenue, units, ASP Revenue ($mn)"
  },
  {
    "figure_id": "F217",
    "report_id": "R024",
    "label": "EXHIBIT 23",
    "context": "EXHIBIT 23: Japan iPhone revenue, units, ASP Revenue ($mn)"
  },
  {
    "figure_id": "F218",
    "report_id": "R025",
    "label": "Exhibit 1",
    "context": "Exhibit 1. Key ratings, target prices and data points Exhibit 2. Daily token consumption from AI services is growing rapidly"
  },
  {
    "figure_id": "F219",
    "report_id": "R025",
    "label": "Exhibit 3",
    "context": "Red arrows indicate growth rates: 30x (from 2023 to 2025e), 80x (from 2025e to 2030e). Exhibit 3. While frontier LLM API blended pricing continues to fall"
  },
  {
    "figure_id": "F220",
    "report_id": "R025",
    "label": "Exhibit 4",
    "context": "Exhibit 4. The cost per GPU has risen 2x in the latest NVIDIA GB300..."
  },
  {
    "figure_id": "F221",
    "report_id": "R025",
    "label": "Exhibit 5",
    "context": "2x Higher Exhibit 5. Cost per million tokens has fallen by 35x, boosting profitability at AI service providers"
  },
  {
    "figure_id": "F222",
    "report_id": "R025",
    "label": "Exhibit 6",
    "context": "35x Lower Exhibit 6. Gross profit margin estimates of AI service providers"
  },
  {
    "figure_id": "F223",
    "report_id": "R025",
    "label": "Exhibit 7",
    "context": "Exhibit 7. Forecast penetration rate of ARM based CPUs in the total CPU market Penetration rate of ARM CPUs in the overall CPU market"
  },
  {
    "figure_id": "F224",
    "report_id": "R025",
    "label": "Exhibit 8",
    "context": "Exhibit 8. SO-CAMM2 demand estimates from the Vera Rubin platform; $6 - 10\\%$ of total DRAM demand"
  },
  {
    "figure_id": "F225",
    "report_id": "R025",
    "label": "Exhibit 9",
    "context": "Exhibit 9. NAND demand estimates from the Vera Rubin platform; $4 - 7\\%$ of total NAND, opportunities from ICMS"
  },
  {
    "figure_id": "F226",
    "report_id": "R025",
    "label": "Exhibit 10",
    "context": "Exhibit 10. HSBC global tech team recently revised up server shipments, expecting $20\\% / 21\\%$ y-o-y growth in 2026/27e"
  },
  {
    "figure_id": "F227",
    "report_id": "R025",
    "label": "Exhibit 11",
    "context": "The chart includes a dashed line at y-o-y (%) = 0% for reference. The bar series represents HSBCe Server shipments in million units, while the line series represents the y-o-y (%) for the same years. The data points are labeled as 'e'. The chart is titled 'Pre"
  },
  {
    "figure_id": "F228",
    "report_id": "R025",
    "label": "Exhibit 12",
    "context": "+170% Exhibit 12. AI server shipments to grow $28\\%$ y-o-y in 2026e"
  },
  {
    "figure_id": "F229",
    "report_id": "R025",
    "label": "Exhibit 13",
    "context": "Exhibit 13. HBM content to increase significantly in the Rubin Ultra Exhibit 14. Average server DRAM content per unit; strong growth of $17\\%$ in 2026-27e"
  },
  {
    "figure_id": "F230",
    "report_id": "R025",
    "label": "Exhibit 13",
    "context": "Exhibit 13. HBM content to increase significantly in the Rubin Ultra Exhibit 14. Average server DRAM content per unit; strong growth of $17\\%$ in 2026-27e"
  },
  {
    "figure_id": "F231",
    "report_id": "R025",
    "label": "Exhibit 15",
    "context": "Exhibit 15. Bill of materials cost estimates for the GB300 NVL72 server system GB300 NVL72 BOM cost: USD2.9m"
  },
  {
    "figure_id": "F232",
    "report_id": "R025",
    "label": "Exhibit 16",
    "context": "Exhibit 16. Server DRAM vs HBM blended ASP trend (calendar year base)"
  },
  {
    "figure_id": "F233",
    "report_id": "R025",
    "label": "Exhibit 17",
    "context": "Exhibit 17. HBM market growth set to reach USD163bn by 2027e"
  },
  {
    "figure_id": "F234",
    "report_id": "R025",
    "label": "Exhibit 18",
    "context": "117% CAGR (2024-27e) Exhibit 18. HBM bit demand growth: CAGR of $67\\%$ in 2024-27e"
  },
  {
    "figure_id": "F235",
    "report_id": "R025",
    "label": "Exhibit 19",
    "context": "Exhibit 19. One-year contract price trend of AI GPUs (H100) for AI service providers"
  },
  {
    "figure_id": "F236",
    "report_id": "R025",
    "label": "Exhibit 20",
    "context": "Exhibit 20. US cloud service provider (CSP) capex; robust growth to continue at key US CSPs, up $70\\%$ in 2026e"
  },
  {
    "figure_id": "F237",
    "report_id": "R025",
    "label": "Exhibit 21",
    "context": "Stronger US CSP capex seen after CY4Q earnings CY26 growth up to 70% y-o-y (from 60% before 1Q) Exhibit 21. Capex consensus of key global CSPs (US & Chinese) for 2026; continued upside revisions; expected at USD738bn (+80% y-o-y)"
  },
  {
    "figure_id": "F238",
    "report_id": "R025",
    "label": "Exhibit 22",
    "context": "Exhibit 22. Open AI's cloud infra costs continue to grow"
  },
  {
    "figure_id": "F239",
    "report_id": "R025",
    "label": "Exhibit 23",
    "context": "Exhibit 23. Capex estimates of key neo-CSPs; strong growth in 2026e (Neo-CSP capex, USDbn)"
  },
  {
    "figure_id": "F240",
    "report_id": "R025",
    "label": "Exhibit 24",
    "context": "Exhibit 24. Global ABF substrate supply vs demand gap"
  },
  {
    "figure_id": "F241",
    "report_id": "R025",
    "label": "Exhibit 25",
    "context": "Exhibit 25. Global ABF substrate demand growth trend (k sqft/year)"
  },
  {
    "figure_id": "F242",
    "report_id": "R025",
    "label": "Exhibit 26",
    "context": "Exhibit 26. Global DRAM capex trend"
  },
  {
    "figure_id": "F243",
    "report_id": "R025",
    "label": "Exhibit 27",
    "context": "The chart includes a percentage label (+67%, +23%, +10%) indicating year-over-year growth trends for the top three segments. The total stacked bars represent cumulative revenue in USD billions. Exhibit 27. Global NAND capex trend"
  },
  {
    "figure_id": "F244",
    "report_id": "R025",
    "label": "Exhibit 28",
    "context": "The chart includes a percentage label (+38%, +27%, +13%) indicating year-over-year growth trends for the top three companies. The total stacked bars represent cumulative revenue in USD billions. Exhibit 28. Samsung: Advanced DRAM capacity trend (1b and above)"
  },
  {
    "figure_id": "F245",
    "report_id": "R025",
    "label": "Exhibit 29",
    "context": "The chart includes a dotted line indicating year-over-year growth: +60k in 2024, +180k in 2025, +155k in 2026e, and +140k in 2027e. The values for 1bnm and 1cmn are labeled above each bar. The y-axis represents production volume in kilowatts per million (kwpm)"
  },
  {
    "figure_id": "F246",
    "report_id": "R025",
    "label": "Exhibit 29",
    "context": "Exhibit 29. Industry total 1cnm capacity growth estimates, reaching 42% of total DRAM by 2027e Exhibit 30. Global foundry capex of top 4 suppliers set to grow $28\\% / 20\\%$ in 2026/27e"
  },
  {
    "figure_id": "F247",
    "report_id": "R025",
    "label": "Exhibit 31",
    "context": "The chart includes a percentage label (+28%, +20%, +17%) above the bars, likely indicating year-over-year growth or market share changes. Exhibit 31. Samsung foundry capex should rise $100\\%$ y-o-y in 2026e from investments in leading edge node capacity"
  },
  {
    "figure_id": "F248",
    "report_id": "R032",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: May-26 Japan sales totaled 333 thousand units, up 2.8% YoY Japan: Monthly Sales Volume"
  },
  {
    "figure_id": "F249",
    "report_id": "R032",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 3: May-26 US sales totaled 1,480 thousand units, up 0.4% YoY US Monthly Sales Volume"
  },
  {
    "figure_id": "F250",
    "report_id": "R032",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 5: US incentive trend; Toyota kept incentives low at USD 1,843 (-1% QoQ) while the industry at USD 3,450 (+2% QoQ) Note: MMC not covered; 2Q26 representing average of Apr-26 and May-26 EXHIBIT 6: US days supply; Toyota st"
  },
  {
    "figure_id": "F251",
    "report_id": "R032",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 7: Honda: Income Statement Honda: Income Statement"
  },
  {
    "figure_id": "F252",
    "report_id": "R033",
    "label": "Exhibit 1",
    "context": "EXHIBIT 1: US power demand driven by data centers"
  },
  {
    "figure_id": "F253",
    "report_id": "R033",
    "label": "Exhibit 2",
    "context": "EXHIBIT 2: Share price returns: Most Data-center asset heavy plays have rallied sharply over the last couple of years"
  },
  {
    "figure_id": "F254",
    "report_id": "R033",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: \\~\\$98Bn worth of co-location deals (against 4GW IT load) have been signed for the AI co-location model (avg duration of 10-15 years) Bitcoin miners are now integral part of the AI value chain ```mermaid graph LR"
  },
  {
    "figure_id": "F255",
    "report_id": "R033",
    "label": "Exhibit 7",
    "context": "EXHIBIT 7: Grid connection is the key for data center site selection Key factors for data center site selection #the most important factor"
  },
  {
    "figure_id": "F256",
    "report_id": "R033",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: ERCOT large load interconnection queue: most of the incremental requests have come from data centers ERCOT large load interconnection queue change (GW)"
  },
  {
    "figure_id": "F257",
    "report_id": "R033",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: Interconnection waiting time for different ISOs Average time for interconnection in US (years)- 2024"
  },
  {
    "figure_id": "F258",
    "report_id": "R033",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 11: What it takes to convert BTC mining data centers to AI data centers"
  },
  {
    "figure_id": "F259",
    "report_id": "R033",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 11: What it takes to convert BTC mining data centers to AI data centers ```mermaid graph LR"
  },
  {
    "figure_id": "F260",
    "report_id": "R033",
    "label": "Exhibit 16",
    "context": "EXHIBIT 16: Share price trend for US power generation companies None of them is covered by us Two factors are driving this gap - dispatchable generation capacity and location of the plants. The biggest beneficiaries have been comp"
  },
  {
    "figure_id": "F261",
    "report_id": "R033",
    "label": "Exhibit 19",
    "context": "EXHIBIT 19: Vistra Corp: increased revenues (in 2025 vs 2024) from wholesale generation and capacity market EXHIBIT 20: PJM market capacity revenues"
  },
  {
    "figure_id": "F262",
    "report_id": "R033",
    "label": "Exhibit 19",
    "context": "EXHIBIT 19: Vistra Corp: increased revenues (in 2025 vs 2024) from wholesale generation and capacity market EXHIBIT 20: PJM market capacity revenues"
  },
  {
    "figure_id": "F263",
    "report_id": "R033",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 21: ERCOT ATC average power prices"
  },
  {
    "figure_id": "F264",
    "report_id": "R034",
    "label": "Figure 1",
    "context": "Figure 1"
  },
  {
    "figure_id": "F265",
    "report_id": "R035",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Power demand across Europe is growing faster YTD than in 2025 Power demand growth by geography, 2025-26 (percentage)"
  },
  {
    "figure_id": "F266",
    "report_id": "R036",
    "label": "Figure 2",
    "context": "Figure 2: Developers' May contracted sales Figure 3: National residential land sales y-o-y decline narrowed to $36\\%$ in 5M26"
  },
  {
    "figure_id": "F267",
    "report_id": "R036",
    "label": "Figure 4",
    "context": "Figure 4: May average secondary units sold in 10 cities +18% y-o-y"
  },
  {
    "figure_id": "F268",
    "report_id": "R036",
    "label": "Figure 5",
    "context": "Figure 5: Shanghai May secondary transactions (28,023 units) hit a five-year high"
  },
  {
    "figure_id": "F269",
    "report_id": "R036",
    "label": "Figure 7",
    "context": "Figure 7: SOE developers' forward PE (x)"
  },
  {
    "figure_id": "F270",
    "report_id": "R036",
    "label": "Figure 8",
    "context": "Figure 8: SOE developers' NAV discount (%)"
  },
  {
    "figure_id": "F271",
    "report_id": "R036",
    "label": "Figure 9",
    "context": "Figure 9: 2026 YTD share price performance"
  },
  {
    "figure_id": "F272",
    "report_id": "R036",
    "label": "Figure 10",
    "context": "Figure 10: SOE developers' trailing PB (x)"
  },
  {
    "figure_id": "F273",
    "report_id": "R037",
    "label": "Figure 1",
    "context": "Figure 1: Asia Factory Automation & Robotics share price over the past month"
  },
  {
    "figure_id": "F274",
    "report_id": "R037",
    "label": "Figure 2",
    "context": "Figure 2: Asia Factory Automation & Robotics share price YTD"
  },
  {
    "figure_id": "F275",
    "report_id": "R037",
    "label": "Figure 3",
    "context": "Figure 3: China IA market – market size"
  },
  {
    "figure_id": "F276",
    "report_id": "R037",
    "label": "Figure 4",
    "context": "Figure 4: China IA market – quarterly growth Y/Y"
  },
  {
    "figure_id": "F277",
    "report_id": "R037",
    "label": "Figure 5",
    "context": "Figure 5: China industrial robot market – industry sales"
  },
  {
    "figure_id": "F278",
    "report_id": "R037",
    "label": "Figure 6",
    "context": "Figure 6: China industrial robot market – quarterly market share"
  },
  {
    "figure_id": "F279",
    "report_id": "R037",
    "label": "Figure 7",
    "context": "Figure 7: Low voltage inverter market – quarterly market share Figure 8: Small PLC market – quarterly market share"
  },
  {
    "figure_id": "F280",
    "report_id": "R037",
    "label": "Figure 7",
    "context": "Figure 7: Low voltage inverter market – quarterly market share Figure 8: Small PLC market – quarterly market share"
  },
  {
    "figure_id": "F281",
    "report_id": "R037",
    "label": "Figure 9",
    "context": "Figure 9: AC servo market – quarterly market share Figure 10: Mid-to-large PLC market – quarterly market share Figure 11: Fanuc quarterly order trend in China"
  },
  {
    "figure_id": "F282",
    "report_id": "R037",
    "label": "Figure 9",
    "context": "Figure 9: AC servo market – quarterly market share Figure 10: Mid-to-large PLC market – quarterly market share Figure 11: Fanuc quarterly order trend in China"
  },
  {
    "figure_id": "F283",
    "report_id": "R037",
    "label": "Figure 10",
    "context": "Figure 10: Mid-to-large PLC market – quarterly market share Figure 11: Fanuc quarterly order trend in China"
  },
  {
    "figure_id": "F284",
    "report_id": "R037",
    "label": "Figure 12",
    "context": "Figure 12: Yaskawa quarterly order trend in China"
  },
  {
    "figure_id": "F285",
    "report_id": "R038",
    "label": "Figure 1",
    "context": "Figure 1: Hong Kong monthly retail sales – overall"
  },
  {
    "figure_id": "F286",
    "report_id": "R038",
    "label": "Figure 2",
    "context": "Figure 2: Hong Kong monthly retail sales – overall; excluding electrical goods & motor vehicles"
  },
  {
    "figure_id": "F287",
    "report_id": "R038",
    "label": "Figure 3",
    "context": "Figure 3: Hong Kong monthly retail sales – staples"
  },
  {
    "figure_id": "F288",
    "report_id": "R038",
    "label": "Figure 4",
    "context": "Figure 4: Hong Kong monthly retail sales – discretionary"
  },
  {
    "figure_id": "F289",
    "report_id": "R038",
    "label": "Figure 5",
    "context": "Figure 5: Retail sales performance by type of retail outlet – April 2026"
  },
  {
    "figure_id": "F290",
    "report_id": "R038",
    "label": "Figure 6",
    "context": "Figure 6: Retail sales performance by type of retail outlet - 4M26"
  },
  {
    "figure_id": "F291",
    "report_id": "R038",
    "label": "Figure 7",
    "context": "Figure 7: Pinduoduo (拼多多) - Monthly active users (MAU) in Hong Kong Pinduoduo MAU"
  },
  {
    "figure_id": "F292",
    "report_id": "R038",
    "label": "Figure 8",
    "context": "Figure 8: Major non-local e-commerce players – monthly active users (MAU) in Hong Kong MAU # Hong Kong Tourist Arrivals Figure 9: Hong Kong monthly tourist arrivals"
  },
  {
    "figure_id": "F293",
    "report_id": "R038",
    "label": "Figure 8",
    "context": "Figure 8: Major non-local e-commerce players – monthly active users (MAU) in Hong Kong MAU # Hong Kong Tourist Arrivals Figure 9: Hong Kong monthly tourist arrivals"
  },
  {
    "figure_id": "F294",
    "report_id": "R039",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Retail Sales Trend"
  },
  {
    "figure_id": "F295",
    "report_id": "R039",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Strengthening RMB Is Helping"
  },
  {
    "figure_id": "F296",
    "report_id": "R040",
    "label": "Figure 1",
    "context": "Figure 1: Hong Kong's retail sales rose by 9% YoY in Apr, in-line with our forecast of high single digit increase HK retail sales value (HK$m)"
  },
  {
    "figure_id": "F297",
    "report_id": "R040",
    "label": "Figure 2",
    "context": "Figure 2: The April retail sales recovery rate reached 79% (vs 2018) HK retail sales vs mainland visitation recovery rate vs 2018"
  },
  {
    "figure_id": "F298",
    "report_id": "R040",
    "label": "Figure 3",
    "context": "Figure 3: Electrical goods, luxury goods and EV sales continued to drive the retail sales growth in Apr"
  },
  {
    "figure_id": "F299",
    "report_id": "R040",
    "label": "Figure 4",
    "context": "Figure 4: Online penetration remained at 10% in Apr 2026 HK online retail sales growth vs online penetration"
  },
  {
    "figure_id": "F300",
    "report_id": "R040",
    "label": "Figure 5",
    "context": "Figure 5: Monthly HK residents' northbound departures have recently stabilized at +10% in May"
  },
  {
    "figure_id": "F301",
    "report_id": "R040",
    "label": "Figure 6",
    "context": "Figure 6: Overseas departure volumes by HK residents was slightly down 1% in May"
  },
  {
    "figure_id": "F302",
    "report_id": "R043",
    "label": "Figure 2",
    "context": "Figure 2: UBS Evidence Lab's monitor of Global Data Centers shows 181 GW of capacity that is planned or under construction Global Data Center Capacity (GW)"
  },
  {
    "figure_id": "F303",
    "report_id": "R043",
    "label": "Figure 3",
    "context": "Figure 3: Excluding China, the data shows 172 GW of capacity planned or under construction Global (ex-China) Data Center Capacity (GW)"
  },
  {
    "figure_id": "F304",
    "report_id": "R043",
    "label": "Figure 4",
    "context": "Figure 4: Global BESS forecast"
  },
  {
    "figure_id": "F305",
    "report_id": "R043",
    "label": "Figure 5",
    "context": "Figure 5: Global BESS forecast (ex-China)"
  },
  {
    "figure_id": "F306",
    "report_id": "R044",
    "label": "Figure 1",
    "context": "Figure 1: On-Trade Beer Volumes Spiked YoY During Previous World Cup Events..."
  },
  {
    "figure_id": "F307",
    "report_id": "R044",
    "label": "Figure 2",
    "context": "Figure 2: ...As Did Off-Trade Volumes YoY"
  },
  {
    "figure_id": "F308",
    "report_id": "R044",
    "label": "Figure 3",
    "context": "Figure 3: Beer Volumes Have Been Declining at \\~1% Per Year, But 2006 Likely Provided a \\~9% Uplift to Monthly Volumes"
  },
  {
    "figure_id": "F309",
    "report_id": "R044",
    "label": "Figure 4",
    "context": "Figure 4: Figure 5: On-Trade Spirit Volumes Spiked YoY During Previous World Cups Events..."
  },
  {
    "figure_id": "F310",
    "report_id": "R044",
    "label": "Figure 6",
    "context": "Figure 6: ..As Did Off-Trade Volumes YoY"
  },
  {
    "figure_id": "F311",
    "report_id": "R044",
    "label": "Figure 7",
    "context": "Figure 7: Mix of Alcohol Off-Trade During World Cup Years Mix of Alcohol Sold During World Cup (Off-Trade)"
  },
  {
    "figure_id": "F312",
    "report_id": "R044",
    "label": "Figure 8",
    "context": "Figure 8: Mix of Alcohol On-Trade During World Cup Years"
  },
  {
    "figure_id": "F313",
    "report_id": "R044",
    "label": "Figure 9",
    "context": "Figure 9: South Africa Alcohol Mix by Total Volumes"
  },
  {
    "figure_id": "F314",
    "report_id": "R044",
    "label": "Figure 10",
    "context": "Figure 10: Brazil Alcohol Mix by Total Volumes Brazil Total Alcohol Sales Mix by Volume"
  },
  {
    "figure_id": "F315",
    "report_id": "R044",
    "label": "Figure 11",
    "context": "Figure 11: Russia Alcohol Mix by Total Volumes"
  },
  {
    "figure_id": "F316",
    "report_id": "R044",
    "label": "Figure 12",
    "context": "Figure 12: Qatar Alcohol Mix by Total Volumes"
  },
  {
    "figure_id": "F317",
    "report_id": "R044",
    "label": "Figure 13",
    "context": "Figure 13: USA Favors Beer and Spirits..."
  },
  {
    "figure_id": "F318",
    "report_id": "R044",
    "label": "Figure 14",
    "context": "Figure 14: ...While Mexico Overwhelmingly Consumes Beer..."
  },
  {
    "figure_id": "F319",
    "report_id": "R044",
    "label": "Figure 15",
    "context": "Figure 15: ...and Canada Prefers Beer and Wine"
  },
  {
    "figure_id": "F320",
    "report_id": "R044",
    "label": "Figure 16",
    "context": "Figure 16: Absolute Beer EQ Units (T-4W)"
  },
  {
    "figure_id": "F321",
    "report_id": "R044",
    "label": "Figure 17",
    "context": "Figure 17: Absolute Beer Takeaway (T-4W)"
  },
  {
    "figure_id": "F322",
    "report_id": "R044",
    "label": "Figure 18",
    "context": "Figure 18: The Super Bowl Adds an Estimated +6.6% Uplift to Weekly Volumes Annually"
  },
  {
    "figure_id": "F323",
    "report_id": "R045",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: Huawei's tau scaling roadmap τ-Scaling Roadmap: Sustainable PPDC Evolution"
  },
  {
    "figure_id": "F324",
    "report_id": "R045",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Illustration of the LogicFolding principle # LogicFolding ```mermaid graph TD"
  },
  {
    "figure_id": "F325",
    "report_id": "R046",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: Sector performance has been fluctuating and declining since 2026"
  },
  {
    "figure_id": "F326",
    "report_id": "R046",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: In terms of 1-yr forward P/E. pharma valuation has nearly reached all-time low"
  },
  {
    "figure_id": "F327",
    "report_id": "R046",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: In terms of 1-yr forward P/S, China biotech companies have seen a decline since sector peak in 2025 P/S change - Peak & Low vs. Current"
  },
  {
    "figure_id": "F328",
    "report_id": "R046",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: In PD-L1+ NSCLC (1L), sac-TMT combined with pembro solicits higher ORR, deep response rate, and duration of response compared to pembro monotherapy # ORR, Deep Response, and DOR (BICR) Sac-TMT + pembro improved ORR, deep"
  },
  {
    "figure_id": "F329",
    "report_id": "R046",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 17: In 1L HR+/HER2- BC, BGB-43395 reports tolerable hematologic toxicities with G3 and above TEAE for neutropenia at 0% Leading CDKi drugs safety profile comps (1L HER2- BC)"
  },
  {
    "figure_id": "F330",
    "report_id": "R049",
    "label": "Figure 1",
    "context": "Figure 1: Levels of energy storage in a data center ```mermaid graph TD"
  },
  {
    "figure_id": "F331",
    "report_id": "R050",
    "label": "Exhibit 4",
    "context": "EXHIBIT 2: The Japan Video Gaming sector has had a difficult start to : Japan Video Gaming share price performance"
  },
  {
    "figure_id": "F332",
    "report_id": "R050",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: ...with valuation de-rating representing a headwind more or less across the board"
  },
  {
    "figure_id": "F333",
    "report_id": "R050",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: Our tracker of the top global video gaming companies showed c. 11.3% industry revenue growth in the March quarter"
  },
  {
    "figure_id": "F334",
    "report_id": "R050",
    "label": "Exhibit 7",
    "context": "EXHIBIT 7: The Japan Video Gaming stocks we cover (ex. Sony) now trade on 19.7x FY3/27E PE... FY3/27E: Japan Video Gaming PE multiples"
  },
  {
    "figure_id": "F335",
    "report_id": "R050",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: ... and 17.7x FY3/28 P/E on our estimates, which we'd expect investors to focus more on over time FY3/28E: Japan Video Gaming PE multiples"
  },
  {
    "figure_id": "F336",
    "report_id": "R050",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: Japan Video Gaming sector 1-year forward PE now stands below average levels since 2020"
  },
  {
    "figure_id": "F337",
    "report_id": "R050",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: Most Japan Video Gaming stocks now sit toward the lower half of their 10–90th percentile forward PE ranges"
  },
  {
    "figure_id": "F338",
    "report_id": "R050",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: Our coverage stocks now average 11.9x FY3/27 EV/EBIT..."
  },
  {
    "figure_id": "F339",
    "report_id": "R050",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: ... and 10.11x FY3/28 EV/EBIT, similarly cheap compared with history FY3/28E: Japan Video Gaming EV/EBIT multiples"
  },
  {
    "figure_id": "F340",
    "report_id": "R050",
    "label": "Exhibit 18",
    "context": "EXHIBIT 13: RE Requiem has continued to sell well, and drive Resident Evil catalog sales"
  },
  {
    "figure_id": "F341",
    "report_id": "R050",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: Pragmata was confirmed to have exceed sales targets baked into this year's new units guide"
  },
  {
    "figure_id": "F342",
    "report_id": "R050",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: With MH Wilds now fixed, and Capcom releasing several hits in a row, we expect the company's catalog growth to look strong in the coming quarters FY3/21- FY3/26: Capcom catalogue sales volume by IP"
  },
  {
    "figure_id": "F343",
    "report_id": "R050",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 16: We expect the MH Wilds expansion to be announced during summer showcase season EXHIBIT 17: Capcom's forward PE multiple now stands close to one standard deviation below long-term mean"
  },
  {
    "figure_id": "F344",
    "report_id": "R050",
    "label": "Exhibit 21",
    "context": "EXHIBIT 19: Konami's Q1 is setting up to look far stronger than Street expectations, with eFootball monthly revenues growing sharply even before World Cup excitement really takes off"
  },
  {
    "figure_id": "F345",
    "report_id": "R050",
    "label": "EXHIBIT 20",
    "context": "EXHIBIT 20: eFootball is now a much larger game than in 2022, but even assuming a similar absolute World Cup (e.g. much smaller in percentage terms) implies significant beats to Q1 and potentially Q2 expectations"
  },
  {
    "figure_id": "F346",
    "report_id": "R050",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 21: Sensor Tower data likely understates eFootball mobile MAUs..."
  },
  {
    "figure_id": "F347",
    "report_id": "R050",
    "label": "EXHIBIT 22",
    "context": "EXHIBIT 22: ...while PC/console billings growth was said to have matched mobile in recent months"
  },
  {
    "figure_id": "F348",
    "report_id": "R050",
    "label": "EXHIBIT 23",
    "context": "EXHIBIT 23: Konami's forward PE multiple has fallen a long way from last summer's highs, and risk-reward looks favourable in our view"
  },
  {
    "figure_id": "F349",
    "report_id": "R050",
    "label": "Exhibit 27",
    "context": "EXHIBIT 24: We expect assembler output to pick up in the next few months, as Nintendo produces ahead of sell-in EXHIBIT 25: We've assumed an incremental memory cost headwind for Nintendo in FY3/28, but..."
  },
  {
    "figure_id": "F350",
    "report_id": "R050",
    "label": "EXHIBIT 26",
    "context": "EXHIBIT 26: ...a stronger 2027 line-up, with Pokemon Wind & Waves confirmed, should help the company to better manage the impact year on year; the company's openness to remake titles was interesting to note Nintendo Switch 1P title"
  },
  {
    "figure_id": "F351",
    "report_id": "R050",
    "label": "EXHIBIT 27",
    "context": "EXHIBIT 27: Nintendo's forward PE multiples are now back near long-term averages, while earnings estimates have fallen to reflect the rise in memory prices"
  },
  {
    "figure_id": "F352",
    "report_id": "R050",
    "label": "Exhibit 35",
    "context": "EXHIBIT 29: Arc Raiders concurrent users have trended down steadily since launch peak"
  },
  {
    "figure_id": "F353",
    "report_id": "R050",
    "label": "EXHIBIT 30",
    "context": "EXHIBIT 30: China operating profit steps down as ex-China contribution becomes larger gradually"
  },
  {
    "figure_id": "F354",
    "report_id": "R050",
    "label": "EXHIBIT 31",
    "context": "EXHIBIT 31: DNF mobile DAUs have fallen sharply from launch and continue to drift lower"
  },
  {
    "figure_id": "F355",
    "report_id": "R050",
    "label": "EXHIBIT 32",
    "context": "EXHIBIT 32: DNF mobile total time spent mirrors DAU declines, settling at much lower levels"
  },
  {
    "figure_id": "F356",
    "report_id": "R050",
    "label": "EXHIBIT 33",
    "context": "EXHIBIT 33: Similarweb visits to dnf.qq.com are volatile but broadly flat after the mid-2025 spike"
  },
  {
    "figure_id": "F357",
    "report_id": "R050",
    "label": "EXHIBIT 34",
    "context": "EXHIBIT 34: Nexon's surprise accounting change in Q4 drove a large reset of the company's go-forward PE multiple"
  },
  {
    "figure_id": "F358",
    "report_id": "R050",
    "label": "Exhibit 36",
    "context": "EXHIBIT 36: Higher repeat sales and cost savings continue to support a higher floor for Square Enix profits... continued growth in FY3/27E feels likely given the company's release of various Switch 2 edition games FY3/22-FY3/26: S"
  },
  {
    "figure_id": "F359",
    "report_id": "R050",
    "label": "EXHIBIT 37",
    "context": "EXHIBIT 37: MMO revenue was guided to grow in FY3/27E, helped by the Evercold expansion for Final Fantasy XIV"
  },
  {
    "figure_id": "F360",
    "report_id": "R050",
    "label": "EXHIBIT 38",
    "context": "EXHIBIT 38: Square Enix's upcoming mobile launches will be interesting to watch"
  },
  {
    "figure_id": "F361",
    "report_id": "R050",
    "label": "EXHIBIT 39",
    "context": "EXHIBIT 39: In a sector full of cheap stocks, it's still hard for us to call Square Enix's shares especially attractive, but the sense of stability at the company was encouraging"
  },
  {
    "figure_id": "F362",
    "report_id": "R050",
    "label": "Exhibit 43",
    "context": "EXHIBIT 41: Our base case remains that growth in Bandai Namco's Toy & Hobby business tracks broader anime growth... around the $10\\%$ per annum range FY3/23-FY3/26: Group Toy & Hobby revenue by IP"
  },
  {
    "figure_id": "F363",
    "report_id": "R050",
    "label": "EXHIBIT 42",
    "context": "EXHIBIT 42: The lack of FromSoftware games in 2026 and 2027 represents a headwind for Bandai Namco... can SD Gundam, repeat sales, Ace Combat 8, and Blood of Dawnwalker get us there? FY3/24-FY3/27E: Bandai Namco Digital segment oper"
  },
  {
    "figure_id": "F364",
    "report_id": "R050",
    "label": "EXHIBIT 43",
    "context": "EXHIBIT 43: Bandai Namco's forward PE multiple now stands almost one standard deviation below the mean since 2019, but the lack of an obvious catalyst remains an issue in our view"
  }
]