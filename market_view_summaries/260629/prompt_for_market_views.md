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
    "title": "JPM：亚洲央行正经历一场“油跌美升”的轮动",
    "digest": "[wechat_article.md]\n# JPM：亚洲央行正经历一场“油跌美升”的轮动\n\n过去两个月，亚洲新兴市场（EMAX）经济增速平均超过6%（季调后年化），几乎是潜在增长率的两倍。支撑这一强劲表现的是科技出口与生产的持续爆发。但这份JPM最新发布的《全球数据观察：亚洲》报告提出了一个更值得关注的结构性判断：随着中东冲突缓和、原油价格大幅回落，叠加美元重新走强，亚洲各经济体央行面临的约束条件正在发生系统性轮动。对于投资者而言，真正重要的不是当前的增长有多强，而是这种“油跌美升”的格局将如何重塑各国央行的政策路径，并由此改变不同市场的资产定价逻辑。\n\n这份报告的核心主张是：能源价格下行正在为亚洲经济下半年的增长带来上行风险，但美元走强同时也在制造新的分化——一些央行将因此获得喘息空间，另一些则可能被迫进一步收紧。理解这场轮动，是判断下半年亚洲资产配置方向的关键前提。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 能源成本下降正在成为下半年增长的超预期来源\n\n报告明确指出，中东冲突的缓和与原油价格的急剧下跌，显著缓解了亚洲地区此前面临的贸易条件恶化冲击。在此之前，亚洲经济体对中东能源的依赖使其在地缘冲突中尤为脆弱。但现实比预期更有韧性——各国通过积极从其他渠道采购能源、消耗储备以及转向替代品，避免了最坏的结果。\n\n这意味着，尽管能源逆风依然存在，二季度增长仍接近趋势水平。而展望下半年，报告认为上行风险正在积聚。科技生产继续保持强劲势头——虽然台湾5月工业产出显示科技动能较此前“滚烫”的速度有所降温，但仍在以30%的年化季环比增长运行；韩国20天出口数据同样指向强劲的出口动能，尽管近期科技涨幅更多由价格驱动。\n\n> **KC评论：** 市场对亚洲增长的担忧主要集中在中国的放缓上，但JPM认为能源价格的下跌正在成为一个被低估的正面因素。通胀预期下降将提升\n\n[... middle omitted ...]\n\n诺对各国通胀的实际影响，这些细节在完整报告中有更充分的展开。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n亚洲央行面临新抉择：油价跌了，美元涨了\n\n封面：油跌美元升\n副标题：亚洲央行政策面临新权衡\n\n最近某外资投行发了一份亚洲研报，几个有意思的点跟大家聊聊。\n\n**1. 亚洲科技出口还在高位运转**\n尽管台湾5月科技IP增速从之前的高点回落，但年化季率仍高达30%。韩国20天出口数据也显示，科技出口势头依然强劲。科技产业链的景气度，是支撑亚洲经济的重要力量。\n\n**2. 油价下跌是个好消息**\n研报指出，亚洲新兴市场（EMAX）过去两个季度增长强劲，年化季率超6%。过去中东冲突让这些依赖能源进口的经济体承压，但油价大幅回落，将改善贸易条件、压低通胀、提升居民购买力。菲律宾可能不需要加那么多息了，印度、泰国、新加坡央行也更有底气按兵不动。\n\n**3. 中国放缓的影响可能被高估**\n虽然中国下半年增速预计会明显放缓，但研报认为对亚洲的冲击有限——因为这些年亚洲对中国的出口依赖度已经下降。只有印尼和菲律宾近期对中国出口有较明显增长，其他国家影响不大。不过，如果中国内需持续疲弱，可能增加过剩产能外溢的压力。\n\n**4. 美元走强，部分央行压力上升**\n印尼盾承压，印尼央行可能被迫继续加息。韩国央行面临科技热潮+美元走强的\n\n[... middle omitted ...]\n\nwinds, therefore, 2Q growth is still tracking close to trend. Our extant forecast calls for trend-like growth in the second half of the year, but we see growing upside risks from the confluenc\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R002",
    "title": "GS：大宗商品真正的故事不在能源，而在金属与电力",
    "digest": "[wechat_article.md]\n# GS：大宗商品真正的故事不在能源，而在金属与电力\n\n当霍尔木兹海峡的航道重新开放、原油价格开始回落，市场对大宗商品的注意力似乎正在消退。但GS最新的大宗商品策略报告给出了一个截然相反的判断：大宗商品配置的价值不仅没有降低，反而在结构上变得更加重要——只是主角正在从传统的油气转向电力、铜、锂和铝。\n\n这份由Samantha Dart领衔的报告，在分析完霍尔木兹冲突的影响后，明确提出了一个核心主张：战略投资组合依然需要大宗商品，但理由正在发生变化。不再只是对冲通胀，而是应对一个更复杂的、由结构性供给约束和地缘政治重塑共同驱动的新格局。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 霍尔木兹冲突揭示了一个关键事实：能源市场的韧性并未改变长期脆弱性\n\n霍尔木兹海峡中断16周，原油和成品油价格一度分别上涨43%和63%，欧洲天然气和亚洲LNG涨幅达到50%-70%。但最终，全球市场比预期更具弹性——中国在冲突首两个月大幅削减LNG进口，至今仍压低原油进口量，这帮助限制了全球市场的紧张程度。\n\nGS团队指出，这恰恰是值得警惕的地方。市场之所以能消化这次冲击，是因为需求端主动收缩。但一旦需求反弹——他们预计冲突后原油需求将出现超过100万桶/日的战略储备补库推动——供需平衡将重新收紧。成品油市场（汽油、柴油）的回调速度将明显慢于原油。\n\n> **KC评论：** 报告在这里埋了一个关键伏笔：这次冲突的“软着陆”并非因为供给端弹性大，而是因为需求端主动“让路”。一旦需求恢复，能源市场的结构性紧张就会重新浮现。完整报告里有一张图表专门拆解了成品油供需平衡的预期路径，值得细看。\n\n更重要的是，这次冲突对全球GDP的冲击被控制在了0.4个百分点，但如果冲突持续，GS估算的冲击幅度将达到2个百分点。这个数字本身就在提醒：能源市场的尾部\n\n[... middle omitted ...]\n\n到底会在哪一年达到临界点，黄金的央行需求能否对冲ETF流出。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n能源波动后，商品配置逻辑变了\n\n商品再平衡\n\n从能源到金属，为什么还要配商品\n\n某外资投行最新研报拆解了一个核心问题：能源冲击结束后，商品的配置价值在哪里。\n\n关键结论：伊朗冲突带来的能源供给冲击，反而是理解商品长期逻辑的窗口。\n\n1/ 商品不是“涨了才配”\n研报给出三个商品能对冲股债风险的场景：\n- 供给冲击（像霍尔木兹海峡这样），通胀上行+经济走弱\n- 结构性需求支撑，供给却很难跟上\n- 财政或金融风险下，资金往实物资产跑\n\n这三个场景目前都还在，不是短期现象。\n\n2/ 能源冲击后，逻辑转向金属和电力\n伊朗冲突期间，原油和成品油价格一度涨43%-70%。但研报认为，这次冲突真正强化的是电力和金属需求——不是油和气。\n\n原因很直接：\n- 电动车加速替代\n- 可再生能源投资加码\n- 电网升级成为国家安全议题\n- AI竞赛推高电力需求\n\n这些都需要铜、锂、铝，而供给端：铜矿越来越深、品位下降、开采成本上升，新矿开发周期极长。\n\n3/ 铜的结构性缺口，政策加速了\n研报预计到2030年，电网和电力基础设施将驱动超60%的铜需求增长。同时，美国钢铝关税预期让铜提前流向美国，导致非美市场快速吃紧。\n\n铜价预测：2026\n\n[... middle omitted ...]\n\nks, like the Hormuz disruption, which might lead to higher inflation and lower economic growth, (2) structural demand support for commodities that face challenges to growing supply, and (3) a \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R003",
    "title": "摩根斯坦利：MS：融资市场正发出二季度末最危险的信号",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：融资市场正发出二季度末最危险的信号\n\n当美联储还在通过点阵图传递“一次加息”的鹰派信号时，华尔街最敏感的角落已经亮起了红灯。MS利率策略团队在6月27日发布的一份报告中直言：股票融资市场正在经历一场堪比2024年12月年末的紧张局面，二季度末发生去杠杆事件的风险正在上升。\n\n这份报告的核心判断并非来自传统宏观经济模型，而是来自一个多数投资者容易忽视的角落——AXW期货。这个捕捉标普500总收益期货与浮动利率之间价差的工具，正在发出近十年来最极端的信号。\n\n对于任何一个管理着数十亿美元资产、或正在为下半年配置做决策的投资者来说，理解这个信号的含义，可能比关注美联储下一次会议的点阵图更为紧迫。\n\n> **KC评论：** MS不是在预测经济衰退，而是在警告一个技术性的、但可能引发连锁反应的流动性事件。历史上，这类信号往往出现在市场转折点之前。完整的报告里有一张图显示，当AXW期货超过2个标准差时，标普500在随后三个月内都会出现显著回调。这张图表值得每个人仔细看一遍。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 股票融资成本已逼近历史极值，而国债融资市场却异常平静\n\n报告揭示了一个令人不安的分化：国债回购市场目前定价相当温和，隔夜GC回购报价仅为3.75/3.72，与2025年6月季度末和今年4月纳税日时的情况类似。这意味着美联储的利率走廊并未受到实质性挑战，SOFR利率大概率会稳定在目标区间内。\n\n然而，在股票融资的另一端，情况截然不同。7月到期的1个月AXW期货合约在上周五飙升至+200个基点，正在迅速逼近2024年12月年末前创下的历史最高水平。报告特意使用了10日移动平均线来平滑合约滚动的影响，即便如此，读数依然触目惊心。\n\n这种分化的本质是什么？国债融资市场受益于美联储自2025年12\n\n[... middle omitted ...]\n\n。我们会在那里分享报告的核心图表，并持续跟踪融资市场的变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美股融资压力拉警报，季末或迎动荡\n\n季末融资压力来袭\n\n美股融资成本正在快速飙升。某外资投行最新研报显示，1个月期AXW期货合约的融资利率已飙升至+200bp，接近2024年12月创下的历史极值。这个信号值得关注。\n\n为什么融资成本在涨？\n\n1️⃣ 杠杆需求远超券商资产负债表容量\n半导体板块财报后，对冲基金集中做多，但券商受GSIB附加费限制，无法无限放大杠杆。\n\n2️⃣ 融资成本已到极端水平\nAXW期货近1个月标准差超过2个σ，历史上这种极端值出现后，标普500往往会出现均值回归。\n\n3️⃣ 市场上行推力正在减弱\n当融资成本高到一定程度，杠杆买家无力继续加仓，反而可能被迫平仓，形成去杠杆螺旋。\n\n后续可能发生什么？\n\n如果融资压力持续到6月30日后，可能意味着市场需要一次明显的去杠杆事件才能让融资成本正常化。届时，投资者可能会重新审视对美国经济的乐观预期。\n\n市场对美联储加息的定价可能过高。一旦金融条件收紧，市场会减少对鹰派尾部风险的押注。\n\n两个曲线平坦化的可能路径\n\n① 美联储政策失误：前瞻性通胀数据正在走软，核心PCE下半年可能年化降至2.0%。如果美联储真按点阵图加息，市场可能视为错误。\n\n② 石油\n\n[... middle omitted ...]\n\ninancing costs prior to a quarter-end rapidly nearing those hit ahead of year-end in December 2024 encapsulate current stresses in equity funding.\n\n\\- AXW futures are 2+ standard deviations ab\n\n[... middle omitted ...]\n\nuthors are Fixed Income Research Analysts/Strategists and are not opining on or expressing recommendations on equity securities: Aryaman Singh; Shaun Zhou; Eli P Carter; Matthew Hornbach; Martin W Tobias, CFA.\n\n© 2026 MS"
  },
  {
    "id": "R004",
    "title": "美国银行：存储器超级周期可能延续到2030年",
    "digest": "[wechat_article.md]\n# 美国银行：存储器超级周期可能延续到2030年\n\n当多数人还在讨论半导体周期何时见顶时，美国银行最新研报给出了一个反直觉的判断：存储器行业的超级周期不仅没有结束，反而可能延续到2027年甚至2030年。这份基于美光科技最新财报和指引的分析，揭示了一个正在发生的结构性转变——存储器正从周期性行业转向类似台湾晶圆代工的高利润、低波动模式。\n\n报告的核心主张是：存储器行业正在经历一场由长期协议(Long-Term Agreements, LTA)驱动的结构性变革，这将从根本上改变行业的周期特征和盈利模式。这不是又一个周期高点，而是一个新范式的起点。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 美光指引揭示的五个关键信号：超级周期而非周期性反弹\n\n美光科技最新季度财报给出了几个令人瞩目的数字：5月季度营收达到410亿美元，同比增长346%；毛利率85%，营业利润率81%；对8月季度营收指引为500亿美元，意味着环比增长21%。这些数字本身已经足够惊人，但更关键的是美光管理层对行业前景的展望。\n\n美国银行分析师从中提炼出五个对亚洲存储器厂商具有深远影响的判断：\n\n第一，超级周期或芯片短缺可能持续到2027年甚至2030年。这不是一个短期现象，而是由AI需求驱动的长期结构性变化。\n\n第二，与大型科技公司和OEM的长期协议(LTA)正在增加，这有望使行业变得不那么周期性，并实现高利润——类似于台湾晶圆代工的模式。\n\n第三，新建晶圆厂并非易事，面临高建设成本、地方政府监管、电力/水供应问题等多重挑战。\n\n第四，即使到2028年，晶圆产能扩张也有限，因为需要大量洁净室用于旧厂升级，制造周期更长，前端甚至后端设备尺寸更大，先进芯片良率较低，以及HBM与常规DRAM之间较高的转换比例。\n\n第五，尽管资本支出相比正常周期翻倍以上，自\n\n[... middle omitted ...]\n\n以及HBM4对行业格局的潜在影响等未解问题，做更深入的交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n存储芯片超级周期，能持续到2027？\n\n📈 存储芯片景气周期远超预期\n\n**存储芯片的超级周期，可能比想象中更长。**\n\n某外资投行最新研报指出，存储芯片供需紧张格局有望延续到2027年甚至2030年。核心逻辑有五点：\n\n1️⃣ **长协锁定利润**：大科技公司和OEM厂正大量签署长期供货协议（LTA）。未来存储芯片价格波动会变小，行业利润更稳定，类似台积电的商业模式。\n\n2️⃣ **新厂建设困难**：建一座新晶圆厂成本极高，还面临地方政策、水电供应等限制。即便到2028年，产能扩张也有限。\n\n3️⃣ **技术升级拉长周期**：从HBM到更先进制程，生产周期变长、良率降低，前道和后道设备尺寸更大。这导致有效产能释放速度变慢。\n\n4️⃣ **资本开支翻倍**：尽管资本开支比正常周期翻了一倍多，但自由现金流仍在显著增长。说明需求太强，赚的钱远多于投入。\n\n5️⃣ **HBM4已开始贡献收入**：美光HBM4已有10亿美元销售额，同时在全球多地（美国、台湾、新加坡、日本）启动新厂建设，并下了大量EUV光刻机订单。\n\n💡 **价格竞争不会加剧**\n\n一个容易被忽视的点：存储芯片大厂越来越多用长协锁定价格，产品也转向高\n\n[... middle omitted ...]\n\nation, power/water supply issues, etc.); (4) limited wafer capacity expansion even in 2028 (lots of clean rooms needed for old fab upgrades, longer manufacturing cycles, larger sized front-end\n\n[... middle omitted ...]\n\nw in accordance with firm policies.\n\nNeither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information."
  },
  {
    "id": "R005",
    "title": "Bernstein：钠离子电池的“奇点”不在车，在储能",
    "digest": "[wechat_article.md]\n# Bernstein：钠离子电池的“奇点”不在车，在储能\n\n全球储能行业正在经历一个被多数人低估的技术拐点。过去几年，市场焦点始终落在锂价的剧烈波动和电动车渗透率的爬坡节奏上，但一份来自Bernstein的最新周报揭示了一个更值得关注的信号：钠离子电池正在从实验室验证走向商业化部署，而它的第一个引爆场景不是电动车，而是大型储能系统。\n\n这份报告汇集了过去一周全球储能产业链的数十条动态，从CATL推出全球首个公用事业级钠离子储能系统Tener Sodium，到中国钠创科技在宁夏启动10GWh钠离子电池项目，再到Hina电池与一汽解放在极寒条件下完成钠离子重卡电池测试——这些事件拼在一起，指向同一个判断：钠离子电池在储能领域的成本拐点可能比市场预期的来得更早。\n\n对于关注能源转型、电力系统投资和电池供应链格局的读者来说，这是一个需要重新校准认知框架的时刻。\n\n> **KC评论：** 市场对钠离子电池的普遍认知还停留在“能量密度低、只能用在低端两轮车”的阶段。但Bernstein这份周报的拼图显示，钠离子电池的真正突破场景是储能——在那里，能量密度不是核心矛盾，成本、安全性和循环寿命才是。这个认知差本身就是投资机会。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. CATL的Tener Sodium不是概念产品，而是商业交付的起点\n\nCATL在本周正式发布的Tener Sodium，是全球首个面向公用事业级的钠离子储能系统。这不是一款还在PPT阶段的概念产品。报告明确提到，该系统支持单机超过30MWh的容量，储能时长可在1至8小时之间灵活配置，循环寿命达到15,000次，且在极端温度下表现稳定。更重要的是，CATL已经确认技术和供应链均达到商业化水平，计划2026年9月开始在中国交付，2027年推向全球市场。\n\n这些参\n\n[... middle omitted ...]\n\n些关键问题的演变，并将最新的产业信号转化为可操作的认知框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球储能市场，这些变化值得关注\n\n全球储能加速分化\n\n固态电池、钠离子电池都在突破，中美欧各有动作\n\n---\n\n1️⃣ **美国：本土化与固态电池加速**\n- 三星SDI投2000万美元给美国电池初创Forge Nano，帮其建厂，目标2028年起每年采购250MWh电池，主攻国防和航空领域，减少对中国的依赖。Forge Nano还在寻求五角大楼2.75亿美元融资。\n- Lyten花6000万欧元买下Northvolt在德国海德的未完工工厂，改做电池厂+储能系统+数据中心，创造约1000个岗位。\n- QuantumScape与本田达成多年固态电池研发合作，推进QSE-5锂金属电池，能量密度更高、充电更快、更安全。\n- 福特将在密歇根生产LFP电池，用的是宁德时代授权技术，计划2027年用于下一代电动皮卡。\n- 特斯拉Model 3长续航版电池案例：前两年作为租赁车衰减20%，之后私人使用14个月仅再降1个百分点，说明电池早期衰减快、后期趋于稳定。\n- CSIQ为密歇根Coldwater太阳能项目提供75MW/381MWh储能系统，采用SolBank 3.0 LFP电池，2027年交付。\n\n2️⃣ **亚洲：钠\n\n[... middle omitted ...]\n\nls annually starting in 2028, while helping the company secure a more localized, China-free supply chain for U.S. defense and aerospace applications. Forge Nano is also seeking up to USD 275 m\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R006",
    "title": "GS：韩国军工和机器人，下半年最值得关注的两个板块",
    "digest": "[wechat_article.md]\n# GS：韩国军工和机器人，下半年最值得关注的两个板块\n\n当全球投资者的注意力仍被AI和半导体垄断时，一份来自GS的最新调研笔记揭示了一个被忽视的信号：韩国军工和机器人板块，正在酝酿一轮由订单、政策和估值共同驱动的修复行情。\n\n这份报告来自GS韩国工业团队，基于上周在纽约和波士顿的路演反馈写成。核心判断清晰而直接：韩国军工和机器人板块，有望在下半年迎来显著表现。\n\n这不是一个关于“长期趋势”的模糊论断，而是一个关于“催化剂正在密集兑现”的即时判断。报告给出了四个关键支撑：估值压缩后的安全边际、订单加速的可见性、欧洲市场敞口的扩大，以及全球政策层面对机器人产业的集体押注。\n\n对于正在寻找低相关性、有事件驱动逻辑的产业投资者而言，这份报告提供了一个值得认真对待的观察框架。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 军工板块的二季度跑输，恰恰为下半年积累了反弹空间\n\nGS指出，韩国军工股在二季度显著跑输大盘，原因有三：订单进展停滞、市场资金向存储芯片集中、以及全球军工同行股价走弱。\n\n但这份报告的核心洞察在于：这三个因素正在同时逆转。\n\n过去一个月，韩国军工行业出现了至少五个关键催化事件：瑞士因爱国者导弹交付延迟而转向韩国防空系统；西班牙即将敲定韩华航空航天K9自行榴弹炮订单；LIG D&A与莱茵金属签署防空导弹谅解备忘录；泰雷兹与韩华航空航天就Chunmoo制导导弹达成合作；秘鲁总统选举尘埃落定，此前因地缘政治不确定性而搁置的Rotem订单障碍正在解除。\n\n> **KC评论：** 这些事件的意义不在于单个订单的金额，而在于它们共同指向一个结构性变化——西欧国家正在将韩国视为传统军工供应链之外的“第二选择”。当交付速度成为关键变量时，韩国的产能和执行力就构成了核心议价权。报告中的估值图表显示，韩华航空航天和现代Ro\n\n[... middle omitted ...]\n\n群，继续讨论这些未解问题，获取完整报告的原始图表与详细拆解。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n韩国军工与机器人，下半年看点在哪\n\n韩国军工 & 机器人，下半年催化\n\n上周去纽约和波士顿跑了一圈，和机构聊最多的就是韩国军工和机器人。这两个板块在二季度明显跑输，但下半年催化正在密集出现。\n\n**1/ 军工：订单加速 + 估值压缩到位**\n\n二季度军工板块表现平淡，主要因为订单停滞 + 市场偏好记忆体。但过去一个月，关键变化来了：\n\n- 瑞士开始考虑韩国防空系统（替代延迟交付的爱国者）\n- 西班牙大概率敲定K9订单（韩华防务）\n- LIG D&A 与莱茵金属签署防空导弹MOU\n- 泰雷兹与韩华防务签署“天舞”制导导弹MOU\n- 秘鲁大选落地，之前Rotem的订单瓶颈在缓解\n\n西欧国家正加速依赖韩国企业的快速交付能力。而当前估值已回落到有吸引力的区间，下半年有望重拾动能。\n\n**2/ 机器人：政策加码 + 技术标准化**\n\n虽然人形机器人商业化还需要时间，但全球政策正在加速：\n\n- 韩国：科技部明年拨款建机器人数据训练中心，总统6月底召集机器人CEO圆桌\n- 美国：商务部长称机器人是“技术竞争的下一个战场”\n- 英伟达推出Halos开放安全系统，加速人形机器人安全认证\n\n韩国相关公司覆盖了从核心零部件到整机的\n\n[... middle omitted ...]\n\ngs.com  \nGS (Asia) L.L.C., Seoul Branch\n\n## Korea Defense\n\nKorean defense drew strong investor interest, driven by: 1) significant 2Q underperformance, 2) low correlation with AI within Indust\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R007",
    "title": "NOM：人形机器人量产拐点已至，但真正的主线不在机器人本身",
    "digest": "[wechat_article.md]\n# NOM：人形机器人量产拐点已至，但真正的主线不在机器人本身\n\n人形机器人行业正在经历一个被市场低估的转折。NOM在最新发布的研报中给出了一组值得深思的数字：特斯拉Optimus的产能规划从2027年的5万台上调至7万台，2028年再增加一条产线，远期总产能向150万台迈进。但真正重要的不是这个数字本身，而是支撑这一数字背后正在发生的两个结构性变化——数据采集方式的根本性转向，以及整机代工模式的加速成型。\n\n这份报告基于2026年6月中旬对宇树科技、Deep Robotics、申昊科技、梅卡曼德以及特斯拉供应链企业的实地调研，其核心判断是：人形机器人的量产逻辑正在被重写。过去行业争论的焦点是“谁能造出更好的硬件”，而NOM认为，未来12个月的决定性变量是“谁能以更低成本获取更高质量的训练数据”以及“谁能在代工链条中占据不可替代的位置”。\n\n这不是一个关于技术突破的故事，这是一个关于成本曲线和供应链权力转移的故事。\n\n![研报原图 1](assets/xhs_card_01.png)\n\n## 1. 2026年出货量预期大幅上修，消费端而非工业端成为主要驱动力\n\nNOM预计2026年中国市场的人形机器人出货量将达到4万至5万台，较此前预期显著上调。这个数字背后有两个关键驱动因素：一是政府主导的“具身智能基地”采购加速，二是预计2026年下半年由低价产品发布引发的消费需求拐点。\n\n从下游结构来看，NOM的估算显示，消费端和表演/娱乐端各占约30%，政府采购（数据采集）占20%，教育占15%，商业和工业应用仅占3%至5%。这意味着，当前人形机器人的主要出货场景仍然是“数据采集”和“体验消费”，而非真正意义上的工业替代。\n\n> **KC评论：** 工业场景占比仅3%至5%，这个数字值得反复咀嚼。市场对机器人的想象往往集中在工厂流水线，但现实是，工业部署在精度、节拍时\n\n[... middle omitted ...]\n\n把握市场动态。欢迎来知识星球微信群中继续讨论这些未解的问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n人形机器人量产，拐点到了\n\n量产拐点已至\n\n某外资投行最新调研显示，2026年人形机器人正在从“原型验证”跨入“规模量产”阶段，出货量预期显著上调。\n\n1️⃣ 特斯拉Optimus加速扩产\n- 弗里蒙特产线（原Model S/X产线）2027年产能目标从5万台上调至7万台\n- 2028年奥斯汀第二条产线再增7万台，远期合计产能指向150万台\n- 2026年9月目标爬坡至1,000台/周，全年出货约1.5-3.5万台\n\n2️⃣ 中国厂商出货量预期上调\n- 2026年中国市场预计出货4-5万台，由政府集采+低价消费级产品双驱动\n- 头部两家厂商出货约1-1.5万台（同比增2-3倍），二梯队约3,000台\n- 下游结构：消费30%、表演娱乐30%、政府数据采集20%、教育15%\n\n3️⃣ 数据采集范式切换，成本骤降\n- 行业正从“真人机器人采集数据”转向“非机器人采集”（遥操作/UMI/Ego数据）\n- 成本仅为真实机器人采集的20%，速度大幅提升\n- 预计混合训练数据中90%为非机器人数据，2027年真实采集需求将进一步压缩\n\n4️⃣ 代工趋势明确，成本加速下降\n- 硬件供应链重资产、回收期长，多数中小厂商选择外\n\n[... middle omitted ...]\n\nd 3) Robust 3D vision franchise supports diversified clientele and overseas reach. In this report, we draw on our advanced manufacturing tour and recent industry survey to assess the humanoid \n\n[... middle omitted ...]\n\nlable upon request and disclosure information is available at the NOM Disclosure web page: http://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R008",
    "title": "NOM：人民币中间价模型透露的政策信号，比点位更重要",
    "digest": "[wechat_article.md]\n# NOM：人民币中间价模型透露的政策信号，比点位更重要\n\n2026年6月29日，NOM亚洲外汇策略团队发布了一份看似技术性的报告——USD/CNY固定汇率模型更新。报告本身聚焦于模型投影值的微调，但在当前中美关系、国内经济政策博弈的关键节点，这份报告透露出的信息远比一个数字变化更有深意。\n\n**核心判断：人民币中间价的形成机制正在经历一个从“被动跟随”到“主动引导”的微妙切换。** 模型投影值与实际中间价的偏离幅度、逆周期因子的调整方向，正在成为观察中国央行汇率管理意图的前瞻指标。对于高净值投资者和产业决策者而言，理解这些技术细节背后的政策逻辑，比猜测具体点位更重要。\n\n报告给出的最新模型投影值为6.8077，较前次的6.8166下降了89个基点。计入逆周期因子后的投影值为6.8120，较前次下降46个基点。这两个数字本身并不惊人，但变化的方向和幅度，结合近期政策事件的时间表，构成了一个值得深度拆解的信号矩阵。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 模型投影值的下降方向，确认了短期贬值压力的边际缓解\n\nNOM模型的核心输出是USD/CNY中间价的投影值。6月29日的数据显示，投影值从6.8166降至6.8077，降幅为89个基点。这意味着，基于模型捕捉的隔夜市场变量——包括美元指数、欧元/美元、美元/日元等主要货币对的变动——模型认为央行应将中间价设定在更低的位置。\n\n这一变化本身并不意外。过去几周，美元指数因美国经济数据走弱而出现回调，人民币的贬值压力也随之有所缓解。但关键在于，模型投影值的下降幅度大于市场预期，暗示外部压力正在边际减弱。\n\n> **KC评论：** 对于普通投资者而言，不必纠结于模型的具体公式。关键信号是：当模型投影值持续下降，意味着央行面临的“被动贬值”压力在减轻，这为其主动管理汇率\n\n[... middle omitted ...]\n\n这些逻辑对资产配置的实际含义。\n\n期待在社群里与你继续交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n人民币中间价，盯住这个数字就够了\n\n中间价模型给出新信号\n\n最近看某外资投行的中间价预测模型，几个有意思的细节值得记一下：\n\n1/ 模型预测值：6.8077\n比上一次的6.8166低了89个点\n比前一次官方收盘价高了80个点\n（模型没考虑逆周期因子）\n\n2/ 加上逆周期因子后：6.8120\n比上一次中间价低了46个点\n说明逆周期因子继续在平滑波动\n\n3/ 模型误差来源\n主要来自隔夜市场贡献\n前四大权重因子决定了大部分变动\n（具体因子研报没展开，这里是推测：可能包括美元指数、美中利差、一篮子货币走势等）\n\n几个值得关注的时间节点：\n- 7月底：政治局经济工作会议\n- 10月1-7日：国庆黄金周\n- 11月：APEC在深圳\n- 12月中旬：中央经济工作会议\n- 年底：中美高层互动\n\n这些事件都会影响汇率预期\n中间价机制是一个动态调整的过程\n盯住模型预测值，比猜涨跌更有参考意义\n\n欢迎一起讨论你对汇率走势的看法\n\n#学习笔记\n\n[source_mineru.md]\n# USD/CNY fix model\n\n29 June 2026\n\nForeign Exchange - Asia ex-Japan\n\nProject\n\n[... middle omitted ...]\n\nctor)  \n![](images/774b58a73bb0a3e6f43a40578d58d26ebfce70d8e446dab34bd9acfb655355a9.jpg)  \nSource: NOM\n\nFig. 2: Recent model errors (without counter-cyclical factor adjustment)  \n![](images/64\n\n[... middle omitted ...]\n\nOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R009",
    "title": "Bernstein：斗山能源的2500亿美元核能订单，不只是“韩国制造”的故事",
    "digest": "[wechat_article.md]\n# Bernstein：斗山能源的2500亿美元核能订单，不只是“韩国制造”的故事\n\n全球核电建设正在进入新一轮加速周期，但真正值得关注的不是总装机量，而是供应链中少数几家具备重型设备制造能力的公司。Bernstein最新发布的亚太核电深度报告，将目光锁定在一家韩国公司——斗山能源（Doosan Enerbility）。报告的核心判断是：在未来十年，斗山能源面临约2500亿美元的可参与核电项目总市场规模（TAM），其中约440亿美元（67万亿韩元）是可直接转化为设备合同的订单机会。这并非一个模糊的行业乐观叙事，而是一个基于项目进展节点、可追踪、可验证的订单管道。\n\n这份报告的独特价值在于，它没有停留在“核电要复兴”的宏大判断上，而是逐国别、逐项目地拆解了哪些项目已经进入设备采购前阶段，哪些还在可行性研究，以及这些时间节点对斗山这样的设备商意味着什么。对于关注产业投资、能源供应链和制造业升级的读者，这是一份少见的、从“订单可见性”出发的深度分析。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 2500亿美元的可参与市场，核心不是规模而是“可执行性”\n\nBernstein的分析框架有一个关键前提：他们只统计那些已经推进到设备采购前阶段的项目。这意味着这些项目已经完成了或正在完成监管许可、前端工程设计（FEED）以及融资结构确定。在这个阶段之前，项目仍存在高度的不确定性，无法作为订单预测的依据。\n\n基于这一筛选标准，报告识别出约35吉瓦（GW）的核电项目，总项目成本约2500亿美元。这并非所有在建或规划中的核电项目，而是斗山能源“真正有机会拿到设备合同”的那一部分。从区域分布看，欧洲项目是近期订单的主要来源，美国项目则要到2020年代末才会随着融资和供应链支持改善而逐步落地。\n\n这一判断对投资者的含义是明确的：斗山能源\n\n[... middle omitted ...]\n\n以及后续的项目跟踪更新感兴趣，欢迎加入我们的微信群继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n亚太核电 2500 亿美金的订单机会\n\n核电新订单来了\n\n未来十年全球核电项目将密集进入设备采购阶段\n\n1/ 某外资投行最新研报指出：全球约有 35GW 核电项目即将进入设备采购，对应约 2500 亿美金的总市场空间。其中，斗山能源能拿到的设备订单约 440 亿美金（67 万亿韩元）。\n\n2/ 订单节奏很清晰：近看欧洲，波兰今年就要签设备合同；远看美国，随着融资和供应链改善，2030 年前后会有更多项目落地。斗山在 AP1000 和大型反应堆供应链上积累深厚，是少数能规模化交付的供应商。\n\n3/ 除了核电，燃气轮机业务也在扩张。研报预计斗山燃气订单将从 2025 年的 4.7 万亿韩元增长到 2030 年的 7 万亿韩元。随着装机量增加，燃气服务收入到 2030 年可达 0.4 万亿，2035 年接近 1 万亿，这是高毛利的经常性收入。\n\n4/ 综合来看，斗山年订单有望从 2025 年的 15 万亿韩元增长到 2030 年的 21 万亿以上（已做风险调整），超过公司自己的 16.5 万亿目标。利润率也会明显改善，2028 年运营利润率可进入低双位数。\n\n5/ 斗山的竞争优势在于：40 多年的核电设备制造经验，\n\n[... middle omitted ...]\n\ntify \\~35GW or \\~USD250bn of nuclear projects nearing procurement for Doosan Enerbility. This pipeline is primarily driven by large-scale reactors (APR/AP1000) with a smaller contribution from\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R010",
    "title": "NOM：人形机器人的“脊髓”比“大脑”更关键",
    "digest": "[wechat_article.md]\n# NOM：人形机器人的“脊髓”比“大脑”更关键\n\n当市场还在争论大模型能否赋予机器人通用智能时，一份来自NOM的最新研报提出了一个反直觉的判断：物理人工智能落地的真正瓶颈，不是语言模型的推理规模，而是能否构建一个低延迟的“反射层”——相当于人类的脊髓反应。\n\n这份报告以NXP提出的NeuralAxis架构为理论蓝图，以宇树科技新发布的WVLA2.0模型为产品验证，勾勒出一条与当前主流“端到端大模型”路径截然不同的商业化路线。其核心主张是：在物理世界里，40毫秒的反射响应比300毫秒的深度思考更决定生死。这一判断不仅挑战了人形机器人行业的技术共识，更对工业自动化、服务机器人乃至自动驾驶的落地节奏提供了新的观察框架。\n\nNOM分析师Frank Fan和Donnie Teng在实地调研宇树科技后，将这份研报定位为“从架构蓝图到可交付产品的完整推演”。它没有停留在概念层面，而是给出了具体的技术指标、商业化场景排序，以及当前仍未解决的量化验证问题。\n\n![研报原图 1](assets/xhs_card_01.png)\n\n## 1. 物理AI的硬约束不是算力，而是“反射速度”\n\nMoravec悖论指出，对人类来说困难的高阶推理对机器而言相对容易，而人类无意识完成的感知与运动控制对机器却异常艰难。NOM报告借NXP的NeuralAxis框架，将这一悖论具象化为一个工程问题：物理AI系统必须在毫秒级完成对环境的反应，而不是等待云端大模型返回推理结果。\n\nNeuralAxis将系统架构拆解为三个解耦但协同的层级：推理层（大脑皮层，约300毫秒响应）、协调层（小脑，负责运动控制与平衡）、反射层（脊髓，最低可达40毫秒）。这一架构最激进的设计在于，反射处理器被分布部署到关节、手部和足部，而非集中在一个中央大脑。这意味着，当机器人抓取一个未知重量的物体时，手指关节的本地处理器可以\n\n[... middle omitted ...]\n\nmics。欢迎来星球微信群里继续讨论，一起拆解这些未解问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n人形机器人落地，关键不在大模型\n\n封面：物理AI的“脊髓反射”\n\n封面副标题：40ms反应速度，比人类眨眼快10倍\n\n---\n\n最近研究了一份某外资投行的研报，讲的是物理AI（Physical AI）的商业化路径，核心观点很有意思。\n\n**1. 物理AI的瓶颈不是“思考”，而是“反射”**\n\n某芯片巨头提出了一个叫NeuralAxis的架构。核心逻辑：人形机器人的关键限制不是语言模型的推理能力，而是需要工程化一个低延迟的“反射层”——就像人类的无意识反应。\n\n这个架构分三层：\n- **推理层（大脑皮层）**：约300ms响应\n- **协调层（小脑）**：负责运动控制和平衡\n- **反射层（脊髓）**：低至40ms，直接推到关节、手脚的边缘\n\n这意味着：机器人的“大脑”不再集中，而是分布在每个关节。抓握力控制、脚踝平衡这些动作，可以在40ms内自主完成，不依赖中央推理。\n\n**2. 从蓝图到产品：宇树WVLA2.0**\n\n宇树科技（未上市）的WVLA2.0模型，是这套架构的首次商业化落地。\n\n它融合了两种技术路线：\n- **WMA模型**：预测能力\n- **VLA模型**：端到端动作生成\n\n感知层面，融合了4路\n\n[... middle omitted ...]\n\nn how Unitree turns that blueprint into a shipping product and a commercial roadmap through model fusion and hardware-software co-design.\n\n## NeuralAxis by NXP: The reflex-first blueprint for \n\n[... middle omitted ...]\n\nlable upon request and disclosure information is available at the NOM Disclosure web page: http://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R011",
    "title": "国际清算银行：财政风险冲击正在制造“滞胀陷阱”，而央行宽松只会让情况更糟",
    "digest": "[wechat_article.md]\n# 国际清算银行：财政风险冲击正在制造“滞胀陷阱”，而央行宽松只会让情况更糟\n\n当市场开始重新评估政府债务的安全性，后果并不仅仅是主权债券收益率上行。国际清算银行（BIS）最新工作论文揭示了一个更令人不安的传导链条：财政风险冲击会同时推高通胀和压低产出，形成典型的“滞胀”格局。更关键的是，如果央行选择用宽松货币政策来对冲，结果不是缓解，而是让通胀更高、衰退更深。\n\n这份由BIS经济学家Denis Gorea、Ding Xuan Ng和Fabrizio Zampolli完成的第1364号工作论文，构建了一套全新的识别框架，从债券市场数据中分离出纯粹的“财政风险冲击”，并追踪其对12个经济体宏观金融变量的影响。结论清晰且具有政策警示意义：财政纪律的丧失，其代价远不止于更高的融资成本。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 这不是普通的利率波动，而是市场在重新定义“安全资产”的边界\n\n传统上，主权债券被视为无风险资产的基准。但当财政可持续性受到质疑时，这一基准本身开始动摇。BIS论文的核心识别策略恰恰抓住了这一点：当财政风险上升时，投资者会从主权债券转向同等期限的最高等级公司债券。这种“组合再平衡”行为，使得主权债券收益率上升的同时，安全公司债券收益率下降——两者走势背离，正是财政风险冲击的独特指纹。\n\n这一识别的精妙之处在于，它排除了货币政策、通胀预期或全球风险偏好等共同因素。如果主权债券收益率上升是因为央行加息，那么公司债券收益率也会同步上升；如果是因为通胀预期上升，两者同样会一起走高。只有在财政风险这个特定维度上，才会出现主权债券被“降级”、安全公司债券被“升级”的分化格局。\n\n> **KC评论：** 这意味着，投资者不再把本国国债当作终极安全资产。当市场开始用“公司债思维”来定价主权信用时，政府面临的融资约束将\n\n[... middle omitted ...]\n\n动态。社群内还可获取本文完整研报的原始图表与BIS论文全文。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n财政风险来袭，市场如何反应？\n\n财政风险冲击\n\n12国数据揭示的真实影响\n\n最近读到BIS一篇工作论文，用很巧妙的方法识别了财政风险冲击，分享核心发现。\n\n1️⃣ 什么是财政风险冲击？\n- 投资者突然觉得政府债务不安全了\n- 开始抛售国债，转向高质量企业债\n- 导致国债收益率上升，企业债收益率下降\n\n2️⃣ 冲击发生后会发生什么？\n- 通胀和通胀预期立刻上升\n- 工业生产短期提振后持续下滑\n- 收益率曲线变陡，汇率贬值，股市下跌\n\n3️⃣ 什么情况下影响更大？\n- 货币政策宽松时：通胀更高，产出下滑更明显\n- 主权风险已较高时：通胀更持久，股市跌幅更大\n\n4️⃣ 有意思的发现\n- 财政恶化推通胀的效果，比财政改善压通胀的效果更强\n- 长期国债收益率和股市对坏消息更敏感\n- 这种不对称性值得关注\n\n论文用的识别方法很聪明：通过国债和优质企业债收益率的变化方向来分离财政风险冲击，比单纯看国债收益率更干净。\n\n#学习笔记\n\n[source_mineru.md]\n![](images/393bccd27efdbe85b292d818e7db8520c710f7265d3f5932df101508fe89d102.jp\n\n[... middle omitted ...]\n\nd by the Bank. The papers are on subjects of topical interest and are technical in character. The views expressed in this publication are those of the authors and do not necessarily reflect th\n\n[... middle omitted ...]\n\n increase during passive monetary policy episodes ( $D_{i,t}^{MP} = 1$ ) relative to active episodes, conditional on a positive underlying fiscal risk shock. Shaded bands: 67% IV-corrected clustered confidence intervals."
  },
  {
    "id": "R012",
    "title": "国际清算银行：高债务正在悄悄削弱加息的通胀抑制力",
    "digest": "[wechat_article.md]\n# 国际清算银行：高债务正在悄悄削弱加息的通胀抑制力\n\n市场主流叙事一直把通胀能否回落押注在央行加息力度上。但一份来自国际清算银行的最新工作论文给出了一个令人不安的答案：加息对通胀的抑制作用，可能被一个被长期忽略的结构性变量悄悄削弱——公共债务的规模和期限结构。\n\n这份编号1365的工作论文，基于2001至2020年欧元区高频货币政策冲击数据，使用面板局部投影方法，得出了一个对全球投资者和政策制定者都极具冲击力的核心判断：高债务经济体面对加息时，价格和通胀预期的反应显著弱于低债务经济体，而产出收缩幅度却至少持平。换句话说，同样的加息幅度，在高债务国家，通胀更难压下去，但经济代价并不更小。\n\n这不是一个学术象牙塔里的清谈。对于正在评估欧洲资产定价、全球利率路径和主权信用风险的决策者而言，这份报告提供了一个必须纳入分析框架的变量——债务期限结构如何改变了货币政策的传导效率。\n\n---\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 加息对通胀的“刹车”效果，在高债务国家明显失灵\n\n报告的核心实证发现可以用一句话概括：当公共债务占GDP比例从60%上升到120%时，同样幅度的加息，价格水平的下降幅度显著缩小，通胀预期的锚定能力也明显减弱。\n\n这一结果在统计上是显著的。报告作者使用了一个巧妙的识别策略：在保持债务期限结构不变的前提下，仅改变债务总量水平，来分离“债务规模”和“债务期限”两个变量的独立影响。结果显示，高债务经济体面对加息时，价格反应更弱，而产出收缩幅度至少与低债务经济体相当。\n\n这意味着什么？传统教科书模型假设货币政策通过利率渠道影响总需求，进而传导至价格。但高债务环境下，这个链条被扭曲了。加息不仅抑制私人部门需求，还会通过影响政府资产负债表、债券持有人收入和财政风险溢价，产生一系列反向作用力。\n\n> **KC评论：\n\n[... middle omitted ...]\n\n高价值的机构研究，欢迎加入社群，获取完整研报解读与原始图表。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n国债期限结构，才是央行加息的真实力度\n\n封面：加息力度取决于国债结构\n\n副标题：BIS新研究：债务期限比总量更关键\n\n---\n\n刚读完BIS一篇工作论文，思路非常清晰。研究欧元区2001-2020年数据，发现公共债务的水平和期限结构，会显著改变货币政策的传导效果。\n\n**核心发现：**\n1️⃣ 高债务≠弱效果。当债务/GDP从60%升到120%，加息后价格和通胀预期反应更弱，但产出下降幅度反而更大。这像踩到耙子——越用力，反弹越疼。\n\n2️⃣ 期限结构才是关键变量。中间期限（9个月-8年）的债务，会弱化货币政策效果。但超短期（<9个月）和超长期（>8年）债务，反而会放大效果。\n\n**为什么？**\n三个机制在打架：\n- 短期债务：利率传导快，利息收入效应强，可能抵消紧缩效果\n- 长期债务：价格弹性大，估值损失效应强，强化紧缩\n- 中间期限：两种效应相互抵消，政策效果最弱\n\n**溢出效应也重要**\n欧元区加息会影响非欧元区欧洲国家。有意思的是，接收国的债务期限结构同样重要——4-8年期限债务占比越高，溢出效果越强。\n\n一个推论：如果财政政策不配合（比如赤字不缩减），债务对货币政策传导的影响会更显著。研究中发现，加\n\n[... middle omitted ...]\n\nmists, and are published by the Bank. The papers are on subjects of topical interest and are technical in character. The views expressed in this publication are those of the authors and do not\n\n[... middle omitted ...]\n\ne end of 2019\n\n![](images/39df40569e6a974a6dd5194605040035751087d23dacb26c300dd0485026bf21.jpg)  \nResidual Maturity (years)  \nFigure A.4: Detailed maturity structure of CEE countries at the end of 2019, as percent of GDP"
  },
  {
    "id": "R013",
    "title": "波士顿咨询：CEO的AI红利，不在效率，在判断",
    "digest": "[wechat_article.md]\n# 波士顿咨询：CEO的AI红利，不在效率，在判断\n\n当一家公司谈论AI转型时，最值得观察的信号不是它的技术路线图，而是CEO本人如何使用AI。\n\n波士顿咨询（BCG）在2026年6月发布的最新报告中，提出了一个被多数企业忽视的判断：AI对企业最高决策层的最大价值，不是节省时间，而是放大CEO及其核心团队的判断力。报告指出，尽管72%的CEO现在直接负责公司的AI决策，但只有15%的人从中获得了有意义的回报。这15%的先行者与落后者的关键区别，不在于他们是否部署了更先进的系统，而在于他们每周至少花8小时亲自使用AI、理解其能力边界，并将其嵌入自己的决策流程。\n\n这个发现颠覆了常见的AI转型叙事。多数企业将AI视为中层和基层的效率工具，用来优化流程、提升生产力。但BCG认为，真正未被开采的金矿在组织顶端——那里做出的决策影响公司未来数年走向，而判断质量的微小提升，都能带来几乎无限的商业价值。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 先行者CEO已经用AI扮演四种角色，但多数企业仍在观望\n\nBCG通过研究15位高知名度CEO的公开案例，提炼出先行者使用AI的六种常见行为：快速掌握陌生领域知识、预判关键对话、压缩复杂信息、压力测试自身假设、更清晰地表达观点、以及评估自己的时间分配是否匹配战略优先级。\n\n这些行为可以被归纳为四种角色：AI充当“随需导师”，帮助CEO在重大会议前快速建立对新领域的语感；充当“魔鬼代言人”，在决策尚未固化前挑战假设、揭示风险；充当“战略编辑”，将粗糙的想法转化为清晰的沟通；以及充当“反思工具”，通过分析日程和邮件来检验CEO的时间是否真的花在了最重要的事情上。\n\n> **KC评论：** 这些案例听起来像“高级秘书”或“个人助理”的替代品，但重点在于“压力测试”和“反思工具”。当CEO需要下属或\n\n[... middle omitted ...]\n\n？以及，当AI成为CEO的“标配”后，竞争壁垒会转移到哪里？\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nCEO 用 AI，最该警惕什么？\n\nCEO 的 AI 使用手册\n\n别只盯着效率，更要守住判断力\n\n某外资投行最近发了一篇有意思的研报，讲的是 CEO 该怎么用 AI。它没说 AI 多牛，反而提醒：**用不好，反而会削弱领导力。**\n\n以下是几个核心观察：\n\n1/ **CEO 亲自用 AI，比发文件更管用**\n当老板自己天天用 AI，员工才会真的去试。数据显示，72% 的 CEO 已直接负责 AI 决策，但只有 15% 真正用出价值。那些“先行者”每周至少花 8 小时自己上手练。\n\n2/ **AI 的四种“误导”方式**\n- 把“流畅回答”当成“专业判断”\n- 把“快速出答案”当成“更好的决策”\n- 让团队变得同质化（研究显示，AI 会让团队思维多样性降低 41%）\n- 信息过载反而让大脑“烧焦”（14% 的 AI 用户报告过“AI 脑疲劳”）\n\n3/ **CEO 该问自己的 5 个问题**\n- 我是想用 AI 做更好的决策，还是只是更快的决策？\n- 我能判断 AI 什么时候在犯错吗？\n- 谁在挑战 AI 给出的答案？\n- 怎么衡量 AI 是否真的让我变强了？\n\n研报最后点题：AI 不是万能药，但带着纪律、好奇\n\n[... middle omitted ...]\n\nnior team may be reluctant to raise, and manage their schedules more strategically.\n\nWhile early AI use cases like these confer real benefits for an organization by expanding a CEO's understan\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R014",
    "title": "波士顿咨询：金融科技重回增长，但赢家的门槛已经变了",
    "digest": "[wechat_article.md]\n# 波士顿咨询：金融科技重回增长，但赢家的门槛已经变了\n\n金融科技行业在经历2023至2024年的估值修正与资本寒冬后，2025年交出了一份出人意料的成绩单。全球金融科技总收入突破5000亿美元，同比增长22%，增速是传统金融机构的四倍以上。但这份波士顿咨询与FT Partners联合发布的《2026年全球金融科技报告》传递的核心信号，并非简单的“行业复苏”。真正值得关注的判断是：金融科技已经从一个靠烧钱换增长的赛道，进入了一个利润与规模必须同时兑现的新阶段。行业没有回到2021年的狂热，而是进入了一个更成熟、但竞争门槛更高的“选择性繁荣”时期。\n\n这份报告之所以重要，是因为它系统性地回答了三个投资者最关心的问题：增长是否可持续？哪些细分领域真正跑出来了？以及，AI和数字资产到底是泡沫还是下一波基础设施？在行业情绪从悲观转向谨慎乐观的当下，波士顿咨询的判断为决策者提供了一个难得的全局视角。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 这轮增长的本质是盈利能力的修复，而非估值的泡沫重来\n\n报告中最具说服力的数据，不是总收入的增长，而是运营质量的改善。全球最大的85家上市金融科技公司，2025年平均EBITDA利润率提升了4个百分点，达到20%。更关键的是，74%的公司已经实现盈利，而2024年这一比例是68%。同时，符合“40法则”（收入增速加利润率超过40%）的公司占比也在提高。\n\n这意味着什么？2025年的增长不是靠烧钱买来的，而是靠真实的运营效率提升。资本市场的态度也印证了这一点：虽然股权融资总额回升至580亿美元，同比增长53%，但资金高度集中在后期轮次。2023至2025年间，E轮及以后的融资额增长了超过210%，而种子轮和天使轮则收缩了约10%。投资者不再为故事买单，他们只愿意为已经证明有规模化路径和清晰经济\n\n[... middle omitted ...]\n\n表合集，既方便喂给AI模型，也方便人类读者快速把握市场动态。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球金融科技，从复苏到重新爆发\n\n金融科技复苏，但不一样了\n\n全球金融科技收入2025年突破5000亿美元，同比增长22%，增速是传统金融机构的4倍以上。但这不是简单的回归，而是一次结构性的成熟跃迁。\n\n1/ 增长分化明显\n- 交易与投资板块增长38%，存款增长30%，领跑全场\n- 支付依然是最大收入贡献者\n- 亚太增速最快（25%），欧洲24%，北美21%\n\n2/ 盈利质量提升\n- 前85家上市金融科技公司平均EBITDA利润率提升4个百分点至20%\n- 74%已实现盈利（2024年为68%）\n- 融资更挑剔：2025年股权融资580亿美元，同比增长53%，但主要流向后期项目\n\n3/ 区域亮点\n- 巴西Pix支付上线一年覆盖67%成年人\n- 印度UPI月交易量超200亿笔\n- 肯尼亚M-PESA服务约80%人口\n- 菲律宾GCash从2015年5%覆盖面跃升至75%\n\n4/ 资本市场依旧审慎\n- 2025年金融科技IPO42起，同比增长50%\n- M&A交易额从2023年1050亿升至2025年2510亿美元\n- 但过去5年最大30只金融科技IPO年回报跑输金融板块约24个百分点\n\n5/ 竞争逻辑已变\n- \n\n[... middle omitted ...]\n\n trading and investments and deposits leading the pack with about 38% and 30% YoY growth, respectively\n\n400bps\n\nAverage EBITDA margin improvement for the largest public fintechs from 2024 to 2\n\n[... middle omitted ...]\n\nbillion valuation.\n\n![](images/5208938f8aac64690ee682cdf49cfa96b3939091639a16bfe9980e8ccf39088f.jpg)\n\nBCG +\n\nFINANCIAL TECHNOLOGY PARTNERS\n\n![](images/b3e517083cc6425278ea17bb2538e0b674db9c9074c0172d5cbc3260759a241a.jpg)"
  },
  {
    "id": "R015",
    "title": "波士顿咨询：美国P&C保险的“好日子”结束了，但赢家还没定",
    "digest": "[wechat_article.md]\n# 波士顿咨询：美国P&C保险的“好日子”结束了，但赢家还没定\n\n美国财产与意外险（P&C）市场正在经历一个关键的转折点。波士顿咨询（BCG）在最新发布的《2026保险价值创造者报告》中给出一个核心判断：支撑过去几年行业高回报的“硬市场”红利正在消退，费率走软与结构性风险上升正在重塑竞争格局。这不是一次周期性的小波动，而是一次市场底层逻辑的切换。\n\n报告显示，2021至2025年间，美国P&C保险公司实现了约18%的年化总股东回报率（TSR），跑赢全球保险业平均水平的15%，也跑赢了大多数其他行业。但进入2025年，这一势头明显放缓。更值得关注的是，行业内头部与尾部公司的差距正在拉大，这种分化在历史上往往预示着一次市场洗牌的开始。\n\n对于产业决策者和投资者而言，当下最需要回答的问题不是“市场会怎么走”，而是“在费率走软、风险复杂化的新环境下，什么样的公司能持续创造价值”。BCG的报告给出了一个清晰的答案框架，但其中的细节和隐含判断，值得逐层拆解。\n\n> **KC评论：** 波士顿咨询这份报告的价值不在于告诉你市场在变——这已经是共识。它的真正贡献在于，用五年期的TSR数据和承保利润率拆解，量化了“赢家”和“输家”之间的差距究竟来自哪里。读完你会发现，承保能力才是唯一的护城河，投资收入只是止痛药。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 承保利润是分水岭，投资收益只是止痛药\n\nBCG报告中最具冲击力的图表之一，是不同分位保险公司对有形股本回报率（RoTE）的贡献拆解。在2021至2025年间，前四分之一的P&C公司，其承保业务对RoTE的贡献约为11个百分点；而尾部公司的承保贡献为负值。\n\n这意味着什么？在硬市场周期中，行业整体看起来都在赚钱，但利润来源完全不同。头部公司靠的是承保纪律——更低的综合成本率、更精准的风\n\n[... middle omitted ...]\n\n解读版本。这些内容将帮助你在当前市场环境下做出更精准的判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美国财险市场正在洗牌，谁在裸泳？\n\n市场分化加剧\n\n某外资投行最新研报显示，美国财险市场正从“硬市场”转向“软市场”，保费增速放缓，但赔付成本持续攀升。头部和尾部公司的差距正在拉大，盈利增长仍是长期股东回报的核心驱动力。\n\n1️⃣ 定价红利消退\n过去靠提价改善承保结果的公司，现在必须转向数据、细分和费用管控。2025年个人车险综合成本率已从2022年的112%改善至92%，但竞争加剧，费率上涨空间有限。\n\n2️⃣ 承保能力是分水岭\n头部公司有形股本回报率（RoTE）中，承保贡献约11个百分点，而尾部公司承保为负。投资收入一旦正常化，承保质量将决定生死。\n\n3️⃣ 结构性风险在加深\n社会通胀（如“天价判决”）、强对流风暴损失、以及AI带来的新风险，正在重塑风险组合。2024年“天价判决”达135起，创历史新高。第三方诉讼融资市场规模已达150-180亿美元。\n\n4️⃣ AI从实验走向优势\n领先公司已规模化部署AI于承保、理赔和定价，获得运营效率和更精细的风险洞察。但AI本身也带来新风险敞口，目前缺乏历史数据支撑精算定价。\n\n5️⃣ 个人险分化加剧\n个人车险市场恢复盈利后，竞争转向进攻。但赔付频率回升、严重度上升\n\n[... middle omitted ...]\n\ne cost of losses, driven by such factors as social inflation, severe convective storms (SCSs), and elevated claims severity, remains high. The result is a more complex operating\n\nenvironment i\n\n[... middle omitted ...]\n\nG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com."
  },
  {
    "id": "R016",
    "title": "波士顿咨询：95%的公司正在错过AI真正的价值拐点",
    "digest": "[wechat_article.md]\n# 波士顿咨询：95%的公司正在错过AI真正的价值拐点\n\n一份覆盖全球1,250家企业的实证研究给出了一个令人不安的判断：只有5%的公司真正从AI中获得了可量化的商业价值。这5%的企业——波士顿咨询称之为“未来型公司”——不仅跑赢了同行，而且正在加速拉开差距。它们的收入增速是落后者的1.7倍，三年股东总回报是后者的3.6倍，投入资本回报率高出2.7倍。\n\n这份报告的核心洞察并不在于“AI有用”，而在于“AI的价值分配已经出现结构性断裂”。60%的企业虽然持续投入，但几乎没有获得任何实质性回报。真正的问题不是技术不够好，而是大多数公司用错了策略框架——它们在做自动化，而领先者在做再造。\n\n这个差距不是暂时的。它正在自我强化。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 5%的公司正在构筑一条AI价值护城河，而60%的公司正在被反向锁定\n\n波士顿咨询的研究将企业按AI成熟度分为四类：未来型（5%）、规模化中（35%）、新兴型（46%）和停滞型（14%）。后三类合计95%的企业，构成了“追赶者”阵营。\n\n最关键的数字不是5%这个比例，而是这些未来型公司正在创造一种“复合效应”。它们将AI产生的利润重新投入技术基础设施和人才，形成正向循环。2025年，这些公司计划将IT预算中高达64%的份额投入AI，而追赶者这一比例不足其一半。结果是，未来型公司预期在AI应用领域实现双倍于追赶者的收入增长，成本降幅也高出1.4倍。\n\n对于那60%几乎没有回报的公司来说，问题出在顶层。波士顿咨询指出，这些公司的管理层往往“口头上重视AI，但没有明确的量化目标，也没有定期追踪进度的机制”。他们将AI决策下放到中层或基层，导致资源分散在数十个孤立的试点项目中，无法形成规模价值。\n\n> **KC评论：** 这份报告揭示了一个被低估的风险——AI投资正\n\n[... middle omitted ...]\n\net dynamics。完整版报告解读和原始图表已同步上传。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI的“赢家通吃”已经开始\n\n赢家通吃，差距拉大\n\n只有5%的公司真正从AI赚到钱，60%的公司还没摸到门。\n\nBCG最新研究：AI价值鸿沟正在扩大\n\n1️⃣ 只有5%的公司是“未来型”\n收入增速是其他公司的1.7倍\n股东回报是3.6倍\n投资回报率是2.7倍\n这5%的公司已经形成“正向循环”：先发优势→赚到钱→再投资→差距更大\n\n2️⃣ 70%的AI价值集中在核心业务\n销售、制造、供应链、定价是主战场\n研发创新占15%\nIT部门贡献从7%跳涨到13%\n最值钱的是客户相关功能和IT\n\n3️⃣ 智能体AI正在加速\n2024年几乎没人提，2025年已占AI价值的17%\n预计2028年达到29%\n智能体不是独立项目，要嵌入整个工作流\n\n4️⃣ 为什么60%的公司掉队了？\n高管只喊口号不行动\n把AI丢给中层，没人敢拍板\n到处试点，资源分散\n把AI当提效工具，没做战略重构\n\n5️⃣ 未来型公司的5个共同点\n- 有多年AI战略蓝图\n- 重塑核心流程，不是小修小补\n- AI优先的运营模式\n- 大规模培训员工（超50%）\n- 灵活的技术栈和数据基础\n\n差距已经拉开，但路径清晰。关键是：你准备花几年赶上？\n\n#学习笔记\n\n[so\n\n[... middle omitted ...]\n\nctor and Region\n\n11 What Value Generators Do Differently\n• Pursue a Multiyear Strategic AI Ambition\n• Reshape and Invent with Impact\n• Adopt an AI-First Operating Model\n• Secure and Enable the\n\n[... middle omitted ...]\n\nalerts on this topic or others, please visit bcg.com. Follow Boston Consulting Group on LinkedIn, Facebook, and X (formerly Twitter).\n\n![](images/1d7bfc57d3a1e9ad701ad9cbe653c75cfee078efb6aa3451e45868acc2c36836.jpg)\n\nBCG"
  },
  {
    "id": "R017",
    "title": "波士顿咨询：游戏行业的下一个增长引擎不是硬件，是平台碰撞",
    "digest": "[wechat_article.md]\n# 波士顿咨询：游戏行业的下一个增长引擎不是硬件，是平台碰撞\n\n游戏行业正在走出“三年寒冬”。这不是一个模糊的乐观预期，而是波士顿咨询（BCG）在最新发布的《Video Gaming Report 2026》中给出的明确判断。这份基于近3000名全球玩家调研和行业深度分析的报告，核心结论只有一个：游戏行业的下一轮增长，不会来自新一代主机或更快的芯片，而是来自四大趋势的“碰撞”——生成式AI、用户生成内容（UGC）、云游戏和开放应用商店。当这些趋势同时发生，传统的“主机战争”将让位于“生态战争”，而赢家将是那些重新定义分发、发现和变现逻辑的公司。\n\n报告预测，全球游戏收入将从2025年的约2600亿美元增长至2030年的约3300亿美元，复合年增长率约为5%。这个数字远低于2010年代行业规模翻倍的速度，但BCG认为，这是更健康、更可持续的增长模式。更重要的是，增长的结构正在发生根本性变化：云游戏收入将从2025年的约15亿美元飙升至2030年的约300亿美元，UGC创作者经济仅Fortnite和Roblox两个平台在2025年的分成就将超过15亿美元，而应用商店的开放将重塑移动游戏50%全球收入的分发逻辑。\n\n以下是这份报告最值得关注的五个核心判断。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 云游戏终于不再是一个概念，2025年是进入主流的分水岭\n\n过去十年，云游戏一直被贴上“未来技术”的标签，但BCG的调研数据表明，这个未来已经到来。全球范围内，60%的玩家尝试过云游戏，其中80%给出了正面体验反馈。这个数字远超行业预期。\n\n更关键的是，云游戏正在改变“平台”的定义。传统的主机战争——PlayStation vs Xbox vs Nintendo——本质上是对客厅硬件的争夺。但云游戏让硬件变得无关紧要。玩家可以在手\n\n[... middle omitted ...]\n\n0-40页的中文摘要与数据图表合集。这些内容既方便喂给AI进行二次分析，也方便人工快速把握市场动态。如果你希望获得BCG这份报告的完整解读、原始图表和更多未在本文展开的分析，欢迎加入社群继续讨论。\n\n---\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n游戏行业正在悄悄变天\n\n四大趋势重塑游戏业\n\n某外资投行最新研报指出，游戏行业终于走出三年“寒冬”，正进入新一轮增长周期。核心判断：平台边界正在消失，未来五年会发生剧烈变化。\n\n📌 四大趋势正在同时发生\n\n1️⃣ GenAI 加速游戏开发\n约50%的工作室已在用AI，Q3 2025近20%新游戏披露使用了AI。效率提升、NPC变聪明、甚至AI帮你生成整个游戏。但也要小心“游戏垃圾”泛滥。\n\n2️⃣ UGC 创作者经济爆发\n仅Fortnite和Roblox，2025年给创作者的支付超15亿美元。40%的玩家表示比一年前消费了更多UGC内容。5岁小孩的第一款游戏，往往是Minecraft或Roblox。\n\n3️⃣ 云游戏即将起飞\n60%的玩家尝试过云游戏，其中80%体验良好。未来硬件不再重要，游戏跟着你走。\n\n4️⃣ 应用商店开放\n这对占全球游戏收入50%的手游是地震级变化。开发者费用降低，自主分发能力大增。\n\n📌 一些有意思的数据\n\n- 55%的玩家过去半年增加了游戏时长\n- 40%婴儿潮世代每周玩5小时以上游戏\n- 75%的玩家表示价格会影响购买决策\n- 玩家对AI生成内容接受度很高，只有10%对AI作画有负\n\n[... middle omitted ...]\n\nGrowth Through Disruption\n24 About the Global Gaming Survey\n24 About the Authors\n\n![](images/12e49fe0b84197cccc04469010a548bda429f8c83ec7d9eaef57bc6e6b7b21fa.jpg)\n\n## Introduction\n\nAs 2025 com\n\n[... middle omitted ...]\n\nvels of the client organization, fueled by the goal of helping our clients thrive and enabling them to make the world a better place.\n\n![](images/5222010d510a5e95ab69501cb00afaa75c4150e60b107da1dc41914c29120e1f.jpg)\n\nBCG"
  },
  {
    "id": "R018",
    "title": "麦肯锡：美国250年竞争力未断，但真正考验的是“下一章”能否续写",
    "digest": "[wechat_article.md]\n# 麦肯锡：美国250年竞争力未断，但真正考验的是“下一章”能否续写\n\n美国建国250年之际，麦肯锡全球研究院发布了一份罕见的全景式报告，回顾美国经济竞争力的历史弧线，并前瞻下一阶段的挑战。这份报告的核心判断出人意料地清醒：美国目前仍是全球最具竞争力的经济体，但多个历史优势正在变成负债。真正的问题不是庆祝过去，而是能否再次找到资源、雄心、制度与政策的新对齐，以续写下一个章节。\n\n这份报告的价值不在于罗列美国有多强，而在于它提供了一个少见的、长周期的分析框架，把AI、地缘政治、人口结构、财政健康、教育衰退、基础设施老化等看似分散的变量，统一到一个“竞争力演化”的叙事中。对于关注全球资产配置、产业趋势与中美竞争格局的读者，这是一份值得细读的底层框架。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 美国竞争力的“账面”依然强劲，但结构性的裂缝已经清晰可见\n\n报告开篇即点明：美国以全球4%的人口，创造了26%的全球GDP，贡献了超过50%的全球市值。在全球前100强企业中，美国占据了59席。过去几年，美国的生产率增速在主要经济体中领先，宣布的绿地外商直接投资流入也比疫情前翻了一番。\n\n这些数字固然亮眼，但麦肯锡并不满足于复述成就。报告在第一章就引入了“竞争力”的三维定义：全球领先的企业、创新与技术领导力、个人经济机会与繁荣。前两个维度美国表现突出，但第三个维度——经济机会——已经出现明显裂痕。收入不平等、教育水平下滑、基础设施评级仅为C级，这些都被报告明确列为“需要反思的理由”。\n\n> **KC评论：** 这份报告最值得注意的不是美国有多强，而是它把“竞争力”定义为一个包含社会包容性的概念。如果只看GDP和市值，美国依然遥遥领先；但如果把教育、基建、财政可持续性纳入，画面就复杂得多。完整报告中有几十个横向对比图表，覆盖G7国家与\n\n[... middle omitted ...]\n\n。这些未在本文中展开的图表和假设，正是社群中持续讨论的内容。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美国经济竞争力，藏在250年的自我迭代里\n\n封面主标题：美国经济竞争力密码\n封面副标题：250年4个阶段，凭什么领先？\n\n---\n\n**美国的经济竞争力，不是天生的，而是不断“重启”的结果。**\n\n一份来自某外资投行（McKinsey Global Institute）的最新研报，系统梳理了美国从建国到今天的经济竞争力演变。看完最大的感受是：没有一成不变的领先，只有持续进化的能力。\n\n**1/ 当前有多强？**\n- 全球4%的人口，贡献了26%的全球GDP\n- 全球市值前100公司里，美国占59家\n- 过去5年生产率增速在主要经济体中领先\n- 全球AI领域私人投资1091亿美元，是第二名中国的10倍\n\n**2/ 它的竞争力靠什么？**\n研报提炼了三个核心维度：\n- **全球领先的企业**——能打、能规模化的公司\n- **创新与技术领导力**——持续走在技术前沿\n- **经济机会**——增长红利能惠及普通人\n\n这三个维度互相强化：高生产率→高工资→吸引顶尖人才→更多创新→更强企业。\n\n**3/ 历史上的4个章节**\n从农业经济→工业革命→科学时代→数字时代，美国的经济模式一直在变。每一次转型都伴随着基础设施、教\n\n[... middle omitted ...]\n\nnsey Global Institute was established in 1990. Our mission is to provide a fact base to aid decision making on the economic and business issues most critical to the world's companies and polic\n\n[... middle omitted ...]\n\nany\n\nDesigned by the McKinsey Global Institute\n\nmckinsey.com/mgi\n\nX @McKinsey\\_MGI\n\n@McKinseyGlobalInstitute\n\nin @McKinseyGlobalInstitute\n\nSubscribe to MGI's LinkedIn newsletter,\n\nForward Thinking: mck.co/forwardthinking"
  },
  {
    "id": "R019",
    "title": "麦肯锡：HR正站在“被IT吞噬”与“重塑组织”的分叉口",
    "digest": "[wechat_article.md]\n# 麦肯锡：HR正站在“被IT吞噬”与“重塑组织”的分叉口\n\n2026年，全球劳动力市场正在经历一个微妙的转折点。宏观经济的不确定性让员工流动率下降，AI的渗透让技能需求结构发生根本性位移，而HR部门自身的变革速度却远远落后于外部环境的变化。\n\n麦肯锡最新发布的《HR Monitor 2026》报告，基于对全球10个国家、1300名HR专业人士和5500名员工的调研，给出了一个清晰的判断：HR职能正站在一个分叉路口。一条路是继续维持现状，让日益复杂的技术变革超出自身能力边界，最终导致HR的核心职责被IT或数字化部门逐步蚕食。另一条路则是主动重塑，成为AI时代组织转型的架构师和领航员。\n\n这份报告最值得关注的判断并非关于某个具体的HR流程改进，而是一个系统性的警示：**如果HR不能在战略规划、技能管理、运营模式这三个维度上完成从“职能卓越”到“系统级变革”的跃迁，它在未来三到五年内面临的根本不是地位提升问题，而是职能边界被重新定义的问题。**\n\n> **KC评论：** 麦肯锡的这份报告本质上是在说，HR的“舒适区”正在消失。过去几年，HR在流程优化、招聘效率、员工体验等方面取得了不少进步，但这些进步大多是在既定框架内的改良。现在，AI带来的任务重组和组织形态变化，要求HR必须跳出“管人”的旧角色，去思考“人和智能体如何协作”的新命题。报告中的关键数据——比如只有11%的企业在做三年以上的战略性人力规划——暴露了多数组织在这方面的准备严重不足。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 战略规划的最大盲区：11%的企业在做长期规划，而技能缺口正在加速扩大\n\n麦肯锡的报告揭示了一个核心矛盾：几乎所有企业都在做人力规划，但绝大多数是短期的、运营性的。数据显示，62%的受访企业会进行组织层面的人力规划，但只有11%的企业将规划\n\n[... middle omitted ...]\n\n新最新的研报解读与数据合集，帮助你在市场变化中保持信息优势。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nHR的2026：从配角到架构师\n\nHR正在被重写\n\nAI来了，HR不只是招人发工资，它正在成为组织AI转型的“架构师”和“灯塔”。\n\n某外资投行最新2026年HR Monitor报告，调查了10国1300名HR和5500名员工，信息密度极高。帮你划几个重点👇\n\n1️⃣ 人才规划：别只看下季度，要看3-5年\n现在只有11%的企业在做战略级人才规划（3年以上），大部分还盯着12个月内的headcount。AI正在重塑岗位技能，不做前瞻规划，后面会跟不上。\n\n2️⃣ 技能缺口：HR可能低估了变化\n23%的员工现在技能就不够用，22%担心5年内跟不上。但HR对“未来技能”的判断有偏差——软件工程需求在降，数字素养、推理能力在快速上升。这个错位要警惕。\n\n3️⃣ 招聘：市场稳定了，但效率要提\noffer接受率上升了3个百分点，招聘成功率升了4个百分点。但流程还是慢，AI能帮大忙，前提是流程先设计好，不能直接把AI叠在旧系统上。\n\n4️⃣ 员工在留，但为什么留？\n离职率降了2个百分点，但员工最在意的是薪酬（52%）、工作生活平衡（46%）、工作稳定（45%）。HR光加福利没用，公平、透明、可持续的节奏才是关键。\n\n5️⃣\n\n[... middle omitted ...]\n\n![](images/716272e8c332e86b994e15df2d12296c92a5b2d00dc1778c822f196121f04a8e.jpg)\n\nCHAPTER 1\n\n![](images/70e5863b6aacfbab64e08efd6a8fcc12ca693f3cf397a6de25a62e4e61783f0a.jpg)\n\nCHAPTER 2\n\nCHAP\n\n[... middle omitted ...]\n\npyright © McKinsey & Company\n\nwww.McKinsey.com\n\n## Find more content like this on the McKinsey Insights App\n\n![](images/cbb7555a9a6e4cfeed1aa753e4198a180be9f201fc43fcdc648bdfcb6b9d2b4e.jpg)\n\nScan • Download • Personalize"
  },
  {
    "id": "R020",
    "title": "麦肯锡：2025年，企业最大的风险不是AI，而是把学习当成福利",
    "digest": "[wechat_article.md]\n# 麦肯锡：2025年，企业最大的风险不是AI，而是把学习当成福利\n\n2025年，企业面临的最大挑战不是技术选型，不是成本控制，而是如何让组织在持续动荡中保持“学习能力”这一核心资产。麦肯锡研究与创新学习实验室最新发布的《2025学习趋势展望》给出了一个反直觉的判断：当大多数企业还在纠结“要不要用AI替代员工”时，真正领先的组织已经在问一个更根本的问题——如何让工作本身变成发展的引擎。\n\n这份报告不是一份趋势清单。麦肯锡明确将其定义为“导航工具”，而非“趋势摘要”。报告的核心主张是：未来三年，企业的人才发展必须从“支持功能”升级为“战略驱动力”，而实现这一转变的钥匙，藏在三个相互强化的趋势中——流动的发展生态系统、负责任的AI采纳、以及组织韧性的系统性构建。\n\n报告中最值得关注的信号不是某个新技术，而是一个认知转折：**发展不再是一项福利，而是一种“关怀行为”（act of care）**。这个表述听起来温和，但其商业含义极为锋利——那些把员工发展当作福利来做的企业，将在人才争夺战中系统性落后。\n\n> **KC评论：** 这份报告最值得反复咀嚼的不是它列出的趋势，而是它提出的底层逻辑。麦肯锡明确说，三个宏观趋势——流动生态、负责任的AI、韧性——不是独立话题，而是“相互强化、无法孤立成功”的系统。这意味着，过去那种“今年主推AI培训、明年主抓员工幸福感”的碎片化策略，已经行不通了。完整报告里有一张非常清晰的系统互动图，值得仔细研究。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 流动发展生态：从“碎片化学习”到“工作即发展”的范式转换\n\n报告的第一大趋势直指一个长期痛点：企业的人才发展职能仍然处于“被动支撑”状态。2023年ATD调查显示，虽然72%的受访者认识到将HR转型为跨职能学科的重要性，但只有11%报告了有意义的\n\n[... middle omitted ...]\n\n动态。我们会在社群中继续探讨那些报告没有完全展开的关键问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n2025人才发展三大趋势，值得收藏\n\n三大趋势重塑人才发展\n\n2025年，人才发展不再只是培训部门的事。某外资投行最新研报指出，未来工作正在被三大趋势重塑，它们相互交织，缺一不可。\n\n1/ 流动的发展生态\n- 学习与工作的边界正在消失。不再是“停下工作去学习”，而是工作本身成为成长的引擎。\n- 人力资源、学习发展、人才管理等部门必须打破壁垒，围绕技能这一共同语言协同运作。\n- 数据驱动决策：用预测模型和可视化工具追踪技能差距，让发展策略从“事后补救”变为“前瞻布局”。\n\n2/ 负责任的AI应用\n- AI不是来取代你的，而是你的实时导师和协作者。它能根据你的表现、压力水平调整支持方式。\n- 关键在于信任。如果员工觉得AI是来监控或替代自己的，推行就会失败。领导者必须明确传达：AI是为了帮员工成功。\n- 重点培养高阶技能：批判性思维、创造力、情感智慧——这些是AI难以替代的核心竞争力。\n\n3/ 韧性与适应力\n- 不是“反弹回来”，而是“向前跳跃”。组织要学会在变化中预见挑战、主动适应。\n- 多代际员工的管理是机遇而非难题。每代人有不同的优势，关键在于如何激发其潜力。\n- 可持续的工作节奏：支持员工恢复精力，而不是\n\n[... middle omitted ...]\n\nurring. Roles, systems, and scopes of influence that once seemed defined or distinct – learning vs operations, people vs technology, work vs life – are now interdependent, overlapping, and ine\n\n[... middle omitted ...]\n\npany\n\nLearning Lab By McKinsey 2025\n\nCopyright © McKinsey & Company\n\nDesigned by SJO Design Center\n\nwww.mckinsey.com\n\n@McKinsey\n\n@McKinsey\n\n![](images/d30c7201c6e9cbbc44b1449d1ba7a2d858d1569ee12796967c7c773cf08f8691.jpg)"
  },
  {
    "id": "R021",
    "title": "麦肯锡：88%企业在试AI，但81%未见到利润",
    "digest": "[wechat_article.md]\n# 麦肯锡：88%企业在试AI，但81%未见到利润\n\n麦肯锡在2026年2月发布的《组织状态》报告中，抛出了一个让企业决策者无法回避的核心矛盾：绝大多数组织已经开始拥抱人工智能，但绝大多数组织也并未因此获得可观的财务回报。88%的受访组织正在以某种形式试验AI，然而81%的受访者坦言，这些尝试并未对利润产生实质性的影响。这不是一个关于技术是否有效的疑问，而是一个关于组织是否准备好迎接技术的问题。\n\n这份报告基于对全球超过10,000名高管和领导者的调研，覆盖15个国家与16个行业。它试图回答一个根本性的追问：在技术、经济和劳动力三大结构性力量同时重塑商业环境的今天，组织如何才能从短期的韧性转向持续的生产力与长期的价值创造？\n\n报告得出的结论清晰且尖锐：那些只将AI视为效率工具、在现有流程上做局部修补的组织，注定与真正的价值增长无缘。真正的赢家，将是那些敢于推动“双重转型”——同时改造技术与组织——的企业。它们需要重新想象工作如何完成，重新定义职能与端到端流程，并从根本上重塑传统结构。\n\n> **KC评论：** 这个数据点值得所有管理者停下来思考。88%的试验率与81%的无利润结果之间，存在一个巨大的“价值黑洞”。报告暗示，这个黑洞并非技术本身，而是组织层面的障碍——缺乏清晰的所有权、缺乏系统性的流程重构、以及缺乏对员工能力的同步投入。这意味着，企业现在面临的不是“要不要用AI”的选择，而是“如何用组织变革来兑现AI承诺”的紧迫命题。\n\n---\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 86%的领导者承认组织尚未准备好日常运营中融入AI\n\n麦肯锡的调研揭示了一个令人不安的认知鸿沟：高达86%的领导者认为，自己的组织在将AI融入日常运营方面准备不足。更值得警惕的是，每六家组织中就有一家没有明确的C级负责人来推动AI采纳。\n\n[... middle omitted ...]\n\n原始图表，或者希望加入我们的讨论社群，欢迎通过下方图片加入。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n组织正在经历3大重塑力量\n\n**组织变革的三股推力**\n\n某外资投行最新研报《组织状态2026》（State of Organizations 2026）调研了全球15国、16个行业、超10,000名高管，发现：\n\n**1/ 技术颠覆：AI不是插件，是底层逻辑**\n- 88%的组织已在尝试AI，但81%没看到实质利润增长\n- 86%的领导者觉得组织没准备好日常用AI\n- 真正的机会在于“双重转型”：技术+组织，重新设计端到端工作流\n\n**2/ 经济与地缘不确定性**\n- 近3/4受访者表示地缘不确定性已显著影响业务\n- 贸易正向邻近伙伴转移，组织需要“深层灵活性”来反弹，而非恢复原样\n\n**3/ 劳动力结构变化**\n- 员工期望、人口结构、技术驱动的工作模式都在变\n- 领导者需重新定义领导力，从“控制”转向“由内而外”的自我领导\n\n**研报核心判断**：这三股力量不是短期波动，而是结构性重塑。组织的关键词已从短期韧性，转向“持续生产力”和“长期价值创造”。\n\n**一个值得关注的矛盾**：超过一半领导者预期环境变化有正面影响，但72%承认组织没完全准备好。即使乐观派，也仅1/3感到有准备。\n\n**讨论**：你所\n\n[... middle omitted ...]\n\n performance edge\n53 Sharpening the focus on diversity and inclusion\n57 Reinventing leadership: Leading from the inside out\n64 Business as change: Managing continuous transformation in the org\n\n[... middle omitted ...]\n\nro, Sasha Goluskin, Scott Brugmans, Tarek Bakali, Tristan Allen, Yueyang Chen, and Zoe Fox.\n\nState of Organizations 2026\nBy McKinsey\nFebruary 2026\nCopyright © McKinsey & Company\n\nwww.McKinsey.com\n\nX @McKinsey\nf @McKinsey"
  },
  {
    "id": "R022",
    "title": "麦肯锡：CEO不下场，AI永远只是成本",
    "digest": "[wechat_article.md]\n# 麦肯锡：CEO不下场，AI永远只是成本\n\n这份报告最值得看的判断不是“AI使用率又创新高”，而是：**真正从AI中拿到利润的公司，正在做三件大多数企业还没做的事——把CEO拉进治理、重新设计工作流、以及用KPI而不是讲故事来管理AI项目。**\n\n麦肯锡2025年3月发布的《The State of AI》全球调查，覆盖1491位来自101个国家的企业受访者。报告试图回答一个核心问题：当几乎所有公司都在用AI时，为什么只有极少数看到了真实的利润影响？\n\n答案不是技术选型，不是算力投入，而是组织架构的“重布线”。这份报告提供了迄今为止最系统的证据，说明企业需要做出哪些结构性的改变，才能把AI从“实验工具”变成“利润引擎”。\n\n以下是我们从这份报告中提炼出的六个核心洞察，以及一个报告没有完全回答的关键追问。\n\n![研报图表 1](assets/xhs_card_01.png)\n\n## 1. 这轮变化真正考验的是企业能否把规模转化为议价权\n\n报告最反常识的发现是：年收入超过5亿美元的大型企业，在AI部署上正在加速拉开与中小企业的差距。这不是简单的“大公司更有钱”，而是大公司在治理结构、风险管理和人才配置上采取了完全不同的路径。\n\n大型企业更倾向于让CEO亲自监督AI治理，而中小型企业更多把这事交给IT或数字部门。报告通过相关性分析发现，CEO对AI治理的参与度，是所有25个测试属性中，与企业EBIT影响相关度最高的因素之一。在大公司样本中，这个相关性甚至更强。\n\n> **KC评论：** 这意味着AI不是“买了工具就完事”的IT项目，而是一场需要CEO亲自拉动的组织变革。报告没有明说但数据暗示的是：如果CEO不参与，AI项目大概率会变成“成本中心”而非“利润中心”。完整报告里有一张25个属性的相关性排序图，值得仔细看——它揭示了哪些投入真正能转化为利润。\n\n![研\n\n[... middle omitted ...]\n\n表，或者想加入一个每天讨论这些报告结论的社群，欢迎扫码加入。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI落地，CEO必须亲自下场\n\nCEO带队，AI才能出业绩\n\nAI不是IT部门的事，一把手不盯就凉了\n\n某外资投行最新调研显示，企业想从AI里拿到真金白银，关键不是技术多强，而是组织怎么变。\n\n1/ 谁在管AI，决定能赚多少\nCEO亲自管AI治理的企业，AI带来的利润提升最明显。28%的受访企业由CEO主抓AI，大公司（年营收5亿美元以上）更倾向让CEO牵头，规模小的反而依赖董事会。多数企业是“双领导”共管，但效果分化很大。\n\n2/ 流程不改，AI白干\n在所有组织变革动作里，重新设计工作流程对AI利润影响最大。但只有21%的企业真正动手改了流程——大多数还在“旧瓶装新酒”。比如用AI生成营销文案，但审批、分发流程还是老一套，价值根本出不来。\n\n3/ 大公司更舍得“上手段”\n大企业在12项AI落地最佳实践中全面领先：定路线图、设专职团队、建培训体系、跟踪KPI。小公司多数还在单点试水，而大公司已经用“企业级变革思维”在推——从数据治理到代码复用，提前搭好底座。\n\n4/ 风险管控也在升级\n比去年更积极应对AI风险：不准确、网络安全、知识产权侵权是前三大痛点。大公司尤其重视安全和隐私，但对“输出可解释性”反而没那么\n\n[... middle omitted ...]\n\nf555ae093dc404956428b0.jpg)\n\norganizations are starting to make organizational changes designed to generate future value from gen AI, and large companies are leading the way. The latest McKins\n\n[... middle omitted ...]\n\nh 2025  \nCopyright © McKinsey & Company  \nDesigned by McKinsey Global Publishing\n\nFind more content like this on the McKinsey Insights App\n\n![](images/0458fb11ffa1d85bf517ff96c548eb51a4025c0b79a6af63c0bcb79633e51bd1.jpg)"
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "Figure 1",
    "context": "Figure 1: EMAX tech IP and exports %3m/3m, saar, both scales. IP thru Apr, exports incl. May forecast ## Oil Down, Dollar Up: A Rotation in Asian Central Banks With energy prices declining but the US Dollar strengthening, pressu"
  },
  {
    "figure_id": "F002",
    "report_id": "R002",
    "label": "Exhibit 1",
    "context": "Exhibit 1: The Strait of Hormuz disruption contributed to commodity returns outperforming other assets year to date, especially as a strong roll yield for oil combined with higher prices Importantly, the upside to energy prices d"
  },
  {
    "figure_id": "F003",
    "report_id": "R002",
    "label": "Exhibit 2",
    "context": "Exhibit 3: Policy-risk-driven copper flows into the US drove the ex-US market into a deficit this year"
  },
  {
    "figure_id": "F004",
    "report_id": "R002",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Policy-risk-driven copper flows into the US drove the ex-US market into a deficit this year Exhibit 4: Continued central bank diversification remains the main driver of our constructive gold price outlook"
  },
  {
    "figure_id": "F005",
    "report_id": "R002",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Continued central bank diversification remains the main driver of our constructive gold price outlook Exhibit 5: The recent World Gold Council central bank survey suggests continued gold demand ## To Each (Inflation"
  },
  {
    "figure_id": "F006",
    "report_id": "R002",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Continued central bank diversification remains the main driver of our constructive gold price outlook Exhibit 5: The recent World Gold Council central bank survey suggests continued gold demand ## To Each (Inflation"
  },
  {
    "figure_id": "F007",
    "report_id": "R002",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Global EV sales have sharply accelerated during the Iran conflict... Exhibit 7: ...as have China solar panel exports Combined with the fact that power infrastructure can face bottlenecks, as has been the case in the"
  },
  {
    "figure_id": "F008",
    "report_id": "R002",
    "label": "Exhibit 6",
    "context": "Exhibit 8: Commodity supply is currently heavily concentrated, with a large share of supply in geopolitical or trade-dispute hot spots"
  },
  {
    "figure_id": "F009",
    "report_id": "R002",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Commodity supply is currently heavily concentrated, with a large share of supply in geopolitical or trade-dispute hot spots ## Appendix Exhibit 9: The recent Hormuz energy supply disruption is the latest example of w"
  },
  {
    "figure_id": "F010",
    "report_id": "R002",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Commodity supply is currently heavily concentrated, with a large share of supply in geopolitical or trade-dispute hot spots ## Appendix Exhibit 9: The recent Hormuz energy supply disruption is the latest example of w"
  },
  {
    "figure_id": "F011",
    "report_id": "R003",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Bilateral DVP, SOFR, TGCR within the fed funds target range over the past year Exhibit 2: Reserves / Total Commercial Bank Assets and SOFR - IORB spread over different Fed balance sheet regimes In Why So Soft, Repo?,"
  },
  {
    "figure_id": "F012",
    "report_id": "R003",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Bilateral DVP, SOFR, TGCR within the fed funds target range over the past year Exhibit 2: Reserves / Total Commercial Bank Assets and SOFR - IORB spread over different Fed balance sheet regimes In Why So Soft, Repo?,"
  },
  {
    "figure_id": "F013",
    "report_id": "R003",
    "label": "Exhibit 4",
    "context": "Exhibit 3: July 2026 1-month AXW futures contract since February 23 Exhibit 4: Generic front 1-month AXW futures contract since December 2020 Several factors are likely also contributing to rich AXW levels, including issuance-r"
  },
  {
    "figure_id": "F014",
    "report_id": "R003",
    "label": "Exhibit 3",
    "context": "Exhibit 3: July 2026 1-month AXW futures contract since February 23 Exhibit 4: Generic front 1-month AXW futures contract since December 2020 Several factors are likely also contributing to rich AXW levels, including issuance-r"
  },
  {
    "figure_id": "F015",
    "report_id": "R003",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Generic third 1-month AXW futures contract and the S&P 500 since December 2020 Exhibit 6: Generic third 1-month AXW futures contract and the S&P 500 since June 2022, rolling 252-day z-score We think risk of a tumultu"
  },
  {
    "figure_id": "F016",
    "report_id": "R003",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Generic third 1-month AXW futures contract and the S&P 500 since December 2020 Exhibit 6: Generic third 1-month AXW futures contract and the S&P 500 since June 2022, rolling 252-day z-score We think risk of a tumultu"
  },
  {
    "figure_id": "F017",
    "report_id": "R003",
    "label": "Exhibit 7",
    "context": "Exhibit 7: SFRZ6M7 and SFRM7Z7 futures contracts over the past five years Exhibit 8: SFRZ6M7 and SFRM7Z7 futures contracts over the past year ## Two paths to a flatter Z6M7 curve post-FOMC"
  },
  {
    "figure_id": "F018",
    "report_id": "R003",
    "label": "Exhibit 7",
    "context": "Exhibit 7: SFRZ6M7 and SFRM7Z7 futures contracts over the past five years Exhibit 8: SFRZ6M7 and SFRM7Z7 futures contracts over the past year ## Two paths to a flatter Z6M7 curve post-FOMC ## 1. Perception of a Fed policy mista"
  },
  {
    "figure_id": "F019",
    "report_id": "R003",
    "label": "Exhibit 10",
    "context": "Exhibit 9: MS proxy effective fed funds rate and actual effective fed fund rate since June 2006 Exhibit 10: MS proxy effective fed funds rate and actual effective fed fund rate since June 2024"
  },
  {
    "figure_id": "F020",
    "report_id": "R003",
    "label": "Exhibit 9",
    "context": "Exhibit 9: MS proxy effective fed funds rate and actual effective fed fund rate since June 2006 Exhibit 10: MS proxy effective fed funds rate and actual effective fed fund rate since June 2024 \\- That is consistent with how our"
  },
  {
    "figure_id": "F021",
    "report_id": "R003",
    "label": "Exhibit 11",
    "context": "Exhibit 11: 1-year forward 1-year USD CPI swap rate and 1-year USD CPI swap rate since June 2024 Exhibit 12: 1-year forward 1-year USD CPI swap rate and 1-year USD CPI swap rate since June 2024 As shown in Exhibit 11, market par"
  },
  {
    "figure_id": "F022",
    "report_id": "R003",
    "label": "Exhibit 11",
    "context": "Exhibit 11: 1-year forward 1-year USD CPI swap rate and 1-year USD CPI swap rate since June 2024 Exhibit 12: 1-year forward 1-year USD CPI swap rate and 1-year USD CPI swap rate since June 2024 As shown in Exhibit 11, market par"
  },
  {
    "figure_id": "F023",
    "report_id": "R003",
    "label": "Exhibit 13",
    "context": "Exhibit 13: 2-year and 5-year US CPI inflation swaps since June 2021 Exhibit 14: 2-year and 5-year US CPI inflation swaps since June 2025 We continue to think SFRZ6M7 curve flatteners offer a compelling way to express the view t"
  },
  {
    "figure_id": "F024",
    "report_id": "R003",
    "label": "Exhibit 13",
    "context": "Exhibit 13: 2-year and 5-year US CPI inflation swaps since June 2021 Exhibit 14: 2-year and 5-year US CPI inflation swaps since June 2025 We continue to think SFRZ6M7 curve flatteners offer a compelling way to express the view t"
  },
  {
    "figure_id": "F025",
    "report_id": "R003",
    "label": "Exhibit 15",
    "context": "Exhibit 15: SFRZ6M7 and SFRM7Z7 futures contracts over the past five years Exhibit 16: SFRZ6M7 and SFRM7Z7 futures contracts over the past year We suggest investors tighten trailing stops on SFRZ6M7 curve flatteners to 10bp and"
  },
  {
    "figure_id": "F026",
    "report_id": "R003",
    "label": "Exhibit 15",
    "context": "Exhibit 15: SFRZ6M7 and SFRM7Z7 futures contracts over the past five years Exhibit 16: SFRZ6M7 and SFRM7Z7 futures contracts over the past year We suggest investors tighten trailing stops on SFRZ6M7 curve flatteners to 10bp and"
  },
  {
    "figure_id": "F027",
    "report_id": "R004",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Strong MoM growth in Jun (US\\$25.5bn; +16% MoM); more than 3x higher than 2025 year-average level Korea semis exports (mostly memory) – first 20 days of month (US\\$bn) BofA GLOBAL RESEARCH Exhibit 5: Record-high sales"
  },
  {
    "figure_id": "F028",
    "report_id": "R004",
    "label": "Exhibit 3",
    "context": "Exhibit 4: Up 188% YoY in Jun; already five consecutive months of triple-digit growth"
  },
  {
    "figure_id": "F029",
    "report_id": "R004",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Up 188% YoY in Jun; already five consecutive months of triple-digit growth Exhibit 6: Significant margin enhancement in May-Q (GM 85%, OPM 81%); mgmt. expects high-margin profile to continue Micron – Gross/OP margin tr"
  },
  {
    "figure_id": "F030",
    "report_id": "R004",
    "label": "Exhibit 4",
    "context": "Exhibit 7: Robust price hike observed in May-Q (DRAM up low-60% QoQ and NAND up mid-80%)"
  },
  {
    "figure_id": "F031",
    "report_id": "R004",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Robust price hike observed in May-Q (DRAM up low-60% QoQ and NAND up mid-80%) Exhibit 8: Record-high margins in May-Q (DRAM 81%, NAND 78%) Micron – DRAM and NAND OP margin trend ## Global memory forecasts Exhibit 9:"
  },
  {
    "figure_id": "F032",
    "report_id": "R004",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Robust price hike observed in May-Q (DRAM up low-60% QoQ and NAND up mid-80%) Exhibit 8: Record-high margins in May-Q (DRAM 81%, NAND 78%) Micron – DRAM and NAND OP margin trend ## Global memory forecasts Exhibit 9:"
  },
  {
    "figure_id": "F033",
    "report_id": "R004",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Only a few weeks for both DRAM and NAND as of April 2026, much lower than normal (1-2 months); 2H26 inventories likely up following fab utilization increase but still tight (3-4 weeks likely) Exhibit 17: Both DRAM and"
  },
  {
    "figure_id": "F034",
    "report_id": "R004",
    "label": "Exhibit 16",
    "context": "Exhibit 18: Mostly server (including HBM) and smartphone-driven sales seen Implied DRAM sales mix based on bit shipments x ASP by application"
  },
  {
    "figure_id": "F035",
    "report_id": "R004",
    "label": "Exhibit 29",
    "context": "Exhibit 29: Substantial HBM content growth expected in 2025/2026-27, led by B300, Rubin, and Rubin Ultra NVIDIA GPUs HBM spec evolution; Rubin Ultra HBM content also up 3x vs 2026 1 $^{st}$ Rubin BofA GLOBAL RESEARCH Exhibit 30: 1"
  },
  {
    "figure_id": "F036",
    "report_id": "R004",
    "label": "Exhibit 30",
    "context": "Exhibit 30: 10-30% HBM content growth observed in AMD GPUs as well led by MI350X in 2025 and MI400 series in 2026 AMD GPUs HBM spec evolution BofA GLOBAL RESEARCH Exhibit 31: HBM capacity to hit 1TB with Rubin Ultra (2027) and the"
  },
  {
    "figure_id": "F037",
    "report_id": "R004",
    "label": "Exhibit 32",
    "context": "Exhibit 33: Our memory indicator reached an all-time high of 189 in Mar/Apr-26, driven by exceptionally strong DRAM/NAND spot pricing, rising ASPs and billings, along with Korea's $150\\%+$ export growth. BofA Memory Indicator – back"
  },
  {
    "figure_id": "F038",
    "report_id": "R004",
    "label": "Exhibit 33",
    "context": "Exhibit 34: May share price surged to record highs, supported by Samsung (strong 1Q results, optimism around HBM4 upside, and higher exposure to conventional DRAM) and Nanya Tech (record Jan–May monthly sales, up \\~500–700% YoY)."
  },
  {
    "figure_id": "F039",
    "report_id": "R004",
    "label": "Exhibit 34",
    "context": "Exhibit 35: Amazon, Microsoft, Alphabet, Meta, and Oracle capex collectively to grow \\~80% YoY in 2026 to \\$650bn even after strong 65% YoY growth in 2025; 2027/28 capex to hit \\$800/950bn+ Combined capex of top 4 US tech companies"
  },
  {
    "figure_id": "F040",
    "report_id": "R004",
    "label": "Exhibit 35",
    "context": "Exhibit 36: Record-high capex spend by all big-4 hyperscalers expected to continue in 2026E; robust growth since 2024 Hyperscalers' capex growth – YoY change Note: Microsoft and Oracle data adjusted for CY basis \\*\\*Oracle's 2025"
  },
  {
    "figure_id": "F041",
    "report_id": "R004",
    "label": "Exhibit 35",
    "context": "Exhibit 37: Amazon, Microsoft, Alphabet, and Meta overall revenue expected to grow +15-20% in 2026-28"
  },
  {
    "figure_id": "F042",
    "report_id": "R004",
    "label": "Exhibit 37",
    "context": "Exhibit 37: Amazon, Microsoft, Alphabet, and Meta overall revenue expected to grow +15-20% in 2026-28 BofA GLOBAL RESEARCH Exhibit 38: Gross margin of hyperscalers strong at around 70-80% levels Gross margin trend of top 4 US hype"
  },
  {
    "figure_id": "F043",
    "report_id": "R004",
    "label": "Exhibit 37",
    "context": "Exhibit 39: Cloud revenue growth still solid at 35-40% YoY in 2026-28 Cloud revenue of hyperscalers consistently strong BofA GLOBAL RESEARCH"
  },
  {
    "figure_id": "F044",
    "report_id": "R004",
    "label": "Exhibit 38",
    "context": "Exhibit 40: High OPM seen among AWS (35%+) and Azure (40%+); Google's margin also set to reach 30-35% in 2026-28 Cloud OPM trend also high BofA GLOBAL RESEARCH"
  },
  {
    "figure_id": "F045",
    "report_id": "R004",
    "label": "Exhibit 39",
    "context": "Exhibit 41: DRAM spot prices rebounded through June after softening through April–May, following a strong rally from September 2025 to January 2026. Prices have reached multi-decade highs, with 16Gb DDR5 at \\~\\$47 and DDR4 at \\~\\$72"
  },
  {
    "figure_id": "F046",
    "report_id": "R004",
    "label": "Exhibit 41",
    "context": "Exhibit 42: DRAM spot and contract prices climbed to record highs of \\~\\$35–40, with moderate growth in 2Q26 following a strong rally in 4Q25 and 1Q26. DRAM spot and contract price - quarterly average trend"
  },
  {
    "figure_id": "F047",
    "report_id": "R004",
    "label": "Exhibit 42",
    "context": "Exhibit 42: DRAM spot and contract prices climbed to record highs of \\~\\$35–40, with moderate growth in 2Q26 following a strong rally in 4Q25 and 1Q26. DRAM spot and contract price - quarterly average trend BofA GLOBAL RESEARCH Ex"
  },
  {
    "figure_id": "F048",
    "report_id": "R004",
    "label": "Exhibit 43",
    "context": "Exhibit 44: Prices rebounded through May and June, reaching an all-time high (\\$47) following a volatile April. Uptrend was driven by strong gains in Oct (+70%), Nov (+60%), Jan (+25%), before moderating into a more subdued trend du"
  },
  {
    "figure_id": "F049",
    "report_id": "R004",
    "label": "Exhibit 44",
    "context": "Exhibit 46: 8Gb DDR4 prices remained flat in 2H-Jun vs up in 1H-Jun and through May after stabilizing in April; they remain significantly higher YoY due to supply cuts by major vendors, currently around \\$30—well above the prior \\~\\"
  },
  {
    "figure_id": "F050",
    "report_id": "R004",
    "label": "Exhibit 44",
    "context": "Exhibit 48: DDR4 and DDR5 (16Gb) contract prices are similar at US\\$35-\\$40 levels – DDR5 price premium no longer exists due to DDR4 shortage 16Gb DDR5 vs 16Gb DDR4 contract price trend, Feb '23-Jun '26 BofA GLOBAL RESEARCH"
  },
  {
    "figure_id": "F051",
    "report_id": "R004",
    "label": "Exhibit 48",
    "context": "Exhibit 47: Prices edged up slightly in late May/through June after a \\~25% correction from April to mid-May, having peaked near \\~\\$80 in early March. Despite this pullback, prices remain elevated—up \\~2000% from \\~\\$3 in October 2"
  },
  {
    "figure_id": "F052",
    "report_id": "R004",
    "label": "Exhibit 48",
    "context": "Exhibit 47: Prices edged up slightly in late May/through June after a \\~25% correction from April to mid-May, having peaked near \\~\\$80 in early March. Despite this pullback, prices remain elevated—up \\~2000% from \\~\\$3 in October 2"
  },
  {
    "figure_id": "F053",
    "report_id": "R004",
    "label": "Exhibit 45",
    "context": "Exhibit 49: DDR5 and DDR4 contract prices expected to be flat MoM in Jun vs up +10-15% MoM each in Apr/May-26; price strong through 2H25 and early 2026 16Gb DDR5 vs 16Gb DDR4 contract price change - MoM, Feb '23-Jun '26 BofA GLOBA"
  },
  {
    "figure_id": "F054",
    "report_id": "R004",
    "label": "Exhibit 49",
    "context": "Exhibit 49: DDR5 and DDR4 contract prices expected to be flat MoM in Jun vs up +10-15% MoM each in Apr/May-26; price strong through 2H25 and early 2026 16Gb DDR5 vs 16Gb DDR4 contract price change - MoM, Feb '23-Jun '26 BofA GLOBA"
  },
  {
    "figure_id": "F055",
    "report_id": "R004",
    "label": "Exhibit 50",
    "context": "BofA GLOBAL RESEARCH 16Gb DDR5 spot vs contract price trend (US\\$), Aug '23-Jun '26 BofA GLOBAL RESEARCH NAND wafer contract price trend, Aug '23-Jun '26 BofA GLOBAL RESEARCH"
  },
  {
    "figure_id": "F056",
    "report_id": "R004",
    "label": "Exhibit 50",
    "context": "Exhibit 54: 16Gb DDR5 spot and contract prices are in the range of US\\$35-40 vs historical range of US\\$3-5 June-26 is an estimate from TrendForce released on 16th June"
  },
  {
    "figure_id": "F057",
    "report_id": "R004",
    "label": "Exhibit 54",
    "context": "Exhibit 51: Flat in June, while slightly corrected in Apr/May vs up +15-20% in Feb/ Mar-26 and up +40-70% MoM in Oct/Nov/Dec/Jan 512Gb NAND wafer spot average – MoM change, Jun'21 - Jun'26"
  },
  {
    "figure_id": "F058",
    "report_id": "R004",
    "label": "Exhibit 53",
    "context": "Exhibit 55: Jun'26 spot prices turned positive again while contract price expected to be flat, prices had witnessed a sharp Oct–Dec'25 rally and subsequent Feb–Mar moderation"
  },
  {
    "figure_id": "F059",
    "report_id": "R004",
    "label": "Exhibit 52",
    "context": "Exhibit 55: Jun'26 spot prices turned positive again while contract price expected to be flat, prices had witnessed a sharp Oct–Dec'25 rally and subsequent Feb–Mar moderation 16Gb DDR5 spot vs contract price trend – MoM change, Aug"
  },
  {
    "figure_id": "F060",
    "report_id": "R004",
    "label": "Exhibit 55",
    "context": "Exhibit 56: Current NAND spot and contract prices are a few times higher than 2025 summer level BofA GLOBAL RESEARCH Exhibit 58: Current price of 64GB DDR4/DDR5 modules hit all-time high of more than \\$1,000 level (DDR5: US\\$1,200"
  },
  {
    "figure_id": "F061",
    "report_id": "R004",
    "label": "Exhibit 55",
    "context": "Exhibit 56: Current NAND spot and contract prices are a few times higher than 2025 summer level BofA GLOBAL RESEARCH Exhibit 58: Current price of 64GB DDR4/DDR5 modules hit all-time high of more than \\$1,000 level (DDR5: US\\$1,200"
  },
  {
    "figure_id": "F062",
    "report_id": "R004",
    "label": "Exhibit 56",
    "context": "Exhibit 60: 1H-Jun SSD price sharply up vs Mar decline; prices witnessed a sharp surge in 1Q26 and April (per DRAMeXchange), following a gradual upward trend throughout Gb NAND spot vs contract price trend – MoM change, Ju"
  },
  {
    "figure_id": "F063",
    "report_id": "R004",
    "label": "Exhibit 58",
    "context": "Exhibit 58: Current price of 64GB DDR4/DDR5 modules hit all-time high of more than \\$1,000 level (DDR5: US\\$1,200, DDR4: US\\$1,100) Server DRAM contract price trend – DDR5 vs DDR4 modules, Jan '24-May '26 BofA GLOBAL RESEARCH Exhi"
  },
  {
    "figure_id": "F064",
    "report_id": "R004",
    "label": "Exhibit 60",
    "context": "Exhibit 60: 1H-Jun SSD price sharply up vs Mar decline; prices witnessed a sharp surge in 1Q26 and April (per DRAMeXchange), following a gradual upward trend throughout Gb NAND spot vs contract price trend – MoM change, Ju"
  },
  {
    "figure_id": "F065",
    "report_id": "R004",
    "label": "Exhibit 57",
    "context": "Exhibit 61: Jun prices have doubled compared to end-2025 levels, while the 2025 increase was more modest at around 35–40% Client SSD (for PC) price comparison – current vs. end-2025"
  },
  {
    "figure_id": "F066",
    "report_id": "R004",
    "label": "Exhibit 61",
    "context": "Exhibit 62: Memory companies still show very low P/E multiples despite robust stock price rally in May/through-June vs very strong earnings momentum (exceptionally strong DRAM and NAND ASP in 1Q/2Q26) Valuation comparison among memo"
  },
  {
    "figure_id": "F067",
    "report_id": "R004",
    "label": "Exhibit 63",
    "context": "Exhibit 63: Memory prices strongly up this week following Micron's upbeat results/guidance; prices remain elevated year-to-date, led by NAND and HDD with sustained strength in DRAM, underpinned by robust AI-driven demand Exhibit 6"
  },
  {
    "figure_id": "F068",
    "report_id": "R004",
    "label": "Exhibit 63",
    "context": "Exhibit 63: Memory prices strongly up this week following Micron's upbeat results/guidance; prices remain elevated year-to-date, led by NAND and HDD with sustained strength in DRAM, underpinned by robust AI-driven demand Exhibit 6"
  },
  {
    "figure_id": "F069",
    "report_id": "R006",
    "label": "Exhibit 1",
    "context": "Exhibit 1 - Exhibit 4). Exhibit 1: Hanwha Aerospace: 12m fwd P/E Exhibit 2: Hyundai Rotem: 12m fwd P/E Exhibit 3: Hanwha Aerospace: GSe EPS"
  },
  {
    "figure_id": "F070",
    "report_id": "R006",
    "label": "Exhibit 1",
    "context": "Exhibit 1 - Exhibit 4). Exhibit 1: Hanwha Aerospace: 12m fwd P/E Exhibit 2: Hyundai Rotem: 12m fwd P/E Exhibit 3: Hanwha Aerospace: GSe EPS Exhibit 4: Hyundai Rotem: GSe EPS"
  },
  {
    "figure_id": "F071",
    "report_id": "R006",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Hyundai Rotem: 12m fwd P/E Exhibit 3: Hanwha Aerospace: GSe EPS Exhibit 4: Hyundai Rotem: GSe EPS ## Korea Robotics"
  },
  {
    "figure_id": "F072",
    "report_id": "R006",
    "label": "Exhibit 3",
    "context": "Exhibit 5: Recent robotics VC deal activity underscores interests in the robotics sector"
  },
  {
    "figure_id": "F073",
    "report_id": "R006",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Recent robotics VC deal activity underscores interests in the robotics sector While investors frequently question if it is too early to build exposure to long-duration robotics stocks, we emphasize that robotics has be"
  },
  {
    "figure_id": "F074",
    "report_id": "R006",
    "label": "Exhibit 6",
    "context": "Exhibit 6: How long a task AI can do (at $50\\%$ success rate) is growing exponentially Each dot is a frontier AI model AI Task Completion Time Horizon ## Price Target Risks and Methodology - Hanwha Aerospace Our 12-month target p"
  },
  {
    "figure_id": "F075",
    "report_id": "R009",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 2: Continued growth in nuclear and gas equipment orders are expected to support company's valuation"
  },
  {
    "figure_id": "F076",
    "report_id": "R009",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 3: Our nuclear TAM is based on identifiable projects nearing equipment procurement stage Nuclear new build framework"
  },
  {
    "figure_id": "F077",
    "report_id": "R009",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Our nuclear TAM is based on identifiable projects nearing equipment procurement stage Nuclear new build framework EXHIBIT 4: Doosan's vertical integration and experience from projects such as Korea's domestic fleet and"
  },
  {
    "figure_id": "F078",
    "report_id": "R009",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 5: Doosan is the most experienced nuclear power system supplier outside of China and Russia Number of reactors built by supplier in the last 20 years ■ Chinese or Russian suppliers"
  },
  {
    "figure_id": "F079",
    "report_id": "R009",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 6: Doosan's booked nuclear equipment contracts. The company has spent over 40 years as a major global supplier of nuclear components, developing unrivaled expertise in the design and manufacturing of these systems"
  },
  {
    "figure_id": "F080",
    "report_id": "R009",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 8: We estimate around 35GW of nuclear project with USD250bn of TAM where Doosan could realistically participate"
  },
  {
    "figure_id": "F081",
    "report_id": "R009",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: Large reactors dominate, with SMRs contributing a smaller but still meaningful portion of future optionality Nuclear order by reactor (KRW tn) EXHIBIT 10: Regionally, we expect the next several years to be dominated by"
  },
  {
    "figure_id": "F082",
    "report_id": "R009",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 11: Polish nuclear project is one of the most important projects to watch, with the project progressing toward equipment and EPC contracting in the near term ## SCHEDULE FOR THE CONSTRUCTION OF THE FIRST NUCLEAR POWER PLANT"
  },
  {
    "figure_id": "F083",
    "report_id": "R009",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: Polish nuclear project is one of the most important projects to watch, with the project progressing toward equipment and EPC contracting in the near term ## SCHEDULE FOR THE CONSTRUCTION OF THE FIRST NUCLEAR POWER PLANT"
  },
  {
    "figure_id": "F084",
    "report_id": "R009",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 12: Bulgaria is also advancing to EPC contract stage within 2027"
  },
  {
    "figure_id": "F085",
    "report_id": "R009",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 13: We expect nuclear equipment margins are in the mid-double digit EBITDA margin range Framatome's revenue and EBITDA"
  },
  {
    "figure_id": "F086",
    "report_id": "R009",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 13: We expect nuclear equipment margins are in the mid-double digit EBITDA margin range Framatome's revenue and EBITDA ## GAS TURBINE FUNDAMENTALS SUPPORTS PRICE AND MARGIN EXPANSION There has never been a better time to b"
  },
  {
    "figure_id": "F087",
    "report_id": "R009",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 15: There has never been a better time to be a manufacturer of natural gas turbines. Gas turbine orders are set to increase to 100GW annually in the next few years which outpace current capacity of 60GW Global gas turbine or"
  },
  {
    "figure_id": "F088",
    "report_id": "R009",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 16: New orders for gas turbine pricing continues to trend higher, with reported pricing for recent orders reaching 70% above year-ago levels for heavy duty gas turbines Industry gas turbine order price tracker (\\$/kW)"
  },
  {
    "figure_id": "F089",
    "report_id": "R009",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 17: For gas turbine manufacturers, EBIT margins are expanding to the 20% range in 2028. We think this has clear readthrough for Doosan Gas and Power EBIT margin"
  },
  {
    "figure_id": "F090",
    "report_id": "R009",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 18: Doosan's turbine manufacturing capacity and turbine orders Doosan Enerbility: Gas turbine production capacity and orders (units)"
  },
  {
    "figure_id": "F091",
    "report_id": "R009",
    "label": "EXHIBIT 18",
    "context": "EXHIBIT 19: We expect cumulative shipped turbines reaching roughly 45 units by 2030 and 120 units by 2035. This implies gas service revenue of KRW1.1tn by 2035 Gas turbines in service by turbine vintage (units) and service revenue ("
  },
  {
    "figure_id": "F092",
    "report_id": "R009",
    "label": "EXHIBIT 19",
    "context": "EXHIBIT 20: We expect Doosan's gas business new orders to increase from KRW4.7tn in 2025 to KRW6.2tn in 2026, and to reach KRW6.9tn by 2030 Doosan Enerbility: Gas segment annual orders (KRW tn)"
  },
  {
    "figure_id": "F093",
    "report_id": "R009",
    "label": "EXHIBIT 20",
    "context": "EXHIBIT 21: New orders are a key driver of future revenue and backlog growth"
  },
  {
    "figure_id": "F094",
    "report_id": "R009",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 22: We expect order backlog reaches KRW53tn in 2030 which is above company target of KRW48tn Doosan Enerbility: 2030E Order backlog (KRW bn)"
  },
  {
    "figure_id": "F095",
    "report_id": "R009",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 23: We project revenue to reach KRW14.7tn in 2030 (+13% CAGR). Notably, our forecast exceeds the company's own target of KRW11.3tn for 2030, reflecting our more optimistic view on the business's growth prospects Doosan Enerb"
  },
  {
    "figure_id": "F096",
    "report_id": "R009",
    "label": "EXHIBIT 23",
    "context": "EXHIBIT 24: Doosan's nuclear and gas power generation equipment revenue mix is expected to increase from $41\\%$ in 2024 to over $75\\%$ by 2028 Doosan Enerbility: Standalone revenue mix by segment (%)"
  },
  {
    "figure_id": "F097",
    "report_id": "R009",
    "label": "EXHIBIT 24",
    "context": "EXHIBIT 25: We forecast a significant rise in Enerbility's operating profit margin, from $4\\%$ in 2025 to low-teens from 2028+ Doosan Enerbility: OPM vs Nuclear + Gas Mix"
  },
  {
    "figure_id": "F098",
    "report_id": "R009",
    "label": "EXHIBIT 25",
    "context": "EXHIBIT 26: Doosan Enerbility's consolidated financial outlook"
  },
  {
    "figure_id": "F099",
    "report_id": "R009",
    "label": "EXHIBIT 29",
    "context": "EXHIBIT 30: Doosan Enerbility's financial outlook Doosan Enerbility (034020 KS) KRW billion, except per share amounts"
  },
  {
    "figure_id": "F100",
    "report_id": "R011",
    "label": "Figure 1",
    "context": "Figure 1: Estimated fiscal risk shocks for the U.S. in 2025 Notes: This figure shows the evolution of fiscal risk shocks in the US in 2025. The thick line represents the median target shock from the distribution of shocks recovere"
  },
  {
    "figure_id": "F101",
    "report_id": "R011",
    "label": "Figure 1",
    "context": "Figure 1: Estimated fiscal risk shocks for the U.S. in 2025 Notes: This figure shows the evolution of fiscal risk shocks in the US in 2025. The thick line represents the median target shock from the distribution of shocks recovere"
  },
  {
    "figure_id": "F102",
    "report_id": "R011",
    "label": "Figure 3",
    "context": "Figure 3: Baseline 2SLS local-projection impulse response functions Notes: Impulse response functions to a 1-percentage-point fiscal-risk-driven increase in the 5-year government bond yield, estimated via 2SLS-LP as in equation (3"
  },
  {
    "figure_id": "F103",
    "report_id": "R011",
    "label": "Figure 4",
    "context": "Figure 4: Monetary accommodation premium $\\hat{\\gamma}_A^{(h)}$ : passive vs. active monetary policy episodes Notes: Estimated accommodation premium $\\hat{\\gamma}_{A}^{(h)}$ from equation (10) at each horizon $h = 0, \\ldots, 23$ m"
  },
  {
    "figure_id": "F104",
    "report_id": "R011",
    "label": "Figure 5",
    "context": "Figure 5: State-dependent effects of fiscal risk shocks: high vs. low CDS environment (p90 vs. p10) Notes: Impulse response functions from equation (11), scaled by $(z_{90}-z_{10})$ to represent the difference in macro-financial t"
  },
  {
    "figure_id": "F105",
    "report_id": "R011",
    "label": "Figure 3",
    "context": "As an alternative to the two-stage procedure in equation (3), the impulse responses can be recovered using a direct (one-step) estimator in which $s_{i,t}$ itself is the regressor, bypassing the explicit first-stage regression. The LP is estimated at each hori"
  },
  {
    "figure_id": "F106",
    "report_id": "R011",
    "label": "Figure 3",
    "context": "## F.4 Sampling Uncertainty versus Shock Estimation Uncertainty Following Cieslak and Pang (2021), we distinguish between two conceptually distinct sources of uncertainty in the reported impulse responses. Sampling uncertainty arises from finite-sample variati"
  },
  {
    "figure_id": "F107",
    "report_id": "R011",
    "label": "Figure 3",
    "context": "We apply an analogous decomposition here by generating $N_{sim}$ alternative shock series consistent with the identifying restrictions via Monte Carlo simulation, and re-estimating equation (3) for each simulated draw. The resulting simulation envelope—shown i"
  },
  {
    "figure_id": "F108",
    "report_id": "R011",
    "label": "Figure 3",
    "context": "Notes: Impulse response functions using a direct (one-step) IV estimator with alternative shock measures. Baseline shock measure is in solid blue line; with three alternative measures in dashed lines. Red dashed line shows shock series from BVAR augmented with"
  },
  {
    "figure_id": "F109",
    "report_id": "R011",
    "label": "Figure 3",
    "context": "Here $\\delta^{(h)}$ captures the baseline 2SLS response on negative-shock episodes ( $D_{i,t}^{+}=0$ ), and $\\hat{\\gamma}^{(h)}$ is the asymmetry differential: the additional marginal response on positive-shock episodes relative to negative ones following a 1-"
  },
  {
    "figure_id": "F110",
    "report_id": "R011",
    "label": "Figure 4",
    "context": "so that passive monetary policy is declared when the shock is positive and real rates remain negative for at least six of the eight months following the shock, indicating a sustained accommodative stance. $^{28}$ Results are shown in Figure H.1, with results s"
  },
  {
    "figure_id": "F111",
    "report_id": "R012",
    "label": "Figure 1",
    "context": "Figure 2: Response of key variables to a monetary policy shock, using asymmetric shocks. Note: The shaded area shows the 90% confidence intervals. The responses are in %; the size of the monetary policy shock is one standard devia"
  },
  {
    "figure_id": "F112",
    "report_id": "R012",
    "label": "Figure 1",
    "context": "Figure 2: Response of key variables to a monetary policy shock, using asymmetric shocks. Note: The shaded area shows the 90% confidence intervals. The responses are in %; the size of the monetary policy shock is one standard devia"
  },
  {
    "figure_id": "F113",
    "report_id": "R012",
    "label": "Figure 2",
    "context": "Figure 3: Euro area government debt residual maturity, by select maturity bins, relative to the size of GDP. Note: The line denotes the median, the box the interquartile range, and the whiskers the 25th (75th) percentiles minus (p"
  },
  {
    "figure_id": "F114",
    "report_id": "R012",
    "label": "Figure 3",
    "context": "Figure 3: Euro area government debt residual maturity, by select maturity bins, relative to the size of GDP. Note: The line denotes the median, the box the interquartile range, and the whiskers the 25th (75th) percentiles minus (p"
  },
  {
    "figure_id": "F115",
    "report_id": "R012",
    "label": "Figure 3",
    "context": "Figure 3: Euro area government debt residual maturity, by select maturity bins, relative to the size of GDP. Note: The line denotes the median, the box the interquartile range, and the whiskers the 25th (75th) percentiles minus (p"
  },
  {
    "figure_id": "F116",
    "report_id": "R012",
    "label": "Figure 5",
    "context": "Figure 6: Maturity structures of two countries with similar debt-to-GDP levels at the end of 2019. Note: Debt levels for each country are between 97 and 98% of GDP."
  },
  {
    "figure_id": "F117",
    "report_id": "R012",
    "label": "Figure 5",
    "context": "Figure 6: Maturity structures of two countries with similar debt-to-GDP levels at the end of 2019. Note: Debt levels for each country are between 97 and 98% of GDP. To what extent do these effects arise merely due to elevated sove"
  },
  {
    "figure_id": "F118",
    "report_id": "R012",
    "label": "Figure 6",
    "context": "Figure 6: Maturity structures of two countries with similar debt-to-GDP levels at the end of 2019. Note: Debt levels for each country are between 97 and 98% of GDP. To what extent do these effects arise merely due to elevated sove"
  },
  {
    "figure_id": "F119",
    "report_id": "R012",
    "label": "Figure 7",
    "context": "In particular, we exclude the quarters identified in Johns et al. (2026) as corresponding to high sovereign risk in the respective euro area economies, where the level of sovereign CDS spreads was at the highest quartile of the panel distribution. Figure 8 sho"
  },
  {
    "figure_id": "F120",
    "report_id": "R012",
    "label": "Figure 8",
    "context": "## 3.3 Fiscal response The effects of the monetary policy shock and the associated income and valuation effects are likely to also depend on the response of the fiscal authority. For example, in response to a monetary tightening, any decline in current or expe"
  },
  {
    "figure_id": "F121",
    "report_id": "R012",
    "label": "Figure 9",
    "context": "The lower of panel of Figure 10 plots the responses of primary balances and government debt, respectively, to monetary policy shocks. It shows that, over the sample period, fiscal balances have deteriorated in response to contractionary monetary policy shocks."
  },
  {
    "figure_id": "F122",
    "report_id": "R012",
    "label": "Figure 9",
    "context": "The lower of panel of Figure 10 plots the responses of primary balances and government debt, respectively, to monetary policy shocks. It shows that, over the sample period, fiscal balances have deteriorated in response to contractionary monetary policy shocks."
  },
  {
    "figure_id": "F123",
    "report_id": "R012",
    "label": "Figure 10",
    "context": "The lower of panel of Figure 10 plots the responses of primary balances and government debt, respectively, to monetary policy shocks. It shows that, over the sample period, fiscal balances have deteriorated in response to contractionary monetary policy shocks."
  },
  {
    "figure_id": "F124",
    "report_id": "R012",
    "label": "Figure 10",
    "context": "These results indicate that fiscal policy has generally not provided backing to monetary policy over the sample - as monetary policy has tightened, fiscal policy has become looser, with primary balances declining and government debt rising. These dynamics coul"
  },
  {
    "figure_id": "F125",
    "report_id": "R012",
    "label": "Figure 10",
    "context": "strength of monetary transmission. The upper panel of Figure 10 plots the responses of 10-year government bond yields and the corresponding bond returns, respectively, to the monetary policy shocks. We consider the expected changes in these variables, as they "
  },
  {
    "figure_id": "F126",
    "report_id": "R012",
    "label": "Figure 10",
    "context": "The upper panel of Figure 10 plots the responses of 10-year government bond yields and the corresponding bond returns, respectively, to the monetary policy shocks. We consider the expected changes in these variables, as they could be important in driving the r"
  },
  {
    "figure_id": "F127",
    "report_id": "R012",
    "label": "Figure 11",
    "context": "Expected long-term bond return (%) Primary Balance (% GDP) Debt (% GDP)"
  },
  {
    "figure_id": "F128",
    "report_id": "R012",
    "label": "Figure 11",
    "context": "Primary Balance (% GDP) Debt (% GDP) Figure 11 shows corresponding evidence for monetary contractions and expansions, respectively. As in the case of symmetric shocks, fiscal balances deteriorate in response to contractionary monetary policy shocks, the expect"
  },
  {
    "figure_id": "F129",
    "report_id": "R012",
    "label": "Figure 11",
    "context": "Primary Balance (% GDP) Debt (% GDP) Figure 11 shows corresponding evidence for monetary contractions and expansions, respectively. As in the case of symmetric shocks, fiscal balances deteriorate in response to contractionary monetary policy shocks, the expect"
  },
  {
    "figure_id": "F130",
    "report_id": "R012",
    "label": "Figure 11",
    "context": "Primary Balance (% GDP) Debt (% GDP) Figure 11 shows corresponding evidence for monetary contractions and expansions, respectively. As in the case of symmetric shocks, fiscal balances deteriorate in response to contractionary monetary policy shocks, the expect"
  },
  {
    "figure_id": "F131",
    "report_id": "R012",
    "label": "Figure 12",
    "context": "Figure 12: Average maturity of total debt vs. debt held by private sector Given the data available to us, we address this issue by comparing the transmission of monetary policy shocks conditional on the weighted average maturity (W"
  },
  {
    "figure_id": "F132",
    "report_id": "R012",
    "label": "Figure 12",
    "context": "Figure 13: Monetary policy effectiveness and weighted average maturity of total vs privately-held public debt. Note: Maturities are divided into four quartiles based on the distributions of the weighted average maturity. Hollow poi"
  },
  {
    "figure_id": "F133",
    "report_id": "R012",
    "label": "Figure 12",
    "context": "Figure 13: Monetary policy effectiveness and weighted average maturity of total vs privately-held public debt. Note: Maturities are divided into four quartiles based on the distributions of the weighted average maturity. Hollow poi"
  },
  {
    "figure_id": "F134",
    "report_id": "R012",
    "label": "Figure 12",
    "context": "Figure 13: Monetary policy effectiveness and weighted average maturity of total vs privately-held public debt. Note: Maturities are divided into four quartiles based on the distributions of the weighted average maturity. Hollow poi"
  },
  {
    "figure_id": "F135",
    "report_id": "R012",
    "label": "Figure 14",
    "context": "Figure 14: Spillover countries' government debt residual maturity, by select maturity bins, relative to the size of GDP. Note: The line denotes the median, the box the interquartile range, and the whiskers the 25th (75th) percentil"
  },
  {
    "figure_id": "F136",
    "report_id": "R012",
    "label": "Figure 15",
    "context": "Figure 14: Spillover countries' government debt residual maturity, by select maturity bins, relative to the size of GDP. Note: The line denotes the median, the box the interquartile range, and the whiskers the 25th (75th) percentil"
  },
  {
    "figure_id": "F137",
    "report_id": "R012",
    "label": "Figure 14",
    "context": "Figure 14: Spillover countries' government debt residual maturity, by select maturity bins, relative to the size of GDP. Note: The line denotes the median, the box the interquartile range, and the whiskers the 25th (75th) percentil"
  },
  {
    "figure_id": "F138",
    "report_id": "R012",
    "label": "Figure 16",
    "context": "What are the effects of the same shocks on interest rates, the exchange rates and sovereign debt in the non-EA European countries? Figure 16 shows that, in response to a euro area monetary policy tightening, currencies outside the euro area depreciate, policy "
  },
  {
    "figure_id": "F139",
    "report_id": "R014",
    "label": "Exhibit 1",
    "context": "Investors are placing more emphasis on which business models can capture the next wave of value, which technologies can create durable advantage, and how far players can extend into adjacent products, geographies, and infrastructure layers while navigating a m"
  },
  {
    "figure_id": "F140",
    "report_id": "R014",
    "label": "Exhibit 1",
    "context": "There has been a striking reversal of mood within the global fintech sector. Two years ago, the sector was still working through the aftershocks of the 2021 reset, a period during which capital was scarce, valuations compressed sharply, and questions about the"
  },
  {
    "figure_id": "F141",
    "report_id": "R014",
    "label": "Exhibit 2",
    "context": "# Global Fintech Revenues Break Half a Trillion Dollars in 2025 Global fintech revenue by vertical (2021–2025, \\$B) Global fintech revenue by region (2021–2025, \\$B) Sources: S&P Capital IQ; BCG FinTech Control Tower; BCG Banking and Insurance Revenue Pools; B"
  },
  {
    "figure_id": "F142",
    "report_id": "R014",
    "label": "EXHIBIT 3",
    "context": "Fintechs account for \\~4% of global financial services revenues TOTAL GLOBAL REVENUE, 2025 (\\$) Fintech revenue growth outpaced incumbents across all verticals FINTECH VS. INCUMBENT REVENUE GROWTH YOY, 2024–2025 (%) $^{1}$ Sources: S&P Capital IQ; Pitchbook; B"
  },
  {
    "figure_id": "F143",
    "report_id": "R014",
    "label": "EXHIBIT 3",
    "context": "Sources: S&P Capital IQ; Pitchbook; BCG FinTech Control Tower; BCG Banking and Insurance Revenue Pools; BCG analysis. $^{1}$ Excludes “financial infrastructure,” as the category is not relevant for incumbent financial institutions. ## EXHIBIT 3 Payments Remain"
  },
  {
    "figure_id": "F144",
    "report_id": "R014",
    "label": "Exhibit 5",
    "context": "Since GCash's explosive growth starting in 2015, the financially excluded population in the Philippines declined from \\~70% to \\~20% Brazil Kenya Philippines Sources: World Bank; UN World Population Prospects; Kenya National Bureau of Statistics; Central Bank "
  },
  {
    "figure_id": "F145",
    "report_id": "R014",
    "label": "Exhibit 5",
    "context": "Brazil Kenya Philippines Sources: World Bank; UN World Population Prospects; Kenya National Bureau of Statistics; Central Bank of Kenya; Safaricom Reports; Philippine Statistics Authority, Bangko Sentral ng Pilipinas FIS, Globe Telecom/Mynt/Gcash Reports; BCG "
  },
  {
    "figure_id": "F146",
    "report_id": "R014",
    "label": "Exhibit 6",
    "context": "Maturation is also evident in where capital is going. Equity funding rose 53% to \\$58 billion in 2025, but funding growth was not evenly distributed. (See Exhibit 6.) Trading and investment fintechs captured roughly one-third of all funding, up from about one-"
  },
  {
    "figure_id": "F147",
    "report_id": "R014",
    "label": "EXHIBIT 6",
    "context": "AVERAGE EBITDA MARGIN (%) SHARE OF FINTECHS ABOVE THE RULE OF $40^{2}$ (\\%) Sources: Financial analysis of the top 85 fintechs, S&P Capital IQ; Pitchbook; BCG FinTech Control Tower; BCG analysis. $^{1}$ Profitability defined as EBITDA or EBT. $^{2}$ Rule of 40"
  },
  {
    "figure_id": "F148",
    "report_id": "R014",
    "label": "EXHIBIT 6",
    "context": "REVENUE MULTIPLE FOR PUBLIC FINTECHS ## EXHIBIT 6 Equity Funding and IPO Activity Have Accelerated, While Valuations Have Grown Moderately FINTECH EQUITY FINANCING (\\$B) 2025 funding rebound has continued into 2026, with Q1 equity funding reaching \\$14.8B, sur"
  },
  {
    "figure_id": "F149",
    "report_id": "R014",
    "label": "EXHIBIT 7",
    "context": "GS Growth Equity ## EXHIBIT 7 AI Is More Than a Tool Upgrade, It Is an Organizational Transformation In a digitally enhanced model, people are the core drivers, with AI tools to boost efficiency Core processes built around people Supplemented by digital tools "
  },
  {
    "figure_id": "F150",
    "report_id": "R014",
    "label": "Exhibit 8",
    "context": "While many of the narratives around consumer-facing autonomous agents still feel premature, some do present glimpses of a potential agentic future. A few AI-native fintechs at the bleeding edge of agentic AI adoption have incorporated agentic AI into everythin"
  },
  {
    "figure_id": "F151",
    "report_id": "R014",
    "label": "EXHIBIT 9",
    "context": "How far can fintech penetrate B2B, and what it will take to win? The answer will depend as much on trust as on product quality. To displace entrenched systems, fintechs must convince clients that the operational risk and complexity of unwinding existing workfl"
  },
  {
    "figure_id": "F152",
    "report_id": "R014",
    "label": "Exhibit 10",
    "context": "We believe that autonomous agentic commerce has a reasonably long path to scale, and may only get there in certain cases. The reasons exist on both the demand side and the supply side. On the former, consumers are more likely to adopt agents where they create "
  },
  {
    "figure_id": "F153",
    "report_id": "R014",
    "label": "Exhibit 11",
    "context": "Trust is a foundational issue across all of these categories, not an isolated problem in any one vertical. Consumers need confidence that the agent is acting within clear boundaries, that mistakes can be corrected easily, and that the downside of delegation is"
  },
  {
    "figure_id": "F154",
    "report_id": "R014",
    "label": "Exhibit 12",
    "context": "# Google Staking a Position in Agentic Commerce The next phase of fintech will not be confined to fintechs themselves. As AI changes how consumers discover, compare, and buy, Google is moving to defend discovery—but its response goes beyond preserving search t"
  },
  {
    "figure_id": "F155",
    "report_id": "R014",
    "label": "EXHIBIT 12",
    "context": "## EXHIBIT 12 # About 7,000 Fintechs Are Building the Digital Asset Ecosystem and Comprise an Increasing Share of Fintech Equity Funding and Revenue SHARE OF ACTIVE FINTECHS, BY DIGITAL ASSETS (COMPANY COUNT) Sources: S&P Capital IQ; Pitchbook; BCG FinTech Con"
  },
  {
    "figure_id": "F156",
    "report_id": "R014",
    "label": "EXHIBIT 14",
    "context": "Sources: BCG FinTech Control Tower. $^{1}$ Cumulative number of digital asset fintech and equity funding attracted from 2000 to 2025 inclusive. ## EXHIBIT 14 ## The Asset Tokenization Flywheel Is Starting to Spin Sources: RWA.xyz; BCG analysis. Note: CBDC = ce"
  },
  {
    "figure_id": "F157",
    "report_id": "R014",
    "label": "EXHIBIT 16",
    "context": "## EXHIBIT 16 Federal Bank Charters and Depository Institution Applications Increased Over 5x from 2024 to 2025 Federal bank charter and new-bank application volume $^{1}$ (2021–2026 Q1) Sources: OCC; FDIC. $^{1}$ Includes OCC national bank / national trust ch"
  },
  {
    "figure_id": "F158",
    "report_id": "R014",
    "label": "Exhibit 18",
    "context": "Despite continued public-market volatility and investor selectivity, IPO and M&A activity are likely to continue at their current levels. Scaled fintechs still need paths to liquidity, and strategic urgency across the sector remains high. But the composition o"
  },
  {
    "figure_id": "F159",
    "report_id": "R014",
    "label": "EXHIBIT 18",
    "context": "## EXHIBIT 18 2025 Saw the Highest Number of M&A Deals and Second-Highest Amount; Scaled Fintechs Were the Most Active Acquirers Scaled fintechs were the most active acquirers in 2025 (COUNT BY ACQUIRER TYPE $^{1}$ ) $^{1}$ Analysis by acquirer type only inclu"
  },
  {
    "figure_id": "F160",
    "report_id": "R015",
    "label": "Exhibit 1",
    "context": "The primary engine of value creation over the 2021–2025 period remains growth in tangible book value (TBV), the result of strong underwriting income. (See Exhibit 1.) Cash flow contribution (dividends and buybacks) remains the second major lever, while multipl"
  },
  {
    "figure_id": "F161",
    "report_id": "R015",
    "label": "EXHIBIT 2",
    "context": "Top quartile ## EXHIBIT 2 Underwriting Results Drove Performance of Top-Quartile Companies CONTRIBUTION TO RETURN ON TANGIBLE EQUITY, 2021–2025 (PP) Sources: S&P Capital IQ; BCG ValueScience Center; BCG analysis. Note: PP = percentage points; RoTE = return on "
  },
  {
    "figure_id": "F162",
    "report_id": "R015",
    "label": "Exhibit 3",
    "context": "Sources: S&P Capital IQ; BCG ValueScience Center; BCG analysis. Note: PP = percentage points; RoTE = return on tangible equity. RoTE is calculated as pretax operating income gross of interest expenses, as a percentage of year-end tangible book value of equity "
  },
  {
    "figure_id": "F163",
    "report_id": "R015",
    "label": "Exhibit 4",
    "context": "The subsegments of US P&C performed similarly from 2021 through 2025, with TSRs of 17% and 18% for personal and commercial lines, respectively. Behind these figures, however, are signs of diverging markets. (See Exhibit 4.) Commercial lines benefited from a pr"
  },
  {
    "figure_id": "F164",
    "report_id": "R015",
    "label": "Exhibit 5",
    "context": "Sources: S&P Capital IQ; BCG ValueScience Center; BCG analysis. Note: TSRs are weighted by market cap as of January 1, 2021. P&C = property and casualty; PP = percentage point; P/TBV = price to TBV; TBV = tangible book value; TSR = total shareholder return. $^"
  },
  {
    "figure_id": "F165",
    "report_id": "R016",
    "label": "Exhibit 1",
    "context": "• Use Fit-for-Purpose Technology and Data 17 How to Accelerate AI Value Creation 19 Appendix • AI Definitions • Survey Methodology # Are You Generating Value from AI? How much value is your company generating from your investments in AI? It’s a question more C"
  },
  {
    "figure_id": "F166",
    "report_id": "R016",
    "label": "Exhibit 2",
    "context": "AI-driven value accrues over time, creating a compounding effect. (See Exhibit 2.) Future-built companies that moved early enjoy outsized benefits across financial and operational fronts, and this performance gap is widening. Future-built firms plan to spend 2"
  },
  {
    "figure_id": "F167",
    "report_id": "R016",
    "label": "Exhibit 3",
    "context": "Our research has found that 70% of potential value from AI is concentrated in core business functions such as sales and marketing, manufacturing, supply chain, and pricing. R&D and innovation alone account for 15% of the total potential value. This continues a"
  },
  {
    "figure_id": "F168",
    "report_id": "R016",
    "label": "EXHIBIT 5",
    "context": "Agents do not operate without humans. Their performance depends on strong human orchestration in redesigned roles. The best companies reconfigure workflows to combine autonomous agents with human oversight, maximizing value and adoption. ## EXHIBIT 5 ## Value "
  },
  {
    "figure_id": "F169",
    "report_id": "R016",
    "label": "Exhibit 6",
    "context": "...Thanks to budget allocation 30% Of companies are spending over 15% of their AI budget on agents Top 5 functions prioritized for agentic AI usage $(\\%)^{2}$ Note: Because of rounding, not all bar segment totals equal 100%. # What Value Generators Do Differen"
  },
  {
    "figure_id": "F170",
    "report_id": "R016",
    "label": "Exhibit 6",
    "context": "Of companies are spending over 15% of their AI budget on agents Top 5 functions prioritized for agentic AI usage $(\\%)^{2}$ Note: Because of rounding, not all bar segment totals equal 100%. # What Value Generators Do Differently Our research shows that regardl"
  },
  {
    "figure_id": "F171",
    "report_id": "R016",
    "label": "EXHIBIT 6",
    "context": "## Pursue a Multiyear Strategic AI Ambition Future-built companies approach AI as board- and CEO-sponsored programs, thereby elevating the agenda above isolated experiments or pilots. Top management translates overall business goals into a multiyear, fully fun"
  },
  {
    "figure_id": "F172",
    "report_id": "R016",
    "label": "EXHIBIT 8",
    "context": "Future-built companies understand the need to move fast, but they are equally attentive to evolving their operating model over time along multiple dimensions. An effective AI operating model does not focus on replacing people with technology; it entails reimag"
  },
  {
    "figure_id": "F173",
    "report_id": "R016",
    "label": "EXHIBIT 8",
    "context": "## EXHIBIT 8 Efficient Prioritization Enables Future-Built Companies to Deploy and Scale More Workflows Faster Future-built companies have over 5x the AI workflows in deployment (\\%)... ... and are up to 2x faster Average number of months required to fully dep"
  },
  {
    "figure_id": "F174",
    "report_id": "R016",
    "label": "Exhibit 9",
    "context": "Clear principles guide the hybrid portfolio strategy. Smart companies focus on core enablers such as data readiness and internal skills—platform-agnostic investments that deliver sustained value. It is also essential to treat the ownership of models and prompt"
  },
  {
    "figure_id": "F175",
    "report_id": "R016",
    "label": "Exhibit 10",
    "context": "(See Exhibit 10.) Our research shows that most roadblocks involve people, organization, and processes. In 2024, companies struggled with aligning AI to the overall strategy and establishing a business case, but now the priority has shifted to more concrete imp"
  },
  {
    "figure_id": "F176",
    "report_id": "R016",
    "label": "EXHIBIT 10",
    "context": "Future-built ## EXHIBIT 10 ## Most AI Roadblocks Involve People, Organization, and Processes BCG's 10-20-70 model Key challenges named by respondents (%) Significantly higher for laggards versus future-built ## Appendix ## AI Definitions"
  },
  {
    "figure_id": "F177",
    "report_id": "R017",
    "label": "Exhibit 1",
    "context": "10 Platform Evolution: From Console Wars to Cloud Wars 13 UGC: Welcome to the New Creator Economy 16 App Stores Opening Up: A Revolution for Distribution 19 Improving Monetization: The New Math of Game Pricing 23 Growth Through Disruption 24 About the Global G"
  },
  {
    "figure_id": "F178",
    "report_id": "R017",
    "label": "Exhibit 2",
    "context": "One ground for optimism is that gamers remain passionate about gaming. Around 55% of gamers in our survey have increased their gaming time over the past six months. In addition, gaming parents told us they are introducing the children to the activity early, cr"
  },
  {
    "figure_id": "F179",
    "report_id": "R017",
    "label": "Exhibit 3",
    "context": "Almost Half of All Gamer Parents' Kids Start Playing Video Games by Age 5, and Two of Their Most Common First Games Contain UGC Today, more than 50% of respondents' children began their digital journey by age 5, and about 77% began playing video games by age 7"
  },
  {
    "figure_id": "F180",
    "report_id": "R017",
    "label": "Exhibit 3",
    "context": "Q: How old was your child when they had their first digital experience? (%) Q: How old was your child when they first started playing video games? (%) Two of the three most popular first games for kids are UGC games: Minecraft and Roblox Q: What was the first "
  },
  {
    "figure_id": "F181",
    "report_id": "R017",
    "label": "EXHIBIT 3",
    "context": "## EXHIBIT 3 Adults Are Driving Growth at Both Ends by Introducing the Next Generation to Gaming and Remaining Engaged Well into Retirement Most children are introduced to gaming by their parents, making adults the primary onboarding channel Q: How was your ch"
  },
  {
    "figure_id": "F182",
    "report_id": "R017",
    "label": "EXHIBIT 4",
    "context": "Q: How was your child first introduced to video games? (%) Sources: BCG Global Gaming Survey (N = 2,972); BCG analysis. Note: Because of rounding not all bar chart totals add up to 100%. Boomers continue gaming into retirement, signaling long-term engagement Q"
  },
  {
    "figure_id": "F183",
    "report_id": "R017",
    "label": "EXHIBIT 4",
    "context": "## EXHIBIT 4 # Younger Gamers Prefer Consoles, Particularly PlayStation and Switch, While Gen X and Boomers Spend More Time Gaming on Mobile ## RESPONDENT'S PRIMARY GAMING PLATFORM, BY GENERATION (%) \\- Console gamers tend to be younger, as consoles—Xbox, Swit"
  },
  {
    "figure_id": "F184",
    "report_id": "R017",
    "label": "EXHIBIT 5",
    "context": "Players, however, are generally not concerned. In our Global Gaming Survey, the most significant point of resistance involved adult gamers reacting to AI for generating art/animation; but even there, only 10% had a negative view. Likewise, just 7% of adult gam"
  },
  {
    "figure_id": "F185",
    "report_id": "R017",
    "label": "EXHIBIT 5",
    "context": "## EXHIBIT 5 ## GenAI Is Becoming More Common in Game Development ## Approximately one-fifth of titles released in Q3 2025 disclosed AI integration The top three genres disclosing AI use are casual (20%), adventure (16%), and action (14%) Note: NPC = nonplayer"
  },
  {
    "figure_id": "F186",
    "report_id": "R017",
    "label": "EXHIBIT 6",
    "context": "## Approximately one-fifth of titles released in Q3 2025 disclosed AI integration The top three genres disclosing AI use are casual (20%), adventure (16%), and action (14%) Note: NPC = nonplayer character. Asset creation is the main use; narrative, audio, and "
  },
  {
    "figure_id": "F187",
    "report_id": "R017",
    "label": "EXHIBIT 6",
    "context": "The top three genres disclosing AI use are casual (20%), adventure (16%), and action (14%) Note: NPC = nonplayer character. Asset creation is the main use; narrative, audio, and user experience are secondary ## EXHIBIT 6 ## How GenAI Is Changing the Games Indu"
  },
  {
    "figure_id": "F188",
    "report_id": "R017",
    "label": "EXHIBIT 6",
    "context": "Asset creation is the main use; narrative, audio, and user experience are secondary ## EXHIBIT 6 ## How GenAI Is Changing the Games Industry ## Driving efficiency Modl.AI and Mighty Build & Test are complementary AI platforms that automate QA, representing the"
  },
  {
    "figure_id": "F189",
    "report_id": "R017",
    "label": "Exhibit 7",
    "context": "Significantly, the gamers in our survey were reacting to features they have not yet experienced. A tsunami of low-grade AI-created games could quickly sour their views. Data from our survey of developers reveals that some are moving fast while many others are "
  },
  {
    "figure_id": "F190",
    "report_id": "R017",
    "label": "EXHIBIT 9",
    "context": "of gamers who tried it reported an overall positive experience However, gamers who use cloud gaming also play on other platforms HOW CLOUD GAMERS APPORTION THEIR GAMING TIME (%) TIME DEVOTED TO CLOUD GAMING (%) Sources: BCG Global Gaming Survey (N = 2,972); BC"
  },
  {
    "figure_id": "F191",
    "report_id": "R017",
    "label": "EXHIBIT 9",
    "context": "Sources: BCG Global Gaming Survey (N = 2,972); BCG analysis. ## EXHIBIT 9 Cloud Gaming Is Ready for Liftoff as the Gaming Experience Improves CLOUD GAMING USERS (MILLIONS) Note: CAGR = compound annual growth rate. CLOUD GAMING MARKET (\\$BILLIONS) ## Seizing th"
  },
  {
    "figure_id": "F192",
    "report_id": "R017",
    "label": "EXHIBIT 10",
    "context": "## EXHIBIT 10 ## Gamers Are Interacting With UGC, but Creators Are Still a Minority More than 40% of gamers are consuming more UGC than they did a year ago... Q: Select how much you agree/disagree with the following statement: I consume more UGC now than I did"
  },
  {
    "figure_id": "F193",
    "report_id": "R017",
    "label": "EXHIBIT 11",
    "context": "Developers that want to harness UGC's power should prioritize building an ecosystem that fits the game and offers the right incentives. ## EXHIBIT 11 Gen Z and Millennials Are Interacting More With UGC; Older Gamers Show Potential Q: Select all the ways you ha"
  },
  {
    "figure_id": "F194",
    "report_id": "R017",
    "label": "Exhibit 13",
    "context": "In addition paying lower fees, developers will gain a range of opportunities through new distribution channels, including the ability to build cross-platform ecosystems that were impossible just a few years ago, deepening player engagement without the need to "
  },
  {
    "figure_id": "F195",
    "report_id": "R017",
    "label": "EXHIBIT 14",
    "context": "## EXHIBIT 14 ## Most Gamers Are Price-Conscious and Are Prepared to Wait for Discounts More than 75% of gamers say prices will heavily impact their purchase choices Q: Please select how much you agree with the following statements: Price significantly influen"
  },
  {
    "figure_id": "F196",
    "report_id": "R017",
    "label": "EXHIBIT 15",
    "context": "Q: Please select how much you agree with the following statements: Price significantly influences my choice of brand/product/service (%) Sources: BCG Global Gaming Survey 2025 (N = 2,972); BCG analysis. About 65% of gamers have tactics to limit their spending "
  },
  {
    "figure_id": "F197",
    "report_id": "R017",
    "label": "EXHIBIT 15",
    "context": "Q: When multiple games in the same franchise are released in the same year, which of the following do you do? (%) ## EXHIBIT 15 Premium Games Are a Good Value, and the Average Launch Price of AAA Games Has Declined When Adjusted for Inflation Consumer cost per"
  },
  {
    "figure_id": "F198",
    "report_id": "R017",
    "label": "EXHIBIT 15",
    "context": "## EXHIBIT 15 Premium Games Are a Good Value, and the Average Launch Price of AAA Games Has Declined When Adjusted for Inflation Consumer cost per hour of entertainment by medium and format for major categories, as of 2025 (\\$) $^{1}$ Sources: BCG GEMS; PQ Med"
  },
  {
    "figure_id": "F199",
    "report_id": "R017",
    "label": "Exhibit 16",
    "context": "## • Alternative monetization will expand rapidly. Many free-to-play games on mobile already deploy these strategies to great effect. As strategies such as in-game transactions and downloadable content increase, the proportion of gamers' spending that goes to "
  },
  {
    "figure_id": "F200",
    "report_id": "R017",
    "label": "EXHIBIT 16",
    "context": "## EXHIBIT 16 Gaming Preferences Reveal Generational Divides in Format and Monetization Models, Including Access-Based Models I prefer live-service games to single-player games (%) I prefer accessing games via subscription over buying individual games (%) \\- I"
  },
  {
    "figure_id": "F201",
    "report_id": "R017",
    "label": "Exhibit 17",
    "context": "Gaming Preferences Reveal Generational Divides in Format and Monetization Models, Including Access-Based Models I prefer live-service games to single-player games (%) I prefer accessing games via subscription over buying individual games (%) \\- In-game adverti"
  },
  {
    "figure_id": "F202",
    "report_id": "R017",
    "label": "Exhibit 17",
    "context": "I prefer live-service games to single-player games (%) I prefer accessing games via subscription over buying individual games (%) \\- In-game advertising will emerge as a stronger revenue stream. Mobile games typically earn 20% of their revenue from advertising"
  },
  {
    "figure_id": "F203",
    "report_id": "R017",
    "label": "EXHIBIT 17",
    "context": "For the money, gaming delivers more value than many other hobbies. This is a sign that the industry needs to work harder on pricing, not just to raise revenue but also to protect the scarcity and visibility that make big games significant events in popular cul"
  },
  {
    "figure_id": "F204",
    "report_id": "R017",
    "label": "Exhibit 18",
    "context": "Gaming accounts for 12.5% of gamers' time spent with media, but only around 3% of media ad spending Sources: BCG GEMS; PQ Media; BCG Global Gaming Survey 2025 (N = 2,972). Around $30\\%$ of gamers wouldn't mind sponsored listings in a games store; hardcore game"
  },
  {
    "figure_id": "F205",
    "report_id": "R017",
    "label": "Exhibit 18",
    "context": "Sources: BCG GEMS; PQ Media; BCG Global Gaming Survey 2025 (N = 2,972). Around $30\\%$ of gamers wouldn't mind sponsored listings in a games store; hardcore gamers are most open to this Q: Agreement with “I don’t mind sponsored listings within my gaming store” "
  },
  {
    "figure_id": "F206",
    "report_id": "R017",
    "label": "EXHIBIT 18",
    "context": "By 2030, we should see an explosion of gaming content, an expansion of the global audience for games, and broadening expectations for omniplatform gaming. We anticipate a healthy, growing market, although there will be on the AAA business model will experience"
  },
  {
    "figure_id": "F207",
    "report_id": "R018",
    "label": "Exhibit 1",
    "context": "Through every chapter of the past 250 years, the United States has harnessed these foundations, not in a fixed economic model but through flexible institutions that have made the next adaptation possible. And it has done so collectively. “We the people”—farmer"
  },
  {
    "figure_id": "F208",
    "report_id": "R018",
    "label": "Exhibit 1",
    "context": "# The United States has cause for celebration. But there are also reasons for reflection. ## Exhibit 1 ## By 1900, the United States had the world's leading economy by size and individual incomes. Real gross domestic product, $^{1}$ 1820–2024, \\$ trillion in 2"
  },
  {
    "figure_id": "F209",
    "report_id": "R018",
    "label": "Exhibit 1",
    "context": "## Exhibit 1 ## By 1900, the United States had the world's leading economy by size and individual incomes. Real gross domestic product, $^{1}$ 1820–2024, \\$ trillion in 2024 Real gross domestic product per capita, $^{2}$ purchasing power parity, 1800–2024 $^{1"
  },
  {
    "figure_id": "F210",
    "report_id": "R018",
    "label": "Exhibit 3",
    "context": "American companies make up more than half of the top 100 firms globally by market capitalization and revenue (Exhibit 3). From start-ups to large corporations, they attract an outsize share of capital from global markets. US firms hold more than half of global"
  },
  {
    "figure_id": "F211",
    "report_id": "R018",
    "label": "Exhibit 4",
    "context": "To be sure, a sizable share of US market capitalization is connected to the technology sector. Yet US firms lead across a range of sectors and are present in the upper echelons of all of them. $^{10}$ US market leadership is not a recent development: The Unite"
  },
  {
    "figure_id": "F212",
    "report_id": "R018",
    "label": "Exhibit 5",
    "context": "McKinsey & Company Fundamentally, US firms' outperformance is rooted in greater dynamism: They exhibit higher rates of labor reallocation, market entry and exit, and growth of young firms. $^{11}$ That dynamism translates to higher national productivity growth"
  },
  {
    "figure_id": "F213",
    "report_id": "R018",
    "label": "Exhibit 6",
    "context": "## The US lead in technology is narrowing as China becomes more competitive. ## Exhibit 6 ## Large US firms lead on investment, outpacing their European counterparts. Capital expenditure and R&D spending of large $^{1}$ US and European $^{2}$ companies, $^{3}$"
  },
  {
    "figure_id": "F214",
    "report_id": "R018",
    "label": "Exhibit 7",
    "context": "This gap in income levels has grown over the past 50 years. Although all income segments have seen real growth, market incomes (wages and asset flows) have grown the most for the top two quintiles. For the bottom 60 percent of the population, more income growt"
  },
  {
    "figure_id": "F215",
    "report_id": "R018",
    "label": "Exhibit 9",
    "context": "McKinsey & Company The United States remains the most competitive economy in the world on a multitude of fronts. Getting to this point has not been a straight path. There were twists and turns, transformations and reinventions. Before contemplating the future,"
  },
  {
    "figure_id": "F216",
    "report_id": "R018",
    "label": "Exhibit 9",
    "context": "# Looking back: Four chapters As we have seen, the United States has been the world's largest economy for more than a century. The rise of American competitiveness did not follow a linear or clear trajectory. Growth and innovation often happened in bursts, aft"
  },
  {
    "figure_id": "F217",
    "report_id": "R018",
    "label": "Exhibit 10",
    "context": "## 1. Agricultural abundance ## American Revolution to the Civil War In its first century-plus, the United States was a predominantly agrarian society. In the South, cotton boomed, making up most of the world market by 1820 and meeting strong demand from the b"
  },
  {
    "figure_id": "F218",
    "report_id": "R018",
    "label": "Exhibit 10",
    "context": "The United States had another natural advantage: navigable waterways. Coastal passages with barrier islands and inland rivers made long-distance shipping efficient. The Mississippi River system alone, made fully accessible by the Louisiana Purchase of 1803, in"
  },
  {
    "figure_id": "F219",
    "report_id": "R018",
    "label": "Exhibit 11",
    "context": "## The Apotheosis of Washington and American innovation circa 1865 The Apotheosis of Washington—a grand fresco depicting George Washington “rising to the heavens in glory” flanked by figures of Liberty and Victory—dominates the US Capitol rotunda ceiling. Comp"
  },
  {
    "figure_id": "F220",
    "report_id": "R018",
    "label": "Exhibit 11",
    "context": "Following the Civil War, the US-led Second Industrial Revolution gained full force, and America emerged as the world's preeminent industrial economy. Society grew more connected, shifting away from its agrarian and relatively isolated beginnings. Agricultural "
  },
  {
    "figure_id": "F221",
    "report_id": "R018",
    "label": "Exhibit 12",
    "context": "By 1832, the United States had more railroad miles than any European country, and by 1870, a larger population. The rapid expansion of railroads was fueled by capital expenditure, which at its height topped 4 percent of GDP annually. This played a critical rol"
  },
  {
    "figure_id": "F222",
    "report_id": "R018",
    "label": "Exhibit 13",
    "context": "Perhaps the single most visible token of US scientific leadership was its rise to dominance in Nobel Prizes. The country surpassed the United Kingdom and Germany in annual science-based prizes in the lead-up to World War II and took the lead on cumulative priz"
  },
  {
    "figure_id": "F223",
    "report_id": "R018",
    "label": "Exhibit 11",
    "context": "## Economic disruptions marked a transition The 1970s saw slowing productivity growth, energy crises, and double-digit rates of inflation. Just as the Great Depression provided a tectonic shift in favor of stronger government involvement, the 1970s economic tu"
  },
  {
    "figure_id": "F224",
    "report_id": "R018",
    "label": "Exhibit 14",
    "context": "Demand for a growing pool of US financial assets grew, attracting capital from a globalizing world. $^{96}$ In the years since 1990, foreign investment in US equities and debt has grown substantially, from the equivalent of 11 percent of GDP in each category t"
  },
  {
    "figure_id": "F225",
    "report_id": "R018",
    "label": "Exhibit 15",
    "context": "Productivity growth has been most concentrated in cities with some of the most flourishing knowledge ecosystems. These “superstar” cities have anchoring sectors and, often, universities. Their productivity has continued to push them ahead of the pack. The thre"
  },
  {
    "figure_id": "F226",
    "report_id": "R018",
    "label": "Exhibit 16",
    "context": "In 1767, Benjamin Franklin wrote: \"America, an immense Territory, favour'd by Nature with all Advantages of Climate, Soil, great navigable Rivers and Lakes, &c. must become a great Country, populous and mighty.\" $^{107}$ He was prescient. Over time, the countr"
  },
  {
    "figure_id": "F227",
    "report_id": "R018",
    "label": "Exhibit 17",
    "context": "Reliable and affordable energy has been an enduring"
  },
  {
    "figure_id": "F228",
    "report_id": "R018",
    "label": "Exhibit 19",
    "context": "The entrepreneurial spirit of the United States was not limited to tech visionaries. It was also embedded in the American people and business community, who have long had the appetite (and means) to adopt and scale new technologies, including those invented el"
  },
  {
    "figure_id": "F229",
    "report_id": "R018",
    "label": "Exhibit 20",
    "context": "## Exhibit 20 Demand for AI fluency and technical AI skills rose between 2023 and 2025. Employees in jobs demanding AI-related skills AI fluency skills, calling for people to use or manage AI Technical AI skills, calling for people to develop or govern AI STEM"
  },
  {
    "figure_id": "F230",
    "report_id": "R018",
    "label": "Exhibit 21",
    "context": "Worker shortages across a range of high- and low-skill occupations are already a concern. Many of the sectors experiencing recent shortages have historically been harder to automate and have seen stubbornly low rates of productivity growth. Healthcare, for exa"
  },
  {
    "figure_id": "F231",
    "report_id": "R018",
    "label": "Exhibit 22",
    "context": "## About half of outstanding Treasuries are set to roll over this year and next. Will demand match supply? ## Exhibit 22 ## US fiscal deficits, including net interest payments, are historically elevated. US federal deficits and defense spending, FY 1975–2035E,"
  },
  {
    "figure_id": "F232",
    "report_id": "R018",
    "label": "Exhibit 23",
    "context": "In the coming era, when technologies such as AI become integral to work and society, power demand is likely to surge further. Growing geopolitical competition also means a likely push to build more domestic manufacturing for critical products like semiconducto"
  },
  {
    "figure_id": "F233",
    "report_id": "R018",
    "label": "Exhibit 24",
    "context": "Geopolitics deepens the conundrum. A total of \\$160 billion of US imports are critical, concentrated, and come from geopolitically distant trading partners (see sidebar “Defining geopolitical distance”). This bull’s-eye of potential exposure may seem small, bu"
  },
  {
    "figure_id": "F234",
    "report_id": "R018",
    "label": "Exhibit 25",
    "context": "By this measure, Europe, Japan, South Korea, and the United States sit near one end of a spectrum, while China and Russia sit closer to the other end (Exhibit 25). Most emerging markets sit somewhere in the middle. Of course, relations between countries are dy"
  },
  {
    "figure_id": "F235",
    "report_id": "R019",
    "label": "Exhibit 1",
    "context": "By contrast, a decline in the importance of software development and other highly specialized technical execution skills reflects that AI systems increasingly take over those tasks. At the same time, skills necessary to guide, interpret, and apply AI outputs a"
  },
  {
    "figure_id": "F236",
    "report_id": "R019",
    "label": "Exhibit 2",
    "context": "## Workforce planning remains predominantly short term and operational On average, 62 percent of HR professionals indicate that their companies conduct organization-wide workforce planning, while 34 percent apply it to at least part of their workforce. However"
  },
  {
    "figure_id": "F237",
    "report_id": "R019",
    "label": "Exhibit 2",
    "context": "## Exhibit 2 Engagement in workforce planning, $^{1}$ % of respondents How far in advance companies typically forecast workforce needs, $^{4}$ % of respondents Note: Figures may not sum to 100%, because of rounding. $^{1}$ Question: Does your company carry out"
  },
  {
    "figure_id": "F238",
    "report_id": "R019",
    "label": "Exhibit 3",
    "context": "Yet among less important drivers, we still observe perception gaps: HR professionals underestimate the importance of relationships with direct managers and colleagues. At the same time, HR professionals overestimate the importance of training and development o"
  },
  {
    "figure_id": "F239",
    "report_id": "R019",
    "label": "Exhibit 4",
    "context": "Generally, recruitment outcomes have improved moderately compared with the previous year. The offer acceptance rate has increased to 59 percent globally from 56 percent last year (Exhibit 4). France records the highest acceptance rate at 71 percent, while Pola"
  },
  {
    "figure_id": "F240",
    "report_id": "R019",
    "label": "Exhibit 6",
    "context": "## Learning participation remains limited and overestimated by HR At a time when skill requirements are changing rapidly, learning activity remains low—and is often overestimated by organizations. Employees report an average of 3.4 training days per year, whil"
  },
  {
    "figure_id": "F241",
    "report_id": "R019",
    "label": "Exhibit 7",
    "context": "Frequency of AI usage also varies substantially. Thirty-six percent of employees in Europe report using AI tools daily or several times per week (up 13 percentage points from last year), compared with 47 percent in the United States (down 17 percentage points)"
  },
  {
    "figure_id": "F242",
    "report_id": "R019",
    "label": "Exhibit 8",
    "context": "In other EX-related findings, on average, 11 percent of working hours (equal to 27 working days) are lost due to absenteeism, down from 15 percent a year earlier. This decline may partly reflect the current macroeconomic environment, as uncertainty may lead em"
  },
  {
    "figure_id": "F243",
    "report_id": "R019",
    "label": "Exhibit 9",
    "context": "— Relationship with colleagues (27 percent, down six percentage points). A sense of belonging and positive team dynamics continue to matter, even though this category ranks below economic and structural factors. ## Exhibit 9 Employees now prioritize remunerati"
  },
  {
    "figure_id": "F244",
    "report_id": "R019",
    "label": "Exhibit 10",
    "context": "Contrary to common generational narratives, remuneration and benefits rank first for all generations; work—life balance and job security follow (Exhibit 10). These three factors clearly dominate retention decisions across age groups. Meaningfulness of work ran"
  },
  {
    "figure_id": "F245",
    "report_id": "R019",
    "label": "Exhibit 11",
    "context": "Seven percent of HR employees believe their job may no longer exist in its current form in the coming years, while 18 percent expect considerable change due to AI (Exhibit 11). Taken together, these figures are slightly above the cross-functional average. ## E"
  },
  {
    "figure_id": "F246",
    "report_id": "R019",
    "label": "Exhibit 12",
    "context": "Adopting agentic AI systems that can autonomously plan, decide, and execute multistep workflows represents the next stage of innovation in HR. But awareness and adoption remain limited. In some European countries, up to one-third of surveyed HR professionals a"
  },
  {
    "figure_id": "F247",
    "report_id": "R021",
    "label": "Exhibit 1",
    "context": "These findings raise questions about how organizations can build a “test, learn, and adapt” mindset and a culture of continuous improvement, and about how leaders redefine roles and responsibilities in a world in which machines can think, orchestrate, decide, "
  },
  {
    "figure_id": "F248",
    "report_id": "R021",
    "label": "Exhibit 2",
    "context": "One way to tackle such concerns is to build a responsive risk framework that proactively addresses both technical and ethical challenges. Winning employees' buy-in is another path to accelerating adoption at scale. This can be done by identifying high-impact A"
  },
  {
    "figure_id": "F249",
    "report_id": "R021",
    "label": "Exhibit 3",
    "context": "## Exhibit 3 A majority of survey respondents agreed that AI capabilities will bring exponential productivity gains. Organizations' desired outcomes of developing an Al-savvy workforce, % of respondents (n = 7,904) Faster and widespread access to information"
  },
  {
    "figure_id": "F250",
    "report_id": "R021",
    "label": "Exhibit 3",
    "context": "Faster and widespread access to information Note: Respondents were asked to identify their desired outcomes in developing an Al-savvy workforce. ## Benefits of getting it right Leaders see multiple and significant benefits from successfully developing an AI-sa"
  },
  {
    "figure_id": "F251",
    "report_id": "R021",
    "label": "Exhibit 3",
    "context": "Faster and widespread access to information Note: Respondents were asked to identify their desired outcomes in developing an Al-savvy workforce. ## Benefits of getting it right Leaders see multiple and significant benefits from successfully developing an AI-sa"
  },
  {
    "figure_id": "F252",
    "report_id": "R021",
    "label": "Exhibit 6",
    "context": "Finally, regulatory and geopolitical complexities can impede progress. As AI-native GBS drives cross-border data flows, companies need to navigate data privacy, local AI regulations, and geopolitical risk. These factors now shape GBS footprint strategy, determ"
  },
  {
    "figure_id": "F253",
    "report_id": "R021",
    "label": "Exhibit 8",
    "context": "This obstacle is more pronounced in North America (32 percent) and Europe (29 percent) than in the Asia-Pacific region (23 percent). Cultural resistance hits hardest where energy runs low: 45 percent of employees in fatigued organizations see it as a barrier, "
  },
  {
    "figure_id": "F254",
    "report_id": "R021",
    "label": "Exhibit 9",
    "context": "When it comes to workflow redesign, our surveys suggest that resource allocation is often neglected. While a lack of resources and insufficient investment in change are sometimes cited as obstacles to process optimization, the respondents to our survey downpla"
  },
  {
    "figure_id": "F255",
    "report_id": "R021",
    "label": "Exhibit 10",
    "context": "Longer-term impact can be achieved by prioritizing workflows with the highest strategic impact. For example, for product development, this can entail better product–market fit, faster launch cycles, and an optimized innovation pipeline. For integrated planning"
  },
  {
    "figure_id": "F256",
    "report_id": "R021",
    "label": "Exhibit 11",
    "context": "Effective portfolio management requires frequent divestitures of underperforming businesses. Organizations can free up capacity to take bold bets by shedding areas where they are no longer the best owner or letting go of activities that are no longer core to s"
  },
  {
    "figure_id": "F257",
    "report_id": "R021",
    "label": "Exhibit 11",
    "context": "Exhibit 11 The majority of survey respondents, particularly executives, said they are clear about their organization's must-win battles. Organizations' visibility on must-win battles, % of respondents (n = 10,018) McKinsey & Company Organizations that make por"
  },
  {
    "figure_id": "F258",
    "report_id": "R021",
    "label": "Exhibit 12",
    "context": "The priorities can be new geographic markets, products and services, innovation, customer engagement, or price positioning. Leaders then need to ensure that resources are reallocated decisively and identify low-impact and noncore activities for divestment to f"
  },
  {
    "figure_id": "F259",
    "report_id": "R021",
    "label": "Exhibit 13",
    "context": "Build a culture that puts equal weight on employee performance and well-being The goal here is to ensure employees feel energized rather than contained. High performers who sustain their performance over time are driven by purpose, adaptability, and recovery r"
  },
  {
    "figure_id": "F260",
    "report_id": "R021",
    "label": "Exhibit 14",
    "context": "There are stakeholder benefits, too, including for customers and investors. One in four organizations (24 percent) report that prioritizing D&I initiatives leads to broader customer and market appeal, while 31 percent say these initiatives enhance corporate re"
  },
  {
    "figure_id": "F261",
    "report_id": "R021",
    "label": "Exhibit 15",
    "context": "Specifically, reflective leaders are more attuned to external forces and feel stronger performance pressure. More than one in five (22 percent) say that geopolitical shifts are significantly affecting their organizations, compared with 10 percent of leaders wh"
  },
  {
    "figure_id": "F262",
    "report_id": "R022",
    "label": "Exhibit 1",
    "context": "The survey findings also shed light on how organizations are structuring their AI deployment efforts. Some essential elements for deploying AI tend to be fully or partially centralized (Exhibit 1). For risk and compliance, as well as data governance, organizat"
  },
  {
    "figure_id": "F263",
    "report_id": "R022",
    "label": "Exhibit 2",
    "context": "Organizations have employees overseeing the quality of gen AI outputs, though the extent of that oversight varies widely. Twenty-seven percent of respondents whose organizations use gen AI say that employees review all content created by gen AI before it is us"
  },
  {
    "figure_id": "F264",
    "report_id": "R022",
    "label": "Exhibit 3",
    "context": "## Exhibit 3 Respondents report increasing mitigation of inaccuracy, intellectual property infringement, and privacy risks related to use of gen AI. Gen-AI-related risks that organizations are working to mitigate, $^{1}$ % of respondents Intellectual property "
  },
  {
    "figure_id": "F265",
    "report_id": "R022",
    "label": "Exhibit 5",
    "context": "Respondents continue to see these roles as largely challenging to fill, though a smaller share of respondents than in the past two years describe hiring for many roles as “difficult” or “very difficult” (Exhibit 5). One exception is AI data scientists, who wil"
  },
  {
    "figure_id": "F266",
    "report_id": "R022",
    "label": "Exhibit 6",
    "context": "Many respondents also say that their organizations have reskilled portions of their workforces as part of their AI deployment over the past year and that they expect to undertake more reskilling in the years ahead (Exhibit 6). Our latest survey also shows how "
  },
  {
    "figure_id": "F267",
    "report_id": "R022",
    "label": "Exhibit 7",
    "context": "Looking at the expected effects of gen AI deployment by business function, respondents most often predict decreasing head count in service operations, such as customer care and field services, as well as in supply chain and inventory management (Exhibit 7). In"
  },
  {
    "figure_id": "F268",
    "report_id": "R022",
    "label": "Exhibit 9",
    "context": "Organizations are also using AI in more business functions than in the previous State of AI survey. For the first time, most survey respondents report the use of AI in more than one business function (Exhibit 9). Responses show organizations using AI in an ave"
  },
  {
    "figure_id": "F269",
    "report_id": "R022",
    "label": "Exhibit 10",
    "context": "While organizations in all sectors are most likely to use gen AI in marketing and sales, deployment within other functions varies greatly according to industry (Exhibit 10). Organizations are applying the technology where it can generate the most value—for exa"
  },
  {
    "figure_id": "F270",
    "report_id": "R022",
    "label": "Exhibit 11",
    "context": "Note: Figures may not sum to 100%, because of rounding. # More than one-third of respondents say their organizations use gen AI to create images, and more than one-quarter use it to create computer code. Most respondents reporting use of gen AI—63 percent—say "
  },
  {
    "figure_id": "F271",
    "report_id": "R022",
    "label": "Exhibit 11",
    "context": "Note: Figures may not sum to 100%, because of rounding. # More than one-third of respondents say their organizations use gen AI to create images, and more than one-quarter use it to create computer code. Most respondents reporting use of gen AI—63 percent—say "
  },
  {
    "figure_id": "F272",
    "report_id": "R022",
    "label": "Exhibit 11",
    "context": "Most respondents reporting use of gen AI—63 percent—say that their organizations are using gen AI to create text outputs, but organizations are also experimenting with other modalities. More than one-third of respondents say their organizations are generating "
  },
  {
    "figure_id": "F273",
    "report_id": "R022",
    "label": "Exhibit 12",
    "context": "An increasing share of respondents report value creation within the business units using gen AI. Compared with early 2024, larger shares of respondents say that their organizations' gen AI use cases have increased revenue within the business units deploying th"
  },
  {
    "figure_id": "F274",
    "report_id": "R022",
    "label": "Exhibit 12",
    "context": "Exhibit 12 Organizations increasingly see gen AI's effects on revenues in the business units using the technology. Revenue increase within business units from gen AI use, past 12 months, by function, $^{1}$ % of respondents $^{1}$ Questions were asked only of "
  },
  {
    "figure_id": "F275",
    "report_id": "R022",
    "label": "Exhibit 13",
    "context": "McKinsey & Company Overall, respondents are also more likely than in the previous survey to say they are seeing meaningful cost reductions within the business units using gen AI (Exhibit 13). In early 2024, among respondents reporting use of gen AI in specific"
  },
  {
    "figure_id": "F276",
    "report_id": "R022",
    "label": "Exhibit 13",
    "context": "Overall, respondents are also more likely than in the previous survey to say they are seeing meaningful cost reductions within the business units using gen AI (Exhibit 13). In early 2024, among respondents reporting use of gen AI in specific business functions"
  }
]