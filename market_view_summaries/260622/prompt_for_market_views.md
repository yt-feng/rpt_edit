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
    "title": "GS：市场低估了霍尔木兹冲击对油需的结构性重塑",
    "digest": "[wechat_article.md]\n# GS：市场低估了霍尔木兹冲击对油需的结构性重塑\n\n霍尔木兹海峡的供应冲击正在改变全球石油市场的需求曲线，而不仅仅是供给曲线。这是GS最新研报中最值得关注的判断。市场习惯性地将地缘政治风险简化为短期价格脉冲和库存扰动，但这份报告揭示了一个更深层的机制：当油价因供给冲击而上涨时，消费者行为并非被动接受，而是加速了结构性替代。这份报告的独特价值在于，它用实时数据捕捉了这种替代正在发生，并且量化了它对2027年油需的潜在影响。\n\n报告的核心发现是：自今年2月霍尔木兹冲击开始以来，全球电动汽车渗透率已上升3.4个百分点，达到26.1%的历史新高。这不是一个温和的线性外推，而是一个加速信号。GS据此估算，到2027年12月，全球石油需求可能因此面临每日13万至32万桶的下行风险。这个数字在每日约1亿桶的全球市场中看似微小，但它的意义不在于绝对值，而在于它揭示了需求侧正在发生的结构性变化——而市场对此的定价可能远远不足。\n\n理解这份报告，需要跳出“电动汽车替代石油”的陈旧叙事。真正重要的是三个层次的问题：第一，替代的速度为何在此时加速；第二，这种加速是否具有持续性；第三，当前的市场定价是否已经充分反映了这一变化。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 霍尔木兹冲击正在改变全球电动汽车渗透率的斜率\n\nGS使用的“nowcast”模型显示，全球电动汽车渗透率并非均匀上升，而是在霍尔木兹冲击发生后出现了明显的斜率变化。从2月到5月，全球渗透率从约22.7%跃升至26.1%，这一增幅超过了此前12个月的总和。更值得注意的是，在15个最大的电动汽车市场中，有12个出现了渗透率上升，这是一个罕见的广泛性信号。\n\n中国是这一变化的绝对主力。中国的电动汽车渗透率在同期内上升了11.4个百分点，贡献了全球增量的61%。OECD国家贡\n\n[... middle omitted ...]\n\n场格局的潜在影响。完整报告原文和原始数据图表也在社群内共享。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n电动车加速渗透，石油需求承压\n\n🌍 全球电动车渗透率创新高\n\n某外资投行最新研报显示，自今年2月以来，全球电动车渗透率已上升3.4个百分点，达到26.1%的历史新高。\n\n中国是最大推手，渗透率飙升11.4个百分点。全球15大电动车市场中，12个市场渗透率都在上升。\n\n📊 对石油需求的影响有多大？\n\n研报测算了两类情景对2027年12月全球石油需求的影响：\n\n1️⃣ 临时加速情景：假设各地区电动车渗透率维持在2026年5月水平，预计全球石油需求减少13万桶/日\n\n2️⃣ 持续加速情景：假设各地区按当前趋势线性增长，预计减少32万桶/日\n\n换算一下：每100万辆燃油车被电动车替代，美国道路石油需求减少3万桶/日，其他国家减少2万桶/日。\n\n🔍 还有两个被忽视的维度\n\n研报特别提醒，以上测算只是冰山一角：\n\n• 存量替代效应：高油价已在推动存量车替换，中国汽油及相关产品销售同比下降超20%\n\n• 非乘用车领域：印度92%的电动车是两轮/三轮车，这些车的燃油替代效应可达乘用车的三分之一到一半\n\n🧠 思考题\n\n电动车加速渗透是否会成为石油需求的长期结构性压力？欢迎一起讨论。\n\n#学习笔记\n\n[source_mineru\n\n[... middle omitted ...]\n\nenetration) since February:\n\n☐ Global EV car sales penetration has increased by 3.4pp and reached its all-time high last month of 26.1%, excluding September 2025 (when US EV sales surged in ad\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R002",
    "title": "Bernstein：全球游戏业真正的拐点不在2026年，而在GTA VI之后的2027年",
    "digest": "[wechat_article.md]\n# Bernstein：全球游戏业真正的拐点不在2026年，而在GTA VI之后的2027年\n\n全球视频游戏行业在2025年实现了2180亿美元的收入，同比增长4.8%。这个数字本身并不令人意外——行业早已从疫情后的回调中恢复。真正值得关注的信号，是Bernstein这份年度深度报告揭示的一个结构性转折：行业正在从“增长驱动”转向“整合驱动”，而2026年可能成为近年来最被低估的过渡年份。\n\n报告的核心判断并不复杂：全球游戏行业的收入增长将在2026年放缓至0.7%，然后在2027年回升至3.3%。但数字背后的叙事远比表面丰富。这份报告真正想告诉投资者的，不是增长率的短期波动，而是行业竞争格局正在经历一次自移动游戏爆发以来最深刻的洗牌。\n\n我们整理了Bernstein这份报告的五个核心洞察，以及一个报告尚未完全回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 行业正在进入资本周期的后半段，整合比增长更重要\n\nBernstein在报告中反复强调一个概念：行业正处于“资本周期的后半段”。这意味着，过去几年大量资本涌入、新工作室遍地开花的阶段已经结束，取而代之的是市场集中度的提升和落后产能的出清。\n\n报告明确指出，虽然整体行业收入增速放缓，但上市公司的收入增速预计将达到7-8%，显著高于行业平均水平。这背后有两个驱动力：一是西方市场长期被推迟的工作室关闭潮终于到来，二是头部公司凭借IP和资金优势在竞争中持续扩大份额。\n\n这一判断的意义在于，投资者不应再将注意力集中在行业总规模的增长上，而应关注哪些公司能够在整合中成为赢家。Bernstein用一组数据说明这个逻辑：2025年Steam上发布的新游戏数量从2019年的8100款激增至21400款，但获得超过5000条评论的游戏数量却从73款降到了72款。供应\n\n[... middle omitted ...]\n\n里，与更多产业研究者和投资者一起讨论这些尚未完全解答的问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n2026全球游戏业，洗牌前夜\n\n游戏行业，拐点将至\n\n2026年行业收入预计仅增长0.7%，但暗流涌动\n\n读了一份某外资投行关于全球游戏行业的深度研报，2026年是个微妙的节点。行业整体收入预计2180亿美元，但增速从2025年的4.8%骤降至0.7%。表面平静，底下全是戏。\n\n1️⃣ **GTA VI成了行业“清场”事件**\n为了避开GTA VI，几乎所有大作都挤在9月发售。结果就是供给过剩，如果不是顶级IP或开发商，很容易被淹没。市场对GTA VI的期待已经“从看涨到圣经级别”，11月发售后，很可能成为整个行业情绪和资金流向的转折点。\n\n2️⃣ **PC端是最大惊喜，中国是引擎**\n2025年中国PC游戏市场增长15%，《黑神话：悟空》功不可没。更关键的是，现在普通家用电脑的显存（8-12GB）已经能流畅跑PS4/PS5世代的游戏，加上多平台同步发行成为常态，PC的增长潜力被严重低估。而主机这边，内存成本高企仍是最大拖累。\n\n3️⃣ **平台抽成终于要降了**\n2026年3月，谷歌和苹果先后宣布降低平台抽成（安卓从30%降至20%，iOS降至25%）。研报认为，随着平台流量增长放缓，以及全球各地反垄断诉讼\n\n[... middle omitted ...]\n\n1.jpg)\n\nHyrum Caesar\n\n+81 3 6777 6979\n\nhyrum.caesar@bernsteinsg.com\n\nWe estimate \\$220bn of industry revenue in 2026. This note represents our annual deep dive on global video gaming industry \n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R003",
    "title": "Bernstein：云巨头正在从“算力军备竞赛”转向“资本效率竞赛”",
    "digest": "[wechat_article.md]\n# Bernstein：云巨头正在从“算力军备竞赛”转向“资本效率竞赛”\n\n市场对AI基础设施投资的焦虑从未停止。每一季度云巨头的资本支出数字都在刷新纪录，而关于“何时能看到回报”的质疑声浪也随之升高。但Bernstein最新发布的这份涵盖全球软件、美国和中国互联网以及通信基础设施的季度云报告，给出了一个值得深思的信号：真正决定未来几年赢家的，可能不再是谁能建起最大的GPU集群，而是谁能以最高的资本效率将算力转化为可交付的云收入。\n\n这份由Bernstein全球云团队联合撰写的报告，追踪了亚马逊AWS、微软Azure、谷歌云、甲骨文OCI、阿里云以及新纳入的“Neocloud”代表CoreWeave的季度表现。报告覆盖的周期已延伸至2026年第一季度，并基于长达21个季度的历史数据，构建了一个观察超大规模云市场结构性变化的参照系。其核心判断是：市场正在从单纯的“建设能力”竞争，转向“运营效率”与“资本结构”的复合博弈。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 资本支出与运营现金流的剪刀差扩大，融资能力成为新护城河\n\n报告中最具冲击力的数字之一，是四大云巨头（亚马逊、微软、谷歌、甲骨文）在2026年第一季度的现金资本支出总和已接近1300亿美元。Bernstein模型显示，2026年全年这一数字将达到约6230亿美元，若加上Meta，则逼近7600亿美元。与此同时，这四家公司全年的经营活动现金流估计约为6350亿美元。\n\n这组数据揭示了一个关键矛盾：资本支出的增长速度正在持续超过运营现金流的增长。报告中的图表清晰展示了这一趋势——当资本支出曲线陡峭上行时，现金流增长曲线却呈现波动盘整。这意味着，云巨头们仅靠内部造血已难以支撑其扩张速度。事实上，亚马逊、谷歌和甲骨文近期已陆续进入资本市场进行融资。\n\n这一变化的\n\n[... middle omitted ...]\n\n解：哪些云厂商的扩张是可持续的，哪些可能正在透支未来的回报。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球云巨头最新成绩单：谁在领跑AI？\n\n云巨头AI竞赛新格局\n\n超大规模云市场进入关键转折点\n\n最近读了某外资投行关于全球超大规模云厂商的研报，信息量很大。这轮AI浪潮下，云厂商的竞争格局正在发生有趣变化。\n\n**1️⃣ 资本开支狂飙，但回报还没跟上**\n- 四大云厂商1Q26资本开支合计约1300亿美元\n- 研报预计2026年全年将达6230亿美元（含Meta接近7600亿）\n- 但运营现金流增速明显滞后，2027年可能都需要外部融资\n- 关键是：收入增速虽然回暖，但还远没到证明ROI的程度\n\n**2️⃣ 谷歌云成了最大黑马**\n- 谷歌云Q1利润率从去年同期的17.8%飙升到约33%\n- 积压订单接近翻倍至约4620亿美元，其中超50%将在24个月内转化\n- 开始向客户出售自研TPU芯片，预计2027年贡献更明显\n- 以前是云市场追赶者，现在AI云收入增量已和微软不相上下\n\n**3️⃣ 微软：AI ARR达370亿美元**\n- 押注Azure+AI的策略正在见效\n- Office 365 Copilot和GitHub的AI功能使用量明显增长\n- 研报认为即使AI泡沫破裂，微软也有防御优势：自用需求+大企业\n\n[... middle omitted ...]\n\n79aab99ac0193c518fec0b2.jpg)\n\n![](images/1de7aba99e3ec554a8a9feba045e2cb67051c370d6b58d8baf5b7194bf23a216.jpg)\n\n![](images/513b0733fe979af8106d31f3d484ae84777fe8cdb675e910feb3714b8975e321.jpg)\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R004",
    "title": "GS：AI正在重塑全球深水油田的经济模型，但市场低估了“时间压缩”的定价权",
    "digest": "[wechat_article.md]\n# GS：AI正在重塑全球深水油田的经济模型，但市场低估了“时间压缩”的定价权\n\n一份来自GS的最新报告，以15家以上国际石油公司、油服企业和数字供应商的访谈为基础，试图回答一个对全球能源供给格局至关重要的问题：AI和数字化到底能多大程度改变一个深水油田从发现到产油的时间表，以及这个时间表的变化会如何改写上游项目的投资回报率。\n\n这份报告的核心判断是：AI对油气行业的冲击不是渐进式的效率改善，而是结构性压缩了项目从勘探到最终投资决策(FID)的周期，进而在成本曲线上制造了一个足以影响长期油价预期的位移。GS估算，一个典型的深水绿地项目，全周期时间可从12年压缩至7年，降幅约38%。而由此带来的内部收益率(IRR)提升可达3.5个百分点，盈亏平衡价格下降约15%。\n\n这些数字本身已经足够引人注目。但真正值得产业决策者和投资者关注的，不是AI“能否”带来改变，而是“在哪里”改变、改变“由谁捕获”，以及哪些传统假设正在被颠覆。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 时间压缩的分布极不均匀，90%的收益集中在FID之前\n\nGS的报告给出了一个反直觉的结论：AI带来的时间节省几乎全部发生在项目最终投资决策(FID)之前。具体来看，勘探阶段可缩短55%，评价阶段缩短40-50%，前端工程设计(FEED)同样缩短40-50%。这三个阶段合计贡献了全部时间节省的90%。\n\n这意味着什么？意味着AI正在改写的是油气项目“决策前的确定性”，而不是“建设中的速度”。在传统模式下，从发现油田到决定是否投资，往往需要5-8年的数据收集、地震解释、井位设计和工程验证。AI通过加速地震数据处理、自动解释和工程工作流，将这一周期大幅压缩。GS访谈中，有运营商报告地震解释速度提升了5-10倍，在试点盆地中，预测成功率从约50%提升至约75\n\n[... middle omitted ...]\n\n二阶影响，以及这些变化对不同类型投资者的具体含义。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI正在把深海油田开发周期从12年压到7年\n\nAI重塑深海油田\n\n某外资投行最新研报拆解了AI如何改变油气开发经济学，核心结论很清晰。\n\n1/ 时间压缩，但只在前期\nAI+数字化能把深海油田从发现到产油缩短38%，平均从12年降到7年。但90%的时间节省都发生在最终投资决策之前——勘探快55%、评估快40-50%、前端工程设计快40-50%。一旦进入建设阶段，物理瓶颈决定了压缩空间有限，FPSO建造依然要4年。\n\n2/ 内部收益率提升3.5个百分点\n四项杠杆贡献拆解：资本开支-10%（+1.9pp IRR）、上市时间-3个月（+0.8pp）、产量+3%（+0.5pp）、运营成本-10%（+0.3pp）。综合下来，典型深海项目IRR从15.5%升至19.0%，盈亏平衡点下降约15%。\n\n3/ 哪些已经落地，哪些还在画饼\n研报把杠杆分三档：已证明的（钻井效率、地震数据处理、产量优化）正在产生可量化的结果；新兴的（预测性维护、无人平台）有试点但缺大规模数据；有抱负的（提升采收率）还要5-10年。\n\n4/ 谁最受益\n研报认为三类公司值得关注：拥有全球最大多客户地震数据库的TGS（控制2018年以来约60%的多客户数据\n\n[... middle omitted ...]\n\nn questions about long-term offshore projects — by how much could AI/digitalisation compress project timelines and how materially could it shift the economics of new oil developments — at a ti\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R005",
    "title": "Bernstein：全球储能市场的真正拐点不在技术突破，而在供应链的本地化重构",
    "digest": "[wechat_article.md]\n# Bernstein：全球储能市场的真正拐点不在技术突破，而在供应链的本地化重构\n\n全球储能产业正在经历一个被大多数投资者低估的结构性转变。这份Bernstein最新发布的全球储能周报，表面上是一系列分散的行业动态汇总，但当我们把这些信号拼合在一起，一个清晰的判断浮出水面：市场关注的焦点正在从“谁的技术更先进”转向“谁的供应链更能在本土落地”。这不是一个渐进式的变化，而是一个正在加速的拐点。\n\n为什么现在这个判断重要？因为在过去两年，投资者习惯用电池化学的突破、能量密度的提升、或者固态电池的进展来评估储能公司的价值。但Bernstein这份报告揭示了一个不同的叙事：真正驱动行业格局重塑的力量，来自美国、欧洲、中国三个区域同步发生的供应链本地化运动。这不是贸易摩擦的简单延伸，而是储能产业从“全球化采购”向“区域化闭环”的模式切换。\n\n报告中最值得关注的信号不是某个技术突破，而是几个看似分散的供应链事件：韩国HyVISION Systems拿下950亿韩元的北美ESS设备订单，Sebang与LG Energy Solution合作在俄亥俄州建设模块工厂，以及中国政策要求高速公路配套重卡充电设施。这些事件的共同指向是：储能产业的竞争维度正在从电池性能转向供应链的地理韧性。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 北美市场的核心驱动力不是需求，而是合规驱动的本地化制造\n\nBernstein报告中最密集的信号来自北美。HyVISION Systems的订单金额从初始规模扩张近五倍，直接原因是客户扩大了美国本土生产计划至2028年。Yujin Technology正在向美国、加拿大、波兰的ESS生产线扩大出货。Sebang与LGES的合作项目预计到2028年累计订单价值1.8万亿韩元。\n\n这些事件表面上是韩国设备商的\n\n[... middle omitted ...]\n\n来知识星球微信群继续探讨这些关键变量如何影响具体的投资判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n储能行业正在经历一个“从政策驱动到市场驱动”的转折点。本周全球储能市场信号密集，从北美到欧洲到亚洲，几个关键趋势正在成形。\n\n**1. 北美：供应链本地化加速**\n- HyVISION拿到950亿韩元订单，为LG新能源在俄亥俄州产线供设备。\n- Sebang与LG合作，在俄亥俄建厂生产JF2 Link电网级储能模块，订单目标1.8万亿韩元。\n- Yujin Technology也在扩大对北美、加拿大、波兰的精密设备出口。\n- 一句话：北美储能制造本地化正在从“口号”变成“真金白银的订单”。\n\n**2. 电池技术路线：LMR vs LFP vs 半固态**\n- GM可能优先推进LMR（锂锰富集）电池，成本接近LFP但能量密度高33%，更适合皮卡/SUV。\n- Stellantis开始路测Factorial的半固态电池，能量密度375Wh/kg，15%-90%快充只要18分钟。\n- CATL说固态电池大规模商用化2027年前不太可能，成本仍是核心障碍。\n- 路线之争仍在，但高能量密度+可制造性才是胜出的关键。\n\n**3. 中国：需求结构在变**\n- 碳酸锂期货反弹，分析师说需求已经从“EV单引擎”变成“EV+储能\n\n[... middle omitted ...]\n\ns through 2028. The equipment is expected to support production of LG Energy Solution's grid-scale ESS products at a facility in Ohio, with three assembly lines planned. The deal strengthens H\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R006",
    "title": "摩根斯坦利：半导体设备市场的真正变量不是总量，而是DRAM与NAND的结构性分化",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：半导体设备市场的真正变量不是总量，而是DRAM与NAND的结构性分化\n\n当市场还在争论2026年半导体资本支出是否会创下新高时，摩根斯坦利最新发布的半导体资本设备研报给出了一个更精细的答案：总量确实在上修，但真正值得关注的不是数字本身，而是DRAM和NAND两条主线正在走向截然不同的投资节奏。\n\n这份报告将2026年全球DRAM设备支出（WFE）从之前的446亿美元上调至486亿美元，2027年从571亿美元上调至625亿美元。与此同时，NAND的WFE预测几乎原地踏步——2026年从159亿美元微调至157亿美元，2027年从240亿美元调整至241亿美元。乍看之下，DRAM是绝对的王者。但报告真正的判断藏在更深的层次里：2027年NAND的WFE增速将高达53%，远超DRAM的29%。这意味着，当前市场对设备股的定价，可能正在忽略一个即将到来的结构性切换。\n\n这不是一份简单的“上调预测”报告。它揭示了半导体设备投资中一个容易被忽视的规律——当技术升级遇到产能扩张，谁在提前花钱，谁在等待拐点，决定了下一阶段设备商的赢家格局。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. DRAM的上修并非需求拉动，而是客户“不惜一切代价”的提前支出\n\n摩根斯坦利将DRAM WFE上修的核心驱动力归结为“brownfield”——即现有产线的升级改造，而非全新的晶圆厂建设。2026年绿色field（新建厂）的月产能仅从258kwpm微调至268kwpm，2027年维持395kwpm不变。真正拉动上修的是brownfield部分的假设：报告明确写道，客户正在“不惜一切代价”（doing everything in their power）将设备采购前置。\n\n这意味着什么？DRAM设备支出的增长，不是需求端的自然扩张\n\n[... middle omitted ...]\n\n的完整版PDF，以及我们对其中关键图表的逐张解读。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nDRAM 设备支出正在加速\n\n设备支出正在被拉前\n\nDRAM 扩产比预期更猛\n\n最近某外资投行更新了半导体设备研报，核心结论是：**DRAM 的设备支出（WFE）正在被客户拉前，后续还有上调空间。**\n\n1️⃣ **DRAM 大幅上修**\n2026 年 DRAM 设备支出从 446 亿→486 亿美元，2027 年从 571 亿→625 亿美元。\n主要驱动力来自 **brownfield（现有产线升级）**，客户正在全力把支出往前提。\n对应 bit 供给增速从 26%/32% 上调到 29%/33%。\n\n2️⃣ **NAND 小幅调整**\n2026 年 NAND 设备支出微调至 157 亿美元，2027 年 241 亿美元基本持平。\n但 bit 供给增速从 21%/32% 上调到 24%/31%。\n**关键变量不是产能，而是良率提升**——同样的设备能产出更多 bit。\n\n3️⃣ **设备商受益顺序**\n2026 年 DRAM 支出加速，Applied Materials 受益最直接。\n但到 2027 年，NAND 设备支出增速（53%）会远超过 DRAM（29%）。\n所以研报更偏好 Lam Research\n\n[... middle omitted ...]\n\ne revised higher, we are updating our DRAM and NAND WFE/supply models.\n\nDRAM – WFE and bits revised higher. We raise our 2026/2027 DRAM WFE estimates from \\$44.6bn/\\$57.1bn to \\$48.6bn/\\$62.5b\n\n[... middle omitted ...]\n\ntd>Teradyne Inc (TER.O)</td><td>E (07/30/2025)</td><td>$437.92</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.\n\n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R007",
    "title": "Bernstein：代币化的真正战场不在资产发行，而在交易基础设施的重新定价",
    "digest": "[wechat_article.md]\n# Bernstein：代币化的真正战场不在资产发行，而在交易基础设施的重新定价\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 市场正在用脚投票，但大部分投资者看错了方向\n\n截至2026年6月，代币化现实世界资产的市场总值已突破510亿美元，年初至今增长40%。同一时期，更广泛的加密市场下跌约20%。这个数字本身就包含一个反直觉的判断：代币化并非加密行情的附属品，它正在走出一条独立的增长曲线。\n\n但更值得关注的不是总量，而是结构。私人信贷以47%的占比主导代币化资产类别，美国国债占30%，商品占9%。代币化股票虽然仅占不到3%，但年初至今增长了130%，从7亿美元跃升至16亿美元。Bernstein这份报告的核心判断是：代币化正在从“发行试验”进入“基础设施竞争”阶段，而真正决定胜负的，不是谁能发行更多资产，而是谁能构建合规、高效、可规模化的交易和结算层。\n\n这不是一个关于“区块链能否替代传统金融”的宏大叙事。这是一个关于“在现有监管框架下，谁有能力重新定义证券的清算、交易和持有方式”的具体商业问题。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 当前代币化股票的核心缺陷：所有权与收益权的分离\n\n理解这一轮基础设施竞争的关键，在于看清当前主流代币化股票模型的根本局限。\n\n目前，Robinhood等平台向非美国投资者提供的代币化股票，采用的是第三方赞助商模式。赞助商购买底层股票、托管在受监管账户中，然后发行一个区块链代币。投资者可以24x7交易这些代币，实现实时结算，平台赚取交易佣金。\n\n但这些代币只运行在区块链上，与实际的股东登记簿没有任何对账机制。代币持有者不是股东登记簿上的注册所有人，赞助商才是。这意味着，代币持有者不享有股息、投票权等与股票所有权相关的权利。\n\n[... middle omitted ...]\n\n基础设施竞争有进一步的研究兴趣，欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nTokenized RWA 总市值已突破510亿，背后谁在布局？\n\n**代币化资产，正在卡位**\n\nRWA（真实世界资产）代币化，正在从概念走向实战。总市值已超510亿美元，年内增长40%，而同期加密市场整体下跌约20%。这个赛道韧性很强。\n\n几个关键观察：\n\n1️⃣ **私人信贷是主力，美债和商品紧随其后**\n私人信贷占了RWA市值的约47%，美债约30%，商品约9%。以太坊和Provenance链承载了超过70%的代币化资产，链上地址数已突破90万。\n\n2️⃣ **股权代币化是下一个焦点**\n代币化股权年内增长130%，从7亿到16亿美元。目前主要面向非美国投资者，但美国监管动作在松绑——SEC提议废除某些规则，并批准了纽交所和纳斯达克的代币化证券交易试点。行业还在等“创新豁免”的明确信号。\n\n3️⃣ **两条路线在博弈**\n- **交易基础设施型**：由第三方托管底层资产，发行代币供24/7交易。优点：快速、低成本。缺点：代币持有者不享有股东权利（如分红、投票）。\n- **结算与交易所型**：用区块链做公司实际股票的结算层，投资者享有完整所有权。Figure、Bullish、Securitize都在建受监管\n\n[... middle omitted ...]\n\ners are laying out their early ‘chess moves’ with early product launches, acquisitions and strategic partnerships.\n\nTokenized RWA Industry Metrics - Market cap of tokenized real-world assets h\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R008",
    "title": "Bernstein：AI正被内存成本压到喘不过气，一场供应链“再校准”不可避免",
    "digest": "[wechat_article.md]\n# Bernstein：AI正被内存成本压到喘不过气，一场供应链“再校准”不可避免\n\n当所有人都在关注GPU算力瓶颈时，内存正在悄然成为AI基础设施中最被低估的成本变量。这份Bernstein研报揭示了一个反直觉的判断：市场真正低估的不是需求，而是供给侧定价权转移带来的成本结构重塑。HBM价格即将迎来2-2.5倍的跳升，而经过NVIDIA等GPU供应商的“加价”传导后，超大规模云厂商的AI资本开支可能被迫上调30%。这不是一个边际变化，而是一个需要重新审视整个AI投资回报模型的系统性冲击。\n\n报告的核心信号是：内存价格压力正在从消费电子蔓延至AI领域。过去三年，HBM作为AI算力的“伴生品”，其定价一直被长期合同锁定，与暴涨的常规DRAM价格形成了巨大背离。这种背离正在扭曲内存供应商的产能分配决策，也将倒逼整个供应链进行一次痛苦的“再校准”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 常规DRAM价格暴涨4.5倍，HBM定价扭曲已到极限\n\nBernstein的分析显示，从2025年第三季度到2026年第二季度，常规DRAM价格已经上涨了约4.5倍。而HBM由于采用年度合同定价，价格几乎没有变动。这种定价机制带来的结果是：同样一片晶圆产能，投入常规DRAM产生的收入是HBM的2倍以上，毛利润更是接近3倍。三星和美光在2026年第一季度财报电话会议上均已明确表示，非HBM的DRAM利润率已经领先于HBM，且随着常规DRAM价格继续攀升，这一差距还在扩大。\n\n这里的关键洞察不在于价格差异本身，而在于这个差异对供应行为的扭曲。当内存供应商发现生产常规DRAM比生产HBM更赚钱时，他们会有强烈的动机将产能从HBM转向常规DRAM。而HBM恰恰是当前AI算力最紧缺的组件。这种供给侧的“理性选择”正在制造一个结构性矛盾：A\n\n[... middle omitted ...]\n\n合最新的供应链数据，持续追踪这场“再校准”的每一个关键节点。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n内存涨价，AI也扛不住了？\n\n📌 内存压力传导到AI\n\n当内存涨价成为AI的负担，成本压力开始从消费端蔓延到云端。\n\n1️⃣ HBM定价被低估了\n目前常规DRAM价格已涨约4.5倍，但HBM受年度合约锁定，价格基本没动。结果是，同样一片晶圆，做常规DRAM的营收是HBM的2倍，毛利接近3倍。HBM供应商和GPU厂商已经开始谈判2027年定价，试图缩小这个差距。\n\n2️⃣ GPU厂商的“加价”放大成本\nHBM是封装在GPU里的，比如英伟达。如果HBM成本上涨，英伟达要维持75%的毛利率，需要把HBM涨价部分乘以4倍来定价。这意味着，最终云厂商要承担的HBM成本，比直接采购高得多。\n\n3️⃣ 数据中心capex可能涨30%\n以Vera Rubin机架为例，如果HBM涨价2-2.5倍、加上GPU厂商的加价，再加上常规DRAM和NAND的涨价，云厂商的数据中心资本支出要比原计划高出约30%。虽然竞争压力下他们不会停止投资，但“重新校准”成本分配几乎是必然的。\n\n4️⃣ 谁受益，谁承压？\n三星、SK海力士、美光会因HBM涨价迎来盈利上调，但HBM占比越高，整体盈利能力反而可能下降。联发科可能受益——如果云厂商想绕过GP\n\n[... middle omitted ...]\n\nOutperform ratings on Samsung, SK hynix & Micron & Underperform on KIOXIA.\n\nHBM price needs to go higher to narrow the profitability gap vs. conventional DRAM. From 3QCY25 to 2QCY26, conventio\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R009",
    "title": "Bernstein：印度真正需要的不是算力租用，而是自己的“DeepSeek 时刻”",
    "digest": "[wechat_article.md]\n# Bernstein：印度真正需要的不是算力租用，而是自己的“DeepSeek 时刻”\n\n这份来自Bernstein的研报，提出了一个在当下争论中容易被忽视的核心判断：印度无法在借来的模型上构建自己的AI未来。当市场将目光集中于算力基础设施的建设和应用层的快速迭代时，报告指出，一个更深层的结构性风险正在浮现——基础模型正在从开放的商品演变为受地缘政治管控的战略资产。对于印度而言，问题不在于是否要参与AI生态，而在于其在AI价值链上的定位是否可持续。\n\n报告选择在此时重提这个话题，本身就意味着一种紧迫感。过去，关于“大语言模型不重要”的论调在印度技术圈并不少见。但近期美国对非公民访问最新AI模型的限制，将这一风险从理论推向了现实。这份研报的价值在于，它没有停留在对依赖性的泛泛批评，而是通过梳理印度信息技术产业的深层结构，解释了为什么印度没有出现自己的“DeepSeek 时刻”，并为决策者提供了一套权衡“开放”与“自主”的政策框架。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 基础模型不再是SaaS产品，而是正在成为受管控的“战斗机”\n\nBernstein报告的核心洞见在于对AI资产属性的重新定义。它指出，技术访问权在过去一直是被配给和管控的。从关键矿产和半导体设备，到GPU，再到如今对前沿模型本身的限制，这一趋势正在打破AI“全球化”的幻觉。报告以Anthropic最新模型对非美国公民的限制为例，认为这不再是孤立事件，而是新常态的开始。\n\n这意味着，基础模型将从一种可以随意订阅的软件服务，转变为类似于“战斗机”的国家战略资源。其背后的逻辑是，谁控制了最前沿的模型，谁就掌握了定义下一个时代应用能力的钥匙。对于正在说服自己“基于外国LLM构建应用、靠数据中心收租”是明智AI战略的印度而言，这一判断具有深刻的警示意义\n\n[... middle omitted ...]\n\n，但更深层的竞争，是关于战略选择、路径依赖和风险定价的较量。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n印度AI不能只“借船出海”\n\n**AI不能只租不造**\n\n印度需要自己的DeepSeek时刻\n\n---\n\n**1. AI正在变成“战斗机”，不是SaaS**\n\n过去几年，从关键矿产到GPU，再到前沿模型限制，技术获取正在被“配给化”。最近Anthropic最新模型对非美国公民的禁令，说明这不是偶然。AI正在从商品变成战略资源——前沿模型会像战斗机一样被管控。印度如果只满足于租算力、建数据中心、做应用层，等于把核心模型外包给别人。\n\n**2. 为什么印度没有自己的大模型？**\n\n这很反直觉：印度明明是全球数据大产地，却没能做出自己的LLM。原因很结构性的：\n- 科技生态长期以服务外包为主，缺乏搜索、社交、消息等面向消费者的平台（这些平台才能生成高质量训练数据）\n- 没有数据生态，就不需要培养底层模型的人才和学术深度\n- IT服务模式靠低成本人力帮全球巨头“微调”软件，反而锁死在应用层\n\n很多机构负责人说“印度不需要自己的LLM，专注应用就行”——这更多是路径依赖，不是战略选择。\n\n**3. 把AI核心层交给别人，风险在哪？**\n\n想象一下：印度从企业软件到国防、航天，核心智能层都由外国LLM驱动。一旦地缘冲突，\n\n[... middle omitted ...]\n\n the risk that India could find itself locked out some day, with its applications trailing those in the US and China. We had raised this topic even earlier but were muffled with noises of “LLM\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R010",
    "title": "JPM：市场低估了“供给瓶颈”在日本MLCC股中的定价权，而非AI需求本身",
    "digest": "[wechat_article.md]\n# JPM：市场低估了“供给瓶颈”在日本MLCC股中的定价权，而非AI需求本身\n\n**主判断：** 当前日本MLCC相关股票的上涨，并非单纯由AI需求驱动，更核心的是其作为“供给瓶颈”环节所享有的超额利润定价权。这一轮上涨的结构与2000年代中期的EM商品热潮高度相似，真正的风险不在于需求见顶，而在于“瓶颈效应”向下游转移。\n\n这份来自JPM量化与衍生品策略团队的研报，提供了一个与市场主流叙事截然不同的分析框架。大多数投资者将村田制作所与太阳诱电的强势表现归结为AI带来的基本面增长，但该报告从技术面和资金结构切入，认为这轮上涨的内在逻辑更接近“供给瓶颈溢价”的重现。报告的核心洞察在于：超额利润的可持续性，更多取决于企业在供应链网络中的“瓶颈位置”，而非其自身的竞争力。\n\n为什么现在这个判断重要？因为市场正在将MLCC股票视为AI周期的纯受益者，却忽略了其背后一个更脆弱的结构性特征——高Beta、低Quality。这意味着一旦“瓶颈”转移，这些股票的调整速度可能远超基本面投资者的预期。报告提供了一个历史参照系，以及一套用于观察“瓶颈转移”的信号框架。\n\n以下是对这份研报核心逻辑的拆解与延伸。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 超额利润的来源并非技术壁垒，而是供应链中的“瓶颈位置”\n\n报告最引人注目的论点，是将当前MLCC股票的上涨与2000年代EM热潮中的特定日本股票进行对比。在EM热潮初期（2002-2005年），住友金属矿山（镍冶炼）、三井金属（超薄铜箔）、信越化学（硅片）以及新报国材料（低热膨胀合金）等公司，都曾经历过一段超额利润的爆发期。这些公司的共同点是什么？它们都处于当时全球供应链中难以快速扩产的“瓶颈环节”。\n\n报告通过动态时间规整（DTW）方法，将当前MLCC股票的股价走势与上述EM热潮\n\n[... middle omitted ...]\n\n系，将决定他们能否在“瓶颈转移”发生之前做出正确的仓位调整。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nMLCC 还能涨多久？看这张图就够了\n\n**供给瓶颈的魔力**\n\nMLCC（多层陶瓷电容）相关股票，像村田制作所和太阳诱电，最近涨得很猛。很多人觉得这只是 AI 需求的延伸，但某外资投行量化团队用了一个更酷的视角：把现在的 AI 热潮和 2000 年代中期的 EM（新兴市场）热潮做对比。\n\n**1. 历史不会简单重复，但押韵**\n\n- 他们发现，AI 热潮目前大概处于 EM 热潮的“第六阶段”，还有上涨空间。\n- 在 EM 热潮中，供给瓶颈股（比如镍冶炼、超薄铜箔、硅片）都经历过类似的“超额利润”阶段。\n- 关键点：利润不是来自公司多牛，而是来自它在供应链瓶颈中的位置。\n\n**2. 现在的 MLCC 像当年的谁？**\n\n- 村田和太阳诱电这类 MLCC 厂商，拥有寡头垄断地位和难以扩产的供给结构。\n- 一旦需求爆棚，利润增长会远超销量增长。\n- 目前，上游的半导体、设备、HBM、CoWoS 还在扩张，瓶颈还没转移。\n\n**3. 谁在买？谁还没买？**\n\n- 短期来看，动量交易者和 Beta 追随者是主要买家。他们的仓位还有空间。\n- 长期来看，全球主动投资基金对日本科技板块的配置仍处于“中性偏低”，说明大资金\n\n[... middle omitted ...]\n\n strategies.\n\nWe, the QDS team, have long viewed the current AI boom in relation to the EM (Emerging Markets) boom of the mid-2000s. Under this framework, we expect MLCC stocks to continue to \n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 19 Jun 2026 04:55 PM JST\n\nDisseminated 19 Jun 2026 04:55 PM JST"
  },
  {
    "id": "R011",
    "title": "GS：家电内需压力尚未出清，但出口的结构性机会比想象中更值得关注",
    "digest": "[wechat_article.md]\n# GS：家电内需压力尚未出清，但出口的结构性机会比想象中更值得关注\n\n五月的数据再次确认了一个判断：中国家电行业正处于“内需承压、外需修复”的错位周期中。GS最新发布的五月家电追踪报告显示，国内零售和出厂数据延续了4月的疲软态势，而出口则出现了超预期的环比改善。这份报告的核心信号并非简单的“内冷外热”，而在于两个更值得推敲的结构性变化：一是国内需求的下行斜率正在放缓，基数效应将在6月下旬开始提供缓冲；二是出口的韧性并非仅靠低基数，中国企业在海外市场的份额持续扩张正在成为更持久的驱动力。\n\n对于投资者而言，当前阶段的关键问题不再是“行业是否见底”，而是“底部的形态和分化路径是什么”。GS在报告中明确指出了对美的集团、九号公司和海信家电的偏好，其逻辑并非押注行业整体反转，而是捕捉那些在周期底部仍能通过海外扩张、产品组合和股东回报构建安全边际的公司。\n\n以下是对这份报告核心洞察的拆解。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 五月内需数据低于预期，但真正的拐点信号在于基数的“前高后低”\n\n五月国内家电零售额同比下降16%，与4月-15%的降幅基本持平。空调国内出厂量更是同比下降15%，显著低于此前行业生产计划所隐含的-9%的预期。GS认为，这主要是受到去年同期需求前置以及4月以来部分品牌提价的叠加影响。\n\n但比单月数据更重要的是趋势判断。报告指出，由于去年6月“以旧换新”政策的效果开始逐步消退，从今年6月下旬开始，国内需求的同比基数压力将明显缓解。这意味着，即使终端需求没有显著回暖，7月之后的同比读数也可能出现自然改善。换句话说，当前市场对“内需持续恶化”的线性外推，很可能低估了基数效应带来的读数修复。\n\n这里需要谨慎的是：读数的改善并不等于需求的复苏。真正的拐点需要看到终端动销的实质回升，而非仅仅是统计意义上\n\n[... middle omitted ...]\n\n始图表和GS对个股的详细分析框架，并持续跟踪后续数据的变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n家电内销还在磨底，出口却悄悄回暖了\n\n五月家电数据：内需弱，出口好\n\n1⃣ 内销数据依然疲软\n五月社零家电零售同比-16%，和四月差不多\n空调内销出货同比-15%，比预期的-9%还低\n背后原因：去年提前透支需求 + 四月涨价影响\n618开局数据也不乐观，品牌方开始降价促销\n\n2⃣ 出口数据明显改善\n五月整体家电出口增速回正，超预期\n空调出口从-12%收窄到-4%\n美欧消费者信心回升，美国成屋销售也在改善\n中国品牌持续在海外抢份额\n\n3⃣ 品牌表现分化明显\n空调：海尔+6%，美的-23%，格力-13%\n冰箱四月：美的+25%，海信+15%\n洗衣机四月：美的+3%，海尔持平\n出口端，美的空调+4%，海尔冰箱+36%\n\n4⃣ 后续怎么看\n内销压力可能持续到6月上旬，6月下旬基数压力会缓解\n出口有支撑：美伊备忘录签署后需求可见度提升\n成本端：大宗商品价格稳定，但运费还在涨\n\n欢迎一起讨论家电行业趋势\n\n#学习笔记\n\n[source_mineru.md]\nCHINA CONSUMER DURABLES: APPLIANCE TRACKER\n\n# May 2026: Still weak domestic demand \n\n[... middle omitted ...]\n\nar and price hikes. Going forward, we view it as likely that domestic demand growth will remain under pressure in early June due to a high base. However, base pressure may sequentially ease in\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R012",
    "title": "GS：A股硬科技正在主导中国盈利增长的结构性分化",
    "digest": "[wechat_article.md]\n# GS：A股硬科技正在主导中国盈利增长的结构性分化\n\n2026年第一季度财报季刚刚落幕。GS覆盖了约7000家中国上市公司，并分析了超过4500份业绩会纪要。这份报告传递的核心信号是：中国上市公司的盈利增长正在经历一场深刻的结构性分化，而A股硬科技板块正站在这一分化的主导一侧。\n\n这不是一个简单的“A股优于H股”的判断。真正值得关注的，是支撑这一分化的三个底层力量：AI利润池正在从软件向硬件回摆，企业全球化布局在关税压力下仍在深化，以及上市公司资本配置逻辑正在发生根本性转变。这些力量叠加在一起，正在重塑中国权益资产的定价框架。\n\nGS在报告中明确提出，维持对A股相对于H股的偏好。其预测显示，CSI300在2026年全年盈利增速有望达到20%，而MSCI中国指数仅为8%。在即将到来的二季度业绩期，这一差距预计仍将显著存在——CSI300的盈利增速预期为11%，MSCI中国则接近零。\n\n这一判断的底层逻辑，值得每一位置身中国市场的投资者仔细拆解。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. A股与H股的盈利鸿沟，根源在于“硬科技”与“软科技”的资产结构差异\n\n2026年一季度，全部中国上市公司的净利润同比增长6%，延续了2025年7%的增长节奏。但这一整体数字掩盖了指数层面的巨大分化。CSI300一季度盈利同比增长9%，而MSCI中国指数则同比下滑8%。更极端的对比出现在创业板和科创板——两者分别录得22%和198%的同比盈利增长。\n\n这一差距并非偶然。A股指数中，科技硬件、半导体、电力设备等“硬科技”板块的权重远高于离岸市场。而MSCI中国指数中，互联网、电商、本地生活等“软科技”和消费服务类资产的占比更高。后者的盈利正受到快速商超补贴竞争和AI资本开支扩张的双重挤压。\n\nGS的分析师团队在业绩会纪要的文本分析\n\n[... middle omitted ...]\n\n内持续更新对这份报告的解读，也欢迎分享你们自己的观察和疑问。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nA股硬科技正在领跑，港股还在等风来\n\n封面：A股硬科技领跑\n\n副标题：26Q1盈利拆解：谁在涨，谁在扛\n\n1️⃣ A股 vs 港股，盈利剪刀差拉大\n\n26Q1全中国上市公司净利润同比+6%，但内部结构分化严重。\n- 沪深300：+9%\n- 创业板：+22%\n- 科创板：+198%\n- MSCI中国：-8%\n\nA股硬科技（AI硬件）是核心驱动力，港股被快商务补贴和AI投入拖累。展望后续，沪深300预期26/27年EPS增速20%/12%，而MSCI中国只有8%/12%。\n\n2️⃣ AI利润向硬件回流\n\n全球AI利润池中，中国占比从2024年的10%缩至26Q1的8%。但中国AI供应链内部，硬件利润占比从2024年的41%反弹至54%。\n\n半导体（存储、IC设计、材料）利润份额提升最快，而AI应用（下游软件）从59%跌至46%。背后是中美云厂商持续加码AI资本开支，给硬件厂商提供了确定性需求。\n\n3️⃣ 收入回暖，但利润分化加剧\n\n全中国上市公司营收增速从2025年的+1%提升至26Q1的+4%。但利润端分化明显：\n- 旧经济/国企：利润率修复\n- 新经济/民企/银行：利润率被压缩\n\n内卷行业中，半导体、工业金属\n\n[... middle omitted ...]\n\n/+8% yoy for MSCI China, validating our preference for A over H-shares.\n\n2. AI profits shifting towards hardware, both globally and domestically. Within China's AI supply chain, the hardware p\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R013",
    "title": "Bernstein：数据中心供电的真正瓶颈不在技术，在电网的“连接组织”",
    "digest": "[wechat_article.md]\n# Bernstein：数据中心供电的真正瓶颈不在技术，在电网的“连接组织”\n\n过去一年，市场对AI和数据中心电力需求的讨论，几乎都围绕一个核心问题：电力从哪里来？天然气、核能、可再生能源、燃料电池，每一种技术路线都有自己的拥护者。但Bernstein刚刚发布的一份基于50多家数据中心运营商调研的报告，给出了一个更底层、也更令人不安的回答——问题从来不是“发多少电”，而是“电能不能送到”。\n\n这份报告最值得关注的判断是：数据中心运营商最想要的，是电网连接。不是离网自建，不是孤岛运行，而是接入大电网。但他们面临的现实是，电网的“连接组织”——从并网审批到输电容量到设备交付——正在成为整个AI基础设施扩张的最大瓶颈。这个瓶颈的持续时间，不是一两年，而是以十年为单位。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 电网连接是首选，但并网等待时间已经突破运营商的容忍底线\n\n调研中，98%的受访数据中心运营商表示，电网连接是未来5-10年新项目的首选供电方式。对于100MW以上的大型数据中心，86%的运营商明确偏好“电网连接为主、现场发电为辅”的模式。现场发电（behind-the-meter）目前仅占数据中心电力市场的约5%，Bernstein预计到2030年代，这个比例也只会上升到5-10%。\n\n这个偏好本身并不令人意外。电网供电在成本、可靠性和可扩展性上，通常优于任何形式的现场自发电。真正值得关注的是，运营商对并网等待时间的容忍度极低。调研显示，绝大多数受访者认为“等待超过三年”是不可接受的。但现实是，目前美国主要区域的并网排队时间普遍在4年以上，CAISO区域甚至更久。\n\n这意味着什么？意味着在电网基础设施没有显著改善之前，大量数据中心项目的实际落地时间表，可能要比市场预期的更长。这不是需求不足的问题，而是供给侧的\n\n[... middle omitted ...]\n\n领域的读者一起讨论这些未解问题，欢迎来星球微信群里继续交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n数据中心用电，到底怎么解决？\n\n**用电焦虑怎么解？**\n\n数据中心用电需求暴增，电网压力山大，怎么破？\n\n某外资投行调研了50+数据中心运营商，发现几个核心结论👇\n\n**1/ 电网依然是首选**\n98%的受访者首选电网供电，尤其是100MW以上的大型数据中心，86%倾向电网为主+自备电源为辅。自备电源（BTM）目前只占约5%，预计2030年前后也仅占5-10%。\n\n**2/ 通电速度>成本**\n80%的受访者把“可靠性”排第一，59%把“通电速度”排第二。超过3年的电网接入等待时间，大部分运营商都接受不了。而目前多数地区电网排队时间已经4年+。\n\n**3/ 自备电源是刚需**\n超过95%的受访者认为自备备用电源是设计关键。天然气、太阳能+储能、燃料电池是主要选择。甚至有10%的受访者表示，为了自备电源，可以接受更高成本。\n\n**4/ 五大担忧**\n- 电网接入限制（最大痛点）\n- 审批慢、不确定性高\n- 电价、气价、氢价等波动大\n- 氢能、长时储能技术不够成熟\n- 数据中心增长加剧电网压力\n\n**5/ 可持续目标有影响，但非首要**\n多数大型项目会考虑可持续目标，但可靠性和通电速度才是核心。\n\n所以，电网设\n\n[... middle omitted ...]\n\nverage on Americas Power and Energy Transition last week. \\~20 calls and 1 webinar in two days - initiation feedback notes coming soon!\n\nFor today, we wrote a quick note summarizing the survey\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R014",
    "title": "GS：欧盟暂缓对中国割草机器人征收临时反倾销税，真正的变量不是关税本身，而是企业能否利用这个窗口期重塑竞争壁垒",
    "digest": "[wechat_article.md]\n# GS：欧盟暂缓对中国割草机器人征收临时反倾销税，真正的变量不是关税本身，而是企业能否利用这个窗口期重塑竞争壁垒\n\n2026年6月19日，欧盟委员会宣布，将继续对中国产割草机器人进行反倾销调查，但现阶段不会征收临时反倾销税。理由是案件技术复杂性。\n\n这份GS研报的核心判断是：投资者应当将此视为积极信号。但真正值得深入推敲的，不是“短期内关税没加”这个事实本身，而是这个时间窗口对行业竞争格局意味着什么。\n\nGS覆盖的三家中国公司——九号公司、石头科技和科沃斯——均可能因此受益，其中九号公司受益最为显著。但这份研报的深层逻辑在于：欧盟的决定为中国企业争取了至少6到12个月的缓冲期。这段时间足够做什么？足够一家企业把产能从中国转移到海外，但不足以让转移后的成本劣势完全消失。所以，真正的分化将从这里开始。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 2026年关税风险基本排除，但真正考验的是企业能否把窗口期转化为结构性优势\n\nGS在研报中明确指出，多数中国割草机器人企业原本的计划是在2026年上半年完成对欧洲的大部分出货，并预期从6月起可能面临临时反倾销税的影响。现在欧盟决定暂不征收临时关税，意味着2026年全年适用的关税税率大概率保持不变。\n\n这对企业最直接的影响是利润表。GS判断，中国企业可能不需要通过涨价来对冲关税成本，因此短期内的利润率和市场份额竞争力将得以维持。但这里有一个被市场低估的变量：定价纪律。\n\nGS特别提到，至少到调查结果更加明朗之前，中国割草机器人企业仍将保持定价纪律。这句话的潜台词是，一旦企业认为关税风险解除，可能会重新回到价格战的老路上。而欧盟暂缓加税，反而给了头部企业一个机会——在不牺牲利润率的前提下，继续用产品力而非价格来竞争。\n\n所以，2026年关税风险排除，只是短期利好。真\n\n[... middle omitted ...]\n\n分享GS等外资行的一手研报解读，以及产业层面的深度调研信息。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n欧盟暂缓加税，割草机器人松口气\n\n暂缓加征\n\n给中国割草机器人争取了半年窗口期\n\n最近欧盟对中国割草机器人（RLM）的反倾销调查有了新进展——6月19日，欧盟宣布继续调查，但暂不征收临时反倾销税。这意味着至少到2026年底，中国厂商的出口关税不会变。\n\n1️⃣ 为什么是利好？\n之前市场担心6月起就要交临时税，很多厂商赶在上半年集中发货。现在暂缓，2026年全年税率基本锁定，利润率和价格竞争力短期无忧。某外资投行认为，这个信号能缓解市场情绪。\n\n2️⃣ 但别掉以轻心\n调查还在继续，最终可能追溯征税。不过窗口期拉长，给了中国厂商更多时间准备——比如把产能转移到海外。只是海外建厂初期成本会高10%-20%，主要是劳动效率和供应链磨合。\n\n3️⃣ 谁最受益？\n投行重点提了三家：九号公司（割草机器人占收入9%，利润贡献更高）、石头科技、科沃斯。其中九号因为估值一直受调查压制，这次边际改善最明显。\n\n4️⃣ 后续怎么看？\n中国厂商在定价上会继续保持克制，等调查结果明朗。头部品牌产品定价高、全球产能灵活，应对能力比小厂强。海外建厂虽然成本高，但时间窗口拉长后效率提升空间更大。\n\n你觉得最终反倾销税会落到多少？欢迎一起讨论。\n\n[... middle omitted ...]\n\nn 14 months upon the announcement (Jan 19, 2027). On Jun 19, 2026, the EU announced that it will continue the anti-dumping investigation rather than imposing provisional measures at the curren\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R015",
    "title": "GS：中国家庭资产正在经历从房产到金融资产的结构性迁移",
    "digest": "[wechat_article.md]\n# GS：中国家庭资产正在经历从房产到金融资产的结构性迁移\n\n五月的经济数据提供了一个令人不安的对照：出口同比增长19.4%，但零售销售同比下降0.6%——这是除疫情封控期外，中国首次出现零售负增长。出口强劲与内需疲软之间的裂口，已经不只是周期性的问题，它正在重塑中国经济的底层结构。\n\nGS在最新发布的研报中，用一份长期专题研究给出了一个关键判断：中国家庭资产负债表的再平衡，可能才是理解未来五年资产价格走向的真正主线。这份报告的核心洞察不在于短期数据波动，而在于一个正在发生的结构性迁移——中国家庭资产正在从房产向金融资产转移，而这一过程的深度和速度，可能被市场严重低估。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 五月数据暴露的不只是需求疲软，而是家庭部门正在经历主动去杠杆\n\n五月零售销售同比下降0.6%，固定资产投资同样录得同比收缩。GS指出，这是“除疫情封控期外首次出现负增长”。出口增长19.4%与内需收缩并存，意味着中国经济的“双轨”格局已经固化：生产端和出口端依然有韧性，但消费端和投资端的动力正在流失。\n\n这里需要追问一个“所以呢”的问题：消费收缩是因为收入下降，还是因为家庭主动减少了支出？\n\nGS的报告虽然没有直接给出答案，但结合其同期发布的家庭资产负债表研究，逻辑链条是清晰的。中国家庭资产中房产占比高达52%，而房价持续下跌意味着家庭净资产在缩水。当资产端缩水时，家庭部门为了修复资产负债表，会主动减少消费、增加储蓄。这不是需求暂时被压抑，而是家庭部门正在经历一轮自发的去杠杆。\n\n这意味着，短期刺激政策可能难以撬动消费。如果家庭部门的去杠杆行为是结构性的，那么任何依赖消费反弹的经济预测都需要重新审视其假设。\n\n---\n\n![研报原图 2](assets/source_image_02.jpg\n\n[... middle omitted ...]\n\n细数据，逐一拆解这些关键假设的验证条件和潜在风险。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n出口强消费弱，中国5月数据再分化\n\n出口旺，内需冷\n\n1️⃣ 5月经济数据出现明显分化。工业生产同比+4.5%略超预期，但出口同比+19.4%是亮点，而零售同比下降0.6%，是除疫情封控外首次负增长。固定资产投资继4月后继续同比下滑。一句话：外需撑场面，内需在收缩。\n\n2️⃣ 陆家嘴论坛释放政策信号。央行宣布将隔夜回购利率走廊从70bp缩窄至50bp，进一步向价格型货币政策框架靠拢。同时推出境外机构人民币回购工具（FIMA）、香港5年期国债期货、上海离岸人民币交易等，人民币国际化明显提速。\n\n3️⃣ 中国家庭资产负债表结构正在转变。截至2026Q1，房产占家庭总资产52%，现金/存款占25%。研报预计未来几年，股权和保险占比将显著扩大，房产占比持续收缩。从买房囤钱，到股险配置，趋势已来。\n\n欢迎一起讨论：家庭资产从房产转向金融资产，你开始调整了吗？\n\n#学习笔记\n\n[source_mineru.md]\n# China: Three things in China\n\nThree quick highlights from China:\n\nHui Shan  \n+852-2978-6634 | hui.shan@\n\n[... middle omitted ...]\n\ntrong exports and weak domestic demand.\n\nBoth retail sales and fixed asset investment contracted year-over-year in May\n\n![](images/a3020284cdaa06923b7747a4a4f688c3d66d0177b88100180d09d91ff282a\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R016",
    "title": "GS：欧洲化工的真正危机不是红海冲突，而是冲突结束后暴露的结构性过剩",
    "digest": "[wechat_article.md]\n# GS：欧洲化工的真正危机不是红海冲突，而是冲突结束后暴露的结构性过剩\n\n当市场还在关注地缘冲突何时结束、物流何时恢复时，一份来自GS的研报给出了一个反直觉的判断：冲突的终结可能才是欧洲化工行业真正考验的开始。\n\nGS分析师团队在参加ICIS与欧洲化工分销商协会（Fecc）联合举办的CEO圆桌会议后，发布了一份基调偏冷的研究笔记。出席会议的包括Equilex董事会主席Patrick Elie、Integra Petrochemicals CEO Gina Fyffe、IMCD CEO Marcus Jordan以及National Chemical Co. CEO Alan Looney。这些行业高管的共识性判断，指向一个令人不安的前景：当前的市场疲软并非单纯的季节性因素，而是价值毁灭的真实信号。\n\n这份研报的核心洞察可以浓缩为一句话：欧洲化工行业正在经历一场“双重挤压”——短期面临需求疲软与物流紊乱带来的交易混乱，中期则面临中国产能外溢、欧洲本地产能永久性关停，以及结构性配方重构的三重冲击。GS认为，真正值得关注的不是冲突何时结束，而是结束后暴露出来的过剩产能将如何重塑全球化工竞争格局。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 冲突结束并非利好，而是暴露潜在过剩产能的催化剂\n\n市场普遍认为红海冲突的结束将带来供应链正常化，但GS从圆桌会议中捕捉到的信号恰恰相反：冲突结束可能让行业变得更糟。\n\nIntegra Petrochemicals的CEO明确指出，即使假设冲突已经结束，正常化所需的时间将远超预期。仅清理积压的船舶就需要6至8周。第三季度预计将非常混乱，因为买家害怕做决策，对公平定价存在不确定性。\n\n更深层的担忧在于，一旦冲突结束，生产恢复常态，供应重新变得充足，市场将直接暴露在潜在过剩产能面前。这\n\n[... middle omitted ...]\n\n里继续讨论，我们将分享原始报告全文与更多交叉验证的数据分析。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n欧洲化工，下半年真的难\n\n欧洲化工，下半年会更难\n\n一场闭门会议，10个关键信号\n\n最近参加了一场欧洲化工分销商CEO圆桌，聊的是下半年怎么看。整体基调很冷，几个点值得记下来。\n\n1/ 真正的价值毁灭来了，不只是季节性疲软。有CEO说，就算冲突结束，恢复正常也要6-8周清船。Q3会很乱，买家不敢决策，不确定什么才是合理价格。\n\n2/ 中国正在“趁势”抢占份额。国内需求弱+产能过剩，中国化工品正大量出口。3-4月中国对亚洲其他地区的化工品出口增长了70%。\n\n3/ 配方重构在加速。原料太贵，很多公司开始改配方。有些可能是临时调整，但有些可能永久改变。这对传统原料需求是结构性威胁。\n\n4/ 下游更看重创新能力了。越往特种化学品走，客户越在意供应商的研发实力和长期合作能力，而不是只拼价格。\n\n5/ 欧洲本地采购比例明显下降，从3年前的80%降到现在约60%。但客户其实还是偏爱欧洲本地生产，只是很多产品欧洲根本不产了。\n\n6/ 客户在主动降低库存。供应链持续不稳定，客户更倾向于减少资金占用，对分销商的库存管理和预测能力要求更高了。\n\n7/ 涨价终于落地了。一开始供应商不敢涨太多，怕丢份额。但冲突持续太久，已经推了一两\n\n[... middle omitted ...]\n\nading into the second half of the year, with clear signals of value destruction observed alongside seasonal demand weakness. Commentary was consistent in noting that a potential resolution to \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R017",
    "title": "摩根斯坦利：市场低估的不是AI需求，而是供给端结构性约束的定价权",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：市场低估的不是AI需求，而是供给端结构性约束的定价权\n\n这份研报的核心判断并不复杂，却容易被当前高涨的情绪掩盖：半导体周期的驱动力正在从需求侧的单边拉动，转向供给侧的结构性约束与客户长期承诺的博弈。摩根斯坦利在最新周报中同时上调了美光（Micron）的盈利预期，并维持对Cerebras Systems的看好，但真正值得关注的不是数字本身，而是支撑这些数字背后的逻辑正在发生质变。\n\n市场习惯于用“AI需求爆发”来解释一切上涨，但这份报告揭示了一个更微妙的层次——当需求已经充分预期，真正决定下一阶段回报率的，是企业能否将规模转化为议价权，以及供给端的技术与资本约束能否被突破。这正是当前半导体投资中容易被忽视的第二层思考。\n\n这份报告发布于6月18日，覆盖美光（MU）和Cerebras Systems（CBRS）两家公司即将发布的财报。摩根斯坦利对两者均给予“超配”（Overweight）评级，美光目标价1050美元，Cerebras目标价未在摘要中明确给出，但分析师强调其“差异化架构”是核心看点。然而，在看似乐观的表象下，报告埋下了几个值得深挖的关键线索。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 美光的盈利上调并非终点，而是供给约束重新定价的起点\n\n摩根斯坦利将美光5月季度（F3Q26）的EPS预期从20.57美元上调至21.31美元，8月季度（F4Q26）从25.00美元上调至26.01美元。驱动因素非常直接：DRAM和NAND的ASP涨幅均超出此前预期。报告将DRAM ASP环比涨幅从40%上调至45%，NAND从35%上调至50%，而第三方预测甚至更高——DRAM约60%，NAND约75%。\n\n但真正有洞察力的部分不是这些数字本身，而是分析师如何看待这些数字的可持续性。报告明确指出：“比强\n\n[... middle omitted ...]\n\n能否兑现市场预期。这些讨论的价值，往往比研报本身更值得关注。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nDRAM短缺还在加剧，这家公司下周财报是关键\n\nDRAM涨价还在加速\n\n某外资投行刚刚上调了美光（MU）的预期，原因是存储芯片供不应求的情况比之前更严重了，尤其是DRAM。\n\n1️⃣ 涨价幅度超预期\n- 5月季度原本指引ASP涨30-35%，现在模型上调到DRAM涨45%、NAND涨50%\n- 第三方预测更激进：C2Q DRAM涨60%、NAND涨75%\n- EPS预期21.31美元，高于市场共识20.57美元\n- 8月季度预计继续涨价20%左右，有上行可能\n\n2️⃣ 供需缺口短期难解\n- 需求端：客户在所有市场都面临“做艰难决定”，说明短缺是持续的\n- 供应端：即使资本支出上调到270亿美元，实际bit出货增长仍只有中个位数，远低于需求增速\n- 新厂建设周期、HBM良率损耗、制程迁移效率都在限制供应响应速度\n\n3️⃣ 长期合同是市场关注的焦点\n- 上次披露签了5年战略客户协议，但细节很少\n- 这次可能宣布更多交易，但不一定透露条款细节\n- 这些合同对市场信心很重要，如果信息有限，股价可能短期承压\n\n另外Cerebras（CBRS）也将首次作为上市公司发布财报，核心关注点是250MW产能部署进度，预计2027\n\n[... middle omitted ...]\n\nlspan=\"2\">Research Associate</td></tr><tr><td>Mason.Wayne@morganstanley.com</td><td>+1 212 761-6012</td></tr><tr><td colspan=\"2\">Shane Brett</td></tr><tr><td colspan=\"2\">Equity Analyst</td></t\n\n[... middle omitted ...]\n\nSynopsys Inc. (SNPS.O)</td><td>E (02/27/2026)</td><td>$455.51</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R018",
    "title": "NOM：人民币中间价模型正在传递一个比市场预期更克制的信号",
    "digest": "[wechat_article.md]\n# NOM：人民币中间价模型正在传递一个比市场预期更克制的信号\n\n这份NOM亚洲外汇策略团队的最新报告，看似只更新了一个每日模型预测数字，但拆解其内部结构和参数调整后，一个清晰的信号浮现出来：当前人民币定价机制中的“逆周期因子”正在发挥比表面数字更重要的校准作用，市场对汇率单向波动的定价可能过于激进。\n\n报告的核心判断并不复杂：NOM模型给出的美元兑人民币中间价预测为6.7787，较前次预测下移了343个基点。但当我们把目光从绝对数字移开，聚焦于模型内部的结构性调整时，会发现一个更具深意的变化——计入逆周期因子后的预测值为6.8008，与前一交易日官方收盘价的偏离仅为122个基点。这个差值，才是真正值得关注的信号。\n\n市场往往习惯于将注意力集中在人民币汇率的绝对水平上，讨论“破7”还是“守7”，讨论升值还是贬值的方向。但这份NOM报告提示了一个更精细的观察维度：政策制定者正在通过逆周期因子，对模型输出的“纯粹”市场定价进行微调，而这种微调的幅度和频率，才是理解当前汇率政策意图的真正钥匙。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 模型预测的下移并非线性趋势，而是多重短期因素的一次性校准\n\nNOM模型预测从6.8130下移至6.7787，表面上看是343个基点的显著变化。但报告中的“无逆周期因子模型预测”和“含逆周期因子模型预测”两个数值的差异，揭示了这并非一个简单的方向性信号。\n\n从报告提供的图表看，模型误差和隔夜贡献因素的变化，是推动预测下移的主要驱动力。这些因素包括隔夜美元指数的波动、其他亚洲货币的交叉汇率变动、以及市场情绪的短期扰动。它们具有明显的时效性，而非结构性趋势的改变。\n\n一个关键点在于：模型预测的下移幅度，与官方中间价的实际调整幅度之间存在差距。这种差距本身就是一种政策信号。当市场参与者单纯追\n\n[... middle omitted ...]\n\n辑有更深入的兴趣，这些讨论或许能提供比单篇报告更完整的视角。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n人民币汇率最新模型推演\n🔍 6.7787\n某外资投行下调预测\n\n最近翻到一份关于亚洲汇率（除日本）的研报，内容挺扎实，直接拉出来给大家拆着看。\n\n1️⃣ 模型核心数字\n- 最新预测：6.7787\n- 对比上次预测：6.8130（下调了343个基点）\n- 对比官方收盘价：高了164个基点\n- 加入逆周期因子后：6.8008（比上次定盘价低122个基点）\n\n2️⃣ 逆周期因子的作用\n这个因子是央行用来平滑汇率波动的工具。加入了它之后，预测值从6.7787调整到6.8008，说明模型在考虑政策干预后的结果会更温和一些。\n\n3️⃣ 值得关注的时间节点\n研报列了2026年下半年几个重要事件：\n- 7月底：政治局经济工作会议\n- 10月初：国庆黄金周\n- 11月：APEC峰会（深圳）\n- 12月中旬：中央经济工作会议\n- 12月底：政治局会议\n- 年底：可能有中美高层会晤\n\n这些节点往往会影响市场预期和汇率波动，值得跟踪。\n\n4️⃣ 一点思考\n模型预测下调，更多反映的是短期市场情绪和资金流向变化。汇率的实际走向还会受到政策、贸易谈判、经济数据等多重因素影响。\n\n欢迎一起讨论你对下半年汇率走势的看法。\n\n#学习笔记\n\n[s\n\n[... middle omitted ...]\n\nf6a3b7e5d8ab22fb3c1873162996bcdba69531c57e2fdbc15a.jpg)  \nSource: NOM\n\nFig. 2: Recent model errors (without counter-cyclical factor adjustment)  \n![](images/3490db29059e7dcff03a4c858b067a9ff4c\n\n[... middle omitted ...]\n\nOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R019",
    "title": "Bernstein：日本零售业真正被低估的不是消费复苏，而是供给侧的整合拐点",
    "digest": "[wechat_article.md]\n# Bernstein：日本零售业真正被低估的不是消费复苏，而是供给侧的整合拐点\n\n全球投资者长期将日本国内零售视为一个“已被充分讨论”的市场——人口萎缩、增长有限、整合停滞。这种看法本身并没有错，但它遗漏了一个关键变量：过去三十年“失去的岁月”同时也是一个漫长的通缩过滤器，弱者被淘汰，幸存者的运营效率在压力下持续进化。Bernstein最新发布的日本零售系列报告提出了一个与市场共识截然不同的判断：日本国内零售业正在接近一个加速整合的拐点，而这一变化的驱动力已经从周期性转向结构性。\n\n这份报告的核心洞见在于，日本零售业当前面临的不是需求端的短期波动，而是供给端成本结构的根本性重塑。超市行业约1.5%的经营利润率，对应着约14%的人工成本率——这个方程式在最低工资自2015年以来累计上涨超过30%、远超CPI约10%涨幅的背景下，已经变得不可持续。支撑行业碎片化的传统支柱——店内生鲜加工、地理分散化、对非正规劳动力的依赖——正在同时瓦解。规模较小的企业，缺乏投资自动化和中央加工的能力，正在被系统性边缘化。\n\n这与西方零售业完成整合的历史路径不同。西欧和美国在几十年前就完成了这一过程，而日本现在才进入“中场局”。对于产业决策者和投资者而言，这意味着一个清晰的、未来十年的集中度提升路径正在形成，而非市场普遍预期的“一成不变”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 消费者行为的分裂正在结构性淘汰中间业态\n\n日本现代消费者呈现出一种鲜明的二元模式：工作日的“效用型”购物——快速、功能性支出集中在药妆店——与周末的“寻宝型”消费在折扣零售商处完成。这种分裂几乎没有给中间路线业态留下生存空间。\n\n综合超市（GMS）曾经是“一站式解决方案”，但现在正被专业零售商和更聚焦的业态持续蚕食品类份额。结果是，GMS逐渐变成了一\n\n[... middle omitted ...]\n\n的一线调研反馈，以及对这些关键问题的持续跟踪分析。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本零售，终于熬出头了\n\n📈 行业拐点来了\n\n日本零售正在经历一场“倒逼式”洗牌。\n\n过去30年通货紧缩，像一场漫长的冬天——弱的店被淘汰，活下来的都练出了效率。现在，这个淘汰过程终于要加速了。\n\n📌 为什么说拐点到了？\n\n1️⃣ 人力成本压力拉爆\n超市利润率才1.5%，但人力成本占比高达14%。2015年以来日本最低工资涨了30%，CPI只涨了10%。小玩家没有钱搞自动化，越来越难活。\n\n2️⃣ 消费习惯两极分化\n日本消费者现在工作日去药妆店快速买必需品，周末去折扣店“寻宝”。中间地带的百货超市（GMS）两边不讨好，地位越来越尴尬。\n\n3️⃣ 行业整合窗口打开\n欧美零售整合早就完成了，日本现在才进“中局”。未来10年，集中度会明显提高，龙头效应会更强。\n\n📌 谁更值得关注？\n\n折扣店模式最吃香。某外资投行看好PPIH（唐吉诃德母公司），因为它走的是“高毛利率×高成本×高利润”的独特路线，而且免税销售和自有品牌还有增长空间。\n\n便利店巨头Seven & i处于中性评级——核心业务增长见顶，加盟商压力大，但因为有收购预期，股价还有一定支撑。\n\n永旺（AEON）被看空，估值已经很高，市场对整合效应的期待可能过于乐\n\n[... middle omitted ...]\n\nthe forest: weaker trees withered, survivors hardened, and space gradually opened beneath the canopy. Now, as the frost lifts, sunlight is finally reaching the ground.\n\nJapan's domestic retail\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R020",
    "title": "GS：软件行业的真正分水岭不是AI本身，而是“好粘性”与“坏粘性”的重新定价",
    "digest": "[wechat_article.md]\n# GS：软件行业的真正分水岭不是AI本身，而是“好粘性”与“坏粘性”的重新定价\n\nDatabricks年度大会结束后，GS软件团队发布了一份不同寻常的报告。它没有罗列产品更新清单，而是提出了一个判断：软件行业的估值分化将加速，而分化的核心变量不是AI能力的有无，而是“粘性”的质量。\n\n这份报告的洞察起点是一个简单却尖锐的问题：当AI让数据迁移成本骤降，哪些软件公司的护城河会变浅？哪些反而会更深？GS分析师给出的框架是“好粘性”与“坏粘性”之分。前者靠持续创新和客户热爱来锁定用户，后者依赖历史遗留的迁移成本。AI正在系统性地瓦解后者。\n\n这意味着，未来12-18个月，软件投资的核心命题不再是“谁有AI故事”，而是“谁的商业模式经得起重新定价”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 迁移成本正在被AI工具系统性地压低，依赖“坏粘性”的公司面临估值重塑\n\nGS的报告明确点出了一个被市场低估的结构性变化：AI不仅改变了软件的功能边界，更改变了竞争的基础设施。过去，一家SaaS公司只要把客户数据锁在自己的格式里，就能获得相当可观的定价权。客户即使不满意，也会因为迁移成本过高而选择留下。这种“坏粘性”曾经是很多软件公司利润率的基石。\n\n但Databricks在大会上的产品发布，尤其是LTAP（Lake Transactional/Analytical Processing）和Open Sharing协议，清晰地展示了新范式：数据可以在开放格式下自由流动，分析引擎和事务引擎可以共享同一个数据源。当客户的数据不再被某个特定平台绑架，迁移成本就大幅下降。\n\nGS分析师特别指出，Databricks的定价策略本身就反映了这种逻辑。公司内部明确表示，它可以选择定价高出两倍，但短期定价优化往往会牺牲长期竞争力和客户终身价值。\n\n[... middle omitted ...]\n\n演进，并结合完整报告中的原始图表和财务数据，做更深度的推演。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n好粘 vs 坏粘性，软件公司怎么选\n\n软件护城河在变\n\n最近投行研报聊了一个很有意思的框架：软件公司的“粘性”分好坏。\n\n好粘性 = 产品迭代快 + 客户真心爱用。比如Shopify、Cloudflare，定价有杀伤力，目标是长期市场份额。\n\n坏粘性 = 创新放缓，但客户懒得迁移。这种护城河正在被AI侵蚀——现在用AI做数据迁移比以前容易太多了。\n\n1️⃣ 数据平台的新逻辑\nDatabricks的DAIS大会透露出几个关键信号：\n- 开放标准 + 易用数据接入 = 好数据质量 = 好AI结果\n- 企业定制化agent应用正在崛起，填补传统SaaS之间的空白\n- 价值正在向能打通这两个架构的公司集中\n\n2️⃣ 定制 vs 标准化应用\n最有意思的agent应用，大概率会出现在传统SaaS的缝隙里。\n复杂组织倾向于自建，简单场景用SaaS现成方案。\n研报预计：到2030年，软件TAM会因agentic应用增长20%。\n\n3️⃣ 数据库技术的暗线\n当大家都在聊agentic时，Databricks在默默升级底层数据库。\nLTAP技术解决了40年的数据库工程难题——把OLTP和OLAP统一到一个平台。\nPostgres\n\n[... middle omitted ...]\n\ncific use cases that sit in the white space between classic SaaS systems, in turn supported by a unified operation system/ontology layer with governance and model controls. Our conversations s\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "Exhibit 1",
    "context": "Exhibit 1: According to Our Nowcast, Global EV Car Sales Penetration Has Increased By 3.4pp Since the Beginning of the Hormuz Shock"
  },
  {
    "figure_id": "F002",
    "report_id": "R001",
    "label": "Exhibit 1",
    "context": "Exhibit 3: The Increase in Global EV Car Sales Penetration Since February Has Been Driven 61% By China, 21% By OECD, and 19% By Non OECD ex China"
  },
  {
    "figure_id": "F003",
    "report_id": "R001",
    "label": "Exhibit 1",
    "context": "Exhibit 3: The Increase in Global EV Car Sales Penetration Since February Has Been Driven 61% By China, 21% By OECD, and 19% By Non OECD ex China Exhibit 4: 12 Out of the 15 Largest EV Markets Have Experienced an Increase in EV C"
  },
  {
    "figure_id": "F004",
    "report_id": "R001",
    "label": "Exhibit 2",
    "context": "Exhibit 4: 12 Out of the 15 Largest EV Markets Have Experienced an Increase in EV Car Sales Penetration Since February For 15 largest EV markets by 2025 sales volume. Solid bars indicate that May share is calculated using realize"
  },
  {
    "figure_id": "F005",
    "report_id": "R001",
    "label": "Exhibit 3",
    "context": "Exhibit 6: EV Car Sales Have Accelerated Meaningfully Since February Across the World ex US"
  },
  {
    "figure_id": "F006",
    "report_id": "R001",
    "label": "Exhibit 6",
    "context": "Exhibit 6: EV Car Sales Have Accelerated Meaningfully Since February Across the World ex US Red diamonds indicate data points that are nowcasted. The vertical line on each chart indicates the start of the Hormuz shock. Exhibit"
  },
  {
    "figure_id": "F007",
    "report_id": "R001",
    "label": "Exhibit 6",
    "context": "Exhibit 6: EV Car Sales Have Accelerated Meaningfully Since February Across the World ex US Red diamonds indicate data points that are nowcasted. The vertical line on each chart indicates the start of the Hormuz shock. Exhibit"
  },
  {
    "figure_id": "F008",
    "report_id": "R002",
    "label": "Exhibit 2",
    "context": "EXHIBIT 2: We estimate global video gaming revenue reached US\\$218bn in 2025, +4.8% year on year EXHIBIT 3: Our video gaming model breaks down the global revenue pool by platform and by region EXHIBIT 4: 2025 was a strong year"
  },
  {
    "figure_id": "F009",
    "report_id": "R002",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 5: North American growth stayed muted in 2025, while other regions rebounded"
  },
  {
    "figure_id": "F010",
    "report_id": "R002",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Our video gaming model breaks down the global revenue pool by platform and by region EXHIBIT 4: 2025 was a strong year for console, helped by the Switch 2 launch EXHIBIT 5: North American growth stayed muted in 2025,"
  },
  {
    "figure_id": "F011",
    "report_id": "R002",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: 2025 was a strong year for console, helped by the Switch 2 launch EXHIBIT 5: North American growth stayed muted in 2025, while other regions rebounded 2025: Global gaming market revenue by region EXHIBIT 6: Asia-Pa"
  },
  {
    "figure_id": "F012",
    "report_id": "R002",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: North American growth stayed muted in 2025, while other regions rebounded 2025: Global gaming market revenue by region EXHIBIT 6: Asia-Pacific is mobile dominated, while console leads elsewhere EXHIBIT 7: Console is"
  },
  {
    "figure_id": "F013",
    "report_id": "R002",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: Asia-Pacific is mobile dominated, while console leads elsewhere EXHIBIT 7: Console is biggest in Europe and North America, while Asia dominates mobile and PC ## WINNERS AND LOSERS IN 2025 Company-level growth in the in"
  },
  {
    "figure_id": "F014",
    "report_id": "R002",
    "label": "Exhibit 8",
    "context": "EXHIBIT 8: Tencent, Nintendo, and Roblox led incremental revenue growth in 2025 versus the prior year 2025 vs. 2024: Global video gaming companies incremental revenue 2025 vs. 2024: Global video gaming companies revenue growth EX"
  },
  {
    "figure_id": "F015",
    "report_id": "R002",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: Tencent, Nintendo, and Roblox led incremental revenue growth in 2025 versus the prior year 2025 vs. 2024: Global video gaming companies incremental revenue 2025 vs. 2024: Global video gaming companies revenue growth EX"
  },
  {
    "figure_id": "F016",
    "report_id": "R002",
    "label": "Exhibit 14",
    "context": "EXHIBIT 10: We’ve updated our tally of R&D expenses per employee across the global video gaming industry... 2025: Global video game companies R&D expenses per employee EXHIBIT 11: ...the fact Asian developers have a fraction of th"
  },
  {
    "figure_id": "F017",
    "report_id": "R002",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 12: The companies we cover own some of the world's top IPs, an important input into video game sales success Top 15 bestselling game franchises on VGChartz EXHIBIT 13: The live service game scene is dominated by a collecti"
  },
  {
    "figure_id": "F018",
    "report_id": "R002",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 14: The ongoing wave of video gaming studio shutdowns in Western markets was overdue in our view, and should help to move the industry to a more favourable part of the capital cycle"
  },
  {
    "figure_id": "F019",
    "report_id": "R002",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 14: The ongoing wave of video gaming studio shutdowns in Western markets was overdue in our view, and should help to move the industry to a more favourable part of the capital cycle"
  },
  {
    "figure_id": "F020",
    "report_id": "R002",
    "label": "Exhibit 19",
    "context": "EXHIBIT 15: We model 0.7% aggregate industry revenue growth in 2026, slower year on year to reflect Playstation hardware declines, and a higher base for Nintendo EXHIBIT 16: We model faster PC growth continuing in 2026, low-single"
  },
  {
    "figure_id": "F021",
    "report_id": "R002",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 16: We model faster PC growth continuing in 2026, low-single digit growth mobile growth, and lower console revenue growth than in 2025 EXHIBIT 17: Consensus forecasts point to slower growth in the next few quarters, follow"
  },
  {
    "figure_id": "F022",
    "report_id": "R002",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 17: Consensus forecasts point to slower growth in the next few quarters, followed by faster growth into year-end, partly reflecting the GTA VI launch EXHIBIT 18: In hindsight, mid-2024 was the trough of the post-Covid down"
  },
  {
    "figure_id": "F023",
    "report_id": "R002",
    "label": "EXHIBIT 18",
    "context": "EXHIBIT 18: In hindsight, mid-2024 was the trough of the post-Covid down cycle for video gaming industry revenue EXHIBIT 19: The industry's desire to avoid competing with the GTA VI launch has contributed to a logjam of new games"
  },
  {
    "figure_id": "F024",
    "report_id": "R002",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 21: We think engagement concerns in video gaming are partly backward looking... EXHIBIT 23: PSN engagement has remained resilient into the end of the current console cycle"
  },
  {
    "figure_id": "F025",
    "report_id": "R002",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 21: We think engagement concerns in video gaming are partly backward looking... EXHIBIT 23: PSN engagement has remained resilient into the end of the current console cycle Sony GNS - PSN MAUs EXHIBIT 24: ...while the s"
  },
  {
    "figure_id": "F026",
    "report_id": "R002",
    "label": "EXHIBIT 22",
    "context": "EXHIBIT 25: The normalisation of Roblox engagement back near the pre-2025 trend-line has been interesting to observe, and puts claims around Roblox disrupting the industry into perspective"
  },
  {
    "figure_id": "F027",
    "report_id": "R002",
    "label": "EXHIBIT 23",
    "context": "EXHIBIT 25: The normalisation of Roblox engagement back near the pre-2025 trend-line has been interesting to observe, and puts claims around Roblox disrupting the industry into perspective"
  },
  {
    "figure_id": "F028",
    "report_id": "R002",
    "label": "EXHIBIT 25",
    "context": "EXHIBIT 25: The normalisation of Roblox engagement back near the pre-2025 trend-line has been interesting to observe, and puts claims around Roblox disrupting the industry into perspective ## THE BULL CASE FOR PC GAMING GROWTH Ass"
  },
  {
    "figure_id": "F029",
    "report_id": "R002",
    "label": "Exhibit 26",
    "context": "EXHIBIT 26: Our views on PC growth last year align more with Newzoo's modelling of revenue acceleration EXHIBIT 27: Steam continues to grow faster than the aggregate PC market EXHIBIT 28: A majority of PCs on Steam can now play"
  },
  {
    "figure_id": "F030",
    "report_id": "R002",
    "label": "EXHIBIT 26",
    "context": "EXHIBIT 29: The PC market in China saw a significant acceleration in growth following the Black Myth Wukong success... we think other markets are due to follow in the coming years"
  },
  {
    "figure_id": "F031",
    "report_id": "R002",
    "label": "EXHIBIT 27",
    "context": "EXHIBIT 29: The PC market in China saw a significant acceleration in growth following the Black Myth Wukong success... we think other markets are due to follow in the coming years FY3/21-FY3/25: Capcom unit sales by region"
  },
  {
    "figure_id": "F032",
    "report_id": "R002",
    "label": "EXHIBIT 28",
    "context": "EXHIBIT 30: Capcom's success has partly been driven by expansion on PC, and in emerging markets EXHIBIT 31: eFootball has also seen Steam CCUs ramp considerably in recent years"
  },
  {
    "figure_id": "F033",
    "report_id": "R002",
    "label": "EXHIBIT 29",
    "context": "EXHIBIT 31: eFootball has also seen Steam CCUs ramp considerably in recent years ## WE USE SENSOR TOWER TO TRACK MOBILE GAMING BILLINGS"
  },
  {
    "figure_id": "F034",
    "report_id": "R002",
    "label": "EXHIBIT 30",
    "context": "EXHIBIT 30: Capcom's success has partly been driven by expansion on PC, and in emerging markets EXHIBIT 31: eFootball has also seen Steam CCUs ramp considerably in recent years ## WE USE SENSOR TOWER TO TRACK MOBILE GAMING BILLI"
  },
  {
    "figure_id": "F035",
    "report_id": "R002",
    "label": "EXHIBIT 32",
    "context": "EXHIBIT 32: We've modelled 1% global mobile game billings growth in 2026 EXHIBIT 33: Google's announcement of lower platform fees will represent an earnings tailwind for mobile developers EXHIBIT 34: iOS platform fees were recen"
  },
  {
    "figure_id": "F036",
    "report_id": "R002",
    "label": "EXHIBIT 32",
    "context": "EXHIBIT 32: We've modelled 1% global mobile game billings growth in 2026 EXHIBIT 33: Google's announcement of lower platform fees will represent an earnings tailwind for mobile developers EXHIBIT 34: iOS platform fees were recen"
  },
  {
    "figure_id": "F037",
    "report_id": "R002",
    "label": "EXHIBIT 33",
    "context": "EXHIBIT 33: Google's announcement of lower platform fees will represent an earnings tailwind for mobile developers EXHIBIT 34: iOS platform fees were recently cut in Europe and China, which helps too ## WE MODEL CONSOLE BOTTOM-U"
  },
  {
    "figure_id": "F038",
    "report_id": "R002",
    "label": "Exhibit 39",
    "context": "EXHIBIT 37: Software sales revenue outweighs hardware sales for console platforms"
  },
  {
    "figure_id": "F039",
    "report_id": "R002",
    "label": "EXHIBIT 36",
    "context": "EXHIBIT 36: This drives our estimate of the respective console installed bases FY3/08-FY3/28E: Console hardware install base EXHIBIT 37: Software sales revenue outweighs hardware sales for console platforms 2025: Sony and Nintendo"
  },
  {
    "figure_id": "F040",
    "report_id": "R002",
    "label": "EXHIBIT 36",
    "context": "EXHIBIT 38: We model both Sony and Nintendo on the basis of billings, grossing up third-party games 2025: Sony and Nintendo game billing breakdown Hardware billings Software billings Subscription billings"
  },
  {
    "figure_id": "F041",
    "report_id": "R002",
    "label": "EXHIBIT 37",
    "context": "EXHIBIT 39: High memory prices represent an obvious headwind for both in 2026 and onwards Q2 2026 vs. Q2 2025: DRAM+SSD share of bill of materials cost"
  },
  {
    "figure_id": "F042",
    "report_id": "R002",
    "label": "EXHIBIT 38",
    "context": "EXHIBIT 40: Current contract pricing implies further downside to hardware margins ## AI ADOPTION UPDATE: JAPAN NOW ON BOARD"
  },
  {
    "figure_id": "F043",
    "report_id": "R002",
    "label": "EXHIBIT 39",
    "context": "EXHIBIT 39: High memory prices represent an obvious headwind for both in 2026 and onwards Q2 2026 vs. Q2 2025: DRAM+SSD share of bill of materials cost EXHIBIT 40: Current contract pricing implies further downside to hardware marg"
  },
  {
    "figure_id": "F044",
    "report_id": "R002",
    "label": "Exhibit 44",
    "context": "EXHIBIT 43: AI doesn't solve for visibility, IP and name recognition do... the number of truly popular games launched each year has remained roughly constant over time"
  },
  {
    "figure_id": "F045",
    "report_id": "R002",
    "label": "EXHIBIT 41",
    "context": "EXHIBIT 43: AI doesn't solve for visibility, IP and name recognition do... the number of truly popular games launched each year has remained roughly constant over time EXHIBIT 44: The video gaming industry has increasingly found w"
  },
  {
    "figure_id": "F046",
    "report_id": "R002",
    "label": "EXHIBIT 42",
    "context": "EXHIBIT 44: The video gaming industry has increasingly found ways to integrate AI into development workflows..."
  },
  {
    "figure_id": "F047",
    "report_id": "R003",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 2: While cloud revenue growth has accelerated in the recent quarters, it needs to continue accelerating to keep up with the pace of capex growth Quarterly Cloud Revenue: AWS+Azure+GCP+OCI Based on calendar quarters (Calen"
  },
  {
    "figure_id": "F048",
    "report_id": "R003",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 3: On the other hand, ignoring contract duration, total backlog (RPO) growth has accelerated significantly across all hypersclaers in recent quarters, totaling \\$2T as of 1Q26"
  },
  {
    "figure_id": "F049",
    "report_id": "R003",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 5: Meanwhile, as hyperscalers are running out of internal funding, to increase Capex further they likely need to (and have been) raise capital, through either debt or equity"
  },
  {
    "figure_id": "F050",
    "report_id": "R003",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 5: Meanwhile, as hyperscalers are running out of internal funding, to increase Capex further they likely need to (and have been) raise capital, through either debt or equity Hyperscaler Cash Flow vs. Capex, CY 26E Based o"
  },
  {
    "figure_id": "F051",
    "report_id": "R003",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: So, which tale would you rather believe? Y/Y Growth%: Revenue vs. Capex vs. CFO vs. Backlog EXHIBIT 5: Meanwhile, as hyperscalers are running out of internal funding, to increase Capex further they likely need to (and"
  },
  {
    "figure_id": "F052",
    "report_id": "R003",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: The five hyperscale providers report Cloud revenue, which includes not only IaaS/PaaS but also other revenues Google includes Workspace. Microsoft Azure revenue is based on our estimates. EXHIBIT 7: In Q1 CY26, Microso"
  },
  {
    "figure_id": "F053",
    "report_id": "R003",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 8: On a Q/Q basis, AWS added \\$2.0B vs Azure at \\$2.5B vs Google Cloud at \\$2.4B vs Oracle at \\$0.9B EXHIBIT 9: Of the incremental dollars added Q/Q by the hyperscale Cloud providers (excluding BABA), Google and Oracle ha"
  },
  {
    "figure_id": "F054",
    "report_id": "R003",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 10: Q over Q, incremental share gained by each hyperscaler (excluding Alibaba)"
  },
  {
    "figure_id": "F055",
    "report_id": "R003",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 10: Q over Q, incremental share gained by each hyperscaler (excluding Alibaba) All quarters represent calendar quarters, Google's cloud revenues include both GCP and Workspace. Microsoft Azure numbers are based on estimate"
  },
  {
    "figure_id": "F056",
    "report_id": "R003",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: Of the incremental dollars added Q/Q by the hyperscale Cloud providers (excluding BABA), Google and Oracle have gained incremental shares this quarter. Microsoft Azure numbers are based on estimates EXHIBIT 10: Q over"
  },
  {
    "figure_id": "F057",
    "report_id": "R003",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: AWS Backlog grew to \\$364B up \\~50% from the \\$244B announced in 4Q25 EXHIBIT 12: AWS average contract life rose Q/Q to 5.5 years in 1Q26 AWS Weighted average contract life (Yrs.) ## Microsoft Azure"
  },
  {
    "figure_id": "F058",
    "report_id": "R003",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: AWS Backlog grew to \\$364B up \\~50% from the \\$244B announced in 4Q25 EXHIBIT 12: AWS average contract life rose Q/Q to 5.5 years in 1Q26 AWS Weighted average contract life (Yrs.) ## Microsoft Azure \\- Microsoft Azur"
  },
  {
    "figure_id": "F059",
    "report_id": "R003",
    "label": "EXHIBIT 13",
    "context": "EXHIBIT 13: Microsoft Azure constant currency growth Azure Revenue growth (CC) EXHIBIT 14: CAPEX has gone up as Microsoft continues to invest in AI to meet demand Microsoft Total Capex (Cash + Financial Lease), in \\$B"
  },
  {
    "figure_id": "F060",
    "report_id": "R003",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: CAPEX has gone up as Microsoft continues to invest in AI to meet demand Microsoft Total Capex (Cash + Financial Lease), in \\$B ## Google Cloud \\- Google Cloud is gaining solid ground, with revenue surging 63% Y/Y to ex"
  },
  {
    "figure_id": "F061",
    "report_id": "R003",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: Google cloud's backlog of \\$460B nearly doubled Q/Q EXHIBIT 16: Revenue/backlog ratio significantly increased sequentially for Google Cloud ## Alibaba"
  },
  {
    "figure_id": "F062",
    "report_id": "R003",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: Google cloud's backlog of \\$460B nearly doubled Q/Q EXHIBIT 16: Revenue/backlog ratio significantly increased sequentially for Google Cloud ## Alibaba \\- Alibaba's cloud revenue is reported on a gross basis inclusive"
  },
  {
    "figure_id": "F063",
    "report_id": "R003",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 17: OCI revenue guidance through FY30 (CY29-30) EXHIBIT 18: Oracle RPO and CRPO OCI 5Y Revenue Guidance (FY26-30) ## WHAT ABOUT MARGINS? AI, we believe, is going to be a drag on gross margins at least during the build-ou"
  },
  {
    "figure_id": "F064",
    "report_id": "R003",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 17: OCI revenue guidance through FY30 (CY29-30) EXHIBIT 18: Oracle RPO and CRPO OCI 5Y Revenue Guidance (FY26-30) ## WHAT ABOUT MARGINS? AI, we believe, is going to be a drag on gross margins at least during the build-ou"
  },
  {
    "figure_id": "F065",
    "report_id": "R003",
    "label": "EXHIBIT 20",
    "context": "EXHIBIT 20: Software Moat Overview EXHIBIT 21: GPU Cloud Landscape (Scale v. Sophistication) Sophistication / (SemiAnalysis ClusterMAX 2.0) EXHIBIT 22: CRWV Revenue Growth CRWV Revenue Growth"
  },
  {
    "figure_id": "F066",
    "report_id": "R003",
    "label": "EXHIBIT 22",
    "context": "EXHIBIT 22: CRWV Revenue Growth CRWV Revenue Growth EXHIBIT 23: CRWV Debt Overview (Times, %) CRWV Debt Overview Leverage calculated as LTM Adj. EBITDA over net debt"
  },
  {
    "figure_id": "F067",
    "report_id": "R003",
    "label": "EXHIBIT 23",
    "context": "EXHIBIT 23: CRWV Debt Overview (Times, %) CRWV Debt Overview Leverage calculated as LTM Adj. EBITDA over net debt EXHIBIT 24: CRWV CAPEX Expense (\\$B, %) CRWV CAPEX Expense EXHIBIT 25: CRWV Capital Intensity (Times) CRWV Capital"
  },
  {
    "figure_id": "F068",
    "report_id": "R003",
    "label": "EXHIBIT 24",
    "context": "EXHIBIT 24: CRWV CAPEX Expense (\\$B, %) CRWV CAPEX Expense EXHIBIT 25: CRWV Capital Intensity (Times) CRWV Capital Intensity \\- CoreWeave's margin profile is currently depressed by a structural OpEx–revenue lag. The company begi"
  },
  {
    "figure_id": "F069",
    "report_id": "R003",
    "label": "EXHIBIT 24",
    "context": "EXHIBIT 24: CRWV CAPEX Expense (\\$B, %) CRWV CAPEX Expense EXHIBIT 25: CRWV Capital Intensity (Times) CRWV Capital Intensity \\- CoreWeave's margin profile is currently depressed by a structural OpEx–revenue lag. The company begi"
  },
  {
    "figure_id": "F070",
    "report_id": "R003",
    "label": "EXHIBIT 26",
    "context": "EXHIBIT 26: CRWV Adj. Operating Income (\\$M) CRWV Adj. Operating Income Adj. Operating Income — Adj. Operating Income Margin EXHIBIT 27: CRWV Adj. EBITDA (\\$M) CRWV Adj. EBITDA"
  },
  {
    "figure_id": "F071",
    "report_id": "R003",
    "label": "EXHIBIT 27",
    "context": "EXHIBIT 27: CRWV Adj. EBITDA (\\$M) CRWV Adj. EBITDA EXHIBIT 28: CRWV Diluted EPS (\\$) CRWV Diluted EPS ## I. REQUIRED DISCLOSURES"
  },
  {
    "figure_id": "F072",
    "report_id": "R003",
    "label": "EXHIBIT 27",
    "context": "EXHIBIT 27: CRWV Adj. EBITDA (\\$M) CRWV Adj. EBITDA EXHIBIT 28: CRWV Diluted EPS (\\$) CRWV Diluted EPS ## I. REQUIRED DISCLOSURES Bernstein is part of a joint venture between SG (SG) and AllianceBernstein, L.P. (AB). Unless spec"
  },
  {
    "figure_id": "F073",
    "report_id": "R004",
    "label": "Exhibit 1",
    "context": "Exhibit 2: At 11-15% commercial WACC, the 75th percentile of the oil cost curve would move from \\$66/bbl to \\$57/bbl"
  },
  {
    "figure_id": "F074",
    "report_id": "R004",
    "label": "Exhibit 1",
    "context": "Exhibit 2: At 11-15% commercial WACC, the 75th percentile of the oil cost curve would move from \\$66/bbl to \\$57/bbl"
  },
  {
    "figure_id": "F075",
    "report_id": "R004",
    "label": "Exhibit 2",
    "context": "Exhibit 4: Drivers of the improvement of oil field economics through AI"
  },
  {
    "figure_id": "F076",
    "report_id": "R004",
    "label": "Exhibit 2",
    "context": "Exhibit 4: Drivers of the improvement of oil field economics through AI ## AI levers on a producing offshore field Productivity and cost levers — sized for a typical deepwater hub. Sourced from operator and vendor calls."
  },
  {
    "figure_id": "F077",
    "report_id": "R004",
    "label": "Exhibit 6",
    "context": "Exhibit 6: We estimate AI and advanced computing could compress the full greenfield deepwater cycle — from licence award to first oil — from c.12 years to c.7 years, a savings of c.4 years (-c.38%). Block durations match the indi"
  },
  {
    "figure_id": "F078",
    "report_id": "R004",
    "label": "Exhibit 7",
    "context": "Exhibit 8: Around 80% of the potential calendar savings sits in three phases on the critical path: interpretation, well design and seismic processing. Total cycle saving: 28 months (51 → 23 mo, -56%). Marginal contribution per phas"
  },
  {
    "figure_id": "F079",
    "report_id": "R004",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Around 80% of the potential calendar savings sits in three phases on the critical path: interpretation, well design and seismic processing. Total cycle saving: 28 months (51 → 23 mo, -56%). Marginal contribution per phas"
  },
  {
    "figure_id": "F080",
    "report_id": "R004",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Appraisal: potential \\~40-50% cycle compression, almost entirely from the subsurface workflow ## 3) Pre-FID/Concept: FEED — c.40-50% time compression driven by three roughly equal levers Average FEED shortens from c.12"
  },
  {
    "figure_id": "F081",
    "report_id": "R004",
    "label": "Exhibit 10",
    "context": "Exhibit 10: The phase compresses by only c.10% with AI / digital tools — from c.4.5 years to c.4 years on a typical deepwater project — making it the least AI-impacted block in the lifecycle Development / Construction phase — stairc"
  },
  {
    "figure_id": "F082",
    "report_id": "R004",
    "label": "Exhibit 10",
    "context": "Exhibit 10: The phase compresses by only c.10% with AI / digital tools — from c.4.5 years to c.4 years on a typical deepwater project — making it the least AI-impacted block in the lifecycle Development / Construction phase — stairc"
  },
  {
    "figure_id": "F083",
    "report_id": "R004",
    "label": "Exhibit 11",
    "context": "Exhibit 13: We estimate AI could lift the IRR of an average greenfield field by 3.5pp, with capex and time to market driving the majority IRR decomposition of our AI scenario on an average greenfield field"
  },
  {
    "figure_id": "F084",
    "report_id": "R004",
    "label": "Exhibit 11",
    "context": "Exhibit 13: We estimate AI could lift the IRR of an average greenfield field by 3.5pp, with capex and time to market driving the majority IRR decomposition of our AI scenario on an average greenfield field This report draws on com"
  },
  {
    "figure_id": "F085",
    "report_id": "R004",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Capex and OCF profile of an average greenfield field, base vs AI scenario (\\$bn) Exhibit 13: We estimate AI could lift the IRR of an average greenfield field by 3.5pp, with capex and time to market driving the majority"
  },
  {
    "figure_id": "F086",
    "report_id": "R006",
    "label": "Exhibit 1",
    "context": "Exhibit 1: We now forecast DRAM WFE to average \\$58bn during 2026-28 and average bit output of 31% Exhibit 2: As we exit 2026/27/28 at 2,251/2,661/3,081kwpm Exhibit 3: Wafer adds will be driven by all 4 major players"
  },
  {
    "figure_id": "F087",
    "report_id": "R006",
    "label": "Exhibit 1",
    "context": "Exhibit 1: We now forecast DRAM WFE to average \\$58bn during 2026-28 and average bit output of 31% Exhibit 2: As we exit 2026/27/28 at 2,251/2,661/3,081kwpm Exhibit 3: Wafer adds will be driven by all 4 major players Exhibit"
  },
  {
    "figure_id": "F088",
    "report_id": "R006",
    "label": "Exhibit 2",
    "context": "Exhibit 2: As we exit 2026/27/28 at 2,251/2,661/3,081kwpm Exhibit 3: Wafer adds will be driven by all 4 major players Exhibit 5: HBM's trade ratio is driving approx. 27% of 2028 bits to be \"lost bits\" Exhibit 4: Non-HBM wafer"
  },
  {
    "figure_id": "F089",
    "report_id": "R006",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Wafer adds will be driven by all 4 major players Exhibit 5: HBM's trade ratio is driving approx. 27% of 2028 bits to be \"lost bits\" Exhibit 4: Non-HBM wafer adds will surpass HBM wafer adds from 2027 Exhibit 6: As"
  },
  {
    "figure_id": "F090",
    "report_id": "R006",
    "label": "Exhibit 3",
    "context": "Exhibit 7: Our NAND WFE forecast doesn't materially change, but we continue to see capacity adds as a contributor to bit supply in 2027/28"
  },
  {
    "figure_id": "F091",
    "report_id": "R006",
    "label": "Exhibit 4",
    "context": "Exhibit 8: We model eSSD bits to grow at a 3-year CAGR of 66% from 2025-28"
  },
  {
    "figure_id": "F092",
    "report_id": "R006",
    "label": "Exhibit 6",
    "context": "Exhibit 9: We model eSSD mix to increase from 29% in 2025 to 67% in 2028"
  },
  {
    "figure_id": "F093",
    "report_id": "R006",
    "label": "Exhibit 7",
    "context": "Exhibit 10: Our 2026-28 NAND WFE forecast translates to bit supply of 29% during 2026-28"
  },
  {
    "figure_id": "F094",
    "report_id": "R006",
    "label": "Exhibit 8",
    "context": "Exhibit 11: We expect non-China players to be a meaningful contributor to NAND Wafer adds in 2027-28"
  },
  {
    "figure_id": "F095",
    "report_id": "R006",
    "label": "Exhibit 9",
    "context": "Exhibit 12: We don't model NAND wafer starts to surpass prior peak of 1,762kwpm (Q3 2022) in our forecast horizon"
  },
  {
    "figure_id": "F096",
    "report_id": "R006",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Our 2026-28 NAND WFE forecast translates to bit supply of 29% during 2026-28 Exhibit 11: We expect non-China players to be a meaningful contributor to NAND Wafer adds in 2027-28 Exhibit 12: We don't model NAND wafer"
  },
  {
    "figure_id": "F097",
    "report_id": "R006",
    "label": "Exhibit 11",
    "context": "Exhibit 11: We expect non-China players to be a meaningful contributor to NAND Wafer adds in 2027-28 Exhibit 12: We don't model NAND wafer starts to surpass prior peak of 1,762kwpm (Q3 2022) in our forecast horizon ## Valuation"
  },
  {
    "figure_id": "F098",
    "report_id": "R007",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: Tokenized RWA - Market Cap (\\$Bn) Tokenized RWA - Market Cap (\\$Bn) Private credit includes Figure tokenized credit EXHIBIT 2: Tokenized RWA market cap split by asset class Private credit includes Figure tokenized cr"
  },
  {
    "figure_id": "F099",
    "report_id": "R007",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 3: Tokenized RWA split by blockchain network Tokenized RWA - Blockchain network split (%)"
  },
  {
    "figure_id": "F100",
    "report_id": "R007",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Tokenized RWA split by blockchain network Tokenized RWA - Blockchain network split (%) EXHIBIT 4: Top RWA tokenization platforms"
  },
  {
    "figure_id": "F101",
    "report_id": "R007",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: Top RWA tokenization platforms EXHIBIT 5: Tokenized real world asset holders RWA Asset Holders (in '000) EXHIBIT 6: FIGR - Consumer Loan Volumes (\\$Bn) FIGR - Consumer Loan Volumes (\\$Bn) EXHIBIT 7: Tokenized Equitie"
  },
  {
    "figure_id": "F102",
    "report_id": "R007",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: Tokenized real world asset holders RWA Asset Holders (in '000) EXHIBIT 6: FIGR - Consumer Loan Volumes (\\$Bn) FIGR - Consumer Loan Volumes (\\$Bn) EXHIBIT 7: Tokenized Equities - Monthly Transfer Volumes Tokenized Equ"
  },
  {
    "figure_id": "F103",
    "report_id": "R007",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: FIGR - Consumer Loan Volumes (\\$Bn) FIGR - Consumer Loan Volumes (\\$Bn) EXHIBIT 7: Tokenized Equities - Monthly Transfer Volumes Tokenized Equity - Transfer Volumes (\\$Bn) June'26 numbers based on runrate as of June"
  },
  {
    "figure_id": "F104",
    "report_id": "R008",
    "label": "Exhibit 3",
    "context": "EXHIBIT 1: We forecast 2-2.5x increase in HBM prices YoY next year so that the profitability of HBM & conventional DRAM can narrow. EXHIBIT 2: We expect the price increase to take place at all generations of HBM. EXHIBIT 3: We"
  },
  {
    "figure_id": "F105",
    "report_id": "R008",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: We forecast 2-2.5x increase in HBM prices YoY next year so that the profitability of HBM & conventional DRAM can narrow. EXHIBIT 2: We expect the price increase to take place at all generations of HBM. EXHIBIT 3: We"
  },
  {
    "figure_id": "F106",
    "report_id": "R008",
    "label": "EXHIBIT 2",
    "context": "Exhibit 1-Exhibit 2). HBM profitability hence will remain below that of conventional DRAM next year, but the gap should be much smaller than this year."
  },
  {
    "figure_id": "F107",
    "report_id": "R008",
    "label": "Exhibit 4",
    "context": "EXHIBIT 6: Conventional DRAM now generates considerably more revenue per wafer capacity than HBM, and we project an HBM price hike next year to narrow that gap."
  },
  {
    "figure_id": "F108",
    "report_id": "R008",
    "label": "Exhibit 8",
    "context": "EXHIBIT 6: Conventional DRAM now generates considerably more revenue per wafer capacity than HBM, and we project an HBM price hike next year to narrow that gap. EXHIBIT 7: We believe the margin gap between HBM and conventional DR"
  },
  {
    "figure_id": "F109",
    "report_id": "R008",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 7: We believe the margin gap between HBM and conventional DRAM to narrow next year. S. Chungcheong Export N. Chungcheong Export + Icheon Export Other Provinces"
  },
  {
    "figure_id": "F110",
    "report_id": "R008",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 8: Value per weight remained largely in the same range though the export value per weight for Samsung rose notably & suggested HBM4 shipment in May. Korea Multichip Memory Export Value per Weight to TW+MY"
  },
  {
    "figure_id": "F111",
    "report_id": "R008",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 10: With the expected HBM price increase, we forecast HBM's revenue mix in DRAM to rebound next year. HBM Contribution to DRAM Revenue"
  },
  {
    "figure_id": "F112",
    "report_id": "R008",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 10: With the expected HBM price increase, we forecast HBM's revenue mix in DRAM to rebound next year. HBM Contribution to DRAM Revenue ## DRAM stocks will benefit from a rapid upward earnings revision in the near term."
  },
  {
    "figure_id": "F113",
    "report_id": "R008",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 10: With the expected HBM price increase, we forecast HBM's revenue mix in DRAM to rebound next year. HBM Contribution to DRAM Revenue ## DRAM stocks will benefit from a rapid upward earnings revision in the near term. con"
  },
  {
    "figure_id": "F114",
    "report_id": "R008",
    "label": "EXHIBIT 13",
    "context": "EXHIBIT 13: Our Micron FY27 EPS forecast is 38% above consensus too. EXHIBIT 14: We expect EPS to grow exponentially going forward. EXHIBIT 15: We model earnings to reach peak in 2HCY27... EXHIBIT 16: ... and then gradually decl"
  },
  {
    "figure_id": "F115",
    "report_id": "R008",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: We expect EPS to grow exponentially going forward. EXHIBIT 15: We model earnings to reach peak in 2HCY27... EXHIBIT 16: ... and then gradually decline in CY28 as prices normalize. EXHIBIT 17: We forecast DRAM price"
  },
  {
    "figure_id": "F116",
    "report_id": "R008",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 18: ROE will rise to unprecedented levels."
  },
  {
    "figure_id": "F117",
    "report_id": "R008",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 18: ROE will rise to unprecedented levels. EXHIBIT 19: Samsung BVPS can grow by nearly 2x in both 2026 and 2027."
  },
  {
    "figure_id": "F118",
    "report_id": "R008",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 20: SK hynix can see even steeper accretion in BVPS."
  },
  {
    "figure_id": "F119",
    "report_id": "R008",
    "label": "EXHIBIT 18",
    "context": "EXHIBIT 18: ROE will rise to unprecedented levels. EXHIBIT 19: Samsung BVPS can grow by nearly 2x in both 2026 and 2027. EXHIBIT 20: SK hynix can see even steeper accretion in BVPS. EXHIBIT 21: We see 4x increase in Micron BVP"
  },
  {
    "figure_id": "F120",
    "report_id": "R008",
    "label": "EXHIBIT 19",
    "context": "EXHIBIT 19: Samsung BVPS can grow by nearly 2x in both 2026 and 2027. EXHIBIT 20: SK hynix can see even steeper accretion in BVPS. EXHIBIT 21: We see 4x increase in Micron BVPS from now to end of FY27. EXHIBIT 22: Cash will ac"
  },
  {
    "figure_id": "F121",
    "report_id": "R008",
    "label": "EXHIBIT 20",
    "context": "EXHIBIT 20: SK hynix can see even steeper accretion in BVPS. EXHIBIT 21: We see 4x increase in Micron BVPS from now to end of FY27. EXHIBIT 22: Cash will accumulate at unprecedented pace as well. EXHIBIT 23: We forecast cash t"
  },
  {
    "figure_id": "F122",
    "report_id": "R008",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 21: We see 4x increase in Micron BVPS from now to end of FY27. EXHIBIT 22: Cash will accumulate at unprecedented pace as well. EXHIBIT 23: We forecast cash to reach 70-80% of book value... EXHIBIT 24: ... unless compan"
  },
  {
    "figure_id": "F123",
    "report_id": "R008",
    "label": "EXHIBIT 22",
    "context": "EXHIBIT 22: Cash will accumulate at unprecedented pace as well. EXHIBIT 23: We forecast cash to reach 70-80% of book value... EXHIBIT 24: ... unless company meaningful increase payout or use it for M&A. EXHIBIT 25: We now targ"
  },
  {
    "figure_id": "F124",
    "report_id": "R008",
    "label": "EXHIBIT 23",
    "context": "EXHIBIT 23: We forecast cash to reach 70-80% of book value... EXHIBIT 24: ... unless company meaningful increase payout or use it for M&A. EXHIBIT 25: We now target 6.2x 1 year P/E to value Samsung. EXHIBIT 26: We also use 6.2"
  },
  {
    "figure_id": "F125",
    "report_id": "R008",
    "label": "EXHIBIT 24",
    "context": "EXHIBIT 24: ... unless company meaningful increase payout or use it for M&A. EXHIBIT 25: We now target 6.2x 1 year P/E to value Samsung. EXHIBIT 26: We also use 6.2x P/E for hynix. EXHIBIT 27: Micron target P/E is 7.7x, still"
  },
  {
    "figure_id": "F126",
    "report_id": "R008",
    "label": "EXHIBIT 25",
    "context": "EXHIBIT 25: We now target 6.2x 1 year P/E to value Samsung. EXHIBIT 26: We also use 6.2x P/E for hynix. EXHIBIT 27: Micron target P/E is 7.7x, still close to past trough levels. ## APPENDIX - FINANCIAL FORECASTS"
  },
  {
    "figure_id": "F127",
    "report_id": "R008",
    "label": "EXHIBIT 26",
    "context": "EXHIBIT 26: We also use 6.2x P/E for hynix. EXHIBIT 27: Micron target P/E is 7.7x, still close to past trough levels. ## APPENDIX - FINANCIAL FORECASTS ## EXHIBIT 28: Samsung Income Statement Figures in KRW B Unless Otherwise St"
  },
  {
    "figure_id": "F128",
    "report_id": "R009",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Too lumpy, too little: India's AI strategy so far has been that of trying to do a lot from less resources Allocation and Actual Spend in India's AI mission (INR bn) ## DEFOCUSED, THINLY SPREAD Beyond funding, the broad"
  },
  {
    "figure_id": "F129",
    "report_id": "R009",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: Too defocused, thinly spread: Even with lesser and lumpy allocations, the focus is all over the place, creating no single area with meaningful advantage for India How Government's INR 104 billion AI allocation is split"
  },
  {
    "figure_id": "F130",
    "report_id": "R010",
    "label": "Figure 3",
    "context": "Figure 3: Factor exposure of electrical equipment (TSE 33 sector): As of June 12"
  },
  {
    "figure_id": "F131",
    "report_id": "R010",
    "label": "Figure 10",
    "context": "Figure 3: Factor exposure of electrical equipment (TSE 33 sector): As of June 12 Figure 4: Factor exposure of two MLCC-related companies (Murata Manufacturing and Taiyo Yuden): As of June 12"
  },
  {
    "figure_id": "F132",
    "report_id": "R010",
    "label": "Figure 2",
    "context": "Figure 4: Factor exposure of two MLCC-related companies (Murata Manufacturing and Taiyo Yuden): As of June 12 Figure 5: Estimated net position and profit margin momentum of Cash Equity Trend-Followers for two MLCC-related compan"
  },
  {
    "figure_id": "F133",
    "report_id": "R010",
    "label": "Figure 3",
    "context": "Figure 6: Estimated net position and profit margin momentum of Cash Equity Trend-Followers for two MLCC-related companies: Taiyo Yuden"
  },
  {
    "figure_id": "F134",
    "report_id": "R010",
    "label": "Figure 4",
    "context": "Figure 6: Estimated net position and profit margin momentum of Cash Equity Trend-Followers for two MLCC-related companies: Taiyo Yuden Figure 7: Regional Allocation of global active investment trusts (DM+EM) (mainland China stoc"
  },
  {
    "figure_id": "F135",
    "report_id": "R010",
    "label": "Figure 5",
    "context": "Figure 7: Regional Allocation of global active investment trusts (DM+EM) (mainland China stocks + Hong Kong stocks) and US import ratios from China Figure 8: Relative differences in regional allocation of global active investmen"
  },
  {
    "figure_id": "F136",
    "report_id": "R010",
    "label": "Figure 6",
    "context": "Figure 9: Regional allocation of global active investment trusts (DM+EM): As of end-April"
  },
  {
    "figure_id": "F137",
    "report_id": "R010",
    "label": "Figure 7",
    "context": "Figure 9: Regional allocation of global active investment trusts (DM+EM): As of end-April Figure 10: Regional allocation of global active investment trusts (DM+EM) – Trends for Japan, South Korea, and Taiwan: As of end-April"
  },
  {
    "figure_id": "F138",
    "report_id": "R010",
    "label": "Figure 8",
    "context": "Figure 9: Regional allocation of global active investment trusts (DM+EM): As of end-April Figure 10: Regional allocation of global active investment trusts (DM+EM) – Trends for Japan, South Korea, and Taiwan: As of end-April F"
  },
  {
    "figure_id": "F139",
    "report_id": "R010",
    "label": "Figure 9",
    "context": "Figure 12: Changes in sector weightings of Japanese stocks in global active investment trusts (DM) (Active vs. Passive): As of end-April"
  },
  {
    "figure_id": "F140",
    "report_id": "R010",
    "label": "Figure 10",
    "context": "Figure 12: Changes in sector weightings of Japanese stocks in global active investment trusts (DM) (Active vs. Passive): As of end-April"
  },
  {
    "figure_id": "F141",
    "report_id": "R010",
    "label": "Figure 11",
    "context": "Figure 11: Sector weightings of Japanese stocks in global active investment trusts (DM) (Active vs. Passive): As of end-April Figure 12: Changes in sector weightings of Japanese stocks in global active investment trusts (DM) (Act"
  },
  {
    "figure_id": "F142",
    "report_id": "R011",
    "label": "Exhibit 2",
    "context": "Exhibit 2: AC domestic ex-factory shipment growth weakened sequentially in May Domestic ex-factory shipment vol. (10,000 units) Exhibit 3: AC domestic shipment moderated in May (-15% yoy in May vs -7% yoy in Apr)... AC domestic e"
  },
  {
    "figure_id": "F143",
    "report_id": "R011",
    "label": "Exhibit 3",
    "context": "Exhibit 7: Domestic refrigerator ex-factory shipments improved to -4% yoy growth in Apr Refrigerator domestic ex-factory shipment vol. (LHS, 10,000 units); yoy growth (RHS, %)"
  },
  {
    "figure_id": "F144",
    "report_id": "R011",
    "label": "Exhibit 3",
    "context": "Exhibit 7: Domestic refrigerator ex-factory shipments improved to -4% yoy growth in Apr Refrigerator domestic ex-factory shipment vol. (LHS, 10,000 units); yoy growth (RHS, %) Exhibit 4: ...with Midea/Gree/Haier/Hisense's domestic"
  },
  {
    "figure_id": "F145",
    "report_id": "R011",
    "label": "Exhibit 7",
    "context": "Exhibit 5: Washing machine domestic shipment growth stayed at -6% yoy in Apr Exhibit 6: Haier/Midea grew above industry at -1%/-1% yoy in Apr Washing machine (WM) domestic ex-factory shipment yoy growth by company"
  },
  {
    "figure_id": "F146",
    "report_id": "R011",
    "label": "Exhibit 7",
    "context": "Exhibit 5: Washing machine domestic shipment growth stayed at -6% yoy in Apr Exhibit 6: Haier/Midea grew above industry at -1%/-1% yoy in Apr Washing machine (WM) domestic ex-factory shipment yoy growth by company Exhibit 8: Mi"
  },
  {
    "figure_id": "F147",
    "report_id": "R011",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Washing machine domestic shipment growth stayed at -6% yoy in Apr Exhibit 6: Haier/Midea grew above industry at -1%/-1% yoy in Apr Washing machine (WM) domestic ex-factory shipment yoy growth by company Exhibit 8: Mi"
  },
  {
    "figure_id": "F148",
    "report_id": "R011",
    "label": "Exhibit 8",
    "context": "Exhibit 9: Domestic VRF ex-factory sales improved to -6% yoy in Apr VRF domestic sales (LHS, RMB mn); yoy growth (RHS, %)"
  },
  {
    "figure_id": "F149",
    "report_id": "R011",
    "label": "Exhibit 9",
    "context": "Exhibit 11: China white goods exports improved in Apr, with better EU/US consumer sentiment in May/Jun"
  },
  {
    "figure_id": "F150",
    "report_id": "R011",
    "label": "Exhibit 9",
    "context": "Exhibit 11: China white goods exports improved in Apr, with better EU/US consumer sentiment in May/Jun Exhibit 12: US pending home sales, a leading indicator of existing home sales, showed improvements in May"
  },
  {
    "figure_id": "F151",
    "report_id": "R011",
    "label": "Exhibit 10",
    "context": "Exhibit 12: US pending home sales, a leading indicator of existing home sales, showed improvements in May Exhibit 13: AC ex-factory export shipments decreased by 4% yoy in May, up from -12% yoy in Apr AC export ex-factory shipment"
  },
  {
    "figure_id": "F152",
    "report_id": "R011",
    "label": "Exhibit 11",
    "context": "Exhibit 14: Washing machine export growth was +14% yoy in Apr, vs. +7% yoy in Mar"
  },
  {
    "figure_id": "F153",
    "report_id": "R011",
    "label": "Exhibit 12",
    "context": "Exhibit 14: Washing machine export growth was +14% yoy in Apr, vs. +7% yoy in Mar Exhibit 15: Refrigerator export shipment growth improved to +13% yoy in Apr, vs. -3% yoy in Mar Refrigerator export ex-factory shipment vol. (LHS, 1"
  },
  {
    "figure_id": "F154",
    "report_id": "R011",
    "label": "Exhibit 13",
    "context": "Exhibit 15: Refrigerator export shipment growth improved to +13% yoy in Apr, vs. -3% yoy in Mar Refrigerator export ex-factory shipment vol. (LHS, 10,000 units); yoy growth (RHS, %) Exhibit 17: Shipping rates increased in the past"
  },
  {
    "figure_id": "F155",
    "report_id": "R011",
    "label": "Exhibit 14",
    "context": "Exhibit 17: Shipping rates increased in the past month... Weekly CCFI ## Exhibit 16: VRF export ex-factory sales grew +1% yoy in Apr"
  },
  {
    "figure_id": "F156",
    "report_id": "R011",
    "label": "Exhibit 15",
    "context": "Exhibit 16: VRF export ex-factory sales grew +1% yoy in Apr VRF export sales (LHS, RMB mn); yoy growth (RHS, %)"
  },
  {
    "figure_id": "F157",
    "report_id": "R011",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Shipping rates increased in the past month... Weekly CCFI ## Exhibit 16: VRF export ex-factory sales grew +1% yoy in Apr VRF export sales (LHS, RMB mn); yoy growth (RHS, %) Exhibit 18: ... and yoy growth increased as"
  },
  {
    "figure_id": "F158",
    "report_id": "R011",
    "label": "Exhibit 16",
    "context": "Exhibit 16: VRF export ex-factory sales grew +1% yoy in Apr VRF export sales (LHS, RMB mn); yoy growth (RHS, %) Exhibit 18: ... and yoy growth increased as of mid-June Weekly CCFI yoy growth % ## Retail sales remained weak on a"
  },
  {
    "figure_id": "F159",
    "report_id": "R011",
    "label": "Exhibit 22",
    "context": "Exhibit 24: We note select brands like Midea and Xiaomi lowered prices during 618 vs 2025 Singles' Day, but higher than last 618"
  },
  {
    "figure_id": "F160",
    "report_id": "R011",
    "label": "Exhibit 22",
    "context": "Exhibit 24: We note select brands like Midea and Xiaomi lowered prices during 618 vs 2025 Singles' Day, but higher than last 618 Pricing of entry-level AC"
  },
  {
    "figure_id": "F161",
    "report_id": "R011",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Midea, Xiaomi and Haier showed mom market share increase in Apr, while Gree lost share mom Online market share for AC on Taobao, Tmall and JD (%) Exhibit 24: We note select brands like Midea and Xiaomi lowered prices d"
  },
  {
    "figure_id": "F162",
    "report_id": "R011",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Midea, Xiaomi and Haier showed mom market share increase in Apr, while Gree lost share mom Online market share for AC on Taobao, Tmall and JD (%) Exhibit 24: We note select brands like Midea and Xiaomi lowered prices d"
  },
  {
    "figure_id": "F163",
    "report_id": "R011",
    "label": "Exhibit 25",
    "context": "Exhibit 27: Growth of RVC moderated mom on Amazon US in May"
  },
  {
    "figure_id": "F164",
    "report_id": "R011",
    "label": "Exhibit 25",
    "context": "Exhibit 27: Growth of RVC moderated mom on Amazon US in May Sales/Volume/ASP yoy growth by category & Market share/Sales/Volume/ASP yoy growth by company on EC channel (Amazon US) Monthly sales data showed volatility so the absolute"
  },
  {
    "figure_id": "F165",
    "report_id": "R011",
    "label": "Exhibit 28",
    "context": "Exhibit 28: Robotic lawn mower demand remained solid with DD% growth and Ninebot's continued market share gains with $100\\%+$ growth in May Download growth of leading robotic lawn mower apps (yoy, %) Exhibit 29: Residential prop"
  },
  {
    "figure_id": "F166",
    "report_id": "R011",
    "label": "Exhibit 28",
    "context": "Exhibit 28: Robotic lawn mower demand remained solid with DD% growth and Ninebot's continued market share gains with $100\\%+$ growth in May Download growth of leading robotic lawn mower apps (yoy, %) Exhibit 29: Residential prop"
  },
  {
    "figure_id": "F167",
    "report_id": "R011",
    "label": "Exhibit 29",
    "context": "Exhibit 29: Residential property completions decline narrowed slightly to -20% in May (vs. -22% in Apr), 45% below pre-Covid levels Residential property completions (LHS, mn sqm); yoy growth (RHS, %); growth vs. 2019 (RHS, %) Exhi"
  },
  {
    "figure_id": "F168",
    "report_id": "R011",
    "label": "Exhibit 29",
    "context": "Exhibit 29: Residential property completions decline narrowed slightly to -20% in May (vs. -22% in Apr), 45% below pre-Covid levels Residential property completions (LHS, mn sqm); yoy growth (RHS, %); growth vs. 2019 (RHS, %) Exhi"
  },
  {
    "figure_id": "F169",
    "report_id": "R011",
    "label": "Exhibit 31",
    "context": "Exhibit 32: SHFE copper price increased mildly in the past month, +2%/+34% mom/yoy as of mid-Jun SHFE copper price (LHS, RMB/ton); yoy growth (RHS, %) Exhibit 33: SHFE aluminum price grew by -2%/+16% mom/yoy as of mid-Jun"
  },
  {
    "figure_id": "F170",
    "report_id": "R011",
    "label": "Exhibit 31",
    "context": "Exhibit 32: SHFE copper price increased mildly in the past month, +2%/+34% mom/yoy as of mid-Jun SHFE copper price (LHS, RMB/ton); yoy growth (RHS, %) Exhibit 33: SHFE aluminum price grew by -2%/+16% mom/yoy as of mid-Jun SHFE alu"
  },
  {
    "figure_id": "F171",
    "report_id": "R011",
    "label": "Exhibit 32",
    "context": "Exhibit 34: Our covered appliances companies' share prices changed by -25% to +14% in the past month, yielding YTD returns of -38% to +12% Prices as of May 19, 2026."
  },
  {
    "figure_id": "F172",
    "report_id": "R011",
    "label": "Exhibit 34",
    "context": "Exhibit 34: Our covered appliances companies' share prices changed by -25% to +14% in the past month, yielding YTD returns of -38% to +12% Prices as of May 19, 2026. Exhibit 35: Valuations of most covered appliances companies show"
  },
  {
    "figure_id": "F173",
    "report_id": "R011",
    "label": "Exhibit 34",
    "context": "Exhibit 34: Our covered appliances companies' share prices changed by -25% to +14% in the past month, yielding YTD returns of -38% to +12% Prices as of May 19, 2026. Exhibit 35: Valuations of most covered appliances companies show"
  },
  {
    "figure_id": "F174",
    "report_id": "R012",
    "label": "Exhibit 1",
    "context": "Exhibit 1: A-share tech/small-mid caps led year-on-year earnings growth in 1Q26 Exhibit 2: Better earnings revision trend in A-shares/IT compared to MSCI China/Internet Exhibit 3: We now expect 8%/12% earnings growth for MSCI C"
  },
  {
    "figure_id": "F175",
    "report_id": "R012",
    "label": "Exhibit 1",
    "context": "Exhibit 4: Profit growth momentum for offshore tech could improve in 2H26 per GS and consensus expectations"
  },
  {
    "figure_id": "F176",
    "report_id": "R012",
    "label": "Exhibit 2",
    "context": "Exhibit 5: The 1H/2Q26 earnings season will kick off in August"
  },
  {
    "figure_id": "F177",
    "report_id": "R012",
    "label": "Exhibit 3",
    "context": "Exhibit 3: We now expect 8%/12% earnings growth for MSCI China in 2026/27E, below consensus estimates Exhibit 4: Profit growth momentum for offshore tech could improve in 2H26 per GS and consensus expectations Exhibit 5: The 1H"
  },
  {
    "figure_id": "F178",
    "report_id": "R012",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Profit growth momentum for offshore tech could improve in 2H26 per GS and consensus expectations Exhibit 5: The 1H/2Q26 earnings season will kick off in August ## 2) AI profits shifting towards hardware, both globa"
  },
  {
    "figure_id": "F179",
    "report_id": "R012",
    "label": "Exhibit 5",
    "context": "Exhibit 5: The 1H/2Q26 earnings season will kick off in August ## 2) AI profits shifting towards hardware, both globally and domestically Global AI profit pool: We laid out our global AI equity universe maps in March, covering"
  },
  {
    "figure_id": "F180",
    "report_id": "R012",
    "label": "Exhibit 9",
    "context": "Exhibit 7: China's share in global AI profit pool declined as other regions gained Exhibit 8: The margin profile for Chinese AI companies still lags global peers Exhibit 9: Both US and Chinese hyperscalers keep scaling up AI Ca"
  },
  {
    "figure_id": "F181",
    "report_id": "R012",
    "label": "Exhibit 9",
    "context": "Exhibit 10: The semiconductors layer grew the fastest in the Chinese AI universe in 1Q26"
  },
  {
    "figure_id": "F182",
    "report_id": "R012",
    "label": "Exhibit 8",
    "context": "Exhibit 11: Within China's AI supply chain, the internal profit pool has undergone a rebound toward hardware"
  },
  {
    "figure_id": "F183",
    "report_id": "R012",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Both US and Chinese hyperscalers keep scaling up AI Capex estimates by GS Internet team (US\\$bn) Exhibit 10: The semiconductors layer grew the fastest in the Chinese AI universe in 1Q26 Exhibit 11: Within China's AI"
  },
  {
    "figure_id": "F184",
    "report_id": "R012",
    "label": "Exhibit 10",
    "context": "Exhibit 10: The semiconductors layer grew the fastest in the Chinese AI universe in 1Q26 Exhibit 11: Within China's AI supply chain, the internal profit pool has undergone a rebound toward hardware ## 3) Recovering aggregate rev"
  },
  {
    "figure_id": "F185",
    "report_id": "R012",
    "label": "Exhibit 33",
    "context": "Exhibit 12: Aggregate revenue growth for the All China universe accelerated to 4% in 1Q26 vs. +1% in 2025 Exhibit 13: Mixed margin profile across the “involuted” sectors in 1Q26 ## 4) \"Going Global\" is still ongoing"
  },
  {
    "figure_id": "F186",
    "report_id": "R012",
    "label": "Exhibit 33",
    "context": "Exhibit 12: Aggregate revenue growth for the All China universe accelerated to 4% in 1Q26 vs. +1% in 2025 Exhibit 13: Mixed margin profile across the “involuted” sectors in 1Q26 ## 4) \"Going Global\" is still ongoing Sustained mo"
  },
  {
    "figure_id": "F187",
    "report_id": "R012",
    "label": "Exhibit 16",
    "context": "Exhibit 14: Foreign sales exposure of Chinese listed universe rose further to 18% despite tariff headwinds Exhibit 15: Autos and Pharma are the leaders in the globalization trend Exhibit 16: Most sectors enjoy better profitabili"
  },
  {
    "figure_id": "F188",
    "report_id": "R012",
    "label": "Exhibit 14",
    "context": "Exhibit 17: A slight FX loss was recorded in 2025 due to CNY appreciation"
  },
  {
    "figure_id": "F189",
    "report_id": "R012",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Autos and Pharma are the leaders in the globalization trend Exhibit 16: Most sectors enjoy better profitability in the overseas markets Exhibit 17: A slight FX loss was recorded in 2025 due to CNY appreciation ## 5"
  },
  {
    "figure_id": "F190",
    "report_id": "R012",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Most sectors enjoy better profitability in the overseas markets Exhibit 17: A slight FX loss was recorded in 2025 due to CNY appreciation ## 5) Record cash returns along with more R&D and acquisitions Record-high cas"
  },
  {
    "figure_id": "F191",
    "report_id": "R012",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Chinese corporates spent more cash on dividends, acquisitions, and R&D in 2025 (Rmb tn/%) All China listed universe - Use of Cash Exhibit 19: Dividend payout ratio edged up to 39% in 2025 Exhibit 20: Net buybacks rem"
  },
  {
    "figure_id": "F192",
    "report_id": "R012",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Chinese corporates spent more cash on dividends, acquisitions, and R&D in 2025 (Rmb tn/%) All China listed universe - Use of Cash Exhibit 19: Dividend payout ratio edged up to 39% in 2025 Exhibit 20: Net buybacks rem"
  },
  {
    "figure_id": "F193",
    "report_id": "R012",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Dividend payout ratio edged up to 39% in 2025 Exhibit 20: Net buybacks remain accretive to EPS despite lower absolute volumes Represents the net change in the carrying value of common and preferred stock 6) Key theme"
  },
  {
    "figure_id": "F194",
    "report_id": "R012",
    "label": "Exhibit 24",
    "context": "Exhibit 24: The refreshed portfolio exhibits strong performance and EPS revision trends Exhibit 25: The portfolio trades at 23x fP/E and 1.4x fPEG on an equal-weighted basis"
  },
  {
    "figure_id": "F195",
    "report_id": "R012",
    "label": "Exhibit 24",
    "context": "Exhibit 24: The refreshed portfolio exhibits strong performance and EPS revision trends Exhibit 25: The portfolio trades at 23x fP/E and 1.4x fPEG on an equal-weighted basis"
  },
  {
    "figure_id": "F196",
    "report_id": "R012",
    "label": "Exhibit 27",
    "context": "Exhibit 27: Top-line growth may pick up for MSCI China universe Exhibit 28: Exporters saw resilient top-line and earnings growth in 1Q26 Exhibit 29: All listed developers incurred around Rmb400bn of net losses in 2025"
  },
  {
    "figure_id": "F197",
    "report_id": "R012",
    "label": "Exhibit 27",
    "context": "Exhibit 30: Still around 60% of companies in property sector are loss-making"
  },
  {
    "figure_id": "F198",
    "report_id": "R012",
    "label": "Exhibit 28",
    "context": "Exhibit 30: Still around 60% of companies in property sector are loss-making Including both developers and property management companies; % in recent years are underestimated as some real estate companies stopped/delayed disclosin"
  },
  {
    "figure_id": "F199",
    "report_id": "R012",
    "label": "Exhibit 29",
    "context": "Exhibit 33: Consensus estimates Capex growth to moderate in most sectors while tech hardware notably upscales the Capex"
  },
  {
    "figure_id": "F200",
    "report_id": "R013",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 3: Interconnection queues are \\~4+ years for all regions, CAISO is the worst served region... Duration from IR to COD by region Most respondents indicated a preference for grid connected power, supplemented by onsite reso"
  },
  {
    "figure_id": "F201",
    "report_id": "R013",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 3: Interconnection queues are \\~4+ years for all regions, CAISO is the worst served region... Duration from IR to COD by region Most respondents indicated a preference for grid connected power, supplemented by onsite reso"
  },
  {
    "figure_id": "F202",
    "report_id": "R013",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 5: 45% of respondents preferred fossil fuel onsite back up; followed by Solar+ BESS, and Fuel Cells Which Type of Onsite Gen is preferred? Finally, We asked a long form question around how sustainability commitments shape"
  },
  {
    "figure_id": "F203",
    "report_id": "R013",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 6: Survey question: What role, if any, do decarbonization or sustainability commitments play in shaping your organization's preference around power supply sourcing and configuration?"
  },
  {
    "figure_id": "F204",
    "report_id": "R013",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: Survey question: What role, if any, do decarbonization or sustainability commitments play in shaping your organization's preference around power supply sourcing and configuration? Total 47 responses ## I. REQUIRED DISC"
  },
  {
    "figure_id": "F205",
    "report_id": "R016",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Under weak domestic demand conditions, better than anticipated feedstock supply and though inventory draw down, China's exports have ramped significantly in April thousand tonnes per month ## Valuation & Risks"
  },
  {
    "figure_id": "F206",
    "report_id": "R016",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Under weak domestic demand conditions, better than anticipated feedstock supply and though inventory draw down, China's exports have ramped significantly in April thousand tonnes per month ## Valuation & Risks ## BAS"
  },
  {
    "figure_id": "F207",
    "report_id": "R017",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Weekly stock performance"
  },
  {
    "figure_id": "F208",
    "report_id": "R017",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Weekly stock performance Exhibit 4: Monthly stock performance Exhibit 5: YTD stock performance"
  },
  {
    "figure_id": "F209",
    "report_id": "R017",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Weekly stock performance Exhibit 4: Monthly stock performance Exhibit 5: YTD stock performance ## Semis Week Ahead"
  },
  {
    "figure_id": "F210",
    "report_id": "R017",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Monthly stock performance Exhibit 5: YTD stock performance ## Semis Week Ahead Exhibit 6: June 22nd - June 26th, 2026 Monday, June 15th"
  },
  {
    "figure_id": "F211",
    "report_id": "R017",
    "label": "Exhibit 8",
    "context": "Exhibit 8: MS vs. Street Revenue and EPS Growth Exhibit 9: 2025-27e Revenue CAGR Exhibit 10: 2025-27e EPS CAGR ## Inventory"
  },
  {
    "figure_id": "F212",
    "report_id": "R017",
    "label": "Exhibit 9",
    "context": "Exhibit 9: 2025-27e Revenue CAGR Exhibit 10: 2025-27e EPS CAGR ## Inventory Exhibit 11: Semiconductor Company inventory is at 111 days, up 3 days q/q which is 4 days behind of the seasonal decrease of 1 days. DOI is 22 days abo"
  },
  {
    "figure_id": "F213",
    "report_id": "R017",
    "label": "Exhibit 11",
    "context": "Exhibit 12: Semi Customer DOI decreased 6 days sequentially to 52 days, below the seasonal decrease of 3 days. DOI is below the historical median and trailing 4 quarters increased from last quarter. Semi Customers (DOI)"
  },
  {
    "figure_id": "F214",
    "report_id": "R017",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Semi Customer DOI decreased 6 days sequentially to 52 days, below the seasonal decrease of 3 days. DOI is below the historical median and trailing 4 quarters increased from last quarter. Semi Customers (DOI) Exhibit 13"
  },
  {
    "figure_id": "F215",
    "report_id": "R017",
    "label": "Exhibit 12",
    "context": "Exhibit 14: Short Interest as % of Float"
  },
  {
    "figure_id": "F216",
    "report_id": "R019",
    "label": "Exhibit 4",
    "context": "EXHIBIT 2: Japan has the highest number of retail stores per capita among the developed nations Retail density per 1,000 inhabitants Year: 2025 EXHIBIT 3: Per-kilometer density makes the over-supply even starker-Japan's 2.61 stor"
  },
  {
    "figure_id": "F217",
    "report_id": "R019",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Per-kilometer density makes the over-supply even starker-Japan's 2.61 stores per sq km is 2x the next-closest peer Retail density per square kilometer Year: 2025 EXHIBIT 4: The math of the shakeout—the survivors inheri"
  },
  {
    "figure_id": "F218",
    "report_id": "R019",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: The math of the shakeout—the survivors inherit a larger slice of a stagnant pie ## THIS OVER-STORED MARKET IS NOW TOO EXPENSIVE TO REMAIN FRAGMENTED Global grocery retail has largely consolidated into a game of scale,"
  },
  {
    "figure_id": "F219",
    "report_id": "R019",
    "label": "Exhibit 6",
    "context": "EXHIBIT 5: The consolidation runway made quantitative—Japan has 40+ percentage points of concentration to catch up Top 5 grocery retailers' combined market share by country Year: 2025 Before Why fragmentation survived EXHIBIT 6:"
  },
  {
    "figure_id": "F220",
    "report_id": "R019",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: Three structural shields, all down simultaneously—the old fragmentation no longer has a defense After Why fragmentation is collapsing ## Pillar 1 Freshness culture Japan CR5\\~30% (1990s-2010s) Store-level processing fo"
  },
  {
    "figure_id": "F221",
    "report_id": "R019",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: Grocery is Japan's largest retail category by a wide margin 2024: Japan retail sales breakdown by industry"
  },
  {
    "figure_id": "F222",
    "report_id": "R019",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 9: Why \"over-stored\" becomes \"impossibly overstored\"—the denominator itself is shrinking"
  },
  {
    "figure_id": "F223",
    "report_id": "R019",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: A long tail waiting to be consolidated—the top two names hold barely one-fifth of the market FY2024 Japan grocery retail sales breakdown by company EXHIBIT 9: Why \"over-stored\" becomes \"impossibly overstored\"—the denom"
  },
  {
    "figure_id": "F224",
    "report_id": "R019",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: Why \"over-stored\" becomes \"impossibly overstored\"—the denominator itself is shrinking EXHIBIT 10: The inflation that finally matters—minimum wage has broken out above CPI, and the weak supermarkets cannot follow EXHI"
  },
  {
    "figure_id": "F225",
    "report_id": "R019",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: The inflation that finally matters—minimum wage has broken out above CPI, and the weak supermarkets cannot follow EXHIBIT 11: Rising labor costs are pushing supermarkets toward a breaking point – only scale can solve i"
  },
  {
    "figure_id": "F226",
    "report_id": "R019",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: The inflation that finally matters—minimum wage has broken out above CPI, and the weak supermarkets cannot follow EXHIBIT 11: Rising labor costs are pushing supermarkets toward a breaking point – only scale can solve i"
  },
  {
    "figure_id": "F227",
    "report_id": "R020",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Databricks core growth has accelerated over the last 5 quarters as a function of its product market fit with AI; Snowflake is also starting to show acceleration, albeit to a lesser extent \\*Databricks expects ARR to grow"
  }
]