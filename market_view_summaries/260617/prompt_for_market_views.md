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
    "title": "Citi：市场对美联储的“鹰派”定价已足够充分，真正的交易机会在于美元走弱时的战术性做空",
    "digest": "[wechat_article.md]\n# Citi：市场对美联储的“鹰派”定价已足够充分，真正的交易机会在于美元走弱时的战术性做空\n\n这份Citi研报的标题直接点明了核心判断：Fade EUR rallies if Warsh disappoints hawks。翻译过来，就是“如果新任美联储主席沃什未能满足鹰派预期，则逢高做空欧元”。这看似是一个具体的交易建议，但其背后隐藏着一个对当前宏观交易格局更根本的判断：市场已经提前消化了美联储转向鹰派的大部分预期，美元指数长达12个月的区间震荡格局，其突破的触发点并不在本次会议本身，而在于沃什在新闻发布会上的措辞，以及更重要的——地缘政治风险的缓和。\n\n这不再是一个简单的“加息与否”的二元博弈。报告揭示了一个更微妙的定价环境：美元的多头头寸已经大幅回撤，美元指数也已接近其短期公允价值。这意味着，即便美联储如市场所愿释放鹰派信号，其边际效用也在递减。真正的变量，是那些尚未被充分定价的“非对称风险”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 市场已为“鹰派声明”充分定价，沃什的“模糊”才是大概率事件\n\n报告明确指出，市场对于本次FOMC声明的鹰派调整已有充分预期：声明可能删除宽松倾向、核心PCE预测将被上调、点阵图中位数将指向2026年不再降息，甚至可能出现一两个加息点。这些变化，在Citi看来，不足以引发显著的外汇市场反应，因为它们已经“price in”了。\n\n真正的悬念在于沃什的新闻发布会。作为新任主席，他的沟通风格和具体措辞将成为市场关注的焦点。Citi的基准判断是，沃什将延续其“减少前瞻指引”的一贯立场，对当前市场定价（即年内加息18个基点，2027年3月首次加息完全定价）给出模棱两可的回答。这种“模糊”本身，就是对当前鹰派定价的一种温和打压。\n\n这个判断的核心含义在于：市场对“鹰派美联储”的叙\n\n[... middle omitted ...]\n\n加元融资的利差交易篮子，我们也会在群内进行更贴近实战的推演。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美联储新主席首秀，美元要变盘？\n\n美元要动了吗？\n\n**市场都在等Warsh的发言**\n\n本周美联储新主席Warsh首秀，大家都在猜他会说什么。研报观点很明确：市场已经提前消化了偏鹰的声明和点阵图，真正的变量是Warsh在发布会上的态度。\n\n**核心逻辑拆解：**\n\n1️⃣ **市场已经price in了**\n   - 声明可能去掉宽松偏向\n   - 核心PCE预测上修\n   - 点阵图显示2026年不降息\n   但这些已成共识，不会引发大波动\n\n2️⃣ **真正的看点**\n   Warsh会不会认可市场对加息的定价（目前预期+18bp，首次加息在2027年3月）？如果他说“加息和降息概率相当”，美元可能迎来突破性上涨。\n\n3️⃣ **美元短期怎么走**\n   - 多头仓位已经出清\n   - DXY接近公允价值\n   - 短期可能继续区间震荡，但中期看涨\n   关键阻力在1.1660-1.1680（欧元兑美元）\n\n4️⃣ **风险偏好回暖**\n   - 伊朗协议可能性上升\n   - 大型IPO成功\n   - 油价预期下调\n   这些都在支撑风险资产，利好套利交易（用欧元和加元融资）\n\n5️⃣ **需要关注的意\n\n[... middle omitted ...]\n\nuld see risk stabilize and rally. In FX, that should see carry trades resume, which we prefer funding with EUR and CAD.\n\n## Daniel Tobon AC\n\n+1-212-816-8340\n\ndaniel.tobon@citi.com\n\n## Brian Le\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R002",
    "title": "0002-02-Bernstein-Global Metals - Mining- Copper Taco or Boco Season Finale - U.S. policy is distorting copper price but",
    "digest": "[wechat_article.md]\nDeepSeek 生成 WeChat article 失败：Response ended prematurely\n\n请复制对应 prompt 文件手动生成。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n![研报原图 2](assets/source_image_02.jpg)\n\n![研报原图 3](assets/source_image_03.jpg)\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n铜的关税赌局，6月底见分晓\n\n铜价拐点将至？\n\n6月30日是白宫决定精炼铜关税的截止日\n\n铜价这波上涨，背后有四个推手：\n\n1️⃣ 矿山供应中断：Kamoa-Kakula和Grasberg等大矿接连出事，去年9月Freeport的Grasberg泥浆事故直接推铜价破$10,000/t。\n\n2️⃣ 金融投机加码：去年Q4期货净多头仓位飙升，铜价从$11,000一路冲到$13,000。\n\n3️⃣ 美国囤货潮：交易员押注2027年1月开征15%关税、2028年可能再加到30%，提前往美国仓库塞货。Comex库存去年涨了344kt，今年又加了152kt。\n\n4️⃣ 风险情绪回暖：美股创新高，LME与Comex价差扩大，铜价5月中旬摸到历史新高$14,109/t。\n\n关键变量是关税怎么走。某外资投行给出了两条路径：\n\n📌 基准情景（无关税）：宣布精炼铜不征关税。美国库存可能回流全球，铜价逐步回落到$11,000/t。\n\n📌 看涨情景（三种可能）：延期决定 → 铜继续涨；只征15%且无后续指引 → 更涨；15%+30%两步走 → 涨到新高。即便矿山不出事，铜价也可能重返历史高点。\n\n风险回报比很诱人：从西欧运铜到美国的成本约$400-754/t，但一旦征15%关税，价差可能超过$2,000/t。交易员有足够动力继续往Comex塞货。\n\n对铜价敏感度最高的公司是FCX和ANTO（beta约1.5x和1.4x），其次是AAL（1.1x），BHP相对温和（0.7x）。\n\n6月底这个节点，值得盯着。\n\n#学习笔记\n\n[source_mineru.md]\n## Global Metals & Mining\n\n# Global Metals & Mining: Copper Taco or Boco Season Finale - U.S. policy is distorting copper price but what can we do about it?\n\n![](images/516a99dd84a8998b6a548453143fc63a85b4dbc6009d544a4b1b489426ab7c20.jpg)\n\nBob Brackett, Ph.D.\n\n+1 917 344 8422\n\nbob.brackett@bernsteinsg.com\n\n![](images/c0ce408738fe8c3ae43c5a66a37df4e2711117d8e5e2e42ad811733010a818cd.jpg)\n\nAndrianto Guntoro, CFA\n\n+44 20 7676 6825\n\nandrianto.guntoro@bernsteinsg.com\n\nWe approach the deadline (June 30th) for the White House to decide on tariffs on refined copper. In previous notes, we expressed our TACO view of no tariffs. Trade deals were promised (Trump Directs Negotiations to Adjust Imports of Processed Critical Minerals) but haven't arrived from, say, Chile or Indonesia. In this note\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R003",
    "title": "Bernstein：AI从聊天走向智能体，CPU正在经历一场被低估的复兴",
    "digest": "[wechat_article.md]\n# Bernstein：AI从聊天走向智能体，CPU正在经历一场被低估的复兴\n\n过去两年，AI基础设施的投资逻辑几乎被GPU完全定义。市场默认的叙事是：算力即GPU算力，数据中心建设等于加速器集群的扩张。CPU被降格为“配角”，在AI服务器中的价值占比被不断压缩，甚至出现一台服务器搭配8颗GPU、只配1颗CPU的极端配置。\n\n但这份Bernstein研报提出了一个值得所有产业决策者重新审视的判断：**随着AI从1.0的聊天机器人范式，转向2.0的智能体范式，CPU正在经历一场结构性复兴。** 而市场对这一转变的定价，可能才刚刚开始。\n\nBernstein将2030年服务器CPU市场空间从此前的1370亿美元大幅上调至2230亿美元，并明确指出——这个数字在牛市情景下可能达到3300亿美元。驱动这一变化的，不是CPU自身的性能突破，而是AI工作负载的底层逻辑正在发生根本性转变。\n\n以下是我们从这份报告中提炼出的五个核心洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 智能体AI改变了CPU与GPU的配比逻辑，从1:8回归到1:1甚至更高\n\n理解这份报告的核心，首先要理解一个关键比率：CPU与GPU的配对比例。\n\n在传统的AI推理集群中，GPU是绝对的主角。以Google的TPU v6e和Meta的Grand Teton为例，GPU与CPU的配比曾达到8:1。这背后的逻辑是：推理任务本质上是“一次模型调用、一次返回结果”，CPU只需要承担数据加载和结果传递的轻量级工作，GPU负责最密集的矩阵运算。CPU被视作“税”，是必须支付但越少越好的开销。\n\n智能体AI彻底改变了这一假设。当一个AI系统不再只是回答问题，而是需要自主执行任务时，工作流变成了一个循环：用户请求触发检索，系统调用工具、进行中间推理、再次调用模型、\n\n[... middle omitted ...]\n\n入拆解。而这份Bernstein报告，只是打开了讨论的序幕。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nCPU复兴：AI从聊天走向干活\n\nCPU重回C位\n\nAI从聊天机器人进化到智能体时代，CPU不再是配角\n\n---\n\n最近读了一份投行研报，核心观点很直接：AI正在从1.0聊天机器人走向2.0智能体时代，CPU的地位将大幅提升。\n\n1/ 为什么CPU突然重要了？\n以前AI数据中心里，CPU和GPU的比例是1:4甚至1:8，GPU是绝对主角。但智能体AI需要自主调度任务、调用工具、管理内存——这些全是CPU的活。GPU负责密集计算，CPU负责让整个系统不卡顿。研报预测，这个比例会从1:8拉回到1:1甚至更高。\n\n2/ 市场规模直接翻倍\n研报把2030年服务器CPU总市场规模从之前预测的1370亿美元上调到2230亿美元，前提是3.5万亿美元的AI资本开支。如果AI投入达到4万亿，市场规模可能冲到3300亿。\n\n3/ 谁最受益？\nArm被看作结构性受益者——它的架构在功耗效率上有优势，而且正从只卖IP转向自己做CPU。AMD和Intel也会受益于更强的服务器需求，AMD产品目前领先，Intel在追赶。中国的海光信息会受益于国产替代，预计到2030年在中国x86服务器CPU市场份额超过35%。\n\n4/ 风险在哪？\n研\n\n[... middle omitted ...]\n\n442881261e08b4d3.jpg)\n\nMark Li\n\n+852 2123 2645\n\nmark.li@bernsteinsg.com\n\n![](images/af230e66cbbb16cf0271b8c30234566bdbdf831e7fb4fef1df63745d2c26cffa.jpg)\n\nJuho Hwang\n\n+852 2123 2632\n\njuho.hwan\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R004",
    "title": "Bernstein：市场低估的不是供给恢复的速度，而是库存重建的深度",
    "digest": "[wechat_article.md]\n# Bernstein：市场低估的不是供给恢复的速度，而是库存重建的深度\n\n这份报告的标题“Let the oil flow”看似直白，但真正有穿透力的判断藏在数字背后：全球石油市场在过去一段时间内累计消耗了约10亿桶库存。当所有人都在关注霍尔木兹海峡何时重新开放、供给何时恢复时，Bernstein的分析指向了一个更根本的问题——即便供给恢复正常，市场真正需要的不是“增量”，而是“补量”。重建这10亿桶库存，意味着未来两年内每天需要额外吸收约300万桶的供给。这个数字，才是理解油价底部和资产定价的关键。\n\n这份Bernstein研报发布于一个微妙的时点：布伦特原油年初至今均价约87美元/桶，市场正处于对地缘政治缓和的乐观预期与物理供需现实之间的拉锯中。报告没有给出廉价的看多或看空结论，而是构建了一个“短期偏紧、中期逐渐宽松、长期受边际成本锚定”的分阶段框架。对于亚太油气行业的决策者和投资者而言，这份报告提供的不是简单的方向判断，而是一套理解库存周期如何重塑竞争格局的分析工具。\n\n以下是我们从这份报告中提炼出的四个核心洞察，以及一个报告尚未完全回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 10亿桶库存消耗才是当前油价的真实支撑，而非地缘溢价\n\n市场普遍将油价维持在80-90美元/桶归因于地缘政治风险溢价。Bernstein的框架提供了一个更坚实的解释：物理库存的消耗。报告详细拆解了这约10亿桶的消耗构成——约3亿桶来自战略石油储备（SPR），约4.5亿桶来自中国库存，约1.4亿桶来自海上浮仓，其余来自商业库存。这不是一个抽象的数字，而是一个已经被市场吸收的供给冲击。\n\n这意味着什么？意味着即便霍尔木兹海峡明天就完全恢复通航，第一批恢复的油流并不会直接满足终端需求，而是会首先进入库存重建通道。Ber\n\n[... middle omitted ...]\n\n被充分讨论的假设？这些问题的答案，可能比报告本身更值得深思。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n霍尔木兹重启，油价怎么走？\n\n油价锚还在，别急\n\n霍尔木兹海峡恢复通航的备忘录是积极信号，但别指望油价立刻变天。\n\n1️⃣ 恢复需要时间，不是开关\n- 研报估算，全球已累计消耗约10亿桶库存（包括战略储备、中国库存、海上浮仓等）。\n- 即使协议落地，扫雷、保险、船只调度等至少需要6个月才能逐步恢复正常。\n- 所以短期库存仍会继续下降，油价有支撑。\n\n2️⃣ 供需平衡的时间表\n- 2026年Q1-Q3：市场持续供不应求。\n- 2026年Q4：供需接近平衡。\n- 2027年：可能出现约280万桶/日的过剩，但大部分会被补库需求吸收。\n\n3️⃣ 油价预期区间\n- 2026-2027年：布伦特预计在80-90美元/桶区间。\n- 2027年均价预测约78美元/桶（上半年偏强，下半年走弱）。\n- 长期锚定在75美元/桶附近。\n\n4️⃣ 关键变量\n- 阿联酋若增产至500万桶/日，会加剧过剩压力。\n- 各国可能因这次事件而主动增加库存，这也会吸收部分供应。\n\n总结：短期库存低位支撑油价，中期供给恢复+补库需求决定走势。目前市场已部分定价恢复预期，但实际节奏可能慢于预期。\n\n欢迎一起讨论，你们觉得补库周期会持续多久？🤔\n\n#\n\n[... middle omitted ...]\n\ntrait of Hormuz, but uncertainty remains high. Operational details are still unclear, including the timing of vessel returns, availability and pricing of war-risk insurance, and safety protoco\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R005",
    "title": "DB：日本央行鸽派转向比加息本身更值得关注",
    "digest": "[wechat_article.md]\n# DB：日本央行鸽派转向比加息本身更值得关注\n\n日本央行在6月会议上加息25个基点，这本该是一条中规中矩的紧缩路径。但DB最新研报揭示了一个被市场低估的信号：一位新任委员在就职不到三个月就投下反对票，这不仅打破了惯例，更预示着未来政策委员会的构成将发生根本性变化。\n\n这份报告的核心判断是：日本央行正在用一种“鸽派加息”的方式完成紧缩，其政策工具的退出节奏存在显著不对称性，而这种不对称性恰恰是市场未来定价的盲点。\n\n投资者习惯盯着利率终点在哪里，但真正决定资产定价的，往往是央行如何到达那里。DB的这份报告，提供了一套理解日本央行“行为逻辑”的新框架。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 一位新任委员的反对票，可能改变了整个政策委员会的走向\n\n6月会议以7比1的投票结果通过加息决议，唯一反对票来自今年3月才加入委员会的浅田委员。DB指出，在就职不到三个月内就公开反对行长提案，这在日本央行历史上极为罕见。\n\n这一票的意义不在于它阻止了加息——毕竟加息还是通过了。它的真正意义在于，它暴露了政策委员会内部正在形成的裂痕。浅田委员由首相高市早苗任命，而高市首相在货币政策立场上偏向鸽派。\n\n更关键的是，DB在研报中提醒：另一位新委员佐藤将于6月加入委员会。如果他也采取类似的鸽派立场，那么委员会的投票格局将从“鹰派主导”转向“鸽派力量显著增强”。而到了2027年7月，目前最鹰派的两位委员高田和田中的任期将届满。如果高市首相继续主导继任者的任命，委员会的鸽派倾向将进一步加深。\n\n这意味着什么？市场当前对加息路径的定价，可能严重低估了未来政策决策的政治化风险。一个越来越鸽派的委员会，即便继续加息，其节奏和力度也会受到内部制约。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 前\n\n[... middle omitted ...]\n\n一步拆解日本央行政策退出的真实节奏及其对全球利率环境的含义。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本央行这次加息，信号比你想象的更鸽派\n\n鸽派信号明显\n\n日本央行6月会议加息25bp，投票结果是7:1。唯一投反对票的是3月刚上任的委员Asada，他被首相高市早苗提名，上任不到三个月就公开反对行长提案，非常罕见。\n\n这背后有几个关键信号值得关注：\n\n1. 未来委员会更鸽派。6月还有一位新委员Sato上任，可能也偏鸽。到2027年7月，两位最鹰派的委员Takata和Tamura任期届满，如果高市继续提名继任者，央行鸽派倾向会更明显。\n\n2. 为什么没加50bp？研报指出，两位鹰派委员对通胀展望投了反对票，理由是“核心通胀已达目标”，但没说“通胀超目标”——所以不是鹰派意外，也解释了为什么没提更激进的加息方案。\n\n3. 前瞻指引变了。删掉了“实际利率处于极低水平”，换成“金融环境一直宽松”。这意味着日本央行不再盯着难测的自然利率，而是用更宽泛的指标判断政策，给自己留了更大灵活空间。研报判断，这暗示央行不打算连续激进加息，也不打算把利率推入紧缩区间。\n\n4. 国债购买退出更谨慎。央行明确把“改善市场功能与稳定”作为购债目标，这是新变化。研报认为，这降低了央行在市场动荡时增加购债的心理门槛。相比其他政策工具（比如\n\n[... middle omitted ...]\n\nion has significant implications for the future composition of the policy board. It is conceivable that the new member, Sato, scheduled to join in June, may also adopt a dovish voting stance. \n\n[... middle omitted ...]\n\nk, NY 10019</td><td>Tower,</td><td></td></tr><tr><td>Tel: (44) 20 7545 8000</td><td>Tel: (1) 212 250 2500</td><td>Singapore 048583</td><td></td></tr><tr><td></td><td></td><td>Tel: +65 6423 8001</td><td></td></tr></table>"
  },
  {
    "id": "R006",
    "title": "DB：美国债券市场的真正变化不在需求端，而在持有者结构的不可逆重置",
    "digest": "[wechat_article.md]\n# DB：美国债券市场的真正变化不在需求端，而在持有者结构的不可逆重置\n\n这份来自DB、由Matthew Luzzetti等五位分析师联合撰写的研报，提供了一个观察美国固定收益市场的新框架。报告的核心判断并非关于利率走势或通胀预期，而是关于一个更深层的问题：美国61万亿美元债券市场的持有者结构，正在经历一场不可逆的重置。\n\n这份报告的价值在于，它没有停留在“谁在买”的简单统计上，而是试图回答一个更根本的问题：当美联储不再是最大买家、外国央行趋于保守、而国内私人部门开始重新定价风险时，市场运行逻辑会发生怎样的变化。\n\n以下是对这份报告核心洞察的解读。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 外国持有者占比已降至30%，这个数字的背后是结构性而非周期性的退出\n\n报告显示，外国持有美国国债的比例在2026年第一季度降至30%，接近2023年第三季度29%的多年低点。这个数字本身并不惊人，但结合全球外汇储备总额的变化来看，趋势值得关注。\n\n全球外汇储备总额在2025年第三季度约为13万亿美元，虽然总量仍在增长，但美元占比持续走低。报告没有给出具体的美元占比数据，但从上下文可以推断，外国央行的增持意愿正在减弱。原因并非简单的“去美元化”，而是更务实的选择：多极储备体系下，各国央行在边际上更倾向于分散配置。\n\n这里的关键洞察是：外国持有者占比下降，不是因为他们抛售，而是因为美国国债发行量增长更快。这意味着，美国必须找到新的国内买家来吸收增量供给。谁将成为这些增量国债的边际买家，将直接影响利率定价和金融市场的稳定性。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 一级交易商的国债库存激增至5500亿美元，市场缓冲垫正在变薄\n\n报告中一个容易被忽视但极其重要的数据点：一级交易商\n\n[... middle omitted ...]\n\nMBS的配置？\n\n这些问题的答案，隐藏在这份报告的细节之中。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美债规模已破61万亿，谁在买？\n\n美债买家画像\n\n2026年Q1美国固收市场全景拆解\n\n某外资投行最新研报，把美债的买家结构拆得很清楚。几个有意思的点，直接划重点👇\n\n1️⃣ 美债总盘子有多大？\n- 截至2026年Q1，美国固收证券总规模61万亿美元\n- 国债+机构债占比约70%，是绝对主力\n- 国债占GDP比重96%，疫情前是75%\n\n2️⃣ 谁在买国债？\n- 海外持有占比降至30%，接近2023年Q3的29%低点\n- 美联储仍持有约30%的10年期以上长债\n- 私人部门持仓集中在5年以内短端\n\n3️⃣ 一级交易商仓位变化\n- 2022年以来，一级交易商的美债净持仓大幅攀升\n- 当前约5500亿美元，主要集中在中长期\n- 银行在紧缩周期减持后，又开始增持国债和机构债\n\n4️⃣ 信用债市场格局\n- 外资、保险、共同基金是三大买家\n- 外资占比约28%，寿险23%，共同基金14%\n- 非金融企业债/GDP从疫情峰值55%降至41%\n\n5️⃣ 抵押贷款市场\n- 机构MBS和机构债仍是重要组成部分\n- 银行和外资是主要持有者\n\n研报未给出具体预测，但趋势很清晰：美债供给持续增加，买家结构在变化，海外占比下降，国内机\n\n[... middle omitted ...]\n\nn Bonds?</td><td>54</td></tr><tr><td>Who is buying municipal securities and loans?</td><td>57</td></tr><tr><td>Asset allocations by investor account</td><td>61</td></tr><tr><td>Outlook</td><td\n\n[... middle omitted ...]\n\ns of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.\n\nCopyright © 2025 DB AG"
  },
  {
    "id": "R007",
    "title": "GS：日本央行加息至1%，市场真正低估的不是终点利率，而是加息节奏的重新定价",
    "digest": "[wechat_article.md]\n# GS：日本央行加息至1%，市场真正低估的不是终点利率，而是加息节奏的重新定价\n\n6月16日，日本央行以多数票通过将政策利率上调25个基点至1.0%，并维持了从明年4月起每月约2万亿日元的国债购买计划。这看起来是一次符合预期的“温和加息”。然而，GS在第一时间发布的研报中揭示了一个被市场普遍低估的深层信号：日本央行对通胀上行风险的承认，正在悄然改变未来加息的节奏预期。\n\n市场习惯于将此次加息视为“一锤子买卖”的终点，但GS的分析指向了一个不同的结论。真正需要关注的，不是1.0%这个数字本身，而是日本央行在措辞中从“实际利率极低”转向“金融环境宽松”这一表述变化背后蕴含的政策逻辑。这意味着，日本央行正在为后续的连续加息构建新的叙事框架，而市场对此的定价远未充分。\n\n这份报告的核心价值，不在于复述加息决定，而在于它精准地指出了市场与央行之间在“加息速度”和“终端利率”两个维度上的认知鸿沟。对于持有日本资产或关注全球利率环境的决策者而言，忽略这个信号可能会付出代价。\n\n![研报原图 1](assets/xhs_card_01.png)\n\n## 1. 加息本身不是新闻，但“承认通胀上行风险”才是真正的政策转向\n\nGS研报中最值得细读的，不是加息25个基点这一动作，而是日本央行在声明中明确写入的一句话：“存在基础CPI通胀偏离2%价格稳定目标上行的风险。” 这句话在4月的展望报告中尚未出现，而此次被正式纳入政策声明，意味着日本央行内部对通胀路径的评估已经发生了实质性变化。\n\n在过去的加息周期中，日本央行始终强调通胀的“暂时性”和“成本推动”特征，以此安抚市场对过快加息的担忧。但现在，措辞从“通胀正在放缓”调整为“存在上行风险”，这等同于承认：工资上涨向价格传导的机制可能比预期更持久、更广泛。\n\nGS的分析师敏锐地捕捉到，这一表述变化直接关联到后续加息紧迫性的判断。如\n\n[... middle omitted ...]\n\n息路径的概率分布，以及它对全球套利交易和日元汇率的潜在影响。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本央行加息到1%，还说了什么？\n\n**加息落地，信号明确**\n\n日本央行6月会议宣布加息0.25%，政策利率来到1%。同时维持每月购债计划，到2027年一季度逐步降到约2万亿日元，之后保持这个规模。\n\n**三个关键点**\n\n1️⃣ **加息节奏没停**\n虽然这次是预期内的动作，但央行明确表示“将继续加息”。有一位委员反对加息，另一位想加快缩债，说明内部有分歧，但主流方向是收紧。\n\n2️⃣ **通胀风险被点名**\n研报注意到，央行承认“核心通胀有超出2%目标的风险”。这是下次加息节奏的重要线索——如果通胀压力持续，后续动作可能不会等太久。\n\n3️⃣ **中性利率成焦点**\n央行此前估算中性利率在1.1%-2.5%之间。现在利率刚到1%，处于下限附近。接下来市场会紧盯副行长发布会，看他怎么评估加息空间还有多大。\n\n**后续怎么看**\n\n副行长内田真一的发布会，重点看三点：对通胀上行风险的判断、对中性利率的看法、以及是否担心“落后于曲线”。这些会直接影响市场对下次加息时点的预期。\n\n欢迎一起讨论日本央行的政策路径。\n\n#学习笔记\n\n[source_mineru.md]\n# Japan: BOJ: Raises P\n\n[... middle omitted ...]\n\n majority vote).  \nAs for the future conduct of monetary policy, the BOJ stated that it will continue to raise the policy interest rate.  \nAt Deputy Governor Shinichi Uchida's press conference\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R008",
    "title": "JPM：出口仍是唯一结构性亮点，但国内需求疲软正在拉长政策等待期",
    "digest": "[wechat_article.md]\n# JPM：出口仍是唯一结构性亮点，但国内需求疲软正在拉长政策等待期\n\n这份由JPM新兴市场亚洲经济与政策研究团队发布的第57期中国高频数据追踪报告，传递了一个核心信号：5-6月的经济活动数据并未形成清晰的复苏趋势。出口侧的运量数据在6月出现了显著的同比加速，但国内生产、信贷、汽车销售和房地产市场的信号依然偏弱。JPM团队通过高频指标与官方月度数据的映射，给出了一个值得产业决策者关注的关键判断——二季度增长动能的重新校准，将高度依赖6月剩余时间的数据表现，而政策的主动发力窗口可能正在向后推迟。\n\n报告中最引人注目的变化来自出口侧。截至6月中，港口跟踪数据显示，离港集装箱船和散货船的载重吨位分别环比增长8.9%和10.8%，同比增速更是从5月的7.7%跃升至17.9%。这意味着6月的出口量增长正在与近期运价上涨形成共振。然而，这一亮点的背面是国内需求的持续承压。JPM团队指出，4月国内活动指标的疲软已经将二季度增长风险向下倾斜，而5-6月的混合数据并未提供充分的逆转证据。对于投资者而言，真正的挑战不在于判断出口能否维持，而在于理解国内需求疲软何时会触发更实质性的政策响应，以及哪些资产类别会对这一响应率先定价。\n\n以下是对这份报告核心洞察的深度拆解。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 出口的强劲并非孤例，但运力与运价的同步上行正在重塑贸易利润分配\n\nJPM的高频追踪显示，6月以来的出口表现超出了季节性规律。不仅集装箱船离港量增长加速，散货船离港量同比增速更是达到了21.7%，环比增长10.8%。与此同时，中国出口集装箱运价指数(CCFI)至美东和美西航线分别较两周前上涨6.5%和9.1%，至波斯湾/红海航线也上涨了8.6%。运量与运价的同步上行，意味着出口企业面临的并非单纯的“量”的扩张，而是运输成本端也\n\n[... middle omitted ...]\n\n，持续跟踪中国经济的边际变化，并探讨其对全球资产配置的含义。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n出口还是那个亮点，内需在等接力棒\n\n出口延续强势，内需等待接力\n\n最近看了份外资行的高频追踪报告，6月的出口数据很亮眼，但内需这边还在等政策接力。一起拆几个关键信号👇\n\n1️⃣ 出口是最大亮点\n- 6月离港集装箱载重吨同比+17.9%（5月仅+7.7%），量价齐升\n- 集运价格继续走高，到美东/美西航线分别涨6.5%/9.1%，到波斯湾/红海航线再涨8.6%\n- 但油轮到港量依然低迷，与5月持平\n\n2️⃣ 生产端分化明显\n- 原油加工量：5月收缩加深，6月还在下滑（4月同比-5.8%）\n- 汽车产量：5月小幅改善，6月放缓（4月同比-2.6%）\n- 钢铁产量：5月收缩加深，6月有望收窄（4月同比-1.7%）\n\n3️⃣ 内需还在等风来\n- 汽车零售：5月同比-22%，新能源车跌幅小些（-7.5%）\n- 6月前两周乘用车零售同比-23%，新能源车-14%\n- 新房/二手房6月成交好于去年同期，但近期动能有所放缓\n\n4️⃣ 政策信号\n- 政府债券发行节奏放缓，6月至今仅6160亿（5月1.14万亿）\n- 若内需持续偏弱，预计三季度会加速发债和资金落地\n- 央行6月净投放4100亿，若经济压力加大，下半年降息概率上升\n\n[... middle omitted ...]\n\nreased m/m nsa mtd in June. Annual growth held up further. In aggregate, departing shipments deadweight tonnage (excluding tankers) rose 17.9% oya mtd in June (vs. 7.7% in May), suggesting vol\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 16 Jun 2026 01:55 AM HKT\n\nDisseminated 16 Jun 2026 01:55 AM HKT"
  },
  {
    "id": "R009",
    "title": "摩根斯坦利：市场真正低估的不是AI泡沫，而是供给侧的定价权转移",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：市场真正低估的不是AI泡沫，而是供给侧的定价权转移\n\n这份研报的标题叫“Charts That Caught My Eye”，出自摩根斯坦利全球研究总监Katy Huberty之手。它看起来像是一封内部备忘录——用七张图表串联起当前最值得关注的宏观与主题信号。但读完之后你会发现，这根本不是一份轻松的“看图说话”。它试图回答一个更根本的问题：当市场还在争论AI是不是泡沫、关税有没有效果、中国经济何时见底时，哪些结构性力量已经在静悄悄地改变资产定价的底层逻辑？\n\n我们的判断是：这份报告隐含的主线，并非AI主题的短期涨跌，而是全球资本正在经历一次“供给侧定价权”的再分配。从AI基础设施的“逢低买入”策略回测，到欧洲行业模型的重新排序，再到美国回流数据的“名实不符”，再到中国K型经济的固化——每一张图表都在指向同一个方向：那些掌握稀缺供给能力的企业和资产，正在获得前所未有的议价权。而市场对这一变化的定价，仍然不够充分。\n\n以下是我们从这份报告中提炼出的五个层次洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI主题的“逢低买入”策略并非情绪交易，而是对供给稀缺性的结构性套利\n\n报告中最引人注目的实证，是摩根斯坦利对AI基础设施和电力AI两个子主题开发的“逢低买入”策略回测。其规则很清晰：当主题组合下跌5%时加仓至150%，下跌15%时加仓至200%，加仓持仓三个月后恢复基准。回测结果显示，这一策略自2023年以来在两个子主题上都产生了显著的超额收益。\n\n这意味着什么？不是“AI跌了就该买”这么简单。它的深层含义是：AI基础设施的供给端存在结构性瓶颈，每一次市场情绪导致的回调，都会被后续的供需基本面修正所“救赎”。换句话说，这个主题的波动更多来自需求侧的预期摇摆，而非供给侧的实际松动。当市场因为某个短\n\n[... middle omitted ...]\n\n的研报原文、更详细的图表解析，以及对这些未解问题的持续跟踪。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI主题“逢跌买入”真的有效吗？\n\n📊 投研笔记\n\n一张图看懂机构最新观点\n\n---\n\n最近翻到一份某外资投行的研报，里面总结了几张“最值得看的图表”，信息量很大，帮你划重点 👇\n\n1️⃣ AI主题：逢跌买入策略有效\n研报回测了AI相关主题（AI基建+AI电力）的“逢跌买入”策略：在主题下跌5%时加仓到150%，下跌15%时加到200%，持有3个月。回测显示，这一策略能显著增强收益。注意是回测，不是未来保证。\n\n2️⃣ 美国CPI的3%是个分水岭\n当CPI高于3%时，通胀数据超预期会明显推高短端利率；当CPI在2%-3%之间时，只有股市反应显著；低于2%时，数据惊喜对股债都没有稳定影响。这个阈值思维很实用。\n\n3️⃣ 欧洲板块模型大洗牌\n半导体排第一，金属矿业升至第二，银行从第六跃升至第三。研报对AI、银行、矿业“加倍下注”，但调降了国防板块的评级——长期逻辑仍在，但短期缺乏催化剂。\n\n4️⃣ 中国“K型经济”持续\n预计2026年实际GDP增长4.8%，2027年4.7%。出口和新兴制造业（AI、能源转型）是主要拉动力，但消费受就业和地产拖累。净出口对GDP增长的贡献从历史均值5%飙升至30%左右，外部依赖度\n\n[... middle omitted ...]\n\n depending on whether the CPI is above / below 3%.  \n3. Europe Equity Strategy: We have refreshed our data-driven sector model, doubling down on AI, Banks, and Mining.  \n4. China Economics: We\n\n[... middle omitted ...]\n\nrantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read\n\nall the related documents carefully before investing.\n\n© 2026 MS"
  },
  {
    "id": "R010",
    "title": "GS：市场低估的不是供需平衡，而是安全溢价的结构性重置",
    "digest": "[wechat_article.md]\n# GS：市场低估的不是供需平衡，而是安全溢价的结构性重置\n\n当特朗普宣布达成临时协议、霍尔木兹海峡即将重新开放的消息传出，多数市场参与者的第一反应是油价将大幅回落。这份直觉没有错，但可能过于简单。GS在最新发布的研报中做出了一个看似矛盾、实则深刻的判断：即便在供应提前恢复正常的情景下，油价底部比大多数人想象的更坚实。\n\nGS将2026年第四季度布伦特原油预测从90美元下调至80美元，2027年均价从80美元下调至75美元。表面看这是看空调整，但隐含的结论是：即便全球石油市场在2027年面临每天320万桶的过剩，油价仍将维持在每桶75美元左右。这个数字恰好是GS的长期公允价值。\n\n这组预测的真正张力在于：一个被历史性供应冲击打乱的市场，在冲击解除后，并不会回到冲击前的定价逻辑。因为市场已经经历了一次“结构性的安全溢价重定价”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 供应恢复的时间差被压缩，但价格弹性的不对称性更值得关注\n\nGS将波斯湾出口恢复至战前水平的时间节点从8月底提前到7月底，这个一个月的提前意味着2026年第四季度和2027年油价公允价值分别下调约10美元和5美元。这个调整的幅度本身并不令人意外，但需要追问的是：为什么下调幅度不是对称的？\n\n答案藏在供需弹性的不对称中。当供应冲击发生时，价格上行的幅度远超基本面隐含的均衡水平——这是稀缺溢价。但当冲击解除时，价格下行却受到多重因素的托底，不会跌回冲击前的水平。GS称之为“安全溢价”。\n\n这种不对称在2027年的预测中表现得尤为明显。尽管GS预计2027年全球石油市场将出现每天320万桶的过剩，但布伦特原油价格预测仍维持在75美元，与长期公允价值一致。这意味着，即便在供过于求的背景下，市场仍愿意为地缘政治风险支付一个结构性溢价。\n\n这个判断对资产定价\n\n[... middle omitted ...]\n\n讨论，我们会在群内分享GS研报的完整图表和更详细的数据解读。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n霍尔木兹要通了？油价逻辑全变\n\n油价逻辑正在切换\n\n投行研报刚刚更新了油价预测，核心变化是：霍尔木兹海峡可能重新开放。\n\n之前市场一直担心波斯湾供应中断，但现在情况变了。研报认为，随着临时协议推进，波斯湾原油出口可能在7月底恢复到战前水平，比之前预期的8月提前了一个月。\n\n1️⃣ 油价预测下调\n- 2026Q4布伦特从$90下调至$80\n- 2027年均价从$80下调至$75\n- 供应恢复时间提前一个月，影响约$10/桶（2026Q4）和$5/桶（2027）\n\n2️⃣ 供应恢复存在两股力量拉扯\n向上风险（供应可能更快恢复）：\n- 沙特、阿联酋可能趁低商业库存加大增产\n- 伊朗可能因制裁放松，产量超战前水平\n\n向下风险（恢复可能更慢）：\n- 地区冲突可能反复，航运商仍谨慎\n- 清除水雷需要时间\n- 伊朗可能再次封锁海峡\n\n3️⃣ 2027年虽有大过剩，但价格不会太低\n研报预测2027年有320万桶/天的供应过剩，但OECD商业库存不会堆积过高，加上地缘风险溢价，油价仍有支撑。\n\n4️⃣ 风险偏向上行\n研报给出两种情景：\n- 上行：若霍尔木兹持续中断到2027，布伦特可能到$130+\n- 下行：若7月初就恢复，叠\n\n[... middle omitted ...]\n\n(Exhibit 1, consistent with our estimate that moving the supply normalization process one month forward reduces the fair value of crude prices for 2026Q4/2027 by around \\$10/\\$5, respectively.\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R011",
    "title": "GS：市场低估的不是电商增速放缓，而是云计算在AI需求下的重新定价",
    "digest": "[wechat_article.md]\n# GS：市场低估的不是电商增速放缓，而是云计算在AI需求下的重新定价\n\n中国互联网板块正在经历一次罕见的估值分化。一方面，电商GMV增速在5月仅录得3%的同比增长，低于市场预期，零售数据疲软直接压低了以阿里、京东为代表的电商平台股价。另一方面，云计算与AI基础设施的投资叙事却持续升温，GS在最新报告中明确将“云与数据中心”列为其最看好的子板块。这种分化背后隐藏着一个更深层的判断：市场对互联网公司的定价逻辑，正在从“电商交易规模”转向“AI计算能力的供给与议价权”。真正被低估的，不是电商需求何时复苏，而是云计算在AI需求爆发中获得的重新定价空间。\n\n这份GS于2026年6月发布的《Navigating China Internet: Ecommerce Tracker》报告，看似是一份常规的电商追踪月报，实则是对阿里近期股价疲软的全面回应，并在此基础上重构了整个中国互联网的投资排序。报告的核心信号是：电商的短期压力是真实的，但云计算的结构性机会正在被低估，而阿里恰好是这两个叙事交汇点上的关键标的。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 五月零售数据的“坏消息”已被市场消化，电商竞争格局正在从价格战转向运营效率\n\n五月全国线上零售商品GMV同比增长3%，相较于四月的零增长有所改善，但整体零售数据低于彭博一致预期。珠宝、家电、体育用品等品类分别录得-8.9%、-15.6%和-8%的同比下滑，显示出消费端的谨慎情绪并未消散。家电品类的进一步下滑尤其值得关注，GS指出这与去年“以旧换新”政策带来的高基数有关，手机品类自2025年1月被纳入换新补贴后，基数效应仍在拖累同比增速。\n\n对于市场最关心的阿里CMR（客户管理收入）问题，GS的判断是：市场已经预期了二季度CMR的低个位数同比下滑，而包裹量的健康增长可能会缩小\n\n[... middle omitted ...]\n\n将基于这份报告和后续的数据更新，持续跟踪这些关键变量的演变。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n五月线上零售回暖，阿里AI云成焦点\n\n线上零售企稳回升\n\n5月线上零售商品GMV同比增长3%，相比4月的持平有明显改善。食品和服装品类表现不错，但家电和通讯设备继续拖后腿，分别同比-16%和+1%。整体社零数据低于预期，5月同比-0.6%，珠宝、家电、体育用品下滑明显。\n\n618大促新趋势\n\n今年618平台打法变了，不再搞复杂满减，转向直接折扣。竞争更理性，监管也在收紧。5月13日到6月14日，包裹量同比增长8%，比去年同期的16%有所放缓。快递行业5月包裹量增速约6%，6月初已回升到9%左右。\n\n阿里近期关注点拆解\n\n1️⃣ 电商CMR承压：4-5月零售数据疲软，加上商家返利政策，预计6月季度CMR同比下滑。但包裹量增长可能缩小GMV和CMR的差距，竞争环境良性。\n\n2️⃣ AI云竞争格局：政府计划5年投2万亿建数据中心，电信运营商主导。但互联网巨头在AI模型和芯片能力上有先发优势，MaaS和定制芯片将形成差异化。\n\n3️⃣ AI模型定价：竞争比预期激烈，但头部模型（如GLM、Qwen3.7 Max）仍有定价权。阿里云在计算层领先，有望受益于AI token需求的爆发。\n\n4️⃣ 资本开支来源：未来3年预计\n\n[... middle omitted ...]\n\nfurther/moderated to -16%/+1% yoy (vs. -15%/+6% in Apr) on the high-base of the trade-in program last year (mobile phones were included in trade-in since Jan-2025). We continue to estimate 2Q \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R012",
    "title": "GS：白酒端午动销预期转弱，市场低估了渠道库存周期的“钝化”",
    "digest": "[wechat_article.md]\n# GS：白酒端午动销预期转弱，市场低估了渠道库存周期的“钝化”\n\n当市场还在讨论“低基数能否带来端午反弹”时，一份来自GS的最新渠道追踪报告给出了一个更冷静的判断：今年的端午节，可能不会成为白酒行业的拐点。\n\n这份于6月中旬发布的研报，通过密集的渠道调研和价格数据跟踪，揭示了一个值得产业决策者关注的信号。尽管2025年同期因政策冲击形成了低基数，但经销商对今年端午的零售增长预期反而从此前的20%-30%下修至10%-20%。飞天茅台批发价在1635-1670元区间窄幅波动，而普五和国窖1573的批价则持续疲软，其中普五在部分批发市场的报价甚至受618补贴压力跌至760元。\n\n这些数字背后，不是一个简单的“旺季不旺”的故事。它指向一个更深层的结构性变化：白酒行业的渠道库存周期正在失去弹性，价格信号对短期消费刺激的反应正在钝化。对于投资者和管理者而言，理解这种“钝化”的成因，比猜测下一个节日的销量数字更重要。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 经销商预期的下修并非季节性扰动，而是渠道信心的系统性降温\n\nGS报告中最值得关注的数据点，并非批发价格的绝对水平，而是经销商预期的变化轨迹。从“期待20%-30%增长”到“预期10%-20%增长”，这个下修发生在2025年低基数背景之下。这意味着，经销商并非因为去年卖得差而悲观，而是因为当前动销环境的疲软超出了他们对“低基数反弹”的原有判断。\n\n渠道备货节奏是另一个佐证。报告指出，品牌方在节前的渠道动作相对平淡。在白酒行业，节前品牌方通常会通过密集的渠道政策、促销活动来推动经销商打款备货。如果连品牌方自身都选择“按兵不动”，这通常意味着它们对终端真实需求的判断同样保守。\n\n这里需要强调的是，端午节在白酒消费周期中的权重远不及中秋国庆。GS在报告中明确提示，中秋国庆\n\n[... middle omitted ...]\n\n追踪这些关键变量的变化，并获取完整的原始图表和更多独家分析。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n白酒端午备货，经销商有点冷\n\n白酒端午备货偏弱\n\n这次端午，经销商预期降温了\n\n最近某外资投行更新了白酒渠道追踪，聊几个核心观察👇\n\n**1/ 端午动销预期下调**\n- 经销商反馈：茅台/五粮液终端零售增长预期从20-30%降至10-20%\n- 今年基数低（去年端午受政策影响高端酒下滑双位数），但依然没提振信心\n- 品牌方节前铺货动作偏保守，渠道备货意愿不强\n\n**2/ 飞天茅台批价稳，非标偏软**\n- 原箱飞天：1670元/瓶（微降5元），散瓶：1635元/瓶（持平）\n- 生肖/1L装茅台价格回调（分别跌60/30元），推测跟i茅台放量有关\n- i茅台5月MAU达956万，5月26日单日交易量713万笔（vs Q1日均398万）\n\n**3/ 普五和1573价格承压**\n- 普五批价：840元（第三方数据）/ 760元（百荣市场，受618补贴影响）\n- 国窖1573：840元，持平但偏弱\n- 五粮液暂停发货后批价仍稳不住，反映需求端压力\n\n**4/ 渠道库存健康，但信心不足**\n- 飞天茅台渠道库存<1个月（华东地区）\n- 经销商普遍对中秋国庆更关注，端午只是小节点\n\n**5/ 行业动态**\n- 五粮液管理层\n\n[... middle omitted ...]\n\ndistributor stocking pace/demand for the Dragon Boat Festival, our channel checks show relatively muted pre-season channel actions by brands, indicating still cautious distributor sentiment/ou\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R013",
    "title": "GS：5月经济数据低于预期，但政策窗口正在打开",
    "digest": "[wechat_article.md]\n# GS：5月经济数据低于预期，但政策窗口正在打开\n\n中国经济在二季度中段遭遇了比预期更猛烈的逆风。5月固定资产投资与零售数据双双低于市场预期，工业产出大体符合预期。这份GS研报的核心判断并非停留在“数据不好”这一表层，而是提出了一个值得所有决策者仔细推敲的叙事：**短期疲软背后，结构性分化正在加剧，而政策空间与外部环境的边际改善，可能正在为三季度积蓄反弹动能。**\n\n这不是一份简单的“数据点评”。它揭示了几个关键信号：服务消费与商品消费的增速缺口在持续扩大；投资端的拖累并非均匀分布，天气与债券发行节奏的扰动被市场低估；而房地产虽然在低位，但一线城市的“绿芽”并未完全枯萎。更重要的是，GS明确指出了7月政治局会议作为潜在政策调整窗口的战略意义。\n\n对于关注中国资产定价的读者而言，这份报告最值得深思的地方，不是5月数据有多差，而是**市场是否正在低估供给侧的再定价能力，以及政策应对的灵活性。**\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 工业产出的韧性来自出口，但汽车与化工的拖累不容忽视\n\n5月工业增加值同比增长4.5%，较4月的4.1%温和回升，基本符合预期。表面上看，这是好消息。但GS的拆解揭示了一个更复杂的图景：支撑增长的主要是计算机与电子设备、电力热力等行业，而汽车、化工、有色金属冶炼的产出增速却在放缓。\n\n汽车产量同比增速从4月的-2.6%进一步下滑至5月的-3.2%。这并非孤立现象。全球能源冲击持续压制化工相关制造业，硫酸和化学纤维产出增速依然疲弱。与此同时，智能手机和计算机产量同比分别下降8.8%和19.4%，消费电子链条的压力依然显著。\n\n真正值得关注的是，工业机器人产量同比增长27.9%，金属切削机床增长10.7%。这组数据暗示，自动化设备投资仍在加速，企业并非全面收缩，而是在有选择地加大资本\n\n[... middle omitted ...]\n\n，结合更多一手数据，与读者一起推演下半年中国经济的关键变量。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月经济数据：出口撑住，内需有点冷\n\n📊 5月经济观察\n\n5月的经济数据出来了，工业还行，但投资和消费有点弱。\n\n**1️⃣ 工业：出口是最大支撑**\n5月工业增加值同比+4.5%，比4月好一些。主要靠出口拉动，计算机、电子设备、电力这些行业生产加快，但汽车产量还在下滑，化工受能源价格影响也偏弱。\n\n**2️⃣ 投资：基建和地产都在拖后腿**\n固定资产投资单月同比-10.6%，比4月更差。一方面是天气不好（南方暴雨+北方高温），另一方面政府债券发行还是偏慢。地产投资-24.3%，基建-11.2%，只有制造业投资略有改善。\n\n**3️⃣ 消费：降幅扩大，服务消费好于商品**\n社零同比-0.6%，是2022年12月以来最低。汽车、家电都在下滑，但服务消费指数还在往上走，说明大家更愿意为体验花钱，而不是买东西。\n\n**4️⃣ 地产：压力持续，但一线城市有回暖迹象**\n销售面积-13.1%，新开工-24.6%，房价还在跌，主要压力在低线城市。\n\n**5️⃣ 就业：略有改善**\n全国失业率从5.2%降到5.1%，但16-24岁年轻人失业率还有16.3%（4月数据），压力不小。\n\n**6️⃣ 展望：Q2可能低于预期，Q3\n\n[... middle omitted ...]\n\nxed asset investment (FAI) growth fell further -10.6% yoy in May from -8.2% yoy in April, reflecting both adverse weather conditions and a still-slow pace of government bond issuance. Retail s\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R014",
    "title": "GS：市场低估了全球LNG供给的结构性改善，而非地缘政治风险",
    "digest": "[wechat_article.md]\n# GS：市场低估了全球LNG供给的结构性改善，而非地缘政治风险\n\n欧洲天然气市场刚刚经历了一个关键的转折点。美伊协议为霍尔木兹海峡的能源流动恢复铺平了道路，这直接决定了欧洲今年冬季的天然气储存补充前景。但GS这份研报的真正价值，并不在于它对地缘政治事件的判断——毕竟协议的达成与落空都存在变数——而在于它揭示了一个被当前价格所忽视的结构性变化：全球除卡塔尔外的LNG供给正在以超出预期的速度增长，这一变化正在从根本上改变欧洲天然气市场的供需平衡。\n\n这份报告最值得关注的判断是：即便霍尔木兹海峡的恢复时间晚于预期，欧洲天然气价格在2026年下半年仍将稳定在41欧元/兆瓦时左右，而2027年将进一步降至30欧元/兆瓦时。这背后是两个被市场低估的变量：一是非卡塔尔LNG供给的大幅增长，二是市场对欧洲储气库填充目标的主动下调。这两个变量正在重塑欧洲天然气市场的定价锚。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 非卡塔尔LNG供给的意外增长正在抵消霍尔木兹中断的紧缩效应\n\nGS在报告中明确指出，全球除卡塔尔外的LNG供给增长超出了他们此前的预期。他们将2026年6月全球除卡塔尔外的LNG供给预测从此前水平上调了10百万吨/年，达到384百万吨/年。这一上调主要来自几个来源：阿曼、马来西亚和挪威等地的维护作业明显减少；尼日利亚的原料气供应出现强劲反弹；以及俄罗斯受制裁的LNG出口量增加。\n\n这一判断的意义在于：市场此前对欧洲天然气紧缺的担忧，很大程度上建立在对卡塔尔LNG供给中断的线性外推上。但GS的数据表明，全球LNG供给的韧性远比市场想象的更强。当卡塔尔的供给出现缺口时，其他地区的产能正在通过维护优化和产能释放来弥补这一缺口。这不是一次性的应急反应，而是全球LNG供给体系在价格信号下的自我调节。\n\n对于产业决策者而言，\n\n[... middle omitted ...]\n\n图表数据和敏感性分析的读者，欢迎来我们的星球微信群继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美伊协议落地，欧洲气价怎么看？\n\n封面：欧洲气价逻辑拆解\n\n副标题：存储补库压力缓解了吗\n\n---\n\n最近美伊达成协议，霍尔木兹海峡的能源流动有望恢复。这对欧洲天然气市场意味着什么？某外资投行更新了判断。\n\n**1/ 核心逻辑变了**\n之前分析师反复提醒：欧洲储气库补库压力很大，如果霍尔木兹的LNG流量不恢复，TTF（欧洲气价）就得涨到100欧元以上才能逼退亚洲买家。现在协议落地，情况转向。\n\n**2/ 时间线小幅推迟**\n预计LNG流量在7月底前恢复正常，比之前预期的6月底晚了一个月。但有两个因素对冲了推迟的影响：\n- 卡塔尔以外的全球LNG供应超预期增长（阿曼、马来西亚、挪威检修减少，尼日利亚反弹）\n- 市场对储气率的目标从80%下调到了70-75%\n\n**3/ 储气库能补到多满？**\n只要气价相对煤价偏贵（TTF在40欧元出头），西北欧储气库到10月底可以补到74%左右。这个水平能扛住一个标准差以上的冷冬。\n\n**4/ 2027年更宽松**\n预计2027年全球LNG供应同比增加47百万吨/年，叠加冬季末库存更高，2027年10月底储气率可达89%。对应TTF均价预测30欧元/兆瓦时。\n\n**5/ 风险依\n\n[... middle omitted ...]\n\ntly driven by maintenance avoidance. Second, TTF pricing in recent weeks suggests that the market is targeting a 70%-75% gas storage fill this summer, lower than the 80% we had previously assu\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R015",
    "title": "NOM：五月经济数据印证了一个被市场低估的核心矛盾——供给侧的约束比需求侧更顽固",
    "digest": "[wechat_article.md]\n# NOM：五月经济数据印证了一个被市场低估的核心矛盾——供给侧的约束比需求侧更顽固\n\n五月经济数据出炉，零售销售同比转负，固定资产投资大幅下滑，工业增加值反弹微弱。市场习惯性地将这些数字解读为“内需不足”，并等待新一轮刺激政策。NOM这份研报提供的关键洞察是：真正的问题不是需求不够，而是供给端出现了多重结构性约束——从石油供应中断到“反内卷”政策对产能的主动压制，这些约束正在改变经济的运行逻辑。投资者若只盯着需求侧的刺激预期，可能会错过更深刻的定价变化。\n\n以下是我们从这份报告中提炼出的五个关键层次，每一个都在回答同一个问题：为什么五月数据比表面数字更值得警惕。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 五月数据的核心特征是“需求弱、供给更紧”，而非简单的经济放缓\n\n零售销售同比转负至-0.6%，固定资产投资同比暴跌至-10.7%，这两个数字足以让市场紧张。但NOM的分析指出，这两条线背后的驱动力并不相同。零售的疲软更多来自消费者信心低迷和以旧换新政策退坡后的“还债效应”，而固定资产投资的崩塌则叠加了政策主动压缩产能的影响——尤其是“反内卷”运动在制造业投资上的持续压制。这意味着，即使未来需求有所回暖，供给端也可能因为政策约束和原料短缺而无法同步响应。这种“供给刚性”才是当前经济运行中最容易被忽视的变量。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 石油供应冲击对工业生产的传导，远比市场预期的更深、更持久\n\n五月原油加工量同比下滑9.1%，创下多年新低。NOM明确指出，这不仅仅是短期事件，而是中东能源供应中断后，中国工业体系暴露出的结构性脆弱。硫磺短缺已经传导至硫酸产量下滑，进而影响整个化工产业链。乙烯、化学纤维等关键中间品的产出增速连续数月下滑。这意味着，即\n\n[... middle omitted ...]\n\n更多关于财政效率、项目审批动态以及下半年经济走势的跟踪分析。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月经济数据：内需疲软，AI难救场\n\n内需持续走弱，AI救不了\n\n某外资投行最新研报显示，5月中国经济数据整体偏弱，内需进一步恶化。零售销售同比-0.6%，为2022年底以来首次转负；固定资产投资同比-10.7%，远低于预期。工业生产小幅反弹至4.5%，但动力不足。\n\n1️⃣ 零售“冷”得明显\n- 汽车零售额同比-16.1%，消费信心低迷\n- 家电、家具、体育娱乐零售持续负增长\n- 餐饮收入增速降至0.6%，大餐厅甚至转负\n- 石油产品零售额虽改善，但实际消费可能大降30%\n\n2️⃣ 投资“急刹车”\n- 固定资产投资同比-10.7%，连续两个月负增长\n- 制造业投资-4.2%，政策限制产能扩张成主因\n- 基建投资-10.8%，资金到位但项目落地慢\n- 房地产投资-24.3%，仍是最大拖累项\n\n3️⃣ 工业“结构性分化”\n- 集成电路产量+22.9%，AI需求支撑\n- 电脑、手机产量大幅下滑（-19.4%、-8.8%）\n- 汽车产量-3.2%，内销疲软拖累\n- 石油加工量-9.1%，能源供应链持续受扰\n\n4️⃣ 房价“一线涨、全国跌”\n- 一线城市二手房价格+0.35%，北上广深均涨\n- 二线城市-0.19%，\n\n[... middle omitted ...]\n\n: -4.9%). IP growth rebounded marginally to 4.5% y-o-y in May from 4.1% in April, largely in line with market expectations (Consensus: 4.4%; NOM: 4.1%) but well below the readings of 6.1% in Q\n\n[... middle omitted ...]\n\nable upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R016",
    "title": "Citi：市场低估了中国AI供应链在下一代GPU架构中的份额跃迁",
    "digest": "[wechat_article.md]\n# Citi：市场低估了中国AI供应链在下一代GPU架构中的份额跃迁\n\n这份Citi研报的核心判断并非“AI需求仍在增长”这类共识，而是一个更具体、更具投资含义的结论：中国AI基础设施供应商在英伟达GB200架构中获得的份额有限，但在GB300和Vera Rubin架构中，他们将实现显著的份额跃迁。这不是一个渐进式的改善，而是一个由技术升级、响应速度和产能承诺共同驱动的结构性拐点。对于关注中国制造业升级和AI产业链定价权的投资者来说，这是当前最值得深入理解的变化。\n\n报告基于2026年6月9日至12日的一场产业调研，覆盖了13家中国工业与机器人领域公司。调研中最受投资者关注的公司几乎全部集中在英伟达供应链内，包括PCB钻孔设备商大族数控、全球最大覆铜板（CCL）厂商生益科技、全球最大钻头公司鼎泰高科，以及一家英伟达认证的电源供应商。这些公司过去在GB200中的“钱包份额”远低于日韩台同行，但调研反馈一致指向一个转折点：下一代架构将成为中国供应商证明自身价值的主战场。\n\n这份报告的价值不仅在于揭示了这一趋势，更在于它提供了足够细致的产业链验证——从覆铜板、玻纤布到PCB设备，每一环节的产能瓶颈、技术壁垒和盈利前景都有具体数据支撑。以下是我们从报告中提炼出的五个关键洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 中国AI供应商的份额跃迁不是价格战的结果，而是技术曲线和响应速度的胜利\n\n一个常见的误解是，中国供应商的竞争力主要来自价格。但这份报告纠正了这一看法。调研中，生益科技、大族数控、Grace Fabric等公司明确指出，他们赢得更多份额的核心因素依次是：技术曲线从全球视角看已实现升级、对英伟达快速变化的架构有更敏捷的响应时间、以及对产能建设有更坚定的承诺。价格竞争被排在最后。\n\n这一判断有重要的行业含义。\n\n[... middle omitted ...]\n\n完整报告的原始图表和财务模型，对这些未解问题做更深入的拆解。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI产业链里，中国玩家正在“抢份额”\n\n中国AI基础设施，份额在涨\n\n某外资投行刚调研回来，核心观点：中国AI基础设施公司，正在英伟达下一代架构里拿到更多份额。\n\n1️⃣ 从GB200到GB300/Vera Rubin，中国供应商的“钱包份额”要涨了\n- 之前GB200时代，中国供应商拿到的份额远低于日韩台同行\n- 但到了GB300和Vera Rubin，技术升级、响应速度、产能投入，都让中国玩家更有竞争力\n- 研报认为，这不是简单的价格战，而是技术曲线升级带来的结构性机会\n\n2️⃣ 上游材料是最大瓶颈，也是最大机会\n- AI玻纤布和电子玻纤布，是CCL/PCB供应链里产能最紧张的环节\n- 某CCL龙头，AI-CCL月产能占比从去年的~10%涨到今年中的~15%，年底可能到~20%\n- 某玻纤布龙头，AI玻纤布产能从2025年~500万米，暴增到2026年2500万米，2027年至少3300万米\n\n3️⃣ 人形机器人链：零部件>整机\n- 某精密零部件公司已向美国头部机器人公司批量出货\n- 预计Optimus Gen3今年产量1-2万台，明年可能10倍增长到10万+\n- 研报认为，零部件环节比整机更有吸引力\n\n[... middle omitted ...]\n\ner-changing NVDA architecture and commitment for capacity build. This should lead to earnings upside for China plays in our coverage. Besides AI-Infra, other verticals like embodied AI, factor\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R017",
    "title": "GS：中国房地产市场的真实信号并非全面回暖，而是核心城市的结构性再定价",
    "digest": "[wechat_article.md]\n# GS：中国房地产市场的真实信号并非全面回暖，而是核心城市的结构性再定价\n\n市场参与者对5月房地产数据的解读，很容易滑入两个极端：要么被全国层面的同比下滑数字吓退，要么被一线城市的环比改善故事所吸引。GS最新发布的5月中国房地产月度追踪报告提供了一组值得细看的数据，其核心判断并非简单的“回暖”或“继续探底”，而是一个更为精细的结构性叙事——全国总量的疲软掩盖了核心城市正在发生的资产价格再定价过程，而这种再定价的可持续性，取决于供给侧的深度调整而非需求侧的短暂脉冲。\n\n这份报告最值得关注的信号，是一线城市已经连续3至4个月录得二手房价格环比正增长，同时二手房挂牌量同比连续第三个月下降。这两个指标的同步出现，在近两年的市场周期中并不常见。它意味着核心城市的二手房市场，正在从“降价换量”的存量博弈，转向“量稳价升”的供需再平衡。对于产业决策者和高净值投资者而言，真正需要追问的不是“市场到底了没有”，而是“哪些城市的资产正在被重新定价，以及这种定价能走多远”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 一线城市的价格韧性并非偶然，而是供给收缩与需求结构升级共同作用的结果\n\nGS报告显示，5月70城新房价格环比平均下降0.2%，与4月、3月基本持平；而二手房价格环比降幅则从4月的0.2%扩大至0.3%。表面上看，二手房市场似乎比新房更弱。但一线城市的表现提供了完全相反的图景：5月一线城市新房价格环比上涨0.2%，已是连续第4个月正增长；二手房价格环比上涨0.3%，是连续第3个月正增长。深圳和上海几乎所有产品类型的二手房成交价格都在改善，北京的高端项目也跑赢大盘。\n\n这里需要回答一个“为什么”的问题。一线城市的价格韧性，不能简单归结为“有钱人还在买房”。GS报告指出，新房价格受到产品结构升级的支撑——核心区域的新房供应\n\n[... middle omitted ...]\n\n哪些二线城市最有可能率先跟上——欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n一线城市房价，连续3个月回暖\n\n**一线城市，韧性显现**\n\n看了一圈5月的地产数据，最直观的感受是：**一线城市真的稳住了**，但全国其他城市还在磨底。某外资投行的跟踪报告，信息量不小，挑几个重点聊聊。\n\n**1. 房价：一线涨，二线跌，分化加剧**\n- 5月新房价格（70城）环比跌0.2%，和4月、3月差不多。\n- 但一线城市新房环比涨0.2%，二手房涨0.3%，**已经连续3-4个月环比为正**。\n- 深圳、上海二手房大部分户型都在涨，北京高端盘也表现不错。而二线城市新房、二手房还在环比跌0.1%-0.2%。\n\n**2. 成交量：新房弱，二手房反而有亮点**\n- 5月全国新房销售面积同比跌13%，金额跌9%，略低于预期。\n- 但15城二手房成交量同比涨8%，比4月的+4%还强。挂牌量也连续3个月同比下降，说明卖房的人在减少，成交速度在加快。\n\n**3. 租金：一线城市意外回暖**\n- 虽然50城平均租金还在跌，但**一线城市租金已经连续3个月环比上涨**。上海、深圳、天津、乌鲁木齐是过去三个月表现最好的城市。\n\n**4. 开发商：拿地更谨慎，但利润还行**\n- 跟踪的几家开发商，5月拿地强度（拿地金额/\n\n[... middle omitted ...]\n\nion activities were moderately below GSe; secondary sales above GSe at +HSD% yoy; rent resilient in Tier-1 cities while continuing to trend lower in 50-cities; tracked developers' landbanking \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R018",
    "title": "GS：新能源车周订单回落，但渗透率突破67%才是市场真正该关注的信号",
    "digest": "[wechat_article.md]\n# GS：新能源车周订单回落，但渗透率突破67%才是市场真正该关注的信号\n\n6月第二周，中国新能源车市交出了一份看似矛盾的答卷：周订单环比下降13%，同比下降14%，但零售与批发的新能源渗透率却双双突破67%。对于习惯用周订单增速来线性外推行业景气度的投资者而言，这个组合容易引发困惑。\n\nGS本周发布的《中国新能源汽车周刊》提供了理解这一现象的关键框架。报告的核心洞察在于：订单的短期波动主要受到5月底新品集中上市脉冲退潮的影响，属于预期内的周期性回落；而渗透率在6月初持续上行至历史高位，则指向一个更深层的结构性变化——燃油车市场份额正在被不可逆地侵蚀，且这一过程并未因个别品牌的订单波动而放缓。\n\n市场真正需要关注的，不是“下周订单会不会反弹”，而是“当渗透率突破三分之二后，行业竞争的逻辑将从抢增量转向抢存量，这意味着什么”。GS的数据显示，这一临界点已经到来。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 订单回落是新品脉冲退潮的正常表现，而非需求拐点\n\nGS追踪的9家主要新能源品牌在6月第二周（6月8日至14日）合计订单为15.36万辆，环比下降13%，同比下降14%。表面上看，这一数据似乎预示着5月以来的回暖势头正在受阻。\n\n但报告明确指出，这一回落是“coming off the initial pulse of new model launches in late May”——即5月底新品上市带来的首波脉冲消退后，订单回归正常节奏。5月最后一周（W22），合计订单曾达到20.78万辆的年内高位，随后W23回落至17.71万辆，W24进一步降至15.36万辆。这是一个典型的“发布周冲高、随后回归”的节奏，在汽车行业的新品周期中属于正常现象。\n\n从同比角度看，虽然整体下降14%，但结构分化显著。蔚来、理想、小\n\n[... middle omitted ...]\n\n方向。欢迎加入我们的星球微信群，一起追踪这些关键变量的变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n新能源周报：订单回落，渗透率破67%\n\n📊 新能源渗透率站上67%\n\n6月第一周（6/1-6/7），新能源车零售渗透率66.7%，批发渗透率67.2%，相比5月的63%/61.1%明显提升。整体乘用车零售22.8万辆，同比-23%。\n\n📉 订单降温，谁在抗压？\n\n6月第二周（6/8-6/14），主要新能源品牌合计订单环比-13%，同比-14%。5月底新车上市脉冲效应退潮后，订单自然回落。\n\n1️⃣ **吉利、比亚迪、特斯拉相对抗跌**：周订单环比分别+8%/-4%/-8%，跑赢大盘\n2️⃣ **蔚来表现亮眼**：YTD订单同比+93%，6月第二周订单虽环比-30%，但绝对量仍处高位\n3️⃣ **鸿蒙智行**：YTD订单同比+31%，但周订单环比-25%，波动较大\n\n🔍 三个关键信号\n\n**价格端**：新能源经销商折扣小幅收窄（7.54% vs 上周7.79%），燃油车折扣继续扩大（19.56%），燃油车压力不减。\n\n**上游电池**：电池级碳酸锂涨至17.45万/吨（环比+3.6%），但电芯价格稳定，成本传导暂未发生。\n\n**新品密集上市**：蔚来ET5/ET5T/EC6改款、零跑C10/C11/C16改款、\n\n[... middle omitted ...]\n\n026 Week 24 highlights:\n\nKey brand orders: Geely / BYD / Tesla showed defensive growth at +8%/-4%/-8% wow.  \nCPCA weekly trend: As of Jun 1-7, PV retail volume was 228k units (-23% yoy/-11% mo\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R019",
    "title": "GS：五月新房价格跌幅收窄，但市场真正的信号藏在二手房与库存之间",
    "digest": "[wechat_article.md]\n# GS：五月新房价格跌幅收窄，但市场真正的信号藏在二手房与库存之间\n\n这份来自GS中国经济学团队的最新研报，基于国家统计局70城数据，给出了一个看似温和但内部结构高度分化的判断：五月新房价格环比跌幅收窄，一线城市甚至出现环比正增长。但如果你只读到“企稳”两个字，可能就错过了这份报告真正想传达的信息。\n\nGS团队在报告中反复强调一个关键区分：70城数据仅覆盖新房市场。而二手房市场的价格，根据NBS及第三方平台的数据，过去一年跌幅在5%至10%之间。这意味着，当前市场的价格信号存在明显的“双轨”特征——新房市场的边际改善，并不能简单等同于整体房价的触底。\n\n对于产业决策者和高净值读者而言，真正需要追问的不是“市场是否已经见底”，而是“在总量数据改善的表象下，哪些结构性变量正在重塑定价逻辑”。这份报告提供了几个值得深挖的线索。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 一线城市新房价格环比转正，但驱动力高度集中且依赖局部政策\n\n五月数据最亮眼的部分是一线城市新房价格环比年化上涨1.4%，较四月的0.7%明显加速。其中深圳表现最为突出，环比年化涨幅达到3.9%，远超四月的1.6%。上海、杭州、合肥等城市同比依然保持正增长。\n\n然而，GS在报告中明确指出，近期的政策宽松仍然是“局部性的”。广州的收储计划、各地对住房公积金使用的扩大，这些措施并未形成全国性的、系统性的需求提振。换言之，一线城市的回暖更多是局部政策刺激与个别城市供需结构改善的结果，而非全国房地产市场的普遍性复苏。\n\n这意味着，投资者在关注一线城市数据时，需要追问：这种环比改善的可持续性如何？如果政策刺激的边际效应递减，这些城市能否依靠自身的基本面维持价格稳定？目前报告并未给出明确答案，但隐含的判断是，这种改善的广度与深度仍有待观察。\n\n![研报原图 2]\n\n[... middle omitted ...]\n\n，以及我们基于这些数据对下半年地产板块资产配置的进一步推演。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月新房跌幅收窄，一线城市转涨\n\n新房数据回暖\n\n5月70城新房均价环比跌幅收窄至1.8%，比4月的2.9%好不少。一线城市更是连续两个月环比上涨，深圳领涨（+3.9%）。\n\n三个值得关注的点：\n\n1️⃣ 新房 vs 二手房分化明显\n新房数据好看，但二手房才是真实市场。投行研报指出，过去一年二手房实际跌了5-10%。上海、杭州、合肥新房同比还在涨，但全国整体同比仍跌3.5%。\n\n2️⃣ 城市梯队分化加剧\n一线城市环比涨1.4%，深圳最强。二三线城市跌幅也在收窄（二线-1.1%，三线-1.8%），但整体仍是下行趋势。政策调整集中在局部城市，比如广州的收储计划。\n\n3️⃣ 库存压力略有缓解\n30城新房交易量5-6月基本持平去年。主要城市去化周期从28.9个月降到28.5个月，主要是二线城市贡献。\n\n整体看，新房市场在政策刺激下出现企稳迹象，但二手房是否跟涨、能否持续，还要观察后续数据。\n\n欢迎一起讨论你对当前楼市的观察。\n\n#学习笔记\n\n[source_mineru.md]\n# China: 70-city average primary property price decline narrowed in Ma\n\n[... middle omitted ...]\n\n(new home sales) only; secondary market data by NBS and some third-party platforms suggest price declines of $5 - 10\\%$ over the past year.\n\n## Key numbers: $^{1}$\n\nNBS' 70-city primary-market\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R020",
    "title": "摩根斯坦利：中国房地产市场真正的拐点信号，不是成交量的反弹，而是成交结构的断裂",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：中国房地产市场真正的拐点信号，不是成交量的反弹，而是成交结构的断裂\n\n这份摩根斯坦利最新一期中国房地产周度数据库追踪报告，覆盖截至6月14日的数据，释放的信号远比表面数字复杂。市场在寻找“底部确认”的信号，但这份报告揭示的，是一个更值得警惕的结构性分化：新房与二手房、一线与低线城市之间的表现正在走向彻底断裂。\n\n报告最核心的判断并非成交量本身，而是这组数据合在一起指向了一个结论：中国房地产市场的定价机制正在从“新房锚定”转向“二手房锚定”，而这一转变对开发商、投资者和地方财政的含义，远未被市场充分定价。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 新房成交的“脉冲式反弹”正在退潮，同比增速从+21%骤降至-1%，市场不应将其视为常态波动\n\n上周50城新房成交同比下滑1%，而此前一周还是+21%的增长。两周之内，增速落差高达22个百分点。这不是正常波动，而是一个清晰的信号：此前几周的反弹更多依赖于积压需求和政策窗口期的集中释放，而非需求面的根本改善。\n\n从全年累计看，新房成交同比仍为-12%。一线城市表现最弱，同比下降9%，而此前一周还是+3%。三线城市同样从+27%跌至-4%。这种同步回落，说明反弹并非个别城市的独立行情，而是整体市场缺乏持续动力。\n\n这组数据意味着什么？如果市场参与者仍用“政策刺激后会有持续反弹”的历史经验来预测未来，可能会持续误判。本轮周期的特殊性在于，需求端的修复速度远慢于供给端的收缩，而政策工具的空间也已大幅收窄。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 二手房成交的韧性正在重塑市场定价权，这是报告最容易被忽视的结构性信号\n\n与新房形成鲜明对比的是，10城二手房成交同比增长4%，全年累计+6%。一线城市二手房成交同比+3\n\n[... middle omitted ...]\n\n合更多机构的交叉验证数据，持续跟踪这个市场最关键的信号变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n6月楼市数据出炉，新房成交小幅回落\n\n📉 新房成交微降\n\n某外资投行最新研报显示，6月第二周（截至6月14日），50城新房成交面积同比下滑1%，相比前一周的+21%有明显回落。\n\n分城市看：\n1️⃣ 一线城市：同比-9%，较前一周的+3%转跌\n2️⃣ 二线城市：同比+2%，但增速从+25%大幅放缓\n3️⃣ 三线城市：同比-4%，前一周为+27%\n\n整体来看，今年累计新房成交仍为-12%。\n\n📈 二手房相对坚挺\n\n10城二手房成交同比+4%，虽然增速从+23%放缓，但韧性更强。\n\n一线城市二手房成交同比+3%（前周+34%）\n二线城市同比+3%（前周+17%）\n\n累计同比+6%，说明二手房市场修复节奏更稳。\n\n🏠 去化率腰斩\n\n上周整体去化率仅48%，前一周为100%。一线城市从100%降至45%，二线城市51%。\n\n挂牌价方面，六城二手挂牌价指数为17.4%（前周17.5%），基本持平。一线城市中介指数53.2（前周54.4），小幅回落。\n\n📌 几点观察\n\n- 新房热度未能延续，政策刺激效果在减弱\n- 二手房成交相对稳定，但挂牌价指数未明显改善\n- 去化率大幅回落，供需关系仍需时间修复\n\n大家觉得下半年楼市会\n\n[... middle omitted ...]\n\n cities increased 4% YoY (vs. +23% YoY in the previous week), bringing YTD sales to +6% YoY: Tier 1 city weekly secondary unit sales rose 3% YoY (vs. +34% YoY). Tier 2 city weekly secondary un\n\n[... middle omitted ...]\n\nperty Co Ltd (0123.HK)</td><td>O (09/27/2024)</td><td>HK$4.36</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R021",
    "title": "Bernstein：数据中心互联的“网络效应”才是真正的护城河",
    "digest": "[wechat_article.md]\n# Bernstein：数据中心互联的“网络效应”才是真正的护城河\n\n市场对数据中心行业的关注，多数时候停留在“电力够不够”和“机柜租金涨不涨”这两个维度。但一份来自Bernstein的最新深度报告，提出了一个被严重低估的判断：在AI时代，真正决定一家数据中心运营商长期价值的，不是它拥有多少兆瓦的电力容量，而是它能在多大程度上把物理空间转化为一个“网络枢纽”——也就是互联能力。\n\n这份报告的核心结论相当直接：互联业务（Interconnection）是一个毛利率高达70%-90%、客户粘性极强、且具有“网络效应”的利润层。而在这个赛道里，Equinix（EQIX）的领先优势比市场普遍认知的还要大，其护城河不仅深厚，而且正在被AI需求持续加固。这不仅仅是一份关于某家公司的研报，它实际上提供了一个重新评估整个数据中心资产定价逻辑的新框架。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 互联不是增值服务，而是数据中心从“仓库”变成“枢纽”的关键\n\n理解这份报告的价值，首先需要跳出传统认知。很长一段时间里，数据中心被视为“数字世界的仓库”——企业租用空间和电力，放置自己的服务器。互联（cross-connects）只是这个仓库里的一个附加功能，用于连接不同网络，避免流量经过公共互联网，以降低延迟、提升安全性。\n\n但Bernstein指出，这种理解已经过时。互联正在从“购买数据中心的考虑因素”演变为“数据中心自身的一种高利润产品”。其商业逻辑非常清晰：一根物理或虚拟的交叉连接线，对运营商来说成本极低，但一旦客户部署了生产流量，这根线就变得极度“粘性”，几乎不可能被替换。更重要的是，当同一个数据中心园区内聚集的网络提供商越多，每一根新增的连接线的价值就越高——这是一个典型的“网络效应”。\n\n这意味着，那些成功从“卖电力和空间\n\n[... middle omitted ...]\n\n中的完整图表和更详细的数据拆解。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n数据中心互联：一张真实的网络效应网\n\n数据中心互联，不只是“拉根线”\n\n最近某外资投行出了一份深度研报，把数据中心互联（Interconnection）这个细分赛道拆得非常透。我挖了几个核心观点，分享给大家。\n\n1/ 什么是数据中心互联？\n简单说，就是让不同网络在数据中心内部直接“握手”，数据不经过公共互联网。好处很直接：成本更低、延迟更低、安全性更高。\n\n2/ 为什么说它是个好生意？\n- 毛利率高达70-90%，是典型的高利润业务\n- 客户粘性极强，一旦接入就很难迁移\n- 随着园区入驻率提升，连接价值会指数级增长——真正的网络效应\n\n3/ AI时代的新故事\n以前互联只是企业选数据中心的一个参考因素，现在成了关键决策点。数据越来越重、模型越来越大、工作负载对延迟越来越敏感...互联能力正在成为数据中心的核心竞争力。\n\n4/ 谁在领跑？\n研报搭建了一个覆盖645个全球关键设施的数据库，记录超过21,000条互联连接。结论很明确：\n- Equinix（EQIX）遥遥领先：222个设施，平均每站58个互联伙伴，支撑51.3万条创收连接\n- CoreSite（AMT旗下）排第二：29个设施，平均每站46个伙伴\n- D\n\n[... middle omitted ...]\n\ning the traffic off of the public internet. Players do this to minimize costs, lower latency, and increase security. It's an \\~\\$8B market, but measurement has always been a bit wishy-washy...\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R022",
    "title": "DB：五月社融回暖但需求根基未稳，银行股的选股逻辑正在从规模转向定价权",
    "digest": "[wechat_article.md]\n# DB：五月社融回暖但需求根基未稳，银行股的选股逻辑正在从规模转向定价权\n\n五月的金融数据，像一杯温水——比四月的冰水好一些，但远谈不上滚烫。DB最新发布的研报显示，五月新增社融和人民币贷款分别录得2.0万亿和5200亿，较四月的低点有所回升，也略高于市场一致预期。但存量社融和贷款同比增速分别放缓至7.7%和5.5%，双双触及历史新低。\n\n这份数据最值得关注的判断不是“回暖”本身，而是回暖的结构揭示了什么：政府债券仍然是社融的绝对主力，企业中长期贷款连续为负，居民贷款延续收缩。换句话说，金融体系正在靠财政和票据“撑场子”，真实的实体融资意愿并未修复。对银行投资者而言，这意味着过去依赖规模扩张的盈利模式正在被挑战，真正需要评估的变量，不再是信贷增速，而是银行在弱需求环境中能否将有限的信贷资源转化为定价权和资产质量优势。\n\nDB在报告中明确表示，偏好具有较大企业业务敞口、经营韧性较强、股息率合理的大型银行，其首选为建设银行H股和中国银行H股。这个判断背后，是对银行股选股逻辑的一次重新定义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 社融回暖只是表象，三个结构性信号说明需求依然疲弱\n\n五月社融2.0万亿，看似从四月6250亿的“地量”中反弹，但同比去年五月仍少增约3000亿。拆开来看，有三个信号值得深究。\n\n第一，政府债券发行放缓。五月政府债净融资1.2万亿，低于四月的1.5万亿，说明财政发力的节奏并未加速。在社融构成中，政府债仍是最大单一贡献项，但其增速放缓意味着，如果没有更积极的财政扩张，后续社融的支撑力可能进一步减弱。\n\n第二，企业中长期贷款继续为负。五月企业中长期贷款录得-200亿，虽然比四月的-2000亿有所收窄，但连续为负的态势表明，企业用于固定资产投资的中长期融资需求依然疲弱。这不是季节性波动，而是\n\n[... middle omitted ...]\n\n会在社群中持续追踪这些关键变量，欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月社融回暖，但别急着乐观\n\n社融边际改善，但需求仍弱\n\n5月社融和信贷数据出来了，整体比4月好一些，但别急着下结论。\n\n社融2.0万亿，环比4月的6250亿明显回升，但同比去年5月的2.3万亿还是少。说明实体经济融资需求整体偏弱，只有企业债和股权融资同比在增长。\n\n**几个关键点拆解👇**\n\n**1/ 政府债仍是主力，但节奏放缓**\n5月政府债发行1.2万亿，比4月的1.5万亿少了。虽然还是社融最大贡献项，但财政支持力度边际减弱。\n\n**2/ 信贷：企业端分化明显**\n新增人民币贷款5200亿，环比4月的-100亿终于转正了，但同比去年5月的6200亿还是弱。\n- 企业短贷+1000亿，票据融资持续支撑（+5570亿）\n- 但企业中长贷仍为负（-200亿），说明实体投资意愿不强\n- 居民贷款延续负增长（-1410亿），消费和房贷需求依然谨慎\n\n**3/ 存款结构在变化**\n新增存款1.8万亿，主要靠非银金融机构存款（+1.1万亿）和财政存款（+7100亿）拉动。居民和企业存款都在减少，说明资金在往理财和资本市场迁移。\n\n**4/ M1和M2增速**\nM1增速5.5%（前值5.0%），M2增速8.6%（前值8\n\n[... middle omitted ...]\n\nrical lows.\n\nTSF in May was RMB2.0tn, rebounding from RMB625bn in April but remaining below RMB2.3tn in May last year. This suggests that real-economy financing demand remains weak across most\n\n[... middle omitted ...]\n\nk, NY 10019</td><td>Tower,</td><td></td></tr><tr><td>Tel: (44) 20 7545 8000</td><td>Tel: (1) 212 250 2500</td><td>Singapore 048583</td><td></td></tr><tr><td></td><td></td><td>Tel: +65 6423 8001</td><td></td></tr></table>"
  },
  {
    "id": "R023",
    "title": "DB：市场真正低估的不是风险，而是结构性资金洪流对资产定价的重塑",
    "digest": "[wechat_article.md]\n# DB：市场真正低估的不是风险，而是结构性资金洪流对资产定价的重塑\n\n当大多数市场参与者还在争论利率走势与信用周期时，一份来自DB证券化研究团队的2026年中展望报告提出了一个更根本的判断：当前证券化市场的核心定价逻辑，已经从“信用风险定价”转向了“需求冲击定价”。\n\n这份报告的核心洞察是：美国证券化市场正在经历一场由结构性资金流入驱动的定价重估。2026年全年证券化发行总量预计首次突破1万亿美元，但净供给仅为2700亿美元。与此同时，仅固定年金和IG债券基金两个渠道，就有约5000亿美元的资金涌入信用市场。供给侧的克制与需求侧的爆发，正在改写几乎所有资产类别的定价方程。\n\n这不是一个关于周期拐点的判断，而是一个关于市场结构永久性变化的判断。理解这一点，比预测下一次降息时点重要得多。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 1万亿美元发行量背后，真正的故事是净供给只有2700亿\n\n粗看2026年证券化市场的发行数据，很容易得出“供给过剩”的结论。DB预测全年总发行量将达到1万亿美元，创历史新高。但报告真正有价值的数据点，藏在净供给这个数字里。\n\n全年净供给预计仅为2700亿美元。这意味着，超过70%的新发行债券，实际上只是在替换到期或提前偿还的存量债券。市场的“净吸水效应”远比表面看起来温和。\n\n以非代理RMBS为例，全年发行量预计达到2150亿美元，但考虑到1350亿美元的预期偿还，净供给只有800亿美元。ABS的情况类似，3600亿发行量对应3050亿偿还，净供给仅550亿。CLO的净供给相对较高，但绝对规模也仅为900亿美元。\n\n这个结构意味着什么？对于投资者而言，新券的稀缺性远比发行量数字所暗示的要高。在需求端持续膨胀的背景下，这种供给结构天然形成了对利差的压制。报告明确判断，AAA级证券化利差将\n\n[... middle omitted ...]\n\n键图表和数据表格，并持续跟踪这些判断在后续市场中的验证情况。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n2026年资产证券化，谁是最大买家？\n\n需求激增，供给有限\n\n某外资投行预测，2026年结构化信用产品总发行量将首破1万亿美元，但净供给仅2700亿美元。背后是需求端两个大买家在疯狂扫货。\n\n1/ 保险公司：一年买走1万亿美元？\n- 2025年保险持有信用类证券化资产已超1万亿美元\n- 其中CLO 3110亿、非机构RMBS 1860亿、非机构CMBS 2000亿\n- 传统ABS只是冰山一角，还包括数据中心、飞机租赁、音乐版权等另类ABS\n- 背后驱动力：年金销售预计达3000亿美元，保险公司需要高收益资产兑付5.5%的年金利率\n\n2/ 婴儿潮一代：等待十年的配置窗口\n- 60岁以上人口8400万，控制60%-70%的金融财富\n- 住房拥有率超75%，过去40年房产增值5.5倍，标普涨70倍\n- 但过去20年10年期国债平均仅2.9%，现在4.5%+，终于等到配置固收的时机\n- 预计未来十年将释放2-4万亿美元的固收需求\n\n3/ 银行：Basel III新规让银行重新入场\n- 优先级风险权重下限从20%降至15%\n- P因子维持0.5不变（此前提议1.0会大幅提高资本占用）\n- 银行过去几年持续净卖出，现在政\n\n[... middle omitted ...]\n\nization Market Databank.xlsx\n\n## Securitized Mid-Year Outlook Demand-surge pricing\n\nEd Reardon, Managing Director\nRupesh Shrivastav, Research Associate\n\n## Big Pic: Demand surge pricing\n\nDB Ec\n\n[... middle omitted ...]\n\ns of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.\n\nCopyright © 2026 DB AG"
  },
  {
    "id": "R024",
    "title": "摩根斯坦利：人形机器人市场真正被低估的不是需求，而是供应链的再定价",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：人形机器人市场真正被低估的不是需求，而是供应链的再定价\n\n这份报告的发布时间是2026年6月，但它的判断框架值得今天就读懂。\n\n摩根斯坦利亚太研究团队在最新的《Asia Summer School: Asia Robotics and Humanoids》中给出了一个极其明确的预测：到2050年，全球人形机器人市场规模将达到7.5万亿美元，保有量超过10亿台。这个数字本身已经足够震撼，但真正值得产业决策者和投资者关注的，不是终局数字有多大，而是这个市场正在以什么样的节奏、沿着什么样的路径、在哪些环节率先形成真实的经济性。\n\n报告的核心判断可以提炼为一句话：人形机器人正在从“技术可行性验证”阶段，进入“小规模商业化”阶段。2026年就是这个转折点。而这一转折，将驱动整个供应链——从精密零部件到边缘计算芯片——出现一次前所未有的价值重估。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 商业化不是“即将到来”，而是“已经启动”，但信号藏在供应链里\n\n摩根斯坦利明确判断，小规模商业化将在2026年开始。这不是一个模糊的展望。报告给出的证据链条是清晰的。\n\n从资本市场的活动来看，2026年前四个月全球人形机器人领域的风险投资总额已经超过了2025年全年。多家初创公司在这一期间跻身独角兽行列：美国的Figure估值达到390亿美元，德国的Neura Robotics估值70亿美元，中国的银河通用、星海图、星动纪元等也相继突破10亿美元估值门槛。更值得注意的是，多家公司已经提交了IPO申请——Unitree、Deep Robotics、乐聚机器人都在列。\n\n这意味着什么？资本市场的加速不是终点信号，而是起点信号。当一家行业还在VC/PE阶段就出现如此密集的IPO准备，说明产业资本和金融资本已经形成共识：商业化窗\n\n[... middle omitted ...]\n\n解报告中的关键图表和隐含假设，并持续跟踪这个领域的最新变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n# 人形机器人：7.5万亿美金的未来\n\n**7.5万亿市场，今年启动**\n\n某外资投行最新研报给出一个大胆预测：到2050年，全球人形机器人市场规模将达到7.5万亿美元。更关键的是，今年就能看到小规模商业化落地。\n\n**为什么是人形？**\n\n1️⃣ **人形 vs 专用机器人**\n专用机器人擅长重复性简单任务，但遇到需要精细操作或复杂判断的场景就吃力了。人形机器人的优势在于：不需要改造现有工作环境，能直接替代人类完成复杂任务。\n\n2️⃣ **三个核心瓶颈**\n- 模型：VLA还是World Model？路径还没统一，通用能力有限\n- 数据：不像互联网文本那样取之不尽，机器人训练数据又贵又稀缺\n- 硬件：成本、性能和量产能力都还在爬坡\n\n3️⃣ **资本加速**\n2026年前4个月，全球人形机器人VC融资已经超过2025年全年。中美德三国已诞生多个独角兽，部分企业已启动IPO。\n\n**产业链机会在哪？**\n\n到2040年，核心零部件市场总规模预计达7800亿美元：\n- 电机：2073亿\n- 边缘计算：1233亿\n- 减速器：1370亿\n- 摄像头：316亿\n\n**应用场景已清晰**\n\n工业场景（搬运、质检、装配\n\n[... middle omitted ...]\n\ns Dominance in Global Manufacturing\n\nMS ASIA LIMITED+\n\n## Sheng Zhong\n\nEquity Analyst\n\nSheng.Zhong@morganstanley.com +852 2239-7821\n\nMS & CO. INTERNATIONAL PLC, SEOUL BRANCH+\n\n## Young Suk Shi\n\n[... middle omitted ...]\n\nv Co. Ltd. (064960.KS)</td><td>E (05/01/2026)</td><td>W30,700</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R025",
    "title": "NOM：消费数据跌破疫后低点，市场正在低估“无政策刺激”下的结构性分化",
    "digest": "[wechat_article.md]\n# NOM：消费数据跌破疫后低点，市场正在低估“无政策刺激”下的结构性分化\n\n2026年5月的社零数据，给所有还在观望消费复苏节奏的人一记明确的警钟。根据国家统计局6月16日公布的数据，中国社会消费品零售总额在5月录得同比下跌0.6%，这是自2022年底中国经济刚走出疫情封锁以来，首次出现月度同比负增长。这一数字不仅远低于市场预期的微增0.1%，更打破了此前关于“消费正在磨底”的温和叙事。\n\nNOM这份最新研报的核心判断是：消费疲软正在从个别品类扩散为系统性现象，而市场此前对“房地产回暖带动财富效应”和“AI行情支撑消费信心”的期待，均未在数据中得到验证。更值得关注的是，报告明确指出，在没有实质性需求侧政策刺激的背景下，消费情绪在短期内难以逆转。\n\n但这篇报告的价值不在于确认“消费不好”这一已知事实，而在于它提供了一个在总量下行中寻找结构性机会的分析框架。当大多数公司面临收入增长放缓的压力时，哪些企业能够凭借清晰的战略、可见的利润率趋势和有吸引力的估值，成为穿越周期的少数赢家？NOM给出了两个明确的标的，但其背后的选股逻辑，值得所有产业决策者认真拆解。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 5月社零数据的结构性恶化，比总量数字更值得警惕\n\n总量数据是-0.6%，但真正令人担忧的是内部结构的普遍走弱。限额以上企业商品零售总额同比下跌5.2%，成为拖累整体社零的主要力量。NOM在报告中指出，虽然部分下滑可以归因于高基数效应和5月不利天气条件——气温偏高、降雨日数增多限制了消费者活动——但这不足以解释如此广泛的疲软。\n\n分项数据揭示了几个关键信号：\n\n首先，餐饮服务收入增速从4月的2.2%进一步放缓至5月的0.6%，几乎逼近零增长。餐饮作为消费景气度的“温度计”，其持续走弱说明居民外出消费意愿正在快速收缩。\n\n[... middle omitted ...]\n\n关心产业逻辑的读者一起，把报告的洞察转化为可执行的观察框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n消费数据转弱，五月社零首次负增长\n\n消费真的冷了吗？\n\n5月社零同比-0.6%，是2022年底以来首次转负，也低于市场预期的+0.1%。\n\n1/ 餐饮增速从4月的+2.2%放缓至+0.6%，商品零售从-0.1%进一步下滑至-0.7%。除了饮料（+6.1%）、服装（+3.8%）、办公用品（-1.5%但环比改善）外，大部分品类都在走弱。\n\n2/ 家电（-15.6%）和建材（-13.6%）依然深陷负增长，没有回暖信号。限额以上企业商品零售同比-5.2%，是主要拖累项。\n\n3/ 某外资投行认为，需求端缺乏消费刺激政策、楼市回暖对财富效应拉动有限、股市上涨对消费支撑不足，短期消费情绪难改善。\n\n4/ 在这种环境下，他们偏好有清晰战略、利润率趋势可见、估值有吸引力的公司。比如运动服饰的安踏，以及老铺黄金——如果金价在更宽松的地缘环境下企稳，它有望维持较稳定的利润率并改善经营杠杆。\n\n欢迎一起聊聊，你觉得消费什么时候能企稳？\n\n#学习笔记\n\n[source_mineru.md]\n## China consumer\n\nEQUITY: CONSUMER RELATED\n\n## Retail sales momentum weake\n\n[... middle omitted ...]\n\no missed the Wind consensus of a mild $0.1\\%$ y-y increase. Total retail sales of merchandise by enterprises above designated size was the major drag to the total social retail sales reading i\n\n[... middle omitted ...]\n\nable upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R026",
    "title": "NOM：电商渗透率回升背后，消费结构的分化比总量更值得关注",
    "digest": "[wechat_article.md]\n# NOM：电商渗透率回升背后，消费结构的分化比总量更值得关注\n\n5月中国电商零售数据公布后，市场焦点大多落在“增速小幅回暖”这个数字上。NOM在最新发布的Quick Note中捕捉到一个更值得关注的信号：电商渗透率同比回升1.0个百分点至31.6%，但各品类增长轨迹的分化程度，远超总量数据所能表达的范围。\n\n这不是一个简单的“消费复苏”或“消费降级”的故事。NOM的数据拆解显示，5月电商销售同比增长2.6%，较4月的0.2%明显提速，但同期社会消费品零售总额（剔除汽车）增速却从1.8%回落至1.1%。线上与线下、必需品与可选品、食品饮料与家电手机——不同维度的增长曲线正在朝着相反方向移动。\n\n对于关注中国消费市场的投资者而言，真正的问题不是“电商是否还能增长”，而是“增长的结构性驱动因素正在发生怎样的根本性转变”。这份报告提供的数据线索，指向一个比表面增速更复杂的判断：消费者在品类间的支出再分配，正在重塑电商平台的竞争逻辑。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 必需品与可选品的增速裂口，揭示的不是消费意愿而是消费优先级\n\nNOM的数据显示，5月线上食品饮料销售在1-5月累计同比增长15.5%，与4月的15.6%几乎持平。这是一个值得注意的稳定性——在整体零售增速放缓的背景下，食品饮料作为刚需品类，其线上增长几乎没有受到宏观经济波动的侵蚀。\n\n对比之下，可选消费品的表现出现了明显分化。线上服装销售累计增速从4月的6.8%微升至7.2%，但化妆品增速从4.7%回落至2.5%，家电销售更是录得15.6%的同比下滑。同一份数据中，线下渠道的饮料销售增速反而从3.6%加速至6.1%。\n\n这些数字合在一起意味着什么？消费者并没有停止花钱，而是在重新排列支出优先级。食品饮料和服装等“日常必需的可选品”依然获得稳定的\n\n[... middle omitted ...]\n\n的解读框架，以及如何将这些月度数据转化为持续跟踪的投资逻辑。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月电商：增速回升，分化明显\n\n**电商增速回暖**\n\n**线上渗透率同比提升1个百分点**\n\n5月社零数据出来了，电商大盘有点意思。\n\n整体零售增速放缓至1.1%（4月1.8%），但电商却逆势加速——线上商品销售同比增2.6%，比4月的0.2%明显回暖。渗透率也来到31.6%，同比+1.0pp。\n\n1/ 线上吃吃喝喝依然稳\n前5个月，线上食品饮料累计增15.5%，和4月（15.6%）基本持平。这赛道韧性真强，大家该囤还是囤。\n\n2/ 服装线上在修复\n线上服装累计增速从4月的6.8%微升至7.2%，虽然不快，但趋势向上。线下服装零售也差不多，5月同比+3.8%，和4月持平。\n\n3/ 家电拖后腿，手机有点软\n家电零售同比-15.6%，和4月（-15.1%）差不多，主要是高基数+补贴退坡。手机仅+0.7%，4月还有6.2%，原因是芯片涨价推高售价、抑制需求。\n\n4/ 美妆降温明显\n化妆品零售增速从4月的4.7%放缓到2.5%，线下渠道压力更大。\n\n整体看，5月电商是“吃穿稳、用分化”——食品饮料和服装扛大旗，家电手机拖后腿。这个节奏你感受到了吗？\n\n#学习笔记\n\n[source_mineru.md]\n## Chi\n\n[... middle omitted ...]\n\no $31.6\\%$ in May.\n\nBased on NBS data, China's online food and beverage sales rose $15.5\\%$ y-y in 5M26, on par with the $15.6\\%$ y-y growth in 4M26. Online apparel sales recorded a $7.2\\%$ y-\n\n[... middle omitted ...]\n\nable upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R027",
    "title": "Citi：进口车市场正在经历的不是周期性波动，而是品牌溢价能力的根本性分化",
    "digest": "[wechat_article.md]\n# Citi：进口车市场正在经历的不是周期性波动，而是品牌溢价能力的根本性分化\n\n中国进口车市场正在经历一场超出多数人预期的结构性调整。Citi最新发布的基于ThinkerCar保险数据的研报显示，2026年5月，中国进口乘用车零售销量同比下滑38%，环比零增长，当月销量仅为2.93万辆。前五个月累计销量16.48万辆，同比下跌28%。\n\n这些数字本身已经足够引人注目。但比总量下滑更值得关注的，是不同品牌之间的表现差异——这种差异指向一个更深层的判断：进口车市场正在从“品牌驱动”向“产品力与价格匹配度驱动”切换，而大多数传统豪华品牌尚未完成这一转变。\n\nCiti这份报告的价值不在于它披露了销量数字——这些数据市场已有感知——而在于它提供了一个清晰的、可横向比较的品牌表现图谱。透过这张图谱，我们可以识别出哪些品牌正在失去议价权，哪些品牌尚能维持基本面，以及更重要的是，哪些结构性变量正在重塑这个市场的竞争逻辑。\n\n以下是我们从这份报告中提炼出的五个核心洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 雷克萨斯和奔驰的相对韧性说明，品牌护城河正在从“豪华认知”转向“供需纪律”\n\n在几乎所有品牌都录得两位数下滑的背景下，雷克萨斯和奔驰的表现值得单独拿出来讨论。雷克萨斯5月销量10,516辆，同比下滑38%，但环比持平；前五个月累计销量60,123辆，同比下滑19%。奔驰5月销量6,271辆，同比下滑19%，环比增长3%；前五个月累计34,366辆，同比下滑25%。\n\n从绝对数字看，这两个品牌同样身处下行通道。但从相对位置看，它们明显优于同行。宝马5月销量3,356辆，同比下滑41%；保时捷2,582辆，同比下滑32%；奥迪947辆，同比下滑66%；路虎2,035辆，同比下滑45%。\n\n这里的核心差异不在于品牌知名度—\n\n[... middle omitted ...]\n\n些在公开渠道不容易拿到，但对于判断行业拐点有直接的参考意义。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n进口车5月销量跌38%，谁还在逆势增长？\n\n进口车市场持续降温\n\n5月进口车零售数据出炉，同比跌38%，环比持平，销量仅2.93万辆。前5个月累计16.48万辆，同比下滑28%。整体趋势很清晰：进口车市场还在缩量调整中。\n\n1️⃣ 雷克萨斯：第一但也在跌\n销量10516辆，同比-38%，环比0%。虽然稳坐进口品牌第一，但跌幅和行业整体一致，没有跑赢大盘。\n\n2️⃣ 保时捷：环比反弹明显\n销量2582辆，同比-32%，环比+27%。5月环比增长最亮眼，可能是新款到店拉动了一波需求。\n\n3️⃣ 大众：逆势翻红\n销量511辆，同比+84%，环比+86%。虽然绝对量小，但两位数的正增长在全员下跌中很突出。\n\n4️⃣ 奥迪、沃尔沃：跌幅最深\n奥迪947辆，同比-66%；沃尔沃455辆，同比-66%。这两个品牌进口线压力最大。\n\n5️⃣ 宝马、路虎：跌幅超四成\n宝马3356辆，同比-41%；路虎2035辆，同比-45%。豪华品牌进口车同样承压。\n\n从5月vs前5月散点图看：大众是唯一双维度正增长品牌，雷克萨斯、奔驰跌幅相对温和。奥迪、沃尔沃在两个时间维度都垫底。\n\n进口车市场整体还在寻底，但品牌分化明显。大众的逆势增长值\n\n[... middle omitted ...]\n\ns</td><td>YoY</td></tr><tr><td>Lexus</td><td>10,516</td><td>-38%</td><td>0%</td><td>60,123</td><td>-19%</td></tr><tr><td>Mercedes-Benz</td><td>6,271</td><td>-19%</td><td>3%</td><td>34,366</td>\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R028",
    "title": "摩根斯坦利：市场对日本汽车股的悲观定价，忽略了三个尚未被充分理解的变量",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：市场对日本汽车股的悲观定价，忽略了三个尚未被充分理解的变量\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 市场情绪已经过度集中在中东地缘与中国对手身上\n\n2026年6月，摩根斯坦利日本汽车团队在纽约和旧金山与机构投资者进行了一轮密集会议。这份调研反馈报告透露出的信号，与当前股价反映的市场共识之间存在一个值得注意的偏差：绝大多数投资者对日本汽车股的判断框架，几乎完全被两个因素主导——中东局势对供应链的冲击，以及中国OEM崛起对市场份额的侵蚀。但这份报告暗示，真正影响个股定价差异的变量，可能并不在这两个已经被充分讨论的叙事里。\n\n当市场对某个行业的担忧高度趋同时，往往意味着定价已经部分吸收了这些风险。而那些尚未被广泛定价的结构性因素，才是超额收益或风险暴露的真正来源。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 1. 丰田的盈利指引被误解为保守，但市场低估了HEV带来的结构性利润弹性\n\n报告中最值得关注的细节之一，是摩根斯坦利团队的一个判断：市场对丰田F3/27营业利润指引的保守性质“理解并不充分”。这句话的潜台词是，丰田给出的指引数字很可能远低于公司内部的实际预期。\n\n为什么丰田会选择给出一个明显偏保守的指引？这背后可能涉及日本企业一贯的“低预期管理”策略，但也可能反映了管理层对2026-2027年期间多个不确定性的主动对冲。然而，真正让这份报告值得深读的，是投资者对HEV（混合动力车型）盈利贡献的关注度。在纯电动车渗透率增速放缓、充电基础设施瓶颈尚未完全解决的背景下，丰田在HEV领域的技术积累和规模效应，可能正在转化为一种被市场低估的利润缓冲垫。\n\n这意味着：如果中东局势出现任何缓解信号，丰田的盈利修正幅度可能比市场预期的更大。而如果局势持续恶化，HEV较高的利\n\n[... middle omitted ...]\n\n断，以及那些在调研反馈中一闪而过但可能被市场忽略的细节信号。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球汽车行业，投资者在观望什么？\n\n📊 投研视角看日本车企\n\n最近某外资投行发布了日本汽车行业的调研纪要，分享了6月初与美国机构投资者的交流情况。整体来看，市场情绪偏谨慎，但也有人在等一个反转机会。\n\n**1/ 行业整体：中东局势是最大变量**\n多数投资者对汽车行业保持观望，核心担忧两点：\n- 供应链限制和原材料涨价（受中东局势影响）\n- 中国车企崛起，日本车企份额承压\n另外，2026年7月USMCA（美墨加协定）审查也是热门话题。\n\n**2/ 个股看点：各有各的焦虑**\n- **丰田**：市场对F3/27财年营业利润指引的保守性理解不足，HEV（混动）车型贡献和新总裁上任后变化是关注焦点。\n- **本田**：储能系统（ESS）业务被问得最多，两轮车增长潜力受关注，但EV（电动车）占比上升可能拉低利润率。\n- **日产**：固定成本削减获认可，但汽车业务扭亏和正向自由现金流前景仍存疑。\n- **斯巴鲁**：除股东回报调整外，长期盈利展望（降本+产品线扩充）是重点。\n- **马自达**：新CX-5 SUV换代带来的销售增长预期，因中东局势降温。\n- **铃木**：印度汽车销售趋势、5月涨价和油价前景是核心，但中\n\n[... middle omitted ...]\n\nAutos industry as a whole: Our impression was that most investors have taken a cautious stance on the industry with the Middle East situation ongoing. Some – albeit not many – have already a\n\n[... middle omitted ...]\n\naha Motor (7272.T)</td><td>E (04/17/2025)</td><td>¥1,232</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS MUFG"
  },
  {
    "id": "R029",
    "title": "摩根斯坦利：能源基础设施的定价权正在从宏观叙事转向微观资产",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：能源基础设施的定价权正在从宏观叙事转向微观资产\n\n这份摩根斯坦利本周发布的北美中游与可再生能源基础设施周报，提供了一组看似孤立、实则紧密关联的信号。报告覆盖了从霍尔木兹海峡的地缘政治博弈到Permian盆地管道扩容的微观工程进展，从中国原油进口的急剧收缩到AI数据中心项目的搁浅。将这些信号放在一起，一个更值得关注的判断浮现出来：当前市场对能源基础设施资产的定价，正在从依赖宏观地缘叙事转向聚焦微观资产的运营现实与合约结构。这一转变意味着，过去两年基于“能源安全”和“AI电力需求”的板块普涨逻辑，正在被更精细的资产选择逻辑所取代。\n\n为什么现在重要？因为市场正在经历一个“压力测试”窗口。霍尔木兹海峡可能重新开放的前景正在压低原油价格，而AI相关股票的动量因子正在经历今年以来最剧烈的回撤。在这两个负面因素同时作用下，中游能源基础设施资产的表现分化将比以往任何时候都更能揭示哪些公司真正拥有结构性护城河，哪些只是搭上了主题的便车。\n\n这份报告最值得细读的地方在于，它没有停留在宏观判断，而是提供了多个具体资产层面的数据点——从Waha天然气价格的反弹驱动因素，到单个管道项目的在役时间线，再到AI数据中心项目的客户承诺缺失。这些微观证据，才是判断未来6-12个月能源基础设施投资方向的关键。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 霍尔木兹海峡的“投降式”重开并不会终结中游资产的吸引力，反而会加速资本向拥有长期合约的资产集中\n\n报告开篇就抛出了一个大胆的判断：如果美伊达成协议重新开放霍尔木兹海峡，这将被市场视为一个“投降事件”，促使资本从避险资产重新轮动回能源板块。这个判断看似矛盾——地缘风险溢价消失，为什么反而利好能源？但仔细推敲，逻辑是成立的。\n\n关键前提在于时机与不确定性。报告指出，交通流量正常化和全\n\n[... middle omitted ...]\n\n的影响、AI数据中心项目的真实落地节奏——进行更深入的交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n能源基建本周几个关键信号\n\n能源基建观察\n\n输油气管网与AI数据中心的交叉点\n\n本周研报有几个值得关注的点，拆开聊聊👇\n\n**1/ 霍尔木兹海峡的“反转”逻辑**\n如果美伊达成协议重新开放海峡，研报认为这可能成为资金重新回流能源板块的“转折点”。关键变量是：航道恢复正常的时间、全球库存补充的节奏。这个逻辑链条值得跟踪。\n\n**2/ 天然气管道扩容落地**\nKMI的Gulf Coast Express管道扩容已投运（研报引用Hart Energy数据），这是近期Waha地区天然气价格反弹的主要推手。另外两条新管道（WhiteWater的Blackcomb和ET的Hugh Brinson）未来几个月也将投产，但新产能可能很快填满——这对Permian盆地的天然气处理商来说是量上的利好。\n\n**3/ AI/数据中心股票回调拖累了天然气基建**\n近期动量因子出现年内最大回撤，AI/电力相关股票回调，连带天然气基建股（如WMB、DTM、KMI）走弱。研报认为这个超跌有些过度，因为下半年仍可能有新的项目公告，背后的支撑是超大规模云厂商在AI上的资本开支加速（图表显示2026-2027年预计持续增长）。\n\n**4/ 油价为\n\n[... middle omitted ...]\n\ns a possibility post-Coterra deal close.  \nPresident Donald Trump accused New York Gov. Kathy Hochul of breaking an agreement to support WMB's Constitution Pipeline project.  \nA federal court \n\n[... middle omitted ...]\n\nrastructure, LP (XIFR.N)</td><td>U (02/03/2025)</td><td>$11.66</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.\n\n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R030",
    "title": "NOM：中国焦煤供应冲击的真正影响，不在中国，而在印度钢厂的利润结构",
    "digest": "[wechat_article.md]\n# NOM：中国焦煤供应冲击的真正影响，不在中国，而在印度钢厂的利润结构\n\n市场正在错误地解读近期山西煤矿事故的后续影响。多数投资者关注的是中国国内焦煤价格是否还会继续上涨，或者澳大利亚海运煤出口能否填补缺口。但NOM这份最新报告揭示了一个更值得注意的判断：**真正需要重新定价的，不是中国焦煤的短期供应，而是印度钢铁企业的利润韧性。**\n\n5月26日山西煤矿事故发生后，中国有137座焦煤矿被暂停生产。截至6月11日，虽然77座矿井已经复产，但恢复进程并不均衡——部分矿井在重启几天后再次停产。国内焦煤现货价格已上涨超过10%至每吨270美元。这些信息已被市场消化。但报告真正有价值的部分，在于它如何拆解这一事件对不同市场参与者的差异化影响。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮供应冲击暴露了中国煤炭监管的深层模式，而非一次性事件\n\n事故后复产速度看起来很快——56%的停产的矿井在两周内恢复。但NOM的数据显示，恢复路径并非线性。6月11日的数据甚至显示，复产矿井数量从81座回落至77座，同时停产矿井数从56座回升至60座。这不是一次性的生产中断，而是一个反复震荡的过程。\n\n更关键的是，当局已将安全检查扩展至主要产煤区，重点打击非法和隐蔽采掘巷道。这意味着监管压力不会随着事故热度消退而解除。NOM将这一模式称为“监管风险叙事”——中国煤炭供应的核心变量正在从产能本身转向政策执行力度。\n\n对中国市场而言，这意味着国内焦煤价格很难迅速回到事故前水平。每吨270美元的现货价格，可能不是短期情绪溢价，而是市场在为一种新的供应常态定价。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 澳大利亚出口激增的背后，是结构性替代正在发生，但规模仍有上限\n\n5月澳大利亚对中国焦煤出\n\n[... middle omitted ...]\n\n解报告的完整逻辑、对比不同机构的假设差异、跟踪后续数据变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n山西焦煤矿难后的供应恢复，比想象中慢\n\n供应恢复不均\n\n投行研报显示，5月底山西矿难后，停产焦煤矿逐步复产。截至6月11日，137座停产矿中77座已恢复（约56%）。但恢复不均，部分矿复产几天后因安全检查再次停工，且检查已扩大至主要矿区，尤其是非法隐蔽巷道。\n\n国内焦煤价格已涨超10%\n\n尽管部分复产，国内焦煤现货价已升至270美元/吨，较事故前涨超10%。市场定价的不仅是单一事件，而是国内钢铁原料供应整体收紧的预期。\n\n澳洲出口中国激增114%\n\n5月澳洲焦煤对华出口环比激增114%（同比+77%），达148万吨，占中国进口份额从7%升至11%。研报认为，若安全限产持续，中国可能更多转向海运煤。但蒙古和俄罗斯受物流和品质限制，难以完全替代。若国内供应恢复慢，中国对澳洲海运煤需求或推高全球焦煤价格。不过当前澳洲优质硬焦煤价格仅微涨1.5%至244美元/吨，尚稳定。\n\n印度钢企利润暂时安全\n\n传导路径是进口焦煤成本。研报测算，焦煤每涨10美元/吨，对印度综合钢企EBITDA影响约7-9美元/吨。JSW Steel和Tata Steel暴露度最高，Jindal Steel部分暴露。但中国供应逐步恢复使海运煤价趋稳\n\n[... middle omitted ...]\n\nemains uneven, with some mines reportedly suspending operations again after only a few days of resumption amid intensified safety inspections. Notably, authorities have expanded inspections ac\n\n[... middle omitted ...]\n\nisclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Financial Advisory and Securities (India) Private Limited, India. All rights reserved."
  },
  {
    "id": "R031",
    "title": "GS：市场低估了资本支出超级周期对资产定价的深远重塑",
    "digest": "[wechat_article.md]\n# GS：市场低估了资本支出超级周期对资产定价的深远重塑\n\n过去四十年，投资者习惯了低利率、低通胀、低波动和全球化带来的确定性回报。但GS在最新一期全球策略报告中提出了一个核心判断：我们正站在一个全新周期的起点，这个周期的底层逻辑与1980年代以来的“现代周期”截然不同。市场目前对AI和基础设施投资带来的资本支出浪潮有所定价，但真正被低估的，是这一资本支出超级周期将如何系统性重塑股票回报的构成、行业竞争格局以及资产定价的锚。\n\n这份报告的核心洞察在于，投资回报的驱动力正在发生根本性转移。从依赖估值扩张和多重压缩的“金融工程”时代，转向依赖盈利增长和现金流的“实业创造”时代。理解这一转变，比预测下一个季度的GDP数据或美联储的降息时点更为重要。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 过去四十年的“现代周期”已不可逆地终结，其底层驱动因素正在全面逆转\n\nGS将1982年至疫情前的时期定义为“现代周期”。这一周期的核心特征是：低通胀、低利率、低波动、全球化、低资本密集度和高利润率。这些因素共同造就了历史上最长的股票牛市，也塑造了整整一代投资经理的思维范式。\n\n但这份报告清晰地指出，支撑这一周期的所有支柱都在瓦解。从低通胀转向再通胀，从量化宽松和零利率转向更高的资金成本，从全球化转向区域化和碎片化，从低资本密集度转向大规模基础设施投资。这些不是短期的周期性波动，而是结构性转变。例如，全球军事支出占GDP的比重在经历了数十年的下降后，自2022年以来已经重新上升。企业税率在经历了长期下降后，也面临上行压力。劳动力成本在全球化退潮和人口结构变化下，其下降趋势已经逆转。\n\n这意味着，投资者不能再简单地将过去四十年的经验外推。那种“买入并持有”就能享受估值扩张和全球化红利的日子，可能已经过去了。未来的投资回报将更加依赖对\n\n[... middle omitted ...]\n\n里继续讨论，与更多志同道合的投资者一起，在变化中寻找确定性。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n别再用老眼光看市场了\n\n旧周期已结束\n新逻辑正在生效\n\n最近读到一篇某外资投行的研报，核心观点非常清晰：我们正处在一个“后现代周期”的开端，旧的赚钱逻辑正在失效。\n\n过去40年的“现代周期”靠什么？\n- 低通胀、低利率、全球化\n- 企业减税、劳动力成本下降\n- 宏观波动小，估值扩张驱动回报\n\n但后疫情时代，一切都在反转：\n1️⃣ 从通缩→再通胀\n2️⃣ 从零利率→高利率\n3️⃣ 从全球化→区域化\n4️⃣ 从资本轻→资本重\n\n最核心的变化：**资本支出超级周期来了**\n- AI革命带动私营部门投资激增\n- 能源安全和地缘政治催生公共投资\n- 供应链从效率优先转向韧性优先\n\n这意味着什么？\n- 市场回报将从“估值驱动”转向“盈利增长驱动”\n- 资产之间的收益差异会拉大，选股能力更值钱\n- 传统“买指数躺赢”的策略可能失效\n\n一个值得思考的问题：当低垂的果实都被摘完，我们准备好应对更高波动的环境了吗？\n\n#学习笔记\n\n[source_mineru.md]\nGLOBAL STRATEGY PAPER NO. 76\n\n# The Post Modern Cycle – Navigating the Capex Boom\n\n[... middle omitted ...]\n\nrvention and regionalisation. The composition of returns is likely to shift further away from valuation as a driver of returns toward EPS growth.  \n- A capex supercycle is taking hold. The AI \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R032",
    "title": "Citi：AI产业真正的分水岭不是模型能力，而是推理成本的精细化控制",
    "digest": "[wechat_article.md]\n# Citi：AI产业真正的分水岭不是模型能力，而是推理成本的精细化控制\n\n2026年6月的Research and Applied AI Summit（RAAIS）传递了一个清晰但容易被市场噪音掩盖的信号：AI行业的竞争焦点，正在从“谁拥有最大的模型”转向“谁能以最低的token成本交付可用的推理结果”。这不是一个渐进式的优化，而是一个可能重塑产业链价值分配的结构性转折。\n\nCiti在最新发布的研报中系统梳理了RAAIS 2026的核心技术趋势，并将“推理成本效率”和“递归自我改进”列为当前最值得关注的产业变量。这份报告的价值不在于罗列技术名词，而在于揭示了两个正在并行发生的深层变化：第一，前沿模型的边际收益正在递减，而推理成本的高速增长正在倒逼整个行业重新设计技术栈；第二，AI从“语言模型”向“世界模型”的跃迁，其商业化路径远比市场预期的要长，但一旦突破，其影响将远超当前任何单一应用场景。\n\n以下是我们从这份研报中提炼的五个核心洞察，以及它们对产业决策者和投资者的含义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 推理成本正在成为AI商业化的第一约束，而“降本”本身已经催生出一个新的技术层\n\nCiti研报中两个数字值得反复咀嚼。Revolut的ML工程负责人披露，其内部开发的模型路由平台通过“为任务匹配正确规模的模型”，实现了**8倍的成本节约且质量无损**。ElevenLabs的研究工程师则展示了在固定硬件上实现**70倍吞吐量提升**的技术组合，其中仅连续批处理（continuous batching）一项就贡献了15倍增益。\n\n这些数字背后是一个正在成型的产业逻辑：当模型能力达到一定阈值后，企业竞争力的核心不再是“能否调用最强模型”，而是“能否在维持质量的前提下，将推理成本压到对手无法跟进的水平”。R\n\n[... middle omitted ...]\n\n将结合更多一手资料和跨机构视角，共同推演这些趋势的演变路径。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI下一步：自进化、降成本、建世界模型\n\nAI正在自我进化\n\n最近一场AI前沿峰会，信息量很大。几个关键趋势值得关注：\n\n1️⃣ **推理成本大幅下降**\nRevolut自研路由平台，把任务从大模型分流到合适的小模型，成本降低8倍，质量不变。ElevenLabs在固定硬件上实现70倍吞吐提升——连续批处理贡献15倍，FP8量化、推测解码等技术叠加效果惊人。模型“按需分配”正在成为标配。\n\n2️⃣ **AI开始自我改进**\n去年DeepMind展示“AI平方”——AI帮助AI提升。今年更进一步：科学发现被重新定义为强化学习问题，从发现到开放发现，再到加速发现。基础设施包括支持4亿+研究任务的DiscoGen、MLGym-Bench等。Odyssey的PROWL系统更酷——用强化学习优化世界模型本身，而不仅仅是决策策略。\n\n3️⃣ **世界模型处于“GPT-2时刻”**\n世界模型商业化早期，但正在打破机器人领域的瓶颈。Odyssey认为建模世界交互比纯语言更丰富——其模型在物理基准测试中得分93。DeepMind的Genie 3能实时生成视频，适合教育和智能体训练。机器人灵巧操作已达人类水平。\n\n4️⃣ **AI\n\n[... middle omitted ...]\n\nen efficiency threaded throughout the day, as Revolut noted an “8x cost savings” from its internally developed platform routing work away from frontier models, while ElevenLabs detailed techni\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R033",
    "title": "JEF：锂电产业链的真实信号不是价格下跌，而是库存认知的分裂",
    "digest": "[wechat_article.md]\n# JEF：锂电产业链的真实信号不是价格下跌，而是库存认知的分裂\n\n这份JEF锂电产业链调研报告，覆盖了中国市场约77%的锂盐转化企业和73%的电池材料生产企业，是当前最有代表性的产业链一线感知采样。读完整份报告，最值得关注的核心判断不是价格还会跌多少——市场对此已有充分预期——而是一个正在悄然形成的结构性裂痕：上游转化企业和下游电池企业对库存水平的认知出现了方向性分歧。这种分歧，正在重塑整个锂电产业链的议价机制和利润分配格局。\n\n报告显示，转化企业认为电池厂商的库存“过低”，但电池厂商却认为自己的客户——整车厂和储能集成商——存在“适度过剩”的库存。同一组数据，两个环节读出了完全相反的结论。这意味着什么？意味着产业链的信息传导已经不再是对称的，每一环都在根据自身订单感受做出独立判断，而这些判断正在驱动截然不同的采购和备货行为。\n\n这份调研发生于一个微妙的时点。锂价在经历了2022年的狂飙和2023年的回调后，市场普遍认为底部区域已经探明，但去库存周期何时结束、需求何时真正企稳，始终缺乏高频、一手的数据支撑。JEF的这份调研，恰好填补了这一空白。它不是基于模型推演，而是基于实际负责采购和排产的一线管理者的直接反馈。\n\n以下，我们从五个层次来拆解这份调研揭示的核心信号。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 价格预期已经触底，但转化企业的悲观情绪仍在蔓延\n\n调研中一个最直接的信号是价格预期。转化企业预计未来三个月锂盐价格将出现超过10%的下跌，而电池企业的预期则温和得多，仅为个位数跌幅。值得注意的是，从2024年初至今，转化企业的价格预期曲线始终在电池企业下方，且差距在2025年下半年开始明显扩大。\n\n这意味着什么？转化企业正在承受比下游更重的价格压力。原因不难理解：转化环节产能过剩更为严重，且产品同质化程\n\n[... middle omitted ...]\n\n链最新信号做定向拆解，也会邀请有实操经验的产业人士参与讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n锂链情绪降温，信号分化\n\n锂价短期承压\n\n某外资投行最新调研了锂产业链上下游，发现信号明显分化。\n\n**1. 价格预期偏弱**\n- 锂盐加工商预期Q3价格将下跌超10%\n- 电池材料生产商预期跌幅约4%\n- 整体对价格走势偏保守\n\n**2. 订单量放缓**\n- 新订单增速在减速\n- 订单信心也在下滑\n- 加工商的订单积压指数低于50%扩张线\n\n**3. 库存观点出现分歧**\n- 加工商认为下游电池厂库存偏低\n- 但电池厂认为自己的客户库存略高\n- 上下游对库存水平的判断不一致\n\n**4. 销量预期分化**\n- 加工商对未来1个月销量预期同比负增长\n- 电池厂销量预期基本持平或小幅正增长\n- 加工环节压力更大\n\n这是典型的周期调整期，产业链不同环节的感受差异明显。你觉得锂价会在Q3触底吗？\n\n#学习笔记\n\n[source_mineru.md]\n## Lithium Value Chain Survey: Temporary Pullback, Diverging Signals\n\nOur survey of lithium converters (77% of sales in China) and batte\n\n[... middle omitted ...]\n\nb1787a52c00f1443cf6f365e05372e554bf5d93a3296d4077120.jpg)\n\n<details>\n<summary>line chart</summary>\n\n| Month    | Converter | Battery Producer |\n| -------- | --------- | ---------------- |\n| Ja\n\n[... middle omitted ...]\n\nrd\\_iapd\\_Brochure.aspx?BRCHR\\_VRSN\\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://avatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.\n\n© 2026 JEF"
  },
  {
    "id": "R034",
    "title": "Bernstein：液冷CDU的真正分化不在技术路线，而在推理与训练的两极定价",
    "digest": "[wechat_article.md]\n# Bernstein：液冷CDU的真正分化不在技术路线，而在推理与训练的两极定价\n\n当市场还在争论液冷与风冷谁将主导下一代数据中心时，一份来自Bernstein的研报揭示了一个更微妙的信号：技术路线的选择不是核心变量，真正决定CDU制造商未来估值分化的，是AI工作负载的“推理”与“训练”两极分化，以及由此引发的CDU产品分层定价。\n\n这份报告讨论的是谷歌近期发布的“Brazos”项目——一款面向开放计算项目的液冷到空气CDU参考设计。表面看，这只是又一个技术规格的公布。但Bernstein的分析指向一个更深层的判断：这不是一次技术迭代，而是一次对CDU市场结构的重新定义。它意味着市场正在被切割为两个截然不同的价格带——一个属于高溢价、高技术壁垒的训练CDU，另一个属于可标准化、可商品化的推理CDU。\n\n对于投资者而言，理解这个分化的含义，远比追踪下一个液冷技术突破更为紧迫。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 谷歌Brazos的真实意图不是竞争，而是为推理负载开辟一条低成本通道\n\n研报明确指出，Brazos并非谷歌要亲自制造的CDU产品。它是一套开放的技术规格，供Vertiv、nVent、Boyd等OCP生态成员生产。其冷却容量仅为60kW，甚至无法支撑一个Blackwell机架（需要约120kW）。从参数上看，它并不“惊艳”。\n\n但Bernstein的洞察在于：这种“不够强”恰恰是设计意图的体现。Brazos被设计为直流供电，适配已有直流基础设施的旧有数据中心。60kW的冷却能力虽然无法支持前沿训练模型，却恰好覆盖推理负载的常见功率范围。\n\n这背后有一个更宏大的逻辑：尽管训练模型需要新建高密度数据中心，但推理负载的增长速度预计在2030年前将超过训练。而推理负载的部署面临的最大瓶颈不是技术能力，而是\n\n[... middle omitted ...]\n\n中分享更多Bernstein原始报告的图表和我们的延伸分析。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n谷歌刚刚放了个“冷”大招\n\n液冷CDU，没那么吓人\n\n谷歌公布了新的液冷方案“Brazos”，但不是自己造，是给供应商的参考设计。\n\n1/ 别慌，这不是降维打击\nBrazos 是液对空（L2A）的CDU，单台只有60kW冷却能力，连一个Blackwell机柜（~120kW）都带不动。它主打的是老旧数据中心改造，用直流电，适配OCP标准——说白了就是给存量机房“续命”用的。\n\n2/ 真正的战场在推理侧\n研报推测，Brazos 瞄准的是推理（inference）场景。推理需求到2030年增速可能超过训练，但很多机房根本来不及新建。一个能快速改造、插上就能用的L2A方案，反而能卡位这个缺口。\n\n3/ 对厂商有两个隐患\n- 低端CDU可能被“卷”成标准品：Brazos 的规格不高，做起来不难，利润率大概率比高端训练CDU低。\n- 需求可能从新建转向改造：如果项目延期，标准化L2A CDU就是超大规模客户的“备胎”。\n\n但也不必过度担心——旗舰CDU的技术溢价依然存在，顶尖玩家还能靠创新守住利润。\n\n你觉得推理场景的机柜密度会稳定在60kW以下吗？欢迎一起讨论。\n\n#学习笔记\n\n[source_mineru.md]\n#\n\n[... middle omitted ...]\n\nb99fdfe73b9f77a122daa5086d10422588cc8b3.jpg)\n\nMadison Rezaei\n\n+19173448622\n\nmadison.rezaei@bernsteinsg.com\n\n## Specialist Sales\n\n![](images/9461c6306ed343985afae7d2fd63e51991e6e9c334b181623937\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R035",
    "title": "GS：日本银行股正在定价的利率路径，可能比市场意识到的更陡",
    "digest": "[wechat_article.md]\n# GS：日本银行股正在定价的利率路径，可能比市场意识到的更陡\n\n日本央行在6月议息会议上将政策利率从0.75%上调至1.0%，这本身并不令人意外。真正值得关注的信号，藏在加息之后的两个细节里：主要银行在存款利率上调中保持了与市场预期一致的存款贝塔系数，以及横滨金融集团率先披露了加息对下财年利润的正面影响。GS这份报告的核心判断是，市场对日本银行股的定价仍然偏保守——当前股价隐含的政策利率假设大约在0.75%至1.0%区间，而央行传递的加息周期延续信号，意味着这个区间需要重新校准。\n\n这不是一个关于“加息利好银行股”的简单叙事。真正的问题在于，哪些银行能够将加息转化为可持续的利润增长，以及市场何时会开始为更深的利率正常化定价。报告提供了几个关键的分析锚点，值得逐层拆解。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 存款利率上调和贷款利率上调之间的利差，决定了加息的实际利润转化率\n\n加息对银行利润的影响，从来不是政策利率变动的简单函数。关键在于净息差的变化，而净息差取决于资产端和负债端利率调整的节奏差。\n\n从报告披露的数据看，三菱UFJ金融集团将普通存款利率从0.30%上调至0.40%，上调幅度10个基点，同时将短期优惠利率从2.125%上调至2.375%，上调幅度25个基点。这意味着存款利率对政策利率的贝塔系数维持在40%，与市场此前预期一致。三井住友金融集团和Mizuho金融集团随后跟进，将普通存款利率同样上调至0.40%。\n\n这个数字很关键。40%的存款贝塔系数意味着，每100个基点的政策利率上调，银行只需要将其中40个基点传导给存款人，剩余60个基点则转化为净息差的扩张。报告中的测算显示，对于以0.75%政策利率假设编制指引的银行，一次25个基点的加息对净利润的影响在1.1%至13.5%之间，差异巨大。M\n\n[... middle omitted ...]\n\n各家银行中期计划的调整节奏，以及日本央行政策沟通的边际变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本银行加息，银行股怎么看？\n\n加息周期确认\n银行股还有空间\n\n日本央行刚刚把政策利率从0.75%加到了1.0%，并且明确表示，只要经济和通胀配合，还会继续加。\n\n这对日本银行股意味着什么？我拆了三点逻辑👇\n\n1️⃣ 盈利预期可能上调\n之前很多银行做业绩指引时，假设的政策利率只有0.75%。现在利率到了1.0%，意味着不少银行的盈利预测有上调空间。已经有银行（比如横滨FG）主动披露了加息对下一年利润的正面影响，预计税后利润增加约100亿日元，ROE提升0.7%。其他银行大概率会跟上。\n\n2️⃣ 中期计划的兑现概率上升\n银行的中期计划（到2029年）普遍假设利率在0.75%-1.0%。现在加息周期确认，加上存款利率上浮幅度（存款beta）基本符合预期，市场会越来越相信这些计划能实现甚至超预期。\n\n3️⃣ 仓位轻，存在重估空间\n加息前，因为中东局势等不确定性，市场对银行股的持仓并不重。参考去年12月加息后的走势，银行股在加息后往往迎来一波估值修复或空头回补。目前银行股的市净率（P/B）大约只反映了0.75%-1.0%的利率水平，如果加息继续，估值还有上行空间。\n\n一句话总结：加息周期确认+盈利预期上调+仓位不重，\n\n[... middle omitted ...]\n\nit beta to policy rate at 40% as widely expected. SMFG and Mizuho followed with ordinary rate hikes to 0.40%. Aozora Bank hiked deposit rate by +25bp for deposits below Y1 million, same as aft\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R036",
    "title": "摩根斯坦利：国防产业正经历一场“去空心化”的结构性重塑，而非简单的周期上行",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：国防产业正经历一场“去空心化”的结构性重塑，而非简单的周期上行\n\n国防产业的拐点，往往不是由军费预算的增减来定义的。真正值得关注的信号，是资本结构、技术扩散路径和产业组织形态同时发生系统性变化。摩根斯坦利在其首届国家安全创新峰会的总结报告中，捕捉到了这样一个时刻。这份报告的核心判断并非“国防开支在增长”，而是：美国国防产业正在经历一场从“冷战后的空心化”向“新中层的重建”的深层转型。驱动这一转型的，不是单一的政策指令，而是资本、技术和地缘竞争三重力量在供给侧的协同作用。对于关注这一领域的投资者和决策者而言，理解这场结构性重塑，远比追逐季度订单数字更为关键。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 冷战后的“和平红利”正在逆转，产业空心化催生了新中层的崛起\n\n冷战结束后，美国国防产业经历了一轮大规模的整合浪潮。其直接后果是，中型国防企业（Mid-tier Defense Assets）被大量兼并或消失，产业格局呈现出“两头大、中间小”的哑铃型结构：一端是少数几家巨头（如洛克希德·马丁、诺斯罗普·格鲁曼），另一端是大量小而专的技术初创公司。摩根斯坦利指出，这种“空心化”在相当长一段时间内制约了产业的灵活性和创新效率。而现在，随着大国竞争回归，国防需求从“维持存量”转向“快速迭代与规模化生产”，这种结构性缺陷变得不可持续。\n\n报告揭示了两股力量正在共同“填补”这个中空地带。其一是国防硬件的商业化。许多原本仅用于军事领域的传感器、通信和动力技术，开始在商业市场找到应用场景，这降低了单一客户依赖风险，也吸引了更广泛的资本。其二是风险资本的介入。传统上，国防领域因其长周期、高门槛和客户单一性，对风险资本缺乏吸引力。但现在，一批愿意承担早期技术和市场风险的“颠覆性资本”正在涌入，它们不追求短期回报，而是押\n\n[... middle omitted ...]\n\n报告的完整图表、数据细节，并围绕这些未解的问题展开深度讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n国防投研圈正在发生什么变化\n\n国防业正在经历转折点\n\n刚参加完某外资投行的首届国家安全创新峰会，一天10场panel，30多家公司、150多位投资人。信息密度极高，和大家分享几个核心观察。\n\n1/ 国防的“中间层”正在重建\n冷战后的整合潮让国防业中间层空心化，但现在“和平红利”正在消退。两个关键变化：国防硬件的商业化 + 愿意承担风险的新资本涌入。估值逻辑越来越像成长股，只要能证明赛道领导力和可规模化生产。\n\n2/ 太空情报：速度优先于精度\n太空情报的核心设计目标正在从“收集质量”转向“降低延迟”。未来价值创造可能不属于硬件最强的公司，而是那些能简化数据访问和决策流程的公司。\n\n3/ 战场自主：不是替代，而是扩展\n自主技术本身不新，新的是规模化部署。不是取代高端平台，而是用低成本系统扩充整体作战能力。乌克兰的无人机技术已经被非国家行为体获取，反无人机技术变得紧迫。\n\n4/ 导弹供应链有隐形瓶颈\n除了大家关注的高超音速测试，供应链瓶颈在记忆体、化学品、高温材料等环节。定制化和规模化之间的张力是行业老大难。\n\n5/ 生产能力正在成为战略资产\n最近冲突表明，工业韧性可能和技术优势同等重要。下一代国防制造商的竞争优势\n\n[... middle omitted ...]\n\nsed defense, battlefield autonomy, missile production, dual-use technology, rare earths, and more. It's clear to us that Defense is approaching a defining moment as the sector digests harsh le\n\n[... middle omitted ...]\n\n Grumman Corp. (NOC.N)</td><td>O (09/07/2020)</td><td>$544.73</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R037",
    "title": "摩根斯坦利：市场低估的不是油运需求，而是供给侧的再定价",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：市场低估的不是油运需求，而是供给侧的再定价\n\n过去三周，油轮运输板块股价跑输大盘17至27个百分点。市场给出的理由很清晰：霍尔木兹海峡关闭时间超出预期，全球原油库存持续消耗，市场担忧油运需求萎缩，进而导致运力过剩、即期运价承压。\n\n但摩根斯坦利在最新发布的一份研报中提出了一个与市场共识截然相反的判断——如果海峡真的重新开放，油轮运输板块非但不是利空出尽，反而可能迎来一轮持续性更强的运价支撑。这份报告的核心价值不在于预测运价能涨多少，而在于指出了市场定价中一个被系统性忽视的结构性变量：供给侧的真实弹性远低于市场假设。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 市场对“需求萎缩”的担忧可能正好把方向搞反了\n\n市场在过去三周抛售油轮股的逻辑链条是：海峡关闭导致原油运输需求下降，运力过剩，运价承压。这条逻辑在表面上看没有问题，但它隐含了一个关键假设——油运需求的下降是永久性的。\n\n摩根斯坦利的报告给出了完全不同的解读。海峡关闭期间，全球原油库存持续消耗，进口国补库意愿被压制，出口国在波斯湾的储油也无法顺利释放。一旦海峡重新开放，这些被压制的需求不会缓慢恢复，而是可能在短时间内集中释放。进口国需要重建库存，出口国需要清空储油，两股力量叠加，油运需求可能在一两个季度内出现脉冲式增长。\n\n这意味着，过去三周市场定价的“需求萎缩”很可能只是暂时的流动性收缩，而非趋势性恶化。真正值得关注的不是需求是否会恢复，而是当需求以超预期速度回归时，供给端能否接得住。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 即期运价不会一次冲高后迅速回落，真正的定价锚在补库周期的长度\n\n市场对“运价冲高后迅速回落”的担忧有其合理性。历史上，突发事件后的运价脉冲往往难以持续。但摩根斯坦利在\n\n[... middle omitted ...]\n\n完整研报的原始图表和估值拆解，并持续跟踪这些关键变量的变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n霍尔木兹重启，油运要反转？\n\n油运反转逻辑拆解\n\n最近油运板块跌了17-27%，市场情绪跌到冰点。但某外资投行刚刚发了研报，说如果霍尔木兹海峡重新开放，油运很可能迎来一波反弹。\n\n1️⃣ 为什么之前跌了那么惨？\n5月21日到6月11日，油运股跑输大盘17-27%。核心原因是：市场原本预期海峡很快会重开，结果等了很久还没动静。全球石油库存越用越低，大家担心运输需求会萎缩，运价也会跟着跌。\n\n2️⃣ 如果海峡真的重开，会发生什么？\n研报认为会出现两个连锁反应：一是进口国急着补库存，出口国要清空波斯湾的储油，运输需求会爆发式增长。二是很多油轮已经跑到大西洋市场去了，中东可能出现运力短缺。关键是，现在波斯湾里虽然还有船，但都是满载状态，短期内放不出运力。\n\n3️⃣ 涨完一波就完了吗？\n不一定。研报重点看的是未来3-6个月两个变量：全球石油补库存的持续性（可能持续几个季度甚至更久），以及伊朗石油制裁是否解除。这两个因素都可能让运价维持在高位。\n\n4️⃣ 二季度业绩怎么看？\n招商轮船（CMES）预计二季度净利润42亿，环比增长超50%，主要受益于3月VLCC即期运价大涨和干散货运价走强。中远海能（CSE）预计只有22亿，\n\n[... middle omitted ...]\n\nmes' share prices underperformed market indexes by 17-27ppts during May 21 and Jun 11, 2026, mainly on the market's disappointment that the Strait of Hormuz had remained closed for longer than\n\n[... middle omitted ...]\n\ning Co Ltd (002120.SZ)</td><td>U (07/29/2020)</td><td>Rmb6.71</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "Figure 1",
    "context": "Despite significant interest for Kevin Warsh's first meeting, we do not expect any big surprises this week. Market expectations already lean towards a hawkish statement and SEP: (1) the statement is likely to drop the easing bias; (2) the core PCE forecast sho"
  },
  {
    "figure_id": "F002",
    "report_id": "R001",
    "label": "Figure 2",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 2. DXY is close to its short-term fair value"
  },
  {
    "figure_id": "F003",
    "report_id": "R001",
    "label": "Figure 3",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Ultimately, our medium-term USD view is based on relative growth differentials, which leaves us looking for EURUSD towards 1.14 (with potential for a downside overshoot). But we may first ne"
  },
  {
    "figure_id": "F004",
    "report_id": "R001",
    "label": "Figure 4",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 4. DXY range at the base of the uptrend continues"
  },
  {
    "figure_id": "F005",
    "report_id": "R002",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: Net COT positioning had climbed significantly in late Q4 2025, helping copper price to reach \\$13,000/t in December. Copper Prices vs. COT Investment Funds Positioning"
  },
  {
    "figure_id": "F006",
    "report_id": "R002",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: Comex copper inventories have steadily risen since April 2025 with an average of c.9kt incremental inventories per week. Comex Copper Inventories (short ton) vs. Weekly Change"
  },
  {
    "figure_id": "F007",
    "report_id": "R002",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Copper comex inventories have risen steadily by c.10,000 tonnes per week since summer 2025 as traders anticipate US tariffs on refined copper. Copper Inventory (t, LHS) vs Copper Price (\\$/t, RHS)"
  },
  {
    "figure_id": "F008",
    "report_id": "R002",
    "label": "Exhibit 4",
    "context": "EXHIBIT 4: Positive sentiment in the stock market has helped copper to break past \\$14,000/t level in mid-May. Widening spread between LME and Comex also helps to maintain positive sentiment in the copper market."
  },
  {
    "figure_id": "F009",
    "report_id": "R002",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 10: The CME copper contract is a duty paid, customs cleared contract. Hence, when the section 212 investigation on copper begun in Q1 2025, the market started pricing in potential tariffs."
  },
  {
    "figure_id": "F010",
    "report_id": "R002",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: Space availability in CME copper warehouse is unlikely to be the limiting factor for further arbitrage trading"
  },
  {
    "figure_id": "F011",
    "report_id": "R002",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: Traders expect the US might add import taxes on refined copper. Unlike the CME, the LME delivers metal only to duty-free zones. If a trader's long position expires on the LME, they get a warrant but must pay duty to brin"
  },
  {
    "figure_id": "F012",
    "report_id": "R002",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 16: Copper price forecasts - consensus and Bernstein estimates"
  },
  {
    "figure_id": "F013",
    "report_id": "R002",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 17: Coverage Exposure by Commodity Coverage Exposure by Commodity (2027e EBITDA\\*)"
  },
  {
    "figure_id": "F014",
    "report_id": "R002",
    "label": "EXHIBIT 18",
    "context": "EXHIBIT 18: ANTO has 1.4 beta to copper prices Daily Price Changes"
  },
  {
    "figure_id": "F015",
    "report_id": "R002",
    "label": "EXHIBIT 19",
    "context": "EXHIBIT 19: FCX has 1.5 beta to copper prices Daily Price Changes FCX vs. LME Copper (2026)"
  },
  {
    "figure_id": "F016",
    "report_id": "R002",
    "label": "EXHIBIT 20",
    "context": "EXHIBIT 20: AAL has a decent 1.1 beta to copper prices but with slightly lower R sq"
  },
  {
    "figure_id": "F017",
    "report_id": "R002",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 21: BHP has 0.7 beta to copper prices Daily Price Changes"
  },
  {
    "figure_id": "F018",
    "report_id": "R003",
    "label": "Exhibit 3",
    "context": "EXHIBIT 2: Arm argues that agentic AI shifts more work back to the CPU: accelerators generate tokens, but CPUs orchestrate the agents, memory and workflows needed to deliver answers, making Arm's efficient CPU architecture increasi"
  },
  {
    "figure_id": "F019",
    "report_id": "R003",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: CPU is expected to play a more important role within inference, in the agentic area."
  },
  {
    "figure_id": "F020",
    "report_id": "R003",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: Agentic AI shifts compute balance toward CPUs, with CPU share rising from \\~14% in Traditional LLMs to 50%, highlighting CPUs' growing orchestration role alongside GPUs in AI workloads at scale CPU:GPU ratio shift in Age"
  },
  {
    "figure_id": "F021",
    "report_id": "R003",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: AI infrastructure TAM expands sharply by CY30, led by data center accelerators reaching \\$1T, while data center CPU also quadruples from \\$33bn to \\$137bn. CPU/GPU TAM"
  },
  {
    "figure_id": "F022",
    "report_id": "R003",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: We expect the server CPU market to grow from US\\$37bn in 2025 to US\\$223bn in 2030, accelerating at a 43% CAGR, driven by Agentic AI adoption."
  },
  {
    "figure_id": "F023",
    "report_id": "R003",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: We estimate AI accelerator GPU power reaches \\~37GW in 2028 versus 12.8GW in 2025, a 43% CAGR over 2025–2028E. If we assume GPUs to account for \\~70% of server power, total AI data center demand scales from \\~18GW in 202"
  },
  {
    "figure_id": "F024",
    "report_id": "R003",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: CPU represents between 40% and 60% of power consumption in a general server, but only 5–10% in an AI server, where most power is consumed by AI accelerators. CPU as % of Power"
  },
  {
    "figure_id": "F025",
    "report_id": "R003",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: Compariison of Server CPU specifications for Arm ASICs, Nvidia custom CPUs and x86. EXHIBIT 12: We expect Arm's market share to continue the strong trend of growth."
  },
  {
    "figure_id": "F026",
    "report_id": "R003",
    "label": "EXHIBIT 13",
    "context": "EXHIBIT 13: Roadmap of CPUs based on Arm IP"
  },
  {
    "figure_id": "F027",
    "report_id": "R003",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: We now forecast Arm AGI CPU sales to reach \\$22bn by FY31. FY27-FY31E: Arm AGI CPU Sales"
  },
  {
    "figure_id": "F028",
    "report_id": "R003",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: We believe OP contribution from Arm silicon could go as high as \\$7.7bn as of FY31. FY27-FY31E: Arm AGI CPU OP"
  },
  {
    "figure_id": "F029",
    "report_id": "R003",
    "label": "Exhibit 16",
    "context": "EXHIBIT 16: We estimate a 2030 server CPU TAM of \\$223bn, of which we believe Arm will be around \\$123bn. EXHIBIT 17: We estimate Nvidia-related Arm CPU units to grow by 5x by 2030."
  },
  {
    "figure_id": "F030",
    "report_id": "R003",
    "label": "Exhibit 18",
    "context": "For hyperscaler in-house CPUs, such as AWS Graviton and Google Axion, we model it as a function of server unit assumptions as well as ODM-direct server exposures, and applying Arm penetration within the CSP server base. In our model, we assume Arm penetration "
  },
  {
    "figure_id": "F031",
    "report_id": "R003",
    "label": "EXHIBIT 19",
    "context": "EXHIBIT 19: Within the estimated 2030 TAM of \\$123bn, Nvidia / CSP demand comprises the majority."
  },
  {
    "figure_id": "F032",
    "report_id": "R003",
    "label": "Exhibit 20",
    "context": "EXHIBIT 20: Core count for server-side CPUs is increasing."
  },
  {
    "figure_id": "F033",
    "report_id": "R003",
    "label": "Exhibit 22",
    "context": "EXHIBIT 21: We expect per-chip royalty to drop in FY26-FY27 due to Grace / Vera, but expect strong growth going forward due to increase in royalty rate. FY22-FY31E: Blended per-chip royalty for server CPUs"
  },
  {
    "figure_id": "F034",
    "report_id": "R003",
    "label": "EXHIBIT 22",
    "context": "EXHIBIT 22: We expect a strong growth in cloud royalty revenue. FY21-FY31E: Cloud Royalty revenue"
  },
  {
    "figure_id": "F035",
    "report_id": "R003",
    "label": "EXHIBIT 23",
    "context": "EXHIBIT 24: Arm has rerated significantly over the past month, and is currently valued at +5SD of historical range, on a 1-year forward P/E basis."
  },
  {
    "figure_id": "F036",
    "report_id": "R003",
    "label": "EXHIBIT 25",
    "context": "EXHIBIT 25: As such, we feel it's more sensible to value Arm on FY31E EPS, on which the company anchors their projection. On FY31E EPS, the stock currently trades at 44x, close to +3SD of YTD range."
  },
  {
    "figure_id": "F037",
    "report_id": "R003",
    "label": "Exhibit 32",
    "context": "EXHIBIT 31: Agentic AI has driven a sharp upward revision in x86 server CPU growth this year x86 Server CPU Revenue"
  },
  {
    "figure_id": "F038",
    "report_id": "R003",
    "label": "EXHIBIT 32",
    "context": "EXHIBIT 32: AMD's x86 share gains accelerated in Q1 as Intel found themselves constrained"
  },
  {
    "figure_id": "F039",
    "report_id": "R003",
    "label": "Exhibit 35",
    "context": "EXHIBIT 35: China's share of global x86 server CPU TAM is entering a period of near-term compression, before structurally recovery after 2027 Global vs China x86 server CPU TAM (Bn USD)"
  },
  {
    "figure_id": "F040",
    "report_id": "R003",
    "label": "Exhibit 36",
    "context": "EXHIBIT 36: Hygon has been consistently gaining share and poised for further acceleration after 2027 China x86 server CPU TAM and Domestic/ Hygon share (Bn USD)"
  },
  {
    "figure_id": "F041",
    "report_id": "R004",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: Oil prices to remain supported near \\~\\$90/bbl in 2026 before easing to \\~\\$78/bbl as supply normalises and inventories rebuild"
  },
  {
    "figure_id": "F042",
    "report_id": "R004",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: OPEC seaborne exports fell by \\~14MMbbls/d at peak disruption; recovery to be gradual with Hormuz reopening"
  },
  {
    "figure_id": "F043",
    "report_id": "R004",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: At current OPEC seaborne oil exports of around 13MMbls/d, we expect production will be about 20MMbls/d which is down 8-9MMbls/d from February OPEC + UAE seaborne oil exports vs production (kbd)"
  },
  {
    "figure_id": "F044",
    "report_id": "R004",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: In our supply and demand model, we expect normalisation to take around six months OPEC production (MMbls/d)"
  },
  {
    "figure_id": "F045",
    "report_id": "R004",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: The IEA revised down global oil demand by 0.3MMbls/d to 104.0MMbls/d for 2026 implying demand will fall by 0.4MMbls/d y-o-y"
  },
  {
    "figure_id": "F046",
    "report_id": "R004",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: As flows through Hormuz normalise over the next six months, demand should recover in tandem with improving supply conditions, before strengthening more meaningfully into 2027"
  },
  {
    "figure_id": "F047",
    "report_id": "R004",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: While short-term volatility reflects the impact of supply disruption, the medium-term trajectory remains intact, with demand growth resuming as market conditions normalise and inventories begin to rebuild"
  },
  {
    "figure_id": "F048",
    "report_id": "R004",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: We forecast demand to rise to \\~106.2MMbbls/d in 2027, driven by cyclical recovery and continued structural growth Global oil demand (MMbls/d)"
  },
  {
    "figure_id": "F049",
    "report_id": "R004",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: US commercial crude and product inventories have been drawing since mid-April as the market tightens"
  },
  {
    "figure_id": "F050",
    "report_id": "R004",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: US SPR inventories draws are helping absorb part of the global supply shock"
  },
  {
    "figure_id": "F051",
    "report_id": "R004",
    "label": "EXHIBIT 13",
    "context": "EXHIBIT 13: US oil inventories are drawing counter-cyclically versus historical 5-year average"
  },
  {
    "figure_id": "F052",
    "report_id": "R004",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: US commercial crude oil stocks are below the lower end of the 5-year range"
  },
  {
    "figure_id": "F053",
    "report_id": "R004",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: US product inventories have fallen materially"
  },
  {
    "figure_id": "F054",
    "report_id": "R004",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 17: Based on historical regressions, there is a 1.3x correlation between OECD inventories and US+ARA +Japan stocks (which we track closely)"
  },
  {
    "figure_id": "F055",
    "report_id": "R004",
    "label": "EXHIBIT 18",
    "context": "EXHIBIT 18: Demand and supply outlook based on the latest IEA data"
  },
  {
    "figure_id": "F056",
    "report_id": "R004",
    "label": "EXHIBIT 20",
    "context": "EXHIBIT 20: We expect OECD commercial inventories to draw near term before rebuild next year"
  },
  {
    "figure_id": "F057",
    "report_id": "R004",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 21: Oil prices are highly correlated to OECD commercial inventories"
  },
  {
    "figure_id": "F058",
    "report_id": "R004",
    "label": "EXHIBIT 22",
    "context": "EXHIBIT 22: Oil prices to average \\~\\$90/bbl in 2026 before easing to \\~\\$78/bbl in 2027 as inventories rebuild"
  },
  {
    "figure_id": "F059",
    "report_id": "R004",
    "label": "EXHIBIT 23",
    "context": "EXHIBIT 23: Spot oil is trading in the \\$80 range versus current marginal cost of oil of \\$77/bbl"
  },
  {
    "figure_id": "F060",
    "report_id": "R005",
    "label": "Figure 1",
    "context": "Figure 1: Outlook for outstanding of fund-provisioning measure to stimulate bank lending"
  },
  {
    "figure_id": "F061",
    "report_id": "R005",
    "label": "Figure 2",
    "context": "Figure 2: Forecasts for BoJ's JGB holding Gross purchase"
  },
  {
    "figure_id": "F062",
    "report_id": "R008",
    "label": "Figure 1",
    "context": "- Operating rates for petroleum asphalt plants suggest processed crude oil production contraction may have deepened in May, with further decline in June (vs -5.8% oya in April). - Operating rates for tire plants suggest auto IP growth may have improved modestl"
  },
  {
    "figure_id": "F063",
    "report_id": "R008",
    "label": "Figure 1",
    "context": "Figure 1.2: Industrial production - Auto"
  },
  {
    "figure_id": "F064",
    "report_id": "R008",
    "label": "Figure 1",
    "context": "Figure 1.3: Industrial production - Steel"
  },
  {
    "figure_id": "F065",
    "report_id": "R008",
    "label": "Figure 1",
    "context": "Figure 1.4: China exports"
  },
  {
    "figure_id": "F066",
    "report_id": "R008",
    "label": "Figure 2",
    "context": "Figure 2.3: Deadweight tonnage of departing ships - Container"
  },
  {
    "figure_id": "F067",
    "report_id": "R008",
    "label": "Figure 2",
    "context": "Figure 2.5: Deadweight tonnage of departing ships - Bulk"
  },
  {
    "figure_id": "F068",
    "report_id": "R008",
    "label": "Figure 2",
    "context": "Figure 2.2: BEISL freight index"
  },
  {
    "figure_id": "F069",
    "report_id": "R008",
    "label": "Figure 2",
    "context": "Figure 2.4: Deadweight tonnage of arrived ships - Container"
  },
  {
    "figure_id": "F070",
    "report_id": "R008",
    "label": "Figure 2",
    "context": "Figure 2.6: Deadweight tonnage of arrived ships - Bulk"
  },
  {
    "figure_id": "F071",
    "report_id": "R008",
    "label": "Figure 2",
    "context": "Figure 2.7: Deadweight tonnage of arrived ships - Oil Tanker"
  },
  {
    "figure_id": "F072",
    "report_id": "R008",
    "label": "Figure 2",
    "context": "Figure 2.8: Deadweight tonnage of departing ships - Oil Tanker"
  },
  {
    "figure_id": "F073",
    "report_id": "R008",
    "label": "Figure 2",
    "context": "Figure 2.9: China flight execution"
  },
  {
    "figure_id": "F074",
    "report_id": "R008",
    "label": "Figure 2",
    "context": "Figure 2.10: China flight cancellation rate"
  },
  {
    "figure_id": "F075",
    "report_id": "R008",
    "label": "Figure 2",
    "context": "Figure 2.11: China imports of soybeans from world"
  },
  {
    "figure_id": "F076",
    "report_id": "R008",
    "label": "Figure 2",
    "context": "Figure 2.12: China imports of soybeans from US"
  },
  {
    "figure_id": "F077",
    "report_id": "R008",
    "label": "Figure 3",
    "context": "## 3. Sales and production - Auto sales: According to CPCA, passenger car retail sales fell 22% oya in May, partially on lower per-car trade-in subsidies and purchase tax exemptions, and higher fuel costs. NEV sales fell a narrower 7.5%. This suggests auto sal"
  },
  {
    "figure_id": "F078",
    "report_id": "R008",
    "label": "Figure 3",
    "context": "Figure 3.3: Operating rate for semi-steel tire"
  },
  {
    "figure_id": "F079",
    "report_id": "R008",
    "label": "Figure 3",
    "context": "Figure 3.5: Operating rate for steel rebar at major steel plants"
  },
  {
    "figure_id": "F080",
    "report_id": "R008",
    "label": "Figure 3",
    "context": "Figure 3.2: Operating rate for all-steel tire"
  },
  {
    "figure_id": "F081",
    "report_id": "R008",
    "label": "Figure 3",
    "context": "Figure 3.4: Operating rate for petroleum asphalt plants"
  },
  {
    "figure_id": "F082",
    "report_id": "R008",
    "label": "Figure 3",
    "context": "Figure 3.6: Operating rate for coke oven plants"
  },
  {
    "figure_id": "F083",
    "report_id": "R008",
    "label": "Figure 4",
    "context": "- CGB issuance slowed sharply to 164bn yuan in June mtd (including scheduled issuance for the coming week) from 708bn yuan in May. Ytd issuance reached $37.9\\%$ of annual issuance target, trailing last year's $50.8\\%$ pace. In further breakdown, special CGB is"
  },
  {
    "figure_id": "F084",
    "report_id": "R008",
    "label": "Figure 4",
    "context": "Figure 4.2: China CGB net issuance progress"
  },
  {
    "figure_id": "F085",
    "report_id": "R008",
    "label": "Figure 4",
    "context": "Figure 4.3: China special LGB issuance"
  },
  {
    "figure_id": "F086",
    "report_id": "R008",
    "label": "Figure 4",
    "context": "Figure 4.4: China special LGB issuance progress"
  },
  {
    "figure_id": "F087",
    "report_id": "R008",
    "label": "Figure 4",
    "context": "Figure 4.5: China special CGB net issuance"
  },
  {
    "figure_id": "F088",
    "report_id": "R008",
    "label": "Figure 4",
    "context": "Figure 4.6: Local government special refinancing bonds issuance"
  },
  {
    "figure_id": "F089",
    "report_id": "R008",
    "label": "Figure 4",
    "context": "Figure 4.7: General LGB new issuance"
  },
  {
    "figure_id": "F090",
    "report_id": "R008",
    "label": "Figure 4",
    "context": "Figure 4.8: General LGB new issuance progress"
  },
  {
    "figure_id": "F091",
    "report_id": "R008",
    "label": "Figure 4",
    "context": "Figure 4.9: Outstanding major monetary policy instruments"
  },
  {
    "figure_id": "F092",
    "report_id": "R008",
    "label": "Figure 4",
    "context": "Figure 4.10: Outright OMO operation"
  },
  {
    "figure_id": "F093",
    "report_id": "R008",
    "label": "Figure 5",
    "context": "Home sales in both new and secondary home markets outperformed the same period last year in June mtd, with some momentum easing lately. - 30 major cities' new home sales were $4\\%$ higher than the same period last year in June mtd, an improvement from May's $1"
  },
  {
    "figure_id": "F094",
    "report_id": "R008",
    "label": "Figure 5",
    "context": "Figure 5.2: Major cities' secondary housing transactions"
  },
  {
    "figure_id": "F095",
    "report_id": "R008",
    "label": "Figure 5",
    "context": "Figure 5.3: Centraline tier-1 cities' secondary asking price index"
  },
  {
    "figure_id": "F096",
    "report_id": "R008",
    "label": "Figure 5",
    "context": "Figure 5.4: Centraline sales manager index"
  },
  {
    "figure_id": "F097",
    "report_id": "R008",
    "label": "Figure 5",
    "context": "Figure 5.5: Weekly land sales"
  },
  {
    "figure_id": "F098",
    "report_id": "R008",
    "label": "Figure 5",
    "context": "Figure 5.6: Land sale premium rate"
  },
  {
    "figure_id": "F099",
    "report_id": "R008",
    "label": "Figure 6",
    "context": "- Gasoline, diesel and LPG prices continued to moderate in the first ten days of June, while LNG prices ticked up mildly. Coal prices rose further, now standing at the highest level in nearly 20 months, also on summer seasonal demand. - Petrochemical prices we"
  },
  {
    "figure_id": "F100",
    "report_id": "R008",
    "label": "Figure 6",
    "context": "Figure 6.2: Petrochemical product price Figure 6.3: Fertilizer price"
  },
  {
    "figure_id": "F101",
    "report_id": "R008",
    "label": "Figure 6",
    "context": "Figure 6.2: Petrochemical product price Figure 6.3: Fertilizer price"
  },
  {
    "figure_id": "F102",
    "report_id": "R008",
    "label": "Figure 6",
    "context": "Figure 6.4: Grain and hog price"
  },
  {
    "figure_id": "F103",
    "report_id": "R008",
    "label": "Figure 6",
    "context": "Figure 6.5: Agricultural food product wholesale price"
  },
  {
    "figure_id": "F104",
    "report_id": "R008",
    "label": "Figure 6",
    "context": "Figure 6.6: Pork wholesales price"
  },
  {
    "figure_id": "F105",
    "report_id": "R008",
    "label": "Figure 6",
    "context": "Figure 6.7: Pork wholesales price vs. NBS data"
  },
  {
    "figure_id": "F106",
    "report_id": "R008",
    "label": "Figure 6",
    "context": "Figure 6.8: Commodity futures prices"
  },
  {
    "figure_id": "F107",
    "report_id": "R008",
    "label": "Figure 6",
    "context": "Figure 6.9: Copper price"
  },
  {
    "figure_id": "F108",
    "report_id": "R008",
    "label": "Figure 6",
    "context": "Figure 6.10: Cement price"
  },
  {
    "figure_id": "F109",
    "report_id": "R008",
    "label": "Figure 6",
    "context": "Figure 6.11: Aluminum price"
  },
  {
    "figure_id": "F110",
    "report_id": "R008",
    "label": "Figure 6",
    "context": "Figure 6.12: Steel rebar price"
  },
  {
    "figure_id": "F111",
    "report_id": "R008",
    "label": "Figure 6",
    "context": "Figure 6.13: Retail gasoline price vs. Brent oil"
  },
  {
    "figure_id": "F112",
    "report_id": "R008",
    "label": "Figure 6",
    "context": "Figure 6.14: Global commodity price vs. China PPI"
  },
  {
    "figure_id": "F113",
    "report_id": "R009",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Buy-the-dip strategy cumulative performance since 2023 - \"AI Infrastructure\" sub-theme"
  },
  {
    "figure_id": "F114",
    "report_id": "R009",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Buy-the-dip strategy cumulative performance since 2023 - \"Powering AI\" sub-theme"
  },
  {
    "figure_id": "F115",
    "report_id": "R009",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Hot CPI weighs on the S&P 500 (about -17 bp per +1σ) while hot NFP lifts it"
  },
  {
    "figure_id": "F116",
    "report_id": "R009",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Both CPI and NFP upside surprises raise US yields"
  },
  {
    "figure_id": "F117",
    "report_id": "R009",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Europe's core AI capex beneficiaries make up c. 15% of the MSCI Europe index AI Capex Beneficiaries in MSCI Europe (FFMCap Weighted)"
  },
  {
    "figure_id": "F118",
    "report_id": "R009",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Semis stand out on fundamental momentum indicators; Banks jump back into the top 3"
  },
  {
    "figure_id": "F119",
    "report_id": "R009",
    "label": "Exhibit 7",
    "context": "## The K-Shaped Economy Is Here To Stay We expect China's real GDP growth to be 4.8% in 2026 and 4.7% in 2027. The key driver would be strength in the \"new economy\" – exports and manufacturing capex related to AI, energy transition, and emerging tech sectors. "
  },
  {
    "figure_id": "F120",
    "report_id": "R009",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Increased external demand reliance would increase China's vulnerability to global cycle changes % Contribution of Net Exports to Real GDP Growth"
  },
  {
    "figure_id": "F121",
    "report_id": "R009",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Import penetration, measured as the share of domestic supply derived from imports, rose in 2025"
  },
  {
    "figure_id": "F122",
    "report_id": "R009",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Although nominal numbers suggest gross output rose considerably in 2025, it was largely price-driven Growth in Supply of Goods to Domestic Industry (%Y)"
  },
  {
    "figure_id": "F123",
    "report_id": "R009",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Import penetration for most non-durable goods has been range-bound"
  },
  {
    "figure_id": "F124",
    "report_id": "R009",
    "label": "Exhibit 12",
    "context": "Exhibit 12: The measured breakeven pace for payrolls fell sharply in the three months through February, then rose sharply in the three months through May"
  },
  {
    "figure_id": "F125",
    "report_id": "R009",
    "label": "Exhibit 13",
    "context": "Exhibit 13: We continue to expect 50k per month as the breakeven pace; the past 6, 9, and 12 months look consistent with that estimate"
  },
  {
    "figure_id": "F126",
    "report_id": "R009",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Corporate Cash Tax Rates Likely to Fall Further"
  },
  {
    "figure_id": "F127",
    "report_id": "R009",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Cumulative difference in corporate income tax receipts: 2026 vs. 2025"
  },
  {
    "figure_id": "F128",
    "report_id": "R009",
    "label": "Exhibit 16",
    "context": "Exhibit 16: AI vs. Dot.com: NASDAQ Performance from the key technology's arrival"
  },
  {
    "figure_id": "F129",
    "report_id": "R009",
    "label": "Exhibit 17",
    "context": "Exhibit 17: NTM consensus EPS trend over last 1 year"
  },
  {
    "figure_id": "F130",
    "report_id": "R010",
    "label": "Exhibit 9",
    "context": "■ Two-sided but still net upside price risks. ☐ Price upside scenario: Brent might rise above \\$130 in late 2026 and average \\$105 in 2027 (Exhibit 9) assuming Hormuz remains disrupted through 2027 with Gulf countries' exports rising gradually by 10mb/d by Dec"
  },
  {
    "figure_id": "F131",
    "report_id": "R010",
    "label": "Exhibit 1",
    "context": "Exhibit 1: We Are Reducing Our 2026Q4 Brent Forecast to \\$80 and to \\$75 for the 2027 Average as We Now Assume an Earlier Recovery in Mideast Supply Following a Deal to Reopen Hormuz"
  },
  {
    "figure_id": "F132",
    "report_id": "R010",
    "label": "Exhibit 2",
    "context": "Exhibit 2: We Now Assume That Oil Exports/Production from Persian Gulf Countries Recovers by End of July/October, Respectively"
  },
  {
    "figure_id": "F133",
    "report_id": "R010",
    "label": "Exhibit 3",
    "context": "Exhibit 3: This Normalization in Oil Exports From Gulf Producers to Their Pre-War Level May Be Achieved With a 12mb/d Increase in Hormuz Flows From Current Levels Estimating Early June Hit to Oil Flows from Persian Gulf Countries"
  },
  {
    "figure_id": "F134",
    "report_id": "R010",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Estimated Oil Flows From Persian Gulf Countries Have Trended Up From Less Than 30% of Normal Levels in Early March to Nearly 50% of Normal in Mid-June"
  },
  {
    "figure_id": "F135",
    "report_id": "R010",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Potential Sanctions Relief May Raise Iran Production Above Pre-War Levels and Reduce Oil on Water, Which Remains High at Nearly 120mb"
  },
  {
    "figure_id": "F136",
    "report_id": "R010",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Global Oil Demand Tends to Recover Swiftly Following Oil Supply Shocks But Remain Weak Following Recessions"
  },
  {
    "figure_id": "F137",
    "report_id": "R010",
    "label": "Exhibit 7",
    "context": "Exhibit 7: We Assume a Structural Trend of Global Strategic Stockpiling of Over 1mb/d in 2027"
  },
  {
    "figure_id": "F138",
    "report_id": "R010",
    "label": "Exhibit 8",
    "context": "Exhibit 8: We Estimate a 5mb/d Q2 Deficit, Which is Smaller Than the 14mb/d Hit to Mideast Liquids Production"
  },
  {
    "figure_id": "F139",
    "report_id": "R010",
    "label": "Exhibit 9",
    "context": "Exhibit 9: We See Risks to Our Brent Price Forecast as Two-Sided but Tilted to the Upside on Net"
  },
  {
    "figure_id": "F140",
    "report_id": "R010",
    "label": "Exhibit 10",
    "context": "Exhibit 10: We Reduce Our 2026Q4 Brent Forecast to \\$80 (vs. \\$90 Prior) and Our 2027 Average Forecast to \\$75 (vs. \\$80 Prior) Exhibit 11: We Estimate That Empty Oil Tankers Within the Strait or Within 5 Days of Navigation Have the"
  },
  {
    "figure_id": "F141",
    "report_id": "R010",
    "label": "Exhibit 12",
    "context": "Exhibit 12: We Estimate That OECD Commercial Oil Stocks Will Bottom Out in July at 2,686mb"
  },
  {
    "figure_id": "F142",
    "report_id": "R011",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Decomposing Alibaba & Tencent share price performance YTD"
  },
  {
    "figure_id": "F143",
    "report_id": "R011",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Food delivery + instant shopping comparisons between Meituan, Alibaba and JD (GS estimates)"
  },
  {
    "figure_id": "F144",
    "report_id": "R011",
    "label": "Exhibit 3",
    "context": "Exhibit 3: We estimate per our industry weekly parcel volume tracker, parcel collection volume growth of c.9% yoy in the first 14 days of June Weekly parcel volume tracker"
  },
  {
    "figure_id": "F145",
    "report_id": "R011",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Comparison of online goods GMV yoy growth and parcel volume growth Exhibit 6: 6.18 festival's daily average parcel volume in 2024/25/26"
  },
  {
    "figure_id": "F146",
    "report_id": "R011",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Our estimates for online GMV and parcel volume growth (annual)"
  },
  {
    "figure_id": "F147",
    "report_id": "R011",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Our estimates for parcel volume growth (quarterly)"
  },
  {
    "figure_id": "F148",
    "report_id": "R011",
    "label": "Exhibit 9",
    "context": "Exhibit 10: China eCommerce: Gross GMV share % by platform (quarterly)"
  },
  {
    "figure_id": "F149",
    "report_id": "R011",
    "label": "Exhibit 11",
    "context": "Exhibit 11: China eCommerce: Gross GMV share % by platform (yearly)"
  },
  {
    "figure_id": "F150",
    "report_id": "R011",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Online retail goods sales growth accelerated to +2.6% in May vs. +0.2% in Apr Total retail sales, online retail goods sales & express parcel volumes"
  },
  {
    "figure_id": "F151",
    "report_id": "R011",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Spending on food and clothing +16% and +7% yoy for Jan-May Online retail sales by spending purpose"
  },
  {
    "figure_id": "F152",
    "report_id": "R011",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Total retail sales by category"
  },
  {
    "figure_id": "F153",
    "report_id": "R011",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Restaurant dining sales at +1% yoy in May (vs. +2% yoy in April)"
  },
  {
    "figure_id": "F154",
    "report_id": "R011",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Bloomberg Second measure weekly Temu US Panel Sales BBG Second measure weekly Temu US Panel Sales"
  },
  {
    "figure_id": "F155",
    "report_id": "R011",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Bloomberg Second Measure monthly Temu US Panel Sales BBG Second Measure monthly Temu US Panel Sales"
  },
  {
    "figure_id": "F156",
    "report_id": "R011",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Temu merchants increased +1% mom in May"
  },
  {
    "figure_id": "F157",
    "report_id": "R011",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Temu global MAU down to 485mn in May 2026 (-5% mom)"
  },
  {
    "figure_id": "F158",
    "report_id": "R012",
    "label": "Exhibit 1",
    "context": "Exhibit 1: I-Moutai active users surged from Jan 1st 2026 when Feitian was officially launched on i-Moutai"
  },
  {
    "figure_id": "F159",
    "report_id": "R012",
    "label": "Exhibit 2",
    "context": "Exhibit 2: 53% Feitian Moutai product prices"
  },
  {
    "figure_id": "F160",
    "report_id": "R012",
    "label": "Exhibit 3",
    "context": "Exhibit 3: 52% Common Wuliangye product prices"
  },
  {
    "figure_id": "F161",
    "report_id": "R012",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Guojiao 1573 product prices"
  },
  {
    "figure_id": "F162",
    "report_id": "R012",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Wholesale prices of Moutai's 4 non-standard SKUs"
  },
  {
    "figure_id": "F163",
    "report_id": "R012",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Select Spirits names - 2026 YTD and weekly (Jun 5 \\~ Jun 12) stock performance Moutai (+1.5%) and Laobaigan (+0.9%) were relatively better price performers among China Spirits last week YTD and Past Week Performance"
  },
  {
    "figure_id": "F164",
    "report_id": "R013",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Industrial production rose in month-on-month terms in May after seasonal adjustment"
  },
  {
    "figure_id": "F165",
    "report_id": "R013",
    "label": "Exhibit 2",
    "context": "Exhibit 2: April-to-May acceleration in year-on-year IP growth was led by computer & other equipment, electric machinery and utilities industries"
  },
  {
    "figure_id": "F166",
    "report_id": "R013",
    "label": "Exhibit 3",
    "context": "Exhibit 3: FAI growth declined further in May"
  },
  {
    "figure_id": "F167",
    "report_id": "R013",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Most property activity data remained subdued in May"
  },
  {
    "figure_id": "F168",
    "report_id": "R013",
    "label": "Exhibit 5",
    "context": "Exhibit 5: After seasonal adjustment, nationwide surveyed unemployment rate edged down in May, while the 31-city metric stayed flat"
  },
  {
    "figure_id": "F169",
    "report_id": "R014",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Low European gas storage and an ongoing Asia pull for LNG cargoes at the expense of Europe would likely lead to a further rise in TTF without a Hormuz flow normalization NW European Storage (Ihs) vs Global Ex-Qatar LNG L"
  },
  {
    "figure_id": "F170",
    "report_id": "R014",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Supply growth ex-Qatar has taken global LNG supply back to flat yoy Year-on-year Change in LNG Exports by Region, Right Panel Shows Latest 4wma Data Point"
  },
  {
    "figure_id": "F171",
    "report_id": "R014",
    "label": "Exhibit 3",
    "context": "Exhibit 3: We expect European gas prices to balance the market in the low 40 EURs/MWh for the remainder of summer Realized and forward TTF prices and fuel switching ranges, and TTF GS fcast"
  },
  {
    "figure_id": "F172",
    "report_id": "R014",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Risks to our 2026/27 TTF view remain skewed to the upside EUR/MWh GS TTF Price Scenarios"
  },
  {
    "figure_id": "F173",
    "report_id": "R016",
    "label": "Figure 1",
    "context": "## Upstream CCL and AI-fabric Material Greatest capacity shortages are in Al-fabric and e-glass fabric in CCL / PCB supply chain, as cited by Shengyi Tech and Grace Fabric Shengyi Tech and Grace Fabric both cited the greatest shortage in terms of capacity bein"
  },
  {
    "figure_id": "F174",
    "report_id": "R016",
    "label": "Figure 2",
    "context": "Key technical barrier is not PTFE CCL but PTFE PCB – Shengyi mgmt believes they are able to deliver over 90% production yield for PTFE CCL. They see the technical barrier as PCB end rather than CCL. Han's CNC (301200.SZ, Buy) mgmt, during the tour, also highli"
  },
  {
    "figure_id": "F175",
    "report_id": "R016",
    "label": "Figure 4",
    "context": "Figure 4. Illustration of thickness of fabric to end-applications © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 5. Estimation of 60-95% YTD surge of ASP on KBL e-glass fabric"
  },
  {
    "figure_id": "F176",
    "report_id": "R016",
    "label": "Figure 6",
    "context": "A similar AI spillover effect is occurring in the PCB drill bit sector. Chinese PCB drill bit maker DTECH (301377.SZ) recently received IC substrate drill bit orders from Unimicron (3037.TW) due to tight supply at Unimicron's current drill bit supplier Union T"
  },
  {
    "figure_id": "F177",
    "report_id": "R016",
    "label": "Figure 7",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 7. PCB drilling equipment ASP and GPM by product"
  },
  {
    "figure_id": "F178",
    "report_id": "R016",
    "label": "Figure 8",
    "context": "In China, UBTECH (9880.HK) will soon debut several new robot products, including bionic robots, industrial humanoid robot Walker S3, commercial humanoid robot new Walker C, and wheel-based Cruzr Y1 to drive its top line growth. Mgmt. guided that the total robo"
  },
  {
    "figure_id": "F179",
    "report_id": "R016",
    "label": "Figure 9",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 9. UBTECH: Pre-orders of bionic robot U1 during the first 9 days"
  },
  {
    "figure_id": "F180",
    "report_id": "R016",
    "label": "Figure 10",
    "context": "Our visits to Precision Tsugami China (PTC; 1651.HK) and Bozhon Precision (688097.SS) showed that the electronics supply chain, especially Apple's supply chain and AI-related manufacturing has led to demand improvement for machine tools and factory automation."
  },
  {
    "figure_id": "F181",
    "report_id": "R016",
    "label": "Figure 11",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 11. Inovance: General automation order growth"
  },
  {
    "figure_id": "F182",
    "report_id": "R016",
    "label": "Figure 12",
    "context": "Hengli Hydraulic's (601100.SS) excavator component production lines continue to run at full capacity due to 1) strong large size excavator demand from Chinese OEMs, 2) Hengli's market share gains in the excavator pump and valve market in China, and 3) Hengli's"
  },
  {
    "figure_id": "F183",
    "report_id": "R016",
    "label": "Figure 13",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 13. China's tower crane leasing rate index vs. fleet utilization rate"
  },
  {
    "figure_id": "F184",
    "report_id": "R017",
    "label": "Exhibit 1",
    "context": "Exhibit 2: May-26 70-city ASP index was -0.2%/-0.3% mom (vs. -0.2%/-0.2% mom for Apr), with 16/10 cities (vs. 14/12 in Apr) recording sequentially improved ASPs and 2/3 cities (vs. 7/4 in Apr) recording sequentially flattened ASPs"
  },
  {
    "figure_id": "F185",
    "report_id": "R017",
    "label": "Exhibit 3",
    "context": "Exhibit 3: May 2026: Nationwide property sales above high-frequency tracking and inline with GSe on value terms, while construction activities stayed weak as expected"
  },
  {
    "figure_id": "F186",
    "report_id": "R017",
    "label": "Exhibit 4",
    "context": "Exhibit 4: May-26 70-city primary ASP index was -0.2% mom (vs. -0.2% mom for Apr) and 16 cities (vs. 14 in Apr) recorded sequential ASP improvements in primary markets Average 70 cities primary ASP Index mom"
  },
  {
    "figure_id": "F187",
    "report_id": "R017",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Land market activity remained sluggish in May-26, with volume/value at -31%/-14% yoy (vs. -25%/-34% yoy in Apr), sending 5M26 nationwide land sales volume/value to -22%/-33% yoy Nationwide land sales volume"
  },
  {
    "figure_id": "F188",
    "report_id": "R017",
    "label": "Exhibit 6",
    "context": "Exhibit 6: In May, land auction premium ratio increased mom, mainly driven by Tier-1 cities; and land auction failure ratio improved mom, mainly supported by lower tier cities Monthly land transaction failure ratio nationwide and b"
  },
  {
    "figure_id": "F189",
    "report_id": "R017",
    "label": "Exhibit 7",
    "context": "Exhibit 7: We estimate developers' total new funding sources were -60% mom and -14% yoy in May-26, implying +8% yoy in 5M26 (vs. +4% yoy in 2025) Breakdown of developers' external funding"
  },
  {
    "figure_id": "F190",
    "report_id": "R017",
    "label": "Exhibit 8",
    "context": "Exhibit 8: We estimate Rmb1.53tn local government special bonds have been issued by mid-June Monthly local government special bond issuance tracker"
  },
  {
    "figure_id": "F191",
    "report_id": "R017",
    "label": "Exhibit 9",
    "context": "Exhibit 9: 15 major cities' secondary sales volume on average fell $12\\%$ mom and was $+8\\%$ yoy in May-26, and recorded $-3\\%$ yoy in 5M26 15 major cities' secondary market transaction volume tracker 15 major cities secondary sale"
  },
  {
    "figure_id": "F192",
    "report_id": "R017",
    "label": "Exhibit 10",
    "context": "Exhibit 10: May-26 70-city secondary ASP index was -0.3% mom (vs. -0.2% mom for Apr), and 10 cities (vs. 12 in Apr) recorded sequential ASP improvements in secondary markets Average 70 cities secondary ASP Index mom"
  },
  {
    "figure_id": "F193",
    "report_id": "R017",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Blended 2nd transaction ASP in Shanghai improved 3% mom in May-26, with broad-based improvements except for the lowest/highest-end categories Secondary performance by price range in Shanghai Exhibit 13: ASP in Beijing"
  },
  {
    "figure_id": "F194",
    "report_id": "R017",
    "label": "Exhibit 13",
    "context": "Exhibit 13: ASP in Beijing was -1% mom in May, with high-end products outperforming Secondary performance by price range in Beijing"
  },
  {
    "figure_id": "F195",
    "report_id": "R017",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Similarly, 2nd transaction ASP in Shenzhen rose 2% mom in May-26, driven by broad-based improvements across product types Secondary performance by price range in Shenzhen"
  },
  {
    "figure_id": "F196",
    "report_id": "R017",
    "label": "Exhibit 14",
    "context": "Exhibit 14: May-26 secondary listing volume in 100 cities continued to decline yoy (3nd consecutive month), yet at a slower pace compared to Apr, and inched up mom... Monthly secondary GFA sold in 15 key cities monitored by Centrali"
  },
  {
    "figure_id": "F197",
    "report_id": "R017",
    "label": "Exhibit 15",
    "context": "Exhibit 15: ...with yoy secondary supply balance declines recorded in both Tier-1 and lower tier cities Average secondary listing volume per city, by city tier"
  },
  {
    "figure_id": "F198",
    "report_id": "R017",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Online secondary home searching activities slightly moderated mom in May-26 Secondary home search demand heat index"
  },
  {
    "figure_id": "F199",
    "report_id": "R017",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Secondary housing transaction turnover pace marginally accelerated in May-26 Average number of days on listing, by city tier"
  },
  {
    "figure_id": "F200",
    "report_id": "R017",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Residential rental yield continued to improve in May-26 100 cities' residential rental yield vs. 30-yr Treasury yield and first-home mortgage rate"
  },
  {
    "figure_id": "F201",
    "report_id": "R017",
    "label": "Exhibit 19",
    "context": "Exhibit 19: 50 cities' average rent level trended lower in May-26... Average residential rent and mom in 50 cities monitored by CREIS"
  },
  {
    "figure_id": "F202",
    "report_id": "R017",
    "label": "Exhibit 20",
    "context": "Exhibit 20: ...while Tier-1 cities' rent on average achieved positive mom for three consecutive months, also outperforming May-24/-25 which both recorded negative mom Average residential rent and mom in 4 Tier-1 cities"
  },
  {
    "figure_id": "F203",
    "report_id": "R017",
    "label": "Exhibit 21",
    "context": "Exhibit 21: In May-26, our tracked six developers' new land acquisition spending was about 20% of their contract sales, on average carrying c.23% project-level GPM, with 95% exposure to Tier-1 & 2 cities and 78% exposure to Top-10 c"
  },
  {
    "figure_id": "F204",
    "report_id": "R018",
    "label": "Exhibit 2",
    "context": "Exhibit 2: NEV dealer discount trend"
  },
  {
    "figure_id": "F205",
    "report_id": "R018",
    "label": "Exhibit 3",
    "context": "Exhibit 3: ICE dealer discount trend"
  },
  {
    "figure_id": "F206",
    "report_id": "R019",
    "label": "Exhibit 1",
    "context": "Exhibit 1: In the primary market, the sequential decline in 70-city weighted average property price eased to 1.8% mom annualized in May"
  },
  {
    "figure_id": "F207",
    "report_id": "R019",
    "label": "Exhibit 2",
    "context": "Exhibit 2: The share of cities that experienced sequentially higher property prices edged up in primary markets but fell in secondary markets in May"
  },
  {
    "figure_id": "F208",
    "report_id": "R019",
    "label": "Exhibit 3",
    "context": "Exhibit 3: NBS 70-city secondary home prices continued to decline in May"
  },
  {
    "figure_id": "F209",
    "report_id": "R020",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Primary weekly unit sales and four-week moving average – Total 50 cities"
  },
  {
    "figure_id": "F210",
    "report_id": "R021",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: Global Registered Network Connections by Provider (Units) Global Registered Network Connections by Provider (Units)"
  },
  {
    "figure_id": "F211",
    "report_id": "R021",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: Global Interconnected Sites by Provider (Units)"
  },
  {
    "figure_id": "F212",
    "report_id": "R021",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Average and Median Networks by Facility by Provider (Units) Average and Median Networks by Facility by Provider (Units)"
  },
  {
    "figure_id": "F213",
    "report_id": "R021",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: Densest Global Interconnection Sites by Registered Network Count Densest Global Interconnection Sites by Registered Network Count"
  },
  {
    "figure_id": "F214",
    "report_id": "R021",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: Average Registered Network per Site by Provider (Units) Average Registered Network per Site by Provider (Units)"
  },
  {
    "figure_id": "F215",
    "report_id": "R021",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: Average Number of Providers by Category Per Interconnected Building (Units) EXHIBIT 8: AWS Cloud On-Ramps by Provider(Units, % of total provider locations) AWS Cloud On-Ramps by Provider (Units, % of total provider locat"
  },
  {
    "figure_id": "F216",
    "report_id": "R021",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: GCP Cloud On-Ramps by Provider (Units, % of total provider locations) GCP Cloud On-Ramps by Provider (Units, % of total provider locations)"
  },
  {
    "figure_id": "F217",
    "report_id": "R021",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: Azure Cloud On-Ramps by Provider(Units, % of total provider locations) Azure Cloud On-Ramps by Provider (Units, % of total provider locations)"
  },
  {
    "figure_id": "F218",
    "report_id": "R021",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: OCI Cloud On-Ramps by Provider (Units, % of total provider locations) OCI Cloud On-Ramps by Provider (Units, % of total provider locations)"
  },
  {
    "figure_id": "F219",
    "report_id": "R021",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: Neocloud Interconnect Presence by Provider (Units)"
  },
  {
    "figure_id": "F220",
    "report_id": "R021",
    "label": "EXHIBIT 13",
    "context": "EXHIBIT 13: EQIX Interconnection Revenue Overview (\\$M, %) EQIX Interconnection Revenue Overview ($M, %)"
  },
  {
    "figure_id": "F221",
    "report_id": "R021",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: DLR Interconnection Revenue Overview(\\$M, %) DLR Interconnection Revenue Overview ($M, %)"
  },
  {
    "figure_id": "F222",
    "report_id": "R021",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: Coresite Interconnection Revenue Overview (\\$M, %) Coresite Interconnection Revenue Overview ($M, %)"
  },
  {
    "figure_id": "F223",
    "report_id": "R021",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 16: Interconnection Count by Company (Thousands)"
  },
  {
    "figure_id": "F224",
    "report_id": "R021",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 17: Monthly Interconnection Price by Company (\\$)"
  },
  {
    "figure_id": "F225",
    "report_id": "R021",
    "label": "EXHIBIT 18",
    "context": "EXHIBIT 18: EQIX Monthly Interconnection Pricing (\\$) EQIX Monthly Interrconception Pricing (\\$)"
  },
  {
    "figure_id": "F226",
    "report_id": "R021",
    "label": "EXHIBIT 19",
    "context": "EXHIBIT 19: Interconnection Rev as % of Enterprise Revenue (%) Interconnection Rev as % of Enterprise Revenue (%)"
  },
  {
    "figure_id": "F227",
    "report_id": "R022",
    "label": "Figure 1",
    "context": "Figure 1: New increased TSF - May 2026"
  },
  {
    "figure_id": "F228",
    "report_id": "R022",
    "label": "Figure 2",
    "context": "Figure 2: New increased RMB loans - May 2026"
  },
  {
    "figure_id": "F229",
    "report_id": "R022",
    "label": "Figure 3",
    "context": "Figure 3: New increased deposit - May 2026 New increased deposit contributor"
  },
  {
    "figure_id": "F230",
    "report_id": "R022",
    "label": "Figure 4",
    "context": "Figure 4: Money supply vs TSF (%YoY growth)"
  },
  {
    "figure_id": "F231",
    "report_id": "R022",
    "label": "Figure 5",
    "context": "Figure 5: TSF outstanding and growth"
  },
  {
    "figure_id": "F232",
    "report_id": "R022",
    "label": "Figure 6",
    "context": "Figure 6: Loan growth vs. deposit growth"
  },
  {
    "figure_id": "F233",
    "report_id": "R022",
    "label": "Figure 7",
    "context": "Figure 7: M1 vs. M2"
  },
  {
    "figure_id": "F234",
    "report_id": "R027",
    "label": "Figure 1",
    "context": "Figure 1. Imported Sales by Brand in China (units) © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 2. May-26 and 5M26 YoY Growth of Imported Sales by Brand"
  },
  {
    "figure_id": "F235",
    "report_id": "R029",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Hyperscaler AI Capex"
  },
  {
    "figure_id": "F236",
    "report_id": "R029",
    "label": "Exhibit 3",
    "context": "Exhibit 3: New Loadings of Crude Oil/Condensate for export to China (Leading Indicator of Chinese Imports)"
  },
  {
    "figure_id": "F237",
    "report_id": "R029",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Observable Chinese Crude Oil Inventories China crude inventories (mln bbls)"
  },
  {
    "figure_id": "F238",
    "report_id": "R029",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Waha Natural Gas Prices (\\$/Mcf)"
  },
  {
    "figure_id": "F239",
    "report_id": "R029",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Data Center Behind-the-Meter Projects Data center developers are building their own power plants Data center developers have announced 90 GW of behind-the-meter projects, according to Cleanview's project tracker. Cumul"
  },
  {
    "figure_id": "F240",
    "report_id": "R029",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Announced Data Center Behind-the-Meter Capacity by State Announced behind-the-meter capacity by state Power capacity (MW)"
  },
  {
    "figure_id": "F241",
    "report_id": "R029",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Infrastructure Sector Benchmarks & Major Indices – Weekly Total Return"
  },
  {
    "figure_id": "F242",
    "report_id": "R029",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Infrastructure Sector Benchmarks & Major Indices – 2026 YTD Total Return"
  },
  {
    "figure_id": "F243",
    "report_id": "R029",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Midstream Energy Infrastructure – Weekly Total Return"
  },
  {
    "figure_id": "F244",
    "report_id": "R029",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Midstream Energy Infrastructure – 2026 YTD Total Return"
  },
  {
    "figure_id": "F245",
    "report_id": "R029",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Renewable Energy Infrastructure – Weekly Total Return"
  },
  {
    "figure_id": "F246",
    "report_id": "R029",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Renewable Energy Infrastructure – 2026 YTD Total Return"
  },
  {
    "figure_id": "F247",
    "report_id": "R029",
    "label": "Exhibit 22",
    "context": "Exhibit 22: MS Infrastructure Research Coverage 2027e EV/EBITDA 2027e EV/EBITDA"
  },
  {
    "figure_id": "F248",
    "report_id": "R029",
    "label": "Exhibit 24",
    "context": "Exhibit 24: MS Infrastructure Research Coverage 2027e Dividend Yield"
  },
  {
    "figure_id": "F249",
    "report_id": "R029",
    "label": "Exhibit 26",
    "context": "Exhibit 26: MS Midstream Energy Infrastructure Coverage 2027e FCF Yield"
  },
  {
    "figure_id": "F250",
    "report_id": "R029",
    "label": "Exhibit 23",
    "context": "Exhibit 23: MS Infrastructure Research Coverage 2027e Net Debt/EBITDA"
  },
  {
    "figure_id": "F251",
    "report_id": "R029",
    "label": "Exhibit 25",
    "context": "Exhibit 25: MS Infrastructure Research Coverage 2027e Total Cash Yield (Dividend + Share Buybacks)"
  },
  {
    "figure_id": "F252",
    "report_id": "R031",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Corporate tax rates fell from 1980s to 2020 Effective corporate tax rate. Historical constituents kept constant before year: 1989 (S&P 500), 1996 (FTSE 350), 2000 (SBF 120 and CDAX)"
  },
  {
    "figure_id": "F253",
    "report_id": "R031",
    "label": "Exhibit 2",
    "context": "Exhibit 2: The ‘Modern’ super cycle was characterised by lower volatility in macro variables Data for the US"
  },
  {
    "figure_id": "F254",
    "report_id": "R031",
    "label": "Exhibit 3",
    "context": "Exhibit 3: World trade growth has increased dramatically in the period of globalisation World merchandise imports plus exports, % of GDP"
  },
  {
    "figure_id": "F255",
    "report_id": "R031",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Global spending on defence trended downwards during the ‘Modern’ super cycle World military spending (as a share of GDP)"
  },
  {
    "figure_id": "F256",
    "report_id": "R031",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Labour share declines as profit share dominates in the 21st century Profits and wages as shares of GDP (%) - US"
  },
  {
    "figure_id": "F257",
    "report_id": "R031",
    "label": "Exhibit 6",
    "context": "Exhibit 6: While the economic recovery from the financial crisis was weaker than average... Real US GDP following the end of a recession. Indexed to 100. Average = 9 episodes since 1950 excluding the 2020 episode"
  },
  {
    "figure_id": "F258",
    "report_id": "R031",
    "label": "Exhibit 7",
    "context": "Exhibit 7: ... the opposite was true for financial markets SPX since the trough preceding the end of a recession. Indexed to 100. Average = 9 episodes since 1950 excluding the 2020 episode"
  },
  {
    "figure_id": "F259",
    "report_id": "R031",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Top-line growth has been falling along with declining nominal GDP yoy sales growth (10y rolling average), Market ex Financials (USD)"
  },
  {
    "figure_id": "F260",
    "report_id": "R031",
    "label": "Exhibit 9",
    "context": "Exhibit 9: The performance of growth assets reflected fundamentally stronger profit growth 12m trailing EPS (USD). Indexed to 100 in January 2009"
  },
  {
    "figure_id": "F261",
    "report_id": "R031",
    "label": "Exhibit 10",
    "context": "Exhibit 10: The technology industry enjoyed a strong acceleration in ROE 12-month forward ROE (%)"
  },
  {
    "figure_id": "F262",
    "report_id": "R031",
    "label": "Exhibit 11",
    "context": "Exhibit 11: US consistently outperformed other equity markets, and technology was the strongest driver of returns by sector Relative price performance (in USD)"
  },
  {
    "figure_id": "F263",
    "report_id": "R031",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Real yields have contributed meaningfully to the rise in longer-term nominal forwards after the pandemic Nominal yields by component since 1-Sep-21"
  },
  {
    "figure_id": "F264",
    "report_id": "R031",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Limit to the new cycle: debt has risen Government debt as a percentage of GDP. Dotted lines are GIR Economics forecasts"
  },
  {
    "figure_id": "F265",
    "report_id": "R031",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Only a few years ago, German and Japanese 30-year bonds enjoyed a zero (or close to zero) interest rate 30-year government bond benchmark yields (%)"
  },
  {
    "figure_id": "F266",
    "report_id": "R031",
    "label": "Exhibit 15",
    "context": "Exhibit 15: The US administration has increased tariffs to levels not seen since 1930s US Effective Tariff Rate (Customs Revenue as a Share of Goods Imports) (%)"
  },
  {
    "figure_id": "F267",
    "report_id": "R031",
    "label": "Exhibit 16",
    "context": "Exhibit 16: We have observed a rising trend of government intervention and restrictions to trade By year of implementation, globally"
  },
  {
    "figure_id": "F268",
    "report_id": "R031",
    "label": "Exhibit 17",
    "context": "Exhibit 17: A multi-year high in policy uncertainty Headline Policy Uncertainty Index - Baker, Bloom, Davis"
  },
  {
    "figure_id": "F269",
    "report_id": "R031",
    "label": "Exhibit 18",
    "context": "Exhibit 18: The emergence of large language models has spawned a renewed requirement for capital spending Capex as a % of cash flow from operations, dashed line represents 2026 consensus"
  },
  {
    "figure_id": "F270",
    "report_id": "R031",
    "label": "Exhibit 19",
    "context": "Exhibit 19: After the financial crisis, long duration Growth saw the highest returns, while ‘old economy’, real assets and Value lagged Total return performance in local currency - where applicable"
  },
  {
    "figure_id": "F271",
    "report_id": "R031",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Gold, Emerging Markets, Topix, and Value have performed best since 2025 Total return performance in local currency - where applicable % change in 2025 - today"
  },
  {
    "figure_id": "F272",
    "report_id": "R031",
    "label": "Exhibit 21",
    "context": "Exhibit 21: A pattern of reversal can be seen when comparing the decade after the financial crisis with the period post the pandemic Total return performance (annualised) - World sectors and styles"
  },
  {
    "figure_id": "F273",
    "report_id": "R031",
    "label": "Exhibit 22",
    "context": "Exhibit 22: AI hyperscalers are expected to spend c.\\$755 billion on capex in 2026 Hyperscaler annual capex (\\$bn)"
  },
  {
    "figure_id": "F274",
    "report_id": "R031",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Chip manufacturers appear to have benefited from AI capex, while investors have questioned the hyperscalers' return on capex Relative price performance of US hyperscalers (AMZN, META, GOOGL, MSFT, ORCL) versus MSCI USA S"
  },
  {
    "figure_id": "F275",
    "report_id": "R031",
    "label": "Exhibit 24",
    "context": "Exhibit 24: Innovation in agentic AI has raised concerns about disruption to software business models Relative price performance of US hyperscalers (AMZN, META, GOOGL, MSFT, ORCL) versus MSCI USA Software & Services"
  },
  {
    "figure_id": "F276",
    "report_id": "R031",
    "label": "Exhibit 24",
    "context": "Exhibit 25: Kodak invented the first digital camera in 1975 but filed for bankruptcy in 2012 Stock price indexed to its maximum"
  },
  {
    "figure_id": "F277",
    "report_id": "R031",
    "label": "Exhibit 26",
    "context": "Exhibit 26: Polaroid had a monopoly in the instant photography market Stock price indexed to its maximum"
  },
  {
    "figure_id": "F278",
    "report_id": "R031",
    "label": "Exhibit 27",
    "context": "Exhibit 27: Long duration growth companies such as tech names recently derated Premium/(discount) on 12m forward P/E vs. World ex. TMT. Global Sectors"
  },
  {
    "figure_id": "F279",
    "report_id": "R031",
    "label": "Exhibit 28",
    "context": "Exhibit 28: The fortunes of the virtual and physical worlds have become intertwined for the first time since the rollout and commercialisation of the Internet Asset-heavy vs. asset-light indexed performance - US stocks"
  },
  {
    "figure_id": "F280",
    "report_id": "R031",
    "label": "Exhibit 29",
    "context": "Exhibit 29: In countries such as Germany, defence spending is ramping up German defence orders by region of origin (EUR bn)"
  },
  {
    "figure_id": "F281",
    "report_id": "R031",
    "label": "Exhibit 30",
    "context": "Exhibit 30: The median stock in each region has experienced smaller returns this year Price return in 2026; local currency (APxJ in USD)"
  },
  {
    "figure_id": "F282",
    "report_id": "R031",
    "label": "Exhibit 31",
    "context": "Exhibit 31: The valuation premium of CAPEX beneficiaries remains tightly linked to Developed Markets' capex-to-sales ratio Relative valuation"
  },
  {
    "figure_id": "F283",
    "report_id": "R031",
    "label": "Exhibit 33",
    "context": "Exhibit 32: The performance of CAPEX Beneficiaries tends to lead the global capex cycle by several quarters Relative performance y/y"
  },
  {
    "figure_id": "F284",
    "report_id": "R031",
    "label": "Exhibit 33",
    "context": "Exhibit 33: Earnings growth of CAPEX Beneficiaries is closely correlated with global CAPEX y/y change in EPS"
  },
  {
    "figure_id": "F285",
    "report_id": "R031",
    "label": "Exhibit 35",
    "context": "Exhibit 35: Performance since 2025 of indexes and baskets exposed to global capex expansion Performance since 2025, local currency (USD for Asia ex. Japan) - ICB Sector for Semis; regional GS baskets for Power, Defense and Capital I"
  },
  {
    "figure_id": "F286",
    "report_id": "R034",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: Distinction between Liquid-to-Air and Liquid-to-Liquid CDUs ```mermaid graph TD subgraph L2A"
  },
  {
    "figure_id": "F287",
    "report_id": "R034",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: Project Brazos Overview What exactly is Google Brazos? ```mermaid graph TD"
  },
  {
    "figure_id": "F288",
    "report_id": "R034",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Brazos L2A CDU specs. seem to target inference in OCP compliant environments L2A Product comparison of Brazos vs. peers"
  },
  {
    "figure_id": "F289",
    "report_id": "R034",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: McKinsey and Co. Estimates of GW add by category Global data center demand by workload, 2025–30, gigawatts"
  },
  {
    "figure_id": "F290",
    "report_id": "R034",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: Recap: How does Liquid Cooling work? ```mermaid graph TD"
  },
  {
    "figure_id": "F291",
    "report_id": "R035",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Banks' product rate hikes reflecting BOJ policy rate hike Exhibit 3: Topix banks' share price performance in 30 days before and after previous rate hikes"
  },
  {
    "figure_id": "F292",
    "report_id": "R037",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Relative share performance: Tankers"
  },
  {
    "figure_id": "F293",
    "report_id": "R037",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Tanker Spot Earnings have corrected mildly since May 2026"
  },
  {
    "figure_id": "F294",
    "report_id": "R037",
    "label": "Exhibit 3",
    "context": "Exhibit 3: US oil inventory (including SPR)"
  },
  {
    "figure_id": "F295",
    "report_id": "R037",
    "label": "Exhibit 4",
    "context": "Exhibit 4: OPEC crude oil production"
  },
  {
    "figure_id": "F296",
    "report_id": "R037",
    "label": "Exhibit 5",
    "context": "Exhibit 5: 20% of crude tankers are \"sanctioned\", 24% of global tankers are \"non-compliant\""
  },
  {
    "figure_id": "F297",
    "report_id": "R037",
    "label": "Exhibit 6",
    "context": "Exhibit 6: China crude imports have been decreasing since April 2026"
  }
]