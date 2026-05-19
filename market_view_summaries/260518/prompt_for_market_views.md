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
    "title": "韩国设备进口数据揭示的真正信号：HBM和1c节点正在重塑半导体设备的需求结构",
    "digest": "[wechat_article.md]\n# 韩国设备进口数据揭示的真正信号：HBM和1c节点正在重塑半导体设备的需求结构\n\n市场对半导体周期的讨论，大多还停留在“库存消化”和“AI算力拉动”的叙事框架里。但这份关于韩国半导体设备进口的最新追踪数据，给出了一个更具结构性的信号：真正驱动设备支出的，不是笼统的AI需求，而是韩国存储器双雄在HBM和1c DRAM节点上已然展开的、不可逆的产能竞赛。\n\n2026年4月，韩国半导体设备进口总额同比增长57%，达到34.5亿美元，创下历史新高。尽管环比下降9%，但3个月移动平均仍在环比上升。更值得关注的是，来自荷兰的光刻设备进口虽然环比回落28%，却仍是历史上第二高的季度首月数据。这些数字背后，不是简单的周期回暖，而是存储器市场供给格局的一次重新定价。\n\n这份来自某外资投行的研报，通过跟踪韩国海关的月度设备进口数据，建立了一个独特的“前置指标”体系。它比公司财报更早、更细粒度地揭示了三星和SK海力士的真实资本开支节奏。对于关注ASML、东京电子、爱德万测试以及存储器双雄的投资者来说，这份数据的指向性非常明确。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 设备进口与资本开支的背离，恰恰确认了存储器厂商的“激进”姿态\n\n一个看似矛盾的信号出现在第一季度：尽管设备进口数据在高位运行，三星和SK海力士的合并资本开支却环比下降。研报分析指出，这并非需求减弱，而是2025年第四季度部分基础设施投资被前置的结果。两家公司均已明确指引2026年资本开支将大幅增长，且重点投向基础设施和战略设备。\n\n这意味着，当前设备进口数据反映的更多是“安装”而非“采购”的节奏。设备到厂、安装、调试的周期往往滞后于订单。第一季度资本开支的回落，更像是季度间的正常波动，而非趋势反转。研报的结论是明确的：未来资本开支将恢复增长，甚至可能比进口数据所暗\n\n[... middle omitted ...]\n\n，并持续跟踪韩国海关月度数据的发布，第一时间更新我们的判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n韩国半导体设备进口飙了57%🔥投研信号来了\n\n韩国半导体设备进口数据出炉\n\n4月韩国半导体设备进口同比+57%，创历史新高📈\n\n虽然环比微降9%，但趋势依然强劲。背后是三星和SK海力士的扩产计划在加速推进。\n\n1️⃣ 存储巨头资本开支信号\n三星与SK海力士的合计资本开支与设备进口数据高度相关。虽然1Q26资本开支环比回落（季节性和4Q25前置基建投入），但两家公司都明确指引2026全年资本开支将大幅增长。后续设备进口数据有望继续走强。\n\n2️⃣ 测试设备：爱德万有惊喜？\n韩国测试设备进口（来自日本+马来西亚）4月环比-21%，同比+49%。根据某外资投行的回归模型，这暗示爱德万6月季度韩国收入可能环比+70%，远超市场预期的+5%。虽然只有一个月数据，但值得跟踪。\n\n3️⃣ 光刻设备：ASML韩国收入强劲\n4月韩国从荷兰进口WFE设备7.23亿欧元，是史上第二高的季度首月。虽然环比-28%，但同比暴增约180%。推算ASML韩国2Q系统销售约21亿欧元，占全球系统销售约33%。DRAM扩产和1c节点快速导入是主要驱动力。\n\n4️⃣ 日本设备：东京电子短期承压\n韩国从日本进口的各类设备（CVD、刻蚀、清洗等）4\n\n[... middle omitted ...]\n\nmine Milano, CFA\n\n+44 20 7762 1857\n\ncarmine.milano@bernsteinsg.com\n\n![](images/b04f540858321b267ca824de26c093868ae2a4acee9c15b97162e6741c5352f4.jpg)\n\nJack Lin\n\n+852 2123 2683\n\njack.lin@bernste\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R002",
    "title": "新房价格跌幅收窄，但真正的市场底不在统计局数据里",
    "digest": "[wechat_article.md]\n# 新房价格跌幅收窄，但真正的市场底不在统计局数据里\n\n四月的新房价格数据，终于给出了一点微弱的积极信号。\n\n国家统计局70城数据显示，经季节调整后，新房加权均价环比年化跌幅从3月的4.0%收窄至3.0%。一线城市继续环比上涨，上海领涨全国。二线和三线城市的环比跌幅也有所收窄。\n\n这些数字，看起来像是市场在经历漫长调整后，终于触碰到某种底部。\n\n但真正的问题在于：这个底部，是真实的吗？\n\n看完这份某外资投行的最新研报，我的核心判断是：新房市场的边际改善是真实的，但不足以支撑反转判断。市场真正低估的不是需求何时回暖，而是供给侧的定价逻辑正在发生结构性变化——当二手房以5%至15%的年度跌幅持续定价时，新房市场的价格信号已经失去了代表性。\n\n这份报告最重要的贡献，不是给了我们几个环比改善的数据点，而是揭示了一个关键事实：在中国房地产市场，你看到的“价格”和真实交易发生的“价格”，正在走向两个世界。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 新房价格改善的幅度有限，且集中在少数头部城市\n\n四月的数据确实比三月好看。70城加权均价环比年化跌幅从-4.0%收窄至-3.0%，一线城市从+0.3%加速至+0.4%的环比年化增长。上海表现最为突出，环比年化涨幅达到2.0%，而三月还是-0.9%。\n\n但这份改善的成色需要细看。\n\n同比数据并不乐观。全国加权均价同比跌幅从3月的-3.5%扩大至-3.6%。这意味着，即使环比在改善，但价格水平仍在一年比一年低。真正实现同比上涨的城市屈指可数，上海(+3.7%)和杭州(+2.3%)是其中代表。\n\n二线城市环比跌幅从-4.6%收窄至-2.8%，三线城市从-5.0%收窄至-4.6%。收窄是事实，但绝对值仍然很高。这告诉我们一个简单的道理：市场分化在加剧，头部城市有韧性，但广大二三线城市的\n\n[... middle omitted ...]\n\n周都会围绕类似主题展开讨论，帮助参与者建立更完整的分析框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n新房价格跌幅收窄，一线城市稳住了\n\n📊 4月房价数据：边际改善\n\n某外资投行最新研报显示，4月70城新房价格环比跌幅收窄，从3月的-4.0%收窄至-4月的-3.0%（季调后年化）。虽然同比跌幅略扩至-3.6%，但方向性变化值得关注。\n\n1️⃣ 一线城市表现分化，上海领涨\n- 一线城市整体环比+0.4%（3月为+0.3%），其中上海环比+2.0%，是主要拉动力量\n- 深圳、广州继续放松限购，提高公积金贷款额度，政策效果正在显现\n- 二三线城市跌幅也在收窄：二线从-4.6%收窄至-2.8%，三线从-5.0%收窄至-4.6%\n\n2️⃣ 新房 vs 二手房：两个市场，两种温度\n⚠️ 重要提醒：70城数据仅覆盖新房市场。二手房方面，统计局和第三方平台数据显示过去一年跌幅在5%-15%之间，比新房市场调整更深。\n\n3️⃣ 高频数据：交易量企稳\n- 30城新房交易量在4月和5月初基本持平去年同期\n- 主要城市库存去化周期从29.3个月降至28.9个月，二线城市改善更明显\n- 不过新房价格环比上涨的城市数量在减少（从3月约35%降至4月约20%）\n\n🧐 我的观察：\n上海作为一线城市“领头羊”的地位在强化，新房价格同比+3.7\n\n[... middle omitted ...]\n\nmarket data by NBS and some third-party platforms suggest price declines of $5 - 15\\%$ over the past year.\n\n# Key numbers: $^{1}$\n\nNBS' 70-city primary-market weighted average property price c\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R003",
    "title": "市场真正低估的不是需求，而是供给侧的再定价",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是需求，而是供给侧的再定价\n\n过去一个月，中国宏观数据释放的信号比表面看起来复杂得多。某外资投行最新发布的研报同时覆盖了三个看似独立、实则紧密关联的议题：中美首脑会晤后的贸易前景、远超预期的PPI通胀、以及持续走弱的居民信贷。这三件事放在一起，指向一个容易被忽视的核心判断——市场正在低估供给侧变量对中国资产定价的影响。\n\n4月PPI同比跃升至2.8%，远超市场预期的1.8%。这不是一个温和的通胀读数。更值得注意的是，这一跳升并非来自终端需求的全面复苏，而是上游资源品价格的结构性推升。石油开采和加工业PPI分别同比上涨28.6%和14.2%，有色金属开采和加工业分别上涨38.9%和22.5%。这些数字背后，是地缘政治重塑全球供应链定价权的长期叙事，而非短期需求的周期性波动。\n\n与此同时，居民部门仍在加速去杠杆。4月居民人民币贷款净增量持续为负，居民债务占GDP比率已从2024年一季度的62.3%高点降至去年底的59.4%，且最新信贷数据表明这一趋势在今年前四个月并未逆转。家庭不借钱、不扩表，意味着终端需求的修复路径比政策制定者预期的更漫长。\n\n而中美首脑会晤的官方通报，虽然措辞温和，但双方侧重完全不同——中方强调“战略稳定的中美关系”和台湾问题，美方聚焦中国购买美国商品、霍尔木兹海峡通航和芬太尼管控。结构性矛盾并未消解，只是短期风险有所后移。\n\n这三个信号叠加，意味着什么？中国经济的核心矛盾正从“需求端能否复苏”转向“供给侧如何被重新定价”。对于产业决策者和资产配置者而言，理解这一转变的方向和力度，远比猜测下一个刺激政策更重要。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. PPI跳升的真正含义不是通胀，而是上游定价权的结构性转移\n\n4月PPI超预期，市场的第一反应往往是“通胀压力上升，货币政策\n\n[... middle omitted ...]\n\n都会基于最新的宏观数据和政策动态，更新对这些核心变量的判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中美风向、通胀信号、家庭负债放缓\n\n三个关键信号\n\n最近某外资投行出了一份中国宏观观察，三个点值得细看👇\n\n1️⃣ 元首会面：短期风险下降\n\n特朗普访华后，双方各说各话。\n中方强调“战略稳定”和台湾问题，\n美方更关注买美国货、霍尔木兹海峡、芬太尼。\n\n虽然结构矛盾还在，\n但今年还有三次会面（9月/11月/12月），\n短期升温概率降低了。\n\n2️⃣ PPI超预期：上游涨价明显\n\n4月通胀数据超出预期：\n- CPI同比+1.2%（预期0.9%）\n- PPI同比+2.8%（预期1.8%）\n\nPPI跳升主要来自上游：\n- 石油开采+28.6%，加工+14.2%\n- 有色金属开采+38.9%，加工+22.5%\n\n如果PPI继续走高，\n央行可能从目前极度宽松的状态中，\n逐步回收流动性。\n\n3️⃣ 家庭还在降杠杆\n\n4月社融存量增速7.8%（3月7.9%），\n某投行把全年预测从8.5%下调到8.0%。\n\n关键是家庭贷款：\n- 4月存量贷款同比-0.7%\n- 家庭债务/GDP从2024Q1的62.3%降到去年底的59.4%\n- 4月新增家庭贷款依然为负\n\n说明大家还在还钱、不借钱，\n消费意愿短期难明显反弹。\n\n#学习笔记\n\n[... middle omitted ...]\n\nthe Strait of Hormuz, and controlling fentanyl. Taken together, although structural tensions remain, the summit suggests a lower near-term risk of further escalation. The two leaders are expec\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R004",
    "title": "市场真正低估的不是AI需求，而是AI对竞争格局的再定价",
    "digest": "[wechat_article.md]\n# 市场真正低估的不是AI需求，而是AI对竞争格局的再定价\n\n这份来自某外资投行的研报，核心判断并不在于AI将带来多大的生产力增量，而在于一个被绝大多数讨论忽略的前提性问题：AI究竟是加剧垄断，还是打破垄断？答案将决定未来十年资产定价的核心逻辑。\n\n报告用近一个世纪的税收和行政数据，构建了一个清晰的叙事框架：企业集中度和利润率在过去几十年里同步攀升至历史高位，而AI作为新一轮技术冲击，其最终效果取决于它作用于一个怎样的竞争起点。这个起点，远比大多数人意识到的更加集中、更加固化。\n\n对于产业决策者和长期投资者而言，真正需要追问的，不是“AI能做什么”，而是“AI会改变谁赢谁输”。这份报告提供了回答这一问题所需的底层数据和分析框架。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 企业集中度的长期上升，并非全球化或反垄断弱化的简单结果\n\n报告引用了Ma等经济学家基于近百年税收和行政记录构建的新数据集，揭示了一个被广泛观察但常被误解的趋势：美国企业集中度自1930年代以来持续上升，头部1%企业的销售额占比从1960年代的约60%攀升至近年来的约80%。这一趋势并非美国独有，在奥地利、丹麦、法国、德国、瑞士等发达经济体中，同样数据从类似起点上升至约70%。\n\n关于集中度上升的原因，市场普遍存在两种流行解释：全球化和反垄断执法弱化。报告通过跨国面板数据检验后发现，贸易开放度（以进出口总额与GDP之比衡量）与集中度上升之间缺乏显著关联。同时，以美国司法部反垄断司预算作为执法强度的代理变量，集中度在不同反垄断执法周期内以大致相同的速度上升。\n\n这意味着，将集中度上升简单归咎于政策失误或全球化冲击，可能忽略了更根本的结构性力量。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 真正驱动集\n\n[... middle omitted ...]\n\n层面数据、计量模型细节，以及针对不同行业竞争格局的具体拆解。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI来了，大公司会更强还是被颠覆？\n\n大公司赢面更大？\n\nAI可能加剧竞争，也可能让头部企业甩开对手\n\n最近读到某外资投行的一篇报告，讲的是AI到来前，市场集中度和利润率已经处在历史高位。这篇把逻辑拆得挺清楚，分享几个关键点👇\n\n1/ 集中度上升是大趋势\n从1930年代到现在，美国大公司的市场份额一直在涨。金融、制造业最早，后来扩展到信息、零售和批发。数据很直观：前1%的企业销售额占比从60%涨到了80%+。\n\n2/ 三个解释，哪个最靠谱？\n- 全球化：大公司从全球市场中捞到更多好处，但数据上没发现明显关联\n- 反垄断变弱：虽然有一定影响，但不同监管时期集中度上升速度差不多\n- 技术驱动：新技术让少数公司靠规模效应吃掉更多市场——这个解释最站得住\n\n3/ 利润率也在涨，两者啥关系？\n过去40年，美国企业利润率大幅上升。两个原因：\n- 收入高了，消费者对价格不那么敏感\n- 集中度上升，竞争减少\n报告估算：2000年以来，集中度上升解释了利润率增长的约1/3\n\n4/ AI会怎么改变格局？\n两面性：\n- 可能打破现有格局，让竞争更激烈\n- 也可能让AI用得好公司跑得更远，集中度进一步提高\n历史经验看，技术冲击后，前\n\n[... middle omitted ...]\n\noks like in sectors where AI is likely to have the largest impact.   \nNew data spanning nearly a century of tax and administrative records document a long-run rise in corporate concentration a\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R005",
    "title": "全球资金流向正在发出一个被忽视的信号：美国资产的“虹吸效应”并未减弱，但结构正在裂变",
    "digest": "[wechat_article.md]\n# 全球资金流向正在发出一个被忽视的信号：美国资产的“虹吸效应”并未减弱，但结构正在裂变\n\n过去一个月，全球资本市场的叙事焦点集中在“美国例外论是否终结”以及“新兴市场能否迎来资金回流”。但某外资投行最新发布的高频资金流监测数据揭示了一个更微妙的现实：全球资金仍在持续涌入美国资产，只是流入的结构正在发生实质性变化——权益与债券的偏好正在反转，而新兴市场的资金流入出现了明显的断崖式回落。这些变化背后，隐藏着对全球资产定价逻辑的深层含义。\n\n这份报告的核心价值不在于罗列数字，而在于提供了一个高频、多维度的资金流观测框架。它让我们得以避开月度或季度数据的滞后性，从周度甚至日度数据中捕捉到市场情绪的边际变化。对于关注全球资产配置、汇率走势以及亚太区域资金流动的决策者而言，这些高频信号比宏观叙事更具前瞻性。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 美国权益资产的“吸金”能力依然强劲，但债券市场正在经历资金外流\n\n报告显示，5月8日至14日当周，外国资金净流入美国相关基金达到21亿美元，其中权益类基金贡献了24亿美元的净流入，而债券类基金则出现了2.92亿美元的净流出。这组数据看似矛盾，实则揭示了市场对美国资产定价的核心分歧。\n\n权益市场的持续流入表明，投资者对美股盈利增长、科技叙事以及AI产业链的长期信心并未动摇。尽管市场存在对估值过高的担忧，但资金仍在用行动投票。相比之下，债券市场的流出则反映出市场对美国利率路径的重新定价——通胀粘性、劳动力市场韧性以及美联储的观望态度，正在削弱美债的吸引力。\n\n更值得关注的是月度趋势。5月至今，美国权益类基金已累计流入46亿美元，远超4月全月的31亿美元。这意味着，美国权益资产的吸引力不仅没有减弱，反而在加速强化。而债券市场的月度流入仅有2.17亿美元，较4月的1亿美元有所回升，\n\n[... middle omitted ...]\n\n径。欢迎来星球微信群里继续讨论，一起追踪这些关键变量的演变。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球资金正悄悄往美国走🇺🇸\n\n📊 资金流向观察\n\n**资金偏好明显转向**\n最近一周（5月8-14日），外资买入美国基金的净额达到21亿美元，比前一周的25.7亿略有回落，但仍然处于高位。主要买的是股票基金，净流入24亿美元，债券基金则小幅流出2.92亿。\n\n**新兴市场基金遇冷**\n同期（5月9-15日），新兴市场ETF整体净流出9700万美元，逆转了前一周12亿美元的净流入。拆开看，股票基金流入1.2亿，但债券基金流出2.17亿，债券拖了后腿。\n\n**亚洲投资者动向分化**\n- 🇰🇷韩国散户：继续净卖出美国资产7200万美元，其中股票卖出2.21亿，债券买入1.49亿。5月至今累计净卖出1400万美元，比4月的9.1亿净卖出明显收窄。\n- 🇹🇼台湾投资者：买入美元债券ETF 1.03亿美元，较前一周2.2亿有所放缓。但5月至今累计净买入3.23亿，已扭转4月净卖出3.42亿的局面。\n\n**月度趋势更清晰**\n5月至今，外资买入美国股票基金达46亿美元，已超过4月全月的31亿。债券基金也净流入2.17亿，高于4月的1亿。新兴市场ETF累计净流入11.56亿，但远低于4月的62.85亿。\n\n**一点思考**\n\n[... middle omitted ...]\n\n Korea's retail investor flows into US portfolio assets remained lacklustre, with net selling of USD72mn of US portfolio assets between 9 and 15 May.   \n- Taiwan's investors were also net buye\n\n[... middle omitted ...]\n\nrmation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R006",
    "title": "四月经济数据证实：市场低估的不是反弹结束，而是结构性分化的深度",
    "digest": "[wechat_article.md]\n# 四月经济数据证实：市场低估的不是反弹结束，而是结构性分化的深度\n\n四月经济数据公布后，市场情绪迅速从“一季度反弹是否可持续”切换为“底部在哪里”。但这份来自某外资投行的研报揭示了一个更深层的判断：当前的问题不是简单的复苏乏力，而是一场由供给端政策、外部价格冲击和内生需求萎缩共同驱动的结构性分化。这种分化正在重塑资产定价的逻辑，而市场对此的定价仍然不充分。\n\n研报的核心主张是：**AI 热潮和出口韧性无法对冲房地产下行和反内卷政策带来的收缩效应，中国经济正进入一个“增长中枢下移、结构性分化加剧”的新阶段。** 这不是一个周期性的波动，而是增长模式的再平衡。对于投资者和产业决策者而言，理解分化的具体机制，比争论总量数据何时见底更具实际意义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 工业生产的放缓并非需求疲软的全部答案，AI 驱动的价格效应和反内卷政策共同扭曲了真实产出信号\n\n四月工业增加值同比增速从三月的5.7%骤降至4.1%，远低于市场预期的6.0%。表面上看，这似乎印证了内需走弱的判断。但研报提供了两个关键的结构性视角。\n\n第一个视角是出口价格效应。四月出口同比增长高达14.1%，但其中约一半来自芯片和电子产品价格飙升。这意味着出口量的增长远没有名义数据那么强劲。更关键的是，出口交货值增速从三月的8.7%进一步升至10.6%，说明价格上涨反而可能抑制了实际需求，导致生产端被动放缓。这一机制在集成电路领域尤为明显：四月集成电路产量同比增长22.1%，但出口量增速却从12.9%降至3.7%。产出的增长更多是为了满足国内中间品需求，而非外需拉动。\n\n第二个视角是反内卷政策的持续影响。太阳能电池板产量增速从三月的-20.6%进一步下滑至-25.6%，汽车产量增速也从-0.1%降至-2.6%。这些行业正是政策重点\n\n[... middle omitted ...]\n\n更多关注宏观经济和产业趋势的读者一起，深入讨论这些未解问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n4月数据大降温，Q1反弹只是昙花一现？\n\n📉 4月经济数据全面走弱\n\n---\n\n朋友们，刚看完某外资投行4月中国经济数据解析，信息量很大，咱们直接拆干货👇\n\n**1/ 工业生产：表面出口亮眼，实际内需很冷**\n\n4月工业增加值同比增速从3月的5.7%掉到4.1%，远低于市场预期的6.0%。\n\n出口看着不错（同比+14.1%），但一半增量来自芯片和电子产品涨价，不是量的增长。扣除价格因素，实际出口量并不强。\n\n更关键的是，国内需求疲软才是拖累工业的主因。4月工作日同比少1天，也有影响。\n\n细分看：\n- 制造业产出增速从6.0%降到4.0%\n- 采矿业从5.7%降到3.8%\n- 公用事业反而从3.5%升到5.3%（电力生产回升）\n\n**2/ 消费：零售增速几乎归零**\n\n4月社零同比仅+0.2%，远低于市场预期的2.0%。扣除通胀后，实际零售增速转负（-1.0%），是2022年12月以来首次。\n\n什么在拖后腿？\n- 汽车销售：同比-15.3%，比3月的-11.8%还差\n- 家电：-15.0%（以旧换新政策退坡效应）\n- 石油制品：-6.5%（油价上涨抑制需求）\n- 办公用品：-6.9%（芯片涨价传导到终端）\n\n餐\n\n[... middle omitted ...]\n\nensus: $1.7\\%$ ; NOM: $2.0\\%$ ).\n\nThe weakness in IP growth, which is in real terms, was not a big surprise to us, as about half of headline export growth of $14.1\\%$ y-o-y in April was accoun\n\n[... middle omitted ...]\n\nable upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R007",
    "title": "中国衍生品新规的真正信号：不是收紧，是龙头加速分化的发令枪",
    "digest": "[wechat_article.md]\n# 中国衍生品新规的真正信号：不是收紧，是龙头加速分化的发令枪\n\n中国证监会于近期发布了《衍生品交易监督管理办法（试行）》，这是中国资本市场首部专门针对衍生品的部门规章。市场第一反应往往聚焦于“收紧”二字——更高的资本要求、更严格的交易限制、非合规产品的强制清退。某外资投行最新发布的研报给出了一个更具结构性价值的判断：这份新规的真正含义，不是市场的收缩，而是行业集中度加速提升的起点。对于持有头部券商资产的投资者而言，这可能是未来两到三年最被低估的定价因子。\n\n报告的核心逻辑并不复杂：新规通过提高资本门槛、扩大禁止交易范围、强化分类与隔离要求，系统性地抬高了衍生品业务的运营成本。小机构将被迫退出，而资本充足、风控完善、规模领先的头部券商，将凭借合规成本和产品供给能力的双重优势，进一步扩大市场份额。这不是一个“利空出尽”的故事，而是一个“结构分化”的起点。\n\n以下是我们基于该研报解析出的五个关键层次，每一层都指向同一个主判断：衍生品新规正在重塑中国券商的竞争格局，龙头券商的估值重估才刚刚开始。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 5000万净资本门槛，实际上是一道行业分水岭\n\n新规最直接的硬性约束，是要求开展衍生品交易的证券期货公司近六个月净资本不低于5000万元人民币。这一数字本身并不惊人，但它的结构性含义远大于数字本身。\n\n报告指出，与2026年1月的征求意见稿相比，正式版本保留了这一门槛，并且明确证监会可以根据审慎监管原则进行调整。这意味着，资本实力不再是“加分项”，而是“入场券”。对于中小券商而言，衍生品业务本身需要大量资本占用，5000万净资本只是基础门槛，实际运营中需要匹配的资本规模远高于此。许多小型机构将面临两难选择：要么大幅增资，要么退出这一业务线。\n\n横向来看，报告数据显示，2025年，C\n\n[... middle omitted ...]\n\n兑现，需要时间，也需要市场对“监管收紧”的叙事进行重新定价。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n证监会新规落地，衍生品市场迎来分水岭\n\n衍生品监管升级，头部券商更稳了\n\n这波新规利好龙头，行业洗牌加速\n\n最近某外资投行出了一份关于中国券商衍生品业务的分析，信息量挺大。核心结论是：监管新规短期有阵痛，但中长期利好头部券商，行业集中度会进一步提升。\n\n1️⃣ 新规核心要点\n证监会发布了《衍生品交易监督管理办法（试行）》，这是首部专门针对衍生品的部门规章。主要变化包括：\n- 对券商净资本设置门槛，过去6个月净资本不低于5亿元\n- 扩大交易限制，禁止上市公司、大股东、高管等利用衍生品交易自家股票或类似股权证券\n- 明确衍生品范围包括互换、远期、非标准化期权（含组合），期货除外\n- 强调衍生品应服务套期保值，抑制过度投机\n\n2️⃣ 短期承压，长期利好\n新规11月16日生效，有6个月过渡期。不合规产品要逐步清退，资本实力弱的小机构可能退出市场。但长期看，这为更规范、更有序的杠杆使用打开了空间。\n\n3️⃣ 头部券商优势明显\n数据显示，CITIC、CICC、HTSC、GTJA（原GTJA+海通）四家头部券商，2025年权益衍生品名义本金占所有上市券商的近60%（2024年约52%）。资本实力强、风控体系完善的头部机构，\n\n[... middle omitted ...]\n\ncurities and futures firms), tighter requirements on capital, classification, segregation, and reporting would raise operating costs, and therefore may potentially accelerate industry consolid\n\n[... middle omitted ...]\n\ncom/sa/en/cssa.html.\n\n© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.\n\n![](images/7a7b48137af65a28e0aefb053b198ca1e75ee9ab0ad8834dc2da7729dc2f152b.jpg)"
  },
  {
    "id": "R008",
    "title": "欧元区2026年财政的真实底色：扩张全靠德国，紧缩才是多数国家的选择",
    "digest": "[wechat_article.md]\n# 欧元区2026年财政的真实底色：扩张全靠德国，紧缩才是多数国家的选择\n\n市场对欧洲财政扩张的叙事正在变得过于简单。2026年欧元区财政预算计划揭示了一个与“集体大放水”印象截然不同的图景：整体赤字率将从2.9%上升至3.5%，但这一扩张几乎完全由德国一国驱动。法国、意大利、西班牙这三个核心经济体，实际上都在规划财政紧缩。这份来自某外资投行的研报，通过对21个欧元区国家最新预算计划的系统汇总，给出了一个值得所有关注欧洲资产定价的人重新审视的判断——欧元区的财政故事，本质上是一个德国的故事，而德国能否兑现其庞大的财政扩张承诺，才是决定2026年欧洲增长路径的关键变量。\n\n这不是一份简单的数据汇总。它拆解了各国财政脉冲的方向、力度与结构，并揭示了财政乘数效应在不同支出类型上的显著差异。对于正在重新评估欧洲风险溢价、利率路径和行业配置的投资者而言，理解这份预算计划背后的“非对称性”，比知道一个笼统的赤字数字重要得多。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 2026年欧元区财政脉冲仅为0.2%GDP，且完全系于德国一国的执行\n\n根据各国提交的年度进展报告，2026年欧元区经周期调整的初级财政赤字（CAPB）将扩大约0.2个百分点，这标志着自2021年以来首次出现财政宽松。但这一数字远低于市场此前部分预期，也低于某外资投行自身预测的0.3%GDP。更关键的是，德国一国就贡献了0.5个百分点的宽松力度，而法国、意大利、西班牙各自贡献了0.1个百分点的紧缩，恰好抵消了德国以外的全部扩张。换句话说，如果剔除德国，欧元区2026年的财政立场实际上是略微紧缩的。\n\n这意味着什么？当前市场对欧洲财政扩张的定价，隐含了一个“德国必然执行”的前提假设。但预算计划只是计划，执行才是现实。德国联邦支出在第一季度确实出现了由国防开支驱\n\n[... middle omitted ...]\n\n洲资产的配置逻辑，这些跟踪框架或许能帮你比市场更早看到拐点。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n2026年欧元区财政：全靠德国撑场\n\n德国一己之力撑起全区财政\n\n今年欧元区各国提交的预算计划，核心信号非常清晰：整体在温和放松，但基本全靠德国一家在拉。\n\n1/ 整体赤字率要涨了\n根据各国最新提交的年度进展报告（就是以前的稳定计划），欧元区2026年预算赤字将从2.9%升至3.5%。这是2023年以来的首次上升。背后主要是支出增加——支出占GDP比例预计上升0.8个百分点至50.6%，收入仅增0.3个百分点。\n\n2/ 国家之间分化严重\n21个欧元区国家中，有11个赤字在扩大，9个在缩小，1个持平。\n🔺 德国赤字扩大1.6个百分点至4.3%，爱沙尼亚扩大2.3个百分点至4.3%\n🔻 法国、意大利、西班牙都在收窄，分别缩小0.1、0.2、0.3个百分点\n如果把德国去掉，整个欧元区的赤字其实没变，仍维持在2.9%。\n\n3/ 财政脉冲只有0.2%的GDP\n用周期调整后的基本财政余额（CAPB）来算，2026年欧元区整体财政放松幅度只有0.2%的GDP。而且这里面的全部贡献都来自德国（贡献0.5个百分点），法国、意大利、西班牙反而在收紧（各扣0.1个百分点）。\n如果德国没有落地那个大规模财政方案，整个欧元区反而会略微\n\n[... middle omitted ...]\n\n reformed EU fiscal framework. In this note, we review and aggregate the individual country plans, which show budget deficit increases in around half of Eurozone countries, including much high\n\n[... middle omitted ...]\n\ntual property rights. © UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.\n\n![](images/0a05adbe4b09dd27919713193a8f2805bf97ddd252bfa634b7db0320a2549c9b.jpg)"
  },
  {
    "id": "R009",
    "title": "汽车股真正的alpha不在车本身，而在“非汽车”叙事能否重构估值",
    "digest": "[wechat_article.md]\n# 汽车股真正的alpha不在车本身，而在“非汽车”叙事能否重构估值\n\n过去一周，全球汽车产业链的投资者经历了一次典型的“信号分裂”。一边是S&P Global Mobility再度下调2026年全球汽车产量预期，将同比降幅从-1.8%进一步扩大至-2.4%；另一边，福特（F）凭借储能业务（BESS）的想象空间单周上涨9%，BorgWarner（BWA）和Aptiv（APTV）等供应商也因“非汽车”主题获得资金追捧。某外资投行最新研报揭示了一个正在被定价但不一定被充分理解的结构性变化：在传统汽车产量持续承压的背景下，市场真正奖励的已经不是谁能更好地管理汽车周期，而是谁能把自身技术能力迁移到汽车之外的更高增长领域——尤其是AI数据中心和储能。这份研报的价值不在于重复“行业不好”的共识，而在于提供了一套可操作的框架，用来判断哪些公司具备“跨界叙事”的基因，以及当这种叙事遭遇估值支撑时，为什么可能触发重估。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 产量下修的“前重后轻”结构，对北美供应商比表面数字更友好\n\nS&P Global Mobility上周五将2026年全球产量预测下调0.5个百分点，全年同比降幅从-1.8%扩大至-2.4%。乍看之下，这似乎是对整个供应链的利空。但拆解结构后，结论并不那么悲观。\n\n关键细节在于下修的时间分布。2026年第一季度产量实际上被上调了+1.6%，主要来自中国、中东、南亚和欧洲。这意味着所谓的“强一季度”部分源于OEM厂商为防范原材料/零部件短缺而进行的“提前生产”——这不是真实需求改善，而是库存前置。真正的压力集中在2026年第二至第四季度，这九个月的同比降幅达到-2.6%。\n\n但更重要的结构信息在下修的地区分布。在剩余三个季度的减产中，约41%来自中国，16%来自南亚，欧洲和\n\n[... middle omitted ...]\n\n深度解读和原始数据图表，帮助你在噪音中找到真正的结构性信号。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球汽车产量预期下调，但别急着悲观\n\n全球产量预期下调，但结构有看点\n\n最近S&P Global Mobility调整了2026年全球汽车产量预期，从之前的-1.8%下调到-2.4%。听起来不太乐观，但仔细拆开看，其实有结构性的信号值得关注。\n\n1️⃣ 产量下调集中在Q2-Q4，但Q1反而上调了+1.6%\nQ1的上调主要来自中国、中东、南亚和欧洲。S&P认为部分生产是被“提前”了——OEM在预防零部件短缺，所以把后面的产能往前拉。换句话说，Q1的“强”不完全是需求好，更多是预防性备货。\n\n2️⃣ 下半年下调的41%来自中国，北美只占5%（约4.2万辆）\n对于北美供应商来说，这个结构其实不算太差。研报也提到，他们自己的模型里中国/欧洲的假设已经比S&P低了约1%/0.4%，反而在北美比S&P更乐观。\n\n3️⃣ 2027年预期也被下调了-1.3%，但只是同比+0.8%\n研报推测，这次S&P一次性调得比较多，是为了避免“一点点慢慢砍”的痛苦。如果宏观担忧缓解，未来反而有上调空间。\n\n4️⃣ 汽车AI交易还没死，只是涨太快了\n上周福特（F）的BESS（电池储能系统）机会引发关注，研报看好其与CATL的技术合作、PTC\n\n[... middle omitted ...]\n\n than thought. And S&P indicated \"early evidence that some production is effectively being pulled forward as OEMs guard against potential feedstock/part shortages.\" In looking at the cut over \n\n[... middle omitted ...]\n\ncom/sa/en/cssa.html.\n\n© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.\n\n![](images/a9ce15564d72a064fec4837defbcac69f5b48ef086a37dc1a8f974c8b725a4c6.jpg)"
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "Exhibit 1",
    "context": "EXHIBIT 1: April South Korea imports for SPE was \\$3.4bn, -9% MoM."
  },
  {
    "figure_id": "F002",
    "report_id": "R001",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: April South Korea imports for Japanese SPE was \\$699mn, -19% MoM."
  },
  {
    "figure_id": "F003",
    "report_id": "R001",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: South Korea SPE monthly import data has good directional correlation with Samsung and SK hynix's quarterly capex."
  },
  {
    "figure_id": "F004",
    "report_id": "R001",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: 1QCY26 capex came down QoQ for both Samsung and SK hynix due to seasonality and also as some front loaded infrastructure investments in 4Q25. Capex (KRW B)"
  },
  {
    "figure_id": "F005",
    "report_id": "R001",
    "label": "Exhibit 6",
    "context": "EXHIBIT 5: April tester imports from Japan and Malaysia collectively was -21% MoM."
  },
  {
    "figure_id": "F006",
    "report_id": "R001",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: South Korea tester imports data shows good directional correlation with Advantest's South Korea sales."
  },
  {
    "figure_id": "F007",
    "report_id": "R001",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: Advantest's Quarterly Korean sales shows good correlation with Korean monthly imports. Advantest Quarterly KR Sales vs. KR 1M Import: 1QCY16-1QCY26"
  },
  {
    "figure_id": "F008",
    "report_id": "R001",
    "label": "Exhibit 10",
    "context": "EXHIBIT 9: April imports from Japan for WFE equipment where TEL has exposure, were collectively -19% MoM."
  },
  {
    "figure_id": "F009",
    "report_id": "R001",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: South Korea monthly WFE imports from Japan show good directional correlation with TEL's South Korea revenue."
  },
  {
    "figure_id": "F010",
    "report_id": "R001",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: TEL's Quarterly Korean sales shows decent correlation with Korean monthly imports. TEL Quarterly KR Sales vs. KR Import: 1st Month of 1QCY16-1QCY26"
  },
  {
    "figure_id": "F011",
    "report_id": "R001",
    "label": "Exhibit 13",
    "context": "EXHIBIT 13: South Korea monthly SPE imports from Netherlands shows good directional correlation with ASML's South Korea revenue divided by 3. April Litho Imports of EUR 723mn declined 28% MoM but up \\~180% YoY."
  },
  {
    "figure_id": "F012",
    "report_id": "R001",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: Regressing ASML Korea's quarterly system sales against 1 month + 1M lag of import data, we obtain an R $^{2}$ of 75% and estimate that Q2 ASML Korea revenue will reach EUR 2.1bn, down 26% QoQ."
  },
  {
    "figure_id": "F013",
    "report_id": "R001",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: Our regression indicates very strong KR sales at EUR 2.1Bn, down 26% sequentially due to the record level reached last quarter, implying that KR accounts for approximately 33% of system sales. EXHIBIT 16: We estimate KR"
  },
  {
    "figure_id": "F014",
    "report_id": "R002",
    "label": "Exhibit 1",
    "context": "Exhibit 1: In the primary market, the sequential decline in 70-city weighted average property price eased to $3.0\\%$ mom annualized in April"
  },
  {
    "figure_id": "F015",
    "report_id": "R002",
    "label": "Exhibit 2",
    "context": "Exhibit 2: The share of cities that experienced sequentially higher property prices edged down in secondary markets in April"
  },
  {
    "figure_id": "F016",
    "report_id": "R002",
    "label": "Exhibit 3",
    "context": "Exhibit 3: NBS 70-city secondary home prices continued to decline in April"
  },
  {
    "figure_id": "F017",
    "report_id": "R004",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Corporate Profits and Concentration Are at Record Highs in the US"
  },
  {
    "figure_id": "F018",
    "report_id": "R004",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Corporate Concentration Has Risen Steadily, Both Across Advanced Economies... Sales Share of the Top 1% Firms by Sales Across Advanced Economies*"
  },
  {
    "figure_id": "F019",
    "report_id": "R004",
    "label": "Exhibit 3",
    "context": "Exhibit 3: ...And US Industries Asset Share of the Top 1% Firms by Assets*"
  },
  {
    "figure_id": "F020",
    "report_id": "R004",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Corporate Concentration Has Risen Across Different Antitrust Regimes"
  },
  {
    "figure_id": "F021",
    "report_id": "R004",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Corporate Concentration Has Risen Faster During Periods of Rapid Technological Change"
  },
  {
    "figure_id": "F022",
    "report_id": "R004",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Technological Change Has Widened Productivity Dispersion Across Firms, Particularly in Technology-Related Industries, Increasing the Gap Between Frontier Firms and the Rest"
  },
  {
    "figure_id": "F023",
    "report_id": "R004",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Markups Charged by US Firms Have Risen Since the 1980s..."
  },
  {
    "figure_id": "F024",
    "report_id": "R004",
    "label": "Exhibit 8",
    "context": "Exhibit 8: ...Partly Reflecting Lower Consumer Price Sensitivity as Rising Incomes Lead Households to Search Less Across Sellers Change in US Consumer Sensitivity to Prices Relative to 2006 Estimated at the Product-Level*"
  },
  {
    "figure_id": "F025",
    "report_id": "R004",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Rising Concentration Accounts for Roughly One-Third of the Increase in Profit Margins Since 2000 Change in Corporate Profit Margins, 2000-24*"
  },
  {
    "figure_id": "F026",
    "report_id": "R004",
    "label": "Exhibit 10",
    "context": "Exhibit 10: While Concentration Has Risen at the National Level, It May Have Declined at the Local Level as Larger Firms Have Increasingly Entered Local Markets Change in the Average Herfindahl-Hirschman Index, 1990s vs. 2010s*"
  },
  {
    "figure_id": "F027",
    "report_id": "R004",
    "label": "Exhibit 11",
    "context": "Exhibit 11: AI-Exposed Industries Are Somewhat More Concentrated and Operate with Higher Profit Margins Relationship Between Industry-Level Concentration and AI Exposure"
  },
  {
    "figure_id": "F028",
    "report_id": "R005",
    "label": "Figure 3",
    "context": "- Foreign inflows into US-focused equity ETFs and mutual funds $^{[1]}$ totaled USD2.4bn between 8 and 14 May (Figure 3), continuing from inflows of USD2.2bn in the previous week. MTD May, inflows into these funds totaled USD4.6bn surpassing total inflows of U"
  },
  {
    "figure_id": "F029",
    "report_id": "R007",
    "label": "Figure 1",
    "context": "Figure 1: Leading brokers' share in notional principal of equity derivatives expanded Notional principal of equity derivatives"
  },
  {
    "figure_id": "F030",
    "report_id": "R007",
    "label": "Figure 2",
    "context": "Figure 2: Commodities derivatives dominating exchange-traded in China Exchange-traded derivatives"
  },
  {
    "figure_id": "F031",
    "report_id": "R008",
    "label": "Figure 1",
    "context": "Figure 1: Eurozone headline budget balance, % of GDP"
  },
  {
    "figure_id": "F032",
    "report_id": "R008",
    "label": "Figure 2",
    "context": "Figure 2: Eurozone revenues and expenditures, % of GDP"
  },
  {
    "figure_id": "F033",
    "report_id": "R008",
    "label": "Figure 3",
    "context": "Figure 3: Headline budget deficits, 2026, % of GDP"
  },
  {
    "figure_id": "F034",
    "report_id": "R008",
    "label": "Figure 4",
    "context": "Figure 4: Eurozone, level of cyclically adjusted primary balance, % of GDP"
  },
  {
    "figure_id": "F035",
    "report_id": "R008",
    "label": "Figure 5",
    "context": "Figure 5: Eurozone, change in cyclically adjusted primary balance, % of GDP"
  },
  {
    "figure_id": "F036",
    "report_id": "R008",
    "label": "Figure 6",
    "context": "Figure 6: Eurozone government debt, % of GDP"
  },
  {
    "figure_id": "F037",
    "report_id": "R008",
    "label": "Figure 7",
    "context": "Figure 7: Contributions to 2026 Eurozone fiscal impulse, % of GDP"
  },
  {
    "figure_id": "F038",
    "report_id": "R008",
    "label": "Figure 8",
    "context": "Figure 8: Fiscal measures to counter the energy shock announced in 2026 so far in the Eurozone Figure 9: National fiscal policy support to counter the energy shock, 2026 vs 2022/23, % of GDP"
  },
  {
    "figure_id": "F039",
    "report_id": "R008",
    "label": "Figure 10",
    "context": "Figure 10: Number of Eurozone countries with budget deficits above 3% of GDP"
  },
  {
    "figure_id": "F040",
    "report_id": "R008",
    "label": "Figure 11",
    "context": "Figure 11: Germany budget deficit and CAPB, % of GDP"
  },
  {
    "figure_id": "F041",
    "report_id": "R008",
    "label": "Figure 12",
    "context": "Figure 12: Italy budget deficit and CAPB, % of GDP"
  },
  {
    "figure_id": "F042",
    "report_id": "R008",
    "label": "Figure 13",
    "context": "Figure 13: France budget deficit and CAPB, % of GDP"
  },
  {
    "figure_id": "F043",
    "report_id": "R008",
    "label": "Figure 14",
    "context": "Figure 14: Spain budget deficit and CAPB, % of GDP"
  },
  {
    "figure_id": "F044",
    "report_id": "R008",
    "label": "Figure 15",
    "context": "Figure 15: Key fiscal variables in governments' 2026 annual progress reports Figure 16: NGEU – RRF disbursements, EUR bn"
  },
  {
    "figure_id": "F045",
    "report_id": "R008",
    "label": "Figure 17",
    "context": "Figure 17: NGEU – RRF disbursements, % of 2025 GDP"
  },
  {
    "figure_id": "F046",
    "report_id": "R009",
    "label": "Figure 2",
    "context": "Figure 2: US Automotive coverage stock performance, past week"
  },
  {
    "figure_id": "F047",
    "report_id": "R009",
    "label": "Figure 3",
    "context": "Figure 3: US Automotive coverage stock performance, last 3 months"
  },
  {
    "figure_id": "F048",
    "report_id": "R009",
    "label": "Figure 4",
    "context": "Figure 4: US Automotive coverage stock performance, last 12 months Stock performance, 12 months"
  },
  {
    "figure_id": "F049",
    "report_id": "R009",
    "label": "Figure 6",
    "context": "Figure 6: Auto Industry sub-sector heat map Figure 7: US auto suppliers historical NTM EV/EBITDA multiples"
  },
  {
    "figure_id": "F050",
    "report_id": "R009",
    "label": "Figure 8",
    "context": "Figure 8: US auto suppliers historical relative premium/discount to group"
  },
  {
    "figure_id": "F051",
    "report_id": "R009",
    "label": "Figure 12",
    "context": "Figure 12: US Monthly SAAR Trend"
  },
  {
    "figure_id": "F052",
    "report_id": "R009",
    "label": "Figure 13",
    "context": "Figure 13: US Market Share"
  },
  {
    "figure_id": "F053",
    "report_id": "R009",
    "label": "Figure 14",
    "context": "Figure 14: Company Days Inventory"
  },
  {
    "figure_id": "F054",
    "report_id": "R009",
    "label": "Figure 15",
    "context": "Figure 15: US Industry Days Inventory"
  },
  {
    "figure_id": "F055",
    "report_id": "R009",
    "label": "Figure 16",
    "context": "Figure 16: US SAAR and Inventories Figure 17: Industry Average Transaction Price"
  },
  {
    "figure_id": "F056",
    "report_id": "R009",
    "label": "Figure 16",
    "context": "Figure 16: US SAAR and Inventories Figure 17: Industry Average Transaction Price"
  },
  {
    "figure_id": "F057",
    "report_id": "R009",
    "label": "Figure 18",
    "context": "Figure 18: Value of SAAR"
  },
  {
    "figure_id": "F058",
    "report_id": "R009",
    "label": "Figure 19",
    "context": "Figure 19: Industry Incentive per unit trend"
  },
  {
    "figure_id": "F059",
    "report_id": "R009",
    "label": "Figure 20",
    "context": "Figure 20: Company Incentive per unit trend"
  },
  {
    "figure_id": "F060",
    "report_id": "R009",
    "label": "Figure 21",
    "context": "Figure 21: Manheim used vehicle index"
  },
  {
    "figure_id": "F061",
    "report_id": "R009",
    "label": "Figure 22",
    "context": "Figure 22: North America LVP - S&P Forecast North America LVP"
  },
  {
    "figure_id": "F062",
    "report_id": "R009",
    "label": "Figure 23",
    "context": "Figure 23: Europe LVP - S&P Forecast Europe LVP"
  },
  {
    "figure_id": "F063",
    "report_id": "R009",
    "label": "Figure 24",
    "context": "Figure 24: China LVP - S&P Forecast China LVP"
  },
  {
    "figure_id": "F064",
    "report_id": "R009",
    "label": "Figure 25",
    "context": "Figure 25: Global LVP - S&P Forecast Global LVP"
  },
  {
    "figure_id": "F065",
    "report_id": "R009",
    "label": "Figure 26",
    "context": "Figure 26: Quarterly LVP by Region - S&P Forecast # EPS TRENDS Figure 27: F 2Q26 Consensus EPS Trend"
  },
  {
    "figure_id": "F066",
    "report_id": "R009",
    "label": "Figure 26",
    "context": "Figure 26: Quarterly LVP by Region - S&P Forecast # EPS TRENDS Figure 27: F 2Q26 Consensus EPS Trend"
  },
  {
    "figure_id": "F067",
    "report_id": "R009",
    "label": "Figure 28",
    "context": "Figure 28: F 2026 Consensus EPS Trend"
  },
  {
    "figure_id": "F068",
    "report_id": "R009",
    "label": "Figure 29",
    "context": "Figure 29: GM 2Q26 Consensus EPS Trend"
  },
  {
    "figure_id": "F069",
    "report_id": "R009",
    "label": "Figure 30",
    "context": "Figure 30: GM 2026 Consensus EPS Trend"
  },
  {
    "figure_id": "F070",
    "report_id": "R009",
    "label": "Figure 31",
    "context": "Figure 31: TSLA 2Q26 Consensus EPS Trend"
  },
  {
    "figure_id": "F071",
    "report_id": "R009",
    "label": "Figure 32",
    "context": "Figure 32: TSLA 2026 Consensus EPS Trend"
  },
  {
    "figure_id": "F072",
    "report_id": "R009",
    "label": "Figure 33",
    "context": "Figure 33: RIVN 2Q26 Consensus EPS Trend"
  },
  {
    "figure_id": "F073",
    "report_id": "R009",
    "label": "Figure 34",
    "context": "Figure 34: RIVN 2026 Consensus EPS Trend"
  },
  {
    "figure_id": "F074",
    "report_id": "R009",
    "label": "Figure 35",
    "context": "Figure 35: ADNT F3Q26 Consensus EPS Trend"
  },
  {
    "figure_id": "F075",
    "report_id": "R009",
    "label": "Figure 36",
    "context": "Figure 36: ADNT 2026 Consensus EPS Trend"
  },
  {
    "figure_id": "F076",
    "report_id": "R009",
    "label": "Figure 37",
    "context": "Figure 37: APH 2Q26 Consensus EPS Trend"
  },
  {
    "figure_id": "F077",
    "report_id": "R009",
    "label": "Figure 38",
    "context": "Figure 38: APH 2026 Consensus EPS Trend"
  },
  {
    "figure_id": "F078",
    "report_id": "R009",
    "label": "Figure 39",
    "context": "Figure 39: APTV 2Q26 Consensus EPS Trend"
  },
  {
    "figure_id": "F079",
    "report_id": "R009",
    "label": "Figure 40",
    "context": "Figure 40: APTV 2026 Consensus EPS Trend"
  },
  {
    "figure_id": "F080",
    "report_id": "R009",
    "label": "Figure 41",
    "context": "Figure 41: BWA 2Q26 Consensus EPS Trend"
  },
  {
    "figure_id": "F081",
    "report_id": "R009",
    "label": "Figure 42",
    "context": "Figure 42: BWA 2026 Consensus EPS Trend"
  },
  {
    "figure_id": "F082",
    "report_id": "R009",
    "label": "Figure 43",
    "context": "Figure 43: CARG 2Q26 Consensus EPS Trend"
  },
  {
    "figure_id": "F083",
    "report_id": "R009",
    "label": "Figure 44",
    "context": "Figure 44: CARG 2026 Consensus EPS Trend"
  },
  {
    "figure_id": "F084",
    "report_id": "R009",
    "label": "Figure 45",
    "context": "Figure 45: CARS 2Q26 Consensus EPS Trend"
  },
  {
    "figure_id": "F085",
    "report_id": "R009",
    "label": "Figure 46",
    "context": "Figure 46: CARS 2026 Consensus EPS Trend"
  },
  {
    "figure_id": "F086",
    "report_id": "R009",
    "label": "Figure 47",
    "context": "Figure 47: CVNA 2Q26 Consensus EPS Trend"
  },
  {
    "figure_id": "F087",
    "report_id": "R009",
    "label": "Figure 48",
    "context": "Figure 48: CVNA 2026 Consensus EPS Trend"
  },
  {
    "figure_id": "F088",
    "report_id": "R009",
    "label": "Figure 49",
    "context": "Figure 49: DAN 2Q26 Consensus EPS Trend"
  },
  {
    "figure_id": "F089",
    "report_id": "R009",
    "label": "Figure 50",
    "context": "Figure 50: DAN 2026 Consensus EPS Trend"
  },
  {
    "figure_id": "F090",
    "report_id": "R009",
    "label": "Figure 51",
    "context": "Figure 51: DCH 2Q26 Consensus EPS Trend"
  },
  {
    "figure_id": "F091",
    "report_id": "R009",
    "label": "Figure 52",
    "context": "Figure 52: DCH 2026 Consensus EPS Trend"
  },
  {
    "figure_id": "F092",
    "report_id": "R009",
    "label": "Figure 53",
    "context": "Figure 53: GNTX 2Q26 Consensus EPS Trend Figure 54: GNTX 2026 Consensus EPS Trend"
  },
  {
    "figure_id": "F093",
    "report_id": "R009",
    "label": "Figure 55",
    "context": "Figure 55: LEA 2Q26 Consensus EPS Trend"
  },
  {
    "figure_id": "F094",
    "report_id": "R009",
    "label": "Figure 56",
    "context": "Figure 56: LEA 2026 Consensus EPS Trend"
  },
  {
    "figure_id": "F095",
    "report_id": "R009",
    "label": "Figure 57",
    "context": "Figure 57: MGA 2Q26 Consensus EPS Trend"
  },
  {
    "figure_id": "F096",
    "report_id": "R009",
    "label": "Figure 58",
    "context": "Figure 58: MGA 2026 Consensus EPS Trend"
  },
  {
    "figure_id": "F097",
    "report_id": "R009",
    "label": "Figure 59",
    "context": "Figure 59: MBLY 2Q26 Consensus EPS Trend"
  },
  {
    "figure_id": "F098",
    "report_id": "R009",
    "label": "Figure 60",
    "context": "Figure 60: MBLY 2026 Consensus EPS Trend"
  },
  {
    "figure_id": "F099",
    "report_id": "R009",
    "label": "Figure 61",
    "context": "Figure 61: PHIN 2Q26 Consensus EPS Trend"
  },
  {
    "figure_id": "F100",
    "report_id": "R009",
    "label": "Figure 62",
    "context": "Figure 62: PHIN 2026 Consensus EPS Trend"
  },
  {
    "figure_id": "F101",
    "report_id": "R009",
    "label": "Figure 63",
    "context": "Figure 63: QS 2Q26 Consensus EPS Trend"
  },
  {
    "figure_id": "F102",
    "report_id": "R009",
    "label": "Figure 64",
    "context": "Figure 64: QS 2026 Consensus EPS Trend"
  },
  {
    "figure_id": "F103",
    "report_id": "R009",
    "label": "Figure 65",
    "context": "Figure 65: ST 2Q26 Consensus EPS Trend"
  },
  {
    "figure_id": "F104",
    "report_id": "R009",
    "label": "Figure 66",
    "context": "Figure 66: ST 2026 Consensus EPS Trend"
  },
  {
    "figure_id": "F105",
    "report_id": "R009",
    "label": "Figure 67",
    "context": "Figure 67: TEL F3Q26 Consensus EPS Trend"
  },
  {
    "figure_id": "F106",
    "report_id": "R009",
    "label": "Figure 68",
    "context": "Figure 68: TEL 2026 Consensus EPS Trend"
  },
  {
    "figure_id": "F107",
    "report_id": "R009",
    "label": "Figure 69",
    "context": "Figure 69: VC 2Q26 Consensus EPS Trend"
  },
  {
    "figure_id": "F108",
    "report_id": "R009",
    "label": "Figure 70",
    "context": "Figure 70: VC 2026 Consensus EPS Trend"
  }
]