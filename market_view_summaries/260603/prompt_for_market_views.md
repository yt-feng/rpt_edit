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
    "title": "瑞士手表出口暴跌16.6%：关税扭曲下的数据噪音，掩盖了真正的复苏信号",
    "digest": "[wechat_article.md]\n# 瑞士手表出口暴跌16.6%：关税扭曲下的数据噪音，掩盖了真正的复苏信号\n\n4月瑞士手表出口同比下滑16.6%，这个数字足以让任何关注奢侈品行业的投资者心头一紧。但如果你只看这个标题就得出“全球奢侈品需求崩塌”的结论，很可能犯了方向性错误。\n\n这份来自投行研报的核心判断是：当前出口数据的剧烈波动，本质上是关税政策引发的基数效应扭曲，而非终端需求的实质性恶化。真正值得关注的，不是4月单月数据本身，而是隐藏在噪音之下的三个结构性信号——美国市场在剔除关税扰动后的韧性、大中华区企稳的底部形态，以及中东地缘政治风险对奢侈品行业新增长极的威胁。\n\n报告指出，4月出口同比跌幅较3月的-6%（经工作日调整）显著扩大，而2月还是+9.2%的正增长。这种过山车式的波动，恰恰印证了贸易政策对供应链节奏的深度干扰。去年4月，在“解放日”关税生效前，大量手表被提前发往美国，形成了极高的同比基数。今年4月对美出口暴跌56.4%，正是这个基数的消化过程。如果以2024年为基准，美国市场4月仍录得+8.9%的增长，虽然较1季度的+12.1%略有放缓，但远非崩溃。\n\n**市场真正低估的不是需求，而是数据噪音对判断力的系统性扭曲。**\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 关税扰动正在制造一个“虚假的衰退”，但美国消费者已经消化了价格冲击\n\n对美出口的剧烈波动是4月数据的核心变量。去年4月的抢运潮将出口基数推高至异常水平，今年自然面临同比回撤。但报告特别强调了一个关键细节：公司层面的反馈显示，美国消费者已经“在沉默中消化”了关税带来的涨价。\n\n这意味着什么？意味着奢侈品公司担心的需求价格弹性断裂并未发生。高端腕表的核心客群，其消费决策对价格变动的敏感度远低于大众消费品。这一现象与过去几个季度奢侈品公司在美国市场的整体表现一致——美国仍然\n\n[... middle omitted ...]\n\n500位产业决策者和投资人，一起在数据噪音中寻找真正的信号。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n瑞士手表出口4月骤降16.6%\n\n📉 关税扰动，数据失真\n\n4月瑞士手表出口同比跌16.6%，比3月的-6%明显恶化。但别急着下结论，这背后是关税抢跑导致的基数效应。\n\n1️⃣ **美国市场大跳水**\n对美出口暴跌56.4%，是整体下滑的主因。原因是去年4月美国加征“解放日”关税前，大量订单抢跑发货，推高了对比基数。如果跟2024年比，4月对美出口其实还是+8.9%的正增长。\n\n2️⃣ **大中华区稳住了**\n对香港（+13.5%）和中国内地（+17.1%）都录得双位数增长。同样有低基数因素——去年4月发货被优先调往美国。跟2024年比，仍低约15%，和一季度趋势一致。\n\n3️⃣ **其他区域分化明显**\n法国大涨46.3%，但研报判断更像是中转贸易而非本地需求。中东全线下跌，阿联酋-9.5%、沙特-17.3%、卡塔尔-12%，区域冲突影响在显现。\n\n4️⃣ **价格段表现：全靠基数**\n只有200-500瑞郎区间微增+7.7%，因为去年基数最弱。3000+瑞郎的高端表跌幅最大-19%，去年正好是+19.8%的高基数。\n\n整体来看，瑞士手表需求处于缓慢复苏轨道。中国稳步改善，美国消费者似乎消化了关税带来的涨价\n\n[... middle omitted ...]\n\nb39ce4c68b96a22667e8895a027e2cbf.jpg)\n\nYi-Peng Khoo, CFA\n\n+44 20 7676 6822\n\nyi-peng.khoo@bernsteinsg.com\n\n# Specialist Sales\n\n![](images/4e4d6a0db5c447fae7aecf98ce97fde5e9d5fcde80128b798249ff8\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R002",
    "title": "市场低估的不是波动，而是期权偏斜信号在利率市场中的结构性价值",
    "digest": "[wechat_article.md]\n# 市场低估的不是波动，而是期权偏斜信号在利率市场中的结构性价值\n\n利率市场参与者正在面对一个令人困惑的局面：通胀叙事尚未终结，地缘冲突此起彼伏，政策路径的可见度极低。在这样的环境中，大多数投资者本能地转向了更短的久期、更频繁的调仓、更依赖宏观叙事来形成判断。但一份来自某外资投行利率策略团队的研报提出了一个值得深思的相反观点——真正被市场低估的，不是对波动率本身的定价，而是期权偏斜（skew）作为一种独立信号，在利率方向性交易中的结构性预测能力。\n\n这份报告的核心判断是：短期期权偏斜的变化，在长达17年的历史回测中，始终包含关于未来利率走势的预测信息，且这一关系在2019年之后不仅没有消失，反而在长端利率上变得更强。这不是一个样本内的偶然发现，而是一个经过120种参数组合压力测试后仍然成立的规律。\n\n为什么这一点对当前市场尤其重要？因为当宏观冲击成为常态，传统的久期管理框架容易陷入“追着新闻跑”的被动状态。而偏斜信号提供了一种不同的视角——它不依赖对通胀或就业数据的预测，而是捕捉市场参与者通过期权市场表达出来的、对尾部风险的真实定价变化。这种变化往往领先于现货市场的方向性调整。\n\n报告通过三个层次来验证这一主张：信号在不同参数设定下的稳健性、在不同市场阶段的表现分化、以及信号衰减的速度。以下是我们从中提炼出的关键洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 偏斜信号的预测能力并非数据挖掘的产物，而是市场行为的真实映射\n\n任何量化策略最容易被质疑的问题就是“过拟合”。报告对此做了非常扎实的处理：它没有去寻找一个最优参数组合，而是系统地测试了4种回溯窗口、3种期权期限、10种交易延迟，共计120种规格。结果发现，无论使用互换还是国债期货来表达久期暴露，无论选择1个月、3个月还是6个月的期权期限，偏斜信号的表现\n\n[... middle omitted ...]\n\n下的详细表现数据，以及我们自己对当前偏斜信号状态的独立判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n利率市场一个被忽视的信号：偏斜\n\n📊利率市场的“偏斜”信号\n\n这个信号在2009年至今都有效，2019年后表现更突出。\n\n1️⃣ 什么是偏斜信号？\n- 期权市场的偏斜（skew）变化，能预测利率走势\n- 信号在1个月、3个月、6个月到期期权上都有效\n- 不是特定工具的偶然现象\n\n2️⃣ 信号有多靠谱？\n- 2009年至今保持预测能力\n- 信号信息需要几天才能完全反映到价格中\n- 21天回看窗口表现最稳定\n\n3️⃣ 2019年后的变化\n- 2年期利率：信号变弱，宏观冲击主导\n- 30年期利率：信号变强，持仓因素更重要\n- 市场变化速度加快，快速信号优于慢速信号\n\n4️⃣ 当前信号指向\n- 曲线整体指向短久期\n- 偏斜进一步加深，即使起点已经很高\n\n市场的关键变化不是信号失效，而是变化节奏更快了。\n\n你觉得这个信号在现在的市场环境下还有效吗？欢迎一起讨论。\n\n#学习笔记\n\n[source_mineru.md]\n# US Rates Strategy | North America\n\n# Skew: A Robust Signal in a Changing Market\n\nWe show that the ske\n\n[... middle omitted ...]\n\non is expressed through swaps or Treasury futures, and across short-dated expiries.   \nThe signal retains predictive power back to at least 2009. Since 2019, faster signals have outperformed a\n\n[... middle omitted ...]\n\nuthors are Fixed Income Research Analysts/Strategists and are not opining on or expressing recommendations on equity securities: Aryaman Singh; Shaun Zhou; Eli P Carter; Matthew Hornbach; Martin W Tobias, CFA.\n\n© 2026 MS"
  },
  {
    "id": "R003",
    "title": "五月PMI回落至荣枯线，市场真正担心的不是增长放缓，而是价格传导断裂",
    "digest": "[wechat_article.md]\n# 五月PMI回落至荣枯线，市场真正担心的不是增长放缓，而是价格传导断裂\n\n五月的中国制造业PMI数据，以精确的50.0画下一条分界线。这不仅仅是从扩张到收缩的临界点，更是一个信号：过去几个月由上游价格上涨驱动的经济叙事，正在遭遇下游需求的真实检验。\n\n某外资投行最新发布的研报指出，五月官方制造业PMI较四月回落0.3个百分点，恰好落在荣枯线上。表面上看，这似乎只是经济复苏节奏的暂时放缓。但拆解分项数据后，一个更值得警觉的图景浮现出来：价格上涨的压力开始从上游传导至中游，但下游需求的承接能力正在减弱。这不是简单的供需错配，而是一轮潜在的价格-需求负反馈循环正在酝酿。\n\n对于关注中国资产定价的投资者而言，五月PMI数据最核心的信息不是增长动能衰减，而是价格传导机制出现裂痕。这个判断，将直接影响我们对下半年政策节奏、行业利润分配以及资产配置逻辑的重新评估。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 生产与订单的缺口在扩大，这才是真正的需求信号\n\n五月PMI最值得关注的变化，不是总量数字回落至50，而是生产指数与新订单指数之间的裂口在扩大。\n\n生产指数录得51.2，虽然较四月回落0.3个百分点，但依然稳稳站在扩张区间。这意味着制造业企业仍在积极组织生产，供给端没有出现明显的主动收缩。然而，新订单指数从四月的50.6大幅下滑至49.9，五个月来首次跌破荣枯线。更令人警惕的是新出口订单指数，单月骤降1.7个百分点至48.6。\n\n这两个数字放在一起，揭示了一个关键事实：生产跑在了需求前面，而且差距正在拉大。企业仍在按过去的订单节奏安排生产，但新订单的流入速度已经放缓。这种“生产惯性”与“需求冷却”之间的时间差，正是库存被动累积的典型前兆。\n\n对于投资者而言，这个信号的含义是明确的。过去几个季度，市场对中国制造业的乐观情绪\n\n[... middle omitted ...]\n\n可以围绕这份报告的完整图表和原始数据，展开更具操作性的推演。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月PMI回到50，涨价拖累需求\n\n涨价传导，需求端承压\n\n5月制造业PMI从4月的50.3回落到50.0，刚好卡在荣枯线上。投行研报认为，核心原因是涨价正在拖累终端需求。三个信号：\n\n1️⃣ 订单弱于生产\n生产指数51.2，还在扩张区，但新订单指数降到49.9，是5个月来首次跌破50。新出口订单更是跌到48.6。生产跑在需求前面，差距在拉大。\n\n2️⃣ 成本涨得比售价快\n原材料购进价格指数60.5，出厂价格指数51.9，两者差距连续5个月没缩小。企业被夹在中间，利润被压缩，已经开始影响采购和生产决策。\n\n3️⃣ 上游库存降，成品库存升\n原材料库存降到48.6，但产成品库存升到49.3。企业在涨价压力下减少采购，同时下游销售不畅导致库存积压。方向值得注意。\n\n好消息是服务业PMI回到50.1，信息技术、金融、交通都高于55。但建筑业还在48.8，显示投资端可能持续疲弱。\n\n高频数据也印证：钢价4月底开始涨，锌价跟涨，油价影响在扩散。政府债券发行虽然5月加速，但前5个月累计仍比去年少5000亿。\n\n从历史看，PMI回到50往往对应名义GDP增速在3-4%区间，经济处于弱平衡状态。\n\n#学习笔记\n\n[source\n\n[... middle omitted ...]\n\nApril. We believe this primarily reflects the adverse impact of rising prices on end-demand. Three observations support this reading.\n\nFirst, orders are weaker than production. The production \n\n[... middle omitted ...]\n\n000</td><td>DB Securities Inc.The DB Center1 Columbus CircleNew York, NY 10019Tel: (1) 212 250 2500</td><td>DB AGFiliale SingapurOne Raffles Quay, South TowerSingapore 048583Tel: (65) 6423 8001</td><td></td></tr></table>"
  },
  {
    "id": "R004",
    "title": "市场真正低估的不是需求，而是供给侧的再定价",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是需求，而是供给侧的再定价\n\n这份某外资投行最新发布的Q1财报季分析报告，表面上看是在回答“企业盈利还能撑多久”，但细读下来，它真正揭示的是一组被市场定价忽略的结构性矛盾：消费者现金流的底层逻辑正在被改写，而AI投资的规模已经大到足以独立影响宏观经济账户中的资本形成。这两个方向的力量并不对冲，但它们对资产定价的含义截然不同。\n\n报告覆盖了几乎所有标普500成分股，数据截止日接近完整。其核心判断可以浓缩为一句话：当前的经济韧性建立在两个脆弱支点之上——低储蓄率支撑的消费和超大规模企业主导的AI资本开支。前者面临油价、财政退坡和收入增速下滑的三重挤压，后者则几乎没有受到地缘风险的干扰，反而在加速。\n\n这不是一份“乐观”或“悲观”的报告，而是一份关于“分化正在加剧”的报告。对于产业决策者和资产配置者而言，真正需要理解的问题不是经济会不会衰退，而是哪些部门正在被重新定价，以及这种重新定价的逻辑是否已经被市场消化。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 消费的韧性来自结构性透支，而非基本面改善\n\n财报数据显示，Q1消费者相关企业的营收增长依然强劲：标普500可选消费板块中位数公司营收同比增长9%，必需消费板块也达到5%。从官方统计和替代数据来看，名义消费支出增速在过去几个月保持稳定。\n\n但这份报告真正有价值的洞察不在于这些表面数字，而在于它对消费现金流的底层拆解。报告明确指出，当前的消费韧性建立在一个不可持续的基础之上：个人储蓄率处于低位，实际可支配收入在4月个人收入报告中同比下降了1.1%。这意味着消费者正在动用储蓄来维持支出节奏，而不是因为收入增长在加速。\n\n报告预测2026年下半年的实际消费支出增速仅为1.3%，显著低于市场一致预期。这个数字的背后是三个结构性因素的叠加：高油价对实际购买力\n\n[... middle omitted ...]\n\n信群继续讨论这些未完的问题，一起追踪上述三个信号的实际演变。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nQ1财报季：韧性背后有隐忧\n\n韧性背后，暗流涌动\n\n消费数据亮眼，但企业已在小心预警\n\n刚看完某外资投行最新研报，Q1财报季的核心信息：企业营收增速强劲，但管理层对未来越来越谨慎。\n\n1️⃣ 消费依然有支撑\n- 标普500实际营收（剔除能源）同比增长6.3%，创2021年以来最快\n- 可选消费和必需消费公司销售额中位数分别增长9%和5%\n- 但企业管理层对消费者信心的量化指标已开始回落\n\n2️⃣ 通胀压力正在传导\n- 企业价格公告指数升至2023年底以来最高\n- 成本上涨主要集中在：油价、航运、树脂材料、计算机存储\n- 分析师已下调Q2利润率预期，成本压力最大的板块下调幅度也最大\n\n3️⃣ 消费者现金流承压\n- 个人储蓄率偏低，实际可支配收入同比下降1.1%\n- 研报预计2026下半年实际消费增速仅1.3%，低于市场共识\n- 低收入群体受汽油价格上涨的冲击更大，预计影响其全年实际收入增速1.25个百分点\n\n4️⃣ AI投资依然火热\n- 超大规模企业资本支出预期再次上调，从2025年的约7500亿美元增长83%\n- AI相关支出对整体商业固定投资的拉动约3个百分点\n- 但AI对劳动力市场的影响仍有限，目前主要在\n\n[... middle omitted ...]\n\nte the Iran war and jump in oil prices but voiced concern about the near-term outlook. We expect below-consensus real consumer spending growth of just $1.3\\%$ in 2026H2, reflecting the poor st\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R005",
    "title": "航空航天与防务：市场真正低估的不是需求，而是供给端的结构性重塑",
    "digest": "[wechat_article.md]\n# 航空航天与防务：市场真正低估的不是需求，而是供给端的结构性重塑\n\n过去一周，某外资投行在纽约举办的战略决策会议上，与十二家航空航天与防务公司的CEO进行了密集交流。参会者覆盖了从波音、GE Aerospace到Anduril、L3Harris等商业航空与防务领域的核心玩家。会后发布的一份研报，表面上是对CEO观点的汇总，但深挖下去，它揭示了一个远比短期订单波动更重要的结构性判断：行业正在经历的不是一次周期性的需求起伏，而是供给端——从供应链结构、生产模式到竞争格局——的深层重构。市场当前的定价，可能更多反映了对需求端的担忧或乐观，却尚未充分消化供给端正在发生的、不可逆的变化。\n\n这份报告的价值，不在于告诉读者“航空需求依然强劲”或“防务预算存在不确定性”这类已知信息。它的真正洞察在于，通过十二位CEO的口径，勾勒出了供给端几个同步发生、相互强化的趋势：商业航空领域，售后市场与OE生产同时高负荷运转，正在考验供应链的极限；防务领域，导弹需求的爆发式增长催生了全新的生产框架和合同模式；而Anduril等新进入者的崛起，则从根本上挑战了传统防务承包商的成本结构与交付速度。这些趋势叠加在一起，意味着行业龙头公司的竞争优势、盈利能力和估值逻辑都在被重新定义。\n\n以下是我们从这份报告中提炼出的五个核心洞察。它们不是对报告内容的复述，而是试图回答一个更根本的问题：这些CEO的集体声音，究竟在告诉我们哪些市场尚未完全定价的变化？\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 商业航空的真正压力点不在需求端，而在OE与售后市场同时高负荷运转下的供应链极限\n\n报告中最容易被忽略的一个信息是，所有商业航空公司的CEO都表示，尽管燃油价格高企对航空公司盈利构成压力，但他们尚未看到任何需求疲软的迹象。售后市场的订单簿已经覆盖了未来12\n\n[... middle omitted ...]\n\n航空航天与防务板块的结构性变化，这里应该能给你一些新的视角。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n12位CEO聊透：航太防务新信号\n\n航太防务趋势速览\n\n3天对话，12家CEO，关键信号都在这\n\n上周某外资投行在纽约办了场战略决策会议，一口气请了12家航太防务公司的CEO。从Anduril到波音，从洛马到RTX，信息量很大。我帮你提炼了几个核心逻辑：\n\n**1/ 商用航太：后市场依然坚挺**\n所有商用航太公司都表示，虽然油价高企影响航司利润，但后市场需求还没看到放缓信号。如果高油价持续，可能会影响航电升级、内饰等非刚性支出，但2026年业绩基本不受影响。\n\n波音确认737月产47架的目标夏季可达，CEO还透露未来可能到52、57甚至63架。787年底目标月产10架。供应商库存正在下降，交付与生产更同步了。\n\n但空客A350提速比预期慢，与近期公开说法一致。\n\n发动机后市场订单已经覆盖12-18个月，新机型更久。但OE与后市场同时增长，供应链压力不小。\n\n**2/ 防务：2027预算仍不确定，但方向明确**\n所有防务公司都预期预算会涨，但没人敢打包票能到1.5万亿美元。导弹和导弹防御最热，计划5-7年内产能翻3-4倍，合同还带补偿条款。\n\n固体火箭发动机供应商（L3Harris、诺格、Anduril）都在扩\n\n[... middle omitted ...]\n\nst Sales\n\n![](images/c8309e70881b0b5f33ff06998a43d1697806bec18c46974a32a6f0a2375a4e38.jpg)\n\nSteve Song\n\n+1 917 344 8401\n\nsteve.song@bernsteinsg.com\n\nLast week, we hosted twelve Aerospace & Def\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R006",
    "title": "大宗商品市场正在经历的不是波动，而是定价权的结构性转移",
    "digest": "[wechat_article.md]\n# 大宗商品市场正在经历的不是波动，而是定价权的结构性转移\n\n过去一周，全球大宗商品期货市场的持仓总估值下降了690亿美元，至1.82万亿美元。表面上看，这是一次由能源价格下跌和黄金资金外流共同触发的市场回调。但这份来自某外资投行的研报揭示了一个更值得关注的信号：市场正在从“宏观叙事驱动”向“微观供给结构重定价”切换。真正重要的不是价格涨跌了多少，而是哪些资产在资金流出时仍然吸引了增量资金，哪些市场在价格下跌的同时持仓结构发生了质变。\n\n这份报告最核心的判断可以概括为一句话：大宗商品市场的下一轮机会，不在于押注通胀或衰退的方向，而在于识别那些供给端已经发生不可逆结构性变化的品种。能源市场正在经历需求预期的修正，但LNG的供给弹性正在耗尽；黄金的资金流出掩盖了基本金属中铜的逆势流入；农产品则陷入了持仓稳定但价格信号分化的“假性平衡”。这些信号叠加在一起，指向一个结论：当前的市场定价，低估了结构性供给约束对部分品种的长期支撑，也高估了宏观情绪对整体资产类别的统摄力。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 能源市场的下跌不是需求崩溃，而是中国需求结构的永久性调整\n\n过去一周，能源市场持仓总估值下降560亿美元，至8160亿美元，布伦特和WTI原油价格分别下跌11%和10%。市场容易将这一跌幅解读为全球需求放缓的信号，但报告提供了一个更细致的视角：中国石油需求下降了9%，但背后的经济活动的下降幅度有限。这意味着，中国石油需求的下降并非周期性的需求萎缩，而是一次结构性的消费模式转变——汽油、柴油和燃料油的需求损失中有相当一部分将是永久性的，而航空燃油和石脑油的需求则会大致恢复。\n\n这一判断的含义是深远的。市场目前对原油的定价，仍然隐含了一个假设：中国需求将在经济复苏后回到趋势线。但如果中国石油需求的结构性下降已成定\n\n[... middle omitted ...]\n\n每周更新关键跟踪指标，并讨论市场定价中尚未被充分反映的变量。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n大宗商品持仓一周速览\n\n商品持仓降温，黄金流出明显\n\n最近一周，商品市场整体在降温。跟踪的全球商品期货未平仓合约总值降至1.82万亿美元，比上周缩了4%，主要原因是能源价格走弱（美国天然气除外）和黄金市场流出220亿美元。\n\n**1. 能源：跌得最猛**\n- 原油领跌：布伦特跌11%，WTI跌10%，净多头从610亿降至510亿美元。\n- 天然气：欧洲和亚洲基准价格下跌，但美国天然气逆势上涨。\n- 一个有意思的观察：某外资投行估算，全球LNG市场已吸收了约60%的霍尔木兹海峡供应冲击（来自北美和非洲的新项目），但灵活性正在消退，欧洲库存低于均值，预计价格将在注气季走高。\n\n**2. 贵金属：黄金连续三周流出**\n- 黄金是重灾区：所有交易者类型的净合约流出达220亿美元，但有意思的是，COMEX黄金的Managed Money净多头反而增加了3900手。\n- 全球黄金ETF持仓目前4131吨，YTD仍为正增长（+3%），尽管4-5月又经历了一波抛售。\n\n**3. 基本金属：铜逆势吸金**\n- 铜市场净流入23亿美元，抵消了铝和锌的流出。\n- 锌：供应中断持续，需求依然疲软，但预计锌价将维持在3400-3500\n\n[... middle omitted ...]\n\npotentially increases pressure on the Fed to tighten, but expectations for a mix of easing and stability elsewhere have shifted to a projection for a broad but shallow global tightening cycle \n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 02 Jun 2026 07:12 PM BST\n\nDisseminated 02 Jun 2026 07:12 PM BST"
  },
  {
    "id": "R007",
    "title": "市场真正低估的不是需求放缓，而是出口收缩对定价权的挤压",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是需求放缓，而是出口收缩对定价权的挤压\n\n5月PMI数据已经全部落地。无论是国家统计局发布的官方PMI，还是某外资投行追踪的RatingDog PMI，都指向同一个方向：制造业扩张仍在继续，但速度明显放缓。这个结论本身并不令人意外，一季度超预期的增长之后，市场对二季度自然有回落的心理准备。\n\n但真正值得关注的，不是扩张放缓这个事实，而是放缓的结构性特征——以及这些特征对下半年资产定价意味着什么。\n\n这份报告的核心判断是：当前PMI读数所反映的，不是一次温和的周期性回调，而是一个正在发生的结构性切换——从内需驱动转向外需承压，从成本传导转向利润挤压。市场对后者的定价可能仍然不足。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 出口订单跌破荣枯线，这是一季度增长动能最直接的威胁\n\n5月RatingDog PMI中的新出口订单指数从51.1降至49.6，直接跌入收缩区间。这不是一个孤立的信号。国家统计局PMI中的新出口订单同样下行，从50.3降至48.6。两组数据指向同一个事实：外部需求正在走弱。\n\n报告明确指出，这与航运数据以及最新的官方PMI读数一致。一季度出口对经济增长的拉动作用非常显著，但5月的数据暗示，这个引擎可能正在减速。更关键的是，出口订单的收缩不是边际性的——1.5个点的月度降幅，在PMI体系中已经属于比较显著的变化。\n\n这意味着什么？对于依赖出口的制造业企业来说，二季度末到三季度可能面临一个双重压力：一方面是订单量的收缩，另一方面是价格传导能力的减弱。那些在一季度受益于海外补库需求的行业，可能需要重新评估下半年的营收预期。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 价格压力在缓解，但缓解的方式对利润并不友好\n\n5月的一个积极信号是通\n\n[... middle omitted ...]\n\n整报告原文及相关图表已同步上传，可以结合数据做更深入的分析。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n制造业PMI小幅回落，但仍在扩张区间\n\n📊 5月数据怎么看\n\n5月制造业PMI录得51.8，环比回落0.4，但已连续6个月站在扩张线上。生产端依然稳健，出口开始出现压力。\n\n1️⃣ 生产端：扩张节奏放缓，但动能还在\n产出PMI从53.8微降至53.4，仍处于较高水平。未来产出预期虽从55.7降至55.0，但整体信心不弱。五一假期和出口放缓是主要拖累因素。\n\n2️⃣ 出口：新出口订单跌破荣枯线\n新出口订单从51.1降至49.6，与官方PMI数据趋势一致。外部需求走弱，一季度亮眼的出口增速可能面临逆风。\n\n3️⃣ 价格：通胀压力边际缓解，但成本端仍承压\n投入价格从57.5降至55.8，产出价格从53.6降至52.0。中东局势虽有所缓和，但能源价格和供应链扰动仍在推高成本，且上下游价格涨幅不对称，企业利润空间受挤压。\n\n4️⃣ 就业：连续两个月低于50\n就业指数49.8，微降0.1，延续收缩态势。\n\n整体来看，5月制造业扩张速度放缓，但未失速。出口是当前最大的不确定性，而企业端对新产品、技术突破和产能扩张仍抱有信心。\n\n大家怎么看下半年出口走势？欢迎一起讨论。\n\n#学习笔记\n\n[source_mineru.md]\n\n[... middle omitted ...]\n\nnue without a final deal.  \n- Lower RatingDog PMI readings are broadly consistent with NBS PMIs released yesterday, indicating that manufacturing expansion moderated, in keeping with April act\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 01 Jun 2026 12:53 PM HKT\n\nDisseminated 01 Jun 2026 12:53 PM HKT"
  },
  {
    "id": "R008",
    "title": "市场低估了日本半导体设备的结构性机会，而非周期的尾声",
    "digest": "[wechat_article.md]\n# 市场低估了日本半导体设备的结构性机会，而非周期的尾声\n\n当市场将目光聚焦于AI芯片和先进制程的激烈竞争时，一份来自某外资投行的最新研报揭示了一个被广泛忽视的信号：日本半导体设备（SPE）行业正在经历的不是周期性的尾声，而是一轮由存储资本开支和先进封装驱动的结构性增长拐点。2026年4月的数据显示，日本SPE出货额同比增长25%（以日元计），其中组装设备同比暴增73%，测试设备增长26%。这些数字并非简单的月度波动——它们指向一个更深层的产业再平衡：全球晶圆厂设备（WFE）市场的增长引擎正在从逻辑芯片向存储芯片切换，而日本设备商正是这一切换的最大受益者。\n\n该报告预测，全球WFE市场在2026年将同比增长21.4%，2027年再增长18.2%。这一判断的核心逻辑并非AI需求的线性外推，而是存储厂商（尤其是DRAM和NAND）在经历了两年的资本开支紧缩后，正在启动一轮大规模的产能扩张。对于投资者而言，真正重要的不是判断AI需求是否见顶，而是理解为什么日本设备商在这一轮扩张中拥有比市场预期更强的议价权和份额提升能力。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 4月数据揭示的不是疲软，而是季度节奏的短期扰动\n\n4月单月日本SPE出货额环比下降38%，这一数字很容易被解读为需求走弱的信号。但研报通过3个月移动平均数据清晰地指出，这仅仅是季节性因素导致的基数效应——3月通常是日本财年末的出货高峰，4月自然回落。以3个月均值衡量，4月出货额环比仍增长6%，同比增长11%（以日元计为14%），延续了自2023年中开始的上升趋势。\n\n更值得关注的是设备品类的结构性分化。前道设备（主要对应东京电子TEL）同比增长12%，增速稳健但并未超预期；组装设备（对应DISCO）同比增长73%，虽然部分归因于低基数，但这一增速仍反映了先\n\n[... middle omitted ...]\n\n起跟踪接下来几个月的SEAJ数据变化，验证这一判断是否成立。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本半导体设备四月数据解读\n\n📊 日本设备商四月账单出炉\n\n四月日本半导体设备账单数据已公布，整体呈现温和增长态势。关键数字先看：\n\n1️⃣ 整体表现\n- 四月单月账单：同比增长25%（日元计）\n- 三个月移动平均：环比+6%，同比+14%\n- 单月环比下降38%，主要受三月高基数影响\n\n2️⃣ 分设备类型\n- 前道设备（TEL相关）：同比+12%\n- 组装设备（DISCO相关）：同比+73%，低基数效应明显\n- 测试设备（Advantest相关）：同比+26%，但环比-14%\n\n3️⃣ 关键公司前瞻\n基于SEAJ数据回归分析：\n- TEL：六月季度收入可能环比-18%，低于市场预期的+6%\n- Advantest：六月季度收入可能环比+13%，高于市场预期的+3%\n\n4️⃣ 行业展望\n- 2026年全球WFE市场预计同比+21.4%\n- 2027年预计同比+18.2%\n- DRAM和NAND资本支出将是主要驱动力\n\n日本设备商有望从存储芯片资本支出回升中受益，尤其是HBM和先进封装领域的需求增长。\n\n欢迎一起讨论半导体设备周期走向～\n\n#学习笔记\n\n[source_mineru.md]\n# Global S\n\n[... middle omitted ...]\n\nb74bd932f338528.jpg)\n\nJuho Hwang\n\n+852 2123 2632\n\njuho.hwang@bernsteinsg.com\n\n![](images/9951a0ef6204692975afc7ba9a7870420c51c229957382d5afff88cc6c0f0afc.jpg)\n\nAlrick Shaw\n\n+1 917 344 8454\n\nal\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R009",
    "title": "肺癌治疗格局的真正变量，不在PD-1，而在ADC与双抗的交叉点",
    "digest": "[wechat_article.md]\n# 肺癌治疗格局的真正变量，不在PD-1，而在ADC与双抗的交叉点\n\n2026年ASCO之后，市场对肺癌领域最值得关注的判断不是某款药物数据“好”或“坏”，而是一个结构性信号：**ADC与PD-1/L1xVEGF双抗正在从替代选项变为潜在的基石疗法，但全球数据验证才是真正分水岭**。\n\n某外资投行在ASCO结束后迅速组织了两位肺癌领域KOL的深度讨论。这两位KOL分别来自约翰霍普金斯大学和斯坦福大学，覆盖了从临床实践到早期试验设计的完整视角。他们的判断并非简单的“看好”或“看空”，而是给出了一个更有层次的分析框架：哪些信号已经足够清晰，哪些仍需等待全球数据，以及哪些未解问题将决定未来三到五年的竞争格局。\n\n这份讨论的核心价值不在于复述数据，而在于揭示了市场目前定价最不充分的两个维度——**毒性管理能力对市场份额的直接影响**，以及**中国数据向全球人群的转化风险**。以下是我们从KOL讨论中提炼的五个关键洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. sac-TMT的PFS数据已足够改写一线标准，但OS才是真正的定价锚\n\nKOL对科伦博泰与默沙东合作的sac-TMT（TROP2 ADC）在OptiTROP-Lung05研究中的表现给出了高度评价。一位KOL用了一个生动的比喻：PFS的HR数据在他看过的药物中属于“少数几个真正显著的”，如果用棒球术语来量化，0.5以下的HR就是“全垒打”。而sac-TMT在PD-L1高表达人群中的表现，已经接近这个区间。\n\n但KOL的谨慎同样值得关注。他们明确指出，Keytruda单药作为对照臂在全球范围内并非标准治疗（美国更倾向Keytruda联合化疗），因此中国数据的对照组表现可能被低估。这意味着sac-TMT的PFS优势在全球试验中可能会被压缩。\n\n更关键的是OS。一位\n\n[... middle omitted ...]\n\n被高估，哪些被低估，以及下一个数据读出节点可能带来的催化剂。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n肺癌新药KOL怎么看\n\nASCO之后聊了聊\n\n两位顶级肺癌专家怎么看最新数据\n\n刚开完ASCO，和两位肺癌KOL聊了会。信息量很大，但总结下来就几个关键点：\n\n1️⃣ 科伦/默沙东的sac-TMT，安全性和疗效都让KOL眼前一亮。PFS的HR非常亮眼，停药率才5%左右，毒性可控，没看到什么稀奇古怪的副作用。但最终全球OS数据才是决定能不能改变标准治疗的关键。\n\n2️⃣ 康方/Summit的依沃西单抗（PD-1/VEGF双抗）在HARMONi-6中OS获益明显，HR=0.66，和PFS差距不大，说明疗效持续性好。但KOL提醒中国数据需要在全球人群中验证，尤其是>65岁患者亚组存在争议。全球III期HARMONi-3的鳞癌PFS数据预计下半年读出，KOL认为大概率阳性。\n\n3️⃣ 阿斯利康的Datroway有先发优势（FDA已批单药），但基于中国数据，KOL认为sac-TMT的疗效和安全性潜力更大，前提是全球试验能验证。\n\n4️⃣ 双抗赛道整体受认可。BNTX/BMY和辉瑞的数据支持PD-1/L1×VEGF这个机制。KOL还特别提到三抗（PD-1×CTLA-4×VEGF）和RAS抑制剂是未来值得关注的新方向。\n\n[... middle omitted ...]\n\n profile and ability to manage toxicity, noting the final global overall survival (OS) data will ultimately be important in guiding treatment decisions; 2) ivo's OS benefit over Tevimbra (anti\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R010",
    "title": "关税下调的真正价值不在当期利润，而在日本工程机械的竞争格局重塑",
    "digest": "[wechat_article.md]\n# 关税下调的真正价值不在当期利润，而在日本工程机械的竞争格局重塑\n\n2026年6月2日，白宫一则关于修改钢铁和铝产品232条款关税的总统公告，在东京早盘交易时段引发日本机械板块的异动。表面看，这只是一次针对特定工业品类的税率调整——联合收割机、推土机、叉车等设备的对美出口关税从25%降至15%。但仔细拆解这份公告的生效时间、适用品类范围以及日落条款，会发现一个更值得关注的信号：美国正在有选择地降低某些工业品的进口壁垒，而其真实意图并非简单的贸易缓和，而是为重建本国工业基础争取时间。\n\n投行研报对此事件做了量化分析，估算出对主要日本厂商当期利润的影响——小松约100亿日元增量，久保田和竹内制作所影响有限。但如果我们只停留在利润测算层面，就错过了这份报告真正有价值的部分：关税下调的结构性含义，以及它对日本工程机械行业竞争格局的长期影响。\n\n以下是我们从这份研报中提炼出的五个核心洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 关税下调的窗口期设计，暴露了美国工业政策的真实节奏\n\n研报明确指出，新关税税率适用于6月8日及之后抵达的货物，这意味着实际体现在终端销售价格上要等到11月至12月以后。更关键的是，这项政策的日落日期是2027年12月31日。\n\n这不是一个永久性的税率调整，而是一个为期约18个月的窗口期。美国选择在这个时间点降低工程机械的进口关税，同时维持对钢铁和铝的基础税率不变，反映出一种精细化的政策逻辑：美国需要日本的高端工程机械来支撑其国内基建和制造业投资，但又不希望长期依赖进口。这18个月，恰好是美国本土产能爬坡的时间窗口。\n\n对于日本制造商而言，这个窗口期意味着两件事。第一，短期利润增厚是确定的，但幅度有限——研报测算的100亿日元增量对于小松这样的体量而言，约占其年营业利润的2%-3%，算不上质\n\n[... middle omitted ...]\n\n对这类结构性变化的深度拆解，帮助你建立更系统的产业分析框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美国对日系工程机械减税，小松迎来利好\n\n关税下调，工程机械成本下降\n\n投行研报指出，美国已宣布下调部分工程机械的Section 232关税。从6月8日起，日本出口到美国的拖拉机、液压挖掘机、推土机等，关税将从25%降至15%。\n\n1/ 影响有多大？\n对日本工程机械制造商整体是积极信号。但新税率只适用于6月8日之后到港的产品，实际外销可能要等到11-12月以后。研报测算，本财年小松的利润影响约+100亿日元，久保田和竹内制造影响有限。\n\n2/ 什么时候见效？\n从2027财年起，关税下调的贡献才会全面体现。政策有效期到2027年底，短期看是情绪利好，长期看才是真金白银。\n\n3/ 哪些公司最受益？\n小松是直接受益者，利润弹性最大。久保田和竹内制造也有正面影响，但当前贡献相对有限。\n\n研报未给出具体公司估值变化，这里是基于关税调整逻辑的推测：关税下降直接降低出口成本，对依赖美国市场的日本工程机械企业是结构性利好。\n\n欢迎一起讨论，关税变化对全球工程机械竞争格局会有什么影响？\n\n#学习笔记\n\n[source_mineru.md]\n## Japan Machinery: Construction: Lower Secti\n\n[... middle omitted ...]\n\nlldozers and forklifts on imports from certain countries, including Japan. The above changes will take effect on June 8 (EST) with the aim of promoting near-term investment to rebuild the nati\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R011",
    "title": "市场正在低估“芯片通胀”的扩散半径：从AI算力成本到全球消费品定价",
    "digest": "[wechat_article.md]\n# 市场正在低估“芯片通胀”的扩散半径：从AI算力成本到全球消费品定价\n\n过去十二个月，DRAM价格累计上涨超过六倍。如果只看这个数字，很容易将其归入“半导体周期正常波动”的叙事框架。但一份来自某外资投行研究团队的最新报告提出了一个更具结构性的判断：我们正在经历的，不是一次普通的存储器上行周期，而是一场由AI需求驱动的、跨行业、跨地域的“芯片通胀”开端。\n\n这份报告的标题直指核心——Chipflation。它试图回答一个正在从产业界蔓延到宏观政策圈的问题：当存储器从“大宗商品”变成“战略资产”，其价格重估的冲击波，究竟会传导多远？\n\n我们仔细研读了这份长达数十页的报告，以下是我们提炼出的核心洞察与尚未被市场充分定价的关键变量。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 存储器不再是周期品，而是AI时代的“新石油”\n\n报告最核心的论点在于，本轮存储器价格上涨的驱动力，与传统半导体周期有本质区别。过去的涨价往往源于供给端的短期收缩或下游的补库存行为，价格会在需求正常化后迅速回落。但这一次，需求端的结构性变化是主导因素。\n\nAI基础设施的建设，正在以前所未有的速度吞噬存储器产能。以HBM（高带宽存储器）为例，它是AI加速器的核心组件，但其制造过程极度消耗先进DRAM晶圆产能。报告提供的数据显示，到2028年，HBM将占据领先级存储器晶圆产能的约34%，而2023年这一比例仅为6%。这不仅是量的增长，更是质的挤出——当供应商优先将产能分配给利润更高、需求更确定的AI产品时，留给智能手机、PC、汽车、工业等传统市场的存储器供给，将出现系统性缺口。\n\n报告通过一个“两级DRAM供给瀑布模型”量化了这一缺口：到2027年，PC市场将面临约15%的存储器短缺，智能手机市场短缺约12%，分别对应约5800万台PC和1.34亿部\n\n[... middle omitted ...]\n\n将在社群中结合完整报告的原始图表和数据，做进一步的深度解读。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n芯片涨价潮，正在重塑整个电子产业\n\n芯片涨价，不只是成本问题\n\n某外资投行最新研报抛出一个核心观点：AI正在把存储芯片从“商品”变成“战略资源”，整个电子产业的游戏规则正在被改写。\n\n1/ 存储芯片价格一年涨了6倍\n过去DRAM价格每5年跌到1/10，但现在AI需求爆发，HBM、DRAM、企业级SSD全面吃紧。新建产能需要2年以上才能投产，供给缺口短期内无法填补。\n\n2/ 巨头抢货，小厂遭殃\n云巨头通过长期协议锁定产能，留给传统买家的份额越来越小。研报测算：到2027年，手机DRAM供给缺口12%，PC缺口15%——相当于1.34亿部手机、5800万台PC的产能被AI挤占。\n\n3/ 芯片通胀正在扩散\n成本压力从服务器蔓延到PC、手机、汽车、工业设备。上游存储厂商业绩亮眼，下游硬件厂商要么涨价、要么降配、要么牺牲利润。研报特别提醒：PPI已经同比涨了30%，但CPI影响暂时被低估。\n\n4/ 政策远水解不了近渴\n即使中美出台补贴或税收优惠，产能建设仍需数年。短期内，供给紧张格局难改。\n\n行业正在分裂成“有芯片的”和“没芯片的”两个世界。定价权在上游，下游只能被动应对。\n\n欢迎一起讨论：你觉得下一轮手机和PC涨价会\n\n[... middle omitted ...]\n\nl semiconductor upturn and more like a durable supply-demand reset.\n\nAllocation is replacing commodity-market pricing. Hyperscalers and AI buyers are increasingly using long-term agreements (L\n\n[... middle omitted ...]\n\nme securities: Rajeev Sibal; Diego Anzoategui.\n\nThe following authors are Fixed Income Research Analysts/Strategists and are not opining on or expressing recommendations on equity securities: Ariana Salvatore.\n\n© 2026 MS"
  },
  {
    "id": "R012",
    "title": "全球汽车市场正在经历的不是周期波动，而是竞争逻辑的根本切换",
    "digest": "[wechat_article.md]\n# 全球汽车市场正在经历的不是周期波动，而是竞争逻辑的根本切换\n\n这份来自某外资投行全球汽车研究团队的周度报告，覆盖了从北美到中国、从特斯拉到法拉利的广泛议题。表面上看，这是一份常规的行业跟踪更新：4月全球汽车销量同比微增0.7%，美国和中国仍在下跌，欧洲和新兴市场成为主要支撑。但真正值得关注的不是这些数字本身，而是数字背后的结构性信号——汽车行业的竞争焦点，正在从“谁能造出更好的车”转向“谁能在执行层面把规模、技术和成本控制转化为可持续的利润”。\n\n这不是一个周期性的底部判断。这是一个关于行业竞争逻辑已经发生不可逆变化的判断。理解这一点，比预测下一个季度的销量拐点重要得多。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 全球销量数据揭示的不是需求疲软，而是赢家与输家的加速分化\n\n4月全球主要市场合计销售590万辆，同比仅增长0.7%。但这组平淡的总量数据掩盖了两个关键分化。\n\n第一个分化是区域性的。欧洲整体增长7%，其中英国增长24%、意大利增长12%，而美国下滑5.5%、中国下滑4.3%。新兴市场表现更为突出：印度增长24.6%、巴西增长20.5%、印度尼西亚增长55%。这不是一个“全球需求疲软”的故事，而是一个“成熟市场结构性见顶、新兴市场仍有渗透空间”的故事。对于全球布局的OEM而言，这意味着区域配置的权重正在发生实质性变化。那些过度依赖单一市场的企业，风险敞口正在放大。\n\n第二个分化是品牌层面的。在主要OEM中，特斯拉4月销量同比增长26.8%，市场份额提升0.5个百分点。与此同时，大众集团下滑10.1%、福特下滑13.8%、通用汽车下滑15.7%。更值得关注的是，报告明确指出“高端市场在全球范围内正在失去份额，而大众市场正在增长”。高端品牌整体销量同比下降2.3%，大众市场增长1.3%。这一趋势如果持\n\n[... middle omitted ...]\n\n们可以基于完整报告和原始图表，做一些更细致的推演和交叉验证。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球汽车市场正在分化\n\n需求分化期，谁在突围？\n\n全球4月汽车销量同比+0.7%，但美中两大市场还在跌。美国-5.5%，中国-4.3%。欧洲+7%，印度+24.6%，巴西+20.5%。新兴市场撑起了半边天。\n\n几个关键信号：\n\n1. **特斯拉的自动驾驶在爬坡**\n奥斯汀robotaxi车队的安全数据在改善，FSD使用率在扩大。某外资投行认为这是“速率变化的故事”——不是一夜爆发，但趋势向上。\n\n2. **传统车企在拼执行**\nStellantis的转型目标很激进，但市场不买账，焦点全在能不能落地。Carmax还在等6月的战略更新，目前处于“等待模式”。\n\n3. **法拉利首款纯电来了**\n定位在现有产品线的高端区间，但设计语言引发争议，股价跌了约8%。说明高端电动车也不好做。\n\n4. **中国车企的海外战况**\nBYD 4月海外注册量环比下降10-15%，主要是英国市场从3月峰值回落。但拉美和东南亚在补位，同比仍有55-60%增长。吉利海外注册量环比+10-15%，巴西贡献最大。\n\n5. **印度市场持续火热**\nAshok Leyland一季度利润率14.6%，虽然同比微降，但需求依然坚挺。公司已提价1-\n\n[... middle omitted ...]\n\n//www.extelinsights.com/voting and select \"All-American Research Team\".\n\n![](images/aa7b1951feefabd0350653d8390e4348531f4232037801f9b879fe476e036d37.jpg)\n\n<details>\n<summary>text_image</summar\n\n[... middle omitted ...]\n\n Co. Ltd. (064960.KS)</td><td>E (05/01/2026)</td><td>W29,300</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.   \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R013",
    "title": "铜价突破的关键不在于需求爆发，而在于供给侧的三个结构性断裂",
    "digest": "[wechat_article.md]\n# 铜价突破的关键不在于需求爆发，而在于供给侧的三个结构性断裂\n\n过去六个月，铜价在每吨12,000至13,000美元之间反复拉锯。市场上最主流的两派叙事——一派押注AI与能源转型拉动结构性需求，另一派担忧全球增长放缓与地缘风险——已经在这个区间内完成了充分的定价博弈。但某外资投行最新发布的研报提出了一个更值得关注的判断：铜价将在一个月内触及每吨14,500美元，并在一年内站上15,000美元。\n\n这个判断之所以值得认真对待，不是因为该行上调了需求预测，而是因为它系统性地重估了供给侧的三个关键变量。这三个变量过去被市场视为“已知的已知”，但该报告用最新数据表明，它们正在从“已知”滑向“严重低估”。\n\n更重要的是，这份报告揭示了一个反直觉的定价逻辑：铜价接下来的上行动力，将主要来自“供给跟不上需求”这一事实的重新定价，而非需求本身的加速。对于产业决策者和资产配置者而言，这意味着当前的交易区间可能正在成为过去式。\n\n以下是我们从这份报告中提炼出的五个核心洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 2026年矿山产量零增长，这比表面数字更糟糕\n\n报告最硬核的修正出现在矿山供给端。该行将2026年全球铜矿产量增速从正增长下调至-0.2%——换句话说，产量几乎没有增长。这个数字本身已经低于市场共识，但真正重要的不是这个数字，而是它背后的结构性原因。\n\n报告明确指出，其上调了2027年和2028年的全球矿山中断率假设至7%。这意味着更多矿山的投产和爬坡将出现延误、减产或非计划停产。报告特别点名了几个关键矿区——Grasberg、El Teniente、Kamoa、Cobre Panama——这些全球级矿山在2026-2027年的实际产出都存在显著的执行风险。\n\n更深层的问题是刚果（金）的供给风险。该地区近年已成为全\n\n[... middle omitted ...]\n\n报告的关键图表、我们的二次分析笔记，以及来自产业一线的观察。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n铜价突破窗口已打开\n\n铜价看14500\n\n供应收缩+关税博弈双重催化\n\n最近看了一份某外资投行的铜研报，逻辑很清晰。核心观点是：铜价在未来一个月有望突破14500美元/吨，一年内看至15000美元。为什么？\n\n1️⃣ 供应端收紧是硬支撑\n研报大幅上调了供应扰动率，2027-2028年从4%调高至7%。主要原因是：\n- 关键矿山（如Grasberg、Kamoa）的达产风险增加\n- 刚果的硫磺供应瓶颈限制了冶炼产能释放\n- 全球废铜回收增速跟不上价格涨幅，今年前4个月废铜进口仅温和增长，远低于铜价30%的同比涨幅\n\n2️⃣ 美国关税博弈带来短期溢价\n市场对6月底美国对精炼铜232调查结果的担忧，支撑了COMEX-LME价差。研报推测，政策可能保持“战略模糊”——不明确宣布征税，但也不否认，以鼓励铜继续流入美国。这种不确定性至少能支撑到7月。\n\n3️⃣ 需求韧性比想象中强\n尽管中国新能源装机因高基数同比下滑，但全球PMI回暖正在拉动周期性需求。能源转型和AI的结构性需求，让铜的消费比过去更有韧性。研报预测2027年将出现约36万吨的短缺。\n\n⚠️ 当然也有下行风险：中东局势持续不稳、利率预期走高，都可能拖累风险资产\n\n[... middle omitted ...]\n\nentual deal (base case) to reopen the Strait should be bullish for risk assets. We are now also more conservative on copper supply growth and assume scrap and mine output underperform through \n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R014",
    "title": "新能源渗透率突破63%的真正含义：市场正在重新定义赢家的门槛",
    "digest": "[wechat_article.md]\n# 新能源渗透率突破63%的真正含义：市场正在重新定义赢家的门槛\n\n5月最后一周，中国新能源乘用车单周订单同比、环比双双增长超过10个百分点，渗透率在5月1日至24日期间达到62.5%至63.6%。这些数字本身并不令人意外——市场已经习惯了这个渗透率区间。\n\n但这份某外资投行最新发布的周度报告揭示了一个更值得关注的结构性变化：在整体订单温和增长的表象下，品牌间的分化正在急剧加速。5月最后一周，蔚来订单环比暴增228%，鸿蒙智行增长92%，比亚迪增长15%。而同一周，理想汽车订单环比下滑25%，小鹏下滑61%。\n\n这不是一次普通的周度波动。这是一场关于“谁能在高渗透率时代继续增长”的压力测试。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 新产品周期的启动正在重塑订单结构，但持续性才是真正的考验\n\n5月最后一周的订单数据最突出的特征是“新品驱动”效应。蔚来ES9、问界M9改款、比亚迪元PLUS改款和宋Ultra DM-i的集中上市，直接推动了这几个品牌订单的环比大幅增长。\n\n从数据上看，蔚来5月订单达到86183辆，环比增长96%，同比增长190%；鸿蒙智行5月订单143479辆，环比增长17%，同比增长154%。这些数字在绝对量和增速上都相当可观。\n\n但这里有一个需要冷静看待的问题：新产品上市带来的脉冲式增长，能否转化为可持续的订单曲线？从历史数据来看，大多数品牌在新品上市后的第3到4周，订单增速会出现明显回落。5月最后一周蔚来228%的环比增长，其基数效应（前一周仅11830辆）放大了这一数字的冲击力。\n\n对投资者和产业决策者而言，关键不是盯着单周爆发的幅度，而是观察未来4到6周订单曲线的斜率变化。真正的产品力，体现在上市一个月后能否维持环比正增长。\n\n![研报原图 2](assets/source_image\n\n[... middle omitted ...]\n\n继续讨论，我们会围绕这些关键问题展开更细致的推演和交叉验证。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n新车扎堆，订单回暖了\n\n📈 周订单+11%\n\n5月最后一周，订单有点意思\n\n某外资投行刚出的周报，第22周（5/25-5/31）订单合计环比+11%，同比+20%🆙\n\n1️⃣ 谁在涨？\n- 蔚来：+228% wow，ES9新车拉动明显\n- 鸿蒙智行：+92% wow，M9改款效应\n- 比亚迪：+15% wow，元Plus改款+宋Ultra DM-i\n- 特斯拉：+19% wow，维持稳定\n\n2️⃣ 渗透率持续高位\n5月1-24日，新能源零售渗透率62.5%，批发渗透率63.6%\n比4月的62.8%/57.3%有提升\n\n3️⃣ 终端折扣收窄\n- 新能源经销商折扣7.75%（5/30），低于前周7.79%\n- 燃油车折扣19.47%，也小幅收窄\n- 上游碳酸锂价格微降至17.95万/吨，电池价格稳定\n\n4️⃣ 接下来看什么？\n- 6/11：蔚来乐道L60改款发布\n- 6月：比亚迪大唐、零跑D99上市\n- 7月：小鹏MONA L03\n\n新车周期是订单最直接的催化剂，后续继续关注改款+新车型的放量节奏。\n\n欢迎一起讨论～\n\n#学习笔记\n\n[source_mineru.md]\nCHINA NEW ENERGY VEHI\n\n[... middle omitted ...]\n\n (4) Upstream battery pricing dynamics.\n\n## 2026 Week 22 highlights:\n\n■ Key brand orders: Nio / HIMA / BYD showed the highest growth at +228%/+92%/+15% wow mainly driven by new model launches.\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R015",
    "title": "新能源渗透率突破63%后，市场真正低估的是新车型的订单转化效率",
    "digest": "[wechat_article.md]\n# 新能源渗透率突破63%后，市场真正低估的是新车型的订单转化效率\n\n2026年5月最后一周，中国新能源乘用车市场交出了一份看似平淡、实则暗藏分化的成绩单。某外资投行最新发布的周度研报显示，当周主要新能源品牌合计订单环比增长11%，同比增长20%，新能源渗透率在5月1-24日期间达到62.5%-63.6%。渗透率数字本身并不令人意外——市场早已接受50%以上的新常态。但真正值得关注的是订单增长的结构：它不是普惠式的行业回暖，而是由特定品牌的新车型集中投放所驱动。蔚来周订单环比暴增228%，鸿蒙智行增长92%，比亚迪增长15%。这三家合计贡献了当周绝大部分增量。\n\n这意味着什么？当行业渗透率进入60%以上的高位区间，增长的动力已经从“电动化替代”切换为“产品周期竞争”。每一款新车型的订单转化效率，正在成为决定品牌季度排名的关键变量。市场对此的定价可能仍然不足。\n\n以下，我们从订单结构、折扣信号、定价权分化三个层次，逐一拆解这份研报的核心洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 新车型集中投放正在制造“订单断层”，而非整体复苏\n\n5月最后一周的订单数据，表面上是整体向好，但细看品牌间的差距，几乎是断层式的。蔚来周订单从1.18万辆跃升至3.88万辆，环比增长228%；鸿蒙智行从2.11万辆增至4.07万辆，环比增长92%。而同期，理想汽车订单环比下降25%，小鹏下降61%，吉利银河与极氪合计下降39%。\n\n这种分化并非偶然。研报明确指出，增长主要由新车型驱动：蔚来ES9、问界M9改款、比亚迪元Plus改款和宋Ultra DM-i。换句话说，当周订单增量几乎全部来自“新车效应”，而非存量需求的自然回暖。\n\n对于产业决策者而言，这一信号的含义是明确的：在渗透率高位，任何品牌的订单增长都越来越依赖产品更新节奏。\n\n[... middle omitted ...]\n\n整研报的解读笔记和原始图表，并定期组织对关键问题的深度探讨。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n新能源周报｜5月订单回暖，谁在领跑？\n\n📊 订单回暖，新品驱动\n\n**1. 周度订单反弹**\n5月最后一周，新能源车订单环比+11%，同比+20%。主因是新车集中上市：蔚来ES9、问界M9改款、比亚迪元Plus改款、宋Ultra DM-i等。\n\n**2. 谁在领跑？**\n- 蔚来：周订单环比+228%，同比+558%（ES9拉动明显）\n- 问界（HIMA）：周订单环比+92%，同比+342%\n- 比亚迪：王朝+海洋系列周订单环比+15%，但同比-39%\n- 特斯拉：周订单环比+19%，同比+75%\n\n**3. 渗透率新高**\n5月1-24日新能源渗透率达62.5%-63.6%，比4月的62.8%略有提升。\n\n**4. 价格趋势**\n- 新能源车终端折扣收窄至7.75%（vs 上周7.79%）\n- 燃油车折扣同步收窄至19.47%（vs 上周19.67%）\n- 电池级碳酸锂价格微降至17.95万元/吨（-0.8%）\n\n**5. 后续看点**\n- 6月11日：蔚来乐道L60改款发布\n- 6月：比亚迪大唐、零跑D99上市\n- 6月底：理想L8改款\n- 7月：小鹏MONA L03\n\n5月订单回暖信号明显，但各品牌分化\n\n[... middle omitted ...]\n\n (4) Upstream battery pricing dynamics.\n\n## 2026 Week 22 highlights:\n\n■ Key brand orders: Nio / HIMA / BYD showed the highest growth at +228%/+92%/+15% wow mainly driven by new model launches.\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R016",
    "title": "现代起亚正在悄悄改写美国汽车市场的竞争规则",
    "digest": "[wechat_article.md]\n# 现代起亚正在悄悄改写美国汽车市场的竞争规则\n\n当市场把注意力集中在特斯拉的价格战和比亚迪的全球扩张时，一份来自某外资投行的最新月度跟踪数据揭示了一个容易被忽视的结构性变化：现代汽车与起亚在美国市场的合计份额在2026年5月达到11.8%，同比提升0.3个百分点，更重要的是，两者的混合动力车（HEV）市场份额已逼近20%大关，达到19.9%，同比大幅跃升8.3个百分点。\n\n这不是一次性的月度波动。从YTD数据看，现代与起亚在美国的HEV销量同比分别增长65.1%和102.1%，而同期美国整体HEV市场增速为17.4%。这意味着，这两家韩国车企正在以超过行业3-5倍的速度抢占HEV赛道，而这一赛道的增速本身已是纯电动车（BEV）的3倍以上。\n\n这份报告最值得关注的判断不是11.8%这个数字本身，而是它背后揭示的竞争逻辑：在纯电动车需求增速放缓、消费者回归务实选择的背景下，现代起亚正在通过HEV建立起一种“成本可控的电动化过渡策略”，这种策略正在改写传统车企在北美市场的利润结构。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. HEV正在成为现代起亚在美国的“利润压舱石”，而非过渡产品\n\n2026年5月的数据显示，现代与起亚的HEV销量分别为25,559辆和25,392辆，同比增长高达90.1%和179.4%。这一增速远超行业HEV增速的32.5%，也远超其自身整体销量的个位数增长。更关键的是结构变化：HEV在现代总销量中的占比从去年同期的14.7%跃升至27.1%，在起亚中更是从11.5%飙升至31.5%。\n\n这意味着什么？HEV不再是“等待纯电到来之前的过渡方案”，而是正在成为这两家公司在美国市场的主力利润来源。从激励支出数据也可以佐证这一判断：现代HEV占比提升的同时，其单车激励支出仅为3,330美元，低于行业\n\n[... middle omitted ...]\n\n信群里继续讨论，我们会定期更新对这份报告关键假设的验证进展。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n现代起亚，美区5月市占率破纪录\n\n封面：11.8% 份额新高\n\n副标题：混动占比逼近30%，纯电也在涨\n\n5月数据出来了，现代起亚在美国的市占率创下新高，合计达到11.8%，环比和同比都涨了0.3个百分点。这个数字背后有几个值得关注的细节。\n\n**1. 混动成了绝对主力**\n\n- 现代混动销量2.56万辆，同比增长90.1%\n- 起亚混动2.54万辆，同比暴增179.4%\n- 两家合计混动市占率达到19.9%，同比提升8.3个百分点\n- 混动占现代总销量的27.1%，起亚更是达到31.5%\n\n**2. 纯电也在回暖**\n\n- 现代纯电销量6483辆，同比增长6.1%\n- 起亚纯电2822辆，同比增长89.5%\n- 两家合计纯电市占率10.8%，同比提升3.7个百分点\n- 虽然行业整体纯电销量同比下降19.8%，但现代起亚的纯电份额在扩大\n\n**3. 激励力度加大**\n\n- 现代单车激励3330美元，环比增长16.9%\n- 起亚单车激励3440美元，环比增长9.9%\n- 两家都低于行业平均的3502美元，说明定价能力相对较强\n\n**4. 全年指引**\n\n研报显示，现代预计北美批发量同比增长0.5%，起亚预计美国\n\n[... middle omitted ...]\n\nket share, HMC recorded 6.4% (+0.1ppt MoM, +0.2ppt YoY) and Kia 5.4% (+0.2ppt MoM, +0.1ppt YoY). Combined market share recorded 11.8% (+0.3ppt MoM, +0.3ppt YoY). We expect 12.0% M/S by end of \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R017",
    "title": "市场真正低估的不是需求，而是二手房定价权的结构性转移",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是需求，而是二手房定价权的结构性转移\n\n过去几周，关于中国房地产市场的讨论重新升温。政策端的积极信号、部分城市销售数据的边际改善，让市场参与者再次开始争论“底部是否已到”。\n\n但这份最新发布的中国房地产周度数据库追踪报告，提供了一组值得深思的读数。它揭示了一个比短期销售波动更关键的结构性事实：市场的定价逻辑正在从新房市场向二手房市场转移，而这一转移的速度，可能比大多数投资者意识到的要快。\n\n报告显示，截至5月31日当周，50城新房周度成交同比增长10%，相比前一周的-7%出现明显回升。但与此同时，10城二手房周度成交同比增长9%，虽然增速较前一周的45%有所回落，但年初至今累计同比仍保持5%的正增长。更关键的数据来自去化率：整体去化率从前一周的66%降至53%，其中一线城市从66%降至63%，二线城市从42%降至一个更低的水平。\n\n这些数字组合在一起，指向一个被市场普遍低估的结论：新房市场的短期回暖并不稳固，而二手房市场正在成为定价的锚点。真正重要的不是销售量的月度波动，而是二手房价格发现机制的形成速度，以及它对开发商定价权的侵蚀。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 新房成交的反弹是基数效应和集中推盘的结果，而非需求复苏的信号\n\n50城新房周度成交同比10%的增长，乍看之下是一个积极信号。但如果把时间拉长，年初至今累计同比仍为-14%。这意味着，单周的增长更多是去年同期低基数（-7%）和开发商在5月底集中推盘的结果，而非购房需求的系统性回升。\n\n更值得关注的是去化率的下降。整体去化率从66%降至53%，说明即使推盘量增加，市场吸收新供应的能力并未同步提升。一线城市去化率虽仍维持在63%的较高水平，但同样出现了边际下滑。二线城市42%的去化率则进一步确认了库存压力的积累。\n\n对于投资\n\n[... middle omitted ...]\n\n拆解这些关键变量之间的逻辑关系，并构建更完整的投资判断框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n楼市回暖信号？5月新房成交转正\n\n新房成交转正\n\n50城新房周成交同比+10%\n\n5月最后一周，新房成交数据出现变化。\n\n某外资投行最新周度追踪显示，截至5月31日当周，50城新房成交同比上升10%，扭转了前一周-7%的跌幅。年初至今累计同比仍为-14%。\n\n分城市看，三四线表现最亮眼：\n1️⃣ 一线城市同比+4%（前值+8%）\n2️⃣ 二线城市同比+6%（前值-10%）\n3️⃣ 三线城市同比+34%（前值-12%）\n\n二手房方面，10城周成交同比+9%，增速较前一周的+45%明显回落。一线城市二手房成交同比+12%，二线城市+6%。\n\n一个值得关注的指标：整体去化率53%，低于前一周的66%。一线城市去化率63%，二线42%。\n\n价格端，中原6城二手房挂牌价指数同比-17.5%，较前一周的-18.2%略有收窄。一线城市中介信心指数53.8，前值55.5。\n\n怎么看这个数据组合？\n\n新房成交转正，三线城市贡献最大，可能与基数效应和局部政策放松有关。但去化率走低说明供给端压力仍在。二手房成交增速放缓，价格指数仍在低位，市场信心修复还需时间。\n\n研报对行业整体评级为“In-Line”，中性偏谨慎。\n\n大家觉得这波\n\n[... middle omitted ...]\n\n10 cities increased 9% YoY (vs. +45% YoY in the previous week), bringing YTD sales to +5% YoY: Tier 1 city weekly secondary unit sales rose 12% YoY (vs. +63% YoY). Tier 2 city weekly secondary\n\n[... middle omitted ...]\n\nperty Co Ltd (0123.HK)</td><td>O (09/27/2024)</td><td>HK$4.59</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R018",
    "title": "市场真正低估的不是需求，而是供给侧的再定价",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是需求，而是供给侧的再定价\n\n最近一周，投行研报覆盖的两家中国价值零售龙头——鸣鸣集团和万辰食品，股价分别反弹9%和6%，部分收复了此前两周15%和10%的跌幅。表面看，这是市场对“补贴战扩大”担忧的短期缓解。但这份研报传递的核心信号远比“情绪修复”更值得深究：**中国平价零售赛道正在经历一次供给侧的主动再定价，而市场对这一变化的系统性含义仍然定价不足。**\n\n5月27日至29日的抛售，导火索是市场担心两家公司加大了对加盟商的补贴力度，尤其是针对新店开业。补贴扩大通常被视为行业竞争加剧、单位经济模型恶化的信号。但6月2日收盘后，鸣鸣和万辰几乎同时通过官方渠道发布声明，正式重申对“健康发展”和“理性竞争”的承诺。两家公司明确反对非理性竞争，同时表达了对餐饮价值零售商在零食品类和饮料市场长期增长空间的信心，并强调有序、健康的竞争环境——这与全国性的“反内卷”政策方向高度一致。\n\n这份研报的价值不在于复述这些公开声明，而在于它提供了三个层次的穿透性分析：第一，补贴扩大的真实边界在哪里；第二，门店扩张速度与单店GMV趋势之间的动态平衡；第三，这些变化如何重塑两家公司的估值逻辑。\n\n以下是我们从这份研报中提炼的四个核心洞察，以及一个尚未被完全回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 补贴扩大的本质不是价格战，而是对加盟商进行“供给侧筛选”\n\n市场对补贴的第一反应往往是“利润受损”。但这份研报通过渠道调研指出，本轮补贴扩大的核心目的并非抢占市场份额，而是**加速优质加盟商的招募与筛选**。报告明确写道：“渠道调研显示，本轮补贴增加仍然是有纪律的。”这意味着补贴不是无差别的“烧钱”，而是有针对性的激励。\n\n关键区别在于：无差别补贴会导致存量加盟商补贴依赖、新店质量参差不齐；而有纪律的补\n\n[... middle omitted ...]\n\n贴退坡条件”或“网络重叠量化”有自己判断，也欢迎来群里碰撞。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n零食折扣店，还在加速开店\n\n开店节奏加快\n\n前两周零食折扣店回调，6月2日两家龙头通过官方渠道重申：反对无序竞争，看好行业长期空间。这轮补贴加码有节制，市场足够大，龙头继续扩店没问题。\n\n1️⃣ 开店加速\n- 5月单月，鸣鸣净增900+店，万辰净增1000+店\n- 2Q25以来开店节奏明显提速，5M26两家合计新开超3000家\n\n2️⃣ 单店表现稳\n- 万辰5月日均GMV转正（含新开店）\n- 鸣鸣1Q25单店GMV同比中个位数下滑，2Q预计仍有压力\n\n3️⃣ 估值与催化\n- 回调后鸣鸣/万辰对应2026E PE为17x/14x\n- 近期催化：鸣鸣6月8日纳入港股通；万辰港股上市进展\n\n欢迎一起讨论，你们那的零食折扣店还卷吗？\n\n#学习笔记\n\n[source_mineru.md]\n## CHINA STAPLES\n\n# Value Retailers: Busy Ming/Wanchen officially reiterated commitment to healthy competitive environment; Store open acceleration in May; Buy\n\nBusy Mi\n\n[... middle omitted ...]\n\n Ming and Wanchen reiterated their opposition to irrational competition and expressed confidence in the substantial long-term growth runway for F&B value retailers across the broader snacks an\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R019",
    "title": "市场真正低估的不是需求，而是供给侧的再定价能力",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是需求，而是供给侧的再定价能力\n\n锂价在突破20万元/吨后短暂回落，市场随即出现分歧。一部分投资者担忧高价抑制终端需求，另一部分则怀疑涨势能否持续。但某外资投行在6月初发布的这份研报给出了一个更值得关注的判断：锂价年内有望测试25万元/吨，而权益市场尚未充分定价这一情景。\n\n这不是一个简单的看多观点。它的底层逻辑不同于2021-2022年那轮由补贴和囤货驱动的暴涨。报告的核心主张是：当前锂价上行的驱动力，已经从“故事驱动”切换为“基本面驱动”，而基本面中最被低估的不是需求增速本身，而是供给侧的间歇性断裂与再定价能力。\n\n这份报告基于对电池生产管道、库存动态和供给中断事件的月度追踪，给出了一个可以持续验证的框架。对于任何关注新能源产业链的决策者来说，理解这个框架，比猜测下一个月的锂价数字更有价值。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 电池生产管道显示，需求侧的高频信号比市场预期的更强劲\n\n市场对2026年新能源车和储能需求的担忧，主要集中在两个点上：一是新能源车销量可能不及预期，二是原材料成本上涨可能侵蚀储能的内部收益率，从而抑制装机。但报告引用的第三方咨询数据显示，这些担忧尚未在实物层面兑现。\n\n2026年前四个月，中国电池产量同比增长41%至874 GWh。其中，动力电池产量增长22%，储能电池产量增长99%。更关键的是，这一增长趋势并非脉冲式。从月度数据看，3月和4月的产量分别达到225 GWh和247 GWh，环比持续加速。这意味着，下游电池厂并没有因为锂价上涨而放缓生产节奏。\n\n为什么需求如此坚韧？报告给出了两个容易被忽略的结构性原因。第一，新能源车出口超预期，拉动了国内电池出货。第二，商用车电动化加速，而商用车的单车电池装机量远高于乘用车。2026年一季度，商用车电池装机量\n\n[... middle omitted ...]\n\n分享对锂价、库存和供给事件的跟踪更新，并在关键节点给出判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n碳酸锂看25万，电池链谁最受益？\n\n**锂价再冲高？**\n\n**8-9月可能看到25万/吨**\n\n某外资投行最新研报认为，锂价还没到顶。虽然上周突破20万后回调，但需求端数据持续超预期，加上供应端频繁扰动，判断年内可能再冲25万/吨，时间窗口在8-9月。\n\n1. **需求比想象中更猛**\n今年前4个月电池产量874GWh，同比增长41%。商用车电动化是隐藏变量——1季度商用车电池装机占比升到22%（2024年才16%），每台商用车带电量是乘用车的3-4倍。出口也没拖后腿，新能源车出口量持续超预期。\n\n2. **供应端“拆东墙补西墙”**\n- 江西某大矿（宜春）因采矿证到期+环评问题，从去年8月停到现在，复产时间要看政府审批进度，市场预期偏悲观\n- 云母矿今年可能面临同样的许可证更新问题，虽然企业提前囤货，但实际减量影响可能在8千吨LCE/月\n- 澳洲高成本矿山开始复产，但增量主要在2027年，今年实际投放有限\n- 津巴布韦刚恢复锂矿出口，但要加征10%出口税，成本抬升是确定性趋势\n\n3. **库存信号很明确**\n碳酸锂总库存从年初的9.5万吨降到6.5万吨，冶炼厂库存去化最明显（从5.5万吨降到2万吨）。库存\n\n[... middle omitted ...]\n\n on concern of demand destruction if price stays high, we move up our preference on lithium names as we believe they will outperform the rest of the battery chain when the price rises. We rais\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R020",
    "title": "市场低估的不是需求，而是AI基础设施供应链的再定价",
    "digest": "[wechat_article.md]\n# 市场低估的不是需求，而是AI基础设施供应链的再定价\n\n过去几个月，关于AI算力需求见顶的讨论不绝于耳。一些投资者开始担忧，大模型训练放缓、推理成本快速下降，是否意味着整个AI基础设施的投资逻辑正在松动。\n\n某外资投行5月发布的AI项目追踪报告提供了截然不同的信号。这份报告追踪了全球范围内neocloud、主权AI和企业级部署的最新动态，其核心判断是：AI基础设施市场正在经历从“建设能力”到“交付价值”的关键转型，而这一转型将重塑整个供应链的价值分配逻辑。\n\n真正被市场低估的，不是AI需求本身，而是当基础设施从实验性部署走向生产化运营时，哪些环节将获得重新定价的机会。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. Neocloud的战略转向正在改变GPU资产的定价逻辑\n\n5月最值得关注的两笔交易，都不是简单的产能扩张。IREN收购Mirantis、Nebius收购Eigen AI，这两笔交易的共同特征是：neocloud正在从“提供GPU算力”向“提供生产级推理服务”转型。\n\nIREN以约6.25亿美元收购Mirantis，后者是云基础设施和Kubernetes编排领域的专业服务商。这笔收购的直接效果是让IREN能够更快地部署和运维其GPU基础设施，提升运营可见性和技术服务能力。但更深层的含义在于，IREN正在为自己的GPU资产增加一层“软件溢价”——不再是简单地出租算力，而是提供一套可管理、可监控、可优化的AI云交付平台。\n\nNebius以约6.43亿美元收购Eigen AI的逻辑更为清晰。Eigen AI是推理和模型优化领域的领先公司，其技术栈包括Sparse Attention和Activation-aware Weight Quantization等先进优化技术。Nebius将这些技术整合进其“Toke\n\n[... middle omitted ...]\n\nai推理服务的竞争格局分析，以及企业AI部署的财务模型框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI基建正在经历一场关键转变\n\n云厂商集体升级\n\n从卖算力到卖服务，AI基建进入2.0阶段\n\n5月AI项目圈最值得关注的几个信号：\n\n1️⃣ 新云厂商开始“向上”整合\nIREN收购Mirantis（K8s编排），Nebius收购Eigen AI（推理优化）。这标志着新云厂商不再满足于提供GPU算力，而是向上搭建软件层、推理层，把“机房出租”升级成“生产级AI服务”。目标客户也从实验室转向企业。\n\n2️⃣ 企业级AI部署走向混合与本地化\nDell Tech World上，多个行业客户展示了本地部署方案：\n- 三星用Dell做半导体设计自动化\n- 礼来部署1016块Blackwell Ultra超算（LillyPod）\n- 马自达用PowerScale统一CAD与AI数据湖\n- Hudson River Trading在挪威建专属AI研究数据中心\n企业不想把核心业务数据全放云端，混合部署正在成为标配。\n\n3️⃣ 超大单频出，资本密集度飙升\n- Blackstone+Google合资建TPU云，初期500MW，2027年上线\n- Akamai与Anthropic签下18亿美金、7年云服务合同\n- IREN与NVID\n\n[... middle omitted ...]\n\nrs: Recent neocloud M&A activity (IREN/Mirantis, Nebius/Eigen AI) has been focused on adding vertically integrating orchestration and optimization layers to into GPU compute capacity. This evo\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R021",
    "title": "ASCO 2026的真正信号：日本药企的差异化正在被重新定价",
    "digest": "[wechat_article.md]\n# ASCO 2026的真正信号：日本药企的差异化正在被重新定价\n\n每年ASCO都会带来一批令人振奋的临床数据，但真正值得产业决策者关注的，不是某个药物PFS延长了多少个月，而是这些数据如何改变竞争格局的底层逻辑。今年，某外资投行的日本医药研报揭示了一个被市场低估的结构性变化：日本头部药企的管线价值，正在从“跟随式创新”转向“差异化定价权”的验证期。\n\n这份报告的判断核心并非某个具体药物能否获批，而是：**当全球大药企在PD-1、ADC、KRAS等热门靶点上陷入同质化竞争时，日本公司能否通过精准的患者分层和更优的安全性/便利性组合，在细分适应症中建立不可替代的定价地位。**\n\n以下是我们从报告数据中提炼出的五个关键洞察，以及一个尚未被充分讨论的潜在风险。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. ONO-4578的积极数据背后，隐藏着一个关于“患者筛选”的经典困境\n\nOno Pharmaceutical的ONO-4578在二线胃癌的Phase 2试验中，整体PFS达到了9.0个月对6.9个月的统计学显著改善（HR 0.67）。这看起来是明确的积极信号。但研报在子组分析中指出了关键细节：疗效优势几乎完全集中在PD-L1阳性（CPS≥1）患者群体中，而在CPS<1或不确定的患者中，不仅没有获益，甚至出现了PFS、OS和ORR的恶化趋势。\n\n这意味着什么？Ono计划今年启动全球Phase 3，但Phase 3的设计将面临一个根本性选择：是全人群入组赌整体阳性，还是预先筛选PD-L1阳性人群以最大化疗效信号？前者可能因为阴性人群的拖累导致最终结果不显著，后者则会显著缩小目标市场。\n\n更值得关注的是，在Claudin 18.2阳性患者中，ONO-4578的改善幅度反而更小。这暗示该药物的作用机制可能与现有生物标志物存在\n\n[... middle omitted ...]\n\n？\n\n这些问题的答案，将直接决定你对日本医药板块的配置方向。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nASCO 2026 日本药企关键数据解读\n\n日本制药新数据速览\n\n🔬 4家药企，5个核心管线，1份研报拆解\n\n最近ASCO2026大会，几家日本药企公布了重要临床数据。我快速梳理了核心看点，帮你省时间。\n\n**1️⃣ 小野药品：ONO-4578 胃癌Ⅱ期数据不错，但别急着乐观**\n\n联合Opdivo+化疗一线胃癌，PFS显著延长（9.0月 vs 6.9月，HR=0.67）。好消息是PD-L1阳性组效果更突出（HR=0.52）。\n\n⚠️ 但亚组分析显示：\n- PD-L1阴性组没有明确获益，甚至呈恶化趋势\n- Claudin18.2阳性患者获益偏小\n- 研报特别标注：这是探索性分析，样本量小\n\n小野计划今年启动全球Ⅲ期，还需更多数据验证。\n\n**2️⃣ 武田：IBI363(TAK-928) 肺癌早期数据亮眼**\n\n与信达合作的双功能药物，一线NSCLC（PD-L1低表达/阴性）确认ORR达81.8%。无论鳞癌/非鳞癌、PD-L1阴性/低表达，都观察到疗效。\n\n研报观点：与之前摘要信息一致，没有重大变化。会继续关注美国Ⅱ期数据。\n\n**3️⃣ 第一三共：Datroway面临竞品挑战，但差异化仍在**\n\n中国竞品sa\n\n[... middle omitted ...]\n\ns an exploratory analysis with a small number of subjects) suggested that the patient group showing high efficacy could be limited. As such, we believe it could take time in order to build or \n\n[... middle omitted ...]\n\nhis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any\n\nsuch system."
  },
  {
    "id": "R022",
    "title": "EM债券曲线正在传递一个被忽视的信号：期限溢价的结构性分化正在取代方向性交易",
    "digest": "[wechat_article.md]\n# EM债券曲线正在传递一个被忽视的信号：期限溢价的结构性分化正在取代方向性交易\n\n过去一个月，新兴市场美元债券收益率曲线几乎没有任何方向性变化。EM整体10s30s利差仅收窄1个基点至68bp，EM投资级收窄1bp至61bp，CEMBI同样收窄1bp至56bp。从任何平均指标看，这都是一个沉闷的市场。\n\n但沉闷的表象之下，个体的分化远比均值剧烈。印尼（INDON）的10s30s曲线一个月内收窄了26bp，而多米尼加（DOMREP）同期陡化了11bp。埃及（EGYPT）曲线斜率高达141bp，是印尼的15倍。这些极端差异不是噪声，它们揭示了一个被均值掩盖的结构性事实：EM债券市场正在从“beta交易”转向“alpha分化”，而大多数投资者仍然在用旧框架衡量风险。\n\n这份来自某外资投行的EM曲线月度报告，提供的不只是一组月度变动数据。它真正值得关注的是：在美债收益率大幅波动（10s30s曲线单月熊陡6bp）的背景下，EM曲线整体保持了惊人的韧性。这背后是信用基本面的分化，而非简单的利率传导。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 美债曲线陡化而EM曲线持稳，意味着EM定价逻辑正在从“利率跟随”转向“信用定价”\n\n报告中最引人注目的对比在于：过去一个月，美国国债10s30s曲线熊陡了6bp（长端利率上升更快），而美国高评级公司债曲线同步熊陡了2bp。但EM整体曲线不仅没有跟随，反而牛平了1bp。\n\n这种背离不是偶然的。它表明EM信用资产的定价锚正在从“无风险利率曲线”向“信用基本面曲线”切换。当美债曲线陡化通常反映通胀预期或期限溢价上升时，EM曲线如果同步陡化，意味着市场认为EM信用风险在恶化——这正是2022年大部分时间发生的情况。但当前EM曲线持稳甚至微幅收窄，说明投资者对EM信用风险的评估没有随美债利率\n\n[... middle omitted ...]\n\n些未解问题，也可以获取包含全部图表和原始数据的完整研报解读。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n新兴市场债的曲线在悄悄变平\n\n📊 曲线变平，但整体形态没变\n\n某外资投行最新研报显示，新兴市场主权债（EMBIG）10s30s曲线在过去一个月温和牛平，从72bp收窄到71bp。亚洲地区是主要驱动力，曲线从44bp大幅收窄到37bp，幅度达7bp。\n\n相比之下，美债10s30s曲线同期熊平了6bp到54bp。新兴市场整体走势与美债不同步，说明更多是区域自身因素在驱动。\n\n1️⃣ 最陡 vs 最平\n- 最陡曲线：埃及（141bp）、PEMEX（121bp）、萨尔瓦多（116bp）、南非（104bp）、沙特（90bp）\n- 最平曲线：印尼（9bp）、SQM（22bp）、GRUMAB（39bp）、EXIMBK（39bp）、ECOPET（41bp）\n\n2️⃣ 一个月变化最大的名字\n- 走陡：多米尼加（+11bp）、CDEL（+9bp）、阿里巴巴（+7bp）、沙特（+7bp）、巴拉圭（+7bp）\n- 走平：印尼（-26bp）、GRUMAB（-13bp）、埃及（-12bp）、SQM（-12bp）、AITOCU（-11bp）\n\n3️⃣ 几个有意思的点\n- 印尼曲线最平只有9bp，且一个月内大幅走平26bp，说明市场对长端供\n\n[... middle omitted ...]\n\nso flattened marginally by -1bp m/m to 56bp, led by Latin America (-1bp m/m to 52bp). The magnitude of the bull flattening was more more substantial in the individual pairs within the region, \n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 02 Jun 2026 02:49 PM HKT\n\nDisseminated 02 Jun 2026 02:49 PM HKT"
  },
  {
    "id": "R023",
    "title": "市场真正低估的不是AI需求，而是存储器供给侧的再定价",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是AI需求，而是存储器供给侧的再定价\n\n过去两年，市场对AI基础设施的投资热情从未冷却，但一个关键问题始终悬而未决：当GPU供给逐步跟上，算力瓶颈是否会从“芯片”转移到“存储”？某外资投行在最新发布的研报中给出了一个清晰的判断——DRAM已经成为AI建设中的首要瓶颈，而这一结构性短缺在2028年前看不到快速解决方案。这意味着，存储器股票当前不到10倍的远期市盈率，不是估值泡沫，而是市场对盈利持续性的定价仍不够充分。\n\n这份报告上调了美光科技的目标价至1050美元，SanDisk至1750美元，并大幅调高了2027年的盈利预测。上调幅度之大——美光2027年EPS预测上调48%，SanDisk上调24%——本身就是一个信号：分析师认为市场对存储器公司未来两年盈利能力的理解存在系统性偏差。\n\n本文将从五个维度拆解这份报告的核心逻辑，并指出报告尚未完全回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮存储器短缺不是周期性的，而是由AI建筑的结构性需求驱动\n\n传统上，存储器行业遵循“繁荣-萧条”周期：供不应求时价格上涨，厂商扩产，随后供过于求，价格暴跌。但这一次，驱动因素发生了根本性变化。\n\n报告明确指出，DRAM短缺的核心原因不是消费电子需求回暖，而是AI基础设施建设的持续扩张。超大规模云服务商对HBM（高带宽存储器）的需求几乎无止境，而DRAM的供给增长却受到两个硬约束：一是洁净室建设周期，二是EUV光刻设备的可用性。这两个因素都不是短期能解决的。\n\n报告引用了在台湾的调研反馈：供应链预期DRAM价格在5月季度上涨40%，8月季度再涨15%，甚至高于分析师的模型假设。这意味着，即便分析师已经上调了价格预期，真实市场可能比模型更紧。\n\n这里的关键洞察是：存储器短缺已经从“周期性事件\n\n[... middle omitted ...]\n\n盈利预测，这些数据对于构建自己的投资框架至关重要。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nDRAM短缺，AI基建的硬瓶颈\n\n存储缺芯，没那么快解决\n\n某外资投行刚上调了存储芯片的目标价，核心逻辑是：缺货不是短期现象，可能持续2-3年甚至更久。\n\n1️⃣ DRAM是AI基建的“卡脖子”环节\n超大规模云厂商愿意为DRAM支付高价，因为它是AI算力扩张的主要瓶颈。供给端受限——洁净室和EUV光刻机产能扩张很慢，短期内难以快速放量。\n\n2️⃣ NAND同样紧张，但偏好不同\n超大规模厂商正在抢购高性能NAND，改变了需求结构。但PC和手机需求偏弱，所以相对更看好DRAM占比更高的公司。\n\n3️⃣ 估值还有空间\n两家公司按2027年盈利预期算，PE都不到10倍。研报认为随着市场意识到盈利持续性更强，估值还有扩张空间。\n\n4️⃣ 回购和HBM谈判是催化剂\n2027年有望启动大规模回购，HBM（高带宽内存）合同价格也在重新谈判中，这些都是后续看点。\n\n5️⃣ 供给增长缓慢，资本开支不是解药\n虽然资本开支很高，但大部分被HBM产能消耗，实际比特供给增长有限。新建产能要到2027/2028年才能释放。\n\n📌 一句话：存储缺货的“紧日子”还没到头，供需矛盾是当前的核心逻辑。\n\n你觉得存储芯片的景气周期还能持续多久？欢迎\n\n[... middle omitted ...]\n\nays\n\nDRAM the principle bottleneck in the AI buildout, NAND still very tight, driving continued growth in FCF/EPS as long as AI spending persists   \nBoth MU and Sandisk still <10x PE leaves ro\n\n[... middle omitted ...]\n\n026)</td><td>$402.71</td></tr><tr><td>Cadence Design Systems Inc (CDNS.O)</td><td>O (02/14/2024)</td><td>$416.39</td></tr><tr><td>Synopsys Inc. (SNPS.O)</td><td>E (02/27/2026)</td><td>$508.35</td></tr></table>\n\n© 2026 MS"
  },
  {
    "id": "R024",
    "title": "消费支付数据回暖，但市场真正低估的是银行非息收入的修复弹性",
    "digest": "[wechat_article.md]\n# 消费支付数据回暖，但市场真正低估的是银行非息收入的修复弹性\n\n这份来自某外资投行的研报，在2026年一季度的支付数据中捕捉到了一个被官方零售数据掩盖的转折信号。总系统支付量同比大幅反弹29%，银行卡消费支付在经历了2025年全年负增长后，首次转正至同比上升3.2%。这些数字本身并不令人意外，真正值得关注的是，它们正在讲述一个与官方消费数据截然不同的故事。\n\n官方社会消费品零售总额增速在2026年一季度进一步放缓至2.4%，但支付数据的表现却明显优于这一读数。某外资投行的分析师认为，这种背离可能源于消费从线上向线下渠道的结构性回流。如果这一判断成立，那么市场对银行盈利能力的评估将需要重新校准——尤其是那些长期被低估的非息业务收入。\n\n报告中最具冲击力的数字，是分析师估算的家庭金融资产在2026年一季度实现了10.8%的同比增长，主要由股票和共同基金驱动。这意味着，尽管宏观叙事仍然充满不确定性，但居民部门的资产负债表正在以比大多数人预期的更快的速度修复。而这一点，恰恰是市场目前定价最不充分的变量。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 支付数据的“背离”揭示的不是消费疲弱，而是渠道结构的深刻重置\n\n2026年一季度，官方零售销售增速从2025年全年的水平进一步下滑至2.4%。如果只看这个数字，很容易得出“消费依然疲弱”的结论。但支付数据给出了完全不同的信号。\n\n银联支付增速反弹至11.2%，网联支付增速也维持在7.2%的合理水平。两者均显著高于官方零售增速。更关键的是，总系统支付量同比飙升29%，对比2025年四季度的仅5%增速，这是一个数量级的跃升。\n\n这种背离并非统计误差。某外资投行在报告中提出了一个尚未被市场充分讨论的解释：消费正在从线上渠道回流至线下。如果这一判断成立，那么官方零售数据可能系统性低\n\n[... middle omitted ...]\n\n理完毕，可以结合更多银行的个案数据，一起推演后续的投资逻辑。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n消费支付回暖，银行卡数据转正\n\n支付数据正在说话\n\n某外资投行最新研报显示，1Q26系统支付总量同比大增29%，银行卡消费支付同比转正至3.2%，而官方零售增速已放缓至2.4%。\n\n1️⃣ 支付数据 vs 零售数据\n网联+银联支付增长7.2%和11.2%，明显跑赢社零增速。背后可能是消费从线上回流线下，银行卡支付重回正轨。\n\n2️⃣ 银行卡消费转正\n2025年银行卡消费还在下滑，1Q26已回到3.2%正增长。银行对信用卡贷款仍偏谨慎，但趋势在改善。\n\n3️⃣ 家庭金融资产增长\n估算1Q26家庭金融资产增长10.8%，主要由股票和基金带动。结合消费支付回暖，对银行手续费收入是支撑。\n\n一个观察：支付数据比官方消费数据更早反映真实消费温度，两者差距值得持续跟踪。\n\n#学习笔记\n\n[source_mineru.md]\n## China Financials | Asia Pacific\n\n# 1Q26: healthy payment data; Some consumption payment returned to bank cards\n\n## Key Takeaways\n\nTotal system payme\n\n[... middle omitted ...]\n\n rebounded to 11.2% yoy; while NetsUnion payment growth slightly moderated to 7.2% yoy, also above official retail sales growth.  \n- Household financial asset growth remained decent in 1Q26, u\n\n[... middle omitted ...]\n\npment Bank (600000.SS)</td><td>E (08/05/2025)</td><td>Rmb9.37</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R025",
    "title": "中国自动化需求的真实底色，被季节性波动掩盖了",
    "digest": "[wechat_article.md]\n# 中国自动化需求的真实底色，被季节性波动掩盖了\n\n理解中国制造业投资，不能只看月度环比。2026年5月的数据提供了一个关键信号：当市场将注意力集中在电子和电池行业的季节性回调时，机床工具、纺织机械和通用机械领域的订单正在悄然走强。这份来自某外资投行的研报，通过对台湾气动元件龙头亚德客（Airtac）最新销售数据的拆解，揭示了一个正在发生的结构性变化——AI数据中心投资正在成为自动化需求的新引擎，而这一轮增长的质量和持续性，可能与过去依赖新能源和消费电子的周期有本质不同。\n\n报告的核心判断是：5月亚德客日均销售额同比增长26%，环比仅微降1%，这远好于市场对“五月淡季”的悲观预期。更重要的是，订单价值连续第几个月超过出货价值，意味着积压订单仍在积累。这不是一个需求疲软的信号，而是供给端正在被结构性力量重塑的迹象。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 季节性的回调，掩盖了机床和通用机械的加速上行\n\n5月亚德客销售额环比下降10%，表面看符合季节性规律——劳动节长假减少了工作日。但日均销售额仅环比下降1%，说明需求的内在强度远超表面数据。更值得关注的是分行业表现。\n\n电子行业销售额同比增长12%，电池行业增长55%，但两者均较4月有所回落。报告明确指出，这很大程度上归因于季节性因素。真正超出预期的是机床工具行业，销售额同比增长35%，且较4月的高位继续攀升。纺织机械、包装机械和通用机械的订单也呈现环比改善。\n\n这意味着什么？过去两年，市场习惯将中国自动化需求与消费电子周期和新能源扩产周期挂钩。当这两个领域进入季节性调整时，市场容易得出“需求走弱”的结论。但本轮的不同之处在于，机床工具行业的持续走强，暗示着更底层的资本开支逻辑正在切换——从产能扩张驱动的自动化采购，转向效率提升和技术升级驱动的设备更新。\n\n!\n\n[... middle omitted ...]\n\n织对关键变量的跟踪讨论。这里不是终点，而是更深入对话的起点。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n气动元件5月数据：谁在撑起增长\n\n自动化需求分化，AI基建成新引擎\n\n某外资投行刚发了5月中国工厂自动化数据解析，核心看点是：整体需求不错，但行业间冷热不均。我拆几个关键点👇\n\n**1/ 龙头公司5月表现**\n台湾气动元件厂商Airtac（约90%收入来自中国）5月人民币计销售额同比+26%，环比-10%。考虑五一长假，调整后日均销售额同比+26%、环比仅-1%，基本持平4月——而4月通常是年内高点。公司表示5月订单和出货均创同期新高，订单继续超过出货。\n\n**2/ 行业分化明显**\n- 电子（占比26%）：同比+12%，环比回落（季节性）\n- 电池（占比18%）：同比+55%，环比回落（季节性）\n- 机床（占比8%）：同比+35%，环比继续走高\n- 纺织机械（占比5%）：同比+46%，环比提升\n- 光伏相关（占比3%）：同比-5%，环比继续走弱\n\n**3/ 机床订单的亮点**\n研报特别指出，机床行业订单从4月高位进一步上升，主要受益于AI数据中心投资增加。这逻辑很顺：AI基建→算力需求→设备采购→带动自动化零部件。\n\n**4/ 政策预期**\n公司管理层提到，国家“十五五”规划强调智能制造和工业升级，预期政府\n\n[... middle omitted ...]\n\n(assuming 20.5 business days), broadly in line with April, the period that follows the Lunar New Year and is likely to represent the highest level of the year.\n\nThe company's comments did not \n\n[... middle omitted ...]\n\nation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Securities Co., Ltd., Japan. All rights reserved."
  },
  {
    "id": "R026",
    "title": "人民币中间价的定价权，正在发生一次静默转移",
    "digest": "[wechat_article.md]\n# 人民币中间价的定价权，正在发生一次静默转移\n\n市场对人民币汇率的讨论，长期集中在两个焦点：一是中美利差，二是关税政策的短期冲击。但某头部外资投行最新发布的中间价模型报告，揭示了一个更值得关注的信号——决定人民币每日交易基准的定价机制，正在经历一次结构性的、但尚未被充分定价的调整。\n\n这份报告的核心判断是：模型投影的美元兑人民币中间价，正在系统性偏离实际公布的中间价，且偏离的方向和幅度，已经不能用传统的“逆周期因子”来解释。这意味着，央行对汇率的管理框架，可能已经从“被动对冲外部波动”转向了“主动引导预期锚定”。\n\n本文将基于该报告的核心数据与模型逻辑，拆解这一判断背后的三个层次：模型本身在说什么、模型错误意味着什么、以及这些变化对资产定价和交易策略的启示。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 模型投影与真实中间价的差距，正在揭示一个主动管理信号\n\n报告给出了两组关键数字。第一组是纯粹的模型投影：基于一篮子货币的隔夜变动，模型计算出2026年6月3日的中间价应为6.7705，较前一日官方收盘价低482个基点。第二组是加入逆周期因子后的投影：6.7957，较前一日实际中间价低230个基点。\n\n这两组数字的差值，就是市场通常理解的“逆周期因子”的贡献。但真正值得关注的不是差值本身，而是差值的动态变化。报告没有直接给出历史序列，但从模型误差的历史图表（Fig. 2）中可以看到，模型误差在2025年1月曾达到-1800个基点，随后在2025年中收窄至0附近，2026年初又反弹至+600个基点。\n\n这意味着什么？模型误差的波动，本质上反映了央行对模型结果的“干预强度”。当误差为正时，说明实际中间价高于模型投影（即央行在引导人民币贬值）；当误差为负时，说明实际中间价低于模型投影（即央行在引导人民币升值）。2026\n\n[... middle omitted ...]\n\n在“主动引导”框架下，人民币相关资产的定价逻辑需要如何调整。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n人民币中间价，一个关键信号变了\n\n模型预测：6.7705\n\n较上次预测低了482个基点\n\n---\n\n最近某外资投行更新了人民币中间价预测模型，几个数字值得关注。\n\n1️⃣ 模型预测值大幅下移\n最新模型预测USD/CNY中间价为6.7705，较上次的6.8187低了482个基点。计入逆周期因子后，预测值为6.7957，也比上次低了230个基点。\n\n2️⃣ 主要贡献来自这些货币\n隔夜变动中，对预测贡献最大的四个货币对分别是：卢布（+33.5点）、欧元（+21点）、泰铢（+9点）、日元（+8点）。新兴市场货币和欧元区货币的波动正在传导至人民币定价。\n\n3️⃣ 模型误差在缩小\n从年初到现在，模型每日误差从-1800点逐步收窄至600点左右。虽然仍有偏差，但模型对中间价的拟合能力在改善。\n\n4️⃣ 下半年关键事件密集\n7月底政治局会议、10月国庆假期、11月APEC深圳峰会、12月中央经济工作会议，以及年底可能的中美元首会晤。这些事件都会影响汇率定价逻辑。\n\n汇率定价从来不是单一变量，而是多股力量的博弈结果。你觉得下半年影响人民币走势的核心因素会是什么？\n\n#学习笔记\n\n[source_mineru.md]\n## US\n\n[... middle omitted ...]\n\nge (without counter-cyclical factor)  \n![](images/b9a210511ffb196e9962a4818f54ff019a3be74d5ade3731989b37b54f74aacd.jpg)\n\n<details>\n<summary>bar chart</summary>\n\nTop 4 weighted contribution to \n\n[... middle omitted ...]\n\nrmation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R027",
    "title": "五月新能源车销量超预期，但市场真正低估的不是需求，而是供给侧的再定价",
    "digest": "[wechat_article.md]\n# 五月新能源车销量超预期，但市场真正低估的不是需求，而是供给侧的再定价\n\n五月新能源车销量数据出炉，整体好于市场预期。某外资投行最新研报显示，纳入已披露数据的品牌后，五月新能源车行业批发量环比增长12%，同比增长7%，超出此前市场一致预期。比亚迪、蔚来、零跑、华为鸿蒙智行等品牌均录得显著环比增长。\n\n这份数据本身并不令人意外。真正值得关注的，是数据背后正在发生的结构性变化：行业竞争格局正在从“谁能卖得多”转向“谁能在规模增长中守住定价权”。5月销量超预期的背后，隐藏着一个尚未被市场充分定价的供给侧再平衡过程。\n\n报告的核心判断并非“需求回暖”，而是“供给侧的效率分化正在加速”——头部企业的规模优势开始转化为成本与定价的双重能力，而这一转化过程，将重新定义未来12个月中国新能源车行业的投资逻辑。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 比亚迪的出口爆发正在改变其估值逻辑，国内市场的同比持平反而成为安全垫\n\n比亚迪5月新能源车总销量38.35万辆，同比持平，环比增长19%。乍看之下，同比零增长似乎缺乏亮点。但深入拆解结构，真正的增量来自海外：5月海外销量达到16.06万辆，环比增长19%，前五个月累计海外销量61.69万辆，同比增长65%。\n\n这一数据意味着什么？比亚迪的海外销量占比已从去年的约20%提升至当前的约42%。当一家公司的海外业务增速达到65%，且月销量已经突破16万辆时，其估值框架就不能再仅用国内市场份额来定价。\n\n更值得关注的是，国内市场的同比持平，恰恰说明比亚迪在国内的定价策略正在从“以量换价”转向“以价换量”。5月纯电动车型销量19.87万辆，同比下降3%，而插电混动车型销量17.83万辆，同比增长3%。这一结构变化表明，比亚迪正在国内主动控制纯电产品的促销力度，转而通过插混产品维持量价平\n\n[... middle omitted ...]\n\n会在社群中分享完整报告的解读笔记，并持续跟踪后续数据的变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月新能源车销量：几家欢喜几家愁\n\n5月销量超预期\n\n5月新能源车批发量环比+12%，同比+7%，超市场预期。几家头部品牌表现亮眼，但分化明显。\n\n1/ 比亚迪出口大超预期\n5月新能源车销量38.3万辆，环比+19%。海外销量16.1万辆，环比+19%，前5月累计出口超61.7万辆，同比+65%。腾势环比+45%，方程豹+4%，仰望+8%。纯电占比52.7%，插混占比47.3%。\n\n2/ 新势力阵营分化\n蔚来表现亮眼，5月交付3.8万辆，同比+62%，环比+28%。乐道环比+125%，萤火虫+14%。\n零跑8.2万辆，同比+81%，环比+14%，势头强劲。\n理想3.3万辆，同比-18%，环比-2%，略显疲态。\n小鹏3.2万辆，同比-4%，环比+4%，稳中有升。\n\n3/ 华为系订单爆发\n5月交付4.6万辆，环比+41%。新M9上市24小时订单超2万，智界V9 48小时订单超1万，M6首月订单超2万，后续交付值得关注。\n\n4/ 其他品牌\n极氪3.4万辆，同比+82%，环比+8%。\n广汽埃安3.3万辆，同比+24%，环比+1%。\n长城汽车10万辆，环比-6%，新能源渗透率30%。\n\n整体来看，5月新能源车市热度提升\n\n[... middle omitted ...]\n\nes of 383.5k units (+0% YoY/+19% MoM) and May-26 NEV PV sales of 377.0k units (+0% YoY/+20% MoM). 5M26 sales -20% YoY to 1.41mn units. May Denza +45% MoM to 16,303 units, Fangchengbao +4% MoM \n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R028",
    "title": "市场真正低估的不是算力需求，而是AI基础设施的供给结构正在被重新定义",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是算力需求，而是AI基础设施的供给结构正在被重新定义\n\n当NVIDIA CEO黄仁勋在GTC上宣布Vera Rubin已进入全面量产，以及Qualcomm在Computex上推出数据中心品牌Dragonfly时，市场大多将注意力集中在算力升级的节奏上。但某外资投行最新研报揭示了一个更重要的信号：这两场演讲共同宣告，AI行业已从“基础大语言模型”的静态问答范式，正式转入“代理式AI”与“物理AI”时代。这个转变的真正含义，不是GPU卖得更多，而是整个AI基础设施的供应链结构、芯片架构和商业模式都在经历一次根本性的重构。\n\n报告的核心判断值得认真对待：市场低估的不是需求端，而是供给侧的再定价。当NVIDIA从一家GPU系统公司进化为全栈AI基础设施公司，当Qualcomm将边缘芯片的触角延伸至数据中心，当Vera CPU开始侵蚀x86在服务器处理器中的份额——这些变化叠加在一起，意味着中国AI产业链上许多公司的竞争位置和估值逻辑需要被重新审视。\n\n以下是我们从这份研报中提炼出的五个关键洞察，以及一个报告尚未完全回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. Vera Rubin量产不是一次常规升级，而是NVIDIA从“卖芯片”到“卖工厂”的转折点\n\nVera Rubin进入全面量产，对于供应链而言，确认了2026年下半年的拉货周期。但研报真正值得注意的，是NVIDIA在GTC上对自己定位的重新定义：它不再是一家GPU公司，而是一家全栈AI基础设施公司。\n\n这个表述不是公关话术。报告指出，NVIDIA暗示其供应链控制将从L10（板卡级）延伸到L11（机柜级）和L12（集群级）。Vera Rubin DSX AI Factory参考设计已经展示了一个完整的AI工厂基础设施堆栈，包括NV\n\n[... middle omitted ...]\n\n表和更多细节解读。欢迎加入讨论，一起推演这些变化的二阶影响。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI进入agent时代，英伟达高通都在押注什么？\n\nAI Agent时代来了\n\n英伟达和QCOM的Keynote，透露了AI从“对话式”到“自主执行”的转变。\n\n1️⃣ 英伟达：从GPU公司到全栈AI基础设施商\n- Vera Rubin已进入商用生产阶段，供应链2H26开始上量。\n- 自研Vera CPU，专为Agentic AI设计，88核单芯片，SQL处理快3倍，流数据处理快6倍。\n- RTX Spark平台，把1 petaflop算力塞进笔记本，本地跑AI Agent，不用连云端。\n- 英伟达现在管的不只是服务器，而是整个机柜、集群级别的系统。\n\n2️⃣ 高通：从手机芯片到数据中心全覆盖\n- 发布Dragonfly，正式进军数据中心市场。\n- Snapdragon变成AI Agent原生执行平台，Claude、Gemini都直接跑在上面。\n- 车、机器人、6G，全部纳入AI框架。\n\n3️⃣ 中国产业链影响\n- 某外资投行认为，Vera CPU采用LPDDR5X内存架构，长期可能影响传统DIMM芯片需求。\n- 高通的Dragonfly，可能为国内ASIC数据中心方案提供新选择。\n- 联想作为生态伙伴，同时\n\n[... middle omitted ...]\n\nsee positive implications for Lenovo, which is also one of ecosystem partners set to benefit from the new GPU server platform and Nvidia Windows-based laptops with higher ASPs. We also watch f\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R029",
    "title": "市场真正低估的不是需求，而是供给侧的再定价",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是需求，而是供给侧的再定价\n\n2026年6月，某外资投行举办了其中国房地产专家电话系列的首场会议，邀请趋势动物创始人聂聪分享对市场的判断。这份研报的核心信号并非“市场何时见底”这类老问题，而是一个更结构性的判断：中国房地产市场的复苏路径正在从“是否复苏”演变为“不同资产类别之间的持续分化”。这种分化不是暂时的波动，而是供给结构、政策工具和需求偏好共同作用下的新均衡。\n\n多数投资者仍在等待一个统一的拐点信号——全国房价普涨、成交量全面回暖。但这份研报呈现的证据指向另一个方向：市场正在被切割成三个截然不同的价格体系——政府回购支撑的微型单元、高租金收益率的非核心城市资产、以及仍在加速下跌的中高端改善型住房。这三条线的逻辑不同，驱动因素不同，对投资组合的含义也不同。\n\n更值得关注的是，报告提出了两种截然不同的复苏情景。在基准情景下，复苏将是一个“从两端向中间渗透”的缓慢过程——优质新房和高收益率资产先行，中端住宅随后跟进，且节奏取决于各城市的库存水位。而在大规模政策刺激情景下，市场可能复制香港模式——风险偏好快速扩张，中价位住宅价格迅速反弹。这两种情景对资产定价的含义完全不同，而当前市场定价隐含的是哪一种，恰恰是最大的未解问题。\n\n以下是我们从这份研报中提炼出的几个关键判断，以及它们对投资框架的含义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 全国房价跌幅收窄的背后，是三个完全不同的价格体系在同时运行\n\n如果只看全国层面的月度数据，结论可能是温和的：全国二手房价格指数月环比跌幅已经从年初的-0.5%收窄到近期的-0.4%。但这份收窄并不是因为“所有房子都跌得少了”，而是因为三个价格体系的力量在同时作用。\n\n第一个体系是政府回购驱动的政策性市场。上海50平方米以下的微型单元自2025年11月触底以\n\n[... middle omitted ...]\n\n群中继续讨论。欢迎来星球微信群，一起跟踪这些关键变量的变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n二手房市场出现分化信号\n\n**分化加速，关注这3点**\n\n**上海深圳已企稳，其他城市还在等**\n\n最近投行研报里，一位专注于二手房市场周期的专家分享了一些有意思的观察。整理了几个核心判断，信息量不小👇\n\n**1/ 全国二手房跌势放缓，但分化明显**\n- 5月以来全国二手房价格月度跌幅收窄至-0.4%～-0.5%，相比去年下半年明显改善。\n- 但城市间差异巨大：上海小户型（50-70㎡）从1月低点已涨11%，深圳中高端住宅（总价1000-2000万）也开始企稳回升。\n- 而北京、广州大部分房源仍在承压，杭州、成都的高端项目3月以来加速调整。\n\n**2/ 两类资产率先触底**\n- 高租金收益类：乌鲁木齐核心区（租金收益率3.6%）、大理旅游养老盘（租金约3%）价格已止跌反弹。\n- 政府回购类：上海政府加速收购存量房做保障性租赁住房，直接托底了50㎡以下小户型价格。\n\n**3/ 未来两条路径**\n- 基准情景：没有大规模刺激，优质新房和高租金资产先涨，逐步传导至中端房源，但节奏取决于库存——一线城市库存9-32个月，弱二线14-479个月，三四线更高。\n- 乐观情景：类似香港模式，大幅降息+加速收储，市场风险偏好\n\n[... middle omitted ...]\n\nat the nationwide secondary housing price decline moderated entering May-26 and highlighted two notable trends: 1) structural segment out-performance in Shanghai (led by small-size and low-tot\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R030",
    "title": "KRAS G12C的真相：不是所有抑制剂都一样，组合疗法的门槛比想象中更高",
    "digest": "[wechat_article.md]\n# KRAS G12C的真相：不是所有抑制剂都一样，组合疗法的门槛比想象中更高\n\nASCO 2026进入第二天，讨论的焦点从前沿探索转向了一线治疗的格局重塑。这份某外资投行发布的第二天要点解析，透露出一个清晰但容易被忽略的信号：市场正在为KRAS G12C抑制剂寻找合理的临床定位，但真正的变量不是机制本身，而是分子层面的差异和组合策略的选择门槛。\n\n报告的核心判断可以浓缩为一句话：KRAS G12C单药在一线非小细胞肺癌中的故事线比组合疗法更清晰，而组合疗法的有效性虽然真实存在，但需要更精细的患者分层、更主动的不良反应管理和更严格的剂量连续性。这不是一个“谁更好”的问题，而是一个“谁更适合哪种场景”的格局判断。\n\n以下是我们从这份报告中提炼出的五层洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 单药在一线的故事线比组合更干净，但“干净”不等于“容易”\n\n讨论者对于Divarasib和Elisrasib的数据给出了一个有趣的信号：对单药在一线的前景更有信心。这不是否定组合疗法的价值，而是承认了一个现实——当疗效与毒性需要权衡时，单药方案的确定性更高。\n\n报告特别强调了一个容易被忽视的细节：讨论者认为，化疗联合方案相比免疫联合化疗的长期生存优势有限。这意味着，如果组合疗法的设计只是简单地“把化疗加进去”，而不是考虑与免疫检查点抑制剂的协同，那么这条路径的长期价值可能被高估。\n\n对于专注于KRAS G12C的中国生物科技公司——如Abbisko、Genfleet、Jacobio——这个判断意味着，单药适应症的推进速度可能比市场预期的更具竞争力，前提是分子本身具备足够好的药代动力学特性和安全性窗口。但报告也隐含了一个未完全回答的问题：什么样的单药活性才算“足够好”？这个阈值尚未被明确界定。\n\n![研报原图 2](a\n\n[... middle omitted ...]\n\n始图表和我们的逐段解读，也会持续跟踪ASCO后续的讨论进展。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nASCO Day 2：KRAS战线前移，ADC拼组合\n\nASCO 2026 投研笔记\n\nDay 2 的焦点：前线治疗策略 vs 毒性管理\n\n1️⃣ KRAS G12C：单药 vs 联合的争论\n- 讨论者对单药作为一线疗法更有信心，联合疗法虽然疗效明确，但需要更精细的患者选择（PD-L1、共突变、CNS状态）\n- 核心挑战：肝毒性管理和剂量调整是关键\n- “不是所有G12C抑制剂都一样”——分子层面的PK、CNS穿透和毒性差异很大，ON/OFF机制并不能完全解释持久性\n\n2️⃣ 非G12C和泛RAS：格局还在变\n- 胰腺癌的联合方案目前以化疗为主\n- 未来需要关注MAPK通路搭档、谱系可塑性和皮肤/消化道毒性对生活质量的影响\n- 1L探索仍在继续，但约束条件不少\n\n3️⃣ ADC：1L应用的浪潮\n- 尿路上皮癌、三阴性乳腺癌、HER2+乳腺癌都在推动ADC进入一线\n- 核心议题：联合 vs 序贯，如何实现可耐受的给药方案\n- 下一代创新方向：双载荷/双抗ADC，尤其是超越拓扑异构酶/微管蛋白的新型载荷\n- 需要关注：连接子稳定性、生物标志物依赖性和交叉耐药\n\n🇨🇳 对中国biotech的启示\n- RAS领域：关\n\n[... middle omitted ...]\n\nd; chemo-heavy paths, MAPK partners, lineage plasticity and derm/GI QoL tox remain constraints to watch in 1L.  \nChina read: RAS implications for Abbisko/Genfleet/Jacobio; ADC debate favors Du\n\n[... middle omitted ...]\n\n Co. Ltd. (600216.SS)</td><td>E (02/28/2025)</td><td>Rmb12.89</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R031",
    "title": "肺癌一线治疗变局：真正值得关注的不是单一数据，而是两类新机制的“交叉验证”",
    "digest": "[wechat_article.md]\n# 肺癌一线治疗变局：真正值得关注的不是单一数据，而是两类新机制的“交叉验证”\n\nASCO 2026 的 NSCLC 专场，数据密度极高。但如果我们只提炼一个判断，它应该是：**一线肺癌的标准治疗正在从“PD-1 单药或联合化疗”的单一范式，转向“TROP2 ADC 联合免疫”与“PD-1xVEGF 双抗联合化疗”两条技术路线的并行竞争。** 市场对 Keytruda 2028 年专利到期的担忧早已存在，但 ASCO 这次提供的关键信号在于：挑战者不再只是“另一个 PD-1”，而是两种作用机制截然不同的新药。它们各自的数据，正在交叉验证一个更大的命题——Keytruda 的统治地位并非不可撼动，但取代它的方式可能不止一种。\n\n某外资投行在 ASCO 后的研报中，系统梳理了这两条路径的最新进展。本文基于该报告的核心逻辑，提炼出对产业决策者和投资者真正重要的几个层次。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. TROP2 ADC 的数据增量有限，但“联合用药”的策略信号远比单药 PFS 更重要\n\nMRK/Kelun 的 Sac-TMT（TROP2 ADC）在 ASCO 上公布了 OptiTROP-Lung05 的中国 III 期数据：Sac-TMT 联合 Keytruda 对比 Keytruda 单药治疗 PD-L1 阳性 NSCLC。中位 PFS 未达到 vs 5.7 个月，HR 显著。从数字上看，这符合市场预期——此前模型预测的联合组中位 PFS 约 15-17 个月，与本次公布的参数模型预测值（15.0-17.5 个月）高度一致。研报明确指出，这是“增量正面更新”，而非颠覆性突破。\n\n真正值得关注的是两个隐含信息。第一，Sac-TMT 在 PD-L1 TPS 1-49% 亚组中的 PFS HR 为 0.28\n\n[... middle omitted ...]\n\n业（Big Pharma vs Biotech）的战略含义。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n肺癌一线治疗，ASCO 最新战况\n\n**前线战报**\n\n**PD-1 专利到期前的关键备选方案**\n\nASCO 刚结束，肺癌一线治疗（1L NSCLC）的格局正在被重塑。目前这个市场被某款 PD-1 单抗+化疗统治，但它的专利 2028 年就到期了。这次大会，最值得关注的两条技术路线：**TROP2 ADC** 和 **PD-(L)1xVEGF 双抗**。\n\n1️⃣ **TROP2 ADC：数据不错，但全球验证还在路上**\n\n某款 TROP2 ADC 在中国 3 期临床（PD-L1 阳性人群）中，联合 PD-1 单抗 vs PD-1 单抗，中位 PFS 还没达到，但模型预测在 **15-17 个月**左右，和预期一致（约 15-20 个月）。客观缓解率（ORR）是 **70.2% vs 42.0%**。\n\n⏳ 关键点：OS 数据还不成熟，但趋势有利（HR 0.55）。副作用主要是 ADC 带来的血液毒性和口腔炎，但整体可控，停药率低。\n\n⚠️ 注意：这只是中国数据，**更关键的全球 3 期数据要等今年晚些时候**。另外，它在 PD-L1 低表达人群中的策略也还不清楚。\n\n2️⃣ **PD-(L)1xVEGF \n\n[... middle omitted ...]\n\nrged as some of the leading strategies to attempt to improve upon or replace Keytruda (PD1 antibody, which goes off patent in 2028). MRK is uniquely positioned in that it has a drug in each ca\n\n[... middle omitted ...]\n\narantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n© 2026 MS"
  },
  {
    "id": "R032",
    "title": "市场低估的不是AI算力需求，而是IT服务商从“系统开发”到“代理设计”的职能跃迁",
    "digest": "[wechat_article.md]\n# 市场低估的不是AI算力需求，而是IT服务商从“系统开发”到“代理设计”的职能跃迁\n\n当全球投资者还在争论AI的资本开支何时见顶、企业AI应用的ROI是否成立时，一份来自某外资投行的日本IT服务行业研报，提供了一个更具结构性的观察视角。这份报告的核心判断并非关于算力采购的规模，而是关于AI价值链正在发生的、不易被察觉的职能转移：企业IT服务商（Sler）的业务核心，正在从传统的系统开发，转向企业级AI代理（Agent）的设计、管理与安全。这个转变，将重新定义该行业的定价权与增长天花板。\n\n当前市场对AI的讨论，大多集中在模型能力、算力需求和基础设施投资上。但真正决定未来几年产业格局的，可能是“谁来把通用AI能力转化为企业可用的、成本可控的专用代理”。这份报告从NVIDIA Computex主题演讲中捕捉到的信号表明，这个问题的答案正在向IT服务商倾斜。而这恰恰是当前估值模型中尚未完全定价的部分。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI ROI的困境正在催生一个新的中间层市场，而IT服务商是天然承接者\n\n企业AI应用的ROI问题，已成为制约下一阶段部署的关键瓶颈。报告引用了Uber COO的公开表态——生产力提升是否足以证明AI的token成本是合理的，目前仍不清晰。与此同时，Amazon的策略正在从“最大化token使用量”转向“优化token使用量”。这不是孤立现象。随着模型能力提升，OpenAI API等服务的成本也在持续上升，部分企业已经开始质疑这些支出的合理性。\n\n这个困境的本质是什么？不是AI没有价值，而是通用模型的“一刀切”模式在企业场景中产生了大量无效成本。企业需要的是针对特定任务、经过优化、成本可控的专用代理，而不是每次调用都让一个庞大的通用模型从头“思考”。\n\nNVIDIA在Com\n\n[... middle omitted ...]\n\n路线图与Sler业务协同性的分析，也值得深入探讨。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI赚钱吗？英伟达给了新答案\n\n📌 企业AI ROI的解法来了\n\n某外资投行最新研报拆解了英伟达Computex演讲，核心围绕两个问题：AI到底能不能赚回成本？以及物理AI怎么落地？\n\n1️⃣ 从训练到推理再到Agent，IT服务商的角色变了\n- 英伟达认为，AI正从“训练模型”转向“推理应用”，再进入“Agent智能体”阶段\n- 企业如果要用Agent，不能花大钱，必须低成本、高效率地设计专属Agent\n- 英伟达的方案是推出Nemotron 3 Ultra开源模型——便宜又好用，专为企业做Agent服务\n- 这意味着IT服务商的业务，将从“系统开发”变成“企业AI Agent的设计、管理和安全”\n\n2️⃣ AI ROI争议：Uber说看不清，亚马逊在优化用量\n- 研报提到，Uber的COO直言：生产力提升到底能不能覆盖AI的token成本，还不清楚\n- 亚马逊则从“最大化token使用”转向“优化token使用”\n- 背后的现实是：OpenAI等API费用在涨，有些企业已经扛不住成本\n- 但英伟达的Nemotron 3 Ultra开源模型，正好回应了这个ROI痛点\n- 未来企业会按任务难度和重要性，选择不\n\n[... middle omitted ...]\n\nemotron 3 Ultra model, emphasizing the importance of affordable and fast open models. The implication is that Sler operations may transform from system development → enterprise AI agent design\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R033",
    "title": "日本IT服务业的真正分化点：谁能在AI驱动的效率红利中，把成本节约转化为利润增长",
    "digest": "[wechat_article.md]\n# 日本IT服务业的真正分化点：谁能在AI驱动的效率红利中，把成本节约转化为利润增长\n\n过去几个季度，市场对日本IT服务业的关注焦点一直集中在“需求是否可持续”。金融系统升级、企业数字化转型、政府IT现代化——这些驱动因素看起来都足够坚实。但最近一份覆盖三家非覆盖公司的研报，揭示了一个更微妙的信号：需求侧的故事已经不够用了。真正区分赢家与输家的，不再是订单增长的快慢，而是企业能否在AI驱动的开发效率提升中，把节省下来的人月成本重新转化为利润，而不是被客户的价格压力或内部的费用膨胀所吞噬。\n\n这份研报通过对Simplex Holdings、NSD和DTS三家公司的实地调研，提供了一个极具价值的“对照实验”视角。三家公司同属金融IT服务领域，面对相似的市场环境，但它们的盈利前景却出现了显著分化。Simplex预计FY3/27营业利润增长19%，连续第七年实现两位数增长；而NSD和DTS却只能给出2%-3%的利润增幅指引。这种分化不是需求端的问题——三家公司的订单环境都相当强劲——而是供给端的结构性差异在起作用。\n\n对于关注日本IT服务板块的投资者而言，这意味着传统的“订单增速-收入增速-利润增速”线性分析框架已经不够用了。需要建立一个更精细的观察框架，来评估哪些公司真正具备将AI驱动的效率提升转化为可持续利润的能力。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 订单增长强劲但利润指引分化，说明行业已进入“效率竞争”阶段\n\n三家公司最新的订单数据都相当健康。Simplex 4Q订单同比增长19%，连续第三个季度实现两位数增长；NSD系统开发订单4Q同比增长17%，较3Q的3%明显加速；即使是表现最弱的DTS，虽然订单同比下滑4%，但公司表示大型项目的回撤影响已基本消化，公共和电信领域订单正在复苏。\n\n然而，三家的FY\n\n[... middle omitted ...]\n\n争格局的长期影响，并分享我们对具体公司的估值判断。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本IT服务：三个案例的启示\n\n**投研信号已出现**\n\n**核心观点：咨询与金融IT需求走强**\n\n最近研究了三家日本IT服务公司，发现一个有意思的趋势。虽然它们规模不同，但都指向同一个方向——企业咨询和金融IT需求正在回暖。\n\n📌 **信号一：咨询业务超预期**\nSimplex Holdings连续7年实现两位数利润增长，FY3/27经营利润指引同比+19%。咨询业务Q4利润同比+39%，金融、通信、公共领域都很强。公司甚至上调了中期计划目标，从150亿日元提到172亿日元。\n\n📌 **信号二：AI投入开始见效**\nSimplex开始专注AI驱动开发，预计FY3/29开始贡献利润。因为是按合同项目收费，AI提效带来的工时节省，大部分能转化为公司自己的利润。这是典型的“降本增效”逻辑。\n\n📌 **信号三：订单环境分化明显**\n- NSD：来自大型银行的系统开发订单+17%，但利润增长仅+2%，因为要加大AI等前期投入\n- DTS：受大型银行项目结束影响，订单-4%，但公共和通信领域开始复苏\n\n📌 **信号四：竞争格局与风险**\n- 咨询人才竞争激烈，但Simplex靠有竞争力的薪酬成功招人\n- DTS在新领\n\n[... middle omitted ...]\n\naised its order outlook range. Simplex has begun to focus on AI-driven development, and as it is largely engaged in contract-based development, it sees large scope to capture man-hour reductio\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: Exports of Swiss Wristwatches watches by price categories Swiss watch exports by price - Total market (1'000 units)"
  },
  {
    "figure_id": "F002",
    "report_id": "R001",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: Swiss watch exports by material Swiss watch exports by material - Total market"
  },
  {
    "figure_id": "F003",
    "report_id": "R001",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Swiss watch exports by country in absolute numbers Swiss watch exports by country - Key markets only"
  },
  {
    "figure_id": "F004",
    "report_id": "R002",
    "label": "Exhibit 1",
    "context": "Exhibit 1: 10y tail results for all combinations of lookback window, option expiry, and trading delay # Compare LIBOR and SOFR era The LIBOR-SOFR transition provides a convenient division of the sample into two distinct macro env"
  },
  {
    "figure_id": "F005",
    "report_id": "R002",
    "label": "Exhibit 2",
    "context": "Exhibit 3: 10y tail results from 2019 - today"
  },
  {
    "figure_id": "F006",
    "report_id": "R002",
    "label": "Exhibit 2",
    "context": "Exhibit 3: 10y tail results from 2019 - today"
  },
  {
    "figure_id": "F007",
    "report_id": "R002",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Historical return over the LIBOR era"
  },
  {
    "figure_id": "F008",
    "report_id": "R002",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Historical return over the SOFR era"
  },
  {
    "figure_id": "F009",
    "report_id": "R002",
    "label": "Exhibit 6",
    "context": "Exhibit 6: 3m10y skew and 10y rates"
  },
  {
    "figure_id": "F010",
    "report_id": "R002",
    "label": "Exhibit 7",
    "context": "Exhibit 7: 3m10y skew and 3m10y implied vol"
  },
  {
    "figure_id": "F011",
    "report_id": "R002",
    "label": "Exhibit 8",
    "context": "The performance deterioration since 2019 has been most pronounced in the 2y tail, while the 30y tail is the only part of the curve that saw an improvement. One interpretation is that front-end rates have become increasingly driven by macro and policy shocks, r"
  },
  {
    "figure_id": "F012",
    "report_id": "R002",
    "label": "Exhibit 9",
    "context": "Exhibit 9: 2y tail results from 2019 - today"
  },
  {
    "figure_id": "F013",
    "report_id": "R002",
    "label": "Exhibit 10",
    "context": "Exhibit 11: 5y tail results from 2019 - today"
  },
  {
    "figure_id": "F014",
    "report_id": "R002",
    "label": "Exhibit 10",
    "context": "Exhibit 11: 5y tail results from 2019 - today"
  },
  {
    "figure_id": "F015",
    "report_id": "R002",
    "label": "Exhibit 13",
    "context": "Exhibit 13: 30y tail results from 2019 - today"
  },
  {
    "figure_id": "F016",
    "report_id": "R002",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Exposure across the curve based on skew signal"
  },
  {
    "figure_id": "F017",
    "report_id": "R002",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Total return of strategies based on skew signal over the past year"
  },
  {
    "figure_id": "F018",
    "report_id": "R002",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Dealers' gamma exposure profile"
  },
  {
    "figure_id": "F019",
    "report_id": "R002",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Historical peak gamma exposure"
  },
  {
    "figure_id": "F020",
    "report_id": "R002",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Notional of callable bond issuance"
  },
  {
    "figure_id": "F021",
    "report_id": "R002",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Vega supply from callable issuance"
  },
  {
    "figure_id": "F022",
    "report_id": "R003",
    "label": "Figure 2",
    "context": "Figure 2: Industrial product prices continued to rise"
  },
  {
    "figure_id": "F023",
    "report_id": "R003",
    "label": "Figure 3",
    "context": "Figure 3: Government bond issuance accelerated slightly in May"
  },
  {
    "figure_id": "F024",
    "report_id": "R003",
    "label": "Figure 4",
    "context": "Figure 4: Cross-country comparison"
  },
  {
    "figure_id": "F025",
    "report_id": "R003",
    "label": "Figure 5",
    "context": "Figure 5: , China's manufacturing PMI returned to exactly the 50 boom-bust line"
  },
  {
    "figure_id": "F026",
    "report_id": "R003",
    "label": "Figure 6",
    "context": "Figure 6: Services PMI returned to expansion territory"
  },
  {
    "figure_id": "F027",
    "report_id": "R003",
    "label": "Figure 7",
    "context": "Figure 7: Construction, remained below 50 at 48.8"
  },
  {
    "figure_id": "F028",
    "report_id": "R003",
    "label": "Figure 8",
    "context": "Figure 8: Business expectations softened"
  },
  {
    "figure_id": "F029",
    "report_id": "R003",
    "label": "Figure 9",
    "context": "Figure 9: Upstream inventories are falling while finished-goods inventories are rising"
  },
  {
    "figure_id": "F030",
    "report_id": "R003",
    "label": "Figure 10",
    "context": "Figure 10: Input prices continue to rise by much faster than output prices"
  },
  {
    "figure_id": "F031",
    "report_id": "R003",
    "label": "Figure 11",
    "context": "Figure 11: Exports PMI stayed strong despite the recent decline"
  },
  {
    "figure_id": "F032",
    "report_id": "R004",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Real Corporate Revenues Grew a Strong $6.3\\%$ Year-over-Year in 2026Q1"
  },
  {
    "figure_id": "F033",
    "report_id": "R004",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Alternative Measures of Nominal Consumer Spending Growth Remain Solid"
  },
  {
    "figure_id": "F034",
    "report_id": "R004",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Sentiment Around the Consumer Declined but Remained Around Its Historical Average"
  },
  {
    "figure_id": "F035",
    "report_id": "R004",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Sales Growth Between Companies Exposed to Households on Different Ends of the Income Spectrum Had Narrowed Over the Last Couple of Quarters, but the Rise in Gasoline Prices Will Weigh More on Consumption Growth at the Lo"
  },
  {
    "figure_id": "F036",
    "report_id": "R004",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Our Company Price Announcement Tracker Increased to the Highest Level Since 2023 but Remained Well Below its 2022 Peak"
  },
  {
    "figure_id": "F037",
    "report_id": "R004",
    "label": "Exhibit 6",
    "context": "\\* Share of sentences mentioning higher prices less share of sentences mentioning lower prices."
  },
  {
    "figure_id": "F038",
    "report_id": "R004",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Worries Over Labor Costs Have Fallen to the Lowest Levels in a Decade"
  },
  {
    "figure_id": "F039",
    "report_id": "R004",
    "label": "Exhibit 8",
    "context": "Exhibit 8: $66\\%$ of S&P 500 Management Teams Mentioned AI on Q1 Earnings Calls"
  },
  {
    "figure_id": "F040",
    "report_id": "R004",
    "label": "Exhibit 9",
    "context": "Exhibit 9: The Hyperscalers Are Expected to Spend Roughly \\$750bn on Capex This Year, 12% Above Expectations at the Start of the Earnings Season"
  },
  {
    "figure_id": "F041",
    "report_id": "R004",
    "label": "Exhibit 10",
    "context": "Exhibit 10: A Modest Share of Management Teams Mentioned AI When Discussing Hiring Freezes or Layoffs; Surveys of Businesses Suggest a Limited Impact on Net Employment"
  },
  {
    "figure_id": "F042",
    "report_id": "R004",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Over the Last Month, Tech Companies Have Announced AI-Related Layoffs Layoffs.fyi: US Tech and Startup Companies Conducting Layoffs, by Reason Cited (Classified by GS)"
  },
  {
    "figure_id": "F043",
    "report_id": "R004",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Companies Report Cutting Operations, Data Labeling, Software Development, and Customer Support Roles; Online Job Openings for Tech Companies and Startups That Announced AI-Related Layoffs Suggest an Increase in Demand fo"
  },
  {
    "figure_id": "F044",
    "report_id": "R006",
    "label": "Figure 1",
    "context": "Figure 1: Global commodity markets saw net outflows largely driven by precious metals and energy markets USD billion, cumulative flows across tracked commodity markets"
  },
  {
    "figure_id": "F045",
    "report_id": "R006",
    "label": "Figure 2",
    "context": "Figure 2: The estimated value of global commodity market open interest decreased by 4% WoW USD billion, estimated open interest across tracked commodity markets"
  },
  {
    "figure_id": "F046",
    "report_id": "R006",
    "label": "Figure 3",
    "context": "Figure 3: Net length across commodity markets decreased by \\$20 billion, largely driven by crude oil and agri market real USD million, Net investor positioning aggregated across tracked commodity markets"
  },
  {
    "figure_id": "F047",
    "report_id": "R006",
    "label": "Figure 5",
    "context": "Figure 5: The CTA net long positioning in COMEX Gold stabilised over the week USD/oz (average weekly gold price); bubble size represents magnitude of weekly increase (green) or decrease (red) in CTA F&O net length"
  },
  {
    "figure_id": "F048",
    "report_id": "R006",
    "label": "Figure 4",
    "context": "Figure 4: Latest projections indicate decreasing positioning in energy and agri markets 0-10 standardized scale: 0 = lowest since 2018, 10 = highest since 2018 positioning data in real USD terms"
  },
  {
    "figure_id": "F049",
    "report_id": "R006",
    "label": "Figure 6",
    "context": "Figure 6: The estimated value of open interest across energy markets decreased by 6% WoW USD billion, estimated open interest across tracked energy markets"
  },
  {
    "figure_id": "F050",
    "report_id": "R006",
    "label": "Figure 7",
    "context": "Figure 7: The estimated value of open interest across environmental markets increased by 7% WoW USD billion, estimated open interest across tracked environmental markets"
  },
  {
    "figure_id": "F051",
    "report_id": "R006",
    "label": "Figure 9",
    "context": "Figure 9: The estimated value of open interest across base metals markets increased by 1% WoW USD billion, estimated open interest across tracked base metals markets"
  },
  {
    "figure_id": "F052",
    "report_id": "R006",
    "label": "Figure 11",
    "context": "Figure 11: The estimated value of open interest in crude oil decreased by 7% WoW, remaining near multi-year highs USD billion, estimated open interest across tracked crude oil markets"
  },
  {
    "figure_id": "F053",
    "report_id": "R006",
    "label": "Figure 8",
    "context": "Figure 8: The estimated value of open interest across precious metals decreased by 8% WoW USD billion, estimated open interest across tracked precious metals markets"
  },
  {
    "figure_id": "F054",
    "report_id": "R006",
    "label": "Figure 10",
    "context": "Figure 10: The estimated value of open interest in agri markets stabilised over the week USD billion, estimated open interest across tracked agricultural markets"
  },
  {
    "figure_id": "F055",
    "report_id": "R006",
    "label": "Figure 12",
    "context": "Figure 12: Petroleum products estimated open interest value decreased by 8% WoW USD billion, estimated open interest across tracked petroleum products markets"
  },
  {
    "figure_id": "F056",
    "report_id": "R006",
    "label": "Figure 13",
    "context": "Figure 13: The estimated value of open interest in natural gas markets decreased by 3% WoW USD billion, estimated open interest across tracked natural gas metals markets"
  },
  {
    "figure_id": "F057",
    "report_id": "R006",
    "label": "Figure 15",
    "context": "Figure 15: The estimated value of open interest in soft markets increased by 1% WoW USD billion, estimated open interest across tracked softs agricultural markets"
  },
  {
    "figure_id": "F058",
    "report_id": "R006",
    "label": "Figure 14",
    "context": "Figure 14: The estimated value of open interest in grains & oilseeds markets increased by 1% WoW USD billion, estimated open interest across tracked grains and oilseeds markets"
  },
  {
    "figure_id": "F059",
    "report_id": "R006",
    "label": "Figure 16",
    "context": "Figure 16: The estimated open interest value across livestock markets decreased by 2% WoW USD billion, estimated open interest across tracked livestock markets"
  },
  {
    "figure_id": "F060",
    "report_id": "R006",
    "label": "Figure 17",
    "context": "Figure 17: Price momentum (z-scores) and trading signals across major commodities \\*see methodology in Figure 18"
  },
  {
    "figure_id": "F061",
    "report_id": "R006",
    "label": "Figure 19",
    "context": "Figure 19: Energy sectoral standardised level chart 0-10 standardized scale: 0 = lowest since 2018, 10 = highest since 2018 positioning data in real USD terms"
  },
  {
    "figure_id": "F062",
    "report_id": "R006",
    "label": "Figure 21",
    "context": "Figure 21: NYMEX WTI Crude Oil position and price LHS: n of contracts; RHS: \\$/bbl"
  },
  {
    "figure_id": "F063",
    "report_id": "R006",
    "label": "Figure 23",
    "context": "Figure 23: ICE Dubai Crude Oil position and price LHS: n of contracts; RHS: \\$/bbl"
  },
  {
    "figure_id": "F064",
    "report_id": "R006",
    "label": "Figure 20",
    "context": "Figure 20: Energy underlying commodities standardised level chart 0-10 standardized scale: 0 = lowest since 2018, 10 = highest since 2018 positioning data in real USD terms"
  },
  {
    "figure_id": "F065",
    "report_id": "R006",
    "label": "Figure 22",
    "context": "Figure 22: ICE Brent Crude Oil position and price LHS: n of contracts; RHS: \\$/bbl"
  },
  {
    "figure_id": "F066",
    "report_id": "R006",
    "label": "Figure 24",
    "context": "Figure 24: ICE TTF Natural Gas position and price LHS: TWh; RHS: EUR/MWh"
  },
  {
    "figure_id": "F067",
    "report_id": "R006",
    "label": "Figure 25",
    "context": "Figure 25: Weekly change in total OI due to price/flows"
  },
  {
    "figure_id": "F068",
    "report_id": "R006",
    "label": "Figure 27",
    "context": "Figure 27: Weekly change in total OI from changes in contracts (flows)"
  },
  {
    "figure_id": "F069",
    "report_id": "R006",
    "label": "Figure 26",
    "context": "Figure 26: Weekly change in total OI from changes in prices"
  },
  {
    "figure_id": "F070",
    "report_id": "R006",
    "label": "Figure 28",
    "context": "Figure 28: Environmental markets standardised level chart 0-10 standardized scale: 0 = lowest since 2018, 10 = highest since 2018 positioning data in real USD terms"
  },
  {
    "figure_id": "F071",
    "report_id": "R006",
    "label": "Figure 30",
    "context": "Figure 30: Weekly change in total OI due to price/flows USD million"
  },
  {
    "figure_id": "F072",
    "report_id": "R006",
    "label": "Figure 29",
    "context": "Figure 29: ICE EUA position and price LHS: n of contracts; RHS: \\$/MT"
  },
  {
    "figure_id": "F073",
    "report_id": "R006",
    "label": "Figure 31",
    "context": "Figure 31: Weekly change in total OI from changes in prices USD million"
  },
  {
    "figure_id": "F074",
    "report_id": "R006",
    "label": "Figure 32",
    "context": "Figure 32: Weekly change in total OI from changes in contracts (flows) USD million"
  },
  {
    "figure_id": "F075",
    "report_id": "R006",
    "label": "Figure 33",
    "context": "Figure 33: Metals sectoral standardised level chart 0-10 standardized scale: 0 = lowest since 2018, 10 = highest since 2018 positioning data in real USD terms"
  },
  {
    "figure_id": "F076",
    "report_id": "R006",
    "label": "Figure 35",
    "context": "Figure 35: Precious Metals standardised level chart 0-10 standardized scale: 0 = lowest since 2018, 10 = highest since 2018 positioning data in real USD terms"
  },
  {
    "figure_id": "F077",
    "report_id": "R006",
    "label": "Figure 37",
    "context": "Figure 37: COMEX Copper position and price LHS: n of contracts; RHS: \\$/lb"
  },
  {
    "figure_id": "F078",
    "report_id": "R006",
    "label": "Figure 34",
    "context": "Figure 34: Base Metals standardised level chart 0-10 standardized scale: 0 = lowest since 2018, 10 = highest since 2018 positioning data in real USD terms"
  },
  {
    "figure_id": "F079",
    "report_id": "R006",
    "label": "Figure 36",
    "context": "Figure 36: COMEX Gold position and price LHS: n of contracts; RHS: \\$/t oz"
  },
  {
    "figure_id": "F080",
    "report_id": "R006",
    "label": "Figure 38",
    "context": "Figure 38: LME Copper position and price LHS: n of contracts; RHS: \\$/MT"
  },
  {
    "figure_id": "F081",
    "report_id": "R006",
    "label": "Figure 39",
    "context": "Figure 39: Weekly change in total OI due to price/flows"
  },
  {
    "figure_id": "F082",
    "report_id": "R006",
    "label": "Figure 41",
    "context": "Figure 41: Weekly change in total OI from changes in contracts (flows) USD million"
  },
  {
    "figure_id": "F083",
    "report_id": "R006",
    "label": "Figure 43",
    "context": "Figure 43: Weekly change in total OI from changes in contracts (flows)-precious metals"
  },
  {
    "figure_id": "F084",
    "report_id": "R006",
    "label": "Figure 40",
    "context": "Figure 40: Weekly change in total OI from changes in prices"
  },
  {
    "figure_id": "F085",
    "report_id": "R006",
    "label": "Figure 42",
    "context": "Figure 42: Weekly change in total OI from changes in contracts (flows)-industrial and bulk metals"
  },
  {
    "figure_id": "F086",
    "report_id": "R006",
    "label": "Figure 44",
    "context": "Figure 44: Agriculture commodities sectoral standardised level chart 0-10 standardized scale: 0 = lowest since 2018, 10 = highest since 2018 positioning data in real USD terms"
  },
  {
    "figure_id": "F087",
    "report_id": "R006",
    "label": "Figure 46",
    "context": "Figure 46: Softs standardised level chart 0-10 standardized scale: 0 = lowest since 2018, 10 = highest since 2018 positioning data in real USD terms"
  },
  {
    "figure_id": "F088",
    "report_id": "R006",
    "label": "Figure 48",
    "context": "Figure 48: Weekly change in total OI due to price/flows USD million"
  },
  {
    "figure_id": "F089",
    "report_id": "R006",
    "label": "Figure 45",
    "context": "Figure 45: Grains & oilseeds standardised level chart 0-10 standardized scale: 0 = lowest since 2018, 10 = highest since 2018 positioning data in real USD terms"
  },
  {
    "figure_id": "F090",
    "report_id": "R006",
    "label": "Figure 47",
    "context": "Figure 47: Livestock standardised level chart 0-10 standardized scale: 0 = lowest since 2018, 10 = highest since 2018 positioning data in real USD terms"
  },
  {
    "figure_id": "F091",
    "report_id": "R006",
    "label": "Figure 49",
    "context": "Figure 49: Weekly change in total OI from changes in prices USD million"
  },
  {
    "figure_id": "F092",
    "report_id": "R006",
    "label": "Figure 50",
    "context": "Figure 50: Weekly change in total OI from changes in contracts (flows) USD million"
  },
  {
    "figure_id": "F093",
    "report_id": "R006",
    "label": "Figure 51",
    "context": "Figure 51: Weekly change in total OI from changes in contracts (flows) - grains and oilseeds"
  },
  {
    "figure_id": "F094",
    "report_id": "R006",
    "label": "Figure 52",
    "context": "Figure 52: Weekly change in total OI from changes in contracts (flows)-softs and livestock"
  },
  {
    "figure_id": "F095",
    "report_id": "R006",
    "label": "Figure 53",
    "context": "Figure 53: Weekly change in open interest by trading group US\\$ million (futures and options)"
  },
  {
    "figure_id": "F096",
    "report_id": "R006",
    "label": "Figure 55",
    "context": "Figure 55: Weekly change in OI from changes in contracts & price US\\$ million (futures and options)"
  },
  {
    "figure_id": "F097",
    "report_id": "R006",
    "label": "Figure 57",
    "context": "Figure 57: Seasonal Managed Money net length Lots (1,000)"
  },
  {
    "figure_id": "F098",
    "report_id": "R006",
    "label": "Figure 54",
    "context": "Figure 54: Gross PMPU position and price LHS: lots (1,000), RHS: USD/bbl"
  },
  {
    "figure_id": "F099",
    "report_id": "R006",
    "label": "Figure 56",
    "context": "Figure 56: Open interest share by trader type %"
  },
  {
    "figure_id": "F100",
    "report_id": "R006",
    "label": "Figure 58",
    "context": "Figure 58: Price momentum LHS: Z-score, RHS: USD/bbl"
  },
  {
    "figure_id": "F101",
    "report_id": "R006",
    "label": "Figure 59",
    "context": "Figure 59: Weekly change in open interest by trading group US\\$ million (futures and options)"
  },
  {
    "figure_id": "F102",
    "report_id": "R006",
    "label": "Figure 61",
    "context": "Figure 61: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 63: Seasonal Managed Money net length Lots (1,000)"
  },
  {
    "figure_id": "F103",
    "report_id": "R006",
    "label": "Figure 61",
    "context": "Figure 61: Weekly change in OI from changes in contracts & price US\\$ million (futures and options) Figure 63: Seasonal Managed Money net length Lots (1,000)"
  },
  {
    "figure_id": "F104",
    "report_id": "R006",
    "label": "Figure 60",
    "context": "Figure 60: Gross PMPU position and price LHS: lots (1,000), RHS: USD/bbl"
  },
  {
    "figure_id": "F105",
    "report_id": "R006",
    "label": "Figure 62",
    "context": "Figure 62: Open interest share by trader type %"
  },
  {
    "figure_id": "F106",
    "report_id": "R006",
    "label": "Figure 64",
    "context": "Figure 64: Price momentum LHS: Z-score, RHS: USD/bbl"
  },
  {
    "figure_id": "F107",
    "report_id": "R006",
    "label": "Figure 65",
    "context": "Figure 65: Weekly change in open interest by trading group US\\$ million (futures and options)"
  },
  {
    "figure_id": "F108",
    "report_id": "R006",
    "label": "Figure 67",
    "context": "Figure 67: Weekly change in OI from changes in contracts & price US\\$ million (futures and options)"
  },
  {
    "figure_id": "F109",
    "report_id": "R006",
    "label": "Figure 69",
    "context": "Figure 69: Seasonal Managed Money net length Lots (1,000)"
  },
  {
    "figure_id": "F110",
    "report_id": "R006",
    "label": "Figure 66",
    "context": "Figure 66: Gross PMPU position and price LHS: lots (1,000), RHS: USc/gal"
  },
  {
    "figure_id": "F111",
    "report_id": "R006",
    "label": "Figure 68",
    "context": "Figure 68: Open interest share by trader type %"
  },
  {
    "figure_id": "F112",
    "report_id": "R006",
    "label": "Figure 70",
    "context": "Figure 70: Price momentum LHS: Z-score, RHS: USc/gal"
  },
  {
    "figure_id": "F113",
    "report_id": "R006",
    "label": "Figure 71",
    "context": "Figure 71: Weekly change in open interest by trading group"
  },
  {
    "figure_id": "F114",
    "report_id": "R006",
    "label": "Figure 73",
    "context": "Figure 73: Weekly change in OI from changes in contracts & price"
  },
  {
    "figure_id": "F115",
    "report_id": "R006",
    "label": "Figure 75",
    "context": "Figure 75: Seasonal Managed Money net length"
  },
  {
    "figure_id": "F116",
    "report_id": "R006",
    "label": "Figure 72",
    "context": "Figure 72: Gross PMPU position and price LHS: lots (1,000), RHS: USD/T"
  },
  {
    "figure_id": "F117",
    "report_id": "R006",
    "label": "Figure 74",
    "context": "Figure 74: Open interest share by trader type"
  },
  {
    "figure_id": "F118",
    "report_id": "R006",
    "label": "Figure 76",
    "context": "Figure 76: Price momentum"
  },
  {
    "figure_id": "F119",
    "report_id": "R006",
    "label": "Figure 77",
    "context": "Figure 77: Weekly change in open interest by trading group US\\$ million (futures and options)"
  },
  {
    "figure_id": "F120",
    "report_id": "R006",
    "label": "Figure 79",
    "context": "Figure 79: Weekly change in OI from changes in contracts & price US\\$ million (futures and options)"
  },
  {
    "figure_id": "F121",
    "report_id": "R006",
    "label": "Figure 81",
    "context": "Figure 81: Seasonal Managed Money net length Lots (1,000)"
  },
  {
    "figure_id": "F122",
    "report_id": "R006",
    "label": "Figure 78",
    "context": "Figure 78: Gross PMPU position and price LHS: lots (1,000), RHS: USD/mmbtu"
  },
  {
    "figure_id": "F123",
    "report_id": "R006",
    "label": "Figure 80",
    "context": "Figure 80: Open interest share by trader type %"
  },
  {
    "figure_id": "F124",
    "report_id": "R006",
    "label": "Figure 82",
    "context": "Figure 82: Price momentum LHS: Z-score, RHS: USD/mmbtu"
  },
  {
    "figure_id": "F125",
    "report_id": "R006",
    "label": "Figure 83",
    "context": "Figure 83: Weekly change in open interest by trading group US\\$ billion (futures and options, contracts in MWh)"
  },
  {
    "figure_id": "F126",
    "report_id": "R006",
    "label": "Figure 85",
    "context": "Figure 85: Weekly change in OI from changes in contracts & price US\\$ billion (futures and options, contracts in MWh)"
  },
  {
    "figure_id": "F127",
    "report_id": "R006",
    "label": "Figure 87",
    "context": "Figure 87: Seasonal Investment funds net length MWh (million)"
  },
  {
    "figure_id": "F128",
    "report_id": "R006",
    "label": "Figure 84",
    "context": "Figure 84: Gross commercial position and price LHS: MWh (million), RHS: EUR/MWh"
  },
  {
    "figure_id": "F129",
    "report_id": "R006",
    "label": "Figure 86",
    "context": "Figure 86: Open interest share by trader type"
  },
  {
    "figure_id": "F130",
    "report_id": "R006",
    "label": "Figure 88",
    "context": "Figure 88: Price momentum LHS: Z-score, RHS: EUR/Mwh"
  },
  {
    "figure_id": "F131",
    "report_id": "R006",
    "label": "Figure 89",
    "context": "Figure 89: Weekly change in open interest by trading group US\\$ million (futures and options)"
  },
  {
    "figure_id": "F132",
    "report_id": "R006",
    "label": "Figure 91",
    "context": "Figure 91: Weekly change in OI from changes in contracts & price US\\$ million (futures and options)"
  },
  {
    "figure_id": "F133",
    "report_id": "R006",
    "label": "Figure 93",
    "context": "Figure 93: Seasonal Investment funds net length Lots (1,000)"
  },
  {
    "figure_id": "F134",
    "report_id": "R006",
    "label": "Figure 90",
    "context": "Figure 90: Gross commercial position and price LHS: lots (1,000), RHS: EUR/MtCO2e"
  },
  {
    "figure_id": "F135",
    "report_id": "R006",
    "label": "Figure 92",
    "context": "Figure 92: Open interest share by trader type %"
  },
  {
    "figure_id": "F136",
    "report_id": "R006",
    "label": "Figure 94",
    "context": "Figure 94: Price momentum LHS: Z-score, RHS: EUR/MtCO2e."
  },
  {
    "figure_id": "F137",
    "report_id": "R006",
    "label": "Figure 95",
    "context": "Figure 95: Weekly change in open interest by trading group US\\$ million (futures and options)"
  },
  {
    "figure_id": "F138",
    "report_id": "R006",
    "label": "Figure 97",
    "context": "Figure 97: Weekly change in OI from changes in contracts & price US\\$ million (futures and options)"
  },
  {
    "figure_id": "F139",
    "report_id": "R006",
    "label": "Figure 99",
    "context": "Figure 99: Seasonal Managed Money net length Lots (1,000)"
  },
  {
    "figure_id": "F140",
    "report_id": "R006",
    "label": "Figure 96",
    "context": "Figure 96: Gross PMPU position and price LHS: lots (1,000), RHS: USD/t oz."
  },
  {
    "figure_id": "F141",
    "report_id": "R006",
    "label": "Figure 98",
    "context": "Figure 98: Open interest share by trader type %"
  },
  {
    "figure_id": "F142",
    "report_id": "R006",
    "label": "Figure 100",
    "context": "Figure 100: Price momentum LHS: Z-score, RHS: USD/t oz."
  },
  {
    "figure_id": "F143",
    "report_id": "R006",
    "label": "Figure 101",
    "context": "Figure 101: Weekly change in open interest by trading group US\\$ million (futures and options)"
  },
  {
    "figure_id": "F144",
    "report_id": "R006",
    "label": "Figure 103",
    "context": "Figure 103: Weekly change in OI from changes in contracts & price US\\$ million (futures and options)"
  },
  {
    "figure_id": "F145",
    "report_id": "R006",
    "label": "Figure 105",
    "context": "Figure 105: Seasonal Managed Money net length Lots (1,000)"
  },
  {
    "figure_id": "F146",
    "report_id": "R006",
    "label": "Figure 102",
    "context": "Figure 102: Gross PMPU position and price %"
  },
  {
    "figure_id": "F147",
    "report_id": "R006",
    "label": "Figure 104",
    "context": "Figure 104: Open interest share by trader type %"
  },
  {
    "figure_id": "F148",
    "report_id": "R006",
    "label": "Figure 106",
    "context": "Figure 106: Price momentum LHS: Z-score, RHS: USD/t oz."
  },
  {
    "figure_id": "F149",
    "report_id": "R006",
    "label": "Figure 107",
    "context": "Figure 107: Weekly change in open interest by trading group US\\$ million (futures and options)"
  },
  {
    "figure_id": "F150",
    "report_id": "R006",
    "label": "Figure 109",
    "context": "Figure 109: Weekly change in OI from changes in contracts & price US\\$ million (futures and options)"
  },
  {
    "figure_id": "F151",
    "report_id": "R006",
    "label": "Figure 111",
    "context": "Figure 111: Seasonal Managed Money net length Lots (1,000)"
  },
  {
    "figure_id": "F152",
    "report_id": "R006",
    "label": "Figure 108",
    "context": "Figure 108: Gross PMPU position and price LHS: lots (1,000), RHS: USc/lb"
  },
  {
    "figure_id": "F153",
    "report_id": "R006",
    "label": "Figure 110",
    "context": "Figure 110: Open interest share by trader type %"
  },
  {
    "figure_id": "F154",
    "report_id": "R006",
    "label": "Figure 112",
    "context": "Figure 112: Price momentum LHS: Z-score, RHS: USc/lb"
  },
  {
    "figure_id": "F155",
    "report_id": "R006",
    "label": "Figure 113",
    "context": "Figure 113: Weekly change in open interest by trading group US\\$ million (futures and options)"
  },
  {
    "figure_id": "F156",
    "report_id": "R006",
    "label": "Figure 115",
    "context": "Figure 115: Weekly change in OI from changes in contracts & price US\\$ million (futures and options)"
  },
  {
    "figure_id": "F157",
    "report_id": "R006",
    "label": "Figure 117",
    "context": "Figure 117: Seasonal Managed Money net length Lots (1,000)"
  },
  {
    "figure_id": "F158",
    "report_id": "R006",
    "label": "Figure 114",
    "context": "Figure 114: Gross PMPU position and price LHS: lots (1,000), RHS: USD/t oz."
  },
  {
    "figure_id": "F159",
    "report_id": "R006",
    "label": "Figure 116",
    "context": "Figure 116: Open interest share by trader type %"
  },
  {
    "figure_id": "F160",
    "report_id": "R006",
    "label": "Figure 118",
    "context": "Figure 118: Price momentum LHS: Z-score, RHS: USD/t oz."
  },
  {
    "figure_id": "F161",
    "report_id": "R006",
    "label": "Figure 119",
    "context": "Figure 119: Weekly change in open interest by trading group US\\$ million (futures and options)"
  },
  {
    "figure_id": "F162",
    "report_id": "R006",
    "label": "Figure 121",
    "context": "Figure 121: Weekly change in OI from changes in contracts & price US\\$ million (futures and options)"
  },
  {
    "figure_id": "F163",
    "report_id": "R006",
    "label": "Figure 123",
    "context": "Figure 123: Seasonal Managed Money net length Lots (1,000)"
  },
  {
    "figure_id": "F164",
    "report_id": "R006",
    "label": "Figure 120",
    "context": "Figure 120: Gross PMPU position and price LHS: lots (1,000), RHS: USc/bu"
  },
  {
    "figure_id": "F165",
    "report_id": "R006",
    "label": "Figure 122",
    "context": "Figure 122: Open interest share by trader type %"
  },
  {
    "figure_id": "F166",
    "report_id": "R006",
    "label": "Figure 124",
    "context": "Figure 124: Price momentum LHS: Z-score, RHS: USc/bu"
  },
  {
    "figure_id": "F167",
    "report_id": "R006",
    "label": "Figure 125",
    "context": "Figure 125: Weekly change in open interest by trading group US\\$ million (futures and options)"
  },
  {
    "figure_id": "F168",
    "report_id": "R006",
    "label": "Figure 127",
    "context": "Figure 127: Weekly change in OI from changes in contracts & price US\\$ million (futures and options)"
  },
  {
    "figure_id": "F169",
    "report_id": "R006",
    "label": "Figure 129",
    "context": "Figure 129: Seasonal Managed Money net length Lots (1,000)"
  },
  {
    "figure_id": "F170",
    "report_id": "R006",
    "label": "Figure 126",
    "context": "Figure 126: Gross PMPU position and price LHS: lots (1,000), RHS: USc/bu"
  },
  {
    "figure_id": "F171",
    "report_id": "R006",
    "label": "Figure 128",
    "context": "Figure 128: Open interest share by trader type %"
  },
  {
    "figure_id": "F172",
    "report_id": "R006",
    "label": "Figure 130",
    "context": "Figure 130: Price momentum LHS: Z-score, RHS: USc/bu"
  },
  {
    "figure_id": "F173",
    "report_id": "R006",
    "label": "Figure 131",
    "context": "Figure 131: Weekly change in open interest by trading group US\\$ million (futures and options)"
  },
  {
    "figure_id": "F174",
    "report_id": "R006",
    "label": "Figure 133",
    "context": "Figure 133: Weekly change in OI from changes in contracts & price US\\$ million (futures and options)"
  },
  {
    "figure_id": "F175",
    "report_id": "R006",
    "label": "Figure 135",
    "context": "Figure 135: Seasonal Managed Money net length Lots (1,000)"
  },
  {
    "figure_id": "F176",
    "report_id": "R006",
    "label": "Figure 132",
    "context": "Figure 132: Gross PMPU position and price LHS: lots (1,000), RHS: USc/bu"
  },
  {
    "figure_id": "F177",
    "report_id": "R006",
    "label": "Figure 134",
    "context": "Figure 134: Open interest share by trader type %"
  },
  {
    "figure_id": "F178",
    "report_id": "R006",
    "label": "Figure 136",
    "context": "Figure 136: Price momentum LHS: Z-score, RHS: USc/bu"
  },
  {
    "figure_id": "F179",
    "report_id": "R006",
    "label": "Figure 137",
    "context": "Figure 137: Weekly change in open interest by trading group US\\$ million (futures and options)"
  },
  {
    "figure_id": "F180",
    "report_id": "R006",
    "label": "Figure 139",
    "context": "Figure 139: Weekly change in OI from changes in contracts & price US\\$ million (futures and options)"
  },
  {
    "figure_id": "F181",
    "report_id": "R006",
    "label": "Figure 141",
    "context": "Figure 141: Seasonal Managed Money net length Lots (1,000)"
  },
  {
    "figure_id": "F182",
    "report_id": "R006",
    "label": "Figure 138",
    "context": "Figure 138: Gross PMPU position and price LHS: lots (1,000), RHS: USc/lb"
  },
  {
    "figure_id": "F183",
    "report_id": "R006",
    "label": "Figure 140",
    "context": "Figure 140: Open interest share by trader type %"
  },
  {
    "figure_id": "F184",
    "report_id": "R006",
    "label": "Figure 142",
    "context": "Figure 142: Price momentum LHS: Z-score, RHS: USc/lb"
  },
  {
    "figure_id": "F185",
    "report_id": "R006",
    "label": "Figure 143",
    "context": "Figure 143: Weekly change in open interest by trading group US\\$ million (futures and options)"
  },
  {
    "figure_id": "F186",
    "report_id": "R006",
    "label": "Figure 145",
    "context": "Figure 145: Weekly change in OI from changes in contracts & price US\\$ million (futures and options)"
  },
  {
    "figure_id": "F187",
    "report_id": "R006",
    "label": "Figure 147",
    "context": "Figure 147: Seasonal Managed Money net length Lots (1,000)"
  },
  {
    "figure_id": "F188",
    "report_id": "R006",
    "label": "Figure 144",
    "context": "Figure 144: Gross PMPU position and price LHS: lots (1,000), RHS: USc/lb"
  },
  {
    "figure_id": "F189",
    "report_id": "R006",
    "label": "Figure 146",
    "context": "Figure 146: Open interest share by trader type %"
  },
  {
    "figure_id": "F190",
    "report_id": "R006",
    "label": "Figure 148",
    "context": "Figure 148: Price momentum LHS: Z-score, RHS: USc/lb"
  },
  {
    "figure_id": "F191",
    "report_id": "R006",
    "label": "Figure 149",
    "context": "Figure 149: Weekly change in open interest by trading group"
  },
  {
    "figure_id": "F192",
    "report_id": "R006",
    "label": "Figure 151",
    "context": "Figure 151: Weekly change in OI from changes in contracts & price"
  },
  {
    "figure_id": "F193",
    "report_id": "R006",
    "label": "Figure 153",
    "context": "Figure 153: Seasonal Managed Money net"
  },
  {
    "figure_id": "F194",
    "report_id": "R006",
    "label": "Figure 150",
    "context": "Figure 150: Gross PMPU position and price LHS: lots (1,000), RHS: USc/lb"
  },
  {
    "figure_id": "F195",
    "report_id": "R006",
    "label": "Figure 152",
    "context": "Figure 152: Open interest share by trader type"
  },
  {
    "figure_id": "F196",
    "report_id": "R006",
    "label": "Figure 154",
    "context": "Figure 154: Price momentum"
  },
  {
    "figure_id": "F197",
    "report_id": "R006",
    "label": "Figure 155",
    "context": "Figure 155: Weekly change in open interest by trading group US\\$ million (futures and options)"
  },
  {
    "figure_id": "F198",
    "report_id": "R006",
    "label": "Figure 157",
    "context": "Figure 157: Weekly change in OI from changes in contracts & price US\\$ million (futures and options)"
  },
  {
    "figure_id": "F199",
    "report_id": "R006",
    "label": "Figure 159",
    "context": "Figure 159: Seasonal Managed Money net length Lots (1,000)"
  },
  {
    "figure_id": "F200",
    "report_id": "R006",
    "label": "Figure 156",
    "context": "Figure 156: Gross PMPU position and price LHS: lots (1,000), RHS: USd/MT"
  },
  {
    "figure_id": "F201",
    "report_id": "R006",
    "label": "Figure 158",
    "context": "Figure 158: Open interest share by trader type %"
  },
  {
    "figure_id": "F202",
    "report_id": "R006",
    "label": "Figure 160",
    "context": "Figure 160: Price momentum LHS: Z-score, RHS: USd/MT"
  },
  {
    "figure_id": "F203",
    "report_id": "R006",
    "label": "Figure 161",
    "context": "Figure 161: Weekly change in open interest by trading group US\\$ million (futures and options)"
  },
  {
    "figure_id": "F204",
    "report_id": "R006",
    "label": "Figure 163",
    "context": "Figure 163: Weekly change in OI from changes in contracts & price US\\$ million (futures and options)"
  },
  {
    "figure_id": "F205",
    "report_id": "R006",
    "label": "Figure 165",
    "context": "Figure 165: Seasonal Managed Money net length Lots (1,000)"
  },
  {
    "figure_id": "F206",
    "report_id": "R006",
    "label": "Figure 162",
    "context": "Figure 162: Gross PMPU position and price LHS: lots (1,000), RHS: USc/lb"
  },
  {
    "figure_id": "F207",
    "report_id": "R006",
    "label": "Figure 164",
    "context": "Figure 164: Open interest share by trader type %"
  },
  {
    "figure_id": "F208",
    "report_id": "R006",
    "label": "Figure 166",
    "context": "Figure 166: Weekly change in open interest by trading group US\\$ million (futures and options)"
  },
  {
    "figure_id": "F209",
    "report_id": "R006",
    "label": "Figure 168",
    "context": "Figure 168: Weekly change in OI from changes in contracts & price US\\$ million (futures and options)"
  },
  {
    "figure_id": "F210",
    "report_id": "R006",
    "label": "Figure 170",
    "context": "Figure 170: Seasonal Managed Money net length Lots (1,000)"
  },
  {
    "figure_id": "F211",
    "report_id": "R006",
    "label": "Figure 167",
    "context": "Figure 167: Gross PMPU position and price LHS: lots (1,000), RHS: USc/lb"
  },
  {
    "figure_id": "F212",
    "report_id": "R006",
    "label": "Figure 169",
    "context": "Figure 169: Open interest share by trader type %"
  },
  {
    "figure_id": "F213",
    "report_id": "R008",
    "label": "Exhibit 1",
    "context": "EXHIBIT 2: April single-month billings data was -38% MoM and +25% YoY in JPY."
  },
  {
    "figure_id": "F214",
    "report_id": "R008",
    "label": "Exhibit 3",
    "context": "EXHIBIT 2: April single-month billings data was -38% MoM and +25% YoY in JPY. SEAJ Monthly Billings (Single Month)"
  },
  {
    "figure_id": "F215",
    "report_id": "R008",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Monthly billings for Japanese WFE was +12% YoY / -50% MoM."
  },
  {
    "figure_id": "F216",
    "report_id": "R008",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: Monthly billings for Japanese assembly SPE was +73% YoY / -39% MoM."
  },
  {
    "figure_id": "F217",
    "report_id": "R008",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: Monthly billings for Japanese testers was +26% YoY."
  },
  {
    "figure_id": "F218",
    "report_id": "R008",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: Monthly billings for Japanese testers was -14% MoM."
  },
  {
    "figure_id": "F219",
    "report_id": "R008",
    "label": "Exhibit 7",
    "context": "EXHIBIT 7: Our regression yields a decent correlation and should have good prediction power. TEL Quarterly SPE Sales vs. SEAJ 2M Billings of 1QCY23-4QCY25"
  },
  {
    "figure_id": "F220",
    "report_id": "R008",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: Regression suggests TEL JunQ revenue of -18% QoQ, below consensus. TEL 1QFY26E (2QCY26E) Revenue"
  },
  {
    "figure_id": "F221",
    "report_id": "R008",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: Our regression yields a decent correlation and should have good prediction power. Advantest Quarterly SPE Sales vs. SEAJ 1M Billings of 1QCY23-1QCY26"
  },
  {
    "figure_id": "F222",
    "report_id": "R008",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: Our regression predicts Advantest JunQ revenue could beat consensus. EXHIBIT 12: Regression suggests Advantest JunQ revenue at +13% QoQ, above consensus. Advantest 1QFY26E (2QCY26E) Revenue"
  },
  {
    "figure_id": "F223",
    "report_id": "R011",
    "label": "Exhibit 11",
    "context": "- CPI impact of higher memory costs (Exhibit 11). Higher memory costs carry a measurable CPI pass-through: PCs and smartphones add 0.08pp to headline CPI, with total consumer electronics impact reaching 0.10pp. # Tech Diffusion # A MS Key Theme of 2026 # A mul"
  },
  {
    "figure_id": "F224",
    "report_id": "R011",
    "label": "Exhibit 1",
    "context": "Exhibit 1: DRAM prices YoY"
  },
  {
    "figure_id": "F225",
    "report_id": "R011",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Long-term DRAM price/Gb"
  },
  {
    "figure_id": "F226",
    "report_id": "R011",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Memory supply relief depends on install, qualification, yield ramp and product allocation – a \\~2 year process From Tool Capacity to Qualified Memory Output ASML capacity is expanding; memory relief depends on install, q"
  },
  {
    "figure_id": "F227",
    "report_id": "R011",
    "label": "Exhibit 4",
    "context": "Exhibit 4: We expect hyperscaler capex to surpass US\\$1tr in 2027 and an aggregate \\~US\\$2tr invested since 2024"
  },
  {
    "figure_id": "F228",
    "report_id": "R011",
    "label": "Exhibit 5",
    "context": "Exhibit 5: The 2026 consensus cloud capex forecast increased to +75% Y/Y post results from 64% previously Top 4 Cloud Providers: Cloud Capex Y/Y Growth"
  },
  {
    "figure_id": "F229",
    "report_id": "R011",
    "label": "Exhibit 7",
    "context": "Exhibit 7: AI prioritization turns 2027 supply growth into a consumer memory shortfall PC: AI priority creates residual DRAM shortfall"
  },
  {
    "figure_id": "F230",
    "report_id": "R011",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Our quant analysis implies low-end smartphones and PCs are the most demand elastic, while servers, storage and high-end smartphones are least at risk of demand destruction from higher prices"
  },
  {
    "figure_id": "F231",
    "report_id": "R011",
    "label": "Exhibit 9",
    "context": "Exhibit 9: The Chipflation impact by industry (illustrative) Net margin impact score by industry (highest risk at bottom)"
  },
  {
    "figure_id": "F232",
    "report_id": "R011",
    "label": "Exhibit 10",
    "context": "Exhibit 10: The effect of rising costs is visible in exposed PPI, with some sub-components rising to all time highs"
  },
  {
    "figure_id": "F233",
    "report_id": "R011",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Mainland China accounts for 30% share of 2023–28E net DRAM wafer additions, behind South Korea"
  },
  {
    "figure_id": "F234",
    "report_id": "R011",
    "label": "Exhibit 13",
    "context": "Exhibit 13: China NAND acceleration scenario – YMTC and Koran suppliers' China fabs could add up to 17%-33% of 2028 global NAND supply"
  },
  {
    "figure_id": "F235",
    "report_id": "R011",
    "label": "Exhibit 14",
    "context": "Exhibit 14: How to play the theme? Exhibit 15: Risk/return positioning for key memory and SPE stocks"
  },
  {
    "figure_id": "F236",
    "report_id": "R011",
    "label": "Exhibit 16",
    "context": "Exhibit 16: AI servers are becoming memory systems"
  },
  {
    "figure_id": "F237",
    "report_id": "R011",
    "label": "Exhibit 17",
    "context": "Exhibit 17: From tool capacity to qualified memory output – lead times are multiple quarters From Tool Capacity to Qualified Memory Output ASML capacity is expanding; memory relief depends on install, qualification, yield ramp and p"
  },
  {
    "figure_id": "F238",
    "report_id": "R011",
    "label": "Exhibit 18",
    "context": "Exhibit 18: ASML EUV shipments FY25-FY27e EUV Shipments (FY25-FY27e)"
  },
  {
    "figure_id": "F239",
    "report_id": "R011",
    "label": "Exhibit 19",
    "context": "Exhibit 19: ASML order book and backlog"
  },
  {
    "figure_id": "F240",
    "report_id": "R011",
    "label": "Exhibit 20",
    "context": "Exhibit 20: DRAM – AI server demand becomes dominant ..."
  },
  {
    "figure_id": "F241",
    "report_id": "R011",
    "label": "Exhibit 21",
    "context": "Exhibit 21: ... as well as NAND enterprise SSDs as key growth drivers"
  },
  {
    "figure_id": "F242",
    "report_id": "R011",
    "label": "Exhibit 22",
    "context": "Exhibit 22: DRAM supply sufficiency ratio DRAM sufficiency"
  },
  {
    "figure_id": "F243",
    "report_id": "R011",
    "label": "Exhibit 23",
    "context": "Exhibit 23: NAND supply sufficiency ratio NAND sufficiency"
  },
  {
    "figure_id": "F244",
    "report_id": "R011",
    "label": "Exhibit 24",
    "context": "Exhibit 24: DRAM annual wafer capacity additions are moving to all-time high Annual wafer capacity additions by supplier, kwpm"
  },
  {
    "figure_id": "F245",
    "report_id": "R011",
    "label": "Exhibit 25",
    "context": "Exhibit 25: NAND annual wafer capacity additions are held back by DRAM producers Annual wafer capacity additions by supplier, kwpm"
  },
  {
    "figure_id": "F246",
    "report_id": "R011",
    "label": "Exhibit 26",
    "context": "Exhibit 26: AI memory intensity compounds across chip, server, rack and cluster"
  },
  {
    "figure_id": "F247",
    "report_id": "R011",
    "label": "Exhibit 27",
    "context": "Exhibit 27: HBM die penalty – bit-output is reduced due to much larger DRAM dies"
  },
  {
    "figure_id": "F248",
    "report_id": "R011",
    "label": "Exhibit 28",
    "context": "Exhibit 28: HBM cannibalization: share of advanced DRAM wafer is rising sharply"
  },
  {
    "figure_id": "F249",
    "report_id": "R011",
    "label": "Exhibit 29",
    "context": "Exhibit 29: HBM wafer capacity is still highly concentrated in the Big 3 DRAM companies HBM wafer capacity year-end, kwpm"
  },
  {
    "figure_id": "F250",
    "report_id": "R011",
    "label": "Exhibit 33",
    "context": "Exhibit 33: AI prioritization turns 2027 supply growth into a consumer memory shortfall"
  },
  {
    "figure_id": "F251",
    "report_id": "R011",
    "label": "Exhibit 34",
    "context": "Exhibit 34: Buyer Hierarchy: Who gets memory supply first? ```mermaid graph TD"
  },
  {
    "figure_id": "F252",
    "report_id": "R011",
    "label": "Exhibit 35",
    "context": "Exhibit 35: Memory demand is overwhelmingly shifting towards data center technologies and away from more consumer-facing Smartphone and PC markets NAND Bit Demand Mix"
  },
  {
    "figure_id": "F253",
    "report_id": "R011",
    "label": "Exhibit 36",
    "context": "Exhibit 36: Consumer electronics companies continue to call out margin pressures relating to memory cost inflation Exhibit 37: We estimate that memory accounts for 5-70% of tech hardware products, with servers and PCs more exposed t"
  },
  {
    "figure_id": "F254",
    "report_id": "R011",
    "label": "Exhibit 38",
    "context": "Exhibit 38: Our quant analysis implies low-end smartphones and PCs are the most demand elastic, while servers, storage and high-end smartphones are least at risk of demand destruction from higher prices Demand Elasticity by Hardware"
  },
  {
    "figure_id": "F255",
    "report_id": "R011",
    "label": "Exhibit 37",
    "context": "Exhibit 40: Based on latest industry estimates, memory revenue will increase by \\$600B in 2026 ... Incremental Memory Revenue vs. Smartphone, PC, Server, Storage TAM (2026)"
  },
  {
    "figure_id": "F256",
    "report_id": "R011",
    "label": "Exhibit 41",
    "context": "Exhibit 41: ... which we estimate translates into \\~\\$600B of incremental memory cost across Smartphone, Server, PC, and External Storage markets Incremental Memory Cost & TAM by Market (2026)"
  },
  {
    "figure_id": "F257",
    "report_id": "R011",
    "label": "Exhibit 43",
    "context": "Exhibit 42: We estimate that in order to protect gross margins, hardware vendors would need to raise prices by 35-115% Y/Y in CY26 Y/Y ASP Growth Needed to Hold Gross Margins Steady"
  },
  {
    "figure_id": "F258",
    "report_id": "R011",
    "label": "Exhibit 43",
    "context": "Exhibit 43: For context, if PC ASPs were to rise 67% Y/Y, it would mark the strongest Y/Y ASP growth in PC market history, far surpassing COVID-era inflation"
  },
  {
    "figure_id": "F259",
    "report_id": "R011",
    "label": "Exhibit 44",
    "context": "Exhibit 44: DRAM inventory"
  },
  {
    "figure_id": "F260",
    "report_id": "R011",
    "label": "Exhibit 45",
    "context": "Exhibit 45: NAND inventory"
  },
  {
    "figure_id": "F261",
    "report_id": "R011",
    "label": "Exhibit 46",
    "context": "Exhibit 46: Owing to recent increases in memory prices, memory will become 25%+ of the rack BOM for Rubin # Identifying the cyclical and secular risks of chipflation The bigger question in hardware markets remains: what is the sec"
  },
  {
    "figure_id": "F262",
    "report_id": "R011",
    "label": "Exhibit 47",
    "context": "Exhibit 47: 9% of CIOs say they are revisiting their on-prem hardware strategy and considering a more permanent shift of workloads to the cloud given the risk of significant price increases caused by memory price inflation. Action"
  },
  {
    "figure_id": "F263",
    "report_id": "R011",
    "label": "Exhibit 49",
    "context": "Exhibit 49: Sharp rise in PPI electronics ..."
  },
  {
    "figure_id": "F264",
    "report_id": "R011",
    "label": "Exhibit 50",
    "context": "Exhibit 50: ... boosting upstream input costs"
  },
  {
    "figure_id": "F265",
    "report_id": "R011",
    "label": "Exhibit 52",
    "context": "Exhibit 52: The link between ASP and CPI computers is not 1-to-1 ..."
  },
  {
    "figure_id": "F266",
    "report_id": "R011",
    "label": "Exhibit 53",
    "context": "Exhibit 53: ... and the relationship for smartphones is even weaker"
  },
  {
    "figure_id": "F267",
    "report_id": "R011",
    "label": "Exhibit 54",
    "context": "Exhibit 54: Capacity located in Mainland China rises from \\~18% of industry capacity in 2023 to \\~23% in 2028E"
  },
  {
    "figure_id": "F268",
    "report_id": "R011",
    "label": "Exhibit 55",
    "context": "Exhibit 55: Mainland China accounts for 30% share of 2023–28E net DRAM wafer additions, behind South Korea"
  },
  {
    "figure_id": "F269",
    "report_id": "R011",
    "label": "Exhibit 60",
    "context": "Exhibit 60: Memory cycle conditions by type Memory cycle conditions by type Supply/demand balance from oversupply to critically tight"
  },
  {
    "figure_id": "F270",
    "report_id": "R011",
    "label": "Exhibit 61",
    "context": "Exhibit 61: DRAM Contract price YoY vs. NTM P/B"
  },
  {
    "figure_id": "F271",
    "report_id": "R011",
    "label": "Exhibit 62",
    "context": "Exhibit 62: DRAM cycles in perspective over the last 30 years"
  },
  {
    "figure_id": "F272",
    "report_id": "R011",
    "label": "Exhibit 63",
    "context": "Exhibit 63: DRAM demand grows every year in terms of bit shipments (1mn Gb eq)"
  },
  {
    "figure_id": "F273",
    "report_id": "R011",
    "label": "Exhibit 64",
    "context": "Exhibit 64: DRAM ASP has rebounded quickly since 2024"
  },
  {
    "figure_id": "F274",
    "report_id": "R011",
    "label": "Exhibit 65",
    "context": "Exhibit 65: DRAM inventory"
  },
  {
    "figure_id": "F275",
    "report_id": "R011",
    "label": "Exhibit 66",
    "context": "Exhibit 66: NAND inventory"
  },
  {
    "figure_id": "F276",
    "report_id": "R011",
    "label": "Exhibit 67",
    "context": "Exhibit 67: DRAM Capex (US\\$ mn)"
  },
  {
    "figure_id": "F277",
    "report_id": "R011",
    "label": "Exhibit 68",
    "context": "Exhibit 68: NAND Capex (US\\$ mn)"
  },
  {
    "figure_id": "F278",
    "report_id": "R011",
    "label": "Exhibit 69",
    "context": "Exhibit 69: DRAM in the context of the semiconductor cycle – revenue YoY is highly correlated for memory with DRAM at a more advanced stage relative to NAND"
  },
  {
    "figure_id": "F279",
    "report_id": "R013",
    "label": "Figure 3",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Net long copper positioning is now relatively elevated but remains below the highs of late 2025 and 2024. Funds gross short positions remain subdued on COMEX, likely partly due to lingering "
  },
  {
    "figure_id": "F280",
    "report_id": "R013",
    "label": "Figure 4",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 4. Funds are reluctant to be short copper, particularly on COMEX likely given lingering tariff risk, this could shift post June."
  },
  {
    "figure_id": "F281",
    "report_id": "R013",
    "label": "Figure 5",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. We think lingering fears of a potential US tariff on refined copper can support sentiment until July, beyond which inventory draws/reduced incentive to finance metal domestically can act as "
  },
  {
    "figure_id": "F282",
    "report_id": "R013",
    "label": "Figure 6",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 6. US imports have matched typical import requirements for the last month or so, but widening of arb could incentivise a reacceleration of US-bound shipments"
  },
  {
    "figure_id": "F283",
    "report_id": "R013",
    "label": "Figure 8",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 8. Scrap and mine supply growth expected to fail to match AI and energy transition demand growth this year and next (if we assume any cyclical demand recovery the gap becomes more sev"
  },
  {
    "figure_id": "F284",
    "report_id": "R013",
    "label": "Figure 9",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 9. This reliance on scrap to meet projected demand is shown below as a rising “call-on-scrap” (end-use consumption minus mine supply)"
  },
  {
    "figure_id": "F285",
    "report_id": "R013",
    "label": "Figure 10",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 10. China scrap imports implied from value have broadly correlated with price over time and provide a very broad measure of global copper scrap supply response"
  },
  {
    "figure_id": "F286",
    "report_id": "R013",
    "label": "Figure 11",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 11. China scrap imports up slightly y/y, but do not suggest any surge in scrap recovery that might be expected given copper prices \\~\\$3.5k/t higher y/y in Q1."
  },
  {
    "figure_id": "F287",
    "report_id": "R013",
    "label": "Figure 12",
    "context": "# Power installations base effect weighs on tracked global copper end-use Implied global copper end-use from our proprietary GCET tracker, declined by 0.6% YoY in March 2026, due mainly to a large statistical base effect from China renewables demand due to the"
  },
  {
    "figure_id": "F288",
    "report_id": "R013",
    "label": "Figure 12",
    "context": "The structural drivers of copper demand continue to underpin demand growth. Increased AI-related capex spending, rising EV penetration, surging BESS installations, and a still- growing renewable energy pipeline remain supportive for demand. Despite year-on-yea"
  },
  {
    "figure_id": "F289",
    "report_id": "R013",
    "label": "Figure 14",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 14. Stronger PMIs imply likely recent resilience in cyclical copper demand, but impact of SoH yet to be felt"
  },
  {
    "figure_id": "F290",
    "report_id": "R013",
    "label": "Figure 15",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 15. Weaker China copper end-use (note China's power-related and copper semi exports are captured as Ex-China end-use) has slowed global copper consumption"
  },
  {
    "figure_id": "F291",
    "report_id": "R013",
    "label": "Figure 16",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. China's implied copper end-use had a subdued start to 1Q'26. Based on our tracker, implied copper consumption declined by \\~2% YoY in March. The weakness largely reflects a softer domestic E"
  },
  {
    "figure_id": "F292",
    "report_id": "R013",
    "label": "Figure 17",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 17. China EV retail sales down 17% y/y in 4M'26 China EV retail sales (k units)"
  },
  {
    "figure_id": "F293",
    "report_id": "R013",
    "label": "Figure 18",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 18. China EV exports surged 120% y/y in 4M'26 China EV exports(k units)"
  },
  {
    "figure_id": "F294",
    "report_id": "R013",
    "label": "Figure 19",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 19. BEVs have gained market share over the last 12 months"
  },
  {
    "figure_id": "F295",
    "report_id": "R013",
    "label": "Figure 20",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 20. China's solar installations understandably softer after reporting spike ahead of policy changes last year China monthly solar power installations in GW AC"
  },
  {
    "figure_id": "F296",
    "report_id": "R013",
    "label": "Figure 21",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 21. China's wind installations growing albeit at a slower pace China monthly wind power installations in GW"
  },
  {
    "figure_id": "F297",
    "report_id": "R013",
    "label": "Figure 22",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. We think China refined copper consumption (distinct from end-use) has been supported by robust export activity, particularly in solar, batteries and EVs. Our tracker includes total China aut"
  },
  {
    "figure_id": "F298",
    "report_id": "R013",
    "label": "Figure 23",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission."
  },
  {
    "figure_id": "F299",
    "report_id": "R014",
    "label": "Exhibit 2",
    "context": "Exhibit 2: NEV dealer discount trend"
  },
  {
    "figure_id": "F300",
    "report_id": "R014",
    "label": "Exhibit 3",
    "context": "Exhibit 3: ICE dealer discount trend"
  },
  {
    "figure_id": "F301",
    "report_id": "R014",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Battery and battery raw materials prices"
  },
  {
    "figure_id": "F302",
    "report_id": "R015",
    "label": "Exhibit 2",
    "context": "Exhibit 2: NEV dealer discount trend"
  },
  {
    "figure_id": "F303",
    "report_id": "R015",
    "label": "Exhibit 3",
    "context": "Exhibit 3: ICE dealer discount trend"
  },
  {
    "figure_id": "F304",
    "report_id": "R015",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Battery and battery raw materials prices"
  },
  {
    "figure_id": "F305",
    "report_id": "R016",
    "label": "Exhibit 1",
    "context": "Exhibit 1: HMC & Kia (together HMK) US monthly key metrics snapshot Exhibit 2: HMK US volume trend"
  },
  {
    "figure_id": "F306",
    "report_id": "R016",
    "label": "Exhibit 3",
    "context": "Exhibit 3: HMK US volume YoY trend"
  },
  {
    "figure_id": "F307",
    "report_id": "R016",
    "label": "Exhibit 4",
    "context": "Exhibit 4: HMK US M/S trend"
  },
  {
    "figure_id": "F308",
    "report_id": "R016",
    "label": "Exhibit 5",
    "context": "Exhibit 5: HMK US M/S YoY gain trend"
  },
  {
    "figure_id": "F309",
    "report_id": "R016",
    "label": "Exhibit 6",
    "context": "Exhibit 6: HMK US HEV volume trend"
  },
  {
    "figure_id": "F310",
    "report_id": "R016",
    "label": "Exhibit 7",
    "context": "Exhibit 7: HMK US HEV volume YoY trend"
  },
  {
    "figure_id": "F311",
    "report_id": "R016",
    "label": "Exhibit 8",
    "context": "Exhibit 8: HMK US HEV mix trend"
  },
  {
    "figure_id": "F312",
    "report_id": "R016",
    "label": "Exhibit 9",
    "context": "Exhibit 9: HMK US HEV M/S trend"
  },
  {
    "figure_id": "F313",
    "report_id": "R017",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Primary weekly unit sales and four-week moving average – Total 50 cities"
  },
  {
    "figure_id": "F314",
    "report_id": "R019",
    "label": "Figure 1",
    "context": "# Battery production pipeline reaffirms the strong demand month by month Channel check with ZE Consulting suggests on-the-ground battery production pipeline extends the strong momentum YTD, easing off previous concerns that (1) NEV might be weaker than expecte"
  },
  {
    "figure_id": "F315",
    "report_id": "R019",
    "label": "Figure 2",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 2. Top-5 battery production pipeline YoY change"
  },
  {
    "figure_id": "F316",
    "report_id": "R019",
    "label": "Figure 3",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 3. Commercial vehicle % of battery installation kept soaring in the last few quarters"
  },
  {
    "figure_id": "F317",
    "report_id": "R019",
    "label": "Figure 4",
    "context": "The chart displays the percentage composition of BEV-PV (%), PHEV-PV (%), and Commercial vehicle (%). The data is presented in a horizontal bar format with each bar representing a quarter from Q1 to Q4. The legend indicates that BEV-PV is represented by the da"
  },
  {
    "figure_id": "F318",
    "report_id": "R019",
    "label": "Figure 6",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Zimbabwe (+ve to lithium price) – Zimbabwe resumes the spodumene export by end of Apr-26, after its \\~3 months spodumene export restriction since Feb-26. We estimate the shipment should grad"
  },
  {
    "figure_id": "F319",
    "report_id": "R019",
    "label": "Figure 7",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 7. Lithium carbonate weekly inventory"
  },
  {
    "figure_id": "F320",
    "report_id": "R019",
    "label": "Figure 8",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 8. Spread of battery-grade LC (assume 1M inventory)"
  },
  {
    "figure_id": "F321",
    "report_id": "R019",
    "label": "Figure 9",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 9. Spread of battery-grade LC (assume 1M inventory)"
  },
  {
    "figure_id": "F322",
    "report_id": "R019",
    "label": "Figure 10",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 10. Lithium carbonate monthly production © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 11. Lithium carbonate weekly production"
  },
  {
    "figure_id": "F323",
    "report_id": "R019",
    "label": "Figure 10",
    "context": "Figure 10. Lithium carbonate monthly production © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 11. Lithium carbonate weekly production"
  },
  {
    "figure_id": "F324",
    "report_id": "R019",
    "label": "Figure 12",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 12. Lithium carbonate - inventory in days"
  },
  {
    "figure_id": "F325",
    "report_id": "R019",
    "label": "Figure 13",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 13. Spodumene import by country (4M26)"
  },
  {
    "figure_id": "F326",
    "report_id": "R019",
    "label": "Figure 14",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 14. Monthly apparent consumption (lithium carbonate)"
  },
  {
    "figure_id": "F327",
    "report_id": "R019",
    "label": "Figure 15",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 15. Monthly apparent consumption (lithium hydroxide)"
  },
  {
    "figure_id": "F328",
    "report_id": "R019",
    "label": "Figure 19",
    "context": "Investment thesis — Ganfeng Lithium should benefit from the lithium ASP uplift amid robust on-the-ground battery demand and improving cost competitiveness on increasing contribution from low-cost upstream resources (i.e., Goulamina, Mariana, and others). Its c"
  },
  {
    "figure_id": "F329",
    "report_id": "R019",
    "label": "Figure 20",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 20. Ganfeng Lithium - H: 12M forward P/B"
  },
  {
    "figure_id": "F330",
    "report_id": "R019",
    "label": "Figure 24",
    "context": "Investment thesis — Tianqi Lithium is one of the best positions to benefit from lithium upcycle, on back of its pure exposure to lithium space from upstream spodumene to downstream lithium carbonate. Lithium price uptick supports Tianqi with decent earnings re"
  },
  {
    "figure_id": "F331",
    "report_id": "R019",
    "label": "Figure 25",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 25. Tianqi Lithium - H: 12M forward P/B"
  },
  {
    "figure_id": "F332",
    "report_id": "R022",
    "label": "Figure 1",
    "context": "Figure 1: Steepest and flattest 10s30s curves"
  },
  {
    "figure_id": "F333",
    "report_id": "R022",
    "label": "Figure 2",
    "context": "Figure 2: Largest 1m changes in 10s30s"
  },
  {
    "figure_id": "F334",
    "report_id": "R022",
    "label": "Figure 3",
    "context": "Figure 4: 10s30s curves versus the 10y level relationship"
  },
  {
    "figure_id": "F335",
    "report_id": "R022",
    "label": "Figure 5",
    "context": "Figure 5: 1m change in aggregate 10s30s versus 1m change in aggregate 10y spreads"
  },
  {
    "figure_id": "F336",
    "report_id": "R022",
    "label": "Figure 6",
    "context": "Figure 6: 1m change in aggregate 10s30s versus 1m change in 10y spreads by issuer"
  },
  {
    "figure_id": "F337",
    "report_id": "R022",
    "label": "Figure 7",
    "context": "Figure 7: Historical EM aggregate 10s30s spread curve slope"
  },
  {
    "figure_id": "F338",
    "report_id": "R022",
    "label": "Figure 8",
    "context": "Figure 8: Historical US treasury 10s30s yield curve slope"
  },
  {
    "figure_id": "F339",
    "report_id": "R022",
    "label": "Figure 9",
    "context": "Figure 9: Historical EMBIG vs. CEMBI spread curve slope"
  },
  {
    "figure_id": "F340",
    "report_id": "R022",
    "label": "Figure 10",
    "context": "Figure 10: Historical EM IG vs. HY spread curve slope"
  },
  {
    "figure_id": "F341",
    "report_id": "R022",
    "label": "Figure 11",
    "context": "Figure 11: Historical sovereign vs. quasi-sovereign curve slope"
  },
  {
    "figure_id": "F342",
    "report_id": "R022",
    "label": "Figure 12",
    "context": "Figure 12: EM corporate vs. US HG corporate spread curve slope"
  },
  {
    "figure_id": "F343",
    "report_id": "R022",
    "label": "Figure 13",
    "context": "Figure 13: Historical EMBIGD curve slope by region"
  },
  {
    "figure_id": "F344",
    "report_id": "R022",
    "label": "Figure 14",
    "context": "Figure 14: Historical CEMBI curve slope by region"
  },
  {
    "figure_id": "F345",
    "report_id": "R022",
    "label": "Figure 15",
    "context": "Figure 15: 10s30s spread curve slopes versus 10y spread"
  },
  {
    "figure_id": "F346",
    "report_id": "R022",
    "label": "Figure 16",
    "context": "Figure 16: Asia issuers 10s30s spread curve"
  },
  {
    "figure_id": "F347",
    "report_id": "R022",
    "label": "Figure 17",
    "context": "Figure 17: CEEMEA issuers Figure 18: Latin American issuers"
  },
  {
    "figure_id": "F348",
    "report_id": "R022",
    "label": "Figure 17",
    "context": "Figure 17: CEEMEA issuers Figure 18: Latin American issuers"
  },
  {
    "figure_id": "F349",
    "report_id": "R022",
    "label": "Figure 19",
    "context": "Figure 19: 10s30s spread curve slopes versus 10y spread"
  },
  {
    "figure_id": "F350",
    "report_id": "R022",
    "label": "Figure 20",
    "context": "Figure 20: EMBIG sovereign issuers Figure 21: EMBIG quasi-sovereign issuers"
  },
  {
    "figure_id": "F351",
    "report_id": "R022",
    "label": "Figure 20",
    "context": "Figure 20: EMBIG sovereign issuers Figure 21: EMBIG quasi-sovereign issuers"
  },
  {
    "figure_id": "F352",
    "report_id": "R022",
    "label": "Figure 22",
    "context": "Figure 22: CEMBI issuers"
  },
  {
    "figure_id": "F353",
    "report_id": "R022",
    "label": "Figure 23",
    "context": "Figure 23: 10s30s spread curve slopes versus average credit rating Figure 24: Asia issuers 10s30s spread curve"
  },
  {
    "figure_id": "F354",
    "report_id": "R022",
    "label": "Figure 23",
    "context": "Figure 23: 10s30s spread curve slopes versus average credit rating Figure 24: Asia issuers 10s30s spread curve"
  },
  {
    "figure_id": "F355",
    "report_id": "R022",
    "label": "Figure 25",
    "context": "Figure 25: CEEMEA issuers"
  },
  {
    "figure_id": "F356",
    "report_id": "R022",
    "label": "Figure 26",
    "context": "Figure 26: Latin American issuers 10s30s spread curve"
  },
  {
    "figure_id": "F357",
    "report_id": "R022",
    "label": "Figure 27",
    "context": "Figure 27: Steepest 10s30s spread curves across EM sovereign and corporate credit Figure 28: Steepest 10s30s curves versus the 10y spread"
  },
  {
    "figure_id": "F358",
    "report_id": "R022",
    "label": "Figure 29",
    "context": "Figure 29: Steepest 10s30s curves and 1m change"
  },
  {
    "figure_id": "F359",
    "report_id": "R022",
    "label": "Figure 30",
    "context": "Figure 30: Flattest 10s30s spread curves across EM sovereign and corporate credit Figure 31: Flattest 10s30s curves versus the 10y spread"
  },
  {
    "figure_id": "F360",
    "report_id": "R022",
    "label": "Figure 32",
    "context": "Figure 32: Flattest 10s30s curves and 1m change"
  },
  {
    "figure_id": "F361",
    "report_id": "R022",
    "label": "Figure 33",
    "context": "Figure 33: Largest 1m steepening across 10s30s spread curves Figure 34: 1m change in 10s30s curves versus the current 10s30s"
  },
  {
    "figure_id": "F362",
    "report_id": "R022",
    "label": "Figure 35",
    "context": "Figure 35: Largest 1m steepening and current 10s30s slope"
  },
  {
    "figure_id": "F363",
    "report_id": "R022",
    "label": "Figure 36",
    "context": "Figure 36: Largest 1m flattening across 10s30s spread curves Figure 37: Largest 1m flattening across 10s30s spread curves"
  },
  {
    "figure_id": "F364",
    "report_id": "R022",
    "label": "Figure 38",
    "context": "Figure 38: Largest 1m flattening and current 10s30s slope"
  },
  {
    "figure_id": "F365",
    "report_id": "R023",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Micron Gross PPE by asset class, PPE to expand more by the end of FY27 than 1QFY20-2QFY26 We think both stocks can continue to outperform as the multiples remains reasonable on near term estimates (sub 10x PE on CY27 e"
  },
  {
    "figure_id": "F366",
    "report_id": "R024",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Total system payment volume picked up 29% yoy in 1Q26 vs 5% in 4Q25. Bank card consumption growth turned positive, up 3.2% yoy, vs decline in 2025."
  },
  {
    "figure_id": "F367",
    "report_id": "R024",
    "label": "Exhibit 2",
    "context": "Exhibit 2: UnionPay payment growth rebounded from 4Q, up 11.2% yoy; while NetsUnion payment growth slightly moderated to 7.2% yoy."
  },
  {
    "figure_id": "F368",
    "report_id": "R027",
    "label": "Figure 1",
    "context": "Huawei Harmony – May-26 deliveries came at 46,122 units (+4% YoY/+41% MoM), with 5M26 deliveries +27% YoY to 191,598 units. Orders update: all-new M9 non-refundable order over 20k units in 24 hours post launch, Luxeed V9 non-refundable orders over 10.5k units "
  },
  {
    "figure_id": "F369",
    "report_id": "R027",
    "label": "Figure 2",
    "context": "Horizontal Axis: May-26 MoM growth © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 2. Various NEV Players: May-26 Sales vs May-26 YoY"
  },
  {
    "figure_id": "F370",
    "report_id": "R027",
    "label": "Figure 3",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. © 2026 Citi Inc. No redistribution without Citi's written permission. © 2026 Citi Inc. No redistribution without Citi's written permission."
  },
  {
    "figure_id": "F371",
    "report_id": "R027",
    "label": "Figure 4",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. © 2026 Citi Inc. No redistribution without Citi's written permission. © 2026 Citi Inc. No redistribution without Citi's written permission."
  },
  {
    "figure_id": "F372",
    "report_id": "R027",
    "label": "Figure 5",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. © 2026 Citi Inc. No redistribution without Citi's written permission. # Appendix A-1"
  },
  {
    "figure_id": "F373",
    "report_id": "R031",
    "label": "Exhibit 6",
    "context": "Exhibit 1: Overview of select 1L metastatic NSCLC trials Histology"
  },
  {
    "figure_id": "F374",
    "report_id": "R031",
    "label": "Exhibit 3",
    "context": "Exhibit 3: OS curves from the ITT population of HARMONi-6"
  }
]