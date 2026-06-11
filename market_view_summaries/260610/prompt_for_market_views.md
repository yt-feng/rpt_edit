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
    "title": "摩根斯坦利：市场真正低估的不是通胀本身，而是“通胀但不加息”的定价逻辑",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：市场真正低估的不是通胀本身，而是“通胀但不加息”的定价逻辑\n\n这份报告来自摩根斯坦利2026年6月8日的全球宏观论坛，由跨资产策略主管Serena Tang、美国经济学家Diego Anzoategui、全球宏观策略主管Matthew Hornbach以及首席美国股票策略师Michael Wilson联合撰写。它讨论的不是单一资产类别，而是试图回答一个根本问题：当劳动力市场强劲、通胀回升，但美联储保持中立时，资产价格应该如何重新定价？\n\n报告的核心判断清晰且反直觉：当前市场对通胀的担忧被过度聚焦于负面情景，而忽略了通胀在“美联储不收紧”的条件下，对企业盈利和股票估值可能产生的正面推动。这不是一份看空通胀的报告，而是一份重新定义通胀含义的报告。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 劳动力市场的真实信号不是过热，而是结构性的再平衡\n\n报告首先给出了一个看似矛盾的画面。非农就业新增172k，前值上修93k，三个月移动平均达到188k。失业率稳定在4.3%。从表面看，这是一个典型的“过热”数据。但摩根斯坦利的经济团队提醒读者关注细节。\n\n第一，就业增长的广度并不均匀。报告没有直接给出行业细分，但从其对“能源拖累”尚未显现的判断可以推断，当前的增长更多来自服务业的韧性，而非制造业或能源驱动的扩张。这意味着就业增长的可持续性可能被高估。\n\n第二，薪资增长正在冷却。报告提到“薪资增长低于去年同期”，这被报告视为关键信号。当薪资增长放缓，而就业人数增长稳定时，单位劳动力成本的压力就会减轻。这是一个典型的“软着陆”信号，而不是“再通胀”信号。\n\n第三，报告的隐含判断是，就业市场的韧性恰恰给了美联储“不行动”的空间。如果就业数据疲软，市场会预期降息，但也会引发衰退担忧。如果就业数据过热，市场会预期加息，压制\n\n[... middle omitted ...]\n\n里分享完整的研报原文、图表数据，以及针对未解问题的深度推演。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美国就业数据超预期，通胀却降温了？\n\n就业强，通胀弱，市场在纠结什么？\n\n刚读完某外资投行的宏观论坛纪要，几个关键点值得记录一下。\n\n1️⃣ 就业市场比想象中更稳\n非农就业3个月均值188k，前几个月数据还被上修了93k。失业率维持在4.3%，但要是每月新增就业保持在100k左右，失业率可能会往下走。经济学家估算目前就业的“盈亏平衡点”在50k左右。\n\n2️⃣ 通胀出现分化\n核心CPI在放缓，主要是服务价格变软了。但整体CPI因为基数效应还在4.3%的高位。有意思的是，商品通胀虽然还在涨，但关税的影响在慢慢消退。\n\n3️⃣ 通胀+美联储不动的组合，对周期股有利\n研报的逻辑是：只要美联储不因为通胀而加息，通胀本身对企业盈利反而是好事。PPI领先于标普500的营收增长约4个月。历史上，在盈利高增长+美联储“中性”的环境里，标普500的12个月回报率中位数是14%。\n\n4️⃣ 半导体板块之前太热了\n上周的调整其实不意外。费城半导体指数相对于200日均线的偏离程度，已经到了科技泡沫以来最高。这种“过度延伸”的状态，往往意味着回调压力。\n\n5️⃣ 利率和波动率是近期关键风险\n当10年期美债收益率超过4.5%时，美股和利\n\n[... middle omitted ...]\n\nng their investment decision.\n\nFor analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.\n\n## MS\n\n## Diego Anzoategui\n\n## US\n\n[... middle omitted ...]\n\nCanary Wharf\n\nLondon E14 4AD\n\nUnited Kingdom\n\n+44 (0)20 7425 8000\n\n## Japan\n\n1-9-7 Otemachi, Chiyoda-ku\n\nTokyo 100-8104\n\nJapan\n\n+81 (0) 3 6836 5000\n\n## Asia/Pacific\n\n1 Austin Road West\n\nKowloon\n\nHong Kong\n\n+852 2848 5200"
  },
  {
    "id": "R002",
    "title": "JPM：大宗商品持仓的收缩不是趋势反转，而是结构性再平衡的开始",
    "digest": "[wechat_article.md]\n# JPM：大宗商品持仓的收缩不是趋势反转，而是结构性再平衡的开始\n\n这份JPM截至6月5日的最新商品市场持仓与资金流报告，给出了一个值得产业决策者和投资者认真对待的信号：全球商品期货市场的未平仓合约总值已连续三周下降，累计减少约800亿美元，至1.8万亿美元。表面看，这是市场情绪转冷的证据——农产品和贵金属价格大幅回调，持仓同步萎缩。但深入拆解资金流和仓位结构后，结论远比“避险情绪上升”复杂。\n\n真正重要的不是持仓总量的收缩，而是收缩的内部结构。资金并未逃离商品资产类别，而是在不同板块之间剧烈再分配：贵金属和基本金属获得了净资金流入，而能源和农产品则遭遇了净流出。这种分化背后，是市场正在重新定价三个核心变量——美联储政策路径、中东供应风险的真实持续性、以及中国需求的结构性变化。\n\n这份报告的价值不在于告诉你市场在跌，而在于告诉你，下跌中谁在买入、谁在卖出、以及这些行为背后的一致性逻辑。以下是我们从这份研报中提炼出的五个核心洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 贵金属的持仓收缩是价格下跌的结果，而非资金逃离的原因，但空头信号正在累积\n\n贵金属板块未平仓合约总值单周下降72亿美元至2570亿美元，连续多周下滑。但同期净合约流入达到54亿美元，其中黄金和白银分别吸收了24亿和27亿美元。这意味着持仓价值的下降几乎完全由价格下跌驱动，而非投资者主动平仓。\n\nJPM的数据显示，截至6月2日，COMEX黄金期货的投机性净多头头寸仍高达11.2万手，较前一周增加1.47万手。这说明市场在价格下跌中反而在加仓。然而，报告同时指出，自中东冲突爆发以来，金价已下跌18%，且短期价格动量信号已触及极端负值阈值，提示趋势可能衰竭。\n\n这里存在一个关键张力：如果美联储因强劲就业数据而进一步转鹰，金价的下行风险将持续存在。\n\n[... middle omitted ...]\n\n证，并分享我们基于JPM完整数据集的补充分析框架。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球商品持仓持续降温\n\n📊 商品市场资金流向速读\n\n最近全球商品市场整体降温，持仓规模连续三周下滑，但内部结构很有意思。\n\n**1/ 整体趋势：总量收缩，结构分化**\n- 全球商品期货持仓总规模降至1.8万亿美元，周环比减少140亿\n- 净多头仓位维持在2230亿美元，表面看没变化，但内部在剧烈调仓\n- 贵金属净多头增加100亿，能源减少77亿，农产品减少60亿\n\n**2/ 贵金属：资金流入，价格承压**\n- 黄金白银持仓规模下降3%，但资金仍在净流入（黄金24亿，白银27亿）\n- 管理基金在COMEX黄金的净多头增加1.47万手\n- 金价自中东冲突以来已跌18%，若美联储因就业数据转鹰，还有下行空间\n\n**3/ 原油：地缘溢价与基本面博弈**\n- 霍尔木兹海峡若6月重新开放，布伦特原油预计维持100美元附近\n- 若持续关闭，每多一个月库存消耗将推高油价约5美元\n- 目前仅有9艘LNG船在海峡内，出口仍受限\n\n**4/ 农产品：价格大幅回调**\n- 持仓规模降至3820亿美元，谷物油籽价格急跌是主因\n- 软商品逆势获得48亿资金流入，但不足以抵消谷物油籽的流出\n- 小麦、大豆、棉花的长线动量信号已转负\n\n**\n\n[... middle omitted ...]\n\nsee the strong US employment report as reinforcing their view that a cyclical lift in global business spending is now broadening to hiring in a manner that will cushion the energy price drag o\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 09 Jun 2026 06:09 PM BST\n\nDisseminated 09 Jun 2026 06:09 PM BST"
  },
  {
    "id": "R003",
    "title": "摩根斯坦利：市场低估的不是美联储降息时点，而是中国资本管制收紧的资产重定价含义",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：市场低估的不是美联储降息时点，而是中国资本管制收紧的资产重定价含义\n\n这份来自摩根斯坦利亚洲团队的研报，表面上讨论的是美联储政策立场对中国的溢出效应，但真正值得产业决策者和资产配置者关注的，不是美联储何时降息，而是中国正在主动收紧资本外流渠道，并且这一动作正在改变人民币资产的定价逻辑。\n\n报告的时间节点值得注意——2026年6月。此时市场主流叙事仍聚焦于美联储降息路径的不确定性，但摩根斯坦利把分析重心放在了另一个维度：当美国经济从消费驱动转向资本支出驱动，当中国在资本账户管理上从“被动应对”转向“主动调控”，两个经济体之间的资金流向和资产定价关系正在发生结构性的重置。\n\n这份报告的核心价值在于，它提供了一套完整的分析框架，把美联储政策、中国经济内循环、人民币汇率和资本流动整合到一个逻辑链条中。以下是我们提炼出的五个关键洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 美国经济正在经历增长引擎的结构性切换，消费不再是唯一主角\n\n摩根斯坦利对2026-2027年美国实际GDP增长的预测，表面上是一个温和加速的数字——从2025年的1.8%逐步升至2027年的2.5%——但真正重要的不是总量，而是结构。\n\n报告明确指出，增长贡献中最大的变化来自企业固定投资。2025年企业固定投资对GDP的贡献为0.8个百分点，2026年预计升至0.9，2027年进一步升至1.0。与此同时，消费的贡献虽然也在上升，但幅度明显更小——从2025年的1.0个百分点升至2027年的1.3。\n\n这意味着什么？美国经济正在从“消费者花钱”驱动，转向“企业花钱”驱动。而企业投资的核心驱动力，报告毫不含糊地指向了AI相关支出。根据报告的估算，2025年和2026年，AI相关投资对非住宅固定投资的贡献均高达1.6个百分点，而非AI部\n\n[... middle omitted ...]\n\n市场的承接能力，以及AI投资周期对中国科技产业链的长期影响。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美联储降息节奏，全看油价和通胀脸色\n\n封面：降息？还得等\n\n封面副标题：6月研报拆解：油价、就业、人民币\n\n---\n\n最近看了一份某外资投行的研报，把美国经济到人民币的路径都串了一遍。挑几个核心判断，直接说人话。\n\n**1. 美国经济：投资>消费**\n\n研报预测2026-2027年美国GDP增速会从1.8%提升到2.5%。但结构变了——过去靠消费，明年靠投资，尤其是AI相关支出。AI相关投资对GDP的贡献，从2023年的0.1个百分点，拉到2026年的1.6个点，翻了好几倍。\n\n但消费端有压力。汽油价格涨15%，会让每个家庭一年多花375美元，正好把退税增加的325美元吃掉。通胀没走远，消费者先扛。\n\n**2. 就业：看着强，但暗流涌动**\n\n非农就业数据还不错，每月新增10万人左右。研报特意算了个“盈亏平衡线”——只要新增就业超过5万人，失业率就不会涨。目前4.3%的失业率，往下走的概率比往上大。\n\n但注意，能源和AI对就业的拖累还没完全显现。研报原文是“尚未看到”，但留了个问号。\n\n**3. 通胀：核心在降，但整体不低**\n\n核心CPI在放缓，主要靠房租和部分服务业降温。但商品通胀还在，关税影响在消退，却\n\n[... middle omitted ...]\n\nat the end of this report.\n\n## US Economy\n\n## 2026-27 Growth Outlook: Capex Over Consumption\n\nWe expect real GDP growth to step up over 2026E-27E...\n\nContributions to Real GDP (pp, annual rate\n\n[... middle omitted ...]\n\narantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n© 2026 MS"
  },
  {
    "id": "R004",
    "title": "NOM：全球市场正在为一场“滞胀式供给冲击”重新定价，但真正的分歧在于谁有资格加息",
    "digest": "[wechat_article.md]\n# NOM：全球市场正在为一场“滞胀式供给冲击”重新定价，但真正的分歧在于谁有资格加息\n\n2026年6月，NOM在新加坡举办了年度旗舰亚洲投资论坛。在为期四天的会议中，全球首席经济学家团队给出了一个高度一致的判断：当前全球经济正处于一场“供给冲击复合体”之中，其结构性影响远超市场定价所反映的程度。这份研报的核心价值不在于预测了某个具体利率路径，而在于它提供了一套区分“谁在真正面临通胀压力”与“谁只是在承受增长放缓”的分析框架。\n\n市场目前最大的误判，是认为所有经济体的通胀压力是同质的。NOM经济学家们明确指出：当前的通胀并非需求过热驱动，而是由能源、芯片和食品三重供给冲击叠加而成。这意味着，传统“通胀高则加息”的简单逻辑已经失效。真正值得关注的问题是：哪些经济体有资格、有能力、有必要加息？哪些经济体应当忍受通胀、优先保增长？\n\n以下是我们从这份研报中提炼出的五个关键洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 供给冲击的广度被严重低估，全球供应链压力指数已回到疫情外历史最高\n\nNOM全球首席经济学家Rob Subbaraman在论坛上指出，即使霍尔木兹海峡很快重新开放，全球供给侧的中断惯性仍将显著存在。纽约联储的全球供应链压力指数（GSCPI）目前已经攀升至1998年以来的最高水平——如果不算疫情期间的极端值。历史经验表明，2021年12月GSCPI见顶后，美国CPI通胀在六个月后才达到峰值。\n\n这意味着什么？当前这轮供给冲击的传导尚未完全反映在终端价格中。市场对通胀“见顶回落”的乐观预期，可能忽视了供应链压力向消费端传导的滞后性。更关键的是，NOM强调这并非单一的油价冲击，而是一个“能源-芯片-食品”三重价格冲击的组合。芯片价格飙升正在通过AI基础设施投资传导至软件和服务价格，而食品价格冲击则与地缘政治\n\n[... middle omitted ...]\n\n未解问题，以及如何在当前供给冲击框架下调整你的资产配置思路。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球经济的“K型”分化，比想象中更撕裂\n\n全球经济的K型分化\n\n刚看完某外资投行论坛的宏观笔记，信息量很大。全球经济正走向一个极度分化的格局：美国独自繁荣，欧洲和部分亚洲国家在滞胀边缘挣扎，而中国则面临AI机遇和地产拖累的双重夹击。\n\n几个核心观察👇\n\n**1. 美国：AI红利独享，但通胀风险还在**\n*   美国是发达市场的“优等生”，AI投资直接拉高GDP约1个百分点。\n*   核心通胀因AI相关的“软件商品”上涨而走高，美联储主席Warsh可能更偏鸽派。\n*   市场预期：美联储大概率按兵不动到2027年底，甚至加息和降息概率相当。\n\n**2. 欧洲：最怕“滞胀”**\n*   伊朗战争后，欧元区经济预期被大幅下修，属于“增长更弱、通胀更高”的典型。\n*   但和2022年不同，现在货币和财政政策更紧，劳动力市场更松，所以央行只会“温和收紧”，不会大幅加息。\n*   调查显示：70%的人认为欧洲央行更应担心战争对经济的下行冲击，而非通胀。\n\n**3. 日本：工资涨了，央行要动**\n*   只要中东局势不拖到下半年，日本经济Q2后有望恢复。\n*   春季工资谈判确认涨薪更可持续，预计日央行在2026年6月和\n\n[... middle omitted ...]\n\ntunes. The US economy is the clear outperformer in the DM world, while many EM economies are struggling from the commodity price surge while benefitting little from the AI boom.  \n- Even if th\n\n[... middle omitted ...]\n\nrmation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R005",
    "title": "摩根斯坦利：铜关税决策将成为2026年下半年铜价最重要的单一路径依赖",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：铜关税决策将成为2026年下半年铜价最重要的单一路径依赖\n\n市场参与者正在为一个关键的政策节点做准备。美国对精炼铜进口是否征收15%关税的最终决定，预计将在2026年下半年落地。这并非一个普通的贸易政策事件。它直接关系到过去半年多时间里，全球约2.6%的铜需求被美国囤货行为所吸收的异常状态能否持续。\n\n摩根斯坦利在最新发布的金属市场报告中，系统拆解了这一决策的三种可能情景及其对铜价的含义。报告的核心判断是：市场当前定价隐含了约43%的概率认为15%关税将在2027年1月前生效。但真正重要的不是这个概率本身，而是无论最终结果如何，铜市场的定价逻辑都将经历一次结构性重置。当前COMEX相对LME约6%的溢价，以及美国已超过一年正常进口量的库存水平，都预示着市场已经提前在为这个决策定价。接下来的问题不是铜价会不会波动，而是波动的方向、幅度和持续时间将如何重塑全球铜的贸易流和库存分布。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 提前宣布关税是最强的看涨情景，但关键在于“提前”二字\n\n摩根斯坦利分析认为，如果美国在2026年7月左右提前宣布从2027年1月起实施15%的关税，这将是最为看涨的情景。逻辑链条清晰：提前宣布意味着市场有充足的时间窗口进行套利操作，将铜加速运往美国。这会进一步收紧美国以外市场的铜供应，推高LME和COMEX两个基准价格。具体而言，LME的远期曲线前端会进入现货溢价状态，而COMEX相对于LME的溢价将向15%靠拢。\n\n这里需要特别留意报告中的一个隐含判断：宣布时间越早，看涨效应越强。如果关税宣布时间临近实施日期，或者实施日期被提前，市场就没有足够时间进行物流操作，看涨效应将大打折扣。这意味着，政策制定者的“通知期”本身就是价格变量的组成部分。投资者不能简单地将“关税=看涨”作为\n\n[... middle omitted ...]\n\n定期分享更多机构研报的深度解读，并围绕这些未解问题展开讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美国铜关税的3种剧本\n\n铜关税走向\n\n2026年下半年是关键窗口\n\n某外资投行最新研报拆解了美国精炼铜进口关税的三大可能走向，决策窗口在2026年下半年。目前市场已经提前囤货，美国铜库存超过正常年份进口量，这场博弈对全球铜价的影响比想象中大。\n\n1️⃣ 最看多情景：关税落地\n- 如果宣布2027年1月起征收15%关税\n- 市场会继续抢运铜到美国，推高COMEX和LME铜价\n- LME近月合约可能转为现货升水\n- COMEX相对LME溢价或达15%\n- 若提前几个月公告，影响更明显\n\n2️⃣ 最看空情景：关税被否决\n- 美国若放弃征税，当前约2.6%全球铜需求的囤货行为会停止\n- 两大基准铜价均承压\n- COMEX溢价消失，甚至可能低于LME\n- 但研报认为12000美元/吨附近有支撑（结构性供应缺口仍在）\n\n3️⃣ 中性情景：推迟决定\n- 维持现状，关税选项保留但未定\n- 可能被市场解读为征税概率下降，小幅利空\n\n关键数据：市场目前定价2027年1月前征税概率约43%，2027年底前73%。美国铜库存已超一年正常进口量，远超历史水平。\n\n宏观因素也在发力——美联储加息预期升温时，COMEX铜在风险偏好日跑赢，\n\n[... middle omitted ...]\n\n and tightening LME spreads. Less notice would be less bullish.  \nMost bearish = Refined copper tariffs are ruled out completely, putting the 2.5% of copper supply currently going to the US fo\n\n[... middle omitted ...]\n\narantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n© 2026 MS"
  },
  {
    "id": "R006",
    "title": "美国银行：AI基础设施需求正从“GPU短缺”转向“存储与计算架构的再定价”",
    "digest": "[wechat_article.md]\n# 美国银行：AI基础设施需求正从“GPU短缺”转向“存储与计算架构的再定价”\n\n市场正在经历一个关键的认知转变。过去两年，投资者对AI基础设施的关注几乎全部集中于GPU的供应与需求，以及围绕英伟达的资本开支叙事。但美国银行在2026年全球科技大会上释放出的信号表明，真正结构性的变化正在更底层发生：AI的推理和智能体工作负载正在重塑整个IT硬件价值链，从存储到传统服务器，从分销商到企业级软件，都在经历一轮需求与定价权的同步重构。\n\n这份报告的核心判断不是“AI需求依然强劲”这样广为人知的结论，而是一个更微妙但更具投资含义的洞察：**需求强劲已是共识，但市场低估的是供给侧的结构性受限如何改变了定价模式与竞争格局。** 美国银行因此上调了IBM、NetApp、希捷和西部数据的目标价，其逻辑并非简单的需求拉动，而是这些公司正在从“卖硬件”转向“卖架构与锁定收益”。\n\n以下是我们从这份研报中提炼出的五个关键洞察，它们共同指向一个结论：AI基础设施投资的下一阶段，赢家将是那些能够将规模转化为议价权、将技术转化为长期合同的企业。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 推理与智能体AI正在创造传统计算的新需求周期，这比市场预期的更持久\n\n大多数投资者仍将AI服务器需求视为围绕GPU的单一叙事。但美国银行在会议中发现，推理和智能体AI正在成为传统计算的新驱动力。这一判断的关键在于，智能体工作负载将部分计算从并行GPU处理转移到了顺序CPU处理。这意味着，CPU密集型服务器和企业基础设施的需求正在被重新激活。\n\nDell和HPE都报告了传统计算需求的显著增长，而IBM则展示了推理和现代化工作负载如何在其非GPU平台（如大型机）上创造新的消费增长。这不仅仅是“AI服务器之外还有传统服务器”的简单补充，而是意味着整个企业IT基\n\n[... middle omitted ...]\n\n后的潜在利润路径。这些信息对于构建更完整的投资框架至关重要。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI 需求比想象中更持久\n\n投研观察\n\nAI 基建需求正变得更宽更深\n\n最近参加了某外资投行的科技大会，和几家 IT 硬件头部公司聊了一圈，感受很直接：AI 基础设施的需求不是短期的“抢货”，而是一轮结构性的扩张。\n\n1️⃣ 推理需求正在拉动传统服务器\n过去大家都盯着 GPU 服务器，但现在出现了新变化——推理和 agentic AI 开始带动 CPU 密集型服务器需求。简单说，AI 从训练走向应用，需要更多传统计算资源来“跑逻辑”。Dell 和 HPE 都提到，传统服务器需求明显回暖，IBM 也举例说推理任务正在非 GPU 平台上跑出增量。\n\n2️⃣ 存储成了新的瓶颈\n训练、推理、agentic 工作流，都在产生海量数据。这些数据要存、要查、要喂回模型。WDC 预计 HDD 收入未来 3-5 年增速可能超过 25%，Seagate 也说订单已经排到 4-5 个季度后。Dell 的 ISG 总裁甚至说，agentic AI 让数据没有“冷”或“暗”之分了。\n\n3️⃣ 供应链紧张反而利好龙头\n内存、CPU、HDD、NAND 都在涨价，交期拉长。分销商和 EMS 厂商因为能帮客户锁定供应、管理长交期，反而受益。D\n\n[... middle omitted ...]\n\nkets with SNDK highlighting its new business models that include both volume commitments, as well as fixed pricing for an initial period, followed by variable pricing over the rest of the cont\n\n[... middle omitted ...]\n\nw in accordance with firm policies.\n\nNeither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information."
  },
  {
    "id": "R007",
    "title": "GS：中国通胀数据的真正信号不在 CPI 本身，而在 PPI 的结构性集中",
    "digest": "[wechat_article.md]\n# GS：中国通胀数据的真正信号不在 CPI 本身，而在 PPI 的结构性集中\n\n五月的中国通胀数据，表面上看是一个“温和”的故事。CPI 同比持平于 1.2%，PPI 从 2.8% 升至 3.9%。市场大多会将其解读为“需求端没有过热风险，供给端成本压力正在传导”。但GS这份最新报告揭示了一个更值得关注的判断：真正重要的不是通胀的绝对水平，而是 PPI 反弹的结构——超过 80% 的贡献来自上游行业，而核心 CPI 却在走软。\n\n这意味着什么？意味着当前的通胀格局不是需求驱动的全面复苏，而是一场由能源和化工价格主导的“成本冲击”，并且这个冲击正在挤压下游利润空间。对于投资者和产业决策者而言，忽视这个结构性差异，可能会对宏观环境做出误判。\n\n这份报告提供了一个关键的分析框架：把通胀数据拆解为“上游成本推动”和“下游需求拉动”两个维度。五月的数据清晰表明，前者在加速，后者在减速。核心 CPI 从 1.2% 回落至 1.1%，虽然幅度不大，但方向明确——旅游相关服务价格的走软，暗示消费端的恢复可能比预期更脆弱。\n\n以下是这份报告的核心洞察及其对资产定价和行业格局的含义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 上游 PPI 的反弹高度集中，这意味着成本压力并非均匀分布\n\nGS报告中最引人注目的数字是：上游行业贡献了 PPI 同比反弹的 82%。具体来看，化学品、石油天然气和煤炭价格分别贡献了 0.3、0.2 和 0.2 个百分点，推动 PPI 同比从 4 月的 2.8% 升至 5 月的 3.9%。\n\n这个集中度意味着什么？它意味着成本压力并非广泛扩散，而是集中在少数几个关键上游环节。对于下游制造业来说，这是一个典型的“成本挤压”场景——上游涨价，但下游消费品 PPI 同比仅为 -0.8%，虽然比 4 月的 -1\n\n[... middle omitted ...]\n\n讨论的价值，往往不在报告本身，而在报告没有说透的那些缝隙里。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nCPI不动，PPI在涨，什么信号？\n\n📊 5月通胀数据拆解\n\n5月CPI同比+1.2%，和上月持平，但PPI从+2.8%跳升到+3.9%\n\n简单说：上游在涨价，下游没跟\n\n1️⃣ CPI为什么没动？\n能源涨价被食品降价抵消了\n猪肉同比-16.1%（比4月还弱）\n水果-2.2%，蔬菜+1.6%\n核心CPI反而从+1.2%降到+1.1%\n——旅游出行相关服务价格变软了\n\n2️⃣ PPI为什么涨这么多？\n82%的反弹来自上游\n化工、油气、煤炭是三大推手\n但环比看，PPI从+22.4%降到+9.7%\n——涨速其实在放缓\n\n3️⃣ 值得关注的细节\n能源价格是非食品CPI里唯一贡献增量的部分\n燃料同比+21.1%\n运输服务价格同比+4.7%（比上月降了）\n\n上下游价格分化还在持续\n上游成本压力是否能传导下去\n要看后续需求端恢复情况\n\n大家觉得下半年CPI会怎么走？\n欢迎一起讨论\n\n#学习笔记\n\n[source_mineru.md]\n# China: Energy-led PPI increased further in May, while core CPI softened\n\n## Bottom line:\n\nChin\n\n[... middle omitted ...]\n\nCPI: +1.2% yoy (+1.0% mom annualized\\*) in May vs. GS: +1.4% yoy, Bloomberg consensus: +1.3% yoy; April: +1.2% yoy (+2.4% mom annualized\\*).\n\nFood: -1.7% yoy in May (-0.9% mom annualized\\*) vs\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R008",
    "title": "Bernstein：储能市场真正的超预期不在需求，而在供给端正在发生的结构性收紧",
    "digest": "[wechat_article.md]\n# Bernstein：储能市场真正的超预期不在需求，而在供给端正在发生的结构性收紧\n\n储能行业正在经历一个罕见的时刻：需求端的高增长已经被市场充分定价，但供给端的变化——产能利用率从69%跃升至94%、头部企业份额的微妙再分配、以及海外市场的结构性启动——才是这份Bernstein最新全球储能追踪报告最值得关注的信号。\n\n2026年4月，中国储能电池出货量达到93.1GWh，同比增长92%，环比增长14%。这个数字本身并不令人意外——过去一年中国储能市场一直保持着高速增长。真正值得深究的是隐藏在总量背后的三个结构性变化：产能利用率已经逼近极限、竞争格局正在从“百花齐放”转向“强者分化”、以及海外市场终于开始贡献有意义的增量。\n\nBernstein在这份报告中给出了一个清晰的判断：中国储能市场已经从“产能过剩”阶段进入“供需紧平衡”阶段，而这一点尚未被市场充分定价。对于关注电池产业链的投资者来说，这意味着定价逻辑需要从“量的增长”切换到“利润率的修复”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 产能利用率从69%到94%的变化，意味着行业定价权正在发生转移\n\n这是这份报告中最容易被忽视但最重要的数据点。2025年4月，中国储能电池工厂的产能利用率仅为69%。一年后，这个数字跃升至94%。在同一时期，月度产能从67.1GWh增长到98.0GWh，增幅为46%——产能确实在扩张，但出货量的增长速度（92%）远远超过了产能扩张的速度。\n\n94%的产能利用率意味着什么？在制造业中，当产能利用率超过85%，行业就进入了“卖方市场”。当利用率超过90%，任何意外的需求波动都会导致供应紧张和价格上行。Bernstein的报告明确指出，这“预示着近期市场条件正在收紧，因为需求增长正在赶上行业产能”。\n\n这对投资框架的含义是\n\n[... middle omitted ...]\n\n结合更多维度的数据来验证或挑战Bernstein的分析框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n储能出货量四月创历史新高\n\n**93.1GWh，同比+92%**\n\n这个数字背后是产业逻辑在变\n\n最近看了一份外资投行的储能跟踪报告，几个关键信息值得记录：\n\n**1️⃣ 中国储能加速跑**\n- 4月出货93.1GWh，同比+92%，环比+14%\n- 前4个月累计309.1GWh，同比+109%\n- 产能利用率94%，去年同期仅69%，说明供需在收紧\n\n**2️⃣ 头部格局稳定，黑马在追赶**\n- 宁德时代：19.8GWh，份额22.5%\n- 亿纬锂能：8.5GWh，份额9.6%\n- 海辰储能：8.4GWh，份额9.5%\n- 比亚迪：7.4GWh，份额7.6%\n- 增速最快的是赣锋（+220%）、鹏辉（+269%）、科陆（+140%）\n\n**3️⃣ 海外市场分化明显**\n- 德国：4月装机0.8GWh，同比+74%，大型储能贡献最大（+833%）\n- 美国：4月装机4.3GWh，同比-18%，但环比+71%，夏季有望回暖\n\n**4️⃣ 招标量预示未来需求**\n4月招标55.6GWh，同比+44%；前4个月累计224.6GWh，同比+190%，意味着订单储备充足\n\n储能的增长逻辑很清晰：成本下降+政策支持让经济\n\n[... middle omitted ...]\n\nrepresenting 92% YoY and 14% MoM growth. Our industry model can be downloaded here (Link). Domestic shipments remained the key driver, increasing 89% YoY to 89.9GWh, while overseas shipments g\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R009",
    "title": "JPM：关税政策的真正转折不在税率高低，而在法律框架的切换",
    "digest": "[wechat_article.md]\n# JPM：关税政策的真正转折不在税率高低，而在法律框架的切换\n\n市场正在低估一个关键变化：美国关税政策的核心博弈点，已经从“加多少”转向了“用什么法律工具来加”。JPM在最新发布的研报中明确指出，随着IEEPA关税被法院推翻、Section 122关税即将于7月24日到期，美国政府正在系统性地将关税权力基础从临时性的紧急授权，转向更具持久性的Section 301框架。这个切换，表面上是法律技术的调整，实质上意味着关税政策的可预期性进一步降低、诉讼风险显著上升，而企业需要面对的，将是一轮比2018年中美贸易摩擦更广泛、更碎片化的政策不确定性。\n\n这不是一个关于关税税率升降的故事。这是一个关于政策工具选择如何重塑全球供应链决策逻辑的故事。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 关税的“名义税率”和“实际税率”之间存在巨大鸿沟，而豁免清单才是真正的博弈场\n\nJPM的测算揭示了一个被广泛忽视的事实：美国对全球征收的平均关税税率，在静态权重下约为11%，但实际征收中观察到的税率仅有6.7%。这4.3个百分点的差距，几乎全部来自豁免条款。能源、药品、电子产品、USMCA合规贸易——这些领域的大规模豁免，使得实际税率远低于政策声明的水平。\n\n这意味着，企业在评估关税风险时，不能只看白宫发布的税率数字，而必须拆解每一类产品的豁免状态。当前Section 301的强制劳动调查中，美国贸易代表办公室提议对60个经济体征收10%-12.5%的关税，但豁免范围比之前的IEEPA和Section 122更为宽泛——新增了飞机、部分机械设备等品类。对于法国这样的航空出口大国，由于飞机出口占其对美贸易的相当比重，实际有效税率反而可能下降。\n\n这里的核心洞察是：关税政策的真实影响，从来不取决于最高税率，而取决于谁在豁免清单上、谁不在\n\n[... middle omitted ...]\n\n每周拆解一份关键研报，并尝试回答那些报告没有完全展开的问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美国关税大转向：Section 122到期后新玩法\n\n关税换挡，谁最受伤？\n\n某外资投行最新研报指出，美国关税体系正经历一轮重大调整。7月24日Section 122临时关税到期后，白宫将转向更广泛的Section 301机制，核心是两把“新刀”。\n\n**1/ 两线并行，范围更广**\n- 强迫劳动调查：覆盖约60个经济体，拟征10%-12.5%关税\n- 产能过剩调查：覆盖16个经济体，税率未定，但范围可能更广\n这两项调查比2017-2018年针对中国的措施范围更大、推进更快，但法律风险也更高——法院最近更看重法律条文，而不是政府解释。\n\n**2/ 谁会受影响？**\n- 巴西最受伤：新增25%基础关税，有效税率从10.5%跳升至19%\n- 中国依旧高：维持23%左右，变化不大\n- 欧盟、英国反而小幅下降：因为Section 122取消后，新关税覆盖范围更窄\n- 加拿大、墨西哥靠USMCA豁免，基本稳定在3%\n\n**3/ 实际税率比表面低**\n虽然名义税率在10%左右，但实际征收只有6.7%。原因很直接：\n- 能源、药品、电子产品享受大范围豁免\n- 飞机等商品按“非民用部分”计税，实际税率从10%降到1%\n- 进\n\n[... middle omitted ...]\n\nApril 15; no tariff rates announced yet).\n\nThese actions are broader and faster-moving than the 2017–18 China measures, but may face heightened legal risk given the courts' emphasis on statuto\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 09 Jun 2026 11:32 AM BST\n\nDisseminated 09 Jun 2026 11:32 AM BST"
  },
  {
    "id": "R010",
    "title": "Citi：黄金股回调是表象，真正的机会藏在现金流与远期定价的错位中",
    "digest": "[wechat_article.md]\n# Citi：黄金股回调是表象，真正的机会藏在现金流与远期定价的错位中\n\n当金价从2026年1月的高点回落约11%，黄金股却经历了高达25%的修正。市场直观地将此解读为“金价跌了，黄金股自然要跌”。但Citi这份最新研报揭示了一个被忽视的核心判断：**黄金股当前的价格，并非在定价金价的短期波动，而是在错误地定价了这些公司未来两年持续改善的自由现金流。** 真正值得关注的，不是金价还能不能回到高点，而是这些公司能否在当前的运营效率下，将现金流转化为估值重估的杠杆。\n\n这份发布于2026年6月8日的报告，覆盖了AngloGold Ashanti和Gold Fields两家标的，均维持“买入”评级。但报告最引人深思的，并非简单的评级，而是Citi在调降目标估值倍数（从8倍降至6-7倍）的同时，仍大幅上调了远期EBITDA预期，并给出了60%以上的预期总回报率。这种“降倍提价”的微妙组合，恰恰点出了当前市场定价中最核心的错位。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 金价回调并非系统性风险，而是对运营韧性的压力测试\n\n市场对黄金股的担忧，往往集中在金价下跌对盈利的直接侵蚀。Citi的数据显示，自1月高点以来，金价从约5000美元/盎司回落至当前约4350美元，跌幅约13%。但同期两家公司的股价跌幅却远超金价，达到20%-25%。这种非对称下跌，意味着市场正在为“金价继续下跌”这一情景支付过高的保险溢价。\n\n然而，Citi的Q1 2026运营数据给出了相反的信号。两家公司的运营表现均“稳定”，这并非一句套话。在成本端，能源价格高企带来的通胀压力尚未实质性地传导至矿山运营成本；在产量端，Obuasi矿山的爬坡和Nevada项目的推进，正在为AngloGold提供内生增长。Gold Fields的Windfall项目同样\n\n[... middle omitted ...]\n\n的完整解读与原始图表，并持续跟踪两家公司的季度运营数据变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n金价回调，但现金流撑住了\n\n黄金股的估值锚在哪？\n\n某外资投行最新研报拆解\n\n最近金价从1月高点回落，黄金股最多跌了25%。但仔细看Q1运营数据，两家标的现金流依然稳，这波回调反而让估值变得有意思了。\n\n1️⃣ 金价展望：2027年看5000美元/盎司\n• 当前现货约4350美元，研报认为远期依然看涨\n• 2027年目标价5000美元，比现在高出约15%\n• 短期金价波动带来盈利压力，但运营端现金流能对冲\n\n2️⃣ 两家公司的关键数字对比\n• AngloGold：自由现金流收益率10.5%，估值4.7倍EBITDA\n• Gold Fields：自由现金流收益率12%，估值3.6倍EBITDA\n• 两者都低于全球同行和历史均值，但现金流质量不错\n\n3️⃣ 催化剂与风险点\n• AngloGold：Obuasi矿爬坡、Nevada项目进展\n• Gold Fields：Windfall项目推进\n• 共同风险：加纳政策不确定性、能源成本通胀\n\n4️⃣ 估值调整逻辑\n• 研报下调了目标倍数（ANG从8x→7x，GFI从8x→6x）\n• 但上调了金价预期，两者对冲后目标价变动不大\n• ANG目标价上调至130美元，GFI下\n\n[... middle omitted ...]\n\n 2027 vs spot at c\\$4,350. We have updated our estimates with latest gold prices leading to net upgrades to our EBITDA estimates. However, we have lowered the target multiples used to set TPs \n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R011",
    "title": "NOM：全球资金正在重新定价“美国例外论”，但亚洲的撤退信号更值得警惕",
    "digest": "[wechat_article.md]\n# NOM：全球资金正在重新定价“美国例外论”，但亚洲的撤退信号更值得警惕\n\n全球资金流向正在讲述一个比表面数据更复杂的故事。这份NOM在2026年6月9日发布的亚洲外汇周报，提供了一组高频资金流动数据，覆盖截至6月5日至6日的五个交易日。如果只扫一眼标题，你可能会得出一个简单的结论：资金仍在涌入美国，新兴市场正在失血。但真正重要的不是这个方向判断，而是流动的结构性变化——AI乐观情绪驱动的美国权益资金流入依然强劲，但债券市场几乎无人问津；新兴市场资金连续第二周转为净流出，且流出的速度在加快；韩国散户在连续两个月净卖出后开始回补，台湾投资者却在加速抛售美元债券。\n\n这些信号叠加在一起，指向一个更深刻的判断：市场对“美国例外论”的定价正在从全面拥抱转向选择性下注，而亚洲市场的资金撤退可能才刚刚开始。这不是一次简单的风险偏好切换，而是一次资产定价逻辑的重新校准。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI乐观情绪正在制造一种“虚假的全面繁荣”\n\n截至6月5日的五个交易日内，外国投资者向美国权益基金净投入25.6亿美元。这个数字虽然略低于前一周的29.1亿美元，但如果拉长到月度维度，5月美国权益基金的外资流入总额达到87.8亿美元，是自2026年1月（95.6亿美元）以来的最高单月水平。\n\n表面上看，这是一个令人振奋的信号。但真正值得追问的是：这些钱到底流向了哪里？\n\nNOM的数据没有拆分行业，但结合近期市场叙事，答案几乎是确定的——AI相关资产。从2025年底到2026年上半年，AI主题始终是驱动全球资金流向美国的核心引擎。问题在于，当AI乐观情绪成为唯一支撑美国权益流入的支柱时，这个市场就变得极其脆弱。一旦AI叙事出现任何裂痕——无论是监管收紧、技术突破放缓，还是商业化不及预期——这些资金流出的速度可能比流\n\n[... middle omitted ...]\n\n享更详细的资金流向拆解，以及基于这些数据做出的资产配置判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球资金流向出现新变化\n\n📊 资金流向速览\n\n最近一周全球资金流向有个明显的信号：AI热情不减，但新兴市场开始被抽水。\n\n投行研报数据显示，6月1-5日，外资净买入美国股票基金约26亿美元，虽比前一周的29亿略降，但5月整月净流入88亿美元，创今年1月以来新高。\n\n反观新兴市场，同一时期ETF净流出2.5亿美元，而前一周还是净流入4.75亿。资金偏好一目了然。\n\n1️⃣ 美国仍是吸金大户\n- 美国股票基金：5月净流入88亿美元，仅次于1月的95亿\n- 美国债券基金：5月净流入7.76亿，连续第二个月正流入\n- 6月初虽略有降温，但整体趋势未变\n\n2️⃣ 新兴市场遭遇回吐\n- 新兴市场ETF从净流入转为净流出\n- 5月净流入25亿，但4月还有63亿——速度在放缓\n- 资金似乎在“追涨”美国，而非布局新兴市场\n\n3️⃣ 韩国散户开始“回头”\n- 6月2-6日，韩国散户净买入美国资产1.39亿美元\n- 此前两周连续净卖出，合计流出6.01亿\n- 这次以买美股为主（净买2.35亿），卖美债（净卖0.95亿）\n\n4️⃣ 台湾投资者继续减持美债\n- 6月1-5日，净卖出美元计价债券基金1.96亿美元\n- 前一周净卖出1.\n\n[... middle omitted ...]\n\nnated bond funds between 1 and 5 June, and compared with net selling of USD149mn over the previous week.\n\n## Research Analysts\n\n## Asia FX Strategy\n\nCraig Chan - NSL\n\ncraig.chan@NOM.com\n\n+65 6\n\n[... middle omitted ...]\n\nrmation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R012",
    "title": "JPM：中国新ODI框架对全球银行的冲击比预期更广，财富管理业务的增量摩擦才刚刚开始",
    "digest": "[wechat_article.md]\n# JPM：中国新ODI框架对全球银行的冲击比预期更广，财富管理业务的增量摩擦才刚刚开始\n\n这份JPM最新研报揭示了一个被市场低估的关键信号：中国新的境外直接投资（ODI）监管框架，其影响范围远不止于跨境资金流动本身。该机构在与法律专家的深入讨论后，得出了一个比此前预期更为悲观的结论——无论是定义中国内地居民的范围，还是对存量海外资产的追溯，乃至对境外收入的覆盖，都意味着全球银行在亚洲财富管理业务上的增量摩擦可能才刚刚开始计价。\n\n为什么这个判断现在值得关注？因为全球银行正处在财富管理业务贡献快速提升的关键阶段。JPM数据显示，HSBC和渣打的财富收入在2025年都实现了24%的同比增长，而未来几年财富业务在集团收入中的占比预计将持续攀升。如果监管框架的执行力度超出预期，这些银行面临的不仅是新增客户的放缓，更是存量资产合规成本的系统性上升。\n\n这份研报的核心价值在于，它通过法律专家的解读，将抽象的政策框架翻译成了具体的业务冲击路径。以下是我们从这份报告中提炼出的五个关键洞察，以及一个报告尚未完全回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 中国内地居民的定义远比想象中宽泛，香港身份证不再是“豁免通行证”\n\n市场此前普遍认为，持有香港身份证的个人可以被视为香港居民，从而规避ODI框架的约束。但JPM邀请的法律专家给出了截然不同的解读：只要个人仍持有中国内地户籍（户口），且每年在内地停留超过183天，即使持有香港身份证（包括永久居民身份），仍可能被认定为“中国内地居民”。\n\n这个定义的改变意味着什么？它直接扩大了监管对象的人口基数。许多在香港工作、持有香港身份证但未注销内地户籍的高净值人士，将被纳入监管范围。对于银行而言，这意味着他们需要重新评估客户分类体系，而不是简单地把持有香港身份证的客户视为“\n\n[... middle omitted ...]\n\n展和银行应对策略，帮助读者在不确定性中找到更清晰的判断框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国财富新规：谁受影响最大？\n\n财富管理新规解析\n\n最近跟一位法律专家聊了中国最新的境外直接投资（ODI）新规，结论比预想的要复杂。简单说：**财富管理行业的合规门槛要提高了**。\n\n1️⃣ **“中国居民”定义比想象中宽**\n- 只要还持有中国户籍 + 每年在大陆住满183天，就算是中国居民\n- 哪怕有香港身份证，只要没注销内地户口，也算在内\n- 这意味着很多“新香港人”也逃不开新规\n\n2️⃣ **投资范围扩大**\n- 境外IPO套现、境外子公司收入，都可能纳入监管\n- 保险和房地产投资依然受限（人民币换汇后不能买海外房产和保险）\n- 存量海外资产可能也要申报\n\n3️⃣ **谁最受伤？**\n- HSBC：保险业务自营，受冲击更大（渣打是第三方分销模式）\n- UBS/宝盛：高净值客户受影响，新钱流入可能放缓\n- 整体来看，财富管理的新增资金将面临摩擦\n\n4️⃣ **监管工具箱**\n- CRS（共同申报准则）已经让监管对海外资产有基本了解\n- AI交叉验证数据，申报不完整可能触发审查\n- 长期看，合规渠道（如港股通）反而可能受益\n\n5️⃣ **数据支撑**\n- HSBC香港财富收入占集团7.6%，渣打占6.6%\n\n[... middle omitted ...]\n\ncted and includes anyone who still has a Chinese household registration & stays in China for more than 183 days (vs our previous expectation of those with a HK ID card as out of scope); 2) the\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 08 Jun 2026 08:02 PM BST\n\nDisseminated 09 Jun 2026 12:15 AM BST"
  },
  {
    "id": "R013",
    "title": "GS：日本通胀的“二阶导”拐点比绝对水平更重要",
    "digest": "[wechat_article.md]\n# GS：日本通胀的“二阶导”拐点比绝对水平更重要\n\n五月日本国内企业商品价格指数（CGPI）环比上涨0.9%，较四月2.8%的历史性飙升大幅回落。这份来自GS日本经济团队的月度数据解读，看起来只是一次常规的通胀追踪，但真正值得关注的信号，隐藏在环比增速的减速幅度和品类扩散的边际变化中。\n\n市场通常关注通胀的绝对水平——CPI同比是否破3%，CGPI是否创历史新高。但GS这份报告揭示了一个更微妙的判断：日本通胀正在经历从“全面跳升”到“结构性分化”的转折。四月的价格跳升是一次性的定价调整冲击，五月的读数才是判断持续性通胀压力的真实起点。\n\n对于任何关注日本资产定价、日元走势以及日本企业定价权可持续性的投资者来说，理解这个“二阶导”拐点，远比盯着同比数字的绝对值更重要。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 四月跳升是一次性定价调整，五月才是压力测试的真实基线\n\n四月CGPI环比飙升2.8%，是1980年4月以来（剔除消费税上调影响）的最大单月涨幅。这个数字本身容易引发对通胀失控的担忧。但GS报告明确指出，五月环比增速回落至0.9%，是因为“四月许多品类因价格修订出现的急剧上涨在五月暂时平息”。\n\n这意味着四月的数据更多反映的是企业集中调价窗口期的一次性行为，而非需求驱动或成本持续攀升的线性外推。五月的0.9%环比增速，虽然仍处于高位，但已经回到更接近趋势性的水平。真正的判断问题应该是：0.9%的月环比增速是否可持续？它背后是成本推动还是需求拉动？\n\nGS报告没有直接回答这个问题，但提供了关键线索：五月环比增速的减速是广泛性的，几乎所有主要品类都在减速，而非少数品类异常回调。这说明四月跳升后的“均值回复”是系统性的，而非结构性力量在减弱。\n\n对于企业决策者而言，这意味着不应将四月的数据作为未来成本预测的基准\n\n[... middle omitted ...]\n\n可以更深入地拆解那些报告没有完全展开、但实际影响巨大的变量。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本5月物价数据：涨幅放缓，但压力还在\n\n封面：物价涨速放缓\n\n副标题：4月创近45年最大涨幅后，5月回归理性\n\n---\n\n**1/ 整体趋势：涨势降温，但同比仍在加速**\n\n5月日本国内企业商品价格指数（CGPI）环比+0.9%，相比4月+2.8%的惊人涨幅明显回落（4月是1980年4月以来最大单月涨幅，不含消费税影响）。但同比从+5.3%加速至+6.3%，创2023年3月以来新高。\n\n简单说：涨价惯性还在，但冲劲减弱了。\n\n**2/ 分项拆解：能源和化工是主要推手**\n\n- 石油煤炭制品：环比+3.0%，贡献整体涨幅0.21pp，但远低于4月的+11.8%和0.75pp贡献\n- 化工产品：环比+2.3%，贡献0.19pp\n- 电力燃气水道：环比+3.5%，同样贡献0.19pp\n\n23个主要品类中，有4个环比下跌（生产机械、商业机械、电气机械、农林水产品）。\n\n**3/ 进口价格：涨幅也在收窄**\n\n5月日元计价进口价格环比+2.7%，4月曾达+8.7%。同比则从+21.0%加速至+25.5%。\n\n石油煤炭天然气环比+8.0%，贡献1.7pp（4月+27.3%）。化工和金属涨幅更小，乙烯价格环比-4.1%（\n\n[... middle omitted ...]\n\nic CGPI, yoy, May: +6.3%, April: +5.3%  \n■ Export price (yen basis), mom, May: +0.4%, April: +4.1%  \n■ Import price (yen basis), mom, May: +2.7%, April: +8.7%\n\n## MAIN POINTS:\n\nDomestic CGPI r\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R014",
    "title": "JPM：霍尔木兹海峡的“例外通行”不会改变全球LNG市场的结构性缺口",
    "digest": "[wechat_article.md]\n# JPM：霍尔木兹海峡的“例外通行”不会改变全球LNG市场的结构性缺口\n\n这份JPM在6月8日发布的全球LNG供应与航运追踪报告，表面上在更新一艘船的航迹——ADNOC的Mubaraz号在4月26日成为冲突后首艘满载驶出霍尔木兹海峡的LNG船，如今又重新进入海峡、靠近Das Island准备装货。但真正值得关注的判断藏在数据背后：即便海峡出现零星通行，JPM仍将其定性为“例外而非新常态”，并维持卡塔尔LNG产能到9月才能恢复到83%利用率的预测。这意味着2026年全年卡塔尔LNG产量将同比腰斩，从2025年的1.05亿吨降至仅0.6亿吨。市场可能正在低估这一供给缺口的持续时间和定价影响。\n\n这份报告的核心贡献，不是告诉你霍尔木兹海峡有船在动，而是提供了一个框架：把“地缘政治事件”转化为“可量化的供给约束”，并由此推演出JKM（东北亚LNG现货价格）对TTF（欧洲天然气基准价）的溢价将持续存在，甚至需要更高的价格来抑制亚洲需求、支撑欧洲储气。对于产业决策者和资产配置者而言，真正需要关注的不再是“冲突何时结束”，而是“后冲突时代的LNG定价机制正在被重写”。\n\n以下是我们从这份报告中提炼出的五个关键洞察，以及一个尚未被充分讨论的变量。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 霍尔木兹海峡的“例外通行”无法改变卡塔尔产能恢复的硬约束\n\nJPM追踪到，截至6月8日，霍尔木兹海峡内有9艘可用的LNG船。Al Daayen号当天驶出海峡、目的地为中国，而ADNOC的Mubaraz号在6月3日重新进入海峡。这些信号容易被解读为“供给正在恢复正常”，但报告明确警告：这些通行是例外，而非新常态。\n\n核心约束来自三个层面。第一，海峡内的LNG船数量有限，这天然限制了可立即装运的货物量。第二，即便海峡完全开放，卡塔尔的液化设施\n\n[... middle omitted ...]\n\n三个变量的变化，并在关键转折点出现时第一时间分享我们的分析。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n霍尔木兹海峡 LNG 船动了\n\n第一艘船重返海峡\n\nADNOC 的 Mubaraz 号，4月26日满载离开后，6月3日再次进入海峡，现在停在 Das Island 附近准备装货。\n\n卡塔尔能源的 Al Daayen 号今天（6月8日）驶出海峡，目的地显示为中国。\n\n目前海峡内还有9艘LNG船可用。\n\n1/ 卡塔尔恢复节奏\n某外资投行维持6月重启的基准判断，预测卡塔尔能源9月利用率达到83%，但2026全年利用率仅57%（2025年是105%）。\nCEO明确说：即使海峡完全开放，未受损的液化生产线恢复正常出口，至少还需要2-3个月。\n\n2/ 亚洲溢价在扩大\nJKM 比 TTF 贵约2美元/百万英热单位，夏季制冷需求 + 可能的超强厄尔尼诺事件推高了亚洲价格。\n美国墨西哥湾LNG增量全部流向亚洲，欧洲只能靠高价抑制需求来补库存。\n\n3/ 运价大幅回落\n苏伊士以西运价8万美元/天，以东4.5万美元/天，均较冲突第二周峰值跌超60%。\n\n4/ 新项目有隐忧\nGolden Pass 气源流量近3-4天再次接近零，该设施3月底才产出首船LNG，目前利用率远低于预期的80%，2026年最多5亿立方米产量可能面临风险。\n\n5\n\n[... middle omitted ...]\n\n>\n<summary>text_image</summary>\n\nVessels\nAll Types\nVessel History\nAL DRAYEN\nFIRISRAZ\n500 km\n</details>\n\nSource: Bloomberg Finance L.P.\n\nFollowing the two observed crossings, we count nine avai\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 08 Jun 2026 10:18 PM BST\n\nDisseminated 08 Jun 2026 10:22 PM BST"
  },
  {
    "id": "R015",
    "title": "摩根斯坦利：新兴市场真正的风险不是基本面，而是融资货币的单一化",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：新兴市场真正的风险不是基本面，而是融资货币的单一化\n\n全球经济正在经历一个罕见的错位阶段。美国增长强劲、利率预期重新定价、美元走强，而新兴市场的基本面却在持续改善——通胀回落、政策信誉修复、经常账户结构优化。这两个方向同时成立，却让大多数投资者的框架出现了盲区。\n\n摩根斯坦利最新发布的全球新兴市场策略报告《Finding Your Funder》，给出了一个反直觉的结论：市场对新兴市场的担忧方向错了。问题不在于是否应该持有新兴市场资产，而在于用什么货币来为这一头寸融资。\n\n这份报告的核心判断是：新兴市场资产本身的吸引力并未减弱，但传统的美元融资方式正在成为最大的约束。如果投资者继续以美元作为唯一的融资货币，即使新兴市场基本面继续向好，回报也可能被汇率波动侵蚀。而选择正确的融资货币组合——尤其是以加元或G3篮子货币融资——可以在不牺牲收益的情况下显著降低波动。\n\n这不是一个关于“买不买”的讨论，而是一个关于“怎么买”的结构性建议。在当前美元强势的背景下，这个视角可能比大多数宏观判断更具实操价值。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 美元走强并非新兴市场的终结信号，而是暴露了融资结构的脆弱性\n\n报告开篇就点明了当前市场的核心矛盾。摩根斯坦利团队在5月发布的中期展望中，对新兴市场本地货币资产的基本面持建设性态度，客户也普遍认同两个判断：新兴市场基本面在改善，且全球投资者对新兴市场本地货币资产的配置仍有提升空间。\n\n但分歧出现在宏观层面。美国强劲的就业数据推动利率重新定价，市场对美联储年内降息的预期持续降温，美元指数走强。许多客户认为，美国股市的超额表现和增长前景将继续支撑美元——至少在DXY层面如此。\n\n摩根斯坦利并没有改变其对美元的看空立场，但报告承认，美元走强对新兴市场确实构成显著压力，尤\n\n[... middle omitted ...]\n\n议题，我们会在群内分享更多来自原始报告的数据图表和延伸分析。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美元反弹，新兴市场还能跟吗\n\n📉 新兴市场还能买吗？\n\n美元走强，新兴市场压力不小\n\n某外资投行最新研报认为：新兴市场的基本面仍然扎实，货币和财政纪律在改善，相比发达国家更有韧性。但短期美元反弹确实给市场带来了扰动。\n\n1️⃣ 核心观点：新兴市场依然有吸引力\n- 新兴市场资产基本面偏强，尤其是拉美和部分东欧国家\n- 亚洲相对偏弱，但整体仍优于发达市场\n- 投资者目前配置偏低，有增持空间\n\n2️⃣ 最大的变数：美元\n- 美国经济数据强劲，美元短期可能继续走强\n- 但新兴市场货币相对G3货币仍有望跑赢\n- 关键在于怎么“融资”来买新兴市场\n\n3️⃣ 一个有趣的发现：融资币种的选择\n- 用欧元融资买新兴市场，今年表现最好（年化回报9%，波动仅4%）\n- 用加元融资也不错：年化回报3.6%，波动6.3%，最大回撤仅-12.3%\n- 用篮子货币（如美元+欧元+日元）融资，长期表现更稳定\n\n4️⃣ 怎么操作更聪明？\n- 单一货币融资有风险，比如用日元融资虽然收益高，但波动也大\n- 用一篮子G3货币（美元、欧元、日元）融资，Sharpe比率更高，回撤更小\n- 加元是单币种中的“优等生”，但篮子策略更稳健\n\n📌 总结\n新兴市\n\n[... middle omitted ...]\n\ne the return profiles of long EM exposure with different funding currencies. CAD has been an effective choice by raising returns while lowering vol.  \n- Across multiple time frames though, usi\n\n[... middle omitted ...]\n\nch Analysts/Strategists and are not opining on or expressing recommendations on equity securities: Nimish M Prabhune; Simon Waever; Ioana Zamfir; Emma C Cerda; Gek Teng Khoo; Neville Z Mandimika; James K Lord.\n\n© 2026 MS"
  },
  {
    "id": "R016",
    "title": "HSBC：AI产业真正被低估的不是消费者市场，而是企业级需求的加速爆发",
    "digest": "[wechat_article.md]\n# HSBC：AI产业真正被低估的不是消费者市场，而是企业级需求的加速爆发\n\n当市场还在争论ChatGPT的用户增长是否见顶、OpenAI能否守住领先地位时，一份来自HSBC的最新研报给出了一个更值得关注的信号：全球AI产业的可寻址市场（TAM）正在被系统性重估，而驱动这一重估的核心力量，并非来自消费者端，而是来自企业级市场的结构性提速。\n\n这份发布于2026年6月的报告，将2026年至2030年全球AI行业累计收入预期上调了38%，从1.84万亿美元提升至2.55万亿美元。但真正值得注意的不是这个数字本身，而是数字背后的分化：B2B收入预期被大幅上调74%，而B2C收入预期反而被下调了20%。\n\n这意味着什么？意味着AI产业的增长引擎正在发生一次静悄悄的切换。过去三年，市场习惯用ChatGPT的月活增长、OpenAI的融资故事、消费者对聊天机器人的好奇心去定义这个行业的想象力。但HSBC的报告清楚地告诉我们：接下来的五年，真正决定行业走向的，是企业客户是否愿意为AI代理、代码工具和行业解决方案买单，而不是消费者是否愿意为聊天机器人订阅费升级。\n\n这不是一个关于“AI是否过热”的判断，而是一个关于“AI的钱到底从哪里来”的结构性重估。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. B2B市场正在经历一次由Agentic AI驱动的非线性加速\n\nHSBC之所以将B2B收入预期大幅上调74%，核心依据是Agentic AI（代理型AI）的涌现正在改变企业采用AI的方式。与传统的对话式AI不同，Agentic AI能够自主执行多步骤任务、调用外部工具、与企业现有系统深度集成。这不再是一个“问答工具”，而是一个“数字员工”。\n\n报告特别指出，Anthropic在这一领域的领先地位已经确立。截至2026年5月，Anthro\n\n[... middle omitted ...]\n\n国模型的非对称竞争路径、以及OpenAI融资缺口的最新动态。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI行业大洗牌：B2B起飞，B2C遇冷\n\nB2B爆发，B2C降温\n\n最近某外资投行更新了AI行业到2030年的收入预测，结论很明确：B2B市场正在加速爆发，而B2C那边却有点凉。\n\n1️⃣ B2B市场大幅上调\n- 2026-2030年B2B行业收入预期上调74%\n- 核心驱动力：Agentic AI带来新应用场景，编程工具快速迭代\n- 目前B2B领域，Anthropic是绝对领先者，OpenAI和Gemini紧随其后\n\n2️⃣ B2C市场下调20%\n- 用户增长不及预期，尤其是领头羊OpenAI\n- 低价套餐拉低ARPU，订阅和广告收入受影响\n- 消费者聊天机器人的变现比想象中更难\n\n3️⃣ 整体AI市场仍上调38%\n- B2B的强劲增长完全覆盖了B2C的下滑\n- 2026-2030年累计行业收入预计达2547亿美元\n\n有意思的是，Anthropic在B2B的ARR（年化收入）已经超过OpenAI，达到470亿美元，而OpenAI还在300亿左右徘徊。两家都在积极布局企业市场，OpenAI甚至砍掉了Sora等副线项目，全力押注编程和企业用户。\n\n全球AI市场正在形成西方寡头格局——算力成本太高，形成了天然壁垒\n\n[... middle omitted ...]\n\naccelerating significantly and (2) the B2C market is not growing as fast as we were expecting. For background, see Global Tech Platforms: OpenAI: Back to chatbots – new HSBC forecasts, 1 April\n\n[... middle omitted ...]\n\n2daa1fe2ce7fada951097.jpg)\n\n## Newsletters\n\nSubscribe to our monthly collection of free to view reports and interviews in Open Pass or read our bite-sized round up of research covering our nine key themes, Talking Points"
  },
  {
    "id": "R017",
    "title": "JPM：中国车企在欧洲的真正优势不是价格，而是零售执行与生态系统的护城河",
    "digest": "[wechat_article.md]\n# JPM：中国车企在欧洲的真正优势不是价格，而是零售执行与生态系统的护城河\n\n市场对中国汽车出海的讨论，长期集中在两个叙事上：一是关税壁垒，二是低价倾销。但JPM最近一份基于欧洲实地调研的报告，提供了一个截然不同的判断框架。\n\n这份报告的核心发现是：中国车企在欧洲的份额增长，已经不是简单的“便宜BEV出口”故事。2026年4月，中国品牌在欧洲新能源车市场的份额达到18.3%，是去年同期的三倍以上。更关键的是，这一增长背后，是三个被市场低估的结构性变量在同时起作用——产品组合策略、零售执行能力和充电生态建设。\n\n报告分析师团队在伦敦和巴黎的BYD门店进行了实地走访，并与欧洲汽车大会的行业参与者进行了深度交流。基于这些第一手信息，JPM将比亚迪和吉利2026年的海外销量预测分别上调了约15%和30%。\n\n以下是我们从这份报告中提炼出的四个关键洞察，以及一个报告尚未完全回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 欧洲不是一个纯BEV市场，中国车企正在用“混合动力+品牌阶梯”组合赢得过渡期\n\n市场普遍认为中国电动车出海就是卖纯电，但JPM的门店调研揭示了一个截然不同的现实：在欧洲这个“混合动力过渡市场”，PHEV的贡献正在快速上升。\n\n在巴黎和伦敦的BYD门店，销售人员反馈，订单中PHEV占比高达50%到60%。最畅销的PHEV车型Seal U DMi起售价约4万欧元，月供仅600-700欧元，等待时间约一个月。而纯电车型Sealion 7虽然也被定位为“高性价比”产品，但在巴黎门店的等待时间长达三到四个月，表明供应端存在明显瓶颈。\n\n这意味着什么？中国车企的竞争优势并非来自单一价格战，而是来自“多动力总成组合+品牌阶梯”的产品矩阵。比亚迪从主流品牌到高端品牌Denza的布局，吉利通过极氪等品牌的多\n\n[... middle omitted ...]\n\n析，欢迎加入我们的知识星球微信群，与产业研究者一同深入讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国车企，正在欧洲悄悄变强\n\n欧洲实地调研：中国车企正在赢\n\n上周跟某外资投行的欧洲汽车会，去伦敦和巴黎看了比亚迪门店。结论很直接：中国车企的海外扩张，比想象中更有章法。\n\n**1/ 欧洲不是纯电战场，是“混动过渡期”**\n- 巴黎和伦敦门店，PHEV（插混）需求非常强。Seal U DMi是店员口中的畅销款，订单里PHEV占了50-60%。\n- 纯电也在卖，但靠的是“高配低价”——比如Sealion 7标配L2级智驾+360影像，德系竞品这些都要选装加钱。\n- 消费者比的不是裸车价，而是“每月月供”和“配置性价比”。\n\n**2/ 零售打法变了：渠道+售后+残值管理**\n- 比亚迪在欧洲密集铺门店，试驾转化率高达45-50%。\n- 重点不是打价格战，而是靠售后网络和残值管理建立信任。门店促销折扣只有5-7%，更多是营销习惯。\n- 这对传统品牌是压力：中国车标配高，德系还在卖选装包。\n\n**3/ 下一个护城河：充电生态**\n- 比亚迪计划到2026年底在欧洲建3000个超快充桩（英国300个）。\n- 高端品牌Denza Z9 GT下半年欧洲首秀，配闪充技术（10%-97%只需9分钟）。\n- 巴黎店员透露：Den\n\n[... middle omitted ...]\n\nect our positive stance, we raise our 2026 overseas sales forecasts for BYD/Geely by \\~15%/30%. Key strategic highlights below:\n\n- Europe: Mixed-propulsion transition market: Chinese OEMs are \n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R018",
    "title": "JPM：香港房价已接近全年预测上限，但真正的不确定性不在价格本身",
    "digest": "[wechat_article.md]\n# JPM：香港房价已接近全年预测上限，但真正的不确定性不在价格本身\n\n这份JPM最新发布的Property Data Monitor，数据本身并不复杂。但如果我们只把它当作周度数据读，就错过了报告真正想传递的信号。\n\n核心判断是：香港住宅市场正在快速接近JPM2026年全年房价预测区间10%-15%的上沿——年初至今已涨9.6%，距离上限仅0.4个百分点。这意味着，如果当前趋势延续，JPM对全年的基准预测可能在未来几周内被触及甚至突破。但报告真正值得关注的，不是这个数字本身，而是它背后揭示的市场结构：一手楼定价策略正在发生微妙但重要的转变，而内地市场的库存消化节奏，正在从“量”的改善转向“价”的博弈。\n\n以下是我们从这份报告中提炼的五个关键洞察，以及一个报告尚未完全回答的问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 香港一手楼定价正在从“折让”转向“溢价”，这可能是市场信心分层的信号\n\n过去两年，香港开发商普遍采用“低开”策略——一手楼定价低于或持平于二手市场，以加速去化。但这份报告显示，上周推出的三个新盘中，有两个定价显著高于周边二手物业：Pavilia Rosa（九龙塘）首批均价达33,800港元/平方呎，高出二手市场41%，创过去五年一手新盘定价最高纪录。即使是定价相对保守的Headland Residences（柴湾）和One Victoria Cove Ph4（红磡），仍分别高出二手市场15%和18%。\n\n这组数据意味着什么？不是开发商集体乐观，而是市场正在出现明显的“价格分层”。高端地段（如九龙塘）的一手楼开始敢于定出显著溢价，而中端项目仍在谨慎试水。报告没有直接展开这个判断，但结合其后续提到的深圳高端住宅销售强劲、中端疲软的分化现象，可以合理推断：香港住宅市场正在经历类似的“K型复苏”——\n\n[... middle omitted ...]\n\n球资产配置和产业周期的读者一起，持续追踪这些关键变量的演变。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n一线城市二手房挂牌量降了\n\n📉 五月数据有点意思\n\n北京挂牌量降幅最大，库存压力在减轻\n\n最近翻到某外资投行的地产监测报告，发现几个有意思的细节，分享给大家参考。\n\n**大陆市场：二手房挂牌量在降**\n- 5月一线城市二手房挂牌量环比降0.7%\n- 库存月数从18.8个月微降到18.6个月\n- 北京降幅最大（-2%），库存月数降到16.6个月\n- 上海紧随其后（-1%），库存月数从12.4降到11.9\n\n**新房成交有回暖迹象**\n- 60城新房成交同比增18%，比上周的10%明显提速\n- 12城二手房成交同比增38%，上海（+57%）和深圳（+55%）是主力\n- 年初至今，12城二手房成交累计同比增6%，上海贡献最大（+14%）\n\n**两个先行指标值得关注**\n1. 中原一线城市二手房报价指数持平在17.7（数值越高表示涨价项目越多）\n2. 中原经理人信心指数持平在54（>50意味着市场情绪偏正面）\n\n**香港市场：楼价年内涨了9.6%**\n- 最新一周楼价指数环比涨0.3%\n- 年初至今累计涨幅9.6%，距离某外资投行对2026年全年10-15%的预测仅差0.4%\n- 但成交有点冷：35大屋苑二手房成交5\n\n[... middle omitted ...]\n\n 12-city secondary sales registrations rose 38% Y/Y (last week: +14% (Figure 5), Shanghai (+57%) and Shenzhen (+55%) saw the strongest Y/Y growth among tier-1 cities. YTD, 12-city secondary sa\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 08 Jun 2026 11:18 PM HKT\n\nDisseminated 08 Jun 2026 11:18 PM HKT"
  },
  {
    "id": "R019",
    "title": "摩根斯坦利：市场低估的并非政策力度，而是成交量回升背后的结构性分化",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：市场低估的并非政策力度，而是成交量回升背后的结构性分化\n\n过去一周，中国房地产市场的周度数据出现了一组值得注意的信号。摩根斯坦利最新发布的周度数据库追踪报告显示，截至6月7日当周，50城新房注册成交量同比增长23%，较前一周14%的同比增速明显抬升。10城二手房成交量同比增幅则从9%扩大至23%。\n\n单看这些数字，很容易被解读为“政策见效、市场回暖”。但真正重要的判断藏在数字背后：这轮成交量回升并非全面复苏，而是一场结构性分化正在加速——一线城市二手房正在成为资金真正的“避风港”，而新房市场的反弹高度依赖供给端的节奏控制，并非需求端的自发修复。\n\n这份报告的价值不在于告诉你“市场变好了”，而在于它提供了拆解“变好”背后真实驱动力的数据框架。以下是我们基于报告核心数据的四点解读，以及一个报告尚未完全回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 二手房成交量正在成为比新房更可靠的市场温度计\n\n报告最核心的信号来自二手房市场。10城二手房周度成交量同比增长23%，年初至今累计增幅已达6%。更值得关注的是结构：一线城市二手房成交同比增幅从前一周的12%跃升至34%，二线城市也从6%提升至17%。\n\n这意味着什么？二手房市场正在承接新房市场的部分需求外溢。当购房者对期房交付信心不足、对开发商信用风险仍有顾虑时，二手房“所见即所得”的属性正在转化为实实在在的成交优势。这个趋势在年初至今的数据中已经形成了持续轨迹，而非单周波动。\n\n对产业决策者而言，这一信号意味着：未来判断市场真实温度，二手房成交量可能比新房数据更具先行指标意义。如果二手房成交量能够持续维持在正增长区间，才意味着需求端真正出现了底部企稳的可能。而新房成交的波动，更多反映的是供给节奏和开发商推盘意愿。\n\n![研报原图 2](as\n\n[... middle omitted ...]\n\n，一起拆解这份报告的完整Excel数据表和更多历史对比图表。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n6月第一周，楼市数据有变化\n\n📊 新房二手房都在涨？\n\n**1/ 新房：50城周度成交同比+23%**\n比上周的+14%明显提速\n但年初至今累计仍是-12%\n原因？去年端午假期在6月初，基数较高\n\n**2/ 分城市看，二线最猛**\n- 一线：同比+1%（上周是+27%，回落明显）\n- 二线：同比+30%（上周+8%，加速）\n- 三线：同比+22%（上周+24%，略降）\n\n**3/ 二手房：10城同比+23%**\n比上周的+9%明显加速\n一线尤其突出：同比+34%（上周+12%）\n\n**4/ 去化率：上海新盘少，拉高整体**\n本周整体去化率100%，上周才53%\n一线城市去化率100%，上周63%\n二线本周没新盘推出，上周42%\n\n**5/ 挂牌价指数稳定**\n中原6城二手房挂牌价指数17.5%，与前一周持平\n一线城市中介指数54.4，略高于上周53.8\n\n整体看，6月首周数据有改善\n但年初累计新房成交仍在下降\n二手房表现相对更好\n\n你们城市最近楼市怎么样？\n欢迎一起讨论\n\n#学习笔记\n\n[source_mineru.md]\n## China Property | Asia Pacific\n\n# Weekly \n\n[... middle omitted ...]\n\neased 30% YoY (vs. +8% YoY).  \n• Tier 3 city sales increased 22% YoY (vs. +24% YoY).\n\nWeekly secondary registered unit sales in 10 cities increased 23% YoY (vs. +9% YoY in the previous week), \n\n[... middle omitted ...]\n\n>Yuexiu Property Co Ltd (0123.HK)</td><td>O (09/27/2024)</td><td>HK$4.30</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted."
  },
  {
    "id": "R020",
    "title": "GS：中国数据中心市场真正被低估的不是投资规模，而是电力需求的非线性跃迁",
    "digest": "[wechat_article.md]\n# GS：中国数据中心市场真正被低估的不是投资规模，而是电力需求的非线性跃迁\n\n当市场还在热议“2万亿投资计划”能否落地时，一份来自GS的研报揭示了一个更值得关注的信号：中国国家能源局（NEA）预计，到2030年数据中心电力消费将达到800 TWh。这个数字意味着什么？它意味着中国数据中心用电量将以36%的年复合增速增长，到2030年将占全国总用电量的6%，远超当前1.6%的水平。\n\n更关键的是，这一预期已经超过了GS自己对美国数据中心市场的预测——726 TWh。换句话说，中国正在从“跟随者”变为“引领者”，而市场对这一结构性变化的定价可能还远远不够。\n\n这份报告的核心判断并非“2万亿投资”本身，而是这背后隐含的电力需求非线性增长逻辑。当多数投资者还在纠结于政策能否兑现、建设节奏会不会低于预期时，真正需要追问的问题应该是：如果需求增速真的达到NEA预测的水平，哪些环节会被迫重新定价？\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 2万亿投资计划不是新闻，真正的新信息是NEA的需求预测比GS自己的模型更乐观\n\n2025年1月，国家发改委、国家数据局、工信部联合发布的《国家数据基础设施建设指引》中，国家数据局就已提出未来五年数据基础设施将吸引约2万亿直接投资。这一数字并非新消息，但市场此前并未充分消化其隐含的需求端含义。\n\nGS研报的核心贡献在于，它将NEA在2026年5月发布的数据中心电力需求预测与自己的模型进行了对比。NEA预计2030年数据中心用电量达800 TWh，而GS自己此前的预测是IT电力需求增速约为20%的年复合增长率。两者之间的差距，正是市场认知的盲区。\n\n这里的逻辑链条值得拆解：如果数据中心用电量真的以36%的增速增长，考虑到PUE（电能利用效率）的持续改善，IT设备本身的电力需求增速将更快。这\n\n[... middle omitted ...]\n\n一起探讨——这些问题的答案，可能比2万亿投资本身更值得关注。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国砸2万亿建数据中心，2030年用电量超美国\n\n2万亿，5年\n\n数据中心用电量将占全国6%\n\n最近Bloomberg一条消息引发关注：中国准备在未来5年花约2万亿人民币（2950亿美元）建设数据中心。这笔钱不是空穴来风，今年1月发改委、国家数据局、工信部联合发布的文件里就提到过，数据基础设施预计吸引约2万亿直接投资，包括网络、算力、安全设施等。\n\n几个有意思的点：\n\n1️⃣ 2030年数据中心用电量预测比我们想的更猛\n国家能源局预计，到2030年中国数据中心用电量将达800TWh，相当于2025-2030年复合增速36%（2025年才170TWh）。这个数字比某外资投行之前的预测（20%增速）高出一大截。更关键的是，800TWh意味着数据中心用电将占全国总用电量的6%（2025年仅1.6%）。\n\n2️⃣ 可能超越美国数据中心用电量\n同样是2030年，美国数据中心用电量预测为726TWh，中国这个800TWh的数字意味着——中国数据中心用电量可能反超美国。背后反映的是AI算力需求爆发。\n\n3️⃣ 当前增速已经很快\n2026年1-4月，全国互联网数据服务业用电量同比增长44%，这个数字说明需求已经在加速。\n\n⚠\n\n[... middle omitted ...]\n\na Infrastructure were jointly issued by the National Development and Reform Commission (NDRC), the National Data Administration (NDA), and the Ministry of Industry and Information Technology (\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R021",
    "title": "JEF：储能市场的真正拐点不是增长，而是增长的结构性分化",
    "digest": "[wechat_article.md]\n# JEF：储能市场的真正拐点不是增长，而是增长的结构性分化\n\n这份研报最值得看的判断，并非2026年全球储能装机将增长80%——这个数字已经在预期之内。真正重要的信号是：储能市场的增长正在从“总量驱动”转向“场景驱动”，而不同场景的竞争壁垒、利润结构和投资逻辑正在快速分化。那些能在AI数据中心储能、工商业储能和户用储能三个赛道同时建立优势的企业，将享受估值溢价；而只依赖单一市场或单一产品的公司，可能面临增长见顶后的残酷洗牌。\n\nJEF在SNEC 2026首日与华为储能专家、SMM专家、远景能源及多家头部企业高管的交流，揭示了一个正在发生的结构性变化：储能不再是光伏的附属品，而是正在成为独立于光伏的、由AI算力需求驱动的全新增长极。这一判断如果成立，将重塑整个产业链的估值体系。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 全球储能装机80%增长的背后，真正驱动力量正在从政策转向算力\n\nJEF专家预计2026年全球储能装机将超过150GWh，同比增长80%，且2026年后仍将保持20-30%的年增长率。但比总量更值得关注的是增长的结构：中国仍占全球60%的份额，但美国AI数据中心储能需求正在成为新的增长引擎。\n\n华为储能产品总监明确指出，美国AIDC储能需求预计2026年翻倍至10GWh，到2030年将增长至70-80GWh。这意味着未来五年，仅美国AI数据中心这一个场景，就将创造约7-8倍的储能增量。这与传统认知中“储能增长靠新能源配储”的逻辑完全不同——AI数据中心储能的核心诉求是电网稳定性、负载平滑和备用电源，而非新能源消纳。\n\n这一判断的产业含义是：储能企业的技术路线选择将出现分化。面向AI数据中心场景，需要的是高可靠性（系统可用性99.999%）、快速响应和与燃气轮机/柴油发电机的协同能力。那些在电力电\n\n[... middle omitted ...]\n\n这些关键假设的验证节点，以及如何根据不同的情景调整投资框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球储能，2026年要加速了\n\n储能加速，2026年全球要破150GWh\n\n全球储能装机预计2026年超150GWh\n\n最近看了一份某外资投行的SNEC 2026调研笔记，信息量很大。几个核心判断分享出来，一起讨论。\n\n1/ 全球储能装机要加速了\n- 2026年全球储能装机预计超150GWh，同比+80%\n- 中国占全球60%份额，仍是主力\n- 2026年后增速会放缓到20-30%/年\n\n2/ 户用储能：欧洲是主要增长引擎\n- 全球户储出货2026年预计30GWh，同比+14%\n- 欧洲占全球户储约50%，2026年预计增速30%\n- 增长驱动：系统升级、阳台储能快速扩张\n- 澳大利亚补贴退坡后，专家仍预计2026/27年增长20%\n\n3/ 工商业储能：66%增长，AIDC是核心\n- 2026年全球工商业储能装机预计32GWh，同比+66%\n- 中国占60%，美国AIDC（人工智能数据中心）是主要增长点\n- 美国AIDC储能需求2026年翻倍至10GWh，2030年预计达70-80GWh\n\n4/ 光伏行业：供给侧改革在路上\n- 行业成本核查预计2025年8-9月启动，但执行节奏会比较温和\n- 专家认为大厂破产\n\n[... middle omitted ...]\n\n YoY in 2026, incl upgrades to larger ESS systems, rapid expansion of balcony ESS, etc. 3) Annual C&I ESS installation is expected to grow by 66% YoY to 32GWh in 2026 (China acct for 60% of to\n\n[... middle omitted ...]\n\nrd\\_iapd\\_Brochure.aspx?BRCHR\\_VRSN\\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://avatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.\n\n© 2026 JEF"
  },
  {
    "id": "R022",
    "title": "JEF：AI竞争已从模型性能转向Agent生态与成本效率的再定价",
    "digest": "[wechat_article.md]\n# JEF：AI竞争已从模型性能转向Agent生态与成本效率的再定价\n\n这份报告最值得关注的核心判断是：中国AI模型正在从“追赶性能”切换到“定义成本效率”的新阶段，而真正驱动token消耗爆发式增长的不是聊天场景，而是Agent间协作（A2A）与行业专用工具链的落地。JEF在这期AI系列研报中提供了超过50个数据点，但最关键的信号隐藏在Token消耗的环比变化和模型排名的结构性位移中——中国模型在OpenRouter平台上的周Token消耗首次超越美国模型，而排名第一的DeepSeek V4 Flash单周消耗量达到3.69万亿Token，几乎是第二名腾讯Hy3 preview的1.25倍。\n\n这不是一个简单的“中国大模型跑得更快”的故事。JEF的数据揭示出三个正在重塑行业格局的结构性变量：第一，Agent-to-Agent的生态化协作正在替代单一模型的能力竞赛，腾讯与美团、手机厂商的A2A合作是这一趋势的缩影；第二，中国模型在API成本上仅为美国模型的几分之一，这种成本优势在推理量持续放大的背景下，正在改写云服务商和AI应用层的利润模型；第三，OpenAI和Anthropic正在向金融和法律等垂直领域加速渗透，这意味着通用模型的红利期正在收窄，行业专用Agent将成为下一轮竞争的主战场。\n\n以下五个维度，是理解这份报告真正含义的关键切口。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. Token消耗的结构性跃升背后，是Agent从“对话”到“工作流”的范式切换\n\nJEF的数据显示，截至6月1日当周，OpenRouter平台周Token消耗环比增长13.5%至36.1万亿。表面上看这是用量增长，但真正值得追问的是：什么场景在驱动这种增长？报告明确指出，2026年2月Token消耗的显著跃升有两个直接原因——Co\n\n[... middle omitted ...]\n\n数据和框架，但最终的判断需要投资者基于自己的行业认知来做出。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI圈正发生一场“Agent到Agent”的联结革命\n\nAgent生态正在重塑\n\n1/ 腾讯正搭建Agent-to-Agent（A2A）生态。元宝App已接入美团AI助手“小美”，用户提交本地生活需求时，两个Agent直接通信完成服务。手机厂商OPPO、小米、华为、vivo、荣耀也已接入，用户对手机语音助手说句话，就能直接发微信消息或启动音视频通话——不再需要手动打开微信App。\n\n2/ 阿里通义千问App开放第三方Agent和技能接入，首批合作包括肯德基、瑞幸、蜜雪冰城、东航。用户可以在一个App里完成点餐、买咖啡、查航班，一站式个性化服务。6月1日还发布了Qwen3.7-Plus，多模态交互+统一图形/命令行界面，能同时处理视觉和文本任务。\n\n3/ 美图与WPS合作，WPS用户可以直接用美图AI功能生成海报和短视频，尤其适合电商商家做营销素材。\n\n4/ OpenAI在Anthropic之后也推出金融和法律专用AI工具，Codex新增6个金融插件，法律插件正在开发中。Anthropic5月已发布10个金融服务Agent模板。\n\n5/ 可灵AI全球用户突破1亿（6月26日），比2025年底的6000万增长67\n\n[... middle omitted ...]\n\nter, pricing for different models, model intelligence in Artificial Analysis, user trends by sub-sector and other industry data for analysis.\n\nTencent: Building up Agent-to-Agent ecosystem. Th\n\n[... middle omitted ...]\n\nd\\_iapd\\_Brochure.aspx?BRCHR\\_VRSN\\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://javatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.\n\n© 2026 JEF"
  },
  {
    "id": "R023",
    "title": "摩根斯坦利：AI资本开支已超越互联网泡沫，但市场尚未定价折旧的滞后冲击",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：AI资本开支已超越互联网泡沫，但市场尚未定价折旧的滞后冲击\n\n这份摩根斯坦利GVAT策略团队在2026年6月发布的研报，提供了一个关键但容易被忽视的视角：AI基础设施投资的规模不仅在总量上创下纪录，更在资本密集度、融资结构和资产负债表外承诺三个维度上，同时超越了市场此前的认知边界。\n\n报告的核心判断可以概括为一句话：市场当前对AI投资的讨论，仍然停留在“资本开支增速”这个旧框架里，而真正需要被重新定价的，是这些投资在未来三年内如何转化为折旧、如何影响利润率、以及资产负债表外的租赁和采购承诺如何改变行业的风险分布。\n\n这不是一份关于“AI是否过热”的报告。它是一份关于“当资本开支峰值已成定局，哪些财务指标将接力成为新的市场叙事”的路线图。对于产业决策者和机构投资者而言，理解这份报告的框架，比争论资本开支何时见顶更有价值。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 资本密集度超过互联网泡沫峰值，但融资结构的变化比数字本身更重要\n\n摩根斯坦利预测，2026至2028年，超大规模云服务商的资本开支与销售比将分别达到36%、44%和42%。作为对比，2000年互联网泡沫时期，光纤相关投资的峰值也不过32%。这意味着，即便以最宽松的历史标准衡量，当前的投资强度也已经进入了一个前所未有的区间。\n\n但真正值得关注的不是数字本身，而是数字背后的融资结构。报告明确指出，增量资本开支的修订现在往往伴随着资本募集或创新融资安排。融资租赁的使用正在推高名义资本开支数字。当资本开支中的相当一部分来自租赁而非自有现金时，企业的财务灵活性和风险敞口会发生本质变化。\n\n这带来的第一个含义是：资本开支的“真实”规模比账面数字更大。因为融资租赁意味着未来数年内持续的现金流出义务，而这些义务在传统的资本开支统计中往往只体现为一次性投\n\n[... middle omitted ...]\n\n于最新SEC文件的更新图表，并针对这些未解问题进行持续跟踪。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI投研笔记｜超算资本开支已超科网泡沫\n\n封面：AI算力基建的“疯狂”账本\n\n副标题：租赁承诺超8000亿美元意味着什么\n\n---\n\n最近翻到一份外资投行的AI生态研报，几个数字让人印象深刻：\n\n**1️⃣ 资本强度创历史纪录**\n超大规模云厂商的资本开支占收入比，预计2026-2028年达到36%-44%，已经超过2000年科网泡沫时期32%的峰值。而且这还没算上融资租赁的杠杆效应。\n\n**2️⃣ 近1万亿美元的长期采购承诺**\n截至2026年Q1，主要AI参与者的长期采购承诺接近1万亿美元，未开始的租赁承诺也超过8000亿美元。这些数字支撑着AI基建的持续扩张。\n\n**3️⃣ RPO（剩余履约义务）近三年涨了3倍**\n主要AI计算企业的合同负债已超过2万亿美元——客户愿意签更长期的合同，说明需求不是短期炒作。\n\n**4️⃣ 折旧将是下一个关注点**\n微软、甲骨文、Meta、谷歌四家未来三年累计折旧预计超过5200亿美元。大规模资本开支最终会转化为成本压力，除非收入端能同步跟上。\n\n**5️⃣ AI投资占全美企业资本开支半壁江山**\n预计到2026年，AI相关支出将占罗素1000指数企业资本开支的50%以上\n\n[... middle omitted ...]\n\nt, with AI-related spend expected to make up more than 50% of R1000 capex in 2026, of which hyperscalers contribute \\~90%.  \nAmong major AI compute players, RPO has nearly tripled in the last \n\n[... middle omitted ...]\n\n Analysts/Strategists nor Fixed Income Research Analysts/Strategists and are not opining on or expressing recommendations on equity or fixed income securities: Todd Castagno, CFA, CPA; Clinton Chang, CFA, CPA.\n\n© 2026 MS"
  },
  {
    "id": "R024",
    "title": "摩根斯坦利：GB200/300机柜出货量环比下降7%，但这轮调整的真正含义是供应链议价权的再分配",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：GB200/300机柜出货量环比下降7%，但这轮调整的真正含义是供应链议价权的再分配\n\n2026年5月，全球GB200/300 NVL72机柜出货量约为7700台，环比下降7%。如果只看这个数字，很容易得出“AI服务器需求见顶”的结论。但摩根斯坦利这份最新月度追踪报告传递的信号恰恰相反：**2026年全年出货量预计仍将超过7-8万台，同比增长超过100%。** 月度波动不是需求问题，而是供应链节奏问题。\n\n更重要的是，这份报告揭示了三个被市场低估的结构性变化：第一，鸿海精密（Hon Hai）的份额正在从2025年的51%下降至2026年的41%，而纬创（Wistron）和广达（Quanta）的份额相对稳定；第二，纬创的营收在5月环比增长2%，主要来自其子公司纬颖（Wiwynn）的贡献，而非传统PC业务；第三，摩根斯坦利对三家ODM的偏好排序是“纬创 > 鸿海 > 广达”，这一排序本身就在告诉市场：**在AI服务器供应链中，真正的价值创造正在从“规模”转向“议价权”。**\n\n以下是我们从这份报告中提炼出的五个关键洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 5月出货量环比下降是正常的季度节奏调整，不应被误读为需求拐点\n\n5月GB200/300机柜出货量7700台，较4月的8300台下降7%。广达从约2100台降至1800-1900台，鸿海从约3700台降至3300台，纬创则基本持平在1300-1400台。摩根斯坦利明确指出，广达的2Q整体出货量预计仍将环比增长40%至约6700台，下降的部分只是被推迟到了下半年。\n\n这意味着什么？AI服务器供应链的季度内节奏正在变得更有规律：1Q是爬坡期，2Q加速，3Q和4Q是出货高峰。2025年的数据也印证了这一模式——从1Q的900台到4Q的15500台\n\n[... middle omitted ...]\n\n感兴趣，欢迎加入，和我们一起追踪这个产业链的每一个关键信号。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nGB200机柜出货量，5月小幅回落\n\n📊 5月出货追踪\n\n**核心数据**\n5月GB200/300机柜出货约7700台，环比下降7%。某外资投行预计全年总量7-8万台，同比翻倍以上。\n\n**三大ODM表现**\n1️⃣ 鸿海：出货约3300台，环比降11%，仍是出货量最大的代工厂\n2️⃣ 广达：出货1800-1900台，略低于4月，5月营收新台币3115亿，环比降8%\n3️⃣ 纬创：出货1300-1400台，环比微增2%，5月营收新台币2900亿，环比增2%\n\n**值得注意的趋势**\n- 实际交付到终端客户的数量可能低于这些数字，因为纬创的L10计算托盘被折算为机柜等效量，未考虑L11组装和测试时间\n- 广达Q2出货预估下调至约6700台（环比增40%），但全年维持约18700台不变\n- 鸿海Q2 AI机柜出货预计达约10000台，环比增18%\n\n**投行偏好排序**\n纬创 > 鸿海 > 广达（基于目标价上行空间）\n\n整体来看，5月出货虽有小幅回落，但全年增长趋势仍然明确，Q2环比增速依然可观。\n\n#学习笔记\n\n[source_mineru.md]\nJune 8, 2026 03:55 PM GMT\n\n# Gr\n\n[... middle omitted ...]\n\nyear should remain a strong one for downstream rack assembly. We expect over 100% y/y growth in rack shipments, vs. \\~29k last year.\n\nWe believe actual rack deliveries to end-customers are lik\n\n[... middle omitted ...]\n\naxy Co Ltd (2455.TW)</td><td>E (09/11/2023)</td><td>NT$359.50</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R025",
    "title": "NOM：人民币中间价模型正在发出一个被市场忽视的稳定信号",
    "digest": "[wechat_article.md]\n# NOM：人民币中间价模型正在发出一个被市场忽视的稳定信号\n\n人民币汇率市场当前最值得关注的，或许不是每日的即期波动，而是那个看似技术性的、由模型驱动的每日中间价设定机制。NOM亚洲外汇策略团队近期发布的一份模型追踪报告，揭示了一个关键判断：**基于当前模型估算，人民币兑美元中间价的预测值已出现显著下移，这表明定价机制本身正在释放一种被市场低估的稳定性信号。**\n\n这份报告的核心价值不在于提供一个具体的点位预测，而在于它提供了一套拆解中间价形成机制的量化框架。对于关注中国资产定价逻辑的投资者而言，理解这个框架，比追逐任何单一汇率目标都更重要。\n\n我们需要回答的问题是：这个模型下移意味着什么？它背后的驱动力是什么？以及，这个信号对未来的市场博弈格局有什么含义？\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 模型预测的显著下移，正在重新定义中间价的“锚”\n\nNOM模型的最新预测显示，剔除逆周期因子后的中间价预测值为6.7775，较前次预测的6.8147大幅下移了372个基点。这是一个不容忽视的幅度。更值得注意的是，即便计入逆周期因子，模型预测值也达到6.7962，较前次调降了185个基点。\n\n这个数字本身不是预言，而是一个信号。它表明，在NOM模型的框架下，推动中间价变动的核心变量组合——主要是隔夜一篮子货币的变动——正在指向一个更低的人民币定价中枢。这意味着，如果市场条件不发生剧烈变化，官方中间价可能在未来一段时间内，以更温和的方式向这个方向靠拢。\n\n对于市场参与者而言，这相当于一个“隐性指引”。中间价设定机制本身，正在扮演一个比即期汇率更稳定的锚。投资者不应该只盯着即期市场每天几百点的波动，而应该关注这个锚的变动方向。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. \n\n[... middle omitted ...]\n\n据，持续追踪这些变量如何演变，以及它们对资产配置的深远含义。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n人民币中间价模型指向6.77\n\n🧠 中间价模型怎么看？\n\n投行研报更新了USD/CNY中间价预测模型，最新投影值指向6.7775，比上一期低了372个点。\n\n1️⃣ 逆周期因子在发力\n模型算出的原始投影是6.7775（比前次低372点），但加入逆周期因子调整后，中间价变为6.7962，实际只低了185点。这说明官方在通过逆周期因子平滑波动，不希望中间价走得太快。\n\n2️⃣ 隔夜贡献最大的货币\n模型显示，对本次投影变化贡献最大的4个货币是：\n- AUD（+15.3点）\n- KRW（+12.3点）\n- EUR（+8.0点）\n- JPY（+6.4点）\n澳元和韩元是主要推手，可能跟近期亚太市场情绪有关。\n\n3️⃣ 模型误差有规律\n历史误差图显示，模型在2025年1月误差较大（-1800点），之后逐渐收窄，2026年以来误差稳定在±600点内。说明模型近期表现更稳定了。\n\n4️⃣ 未来重要时间节点\n研报列出了2026年下半年的关键事件：\n- 7月底：政治局经济工作会议\n- 10月：国庆黄金周\n- 11月：深圳APEC峰会\n- 12月中旬：中央经济工作会议\n- 年底：可能的中美元首会晤\n这些都可能影响汇率走向。\n\n#学习\n\n[... middle omitted ...]\n\n![](images/f2f2f160cff014cff0316468b0b4b27ffa040c48474fb1edbd6d61a74bdb816b.jpg)\n\n<details>\n<summary>bar chart</summary>\n\nTop 4 weighted contribution to projected change (pips)\n| Index | Top 4\n\n[... middle omitted ...]\n\nrmation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R026",
    "title": "BARC：市场低估了供给侧的持续收紧，而非单纯押注地缘风险",
    "digest": "[wechat_article.md]\n# BARC：市场低估了供给侧的持续收紧，而非单纯押注地缘风险\n\n这份BARC研报最值得关注的核心判断，并非它预测2026年布伦特原油均价为100美元/桶——这个数字本身在市场中已有讨论——而是它揭示了一个更深层的结构性矛盾：即便假设霍尔木兹海峡在本月底恢复通行，2027年的油价仍将显著高于远期曲线和共识预期。报告给出的2027年布伦特均价预测为88美元/桶，高出远期曲线7美元/桶，高出共识13美元/桶。这意味着，BARC认为市场正在系统性地低估一个超出短期地缘冲突范畴的供给侧再定价过程。\n\n当前市场的主流叙事是“地缘溢价正在消退”。管理基金在原油期货和期权上的净投机仓位已回落至战前水平，隐含波动率也同步下降。市场似乎在告诉投资者：最坏的时刻已经过去，基本面正在消化冲击。但BARC的数据指向了一个相反的结论：基本面不仅没有消化冲击，反而在被动地“长入”最初的恐慌——库存以每天450万桶的速度下降，美国商业原油库存（经管道填充和战略储备释放调整后）已逼近2008年金融危机的低点，库欣储油设施的利用率降至2010年以来最低。\n\n这份报告的价值不在于预测一个精确的油价数字，而在于它拆解了一个关键问题：为什么市场与基本面之间出现了如此大的认知裂口？答案指向一个被广泛忽视的变量——中国需求的“战略性沉默”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 中国需求的骤降并非价格弹性，而可能是一种审慎的战略储备行为\n\n报告中最具颠覆性的观察来自中国。4月份中国石油需求同比下降12%，市场普遍将其解读为“高油价下的需求破坏”——即价格弹性发挥了作用。但BARC提出了一个截然不同的假设：这种需求下降可能并非真实的消费萎缩，而是中国在主动抑制采购、暗中储备。\n\n支持这一判断的证据来自库存数据。自伊朗战争爆发以来，中国的原油显性库存几\n\n[... middle omitted ...]\n\n更多原始图表和情景分析，拆解不同假设下的油价路径和投资含义。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n某外资投行预计2026年布伦特原油均价100美元\n\n2026年布伦特均价100美元\n\n2027年预计回落至88美元\n\n最近在投行研报里看到一组很有意思的油价预测，逻辑讲得很清楚，分享给大家一起讨论。\n\n**核心判断：**\n假设霍尔木兹海峡在本月底恢复通航，2026年布伦特均价预计为100美元/桶，2027年均价88美元/桶。这两个数字分别比当前远期曲线高出9美元和7美元。\n\n**三个关键逻辑拆解：**\n\n1️⃣ **库存持续下降，市场处于深度短缺状态**\n全球观察库存近8周以约450万桶/天的速度下降，调整后估算当前市场存在约700万桶/天的供需缺口。美国商业原油库存（剔除SPR释放和管道填充影响）自2008年以来已下降3.23亿桶，按目前速度，8-10周内可能跌破20年最低水平。\n\n2️⃣ **中国需求骤降是最大的意外变量**\n4月中国石油需求同比下降12%，1-4月整体仍增长2%。研报认为，中国可能并非因价格弹性而减少消费，而是在主动储备库存以应对封锁长期化。证据是中国的可见库存自冲突开始以来基本未变，而其他地区库存大幅下降。\n\n3️⃣ **市场情绪已回归理性，但基本面在追赶**\n投机性仓位和隐含波动率都\n\n[... middle omitted ...]\n\nb in 2026 and \\$95/b in 2027. On the other hand, if it gets pushed out to the end of August, we would expect Brent to average \\$110/b in 2026 and \\$105/b in 2027.\n\nIn late March, we thought th\n\n[... middle omitted ...]\n\nrior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request."
  },
  {
    "id": "R027",
    "title": "GS：澳大利亚消费者信心连续三个月低迷，但市场真正该关注的不是情绪本身",
    "digest": "[wechat_article.md]\n# GS：澳大利亚消费者信心连续三个月低迷，但市场真正该关注的不是情绪本身\n\n澳大利亚消费者信心指数在6月进一步下滑至80.6，较历史均值低约20%。这已经是连续第三个月处于极弱水平。GS最新研报披露了这一数据，但真正值得投资者警觉的，并非情绪本身有多差，而是情绪低迷正在从“可被忽略的噪音”转变为“可能自我实现的经济拖累”。\n\n过去两年，澳大利亚央行一直认为消费者信心与消费行为之间的关联有限。但GS在报告中引用央行的最新表述时留下了一个关键的伏笔：当情绪低迷持续足够久，且伴随资产价格下跌时，它可能开始产生实质性的二阶效应。6月的数据恰好提供了这种转变的初步证据——家庭财务状况感知全面恶化，住房价格预期三年来首次跌破长期均值，悉尼和墨尔本的跌幅尤其显著。\n\n这份报告的价值不在于告诉你“消费者不开心”，而在于它揭示了一个正在形成的反馈循环：信心疲弱正在抑制住房市场，住房市场走弱反过来进一步打击信心。这个循环是否会被打破，取决于接下来的劳动力市场走势和央行的政策路径。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 家庭财务状况感知全面恶化，这是比整体指数更危险的信号\n\n整体信心指数下降2.9%固然值得关注，但更值得细看的是分项数据。GS报告显示，家庭对当前财务状况的感知环比下降7.5%，对未来一年的财务预期更是暴跌8.5%。这两个分项同时恶化，意味着消费者不仅在抱怨当下，更在提前调低对未来的预期。\n\n这里有一个重要的结构性差异：长期经济前景预期虽然也下降了3.2%，但一年期经济预期反而回升了4.9%。这种“短期经济预期改善、家庭财务预期恶化”的分化，实际上指向了一个更具体的担忧——消费者并不认为宏观经济会崩溃，但他们认为自己的钱包正在被挤压。换句话说，这是一种“我比经济更难过”的微观体感，这种体感一旦形成，往往比宏观悲\n\n[... middle omitted ...]\n\n的原始图表和更多细节，也会定期组织对关键经济变量的跟踪讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n澳洲人连续3个月“不想花钱”\n\n消费者信心跌麻了\n\n连续3个月，澳洲人消费意愿都在历史低位徘徊\n\n---\n\n**1. 信心指数跌回冰点**\n6月澳洲消费者信心指数环比下降2.9%，报80.6，比历史均值（100.1）低约20%。这是连续第三个月处于极弱水平。不过某外资投行指出，澳联储认为信心本身对消费的独立驱动作用有限——除非信心持续大幅恶化。\n\n**2. 家庭财务感知全面转弱**\n- 对当前财务状况的看法：环比-7.5%\n- 对未来一年财务状况的看法：环比-8.5%\n- 对长期经济前景的看法：环比-3.2%\n唯一好转的是对短期经济前景的预期，从低位回升了+4.9%。\n\n**3. 房市信心也撑不住了**\n- 房价预期环比大跌14.9%，三年来首次低于长期均值\n- 悉尼和墨尔本跌幅最大（-19%和-18%），与实际房价下跌一致\n- “购房时机”指数在5月暴跌后反弹12.6%\n- 房贷利率预期也有所回落（-4.8%）\n\n**4. 一个小亮点**\n“购买大件家庭用品”的意愿小幅上升（+0.9%），但整体仍偏弱。\n\n---\n\n你觉得，澳洲人什么时候才会重新愿意花钱？\n\n#学习笔记\n\n[source_mineru.md\n\n[... middle omitted ...]\n\nr of consumption.\n\nSentiment towards the housing market remained weak. House price expectations fell $14.9\\%$ mom to below its long-run average for the first time in three years.\n\n## Main poin\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R028",
    "title": "JPM：中国出口正在成为全球金属市场结构性短缺的“泄压阀”",
    "digest": "[wechat_article.md]\n# JPM：中国出口正在成为全球金属市场结构性短缺的“泄压阀”\n\n全球基本金属市场正在经历一个罕见的错位时刻。JPM最新发布的《基本金属供需追踪报告》揭示了一个被广泛讨论但未被充分定价的格局：中国国内需求正在放缓，但中国生产商却在高价区间继续扩产；与此同时，除中国以外的市场库存正在快速消耗，而中国自身的库存却处于多年高位。这两组矛盾现象的背后，隐藏着一个关键的结构性变量——中国出口正在成为全球金属供应链的“泄压阀”。\n\n这份报告的核心判断并不复杂，但其对资产定价和产业策略的影响远未被市场完全消化。中国不是全球需求的“发动机熄火”，而是正在从需求方转变为供给的“调节器”。理解这一角色转换，是理解未来12个月基本金属价格走势的前提。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 中国铜消费的真实图景远比表面数字复杂，终端需求放缓与表观消费高企的背离蕴含关键信号\n\nJPM的数据显示了一个令人困惑的现象：2026年4月，中国的铜表观消费同比增长了9%，但该机构自建的终端消费加权指标却同比下降了4%。即便将年初至今的数据拉平，终端需求也仅微增1.2%。这种背离并非统计噪声，而是反映了供应链行为的深刻变化。\n\n表观消费的高企主要来自两个因素。其一，2025年四季度至2026年一季度中国买家“罢工”期间积累的库存正在被消化，去库存行为在4月集中体现为表观消费的虚高。其二，电网投资和新能源汽车生产仍在支撑部分需求，但这不足以抵消可再生能源装机骤降和白电产量下滑带来的拖累。报告特别指出，4月太阳能装机同比暴跌79%，风力装机下降7%，白色家电中的空调产量同比下滑9%。\n\n这意味着什么？中国铜的真实需求并没有价格所反映的那么强劲。当前铜价在每吨13500至14000美元区间震荡，很大程度上是库存再分配和供给端故事在驱动，而非终端消费\n\n[... middle omitted ...]\n\n持续追踪这些变量的边际变化，并分享对资产定价含义的实时更新。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国铜铝需求，正在悄悄分化\n\n铜铝需求，冰火两重天\n\n中国新能源和白色家电放缓，铜的真实需求在降温\n\n1️⃣ **铜：表观消费 vs 实际需求，差距拉大**\n- 4月中国铜表观消费同比+9%，看似强劲\n- 但剔除库存变动后，实际终端消费同比-4%！\n- 拖累来自：光伏安装暴跌79%、白色家电产量下滑\n- 支撑来自：电网投资+30%、新能源车产量+4%\n- 库存去化动力正在减弱，铜价在$13,500-14,000区间徘徊\n\n2️⃣ **铝：中国出口成了全球的“减压阀”**\n- LME铝库存降至33万吨，但中国库存还有140万吨\n- 中国半成品出口套利窗口打开，出口加速\n- 4月中国原铝产量同比+3.4%，年化4500万吨\n- 关键风险：几内亚铝土矿占中国进口75%，一旦中断影响大\n\n3️⃣ **锌：矿端收紧，冶炼还在硬撑**\n- 4月锌精矿进口同比-10%，加工费已转负\n- 冶炼产量却仍+5%，靠消耗库存撑着\n- 需求疲软：镀锌开工率低于5年均值，表观需求-12%\n\n4️⃣ **镍：库存增速放缓，政策压力增大**\n- 全球镍库存约47万吨，印尼政策框架抑制利润\n- 矿石基准价走高，可能压制产量\n\n新能源车全球销\n\n[... middle omitted ...]\n\nble in April (+9% yoy), with inventory draws boosting overall figures reflecting the level of inventory destock across the supply chain over the 4Q25/1Q26 buyers strike in China. More recently\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 08 Jun 2026 04:46 PM BST\n\nDisseminated 08 Jun 2026 04:46 PM BST"
  },
  {
    "id": "R029",
    "title": "JPM：美国军工复合体的真正危机不在于预算，而在于工业基础的结构性过时",
    "digest": "[wechat_article.md]\n# JPM：美国军工复合体的真正危机不在于预算，而在于工业基础的结构性过时\n\n美国仍然是全球最强大的军事力量。但JPM一份最新发布的深度研报提出了一个让产业决策者无法回避的问题：支撑这种力量的工业基础，是否已经跟不上它所面对的战争形态？\n\n这份报告的核心判断是：美国国防工业基础（DIB）当前面临的挑战，不是钱不够，而是结构不对。过去三十年的整合与集中化，让美国军工体系走向了“精致但脆弱”的路径——以F-35为代表的高端旗舰平台在技术上无可匹敌，但开发周期长、成本高昂、难以规模化。而今天的战场，从乌克兰到中东，再到潜在的台海冲突，正在同时要求三样东西：可消耗的硬件、可迭代的软件、以及能够快速整合两者的工业能力。\n\n这不是一份关于预算拨款的报告。这是一份关于工业逻辑如何被战争形态倒逼重写的分析框架。对于关注军工产业链、国防科技创业、以及中美竞争格局的读者，这份报告的参考价值不仅在于它梳理了历史，更在于它提出了一个尚未被市场充分定价的命题：美国军工股的估值逻辑，可能正站在一个结构性拐点上。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 冷战后的“旗舰崇拜”让美国军工体系失去了规模弹性\n\nJPM研报追溯了美国DIB的演变轨迹，其核心叙事线非常清晰：从二战时期的全民动员，到冷战时期的专业化与垂直整合，再到冷战结束后的剧烈整合，每一次转变都在提升技术深度，但也在牺牲生产弹性。\n\n二战期间，美国动员了超过80万家民用企业参与国防生产，飞机年产量从1939年的约6000架飙升至1944年的约23.7万架。那是一个“规模即优势”的时代。冷战时期，面对苏联的明确威胁，美国转向了专业化承包商体系，技术深度大幅提升，但供应商基础开始收窄。1993年，时任副国防部长威廉·佩里召集了著名的“最后的晚餐”会议，敦促军工企业合并。到2000年，\n\n[... middle omitted ...]\n\n解问题的后续分析。期待与你一起，把这组问题的答案拼得更完整。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美军工业基础，正在打一场硬仗\n\n🔧 一场硬仗\n\n全球冲突数量近20年增了52%，军费也水涨船高——2024年全球军事支出达2.7万亿美元，比2010年涨了34%。美国一家就占了全球36%。\n\n但问题在于：美国的国防工业基础（DIB）越来越“瘦”——集中在少数大型承包商手里，主打昂贵、高性能的“旗舰平台”（比如F-35）。冷战结束后，预算收紧，行业大合并，主承包商从50多家缩到5家，控制着60%以上的合同额。\n\n结果呢？四个漏洞：\n\n1️⃣ 供应链太浅——二级三级供应商减少，成了瓶颈，一卡就停。\n\n2️⃣ 采购太慢——重大武器项目动辄8年起步，等造出来技术可能都过时了。\n\n3️⃣ 行业太集中——巨头垄断，创新慢，替代产能难建。\n\n4️⃣ 供应链太脆弱——关键材料和元器件依赖全球，尤其对中国依赖度高。\n\n现在对手也变了：既有中俄这样的近等竞争者，也有拿着低成本精确武器的中等国家，还有用商业技术搞事的非国家行为体。中国搞“军民融合”，把商业和国防深度绑定，造船和导弹产能远超美国。\n\n乌克兰和伊朗的战争暴露了一个关键：低成本、可消耗的系统（比如无人机）和实时软件、数据整合，正在改变战场规则。不是要用软件取代硬件，而是\n\n[... middle omitted ...]\n\nifficult to scale.  \n- Over the past two decades, the threat landscape has diversified, spanning near-peer competitors, mid-tier states armed with low-cost precision weapons, and non-state act\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 08 Jun 2026 01:41 PM EDT\n\nDisseminated 08 Jun 2026 02:48 PM EDT"
  },
  {
    "id": "R030",
    "title": "摩根斯坦利：中国尿素出口底价的重新设定，是全球化肥定价逻辑的一次结构性重置",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：中国尿素出口底价的重新设定，是全球化肥定价逻辑的一次结构性重置\n\n全球化肥市场正在经历一个被多数投资者低估的定价机制转变。摩根斯坦利最新发布的这份报告揭示了一个关键信号：中国刚刚重新设定了尿素出口价格下限——对印度出口的大颗粒尿素不低于每吨500美元FOB，车用级不低于每吨510美元FOB。这一数字本身并不令人震惊，真正值得关注的是它背后的逻辑：中国正在用价格工具替代配额工具，从“限制出口数量”转向“锁定出口价格”。\n\n这意味着什么？意味着全球尿素市场的价格锚点正在被重新定义。过去几年，市场习惯了用中国出口配额作为供给侧的调节器，但这份报告暗示，配额逻辑正在被价格逻辑取代。而这一转变的背景，是霍尔木兹海峡持续关闭、伊朗供给中断、以及沙特SABIC正在加速的产能转移。\n\n这不是一个短期事件。它可能重塑未来12-18个月全球化肥贸易的竞争格局。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 价格下限不是简单的限价，而是中国化肥出口政策的范式转换\n\n摩根斯坦利的分析显示，中国此次设定的价格下限与此前每吨660-680美元FOB的初始水平相比，已经显著下调。但更关键的是政策工具本身的变化。\n\n过去几年，中国对尿素及DAP/MAP出口采取的是“配额+窗口期”管理。出口商需要在有限的配额内竞争，结果往往是价格被压低，利润被压缩。而现在，价格下限的引入意味着：只要出口价格不低于底线，出口商可以自由交易。这本质上是一种从“量控”到“价控”的转变。\n\n报告提到，低于下限出口的出口商可能失去“自律性企业”资格。这不是一个软性约束，而是一个有实际惩罚机制的硬性门槛。对于中国化肥企业而言，这意味着它们的出口策略必须从“抢配额、拼价格”转向“保价格、赚利润”。\n\n这个转变的含义是：中国不再追求全球市场份额的最大化，而是追求\n\n[... middle omitted ...]\n\n于这份报告的完整数据，持续更新对全球化肥市场供需格局的判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国尿素出口设限，全球化肥市场变局\n\n中国收紧尿素出口\n\n最近中国重新设定了尿素出口价格下限，大颗粒不低于500美元/吨FOB，车用级不低于510美元/吨FOB。其他目的地的出口价格可以“适当降低”，但具体水平仍在讨论中。\n\n这波操作背后有原因。最新印度招标约170万吨，报价低至410美元/吨CFR，换算成中国出口FOB价不到400美元。按新规，中国大概率不会参与这次印度招标了。\n\n全球市场已经感受到波动。美国Nola价格跌到360-410美元/吨，巴西跌了55美元到530-540美元/吨CFR，伊朗更是暴跌100美元到620-630美元/吨FOB。\n\n1/ 中国为何此时出手？\n研报指出，近年来中国对尿素和磷铵出口一直很谨慎，主要考虑到地缘冲突导致的供应中断风险（先是俄乌，现在是伊朗）。这导致国内供应过剩，农民享受低价，但化肥企业利润承压。价格下限能在控制出口量的同时，最大化企业现金流，同时战略性地保持国内高库存。\n\n2/ 霍尔木兹海峡是关键变量\n市场一直担心中国会在海峡重新开放前收紧尿素出口。现在价格下限虽已设定，但海峡依然关闭。研报推测，这可能是中国在应对全球供应链不确定性。\n\n3/ 后续关注什么？\nSA\n\n[... middle omitted ...]\n\nmes as the latest India tender for \\~1.7mm mt reportedly saw offers as low as \\$410s/t CFR which would net back to below \\$400/t FOB for Chinese exporters. Given the now \\$500 mt floor, the si\n\n[... middle omitted ...]\n\nd>Westlake Corp (WLK.N)</td><td>E (01/09/2018)</td><td>$85.26</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R031",
    "title": "摩根斯坦利：中国取消尿素出口底价，全球化肥市场的定价权正发生结构性转移",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：中国取消尿素出口底价，全球化肥市场的定价权正发生结构性转移\n\n中国在5月27日刚为尿素出口设置了价格底线，不到两周就悄然撤除。这个动作本身并不意外，因为全球尿素价格已经跌到远低于中国设定的每吨660-680美元FOB水平，继续维持底价在商业上没有意义。但摩根斯坦利这份报告真正值得关注的判断，不在于“中国调整了政策”，而在于这个调整透露了中国化肥出口战略的深层逻辑转变——中国正在从“保国内供应、限出口”的防御姿态，转向“在保障国内低价的同时，最大化出口现金流”的平衡策略。这一转变的隐含含义，可能被全球农产品和化肥市场严重低估。\n\n报告的核心洞察只有一个：中国化肥出口政策不再是简单的开关式管控，而是进入了精细化、选择性、与地缘风险高度耦合的新阶段。对于全球氮肥和磷肥市场而言，这意味着中国不再只是一个被动的价格接受者，而是正在成为供给侧的主动定价变量。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 价格底线的取消，暴露了中国出口策略的真正优先级\n\n市场此前对中国设置尿素出口底价存在两种解读。一种认为这是中国在限制出口总量的同时，为国内生产商争取更高利润；另一种则认为这是中国在地缘不确定性下，战略性保留国内库存的手段。摩根斯坦利通过“底价取消”这个逆向验证，给出了清晰的判断：中国优先级的核心不是利润最大化，而是出口量的释放。\n\n底价设置的初衷，是在3百万吨出口配额内，确保中国生产商不会因低价亏损而减少出口。但当全球价格跌至底价以下后，中国没有选择“等价格反弹再出口”，而是直接取消底价，允许出口在更低价格水平上继续。这个选择说明，对中国而言，维持出口通道的畅通、消化国内过剩产能，比短期价格谈判权更重要。\n\n这一判断对中国化肥行业的竞争格局有直接含义。如果中国愿意在低于全球成本曲线的价格水平上出口，那么全球尿\n\n[... middle omitted ...]\n\n肥出口的动态，并分享摩根斯坦利完整报告的原始数据和图表分析。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国尿素出口价格底限取消\n\n出口变局\n\n中国取消尿素出口底价，全球化肥市场怎么看？\n\n上周五，某外资投行发布研报指出，中国已取消5月27日设立的尿素出口价格底限。原底价为：颗粒尿素FOB 670美元/吨，印度出口额外要求680美元/吨。这个动作比预期要快。\n\n1️⃣ 为什么取消？\n全球尿素价格早已跌破中国设定的底价，继续保留底价已无实际意义。如果坚持不放，反而说明中国可能想通过“限量+高价”策略最大化出口利润。现在取消，说明中国的目标更偏向于保障国内供应稳定。\n\n2️⃣ 对国内市场的影响\n过去几年，中国在尿素和磷肥出口上一直很谨慎——地缘冲突（俄乌、伊朗）导致全球供应紧张，中国选择优先保国内农民，造成国内化肥供给过剩、价格极低。这虽然利好农民，但化肥企业利润承压。取消底价，意味着出口量可能增加，对国内化肥企业是正面信号。\n\n3️⃣ 后续关键看什么？\n研报认为，下一个重要节点是8月中国MAP/DAP（磷肥）出口是否恢复。目前硫磺市场持续紊乱（不只是霍尔木兹海峡问题，俄罗斯最近也在减少出口），8月能否恢复出口“更难判断”，取决于硫磺供给和成本能否改善。\n\n4️⃣ 还有一个细节\n印度最近一轮尿素招标即将截止，目前还\n\n[... middle omitted ...]\n\nand DAP/MAP exports in recent years given potential (and now real) supply disruptions from various geopolitical conflicts (first Russia/Ukraine and now Iran). This has created local oversupply\n\n[... middle omitted ...]\n\nd>Westlake Corp (WLK.N)</td><td>E (01/09/2018)</td><td>$84.64</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R032",
    "title": "BARC：企业级服务器的意外走强，正在改写服务器市场的增长叙事",
    "digest": "[wechat_article.md]\n# BARC：企业级服务器的意外走强，正在改写服务器市场的增长叙事\n\n市场对AI服务器的关注从未减弱，但真正让这份BARC研报值得反复阅读的，不是它确认了超大规模云厂商的资本开支仍在攀升，而是它在企业级服务器这个被普遍认为“平稳甚至萎缩”的细分市场，捕捉到了一个出乎意料的信号。\n\n在最近的财报季中，多家服务器厂商的企业级业务表现显著超出预期。BARC团队在更新其服务器模型后，给出了一个值得产业决策者和投资者深思的判断：企业级服务器收入的增长，并非仅仅来自价格驱动的短期波动，其背后正在浮现由代理式AI和推理需求催生的结构性机会。当然，这并不意味着企业级市场将迎来长期繁荣，但至少在未来一年内，它正在改写整个服务器市场的增长曲线。\n\n这份报告的核心价值不在于提供了多精确的数字，而在于它揭示了一个正在发生的结构性转变：当所有人都盯着云端的千亿级资本开支时，企业端的采购逻辑和需求形态正在悄然变化。理解这个变化，比记住任何营收预测都更重要。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 云服务器的高增长已是明牌，真正的增量来自企业级市场的“意外跃升”\n\nBARC的模型调整，最引人注目的部分并非云服务器。云端的增长逻辑非常清晰：超大规模云厂商的资本开支预期已从2025年的约4230亿美元跃升至2026年的超过7000亿美元。BARC据此将云服务器的五年复合年增长率预期从约59%上调至约62%。这是一个巨大的数字，但市场对此已有充分预期，甚至已经部分定价。\n\n真正的意外发生在企业级服务器市场。BARC此前预计企业级服务器收入在2026年仅有约2%的增长，但在最新的财报季中，戴尔、慧与等OEM厂商的数据彻底颠覆了这一判断。戴尔预计其传统服务器业务在本财年将增长超过60%，慧与则报告传统服务器订单实现了三位数增长。BARC因此将20\n\n[... middle omitted ...]\n\nAI如何改变企业IT采购逻辑有自己的观察，也欢迎在群里分享。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n服务器市场，超预期的不止AI\n\n企业服务器逆袭\n\n某外资投行最新服务器模型更新。几个核心变化值得记下来：\n\n1️⃣ 企业服务器意外爆发\n- 今年企业服务器收入预计增长33%（之前预期只有2%）\n- 主要驱动力：ASP大幅上涨 + 客户采购量好于预期\n- 戴尔传统服务器FY增长超60%，HPE订单同比增长三位数\n- 但注意：明年可能只剩1%增长，涨价会抑制需求\n\n2️⃣ AI服务器依然强劲\n- 云服务器5年CAGR从59%上调至62%\n- 超大规模云厂商资本支出：CY26预计超7000亿美元（CY25约4230亿）\n- 戴尔AI服务器收入Q/Q增长80%，积压订单513亿美元\n- GPU服务器占2026年服务器份额71%\n\n3️⃣ 关键结构性变化\n- 白牌（含英伟达）持续抢占品牌厂商份额\n- 企业级市场：代理AI和推理成为传统服务器新需求\n- 但企业服务器增长不可持续，2027年预计仅1%\n\n4️⃣ 值得关注的信号\n- 超大规模厂商资本支出持续上调，直接转化为网络基础设施投资\n- 戴尔AI客户群已达5000家（半年增长超50%）\n- SMCI因客户准备问题收入miss，但企业业务占比从15%升至28%\n\n#学习\n\n[... middle omitted ...]\n\nlusive of AI) and Enterprise servers vs previously where we used AI vs Traditional.\n\nOur Cloud estimates move higher, in line with major hyperscalers' lifted capex expectations, and we now est\n\n[... middle omitted ...]\n\nrior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request."
  },
  {
    "id": "R033",
    "title": "Citi：市场低估的不是新能源渗透率，而是出口定价权的结构性重构",
    "digest": "[wechat_article.md]\n# Citi：市场低估的不是新能源渗透率，而是出口定价权的结构性重构\n\n这份Citi于2026年6月8日发布的CPCA 5月销量追踪报告，表面上是每月一次的数据更新，但若只看到“5月新能源乘用车批发135万辆，同比+10.6%”这个数字，就错过了报告真正有价值的信息。\n\n真正值得关注的判断是：**中国汽车产业正在经历从“国内渗透率竞赛”到“全球定价权争夺”的转折点。** 5月的数据揭示了一个结构性信号——新能源出口占比首次突破54%，而国内零售端却出现了新能源销量同比下滑7.5%的反直觉现象。这两个方向同时发生，意味着市场惯用的“渗透率单边上升”叙事已经不足以解释当下的产业逻辑。\n\nCiti这份报告提供的不是乐观或悲观的情绪，而是一个需要重新校准的观察框架。以下是我们从数据中提炼出的四个核心洞察，以及一个报告尚未完全回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 新能源批发与零售的背离，暴露了渠道库存的深层博弈\n\n5月新能源乘用车批发135万辆，同比+10.6%，但零售仅95万辆，同比-7.5%。批发与零售之间40万辆的差距，远超正常季节波动。Citi估算5月整个乘用车行业去库存约8.2万辆，而新能源板块的批发-零售差值意味着，新能源渠道库存仍在累积而非消化。\n\n这背后不单是需求疲软，更可能是车企在国七排放标准切换预期下的主动铺货行为。传统燃油车批发同比下滑21%，零售更是暴跌39%，说明经销商对燃油车库存极度谨慎。而新能源批发保持正增长，更多是车企为抢占下半年市场份额而提前铺货——这是一种“以库存换份额”的策略性博弈。\n\n对于投资者而言，批发数据的高增长需要打折扣。真正应该关注的不是月度批发量的绝对值，而是零售端能否在未来2-3个月内跟上批发节奏。如果零售持续落后，下半年价格战的烈度可能超出预期\n\n[... middle omitted ...]\n\n数据、渠道库存测算方法，以及我们对下半年行业拐点的预判框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月中国车市：出口猛涨，库存加速去化\n\n出口强，新能源稳\n\n**5月出口再创新高，新能源渗透率突破六成**\n\n刚看完某外资投行最新研报，5月车市数据出来了，几个关键点值得关注：\n\n1️⃣ **出口继续狂飙**\n5月乘用车出口78.4万辆，同比+75.1%\n其中新能源出口42.4万辆，同比翻倍+112.6%\n前5个月累计出口338万辆，同比+69%\n\n2️⃣ **新能源批发符合预期**\n5月新能源乘用车批发135万辆，同比+10.6%\n纯电（BEV）88.6万辆，同比+16.6%\n插混（PHEV）37.2万辆，同比+10.5%\n增程（EREV）9.5万辆，同比-24.9%\n\n3️⃣ **新能源渗透率创新高**\n批发渗透率61.1%，同比+8个百分点\n零售渗透率62.9%，同比+9.9个百分点\n\n4️⃣ **库存加速消化**\n5月乘用车行业去库存约8.2万辆\n前5个月累计去库存35万辆（去年同期是补库存1万辆）\n\n5️⃣ **特斯拉表现**\n5月国内批发85,982辆（Model Y 54,765，Model 3 31,217）\n国内零售约4.73万辆，环比大增80%\n\n6️⃣ **燃油车继续承压**\n5月燃油车\n\n[... middle omitted ...]\n\nPCA estimates PV sector inventory destocking at around 82k units in May-26, with 5M26 sector destocking of 350k units (vs restocking of 10k units in 5M25). Further reading: China Auto Manufact\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R034",
    "title": "JPM：市场误读了SOCAMM降配，真正的机会藏在供给硬约束和NVIDIA的生态锁定里",
    "digest": "[wechat_article.md]\n# JPM：市场误读了SOCAMM降配，真正的机会藏在供给硬约束和NVIDIA的生态锁定里\n\n过去一周，全球存储器板块经历了一次幅度约11%的急跌，同期费城半导体指数仅下跌6%。触发因素是一则看似利空的消息：NVIDIA下一代Vera Rubin超级计算系统的CPU内存模组SOCAMM，单颗CPU配置可能从192GB降至96GB。市场的第一反应是“CPU驱动的高阶内存需求逻辑被削弱了”，随即抛售了三星电子、SK海力士等头部厂商的股票。\n\n但JPM在最新发布的这份研报中，提出了一个与市场情绪截然相反的判断。这份报告的核心主张是：**SOCAMM降配并非需求疲软的信号，而是供应极度紧张的副产品。更关键的是，NVIDIA与SK海力士刚刚签署的多年技术合作协议，以及Computex 2026上浮现的AI存储架构变革，正在将存储器产业从“周期博弈”推入“结构锁定”的新阶段。**\n\n对于关注AI基础设施投资的决策者而言，现在需要区分两类信息：一类是短期噪音，另一类是正在重塑行业竞争格局的长期变量。SOCAMM降配属于前者，而NVIDIA的生态圈层化、eSSD在AGI架构中的基础设施化，以及HBM4向HBM4E的加速迭代，都属于后者。JPM认为，过去一周的调整恰恰提供了一个“买入回调”的窗口。\n\n以下是我们从这份研报中提炼出的四个核心洞察和一个尚未完全解答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. SOCAMM降配不是需求萎缩，而是供应瓶颈下的被动重组\n\n市场之所以对SOCAMM从192GB降至96GB反应剧烈，是因为它触及了投资者对AI内存需求增速的核心假设。如果单颗CPU的内存容量腰斩，那么即便Vera Rubin出货量增长，整体内存比特需求也可能达不到预期。\n\n但JPM的供应链核查得出了一个相反的结论：*\n\n[... middle omitted ...]\n\n颈何时缓解”“哪些二线标的可能受益”等未解问题进行深入交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI记忆体的「抄底」时刻到了？\n\n📉 下跌11%后，机会来了\n\n上周AI记忆体板块回调11%，但某外资投行认为这是「买在下跌」的好时机。核心逻辑是：市场对SOCAMM内容下调的担忧被过度解读了。\n\n1️⃣ SOCAMM的真相\n媒体说Vera Rubin的SOCAMM从192GB降到96GB，需求要凉。但研报供应链调研显示：这更像是供应紧张导致的配置调整，而不是需求萎缩。96GB模块需求反而在涨，总采购量没变，只是内容与数量的重新搭配。\n\n2️⃣ NVDA与SK海力士的深度绑定\n两家签了2年+可延长的技术合作，SK海力士正式成为NVDA最大记忆体伙伴。合作覆盖HBM、SOCAMM、LPDDR5X等全产品线，延伸到AI基础设施、个人AI和实体AI。这对其他供应商也是利好，因为供应本来就很紧。\n\n3️⃣ Computex 2026的关键信号\n- SK海力士：12层HBM4量产顺利，HBM4E开始送样\n- Solidigm：SSD在AI数据管线中越来越重要，KV Cache卸载到NAND能提升27倍响应速度\n- Kioxia：与NVDA在RAG服务器上的软件合作是差异化优势\n\n4️⃣ 为什么说这是机会？\n记忆体需求的\n\n[... middle omitted ...]\n\n Based on our supply chain checks, we sense growing demand for the 96GB SOCAMM module, while believe that the shift in demand is predominantly due to limited memory supply rather than performa\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 09 Jun 2026 12:19 AM HKT\n\nDisseminated 09 Jun 2026 12:19 AM HKT"
  },
  {
    "id": "R035",
    "title": "JEF：市场对AI颠覆软件的恐惧过度，中国软件公司反而更具韧性",
    "digest": "[wechat_article.md]\n# JEF：市场对AI颠覆软件的恐惧过度，中国软件公司反而更具韧性\n\n这份研报的核心判断，与过去半年市场的主流叙事截然不同。当全球投资者因为Claude Cowork、GPT-5.5等AI Agent的涌现而抛售软件股时，JEF的分析团队提出了一个反直觉的结论：AI对软件行业不是“末日审判”，而是一场“自然选择”。更关键的是，中国软件公司在这场选择中，可能比美国同行拥有更强的生存韧性。\n\n这份报告发布于市场情绪最为悲观的时刻。自2025年10月以来，美国软件板块因AI颠覆SaaS的担忧大幅下跌，Anthropic在2026年1月12日发布的Claude Cowork更是将恐慌推至顶峰，导致板块在3月31日前累计下跌约23%。此后市场虽有所修复，但中国软件板块的处境更为艰难——年初至今下跌13%，远超美国软件6.4%的跌幅。然而，JEF认为，这种下跌更多源于盈利下修和估值压缩，而非AI颠覆本身。\n\n为什么中国软件公司反而可能更安全？为什么JEF将金蝶列为中国软件板块的首选？这些判断背后，是对软件行业底层商业逻辑的重新审视。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI对软件的影响是“自然选择”而非“末日”，关键在于护城河的厚度\n\nJEF将AI对软件行业的影响定义为“自然选择机制”，而非市场的普遍认知——“SaaS末日”。这一判断的核心在于，AI并不会让软件变得无关紧要，而是会重塑软件的架构和经济模型。\n\n报告指出，AI Agent能够自主执行任务，但它们仍然依赖软件的API接口来获取工作流、业务逻辑和数据。这意味着，拥有强大护城河的软件公司——那些深度嵌入客户核心业务流程、掌握专有数据、拥有严格合规资质的公司——不仅不会被颠覆，反而可能进化为AI原生平台。而那些护城河薄弱、对AI反应迟缓的公司，则面临被替代的\n\n[... middle omitted ...]\n\n底？这些问题的答案，可能就藏在完整报告的细节和后续的跟踪中。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI不是来砸SaaS饭碗的\n只是“自然选择”\n\n中国软件其实比美国扛打\n\n某外资投行刚出了份中国软件研报，核心观点很有意思：AI对软件业不是末日，是自然选择。而且中国软件公司比美国同行更抗打。\n\n为什么？\n\n1️⃣ 中美软件定价模式不同\n美国SaaS普遍按人头收费，AI代理一旦替代人工，收入直接塌方。中国软件公司大多按项目或模块收费，国企客户更爱定制化+本地部署，对AI冲击的免疫力更强。\n\n2️⃣ 中国软件这波下跌，主因不是AI\n美国软件今年跌了6.4%，纯粹是估值收缩。中国软件跌了13%，是因为盈利预期下修+估值双杀。说白了，IT预算吃紧才是真问题。\n\n3️⃣ 三类软件最不容易被AI替代\n工业软件、金融IT、ERP。原因：深度嵌入工作流、有专有数据、对幻觉零容忍、供应商准入门槛高。\n\n4️⃣ 某国产ERP龙头被看好\n研报认为最近回调反而是机会。原因：ERP是客户的核心系统，替换成本极高；模块化定价不受裁员影响；已推出自研AI原生ERP套件，2026年AI收入指引10亿；SaaS占比超50%，估值只有0.7倍PEG。\n\n整体看，AI会淘汰那些护城河浅、转型慢的公司，但也会让有壁垒的玩家进化成AI原生平台。中国\n\n[... middle omitted ...]\n\nmultiple compression. Since Oct 2025, the US software (SW) sector has sold off sharply on fears that AI will disrupt SaaS. Anthropic's release of Claude Cowork on Jan 12, 2026 intensified the \n\n[... middle omitted ...]\n\nd\\_iapd\\_Brochure.aspx?BRCHR\\_VRSN\\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://javatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.\n\n© 2026 JEF"
  },
  {
    "id": "R036",
    "title": "摩根斯坦利：市场正在用不同估值逻辑为互联网公司定价，但真正的分歧不在AI硬件与软件之间",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：市场正在用不同估值逻辑为互联网公司定价，但真正的分歧不在AI硬件与软件之间\n\n这周美国互联网板块经历了一场令人瞩目的分化。整体互联网公司下跌了5%，但跌幅分布极不均匀。亚马逊下跌了9%，Meta下跌了6%，而Pinterest却逆势上涨了7%。在同一周内，同一板块内出现如此巨大的差异，市场到底在交易什么？\n\n一个常见的叙事是：市场正在从AI硬件转向AI软件。但这个判断过于笼统，甚至可能误导决策。摩根斯坦利这份6月5日发布的研报，通过一张详尽的估值表和一组长达一周的板块表现数据，揭示了一个更精确的信号：市场不是在简单地切换板块偏好，而是在对每个公司重新评估其商业模式在AI时代下的护城河宽度。\n\n这份报告最值得关注的判断是：互联网公司的估值离散度正在急剧扩大，传统倍数框架已经无法解释股价表现。真正决定资金流向的，是企业能否将AI能力转化为可定价的竞争优势，而非仅仅作为成本节约的工具。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 电商与数字广告的估值逻辑正在分道扬镳，但原因不是市场风格切换\n\n从摩根斯坦利提供的估值表来看，数字媒体板块的2026年EV/EBITDA中位数是8.5倍，而电商/市场板块是8.7倍，两者几乎相同。但过去一周的表现却天差地别：电商板块市值加权平均下跌了8.9%，而数字广告板块仅下跌3.8%。\n\n这不是市场在简单地“卖出电商、买入广告”。如果看个股，Pinterest上涨了7%，而同样属于数字广告的Meta却下跌了6%。如果是板块轮动，不应该出现同一个子板块内部如此大的分化。\n\n真正的解释在于：市场正在对每个公司独立评估其AI投资的回报周期。那些AI投入尚未转化为可见收入增长的公司，即使属于热门赛道，也被重新定价。而那些能够讲清楚AI如何直接驱动广告变现效率提升的公司，即使规模较\n\n[... middle omitted ...]\n\n会定期分享对关键报告的深度解读，以及基于这些框架的实战跟踪。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n# 北美互联网板块：AI硬件与软件的资金流向博弈\n\n**封面：** 互联网板块降温\n\n**副标题：** 一周跌幅背后的逻辑\n\n---\n\n上周北美互联网板块整体回调，标普和纳斯达克分别跌3%和5%，而互联网板块整体跌了5%。几个大票的跌幅尤为明显：AMZN跌9%，META跌6%，GOOGL跌3%。💻\n\n**1. 估值怎么看？**\n\n按2026年预期盈利算，AMZN目前25倍PE，GOOGL 25倍，META 18倍。对比过去12个月的平均估值，AMZN低了19%，GOOGL低了2%，META低了27%。\n\n换句话说，市场在给这些公司重新定价，尤其对META的盈利预期压得比较低。\n\n**2. 板块分化明显**\n\n数字广告板块加权平均跌3.8%，电商板块跌得更惨，接近9%。但有意思的是，旅行和共享经济板块基本持平，只跌了0.3%和0.1%。\n\nPINS反而是这周少数涨了7%的标的，说明市场不是无差别抛售，而是在挑方向。\n\n**3. 资金在往哪流？**\n\n从一周表现看，电商板块资金流出最明显，而旅行、共享经济相对抗跌。这背后可能是市场在重新评估不同细分领域的增长确定性。\n\nAI硬件vs软件的讨论还在继续，但短期内，市\n\n[... middle omitted ...]\n\nffce460f1504f98e94.jpg)\n\n<details>\n<summary>text_image</summary>\n\nMS | RESEARCH\n2026 EXTEL\nALL-AMERICA\nRESEARCH POLL\nVIEW OUR\nANALYSTS >\nMay 26 - June 12 2026\nWe appreciate your support\nVOTE H\n\n[... middle omitted ...]\n\nnternational Inc (WW.O)</td><td>E (08/01/2025)</td><td>$17.19</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R037",
    "title": "NOM：2万亿投资计划不仅是短期催化剂，更是中国AI供应链国产化进程的加速器",
    "digest": "[wechat_article.md]\n# NOM：2万亿投资计划不仅是短期催化剂，更是中国AI供应链国产化进程的加速器\n\n市场对于中国AI领域的投资预期，往往停留在“政策刺激”的短期逻辑上。但NOM最新的一份报告揭示了一个更深层的信号：中国正在以国家意志，系统性地构建一个自主可控的AI基础设施体系。这份报告的核心判断并非简单的“政府要花钱了”，而是“这笔钱将如何重塑中国AI供应链的竞争格局”。\n\n这份报告发布于2026年6月9日，针对的是当日彭博社报道的中国计划在未来五年内投资约2950亿美元（约合人民币2万亿元）建设全国数据中心网络的消息。NOM的分析师团队迅速给出了他们的专业解读：这并非一个全新的消息，但它的意义在于确认了政府长期、坚定的决心，并指明了最直接的受益方向。\n\n为什么这个判断值得决策者高度关注？因为它回答了一个核心问题：在先进AI芯片获取受限的背景下，中国AI产业的增长路径在哪里？NOM的答案是，路径不再单纯依赖算力的绝对领先，而是转向了基础设施的网络化、国产化，以及将规模优势转化为议价权。\n\n![研报原图 1](assets/xhs_card_01.png)\n\n## 1. 2万亿投资的核心不是“花钱”，而是“建网”，这改变了AI产业的竞争维度\n\nNOM报告的核心洞察在于，它没有将这笔投资仅仅视为一次性的财政刺激，而是将其解读为一次基础设施的“网络化”重构。根据报告，中国发改委等关键部门正在起草一份蓝图，旨在建设一个全国性的互联计算枢纽网络。这意味着，投资的重点并非简单地建设一个个孤立的数据中心，而是要将它们连接成一个高效、协同的“算力网”。\n\n这种“建网”逻辑，与过去几年中国在特高压、5G等领域的思路一脉相承。其战略意图非常清晰：通过国家主导的顶层设计，解决算力资源分布不均、利用率低下的问题。对于产业而言，这意味着未来的竞争将从“谁拥有更多算力”转向“谁能更高效地调度和利用网络\n\n[... middle omitted ...]\n\n代各环节的真实进度”这两个核心议题，进行更深度的拆解和跟踪。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国砸2万亿建数据中心，AI产业链要起飞？\n\n2万亿AI基建计划\n\n未来5年，全国算力网络大布局\n\n---\n\n最近Bloomberg报道，中国计划未来五年投入约2万亿人民币，在全国铺开数据中心建设。如果算上配套电力网络等，总投入可能到5万亿。\n\n这不是全新消息，1月就有类似讨论。但某外资投行认为，这仍会是国内AI供应链的短期催化剂。\n\n🔍 关键信息：\n- 发改委等部门正在起草全国算力枢纽互联蓝图\n- 中国移动、中国电信等国企将主导数据中心运营与连接\n- 核心技术上，会依赖华为等本土供应商，尤其在AI芯片领域\n\n🎯 谁最受益？\n1️⃣ AI计算/服务器：紫光股份等\n2️⃣ AI网络：光模块/组件/交换机/光纤，如长飞光纤\n3️⃣ IDC/云：中国移动、中国电信、万国数据、世纪互联\n\n⚠️ 需要留意的风险：\n- 先进AI芯片产能仍受限\n- 企业端和应用市场可能竞争加剧，影响变现节奏\n\n你怎么看这轮AI基建的投资逻辑？欢迎一起讨论。\n\n#学习笔记\n\n[source_mineru.md]\n## Reports on China ramping up AI investment...\n\nGlobal Markets R\n\n[... middle omitted ...]\n\nmmission (NDRC), are drafting a blueprint to erect a network of inter-connected computing hubs across the country; state firms such as China Mobile (941 HK, Buy) and China Telecom (728 HK, Neu\n\n[... middle omitted ...]\n\nable upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R038",
    "title": "Bernstein：存储行业的结构性重定价远未完成，真正的机会在NAND和HDD的后半场",
    "digest": "[wechat_article.md]\n# Bernstein：存储行业的结构性重定价远未完成，真正的机会在NAND和HDD的后半场\n\n当一家公司股价在12个月内上涨近4000%，绝大多数投资者的第一反应是“太贵了”。但Bernstein在最近的第42届战略决策会议上，恰恰把这家公司——SanDisk——作为短期首选推荐。这不是追高，而是基于一个从2013年就开始论证、至今仍在展开的结构性判断：存储行业正在经历一次“新范式”的重定价，而市场目前只定价了前半段。\n\n这份研报的核心主张是：AI正在驱动存储行业有史以来最大规模的需求浪潮，但市场对供给侧的长期结构性约束仍然定价不足。DRAM已经验证了“新范式”的逻辑，NAND正在复制它，而HDD则出现了历史上第一次“既集中又增长”的格局。这三个细分市场合在一起，意味着存储行业的周期性正在被系统性削弱，盈利中枢正在上移。\n\n以下是我们从这份研报中提炼出的五个关键层次。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI对存储的需求不是一条直线，而是一个逐级放大的阶梯\n\n大多数投资者对AI存储需求的理解停留在HBM和DRAM上。这是对的，但不够。Bernstein将AI工作负载分为四个阶段：训练、基础推理、高级推理（长上下文、RAG、推理）、以及最终Agentic AI。每个阶段对存储的需求类型和强度都不同。\n\n训练阶段对HBM的需求是“极端的”，对NAND和HDD的需求是“高的”。但到了Agentic AI阶段，HBM的需求回落至“高”，而常规DRAM、NAND和HDD的需求全部升至“极端”或“高”。这意味着，随着AI从“生成答案”进化到“执行任务”，存储需求的重心正在从最顶层的SRAM/HBM向下迁移到NAND和HDD。\n\n这个判断的含义很直接：如果市场对存储的定价主要基于HBM和DRAM的紧缺程度，那么当N\n\n[... middle omitted ...]\n\n论哪些变量最可能成为未来6-12个月的关键转折点。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI引爆存储芯片新周期\n\n存储芯片，正在经历一场结构性变革\n\n投行研报认为，AI正在驱动一场前所未有的存储需求浪潮。从训练到推理，再到Agentic AI，每个阶段对存储的需求都在升级。HBM和DRAM是早期受益者，但NAND和HDD也正在迎来机会。\n\n1/ 数据中心客户占据主导地位\n如今，数据中心客户在DRAM、NAND和HDD的需求占比已远超传统客户。更重要的是，这些超大规模客户对价格敏感度更低，支撑了比以往周期更强的定价能力。\n\n2/ “新存储范式”卷土重来\n2013-2014年，该行曾提出“新存储范式”理论：技术迁移带来的供应增长放缓，行业整合加剧，导致上升周期更强、下降周期更温和。这一逻辑在DRAM上已充分验证，NAND因3D NAND过渡延迟了验证，但如今也开始显现类似趋势。\n\n3/ HDD迎来历史性转折\n这是HDD行业首次同时实现“整合+增长”。自2012年整合后，HDD一度被NAND蚕食，如今这种压力基本消失。剩下的业务关键型存储市场，是NAND无法替代的。\n\n4/ 长协条款越来越友好\n供应商在定价、预付款和照付不议条款上获得更多保障，进一步降低了周期波动。\n\n研报显示，某外资投行认为NAND\n\n[... middle omitted ...]\n\necisions Conference, we pitched Memory and Storage as our best idea, where we brushed off our New Memory Paradigm thesis from a decade ago and addressed where we got things right and wrong and\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R039",
    "title": "Citi：特高压订单翻倍背后的关键信号——电网设备竞争已从“订单量”转向“议价权”",
    "digest": "[wechat_article.md]\n# Citi：特高压订单翻倍背后的关键信号——电网设备竞争已从“订单量”转向“议价权”\n\n国家电网2026年第二批特高压设备招标结果出炉，总金额94亿元，是第一批的两倍有余，已接近2025年全年五批招标总额的43%。这份来自Citi研报的数据，在多数市场参与者还在关注“谁拿到了最大份额”时，揭示了一个更值得追问的结构性变化：随着招标量放大、铜价上行、交付节奏加快，这一轮电网投资的真正赢家，可能不是订单最多的企业，而是能在规模扩张中守住甚至提升毛利率的企业。\n\n换句话说，市场对特高压板块的定价逻辑，正在从“订单驱动”切换为“盈利质量驱动”。Citi在这份研报中，通过平高、思源、特变电工三家公司的订单结构、产品交付细节和估值对比，提供了这一判断的支撑证据。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 招标金额翻倍不是线性增长，而是电网投资节奏的质变信号\n\n2026年第二批特高压设备招标94亿元，放在历史坐标中看，意义远超数字本身。2025年全年五批合计221亿元，而2026年仅前两批就已达到184亿元。如果加上3月31日第一批的约50亿元（Citi在研报中标注了第一批为98.34亿元，但此处以正文数据为准），2026年上半年累计招标已接近去年全年。\n\n更关键的是节奏的变化。2025年的招标集中在第四批（165亿元），呈现出“前低后高、年底集中”的特征。而2026年第二批就达到94亿元，且Citi明确指出，平高预计2026年还将有至少2个新的交流特高压项目获批，叠加2025年已获批但尚未招标的3个交流项目（达拉特-蒙西、攀枝花-西昌、浙江环网），后续招标量仍有支撑。\n\n这意味着，电网投资不再是一次性的“脉冲式”放量，而是进入了持续高强度的建设周期。Citi在研报中援引的数据也佐证了这一点：2026年一季度全国电网资本\n\n[... middle omitted ...]\n\n研报原文、估值表格和后续跟踪框架。期待在群里与大家深入交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n特高压订单翻倍，谁在拿大单？\n\n国家电网第二批招标结果出炉\n\n投行研报拆解了国网2026年第二批特高压设备招标结果，总金额94亿，是第一批的2倍多，占去年全年5批总额的42.6%。这个量级，值得仔细看。\n\n1️⃣ 谁拿单最多？\n- 平高电气：20.92亿，占22.3%，排第一\n- 中国西电：18.99亿，占20.2%\n- 特变电工：4.73亿，占5.0%\n- 思源电气：1.96亿，占2.1%\n- 国电南瑞：1.44亿，占1.5%\n\n这次共79家企业中标，平均每家1.19亿。前三名占了近58%，集中度很高。\n\n2️⃣ 产品结构看亮点\n94亿中，1000kV GIS（气体绝缘开关设备）占了57.4%，是绝对大头。其次是原材料12.6%，1000kV电抗器7.0%。GIS是特高压核心设备，技术壁垒高，毛利率也相对可观。\n\n3️⃣ 电网投资增速在加速\n1Q26全国电网资本开支1675亿，同比增40%。南瑞解释，增量主要来自土建工程，因为政府需要拉动固投转正（从2025年的-3.9%到1Q26的+1.7%）。南瑞预计2Q26高增速还会持续。\n\n4️⃣ 平高2026年交付预期\n- 1100kV GIS交付15台（+36%\n\n[... middle omitted ...]\n\n3% of the new orders; (ii) China XD Electric (601179 CH, not covered) winning Rmb1.899bn or 20.2%; (iii) TBEA (600089 CH, BUY) winning Rmb473m or 5.0%; (iv) Sieyuan Electric (002028 CH, BUY) w\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R040",
    "title": "0005-41-BARC-U.S. Equity-Linked Strategies AI Capex Funding- Why Equity- Why Converts--260609",
    "digest": "[wechat_article.md]\nDeepSeek 生成 WeChat article 失败：Response ended prematurely\n\n请复制对应 prompt 文件手动生成。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n![研报原图 2](assets/source_image_02.jpg)\n\n![研报原图 3](assets/source_image_03.jpg)\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI烧钱太快，巨头开始发可转债了\n\n**AI融资新解法**\n\n**巨头们为什么选择股权+可转债？**\n\n最近投行研报拆了AI巨头们的融资策略，核心逻辑很清晰：AI投资周期太长、体量太大，光靠发债已经不够用了。\n\n1️⃣ **为什么需要股权融资？**\nAI资本支出正在快速吞噬经营现金流。研报数据显示，2028年五大云厂商总资本支出预计达1.16万亿美元，而现金流覆盖比例可能逼近97%。债务市场虽然仍开放，但无限度发债会挤压信用空间。股权融资的核心作用不是“缺钱”，而是：\n- 拓宽融资渠道，减少对单一债务市场的依赖\n- 降低杠杆率，为未来继续发债留出空间\n- 给债券持有人一个“安全垫”，稳定市场信心\n\n2️⃣ **可转债：债务和股权的中间地带**\n可转债兼具两者优势：不需要立即发行全部普通股，又能获得类股权资本。美国可转债市场今年已发行约780亿美元，创2003年以来同期最高。AI相关发行占比高达71%。对于成熟大公司，可转债还能做到“隔夜定价”，速度极快。\n\n3️⃣ **强制可转债：最干净的股权信用结构**\n谷歌和甲骨文都采用了这种结构。它能在资产负债表上获得近乎完全的股权处理，三年后强制转换为普通股，给市场一个明确的资本强化路径。不是最便宜的资金，但信号最强。\n\n4️⃣ **谁可能是下一个？**\nMeta、微软、亚马逊现金流充裕，但研报认为它们也可能通过股权挂钩工具来主动管理资产负债表。一些AI基础设施公司已经在广泛使用可转债。\n\n**核心观点**：这不是融资危机，而是管理团队在利用有利市场条件，提前为多年度AI建设储备资本。股权和可转债是战略工具，不是最后手段。\n\n欢迎一起讨论AI基础设施的融资逻辑。\n\n#学习笔记\n\n[source_mineru.md]\n## U.S. Equity-Linked Strategies\n\n# AI Capex Funding: Why Equity? Why Converts?\n\nAs AI capex becomes larger and longer duration, hyperscalers are broadening their funding mix beyond IG debt. Equity and equity-linked capital can preserve debt capacity, strengthen credit confidence, and support continued investment.\n\nA reminder that we are entering the late innings of the 2026 Extel All-America Research Survey! If you’ve already submitted your ballot, thank you – we truly appreciate it. If not, our team would be grateful for your consideration for a ★★★★★ 5 Star Vote in the [Macro] → [Equity-Linked Strategies & Portfolio Strategy] categories.\n\nEquity capital raise does not signal \"last resort\" financing. Debt markets remain open to AI hyperscalers, but equity broadens the funding bas\n\n[... middle omitted ...]\n\nrior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request."
  },
  {
    "id": "R041",
    "title": "摩根斯坦利：CLO市场真正的分化不在区域，而在管理人的议价权",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：CLO市场真正的分化不在区域，而在管理人的议价权\n\n当大多数市场参与者仍在争论“美国还是欧洲”作为CLO配置的主战场时，摩根斯坦利这份6月CLO追踪报告揭示了一个更本质的信号：市场正在从“买什么区域”转向“买谁管理的资产”。这不是一个温和的风格切换，而是信用周期进入后半段时，市场定价逻辑的一次结构性重组。\n\n这份报告基于摩根斯坦利团队近期跨大西洋与大量CLO投资者的直接对话，结合5月发行数据与信用基本面研判，给出了一组值得产业决策者与资产配置者认真对待的观察。5月新发行量从4月的60亿美元反弹至约170亿美元，而再融资与重置活动更达到年内最强的390亿美元——但在这组看似乐观的数字背后，投资者的叙事已经发生了微妙但深刻的转变。\n\n报告的核心判断可以浓缩为一句话：CLO市场的超额回报正从beta（市场方向）转向alpha（管理人能力），而这一转移对资产定价、管理人格局乃至私人信贷市场的结构都将产生持续影响。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 管理人选股能力正在取代宏观判断，成为CLO定价的首要变量\n\n在与几乎每一位投资者的对话中，摩根斯坦利团队都听到了同一个主题：管理人的选择已成为CLO投资中最重要的决策。这不是一句空洞的行业共识，而是基于一组正在加速变化的市场事实。\n\n报告明确指出，当前信用利差在资本结构的多数层级上仍处于偏紧状态，而AI颠覆风险正在导致抵押品表现出现更大的离散度。这意味着，过去那种“只要市场方向判断对了，组合就能赚钱”的模式正在失效。投资者越来越关注管理人特有的alpha，而非广泛的市场beta。\n\n这一判断有坚实的底层逻辑支撑。摩根斯坦利在报告中提到，当前周期的一个关键特征是：市场走势的方向性减弱，而不同组合之间的表现差异在拉大。这直接考验的是管理人的承销\n\n[... middle omitted ...]\n\n与图表，与关注信用市场的朋友们一起拆解CLO定价的底层逻辑。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nCLO 市场风向：选管理人比选赛道更重要\n\n选管理人是 CLO 投资第一课\n\n最近投行研报跟 CLO 投资者聊了一圈，发现市场共识很明确：**现在不是买 beta 的时候，alpha 全看管理人。** 信用利差整体偏紧，AI 扰动让底层资产表现越来越分化，选对管理人比猜对方向重要得多。\n\n1/ 投资者普遍偏爱有长期业绩的老牌管理人，尤其在欧洲，新管理人那点利差补偿根本不够看。软件敞口低、对 AI 风险有清晰评估框架的管理人更受欢迎。股权投资者尤其看重管理人的控制力，尤其在私募信贷交易里。\n\n2/ 私募信贷 CLO 不是铁板一块。虽然整体情绪偏谨慎——负面新闻多、利差补偿不够——但投资者也承认，**私募信贷太多样，不能一刀切。** 融资驱动型交易（尤其管理人控制力强的）更受青睐。低端中市交易因契约保护强、贷款人群体小，被看高一线；上端中市则因契约条款弱化，普遍被谨慎对待。\n\n3/ 美欧偏好：基本面倾向美国，相对价值倾向欧洲。美国市场深度、管理人广度、发行人多样性优势明显。但欧洲 AAA/AA 档在 Solvency 2 新规下可能迎来保险资金需求，相对价值更吸引人。不过往下走，欧洲的估值优势就不那么明显了。\n\n[... middle omitted ...]\n\naccounts expressed caution against upper-middle-market deals, noting the covenant and documentation erosion seen in the space.  \nOn USD vs EUR, investor preference is firmly tilted toward the \n\n[... middle omitted ...]\n\nhe following authors are Fixed Income Research Analysts/Strategists and are not opining on or expressing recommendations on equity securities: Vasundhara Goel; Gabriel Reyes Esclasans; James Egan; Joyce Jiang.\n\n© 2026 MS"
  },
  {
    "id": "R042",
    "title": "摩根斯坦利：全球矿业正在经历一场“主权供需”的结构性重塑",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：全球矿业正在经历一场“主权供需”的结构性重塑\n\n这份摩根斯坦利最新发布的澳大利亚材料行业研报，表面上是一份常规的行业数据汇编与个股偏好排序。但真正值得产业决策者和长期投资者关注的，是报告中一个正在加速形成的结构性趋势——全球关键矿产的供需两端，都在被主权力量重新组织。这不再是周期性的价格波动，而是贸易规则和竞争格局的底层逻辑变化。\n\n报告提出的核心观察是：以中国新成立的中央采购机构（CMRG）为代表的需求侧主权集中，与印度尼西亚通过国有出口机构（DSI）对煤炭、棕榈油和铁合金进行中央化出口的供给侧主权集中，正在同时发生。过去，市场习惯将矿业视为自由市场定价的典范；但这份研报揭示，未来的游戏规则可能截然不同——国家正在成为最重要的交易对手。\n\n为什么这个判断现在至关重要？因为澳大利亚的矿业公司正处于这场结构性变化的十字路口。澳大利亚是全球铁矿石、冶金煤和锂的关键供应国，但其矿业公司目前受到竞争法的严格约束，无法像主权买家或主权卖家那样进行协调定价或分配策略。摩根斯坦利提出了一个大胆的假设性框架：如果澳大利亚也建立类似的国家出口平台，会怎样？这种“主权对主权”的格局，将彻底改变当前基于边际成本和供需平衡的定价模型。\n\n以下，我们将沿着报告的逻辑链条，逐一拆解这一趋势对行业、公司以及投资者观察框架的具体含义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 主权买家与主权卖家的同步崛起，正在重新定义矿业的交易对手\n\n摩根斯坦利研报最重要的贡献，是将两个看似独立的政策动向——中国的集中采购和印尼的集中出口——放在同一个分析框架下。这不仅仅是巧合，而是全球资源民族主义在贸易层面的具体表现。\n\n从需求侧看，中国成立CMRG的目标是增强议价能力。对于一个占全球铁矿石进口量超过70%的国家来说，分散的采购结构意味着\n\n[... middle omitted ...]\n\n中，结合更多一手信息，与大家共同推演这些关键变量的演变路径。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n资源主权博弈：谁在重新洗牌全球矿业\n\n主权买家 vs 主权卖家\n\n最近某外资投行发了份有意思的研报，讲的是各国政府正在悄悄改变大宗商品的贸易规则。\n\n1/ 中国成立CMRG作为集中采购机构，印尼则把煤炭、棕榈油和铁合金出口统一交给国企DSI管理。印尼占了全球棕榈油出口55%、动力煤海运量45%。\n\n2/ 澳大利亚也不甘示弱——铁矿石海运出口占全球59%，焦煤38%，动力煤20%，锂矿约24%。但目前澳洲矿企没法像政府那样统一行动，怕违反竞争法。\n\n3/ 研报核心观点：如果澳洲也学印尼搞个\"国家出口平台\"，虽然会引发贸易摩擦担忧，但反而能帮矿企在面对政府买家时更有议价能力。\n\n4/ 具体到个股偏好：BHP（目标价隐含铁矿石价约82美元/吨）排在RIO前面（89美元/吨），FMG被看低（98美元/吨），DRR则因高品位矿和低价格敏感度被看好（FY27股息率5.1%）。\n\n全球资源贸易正在从\"市场定价\"转向\"国家博弈\"，这对产业链的影响可能比想象中更深。\n\n#学习笔记\n\n[source_mineru.md]\n## Australia Materials | Asia Pacific\n\n# DataDig: Sove\n\n[... middle omitted ...]\n\nre proceeds onshore. Indonesia accounts for \\~55% of global palm oil exports, and 45% of traded thermal coal supply for 2026. Australia represents \\~59% of seaborne iron ore exports, 38% and 2\n\n[... middle omitted ...]\n\nkel Industries (NIC.AX)</td><td>E (04/09/2025)</td><td>A$1.02</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R043",
    "title": "JPM：合成橡胶的供给缺口正在重塑化工定价权，而市场仍在关注需求侧",
    "digest": "[wechat_article.md]\n# JPM：合成橡胶的供给缺口正在重塑化工定价权，而市场仍在关注需求侧\n\n一份来自JPM亚洲能源与化工研究团队的报告，在2026年6月初释放了一个值得产业链决策者高度重视的信号：韩国NBL（丁腈胶乳）价格在5月攀升至每吨1633美元，4-5月均价创下五年新高。更关键的是，NBL与SBR（丁苯橡胶）的价差结构发生了根本性逆转——NBL的加工利润（Spread）自2022年以来首次超越SBR，达到每吨916美元，为2021年以来的最高水平。\n\n这不是一个简单的价格波动。这是一次由供给端结构性短缺驱动的再定价，而市场的主流叙事仍然停留在需求复苏的节奏上。\n\n这份报告的核心判断可以概括为一句话：**当前合成橡胶市场的超额利润并非来自需求端的强劲反弹，而是来自原料石脑油/LPG短缺引发的供给刚性收缩，以及全球丁二烯体系与下游橡胶产品之间的传导断裂。** 理解这一判断，比猜测下一个季度的油价走势更重要。\n\n为什么现在必须重视这个信号？因为化工行业过去两年的核心叙事是“产能过剩、利润压缩”。几乎所有投资者都在关注需求何时恢复、库存何时去化。但JPM的这份报告揭示了一个相反的局部：在合成橡胶的特定细分领域，供给侧的收缩已经硬到足以让价格脱离成本曲线的牵引。如果这种供给刚性在未来2-3年持续，那么部分化工子行业的定价逻辑将从“需求驱动”切换为“供给约束驱动”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 原料短缺不是暂时的扰动，而是正在改变合成橡胶的竞争格局\n\n报告最引人注目的数据之一，是韩国NBL的出口量在2026年4-5月平均仅为4.4万吨，比2026年第一季度的月均水平下降了33%。这不是需求疲软导致的减产。JPM明确将原因指向了中东局势后的石脑油供应短缺，并据此预测锦湖石化（Kumho Petchem）2026年第二季度\n\n[... middle omitted ...]\n\n塑胶作为JPM亚太区首选标的的逻辑细节。期待与你的深入交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nNBL利润创五年新高，橡胶供应紧张\n\n封面：橡胶原料大涨价\n\n副标题：丁二烯暴跌，NBL却逆势上涨\n\n最近化工圈最热的话题，就是合成橡胶原料NBL（丁腈胶乳）价格创下五年新高。📈\n\n某外资投行最新研报显示，5月韩国NBL价格环比上涨3.4%至1633美元/吨，4-5月均价1606美元/吨，是五年来最高水平。背后的逻辑很清晰：\n\n1️⃣ **原料短缺是主因**\n中东局势导致石脑油供应紧张，预计锦湖石化2季度NBL产量环比下降超20%。同时，美国补库带动马来西亚医疗手套需求回升，进一步推高NBL价格。\n\n2️⃣ **利润结构在变化**\nNBL利润已扩大至916美元/吨，自2022年以来首次超过SBR（丁苯橡胶），创2021年以来新高。受益方包括锦湖石化和LG化学。\n\n3️⃣ **丁二烯暴跌≠橡胶价格跌**\n有意思的是，亚洲丁二烯5月大跌27%，从4月高点1945美元/吨回落。但NBL价格依然坚挺，说明供应端确实紧张。马来西亚手套厂甚至因原料短缺而减产，WRP亚太公司已宣布停产。\n\n4️⃣ **未来怎么看？**\n研报预计NBL价格将逐步回落：3季度1281美元/吨，4季度1083美元/吨。但到2028年，价格仍将高\n\n[... middle omitted ...]\n\nand the highest since 2021. Key beneficiaries include Kumho Petchem and LG Chem, for which we forecast 2Q chems OP to increase q/q despite lower volumes. Our APAC top pick remains Nan Ya Plast\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 08 Jun 2026 10:15 PM HKT\n\nDisseminated 08 Jun 2026 10:15 PM HKT"
  },
  {
    "id": "R044",
    "title": "摩根斯坦利：AI融资的“夏季攻势”已提前到来，市场定价权正从基本面转向供给节奏",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：AI融资的“夏季攻势”已提前到来，市场定价权正从基本面转向供给节奏\n\n市场参与者正在经历一个罕见的时刻：基本面依然强劲，但价格行为的主导力量已经悄然切换。摩根斯坦利在最新发布的《AI债务融资追踪》报告中给出了一个清晰的信号——截至5月31日，2026年全球AI相关债务发行量已达2360亿美元，是2025年同期的4倍以上。但真正值得关注的不是这个数字本身，而是它背后的结构性变化：四月的发行热潮之后，五月美国市场迅速降温，但超大规模云服务商（hyperscalers）并未停止融资脚步，而是通过欧元、加元、瑞士法郎和日元等非美元市场发行了约240亿美元债券。\n\n这意味着什么？AI基础设施的资本密集型属性，正在催生一个前所未有的、跨币种、跨资产类别的融资周期。摩根斯坦利预测，2026年全年全球AI相关债务供应将达到约5700亿美元，较2025年增长162%。但这份报告最核心的判断并不在于供应量的增长，而在于一个被市场低估的变量：**融资节奏的波动本身，正在成为比需求基本面更重要的定价因子。**\n\n报告明确指出，当前市场定价更多由供应预期驱动，而非基本面。这听起来像是一个短期技术面现象，但如果我们深入拆解，会发现这背后隐藏着一个更深层的叙事转换——AI基础设施建设正在从“概念验证”阶段进入“资本运作”阶段，而资本市场对此的定价逻辑，也正在经历一次范式转移。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 四月发行高峰揭示了AI融资的结构性特征，而非季节性波动\n\n四月单月发行量超过740亿美元，创下年内新高。这个数字本身令人印象深刻，但摩根斯坦利的数据揭示了更关键的细节：在AI相关的高收益债发行中，85%用于数据中心外壳建设；在投资级债券中，这一比例也达到了40%。\n\n这意味着，当前AI融资的核心用途并非购买G\n\n[... middle omitted ...]\n\n对AI融资的结构性变化有自己的观察，也欢迎在群里与我们交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI发债节奏：4月爆量，5月蓄力\n\nAI发债热潮，正在升温\n\n某外资投行追踪发现，AI相关债券发行正在加速。4月是今年最忙的一个月，单月发行超740亿美元。5月虽有所放缓，但头部科技公司转向欧元、加元、日元等非美货币市场，发了约240亿美元债。\n\n关键数据点：\n\n1️⃣ 4月是高峰\n- AI相关发行创年内新高，超740亿美元\n- 数据中心项目融资占高收益债的85%、投资级债的40%\n- 大部分资金用于建设数据中心“外壳”\n\n2️⃣ 5月在“喘口气”\n- 美国市场新发减少，但头部科技公司在其他货币市场集体发力\n- 欧元、英镑等基准中，这些发行人占比仍低于美元，意味着非美债还有空间\n- 投资者基础正在扩Daiwa多元化\n\n3️⃣ 技术面＞基本面\n- 基本面依然强劲，但近期价格波动主要受供给预期驱动\n- 尽管供给量高，各类资产利差自一季度末以来普遍收窄\n\n4️⃣ 2026年规模预估\n- 截至5月底，全球AI相关发行已达约2360亿美元，是2025年同期的4倍以上\n- 研报预测2026年全年全球AI相关供给约5700亿美元\n- 预计2026年下半年发行加速，头部科技公司2027年现金资本支出或超1万亿美元\n\n5️⃣ \n\n[... middle omitted ...]\n\ns to fund construction of data center shells accounted for 85% of the AI-related HY supply and 40% of the IG.  \n“May” Be Catching Its Breath: We saw limited new issuance in the US markets in M\n\n[... middle omitted ...]\n\nquity securities: Aron Becker; Eva C Baurmeister; Vishwanath Tirupattur; James Egan; Kelvin Pang; Carolyn L Campbell; Raquel Kanner; Yagyesh Modi; Ellie Dann; Vishwas Patkar; Fernanda Lima; Christina C Sigler.\n\n© 2026 MS"
  },
  {
    "id": "R045",
    "title": "JPM：AI基础设施的下一轮投资机会，藏在松下投资者日被低估的细节里",
    "digest": "[wechat_article.md]\n# JPM：AI基础设施的下一轮投资机会，藏在松下投资者日被低估的细节里\n\n当市场还在为AI芯片的算力竞赛兴奋时，一份来自JPM日本团队的报告，将目光投向了AI基础设施中一个容易被忽视的环节——电源与材料。这份报告的核心判断不是关于GPU的迭代，也不是关于云资本开支的增速，而是指向一个更具体、更可追踪的叙事：**AI基础设施的物理层正在经历从“够用”到“必须重构”的转折，而松下等传统电子巨头，正在这个转折点上占据一个被低估的位置。**\n\n这份报告发布于松下控股投资者日之后，聚焦于能源与产业两大板块的AI基础设施业务。报告中最引人注目的信号，并非松下已经公布的FY2028销售目标——这些在5月的业绩会上已经披露——而是管理层在投资者日上展现出的两个关键态度：第一，他们对FY2028目标的实现有高度信心，甚至暗示实际数字可能更高；第二，他们详细披露了实现这些目标的具体路径和管道。对于习惯于日本企业保守指引的投资者来说，这种程度的明确性本身就是一种信号。\n\n但真正值得深入挖掘的，是报告在字里行间透露出的几个结构性变化。这些变化不仅关乎松下这一家公司，也关乎整个AI基础设施供应链的竞争格局和投资逻辑。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 数据中心储能市场正在从“备用”走向“主动”，CBU将成为下一个增长奇点\n\n松下对数据中心储能系统的目标非常具体：FY2028年实现约1万亿日元的销售收入，而FY2026年的指引仅为5500亿日元。这意味着两年内接近翻倍的增长。但更值得注意的是，松下认为这个目标已经包含了“已确认的产品开发和订单协议”，以及“部分延迟风险”。换句话说，这个目标不是乐观预测，而是基于已有订单的保守估计。\n\n报告中真正的新信息，是松下对电容器备用单元（CBU）市场的展望。松下预计CBU市场在FY202\n\n[... middle omitted ...]\n\n研和后续财报数据，持续更新我们对AI基础设施投资逻辑的理解。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n松下投资者日，数据中心储能是重点\n\n🔋 数据中心储能，目标很明确\n\n松下在投资者日重点讲了AI基础设施业务，给到FY2028的指引非常清晰：\n\n- 能源板块目标：2万亿日元营收，3000亿日元调整后营业利润\n- 其中数据中心储能系统贡献约1万亿日元（FY2026指引是5500亿）\n\n这个1万亿目标已经考虑了已确认的订单和一些延迟风险，实际可能更高。\n\n1️⃣ 下一代产品在路上了\n\n除了传统电池备份单元（BBU），松下在推新品：\n- 电容备份单元（CBU）：预计FY2028市场接近100亿日元，FY2030到1000亿日元\n- 功率机架BBU也在规划中\n\n产能投资3500亿日元，包括日本、堪萨斯（美国）的电池产线，墨西哥的新模块工厂。\n\n2️⃣ 材料与器件，AI相关增长快\n\n行业板块的AI相关业务目标：\n- FY2028：4300亿日元\n- FY2030：5000亿日元\n- FY2026基准：2700亿日元\n\n利润率约20%，和BBU差不多。\n\n核心产品是先进基板材料和导电聚合物电容，计划到FY2030产能翻倍。\n\n有意思的是，基板材料方面，M6及以下占60%，M7/M8约40%，但客户已经在问M9/M10了—\n\n[... middle omitted ...]\n\n industry segments from FY2029, but think discussions about advanced substrate material market share and advantages versus competitors seemed somewhat limited. See below for the main takeaways\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 08 Jun 2026 11:56 PM JST\n\nDisseminated 08 Jun 2026 11:56 PM JST"
  },
  {
    "id": "R046",
    "title": "JPM：市场误读了英伟达进入基站射频单元的影响",
    "digest": "[wechat_article.md]\n# JPM：市场误读了英伟达进入基站射频单元的影响\n\n过去一周，诺基亚和爱立信的股价双双下跌，市场给出的解释高度一致：英伟达正在将AI芯片的触角延伸至基站中最核心、最定制化的射频单元（Radio Unit），这对传统设备商构成生存威胁。\n\n但JPM在最新发布的研报中给出了一个直接对冲市场情绪的结论：这轮下跌是“事后合理化的价格反应”，而非基本面逻辑的必然结果。报告的核心判断是——英伟达的介入不会颠覆设备商的竞争格局，反而可能加速一个更值得关注的结构性变化：电信设备的价值链正在从“硬件定制决定性能”转向“软件差异决定溢价”。\n\n这一判断之所以重要，是因为它触及了通信行业未来五年最根本的路线之争。传统上，基站设备商靠自研ASIC芯片实现性能和功耗的最优解，这是爱立信和诺基亚护城河的核心组成。但英伟达的方案提出了一个替代路径：用标准化的GPU平台承载更多基站功能，让设备商的差异化从芯片设计转移到软件算法。JPM认为，两条路径各有优劣，市场目前高估了英伟达对设备商的威胁，同时低估了诺基亚率先做出选择后可能获得的先发优势。\n\n以下是我们从这份研报中提炼出的四个关键洞察，以及对一个尚未被充分讨论的风险的拆解。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 英伟达的射频单元芯片并未改变设备商的核心选择权\n\nJPM的分析起点是对技术事实的澄清。英伟达正在开发的是面向6G射频单元的GPU芯片，用于替代传统Massive MIMO天线中负责波束赋形等底层物理层功能的定制ASIC。技术驱动力是明确的：随着天线配置从4T4R向128T128R甚至1024T演进，射频单元所需的计算量呈32倍以上增长，可编程的GPU在处理灵活性和规模经济上开始具备理论优势。\n\n但报告明确指出，这并不意味着设备商失去了选择权。诺基亚已经宣布将在6G基带单元（\n\n[... middle omitted ...]\n\n的兴趣，欢迎加入我们的讨论，一起观察这些关键变量的演化路径。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n英伟达入局基站，对设备商是利空吗？\n\n**英伟达的“基站芯片”计划**\n\n**它盯上的是6G时代的天线计算**\n\n---\n\n某外资投行最新研报聊了个有意思的话题：英伟达正在开发一款面向基站射频单元（RU）的GPU芯片，计划用于6G网络，替代传统专用芯片（ASIC）。\n\n1️⃣ **为什么英伟达觉得有机会？**\n核心驱动是Massive MIMO天线阵列的升级。从4T4R（4发4收）到128T128R，计算量暴增约32倍，未来还可能走向1024T1024R。传统ASIC在规模不大的设备市场里缺乏规模经济，而可编程的GPU方案反而有了空间。\n\n2️⃣ **功耗和性能是两大争议点**\n基站RU占了网络约90%的能耗。英伟达的策略可能是推出类似车规级的低功耗嵌入式GPU（低于100W）。但性能上，标准芯片永远追不上定制ASIC。电信运营商需要在“灵活性和成本”与“极致性能”之间做选择。\n\n3️⃣ **诺基亚和爱立信的分岔路**\n- **诺基亚**已明确在基带单元（CU/DU）采用英伟达方案，未来如果全面转向标准平台，RU也可能跟进。它们有CUDA生态的合作经验，切换更快。\n- **爱立信**目前表态不会放弃ASIC，\n\n[... middle omitted ...]\n\n 1,024T/1,024R, more PHY processing shifts to the RU to preserve performance (e.g., beamforming). Nvidia believes this creates an opening to replace RU ASICs with a GPU-based approach as it ma\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 09 Jun 2026 06:06 PM BST\n\nDisseminated 09 Jun 2026 06:08 PM BST"
  },
  {
    "id": "R047",
    "title": "摩根斯坦利：移动广告技术市场最被低估的增长引擎，不是需求，而是转化效率的杠杆效应",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：移动广告技术市场最被低估的增长引擎，不是需求，而是转化效率的杠杆效应\n\n移动广告技术行业正处于一个关键拐点。多数投资者将注意力集中在广告主预算的周期性波动上，关注宏观环境如何影响总支出。但摩根斯坦利最新发布的移动广告技术入门报告揭示了一个更深层的结构性机会：真正的增长驱动力并非来自广告主多花多少钱，而是来自广告技术平台如何通过提升转化率来撬动自身收入。\n\n这份报告的核心判断是：**独立移动广告技术平台正站在一个“效率杠杆”的起点上——转化率每提升一个百分点，平台净收入增长的弹性远高于广告主支出同等幅度的增长。** 当前市场对这一机制的理解仍不充分，尤其是当我们将头部平台（如Meta）与独立平台（如AppLovin、Unity）的转化率进行对比时，差距的规模本身就暗示了巨大的潜在上升空间。\n\n为什么这个判断现在重要？因为市场正在两个方向上产生分歧。一方面，游戏内广告的存量增长正在放缓，独立平台需要寻找新的垂直领域。另一方面，电商、零售等非游戏领域的广告支出正在快速流入移动端。摩根斯坦利估算，独立应用内广告技术平台的可寻址市场在2025年约为790亿美元，到2030年将增长至1360亿美元，年复合增长率约为11%。但真正有趣的问题不是这个市场有多大，而是哪些平台能够最有效地将流量转化为收入，以及这一转化效率本身如何成为竞争的护城河。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 转化效率的差异，定义了独立平台与围墙花园之间的估值鸿沟\n\n理解移动广告技术行业，首先需要理解一个核心指标链条：点击率乘以转化率，决定了广告平台为广告主带来一次安装或购买所需消耗的展示次数。而这一效率，直接决定了平台能够从广告主支出中“截留”多少作为自己的净收入——也就是所谓的“抽成率”。\n\n摩根斯坦利的分析提供了一个令人震惊的\n\n[... middle omitted ...]\n\n没有标准答案。但它们正是值得在更深入的讨论中继续探索的方向。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n移动广告技术，一篇讲透\n\n**广告技术到底在玩什么**\n\n某外资投行最近出了一份移动广告技术科普研报，把整个生态链拆得很清楚。我提炼了几个关键点，适合想了解这个赛道的朋友。\n\n**1/ 市场有多大？**\n全球移动广告支出每年$5540亿，其中App内广告占了$3320亿。而独立广告技术平台能分到的蛋糕大概是$790亿，预计到2030年能涨到$1360亿。增长主要靠游戏、零售和娱乐这几个赛道。\n\n**2/ 玩家分哪几类？**\n- **DSP**：帮广告主自动买广告位的软件，能分析数据、做用户定向\n- **SSP**：帮媒体方把广告位卖出去，通常用拍卖形式，追求收益最大化\n- **Mediation**：媒体方用来连接多个SSP的工具，实时比价，选最高出价方\n\n核心玩家比如AppLovin、Unity、Google等，很多公司同时扮演多个角色。\n\n**3/ 钱怎么分的？**\n以$3 CPM为例：广告主出$3，DSP拿$0.45，SSP拿$0.45，Mediation拿$0.06，剩下$2.04归媒体方。大部分利润在媒体方手里。\n\n**4/ 增长的核心逻辑**\n不是靠广告主多花钱，而是靠提升转化率。转化率高了，广告\n\n[... middle omitted ...]\n\nity Of Growth\"]\n  B --> C[\"3\\nCompetition\"]\n  C --> D[\"4\\nImpact of AI\"]\n  D --> E[\"5\\nSignal/Privacy & Platform Risk\"]\n```\n</details>\n\n## In-App Ads Typically Send Consumers to the App Stores\n\n[... middle omitted ...]\n\nCanary Wharf\n\nLondon E14 4AD\n\nUnited Kingdom\n\n+44 (0)20 7425 8000\n\n## Japan\n\n1-9-7 Otemachi, Chiyoda-ku\n\nTokyo 100-8104\n\nJapan\n\n+81 (0) 3 6836 5000\n\n## Asia/Pacific\n\n1 Austin Road West\n\nKowloon\n\nHong Kong\n\n+852 2848 5200"
  },
  {
    "id": "R048",
    "title": "摩根斯坦利：市场低估的不是半导体设备周期性，而是结构性瓶颈的再定价",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：市场低估的不是半导体设备周期性，而是结构性瓶颈的再定价\n\n当台北的Computex和AI Summit刚刚落幕，许多参会者带回的共识是：半导体设备板块的热度似乎从2025年底至2026年初的亢奋中冷却下来。投资者态度变得“更加平衡”。但这份来自摩根斯坦利日本团队的调研笔记，真正想传递的信号恰好相反——市场正在犯一个典型的“半杯水”错误。\n\n会议期间，投资者对存储周期的担忧在现货价格回升后明显消退，对2027年前的存储景气度几乎没有悲观声音。但真正值得关注的，不是周期是否延续，而是三个正在重塑半导体设备行业定价权的结构性变量：Agentic AI对DRAM需求的量级跳跃、铜墙(Cu Wall)迫使光互连提前成为技术瓶颈，以及日本设备商在定价能力上的沉默但剧烈变化。\n\n这份报告最核心的判断是：半导体设备行业正在从“周期成长”切换为“结构成长”，而市场对这一切换的定价仍不充分。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 一颗Vera CPU的需求量级，正在改写DRAM的供需方程\n\n摩根斯坦利台湾半导体分析师Charlie Chan从供应链确认的数据，值得每一个关注AI资本开支的人重新审视。NVIDIA的Vera CPU单颗可搭载1.5TB的LPDDR5X，是上一代Grace CPU的三倍。以200-400万颗产量估算，仅Vera一个产品线，就需要消耗2025年全球DRAM bit总需求的10%-16%。\n\n这不是一个边际增量。这是在一个原本被认为供需趋于平衡的市场中，突然出现的、由单一产品驱动的结构性缺口。换算成产能，这相当于10-20万片/月的1cnm晶圆产能需求。考虑到先进DRAM产能的扩产周期和良率爬坡速度，这个数字意味着未来2-3年内，存储设备订单的可预见性远高于市场共识。\n\n摩根斯坦利的调\n\n[... middle omitted ...]\n\n内分享完整的研报解读和原始图表，并围绕这些未解问题持续跟踪。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n半导体设备，机会藏在后道里\n\n📌 铜墙到顶，光互联接棒\n\n刚从台北Computex回来，某外资投行团队的核心感受是：市场对半导体设备的热情比年初冷静了，但对存储周期的悲观反而少了。\n\n关键是三个新信号👇\n\n**1/ 存储需求不会停**\nVera CPU单颗需要1.5TB LPDDR5X，是Grace的三倍。按200-400万颗产量算，光这一个芯片就要吃掉全球DRAM产能的10%以上。存储短缺可能持续2-3年，前道设备依然是最大赢家。\n\n**2/ “铜墙”逼出的CPO机会**\nMarvell在Computex上解释了为什么光互联不可避免：铜线传输距离和速率成反比。\n- 100G/lane：5米\n- 200G：2.5米\n- 400G（2028年）：1.25米\n机柜高度2米，到400G时铜线根本不够用。CPO测试设备市场将从2026年的1亿美金，跳到2028年的3-7亿美金，之后破10亿。\n\n**3/ 几个具体标的的看点**\n- Advantest：被调为Top Pick，后续催化剂来自EPS上修，CPO测试需求是长期逻辑\n- Kokusai：当前保守指引有上修空间，中国DRAM客户和NAND回暖是额外弹性\n- T\n\n[... middle omitted ...]\n\ne recently made Advantest our Top Pick.  \nThrough Computex, etc., we reconfirmed memory demand expansion driven by agentic AI, as well as growing focus on co-packaged optics (CPO) as the next \n\n[... middle omitted ...]\n\n<td>Ushio (6925.T)</td><td>O (01/05/2026)</td><td>¥4,260</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS MUFG"
  },
  {
    "id": "R049",
    "title": "摩根斯坦利：欧洲猎头行业的真正风险不在需求，而在永久招聘的结构性萎缩",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：欧洲猎头行业的真正风险不在需求，而在永久招聘的结构性萎缩\n\n市场正在为欧洲人力资源服务公司的有机增长改善而松一口气，但这份摩根斯坦利的最新研报提出了一个更值得警惕的判断：临时招聘的回暖并不能掩盖永久招聘（perm recruitment）正在发生的结构性恶化，后者才是决定这些公司毛利率、经营杠杆和估值能否修复的真正变量。\n\n这份报告发布于2026年6月，正值欧洲宏观环境因地缘政治不确定性再度升温之际。摩根斯坦利的分析师团队对欧洲人力资源板块进行了评级调整，其核心逻辑不是基于对经济周期的简单判断，而是基于对招聘业务结构本身的风险重估。\n\n报告明确指出，尽管行业有机增长在过去几个季度有所改善，但改善主要来自临时招聘，而永久招聘的持续恶化正在侵蚀毛利率和经营利润。更关键的是，市场共识尚未充分反映这一风险。\n\n这意味着什么？如果永久招聘的萎缩不是周期性的，而是结构性的——比如企业用人模式正在从“雇佣”转向“灵活用工”——那么当前估值所隐含的复苏预期可能过于乐观。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 临时招聘回暖是假象，永久招聘的恶化才是决定毛利率的关键\n\n过去几个季度，欧洲人力资源公司的有机增长数据确实出现了改善迹象。但摩根斯坦利指出，股价对这些改善几乎没有反应。原因在于，投资者真正在等待的是毛利率的恢复和经营杠杆的改善，而这两者恰恰与永久招聘的占比高度相关。\n\n永久招聘的毛利率远高于临时招聘。当一家公司从永久招聘中获得的收入占比下降时，整体毛利率就会承压。报告中的数据显示，Adecco的永久招聘占毛利润比例约为15-17%，Randstad约为16%，而Hays高达38%，Page Group更是达到72%。\n\n这意味着，Page Group和Hays对永久招聘的依赖度远高于Adecco和Ra\n\n[... middle omitted ...]\n\n业、或者如何评估不同公司之间的相对价值感兴趣，欢迎加入讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n欧洲猎头行业，正在经历一场结构性分化\n\n📉 永久招聘风险上升\n\n最近某外资投行更新了欧洲招聘行业的研究观点，核心逻辑很清晰：宏观不确定性正在对永久招聘（perm recruitment）形成持续压力，而这部分业务的高利润属性，决定了它直接影响公司毛利率和经营杠杆。\n\n1️⃣ 行业现状：临时招聘回暖，但永久招聘持续走弱\n虽然行业有机增长近期有所改善（主要靠临时工拉动），但宏观和地缘政治环境变得更不确定。投行认为，市场共识还没完全消化永久招聘进一步恶化的风险。同时，AI对中期的潜在冲击也在压制估值。\n\n2️⃣ 为什么市场不买账？\n最近几次有机增长超预期，股价却没有正面反应。说明投资者在等毛利率回升和经营杠杆改善。但永久招聘持续走弱，意味着毛利率和经营利润还会承压。下一个财报季，催化剂的缺失让板块很难获得重新评级。\n\n3️⃣ 个股偏好调整\n投行重新排序了覆盖标的：\n- Randstad（EW）> Adecco（UW）：Adecco面临更大的预期下行风险，加上杠杆偏高和股票股息带来的稀释风险\n- Hays（EW）> Page Group（UW）：Page Group有72%的毛利来自永久招聘，是同行中暴露度最高的，而\n\n[... middle omitted ...]\n\n macroeconomic and geopolitical environment has become more uncertain and could take a toll on the recruitment/ staffing market, something we think has not yet been fully reflected in consensu\n\n[... middle omitted ...]\n\nr><tr><td>TP (TEPRF.PA)</td><td>E (03/24/2026)</td><td>€58.66</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R002",
    "label": "Figure 1",
    "context": "Figure 1: Global commodity flows recovered over the week, owing to metals-led inflows, partially offset by outflows from crude oil USD billion, cumulative flows across tracked commodity markets"
  },
  {
    "figure_id": "F002",
    "report_id": "R002",
    "label": "Figure 2",
    "context": "Figure 2: The estimated value of global commodity market open interest decreased by 1% WoW USD billion, estimated open interest across tracked commodity markets"
  },
  {
    "figure_id": "F003",
    "report_id": "R002",
    "label": "Figure 3",
    "context": "Figure 3: Net length across commodity markets increased by \\$0.2 billion WoW real USD million, Net investor positioning aggregated across tracked commodity markets"
  },
  {
    "figure_id": "F004",
    "report_id": "R002",
    "label": "Figure 5",
    "context": "Figure 5: The CTA net long positioning in COMEX Gold increased by 11% over the week USD/oz (average weekly gold price); bubble size represents magnitude of weekly increase (green) or decrease (red) in CTA F&O net length"
  },
  {
    "figure_id": "F005",
    "report_id": "R002",
    "label": "Figure 4",
    "context": "Figure 4: Latest projections indicate decreasing positioning in agri markets 0-10 standardised scale: 0 = lowest since 2018, 10 = highest since 2018 positioning data in real USD terms"
  },
  {
    "figure_id": "F006",
    "report_id": "R002",
    "label": "Figure 6",
    "context": "Figure 6: The estimated value of open interest across energy markets stabilised over the week USD billion, estimated open interest across tracked energy markets"
  },
  {
    "figure_id": "F007",
    "report_id": "R002",
    "label": "Figure 7",
    "context": "Figure 7: The estimated value of open interest across environmental markets decreased by 4% WoW USD billion, estimated open interest across tracked environmental markets"
  },
  {
    "figure_id": "F008",
    "report_id": "R002",
    "label": "Figure 9",
    "context": "Figure 9: The estimated value of open interest across base metals markets plateaued over the week USD billion, estimated open interest across tracked base metals markets"
  },
  {
    "figure_id": "F009",
    "report_id": "R002",
    "label": "Figure 11",
    "context": "Figure 11: The estimated value of open interest in crude oil decreased by 1% WoW USD billion, estimated open interest across tracked crude oil markets"
  },
  {
    "figure_id": "F010",
    "report_id": "R002",
    "label": "Figure 8",
    "context": "Figure 8: The estimated value of open interest across precious metals decreased by 3% WoW USD billion, estimated open interest across tracked precious metals markets"
  },
  {
    "figure_id": "F011",
    "report_id": "R002",
    "label": "Figure 10",
    "context": "Figure 10: The estimated value of open interest in agri markets decreased by 3% WoW USD billion, estimated open interest across tracked agricultural markets"
  },
  {
    "figure_id": "F012",
    "report_id": "R002",
    "label": "Figure 12",
    "context": "Figure 12: Petroleum products estimated open interest value increased by 3% WoW USD billion, estimated open interest across tracked petroleum products markets"
  },
  {
    "figure_id": "F013",
    "report_id": "R002",
    "label": "Figure 13",
    "context": "Figure 13: The estimated value of open interest in natural gas markets increased by 3% WoW USD billion, estimated open interest across tracked natural gas metals markets"
  },
  {
    "figure_id": "F014",
    "report_id": "R002",
    "label": "Figure 15",
    "context": "Figure 15: The estimated value of open interest in soft markets increased by 2% WoW USD billion, estimated open interest across tracked soft agricultural markets"
  },
  {
    "figure_id": "F015",
    "report_id": "R002",
    "label": "Figure 14",
    "context": "Figure 14: The estimated value of open interest in grains & oilseeds markets decreased by 5% WoW USD billion, estimated open interest across tracked grains and oilseeds markets"
  },
  {
    "figure_id": "F016",
    "report_id": "R002",
    "label": "Figure 16",
    "context": "Figure 16: The estimated open interest value across livestock markets decreased by 3% WoW USD billion, estimated open interest across tracked livestock markets"
  },
  {
    "figure_id": "F017",
    "report_id": "R002",
    "label": "Figure 17",
    "context": "Figure 17: Price momentum (z-scores) and trading signals across major commodities \\*see methodology in Figure 18"
  },
  {
    "figure_id": "F018",
    "report_id": "R002",
    "label": "Figure 19",
    "context": "Figure 19: Energy sectoral standardised level chart 0-10 standardised scale: 0 = lowest since 2018, 10 = highest since 2018 positioning data in real USD terms"
  },
  {
    "figure_id": "F019",
    "report_id": "R002",
    "label": "Figure 21",
    "context": "Figure 21: NYMEX WTI Crude Oil position and price LHS: n of contracts; RHS: \\$/bbl"
  },
  {
    "figure_id": "F020",
    "report_id": "R002",
    "label": "Figure 23",
    "context": "Figure 23: ICE Dubai Crude Oil position and price LHS: n of contracts; RHS: \\$/bbl"
  },
  {
    "figure_id": "F021",
    "report_id": "R002",
    "label": "Figure 20",
    "context": "Figure 20: Energy underlying commodities standardised level chart 0-10 standardised scale: 0 = lowest since 2018, 10 = highest since 2018 positioning data in real USD terms"
  },
  {
    "figure_id": "F022",
    "report_id": "R002",
    "label": "Figure 22",
    "context": "Figure 22: ICE Brent Crude Oil position and price LHS: n of contracts; RHS: \\$/bbl"
  },
  {
    "figure_id": "F023",
    "report_id": "R002",
    "label": "Figure 24",
    "context": "Figure 24: ICE TTF Natural Gas position and price LHS: TWh; RHS: \\$/MWh"
  },
  {
    "figure_id": "F024",
    "report_id": "R002",
    "label": "Figure 25",
    "context": "Figure 25: Weekly change in total OI due to price/flows"
  },
  {
    "figure_id": "F025",
    "report_id": "R002",
    "label": "Figure 27",
    "context": "Figure 27: Weekly change in total OI from changes in contracts (\\$flows)"
  },
  {
    "figure_id": "F026",
    "report_id": "R002",
    "label": "Figure 26",
    "context": "Figure 26: Weekly change in total OI from changes in prices"
  },
  {
    "figure_id": "F027",
    "report_id": "R002",
    "label": "Figure 28",
    "context": "Figure 28: Environmental markets standardised level chart 0-10 standardised scale: 0 = lowest since 2018, 10 = highest since 2018 positioning data in real USD terms"
  },
  {
    "figure_id": "F028",
    "report_id": "R002",
    "label": "Figure 30",
    "context": "Figure 30: Weekly change in total OI due to price/flows USD million"
  },
  {
    "figure_id": "F029",
    "report_id": "R002",
    "label": "Figure 29",
    "context": "Figure 29: ICE EUA position and price LHS: n of contracts; RHS: \\$/MT"
  },
  {
    "figure_id": "F030",
    "report_id": "R002",
    "label": "Figure 31",
    "context": "Figure 31: Weekly change in total OI from changes in prices USD million"
  },
  {
    "figure_id": "F031",
    "report_id": "R002",
    "label": "Figure 32",
    "context": "Figure 32: Weekly change in total OI from changes in contracts (flows) USD million"
  },
  {
    "figure_id": "F032",
    "report_id": "R002",
    "label": "Figure 33",
    "context": "Figure 33: Metals sectoral standardised level chart 0-10 standardised scale: 0 = lowest since 2018, 10 = highest since 2018 positioning data in real USD terms"
  },
  {
    "figure_id": "F033",
    "report_id": "R002",
    "label": "Figure 35",
    "context": "Figure 35: Precious Metals standardised level chart 0-10 standardised scale: 0 = lowest since 2018, 10 = highest since 2018 positioning data in real USD terms"
  },
  {
    "figure_id": "F034",
    "report_id": "R002",
    "label": "Figure 37",
    "context": "Figure 37: COMEX Copper position and price LHS: n of contracts; RHS: \\$/lb"
  },
  {
    "figure_id": "F035",
    "report_id": "R002",
    "label": "Figure 34",
    "context": "Figure 34: Base Metals standardised level chart 0-10 standardised scale: 0 = lowest since 2018, 10 = highest since 2018 positioning data in real USD terms"
  },
  {
    "figure_id": "F036",
    "report_id": "R002",
    "label": "Figure 36",
    "context": "Figure 36: COMEX Gold position and price LHS: n of contracts; RHS: \\$/t oz"
  },
  {
    "figure_id": "F037",
    "report_id": "R002",
    "label": "Figure 38",
    "context": "Figure 38: LME Copper position and price LHS: n of contracts; RHS: \\$/MT"
  },
  {
    "figure_id": "F038",
    "report_id": "R002",
    "label": "Figure 39",
    "context": "Figure 39: Weekly change in total OI due to price/flows"
  },
  {
    "figure_id": "F039",
    "report_id": "R002",
    "label": "Figure 41",
    "context": "Figure 41: Weekly change in total OI from changes in contracts (\\$flows)"
  },
  {
    "figure_id": "F040",
    "report_id": "R002",
    "label": "Figure 43",
    "context": "Figure 43: Weekly change in total OI from changes in contracts (flows)-precious metals"
  },
  {
    "figure_id": "F041",
    "report_id": "R002",
    "label": "Figure 40",
    "context": "Figure 40: Weekly change in total OI from changes in prices"
  },
  {
    "figure_id": "F042",
    "report_id": "R002",
    "label": "Figure 42",
    "context": "Figure 42: Weekly change in total OI from changes in contracts (flows)-industrial and bulk metals"
  },
  {
    "figure_id": "F043",
    "report_id": "R002",
    "label": "Figure 44",
    "context": "Figure 44: Agriculture commodities sectoral standardised level chart 0-10 standardised scale: 0 = lowest since 2018, 10 = highest since 2018 positioning data in real USD terms"
  },
  {
    "figure_id": "F044",
    "report_id": "R002",
    "label": "Figure 46",
    "context": "Figure 46: Softs standardised level chart 0-10 standardised scale: 0 = lowest since 2018, 10 = highest since 2018 positioning data in real USD terms"
  },
  {
    "figure_id": "F045",
    "report_id": "R002",
    "label": "Figure 48",
    "context": "Figure 48: Weekly change in total OI due to price/flows USD million"
  },
  {
    "figure_id": "F046",
    "report_id": "R002",
    "label": "Figure 45",
    "context": "Figure 45: Grains & oilseeds standardised level chart 0-10 standardised scale: 0 = lowest since 2018, 10 = highest since 2018 positioning data in real USD terms"
  },
  {
    "figure_id": "F047",
    "report_id": "R002",
    "label": "Figure 47",
    "context": "Figure 47: Livestock standardised level chart 0-10 standardised scale: 0 = lowest since 2018, 10 = highest since 2018 positioning data in real USD terms"
  },
  {
    "figure_id": "F048",
    "report_id": "R002",
    "label": "Figure 49",
    "context": "Figure 49: Weekly change in total OI from changes in prices USD million"
  },
  {
    "figure_id": "F049",
    "report_id": "R002",
    "label": "Figure 50",
    "context": "Figure 50: Weekly change in total OI from changes in contracts (\\$flows) USD million"
  },
  {
    "figure_id": "F050",
    "report_id": "R002",
    "label": "Figure 51",
    "context": "Figure 51: Weekly change in total OI from changes in contracts (flows) - grains and oilseeds"
  },
  {
    "figure_id": "F051",
    "report_id": "R002",
    "label": "Figure 52",
    "context": "Figure 53: The Global Commodities Inventory Monitor is estimated on a global and ex-China basis, showing apparent inventories on a days of use basis LHS: Inventories in days of use; RHS: BCOM Price index"
  },
  {
    "figure_id": "F052",
    "report_id": "R002",
    "label": "Figure 53",
    "context": "Figure 53: The Global Commodities Inventory Monitor is estimated on a global and ex-China basis, showing apparent inventories on a days of use basis LHS: Inventories in days of use; RHS: BCOM Price index"
  },
  {
    "figure_id": "F053",
    "report_id": "R002",
    "label": "Figure 54",
    "context": "Figure 54: The Ex-US natural gas Global Commodity Inventory Monitor is estimated on a global and ex-China basis, showing apparent inventories on a days of use basis LHS: Inventories in days of use; RHS: BCOM Price index"
  },
  {
    "figure_id": "F054",
    "report_id": "R002",
    "label": "Figure 55",
    "context": "Figure 55: China's share of world commodity inventories"
  },
  {
    "figure_id": "F055",
    "report_id": "R002",
    "label": "Figure 56",
    "context": "Figure 56: The Global and Ex-China Commodities Inventory Monitors reported in standardised form Z-scores of global commodities inventories as days of use"
  },
  {
    "figure_id": "F056",
    "report_id": "R002",
    "label": "Figure 57",
    "context": "Figure 57: The Ex-US natural gas Global and Ex-US natural gas Ex-China Commodities Inventory Monitors reported in standardised form Z-scores of global commodities inventories as days of use"
  },
  {
    "figure_id": "F057",
    "report_id": "R002",
    "label": "Figure 58",
    "context": "Figure 58: Sectoral Global Commodities Inventory Monitors Z-scores of global commodities inventories as days of use"
  },
  {
    "figure_id": "F058",
    "report_id": "R002",
    "label": "Figure 59",
    "context": "Figure 59: Sectoral Ex-China Commodities Inventory Monitors Z-scores of global commodities inventories as days of use"
  },
  {
    "figure_id": "F059",
    "report_id": "R002",
    "label": "Figure 60",
    "context": "Figure 60: Global commodities inventory seasonality"
  },
  {
    "figure_id": "F060",
    "report_id": "R002",
    "label": "Figure 61",
    "context": "Figure 61: Global commodities inventory seasonality (Ex-natural gas)"
  },
  {
    "figure_id": "F061",
    "report_id": "R002",
    "label": "Figure 62",
    "context": "Figure 62: Ex-China commodities inventory seasonality Z-scores of global commodities inventories as days of use"
  },
  {
    "figure_id": "F062",
    "report_id": "R002",
    "label": "Figure 63",
    "context": "Figure 63: Ex-US natural gas Ex-China commodities inventory seasonality Z-scores of global commodities inventories as days of use"
  },
  {
    "figure_id": "F063",
    "report_id": "R002",
    "label": "Figure 64",
    "context": "Figure 64: Oil inventories"
  },
  {
    "figure_id": "F064",
    "report_id": "R002",
    "label": "Figure 66",
    "context": "Figure 66: US Natural Gas inventories"
  },
  {
    "figure_id": "F065",
    "report_id": "R002",
    "label": "Figure 65",
    "context": "Figure 65: Oil inventories on a days of use basis"
  },
  {
    "figure_id": "F066",
    "report_id": "R002",
    "label": "Figure 67",
    "context": "Figure 67: US Natural Gas inventories on a days of use basis"
  },
  {
    "figure_id": "F067",
    "report_id": "R002",
    "label": "Figure 68",
    "context": "Figure 68: Copper inventories"
  },
  {
    "figure_id": "F068",
    "report_id": "R002",
    "label": "Figure 70",
    "context": "Figure 70: Aluminium inventories"
  },
  {
    "figure_id": "F069",
    "report_id": "R002",
    "label": "Figure 72",
    "context": "Figure 72: Zinc inventories"
  },
  {
    "figure_id": "F070",
    "report_id": "R002",
    "label": "Figure 69",
    "context": "Figure 69: Copper inventories on a days of use basis"
  },
  {
    "figure_id": "F071",
    "report_id": "R002",
    "label": "Figure 71",
    "context": "Figure 71: Aluminium inventories on a days of use basis"
  },
  {
    "figure_id": "F072",
    "report_id": "R002",
    "label": "Figure 73",
    "context": "Figure 73: Zinc inventories on a days of use basis"
  },
  {
    "figure_id": "F073",
    "report_id": "R002",
    "label": "Figure 74",
    "context": "Figure 74: Nickel inventories"
  },
  {
    "figure_id": "F074",
    "report_id": "R002",
    "label": "Figure 76",
    "context": "Figure 76: Lead inventories"
  },
  {
    "figure_id": "F075",
    "report_id": "R002",
    "label": "Figure 78",
    "context": "Figure 78: Corn inventories"
  },
  {
    "figure_id": "F076",
    "report_id": "R002",
    "label": "Figure 75",
    "context": "Figure 75: Nickel inventories on a days of use basis"
  },
  {
    "figure_id": "F077",
    "report_id": "R002",
    "label": "Figure 77",
    "context": "Figure 77: Lead inventories on a days of use basis"
  },
  {
    "figure_id": "F078",
    "report_id": "R002",
    "label": "Figure 79",
    "context": "Figure 79: Corn inventories on a days of use basis"
  },
  {
    "figure_id": "F079",
    "report_id": "R002",
    "label": "Figure 80",
    "context": "Figure 80: Wheat inventories"
  },
  {
    "figure_id": "F080",
    "report_id": "R002",
    "label": "Figure 82",
    "context": "Figure 82: Cotton inventories"
  },
  {
    "figure_id": "F081",
    "report_id": "R002",
    "label": "Figure 84",
    "context": "Figure 84: Cocoa global inventories"
  },
  {
    "figure_id": "F082",
    "report_id": "R002",
    "label": "Figure 81",
    "context": "Figure 81: Wheat inventories on a days of use basis"
  },
  {
    "figure_id": "F083",
    "report_id": "R002",
    "label": "Figure 83",
    "context": "Figure 83: Cotton inventories on a days of use basis"
  },
  {
    "figure_id": "F084",
    "report_id": "R002",
    "label": "Figure 85",
    "context": "Figure 85: Cocoa global inventories on a days of use basis"
  },
  {
    "figure_id": "F085",
    "report_id": "R002",
    "label": "Figure 86",
    "context": "Figure 86: Coffee inventories"
  },
  {
    "figure_id": "F086",
    "report_id": "R002",
    "label": "Figure 88",
    "context": "Figure 88: Sugar global inventories"
  },
  {
    "figure_id": "F087",
    "report_id": "R002",
    "label": "Figure 90",
    "context": "Figure 90: Soybean inventories"
  },
  {
    "figure_id": "F088",
    "report_id": "R002",
    "label": "Figure 87",
    "context": "Figure 87: Coffee inventories on a days of use basis"
  },
  {
    "figure_id": "F089",
    "report_id": "R002",
    "label": "Figure 89",
    "context": "Figure 89: Sugar global inventories on a days of use basis"
  },
  {
    "figure_id": "F090",
    "report_id": "R002",
    "label": "Figure 91",
    "context": "Figure 91: Soybean inventories on a days of use basis"
  },
  {
    "figure_id": "F091",
    "report_id": "R002",
    "label": "Figure 92",
    "context": "Figure 92: Soybean Meal inventories"
  },
  {
    "figure_id": "F092",
    "report_id": "R002",
    "label": "Figure 94",
    "context": "Figure 94: Soybean Oil inventories"
  },
  {
    "figure_id": "F093",
    "report_id": "R002",
    "label": "Figure 93",
    "context": "Figure 93: Soybean Meal inventories on a days of use basis"
  },
  {
    "figure_id": "F094",
    "report_id": "R002",
    "label": "Figure 95",
    "context": "Figure 95: Soybean Oil inventories on a days of use basis"
  },
  {
    "figure_id": "F095",
    "report_id": "R005",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Using forward curve differentials, the copper market is pricing 43% chance of a 15% tariff in place by Jan 2027 and 73% by Dec 2027"
  },
  {
    "figure_id": "F096",
    "report_id": "R005",
    "label": "Exhibit 2",
    "context": "Exhibit 2: The COMEX-LME spread has been rising"
  },
  {
    "figure_id": "F097",
    "report_id": "R005",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Seaborne copper imports remain above the estimate 15-20kt/week that the US needs"
  },
  {
    "figure_id": "F098",
    "report_id": "R005",
    "label": "Exhibit 4",
    "context": "US Implied Copper Stockpiling (kt)"
  },
  {
    "figure_id": "F099",
    "report_id": "R005",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Ex-US LME inventories have been tightening in China and on the LME"
  },
  {
    "figure_id": "F100",
    "report_id": "R005",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Base metals price indices (12-month rolling)"
  },
  {
    "figure_id": "F101",
    "report_id": "R005",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Precious metals indices (12-month rolling)"
  },
  {
    "figure_id": "F102",
    "report_id": "R005",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Bulk commodity price indices (12-month rolling)"
  },
  {
    "figure_id": "F103",
    "report_id": "R005",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Spot commodity prices vs. the marginal cost of production"
  },
  {
    "figure_id": "F104",
    "report_id": "R005",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Key metals: one-week absolute performance"
  },
  {
    "figure_id": "F105",
    "report_id": "R005",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Key metals: YTD absolute performance"
  },
  {
    "figure_id": "F106",
    "report_id": "R005",
    "label": "Exhibit 18",
    "context": "Exhibit 18: China's Electricity Output & Consumption"
  },
  {
    "figure_id": "F107",
    "report_id": "R005",
    "label": "Exhibit 19",
    "context": "Exhibit 19: China's Purchasing Managers Index and Industrial Production (IP)"
  },
  {
    "figure_id": "F108",
    "report_id": "R005",
    "label": "Exhibit 20",
    "context": "Exhibit 20: China's Money Supply"
  },
  {
    "figure_id": "F109",
    "report_id": "R005",
    "label": "Exhibit 21",
    "context": "Exhibit 21: China's Output of Industrial Products"
  },
  {
    "figure_id": "F110",
    "report_id": "R005",
    "label": "Exhibit 22",
    "context": "Exhibit 22: China's Infrastructure Fixed Asset Investments (FAI)"
  },
  {
    "figure_id": "F111",
    "report_id": "R005",
    "label": "Exhibit 24",
    "context": "Exhibit 24: China's Floor Space Started, Sold and Completed"
  },
  {
    "figure_id": "F112",
    "report_id": "R005",
    "label": "Exhibit 23",
    "context": "Exhibit 23: China's Fixed Asset Investments"
  },
  {
    "figure_id": "F113",
    "report_id": "R005",
    "label": "Exhibit 25",
    "context": "Exhibit 25: Floor Space of Buildings Newly Started"
  },
  {
    "figure_id": "F114",
    "report_id": "R005",
    "label": "Exhibit 26",
    "context": "Exhibit 26: China Autos Production"
  },
  {
    "figure_id": "F115",
    "report_id": "R005",
    "label": "Exhibit 27",
    "context": "Exhibit 27: China Cumulative Grid Investment"
  },
  {
    "figure_id": "F116",
    "report_id": "R005",
    "label": "Exhibit 28",
    "context": "Exhibit 28: China Demand Indicators China Demand Indicators (% YoY)"
  },
  {
    "figure_id": "F117",
    "report_id": "R005",
    "label": "Exhibit 29",
    "context": "Exhibit 29: China Excavator Sales"
  },
  {
    "figure_id": "F118",
    "report_id": "R005",
    "label": "Exhibit 30",
    "context": "Exhibit 30: China Railway FAI YTD"
  },
  {
    "figure_id": "F119",
    "report_id": "R005",
    "label": "Exhibit 31",
    "context": "Exhibit 31: China Shipbuilding Output"
  },
  {
    "figure_id": "F120",
    "report_id": "R005",
    "label": "Exhibit 32",
    "context": "Exhibit 32: Global Aluminium Inventories"
  },
  {
    "figure_id": "F121",
    "report_id": "R005",
    "label": "Exhibit 33",
    "context": "Exhibit 33: China Aluminium Inventories"
  },
  {
    "figure_id": "F122",
    "report_id": "R005",
    "label": "Exhibit 34",
    "context": "Exhibit 34: Indonesia Aluminium Exports"
  },
  {
    "figure_id": "F123",
    "report_id": "R005",
    "label": "Exhibit 35",
    "context": "Exhibit 35: Raw Materials: Spot Alumina vs China Domestic Price"
  },
  {
    "figure_id": "F124",
    "report_id": "R005",
    "label": "Exhibit 36",
    "context": "Exhibit 36: Price Differentials: SHFE vs LME"
  },
  {
    "figure_id": "F125",
    "report_id": "R005",
    "label": "Exhibit 37",
    "context": "Exhibit 37: Physical demand: aluminium premia, by region"
  },
  {
    "figure_id": "F126",
    "report_id": "R005",
    "label": "Exhibit 38",
    "context": "Exhibit 38: IAI Global Aluminium Production"
  },
  {
    "figure_id": "F127",
    "report_id": "R005",
    "label": "Exhibit 39",
    "context": "Exhibit 39: China Aluminium Production China Annualised Aluminium Output (ktpa)"
  },
  {
    "figure_id": "F128",
    "report_id": "R005",
    "label": "Exhibit 40",
    "context": "Exhibit 40: Aluminium C1 Cost Curve vs Spot (\\$/t)"
  },
  {
    "figure_id": "F129",
    "report_id": "R005",
    "label": "Exhibit 41",
    "context": "Exhibit 41: Aluminium Cost Curve Evolution"
  },
  {
    "figure_id": "F130",
    "report_id": "R005",
    "label": "Exhibit 42",
    "context": "Exhibit 42: Alumina Total Cost Curve vs Spot (\\$/t)"
  },
  {
    "figure_id": "F131",
    "report_id": "R005",
    "label": "Exhibit 43",
    "context": "Exhibit 43: Alumina Cost Curve Evolution"
  },
  {
    "figure_id": "F132",
    "report_id": "R005",
    "label": "Exhibit 44",
    "context": "Exhibit 44: Global Copper Inventories"
  },
  {
    "figure_id": "F133",
    "report_id": "R005",
    "label": "Exhibit 46",
    "context": "Exhibit 46: Copper Price versus China Apparent Consumption China Apparent Consumption and Copper Price"
  },
  {
    "figure_id": "F134",
    "report_id": "R005",
    "label": "Exhibit 45",
    "context": "Exhibit 45: China Copper Inventories"
  },
  {
    "figure_id": "F135",
    "report_id": "R005",
    "label": "Exhibit 47",
    "context": "Exhibit 47: Copper CFTC Positioning"
  },
  {
    "figure_id": "F136",
    "report_id": "R005",
    "label": "Exhibit 48",
    "context": "Exhibit 48: Price Differentials: SHFE vs LME"
  },
  {
    "figure_id": "F137",
    "report_id": "R005",
    "label": "Exhibit 50",
    "context": "Exhibit 50: Raw materials: China's copper concentrate, refined and scrap monthly import China Copper Imports (tonnes per month)"
  },
  {
    "figure_id": "F138",
    "report_id": "R005",
    "label": "Exhibit 49",
    "context": "Exhibit 49: Copper treatment charges (TCs)"
  },
  {
    "figure_id": "F139",
    "report_id": "R005",
    "label": "Exhibit 51",
    "context": "Exhibit 51: Physical Demand: Copper Premia By Region"
  },
  {
    "figure_id": "F140",
    "report_id": "R005",
    "label": "Exhibit 52",
    "context": "Exhibit 52: Copper C1 Cost Curve vs Spot (USc/lb)"
  },
  {
    "figure_id": "F141",
    "report_id": "R005",
    "label": "Exhibit 54",
    "context": "Exhibit 54: Copper: Aluminium Ratio"
  },
  {
    "figure_id": "F142",
    "report_id": "R005",
    "label": "Exhibit 53",
    "context": "Exhibit 53: Copper Cost Curve Evolution"
  },
  {
    "figure_id": "F143",
    "report_id": "R005",
    "label": "Exhibit 55",
    "context": "Exhibit 55: China Grid Investment"
  },
  {
    "figure_id": "F144",
    "report_id": "R005",
    "label": "Exhibit 56",
    "context": "Exhibit 56: Global Nickel Inventories"
  },
  {
    "figure_id": "F145",
    "report_id": "R005",
    "label": "Exhibit 58",
    "context": "Exhibit 58: Nickel C1 Cost Curve vs Spot (USc/lb)"
  },
  {
    "figure_id": "F146",
    "report_id": "R005",
    "label": "Exhibit 57",
    "context": "Exhibit 57: LME Nickel Positioning"
  },
  {
    "figure_id": "F147",
    "report_id": "R005",
    "label": "Exhibit 59",
    "context": "Exhibit 59: Nickel Cost Curve Evolution"
  },
  {
    "figure_id": "F148",
    "report_id": "R005",
    "label": "Exhibit 60",
    "context": "Exhibit 60: Nickel Product Spreads vs LME Price"
  },
  {
    "figure_id": "F149",
    "report_id": "R005",
    "label": "Exhibit 62",
    "context": "Exhibit 62: China NEV Sales"
  },
  {
    "figure_id": "F150",
    "report_id": "R005",
    "label": "Exhibit 61",
    "context": "Exhibit 61: Global Battery Deployment by Chemistry"
  },
  {
    "figure_id": "F151",
    "report_id": "R005",
    "label": "Exhibit 63",
    "context": "Exhibit 63: China PHEV Sales"
  },
  {
    "figure_id": "F152",
    "report_id": "R005",
    "label": "Exhibit 64",
    "context": "Exhibit 64: Global Zinc Inventories"
  },
  {
    "figure_id": "F153",
    "report_id": "R005",
    "label": "Exhibit 65",
    "context": "Exhibit 65: China Refined Zinc Imports China Refined Zinc Imports (ktpm)"
  },
  {
    "figure_id": "F154",
    "report_id": "R005",
    "label": "Exhibit 66",
    "context": "Exhibit 66: China Zinc Concentrate Imports China Zinc Conc Imports (ktpm)"
  },
  {
    "figure_id": "F155",
    "report_id": "R005",
    "label": "Exhibit 67",
    "context": "Exhibit 67: China Refined Zinc Output China Refined Zinc Output (ktpm)"
  },
  {
    "figure_id": "F156",
    "report_id": "R005",
    "label": "Exhibit 68",
    "context": "Exhibit 68: Price Differentials: SHFE vs LME"
  },
  {
    "figure_id": "F157",
    "report_id": "R005",
    "label": "Exhibit 70",
    "context": "Exhibit 70: Zinc Premia"
  },
  {
    "figure_id": "F158",
    "report_id": "R005",
    "label": "Exhibit 69",
    "context": "Exhibit 69: Zinc Treatment Charges"
  },
  {
    "figure_id": "F159",
    "report_id": "R005",
    "label": "Exhibit 71",
    "context": "Exhibit 71: Zinc/Lead Ratio"
  },
  {
    "figure_id": "F160",
    "report_id": "R005",
    "label": "Exhibit 72",
    "context": "Exhibit 72: Zinc C1 Cost Curve vs Spot (\\$/t)"
  },
  {
    "figure_id": "F161",
    "report_id": "R005",
    "label": "Exhibit 74",
    "context": "Exhibit 74: Zinc Positioning LME Investment Funds Zinc Positioning"
  },
  {
    "figure_id": "F162",
    "report_id": "R005",
    "label": "Exhibit 73",
    "context": "Exhibit 73: Zinc Cost Curve Evolution"
  },
  {
    "figure_id": "F163",
    "report_id": "R005",
    "label": "Exhibit 75",
    "context": "Exhibit 75: Lead Positioning LME Investment Funds Lead Positioning"
  },
  {
    "figure_id": "F164",
    "report_id": "R005",
    "label": "Exhibit 76",
    "context": "Exhibit 76: Lithium Chemical Prices"
  },
  {
    "figure_id": "F165",
    "report_id": "R005",
    "label": "Exhibit 78",
    "context": "Exhibit 78: China Lithium Carbonate Imports"
  },
  {
    "figure_id": "F166",
    "report_id": "R005",
    "label": "Exhibit 77",
    "context": "Exhibit 77: Non-integrated Convertor Margins"
  },
  {
    "figure_id": "F167",
    "report_id": "R005",
    "label": "Exhibit 79",
    "context": "Exhibit 79: Chile Lithium Exports"
  },
  {
    "figure_id": "F168",
    "report_id": "R005",
    "label": "Exhibit 80",
    "context": "Exhibit 80: Uranium Price (Spot and Term) Monthly Uranium Price (\\$/lb)"
  },
  {
    "figure_id": "F169",
    "report_id": "R005",
    "label": "Exhibit 82",
    "context": "Exhibit 82: US Enriched Uranium Imports US Imports of Enriched Uranium (tonnes/month)"
  },
  {
    "figure_id": "F170",
    "report_id": "R005",
    "label": "Exhibit 81",
    "context": "Exhibit 81: Sprott ETF Purchases Sprott Physical Uranium Purchases (Mn lb) vs Spot Price (\\$/lb)"
  },
  {
    "figure_id": "F171",
    "report_id": "R005",
    "label": "Exhibit 83",
    "context": "Exhibit 83: Quarterly contracting volumes Uranium Traded Volumes (mln lbs U308)"
  },
  {
    "figure_id": "F172",
    "report_id": "R005",
    "label": "Exhibit 84",
    "context": "Exhibit 84: CFTC Gold Futures Positioning"
  },
  {
    "figure_id": "F173",
    "report_id": "R005",
    "label": "Exhibit 86",
    "context": "Exhibit 86: COMEX Gold Inventories"
  },
  {
    "figure_id": "F174",
    "report_id": "R005",
    "label": "Exhibit 85",
    "context": "Exhibit 85: COMEX-LBMA Gold Premium"
  },
  {
    "figure_id": "F175",
    "report_id": "R005",
    "label": "Exhibit 87",
    "context": "Exhibit 87: London Gold Vault Stocks"
  },
  {
    "figure_id": "F176",
    "report_id": "R005",
    "label": "Exhibit 88",
    "context": "Exhibit 88: US 10 Year TIPS and DXY"
  },
  {
    "figure_id": "F177",
    "report_id": "R005",
    "label": "Exhibit 90",
    "context": "Exhibit 90: Global Gold Demand by Sector"
  },
  {
    "figure_id": "F178",
    "report_id": "R005",
    "label": "Exhibit 89",
    "context": "Exhibit 89: ETF Holdings vs Gold Price"
  },
  {
    "figure_id": "F179",
    "report_id": "R005",
    "label": "Exhibit 91",
    "context": "Exhibit 91: Gold Cost Curve Evolution"
  },
  {
    "figure_id": "F180",
    "report_id": "R005",
    "label": "Exhibit 92",
    "context": "Exhibit 92: Geopolitical Risk Index"
  },
  {
    "figure_id": "F181",
    "report_id": "R005",
    "label": "Exhibit 93",
    "context": "Exhibit 93: Monthly Central Bank Purchasing"
  },
  {
    "figure_id": "F182",
    "report_id": "R005",
    "label": "Exhibit94",
    "context": "Exhibit94: Gold/Silver Ratio"
  },
  {
    "figure_id": "F183",
    "report_id": "R005",
    "label": "Exhibit95",
    "context": "Exhibit95: CFTC Silver Futures Positioning"
  },
  {
    "figure_id": "F184",
    "report_id": "R005",
    "label": "Exhibit 96",
    "context": "Exhibit 96: COMEX Silver Inventories"
  },
  {
    "figure_id": "F185",
    "report_id": "R005",
    "label": "Exhibit 98",
    "context": "Exhibit 98: Total ETF Holdings"
  },
  {
    "figure_id": "F186",
    "report_id": "R005",
    "label": "Exhibit 97",
    "context": "Exhibit 97: London Vault Silver Stocks"
  },
  {
    "figure_id": "F187",
    "report_id": "R005",
    "label": "Exhibit 99",
    "context": "Exhibit 99: China Solar Installations China YTD Solar Installations (GW)"
  },
  {
    "figure_id": "F188",
    "report_id": "R005",
    "label": "Exhibit 100",
    "context": "Exhibit 100: China CISA Steel Production"
  },
  {
    "figure_id": "F189",
    "report_id": "R005",
    "label": "Exhibit 101",
    "context": "Exhibit 101: China Steel Inventory"
  },
  {
    "figure_id": "F190",
    "report_id": "R005",
    "label": "Exhibit 102",
    "context": "Exhibit 102: China Steel Exports"
  },
  {
    "figure_id": "F191",
    "report_id": "R005",
    "label": "Exhibit 103",
    "context": "Exhibit 103: Global Steel Production"
  },
  {
    "figure_id": "F192",
    "report_id": "R005",
    "label": "Exhibit 104",
    "context": "Exhibit 104: China BF Utilisation Rate"
  },
  {
    "figure_id": "F193",
    "report_id": "R005",
    "label": "Exhibit 105",
    "context": "Exhibit 105: China EAF Utilisation Rate"
  },
  {
    "figure_id": "F194",
    "report_id": "R005",
    "label": "Exhibit 106",
    "context": "Exhibit 106: China Steel Scrap Ratio"
  },
  {
    "figure_id": "F195",
    "report_id": "R005",
    "label": "Exhibit 107",
    "context": "Exhibit 107: China Steel Mill Margin"
  },
  {
    "figure_id": "F196",
    "report_id": "R005",
    "label": "Exhibit 108",
    "context": "Exhibit 108: China BF Utilisation"
  },
  {
    "figure_id": "F197",
    "report_id": "R005",
    "label": "Exhibit 109",
    "context": "Exhibit 109: China Iron Ore Port Inventory"
  },
  {
    "figure_id": "F198",
    "report_id": "R005",
    "label": "Exhibit 110",
    "context": "Exhibit 110: Australia Iron Ore Shipments"
  },
  {
    "figure_id": "F199",
    "report_id": "R005",
    "label": "Exhibit 111",
    "context": "Exhibit 111: China Iron Ore Arrivals"
  },
  {
    "figure_id": "F200",
    "report_id": "R005",
    "label": "Exhibit 112",
    "context": "Exhibit 112: India Iron Ore Shipments"
  },
  {
    "figure_id": "F201",
    "report_id": "R005",
    "label": "Exhibit 113",
    "context": "Exhibit 113: Brazil Iron Ore Shipments"
  },
  {
    "figure_id": "F202",
    "report_id": "R005",
    "label": "Exhibit 114",
    "context": "Exhibit 114: Freight Rates to China"
  },
  {
    "figure_id": "F203",
    "report_id": "R005",
    "label": "Exhibit 115",
    "context": "Exhibit 115: Iron Ore Premia/Discount"
  },
  {
    "figure_id": "F204",
    "report_id": "R005",
    "label": "Exhibit 116",
    "context": "Exhibit 116: China Coal Imports"
  },
  {
    "figure_id": "F205",
    "report_id": "R005",
    "label": "Exhibit 117",
    "context": "Exhibit 117: China Coal Production"
  },
  {
    "figure_id": "F206",
    "report_id": "R005",
    "label": "Exhibit 118",
    "context": "Exhibit 118: China Thermal Coal Imports China's Thermal Coal Imports by Origin (Mt/month)"
  },
  {
    "figure_id": "F207",
    "report_id": "R005",
    "label": "Exhibit 119",
    "context": "Exhibit 119: China Met Coal Imports China's Met Coal Imports by Origin (Mt/month)"
  },
  {
    "figure_id": "F208",
    "report_id": "R005",
    "label": "Exhibit 120",
    "context": "Exhibit 120: India Coal Imports"
  },
  {
    "figure_id": "F209",
    "report_id": "R005",
    "label": "Exhibit 121",
    "context": "Exhibit 121: India Coal Production"
  },
  {
    "figure_id": "F210",
    "report_id": "R005",
    "label": "Exhibit 122",
    "context": "Exhibit 122: India Coal Consumption"
  },
  {
    "figure_id": "F211",
    "report_id": "R005",
    "label": "Exhibit 123",
    "context": "Exhibit 123: India Coal Inventory at Power Station India's Coal Inventory at Power Stations (Mt)"
  },
  {
    "figure_id": "F212",
    "report_id": "R005",
    "label": "Exhibit 124",
    "context": "Exhibit 124: India Steel Production"
  },
  {
    "figure_id": "F213",
    "report_id": "R005",
    "label": "Exhibit 126",
    "context": "Exhibit 126: India Thermal Coal Imports India's Thermal Coal Imports by Origin (Mt/month)"
  },
  {
    "figure_id": "F214",
    "report_id": "R005",
    "label": "Exhibit 125",
    "context": "Exhibit 125: India Coal Arrivals India's weekly total coal arrivals (4-week moving average, Mt/week)"
  },
  {
    "figure_id": "F215",
    "report_id": "R005",
    "label": "Exhibit 127",
    "context": "Exhibit 127: India Met-Coal Imports"
  },
  {
    "figure_id": "F216",
    "report_id": "R005",
    "label": "Exhibit 128",
    "context": "Exhibit 128: Queensland Coal Shipments"
  },
  {
    "figure_id": "F217",
    "report_id": "R005",
    "label": "Exhibit 129",
    "context": "Exhibit 129: Australia Thermal Coal Shipments"
  },
  {
    "figure_id": "F218",
    "report_id": "R005",
    "label": "Exhibit 130",
    "context": "Exhibit 130: Coal Stocks at Qinhuangdao Port"
  },
  {
    "figure_id": "F219",
    "report_id": "R005",
    "label": "Exhibit 131",
    "context": "Exhibit 131: China Coal-fired Power Generation"
  },
  {
    "figure_id": "F220",
    "report_id": "R005",
    "label": "Exhibit 132",
    "context": "Exhibit 132: Aluminium (large cap)"
  },
  {
    "figure_id": "F221",
    "report_id": "R005",
    "label": "Exhibit133",
    "context": "Exhibit133: Aluminium (small-medium cap)"
  },
  {
    "figure_id": "F222",
    "report_id": "R005",
    "label": "Exhibit134",
    "context": "Exhibit134: Alumina"
  },
  {
    "figure_id": "F223",
    "report_id": "R005",
    "label": "Exhibit 135",
    "context": "Exhibit 135: Copper"
  },
  {
    "figure_id": "F224",
    "report_id": "R005",
    "label": "Exhibit136",
    "context": "Exhibit136: Nickel (large cap)"
  },
  {
    "figure_id": "F225",
    "report_id": "R005",
    "label": "Exhibit 137",
    "context": "Exhibit 137: Nickel (small-medium cap)"
  },
  {
    "figure_id": "F226",
    "report_id": "R005",
    "label": "Exhibit138",
    "context": "Exhibit138: Diversifieds"
  },
  {
    "figure_id": "F227",
    "report_id": "R005",
    "label": "Exhibit 139",
    "context": "Exhibit 139: Zinc"
  },
  {
    "figure_id": "F228",
    "report_id": "R005",
    "label": "Exhibit140",
    "context": "Exhibit140: Gold (large cap)"
  },
  {
    "figure_id": "F229",
    "report_id": "R005",
    "label": "Exhibit141",
    "context": "Exhibit141: Gold (small/medium cap)"
  },
  {
    "figure_id": "F230",
    "report_id": "R005",
    "label": "Exhibit142",
    "context": "Exhibit142: Gold (small / medium cap)"
  },
  {
    "figure_id": "F231",
    "report_id": "R005",
    "label": "Exhibit143",
    "context": "Exhibit143: Silver"
  },
  {
    "figure_id": "F232",
    "report_id": "R005",
    "label": "Exhibit144",
    "context": "Exhibit144: Iron ore"
  },
  {
    "figure_id": "F233",
    "report_id": "R005",
    "label": "Exhibit145",
    "context": "Exhibit145: Metallurgical coal"
  },
  {
    "figure_id": "F234",
    "report_id": "R005",
    "label": "Exhibit146",
    "context": "Exhibit146: Thermal coal – Asia"
  },
  {
    "figure_id": "F235",
    "report_id": "R005",
    "label": "Exhibit 147",
    "context": "Exhibit 147: Thermal coal – North America"
  },
  {
    "figure_id": "F236",
    "report_id": "R005",
    "label": "Exhibit148",
    "context": "Exhibit148: Uranium"
  },
  {
    "figure_id": "F237",
    "report_id": "R005",
    "label": "Exhibit149",
    "context": "Exhibit149: Oil"
  },
  {
    "figure_id": "F238",
    "report_id": "R005",
    "label": "Exhibit150",
    "context": "Exhibit150: Diversifieds"
  },
  {
    "figure_id": "F239",
    "report_id": "R005",
    "label": "Exhibit 151",
    "context": "Exhibit 151: PGM"
  },
  {
    "figure_id": "F240",
    "report_id": "R007",
    "label": "Exhibit 4",
    "context": "Exhibit 1: Year-over-year PPI inflation increased further from April to May"
  },
  {
    "figure_id": "F241",
    "report_id": "R007",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Food CPI inflation fell in May on a broad-based decline in food prices Contribution to year-over-year food inflation"
  },
  {
    "figure_id": "F242",
    "report_id": "R007",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Non-food CPI inflation edged up on higher energy prices"
  },
  {
    "figure_id": "F243",
    "report_id": "R007",
    "label": "Exhibit 4",
    "context": "Exhibit 4: PPI inflation increased further from April to May, mainly due to higher energy and related chemical prices Contribution to year-over-year PPI inflation"
  },
  {
    "figure_id": "F244",
    "report_id": "R008",
    "label": "Exhibit 2",
    "context": "EXHIBIT 2: Monthly China ESS batteries shipments 93.1GWh (92% YoY, 14% MoM) China ESS shipment (GWh)"
  },
  {
    "figure_id": "F245",
    "report_id": "R008",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Monthly China ESS batteries shipments divided by producers"
  },
  {
    "figure_id": "F246",
    "report_id": "R008",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: China ESS shipment growth rate for top producers CATL, BYD and LG are covered by Bernstein. The rest are not covered. EXHIBIT 6: China ESS top producers' shipment in 2026 China ESS shipment by Top Producers (GWh) in 20"
  },
  {
    "figure_id": "F247",
    "report_id": "R008",
    "label": "Exhibit 7",
    "context": "EXHIBIT 7: Monthly China ESS batteries manufacturing capacity was 98.0GWh (35% YoY, 15% MoM)"
  },
  {
    "figure_id": "F248",
    "report_id": "R008",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: Monthly China ESS manufacturing capacity utilization rate China Manufacturing Capacity Utilization Rate"
  },
  {
    "figure_id": "F249",
    "report_id": "R008",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: Monthly China ESS batteries manufacturing capacity share by producers China ESS Manufacturing Capacity by Producers"
  },
  {
    "figure_id": "F250",
    "report_id": "R008",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: Monthly China ESS batteries manufacturing capacity by producers China ESS Manufacturing Capacity by Producers (GWh) CATL and BYD are covered by Bernstein. The rest are not covered. EXHIBIT 11: Monthly China ESS batteri"
  },
  {
    "figure_id": "F251",
    "report_id": "R008",
    "label": "Exhibit 13",
    "context": "EXHIBIT 13: Monthly China ESS tender (GWh)"
  },
  {
    "figure_id": "F252",
    "report_id": "R008",
    "label": "Exhibit 14",
    "context": "EXHIBIT 14: Monthly China ESS winning bid(GWh) China winning bid (GWh)"
  },
  {
    "figure_id": "F253",
    "report_id": "R008",
    "label": "Exhibit 15",
    "context": "EXHIBIT 15: Monthly U.S. installation 2.5GWh, -25% YoY, 77% MoM US monthly installation (GWh)"
  },
  {
    "figure_id": "F254",
    "report_id": "R008",
    "label": "Exhibit 16",
    "context": "EXHIBIT 16: Monthly Germany ESS battery installation 1.0GWh (58% YoY, 177% MoM) Germany's monthly installation (GWh)"
  },
  {
    "figure_id": "F255",
    "report_id": "R008",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 17: CATL – monthly utilization rate for ESS was 96% EXHIBIT 18: CATL – monthly capacity for ESS was 20.8 GWh(56%YoY) CATL's ESS Utilization rate"
  },
  {
    "figure_id": "F256",
    "report_id": "R008",
    "label": "EXHIBIT 19",
    "context": "EXHIBIT 19: CATL – monthly shipment for ESS was 20 GWh(72%YoY) CATL's ESS Shipment (GWh)"
  },
  {
    "figure_id": "F257",
    "report_id": "R008",
    "label": "EXHIBIT 20",
    "context": "EXHIBIT 20: CATL – monthly production for ESS was 20 GWh(100%YoY) CATL's ESS Production (GWh)"
  },
  {
    "figure_id": "F258",
    "report_id": "R008",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 21: Hithium – monthly utilization rate for ESS was 105% Hithium's ESS Utilization rate"
  },
  {
    "figure_id": "F259",
    "report_id": "R008",
    "label": "EXHIBIT 22",
    "context": "EXHIBIT 22: Hithium – monthly capacity for ESS was 6.7 GWh(14%YoY) Hithium's ESS Capacity (GWh)"
  },
  {
    "figure_id": "F260",
    "report_id": "R008",
    "label": "EXHIBIT 23",
    "context": "EXHIBIT 23: Hithium – monthly shipment for ESS was 8.4 GWh(68%YoY) Hithium's ESS Shipment (GWh)"
  },
  {
    "figure_id": "F261",
    "report_id": "R008",
    "label": "EXHIBIT 24",
    "context": "EXHIBIT 24: Hithum – monthly production for ESS was 7.0 GWh(40%YoY) Hithium's ESS Production (GWh)"
  },
  {
    "figure_id": "F262",
    "report_id": "R008",
    "label": "EXHIBIT 25",
    "context": "EXHIBIT 25: CALB – monthly utilization rate for ESS was 96%"
  },
  {
    "figure_id": "F263",
    "report_id": "R008",
    "label": "EXHIBIT 26",
    "context": "EXHIBIT 26: CALB – monthly capacity for ESS was 5.8GWh(27%YoY)"
  },
  {
    "figure_id": "F264",
    "report_id": "R008",
    "label": "EXHIBIT 27",
    "context": "EXHIBIT 27: CALB – monthly shipment for ESS was 6.1GWh(53%YoY)"
  },
  {
    "figure_id": "F265",
    "report_id": "R008",
    "label": "EXHIBIT 28",
    "context": "EXHIBIT 28: CALB – monthly production for ESS was 5.6GWh(55%YoY)"
  },
  {
    "figure_id": "F266",
    "report_id": "R008",
    "label": "EXHIBIT 29",
    "context": "EXHIBIT 29: BYD – monthly utilization rate for ESS was 96%"
  },
  {
    "figure_id": "F267",
    "report_id": "R008",
    "label": "EXHIBIT 30",
    "context": "EXHIBIT 30: BYD – monthly capacity for ESS was 7.5GWh(38%YoY) BYD's ESS Capacity (GWh)"
  },
  {
    "figure_id": "F268",
    "report_id": "R008",
    "label": "EXHIBIT 31",
    "context": "EXHIBIT 31: BYD – monthly shipment for ESS was 7.4GWh(48%YoY) BYD's ESS Shipment (GWh)"
  },
  {
    "figure_id": "F269",
    "report_id": "R008",
    "label": "EXHIBIT 32",
    "context": "EXHIBIT 32: BYD – monthly production for ESS was 7.2GWh(80%YoY) BYD's ESS Production (GWh)"
  },
  {
    "figure_id": "F270",
    "report_id": "R008",
    "label": "EXHIBIT 33",
    "context": "EXHIBIT 33: EVE – monthly utilization rate for ESS was 96% EVE's ESS Utilization rate"
  },
  {
    "figure_id": "F271",
    "report_id": "R008",
    "label": "EXHIBIT 34",
    "context": "EXHIBIT 34: EVE – monthly capacity for ESS was 8.3GWh(51%YoY) EVE's ESS Capacity (GWh)"
  },
  {
    "figure_id": "F272",
    "report_id": "R008",
    "label": "EXHIBIT 35",
    "context": "EXHIBIT 35: EVE – monthly shipment for ESS was 8.5GWh(70%YoY) EVE's ESS Shipment (GWh)"
  },
  {
    "figure_id": "F273",
    "report_id": "R008",
    "label": "EXHIBIT 36",
    "context": "EXHIBIT 36: EVE – monthly production for ESS was 8.0GWh(60%YoY) EVE's ESS Production (GWh)"
  },
  {
    "figure_id": "F274",
    "report_id": "R008",
    "label": "EXHIBIT 37",
    "context": "EXHIBIT 37: Global ESS battery demand outlook EXHIBIT 38: At the battery cell shipment level, we expect BESS battery demand to increase by 86%, reaching 1,023GWh in 2026, followed by a CAGR of 20% over the next four years, culminati"
  },
  {
    "figure_id": "F275",
    "report_id": "R011",
    "label": "Figure 3",
    "context": "- Foreign inflows into US-focused equity ETFs and mutual funds[1] totaled USD2.6bn between 1 and 5 June (Figure 3), and compared with inflows of USD2.9bn over the previous week. In May, inflows into these funds totaled USD8.8bn, the largest inflows since USD9."
  },
  {
    "figure_id": "F276",
    "report_id": "R013",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Inflation Indices and USD/JPY Rate"
  },
  {
    "figure_id": "F277",
    "report_id": "R013",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Domestic CGPI: Gasoline and Naphtha Prices"
  },
  {
    "figure_id": "F278",
    "report_id": "R014",
    "label": "Figure 1",
    "context": "Figure 1: Recent LNG tanker movements across the Strait of Hormuz Vessels All Types Vessel History AL DRAYEN"
  },
  {
    "figure_id": "F279",
    "report_id": "R014",
    "label": "Figure 3",
    "context": "Figure 3: USGC LNG exports to Europe/Mediterranean"
  },
  {
    "figure_id": "F280",
    "report_id": "R014",
    "label": "Figure 4",
    "context": "Figure 4: USGC LNG exports to Asia/RoW"
  },
  {
    "figure_id": "F281",
    "report_id": "R014",
    "label": "Figure 5",
    "context": "Figure 5: Shipping costs"
  },
  {
    "figure_id": "F282",
    "report_id": "R014",
    "label": "Figure 6",
    "context": "Figure 6: Change in LNG imports Bcm, 1-7 June 2026"
  },
  {
    "figure_id": "F283",
    "report_id": "R014",
    "label": "Figure 7",
    "context": "Figure 7: Change in LNG exports (loadings) Bcm, 1-7 June 2026"
  },
  {
    "figure_id": "F284",
    "report_id": "R014",
    "label": "Figure 9",
    "context": "Figure 9: LNG vessels through the Strait of Hormuz n of vessels, 7 day moving sum"
  },
  {
    "figure_id": "F285",
    "report_id": "R014",
    "label": "Figure 11",
    "context": "Figure 11: LNG vessels through the Panama Canal n of vessels, 7 day moving sum"
  },
  {
    "figure_id": "F286",
    "report_id": "R014",
    "label": "Figure 10",
    "context": "Figure 10: LNG vessels through the Suez Canal n of vessels, 7 day moving sum"
  },
  {
    "figure_id": "F287",
    "report_id": "R014",
    "label": "Figure 12",
    "context": "Figure 12: LNG vessels through the Cape of Good Hope n of vessels, 7 day moving sum"
  },
  {
    "figure_id": "F288",
    "report_id": "R014",
    "label": "Figure 13",
    "context": "Figure 13: Plaquemines weekly exports and capacity utilisation"
  },
  {
    "figure_id": "F289",
    "report_id": "R014",
    "label": "Figure 15",
    "context": "Figure 15: CCL 3 weekly exports and capacity utilisation"
  },
  {
    "figure_id": "F290",
    "report_id": "R014",
    "label": "Figure 17",
    "context": "Figure 17: LNG Canada weekly exports and capacity utilisation"
  },
  {
    "figure_id": "F291",
    "report_id": "R014",
    "label": "Figure 14",
    "context": "Figure 14: Plaquemines seasonal exports"
  },
  {
    "figure_id": "F292",
    "report_id": "R014",
    "label": "Figure 16",
    "context": "Figure 16: CCL 3 seasonal exports"
  },
  {
    "figure_id": "F293",
    "report_id": "R014",
    "label": "Figure 18",
    "context": "Figure 18: LNG Canada seasonal exports"
  },
  {
    "figure_id": "F294",
    "report_id": "R014",
    "label": "Figure 19",
    "context": "Figure 19: Arctic LNG 2 weekly exports and capacity utilisation LHS: Bcm, RHS: %"
  },
  {
    "figure_id": "F295",
    "report_id": "R014",
    "label": "Figure 21",
    "context": "Figure 21: Darwin weekly exports and capacity utilisation LHS: Bcm, RHS: %"
  },
  {
    "figure_id": "F296",
    "report_id": "R014",
    "label": "Figure 23",
    "context": "Figure 23: Tortue LNG weekly exports and capacity utilisation LHS: Bcm, RHS: %"
  },
  {
    "figure_id": "F297",
    "report_id": "R014",
    "label": "Figure 20",
    "context": "Figure 20: Arctic 2 seasonal exports Mcm/day, 4w MA"
  },
  {
    "figure_id": "F298",
    "report_id": "R014",
    "label": "Figure 22",
    "context": "Figure 22: Congo weekly exports and capacity utilisation LHS: Bcm, RHS: %"
  },
  {
    "figure_id": "F299",
    "report_id": "R014",
    "label": "Figure 24",
    "context": "Figure 24: Golden Pass feedgas flows MMcf/day"
  },
  {
    "figure_id": "F300",
    "report_id": "R014",
    "label": "Figure 25",
    "context": "Figure 25: Golden Pass weekly exports and capacity utilisation LHS: Bcm, RHS: %"
  },
  {
    "figure_id": "F301",
    "report_id": "R015",
    "label": "Exhibit 1",
    "context": "Exhibit 1: EM gains vs G3 expected"
  },
  {
    "figure_id": "F302",
    "report_id": "R015",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Diversified funding reduces risk Expected Total Returns / Vol"
  },
  {
    "figure_id": "F303",
    "report_id": "R015",
    "label": "Exhibit 3",
    "context": "Exhibit 3: EM vs DM Gains Continue"
  },
  {
    "figure_id": "F304",
    "report_id": "R015",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Long EM vs EUR has been effective, but vs G3 also attractive"
  },
  {
    "figure_id": "F305",
    "report_id": "R015",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Return statistics for differently funded long EM currency exposure (since 2010) Exhibit 6: Funding with either baskets or CAD provided higher Sharpe ratios & more consistent returns Total Return / Vol"
  },
  {
    "figure_id": "F306",
    "report_id": "R015",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Debt flows have somewhat stabilized Net Monthly FPI in Debt (US$ bn)"
  },
  {
    "figure_id": "F307",
    "report_id": "R015",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Equities continue to see foreign outflows Net Monthly FPI in Equity (US$ bn)"
  },
  {
    "figure_id": "F308",
    "report_id": "R015",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Net FPI flows by financial year Net FPI by Financial Year (US$ bn)"
  },
  {
    "figure_id": "F309",
    "report_id": "R015",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Cumulative debt flow in recent years"
  },
  {
    "figure_id": "F310",
    "report_id": "R015",
    "label": "Exhibit 10",
    "context": "Exhibit 10: FAR and General G-Sec flows since JPM GBI-EM inclusion announcement Foreign Bond Flows since JPM GBI-EM Inclusion Announcement (in US$ bn)"
  },
  {
    "figure_id": "F311",
    "report_id": "R015",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Cumulative equity flow in recent years"
  },
  {
    "figure_id": "F312",
    "report_id": "R015",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Flows have stabilised"
  },
  {
    "figure_id": "F313",
    "report_id": "R015",
    "label": "Exhibit 14",
    "context": "Exhibit 14: 3m flows negative but the weakness is back-loaded"
  },
  {
    "figure_id": "F314",
    "report_id": "R015",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Inflows are correlated with returns. So if we hit extremes on outflows (not there yet) the risk/reward to enter the market could be strong"
  },
  {
    "figure_id": "F315",
    "report_id": "R015",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Positioning in the FX Options Market"
  },
  {
    "figure_id": "F316",
    "report_id": "R015",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Much of CEEMEA and Asia have underperformed ytd)"
  },
  {
    "figure_id": "F317",
    "report_id": "R017",
    "label": "Figure 1",
    "context": "Figure 1: Chinese OEMs' annual market share in the NEV space in Europe"
  },
  {
    "figure_id": "F318",
    "report_id": "R017",
    "label": "Figure 3",
    "context": "Figure 3: BYD market share in Europe's NEV market (8% in Apr-26)"
  },
  {
    "figure_id": "F319",
    "report_id": "R017",
    "label": "Figure 2",
    "context": "Figure 2: Chinese OEMs' monthly market share in the NEV space in Europe"
  },
  {
    "figure_id": "F320",
    "report_id": "R017",
    "label": "Figure 4",
    "context": "Figure 4: MG (under SAIC) market share in Europe's NEV market (2% by Apr-26)"
  },
  {
    "figure_id": "F321",
    "report_id": "R017",
    "label": "Figure 3",
    "context": "Figure 3: BYD store in Paris (the bestselling BEV, Sealion 7, at an MSRP of \\~€48k or a monthly installment of \\~€800 and three months' wait time Exterior view of a modern white BYD electric vehicle on display at an auto show, w"
  },
  {
    "figure_id": "F322",
    "report_id": "R017",
    "label": "Figure 4",
    "context": "Figure 4: BYD store in London BYD BYD"
  },
  {
    "figure_id": "F323",
    "report_id": "R018",
    "label": "Figure 1",
    "context": "Figure 1: Centraline secondary asking price index vs. NBS secondary home price index M/M in tier-1 cities"
  },
  {
    "figure_id": "F324",
    "report_id": "R018",
    "label": "Figure 2",
    "context": "Figure 2: Centraline secondary manager confidence index in tier-1 cities vs. three-month rolling secondary sales"
  },
  {
    "figure_id": "F325",
    "report_id": "R018",
    "label": "Figure 3",
    "context": "Figure 3: 60-city weekly primary sales registrations – compared with 2019-24"
  },
  {
    "figure_id": "F326",
    "report_id": "R018",
    "label": "Figure 4",
    "context": "Figure 4: 60-city weekly primary sales registrations"
  },
  {
    "figure_id": "F327",
    "report_id": "R018",
    "label": "Figure 5",
    "context": "Figure 5: 12-city daily secondary sales registrations"
  },
  {
    "figure_id": "F328",
    "report_id": "R018",
    "label": "Figure 6",
    "context": "Figure 6: 12-city secondary sales registrations' seven-day moving average"
  },
  {
    "figure_id": "F329",
    "report_id": "R018",
    "label": "Figure 7",
    "context": "Figure 7: Tier-1 cities - secondary listings and inventory months"
  },
  {
    "figure_id": "F330",
    "report_id": "R018",
    "label": "Figure 8",
    "context": "Figure 8: Midland weekend appointment volume (in 15 housing estates)"
  },
  {
    "figure_id": "F331",
    "report_id": "R018",
    "label": "Figure 9",
    "context": "Figure 9: Centraline – No. of secondary listings (for sale)"
  },
  {
    "figure_id": "F332",
    "report_id": "R018",
    "label": "Figure 10",
    "context": "Figure 10: Hong Kong weekly secondary transactions in 35 major estates"
  },
  {
    "figure_id": "F333",
    "report_id": "R018",
    "label": "Figure 11",
    "context": "Figure 11: Hong Kong secondary home prices (Centa-city Leading Index, or CCL)"
  },
  {
    "figure_id": "F334",
    "report_id": "R018",
    "label": "Figure 12",
    "context": "Figure 12: Centa Valuation Index (CVI) vs. secondary home prices (CCL) 1m rolling W/W"
  },
  {
    "figure_id": "F335",
    "report_id": "R018",
    "label": "Figure 13",
    "context": "Figure 13: Centa-Salesman Index (CSI) vs. secondary home prices (CCL)"
  },
  {
    "figure_id": "F336",
    "report_id": "R018",
    "label": "Figure 14",
    "context": "Figure 14: Hong Kong seven-day rolling average total tourist arrivals minus resident departures"
  },
  {
    "figure_id": "F337",
    "report_id": "R018",
    "label": "Figure 15",
    "context": "Figure 15: Mainland China Property – Weekly share price performance (%)"
  },
  {
    "figure_id": "F338",
    "report_id": "R018",
    "label": "Figure 16",
    "context": "Figure 16: Hong Kong Property & Conglomerates – Weekly share price performance (%)"
  },
  {
    "figure_id": "F339",
    "report_id": "R018",
    "label": "Figure 17",
    "context": "Figure 17: Mainland China / Hong Kong Property & Conglomerates – Weekly share price performance by company type"
  },
  {
    "figure_id": "F340",
    "report_id": "R018",
    "label": "Figure 18",
    "context": "Figure 18: Short interest in Mainland China / Hong Kong Property – 30-day moving average"
  },
  {
    "figure_id": "F341",
    "report_id": "R018",
    "label": "Figure 19",
    "context": "Figure 19: HK property average southbound holdings as % of free float"
  },
  {
    "figure_id": "F342",
    "report_id": "R018",
    "label": "Figure 20",
    "context": "Figure 20: JACI China HY Property Index: Performance since 2026 (January 2026 = 100)"
  },
  {
    "figure_id": "F343",
    "report_id": "R019",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Primary weekly unit sales and four-week moving average – Total 50 cities"
  },
  {
    "figure_id": "F344",
    "report_id": "R022",
    "label": "Exhibit 1",
    "context": "Exhibit 1 - Weekly token consumption over the past 12 months as of 8 Jun (tn)"
  },
  {
    "figure_id": "F345",
    "report_id": "R022",
    "label": "Exhibit 3",
    "context": "Exhibit 3 - Weekly token consumption over the past 12 months as of 8 Jun (tn)"
  },
  {
    "figure_id": "F346",
    "report_id": "R022",
    "label": "Exhibit 4",
    "context": "Exhibit 4 - Market share: weekly token consumption by company as of 8 Jun"
  },
  {
    "figure_id": "F347",
    "report_id": "R022",
    "label": "Exhibit 5",
    "context": "Exhibit 5 - Weekly token consumption since Jan-26 (bn)"
  },
  {
    "figure_id": "F348",
    "report_id": "R022",
    "label": "Exhibit 8",
    "context": "Exhibit 8 - Cache hit/Input/Output API price for leading models as of 8 Jun"
  },
  {
    "figure_id": "F349",
    "report_id": "R022",
    "label": "Exhibit 9",
    "context": "Exhibit 9 - Intelligence index for top 20 models as of 8 Jun"
  },
  {
    "figure_id": "F350",
    "report_id": "R022",
    "label": "Exhibit 10",
    "context": "Exhibit 10 - Frontier Language Model Intelligence over time as of 8 Jun"
  },
  {
    "figure_id": "F351",
    "report_id": "R022",
    "label": "Exhibit 11",
    "context": "Exhibit 11 - Agentic index for top 20 models as of 8 Jun"
  },
  {
    "figure_id": "F352",
    "report_id": "R022",
    "label": "Exhibit 13",
    "context": "Exhibit 13 - Cost to run Artificial Intelligence Index as of 8 Jun"
  },
  {
    "figure_id": "F353",
    "report_id": "R022",
    "label": "Exhibit 12",
    "context": "Exhibit 12 - Coding index for top 20 models as of 8 Jun"
  },
  {
    "figure_id": "F354",
    "report_id": "R022",
    "label": "Exhibit 14",
    "context": "Exhibit 14 - Output speed to run Artificial Intelligence Index as of 8 Jun"
  },
  {
    "figure_id": "F355",
    "report_id": "R022",
    "label": "Exhibit 37",
    "context": "Exhibit 37 - Token consumption for OpenClaw (bn)"
  },
  {
    "figure_id": "F356",
    "report_id": "R022",
    "label": "Exhibit 39",
    "context": "Exhibit 39 - Top 15 models used by OpenClaw over the last 30 days (as of 8 Jun) Exhibit 38 - Token consumption for Hermes Agent (bn)"
  },
  {
    "figure_id": "F357",
    "report_id": "R022",
    "label": "Exhibit 41",
    "context": "Exhibit 41 - Global: Top 10 models by success rate as of 8 Jun"
  },
  {
    "figure_id": "F358",
    "report_id": "R022",
    "label": "Exhibit 42",
    "context": "Exhibit 42 - China: Top 10 models by success rate as of 8 Jun"
  },
  {
    "figure_id": "F359",
    "report_id": "R022",
    "label": "Exhibit 43",
    "context": "Exhibit 43 - Weekly DAU for leading AI Assistants in China (mn)"
  },
  {
    "figure_id": "F360",
    "report_id": "R022",
    "label": "Exhibit 45",
    "context": "Exhibit 45 - Weekly user time spent per weekly DAU for leading AI Assistants in China (mins)"
  },
  {
    "figure_id": "F361",
    "report_id": "R022",
    "label": "Exhibit 44",
    "context": "Exhibit 44 - Monthly DAU for Leading AI Assistants in China (mn)"
  },
  {
    "figure_id": "F362",
    "report_id": "R022",
    "label": "Exhibit 46",
    "context": "Exhibit 46 - Monthly user daily time spent per monthly DAU for leading AI Assistants in China (mins)"
  },
  {
    "figure_id": "F363",
    "report_id": "R022",
    "label": "Exhibit 51",
    "context": "Exhibit 51 - MAU for Taobao / PDD / JD in Apr-26"
  },
  {
    "figure_id": "F364",
    "report_id": "R022",
    "label": "Exhibit 52",
    "context": "Exhibit 52 - DAU for Taobao / PDD / JD in Apr-26"
  },
  {
    "figure_id": "F365",
    "report_id": "R022",
    "label": "Exhibit 53",
    "context": "Exhibit 53 - MAU for Meituan app in past 12 months"
  },
  {
    "figure_id": "F366",
    "report_id": "R022",
    "label": "Exhibit 54",
    "context": "Exhibit 54 - MAU for TME, Soda Music and NetEase Cloud Music in Apr-26"
  },
  {
    "figure_id": "F367",
    "report_id": "R022",
    "label": "Exhibit 55",
    "context": "Exhibit 55 - MAU for Soda Music in past 12 months"
  },
  {
    "figure_id": "F368",
    "report_id": "R022",
    "label": "Exhibit 56",
    "context": "Exhibit 56 - MAU for IQ, Tencent Video and Youku in Apr-26"
  },
  {
    "figure_id": "F369",
    "report_id": "R022",
    "label": "Exhibit 57",
    "context": "Exhibit 57 - DAU for Douyin over the past 12 months"
  },
  {
    "figure_id": "F370",
    "report_id": "R022",
    "label": "Exhibit 58",
    "context": "Exhibit 58 - MAU for BILI over the past 12 months"
  },
  {
    "figure_id": "F371",
    "report_id": "R022",
    "label": "Exhibit 59",
    "context": "Exhibit 59 - TCOM's MAU over the past 12 months"
  },
  {
    "figure_id": "F372",
    "report_id": "R022",
    "label": "Exhibit 60",
    "context": "Exhibit 60 - Weibo MAU over the past 12 months"
  },
  {
    "figure_id": "F373",
    "report_id": "R022",
    "label": "Exhibit 61",
    "context": "Exhibit 61 - Baidu MAU over the past 12 months"
  },
  {
    "figure_id": "F374",
    "report_id": "R022",
    "label": "Exhibit 62",
    "context": "Exhibit 62 - China's MaaS market monthly average daily token consumption in 2025"
  },
  {
    "figure_id": "F375",
    "report_id": "R022",
    "label": "Exhibit 64",
    "context": "Exhibit 64 - Market share of major vendors in China's MaaS market in 2025 (revenue basis)"
  },
  {
    "figure_id": "F376",
    "report_id": "R022",
    "label": "Exhibit 66",
    "context": "Exhibit 66 - The most important factors that drive people's decision to deploy model widely"
  },
  {
    "figure_id": "F377",
    "report_id": "R022",
    "label": "Exhibit 63",
    "context": "Exhibit 63 - China's MaaS market share by token consumption in 2025"
  },
  {
    "figure_id": "F378",
    "report_id": "R022",
    "label": "Exhibit 65",
    "context": "Exhibit 65 - Market share of major vendors in China's private large model platform market in 2025 (revenue basis)"
  },
  {
    "figure_id": "F379",
    "report_id": "R022",
    "label": "Exhibit 69",
    "context": "Exhibit 69 - Global AI code tools market size (USDbn)"
  },
  {
    "figure_id": "F380",
    "report_id": "R022",
    "label": "Exhibit 70",
    "context": "Exhibit 70 - China AI code generation market size by service type (RMBbn)"
  },
  {
    "figure_id": "F381",
    "report_id": "R022",
    "label": "Exhibit 71",
    "context": "Exhibit 71 - China AI code penetration in different industries"
  },
  {
    "figure_id": "F382",
    "report_id": "R022",
    "label": "Exhibit 72",
    "context": "Exhibit 72 - China AI + Workspace Market Size"
  },
  {
    "figure_id": "F383",
    "report_id": "R022",
    "label": "Exhibit 73",
    "context": "Exhibit 73 - Generative AI in Content Creation Market Size 2025 to 2035 (USD bn)"
  },
  {
    "figure_id": "F384",
    "report_id": "R022",
    "label": "Exhibit 74",
    "context": "Exhibit 74 - Daily token consumption in China by enterprises in 2H25 vs 1H25 (tn)"
  },
  {
    "figure_id": "F385",
    "report_id": "R022",
    "label": "Exhibit 75",
    "context": "Exhibit 75 - Market share in terms of tokens used among enterprises in 1H25"
  },
  {
    "figure_id": "F386",
    "report_id": "R022",
    "label": "Exhibit 76",
    "context": "Exhibit 76 - Market share in terms of tokens used among enterprises in 2H25"
  },
  {
    "figure_id": "F387",
    "report_id": "R022",
    "label": "Exhibit 77",
    "context": "Exhibit 77 - Market size of China LLM (RMB billions)"
  },
  {
    "figure_id": "F388",
    "report_id": "R022",
    "label": "Exhibit 78",
    "context": "Exhibit 78 - Market size of China Enterprise LLM (RMB billions)"
  },
  {
    "figure_id": "F389",
    "report_id": "R022",
    "label": "Exhibit 79",
    "context": "Exhibit 79 - ARR of Anthropic"
  },
  {
    "figure_id": "F390",
    "report_id": "R022",
    "label": "Exhibit 81",
    "context": "Exhibit 81 - OpenAI revenue between 2023 and 2030F (as of 3Q25)"
  },
  {
    "figure_id": "F391",
    "report_id": "R022",
    "label": "Exhibit 80",
    "context": "Exhibit 80 - ARR of OpenAI"
  },
  {
    "figure_id": "F392",
    "report_id": "R022",
    "label": "Exhibit 82",
    "context": "Exhibit 82 - Revenue mix of OpenAI between 2024 and 2030F (as of 3Q25)"
  },
  {
    "figure_id": "F393",
    "report_id": "R022",
    "label": "Exhibit 83",
    "context": "Exhibit 83 - MiniMax: % of OpenAI revenue over the next few years"
  },
  {
    "figure_id": "F394",
    "report_id": "R022",
    "label": "Exhibit 91",
    "context": "Exhibit 91 - China Daily token usage"
  },
  {
    "figure_id": "F395",
    "report_id": "R022",
    "label": "Exhibit 92",
    "context": "Exhibit 92 - Doubao daily token consumption"
  },
  {
    "figure_id": "F396",
    "report_id": "R022",
    "label": "Exhibit 93",
    "context": "Exhibit 93 - Token share by region"
  },
  {
    "figure_id": "F397",
    "report_id": "R023",
    "label": "Exhibit 1",
    "context": "Exhibit 1: MSe expects Hyperscaler capex/sales to surpass dot-com peaks reaching 44% in '27"
  },
  {
    "figure_id": "F398",
    "report_id": "R023",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Cons expects Hyperscaler capex to reach 45% of the R1000 in '27 and '28"
  },
  {
    "figure_id": "F399",
    "report_id": "R023",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Leases not yet started have hit"
  },
  {
    "figure_id": "F400",
    "report_id": "R023",
    "label": "Exhibit 4",
    "context": "Exhibit 4: ...while purchase commitments reach close to \\$1tn"
  },
  {
    "figure_id": "F401",
    "report_id": "R023",
    "label": "Exhibit 5",
    "context": "Exhibit 5: AI ecosystem has become increasingly interconnected.... ```mermaid graph TD"
  },
  {
    "figure_id": "F402",
    "report_id": "R023",
    "label": "Exhibit 6",
    "context": "``` Note: MSFT, and CRWV are covered by Josh Baer. ORCL is covered by Sanjit Singh. NVDA and AMD are covered by Joseph Moore. AMZN is covered by Brian Nowak. DIS is covered by Sean Diffley. Data as of 3/19/26."
  },
  {
    "figure_id": "F403",
    "report_id": "R024",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Industry-wide GB200/300 NVL72-equivalent monthly rack output, by major ODMs (2025) GB200/300 NVL72 racks by major ODMs (000s)"
  },
  {
    "figure_id": "F404",
    "report_id": "R024",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Industry-wide GB200/300 NVL72-equivalent monthly rack output, by major ODMs (2026) GB200/300 NVL72 racks by major ODMs (000s)"
  },
  {
    "figure_id": "F405",
    "report_id": "R024",
    "label": "Exhibit 3",
    "context": "GB200/300 NVL72 racks by major ODMs (000s)"
  },
  {
    "figure_id": "F406",
    "report_id": "R024",
    "label": "Exhibit 4",
    "context": "Exhibit 4: GB200/300 rack supply share, by major ODMs (2025) GB200/300 NVL72-equivalent rack supply share (2025)"
  },
  {
    "figure_id": "F407",
    "report_id": "R024",
    "label": "Exhibit 5",
    "context": "Exhibit 5: GB200/300 rack supply share, by major ODMs (2026) GB200/300 NVL72-equivalent rack supply share (2026)"
  },
  {
    "figure_id": "F408",
    "report_id": "R026",
    "label": "FIGURE 1",
    "context": "BCI, US FIGURE 1. Managed money positioning in oil is back to pre-war levels..."
  },
  {
    "figure_id": "F409",
    "report_id": "R026",
    "label": "FIGURE 2",
    "context": "Note: Net speculative positioning in Brent and WTI futures and options combined, percentile rank based on data since 2014. FIGURE 2. ...so is excess implied vol in oil markets"
  },
  {
    "figure_id": "F410",
    "report_id": "R026",
    "label": "Figure 3",
    "context": "Note: OVX minus VIX in standard deviation from mean since 2020 We reiterate that this is not a new equilibrium. The Strait cannot remain closed in perpetuity with oil prices at \\$100/b. Oil inventories continue to draw down, although the pace has not accelerat"
  },
  {
    "figure_id": "F411",
    "report_id": "R026",
    "label": "FIGURE 4",
    "context": "Note: Our weekly global total oil inventory indicator excluding the Middle East Gulf region minus the pre-pandemic seasonal average (2017-19), mb FIGURE 4. ...but the pace has not accelerated because of the pull back in Chinese demand"
  },
  {
    "figure_id": "F412",
    "report_id": "R026",
    "label": "Figure 4",
    "context": "The biggest surprise relative to the scenarios we laid out in late-March has been a sharp decline in Chinese oil demand (Figure 4). In April, China's oil demand was down 12% y/y but was still up 2% y/y for the first four months of 2026. Most market participant"
  },
  {
    "figure_id": "F413",
    "report_id": "R026",
    "label": "FIGURE 6",
    "context": "Note: China's crude oil inventories, bb FIGURE 6. US commercial crude oil inventories have been tightening under the surface"
  },
  {
    "figure_id": "F414",
    "report_id": "R026",
    "label": "Figure 6",
    "context": "Note: Change in US commercial crude oil inventories since 2008, mb The flip side is that in the US, which has driven a large majority of all supply growth for the past several years, commercial crude oil inventories, adjusted for the decline in SPR and the inc"
  },
  {
    "figure_id": "F415",
    "report_id": "R026",
    "label": "FIGURE 8",
    "context": "NOte: US commercial crude oil inventories in days of refining demand FIGURE 8. Cushing storage utilization has been declining fast"
  },
  {
    "figure_id": "F416",
    "report_id": "R027",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Consumer sentiment fell in June reversing the small rise in May"
  },
  {
    "figure_id": "F417",
    "report_id": "R028",
    "label": "Figure 2",
    "context": "Figure 2: Building new starts growth"
  },
  {
    "figure_id": "F418",
    "report_id": "R028",
    "label": "Figure 3",
    "context": "Figure 3: Building completions growth"
  },
  {
    "figure_id": "F419",
    "report_id": "R028",
    "label": "Figure 4",
    "context": "Figure 4: Investment in power generation Percent change, yoy"
  },
  {
    "figure_id": "F420",
    "report_id": "R028",
    "label": "Figure 6",
    "context": "Figure 6: Solar power plant capacity additions LHS: Gigawatts; RHS: Percent change, YTD yoy"
  },
  {
    "figure_id": "F421",
    "report_id": "R028",
    "label": "Figure 8",
    "context": "Figure 8: Wind power plant capacity additions LHS: Gigawatts; RHS: Percent change, yoy"
  },
  {
    "figure_id": "F422",
    "report_id": "R028",
    "label": "Figure 5",
    "context": "Figure 5: Fixed asset investment in grid infrastructure Percent change, yoy"
  },
  {
    "figure_id": "F423",
    "report_id": "R028",
    "label": "Figure 7",
    "context": "Figure 7: Solar power plant capacity addition growth Percent change, yoy"
  },
  {
    "figure_id": "F424",
    "report_id": "R028",
    "label": "Figure 9",
    "context": "Figure 9: Wind power plant capacity addition growth Percent change, yoy"
  },
  {
    "figure_id": "F425",
    "report_id": "R028",
    "label": "Figure 10",
    "context": "Figure 10: Cumulative wind installed capacity LHS: Gigawatts; RHS: Percent change, yoy of monthly installations"
  },
  {
    "figure_id": "F426",
    "report_id": "R028",
    "label": "Figure 12",
    "context": "Figure 12: Air conditioner production, monthly Thousand units"
  },
  {
    "figure_id": "F427",
    "report_id": "R028",
    "label": "Figure 14",
    "context": "Figure 14: Fridge and freezer production, monthly Thousand units"
  },
  {
    "figure_id": "F428",
    "report_id": "R028",
    "label": "Figure 11",
    "context": "Figure 11: Cumulative solar installed capacity LHS: Gigawatts; RHS: Percent change, yoy of monthly installations"
  },
  {
    "figure_id": "F429",
    "report_id": "R028",
    "label": "Figure 13",
    "context": "Figure 13: Air conditioner production growth Percent change, yoy"
  },
  {
    "figure_id": "F430",
    "report_id": "R028",
    "label": "Figure 15",
    "context": "Figure 15: Fridge and freezer production growth Percent change, yoy"
  },
  {
    "figure_id": "F431",
    "report_id": "R028",
    "label": "Figure 16",
    "context": "Figure 16: Washing machine production, monthly"
  },
  {
    "figure_id": "F432",
    "report_id": "R028",
    "label": "Figure 18",
    "context": "Figure 18: Passenger vehicle production growth"
  },
  {
    "figure_id": "F433",
    "report_id": "R028",
    "label": "Figure 20",
    "context": "Figure 20: Industrial robot production growth"
  },
  {
    "figure_id": "F434",
    "report_id": "R028",
    "label": "Figure 17",
    "context": "Figure 17: Washing machine production growth"
  },
  {
    "figure_id": "F435",
    "report_id": "R028",
    "label": "Figure 19",
    "context": "Figure 19: Passenger NEV production growth"
  },
  {
    "figure_id": "F436",
    "report_id": "R028",
    "label": "Figure 21",
    "context": "Figure 21: Excavator production growth"
  },
  {
    "figure_id": "F437",
    "report_id": "R028",
    "label": "Figure 22",
    "context": "Figure 22: Consumption-weighted end use indicator for Chinese copper demand growth"
  },
  {
    "figure_id": "F438",
    "report_id": "R028",
    "label": "Figure 24",
    "context": "Figure 24: YoY Growth – Consumption-weighted end use copper demand indicator vs apparent demand"
  },
  {
    "figure_id": "F439",
    "report_id": "R028",
    "label": "Figure 23",
    "context": "Figure 23: China copper apparent demand growth Percent change"
  },
  {
    "figure_id": "F440",
    "report_id": "R028",
    "label": "Figure 25",
    "context": "Figure 25: YTD YoY Growth – Consumption-weighted end use copper demand indicator vs apparent demand Percent change, YTD yoy"
  },
  {
    "figure_id": "F441",
    "report_id": "R028",
    "label": "Figure 26",
    "context": "Figure 26: China apparent copper demand"
  },
  {
    "figure_id": "F442",
    "report_id": "R028",
    "label": "Figure 28",
    "context": "Figure 28: Global visible copper inventories"
  },
  {
    "figure_id": "F443",
    "report_id": "R028",
    "label": "Figure 30",
    "context": "Figure 30: Total visible China copper inventory (SHFE + Bonded) Figure 27: China apparent copper demand"
  },
  {
    "figure_id": "F444",
    "report_id": "R028",
    "label": "Figure 29",
    "context": "Figure 29: Global visible copper inventory in days of use"
  },
  {
    "figure_id": "F445",
    "report_id": "R028",
    "label": "Figure 31",
    "context": "Figure 31: Copper regional premiums"
  },
  {
    "figure_id": "F446",
    "report_id": "R028",
    "label": "Figure 32",
    "context": "Figure 32: Monthly US refined copper imports"
  },
  {
    "figure_id": "F447",
    "report_id": "R028",
    "label": "Figure 36",
    "context": "Figure 36: China copper imported concentrate treatment charges vs annual benchmark"
  },
  {
    "figure_id": "F448",
    "report_id": "R028",
    "label": "Figure 33",
    "context": "Figure 33: Jul'26 COMEX/LME copper spread LHS: US\\$/mt, RHS: Percent of LME price (implied tariff rate) Figure 37: China copper concentrate imports Figure 34: Monthly US copper scrap exports"
  },
  {
    "figure_id": "F449",
    "report_id": "R028",
    "label": "Figure 35",
    "context": "Figure 35: Chinese spot copper import arbitrage and onshore spot premium/discount"
  },
  {
    "figure_id": "F450",
    "report_id": "R028",
    "label": "Figure 38",
    "context": "Figure 38: China refined copper imports LHS: Thousand mt; RHS: Percent change, yoy"
  },
  {
    "figure_id": "F451",
    "report_id": "R028",
    "label": "Figure 40",
    "context": "Figure 40: China contained copper scrap imports, 3mma LHS: Thousand mt (Cu contained); RHS: Percent change, yoy"
  },
  {
    "figure_id": "F452",
    "report_id": "R028",
    "label": "Figure 42",
    "context": "Figure 42: China refined copper production, monthly Thousand mt"
  },
  {
    "figure_id": "F453",
    "report_id": "R028",
    "label": "Figure 39",
    "context": "Figure 39: China refined copper exports vs LME 3-month copper price LHS: Thousand mt; RHS: US\\$/mt"
  },
  {
    "figure_id": "F454",
    "report_id": "R028",
    "label": "Figure 41",
    "context": "Figure 41: China copper imports of concentrate, cathode and contained scrap LHS: Thousand mt; RHS: Percent change, yoy"
  },
  {
    "figure_id": "F455",
    "report_id": "R028",
    "label": "Figure 43",
    "context": "Figure 43: Annualized China refined copper production LHS: Thousand mt; RHS: Percent change, yoy"
  },
  {
    "figure_id": "F456",
    "report_id": "R028",
    "label": "Figure 44",
    "context": "Figure 44: China copper wire and cable producer operating rates"
  },
  {
    "figure_id": "F457",
    "report_id": "R028",
    "label": "Figure 46",
    "context": "Figure 46: China copper tube producer operating rates"
  },
  {
    "figure_id": "F458",
    "report_id": "R028",
    "label": "Figure 48",
    "context": "Figure 48: Chile copper mine production"
  },
  {
    "figure_id": "F459",
    "report_id": "R028",
    "label": "Figure 45",
    "context": "Figure 45: China copper cathode-fed rod producer operating rates"
  },
  {
    "figure_id": "F460",
    "report_id": "R028",
    "label": "Figure 47",
    "context": "Figure 47: China copper flat-rolled producer operating rates"
  },
  {
    "figure_id": "F461",
    "report_id": "R028",
    "label": "Figure 49",
    "context": "Figure 49: Chile and Peru copper mine production, 12mma"
  },
  {
    "figure_id": "F462",
    "report_id": "R028",
    "label": "Figure 50",
    "context": "Figure 50: Chile copper mine production, monthly"
  },
  {
    "figure_id": "F463",
    "report_id": "R028",
    "label": "Figure 51",
    "context": "Figure 51: Peru copper mine production, monthly"
  },
  {
    "figure_id": "F464",
    "report_id": "R028",
    "label": "Figure 52",
    "context": "Figure 52: Global copper mining C1 + sustaining capex costs by %-tile and LME 3M copper price"
  },
  {
    "figure_id": "F465",
    "report_id": "R028",
    "label": "Figure 53",
    "context": "Figure 53: Global visible aluminium inventories"
  },
  {
    "figure_id": "F466",
    "report_id": "R028",
    "label": "Figure 57",
    "context": "Figure 57: China apparent aluminium demand"
  },
  {
    "figure_id": "F467",
    "report_id": "R028",
    "label": "Figure 56",
    "context": "Figure 56: Regional aluminium ingot premiums Figure 58: China apparent aluminium demand Figure 55: Total visible China aluminium inventory (SHFE + regional warehouses) Figure 54: Global visible aluminium inventory in days of use"
  },
  {
    "figure_id": "F468",
    "report_id": "R028",
    "label": "Figure 59",
    "context": "Figure 59: Chinese unwrought aluminium and aluminium product exports, 3-month rolling average"
  },
  {
    "figure_id": "F469",
    "report_id": "R028",
    "label": "Figure 61",
    "context": "Figure 61: China refined aluminium imports by region LHS: Thousand mt; RHS: Percent of total"
  },
  {
    "figure_id": "F470",
    "report_id": "R028",
    "label": "Figure 63",
    "context": "Figure 63: China aluminium wire & rod producer operating rates"
  },
  {
    "figure_id": "F471",
    "report_id": "R028",
    "label": "Figure 60",
    "context": "Figure 60: Chinese unwrought aluminium and aluminium product imports"
  },
  {
    "figure_id": "F472",
    "report_id": "R028",
    "label": "Figure 62",
    "context": "Figure 62: China aluminium profile producer operating rates"
  },
  {
    "figure_id": "F473",
    "report_id": "R028",
    "label": "Figure 64",
    "context": "Figure 64: China aluminium extrusions producer operating rates"
  },
  {
    "figure_id": "F474",
    "report_id": "R028",
    "label": "Figure 65",
    "context": "Figure 65: China total bauxite imports LHS: Million mt; RHS: Percent change yoy"
  },
  {
    "figure_id": "F475",
    "report_id": "R028",
    "label": "Figure 67",
    "context": "Figure 67: China alumina price"
  },
  {
    "figure_id": "F476",
    "report_id": "R028",
    "label": "Figure 69",
    "context": "Figure 69: China port inventory of bauxite and alumina"
  },
  {
    "figure_id": "F477",
    "report_id": "R028",
    "label": "Figure 66",
    "context": "Figure 66: China imports of bauxite from Guinea, 3-week ma"
  },
  {
    "figure_id": "F478",
    "report_id": "R028",
    "label": "Figure 68",
    "context": "Figure 68: China monthly alumina production LHS: Thousand mt; RHS: Percent change"
  },
  {
    "figure_id": "F479",
    "report_id": "R028",
    "label": "Figure 70",
    "context": "Figure 70: Annualized Chinese refined monthly aluminium production"
  },
  {
    "figure_id": "F480",
    "report_id": "R028",
    "label": "Figure 71",
    "context": "Figure 71: China aluminium ingot producer operating rates Percent"
  },
  {
    "figure_id": "F481",
    "report_id": "R028",
    "label": "Figure 72",
    "context": "Figure 72: China aluminium semis export arb proxy (China to rest of Asia)"
  },
  {
    "figure_id": "F482",
    "report_id": "R028",
    "label": "Figure 73",
    "context": "Figure 73: Global primary aluminium smelting C1 costs by %-tile and LME 3M aluminium price"
  },
  {
    "figure_id": "F483",
    "report_id": "R028",
    "label": "Figure 74",
    "context": "Figure 74: Global visible zinc inventories Thousand metric tonnes"
  },
  {
    "figure_id": "F484",
    "report_id": "R028",
    "label": "Figure 76",
    "context": "Figure 76: Total visible China zinc inventory (SHFE + Regional Warehouses) Y-axis: Thousand mt; X-axis: Weeks around Chinese New Year (0 = week closest to start of CNY)"
  },
  {
    "figure_id": "F485",
    "report_id": "R028",
    "label": "Figure 78",
    "context": "Figure 78: China apparent zinc demand LHS: Thousand mt; RHS: Percent change, yoy"
  },
  {
    "figure_id": "F486",
    "report_id": "R028",
    "label": "Figure 75",
    "context": "Figure 75: Global visible zinc inventories in days of use"
  },
  {
    "figure_id": "F487",
    "report_id": "R028",
    "label": "Figure 77",
    "context": "Figure 77: Regional zinc premiums US\\$/mt"
  },
  {
    "figure_id": "F488",
    "report_id": "R028",
    "label": "Figure 79",
    "context": "Figure 79: China apparent zinc demand Thousand mt"
  },
  {
    "figure_id": "F489",
    "report_id": "R028",
    "label": "Figure 80",
    "context": "Figure 80: China zinc spot concentrate treatment charges vs annual benchmark"
  },
  {
    "figure_id": "F490",
    "report_id": "R028",
    "label": "Figure 82",
    "context": "Figure 82: China zinc concentrate imports"
  },
  {
    "figure_id": "F491",
    "report_id": "R028",
    "label": "Figure 84",
    "context": "Figure 84: China refined zinc exports"
  },
  {
    "figure_id": "F492",
    "report_id": "R028",
    "label": "Figure 85",
    "context": "Figure 85: China zinc export arb proxy Figure 81: China net imports of refined zinc and China's zinc import arb"
  },
  {
    "figure_id": "F493",
    "report_id": "R028",
    "label": "Figure 83",
    "context": "Figure 83: China zinc ore port inventories"
  },
  {
    "figure_id": "F494",
    "report_id": "R028",
    "label": "Figure 86",
    "context": "Figure 86: China zinc galvanizers operating rates"
  },
  {
    "figure_id": "F495",
    "report_id": "R028",
    "label": "Figure 87",
    "context": "Figure 87: China monthly refined zinc production LHS: Thousand mt; RHS: Percent change yoy"
  },
  {
    "figure_id": "F496",
    "report_id": "R028",
    "label": "Figure 88",
    "context": "Figure 88: Global zinc C1 mining costs by %-tile and LME 3M copper price"
  },
  {
    "figure_id": "F497",
    "report_id": "R028",
    "label": "Figure 89",
    "context": "Figure 89: Global visible nickel inventory"
  },
  {
    "figure_id": "F498",
    "report_id": "R028",
    "label": "Figure 90",
    "context": "Figure 90: Global visible nickel inventory in days of use"
  },
  {
    "figure_id": "F499",
    "report_id": "R028",
    "label": "Figure 91",
    "context": "Figure 91: Chinese nickel pig iron prices (8-12%) and LME cash nickel prices"
  },
  {
    "figure_id": "F500",
    "report_id": "R028",
    "label": "Figure 92",
    "context": "Figure 92: Discount spread of NPI prices compared to LME cash nickel prices"
  },
  {
    "figure_id": "F501",
    "report_id": "R028",
    "label": "Figure 93",
    "context": "Figure 93: China monthly refined nickel imports and exports"
  },
  {
    "figure_id": "F502",
    "report_id": "R028",
    "label": "Figure 94",
    "context": "Figure 94: China monthly ferronickel and nickel ore imports"
  },
  {
    "figure_id": "F503",
    "report_id": "R028",
    "label": "Figure 95",
    "context": "Figure 95: Indonesia monthly nickel mine production LHS: Thousand mt; RHS: Percent change, yoy"
  },
  {
    "figure_id": "F504",
    "report_id": "R028",
    "label": "Figure 97",
    "context": "Figure 97: China stainless steel production"
  },
  {
    "figure_id": "F505",
    "report_id": "R028",
    "label": "Figure 99",
    "context": "Figure 99: Total visible China nickel inventory (SHFE + Regional Warehouses) Y-axis: Thousand mt; X-axis: Weeks around Chinese New Year (0 = week closest to start of CNY)"
  },
  {
    "figure_id": "F506",
    "report_id": "R028",
    "label": "Figure 96",
    "context": "Figure 96: Indonesia monthly refined nickel production LHS: Thousand mt; RHS: Percent change, yoy"
  },
  {
    "figure_id": "F507",
    "report_id": "R028",
    "label": "Figure 98",
    "context": "Figure 98: China nickel ore port inventory Million tonnes"
  },
  {
    "figure_id": "F508",
    "report_id": "R028",
    "label": "Figure 100",
    "context": "Figure 100: Global nickel industry C1 costs by %-tile and LME 3M nickel price"
  },
  {
    "figure_id": "F509",
    "report_id": "R029",
    "label": "Figure 1",
    "context": "Figure 1: State-based conflicts by region"
  },
  {
    "figure_id": "F510",
    "report_id": "R029",
    "label": "Figure 2",
    "context": "Figure 2: Global defense spending"
  },
  {
    "figure_id": "F511",
    "report_id": "R029",
    "label": "Figure 3",
    "context": "Figure 3: What is a kill chain? A kill chain is a structured process to detect, identify, and engage a target, then evaluate the results. One commonly used framework breaks this process into six steps: Find, Fix, Track, Target, En"
  },
  {
    "figure_id": "F512",
    "report_id": "R029",
    "label": "Figure 4",
    "context": "Figure 4: DoD's procurement process timeline"
  },
  {
    "figure_id": "F513",
    "report_id": "R029",
    "label": "Figure 5",
    "context": "More broadly, there are a handful of overarching issues with the current DIB that have been widely noted. - First, the production base—especially among tier-2 and tier-3 suppliers—has thinned dramatically. The specialized segments that produce castings, energy"
  },
  {
    "figure_id": "F514",
    "report_id": "R029",
    "label": "Figure 6",
    "context": "Figure 6: U.S. Defense Industrial Base Supply Chain Flow of products and services from raw materials suppliers (bottom) to the end-customer (top) Department of War Department of Energy Department of Homeland Security NASA"
  },
  {
    "figure_id": "F515",
    "report_id": "R029",
    "label": "Figure 7",
    "context": "Figure 7: RoRo shipbuilding orders at Chinese shipyards # of orders based on delivery year"
  },
  {
    "figure_id": "F516",
    "report_id": "R029",
    "label": "Figure 8",
    "context": "Figure 8: Chinese shipyards capacity Number of ships"
  },
  {
    "figure_id": "F517",
    "report_id": "R029",
    "label": "Figure 9",
    "context": "Figure 9: U.S. and Chinese naval warships Units"
  },
  {
    "figure_id": "F518",
    "report_id": "R029",
    "label": "Figure 10",
    "context": "Figure 10: U.S. Navy Tomahawk missiles"
  },
  {
    "figure_id": "F519",
    "report_id": "R029",
    "label": "Figure 11",
    "context": "Figure 11: Chinese missile launchers"
  },
  {
    "figure_id": "F520",
    "report_id": "R029",
    "label": "Figure 12",
    "context": "Figure 12: China's exports have a large defense-related component % of major goods exports"
  },
  {
    "figure_id": "F521",
    "report_id": "R029",
    "label": "Figure 13",
    "context": "Figure 13: DoD weapons and infrastructure supply chain that relies on Chinese semiconductors %"
  },
  {
    "figure_id": "F522",
    "report_id": "R029",
    "label": "Figure 14",
    "context": "Figure 14: Defense spending by Israel, South Korea and Sweden"
  },
  {
    "figure_id": "F523",
    "report_id": "R029",
    "label": "Figure 15",
    "context": "Figure 15: S. Korea arms and ammunition exports"
  },
  {
    "figure_id": "F524",
    "report_id": "R029",
    "label": "Figure 16",
    "context": "Figure 16: Defense spending by country"
  },
  {
    "figure_id": "F525",
    "report_id": "R029",
    "label": "Figure 17",
    "context": "Figure 17: Market share of leading arms exporters % of global exports, 2021-25"
  },
  {
    "figure_id": "F526",
    "report_id": "R029",
    "label": "Figure 18",
    "context": "Figure 18: Comparative analysis of U.S. and other DIBs Score, 1= worse, 5= best"
  },
  {
    "figure_id": "F527",
    "report_id": "R029",
    "label": "Figure 19",
    "context": "Figure 19: AI firms' share of economy-wide capex % (Publicly-listed AI firms' capex divided by total publicly-listed firms' capex)"
  },
  {
    "figure_id": "F528",
    "report_id": "R029",
    "label": "Figure 20",
    "context": "Figure 20: Military personnel"
  },
  {
    "figure_id": "F529",
    "report_id": "R029",
    "label": "Figure 21",
    "context": "Figure 21: Land assets"
  },
  {
    "figure_id": "F530",
    "report_id": "R029",
    "label": "Figure 22",
    "context": "Figure 22: Air assets Units"
  },
  {
    "figure_id": "F531",
    "report_id": "R029",
    "label": "Figure 23",
    "context": "Figure 23: Space military assets (satellites) Units"
  },
  {
    "figure_id": "F532",
    "report_id": "R029",
    "label": "Figure 24",
    "context": "Figure 24: Drone companies by country Number of companies"
  },
  {
    "figure_id": "F533",
    "report_id": "R029",
    "label": "Figure 25",
    "context": "Figure 25: Private capital invested by country US\\$ million"
  },
  {
    "figure_id": "F534",
    "report_id": "R029",
    "label": "Figure 26",
    "context": "Figure 26: Private capital in U.S. robotics and drones"
  },
  {
    "figure_id": "F535",
    "report_id": "R029",
    "label": "Figure 27",
    "context": "Figure 27: U.S. VC funding of robotics and drones"
  },
  {
    "figure_id": "F536",
    "report_id": "R029",
    "label": "Figure 28",
    "context": "Figure 28: U.S. marketed UAVs by group and company Number of UAVs"
  },
  {
    "figure_id": "F537",
    "report_id": "R029",
    "label": "Figure 29",
    "context": "Figure 29: The F-35, refueling mid-air Exterior view of a modern fighter jet in flight above Earth (no visible text or symbols)"
  },
  {
    "figure_id": "F538",
    "report_id": "R029",
    "label": "Figure 30",
    "context": "Figure 30: The Barracuda 500 Side view of a black submarine with yellow markings (no text or symbols visible) Barracuda-500"
  },
  {
    "figure_id": "F539",
    "report_id": "R032",
    "label": "FIGURE 1",
    "context": "- Our new Cloud server revenue estimates are \\$567Bn/\\$885Bn in CY26/27 vs our prior estimates of \\$585Bn/\\$817Bn, respectively. We model growth of 77% and 56% in 2026/2027 vs our prior estimates of 84% and 40%. xPU server estimates and updated segmentation fr"
  },
  {
    "figure_id": "F540",
    "report_id": "R032",
    "label": "FIGURE 2",
    "context": "We expect growth from Cloud and Enterprise servers moving through CY26-27. We find the Cloud growth impressive, given the large base it's growing from. Additionally, our Enterprise server growth this year accounts for the ASP increases along with continued vol"
  },
  {
    "figure_id": "F541",
    "report_id": "R032",
    "label": "FIGURE 3",
    "context": "AI has been a big positive for the server industry, with a focus on companies' growing AI server share and backlog. The Cloud server market has grown to multiples the size of the Enterprise server market, on a revenue basis. White box (inclusive of NVDA) conti"
  },
  {
    "figure_id": "F542",
    "report_id": "R032",
    "label": "FIGURE 4",
    "context": "However, once Enterprise/Inferencing and Sovereign AI ramp more meaningfully, we expect some share distribution towards branded players. FIGURE 4. Cloud Server Market by Vendor"
  },
  {
    "figure_id": "F543",
    "report_id": "R032",
    "label": "FIGURE 5",
    "context": "We entered the year under the assumption ASP increases would offset expected unit volume declines. However, ASP increases coupled with unit volumes holding in better than expected caused material upside to our estimates. Although we believe the majority of out"
  },
  {
    "figure_id": "F544",
    "report_id": "R034",
    "label": "Figure 1",
    "context": "Figure 1: Global memory makers' share price performance including SOX (Philadelphia Semiconductor index)"
  },
  {
    "figure_id": "F545",
    "report_id": "R035",
    "label": "Exhibit 1",
    "context": "Exhibit 1 - SW Baskets' EV/S - US vs CN"
  },
  {
    "figure_id": "F546",
    "report_id": "R035",
    "label": "Exhibit 2",
    "context": "Exhibit 2 - China SW EV/S Premium over China Internet"
  },
  {
    "figure_id": "F547",
    "report_id": "R035",
    "label": "Exhibit 3",
    "context": "Exhibit 3 - Ranking of China SW AI Defensibility"
  },
  {
    "figure_id": "F548",
    "report_id": "R035",
    "label": "Exhibit 4",
    "context": "Exhibit 4 - JEF SW coverage's AI moat and timeframe of AI transition"
  },
  {
    "figure_id": "F549",
    "report_id": "R035",
    "label": "Exhibit 5",
    "context": "Exhibit 5 - US SW Cohort's Mkt Cap Chg"
  },
  {
    "figure_id": "F550",
    "report_id": "R035",
    "label": "Exhibit 6",
    "context": "Exhibit 6 - CN SW Cohort's Mkt Cap Chg"
  },
  {
    "figure_id": "F551",
    "report_id": "R035",
    "label": "Exhibit 7",
    "context": "Exhibit 7 - US SW Cohort's Cons Rev Ests US SW Rev cons from Jan 12 - May 31: +2%"
  },
  {
    "figure_id": "F552",
    "report_id": "R035",
    "label": "Exhibit 8",
    "context": "Exhibit 8 - CN SW Cohort's Cons Rev Ests CN SW Rev cons from Jan 12 - May 31: -5%"
  },
  {
    "figure_id": "F553",
    "report_id": "R035",
    "label": "Exhibit 9",
    "context": "Exhibit 9 - SW Companies EV/S - US vs CN"
  },
  {
    "figure_id": "F554",
    "report_id": "R035",
    "label": "Exhibit 10",
    "context": "Exhibit 10 - China SW EV/S Premium over China Internet"
  },
  {
    "figure_id": "F555",
    "report_id": "R035",
    "label": "Exhibit 13",
    "context": "Exhibit 13 - The Architectural Paradigm Shift: From SW-as-tool to SW-as-digital-labor Traditional Software/ SaaS ```mermaid graph LR"
  },
  {
    "figure_id": "F556",
    "report_id": "R035",
    "label": "Exhibit 14",
    "context": "Exhibit 14 - AI will drive consumption-based or outcome-based monetization from Software ```mermaid graph LR"
  },
  {
    "figure_id": "F557",
    "report_id": "R035",
    "label": "Exhibit 15",
    "context": "Exhibit 15 - JEF SW coverage's AI moat and timeframe of AI transition"
  },
  {
    "figure_id": "F558",
    "report_id": "R035",
    "label": "Exhibit 16",
    "context": "Exhibit 16 - Artificial Analysis AI model Intelligence index"
  },
  {
    "figure_id": "F559",
    "report_id": "R035",
    "label": "Exhibit 17",
    "context": "Exhibit 17 - Intelligence Score of Leading AI Labs' Models"
  },
  {
    "figure_id": "F560",
    "report_id": "R035",
    "label": "Exhibit 18",
    "context": "Exhibit 18 - Frontier Language Model Intelligence China vs. US"
  },
  {
    "figure_id": "F561",
    "report_id": "R035",
    "label": "Exhibit 19",
    "context": "Exhibit 19 - Frontier Language Model Intelligence China vs. US"
  },
  {
    "figure_id": "F562",
    "report_id": "R035",
    "label": "Exhibit 20",
    "context": "Exhibit 20 - Token Usage Share by Vendors"
  },
  {
    "figure_id": "F563",
    "report_id": "R035",
    "label": "Exhibit 21",
    "context": "Exhibit 21 - Frontier Model Price - New vs previous models"
  },
  {
    "figure_id": "F564",
    "report_id": "R035",
    "label": "Exhibit 22",
    "context": "Exhibit 22 - CH Frontier Model Price As % of US'"
  },
  {
    "figure_id": "F565",
    "report_id": "R035",
    "label": "Exhibit 23",
    "context": "Exhibit 23 - Frontier Model Price - US vs. CN"
  },
  {
    "figure_id": "F566",
    "report_id": "R035",
    "label": "Exhibit 24",
    "context": "Exhibit 24 - API Price vs. Model Intelligence"
  },
  {
    "figure_id": "F567",
    "report_id": "R035",
    "label": "Exhibit 25",
    "context": "Exhibit 25 - LLM Intelligence per Dollar"
  },
  {
    "figure_id": "F568",
    "report_id": "R036",
    "label": "Exhibit 4",
    "context": "Exhibit 4: NTM EV/EBITDA for AMZN/GOOGL/META vs. Historical Averages Exhibit 5: Internet names fell -5% last week (SPX/NDX -3/-5%)"
  },
  {
    "figure_id": "F569",
    "report_id": "R036",
    "label": "Exhibit 6",
    "context": "Exhibit 6: NTM EV/EBITDA Multiples Are -4%/-9% vs. 5/10-Year Averages..."
  },
  {
    "figure_id": "F570",
    "report_id": "R036",
    "label": "Exhibit 7",
    "context": "Exhibit 7: ... and NTM EV/Sales Multiples Are +21%/+24% vs. 5/10-Year Averages"
  },
  {
    "figure_id": "F571",
    "report_id": "R036",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Digital Media: Treating SBC as Cash Increases EV/EBITDA Multiples by \\~36%, on Average Digital Media"
  },
  {
    "figure_id": "F572",
    "report_id": "R036",
    "label": "Exhibit 9",
    "context": "Exhibit 9: eCommerce: Treating SBC as Cash Increases EV/EBITDA Multiples by \\~30%, on Average ecommerce"
  },
  {
    "figure_id": "F573",
    "report_id": "R036",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Video Games: Treating SBC as Cash Increases EV/EBITDA Multiples by \\~17%, on Average Video Games"
  },
  {
    "figure_id": "F574",
    "report_id": "R036",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Travel / Shared Economy / Real Estate Tech: Treating SBC as Cash Increases EV/EBITDA Multiples by \\~44%, on Average Travel / Shared Economy + Real Estate Tech"
  },
  {
    "figure_id": "F575",
    "report_id": "R038",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Memory/Storage Hierarchy for AI At the heart of AI is data, which resides in Memory and Storage"
  },
  {
    "figure_id": "F576",
    "report_id": "R038",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: AI Demand for Memory & Storage AI is driving unprecedented demand surge in Memory & Storage"
  },
  {
    "figure_id": "F577",
    "report_id": "R038",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: Data Center Mix for NAND, DRAM, and HDD ## Less price sensitive Data Center customers now dominate demand NAND"
  },
  {
    "figure_id": "F578",
    "report_id": "R038",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: 2013/2014 Black Book on the New Memory Paradigm ## Is the New Memory Paradigm back? Bernstein's 2013/2014 Black Book on the New Memory Paradigm Bernstein BERNSTEIN GLOBAL VIEW Global Memory: A New Paradigm MAY 2013"
  },
  {
    "figure_id": "F579",
    "report_id": "R038",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: DRAM Structural Supply Growth vs. Demand Growth today ## Technology driven supply constraint has played out in DRAM DRAM Structural Supply Growth vs. Demand Growth today"
  },
  {
    "figure_id": "F580",
    "report_id": "R038",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: Industry Concentration Across Memory/Storage Segments ## Memory/Storage segments have consolidated: HDD is the highest concentration, followed by DRAM and NAND HHI Index – measurement of industry concentration"
  },
  {
    "figure_id": "F581",
    "report_id": "R038",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: DRAM Gross Margin DRAM: Higher highs and Higher lows should continue"
  },
  {
    "figure_id": "F582",
    "report_id": "R038",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: NAND Structural Supply Growth vs. Demand Growth today # 3D NAND adoption led to an explosion of NAND supply – this is now finally reaching diminishing returns NAND Structural Supply Growth vs. Demand Growth today NAND"
  },
  {
    "figure_id": "F583",
    "report_id": "R038",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: NAND Industry Gross Margin ## NAND: Return of the New Memory Paradigm should signal higher highs and higher lows going forward NAND Industry Gross Margin"
  },
  {
    "figure_id": "F584",
    "report_id": "R038",
    "label": "EXHIBIT 13",
    "context": "EXHIBIT 13: DRAM, NAND Flash Capex Spending ## NAND is earlier cycle vs. DRAM, with minimal capex response so far Capex Spending (\\$mn)"
  },
  {
    "figure_id": "F585",
    "report_id": "R038",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: HDD Industry Total Revenue ## HDD: Both consolidated and growing for the first time in history"
  },
  {
    "figure_id": "F586",
    "report_id": "R038",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: HDD Industry Gross Margin HDD: As a result we should also see sustainably higher margins HDD Industry Gross Margin"
  },
  {
    "figure_id": "F587",
    "report_id": "R038",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 16: Average Selling Price per GB ## Cyclicality should be dampened by LTA Our calc. on LTA floor pricing suggests only $10\\%$ discount to projected Jun'26 ASP"
  },
  {
    "figure_id": "F588",
    "report_id": "R038",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 17: Memory/Storage P/FE Memory stocks valuation suggest market priced in boom-bust Memory/Storage P/FE"
  },
  {
    "figure_id": "F589",
    "report_id": "R039",
    "label": "Figure 1",
    "context": "Not for distribution in the People's Republic of China, excluding the Hong Kong Special Administrative Region and Qualified Foreign Institutional Investors. comprising Rmb647m won by Pinggao which ranked No. 2 among all companies participating in the biddings."
  },
  {
    "figure_id": "F590",
    "report_id": "R040",
    "label": "FIGURE 1",
    "context": "## The AI Capex Cycle Begins to Overwhelm Operating Cash Flows The AI investment cycle continues to defy traditional capital intensity frameworks. Following the latest spending commitments, we believe peak capex has been deferred further out, reflecting both p"
  },
  {
    "figure_id": "F591",
    "report_id": "R040",
    "label": "FIGURE 2",
    "context": "BARC Estimates $1,160 From AI's S-Curve Is Steepening (1 June 2026). FIGURE 2. ...which is \\~26% above the Street..."
  },
  {
    "figure_id": "F592",
    "report_id": "R040",
    "label": "FIGURE 3",
    "context": "FIGURE 3. ...driving operating cash flow pressure that we expect to intensify into 2028... Capex/OCF"
  },
  {
    "figure_id": "F593",
    "report_id": "R040",
    "label": "FIGURE 4",
    "context": "BARC Estimates Estimates from BARC' Internet research team. Note that for AMZN, capex is AWS only, while OCF is total AMZN. FIGURE 4. ...which is not baked into consensus estimates Capex/OCF"
  },
  {
    "figure_id": "F594",
    "report_id": "R040",
    "label": "FIGURE 5",
    "context": "## Converts as the Capital-Structure Bridge for the AI Capex Cycle The AI infrastructure funding debate is no longer just debt versus equity; it is about which form of capital best preserves balance-sheet flexibility while allowing hyperscalers to keep investi"
  },
  {
    "figure_id": "F595",
    "report_id": "R040",
    "label": "FIGURE 6",
    "context": "FIGURE 6. AI-related convert issuance has become a major"
  },
  {
    "figure_id": "F596",
    "report_id": "R040",
    "label": "FIGURE 7",
    "context": "\\$16.75bn dual-tranche mandatory convertible is therefore not an isolated transaction; it underscores how equity-linked capital is becoming a larger part of the AI capex funding toolkit. ## Why Equity-Linked Capital, Not Just Straight Debt? The reason to issue"
  },
  {
    "figure_id": "F597",
    "report_id": "R041",
    "label": "Exhibit 1",
    "context": "Exhibit 1: PC vs BSL AAAs widened to 32bp over the 3 months ending in May"
  },
  {
    "figure_id": "F598",
    "report_id": "R041",
    "label": "Exhibit 2",
    "context": "Exhibit 2: PC vs BSL AAAs widened to 32bp over the 3 months ending in May"
  },
  {
    "figure_id": "F599",
    "report_id": "R041",
    "label": "Exhibit 3",
    "context": "Exhibit 3: PC vs BSL BBBs widened to levels last seen two years ago"
  },
  {
    "figure_id": "F600",
    "report_id": "R041",
    "label": "Exhibit 4",
    "context": "Exhibit 4: In US NI AAAs screen cheaper to AAs and As %-Tile Range of US CLO Spreads in Primary Market (2016-Nov)"
  },
  {
    "figure_id": "F601",
    "report_id": "R041",
    "label": "Exhibit 5",
    "context": "Exhibit 5: In Europe, NI AAAs screen relatively cheaper, tracking \\~45th %-tile Percentile of EU CLO NI spreads(inc floor) versus 10 year range"
  },
  {
    "figure_id": "F602",
    "report_id": "R041",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Monthly CLO Creation (New Issue and Refis/Resets)"
  },
  {
    "figure_id": "F603",
    "report_id": "R041",
    "label": "Exhibit 12",
    "context": "Exhibit 12: New Issue US CLO Arb"
  },
  {
    "figure_id": "F604",
    "report_id": "R041",
    "label": "Exhibit 13",
    "context": "Exhibit 13: New Issue EU CLO Arb"
  },
  {
    "figure_id": "F605",
    "report_id": "R041",
    "label": "Exhibit 14",
    "context": "Exhibit 14: US CLO vs. IG Corp 24-month Z-Score"
  },
  {
    "figure_id": "F606",
    "report_id": "R041",
    "label": "Exhibit 15",
    "context": "Exhibit 15: US CLO vs. HY Corp & Loans 24-month Z-Score"
  },
  {
    "figure_id": "F607",
    "report_id": "R041",
    "label": "Exhibit 16",
    "context": "Exhibit 16: EU CLO vs. IG Corp 24-month Z-Score"
  },
  {
    "figure_id": "F608",
    "report_id": "R041",
    "label": "Exhibit 17",
    "context": "Exhibit 17: EU CLO vs. HY Corp & Loans 24-month Z-Score"
  },
  {
    "figure_id": "F609",
    "report_id": "R041",
    "label": "Exhibit 18",
    "context": "Exhibit 18: FX-hedged and unhedged generic US CLO yields\\* for JPY-funded investors"
  },
  {
    "figure_id": "F610",
    "report_id": "R041",
    "label": "Exhibit 19",
    "context": "Exhibit 19: FX-hedged and unhedged generic European CLO yields\\* for JPY-funded investors"
  },
  {
    "figure_id": "F611",
    "report_id": "R041",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Monthly IG-rated CLO/CDO Trading Volume - TRACE"
  },
  {
    "figure_id": "F612",
    "report_id": "R041",
    "label": "Exhibit 21",
    "context": "Exhibit 21: Monthly BIG-rated CLO/CDO Trading Volume - TRACE"
  },
  {
    "figure_id": "F613",
    "report_id": "R041",
    "label": "Exhibit 22",
    "context": "Exhibit 22: Monthly CLO BWIC Volume"
  },
  {
    "figure_id": "F614",
    "report_id": "R041",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Initial AAA Par Sub by Issuance Vintage Exhibit 24: Median US CLO Junior OC Cushions"
  },
  {
    "figure_id": "F615",
    "report_id": "R041",
    "label": "Exhibit 25",
    "context": "Exhibit 25: Median European CLO Junior OC Cushions"
  },
  {
    "figure_id": "F616",
    "report_id": "R041",
    "label": "Exhibit 27",
    "context": "Exhibit 27: OC Test Failures and Deferred Interest in April 2026"
  },
  {
    "figure_id": "F617",
    "report_id": "R041",
    "label": "Exhibit 28",
    "context": "Exhibit 28: Median US CLO 2.0 CCC Assets by Vintage"
  },
  {
    "figure_id": "F618",
    "report_id": "R041",
    "label": "Exhibit 29",
    "context": "Exhibit 29: Vintage Median %CCC in CLO Portfolios Exhibit 30: Median CCC Assets in CLO Portfolios"
  },
  {
    "figure_id": "F619",
    "report_id": "R041",
    "label": "Exhibit 33",
    "context": "Exhibit 33: CLO 2.0 Equity NAV Percentiles"
  },
  {
    "figure_id": "F620",
    "report_id": "R041",
    "label": "Exhibit 34",
    "context": "Exhibit 34: European CLO 2.0 Equity NAV Percentiles"
  },
  {
    "figure_id": "F621",
    "report_id": "R041",
    "label": "Exhibit 36",
    "context": "Exhibit 36: US Leveraged Debt Maturity Profile"
  },
  {
    "figure_id": "F622",
    "report_id": "R041",
    "label": "Exhibit 37",
    "context": "Exhibit 37: Spot and Forward 3m Libor"
  },
  {
    "figure_id": "F623",
    "report_id": "R041",
    "label": "Exhibit 38",
    "context": "Exhibit 38: Collateral Trading Below 90 in US & EU CLO Portfolios"
  },
  {
    "figure_id": "F624",
    "report_id": "R041",
    "label": "Exhibit 39",
    "context": "Exhibit 39: US Collateral Holdings Below 90 by Vintage Year"
  },
  {
    "figure_id": "F625",
    "report_id": "R041",
    "label": "Exhibit 40",
    "context": "Exhibit 40: EU Collateral Holdings Below 90 by Vintage Year"
  },
  {
    "figure_id": "F626",
    "report_id": "R041",
    "label": "Exhibit 41",
    "context": "Exhibit 41: US Loan Index Bid Price & % Priced at or Above Par"
  },
  {
    "figure_id": "F627",
    "report_id": "R041",
    "label": "Exhibit 42",
    "context": "Exhibit 42: Eur. Loan Index Bid Price & % Priced at or Above Par"
  },
  {
    "figure_id": "F628",
    "report_id": "R041",
    "label": "Exhibit 43",
    "context": "Exhibit 43: Median US CLO Port. Prices & LTM TR Volatilities"
  },
  {
    "figure_id": "F629",
    "report_id": "R041",
    "label": "Exhibit 44",
    "context": "Exhibit 44: Median Eur. CLO Collat. Prices & LTM TR Volatilities"
  },
  {
    "figure_id": "F630",
    "report_id": "R041",
    "label": "Exhibit 45",
    "context": "Exhibit 45: S&P LSTA Loan Index Upgrades vs. Downgrades"
  },
  {
    "figure_id": "F631",
    "report_id": "R041",
    "label": "Exhibit 46",
    "context": "Exhibit 46: Leveraged Loan Default Rates LTM (Principal Amount)"
  },
  {
    "figure_id": "F632",
    "report_id": "R041",
    "label": "Exhibit 47",
    "context": "Exhibit 47: Monthly Leveraged Loan Repayment Rates"
  },
  {
    "figure_id": "F633",
    "report_id": "R041",
    "label": "Exhibit 48",
    "context": "Exhibit 48: Historical US Corporate Bond and Loan Recoveries"
  },
  {
    "figure_id": "F634",
    "report_id": "R041",
    "label": "Exhibit 49",
    "context": "Exhibit 49: Par Amount of Outstanding Leveraged Loans"
  },
  {
    "figure_id": "F635",
    "report_id": "R041",
    "label": "Exhibit 50",
    "context": "Exhibit 50: US Loan Funds Flows and Fed Funds Rate"
  },
  {
    "figure_id": "F636",
    "report_id": "R041",
    "label": "Exhibit 51",
    "context": "Exhibit 51: US Leveraged Loan Issuance and CLO Issuance"
  },
  {
    "figure_id": "F637",
    "report_id": "R041",
    "label": "Exhibit 52",
    "context": "Exhibit 52: % New Issue First Lien US Leveraged Loans with Libor Floors and Level"
  },
  {
    "figure_id": "F638",
    "report_id": "R042",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Australia Exports a Significant Share of Key Commodities Share of Global Seaborne Supply"
  },
  {
    "figure_id": "F639",
    "report_id": "R042",
    "label": "Exhibit 5",
    "context": "Exhibit 5: EBITDA margins of ASX miners in our coverage CY2026 EBITDA Margin"
  },
  {
    "figure_id": "F640",
    "report_id": "R042",
    "label": "Exhibit 6",
    "context": "Exhibit 6: P/E ratios of ASX miners in our coverage PE Ratio"
  },
  {
    "figure_id": "F641",
    "report_id": "R042",
    "label": "Exhibit 7",
    "context": "Exhibit 7: FCF margin of ASX miners in our coverage FCF Margin"
  },
  {
    "figure_id": "F642",
    "report_id": "R042",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Net debt/EBITDA of ASX miners in our coverage"
  },
  {
    "figure_id": "F643",
    "report_id": "R042",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Dividend yield of ASX miners in our coverage Div Yield (%)"
  },
  {
    "figure_id": "F644",
    "report_id": "R042",
    "label": "Exhibit 10",
    "context": "Exhibit 10: 2026e P/B vs. ROE of ASX miners in our coverage"
  },
  {
    "figure_id": "F645",
    "report_id": "R042",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Commodity Revenue Exposure of Australian Coverage"
  },
  {
    "figure_id": "F646",
    "report_id": "R042",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Commodity Revenue Exposure of Australian Coverage"
  },
  {
    "figure_id": "F647",
    "report_id": "R042",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Next 12 months EV/EBITDA: Bottom-up mining and industrials indices"
  },
  {
    "figure_id": "F648",
    "report_id": "R042",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Next 12 months P/B: Mining and industrials indices"
  },
  {
    "figure_id": "F649",
    "report_id": "R042",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Next 12 months dividend yield: Bottom-up mining and industrials indices"
  },
  {
    "figure_id": "F650",
    "report_id": "R042",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Next 12 months P/E: Bottom-up mining and industrials indices"
  },
  {
    "figure_id": "F651",
    "report_id": "R042",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Next 12 months FCF yield: Bottom-up mining and industrials indices"
  },
  {
    "figure_id": "F652",
    "report_id": "R042",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Next 12 months ROE: Bottom-up mining and industrials indices"
  },
  {
    "figure_id": "F653",
    "report_id": "R042",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Next 12 months relative EV/EBITDA: Bottom-up mining and industrials indices"
  },
  {
    "figure_id": "F654",
    "report_id": "R042",
    "label": "Exhibit 21",
    "context": "Exhibit 21: Next 12 months relative P/B: Mining and industrials indices"
  },
  {
    "figure_id": "F655",
    "report_id": "R042",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Next 12 months relative dividend yield: Bottom-up mining and industrials indices"
  },
  {
    "figure_id": "F656",
    "report_id": "R042",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Next 12 months relative P/E: Bottom-up mining and industrials indices"
  },
  {
    "figure_id": "F657",
    "report_id": "R042",
    "label": "Exhibit 22",
    "context": "Exhibit 22: Next 12 months relative FCF yield: Bottom-up mining and industrials indices"
  },
  {
    "figure_id": "F658",
    "report_id": "R042",
    "label": "Exhibit 24",
    "context": "Exhibit 24: Next 12 months relative ROE: Bottom-up mining and industrials indices"
  },
  {
    "figure_id": "F659",
    "report_id": "R042",
    "label": "Exhibit 25",
    "context": "Exhibit 25: Relative EV/EBITDA: Australia vs. Global Mining"
  },
  {
    "figure_id": "F660",
    "report_id": "R042",
    "label": "Exhibit 26",
    "context": "Exhibit 26: Relative P/E: Australia vs. Global Mining"
  },
  {
    "figure_id": "F661",
    "report_id": "R042",
    "label": "Exhibit 27",
    "context": "Exhibit 27: Relative P/B: Australia vs. Global Mining"
  },
  {
    "figure_id": "F662",
    "report_id": "R042",
    "label": "Exhibit 28",
    "context": "Exhibit 28: Relative FCF Yield: Australia vs. Global Mining"
  },
  {
    "figure_id": "F663",
    "report_id": "R042",
    "label": "Exhibit 29",
    "context": "Exhibit 29: Relative Dividend Yield: Australia vs. Global Mining"
  },
  {
    "figure_id": "F664",
    "report_id": "R042",
    "label": "Exhibit 30",
    "context": "Exhibit 30: Relative ROE: Australia vs. Global Mining"
  },
  {
    "figure_id": "F665",
    "report_id": "R042",
    "label": "Exhibit 31",
    "context": "Exhibit 31: World Datastream Mining index RoE relative to Datastream World Index"
  },
  {
    "figure_id": "F666",
    "report_id": "R042",
    "label": "Exhibit 32",
    "context": "Exhibit 32: World Datastream Mining index P/B relative to Datastream World Index"
  },
  {
    "figure_id": "F667",
    "report_id": "R042",
    "label": "Exhibit 33",
    "context": "Exhibit 33: World Datastream Mining index 12m forward P/E relative to Datastream World Index"
  },
  {
    "figure_id": "F668",
    "report_id": "R042",
    "label": "Exhibit 34",
    "context": "Exhibit 34: World Datastream Mining index 12m forward Div Yield relative to Datastream World Index"
  },
  {
    "figure_id": "F669",
    "report_id": "R042",
    "label": "Exhibit 35",
    "context": "Exhibit 35: World Datastream Mining index share price relative to Datastream World Index"
  },
  {
    "figure_id": "F670",
    "report_id": "R042",
    "label": "Exhibit 44",
    "context": "Exhibit 44: Commodity Price Performance vs. Forecasts Exhibit 45: Spot commodity prices vs. marginal cost of production Spot Prices vs. 90th Percentile Marginal Cost"
  },
  {
    "figure_id": "F671",
    "report_id": "R042",
    "label": "Exhibit 46",
    "context": "Exhibit 46: China: April 2026 trade data Exhibit 47: Total local government special bond issuance"
  },
  {
    "figure_id": "F672",
    "report_id": "R042",
    "label": "Exhibit 48",
    "context": "Exhibit 48: Value of NDRC-approved projects (by approval date) Value of NDRC approved projects (by approval date)"
  },
  {
    "figure_id": "F673",
    "report_id": "R042",
    "label": "Exhibit 49",
    "context": "Exhibit 49: Chinese PMI and IP"
  },
  {
    "figure_id": "F674",
    "report_id": "R042",
    "label": "Exhibit 50",
    "context": "Exhibit 50: Chinese CPI and PPI"
  },
  {
    "figure_id": "F675",
    "report_id": "R042",
    "label": "Exhibit 51",
    "context": "Exhibit 51: Chinese power generation"
  },
  {
    "figure_id": "F676",
    "report_id": "R042",
    "label": "Exhibit 52",
    "context": "Exhibit 52: Chinese new loans and M2 supply"
  },
  {
    "figure_id": "F677",
    "report_id": "R042",
    "label": "Exhibit 53",
    "context": "Exhibit 53: China – Total Floor Space Started"
  },
  {
    "figure_id": "F678",
    "report_id": "R042",
    "label": "Exhibit 54",
    "context": "Exhibit 54: China – Total Floor Space Started (YoY)"
  },
  {
    "figure_id": "F679",
    "report_id": "R042",
    "label": "Exhibit 55",
    "context": "Exhibit 55: China – Total Floor Space Completed"
  },
  {
    "figure_id": "F680",
    "report_id": "R042",
    "label": "Exhibit 56",
    "context": "Exhibit 56: China – Total Floor Space Completed (YoY)"
  },
  {
    "figure_id": "F681",
    "report_id": "R042",
    "label": "Exhibit 57",
    "context": "Exhibit 57: China – Total Floor Space Sold"
  },
  {
    "figure_id": "F682",
    "report_id": "R042",
    "label": "Exhibit 58",
    "context": "Exhibit 58: China – Total Floor Space Sold (YoY)"
  },
  {
    "figure_id": "F683",
    "report_id": "R042",
    "label": "Exhibit 59",
    "context": "Exhibit 59: China – Total Land Area Sold"
  },
  {
    "figure_id": "F684",
    "report_id": "R042",
    "label": "Exhibit 60",
    "context": "Exhibit 60: China – Total Land Sales (YoY)"
  },
  {
    "figure_id": "F685",
    "report_id": "R042",
    "label": "Exhibit 61",
    "context": "Exhibit 61: China – Average Property Sales Price/sq. m (YoY)"
  },
  {
    "figure_id": "F686",
    "report_id": "R042",
    "label": "Exhibit 62",
    "context": "Exhibit 62: Chinese Property – Total Inventory Months"
  },
  {
    "figure_id": "F687",
    "report_id": "R042",
    "label": "Exhibit 63",
    "context": "Exhibit 63: China – Infrastructure spending"
  },
  {
    "figure_id": "F688",
    "report_id": "R042",
    "label": "Exhibit 64",
    "context": "Exhibit 64: White goods production and sales"
  },
  {
    "figure_id": "F689",
    "report_id": "R042",
    "label": "Exhibit 65",
    "context": "Exhibit 65: China – Excavator sales"
  },
  {
    "figure_id": "F690",
    "report_id": "R042",
    "label": "Exhibit 66",
    "context": "Exhibit 66: China – Passenger vehicle sales"
  },
  {
    "figure_id": "F691",
    "report_id": "R042",
    "label": "Exhibit 67",
    "context": "Exhibit 67: Transportation infrastructure new orders reported by large infrastructure construction groups"
  },
  {
    "figure_id": "F692",
    "report_id": "R042",
    "label": "Exhibit 68",
    "context": "Exhibit 68: Building construction new order trend for CSCEC and MCC"
  },
  {
    "figure_id": "F693",
    "report_id": "R042",
    "label": "Exhibit 69",
    "context": "Exhibit 69: Majority of PPP Projects Are in Transportation PPP projects total investment by industry"
  },
  {
    "figure_id": "F694",
    "report_id": "R042",
    "label": "Exhibit 70",
    "context": "Exhibit 70: EV Raw Material Demand as a Percentage of Total Global Demand"
  },
  {
    "figure_id": "F695",
    "report_id": "R042",
    "label": "Exhibit 72",
    "context": "Exhibit 72: Metal Consumption Intensity for Battery Electric Vehicles (BEVs) Consumption intensity of Battery Electric Vehicles (BEV) - 2025 (Kg)"
  },
  {
    "figure_id": "F696",
    "report_id": "R042",
    "label": "Exhibit 74",
    "context": "Exhibit 74: Global EV Battery Installation Global EV battery installation"
  },
  {
    "figure_id": "F697",
    "report_id": "R042",
    "label": "Exhibit 71",
    "context": "Exhibit 71: Metal Demand Growth Rates Under Different Scenarios 2024-27e metal demand CAGR from EVs"
  },
  {
    "figure_id": "F698",
    "report_id": "R042",
    "label": "Exhibit 73",
    "context": "Exhibit 73: World BEV Sales Penetration Forecasts Global BEV sales penetration"
  },
  {
    "figure_id": "F699",
    "report_id": "R042",
    "label": "Exhibit 75",
    "context": "Exhibit 75: China EV Battery Installation China EV battery installation"
  },
  {
    "figure_id": "F700",
    "report_id": "R042",
    "label": "Exhibit 76",
    "context": "Exhibit 76: China – EV Sales and Production"
  },
  {
    "figure_id": "F701",
    "report_id": "R042",
    "label": "Exhibit 77",
    "context": "Exhibit 77: China – Monthly EV Sales (Passenger + Commercial)"
  },
  {
    "figure_id": "F702",
    "report_id": "R042",
    "label": "Exhibit 78",
    "context": "Exhibit 78: Global BEV Sales - YTD April 2026 vs. YTD April 2025 Global BEV Sales"
  },
  {
    "figure_id": "F703",
    "report_id": "R042",
    "label": "Exhibit 79",
    "context": "Exhibit 79: BEV Penetration - April 2026 vs. April 2025"
  },
  {
    "figure_id": "F704",
    "report_id": "R042",
    "label": "Exhibit 80",
    "context": "Exhibit 80: April 2026: YTD Deployments by Region in MWh"
  },
  {
    "figure_id": "F705",
    "report_id": "R042",
    "label": "Exhibit 81",
    "context": "Exhibit 81: April 2026 YTD: Top 5 Countries by Deployment in MWh Exhibit 83: Specific Capacity Is the Amount of Electric Charge the Battery Can Deliver per g of Material Lithium battery properties - Specific Capacity (mAh/g)"
  },
  {
    "figure_id": "F706",
    "report_id": "R042",
    "label": "Exhibit 82",
    "context": "Exhibit 82: April 2026 vs April 2025: Top 5 Countries by MWh Deployed"
  },
  {
    "figure_id": "F707",
    "report_id": "R042",
    "label": "Exhibit 84",
    "context": "Exhibit 84: NCM Batteries Generally Have the Highest Lithium Content per KWh of Battery"
  },
  {
    "figure_id": "F708",
    "report_id": "R042",
    "label": "Exhibit 85",
    "context": "Exhibit 85: MS Global EV Forecasts"
  },
  {
    "figure_id": "F709",
    "report_id": "R042",
    "label": "Exhibit 86",
    "context": "Exhibit 86: MS Global EV Penetration Forecasts"
  },
  {
    "figure_id": "F710",
    "report_id": "R042",
    "label": "Exhibit 87",
    "context": "Exhibit 87: US BEV Sales (MS Forecasts)"
  },
  {
    "figure_id": "F711",
    "report_id": "R042",
    "label": "Exhibit 88",
    "context": "Exhibit 88: Europe BEV Sales (MS Forecasts)"
  },
  {
    "figure_id": "F712",
    "report_id": "R042",
    "label": "Exhibit 89",
    "context": "Exhibit 89: China BEV Sales (MS Forecasts)"
  },
  {
    "figure_id": "F713",
    "report_id": "R042",
    "label": "Exhibit 90",
    "context": "Exhibit 90: BEV vs. ICE Unit Sales (mm) Forecasts"
  },
  {
    "figure_id": "F714",
    "report_id": "R042",
    "label": "Exhibit 91",
    "context": "Exhibit 91: Consumption of Aluminum in China China aluminum demand breakdown by sectors"
  },
  {
    "figure_id": "F715",
    "report_id": "R042",
    "label": "Exhibit92",
    "context": "Exhibit92: Aluminium Exchange Inventories and Days of Consumption"
  },
  {
    "figure_id": "F716",
    "report_id": "R042",
    "label": "Exhibit93",
    "context": "Exhibit93: Aluminum Inventory in China"
  },
  {
    "figure_id": "F717",
    "report_id": "R042",
    "label": "Exhibit94",
    "context": "Exhibit94: China's apparent aluminium consumption vs. LME price"
  },
  {
    "figure_id": "F718",
    "report_id": "R042",
    "label": "Exhibit95",
    "context": "Exhibit95: Raw Materials: China's Alumina Production"
  },
  {
    "figure_id": "F719",
    "report_id": "R042",
    "label": "Exhibit96",
    "context": "Exhibit96: Raw Materials: Spot Alumina vs. China's Domestic Price"
  },
  {
    "figure_id": "F720",
    "report_id": "R042",
    "label": "Exhibit 97",
    "context": "Exhibit 97: Monthly Alumina Balance in China Monthly Alumina Balance in China (kt)"
  },
  {
    "figure_id": "F721",
    "report_id": "R042",
    "label": "Exhibit99",
    "context": "Exhibit99: Price Differentials: SHFE vs. LME"
  },
  {
    "figure_id": "F722",
    "report_id": "R042",
    "label": "Exhibit101",
    "context": "Exhibit101: Contango vs. Backwardation: Aluminium Futures Curve Movement"
  },
  {
    "figure_id": "F723",
    "report_id": "R042",
    "label": "Exhibit98",
    "context": "Exhibit98: Aluminium World Production ex-China"
  },
  {
    "figure_id": "F724",
    "report_id": "R042",
    "label": "Exhibit100",
    "context": "Exhibit100: Physical Demand: Aluminium Premia by Region"
  },
  {
    "figure_id": "F725",
    "report_id": "R042",
    "label": "Exhibit 102",
    "context": "Exhibit 102: China Aluminium Exports: Breakdown, by Product Type China Breakup of Aluminium Exports"
  },
  {
    "figure_id": "F726",
    "report_id": "R042",
    "label": "Exhibit 103",
    "context": "Exhibit 103: China Aluminium Net Exports China Net Exports (Semis-Aluminum Product)"
  },
  {
    "figure_id": "F727",
    "report_id": "R042",
    "label": "Exhibit 104",
    "context": "Exhibit 104: Bauxite Price"
  },
  {
    "figure_id": "F728",
    "report_id": "R042",
    "label": "Exhibit 105",
    "context": "Exhibit 105: China – Bauxite Imports, by Country Bauxite mine import by country"
  },
  {
    "figure_id": "F729",
    "report_id": "R042",
    "label": "Exhibit 106",
    "context": "Exhibit 106: Aluminium Cost Curve"
  },
  {
    "figure_id": "F730",
    "report_id": "R042",
    "label": "Exhibit107",
    "context": "Exhibit107: China – Thermal-based power generation vs. coal apparent monthly consumption"
  },
  {
    "figure_id": "F731",
    "report_id": "R042",
    "label": "Exhibit108",
    "context": "Exhibit108: Inventories: Qinhuangdao port coal stocks Qinhuangdao Port Thermal Coal Inventory"
  },
  {
    "figure_id": "F732",
    "report_id": "R042",
    "label": "Exhibit109",
    "context": "Exhibit109: China – Coal imports vs. prices"
  },
  {
    "figure_id": "F733",
    "report_id": "R042",
    "label": "Exhibit110",
    "context": "Exhibit110: Inventories: China's coking coal inventories at steel mills"
  },
  {
    "figure_id": "F734",
    "report_id": "R042",
    "label": "Exhibit111",
    "context": "Exhibit111: China's Coking Coal Prices – Mine-mouth vs. FOR"
  },
  {
    "figure_id": "F735",
    "report_id": "R042",
    "label": "Exhibit112",
    "context": "Exhibit112: Coal Inventory at QHD Port"
  },
  {
    "figure_id": "F736",
    "report_id": "R042",
    "label": "Exhibit 113",
    "context": "Exhibit 113: Thermal coal cost curve"
  },
  {
    "figure_id": "F737",
    "report_id": "R042",
    "label": "Exhibit 114",
    "context": "Exhibit 114: Met coal cost curve"
  },
  {
    "figure_id": "F738",
    "report_id": "R042",
    "label": "Exhibit 115",
    "context": "Exhibit 115: Consumption of Copper in China China copper demand breakdown by sectors"
  },
  {
    "figure_id": "F739",
    "report_id": "R042",
    "label": "Exhibit117",
    "context": "Exhibit117: Exchange and Bonded Warehouse Stocks vs. Days of Consumption"
  },
  {
    "figure_id": "F740",
    "report_id": "R042",
    "label": "Exhibit119",
    "context": "Exhibit119: CFTC speculative net length"
  },
  {
    "figure_id": "F741",
    "report_id": "R042",
    "label": "Exhibit116",
    "context": "Exhibit116: Grid Investments, Car Sales and Air Conditioner Sales"
  },
  {
    "figure_id": "F742",
    "report_id": "R042",
    "label": "Exhibit118",
    "context": "Exhibit118: China Copper Price vs. Apparent Consumption"
  },
  {
    "figure_id": "F743",
    "report_id": "R042",
    "label": "Exhibit120",
    "context": "Exhibit120: China – refined copper imports"
  },
  {
    "figure_id": "F744",
    "report_id": "R042",
    "label": "Exhibit 121",
    "context": "Exhibit 121: LME Speculative Net Position"
  },
  {
    "figure_id": "F745",
    "report_id": "R042",
    "label": "Exhibit122",
    "context": "Exhibit122: Physical Demand: Copper Premia, by Region"
  },
  {
    "figure_id": "F746",
    "report_id": "R042",
    "label": "Exhibit123",
    "context": "Exhibit123: Copper Treatment Charges (TCs) vs. Price"
  },
  {
    "figure_id": "F747",
    "report_id": "R042",
    "label": "Exhibit 124",
    "context": "Exhibit 124: Chile: Copper Production"
  },
  {
    "figure_id": "F748",
    "report_id": "R042",
    "label": "Exhibit125",
    "context": "Exhibit125: Contango vs. Backwardation: Copper Futures Curve Movement"
  },
  {
    "figure_id": "F749",
    "report_id": "R042",
    "label": "Exhibit 126",
    "context": "Exhibit 126: Copper Cost Curve"
  },
  {
    "figure_id": "F750",
    "report_id": "R042",
    "label": "Exhibit 127",
    "context": "Exhibit 127: Copper Mine Production"
  },
  {
    "figure_id": "F751",
    "report_id": "R042",
    "label": "Exhibit 128",
    "context": "Exhibit 128: Global Copper Refined Production"
  },
  {
    "figure_id": "F752",
    "report_id": "R042",
    "label": "Exhibit 129",
    "context": "Exhibit 129: Copper Mine Production (YoY)"
  },
  {
    "figure_id": "F753",
    "report_id": "R042",
    "label": "Exhibit 130",
    "context": "Exhibit 130: Global Copper Refined Production (YoY)"
  },
  {
    "figure_id": "F754",
    "report_id": "R042",
    "label": "Exhibit 131",
    "context": "Exhibit 131: South China Copper Smelters Capacity Utilization"
  },
  {
    "figure_id": "F755",
    "report_id": "R042",
    "label": "Exhibit 132",
    "context": "Exhibit 132: Global Refined Balance Surplus/Deficit"
  },
  {
    "figure_id": "F756",
    "report_id": "R042",
    "label": "Exhibit133",
    "context": "Exhibit133: ETF gold holdings vs. gold price"
  },
  {
    "figure_id": "F757",
    "report_id": "R042",
    "label": "Exhibit134",
    "context": "Exhibit134: Gold price vs. US five-year TIPS"
  },
  {
    "figure_id": "F758",
    "report_id": "R042",
    "label": "Exhibit135",
    "context": "Exhibit135: Gold performance vs. volatility index vs. dollar index"
  },
  {
    "figure_id": "F759",
    "report_id": "R042",
    "label": "Exhibit136",
    "context": "Exhibit136: Gold imports: China vs. India"
  },
  {
    "figure_id": "F760",
    "report_id": "R042",
    "label": "Exhibit137",
    "context": "Exhibit137: Gold-to-silver ratio"
  },
  {
    "figure_id": "F761",
    "report_id": "R042",
    "label": "Exhibit138",
    "context": "Exhibit138: Nymex positioning per COTR"
  },
  {
    "figure_id": "F762",
    "report_id": "R042",
    "label": "Exhibit 139",
    "context": "Exhibit 139: Gold cost curve"
  },
  {
    "figure_id": "F763",
    "report_id": "R042",
    "label": "Exhibit 140",
    "context": "Exhibit 140: Consumption of steel in China 2025 MSe China Steel Demand Drivers"
  },
  {
    "figure_id": "F764",
    "report_id": "R042",
    "label": "Exhibit 141",
    "context": "Exhibit 141: China – 10-day annualized crude steel output (member mills)"
  },
  {
    "figure_id": "F765",
    "report_id": "R042",
    "label": "Exhibit 142",
    "context": "Exhibit 142: Total steel inventory in China (traders + mills)"
  },
  {
    "figure_id": "F766",
    "report_id": "R042",
    "label": "Exhibit 143",
    "context": "Exhibit 143: GP/t for mills at spot prices Exhibit 144: Chinese exports vs. international HRC price spread"
  },
  {
    "figure_id": "F767",
    "report_id": "R042",
    "label": "Exhibit 143",
    "context": "Exhibit 143: GP/t for mills at spot prices Exhibit 144: Chinese exports vs. international HRC price spread"
  },
  {
    "figure_id": "F768",
    "report_id": "R042",
    "label": "Exhibit 145",
    "context": "Exhibit 145: China – Iron ore stock at port"
  },
  {
    "figure_id": "F769",
    "report_id": "R042",
    "label": "Exhibit 146",
    "context": "Exhibit 146: Implied China iron ore production (62% Fe equivalent) Implied China Iron Ore Production (62% Fe equivalent)"
  },
  {
    "figure_id": "F770",
    "report_id": "R042",
    "label": "Exhibit 148",
    "context": "Exhibit 148: Weekly steel demand"
  },
  {
    "figure_id": "F771",
    "report_id": "R042",
    "label": "Exhibit 147",
    "context": "Exhibit 147: CISA member mill vs. NBS (restated) average daily steel output"
  },
  {
    "figure_id": "F772",
    "report_id": "R042",
    "label": "Exhibit 149",
    "context": "Exhibit 149: Iron ore inventory at small/mid-sized Chinese steel mills"
  },
  {
    "figure_id": "F773",
    "report_id": "R042",
    "label": "Exhibit150",
    "context": "Exhibit150: Iron ore inventories at Chinese sea ports and inventory days of consumption"
  },
  {
    "figure_id": "F774",
    "report_id": "R042",
    "label": "Exhibit 152",
    "context": "Exhibit 152: MS Estimated Scrap Steel Mix in Long Process Steelmaking"
  },
  {
    "figure_id": "F775",
    "report_id": "R042",
    "label": "Exhibit 154",
    "context": "Exhibit 154: Iron ore cost curve"
  },
  {
    "figure_id": "F776",
    "report_id": "R042",
    "label": "Exhibit 151",
    "context": "Exhibit 151: EAF capacity utilization rate"
  },
  {
    "figure_id": "F777",
    "report_id": "R042",
    "label": "Exhibit 153",
    "context": "Exhibit 153: Iron ore prices: -Discount/+premium vs. 62% Fe (%)"
  },
  {
    "figure_id": "F778",
    "report_id": "R042",
    "label": "Exhibit 155",
    "context": "Exhibit 155: China – Domestic lithium compound prices"
  },
  {
    "figure_id": "F779",
    "report_id": "R042",
    "label": "Exhibit 157",
    "context": "Exhibit 157: Spodumene price vs. China's lithium hydroxide spot price"
  },
  {
    "figure_id": "F780",
    "report_id": "R042",
    "label": "Exhibit 159",
    "context": "Exhibit 159: Weekly lithium hydroxide output in China"
  },
  {
    "figure_id": "F781",
    "report_id": "R042",
    "label": "Exhibit 156",
    "context": "Exhibit 156: Spodumene price vs. China's lithium carbonate spot price"
  },
  {
    "figure_id": "F782",
    "report_id": "R042",
    "label": "Exhibit 158",
    "context": "Exhibit 158: Weekly lithium carbonate output in China"
  },
  {
    "figure_id": "F783",
    "report_id": "R042",
    "label": "Exhibit 160",
    "context": "Exhibit 160: China – Monthly lithium import prices (US\\$/ton)"
  },
  {
    "figure_id": "F784",
    "report_id": "R042",
    "label": "Exhibit 161",
    "context": "Exhibit 161: China – Lithium carbonate imports and implied ASP Total LC imports & Implied ASP"
  },
  {
    "figure_id": "F785",
    "report_id": "R042",
    "label": "Exhibit 162",
    "context": "Exhibit 162: China – Lithium hydroxide exports and implied ASP Total LiOH exports & Implied ASP"
  },
  {
    "figure_id": "F786",
    "report_id": "R042",
    "label": "Exhibit 163",
    "context": "Exhibit 163: China – Monthly lithium carbonate imports breakdown"
  },
  {
    "figure_id": "F787",
    "report_id": "R042",
    "label": "Exhibit 164",
    "context": "Exhibit 164: China – Monthly lithium hydroxide exports breakdown"
  },
  {
    "figure_id": "F788",
    "report_id": "R042",
    "label": "Exhibit 165",
    "context": "Exhibit 165: Monthly cathode production in China by type"
  },
  {
    "figure_id": "F789",
    "report_id": "R042",
    "label": "Exhibit 166",
    "context": "Exhibit 166: Monthly cathode production in China by type (%) Monthly battery cathode production by type (%)"
  },
  {
    "figure_id": "F790",
    "report_id": "R042",
    "label": "Exhibit 167",
    "context": "Exhibit 167: Japan – Monthly imports (tons)"
  },
  {
    "figure_id": "F791",
    "report_id": "R042",
    "label": "Exhibit 168",
    "context": "Exhibit 168: South Korea – Monthly imports (tons)"
  },
  {
    "figure_id": "F792",
    "report_id": "R042",
    "label": "Exhibit 169",
    "context": "Exhibit 169: US – Monthly imports (tons)"
  },
  {
    "figure_id": "F793",
    "report_id": "R042",
    "label": "Exhibit 170",
    "context": "Exhibit 170: US – Monthly exports (tons)"
  },
  {
    "figure_id": "F794",
    "report_id": "R042",
    "label": "Exhibit 171",
    "context": "## Exhibit 171:"
  },
  {
    "figure_id": "F795",
    "report_id": "R042",
    "label": "Exhibit 172",
    "context": "Exhibit 172: Australian spodumene concentrate production on the rise..."
  },
  {
    "figure_id": "F796",
    "report_id": "R042",
    "label": "Exhibit 173",
    "context": "Exhibit 173: ...along with shipments"
  },
  {
    "figure_id": "F797",
    "report_id": "R042",
    "label": "Exhibit 174",
    "context": "Exhibit 174: Inventory build currently limited at Australian mines"
  },
  {
    "figure_id": "F798",
    "report_id": "R042",
    "label": "Exhibit 176",
    "context": "Exhibit 176: Lithium carbonate refining cost curve Lithium carbonate chemicals refining costs (US$/t, kt carbonate)"
  },
  {
    "figure_id": "F799",
    "report_id": "R042",
    "label": "Exhibit 177",
    "context": "Exhibit 177: Lithium hydroxide refining cost curve Lithium hydroxide chemicals refining costs (US$/t, kt hydroxide)"
  },
  {
    "figure_id": "F800",
    "report_id": "R042",
    "label": "Exhibit 178",
    "context": "Exhibit 178: Feedstock costs make up \\~85% of non-integrated converters' total cost Total carbonate refining costs broken down (US$/t, kt carbonate)"
  },
  {
    "figure_id": "F801",
    "report_id": "R042",
    "label": "Exhibit 179",
    "context": "Exhibit 179: Margins of non-integrated spodumene carbonate refiners have declined sharply this year"
  },
  {
    "figure_id": "F802",
    "report_id": "R042",
    "label": "Exhibit 180",
    "context": "Exhibit 180: China – artificial graphite import volumes"
  },
  {
    "figure_id": "F803",
    "report_id": "R042",
    "label": "Exhibit 181",
    "context": "Exhibit 181: China – artificial graphite export volumes China Artificial Graphite Export Volume"
  },
  {
    "figure_id": "F804",
    "report_id": "R042",
    "label": "Exhibit 182",
    "context": "Exhibit 182: China – natural spherical graphite import volumes China Natural Spherical Graphite Import Volume"
  },
  {
    "figure_id": "F805",
    "report_id": "R042",
    "label": "Exhibit 183",
    "context": "Exhibit 183: China – natural spherical graphite export volumes China Natural Spherical Graphite Export Volume"
  },
  {
    "figure_id": "F806",
    "report_id": "R042",
    "label": "Exhibit 184",
    "context": "Exhibit 184: Graphite prices (US\\$/t)"
  },
  {
    "figure_id": "F807",
    "report_id": "R042",
    "label": "Exhibit 185",
    "context": "Exhibit 185: China – Rare Earths Exports"
  },
  {
    "figure_id": "F808",
    "report_id": "R042",
    "label": "Exhibit 186",
    "context": "Exhibit 186: China – Industrial Ex-factory PPI, rare earths metal ore mining"
  },
  {
    "figure_id": "F809",
    "report_id": "R042",
    "label": "Exhibit 187",
    "context": "Exhibit 187: China – Industrial Ex-factory PPI, rare earths metal smelting"
  },
  {
    "figure_id": "F810",
    "report_id": "R042",
    "label": "Exhibit 188",
    "context": "Exhibit 188: China – NdPr FOB prices"
  },
  {
    "figure_id": "F811",
    "report_id": "R042",
    "label": "Exhibit 189",
    "context": "Exhibit 189: China – neodymium oxide FOB prices"
  },
  {
    "figure_id": "F812",
    "report_id": "R042",
    "label": "Exhibit 190",
    "context": "Exhibit 190: China – praseodymium oxide FOB prices"
  },
  {
    "figure_id": "F813",
    "report_id": "R042",
    "label": "Exhibit 191",
    "context": "Exhibit 191: China – terbium oxide FOB prices"
  },
  {
    "figure_id": "F814",
    "report_id": "R042",
    "label": "Exhibit 192",
    "context": "Exhibit 192: China – lanthanum oxide FOB prices"
  },
  {
    "figure_id": "F815",
    "report_id": "R042",
    "label": "Exhibit 193",
    "context": "Exhibit 193: China – cerium oxide FOB prices"
  },
  {
    "figure_id": "F816",
    "report_id": "R042",
    "label": "Exhibit194",
    "context": "Exhibit194: Nickel exchange inventories and days of consumption"
  },
  {
    "figure_id": "F817",
    "report_id": "R042",
    "label": "Exhibit195",
    "context": "Exhibit195: Nickel LME price"
  },
  {
    "figure_id": "F818",
    "report_id": "R042",
    "label": "Exhibit196",
    "context": "Exhibit196: Raw materials: Nickel laterite ore inventories"
  },
  {
    "figure_id": "F819",
    "report_id": "R042",
    "label": "Exhibit197",
    "context": "Exhibit197: Raw materials: China's ore imports, by"
  },
  {
    "figure_id": "F820",
    "report_id": "R042",
    "label": "Exhibit198",
    "context": "Exhibit198: China's nickel ore imports vs. stainless steel production"
  },
  {
    "figure_id": "F821",
    "report_id": "R042",
    "label": "Exhibit199",
    "context": "Exhibit199: Contango vs. backwardation: Nickel futures curve movement"
  },
  {
    "figure_id": "F822",
    "report_id": "R042",
    "label": "Exhibit 200",
    "context": "Exhibit 200: Nickel cost curve"
  },
  {
    "figure_id": "F823",
    "report_id": "R042",
    "label": "Exhibit201",
    "context": "Exhibit201: Zinc exchange inventories and days of consumption"
  },
  {
    "figure_id": "F824",
    "report_id": "R042",
    "label": "Exhibit202",
    "context": "Exhibit202: China's apparent zinc consumption vs. LME price"
  },
  {
    "figure_id": "F825",
    "report_id": "R042",
    "label": "Exhibit203",
    "context": "Exhibit203: Raw materials: China's zinc concentrate imports"
  },
  {
    "figure_id": "F826",
    "report_id": "R042",
    "label": "Exhibit204",
    "context": "Exhibit204: Zinc price differentials: SHFE vs. LME"
  },
  {
    "figure_id": "F827",
    "report_id": "R042",
    "label": "Exhibit 205",
    "context": "Exhibit 205: Zinc TCs vs. spot"
  },
  {
    "figure_id": "F828",
    "report_id": "R042",
    "label": "Exhibit 206",
    "context": "Exhibit 206: Contango vs. backwardation: Zinc futures curve movement"
  },
  {
    "figure_id": "F829",
    "report_id": "R042",
    "label": "Exhibit 207",
    "context": "Exhibit 207: Zinc cost curve"
  },
  {
    "figure_id": "F830",
    "report_id": "R043",
    "label": "Figure 1",
    "context": "Figure 1: JPM NBL price forecast (\\$/t) Figure 2: Korea NBL price (\\$/t)"
  },
  {
    "figure_id": "F831",
    "report_id": "R043",
    "label": "Figure 3",
    "context": "Figure 3: Korea NBL export volume (kt)"
  },
  {
    "figure_id": "F832",
    "report_id": "R043",
    "label": "Figure 4",
    "context": "Figure 4: Key chemical spreads for Kumho Petchem Monthly spread data (\\$/tonne) BPA vs Phenol"
  },
  {
    "figure_id": "F833",
    "report_id": "R048",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Vera CPU alone could account for more than $10\\%$ of total global DRAM bit demand for 2025 LPDDR5X bit demand for Vera CPU relative to 2025 total DRAM bit demand (=38TB)"
  },
  {
    "figure_id": "F834",
    "report_id": "R048",
    "label": "Exhibit 2",
    "context": "Exhibit 2: The shift toward 400G-per-lane signaling targeted from around 2028 would push electrical copper transmission to $1.25\\mathrm{m}$ , below typical rack sizes ( $\\sim 2\\mathrm{m}$ ), reinforcing the need for optical interco"
  },
  {
    "figure_id": "F835",
    "report_id": "R048",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Kokusai Electric's sales breakdown by equipment application Kokusai Electric"
  },
  {
    "figure_id": "F836",
    "report_id": "R049",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Staffers' organic growth has recovered, mainly driven by temp..."
  },
  {
    "figure_id": "F837",
    "report_id": "R049",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Indeed job postings have continued to deteriorate... Exhibit 5: Staffing exposure to permanent recruitment (% of gross profit)"
  },
  {
    "figure_id": "F838",
    "report_id": "R049",
    "label": "Exhibit 2",
    "context": "Exhibit 2: ... but gross margins remain under pressure"
  },
  {
    "figure_id": "F839",
    "report_id": "R049",
    "label": "Exhibit 4",
    "context": "Exhibit 4: .... and so have job vacancies in key recruitment markets"
  },
  {
    "figure_id": "F840",
    "report_id": "R049",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Adecco's financial leverage compared to Randstad's"
  },
  {
    "figure_id": "F841",
    "report_id": "R049",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Adecco EV/EBIT valuation relative to Randstad"
  },
  {
    "figure_id": "F842",
    "report_id": "R049",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Staffing coverage FCF yield valuation"
  },
  {
    "figure_id": "F843",
    "report_id": "R049",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Organic growth of generalist staffers (Adecco, Manpower, Randstad)"
  },
  {
    "figure_id": "F844",
    "report_id": "R049",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Organic growth of specialist staffers (Hays, Page Group)"
  },
  {
    "figure_id": "F845",
    "report_id": "R049",
    "label": "Exhibit 12",
    "context": "Exhibit 12: yoy changes in operating margin for generalist staffers (Adecco, Manpower, Randstad)"
  },
  {
    "figure_id": "F846",
    "report_id": "R049",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Gross margin evolution at generalist staffers"
  },
  {
    "figure_id": "F847",
    "report_id": "R049",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Job vacancies in France, Germany, the UK and the US (re-based December 2018)"
  },
  {
    "figure_id": "F848",
    "report_id": "R049",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Indeed job posting (re-based to 100 in February 2020) Exhibit 17: Indeed quarterly job posting yoy growth"
  },
  {
    "figure_id": "F849",
    "report_id": "R049",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Perm recruitment yoy growth"
  },
  {
    "figure_id": "F850",
    "report_id": "R049",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Number of people employed in AI disrupted vs AI protected jobs, yoy growth"
  },
  {
    "figure_id": "F851",
    "report_id": "R049",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Employment by job type yoy growth in 2023/24/25"
  },
  {
    "figure_id": "F852",
    "report_id": "R049",
    "label": "Exhibit 21",
    "context": "Exhibit 21: Employment growth in the AI-disrupted basket consistently outperformed employment growth in the AI-protected basket until the launch of ChatGPT AI-disrupted employment growth minus AI-protected employment growth"
  },
  {
    "figure_id": "F853",
    "report_id": "R049",
    "label": "Exhibit 22",
    "context": "Exhibit 22: Adecco vs Randstad quarterly organic growth"
  },
  {
    "figure_id": "F854",
    "report_id": "R049",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Adecco quarterly organic growth by GBU"
  },
  {
    "figure_id": "F855",
    "report_id": "R049",
    "label": "Exhibit 24",
    "context": "Exhibit 24: Adecco geographic exposure (FY24)"
  },
  {
    "figure_id": "F856",
    "report_id": "R049",
    "label": "Exhibit 25",
    "context": "Exhibit 25: Randstad geographic exposure (FY23)"
  },
  {
    "figure_id": "F857",
    "report_id": "R049",
    "label": "Exhibit 26",
    "context": "Exhibit 26: Randstad financial leverage"
  },
  {
    "figure_id": "F858",
    "report_id": "R049",
    "label": "Exhibit 28",
    "context": "Exhibit 28: Hypothetical illustration of Adecco's FY27 financial leverage, assuming different scrip dividend take rates in FY26e\\*"
  },
  {
    "figure_id": "F859",
    "report_id": "R049",
    "label": "Exhibit 27",
    "context": "Exhibit 27: Adecco financial leverage"
  },
  {
    "figure_id": "F860",
    "report_id": "R049",
    "label": "Exhibit 29",
    "context": "Exhibit 29: Hypothetical illustration of Adecco's FY28 financial leverage, assuming different scrip dividend take rates in FY26/27e\\*"
  },
  {
    "figure_id": "F861",
    "report_id": "R049",
    "label": "Exhibit 30",
    "context": "Exhibit 30: Potential shareholder dilution depending on script take rate in FY26e\\*"
  },
  {
    "figure_id": "F862",
    "report_id": "R049",
    "label": "Exhibit 31",
    "context": "Exhibit 31: Potential shareholder dilution depending on script take rate in FY26/27e\\*"
  },
  {
    "figure_id": "F863",
    "report_id": "R049",
    "label": "Exhibit 55",
    "context": "Exhibit 32: Organic growth of Adecco, Randstad and Manpower since 2004 vs consensus expectations"
  },
  {
    "figure_id": "F864",
    "report_id": "R049",
    "label": "Exhibit 41",
    "context": "Exhibit 41: Share price performance of our staffing coverage ytd"
  },
  {
    "figure_id": "F865",
    "report_id": "R049",
    "label": "Exhibit 42",
    "context": "Exhibit 42: Adecco EV/sales over the last 10y"
  },
  {
    "figure_id": "F866",
    "report_id": "R049",
    "label": "Exhibit 43",
    "context": "Exhibit 43: Randstad EV/sales over the last 10y"
  },
  {
    "figure_id": "F867",
    "report_id": "R049",
    "label": "Exhibit 44",
    "context": "Exhibit 44: Adecco EV/EBIT over the last 10y"
  },
  {
    "figure_id": "F868",
    "report_id": "R049",
    "label": "Exhibit 45",
    "context": "Exhibit 45: Randstad EV/EBIT over the last 10y"
  },
  {
    "figure_id": "F869",
    "report_id": "R049",
    "label": "Exhibit 46",
    "context": "Exhibit 46: Adecco EV/sales valuation relative to Randstad over the last 10y"
  },
  {
    "figure_id": "F870",
    "report_id": "R049",
    "label": "Exhibit 47",
    "context": "Exhibit 47: Adecco EV/EBIT valuation relative to Randstad over the last 10y"
  },
  {
    "figure_id": "F871",
    "report_id": "R049",
    "label": "Exhibit 48",
    "context": "Exhibit 48: Hays EV/GP"
  },
  {
    "figure_id": "F872",
    "report_id": "R049",
    "label": "Exhibit 49",
    "context": "Exhibit 49: Page Group EV/GP"
  },
  {
    "figure_id": "F873",
    "report_id": "R049",
    "label": "Exhibit 50",
    "context": "Exhibit 50: Hays EV/EBIT since"
  },
  {
    "figure_id": "F874",
    "report_id": "R049",
    "label": "Exhibit 51",
    "context": "Exhibit 51: Page Group EV/EBIT over the last 10y"
  },
  {
    "figure_id": "F875",
    "report_id": "R049",
    "label": "Exhibit 52",
    "context": "Exhibit 52: Page Group EV/GP valuation relative to Hays over the last 10y"
  },
  {
    "figure_id": "F876",
    "report_id": "R049",
    "label": "Exhibit 53",
    "context": "Exhibit 53: Page Group EV/EBIT valuation relative to Hays over the last 10y"
  },
  {
    "figure_id": "F877",
    "report_id": "R049",
    "label": "Exhibit 54",
    "context": "Exhibit 54: Staffing coverage dividend yield over the next 12 months"
  },
  {
    "figure_id": "F878",
    "report_id": "R049",
    "label": "Exhibit 55",
    "context": "Exhibit 55: Consensus dividend coverage for next 12 months\\*"
  },
  {
    "figure_id": "F879",
    "report_id": "R049",
    "label": "Exhibit 56",
    "context": "Exhibit 56: Staffing coverage FCF yield over the next 12 months"
  },
  {
    "figure_id": "F880",
    "report_id": "R049",
    "label": "Exhibit 57",
    "context": "Exhibit 57: Staffing coverage EV/FCF over the next 12 months"
  }
]