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
    "title": "DB：市场正从“成本推动的通胀”转向“需求分化的定价游戏”",
    "digest": "[wechat_article.md]\n# DB：市场正从“成本推动的通胀”转向“需求分化的定价游戏”\n\n这份来自DB的最新通胀监测报告，表面上是5月CPI与PPI数据的例行更新，但仔细拆解其内部结构变化后，一个更关键的判断浮现出来：中国经济正在经历一轮价格信号的“结构性分裂”。上游PPI的持续回暖并非简单的成本传导，其驱动力正在从能源价格切换至AI相关需求与中下游的议价能力重塑。与此同时，CPI的停滞与核心通胀的走软，则揭示出终端消费需求并未同步复苏。报告给出的核心洞察是，市场真正需要关注的，不是通胀数字本身的高低，而是这一轮价格分化如何重新定义不同产业的利润分配与竞争格局。\n\n这份报告发布于2026年6月10日，覆盖了5月份的通胀数据。其价值不在于数据点的罗列，而在于指出了驱动力的切换。对于产业决策者和投资者而言，理解这种切换，比预测下个月的CPI数字重要得多。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. PPI的再通胀已从“能源单引擎”切换至“AI与传导双引擎”\n\n5月PPI同比上涨3.9%，符合预期，环比仍为正增长0.5%。但报告明确指出，4月之前驱动PPI上涨的核心变量——国际能源价格——在5月趋于平稳，石油相关行业价格甚至出现小幅环比下跌。这意味着，PPI的韧性并非来自能源的二次冲击，而是来自两个新的结构性力量。\n\n第一个力量是前期能源价格上涨的“成本传导”效应正在向中下游扩散。化学制品、黑色金属、纺织等中下游行业在5月录得了更快的环比价格涨幅。这并非新一轮成本冲击，而是产业链消化前期成本后的重新定价。\n\n第二个力量更具长期意义：AI相关需求持续推高锡、铜等有色金属价格，并带动电气机械、光纤电缆、计算机等终端产品价格上行。这不是短期的库存回补，而是由资本开支驱动的结构性需求。报告将其单独列出，暗示这一力量在未来几个季度可能成为PPI的新锚\n\n[... middle omitted ...]\n\n步拆解AI产业链的定价权分布，以及中游制造业的利润压力测试。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nPPI涨 CPI平，内需在悄悄走弱\n\n📊 5月通胀信号\n\n---\n\n最近投行研报更新了5月通胀数据，信息量很大，直接划重点👇\n\n1⃣ **PPI持续回暖，但驱动力在切换**\n5月PPI同比+3.9%，环比+0.5%（比4月放缓）。能源价格涨势趋稳，但涨价开始向下游传导：\n- 化学、黑色金属、纺织等中下游涨价加快\n- AI需求拉动锡、铜、电气机械、光纤、电脑等价格\n- 预计年底PPI到5%左右，年均3.3%\n\n2⃣ **CPI原地踏步，内需信号偏弱**\n5月CPI同比1.2%，环比-0.1%。服务业、食品、家电、汽车都出现环比下降。\n- 能源价格环比-0.1%（前月+5.7%）\n- AI需求撑住手机（+1.6%）和电脑（+1.1%）\n- 夏季服装涨价，但整体消费需求偏软\n\n3⃣ **全年CPI预测下调**\n因以旧换新补贴效果边际减弱，研报把全年CPI预测从1.6%下调至1.5%，年底预期从2.0%降至1.8%。\n\n整体来看：PPI涨价在扩散，但内需端CPI走弱，消费复苏仍需观察。\n\n欢迎一起讨论你对通胀和消费趋势的判断～\n\n#学习笔记\n\n[source_mineru.md]\nEconomics\n\nChina M\n\n[... middle omitted ...]\n\ninued, with chemicals, ferrous metals and textiles all registering faster sequential price gains. In addition, AI-related demand continued to push up prices in non-ferrous metals such as tin a\n\n[... middle omitted ...]\n\nl: (44) 20 7545 8000</td><td>The DB Center 1 Columbus Circle New York, NY 10019 Tel: (1) 212 250 2500</td><td>Filiale Singapur One Raffles Quay, South Tower Singapore 048583 Tel: (65) 6423 8001</td><td></td></tr></table>"
  },
  {
    "id": "R002",
    "title": "摩根斯坦利：市场低估了“再通胀退潮”的结构性含义",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：市场低估了“再通胀退潮”的结构性含义\n\n5月的通胀数据刚刚发布，PPI同比冲至3.9%，创下近四年新高。如果只看这个数字，很容易得出“通胀压力正在积聚”的判断。但摩根斯坦利这份最新报告揭示了一个完全不同的图景：通胀的驱动力正在快速切换，而真正重要的不是PPI同比有多高，而是环比动能在哪里减速。\n\n报告的核心主张可以概括为一句话：**5月数据确认了中国正处于“再通胀退潮”的早期阶段，油价脉冲消退后，下游缺乏接力，核心CPI将进入温和下行通道。** 这不是一个短期波动，而是一个结构性信号——意味着企业定价权的分布正在发生根本性变化。\n\n为什么现在需要认真对待这份报告？因为市场对通胀的讨论仍然停留在“油价涨了多少”“PPI同比会不会破4%”这些表层问题上。而摩根斯坦利把焦点拉到了更关键的层面：在油价推动消退之后，还有哪些力量能支撑价格？答案是，几乎没有。这种“单一引擎熄火”的格局，对资产定价、行业配置和宏观判断都有深远含义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 5月PPI环比动能的骤降，暴露了“低基数幻觉”背后的真实疲弱\n\n5月PPI同比从2.8%跳升至3.9%，表面上看非常强劲。但摩根斯坦利报告明确拆解了背后的结构：环比从4月的1.7%骤降至0.5%，降幅高达1.2个百分点。而环比才是衡量当前价格动能的真实指标。\n\n这个环比减速几乎完全由油价驱动。4月油价对PPI环比的贡献高达1.7个百分点中的绝大部分，而5月全球油价趋于稳定后，石油相关的价格推升效应归零。换言之，4月的“通胀脉冲”本质上是油价的一次性冲击，而不是需求驱动的持续性上涨。\n\n对于投资者来说，这意味着什么？如果你在4月PPI数据公布后认为“通胀上行趋势已经确立”，那么5月的数据就是一个重要的修正信号。PPI同比在未来两个月可能因\n\n[... middle omitted ...]\n\n产能出清节奏”“政策应对空间”等本篇导读未能完全回答的问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n油价推力减弱，通胀靠啥撑？\n\n**通胀分化期**\n\n**PPI冲高但动力放缓，核心CPI走弱**\n\n---\n\n5月PPI同比冲到了3.9%（预期3.7%），创近四年新高，主要是低基数效应。但环比增速从4月的1.7%大幅回落到0.5%，核心原因是油价推动力减弱了。\n\n1️⃣ **油价降温，通胀扩散有限**\n\n全球油价稳定后，零售燃料和运输成本回落，CPI环比从0.6%降到0.1%。除石油外，只有煤炭（夏季用电需求）和有色金属（铝相关资本开支）小幅上涨，下游工厂价格环比持平在0.2%，说明产能过剩仍在压制价格传导。\n\n2️⃣ **AI需求拉动消退，核心CPI走弱**\n\n剔除黄金后，核心CPI环比从0.2%降到0%。之前AI换机潮带动的电子产品涨价已基本结束。就业市场疲弱、房地产调整持续，消费端难有起色——光靠资本密集型出口撑不起价格。\n\n3️⃣ **前瞻：PPI还会冲，但核心CPI要下行**\n\n6-7月PPI同比可能冲上4%以上（低基数），但核心CPI会进入温和下行通道。最大风险是地缘冲突导致油价非线性飙升——某外资投行已将Q4 2026和H1 2027的油价预测上调了5美元/桶。\n\n总结一下：短期通胀靠基数效应\n\n[... middle omitted ...]\n\n a low base, core CPI will likely enter a shallow moderating path. Tail risk remains a non-linear oil price spike.\n\nNarrow industrial reflation beyond oil: May PPI MoM softened on a sequential\n\n[... middle omitted ...]\n\narantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n© 2026 MS"
  },
  {
    "id": "R003",
    "title": "Citi：PPI再通胀的真正含义不是能源，而是中国工业定价权的结构性拐点",
    "digest": "[wechat_article.md]\n# Citi：PPI再通胀的真正含义不是能源，而是中国工业定价权的结构性拐点\n\n五月通胀数据公布后，市场注意力几乎被CPI的小幅不及预期和能源价格回落所吸引。但这份Citi研报提出的核心判断值得认真对待：PPI再通胀正在从“能源脉冲”切换为“结构扩散”——这不是一次短暂的价格波动，而是中国工业部门定价逻辑正在发生改变的早期信号。\n\nCiti维持CPI和PPI全年预测分别为1.0%和2.8%同比，这本身并不激进。真正有意思的是报告在数据细节中捕捉到的三个结构性变化：投资企稳的初步迹象、AI超周期开始显性化为价格力量、以及K型分化下下游通缩与上游通胀的持续拉锯。\n\n这些事实合在一起，指向一个比市场共识更复杂的叙事：中国的价格信号正在从“总量问题”演变为“结构问题”。对于产业决策者和资产配置者来说，理解这种结构性分化，远比争论CPI是否见底更有价值。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 能源脉冲退潮后，PPI扩散才是关键信号\n\n五月PPI同比3.9%，略高于Citi预期的3.8%，但环比增速从四月的1.7%大幅回落至0.5%。表面上看，这是中东冲突溢出的价格冲击正在消退——石油和天然气开采PPI环比从18.5%骤降至-0.1%，燃料加工PPI环比归零。\n\n但报告明确指出，真正值得关注的不是能源的退潮，而是再通胀的“广度”在扩大。Citi估算，能源和化工对五月PPI环比的合计贡献仅为0.2个百分点，远低于四月的1.6个百分点。这意味着，即使剔除能源冲击，PPI仍然录得了0.3个百分点的环比正增长。\n\n这个“剔除能源后的PPI”才是报告的核心洞察。它说明工业品价格上涨的动力正在从单一的地缘政治冲击，切换为更广泛的内生性因素——包括投资需求的边际改善、上游原材料成本的传导、以及部分行业供给侧的收紧。\n\n对于投资者而\n\n[... middle omitted ...]\n\n原始图表、更详细的行业拆解，以及对关键假设的持续跟踪和验证。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月物价：AI通胀来了，但消费还在冷\n\nAI超级周期正在成为新的通胀推手\n\n**5月物价数据：上游暖，下游冷**\n\n5月CPI同比1.2%，略低于预期。PPI继续回升至3.9%，但结构分化明显。\n\n**1. 能源冲击退潮，但PPI再通胀在扩散**\n\n中东冲突带来的能源脉冲正在消退。5月石油开采PPI环比从+18.5%骤降至-0.1%。但有意思的是，PPI改善的广度在扩大——煤炭开采PPI环比+3.2%，连续5个月加速；黑色金属矿采选环比+0.9%，建筑业相关PPI贡献创一年次高。研报认为这是“投资企稳的初步迹象”。\n\n**2. AI超级周期正在制造通胀**\n\n一个容易被忽略的点：AI不仅影响科技PPI，也开始推高电信CPI。5月通信设备CPI环比+1.5%，同比6.6%，创历史第二高。而汽车CPI环比-0.4%，已连跌3个月——消费需求疲弱拖累。同一个经济体内，AI相关和传统耐用品的价格走势完全相反。\n\n**3. 下游通缩仍在持续**\n\n核心CPI环比-0.1%，服务价格在五一假期后回落。旅游价格环比从+4.1%降至+1.0%，租车和机票价格环比分别-6.8%和-6.3%。下游多数行业PPI仍处于通缩区间，说\n\n[... middle omitted ...]\n\nthe holiday boost unwound, pointing to still-sluggish consumer demand that continues to cap upstream prices passthrough. We maintain our forecast for CPI and PPI at 1.0% YoY and 2.8% YoY, resp\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R004",
    "title": "Citi：市场低估了“六网”投资对中国固定资产投资的托底力度",
    "digest": "[wechat_article.md]\n# Citi：市场低估了“六网”投资对中国固定资产投资的托底力度\n\n中国四月固定资产投资增速转负，市场情绪一度转向悲观。但Citi在最新研报中提出了一个值得重新审视的判断：政策正在加速落地，以“六网”为核心的新一轮基建投资，其规模、节奏和融资路径，都比市场预期的更为清晰和坚决。这份报告的价值不在于罗列项目清单，而在于它揭示了投资结构正在发生的深层切换——从传统的房地产和旧基建，转向由AI算力、数据中心和城市更新驱动的新经济投资。这意味着，市场对投资增速的线性外推可能低估了结构性变量的影响。\n\n四月固定资产投资累计同比增速转负，是这一轮经济复苏节奏中最刺眼的数据点。按照传统框架，这意味着内需疲弱，政策刺激效果递减。但Citi的分析提供了一个不同的视角：投资总量的短期失速，恰恰是结构转换期的典型特征。旧动能（房地产）的收缩速度超过了新动能（新基建、制造业升级）的扩张速度，造成了统计上的“真空期”。而近期一系列高规格项目的启动，正是政策层试图填补这一真空期的主动作为。\n\n三峡新通道、两万亿级别的数据中心投资计划、以及城市更新的明确量化目标，这三件事在同一个月内密集发生，不是巧合。它们共同指向了一个顶层设计的落地：即“六网”建设。Citi的报告点出了一个关键事实——国家发改委年初承诺今年“六网”投资规模超过7万亿元，而市场并未给予足够定价。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 三峡新通道与数据中心：两个标志性项目打开了投资的想象空间\n\n六月八日，三峡新通道项目正式开工，总投资约772亿元，建设周期约十年。这是“十五五”规划中首个启动的超级工程。它的意义不仅在于投资体量，更在于它释放了一个明确的信号：中央层面对大型基建项目的审批和推进节奏正在加快。\n\n与此同时，彭博报道中国计划在未来五年投入约两万亿元建设数据中心\n\n[... middle omitted ...]\n\n产业链调研数据，帮助各位在不确定性中逐步建立自己的判断框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n“六网”落地，AI投资扛大旗\n\n🧠 基建投资的新方向\n\n最近政策密集落地，三大项目浮出水面：\n1️⃣ 三峡新水运通道开工，投资772亿，是十五五首个超级工程\n2️⃣ 数据中心建设规划2万亿，若算上电网配套，总规模至少5万亿\n3️⃣ 城市更新明确量化目标，地下管网改造365千公里\n\n💰 钱从哪来？\n- 中央一般预算：今年已安排970亿用于城市更新\n- 特别国债：地下管网1600亿，数据中心大概率也纳入\n- 政策性金融工具：今年5000亿，明年8000亿\n- 政府引导基金配合\n\n⏰ 为什么现在推？\n四月固投增速转负，稳投资的紧迫性上升。AI超级周期正在展开，基础设施必须跟上。\n\n📊 复苏信号初现\n五月建筑业PMI反弹，水泥开工率改善。但整体固投回升还需要时间，大概率是K型复苏——新经济投资领跑。\n\n🤔 你所在的城市，有感受到城市更新或新基建的推进吗？欢迎一起讨论。\n\n#学习笔记\n\n[source_mineru.md]\n10 Jun 2026 05:47:30 ET | 9 pages\n\n# China Economics\n\nThe \"Six Networks\" Arrive – Driving AI Buildo\n\n[... middle omitted ...]\n\ncial government bonds, and dedicated policy tools. The urgency is clear following April’s sharp investment slowdown. While early green shoots are emerging, the path forward will likely be a K-\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R005",
    "title": "Citi：市场正在重新定价“增长的质量”，而非增长本身",
    "digest": "[wechat_article.md]\n# Citi：市场正在重新定价“增长的质量”，而非增长本身\n\n当绝大多数投资者还在争论AI是泡沫还是革命时，一份来自Citi的年度主题评估框架给出了一个更微妙的信号：市场已经不再为“故事”买单，而是在为“可持续性”和“质量溢价”重新排序。\n\nCiti的Global Theme Machine覆盖了83个全球主题、近3600只股票，建立了超过2万个个股-主题关联。这份报告的价值不在于告诉你哪些主题涨了，而在于揭示了一个关键的结构性变化——主题排名的驱动力正在从单纯的“价格动量”转向“盈利可见性”与“质量因子”的组合。这意味着，即便是在同一个AI赛道内部，不同公司的命运分化才刚刚开始。\n\n这不是一个关于“买什么”的报告，而是一个关于“用什么框架判断买什么”的报告。对于产业决策者和高净值投资者而言，理解这个框架的演化，可能比追逐任何一个具体主题都更重要。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 主题排名的驱动力正在发生根本性切换：从“动量”到“质量”\n\nCiti的排名体系并非简单的涨跌幅排序。它整合了估值、增长、价格动量、质量、低风险、盈利动量六个维度，最终给出综合排名。最新数据显示，排名靠前的主题不再单纯依赖价格动量，而是呈现出“质量+盈利可见性”的双轮驱动特征。\n\n以排名第二的“Risky Business”主题为例，其价格动量排名仅为53（共84个主题），但质量排名第2，低风险排名第1。同样，排名第三的“Pension Shortfalls”主题，估值排名第1，质量排名第7，低风险排名第2。这两个主题的共同特点是：它们不是市场上最“性感”的叙事，但它们在盈利稳定性、估值安全垫和风险控制上得分极高。\n\n这意味着什么？Citi的框架在告诉我们：当前市场的定价逻辑正在从“谁的故事更宏大”转向“谁的盈利更可预测”。\n\n[... middle omitted ...]\n\n暴露度的风险对冲策略，以及几个被当前排名“低估”的主题候选。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI与工业主题持续领跑\n\n**AI与工业持续领跑**\n\n83个全球主题，谁在上涨？\n\n某外资投行最新发布的全球主题研究框架，覆盖83个主题、3600多家公司。5月数据显示，结构性增长主题依然占据主导。\n\n**1/ 哪些主题在领跑？**\n相对MSCI World指数，超额收益最明显的是：\n- Greening the Home（+8.8%）\n- 云计算（+6.5%）\n- 可穿戴技术（+5.2%）\n- AI赋能者（+4.6%）\n- 制造业回流（+3.7%）\n\n数字化+工业转型，是持续主线。\n\n**2/ 排名变化看什么？**\n5月排名提升最快的主题：\n- 云计算：从第7升至第4，价格动能改善明显\n- 可穿戴技术：从第25飙升至第11，盈利动能大幅提升\n- 虚拟现实：从第19升至第9，盈利动能是主要推手\n\n而奢侈品消费、全球旅游、太阳能排名明显下滑——市场开始惩罚“价格涨但基本面跟不上”的主题。\n\n**3/ 哪些公司覆盖多个强势主题？**\n一些公司同时覆盖多个前15主题，比如：\n- 亚马逊（6个主题：SaaS、支付、IT服务、云计算、AI赋能、AI与发电）\n- 谷歌（同样6个主题）\n- 韩国Naver、Kakao（各\n\n[... middle omitted ...]\n\n be delighted to discuss it in greater depth.\n\nTheme Model Performance — The Theme Model showed significant dispersion, with top-performing themes including Greening the Home and Cloud Computi\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R006",
    "title": "JPM：市场低估的不是原油价格，而是美国西海岸成品油的结构性短缺",
    "digest": "[wechat_article.md]\n# JPM：市场低估的不是原油价格，而是美国西海岸成品油的结构性短缺\n\n这份JPM最新发布的石油市场周报，标题意味深长——“The first thousand miles”（最初的一千英里）。它指向一个反直觉的事实：自冲突爆发以来，历史上最大的供应中断，却只带来了一个“平淡无奇”的价格图表。布伦特原油均价仅101美元，几乎完全贴合该行早在3月初就划定的价格路径。\n\n市场普遍关注的是，为什么原油价格没有暴涨？但这份报告真正值得读的判断是：**市场已经通过需求损失和库存释放消化了供应冲击，但成品油市场的结构性紧张，尤其是美国西海岸，正在成为新的、更隐蔽的定价锚点。** 对于关注通胀、供应链和资产定价的决策者而言，真正需要跟踪的，不是布伦特能否站上120美元，而是加州每加仑5.89美元的汽油和7.16美元的柴油，如何通过物流成本传导至全美。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 报告自己推翻了3月的核心假设：成品油短缺并未发生，但“向下游转移”的逻辑失效了\n\n3月初，JPM提出了一个精妙的框架：如果原油价格无法充分反映供应中断，那么调整一定会“向下游转移”——即原油价格维持100美元附近，但短缺会体现在汽油、柴油和航空煤油的裂解价差上。这个框架的第一部分（原油价格路径）被完美验证，但第二部分（成品油短缺）被证伪。\n\n从2月27日至6月8日的数据来看，汽油、柴油和航空煤油价格在经历最初飙升后，已显著回落，炼油利润率不但没有扩大，反而收窄。这意味着，市场吸收冲击的机制比预想的更复杂：**需求损失（冲突区、亚洲、中国、非洲）和库存释放（政府和商业库存）共同作用，使得成品油市场并未出现极端短缺。** 这个“证伪”本身就是一个重要洞察：它告诉我们，全球石油市场的缓冲能力，至少在成品油层面，比许多模型假设的要强。\n\n但这\n\n[... middle omitted ...]\n\n链有深入兴趣的读者，来我们的星球微信群继续讨论这些未解问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n油价100美元，为什么加油站还在涨？\n\n**油价100美元，加州的痛**\n\n史上最大供应中断，油价却波澜不惊。布伦特原油自冲突以来均价仅101美元，市场怎么消化的？答案藏在产品端。\n\n1️⃣ **原油平静，产品市场却暗流涌动**\n   - 研报预测原油会稳在100附近，产品价格飙升。结果原油对了，产品市场没跟——汽油、柴油、航油价格冲高后回落，炼油利润反而收窄。\n   - 市场实际靠“需求损失+大规模库存释放”吸收冲击。冲突区需求减弱，亚洲部分国家直接减少消费，中国替代效应超预期，非洲传统需求破坏也在发生。\n\n2️⃣ **美国零售汽油全年4美元/加仑是常态**\n   - 研报预计2026年剩余时间布伦特均价约100美元，对应美国零售汽油全年维持在4美元/加仑附近。\n   - 远低于极端短缺场景，但对家庭和政策制定者仍是持续压力。\n\n3️⃣ **加州才是真正的“油价孤岛”**\n   - 全美汽油均价已从5月峰值4.56美元回落至4.16美元，但加州仍高达5.89美元，柴油更飙到7.16美元。\n   - 原因：两座炼厂关闭（占州产能17%），依赖亚洲进口的CARB标准汽油因霍尔木兹扰动供应受限，且无管道连接其他州\n\n[... middle omitted ...]\n\nay 2026). Under that scenario, crude prices could hover near \\$100/bbl while scarcity shows up instead in gasoline, diesel, and jet fuel prices. The shock would be expressed not through materi\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 09 Jun 2026 11:28 PM EDT\n\nDisseminated 10 Jun 2026 07:00 AM EDT"
  },
  {
    "id": "R007",
    "title": "JPM：市场低估了全球药企对中国创新资产的刚性需求，而非地缘风险",
    "digest": "[wechat_article.md]\n# JPM：市场低估了全球药企对中国创新资产的刚性需求，而非地缘风险\n\n投资决策者过去半年最纠结的问题，莫过于中国生物医药资产是否已被地缘政治风险“污染”。美国国会信函、FDA对中国临床数据的审查信号、药明康德被列入1260H清单——每一则新闻都足以让交易员本能地调低中国创新药的估值权重。\n\n但JPM在6月11日发布的一份研报中，给出了一个与市场情绪相反的核心判断：**全球大型药企对中国创新资产的结构性需求，其影响力远超美国政策噪音**。这份报告并非来自JPM的中国团队，而是由其美国制药/生物技术分析师团队在ASCO和ADA会议后，面向全球投资者进行的专题电话会纪要。美国分析师们从全球创新流动、并购纪律、临床数据价值三个维度，系统性地论证了一个结论：真正决定中国生物医药资产价格的，不是华盛顿的政治信号，而是波士顿、新泽西和旧金山的研发管线缺口。\n\n这不是一份“中国资产看多”的宣传稿。它的价值在于，给出了美国产业界如何看待中国创新的第一手视角——这些分析师每天与大型药企管理层对话，他们的判断直接反映了资本配置的真实逻辑。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 美国政策风险是“噪音”，而非结构性障碍\n\nJPM美国分析师团队对政策风险的定性，值得每一个关注中国医药资产的投资者仔细咀嚼。他们明确区分了“影响投资者情绪”和“改变全球药物开发轨迹”两个层次，并认为政策因素属于前者，而非后者。\n\n具体而言，美国分析师指出，美国国会信函要求FDA限制中国临床数据使用，以及药明康德被列入1260H清单，更多是“政治信号”而非“可执行的壁垒”。在电话会上，他们反复使用了一个词：noise。这不是轻描淡写，而是基于对产业逻辑的深刻理解。\n\n关键在于，全球创新药研发的底层逻辑没有改变：科学在哪里，创新就流向哪里。如果中国科学家和\n\n[... middle omitted ...]\n\n的完整逻辑链条，并持续跟踪后续的全球临床数据更新和交易动态。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国创新药出海逻辑没变\n\n科学为王，创新不被卡\n\n全球化才是真正的护城河\n\n某外资投行刚开完一场医药分析师电话会，聊了ASCO、ADA和2026下半年展望。核心判断：中国创新药的全球需求逻辑没有变，政策噪音是情绪层面的，不是结构性的。\n\n1️⃣ 政策噪音≠实质壁垒\n美国对中国临床数据、药明系的审查，更多是政治信号，而非可执行的壁垒。分析师共识是：创新会流向“科学所在的地方”，交易结构可能会变，但中国药企在全球研发中的角色不会被动摇。对于药明系的客户，大药企会继续找“China+1”的替代方案。\n\n2️⃣ M&A和license-out：交易更多，但估值更精\n调查显示60%+投资者认为今年并购会比去年多。大药企弹药充足，重点在肿瘤、免疫、心血管代谢和神经科学。但买方越来越精明——如果有一个比西方资产晚6个月但同样优秀的中国资产，他们不愿意为西方资产支付高溢价。这意味着：中国药企的license-out仍可变现，但对方会在估值和风险分担上更严格。\n\n3️⃣ PD-1/VEGF：太重要，不会被卡\n以康方生物的依沃西单抗为例，分析师认为这类IO资产临床价值太大，监管方如果仅因数据来自中国就阻止美国患者使用，会面临巨大\n\n[... middle omitted ...]\n\nexpected to navigate geopolitical considerations. Against this backdrop, M&A and out-licensing activity is likely to remain active but increasingly disciplined, with large pharma favoring to o\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 11 Jun 2026 02:05 AM HKT\n\nDisseminated 11 Jun 2026 02:07 AM HKT"
  },
  {
    "id": "R008",
    "title": "JPM：全球电动车市场的真正分歧不在渗透率，而在区域利润结构",
    "digest": "[wechat_article.md]\n# JPM：全球电动车市场的真正分歧不在渗透率，而在区域利润结构\n\n五月的全球电动车销量数据，读起来像一份分裂的诊断报告。欧洲五国EV+PHEV渗透率同比跳升8个百分点至32%，中国乘用车市场整体萎缩22%但新能源渗透率却逆势突破63%，而美国市场仍在原地踏步，渗透率甚至同比下滑至7%。这三条曲线放在一起，最容易被忽略的判断是：全球电动车投资的主题正在从“总量增长”切换到“区域利润结构”的重构。\n\nJPM这份五月全球电动车与电池月度更新，提供了几个值得产业决策者重新审视的信号。中国新能源车渗透率突破60%之后，整车销量总量下滑反而成为结构性利好——它意味着车企的盈利驱动因素正在从国内规模转向海外溢价和新能源车占比。欧洲的补贴政策和廉价车型正在真实地拉动渗透率，而美国市场的持续疲软则暗示着消费者选择不足和OEM撤退的负反馈循环。与此同时，储能系统作为整份报告中最明确的亮点，正在成为电池产业链中定价权最集中的环节。\n\n以下是我们从这份报告中提炼出的四个关键洞察，以及一个报告尚未完全回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 中国新能源车渗透率突破60%后，总量下滑反而成为盈利结构优化的催化剂\n\n五月中国新能源乘用车零售销量为95万辆，同比下滑7%，但渗透率却达到63%，同比提升10个百分点。这个数字放在全球背景下来看，意义不亚于欧洲的复苏。JPM的中国汽车团队已经将2026年国内乘用车零售预测从此前的同比下滑4%大幅下调至下滑15%，但报告明确指出：“新能源车占比和海外敞口正在成为比行业总量增长更重要的盈利驱动因素。”\n\n这意味着什么？当渗透率超过60%，新能源车已经不再是“增量市场”中的增长故事，而是“存量市场”中的结构性替代。对于比亚迪和吉利这样的头部OEM，国内销量的绝对数字增长不再是估值锚\n\n[... middle omitted ...]\n\n微信群里继续讨论，我们会在后续的月度更新中持续追踪这些变量。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n欧洲电动车分化，储能才是真亮点\n\n全球电动车渗透率持续分化\n\n5月数据出来了，欧盟五国继续高歌猛进，电动车渗透率达到32%，同比+8个百分点。法国表现最猛（+13ppt），意大利、德国也有明显提升。背后是各国补贴政策和平价车型在推进。\n\n中国这边，虽然整体乘用车销量下滑，但新能源车渗透率反而突破63%，同比+10个百分点。纯电和插混都在涨，说明消费者认这个方向。\n\n美国就有点惨，渗透率只有7%，同比还掉了2个百分点。车企在砍新车型、收缩营销，消费者选择变少了。\n\n储能是真正的亮点\n\n全球储能需求正在加速，4M26出货量同比翻倍以上。国内需求+非美地区出口双轮驱动。美国市场则转向韩国和日本电池厂，因为OBBBA规则还在执行。\n\nAIDC（AI数据中心）储能正在成为新变量。西门子和NVIDIA、Fluence合作开发架构，Fluence已经和两家超大规模云厂商签了供货协议。虽然安装看起来慢，但储能本来就在数据中心建设后期才进场，大型项目还在早期施工阶段。\n\n中国车企出海逻辑变了\n\n不再是简单的“便宜电动车”故事，而是有了完整产品矩阵、品牌梯队和技术牌。中国品牌在欧洲新能源车市占率已经18%，同比翻了三倍。本地化生\n\n[... middle omitted ...]\n\ne: France (+13%pts), followed by Italy (+9%pts), Germany (+8%pts), UK (+7%pts), Spain (+4%pts), supported by country-level subsidy schemes and affordable mass EVs penetrating the market. This \n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 11 Jun 2026 05:50 PM HKT\n\nDisseminated 11 Jun 2026 05:50 PM HKT"
  },
  {
    "id": "R009",
    "title": "美国银行：欧元弱势远未结束，市场低估了技术面与基本面的共振",
    "digest": "[wechat_article.md]\n# 美国银行：欧元弱势远未结束，市场低估了技术面与基本面的共振\n\n这份报告的核心判断并不复杂，但它的分量在于时机。美国银行在5月20日通过一个1.15-1.13的看跌价差组合建立了欧元空头头寸，并在6月8日欧元测试1.15心理关口后，明确表示将继续持有空头进入夏季。这不是一个战术性的短线交易，而是一个基于结构性逻辑的持仓决策。\n\n在多数市场参与者仍在猜测欧元何时触底、中东停火协议能否带来反转的时候，美国银行提供的分析框架给出了一个更清晰的判断：欧元当前面临的不是单一风险，而是技术面破位、基本面背离和历史模式重复三重压力的叠加。这三者单独看都不足以构成决定性信号，但合在一起，指向的是一轮可能被低估的美元上行周期。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 技术面已经给出了明确的破位信号，反弹是卖出机会而非反转起点\n\n美国银行的技术分析师指出了三个关键的图表信号。第一个是欧元在6月5日美国非农数据公布后跌破了上升趋势线支撑，这是自4月以来的最低水平。第二个信号更加值得关注——周线图上，欧元正在构建一个头肩顶形态的右肩，颈线支撑位在1.1411-1.1392区间。一旦这个区间被有效跌破，头肩顶形态确认，下行目标将指向1.11甚至200周移动均线附近的1.0980。\n\n第三个信号来自美元指数。美国银行的分析师发现，美元指数在特朗普第二任期的走势与第一任期高度相似。2016-2018年的模式是：大选后美元突破多年区间上涨约6.4%，随后形成头肩顶并在2017年下跌，2018年一季度触底，4月底突破后继续上涨约6.6%至8月。2024-2026年的走势几乎在重复这一路径。如果这个类比继续成立，美元指数在当前底部确认突破后，可能在未来几个月向103-105区间上行。\n\n对于读者而言，这意味着什么？欧元当前1.15附近的反弹\n\n[... middle omitted ...]\n\n情景分析，以及美元指数2016-2018类比的最新验证信号。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n欧元，夏天还要跌👇\n\n**封面短标题：欧元空头持续**\n**封面副标题：技术面+基本面，双重压制**\n\n最近投行研报的结论很直接：欧元这波反弹，不是反转。\n\n**1. 技术面：反弹是用来卖的**\n- 上周非农数据后，欧元跌破了上升趋势线支撑。\n- 6月8日测试1.15心理关口后反弹，但上方1.1576-1.16区域是新的阻力位。\n- 更关键的是，周线图正在形成头肩顶形态，颈线在1.1411-1.1392。一旦跌破，下方空间打开到1.11甚至1.0980。\n\n**2. 历史规律：美元在重复2018年剧本**\n- 美元指数走势与2016-2018年惊人相似。2018年美元在二季度触底后，下半年涨了6.6%。\n- 现在DXY在100.51附近尝试筑底，如果收盘站上，可能开启新一轮上行周期。\n- 如果这个规律继续，欧元下半年大概率承压。\n\n**3. 基本面：美欧增长差被低估**\n- 美国经济数据持续超预期，就业市场韧性很强。\n- 市场对美联储加息的定价还不够充分，而欧洲的加息反而可能因经济疲弱而难以持续。\n- 中东局势虽带来能源价格波动，但整体上对欧元区是负面压力（贸易条件恶化）。\n\n**总结一下**：技术面破位+历\n\n[... middle omitted ...]\n\n47%). We remain short. See report: Six reasons to short euro 20 May 2026\n\n## Technicals: Euro broke support, bias is to fade bounces\n\nOne immediate market response to the latest US payrolls re\n\n[... middle omitted ...]\n\nw in accordance with firm policies.\n\nNeither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information."
  },
  {
    "id": "R010",
    "title": "JPM：中国通胀的真正信号不是PPI回升，而是AI定价权开始向消费端传导",
    "digest": "[wechat_article.md]\n# JPM：中国通胀的真正信号不是PPI回升，而是AI定价权开始向消费端传导\n\n中国5月通胀数据公布后，市场目光大多停留在PPI同比3.9%的温和超预期上。但这份JPM研报传递的核心判断，远比一个数字深刻：中国正在经历一场由产业升级和AI需求驱动的结构性定价重估，而这股力量正在从工业端向消费端扩散。市场如果只看到“通胀温和、需求疲软”的旧叙事，就会错过供给端正在发生的根本性变化。\n\n这份报告的价值不在于确认通胀符合预期，而在于揭示了一个正在成型的传导链条——AI驱动的半导体和电子元器件涨价，已经从上游的封装测试、存储设备，蔓延到下游的通讯工具、平板电脑等消费电子终端价格。这不再是短暂的成本冲击，而是与全球科技上行周期和中国“AI+”战略深度耦合的持久性通胀尾风。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 食品通缩掩盖了非食品价格的韧性，核心通胀的“假疲软”需要重新审视\n\n5月CPI同比1.2%，略低于市场预期的1.3%，表面看延续了温和态势。但拆解结构后会发现，拖累主要来自食品端——鲜菜和猪肉价格继续下行，食品CPI同比降至-1.7%。这恰恰是数据中最具误导性的部分。\n\n非食品CPI同比已升至1.9%，环比仍录得0.2%的正增长。其中交通运输和通信类价格环比上涨0.2%，虽然较前两个月月均2.0%的环比增速有所放缓，但通信工具价格环比跳升1.5%（经季调后JPM估算为1.8%），统计局明确提及手机和平板电脑分别上涨1.6%和1.1%。背后驱动因素正是AI相关存储芯片的紧张正在向终端传导。\n\n更值得关注的是核心CPI——剔除食品和能源后，同比虽回落至1.1%，但环比持平。这个“平”字背后，是服务业CPI同比放缓至0.8%的隐忧。但JPM的分析暗示，核心CPI的疲软更多反映的是消费信心不足和收入预期偏弱，而非通缩\n\n[... middle omitted ...]\n\n助你建立自己的通胀跟踪框架，在变化中找到结构性的机会与风险。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nCPI温和，PPI强势，AI是隐藏主线\n\n📊 5月通胀拆解\n\n5月通胀数据基本符合预期，核心看点是：\nCPI继续偏弱，PPI延续涨势但节奏放缓。\n\n1️⃣ CPI：食品拖累，AI悄悄推高手机价格\n- 整体CPI同比+1.2%，环比仅微涨0.1%\n- 食品持续通缩：鲜菜、猪肉拖累\n- 交通通信环比+0.2%，但汽车和燃料在跌\n- **手机平板涨了1.6%**，AI带动存储芯片涨价传导至终端\n- 黄金饰品虽环比跌0.2%，但同比仍+9.9%，贡献0.3个百分点\n- 核心CPI（剔除食品能源）同比回落至1.1%\n\n2️⃣ PPI：工业升级+AI需求是主推手\n- PPI同比+3.9%，环比+0.8%（上月+1.7%）\n- 锡冶炼+4.8%、铜冶炼+3.1%\n- **芯片封装测试+2.9%，存储设备+1.9%**——AI算力需求持续扩散\n- 夏季用电高峰支撑煤电价格\n- 但全球油价波动压制上游，消费类PPI仍处通缩（-0.8%）\n\n3️⃣ AI通胀传导正在扩大\n从云厂商资本开支到上游半导体，再到下游电子终端，AI相关的成本推动比预期更持久。中国工业升级+AI+战略是多年级蓝图，不是短期脉冲。\n\n4️⃣ 后续怎么看？\n-\n\n[... middle omitted ...]\n\n excess capacity and weak demand limit pass-through, leaving CPI benign. GDP deflator may turn positive in 2Q.\n\nChina's May inflation was broadly in line with expectations. The PPI sequential \n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 10 Jun 2026 12:44 PM HKT\n\nDisseminated 10 Jun 2026 01:03 PM HKT"
  },
  {
    "id": "R011",
    "title": "JPM：市场真正低估的不是通胀读数，而是AI成本传导正在重塑中国的价格结构",
    "digest": "[wechat_article.md]\n# JPM：市场真正低估的不是通胀读数，而是AI成本传导正在重塑中国的价格结构\n\n中国5月通胀数据“大致符合预期”——这是JPM最新研报的开场判断。CPI同比1.2%，PPI同比3.9%，与市场共识几乎一致。如果只看这个表面数字，你可能会认为这是一份平淡无奇的月度数据更新。\n\n但这份报告真正值得关注的，不是数字本身，而是数字背后的结构性变化。JPM在看似温和的通胀读数中，捕捉到了一个正在加速的趋势：**AI驱动的成本传导已经从半导体上游蔓延到消费电子终端，并在中国的工业升级周期中找到了独特的放大机制。**\n\n这不是一次性的价格脉冲。这是中国价格体系正在经历的一次供给侧再定价。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. PPI上行中隐藏着一个比能源冲击更持久的驱动力：AI成本传导正在拓宽\n\n5月PPI环比上涨0.8%（季调后），同比加速至3.9%。乍看之下，这似乎延续了过去两个月由能源价格和季节性需求推动的上行趋势。但JPM的分析揭示了一个更重要的细节：推动PPI上行的力量正在切换。\n\n报告明确指出，本月的价格支撑来自“工业升级和AI驱动的计算需求”，具体体现在金属、电气机械和电子设备价格上。国家统计局重点提及了锡冶炼环比上涨4.8%、铜冶炼上涨3.1%，以及集成电路封装测试和外部存储设备分别上涨2.9%和1.9%。\n\n这些数据点共同指向一个判断：**AI相关的内存紧张正在从数据中心建设端向消费电子终端传导。** 手机和平板电脑价格环比上涨1.6%和1.1%，通信工具价格环比跳升1.5%（JPM估算季调后为1.8%），这是AI成本传导进入终端消费品的明确信号。\n\n与能源冲击不同——中东局势缓和后油价可能回落——AI驱动的通胀脉冲“可能更具持久性”。全球科技上行周期仍然完整，而中国的工业升级和AI+战略是多年规划\n\n[... middle omitted ...]\n\n报的完整解读和原始图表，并围绕这些未解问题展开更深入的交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月通胀：AI涨价在扩散\n\n**AI通胀扩散中**\n\n**PPI继续上行，CPI仍温和**\n\n5月通胀数据基本符合预期。PPI延续回升，但速度放缓；CPI依然偏软。\n\n1/ **PPI：工业升级+AI需求是主要推手**\n- 有色金属（锡冶炼+4.8%、铜冶炼+3.1%）、电气机械和电子设备涨价明显\n- 统计局特别提到：集成电路封装测试涨2.9%，外部存储设备涨1.9%\n- 夏季用电高峰也推高了煤炭、制冷设备价格\n- 全球油价波动限制了涨幅上限\n\n2/ **AI相关涨价正在扩散**\n- 从数据中心建设→上游半导体→下游电子产品，成本传导链条在拉长\n- 手机平板涨价1.6%/1.1%，通信工具环比涨1.8%\n- 研报判断：这个通胀推动力可能比能源冲击更持久\n\n3/ **CPI：食品通缩抵消了其他涨幅**\n- 核心CPI同比1.1%，环比持平\n- 交通通信受汽车降价拖累，但通信工具因AI内存涨价而跳升\n- 服务CPI放缓至0.8%\n- 食品仍是主要拖累，鲜菜猪肉持续下滑\n\n4/ **后续怎么看**\n- PPI仍有上行风险，但产能过剩+需求疲软限制传导\n- GDP平减指数有望在二季度转正，结束三年通缩\n- 核心CPI\n\n[... middle omitted ...]\n\n excess capacity and weak demand limit pass-through, leaving CPI benign. GDP deflator may turn positive in 2Q.\n\nChina's May inflation was broadly in line with expectations. The PPI sequential \n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 10 Jun 2026 12:44 PM HKT\n\nDisseminated 10 Jun 2026 01:03 PM HKT"
  },
  {
    "id": "R012",
    "title": "Bernstein：AI模型商品化进程比市场想象的更快，竞争格局正从智能竞赛转向成本与信任竞赛",
    "digest": "[wechat_article.md]\n# Bernstein：AI模型商品化进程比市场想象的更快，竞争格局正从智能竞赛转向成本与信任竞赛\n\n过去一周，AI行业发生了三件看似独立、实则指向同一方向的事件：Anthropic的Claude Fable 5定价高到让开发者开始理性配给token用量；OpenAI被报道正在降价以争夺市场份额；腾讯、微软等大型AI用户开始重新审视“token最大化”策略的经济性。这些信号叠加在一起，指向一个Bernstein在最新研报中明确提出的判断：AI模型的商品化进程，正在被人类用户的感知边界加速，而非由底层模型智能的收敛速度决定。\n\n这份由Bernstein全球互联网团队发布的报告，提供了一套全新的分析框架——不是从模型能力本身出发，而是从“什么情况下人类用户认为AI已经足够好”这一视角，重新定义AI市场的竞争逻辑。报告的核心主张是：一旦某个垂直场景的AI任务完成质量达到“可靠可用”的阈值，竞争的决定性因素将从推理能力转向成本、可用性和开发者信任。这将对全球AI实验室的商业模式、中国AI厂商的市场空间、以及投资者评估AI资产的方式产生深远影响。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI商品化的真正驱动力不是技术收敛，而是人类用户的“够用”感知\n\nBernstein报告提出的核心框架，与市场上主流讨论的“模型智能趋同”理论有本质区别。当前流行的观点认为，随着模型能力提升，不同AI模型之间的智力差距会逐渐缩小，最终导致商品化。但Bernstein认为，这种技术收敛的假设既无法验证，也不重要。\n\n真正驱动商品化的，是人类用户在不同使用场景中对AI表现的主观感知。当一个AI系统能够可靠地完成特定任务——比如订奶茶、预订酒店、生成营销文案——用户就不再关心底层的模型架构是否与前沿模型一致，而只关心它是否好用、便宜、稳定。\n\n[... middle omitted ...]\n\n者一起，追踪AI竞争格局的演变，拆解头部公司的真实估值逻辑。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI模型会变成“白菜价”吗？\n\nAI模型正在“够用化”\n\n最近投行研报抛出一个新观点：AI模型的竞争，未来可能不是比谁更聪明，而是比谁更“够用”、更便宜。\n\n核心逻辑是这样的👇\n\n1/ 用户感知决定“够用”标准\n模型智商是否趋同不重要，重要的是人觉得它“够用了”。\n比如订奶茶、订酒店这类消费场景，很快就会被AI解决；而写代码、做Excel这种企业级任务，还需要更久；至于前沿科学（国防、医疗、核聚变），可能永远需要最顶尖的模型。\n\n2/ 一旦“够用”，竞争焦点就变了\n当某个场景被AI搞定后，胜负手就从推理能力切换成：价格、可靠性、开发者信任。\n这意味着，中国开源模型的机会来了——以更低价格提供“够用”的推理能力。研报估算，即使考虑地缘政治限制，中国AI实验室也能拿下全球AI市场35-40%的份额。\n\n3/ 研发投入的“拐点”逻辑\n当一个任务被“解决”，继续砸钱做研发的边际回报骤降。\n长期看，值得花指数级成本去攻克的任务会越来越少，模型训练总成本增速放缓，AI实验室反而更容易实现盈利。\n\n4/ 市场会分两层\n一层是美国前沿实验室服务高端、小众、高付费意愿客户；另一层是中国和开源模型服务日常消费和企业场景，靠价格和\n\n[... middle omitted ...]\n\ne3a.jpg)  \nMin-Joo Kang\n\n+852 2123 2644\n\nminjoo.kang@bernsteinsg.com\n\n![](images/fbec7ebd0eb3cc6127d0fce606f347a29dbb5f76fa11f08608cb895040d35b3d.jpg)  \nHyrum Caesar\n\n+81 3 6777 6979\n\nhyrum.ca\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R013",
    "title": "GS：铝市场真正超预期的不是中国产量，而是海外供给的加速释放",
    "digest": "[wechat_article.md]\n# GS：铝市场真正超预期的不是中国产量，而是海外供给的加速释放\n\n全球铝市场正在经历一个被多数投资者低估的结构性变化。多数市场参与者仍在争论中国4500万吨产能红线能否守住，但GS最新一场专家电话会揭示了一个更关键的信号：海外铝冶炼产能的扩张速度正在显著加快，其体量和节奏远超此前的市场预期。\n\n这份报告的核心判断是：未来三年全球铝市场面临的主要矛盾，将从“中国供给约束”转向“海外产能加速释放”。印尼和中亚正在成为中国铝企海外扩张的核心战场，2026年至2028年间，仅这两个地区的铝产能增量就可能达到近600万吨。这一数字意味着什么？它相当于全球铝市场规模的5%以上，足以改写未来几年的供需平衡表。\n\n为什么这个判断现在重要？因为市场对铝的定价逻辑仍停留在“中国减产-供给偏紧”的旧框架中。但GS专家在实地调研后的结论是：中国产量已持续超过4500万吨，而海外产能的扩张正在形成新的供给曲线。如果投资者只盯着中国的环保督察和产能置换，可能会错过更大的结构性变量。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 印尼正在成为全球铝供给的新变量，产能释放节奏远超年初预期\n\nGS专家在近期访问印尼后指出，印尼铝冶炼产能的扩张条件正在显著改善。最核心的变化是电力瓶颈的解除。在青山工业园，部分暂停的镍冶炼产能被重新调配给铝冶炼使用，释放了大量电力资源。与此同时，当地电厂建设的进度好于预期，包括710MW超临界火电机组的顺利出口，都为铝冶炼提供了稳定的能源保障。\n\n基于实地调研，专家将印尼2026年的铝产能增量预期从年初的142万吨大幅上调至215万吨，2027年进一步上调至197.5万吨。这意味着仅印尼一地，两年内的产能增量就将超过400万吨。更重要的是，这些项目的投产节奏将从2026年四季度开始明显加速。\n\n具体来看，几个关键项\n\n[... middle omitted ...]\n\n变化的读者，完整报告中的图表和敏感性分析提供了更细致的视角。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n铝的产能扩张，正在加速\n\n产能扩张加速\n\n中国企业在海外的产能扩张明显提速\n\n最近某外资投行组织了一场铝冶炼行业的专家电话会。专家刚从印尼和哈萨克斯坦实地调研回来，分享了几个关键变化：\n\n**1/ 印尼：电力瓶颈缓解，产能加速落地**\n过去制约印尼铝产能的电力问题正在消退。青山工业园把部分暂停的镍冶炼电力转给了铝厂，加上当地电厂建设进展顺利，产能释放节奏明显加快。\n专家预计2026-2027年印尼新增产能约4.1百万吨，比3月的预测高出1.6百万吨。其中约70%来自镍冶炼电力转移。\n\n**2/ 中亚：中国企业在哈萨克斯坦布局**\n哈萨克斯坦规划了2个项目，总产能5.4百万吨。第一期约1.8百万吨预计2028年投产，相当于全球市场的2.4%。\n\n**3/ 中国：产量持续超限**\n今年1-4月中国原铝产量年化已达47.1百万吨，超过45百万吨的“天花板”。专家估计有1.0-1.2百万吨来自违规超产和未按期淘汰的旧产能。\n近期环保检查属于常规安排，并非针对铝行业。专家预测2026年中国原铝产量45.5百万吨，同比增1百万吨。\n\n**4/ 出口订单回暖**\n4-5月以来，未锻轧铝、铝合金、铝板带等产品出口订单明显回升\n\n[... middle omitted ...]\n\nproducers in ex-China, driven by projects in Indonesia and Central Asia. Overproduction in Chinese primary aluminium, beyond the 45mnt, would also persist in the current environment. The speak\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R014",
    "title": "摩根斯坦利：中国原油进口的骤降并非需求崩塌，而是库存周期的主动调节",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：中国原油进口的骤降并非需求崩塌，而是库存周期的主动调节\n\n当全球市场都在关注霍尔木兹海峡的供应冲击时，一个关键变量正在被误读。中国在3月至5月期间，将原油进口量从2月的约12.8百万桶/日骤降至5月的约7.8百万桶/日，降幅接近500万桶/日。这一数字足以让任何大宗商品分析师警觉：全球最大的原油进口国是否正在经历需求端的断崖式下跌？\n\n摩根斯坦利在最新发布的《石油数据摘要：欧洲》专题报告中，给出了一个反直觉但逻辑严密的判断。该机构大宗商品策略师Charlotte Firkins与Martijn Rats通过拆解中国的原油贸易、炼厂运行以及终端需求数据，揭示了一个被市场普遍忽略的事实：中国进口的锐减，并非因为经济突然失速或需求崩溃，而是在一个持续了数月的库存过剩周期中，主动进行的调节性收缩。\n\n这份报告的价值不在于它告诉市场中国需求在下降——这已经是共识——而在于它精确地刻画了下降的性质、结构以及背后的驱动力。对于试图理解全球油市再平衡路径的投资者而言，这组数据提供了远比“需求疲软”四个字更丰富的分析框架。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 进口暴跌与库存反增的悖论，指向的是此前的过度进口而非当前的需求坍塌\n\n市场最容易犯的错误，是将进口量的变化直接等同于消费量的变化。摩根斯坦利的数据清晰地展示了这一逻辑陷阱。5月中国原油进口降至约7.8百万桶/日，同比下降3.2百万桶/日，较2月危机前水平更是低了近500万桶/日。单看这个数字，很容易得出“中国需求大幅萎缩”的结论。\n\n但报告提供了一个关键的反证：根据Vortexa的可观测原油库存数据，中国的商业和战略原油库存在3月和4月竟然还在持续累积，平均建库速度约为1.1百万桶/日。直到5月，库存才开始转为去化，平均速度约为75万桶/日。\n\n进口\n\n[... middle omitted ...]\n\n交流，帮助订阅者在信息过载的市场中，建立属于自己的分析框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国原油进口大降，但没那么简单\n\n📌 进口骤降≠需求崩塌\n\n某外资投行最新研报拆解了中国3-5月的原油数据，发现一个反直觉的现象：进口暴跌但库存却先涨后跌。\n\n1️⃣ 进口大降的真相\n- 5月原油进口仅780万桶/天，同比降320万桶/天\n- 比冲突前2月少了近500万桶/天\n- 但这不是需求崩溃，而是中国在冲突前过度进口，库存本来就很满\n- 2月时，中国原油超采约270万桶/天\n\n2️⃣ 库存数据怎么说\n- 3-4月库存还在小幅增加（约110万桶/天）\n- 5月才转为去库存（约75万桶/天）\n- 数据方向一致：进口下降是建立在前期库存过剩基础上\n\n3️⃣ 需求到底弱在哪\n- 4月表观需求同比降120万桶/天（-8%）\n- 主要拖累来自LPG和燃料油，占降幅70%\n- 柴油和汽油相对有韧性，但新能源车正在侵蚀汽油需求\n- 4月汽油零售价涨了30美元/桶，已经触发了消费者敏感阈值\n\n4️⃣ 炼厂在干嘛\n- 国企炼厂大幅减产，4月加工量比2月降180万桶/天\n- 独立炼厂被要求维持开工，但利润已转负\n- 山东某炼厂零售端销量3-4月比2月降了20%\n\n5️⃣ 新能源的冲击\n- 新能源乘用车渗透率：3月51%→4月\n\n[... middle omitted ...]\n\nmb/d YoY and almost \\~5 mb/d lower than pre-conflict levels in February. However, observable crude inventory data shows China's crude stocks rising over the course of March and April before ev\n\n[... middle omitted ...]\n\narantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n© 2026 MS"
  },
  {
    "id": "R015",
    "title": "GS：CLO套利空间的真正故事不在利差本身，而在资本结构如何重塑定价权",
    "digest": "[wechat_article.md]\n# GS：CLO套利空间的真正故事不在利差本身，而在资本结构如何重塑定价权\n\nCLO（担保贷款凭证）市场正在经历一个被多数投资者低估的结构性转变。传统上，市场参与者衡量CLO股权层吸引力时，习惯于计算新发杠杆贷款利差与CLO债务加权平均成本之间的差值。这个指标直观、易得，但GS最新发布的研报指出，它遗漏了一个关键维度：交易层面的实际超额利差。\n\nGS使用Intex的交易级和分层级数据，构建了一套“交易匹配套利利差”指标，覆盖美元和欧元CLO。结论清晰且反直觉：美元CLO套利空间并非只是周期性波动，而是出现了更显著的趋势性收窄。这背后，一个重要的结构性驱动力是“自有股权资本”的崛起。这种资本改变了CLO股权投资者的行为模式，使得市场对即期套利条件的敏感度下降。对于决策者而言，理解这一变化，远比盯着利差数字本身更重要。\n\n这份报告的价值不仅在于提出了一个更精确的测量工具，更在于它揭示了CLO市场定价权的转移——从依赖市场波动获取超额收益，转向依赖规模、品牌和持续部署能力。以下是我们从报告中提炼出的四个核心洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 美元CLO套利空间的结构性收窄，根源在于“自有股权资本”改变了行为逻辑\n\nGS构建的交易匹配套利指标显示，美元CLO套利空间在过去两年收窄幅度远超传统指标所反映的程度。传统指标可能显示利差在某个区间波动，但新指标清晰地画出了一条向下的趋势线。报告认为，这并非简单的周期性现象，而是一个结构性的变化。\n\n驱动这一变化的关键变量是“自有股权资本”的增长。这类资本通常承诺跨年份部署，并将管理权和投资决策权交给发起机构。它们追求的不是单笔交易的最大化入场利差，而是连续部署和年份分散化。这意味着，即使即期套利空间收窄，这些资本也不会轻易退场。这实际上降低了股权需求对利差变化的\n\n[... middle omitted ...]\n\n在社群中分享报告的PDF原文，并就上述未解问题展开专题讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nCLO套利空间正在收窄\n\n套利空间被谁吃掉了？\n\n某外资投行最新研报，用“交易匹配”方法重新测算了CLO套利空间（资产端收益-负债端成本），发现几个有意思的现象👇\n\n**1/ 美元CLO套利空间在结构性压缩**\n传统算法只算新发贷款与负债成本之差，但实际交易中，利差比传统指标更紧。原因：市场成熟+更多经理人涌入，竞争推高了资产价格、压低了收益空间。\n\n**2/ 重置交易≠更好回报**\n很多人以为重置（reset）能降低负债成本、改善套利。但研报发现：2023年以来，美元市场资产端利差压缩速度常常超过负债端改善，重置后净套利改善有限。欧元市场情况稍好，因资产端压缩没那么激进。\n\n**3/ 高评级经理≠低套利空间**\n在美元市场，高评级经理反而能维持更宽的套利空间；欧元市场则相反，低评级经理套利更宽。原因：美元市场经理分化主要体现在负债端，欧元更多在资产端。\n\n**4/ 欧元套利看似便宜，但非“免费午餐”**\n欧元CLO套利空间确实比美元宽，但区域基本面偏弱（违约率上升、政策环境不友好），这部分“超额利差”可能只是对信用损失的补偿。\n\n**5/ 核心变量：自有资金池**\n研报认为，美元市场套利收窄的一个重要推手是\n\n[... middle omitted ...]\n\narbitrage measure for USD and EUR CLOs. While it broadly tracks traditional measures, it also shows a more pronounced secular tightening in USD broadly syndicated loan CLO arbitrage as the mar\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R016",
    "title": "GS：市场低估的不是地缘冲突的烈度，而是需求破坏的持久性",
    "digest": "[wechat_article.md]\n# GS：市场低估的不是地缘冲突的烈度，而是需求破坏的持久性\n\n当霍尔木兹海峡的通行量降至战前水平的不足10%，布伦特原油价格却从三月末的高点回落了约25%。这一看似矛盾的价格走势，正在挑战一个根深蒂固的市场直觉：地缘供给中断必然导致油价飙升。GS最新发布的这份研报提供了一个关键判断——市场真正需要重新定价的，不是冲突升级的风险溢价，而是在供给冲击持续期间，需求端正在发生的结构性坍塌。这份报告的核心主张是，一个更持久的霍尔木兹中断，已被一个更小的供需赤字所抵消，而后者主要源于需求破坏的规模远超预期。\n\n这份研报维持了对2026年第四季度布伦特原油每桶90美元的预测。维持预测本身并不惊人，真正值得关注的是维持预测的理由发生了根本性置换：此前市场担忧的是供给中断的持续时间，而GS现在指出，一个更小的赤字（5-6百万桶/日）抵消了一个更长的中断（恢复时间从六月底推迟至八月底）。这意味着，油价的地板不再由供给侧的物理瓶颈决定，而是由需求端的脆弱性重新锚定。\n\n对于产业决策者和资产配置者而言，理解这种定价逻辑的转移，比预测下一个地缘事件更为紧迫。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮供给冲击的真实赤字仅为生产损失的约三分之一\n\nGS估算，中东液体燃料生产在二季度受到的冲击高达14-15百万桶/日。然而，全球石油市场同期出现的供需赤字仅为5-6百万桶/日。两者之间近9百万桶/日的差距，揭示了市场缓冲机制的深度。\n\n这一差距由三个因素构成。首先，战前市场本就存在约3百万桶/日的供给过剩。其次，中东以外地区的供给在冲突期间反而上调了约1.5百万桶/日，主要来自美洲（美国、巴西、圭亚那、委内瑞拉）的增产。但最大的变量，是需求侧。GS估算，全球石油需求因冲突而损失的规模接近5百万桶/日。这意味着，供给中断的冲击，有超过\n\n[... middle omitted ...]\n\n会有对这份研报更完整的解读，以及围绕核心假设的持续跟踪讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n原油供需博弈：需求疲软对冲供应中断\n\n封面：供需拉锯战\n副标题：需求疲软如何抵消供应冲击\n\n最近原油市场很有意思，一边是霍尔木兹海峡的供应中断还在持续，另一边油价却从3月高点跌了约25%。原因其实很直白：需求塌得比预期更快。\n\n**1/ 供需缺口比想象中小**\n虽然中东产量每天少掉14-15百万桶，但实际全球缺口只有5-6百万桶/天。原因有三：\n- 需求损失约5百万桶/天（中国进口量同比降了近4百万桶）\n- 战前就有约3百万桶/天的过剩\n- 非中东地区增产约1.5百万桶/天\n\n**2/ 恢复节奏在变**\n投行研报将海湾国家出口恢复时间从6月底推迟到8月底。但有意思的是，他们认为一旦海峡重新开放，产量恢复速度会比市场预期的快——因为油井的设备和人员其实都在准备复工状态。\n\n**3/ 2027年油价怎么看？**\n研报将2027年均价预测下调5美元至80美元/桶，原因：\n- 阿联酋退出OPEC后增产\n- 美洲（美国、巴西、圭亚那、委内瑞拉）供给增加\n- 中国电动车替代加速，部分需求回不来\n\n**4/ 风险是双向的**\n研报列了几个情景：\n- 中性：2026Q4布伦特90美元\n- 不利：如果10月底才恢复，可能到11\n\n[... middle omitted ...]\n\nich may be achieved with a rise in Hormuz flows to $70 \\%$ of pre-war levels given current redirections.\n\nNudging down 2027 forecast. We lower our 2027 average Brent forecast by \\$5 to \\$80 on\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R017",
    "title": "摩根斯坦利：北美油气高管薪酬设计已传递出比产量更重要的信号",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：北美油气高管薪酬设计已传递出比产量更重要的信号\n\n2026年北美油气公司的委托书（proxy filing）刚刚披露完毕。对于关注这个行业的投资者和决策者来说，这些文件通常被视为例行公事——一堆关于薪酬、治理和投票事项的合规性披露。但摩根斯坦利这份最新研报揭示了一个被市场低估的信号：高管薪酬框架的稳定本身就是一个重要的战略声明。\n\n这份报告的核心判断是：北美油气公司董事会正在通过薪酬设计，不动声色地锁定行业纪律，而不是为下一轮增长周期做准备。如果你还在用产量增长或资本开支计划来衡量这些公司的战略意图，你可能错过了真正重要的结构性变化。\n\n为什么现在需要关注这个信号？过去两年，市场对油气板块的定价逻辑经历了剧烈摇摆。从2022年的暴利到2023-2024年的回归均值，投资者的核心焦虑已经从“这些公司能不能赚钱”转变为“这些公司会不会把钱花掉”。2026年的委托书披露，恰恰提供了检验这一焦虑的窗口——董事会是否真的站在投资者这边。\n\n摩根斯坦利团队分析了覆盖范围内的北美油气公司2026年短期激励（STI）计划，发现了一个值得深思的结论：整体框架几乎没有变化。这种稳定不是惰性，而是一种刻意的选择。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 薪酬框架的稳定揭示了董事会真正的优先级排序\n\n2026年与2025年相比，北美油气公司短期激励指标的加权平均权重变化幅度极小。美国生产商的核心指标——EHS（环境、健康与安全）、现金流、资本效率——权重分别为18%、18%和15%，与上年几乎完全一致。加拿大同行则更侧重EHS（24%）、生产/交付（16%）和运营效率（14%），同样保持稳定。\n\n这种稳定性的含义需要仔细拆解。在一个能源价格波动、能源转型压力持续、投资者对资本纪律高度敏感的行业环境中，董事会选择不调\n\n[... middle omitted ...]\n\n报原始图表、深度解读和行业动态，帮助你建立更系统的分析框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n北美油气高管薪酬：资本纪律仍是主线\n\n资本纪律＞增长扩张\n\n2026年代理投票文件显示，北美油气公司薪酬框架基本没变，董事会仍在强调资本纪律和回报，而非转向增长。\n\n📌 核心发现\n1️⃣ 短期激励（STI）权重稳定\n美国公司最看重：EHS（18%）、现金流（18%）、资本效率（15%）\n加拿大公司更侧重：EHS（24%）、产量/交付（16%）、运营效率（14%）\n\n2️⃣ 长期激励（LTI）占比惊人\nCEO薪酬平均75%来自长期激励\nEQT和PR的CEO薪酬100%为可变/绩效挂钩\n\n3️⃣ 部分公司做了微调\nOXY用FCF替换了CROCE\nEXE新增FCF、移除每千立方英尺资本效率\nCRK用杠杆目标替代运营成本改善\n\n4️⃣ 控制权变更条款\n平均约2.5倍CEO年薪，低于近期卖方中位数\n\n💡 有意思的发现\nCEO薪酬与三年相对股东总回报（TSR）关联度不高，说明股东回报只是薪酬设计的输入之一，公司规模、业务复杂度、激励设计同样重要。\n\n从2019年到2026年，生产/交付类指标权重从18%降至7%，EHS从7%升至19%，资本纪律和运营安全成为新主线。\n\n整体看，北美油气行业薪酬设计仍在传递“纪律优先”的信\n\n[... middle omitted ...]\n\n), and Capital Efficiency (15%).  \nCanadian peers place greater emphasis on EHS (24%), Production/Delivery (16%), and Operating Efficiency (14%).  \nExec comp remains heavily variable and perfo\n\n[... middle omitted ...]\n\n<tr><td>Suncor Energy Inc (SU.TO)</td><td>E (12/16/2024)</td><td>C$85.32</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted."
  },
  {
    "id": "R018",
    "title": "美国银行：市场低估了房地产信用分化中的结构性机会，而非整体复苏",
    "digest": "[wechat_article.md]\n# 美国银行：市场低估了房地产信用分化中的结构性机会，而非整体复苏\n\n这份美国银行最新发布的大中华区房地产研报，表面上呈现的是6月香港一手房成交放缓、高收益债收益率小幅走阔等短期波动信号。但如果把报告中的三个独立模块——香港住宅销售、中央财政支持城市更新、以及信用研究员对个别债券的明确超配建议——放在一起看，真正的核心判断并非“市场在变差”，而是“市场正在从总量博弈转向个券和个票的alpha挖掘”。\n\n报告的真正价值不在于描述了6月的数据有多弱，而在于它指出了一个正在发生的结构性转变：政策子弹的边际效用正在递减，但信用主体的分化正在加速。对于高净值投资者和产业决策者来说，这意味着过去两年“买整个板块”的交易策略正在失效，取而代之的是一种更精细、更依赖主体信用判断的配置逻辑。\n\n以下是我们从这份研报中提炼出的五个关键洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 6月香港一手房成交放缓不是需求坍塌，而是开发商主动的供给节奏调整\n\n报告显示，截至6月，香港一手房成交仅约240宗，而过去五个月的月均成交量超过2000宗。单看这个数字，很容易得出“市场急冻”的结论。但美国银行的分析师将原因归结为三个方面：本地股市下跌带来的负财富效应、对美国加息的重新担忧、以及中国内地新出台的离岸投资规则带来的不确定性。\n\n这里的关键在于，报告明确指出开发商正在“更谨慎地控制推盘节奏”。这不是需求端的全面崩溃，而是供给端在多重不确定性下的主动收缩。从投资角度看，这意味着香港楼市的短期成交量数据可能失真，不能简单线性外推为价格趋势。真正需要关注的是，当开发商重新加速推盘时，市场能否消化——而这取决于上述三个不确定性因素的演变。\n\n报告也坦承，离岸投资规则的不确定性“短期内将持续存在，直到更清晰的实施细则出台”。这是一个尚未落地的核心变\n\n[... middle omitted ...]\n\n产出售的进展？我们会在社群中分享更完整的原始图表和逐段解读。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n香港楼市6月突然降温，新房成交骤降\n\n🏠 6月香港楼市，凉了？\n\n6月新房成交仅约240宗\n对比前5个月月均2000+的水平\n明显掉速了\n\n开发商推盘节奏明显放缓\n背后的三个原因👇\n\n1️⃣ 本地股市走弱，财富效应转负\n2️⃣ 市场重新担忧美国加息\n3️⃣ 内地新出台的离岸投资法规带来不确定性\n\n研报认为，第三个因素短期内还会继续影响市场\n直到具体实施细则更清晰\n\n🏗️ 城市更新：中央拨款来了\n\n国务院政策吹风会透露\n2026年中央预算安排970亿\n另加1600亿超长期特别国债\n用于支持地方城市更新\n\n但对比每年超3万亿的城市更新投资总额\n大头还是地方自己扛\n（专项债+政策性银行贷款）\n\n研报判断：增量影响相对有限\n\n📊 债券市场速览\n\n过去一周，中国高收益地产债收益率\n上行18bp至9.58%\n年初至今仍收窄162bp\n\n香港投资级地产债利差\n收窄3bp至61bp\n\n值得关注的是\n研报对某香港地产公司持偏乐观看法\n理由：\n✅ 债务重组条款仍有不错空间\n✅ 利息覆盖约1倍，资产出售持续推进去杠杆\n✅ 公司主动卖资产，解决债务问题的态度明确\n\n后续关注：\n建行大楼出售完成情况\n债务重组谈判进展\n更多资产出售\n\n[... middle omitted ...]\n\nch)\n\n## Central govt' financing subsidy to aid urban renewal\n\nAt a policy briefing held by the State Council, the Vice Minister stated that RMB 97bn from the central budget and RMB 160bn ultra\n\n[... middle omitted ...]\n\nw in accordance with firm policies.\n\nNeither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information."
  },
  {
    "id": "R019",
    "title": "BARC：校园网络市场正在回归正常增长，真正的竞争焦点是份额再分配",
    "digest": "[wechat_article.md]\n# BARC：校园网络市场正在回归正常增长，真正的竞争焦点是份额再分配\n\n市场已经消化了疫情后混合办公带来的网络设备需求爆发，也消化了2024年的库存修正。但BARC这份最新发布的校园网络模型更新报告揭示了一个更值得关注的信号：未来两年市场增速将温和回落至7%-8%，而真正拉开公司间估值差距的，不再是行业贝塔，而是结构性份额迁移。\n\n这份报告的核心判断可以简化为一句：校园网络市场正在从“周期修复”转向“常态增长”，而在这个阶段，赢家不是靠市场涨潮，而是靠从竞争对手手中夺取份额。\n\n对于关注Arista Networks、Cisco、HPE等网络设备巨头的投资者而言，现在需要回答的问题不再是“市场会不会恢复”，而是“在恢复之后，谁会留下，谁会被挤出”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 2024年的深度调整不是终点，而是增长中枢下移的确认\n\nBARC的模型显示，2024年全球校园网络市场经历了16%的同比下滑。这个数字本身并不令人意外——2021年至2023年，市场分别增长了20%、15%和17%，远高于疫情前多年的中个位数增速。混合办公带来的超额采购需求在三年内被集中释放，随后必然是库存消化和订单回落。\n\n但真正重要的不是2024年的修正幅度，而是修正之后的增长中枢。BARC将2026年和2027年的增速预期分别下调至8%和7%，2021年至2026年的复合年增长率从7%降至6%。这意味着，即使市场走出低谷，也不会回到2021-2023年的高位，而是回到一个更接近历史均值、但略高于疫情前水平的“新常态”。\n\n这个判断的背后逻辑是：混合办公带来的结构性需求增量已经基本被定价，未来增长将更多依赖正常的设备更新周期和AI推理在边缘侧的网络准备。对于产业决策者而言，这意味着不能再以“市场会回到2023年水平”\n\n[... middle omitted ...]\n\n踪Arista、Cisco、HPE的最新订单趋势和竞争动态。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n园区网络市场，增长正在“减速”\n\n增长放缓，但结构机会还在\n\n最近看了份外资投行的园区网络研报，核心结论是：市场增速在逐步回归正常化。\n\n**1. 整体增速怎么看？**\n- 2025年增长约10%，2026年降到8%，2027年进一步放缓至7%。\n- 之前2021-2023年因为混合办公需求，增长特别猛（20%、15%、17%），2024年经历了一次16%的修正回调。\n- 现在市场回到更可持续的增长轨道，2021-2026年复合增速预计6%。\n\n**2. 几个细分市场在分化**\n- **有线交换**：最大的一块，企业正在正常更新设备，同时为AI推理做准备，订单和收入增长都不错。\n- **WLAN（无线局域网）**：WiFi 7在起量，2026年预计增长12%，2027年8%。其中云管理WLAN增速更快，2021-2026年复合增速17%。\n- **企业路由**：体量最小、变化慢，预计未来两年低个位数增长。\n- **SD-WAN**：2021-2026年复合增速约11%，2020-2023年高速增长后2024年也有回调。\n\n**3. 主要玩家在干嘛？**\n- **Cisco**：市占率近50%，但份额可能被蚕食\n\n[... middle omitted ...]\n\nustration of a glowing light bulb with an atom symbol inside, set against a star rating background (no text or symbols)\n</details>\n\nIn this report, we provide an update to our Campus Networkin\n\n[... middle omitted ...]\n\nrior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request."
  },
  {
    "id": "R020",
    "title": "美国银行：市场低估的不是AI算力需求，而是CPU在Agentic时代的重新定价",
    "digest": "[wechat_article.md]\n# 美国银行：市场低估的不是AI算力需求，而是CPU在Agentic时代的重新定价\n\n当整个半导体行业的目光都聚焦在GPU算力军备竞赛时，一份来自美国银行的最新研报提出了一个截然不同的核心判断：到2030年，服务器CPU的市场总规模将从当前的350亿美元跃升至1700亿美元以上，实现近5倍的增长。这个数字远高于该机构此前预估的1250亿美元。\n\n这个修正并非简单的乐观情绪。它源自一个正在发生的结构性转变：AI的工作负载正在从“一问一答”的生成式模式，转向“自主规划、调用工具、执行代码”的Agentic模式。在这种新范式下，CPU的角色从“后台管家”升级为“前线总指挥”，其价值也随之被重新定义。\n\n这份报告的核心洞察在于：CPU TAM的扩张，不是对GPU市场的零和博弈，而是整个AI系统复杂化带来的增量。对于投资者和产业决策者而言，理解这个“增量”从何而来，比争论“CPU vs. GPU”更有价值。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. Agentic AI让CPU从“配角”变为“总指挥”，这才是TAM扩张的真正引擎\n\n传统AI推理中，GPU承担了绝大部分计算，CPU主要负责数据搬运和调度。但在Agentic AI系统中，工作流发生了根本变化：一个AI Agent需要自主理解任务、分解步骤、检索知识库、调用外部API、执行代码，并在多步骤循环中保持状态记忆。\n\n这些任务的特点是：延迟敏感、顺序执行、I/O密集。这正是CPU的专长领域，而非GPU的强项。美国银行的报告将CPU在这一新架构中的角色定义为“中央思维引擎与任务协调器”。\n\n该机构据此将CPU市场拆分为三个相互独立且不重叠的细分领域：\n- 传统/本地/多云CPU：约300亿美元，基本盘，增长平稳。\n- AI集群计算/头节点CPU：约700亿美元，负责\n\n[... middle omitted ...]\n\n的CPU竞争格局模型感兴趣，也欢迎加入社群，与我们一同探讨。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI代理爆发，CPU市场翻倍增长\n\nCPU需求暴增5倍\n\n某外资投行最新研报指出，AI代理正在重塑计算架构，CPU不再是配角。\n\n核心逻辑：AI代理的工作模式从“一问一答”变成多步骤自主执行，需要大量CPU做规划、推理、调用工具。这类任务对延迟敏感、顺序执行、IO密集，XPU反而不如CPU合适。\n\n1️⃣ 服务器CPU市场大洗牌\n- 2030年市场规模从1250亿上调至1700亿美元\n- 2025-2030年复合增长率37%\n- 拆分三大场景：传统CPU约300亿、AI集群头节点约700亿、AI代理独立节点约700亿\n\n2️⃣ 各玩家位置变化\n- AMD目标价从500上调至560美元，仍是CPU首选\n- Intel从减持直接跳到买入，目标价135美元，看好其先进封装和晶圆能力\n- ARM目标价245→335美元，但认为估值已合理\n- 英伟达维持首选，受益于CPU-GPU-网络全栈整合\n\n3️⃣ 市场份额预测（2030年）\n- Intel和AMD各占约25%\n- ARM商业授权占35%\n- ARM定制化方案占15%\n\n4️⃣ 最关键的讨论\nCPU是在抢GPU的蛋糕，还是在做大整个AI市场？研报倾向后者：AI系统\n\n[... middle omitted ...]\n\n on higher CPU/GPU estimates, ARM to \\$335 from \\$245 on greater l-t chiplet potential; INTC is double-upgraded to Buy with a \\$135 PO (see our ), with higher estimates now reflecting both n-t\n\n[... middle omitted ...]\n\nw in accordance with firm policies.\n\nNeither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information."
  },
  {
    "id": "R021",
    "title": "Citi：光伏市场的真正拐点不在国内价格战，而在海外框架协议的规模与结构",
    "digest": "[wechat_article.md]\n# Citi：光伏市场的真正拐点不在国内价格战，而在海外框架协议的规模与结构\n\n过去一年，中国光伏行业在“内卷”与“出清”之间反复拉扯。市场参与者习惯于将注意力锁定在国内产业链价格的每一次波动上——多晶硅又跌了多少，电池片是否跌破现金成本，组件价格何时见底。\n\n但这份Citi在2026年6月10日发布的周度更新，提供了一个截然不同的观察信号。报告的核心判断并非关于价格底部，而是关于需求结构的切换。这份报告最值得看的结论是：**中国光伏产品的海外销售正在以框架协议的形式大规模落地，而国内市场的价格信号已经不再是行业景气度的唯一风向标。**\n\n对于产业决策者和投资者而言，理解这一结构性变化，远比预测下周多晶硅价格是否再跌1%更为重要。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 国内价格仍在低位徘徊，但最剧烈的下跌阶段已经过去\n\n截至6月10日当周，n型多晶硅价格下跌1.3%至每公斤33.3元人民币，太阳能电池片价格下跌4.6%至每瓦0.31元，组件价格微跌0.3%至每瓦0.721元。这些数字本身并不令人意外——它们延续了过去两年的下行趋势，且Citi明确指出，当前市场价格已接近可变生产成本。\n\n真正值得关注的不是跌幅本身，而是价格波动的形态。从Citi提供的长期价格走势图来看，多晶硅、硅片、电池片、组件的价格曲线在2024年至2025年间经历了最陡峭的下滑，而进入2026年后，曲线斜率明显放缓。这意味着，即便行业产能过剩的格局尚未根本改变，但价格下行的边际冲击正在减弱。\n\n这背后有两个支撑因素：一是部分高成本产能已经退出市场，二是产业链库存虽然仍处高位，但增速已明显放缓。以多晶硅为例，截至6月4日，生产商库存为29.5万吨，环比下降1.0%。虽然绝对水平依然很高，但方向性的变化值得留意。\n\n对于投资者来说，这意味\n\n[... middle omitted ...]\n\n完整报告和原始图表，进一步拆解这些关键假设背后的逻辑与风险。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n光伏链价格还在磨底，出口成唯一亮点\n\n📉 光伏链价格还在磨底\n\n光伏产业链上周继续低位运行，n型多晶硅、电池片、组件价格周环比均下跌，硅片持平，玻璃库存高达53.4天。不过出口端倒是签了不少大单。\n\n1️⃣ 上游：多晶硅还在跌\nn型棒状多晶硅均价33.3元/kg，周跌1.3%，颗粒硅持平在33.5元/kg。库存29.5万吨，供应依然充裕。硅片182mm、210mm价格都稳住，但小厂有降价动作。\n\n2️⃣ 中游：电池片跌最惨\nTOPCon电池片均价0.31元/W，周跌4.6%。组件182mm均价0.721元/W，微跌0.3%。玻璃2.0mm和3.2mm价格不变，但库存周期高达53.4天。\n\n3️⃣ 出口端：好消息来了\n6月初SNEC展会在上海闭幕，现场签约全是GW级框架协议。隆基、晶科、天合、晶澳分别与中东、非洲、东南亚买家签了新供应合同，还有少量光储一体化合作。多晶硅和硅片则基本靠年度长协。\n\n4️⃣ 新方向：空间光伏\n协鑫和晶澳分别牵头成立了空间光伏产业联盟，头部厂商在开发轻量级叠层电池供卫星使用，这是个全新的应用市场。\n\n某外资投行认为，由于供给过剩，对光伏板块持选择性态度。2026年政府反内卷措施预计会\n\n[... middle omitted ...]\n\nghai recently. We are selective on the China solar sector due to excessive supply. Anti-involution measures from the government, if any, in 2026E would likely be softer than those in 2025 sinc\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R022",
    "title": "Citi：AI供应链的紧俏不是短期噪音，而是新一轮定价权转移的信号",
    "digest": "[wechat_article.md]\n# Citi：AI供应链的紧俏不是短期噪音，而是新一轮定价权转移的信号\n\n市场对AI硬件的讨论，近期似乎出现了一些杂音。800V高压直流（HDVC）的采用被质疑进展缓慢，共封装光学（CPO）的落地时间表被推后，VR NVL72的内存配置低于预期。这些声音让部分投资者开始怀疑，AI供应链的景气周期是否已经见顶。\n\n但Citi刚刚发布的这份台湾科技月度追踪报告，给出了一个与市场情绪截然不同的结论。报告的数据和实地调研指向一个清晰的判断：**供应链的紧张不仅没有缓解，反而正在从产能层面蔓延到定价层面，而这一轮结构性变化，真正受益的或许不是市场最关注的那些名字。**\n\n这份报告最值得关注的，不是某个公司的月度营收超预期，而是一个正在发生的系统级变化——整个台湾科技供应链，从先进制程晶圆代工到封装测试，再到基板与铜箔基板（CCL），正在经历一轮由成本推动、由产能紧缺支撑的全面涨价周期。这不仅是短期的供需错配，更是AI基础设施建设从“抢产能”进入“抢议价权”阶段的标志。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 先进制程与封测的紧俏不是短期现象，而是AI芯片迭代加速的结构性结果\n\nCiti报告中最硬的信号来自台积电。5月营收4170亿新台币，同比增长30%，前5个月累计增长同样达到30%。这个数字本身并不令人意外，但报告明确指出，随着下半年N3制程的AI芯片和N2制程的智能手机SoC开始放量，**台积电有极大可能再次上调全年营收增长目标**。这意味着，市场对AI芯片需求的测算可能仍然偏保守。\n\n真正值得关注的是，Citi提到了一个增量因素：用于“代理型AI”（agentic AI）的CPU，将在明年为台积电提供额外的增长动力。这暗示AI芯片的需求结构正在从单一的GPU训练，向更多元的推理与边缘计算场景扩展。如果这一判断成\n\n[... middle omitted ...]\n\n针对某些关键假设进行压力测试。这些内容，一篇文章是装不下的。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n台系半导体5月追踪：AI链持续紧绷\n\n📌 供应链紧张持续\n\n某外资投行最新月度追踪显示，台系科技供应链5月营收整体符合预期，AI需求依然强劲，部分环节出现涨价趋势。\n\n1️⃣ **先进制程与封测**\n- 台积电5月营收4170亿新台币，月增2%/年增30%，前5月累计增长30%\n- 随着下半年N3 AI芯片、N2手机SoC放量，全年营收指引有上调空间\n- 联电、世界先进预计2H26迎来涨价周期\n- 封测厂ASEH、KYEC受益于LEAP平台和新AI芯片测试业务，订单能见度提升\n\n2️⃣ **测试接口与设备**\n- MPI、鸿劲精密、致茂5月营收表现超预期，GPU/AI ASIC客户订单强劲\n- 中华精测5月营收再创新高，管理层对全年月营收月增保持信心\n- 雍智科技受产能限制，但仁武厂6月有望贡献增量\n\n3️⃣ **IC设计分化明显**\n- AI相关：信骅、创意优于预期，产能瓶颈是短期风险\n- 消费电子：联发科、瑞昱、联咏在需求疲软中持稳，联发科2H26或有涨价空间\n- 世芯-KY的Trn3量产集中在2H26，预计6月营收回暖\n\n4️⃣ **服务器与PC**\n- 鸿海5月营收8594亿新台币，月增3%/年增40\n\n[... middle omitted ...]\n\nrt from scale-out first in 2H26 and 2027. This is also confirmed by our recent Computex tour and Taiwan tech conference. Among Taiwan tech supply chain, we see tight supply across advanced nod\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R023",
    "title": "JPM：中国汽车市场真正的拐点不是电动化渗透率，而是燃油车库存的定价崩塌",
    "digest": "[wechat_article.md]\n# JPM：中国汽车市场真正的拐点不是电动化渗透率，而是燃油车库存的定价崩塌\n\n这份来自JPM日本股票研究团队的五月中国汽车行业报告，表面上看是在更新月度销量数据，但真正值得产业决策者注意的，不是新能源渗透率突破63%这个数字本身，而是报告中一个被轻描淡写、却可能改变整个市场定价逻辑的信号——零里程二手燃油车数量正在上升。\n\n这意味着什么？意味着燃油车的新车价格和销量之间，正在形成一个自我强化的下行螺旋。这个夏季，燃油车市场将面临的不只是季节性低迷，而是一场由库存结构引发的定价机制重塑。电动化的故事我们已经听了太多次，但燃油车资产贬值速度的加速，才是当前最被低估的结构性变量。\n\n这份报告的价值在于，它用数据揭示了一个正在发生但尚未被充分讨论的转折点：消费者在新能源车比同级别燃油车更贵的情况下，仍然在加速转向新能源。这不是价格驱动的替代，而是认知驱动的替代。当燃油车的新车折价和二手残值同步下降，整个燃油车生态的盈利模型都需要重新审视。\n\n以下是我们从这份JPM报告中提炼出的五个核心洞察，以及一个尚未被充分回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 新能源渗透率突破63%的真正含义：消费者已不再用价格做选择\n\n五月中国乘用车零售销量152.8万辆，同比下降22%，连续第八个月同比下滑。但在这个总量萎缩的背景下，结构性的分化才是关键。燃油车零售57.9万辆，同比暴跌38%；新能源车零售84.9万辆，仅下降7%。新能源渗透率从四月的61%进一步攀升至63%。\n\n更值得关注的是价格信号。JPM指出，在10万元人民币（约合230万日元）以下的入门级市场，主流新能源车型的价格已经高于同级别燃油车。换言之，消费者选择新能源车，不是因为它们更便宜，而是因为它们在智能化体验、使用成本和使用场景上提供了燃油车无法替\n\n[... middle omitted ...]\n\n一起讨论这些数据的二阶影响，以及如何调整你的投资和经营假设。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月中国车市：燃油车熬不过这个夏天了\n\n**燃油车，真的危险了**\n\n**NEV渗透率63%，燃油车降价也卖不动**\n\n5月国内乘用车零售152.8万辆，同比-22%，连续第8个月下滑。但结构很说明问题：\n\n1️⃣ **NEV渗透率加速到63%**，环比再涨1.6个百分点。燃油车零售仅57.9万辆（-38%），而NEV卖了84.9万辆（-7%）。消费者用脚投票，即便10万元以下入门级NEV已经比同档燃油车更贵，大家还是选NEV。\n\n2️⃣ **燃油车这个夏天会很难熬**。丰田5月零售10.2万辆（-29%），本田2.8万辆（-49%）。更糟的是，零公里二手燃油车库存又开始堆积，这会进一步压低新车价格和销量。燃油车保值率也在下降，对NEV的优势正快速消失。\n\n3️⃣ **出口创历史新高**，5月乘用车出口80.9万辆（+73%），连续三个月破纪录。其中NEV出口43.5万辆（+110%），燃油车出口37.4万辆（+42%）。比亚迪等热门品牌产能接近极限，国内外交付周期都在拉长。除了欧洲和东盟，巴西和澳大利亚正成为中国汽车出口的新重点。\n\n燃油车降价也没能阻止份额流失，这个夏天可能是转折点。欢迎一起讨论。\n\n#学\n\n[... middle omitted ...]\n\npular internal combustion engine (ICE) models dropped out of the top sales rankings, despite deeper discounts. We assume that ICE auto sales will fall this summer because of seasonal factors, \n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 11 Jun 2026 03:28 AM JST\n\nDisseminated 11 Jun 2026 03:28 AM JST"
  },
  {
    "id": "R024",
    "title": "摩根斯坦利：市场低估了供给侧的“结构性断裂”，而非仅仅需求回暖",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：市场低估了供给侧的“结构性断裂”，而非仅仅需求回暖\n\n这份摩根斯坦利2026年6月发布的“亚洲暑期学校：中国材料”报告，传递了一个与市场普遍叙事不同的信号。多数投资者仍在纠结于中国房地产何时触底、基建投资能否加码，但该机构认为，真正值得关注的并非需求端的线性复苏，而是供给端正在发生的、不可逆的结构性变化。\n\n报告的核心判断是：中国材料行业正经历一场由供给约束与新兴需求（储能系统ESS与人工智能AI）共同驱动的再定价。摩根斯坦利明确表示，在这一环境下，他们更偏好铝、铜、锂、铀、金和玻璃纤维等领域的权益资产。这意味着，投资者需要将分析框架从“需求预测”转向“供给弹性评估”。\n\n这份报告的独特价值在于，它不仅给出了自上而下的行业观点，还提供了详尽的消费指数模型，将宏观叙事拆解为可追踪的微观指标。以下是我们从这份报告中提炼出的几个关键洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 供给约束正在从“周期性扰动”演变为“结构性天花板”\n\n市场对大宗商品的分析往往过度聚焦于需求端，尤其是中国房地产的拖累。但摩根斯坦利在报告中反复强调的，是供给侧的长期紧缩。这并非简单的矿山停产或冶炼厂检修，而是一种更深层次的、由资本开支不足、ESG合规成本上升以及地缘政治风险共同塑造的供给刚性。\n\n以铝为例，中国电解铝产能已经逼近4500万吨的政策天花板，新增产能极为有限。同时，海外能源成本的上升也抑制了非中国地区的复产意愿。摩根斯坦利对2026年铝价的预测为3386美元/吨，较市场共识高出11%，对2027年的预测更是高出13%。这种显著的偏离，恰恰说明市场尚未充分定价供给侧的“硬约束”。\n\n对于投资者而言，这意味着那些拥有稳定、低成本产能且符合环保标准的龙头企业，其定价权将比历史周期更强。传统的“需求下行-价格下跌”逻\n\n[... middle omitted ...]\n\n系数）进行更细致的拆解，并分享我们整理的相关产业链数据图表。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国材料板块，正在经历一场“供给侧”驱动的结构性机会。\n\n最近某外资投行出了一份中国材料研报，核心逻辑很清晰：供给干扰 + 储能（ESS）与AI需求改善 = 精选材料股的机会。\n\n他们明确看好6个方向：铝、铜、锂、铀、黄金、玻璃纤维。\n\n1️⃣ 铝：最确定\n- 研报给出的2026/2027年铝价预测，都比市场共识高11%/13%。\n- 核心逻辑：国内产能天花板+海外供应扰动，供给弹性很弱。\n\n2️⃣ 铜：AI和电力是双引擎\n- 中国铜消费指数显示，电力（占比47%）是绝对主力。\n- 研报预测2026年电力用铜增速8%，明显高于2025年的5%。\n\n3️⃣ 锂：供需边际改善\n- 2026年碳酸锂价格预测22840美元/吨，比市场共识高17%。\n- 注意：研报认为长期价格会回落，短期供给端有支撑。\n\n4️⃣ 黄金：避险+央行购金\n- 2026年金价预测4916美元/盎司，2027年4950美元，持续高位。\n\n5️⃣ 铀：核能复兴故事\n- 2026年铀价预测93.4美元/磅，比共识高6%。\n\n6️⃣ 玻璃纤维：需求结构升级\n- 风电、电子布等高端应用拉动，不是传统建材逻辑。\n\n💡 几点观察：\n- 钢铁需求2026年\n\n[... middle omitted ...]\n\nciate\n\nCynthia.Tang@morganstanley.com +852 3963-4360\n\n![](images/cc4abe4695c35b10cdecd5610151dc98602337a55a3fa2df0ed2f0e59445d87d.jpg)\n\n<details>\n<summary>text_image</summary>\n\nAsia Summer Sch\n\n[... middle omitted ...]\n\nChina Cement (2233.HK)</td><td>U (04/20/2026)</td><td>HK$1.63</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R025",
    "title": "摩根斯坦利：中国聚乙烯净进口量才是美国合同价格真正的定价锚",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：中国聚乙烯净进口量才是美国合同价格真正的定价锚\n\n市场参与者习惯将目光聚焦于中东霍尔木兹海峡的供应中断，并据此线性外推美国聚乙烯价格的上涨路径。摩根斯坦利最新发布的研报却提供了一个截然不同的分析框架：真正决定美国合同价格走向的关键变量，并不在中东，而在中国。这份报告的核心判断是，中国聚乙烯净进口量的变化幅度与可持续性，将成为未来数月美国合同价格走势最核心的KPI，其影响力甚至超过了供应中断事件本身。\n\n4月份的数据已经验证了这一逻辑的威力。当霍尔木兹海峡关闭导致全球供应减少约15%时，中国净进口量的急剧收缩，从冲突前每月约110万吨骤降至4月的约18万吨，相当于向除中国以外的全球市场释放了约9%的额外供应。这一行为几乎完全对冲了中东供应中断带来的紧张局面，使得4月美国出口市场并未如市场普遍担忧的那样出现极端紧缺。市场低估的，从来不是地缘政治事件本身，而是中国作为全球最大聚乙烯买方，其库存行为与贸易流调整对全球供需平衡的再定价能力。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 中国4月净进口量的骤降揭示了一个被低估的库存缓冲池\n\n报告的核心发现之一，是中国在冲突爆发前积累了远超市场认知的过剩库存。摩根斯坦利通过咨询行业专家推断，在伊朗冲突爆发前的6至12个月内，中国贸易商可能积累了约100万吨的额外库存，将中国的过剩库存总量推高至约230万至350万吨，相当于约30天的国内需求量。这一判断直接解释了4月中国为何有能力将净进口依赖度从2025年约31%的水平骤降至约5%。\n\n这一行为意味着，中国并非被动接受供应中断，而是主动利用其庞大的库存作为缓冲，不仅减少了进口（尤其是从美国的进口减少了约40%，约50万吨），还增加了出口（约40万吨，主要流向东南亚以填补中东出口缺口）。这种主动的贸易流调整，使得\n\n[... middle omitted ...]\n\n这一关键假设的验证结果及其对下半年全球聚乙烯定价格局的含义。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国PE净进口量，成了关键风向标\n\n📊 中国PE净进口量，怎么影响全球？\n\n某外资投行最新研报指出：中国聚乙烯（PE）的净进口数据，是判断美国PE合同价格走势的关键指标。\n\n1️⃣ 发生了什么？\n4月霍尔木兹海峡关闭期间，中国大幅调整了PE进出口策略。净进口从冲突前每月约110万吨骤降至4月的18万吨，降幅达83%。具体操作：进口砍了约50万吨（美国货少了40%），出口增加了约40万吨（主要填补中东缺口）。\n\n2️⃣ 影响有多大？\n中国净进口依赖度从2025年的31%直接跌到4月的5%。这波操作给全球市场额外增加了9%的供应，部分抵消了海峡关闭导致的15%供应缺口。\n\n3️⃣ 库存是关键\n研报推测，中国在冲突前可能积累了约230-350万吨的过剩库存（相当于30天国内需求），远超市场预期。4月高峰后，中石化和中石油的聚烯烃库存已下降19%，回到2024/2025年水平。\n\n4️⃣ 后续推演\n如果中国在6-7月消耗完过剩库存，恢复冲突前的进口节奏，每月可能额外需要约25万吨美国出口（占美国年供应12%），这可能推高美国PE合同价。反之，价格可能加速回落。\n\n5️⃣ 当前市场\n美国现货价已从3-4月的大涨后开始回\n\n[... middle omitted ...]\n\n by: i) reducing imports by \\~500K mt (approximately \\~40% less from the US in particular); and ii) increasing exports by \\~400K MT (most of which we believe went to Southeast Asia to offset t\n\n[... middle omitted ...]\n\nd>Westlake Corp (WLK.N)</td><td>E (01/09/2018)</td><td>$87.12</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R026",
    "title": "BARC：通胀数据揭示的真正风险不是物价上涨，而是定价权断裂",
    "digest": "[wechat_article.md]\n# BARC：通胀数据揭示的真正风险不是物价上涨，而是定价权断裂\n\n中国5月通胀数据已经发布。CPI同比1.2%，PPI同比3.9%。从数字看，物价似乎在温和回升。但真正值得关注的，不是这两个数字本身，而是它们背后的结构性断裂：上游成本正在加速传导，但下游企业几乎完全丧失了转嫁能力。PPI上游原材料同比上涨9.2%，采掘业同比上涨15.8%，而下游消费品PPI却仍在收缩，同比负增长0.8%。这组数据描绘的不是一个通胀周期，而是一个利润分配极端失衡的图景。\n\n这份BARC研报的核心价值，不在于它预测了通胀数字，而在于它揭示了当下中国经济中最关键的价格传导机制正在失效。当上游成本无法向下游有效传递时，制造业企业的利润率将面临持续挤压，而终端需求的疲弱又会反过来抑制就业和收入预期。这不是一个短期波动，而是一个需要重新评估资产定价的结构性信号。\n\nBARC的报告指出，5月核心CPI从1.2%回落至1.1%，服务CPI从0.9%降至0.8%。在能源价格推高整体通胀的同时，扣除能源和食品的核心通胀却在走弱。这意味着，所谓的“通胀”更多是输入性的成本推动，而非需求拉动的内生复苏。对于投资者和产业决策者而言，真正需要关注的不是CPI和PPI的绝对值，而是这两者之间的剪刀差所反映的定价权分布。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 上游涨价正在加速，但下游企业只能“咽下”成本\n\n这份研报最清晰的信号来自PPI的分项数据。5月PPI同比增速从4月的2.8%跳升至3.9%，连续第二个月加速。但这一增长高度集中于上游。采掘业PPI同比上涨15.8%，原材料PPI上涨9.2%，而制造业PPI仅增长2.3%。这意味着，利润正在向上游资源品环节集中，而大量中下游制造企业面临成本上升与售价低迷的双重挤压。\n\nBARC特别指出，有色金属矿\n\n[... middle omitted ...]\n\n致的行业拆解和后续数据追踪，一起探讨这些未解问题的可能答案。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nPPI 上游飙涨，下游却难涨价\n\n上游猛涨，下游承压\n\n5月CPI持平1.2%，PPI加速至3.9%。油价是主要推手，但核心CPI和服务CPI反而走弱，说明内需依然疲弱，涨价传导不畅。\n\n1️⃣ PPI：上游集中涨价，下游仍在通缩\n- 采掘业PPI同比15.8%（4月10.6%），原材料9.2%（4月7.1%），主要受非金属矿和能源拉动\n- 制造业PPI仅2.3%，下游消费品PPI继续负增长-0.8%\n- 企业难以将成本转嫁，利润空间被挤压\n\n2️⃣ CPI：油价支撑，核心走弱\n- 能源贡献0.66pp，汽油同比23.5%\n- 核心CPI降至1.1%，低于年初均值1.3%\n- 汽车价格持续下跌，房租创2023年1月以来最大跌幅\n\n3️⃣ 关键信号：没有“第二轮效应”\n- 上游涨价没有传导到下游消费品和服务\n- 住房租金、汽车价格持续走弱，反映内需不足\n- 黄金珠宝贡献减弱，从0.2pp降至0.17pp\n\n简单说：上游在涨价，下游在降价，中间企业两头受气。内需疲弱是核心问题，油价撑起来的CPI不可持续。\n\n大家怎么看后续PPI走势？欢迎一起讨论。\n\n#学习笔记\n\n[source_mineru.md]\n## Ch\n\n[... middle omitted ...]\n\ninflation and energy-related components of CPI, while the impact on core and services CPI remained contained, pointing to limited second-round effects. On a month-on-month basis, PPI began to \n\n[... middle omitted ...]\n\nrior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request."
  },
  {
    "id": "R027",
    "title": "NOM：人民币中间价模型正在揭示一个被低估的政策信号",
    "digest": "[wechat_article.md]\n# NOM：人民币中间价模型正在揭示一个被低估的政策信号\n\n人民币汇率中间价的每日设定，长期以来被市场视为中国央行汇率管理意图的“温度计”。但多数观察者只盯着最终公布的数值本身，而忽略了模型内部各因子的结构性变化。NOM最新发布的USD/CNY定盘价模型报告，提供了一个更锐利的观察视角：模型隐含的“逆周期因子”调整力度正在发生质变，这背后可能不是简单的维稳，而是对人民币定价逻辑的一次系统性再校准。\n\n这份报告的核心价值不在于给出一个预测点位，而在于它拆解了中间价形成的“黑箱”。当模型投影值与实际公布值之间的偏差持续扩大时，市场真正应该关注的不是汇率会贬到多少，而是政策制定者正在用什么样的新框架来管理预期。本文将从NOM模型的三个关键维度出发，解读这一信号对投资者意味着什么。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 模型投影的“跳降”并非单边看空，而是多因子共振的结果\n\nNOM模型显示，最新的USD/CNY定盘价模型投影值为6.7816，较前一次的6.8130下降了314个基点。这个幅度在近期并不常见。但更值得关注的是，模型投影的下降并非由单一货币驱动，而是来自一个多元化的因子组合。\n\n根据报告中的贡献度分析，欧元和澳元分别贡献了15.6和8.5个基点的正向变动，而韩元则反向贡献了13.5个基点。这意味着，人民币中间价的模型投影变化，本质上是全球外汇市场在特定时间窗口内对主要货币相对价值重估的映射。欧元和澳元的走强，部分抵消了韩元等亚洲货币带来的贬值压力。\n\n这里的关键洞察是：中间价模型并非被动反应，而是一个动态加权系统。当欧元和澳元的权重上升时，美元指数的波动对人民币的影响就会被部分对冲。NOM模型揭示的，正是一个正在从“盯住美元”转向“盯住一篮子货币”的精细化操作过程。对于投资者而言，这意味着不能再简单用\n\n[... middle omitted ...]\n\n踪逆周期因子的变化轨迹，并分享对年底前人民币汇率路径的推演。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n人民币中间价，模型在说什么\n\n模型指向6.78\n\n比上次低314个点\n\n最近某外资投行更新了人民币中间价预测模型，数据挺有意思，跟朋友们分享一下逻辑。\n\n**模型怎么看？**\n1️⃣ 最新模型预测：6.7816，比上次的6.8130低了314个点。加上逆周期因子后是6.7957，比上次低173个点。\n2️⃣ 主要贡献来自欧元（+15.6点）和澳元（+8.5点），韩元拖后腿（-13.5点）。\n\n**近期误差有意思**\n- 今年1月误差高达-1800点，4月-1200点，最近几个月误差明显收窄到+600点。\n- 模型在修正，说明预测框架在适应新环境。\n\n**几个关键时间点**\n- 7月底：政治局会议定调经济工作\n- 10月黄金周、11月APEC在深圳\n- 12月中央经济工作会议\n- 年底可能还有高层访问\n\n模型就是个参考框架，实际中间价还要看逆周期调节和篮子货币走势。欢迎一起讨论汇率逻辑。\n\n#学习笔记\n\n[source_mineru.md]\n## USD/CNY fix model\n\nGlobal Markets Research\n\n11 June 2026\n\nForeign Exchange - Asia e\n\n[... middle omitted ...]\n\ned change (without counter-cyclical factor)  \n![](images/77d0141e99cb61eee718ad4aa9665030565193c3946cc89c48291f54e04cd538.jpg)\n\n<details>\n<summary>bar chart</summary>\n\nTop 4 weighted contribut\n\n[... middle omitted ...]\n\nrmation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R028",
    "title": "NOM：人民币中间价模型正在释放一个被市场低估的政策信号",
    "digest": "[wechat_article.md]\n# NOM：人民币中间价模型正在释放一个被市场低估的政策信号\n\n市场对人民币汇率的讨论，往往集中在两个维度：一是美元指数的强弱，二是中国央行的政策意图。但NOM这份发布于2026年6月12日的USD/CNY定盘价模型报告，提供了一个更精细、更值得关注的视角——中间价定价机制本身正在发生结构性变化，而市场对此的定价可能远远不够。\n\n这份报告的模型投影显示，在没有逆周期因子的情况下，USD/CNY中间价模型预测值为6.7607，较前一日的6.8150大幅下调543个基点。即使计入逆周期因子，预测值也降至6.7759，较前一日定盘价低391个基点。这不是一次简单的技术调整。它意味着，在当前的汇率形成机制下，人民币中间价的内在压力方向已经发生了根本性扭转。\n\n真正重要的不是这个数字本身，而是数字背后的逻辑：NOM的模型正在捕捉到一种从“贬值压力”向“升值压力”的切换信号。这种切换，如果持续，将深刻影响所有持有人民币资产、或对中国宏观经济有敞口的投资者的定价框架。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 模型投影的543个基点下调，不是噪音，是趋势拐点的信号\n\n理解这份报告的价值，首先要理解NOMUSD/CNY定盘价模型的工作原理。该模型并非预测市场交易价格，而是基于一篮子货币的隔夜变动、以及其他技术性因子，来推算央行可能设定的每日中间价。其核心价值在于，它剥离了市场情绪和短期投机因素，呈现的是“如果央行完全遵循规则，中间价应该在哪里”。\n\n6月12日的模型投影显示，无逆周期因子调整的中间价应为6.7607，较前一日官方定盘价低543个基点。这是一个巨大的单日变动。回顾报告中的历史模型误差图（Fig. 2），在2025年的大部分时间里，模型误差持续为负，意味着实际中间价持续高于模型预测——央行在用逆周期因子对冲贬值压\n\n[... middle omitted ...]\n\n场的传导路径。期待与您一起，在不确定的市场中寻找确定的逻辑。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n人民币中间价模型指向6.76\n\n模型预测 6.7607\n\n较前次低543个基点\n\n某外资投行刚刚更新了人民币中间价预测模型，最新读数是6.7607，比前一次预测低了543个基点。这个数字比前一交易日官方收盘价也低了166个基点。\n\n如果加入逆周期因子，模型预测会调整到6.7759，比前次定盘价低391个基点。\n\n1/ 模型怎么算的\n模型主要参考一篮子货币隔夜变动。昨晚贡献最大的四个货币是：韩元(-36个基点)、欧元(-32个基点)、澳元(-20个基点)、墨西哥比索(-13.5个基点)。整体来看，非美货币走弱带动了中间价下行。\n\n2/ 模型误差在收窄\n从历史误差看，今年1月模型偏差还有-1800个基点，4月收窄到-1200，到7月已经接近0。最近几个月误差基本在600个基点以内，说明模型稳定性在提升。\n\n3/ 后续关注什么\n研报列了几个重要时间节点：7月底政治局经济工作会议、10月国庆假期、11月深圳APEC、12月中央经济工作会议，以及年底可能的中美高层会晤。\n\n这些事件都可能影响汇率政策方向，值得持续跟踪。\n\n#学习笔记\n\n[source_mineru.md]\n# USD/CNY fix model\n\nGl\n\n[... middle omitted ...]\n\nd change (without counter-cyclical factor)  \n![](images/7ed9f2f094245f7b6a89486bdef7cfd5515112a2a95b9cdc104ffc390778661b.jpg)\n\n<details>\n<summary>bar chart</summary>\n\n| Index | Top 4 weighted \n\n[... middle omitted ...]\n\nrmation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R029",
    "title": "GS：市场真正低估的不是2万亿数据中心投资，而是“六张网”的宏观含义",
    "digest": "[wechat_article.md]\n# GS：市场真正低估的不是2万亿数据中心投资，而是“六张网”的宏观含义\n\n一份关于中国政府计划在未来五年投入2万亿元建设数据中心的外媒报道，上周引发了市场对AI基建主题的再度关注。然而，这份来自GS中国宏观团队的研报给出了一个与市场直觉相反的判断：这个数字本身并非新闻，真正值得关注的，是它背后所揭示的中国财政扩张逻辑正在发生一次结构性切换。\n\n市场往往将此类消息解读为“AI概念股利好”，但GS的分析框架提醒我们，如果只看到数据中心本身，就错过了这份报告最核心的洞察——中国正在通过“六张网”的投资框架，重新定义政府主导投资的投向、融资方式与节奏。理解这个框架，比猜测2万亿元是否超预期重要得多。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 2万亿数据中心投资不是增量信号，但“六张网”的加速落地才是\n\nGS明确指出，所谓“2万亿元数据中心投资计划”并非新消息。早在今年3月“两会”期间发布的“十五五”规划中，数据中心已被纳入“六张网”的算力网络范畴。4月政治局会议和6月央视的再度强调，更多是对既有规划的重复确认，而非新增承诺。\n\n那么市场为什么会有反应？GS的解释是，市场对政策信号的定价存在错位。投资者习惯于将单一项目的规模数字视为催化剂，而忽略了政策执行节奏的变化才是更关键的变量。真正的新信息并非2万亿元本身，而是近期政策沟通频率和项目准备工作的明显提速。\n\nGS观察到，5月底以来，包括政策性银行新融资工具在内的多种财政工具已开始加速落地，部分地方政府在6月初即加快了项目推进。这与一季度GDP超预期后、二季度财政支出节奏明显放缓形成了对比。换言之，政策制定者正在从“等待数据”转向“提前准备”。\n\n对这一判断的深层含义在于：如果投资者只盯着2万亿元这个数字是否被市场消化，就会错过“六张网”整体投资加速这一更大的叙事。\n\n[... middle omitted ...]\n\n群中分享更多原始图表、数据细节以及对这些未解问题的持续跟踪。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n2万亿算力投资，不是新故事\n\n算力基建加速\n\n但这是旧闻，不是突发\n\n最近都在传“2万亿建数据中心”的消息。其实，这事在3月“十五五”规划里就定了，属于“六张网”的算力网部分。\n\n拆开看几个关键点：\n\n1️⃣ 钱从哪里来\n超长期国债+地方专项债+政策性银行新工具+商行贷款。这次不走老路，不靠城投平台加杠杆，而是想带动社会资本一起投。\n\n2️⃣ 为什么现在提\n二季度财政支出节奏慢下来了，GDP超预期后政策在观望。但5月底还有7.7万亿未发完的债券额度，加上8000亿政策性银行工具，弹药充足。最近政策信号变多，说明可能在为下半年加速部署做准备。\n\n3️⃣ 规模有多大\n按某外资投行测算，2万亿算力投资只占2026-30年固投的0.8%。更大的是“六张网”整体——发改委说今年可能超7万亿，占固投约14%。\n\n4️⃣ 核心信号\n政策方向在明确转向：高技术制造、AI基础设施、战略供应链、民生。7月政治局会议是关键观察窗口，如果二季度GDP继续走弱，可能会加速动用财政余力。\n\n简单说：不是新故事，但执行节奏在加快。\n\n#学习笔记\n\n[source_mineru.md]\n# China: Media reported RMB\n\n[... middle omitted ...]\n\ntics networks — investment push may be accelerating, supported by a wider funding mix that includes central and local government bonds, the policy bank new financing tool, and commercial bank \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R030",
    "title": "摩根斯坦利：市场误读了中国的资本管控信号，真正焦点在实体经济出海而非个人资金外逃",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：市场误读了中国的资本管控信号，真正焦点在实体经济出海而非个人资金外逃\n\n过去几周，关于中国收紧境外投资监管的消息在市场上引发了一轮不小的焦虑。AIA、HSBC、渣打等香港金融股出现波动，一些投资者开始担忧中国正在逆转资本账户开放的方向。但摩根斯坦利最新发布的一份研报给出了一个与市场情绪截然不同的判断——这些新规的核心目标不是堵截个人资金外流，而是为中国企业日益增长的海外实体投资建立一个系统性的法律保护框架。\n\n这份报告的价值不在于它提供了多少新的政策细节，而在于它拆解了一个关键问题：当市场把注意力集中在“资本外逃”这个叙事上时，真正重要的结构性变化是什么。如果我们只看新闻标题，很容易得出“中国在收紧”的结论。但如果仔细审视政策制定的参与者、文件的法律分类、以及具体的执行细则，会发现一个完全不同的故事。\n\n这份摩根斯坦利研报最值得关注的判断是：当前的政策调整本质上是制度升级，而非方向逆转。中国正在从“逐案审批”的碎片化管理模式，转向“立法框架”的系统性保护模式。对于长期关注中国金融开放和香港市场地位的投资者来说，这意味着需要重新校准对政策风险的定价。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 国务院新规的核心信号：只有实业主管部门出席，没有金融监管机构参与\n\n判断一项政策的真实意图，最简单的方法就是看谁在主导。摩根斯坦利在报告中指出，国务院新规的新闻发布会上，出席的只有司法部、发改委和商务部——没有任何金融监管机构参与。这个细节本身就是最直接的答案。\n\n如果这是一项针对个人金融投资的收紧政策，银保监会、证监会、外汇局不可能缺席。这三家机构的缺席意味着，政策的目标群体是进行海外实业投资的企业，而不是进行证券投资的个人。\n\n从文件的法律分类来看，新规被归入国务院文件体系中的“商贸、海关、旅游、对外经\n\n[... middle omitted ...]\n\n告的原始图表和解读，并与读者一起追踪这些关键假设的验证过程。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n海外投资新规，别自己吓自己\n\n🔍 拆解核心逻辑\n\n最近关于海外投资的新规讨论很多，我仔细看了某外资投行的研报，核心观点很清晰：**这次政策主要针对企业出海，不是管个人。**\n\n1️⃣ 政策目标：保护企业走出去\n- 发布会只有司法部、发改委、商务部出席，没有金融监管机构\n- 政策分类在商务、海关、对外经济合作领域\n- 核心是建立法律框架保护中国海外实业投资，不是限制个人金融投资\n\n2️⃣ 个人跨境投资影响有限\n- 证监会的清理重点是“在境内从事跨境股票交易”，不是关境外账户\n- 香港证监会明确：正常开户、交易不受影响（只要符合KYC）\n- 个人5万美元换汇额度没变化\n- 家庭金融资产增速>10%，但收入只增4-5%，数据不支持大规模资本外逃\n\n3️⃣ 政策逻辑很清晰\n- 企业出海需要更系统的法律保护\n- 单个企业谈判能力有限，政府出面更有议价权\n- 监管框架化是长期趋势，金融法也在走同样路径\n\n💡 几点思考：\n- 政策是“保护”不是“限制”\n- 跨境金融活动只要合规，影响有限\n- 港股通等正规渠道会持续受益\n\n欢迎一起讨论你对新规的理解~\n\n#学习笔记\n\n[source_mineru.md]\n## China \n\n[... middle omitted ...]\n\ncil press conference announcing the new rules, only the Ministry of Justice, the NDRC.and the Ministry of Commerce were present – none of the financial regulators were involved. We view that a\n\n[... middle omitted ...]\n\npment Bank (600000.SS)</td><td>E (08/05/2025)</td><td>Rmb9.59</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R031",
    "title": "Bernstein：市场低估的不是电力需求，而是非日照时段的供给刚性",
    "digest": "[wechat_article.md]\n# Bernstein：市场低估的不是电力需求，而是非日照时段的供给刚性\n\n印度电力板块在过去二十年里，几乎被市场当作“空调股”来交易——夏季来临前买入，季风来临前卖出。这种季节性博弈在2024年中达到顶峰，随后需求增速骤降至同比约1%，持续了近20个月。今年，天气、能源安全与数据中心三大因素重新点燃了市场热情。但Bernstein这份研报的核心判断是：市场正在低估一个结构性变化——印度电力短缺的真正瓶颈，已经从总量转向时段，而非日照时段的供给刚性在未来三年内几乎无法缓解。\n\n这不仅仅是印度电力股的投资信号。对于关注全球制造业转移、数据中心布局与新兴市场基础设施投资的决策者而言，这份报告提供了一个难得的观察窗口：当一个经济体的电力系统从“总量过剩”切换到“时段性短缺”时，资产定价的逻辑正在被重写。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 表面数据在说“宽松”，但拆解时段后看到的却是持续恶化的晚间缺口\n\n如果只看印度电力现货市场的总量数据，结论很可能是“供需正在趋于平衡”。Bernstein指出，今年4-5月现货市场的平均电力价格约为3.8卢比/千瓦时，显著低于2023年的高点；买卖报价比也低于1，意味着卖盘多于买盘。这些指标似乎在暗示紧张局势正在缓解。\n\n但问题出在平均数据掩盖了结构性分化。当Bernstein将数据按“一天中的时段”进行拆解后，一个截然不同的图景浮现出来：早晨与晚间的电力价差已经扩大到约7卢比/千瓦时，并且仍在扩大。而在过去十年里，这个价差几乎为零。晚间时段的买卖报价比在今年夏季达到2.2倍，而2020年仅为0.5倍。\n\n这意味着什么？总量层面的宽松，完全是由日照时段的太阳能电力供给充裕造成的。而真正的压力——非日照时段——正在以肉眼可见的速度恶化。对于任何依赖晚间连续生产或高负荷运行的工\n\n[... middle omitted ...]\n\nein报告中的关键图表与原始数据，帮助你建立自己的判断框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n印度电力：不是缺电，是缺傍晚的电\n\n封面短标题：电力缺口在哪？\n\n封面副标题：晚上7点，才是真正的用电高峰\n\n正文：\n\n某外资投行最新研报拆解印度电力市场，结论很清晰：整体不缺电，但傍晚时段缺口越来越大。这不是一个周期性故事，而是结构性变化。\n\n1/ 表面数据在“降温”，但晚上才是真相\n- 现货市场均价从疫情高点回落，买卖比也低于1\n- 但拆开看时段：早间和晚间价差已拉大到7卢比/度（历史接近0）\n- 傍晚买卖比今年夏天2.2倍，2020年只有0.5倍\n- 储能成了天然套利工具\n\n2/ 需求：低基数+天气，今年增长可能超预期\n- 去年电力需求只增了1%，今年预计6%已经算保守\n- 降雨预测低于正常，叠加数据中心、电气化等结构性需求\n- 过去投资者习惯夏季后卖出，但这次下半年可能继续走强\n\n3/ 供给：未来3年傍晚缺口难解\n- 上轮周期2012年有100GW在建，这次只有40GW\n- 未来3年预计仅新增15GW火电，而傍晚需求将增长50GW\n- 除非每年加15GW电池储能，否则缺口无解\n- 去年大量BESS招标由小玩家低价拿下，现在电池价格和汇率都不利，很多可能无法落地\n\n4/ 估值：国企便宜，民企溢价\n- 国\n\n[... middle omitted ...]\n\na structural and not a cyclical story, but the sector has traded more like air-conditioner stocks - buy before summer and sell before onset of monsoons. The sector peaked in mid-CY24, post whi\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R032",
    "title": "Bernstein：日本半导体设备在中国市场的份额流失并非结构性，反转正在酝酿",
    "digest": "[wechat_article.md]\n# Bernstein：日本半导体设备在中国市场的份额流失并非结构性，反转正在酝酿\n\n市场对日本半导体设备商在中国市场份额持续下滑的担忧，可能夸大了问题的严重性。Bernstein最新发布的一份深度研报指出，2024至2025年间日本设备商在中国进口市场的名义份额从26%降至23%，表面上看是连续三年的下滑趋势延续。但报告的核心判断是：这一流失主要由汇率和客户下单节奏等暂时性因素驱动，而非竞争力被中国本土或海外对手结构性侵蚀。随着日元贬值红利转化为定价空间、中国客户投资节奏恢复正常化，日本设备商有望从2026年下半年起重新收复失地。\n\n这份报告之所以值得关注，不仅因为它挑战了市场对“日本设备在中国节节败退”的简单叙事，更因为它提供了一个拆解复杂市场份额变化的分析框架——在汇率波动超过30%、中国自主化进程加速、客户投资周期分化的背景下，名义份额数据本身可能产生严重误导。对于持有或关注东京电子、科休半导体、斯库林等日本前道设备龙头的投资者而言，报告的判断直接关系到未来12至18个月的估值叙事能否逆转。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 日元贬值31%带来的名义份额流失，掩盖了日本设备实际竞争力的稳定\n\nBernstein报告首先做了一件必要但容易被市场忽略的工作：剔除汇率影响重新计算日本设备商在中国的真实市场份额。过去五年日元对美元贬值约31.5%，而日本设备商普遍以日元报价，这意味着以美元计价的进口统计会系统性地低估日本设备的实际出货量。\n\n调整后的数据令人意外。2024年日本设备商在中国进口市场中的名义份额为26%，但经汇率调整后实际份额为31%；2025年名义份额降至23%，调整后为26%。如果将2024和2025年合并平均，调整后的份额为28.6%，与2021至2023年间的平均水平28.1%几\n\n[... middle omitted ...]\n\n日本设备商在中国市场是迎来阶段性反弹，还是进入长期下行通道。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本半导体设备，正在中国“回血”\n\n中国进口份额触底了\n\n日本设备在中国进口份额从26%→23%，但别急着下结论。\n\n1️⃣ 汇率才是“元凶”\n日元过去5年贬值31.5%，日本设备商以日元计价，名义份额自然缩水。调整汇率后，2024/2025年份额其实是31%/26%，和2021年的28%差不多。\n\n2️⃣ 订单节奏≠结构流失\n客户下单时间差导致2025年份额波动。比如长鑫存储（CXMT）2025年订单减少，但这不是永久性流失。把2024-2025年数据平均，日本设备份额28.6%，和2021-2023年均值28.1%几乎持平。\n\n3️⃣ 各家情况不同\n- 东京电子（TEL）：客户组合和定价策略导致份额下滑\n- Screen：订单节奏+客户本土化尝试，清洗设备领域国产替代加速\n- Kokusai：主要受CXMT投资节奏影响\n\n4️⃣ 反转信号已现\n日元贬值让日本设备性价比突出，涨价空间打开。中国客户正重新增加对日订单，日本设备商也开始更积极调价。TEL已明确表示在中国有涨价空间，Screen预计CXMT订单2年后回归。\n\n5️⃣ 设备板块机会\n过去2-3个月半导体设备跑输存储/模拟等周期股，但未来几年资本支出\n\n[... middle omitted ...]\n\nFrancis Ma\n\n+852 2123 2626\n\nfrancis.ma@bernsteinsg.com\n\n![](images/dea3f61a1a3ad987bd649c80a97c4b021b071fe9bc85926d243b64ff373019d3.jpg)\n\nCarmine Milano, CFA\n\n+44 20 7762 1857\n\ncarmine.milan\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R033",
    "title": "Citi：中国新能源车市真正的拐点不是渗透率破60%，而是龙头集中度开始松动",
    "digest": "[wechat_article.md]\n# Citi：中国新能源车市真正的拐点不是渗透率破60%，而是龙头集中度开始松动\n\n中国新能源汽车市场五月销量数据出炉，渗透率首次稳稳站上61%。这个数字本身并不令人惊讶——市场早已预期2026年渗透率将突破60%大关。真正值得关注的信号，藏在Citi这份五月数据库更新中：CR5（前五大厂商集中度）在五月为57.0%，环比微增0.4个百分点，但同比下降了2.0个百分点。\n\n这不是一个简单的数字波动。它意味着，在渗透率快速攀升的“上半场”结束后，中国新能源车市正在进入一个没有历史参照的新阶段——头部阵营的份额不再单向扩张，而是出现了结构性松动。对于投资者和产业决策者而言，过去几年“买龙头就能分享行业增长”的简单逻辑，可能需要重新审视。\n\nCiti分析师Jeff Chung和Kyle Wu在报告中呈现的，远不止一份月度销量统计。它是一张正在变化的竞争版图，其中既有比亚迪的份额压力、新势力的分化加速，也有“第二梯队”玩家以超出预期的速度蚕食头部空间。这些信号叠加在一起，指向一个更深层的判断：市场真正低估的不是需求，而是供给侧竞争格局的再定价。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 渗透率突破六成之后，增长引擎从“增量红利”切换为“存量争夺”\n\n五月新能源乘用车批发销量135.2万辆，同比增长11%，环比增长10%。纯电动（BEV）批发88.6万辆，同比增速达到17%，环比14%；插电混动（PHEV）46.6万辆，同比仅增长1%，环比增长4%。前五个月累计新能源乘用车批发531万辆，同比增长1%。\n\n渗透率61.1%，同比提升8.4个百分点，环比提升3.0个百分点。这个数字放在全球任何主要汽车市场都是里程碑式的——中国新能源车已经不再是“替代者”，而是绝对主流。但Citi报告的数据也揭示了一个容易被忽视的事实：在\n\n[... middle omitted ...]\n\n报告的图表和更多行业数据，深入分析这些信号对投资决策的启示。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月新能源：渗透率突破61%\n\n新能源渗透率突破60%了\n\n5月数据很清晰，几个关键变化\n\n5月新能源乘用车批发135万辆，同比+11%，环比+10%。最值得关注的是渗透率来到61.1%，同比+8.4ppt，环比+3ppt。纯电增速明显好于插混：纯电同比+17%，插混仅+1%。\n\n1/ 头部集中度继续提升\nCR5市占率57%，环比+0.4ppt。比亚迪27.9%稳居第一，环比+2.2ppt。海鸥环比+47%到3.99万辆，表现亮眼。\n\n2/ 新势力分化明显\n蔚来同比+62%，环比+28%，乐道L90和L80合计贡献1万辆。零跑同比+81%，市占率6%创新高。理想同比-18%，L9环比+469%但其他主力车型下滑。\n\n3/ 特斯拉中国回暖\n5月销量8.6万辆，同比+39%，环比+8%。Model Y卖出5.48万辆，环比+5%。\n\n4/ 插混增速放缓\n纯电批发88.6万辆，插混46.6万辆。插混同比仅+1%，增速明显跑输纯电。\n\n从车型结构看，B级车市占率持续提升，A00级持续萎缩。研报判断纯电在中高端市场加速替代。\n\n你们觉得下半年哪家新势力能跑出来？\n\n#学习笔记\n\n[source_mineru.md]\n1\n\n[... middle omitted ...]\n\nesale volume of 377.0k units of sales, with +0% YoY/ +20% MoM and May market share -3.0ppt YoY/ +2.2ppt MoM to 27.9%. Song DM and Tai 7 PHEV saw +15%/+0% MoM to 62.1k/17.0k units, Dolphin +2% \n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R034",
    "title": "GS：鲜零食零售的兴起不是威胁，而是价值零售龙头品类升级的催化剂",
    "digest": "[wechat_article.md]\n# GS：鲜零食零售的兴起不是威胁，而是价值零售龙头品类升级的催化剂\n\n中国消费市场从来不缺新概念。2025年至今，鲜零食零售连锁以200多家门店、十余个新品牌的速度集中涌现，日销超过10万元、毛利率30%以上、EBITDA利润率达到两位数——这些数字让市场再次兴奋，也带来了一个自然的问题：这对已经跑通模型的食品饮料价值零售商（如鸣鸣很忙、万辰）意味着什么？\n\nGS最新发布的研报给出了一个清晰且反直觉的判断：鲜零食零售的崛起，非但不是对现有价值零售龙头的威胁，反而为它们提供了品类扩张、店型升级和竞争壁垒加固的三重机遇。市场如果只看到“新业态抢流量”，就低估了规模龙头在供应链密度、运营系统和会员资产上的结构性优势。\n\n这份报告的价值不在于罗列几个新品牌的数据，而在于它提供了一个分析框架：当消费零售行业出现新物种时，如何判断它是颠覆者还是催化剂。以下是我们从报告中提炼出的三个核心层次。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 鲜零食零售证明了零食消费的韧性，但真正的变量是“高频复购”和“单店天花板”\n\nGS报告的第一个洞察是：鲜零食零售的繁荣，首先验证了零食消费的基本盘依然强劲。这不是零和博弈，而是品类边界的扩展。\n\n从数据看，鲜零食零售的店效模型确实令人印象深刻。以头部品牌金粒门为例，其旗舰店年化GMV可达2400万至4800万元，日均订单量在1300至2600单之间，客单价约50元。相比之下，鸣鸣很忙和万辰的典型门店年化GMV约在500万元左右，日均订单约400至500单，客单价约31元。鲜零食门店的坪效（每平米销售额）达到8万至12万元，是价值零售门店（约3.6万元）的两到三倍。\n\n但更值得关注的不是绝对值，而是驱动这些数字的底层逻辑。GS指出，鲜零食零售的核心优势在于两个维度：\n\n第一，高频复购。鲜零食\n\n[... middle omitted ...]\n\n、价值零售龙头的品类试验进展，以及UE模型的变化。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n鲜食集合店，零食赛道新变量\n\n新零食店正在跑出\n\n最近一批鲜食集合店（卖现做糕点/卤味/坚果/饮品）在2025年集中冒头，单店日销能到10万+，毛利率30%+。它们跟零食量贩店（比如鸣鸣/万辰）有什么关系？投行研报拆了三个关键点：\n\n1️⃣ 品类扩容：鲜食拉高复购天花板\n鲜食比包装零食天然更容易触发高频购买（早餐/夜宵/囤货），单店销售额上限更高。鸣鸣已经在试烤蛋挞和热狗肠，2H25开始拉动单店GMV。但短保品对供应链和周转要求更高，差异化是关键。\n\n2️⃣ 店型进化：从开店数量到店型升级\n头部玩家已经在试冷鲜品、便利店/折扣超市等新店型。鲜食店大店（200-400平）靠高客流+高坪效（旗舰店年化GMV可达2000-5000万），是量贩店未来形态的好实验场。\n\n3️⃣ 竞争格局：短期不构成威胁\n鲜食店SKU少（几百到1000+）、人工密集、对位置和冷链要求高，下沉和加盟难度大。但头部量贩店（鸣鸣/万辰）凭借网络密度、供应链和会员体系，做短保反而能放大优势。\n\n#学习笔记\n\n[source_mineru.md]\n## CHINA STAPLES\n\n# Value Retailers: Our three key\n\n[... middle omitted ...]\n\n up to Rmb100k+)/robust margin (30%+ GPM/teens% EBITDA margin, Exhibit 4/Exhibit 6) of fresh snacks retailers reinforces that consumer demand for snacks and beverages remains robust driven by \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R035",
    "title": "GS：IP零售的“高基数疲劳”正在重塑市场对增长的定价逻辑",
    "digest": "[wechat_article.md]\n# GS：IP零售的“高基数疲劳”正在重塑市场对增长的定价逻辑\n\n当市场还在为潮玩IP的爆发力欢呼时，一份来自GS的月度追踪报告揭示了一个更微妙的信号：中国IP零售的核心玩家正在经历“高基数疲劳”。这不是简单的增速放缓，而是增长引擎从“流量红利”切换到“IP运营能力”的关键转折点。\n\n这份5月更新的报告覆盖了泡泡玛特、名创优品和布鲁可三家代表性公司。数据显示，泡泡玛特国内线上销售额同比增长29%，但相比4月的95%明显减速；名创优品线上增速从一季度的43%降至5月的21%；布鲁可虽然在加速推新，但2季度至今的线上增速仍低于一季度。这些数字单独看并不差，但放在一起，它们指向一个共同问题：IP零售的增长故事正在进入新阶段，市场需要更精细的观察框架。\n\n更值得关注的是，GS在海外市场也捕捉到了类似信号。泡泡玛特美国市场5月信用卡销售同比下降36%，虽然较4月的43%降幅有所收窄，但2季度至今仍维持约40%的同比下滑。名创优品美国市场增速虽从4月的19%回升至5月的31%，但2季度累计增速仍低于一季度。这些数据意味着，即使在中国IP零售商的海外扩张故事中，基数效应和消费者情绪波动正在成为不可忽视的变量。\n\n对于决策者而言，现在需要回答的核心问题不是“IP零售是否还有增长空间”，而是“下一阶段的增长来自哪里，以及哪些公司具备穿越周期的能力”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 泡泡玛特的减速不是需求问题，而是供给节奏与基数效应的双重挤压\n\nGS报告中最引人注目的数据是泡泡玛特国内线上增速从4月的95%骤降至5月的29%。这个数字本身已经足够说明问题，但背后的结构性原因更值得深究。\n\n从供给端看，5月的新品表现明显弱于此前。GS追踪显示，5月推出的“Dear Birds”多IP系列在抖音和天猫的首月销量分别超过3\n\n[... middle omitted ...]\n\n指数与潮玩消费的相关性，以及IP零售公司估值框架的调整方向。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n泡泡玛特5月线上增速放缓，名创优品加速IP上新\n\n封面：IP零售5月速览\n\n副标题：Labubu热度边际走弱，关注世界杯催化\n\n**泡泡玛特：国内线上增速放缓，海外美国市场仍在磨底**\n\n5月天猫+抖音合计线上销售同比+29%，相比4月的+95%明显回落，主因基数走高。抖音端6月至今的销售节奏环比5月也在走弱，且面临去年6月Labubu“大闹”系列高基数压力。\n\n美国市场5月同比-36%（4月为-43%），低基数略有改善，但6月起基数压力会重新加大。信用卡跟踪数据显示2Q至今仍为约-40%的同比下滑（1Q为低个位数正增长）。二级市场溢价率和谷歌热度在5月也未看到IP势能的显著回升。\n\n新品表现分化：Crybaby和Hacipupu的新毛绒系列未在首发日售罄；Zsiga新品在抖音已售罄。Dear Birds多IP系列首发表现相对平淡，截至6月8日仍可购买，而此前“Have a good run”系列首月抖音销量超20万件。\n\n**名创优品：IP上新节奏持续加快，国内五一表现亮眼**\n\n5月-6月初持续快速上新IP，包括自有IP Yoyo、电影IP（星球大战、玩具总动员）及热门IP Chiikawa x Sanr\n\n[... middle omitted ...]\n\nine (-36% yoy) slightly narrowed vs Apr (-43% yoy) thanks to an easier prior-year base; however, the comparison base will become more challenging heading into June. 2Q-to-date credit card sale\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R036",
    "title": "JPM：AI驱动的半导体超级周期才刚刚进入第二阶段",
    "digest": "[wechat_article.md]\n# JPM：AI驱动的半导体超级周期才刚刚进入第二阶段\n\n2026年4月的全球半导体销售数据，让市场上大多数关于“周期见顶”的讨论显得为时过早。JPM最新发布的亚洲半导体行业报告显示，当月整体半导体营收同比增长106%，这是自1994年以来的最高增速，也是连续第八个月加速。这个数字本身已经足够震撼，但真正值得决策者关注的，不是增速本身，而是支撑这一增速的结构性力量正在从“单一引擎”切换为“多引擎驱动”。\n\n这份报告的核心判断是：市场对AI半导体的定价逻辑仍停留在“需求爆发”的第一阶段，但供给侧的硬约束——尤其是先进制程和HBM的产能瓶颈——正在成为未来2-3年更关键的定价因子。这意味着，当前的营收增长不是周期性的脉冲，而是结构性供需失衡的早期信号。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 四月数据揭示的不仅是增速，更是增长结构的质变\n\n整体半导体营收同比增长106%，其中逻辑半导体增长33%，存储器增长359%。这些数字的含金量在于它们的“广度”。JPM指出，4月半导体出货量同比增长15%，较3月的10%明显加速，说明增长不再仅仅依赖价格提升，而是有实实在在的出货量支撑。ASP同比上涨79%，其中存储器ASP飙升198%，逻辑ASP上涨18%。\n\n更深层的信号在于增长的“去集中化”。虽然AI加速器仍然是核心驱动力，但报告明确提到，逻辑半导体的增长已经扩展到服务器CPU、网络芯片，以及苹果iPhone/Mac产品线的持续需求。这意味着，AI对半导体的拉动正在从数据中心内部向外溢出，进入终端设备和基础设施层面。\n\n对于产业观察者而言，这意味着一个关键判断：如果AI半导体的需求来源变得更加分散，那么单一客户或单一应用的订单波动对整体产业链的冲击力将显著下降。这是行业进入更稳定增长阶段的前提条件。\n\n![研报原图 \n\n[... middle omitted ...]\n\n对产业链的深远影响，以及HBM定价博弈中可能出现的二阶效应。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n4月半导体数据：增速创30年新高\n\n📈 半导体增长加速\n\n4月全球半导体收入同比增长106%，是1994年以来最高增速。逻辑芯片+33%，存储芯片更是暴涨+359%。连续8个月加速，背后两大推手：AI算力需求持续爆发，存储芯片供应紧张推动价格上涨。\n\n🔍 核心观察\n\n1️⃣ 先进制程产能吃紧\nN3/N5工艺需求强劲，GPU、服务器CPU、苹果产品都在抢产能。研报预计N3将成为AI加速器的主要瓶颈，2026年供需缺口约60万片晶圆，对应150-180亿美元代工收入。\n\n2️⃣ 存储芯片结构性紧缺\nHBM占DRAM晶圆产能比例将从2026年的24%升至2028年的31%，未来三年HBM需求年复合增长85%。存储芯片价格今年预计上涨220-250%，明年在长期合约支撑下走势趋稳。\n\n3️⃣ 需求基础更广\n除了AI主线，工业领域出现复苏信号，AI周边芯片（PMIC等）需求旺盛。苹果iPhone 17在中国市场份额提升，MacBook Neo受到关注，抵消了中低端手机疲软。\n\n🎯 展望\n研报认为AI驱动的半导体上行周期至少延续到2026年，先进制程产能紧张可能持续到2027-2028年。美国四大云服务商2026年资本开\n\n[... middle omitted ...]\n\nid persistently tight supply conditions. Memory growth was driven by CSP-led demand across both HBM and conventional memory, with suppliers continuing to prioritize HBM allocation.\n\n- Logic se\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 10 Jun 2026 01:32 PM HKT\n\nDisseminated 10 Jun 2026 01:35 PM HKT"
  },
  {
    "id": "R037",
    "title": "摩根斯坦利：AI需求的结构性韧性正在重塑台湾科技股的定价逻辑",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：AI需求的结构性韧性正在重塑台湾科技股的定价逻辑\n\n五月营收数据出炉，台湾科技板块整体同比增长39%，环比增长4%，表面上是AI需求持续抵消消费电子季节性疲软的又一个佐证。但这份摩根斯坦利研报真正值得关注的信号，不是总量增长本身，而是增长质量的分化：数据中心硬件和智能手机供应链超出预期，而IC代工全线miss。这意味着市场此前对AI溢价的定价逻辑可能需要重新校准——真正受益的不是所有与AI沾边的环节，而是那些具备订单可见性优势或产业链议价权的公司。\n\n这份报告发布后，台湾加权指数和相关科技股已累计上涨11%，但摩根斯坦利的推荐清单却高度集中：MediaTek、Macronix、Delta、Bizlink、Accton、Wiwynn、Yageo、Zhen Ding。这八只股票的共同特征，并非同属AI赛道，而是各自在供应链中拥有不可替代的位置或清晰的订单能见度。换言之，市场正在从一个“AI概念普涨”的阶段，进入一个“AI业绩必须兑现”的阶段。\n\n以下是我们从这份研报中提炼出的五个核心洞察，以及一个报告尚未完全回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. IC代工集体miss揭示的不是需求问题，而是产能定价权的再分配\n\n五月营收中，IC代工板块成为最突出的低于预期区域。台积电、联电、世界先进、力积电等主要代工厂无一例外地miss了市场预期，其中台积电5月营收416,975百万新台币，低于预期的451,798百万新台币，miss幅度达8%。联电同样miss 6%，世界先进miss 2%，力积电是唯一beat的例外，但幅度仅有2%。\n\n这些数据合在一起意味着什么？不是AI需求减弱了，而是代工环节的产能紧张程度正在缓解。台积电的miss尤其值得关注——作为全球最先进的制程供应商，其营收连续低\n\n[... middle omitted ...]\n\n评级和价格目标。欢迎加入，一起追踪AI产业链的业绩兑现节奏。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n台湾科技5月营收：AI撑住全场，消费电子拖后腿\n\nAI需求扛大旗\n\n台湾科技公司5月营收出炉，环比+4%、同比+39%，数据亮眼。AI需求持续强劲，成功抵消了消费电子淡季的疲软。\n\n数据中心硬件和手机供应链表现超预期，但IC代工板块低于预期。\n\n1️⃣ 数据中心硬件\nAI服务器、交换机需求依然旺盛，Accton、Gold Circuit、KingSlide等5月营收都超预期。KingSlide环比暴增46%，同比+172%。\n\n2️⃣ 手机供应链\n鸿海5月营收8594亿新台币，同比+40%，超预期。Zhen Ding、Yageo也交出beat成绩单。\n\n3️⃣ IC代工\n台积电、联电、世界先进、力积电等营收均低于预期。只有力积电beat，环比+14%、同比+59%。\n\n4️⃣ 存储芯片\nNanya、Macronix、Winbond营收同比暴增（730%/176%/182%），但也都miss预期。\n\n研报偏好订单能见度高的个股：联发科、Macronix、台达电、Bizlink、Accton、Wiwynn、国巨、臻鼎-KY。\n\n5月4日以来，台湾科技股和台股大盘已同步上涨11%。\n\n大家觉得下半年AI需求还能维持\n\n[... middle omitted ...]\n\nWAN LIMITED+\n\n## Sharon Shih\n\nEquity Analyst\n\nSharon.Shih@morganstanley.com +886 2 2730-2865\n\n## Charlie Chan\n\nEquity Analyst\n\nCharlie.Chan@morganstanley.com +886 2 2730-1725\n\n## Daniel Yen, C\n\n[... middle omitted ...]\n\ny Co Ltd (6515.TW)</td><td>O (04/17/2026)</td><td>NT$8,125.00</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R038",
    "title": "摩根斯坦利：大宗商品周期的分化正在重塑中国消费股的盈利格局",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：大宗商品周期的分化正在重塑中国消费股的盈利格局\n\n大宗商品价格从来不是消费股投资的核心叙事——直到它开始系统性地改变利润表的每一个科目。\n\n这份摩根斯坦利在5月底发布的原材料价格图鉴，表面上是一张月度商品价格追踪表，但真正值得决策者关注的，不是锡涨了还是铜跌了，而是一个更结构性的信号：中国消费行业正在经历一轮“成本端的分化式出清”。上游价格不再同步涨跌，而是沿着各自供需逻辑走向截然不同的方向。这种分化，正在把一批公司推入利润修复通道，同时让另一批公司面临被成本压垮的风险。\n\n市场目前的定价，更多聚焦在需求端的弱复苏上，对成本端正在发生的结构性变化定价不足。这正是这份报告最值得细读的地方。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 原奶价格企稳的信号，比表面看起来重要得多\n\n原奶价格在5月环比微涨0.2%，全年累计下跌约1%。这个数字本身并不惊艳，但结合供给端的减产趋势，意义完全不同。\n\n报告明确指出，上游供给削减后，原奶价格已经趋于稳定，并预计2026年将逐步回升。这意味着持续了两年的原奶成本下行周期正在接近尾声。对于伊利和蒙牛这两家龙头来说，这既是挑战也是机会。\n\n挑战在于，成本上升将压缩低端产品的利润空间。但机会在于，原奶价格上涨会加速中小乳企的退出。伊利和蒙牛均将2026年液态奶恢复增长作为目标，并预期在原奶价格回升过程中，能从中小玩家手中夺取市场份额。\n\n更重要的是，报告提到“2026年存货拨备将大幅减少”。过去两年，原奶价格持续下跌导致乳企面临大量存货减值压力，这部分非经营性损失严重拖累了净利润。一旦存货拨备压力消退，净利率的修复弹性可能超出市场预期。\n\n这里的关键判断是：原奶价格企稳不是一个简单的成本拐点，而是一个行业竞争格局的转折点——成本下行期是中小企业的“续命期”，成本上行期\n\n[... middle omitted ...]\n\n及对最新价格数据的实时追踪。\n\n欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n标题：原料价格波动，消费股谁受益？\n\n封面短标题：消费原料价格图鉴\n\n封面副标题：看懂原料走势，拆解消费股逻辑\n\n---\n\n最近某外资投行发布了一份中国消费行业原料价格图鉴，信息量很大，直接关系到乳业、肉制品、饮料、啤酒等多个板块的成本和利润。\n\n原料价格涨跌背后，哪些公司可能承压，哪些反而有机会？我提炼了几个关键逻辑，分享给大家。\n\n**1️⃣ 乳业：原奶价格趋稳，利好龙头**\n*   研报判断，原奶价格预计在2026年逐步企稳，供需更趋平衡。\n*   伊利和蒙牛都计划在2026年恢复液态奶增长，并有望凭借成本优势抢占小品牌份额。\n*   更重要的是，2026年库存减值准备大概率大幅减少，直接利好净利率。\n\n**2️⃣ 肉制品：成本分化，各有看点**\n*   **双汇发展**：中国生猪价格走低，降低了包装肉的成本，这块业务回报有望保持高位。美国业务则受益于持续的高猪价，下游产品组合和运营效率也在改善。\n*   **牧原股份**：虽然短期盈利承压，但猪价持续下跌会加速行业产能出清，预计2026年中迎来价格拐点。作为行业龙头，猪价反弹时弹性最大。\n\n**3️⃣ 饮料：PET成本锁定的优势**\n*   **东鹏饮\n\n[... middle omitted ...]\n\nt market share gains from smaller players amid potential recovery of raw milk prices. On the other hand, provisions for inventory will likely be largely reduced in 2026, which should benefit n\n\n[... middle omitted ...]\n\nstrial Hldg (0551.HK)</td><td>E (09/14/2021)</td><td>HK$14.06</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R039",
    "title": "Bernstein：人形机器人真正的竞争壁垒不是技术，而是分化能力",
    "digest": "[wechat_article.md]\n# Bernstein：人形机器人真正的竞争壁垒不是技术，而是分化能力\n\n人形机器人赛道正在经历一场奇特的拥挤。超过150家玩家挤满了供应链的每一个环节，而且这个名单每个月都在变长。按照常规逻辑，这指向一个低门槛市场，不值得严肃对待。但Bernstein这份研报给出了一个截然相反的判断：真正的问题不是“进入门槛”，而是“分化空间”。走进人形机器人这扇门很容易，但门后的房间天花板极高。\n\n这份报告以四个角色——科学家、发明家、工程师、园丁——构建了一套极为精炼的竞争分化框架。它不是在罗列哪家公司做了什么事，而是在回答一个更本质的问题：在这个产业从实验室走向商业化的过程中，什么样的能力结构才能让一家企业不被淹没，反而在拥挤中建立起真正的护城河。\n\n我们需要认真对待这个框架，因为它揭示了一个反直觉的事实：人形机器人产业最稀缺的资源，不是某个单一技术突破，而是同时驾驭多种角色的能力。而这恰恰是当前市场定价中尚未被充分认知的部分。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 产业拥挤不是信号，真正值得关注的是谁在拥挤中拥有“多角色”能力\n\n超过150家玩家的存在，让很多人得出“门槛太低”的判断。但Bernstein的分析框架告诉我们，这恰恰是理解产业竞争格局的起点，而非终点。\n\n科学家、发明家、工程师、园丁——这四个角色分别对应四种截然不同的能力。科学家负责探索未知，解决“大脑模型”这类前沿科学问题；发明家负责将功能需求转化为形态设计和技术规格，赋予机器人“小脑”的运动能力；工程师负责把部件做得更好更便宜，在技术原理已被业界掌握的前提下追求极致的精度、强度、可靠性；园丁则负责构建生态，成为产业链各类参与者的引力中心。\n\n关键洞察在于：大多数玩家只能胜任其中一个角色。而真正具备投资价值的公司，往往是那些能够身兼多角的选手。\n\n[... middle omitted ...]\n\n和数据才能深入展开，也是当前公开信息中最值得持续跟踪的部分。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n人形机器人赛道，谁才是赢家？\n\n人形机器人，不只是组装\n\n1. 门槛低，但天花板高\n人形机器人赛道已有超过150个玩家，且每月都在增加。这说明进入门槛不高。但关键不是“门槛”，而是“差异化空间”——门好进，但门后的房间天花板极高。\n\n2. 四种角色，四种竞争力\n研报用了一个很妙的比喻：走进这个房间的，有科学家、发明家、工程师和园丁。\n\n- 科学家：研究机器人“大脑”，比如VLA模型、世界模型。这是最前沿的领域，目前还在探索中，隧道很长但已有光。\n- 发明家：设计机器人形态，从双腿到轮式，甚至八臂。他把功能需求转化为硬件规格，平衡通用性和性能。\n- 工程师：把组件做得更好更便宜。精度、强度、可靠性、重量、能效……每一个维度都是竞争点。\n- 园丁：构建生态，整合技能包、数据、部署。他站在中心，让其他玩家围绕自己生长。\n\n3. 谁更有优势？\n研报认为，机器人整机厂（OEM）比零部件供应商更有结构性优势。因为整机厂可以同时扮演多种角色——既是发明家，也是工程师，甚至自己开发大脑模型。最好的整机厂，已经开始成为生态中心。\n\n比如发那科（FANUC），既是发明家，也在做园丁，与英伟达、谷歌合作。基恩士（Keyence）则\n\n[... middle omitted ...]\n\n-- in this magnificent place called humanoid robotics, it is easy to enter the door, but through that door is a room with a very high ceiling.\n\nWalking into this room are a scientist, an inven\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R040",
    "title": "JPM：AI服务器与PC的背离正在重塑台湾ODM的投资逻辑",
    "digest": "[wechat_article.md]\n# JPM：AI服务器与PC的背离正在重塑台湾ODM的投资逻辑\n\n市场对台湾ODM板块的关注，往往停留在“AI服务器高增长”这一单一叙事上。但JPM最新发布的5月营收追踪报告揭示了一个更复杂的图景：AI服务器确实在加速，但传统服务器、PC、VGA/主板等板块已经出现了明显的需求分化和利润压力。这份报告的真正价值，不在于确认AI服务器的景气度——这已是共识——而在于量化了非AI业务的疲软程度，并指出了哪些公司的产品组合将在这种背离中受益或承压。\n\n对于产业决策者和投资者而言，当前的关键问题不是“AI服务器还能涨多少”，而是“当PC和传统硬件的利润开始收缩时，哪些公司的估值安全垫足够厚”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI服务器出货量正在加速，但3季度可能出现短暂空窗期\n\nJPM对NVL72机架出货量的追踪显示，2026年全年出货量预估为65,000至70,000台，其中2季度单季出货量预计达到19,000台，较1季度的17,000台环比增长约12%。这一增长主要由GB300的持续放量驱动，5月数据显示出货节奏符合预期。\n\n但报告也提示了一个潜在隐患：由于产品从GB300向VR200的过渡，3季度可能出现“air pockets”（出货空窗期）。VR200系统的正式放量预计要到4季度才会开始。这意味着，AI服务器供应链在3季度的环比增速可能阶段性放缓，而这对于已经将高增长预期计入股价的公司而言，是一个需要警惕的短期风险。\n\n更值得关注的是AWS ASIC服务器（Trainium 3项目）的进展。JPM在5月观察到组件拉货需求开始启动，包括服务器滑轨、电源、机箱、CCL/PCB等环节，并预计6月开始系统级出货。这对Wiwynn（纬颖）而言是明确的正面信号，因为ASIC服务器正是其差异化竞争的核心领域。\n\n[... middle omitted ...]\n\n在机会，并探讨HVDC渗透率假设变化对供应链定价的潜在影响。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n服务器五月成绩单：AI撑场，PC承压\n\n📊 五月数据看点\n\n**1. AI服务器：持续高景气**\n- GB300 持续出货，NVL72 机柜Q2预估出货1.9万台，环比双位数增长\n- AWS ASIC（Trainium 3）组件拉货启动，6月系统开始爬坡\n- 全年NVL72机柜出货预计6.5-7万台\n\n**2. 通用服务器：需求稳健**\n- 五月持续增长，Q2环比双位数增长\n- 全年传统服务器出货预计同比+20%\n- 供应链反馈下半年动能更强，CPU供应改善\n\n**3. PC：需求疲软，下半年更弱**\n- 五月NB ODM出货环比微增，Q2环比持平或微增\n- 下半年预计环比下滑，全年1H/2H比例约55%/45%\n- 价格弹性效应拖累，PC品牌利润率面临压力\n\n**4. 主板/显卡：双位数下滑**\n- 微星Q2主板显卡出货同比/环比均双位数下降\n- 下半年持续疲软，缺乏新品驱动\n- 微星、华硕PC组件营收占比40-50%/20%，影响较大\n\n**5. iPhone：短期强劲，下半年谨慎**\n- 鸿海/和硕五月营收超季节，受618备货和份额提升推动\n- 但下半年iPhone EMS组装预计同比-7%（上半年+9\n\n[... middle omitted ...]\n\ndragged by price elasticity impact. VGA/MB shipments appear to be down double digit % QoQ/YoY in 2Q26 and likely to see continued weakness into 2H26, due to a lack of new product and end deman\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 10 Jun 2026 10:51 PM HKT\n\nDisseminated 10 Jun 2026 10:51 PM HKT"
  },
  {
    "id": "R041",
    "title": "摩根斯坦利：中国机场股的核心问题不是客流，而是盈利结构尚未完成重置",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：中国机场股的核心问题不是客流，而是盈利结构尚未完成重置\n\n市场对机场股的关注点长期停留在“客流恢复”这一个维度上。但摩根斯坦利在2026年6月发布的最新研报中，提出了一个更令人不安的判断：即便客流数据看起来尚可，中国三大机场的盈利修复路径已经因为三个结构性因素而显著偏离了市场预期。\n\n这份研报不是简单的行业更新，它实际上是在重新定价中国机场资产的估值逻辑。摩根斯坦利同时下调了三大机场的目标价，降幅均达到40%左右，并将广州白云机场的评级从“持有”直接下调至“减持”。背后的核心逻辑是：市场正在低估能源冲击对客流的持续压制、免税业务转型期的收入真空，以及新产能投产后成本分担机制的不确定性。\n\n这不是一个“等待反转”的故事。这是一个盈利结构需要被重新审视的时刻。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 能源冲击正在重塑出行结构，航空客流的增长拐点尚未到来\n\n摩根斯坦利的数据显示，中国航空客运量自2026年4月以来明显承压，直接原因是全球能源价格飙升推高了机票价格。四月全国航空客运量同比仅增长0.4%，其中国内航线甚至出现了0.2%的同比下滑。这个数字与一季度6.5%的增速相比，是一个急剧的减速。\n\n更关键的信号出现在出行方式的替代上。铁路客运量在同期加速增长，四月同比增速达到10.5%，而一季度仅为5.5%。摩根斯坦利明确指出，这是旅客从航空向铁路转移的明确证据。五一假期的数据进一步印证了这一趋势：航空客运量同比下降5.7%，而铁路客运量同比增长4.6%。\n\n对于机场股来说，这意味着客流量增长的基本面正在被侵蚀。上海机场、白云机场和首都机场的国内客运增速从一季度的6%至10%，全面放缓至四月的3%至4%。国际航线同样未能幸免，增速从一季度的7%至24%回落至四月的4%至18%。其中上海机场表现最弱\n\n[... middle omitted ...]\n\n根斯坦利这份报告的核心假设，逐一拆解其对资产定价的深层含义。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国机场板块，还在等风来\n\n三大机场都在过“苦日子”\n\n最近看了份外资投行对中国三大机场的研报，信息量很大，简单拆解一下。\n\n1️⃣ 客流增长被能源成本“卡脖子”\n- 从4月开始，航空旅客增速明显放缓，三大机场国内客流从Q1的6-10%降到3-4%\n- 高铁抢走了不少乘客，4月铁路客流增速10.5%，航空只有0.4%\n- 上海机场受日本航线拖累，表现最弱\n\n2️⃣ 免税业务还在“换挡期”\n- 虽然去年12月签了新合同，机场议价能力变强了\n- 但新运营商需要时间铺货，上海机场还有3个月免租期\n- Q1上海机场免税租金直接腰斩，同比下降49%\n- 不过人均免税消费可能已经见底，中长期有望改善\n\n3️⃣ 白云机场压力最大\n- 新产能成本分摊方案还没敲定，T1又要关闭装修\n- 能源成本高企抑制出行需求，新航站楼带来的增量收入被抵消\n- 研报认为盈利恢复会比预期慢很多\n\n整体来看，三大机场都面临客流放缓+免税承压的双重挑战，短期难有明显改善。\n\n你们觉得机场股的拐点会在什么时候出现？欢迎一起讨论。\n\n#学习笔记\n\n[source_mineru.md]\n# Chinese Airports | Asia Pacific\n\n[... middle omitted ...]\n\nwed to $3 - 4\\%$ YoY in Apr-26 from $6 - 10\\%$ YoY in 1Q26. Non-domestic traffic growth also softened to $4 - 18\\%$ YoY in Apr-26 from $7 - 24\\%$ YoY in 1Q26. SIAC underperformed likely due to\n\n[... middle omitted ...]\n\ning Co Ltd (002120.SZ)</td><td>U (07/29/2020)</td><td>Rmb6.57</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R042",
    "title": "摩根斯坦利：市场低估了eBay和Etsy在智能体电商时代的独特优势",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：市场低估了eBay和Etsy在智能体电商时代的独特优势\n\n智能体电商（Agentic Commerce）正在从概念走向落地。当行业焦点集中在亚马逊和沃尔玛如何应对这一变革时，摩根斯坦利的最新研报给出了一个反直觉的判断：在中小市值电商领域，被市场长期视为“结构性输家”的eBay和Etsy，实际上拥有被低估的结构性优势。\n\n这份报告的核心洞察并非简单的“买入建议”，而是一个关于资产重新定价的框架。市场对这两家公司的定价，仍然停留在关键词搜索时代的竞争逻辑中，而智能体电商的范式转换，将重新定义哪些资产真正稀缺、哪些商业模式真正具备防御性。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 智能体电商不是技术升级，而是竞争逻辑的重置\n\n摩根斯坦利提出的“5I框架”——Inventory（库存）、Infrastructure（基础设施）、Innovation（创新）、Incrementality（增量空间）、Income Statement Impact（损益影响）——本质上是在回答一个根本问题：当消费者从“搜索关键词”转向“对话式购物助手”时，什么才是真正的护城河？\n\n传统电商的竞争逻辑建立在流量获取和转化效率上。谁能在搜索结果页获得更高排名，谁就能获得更多订单。这种逻辑下，亚马逊凭借规模效应和履约网络占据了绝对优势。但智能体电商改变了游戏规则：购物助手不再只是匹配关键词，而是理解意图、比较价格、发现长尾商品。\n\n这意味着，库存的独特性和定价优势，将比配送速度更成为竞争的关键变量。而恰恰在这两点上，eBay和Etsy拥有亚马逊无法复制的结构性优势。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. eBay的库存护城河：90%的独特库存，是智能体电商时代的稀缺资产\n\n[... middle omitted ...]\n\n，哪些最可能受益，以及我们如何建立自己的评估框架。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\neBay和Etsy在AI时代被低估了？\n\n**封面标题：** AI购物时代\n**副标题：** 谁才是真正的赢家？\n\n最近读到一份某外资投行的研报，专门分析了eBay和Etsy在“智能体购物”时代的潜力。简单来说，就是AI帮你买东西的时代要来了，这两家老牌电商平台反而可能迎来新机会。\n\n**1/ eBay：被低估的“库存护城河”**\n\n研报认为，eBay最大的优势是它的库存——约25亿件商品中，90%是二手或过季品。这种“非标品”在传统搜索里很难被找到，但AI智能体可以精准匹配。\n\n- **价格优势**：二手货天然便宜，AI比价时eBay排名会靠前。\n- **降低卖家门槛**：AI能帮卖家自动填写商品信息，据说新工具让上架时间缩短25%，卖家GMV提升两位数。\n- **结果**：研报预测，在乐观场景下，eBay的2030年GMV和EBITDA可能比基准高出26%和30%。\n\n**2/ Etsy：短期有机会，长期有风险**\n\nEtsy的情况更复杂。它的优势是“礼物场景”和“非标品”，AI对话式搜索能帮用户更精准地找到“给妈妈的礼物”，提高转化率。\n\n- **短期机会**：研报测算，每个买家多花5美元，Etsy的GMV\n\n[... middle omitted ...]\n\ne; our favorite name in SMID eCommerce  \n- ETSY (EW \\$64 PT): Although there are clear long-term risks, we see a more compelling medium-term opportunity that could drive GMS growth and lead to\n\n[... middle omitted ...]\n\nnternational Inc (WW.O)</td><td>E (08/01/2025)</td><td>$18.47</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R043",
    "title": "摩根斯坦利：印度钢铁的强势周期远未结束，但真正值得关注的是供给侧的再定价",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：印度钢铁的强势周期远未结束，但真正值得关注的是供给侧的再定价\n\n当一家投行在Sensex指数年内下跌约13%的背景下，其覆盖的钢铁股却逆势上涨约12%，这本身就值得每一个产业决策者和资产配置者停下来问一句：这轮上涨的驱动力到底是什么？是短期季节性需求的脉冲，还是某种更深层的结构性变化？\n\n摩根斯坦利最新发布的印度材料行业研报给出了一个明确的判断：印度钢铁的强势周期尚未结束。但真正值得深入解读的，不是“继续看好”这个结论本身，而是支撑这个结论的三个结构性支柱——本地化政策护城河、中国供给侧的外溢效应、以及全球地缘冲突下的成本传导机制。这三者叠加，正在重塑印度钢铁行业的定价逻辑，而市场对此的定价可能仍然不够充分。\n\n这份报告发布于2026年6月，正值印度季风季节来临前的传统需求淡季。国内热轧卷（HRC）价格从4月高点回落约11%，市场情绪出现分化。正是在这个看似需要谨慎的时点，摩根斯坦利选择上调多家钢铁公司的盈利预测和目标价。这种逆势判断背后，是对行业中期格局的重新审视。\n\n以下是我们从这份报告中提炼出的五个关键洞察，以及一个报告尚未完全回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮上涨的核心不是需求爆发，而是供给侧的多重锁定\n\n市场习惯用需求侧的逻辑来理解钢铁股——基建投资、制造业扩张、房地产复苏。但摩根斯坦利这份报告传递的核心信号是：这轮钢铁股表现优异的根本原因，是供给侧正在经历一次罕见的、多重力量叠加的锁定。\n\n首先是印度本地的贸易保护措施。报告明确指出，保障性关税的延期是支撑国内HRC价格从去年12月中旬低点反弹约26%的关键因素。这不是一个临时性的政策工具，而是印度政府在“印度制造”战略下持续推进的产业本地化政策的延续。\n\n其次是中国的中期“反内卷”主题。中国的钢铁出口\n\n[... middle omitted ...]\n\n更多投行的观点和产业数据，帮助社群成员构建更完整的判断框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n印度钢铁股：雨季扰动后，还有第二波？\n\n封面：钢铁周期未结束\n副标题：雨季过后，价差有望再次走阔\n\n最近印度钢铁板块表现很亮眼，年初至今涨了约12%，而同期大盘Sensex跌了13%。某外资投行认为，这个强势周期还没结束。\n\n1/ 价差承压是季节性的\n国内热轧卷价格从12月中旬低点反弹了26%，最近回落约11%，主要是雨季需求偏弱。目前国内HRC比进口平价低约8%。等雨季结束，需求回暖，价差有望重新走阔。\n\n2/ 中东冲突影响有限\n虽然炸药和物流成本上升，但印度钢铁厂的原料采购基本不依赖中东，直接冲击较小。不过如果冲突持续，下游行业可能承压，需要留意。\n\n3/ 中国“反内卷”是中期支撑\n中国钢铁出口近期因中东冲突和国内需求偏弱有所放缓，但中期来看，中国钢铁行业去产能、减量发展的方向对全球钢价是结构性支撑。\n\n该行上调了印度HRC价格假设，F27年钢铁价差预测上调约2%。看好JSW Steel、Jindal Steel、Tata Steel，对SAIL持谨慎态度。\n\n大家觉得雨季后的钢价反弹力度会如何？欢迎一起讨论。\n\n#学习笔记\n\n[source_mineru.md]\n## India Materials |\n\n[... middle omitted ...]\n\nin our coverage rose \\~12% YTD (market cap-weighted), while the Sensex declined \\~13% (vs. +27% for steel and \\~9% for the Sensex in 2025).\n\nWe believe this strong performance cycle is not yet\n\n[... middle omitted ...]\n\nment Ltd (ULTC.NS)</td><td>O (06/02/2022)</td><td>Rs10,866.00</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R044",
    "title": "NOM：光器件供应链的瓶颈不在产能，而在核心衬底的锁定能力",
    "digest": "[wechat_article.md]\n# NOM：光器件供应链的瓶颈不在产能，而在核心衬底的锁定能力\n\n当市场还在讨论AI算力需求对光模块出货量的拉动时，一个更根本的约束正在浮出水面：光器件的核心原材料——磷化铟（InP）衬底——已经进入实质性紧缺阶段。这不是一个遥远的预警，而是已经传导至行业头部公司采购策略的当下事实。\n\nNOM在最新发布的研报中指出，全球主要光器件生产商Lumentum Holdings在6月9日的投资者交流中，明确表示需要寻找新的InP衬底供应商。这距离该公司5月5日财报会议上“长期合同保障供应稳定”的表态，仅隔了一个月。一个月内，一家行业龙头从“供应可控”转向“必须找新来源”，意味着供需紧张程度已经出现了质的跃迁。\n\n这份报告的核心判断是：InP衬底的供应格局正在从“相对均衡”转向“结构性偏紧”，而这一变化的真正赢家，不是那些组装能力最强的光模块厂商，而是掌握衬底产能的垂直整合型企业。具体而言，NOM认为住友电工（Sumitomo Electric Industries）拥有全球最大的InP衬底产能，并且同时具备光器件芯片的自制能力，这种“材料+器件”的双重优势正在成为竞争壁垒，而市场可能尚未充分定价这一结构性变化。\n\n以下，我们将从供应链动态、竞争格局、以及尚未被充分回答的问题三个层面，拆解这份研报的核心逻辑。\n\n![研报原图 1](assets/xhs_card_01.png)\n\n## 1. 从“长期合同”到“寻找新供应商”的转变，是供需格局的拐点信号\n\n一份长期合同的意义在于锁定价格和供应量。当一家企业从依赖长期合同转向主动寻找替代供应商，通常只有两种可能：一是现有供应商无法满足增量需求，二是现有供应商的报价或条款已经不可接受。无论哪种情况，都指向同一个结论——InP衬底市场已经进入卖方市场。\n\nLumentum的转变发生在短短一个月内。5月5日财报会议上，该公司还\n\n[... middle omitted ...]\n\n解读笔记、关键图表的原始数据，以及对这些未解问题的持续跟踪。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n磷化铟基板，突然变抢手了\n\n🔍 供需正在收紧\n\n某外资投行最新研报指出，光器件关键材料——磷化铟（InP）基板的供需格局正在进一步趋紧。\n\n1️⃣ 龙头光器件厂商Lumentum在5月财报会上就提过InP基板供应紧张，但当时认为长协能保障稳定采购。然而，6月最新表态变了：由于光器件需求持续升温，Lumentum表示需要寻找新的InP基板供应商。\n\n2️⃣ 住友电工是全球InP基板产能最大的厂商，同时自产连续波激光二极管（CW-LD）和电吸收调制器集成激光器（EML）芯片，部分对外销售。研报认为，凭借核心材料供应优势，住友电工在扩产光器件时比竞争对手更灵活，且能享受更高利润率。\n\n3️⃣ 值得注意的是，Lumentum还提到会增加从英国供应商的采购。2025年12月它已与英国公司IQE签了多年协议采购InP外延片，未来可能进一步扩大合作。\n\n📌 核心逻辑：上游材料自给能力，正在成为光器件赛道的关键竞争变量。\n\n欢迎一起讨论光通信产业链的最新变化～\n\n#学习笔记\n\n[source_mineru.md]\n# Wire & cable: Optical devices\n\nEQUITY: JAPAN STEEL, NO\n\n[... middle omitted ...]\n\n-term contracts should ensure stable procurement. However, demand for optical devices has been rising further since the results briefing in May, and it has now said that it will need to find a\n\n[... middle omitted ...]\n\nation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Securities Co., Ltd., Japan. All rights reserved."
  },
  {
    "id": "R045",
    "title": "美国银行：市场正在为一场“通胀高于增长”的资产重新定价做准备",
    "digest": "[wechat_article.md]\n# 美国银行：市场正在为一场“通胀高于增长”的资产重新定价做准备\n\n这份报告最值得看的判断，不是某个资产类别下周的涨跌，而是美国银行首席投资策略师Michael Hartnett团队通过资金流数据揭示的一个正在成形的宏观叙事：通胀正在重新成为主导变量，而资产配置却仍停留在“看涨惯性”中。当通胀预期与政策应对之间的落差被市场意识到时，资产价格的重估可能比大多数人预期的更剧烈。\n\n报告的核心信号有两个层面。第一个是数据层面的确认：美国通胀已经超过4%，而特朗普在通胀问题上的支持率跌至27%，低于拜登任内低点。第二个是行为层面的警示：尽管美国银行的牛熊指标已经连续四周发出“卖出信号”，但资金仍在涌入股票，尤其是科技股——上周科技基金录得创纪录的123亿美元流入。这种“知道风险但仍在加仓”的张力，正是资产定价中最值得警惕的状态。\n\n为什么现在重要？因为历史提供了清晰的参照系。报告特别点出了1994年的类比：当时美联储在滞后于曲线后被迫大幅加息，最终导致债券收益率飙升、股市陷入多月的交易区间，直到墨西哥比索危机和橙县破产事件才完成了去杠杆。今天的情景——通胀走高、就业市场紧张、政策制定者仍在强调“美国优先”——与1994年有着令人不安的相似性。\n\n以下是我们从这份报告中提炼的五个核心洞察，它们共同指向一个判断：当前资产配置的“看涨惯性”正在积累风险，而真正的机会可能出现在那些已经被资金抛弃、但基本面正在改善的角落。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 资金流显示市场正在形成“科技单边市”，但历史表明这种拥挤往往以剧烈调整收场\n\n上周的数据是惊人的。全球股票基金净流入315亿美元，其中美国股票占174亿美元，已是连续第11周净流入——这是自2025年12月以来最长的连续流入记录。而在这174亿美元中，科技板块独占了\n\n[... middle omitted ...]\n\n资产定价逻辑可能发生根本转变的时刻，一个人的视野总是有限的。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nCPI破4%，华尔街开始收缩了\n\n**市场信号偏谨慎**\n\n某外资投行最新周报显示，资产配置已进入“冷思考”阶段。核心逻辑：通胀 >4%，失业率 <4.3%，这种组合历史上对应加息周期，市场压力不小。\n\n1/ **资金流在转向**\n- 科技股单周净流入123亿美元，创历史新高（含大量半导体ETF）\n- 但黄金连续4周流出，加密货币5周流出66亿美元，创纪录\n- EM股票9周来首次净流入，韩国流入59亿美元\n\n2/ **“3P”信号亮了红灯**\n- 持仓（Positioning）过于乐观\n- 盈利预期（Profit expectations）仍高\n- 政策（Policy）可能从降息转向加息\n研报建议：继续减仓，直到市场条件收紧到位。\n\n3/ **1994年的剧本在重演？**\n通胀 >4%时，标普500未来3个月平均跌4%，6个月跌7%。1994年美联储被迫大幅加息，市场直到年底才稳住。现在CPI已4.2%，走势相似。\n\n4/ **值得关注的“逆向”机会**\n如果地缘冲突缓和，消费股、REITs、欧洲、新兴市场货币（印度、印尼）可能受益。研报提到“和平赢家”逻辑。\n\n5/ **私人银行在买什么**\n过去4周，高净\n\n[... middle omitted ...]\n\napproval @ 27% (below Biden lows - Chart 4), US oil inventories down to 48 days (close to 45-year lows – Chart 5), policy maker conviction best route to “America First” via “Wall Street First”\n\n[... middle omitted ...]\n\nw in accordance with firm policies.\n\nNeither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information."
  },
  {
    "id": "R046",
    "title": "摩根斯坦利：阿尔茨海默病的真正拐点不在新药，而在“脑穿梭”能否重构成本曲线",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：阿尔茨海默病的真正拐点不在新药，而在“脑穿梭”能否重构成本曲线\n\n这份报告最值得看的判断，不是阿尔茨海默病市场规模有多大，而是：**美国正在经历一场由人口结构决定的健康支出被动升级，而阿尔茨海默病是这场升级中最集中的成本放大器。** 摩根斯坦利在这份题为《Can Innovation Ease Alzheimer's Growing Burden?》的研报中，系统性地论证了一个让投资者重新审视生物科技板块底层逻辑的观点——真正值得关注的不是任何一个单药能否成功，而是“脑穿梭”技术平台能否将阿尔茨海默病从不可控的财政黑洞，转化为可管理的治疗路径。\n\n这不是一份常规的行业综述。它从人口统计的硬约束出发，推演到医疗支出的机械性增长，再落到生物技术能否改变这一轨迹。它的核心洞察是：我们正在把增加的寿命，系统性地转化为增加的失能年数。阿尔茨海默病是这个转化过程中最高效的“催化剂”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 人口结构本身就是一个被低估的医疗支出引擎\n\n摩根斯坦利的分析起点，是一个容易被忽视的宏观事实：美国人口总量在2050年达到约3.64亿峰值后，将进入长期缓慢下降，到2099年基本回到当前水平。这意味着，**未来75年美国医疗支出的增长，几乎完全由年龄结构的“顶部加重”驱动，而非人口总量的扩张。**\n\n数字本身已经足够说明问题。目前美国老年人（65岁以上）占人口约18.8%，到2099年将升至30.5%。而老年人的年均个人医疗支出约为22,400美元，是成年人的2.4倍、儿童的5倍以上。仅凭年龄结构变化，美国个人医疗支出占GDP的比重将从当前的11.7%被动推升至2050年的约13.1%。\n\n报告估算，当前美国阿尔茨海默病相关市场规模约为500亿美元，基于约700万患者、80%为轻中度\n\n[... middle omitted ...]\n\n团队对关键节点的前瞻判断感兴趣，欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n老龄化正在把延寿变成延长失能期\n\n**健康寿命的硬边界**\n\n阿尔茨海默是那个最会把长寿转化为失能年限的疾病。\n\n**1/ 人口结构在变，但总盘子没怎么涨**\n\n投行研报指出，美国人口预计2050年见顶，之后缓慢回落。真正的问题不是人多，而是老人比例飙升——从2026年的18.8%涨到2099年的30.5%。\n\n老人人均医疗花费是劳动年龄人口的2.4倍。仅仅是年龄结构变化，就能把美国个人医疗支出占GDP的比例从11.7%推到13.1%。\n\n**2/ GLP-1 救不了阿尔茨海默**\n\n口服司美格鲁肽在早期阿尔茨海默的3期试验（EVOKE/EVOKE+）失败了，2025年11月终止。代谢通路和神经退行之间的鸿沟，比很多人想象的要深。\n\n**3/ 现有疗法有效，但天花板明显**\n\nLecanemab 和 Donanemab 清除淀粉样蛋白的效果已接近极限，临床获益约27%的延缓（18个月CDR-SB评分约0.45分），但不够。\n\n研报估算美国阿尔茨海默治疗市场约700亿美元，其中：\n- 疾病修饰疗法（淀粉样蛋白/tau蛋白）：约500亿\n- 症状控制（精神病性症状/激越）：约200亿\n\n**4/ 脑穿梭技术是真正\n\n[... middle omitted ...]\n\nretirement-system problem. We estimate a \\$70B US market for AD therapies.  \nLife expectancy has risen to an apparent ceiling near \\~80yrs, while healthspan (years without disease impairment) \n\n[... middle omitted ...]\n\nharmaceuticals (VRTX.O)</td><td>O (12/03/2025)</td><td>$445.77</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.\n\n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "Figure 1",
    "context": "Figure 1: PPI reflation was in line with our forecast"
  },
  {
    "figure_id": "F002",
    "report_id": "R001",
    "label": "Figure 2",
    "context": "Figure 2: Pass-through of energy price increases continued"
  },
  {
    "figure_id": "F003",
    "report_id": "R001",
    "label": "Figure 3",
    "context": "Figure 3: CPI was unchanged at 1.2% YoY, while core CPI slowed to 1.1% YoY"
  },
  {
    "figure_id": "F004",
    "report_id": "R001",
    "label": "Figure 4",
    "context": "Figure 4: Energy price increases continued to support CPI inflation"
  },
  {
    "figure_id": "F005",
    "report_id": "R001",
    "label": "Figure 5",
    "context": "Figure 5: Core inflation declined on a MoM basis"
  },
  {
    "figure_id": "F006",
    "report_id": "R001",
    "label": "Figure 6",
    "context": "Figure 6: Food inflation rebounded slightly but was still in negative territory"
  },
  {
    "figure_id": "F007",
    "report_id": "R001",
    "label": "Figure 7",
    "context": "Figure 7: We revise down the full-year CPI forecast to 1.5% from 1.6%"
  },
  {
    "figure_id": "F008",
    "report_id": "R001",
    "label": "Figure 8",
    "context": "Figure 8: PPI reflation emerged in mid- and downstream sectors"
  },
  {
    "figure_id": "F009",
    "report_id": "R002",
    "label": "Exhibit 1",
    "context": "Exhibit 2: Sequentially oil push slowed, limited reflation elsewhere"
  },
  {
    "figure_id": "F010",
    "report_id": "R002",
    "label": "Exhibit 1",
    "context": "Exhibit 2: Sequentially oil push slowed, limited reflation elsewhere"
  },
  {
    "figure_id": "F011",
    "report_id": "R003",
    "label": "Figure 1",
    "context": "■ Construction: A modest rebound emerged, with PPI at 3.3%YoY and 0.9%MoM for ferrous metal mining, and -3.4%YoY and 0.4%MoM for non-metallic mining. The combined contribution from construction-related items to PPI rose to 0.1ppts per our estimate, still small"
  },
  {
    "figure_id": "F012",
    "report_id": "R003",
    "label": "Figure 3",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 3. The AI supercycle is an inflation driving force now with telecom CPI at second all-time high"
  },
  {
    "figure_id": "F013",
    "report_id": "R003",
    "label": "Figure 2",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 2. Core CPI dipped on both services and core goods, another reminder of weak consumer demand"
  },
  {
    "figure_id": "F014",
    "report_id": "R003",
    "label": "Figure 4",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 4. The small rebound in construction prices in May offers a bright spot"
  },
  {
    "figure_id": "F015",
    "report_id": "R004",
    "label": "Figure 1",
    "context": "Figure 1. State Council has set explicit targets for urban renewal in its latest guidance © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 2. IT FAI has outpaced headline FAI and stayed buoyant in April FAI, Headline and IT"
  },
  {
    "figure_id": "F016",
    "report_id": "R005",
    "label": "Figure 1",
    "context": "As part of our annual update cycle, we have recently completed a comprehensive thematic reassessment and stock remapping, reflected in our latest publication, Global Theme Machine: Reassessment of Themes for 2026. Leveraging tools refined over many years, we a"
  },
  {
    "figure_id": "F017",
    "report_id": "R005",
    "label": "Figure 2",
    "context": "Mobile Payments Global Tourism Supply Chain Solutions Pension Shortfalls Digital Currency Figure 2. 2026 Themes (Contd.) Resources Clean Water Food Innovation Scarce Resources"
  },
  {
    "figure_id": "F018",
    "report_id": "R005",
    "label": "Figure 4",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. ## Model Performance Top quintile themes rose $3.6\\%$ in the latest month, modestly ahead of the $3.4\\%$ return from bottom quintile themes, although both lagged the MSCI World's $4.6\\%$ gai"
  },
  {
    "figure_id": "F019",
    "report_id": "R005",
    "label": "Figure 5",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 5. Monthly Performance Since May 2025"
  },
  {
    "figure_id": "F020",
    "report_id": "R005",
    "label": "Figure 8",
    "context": "Figure 8. Bottom Performing Themes in Last Month (red denotes the bottom performing theme for the corresponding period) © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 9. Top 10 & Bottom 10 Themes by Last month's Returns"
  },
  {
    "figure_id": "F021",
    "report_id": "R005",
    "label": "Figure 11",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 11. Top 10 & Bottom 10 Themes by Last 12 months' Returns"
  },
  {
    "figure_id": "F022",
    "report_id": "R005",
    "label": "Figure 10",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 10. Top 10 & Bottom 10 Themes by Last 3 months' Returns"
  },
  {
    "figure_id": "F023",
    "report_id": "R005",
    "label": "Figure 12",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 12. Top 10 & Bottom 10 Themes by Last 3 Years' Returns"
  },
  {
    "figure_id": "F024",
    "report_id": "R005",
    "label": "Figure 23",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. ## Idiosyncratic Risk and Relative Macro Exposures Given the persistent influence of macro variables on equity return dispersion, we overlay the Global Theme Machine with Citi's Global Risk "
  },
  {
    "figure_id": "F025",
    "report_id": "R006",
    "label": "Figure 1",
    "context": "Figure 1: US petroleum product price change from February 27 to June 8"
  },
  {
    "figure_id": "F026",
    "report_id": "R006",
    "label": "Figure 2",
    "context": "Figure 2: JPM US retail gasoline price forecast under alternative Strait of Hormuz reopening scenarios \\$ per gallon"
  },
  {
    "figure_id": "F027",
    "report_id": "R006",
    "label": "Figure 3",
    "context": "Figure 3: Average retail gasoline price by state \\$/gallon"
  },
  {
    "figure_id": "F028",
    "report_id": "R006",
    "label": "Figure 4",
    "context": "Figure 4: US commercial inventories of gasoline and diesel"
  },
  {
    "figure_id": "F029",
    "report_id": "R006",
    "label": "Figure 5",
    "context": "Figure 5: US commercial inventories of gasoline and diesel in days of demand coverage"
  },
  {
    "figure_id": "F030",
    "report_id": "R006",
    "label": "Figure 6",
    "context": "Figure 6: US commercial inventories of jet in days of demand coverage Days (LHS); Commercial inventory (RHS) in thousands of barrels"
  },
  {
    "figure_id": "F031",
    "report_id": "R008",
    "label": "Figure 1",
    "context": "Figure 1: Global EV battery installations by company vs KOR battery cell market share GWh, %"
  },
  {
    "figure_id": "F032",
    "report_id": "R008",
    "label": "Figure 2",
    "context": "Figure 2: Global EV battery installation market share trend by company %"
  },
  {
    "figure_id": "F033",
    "report_id": "R008",
    "label": "Figure 3",
    "context": "Figure 3: EU10 + US + China EV/PHEV sales and penetration trend"
  },
  {
    "figure_id": "F034",
    "report_id": "R008",
    "label": "Figure 5",
    "context": "Figure 5: EU-5+US+China EV/PHEV sales mix trend"
  },
  {
    "figure_id": "F035",
    "report_id": "R008",
    "label": "Figure 7",
    "context": "Figure 7: EU-5 EV/PHEV penetration trend"
  },
  {
    "figure_id": "F036",
    "report_id": "R008",
    "label": "Figure 4",
    "context": "Figure 4: EU10 + US + China EV sales and penetration trend"
  },
  {
    "figure_id": "F037",
    "report_id": "R008",
    "label": "Figure 6",
    "context": "Figure 6: US EV/PHEV penetration trend"
  },
  {
    "figure_id": "F038",
    "report_id": "R008",
    "label": "Figure 8",
    "context": "Figure 8: China EV/PHEV penetration trend"
  },
  {
    "figure_id": "F039",
    "report_id": "R008",
    "label": "Figure 9",
    "context": "Figure 9: US: EV penetration and incentive trends"
  },
  {
    "figure_id": "F040",
    "report_id": "R008",
    "label": "Figure 11",
    "context": "Figure 11: HMC/Kia vs global OEM share performance"
  },
  {
    "figure_id": "F041",
    "report_id": "R008",
    "label": "Figure 13",
    "context": "Figure 13: HMC/Kia vs US OEM share performance Figure 10: US: EV inventory trends"
  },
  {
    "figure_id": "F042",
    "report_id": "R008",
    "label": "Figure 13",
    "context": "Figure 13: HMC/Kia vs US OEM share performance Figure 10: US: EV inventory trends"
  },
  {
    "figure_id": "F043",
    "report_id": "R008",
    "label": "Figure 12",
    "context": "Figure 12: HMC/Kia vs JP OEM share performance"
  },
  {
    "figure_id": "F044",
    "report_id": "R008",
    "label": "Figure 14",
    "context": "Figure 14: HMC/Kia vs EU OEM share performance"
  },
  {
    "figure_id": "F045",
    "report_id": "R008",
    "label": "Figure 15",
    "context": "Figure 15: Share price performance – regional comparison"
  },
  {
    "figure_id": "F046",
    "report_id": "R008",
    "label": "Figure 17",
    "context": "Figure 17: Battery ecosystem – FY26E P/E multiple vs sales growth"
  },
  {
    "figure_id": "F047",
    "report_id": "R008",
    "label": "Figure 19",
    "context": "Figure 19: Battery ecosystem – FY26E P/E multiple vs OPM"
  },
  {
    "figure_id": "F048",
    "report_id": "R008",
    "label": "Figure 21",
    "context": "Figure 21: Battery ecosystem – FY26E EV/EBITDA multiple vs EBITDAM EV/EBITDA (x), %"
  },
  {
    "figure_id": "F049",
    "report_id": "R008",
    "label": "Figure 16",
    "context": "Figure 16: Korean EV battery and material market capitalization"
  },
  {
    "figure_id": "F050",
    "report_id": "R008",
    "label": "Figure 18",
    "context": "Figure 18: Battery ecosystem – FY27E P/E multiple vs sales growth"
  },
  {
    "figure_id": "F051",
    "report_id": "R008",
    "label": "Figure 20",
    "context": "Figure 20: Battery ecosystem – FY27E P/E multiple vs OPM"
  },
  {
    "figure_id": "F052",
    "report_id": "R008",
    "label": "Figure 22",
    "context": "Figure 22: Battery ecosystem – FY27E EV/EBITDA multiple vs EBITDAM"
  },
  {
    "figure_id": "F053",
    "report_id": "R009",
    "label": "Exhibit 1",
    "context": "Exhibit 1: USD still trading within its previous 12m range, while labor surprise measures reach fresh multi-year highs DXY & Bloomberg US Labor Surprise Index"
  },
  {
    "figure_id": "F054",
    "report_id": "R009",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Policy differentials now priced for modest but steady narrowing (towards EUR)... Fed & ECB policy rate"
  },
  {
    "figure_id": "F055",
    "report_id": "R009",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Since the closure of the Strait of Hormuz, the EUR has remained resilient relative to the upward pressure on gas prices European Gas (TZT) & EUR (inverted)"
  },
  {
    "figure_id": "F056",
    "report_id": "R009",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Relative US vs. Euro area data trends have been stark, suggesting further space for the EUR to depreciate further Economic Change Indices: EA - USA"
  },
  {
    "figure_id": "F057",
    "report_id": "R009",
    "label": "Exhibit 4",
    "context": "Exhibit 4: ... Yet post-“Liberation Day” structural break between FX and policy rates has continued ECB-Fed policy differential (and OIS Implied) vs. EUR"
  },
  {
    "figure_id": "F058",
    "report_id": "R009",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Vast majority of Fed forecasters have still been reluctant to call for hikes in 2026 or 2027 Histogram of YE '26 and YE '27 Fed funds forecasts Fed Funds Upper Bound Cons. Forecasts"
  },
  {
    "figure_id": "F059",
    "report_id": "R012",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: Our perception of AI model quality increasing centres around differentiable quality as perceived by humans, as opposed to underlying reasoning capabilities necessarily converging in a strict academic sense"
  },
  {
    "figure_id": "F060",
    "report_id": "R012",
    "label": "Exhibit 4",
    "context": "Outside this perimeter however, for a growing envelope of lagging edge workloads, especially outside the US, we'd expect the Chinese AI labs' much lower token costs to prove attractive, and help them win share. Exhibit 4 shows directionally how we mentally bre"
  },
  {
    "figure_id": "F061",
    "report_id": "R012",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: We expect the Chinese AI labs to win share on the basis of their much cheaper tokens, but the accessibility of the overseas market will vary by region EXHIBIT 5: We think at least 35-40% of the long-term global TAM for A"
  },
  {
    "figure_id": "F062",
    "report_id": "R012",
    "label": "Exhibit 6",
    "context": "EXHIBIT 6: Over time we expect a wider range of AI end uses to become “good enough” and therefore no longer worthy of incremental R&D, allowing the AI labs to move on to more frontier end uses Evolution of AI R&D focus"
  },
  {
    "figure_id": "F063",
    "report_id": "R013",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Monthly China aluminum ouptut run rate reached 47.1mnt in April 2026, 1.8 mnt higher than the average outout of 45.3mnt in 2025A China primary aluminum output (annualized, mmt)"
  },
  {
    "figure_id": "F064",
    "report_id": "R013",
    "label": "Exhibit 2",
    "context": "Net addition of aluminum capacity/output in Indonesia"
  },
  {
    "figure_id": "F065",
    "report_id": "R014",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Crude net imports fell 2.4 mb/d MoM in April to 9.3 mb/d. Net imports then declined to 7.8 mb/d in May, down 3.2 mb/d YoY."
  },
  {
    "figure_id": "F066",
    "report_id": "R014",
    "label": "Exhibit 2",
    "context": "Exhibit 2 : Observable Chinese crude inventories continued to build over March and April, based on Vortexa data. Average build rate was \\~1.1 mb/d. However, inventories switched to draws in May, with an average draw rate of 750 kb/d"
  },
  {
    "figure_id": "F067",
    "report_id": "R014",
    "label": "Exhibit 3",
    "context": "Exhibit 3: China's apparent oil demand fell 1.4 mb/d MoM and was 1.2 mb/d lower YoY (-8%) in April China Apparent Oil Demand (mb/d)"
  },
  {
    "figure_id": "F068",
    "report_id": "R014",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Apparent diesel demand fell 100 kb/d MoM and was down 70 kb/d YoY (-2%) in April"
  },
  {
    "figure_id": "F069",
    "report_id": "R014",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Apparent gasoline demand fell 290 kb/d MoM but was up 60 kb/d YoY (+2%) in April"
  },
  {
    "figure_id": "F070",
    "report_id": "R014",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Traffic levels in China have tracked broadly flat YoY over May"
  },
  {
    "figure_id": "F071",
    "report_id": "R014",
    "label": "Exhibit 7",
    "context": "Exhibit 7: China flight numbers were down 1% YoY in April, driven by a decline in domestic flight numbers. China Domestic and International Flight numbers (thousands)"
  },
  {
    "figure_id": "F072",
    "report_id": "R014",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Jet fuel/kerosene apparent demand fell 200 kb/d MoM but was up 30 kb/d YoY (+4%) in April"
  },
  {
    "figure_id": "F073",
    "report_id": "R014",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Apparent fuel oil demand fell by 315 kb/d MoM and was down 295 kb/d YoY (-37%) in April China apparent fuel oil demand (mb/d)"
  },
  {
    "figure_id": "F074",
    "report_id": "R014",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Apparent LPG demand fell by 400 kb/d MoM and was down 570 kb/d YoY (-21%) in April China apparent LPG demand (mb/d)"
  },
  {
    "figure_id": "F075",
    "report_id": "R014",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Apparent naphtha demand fell 75 kb/d MoM and was down 60 kb/d YoY (-3%) in April"
  },
  {
    "figure_id": "F076",
    "report_id": "R014",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Crude production fell 130 kb/d MoM in April but was still up 50 kb/d YoY"
  },
  {
    "figure_id": "F077",
    "report_id": "R014",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Both Russia's Urals crude and Iran's Iranian Light crude grades priced at a premium to Brent over March and April, having priced at a discount since 2022 due to sanctions on these crudes. Crude oil price differentials"
  },
  {
    "figure_id": "F078",
    "report_id": "R014",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Refinery runs fell 1.2 mb/d MoM and were down 830 kb/d YoY (-6%) in April China refinery throughput (mb/d)"
  },
  {
    "figure_id": "F079",
    "report_id": "R014",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Seaborne data shows China's imports dropping to 6.6 mb/d in May, \\~5 mb/d below February levels..."
  },
  {
    "figure_id": "F080",
    "report_id": "R014",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Crude imports fell 2.3 mb/d lower YoY in April and were 3.2 mb/d lower YoY in May at 7.8 mb/d China crude oil imports (mb/d)"
  },
  {
    "figure_id": "F081",
    "report_id": "R014",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Gasoline export margins averaged +\\$22/bbl in March, when April loadings were scheduled"
  },
  {
    "figure_id": "F082",
    "report_id": "R014",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Diesel export margins averaged +\\$84/bbl in March, when April loadings were scheduled"
  },
  {
    "figure_id": "F083",
    "report_id": "R014",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Gasoline net exports were down 60 kb/d MoM in April and 210 kb/d lower YoY"
  },
  {
    "figure_id": "F084",
    "report_id": "R014",
    "label": "Exhibit 21",
    "context": "Exhibit 21: Diesel net exports were down 120 kb/d MoM in April and 60 kb/d lower YoY"
  },
  {
    "figure_id": "F085",
    "report_id": "R014",
    "label": "Exhibit 22",
    "context": "Exhibit 22: Jet fuel net exports were down 130 kb/d MoM and 230 kb/d lower YoY"
  },
  {
    "figure_id": "F086",
    "report_id": "R014",
    "label": "Exhibit 24",
    "context": "Exhibit 24: LPG net exports were 370 kb/d higher MoM and 660 kb/d higher YoY"
  },
  {
    "figure_id": "F087",
    "report_id": "R014",
    "label": "Exhibit 26",
    "context": "Exhibit 26: Net refined product exports rose 210 kb/d MoM in April and were up 80 kb/d YoY"
  },
  {
    "figure_id": "F088",
    "report_id": "R014",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Fuel oil net exports were up 270 kb/d MoM but 180 kb/d lower YoY"
  },
  {
    "figure_id": "F089",
    "report_id": "R014",
    "label": "Exhibit 25",
    "context": "Exhibit 25: Naphtha net exports were 70 kb/d higher MoM and 230 kb/d higher YoY"
  },
  {
    "figure_id": "F090",
    "report_id": "R014",
    "label": "Exhibit 27",
    "context": "Exhibit 27: Total product exports fell 330 kb/d MoM in April and were down 470 kb/d YoY (-40%)"
  },
  {
    "figure_id": "F091",
    "report_id": "R014",
    "label": "Exhibit 28",
    "context": "Exhibit 28: Total product imports were down 540 kb/d MoM in April and 550 kb/d lower YoY (-50%)"
  },
  {
    "figure_id": "F092",
    "report_id": "R014",
    "label": "Exhibit 29",
    "context": "Exhibit 29: Domestic diesel and gasoline cracks turned deeply negative over March and April China Bohai Bay product crack spreads, excl. tax, \\$/bbl)"
  },
  {
    "figure_id": "F093",
    "report_id": "R014",
    "label": "Exhibit 30",
    "context": "Exhibit 30: Seasonal changes in Chinese gasoline and diesel cracks China Bohai Bay product crack spreads, excl. tax, \\$/bbl)"
  },
  {
    "figure_id": "F094",
    "report_id": "R014",
    "label": "Exhibit 31",
    "context": "Exhibit 31: Chinese CDU outages rose 600 kb/d MoM in April to 1.45 mb/d"
  },
  {
    "figure_id": "F095",
    "report_id": "R014",
    "label": "Exhibit 32",
    "context": "Exhibit 32: Refinery runs fell 1.2 mb/d MoM and were 830 kb/d lower YoY (-6 %) in April"
  },
  {
    "figure_id": "F096",
    "report_id": "R014",
    "label": "Exhibit 33",
    "context": "Exhibit 33: State-owned refineries' utilisation levels dropped sharply to 79% in March and 69% in April..."
  },
  {
    "figure_id": "F097",
    "report_id": "R014",
    "label": "Exhibit 34",
    "context": "Exhibit 34: ... with independent refinery util rates inched higher to 54% in March and 55% in April"
  },
  {
    "figure_id": "F098",
    "report_id": "R014",
    "label": "Exhibit 35",
    "context": "Exhibit 35: Refinery output of diesel fell 230 kb/d MoM and was down 130 kb/d YoY (-3%)"
  },
  {
    "figure_id": "F099",
    "report_id": "R014",
    "label": "Exhibit 37",
    "context": "Exhibit 37: Refinery output of jet fuel/kerosene was down 330 kb/d MoM and fell 200 kb/d YoY (-17%)"
  },
  {
    "figure_id": "F100",
    "report_id": "R014",
    "label": "Exhibit 39",
    "context": "Exhibit 39: Refinery output of naphtha was flat MoM but was 160 kb/d higher YoY (+9%)"
  },
  {
    "figure_id": "F101",
    "report_id": "R014",
    "label": "Exhibit 36",
    "context": "Exhibit 36: Refinery output of gasoline was down 350 kb/d MoM and was 150 kb/d lower YoY (-4%)"
  },
  {
    "figure_id": "F102",
    "report_id": "R014",
    "label": "Exhibit 38",
    "context": "Exhibit 38: Refinery output of fuel oil fell 5 kb/d MoM and was 120 kb/d lower YoY (-15%)"
  },
  {
    "figure_id": "F103",
    "report_id": "R014",
    "label": "Exhibit 40",
    "context": "Exhibit 40: Refinery output of LPGs fell 30 kb/d MoM but was up 90 kb/d YoY (+6%)"
  },
  {
    "figure_id": "F104",
    "report_id": "R014",
    "label": "Exhibit 41",
    "context": "Exhibit 41: China's observable crude inventories have built over March and April, as crude supply still outpaced refinery demand. Change in China onshore crude inventory"
  },
  {
    "figure_id": "F105",
    "report_id": "R014",
    "label": "Exhibit 42",
    "context": "Exhibit 42: Observable crude inventories built by \\~55 mln bbls over the course of March and April China crude inventories (mln bbls)"
  },
  {
    "figure_id": "F106",
    "report_id": "R014",
    "label": "Exhibit 43",
    "context": "Exhibit 43: Observable aggregated product inventories China aggregated oil products inventories (mln bbls)"
  },
  {
    "figure_id": "F107",
    "report_id": "R014",
    "label": "Exhibit 44",
    "context": "Exhibit 44: Observable gasoline inventories China gasoline inventories (mln bbls)"
  },
  {
    "figure_id": "F108",
    "report_id": "R014",
    "label": "Exhibit 45",
    "context": "Exhibit 45: Observable diesel inventories China diesel inventories (mln bbls)"
  },
  {
    "figure_id": "F109",
    "report_id": "R014",
    "label": "Exhibit 46",
    "context": "Exhibit 46: Comparison of demand estimates from different data agencies"
  },
  {
    "figure_id": "F110",
    "report_id": "R014",
    "label": "Exhibit 47",
    "context": "Exhibit 47: China Customs import data and Vortexa seaborne import data implies a small decline in pipeline crude imports in April"
  },
  {
    "figure_id": "F111",
    "report_id": "R015",
    "label": "Exhibit 1",
    "context": "Exhibit 1: The deal-level arbitrage spreads generally correlate with the new issue calculations Deal-matched arbitrage spread is trailing 3-month deal-weighted figure; new Issue spread uses new issue loan spreads net monthly new is"
  },
  {
    "figure_id": "F112",
    "report_id": "R015",
    "label": "Exhibit 2",
    "context": "Exhibit 2: The trend towards tighter arbitrage spreads coincides with more managers in a more mature market"
  },
  {
    "figure_id": "F113",
    "report_id": "R015",
    "label": "Exhibit 3",
    "context": "Exhibit 3: USD Middle Market CLO arbitrage spreads have tightened towards 300bp Direct Lending spread calculated as difference between CDLI yield-to-maturity and 3-month LIBOR (SOFR after December 2020) USD Middle Market CLO arbi"
  },
  {
    "figure_id": "F114",
    "report_id": "R015",
    "label": "Exhibit 4",
    "context": "Exhibit 4: EUR IG tranches offer a spread pickup relative to USD EUR/USD tranche spread ratios (adjusted with 5-year cross-currency basis); median since 2021 EUR/USD primary tranche spread ratio"
  },
  {
    "figure_id": "F115",
    "report_id": "R015",
    "label": "Exhibit 5",
    "context": "Exhibit 5: USD deal economics have improved by less than 20bp on reset since 2023 Change in USD CLO arbitrage spread for resets by new issue vintage"
  },
  {
    "figure_id": "F116",
    "report_id": "R015",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Whereas EUR deals have improved by nearly 50bp over the same period Change in EUR CLO arbitrage spread for resets by new issue vintage"
  },
  {
    "figure_id": "F117",
    "report_id": "R015",
    "label": "Exhibit 7",
    "context": "Exhibit 7: EUR new issue loan spreads have lagged the tightening impulse, in part because of lower repricing volumes Repricing volumes scaled by market notional"
  },
  {
    "figure_id": "F118",
    "report_id": "R015",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Arbitrage spreads are slightly wider for most defensive managers, while EUR CLO spreads exhibit the opposite pattern BSL arbitrage spread by manager tier"
  },
  {
    "figure_id": "F119",
    "report_id": "R016",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Investor Positioning Moderation Has Been One Driver of the Decline in Oil Prices"
  },
  {
    "figure_id": "F120",
    "report_id": "R016",
    "label": "Exhibit 1",
    "context": "Exhibit 2: We Maintain Our 2026Q4 Brent Oil Price Forecast at \\$90 But Reduce Our 2027 Average Forecast by \\$5 to \\$80"
  },
  {
    "figure_id": "F121",
    "report_id": "R016",
    "label": "Exhibit 3",
    "context": "Exhibit 3: We Maintain Our 2026Q4 OECD Commercial Stocks Forecast as the Slower-Than-Expected Pace of Draws Roughly Offsets the Longer Expected Duration of Draws"
  },
  {
    "figure_id": "F122",
    "report_id": "R016",
    "label": "Exhibit 4",
    "context": "Exhibit 4: A Nearly \\$30 Boost From the Hormuz Shock to Brent Prices in 2026Q4 on Lower Commercial Stocks (Driven by Lower Gulf Production) and Higher Long-Dated Prices GS 2026Q4 Brent Price Forecast"
  },
  {
    "figure_id": "F123",
    "report_id": "R016",
    "label": "Exhibit 5",
    "context": "Exhibit 5: We Estimate a 5-6mb/d Q2 Deficit, Which Is Smaller Than the 14-15mb/d Hit to Mideast Production Reconciling 14-15mb/d Mideast Supply Loss With 5-6mb/d 2026Q2 Global Deficit"
  },
  {
    "figure_id": "F124",
    "report_id": "R016",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Full Normalization in Oil Exports Requires Hormuz Flows to Recover to 70% of Pre-War Levels (Assuming Redirections Remain at Current Levels) Estimating Hit to Oil Flows from Persian Gulf Countries"
  },
  {
    "figure_id": "F125",
    "report_id": "R016",
    "label": "Exhibit 7",
    "context": "Exhibit 7: We Expect Recovery in Mideast Production to Begin Later But Occur at a Faster Pace"
  },
  {
    "figure_id": "F126",
    "report_id": "R016",
    "label": "Exhibit 9",
    "context": "Exhibit 8: We Expect a Faster Rise in Production After Reopening Than Other Forecasters Crude Production from Persian Gulf Countries: Forecasts Comparison"
  },
  {
    "figure_id": "F127",
    "report_id": "R016",
    "label": "Exhibit 9",
    "context": "Exhibit 9: The Active Rig Count Has Increased Since the Start of the War in Saudi Arabia"
  },
  {
    "figure_id": "F128",
    "report_id": "R016",
    "label": "Exhibit 10",
    "context": "Exhibit 10: We Have Revised Higher Our 2027 Global Oil Surplus to 3.5mb/d Given Our Expectation of Higher Production in the UAE and Americas GS 2027 Global Oil Surplus"
  },
  {
    "figure_id": "F129",
    "report_id": "R016",
    "label": "Exhibit 11",
    "context": "Exhibit 11: We Expect UAE Crude Production to Increase to 4.1mb/d by Dec27"
  },
  {
    "figure_id": "F130",
    "report_id": "R016",
    "label": "Exhibit 8",
    "context": "Exhibit 12: Global Oil Demand Tends to Recover Swiftly Following Oil Supply Shocks But Remain Weak Following Recessions"
  },
  {
    "figure_id": "F131",
    "report_id": "R016",
    "label": "Exhibit 13",
    "context": "Exhibit 13: The EV Share in Passenger Car Sales Increased From $50\\%$ in February to $62\\%$ in May"
  },
  {
    "figure_id": "F132",
    "report_id": "R016",
    "label": "Exhibit 14",
    "context": "Exhibit 14: We Expect OECD SPR Inventories to Structurally Build at an Average Pace of 0.3mb/d From Late 2026"
  },
  {
    "figure_id": "F133",
    "report_id": "R016",
    "label": "Exhibit 15",
    "context": "Exhibit 15: We See Risks to Our Brent Price Forecast as Two-Sided but Tilted to the Upside on Net"
  },
  {
    "figure_id": "F134",
    "report_id": "R016",
    "label": "Exhibit 18",
    "context": "Exhibit 19: We Assume a Structural Rise in Strategic Stockpiling Demand in Non-OECD Economies"
  },
  {
    "figure_id": "F135",
    "report_id": "R017",
    "label": "Exhibit 1",
    "context": "Exhibit 1: US producers place relatively greater weight on cash flow, capital efficiency, and returns, while Canadian peers skew more toward EHS and operational execution, particularly production/delivery and operating efficiency."
  },
  {
    "figure_id": "F136",
    "report_id": "R017",
    "label": "Exhibit 2",
    "context": "Exhibit 2: CEO pay shows only a modest relationship with three-year relative TSR, underscoring that shareholder returns are only one input into compensation outcomes. CEO Compensation vs. Three-Year Relative TSR"
  },
  {
    "figure_id": "F137",
    "report_id": "R017",
    "label": "Exhibit 3",
    "context": "Exhibit 3: The ratio of change in control provisions to CEO annual compensation for the remaining public E&Ps is 2.5x, below recent seller medians though dispersion remains wide."
  },
  {
    "figure_id": "F138",
    "report_id": "R017",
    "label": "Exhibit 4",
    "context": "Exhibit 4: STI frameworks have moved away from production and strategic goals since 2019, with greater emphasis on EHS and continued focus on cash flow and capital efficiency. Changes from 2025 to 2026 were limited. Total Coverage"
  },
  {
    "figure_id": "F139",
    "report_id": "R017",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Across US producers, average STI weightings have shifted since 2019 toward EHS and capital efficiency, while production/delivery and strategic/discretionary metrics have become less prominent. US Average Weighting of Sho"
  },
  {
    "figure_id": "F140",
    "report_id": "R017",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Canadian STI design has shifted since 2019 toward EHS, production/delivery, operating efficiency, and strategic/discretionary goals, while cash flow, returns, and balance sheet metrics have become less prominent; weighti"
  },
  {
    "figure_id": "F141",
    "report_id": "R017",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Executive compensation across E&Ps remains overwhelmingly variable and performance-based, with PR, EQT, and IMO at the high end of the group. % of Variable Pay in CEO and Named Executive Officer Compensation"
  },
  {
    "figure_id": "F142",
    "report_id": "R017",
    "label": "Exhibit 10",
    "context": "Exhibit 10: LTI accounts for roughly 75% of executive compensation on average across our coverage. Long-Term Incentives as % of Total Compensation"
  },
  {
    "figure_id": "F143",
    "report_id": "R017",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Relative TSR and three-year TSR remain broadly embedded in LTI design across E&Ps, with nearly 90% of peers using both metrics."
  },
  {
    "figure_id": "F144",
    "report_id": "R017",
    "label": "Exhibit 12",
    "context": "Exhibit 12: CEO pay shows only a modest relationship with three-year relative TSR, suggesting realized compensation continues to reflect factors beyond shareholder returns alone."
  },
  {
    "figure_id": "F145",
    "report_id": "R017",
    "label": "Exhibit 13",
    "context": "Exhibit 13: 2025 CEO bonus payouts were largely delivered at or above target across the sector. 2025 CEO Bonus Payout vs Target Distribution"
  },
  {
    "figure_id": "F146",
    "report_id": "R017",
    "label": "Exhibit 14",
    "context": "Exhibit 14: CEO pay per flowing barrel varies widely across E&Ps, with smaller-scale companies generally screening above the median and larger producers below it. CRK stands out as an outlier, while CNQ, TOU, XOM, and CVX exhibit am"
  },
  {
    "figure_id": "F147",
    "report_id": "R017",
    "label": "Exhibit 15",
    "context": "Exhibit 15: The ratio of change in control provisions to CEO annual compensation for the remaining public E&Ps is 2.5x, below recent seller medians though dispersion remains wide."
  },
  {
    "figure_id": "F148",
    "report_id": "R018",
    "label": "Exhibit 2",
    "context": "Exhibit 2: China Property Developers' bond yields vs. share prices The average bond yield widened 18bp WoW to $9.58\\%$ , and the share price $-0.9\\%$ WoW."
  },
  {
    "figure_id": "F149",
    "report_id": "R018",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Hong Kong property issuers' bond spreads vs. share prices The average bond spread (OAS) tightened 3bp WoW to 61bp and the share price -7.2% WoW."
  },
  {
    "figure_id": "F150",
    "report_id": "R018",
    "label": "Exhibit 4",
    "context": "Exhibit 4: YTM (%) of benchmark bonds for select Chinese HY property developers The average yield of benchmark bonds widened 10bp WoW on average basis."
  },
  {
    "figure_id": "F151",
    "report_id": "R018",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Z-spread (bp) of benchmark bonds for select Hong Kong IG Property issuers The average z-spread of benchmark bonds widened 3bp WoW on average basis."
  },
  {
    "figure_id": "F152",
    "report_id": "R018",
    "label": "Exhibit 6",
    "context": "BofA GLOBAL RESEARCH"
  },
  {
    "figure_id": "F153",
    "report_id": "R019",
    "label": "FIGURE 1",
    "context": "From a vendor standpoint: \\- ANET (OW rated) entered the Campus market later and has grown its LSD share over the years. In the most recent earnings call, the company campus revenue guidance was \\$1.25B for 2026. Arista's market share in campus was 0.3% in 202"
  },
  {
    "figure_id": "F154",
    "report_id": "R019",
    "label": "FIGURE 2",
    "context": "\\- CSCO (EW rated) has the lion's share of the market (\\~50%). Networking revenues contracted in 2024 across the industry, but CSCO was hit harder on inventory correction. Since then, performance has been strong. In F3Q26, Cisco campus networking orders grew m"
  },
  {
    "figure_id": "F155",
    "report_id": "R019",
    "label": "FIGURE 3",
    "context": "\\- HPE (OW rated) has historically controlled low-DD share. Like CSCO, HPE experienced a bottoming of its Aruba business in 2024, and we model a strong return to growth in the Networking segment this year. We expect HPE to maintain the low DD market share leve"
  },
  {
    "figure_id": "F156",
    "report_id": "R019",
    "label": "FIGURE 4",
    "context": "## Campus Networking Market FIGURE 4. Total Campus Networking Revenue Growth"
  },
  {
    "figure_id": "F157",
    "report_id": "R019",
    "label": "FIGURE 5",
    "context": "FIGURE 5. Total Market Share"
  },
  {
    "figure_id": "F158",
    "report_id": "R019",
    "label": "FIGURE 6",
    "context": "CSCO dominates the campus market and has close to 50% share by our estimate. ANET came into the market much later, and, though a LSD player currently we expect it to continue gaining share in 2026 and 2027. HPE has maintained low DD share. FIGURE 6. Total Swit"
  },
  {
    "figure_id": "F159",
    "report_id": "R019",
    "label": "FIGURE 7",
    "context": "The Enterprise DC Switching market has been growing faster than the Campus market. We estimate 9% and 7% growth for campus switching and 47% and 24% for enterprise DC switching in 2026 and 2027, respectively. FIGURE 7. Enterprise WLAN Revenue (\\$M)"
  },
  {
    "figure_id": "F160",
    "report_id": "R019",
    "label": "FIGURE 8",
    "context": "The WLAN market accelerated in 2021 and 2022 before correcting in 2024. We model 12% growth for 2026 and 8% for 2027. Within this, we have WLAN Cloud growing faster at 17% CY21-27E CAGR. FIGURE 8. Enterprise SD-WAN Market Share"
  },
  {
    "figure_id": "F161",
    "report_id": "R020",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Of the total \\$2.1Tn CY30 DC Systems TAM, we see AI CPUs representing \\~\\$140bn of the value (split roughly 50/50 across compute/head node and agentic AI node), non-AI CPUs \\~\\$30bn Data Center Systems TAM – Breakout by:"
  },
  {
    "figure_id": "F162",
    "report_id": "R020",
    "label": "Exhibit 3",
    "context": "Exhibit 3: We flag three key roles of CPUs in servers: 1. Traditional, 2. AI compute/head node, 3. AI agentic node Role of the CPU in different server architectures ## ROLE OF THE CPU IN DIFFERENT SERVER ARCHITECTURES ```mermaid"
  },
  {
    "figure_id": "F163",
    "report_id": "R020",
    "label": "Exhibit 5",
    "context": "Exhibit 5: We expect INTC/AMD to each represent \\~25% value share, ARM merchant \\~35%, ARM custom \\~15% by CY30 Server CPU TAM (\\$mn) and Value Market Share Outlook"
  },
  {
    "figure_id": "F164",
    "report_id": "R020",
    "label": "Exhibit 6",
    "context": "Exhibit 6: We expect INTC to represent \\~38% unit share, AMD \\~24%, ARM merchant \\~19%, and ARM custom \\~18% by CY30 Server CPU TAM (mn units) and Unit Market Share Outlook"
  },
  {
    "figure_id": "F165",
    "report_id": "R020",
    "label": "Exhibit 8",
    "context": "Exhibit 8: We expect server CPUs to make up 8%+ of total DC TAM value over time, modestly expanding over time as their roles increase in agentic AI workloads Server CPU as a \\% of DC Systems TAM"
  },
  {
    "figure_id": "F166",
    "report_id": "R020",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Server CPU TAM could reach \\$170bn+ by CY30E, with AI CPUs representing 80%+ Server CPU TAM and AI Server CPU as a % of mix"
  },
  {
    "figure_id": "F167",
    "report_id": "R020",
    "label": "Exhibit 16",
    "context": "Exhibit 16: NVDA will begin offering standalone Vera CPU racks, alongside the Vera Rubin Platform beginning in 2H26, more directly addressing previously unaddressed or overlooked workloads in AI inference Nvidia Vera Rubin SuperPOD"
  },
  {
    "figure_id": "F168",
    "report_id": "R020",
    "label": "Exhibit 17",
    "context": "Exhibit 17: QCOM only expected to grow at a 4% CAGR between FY25-FY29E due to handset market softness and Apple roll-off"
  },
  {
    "figure_id": "F169",
    "report_id": "R020",
    "label": "Exhibit 18",
    "context": "Exhibit 18: QCOM diversification is underway, though Data Center revenues likely only \\$3bn or \\~6% by FY29E"
  },
  {
    "figure_id": "F170",
    "report_id": "R020",
    "label": "Exhibit 19",
    "context": "In that regime, CPUs were necessary but largely secondary — responsible for feeding accelerators, preprocessing data, tokenization, scheduling, storage access, and orchestration. As a result, AI accelerator spend grew far faster than CPU spend particularly bet"
  },
  {
    "figure_id": "F171",
    "report_id": "R020",
    "label": "Exhibit 20",
    "context": "Exhibit 20: AI accelerators as a % of total data center compute spend has risen to 85% by 2025 (CPUs 15%), from just 26% in 2021 (CPUs 74%) before the rise of AI compute demand CPUs vs. AI Accelerators TAM (%)"
  },
  {
    "figure_id": "F172",
    "report_id": "R020",
    "label": "Exhibit 21",
    "context": "Exhibit 21: LLM inference process can also be broken into three phases: load phase, prefill phase, and decode phase LLM Inference Process in Three Phases ```mermaid graph LR"
  },
  {
    "figure_id": "F173",
    "report_id": "R020",
    "label": "Exhibit 24",
    "context": "Exhibit 24: NVDA will begin offering standalone Vera CPU racks, alongside the Vera Rubin Platform beginning in 2H26, more directly addressing previously unaddressed or overlooked workloads in AI inference Nvidia Vera Rubin SuperPOD"
  },
  {
    "figure_id": "F174",
    "report_id": "R020",
    "label": "Exhibit 25",
    "context": "Exhibit 25: Each Vera Rubin pod contains 1,152 Rubin GPUs, 512 Vera CPUs (as part of compute), and potentially another 576 Vera CPUs (standalone) Nvidia Vera Rubin SuperPOD, full pod of 40 racks Black-and-white architectural rende"
  },
  {
    "figure_id": "F175",
    "report_id": "R021",
    "label": "Figure 1",
    "context": "Figure 1. PRC weekly polysilicon prices in the week ended Jun 10 © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 2. PRC weekly polysilicon price"
  },
  {
    "figure_id": "F176",
    "report_id": "R021",
    "label": "Figure 3",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 3. PRC weekly wafer price"
  },
  {
    "figure_id": "F177",
    "report_id": "R021",
    "label": "Figure 4",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 4. PRC weekly cell price"
  },
  {
    "figure_id": "F178",
    "report_id": "R021",
    "label": "Figure 5",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 5. PRC weekly module price"
  },
  {
    "figure_id": "F179",
    "report_id": "R021",
    "label": "Figure 6",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 6. PRC weekly solar glass price"
  },
  {
    "figure_id": "F180",
    "report_id": "R023",
    "label": "Figure 1",
    "context": "Figure 1: China Passenger Car Monthly Wholesale Volume 1,000 units, %"
  },
  {
    "figure_id": "F181",
    "report_id": "R025",
    "label": "Exhibit 1",
    "context": "Exhibit 1: China Net Import Reliance for PE China Net Import Reliance for PE"
  },
  {
    "figure_id": "F182",
    "report_id": "R025",
    "label": "Exhibit 2",
    "context": "Exhibit 2: MSe 2026 US PE contract expectations, alongside (i) a scenario where incremental US exports drive higher prices and (ii) another where the reversion to a lower mean is accelerated"
  },
  {
    "figure_id": "F183",
    "report_id": "R025",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Sinopec and Petrochina Polyolefin Inventories (PE & PP)"
  },
  {
    "figure_id": "F184",
    "report_id": "R025",
    "label": "Exhibit 4",
    "context": "Exhibit 4: North American Polyethylene Prices"
  },
  {
    "figure_id": "F185",
    "report_id": "R025",
    "label": "Exhibit 6",
    "context": "Exhibit 6: US PE Prices, Chinese PE prices and the difference"
  },
  {
    "figure_id": "F186",
    "report_id": "R025",
    "label": "Exhibit 7",
    "context": "Exhibit 7: US PE contract prices vs. spot domestic-implied contract prices (based on a regression with domestic spot price averages with 0.92 r-squared)"
  },
  {
    "figure_id": "F187",
    "report_id": "R025",
    "label": "Exhibit 9",
    "context": "Exhibit 9: \\~3.5kMT excess Chinese inventory draw down scenario Exhibit 10: China Net Import Reliance Illustrative Iran-conflict Impact to 2026 and normalization post-2026 China Net Import Reliance for PE"
  },
  {
    "figure_id": "F188",
    "report_id": "R025",
    "label": "Exhibit 11",
    "context": "Exhibit 11: East-to-West freight costs per lb of PE"
  },
  {
    "figure_id": "F189",
    "report_id": "R025",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Chinese Exports of Packaging and Containers"
  },
  {
    "figure_id": "F190",
    "report_id": "R026",
    "label": "FIGURE 1",
    "context": "Looking at the breakdown, PPI gains remain highly concentrated in upstream sectors. The producer goods PPI for mining (May: 15.8% y/y, April: 10.6%, March: 2.0%) and raw materials (May: 9.2%, April: 7.1%, March: 1.1%) accelerated, while manufacturing PPI picke"
  },
  {
    "figure_id": "F191",
    "report_id": "R026",
    "label": "FIGURE 2",
    "context": "FIGURE 2. ...led by non-ferrous metals and energy-related sectors"
  },
  {
    "figure_id": "F192",
    "report_id": "R026",
    "label": "FIGURE 3",
    "context": "FIGURE 3. Energy remains a key driver of headline CPI... pp contribution to CPI inflation (% y/y)"
  },
  {
    "figure_id": "F193",
    "report_id": "R026",
    "label": "FIGURE 4",
    "context": "FIGURE 4. ...while core and services CPI moderated"
  },
  {
    "figure_id": "F194",
    "report_id": "R026",
    "label": "FIGURE 5",
    "context": "FIGURE 5. Auto prices continued to drop..."
  },
  {
    "figure_id": "F195",
    "report_id": "R026",
    "label": "FIGURE 6",
    "context": "FIGURE 6. ...and so did housing rentals"
  },
  {
    "figure_id": "F196",
    "report_id": "R029",
    "label": "Exhibit 1",
    "context": "Exhibit 1: We expect China's AFD to widen in H2 after narrowing in Q2"
  },
  {
    "figure_id": "F197",
    "report_id": "R030",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Household financial asset growth remained above 10%... China household financial assets, Rmb bn"
  },
  {
    "figure_id": "F198",
    "report_id": "R030",
    "label": "Exhibit 3",
    "context": "Exhibit 3: The PBOC withdrew liquidity over the past three months Monthly PBoC Liquidity Injection/(withdrawal), Rmb mn"
  },
  {
    "figure_id": "F199",
    "report_id": "R030",
    "label": "Exhibit 5",
    "context": "Exhibit 5: AIA's valuation is more appealing"
  },
  {
    "figure_id": "F200",
    "report_id": "R030",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Net new money as a percentage of outstanding AUM"
  },
  {
    "figure_id": "F201",
    "report_id": "R030",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Net New AUM and Invested Asset forecasts Net New Money and Invested Assets"
  },
  {
    "figure_id": "F202",
    "report_id": "R031",
    "label": "Exhibit 1",
    "context": "Uma Menon Aman Jain We see the Indian power sector a structural and not a cyclical story, but the sector has traded more like air-conditioner stocks - buy before summer and sell before onset of monsoons. The sector peaked in mid-CY24, post which demand slowed "
  },
  {
    "figure_id": "F203",
    "report_id": "R031",
    "label": "Exhibit 2",
    "context": "EXHIBIT 2: Exchange: Buy-Sell ratio has come down from earlier levels, indicating an easing in the tight demand-supply situation..."
  },
  {
    "figure_id": "F204",
    "report_id": "R031",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: But on disaggregating by time slot, we continue to see the evening situation being tight in the power sector"
  },
  {
    "figure_id": "F205",
    "report_id": "R031",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: Spot power prices: While overall spot prices have come down, evening continues to be high, and also the day-evening arbitrage is increasing"
  },
  {
    "figure_id": "F206",
    "report_id": "R031",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: Power demand growth vs. GDP growth: FY26 saw another year of moderated demand growth, however FY27 demand so far looks strong. We retain our 1x real gdp long term view for power demand growth"
  },
  {
    "figure_id": "F207",
    "report_id": "R031",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: Power demand: May and June 2026 saw over 10% power demand YoY growth benefitting from a low base last year Power demand YoY growth by month (%)"
  },
  {
    "figure_id": "F208",
    "report_id": "R031",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: Rainfall in 2026 is expected to be much lower than last year EXHIBIT 9: CY2026: Monthly power demand growth vs. our estimates"
  },
  {
    "figure_id": "F209",
    "report_id": "R031",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: Rainfall in 2026 is expected to be much lower than last year EXHIBIT 9: CY2026: Monthly power demand growth vs. our estimates"
  },
  {
    "figure_id": "F210",
    "report_id": "R031",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: Power demand growth accelerating globally"
  },
  {
    "figure_id": "F211",
    "report_id": "R031",
    "label": "Exhibit 11",
    "context": "EXHIBIT 11: Cost of sourcing power by state DISCOMs on a downward trend with revenues realized increasing"
  },
  {
    "figure_id": "F212",
    "report_id": "R031",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: State DISCOMs have improved in terms of profitability during FY25 on an overall basis YoY change in accumulated losses (Rs. Bn)"
  },
  {
    "figure_id": "F213",
    "report_id": "R031",
    "label": "Exhibit 14",
    "context": "EXHIBIT 13: Limited thermal capacity additions next 3 yrs"
  },
  {
    "figure_id": "F214",
    "report_id": "R031",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: Power demand-supply: We see power shortages continue next 3 years, and a need for 15 GW/yr of BESS to reduce the gap... India - Peak Demand-Supply (GW)"
  },
  {
    "figure_id": "F215",
    "report_id": "R031",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: Valuations: No longer cheap compared to last cycle, NTPC and PFC still lower though Power sector valuations (Last filed P/B) along with exchange prices EXHIBIT 16: Global utilities: EV to 12month forward EBITDA"
  },
  {
    "figure_id": "F216",
    "report_id": "R031",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: Valuations: No longer cheap compared to last cycle, NTPC and PFC still lower though Power sector valuations (Last filed P/B) along with exchange prices EXHIBIT 16: Global utilities: EV to 12month forward EBITDA"
  },
  {
    "figure_id": "F217",
    "report_id": "R031",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 17: Global utilities 12m fwd P/E comparison 12M Fwd P/E (As of 10 June 2026)"
  },
  {
    "figure_id": "F218",
    "report_id": "R031",
    "label": "EXHIBIT 18",
    "context": "EXHIBIT 18: Global utilities P/B comparison Price to book (Last filed) (As of 10 June 2026)"
  },
  {
    "figure_id": "F219",
    "report_id": "R032",
    "label": "Exhibit 1",
    "context": "EXHIBIT 1: WFE imports to China has been on a constant rise... Total China WFE imports (USD bn)"
  },
  {
    "figure_id": "F220",
    "report_id": "R032",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: ...but Japan has been constantly dropping market share since 2022."
  },
  {
    "figure_id": "F221",
    "report_id": "R032",
    "label": "Exhibit 3",
    "context": "EXHIBIT 3: JPY has depreciated 31.5% over the last 5 years."
  },
  {
    "figure_id": "F222",
    "report_id": "R032",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: FX may have some impact on Japan's market share loss as they charge customers mostly in JPY."
  },
  {
    "figure_id": "F223",
    "report_id": "R032",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: Overall, Japanese vendors have lost some market share in 2025..."
  },
  {
    "figure_id": "F224",
    "report_id": "R032",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: ...and the trend looks more pronounced for the 4 segments with Japanese exposure."
  },
  {
    "figure_id": "F225",
    "report_id": "R032",
    "label": "Exhibit 10",
    "context": "EXHIBIT 7: TEL China's sales declined in FY26... FY22-FY26: TEL China sales"
  },
  {
    "figure_id": "F226",
    "report_id": "R032",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: ...as did Screen's..."
  },
  {
    "figure_id": "F227",
    "report_id": "R032",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: ...and Kokusai's, but we expect them to resume growth. FY22-FY26: Kokusai China sales"
  },
  {
    "figure_id": "F228",
    "report_id": "R032",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: Over the last 2 months, SPEs have significantly underperformed analog (Renesas) and commodity (Ibiden / Sumco)."
  },
  {
    "figure_id": "F229",
    "report_id": "R032",
    "label": "Exhibit 11",
    "context": "EXHIBIT 11: Chinese WFE market is growing, and self-sufficiency is expected to increase further. China Wafer Fab Equipment (WFE) TAM and Domestic Share USD bn"
  },
  {
    "figure_id": "F230",
    "report_id": "R032",
    "label": "Exhibit 12",
    "context": "EXHIBIT 12: Litho intensity was notably higher since 2023 onwards in China."
  },
  {
    "figure_id": "F231",
    "report_id": "R032",
    "label": "Exhibit 13",
    "context": "EXHIBIT 13: Conversely, Malaysia / Singapore have been gaining market share in recent years."
  },
  {
    "figure_id": "F232",
    "report_id": "R032",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: Thermal processes, CMP, Dry etch, Cleaning, and Deposition are the segments in which China has achieved some degree of self-sufficiency. EXHIBIT 15: Japanese market share in Dry etch has dropped the most sharply."
  },
  {
    "figure_id": "F233",
    "report_id": "R032",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 16: Japanese Thermal process equipments has been consistently losing market share."
  },
  {
    "figure_id": "F234",
    "report_id": "R032",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 17: Japan is losing market share in dry etch mainly to Malaysia, and 2026 YTD to Taiwan also. Market share among global players (excluding China local) EXHIBIT 18: TEL has a dominant market share in dielectric etch..."
  },
  {
    "figure_id": "F235",
    "report_id": "R032",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 17: Japan is losing market share in dry etch mainly to Malaysia, and 2026 YTD to Taiwan also. Market share among global players (excluding China local) EXHIBIT 18: TEL has a dominant market share in dielectric etch..."
  },
  {
    "figure_id": "F236",
    "report_id": "R032",
    "label": "EXHIBIT 19",
    "context": "EXHIBIT 19: ...but has a minimal exposure to conductor etch."
  },
  {
    "figure_id": "F237",
    "report_id": "R032",
    "label": "EXHIBIT 20",
    "context": "EXHIBIT 20: In thermal process, Japan is losing market share to both US and Singapore. Market share among global players (excluding China local) EXHIBIT 21: TEL's dry etch market share has declined significantly in 2025."
  },
  {
    "figure_id": "F238",
    "report_id": "R032",
    "label": "EXHIBIT 20",
    "context": "EXHIBIT 20: In thermal process, Japan is losing market share to both US and Singapore. Market share among global players (excluding China local) EXHIBIT 21: TEL's dry etch market share has declined significantly in 2025."
  },
  {
    "figure_id": "F239",
    "report_id": "R032",
    "label": "EXHIBIT 22",
    "context": "EXHIBIT 22: Japanese companies seem to have dropped significant market share for thermal process."
  },
  {
    "figure_id": "F240",
    "report_id": "R032",
    "label": "EXHIBIT 23",
    "context": "EXHIBIT 23: Among foreign vendors, LRCX has gained market share within etch."
  },
  {
    "figure_id": "F241",
    "report_id": "R032",
    "label": "EXHIBIT 24",
    "context": "EXHIBIT 24: Among foreign vendors, AMAT has gained market share within thermal processes."
  },
  {
    "figure_id": "F242",
    "report_id": "R032",
    "label": "Exhibit 25",
    "context": "EXHIBIT 25: Japanese cleaning equipment has gained market share over the years."
  },
  {
    "figure_id": "F243",
    "report_id": "R032",
    "label": "EXHIBIT 26",
    "context": "Market share among global players (excluding China local)"
  },
  {
    "figure_id": "F244",
    "report_id": "R032",
    "label": "EXHIBIT 27",
    "context": "EXHIBIT 27: Japan is losing some market share in 2026 YTD to Austria."
  },
  {
    "figure_id": "F245",
    "report_id": "R032",
    "label": "EXHIBIT 28",
    "context": "EXHIBIT 28: For cleaning, Screen / TEL's 2025 market share declined significantly."
  },
  {
    "figure_id": "F246",
    "report_id": "R032",
    "label": "EXHIBIT 29",
    "context": "EXHIBIT 29: Japan WFE vendors' deposition market share declined in 2025."
  },
  {
    "figure_id": "F247",
    "report_id": "R033",
    "label": "Figure 1",
    "context": "Figure 1. NEV Wholesale Volume (units) by Major OEMs © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 2. NEV-PV Monthly Sales Volume and YoY Change"
  },
  {
    "figure_id": "F248",
    "report_id": "R033",
    "label": "Figure 3",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 3. BEV vs PHEV growth rate"
  },
  {
    "figure_id": "F249",
    "report_id": "R033",
    "label": "Figure 4",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 4. NEV Market share by vehicle type"
  },
  {
    "figure_id": "F250",
    "report_id": "R034",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Tier-2 players have lower store count and are also concentrated in tier-12 cities, mainly launched in 2025/2026 As of June 2026 Exhibit 3: Store open trajectory of leading tier-1 players vs Busy Ming/Wanchen at early sta"
  },
  {
    "figure_id": "F251",
    "report_id": "R035",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Pop Mart's online sales growth in May and 2Q26-to-date growth were both slower sequentially based on the data we track Pop Mart China online sales growth"
  },
  {
    "figure_id": "F252",
    "report_id": "R035",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Labubu's resale prices of Sanrio/FIFA series slightly corrected in May for the SKUs we track Labubu plush toy price premium in secondary market"
  },
  {
    "figure_id": "F253",
    "report_id": "R035",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Pop Mart's plush toy supply on Douyin slightly moderated in May"
  },
  {
    "figure_id": "F254",
    "report_id": "R035",
    "label": "Exhibit 4",
    "context": "As of Jun 6, 2026."
  },
  {
    "figure_id": "F255",
    "report_id": "R035",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Most adult IPs saw sequential sales volume increase in May, except for Pokemon Sales volume in Bloks Tmall flagship store"
  },
  {
    "figure_id": "F256",
    "report_id": "R035",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Sales value in Bloks Tmall flagship store Sales value in Bloks Tmall flagship store"
  },
  {
    "figure_id": "F257",
    "report_id": "R035",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Pop Mart US credit card sales decelerated sequentially in 2Q26-to-date Pop Mart US credit card sales (quarterly)"
  },
  {
    "figure_id": "F258",
    "report_id": "R035",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Pop Mart US credit card sales decline narrowed to 36% in May vs. 43% yoy decline in Apr Pop Mart US credit card sales (weekly yoy)"
  },
  {
    "figure_id": "F259",
    "report_id": "R035",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Labubu Google search index stabilized in the US Google Trend data for different IPs in the US"
  },
  {
    "figure_id": "F260",
    "report_id": "R035",
    "label": "Exhibit 11",
    "context": "Global Google Trends data for Labubu (based on absolute search volume), YTD"
  },
  {
    "figure_id": "F261",
    "report_id": "R035",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Pop Mart APP MAU in US/ASEAN picked up sequentially in May; while Europe MAU remained to decline slightly Pop Mart APP overseas MAU"
  },
  {
    "figure_id": "F262",
    "report_id": "R035",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Miniso US credit card sales growth re-accelerated to $+31\\%$ in May from $+19\\%$ yoy in Apr"
  },
  {
    "figure_id": "F263",
    "report_id": "R035",
    "label": "Exhibit 12",
    "context": "Global Google Trends data for Labubu (based on absolute search volume), YTD Google search volume of Labubu, weekly"
  },
  {
    "figure_id": "F264",
    "report_id": "R035",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Miniso's US credit card sales growth decelerated in 2Q26-to-date vs. 1Q26 Miniso US credit card sales (quarterly)"
  },
  {
    "figure_id": "F265",
    "report_id": "R035",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Consumer sentiment in US/Singapore/Indonesia deteriorated, while sentiment in Malaysia/Euro area slightly recovered"
  },
  {
    "figure_id": "F266",
    "report_id": "R035",
    "label": "Exhibit 17",
    "context": "Exhibit 17: P/E band of GS covered IP retailers in China"
  },
  {
    "figure_id": "F267",
    "report_id": "R036",
    "label": "Figure 1",
    "context": "Figure 1: Semi ex-memory revenue YoY (May-24 onwards)"
  },
  {
    "figure_id": "F268",
    "report_id": "R036",
    "label": "Figure 3",
    "context": "Figure 3: Semi revenue (monthly) and YoY"
  },
  {
    "figure_id": "F269",
    "report_id": "R036",
    "label": "Figure 5",
    "context": "Figure 5: Semi ASP and YoY"
  },
  {
    "figure_id": "F270",
    "report_id": "R036",
    "label": "Figure 2",
    "context": "Figure 2: Memory revenue YoY (May-24 onwards)"
  },
  {
    "figure_id": "F271",
    "report_id": "R036",
    "label": "Figure 4",
    "context": "Figure 4: Semi units (monthly) and YoY"
  },
  {
    "figure_id": "F272",
    "report_id": "R036",
    "label": "Figure 6",
    "context": "Figure 6: Semi ex-memory revenue (monthly) and YoY"
  },
  {
    "figure_id": "F273",
    "report_id": "R036",
    "label": "Figure 7",
    "context": "Figure 7: Semi ex-memory units and YoY"
  },
  {
    "figure_id": "F274",
    "report_id": "R036",
    "label": "Figure 9",
    "context": "Figure 9: Memory revenue (monthly) and YoY"
  },
  {
    "figure_id": "F275",
    "report_id": "R036",
    "label": "Figure 11",
    "context": "Figure 11: Memory ASP and YoY"
  },
  {
    "figure_id": "F276",
    "report_id": "R036",
    "label": "Figure 8",
    "context": "Figure 8: Semi ex-memory ASP and YoY"
  },
  {
    "figure_id": "F277",
    "report_id": "R036",
    "label": "Figure 10",
    "context": "Figure 10: Memory units and YoY"
  },
  {
    "figure_id": "F278",
    "report_id": "R037",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Taiwan Tech: Monthly revenue – May 2026"
  },
  {
    "figure_id": "F279",
    "report_id": "R038",
    "label": "Exhibit 2",
    "context": "Exhibit 2: PET Prices (Weekly)"
  },
  {
    "figure_id": "F280",
    "report_id": "R038",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Hog/Piglet/Pork Price (Weekly)"
  },
  {
    "figure_id": "F281",
    "report_id": "R038",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Palm Oil Spot Price (Daily)"
  },
  {
    "figure_id": "F282",
    "report_id": "R038",
    "label": "Exhibit 7",
    "context": "Exhibit 7: CPI and Food CPI"
  },
  {
    "figure_id": "F283",
    "report_id": "R038",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Soybean Price (Weekly)"
  },
  {
    "figure_id": "F284",
    "report_id": "R038",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Soybean Futures Price (Daily)"
  },
  {
    "figure_id": "F285",
    "report_id": "R038",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Soybean Imports (Monthly)"
  },
  {
    "figure_id": "F286",
    "report_id": "R038",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Soybean Crushing Margin"
  },
  {
    "figure_id": "F287",
    "report_id": "R038",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Soybean Meal Spot Price (Weekly)"
  },
  {
    "figure_id": "F288",
    "report_id": "R038",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Soybean Meal Futures Price (Daily)"
  },
  {
    "figure_id": "F289",
    "report_id": "R038",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Soybean Meal Spot Price (Daily)"
  },
  {
    "figure_id": "F290",
    "report_id": "R038",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Soybean Oil Spot Price (Weekly)"
  },
  {
    "figure_id": "F291",
    "report_id": "R038",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Soybean Oil Futures Price (Daily)"
  },
  {
    "figure_id": "F292",
    "report_id": "R038",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Soybean Oil Spot Price (Daily)"
  },
  {
    "figure_id": "F293",
    "report_id": "R038",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Palm Oil Spot Price (Weekly)"
  },
  {
    "figure_id": "F294",
    "report_id": "R038",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Palm Oil Futures Price (Daily)"
  },
  {
    "figure_id": "F295",
    "report_id": "R038",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Palm Oil Spot Price (Daily)"
  },
  {
    "figure_id": "F296",
    "report_id": "R038",
    "label": "Exhibit 21",
    "context": "Exhibit 21: Rapeseed Oil Spot Price (Weekly)"
  },
  {
    "figure_id": "F297",
    "report_id": "R038",
    "label": "Exhibit 22",
    "context": "Exhibit 22: Rapeseed Oil Futures Price (Daily)"
  },
  {
    "figure_id": "F298",
    "report_id": "R038",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Rapeseed Spot Price (Weekly)"
  },
  {
    "figure_id": "F299",
    "report_id": "R038",
    "label": "Exhibit 24",
    "context": "Exhibit 24: Wheat Spot Price (Weekly)"
  },
  {
    "figure_id": "F300",
    "report_id": "R038",
    "label": "Exhibit 25",
    "context": "Exhibit 25: Wheat Futures Price (Daily)"
  },
  {
    "figure_id": "F301",
    "report_id": "R038",
    "label": "Exhibit 26",
    "context": "Exhibit 26: Flour Spot Price (Weekly)"
  },
  {
    "figure_id": "F302",
    "report_id": "R038",
    "label": "Exhibit 27",
    "context": "Exhibit 27: Rice Spot Price (Weekly)"
  },
  {
    "figure_id": "F303",
    "report_id": "R038",
    "label": "Exhibit 28",
    "context": "Exhibit 28: Rice Futures Price (Daily)"
  },
  {
    "figure_id": "F304",
    "report_id": "R038",
    "label": "Exhibit 29",
    "context": "Exhibit 29: Corn Spot Price (Weekly)"
  },
  {
    "figure_id": "F305",
    "report_id": "R038",
    "label": "Exhibit 30",
    "context": "Exhibit 30: Corn Futures Price (Daily)"
  },
  {
    "figure_id": "F306",
    "report_id": "R038",
    "label": "Exhibit 31",
    "context": "Exhibit 31: Barley Spot Price"
  },
  {
    "figure_id": "F307",
    "report_id": "R038",
    "label": "Exhibit 32",
    "context": "Exhibit 32: Sugar Spot Price"
  },
  {
    "figure_id": "F308",
    "report_id": "R038",
    "label": "Exhibit 33",
    "context": "Exhibit 33: Sugar Futures Price"
  },
  {
    "figure_id": "F309",
    "report_id": "R038",
    "label": "Exhibit 34",
    "context": "Exhibit 34: Milk Powder Price (Weekly)"
  },
  {
    "figure_id": "F310",
    "report_id": "R038",
    "label": "Exhibit 35",
    "context": "Exhibit 35: Raw Milk Price (Monthly)"
  },
  {
    "figure_id": "F311",
    "report_id": "R038",
    "label": "Exhibit 36",
    "context": "Exhibit 36: Hog/Piglet Price (Weekly)"
  },
  {
    "figure_id": "F312",
    "report_id": "R038",
    "label": "Exhibit 37",
    "context": "Exhibit 37: Hog/Piglet/Pork Price (Weekly)"
  },
  {
    "figure_id": "F313",
    "report_id": "R038",
    "label": "Exhibit38",
    "context": "Exhibit38: Pork Wholesale/Retail Price (Weekly)"
  },
  {
    "figure_id": "F314",
    "report_id": "R038",
    "label": "Exhibit 39",
    "context": "Exhibit 39: US Hog and Corn Futures (Monthly)"
  },
  {
    "figure_id": "F315",
    "report_id": "R038",
    "label": "Exhibit 40",
    "context": "Exhibit 40: US Hog-raising Profit (Monthly)"
  },
  {
    "figure_id": "F316",
    "report_id": "R038",
    "label": "Exhibit 41",
    "context": "Exhibit 41: Retail Price of White Chicken and Duck (Weekly)"
  },
  {
    "figure_id": "F317",
    "report_id": "R038",
    "label": "Exhibit 42",
    "context": "Exhibit 42: Wholesale Price of White Chicken (Weekly)"
  },
  {
    "figure_id": "F318",
    "report_id": "R038",
    "label": "Exhibit 43",
    "context": "Exhibit 43: Retail Price: Beef (Weekly)"
  },
  {
    "figure_id": "F319",
    "report_id": "R038",
    "label": "Exhibit 44",
    "context": "Exhibit 44: Wholesale Price: Beef (Daily)"
  },
  {
    "figure_id": "F320",
    "report_id": "R038",
    "label": "Exhibit 45",
    "context": "Exhibit 45: China: Cotton Futures Prices"
  },
  {
    "figure_id": "F321",
    "report_id": "R038",
    "label": "Exhibit 46",
    "context": "Exhibit 46: DDGS Price (Weekly)"
  },
  {
    "figure_id": "F322",
    "report_id": "R038",
    "label": "Exhibit 47",
    "context": "Exhibit 47: PET Price (Weekly)"
  },
  {
    "figure_id": "F323",
    "report_id": "R038",
    "label": "Exhibit 48",
    "context": "Exhibit 48: Tin Price (Weekly)"
  },
  {
    "figure_id": "F324",
    "report_id": "R038",
    "label": "Exhibit 49",
    "context": "Exhibit 49: Fiberboard Price (Weekly)"
  },
  {
    "figure_id": "F325",
    "report_id": "R038",
    "label": "Exhibit 50",
    "context": "Exhibit 50: Pulp – Long Fiber & Short Fiber"
  },
  {
    "figure_id": "F326",
    "report_id": "R038",
    "label": "Exhibit 51",
    "context": "Exhibit 51: Guangxi Molasses Price Index"
  },
  {
    "figure_id": "F327",
    "report_id": "R038",
    "label": "Exhibit 52",
    "context": "Exhibit 52: Gold Spot Price (Weekly)"
  },
  {
    "figure_id": "F328",
    "report_id": "R038",
    "label": "Exhibit 53",
    "context": "Exhibit 53: Platinum Spot Price (Weekly)"
  },
  {
    "figure_id": "F329",
    "report_id": "R038",
    "label": "Exhibit 54",
    "context": "Exhibit 54: Diamond – Average Price (Weekly)"
  },
  {
    "figure_id": "F330",
    "report_id": "R038",
    "label": "Exhibit 55",
    "context": "Exhibit 55: Silver Spot Price (Weekly)"
  },
  {
    "figure_id": "F331",
    "report_id": "R038",
    "label": "Exhibit 56",
    "context": "Exhibit 56: Copper, Aluminum, Steel Price Growth Rates"
  },
  {
    "figure_id": "F332",
    "report_id": "R038",
    "label": "Exhibit 57",
    "context": "Exhibit 57: Copper Spot Price (Daily)"
  },
  {
    "figure_id": "F333",
    "report_id": "R038",
    "label": "Exhibit58",
    "context": "Exhibit58: Aluminium Spot Price (Daily)"
  },
  {
    "figure_id": "F334",
    "report_id": "R039",
    "label": "Exhibit 1",
    "context": "EXHIBIT 1: Rapid evolution of World Action Models (WAMs) ```mermaid graph TD"
  },
  {
    "figure_id": "F335",
    "report_id": "R039",
    "label": "Exhibit 3",
    "context": "EXHIBIT 3: The Physical AI and Robotic ecosystem ```mermaid graph TD"
  },
  {
    "figure_id": "F336",
    "report_id": "R039",
    "label": "Exhibit 2",
    "context": "EXHIBIT 4: Keyence generates \\~20% of revenue from new products every year and steadily expands its product scope. ```mermaid graph TD"
  },
  {
    "figure_id": "F337",
    "report_id": "R040",
    "label": "Figure 1",
    "context": "Figure 1: Aggregated top 3 MB vendors' quarterly shipments and qoq trend"
  },
  {
    "figure_id": "F338",
    "report_id": "R040",
    "label": "Figure 3",
    "context": "Figure 3: Aggregated top 3 MB vendors' quarterly shipments and yoy trend"
  },
  {
    "figure_id": "F339",
    "report_id": "R040",
    "label": "Figure 2",
    "context": "Figure 2: Aggregated top 3 VGA card vendors' quarterly shipments and qoq trend"
  },
  {
    "figure_id": "F340",
    "report_id": "R040",
    "label": "Figure 4",
    "context": "Figure 4: Aggregated top 3 VGA card vendors' quarterly shipments and yoy trend"
  },
  {
    "figure_id": "F341",
    "report_id": "R041",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Domestic-operated flights"
  },
  {
    "figure_id": "F342",
    "report_id": "R041",
    "label": "Exhibit 3",
    "context": "Exhibit 3: China's non-domestic capacity YoY"
  },
  {
    "figure_id": "F343",
    "report_id": "R041",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Railway is gaining market share vs. air since Mar-26."
  },
  {
    "figure_id": "F344",
    "report_id": "R041",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Domestic air pax growth at SIAC, GBIA and BCIA slowed to 3-4% YoY in Apr-26 from 6-10% YoY in 1Q26"
  },
  {
    "figure_id": "F345",
    "report_id": "R041",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Non-domestic traffic growth also softened to 4-18% YoY in Apr-26 from 7-24% YoY in 1Q26"
  },
  {
    "figure_id": "F346",
    "report_id": "R041",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Duty-free rent at SIAC dropped 49% YoY in 1Q26 due mainly to rent-free period, we think"
  },
  {
    "figure_id": "F347",
    "report_id": "R041",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Chinese airports under our coverage all underperformed respective indexes YTD2026 Chinese airports relative share performance YTD2026"
  },
  {
    "figure_id": "F348",
    "report_id": "R041",
    "label": "Exhibit 10",
    "context": "Exhibit 10: We estimate GBIA's net profit will drop by 54% YoY in 2026 GBIA: Net profit (Rmb mn)"
  },
  {
    "figure_id": "F349",
    "report_id": "R041",
    "label": "Exhibit 12",
    "context": "Exhibit 12: We estimate SIAC's net profit will continue to grow by \\~20% YoY in 2026-27, before dropping YoY in 2028 due to capacity expansion SIAC: Net profit (Rmb mn)"
  },
  {
    "figure_id": "F350",
    "report_id": "R041",
    "label": "Exhibit 11",
    "context": "Exhibit 11: GBIA stock is trading at 31x 2026e P/E and 26x 2027e P/E vs. historical average of 24x"
  },
  {
    "figure_id": "F351",
    "report_id": "R041",
    "label": "Exhibit 13",
    "context": "Exhibit 13: SIAC stock is trading at 22x 2026e P/E vs. historical average of 30x since listing"
  },
  {
    "figure_id": "F352",
    "report_id": "R041",
    "label": "Exhibit 14",
    "context": "Exhibit 14: We believe BCIA's earnings growth could be slow if additional flight slots are not added soon BCIA: Net profit (Rmb mn)"
  },
  {
    "figure_id": "F353",
    "report_id": "R041",
    "label": "Exhibit 15",
    "context": "Exhibit 15: BCIA stock is trading at 0.5x 2026e P/B, lower vs. historical average of 1.0x since reopening"
  },
  {
    "figure_id": "F354",
    "report_id": "R041",
    "label": "Exhibit 22",
    "context": "Mean organ Stanley Estimates"
  },
  {
    "figure_id": "F355",
    "report_id": "R042",
    "label": "Exhibit 1",
    "context": "Exhibit 2: We outline agentic bull & bear scenarios for EBAY; upside largely driven by incremental GMV growth EBAY Agentic Scenarios: 2030 EBITDA Bear/Base/Bull Bridge"
  },
  {
    "figure_id": "F356",
    "report_id": "R042",
    "label": "Exhibit 3",
    "context": "Exhibit 3: We outline agentic bull & bear scenarios for ETSY; upside split between GMS growth and margin expansion while take rate is a concern in the bear case ETSY Agentic Scenarios: 2030 EBITDA Bear/Base/Bull Bridge"
  },
  {
    "figure_id": "F357",
    "report_id": "R042",
    "label": "Exhibit 4",
    "context": "Exhibit 4: \\~90% of EBAY's inventory is unique, which we believe positions it well - offensively & defensively - for agentic commerce EBAY Inventory Base by Type"
  },
  {
    "figure_id": "F358",
    "report_id": "R042",
    "label": "Exhibit 5",
    "context": "Exhibit 5: EBAY has 7 global authentication hubs along with 5 more partner facilities... Global Authenticity Guarantee (AG) Infrastructure Scaling global trust with over 15M items authenticated to date Canada CA Hub"
  },
  {
    "figure_id": "F359",
    "report_id": "R042",
    "label": "Exhibit 6",
    "context": "Exhibit 6: ...along with various Bespoke shipping programs across 14 countries Facilitating Cross-Border Trade Through Shipping Solutions Current Cross-Border Shipping Programs eBay International Shipping (eIS) • US • Canada"
  },
  {
    "figure_id": "F360",
    "report_id": "R042",
    "label": "Exhibit 8",
    "context": "Exhibit 8: EBAY has \\~3.0% market share within US eCommerce, although higher in its core verticals"
  },
  {
    "figure_id": "F361",
    "report_id": "R042",
    "label": "Exhibit 10",
    "context": "Exhibit 10: EBAY Agentic Bear to Bull Case Waterfall EBAY Agentic Scenarios: 2030 EBITDA Bear/Base/Bull Bridge"
  },
  {
    "figure_id": "F362",
    "report_id": "R042",
    "label": "Exhibit 13",
    "context": "Exhibit 13: At least 3/4ths of ETSY's top sellers already sell on other channels, showing most inventory is not unique to Etsy.com Do ETSY Stores Sell Elsewhere?"
  },
  {
    "figure_id": "F363",
    "report_id": "R042",
    "label": "Exhibit 14",
    "context": "Exhibit 14: ETSY has the highest take rate among 'pure' public marketplaces (those without fulfillment) Pure 3P Marketplace Take Rates"
  },
  {
    "figure_id": "F364",
    "report_id": "R042",
    "label": "Exhibit 15",
    "context": "Exhibit 15: On GOOGL's UCP Tech Council, ETSY is the smallest company - showing its outsized impact on digital infrastructure relative to its size UCP Tech Council by Market Cap (\\$B, Log Scale)"
  },
  {
    "figure_id": "F365",
    "report_id": "R042",
    "label": "Exhibit 17",
    "context": "Exhibit 17: ETSY has just $\\sim$ 1.7\\% online share within its $\\sim$ 600B TAM or a $\\sim$ 0.5\\% share among its $\\sim$ 2T total (online/offline) TAM Retail Sales across ETSY's Key Geographies & Categories $2T"
  },
  {
    "figure_id": "F366",
    "report_id": "R042",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Despite its early lead, ETSY has seen smaller incremental gains in AI referral traffic"
  },
  {
    "figure_id": "F367",
    "report_id": "R042",
    "label": "Exhibit 20",
    "context": "Exhibit 20: ETSY Agentic Bull/Bear Waterfall ETSY Agentic Scenarios: 2030 EBITDA Bear/Base/Bull Bridge"
  },
  {
    "figure_id": "F368",
    "report_id": "R043",
    "label": "Exhibit 2",
    "context": "Exhibit 2: India: Expect domestic production growth to pick up as new capacities ramp up through the year; demand likely to remain good"
  },
  {
    "figure_id": "F369",
    "report_id": "R043",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Gross exports of finished steel picked up recently, but should normalize as demand picks up beyond monsoons (million tons)"
  },
  {
    "figure_id": "F370",
    "report_id": "R043",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Gross imports of finished steel rose April-May, but should moderate given unfavourable pricing (million tons)"
  },
  {
    "figure_id": "F371",
    "report_id": "R043",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Finished steel inventory (non-alloy) on an absolute basis has come off (mnt)..."
  },
  {
    "figure_id": "F372",
    "report_id": "R043",
    "label": "Exhibit 6",
    "context": "Exhibit 6: ...and looks even more attractive on an inventory days outstanding basis"
  },
  {
    "figure_id": "F373",
    "report_id": "R043",
    "label": "Exhibit 7",
    "context": "Exhibit 7: International iron ore prices have remained elevated in recent months; we expect some pullback from here"
  },
  {
    "figure_id": "F374",
    "report_id": "R043",
    "label": "Exhibit 78",
    "context": "Exhibit 78: Domestic iron ore prices (NMDC) have also seen some expansion"
  },
  {
    "figure_id": "F375",
    "report_id": "R043",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Domestic iron ore prices discount vs. import parity has narrowed (%)"
  },
  {
    "figure_id": "F376",
    "report_id": "R043",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Domestic steel prices have seen some rollbacks to account for upcoming weak demand season"
  },
  {
    "figure_id": "F377",
    "report_id": "R043",
    "label": "Exhibit 13",
    "context": "Exhibit 13: India's HRC spreads: We expect support over medium term"
  },
  {
    "figure_id": "F378",
    "report_id": "R043",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Coking coal prices too have stayed higher over recent months"
  },
  {
    "figure_id": "F379",
    "report_id": "R043",
    "label": "Exhibit 12",
    "context": "Exhibit 12: India's HRC prices: Currently at \\~8% discount to import parity prices including safeguard duty"
  },
  {
    "figure_id": "F380",
    "report_id": "R043",
    "label": "Exhibit 14",
    "context": "Exhibit 14: HRC prices: Trends and expectations HRC Prices (Rs '000/t)"
  },
  {
    "figure_id": "F381",
    "report_id": "R043",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Iron ore prices: Trends and expectations NMDC Iron Ore Prices (Blended, Rs/t)"
  },
  {
    "figure_id": "F382",
    "report_id": "R043",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Coking coal prices: Trends and expectations Coking Coal Prices (Australia HCC, US$/t)"
  },
  {
    "figure_id": "F383",
    "report_id": "R043",
    "label": "Exhibit 28",
    "context": "organ Stanley Estimates"
  },
  {
    "figure_id": "F384",
    "report_id": "R046",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Longevity of the Brain: Alzheimer's, the GLP-1 Boundary, and the Next Spend Curve ```mermaid graph LR"
  },
  {
    "figure_id": "F385",
    "report_id": "R046",
    "label": "Exhibit 6",
    "context": "Exhibit 6: CBO US Population forecast Exhibit 7: CBO US Population forecast"
  },
  {
    "figure_id": "F386",
    "report_id": "R046",
    "label": "Exhibit 9",
    "context": "Exhibit 8: Average PHC spending age segment"
  },
  {
    "figure_id": "F387",
    "report_id": "R046",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Seniors drive PHC spend"
  },
  {
    "figure_id": "F388",
    "report_id": "R046",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Care for Seniors with dementia is meaningfully higher than Seniors without dementia. Dementia is the deciding cost driver."
  },
  {
    "figure_id": "F389",
    "report_id": "R046",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Healthspan (years without severe impairment) ends in the last decade of life Global Lifespan vs. Healthspan (High income countries)"
  },
  {
    "figure_id": "F390",
    "report_id": "R046",
    "label": "Exhibit 15",
    "context": "Exhibit 14: AD prevalence continues to increase, and is estimated to surpass 10M US adults by 2035 AD & MCI US Prevalence Forecast"
  },
  {
    "figure_id": "F391",
    "report_id": "R046",
    "label": "Exhibit 15",
    "context": "Exhibit 15: AD prevalence, gross spend, and per capita spend (MSe vs Alzheimer's association forecast)"
  },
  {
    "figure_id": "F392",
    "report_id": "R046",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Innovation impact on mortality (green bars signify reduced mortality rate) Exhibit 19: Mortality driven by non-communicable diseases over communicable disease) Global Health Estimates 2021: Deaths (000s)"
  },
  {
    "figure_id": "F393",
    "report_id": "R046",
    "label": "Exhibit 20",
    "context": "Exhibit 20: US major drivers of mortality 2022 Deaths in US"
  },
  {
    "figure_id": "F394",
    "report_id": "R046",
    "label": "Exhibit 25",
    "context": "Exhibit 26: TfR lead to less monoclonal antibodies (yellow) in blood vessels, reducing risk of ARIA and concentrating the drug where it's needed. Microscopic view of a branching biological structure with yellow fluorescent spots ("
  },
  {
    "figure_id": "F395",
    "report_id": "R046",
    "label": "Exhibit 27",
    "context": "Exhibit 27: TfR strategies for augmenting CNS delivery ATV.TfR TfR Brain Concentration Time"
  }
]