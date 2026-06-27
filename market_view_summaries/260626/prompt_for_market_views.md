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
    "title": "Citi：AI超级周期正在重塑中国K型经济，但“涓滴效应”远未到来",
    "digest": "[wechat_article.md]\n# Citi：AI超级周期正在重塑中国K型经济，但“涓滴效应”远未到来\n\n中国经济的核心问题，在2026年中期已经不再是“复苏是否稳固”，而是“谁在复苏，谁在被遗忘”。Citi在最新发布的2026年下半年展望报告中，给出了一个清晰但令人不安的判断：AI超级周期正在成为中国K型经济中最强大的驱动力，但它同时也在加深结构性裂痕，而非弥合它们。\n\n这份报告的核心洞察并非关于AI本身的技术突破——DeepSeek、OpenClaw和Agentic AI的崛起已是共识。Citi真正有价值的主张在于：AI对中国经济的影响，已经从“概念叙事”全面转向“可量化的宏观冲击”。它同时支撑着出口、生产和新兴产业，却也在就业、消费和传统投资端制造着新的压力。4.7%的2026年GDP增速预测背后，是一个正在加速分化的经济图景。\n\n对于决策者和投资者而言，理解这种分化，比预测整体数字更为关键。\n\n> **KC评论：** Citi的框架很直接——中国经济的“强腿”（出口、生产、新经济）在AI加持下更强，“弱腿”（消费、房地产、传统投资）则在AI冲击下更加碎片化。这不是一个“好坏参半”的中性判断，而是一个“赢家通吃、输家更难翻身”的结构性警告。完整报告中有多张图表展示了这种分化的具体规模，包括AI相关出口占比、消费信心指数连续50个月低于荣枯线等关键数据，值得仔细推敲。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI经济已从算法竞赛转向硬件基建，这是宏观影响真正开始落地的地方\n\nCiti用一组数据勾勒出AI经济的膨胀轨迹：中国每日Token使用量从2024年初的0.1万亿飙升至2026年3月的140万亿；智能算力在2025年同比增长三倍；AI相关的市场表现已经从互联网巨头轮动至半导体和材料供应商。这些数字背后，是一个从“无形算法开发”到“\n\n[... middle omitted ...]\n\n讨论这些未解问题，一起追踪AI超级周期下的中国经济分化图景。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI正在重塑中国经济的“K型”走势\n\nAI是K型经济的关键变量\n\n某外资投行最新研报指出，AI超周期正在加深中国经济的“K型”裂痕。\n\n一边是AI驱动的新经济（出口、生产）越来越强，另一边是消费和旧经济承压。而且，AI对就业的替代风险，正在拖累本就脆弱的消费者信心。\n\n几个关键数据点，帮你快速理解：\n\n1️⃣ **AI基建爆发式增长**\n- 中国日均Token使用量：从2024年初的0.1万亿，飙升至2026年3月的140万亿\n- 智能算力：2025年较2024年增长3倍\n- 股市热点已从互联网巨头，转向半导体和材料供应商\n\n2️⃣ **出口的结构性变化**\n- AI相关出口占中国总出口的20.3%（2025年）\n- 2026年前5个月增速达34.8%，贡献了出口增长的6.8个百分点\n- 全球AI转型仍在早期，这个趋势很难逆转\n\n3️⃣ **内需的碎片化**\n- 消费者信心指数自2022年4月以来，已连续50个月低于100的荣枯线\n- 家庭净还贷额达6310亿元（2026年前5个月），超额储蓄仍有28.4万亿\n- 房产市场：一线城市价格企稳，但全国指数仍在寻底\n\n4️⃣ **政策方向**\n- 预计7月政治局会\n\n[... middle omitted ...]\n\ngrowth forecast for 2026E, with 26Q2 likely the low point. The July Politburo should signal piecemeal consumer support – not broad-based stimulus, in our view. An outright deficit expansion is\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R002",
    "title": "BARC：全球正从“储蓄过剩”转向“债券过剩”，长端利率的结构性上行才刚刚开始",
    "digest": "[wechat_article.md]\n# BARC：全球正从“储蓄过剩”转向“债券过剩”，长端利率的结构性上行才刚刚开始\n\n全球投资者正在经历一个被多数人低估的范式转换。过去二十年，市场习惯了“全球储蓄过剩”压低长期利率的故事——新兴市场央行和主权财富基金对发达市场国债的刚性需求，让长端收益率持续处于低位。但BARC利率策略团队在最新发布的深度报告中提出了一个截然相反的判断：世界正从“储蓄过剩”转向“债券过剩”，而这一转变意味着长端收益率的结构性上行远未结束。\n\n这份报告的核心洞察并非简单的“利率会更高”，而是揭示了当前5%左右的30年期国债收益率与2007年5%的收益率在构成上存在根本性差异。今天的5%中，包含了更低的短期利率预期和更高的期限溢价与财政风险溢价。换句话说，市场正在为持有长期国债要求更多的补偿，而这一趋势背后的驱动力——持续的财政赤字与价格敏感的买家基础——短期内看不到逆转的可能。\n\n**BARC认为，无论是美国财政部缩短发行久期、欧洲降低加权平均到期期限，还是日本削减超长端发行量，这些供给侧的调整只能在边际上减缓调整速度，无法改变方向。**\n\n> **KC评论：** 这份报告最值得反复咀嚼的是它对30年期美债收益率的拆解框架。它把5%的收益率分成了三块：预期短期利率（3.1%）、利率期限溢价（1.1%）和财政风险溢价（0.7%）。对比2007年，当时预期短期利率高达4.4%，而期限溢价和财政溢价几乎可以忽略。这意味着，今天的市场不是在为“未来加息”定价，而是在为“长期持有国债的不确定性”定价。这种结构性变化，比简单的加息周期更值得投资者关注。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 30年期收益率重回5%，但驱动因素已截然不同\n\nBARC通过分解30年期美债收益率的历史构成，揭示了一个关键事实：当前5%的水平与2007年5%的\n\n[... middle omitted ...]\n\n化。我们会在微信群里继续讨论这些未解问题，欢迎你的加入。**\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球债券大甩卖，长端利率难回头\n\n长端利率，结构性抬升\n\n最近翻到某外资投行的利率策略报告，核心观点很直接：全球正从“储蓄过剩”转向“债券过剩”，长端收益率可能长期维持高位。不是短期波动，是结构性的。\n\n**1. 为什么说“债券过剩”？**\n- 主要经济体财政赤字持续高位，政府发债量大增。\n- 买家变了：央行和官方机构过去“不挑价格”地买，现在它们退场了。私营投资者接手，但对价格非常敏感，要求更高的“期限溢价”才肯接盘。\n- 债券的“避险”光环减弱。过去股跌债涨，现在通胀担忧下，股债同跌，投资者不再愿意为“保险”支付高价。\n\n**2. 长端利率的“配方”变了**\n以美国30年期国债为例，收益率回到5%附近（2007年水平），但构成完全不同：\n- 预期短期利率部分：从2007年的4.4%降至约3.1%。市场不认为未来会大幅加息。\n- 期限溢价部分：从0.9%升至1.1%。纯为承担久期风险要的补偿。\n- 财政风险溢价部分：从-0.5%飙升至+0.7%。投资者明确要求为财政恶化“买单”。\n\n**3. 未来还有上行空间**\n- 中性利率可能被低估：AI等投资拉动需求，储蓄率下降，模型显示中性利率可能向3.5%-4%靠\n\n[... middle omitted ...]\n\nf short rates, pointing to a structural shift in how duration risk is priced (Figure 1).\n\n\\- Budget deficits remain elevated across major economies, but the causes differ across regions: in th\n\n[... middle omitted ...]\n\npermission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request.\n\n## BRCF2242"
  },
  {
    "id": "R003",
    "title": "JPM：全球经济的“滞胀幻觉”正在被打破，真正的周期上行已经启动",
    "digest": "[wechat_article.md]\n# JPM：全球经济的“滞胀幻觉”正在被打破，真正的周期上行已经启动\n\n当市场还在为中东冲突引发的能源价格飙升和通胀反弹焦虑时，JPM在最新发布的2026年中期全球经济展望中给出了一个反直觉的结论：全球经济并未滑向滞胀，而是处于一轮由商业信心修复、科技投资扩散和库存周期重启共同驱动的“自觉再耦合”之中。\n\n这份由全球首席经济学家Bruce Kasman领衔的报告，核心判断清晰而有力：去年贸易战导致的企业悲观情绪正在消退，非科技领域的投资和雇佣正在从低迷水平反弹，而AI投资正从超大规模云厂商向更广泛的产业扩散。尽管能源冲击让全球GDP增速在年中出现阶段性下移，但多重缓冲因素将在下半年推动经济重新加速。\n\n这是当前宏观叙事中一个重要的分歧点。市场的主流预期是“结构性放缓+通胀黏性”，而JPM看到的，是一个被能源冲击暂时掩盖但正在自我强化的周期上行。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 商业信心的“V型修复”是理解本轮周期的关键变量\n\nJPM的分析框架中，最核心的驱动力并非货币或财政政策，而是企业心理状态的转变。报告明确指出，2025年贸易战导致全球商业信心跌至谷底，企业暂停了非科技领域的资本开支和招聘。而进入2026年，这种“过度谨慎”正在自然消退。\n\n报告构建的全球商业预期指数显示，该指数在2026年初已开始反弹，虽因中东冲突短暂中断，但随着霍尔木兹海峡重新开放和能源价格回落，这一修复进程将在未来几个月重新启动。尤其值得注意的是，西欧地区在冲突期间经历了最显著的情绪下滑，因此修复空间也最大。\n\n> **KC评论：** JPM将“商业信心修复”而非任何政策变量作为周期上行的催化剂，这个视角值得重视。这意味着，如果判断成立，本轮复苏将具有更广泛的内生性——不是靠刺激“推”出来的，而是企业自己“走”出\n\n[... middle omitted ...]\n\n更多产业决策者和专业投资者一起，持续跟踪这些关键变量的演变。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球经济的“中场战事”\n\n🌍 经济周期正在换挡\n\n上半年能源价格冲击不小，但全球经济比想象中更有韧性。科技投资持续火热，企业招聘和非科技支出开始回暖，这些都在支撑一个“高于潜力”的增长节奏。\n\n1️⃣ 企业信心正在修复\n去年贸易摩擦让企业缩手缩脚，但今年初开始，商业情绪已经触底反弹。中间虽然被中东局势打断，但随着霍尔木兹海峡重新开放，情绪修复有望在下半年加速。尤其是西欧，之前跌得最惨，反弹空间也最大。\n\n2️⃣ 消费放缓，但工业有支撑\n油价上涨挤压了购买力，全球零售可能会在年中走弱。但工业产出不会跟着躺平——科技支出还在扩张，库存周期也在转向，制造业有理由保持活跃。就业市场也在改善，美国每月新增岗位有望稳定在10万以上。\n\n3️⃣ 通胀黏性超出预期\n核心通胀连续第六年高于央行目标，预计2026年全球核心CPI涨幅超过3%。核心商品价格涨幅从0.9%跳升至2%，服务业通胀也反弹到3.8%。工资增速虽然放缓，但仍在3.5%，比2000年代扩张期的高点还高。\n\n4️⃣ 央行面临两难\n通胀黏性叠加劳动力市场紧张，美联储、欧央行等大概率会继续加息。但金融条件目前仍偏宽松，全球政策利率未来一年累计上调预计不到30个基点。\n\n[... middle omitted ...]\n\nit of Hormuz. However, global GDP growth is still expected to downshift into midyear as the recent CPI spike softens consumption gains.\n\n\\- Several factors should temper this downshift and set\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R004",
    "title": "GS：日本造船业的“经济安全”逻辑，正在催生一个被低估的结构性机会",
    "digest": "[wechat_article.md]\n# GS：日本造船业的“经济安全”逻辑，正在催生一个被低估的结构性机会\n\n日本政府正在将造船业从“夕阳产业”的叙事中彻底剥离，并重新定义为经济安全的核心支柱。这并非空洞的口号，而是正在转化为有明确数字、时间表和投资规模的产业政策。\n\n这份来自GS日本策略团队的研报，核心判断是：日本造船业正站在一个由地缘政治和产业政策共同驱动的结构性拐点上。其意义不仅在于订单量的恢复，更在于日本政府正在用“经济安全”的框架，重塑整个产业的竞争逻辑——从追求规模转向掌控关键节点，从单纯造船转向技术主权。\n\n报告最值得关注的信号，并非日本要造多少船，而是它明确了要在哪些领域建立“不可替代性”：下一代零排放船舶、LNG运输船、军舰建造与维护、港口起重机。这四个领域，每一个都直指全球供应链的脆弱环节。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 政策目标不是“重回第一”，而是“守住关键节点”\n\n日本政府提出的目标非常具体：到2035年，将国内造船量在2024年基础上翻倍。但更值得解读的是，这个目标背后的逻辑并非追求全球份额第一，而是为了“确保国际竞争力”和“稳定供应”。\n\nGS在报告中直接点明了这一转变的背景：当前日本国内造船量，已经低于日本船东和运营商的自身需求。这意味着，日本造船业过去几十年的萎缩，已经触碰到了经济安全的底线——一个岛国，连自己商船队的造船需求都无法满足，这在战略上是不可以接受的。\n\n因此，这轮政策的本质是“补短板”和“建壁垒”。目标不是与中韩在常规商船领域打价格战，而是在下一代船舶、LNG运输船、军用舰艇和港口设备这些高附加值、高技术壁垒、且与国家安全直接相关的领域，建立日本自己的供应体系。\n\n> **KC评论：** 理解这一点很重要。如果你用“造船业复苏”的旧框架去看，会认为日本的目标只是增加订单量。但GS研报揭\n\n[... middle omitted ...]\n\n报摘要与数据图表，帮助你在第一时间把握产业和市场的动态变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本造船业：经济安全视角下的战略押注\n\n造船业，重回国家战略C位\n\n日本政府最新增长战略会议披露了一份文件，核心信号很明确：造船业不只是造船，而是经济安全的关键拼图。\n\n1/ 目标翻倍：到2035年，国内造船量要在2024年基础上翻一番。靠的不是盲目扩产，而是下一代船舶（零排放船舶）的技术卡位。日本船东的需求目前国内供给根本接不住，缺口就是机会。\n\n2/ LNG船：日本过去是LNG船建造强国，但2019年后国内已无新船订单。现在政府目标——2035年起，每年在国内建3-5艘LNG船，把流失的建造技术链重新接上。\n\n3/ 修船市场：目前日本90%以上的修船业务集中在近海船，远洋船严重依赖海外。政府计划投入1000亿日元（公私合计）提升修船产能，包括政府船只错峰维修、引入自动化、利用友好国家设施。\n\n4/ 港口起重机：日本企业在岸桥和场桥的全球存量份额约10%，对手一家独大。目标是对美出口份额到2040年达到30%，年销售额200-300亿日元。Mitsui E&S（国内订单份额100%）是直接受益方。\n\n5/ 防卫装备：最上级护卫舰已引起盟国兴趣，小型无人机、舰艇出口是重点。防卫采购预算FY2026约3400亿\n\n[... middle omitted ...]\n\nant from the perspective of Japan's economic security in our view, and we will be watching their business development leveraging future policies. We maintain our Buy rating on all three compan\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R005",
    "title": "GS：数据中心最大的瓶颈不是电力，是碳化硅",
    "digest": "[wechat_article.md]\n# GS：数据中心最大的瓶颈不是电力，是碳化硅\n\n全球数据中心正在经历一场由AI驱动的需求爆发，但多数市场参与者仍然把注意力放在“电够不够”这个问题上。这份GS近期组织的专家电话会纪要，提供了一个来自产业链核心供应商的视角，其结论比表面看到的更尖锐：电力确实紧张，但真正卡住全球数据中心扩张速度的，是晶体管——更具体地说，是碳化硅（SiC）功率器件的供应。这个瓶颈的缓解时间表，将直接决定未来两年超大规模云厂商和托管服务商的交付节奏。\n\n这份研报解析的价值，不在于复述“AI带动数据中心需求”这个已知事实，而在于揭示一个正在发生的权力转移：过去是基础设施决定部署什么设备，现在是英伟达的架构和生态在倒逼基础设施重新设计。从电源到冷却，从布线到预制模块，整个产业链的竞争逻辑正在被重写。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 供应链正在从“规模竞赛”转向“关系竞赛”，锁单能力成为新护城河\n\nGS这份电话会纪要最直接的信号，来自Delta Electronics——全球最大的服务器和笔记本电脑电源供应商，市占率约60%-70%，同时也是全球最大的液对气冷却制造商。Delta的管道订单规模已经远超其生产能力，尤其在基础设施侧。这意味着什么？不是所有数据中心玩家都能拿到货。\n\nDelta认为，未来最有竞争力的托管服务商，将是那些拥有最强供应链关系并已锁定远期订单的企业。这不是一个温和的警告。在全球UPS解决方案持续紧张、Delta自产电池未来18个月已全部售罄的背景下，供应链的“先到先得”逻辑正在取代“价高者得”。对于正在规划新数据中心的企业而言，现在需要评估的不是“我们能不能拿到地/电”，而是“我们能不能拿到设备”。\n\n> **KC评论：** 很多投资者还在盯着土地审批和电网容量，但Delta的信号表明，设备交期可能成为\n\n[... middle omitted ...]\n\n的走向、800VDC的推广节奏、以及碳化硅供应瓶颈何时缓解。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球数据中心，正在经历一场静悄悄的大洗牌\n\n🌍数据中心正在被AI重塑\n\n最近听了一位行业专家的分享，聊聊全球数据中心（DC）产业的关键变化。\n\n1️⃣ 供应链紧张，谁有货谁赢\n全球最大电源供应商的订单积压远超产能，尤其是基础设施端。关键瓶颈在碳化硅晶体管，交期从10-20周飙到40周。UPS电源也极度紧缺，某全球供应商自产电池已售罄未来18个月。\n\n2️⃣ AI反过来倒逼基础设施\n以前是基础设施决定放什么设备，现在是英伟达架构倒逼生态配套。液冷方案正从改造项目转向新建项目，空气冷却项目预计2028-2030年减少5%-10%。\n\n3️⃣ 预制化数据中心是趋势\n新型AI模块化方案能缩短部署时间50-60%，产能计划6个月扩4倍。微软和AWS坚持传统方案，但区域部署靠托管商，美国自建占90%。\n\n4️⃣ 800V高压直流电是下一个突破口\n与英伟达联合开发，用更少铜和线缆（2根vs原来4-5根），系统成本有望降30-40%。预计2027上半年在澳洲、欧洲、东南亚落地。\n\n5️⃣ 新规可能推高成本\n澳洲拟要求100MW以上数据中心配备电池储能系统，成本可能翻倍。目前全球还没有UPS系统能合规。\n\n欢迎一起讨论数据中心\n\n[... middle omitted ...]\n\n annabel.li@gs.com  \nGS Australia Pty Ltd\n\nChao Wang\n+886(2)2730-4195 | kuan-\nchao.wang@gs.com\nGS (Asia) L.L.C., Taipei\nBranch\n\nJamie Laskovski  \n+61(2)9321-8688 |  \njamie.laskovski@gs.com  \nG\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R006",
    "title": "BARC：盈利周期未过热，但市场已容不下意外",
    "digest": "[wechat_article.md]\n# BARC：盈利周期未过热，但市场已容不下意外\n\n这份来自BARC的2026年第三季度全球宏观展望，在谨慎乐观的表象下，藏着一个对投资者而言至关重要的判断：当前全球市场的核心矛盾，不是经济是否在扩张，而是市场定价已经提前透支了大部分利好。\n\n报告开篇便点明，第三季度的市场前景取决于一个张力——以美国为主的盈利周期仍在强劲交付，但市场已经吸收了大部分好消息。这种张力如何化解，将决定未来几个月的金融市场走向。BARC的结论是，全球扩张的基本面依然稳固，但投资者的自满情绪，恰恰是目前最大的风险。\n\n这不是一份简单的看多或看空报告。它更像是一份关于“何时需要警惕”的路线图。BARC用详实的数据告诉你，经济的引擎还在轰鸣，但仪表盘上的警示灯已经开始闪烁。\n\n> **KC评论：** BARC的核心主张是“Long the cycle, short the complacency”。翻译成大白话就是：你可以继续看好经济周期本身，但必须警惕市场过度乐观带来的脆弱性。这份报告最值得读的，不是它说了什么，而是它揭示了哪些“看似美好，实则危险”的细节。\n\n![研报原图 1](assets/xhs_card_01.png)\n\n## 1. 盈利周期正在扩散，但市场已经为此支付了溢价\n\n美国企业的盈利周期，仍然是全球宏观的主导力量。第二季度标普500指数每股盈利同比增长19%，这本身就值得关注。但更关键的是盈利的构成。大型科技股贡献了30%的增长，这已是预期之内。真正的惊喜来自科技板块的其他部分——盈利同比飙升50%，这一速度表明，人工智能的货币化进程早已超越了少数几家巨头。\n\n材料板块受益于AI基础设施建设，利润率正在扩张。金融板块则受益于股市上涨和交易活跃。医疗保健在经历疫情后的利润率压缩后，也开始看到运营杠杆的回归。当盈利周期以这种方式扩散时，它会形成自我强化的循环：行业层面的\n\n[... middle omitted ...]\n\n报告背后的更多细节，以及如何将这些判断转化为自己的投资框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球盈利扩张，市场定价偏满\n\n盈利周期还在，但容错空间收窄\n\n某外资投行最新Q3展望，核心观点一句话：全球（尤其美国）盈利周期依然强劲，但市场已经把好消息price in了，容错空间收窄。\n\n1️⃣ 盈利不再是科技巨头的独角戏\n- S&P 500二季度盈利同比增长19%，其中非科技巨头EPS飙升50%\n- 材料、金融、医疗板块利润也在扩张，盈利周期正在自我强化\n- 风险在于：当前指数已隐含2027年双位数EPS增长预期，一旦利润率受挤压，市场会紧张\n\n2️⃣ 美国劳动力市场：企稳，但没过热\n- 失业率维持在4.3-4.4%附近，工资压力不明显\n- 就业增长广泛，但距离推高工资成本还有距离\n- 这对盈利周期是利好：就业支撑消费，消费支撑收入\n\n3️⃣ 消费者：数据看似脆弱，实际没那么糟\n- 储蓄率2.6%确实低，但过去两年BEA都大幅上修过储蓄率\n- 财政赤字、股市财富、AI资本开支都在支撑消费\n- 认为消费会大幅下滑，需要忽略太多正面因素\n\n4️⃣ AI资本开支：争论已结束，建设还在继续\n- 主要云平台AI年化收入过去一年翻了三倍\n- 2027年AI基础设施总支出可达1万亿美元\n- 这些支出是合同性的，不是可\n\n[... middle omitted ...]\n\nthe ECB and BoJ will likely tighten policy at the margin, but we expect the Fed to stay on hold for the rest of the year. Bonds remain the most challenged asset class, as fiscal and inflation \n\n[... middle omitted ...]\n\nrior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request."
  },
  {
    "id": "R007",
    "title": "BARC：标普500目标上调至7800，但真正驱动上涨的不是估值",
    "digest": "[wechat_article.md]\n# BARC：标普500目标上调至7800，但真正驱动上涨的不是估值\n\n2026年过半，美股在经历了一场地缘政治冲击、AI叙事震荡和通胀反复的过山车之后，标普500指数距离历史高点仅一步之遥。但投资者普遍感到困惑：这个市场是靠什么涨起来的？估值已经不算便宜，美联储降息遥遥无期，消费数据开始走软，AI资本开支的回报周期仍不清晰。\n\nBARC最新发布的美国权益策略报告给出了一个清晰但反直觉的答案：这轮上涨的驱动力不是估值扩张，而是盈利。该机构将2026年标普500每股盈利预测从321美元上调至337美元，并将年底目标价从7650点上调至7800点。更值得关注的是，他们同步给出了2027年的盈利预测和目标价——389美元和8800点。\n\n这是一个“盈利接棒”的故事。当宏观环境从“软着陆”滑向“滞胀边缘”，当市场定价权从美联储转向企业基本面，真正能推动指数向上的，只有利润的实打实改善。但这份报告也坦诚地指出了盈利增长背后的脆弱性：AI资本开支的融资压力、消费端的滞后风险、以及利率重新成为核心风险因子。这些矛盾点，恰恰是投资者需要深入阅读完整报告才能把握的细节。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 市场的韧性来自盈利，而不是估值\n\nBARC的定价框架调整本身就说明问题。他们将2026年标普500目标价从7650点上调至7800点，但同时将估值倍数从约24倍下调至23.1倍。这意味着，目标价的上调完全由盈利增长驱动，估值反而被压缩了。\n\n这种“盈利上修、估值下修”的组合，反映了BARC对当前市场环境的判断：宏观不确定性依然存在，但企业盈利的韧性正在超出预期。报告指出，1季度财报季表现显著强于预期，科技板块的盈利增长达到了2010年以来最好的水平，全年盈利指引的上修速度也创下了历史纪录。\n\n> **KC评论\n\n[... middle omitted ...]\n\nics。欢迎加入我们的星球和微信群，继续讨论这些未解的问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n标普上调目标价，但风险在哪\n\n📈 7800点\n\n不确定性中上调盈利预期\n\n某外资投行最新研报认为，虽然宏观环境复杂，但美股盈利前景正在改善。他们把2026年标普500每股盈利预测从$321上调至$337，年底目标价也从7650点提高到7800点。\n\n几个关键判断👇\n\n1⃣ 盈利增长是核心驱动力\n- 2026年EPS增速预计达21%，主要来自科技板块的AI需求转化\n- 工业端也相对支持，部分对冲消费端压力\n- 这是基于1季度财报季超预期、再通胀支撑名义收入增长\n\n2⃣ 估值反而在压缩\n- 目标估值从24倍降至23倍PE\n- 原因是AI资本开支规模、融资方式、货币化时间线仍存不确定性\n- 更高的名义收益率和通胀也在压制估值\n\n3⃣ 行业观点有调整\n- 金融和医疗板块从看多转为中性\n- 继续看好TMT、工业、公用事业\n- 对消费板块保持谨慎\n\n4⃣ 下半年需要关注的风险\n- AI投资周期是否出现压力信号：模型进步速度、电力供应、融资复杂度\n- 新美联储主席上任后利率路径的重新定价\n- 通胀回升对消费者购买力的滞后影响\n\n研报给出的三种情景：\n- 牛市：EPS $343，目标8500点\n- 基准：EPS $337，目\n\n[... middle omitted ...]\n\n push rate cuts further out. Input costs are rising again, though not yet a growth shock large enough to derail the cycle. The equity bull case remains intact, but earnings and AI capex visibi\n\n[... middle omitted ...]\n\nrior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request."
  },
  {
    "id": "R008",
    "title": "GS：市场正在快速定价一个未来的供应过剩",
    "digest": "[wechat_article.md]\n# GS：市场正在快速定价一个未来的供应过剩\n\n这份GS最新发布的《Oil Tracker》报告，在短短一周内捕捉到了一个关键信号：市场情绪和定价逻辑正在发生一次方向性的转变。报告的核心判断并非关于油价本身，而是关于市场如何解读近期的一系列事件。\n\n过去一周，布伦特原油现货价格下跌了8%。直接的触发因素包括美伊谈判取得“重大进展”、波斯湾石油流量显著回升、美国发布授权伊朗石油销售的60天豁免，以及原油持仓的持续下降。但GS认为，这些事件背后更重要的含义是，市场正在从对供应中断的担忧，快速转向对未来供应过剩的定价。\n\n这意味着，油市交易的核心叙事已经切换。投资者不应再仅仅盯着地缘政治事件本身，而需要审视市场如何对这些事件进行“二阶”定价。这份报告提供了一套完整的分析框架，帮助我们理解这种叙事切换的底层逻辑、当前所处的阶段，以及哪些关键变量可能打破这一预期。\n\n> **KC评论：** GS这份报告最有价值的地方，不在于它预测了油价会跌到多少，而在于它指出了市场正在“快进”到对未来供需平衡的定价。这提醒我们，当市场开始为尚未发生的过剩定价时，基于当前现货价格的交易策略可能需要重新审视。完整报告中关于“安全溢价”消退的详细论证，是理解当前市场心态转变的关键。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 波斯湾出口的恢复速度，正在重塑市场对供给弹性的认知\n\n报告中最引人注目的数据是，波斯湾总出口量已恢复到正常水平的63%（以7天移动平均计）。霍尔木兹海峡的可见流量正在快速恢复，这既反映了更多船只的通行，也反映了更多船只重新打开了AIS信号，使得“可见”流量增加。自6月11日以来，霍尔木兹海峡周边未再报告有船只遇袭事件。\n\n这一恢复速度本身就是一个重要信号。此前市场普遍认为，如此大规模的供应中断需要数月甚至更长时\n\n[... middle omitted ...]\n\n话题有更深入的兴趣，欢迎加入我们的星球微信群，继续交流讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n海湾原油快速回归，市场提前定价过剩\n\n供需天平正在倾斜\n\n上周布伦特原油跌了8%，原因很直接：美伊谈判有重大进展、波斯湾油轮流量快速回升、美国还发了60天的伊朗石油豁免许可。市场已经开始提前消化未来的供应过剩。\n\n1️⃣ 供应端恢复速度超预期\n- 海湾地区总出口已恢复到正常水平的63%（7天移动平均）\n- 霍尔木兹海峡的可观测流量快速回升，更多油轮重新打开AIS信号\n- 波斯湾空油轮运力持续增加，上周新增5200万桶空船进入，同期只有5300万桶装载离开\n- 不过伊拉克西古尔纳2油田因缺空油轮已暂停生产（这是目前唯一的瓶颈）\n\n2️⃣ 伊朗石油豁免释放库存\n- 美国60天豁免可能释放约6000万桶伊朗海上浮油\n- 但即使制裁延续到8月21日之后，伊朗产量大幅增加的可能性不大\n- 亚洲（尤其中国）仍是伊朗原油主要买家，欧盟和英国制裁依然存在\n- 有意思的是：2020-2025年伊朗在“极限施压”下产量仍增长了130万桶/天（+59%），说明制裁对生产的约束力可能被高估\n\n3️⃣ 库存消耗速度明显放缓\n- 全球可见库存消耗从5月的550万桶/天降至6月的180万桶/天\n- 海上运输中的原油自3月底以来增加了1.3\n\n[... middle omitted ...]\n\nof visible Hormuz flows (Exhibit 6), likely reflecting more crossings and a larger share of crossings that are “visible” (ships that are now keeping their AIS on).\n\n☐ Empty tanker capacity con\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R009",
    "title": "HSBC：消费谨慎，但资本正在重新发现中国",
    "digest": "[wechat_article.md]\n# HSBC：消费谨慎，但资本正在重新发现中国\n\n2026年陆家嘴论坛刚落幕，一份来自HSBC的宏观周报给出了一个看似矛盾、实则逻辑清晰的判断：中国消费端仍然谨慎，但金融开放与外资流入正在形成新的正向循环。\n\n这份报告没有用“复苏”或“放缓”这样的单一标签来概括当前经济。它呈现的是一幅更精细的图景——消费与投资的温差在扩大，政策工具箱在加速重构，而外资对中国的兴趣正在从“成本导向”转向“创新导向”。\n\n如果你只关注端午节人均消费低于2019年14%的数据，可能会得出悲观的结论。但HSBC经济学家提醒我们，另一个信号同样重要：2025年前五个月，近4000家外国企业在华扩大投资，美国对华直接投资同比增长17.3%，沙特投资更是暴增285.5%。\n\n这不是一个简单的“好不好”的问题。这是一个“结构正在被重新定义”的时刻。\n\n> **KC评论：** 很多投资者习惯用消费数据来判断中国经济的温度，但HSBC报告真正想说的是——消费只是拼图的一块。金融开放、外资回流、人民币国际化，这三条线索正在形成一条新的逻辑链。完整报告里有一张“真实FDI”的图表，剔除了所谓的“幽灵投资”，值得仔细看。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 陆家嘴论坛发出的信号：金融开放不再是口号，而是有具体工具支撑\n\n2026年陆家嘴论坛释放的政策信号，其密度和操作性都超出了市场预期。HSBC报告指出，央行、金融监管总局、证监会、外汇局四部门的发言，共同指向一个方向：高水平金融开放正在进入“工具落地”阶段。\n\n最值得关注的不是某个单一政策，而是这些政策背后的逻辑链条。央行推出了面向境外央行的FIMA人民币回购工具，同时调整了临时隔夜回购和逆回购操作工具的利率区间。这意味着什么？人民币的流动性管理工具正在向国际标准靠拢——以隔夜利率作\n\n[... middle omitted ...]\n\n真实动态。\n\n这里没有噪音，只有经过筛选的信息和持续的讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n金融开放进入实操阶段，消费端还在等风来\n\n金融开放加速，消费仍需观察\n\n最近投行研报覆盖了陆家嘴论坛、消费数据和财政支出几个关键信号，信息量不小，挑重点拆一下。\n\n1️⃣ 陆家嘴论坛：金融开放进入实操\n- 高层明确支持高水平金融开放，要试点离岸金融业务，包括离岸贸易融资、自贸区离岸债券等\n- 六家大行获准在上海自贸区开展离岸人民币外汇交易\n- 央行为海外央行设立人民币回购工具，支持人民币国际化\n- 货币政策工具调整：临时隔夜回购利率走廊从70bp缩窄到50bp，有助于控制季末资金波动\n\n2️⃣ 消费：节日数据偏弱\n- 端午节假期旅游人次同比+4.4%，总花费+4%，但人均消费仍比2019年低14%\n- 618大促GMV约8640亿，同比基本持平，商品需求偏弱\n- 服务业增速（5.4%）明显好于商品零售（1.4%），服务消费是亮点\n\n3️⃣ FDI：外资仍在加码\n- 商务部发布新行动计划，扩大服务业、金融、医药等领域准入\n- 今年前5月近4000家外资企业在华扩大投资\n- 美国对华FDI同比+17.3%，沙特投资激增285.5%\n- 外资研发中心集中在医药领域，占研发投资70.8%\n\n4️⃣ 财政支出：基建放缓\n\n[... middle omitted ...]\n\nrticipating. The commitment to high-level opening-up, capital market reforms, and monetary policy reform was evident in their speeches, while a slew of measures was also unveiled (see Table 1).\n\n[... middle omitted ...]\n\nhugo.pienaar@hsbc.com\n\n## Latin America\n\nChief Economist, Mexico\nJose Carlos Sanchez +52 55 5721 5623\njose.c.sanchez@hsbc.com.mx\n\nHead of Brazil Economics Research\nDaniel Lavarda +55 11 2802 2640\ndaniel.lavarda@hsbc.com"
  },
  {
    "id": "R010",
    "title": "JPM：日本370万亿投资计划，国债市场才是真正的考场",
    "digest": "[wechat_article.md]\n# JPM：日本370万亿投资计划，国债市场才是真正的考场\n\n日本政府刚刚公布了一项雄心勃勃的蓝图：到2040年，通过官民合作撬动超过370万亿日元的投资，覆盖AI、半导体、生物技术等17个战略领域。市场第一反应往往是“增长叙事”，但JPM日本利率策略团队在最新报告中指出一个更值得关注的信号：这笔投资的融资方式——而非投资本身——才是决定日本国债市场未来五年走向的关键变量。\n\n报告的核心判断是：即便通过特别账户和桥接债券来维持形式上的财政纪律，日本国债的实际供给压力可能从2027财年起显著上升。当高市政府的扩张性财政与消费税减税、国防支出缺口等多重因素叠加，日本财务省的调控空间正在被压缩。\n\n这不是一份关于“日本能否实现增长”的报告，而是一份关于“增长的成本由谁承担”的预警。以下是我们从这份报告中提炼出的五个关键洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 370万亿的规模不是重点，每年4万亿还是10万亿的政府支出才是分歧所在\n\nJPM报告首先澄清了一个数字迷思。370万亿日元是官民投资总额，政府实际承担的部分取决于“杠杆率”。以GX（绿色转型）投资框架为参照——政府先期投入20万亿日元，撬动150万亿日元总投资，政府占比约15%——按此比例，370万亿日元对应的政府支出约为55万亿日元。\n\n如果这笔支出平均分摊到2027至2040财年的14年间，年均规模约4万亿日元。这在日本国债市场的历史供给中并不算惊人。\n\n但报告同时指出，日本政府在“中长期经济财政展望”材料中给出了另一种模拟：假设2027财年新增财政支出10万亿日元，此后仅随通胀和工资增长上调。在这个假设下，债务/GDP比率仍呈下降趋势。换言之，政府自己也在暗示，实际支出可能更接近10万亿日元而非4万亿日元。\n\n> **KC评论：** 4万亿和10\n\n[... middle omitted ...]\n\n何调整日本国债头寸——欢迎来我们的知识星球和微信群继续交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本370万亿日元投资计划，怎么看？\n\n日本官民投资蓝图曝光\n\n高市政府昨天公布了官民投资政策框架，计划到2040年累计投资超过370万亿日元。核心逻辑是政府先花钱，带动民间资本跟进。\n\n1/ 钱投在哪？\n- AI/半导体：186万亿日元（最大头）\n- 生物科技/新药研发：98万亿日元\n- 资源/能源：29万亿日元\n这三块是增长战略的核心。\n\n2/ 钱从哪来？\n- 从2027财年起，通过特别账户发行“桥梁债券”融资\n- 参考GX投资经验，政府出资比例约15%，按370万亿算，年均约4万亿日元\n- 但官方模拟显示年支出可能接近10万亿日元，规模远超预期\n\n3/ 债券市场压力山大\n- 如果每年真发10万亿债券，JGB供给会显著增加\n- 叠加能源补贴、消费税减免、防务支出等多个财政扩张因素\n- 财务省可能难以完全对冲市场影响\n\n4/ 未来几个关键节点\n- 2026财年：可能出台第二轮补充预算（能源补贴）\n- 2027财年：增长战略债券发行启动，消费税减免落地\n- 2028财年：“防务资金悬崖”出现，防务支出缺口扩大\n\n值得关注的是，7月发布的“基本方针”会给出更多细节。目前很多数字只到2040年，中期政府支出节奏还\n\n[... middle omitted ...]\n\nas a catalyst to encourage private investment, and the introduction of a new investment framework under the “Strong and Prosperous Japan” policy from FY2027 is under consideration, alongside p\n\n[... middle omitted ...]\n\nvirus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase &"
  },
  {
    "id": "R011",
    "title": "NOM：央行加急推出隔夜逆回购，不是降息信号而是框架升级",
    "digest": "[wechat_article.md]\n# NOM：央行加急推出隔夜逆回购，不是降息信号而是框架升级\n\n6月28日，中国央行宣布将于6月29日至30日，通过“固定利率、数量招标”的方式，在公开市场操作中新增隔夜逆回购工具。这一动作距离央行行长潘功胜在陆家嘴论坛上释放相关信号，仅过去了11天。\n\n市场第一反应往往是：央行是不是要降息了？隔夜逆回购利率会不会低于当前7天逆回购的1.40%？流动性宽松是否即将加码？\n\nNOM亚洲经济团队在最新发布的研报中给出了一个与市场直觉相反的核心判断：**这不是政策宽松的信号，而是中国货币政策框架现代化的关键一步。** 央行正在用更精细的工具箱，去“正式化”市场早已定价的事实——隔夜利率才是中国银行间市场真正的资金锚。\n\n本文基于这份研报，梳理其核心逻辑与未完全展开的悬念。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 央行不是在放水，而是在重新定义利率传导的“最后一公里”\n\n理解这一操作的关键，不在于利率水平的高低，而在于央行正在解决一个长期存在的结构性错配。\n\n中国银行间回购市场，隔夜品种的交易量长期占据绝对主导地位。这意味着，金融机构实际的资金成本锚定的是隔夜利率（DR001/R001），而非政策工具所锚定的7天利率。但过去，央行公开市场操作的主力工具却是7天逆回购。这就形成了一个奇怪的“错位”：政策信号通过7天利率发出，但市场实际运作却以隔夜利率为基准。\n\nNOM报告指出，央行推出隔夜逆回购，是对这一市场现实的正式认可和制度化。通过将操作利率走廊从原先的“7天利率加减一定幅度”，调整为以隔夜利率为核心、对称50个基点的走廊，央行实际上是在用更贴近市场运作节奏的工具来传导政策意图。\n\n> **KC评论：** 这就像一家公司一直在用季度考核来管理员工日常表现，现在终于开始引入周报制度。工具变了，不代表公司目标变了，而\n\n[... middle omitted ...]\n\n速把握全球市场dynamics。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n央行悄悄加了个夜盘工具\n\n央行上线隔夜逆回购\n\n利率走廊收窄，信号更强\n\n最近央行在公开市场操作里加了个新工具——隔夜逆回购。这事其实6月17号陆家嘴论坛上潘功胜行长就预告过，只是没想到动作这么快。\n\n1️⃣ 隔夜逆回购是什么？\n简单说，央行以前主要用7天逆回购来调控市场利率，但银行间市场实际交易量最大的其实是隔夜品种。这就好比用1米尺子量2厘米的东西，不太匹配。现在补上这把短尺，调控更精准。\n\n2️⃣ 利率大概定多少？\n根据DR007和DR001的利差（过去12个月平均约12bp），研报推测隔夜逆回购利率可能在1.30-1.35%，比当前7天逆回购利率1.40%略低。注意，这不算降息，只是不同期限的自然价差。\n\n3️⃣ 利率走廊在调整\n原来隔夜利率的上下限是7天逆回购利率+50bp和-20bp，现在改成+25bp和-25bp。更窄更对称的走廊，政策信号更清晰。而且下沿调低，说明央行对流动性充裕的容忍度边际上升了。\n\n4️⃣ 操作时间也改了\n临时隔夜操作窗口从16:00-16:20调到15:00-15:30。别小看这半小时，以前离市场收盘太近，机构根本来不及调头寸，现在窗口提前，给了更多匹配时间。\n\n5️⃣ \n\n[... middle omitted ...]\n\nthe current 7d OMO rate of 1.40%. We view the introduction of overnight OMO as part of the PBoC’s ongoing efforts to modernize its monetary policy framework and bring itself closer in line wit\n\n[... middle omitted ...]\n\nable upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R012",
    "title": "GS：欧洲公用事业股的下行已近尾声，真正的机会藏在电气化超级周期里",
    "digest": "[wechat_article.md]\n# GS：欧洲公用事业股的下行已近尾声，真正的机会藏在电气化超级周期里\n\n当市场目光聚焦于中东局势的每一个转折，欧洲公用事业板块的投资者正经历一场典型的“叙事切换”。霍尔木兹海峡一旦重新开放，资金会迅速从防御型资产轮动至周期敏感型板块。GS在最新发布的研报中直接点明：公用事业板块近期的相对弱势可能还会持续一小段时间。但这份报告的真正价值不在于判断短期轮动，而在于给出了一个反直觉的主判断——公用事业板块的下行已近尾声，一个由电气化驱动的盈利超级周期正在形成，而当前恰恰是布局的窗口期。\n\n这份由首席分析师Alberto Gandolfi领衔的报告，没有停留在地缘政治的短期扰动上。它试图回答一个更根本的问题：当市场的噪音消退，欧洲公用事业真正的价值锚点在哪里？答案是，在一个被严重低估的结构性趋势里——欧洲正在迎来一场规模空前的电气化投资浪潮。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 短期承压是“去风险”的必要过程，而非趋势逆转\n\nGS的分析框架清晰地划分了两个阶段。冲突初期，公用事业作为防御板块跑赢大盘，资金涌入可再生能源和电力安全主题。但随着冲突预期延长，市场转而担忧利率上升和资本成本提高，板块开始承压。而一旦和平协议达成，这种承压可能暂时加剧——因为资金会轮动到直接受益于霍尔木兹海峡重新开放的板块，同时大宗商品价格暴跌也会影响IPP和可再生能源开发商的短期利润。\n\n但报告的核心洞察在于：这种承压是“去风险”过程的一部分，而非趋势的逆转。GS明确提出，板块即将被“去风险化”，而他们正在寻找入场点。这个判断建立在五个结构性驱动力之上，每一个都指向同一个方向：欧洲电力需求的长期增长曲线已经发生了根本性的跃迁。\n\n> **KC评论：** 理解这份报告的关键，在于区分“交易性叙事”和“结构性周期”。短期承压是交易层面的\n\n[... middle omitted ...]\n\nI，也方便人工快速把握市场动态。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n欧洲公用事业，拐点要来了？🔌\n\n电力需求爆发前夜\n\n最近中东局势缓和，资金从防御板块流出，公用事业表现暂时偏弱。但某外资投行认为，这个阶段快结束了，公用事业正站在一个重要的转折点上。\n\n核心逻辑很清晰，拆成三点：\n\n1️⃣ 电力需求正在加速增长\n2025年起，欧洲电力需求由负转正。热泵、电动车普及，加上数据中心建设热潮（在建20GW，接入申请高达500GW，相当于欧盟用电量的1.5倍），预计2028-29年起每年拉动用电增长1.5-2%。\n\n2️⃣ 基础设施缺口巨大\n电网平均40岁“高龄”，电厂退役加速，投资需求未来十年高达2.5-3.5万亿欧元，而过去十年仅1.5万亿。缺口意味着回报率提升空间，特别是可再生能源和灵活发电领域。\n\n3️⃣ 盈利超级周期可期\n主要电力公司有望保持高个位数到低两位数的盈利增长，持续到2030年代。这轮盈利修复将推动估值扩张，并降低板块对利率和商品价格的敏感度。\n\n具体哪些公司值得关注？\n\n🔹 Enel（目标价€12）\n短期利率下行降低成本，电网业务占EBITDA超40%，年增长7-8%。美国15GW可再生能源项目在竞标中，预计EPS年复合增长7%，当前估值仅12.5倍PE，远低于\n\n[... middle omitted ...]\n\no sectors more positively geared to a re-opening of the Strait of Hormuz, and as a sharp fall in commodities could affect IPPs and Renewable Developers. And yet, we think this underperformance\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R013",
    "title": "JPM：日本化妆品巨头正集体失速于中国战场",
    "digest": "[wechat_article.md]\n# JPM：日本化妆品巨头正集体失速于中国战场\n\n中国市场回暖的迹象并未均匀惠及所有人。当进口数据持续攀升、本土品牌加速崛起，那些曾经依赖中国消费者实现增长的日本化妆品巨头，正在经历一场前所未有的压力测试。\n\nJPM最新发布的日本化妆品行业季度前瞻报告，覆盖了资生堂、高丝、宝丽奥蜜思控股以及乐敦制药四家核心标的。报告的核心判断并非关于营收能否达标——分析师认为，即使这些公司即将公布的4-6月业绩符合指引，也难以提振市场对未来增长的预期。\n\n真正的问题是：这些公司是否拥有足够清晰的核心品牌增长战略和利润率提升路径？从目前的数据来看，答案并不乐观。\n\n> **KC评论：** 这份报告的结论对持有或关注日本消费股的投资者来说，是一个重要的警示信号。它不是在讨论短期波动，而是在质疑这些公司的中期增长引擎是否已经熄火。完整报告里包含了每家公司的详细估值表和汇率敏感性分析，这些数据将直接决定你的持仓风险。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 中国市场的“温差”正在拉大，进口激增掩盖了本土消费的疲软\n\n报告引用的4-5月数据显示，中国化妆品零售环境复苏速度正在放缓。大型零售商店的化妆品销售额同比增速在经历了年初的短暂反弹后，再次出现波动。与此同时，化妆品及盥洗用品进口量却保持增长。\n\n这一组数据组合揭示了一个关键矛盾：进口增长并不等于终端消费强劲。更合理的解释是，渠道商在积极备货，但消费者端的实际购买力恢复速度低于预期。对于在中国市场拥有大量业务的日本化妆品公司而言，这意味着库存压力可能在未来几个季度逐渐显现。\n\nJPM特别指出，国内化妆品出货量在4-5月环比有所改善，但竞争格局的恶化程度远超出货量的改善幅度。进口品牌之间、进口品牌与本土品牌之间的价格和渠道争夺战，正在压缩所有人的利润空间。\n\n![研报原图 2](a\n\n[... middle omitted ...]\n\n妆品巨头是否值得逆向布局，或者是否应该等待更明确的拐点信号。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日系美妆Q2前瞻：核心品牌才是胜负手\n\n**谁在逆风扛旗？**\n\n**4-5月数据暗示，国货美妆出货回暖，但进口增加让竞争更卷。**\n\n某外资投行最新研报拆了4家日系美妆Q2（4-6月）预期，结论很直白：即便业绩达标，也很难拉升全年增长预期。关键要看 **核心品牌策略** 和 **利润率修复**。\n\n**1️⃣ 乐敦制药：亚洲扛大旗**\n- Q2预期：固定汇率下销售额同比+5%，营业利润125亿日元（+8亿）。\n- 日本本土：新品热度可能回落，但亚洲市场是核心引擎。\n- 关键看点：收购的余仁生是否已贡献利润。\n- 外部数据：4-5月本土护肤销售略好于市场平均。\n\n**2️⃣ 资生堂：利润修复靠中国和旅游零售**\n- Q2预期：销售额同比持平，核心营业利润205亿日元（+54亿）。\n- 利润增长主要来自：中国、旅游零售（TR），以及美洲亏损收窄。\n- 关注点：创新产品在中国和美国的动销情况。\n- 外部数据：4-5月本土中低价位化妆品销售略低于市场平均。\n\n**3️⃣ 高丝：营销投入效果待检验**\n- Q2预期：销售额同比+6%，营业利润56亿日元（+9亿）。\n- 一季度前置营销投入，二季度看转化。\n- 关键看点\n\n[... middle omitted ...]\n\nconfirm whether companies have strategies to grow their core brands and improve overall margins.\n\n\\- Rohto Pharmaceutical (4527, Overweight): We expect April–June sales growth of around 5% YoY\n\n[... middle omitted ...]\n\ned by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not\n\nCompleted 25 Jun 2026 09:32 AM JST"
  },
  {
    "id": "R014",
    "title": "NOM：人民币中间价模型已释放一个被低估的政策信号",
    "digest": "[wechat_article.md]\n# NOM：人民币中间价模型已释放一个被低估的政策信号\n\n人民币汇率正在经历一段看似平静、实则暗流涌动的时期。市场目光多聚焦于中美利差、出口数据与特朗普关税的博弈节奏，但真正衡量政策意图的晴雨表，往往不在即期价格本身，而在每日开盘前那个被多数交易员快速扫过的数字——中间价。\n\nNOM亚洲外汇策略团队在最新一期日度模型中，给出了一个值得细读的信号。其模型测算的美元兑人民币中间价预测值为6.8023，较前一日模型预测值6.8209低了186个基点。即使加入逆周期因子调整后，预测值仍为6.8089，较前一日实际中间价低了120个基点。\n\n这不是一个巨大的数字，但它的方向与幅度，在当前的宏观语境下，传递了一个清晰的判断：政策层面对人民币贬值速度的容忍度，可能正在发生微妙但重要的变化。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 模型预测的“下修”幅度，指向的是政策意图而非市场波动\n\nNOM模型的核心价值不在于它预测的绝对点位是否准确，而在于它量化了“如果没有政策干预，中间价应该落在哪里”与“实际中间价落在哪里”之间的差值。这个差值，就是市场理解政策意图的关键窗口。\n\n本次模型预测值较前一日下修186个基点，即便计入逆周期因子后仍下修120个基点，这意味着一件事：在NOM的框架中，隔夜市场因素对人民币的定价方向是偏强的，而非偏弱的。换句话说，模型认为人民币在基本面层面有升值压力，但实际中间价的设定并未完全反映这一压力。\n\n这里需要区分两个概念：模型预测的“方向”与市场交易的“方向”。模型预测下修，代表的是模型认为中间价应当走低（即人民币升值），而不是市场在抛售人民币。这与许多读者直觉中“下修=贬值”的理解正好相反。\n\n> **KC评论：** NOM的模型告诉我们，当前人民币并不缺乏基本面层面的支撑。问题在于，政策层是否愿\n\n[... middle omitted ...]\n\n事件对汇率政策的影响推演，欢迎来知识星球和微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n人民币定价模型发出新信号\n\n6.80附近\n\n短期波动空间收窄\n\n刚刷到某外资投行最新一期亚洲外汇研报，核心结论很干脆：模型对人民币中间价的预测值从6.8209下调至6.8023，下移了186个基点。\n\n这背后的逻辑拆解下来，其实就三点——\n\n1️⃣ 模型本身在修正\n对比上一期预测，模型预测值下降了186pips，说明短期定价压力在减弱。如果加入逆周期因子，预测值是6.8089，比上一次官方中间价低了120pips。这一块说明政策端依然在平滑波动。\n\n2️⃣ 隔夜贡献权重是核心变量\n研报配了一张图，展示了四大隔夜因子对预测变动的贡献权重（研报未给出具体因子名称，这里是推测），这是模型调整的最直接驱动力。简单理解，就是夜间交易时段的价格变化，在模型里被赋予了更高权重。\n\n3️⃣ 未来几个关键时间窗口值得留意\n研报列了一个事件日历，值得圈出的是：\n- 7月下旬：政治局经济工作会议\n- 11月：深圳APEC峰会\n- 12月中旬：中央经济工作会议\n- 年底：中美高层互动（研报提到有出访计划）\n\n这些节点往往是政策信号密集期，也是汇率波动容易放大的窗口。\n\n整体来看，模型信号偏向短期压力缓解，但方向性突破还需要更多催化剂\n\n[... middle omitted ...]\n\n76332bd843e0dd905a95ed4474f17b0cee0053d93166c3874.jpg)  \nSource: NOM\n\nFig. 2: Recent model errors (without counter-cyclical factor adjustment)  \n![](images/93bb8ed3d816ba4054e9c2ea76aea8477871\n\n[... middle omitted ...]\n\nOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R015",
    "title": "Bernstein：钠离子电池正在改写光伏基荷电力的经济学",
    "digest": "[wechat_article.md]\n# Bernstein：钠离子电池正在改写光伏基荷电力的经济学\n\n一份来自Bernstein的最新研报，提出了一个足以让能源行业重新思考十年规划的判断：钠离子电池的成本下降速度，可能比市场预期的更快，而它真正颠覆的，不是电动汽车的续航里程，而是太阳能发电与天然气争夺基荷电源的竞争格局。\n\n这份报告的作者团队，包括了Bernstein亚洲能源研究主管Neil Beveridge。他们在欧洲实地调研中发现，德国6月太阳能发电占比已接近25%，西班牙在6月6日一度达到70%。但真正让分析师团队感到“大开眼界”的，是客户对储能技术，特别是钠离子电池的关注热度。\n\n问题的核心在于：当光伏和风电的渗透率超过一定阈值，电网对储能的需求就从“调峰”转向“基荷替代”。而储能的成本，直接决定了这种替代是否具备经济性。Bernstein的报告给出了一组关键数字：如果钠离子电池成本降至每千瓦时50美元，那么光伏加48小时储能的总成本，将能够与天然气联合循环电厂正面竞争。\n\n这不是一个遥远的预测。报告指出，钠离子电池的电芯成本已经同比下跌15%，从每千瓦时66美元降至55美元。而行业龙头宁德时代的董事长曾毓群认为，钠离子电池成本将降至每千瓦时50美元——这比当前磷酸铁锂电池80-90美元的成本低近一半，更只有三元锂电池成本的不到一半。\n\n> **KC评论：** 这个成本差异不是简单的“更便宜”，而是从根本上改变了储能的商业模式。如果钠离子电池能做到每千瓦时50美元，那么“光伏+长时储能”的综合度电成本，就可能低于新建天然气电厂的度电成本。这意味着，能源转型的终局图景，可能不是光伏和天然气并存，而是光伏+储能直接替代天然气。报告后面给出了详细的平准化度电成本测算，值得仔细看。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 钠离子电池的“三重\n\n[... middle omitted ...]\n\n的增长路径有进一步兴趣，欢迎来我们的星球和微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n钠离子电池，光伏的“新搭档”\n\n钠离子电池要起飞了\n\n光伏+储能成本或将低于天然气\n\n最近在看某外资投行的研报，发现钠离子电池的进展比想象中快很多。\n\n简单说，这可能是让太阳能真正成为基荷电源的关键拼图。\n\n1/ 成本优势正在兑现\n- 工业钠价格约5000美元/吨，碳酸锂超20000美元/吨\n- 宁德时代曾毓群预计钠离子电池成本将降至50美元/kWh\n- 对比：LFP磷酸铁锂约80-90美元/kWh，NMC三元超100美元/kWh\n- 研报认为2026年钠电成本将持平LFP，之后优势扩大\n\n2/ 性能不输LFP\n- 循环寿命翻倍：钠离子可达15000次，LFP仅6000-8000次\n- 这意味着每天充放两次可用20年，配合光伏全生命周期无需更换\n- 按美元/kWh/cycle算，钠电成本只有LFP的三分之一\n- 热失控温度约200°C，安全性更好\n- 低温性能优异，-20°C下能量保持率超92%\n- 宁德时代Naxtra电池能量密度达185Wh/kg，接近LFP的190-210Wh/kg\n\n3/ 储能成本下降将改变能源格局\n- 2020年储能系统成本约500美元/kWh，现在降至约150美元/kWh\n- 如果\n\n[... middle omitted ...]\n\n?\n\nOur recent travels in Europe have highlighted two things. Firstly, how hot and sunny it is. In Germany this month roughly 25% of power generation came from solar while in Spain solar share \n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R016",
    "title": "Bernstein：日本车市正在K型分化，丰田和铃木是赢家",
    "digest": "[wechat_article.md]\n# Bernstein：日本车市正在K型分化，丰田和铃木是赢家\n\n当大多数投资者还在用日本汽车总销量、平均ASP、行业利润率这些“平均数”来评估日本车企时，一份来自Bernstein的深度研报揭示了完全不同的图景：日本车市正在经历一场剧烈的K型分化，低端与高端需求同时扩张，而传统中端市场正在被掏空。这不是周期性的波动，而是结构性的重塑。在这轮分化中，丰田和铃木凭借对两极市场的同时覆盖，展现出远超同行的盈利韧性，而本田、日产、马自达和斯巴鲁则面临定位尴尬。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 日本车市的“平均数”正在掩盖一个危险的真相\n\n从2015年到2025年，日本家庭月均新车购车支出仅从1.03万日元微增至1.05万日元，十年涨幅不过2%。如果只看这个数字，你会以为日本车市是一个稳定甚至停滞的市场。但Bernstein拆开收入阶层后发现，这2%的微弱增长是两股相反力量相互抵消的结果。\n\n在年收入低于400万日元的低收入家庭中，新车购车支出全面下降。年收入低于200万日元的家庭，月均支出从2900日元降至2300日元，降幅达22%。年收入300-400万日元的家庭也下降了16%。与此同时，年收入超过2000万日元的高收入家庭，月均支出从2.43万日元飙升至3.20万日元，增幅高达32%。\n\n这意味着，日本车市的整体数据已经失去了参考价值。当市场在低端和高端同时扩张，而中端被压缩时，任何用“平均”来指导决策的分析都会产生严重的误导。\n\n> **KC评论：** 这是典型的“辛普森悖论”——整体趋势与分组趋势完全相反。对于投资者来说，这意味着不能再简单地用日本汽车总销量或行业平均利润率来评估车企前景。真正重要的是，你的持仓车企在K型曲线的哪一端，以及它是否同时覆盖了两端。\n\n![研报原图 2](assets/\n\n[... middle omitted ...]\n\n新数据图表合集，既方便喂给AI，也方便人工快速把握市场动态。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本车市正在“K型分化”\n\n中产塌了，两端在涨\n\n---\n\n**日本车市正在发生一个很有意思的变化：** 买得起车的人越来越愿意花钱，买不起的人干脆不买了。整个市场被劈成了“高端”和“低端”两条路，中间地带正在消失。\n\n**1/ 贫富差距，变成了“有车”和“没车”的差距**\n\n从2015到2025年，低收入家庭（年收入<400万日元）的月购车支出下降了6%~22%不等。而高收入家庭（年收入>1250万日元）反而增加了3%~32%。结果就是，整体保有率虽然从80%降到72%，但高低收入家庭的差距从27个百分点扩大到了30个百分点。\n\n**2/ 购车价格也在“两极化”**\n\n2017年时，100万日元以下的车只占1%，现在涨到了6%；500万日元以上的车从6%涨到了15%。而原来最主流的100-200万日元区间，直接从46%暴跌到19%。中间的“大众市场”正在被抽空。\n\n**3/ 谁在这种结构里活得更好？**\n\n研报分析了几家车企的日本国内销售结构：低端（<200万日元）+高端（>500万日元）的合计占比，铃木最高（74%），丰田第二（43%），本田38%、马自达37%、日产29%、斯巴鲁10%。巧合的是，这些车\n\n[... middle omitted ...]\n\nwas the worst of times\". The famous opening line of Charles Dickens' 'A Tale of Two Cities' captures a period of contradiction: the French aristocracy indulging in opulence and privilege, the \n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R017",
    "title": "GS：光伏盈利拐点只出现在组件，上游还在失血",
    "digest": "[wechat_article.md]\n# GS：光伏盈利拐点只出现在组件，上游还在失血\n\n这份GS6月底发布的《中国光伏：追踪盈利拐点》报告，在行业普遍关注“反内卷”政策效果和需求触底的背景下，给出了一个并不对称的判断：产业链的盈利修复远未到来，而且分化正在加剧。组件环节的毛利改善，恰恰是以上游更深的亏损为代价的。这不是一个行业整体回暖的信号，而是一个利润重新分配的起点。\n\n报告的核心数据指向一个反直觉的结论：当市场还在争论光伏产能出清何时结束时，GS已经用6月的价格和库存数据表明，上游环节的定价权正在以加速度流失，而组件环节的“韧性”更多来自成本端的被动让利，而非需求端的主动拉动。\n\n这份报告的价值不在于它预测了某个价格拐点，而在于它拆解了产业链内部利润再分配的路径，并指出了哪些公司可能在这一轮洗牌中穿越周期。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 6月全产业链价格继续下探，但组件是唯一毛利率改善的环节\n\n6月光伏产业链价格延续了5月以来的疲软态势。根据GS的追踪数据，6月全价值链平均价格环比下跌约5%。其中，胶膜（-12% MTD）和电池片（-11% MTD）跌幅居前，分别受到原油价格下跌（-8% MoM）和银价回落（-13% MoM）的成本端拖累，但更关键的是，这两个环节的产成品库存分别环比激增了21%。\n\n从盈利角度看，这种价格下跌直接反映为现金毛利率的恶化：电池片、胶膜、多晶硅、玻璃的现金毛利率分别环比下降了8、7、4、3个百分点。而组件环节却逆势改善了2个百分点。\n\n> **KC评论：** 组件毛利率的改善，并不是因为组件价格涨了——事实上6月组件价格环比持平。改善的唯一来源是上游原材料成本下降。这本质上是一种“剪刀差”效应：上游的亏损通过价格传导，变成了下游的利润。对于组件企业来说，这是一个“被动受益”的阶段，而不是主动议价能力\n\n[... middle omitted ...]\n\n者廉价金属技术的详细影响感兴趣，欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n光伏产业链利润正在“大挪移”\n\n**利润分化，谁是赢家？**\n\n6月光伏产业链价格继续承压，但利润走向出现明显分化——组件端开始受益，上游却更难受了。\n\n**1/ 上游跌价还在继续**\n6月以来，光伏全产业链价格平均下跌约5%。其中：\n- 电池片环比跌11%，薄膜跌12%，跌幅最大\n- 多晶硅和玻璃分别跌4%和2%\n- 背后原因：电池片库存环比暴增21%，叠加银价下跌；薄膜则受油价走低拖累\n\n**2/ 利润端：组件悄悄好转**\n虽然上游价格疲软，但组件端反而受益于成本下降：\n- 组件现金毛利率环比提升2个百分点（至约12%）\n- 电池、薄膜、多晶硅、玻璃的毛利率分别下滑8/7/4/3个百分点\n- 简单说：上游亏的，组件赚回来了\n\n**3/ 需求数据不太乐观**\n5月全球组件需求29GW，环比降22%，同比降79%。1-5月累计193GW，同比降46%。主要拖累来自中国（5月同比降91%）。\n\n**4/ 接下来怎么看？**\n研报认为价格疲软还会持续，因为：\n- 7-8月是传统需求淡季，库存压力可能更大\n- 上游跌价+头部企业三季度开始用低成本金属化技术，组件成本还有下行空间\n\n**5/ 哪些环节更值得关注？**\n\n[... middle omitted ...]\n\nower oil price (-8% MoM) and lower silver cost (-13% MTD) amid surging producer-side inventory during the period (+21% MoM), respectively. In terms of profitability, lower pricing has led to 8\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R018",
    "title": "GS：中国银行税案冲击有限，真正考验的是净息差",
    "digest": "[wechat_article.md]\n# GS：中国银行税案冲击有限，真正考验的是净息差\n\n中国银行被曝出税务问题，H股单日跌幅超过5%，拖累整个银行板块下跌约3%。市场恐慌情绪不难理解——如果一家大行能通过包装产品逃税，那么整个行业的有效税率会不会因此被迫上调？利润会不会被进一步压缩？同业间的流动性会不会被牵连收紧？\n\nGS在事件发生后迅速发布报告，给出了一个与市场直觉相反的判断：**有效税率不会因此大幅上升，流动性也不会因此显著收紧。** 但报告同时揭示了一个更值得关注的信号——银行对净息差的展望比此前更加悲观。\n\n这份报告的核心结论，用一句话概括就是：**短期冲击被高估，但长期盈利压力被低估。**\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 有效税率不会上升，因为驱动低税率的真正引擎是国债而非基金\n\nGS的逻辑链条清晰而直接。中国大行有效税率在过去三年持续下降至平均13%，市场普遍将这一趋势部分归因于银行持有的公募基金产品享受税收优惠。但GS通过数据拆解发现，真正压低有效税率的“主力军”是国债，而非基金。\n\n以四大行为例，过去三年国债持仓累计增加了约16万亿元，而基金投资的增加额仅为0.3万亿元。两者规模相差超过50倍。国债利息收入免税，这才是大行有效税率持续走低的根本原因。\n\n> **KC评论：** 市场往往对“事件驱动”的冲击过度反应。中国银行的税务问题本质上是操作合规问题，并非行业性的有效税率系统性重估。GS的数据告诉我们，即使监管收紧公募基金的税收优惠，对有效税率的影响也微乎其微——因为国债才是真正的主角。\n\nGS进一步预测，未来三年四大行的平均有效税率将从13%进一步降至12%。这背后是银行出于信贷投放需求和资本节约考量，将持续增持国债。因此，即便公募基金税收优惠被压缩，也无法逆转这一趋势。\n\n![研报原图 2](assets/so\n\n[... middle omitted ...]\n\n续讨论这份报告中的未解问题，以及它们对银行股定价的真实含义。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n银行税案冲击有多大？来拆解\n\n银行税案冲击拆解\n\n中行被通报补税23.67亿，H股跌超5%，市场开始担心两件事：银行有效税率会不会上升，市场流动性会不会收紧。来看某外资投行的拆解逻辑。\n\n**1/ 有效税率大概率不会明显上升**\n过去三年四大行有效税率平均13%，未来三年预测平均12%。核心原因是：银行低税资产的主要来源是国债，不是基金。过去三年四大行国债持仓增加了16万亿，基金投资只增加了0.3万亿。国债的免税效应是主因，就算基金税收优惠收紧，也不改变大趋势。\n\n**2/ 流动性收紧的可能性也不大**\n银行持有货基主要为了获取同业负债，同时享受税收优惠。短期看，货基的税收优惠政策不太可能改变——这是支持基金行业发展的重要工具。再加上近期利率走廊中枢下移，以及对非银机构的流动性支持，同业市场流动性应该够。\n\n**3/ 真正要关注的是NIM**\n银行自己的预期是：存款成本虽然还在降，但降幅会逐步收窄，对NIM的支撑会越来越弱。在贷款增速放缓的环境下，能维持NIM和资产质量的银行更值得关注。\n\n欢迎一起讨论研究框架。\n\n#学习笔记\n\n[source_mineru.md]\nCHINA BANKS\n\n# Questi\n\n[... middle omitted ...]\n\n this reported incident could create upward pressure on banks' effective tax rates, potentially weighing on net profit; 2) whether interbank liquidity could tighten as a result.\n\nShuo Yang, Ph\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R019",
    "title": "JPM：618之后，中国美妆的“双轨”格局已经固化",
    "digest": "[wechat_article.md]\n# JPM：618之后，中国美妆的“双轨”格局已经固化\n\n618大促刚刚落幕，JPM在6月23日组织了一场专家电话会，试图拆解这个中国美妆行业最重要的销售窗口背后的结构性变化。结论值得每一个关注消费赛道的人认真对待：中国美妆市场正在进入一个“双轨并行”的新阶段——国际品牌在高价位段和抖音渠道全面收复失地，而本土头部品牌则凭借品牌资产在特定价位带和平台上守住了基本盘。这不是一场简单的“国货vs进口”的零和博弈，而是两种增长逻辑在同一市场中的分层并存。\n\n这份报告最核心的判断是：过去两年“国货替代”的叙事正在被“品牌分层”取代。国际品牌在中高端和超高端段位的统治力不仅没有削弱，反而在2026年618期间进一步强化；而本土品牌中，除了少数拥有真正品牌议价能力的玩家，大部分大众定位的品牌正在承受越来越大的压力。市场不是在“反转”，而是在“分化”。\n\n> **KC评论：** JPM专家电话会的一个关键信号是，国际品牌在抖音和天猫两个平台都拿回了Top 1位置——修丽可在天猫、雅诗兰黛在抖音。这距离双十一2025年国际品牌在天猫Top 10中只有5席、抖音只有8席已经过去不到一年。完整报告中的两张Top 20排名表值得仔细对比，你会发现哪些品牌在“换位”，哪些在“掉队”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 国际品牌在抖音和天猫同时完成“反超”，背后是三大战术的协同发威\n\nJPM专家电话会披露的数据显示，2026年618期间国际品牌在天猫Top 10中占据9席、在抖音Top 10中占据6席，相比双十一2025年的8席和5席均有提升。更值得注意的是，修丽可和雅诗兰黛分别拿下了天猫和抖音的榜首——这是近年来国际品牌首次在两大平台同时登顶。\n\n这种“反超”并非偶然。专家总结了三个具体驱动因素：第一，国际品牌大幅扩展了与中\n\n[... middle omitted ...]\n\n欢迎来星球微信群里继续讨论，一起追踪这些关键假设的验证过程。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n618美妆大促，国货稳住高端反攻\n\n国货稳住，高端反攻\n\n618美妆成绩单出炉，整体GMV同比增长11%，跑赢大盘。某外资投行专家解读，几个有意思的点值得记下来。\n\n1/ 平台分化明显\n天猫高端线（>800元）增长超20%，抖音主打300-500元中端，增长约25%。消费分层在继续。\n\n2/ 折扣在加深\n尽管大牌名义折扣稳定，但平台券+直播券+政府补贴叠加后，实际到手价更低了。\n\n3/ 国货龙头守住了\n- 毛戈平整体增长约35%，熊猫IP联名款很受欢迎\n- 珀莱雅稳居天猫/抖音前4，618期间天猫一度冲到第1\n- 薇诺娜双平台增长超20%\n- 韩束在抖音压力较大（从第1掉到第6），但专家对公司多品牌布局（Newpage翻倍增长）和研发能力有信心\n- 可复美恢复正增长\n- 林清轩抖音三位数增长\n\n4/ 国际品牌全面反攻\n修丽可和雅诗兰黛分别拿下天猫/抖音第1，国际品牌在天猫Top10占9席、抖音占6席（vs去年双11的8/5席）。但专家谨慎看待大众线国际品牌（欧莱雅、玉兰油），国货竞争太激烈。\n\n毛戈平被投行列为中国美妆首选标的，看好其体验式消费定位。\n\n欢迎一起讨论，这次618你买了什么？觉得国货和国际品牌谁\n\n[... middle omitted ...]\n\nrce: NBS). Key highlights from the discussion include: (1) a divergence of pricing range trends between platforms: Tmall's $>Rmb800$ ASP segment GMV up $>20\\%$ , while Douyin's Rmb300-500 segm\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R020",
    "title": "JEF：中国半导体设备进口的窄幅下跌背后，藏着一个更大的结构性故事",
    "digest": "[wechat_article.md]\n# JEF：中国半导体设备进口的窄幅下跌背后，藏着一个更大的结构性故事\n\n5月中国半导体设备进口数据出炉，表面看并不乐观——WFE（晶圆制造设备）进口同比下降12%，连续三个月恶化。但如果只看总量，你会错过真正的信号。\n\nJEF（JEF）最新研报的核心判断是：这轮下跌是“窄基”的，几乎完全由刻蚀设备进口骤降驱动，而沉积、离子注入等关键环节仍在增长。更关键的是，报告揭示了一个更长期、更具决定性的驱动力——中国半导体贸易逆差正在以惊人的速度扩大，这将成为未来WFE资本开支持续强劲的根本支撑。\n\n这份报告的价值不在于告诉你5月数据好不好，而在于它帮你把短期波动和长期结构分开了。对于关注中国半导体自主化进程的决策者来说，理解这种“窄幅下跌”背后的逻辑，比纠结于月度数字本身重要得多。\n\n> **KC评论：** 很多读者看到设备进口下降，第一反应是“自主化受阻”或“需求疲软”。但JEF的分析恰恰相反——下跌是结构性的、局部的，而真正的增长引擎（贸易逆差驱动的长期资本开支）正在加速。这种“总量悲观、结构乐观”的错位，恰恰是专业研报最有价值的地方。完整报告里有更详细的设备分类和国别数据，能帮你验证这个判断到底站不站得住。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 5月的下跌是窄基的，真正需要关注的是哪些环节在逆势增长\n\n5月WFE进口下降12%，听起来确实比4月的6%和3月的3%降幅更大。但JEF的分析师指出，这个下跌几乎完全由刻蚀设备贡献——刻蚀进口骤降24%，而沉积设备增长12%，离子注入设备增长21%，光刻设备基本持平。\n\n这意味着什么？下跌不是系统性的需求萎缩，而是特定环节、特定供应商的调整。报告认为，刻蚀设备下降主要与从日本和马来西亚的进口骤降有关——5月从这两国的WFE进口分别下降58%和28%。这很可能反映了特\n\n[... middle omitted ...]\n\n踪中国半导体设备这条线，欢迎来我们的社群和微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n芯片进口激增，设备跌的是“假摔”\n\n🔍 5月数据解读\n\n5月WFE进口同比跌12%，表面不好看，但仔细看——几乎全由蚀刻设备跌32%拖累。沉积/离子注入反而涨12%/21%，光刻持平。这种“窄基下跌”反而是个积极信号。\n\n🧠 为什么说不是真弱？\n\n**1. 封装是亮点**\n测试封装设备进口5月增长19%，YTD涨8%，是唯一正增长类别。华为的“Tau”缩放定律基于先进封装，且中国在封装工具上没有进口限制，预计未来12-24个月是强增长领域。\n\n**2. 下跌有特殊原因**\n- 长鑫存储去年大量拉货后放缓，在等美国限制松绑信号\n- 先进逻辑去年已提前拉货，加上灰市关键设备交期很长\n两者都只是阶段性调整，不是趋势性走弱\n\n**3. 下半年有恢复动力**\n研报预计2026全年WFE资本支出低个位数到中个位数增长，下半年存储会是主要驱动力。\n\n🌏 进口来源大洗牌\n\n新加坡已超越日本成为中国最大WFE进口来源地（5M26占25%），日本23%退居第二，荷兰18%滑到第三。\n有意思的是，5月蚀刻设备大跌32%时，来自马来西亚/日本的WFE进口分别跌58%/28%——说明中国买的蚀刻设备主要来自这两国。\n\n⚠️ 真正的长期\n\n[... middle omitted ...]\n\nbut it is narrow-based. China's May SPE imports fell 9%, driven mainly by 12% decline in WFE. Packaging imports grew 8% YTD, the only category with positive growth. We highlighted before Huawe\n\n[... middle omitted ...]\n\nd\\_iapd\\_Brochure.aspx?BRCHR\\_VRSN\\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://javatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.\n\n© 2026 JEF"
  },
  {
    "id": "R021",
    "title": "摩根斯坦利：MS：工业资本开支比生产更值得关注——一个选择性扩散的时机",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：工业资本开支比生产更值得关注——一个选择性扩散的时机\n\n工业投资者正站在一个微妙的岔路口。全球宏观经济叙事在过去半年经历了从“衰退恐惧”到“地缘冲突溢价”再到“软着陆预期”的多次翻转，市场对欧洲工业股的定价已经出现了显著分化。MS在2026年6月发布的一份欧洲资本品深度报告中，给出了一个清晰且可操作的核心判断：资本开支（capex）的韧性正在取代产量增长，成为工业板块最可靠的利润支撑；但与此同时，成本压力正在从机械向电气领域转移，这意味着行业内部的胜负手正在切换。\n\n这份报告的价值不在于预测宏观走向——那从来不是投行研报最擅长的部分。它的价值在于，它用大量硬数据（订单、库存、产能利用率、成本结构）拆解了当前工业板块“哪里在真增长、哪里只是价格幻觉、哪里可能被市场误判”。对于持有或正在考虑配置欧洲工业股的投资者而言，这份报告提供的不是一个简单的“买或卖”，而是一个精细化的筛选框架。\n\n以下是我们从这份研报中提炼的五层核心洞察，以及它们对投资决策的含义。\n\n> **KC评论：** MS的核心论点是“Industrial capex > production”。翻译成白话就是：现在看工业股，不要只看工厂开了多少、产量增加了多少，而要看企业有没有能力把资本开支转化为定价权和利润。这是一个非常关键的视角切换——在通胀和地缘冲突叠加的环境下，单纯追求量的增长反而可能带来利润率压缩。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮资本开支的韧性来自“战略支出”，而非周期性复苏\n\nMS分析师指出，当前全球工业资本开支的韧性，在结构上与2022年相似，但与2023-2024年截然不同。支撑增长的主要不是传统的制造业补库存或消费者需求回暖，而是三个“战略型”驱动力：数据中心建设、能源安全相关的产能投资、以及\n\n[... middle omitted ...]\n\n、电气公司利润率传导的具体时滞、以及欧洲折扣是否真的会收窄。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n工业资本开支韧性超预期\n\n资本开支韧性\n\n---\n\n刚读了一篇某外资投行的欧洲工业研报，信息量很大。\n\n核心判断：工业资本开支比生产更坚挺，市场应该从纯主题扩散到更多细分领域。\n\n**1/ 资本开支韧性还在，但成本压力是更大风险**\n\n- 数据中心、战略资本开支和定价能力在保护名义收入\n- 更大的风险来自：EBITA利润率和成本压力，以及利率走高对估值的影响\n- 美国/亚洲出现资本开支“绿芽”，客户开始“看穿”不确定性\n- 成本通胀卷土重来，这次电气板块比机械板块更受伤\n\n**2/ 电气 vs 机械，偏好有质量增长**\n\n- 电气板块：偏好某龙头，增长与估值平衡最好\n- 上游矿业：3月以来更偏好某矿机公司而非另一家，但买中游还为时过早\n- 看好“拓宽”品种：某压缩机、某制动系统、某工程公司\n- 谨慎看待：某发动机、某照明、某电梯\n\n**3/ 短期数据：美国/亚洲保持韧性，欧洲横盘**\n\n- 美国ISM新订单仍高于50，新订单/库存比健康\n- 日本机床订单4月外国需求增长46%（1季度平均35%）\n- 某自动化公司1季度订单环比+20%，汽车和食品饮料项目解锁\n- 德国IFO指数6月同比-3.1%，虽然环比小幅\n\n[... middle omitted ...]\n\nger sector risks are 1) EBITA margins and cost pressure, and 2) multiples, particularly if interest rates start moving higher.\n\n\\- Capex ‘green-shoots’, in particular in US and in Asia. Custom\n\n[... middle omitted ...]\n\n20 Bank Street, Canary Wharf\nLondon E14 4AD\nUnited Kingdom\n+44 (0)20 7425 8000\n\nJapan\n1-9-7 Otemachi, Chiyoda-ku\nTokyo 100-8104\nJapan\n+81 (0) 3 6836 5000\n\n1 Austin Road West\nKowloon\nHong Kong\n+852 2848 5200\n\nAsia/Pacific"
  },
  {
    "id": "R022",
    "title": "NOM：字节AI视频生成已跨过“生产门槛”，但真正的战场还在别处",
    "digest": "[wechat_article.md]\n# NOM：字节AI视频生成已跨过“生产门槛”，但真正的战场还在别处\n\n字节跳动旗下火山引擎近日举办了一场AI云峰会，发布了视频生成工具Seedance 2.5和基础模型Doubao Seed 2.1。NOM随即发布了一份深度解读，核心判断是：视频生成和AI编程正在成为中国AI平台竞争最激烈的商业化赛道，但字节在这两个领域的位势并不相同。这份报告最值得关注的信号不是技术参数，而是它揭示了AI竞争正在从“谁能吸引最多C端流量”转向“谁能在B端场景中真正赚到钱”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 字节的视频生成已领先一个身位，但商业化规模仍需验证\n\nSeedance 2.5的参数升级足够亮眼：单次输出从15秒提升到30秒，分辨率升级至4K，参考素材输入量从12个跃升至50个。但NOM分析师更看重的是这些参数背后的商业逻辑——它们直接指向了短视频电商、广告和短剧这三个最可能率先实现AI视频商业化的场景。\n\nNOM特别指出，Seedance 2.0已经被定义为字节第一款“跨过生产门槛”的视频模型。这意味着它不再是一个实验性的UGC工具，而是能够产出可用于商业投放的视频内容。Seedance 2.5在此基础上进一步强化了可控编辑和多参考能力，让同一个创意基底可以根据不同产品、价格点、国家、语言、用户群体快速迭代。\n\n> **KC评论：** 这里的关键不是技术参数本身，而是“生产门槛”这个判断。一个AI视频工具如果只是生成效果好但不可控、不可编辑、不可批量复制，它就永远停留在实验室demo阶段。Seedance 2.5的多参考和可控编辑功能，恰恰是在解决从“能看”到“能用”之间的鸿沟。完整报告中有详细的参数对比表和具体商业用例拆解，值得细看。\n\n![研报原图 2](assets/source_image_02.\n\n[... middle omitted ...]\n\nmarket dynamics。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n字节跳动的AI新方向：视频生成与编码\n\nAI视频大战升级\n\n字节跳动火山引擎大会透露了哪些关键信息？\n\n最近看了下字节跳动火山引擎的FORCE大会，有几个点值得关注：\n\n**1/ 视频生成是当前最亮眼的牌**\n- Seedance 2.5即将在7月初发布，直接把单次视频生成时长从15秒提升到30秒，画质升级到4K\n- 支持最多50个多模态参考素材输入，对于商业内容制作来说，保持角色、产品、场景的一致性变得容易很多\n- 可控编辑功能——可以只改背景、换商品、调模特，而不用重新生成整个视频\n\n**2/ 商业应用场景很清晰**\n- 短剧、广告、短视频电商是主要落地方向\n- 对TikTok Shop的跨境卖家尤其有用：能用不同语言和本地化风格生成产品展示视频，降低创意制作成本\n\n**3/ AI编码赛道竞争激烈，但格局未定**\n- 字节的豆包Seed 2.1 Pro展示了更强的代理能力，但据行业人士反馈，目前还落后于GLM-5.2、Deepseek和阿里这一梯队\n- 不过编码市场还没有出现绝对的领导者，产品迭代周期已经从5-6个月压缩到1-2个月\n\n**4/ 行业资源正在集中**\n- 芯片供应紧张，AI平台被迫把资源集\n\n[... middle omitted ...]\n\non for agentic tasks. VE management indicated that the Doubao Seed 2.1 series should provide ByteDance with an entry ticket into the AI coding arena.\n\nRecent industry events hosted by major AI\n\n[... middle omitted ...]\n\n front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R023",
    "title": "JPM：散户杠杆正在撤退，科技股的下一个对手不是关税",
    "digest": "[wechat_article.md]\n# JPM：散户杠杆正在撤退，科技股的下一个对手不是关税\n\n一份来自JPM全球市场策略团队的流动性报告，在6月下旬发出了一个值得关注的信号：散户投资者在期权和保证金账户中的杠杆水平，在年初触及极端高位后，正在出现撤退迹象。这不是一个关于关税或地缘政治的叙事，而是一个纯粹的市场微观结构层面的警告——科技股过去几个月的上涨，很大程度上被散户杠杆放大，而当这股力量开始消退时，市场的驱动力将发生根本性转变。\n\n这份由Nikolaos Panigirtzoglou领衔的研报，核心判断并非“市场即将崩盘”，而是“支撑科技股超额收益的一根支柱正在动摇”。报告系统性地拆解了不同投资者群体的杠杆水平，从散户到对冲基金、风险平价基金，再到银行和企业部门，最终指向一个分层清晰的结论：金融杠杆正在局部撤退，而宏观杠杆依然健康。这意味着，如果市场出现调整，更可能是流动性驱动而非信用驱动。\n\n以下是我们从这份报告中提炼出的五个关键洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 散户的期权杠杆已从极端高位回落，历史表明这往往是科技股调整的前奏\n\n报告中最引人注目的数据来自期权市场。JPM使用OCC（期权清算公司）的数据，追踪单笔交易少于10份合约的散户投资者在交易所交易的看涨期权买卖情况。这个代理指标在6月5日触及约1400万份合约的峰值，与2025年10月和2021年11月的前期高点相当。而在这两次峰值之后，科技股都经历了为期数月的调整，直到该指标回落至200-400万份合约的区间才触底。\n\n当前，该指标已从峰值回落，尽管尚未触及“底部”区域，但趋势方向已经明确。这意味着散户在期权市场的冲动正在消退，而科技股恰好是散户最偏爱的栖息地。\n\n> **KC评论：** 散户期权杠杆是科技股“自我强化”行情的燃料。当散户大量买入看涨期权，做市商\n\n[... middle omitted ...]\n\nmics。欢迎来星球微信群里继续讨论这些未解问题的后续演变。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n散户的杠杆，开始退了📉\n\n封面短标题：杠杆开始撤退\n\n封面副标题：科技股的资金面信号在变\n\n最近某外资投行的资金流研报里，核心观察是：散户的杠杆，正在从极端位置退潮。\n\n1️⃣ 散户期权杠杆：峰值已过\n- 小额期权买入量在6月5日创下14 million合约的峰值，跟2021年11月和2025年10月的历史高点持平\n- 前两次这种峰值后，科技股都经历了几个月的回调\n- 目前这个指标已经明显回落，意味着散户在期权上的冲动在降温\n\n2️⃣ 保证金账户也在去杠杆\n- NYSE净借记余额（衡量散户通过保证金借钱的程度）处于历史极端水平\n- 今年峰值已经追平2021年底和2018年中\n- 这两个时间点之后，市场都出现了多月的调整\n\n3️⃣ 其他玩家的杠杆信号\n- 风险平价基金：5月中旬创10年新高后，最近几周明显回落\n- 对冲基金：杠杆还在高位，但可能有见顶迹象（研报说的是“更初步”的信号）\n- 银行杠杆：虽然过去一年在监管放松下有所上升，但远低于2008年前水平\n\n4️⃣ 经济杠杆不是问题\n- 企业和家庭杠杆率自疫情以来一直在下降\n- 净利息支出占现金流比例也在降低\n- 所以宏观层面，杠杆不太可能成为冲击来源\n\n5️\n\n[... middle omitted ...]\n\ny to macro shocks.\n\n\\- A modest deterioration in the global bond supply-demand balance for 2026 is already priced in by bond markets.\n\n## Cross Asset Fund Flow Monitor\n\nCurrent level shows the\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 24 Jun 2026 11:12 PM BST\n\nDisseminated 24 Jun 2026 11:12 PM BST"
  },
  {
    "id": "R024",
    "title": "美国银行：资金正从科技巨头流向小盘股，但真正的信号是“规模”不再为王",
    "digest": "[wechat_article.md]\n# 美国银行：资金正从科技巨头流向小盘股，但真正的信号是“规模”不再为王\n\n这份来自美国银行（BofA）最新一期“The Flow Show”的报告，在2026年6月25日的数据中，揭示了一个正在发生的、但多数投资者尚未充分定价的结构性转变。报告的核心判断是：市场正在经历一场从“规模崇拜”到“流动性扩散”的再平衡。科技巨头（Magnificent Seven）的ETF资金流出创下93亿美元的纪录，而房地产、基础设施等此前被忽视的板块却迎来了久违的资金流入。这不是一次简单的板块轮动，而是市场在美联储新主席Warsh治下，对“增长叙事”和“资产定价锚”进行的根本性重估。\n\n为什么这很重要？因为过去两年，全球资本市场的核心逻辑就是“越大越好”——市值越大、AI叙事越强、资金越集中。但这份报告显示，当Warsh就任美联储主席后，美国国债收益率开始下行，而股市却出现下跌，这与历史上多位“鸽派”或“低利率”联储主席任期初期的表现惊人相似。市场似乎在说：过去靠规模溢价支撑的估值，现在需要新的逻辑来验证。\n\n**报告没有直接说出的结论是：当下最拥挤的交易，恰恰是风险最大的交易。**\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 科技巨头的资金流出不是偶然，而是“规模溢价”退潮的起点\n\n报告中最刺眼的数据是：美国股票基金录得85亿美元净流出，这是自2026年3月以来的首次。而科技板块更是创下了93亿美元的纪录级流出，紧随此前创纪录的192亿美元流入。\n\n这组数据的含义远不止“获利了结”。它意味着，过去两年驱动美股上涨的核心引擎——对AI和超大规模云计算的无限资本开支信仰——正在被市场重新定价。报告中的“时代精神”（Zeitgeist）问题一针见血：“超大规模企业需要跌多少，市场才会开始交易资本开支削减？”\n\n当投资者开始\n\n[... middle omitted ...]\n\n，继续围绕这些“报告没有完全展开”的关键问题做更深入的讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nMAGS跌破60美元，资金开始往小盘跑\n\n**小盘才是大机会**\n\n**资金从科技巨头流向冷门板块**\n\n最近市场有个明显变化：资金开始从科技七巨头（MAGS）流出，转向半导体、小盘股、地产和REITs。如果MAGS跌破60美元，AUDJPY跌破110，很可能触发一轮夏季避险行情。\n\n1️⃣ **资金流向大变局**\n- 科技股单周流出93亿美元，创纪录（之前刚创下192亿流入纪录）\n- 地产基金流入9亿美元，为2024年3月以来最大\n- 基建基金流入15亿美元，6周最高\n- 能源基金流出15亿美元，2025年4月以来最大\n\n2️⃣ **美联储新主席的“低利率信号”**\nWarsh上任以来，10年期美债收益率已下降17个基点，美股微跌2%。历史数据显示，他的任期初期走势与Eccles、Volcker、Greenspan、Bernanke相似——这些主席任内收益率都走低。目前长端美债仍是市场上最反共识的长期交易。\n\n3️⃣ **黄金值得关注**\n金价低于4000美元被视为不错入场点。虽然地缘政治缓和短期压制金价，但2020年代仍是分裂的地缘政治+民粹主义时代，各国优先保增长而非控通胀——这对黄金长期有利。\n\n4️\n\n[... middle omitted ...]\n\nart 6) = love for stocks, and liquidity pulled from mega-cap AI arms racers simply racing into semis & illiquid cyclicals (small/mid-cap, housing, REITs) to front-run Trump pivot to affordabil\n\n[... middle omitted ...]\n\nw in accordance with firm policies.\n\nNeither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information."
  },
  {
    "id": "R025",
    "title": "GS：AI“失业末日”不会来，但真正的考验藏在2027年",
    "digest": "[wechat_article.md]\n# GS：AI“失业末日”不会来，但真正的考验藏在2027年\n\n关于AI会消灭多少工作岗位，市场已经听过太多耸人听闻的预言。但这份GS最新发布的《Top of Mind》报告，罕见地同时邀请了三位立场不同的顶尖学者与经济分析师——MIT的Daron Acemoglu、Neil Thompson，以及GS首席经济学家Joseph Briggs——来正面辩论同一个问题。他们的结论出奇一致：AI不会引发“失业末日”。但分歧在于，冲击的规模、节奏和谁先受伤，远比公众想象的复杂。\n\n这份报告最值得关注的判断不是“AI不会取代人类”，而是：**未来五年，AI对劳动力市场的净负面影响可能只有2-4%，但2027年将是第一个真正的压力测试节点。而投资者目前完全无法为这种不确定性定价。**\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 三位顶级专家的共识与分歧：冲击会来，但不是海啸\n\nGS这份报告的价值，在于它没有让单一声音主导叙事。三位专家在核心结论上罕见地达成一致：大规模、突发的AI失业不会在短期内发生。但他们的分歧点，恰恰是投资者和产业决策者最应该关注的。\n\nJoseph Briggs的立场相对乐观。他假设AI会在十年过渡期内取代超过9%的劳动力——约1500万工人——但他坚信这些损失是暂时的。他的逻辑基于历史：每一次技术浪潮最终都创造了更多新岗位。美国经济的动态性，加上十年的过渡期，足以让市场自我调整。\n\nNeil Thompson则从技术落地的实际障碍出发。他提醒，能力只是第一步。AI必须可靠、能访问正确数据、并且成本有效，才能真正冲击就业。大多数工作由多个任务组成，只有部分能被自动化。因此，他预期调整将是“缓慢且不均衡的”，更像“涨潮”而非“海啸”。\n\nDaron Acemoglu的立场最为审慎。他预计未来五年AI对就\n\n[... middle omitted ...]\n\nmarket dynamics。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI抢饭碗？经济学家们这么说\n\nAI取代人类工作？\n\n三位顶级学者观点大不同\n\n最近AI能力进步飞快，企业也在加速落地。很多人担心：AI会不会在十年内让大规模失业成为现实？\n\n我翻了份外资投行的研报，采访了三位顶级经济学家，他们的观点很有意思👇\n\n**1️⃣ 短期影响：没那么夸张**\n\nMIT诺奖得主Acemoglu认为，未来5年AI对就业的净负面影响只有2-4%，远低于很多技术乐观派的预测。\n\n原因很简单：现在AI模型更擅长替代人，而不是辅助人。真正好用、能让大企业直接用的AI应用还太少。\n\n目前的AI更像是“需要你不断调教的高级工具”，而不是即插即用的生产力神器。\n\n**2️⃣ 谁最容易被替代？**\n\n主要是从事认知性、重复性工作的白领，比如客服、后台运营。\n\n这类工作在美国大概有800-900万人，占总劳动力的5%左右。\n\n但Acemoglu警告：如果AI投资持续偏向“替代人”而不是“辅助人”，长期影响会更大。\n\n**3️⃣ 历史告诉我们什么？**\n\n前几轮技术革命（比如自动化）最后都创造了更多新工作。\n\n但MIT的Thompson指出：AI处理信息的方式比以往任何技术都更像人类，所以这次可能真的不一样\n\n[... middle omitted ...]\n\ny temporarily as new jobs eventually emerge. Thompson is less convinced about large-scale job displacement and takes comfort in the ability to anticipate changes, seeing AI as a rising tide ra\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R026",
    "title": "GS：澳洲保险业正进入“费率见顶、并购重启”的关键拐点",
    "digest": "[wechat_article.md]\n# GS：澳洲保险业正进入“费率见顶、并购重启”的关键拐点\n\n阅读一份GS最新发布的澳洲保险行业深度报告，最值得关注的不是某个公司的季度利润，而是一个正在形成的结构性判断：随着保费费率上涨放缓，澳洲非寿险行业正从“赚超额利润”转向“用资本结构和并购重新分配利润”的阶段。\n\n这不是一个利空信号。恰恰相反，GS认为，这个转变对头部玩家IAG和Suncorp意味着新的ROE优化路径，而对全球资本——尤其是日本三大保险集团——则打开了一个估值合理的并购窗口。\n\n报告的核心逻辑可以浓缩为一句话：费率周期的“硬市场”红利正在消退，但行业正在进入一个由再保险结构优化和跨境并购驱动的新阶段。这个阶段比上一个更考验管理层的资本配置能力，但也更有可能产生超额回报。\n\n以下是GS这份研报中最值得深读的六个判断。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 再保险费率在六月续转期可能下降10%-15%，这远不是底部\n\nGS指出，4月1日的续转窗口已经显示，美国和亚洲的风险调整后费率大幅回落至2020年代初的水平。而澳洲7月1日的续转期，预计整体下降幅度在10%-15%之间，更接近15%这一端。\n\n为什么这不是底部？因为再保险公司的ROE仍然远超长期均值。报告数据显示，全球再保险资本已增至7850亿美元，第三方资本（巨灾债券/保险连接证券）更是增长了18%，而再保险公司的ROE仍在17%左右。只要再保险公司还在“超赚”，费率下行的空间就还没有耗尽。\n\n> **KC评论：** 再保险费率下行对直保公司是利好——它们可以用更低成本转移风险，从而优化资本回报。但这里的关键问题是：下行速度有多快？如果费率下降快于预期，那些过度依赖再保险转移风险的公司的利润波动会加剧。完整报告中有再保险ROE和资本充足率的历史图表，值得仔细看。\n\n![研报原图 \n\n[... middle omitted ...]\n\n优化路径有更深入的讨论需求，欢迎来我们的星球微信群继续交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n保险费率放缓，M&A机会来了\n\n澳洲保险业迎来结构性变局\n\n某外资投行最新研报指出，全球再保险费率进入下行通道，预计今年7月澳洲市场将下降10-15%。这背后藏着几个值得关注的逻辑：\n\n1️⃣ 再保险市场正在变“便宜”\n- 全球再保险资本增长约10%，达7850亿美元\n- 第三方资本（CAT债券）增长18%\n- 再保险公司ROE仍处高位，有空间继续降价\n- 说白了：保险公司现在可以用更低成本转移风险\n\n2️⃣ 费率放缓=并购窗口打开\n- 历史规律显示：费率软化期往往伴随M&A活跃\n- 日本三大非寿险公司（东京海上、Sompo、MS&AD）手握大量资金\n- 东京海上与伯克希尔成立战略合作，并购弹药可达200亿美元\n- Sompo刚花35亿美元收购Aspen，还有近90亿澳元余粮\n\n3️⃣ 澳洲本土玩家在做什么\n- IAG正在收购RACI，同时考虑再保险结构优化商业业务资本\n- SUN在出售银行后成为纯险企，也在评估商业领域机会\n- 两家公司的个人险业务利润率已超目标，考虑用再保险“平滑”利润\n\n4️⃣ 东京海上的澳洲野心\n- 2035战略明确要加大澳洲布局\n- 偏好非上市标的（估值更友好）\n- 重点关注费率软化\n\n[... middle omitted ...]\n\nrt capacity for large scale reinsurance transactions. We think this presents opportunities for IAG's Intermediated business and also for SUN to consider optimising returns across their busines\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R027",
    "title": "JPM：散户正在用行动重写“逢低买入”的定义",
    "digest": "[wechat_article.md]\n# JPM：散户正在用行动重写“逢低买入”的定义\n\n本周全球科技股遭遇剧烈抛售，韩国与半导体板块领跌。但JPM最新一期《Retail Radar》报告揭示了一个反直觉的现象：散户不仅没有撤退，反而在主动承接抛压。这份覆盖6月18日至24日交易数据的周报，核心判断值得每一个关注市场结构的投资者认真对待——**散户参与度依然坚挺，但结构正在发生深刻的内部迁移，ETF与个股之间的资金流向分化，正在暴露新的定价机制。**\n\n这不是一份简单的资金流量统计。JPM团队在报告中系统性地追踪了散户在单只股票、ETF、期权及主题篮子中的活动。其核心发现是：尽管整体零售资金流从上周高位回落，但个股交易活跃度仍处于65%分位数，而ETF活动已降至25%分位数。这意味着，散户正在从被动配置转向主动选股，而且他们选择的标的和时机，正在与机构形成越来越明显的对赌。\n\n为什么现在重要？因为当散户开始集中力量承接半导体和AI硬件股、同时对黄金ETF和通信服务板块果断离场时，这不再是“噪音交易”，而是具备价格发现功能的资金行为。JPM的数据显示，本周零售总资金流为63亿美元，略低于12周均值67亿美元，但结构上的分化远比总量有意义。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 半导体暴跌中的逆势买入：散户正在成为“记忆体”的边际定价者\n\n报告中最引人注目的数据来自存储芯片板块。在半导体股票本周普遍下跌6%至14%的背景下，散户对美光（MU）和闪迪（SNDK）的买入强度达到了极端水平。MU在6月18日单日零售资金流入高达8.3个标准差，这在其财报发布前就已经出现。而SNDK整周净买入3.54亿美元，达到2.4个标准差。\n\nJPM团队专门绘制了MU的零售资金流图（Figure 2），清晰地显示散户在股价下跌过程中持续加仓。这种行为模式并非\n\n[... middle omitted ...]\n\nmarket dynamics。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球科技股大跌，散户却在悄悄加仓\n\n📉 跌出来的机会\n\n上周全球科技股经历了一轮剧烈调整，但散户资金并未退缩。某外资投行最新数据显示，虽然整体交易量从高位回落，但仍处于近一年中位数水平，个股流入更是达到65%分位。\n\n1️⃣ 存储芯片成最大赢家\n在半导体板块领跌的背景下，散户逆势加仓存储芯片股。MU（美光）成为当周最受追捧的个股，净流入8.68亿美元，周三单日就达8.3亿美元。随后MU强劲的财报推动盘后股价大涨超14%。SNDK也持续获得2.4亿美元净买入。\n\n2️⃣ Mag7全线买入\n科技巨头依然是散户的“压舱石”。当周Mag7全部获得净买入：NVDA（4.7亿）、TSLA（4.25亿）、MSFT（2.56亿）、GOOGL（1.07亿）、META（1.02亿）、AMZN（0.32亿），AAPL持平。\n\n3️⃣ 期权交易活跃度创新高\n通信板块期权交易量飙升，带动零售期权交易占比达到历史高点。最活跃的期权标的依次是：TSLA、MU、NVDA、AMZN、META。\n\n4️⃣ 黄金ETF遭冷落\nGLD跌破4000美元关口反而触发更大规模流出（单日-1.9亿美元），散户对贵金属ETF兴趣持续低迷。\n\n5️⃣ 社交媒体\n\n[... middle omitted ...]\n\ng. EWY and KORU) saw mixed flows (-4.2z and +2.7z, resp.). Communication ETFs Imbalance reached a 15-month low, Figure 9, driven by XLC (-4.2z, Figure 10). GLD has been effectively ignored by \n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 24 Jun 2026 10:20 PM EDT\n\nDisseminated 24 Jun 2026 10:20 PM EDT"
  },
  {
    "id": "R028",
    "title": "摩根斯坦利：MS：Warsh治下的美联储，波动率回归格林斯潘时代",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：Warsh治下的美联储，波动率回归格林斯潘时代\n\n这份报告的结论比标题更锋利：如果Warsh持续减少前瞻指引，市场对经济数据的敏感度可能回升至格林斯潘时期的水平。这意味着，当前利率市场的低波动环境，可能是一种正在被侵蚀的稳态。\n\n2026年6月，Warsh主持的首次FOMC新闻发布会已经释放了一个明确信号：美联储正在系统性缩减前瞻指引。对于习惯了“听美联储说话”的市场而言，这意味着交易框架的根本性转变——从“政策路径驱动”转向“数据驱动”。MS这份报告的核心贡献，不是告诉你波动率会上升，而是用历史数据量化了“会上升多少”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 市场对数据的敏感度，已经历了从格林斯潘到鲍威尔的系统性衰减\n\n报告选取了一个极为干净的量化维度：经济数据意外与2年期国债收益率变动的关系，且两者均经过标准化处理。这种方法排除了绝对数值的噪音，直接衡量“单位意外”引发的市场反应。\n\n通过对1997年以来各任美联储主席任期的分段回归，MS发现了一个清晰的趋势：市场对非农数据的敏感度，从格林斯潘时代到鲍威尔（疫情前）时期，下降了大约50%。换句话说，同样一个非农意外，在格林斯潘时代引发的2年期收益率波动，是疫情前鲍威尔时代的两倍。\n\n这个趋势的背后，正是美联储前瞻指引的逐步强化。当市场从美联储那里获得了足够多的政策路径信息，经济数据本身的信息含量自然下降。这不是市场变钝了，而是美联储变得更“透明”了。\n\n> **KC评论：** 对于利率交易者，这个历史框架意味着一个关键判断：如果Warsh逆转这一趋势，市场敏感度的回升幅度是“可量化”的。报告给出的数字是，完全回归格林斯潘水平意味着每单位数据意外额外带来0.5倍日波动率的增幅。这不是模糊的方向判断，而是可以用于仓位校准的参考锚点。\n\n[... middle omitted ...]\n\n。欢迎来知识星球和微信群里，和我们一起持续跟踪这些关键信号。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美联储新主席少说话，市场波动会更大？\n\n**少说，就多波动**\n\n新主席上台，美联储开始减少前瞻指引。\n\n市场少了方向，只能盯着数据做反应。\n\n某外资投行用格林斯潘时代做参照，发现数据敏感度每提升1单位，日波动可能增加0.5倍。\n\n**1/ 数据比指引更值钱**\n\n美联储减少沟通，市场必须从经济数据里找答案。\n\n结果是：数据越意外，利率波动越大。\n\n回顾历史，从格林斯潘到鲍威尔（疫情前），市场对非农的敏感度下降了约50%。\n\n**2/ 通胀数据成新焦点**\n\n非农数据的影响在疫情后反弹回格林斯潘水平。\n\n但通胀数据更猛——疫情前CPI对利率影响不大，现在敏感度直接翻了3倍。\n\n新主席近期表态也强调通胀是首要关注。\n\n**3/ 短期波动会先动**\n\n研报认为，短期波动会先上升，中期波动会跟随。\n\n如果数据敏感度完全回到格林斯潘水平，每次数据发布日的波动可能翻倍。\n\n欢迎一起讨论，你们觉得数据敏感度能回到格林斯潘时代吗？\n\n#学习笔记\n\n[source_mineru.md]\nJune 24, 2026 11:55 AM GMT\n\nUS Rates Strategy | North America\n\n# How Mu\n\n[... middle omitted ...]\n\nr a less guided Fed and offers clues on how much market sensitivity to economic data could increase.\n\nWe measure market sensitivity using the relationship between economic surprises and Treasu\n\n[... middle omitted ...]\n\nuthors are Fixed Income Research Analysts/Strategists and are not opining on or expressing recommendations on equity securities: Aryaman Singh; Shaun Zhou; Eli P Carter; Matthew Hornbach; Martin W Tobias, CFA.\n\n© 2026 MS"
  },
  {
    "id": "R029",
    "title": "布鲁金斯学会：土耳其军工的“十字路口”是欧洲的机遇，也是北约的难题",
    "digest": "[wechat_article.md]\n# 布鲁金斯学会：土耳其军工的“十字路口”是欧洲的机遇，也是北约的难题\n\n一份来自布鲁金斯学会与IISS的联合报告，把土耳其的国防工业推到了一个不容回避的审视台上。报告的核心判断并非土耳其能否造出第五代战斗机，而是这个从“客户”蜕变为“竞争者”的过程，正在重塑欧洲安全供应链的底层逻辑。对于关注地缘政治与产业博弈的读者而言，这份报告的价值不在于罗列土耳其的装备清单，而在于揭示一个中等强国如何用七十年的时间，把被禁运的屈辱转化为出口的筹码，并最终让自己成为国际军工体系里一个“无法忽视、但也不好合作”的角色。\n\n报告开篇就点明了土耳其当前面临的根本矛盾：自主性与可持续性之间的张力。一方面，从1923年建国至今，对单一供应商的恐惧——尤其是1974年塞浦路斯行动后西方盟友的武器禁运——一直是驱动土耳其国产化的核心动力。另一方面，当国产化走到平台级装备（如KAAN战斗机、阿纳多卢号两栖攻击舰）阶段时，成本与技术复杂度呈指数级上升，“完全自主”在经济学上已不现实。报告由此引出一个关键追问：当出口成为维系产业的唯一出路，土耳其的武器买家将如何影响其外交选择？这个问题，欧洲和北约至今没有给出清晰答案。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 禁运是最好的催化剂：土耳其军工的“创伤记忆”决定了其行为逻辑\n\n报告用大量篇幅回溯了土耳其军工的“创伤记忆”，这不是历史回顾，而是理解当前决策的钥匙。1923年至1947年间，土耳其作为“客户”在国际军火体系中摸索，但两次关键事件彻底改变了轨迹。第一次是1964年约翰逊总统的信件——美国明确警告土耳其不得使用美制装备干预塞浦路斯。第二次是1974年塞浦路斯行动后，美国、欧洲多国对土耳其实施了全面或局部武器禁运。\n\n> **KC评论：** 禁运的冲击力不在于“买不到武器”，而在于它摧毁了土耳其对\n\n[... middle omitted ...]\n\n。顺着这些未解问题，继续读完整报告，你会看到更多有趣的细节。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n土耳其军工：从买家到对手的逆袭路\n\n🇹🇷 从客户到竞争者\n\n土耳其军工百年发展，从依赖进口到自主研发，再到成为国际军贸市场的新玩家。\n\n**1. 起步期：1923-1947**\n- 建国初期靠德国、苏联技术\n- 在Kayseri建飞机装配厂\n- 主要生产轻武器和弹药\n\n**2. 冷战依赖期：1947-1964**\n- 美国军援大量涌入\n- 本土军工几乎停滞\n- 3,085辆M48坦克、260架F-100战机免费拿\n\n**3. 转折点：1974塞浦路斯危机**\n- 西方武器禁运\n- 被迫启动国产化\n- 1985年成立国防工业署\n\n**4. 爆发期：2004至今**\n- Bayraktar TB2无人机全球瞩目\n- KAAN五代机首飞\n- 年出口额突破55亿美元\n\n核心逻辑：禁运是最好的催化剂。西方封锁反而倒逼出土耳其的军工自主之路。\n\n现在土耳其面临新选择：继续追求完全自主，还是与盟友合作分摊成本？\n\n你对土耳其军工崛起怎么看？欢迎一起讨论。\n\n#学习笔记\n\n[source_mineru.md]\n# From Client to Competitor: The Rise of Turkiye's Defence\n\n[... middle omitted ...]\n\ns (CATS).\n\n## Disclaimers\n\nThe views outlined in this paper are exclusively those of the authors and do not represent institutional views of the CFPPR or the IISS.\n\n## Contents\n\nExecutive Summ\n\n[... middle omitted ...]\n\nvenes conferences including the IISS Shangri-La Dialogue and IISS Manama Dialogue, world-leading forums for the discussion of security issues. IISS research helps governments, academics, the media and the private sector."
  },
  {
    "id": "R030",
    "title": "布鲁金斯学会：墨西哥野生动物走私，正被贩毒集团“收编”为中墨地下贸易通道",
    "digest": "[wechat_article.md]\n# 布鲁金斯学会：墨西哥野生动物走私，正被贩毒集团“收编”为中墨地下贸易通道\n\n当你以为野生动物走私只是环保议题时，它已经变成了毒品贸易的“结算系统”。\n\n这份来自布鲁金斯学会的深度报告揭示了一个被严重低估的现实：在墨西哥，针对中国市场的野生动物盗猎与走私，早已不是孤立的生态犯罪。它正被锡那罗亚等贩毒集团系统性地“收编”，成为毒品前体化学品交易的价值转移工具，以及洗钱的新通道。\n\n报告的核心判断是：墨西哥的野生动物走私，正在从“盗猎者-中国买家”的简单链条，演变为“贩毒集团控制渔场与林场-强制介入中间环节-以珍稀物种作为毒品交易的‘硬通货’”的复杂地下经济网络。这一变化，远比单纯的物种灭绝威胁更为深远——它意味着中国买家与墨西哥最暴力的犯罪组织之间，正在形成一种结构性的共生关系。\n\n这不仅仅是一份环保报告，它是一份关于跨国犯罪、毒品经济与全球供应链阴影地带的深度商业与安全分析。以下是我们从这份报告中提炼出的五个核心洞察。\n\n> **KC评论：** 这份报告最反常识的地方在于，它没有把问题归结为“中国消费者爱吃鱼翅/穿山甲”，而是指出中国贸易商在墨西哥的采购行为，正在被当地贩毒集团“绑架”。如果你只关注环保，你会错过背后那个更庞大的非法经济网络。完整报告里对锡那罗亚卡特尔如何从渔民手中“收税”的细节描写，会让你对“供应链控制”这个词有全新的认识。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 贩毒集团正在对墨西哥渔业实施“全链条垄断”，中国买家被迫与其直接交易\n\n报告指出，墨西哥的有组织犯罪集团，特别是锡那罗亚卡特尔，正在试图垄断从捕捞到出口的全链条。他们不仅向合法和非法渔民征收“保护费”，更强制规定渔民只能将渔获卖给他们，甚至要求面向国际游客的餐厅只能从他们手中进货。\n\n这意味着，曾经直接与当地渔民或猎手交易的中国贸易商\n\n[... middle omitted ...]\n\n二次分析，也方便你在繁忙的工作中快速把握全球市场的关键动态。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n墨西哥的野生动物，正在被悄悄运往中国\n\n中国需求下的墨西哥生态危机\n\n如果你以为墨西哥的野生动物走私只跟美国有关，那可能要重新想想了。\n\n一份来自某外资投行的研报揭露了一个被严重低估的问题：越来越多墨西哥的珍稀物种，正在被非法运往中国。而且，这个链条的复杂性远超想象。\n\n1/ 走私物种比你想象的多\n- 陆生：爬行动物、美洲豹、各种名贵木材\n- 海洋：海参、石首鱼、鲍鱼、鲨鱼\n- 很多物种先经美国中转，最终流向中国市场\n- 合法贸易（如海参、鳄鱼皮）反而成了洗白非法捕获的掩护\n\n2/ 墨西哥黑帮已经全面介入\n- 锡那罗亚等犯罪集团正在控制整个渔业产业链\n- 他们强制渔民只能卖给他们，再转手给中国买家\n- 甚至规定餐馆只能从他们那里进货\n- 十五年前中国商人直接跟渔民交易，现在必须通过黑帮\n\n3/ 更惊人的是：野生动物成了毒品交易的\"货币\"\n- 墨西哥黑帮用野生动物产品，向中国商人交换制毒前体（如芬太尼原料）\n- 这种\"物物交换\"比现金更难追踪\n- 研报指出：墨西哥的野生动物走私与毒品、洗钱之间的交织，比世界上任何地方都严重\n\n4/ 中国政府的反应：推诿+有限行动\n- 官方立场：这是墨西哥自己的问题\n- 2018\n\n[... middle omitted ...]\n\n regarding Mexico-linked wildlife trafficking\nAnti-money laundering efforts\nTrilateral anti-wildlife crime efforts\nLegal assistance\nV. \"FIX IT YOURSELF, MEXICO\": ENVIRONMENTAL REGULATION ENFOR\n\n[... middle omitted ...]\n\nnagement, or its other scholars.\n\n![](images/2f505c8335626f1501632dacd0ffb9a01bf0df25a5bc651a64395aeac948a49b.jpg)\n\n## BROOKINGS\n\nThe Brookings Institution\n1775 Massachusetts Ave., NW\nWashington, D.C. 20036\nbrookings.edu"
  },
  {
    "id": "R031",
    "title": "布鲁金斯学会：霍尔木兹海峡不会回到从前，伊朗已学会“政治定价”",
    "digest": "[wechat_article.md]\n# 布鲁金斯学会：霍尔木兹海峡不会回到从前，伊朗已学会“政治定价”\n\n美伊签署谅解备忘录结束战争，霍尔木兹海峡正在重新开放。第一批油轮已试探性通过，全球能源市场松了一口气。然而，布鲁金斯学会三位资深学者在最新一期播客中发出一个被市场忽略的警告：即便海峡今天开放，伊朗已经改变了全球航运的底层规则。这场战争留下的真正遗产，不是伊朗核计划的去留，而是一个主权国家第一次将“政治定价”系统性地嵌入国际水道通行权。\n\n这意味着什么？意味着全球贸易的“高速公路”可能从此不再是公共品，而变成了地缘杠杆。伊朗建立了波斯湾海峡管理局，开设了国有保险公司保险政策，甚至尝试对盟友打折、对敌人加价。这些做法没有因为停火而撤销。备忘录中，伊朗只是承诺60天内免费通行，但明确保留了与阿曼协商未来海峡管理权的条款。换句话说，伊朗没有承诺“永不封锁”，它只是换了一种更精细的控制方式。\n\n> **KC评论：** 市场往往把“重新开放”等同于“恢复正常”。但布鲁金斯学会的分析提醒我们，伊朗正在把霍尔木兹海峡从一个物理瓶颈升级为一个制度化的政治工具。这对全球航运成本结构、保险定价、甚至供应链地缘布局都有深远影响。完整报告里有一张关于“政治定价”的机制图解，值得细看。\n\n---\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 伊朗的“政治定价”实验，可能成为全球航运的新常态\n\n伊朗在整个战争期间做的，不仅仅是封锁海峡。它做了一件更危险的事：根据对象国与自己的政治关系，差异化定价。盟友享受折扣，敌人支付溢价。这不是传统意义上的“战时管制”，而是把国际水道变成了一个可调节的地缘阀门。\n\n布鲁金斯学会经济研究高级研究员Kari Heerman指出，这种做法不仅背离了数十年来的国际惯例，也直接挑战了国际海洋法的基本原则。传统上，国际海峡的通行权是“非歧视性”的，所有国家享\n\n[... middle omitted ...]\n\n险，欢迎加入社群，与我们一起持续拆解这些正在重塑世界的力量。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n霍尔木兹：停火后的新棋局\n\n🌍 一场改变全球航运规则的博弈\n\n刚读完布鲁金斯学会最新播客解析，关于美伊协议后的霍尔木兹海峡局势，信息量爆炸👇\n\n1️⃣ **伊朗的“新武器”**\n伊朗发现，核弹不如海峡管用。战时他们不仅封锁海峡，还搞了“政治化通行”——朋友打折，敌人加价。这打破了百年自由航行惯例，给全球海上贸易开了个危险先例。\n\n2️⃣ **60天窗口期**\n协议规定：伊朗开放海峡+美国放松制裁。但伊朗没承诺永不再封，还保留了一个“波斯湾海峡管理局”，未来可能收通行费。更棘手的是：海峡里还有水雷！伊朗自己排雷要数月，欧洲帮忙也得几个月。\n\n3️⃣ **不止石油**\n70%全球能源、90%贸易、99%数据走海底电缆。伊朗战时威胁对数据流征税，这比石油封锁更难应对——对自己经济伤害小，但对全球通信破坏大。\n\n4️⃣ **美国海军力不从心**\n冷战后美海军从600艘缩到280艘，而中国已成最大海上力量。全球航运风险上升，美国保卫航线的能力却在下降。\n\n5️⃣ **重建基金？没那么简单**\n制裁解除是法律工程，重建基金细节模糊。JD Vance说不会用美国纳税人钱，但区域国家可能参与。问题是：谁能保证这不会再次崩盘？\n\n[... middle omitted ...]\n\ntes and Iran signed a memorandum of understanding to end the war, Aslı Aydıntaşbaş spoke to Kari Heerman and Bruce Jones about its geopolitical implications, building on their recent articles \n\n[... middle omitted ...]\n\n to also thank our listeners for listening and watching.\n\n[music]\n\nYou can learn about all of this, as well as read Bruce and Kari's pieces on our website at Brookings dot edu.\n\nThis is Aslı Aydıntaşbaş from The Current."
  },
  {
    "id": "R032",
    "title": "国际货币基金组织：IMF：AI将冲击全球60%高薪岗位，但真正危险的只有一半",
    "digest": "[wechat_article.md]\n# 国际货币基金组织：IMF：AI将冲击全球60%高薪岗位，但真正危险的只有一半\n\n这份由国际货币基金组织（IMF）在2024年1月发布的Staff Discussion Note，可能是迄今为止对AI与劳动力市场关系最系统的全球性分析。它没有停留在“AI会取代多少工作”这类粗糙判断上，而是试图回答一个更关键的问题：哪些岗位会被AI替代，哪些会被AI增强，以及这种分化将如何重塑国家之间、阶层之间的财富分配。\n\n报告的核心结论值得每一个产业决策者和高净值读者认真对待：全球近40%的就业岗位暴露在AI影响之下，但不同国家、不同人群的命运将截然不同。先进经济体约60%的岗位面临AI冲击，其中约一半可能被削弱，另一半则可能因AI而获得生产力跃升。新兴市场和发展中经济体的暴露度则低得多，分别为40%和26%。\n\n这意味着什么？AI不会均匀地改变世界。它正在制造一条新的分界线——不是南北国家之间的旧分界线，而是“谁有能力利用AI”与“谁只能被动承受AI”之间的新分界线。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 先进经济体面临的双重命运：60%的暴露率背后是“一半天堂，一半地狱”\n\n报告最引人注目的发现之一，是先进经济体极高的AI暴露率。约60%的就业岗位被判定为“暴露于AI”——这个数字远高于新兴市场的40%和低收入国家的26%。原因很直接：先进经济体的就业结构以认知密集型岗位为主，而AI擅长的正是认知任务。\n\n但报告没有止步于此。它引入了一个关键区分：AI暴露并不等于AI替代。研究团队开发了一套新的衡量指标，试图区分“AI可能替代人类”和“AI可能增强人类”两种截然不同的影响路径。在先进经济体的高暴露岗位中，大约一半属于“高互补性”——即AI有望大幅提升这些岗位的生产力；而另一半则属于“高风险”——AI可能直接替代这些岗位的\n\n[... middle omitted ...]\n\n），或者希望加入讨论AI对特定行业的影响，欢迎扫码加入社群。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI对工作的影响，比你想象得更分化\n\nAI重塑就业格局\n\nIMF最新研究拆解了AI对不同人群的影响，结论很清晰：不是所有人都站在同一起跑线上。\n\n1️⃣ 谁更容易被AI影响？\n- 发达经济体约60%的工作暴露在AI影响下\n- 新兴市场40%，低收入国家仅26%\n- 原因：发达经济体以认知密集型工作为主，AI更容易替代或辅助\n\n2️⃣ 性别与教育差异明显\n- 女性和高学历人群更可能被AI影响，但也更容易受益\n- 年长工人适应性较差，转型难度更大\n- 高收入者如果与AI互补，收入会大幅提升；如果被替代，风险也更高\n\n3️⃣ 收入不平等可能加剧\n- 模型显示：如果AI与高收入者互补性强，劳动收入不平等会扩大\n- 资本回报增加会进一步拉大财富差距\n- 但如果生产力提升足够大，大多数人的收入水平还是会上涨\n\n4️⃣ 不同国家准备程度不同\n- 发达经济体应重点推动AI创新与监管框架\n- 新兴市场和发展中国家需要优先建设数字基础设施与技能培训\n- 所有国家都要加强社保网络，帮助受影响的工人转型\n\nAI不是在替代所有人，而是在重新分配机会。关键在于你能不能成为那个“互补”的人。\n\n#学习笔记\n\n[source_mineru.\n\n[... middle omitted ...]\n\ned7c176f41c3318410bd55d676a25e302efc5663ba34409ac5e66f.jpg)\n\n# IMF Staff Discussion Notes Research Department\n\n# Gen-AI: Artificial Intelligence and the Future of Work\n\nPrepared by Mauro Cazza\n\n[... middle omitted ...]\n\nT. Kyyrä, H. Hwang, and J. Tuomala. 2022. “Technology, Labour Market Institutions and Early Retirement.” Economic Policy 37 (112): 811–49.\n\n![](images/ad3b2b359842b04ea78b0d72e843d7960b1c886587a4a28d550404c23af185b1.jpg)"
  },
  {
    "id": "R033",
    "title": "兰德公司：AI Agent已让网络攻击成本降至20美元，无技能门槛",
    "digest": "[wechat_article.md]\n# 兰德公司：AI Agent已让网络攻击成本降至20美元，无技能门槛\n\n2025年，一个没有网络安全背景的普通人，即便借助当时最先进的AI聊天机器人，也几乎不可能攻破一台中等难度的靶机。2026年4月，同样的人，只需要安装一个开源工具、输入一段通用提示词，就能在不到一小时内完成攻击，总API成本不到20美元。\n\n这不是科幻，而是兰德公司（RAND Corporation）在2026年发布的一份最新实验报告的核心发现。这份报告的全称是《AI agents put offensive cyber within reach of novices》，它通过严谨的对照实验，揭示了一个正在发生的、但可能被大多数人低估的转折点：AI Agent，而非更强大的大模型本身，才是真正把网络攻击能力“平民化”的关键变量。\n\n兰德公司的实验设计非常清晰。他们首先在2025年8月到2026年1月间，招募了156名背景各异的参与者，包括技术小白和有一定技术背景的用户，让他们在有无AI辅助（当时最先进的Claude Opus 4.1和GPT-5）的情况下，尝试攻破三个难度递增的“夺旗”（CTF）挑战。结果令人沮丧：即便有AI帮助，参与者依然普遍挣扎，在中等和困难挑战上几乎没有成功案例。\n\n然后，在2026年4月，研究团队用同一个CTF环境，换上了Claude Code（一种AI Agent框架），搭配当时最新的Opus 4.6和Sonnet 4.6模型。结果发生了质变。AI Agent在几乎没有人类干预、无需任何网络安全知识的情况下，在不到一小时内攻破了所有三个挑战，总API成本仅为16.22美元。\n\n> **KC评论：** 这个对比的核心不在于模型从4.1升级到了4.6，而在于从“聊天机器人”切换到了“AI Agent”。聊天机器人需要人类告诉它每一步做什么，而Agent可以自主规划\n\n[... middle omitted ...]\n\n你快速把握市场动态，也适合作为AI模型的训练语料。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI黑客攻击，新手也能上手\n\nAI攻击平民化\n\n2026年，普通人也能搞定网络攻击\n\n某外资投行最新研报揭示了一个关键趋势：AI agent正在让复杂网络攻击变得“人人可操作”。2025年，即使有AI辅助，新手和技术用户也几乎无法完成中等难度的CTF挑战；但到了2026年4月，同样的任务被AI在1小时内、成本不到20美元全部解决。\n\n1️⃣ **2025年：AI辅助效果有限**\n- 156名参与者（从新手到技术用户）使用2025年8月的AI模型（如Claude Opus 4.1、GPT-5）\n- 新手在简单任务上成功率仅从8%提升到21%（统计不显著）\n- 中等和困难任务几乎无人完成，只有1位AI辅助用户成功通关\n\n2️⃣ **2026年：Claude Code的飞跃**\n- 使用Claude Code（Sonnet/Opus 4.6）重新测试相同挑战\n- 所有任务在1小时内解决，总API成本不到20美元\n- 无需专业网络知识，只需简单提示和基本监督\n- 模型自己完成侦察、漏洞利用、权限提升全流程\n\n3️⃣ **关键发现**\n- 2025年非专家无法完成的攻击，现在通过安装Claude Code即可实现\n- \n\n[... middle omitted ...]\n\nw.randeurope.org.\n\n## Research Integrity\n\nOur mission to help improve policy and decision making through research and analysis is enabled through our core values of quality and objectivity and\n\n[... middle omitted ...]\n\n a correspondingly large uplift. In either case, ensuring that cybersecurity capabilities can be measured continuously and reliably is essential to managing the risks and opportunities of increasingly capable AI systems."
  },
  {
    "id": "R034",
    "title": "兰德公司：AI Agent正在降低生物武器设计的技术门槛，但可靠性仍是关键瓶颈",
    "digest": "[wechat_article.md]\n# 兰德公司：AI Agent正在降低生物武器设计的技术门槛，但可靠性仍是关键瓶颈\n\n当大型语言模型开始像使用计算器一样调用生物设计工具，一个长期以来的安全假设正在被动摇。\n\n长期以来，生物安全领域有一个默认的防线：复杂的生物工具需要深厚的专业知识才能操作。这一假设构成了防止恶意使用者将前沿生物技术武器化的核心屏障。但兰德公司一份最新发布的评估报告，直接对这道防线提出了系统性的检验。\n\n这份由Jeffrey Lee等17位研究人员共同完成的报告，核心判断十分明确：当前最前沿的LLM Agent已经具备初步选择和操作生物工具的能力，这意味着非专业恶意行为者获取生物武器设计能力的门槛正在显著降低。但报告同时指出，这种能力在可靠性上参差不齐，距离构成实质性威胁仍有距离，而恰恰是这种“不完美的能力”，恰恰构成了最值得关注的监管窗口期。\n\n以下是对这份报告的深度解读。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 七款前沿模型全部通过“工具选择”测试，但场景理解暴露短板\n\n兰德团队设计了一套双轨评估体系。第一轨是“生物工具选择”知识测试，包含两类问题：一类是去情境化的直接提问，例如“哪种工具可以设计蛋白质”；另一类是嵌入具体生物设计场景的情境题，例如“在开发一种新型疫苗时，你需要预测病毒逃逸突变，应选用何种工具”。\n\n结果令人警醒。在直接提问中，所有七款前沿LLM（包括闭源和开源模型）的正确率均接近或达到80%。这意味着，这些模型能够准确地将“蛋白质设计”“免疫逃逸预测”等抽象功能与对应的生物工具匹配起来。它们知道工具箱里有什么。\n\n但当问题被包装成具体的生物工作流场景时，所有模型的准确率都出现了显著下降。模型在理解“这个任务在真实实验流程中处于哪个环节”时，暴露出明显的认知盲区。\n\n> **KC评论：** 这组对比揭示了一个关键\n\n[... middle omitted ...]\n\n前的AI与生物安全交叉领域，信息的时效性和深度理解同样重要。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nLLM Agent已经能操作生物工具了？\n\nAI+生物安全\n\n新报告：Agent初步可用\n\nRAND出了一份新报告，专门评估LLM Agent能不能选对、用对生物研究工具（BT）。\n\n核心发现很直接：能，但没那么稳。\n\n1/ 选工具还行\n7个前沿模型在“选对工具做对事”上表现都不错，得分接近80%。\n但一旦换成具体生物场景（比如“设计某蛋白”），准确率就掉。\n而且闭源模型在涉及“风险场景”时会频繁拒绝回答。\n\n2/ 操作工具：能跑，但容易翻车\n用EVEscape预测免疫逃逸、用ESM3做蛋白重设计，Agent都能上手。\n但一致性很差，换个蛋白目标就掉链子。\n常见翻车点：自主操作出错、数据处理失误。\n\n3/ 加提示词不一定有用\n给更多生物信息，结果并不稳定。\n有的任务变好，有的反而变差。\n也就是说，即使你懂生物学，也不一定能预测Agent会怎么反应。\n\n4/ 闭源模型“拒绝”是常态\n涉及病毒蛋白的任务，闭源模型经常直接拒绝执行。\n这种“拒绝”本身也是风险——如果模型只拒不安全任务，但坏人可以用开源模型绕过。\n\n一句话总结：LLM Agent已经能完成生物工具的基础交互，但可靠性和安全性都还远没达标。未来需要更深\n\n[... middle omitted ...]\n\nlops solutions to public policy challenges to help make communities throughout the world safer and more secure, healthier and more prosperous. RAND is nonprofit, nonpartisan, and committed to \n\n[... middle omitted ...]\n\nh.D. in social statistics.\n\nSteph Guerra is a Senior Research Resident at RAND leading research at the intersection of AI, biotechnology, and national security. Guerra holds a Ph.D. in Biological and Biomedical Sciences."
  },
  {
    "id": "R035",
    "title": "兰德公司：课外时间才是年轻人“软技能”的真正战场",
    "digest": "[wechat_article.md]\n# 兰德公司：课外时间才是年轻人“软技能”的真正战场\n\n当大多数讨论聚焦于学校课堂如何培养孩子的品格与社交能力时，一份来自兰德公司的最新研究报告给出了一个反直觉的判断：真正决定年轻人能否掌握“生活技能”的关键场景，不在校内，而在放学后。\n\n这份长达80余页、由华莱士基金会资助的实践指南，基于对全美六个城市超过100个课后项目的长期追踪，提炼出一个核心主张——课外时间项目（OST）才是年轻人发展自我意识、团队协作、毅力和负责任决策能力的最优场域。而连接这些项目与标准化学校的“中介组织”，正在成为整个教育生态中最被低估的力量。\n\n这不是一份关于“教育公平”的泛泛之谈。兰德公司给出的是一套可复制的操作框架：从建立生活技能框架，到连接循证资源，再到设计专业发展路径。每一个环节都指向同一个问题——我们如何把“软技能”从一个模糊的概念，变成可衡量、可执行、可规模化的事实。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 中介组织才是“软技能”落地的核心杠杆，而非学校本身\n\n报告开篇即点明一个被长期忽视的结构性事实：课外时间项目提供了学校无法替代的环境——安全、低压力、关系驱动。在课后场景中，年轻人与关爱他们的成年人和同龄人建立关系，在活动中练习自我控制、团队合作、目标设定和坚持完成。这些正是生活技能的核心要素。\n\n但问题在于，大多数课后项目缺乏系统性的能力建设框架。此时，兰德公司定义的“中介组织”就成为了关键角色。这类组织可以是联合劝募协会、基督教青年会、男孩女孩俱乐部，也可以是城市政府部门或州级协调机构。它们不直接面对年轻人，而是连接、协调、赋能那些直接提供服务的课后项目。\n\n> **KC评论：** 这意味着，如果你关注年轻人发展，不要只盯着学校改革。真正值得投入资源的地方，是那些看似边缘的课后项目及其背后的协调网络。这些中介组织正\n\n[... middle omitted ...]\n\n的投资人和决策者，一起探讨那些报告里没有完全展开的二阶问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n标题：课后项目如何培养孩子核心能力\n\n封面：成长的关键时刻\n\n副标题：不止是托管，更是能力培养场\n\n正文：\n\n你有没有想过，孩子放学后的那几小时，其实藏着巨大的成长机会？\n\n最近读了一份由RAND Corporation发布的研报，讲的是课后项目（OST）如何系统培养青少年的生活技能。不是鸡汤，是经过6个城市、100多个项目验证的方法论。\n\n核心发现：课后项目是培养生活技能的黄金场景，关键是三个抓手要联动。\n\n1️⃣ 建立生活技能框架\n- 不是随便抓几个词贴墙上\n- 需要明确：自我意识、团队合作、做负责任的决定等\n- 框架要贯穿所有活动设计，而不是单独开课\n\n2️⃣ 连接循证资源\n- 找到经过验证的工具和方法\n- 把技能培养融入日常活动，比如团队游戏、项目合作\n- 设置清晰的学习目标，给足练习时间\n\n3️⃣ 专业发展支持\n- 一线工作者需要培训才能把框架落地\n- 不是一次性培训，而是持续的支持\n- 包括如何营造氛围、如何把技能和活动挂钩\n\n有意思的是，2021年全美调查显示，家长最希望在课后项目中培养的三个能力是：社交技能、团队合作、自信心。这和研报的核心发现高度一致。\n\n研报特别强调：框架、资源、培训三者缺\n\n[... middle omitted ...]\n\nprofit, nonpartisan, and committed to the public interest. To learn more about RAND, visit www.rand.org.\n\n## Research Integrity\n\nOur research integrity is grounded in RAND's core values of qua\n\n[... middle omitted ...]\n\nssioned by\nThe Wallace Foundation\n\nwww.rand.org\n\n![](images/0d33abe634a1b7652729700cbdabf849131146819b87ee51be479849953c5f7c.jpg)\n\n\\$44.00\n\n![](images/3c1797454d550c987d68e9cdb3d9b6a65c41ea0ffa35e9526091223497eb0b74.jpg)"
  },
  {
    "id": "R036",
    "title": "兰德公司：AI缺的不是芯片，是电网里的天然气轮机",
    "digest": "[wechat_article.md]\n# 兰德公司：AI缺的不是芯片，是电网里的天然气轮机\n\n当全球目光聚焦于英伟达的GPU供应是否充足时，一份来自兰德公司的深度报告揭示了更底层、也更棘手的瓶颈：支撑AI算力扩张的电力基础设施，其供应链远比想象中脆弱。\n\n这份由兰德公司Center on AI, Security, and Technology团队撰写的研究，系统性地评估了美国为满足前沿AI数据中心电力需求所需的关键电气设备供应链。结论并非耸人听闻，但足够令人警觉：到2030年，仅前端计量（FTM）设备的供应链威胁，就可能导致美国电网可用净容量下降7%至31%。而如果数据中心被迫大规模转向离网供电（Bridge Power），对天然气轮机的额外需求将是一个在现有供应链上几乎不可能完成的任务。\n\n这不再是一个“电力够不够用”的宏观叙事，而是一个“设备能不能按时造出来、运到、装好”的工程与供应链问题。对于任何关注AI基础设施投资、科技巨头资本开支方向以及美国再工业化进程的决策者而言，这份报告提供了一个必须纳入决策框架的分析工具。\n\n> **KC评论：** 很多关于AI能源的讨论停留在“可再生能源占比”或“核电重启”的宏大叙事上。兰德这份报告的价值在于，它把问题拆解到了具体设备级别——天然气轮机、变压器、电池——并量化了每种设备供应链脆弱性的来源。读完你会发现，真正的瓶颈可能不是“有没有电”，而是“能不能造出足够多的变压器和轮机来把电送到数据中心”。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 供应链脆弱性并非均匀分布：发电设备比输电设备更危险\n\n报告的核心贡献之一，是构建了一个复合供应链脆弱性评分体系，并以此对关键电气设备进行排名。结论清晰且具有政策含义：发电侧组件的脆弱性系统性高于输电侧组件。\n\n在2025年的排名中，前端计量（FTM）发电类别里，蒸汽轮机、\n\n[... middle omitted ...]\n\n标准化能否在五年内落地？以及，谁最终会为这场供应链韧性买单。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI数据中心，电够用吗？\n\n电不够用\n\n2030年缺口最大\n\n最近看了一份RAND的研报，专门分析AI数据中心的电力供应链。信息量很大，我帮你拆成3个核心发现👇\n\n1️⃣ 电力设备供应链比想象中脆弱\n- 天然气轮机、蒸汽轮机、变压器、电池这些关键设备，都在供应链脆弱性排名前列\n- 发电设备比输电设备更脆弱，因为技术门槛高、供应商少\n- 变压器的主要问题是需求波动大，涡轮机则是市场太集中\n\n2️⃣ 供需缺口有多大？\n- 假设供应链正常，2030年可能仍有7%-31%的电力缺口\n- 如果数据中心想靠离网自发电，需要额外91-123台110MW涡轮机（2027年），到2030年这个数字会飙升到1582-1690台\n- 离网并不能解决供应链问题，因为需要的设备跟并网基本一样\n\n3️⃣ 哪些方向值得关注？\n- 钠电池替代锂电池：供应链脆弱性更低，可能是储能新方向\n- 设备标准化：能缓解市场集中度问题\n- 建立战略储备：像石油储备一样，储备关键电网组件\n\n研报还提到，美国NERC已经警告，未来5-10年北美一半以上区域面临电力短缺风险。AI需求、电气化、工业增长三管齐下，电网压力不小。\n\n欢迎一起讨论：你觉得AI数据中心\n\n[... middle omitted ...]\n\nch integrity is grounded in RAND's core values of quality and objectivity. Rigorous quality assurance procedures, conflict of interest screening, and transparency in funding ensure that every \n\n[... middle omitted ...]\n\nstructure build-out, the systemic risks emerging from recent development, and government finance and equity implications of adaptation interventions. He holds an M.P.A. with a concentration in economic and public policy."
  },
  {
    "id": "R037",
    "title": "世界银行：AI准备度差距的真正分水岭，不在算力而在经济复杂度",
    "digest": "[wechat_article.md]\n# 世界银行：AI准备度差距的真正分水岭，不在算力而在经济复杂度\n\n全球AI竞赛的叙事，长期被两个极端主导。一端是中美两国在基础模型、算力集群和前沿人才上的军备竞赛；另一端是大量发展中国家连基本数字基础设施都尚未完成，似乎注定被新一轮技术鸿沟吞噬。但世界银行最新发布的工作论文《超越AI鸿沟》给出了一个更具政策操作性的判断：决定一个国家能否在AI时代“超常发挥”的关键变量，不是它有多少GPU，而是其经济复杂度——即经济体所拥有的知识、技能和生产能力的多样性与精密程度。\n\n这份报告利用国际货币基金组织2023年发布的AI准备度指数，结合经济复杂度指数，构建了一套筛选“全球和本地AI超常表现者”的简洁方法。研究覆盖125个国家，发现经济复杂度可以解释约70%-80%的AI准备度差异。但真正有价值的不是这个相关系数，而是那些落在回归线上方的国家——它们以低于预期的经济复杂度，实现了高于预期的AI准备度。这些国家的经验，才是全球政策制定者最应该学习的样本。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 经济复杂度是AI准备度的最强单一预测因子，但超常表现者揭示的才是关键\n\n报告的核心方法论并不复杂。研究者将每个国家的AI准备度指数对经济复杂度指数做加权回归，然后识别出那些实际得分显著高于预测得分的国家。R方值高达0.70-0.79，意味着经济复杂度几乎可以解释AI准备度四分之三的跨国差异。\n\n这个发现本身并不令人意外。一个能够生产复杂电子产品、拥有深厚研发积累的经济体，自然更容易部署和吸收AI技术。但报告的价值在于追问：为什么有些国家能够“超常发挥”？它们做对了什么，让AI准备度超过了经济复杂度的“天花板”？\n\n答案指向一个被广泛讨论但较少被量化检验的维度：制度质量。通过贝叶斯模型平均法分析67个历史、政治和经济指标，报告发现，1\n\n[... middle omitted ...]\n\n动态。这些材料可以帮助你建立自己的“AI能力拼图”分析框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI比你想象中更“势利”\n\nAI的“势利眼”\n\n财富与准备度强相关，但有些国家跑赢了。\n\n1/ 投行研报用IMF的AI准备度指数（AIPI）对比经济复杂度指数（ECI），发现：高收入国家普遍准备更充分，但新加坡、韩国、北欧国家属于“全球超常发挥”。\n\n2/ 中低收入组也有赢家：中国、马来西亚、印尼、越南、印度、加纳、卢旺达——这些国家在AI准备上跑赢了自身经济复杂度。\n\n3/ 驱动因素分三档：\n- 低收入国：法规+劳动力培训是基础\n- 中高收入国：法规+人力资本+数字基建并行\n- 高收入国：法规+数字基建+创新系统全面成熟\n\n4/ 有趣发现：儒家文化圈（中/新/韩/港）和东亚地区在AI准备上持续领先，政治不稳定则显著拖后腿。\n\n5/ 方法很简单：拿AIPI实测值，减去基于ECI的预测值，正残差就是“超常发挥者”。人口加权，确保大国的实际影响力被合理反映。\n\n所以AI准备度，不只看钱，还要看制度、教育、基建的“组合拳”。资源有限的国家，选对赛道也能弯道超车。\n\n你们觉得，中国在AI应用落地方面，是“超常发挥”还是“正常发挥”？\n\n#学习笔记\n\n[source_mineru.md]\n# Beyond the\n\n[... middle omitted ...]\n\nring a comprehensive assessment of national artificial intelligence capabilities. The findings highlight the varying significance of regulation and ethics frameworks, digital infrastructure, a\n\n[... middle omitted ...]\n\nrom the “wbopendata” module in Stata (Azevedo, 2020), with data for Taiwan Province of China obtained from the Statista website. For more details, see the \\`\\` Data and Methodology\" and \\`\\` Empirical Findings\" sections."
  },
  {
    "id": "R038",
    "title": "世界银行：高债务国家反而能从数据透明中获益——这对全球债券投资者意味着什么",
    "digest": "[wechat_article.md]\n# 世界银行：高债务国家反而能从数据透明中获益——这对全球债券投资者意味着什么\n\n全球投资者在配置新兴市场主权债券时，习惯性将“高债务”等同于“高风险、低回报”。世界银行最新工作论文（Policy Research Working Paper 11054）提供了一个反直觉的结论：在高债务国家，提升数据透明度不仅不会压低回报，反而能吸引更多资本流入，显著提升主权债券回报率。这一发现挑战了传统认知——过去学界和市场的注意力几乎全部集中在“透明度如何降低借款国融资成本”这一面，而几乎没有人系统测算透明度对债权人（即全球债券投资者）的收益贡献。\n\n这份报告的真正价值在于，它把数据透明度的受益者从借款国扩展到投资者，并给出了可量化的阈值和国别收益表。对于正在重新评估新兴市场敞口的机构投资者而言，这是一个需要认真对待的信号。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 数据透明度的回报效应存在“制度门槛”——低于这个门槛，透明度反而无效\n\n报告的核心发现之一是，数据透明度对主权债券回报的正向影响并非线性，而是取决于借款国的制度质量。研究使用国际国家风险指南（ICRG）指数作为制度质量的代理变量，发现只有当ICRG指数（取对数后）超过4.15时，提升透明度才能显著提高债券回报。换算成原始分值，这意味着借款国的制度质量得分至少需要达到约63.66分（满分100分）。\n\n这个门槛的含义非常清晰：在制度质量较低的国家，即使政府发布更多数据，投资者也不会因此给予更高的回报溢价。原因在于，在制度薄弱的环境中，数据的可信度本身存疑——投资者无法确定公开数据是否反映了真实的经济状况。只有在制度质量达到中等以上水平时，透明度的提升才能转化为投资者信心的改善，进而推高债券价格。\n\n> **KC评论：** 投资者在筛选新兴市场债券时，不应只看债务率和透\n\n[... middle omitted ...]\n\n以及我们整理的国别收益计算明细，欢迎加入社群，每天获取更新。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n透明数据，才是真“金”矿\n\n数据透明能赚钱？\n\n投行研报发现，提高数据透明度，能帮主权债投资者赚更多回报。逻辑链条很清晰：\n\n**1/ 数据透明 ≠ 立刻赚钱，要看门槛**\n- 只有在制度质量中上的国家，数据透明才对债券回报有正面影响\n- 门槛值：ICRG评分（对数）＞4.15，大概对应制度质量中等偏上\n\n**2/ 高负债不是死局，透明能“解药”**\n- 债务高的国家，债券回报通常更低\n- 但增强数据透明，能抵消高负债的负面冲击\n- 即使负债率很高，透明化也能让投资者更愿意买\n\n**3/ 投资者能赚多少？研报算了笔账**\n- 如果借款国把数据透明提升到中高收入国家前10%水平\n- 不同地区的额外收益差异很大：\n  - 东亚：566个基点（约3178亿美元）\n  - 拉美：527个基点（约2928亿美元）\n  - 撒哈拉以南非洲：825个基点（约1126亿美元）\n  - 中东北非：395个基点（约334亿美元）\n\n**4/ 信用评级也很重要**\n- S&P主权评级是投资者决策的有效信号\n- 评级越高，透明化的正向效果越明显\n\n**5/ 为什么投资者在乎？**\n- 透明数据降低信息不对称，减少风险溢价\n- \n\n[... middle omitted ...]\n\n that it examines the relationship between sovereign bond returns and data transparency, and then calculates the benefits accrued by external creditors from improved data transparency in the b\n\n[... middle omitted ...]\n\n 2: Impact of a 10% Change in Data Transparency on Sovereign Bond Returns Conditional on the Level of PPG External Debt in 2020 by Region  \n![](images/109884ab3b56e4ebeeefa2c6448ef2f33ccb3f25d0b85da3b034bb7e85acd2fd.jpg)"
  },
  {
    "id": "R039",
    "title": "世界银行：冲突地带才是全球生物多样性保护的真正盲区",
    "digest": "[wechat_article.md]\n# 世界银行：冲突地带才是全球生物多样性保护的真正盲区\n\n全球生物多样性正在以自然基线1000倍的速度消失。1万个物种濒临灭绝，68%的种群规模自1970年以来已经下降。这些数字并不新鲜。真正值得关注的问题是：最需要保护的区域，恰恰是数据最稀缺、治理最薄弱、冲突最频繁的地方。\n\n世界银行最新发布的工作论文（Policy Research Working Paper 11076）给出了一个反常识的判断：全球生物多样性保护的最大缺口，不在亚马逊雨林，不在东南亚热带丛林，而在那些“法律地位未定”的领土、武装冲突频发的国家、以及机构脆弱的失败国家。这些区域覆盖了311个国际河流流域、18个海洋联合管辖区、35个非确定法律地位领土，以及19个冲突影响国家和20个脆弱国家。\n\n更关键的是，世界银行的团队利用全球生物多样性信息设施（GBIF）的开放数据，通过机器学习方法绘制了近60万个物种的分布地图。这些地图揭示了一个令人不安的事实：上述区域不仅是物种丰富度最高的地区之一，也是特有物种和濒危物种最集中的地区。换句话说，人类冲突最激烈的地方，恰好是地球生物多样性最珍贵的地方。\n\n---\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 冲突与治理真空地带，恰恰是物种多样性的最后堡垒\n\n世界银行的这项研究并非凭空发出呼吁。它基于一套全新的、经过专家验证的物种分布数据库。研究团队利用GBIF自1970年以来的数亿条经纬度标记的物种记录，通过alphahull算法和k-means聚类算法，生成了涵盖陆生、淡水和海洋环境的近60万个物种的分布图。\n\n将这些地图与全球冲突数据库、脆弱国家指数、国际河流流域边界等空间数据叠加后，一个清晰的模式浮现出来：非确定法律地位领土（如西撒哈拉、克什米尔等）、冲突影响国家（如叙利亚、也门）、以及机构脆弱国家（如索马\n\n[... middle omitted ...]\n\n们一起探讨：在冲突与生态的交汇地带，数据能否成为真正的桥梁。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球冲突区的生物多样性，还有救吗\n\n冲突区也有生态希望\n\n保护生物多样性的关键，是可靠又可比的数据\n\n---\n\n**1. 别以为生物多样性只在“和平区”重要**\n\n全球生物多样性正以自然速率1000倍的速度消失，但最容易被忽略的，恰恰是那些冲突区、边界模糊区、治理脆弱区。这些地方物种丰富度不低，但保护难度极高：政策弱、执法乱、机构散。\n\n某外资投行最新研报用GBIF公开数据做了件大事——绘制了近60万种物种的分布图，专门覆盖了：\n- 35个法律地位未定区域\n- 19个受冲突影响国家\n- 20个脆弱国家\n- 18个海洋联合管辖区\n- 311个国际河流流域\n\n**2. 数据是“破冰”的工具**\n\n冲突区最大的问题不是物种少，而是没有可比的基础数据。各方不信任，数据不共享，保护无从下手。\n\n报告用的方法很聪明：GBIF数据库+机器学习模式识别，从1970年至今的物种记录中提取有效信息，不依赖政府官方监测。这意味着，即使某个国家政府瘫痪，卫星和公民科学家的数据依然能支撑保护规划。\n\n**3. 三个关键发现**\n\n① 这些“麻烦区域”里，栖息着大量特有物种和高灭绝风险物种，尤其需要针对性保护措施。\n\n② 数据可比性比数\n\n[... middle omitted ...]\n\nange. Effective conservation requires urgent, coordinated global action, as ecosystems and species habitats often transcend national borders. Collaboration among governments, industries, and c\n\n[... middle omitted ...]\n\nnd Implementation Plan for the Zambezi River Basin (ZAMSTRAT). https://zambezicommission.org/publication/integrated-water-resources-management-strategy-and-implementation-plan-zambezi-river-1 (Accessed 11 December 2024)."
  },
  {
    "id": "R040",
    "title": "世界银行：国企不是铁饭碗，它真正改变的是市场生态",
    "digest": "[wechat_article.md]\n# 世界银行：国企不是铁饭碗，它真正改变的是市场生态\n\n过去几年，关于国有企业在疫情中扮演“稳定器”角色的讨论重新升温。但一个被长期忽视的问题是：当政府以股东身份深度参与竞争性行业时，它对就业、创新和整个市场的活力究竟意味着什么？\n\n世界银行最新发布的工作论文，以巴西为样本，给出了一个层次丰富的答案。这份报告没有停留在“国企效率高还是低”的二元争论，而是通过一个涵盖全资国有、混合所有制和参股企业的独特数据集，揭示了国家作为企业所有者的多重影响。\n\n核心判断是：国企确实支付了显著更高的工资溢价，私有化会压降工人薪资，但并未导致大规模裁员。真正值得警惕的，是国企的行业存在感越高，年轻企业的生存空间越小，市场集中度越高——这种“稳态”可能是以牺牲创新和竞争为代价的。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 国企的工资溢价不是幻觉，但私有化的冲击也真实存在\n\n报告首先确认了一个直观感受：在巴西，国企员工确实挣得更多。在控制企业特征后，国企的工资溢价约为18.5%。但当进一步控制员工个体固定效应——即排除“能力强的人更倾向于选择国企”这种自选择偏差后，溢价大幅缩水至4.5%。\n\n这意味着，国企高薪的相当一部分，是因为它吸引了更优秀的人才，而非单纯因为“体制内”的定价机制。但即便如此，4.5%的纯制度性溢价仍然存在。\n\n更关键的是私有化带来的冲击。报告采用事件研究法发现，私有化发生后，留在原企业的员工在头两年内相对工资下降约10%。而且被裁撤的员工更集中于高学历、高年龄和长工龄群体——这暗示私有化不仅是薪资调整，更是一次面向效率的劳动力重组。\n\n> **KC评论：** 这组数据值得投资人关注。如果中国推进国企混改或竞争性领域退出，短期内的劳资摩擦和薪资调整是必然的，但报告也指出“没有稳健证据表明私有化导致总就业下降”。这意味着\n\n[... middle omitted ...]\n\n集，方便喂给AI或快速把握市场动态），欢迎加入社群继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n国企研究：巴西的就业与市场真相\n\n**国企≠铁饭碗？**\n\n**一份世界银行研报的深度拆解**\n\n最近读了份世界银行的巴西国企研报，数据量超大，逻辑也很清晰。简单拆解几个核心发现，看看国企（BOS）到底对经济和打工人意味着什么。\n\n1️⃣ **国企确实给得更多**\n数据显示，巴西国企平均工资比私企高18.5%。但如果控制员工个人能力差异（比如高学历、高技能的人更倾向于去国企），这个溢价会降到4.5%。也就是说，国企的高工资有一部分是“人才筛选”的结果，而非纯粹的制度红利。\n\n2️⃣ **私有化后，工资会降**\n研究追踪了国企私有化后的员工工资变化，发现：\n- 私有化后头两年，员工相对工资下降约10%\n- 被裁员的往往是教育水平更高、年龄更大、工龄更长的员工\n- 但有趣的是，私有化并未导致公司总就业人数显著下降——企业可能通过结构优化而非简单裁员来调整\n\n3️⃣ **国企对市场活力的双重影响**\n研报用了2016-2020年的数据，发现国企占比高的行业：\n- ❌ 年轻企业参与度降低，新公司更难进入\n- ❌ 企业退出率下降（市场竞争筛选减弱）\n- ❌ 市场集中度上升\n- ✅ 但净就业变化为正，因为就业创造率高于就\n\n[... middle omitted ...]\n\nwned or mixed enterprises and with indirect state participation in competitive sectors. The paper looks at their impact through two connected perspectives: employment and business dynamism. Fi\n\n[... middle omitted ...]\n\nf employees. The results indicate that privatized BOS have a wage premium of 0.04 log points larger than their non-privatized peers, the difference between the two groups is not statistically different from zero. $^{18}$"
  },
  {
    "id": "R041",
    "title": "世界银行：亲密伴侣暴力数据采集，隐私先行不是可选项",
    "digest": "[wechat_article.md]\n# 世界银行：亲密伴侣暴力数据采集，隐私先行不是可选项\n\n在发展中国家农村地区，亲密伴侣暴力（IPV）是一个被严重低估的问题。传统面对面访谈中，女性因恐惧、羞耻和隐私担忧而选择沉默，这不仅是数据质量问题，更是政策干预失准的根源。世界银行最新政策研究工作报告（编号11077）基于巴基斯坦农村近6,135名已婚女性的实验，给出了一个反常识的发现：让受访者先用音频电脑辅助自填问卷（ACASI）私下回答敏感问题，能显著提升随后面对面访谈中的披露率——幅度高达41%至57%。\n\n这不是技术细节，而是测量方法论的范式转换。它意味着，在文盲率高达93%的农村贫困环境中，隐私保护不是可选项，而是获取真实数据的必要条件。对于所有从事发展中国家社会政策评估、性别研究及发展经济学实证研究的从业者而言，这份报告的价值不在于技术本身，而在于它挑战了一个长期存在的假设：文盲群体无法有效使用自填问卷。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 文盲并非自填问卷的障碍，设计不当才是\n\n长期以来，学界普遍认为自填问卷在低识字率群体中不可行。Park等人（2021）在利比里亚和马拉维的研究显示，约三分之一的受访者无法正确回答训练问题，这直接挑战了ACASI方法在文盲群体中的有效性。但世界银行团队在巴基斯坦拉亚县（Layyah）的实验给出了截然不同的结论。\n\n关键在于界面设计的适应性改进。传统ACASI使用彩色方块或形状代表不同答案选项，要求受访者记忆颜色与答案的映射关系，这对认知能力是额外负担。世界银行团队与当地调查员合作，开发了更直观的图像：将频率类李克特量表的每个选项与具体图像关联，而非抽象符号。例如，“从未发生”对应空白，“发生一次或两次”对应少量符号，“发生三次及以上”对应多个符号。\n\n实验结果显示，即使随机化答案选项的排列顺序（升序与降序），\n\n[... middle omitted ...]\n\n行一起探讨这些方法论创新如何落地到你的研究或项目评估中。**\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n家暴数据很难收集？这个实验颠覆认知\n\n📊 数据采集，方法比想象更重要\n\n最近读了一份巴基斯坦的田野实验研报，讲的是怎么让受访者更愿意说出家暴经历。数据来自6000多位农村已婚女性，93%不识字。\n\n核心发现很反直觉👇\n\n1️⃣ 不识字也能用自助问卷\n传统观点认为，文盲率高就不能用自填问卷。但实验用音频自助访谈（ACASI）配合图像选项，发现受访者完全能理解。通过随机打乱选项顺序测试，回答结果一致，说明不是乱选。\n\n2️⃣ 先私下回答，再面对面，坦诚度飙升\n实验把两个家暴问题分成两组：一组先面对面问，另一组先通过ACASI私下回答。结果：先私下回答的那组，后续面对面时，家暴披露率高出41%-57%。\n\n3️⃣ 非敏感问题没这个效应\n同样的问题换成“丈夫吃了几次肉”，先私下还是先面对面，回答几乎没差别。说明这个机制不是简单的“习惯问卷”，而是针对敏感话题的破冰效应。\n\n为什么有效？研究者推测，先让受访者在私密环境下“演练”一次，能降低羞耻感和恐惧，后续面对真人调查员时更容易开口。\n\n这个设计对很多敏感话题的调查都有启发——不是技术多先进，而是怎么让人感到安全。\n\n欢迎一起讨论，你遇到过哪些“知道但说不出口”的调查\n\n[... middle omitted ...]\n\nompare disclosure of intimate partner violence when questions were asked face-to-face first versus through audio computer-assisted interviewing first. The findings show that despite high illit\n\n[... middle omitted ...]\n\n Malawi. NBER Working Paper 29584.\n\nPeterman, A., Dione, M., Le Port, A., Briaux, J., Lamesse, F. and Hidrobo, M. (2024). Disclosure of violence against women and girls in Senegal. World Bank Economic Review Forthcoming."
  },
  {
    "id": "R042",
    "title": "世界银行：避孕针到家，反而降低了避孕覆盖率？",
    "digest": "[wechat_article.md]\n# 世界银行：避孕针到家，反而降低了避孕覆盖率？\n\n在布隆迪的农村，一项旨在让社区健康工作者上门提供长效避孕注射剂的干预实验，得到了一个反直觉的核心结论：服务可及性的大幅提升，并没有带来避孕覆盖率的净增长。世界银行发布的这份政策研究工作论文指出，授权社区健康工作者在例行家访中提供新一代皮下避孕注射剂，虽然使得这种注射剂的用量飙升约70%，但代价是女性放弃了原本可能选择的长效避孕植入物和宫内节育器。这意味着，一个看似“更便捷”的供给方案，最终可能削弱了整体的避孕保护效果。\n\n这份报告的价值，不在于它否定社区健康工作者的作用，而在于它揭示了发展干预中一个极易被忽视的结构性问题：**供给侧的效率提升，如果无法匹配需求侧的真实偏好和认知，可能引发非预期的替代效应，最终导致干预目标的落空。** 对于任何关注新兴市场、公共卫生政策、以及“最后一公里”服务交付的决策者而言，这都是一则必须认真对待的警示。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 便捷性提升并未转化为整体覆盖率的增长，替代效应是核心原因\n\n这份研究最核心的发现，是干预措施在增加特定产品使用量的同时，未能扩大整体避孕药具的覆盖范围。实验数据显示，在干预组，Sayana Press（一种预充式、可皮下注射、提供三个月保护的新型避孕针）的月均使用量比对照组高出约13个单位，增幅约70%。然而，健康中心报告的总避孕药具分发量并没有发生统计学上显著的变化。\n\n> **KC评论：** 这组数据揭示了一个关键逻辑：当一种新服务被引入时，我们不能只看它自身的增长，更要看它是否在“吃掉”其他更有效的服务。世界银行的这份报告明确指出了“替代效应”的存在。对于读者而言，这意味着在评估任何政策或商业模式的创新时，必须同时考察其“净增量”和“替代量”，而非仅仅关注“使用量”的增长。完整报告中\n\n[... middle omitted ...]\n\n未来的展望感兴趣，欢迎加入社群，领取完整研报解读与原始图表。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n布隆迪农村避孕新策略：社区护士是关键\n\n社区护士上门打针\n\n一次培训，避孕注射量增加70%\n\n最近读了一篇某外资投行的研报，讲的是非洲布隆迪农村怎么提高避孕覆盖率。逻辑很清晰，分享给大家。\n\n1/ 背景是啥？\n布隆迪农村，避孕率很低（只有21.5%）。传统方法要跑卫生所，路远、排队、怕被人看见，很多女性就不去了。\n\n2/ 他们做了什么？\n让社区护士（CHW）经过培训后，可以在日常家访时给女性打一种新型避孕针（Sayana Press）。这种针是皮下注射，比传统肌肉注射简单，社区护士就能操作。\n\n3/ 结果怎么样？\n- 避孕针使用量增加了约70%！数据很扎实。\n- 但！整体避孕覆盖率并没有显著提升。\n- 为什么？因为很多女性从长效避孕方式（比如避孕植入物、宫内节育器）换成了这个针，产生了“替代效应”。\n\n4/ 核心洞察：\n这个干预措施增加了便利性和隐私性（社区护士本来就是熟人，不会引起注意），但并没有创造新的避孕需求，只是改变了避孕方式的选择。\n\n5/ 一个值得思考的点：\n研报提到，这种皮下注射针未来可能让女性实现“自我注射”，那隐私性和便利性会进一步提升。但如何避免单纯的替代效应，真正提高整体避孕覆盖率，还是\n\n[... middle omitted ...]\n\nncrease of approximately 70 percent in the administered quantity of these injections, which provide average protection for three months. However, the results suggest that the intervention does\n\n[... middle omitted ...]\n\nation and development review 43(Suppl Suppl 1), 166–191.\n\nUnited Nations (2022). World Family Planning 2022: Meeting the changing needs for family planning: Contraceptive use by age and method. UN DESA/POP/2022/TR/NO. 4."
  },
  {
    "id": "R043",
    "title": "世界银行：中东产油国补贴越狠，碳排放越高，但经济并未受益",
    "digest": "[wechat_article.md]\n# 世界银行：中东产油国补贴越狠，碳排放越高，但经济并未受益\n\n全球每年有7万亿美元被用于化石燃料补贴，相当于德国和法国GDP之和。这笔钱没有让经济更快增长，却让碳排放居高不下。\n\n世界银行最新工作论文对中东和北非41个国家2011-2018年数据的实证分析，得出了一个反直觉却极具政策含义的结论：石油补贴对中东产油国的经济增长既无短期刺激，也无长期拉动。但补贴每增加一个百分点，二氧化碳排放就显著上升。\n\n这不是一个关于道德的说教，而是一个关于资源配置效率的冷酷计算。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 补贴的真正问题不是价格，是它掩盖了一个结构性扭曲\n\n传统讨论中，化石燃料补贴被视为一种社会福利安排——政府通过压低能源价格来降低居民生活成本、支持工业竞争力。但这种理解忽略了中东产油国的特殊结构。\n\n世界银行报告指出，中东产油国的补贴机制与石油进口国完全不同。对于沙特、伊朗这样的国家，原油生产成本极低——2016年沙特每桶生产成本仅约8.5美元，而国际油价平均43美元。政府补贴的不是“成本价以上”的部分，而是“国际价格与国内售价之间的差额”。\n\n这意味着补贴的本质不是让穷人买得起油，而是让整个经济体长期生活在扭曲的价格信号中。当国内油价被人为压低到远低于国际水平，能源密集型产业获得了隐性竞争优势，消费者失去了节能激励，整个经济结构被锁定在“高能耗、高碳排”的路径上。\n\n> **KC评论：** 这份报告的真正洞见不在于“补贴不好”这个常识，而在于它量化了“补贴到底有多无效”。报告用面板数据证明了，补贴对经济增长的贡献在统计上不显著，但对碳排放的影响却非常显著。这意味着中东产油国正在用巨大的财政支出，换来了一个既没有增长、又加剧气候风险的坏结果。完整报告中包含了对41个国家2011-2018年逐年的详细回归结果和稳健\n\n[... middle omitted ...]\n\n喂给AI做进一步分析，也适合在早餐时间快速把握全球市场动态。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nMENA石油补贴：减碳与增长的意外真相\n\n减碳≠牺牲增长\n\n某外资投行最新研报，对MENA（中东和北非）41国做了实证分析，结论有点反直觉——\n\n1/ 石油补贴是碳排放的“加速器”\n- 在MENA产油国，石油补贴与碳排放强正相关\n- 主要通过“能源消费路径”起作用\n- 即使控制消费效应，补贴本身对碳排放仍有直接影响（可能来自制造业）\n\n2/ 补贴取消≠经济受损\n- 无论短期还是长期，石油补贴对经济增长都没有显著正向影响\n- 这意味着：取消补贴不会拖累经济\n- 对产油国和非产油国都成立\n\n3/ 政策顺序很重要\n- 在补贴规模大的地方，取消补贴是“最优策略”\n- 碳税虽然有效，但实施需要更长时间\n- 建议：先取消补贴，再推碳税\n\n4/ 全球视角：MENA的碳贡献被低估\n- MENA占全球石油产量36.1%，天然气21.7%\n- 油气生产贡献全球15%温室气体\n- 加上运输消费端，实际碳排远高于统计的5%\n\n5/ 一个有趣的测算\n- 沙特2016年石油生产成本约8.5美元/桶\n- 加上精炼和运输，总成本约14美元\n- 但国际油价约43美元\n- 补贴参照系不同，规模差异巨大\n\n核心洞察：减碳不是零和游戏，取消补贴反而\n\n[... middle omitted ...]\n\nThese new estimates contribute to the literature seeking to understand the pros and cons and effectiveness of various policy instruments in promoting decarbonization, with particular focus on \n\n[... middle omitted ...]\n\ntd><td>369</td><td>5.06E-09</td><td>1.34E-08</td><td>0</td><td>9.97E-08</td></tr><tr><td>subsidy share of GDP: MENA oil exporters</td><td>369</td><td>4.11E-09</td><td>1.32E-08</td><td>0</td><td>9.97E-08</td></tr></table>"
  },
  {
    "id": "R044",
    "title": "世界银行：不决策，也是一种权力",
    "digest": "[wechat_article.md]\n# 世界银行：不决策，也是一种权力\n\n世界银行最新政策研究工作论文提出一个看似反直觉的判断：在家庭决策中，不直接参与决策的人，未必是缺乏权力的人。相反，某些人恰恰因为权力足够大，才选择不决策。这份基于肯尼亚沿海农村家庭数据的深度研究，正在挑战发展经济学和性别研究中沿用了数十年的“代理权”测量框架。\n\n如果你长期关注发展经济学、性别平等政策或家庭内部资源配置，这份报告值得你花时间理解。因为它可能意味着，我们过去用来衡量女性赋权的“决策参与度”指标，存在系统性低估——但不是低估了女性，而是低估了男性。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. “不决策”背后存在两种截然不同的权力逻辑\n\n研究团队在肯尼亚基利菲县的农村家庭中，对每位成年家庭成员进行了独立的入户调查，并辅以质性访谈。他们发现，当一个人没有直接参与某个家庭决策时，背后可能存在完全不同的动机结构。\n\n第一种是“委托式有效权力”。一个人选择不参与决策，是因为他确信自己的偏好会自动被满足。这通常发生在家庭中拥有较高地位的成员身上——比如男性户主。他们知道，无论是否出席会议、是否表态，家庭的水源选择、支出分配都会按照他们的意愿进行。不决策，本质上是一种权力溢出：他们不需要耗费时间和认知资源去争取，结果已经内嵌在家庭默认选项中。\n\n第二种是“影响式有效权力”。一个人不直接参与决策，但通过背后游说、情感施压、日常对话等方式影响决策者。这种路径更多见于家庭中地位较低的成员，尤其是女性。她们可能因为社会规范不允许公开表态，或担心直接参与会招致惩罚，转而采取迂回策略。\n\n> **KC评论：** 这两种“不决策”的权力质量完全不同。委托式权力是高位者的特权，几乎零成本；影响式权力是低位者的策略，需要持续投入。报告用“有效权力”这个框架统一了它们，但读者要记住：同一个“不参与”的表\n\n[... middle omitted ...]\n\n继续讨论这份报告未解的问题，并分享完整的原始图表与数据。**\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n不参与决策，也可能是一种权力\n\n**不决策的权力**\n\n**当你不做决定，反而更有影响力**\n\n我们通常认为“参与决策”才代表有话语权，但这份来自某外资投行的研报提出了一个反直觉的观点：**不直接参与决策，有时恰恰是权力最大的体现。**\n\n研报基于肯尼亚Kilifi County农村家庭的混合方法数据，发现传统的决策参与度指标，可能严重低估了某些人的真实影响力——尤其是那些“一家之主”。\n\n**1/ 什么是“有效权力”？**\n\n研报区分了两种“不参与决策”的权力：\n- **代理权力**：你信任某人会做出符合你利益的决定，于是主动选择“放权”，省下时间和精力。\n- **影响/说服权力**：你通过间接方式（如私下沟通、利用社会规范）影响决策者，让结果偏向你的意愿，同时避免直接冲突或社会反弹。\n\n**2/ 谁在“不决策”中获益？**\n\n数据显示，在肯尼亚农村，**丈夫和父亲**往往能通过“代理权力”轻松达成自己的偏好——即使他们不参与日常用水、开支等决策，家里的安排也会自然符合他们的习惯和利益。这种“默认选项”对地位高的人天然有利。\n\n而女性，尤其是**年轻的儿媳和女儿**，则很难享受这种“不决策的福利”。她们往往\n\n[... middle omitted ...]\n\nr by proxy and effective power by influence or persuasion. The paper explores indirect ways of pursuing one’s goals when not directly involved in the decision, using unique mixed methods data \n\n[... middle omitted ...]\n\nble>\n\nNotes: Standard errors in parentheses. \\*\\*\\* p<0.01, \\*\\* p<0.05, \\* p<0.1. All estimations are computed using survey weights to address sampling. There is less than one percent of men who live with their in-laws."
  },
  {
    "id": "R045",
    "title": "世界银行：你的实验可能被“忽视的集群异质性”悄悄削弱了",
    "digest": "[wechat_article.md]\n# 世界银行：你的实验可能被“忽视的集群异质性”悄悄削弱了\n\n一份来自世界银行的研究，可能正在改变你对随机对照实验（RCT）设计的理解。它揭示了一个被多数研究者默认为“可忽略”的变量——集群异质性，实际上可能是决定实验成败的关键。\n\n这份报告的核心判断是：**当集群（cluster）的规模和结果分布在实验设计中未被充分建模时，实验的统计功效可能被严重高估，从而导致研究者在实际中无法检测到真实存在的处理效应。**\n\n换句话说，你的实验可能从一开始就注定“不够有力”，而你甚至没有意识到。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 集群异质性不是噪声，而是实验设计的“隐藏杠杆”\n\n在社会科学和经济学中，随机对照实验通常将个体分组到相互独立的集群中——学校、村庄、企业、街区。研究者假设，只要随机分配发生在集群层面，或者通过控制集群内的相关性（即“聚类效应”），就能得到准确的估计。\n\n但世界银行的这份报告指出，这个假设忽略了两个关键维度：**集群规模的异质性**和**集群结果分布的异质性**。\n\n想象一个场景：200个集群中，前10个集群各有100个单位，后190个集群各有25个单位。如果大集群的平均结果显著高于小集群（例如大集群的居民收入更高、纳税意愿更强），而你只是简单地将所有集群视为同质，那么你的方差估计将严重偏小。\n\n报告通过数值模拟展示了这种偏差的后果：在忽略集群异质性的情况下，研究者计算出在80%统计功效下可检测的最小效应（MDE）为0.29个标准差。但当考虑集群规模异质性时，实际功效降至69%；当进一步考虑分布异质性时，实际功效仅为48%。**这意味着，你有超过一半的概率无法发现真实存在的、大小与预期一致的效应。**\n\n> **KC评论：** 这是一个被低估的“沉默杀手”。很多研究者会检查集群内的相关性（如组内相\n\n[... middle omitted ...]\n\n整解读与原始图表，并与同行讨论这些方法论在自身研究中的应用。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n房东发信催税，邻居也跟着交钱？\n\n邻居效应，有数据\n\n最近读了一份某外资投行的研报，讲的是实验设计里的“溢出效应”。简单说，就是当你给一群人发催税信，没收到信的邻居会不会也跟着乖乖交钱？\n\n结论是：会的。而且效果还挺明显。\n\n1/ 实验怎么设计的？\n- 把居民按“街区”分组\n- 有的街区全部不发信（纯对照组）\n- 有的街区随机选一部分人发信\n- 然后看：收到信的人 vs 没收到信但同住一个街区的邻居，交税行为有啥变化\n\n2/ 关键发现\n- 直接效果：收到信的人，缴税率提高了约5.1个百分点\n- 溢出效果：没收到信但住在高密度发信街区的邻居，缴税率提高了约2.6个百分点\n- 溢出效应约为直接效应的50%，在统计上显著\n\n3/ 为什么要注意“街区大小”？\n研报特别强调了一个坑：如果街区（cluster）大小差异很大，比如有的街区100户，有的只有25户，直接用传统方法算统计功效会严重低估。他们模拟发现，忽略这种异质性，实验可能完全“没力气”检测出真实效果。\n\n4/ 对研究者的实用建议\n- 做实验前，先搞清楚你的“群”大小分布\n- 用他们推导的公式算最小可检测效应，而不是套用标准模板\n- 如果群之间结果分布也不一样\n\n[... middle omitted ...]\n\noring cluster heterogeneity may result in severely underpowered experiments and (ii) the cluster-robust variance estimator may be upward-biased when clusters are heterogeneous. The paper deriv\n\n[... middle omitted ...]\n\n) ]\n$$\n\nwhich completes the proof. □\n\n## D.9 Proof of Theorem 4\n\nThis result follows from the fact that conditions (i) and (ii) imply Assumption 5 and thus under the conditions for Theorem 3, Corollary 1 holds. $\\square$"
  },
  {
    "id": "R046",
    "title": "世界银行：乌克兰难民学生在意大利的学业，比想象中更依赖语言之外的东西",
    "digest": "[wechat_article.md]\n# 世界银行：乌克兰难民学生在意大利的学业，比想象中更依赖语言之外的东西\n\n2022年俄乌冲突爆发后，超过600万乌克兰人被迫流离失所，其中近八成是妇女和儿童。意大利作为欧盟第五大接收国，接纳了约17万乌克兰难民。当这些孩子进入意大利学校时，一个关键问题浮现：他们的教育融入，究竟卡在哪里？\n\n世界银行最新发布的工作论文《Displaced Learners: Early Integration of Ukrainian Refugee Students into Italy‘s Schools》给出了一个既直观又反直觉的答案。这份基于意大利教育部和INVALSI标准化考试数据的实证研究，覆盖了2021-2022至2023-2024学年，追踪了超过8000名乌克兰难民中学生的表现。核心判断是：乌克兰难民学生的学业困境并非单纯的语言障碍，而是语言、心理创伤、出勤率下降和教师期望之间复杂交互的结果。其中，一个被忽视的变量——教师推荐——正在成为决定这些学生长期教育轨迹的隐秘杠杆。\n\n这不是一份简单的“难民需要帮助”的报告。它揭示了在接纳体系中，一个群体的“潜力信号”如何被识别、被放大或被浪费。对于关注人力资本投资、移民政策或欧洲社会结构的读者，这里有一组值得拆解的数据逻辑。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 入学率在改善，但真正的问题是高年级的“隐形流失”\n\n报告数据显示，乌克兰难民学生的入学率在逐步上升，但远未达到理想水平。与意大利本土学生和已在意大利的其他外国学生相比，乌克兰难民在中学阶段的注册比例持续偏低。更值得关注的是结构性断层：在低年级（6-8年级），乌克兰难民学生的比例相对稳定，但进入高中阶段（10年级以上）后，这一比例急剧下降。到13年级（相当于高三），乌克兰难民学生仅占所有学生的0.06%。\n\n这意\n\n[... middle omitted ...]\n\n加入社群，领取完整研报解读与原始图表，一起讨论这些未解问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=“color:#999999;font-size:12px;”>Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n逃难来的乌克兰学生，在意大利学校过得怎么样？\n\n**流离失所的学习者**\n\n**乌克兰难民学生融入意大利学校的真实数据**\n\n---\n\n最近读了一份某外资投行关于乌克兰难民学生融入意大利教育系统的研报，数据很扎实，分享几个核心发现：\n\n**1/ 入学率低，缺勤率高**\n相比意大利本地学生和其他外国学生，乌克兰难民学生的入学率明显更低。即便入学了，缺勤天数也几乎是本地学生的两倍（平均46天 vs 23天）。\n\n**2/ 语言是最大障碍**\n考试成绩方面，乌克兰难民学生在意大利语和英语科目上显著落后，但在数学上表现不错——说明他们之前的教育基础并不差，语言才是卡点。\n\n**3/ 老师反而更看好他们**\n尽管成绩不理想，但意大利老师给乌克兰难民学生推荐“高学术路径”（大学预科方向）的比例，反而高于其他新来的外国学生。研报推测，这可能是因为老师看到了他们的潜力，尤其是数学能力。\n\n**4/ 三大障碍：语言、心理、不确定的未来**\n除了语言，研报还指出心理健康问题和前途未卜的焦虑，是影响这些学生融入的主要因素。\n\n**5/ 意大利做了什么？**\n启动欧盟临时保护指令，简化入学流程，要求学校提供语言支持、心理辅导和跨文化\n\n[... middle omitted ...]\n\nabsenteeism, and lower test scores than other students, particularly in subjects requiring language proficiency. Despite these challenges, teachers often recommend Ukrainian refugee students f\n\n[... middle omitted ...]\n\ners arrived in the country after February 2022 and enrolled in Grades 8 through 13. “Ukr Post Feb 2022 is a variable identifying Ukrainian refugees. The “recommended for high-track” variable is relevant for grade 8 only."
  },
  {
    "id": "R047",
    "title": "世界银行：免费短信反而劝退了求职者",
    "digest": "[wechat_article.md]\n# 世界银行：免费短信反而劝退了求职者\n\n一项在科特迪瓦开展的随机对照实验得出了一个反直觉的结论：当你试图通过短信提醒年轻人某个职业培训项目“完全免费”时，如果这条短信同时发给了他们的家人或联系人，反而会大幅降低报名率。男性报名率下降了42%，女性下降了20%。这个发现挑战了发展援助领域一个根深蒂固的假设——消除价格障碍就能提升参与率。\n\n这份由世界银行研究团队发布的政策研究工作论文，基于国际救援委员会在科特迪瓦实施的PRO-Jeunes青年就业项目，通过对2926名合格申请者的随机分组实验，揭示了信息传递中一个被长期忽视的陷阱：当“免费”成为唯一卖点，它可能被解读为“廉价”或“欺诈”。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 向申请者和联系人同时发送“免费”信息，反而导致报名率骤降\n\n实验设计了两个处理组：第一组只向青年申请者本人发送短信，提醒项目免费；第二组同时向申请者及其预留的联系人发送相同内容。结果显示，只给本人发短信对报名率没有显著影响——既不提升也不降低。但一旦联系人也被纳入信息接收范围，报名率出现断崖式下跌。\n\n男性从对照组的43.8%降至25.2%，女性从38.5%降至30.7%。这个差异在统计上高度显著。更值得关注的是，这种负面效应在男性身上比女性严重得多——男性的报名率降幅比女性多出10.8个百分点。\n\n> **KC评论：** 这组数据揭示了一个关键机制：信息接收者并非孤立决策者。在集体主义文化浓厚的西非社会，家庭和社区的意见对青年选择有决定性影响。当联系人——通常是父母或配偶——收到“免费”信息时，他们缺乏对项目背景的了解，更容易产生怀疑。完整报告中的定性访谈数据进一步印证了这一点：联系人普遍认为“免费”要么意味着低质量，要么是骗局。\n\n![研报图表 2](assets/xhs_card_02\n\n[... middle omitted ...]\n\n盖最新数据图表合集，方便快速把握全球发展政策研究的前沿动态。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n免费短信反而劝退报名\n\n免费≠好？短信翻车了\n\n某外资投行在科特迪瓦做了一个年轻人就业培训项目，发现一个反直觉现象——发短信强调“免费”，反而把报名率拉低了。\n\n1/ 他们给已登记的青年发短信：“快来参加免费培训！”结果：\n- 只发给本人 → 没影响\n- 同时发给本人+紧急联系人 → 报名率暴跌\n\n男生从44%降到25%（降42%），女生从39%降到31%（降20%）。\n\n2/ 为什么？\n定性访谈发现：当“免费”信息传到不太了解项目的联系人那里，对方会怀疑——免费是不是质量差？是不是骗局？信任缺失直接劝退。\n\n3/ 性别差异更有意思\n- 男生无论联系人是谁，都被劝退\n- 女生只有联系人是男性时才被劝退；如果联系人是女性，完全不受影响\n- 妈妈当联系人时，女生报名率没下降\n\n4/ 这说明什么？\n在集体主义文化里（科特迪瓦），年轻人的职业选择受家庭影响很大。光说“免费”不够，还得让关键决策者信任项目质量。\n\n推广策略不能只盯着目标用户，得把“影响决策的人”也考虑进来。\n\n你们觉得，如果换成“知名机构主办+免费”，效果会不同吗？\n\n#学习笔记\n\n[source_mineru.md]\n# Does Free Soun\n\n[... middle omitted ...]\n\ngative effect was smaller for women, and null when their contact was also female. Qualitative findings suggest that distrust among unfamiliar contacts contributed to this decline. The study hi\n\n[... middle omitted ...]\n\nontacts, the impact differed by gender: it decreased enrollment for men but increased enrollment for women. Due to the inconclusive nature of these results, we have chosen to focus on the first type of SMS in this paper."
  },
  {
    "id": "R048",
    "title": "世界银行：社会流动性不能只看“相对”，真正拉动增长的只有一件事",
    "digest": "[wechat_article.md]\n# 世界银行：社会流动性不能只看“相对”，真正拉动增长的只有一件事\n\n社会流动性越高，经济发展就越快——这个直觉听起来无懈可击。但世界银行最新发布的工作论文，用68个国家20年的数据，给出了一个反直觉的结论：不是所有形式的流动性都促进增长，有些甚至与更高收入负相关。\n\n这份由Ivan Torre、Michael Lokshin和James Foster完成的政策研究工作论文，核心判断是：**只有“绝对向上流动”——特别是高等教育层面的向上流动——才与人均GDP有显著正相关；而经济学界常用的“相对流动性”指标，在多数地区与经济发展无关，在拉丁美洲甚至呈现负相关。**\n\n这个结论之所以重要，是因为全球政策制定者和国际组织长期将“提升社会流动性”作为经济改革的核心目标之一。如果选错了衡量标准，政策资源可能被导向一个与增长无关甚至相反的方向。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 你熟悉的“流动性指标”可能正在误导政策判断\n\n学术界和媒体讨论社会流动性时，最常引用两类指标：一是“代际弹性”或“代际相关性”——衡量子女教育在多大程度上由父母教育决定；二是“转型矩阵”——计算不同教育阶层之间的流动概率。前者是相对指标，后者可转化为绝对指标。\n\n世界银行这篇论文的贡献之一，是首次将这些指标放在同一个框架下，检验它们与经济发展的关系。结果令人意外。\n\n在欧洲和中亚地区，相对流动性指标（代际弹性和代际相关性）与人均GDP没有任何统计显著关系。真正与增长挂钩的，是一个更窄的指标：**子女完成高等教育的概率，当他们的父母没有完成高等教育时**。论文将这个指标称为“高等教育向上流动概率”（UMHE）。\n\n换句话说，一个社会是否“公平”并不直接决定它是否繁荣；真正重要的是，这个社会是否能让那些出身教育弱势家庭的孩子，最终拿到大学文凭。\n\n[... middle omitted ...]\n\n沿的动态。如果你对这些未解问题有想法，欢迎加入社群继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n社会流动，真的能拉动经济吗？\n\n社会流动 vs 经济发展\n\n一份覆盖68国、跨度20年的跨国研报发现——\n\n社会流动≠经济增长，关键要看在哪、怎么量。\n\n1️⃣ 流动性的测量方式，决定结论\n- 绝对流动（你比爸妈多读几年书）vs 相对流动（你在同龄人中的教育排名）\n- 研报引入了一个新指标：定向教育流动缺口（oriented mobility gap），衡量“向上”和“向下”流动的幅度\n\n2️⃣ 不同地区，逻辑完全不同\n- 欧洲/中亚：只有“高等教育向上流动”（父母没上过大学但孩子上了）才和人均GDP正相关，相对流动指标不显著\n- 拉美：相对流动越高，收入反而越低；绝对流动越高，收入越高\n- 其他区域：两种模式混合，无明显规律\n\n3️⃣ 为什么相对流动在拉美“反直觉”？\n推测：相对流动提升可能伴随不平等加剧，或反映教育扩张但质量分化，导致整体经济表现被拉低（研报未明确，这里是推演）\n\n4️⃣ 对政策设计的启示\n- 光看“流动性”不够，要拆解是哪个方向的流动、在哪个教育阶段\n- 促进高等教育向弱势群体开放，可能比单纯降低教育代际相关性更有效\n\n社会流动不是万能药，但“让有天赋的孩子不被家庭出身拖累”——这个方向始终\n\n[... middle omitted ...]\n\nh gross domestic product per capita in Europe and Central Asia, but relative mobility indicators are uncorrelated with country income. In Latin America, higher relative mobility is associated wi\n\n[... middle omitted ...]\n\n![](images/7d9e4862cff917286a5d1de94f68ff2f783f5546933d2ddfc807525e88c8dfee.jpg)  \nNote: The figure plots the posterior densities in the Bayesian Model Averaging linear regression for each of the four mobility indices."
  },
  {
    "id": "R049",
    "title": "世界银行：财政规则的效果，关键不在规则本身，而在引入时的条件",
    "digest": "[wechat_article.md]\n# 世界银行：财政规则的效果，关键不在规则本身，而在引入时的条件\n\n一份来自世界银行的最新研究，对全球108个国家近三十年的财政规则实践做了系统检验，得出一个反直觉的判断：财政规则的效果并非随时间线性增强，而是取决于“谁在什么时候、什么状态下引入它”。对于正在讨论新一轮财政框架改革的中国，以及所有面临债务约束的新兴市场，这份报告的结论值得细读。\n\n报告的核心发现是：财政规则的引入确实能改善初级财政余额，十年内平均提升约1%的GDP。但这个平均数字掩盖了巨大的结构性差异。在发达经济体和制度质量高的国家，财政规则的效果会随时间逐渐增强；而在新兴市场和发展中经济体，尤其是制度薄弱的国家，这些效果往往在中期后逐渐消退。\n\n更关键的是，初始条件——规则引入时的经济状况和政治格局——对规则的长期效果有决定性影响。在经济困难时期或政治权力高度集中时引入的财政规则，其中期效果往往大打折扣。这意味着，财政规则的成功，与其说取决于规则本身的条款设计，不如说取决于引入的时机和共识基础。\n\n> **KC评论：** 这份报告最值得关注的点不是“财政规则有没有用”，而是“什么条件下它会失效”。对于投资者和政策研究者来说，理解这些条件，远比记住一个平均效应重要。完整报告中有大量关于制度质量、政治集中度、经济周期不同阶段下效果差异的细分图表，这些才是真正可以用于判断具体国家财政纪律前景的工具。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 财政规则的效果不是线性的，发达经济体和新兴市场走的是两条完全不同的路径\n\n报告使用局部投影法（Local Projections）追踪了财政规则引入后十年内的动态效果。结果显示，在全部样本中，初级财政余额在规则引入后逐步改善，十年累计提升约1%的GDP。但这个平均效应掩盖了发达经济体与新兴市场之间的根本性分化。\n\n对\n\n[... middle omitted ...]\n\n解读与原始图表，继续探讨财政规则在不同环境下的真实效果边界。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n财政纪律不是一劳永逸的\n\n财政规则，有用但分人\n\n关键看初始条件与制度质量\n\n最近读了一篇某外资投行的研报，讲的是财政规则的动态效果。简单来说，他们用了108个国家1984-2012年的数据，发现：\n\n1️⃣ 财政规则确实能改善财政纪律（比如提升初级财政余额），但效果不是一成不变的。\n\n2️⃣ 在发达经济体+制度质量高的国家，效果会随时间增强；但在新兴市场和发展中经济体，尤其是制度较弱的地方，效果会逐渐消退。\n\n3️⃣ 规则引入时的“初始条件”很关键：\n   - 经济困难时期仓促上马的规则，长期效果往往打折扣\n   - 政治权力过于集中时通过的规则，执行效果也容易走弱\n   - 反而是政府与反对党席位相对均衡时，规则更可能被认真执行\n\n4️⃣ 不是制度强就万事大吉，共识和时机同样重要。\n\n一句话总结：好的财政纪律，需要好的时机、好的制度、好的共识，三者缺一不可。\n\n#学习笔记\n\n[source_mineru.md]\n# Dynamic Effects of Fiscal Rules Do Initial Conditions Matter?\n\nAntonio Fatás\n\nBram Gootjes\n\nJose\n\n[... middle omitted ...]\n\nal rules generally improve the primary balance, their effects depend on the time horizon under consideration and the context of adoption. In advanced economies and countries with strong politi\n\n[... middle omitted ...]\n\non, DC.\n\nWyplosz, C. 2013. “Fiscal Rules: Theoretical Issues and Historical Experiences.” In Fiscal Policy After the Financial Crisis, edited by Alesina, A. and F. Giavazzi, 495-525. Chicago: University of Chicago Press."
  },
  {
    "id": "R050",
    "title": "世界银行：卫星+AI正在重塑非洲财富测绘，10%样本量是关键拐点",
    "digest": "[wechat_article.md]\n# 世界银行：卫星+AI正在重塑非洲财富测绘，10%样本量是关键拐点\n\n当国际发展机构还在为2030年“消除贫困”目标倒计时，一个根本性的障碍始终未被攻克：我们无法及时、精确地知道贫困在哪里、变化有多快。传统入户调查成本高昂、频次低、空间颗粒度粗，往往在贫困干预需要落地时，数据已经过时。\n\n世界银行与斯坦福大学联合发布的最新工作论文，给出了一个令人意外的答案。这份基于四个非洲国家超过1200万家庭数据的实证研究证明，视觉Transformer架构配合公开卫星影像，能够在数据稀缺环境中实现高精度、高分辨率的财富测绘。更关键的是，研究找到了一个数据效率的“临界点”——当训练样本覆盖10%的普查区域时，模型性能开始急剧提升，而在此之前，增加每区域内的家庭样本数对精度提升几乎无效。\n\n这意味着，贫困测绘的成本结构正在被根本性改变。过去，精度的瓶颈是“调查多少家庭”；未来，精度的瓶颈可能是“覆盖多少空间单元”。这个判断如果成立，将直接影响国际援助资金分配、政府社保瞄准机制，甚至商业机构在新兴市场的选址策略。\n\n---\n\n> **KC评论：**\n> 这份报告最有价值的地方不在于“AI能预测贫困”这个已经不算新闻的结论，而在于它用大规模、高精度的黄金标准数据，定量回答了“到底需要多少数据、什么类型的数据、什么样的模型”才能让卫星测绘真正可用。这些答案直接关系到这项技术能否从学术论文走向政策落地。\n\n---\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 视觉Transformer首次在贫困测绘中全面超越CNN，精度提升并非渐进而是结构性\n\n此前该领域的主流模型是卷积神经网络。Yeh等人2020年在《自然·通讯》上的开创性工作，就是用CNN结合Landsat影像在非洲五国实现了财富预测。但CNN有一个固有缺陷：它在捕获全局空间依赖关系时能\n\n[... middle omitted ...]\n\n们团队对非洲城市测绘可行性的延伸分析，欢迎加入社群继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n用卫星看非洲家庭财富，准吗？\n\n📡 AI看卫星，测非洲财富\n\n卫星+深度学习，测非洲4国1200万户家庭财富，准确率最高达83%\n\n---\n\n1/ 传统入户调查成本高、周期长、覆盖面小，很多非洲国家几年才做一次普查，数据严重滞后\n\n2/ 这篇研报用 Vision Transformer 模型，直接分析卫星影像，预测家庭资产财富指数（AWI）\n\n3/ 在马拉维、莫桑比克、马达加斯加，模型预测准确率分别达到 83%、70%、62%\n\n4/ 最关键的发现：每个区域只要有10户以上家庭数据，模型表现就和用全量数据几乎一样（差距仅3个百分点）\n\n5/ 这意味着未来做财富普查，可以大幅降低地面采样成本，优先覆盖更多区域而非更多家庭\n\n6/ 模型还能捕捉城市内部的财富差异，甚至预测10年间同一地区的财富变化\n\n7/ 整个国家级的财富地图生成，用8块GPU不到1小时就能完成\n\n---\n\n这种方法的潜力在于：未来贫困监测可以更实时、更精细、更便宜，尤其适合数据稀缺地区\n\n欢迎一起讨论卫星遥感在社经研究中的应用边界～\n\n#学习笔记\n\n[source_mineru.md]\n# Dynamic, High-Resolution We\n\n[... middle omitted ...]\n\nsed deep learning approaches using detailed household census extracts from four African countries to accelerate progress toward comprehensive, fine-scale, and dynamic measurement of asset weal\n\n[... middle omitted ...]\n\nPerez, A., Driscoll, A., Azzari, G., Tang, Z., Lobell, D., Ermon, S., Burke, M., 2020. Using publicly available satellite imagery and deep learning to understand economic well-being in africa. Nature communications 11, 2"
  },
  {
    "id": "R051",
    "title": "世界银行：刚果金国家WASH项目“有设施，无健康”，基础设施改善并未转化为腹泻与发育迟缓的下降",
    "digest": "[wechat_article.md]\n# 世界银行：刚果金国家WASH项目“有设施，无健康”，基础设施改善并未转化为腹泻与发育迟缓的下降\n\n一份来自世界银行的随机对照试验，在刚果民主共和国农村地区评估了一个国家级水、环境卫生与个人卫生项目的长期效果。结论清晰且令人警醒：项目成功建立了村级WASH委员会，显著提升了改善水源和卫生设施的使用率，但这些基础设施层面的进步，并未带来儿童腹泻发病率的降低，也未改善儿童的身长发育指标。这为全球发展领域一个长期悬而未决的问题——基础设施改善与健康结果之间的“最后一公里”鸿沟——提供了来自冲突地区的高质量证据。\n\n这份研究报告发表于2025年1月，基于对刚果金五个省份、121个村庄集群、超过3200户家庭的追踪调查，随访中位时间长达3.6年。其核心发现是：社区主导的WASH项目在“硬件”和“制度”上取得了成功，但在最核心的“健康”目标上失败了。这一结果对全球每年数百亿美元的发展援助资金投向，提出了根本性的拷问。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 项目在“制度”与“设施”上取得了可量化的成功，且效果持续超过三年\n\n报告最坚实的正向结论，在于项目成功构建了可持续的基层治理结构。在干预组村庄，一个活跃的WASH委员会（或仅水委员会）的存在比例，比对照组高出21个百分点。更关键的是，这个制度优势并非短期现象，而是在干预结束三年多后依然可被观测到。\n\n这种制度能力直接转化为了基础设施的改善。干预组家庭报告使用改善水源的比例高出对照组24个百分点，使用改善卫生设施的比例高出18个百分点。村民对水治理的感知也更为积极。这组数据表明，社区主导的发展模式在刚果金这样一个治理薄弱、部分地区受冲突影响的复杂环境中，依然有能力动员社区、建立组织、并完成物理设施的升级。\n\n> **KC评论：** 对发展经济学和公共卫生研究者而言，这个结论\n\n[... middle omitted ...]\n\n入交流，欢迎加入社群，与我们一同追踪这些关键问题的后续进展。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n刚果金全国水卫项目，效果到底怎么样？\n\n**卫生设施升级≠儿童健康改善**\n\n投行研报解析：刚果金国家级水卫项目随机对照试验（3.6年追踪）\n\n---\n\n1/ 项目做了什么？\n- 给村庄提供约2000美元厕所升级+2000美元饮用水升级\n- 建立村级水卫委员会+行为改变宣传\n- 目标是降低腹泻率、改善儿童生长发育\n\n2/ 结果出乎意料：\n- 腹泻率：❌ 无显著下降\n- 儿童身高年龄Z评分：❌ 无改善\n- 水卫设施使用率：✅ 提升24%（饮用水）和18%（厕所）\n- 村级水卫委员会活跃度：✅ 提升21个百分点\n\n3/ 为什么设施改善了，健康没变？\n- 研报推测：从改善设施到降低疾病暴露，中间链条太长\n- 社区干预强度不足，可能无法彻底切断粪口传播路径\n- 冲突地区执行效果打折扣（北基伍省因安全原因未能纳入试验）\n\n4/ 这个试验设计有什么特别？\n- 121个村庄集群随机分配，追踪3.6年\n- 是目前少有的在冲突地区做的长期水卫项目评估\n- 干预组50个集群，对照组71个集群\n\n5/ 核心启示：\n- 硬件投入（厕所+水管）可以持续3年以上\n- 但单独靠社区驱动模式，可能不足以解决儿童营养不良问题\n- 未来需\n\n[... middle omitted ...]\n\nnd sanitation institutions. The program combined (i) funds for latrine and water upgrades, (ii) institutional strengthening activities, and (iii) behavior change campaigns. In 2018, the progra\n\n[... middle omitted ...]\n\nrials, non-pharmacological treatments, herbal interventions, and pragmatic trials. Additional extensions are forthcoming: for those and for up-to-date references relevant to this checklist, see www.consort-statement.org."
  },
  {
    "id": "R052",
    "title": "世界银行：电价上涨1%，高能耗低效企业裁员1.5%",
    "digest": "[wechat_article.md]\n# 世界银行：电价上涨1%，高能耗低效企业裁员1.5%\n\n全球能源转型进程中，一个被反复追问但始终缺乏实证答案的问题是：电价上涨，到底会怎样影响企业——尤其是那些本就脆弱的新兴市场企业？\n\n世界银行最新发布的工作论文给出了一个既反直觉又令人警惕的答案。这份基于24个新兴市场和发展中经济体、超过6万家企业在2019至2023年间表现的研究，没有简单重复“能源价格伤害企业”的常识。它揭示了一个更精细的传导机制：电价上涨对不同企业的冲击，取决于两个关键变量——行业能源密集度，以及企业是否采取了能效措施。\n\n这份报告最核心的判断是：电价上涨1%，在没有采取能效措施的高能耗行业中，企业就业人数将下降约1.5%。与此同时，这些企业的销售额和生产率反而可能上升。这不是统计上的矛盾，而是一个关于企业如何“牺牲劳动力来保护利润”的残酷故事。\n\n---\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 电价上涨的真正赢家是“有效率的企业”，不是“所有的企业”\n\n研究的第一层发现，与直觉相悖：整体来看，电价上涨后，企业的销售额和生产率反而上升。但这一结果在统计上并不稳健——当研究者改变模型设定后，这个“正面效应”消失了。\n\n真正稳健的发现隐藏在交叉项中。报告显示，电价上涨对销售额和生产率的正面影响，几乎完全集中在已经实施了能效措施的企业身上。对于没有采取能效措施的企业，这个正面效应显著减弱，甚至消失。\n\n这意味着什么？电价上涨本身并不会自动激发企业变得更高效。它更像一个筛选器：那些提前布局能效的企业，在成本上升时能够更快调整，甚至利用竞争对手的困境扩大市场份额。而那些没有行动的企业，则被成本压力挤压，无法从价格上涨中获得任何好处。\n\n> **KC评论：** 这份报告揭示了一个被许多政策讨论忽略的事实——能源价格改革的效果，很大程度上取决于企业的“\n\n[... middle omitted ...]\n\n的分类细节感兴趣，欢迎加入社群，与我们一同拆解这些关键问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n电价涨1%，这类公司裁员1.5%\n\n电价涨了，谁最受伤？\n\n某外资投行最新研报，用24个新兴市场国家数据，拆解了电价上涨对不同企业的影响。\n\n1/ 整体来看，电价上涨后，企业反而可能提升销售额和生产率——因为可以把成本转嫁给消费者，或者倒逼技术升级。\n\n2/ 但有一个群体明显受损：高能耗行业里，没有采取节能措施的企业。电价每涨1%，它们的就业规模就减少约1.5%。\n\n3/ 为什么一边增产一边裁员？企业可能通过节能技术替代人力，同时在需求弹性低的市场提价，但成本压力最终还是会压缩用工。\n\n4/ 研报用的是世界银行企业脉搏调查数据（2019-2023），覆盖16个国家近2万条企业记录，按行业能耗强度和企业是否采取节能措施做了交叉分析。\n\n5/ 有趣的是，那些已经做了节能改造的高能耗企业，电价上涨对就业的冲击明显更小。节能措施在这里更像是就业的“缓冲垫”。\n\n所以，电价波动不是均匀地影响所有企业。有没有节能能力，决定了你是“转危为机”还是“被动承压”。\n\n欢迎一起讨论：你所在行业对电价敏感吗？企业有哪些节能实践？\n\n#学习笔记\n\n[source_mineru.md]\n# Energy Prices, Energy \n\n[... middle omitted ...]\n\n(self-reported in the Business Pulse Survey). The findings show that increasing electricity prices by 1 percent reduces employment at firms in energy-intensive industries that did not adopt en\n\n[... middle omitted ...]\n\nS</td></tr></table>\n\nRobust standard errors in parentheses\n\\*\\*\\* p<0.01, \\*\\* p<0.05, \\* p<0.1\nWeighted by country sample size\nControls for size[1], age, wave, and subsector [1] Sales if dependent variable is employment"
  },
  {
    "id": "R053",
    "title": "世界银行：阿根廷房产税揭示的真正性别差距不在逃税，而在高价值资产所有权",
    "digest": "[wechat_article.md]\n# 世界银行：阿根廷房产税揭示的真正性别差距不在逃税，而在高价值资产所有权\n\n世界银行最新发布的工作论文，借助阿根廷一个大型城市的微观税务数据，对房地产所有权和房产税合规中的性别差异进行了迄今最为细致的实证分析。这份报告的核心发现，指向一个反直觉的判断：在逃税行为上，男性和女性几乎没有差别；真正的性别鸿沟，隐藏在财产价值金字塔的顶端。\n\n这份研究覆盖了布宜诺斯艾利斯都会区第三大城市特雷斯德费布雷罗，分析了超过10万处房产、跨越2018至2020年的完整税务记录。对于关注新兴市场资产配置、公共财政和性别经济学的读者而言，这份报告提供的数据颗粒度和因果识别策略，值得深入剖析。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 逃税率高达46%，但男性和女性的合规行为几乎镜像一致\n\n报告首先提供了一个令人警醒的宏观背景：该市的房产税逃税率平均为46%。这一比例意味着每年流失的税收大约相当于该市全年公共安全预算的总和，占市政总支出的8%。\n\n然而，真正值得注意的发现是性别维度的分析。世界银行的研究者利用阿根廷个人税务识别号码的结构特征，成功推断出超过10万处房产所有者的性别信息，并进行了严格的因果识别。结果显示，无论从总体逃税率、按时支付率，还是对税务催缴信函的反应来看，男性和女性的行为模式高度相似。\n\n具体而言，女性拥有的房产逃税率约为46%，男性约为48.5%，差异在统计上微乎其微。在按时支付率上，两者也几乎完全重叠，均随房产价值上升而提高——从最低百分位的约35%升至最高百分位的约60%。报告还利用2020年10月进行的一项大规模随机实验发现，收到个性化催缴信函后，女性的按时支付率提高了4.2个百分点，男性提高了4.7个百分点，差异不显著。\n\n> **KC评论：** 这个发现对政策制定者意味着什么？它挑战了税务领域一个流传已久\n\n[... middle omitted ...]\n\n及过去一周内所有已发布的国际投行与多边机构研究报告摘要合集。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n女性房产持有，高端差距惊人\n\n房产持有真相\n\n高端物业女性占比不足20%\n\n---\n\n**一个被忽视的财富差距：房产持有里的性别鸿沟**\n\n某外资投行最新研报，用阿根廷一城市的税务数据，揭露了一个真实但少被讨论的现象。\n\n**1/ 女性持有房产，中低端持平，高端断崖**\n\n- 在房产价值前40%的区间，女性、男性、共同持有的比例差不多，各占约1/3。\n- 但越往高端走，女性份额直线下降。到了最贵的1%物业里，女性持有不到20%，男性约30%，共同持有超50%。\n- 也就是说，女性拥有的房产更“平价”，这直接影响了后续的税负。\n\n**2/ 逃税率46%，但男女付税习惯几乎一样**\n\n- 整体房产税逃税率46%，女性略低（46% vs 男性48.5%），但差距很小。\n- 按时缴税的比例随房产价值上升而提高——从最低的35%到最高的60%，男女表现一致。\n- 不过，因为女性持有更多低价值房产，而当地税制对低价值房产实际税率更高（固定费用占比大），所以女性实际承担的税率略高。\n\n**3/ 催缴信的效果：男女反应相似，但男性更快**\n\n- 实验显示，收到提醒信后，男女按时缴税的比例都提高了约4-5个百分点（女性+12%\n\n[... middle omitted ...]\n\narities, with women's share dropping to less than $20\\%$ in the top $1\\%$ . Tax compliance increases with property value, with an average evasion rate of $46\\%$ , and men and women are equally\n\n[... middle omitted ...]\n\nf each regression, corresponding to the average of the dependent variable for accounts that did not receive a letter. Standard errors clustered by blocks are reported in parentheses. \\* p<0.10, \\*\\* p<0.05, \\*\\*\\* p<0.01"
  },
  {
    "id": "R054",
    "title": "世界银行：气温每升高0.5度，中小企营收下降12%",
    "digest": "[wechat_article.md]\n# 世界银行：气温每升高0.5度，中小企营收下降12%\n\n气温上升对经济的影响，大多数讨论停留在宏观层面——GDP增速放缓、农业减产、能源需求上升。但世界银行这份覆盖134个国家、近16万家企业的微观研究，给出了一组更具体的数字：在低和低中收入国家，当年度平均气温比历史均值高出0.5摄氏度时，中小企业的营收下降12%。这个数字并不抽象。它意味着，对于一家年营收100万美元的制造企业，一次异常高温年份直接抹去12万美元的收入。更关键的是，这份研究回答了一个长期被忽视的问题：企业到底有没有在适应气候变化？答案令人不安——市场缺陷严重限制了企业的适应能力，尤其是在发展中国家。\n\n这份报告的核心判断可以概括为一句话：气温上升对企业的冲击，不是均匀分布的，而是由企业的规模、所在国的收入水平、以及当地政策环境共同决定的。小企业、新创企业、以及面临融资约束和监管负担的企业，承受了不成比例的压力。而制造业和服务业受到的冲击同样显著，这意味着没有哪个部门可以幸免。\n\n> **KC评论：** 0.5度听起来不大，但报告用的是“偏离历史均值”的概念。对于许多热带国家，基线温度已经在25-30度区间，再往上加0.5度，就进入了劳动生产率和设备效率显著下降的临界区。完整报告中有134个国家各自的历史温度偏差数据，你可以对照自己关注的区域，看看哪些国家已经进入了“危险区间”。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 中小企业是气温上升的最大受害者，大企业反而几乎没有影响\n\n报告最核心的发现来自对温度响应函数的估计。研究团队将每家企业的地理位置与高分辨率卫星气象数据匹配，计算出该企业所在位置在报告财年内的平均温度与1980-2008年历史均值的偏差。然后将这个偏差与企业营收、劳动生产率、投资等指标建立非线性关系。\n\n结果清晰得令人不安：在低和低\n\n[... middle omitted ...]\n\n温度偏差数据，欢迎加入社群，与我们一起持续跟踪这些关键信号。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n温度升高0.5℃，收入降12%\n\n🌡️ 升温冲击\n\n某外资投行最新研报，追踪134个国家、近16万家企业数据，发现：\n\n当年度平均气温比历史均值高0.5℃时，低收入国家的中小企业收入下降12%。\n\n制造业和服务业受影响程度相当，核心原因是劳动生产率和工资下降。\n\n1️⃣ 谁最脆弱？\n- 中小企业 & 初创企业：收入降幅最大\n- 高温敏感行业（食品、交通等）：冲击更明显\n- 生产能力弹性低的企业：恢复更难\n\n2️⃣ 为什么难适应？\n- 融资受限 → 买不起降温设备\n- 监管负担重 → 改造成本高\n- 治安/电力等公共服务差 → 运营雪上加霜\n\n3️⃣ 高收入国家呢？\n- 温度-收入曲线更平缓\n- 企业适应能力明显更强\n- 政策环境更友好是关键变量\n\n有意思的是，同一份数据显示：高历史气温波动地区的企业，反而适应能力更强——被\"训练\"出来了。\n\n欢迎一起讨论，你观察到哪些行业或地区受高温影响更大？\n\n#学习笔记\n\n[source_mineru.md]\nPolicy Research Working Paper\n\n11081\n\n# Firm-Level Climate Change Adaptation Micro\n\n[... middle omitted ...]\n\ns in 134 countries over a 15-year period. Our results show that market imperfections in low- and middle-income countries constrain firms' ability to adapt. Small and medium-size firms in low- \n\n[... middle omitted ...]\n\n108(0.071)</td><td>-0.113(0.036)</td><td>-0.063(0.034)</td><td>-0.166(0.228)</td><td>-0.034(0.041)</td><td>-0.136(0.059)</td><td>0.113(0.096)</td></tr></table>\n\nTable A8: Regression Results using Coefficient of Variation"
  },
  {
    "id": "R055",
    "title": "世界银行：冲突改变的不只是流亡路线，还有对职业尊严的定价",
    "digest": "[wechat_article.md]\n# 世界银行：冲突改变的不只是流亡路线，还有对职业尊严的定价\n\n一份来自世界银行的最新工作论文，以缅甸为实验场，揭示了一个被长期忽视的机制：当暴力冲突升级，高技能潜在移民愿意接受多少降级工作的“补偿溢价”会显著下降。换句话说，安全威胁在改写人力资本市场的定价逻辑。\n\n这份报告的核心判断并不复杂，但含义深远：冲突不仅仅在物理上驱赶人口，它还在心理上降低了移民对“工作是否匹配自身技能”的要求。当生存成为首要目标，职业尊严的溢价就被压缩了。\n\n对于关注全球劳动力流动、东南亚地缘风险，以及移民政策制定的人来说，这份报告提供了一个关键的分析框架：冲突对人力资本的损耗，不仅发生在流亡途中，更早在人们决定离开之前就已经开始了。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 一个被忽略的机制：冲突降低了移民对职业匹配的要价\n\n传统经济学研究移民的职业降级，大多聚焦于移民抵达目的地之后——语言障碍、资质不认、社会网络缺失。但这份报告提出了一个不同的问题：在离开之前，冲突地区的人是不是已经准备好接受更差的工作了？\n\n答案是肯定的。\n\n研究人员设计了一个精巧的实验。他们向缅甸的高技能青年提供两个虚构的海外工作场景：一个与当前工作相似，另一个明显低于其技能水平。受访者需要回答，需要多高的工资溢价才愿意接受这两个工作。两者的溢价之差，就是“补偿性工资差异”——可以理解为一个人为了接受降级工作所要求的额外补偿。补偿越高，说明越不愿意接受降级。\n\n理论预测，所有人都会要求更高的溢价去接受降级工作。但关键发现是：生活在冲突更激烈地区的人，这个额外溢价显著更低。冲突每增加一个单位，补偿性工资差异下降约7-9个百分点。这意味着，冲突地区的人愿意以更低的“价格”出卖自己的技能优势。\n\n> **KC评论：** 这不是说冲突地区的人能力更差或要求更低，而是说他们\n\n[... middle omitted ...]\n\n表合集，既方便喂给AI，也方便人工快速把握全球市场动态。**\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n冲突越激烈，对降级工作越妥协\n\n冲突加剧，职业降级\n\n缅甸青年跨国迁移的新发现\n\n最近读到一篇缅甸青年迁移的研究，很有启发。它讲的是冲突如何影响高技能人才对“降级工作”的态度。\n\n核心发现很直接：\n\n1️⃣ **正常情况**：人们要求更高工资才接受低于自己技能的工作，这被称为“补偿性工资差异”（CWD）。研究里，缅甸青年平均要求多20%的溢价。\n\n2️⃣ **冲突影响**：当家乡冲突加剧，人们愿意接受更低的溢价——也就是对职业降级更“妥协”。冲突每增加一个单位，CWD下降约7-9个百分点。\n\n3️⃣ **谁更受影响**：女性、少数民族、语言弱势群体、收入下降者、缺乏海外关系网的人，效果更显著。冲突让本就脆弱的人更愿意“先走再说”。\n\n4️⃣ **背后的机制**：不是所有人反应一样。住在领土争夺区的人、征兵令颁布后符合条件的年轻人，妥协意愿最强。说明安全焦虑压倒了职业匹配偏好。\n\n简单说：冲突迫使人们用职业前景换安全。这不是理性的职业规划，而是生存决策。\n\n研究者用了一个巧妙的方法：给受访者假设两个工作机会——一个匹配技能，一个低于技能，然后看他们愿意接受多少工资溢价。冲突地区的青年对低技能工作要价更低。\n\n这\n\n[... middle omitted ...]\n\nuced by conflict reduces the additional wage premium that individuals would typically demand for taking on lower skilled work, indicating greater amenability to occupational downgrading. These\n\n[... middle omitted ...]\n\n/td><td>762</td><td>868</td><td>614</td><td>1016</td><td>1098</td><td>454</td></tr></table>\n\nFor all tables: Standard errors clustered at the township level and indicated in parentheses. Controls as indicated in Table 2."
  },
  {
    "id": "R056",
    "title": "世界银行：性别壁垒下降贡献了全球28%的人均GDP增长，但印度是例外",
    "digest": "[wechat_article.md]\n# 世界银行：性别壁垒下降贡献了全球28%的人均GDP增长，但印度是例外\n\n一份来自世界银行的最新研究，对过去五十年间全球劳动力市场的结构性变化提供了一个被严重低估的解释框架。\n\n这份由Gaurav Chiplunkar和Tatjana Kleineberg撰写的政策研究工作论文，基于91个国家超过300个年份的微观数据，系统性地回答了三个问题：女性劳动力参与率上升的驱动力究竟是什么？这种变化如何重塑了全球的产业就业结构？以及，它到底为经济增长贡献了多少？\n\n研究给出的核心判断是：性别壁垒的下降——而非单纯的技术进步或教育扩张——是推动服务业扩张、制造业转型和人均GDP增长的关键变量。平均而言，1970年至2018年间，性别壁垒的下降解释了样本国家28%的人均GDP增长。但这个平均数掩盖了巨大的国别差异：巴西超过50%，加拿Daiwa墨西哥约40%，美国约28%，而印度则是负数——其性别壁垒在五十年间不仅没有改善，反而恶化了。\n\n这个发现的意义在于，它将性别平等从一个社会议题重新定位为一个宏观经济效率议题。对于关注长期增长潜力的决策者和投资者而言，这意味着对劳动力市场结构性红利的评估需要纳入一个此前被低估的维度。\n\n> **KC评论：** 这份报告最有价值的地方不在于“性别平等是好事”这个常识，而在于它给出了一个可量化的因果链条：性别壁垒下降 -> 人才重新配置 -> 产业结构转型 -> 人均产出提升。它把性别问题从社会学范畴拉进了增长核算的框架里。完整报告中包含了对六个主要经济体长达50年的分行业、分职业的详细数据拆解和模型参数，这些图表和假设是理解这一结论可信度的关键。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 女性的就业路径与男性完全不同，这决定了结构性转型的性别不对称\n\n研究首先揭示了一个被宏观数据掩盖的事实：经典\n\n[... middle omitted ...]\n\n给AI进行二次分析，也方便人工快速把握全球市场的结构性动态。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n女性就业怎么影响经济？一篇看懂\n\n女性就业≠经济贡献？\n\n📌 研报核心：性别壁垒下降，是经济转型的重要推手\n\n正文👇\n\n1️⃣ 女性就业的模式，和男性完全不同\n- 经济发展初期，女性离开农业后，不是去工业，而是直接退出劳动力市场\n- 等到服务业扩张，女性才重新进入，主要扎堆服务业\n- 制造业里女性占比始终不高，不管国家多发达\n\n2️⃣ 性别壁垒到底是什么？\n- 两种：一是“性别规范”（社会文化成本），二是“工资歧视”（同工不同酬）\n- 壁垒越高，女性越可能放弃高回报岗位，甚至不工作\n- 这导致人才错配，拖累整体生产力\n\n3️⃣ 壁垒下降，经济受益有多大？\n- 基于6大经济体（印度、印尼、巴西、墨西哥、加拿大、美国）1970-2018年数据\n- 性别壁垒下降，解释了：\n  - 制造业和服务业20%-35%的产出增长\n  - 28%的人均GDP增长（各国差异大：巴西超50%，美国28%，印尼仅10%）\n- 印度是唯一壁垒恶化的国家——如果没恶化，增长本应更高\n\n4️⃣ 关键机制：服务业崛起的新解释\n- 性别壁垒下降，女性大量进入服务业→收入提高→消费更多服务→进一步推动服务业扩张\n- 这为“过早去工业化”（发展中\n\n[... middle omitted ...]\n\nining gender barriers—defined as gender-specific distortions in employment and wages—were a key driver of the observed rise in female labor force participation, expansion of the service sector\n\n[... middle omitted ...]\n\nart-time workers as described above.\n\nEarnings in Home Sector: For each country-year, we set earnings in the Home Sector equal to the measured earnings of women who work in “elementary occupations” in the service sector."
  },
  {
    "id": "R057",
    "title": "世界银行：中小企业不是“怕”税务局，是“不信”税务局",
    "digest": "[wechat_article.md]\n# 世界银行：中小企业不是“怕”税务局，是“不信”税务局\n\n坦桑尼亚税务局把官员派到了中小企业门口，结果怎样？\n\n世界银行一份最新实验给出了一个让税务部门既欣慰又头疼的答案：中小企业纳税人的反应，远比“多派几个人去查”要复杂。\n\n这份题为《对税务局撒谎还是接受帮助？》的工作论文，通过一项在坦桑尼亚119个城区和近郊区域实施的随机对照实验，检验了一个朴素但从未被严格验证的命题——如果税务局官员只是站在旁边，什么都不做，中小企业会不会变得更诚实？\n\n实验的设计本身就是一个创新。世界银行与坦桑尼亚税务局合作，在一轮全国性的中小企业面对面调查中，随机让税务局官员陪同独立调查公司的访员进入一半的样本区域。这些官员不参与提问，不查阅账本，仅仅是“在场”。这是一种介于传统审计威慑与纯粹自愿遵从之间的干预：它既不是惩罚性的，也不是纯粹的宣传教育，而是试图通过增加税务局在社区中的物理可见性，来改变纳税人的心理参照系。\n\n结果令人意外。整体来看，税务局官员的“在场”并没有对中小企业的纳税遵从度和纳税道德产生显著的统计影响。但细分之后，故事变得有趣：在最大城市达累斯萨拉姆，干预带来了短期的纳税额提升；而在其他地区，纳税道德出现了持续性的改善。\n\n> **KC评论：** 这份报告最值得关注的地方不在于它证明“派人有用”或“派人没用”，而在于它揭示了一个被许多税收改革忽略的中介变量——纳税人对执法可信度的感知。达累斯萨拉姆的短期效果，很可能是因为企业主原本就认为税务局“抓不到我”，突然看见官员出现在社区，打破了这种预期。而在其他地区，企业主原本可能连税务局长什么样都不清楚，看见官员反而觉得“这个系统是认真的”。\n\n这引出了一个更深层的追问：为什么整体效果不显著？是干预强度不够，还是中小企业主在调查中“对税务局撒谎”了？\n\n![研报图表 1](assets/xhs_card_01.pn\n\n[... middle omitted ...]\n\n方便人工快速把握市场动态。内容长度约10到40页，每天更新。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n税务官站旁边，小老板会说实话吗？\n\n**真相还是求生欲？**\n\n一场在坦桑尼亚做的实验，税务官陪着调查员去走访中小企业。\n\n结果很有意思：老板们嘴上说的，和实际做的，可能完全两回事。\n\n1️⃣ 实验怎么做的？\n- 世界银行和坦桑尼亚税务局合作，在119个城区/近郊随机抽样\n- 一半地区，税务局官员跟着调查员上门\n- 另一半没有，作为对照组\n- 目的是看“税务官在场”是否影响老板的回答和纳税行为\n\n2️⃣ 核心发现：短期有效，长期存疑\n- 整体来看，税务官在场并没有显著提升纳税合规率\n- 但在首都达累斯萨拉姆，短期内有明显的纳税增加\n- 在非首都地区，老板的“纳税意愿”反而提升了（嘴上说愿意交）\n\n3️⃣ 为什么老板会“说谎”？\n- 一种解释：税务官在场，老板不敢说“我不想交税”，这是求生欲\n- 另一种解释：看到税务官亲自上门，觉得税务局变亲民了，信任感增加\n- 后续追踪调查更倾向于第一种——老板们在“演戏”\n\n4️⃣ 对政策设计的启示\n- 单纯增加税务官“刷脸”，效果有限\n- 如果老板觉得你是来“抓”我的，反而可能适得其反\n- 真正的合规提升，需要让老板觉得“被帮助”而不是“被盯着”\n\n💡 一句话总结：税务官\n\n[... middle omitted ...]\n\n mainland Tanzania. An independent survey firm was accompanied by Tanzania Revenue Authority officers, who observed the interviews in a randomly selected set of urban and peri-urban wards. Thi\n\n[... middle omitted ...]\n\ntd><td></td><td></td></tr><tr><td>Other</td><td>381</td><td>(62.5)</td><td>345</td><td>(57.5)</td><td>0.10135</td></tr><tr><td>Wholesale ~1</td><td>229</td><td>(37.5)</td><td>255</td><td>(42.5)</td><td></td></tr></table>"
  },
  {
    "id": "R058",
    "title": "世界银行：越南增长奇迹背后，穷人正在被“隔离”",
    "digest": "[wechat_article.md]\n# 世界银行：越南增长奇迹背后，穷人正在被“隔离”\n\n越南是全球公认的增长与减贫典范。过去二十年，这个国家的人均收入翻了三倍以上，贫困率从近30%骤降至5%以下。世界银行最新发布的政策研究工作论文，却在这份成绩单上画下了一个醒目的问号：经济增长在加速，但穷人正在被越来越清晰地“隔离”到特定省份。更令人警惕的是，省内不平等已经取代省际差距，成为理解越南社会分化的核心变量。\n\n这份题为“Rapid Economic Growth but Rising Poverty Segregation”的报告，基于2002至2020年十轮越南家庭生活水平调查数据，首次系统性地同时考察了经济增长、不平等与贫困三者之间的动态关系。它的核心判断直指一个政策困境：如果只盯着全国平均数据，你会错过正在发生的结构性撕裂。\n\n**增长没有错，但增长的红利分配机制正在发生变化。** 这份报告揭示的，不是一个失败的故事，而是一个成功故事中正在酝酿的复杂风险。对于任何关注新兴市场发展模式、或者试图理解“增长与公平”这一经典命题的读者来说，越南的案例都是一面值得细看的镜子。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 省内不平等已超过省际差距，且差距还在拉大\n\n大多数关于不平等的讨论，习惯性地聚焦于“区域差距”——沿海与内陆、城市与乡村。但世界银行这份报告提供了一个反直觉的发现：越南真正的分化，不是发生在省份之间，而是发生在省份内部。\n\n报告使用泰尔指数（Theil index）对不平等进行了分解，这种方法的优势在于可以将总不平等精确拆分为“省内”和“省际”两个部分。结果显示，2002年时，省内不平等解释了总不平等的约66%，而到了2020年，这一比例已超过70%。换算成倍数关系：2000年代初，省内不平等约是省际不平等的两倍；到2010年代末，这个差距扩\n\n[... middle omitted ...]\n\n天更新，持续跟踪全球顶级机构对中国和新兴市场的最新判断。**\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n越南经济亮眼，但贫富差距在扩大\n\n**贫富差距拉大**\n\n**20年经济增长，贫困却在某些省份聚集**\n\n最近读了一份世界银行研究团队的研报，关于越南2002-2020年的经济增长与贫富分化。数据非常扎实，分享几个核心发现：\n\n1️⃣ **经济增长确实猛，但分配出了问题**\n- 人均实际支出从347.6万越南盾涨到1425.1万，翻了3倍多\n- 贫困率从29%降到5%以下，成绩亮眼\n- 但省内不平等程度在持续上升，到2020年省内不平等已经是省际不平等的3倍\n\n2️⃣ **贫困正在“聚集”**\n- 虽然整体贫困下降，但贫困人口越来越集中在特定省份\n- 贫困率最高的省份：奠边省（62%）、莱州省（60%）、河江省（56%）\n- 这些省份的共同特点：山区、80%以上农村人口、70%以上少数民族\n\n3️⃣ **经济增长 vs 不平等，互相影响**\n- 经济增长确实有利于减贫，但这个效果会受不平等程度影响\n- 不平等程度越高，对经济增长的负面影响越大\n- 从农业转向非农经济，对减贫和增长都有正面作用\n\n4️⃣ **有意思的发现**\n- 人口密度高、城市化率高的省份增长更快\n- 少数民族比例高的省份，经济增长相对较慢\n\n[... middle omitted ...]\n\nother data sources, this paper finds within-province inequality to be much larger than between-province inequality. Furthermore, this inequality gap has been rising over time. Despite the coun\n\n[... middle omitted ...]\n\nnd predict per capita expenditure for these households. As a result, we have per capita expenditure data for the full sample of 45,000 households, and we use this data to estimate the per capita expenditure of provinces."
  },
  {
    "id": "R059",
    "title": "世界银行：小国正在从贸易中获得远超预期的隐性红利",
    "digest": "[wechat_article.md]\n# 世界银行：小国正在从贸易中获得远超预期的隐性红利\n\n当一个国家的消费者能够买到来自13个不同国家的同一款起泡酒，而不是只有一个选择时，这个国家的经济到底获得了多少好处？\n\n世界银行最新发布的工作论文（Policy Research Working Paper 11072）给出了一个令人意外的量化答案：从1995年到2021年，28个东亚和东非发展中国家因进口商品种类增加而获得的福利收益，平均相当于GDP的5.49%。其中非洲国家平均获益5.47%，亚洲国家（不含不丹）平均获益3.46%。\n\n这个数字意味着什么？它意味着贸易带来的好处，远不止教科书上说的“比较优势”和“规模经济”。在传统贸易理论往往忽视的角落里，一个更隐蔽、更持久的福利源泉正在发挥作用——进口品种的爆炸式增长。\n\n这份报告的核心判断是：**对于小型和转型经济体而言，建立和扩展贸易联系本身就是一种重要的福利来源。** 这个观点在关于全球化和经济一体化的讨论中，常常被低估甚至忽视。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 品种扩张的规模远超预期，传统统计方法严重低估了贸易收益\n\n大多数关于贸易收益的研究，都假设产品种类是固定不变的。这个假设看似无害，实则造成了系统性低估。\n\n看看这组数据就能明白问题的严重性。1995年到2021年间，卢旺达进口的产品种类（按HS-6位码计算）从1608种增加到3731种，翻了2.3倍；柬埔寨从2446种增至4270种；蒙古从2074种增至3639种。更惊人的是品种数的增长——卢旺达的进口品种（同一产品来自不同国家被算作不同品种）增长了超过10倍，蒙古增长了8倍，柬埔寨增长了7倍。\n\n如果按固定篮子计算价格指数，这些新出现的品种根本不会被纳入。而恰恰是这些新品种，构成了福利收益的主要来源。\n\n> **KC评论：** 这\n\n[... middle omitted ...]\n\n方便直接喂给AI模型，也适合人工快速把握市场动态和学术前沿。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n进口品种多了，福利竟然涨了\n\n进口越多越赚？\n\n非洲和亚洲小国，靠“买买买”走出福利增长路\n\n---\n\n**一个反常识的结论：进口品种越多，国家福利越高。**\n\n最近读到一份世界银行工作论文，研究进口品种增长对28个东非和东亚国家的福利影响。数据跨度1995-2021，结论很有意思。\n\n**1/ 福利不是只靠出口**\n\n传统观念总盯着出口创汇，但论文指出，进口品种增加同样能带来真实福利提升。消费者能选到更多样的商品，单位成本下降，这就是福利来源。研究发现，样本国家平均获得5.49% GDP的福利增益，其中非洲国家平均5.47%，亚洲国家（不含不丹）3.46%。\n\n**2/ 小国和转型经济体是最大赢家**\n\n不丹、蒙古、卢旺达、莫桑比克是品种增长最快的国家。以蒙古为例，1995年只从德国进口起泡葡萄酒，2015年已从13个国家进口同一品种。品种翻了8倍，福利直接拉满。法国、德国这种大经济体反而出现负增益——因为它们早已高度一体化，品种增长空间有限。\n\n**3/ 弹性是关键变量**\n\n论文估计了超过10万个替代弹性系数，平均弹性13，中位数4.1。弹性越低，商品差异化越大，品种增长带来的福利空间就越大。这些弹性数\n\n[... middle omitted ...]\n\n level of disaggregation. More than 100,000 elasticities are estimated, and the paper constructs an exact price index to measure the welfare gains from variety growth. The findings show that f\n\n[... middle omitted ...]\n\n:5–38.\n\nSato, K. (1976). The ideal log-change index number. The Review of Economics and Statistics, pages 223–228.\n\nVartia, Y. O. (1976). Ideal log-change index numbers. scandinavian Journal of statistics, pages 121–126."
  },
  {
    "id": "R060",
    "title": "世界银行：刚果金的修路和平红利，三年就过期",
    "digest": "[wechat_article.md]\n# 世界银行：刚果金的修路和平红利，三年就过期\n\n刚果金每年收到数十亿美元的国际援助用于修复公路，目的是通过改善交通来终结冲突。世界银行最新工作论文给出了一个反直觉但极其务实的答案：修路确实能降低暴力事件，但这个“和平红利”平均只能维持三年。\n\n刚果金东部至今活跃着超过120个武装组织，近一半的暴力事件发生在公路附近或公路沿线。国际社会长期将“修路”视为稳定战略的核心工具——公路能降低物流成本、促进经济发展、延伸国家权力。世界银行的这份报告首次用严谨的因果识别方法检验了这个假设，结果令人深思。\n\n报告的核心发现有两个。第一，公路修复完成后，项目所在区域的暴力事件发生率显著下降，降幅约为5至10个百分点，其中针对平民的暴力减少最为明显。第二，也是更重要的发现：这个和平效应是“易腐品”。随着公路在缺乏养护的情况下逐渐退化，暴力事件在三年内反弹至修复前的水平。\n\n这意味着，国际社会投入巨资修建的公路，如果不同时解决“谁来养护”这个根本问题，其安全效益只能维持一个中短期周期。对于所有在脆弱地区从事基础设施投资的政策制定者和投资者，这是一个必须正视的硬约束。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 修路确实能降低暴力，但前提是路是好的\n\n世界银行的这份研究首次系统回答了“修路能否降低冲突”这个长期悬而未决的问题。此前的学术文献对公路与暴力的关系存在完全相反的两种理论：一种认为公路是政府控制力的延伸，能压制叛乱；另一种则认为公路便利了武装分子的后勤，反而加剧暴力。\n\n该报告利用刚果金2003年以来的192个大型城际公路修复项目数据，采用匹配双重差分法识别因果关系。结果显示，公路修复完成后，项目所在区域的暴力事件显著下降。这个效应在处理“针对平民的暴力”时最为显著，降幅可达10个百分点。\n\n> **KC评论：** 报告的因果识别\n\n[... middle omitted ...]\n\n表，以及每日更新的投行研报解读，将在社群中持续分享。\n\n`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n刚读完一份关于刚果（金）道路与冲突的研报，结论很有启发——修路能降低暴力，但“和平红利”会过期。\n\n**修路 ≠ 永久和平**\n\n某外资投行研究了刚果（金）192个道路修复项目，发现：\n1️⃣ 路修好后，当地暴力事件下降5-10个百分点\n2️⃣ 效果最强的是针对平民的暴力减少\n3️⃣ 但！这个和平红利只持续约3年\n\n**为什么？**\n因为刚果（金）的路况退化速度惊人。研报用机器学习分析卫星数据发现：\n- 道路质量每年退化26.5%\n- 3年内，修复过的路平均质量下降60%\n- 路一烂，暴力又回来了\n\n**历史也很关键**\n比利时殖民时期用强征劳工修了13万公里路，1960年独立后民众立刻放弃修路，60%的路几个月就废了。Mobutu时期，他怕修好路让叛军直捣金沙萨，刻意不让东西部连通。\n\n**现实很复杂**\n- 70%的政府军设卡点在国家/省级公路\n- 79%的叛军设卡点在乡村小路\n- 2017-2019年，近一半暴力事件发生在路边或附近\n\n所以修路不是万能药，持续维护才是关键。没有配套的养护机制，和平红利很快就烂在路上了。\n\n#学习笔记\n\n[source_mineru.md]\n# Road Investme\n\n[... middle omitted ...]\n\nad rehabilitation deter violence, which decreases significantly by around 5 to 10 percentage points after the completion of road rehabilitation. However, another significant finding, based on \n\n[... middle omitted ...]\n\n level often led to changes in leadership within the PS, with ministers opting to nominate a confidant to lead the PS.”\n\n5. Democratic Republic Of Congo Emergency Social Action Project P086874 Large Implementation delays"
  },
  {
    "id": "R061",
    "title": "世界银行：印度农村非农就业的真正瓶颈不是机会，是教育与社会身份",
    "digest": "[wechat_article.md]\n# 世界银行：印度农村非农就业的真正瓶颈不是机会，是教育与社会身份\n\n这份来自世界银行的政策研究工作论文，聚焦印度拉贾斯坦邦的农村非农就业问题，但其核心发现对理解所有发展中经济体的农村转型都具有参考意义。报告的核心判断并不复杂：农村非农就业确实能显著提升家庭福利，但通向高质量非农岗位的路径，被教育、性别和社会身份这三重门槛牢牢卡住。机会在增长，但分配机制远未公平。\n\n为什么现在要关注这份报告？因为全球正在经历一轮新的供应链重构与制造业迁移，而印度被普遍视为受益者之一。但农村劳动力能否从低附加值的农业或零工，顺利转入高附加值的正规非农岗位，决定了这一轮红利能否转化为可持续的内需增长。拉贾斯坦邦的案例，恰好提供了一个微观视角，让我们看清这个转化过程卡在了哪里。\n\n报告选取了拉贾斯坦邦作为研究对象，并非偶然。这个邦有60%的土地被塔尔沙漠覆盖，年均降雨量仅为574毫米，远低于印度全国平均的1186毫米。农业的自然瓶颈极其明显，非农就业的转型压力远大于其他邦。报告利用1999年至2015年的多轮全国性调查数据，从个体、家庭、企业三个层面，系统分析了非农就业的决定因素、福利效应以及企业面临的约束。\n\n**世界银行这份报告的真正价值，不在于告诉你非农就业有多重要，而在于它用数据证明了：教育、性别和种姓这三重变量，如何在看似相同的经济环境中，制造出截然不同的就业结果。**\n\n> **KC评论：** 这里需要特别留意报告的一个关键设计——它不仅分析了个体特征（如教育水平）对就业的影响，还检验了个体特征与地区特征（如该地区的银行密度、制造业占比）之间的交互效应。这意味着，同样的教育水平，在基础设施好的地区和差的地区，回报率可能完全不同。这份报告为这种“环境乘数”效应提供了实证支撑。完整报告中的Table 2和Table 3详细展示了这些交互项的具体系数，值得细看。\n\n![研报\n\n[... middle omitted ...]\n\n社群，领取完整研报解读与原始图表，与更多产业决策者一起讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n拉贾斯坦邦农村非农就业，藏着什么秘密？\n\n农村非农就业的真相\n\n教育是钥匙，但性别和种姓是墙\n\n投行研报拆解：印度拉贾斯坦邦的农村非农就业，揭示了发展中国家农村转型的普遍痛点。\n\n1/ 教育是“硬通货”\n完成中学教育的农村劳动力，获得正规非农工作的概率是仅有小学学历者的3倍。教育不仅提升个人竞争力，还激励家庭增加人力资本投入——形成良性循环。\n\n2/ 性别和种姓的隐形天花板\n女性参与非农就业的比例显著低于男性，尤其在高技能服务岗位。社会边缘群体（如表列种姓/表列部落）即使受教育，进入正规非农部门的概率也比其他群体低4个百分点。银行账户的普及对女性就业的正面效应有限，说明金融接入≠就业机会平等。\n\n3/ 非农就业≠脱贫万能药\n有成员从事正规非农工作的家庭，消费水平明显更高。但“临时非农工作”的福利改善效果与农业劳工几乎持平——不是所有非农工作都能拉高生活水平。关键在于：是高技能、稳定的服务业岗位，还是低端、不稳定的零工。\n\n4/ 农村企业卡在哪？\n本地需求不足（市场太小）+ 信贷约束（银行不愿放贷）是两大核心瓶颈。这解释了为什么很多农村微企长不大：不是不想扩张，是既没订单，也借不到钱。\n\n5/ 地域差异巨\n\n[... middle omitted ...]\n\nly predicts participation in non-farm activities, particularly in skilled service sector jobs. However, women and socially marginalized groups face significant barriers in accessing non-farm e\n\n[... middle omitted ...]\n\nforce. Educated is a dummy equaling 1 if the individual has completed secondary or higher education; Bank is a dummy equaling 1 if the individual has a bank account. Standard errors in parentheses, clustered by district."
  },
  {
    "id": "R062",
    "title": "世界银行：埃塞俄比亚的种子革命，玉米赢了，小麦输了",
    "digest": "[wechat_article.md]\n# 世界银行：埃塞俄比亚的种子革命，玉米赢了，小麦输了\n\n埃塞俄比亚的农业改革实验，正在揭示一个被忽视的真相：市场化的种子分销体系，对不同作物的效果完全相反。\n\n世界银行最新发布的工作论文，首次对埃塞俄比亚2011年启动的直接种子营销（DSM）改革进行了严格的量化评估。结论清晰且反直觉：DSM使农民购买玉米种子的比例提高了15个百分点，每公顷玉米种子购买量增加45%，玉米单产提升18%。但对小麦，所有效果在统计上均不显著。\n\n这意味着什么？一个经过精心设计的市场化改革，在同一个国家、同一套制度框架下，对两种主要粮食作物产生了截然不同的结果。这不是政策的成功或失败，而是对“种子市场改革”这一宏大叙事的深度拆解——改革的成效，取决于作物本身的生物学特性。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 改革的核心逻辑：用市场化替代行政化，但只对杂交作物有效\n\n埃塞俄比亚的传统种子分销体系，是一个高度中央集权的系统。国有种子企业负责从品种培育到种子分销的全链条，农户通过行政渠道获取种子。这个系统的核心问题是：需求评估不准确、供应与需求长期错配、种子交付延迟、价格偏高。\n\nDSM改革的逻辑很清晰：允许公共和私营种子生产者直接向农民销售种子，而不是通过国家行政体系。改革者希望借此缩短分销链条、降低交易成本、引入竞争机制，并让种子生产者直接对种子质量负责，从而将公共部门的稀缺资源从种子分销中释放出来，转向品种研发和质量监管。\n\n但世界银行的实证研究揭示了一个关键差异：DSM对玉米的效果显著，对小麦却无效。原因在于两种作物的繁殖生物学特性。玉米主要使用杂交品种，农民每季都需要购买新种子以获取杂交优势带来的产量增益。小麦是自花授粉作物，农民可以留种，对购买新种子的需求天然较低。\n\n> **KC评论：** 这不是政策执行的问题，而是作物经济\n\n[... middle omitted ...]\n\n性分析感兴趣，欢迎加入社群，获取完整研报解读与原始数据图表。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n埃塞俄比亚的种子革命，农民开始自己选种子了\n\n种子直销，农民说了算\n\n埃塞俄比亚的种子系统，以前是典型的“计划分配”——政府定需求、国企生产、层层下发。结果呢？农民要么拿不到种子，要么拿到的时候已经过了播种季。\n\n2011年，埃塞俄比亚搞了一个实验：直接种子营销（DSM）。让种子公司直接卖给农民，跳过政府这条长链条。\n\n1️⃣ 效果有多明显？\n- 买玉米种子的农户比例，提高了15个百分点\n- 每公顷玉米种子购买量，增加了45%\n- 玉米单产，提升了18%\n\n数据来自2012/2016/2019三轮农户追踪调查，用的是双重差分法，比较了DSM试点区和非试点区的变化。\n\n2️⃣ 但小麦就没这么幸运了\n小麦的种子购买量和单产，都没有显著变化。\n\n为什么？核心在作物本身的生物学特性：\n- 玉米杂交种，每年都得买新种子，不然产量掉得厉害\n- 小麦是自花授粉，农民可以自己留种，对买新种子的动力不足\n\n3️⃣ 这个实验告诉我们什么？\n放开市场不是万能药。对玉米这种“必须年年买种子”的作物，DSM效果立竿见影；但对小麦、苔麸这类作物，光靠市场化还不够，需要更精细的政策设计。\n\nDSM还有一个隐藏好处：把农业推广员从卖种子的角\n\n[... middle omitted ...]\n\nia introduced a novel experiment—the direct seed marketing approach—to reduce some of the centralized, state-run attributes of the country's seed market and rationalize the use of public resou\n\n[... middle omitted ...]\n\n3060d65f301a68c0c393f9c7f6933c02.jpg)  \nNote: ATT refers to the Average Treatment Effect on the Treated. DSM refers to Direct Seed Marketing. Source: Authors' estimation based on the ACC 2012, 2016, and 2019 survey data."
  },
  {
    "id": "R063",
    "title": "世界银行：数字化企业更环保、更培训员工，但女性高管更少",
    "digest": "[wechat_article.md]\n# 世界银行：数字化企业更环保、更培训员工，但女性高管更少\n\n数字化和科技，究竟是推动企业伦理进步的引擎，还是加剧了某些结构性不平等？世界银行一份覆盖158个国家、近20万家企业、跨度17年的最新研究，给出了一个令人不安的答案：数字科技企业在环境和社会责任方面表现更优，但在公司治理的性别维度上，却显著落后于传统企业。\n\n这份报告的核心结论，并非简单的“科技企业更道德”或“科技企业更歧视”。它揭示了一个更复杂的三角关系：当企业同时具备“技术密集型”和“数字化运营”两个特征时，其对ESG的不同维度产生了截然相反的影响。这一发现，直接挑战了市场对科技公司“天然向善”的普遍叙事。\n\n对于关注产业趋势、企业治理和投资组合构建的高净值读者和决策者而言，这份报告的真正价值在于：它迫使我们去追问，为什么同一个“科技驱动力”，会在环境和社会层面带来正面效应，却在领导层性别平等方面造成负面结果？这背后是技术本身的属性，还是更深层的社会文化与制度环境在起作用？\n\n本文基于世界银行这份最新工作论文，提炼出五个关键洞察，并尝试回答上述追问。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 科技企业的ESG表现并非铁板一块：环境和社会维度领先，治理维度落后\n\n报告将企业的伦理实践拆解为三个可测量的维度：环境维度（是否监测二氧化碳排放）、社会维度（是否为员工提供正式培训）、治理维度（是否雇佣女性高管）。研究结论清晰且具有分化性。\n\n在环境与社会维度上，数字科技企业（同时具备高技术密集度和数字化运营的企业）展现出更强的积极性。例如，这类企业监测自身碳排放的概率显著高于传统企业，也更倾向于为员工提供正规培训。这表明，技术本身，尤其是数字化工具（如网站、社交媒体），确实为企业在环境管理和人力资本投资方面提供了便利和动力。一个拥有官网和社交媒体的科技企业，更有\n\n[... middle omitted ...]\n\n量投研内容，欢迎加入我们的社群，与志同道合的决策者一同探讨。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n科技公司的ESG，藏着哪些反直觉真相？\n\n科技公司的环保和社会责任，真的更好吗？\n\n某外资投行最新研报，基于2006-2023年全球158个国家19万家企业数据，拆解了科技公司的ESG表现。结论有点反直觉👇\n\n**1/ 环保和社会维度，科技公司确实更积极**\n- 数字化技术企业更倾向于监测CO2排放\n- 也更愿意为员工提供正式培训\n- 技术确实在推动可持续发展目标\n\n**2/ 但治理维度，反而更差**\n- 科技公司聘用女性高管的比例更低\n- 可能与STEM领域长期存在的性别差距有关\n- 技术发展反而加剧了高管层性别不平等\n\n**3/ 文化差异是关键变量**\n- 在“男性气质”强、短期导向的文化中，性别差距更明显\n- 不同文化背景下，科技公司的ESG表现差异显著\n\n**4/ 监管负担的意外影响**\n- 低监管负担下，科技公司更倾向监测碳排放和培训员工\n- 但有趣的是，监管负担减轻反而扩大了性别差距\n- 可能是因为女性在应对复杂监管上投入更多时间\n\n**5/ 司法环境也在起作用**\n- 当法院不被视为商业障碍时，科技公司反而更少聘用女性高管\n- 这个发现值得深入思考\n\n技术不是万能药，它在推动环保和员工培训的同时\n\n[... middle omitted ...]\n\nen of business regulation, and the perception of the courts as an obstacle to business activity. This underscores the importance of the broader society and the quality of the business environm\n\n[... middle omitted ...]\n\nf the courts are perceived as a major/very severe obstacle to the current operations of the firm, and zero if the courts are perceived as either a minor/moderate obstacle or not perceived as an obstacle</td></tr></table>"
  },
  {
    "id": "R064",
    "title": "世界银行：减税吸引不来投资，真正决定企业去留的是这些",
    "digest": "[wechat_article.md]\n# 世界银行：减税吸引不来投资，真正决定企业去留的是这些\n\n当全球各国竞相用税收优惠争夺企业时，世界银行一份基于突尼斯二十万家企业数据的实证研究给出了一个反直觉的结论：减税可能只改变了企业的注册形式，却没有改变经济活动本身。\n\n这份由世界银行经济学家Massimiliano Cali、Giorgio Presidente和Thiago Scot共同完成的工作论文，利用突尼斯2014年取消出口企业免税政策的自然实验，揭示了企业税收激励的真实效果。研究显示，当出口企业的所得税率从0%提升至10%后，新企业进入数量骤降20%，但就业、工资总额和营收等核心经济指标纹丝不动。\n\n这个发现直击全球产业政策的核心矛盾：各国每年花费GDP的1.4%用于企业税收减免，但这些真金白银的激励究竟换来了什么？\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 突尼斯的自然实验揭示了税收激励的边界效应\n\n突尼斯长期实行双轨税制：出口导向的“离岸企业”享受零所得税，而服务内销市场的“在岸企业”需缴纳30%的所得税。这种制度设计本意是吸引外资、促进出口，但到2013年，离岸企业的免税政策每年耗费的财政收入相当于GDP的6.8%。\n\n2014年的税制改革将离岸企业税率从0%提升至10%，同时在岸企业税率从30%降至25%。这一变化并非渐进式的政策调整——此前近十年间，政府曾多次宣布取消免税但反复推迟执行，直到2013年才真正落地。这种突然的政策转向，为研究者提供了一个近乎理想的准自然实验环境。\n\n世界银行团队利用突尼斯全国企业登记数据、社保数据、海关数据和税务申报数据，构建了2009年至2018年近20万家企业面板数据，采用双重差分法比较离岸企业与在岸企业在改革前后的表现差异。\n\n结果显示，改革后四年内，离岸企业数量相对于在岸企业下降了约20%。但更关键的\n\n[... middle omitted ...]\n\n稳健性检验结果或方法论细节感兴趣，欢迎加入社群继续讨论。**\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n企业减税真能拉动经济吗？一个自然实验\n\n企业减税，效果没那么简单\n\n最近读了一篇世界银行关于突尼斯企业税改的研究，结论挺有意思——减税不一定能带来真实的经济增长。\n\n1/ 突尼斯在2014年做了一次大调整：把出口企业的所得税从0%提到10%，同时把普通企业的税率从30%降到25%。这次改革很“干净”，因为其他优惠政策都没变，方便做因果分析。\n\n2/ 结果发现：税改后，新进入出口行业的企业数量下降了20%。但奇怪的是，整体就业、工资总额和收入都没变化。\n\n3/ 为什么？因为新企业本来就很小，经济活动高度集中在少数大企业手里。这些大企业没走，也没减产。减税吸引来的新企业，对整体经济影响微乎其微。\n\n4/ 这个发现和很多其他研究一致：企业做投资决策时，基础设施、劳动力成本、政治稳定性比税率更重要。减税更像锦上添花，不是决定性因素。\n\n5/ 特别值得注意：很多所谓的“减税吸引投资”，可能只是把本来就要发生的经济活动从个体户转到公司名下，并没有创造新价值。\n\n所以，下次看到“减税就能刺激经济”的说法，可以多想想：减掉的税收，真的换来了等价的增长吗？\n\n#学习笔记\n\n[source_mineru.md]\n# The El\n\n[... middle omitted ...]\n\nhe incentives. However, the reduced entry did not translate into any effects on employment, revenue, or the wage bill, as the reform did not impact the activities of incumbent firms, which acc\n\n[... middle omitted ...]\n\ned to firms in the manufacturing sector. Mbar refers to multiples of the largest deviation from parallel trends in the pre-period (i.e. Mbar = 0.8 considers a deviation equals to 80% of the largest pre-period deviation)."
  },
  {
    "id": "R065",
    "title": "世界银行：AI对低收入国家劳动力的冲击，远比你想象的有限",
    "digest": "[wechat_article.md]\n# 世界银行：AI对低收入国家劳动力的冲击，远比你想象的有限\n\n关于人工智能如何重塑劳动力市场的讨论，过去两年几乎全部集中在发达经济体。硅谷的每一次模型发布、华尔街的每一份自动化报告，都在强化一个叙事：白领工作将被颠覆，知识工作者首当其冲。\n\n但世界银行最新发布的工作论文提出了一个被严重忽视的问题：如果全球70%的劳动力生活在低收入和中等收入国家，那么基于美国O*NET职业分类得出的AI暴露度结论，有多大意义？\n\n这份由Gabriel Demombynes、Jorg Langbein和Michael Weber撰写的研究报告，覆盖了25个国家、覆盖35亿人口、约300万工人的微观数据。它的核心判断值得每一位关注全球产业链和新兴市场投资的读者认真对待：**AI对全球劳动力市场的影响，不是均匀分布的。低收入国家的大部分工人，甚至还没有进入AI的“有效暴露”范围。**\n\n这不是一个关于“谁会被替代”的故事，而是一个关于“谁会被真正触及”的结构性真相。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 低收入国家只有12%的工人处于高AI暴露区间，而美国这一比例超过60%\n\n这是报告最直接也最反常识的发现。研究团队使用Felten等人开发的AI职业暴露指数（AIOE），将每个职业的暴露程度标准化为0到100的刻度。结果显示：\n\n- 美国工人的平均暴露值为62。\n- 上中等收入国家为49。\n- 下中等收入国家为44。\n- 低收入国家仅为37。\n\n更直观的数字是：在低收入国家，只有12%的工人处于高暴露区间；而在美国，这个比例超过60%。\n\n这意味着什么？不是低收入国家的工人“更安全”，而是他们的经济结构和职业分布决定了AI的触角尚未延伸过去。大量劳动力集中在农业、低技能服务业和手工制造业——这些领域的任务目前与AI能力重叠度极低。\n\n[... middle omitted ...]\n\n把握全球市场动态。欢迎加入社群，获取完整研报解读与原始图表。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI对不同收入国家的影响，比你想象得更分化\n\nAI对不同国家的影响，远不止“抢工作”这么简单\n\n---\n\n刚读完一篇某外资投行覆盖25国、35亿人的研报，发现一个反直觉的点：AI对低收入国家的冲击，其实比高收入国家**小很多**。\n\n1️⃣ 收入越高，AI暴露度越高\n- 美国工人的AI暴露度均值62（满分100）\n- 中高收入国家49，中低收入国家44\n- 低收入国家只有37\n简单说：你所在国家越发达，你的工作越可能被AI影响\n\n2️⃣ 谁更“危险”？\n- 女性 > 男性（所有收入组都成立）\n- 城市 > 农村\n- 高学历 > 低学历\n- 白领职业 > 蓝领职业\n这些差异在中高收入国家最明显\n\n3️⃣ 低收入国家的“天然屏障”\n- 电力覆盖不足：低收入国家不到一半人口有稳定电力\n- 互联网普及率仅27%\n- 农业和低技能服务业占比高\n这些因素反而让AI的影响“打折扣”\n\n4️⃣ 教育是关键分水岭\n- 70%低收入国家儿童是“学习贫困”（10岁还读不懂简单文字）\n- 只有受过高等教育的工人，AI暴露度才显著上升\n- 中等教育以下，AI暴露度差异不大\n\n5️⃣ 别误读“暴露度”\n研报特意强调：暴露 ≠ 失业\n- 可能\n\n[... middle omitted ...]\n\n The approach advances work by using harmonized microdata at the level of individual workers, which allows for a multivariate analysis of factors associated with exposure. Additionally, unlike\n\n[... middle omitted ...]\n\n8.65***</td><td>26.46***</td><td>24.19***</td></tr><tr><td>(1.26)</td><td>(6.56)</td><td>(30.59)</td><td>(19.99)</td></tr><tr><td>Observations</td><td>123780</td><td>814562</td><td>1269224</td><td>82189</td></tr></table>"
  },
  {
    "id": "R066",
    "title": "世界银行：一场好雨，印度农村非农经济的“乘数”密码",
    "digest": "[wechat_article.md]\n# 世界银行：一场好雨，印度农村非农经济的“乘数”密码\n\n当印度拉贾斯坦邦迎来一场超出正常水平的降雨，会发生什么？最直观的答案是农作物增产。但世界银行一份最新工作论文揭示了一个更深层、也更值得关注的事实：这场好雨的真正经济价值，并不止于田间地头。\n\n它通过一条清晰的传导链条，撬动了农村非农企业的营收和利润，并最终体现在家庭消费的结构性升级上。这份基于拉贾斯坦邦1990年至2015年农业数据、2010年至2016年企业调查以及2014年至2016年家庭消费数据的研报，为我们拆解了天气冲击如何通过农业-非农业经济链条，重塑农村经济的微观图景。\n\n核心判断是：**农业的天气脆弱性，并非农村经济的终点，而是理解其内部“乘数效应”的起点。对于政策制定者和产业投资者而言，忽视农业波动对非农部门的涟漪效应，就是低估了农村市场的真实韧性与风险。**\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 正降雨冲击使农业生产力提升约7%，但灌溉才是真正的“稳定器”\n\n报告首先用数据验证了一个常识性判断：正向的降雨冲击（相对于该地区历史平均水平）能显著提升农业生产力。在拉贾斯坦邦，这一正向冲击带来的农业生产力增长约为7%。这个数字本身并不令人意外，但报告接下来的发现才是关键。\n\n灌溉基础设施的存在，极大地缓冲了这种冲击。在灌溉条件较好的地区，降雨冲击对生产力的影响大幅减弱。这意味着，灌溉不仅是增产手段，更是农村经济系统对抗气候波动的“减震器”。它让农业产出不再严重依赖“老天爷的脸色”，从而为下游的非农经济活动提供了一个更稳定的上游供给和收入预期。\n\n> **KC评论：** 7%的增产是平均值，但真正有意义的是“谁在波动中损失更少”。对于投资于农业科技或农村基础设施的资本而言，这份报告的数据暗示：灌溉覆盖率高的地区，农业产出的可预测性更强，以此为依托\n\n[... middle omitted ...]\n\n投资逻辑，欢迎加入我们的社群，获取每日更新的完整研报解读包。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n下雨天，农村小店生意反而更好？\n\n封面：雨越多，生意越好？\n\n封面副标题：一份研报揭示的农村经济真相\n\n最近读了一份某外资投行的研报，讲的是印度拉贾斯坦邦的天气冲击如何影响农村经济。数据扎实，逻辑清晰，分享几个有意思的发现。\n\n**1. 雨水多，农业产出涨7%**\n研报分析了1990-2015年的数据：正向降雨冲击（雨量高于正常）能让农业生产力提升约7%。但灌溉设施会削弱这个效应——有灌溉的地方，雨水好坏影响就不那么大了。反过来说，干旱对没灌溉的农田打击更重。\n\n**2. 农业好的年份，农村小店收入涨25.7%**\n这可能是最反直觉的点。研报追踪了2010-2016年拉贾斯坦邦的农村非农企业（小商店、修理铺等），发现正向降雨冲击后，这些小店收入平均涨25.7%，增加值（收入减成本）涨30.3%。为什么？因为农民手里有钱了，会去镇上消费，尤其是买非贸易品（比如理发、餐饮、日用品）。农业好，整个村子都跟着好。\n\n**3. 家庭消费：钱先花在“非必需”上**\n2014-2016年的家庭消费数据更有意思：正向降雨冲击后，农村家庭人均月支出增加6%。但仔细一看，增加的几乎全是“奢侈品”支出（比如外出吃饭、娱乐、衣着），\n\n[... middle omitted ...]\n\nhocks increase agricultural productivity by approximately 7 percent compared to negative shocks, with irrigation infrastructure significantly moderating this effect. Second, these weather-indu\n\n[... middle omitted ...]\n\ntd> $R^2$ </td><td>.78</td><td>.78</td><td>.78</td><td>.78</td><td>.78</td><td>.78</td></tr><tr><td>Dep Var Mean</td><td>282.30</td><td>282.30</td><td>282.30</td><td>282.30</td><td>282.30</td><td>282.30</td></tr></table>"
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "Figure 1",
    "context": "■ Widening divergence: The AI supercycle is powering production, exports, and new economy activity, reinforcing the strong leg of the K. At the same time, AI-driven labor displacement risks – while not yet material – are weighing on consumer confidence (see: T"
  },
  {
    "figure_id": "F002",
    "report_id": "R001",
    "label": "Figure 4",
    "context": "■ Computing power: China's intelligent computing tripled in 2025 vs. 2024, according to MIIT data (Figure 4). ■ Equity market: AI-related outperformance has rotated from internet giants to semiconductor manufacturers and materials providers – mirroring the bro"
  },
  {
    "figure_id": "F003",
    "report_id": "R001",
    "label": "Figure 6",
    "context": "AI is now front and center in China's K-shaped economy. The post-Covid recovery has been bifurcated with supply outpacing demand (Figure 6), external demand ahead of domestic demand (Figure 7), and the new economy leading the old. The unfolding AI supercycle i"
  },
  {
    "figure_id": "F004",
    "report_id": "R001",
    "label": "Figure 3",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 3. China's daily token usage hit 140trn in March, up from 0.1trn in early 2024 Figure 4. China's intelligent computing tripled in 2025 vs. 2024 © 2026 Citi Inc. No redistribution with"
  },
  {
    "figure_id": "F005",
    "report_id": "R001",
    "label": "Figure 4",
    "context": "Figure 4. China's intelligent computing tripled in 2025 vs. 2024 © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 5. AI-related outperformance has rotated from internet giants to semiconductor supply chains ©2026 Citi Inc. No redist"
  },
  {
    "figure_id": "F006",
    "report_id": "R001",
    "label": "Figure 5",
    "context": "Figure 5. AI-related outperformance has rotated from internet giants to semiconductor supply chains ©2026 Citi Inc. No redistribution without Citi's written permission. Note: AI models (Tencent, Meituan, Alibaba, Kuaishou, Baidu, SenseTime, Ubtech, Zhipu and M"
  },
  {
    "figure_id": "F007",
    "report_id": "R001",
    "label": "Figure 6",
    "context": "Figure 6. China's post-Covid recovery has been bifurcated with supply outpacing demand © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 7. External demand fills the gap between supply and domestic demand ©2026 Citi Inc. No redistrib"
  },
  {
    "figure_id": "F008",
    "report_id": "R001",
    "label": "Figure 8",
    "context": "Protectionism poses downside risks but is unlikely to derail China's export growth. On the US-China front, risks appear well contained following the IEEPA ruling and the summit between President Trump and President Xi in Beijing, not to mention potentially mor"
  },
  {
    "figure_id": "F009",
    "report_id": "R001",
    "label": "Figure 9",
    "context": "Figure 9. Their growth accelerated to 34.8%YoY in Jan-May 2026, contributing 6.8ppts to headline growth ©2026 Citi Inc. No redistribution without Citi's written permission. Figure 10. AI-related items also logged strong price momentum across the supply chain ©"
  },
  {
    "figure_id": "F010",
    "report_id": "R001",
    "label": "Figure 10",
    "context": "Figure 10. AI-related items also logged strong price momentum across the supply chain ©2026 Citi Inc. No redistribution without Citi's written permission. Figure 11. Global energy transition amplified by the Middle East conflict provides a further tailwind to "
  },
  {
    "figure_id": "F011",
    "report_id": "R001",
    "label": "Figure 12",
    "context": "Production could prove even more resilient than the export cycle. China's own AI-driven demand is pushing high-tech production higher – and could sustain momentum even if export growth were to subside. ■ High-tech IP rose 13.1% YoY Ytd, with the monthly rate a"
  },
  {
    "figure_id": "F012",
    "report_id": "R001",
    "label": "Figure 13",
    "context": "■ AI-related output growth is gaining momentum. IC output expanded 25.4%YoY in Jan-May, while export volumes only grew 8.8%YoY – with 3% of the increase directed towards domestic use. Industrial robot output grew 28.1%YoY, reflecting AI's growing footprint in "
  },
  {
    "figure_id": "F013",
    "report_id": "R001",
    "label": "Figure 15",
    "context": "■ Household risk appetite stays low. Net loan repayments reached RMB631bn in the first five months of 2026 (Figure 15), with deposit reallocation only beginning to stir. Households still hold RMB28.4trn in excess deposits as of May relative to the linear trend"
  },
  {
    "figure_id": "F014",
    "report_id": "R001",
    "label": "Figure 17",
    "context": "The new economy could, at best, generate sporadic gains within the weak leg. In property, Tier-1 city prices have stabilized, while the national index continues to search for a bottom (Figure 17), with AI startups and hardware suppliers concentrated in major c"
  },
  {
    "figure_id": "F015",
    "report_id": "R001",
    "label": "Figure 15",
    "context": "Figure 15. Household risk appetite stays low with net loans repayment of RMB631bn in Jan-May ©2026 Citi Inc. No redistribution without Citi's written permission. Figure 16. Fading trade-in subsidies drove an outright negative reading of retail sales growth in "
  },
  {
    "figure_id": "F016",
    "report_id": "R001",
    "label": "Figure 16",
    "context": "Figure 16. Fading trade-in subsidies drove an outright negative reading of retail sales growth in May ©2026 Citi Inc. No redistribution without Citi's written permission. Figure 17. Home prices in Tier-1 cities have held up, while the national index continues "
  },
  {
    "figure_id": "F017",
    "report_id": "R001",
    "label": "Figure 18",
    "context": "AI-related investment is building its own momentum, while headwinds gather for the rest. With fiscal resources constrained, the significant AI buildout also risks crowding out old economy investment. ■ AI: IT-related FAI stays buoyant even as headline FAI retr"
  },
  {
    "figure_id": "F018",
    "report_id": "R001",
    "label": "Figure 19",
    "context": "■ Other: Headwinds for the rest are mounting, driven by [1] lagging fiscal deployment, [2] uncertainty from the Middle East conflict, [3] anti-involution pressures, and [4] squeezed margin in downstream sectors. Notably, infrastructure investment posted a doub"
  },
  {
    "figure_id": "F019",
    "report_id": "R001",
    "label": "Figure 20",
    "context": "## Reflation: not all boats are lifted The long-awaited PPI reflation has arrived, broader than an energy shock but very uneven. The Middle East conflict drove the initial leg, while broad AI supply chains and construction costs are now extending the recovery "
  },
  {
    "figure_id": "F020",
    "report_id": "R001",
    "label": "Figure 22",
    "context": "The uneven reflation could continue into 26H2E. We maintain our inflation forecasts at 1.0%YoY for CPI and 2.8%YoY for PPI (Figure 22). Peak PPI momentum may now be behind us, with a potential resolution to the Middle East conflict. From here, reflation likely"
  },
  {
    "figure_id": "F021",
    "report_id": "R001",
    "label": "Figure 21",
    "context": "Figure 21. Profit rebounds through April remain concentrated in a handful of sectors ©2026 Citi Inc. No redistribution without Citi's written permission. Figure 22. We maintain our inflation forecasts at 1.0% YoY for CPI and 2.8% YoY for PPI © 2026 Citi Inc. N"
  },
  {
    "figure_id": "F022",
    "report_id": "R001",
    "label": "Figure 22",
    "context": "Figure 22. We maintain our inflation forecasts at 1.0% YoY for CPI and 2.8% YoY for PPI © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 23. Downstream sectors face a difficult squeeze between weak end-demand and rising costs ## Rea"
  },
  {
    "figure_id": "F023",
    "report_id": "R001",
    "label": "Figure 24",
    "context": "■ Monetary policy: We maintain our call for a symbolic 10bps policy rate cut in 26H2E, with risks skewed to the earlier side (Figure 24). Monetary policy is not in the driver's seat during the AI transition – credit growth, once the most powerful leading indic"
  },
  {
    "figure_id": "F024",
    "report_id": "R001",
    "label": "Figure 24",
    "context": "Figure 24. We maintain our call for a symbolic 10bps policy rate cut in 26H2E, with risks skewed to the earlier side ©2026 Citi Inc. No redistribution without Citi's written permission. Figure 25. Special bond issuance has been less aggressive this year ©2026 "
  },
  {
    "figure_id": "F025",
    "report_id": "R001",
    "label": "Figure 25",
    "context": "Figure 25. Special bond issuance has been less aggressive this year ©2026 Citi Inc. No redistribution without Citi's written permission. Figure 26. Fiscal expenditure for budget and government funds combined has contracted for three months Figure 27. A reversa"
  },
  {
    "figure_id": "F026",
    "report_id": "R001",
    "label": "Figure 26",
    "context": "©2026 Citi Inc. No redistribution without Citi's written permission. Figure 26. Fiscal expenditure for budget and government funds combined has contracted for three months Figure 27. A reversal of de facto fiscal austerity could send fiscal impulse higher in 2"
  },
  {
    "figure_id": "F027",
    "report_id": "R001",
    "label": "Figure 29",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. ## Market Implications Equity and rates markets are caught in the great divide of the K-shaped economy. The equity market remains a key consideration in the policy calculus (Figure 29) – and"
  },
  {
    "figure_id": "F028",
    "report_id": "R001",
    "label": "Figure 29",
    "context": "Figure 29. The equity market remains a key consideration in the policy calculus © 2026 Citi Inc. No redistribution without Citi's written permission. Note: Data for 2023 and after extrapolated using NBS second-hand property prices and SHCOMP. Figure 30. Rates "
  },
  {
    "figure_id": "F029",
    "report_id": "R001",
    "label": "Figure 30",
    "context": "Figure 30. Rates are more anchored to old economy dynamics [long-term loan growth?] © 2026 Citi Inc. No redistribution without Citi's written permission. The RMB exchange rate remains the most flexible lever in China's economy and markets. FX settlement – now "
  },
  {
    "figure_id": "F030",
    "report_id": "R001",
    "label": "Figure 31",
    "context": "The RMB exchange rate remains the most flexible lever in China's economy and markets. FX settlement – now at a decade high – is the primary driver of USDCNY, in our view (Figure 31). Exporter's conversion ratio has also recovered to a five-year high (Figure 32"
  },
  {
    "figure_id": "F031",
    "report_id": "R002",
    "label": "FIGURE 1",
    "context": "BARC, UK Ayao Ehara BSJL, Japan FIGURE 1. The weighted average G7 30y yield is approaching 5%, well above the pre-GFC average of about 4% FIGURE 2. Despite attempts to shorten issuance WAM by DMOs, markets would still have to absorb meaningful duration supply "
  },
  {
    "figure_id": "F032",
    "report_id": "R002",
    "label": "FIGURE 3",
    "context": "FIGURE 3. Although 30y yields are back near 2007 levels, the underlying composition is fundamentally different; expected real returns on cash are significantly lower and term premia are playing a larger role FIGURE 4. The expectations components in 30y yields "
  },
  {
    "figure_id": "F033",
    "report_id": "R002",
    "label": "FIGURE 4",
    "context": "FIGURE 4. The expectations components in 30y yields FIGURE 5. 30y term premium, broken into rates and fiscal ## Where to from here? We see two potential drivers of higher 30y yields: a reassessment of the nominal neutral rate and somewhat greater fiscal risk p"
  },
  {
    "figure_id": "F034",
    "report_id": "R002",
    "label": "Figure 7",
    "context": "From a first principal perspective, the saving-investment imbalance is shifting to excess investment, which points to a higher neutral rate for a given estimate of trend growth. Figure 7 shows that hyperscaler investments have risen to about 2.2% of GDP in 202"
  },
  {
    "figure_id": "F035",
    "report_id": "R002",
    "label": "FIGURE 6",
    "context": "All of the above suggests that the market should be discounting a nominal neutral rate near 3.5%, with the risk of skewing towards 4%, rather than 3%. All else equal, this should push long-term yields even higher. FIGURE 6. The unemployment rate has fallen and"
  },
  {
    "figure_id": "F036",
    "report_id": "R002",
    "label": "FIGURE 7",
    "context": "FIGURE 7. Hyperscaler investments are expected to rise to about 3% GDP FIGURE 8. The household saving rate has moved sharply lower FIGURE 9. Model-based estimates of the nominal neutral rate are above the consensus ## Room for fiscal risk premium to move somew"
  },
  {
    "figure_id": "F037",
    "report_id": "R002",
    "label": "FIGURE 8",
    "context": "FIGURE 8. The household saving rate has moved sharply lower FIGURE 9. Model-based estimates of the nominal neutral rate are above the consensus ## Room for fiscal risk premium to move somewhat higher Figure 10 shows that 30y swap spreads are quite sensitive to"
  },
  {
    "figure_id": "F038",
    "report_id": "R002",
    "label": "Figure 12",
    "context": "Figure 12 shows that the effective tariff rate has fallen to 7-8%, from a peak of 12% and the CBO's assumptions of 15%. The CBO assumed that the custom duties would total about \\$4trn in revenues in 2027-36. At a 10% effective rate, they would be about \\$2.7tr"
  },
  {
    "figure_id": "F039",
    "report_id": "R002",
    "label": "FIGURE 10",
    "context": "We believe the Treasury's issuance strategy is likely helping keep the fiscal risk premium in check for now. It has been skewing issuance to the front end. For instance, of the \\$2.1trn in net borrowing needs it faces in 2026, we expect only \\$1.2trn in notes/"
  },
  {
    "figure_id": "F040",
    "report_id": "R002",
    "label": "FIGURE 11",
    "context": "FIGURE 11. A 1pp increase in deficit/GDP ratio tightens 30y swap spreads about 15bp FIGURE 12. The effective tariff rate has slipped well below the CBO's assumption of 15% FIGURE 13. Higher interest rates would also add to budget deficits ## The rate term prem"
  },
  {
    "figure_id": "F041",
    "report_id": "R002",
    "label": "FIGURE 12",
    "context": "FIGURE 12. The effective tariff rate has slipped well below the CBO's assumption of 15% FIGURE 13. Higher interest rates would also add to budget deficits ## The rate term premium is well priced, but risks remain The rate term premium (the swap rate minus the "
  },
  {
    "figure_id": "F042",
    "report_id": "R002",
    "label": "Figure 17",
    "context": "## Warsh's disdain for a bloated Fed balance sheet poses upside risk to the term premium: While the Fed's Treasury holdings as a share of outstanding debt are below pre-GFC levels, the portfolio is much longer. About 40% of Fed's holdings are greater than 10y,"
  },
  {
    "figure_id": "F043",
    "report_id": "R002",
    "label": "FIGURE 14",
    "context": "Bottom line: 30y yields around 4.9% do not look particularly high in a historical context, and scope remains for further repricing through neutral rates and fiscal premia: R\\* estimates are too anchored to the post GFC–pre COVID era and have room to rise. The "
  },
  {
    "figure_id": "F044",
    "report_id": "R002",
    "label": "FIGURE 15",
    "context": "FIGURE 15. Diversification benefits of USTs in a portfolio have come into question with elevated inflation FIGURE 16. Rate vol was higher on average pre-GFC, when the Fed was communicating less FIGURE 17. Warsh's disdain for a bloated Fed balance sheet poses u"
  },
  {
    "figure_id": "F045",
    "report_id": "R002",
    "label": "FIGURE 16",
    "context": "FIGURE 16. Rate vol was higher on average pre-GFC, when the Fed was communicating less FIGURE 17. Warsh's disdain for a bloated Fed balance sheet poses upside risk to the term premium ## UK: Cassandra Complex ## UK long yields: Telling tales versus tittle tatt"
  },
  {
    "figure_id": "F046",
    "report_id": "R002",
    "label": "FIGURE 18",
    "context": "## UK: Cassandra Complex ## UK long yields: Telling tales versus tittle tattle Long-dated gilt yields have resumed the role that they have taken on episodically since 2022: that of the fixed income universe's lightning conductor for wider fiscal discontent. Re"
  },
  {
    "figure_id": "F047",
    "report_id": "R002",
    "label": "FIGURE 18",
    "context": "FIGURE 18. Evolution of 30y yields since October 2024 FIGURE 19. Gilt 30y vs. UST 10y FIGURE 20. Rolling 3m regression beta UST 10y vs 30y The IMF'S latest Fiscal Monitor notes that \"changing intermediation, diminished convenience yield, and increased rollover"
  },
  {
    "figure_id": "F048",
    "report_id": "R002",
    "label": "Figure 18",
    "context": "FIGURE 19. Gilt 30y vs. UST 10y FIGURE 20. Rolling 3m regression beta UST 10y vs 30y The IMF'S latest Fiscal Monitor notes that \"changing intermediation, diminished convenience yield, and increased rollover exposure amplify the global spillover of US Treasury "
  },
  {
    "figure_id": "F049",
    "report_id": "R002",
    "label": "Figure 21",
    "context": "What should investors make of this? Can (or should) the most recent moves be dismissed as just another bout of turbulence and the long end of then gilt curve is playing its usual role as the most visible pain point of global fixed income? It is easy to dismiss"
  },
  {
    "figure_id": "F050",
    "report_id": "R002",
    "label": "Figure 21",
    "context": "Positive (negative) number = deficit increasing (decreasing) Positive (negative) number = debt as % GDP increase (reduction) vs previous year. Japan excluded for comparability reasons. In March 2026 EFO, the OBR reported that the Chancellor had met her own fis"
  },
  {
    "figure_id": "F051",
    "report_id": "R002",
    "label": "Figure 24",
    "context": "\\- Interest paid on reserves held by banks at the BOE. We net out interest paid to gilts in the APF, as this is a intra-public sector payment, since the APF receives coupons on the gilts it holds, while the Bank pays Bank Rate on the reserves it created to fin"
  },
  {
    "figure_id": "F052",
    "report_id": "R002",
    "label": "Figure 24",
    "context": "The bulk of the increase in the overall debt interest bill comes from interest on new conventional supply, reflecting the DMO's sizable medium-term gross financing requirements. By the end of the forecast period, this makes up about £60bn of the overall £137bn"
  },
  {
    "figure_id": "F053",
    "report_id": "R002",
    "label": "Figure 25",
    "context": "In its reorientation of supply away from the long end, the DMO acted ahead other sovereign issuers, as it acknowledged and adapted to the waning of long-end demand and the rise in policy rates that underpinned rising rates. Figure 25 shows that at the end of 2"
  },
  {
    "figure_id": "F054",
    "report_id": "R002",
    "label": "Figure 26",
    "context": "The flip side is that diversification of the issuer base enforces a degree of market discipline on the fiscal authorities. In gilt space, the continued volatility due to political uncertainty should be expected to steepen the curve. But the curve shape looks b"
  },
  {
    "figure_id": "F055",
    "report_id": "R002",
    "label": "Figure 27",
    "context": "compress the spread between the policy rates and intermediate/long forward rates (Figure 28). The curve has been steeper in the past, but from a valuation perspective, it implies that gilt yields should find better support at current levels. The transition to "
  },
  {
    "figure_id": "F056",
    "report_id": "R002",
    "label": "Figure 28",
    "context": "compress the spread between the policy rates and intermediate/long forward rates (Figure 28). The curve has been steeper in the past, but from a valuation perspective, it implies that gilt yields should find better support at current levels. The transition to "
  },
  {
    "figure_id": "F057",
    "report_id": "R002",
    "label": "FIGURE 29",
    "context": "\\- We see the potential for long-end EGB yields to keep drifting higher, but driven largely by global factors. The overall EGB supply burden and fiscal sustainability worries amid flare-up of political uncertainty are key domestic factors, alongside potential "
  },
  {
    "figure_id": "F058",
    "report_id": "R002",
    "label": "FIGURE 29",
    "context": "When we analysed the outlook for long-end EGBs in June 2025, they had endured a bruising first half of the year, against a backdrop of heavy issuance, a dramatic German fiscal pivot, and overall euro area growth resilience. These factors continued to weigh on "
  },
  {
    "figure_id": "F059",
    "report_id": "R002",
    "label": "Figure 31",
    "context": "## Supply: Relentless deluge meets WAM reductions 2026 has had a record deluge of EGB issuance: total supply should reach c.€1.5trn, up c.€100bn y/y. At the issuer level, heavier gross supply is underpinned by Germany, in the context of the aforementioned fisc"
  },
  {
    "figure_id": "F060",
    "report_id": "R002",
    "label": "Figure 31",
    "context": "While total issuance volumes are sharply higher y/y, DMOs have also responded to last year's curve steepening by trimming the weighted average maturity (WAM) of issuance. For H1, we estimate the WAM of EGB supply at c.10y, down c.0.3y on the same period last y"
  },
  {
    "figure_id": "F061",
    "report_id": "R002",
    "label": "FIGURE 33",
    "context": "On the demand side, investors have become increasingly nervous about the effect of the Dutch pension fund transition on the long end of core EGB curves. Under the old defined benefit system, Dutch pension funds were key receivers of long-end swaps and buyers o"
  },
  {
    "figure_id": "F062",
    "report_id": "R002",
    "label": "FIGURE 33",
    "context": "Besides pension funds, euro area insurers have also traditionally been key investors at the long end of EGB curves, in OATs especially. Nonetheless, insurers had been net sellers at the long end for an extended period. In part, this reflected an extended perio"
  },
  {
    "figure_id": "F063",
    "report_id": "R002",
    "label": "Figure 36",
    "context": "Second, geopolitical tensions in the Middle East have intensified concerns that the BoJ is falling behind the curve, thereby pushing inflation risk premia higher. Behind-the-curve concerns due to higher import prices and greater inflation pass-through have als"
  },
  {
    "figure_id": "F064",
    "report_id": "R002",
    "label": "Figure 36",
    "context": "JGB supply-demand conditions have likely aggravated the upward pressure on yields. According to our analysis, when JGB yields break above their recent range, volatility-averse domestic investors tend to be net sellers (Figure 36). That is, as with pension LDI "
  },
  {
    "figure_id": "F065",
    "report_id": "R002",
    "label": "FIGURE 37",
    "context": "FIGURE 37. JGB supply-demand in FY26 FIGURE 38. Relationship between the 10y/30y JGB term premium curve and the super-long JGB interest rate risk position The risk is for greater upside in JGB yields from fiscal policy. Takaichi's \"responsible proactive fiscal"
  },
  {
    "figure_id": "F066",
    "report_id": "R002",
    "label": "Figure 39",
    "context": "The risk is for greater upside in JGB yields from fiscal policy. Takaichi's \"responsible proactive fiscal policy\" continues to pose upside risks to JGB yields, due to its framework, in our view. Specifically, she is seeking to lower the government debt/GDP rat"
  },
  {
    "figure_id": "F067",
    "report_id": "R002",
    "label": "Figure 41",
    "context": "## Japan demand for foreign bonds Despite higher yields, we see little sign of repatriation away from foreign bonds into JGBs. While JGB yields are expected to remain higher in absolute levels and FX-hedged terms (Figure 41), we see limited room for Japanese i"
  },
  {
    "figure_id": "F068",
    "report_id": "R002",
    "label": "Figure 42",
    "context": "The most carry-sensitive life insurers have already sold a significant amount of foreign bonds in 2022-23, during the global duration selloff and rise in FX hedge costs, putting their holdings back to the levels prior to the BoJ's negative rates policy adoptio"
  },
  {
    "figure_id": "F069",
    "report_id": "R002",
    "label": "Figure 43",
    "context": "In terms of geography, Japanese investors have favored US bonds over other regions in recent years, even with less attractive FX-hedged UST yields over EGBs (Figure 43). This may partly reflect FX-unhedged investment based on higher nominal yields and a constr"
  },
  {
    "figure_id": "F070",
    "report_id": "R002",
    "label": "Figure 44",
    "context": "In terms of products, sovereign bond investment has led the overall increase since 2023, but non-sovereign bonds (eg, credit assets) have also had a steady increase until the recent selloff the after geopolitical flare-up in the Middle East this year (Figure 4"
  },
  {
    "figure_id": "F071",
    "report_id": "R003",
    "label": "Figure 1",
    "context": "Figure 1: Global forecast evolution, 2026 % chg saar, annual figures are %4Q/4Q; potential growth estimates in parentheses"
  },
  {
    "figure_id": "F072",
    "report_id": "R003",
    "label": "Figure 2",
    "context": "Figure 2: Global business confidence and employment \\- ... with a recovery in Western Europe. The rebound in business sentiment should be concentrated in Western Europe, which experienced the most significant drop when the Strai"
  },
  {
    "figure_id": "F073",
    "report_id": "R003",
    "label": "Figure 3",
    "context": "Figure 4: Global consumer goods spending and mfg output %3m/3m, saar"
  },
  {
    "figure_id": "F074",
    "report_id": "R003",
    "label": "Figure 3",
    "context": "Figure 5: Global (ex China) employment"
  },
  {
    "figure_id": "F075",
    "report_id": "R003",
    "label": "Figure 4",
    "context": "Figure 5: Global (ex China) employment Figure 6: Energy contribution to global CPI Underpinning this constructive outlook are accommodative financial conditions and supportive fiscal stances. The Fed's model of the financial c"
  },
  {
    "figure_id": "F076",
    "report_id": "R003",
    "label": "Figure 5",
    "context": "Figure 7: US Fed FCI-G and global credit stress"
  },
  {
    "figure_id": "F077",
    "report_id": "R003",
    "label": "Figure 6",
    "context": "Figure 8: US corporate profits and private wages You can't have your cake and eat it too"
  },
  {
    "figure_id": "F078",
    "report_id": "R003",
    "label": "Figure 7",
    "context": "Figure 9: Global (ex China) labor markets Incoming reports highlight building pressure on goods prices. While the recent spike in energy prices is expected to fade, a mix of tech sector bottlenecks, stronger non-tech demand, and"
  },
  {
    "figure_id": "F079",
    "report_id": "R003",
    "label": "Figure 8",
    "context": "Figure 10: Global\\* core goods CPI model"
  },
  {
    "figure_id": "F080",
    "report_id": "R003",
    "label": "Figure 10",
    "context": "Figure 11: Global core CPI Amidst this uncertainty, we continue to take our lead on service price inflation from labor cost dynamics and signals of pricing power. Consistent with the broad easing in labor markets last year, wage"
  },
  {
    "figure_id": "F081",
    "report_id": "R003",
    "label": "Figure 11",
    "context": "Figure 11: Global core CPI Amidst this uncertainty, we continue to take our lead on service price inflation from labor cost dynamics and signals of pricing power. Consistent with the broad easing in labor markets last year, wage"
  },
  {
    "figure_id": "F082",
    "report_id": "R003",
    "label": "Figure 12",
    "context": "Figure 12: Real policy rate %; Nominal rate less 2y trailing core inflation The expansion's resilience and supportive financial conditions are linked to the tolerance of central banks in the face of persistently elevated inflatio"
  },
  {
    "figure_id": "F083",
    "report_id": "R007",
    "label": "FIGURE 2",
    "context": "The earnings growth engine is firing on all cylinders. Activity data remain constructive: industrial production is on the rise, ISM manufacturing PMI is finally back in expansionary territory, and both durable goods and S&P Global manufacturing output point to"
  },
  {
    "figure_id": "F084",
    "report_id": "R007",
    "label": "FIGURE 2",
    "context": "FIGURE 2. The yield-equity correlation is testing the lower bound of its historical range at current levels of the nominal 10y FIGURE 3. The prospect of resumed hikes has not typically derailed equities ahead of the event S&P 500 Performance Around Fed Reversa"
  },
  {
    "figure_id": "F085",
    "report_id": "R007",
    "label": "FIGURE 3",
    "context": "FIGURE 3. The prospect of resumed hikes has not typically derailed equities ahead of the event S&P 500 Performance Around Fed Reversal of Easing In addition, AI capex continues to pose its own risks. While boosting EPS growth now, it also raises execution risk"
  },
  {
    "figure_id": "F086",
    "report_id": "R007",
    "label": "FIGURE 4",
    "context": "In addition, AI capex continues to pose its own risks. While boosting EPS growth now, it also raises execution risks later. We believe \"peak capex\" has been deferred further out, reflecting both persistent supply constraints in training compute capacity and a "
  },
  {
    "figure_id": "F087",
    "report_id": "R007",
    "label": "FIGURE 5",
    "context": "FIGURE 5. ...which is \\~26% above the Street.... FIGURE 6. ...driving operating cash flow pressure that we expect to intensify into 2028... Estimates from BARC' Internet research team. Note that for AMZN, capex is AWS only, while OCF is total AMZN. FIGURE 7. ."
  },
  {
    "figure_id": "F088",
    "report_id": "R007",
    "label": "FIGURE 6",
    "context": "FIGURE 6. ...driving operating cash flow pressure that we expect to intensify into 2028... Estimates from BARC' Internet research team. Note that for AMZN, capex is AWS only, while OCF is total AMZN. FIGURE 7. ...which is not baked into consensus estimates Ove"
  },
  {
    "figure_id": "F089",
    "report_id": "R007",
    "label": "FIGURE 8",
    "context": "We raise our FY26 S&P 500 EPS estimate to \\$337 from \\$321, modestly below the Street's \\$341 and implying 20.8% y/y growth from \\$279 in FY25. Since our previous update, three developments argue for a higher EPS estimate: 1) 1Q26 earnings season was materiall"
  },
  {
    "figure_id": "F090",
    "report_id": "R007",
    "label": "FIGURE 8",
    "context": "Data as of 10 June 2026. FIGURE 8. Q1 beat-and-raise, secular growth and nominal pricing power to underpin FY26 EPS growth FIGURE 9. We estimate \\$337 in FY26 EPS (+21% y/y) vs. the Street at \\$341 FIGURE 10. FY26 Base, Bull and Bear case EPS scenarios Data as"
  },
  {
    "figure_id": "F091",
    "report_id": "R007",
    "label": "FIGURE 8",
    "context": "FIGURE 8. Q1 beat-and-raise, secular growth and nominal pricing power to underpin FY26 EPS growth FIGURE 9. We estimate \\$337 in FY26 EPS (+21% y/y) vs. the Street at \\$341 FIGURE 10. FY26 Base, Bull and Bear case EPS scenarios Data as of 16 Jun 2026 Data as o"
  },
  {
    "figure_id": "F092",
    "report_id": "R007",
    "label": "FIGURE 11",
    "context": "Data as of 10 Jun 2026 We introduce a preliminary FY27 EPS estimate of \\$389, reflecting a modest deceleration in growth. Our framework assumes a partial recovery in consumption on y/y basis, coupled with continued strength in industrial production as the lagg"
  },
  {
    "figure_id": "F093",
    "report_id": "R007",
    "label": "FIGURE 11",
    "context": "FIGURE 11. We estimate \\$389 in FY27 EPS (+15% y/y) vs. Street at \\$398 Data as of 10 Jun 2026. FIGURE 12. FY27 Base, Bull and Bear case EPS scenarios Data as of 10 Jun 2026. FIGURE 13. YTD revisions to full-year EPS are running well ahead of 10-year norms..."
  },
  {
    "figure_id": "F094",
    "report_id": "R007",
    "label": "FIGURE 12",
    "context": "FIGURE 12. FY27 Base, Bull and Bear case EPS scenarios Data as of 10 Jun 2026. FIGURE 13. YTD revisions to full-year EPS are running well ahead of 10-year norms... FIGURE 14. ...with all quarters seeing a pickup in EPS estimates since the end of calendar 1Q26 "
  },
  {
    "figure_id": "F095",
    "report_id": "R007",
    "label": "FIGURE 13",
    "context": "FIGURE 13. YTD revisions to full-year EPS are running well ahead of 10-year norms... FIGURE 14. ...with all quarters seeing a pickup in EPS estimates since the end of calendar 1Q26 Data as of 16 Jun 2026. FIGURE 15. FY26 EPS growth estimates for Tech industrie"
  },
  {
    "figure_id": "F096",
    "report_id": "R007",
    "label": "FIGURE 15",
    "context": "FIGURE 15. FY26 EPS growth estimates for Tech industries, YE25 vs. today Data as of 13 Jun 2026 FIGURE 16. Semis and IT Hardware account for more than half of the + \\$31 added to FY26 Street estimates YTD Data as of 16 Jun 2026 ## Raise 2026 price target to 78"
  },
  {
    "figure_id": "F097",
    "report_id": "R007",
    "label": "FIGURE 17",
    "context": "Our SOTP valuation framework assigns Big Tech a lower baseline multiple than in March (26x vs. 27.5x). We continue to believe the group offers durable earnings growth, but we trim our valuation assumptions to account for uncertainties about the scale, funding "
  },
  {
    "figure_id": "F098",
    "report_id": "R007",
    "label": "FIGURE 17",
    "context": "Applying the blended multiple takes our YE26 S&P 500 target up to 7800 from 7650, 23x our \\$337 FY26 EPS estimate. Our upwardly revised EPS estimate does the heavy lifting, as our valuation assumptions are reduced modestly from our previous update. Our base ca"
  },
  {
    "figure_id": "F099",
    "report_id": "R007",
    "label": "FIGURE 18",
    "context": "FIGURE 18. 2026 Base, Bull and Bear case PT scenarios Data as of 16 Jun 2026. Extending the horizon into 2027, we introduce targets of 8800 in our base case, 9600 in the bull case and 7100 in the bear case, reflecting a more tempered but still constructive lon"
  },
  {
    "figure_id": "F100",
    "report_id": "R007",
    "label": "FIGURE 19",
    "context": "Extending the horizon into 2027, we introduce targets of 8800 in our base case, 9600 in the bull case and 7100 in the bear case, reflecting a more tempered but still constructive long-duration pathway for equities. These estimates are derived by modestly trimm"
  },
  {
    "figure_id": "F101",
    "report_id": "R007",
    "label": "FIGURE 21",
    "context": "Data as of 11 Jun 2026 ## Sector and factor recommendations As a preamble to our sector views, we'd point out that the evolution of the AI narrative continues to reshape the market structure. Correlations within sectors have collapsed to historically low level"
  },
  {
    "figure_id": "F102",
    "report_id": "R007",
    "label": "FIGURE 21",
    "context": "As a preamble to our sector views, we'd point out that the evolution of the AI narrative continues to reshape the market structure. Correlations within sectors have collapsed to historically low levels, reflecting a market increasingly dominated by idiosyncrat"
  },
  {
    "figure_id": "F103",
    "report_id": "R008",
    "label": "Exhibit 1",
    "context": "Exhibit 2: The US 60-Day Waiver May Unlock Up to Around 60mb of Iran Oil on Water Overhang"
  },
  {
    "figure_id": "F104",
    "report_id": "R008",
    "label": "Exhibit 2",
    "context": "Exhibit 2: The US 60-Day Waiver May Unlock Up to Around 60mb of Iran Oil on Water Overhang Exhibit 3: Oil in Transit Has Increased by 68mb Since May 31 as Persian Gulf Flows Are Recovering ## 1) Persian Gulf Exports"
  },
  {
    "figure_id": "F105",
    "report_id": "R008",
    "label": "Exhibit 2",
    "context": "Exhibit 2: The US 60-Day Waiver May Unlock Up to Around 60mb of Iran Oil on Water Overhang Exhibit 3: Oil in Transit Has Increased by 68mb Since May 31 as Persian Gulf Flows Are Recovering ## 1) Persian Gulf Exports Exhibit 4:"
  },
  {
    "figure_id": "F106",
    "report_id": "R008",
    "label": "Exhibit 3",
    "context": "Exhibit 5: We Estimate That 1.2mb/d of Visible OECD SPR Releases Have Reduced the Estimated Hit to Global Commercial Oil Stocks Since March to 4.3mb/d We estimate global oil inventory draws from latest GS oil balance."
  },
  {
    "figure_id": "F107",
    "report_id": "R008",
    "label": "Exhibit 4",
    "context": "Exhibit 5: We Estimate That 1.2mb/d of Visible OECD SPR Releases Have Reduced the Estimated Hit to Global Commercial Oil Stocks Since March to 4.3mb/d We estimate global oil inventory draws from latest GS oil balance. Exhibit 6"
  },
  {
    "figure_id": "F108",
    "report_id": "R008",
    "label": "Exhibit 5",
    "context": "Exhibit 5: We Estimate That 1.2mb/d of Visible OECD SPR Releases Have Reduced the Estimated Hit to Global Commercial Oil Stocks Since March to 4.3mb/d We estimate global oil inventory draws from latest GS oil balance. Exhibit 6"
  },
  {
    "figure_id": "F109",
    "report_id": "R008",
    "label": "Exhibit 6",
    "context": "Exhibit 7: We Estimate That Empty Oil Tankers Within the Strait or Within 5 Days of Navigation Have the Capacity to Load 785mb"
  },
  {
    "figure_id": "F110",
    "report_id": "R008",
    "label": "Exhibit 6",
    "context": "Exhibit 7: We Estimate That Empty Oil Tankers Within the Strait or Within 5 Days of Navigation Have the Capacity to Load 785mb Oil Tanker Capacity on Both Sides of Hormuz"
  },
  {
    "figure_id": "F111",
    "report_id": "R008",
    "label": "Exhibit 7",
    "context": "Exhibit 7: We Estimate That Empty Oil Tankers Within the Strait or Within 5 Days of Navigation Have the Capacity to Load 785mb Oil Tanker Capacity on Both Sides of Hormuz Exhibit 8: 35% of the Hit to Persian Gulf Crude/Condensa"
  },
  {
    "figure_id": "F112",
    "report_id": "R008",
    "label": "Exhibit 7",
    "context": "Exhibit 7: We Estimate That Empty Oil Tankers Within the Strait or Within 5 Days of Navigation Have the Capacity to Load 785mb Oil Tanker Capacity on Both Sides of Hormuz Exhibit 8: 35% of the Hit to Persian Gulf Crude/Condensa"
  },
  {
    "figure_id": "F113",
    "report_id": "R008",
    "label": "Exhibit 8",
    "context": "Exhibit 9: China and Middle East Landed Visible Inventories Have Drawn by 2.2mb/d and 0.8mb/d, Respectively, Over the Last 14 Days"
  },
  {
    "figure_id": "F114",
    "report_id": "R008",
    "label": "Exhibit 9",
    "context": "Exhibit 9: China and Middle East Landed Visible Inventories Have Drawn by 2.2mb/d and 0.8mb/d, Respectively, Over the Last 14 Days Exhibit 10: Global Visible Draws Have Averaged 3.4mb/d Since March 1st Latest observation is today"
  },
  {
    "figure_id": "F115",
    "report_id": "R008",
    "label": "Exhibit 10",
    "context": "Exhibit 11: Global Diesel High-Frequency Visible Stocks Increased to 6% Above Their Year-Ago Levels Last Week, While Gasoline Stocks Continued to Trend Downwards to 4% Below Their Year-Ago Levels ## 3) Refining Exhibit 12: Estimat"
  },
  {
    "figure_id": "F116",
    "report_id": "R008",
    "label": "Exhibit 11",
    "context": "Exhibit 13: Japanese Refineries Runs Are Starting to Pick Up Exhibit 14: The Utilization Rate of US Refineries Is Up 0.3mb/d Year-Over-Year as US Product Margins Remain High"
  },
  {
    "figure_id": "F117",
    "report_id": "R008",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Estimated Chinese Refineries Runs Have Declined by 1.5mb/d From a Year Ago Exhibit 13: Japanese Refineries Runs Are Starting to Pick Up Exhibit 14: The Utilization Rate of US Refineries Is Up 0.3mb/d Year-Over-Year a"
  },
  {
    "figure_id": "F118",
    "report_id": "R008",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Japanese Refineries Runs Are Starting to Pick Up Exhibit 14: The Utilization Rate of US Refineries Is Up 0.3mb/d Year-Over-Year as US Product Margins Remain High ## 4) Energy Prices ## Energy Prices Across Regions Ex"
  },
  {
    "figure_id": "F119",
    "report_id": "R008",
    "label": "Exhibit 15",
    "context": "Exhibit 16: Global Wholesale Refined Products Margins Continue to Normalize, While Retail Margins Remain Near Their All-Time High"
  },
  {
    "figure_id": "F120",
    "report_id": "R008",
    "label": "Exhibit 15",
    "context": "Exhibit 16: Global Wholesale Refined Products Margins Continue to Normalize, While Retail Margins Remain Near Their All-Time High The global wholesale refined product price is a demand-weighted average of wholesale price indices"
  },
  {
    "figure_id": "F121",
    "report_id": "R008",
    "label": "Exhibit 16",
    "context": "Exhibit 17: Dubai Prompt Timespreads Remain in Contango, While the Brent Physical Contract Is Now Trading at a Discount to Its Financial Counterpart"
  },
  {
    "figure_id": "F122",
    "report_id": "R008",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Dubai Prompt Timespreads Remain in Contango, While the Brent Physical Contract Is Now Trading at a Discount to Its Financial Counterpart Percentiles over a sample from 2011 to the present. Percentiles over a sample f"
  },
  {
    "figure_id": "F123",
    "report_id": "R008",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Dubai Prompt Timespreads Remain in Contango, While the Brent Physical Contract Is Now Trading at a Discount to Its Financial Counterpart Percentiles over a sample from 2011 to the present. Percentiles over a sample f"
  },
  {
    "figure_id": "F124",
    "report_id": "R008",
    "label": "Exhibit 18",
    "context": "Exhibit 18: We Estimate That Global Jet Fuel Demand in June Will be 130kb/d Softer Year-Over-Year, or 6% Below Trend Exhibit 19: Our US Gasoline Demand Nowcast Is Now Roughly In Line With Its Year-Ago Seasonal Levels"
  },
  {
    "figure_id": "F125",
    "report_id": "R008",
    "label": "Exhibit 18",
    "context": "Exhibit 18: We Estimate That Global Jet Fuel Demand in June Will be 130kb/d Softer Year-Over-Year, or 6% Below Trend Exhibit 19: Our US Gasoline Demand Nowcast Is Now Roughly In Line With Its Year-Ago Seasonal Levels Exhibit 2"
  },
  {
    "figure_id": "F126",
    "report_id": "R008",
    "label": "Exhibit 18",
    "context": "Exhibit 18: We Estimate That Global Jet Fuel Demand in June Will be 130kb/d Softer Year-Over-Year, or 6% Below Trend Exhibit 19: Our US Gasoline Demand Nowcast Is Now Roughly In Line With Its Year-Ago Seasonal Levels Exhibit 2"
  },
  {
    "figure_id": "F127",
    "report_id": "R008",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Our US Gasoline Demand Nowcast Is Now Roughly In Line With Its Year-Ago Seasonal Levels Exhibit 20: Global Crude/Condensate Imports Are Down 5.9mb/d from 2025 Average Levels, and Refined Products Imports Are Down 4.6"
  },
  {
    "figure_id": "F128",
    "report_id": "R011",
    "label": "Figure 2",
    "context": "This operational shift also brings China's monetary policy architecture into closer convergence with those of the world's leading central banks. The Fed targets the overnight federal funds rate, the ECB anchors policy to the overnight €STR, and the Bank of Jap"
  },
  {
    "figure_id": "F129",
    "report_id": "R011",
    "label": "Figure 2",
    "context": "Fig. 1: New interest rate corridor Fig. 2: Interbank rates and term spread ## Appendix A-1"
  },
  {
    "figure_id": "F130",
    "report_id": "R013",
    "label": "Figure 1",
    "context": "Figure 1: Domestic Cosmetics: Sales by Channel (YoY) Figure 2: Domestic Cosmetics: Shipments by Product (YoY) Figure 3: Sales at Large Retail Stores in China (YoY)"
  },
  {
    "figure_id": "F131",
    "report_id": "R013",
    "label": "Figure 1",
    "context": "Figure 1: Domestic Cosmetics: Sales by Channel (YoY) Figure 2: Domestic Cosmetics: Shipments by Product (YoY) Figure 3: Sales at Large Retail Stores in China (YoY) Figure 4: Cosmetics and Toiletries Imports in China (YoY)"
  },
  {
    "figure_id": "F132",
    "report_id": "R013",
    "label": "Figure 2",
    "context": "Figure 2: Domestic Cosmetics: Shipments by Product (YoY) Figure 3: Sales at Large Retail Stores in China (YoY) Figure 4: Cosmetics and Toiletries Imports in China (YoY)"
  },
  {
    "figure_id": "F133",
    "report_id": "R013",
    "label": "Figure 3",
    "context": "Figure 3: Sales at Large Retail Stores in China (YoY) Figure 4: Cosmetics and Toiletries Imports in China (YoY) Note 1: Shiseido uses IFRS accounting standards, while others use J-GAAP."
  },
  {
    "figure_id": "F134",
    "report_id": "R015",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 2: Based on the spot battery component prices, the cost of sodium-ion battery declined 15% yoy from US\\$66/kWh to US\\$55/kWh now"
  },
  {
    "figure_id": "F135",
    "report_id": "R015",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 3: Solar with Na-ion storage could compete with CCGT at \\$2-5/mmcf gas price Levelized cost of electricity (US\\$/MWh) Solar + Storage (12hrs) vs Combined-Cycle Gas Plant"
  },
  {
    "figure_id": "F136",
    "report_id": "R015",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 4: Assuming every GW of solar and wind capacity is backed up by 1GW of ESS with 10 hours duration, this could amount to a cumulative demand of 100,000GWh"
  },
  {
    "figure_id": "F137",
    "report_id": "R015",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: Assuming every GW of solar and wind capacity is backed up by 1GW of ESS with 10 hours duration, this could amount to a cumulative demand of 100,000GWh By 2030, we think this number could reach close to 10,000GW. Assumi"
  },
  {
    "figure_id": "F138",
    "report_id": "R016",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: Among lower-income households with annual income below JPY 4 mn, new car purchase spending declined across all income brackets, while among higher-income households with annual income above JPY 12.5 mn, new car purchase"
  },
  {
    "figure_id": "F139",
    "report_id": "R016",
    "label": "Exhibit 2",
    "context": "EXHIBIT 2: Car ownership rates declined more sharply among lower-income households, with the gap between households earning below JPY 2.2 mn and above JPY 7.8 mn widening from 27%p in 2019 to 30%p in 2025 EXHIBIT 3: The gap in ca"
  },
  {
    "figure_id": "F140",
    "report_id": "R016",
    "label": "Exhibit 3",
    "context": "EXHIBIT 2: Car ownership rates declined more sharply among lower-income households, with the gap between households earning below JPY 2.2 mn and above JPY 7.8 mn widening from 27%p in 2019 to 30%p in 2025 EXHIBIT 3: The gap in ca"
  },
  {
    "figure_id": "F141",
    "report_id": "R016",
    "label": "Exhibit 4",
    "context": "EXHIBIT 4: Lower-income households tend to show weaker vehicle purchase demand EXHIBIT 5: Higher-income households tend to show stronger vehicle ownership intention ## Some lower-income households are showing signs not only of"
  },
  {
    "figure_id": "F142",
    "report_id": "R016",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: Lower-income households tend to show weaker vehicle purchase demand EXHIBIT 5: Higher-income households tend to show stronger vehicle ownership intention ## Some lower-income households are showing signs not only of"
  },
  {
    "figure_id": "F143",
    "report_id": "R016",
    "label": "Exhibit 6",
    "context": "EXHIBIT 6: K-shaped polarization is also emerging in replacement demand among car-owning households EXHIBIT 7: Some lower-income households are also showing signs of suspending car ownership altogether ## K-shaped polarization"
  },
  {
    "figure_id": "F144",
    "report_id": "R016",
    "label": "Exhibit 7",
    "context": "EXHIBIT 8: The share of low-end vehicles priced below JPY 1 mn increased from 1% in 2017 to 6% in 2025, while the share of high-end vehicles priced above JPY 5 mn also increased from 6% to 15%"
  },
  {
    "figure_id": "F145",
    "report_id": "R016",
    "label": "Exhibit 8",
    "context": "EXHIBIT 8: The share of low-end vehicles priced below JPY 1 mn increased from 1% in 2017 to 6% in 2025, while the share of high-end vehicles priced above JPY 5 mn also increased from 6% to 15% Note: Cars counted were purchased wi"
  },
  {
    "figure_id": "F146",
    "report_id": "R016",
    "label": "Exhibit 9",
    "context": "EXHIBIT 9: As a result of prolonged stagnation in real GDP growth and real wages, real purchasing power per capita has been trending downward EXHIBIT 10: Real monthly disposable income declined 5% from its 2020 peak of JPY 499 th"
  },
  {
    "figure_id": "F147",
    "report_id": "R016",
    "label": "Exhibit 10",
    "context": "EXHIBIT 11: Industry average ASP increased 32%, from JPY 2.9 mn in 2015 to JPY 3.8 mn in 2025"
  },
  {
    "figure_id": "F148",
    "report_id": "R016",
    "label": "Exhibit 11",
    "context": "EXHIBIT 11: Industry average ASP increased 32%, from JPY 2.9 mn in 2015 to JPY 3.8 mn in 2025 Inflation is having a larger impact on car usage and ownership among lower-income households. As of 2025, the ratio of households answer"
  },
  {
    "figure_id": "F149",
    "report_id": "R016",
    "label": "Exhibit 12",
    "context": "EXHIBIT 12: Inflation is having a larger impact on car usage and ownership among lower-income households EXHIBIT 13: The financial burden is heavier for lower-income households ## Younger consumers are becoming less interested n"
  },
  {
    "figure_id": "F150",
    "report_id": "R016",
    "label": "Exhibit 13",
    "context": "EXHIBIT 14: Driver's license ownership rates among young working adults declined from $87\\%$ in 2017 to $67\\%$ in 2025"
  },
  {
    "figure_id": "F151",
    "report_id": "R016",
    "label": "Exhibit 14",
    "context": "EXHIBIT 14: Driver's license ownership rates among young working adults declined from $87\\%$ in 2017 to $67\\%$ in 2025 EXHIBIT 15: Intention to obtain a driver's license among young working adults declined from $32\\%$ in 2017 to $"
  },
  {
    "figure_id": "F152",
    "report_id": "R016",
    "label": "Exhibit 14",
    "context": "EXHIBIT 14: Driver's license ownership rates among young working adults declined from $87\\%$ in 2017 to $67\\%$ in 2025 EXHIBIT 15: Intention to obtain a driver's license among young working adults declined from $32\\%$ in 2017 to $"
  },
  {
    "figure_id": "F153",
    "report_id": "R016",
    "label": "Exhibit 16",
    "context": "EXHIBIT 18: Historically, growth in the number of licensed drivers generally coincided with growth in passenger car ownership"
  },
  {
    "figure_id": "F154",
    "report_id": "R016",
    "label": "Exhibit 18",
    "context": "EXHIBIT 18: Historically, growth in the number of licensed drivers generally coincided with growth in passenger car ownership EXHIBIT 19: If the decline in newly licensed drivers continues, growth in new vehicle demand for individ"
  },
  {
    "figure_id": "F155",
    "report_id": "R016",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 19: If the decline in newly licensed drivers continues, growth in new vehicle demand for individual ownership could also slow ## AUTOMAKERS WITH EXPOSURE TO BOTH LOW-END AND HIGH-END DEMAND ARE BETTER POSITIONED"
  },
  {
    "figure_id": "F156",
    "report_id": "R016",
    "label": "EXHIBIT 18",
    "context": "EXHIBIT 18: Historically, growth in the number of licensed drivers generally coincided with growth in passenger car ownership EXHIBIT 19: If the decline in newly licensed drivers continues, growth in new vehicle demand for individ"
  },
  {
    "figure_id": "F157",
    "report_id": "R016",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 22: Automakers with exposure to both low-end and high-end segments tend to maintain higher profitability under a K-shaped demand environment"
  },
  {
    "figure_id": "F158",
    "report_id": "R016",
    "label": "Exhibit 22",
    "context": "EXHIBIT 22: Automakers with exposure to both low-end and high-end segments tend to maintain higher profitability under a K-shaped demand environment ## SHARED MOBILITY BENEFITS AS CAR OWNERSHIP BECOMES LESS AFFORDABLE ## Shared mo"
  },
  {
    "figure_id": "F159",
    "report_id": "R016",
    "label": "EXHIBIT 24",
    "context": "EXHIBIT 24: Ride sharing is more affordable below 2,000 km annually, while car sharing is more affordable below 7,000 km than car ownership ## Shared mobility shifts value from car ownership to mobility ecosystems Value creation i"
  },
  {
    "figure_id": "F160",
    "report_id": "R016",
    "label": "Exhibit 25",
    "context": "EXHIBIT 25: Autonomy penetration will accelerate the shift of added value downstream in the car value chain ## I. REQUIRED DISCLOSURES"
  },
  {
    "figure_id": "F161",
    "report_id": "R016",
    "label": "Exhibit 25",
    "context": "EXHIBIT 25: Autonomy penetration will accelerate the shift of added value downstream in the car value chain ## I. REQUIRED DISCLOSURES Bernstein is part of a joint venture between SG (SG) and AllianceBernstein, L.P. (AB). Unless"
  },
  {
    "figure_id": "F162",
    "report_id": "R017",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Sub-sector production to demand ratio improved to 108% in Jun from 118% in May Red dots refer to sub-sector production/downstream production (RHS). Exhibit 4: Producer-side inventory days (vs. demand) improved to 53 da"
  },
  {
    "figure_id": "F163",
    "report_id": "R017",
    "label": "Exhibit 3",
    "context": "Exhibit 5: Comp sheet As of Jun 24, 2026 closing."
  },
  {
    "figure_id": "F164",
    "report_id": "R017",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Global Module demand declined by 22% mom and 79% yoy to 29GW in May 2026, sending 5M26 down by 46% yoy to 193GW Global module demand Exhibit 7: China installation in May declined by 91% yoy to 8.7GW, sending 5M26 dow"
  },
  {
    "figure_id": "F165",
    "report_id": "R017",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Global Module demand declined by 22% mom and 79% yoy to 29GW in May 2026, sending 5M26 down by 46% yoy to 193GW Global module demand Exhibit 7: China installation in May declined by 91% yoy to 8.7GW, sending 5M26 dow"
  },
  {
    "figure_id": "F166",
    "report_id": "R017",
    "label": "Exhibit 7",
    "context": "Exhibit 7: China installation in May declined by 91% yoy to 8.7GW, sending 5M26 down by 70% yoy to 60GW China solar module monthly new installations Breakdown of China solar installation by type Quarterly China solar installa"
  },
  {
    "figure_id": "F167",
    "report_id": "R017",
    "label": "Exhibit 7",
    "context": "Exhibit 7: China installation in May declined by 91% yoy to 8.7GW, sending 5M26 down by 70% yoy to 60GW China solar module monthly new installations Breakdown of China solar installation by type Quarterly China solar installa"
  },
  {
    "figure_id": "F168",
    "report_id": "R017",
    "label": "Exhibit 7",
    "context": "Exhibit 7: China installation in May declined by 91% yoy to 8.7GW, sending 5M26 down by 70% yoy to 60GW China solar module monthly new installations Breakdown of China solar installation by type Quarterly China solar installa"
  },
  {
    "figure_id": "F169",
    "report_id": "R018",
    "label": "Exhibit 4",
    "context": "Exhibit 3: Our model indicates that the average effective tax rate of the four large banks was 13% over the past three years, with a projected average of 12% for the next three years, mainly reflecting the tax-exempt effect and the"
  },
  {
    "figure_id": "F170",
    "report_id": "R018",
    "label": "Exhibit 1",
    "context": "Exhibit 4: Based on the recent Lujiazui Forum, our conclusion is that a downward shift in the center of the interest rate corridor and new liquidity support for non-bank financial institutions should help maintain ample interbank l"
  },
  {
    "figure_id": "F171",
    "report_id": "R018",
    "label": "Exhibit 2",
    "context": "Exhibit 4: Based on the recent Lujiazui Forum, our conclusion is that a downward shift in the center of the interest rate corridor and new liquidity support for non-bank financial institutions should help maintain ample interbank l"
  },
  {
    "figure_id": "F172",
    "report_id": "R018",
    "label": "Exhibit 3",
    "context": "Exhibit 5: Covered banks NIM comparison"
  },
  {
    "figure_id": "F173",
    "report_id": "R023",
    "label": "Figure 1",
    "context": "Figure 1: Flows stemming from equity funds globally In \\$bn per month Figure 2: Flows stemming from equity funds that invest in Korea In \\$bn per month. \\- Where retail investors' leverage appears to be retreating is in option"
  },
  {
    "figure_id": "F174",
    "report_id": "R023",
    "label": "Figure 1",
    "context": "Figure 3: Exchange-traded Call Option Buys at Open minus Sells at Open for Customers with less than 10 contracts for options on individual equities In mn contracts. Last obs is for the week ending 19 $^{th}$ June 2026."
  },
  {
    "figure_id": "F175",
    "report_id": "R023",
    "label": "Figure 2",
    "context": "Figure 4: Net Debit balances in NYSE margin accounts The NYSE margin account Net Debit balance is equal to the margin debit balance minus the sum of total credit balances (cash account credit +margin account credit). The blue line"
  },
  {
    "figure_id": "F176",
    "report_id": "R023",
    "label": "Figure 4",
    "context": "Figure 5: Estimated HF Leverage"
  },
  {
    "figure_id": "F177",
    "report_id": "R023",
    "label": "Figure 5",
    "context": "Figure 6: Implied leverage of risk-parity funds Ratio of 3-month rolling volatility of risk-parity funds' returns to the volatility of our risk parity strategy benchmark."
  },
  {
    "figure_id": "F178",
    "report_id": "R023",
    "label": "Figure 6",
    "context": "Figure 6: Implied leverage of risk-parity funds Ratio of 3-month rolling volatility of risk-parity funds' returns to the volatility of our risk parity strategy benchmark. Figure 7: Estimated US bank leverage \\- Similar to hedge"
  },
  {
    "figure_id": "F179",
    "report_id": "R023",
    "label": "Figure 7",
    "context": "Figure 8: Stock of non-financial corporate sector & household debt as % of nominal GDP for Global GDP ex-China Quarterly data, last obs. is Q4 2025."
  },
  {
    "figure_id": "F180",
    "report_id": "R023",
    "label": "Figure 8",
    "context": "Figure 9: Net interest paid as % of non-financial corporate cash flows from operations Till Q1'26 for US and G4 ex US"
  },
  {
    "figure_id": "F181",
    "report_id": "R023",
    "label": "Figure 8",
    "context": "Figure 9: Net interest paid as % of non-financial corporate cash flows from operations Till Q1'26 for US and G4 ex US ## A modest deterioration in the global bond supply-demand balance for 2026 is already priced in by bond marke"
  },
  {
    "figure_id": "F182",
    "report_id": "R023",
    "label": "Figure 10",
    "context": "Figure 10: Net QE by G4 central banks \\- What about retail investors? In our 2026 global bond supply-demand analysis, we used a forecasting model that forecasts current year annual bond flows as a % of AUM as a function of the pr"
  },
  {
    "figure_id": "F183",
    "report_id": "R023",
    "label": "Figure 11",
    "context": "Figure 12: Y/y loan growth for US and Euro area banks In %. Commercial bank loans and leases from the Fed's H.8 release for the US, ECB data on loans to non-financial corporations ex. general government for the Euro area. \\- What a"
  },
  {
    "figure_id": "F184",
    "report_id": "R023",
    "label": "Figure 12",
    "context": "Figure 13: US and Euro area banks' holdings of debt securities as a share of total assets"
  },
  {
    "figure_id": "F185",
    "report_id": "R023",
    "label": "Figure 12",
    "context": "Figure 14: Bond allocation of private defined benefit pension funds in the Milliman 100 index"
  },
  {
    "figure_id": "F186",
    "report_id": "R023",
    "label": "Figure 14",
    "context": "Figure 14: Bond allocation of private defined benefit pension funds in the Milliman 100 index Figure 15: Funded ratios of US private and public defined benefit pension funds \\- Finally, what about bond supply? Taking updated ne"
  },
  {
    "figure_id": "F187",
    "report_id": "R023",
    "label": "Figure 14",
    "context": "Figure 16: Net global bond supply \\$bn per annum."
  },
  {
    "figure_id": "F188",
    "report_id": "R023",
    "label": "Figure 15",
    "context": "Figure 17: Annual change in the balance between global bond supply and demand Change in excess bond supply in \\$bn per annum in the left axis calculated as the difference between changes in global bond supply and changes in global"
  },
  {
    "figure_id": "F189",
    "report_id": "R023",
    "label": "Figure 17",
    "context": "Figure 17: Annual change in the balance between global bond supply and demand Change in excess bond supply in \\$bn per annum in the left axis calculated as the difference between changes in global bond supply and changes in global"
  },
  {
    "figure_id": "F190",
    "report_id": "R026",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Natural Catastrophe Reinsurance Pricing Cycle as portrayed by Hannover – remains favourable Despite recent rate reduction, reinsurance rates remain very rate adequate. Exhibit 2: Reinsurance sector ROEs Exhibit 3: Re"
  },
  {
    "figure_id": "F191",
    "report_id": "R026",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Natural Catastrophe Reinsurance Pricing Cycle as portrayed by Hannover – remains favourable Despite recent rate reduction, reinsurance rates remain very rate adequate. Exhibit 2: Reinsurance sector ROEs Exhibit 3: Re"
  },
  {
    "figure_id": "F192",
    "report_id": "R026",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Reinsurance sector ROEs Exhibit 3: Reinsurance sector capital ## IAG's Commercial business strategy IAG restructured the licensing of its Intermediated business to support a potential reinsurance structure: IAG has t"
  },
  {
    "figure_id": "F193",
    "report_id": "R026",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Tokio Marine 2035 ambitions ## Tokio Marine /Berkshire Partnership: Collaborating on M&A Tokio Marine entered into a strategic partnership with Berkshire Hathaway insurance in March this year. The partnership mirrors I"
  },
  {
    "figure_id": "F194",
    "report_id": "R026",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Tokio Marine Partnership with Berkshire \\*Whole of Account Quota Share arrangement ## Tokio Marine's M&A strategy"
  },
  {
    "figure_id": "F195",
    "report_id": "R026",
    "label": "Exhibit 6",
    "context": "Exhibit 6: M&A framework and track record ## Exhibit 7: M&A scotp in Commerical ## Rate Cycle and M&A Opportunities The current rate cycle has entered the early stage of a softening phase, leading to an increase in M&A activity."
  },
  {
    "figure_id": "F196",
    "report_id": "R026",
    "label": "Exhibit 6",
    "context": "Exhibit 8: Tokio Marine historical M&A since 2008 TM has been buying global insurers for two decades"
  },
  {
    "figure_id": "F197",
    "report_id": "R026",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Sompo investments in Future growth plan ## Investments in Future Growth"
  },
  {
    "figure_id": "F198",
    "report_id": "R026",
    "label": "Exhibit 10",
    "context": "Exhibit 11: A portion of JPY\\$0.7trn (\\~A\\$6.3bn) will be considered for small to medium-sized bolt-on investments to deepen presence in Asian markets and/ or international life insurance companies."
  },
  {
    "figure_id": "F199",
    "report_id": "R026",
    "label": "Exhibit 10",
    "context": "Exhibit 11: A portion of JPY\\$0.7trn (\\~A\\$6.3bn) will be considered for small to medium-sized bolt-on investments to deepen presence in Asian markets and/ or international life insurance companies. W.R. Berkley 15% acquisition was"
  },
  {
    "figure_id": "F200",
    "report_id": "R026",
    "label": "Exhibit 12",
    "context": "Exhibit 13: Personal lines insurers - ROE (12m rolling) (1) Due to accounting standard changes and data collection limitations, Sep-23 data is unavailable. (2) APRA defines personal line insurers as direct insurers that primarily"
  },
  {
    "figure_id": "F201",
    "report_id": "R026",
    "label": "Exhibit 12",
    "context": "Exhibit 15: Commercial Lines GWP growth (12m rolling) and average"
  },
  {
    "figure_id": "F202",
    "report_id": "R026",
    "label": "Exhibit 13",
    "context": "Exhibit 16: Personal Lines GWP growth (12m rolling) and average"
  },
  {
    "figure_id": "F203",
    "report_id": "R026",
    "label": "Exhibit 14",
    "context": "Exhibit 16: Personal Lines GWP growth (12m rolling) and average (1) Due to accounting standard changes and data collection limitations, Sep-23 data is unavailable and has been estimated. (2) We have built up personal lines GWP to"
  },
  {
    "figure_id": "F204",
    "report_id": "R026",
    "label": "Exhibit 15",
    "context": "Exhibit 16: Personal Lines GWP growth (12m rolling) and average (1) Due to accounting standard changes and data collection limitations, Sep-23 data is unavailable and has been estimated. (2) We have built up personal lines GWP to"
  },
  {
    "figure_id": "F205",
    "report_id": "R027",
    "label": "Figure 1",
    "context": "Figure 1: Retail Imbalance in Memory Stocks (\\$B) As of 24 $^{th}$ June Figure 2: Retail Imbalance in MU As of 24 $^{th}$ June Figure 3: Retail Options Volume (Calls and Puts), Communication Services"
  },
  {
    "figure_id": "F206",
    "report_id": "R027",
    "label": "Figure 1",
    "context": "Figure 1: Retail Imbalance in Memory Stocks (\\$B) As of 24 $^{th}$ June Figure 2: Retail Imbalance in MU As of 24 $^{th}$ June Figure 3: Retail Options Volume (Calls and Puts), Communication Services Figure 4: Retail Options"
  },
  {
    "figure_id": "F207",
    "report_id": "R027",
    "label": "Figure 2",
    "context": "Figure 2: Retail Imbalance in MU As of 24 $^{th}$ June Figure 3: Retail Options Volume (Calls and Puts), Communication Services Figure 4: Retail Options Volume (Calls and Puts), Information Technology Figure 5: Retail Imbala"
  },
  {
    "figure_id": "F208",
    "report_id": "R027",
    "label": "Figure 3",
    "context": "Figure 3: Retail Options Volume (Calls and Puts), Communication Services Figure 4: Retail Options Volume (Calls and Puts), Information Technology Figure 5: Retail Imbalance in EWY As of June 24 $^{th}$ Figure 6: Cumulative R"
  },
  {
    "figure_id": "F209",
    "report_id": "R027",
    "label": "Figure 4",
    "context": "Figure 4: Retail Options Volume (Calls and Puts), Information Technology Figure 5: Retail Imbalance in EWY As of June 24 $^{th}$ Figure 6: Cumulative Retail Imbalance in EWY As of June 24 $^{th}$ Figure 7: Retail Imbalance i"
  },
  {
    "figure_id": "F210",
    "report_id": "R027",
    "label": "Figure 5",
    "context": "Figure 5: Retail Imbalance in EWY As of June 24 $^{th}$ Figure 6: Cumulative Retail Imbalance in EWY As of June 24 $^{th}$ Figure 7: Retail Imbalance in KORU As of June 24 $^{th}$ Figure 9: Communication ETFs Imbalance at it"
  },
  {
    "figure_id": "F211",
    "report_id": "R027",
    "label": "Figure 6",
    "context": "Figure 6: Cumulative Retail Imbalance in EWY As of June 24 $^{th}$ Figure 7: Retail Imbalance in KORU As of June 24 $^{th}$ Figure 9: Communication ETFs Imbalance at its lows... Figure 8: Cumulative Retail Imbalance in KORU As"
  },
  {
    "figure_id": "F212",
    "report_id": "R027",
    "label": "Figure 7",
    "context": "Figure 7: Retail Imbalance in KORU As of June 24 $^{th}$ Figure 9: Communication ETFs Imbalance at its lows... Figure 8: Cumulative Retail Imbalance in KORU As of June 24 $^{th}$ Figure 10: ...driven by large outflows in XLC"
  },
  {
    "figure_id": "F213",
    "report_id": "R027",
    "label": "Figure 9",
    "context": "Figure 9: Communication ETFs Imbalance at its lows... Figure 8: Cumulative Retail Imbalance in KORU As of June 24 $^{th}$ Figure 10: ...driven by large outflows in XLC (-4.2z week) As of Jun 24 $^{th}$ . Figure 11: Retail In"
  },
  {
    "figure_id": "F214",
    "report_id": "R027",
    "label": "Figure 10",
    "context": "Figure 10: ...driven by large outflows in XLC (-4.2z week) As of Jun 24 $^{th}$ . Figure 11: Retail Investor Daily Purchases by Stocks and ETFs \\$M, as of Jun 24 $^{th}$ - -Dec 02-Jan 09-Jan 16-Jan 26-Jan 02-Feb 09-Feb"
  },
  {
    "figure_id": "F215",
    "report_id": "R027",
    "label": "Figure 10",
    "context": "Figure 12: Retail Single Stock Activity by Themes"
  },
  {
    "figure_id": "F216",
    "report_id": "R027",
    "label": "Figure 12",
    "context": "Figure 12: Retail Single Stock Activity by Themes Figure 13: Retail Cumulative Purchases in Mag 7 + PLTR (\\$B) Figure 14: Retail Single Stock Activity by Sector (\\$B) Activity is dominated by Tech and Cons. Disc."
  },
  {
    "figure_id": "F217",
    "report_id": "R027",
    "label": "Figure 13",
    "context": "Figure 13: Retail Cumulative Purchases in Mag 7 + PLTR (\\$B) Figure 14: Retail Single Stock Activity by Sector (\\$B) Activity is dominated by Tech and Cons. Disc. Figure 15: Retail ETF Activity by Themes Buying / Selling of ETF"
  },
  {
    "figure_id": "F218",
    "report_id": "R027",
    "label": "Figure 14",
    "context": "Figure 14: Retail Single Stock Activity by Sector (\\$B) Activity is dominated by Tech and Cons. Disc. Figure 15: Retail ETF Activity by Themes Buying / Selling of ETFs aggregated by themes, in \\$B. ## Single Stock Stories with"
  },
  {
    "figure_id": "F219",
    "report_id": "R027",
    "label": "Figure 18",
    "context": "Figure 18: Retail Activity in BIRD Figure 19: Retail Activity in CPB"
  },
  {
    "figure_id": "F220",
    "report_id": "R027",
    "label": "Figure 18",
    "context": "Figure 18: Retail Activity in BIRD Figure 19: Retail Activity in CPB Figure 20: Retail Activity in ODD"
  },
  {
    "figure_id": "F221",
    "report_id": "R027",
    "label": "Figure 18",
    "context": "Figure 18: Retail Activity in BIRD Figure 19: Retail Activity in CPB Figure 20: Retail Activity in ODD Macro & Fundamental Stories Figure 21: Retail Imbalance in SNDK"
  },
  {
    "figure_id": "F222",
    "report_id": "R027",
    "label": "Figure 19",
    "context": "Figure 19: Retail Activity in CPB Figure 20: Retail Activity in ODD Macro & Fundamental Stories Figure 21: Retail Imbalance in SNDK As of June 24 $^{th}$"
  },
  {
    "figure_id": "F223",
    "report_id": "R027",
    "label": "Figure 20",
    "context": "Figure 20: Retail Activity in ODD Macro & Fundamental Stories Figure 21: Retail Imbalance in SNDK As of June 24 $^{th}$ Figure 22: Cumulative Retail Imbalance in SNDK As of June 24 $^{th}$ Figure 23: Retail Imbalance in MU"
  },
  {
    "figure_id": "F224",
    "report_id": "R027",
    "label": "Figure 21",
    "context": "Figure 21: Retail Imbalance in SNDK As of June 24 $^{th}$ Figure 22: Cumulative Retail Imbalance in SNDK As of June 24 $^{th}$ Figure 23: Retail Imbalance in MU Figure 24: Cumulative Retail Imbalance in MU As of June 24 $^{th"
  },
  {
    "figure_id": "F225",
    "report_id": "R027",
    "label": "Figure 22",
    "context": "Figure 22: Cumulative Retail Imbalance in SNDK As of June 24 $^{th}$ Figure 23: Retail Imbalance in MU Figure 24: Cumulative Retail Imbalance in MU As of June 24 $^{th}$ Figure 25: Retail Imbalance in WDC"
  },
  {
    "figure_id": "F226",
    "report_id": "R027",
    "label": "Figure 23",
    "context": "Figure 23: Retail Imbalance in MU Figure 24: Cumulative Retail Imbalance in MU As of June 24 $^{th}$ Figure 25: Retail Imbalance in WDC Figure 26: Cumulative Retail Imbalance in WDC As of June 23 $^{rd}$"
  },
  {
    "figure_id": "F227",
    "report_id": "R027",
    "label": "Figure 24",
    "context": "Figure 24: Cumulative Retail Imbalance in MU As of June 24 $^{th}$ Figure 25: Retail Imbalance in WDC Figure 26: Cumulative Retail Imbalance in WDC As of June 23 $^{rd}$ Figure 27: Retail Imbalance in AMAT"
  },
  {
    "figure_id": "F228",
    "report_id": "R027",
    "label": "Figure 25",
    "context": "Figure 25: Retail Imbalance in WDC Figure 26: Cumulative Retail Imbalance in WDC As of June 23 $^{rd}$ Figure 27: Retail Imbalance in AMAT As of June 23 $^{rd}$ Figure 28: Cumulative Retail Imbalance in AMAT"
  },
  {
    "figure_id": "F229",
    "report_id": "R027",
    "label": "Figure 26",
    "context": "Figure 26: Cumulative Retail Imbalance in WDC As of June 23 $^{rd}$ Figure 27: Retail Imbalance in AMAT As of June 23 $^{rd}$ Figure 28: Cumulative Retail Imbalance in AMAT As of June 23 $^{rd}$ Figure 29: Retail Imbalance in"
  },
  {
    "figure_id": "F230",
    "report_id": "R027",
    "label": "Figure 27",
    "context": "Figure 27: Retail Imbalance in AMAT As of June 23 $^{rd}$ Figure 28: Cumulative Retail Imbalance in AMAT As of June 23 $^{rd}$ Figure 29: Retail Imbalance in LRCX As of June 23 $^{rd}$ Figure 30: Cumulative Retail Imbalance i"
  },
  {
    "figure_id": "F231",
    "report_id": "R027",
    "label": "Figure 28",
    "context": "Figure 28: Cumulative Retail Imbalance in AMAT As of June 23 $^{rd}$ Figure 29: Retail Imbalance in LRCX As of June 23 $^{rd}$ Figure 30: Cumulative Retail Imbalance in LRCX As of June 23 $^{rd}$ Figure 31: Retail Imbalance i"
  },
  {
    "figure_id": "F232",
    "report_id": "R027",
    "label": "Figure 29",
    "context": "Figure 29: Retail Imbalance in LRCX As of June 23 $^{rd}$ Figure 30: Cumulative Retail Imbalance in LRCX As of June 23 $^{rd}$ Figure 31: Retail Imbalance in KLAC Figure 32: Cumulative Retail Imbalance in KLAC As of June 23 $"
  },
  {
    "figure_id": "F233",
    "report_id": "R027",
    "label": "Figure 30",
    "context": "Figure 30: Cumulative Retail Imbalance in LRCX As of June 23 $^{rd}$ Figure 31: Retail Imbalance in KLAC Figure 32: Cumulative Retail Imbalance in KLAC As of June 23 $^{rd}$ Figure 33: Retail Imbalance in NVDA"
  },
  {
    "figure_id": "F234",
    "report_id": "R027",
    "label": "Figure 31",
    "context": "Figure 31: Retail Imbalance in KLAC Figure 32: Cumulative Retail Imbalance in KLAC As of June 23 $^{rd}$ Figure 33: Retail Imbalance in NVDA As of June 23 $^{rd}$ Figure 34: Cumulative Retail Imbalance in NVDA"
  },
  {
    "figure_id": "F235",
    "report_id": "R027",
    "label": "Figure 32",
    "context": "Figure 32: Cumulative Retail Imbalance in KLAC As of June 23 $^{rd}$ Figure 33: Retail Imbalance in NVDA As of June 23 $^{rd}$ Figure 34: Cumulative Retail Imbalance in NVDA As of June 23 $^{rd}$ Figure 35: Retail Imbalance i"
  },
  {
    "figure_id": "F236",
    "report_id": "R027",
    "label": "Figure 33",
    "context": "Figure 33: Retail Imbalance in NVDA As of June 23 $^{rd}$ Figure 34: Cumulative Retail Imbalance in NVDA As of June 23 $^{rd}$ Figure 35: Retail Imbalance in APGE As of June 23 $^{rd}$ Figure 36: Cumulative Retail Imbalance i"
  },
  {
    "figure_id": "F237",
    "report_id": "R027",
    "label": "Figure 34",
    "context": "Figure 34: Cumulative Retail Imbalance in NVDA As of June 23 $^{rd}$ Figure 35: Retail Imbalance in APGE As of June 23 $^{rd}$ Figure 36: Cumulative Retail Imbalance in APGE As of June 23 $^{rd}$"
  },
  {
    "figure_id": "F238",
    "report_id": "R027",
    "label": "Figure 35",
    "context": "Figure 35: Retail Imbalance in APGE As of June 23 $^{rd}$ Figure 36: Cumulative Retail Imbalance in APGE As of June 23 $^{rd}$ Figure 38: Cumulative Retail Imbalance in ABBV As of June 23 $^{rd}$"
  },
  {
    "figure_id": "F239",
    "report_id": "R027",
    "label": "Figure 36",
    "context": "Figure 36: Cumulative Retail Imbalance in APGE As of June 23 $^{rd}$ Figure 38: Cumulative Retail Imbalance in ABBV As of June 23 $^{rd}$ Figure 39: Retail Imbalance in GETY"
  },
  {
    "figure_id": "F240",
    "report_id": "R027",
    "label": "Figure 38",
    "context": "Figure 38: Cumulative Retail Imbalance in ABBV As of June 23 $^{rd}$ Figure 39: Retail Imbalance in GETY As of June 23 $^{rd}$ Figure 40: Cumulative Retail Imbalance in GETY"
  },
  {
    "figure_id": "F241",
    "report_id": "R027",
    "label": "Figure 38",
    "context": "Figure 38: Cumulative Retail Imbalance in ABBV As of June 23 $^{rd}$ Figure 39: Retail Imbalance in GETY As of June 23 $^{rd}$ Figure 40: Cumulative Retail Imbalance in GETY As of June 23 $^{rd}$ Figure 41: Retail Imbalance i"
  },
  {
    "figure_id": "F242",
    "report_id": "R027",
    "label": "Figure 39",
    "context": "Figure 39: Retail Imbalance in GETY As of June 23 $^{rd}$ Figure 40: Cumulative Retail Imbalance in GETY As of June 23 $^{rd}$ Figure 41: Retail Imbalance in AMC As of June 23 $^{rd}$ Figure 42: Cumulative Retail Imbalance in"
  },
  {
    "figure_id": "F243",
    "report_id": "R027",
    "label": "Figure 40",
    "context": "Figure 40: Cumulative Retail Imbalance in GETY As of June 23 $^{rd}$ Figure 41: Retail Imbalance in AMC As of June 23 $^{rd}$ Figure 42: Cumulative Retail Imbalance in AMC As of June 23 $^{rd}$ Retail Activity in Options"
  },
  {
    "figure_id": "F244",
    "report_id": "R027",
    "label": "Figure 41",
    "context": "Figure 41: Retail Imbalance in AMC As of June 23 $^{rd}$ Figure 42: Cumulative Retail Imbalance in AMC As of June 23 $^{rd}$ Retail Activity in Options Figure 43: Top 40 Equities with Most Delta Bought (in \\$Mn) Figure 44: To"
  },
  {
    "figure_id": "F245",
    "report_id": "R027",
    "label": "Figure 42",
    "context": "Figure 42: Cumulative Retail Imbalance in AMC As of June 23 $^{rd}$ Retail Activity in Options Figure 43: Top 40 Equities with Most Delta Bought (in \\$Mn) Figure 44: Top 40 Equities with Most Gamma Bought (in \\$Mn) Figure 45:"
  },
  {
    "figure_id": "F246",
    "report_id": "R027",
    "label": "Figure 43",
    "context": "Figure 43: Top 40 Equities with Most Delta Bought (in \\$Mn) Figure 44: Top 40 Equities with Most Gamma Bought (in \\$Mn) Figure 45: Top 40 Equities with Most Gamma Sold (in \\$Mn) # Retail Investors Options Activity by Sectors"
  },
  {
    "figure_id": "F247",
    "report_id": "R027",
    "label": "Figure 44",
    "context": "Figure 44: Top 40 Equities with Most Gamma Bought (in \\$Mn) Figure 45: Top 40 Equities with Most Gamma Sold (in \\$Mn) # Retail Investors Options Activity by Sectors Figure 46: Retail Options Trading Share"
  },
  {
    "figure_id": "F248",
    "report_id": "R027",
    "label": "Figure 45",
    "context": "Figure 45: Top 40 Equities with Most Gamma Sold (in \\$Mn) # Retail Investors Options Activity by Sectors Figure 46: Retail Options Trading Share Figure 47: Retail Options Volume (Calls and Puts) Figure 48: Retail Options Volu"
  },
  {
    "figure_id": "F249",
    "report_id": "R027",
    "label": "Figure 46",
    "context": "Figure 46: Retail Options Trading Share Figure 47: Retail Options Volume (Calls and Puts) Figure 48: Retail Options Volume (Calls and Puts), Information Technology Figure 49: Retail Options Volume (Calls and Puts), Communicat"
  },
  {
    "figure_id": "F250",
    "report_id": "R027",
    "label": "Figure 47",
    "context": "Figure 47: Retail Options Volume (Calls and Puts) Figure 48: Retail Options Volume (Calls and Puts), Information Technology Figure 49: Retail Options Volume (Calls and Puts), Communication Services Figure 50: Retail Options V"
  },
  {
    "figure_id": "F251",
    "report_id": "R027",
    "label": "Figure 48",
    "context": "Figure 48: Retail Options Volume (Calls and Puts), Information Technology Figure 49: Retail Options Volume (Calls and Puts), Communication Services Figure 50: Retail Options Volume (Calls and Puts), Health Care Figure 51: Ret"
  },
  {
    "figure_id": "F252",
    "report_id": "R027",
    "label": "Figure 49",
    "context": "Figure 49: Retail Options Volume (Calls and Puts), Communication Services Figure 50: Retail Options Volume (Calls and Puts), Health Care Figure 51: Retail Options Volume (Calls and Puts), Financials Figure 52: Retail Options"
  },
  {
    "figure_id": "F253",
    "report_id": "R027",
    "label": "Figure 50",
    "context": "Figure 50: Retail Options Volume (Calls and Puts), Health Care Figure 51: Retail Options Volume (Calls and Puts), Financials Figure 52: Retail Options Volume (Calls and Puts), Discretionary Figure 53: Retail Options Volume (C"
  },
  {
    "figure_id": "F254",
    "report_id": "R027",
    "label": "Figure 51",
    "context": "Figure 51: Retail Options Volume (Calls and Puts), Financials Figure 52: Retail Options Volume (Calls and Puts), Discretionary Figure 53: Retail Options Volume (Calls and Puts), Staples Figure 54: Retail Options Volume (Calls"
  },
  {
    "figure_id": "F255",
    "report_id": "R027",
    "label": "Figure 52",
    "context": "Figure 52: Retail Options Volume (Calls and Puts), Discretionary Figure 53: Retail Options Volume (Calls and Puts), Staples Figure 54: Retail Options Volume (Calls and Puts), Energy Figure 55: Retail Options Volume (Calls and"
  },
  {
    "figure_id": "F256",
    "report_id": "R027",
    "label": "Figure 53",
    "context": "Figure 53: Retail Options Volume (Calls and Puts), Staples Figure 54: Retail Options Volume (Calls and Puts), Energy Figure 55: Retail Options Volume (Calls and Puts), Materials # Appendix: Alternative Data Points on Retail A"
  },
  {
    "figure_id": "F257",
    "report_id": "R027",
    "label": "Figure 54",
    "context": "Figure 54: Retail Options Volume (Calls and Puts), Energy Figure 55: Retail Options Volume (Calls and Puts), Materials # Appendix: Alternative Data Points on Retail Activity Figure 56: Retail Brokerage Volume Hit Record \\~37% i"
  },
  {
    "figure_id": "F258",
    "report_id": "R027",
    "label": "Figure 56",
    "context": "Figure 56: Retail Brokerage Volume Hit Record \\~37% in January 2021"
  },
  {
    "figure_id": "F259",
    "report_id": "R027",
    "label": "Figure 56",
    "context": "Figure 56: Retail Brokerage Volume Hit Record \\~37% in January 2021"
  },
  {
    "figure_id": "F260",
    "report_id": "R028",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Normalized market response to NFP surprises since 1997 Exhibit 2: Market sensitivity to NFP surprises declined since Greenspan ## Different pattern for inflation data"
  },
  {
    "figure_id": "F261",
    "report_id": "R028",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Normalized market response to NFP surprises since 1997 Exhibit 2: Market sensitivity to NFP surprises declined since Greenspan ## Different pattern for inflation data Exhibit 3 plots normalized surprises in monthly C"
  },
  {
    "figure_id": "F262",
    "report_id": "R028",
    "label": "Exhibit 4",
    "context": "Exhibit 3: Normalized market response to CPI surprises since 1998 Exhibit 4: Market sensitivity to CPI increased post-pandemic ## Trend confirmed by intraday moves"
  },
  {
    "figure_id": "F263",
    "report_id": "R028",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Normalized market response to CPI surprises since 1998 Exhibit 4: Market sensitivity to CPI increased post-pandemic ## Trend confirmed by intraday moves Daily yield changes capture more than the market response to ec"
  },
  {
    "figure_id": "F264",
    "report_id": "R028",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Dealer net gamma exposure Exhibit 8: Historical spot dealer net gamma exposure Exhibit 9: Net customer flow in gamma (\\$k)"
  },
  {
    "figure_id": "F265",
    "report_id": "R028",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Dealer net gamma exposure Exhibit 8: Historical spot dealer net gamma exposure Exhibit 9: Net customer flow in gamma (\\$k)"
  },
  {
    "figure_id": "F266",
    "report_id": "R028",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Notional of callable issuance Exhibit 12: Vega supply from callable issuance Exhibit 13: Recent vega supply by pricing date"
  },
  {
    "figure_id": "F267",
    "report_id": "R028",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Notional of callable issuance Exhibit 12: Vega supply from callable issuance Exhibit 13: Recent vega supply by pricing date Exhibit 14: Coupon of supranational issuance (6-10y maturity) vs. 10y Treasury yields"
  },
  {
    "figure_id": "F268",
    "report_id": "R028",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Vega supply from callable issuance Exhibit 13: Recent vega supply by pricing date Exhibit 14: Coupon of supranational issuance (6-10y maturity) vs. 10y Treasury yields ## Skew Signal Monitor"
  },
  {
    "figure_id": "F269",
    "report_id": "R028",
    "label": "Exhibit 13",
    "context": "Exhibit 15: Skew change and duration position"
  },
  {
    "figure_id": "F270",
    "report_id": "R028",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Skew change and duration position Exhibit 16: Duration position and signal performance • Trade idea: Maintain long 2y10y straddle outright"
  },
  {
    "figure_id": "F271",
    "report_id": "R028",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Skew change and duration position Exhibit 16: Duration position and signal performance • Trade idea: Maintain long 2y10y straddle outright • Trade idea: Maintain long 1y1y F/F+25/F+50 payer ladder ## Valuation Method"
  },
  {
    "figure_id": "F272",
    "report_id": "R029",
    "label": "Figure 1",
    "context": "Figure 1: Turkiye: defence spending, 1980–2024 Note: Figures in Turkish lira reflect the revaluation in 2005, which removed six zeros from the currency. Sources: NATO, 'Financial and Economic Data Relating to NATO Defence'; Mili"
  },
  {
    "figure_id": "F273",
    "report_id": "R029",
    "label": "Figure 1",
    "context": "Figure 1: Turkiye: defence spending, 1980–2024 Note: Figures in Turkish lira reflect the revaluation in 2005, which removed six zeros from the currency. Sources: NATO, 'Financial and Economic Data Relating to NATO Defence'; Mili"
  },
  {
    "figure_id": "F274",
    "report_id": "R029",
    "label": "Figure 2",
    "context": "Figure 2: Turkiye: defence and aerospace imports, 2012–22 SSM was placed under the direct authority of the presidency in 2018. It was accordingly renamed the Defence Industry Agency (Savunma Sanayii Başkanlığı, SSB). This upgrad"
  },
  {
    "figure_id": "F275",
    "report_id": "R029",
    "label": "Figure 3",
    "context": "Figure 3: Turkiye: defence and aerospace exports, 1997–2023 In stark contrast to the bottom-up, purely technical and price-based considerations that led to the selection of the Chinese FD-2000 air- and missile-defence system in"
  },
  {
    "figure_id": "F276",
    "report_id": "R029",
    "label": "Figure 3",
    "context": "Figure 3: Turkiye: defence and aerospace exports, 1997–2023 In stark contrast to the bottom-up, purely technical and price-based considerations that led to the selection of the Chinese FD-2000 air- and missile-defence system in"
  },
  {
    "figure_id": "F277",
    "report_id": "R032",
    "label": "Figure 1",
    "context": "About 40 percent of workers worldwide are in high-exposure occupations; the share is 60 percent in advanced economies, which indicates potentially large macroeconomic implications. Advanced economies have a greater share of high-exposure occupations, with eith"
  },
  {
    "figure_id": "F278",
    "report_id": "R032",
    "label": "Figure 1",
    "context": "24 percent, respectively, and low-income countries have shares of 8 and 18 percent, respectively. $^{5}$ A similar result emerges when looking at selected individual countries using more refined classifications (Figure 1, panel 2). Almost 70 and 60 percent of "
  },
  {
    "figure_id": "F279",
    "report_id": "R032",
    "label": "Figure 2",
    "context": "■ High exposure, high complementarity ■ High exposure, low complementarity ■ Low exposure Sources: American Community Survey; Gran Encuesta Integrada de Hogares; India Periodic Labour Force Survey; International Labour Organization; Labour Market Dynamics in S"
  },
  {
    "figure_id": "F280",
    "report_id": "R032",
    "label": "Figure 2",
    "context": "Note: Country labels use International Organization for Standardization (ISO) country codes. AEs = advanced economies; EMs = emerging market economies; LICs = low-income countries; World = all countries in the sample. Share of employment within each country gr"
  },
  {
    "figure_id": "F281",
    "report_id": "R032",
    "label": "Figure 2",
    "context": "The composition of the labor force in terms of broad occupational groups reflecting countries' economic structure explains most of the differences in exposure and complementarity across countries. Figure 2 reports the employment shares by occupational groups f"
  },
  {
    "figure_id": "F282",
    "report_id": "R032",
    "label": "Figure 3",
    "context": "Beyond the overall exposure of each country to AI, different groups within countries are likely to be affected differently. The advent of AI could exacerbate inequality within countries along various dimensions, such as the income level of individuals, their e"
  },
  {
    "figure_id": "F283",
    "report_id": "R032",
    "label": "Figure 3",
    "context": "Exposure is higher for women and for more educated workers but is mitigated by a higher potential for complementarity with AI (Figure 3). In most countries, women tend to be employed in high-exposure occupations more than men (Figure 3, panel 1). Because this "
  },
  {
    "figure_id": "F284",
    "report_id": "R032",
    "label": "Figure 3",
    "context": "between low- and high-complementarity jobs, the result can be interpreted to mean that women face both greater risks and greater opportunities. Exceptions to this pattern may be attributed to high shares of women in agricultural jobs, especially in countries w"
  },
  {
    "figure_id": "F285",
    "report_id": "R032",
    "label": "Figure 4",
    "context": "Note: The bars represent employment shares in high-exposure occupations. In panel 1, employment shares are conditional on each gender category. In panel 2, employment shares are conditional on each of the four education categories (middle school and below, hig"
  },
  {
    "figure_id": "F286",
    "report_id": "R032",
    "label": "Figure 4",
    "context": "## Figure 4. Share of Employment in High-Exposure Occupations and Potential Complementarity by Income Deciles 1. High-Exposure, Low-Complementarity (Percent) GBR USA BRA COL ZAF IND 2. High-Exposure, High-Complementarity (Percent) GBR USA BRA COL ZAF IND ## 3."
  },
  {
    "figure_id": "F287",
    "report_id": "R032",
    "label": "Figure 5",
    "context": "# III. Worker Reallocation in the AI-Induced Transformation In the long term, workers will adjust to changing skill demands and sector shifts, with some potentially transitioning to high-AI-complementarity roles and some struggling to adapt. The previous secti"
  },
  {
    "figure_id": "F288",
    "report_id": "R032",
    "label": "Figure 5",
    "context": "In the long term, workers will adjust to changing skill demands and sector shifts, with some potentially transitioning to high-AI-complementarity roles and some struggling to adapt. The previous section provided a static picture of AI exposure based on the cur"
  },
  {
    "figure_id": "F289",
    "report_id": "R032",
    "label": "Figure 5",
    "context": "Sources: Pesquisa Nacional por Amostra de Domicílios Contínua; UK Labour Force Survey; and IMF staff calculations. Note: \"From\" indicates the exposure category of the occupation the individual had in the preceding quarter; \"to\" indicates the exposure category "
  },
  {
    "figure_id": "F290",
    "report_id": "R032",
    "label": "Figure 5",
    "context": "Sources: Pesquisa Nacional por Amostra de Domicílios Contínua; UK Labour Force Survey; and IMF staff calculations. Note: \"From\" indicates the exposure category of the occupation the individual had in the preceding quarter; \"to\" indicates the exposure category "
  },
  {
    "figure_id": "F291",
    "report_id": "R032",
    "label": "Figure 5",
    "context": "Workers with a college education have historically shown a greater ability to transition into what are now jobs with high AI-complementarity potential. Both college- and non-college-educated workers frequently change occupations. The average yearly occupation-"
  },
  {
    "figure_id": "F292",
    "report_id": "R032",
    "label": "Figure 6",
    "context": "## Figure 6. Life-Cycle Profiles of Employment Shares by Education Level, Brazil and the United Kingdom —High exposure, high complementarity —High exposure, low complementarity —Low exposure Sources: Pesquisa Nacional por Amostra de Domicílios Continua; UK Lab"
  },
  {
    "figure_id": "F293",
    "report_id": "R032",
    "label": "Figure 6",
    "context": "Sources: Pesquisa Nacional por Amostra de Domicílios Continua; UK Labour Force Survey; and IMF staff calculations. Note: The panels plot the estimated share of employment by age for each exposure category for college- and non-college-educated workers, accordin"
  },
  {
    "figure_id": "F294",
    "report_id": "R032",
    "label": "Figure 6",
    "context": "AI adoption poses challenges but represents an opportunity for young college-educated workers' careers. Figure 6 shows that college-educated workers often transition from low- to high-complementarity jobs in their 20s and 30s. Their career progression stabiliz"
  },
  {
    "figure_id": "F295",
    "report_id": "R032",
    "label": "Figure 7",
    "context": "Historically, older workers have demonstrated less adaptability to technological advances; artificial intelligence may present a similar challenge for this demographic group. After unemployment, older workers previously employed in high-exposure and high-compl"
  },
  {
    "figure_id": "F296",
    "report_id": "R032",
    "label": "Figure 8",
    "context": "## Figure 8. Estimated Wage Premiums from Changing Occupation (Percent) ## 1. Brazil ## 2. United Kingdom ■ To high exposure, high complementarity (HEHC) ■ To high exposure, low complementarity (HELC) ■ To low exposure (LE) Sources: Pesquisa Nacional por Amost"
  },
  {
    "figure_id": "F297",
    "report_id": "R032",
    "label": "Figure 9",
    "context": "The model is calibrated to the United Kingdom, a country that is highly exposed to AI adoption. Workers' income is divided into three categories: (1) labor income, which can be positively or negatively exposed to AI depending on its degree of complementarity w"
  },
  {
    "figure_id": "F298",
    "report_id": "R032",
    "label": "Figure 9",
    "context": "The impact of AI is simulated by building three scenarios, which assume a labor share decline in line with comparable historical episodes associated with automation. The decrease in the labor share has historically been associated with routine-biased automatio"
  },
  {
    "figure_id": "F299",
    "report_id": "R032",
    "label": "Figure 10",
    "context": "The impact of AI on labor income inequality depends on the race between the degree of exposure to, and complementarity with, AI, and its boost to productivity. $^{16}$ When AI has low complementarity with labor, AI adoption leads to a decline in labor income i"
  },
  {
    "figure_id": "F300",
    "report_id": "R032",
    "label": "Figure 10",
    "context": "Figure 10. Change in Total Income by Income Percentile 1. Low Complementarity (Percent) 2. High Complementarity (Percent) 3. High Complementarity and High Productivity (Percent) Under the high-complementarity, high-productivity scenario, the increase in total "
  },
  {
    "figure_id": "F301",
    "report_id": "R032",
    "label": "Figure 11",
    "context": "2. High Complementarity (Percent) 3. High Complementarity and High Productivity (Percent) Under the high-complementarity, high-productivity scenario, the increase in total national income is largest and benefits all workers, although gains for those at the top"
  },
  {
    "figure_id": "F302",
    "report_id": "R032",
    "label": "Figure 11",
    "context": "Under the high-complementarity, high-productivity scenario, the increase in total national income is largest and benefits all workers, although gains for those at the top are larger. In the first scenario, in which AI has low complementarity, the use of AI lea"
  },
  {
    "figure_id": "F303",
    "report_id": "R032",
    "label": "Figure 12",
    "context": "evolving new (digital) business models and the presence of strong governance for effective enforcement. Figure 12. AI Preparedness Index and Employment Share in High-Exposure Occupations Sources: Fraser Institute; International Labour Organization; Internation"
  },
  {
    "figure_id": "F304",
    "report_id": "R032",
    "label": "Figure 13",
    "context": "Sources: Fraser Institute; International Labour Organization; International Telecommunication Union; United Nations; Universal Postal Union; World Bank; World Economic Forum; and IMF staff calculations. Note: The plot comprises 125 countries: 32 AEs, 56 EMs, a"
  },
  {
    "figure_id": "F305",
    "report_id": "R032",
    "label": "Figure 13",
    "context": "Figure 13. Information and Communications Technology Employment Share and Individual Components of the AI Preparedness Index ## 1. Digital Infrastructure 2. Human Capital and Labor Market Policies ## 3. Innovation and Integration 4. Regulation and Ethics Sourc"
  },
  {
    "figure_id": "F306",
    "report_id": "R032",
    "label": "Figure 13",
    "context": "2. Human Capital and Labor Market Policies ## 3. Innovation and Integration 4. Regulation and Ethics Sources: Fraser Institute; International Labour Organization; International Telecommunication Union; United Nations; Universal Postal Union; World Bank; World "
  },
  {
    "figure_id": "F307",
    "report_id": "R032",
    "label": "Figure 13",
    "context": "2. Human Capital and Labor Market Policies ## 3. Innovation and Integration 4. Regulation and Ethics Sources: Fraser Institute; International Labour Organization; International Telecommunication Union; United Nations; Universal Postal Union; World Bank; World "
  },
  {
    "figure_id": "F308",
    "report_id": "R032",
    "label": "Figure 1",
    "context": "Several studies have proposed definitions of AI exposure at the occupational level. The most common is the AI Occupational Exposure (AIOE) index of Felten, Raj, and Seamans (2021), measuring the correspondence between 10 AI applications and 52 human skills. Th"
  },
  {
    "figure_id": "F309",
    "report_id": "R032",
    "label": "Figure 2",
    "context": "Annex Figure 2.1, panel 1, plots the distribution of AI occupational exposure (AIOE) and complementarity for individual occupations within each major occupational group (that is, 4-digit occupation within each major group of the International Standard Classifi"
  },
  {
    "figure_id": "F310",
    "report_id": "R032",
    "label": "Figure 2",
    "context": "Given potential complementarity, $\\theta$ , a complementarity-adjusted AI occupational exposure (C-AIOE) measure can be constructed as follows: C-AIOE = AIOE $* (1 - \\theta - \\theta_{MIN})$ . The adjustment lowers exposure for occupations with higher values of"
  },
  {
    "figure_id": "F311",
    "report_id": "R032",
    "label": "Figure 3",
    "context": "In many emerging market and developing economies, despite high labor informality, AI-induced labor reallocation is unlikely to affect the size of the formal labor force significantly. Growth in high-exposure, high-complementarity occupations will likely be in "
  },
  {
    "figure_id": "F312",
    "report_id": "R032",
    "label": "Figure 3",
    "context": "## Annex Figure 3.1. AI and Informality 1. Share of Employment in Brazil, by Formality and Exposure Category (Percent) 2. Probability of a Formal Worker's Transition to a Low-Exposure Occupation, by Exposure Category (Percent) Note: Panel 1 shows the share of "
  },
  {
    "figure_id": "F313",
    "report_id": "R032",
    "label": "Figure 9",
    "context": "## IV.2 Additional Scenarios Two hypothetical scenarios are reported to highlight the impact of the displacement and the complementarity channels. In the first scenario, the displacement effect affects all workers equally, while complementarity affects workers"
  },
  {
    "figure_id": "F314",
    "report_id": "R032",
    "label": "Figure 4",
    "context": "## Annex Figure 4.1. Change in Total Income by Income Percentile 1. Equally Distributed Exposure and Data-Driven Complementarity (Percent) 2. Data-Driven Exposure with No Complementarity (Percent) Capital income Labor income Total income Note: The plots repres"
  },
  {
    "figure_id": "F315",
    "report_id": "R032",
    "label": "Figure 5",
    "context": "## Annex 5. AI Preparedness Index ## V.1 Indicators One of the main contributions of this note is the construction of an index—underpinning the analysis in Section Note: Data"
  },
  {
    "figure_id": "F316",
    "report_id": "R032",
    "label": "Figure 5",
    "context": "$$ Each aggregate dimension (digital infrastructure, human capital and labor market policies, digital innovation and economic integration, regulation and ethics) is the simple average of its normalized subcomponents. The AI Preparedness Index is then derived a"
  },
  {
    "figure_id": "F317",
    "report_id": "R034",
    "label": "Figure 2",
    "context": "2. BT operation: Here, we evaluate whether an LLM Agent can autonomously navigate BT code repositories and carry out toy tasks that demonstrate basic BT operation. This evaluation component involves two case studies that task an Agent with using EVEscape and E"
  },
  {
    "figure_id": "F318",
    "report_id": "R034",
    "label": "Figure 3",
    "context": "## Scenario Questions LLMs performed worse on the scenario-based question set than on the non-scenario set. As in the non-scenario results, LLMs generally had higher accuracy on questions given in MC format. The scenario-based question set produced higher deni"
  },
  {
    "figure_id": "F319",
    "report_id": "R034",
    "label": "Figure 4",
    "context": "## Results Task performance results are presented by model in Figure 4.1 for Lassa virus GPC and Figure 4.2 for influenza virus HA. All models are tested solely within ReAct scaffolds for the EVEscape task. We discuss the results below, along with insights gai"
  },
  {
    "figure_id": "F320",
    "report_id": "R034",
    "label": "Figure 4",
    "context": "Task performance results are presented by model in Figure 4.1 for Lassa virus GPC and Figure 4.2 for influenza virus HA. All models are tested solely within ReAct scaffolds for the EVEscape task. We discuss the results below, along with insights gained from ma"
  },
  {
    "figure_id": "F321",
    "report_id": "R034",
    "label": "Figure 4",
    "context": "We discuss the results below, along with insights gained from manual reviews of Agent transcripts. Given volume of data generated through this work, systematic review of every Agent attempt was impractical, but we used LLM Scout scanners to identify trends of "
  },
  {
    "figure_id": "F322",
    "report_id": "R034",
    "label": "Figure 4",
    "context": "NOTE: The number of task attempts, out of 10 total, in which each Agent successfully generated a correct cumulative escape score for Lassa GPC. Models are colored by provider, and a red hatching pattern indicates attempts that were blocked by either a model re"
  },
  {
    "figure_id": "F323",
    "report_id": "R034",
    "label": "Figure 4",
    "context": "NOTE: The number of task attempts, out of 10 total, in which each Agent successfully generated a correct cumulative escape score for Lassa GPC. Models are colored by provider, and a red hatching pattern indicates attempts that were blocked by either a model re"
  },
  {
    "figure_id": "F324",
    "report_id": "R034",
    "label": "Figure 4",
    "context": "PROMPT: GUIDING SUGGESTIONS Figure 4.2. Influenza virus HA Results for the EVEscape Case Study NOTE: The number of task attempts, out of 10 total, in which each Agent successfully generated a correct cumulative escape score for the influenza HA protein target."
  },
  {
    "figure_id": "F325",
    "report_id": "R034",
    "label": "Figure 4",
    "context": "Alongside our primary task performance metrics, we present additional data for GFP attempts that completed successfully. In Figure 4.4, we report the fraction of total critical residues, out of 16, $^{47}$ that were present in proteins generated in attempts th"
  },
  {
    "figure_id": "F326",
    "report_id": "R034",
    "label": "Figure 4",
    "context": "As readers examine our results, they should bear in mind that they are not intended to be interpreted as indicative of end-to-end protein engineering capability. The ESM3 task is explicitly framed to steer Agents away from a full, resource-intensive design pip"
  },
  {
    "figure_id": "F327",
    "report_id": "R034",
    "label": "Figure 4",
    "context": "Figure 4.3. GFP Results for the ESM3 Case Study (Solid) Operational Criteria (Hatched) Biological Criteria Denial Figure 4.4. ESM3 GFP Case Study: Fraction of Critical Residues Preserved"
  },
  {
    "figure_id": "F328",
    "report_id": "R034",
    "label": "Figure 4",
    "context": "(Solid) Operational Criteria (Hatched) Biological Criteria Denial Figure 4.4. ESM3 GFP Case Study: Fraction of Critical Residues Preserved"
  },
  {
    "figure_id": "F329",
    "report_id": "R034",
    "label": "Figure 4",
    "context": "(Solid) Operational Criteria (Hatched) Biological Criteria Denial Figure 4.4. ESM3 GFP Case Study: Fraction of Critical Residues Preserved"
  },
  {
    "figure_id": "F330",
    "report_id": "R034",
    "label": "Figure 4",
    "context": "(Solid) Operational Criteria (Hatched) Biological Criteria Denial Figure 4.4. ESM3 GFP Case Study: Fraction of Critical Residues Preserved Figure 4.5. Influenza HA Results for the ESM3 Case Study"
  },
  {
    "figure_id": "F331",
    "report_id": "R034",
    "label": "Figure 4",
    "context": "Figure 4.4. ESM3 GFP Case Study: Fraction of Critical Residues Preserved Figure 4.5. Influenza HA Results for the ESM3 Case Study PROMPT: GUIDING SUGGESTIONS"
  },
  {
    "figure_id": "F332",
    "report_id": "R034",
    "label": "Figure 4",
    "context": "Figure 4.4. ESM3 GFP Case Study: Fraction of Critical Residues Preserved Figure 4.5. Influenza HA Results for the ESM3 Case Study PROMPT: GUIDING SUGGESTIONS"
  },
  {
    "figure_id": "F333",
    "report_id": "R034",
    "label": "Figure 4",
    "context": "Figure 4.5. Influenza HA Results for the ESM3 Case Study PROMPT: GUIDING SUGGESTIONS"
  },
  {
    "figure_id": "F334",
    "report_id": "R034",
    "label": "Figure 4",
    "context": "Figure 4.5. Influenza HA Results for the ESM3 Case Study PROMPT: GUIDING SUGGESTIONS ## Discussion"
  },
  {
    "figure_id": "F335",
    "report_id": "R034",
    "label": "Figure 4",
    "context": "Figure 4.5. Influenza HA Results for the ESM3 Case Study PROMPT: GUIDING SUGGESTIONS ## Discussion As in our EVEscape results, several models neglected to perform the influenza HA variant of our task. The same two models that refused EVEscape, Claude Opus 4.7 "
  },
  {
    "figure_id": "F336",
    "report_id": "R034",
    "label": "Figure 4",
    "context": "Three influenza HA protein designs retained the globular head of the HA1 domain as well as HA2 stalks. These are also visualized in Figure 4.6. Similarly to the GFP designs, these proteins had low protein sequence identity relative to the reference HA (ranging"
  },
  {
    "figure_id": "F337",
    "report_id": "R035",
    "label": "Figure 1",
    "context": "\\- Establish a life skills framework to guide programming and practice. \\- Connect providers to evidence-based resources that support effective skill development. \\- Offer opportunities for professional development (PD) to build staff capacity and confidence. "
  },
  {
    "figure_id": "F338",
    "report_id": "R036",
    "label": "Figure 2",
    "context": "In this report, we discuss existing supply chain vulnerability in electric equipment affecting frontier AI data centers and their impact. In Chapter 2, we briefly review the results of our rapid literature review. In Chapter 3, we present the methodology used "
  },
  {
    "figure_id": "F339",
    "report_id": "R036",
    "label": "Figure 3",
    "context": "\\- FTM refers to components that are part of the electric grid transmission or generation system. $^{27}$ These components are typically owned and operated by electric utilities, independent power producers, or electric grid service providers. \\- BTM refers to"
  },
  {
    "figure_id": "F340",
    "report_id": "R036",
    "label": "Figure 4",
    "context": "Figure 4.1 demonstrates the process of matching HTS codes to the critical components identified in Chapter 3, relying on three sources: the International Trade Administration (ITA) Energy Trade Database, $^{44}$ the USITC HTS code database, $^{45}$ and USITC C"
  },
  {
    "figure_id": "F341",
    "report_id": "R036",
    "label": "Figure 4",
    "context": "Z _ {c o m p o s i t e} = \\sum_ {i = 1} ^ {n} w _ {i} Z _ {i}, $$ where Z represents z-scores for each metric i, $w_{i}$ represents the designated weight for each metric i, n is the number of metrics, and $Z_{composite}$ is the composite vulnerability score. T"
  },
  {
    "figure_id": "F342",
    "report_id": "R036",
    "label": "Figure 4",
    "context": "## Aggregate Findings From left to right, Figure 4.3 presents the composite score for each component, with each following panel presenting the decomposition of import decline, volume volatility, price volatility, HHI, and number of importing countries, respect"
  },
  {
    "figure_id": "F343",
    "report_id": "R036",
    "label": "Figure 4",
    "context": "From left to right, Figure 4.3 presents the composite score for each component, with each following panel presenting the decomposition of import decline, volume volatility, price volatility, HHI, and number of importing countries, respectively. Notably, HHI an"
  },
  {
    "figure_id": "F344",
    "report_id": "R036",
    "label": "Figure 4",
    "context": "Figure 4.4 presents the proportion of components that are exposed to various levels of vulnerability, by metric from year to year. Vulnerability levels correspond to the heatmap in Figure 4.3, with high vulnerability signified by red, low vulnerability by gree"
  },
  {
    "figure_id": "F345",
    "report_id": "R036",
    "label": "Figure 4",
    "context": "## Aggregate Findings Figure 4.5 presents a heatmap across BTM components. A higher proportion of backup power components are shaded in red at the top of the ranking, revealing that supply chain vulnerability in 2025 is not evenly distributed. This category in"
  },
  {
    "figure_id": "F346",
    "report_id": "R036",
    "label": "Figure 4",
    "context": "## Aggregate Findings Figure 4.5 presents a heatmap across BTM components. A higher proportion of backup power components are shaded in red at the top of the ranking, revealing that supply chain vulnerability in 2025 is not evenly distributed. This category in"
  },
  {
    "figure_id": "F347",
    "report_id": "R036",
    "label": "Figure 4",
    "context": "Figure 4.5. Vulnerability Map for BTM Components Figure 4.6 shows the aggregate trends in the proportion of components that are exposed to various levels of vulnerability by metric from year to year. Vulnerability levels correspond to the heatmap in Figure 4.5"
  },
  {
    "figure_id": "F348",
    "report_id": "R036",
    "label": "Figure 5",
    "context": "## Chapter 5. Assessing Supply Chain Risks for Frontier AI Data Center Expansion Using Case Studies In Chapters 3 and 4, we discussed the components that are critical for the expansion of frontier AI data centers and the supply chain vulnerabilities of those c"
  },
  {
    "figure_id": "F349",
    "report_id": "R037",
    "label": "Figure 1",
    "context": "Figure 2: Model Inclusion in BMA on AIPI [hyper-g/n prior; random model prior]"
  },
  {
    "figure_id": "F350",
    "report_id": "R037",
    "label": "Figure 2",
    "context": "Figure 2: Model Inclusion in BMA on AIPI [hyper-g/n prior; random model prior] To measure the economic complexity of each country, we consider ECIs for trade, technology, and research available on the Observatory of Economic Com"
  },
  {
    "figure_id": "F351",
    "report_id": "R037",
    "label": "Figure 3",
    "context": "Figure 3: Global relationship between AIPI and ECI a) Unweighted analysis b) Population-weighted analysis Both charts highlight the top performers in AI preparedness, concentrated in the northeast quadrants. Consistent with pr"
  },
  {
    "figure_id": "F352",
    "report_id": "R037",
    "label": "Figure 3",
    "context": "Figure 3: Global relationship between AIPI and ECI a) Unweighted analysis b) Population-weighted analysis Both charts highlight the top performers in AI preparedness, concentrated in the northeast quadrants. Consistent with pr"
  },
  {
    "figure_id": "F353",
    "report_id": "R037",
    "label": "Figure 4",
    "context": "Figure 5: AI preparedness and economic complexity in LICs and LMICs: Identifying local overperformers"
  },
  {
    "figure_id": "F354",
    "report_id": "R037",
    "label": "Figure 5",
    "context": "Figure 5: AI preparedness and economic complexity in LICs and LMICs: Identifying local overperformers 2024). In contrast, a few LMICs with relatively high observed AIP scores, such as Kenya, Kyrgyzstan, Lebanon, and the Philippi"
  },
  {
    "figure_id": "F355",
    "report_id": "R037",
    "label": "Figure 6",
    "context": "Figure 6: Key pillars driving overperformance across income groups of overperformers In low-income and lower-middle-income overperformers, regulation and ethics emerge as the most significant driver of AI preparedness, accountin"
  },
  {
    "figure_id": "F356",
    "report_id": "R037",
    "label": "Figure 7",
    "context": "Figure 7: Selected HICs (global) overperformers Singapore's AI readiness strategy strongly emphasizes all the AIPi pillars detailed above, and particularly regulation and ethics, as well as the development of robust digital infr"
  },
  {
    "figure_id": "F357",
    "report_id": "R037",
    "label": "Figure 8",
    "context": "Figure 8: Selected UMICs overperformers Spiderweb charts illustrate that China and Malaysia excel in all AIPi pillars relative to the average of non-overperformers within their income group. Notably, China demonstrates exception"
  },
  {
    "figure_id": "F358",
    "report_id": "R037",
    "label": "Figure 9",
    "context": "Figure 9: Selected LICs/LMICs overperformers India's AI readiness strategy places a significant emphasis on both human capital development and an ethical framework to support its vision of becoming a leader in AI innovation (Fig"
  },
  {
    "figure_id": "F359",
    "report_id": "R038",
    "label": "Figure 2",
    "context": "Figure 2: Impact of a 10% Change in Data Transparency on Sovereign Bond Returns Conditional on the Level of PPG External Debt in 2020 by Region"
  },
  {
    "figure_id": "F360",
    "report_id": "R038",
    "label": "Figure 2",
    "context": "Figure 2: Impact of a 10% Change in Data Transparency on Sovereign Bond Returns Conditional on the Level of PPG External Debt in 2020 by Region"
  },
  {
    "figure_id": "F361",
    "report_id": "R039",
    "label": "Figure 1",
    "context": "Figure 1: Total count of species ## Data and Method The data for this study have been provided by the Global Biodiversity Information Facility (GBIF), a global network, funded by various national governments, that offers open ac"
  },
  {
    "figure_id": "F362",
    "report_id": "R039",
    "label": "Figure 2",
    "context": "Figure 2: Selected species occurrence regions ## Results Taken together, non-determined legal status territories, areas with fragile and conflict-affected situations status, joint marine regimes, and transboundary river basins c"
  },
  {
    "figure_id": "F363",
    "report_id": "R039",
    "label": "Figure 3",
    "context": "Figure 3: Countries determined as Fragile and Conflict-affected Situations areas (FCS) in 2024 Figure 4: Log human population density in transboundary river basins Figure 5: Total count of critical species in geopolitically se"
  },
  {
    "figure_id": "F364",
    "report_id": "R039",
    "label": "Figure 3",
    "context": "Figure 3: Countries determined as Fragile and Conflict-affected Situations areas (FCS) in 2024 Figure 4: Log human population density in transboundary river basins Figure 5: Total count of critical species in geopolitically se"
  },
  {
    "figure_id": "F365",
    "report_id": "R039",
    "label": "Figure 3",
    "context": "Figure 3: Countries determined as Fragile and Conflict-affected Situations areas (FCS) in 2024 Figure 4: Log human population density in transboundary river basins Figure 5: Total count of critical species in geopolitically se"
  },
  {
    "figure_id": "F366",
    "report_id": "R039",
    "label": "Figure 6",
    "context": "Figure 7: Taxon variations (species class/order) in GSOA Non-determined Legal Status Areas"
  },
  {
    "figure_id": "F367",
    "report_id": "R039",
    "label": "Figure 7",
    "context": "Figure 7: Taxon variations (species class/order) in GSOA Non-determined Legal Status Areas Fragile Conflict States Marine Joint Regime Transboundary River Basins"
  },
  {
    "figure_id": "F368",
    "report_id": "R039",
    "label": "Figure 8",
    "context": "Figure 7: Taxon variations (species class/order) in GSOA Non-determined Legal Status Areas Fragile Conflict States Marine Joint Regime Transboundary River Basins Figure 8: Global taxon variations"
  },
  {
    "figure_id": "F369",
    "report_id": "R039",
    "label": "Figure 7",
    "context": "Figure 7: Taxon variations (species class/order) in GSOA Non-determined Legal Status Areas Fragile Conflict States Marine Joint Regime Transboundary River Basins Figure 8: Global taxon variations"
  },
  {
    "figure_id": "F370",
    "report_id": "R039",
    "label": "Figure 8",
    "context": "Figure 8: Global taxon variations This lack of governance coverage is especially troubling for endemic species with small occurrence regions (9.4% without treaties; 29.9% without RBOs; 9.3% with neither) and high ETIs (9.6% with"
  },
  {
    "figure_id": "F371",
    "report_id": "R039",
    "label": "Figure 8",
    "context": "Figure 8: Global taxon variations This lack of governance coverage is especially troubling for endemic species with small occurrence regions (9.4% without treaties; 29.9% without RBOs; 9.3% with neither) and high ETIs (9.6% with"
  },
  {
    "figure_id": "F372",
    "report_id": "R040",
    "label": "Figure 1",
    "context": "Figure 1: Distribution of ownership shares by BOS type (a) Public (b) Mixed (c) Participated Note: The figures show the distribution of ownership shares computed using data obtained from Orbis. Data from Orbis, 2019. Public"
  },
  {
    "figure_id": "F373",
    "report_id": "R040",
    "label": "Figure 1",
    "context": "Figure 1: Distribution of ownership shares by BOS type (a) Public (b) Mixed (c) Participated Note: The figures show the distribution of ownership shares computed using data obtained from Orbis. Data from Orbis, 2019. Public"
  },
  {
    "figure_id": "F374",
    "report_id": "R040",
    "label": "Figure 1",
    "context": "Figure 1: Distribution of ownership shares by BOS type (a) Public (b) Mixed (c) Participated Note: The figures show the distribution of ownership shares computed using data obtained from Orbis. Data from Orbis, 2019. Public"
  },
  {
    "figure_id": "F375",
    "report_id": "R040",
    "label": "Figure 2",
    "context": "Figure 3: Effect of privatization on workers' wages for different groups"
  },
  {
    "figure_id": "F376",
    "report_id": "R040",
    "label": "Figure 3",
    "context": "Figure 3: Effect of privatization on workers' wages for different groups (a) Education"
  },
  {
    "figure_id": "F377",
    "report_id": "R040",
    "label": "Figure 3",
    "context": "Figure 3: Effect of privatization on workers' wages for different groups (a) Education (b) Age (c) Tenure"
  },
  {
    "figure_id": "F378",
    "report_id": "R040",
    "label": "Figure 3",
    "context": "Figure 3: Effect of privatization on workers' wages for different groups (a) Education (b) Age (c) Tenure (d) Occupation Note: The figures show the estimates of time-to-event dummies interacted with a privatization indicat"
  },
  {
    "figure_id": "F379",
    "report_id": "R040",
    "label": "Figure 3",
    "context": "Figure 3: Effect of privatization on workers' wages for different groups (a) Education (b) Age (c) Tenure (d) Occupation Note: The figures show the estimates of time-to-event dummies interacted with a privatization indicat"
  },
  {
    "figure_id": "F380",
    "report_id": "R040",
    "label": "Figure 4",
    "context": "Figure 4: Effect of privatization on workers' probability of unemployment (a) Education"
  },
  {
    "figure_id": "F381",
    "report_id": "R040",
    "label": "Figure 4",
    "context": "Figure 4: Effect of privatization on workers' probability of unemployment (a) Education (b) Age (c) Tenure"
  },
  {
    "figure_id": "F382",
    "report_id": "R040",
    "label": "Figure 4",
    "context": "Figure 4: Effect of privatization on workers' probability of unemployment (a) Education (b) Age (c) Tenure (d) Occupation Note: The figures show the estimates of time-to-event dummies interacted with a privatization indica"
  },
  {
    "figure_id": "F383",
    "report_id": "R040",
    "label": "Figure 4",
    "context": "Figure 4: Effect of privatization on workers' probability of unemployment (a) Education (b) Age (c) Tenure (d) Occupation Note: The figures show the estimates of time-to-event dummies interacted with a privatization indica"
  },
  {
    "figure_id": "F384",
    "report_id": "R040",
    "label": "Figure 5",
    "context": "Figure 5: Effect of privatization on firms' average wages and employment (a) Average wage"
  },
  {
    "figure_id": "F385",
    "report_id": "R040",
    "label": "Figure 5",
    "context": "Figure 5: Effect of privatization on firms' average wages and employment (a) Average wage (b) Employment Note: The figures show the estimates of time-to-event dummies interacted with a privatization indicator from regressions"
  },
  {
    "figure_id": "F386",
    "report_id": "R040",
    "label": "Figure 5",
    "context": "Figure 5: Effect of privatization on firms' average wages and employment (a) Average wage (b) Employment Note: The figures show the estimates of time-to-event dummies interacted with a privatization indicator from regressions"
  },
  {
    "figure_id": "F387",
    "report_id": "R040",
    "label": "Figure 6",
    "context": "Figure 6: Employment share of BOS. ## Entry and exit Figure 7: Entry and exit rates."
  },
  {
    "figure_id": "F388",
    "report_id": "R040",
    "label": "Figure 7",
    "context": "Figure 7: Entry and exit rates. Following the observed decline in the entry rate of new firms, we also find a steady fall in the employment share of young firms. Figure 8 reveals that the fraction of employment in firms operatin"
  },
  {
    "figure_id": "F389",
    "report_id": "R040",
    "label": "Figure 8",
    "context": "Figure 9: Job creation and destruction."
  },
  {
    "figure_id": "F390",
    "report_id": "R040",
    "label": "Figure 9",
    "context": "Figure 9: Job creation and destruction. Figure 10: Job reallocation. A lower level of business dynamism is also associated with declining variation in firm-level growth rates. Although there is a declining trend in the standar"
  },
  {
    "figure_id": "F391",
    "report_id": "R040",
    "label": "Figure 9",
    "context": "Figure 11: Standard deviation of firm employment growth."
  },
  {
    "figure_id": "F392",
    "report_id": "R040",
    "label": "Figure 10",
    "context": "Figure 11: Standard deviation of firm employment growth. ## 5.2 BOS and business dynamism We test whether a high concentration of BOS is associated with different metrics of business dynamism using variation in the industry-level"
  },
  {
    "figure_id": "F393",
    "report_id": "R041",
    "label": "Figure 1",
    "context": "Figure 1: A training question preceding the ACASI administered IPV module ## 3 Experiment 1: Do respondents understand ACASI?"
  },
  {
    "figure_id": "F394",
    "report_id": "R041",
    "label": "Figure 2",
    "context": "Figure 2: Design of the Measurement Experiment II Figure 3: Impact of the Measurement Experiment II on Face-to-Face IPV Reporting Notes: The figure shows results from an experiment where for half the respondents two questions"
  },
  {
    "figure_id": "F395",
    "report_id": "R041",
    "label": "Figure 2",
    "context": "Figure 2: Design of the Measurement Experiment II Figure 3: Impact of the Measurement Experiment II on Face-to-Face IPV Reporting Notes: The figure shows results from an experiment where for half the respondents two questions"
  },
  {
    "figure_id": "F396",
    "report_id": "R042",
    "label": "Figure 1",
    "context": "Figure 1: Intervention timeline \\- renewals delivered in health centers (or during home visits by HPO, with very limited capacity) ## 4 Study Design ## Randomization ## Data and Outcomes"
  },
  {
    "figure_id": "F397",
    "report_id": "R042",
    "label": "Figure 2",
    "context": "Figure 2: Evolution of Sayana Press injections (above) and overall number of contraceptives dispensed (below) Notes: The first figure plots the average number of Sayana Press injections while the second figure shows the average"
  },
  {
    "figure_id": "F398",
    "report_id": "R043",
    "label": "Figure 1",
    "context": "Figure 1: Fossil Fuel Subsidies by Country (latest year available) ## 2. Fossil Fuel Subsidies, Resource Rent and Carbon Emissions among Oil Exporters The magnitudes of global subsidies of fossil fuels are staggering. Black et a"
  },
  {
    "figure_id": "F399",
    "report_id": "R043",
    "label": "Figure 2",
    "context": "## 2. Fossil Fuel Subsidies, Resource Rent and Carbon Emissions among Oil Exporters The magnitudes of global subsidies of fossil fuels are staggering. Black et al. (2023) in an IMF working paper estimate that the total global subsidies of fossil fuels amounted"
  },
  {
    "figure_id": "F400",
    "report_id": "R043",
    "label": "Figure 3",
    "context": "However, the above report and other studies of fossil fuel subsidies, such as one by Kojum and Koplow (2017), focus on oil consuming/importing countries or fossil fuel consuming sectors of the economy. The oil and gas producing countries, on the other hand, fa"
  },
  {
    "figure_id": "F401",
    "report_id": "R043",
    "label": "Figure 3",
    "context": "Figure 3. Fossil Fuel Subsidies, Resource Rents and Carbon emission among Oil Exporters: Case 1 Note: The figure assumes producers are subsidized at the production level and thus for full output aimed at domestic and world markets. It also assumes domestic con"
  },
  {
    "figure_id": "F402",
    "report_id": "R043",
    "label": "Figure 4",
    "context": "Figure 4: Fossil Fuel Subsidies significantly contribute to CO2 Emissions in Oil Exporting MENA ## 5.3. Flaring matters in contributing to CO2 emissions only for the full sample of 41 countries Figure 5. Flaring by Country"
  },
  {
    "figure_id": "F403",
    "report_id": "R043",
    "label": "Figure 5",
    "context": "## 5.3. Flaring matters in contributing to CO2 emissions only for the full sample of 41 countries Figure 5. Flaring by Country ## Figure 6. Trends in flaring ## 5.4 World oil prices affect the level of subsidy"
  },
  {
    "figure_id": "F404",
    "report_id": "R043",
    "label": "Figure 5",
    "context": "Figure 5. Flaring by Country ## Figure 6. Trends in flaring ## 5.4 World oil prices affect the level of subsidy ## 6. Country-Level Projections: Removing Subsidies or Taxing Carbon?"
  },
  {
    "figure_id": "F405",
    "report_id": "R044",
    "label": "Figure 1",
    "context": "The quantitative data confirms that while women are more likely than men to make the decisions about the water"
  },
  {
    "figure_id": "F406",
    "report_id": "R045",
    "label": "Figure 1",
    "context": "Figure 1: Distribution of cluster sizes in six partial population experiments (a) This paper; $n = 68,808$ ; $G = 3,982$ ; $n / G = 17.3$ ; $sd(n_g) = 8.25$ . (b) Crépon et al. (2013); $n = 21,431$ ; $G = 235$ ; $n / G = 91.2$"
  },
  {
    "figure_id": "F407",
    "report_id": "R045",
    "label": "Figure 1",
    "context": "Figure 1: Distribution of cluster sizes in six partial population experiments (a) This paper; $n = 68,808$ ; $G = 3,982$ ; $n / G = 17.3$ ; $sd(n_g) = 8.25$ . (b) Crépon et al. (2013); $n = 21,431$ ; $G = 235$ ; $n / G = 91.2$"
  },
  {
    "figure_id": "F408",
    "report_id": "R045",
    "label": "Figure 1",
    "context": "Figure 1: Distribution of cluster sizes in six partial population experiments (a) This paper; $n = 68,808$ ; $G = 3,982$ ; $n / G = 17.3$ ; $sd(n_g) = 8.25$ . (b) Crépon et al. (2013); $n = 21,431$ ; $G = 235$ ; $n / G = 91.2$"
  },
  {
    "figure_id": "F409",
    "report_id": "R045",
    "label": "Figure 2",
    "context": "Figure 2: Power functions - numerical illustration"
  },
  {
    "figure_id": "F410",
    "report_id": "R045",
    "label": "Figure 2",
    "context": "Figure 2: Power functions - numerical illustration Notes: This figure illustrates how ignoring heterogeneity can result in severely underpowered experiments. We consider the simple setting of a cluster RCT with a few “large” clu"
  },
  {
    "figure_id": "F411",
    "report_id": "R045",
    "label": "Figure 2",
    "context": "Figure 3: Direct and spillover effects on property tax payments in high-saturation blocks Direct Effects Treated vs. Pure Control"
  },
  {
    "figure_id": "F412",
    "report_id": "R045",
    "label": "Figure 3",
    "context": "Figure 3: Direct and spillover effects on property tax payments in high-saturation blocks Direct Effects Treated vs. Pure Control Spillover Effects Untreated vs. Pure Control Above Median Compliance"
  },
  {
    "figure_id": "F413",
    "report_id": "R045",
    "label": "Figure 1",
    "context": "Figure A.5: Distribution of payment date for treated, untreated, and pure control (October 2020 billing period) (a) Treated vs. Pure Control (b) Untreated vs. Pure Control Notes: These figures show the fraction of individuals paying the October 2020 bill befor"
  },
  {
    "figure_id": "F414",
    "report_id": "R045",
    "label": "Figure 1",
    "context": "Figure A.5: Distribution of payment date for treated, untreated, and pure control (October 2020 billing period) (a) Treated vs. Pure Control (b) Untreated vs. Pure Control Notes: These figures show the fraction of individuals paying the October 2020 bill befor"
  },
  {
    "figure_id": "F415",
    "report_id": "R045",
    "label": "Figure 3",
    "context": "Finally, for completeness, we also study the relationship between payment rates and exposure to adjacent treated blocks in blocks where 80% of the units were treated, again for the 100-meter buffer. The results of this exercise are reported in Figure B.14. The"
  },
  {
    "figure_id": "F416",
    "report_id": "R045",
    "label": "Figure 1",
    "context": "(a) 2018 vs 2019 (b) 2019 vs 2020 Notes: These figures show compliance in the first 9 billing periods of the year. For each block, we compute the share of total bills paid out of 9. Panel (a) compares 2018 and 2019, and panel (b) compares 2019 and 2020. We res"
  },
  {
    "figure_id": "F417",
    "report_id": "R046",
    "label": "Figure 1",
    "context": "June 30, 2022. $^{15}$ As such, approximately three in each four Ukrainian refugee students in secondary school age were not enrolled in Italian schools in academic year 2021-22. Analysis of MoE data covering academic years 2022-23 through 2023-24 highlights a"
  },
  {
    "figure_id": "F418",
    "report_id": "R046",
    "label": "Figure 3",
    "context": "On average, Ukrainian students miss 46 school days per year in 2022-23, 18 days more than Italians. In upper secondary schools, Ukrainian refugee students exhibit twice the absenteeism of their Italian peers. Italian students miss half as many days (23 days) o"
  },
  {
    "figure_id": "F419",
    "report_id": "R046",
    "label": "Figure 4",
    "context": "## Lower test score performance The evidence suggests that Ukrainian refugees in Italy face important learning gaps across all subjects. Figure 4 reports the INVALIDSI test scores by topic and category of students. $^{23}$ The educational disparity is particul"
  },
  {
    "figure_id": "F420",
    "report_id": "R046",
    "label": "Figure 4",
    "context": "## Lower test score performance The evidence suggests that Ukrainian refugees in Italy face important learning gaps across all subjects. Figure 4 reports the INVALIDSI test scores by topic and category of students. $^{23}$ The educational disparity is particul"
  },
  {
    "figure_id": "F421",
    "report_id": "R046",
    "label": "Figure 4",
    "context": "The evidence suggests that Ukrainian refugees in Italy face important learning gaps across all subjects. Figure 4 reports the INVALIDSI test scores by topic and category of students. $^{23}$ The educational disparity is particularly pronounced between Ukrainia"
  },
  {
    "figure_id": "F422",
    "report_id": "R046",
    "label": "Figure 4",
    "context": "39 points less, and recent migrants score 24 points less than other students, highlighting language as a likely barrier in the learning process."
  },
  {
    "figure_id": "F423",
    "report_id": "R046",
    "label": "Figure 5",
    "context": "## Track enrollment and recommendation Ukrainian students are less likely than Italians to enroll in high track education. Figure 5 shows that the rate of Ukrainian refugees (74%) enrolled in the High Track is much lower than that of Italians (84%) but higher "
  },
  {
    "figure_id": "F424",
    "report_id": "R046",
    "label": "Figure 6",
    "context": "Uncertainty about the future may impact refugees' connectedness to Italy, including to its education system. Figure 6 presents the statistics on aspirations and connectedness to Ukraine and Italy for caregivers and children. Displaced Ukrainians are not only u"
  },
  {
    "figure_id": "F425",
    "report_id": "R047",
    "label": "Figure 1",
    "context": "Figure 1: SMS Delivery Rates by Treatment Group ## Appendix ## SMS on long-term benefits of the program Another type of SMS, emphasizing the long-term benefits of the program, was sent to either youth only or youth and their con"
  },
  {
    "figure_id": "F426",
    "report_id": "R048",
    "label": "Figure 1",
    "context": "\\*\\*\\* significant at the 1% level, \\*\\* significant at the 5% level, \\* significant at the 10% level. Figure 1 Upward mobility, by country and parent (1980s birth cohort) Note: This figure plots the upward mobility gap by parent for the 1980s birth cohort. Th"
  },
  {
    "figure_id": "F427",
    "report_id": "R048",
    "label": "Figure 1",
    "context": "\\*\\*\\* significant at the 1% level, \\*\\* significant at the 5% level, \\* significant at the 10% level. Figure 1 Upward mobility, by country and parent (1980s birth cohort) Note: This figure plots the upward mobility gap by parent for the 1980s birth cohort. Th"
  },
  {
    "figure_id": "F428",
    "report_id": "R048",
    "label": "Figure 2",
    "context": "Note: This figure plots the upward mobility gap by parent for the 1980s birth cohort. The vertical axis plots the value calculated with respect to fathers, while the horizontal axis plots the value calculated with respect to mothers. The 45 degree line is plot"
  },
  {
    "figure_id": "F429",
    "report_id": "R048",
    "label": "Figure 2",
    "context": "Figure 2 Correlation between share of upward movers and upward education gap, by country (1980s birth cohort) Note: The figure is based on data from the Life in Transition Survey (Europe and Central Asia) and the GDIM (remaining regions of the world). Figure 3"
  },
  {
    "figure_id": "F430",
    "report_id": "R048",
    "label": "Figure 3",
    "context": "Figure 3 Average upward mobility (based on mothers' education), by birth cohort Note: The figure is based on data from the Life in Transition Survey (Europe and Central Asia) and the GDIM (remaining regions of the world). Thick lines indicate regional medians "
  },
  {
    "figure_id": "F431",
    "report_id": "R048",
    "label": "Figure 5",
    "context": "Note: The figure is based on data from the Life in Transition Survey (Europe and Central Asia) and the GDIM (remaining regions of the world). Thick lines indicate regional medians Grey lines plot values for individual countries. Figure 5 Average upward educati"
  },
  {
    "figure_id": "F432",
    "report_id": "R048",
    "label": "Figure 6",
    "context": "Note: The figure is based on data from the Life in Transition Survey (Europe and Central Asia) and the GDIM (remaining regions of the world). Thick lines indicate regional medians Grey lines plot values for individual countries. Figure 6 Average upward mobilit"
  },
  {
    "figure_id": "F433",
    "report_id": "R048",
    "label": "Figure 6",
    "context": "Figure 6 Average upward mobility into higher education (based on mothers' education), by birth cohort Note: The figure is based on data from the Life in Transition Survey (Europe and Central Asia) and the GDIM (remaining regions of the world). Thick lines indi"
  },
  {
    "figure_id": "F434",
    "report_id": "R049",
    "label": "Figure 1",
    "context": "Figure 1: Adoption timeline of fiscal rules The academic literature posits the origin of fiscal rules on the need to foster fiscal discipline and ensure debt remains on a sustainable path (Wyplosz 2013; Kopits and Symansky 1998)"
  },
  {
    "figure_id": "F435",
    "report_id": "R049",
    "label": "Figure 2",
    "context": "Figure 2: Dynamic effects of fiscal rule adoption Notes: The figure presents the impulse response function of the primary balance to the adoption of a fiscal rule, with the rule(s) adopted at year h = 0. The blue line shows the"
  },
  {
    "figure_id": "F436",
    "report_id": "R049",
    "label": "Figure 3",
    "context": "Figure 3: Impulse responses: advanced economies vs. EMDEs (b) EMDEs (c) EMDEs with strong institutions (d) EMDEs with weak institutions"
  },
  {
    "figure_id": "F437",
    "report_id": "R049",
    "label": "Figure 3",
    "context": "Figure 3: Impulse responses: advanced economies vs. EMDEs (b) EMDEs (c) EMDEs with strong institutions (d) EMDEs with weak institutions Notes: See notes Figure 2. The analysis is based on 108 countries; the number of obser"
  },
  {
    "figure_id": "F438",
    "report_id": "R049",
    "label": "Figure 3",
    "context": "Figure 3: Impulse responses: advanced economies vs. EMDEs (b) EMDEs (c) EMDEs with strong institutions (d) EMDEs with weak institutions Notes: See notes Figure 2. The analysis is based on 108 countries; the number of obser"
  },
  {
    "figure_id": "F439",
    "report_id": "R049",
    "label": "Figure 2",
    "context": "(b) EMDEs (c) EMDEs with strong institutions (d) EMDEs with weak institutions Notes: See notes Figure 2. The analysis is based on 108 countries; the number of observations included in each regression ranges between 1,807 and 1,817. Figure 3, panel (b), shows a"
  },
  {
    "figure_id": "F440",
    "report_id": "R049",
    "label": "Figure 3",
    "context": "Figure 4: Impulse responses: commodity importers vs. commodity exporters. (a) Commodity importers (b) Commodity exporters (c) Commodity exporters with strong institutions (d) Commodity exporters with weak institutions"
  },
  {
    "figure_id": "F441",
    "report_id": "R049",
    "label": "Figure 4",
    "context": "Figure 4: Impulse responses: commodity importers vs. commodity exporters. (a) Commodity importers (b) Commodity exporters (c) Commodity exporters with strong institutions (d) Commodity exporters with weak institutions Note"
  },
  {
    "figure_id": "F442",
    "report_id": "R049",
    "label": "Figure 4",
    "context": "Figure 4: Impulse responses: commodity importers vs. commodity exporters. (a) Commodity importers (b) Commodity exporters (c) Commodity exporters with strong institutions (d) Commodity exporters with weak institutions Note"
  },
  {
    "figure_id": "F443",
    "report_id": "R049",
    "label": "Figure 2",
    "context": "(b) Commodity exporters (c) Commodity exporters with strong institutions (d) Commodity exporters with weak institutions Notes: See notes Figure 2. The analysis is based on 108 countries; the number of observations included in each regression ranges between 1,8"
  },
  {
    "figure_id": "F444",
    "report_id": "R049",
    "label": "Figure 5",
    "context": "Figure 6: Impulse responses conditional on the state of the economy (a) Strong state of the economy"
  },
  {
    "figure_id": "F445",
    "report_id": "R049",
    "label": "Figure 6",
    "context": "Figure 6: Impulse responses conditional on the state of the economy (a) Strong state of the economy (b) Weak state of the economy (c) Strong state of the economy—Strong institutions (d) Weak state of the economy—Strong insti"
  },
  {
    "figure_id": "F446",
    "report_id": "R049",
    "label": "Figure 6",
    "context": "Figure 6: Impulse responses conditional on the state of the economy (a) Strong state of the economy (b) Weak state of the economy (c) Strong state of the economy—Strong institutions (d) Weak state of the economy—Strong insti"
  },
  {
    "figure_id": "F447",
    "report_id": "R049",
    "label": "Figure 2",
    "context": "(a) Strong state of the economy (b) Weak state of the economy (c) Strong state of the economy—Strong institutions (d) Weak state of the economy—Strong institutions Notes: See notes Figure 2. The analysis is based on 108 countries; the number of observations in"
  },
  {
    "figure_id": "F448",
    "report_id": "R049",
    "label": "Figure 2",
    "context": "(b) Weak state of the economy (c) Strong state of the economy—Strong institutions (d) Weak state of the economy—Strong institutions Notes: See notes Figure 2. The analysis is based on 108 countries; the number of observations in each regression ranges from 1,7"
  },
  {
    "figure_id": "F449",
    "report_id": "R049",
    "label": "Figure 7",
    "context": "Figure 8: Impulse responses conditional on fiscal regime"
  },
  {
    "figure_id": "F450",
    "report_id": "R049",
    "label": "Figure 7",
    "context": "Figure 8: Impulse responses conditional on fiscal regime Notes: See notes Figure 2. The analysis is based on 107 countries; the number of observations in each regression ranges from 1,794 to 1,803. ## 5.3. Political landscape"
  },
  {
    "figure_id": "F451",
    "report_id": "R049",
    "label": "Figure 5",
    "context": "Figure 8: Impulse responses conditional on fiscal regime Notes: See notes Figure 2. The analysis is based on 107 countries; the number of observations in each regression ranges from 1,794 to 1,803. ## 5.3. Political landscape"
  },
  {
    "figure_id": "F452",
    "report_id": "R049",
    "label": "Figure 9",
    "context": "Figure 10: Impulse responses conditional on political conditions (a) Low degree of political power"
  },
  {
    "figure_id": "F453",
    "report_id": "R049",
    "label": "Figure 5",
    "context": "Figure 10: Impulse responses conditional on political conditions (a) Low degree of political power (b) High degree of political power (c) Low degree of political power—Strong institutions (d) High degree of political power—St"
  },
  {
    "figure_id": "F454",
    "report_id": "R049",
    "label": "Figure 10",
    "context": "Figure 10: Impulse responses conditional on political conditions (a) Low degree of political power (b) High degree of political power (c) Low degree of political power—Strong institutions (d) High degree of political power—St"
  },
  {
    "figure_id": "F455",
    "report_id": "R049",
    "label": "Figure 10",
    "context": "Figure 10: Impulse responses conditional on political conditions (a) Low degree of political power (b) High degree of political power (c) Low degree of political power—Strong institutions (d) High degree of political power—St"
  },
  {
    "figure_id": "F456",
    "report_id": "R049",
    "label": "Figure 2",
    "context": "(b) High degree of political power (c) Low degree of political power—Strong institutions (d) High degree of political power—Strong institutions Notes: See notes Figure 2. The analysis is based on 108 countries; the number of observations in each regression ran"
  },
  {
    "figure_id": "F457",
    "report_id": "R049",
    "label": "Figure 11",
    "context": "Figure 11: Robustness analyses (a) Split-sample jackknife estimator (b) Clean-control condition (c) AIPW estimates (d) Cyclically adjusted primary balance"
  },
  {
    "figure_id": "F458",
    "report_id": "R049",
    "label": "Figure 11",
    "context": "Figure 11: Robustness analyses (a) Split-sample jackknife estimator (b) Clean-control condition (c) AIPW estimates (d) Cyclically adjusted primary balance Notes: See text and notes Figure 2. Across all panels, the regressio"
  },
  {
    "figure_id": "F459",
    "report_id": "R049",
    "label": "Figure 11",
    "context": "Figure 11: Robustness analyses (a) Split-sample jackknife estimator (b) Clean-control condition (c) AIPW estimates (d) Cyclically adjusted primary balance Notes: See text and notes Figure 2. Across all panels, the regressio"
  },
  {
    "figure_id": "F460",
    "report_id": "R049",
    "label": "Figure 2",
    "context": "(b) Clean-control condition (c) AIPW estimates (d) Cyclically adjusted primary balance Notes: See text and notes Figure 2. Across all panels, the regression includes 108 countries. The number of observations varies as follows: panel (a) ranges from 1,807 to 1,"
  },
  {
    "figure_id": "F461",
    "report_id": "R049",
    "label": "Figure 2",
    "context": "## Appendix 1 Figure A1: Impulse responses of primary balances, national vs. supranational rules (a) National rules (b) Supranational rules Notes: See notes Figure 2. The regression includes 108 countries, and the number of observations ranges from 1,807 to 1,"
  },
  {
    "figure_id": "F462",
    "report_id": "R049",
    "label": "Figure 2",
    "context": "Figure A1: Impulse responses of primary balances, national vs. supranational rules (a) National rules (b) Supranational rules Notes: See notes Figure 2. The regression includes 108 countries, and the number of observations ranges from 1,807 to 1,817. Figure A2"
  },
  {
    "figure_id": "F463",
    "report_id": "R049",
    "label": "Figure 2",
    "context": "(a) National rules (b) Supranational rules Notes: See notes Figure 2. The regression includes 108 countries, and the number of observations ranges from 1,807 to 1,817. Figure A2: Overlap check: empirical distributions of the treatment propensity score Notes: S"
  },
  {
    "figure_id": "F464",
    "report_id": "R050",
    "label": "Figure 1",
    "context": "Figure 1: Performance of country-level asset wealth index predictions. a. Performance comparison for four countries across four different machine learning methods trained on various fractions of the census extract. Negative $R^{2}"
  },
  {
    "figure_id": "F465",
    "report_id": "R050",
    "label": "Figure 1",
    "context": "Figure 1: Performance of country-level asset wealth index predictions. a. Performance comparison for four countries across four different machine learning methods trained on various fractions of the census extract. Negative $R^{2}"
  },
  {
    "figure_id": "F466",
    "report_id": "R050",
    "label": "Figure 1",
    "context": "Figure 1: Performance of country-level asset wealth index predictions. a. Performance comparison for four countries across four different machine learning methods trained on various fractions of the census extract. Negative $R^{2}"
  },
  {
    "figure_id": "F467",
    "report_id": "R050",
    "label": "Figure 1",
    "context": "Figure 2: Maps of country-level predicted asset wealth index. a. Country-level wealth asset map for Malawi in 2018. b. Country-level wealth asset map for Mozambique in 2017. c. Country-level wealth asset map for Madagascar in 2018"
  },
  {
    "figure_id": "F468",
    "report_id": "R050",
    "label": "Figure 1",
    "context": "Figure 2: Maps of country-level predicted asset wealth index. a. Country-level wealth asset map for Malawi in 2018. b. Country-level wealth asset map for Mozambique in 2017. c. Country-level wealth asset map for Madagascar in 2018"
  },
  {
    "figure_id": "F469",
    "report_id": "R050",
    "label": "Figure 1",
    "context": "Figure 2: Maps of country-level predicted asset wealth index. a. Country-level wealth asset map for Malawi in 2018. b. Country-level wealth asset map for Mozambique in 2017. c. Country-level wealth asset map for Madagascar in 2018"
  },
  {
    "figure_id": "F470",
    "report_id": "R050",
    "label": "Figure 2",
    "context": "Figure 2: Maps of country-level predicted asset wealth index. a. Country-level wealth asset map for Malawi in 2018. b. Country-level wealth asset map for Mozambique in 2017. c. Country-level wealth asset map for Madagascar in 2018"
  },
  {
    "figure_id": "F471",
    "report_id": "R050",
    "label": "Figure 3",
    "context": "Figure 3: Performance of country-level predictions of decadal change in asset wealth index. a. Performance comparison for two countries across three machine learning methods trained on various fractions of the census extract. Nega"
  },
  {
    "figure_id": "F472",
    "report_id": "R050",
    "label": "Figure 3",
    "context": "Figure 3: Performance of country-level predictions of decadal change in asset wealth index. a. Performance comparison for two countries across three machine learning methods trained on various fractions of the census extract. Nega"
  },
  {
    "figure_id": "F473",
    "report_id": "R050",
    "label": "Figure 3",
    "context": "Figure 3: Performance of country-level predictions of decadal change in asset wealth index. a. Performance comparison for two countries across three machine learning methods trained on various fractions of the census extract. Nega"
  },
  {
    "figure_id": "F474",
    "report_id": "R050",
    "label": "Figure 3",
    "context": "Figure 3: Performance of country-level predictions of decadal change in asset wealth index. a. Performance comparison for two countries across three machine learning methods trained on various fractions of the census extract. Nega"
  },
  {
    "figure_id": "F475",
    "report_id": "R050",
    "label": "Figure 4",
    "context": "Figure 4: Performance of city-level asset wealth index prediction. a. Performance comparison for two cities across four different machine learning methods trained on various fractions of the census. b. Performance comparison betwe"
  },
  {
    "figure_id": "F476",
    "report_id": "R050",
    "label": "Figure 4",
    "context": "Figure 4: Performance of city-level asset wealth index prediction. a. Performance comparison for two cities across four different machine learning methods trained on various fractions of the census. b. Performance comparison betwe"
  },
  {
    "figure_id": "F477",
    "report_id": "R050",
    "label": "Figure 4",
    "context": "Figure 4: Performance of city-level asset wealth index prediction. a. Performance comparison for two cities across four different machine learning methods trained on various fractions of the census. b. Performance comparison betwe"
  },
  {
    "figure_id": "F478",
    "report_id": "R050",
    "label": "Figure 5",
    "context": "Figure 5: An example of satellite image with geospatial features and asset wealth index label. This is a case of a country-level training sample. systematic observations from $[14]$ , we choose SwinV2-T $[19]$ as a representative"
  },
  {
    "figure_id": "F479",
    "report_id": "R051",
    "label": "Figure 1",
    "context": "33. Bain R, Johnston R, Khan S, Hancioglu A, Slaymaker T. Monitoring Drinking Water Quality in Nationally Representative Household Surveys in Low- and Middle-Income Countries: Cross-Sectional Analysis of 27 Multiple Indicator Cluster Surveys 2014–2020. Environ"
  },
  {
    "figure_id": "F480",
    "report_id": "R051",
    "label": "Figure 1",
    "context": "## Figures Figure 1. Trial profile Figure 2. Distribution of length-for-age Z-scores, intervention and control groups ## Supporting Information"
  },
  {
    "figure_id": "F481",
    "report_id": "R052",
    "label": "Figure 1",
    "context": "Yusuf, S., Nabeshima, K., & Perkins, D. H. (2006). Under New Ownership: Privatizing China's State-Owned Enterprises. Stanford University Press."
  },
  {
    "figure_id": "F482",
    "report_id": "R052",
    "label": "Figure 1",
    "context": "https://www.globalpetrolprices.com Quarterly electricity price, businesses rate (country level) Figure 1. Average Labor Productivity, Sales, and Employment Figure 2. Energy prices Figure 3a. Explicit subsidies to petroleum Figure 3b. Explicit subsidies to elec"
  },
  {
    "figure_id": "F483",
    "report_id": "R052",
    "label": "Figure 1",
    "context": "Figure 1. Average Labor Productivity, Sales, and Employment Figure 2. Energy prices Figure 3a. Explicit subsidies to petroleum Figure 3b. Explicit subsidies to electricity"
  },
  {
    "figure_id": "F484",
    "report_id": "R052",
    "label": "Figure 2",
    "context": "Figure 2. Energy prices Figure 3a. Explicit subsidies to petroleum Figure 3b. Explicit subsidies to electricity Robust standard errors in parentheses"
  },
  {
    "figure_id": "F485",
    "report_id": "R053",
    "label": "Figure 8",
    "context": "## 5.2.1 Experimental design We estimate the effects of personalized tax letters on current and subsequent property tax payments for women and men by leveraging a large-scale field experiment conducted by Cruces et al. (2023) in Tres de Febrero in October 2020"
  },
  {
    "figure_id": "F486",
    "report_id": "R053",
    "label": "Figure 1",
    "context": "Figure 3: Assessed property value by gender, 2018"
  },
  {
    "figure_id": "F487",
    "report_id": "R053",
    "label": "Figure 1",
    "context": "Figure 4: Tax gap by gender, 2019"
  },
  {
    "figure_id": "F488",
    "report_id": "R053",
    "label": "Figure 2",
    "context": "Figure 4: Tax gap by gender, 2019 Figure 5: Bills paid on-time, 2019"
  },
  {
    "figure_id": "F489",
    "report_id": "R053",
    "label": "Figure 3",
    "context": "Figure 6: Effective tax rates, 2019"
  },
  {
    "figure_id": "F490",
    "report_id": "R053",
    "label": "Figure 4",
    "context": "Figure 7: Effective tax rates, by gender, 2019"
  },
  {
    "figure_id": "F491",
    "report_id": "R053",
    "label": "Figure 5",
    "context": "Figure 8: Property tax compliance: women and men respond similarly to personalized tax letters"
  },
  {
    "figure_id": "F492",
    "report_id": "R053",
    "label": "Figure 6",
    "context": "Figure 8: Property tax compliance: women and men respond similarly to personalized tax letters Timely payments Timely and late"
  },
  {
    "figure_id": "F493",
    "report_id": "R053",
    "label": "Figure 9",
    "context": "Figure 9: Property tax compliance: men respond earlier to the letter, but women catch up (a) Distribution of payment date for women and men (October 2020 bill)"
  },
  {
    "figure_id": "F494",
    "report_id": "R053",
    "label": "Figure 9",
    "context": "Figure 9: Property tax compliance: men respond earlier to the letter, but women catch up (a) Distribution of payment date for women and men (October 2020 bill) (b) Treated vs Control (October 2020 bill)"
  },
  {
    "figure_id": "F495",
    "report_id": "R053",
    "label": "Figure 9",
    "context": "Figure 10: Property tax compliance by quintiles and gender (a) Timely payment rates by quintiles"
  },
  {
    "figure_id": "F496",
    "report_id": "R053",
    "label": "Figure 9",
    "context": "Figure 10: Property tax compliance by quintiles and gender (a) Timely payment rates by quintiles (b) Treated vs Control"
  },
  {
    "figure_id": "F497",
    "report_id": "R053",
    "label": "Figure 10",
    "context": "Figure 10: Property tax compliance by quintiles and gender (a) Timely payment rates by quintiles (b) Treated vs Control Notes: These figures show the effect of the communication campaign on payment rates by quintiles of assesse"
  },
  {
    "figure_id": "F498",
    "report_id": "R053",
    "label": "Figure 10",
    "context": "Figure 10: Property tax compliance by quintiles and gender (a) Timely payment rates by quintiles (b) Treated vs Control Notes: These figures show the effect of the communication campaign on payment rates by quintiles of assesse"
  },
  {
    "figure_id": "F499",
    "report_id": "R053",
    "label": "Figure 2",
    "context": "SUPPLEMENTARY MATERIALS FOR: \"EXPLORING THE GENDER DIVIDE IN REAL ESTATE OWNERSHIP AND PROPERTY TAX COMPLIANCE\" ## A Residential ownership in Tres de Febrero Based on the 2021 ARBA cadaster, the municipality boasts approximately 140,000 registered properties. "
  },
  {
    "figure_id": "F500",
    "report_id": "R053",
    "label": "Figure 2",
    "context": "Figure A.1: Number of residential properties Note: This map presents the number of residential properties at the block \"manzana\" Level in Tres de Febrero 2021 ARBA register. Figure A.2: Assessed values for residential properties, 2018 Note: This figure present"
  },
  {
    "figure_id": "F501",
    "report_id": "R053",
    "label": "Figure 9",
    "context": "Figure C.7: Example of the intervention letter Figure C.8: Property tax compliance: no effect for the placebo bill of July 2020 (a) Distribution of payment date for women and men (July 2020 bill) (b) Treated vs Control (July 2020 bill) Notes: Panel (a) shows t"
  },
  {
    "figure_id": "F502",
    "report_id": "R053",
    "label": "Figure 9",
    "context": "Figure C.8: Property tax compliance: no effect for the placebo bill of July 2020 (a) Distribution of payment date for women and men (July 2020 bill) (b) Treated vs Control (July 2020 bill) Notes: Panel (a) shows the fraction of men and women paying the July 20"
  },
  {
    "figure_id": "F503",
    "report_id": "R053",
    "label": "Figure 9",
    "context": "(b) Treated vs Control (July 2020 bill) Notes: Panel (a) shows the fraction of men and women paying the July 2020 bill before and after the due date (July 8th, 2020). The area of each histogram integrates into one. A larger bar on a particular date means that "
  },
  {
    "figure_id": "F504",
    "report_id": "R053",
    "label": "Figure 9",
    "context": "Notes: Panel (a) shows the fraction of men and women paying the July 2020 bill before and after the due date (July 8th, 2020). The area of each histogram integrates into one. A larger bar on a particular date means that the payment frequency of the correspondi"
  },
  {
    "figure_id": "F505",
    "report_id": "R054",
    "label": "Figure 1",
    "context": "Figure 1: Temperature Response Functions by GDP and Firm Size Vertical axes show changes in the logarithm of sales revenues. Horizontal axes show differences in current fiscal year temperatures compared to historical average tempe"
  },
  {
    "figure_id": "F506",
    "report_id": "R054",
    "label": "Figure 1",
    "context": "Figure 2: Temperature Response Functions by GDP and Firm Characteristics The top panel shows heterogeneity by firm age. The bottom shows heterogeneity by the proportion of sales that are direct exports. Vertical axes show changes"
  },
  {
    "figure_id": "F507",
    "report_id": "R054",
    "label": "Figure 1",
    "context": "Figure 3: Temperature Response Functions by GDP and Sectoral Attributes Vertical axes show changes in the logarithm of sales revenues. Horizontal axes show differences in current fiscal year temperatures compared to historical ave"
  },
  {
    "figure_id": "F508",
    "report_id": "R054",
    "label": "Figure 1",
    "context": "Figure 4: Temperature Response Functions by GDP and Attributes of Business Environment. The top panel shows heterogeneity by access to finance. The bottom panel shows heterogeneity by the regulatory environment. Vertical axes show"
  },
  {
    "figure_id": "F509",
    "report_id": "R054",
    "label": "Figure 1",
    "context": "Figure 5: Temperature Response Functions by GDP and Quality of Public Goods The top panel shows heterogeneity by the quality of electricity access. The bottom panel shows heterogeneity by security. Vertical axes show changes in th"
  },
  {
    "figure_id": "F510",
    "report_id": "R054",
    "label": "Figure 1",
    "context": "Figure 5: Temperature Response Functions by GDP and Quality of Public Goods The top panel shows heterogeneity by the quality of electricity access. The bottom panel shows heterogeneity by security. Vertical axes show changes in th"
  },
  {
    "figure_id": "F511",
    "report_id": "R054",
    "label": "Figure 2",
    "context": "Figure 5: Temperature Response Functions by GDP and Quality of Public Goods The top panel shows heterogeneity by the quality of electricity access. The bottom panel shows heterogeneity by security. Vertical axes show changes in th"
  },
  {
    "figure_id": "F512",
    "report_id": "R055",
    "label": "Figure 1",
    "context": "This paper is set against the backdrop of the military takeover of the Government of Myanmar since 2021, which was followed by high levels of violent conflict and economic slowdown. We explore the factors prompting high-skilled youth to migrate abroad for work"
  },
  {
    "figure_id": "F513",
    "report_id": "R055",
    "label": "Figure 2",
    "context": "Standard errors clustered at the township level in parentheses. Controls include individual demographic and labor market characteristics including occupation, sector of employment, and field of study. 5.2.2 Instrumental Variables Estimation We employ Instrumen"
  },
  {
    "figure_id": "F514",
    "report_id": "R056",
    "label": "Figure 1",
    "context": "Figure 1: Sectoral Employment Transitions by Gender (a) Transitions Across Sectors: Men (b) Transitions Across Sectors: Women (c) (De)Industrialization: Men (d) (De)Industrialization: Women"
  },
  {
    "figure_id": "F515",
    "report_id": "R056",
    "label": "Figure 1",
    "context": "Figure 1: Sectoral Employment Transitions by Gender (a) Transitions Across Sectors: Men (b) Transitions Across Sectors: Women (c) (De)Industrialization: Men (d) (De)Industrialization: Women"
  },
  {
    "figure_id": "F516",
    "report_id": "R056",
    "label": "Figure 2",
    "context": "Figure 2: Occupational Employment Shares by Gender and by Sector (a) Transition Across Occupations: Men (b) Transition Across Occupations: Women More generally, sectors employ occupations in different proportions, creating a d"
  },
  {
    "figure_id": "F517",
    "report_id": "R056",
    "label": "Figure 2",
    "context": "Figure 2: Occupational Employment Shares by Gender and by Sector (a) Transition Across Occupations: Men (b) Transition Across Occupations: Women More generally, sectors employ occupations in different proportions, creating a d"
  },
  {
    "figure_id": "F518",
    "report_id": "R056",
    "label": "Figure 3",
    "context": "Figure 3: H-Index of Gender Segregation across Sectors and Occupations (a) Aggregate Index (b) Fraction Explained Within Sector ## 2.5 Gender Gaps within Countries over Time We next use a core sample of six large economies – I"
  },
  {
    "figure_id": "F519",
    "report_id": "R056",
    "label": "Figure 3",
    "context": "Figure 3: H-Index of Gender Segregation across Sectors and Occupations (a) Aggregate Index (b) Fraction Explained Within Sector ## 2.5 Gender Gaps within Countries over Time We next use a core sample of six large economies – I"
  },
  {
    "figure_id": "F520",
    "report_id": "R056",
    "label": "Figure 4",
    "context": "Figure 4: Effect of Gender Barriers on Sectoral and Occupational Employment Shares (a) Sectoral Population Shares: All (b) Sectoral Population Shares: Women (c) Sectoral Employment Shares (d) Occupational Population Shares"
  },
  {
    "figure_id": "F521",
    "report_id": "R056",
    "label": "Figure 4",
    "context": "Figure 4: Effect of Gender Barriers on Sectoral and Occupational Employment Shares (a) Sectoral Population Shares: All (b) Sectoral Population Shares: Women (c) Sectoral Employment Shares (d) Occupational Population Shares"
  },
  {
    "figure_id": "F522",
    "report_id": "R057",
    "label": "Figure 1",
    "context": "Figure 1: Map of locations covered by survey by treatment and control wards ## 3.1 Tax Administrative Data Administrative data from the TRA was utilized to analyze the impact of the intervention on taxpayers' behavior. This data"
  },
  {
    "figure_id": "F523",
    "report_id": "R058",
    "label": "Figure 1",
    "context": "Figure 1: Density of log of per capita expenditure over time Note: i) Authors' estimation based on VHLSSs data Note: i) Authors' estimation based on VHLSSs data ## Supporting Information for review and online publication only"
  },
  {
    "figure_id": "F524",
    "report_id": "R058",
    "label": "Figure 1",
    "context": "Figure 1: Density of log of per capita expenditure over time Note: i) Authors' estimation based on VHLSSs data Note: i) Authors' estimation based on VHLSSs data ## Supporting Information for review and online publication only"
  },
  {
    "figure_id": "F525",
    "report_id": "R059",
    "label": "Figure 1",
    "context": "## 2 Data and Descriptive Analysis We used trade data from BACI (Gaulier and Zignago, 2010). $^{2}$ We used the import data of the selected countries from 1995 to 2021, covering 27 continuous years. The data contains information on the total values, quantities"
  },
  {
    "figure_id": "F526",
    "report_id": "R060",
    "label": "Figure 1",
    "context": "Figure 2: Road network in Belgian Congo, 1960 Maintenance of feeder roads in rural areas was by and large neglected, and rural populations were forced to rely on subsistence farming; underpaid government agents and local authoriti"
  },
  {
    "figure_id": "F527",
    "report_id": "R060",
    "label": "Figure 1",
    "context": "Figure 2: Road network in Belgian Congo, 1960 Maintenance of feeder roads in rural areas was by and large neglected, and rural populations were forced to rely on subsistence farming; underpaid government agents and local authoriti"
  },
  {
    "figure_id": "F528",
    "report_id": "R060",
    "label": "Figure 3",
    "context": "Figure 3: Political Violence in the DRC Notes: Figure shows the location of ACLED and UCDP events in the DRC. ## 3.2 A New Database of Road Investments First, we created a database of road transport projects relying on multiple"
  },
  {
    "figure_id": "F529",
    "report_id": "R060",
    "label": "Figure 4",
    "context": "Figure 4: Map of Geolocalized Projects One of the main concerns regarding the analysis of roads and violence is the self-selection of road projects into peaceful regions or peaceful periods in violent regions. Three arguments spea"
  },
  {
    "figure_id": "F530",
    "report_id": "R060",
    "label": "Figure 5",
    "context": "Figure 5: Roads and Violence at the Province Level Notes: Figure shows the log of armed conflict event totals per million inhabitants together with the log of completed road projects at the province level. Finally, we provide ev"
  },
  {
    "figure_id": "F531",
    "report_id": "R060",
    "label": "Figure 6",
    "context": "Figure 6: Example of satellite imagery aggregation Project 04 Segments Project 04 Segments (Zoomed) Notes: The road for one of the three projects is divided into segments of 10 km. Segments 180, 181, and 182 are highlighted in"
  },
  {
    "figure_id": "F532",
    "report_id": "R060",
    "label": "Figure 6",
    "context": "Figure 7: Satellite road quality inputs for the decay estimation 2012"
  },
  {
    "figure_id": "F533",
    "report_id": "R060",
    "label": "Figure 6",
    "context": "Figure 7: Satellite road quality inputs for the decay estimation Notes: A representation of classified road image tiles for road segments 180, 181, and 182 from different years. The edge of each segment is mar"
  },
  {
    "figure_id": "F534",
    "report_id": "R060",
    "label": "Figure 7",
    "context": "Figure 7: Satellite road quality inputs for the decay estimation Notes: A representation of classified road image tiles for road segments 180, 181, and 182 from different years. The edge of each segment is mar"
  },
  {
    "figure_id": "F535",
    "report_id": "R060",
    "label": "Figure 7",
    "context": "Figure 7: Satellite road quality inputs for the decay estimation Notes: A representation of classified road image tiles for road segments 180, 181, and 182 from different years. The edge of each segment is mar"
  },
  {
    "figure_id": "F536",
    "report_id": "R060",
    "label": "Figure 8",
    "context": "Figure 8: Mining Locations and Roads Notes: Mining locations for small artisanal mines and large projects together with road investments by international actors. ## 4 Roads and Armed Conflict ## 4.1 Hypothesis and Descriptive Ev"
  },
  {
    "figure_id": "F537",
    "report_id": "R060",
    "label": "Figure 5",
    "context": "Figure 10: Roads and Armed Conflict in North Kivu Notes: The Figure shows the number of violent events sourced from UCDP and the number of PRIO cells with a newly or recently (last year) completed road project for Nord-Kivu."
  },
  {
    "figure_id": "F538",
    "report_id": "R060",
    "label": "Figure 9",
    "context": "Figure 11: Road Stock and Armed Conflict in North Kivu Notes: The Figure shows the number of violent events sourced from UCDP and the road project Stock for North Kivu. A newly completed project takes a value of one. This value g"
  },
  {
    "figure_id": "F539",
    "report_id": "R060",
    "label": "Figure 10",
    "context": "Figure 11: Road Stock and Armed Conflict in North Kivu Notes: The Figure shows the number of violent events sourced from UCDP and the road project Stock for North Kivu. A newly completed project takes a value of one. This value g"
  },
  {
    "figure_id": "F540",
    "report_id": "R060",
    "label": "Figure 12",
    "context": "Figure 12: Roads and Events: PreMDiD Notes: Figure shows the effect of road completion at year 0 compared to a control group that is matched by violence prediction in year -1. Figure 13: Roads and Fatalities: PreMDiD Notes: Fig"
  },
  {
    "figure_id": "F541",
    "report_id": "R060",
    "label": "Figure 12",
    "context": "Figure 12: Roads and Events: PreMDiD Notes: Figure shows the effect of road completion at year 0 compared to a control group that is matched by violence prediction in year -1. Figure 13: Roads and Fatalities: PreMDiD Notes: Fig"
  },
  {
    "figure_id": "F542",
    "report_id": "R061",
    "label": "Figure 1",
    "context": "Figure 2: Trends in Non-Farm Employment by Gender"
  },
  {
    "figure_id": "F543",
    "report_id": "R061",
    "label": "Figure 1",
    "context": "Figure 2: Trends in Non-Farm Employment by Gender Notes: The above figures shows trends in non-farm employment categories and sectors, conditional on participation in the labour force, and disaggregated by gender. NSS survey r"
  },
  {
    "figure_id": "F544",
    "report_id": "R061",
    "label": "Figure 1",
    "context": "Figure 3: Trends in Non-Farm Employment by Gender and Secondary Education"
  },
  {
    "figure_id": "F545",
    "report_id": "R061",
    "label": "Figure 2",
    "context": "Figure 3: Trends in Non-Farm Employment by Gender and Secondary Education"
  },
  {
    "figure_id": "F546",
    "report_id": "R061",
    "label": "Figure 2",
    "context": "Figure 3: Trends in Non-Farm Employment by Gender and Secondary Education Notes: The above figures shows trends in non-farm employment categories and sectors, conditional on participation in the labour force, and disaggreg"
  },
  {
    "figure_id": "F547",
    "report_id": "R061",
    "label": "Figure 3",
    "context": "Figure 4: Trends in Household Monthly Per Capita Expenditures"
  },
  {
    "figure_id": "F548",
    "report_id": "R061",
    "label": "Figure 3",
    "context": "Figure 4: Trends in Household Monthly Per Capita Expenditures"
  },
  {
    "figure_id": "F549",
    "report_id": "R061",
    "label": "Figure 3",
    "context": "Figure 4: Trends in Household Monthly Per Capita Expenditures"
  },
  {
    "figure_id": "F550",
    "report_id": "R061",
    "label": "Figure 4",
    "context": "Figure 4: Trends in Household Monthly Per Capita Expenditures"
  },
  {
    "figure_id": "F551",
    "report_id": "R061",
    "label": "Figure 4",
    "context": "Figure 4: Trends in Household Monthly Per Capita Expenditures"
  },
  {
    "figure_id": "F552",
    "report_id": "R061",
    "label": "Figure 4",
    "context": "Figure 4: Trends in Household Monthly Per Capita Expenditures"
  },
  {
    "figure_id": "F553",
    "report_id": "R061",
    "label": "Figure 4",
    "context": "Figure 4: Trends in Household Monthly Per Capita Expenditures"
  },
  {
    "figure_id": "F554",
    "report_id": "R062",
    "label": "Figure 1",
    "context": "Figure 1. The impact of DSM on farmers' decision to purchase maize and wheat seeds, event study aggregation"
  },
  {
    "figure_id": "F555",
    "report_id": "R062",
    "label": "Figure 1",
    "context": "Figure 1. The impact of DSM on farmers' decision to purchase maize and wheat seeds, event study aggregation"
  },
  {
    "figure_id": "F556",
    "report_id": "R062",
    "label": "Figure 2",
    "context": "The results from the event-study (dynamic) aggregation on the quantity of maize and wheat seed purchased by farmers show coefficients similar to those from the cohort and survey year aggregations. DSM led to a 46 percent increase in the quantity of maize seed "
  },
  {
    "figure_id": "F557",
    "report_id": "R062",
    "label": "Figure 2",
    "context": "The results from the event-study (dynamic) aggregation on the quantity of maize and wheat seed purchased by farmers show coefficients similar to those from the cohort and survey year aggregations. DSM led to a 46 percent increase in the quantity of maize seed "
  },
  {
    "figure_id": "F558",
    "report_id": "R062",
    "label": "Figure 3",
    "context": "Figure 3. The impact of DSM on maize and wheat yields, event study aggregation (a) Maize (b) Wheat Given the lack of a significant impact of DSM on wheat seed purchases and productivity, we extend our analysis to examine whether DSM has any effect on seed purc"
  },
  {
    "figure_id": "F559",
    "report_id": "R062",
    "label": "Figure 3",
    "context": "Figure 3. The impact of DSM on maize and wheat yields, event study aggregation (a) Maize (b) Wheat Given the lack of a significant impact of DSM on wheat seed purchases and productivity, we extend our analysis to examine whether DSM has any effect on seed purc"
  },
  {
    "figure_id": "F560",
    "report_id": "R062",
    "label": "Figure 4",
    "context": "A related explanation for the differences in crop-specific outcomes stems from the historical evolution of DSM in Ethiopia. Even before the introduction of DSM, there was considerable accumulated experience in maize seed production and marketing, along with cl"
  },
  {
    "figure_id": "F561",
    "report_id": "R062",
    "label": "Figure 4",
    "context": "In fact, data on the DSM approach indicate that the initial emphasis was placed exclusively on maize beginning in 2011, with the expansion to wheat following in 2013 (Figure 4). The resulting supply response for maize occurred more rapidly than for wheat: wher"
  },
  {
    "figure_id": "F562",
    "report_id": "R064",
    "label": "Figure 1",
    "context": "Figure 1: Timeline of reform. Note: This timeline depicts the subsequent budget law postponements of the enforcement of the Corporate Income Tax (CIT) reform for Offshore firms, thus leaving the full exemption in place until 201"
  },
  {
    "figure_id": "F563",
    "report_id": "R064",
    "label": "Figure 2",
    "context": "Figure 2: Participation of offshore sector (a) Total firms (b) Total employment (c) Total revenue"
  },
  {
    "figure_id": "F564",
    "report_id": "R064",
    "label": "Figure 2",
    "context": "Figure 2: Participation of offshore sector (a) Total firms (b) Total employment (c) Total revenue (d) Total export value Note: These figures display the participation of offshore firms in several economic aggregates over t"
  },
  {
    "figure_id": "F565",
    "report_id": "R064",
    "label": "Figure 2",
    "context": "Figure 2: Participation of offshore sector (a) Total firms (b) Total employment (c) Total revenue (d) Total export value Note: These figures display the participation of offshore firms in several economic aggregates over t"
  },
  {
    "figure_id": "F566",
    "report_id": "R064",
    "label": "Figure 3",
    "context": "Figure 3: Composition of offshore firms - by sector (a) Number of firms"
  },
  {
    "figure_id": "F567",
    "report_id": "R064",
    "label": "Figure 3",
    "context": "Figure 3: Composition of offshore firms - by sector (a) Number of firms (b) Total Revenue (c) Total Employment Note: These figures display the composition of offshore firms by economic sectors. In panel (a) we present how fi"
  },
  {
    "figure_id": "F568",
    "report_id": "R064",
    "label": "Figure 3",
    "context": "Figure 3: Composition of offshore firms - by sector (a) Number of firms (b) Total Revenue (c) Total Employment Note: These figures display the composition of offshore firms by economic sectors. In panel (a) we present how fi"
  },
  {
    "figure_id": "F569",
    "report_id": "R064",
    "label": "Figure 3",
    "context": "Figure 3: Composition of offshore firms - by sector (a) Number of firms (b) Total Revenue (c) Total Employment Note: These figures display the composition of offshore firms by economic sectors. In panel (a) we present how fi"
  },
  {
    "figure_id": "F570",
    "report_id": "R064",
    "label": "Figure 4",
    "context": "Figure 4: Aggregate quantities (normalized) - Offshore versus Onshore (a) Total firms normalized (b) Normalized numbers of entrants (c) Normalized numbers of exiters"
  },
  {
    "figure_id": "F571",
    "report_id": "R064",
    "label": "Figure 4",
    "context": "Figure 4: Aggregate quantities (normalized) - Offshore versus Onshore (a) Total firms normalized (b) Normalized numbers of entrants (c) Normalized numbers of exiters (d) Number of employees - normalized"
  },
  {
    "figure_id": "F572",
    "report_id": "R064",
    "label": "Figure 4",
    "context": "Figure 4: Aggregate quantities (normalized) - Offshore versus Onshore (a) Total firms normalized (b) Normalized numbers of entrants (c) Normalized numbers of exiters (d) Number of employees - normalized (e) Total wage bi"
  },
  {
    "figure_id": "F573",
    "report_id": "R064",
    "label": "Figure 5",
    "context": "Figure 5: DID estimates: aggregate outcomes (Full sample & Manufacturing)"
  },
  {
    "figure_id": "F574",
    "report_id": "R064",
    "label": "Figure 5",
    "context": "Figure 5: DID estimates: aggregate outcomes (Full sample & Manufacturing) (a) Number of firms"
  },
  {
    "figure_id": "F575",
    "report_id": "R064",
    "label": "Figure 5",
    "context": "Figure 5: DID estimates: aggregate outcomes (Full sample & Manufacturing) (a) Number of firms (b) Entry (c) Exit"
  },
  {
    "figure_id": "F576",
    "report_id": "R064",
    "label": "Figure 5",
    "context": "Figure 5: DID estimates: aggregate outcomes (Full sample & Manufacturing) (a) Number of firms (b) Entry (c) Exit (d) Employment"
  },
  {
    "figure_id": "F577",
    "report_id": "R064",
    "label": "Figure 5",
    "context": "Figure 5: DID estimates: aggregate outcomes (Full sample & Manufacturing) (a) Number of firms (b) Entry (c) Exit (d) Employment (e) Wage bill"
  },
  {
    "figure_id": "F578",
    "report_id": "R064",
    "label": "Figure 7",
    "context": "Figure 6: Employment outcomes on the balanced sample - Offshore versus Onshore (a) Ln(Employees) (b) Firm has more than 2 employees (c) Firm has more than 5 employees"
  },
  {
    "figure_id": "F579",
    "report_id": "R064",
    "label": "Figure 7",
    "context": "Figure 6: Employment outcomes on the balanced sample - Offshore versus Onshore (a) Ln(Employees) (b) Firm has more than 2 employees (c) Firm has more than 5 employees (d) Firm has more than 10 employees"
  },
  {
    "figure_id": "F580",
    "report_id": "R064",
    "label": "Figure 6",
    "context": "Figure 6: Employment outcomes on the balanced sample - Offshore versus Onshore (a) Ln(Employees) (b) Firm has more than 2 employees (c) Firm has more than 5 employees (d) Firm has more than 10 employees Figure 7: Other out"
  },
  {
    "figure_id": "F581",
    "report_id": "R064",
    "label": "Figure 7",
    "context": "Figure 7: Other outcomes on the balanced sample - Offshore versus Onshore (a) Ln(wagebill)"
  },
  {
    "figure_id": "F582",
    "report_id": "R064",
    "label": "Figure 7",
    "context": "Figure 7: Other outcomes on the balanced sample - Offshore versus Onshore (a) Ln(wagebill) (b) $\\mathrm{Ln}(\\mathrm{Revenue})$ (c) $\\mathrm{Ln}(\\mathrm{Profits})$ Note: Firm-level DID obtained from estimating equation (3) on"
  },
  {
    "figure_id": "F583",
    "report_id": "R064",
    "label": "Figure 7",
    "context": "Figure 7: Other outcomes on the balanced sample - Offshore versus Onshore (a) Ln(wagebill) (b) $\\mathrm{Ln}(\\mathrm{Revenue})$ (c) $\\mathrm{Ln}(\\mathrm{Profits})$ Note: Firm-level DID obtained from estimating equation (3) on"
  },
  {
    "figure_id": "F584",
    "report_id": "R064",
    "label": "Figure 7",
    "context": "Figure 7: Other outcomes on the balanced sample - Offshore versus Onshore (a) Ln(wagebill) (b) $\\mathrm{Ln}(\\mathrm{Revenue})$ (c) $\\mathrm{Ln}(\\mathrm{Profits})$ Note: Firm-level DID obtained from estimating equation (3) on"
  },
  {
    "figure_id": "F585",
    "report_id": "R064",
    "label": "Figure 5",
    "context": "Figure A21: Honest DID - Industry-level impacts on Log(number of firms) (a) Original dynamic estimates (Fig 5a) (b) Manufacturing - average post-period (c) Manufacturing - last post-period (d) Full sample - average post-period (e) Full sample - last post-perio"
  },
  {
    "figure_id": "F586",
    "report_id": "R064",
    "label": "Figure 5",
    "context": "(a) Original dynamic estimates (Fig 5a) (b) Manufacturing - average post-period (c) Manufacturing - last post-period (d) Full sample - average post-period (e) Full sample - last post-period Note: Panel (a) reproduces Figure 5(a) in the main text, while remaini"
  },
  {
    "figure_id": "F587",
    "report_id": "R064",
    "label": "Figure 5",
    "context": "(b) Manufacturing - average post-period (c) Manufacturing - last post-period (d) Full sample - average post-period (e) Full sample - last post-period Note: Panel (a) reproduces Figure 5(a) in the main text, while remaining panels report results from the sensit"
  },
  {
    "figure_id": "F588",
    "report_id": "R064",
    "label": "Figure 5",
    "context": "(e) Full sample - last post-period Note: Panel (a) reproduces Figure 5(a) in the main text, while remaining panels report results from the sensitivity tests in Rambachan and Roth (2023) for the described outcomes in the industry-level analysis. Mbar refers to "
  },
  {
    "figure_id": "F589",
    "report_id": "R064",
    "label": "Figure 5",
    "context": "Note: Panel (a) reproduces Figure 5(a) in the main text, while remaining panels report results from the sensitivity tests in Rambachan and Roth (2023) for the described outcomes in the industry-level analysis. Mbar refers to multiples of the largest deviation "
  },
  {
    "figure_id": "F590",
    "report_id": "R065",
    "label": "Figure 1",
    "context": "Figure 2: AI Occupational Exposure by Country Income Group AI Occupation Exposure by Income group"
  },
  {
    "figure_id": "F591",
    "report_id": "R065",
    "label": "Figure 1",
    "context": "Figure 2: AI Occupational Exposure by Country Income Group AI Occupation Exposure by Income group Figure 3: AI Occupational Exposure by GNI per capita"
  },
  {
    "figure_id": "F592",
    "report_id": "R065",
    "label": "Figure 2",
    "context": "Figure 2: AI Occupational Exposure by Country Income Group AI Occupation Exposure by Income group Figure 3: AI Occupational Exposure by GNI per capita"
  },
  {
    "figure_id": "F593",
    "report_id": "R065",
    "label": "Figure 3",
    "context": "Figure 3: AI Occupational Exposure by GNI per capita We categorize the AIOE scores into four exposure levels (high, moderately high, moderately low and low exposure) and analyze these across country income groups and sub-groups"
  },
  {
    "figure_id": "F594",
    "report_id": "R065",
    "label": "Figure 3",
    "context": "Figure 3: AI Occupational Exposure by GNI per capita We categorize the AIOE scores into four exposure levels (high, moderately high, moderately low and low exposure) and analyze these across country income groups and sub-groups"
  },
  {
    "figure_id": "F595",
    "report_id": "R065",
    "label": "Figure 5",
    "context": "## 3.2. The role of worker characteristics in determining AI occupational exposure There is no clear difference in the age pattern across income groups. Younger workers, aged 15-24, tend to have left school earlier and are not employed in occupations with AI e"
  },
  {
    "figure_id": "F596",
    "report_id": "R065",
    "label": "Figure 5",
    "context": "There is no clear difference in the age pattern across income groups. Younger workers, aged 15-24, tend to have left school earlier and are not employed in occupations with AI exposure (Figure 5). This may be explained by the fact that workers who leave educat"
  },
  {
    "figure_id": "F597",
    "report_id": "R065",
    "label": "Figure 6",
    "context": "Figure 7: AI Exposure by Location and Country Income Level"
  },
  {
    "figure_id": "F598",
    "report_id": "R065",
    "label": "Figure 6",
    "context": "Figure 7: AI Exposure by Location and Country Income Level"
  },
  {
    "figure_id": "F599",
    "report_id": "R065",
    "label": "Figure 7",
    "context": "Figure 7: AI Exposure by Location and Country Income Level When analyzing the relationship between income group, exposure to AI in the workplace and education, two patterns emerge: In all countries, the more educated workers are"
  },
  {
    "figure_id": "F600",
    "report_id": "R065",
    "label": "Figure 7",
    "context": "Figure 7: AI Exposure by Location and Country Income Level When analyzing the relationship between income group, exposure to AI in the workplace and education, two patterns emerge: In all countries, the more educated workers are"
  },
  {
    "figure_id": "F601",
    "report_id": "R065",
    "label": "Figure 9",
    "context": "## 3.3. The importance of job choice for AI occupational exposure around the world High-skilled occupations are more exposed to AI than medium- and low-skilled occupations. The ILO defines high-skilled occupations as ISCO categories for \"Managers\", \"Profession"
  },
  {
    "figure_id": "F602",
    "report_id": "R065",
    "label": "Figure 10",
    "context": "Figure 11: AI Exposure by Electricity Access, Location and Country Income Level"
  },
  {
    "figure_id": "F603",
    "report_id": "R065",
    "label": "Figure 10",
    "context": "Figure 11: AI Exposure by Electricity Access, Location and Country Income Level ## 4. Conclusion This paper discusses the potential of artificial intelligence for the next generation of work. While most previous economic research"
  },
  {
    "figure_id": "F604",
    "report_id": "R065",
    "label": "Figure 12",
    "context": "Figure 12: AI occupation exposure for the 2- and 4-digit occupation codes ## AI occupation exposure information detail for 2 digit and 4 digit ISCO codes - Professionals • Technicians and associate professionals • Service and s"
  },
  {
    "figure_id": "F605",
    "report_id": "R065",
    "label": "Figure 12",
    "context": "Figure 12: AI occupation exposure for the 2- and 4-digit occupation codes ## AI occupation exposure information detail for 2 digit and 4 digit ISCO codes - Professionals • Technicians and associate professionals • Service and s"
  },
  {
    "figure_id": "F606",
    "report_id": "R065",
    "label": "Figure 13",
    "context": "Figure 13: AI exposure and industry sector AI Exposure by Industry Sector AI Occupation Exposure by Country"
  },
  {
    "figure_id": "F607",
    "report_id": "R065",
    "label": "Figure 13",
    "context": "Figure 13: AI exposure and industry sector AI Exposure by Industry Sector AI Occupation Exposure by Country Note: Results are population weighted and include workers aged 15 to 64"
  },
  {
    "figure_id": "F608",
    "report_id": "R066",
    "label": "Figure 1",
    "context": "Figure 3: Annual Rainfall Shocks and Household Expenditures"
  },
  {
    "figure_id": "F609",
    "report_id": "R066",
    "label": "Figure 1",
    "context": "Figure 3: Annual Rainfall Shocks and Household Expenditures"
  },
  {
    "figure_id": "F610",
    "report_id": "R066",
    "label": "Figure 1",
    "context": "Figure 3: Annual Rainfall Shocks and Household Expenditures"
  },
  {
    "figure_id": "F611",
    "report_id": "R066",
    "label": "Figure 3",
    "context": "Figure 3: Annual Rainfall Shocks and Household Expenditures Notes: This figure shows the raw correlation between annual rainfall incidence (standardized) and household per capita expenditures. The horizontal axis is divide"
  },
  {
    "figure_id": "F612",
    "report_id": "R066",
    "label": "Figure 3",
    "context": "Figure 3: Annual Rainfall Shocks and Household Expenditures Notes: This figure shows the raw correlation between annual rainfall incidence (standardized) and household per capita expenditures. The horizontal axis is divide"
  },
  {
    "figure_id": "F613",
    "report_id": "R066",
    "label": "Figure 3",
    "context": "Figure 3: Annual Rainfall Shocks and Household Expenditures Notes: This figure shows the raw correlation between annual rainfall incidence (standardized) and household per capita expenditures. The horizontal axis is divide"
  },
  {
    "figure_id": "F614",
    "report_id": "R066",
    "label": "Figure 3",
    "context": "Figure 3: Annual Rainfall Shocks and Household Expenditures Notes: This figure shows the raw correlation between annual rainfall incidence (standardized) and household per capita expenditures. The horizontal axis is divide"
  }
]