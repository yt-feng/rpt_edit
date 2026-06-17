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
    "title": "JPM：市场真正定价的不是衰退，而是财政与通胀的再平衡",
    "digest": "[wechat_article.md]\n# JPM：市场真正定价的不是衰退，而是财政与通胀的再平衡\n\n这份JPM最新宏观策略报告的核心判断，值得每一位资产配置者和产业决策者仔细推敲：当前金融市场正在定价的，并非一次传统意义上的经济衰退或政策宽松周期，而是一个由财政主导、通胀粘性与供给冲击相互缠绕的“再平衡”过程。全球利率曲线、汇率走势和大宗商品定价，都正在被这一深层逻辑重新校准。\n\n报告明确传递了一个信号：市场对美联储降息的定价过于激进，而对财政供给压力和地缘供给侧冲击的持续性则可能低估。这不是一份简单的“看多美债”或“看空美股”的报告，而是一幅关于全球资产定价锚点正在发生结构性位移的路线图。\n\n为什么现在重要？因为过去几个月，市场在“软着陆”叙事与“衰退交易”之间反复摇摆，但真正的结构性力量——美国财政赤字的长期化、全球央行紧缩的惯性、以及霍尔木兹海峡问题对能源和金属供应链的持续扰动——正在被短期情绪掩盖。JPM这份报告的价值，在于将这些力量系统性地纳入了一个可检验的分析框架。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 美国利率的锚点正在从“政策利率”转向“财政供给”\n\n报告最值得关注的一个判断，是美国利率定价的锚点正在发生迁移。传统上，10年期美债收益率主要由对未来联邦基金利率的预期主导，但JPM的模型显示，当前曲线定价中，财政供给因素和期限溢价的权重正在显著上升。\n\n报告明确指出，由于2027财年及之后存在巨大的融资缺口，美国财政部预计将在今年8月移除其前瞻指引中的“至少”措辞，为从2027年2月开始的多季度系列息票增发做准备。这意味着，即使美联储维持利率不变，长端利率也可能因为供给压力而系统性抬升。JPM预测，2年期和10年期美债收益率将在2026年底分别升至4.20%和4.70%。\n\n这一判断的含义是：投资者不能再用“美联储何时降息”来推\n\n[... middle omitted ...]\n\n，我们将围绕这些关键变量，持续跟踪报告的后续更新与市场反馈。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美联储按兵不动，美债收益率还要涨？\n\n**债市逻辑拆解**\n\n美债收益率预测上调，2年期4.20%，10年期4.70%（年底）。\n\n1️⃣ **为什么美联储不动，收益率还在涨？**\n- 市场定价比美联储更鹰：OIS定价未来1-2年加息35bp，而美联储预计仅2027年3季度加一次\n- 就业数据稳定，货币政策到底紧不紧？市场在怀疑\n- 曲线陡峭化会传导到收益率，当前10年期比公允价值低24bp\n\n2️⃣ **美债vs德债，谁更值得持有？**\n- 全球央行偏鹰，美债相对其他发达国家国债估值没吸引力\n- 建议：做空10年期美债 vs 德债（相对价值交易）\n- 曲线策略：推荐10s/30s flatteners（当前比公允值陡14bp，接近2个标准差）\n\n3️⃣ **财政部发债压力不容忽视**\n- FY27起资金缺口扩大，预计8月财政部会修改“至少”措辞，为2027年2月起的多季度增发做铺垫\n- 白宫压低长端利率的意图，可能推迟措辞调整\n- 外国需求和银行需求预期下调\n\n4️⃣ **新主席Warsh上台，政策路径怎么走？**\n- Warsh主张缩表+降息并行，对金融条件影响更中性\n- 模型测算：缩表近1万亿美元才能支\n\n[... middle omitted ...]\n\nsh yields higher from here. We project 2- and 10-year yields will rise to 4.20% and 4.70%, respectively, at YE26. Stay short 10-year Treasuries versus Bunds, and enter 10s/30s Treasury curve f\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R002",
    "title": "NOM：市场低估了中东协议对全球资产定价的连锁效应，而非仅关注地缘风险本身",
    "digest": "[wechat_article.md]\n# NOM：市场低估了中东协议对全球资产定价的连锁效应，而非仅关注地缘风险本身\n\n这份NOM研报的核心判断，并非简单地“看多”或“看空”某个市场，而是提出一个更具结构性的观点：市场正在低估美伊临时协议签署后，全球资产定价逻辑从“地缘风险溢价”向“宏观基本面与相对价值”切换的深度和速度。NOM认为，真正的交易机会不在于赌局势升级或缓和，而在于捕捉这种定价逻辑切换带来的、由本地因素驱动的相对价值交易。\n\n报告发布的时间点——美伊即将于6月19日签署谅解备忘录前夕——本身就极具信号意义。自5月22日以来，NOM已经基于“局势缓和”的假设调整了策略仓位。如今，随着协议签署的确认，NOM进一步强化了这一立场，并做出了数项关键调整。这并非一次简单的战术性调整，而是对全球宏观交易主题的一次系统性重估。\n\n报告最值得关注的信号，不是某个具体的汇率目标价，而是其背后清晰的投资框架：在美元整体偏弱的背景下，交易的重心应从“做多或做空美元”这种笼统的方向性押注，转向“基于各国本地因素（经济增长、货币政策、资本流动、政治风险）进行多空配对交易”。这意味着，未来一段时间的赢家，将是那些能够精准识别并利用各国基本面差异的投资者。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 美伊协议不仅是地缘事件，更是全球资产重定价的触发器\n\n研报明确指出，美伊临时协议的签署，其意义远超出中东地缘政治本身。它直接触发了全球资产定价框架的三个核心变量的变化：能源价格、美元走势和风险偏好。\n\n首先，协议的核心内容之一——重新开放霍尔木兹海峡——直接指向能源供给侧。一旦海峡通航恢复，全球能源价格面临的下行压力将显著增加。这对于高度依赖能源进口的经济体（如新西兰、印度、韩国）是重大利好，而对于能源出口国（如澳大利亚）则构成拖累。NOM正是基于这一逻辑，维持了对澳元\n\n[... middle omitted ...]\n\n深度讨论，欢迎你来，一起拆解这些更复杂、也更诱人的投资谜题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美伊协议落地，外汇策略怎么调\n\n美伊缓和下的外汇调仓\n\n短期看弱美元，关注地区性相对价值\n\n某外资投行最新研报，围绕美伊可能签署临时协议（6月19日签MOU）做了策略调整，核心逻辑是：地缘缓和→能源价格回落→弱美元格局延续，但操作上更强调“精选货币对”。\n\n1️⃣ 整体方向：选择性做空美元\n- 维持看空美元/人民币（目标6.60，8月底），理由包括中间价持续走低、企业结汇需求强、人民币被低估约9.7%\n- 看空美元/台币（目标30.5，9月底），受益于AI需求+科技出口强劲+能源价格若回落\n- 新开空美元/韩元，但信心仅1/5（观察仓），需看到更多条件配合\n\n2️⃣ 地区货币相对价值交易是重点\n- 做多欧元/印度卢比（信心升至3/5），认为能源降价利好欧元，印度虽有FCNR(B)存款流入但本质是央行卖汇\n- 做多新加坡元/印尼盾（信心降至3/5），因MOU签署降低印尼加息必要性，但BI可能购债干预\n- 做空澳元/纽元（信心4/5），RBA加息周期结束+新西兰是石油进口国\n\n3️⃣ G10货币：低β组合\n- 做多瑞郎/日元（信心3/5），风险情绪改善利好日元交叉盘，但注意日本财务省可能干预\n- 做多欧元/英镑（\n\n[... middle omitted ...]\n\nnitiate short USD/KRW, with a conviction level of 1/5, reinitiate our long EUR/INR (raise to 3/5 from 2), and lower the conviction level on our long SGD/IDR to 3/5 (from 4). We also maintain s\n\n[... middle omitted ...]\n\nrmation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R003",
    "title": "摩根斯坦利：存储器价格的结构性重置，远比市场理解的更深远",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：存储器价格的结构性重置，远比市场理解的更深远\n\n2026年，全球存储器市场规模将从2025年的约2200亿美元跃升至约8900亿美元。增量部分——约6000亿美元——已经超过了智能手机、PC或服务器任何一个单一品类的完整市场空间。\n\n这不是一个周期性波动。这是存储器作为数字世界基础输入品，其价格行为正在经历一次结构性重置。\n\n摩根斯坦利在最新发布的《Chipflation – Implications of a Memory Crisis》全球宏观论坛报告中，用一个核心概念概括了这一变化：Chipflation。芯片通胀。报告由首席固定收益策略师Vishwanath Tirupattur领衔，联合半导体、IT硬件、商品策略、美国公共政策和美国经济研究团队共同撰写。这不是一份单一的行业报告，而是一次跨资产、跨领域的系统性推演。\n\n市场目前对这场存储器危机的定价，仍停留在“供应紧张”的周期叙事中。但报告揭示的真相是：AI正在从根本上改变存储器的需求结构和定价逻辑，而供给端的三家寡头格局和地缘政治约束，使得传统的“扩产-降价”循环已经失效。\n\n以下是我们从这份报告中提炼出的五个核心洞察，以及一个报告尚未完全回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 存储器不再遵循摩尔定律：价格六倍上涨背后的结构性断裂\n\n过去一年，存储器价格上涨超过六倍。对于习惯了半导体价格长期下行的产业界和投资者来说，这个数字本身就是一个信号。\n\n摩根斯坦利的分析框架清晰地指出，这不是一次普通的库存周期反转。报告用了一个关键区分：这是一个供给问题，还是一个需求问题？答案是两者兼具，但驱动因素完全不同。\n\n从需求端看，AI创造了突然且价格弹性极低的需求跃升。HBM（高带宽存储器）的使用量，在单个AI芯片层面增长了7倍\n\n[... middle omitted ...]\n\n我们会定期分享机构报告的完整解读、数据图表和跨行业比较分析。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI正在吃掉你的手机和电脑内存\n\n**Chipflation来了**\n\n**内存危机如何影响你的下一台设备**\n\n---\n\n最近某外资投行的宏观论坛抛出一个很有意思的概念——Chipflation（芯片通胀）。这不是普通的芯片涨价，而是一次结构性重置。\n\n1️⃣ **内存不再“越来越便宜”**\n过去一年，内存价格涨了6倍以上。以前我们习惯的“摩尔定律”——每两年性能翻倍、价格减半——可能真的结束了。2025年全球内存市场约2200亿美元，2026年预计冲到8900亿美元。这个增量比整个智能手机、PC或服务器市场还大。\n\n2️⃣ **AI是“罪魁祸首”**\nAI对内存的需求是价格不敏感的。一个AI集群的HBM（高带宽内存）用量，比单颗AI芯片暴增1800倍。而全球90%的DRAM产能集中在3家公司，供给极度刚性。当需求暴增遇上供给锁死，价格就只能往上走。\n\n3️⃣ **PC和手机首当其冲**\n供应商优先把产能分配给高利润的AI/服务器市场，消费级内存被挤压。研报预测：2026年PC出货量可能比2025年下降10%以上，智能手机下降13%。而且设备价格会涨，高端机型更受青睐——因为厂商会优先保利润。\n\n4️⃣ *\n\n[... middle omitted ...]\n\nks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should c\n\n[... middle omitted ...]\n\nCanary Wharf\n\nLondon E14 4AD\n\nUnited Kingdom\n\n+44 (0)20 7425 8000\n\n## Japan\n\n1-9-7 Otemachi, Chiyoda-ku\n\nTokyo 100-8104\n\nJapan\n\n+81 (0) 3 6836 5000\n\n## Asia/Pacific\n\n1 Austin Road West\n\nKowloon\n\nHong Kong\n\n+852 2848 5200"
  },
  {
    "id": "R004",
    "title": "Bernstein：韩国设备进口数据揭示的不是周期复苏，而是记忆体结构性扩张的加速",
    "digest": "[wechat_article.md]\n# Bernstein：韩国设备进口数据揭示的不是周期复苏，而是记忆体结构性扩张的加速\n\n半导体设备进口数据，通常被市场视为周期风向标。当韩国5月半导体设备进口同比飙升51%时，许多投资者的第一反应是“周期回来了”。但这份Bernstein研报揭示的图景远比“周期复苏”复杂——它指向的是记忆体领域一次由技术节点跃迁驱动的结构性资本支出扩张，而非简单的需求回暖。理解这一区别，对于判断设备供应链上各家公司的相对受益程度至关重要。\n\n市场之所以容易误读，是因为传统框架下进口激增往往与下游需求旺盛挂钩。然而，Bernstein团队通过拆解进口来源国别和设备品类，发现本轮增长的核心驱动力来自韩国两大记忆体巨头——三星和SK海力士——对1c纳米DRAM节点的激进导入，以及由此带来的光刻强度（litho intensity）显著提升。这不是一个“量”的故事，而是一个“质”的故事。\n\n这份报告最值得关注的判断是：韩国设备进口的强劲势头，正在从总量层面验证记忆体资本开支的结构性上调，但不同设备供应商之间将出现显著分化。光刻设备供应商ASML有望持续受益于高价值量系统的密集交付，测试设备供应商Advantest可能迎来超预期的季度收入，而日本设备商东京电子（TEL）的收入动能则显示出边际放缓的迹象。这种分化，恰恰是投资者需要重新校准预期的地方。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 光刻设备进口创下季度内第二高纪录，ASML在韩收入动能持续强化\n\n韩国从荷兰进口的半导体设备——几乎可以视为ASML光刻系统的代理变量——在5月达到9.28亿欧元，这是有记录以来季度内第二高的单月数字，环比增长28%，同比增幅约150%。Bernstein的回归模型据此估算，ASML第二季度在韩国的系统销售额约为23.1亿欧元，虽然环比下降18%\n\n[... middle omitted ...]\n\nein的后续更新和更多交叉验证数据，持续追踪这一主题的演变。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n韩国半导体设备进口飙51%，背后是啥信号？\n\n韩国半导体设备进口创新高\n\n5月数据解读：存储扩产信号灯亮了\n\n最近一份投行研报拆解了韩国5月半导体设备进口数据，信息量很大👇\n\n📊 整体数据：进口同比+51%，环比-5%\n前5个月累计增速已从4月的37%加速到39%\n说明韩国存储大厂的扩产节奏还在加快\n\n🔍 三大关键信号\n1️⃣ 光刻机：荷兰进口9.28亿欧元，创季度第二高\n环比+28%，同比约+150%\n研报推测Q2韩国将占ASML系统销售的37%\n背后是DRAM 1c节点量产带来的光刻强度提升\n\n2️⃣ 测试设备：日马进口同比+103%，环比+5%\n回归模型暗示某日本测试设备商Q2韩国收入可能环比+84%\n远高于市场预期的+3%——这里是模型推测，实际要看6月数据\n\n3️⃣ 日本设备：CVD/刻蚀/清洗等环比-27%\n模型暗示Q2收入可能环比-15%\n与市场预期的环比持平存在差距\n\n💡 核心逻辑：设备进口与三星+SK海力士合计资本支出高度相关\n虽然Q1资本支出因季节性和基建前置有所回落\n但两家公司已明确指引2026年资本支出大幅增加\n后续设备进口有望持续走强\n\n#学习笔记\n\n[source_mineru.m\n\n[... middle omitted ...]\n\nrmine Milano, CFA\n\n+44 20 7762 1857\n\ncarmine.milano@bernsteinsg.com\n\n![](images/6e399aec375ec079bc08db92c8e6abb4f9fda00ec83db4a2755f2d4851e1994c.jpg)\n\nJack Lin\n\n+852 2123 2683\n\njack.lin@bernst\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R005",
    "title": "Bernstein：美伊和平对印度而言是反弹，不是反转",
    "digest": "[wechat_article.md]\n# Bernstein：美伊和平对印度而言是反弹，不是反转\n\n印度市场正在庆祝一个期待已久的信号：美伊之间可能达成真正的和平协议，霍尔木兹海峡重新开放。油价应声回落至83美元，航空、石油营销公司（OMC）、医疗保健乃至IT板块的情绪迅速升温。但这份Bernstein研报的核心判断是——市场应当区分“乌云散去”和“阳光普照”是两回事。反弹是确定的，但反转的条件远未成熟。真正值得深挖的，不是短期的情绪修复，而是和平协议可能带来的两个结构性变量：伊朗原油制裁豁免，以及恰巴哈尔港的战略价值。这两点，才是决定印度能否从“反弹”走向“重估”的关键。\n\n这份研报发布于一个微妙的时点。此前三个月，中东的和平声明屡屡被证明是短暂的，市场已对“消息面反弹”产生疲劳。但Bernstein认为这次不同——美伊双方官方渠道同步确认，且得到调解方背书，协议的可靠性高于以往。然而，研报同时警告，魔鬼在细节中。双方出于国内政治需要，可能在短期内各自叙事，真正的条款细节需要数周才能明朗。这意味着，当前市场的定价更多基于情绪，而非事实。\n\n对于投资者而言，核心问题不是“要不要参与反弹”，而是“反弹的持续性和深度由什么决定”。Bernstein的答案很明确：真正的催化剂不是海峡重开，而是伊朗原油回归和地缘战略通道的打通。而这两点，恰恰是当前市场讨论最少、定价最不充分的变量。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 霍尔木兹重开对油价的缓解可能低于预期，因为需求侧会同步反弹\n\n油价从高位回落至83美元，市场的第一反应是成本端压力缓解。但Bernstein指出，霍尔木兹海峡重开带来的供给增量，可能很快被需求端的同步复苏所抵消。全球经济活动在战争阴云消散后有望加速，尤其是航空和工业用油需求将回升。因此，油价更可能在一个较窄的区间内波动，而非趋势性下行\n\n[... middle omitted ...]\n\n迎来到知识星球微信群，和我们一起持续追踪这些未解问题的演变。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美伊和谈，印度市场能反弹多久？\n\n封面：印度反弹\n封面副标题：是机会还是陷阱？\n\n最近美伊传出和平协议，中东紧张局势有望缓解。这对印度市场意味着什么？投行研报给出了深度分析。\n\n**1/ 原油大概率区间震荡**\n霍尔木兹海峡重新开放基本确定，原油已跌至83美元。但别指望油价大幅下跌——需求端可能同步回升，反而支撑油价。好消息是，油价大概率不会破百了。\n\n**2/ 短期反弹看这几个方向**\n- 石油营销公司（OMCs）直接受益于油价下跌\n- 航空、旅游板块也是直接利好\n- 医疗保健受益于美国定价压力缓解\n- 中东战后基建重建（能源+水利）可能带动工业股\n- IT板块可能受益于美国支出环境改善\n\n**3/ 但别太兴奋**\n研报强调：这只是乌云散去，不是阳光普照。\n- 估值仍然偏贵\n- 印度在AI贸易中处于不利地位\n- 原油仍可能高于去年\n- 最近燃油/LPG涨价会推高通胀\n- 厄尔尼诺现象确认，季风担忧未消\n\n**4/ 两个更大的催化剂**\n- 伊朗称协议包含原油制裁豁免，若落实，油价可能跌破80美元\n- 查巴哈尔港的使用具有战略意义——连接中亚、降低航运成本\n\n如果原油制裁豁免落地，印度财政赤字有望守住4.3%\n\n[... middle omitted ...]\n\no end military operations, which we believe is a firm one since it has come from official sources of both parties simultaneously, and also confirmed by the ‘mediators’. Will it lead to a long-\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R006",
    "title": "GS：5月中国外汇流入的真实信号被市场低估了",
    "digest": "[wechat_article.md]\n# GS：5月中国外汇流入的真实信号被市场低估了\n\n市场对中国资本流动的讨论，长期停留在“流出压力”的叙事框架里。但GS最新发布的5月外汇数据解读，给出了一个截然不同的信号：中国在5月录得了约500亿美元的净外汇流入，这不仅是连续第二个月净流入，而且结构上发生了值得关注的转变。\n\n这份报告的核心价值，不在于告诉你“流入还是流出”这个结论，而在于它拆解了流入的构成——经常项目依然强劲，但真正值得关注的，是资本金融项目下出现了一些此前数月未曾见到的边际变化。这些变化能否持续，将直接决定人民币资产定价的底层逻辑是否正在被重新书写。\n\n以下是我们基于这份研报的解读与延伸思考。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 5月净流入的核心驱动力仍是贸易顺差，但“结汇意愿”出现了微妙信号\n\nGS偏好的外汇流量指标显示，5月净流入500亿美元，高于4月的370亿美元。其中，经常项目贡献了370亿美元的净流入，货物贸易相关的净流入从4月的470亿美元升至530亿美元。\n\n表面上看，这延续了“出口强劲、顺差扩大”的老故事。但GS报告里一个容易被忽视的数字是：5月的结汇比率降至51%，低于4月的56%，更远低于一季度74%的平均水平。\n\n这意味着什么？企业赚了更多外汇，但选择“持有”而不是“兑换”人民币的比例在上升。从直觉上看，这似乎是一个负面信号——企业不结汇，说明对人民币汇率缺乏信心。\n\n但这里需要做两层思考。第一，51%的结汇比率仍然高于2022-2024年多数月份的水平，说明企业并非在系统性抛售人民币。第二，更重要的是，结汇比率下降的同时，整体外汇流入却在增加，这意味着“不结汇”的量级本身也在扩大——企业手中积累的外汇头寸正在变厚。一旦汇率预期出现拐点，这些“蓄水池”里的外汇可能集中释放，形成人民币升值的脉冲式力量。\n\n这\n\n[... middle omitted ...]\n\n据构建的汇率和利率观察框架。这些内容，不适合在公开渠道展开。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月外汇流入回暖了\n\n外资回来了\n\n5月净流入500亿美元\n\n---\n\n刚刷到某外资投行的5月跨境资金报告，数据挺有意思的。\n\n1/ 整体看，5月净外汇流入约500亿美元，比4月的370亿明显回暖。主要来自三个渠道：即期结售汇、远期交易、跨境人民币流动，三者加起来推高了整体数字。\n\n2/ 经常项目（贸易）仍是主力，5月净流入370亿美元，其中货物贸易贡献530亿净流入，比4月的470亿还多。但有个细节：企业结汇意愿下降了，5月结汇率只有51%，低于4月的56%和Q1的74%。说明出口企业拿到美元后，更愿意留着不换人民币。\n\n3/ 资本项目（证券投资）也有改善。5月净流入70亿美元，虽然比4月的120亿少，但结构变了——外资通过债券通净买入130亿人民币债券，是2025年4月以来首次净买入，主要买的是国债。这意味着外资对中国债券的兴趣在恢复。\n\n4/ 官方外汇储备5月升至3.442万亿美元，剔除估值效应后实际增加390亿。同时商业银行境外净资产也增加了150亿，说明整个金融体系的外汇头寸在扩张。\n\n整体看，5月数据释放的信号偏积极：贸易顺差依然强劲，外资开始回流债市，企业虽然结汇意愿低但没有恐慌性购汇迹象。\n\n[... middle omitted ...]\n\ny.\n\n## Main points:\n\n1. In May, we saw US\\$34bn net inflows via onshore outright spot transactions, and US\\$14bn inflows via freshly entered and canceled forward transactions. Another SAFE dat\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R007",
    "title": "JPM：市场真正低估的不是增长，而是信用脉冲对风格切换的定价权",
    "digest": "[wechat_article.md]\n# JPM：市场真正低估的不是增长，而是信用脉冲对风格切换的定价权\n\n上周五，美联储与中国人民银行几乎同时发布了两组关键数据——美国一季度资金流量表与中国5月社融数据。这不是一个巧合，而是一个信号。对于大多数投资者而言，这两组数据各自指向不同的方向：美国私人部门信用扩张加速，中国社融连续第三个月放缓。但JPM量化策略团队在其最新报告中提出了一个更值得深思的判断：合在一起看，这两组数据共同指向一个方向——Growth风格相对于Value风格仍有空间，但信心的基础正在变薄。\n\n这不是一篇关于宏观预测的报告。这是一篇关于“如何用信用脉冲作为信号，对风格切换进行定价”的报告。JPM构建了一个简单但有效的框架：将美国与中国信用脉冲信号取平均值，作为判断Growth与Value相对表现的领先指标。自2018年以来的回测显示，这一信号的历史命中率为53%，年化超额收益达到9.9%。目前，该信号仍指向超配Growth，但信号强度已显著低于三个月前。\n\n这个判断的核心在于：市场正在定价的，可能不是增长本身，而是信用创造的速度与方向。而这一框架的真正价值，不在于它给出了一个明确的交易信号，而在于它揭示了市场定价中一个被广泛忽视的结构性变量。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 信用脉冲不是宏观指标，而是风险定价的代理变量\n\n大多数投资者关注信用数据时，着眼的是经济增长的领先指标。JPM提供了一个不同的视角：信用脉冲是风险定价的代理变量，尤其对Growth风格的资产定价高度敏感。\n\n这一逻辑链条值得拆解。Growth资产的定价高度依赖远期的现金流折现，而折现率中的风险溢价部分对宏观流动性环境极为敏感。信用脉冲，即私人部门信用创造的边际变化，恰恰是捕捉这种风险溢价波动的有效工具。当信用扩张加速时，风险溢价下降，Growth资产\n\n[... middle omitted ...]\n\n自己的分析框架，从而在不确定性中做出更理性的判断。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中美信贷脉冲发出同一个信号：成长股\n\n成长继续，但边际减弱\n\n中美数据一正一负，但总量依然指向成长\n\n1️⃣ 上周五巧合了，美联储和央行同时放出关键数据。美联储公布的是1Q26资金流量表，央行是5月社融。两套数据拼在一起，正好是中美信贷脉冲的最新状态。\n\n2️⃣ 信贷脉冲是什么？一个宏观视角，用来观察折现率里的风险成分。成长股定价对这东西特别敏感。简单说，信贷扩张期，成长风格往往跑赢价值。\n\n3️⃣ 两边数据方向相反。美国1Q26私人部门信贷继续加速，脉冲从+1.6pp跳升到+2.5pp。中国这边，5月社融连续第三个月放缓，脉冲已经滑到-0.4pp。一个拉，一个拽。\n\n4️⃣ 合起来看，总量还是往上走的，但只是刚刚超过6个月均值。用某外资投行的回测数据，这个信号自2018年以来命中率53%，年化超额收益+9.9%。当前信号依然偏好成长，但信心比三个月前弱了不少。\n\n5️⃣ 成长vs价值，本质是你在押注什么。成长押的是未来现金流折现变便宜，价值押的是现在的东西被低估。信贷脉冲告诉你，宏观环境还在给成长撑腰，但撑得没以前稳了。\n\n欢迎一起讨论，你觉得接下来成长和价值会怎么切换？\n\n#学习笔记\n\n[source_m\n\n[... middle omitted ...]\n\n/China credit data is one of the macro lenses we monitor. We view credit impulse as a proxy for the risky component of the discount rate, to which the pricing of Growth names is highly sensiti\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 14 Jun 2026 06:48 PM HKT\n\nDisseminated 14 Jun 2026 06:48 PM HKT"
  },
  {
    "id": "R008",
    "title": "摩根斯坦利：中国权益市场正在被低估的并非需求，而是供给侧的结构性定价能力",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：中国权益市场正在被低估的并非需求，而是供给侧的结构性定价能力\n\n这份报告发布的时间点值得玩味。2026年6月，MSCI中国年初至今回报为-10%，而MSCI新兴市场同期上涨18%。表面看，中国资产似乎又一次跑输了。但摩根斯坦利亚洲策略团队在题为“Forging New Horizons”的投资者报告中提出了一个与市场情绪截然不同的判断：中国市场的核心叙事正在从“周期性复苏”切换到“结构性供给优势”，而这一切换尚未被全球定价体系充分反映。\n\n报告的核心主张不是中国需求有多强，而是中国在全球AI和能源转型资本开支超级周期中的供给侧地位，正在系统性地重塑其出口竞争力和企业盈利结构。这意味着，投资者如果继续用过去三年“弱复苏、强政策依赖”的框架来看待中国权益，可能会错过一个更根本的变量——中国正在成为全球资本品和电子供应链中不可替代的“供给锚点”。\n\n这份报告提供的新信号在于：中国在全球出口市场的份额不仅没有因供应链多元化而下滑，反而有望在2030年达到16.5%甚至更高。而这一扩张的驱动力，并非传统的低成本制造，而是深度嵌入全球AI基础设施和能源转型的供给能力。以下是我们从报告中提炼出的五层核心洞察，以及一个尚未被完全回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 指数表现掩盖了结构性分化：CSI 300的风险调整后收益才是真正的信号\n\n报告开篇用一组数据直接挑战了“中国资产表现不佳”的流行叙事。从2024年9月至今，MSCI中国总回报为28%，MSCI新兴市场为49%，S&P 500为30%。单看绝对回报，中国确实落后。但摩根斯坦利引入了更精细的衡量维度——夏普比率。\n\n2025年全年，CSI 300的夏普比率为1.44，高于MSCI EM的1.70吗？不，MSCI EM更高。但请注意\n\n[... middle omitted ...]\n\n。我们将基于这份报告以及后续的行业调研，持续更新我们的判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国A股跑赢大盘的秘密\n\nA股韧性从哪来\n\n2026年，A股的风险调整后收益，竟然悄悄超过了全球多数主流市场\n\n最近翻到某外资投行6月的一份中国策略报告，有几个判断挺有意思，和大家聊聊。\n\n1️⃣ 指数表现分化，A股反而更稳\n- MSCI中国年初至今跌了约10%，但沪深300同期涨了5%\n- 从2024年9月至今，沪深300累计涨幅达53%，远超MSCI中国（28%）和标普500（30%）\n- 更关键的是，沪深300的夏普比率（衡量风险调整后收益）在2025年达到1.44，高于MSCI新兴市场的1.70，也高于标普500的0.66\n\n2️⃣ 指数成分结构是关键\n- 看起来MSCI中国表现一般，但拉出细分行业一看，半导体、资本品、技术硬件这些板块其实涨得很好\n- 拖累指数的主要是软件服务（跌35%）和通信服务（跌35%）\n- 换句话说，不是中国没机会，而是指数权重分布没跟上结构变化\n\n3️⃣ 出口链仍是增长锚\n- 全球AI超级周期和能源转型是两大结构性驱动力\n- 中国在电子和可再生能源供应链深度上优势明显，半导体市场预计2026年突破1万亿美元\n- 报告预测，到2030年中国全球出口市场份额可能达到16.5%（\n\n[... middle omitted ...]\n\nt could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.\n\n## For analyst certification and other important disclosures, r\n\n[... middle omitted ...]\n\narantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n© 2026 MS"
  },
  {
    "id": "R009",
    "title": "摩根斯坦利：贸易韧性掩盖了国内需求的深层裂痕",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：贸易韧性掩盖了国内需求的深层裂痕\n\n这份摩根斯坦利在2026年亚洲夏季研讨会上发布的报告，标题本身就浓缩了一个核心矛盾：“更强劲的贸易，更疲弱的国内需求”。这不是一句中性的描述，而是一个正在撕裂中国宏观叙事的张力结构。对于关注中国资产定价的读者而言，真正重要的不是出口数据有多亮眼，而是当外需的强风暂时掩盖了内需的病灶时，资产价格的风险定价是否已经足够充分。\n\n报告提供的最新信号是：2026年5月的数据显示，出口在AI周期和全球科技产业链重构的推动下出现了罕见的广度改善，电子集成电路、计算机、手机等品类同比增速惊人。但与此同时，私人信贷需求却在全面恶化——5月新增短期居民贷款为负70亿元，新增中长期居民贷款同样为负50亿元，均远低于过去五年的同期均值。这两个方向截然相反的指标同时出现，意味着中国经济正处于一个极其特殊的分化阶段：外循环的动能正在加速，而内循环的收缩尚未触底。\n\n这份报告的价值，不在于它重复了“出口好、内需弱”的共识，而在于它用数据揭示了这种分化的结构细节、政策应对的局限性，以及中长期再平衡所需要的改革前提。以下是我们从这份报告中提炼出的五个核心洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 出口的改善不是简单的周期性回暖，而是科技产业链重构带来的结构性红利\n\n报告中的一张图清晰展示了出口改善的广度：2026年4月至5月，中国出口增速在多个品类上出现跃升。电子集成电路的同比增速从4月的约100%进一步攀升至5月的约110%，计算机从45%升至65%，手机从10%升至45%。即便是此前表现疲软的品类，如精炼石油产品、塑料制品，也在5月转正或加速。\n\n但真正值得关注的不是这些数字本身，而是它们背后的驱动力。报告明确指出，全球AI周期正在驱动中国贸易增长。这意味着当前的出口改善并非传统\n\n[... middle omitted ...]\n\n，以及我们对后续政策路径的推演，欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n出口撑住了，内需还在磨底\n\n出口强，内需弱\n\n某外资投行最新亚太研报划重点，一张图看懂当前经济结构分化👇\n\n1️⃣ 出口全面回暖\n- 全球AI周期拉动中国贸易，5月电子集成电路出口同比+110%\n- 计算机+65%，手机+45%，汽车+40%\n- 非技术类出口也在改善，塑料、家具、纺织品转正\n\n2️⃣ 内需信贷持续收缩\n- 5月居民短期贷款净偿还700亿，中长期贷款净偿还500亿\n- 企业中长期贷款+债券融资仅1450亿，远低于5年均值5350亿\n- 居民仍在去杠杆，楼市回暖只是结构性\n\n3️⃣ 通胀传导有限\n- PPI环比回落，主要受石油价格脉冲减弱拖累\n- 核心CPI仍在低位，6月/6月年化仅0.8%\n- 非有色、煤炭等上游涨价未能传导到消费端\n\n4️⃣ 财政节奏有望加速\n- 截至5月政府债券仅使用41%（去年同期46%）\n- 预计三季度加快支出，重点投向“六网”建设\n- AI算力、互联网数据中心、智能电网是核心方向\n\n5️⃣ 供给过剩问题待解\n- 投资增速放缓但不够快，2026年固投预计+5.9%\n- “全国统一市场”和“反内卷”方向正确，但落地难\n- 地方激励偏向生产，消费端改革仍需推进\n\n6️⃣ 资\n\n[... middle omitted ...]\n\nry>line chart</summary>\n\n| Month   | Exports: Tech | Imports: Tech | Exports: Non-Tech | Imports: Non-Tech |\n|---------|---------------|---------------|-------------------|-------------------|\n\n[... middle omitted ...]\n\narantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n© 2026 MS"
  },
  {
    "id": "R010",
    "title": "摩根斯坦利：ABF载板供需拐点已至，真正稀缺的不是产能，是客户锁定的产能",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：ABF载板供需拐点已至，真正稀缺的不是产能，是客户锁定的产能\n\n当一家欧洲载板厂商宣布将资本支出从4亿欧元大幅上调至10-12亿欧元，同时EBITDA利润率指引从25-29%直接跳升至32-37%，市场的第一反应往往是“供给要过剩了”。但摩根斯坦利这份关于AT&S马来西亚扩产的研报给出了截然相反的判断：这不是供给过剩的信号，而是供给结构性短缺提前到来的确认。\n\n这份研报最值得关注的洞察，不在于AT&S上调了业绩指引，而在于一个关键细节——AT&S追加的15-20亿欧元投资，是在现有厂区增加生产线，而非新建工厂。这意味着新产能将在2027年3月前落地。而摩根斯坦利此前判断ABF载板将从2027年起进入供给短缺周期。两件事放在一起看，结论清晰：短缺不是被推迟了，而是被提前证实了。\n\n市场正在犯一个典型错误——把“产能扩张”等同于“供给过剩”，却忽略了这次扩张的底层逻辑已经改变：客户承诺前置、资本开支锁定、产能被预购。这不再是2018-2020年的产能竞赛，而是AI/HPC需求驱动下的供给再定价。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮扩张的核心信号不是产能，而是客户承诺的深度和结构\n\nAT&S此次扩产的资本开支高达15-20亿欧元，几乎是此前指引的三倍。但真正让这份报告值得细读的，不是金额本身，而是资金来源——AT&S明确表示，这笔投资“fully supported and financed by long-term customer commitments”。\n\n这意味着什么？在传统载板行业，产能扩张通常是厂商基于需求预测做出的风险决策。景气时扩产，低谷时承担闲置成本。但这次，客户——AMD和另一家大型科技公司——直接为产能买单。这不是“厂商赌需求”，而是“客户锁产能”。\n\n[... middle omitted ...]\n\n关公司的估值模型细节，以及我们对替代技术演进路线的持续跟踪。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nABF基板扩产，AI需求在加速\n\n**封面标题**\n扩产信号\n\n**封面副标题**\nAI需求拉动，ABF基板新周期\n\n---\n\n刚看到一份研报，AT&S宣布在马来西亚Kulim扩产，专攻AI/HPC的IC基板。\n\n这次投资15-20亿欧元，背后有AMD和另一家大客户长期订单支持。关键是，AT&S直接把FY26/27的营收增长指引从30-35%上调到45-55%，EBITDA利润率也从25-29%提到32-37%。\n\n**1. 为什么值得关注？**\n因为这次扩产是在现有厂房加产线，不是新建工厂。按研报推测，新产能预计在2027年3月前上线。这意味着——需求比市场预期的更强劲。\n\n**2. 对产业链的影响**\n研报判断，2027年起ABF基板供给会出现缺口。这对几家台系厂商是正面信号：欣兴、南电、臻鼎都被给出超配评级。\n\n**3. 几个核心观察点**\n- 上游扩产节奏加速，说明AI服务器对高端基板的需求在持续放大\n- 扩产方式从新建工厂改为加产线，代表厂商更看重投产效率\n- 客户直接参与融资，显示供应链绑定在加深\n\n**4. 需要留意的风险**\n研报也列出了几个变数：技术路线变化（比如CoWoP不需要基板）、需求突然\n\n[... middle omitted ...]\n\n from €0.4bn, with significantly positive op FCF.\n\nOur thoughts: AT&S raising guidance for FY26/27 on the new capacity announcement implies it will come online by EoFY, or March 2027, as it ap\n\n[... middle omitted ...]\n\naxy Co Ltd (2455.TW)</td><td>E (09/11/2023)</td><td>NT$352.00</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R011",
    "title": "美国银行：市场真正低估的不是AI泡沫，而是通胀二次探底对仓位结构的重塑",
    "digest": "[wechat_article.md]\n# 美国银行：市场真正低估的不是AI泡沫，而是通胀二次探底对仓位结构的重塑\n\n这份报告的核心判断，不是关于AI是否过热，而是关于一个更根本的、正在发生的结构性转变：全球基金经理正在从一个“拥抱风险、追逐增长”的仓位状态，转向一个“警惕通胀、防御性调整”的新阶段。美国银行（BofA）2026年6月的全球基金经理调查（FMS）显示，尽管市场情绪依然偏多，但最关键的信号并非AI的拥挤度创下历史新高，而是投资者对利率预期的剧烈转向，以及由此引发的仓位再平衡。这意味着，未来几个月的资产定价逻辑，可能将从“增长叙事”切换为“利率与通胀叙事”。\n\n为什么现在重要？因为市场正处于一个微妙的“共识分歧”点。一方面，宏观情绪在改善，全球增长与利润预期均创三个月新高；另一方面，对利率的预期却急转直下，认为未来12个月美联储将加息的基金经理占比从16%飙升至40%，为近四年最高。这种“增长向好、利率向上”的组合，在历史上往往不是风险资产的顶部，但却是风格切换和波动加剧的温床。美国银行自己的牛熊指标已升至8.9，触发“卖出信号”，但报告同时指出，这并非“大顶”的信号——真正的顶部通常由债券市场和选民情绪共同确认。\n\n这份调查的价值在于，它提供了一个清晰的“市场温度计”和一套可验证的观察框架。它告诉我们，现在的拥挤交易在哪里，哪些资产正在被抛弃，以及哪些角落可能孕育着反共识的机会。但报告也留下了一些关键问题，比如AI的“繁荣”阶段还能持续多久，以及通胀二次探底的风险是否被充分定价。这些问题，正是我们接下来要深入拆解的。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 利率预期的剧烈转向，正在成为仓位调整的核心驱动力\n\n这份调查中最具冲击力的数据，不是AI的拥挤度，而是利率预期的变化。认为美联储将在未来12个月内至少加息一次的基金经理占比，从5\n\n[... middle omitted ...]\n\n，以及全球宏观数据的边际变化，一起寻找那些被市场忽视的信号。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n基金经理情绪温度计：6月读数\n\n基金经理的“牛市温度”读数\n\n6月全球基金经理调查出炉，情绪依然高亢但略降温。现金比例从3.9%回升至4.1%，整体看多情绪从极端高位小幅回落，但历史数据表明这还不是风险资产的“大顶”。\n\n1/ 宏观与利率：乐观但未过热\n全球增长与盈利预期升至3个月新高，但并未到危险水平。最大变化在利率端：40%的基金经理预计未来12个月美联储至少加息一次（5月仅16%），利率预期创2022年9月以来最高。对本周FOMC会议，55%预计“鹰派按兵不动”，33%预计“鸽派按兵不动”。\n\n2/ 风险与拥挤交易：两大担忧\n最大尾部风险：二次通胀（34%）和AI泡沫（28%）。最拥挤交易：做多全球半导体，80%的选择创调查历史新高。当被问及AI股票处于哪个投资周期阶段，56%说“繁荣期”（FOMO驱动更多买家），21%说“狂热期”（价格/估值进入危险区）。\n\n3/ 仓位变化：夏季减仓\n全球股票超配从50%降至38%，科技超配从33%降至26%。基金经理削减欧洲股票至2024年12月以来最低配，买入日本、材料、银行。美元空头头寸收窄至2025年3月以来最小。黄金首次自2024年2月被认为估值合理。\n\n4\n\n[... middle omitted ...]\n\nr interest rates now highest since Sep'22; on the Fed, 40% (was 16%) forecast hikes in next 12 months, and 55% expect “hawkish hold” from Warsh at tomorrow’s FOMC vs. 33% predicting “dovish ho\n\n[... middle omitted ...]\n\nw in accordance with firm policies.\n\nNeither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information."
  },
  {
    "id": "R012",
    "title": "DB：地缘风险溢价退潮，最被低估的不是避险资产，而是这些被错杀的货币",
    "digest": "[wechat_article.md]\n# DB：地缘风险溢价退潮，最被低估的不是避险资产，而是这些被错杀的货币\n\n地缘政治风险的消退，往往不是均匀地提振所有资产。真正有意义的交易，不是追涨那些已经定价了“和平”的品种，而是寻找那些风险溢价尚未完全回吐、基本面却在同步改善的货币。DB最新发布的这份外汇研究报告，核心判断很直接：美国与伊朗达成和平协议后，霍尔木兹海峡的油轮通行效率将直接决定哪些货币可以迎来系统性重估。报告筛选出了四支货币——瑞典克朗、南非兰特、智利比索和印度卢比——并给出了明确的交易逻辑。但真正值得决策者关注的，不是这些货币的短期方向，而是这份报告揭示的一个更深层问题：市场对“和平红利”的定价，可能仍然停留在情绪层面，而忽略了供给端成本结构变化的长期含义。\n\n这份报告发布于2026年6月15日，时间点本身就值得注意。它不是在地缘冲突爆发初期、市场恐慌最严重时发布的应急分析，而是在局势已经明朗、和平协议即将落地的窗口期，系统性地重新评估汇率定价。这种时间选择本身就说明，DB认为市场对这一轮地缘风险消退的定价，仍然存在较大的结构性的偏差。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮变化真正考验的是企业能否把规模转化为议价权\n\nDB筛选货币的逻辑，表面上看是“油价敏感度”和“经常账户改善”，但底层逻辑其实是一个更根本的经济学命题：当一个经济体长期承受的地缘风险溢价突然消失，哪些国家能最快地把成本下降转化为竞争力提升？答案不是那些最依赖石油进口的国家，而是那些进口成本下降的同时，出口竞争力也在同步改善的国家。\n\n瑞典克朗被列为G10中的首选交易，原因就在这里。报告指出，瑞典经济目前仍具有超过2%的增长潜力，财政刺激持续，且正在受益于全球国防开支上升。但更关键的是，克朗是自3月以来对美元表现最弱的发达市场货币。这意味着，即便和平协议落地，克\n\n[... middle omitted ...]\n\n信群里继续交流，我们一起拆解这份报告中的图表和未展开的假设。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美伊和谈，谁最受益？\n\n谁在受益？\n\n这四类货币，或受益于油路疏通\n\n某外资投行最新研报指出，如果美伊达成和平协议，霍尔木兹海峡的油轮能顺畅通行，部分货币将显著受益。\n\n1️⃣ 瑞典克朗（SEK）——欧洲的“高贝塔”选手\n作为能源进口国，且经济与全球增长高度相关，中东局势缓和将让瑞典经济在下半年跑赢欧洲其他地区。目前克朗是G10里对美元表现最弱的货币，有补涨空间。\n\n2️⃣ 南非兰特（ZAR）——多重利好叠加\n油价风险溢价消退、黄金可能反弹、高实际利率、国内基本面持续改善。模型显示兰特仍被低估，且南非央行有维持鹰派倾向的动力，提供额外支撑。\n\n3️⃣ 智利比索（CLP）——被油价压制的价值洼地\n这是拉美表现最差的货币之一，但若油价回落、铜价维持高位，经常账户赤字有望在年底前收窄。估值和持仓数据都支持比索进一步走强。\n\n4️⃣ 印度卢比（INR）——油价敏感+空头回补\n印度是油价下跌的最大受益者之一。目前卢比空头头寸只回补了约三分之一，还有空间。印度央行已采取强力措施吸引短期资金流入，并可能推动债券纳入全球指数。\n\n整体来看，这些货币的多头头寸可以搭配美元或欧元来做组合，具体取决于对美联储后续路径的判断。\n\n#\n\n[... middle omitted ...]\n\nhalf of the year\n\nZAR: An unwind in oil risk premia, potential rebound in gold, high real-rate buffer and still-improving domestic backdrop should all help.\n\nCLP: The currency has been one of \n\n[... middle omitted ...]\n\nk, NY 10019</td><td>Tower,</td><td></td></tr><tr><td>Tel: (44) 20 7545 8000</td><td>Tel: (1) 212 250 2500</td><td>Singapore 048583</td><td></td></tr><tr><td></td><td></td><td>Tel: +65 6423 8001</td><td></td></tr></table>"
  },
  {
    "id": "R013",
    "title": "摩根斯坦利：油价真正的风险不是地缘缓和，而是供需错位的结构性固化",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：油价真正的风险不是地缘缓和，而是供需错位的结构性固化\n\n这份报告最值得认真对待的判断，不是霍尔木兹海峡即将重新开放，而是：即便中东供应恢复，市场依然面临一个比想象中更顽固的供需错位格局。摩根斯坦利在美伊谅解备忘录签署后迅速下调了近两个季度的布伦特油价预测，3季度从100美元调至90美元，4季度从95美元直降至80美元。但真正值得推敲的，不是这10-15美元的调整幅度，而是调整背后的逻辑链条——报告揭示了一个比“地缘政治溢价消退”更深刻的结构性问题。\n\n当前市场最容易被误解的地方在于：人们倾向于把油价疲软归因于霍尔木兹海峡即将重新开放这一预期，但报告通过大量实物市场数据证明，物理原油市场的疲软早在政治突破之前就已经形成，且其驱动因素——美国出口高企与中国进口低迷——短期内看不到逆转迹象。这意味着即便中东供应恢复节奏符合预期，油价的上行空间也可能比多数人想象的更窄。\n\n这份报告发布的时间点很关键。美伊备忘录签署于6月14日，比摩根斯坦利此前假设的“7月底”提前了约两周。正是这个时间差，让机构得以重新审视此前预测中隐含的一个关键假设：在供应恢复之前，美国出口下降和中国进口回升能否为市场提供缓冲。现在来看，这个缓冲机制不仅没有启动，反而在持续恶化。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 生产恢复的时间表提前了，但真正决定油价的不是这个变量\n\n摩根斯坦利将中东产量恢复的时间线整体前移了约1-2周。按照最新估算，7月中旬开始恢复，9月恢复50%，12月恢复80%，剩余部分在2027年初完成。这个节奏看起来不算慢，但报告真正想表达的是：供应恢复的速度本身并不是当前油价的定价核心。\n\n关键在于，即便在日均约1100万桶的中东原油产量处于停产的背景下，实物市场已经出现了反常的疲软。布伦特现货价格、迪拜升贴水\n\n[... middle omitted ...]\n\n真正有价值的不是预测本身，而是预测背后的逻辑链条和未解问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n霍尔木兹刚松动，油价就要变天？\n\n油价逻辑要重写了\n\n某外资投行刚刚更新了油价预测，核心逻辑很简单：霍尔木兹海峡的紧张局势提前缓解，但短期市场没那么快收紧。\n\n1️⃣ 协议落地比预期早了两周\n美国与伊朗达成初步谅解备忘录，虽然细节没全公布，但核心是停火+开放海峡+60天核谈判。之前投行模型假设“7月底才谈成”，结果提前到6月中旬。\n\n2️⃣ 产量恢复需要时间，但节奏在加快\n清除水雷、重建航运信心、让油轮重新回到波斯湾——这些都需要时间。新预测是：7月中旬开始恢复生产，9月回到50%，12月回到80%，剩余部分要等到2027年初。比之前的节奏快了约1-2周。\n\n3️⃣ 一个诡异的矛盾：供给中断但现货走弱\n尽管中东每天有约1100万桶的产量被关停，但现货市场却在走弱。未售出的原油货盘高于正常水平，从西非到北海到俄罗斯ESPO，到处都有卖不动的迹象。\n\n4️⃣ 两个“缓冲器”在起作用\n美国出口比去年高出约400万桶/天，中国进口则减少了约600万桶/天。这两个因素叠加，相当于给全球市场“释放”了约1000万桶/天的宽松空间。而且从已知油轮轨迹看，6月中国进口可能比5月更低。\n\n5️⃣ 投行调低短期油价预测\n新预测：\n\n[... middle omitted ...]\n\n be restored; we see 50% of production back by Sept, and 80% by Dec, slightly faster than before  \nDespite the disruption, a broad range of indicators has signaled weakness in physical oil mar\n\n[... middle omitted ...]\n\narantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n© 2026 MS"
  },
  {
    "id": "R014",
    "title": "GS：AI ASIC仍是首选主题，但市场低估了CPU和下一个供应链瓶颈的定价权",
    "digest": "[wechat_article.md]\n# GS：AI ASIC仍是首选主题，但市场低估了CPU和下一个供应链瓶颈的定价权\n\n当大多数投资者还在追问AI需求能否持续时，一份来自GS的最新路演反馈显示，对话的焦点正在发生深刻的转移。在刚刚结束的美国投资者路演中，GS团队与超过35位机构投资者进行了交流。一个清晰的信号是：市场情绪依然高度建设性，AI ASIC（专用集成电路）继续是最受追捧的投资主题。但真正值得关注的，不是需求本身是否强劲，而是讨论的层次已经进化到了下一个阶段——CPU需求、供应链定价权以及超大规模资本支出的可持续性。\n\n这份报告的洞察力不在于重复“AI很好”，而在于它捕捉到了一个关键转折：投资者正在从“要不要买AI”转向“买谁能在下一阶段继续增长”。增量资本的配置正变得高度挑剔，半导体持仓已经成为许多机构的最大仓位之一。这意味着，能够继续证明盈利增长可持续性的公司，才能获得进一步的资本青睐。\n\n在众多讨论中，GS提炼出了四个最核心的投资者关切：AI供应链的下一个瓶颈在哪里、生态系统的定价权如何分配、哪些公司能在未来几年维持超速增长、以及市场过热的下行风险是什么。本文将基于这份报告，拆解这些问题的逻辑层次，并指出报告尚未完全回答的关键变量。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 投资者的关注点已从AI需求转向货币化验证和资本支出可持续性\n\n一个反复出现的问题是：当前AI投资周期的可持续性如何？这并非空穴来风。超大规模云服务商（CSP）正在加速资本支出，而投资者开始追问这些投入何时能转化为可观的回报。GS注意到，谷歌近期的融资活动引发了显著关注。历史上，美国投资者倾向于将外部融资视为过度投资或泡沫行为的信号。但情绪正在演变——越来越多的投资者开始将谷歌的融资能力视为对长期AI货币化机会的信心标志。\n\n这一变化意味着什么？它表明市场正在\n\n[... middle omitted ...]\n\n开。欢迎来星球微信群里继续讨论，一起拆解这份报告的未尽之处。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI芯片之后，下一个机会在哪？\n\n📌 别只盯着GPU了\n\n上周和某外资投行一起跑了趟美国，跟35+机构投资者聊了一圈。大家的共识很明确：AI ASIC依然是心头好，但讨论方向已经变了。\n\n1️⃣ 从“需求有没有”到“钱能不能赚回来”\n投资者不再只是问“AI需求大不大”，而是开始认真算账：CSP（云服务商）的资本开支能撑多久？Google发债融资，以前大家觉得是泡沫信号，现在反而解读为对AI变现的信心。风向真的变了。\n\n2️⃣ CPU意外成为新焦点\nAgentic AI（智能体AI）的推理需求，让CPU开始被重新定价。以前觉得CPU只是配角，现在投资者开始认真研究Aspeed和WinWay这类纯CPU标的。尤其是WinWay，研报预测其约40-50%收入已来自CPU（含x86和ARM），但市场还没完全反应过来。\n\n3️⃣ 台积电：利润预期可能还是太保守\n投资者普遍认为台积电有定价权，但奇怪它为什么不更激进涨价。研报观点是：台积电习惯年度调价，但投资者可能低估了它在产能瓶颈突破、产品组合优化上的利润弹性。二季度财报前，利润超预期可能会是催化剂。\n\n4️⃣ 联发科：ASIC故事才刚开始\n很多投资者对联发科的AI A\n\n[... middle omitted ...]\n\ng power across the supply chain, and the sustainability of hyperscaler capital spending.\n\nFollowing the strong performance of AI-related stocks over the past 12 months, many investors highligh\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R015",
    "title": "美国银行：市场真正低估的不是需求，而是AI定价权从算力向硬件的转移",
    "digest": "[wechat_article.md]\n# 美国银行：市场真正低估的不是需求，而是AI定价权从算力向硬件的转移\n\n这份6月发布的美国银行亚洲基金经理调查，捕捉到了一个关键信号：投资者对AI的乐观情绪并未消退，但他们的仓位结构正在发生一次静默但深刻的重组。41%的受访者仍然没有对AI交易的下行风险做任何对冲，而与此同时，印尼已经取代印度成为最不受欢迎的市场，科技硬件在仓位中的权重首次超过半导体。这些数据点合在一起指向一个核心判断：市场正在将AI叙事从“算力军备竞赛”重新定价为“硬件落地周期”，而多数投资者尚未完全理解这一转变对区域配置和行业选择的含义。\n\n这并不是说AI泡沫即将破裂。恰恰相反，调查显示只有9%的投资者认为AI对股市的正面影响已经完全被定价，41%认为“大致合理”，另有41%认为“部分被定价”。关键分歧在于：AI的第二波受益者可能不再是第一波中的那些名字。美国银行的这份报告提供了足够的截面数据来支撑这一判断，但报告本身并未将其提炼为可操作的框架——这正是本文试图补全的部分。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 能源安全焦虑的骤降正在释放被压抑的增长预期，但市场对这一传导链条的定价仍不充分\n\n调查中最引人注目的变化不是仓位，而是情绪底层的宏观变量。4月份有91%的受访者表示对亚太地区的能源安全问题“高度或极度担忧”，到6月这一比例骤降至18%。与此同时，“中度担忧”成为主流观点，占比68%。这一变化的速度和幅度在调查历史上都极为罕见。\n\n能源安全担忧的消退直接反映在增长预期上。亚太（除日本）的企业盈利预期在6月进一步走强，净看多比例达到50%，远高于长期均值。更值得注意的是，认为“共识盈利预测过高”的比例已降至历史第14百分位——这意味着投资者不再认为当前盈利预期存在系统性高估。\n\n这里的逻辑链条是清晰的：能源成本的不确定性曾是压制\n\n[... middle omitted ...]\n\n期分享完整报告的解读和原始图表，以及基于这些数据的实时讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n亚洲基金经理悄悄调仓了\n\n📊 6月调研速报\n\n最近某外资投行的6月亚太基金经理调研结果出来了，有几个挺有意思的变化👇\n\n**1. 能源焦虑大降温**\n4月时91%的人还高度担心能源安全，6月这个比例直接降到18%。现在68%的人只是“轻度担忧”。情绪修复速度很快。\n\n**2. AI交易的分化**\n41%的人对AI交易没做任何对冲，继续拿着。另外41%的人已经在往其他板块转。AI的积极影响，只有9%的人觉得已经充分定价了——大部分人还认为有空间。\n\n**3. 地区偏好变了**\n印尼取代印度，成了最不受待见的市场。北亚依然是心头好。台湾（41%）继续是AI周期的最大受益者，美国也获得更多关注。\n\n**4. 板块轮动很清晰**\n亚太（除日本）来看，科技硬件比半导体更受青睐，金融服务成了新宠。资金从材料和可选消费（除零售）流出，转向金融和电信。日本市场，科技硬件（41%）已经和银行并列第二受欢迎的板块了。\n\n**5. 日本市场新看点**\n41%的人认为盈利是日本股市的关键驱动力，27%的人关注政策正常化。64%的人预期6月日本央行会加息。\n\n整体来看，基金经理们对亚太（除日本）未来12个月的预期回报率在6%左右，和历\n\n[... middle omitted ...]\n\n broadly in line with historical norms. AI upside still appears underappreciated, with only $9\\%$ of FMS investors believing the positive impact of AI on equities is more than fully priced in.\n\n[... middle omitted ...]\n\nw in accordance with firm policies.\n\nNeither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information."
  },
  {
    "id": "R016",
    "title": "GS：中国券商真正的结构性机会不在A股交易量，而在香港的资产负债表扩张",
    "digest": "[wechat_article.md]\n# GS：中国券商真正的结构性机会不在A股交易量，而在香港的资产负债表扩张\n\n过去一个月，中国券商股A股和H股分别上涨7%和5%，同期银行股仅上涨1%和3%。市场习惯性地将这一涨幅归因于IPO回暖或交易量放大，但GS最新发布的中国券商与资管行业研报提出了一个更值得深思的判断：券商板块相对于银行的结构性吸引力，核心驱动力并非周期性收入反弹，而是一场发生在资产负债表层面的、由香港业务驱动的ROE扩张。\n\n这个判断如果成立，意味着当前市场对券商股的定价逻辑需要重新校准。传统上，投资者习惯于把券商当作“看天吃饭”的贝塔品种，用日均交易量、IPO规模等流量指标来线性外推盈利。但GS的报告清晰地展示了一个正在发生的结构性变化：头部券商正在通过资本注入和杠杆提升，系统性地将香港子公司的ROE拉升至集团平均水平的近两倍，从而推动集团整体回报率的持续改善。\n\n以下，我们基于这份研报的核心逻辑，拆解这一结构性机会的底层支撑、关键证据以及尚未被市场充分定价的变量。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 银行与券商的分化焦点已从“谁增长更快”转向“谁的资产负债表更有定价权”\n\nGS在报告开头就点明了一个行业层面的范式转换：随着银行体系贷款增速放缓，盈利增长已不再是银行估值的首要决定因素，投资者的关注点已转向资产负债表的韧性和资本实力。这意味着，银行股的估值框架正在从P/E向P/B回归，而P/B的核心驱动力是资产质量和资本回报率。\n\n与此同时，券商板块正处于一个截然不同的叙事中。券商并不直接承担信用风险，其资产负债表扩张的核心驱动力是杠杆——用自有资本撬动更高的回报。GS覆盖的三家头部券商（CICC、CITIC、广发证券）的集团平均杠杆约为6倍，但其香港子公司的平均杠杆高达11倍，几乎是集团水平的两倍。更重要的是，这些香港子公司的\n\n[... middle omitted ...]\n\n？我们将在社群中分享完整的研报原文、核心图表和更细致的拆解。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n券商正在从“看贷款”转向“看香港”\n\n券商 vs 银行：谁更值得关注？\n\n近期投行研报明确表示，更看好券商而非银行。逻辑很清晰：银行靠贷款增长的时代过去了，市场现在更关注资产负债表的质量；而券商正处在盈利修复+结构改善的双重轨道上。\n\n1️⃣ 香港业务成为ROE提升的核心引擎\n头部券商都在加码香港业务，因为海外杠杆率更高、回报也更好。数据显示，三家主要券商的海外子公司平均杠杆约11倍，而集团整体只有6倍；海外ROE平均16%，集团仅9%。CICC管理层也明确提出，中期ROE目标上调至13-15%，主要靠香港业务驱动。\n\n2️⃣ IPO回暖+AI热度，双重催化\n港股IPO市场明显复苏，2025年新上市公司首月平均回报约40%，头部券商手里还有超过180单IPO储备。同时AI主题带动交易活跃度，券商从中赚取佣金、衍生品和资本服务收入。CICC认为，只要AI主题持续、利率环境友好，交易量不会大幅下滑。\n\n3️⃣ 别被“投资收入”迷惑\n券商参与IPO和科创板投资虽然能短期增厚利润，但历史数据显示，这类收入波动极大（2020-2023年，投资收入增速从+265%到-72%），而且不会提升估值倍数。市场真正看重的，是杠杆\n\n[... middle omitted ...]\n\nking system, earnings growth is no longer the primary determinant of bank valuations; instead, investor focus has shifted toward balance sheet resilience and capital strength. In this context,\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R017",
    "title": "GS：市场低估了“城市更新”作为中国房地产下行缓冲器的真实权重",
    "digest": "[wechat_article.md]\n# GS：市场低估了“城市更新”作为中国房地产下行缓冲器的真实权重\n\n当市场目光仍聚焦在周度成交数据的“平台期”时，一份来自GS的最新周报揭示了一个更值得关注的信号：中央层面对城市更新的资金支持正在从框架走向明细。这或许才是当前房地产叙事中最被低估的结构性变量。\n\n这份报告的核心判断并非关于6月销售能否反弹，而是关于政策供给侧的“再定价”。在成交量与情绪双双进入平台期的背景下，GS分析师王逸团队用一周的篇幅，详细拆解了发改委、财政部在“十五五”城市更新框架下的资金分配逻辑。这不仅仅是政策例行通报，它可能正在重塑开发商资产价值的底层评估逻辑。\n\n对于高净值读者和产业决策者而言，当前需要追问的不是“市场何时见底”，而是“当政策资金从万亿级走向落地，哪些企业真正具备吸收这些红利的资产负债表能力”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 成交量的“平台期”恰恰验证了政策加码的必要性\n\nGS周报的数据本身并不令人兴奋：第24周新房销售面积环比微增1%，同比持平；二手房成交面积环比持平，同比微增1%。这是一个典型的“平台期”信号——市场既没有进一步恶化，也没有出现趋势性好转。\n\n但这份数据背后的含义，比表面数字更重要。GS跟踪的约75个城市数据显示，6月至今新房销售面积中位数环比下降17%，同比下降25%。这意味着，如果没有外部变量的介入，市场自发修复的动力正在衰减。二手房市场虽然相对活跃（YTD同比+1%，较2024年水平+22%），但中介价格预期指数（CSI）环比下降0.9个百分点，卖方挂牌价格预期（CAI）虽然稳定，但中介情绪已经先行走弱。\n\n数据传递的清晰信号是：市场正处在一个需要外力打破的均衡点。而这个外力，GS认为正是城市更新的资金落地。\n\n![研报原图 2](assets/source_image_02\n\n[... middle omitted ...]\n\n产估值，以及当前估值水平下哪些标的可能具备“政策期权”价值。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n楼市新钱到账：257亿专项用于旧改\n\n旧改资金到位\n\n257亿超长期国债加码\n旧改+地下管网获重点支持\n\n最近某外资投行发布了中国地产周报，核心信息是：旧改资金终于有了更清晰的落地路径。简单拆解一下👇\n\n1️⃣ **资金规模明确**\n- 97亿中央预算内投资，专门用于老旧小区和危房改造，覆盖约800万户\n- 1600亿超长期特别国债（同比增加250亿），专攻地下管网升级\n- 50个重点城市已获补贴支持，2026年再增15城\n\n2️⃣ **市场表现平淡**\n- 新房成交量环比+1%，同比持平\n- 二手房成交量环比持平，同比+1%\n- 整体看，6月成交可能同比-7%（vs 5月-2%）\n- 卖家价格预期稳定，但中介信心略有下滑\n\n3️⃣ **库存压力仍存**\n- 库存去化周期27.8个月（5月均值28.5个月）\n- 新房开工5月预计同比-20%+（根据土地成交和水泥出货量推算）\n- 竣工5月预计同比-17%（根据浮法玻璃供需模型）\n\n4️⃣ **开发商估值**\n- 覆盖的国企开发商股价平均-1%\n- 民企/其他国企股价平均+2%/持平\n- 整体交易在0.4-0.5倍2026年市净率\n\n我的观察：这轮资金落地更像是\n\n[... middle omitted ...]\n\nultra-long-term treasury bonds (up Rmb25bn yoy) dedicated to underground pipeline upgrades. Meanwhile, the MOF reaffirmed its commitment to subsidy programs in key cities (15 selected for 2026\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R018",
    "title": "NOM：油价暴跌不是短期交易，而是亚洲资产重新定价的起点",
    "digest": "[wechat_article.md]\n# NOM：油价暴跌不是短期交易，而是亚洲资产重新定价的起点\n\n市场正在用交易员的思维理解美伊和平协议——油价跌了，能源进口国受益，这没错。但这份NOM研报真正值得关注的判断是：油价下行对亚洲的影响远不止于通胀和经常账户的数字改善，它正在改变三个更根本的结构——央行政策路径的重新校准、AI资本开支与能源成本下降的叠加效应、以及区域内国家之间“受益程度”的显著分化。\n\n如果只看油价从100美元以上跌到83美元以下这个结果，你可能会认为这是一个短期交易机会。但NOM的分析框架告诉我们，当油价在80美元附近企稳，2026年全年均价将从基准假设的93.9美元降至85.4美元，下半年油价将比当前假设低约15%。这意味着的，不是一个月的数据波动，而是一个季度的宏观假设重置。\n\n更关键的是，这份报告在“大家都受益”的叙事下埋了一条暗线：受益的程度、方式、时间差，才是决定投资回报的核心变量。泰国、菲律宾、印度、韩国被列为最大赢家，但背后的逻辑完全不同——有的是进口账单下降，有的是通胀快速回落，有的是经常账户顺差扩大，还有一个可能享受“双重红利”。这些差异，才是资产定价的关键。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 油价每跌10%，亚洲的宏观画面就换一次底色，但效果不是同步的\n\nNOM用一组清晰的弹性系数告诉我们油价对亚洲经济的传导路径。每10%的油价下跌，平均提升亚洲经常账户约0.3%的GDP，压低通胀0.2-0.3个百分点，同时对增长和财政也有边际正向贡献。\n\n但这些数字的平均值掩盖了最重要的信息：国别差异。泰国每10%油价下跌对经常账户的改善是0.5个百分点，是所有亚洲经济体中最大的；印度是0.4个百分点，韩国是0.3个百分点。而在通胀端，印度和菲律宾的弹性最大，每10%油价下跌可压低通胀0.5个百分点。\n\n[... middle omitted ...]\n\n告的原始图表和数据，还会基于这些未解问题推演后续的市场情景。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美伊和谈，亚洲最先受益\n\n油价回落，谁最赚？\n\nAI+能源成本下降，亚洲的机会来了\n\n---\n\n**1. 油价跌了，亚洲为何先受益？**\n\n美伊达成临时和平协议，布伦特原油从高点回落25%，目前低于83美元/桶。对亚洲这个能源净进口大户来说，这是实打实的利好——油价每跌10%，亚洲经常账户就能改善约0.3%的GDP。当然，供应链恢复需要时间，好处不会一夜之间全显现。\n\n**2. 谁会是最大赢家？**\n\n从研报数据看，四国最突出：\n\n🇹🇭 **泰国**：能源进口占GDP比重最大，油价跌10%，经常账户改善0.5个百分点，通胀压力也直接缓解。\n\n🇮🇳 **印度**：85%以上原油靠进口，油价下跌等于进口成本下降、经常账户赤字收窄、财政补贴压力减轻。研报甚至用了“双重红利”这个词——低油价+近期FCNR(B)措施，可能带来550亿美元资金流入。\n\n🇵🇭 **菲律宾**：油价完全市场化传导，通胀对油价最敏感。4月CPI冲到7.2%，油价回落能让通胀更快降温。\n\n🇰🇷 **韩国**：AI热潮+低油价，经常账户盈余可能超过当前15.5%的GDP预测，创历史新高。\n\n**3. 内部差异依然关键**\n\n不是所有国家都受益。研报\n\n[... middle omitted ...]\n\nth a lag, as supply chain normalization will likely be gradual.  \n- Key winners: Thailand, Philippines, India and South Korea stand to gain the most – Thailand via a lower import bill and infl\n\n[... middle omitted ...]\n\nrmation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R019",
    "title": "Bernstein：液冷数据中心最被低估的环节不是冷板，而是冷却液分配单元",
    "digest": "[wechat_article.md]\n# Bernstein：液冷数据中心最被低估的环节不是冷板，而是冷却液分配单元\n\n当英伟达的GPU集群单机柜功耗突破100千瓦，传统风冷已经彻底失效。液冷从边缘技术走向数据中心基础设施的核心，这已是行业共识。但多数讨论集中在冷板——那个贴在芯片上的金属块——而忽略了整个液冷系统中真正决定成败的组件：冷却液分配单元。\n\nBernstein这份最新的液冷专题报告，核心判断清晰且反直觉：CDU是一个被市场低估的好生意。它不是简单的泵阀组合，而是兼具技术壁垒、服务粘性和长期定价权的关键节点。更重要的是，在冷板可能走向标准化的过程中，CDU的不可替代性反而在增强。\n\n这份报告的价值不在于告诉你液冷市场有多大——市场规模的争论仍在继续——而在于提供了一个评估CDU企业的分析框架，以及一个值得长期跟踪的技术拐点信号：两相直接接触冷却正在逼近商业化。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 为什么CDU比冷板更难被替代：技术复杂度和服务绑定的双重护城河\n\n冷却液分配单元的核心功能是精确控制冷却液的流量、压力和温度，将其分配到多个机柜和机架，再回收升温后的冷却液。听起来像是一个工业泵站，但Bernstein指出，CDU的复杂程度和关键性远超表面认知。\n\n从技术角度看，CDU需要同时管理多个物理量：流量比、压头、接近温度差、模块化扩展能力。以Bernstein对比的旗舰产品为例，Vertiv的Coolchip 2300可以处理2.3兆瓦的热负荷，流量高达每分钟3400升，压头超过50 psi；Trane Technologies的Giga-modular CDU则实现了14兆瓦的模块化扩展。这些参数背后是流体力学、热交换效率和系统可靠性的工程平衡。\n\n但真正让CDU区别于冷板的是服务绑定。冷板一旦安装，几乎不需要维护\n\n[... middle omitted ...]\n\n却、芯片级散热——也有兴趣，我们可以在后续的讨论中逐一展开。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n数据中心散热，液冷才是未来\n\n液冷散热，不只是噱头\n\n最近在看某外资投行关于液冷散热核心部件——CDU（冷却液分配单元）的研报，信息密度很高，分享几个关键点👇\n\n1️⃣ **为什么液冷成了刚需？**\n芯片和机架越来越密集，传统风冷已经压不住热量了。液冷从边缘技术变成主流，核心是两个部件：CDU和冷板。这篇重点聊CDU。\n\n2️⃣ **CDU是一门好生意**\n- 技术复杂度够高，不容易被完全同质化\n- 一旦CDU故障，多个机架可能烧毁（机架价值越来越高）\n- 客户更看重可靠性，不会单纯选最便宜的供应商\n- 服务收入可观，形成技术护城河\n\n3️⃣ **市场规模预测**\n研报给出：2026年约低十亿美元级别，未来5年保持双位数增长，到2030年达到中高十亿美元级别。但具体数字对新增GW、每kW成本和CDU寿命高度敏感。\n\n4️⃣ **玩家格局一览**\n- 英伟达液冷生态里的玩家（如Vertiv、nVent、Boyd、Motivair）产品都不错\n- Trane表现超出预期\n- Carrier和JCI的CDU产品广度、规格和细节不如其他玩家\n- CoolIt更偏冷板，温度表现落后\n\n5️⃣ **未来五年关键看点**\n\n[... middle omitted ...]\n\na9b1978f2ca4ac5d40be0c151.jpg)\n\nMadison Rezaei\n\n+1 917 344 8622\n\nmadison.rezaei@bernsteinsg.com\n\n## Specialist Sales\n\n![](images/b681c380bc6081f83eb8971f65736a84d82c136998f7ec4b316b902800d3e43\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R020",
    "title": "摩根斯坦利：AI基础设施正在经历从“GPU短缺”到“系统级重构”的转折点",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：AI基础设施正在经历从“GPU短缺”到“系统级重构”的转折点\n\n市场对AI算力的讨论，过去两年几乎全部集中在GPU的产能与交付。但摩根斯坦利最新发布的这份大中华区科技硬件深度报告，传递了一个更值得关注的信号：AI基础设施的投资逻辑，正在从“谁拿到了芯片”切换到“谁能把芯片变成高效、可靠、可扩展的系统”。GPU的稀缺性正在被系统设计的复杂度取代。\n\n这份报告覆盖了从服务器机架、电源架构、散热方案到PCB基板、数据网络互连的完整硬件链条，并明确指出了下一代平台（Vera Rubin、Kyber架构、LPX/Vera CPU机架）带来的设计升级机会。报告的核心判断可以提炼为一句话：AI服务器市场的价值分配，正在从芯片端向系统集成与关键组件端迁移，而这轮迁移的幅度，可能比市场当前定价所反映的要大得多。\n\n为什么现在需要关注这个转折？因为市场对AI资本开支的预期已经相当充分，但对其结构变化的定价却远远不足。报告通过详尽的估值对比表显示，多数AI服务器ODM和组件供应商的2026年预期市盈率仍处于15-25倍区间，而它们的盈利增长轨迹——尤其是2027年的EPS增速——并未被充分计入。这不是一个关于“AI需求会不会持续”的问题，而是一个关于“需求结构变化下，哪些环节会获得超额分配”的问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 下一代AI平台的硬件升级，其幅度可能超过市场预期\n\n报告明确指出，即将到来的Vera Rubin平台、Kyber架构以及LPX/Vera CPU机架，将带来“major design upgrades”。这不仅仅是代际更替，而是系统架构层面的重构。\n\n从组件层面看，这些升级意味着：电源架构从传统方案向800VDC高压直流方案迁移，散热需求从风冷向液冷方案加速过渡，PCB与ABF\n\n[... middle omitted ...]\n\n生逆转？这些问题的答案，将决定我们如何为这份报告的判断定价。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI服务器升级潮，这些环节最值得看\n\nAI服务器升级，供应链机会在哪\n\n最近看了一份某外资投行关于大中华区科技硬件的研报，核心是讲AI服务器和基础设施的升级周期。信息量很大，帮大家拆成3个重点：\n\n1️⃣ 两大升级主线\n- NVIDIA的Vera Rubin平台和Kyber架构，带来服务器/机架设计大改\n- AI ASIC服务器（主要是TPU和Trainium平台）的量增和升级，短期股价空间更值得关注\n\n2️⃣ 供应链的稀缺环节\n- AI服务器电源方案转向800V DC\n- PCB/ABF载板供给偏紧\n- 数据中心网络/互联/CPO升级\n- GB300服务器机架交付顺利，AI服务器ODM风险回报比不错\n\n3️⃣ 需要留意的风险\n- 下半年消费电子（手机/PC）需求受内存涨价影响，利润可能承压\n- 原材料（铜、镍）涨价和供给紧张，侵蚀利润率\n- 供给短缺可能拖累出货节奏\n- 地缘政治影响AI数据中心资本开支\n\n研报还梳理了覆盖的标的，AI服务器硬件是重点，边缘AI也有涉及。整体感觉，这轮AI基础设施升级不只是GPU迭代，电源、散热、连接器、PCB等环节都有结构性机会。\n\n关于风险部分，原材料和供给短缺对利润的影\n\n[... middle omitted ...]\n\nsiness with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS \n\n[... middle omitted ...]\n\naxy Co Ltd (2455.TW)</td><td>E (09/11/2023)</td><td>NT$352.00</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R021",
    "title": "摩根斯坦利：AI互联正在从“规模扩张”转向“架构重构”，市场低估了互联层定价权的转移",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：AI互联正在从“规模扩张”转向“架构重构”，市场低估了互联层定价权的转移\n\n这份摩根斯坦利半导体团队在2026年6月发布的巴士巡回路演纪要不是一份常规的企业拜访汇总。它传递了一个更值得关注的结构性信号：AI基础设施的投资重心，正在从算力芯片的比拼，转向互联架构的决定性博弈。三位CEO——Astera Labs、Marvell、Intel——不约而同地将叙事焦点放在互联层，而非单纯的算力性能上。这并非巧合，而是AI基础设施从粗放扩张进入精细化架构优化的必然产物。\n\n研报的核心判断可以概括为：互联层正在从“必要组件”升级为“系统架构的定义者”。谁能在光学互联、PCIe生态、定制SerDes和先进封装上同时建立优势，谁就能在下一阶段的AI基础设施投资中占据定价权。而目前市场对这一转变的定价，仍然偏保守。\n\n以下是基于该报告提炼的五个关键洞察，以及一个报告尚未完全回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 互联层从“被动跟随”变为“主动定义”，Astera和Marvell正在争夺架构主导权\n\n过去两年，AI基础设施的投资叙事几乎完全由GPU的算力密度和内存带宽主导。互联层（Scale-up与Scale-out网络）被视为“跟着GPU走”的附属品。但这份报告中的两个信号表明，情况正在逆转。\n\n首先，Astera Labs管理层明确表示，其PCIe交换机正在被客户称为“开放生态的NVSwitch”。这不是一个营销话术，而是一个架构信号。NVSwitch是NVIDIA用于GPU间高速互联的专有技术。当客户开始将第三方PCIe交换机类比为NVSwitch时，意味着互联层正在从“标准化连接”走向“架构差异化”。Astera正在定义开放生态中的互联标准，而非仅仅提供兼容性产品。\n\n其次，Marve\n\n[... middle omitted ...]\n\n期组织线上讨论，围绕这些尚未完全定价的变量进行更深入的推演。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n芯片互联大战：谁在抢跑\n\n封面标题：芯片互联暗战\n\n封面副标题：ALAB/MRVL/INTC最新动向\n\n最近某外资投行调研了Astera Labs、Marvell和Intel三家芯片公司，聊下来一个核心判断：AI基础设施正在从“算力堆叠”转向“互联驱动”。分享几个关键洞察👇\n\n**1. Astera Labs：PCIe依然是现金牛**\n- 每XPU互联价值从$1000起步，还在涨\n- 中国市场需求强劲：算力卡以PCIe为主，互联需求反而更大\n- UAL交换机2025年首次部署，2028年放量\n- CXL预计2027年产生收入，DDR4通过CXL延长寿命是个有意思的场景\n- 铜缆在机柜内仍有用武之地，但机柜间400G必转光\n\n**2. Marvell：互联全栈选手**\n- AI机会越来越偏向互联，规模互联（scale-up）才是重头戏\n- 从DCI到CXL到NIC到定制芯片，Marvell几乎全覆盖\n- 定制芯片业务预计从$40亿增长到$100亿\n- 互联业务年增70%，没有放缓迹象\n- 代理型AI（agentic AI）还没算进预测，可能是额外增量\n\n**3. Intel：新CEO的“赌注”**\n- Lip-\n\n[... middle omitted ...]\n\nhly \\~\\$1,000 today as AI infrastructure becomes more interconnect-intensive. The company is investing across optical, UAL, and NVL, and highlighted that customers are increasingly describing \n\n[... middle omitted ...]\n\nSynopsys Inc. (SNPS.O)</td><td>E (02/27/2026)</td><td>$453.89</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R022",
    "title": "GS：霍尔木兹海峡若重开，最被低估的不是油价，而是油运定价权的结构性重置",
    "digest": "[wechat_article.md]\n# GS：霍尔木兹海峡若重开，最被低估的不是油价，而是油运定价权的结构性重置\n\n市场正在关注霍尔木兹海峡可能重启的地缘信号，但多数讨论仍停留在“油价会跌多少”的层面。GS在6月14日发布的一份中国交通运输行业专题报告中，给出了一个更具穿透力的判断：如果海峡在2026年7月底前恢复正常通行，全市场最被低估的变量不是原油价格，而是VLCC（超大型油轮）日租金可能飙升至25万美元/天，甚至35万美元/天——这分别对应了航运公司盈利57%和114%的上行空间。\n\n这份报告之所以值得认真读，不是因为它给出了一个乐观数字，而是因为它揭示了一个正在发生的结构性变化：过去两年中国和韩国船东的激进整合，已经从根本上改变了VLCC市场的定价机制。当供给侧的议价权从分散走向集中，同样的需求波动，会带来完全不同的价格弹性。\n\n以下是我们从这份报告中提炼出的核心逻辑与未解问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 市场真正没算清的账，是油运定价权已经从“船多货少”转向“船东说了算”\n\n多数投资者对油运周期的理解，仍停留在“运价由供需缺口决定”的古典框架里。但GS的报告指出，这个框架已经过时了。\n\n2021至2025年间，VLCC市场每1个百分点的净需求变化，只能带来约6000美元/天的运价波动。而到了2026年前两个月，这个弹性系数已经跃升至2万美元/天——翻了3倍以上。背后的原因，是前十大合规船东的市场份额从2025年的47%飙升至68%，集中度在短短一年内完成了质的飞跃。\n\n这意味着什么？意味着即便需求恢复的速度没有超预期，船东的定价能力也已经今非昔比。过去，运价上涨会迅速触发新船订单和闲置运力回归，形成价格天花板。但在当前格局下，头部船东有能力通过控制运力投放节奏，把运价维持在高位更长时间。\n\n这份报告的核心贡献，不是给出\n\n[... middle omitted ...]\n\n报告的拆解讨论，帮助参与者从研报中提取真正可操作的判断框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n霍尔木兹复航，谁最受益？\n\n**航线重启，运输板块大洗牌**\n\n霍尔木兹海峡若复航，油运弹性最大，航空次之，造船远期受益\n\n---\n\n最近有消息说美国和伊朗可能就结束冲突达成框架，霍尔木兹海峡有望重新开放，伊朗石油制裁也可能解除。某外资投行做了情景推演，结论很有意思。\n\n**1️⃣ 油运：弹性最大，逻辑最顺**\n\n霍尔木兹关闭期间，原油/成品油船运市场出现了9-11个百分点的阶段性供给过剩。一旦复航，补库存需求（全球原油库存比2月低了7.05亿桶）将直接拉动运价。\n\n更关键的是，VLCC市场集中度在提升，定价权变强。每1个百分点的净需求变化，能撬动2万美元/天的运价波动（之前是6000美元）。假设7月底恢复出口，VLCC日租金可能冲到25万美元/天；若叠加伊朗制裁解除（影子船队需求回流合规船队），甚至可能到35万美元/天。\n\n**2️⃣ 航空：油价降，利润升**\n\n油价每降10美元/桶，三大航利润能改善16%-26%。春秋航空受益较小（约4%），因为票价弹性不同。逻辑很简单：燃油成本降+燃油附加费下调刺激需求。\n\n**3️⃣ 造船：远期催化剂**\n\n复航不会立刻影响船厂利润，但高运价+贸易确定性会刺激船东下单\n\n[... middle omitted ...]\n\nb. While the memorandum of understanding is scheduled to be officially signed on Jun 19 $^{th}$ in Switzerland, with a final deal to be discussed in the 60 days following agreement by the two \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R023",
    "title": "GS：美国供应链的“新常态”比市场预期的更早到来",
    "digest": "[wechat_article.md]\n# GS：美国供应链的“新常态”比市场预期的更早到来\n\n当所有人还在讨论关税冲击和地缘冲突是否会引爆新一轮供应链危机时，GS的最新周度追踪指数给出了一组反直觉的信号：截至2026年6月中旬，其供应链拥堵综合指数环比下降4%，瓶颈评分连续多周维持在“2”的水平。这个数字意味着什么？在2021年峰值时期，该评分为“10”，而疫情前的基线水平约为“1.8”到“2.0”。换言之，美国供应链的拥堵程度，已经基本回到了疫情前的“正常”状态。\n\n这不是一个关于“好转”的新闻，而是一个关于“结构性重置”的起点。市场目前对供应链风险的定价，依然停留在“高波动、易中断”的旧叙事中。但GS的数据暗示，一个更稳定、更可预测的供应链新常态可能已经提前到来。如果这一判断成立，那么它对全球贸易流、企业库存策略、航运运价以及资产定价的重新校准，将远比一次简单的数据改善更为深远。\n\n这份报告最值得关注的判断，并非拥堵改善本身，而是改善的“质量”：它不是由需求崩溃驱动的被动去库存，而是在贸易流仍保持一定活跃度下的系统效率提升。这背后，是港口基建投资、铁路运营优化以及集装箱周转率的结构性改善。这意味着，即使未来关税政策或地缘局势出现扰动，供应链的韧性也可能比预期更强。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 拥堵指数回归“2”并非偶然，而是系统效率提升的累积结果\n\nGS的周度瓶颈指数在2026年6月降至“2”，这是自2022年7月以来首次稳定在这一水平。从月度平均评分来看，自2024年初至今，该指数几乎一直围绕“1.8”到“2.0”的区间窄幅波动。相比之下，2021年8月至10月间，该指数曾连续三个月维持在“9”至“10”的极端水平。\n\n这种长期、低波动率的改善，与2022年下半年的“假性正常化”有本质区别。当时拥堵缓解的主要驱动力是需求的急剧\n\n[... middle omitted ...]\n\n，也会针对会员提出的具体问题，进行深度的数据拆解和逻辑推演。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美国供应链压力，已经回到疫情前\n\n📦 供应链压力指数回到“2”\n\n最新投行研报显示，美国供应链拥堵指数上周环比下降4%，瓶颈评分继续维持在“2”的水平——这个数字在疫情高峰期曾飙到“10”，现在基本回到疫情前的流动性水平。\n\n几个关键指标拆开看：\n\n1️⃣ 港口船舶等待数量\n- 西海岸（LA/LB）：继续只有1艘船在等\n- 东海岸+墨西哥湾：5艘船排队，和上周持平\n\n2️⃣ 铁路运输加速\n- 西海岸两大铁路公司（UNP和BNSF）联运量同比增16%，比上周的10%明显提速\n- 但铁路服务指标好坏参半，部分停留时间略增\n\n3️⃣ 运费和底盘周转\n- 亚洲→美西的海运运费环比涨，但同比降了12%\n- 美国港口底盘停留时间小幅缩短，周转效率在改善\n\n📊 月度数据也印证趋势\n- 集装箱平均停留时间：2.6天（4月数据）\n- 中国→美国的门到门运输天数：47天\n- LMI运输能力指数：28.4（4月），显示运力持续宽松\n\n研报观点：如果供应链压力继续缓解，2026年该指数有望稳定在“1”区间。\n\n当然，关税政策和地缘冲突仍是变量——它们会影响货运需求节奏和全球贸易正常化进程。\n\n你觉得供应链这个“隐形变量”，会在下半年\n\n[... middle omitted ...]\n\ny bottleneck scale remained at '2' this week, reflecting the absolute level of the congestion index decreasing moderately on a sequential basis (-4% w/w; Exhibit 2).\n\nFor this week's scale and\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R024",
    "title": "JPM：新兴市场债券曲线正在发出被低估的信用分化信号",
    "digest": "[wechat_article.md]\n# JPM：新兴市场债券曲线正在发出被低估的信用分化信号\n\n这份JPM最新的EM USD 10s30s Spread Curve报告，表面上是一份每周例行的利差曲线追踪，但数据背后隐藏着一个被多数投资者忽视的结构性变化：新兴市场债券的期限结构正在从“风险偏好驱动”转向“信用质量驱动”。这意味着，过去那种用主权评级一揽子判断新兴市场久期策略的时代正在结束，投资者需要更精细地拆解单个发行主体的期限溢价。\n\n报告显示，截至2026年6月12日，EM Aggregate 10s30s利差曲线为67个基点，较一周前收窄2个基点，较一年前收窄10个基点。乍看之下，曲线平坦化似乎是全球利率环境趋稳的普遍结果。但JPM的数据揭示，这一平坦化并非均匀分布——不同区域、不同信用等级、不同发行主体之间的曲线斜率分化正在加剧，而这种分化恰恰是市场尚未充分定价的关键变量。\n\n真正值得关注的不是曲线本身的绝对水平，而是曲线斜率的相对变化所反映的信用分层逻辑。当EM Aggregate 10s30s在过去一年收窄10个基点时，EM IG（投资级）收窄了14个基点，而EM HY（高收益）仅收窄3个基点。这种分化不是偶然的噪音，而是市场正在对信用风险重新定价的信号。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 曲线平坦化的核心驱动力并非宏观，而是信用分层\n\nJPM的数据清晰地展示了这一分化的程度。EM Aggregate 10s30s当前为67个基点，其内部结构已经出现明显裂痕：EM IG为61个基点，EM HY为79个基点。更值得注意的是，在过去一年中，IG曲线收窄了14个基点，而HY仅收窄3个基点。这意味着，投资级债券的久期溢价正在被系统性压缩，而高收益债券的期限溢价几乎纹丝不动。\n\n这一现象与市场直觉相悖——如果曲线平坦化是全球利率环境趋\n\n[... middle omitted ...]\n\n期调整信号。这些未解问题，正是我们持续跟踪和深度讨论的方向。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nEM 债的期限结构，现在谁最陡？\n\n谁在变平？\n\n某外资投行6月12日发布了EM USD 10s30s利差曲线周报，帮大家划重点👇\n\n1️⃣ **EM整体曲线小幅变平**\nEM综合10s30s利差当前67bp，周环比-2bp，同比-10bp。投资级（IG）61bp，高收益（HY）79bp，HY的曲线斜率比IG高近20bp，说明市场对长端HY债要求更多补偿。\n\n2️⃣ **全球对比：EM vs. 美国**\n美国高等级债10s30s利差仅15bp，美债为49bp。EM整体67bp，远高于美国，反映新兴市场长端不确定性更高。过去一周美债曲线反而走陡+3bp，与EM方向相反。\n\n3️⃣ **最陡 vs. 最平**\n- 最陡：埃及134bp、Pemex 112bp、萨尔瓦多109bp、南非107bp、沙特88bp\n- 最平：印尼仅8bp、SQM 25bp、Eximbk 28bp、Bimbo 37bp、智利38bp\n\n4️⃣ **周度变动最大的个体**\n- 走平：埃及-18bp、Eximbk -12bp、AITOCU -10bp、Parguy -10bp、Bgosk -9bp\n- 走陡：AALLN +7bp、印尼+7bp\n\n[... middle omitted ...]\n\nd>EM IG 10s30s</td><td>JPCUEMAI Index</td></tr><tr><td>EM HY 10s30s</td><td>JPCUEMAH Index</td></tr><tr><td>EMBIG 10s30s</td><td>JPCUEMBG Index</td></tr><tr><td>EMBIG IG 10s30s</td><td>JPCUEMB\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 16 Jun 2026 03:19 AM HKT\n\nDisseminated 16 Jun 2026 03:19 AM HKT"
  },
  {
    "id": "R025",
    "title": "JPM：亚洲正在从“被迫加息”转向“主动加息”，市场对此定价不足",
    "digest": "[wechat_article.md]\n# JPM：亚洲正在从“被迫加息”转向“主动加息”，市场对此定价不足\n\n亚洲央行的货币政策叙事正在经历一个被市场普遍低估的转折。JPM最新一期亚洲经济周报提出了一个核心判断：亚洲正从“弱势下的被动加息”阶段，进入“强势增长驱动的主动加息”阶段。这不是一个局部的、边缘的变化，而是一个结构性切换。印尼和菲律宾的加息属于前者——由汇率压力和通胀失控所迫；而韩国、台湾、新加坡正在酝酿的加息则属于后者——由科技繁荣、超预期的增长韧性和通胀传导风险所驱动。市场目前更多关注前者，对后者的定价仍不充分。\n\n这份报告的关键信号在于：当增长本身成为加息的理由，而不是防御性工具时，资产定价的逻辑需要重新校准。对于关注亚洲市场的投资者而言，理解这两类加息的区别，比预测某一次会议的利率决议更重要。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 印尼和菲律宾的加息是“防御性”的，但市场可能低估了菲律宾的紧缩幅度\n\nJPM明确指出，亚洲已经出现两类加息。第一类，也是市场相对熟悉的，是“弱势下的被动加息”。印尼央行在美元/印尼盾突破18200历史新高后，意外进行了25个基点的非周期加息，并辅以一系列监管措施应对汇率风险。菲律宾则是区域内通胀压力最大的经济体，尽管5月通胀数据略低于预期，但6.8%的同比水平仍然令人不安。JPM预计菲律宾央行将在下周加息50个基点，作为锚定通胀预期的预防性措施。\n\n这里的关键洞察不在于加息本身，而在于两点。第一，印尼的加息虽然暂时缓解了汇率压力，但JPM认为压力仍然足以让央行在下次例行会议上再加25个基点。这意味着印尼的紧缩周期尚未结束，市场可能低估了其持续性的风险。第二，菲律宾的加息决策并非板上钉钉。报告坦诚地指出，尽管基线预测是50个基点，但考虑到全球原油价格近期下跌，25个基点的加息也是可能的。这种\n\n[... middle omitted ...]\n\n和原始图表，并持续跟踪下周台湾、印尼、菲律宾的央行会议动态。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n亚洲央行正从“被迫加息”转向“主动加息”\n\n📌 两类加息逻辑在切换\n\n最近投行研报指出，亚洲央行走在两条不同的加息路径上，逻辑正在发生变化。\n\n1️⃣ 被迫加息型：印尼、菲律宾\n- 印尼：美元/印尼盾创历史新高后，央行意外紧急加息25bp，随后又准备再加一次\n- 菲律宾：5月通胀6.8%仍偏高，预计下周加息50bp，但油价下行让25bp也有可能\n- 核心逻辑：汇率压力+通胀失控，不得不加\n\n2️⃣ 主动加息型：韩国、台湾、新加坡\n- 韩国：1Q25 GDP上修至7.5%，全年增速上调至3.7%，央行转鹰，预计未来一年加息100bp\n- 台湾：5月CPI 2.2%、PPI 14.1%，下周会议很关键，看是否暗示年底前加息\n- 核心逻辑：科技出口强劲、增长超预期、通胀风险上升，从“强势地位”主动加息\n\n3️⃣ 中国：AI撑出口，但内需偏弱\n- 5月出口超预期，但主要靠AI芯片、新能源等高价产品拉动，量没跟上\n- 预计5月工业增加值环比+0.5%，零售仅+0.1%，投资仍收缩\n- 2Q增长风险偏下行，但下半年财政可能加速发力，外部需求也有支撑\n\n🧠 总结：亚洲央行不再只是“救火队”，有些开始主动“调温”了。下周关注\n\n[... middle omitted ...]\n\nanother 25 bps hike at next week's regularly scheduled meeting, though this is now a closer call.\n\nFor its part, the Philippines has seen the largest surge in headline inflation in the region.\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R026",
    "title": "摩根斯坦利：市场低估的不是AI需求本身，而是需求在亚洲供应链中产生的结构性再定价",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：市场低估的不是AI需求本身，而是需求在亚洲供应链中产生的结构性再定价\n\n这份摩根斯坦利最新的“Three Actionable Ideas”报告，表面上给出了三个来自不同行业的买入建议，但其背后隐含着一个更深刻的判断：当前亚洲市场的定价逻辑，正在从“谁受益于AI需求”切换到“谁能在AI引发的供应链重构中，重新定义自己的议价权”。\n\n报告选取的三家公司——臻鼎、华邦电、ONGC——分别来自PCB、存储芯片和能源上游三个看似不相关的领域。但将它们放在一起审视，一个清晰的图景浮现出来：摩根斯坦利认为，市场对AI主题的定价已经过于拥挤在少数几个环节，而真正的结构性机会，正在向那些被忽视的“瓶颈”和“再定价”环节扩散。这不是一个关于AI需求增速的讨论，而是一个关于供给结构如何被重塑、以及谁能在这一重塑中占据主动的问题。\n\n以下是我们从这份报告中提炼出的五个核心洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI互连的物理瓶颈正在从芯片转向传输材料，PCB行业的价值分配将迎来拐点\n\n报告将臻鼎列为PCB领域的首选受益者，背后的逻辑并非简单的“AI服务器出货量增长”，而是一个更具体的产业现象：随着数据传输速率从400G向800G乃至1.6T演进，PCB作为信号传输介质的物理瓶颈正在凸显。摩根斯坦利在另一份相关报告中详细讨论了“Optics Drives the Board”这一主题，其核心判断是：高速互联对PCB的材料、层数、制造精度提出了质变级要求，这不仅是量的增加，更是供应链格局的重新洗牌。\n\n臻鼎被看好的原因，在于其有能力在这一技术切换过程中“capture meaningful share”。这意味着，市场此前对PCB行业的认知——一个依赖产能扩张的周期性行业——正在被颠覆。新的竞争壁垒在于对高频\n\n[... middle omitted ...]\n\n的完整解读、原始图表，以及更多关于亚洲供应链重构的深度分析。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n亚太投研：三个值得深挖的方向\n\n**三个方向，一张地图**\n\n某外资投行最新研报，从亚洲市场挑出三个值得关注的逻辑，今天拆开讲讲。\n\n**1/ 光模块 PCB 的受益者：臻鼎**\n\nAI 互联需求催生高速传输，PCB 板升级是绕不开的环节。研报观点：臻鼎在高速传输领域有份额增长潜力，是光模块 PCB 需求扩张中最受益的公司之一。行业从低阶向高阶切换，谁能抓住技术升级窗口，谁就吃下增量。\n\n**2/ 存储的拐点信号：华邦电**\n\n近期股价波动，但研报认为数据面指向更乐观的前景。服务器存储优化更多是供给端的问题，不是需求崩塌。如果供给压力缓解，价格和出货量都有修复空间。短期波动反而可能是观察窗口。\n\n**3/ 能源安全的长期逻辑：ONGC**\n\n能源安全 + AI 电力需求，上游能源生产商的“成长性”被重新定价。ONGC 目前天然气售价在全球范围内属于较高水平，同时公司过去 20 年累计回馈给股东的资本，几乎等于当前市值。这个数据点值得细品。\n\n---\n\n研报还附了一个历史表现统计：从 2025 年 6 月到 2026 年 6 月，该系列所有推荐标的平均 12 个月总回报 14.3%，相对基准超额收益 9.7%。\n\n[... middle omitted ...]\n\npstream energy producers. ONGC now has among the highest natural gas ASPs globally and has returned capital to shareholders equal to where we see its market cap in 20 years.\n\n## Links to repor\n\n[... middle omitted ...]\n\narantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n© 2026 MS"
  },
  {
    "id": "R027",
    "title": "摩根斯坦利：AI基建的真正瓶颈不在资本，而在电力与结构性供给约束",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：AI基建的真正瓶颈不在资本，而在电力与结构性供给约束\n\n市场上关于AI基础设施投资的讨论，大多集中在资本规模、算力需求、以及科技巨头的资本开支计划上。一个被广泛接受的叙事是：只要资金到位，算力就能跟上。但摩根斯坦利最新的一份宏观策略报告提出了一个更冷静的判断——AI基建的真正瓶颈不在融资端，而在供给端，尤其是电力基础设施的结构性约束。这份报告的核心洞察是：电力不再是数据中心建设的“配套条件”，而是与算力建设并列的核心约束变量。理解这一点，才能理解未来几年AI产业链的竞争格局、定价权分布，以及投资逻辑的重塑方向。\n\n报告指出，电力变压器交货周期已从此前的12-16周拉长至平均128周，部分型号甚至达到144周。伯克利实验室的数据显示，截至2025年初，美国电网互联积压项目规模已超过美国现有装机容量的两倍。这些数字背后是一个简单的物理现实：AI驱动的电力需求增长，正在与一个无法快速响应的供给体系发生碰撞。这不是一个边际问题，而是一个系统性问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 电力约束正在从“配套条件”升级为“独立瓶颈”，数据中心选址逻辑因此重构\n\n报告的核心判断之一是，电力供给的约束已经不再是数据中心建设中的一个“需要协调的变量”，而是成为一个前置性的、独立的瓶颈。过去，数据中心开发商的逻辑是：先确定需求、选址、建设，再协调电力接入。但现在，这个顺序正在被逆转——开发者必须首先确认电力可用性，才能推进项目。\n\n这一变化的影响是深远的。它意味着数据中心的选址将从“靠近用户”转向“靠近电力”。那些拥有富余电力容量、或者能够快速接入电网的区域，将获得显著的竞争优势。同时，这也意味着数据中心建设的节奏将不再由资本开支计划决定，而是由电网扩容和发电设施建设的节奏决定。后者通常以年为单位，甚至以五\n\n[... middle omitted ...]\n\n一起，分享各自对电力约束、政策演变和算力定价权的观察与判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI卡在电力上，投研视角怎么解\n\n算力不够？先看电够不够\n\n1️⃣ 电才是真正的瓶颈\nAI数据中心需求暴涨，但发电和电网跟不上\n变压器交货周期从疫情前12-16周，拉长到128-144周\n全美并网积压量已超过现有装机容量的2倍\n🔍结论：建数据中心，先抢电，再谈算力\n\n2️⃣ 钱开始流向“离网”方案\n传统靠电网供电的模式被打破\n燃料电池、燃气轮机、储能、甚至改造比特币矿场\nAI公司自己下场买电站、签合同、搞融资\n资本池正在融合，不再是分开的“科技投资”和“能源投资”\n\n3️⃣ 劳动力、水、政策都在收紧\n未来10年美国缺约30万电工，1/5电工已超55岁\n43%的数据中心建在高水压地区\n纽约拟立法暂停新项目，德州要求数据中心不能推高居民电费\n14个州在讨论限制数据中心的法案\n\n4️⃣ 供不应求，算力变成稀缺资产\n有电有算力的人，拥有定价权\n企业端需求对价格不敏感，高价值应用仍会持续迁移\n稀缺性反过来巩固头部玩家的优势\n\n📌 投研视角：AI基础设施的节奏会比市场预期慢，但结构更复杂、资本更密集。电力和算力正在变成同一件事。\n\n欢迎一起讨论，你关注的是算力还是电力？\n\n#学习笔记\n\n[source_mineru.md\n\n[... middle omitted ...]\n\n and structure of this financing. In this week’s Start, we outline the constraints and their impact on the pace and magnitude of investment as well as their implications.\n\nOne of the most seri\n\n[... middle omitted ...]\n\narefully before investing.\n\nThe following authors are Fixed Income Research Analysts/Strategists and are not opining on or expressing recommendations on equity securities: Raquel Kanner; Vishwanath Tirupattur.\n\n© 2026 MS"
  },
  {
    "id": "R028",
    "title": "NOM：人民币中间价模型正在发出一个被市场忽视的信号",
    "digest": "[wechat_article.md]\n# NOM：人民币中间价模型正在发出一个被市场忽视的信号\n\n市场对人民币汇率的讨论，大多仍然停留在“中美关系”、“出口压力”或“央行干预”这些宏观叙事层面。但一份来自NOM亚洲外汇策略团队的最新研报，通过其定价模型给出了一个更具体、也更值得推敲的判断：人民币中间价的模型预测值，正在出现系统性偏离。\n\n这份报告的核心不在于预测一个具体的点位，而在于揭示一个机制层面的变化——中间价的形成逻辑，可能正在从“被动跟随”转向“主动引导”。这个变化，对于任何持有人民币资产、或关注中国资本流动的决策者来说，都值得重新审视。\n\n报告提供了一个关键数据点：模型对USD/CNY中间价的预测值为6.7575，较上一期大幅下调了513个基点。而如果计入逆周期因子，预测值则为6.7800，仍较前次中间价低288个基点。这不是一个随机波动，而是一个系统性的、由多个因素共同推动的修正。\n\n下面，我们拆解这份报告的核心逻辑，并尝试回答一个更重要的问题：这个信号，到底意味着什么？\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 模型预测的偏离，揭示的不是点位，而是政策意图的转变\n\nNOM这份报告最值得关注的，不是6.7575这个数字本身，而是模型预测值与实际中间价之间的“误差”。报告中的图2展示了模型误差的历史走势：从2025年初的-1800个基点（模型预测远低于实际中间价），逐步收窄，到2026年初接近零，甚至在今年4月转为正600个基点。\n\n这个误差的演变，本质上反映的是“逆周期因子”的调节力度。当模型预测值显著低于实际中间价时，意味着央行在使用逆周期因子来“托底”汇率，防止人民币过快升值。而当误差收窄甚至转正，则意味着这种调节在减弱，或者方向在转变。\n\n报告给出的最新模型预测（不含逆周期因子）为6.7575，比前次低513个基点。这本身就是一\n\n[... middle omitted ...]\n\n。群里不仅有更深入的讨论，还有原始报告的完整图表和后续更新。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n人民币中间价模型，透露什么信号？\n\n📊 中间价模型看方向\n\n某外资投行最新研报，拆解了人民币兑美元中间价的定价模型。核心结论：模型给出的中间价预测是 **6.7575**，比上一日低了513个基点。\n\n如果加入“逆周期因子”，预测值变成 **6.7800**，比前一日低288个基点。\n\n简单说：模型认为，中间价有向下调整的空间。\n\n1️⃣ 谁在影响这个预测？\n四个货币贡献最大：欧元（+13基点）、日元（+5基点）、韩元（-14基点）、俄罗斯卢布（-18基点）。欧日走强对人民币有支撑，韩元卢布走弱则有拖累。\n\n2️⃣ 模型误差在收窄\n从年初的-1800基点，到最近已经接近0。说明模型对中间价的预测越来越准，市场定价效率在提高。\n\n3️⃣ 近期中间价波动\n过去几个月，单日调整幅度在-150到+140基点之间，整体偏向下行。3月有一次+140基点的上调，但4月又出现-150基点的下调。\n\n4️⃣ 年底前重要事件\n7月底政治局会议、10月国庆黄金周、11月APEC深圳峰会、12月中央经济工作会议，以及年底中美领导人会晤。这些事件都可能影响汇率预期。\n\n研报未给出具体方向判断，但模型信号值得关注。欢迎一起讨论你对人民币\n\n[... middle omitted ...]\n\nr)  \n![](images/6f73674832d8a2173b5211c88835cf9cb1fb5ed2bf5125aa17c01c207543d6e2.jpg)\n\n<details>\n<summary>bar chart</summary>\n\n| Currency | Top 4 weighted contribution to projected change (pip\n\n[... middle omitted ...]\n\nrmation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R029",
    "title": "Bernstein：上游资本开支的“超级周期”叙事，市场可能信错了",
    "digest": "[wechat_article.md]\n# Bernstein：上游资本开支的“超级周期”叙事，市场可能信错了\n\n市场正在为一个“上游资本开支超级周期”定价。地缘冲突推高布伦特油价至90美元/桶，霍尔木兹海峡的紧张局势让供给中断的担忧升温，投资者很自然地认为：石油公司会加大投资，一个新的开支上行周期已经启动。但Bernstein这份研报的核心判断恰好相反——这个叙事经不起推敲。该机构认为，2026年全球上游资本开支不仅不会进入超级周期，反而可能出现约400亿美元的收缩。这不是一个关于“会不会投”的问题，而是一个关于“谁在投、投在哪里、为什么投”的结构性判断。市场的定价逻辑，可能错配了供给侧的真正驱动力。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 现金流的改善并未转化为投资意愿，资本纪律比油价更顽固\n\n油价上涨确实带来了上游勘探生产公司现金流的显著改善。Bernstein的数据显示，美国大型E&P公司的经营性现金流自疫情以来持续回升，部分得益于行业整合带来的规模效应。但关键问题在于：这些现金并没有流向资本开支。投资回报率、股票回购和自由现金流稳定性，依然是管理层和投资者共同关注的优先级。报告中的图表清晰表明，即便在2026年一季度地缘冲突推高油价后，那些将更高比例经营性现金流返还给股东的公司，股价表现反而弱于那些保留现金、减少分红的公司。这并非鼓励企业“少花钱”，而是说明市场当前对资本纪律的奖励机制仍然有效。Bernstein的结论是：现金流的改善，不等于投资意愿的恢复。对于上市公司而言，资本开支的决策逻辑已经从“有多少钱投多少”转变为“投多少才能让股东满意”。这个转变是结构性的，不会因为油价短期冲高而逆转。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 已发现资源中约三分之一尚未开发，但可转化为供应的比\n\n[... middle omitted ...]\n\n关于规划价格和地缘溢价的推演，以及与其他机构观点的交叉验证。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n上游资本开支超级周期？我不信\n\n上游开支，只是微调\n\n油价涨了但开支没有大举扩张，市场在等什么？\n\n最近某外资投行的能源研报，用经典的5W框架拆解了当下石油上游资本开支的逻辑，结论很清晰：**别指望“超级周期”** 🛢️\n\n① **WHY 为什么投？** 现金流确实改善，但管理层和股东都更爱回购和分红，而不是扩产。资本纪律是硬道理，谁乱花钱谁被市场嫌弃。\n\n② **WHAT 开发什么油？** 过去发现的大量资源里，还有约1/3没开发。但问题在于——深海油越来越难转化成产量，页岩油产量也进入平台期，油砂还需要更多确定性。\n\n③ **WHO 谁会投？** 下一轮增长的主角不是美国页岩油独立公司，而是**国家石油公司（NOCs）**。边际增长桶的控制权，正在转移。\n\n④ **WHERE 钱去哪？** 最好的地质条件往往在最差的司法管辖区——高税负、政治不稳定、制裁、法治薄弱……资本想投但不敢投。\n\n⑤ **WHEN 什么时候投？** 历史上高油价会刺激钻机活动激增，但这次模式失效了。油服公司也没有上调业绩指引，上游通胀反而在吃掉增量开支。\n\n📉 研报预计2026年上游资本开支约**5600亿美元**，比此前预测仅上\n\n[... middle omitted ...]\n\nstream oil & gas capital expenditures (Bernstein Energy: Global Upstream Capex 2026...the quantity of capex falls now...does the quality of capex follow?) to consider the current environment. \n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R030",
    "title": "Bernstein：福克斯收购Roku，战略逻辑成立但价格昂贵，市场低估了广告协同的潜力",
    "digest": "[wechat_article.md]\n# Bernstein：福克斯收购Roku，战略逻辑成立但价格昂贵，市场低估了广告协同的潜力\n\n这笔交易标志着传统媒体公司向流媒体转型的一次关键尝试，但其真正的价值不在于硬件或用户规模，而在于广告库存的重新定价。\n\nBernstein最新发布的研报，对福克斯（Fox）拟以约220亿美元收购Roku的交易进行了深入剖析。这不是一份简单的交易点评，而是一份关于“在流媒体时代，什么资产才真正具有战略稀缺性”的思考框架。报告的核心判断是：Roku是一个独特的战略资产，但福克斯可能并不需要“拥有”它来实现类似的商业结果。然而，如果广告协同效应能够兑现，这笔交易对福克斯股价的重估意义将远超财务数字本身。\n\n在当前媒体行业估值普遍承压的背景下，这笔交易为投资者提供了一个重新审视“流媒体平台价值”的窗口。市场可能低估了Roku作为广告平台与福克斯优质内容结合后，在广告填充率和定价权上的潜在提升空间。这不仅是两家公司的交易，更是对“内容+分发”商业模式未来走向的一次压力测试。\n\n**以下是这份Bernstein研报的核心洞察与延伸思考。**\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这笔交易真正的战略价值在于广告，而非订阅\n\n许多分析将这笔交易视为福克斯获取流媒体分发渠道、加速数字订阅增长的手段。Bernstein承认这一逻辑存在，但指出“商业合作可能同样有效”。真正让这笔交易变得“战略”而非仅仅是“财务”的，是广告。\n\n福克斯在过去两年新增了超过500家广告客户，其广告库存需求旺盛，CPM持续走高。而Roku拥有美国最大的智能电视操作系统市场份额（以2025年出货量计，约800万台，领先于三星Tizen和亚马逊Fire TV），并积累了大量的第一方用户数据。将福克斯的广告销售能力与Roku的库存和数据结合，意味着福克斯可以更\n\n[... middle omitted ...]\n\n和“下一个可能的收购目标”这两个未解问题，进行更深入的推演。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nFox收购Roku，这步棋值不值\n\n220亿美金买Roku\n\n一场豪赌还是战略卡位？\n\n某外资投行刚出了一份深度报告，解析Fox收购Roku的逻辑。我提炼了几个关键点，一起看看这背后到底在打什么算盘。\n\n1/ 交易结构\n- 60%现金+40%股票收购Roku，总价220亿美元\n- 收购后净杠杆率约2.9倍，还算健康\n- 预计2028年EPS被稀释约10%（未算协同效应前）\n\n2/ 估值不便宜\n- 对应NTM EBITDA约30倍，NTM PE约60倍\n- 在可比公司中处于高位（Netflix EBITDA约19.5倍，Disney约9.2倍）\n- 但战略资产从来不便宜，Roku确实是个独特标的\n\n3/ 为什么是Roku？\n- 美国最大智能电视OS（2025年出货量800万台）\n- 拥有快速增长FAST平台和广告技术能力\n- 关键是第一方数据和分发渠道，这对转型中的媒体公司是稀缺资源\n\n4/ 广告协同是最大看点\n- Fox过去两年新增500+广告主，库存需求强劲\n- 结合Roku的CTV库存和1P数据，可以提升填充率和定价\n- 如果Fox能证明在流媒体订阅和广告上持续增长，估值逻辑可能重估\n\n5/ 监管风险不大\n\n[... middle omitted ...]\n\num—strategic asset for many players in Media. It offers a growing FAST platform,\n\nmeaningful adtech capabilities, and, most importantly, significant distribution reach with $1^{st}$ party data\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R031",
    "title": "GS：市场低估了IRA谈判规则对皮下注射制剂的连锁影响",
    "digest": "[wechat_article.md]\n# GS：市场低估了IRA谈判规则对皮下注射制剂的连锁影响\n\n制药行业对《通胀削减法案》的定价影响已有充分预期，但多数讨论仍停留在IV制剂的谈判框架内。GS在最新一份研报中提出一个被广泛忽视的变量：CMS拟议规则正在将皮下注射制剂纳入2029年药品价格谈判的候选范围。这一政策动向的直接后果是，默沙东的Keytruda Qlex、百时美施贵宝的Opdivo Qvantig和强生的Darzalex Faspro可能面临额外定价压力。GS对此进行了量化分析，结论是即便在最保守的假设下，这些公司2029-2030年的EBIT也将受到低个位数百分比的冲击。\n\n市场对这一消息的反应是迅速的——消息公布当日，默沙东下跌2.8%，强生下跌2.2%，百时美施贵宝下跌1.6%，而同期标普医疗保健板块仅下跌0.6%。但这轮下跌是否已经充分定价？GS的分析框架显示，影响远不止于表面数字。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 皮下制剂的纳入并非新问题，但此次规则修订的约束力显著升级\n\n这不是CMS第一次将目光投向皮下制剂。GS在报告中回溯指出，在IPAY 2028谈判类别的草案指南中，CMS曾包含一个关于固定组合制剂的段落，但在最终指南中被删除。当时市场认为这只是一个试探性动作。然而，2026年的拟议规则不仅重新引入这一条款，而且措辞更为具体——明确提到含有两种或以上活性成分或疫苗抗原成分的制剂将被视为一个谈判单位，且特别点名了含有透明质酸酶的组合制剂。\n\n这一变化的意义在于，皮下注射制剂通常是IV制剂的改良版本，本质上是“老药新剂型”。如果CMS成功将其纳入谈判范围，将打破制药公司通过剂型改良来延长专利生命周期、规避价格谈判的传统策略。GS对此的判断是，这不仅仅是针对三种药物的个案，而是对行业定价策略的一次结构性打击。\n\n对于\n\n[... middle omitted ...]\n\n们会持续追踪CMS最终规则的进展以及三家公司的应对策略演变。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n皮下注射版抗癌药，被盯上了\n\n🔥 医保价格谈判的新靶子\n\n某外资投行最新研报指出，CMS新规可能把皮下注射（SC）抗癌药纳入医保价格谈判范围。这对默沙东、百时美施贵宝、强生的几款重磅产品影响值得关注。\n\n📌 具体影响量化分析\n\n1️⃣ 强生 - Darzalex Faspro\n- 年销售额影响约19亿美元（2029-2030）\n- 约占达雷妥尤单抗总销售额的9%\n- 占强生总EBIT约4%\n\n2️⃣ 默沙东 - Keytruda Qlex\n- 年销售额影响约9亿美元\n- 约占Keytruda总销售额3%\n- 占默沙东总EBIT约3%\n\n3️⃣ 百时美施贵宝 - Opdivo Qvantig\n- 年销售额影响约2.7亿美元\n- 约占Opdivo总销售额4%\n- 占BMY总EBIT约2.5%\n\n📊 关键假设\n- 假设36%的净价格折扣（基于2027年价格谈判的平均水平）\n- 仅限美国Medicare部分\n- 基于2023年CMS数据\n\n💡 公司态度\n- 强生：不认为Darzalex Faspro会在2034年前被纳入\n- 默沙东：无论是否被纳入，财务影响可控\n- BMY：将积极参与意见征询期\n\n🔍 后续关注\n8月\n\n[... middle omitted ...]\n\npdivo Qvantig, and JNJ's Darzalex Faspro — contributing to slight underperformance (MRK -2.8%, JNJ -2.2%, BMY -1.6% vs DRG -1.3%, XLV -0.6%). We note this issue was raised last year, as the CM\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R032",
    "title": "摩根斯坦利：生物科技并购不是脉冲，而是结构性的重新定价",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：生物科技并购不是脉冲，而是结构性的重新定价\n\n这份报告来自摩根斯坦利SMID Cap生物科技团队的第65期周报。标题“Finger On The Pulse”暗示了团队对行业脉搏的持续追踪。在阅读完整份报告后，我们认为最值得提炼的判断不是某只股票的涨跌，而是：**并购正在从偶发事件变为系统性力量，而市场对2026年生物科技资产定价的逻辑，可能仍低估了这一结构性变化的深度。**\n\n这份报告发布于2026年6月14日。此时，市场正处在一个微妙的窗口期：利率环境虽未大幅改善，但已趋于稳定；IPO市场在经历了2025年的极度低迷后，2026年年初至今的融资额已经超过了2025年全年；更重要的是，大型药企的并购动作正在加速。摩根斯坦利的团队没有简单地将这些信号归结为“市场回暖”，而是试图拆解这些现象背后真正驱动行业重新定价的力量。\n\n以下是我们从这份报告中提炼出的四个关键层次，以及一个报告尚未完全回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 2026年的并购不是在追赶潮流，而是在填补未来5年的产品线缺口\n\n报告中最具冲击力的图表之一是“BioPharma M&A Deals Announced in 2025 - 2026”列表。短短一个多月内，GSK以106亿美元收购Nuvalent，Incyte以20亿美元收购Vega Therapeutics，Bayer以24.5亿美元收购Perfuse，再加上Eli Lilly在5月26日单日宣布的三笔收购。这些交易的密集程度，已经超出了简单的“行业整合”叙事。\n\n摩根斯坦利团队在报告中给出了一个关键判断：并购是结构性的，而非偶发性的。这句话的分量在于，它指向了大药企正在面临的专利悬崖压力。以Incyte收购Vega Therapeutics为例，\n\n[... middle omitted ...]\n\n度拆解，以及如何将这些投行级分析框架应用到自己的投资决策中。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n生物科技并购潮，比想象中更猛🔥\n\n🔍 生物科技并购不是一时热度\n\n某外资投行最新研报指出，2026年生物科技并购活动正在加速，有望创下历史新高。这不是短期现象，而是结构性趋势。\n\n📌 三大看点\n\n1️⃣ M&A结构性强于周期性\n研报明确表示并购是“结构性”而非“周期性”，意味着背后有深层逻辑推动，不是昙花一现。\n\n2️⃣ 本周三大标的动态\n- INCY：$1.25B收购Vega Therapeutics，布局罕见出血性疾病，峰值销售潜力预计超$1B\n- SLN：EHA会议数据亮眼，患者生活质量改善明显，8月关键数据值得跟进\n- CGEM：免疫学日数据验证CD19 TCE机制，B细胞清除率超80%，初步疗效信号积极\n\n3️⃣ 利率环境变化\n研报提到“利率上升，商业化改善”，暗示宏观环境对生物科技公司并非全是利空。\n\n💡 核心逻辑\n研报认为SMID Cap生物科技正进入“复兴期”，IPO市场也在回暖——2026年至今IPO平均规模已达$330M，远超去年全年水平。\n\n欢迎一起讨论你对生物科技赛道的看法～\n\n#学习笔记\n\n[source_mineru.md]\n## MS\n\nJune 14, 2026 10:00 P\n\n[... middle omitted ...]\n\nhave a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.\n\nFor analyst certification and ot\n\n[... middle omitted ...]\n\nCanary Wharf\n\nLondon E14 4AD\n\nUnited Kingdom\n\n+44 (0)20 7425 8000\n\n## Japan\n\n1-9-7 Otemachi, Chiyoda-ku\n\nTokyo 100-8109\n\nJapan\n\n+81 (0) 3 6836 5000\n\n## Asia/Pacific\n\n1 Austin Road West\n\nKowloon\n\nHong Kong\n\n+852 2848 5200"
  },
  {
    "id": "R033",
    "title": "摩根斯坦利：天然气轮市场的真正拐点不在2026，而在供给侧的隐性再定价",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：天然气轮市场的真正拐点不在2026，而在供给侧的隐性再定价\n\n这份摩根斯坦利关于西门子能源的最新研报，表面上是在讨论天然气轮订单周期何时见顶，但真正值得产业决策者和投资者关注的，远不止于一个时间点的判断。\n\n报告的核心信号是：市场对天然气轮需求侧的叙事已经高度拥挤，但供给侧的结构性变化——尤其是非传统发电解决方案的产能扩张——正在悄然重塑2030年的竞争格局。这种变化不是线性外推的，而是通过“时间成本”和“替代弹性”两个隐形变量在发挥作用。\n\n摩根斯坦利分析师在密集的投资者交流后发现，即便是最专业的买方，对供给侧的认知也明显滞后于需求侧。超过50份索要供给模型的请求，本身就说明了一个问题：市场的注意力分配严重不均。而正是这种不均，可能孕育着未来最大的预期差。\n\n以下是我们从这份研报中提炼出的五个关键洞察，以及它们对行业格局和投资框架的深层含义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 市场共识正在从“订单还能涨多久”转向“利润弹性还有多大”，但后者的边际改善空间正在收窄\n\n摩根斯坦利维持西门子能源的超配评级，但态度明显比2024-2025年更谨慎。核心原因在于：盈利上调的“速率”正在放缓。\n\n从研报提供的图表可以清晰看到，2024年8月到2025年11月，每次业绩发布后30天内，市场对2028年EBITA的共识上调幅度都在7%以上，最高达到16.2%，伴随的是股价15%-30%的上涨。但进入2026年，上调幅度骤降至5%左右，股价反应也变得平淡甚至为负。\n\n这背后的逻辑很直接：当一家公司的盈利预期已经大幅上修后，继续超预期的难度呈指数级上升。摩根斯坦利目前对西门子能源2030年EBITA的预测仅比共识高5%，而在2024-2025年，他们对2028年EBITA的领先幅度曾高达20%。\n\n这意\n\n[... middle omitted ...]\n\n这里，我们不只是分享报告，更是在构建一个持续迭代的分析框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nSiemens Energy 还能涨多久？投行分歧实录\n\n📊 燃气轮机供需博弈\n\n最近某外资投行发布了西门子能源的深度调研，核心结论是：**市场对2030年的供给过剩风险存在严重分歧**。我整理了5个关键辩论点👇\n\n**1/ 135GW电力解决方案能兑现多少？**\n市场普遍认可97GW的燃气轮机产能，但对新增的“非燃机”方案（如卡特彼勒、瓦锡兰的发动机方案）存疑。投行认为：时间差才是数据中心选址的关键，这些小型方案正在蚕食市场份额。\n\n**2/ 数据中心需求最终会流向大型燃机吗？**\n主流观点认为数据中心最终会接入电网，带动大型燃机需求。但投行反驳：过渡方案可能在中期造成供给过剩，且小型燃机订单的高利润也面临压力。\n\n**3/ 需求强劲能否抵消供给扩张？**\n投资者普遍认为算力需求会带动燃机订单持续增长至2030年。但投行指出：**数据中心建设瓶颈已从电力转向工程、劳工和审批**，订单可能无法无限增长。\n\n**4/ 燃机定价还能坚挺多久？**\n行业反馈定价仍强劲，但投行预计：瓦锡兰等厂商扩大2028年后产能时，小型方案的定价将率先松动。\n\n**5/ 电网业务能否成为新增长引擎？**\n电网业务预期已大幅上调（2\n\n[... middle omitted ...]\n\neciated, (3) Gas turbine order can grow into 2027, (4) Valuation.  \nOn Supply demand. We were surprised that the supply side Gas turbine capacity was not better understood. Many disagree that \n\n[... middle omitted ...]\n\nWeir Group PLC (WEIR.L)</td><td>E (05/12/2025)</td><td>2,324p</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R034",
    "title": "GS：市场误读了美联储的利率路径，最不确定的不是加息，而是何时降息",
    "digest": "[wechat_article.md]\n# GS：市场误读了美联储的利率路径，最不确定的不是加息，而是何时降息\n\n当通胀数据连续数月高于3%的门槛，而劳动力市场又展现出意外的韧性时，市场对美联储下一步行动的定价几乎自动滑向了“加息”。这是过去一年反复出现的市场本能反应。但GS在6月FOMC会议前夕发布的最新研报给出了一个反直觉的判断：**加息的可能性被市场系统性高估了，真正的政策博弈焦点不是“加不加”，而是“何时降”以及“降多少”。**\n\n这份研报的核心价值不在于预测点阵图，而在于它系统性地拆解了美联储不会因为供给冲击而加息的逻辑框架。GS认为，当前的通胀脉冲——主要由关税、油价和存储芯片价格构成——本质上是一次性的价格水平调整，而非需求驱动的持续性通胀。而美联储历史上对供给冲击的反应模式、当前劳动力市场的平衡状态，以及通胀预期并未脱锚的事实，共同指向了一个结论：加息的门槛远比市场想象的更高。\n\n对于资产定价而言，这意味着市场可能正在为一种低概率情景（加息）支付过高的风险溢价。如果GS的框架成立，那么当前债券收益率曲线中包含的加息预期，将在未来几个月被逐步修正，从而为风险资产提供一个新的定价锚。以下是对这份GS研报关键逻辑的拆解。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 劳动力市场的“韧性”正在误导市场对通胀持续性的判断\n\nGS的分析起点，是最近几个月就业增长的回升。数据图表显示，在经历了2025年下半年的极度疲软（甚至月度净负增长）之后，2026年初的就业数据明显反弹，1月至5月的月度新增非农就业从个位数回升至50-130万的水平。\n\n市场很容易将这种反弹解读为经济过热或需求过强，从而推断通胀压力难以消退。但GS提出了一个更细致的观察框架：他们计算了一个“潜在就业趋势”指标，该指标并非简单看月度数据的波动，而是通过加权平均（0.75乘\n\n[... middle omitted ...]\n\n加息风险溢价是否合理”等话题，与大家进行更深入的交流与碰撞。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美国6月议息会议，通胀和就业的拉扯\n\n就业回暖，但通胀还卡在高位\n\n美联储6月议息会议临近，\n某外资投行出了一份前瞻，\n逻辑清晰，信息量很足。\n几个核心看点，帮你快速理清。\n\n1/ 就业市场：回暖但不算热\n5月非农新增130k，明显好于前几个月。\n投行认为这说明劳动力市场没崩，\n但失业率已从低点回升，\n整体在走向更平衡的状态。\n\n2/ 通胀：关税+能源+芯片，三重叠加\n核心PCE通胀预计全年高于3%，\n关税、油价、存储芯片价格是主要推手。\n2027年这些因素消退后，通胀才会明显回落。\n\n3/ 加息？大概率不会\n历史上，美联储很少因油价冲击而加息。\n只要通胀预期不失控，工资不螺旋上涨，\n加息的概率就不高。\n真正触发加息的信号是：\n通胀预期脱锚，或涨价范围大面积扩散。\n\n4/ 点阵图：今年不降，明年降两次\n预测6月点阵图的中位数：\n2026年维持利率不变，\n2027年和2028年各降一次。\n投行自己的基线假设是：\n2027年6月和12月各降一次。\n\n5/ 政策声明：措辞可能转向中性\n预计删除“额外调整的程度和时机”这种措辞，\n转为更平衡的表述。\n但整体声明还有简化空间。\n\n总结一下：\n就业在好转，通胀还在磨顶，\n\n[... middle omitted ...]\n\n                 | -                                          |\n| Apr-24   | 188                 | -                                          |\n| May-24   | 158                 | -            \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R035",
    "title": "Citi：AI推理层正在从“成本竞赛”转向“稀缺性定价”，市场低估了中间层的结构性机会",
    "digest": "[wechat_article.md]\n# Citi：AI推理层正在从“成本竞赛”转向“稀缺性定价”，市场低估了中间层的结构性机会\n\n这份来自Citi的最新AI行业周报，揭示了一个正在发生的关键转变：AI基础设施的定价逻辑，正在从“算力成本下降驱动应用爆发”的线性叙事，转向一个更复杂、也更有利可图的结构——**稀缺性正在被货币化，而货币化的速度超过了稀缺性被解决的速度。**\n\n这不是一个关于“大模型军备竞赛”的故事，而是一个关于“中间层如何捕获价值”的故事。Citi用六周的数据追踪，给出了一个清晰的信号：市场对AI的关注点，应该从“谁的模型最强”转向“谁在控制推理的分配权”。\n\n以下是这份报告的核心洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 稀缺性正在成为AI基础设施的定价锚，而不是成本\n\nCiti的数据显示，最前沿模型的推理价格在六周内几乎翻倍，而性能只提升了4个点。这并非技术进步放缓，而是一种主动的定价策略。报告明确指出，模型提供商已经开始将“配给”作为产品特征——新的顶级模型在6月22日后被置于使用积分之后，这意味着用户无法无限量按需调用。\n\n与此同时，上一代A100 GPU的租赁价格在过去六周内上涨了11%，而高端B200/B300的价格也在稳步攀升。这与市场普遍预期的“算力成本持续下降”形成了鲜明对比。\n\n**这意味着什么？** 算力不再是纯粹的“commodity”，而是正在被分层定价。稀缺性（无论是物理GPU的稀缺，还是顶级模型推理能力的稀缺）正在成为定价的决定性因素。对于依赖推理成本假设来构建商业模型的投资者和企业决策者来说，这是一个需要重新校准的关键变量。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 最前沿的模型正在主动拉大与开源模型的差距，而非被动降价\n\n一个反直觉的数据是：\n\n[... middle omitted ...]\n\n解读、原始数据的讨论，以及更多来自一线从业者和投资者的视角。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI 算力正在被“挤牙膏式”分配\n\n算力稀缺，正在被加速变现\n\n最近某外资投行出了一份AI推理深度报告，几个点很值得聊👇\n\n**1/ 算力越来越贵，但需求还在膨胀**\n- A100租金6周涨了11%，H100/H200租金微降但B200/B300继续涨\n- 新发布的前沿模型，智商涨了4分，价格直接翻倍\n- 稀缺被货币化的速度，比被解决的速度还快\n\n**2/ 模型格局：闭源 vs 开源，差距在拉大**\n- 闭源模型智商从60→64，开源从54→55\n- 两者差距从6分扩大到9分，闭源在靠技术壁垒守“智商高地”\n- 中端模型速度提升明显，6周从64 tok/s涨到105 tok/s\n\n**3/ 数据中心选址暗藏逻辑**\n- 集中在美国零售电价9-12美分/度的州\n- 可再生能源占比超25%的州，吸引了更多产能\n- 电力成本正从“运营开销”变成“建设资本”\n\n**4/ 新模型在打破“串行”瓶颈**\n- Google开源DiffusionGemma，推理速度比Gemma 4快4倍\n- 非串行生成有质量代价，但方向对了\n- 世界模型（Starchild-1、Agora-1）在拓展AI应用边界\n\n**5/ 路由层是下一个\n\n[... middle omitted ...]\n\nodels, routing architectures, and emerging world models seem to be painting the path forward through performance, efficiencies, and a breadth of applications.\n\nModels. DiffusionGemma (6/10) ac\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R036",
    "title": "JPM：先进核能真正的拐点不是技术，而是客户愿意为第一座电站付费",
    "digest": "[wechat_article.md]\n# JPM：先进核能真正的拐点不是技术，而是客户愿意为第一座电站付费\n\n当Meta选择TerraPower的Natrium反应堆作为其数据中心供电方案时，这件事的意义远超一份商业合同。JPM近期与TerraPower管理层举行了一场炉边对话，这份研报揭示了一个正在被市场低估的结构性变化：先进核能的商业化路径，已经从“政府补贴驱动”转向“科技巨头需求驱动”。\n\n这不是关于反应堆技术是否可行的问题。这个问题在学术界和工程界已经争论了二十年。真正的新信号是，一家年营收超过1600亿美元的科技公司，愿意在电站尚未建成、技术尚未大规模验证的阶段，就投入里程碑式的开发资金。Meta的选择不是对技术的赌注，而是对电力供给结构必须重构的判断。\n\nJPM这份报告的价值不在于它对TerraPower的技术细节做了多少描述，而在于它清晰地展示了先进核能商业模式正在经历的三个根本性转变：客户结构从公用事业转向科技巨头，融资结构从政府拨款转向企业预付，竞争焦点从技术参数转向供应链整合能力。理解这些转变，才能理解为什么这次可能真的不一样。\n\n以下是我们从这份研报中提炼出的核心洞察，以及它对产业竞争格局和投资逻辑的含义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 科技巨头正在成为先进核能的第一推动力，但只有头部玩家能承受FOAK风险\n\nMeta的参与方式值得仔细拆解。JPM报告中提到，Meta经过严格的RFP流程后选择了Natrium技术，并且不是简单地承诺未来购电，而是提供“里程碑式开发资本”——这笔资金将覆盖TerraPower在最终投资决策前的FEED、选址和监管工作，周期大约两年。\n\n这个结构的意义是什么？它解决了先进核能商业化中最棘手的“先有鸡还是先有蛋”问题。第一座电站（FOAK）的成本和风险远高于后续电站，因为供应链尚未建立\n\n[... middle omitted ...]\n\n，但对于认真研究这个赛道的投资者来说，可能是最有价值的信息。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n核电SMR，数据中心的新选择\n\n新型核电正在走近\n\n最近看了某外资投行关于TerraPower的研报，这家比尔·盖茨支持的先进核能公司，正在推进Natrium钠冷快堆技术。信息量很大，分享几个核心点。\n\n1/ 技术亮点：灵活调峰\nNatrium反应堆设计很聪明：\n- 基础负荷345MW\n- 高峰时段10分钟内可提升至500MW+\n- 建设成本与常规堆相当\n这种“负荷跟随”能力对数据中心和电网运营商都很有吸引力。\n\n2/ Meta入局：信号意义强\nMeta经过严格招标流程后选择了TerraPower。合作模式值得关注：\n- 提供里程碑式开发资金\n- 覆盖FID前的FEED、选址、监管工作（约2年）\n- 这种结构对FOAK（首堆）风险是一种有效对冲\n\n3/ 供应链布局有章法\n- 与韩国KHNP、SK、现代形成战略合作\n- 与Framatome合作建设燃料制造设施\n- 每座反应堆需要约15吨HALEU燃料，首堆供应已通过DOE解决\n\n4/ 经济性初现\n研报给出关键数据：\n- NOAK（第N座）LCOE有望低于$90/MWh\n- 叠加ITC后可能降至$60/MWh或更低\n- 但融资仍是规模化部署的最大变量\n\n5/ 短\n\n[... middle omitted ...]\n\nstomer types, including hyperscalers and utilities. Here, Meta's decision to select TerraPower after a rigorous RFP process serves as a clear vote of confidence in the design. On the supply ch\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 12 Jun 2026 05:16 PM EDT\n\nDisseminated 15 Jun 2026 12:15 AM EDT"
  },
  {
    "id": "R037",
    "title": "摩根斯坦利：市场正在严重低估HDD周期的长度与定价弹性",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：市场正在严重低估HDD周期的长度与定价弹性\n\n这份来自摩根斯坦利的研报，核心判断只有一句话：硬盘驱动器（HDD）的繁荣周期远未结束，恰恰相反，市场对它的长度和盈利弹性都严重低估了。\n\n报告基于过去三周在亚洲的密集调研——包括台湾AI峰会、Computex展会以及西部数据亚洲路演——得出了一个清晰的结论：HDD的供需缺口正在扩大，定价权正在向供应商转移，而这一趋势至少将持续到2028年。\n\n摩根斯坦利因此大幅上调了希捷科技（Seagate Technology）和西部数据（Western Digital）的盈利预测与目标价。希捷目标价从767美元上调至1035美元，西部数据从488美元上调至650美元。更重要的是，报告指出，在乐观情景下，这两家公司可能在2025至2028年间实现EPS的10倍增长。\n\n这不是一个关于“周期高点”的故事。这是一个关于结构性供需失衡、供应商理性定价以及AI推理需求意外拉动传统存储的故事。对于关注科技硬件和AI基础设施的投资者来说，这可能是当前最具预期差的机会之一。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 供需缺口正在扩大，而不是收窄——短缺至少延续到2028年\n\n市场对HDD周期的一个常见误判是认为这轮需求高峰已经过去。摩根斯坦利的最新调研完全推翻了这一假设。\n\n报告明确指出，HDD需求正在以每年40-50%的速度增长，而供给（以EB计）的增长仅为30-35%。这意味着供需缺口不仅存在，而且在持续扩大。具体数据是：2026年近线HDD供给将比需求少300EB（约10-15%的缺口），2027年和2028年缺口将进一步扩大至400EB。\n\n为什么需求如此强劲？报告给出了两个关键驱动因素。第一，核心云服务的增长超出了预期。第二，AI推理和智能体（agents）的需求正\n\n[... middle omitted ...]\n\n关键变量，并在第一时间分享来自一线调研和深度分析的最新判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nHDD的春天来了？缺口拉大到2028\n\nHDD供给缺口持续扩大\n\n最近某外资投行亚洲调研发现，HDD的景气周期正在拉长。核心逻辑是：需求增速40-50%，但供给增速只有30-35%，供给缺口将至少持续到2028年。\n\n1/ 需求端在变强\n- 云服务增长超预期，AI推理和Agent应用也在拉动通用服务器出货\n- 超大规模云厂商的HDD部署率接近100%（历史水平约70%），库存水位很低\n- ODM厂商的HDD库存仅有1-2周\n\n2/ 定价权正在转移\n- 当前近线HDD价格约14.3-14.9美元/TB\n- 台湾产业链反馈，HDD厂商目标是2-3年内将价格提升到25-30美元/TB\n- 现货市场已有分销商卖到30-35美元/TB，比合同价高出约30%\n- 厂商不愿签12个月以上的长期合同，更倾向短期定价\n\n3/ 新增产能有限\n- HDD厂商在供给端非常克制，没有新建工厂\n- 近线HDD出货增长只能靠现有产能，未来2-3年增速约30-35%\n- 新进入者门槛极高：热辅助磁记录技术花了10年才量产，涉及磁学、材料、光子学等多学科整合\n\n如果价格真的涨到25美元/TB（研报的乐观情景），两家厂商的EPS可能在2027-\n\n[... middle omitted ...]\n\nlly. STX PT to \\$1,035; WDC to \\$650.\n\n## Key Takeaways\n\nOur checks from Asia over the last 3 weeks highlight strengthening (and broadening) HDD demand and the potential for material pricing u\n\n[... middle omitted ...]\n\ntd>Nutanix Inc (NTNX.O)</td><td>E (01/12/2026)</td><td>$49.31</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R038",
    "title": "摩根斯坦利：欧洲软件股正经历近二十年最深的估值回撤，但市场忽视了结构性分化",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：欧洲软件股正经历近二十年最深的估值回撤，但市场忽视了结构性分化\n\n过去二十年，欧洲软件板块经历过两次深度回撤：一次是全球金融危机，一次是疫情后的利率与估值压缩。现在，第三次正在发生，而且持续时间之长、幅度之大，已经逼近前两次的水平。\n\n摩根斯坦利欧洲软件团队在最新一期周报中，用一张跨越二十年的等权重股价走势图，揭示了一个被市场情绪掩盖的关键事实：自2021年高点以来，欧洲应用软件板块已经连续近1700天没有创出新高，累计跌幅超过35%。这个回撤的深度和长度，只有2008年金融危机和2022年加息周期可以比拟。\n\n但这份报告真正值得注意的判断，不是“软件股跌了很多”，而是“跌得如此之深，恰恰说明市场正在对软件资产的定价逻辑进行根本性重置”。而重置过程中，不同子板块的分化才刚刚开始。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 当前软件股的回撤深度与时长已与金融危机相当，但触发机制完全不同\n\n摩根斯坦利选取了2005年1月之前上市的50余只中大型软件股，以等权重方式构建了一个长期价格指数。结果非常直观：这批股票在2021年底达到历史峰值后，至今未能突破新高。截至报告发布，距离上一次历史高点已经超过1700天，指数从峰值回撤超过35%。\n\n历史对比更具说服力。全球金融危机期间，软件板块同样经历了深度回撤，但彼时的触发因素是系统性金融风险蔓延至实体经济，软件公司的基本面遭受了广泛冲击。2022年的回撤则更多是利率上升带来的估值压缩，市场在重新定价未来现金流的折现率。\n\n而本轮回撤的背景完全不同：AI技术浪潮正在重塑整个软件行业，企业软件支出并未出现断崖式下滑，多数头部公司的营收仍在增长。这意味着，当前的价格下跌并非基本面崩溃的结果，而是市场对“软件公司能否将AI转化为可持续利润”这一命题的深度怀疑。\n\n[... middle omitted ...]\n\n完整研报的解读、关键图表的原始数据，以及基于报告的深度讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n欧洲软件股正经历近20年最大回撤\n\n📉 软件股寒冬有多冷？\n\n某外资投行最新研报追踪了50+只全球软件股（2005年至今），发现一个让人意外的数据：\n\n这批股票在2021年底见顶后，至今已将近1700天没创新高，累计回撤超35%。上一次出现这种深度的回撤，还是2008年全球金融危机和2022年加息周期。\n\n1️⃣ 数据基础设施 vs 应用软件\n研报指出，目前软件板块内部已出现明显分化。数据基础设施和网络安全相关公司表现相对坚挺，但应用软件整体承压，是拖累指数的主力。\n\n2️⃣ AI会计自动化浪潮\n税务和会计行业正面临两大结构性挑战：专业人才持续短缺+监管日益复杂。Thomson Reuters最新报告显示，已有约34%的税务公司和税务部门在组织层面部署了生成式AI。核心税引擎市场预计仍由Wolters Kluwer、Thomson Reuters等老牌玩家主导，因为它们的合规系统和客户工作流已深度绑定。\n\n3️⃣ 融资市场回暖信号\n几个值得关注的融资动态（研报标注为未经确认）：\n- Databricks据传正以1650亿+美元估值融资，较2月的1340亿明显跳升\n- 瑞典AI应用构建平台Lovable据传估值12\n\n[... middle omitted ...]\n\n) Visualising the AI Software Drawdown (#Software): The weak price performance across application software largely stems back to around August last year, albeit we have started to see some sub\n\n[... middle omitted ...]\n\nr><tr><td>Tietoevry Oyj (TIETO.HE)</td><td>U (01/12/2026)</td><td>€20.34</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted."
  },
  {
    "id": "R039",
    "title": "Bernstein：印度市场真正低估的不是电动化，而是混动供给侧的再定价",
    "digest": "[wechat_article.md]\n# Bernstein：印度市场真正低估的不是电动化，而是混动供给侧的再定价\n\n印度汽车市场正在上演一场被大多数投资者忽略的结构性变化。2025年，在没有任何中央补贴、仅有8款在售车型、且大型混动车面临40%高税率的环境下，强混动销量依然实现了超过85%的增长，渗透率从1.4%跃升至2.4%。同期，印度市场有35至40款纯电动车型在售，享受5%的低税率，但增速反而落后。\n\n这不是一个需求问题。这是一个供给问题。Bernstein这份研报的核心判断是：印度强混动市场的规模几乎完全由车型供给决定，而供给侧的拐点即将到来。当车型目录在未来十八个月内翻倍，市场将进入一个全新的定价阶段。\n\n为什么这个判断现在值得认真对待？因为在全球范围内，混动正在重新获得关注。美国、欧洲和日本市场在补贴退坡后，混动增速已反超纯电。印度作为全球第三大汽车市场，其混动渗透率目前仅2.3%，但车型数量只有成熟市场的十分之一。如果供给是关键变量，那么当前的渗透率数字可能严重低估了潜在需求。\n\n报告的核心主张是：印度强混动市场将从当前约2.3%的渗透率，在2030年前提升至7%至8%，驱动因素不是政策变化，而是车型供给的集中释放。这一判断的置信度被刻意锚定在本十年的后半段，因为纯电成本下降和税收壁垒是真实存在的风险。但正是这种克制，让报告的结论更加可信。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 83%的增长来自8款车型，这不是巧合，是“被压抑的需求”\n\n印度市场实际上已经无意中做了一次压力测试。在8款强混动车型面对35至40款纯电动车型、混动车享受零补贴且大型混动税率高达40%的条件下，混动销量在2025年增长了83%。Bernstein的数据显示，2025年印度强混动零售量达到10.7万辆，而2024年仅为5.76万辆。\n\n这个数字需要放在\n\n[... middle omitted ...]\n\n销售数据，与群友一起验证或修正Bernstein的判断框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n印度混动车，被低估的拐点将至\n\n混动拐点前夜\n\n谁在卡位，谁在观望\n\n最近看了份外资投行关于印度混动车的深度报告，逻辑很清晰，分享几个核心判断。\n\n1/ 混动车卖不好，不是没人要，是没得选\n2025年印度只有8款强混车型在售，而纯电车有35-40款。但混动车销量增长了85%+，远超纯电。被课以40%高税、无补贴，还能卖成这样，说明需求是真的。消费者用脚投票，产品力自己会说话。\n\n2/ 关键转折点在2028年\n报告预测，到2030年混动渗透率将从现在的2.3%提升到7-8%。核心驱动力不是政策，而是车型供给。从2027年起，Maruti、现代、起亚、雷诺等将密集投放新混动车型，产品线翻倍不止。Maruti的自家混动系统（不再依赖丰田授权）将把价格打到100-150万卢比区间，首次进入主流市场。\n\n3/ Maruti的策略很聪明\n它不赌单一技术路线。到2030年，规划动力总成比例是CNG 35%、燃油25%、混动25%、纯电15%。不求猜对赢家，只求每个赛道都有牌打。更妙的是，在最新车型上，全景天窗、ADAS、通风座椅等高端配置只给混动顶配，用配置差异引导消费者选混动。\n\n4/ 残值和用车成本是隐形优势\n报告指出\n\n[... middle omitted ...]\n\nstrong hybrid models versus 35-40 BEVs. Larger hybrids (>4m) are taxed at 40%, no different from large ICE SUVs, while EVs sit at 5%. There is no central subsidy, and the only meaningful state\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R040",
    "title": "GS：AI眼镜渠道扩容的真正赢家不是Best Buy，而是能完成处方闭环的零售商",
    "digest": "[wechat_article.md]\n# GS：AI眼镜渠道扩容的真正赢家不是Best Buy，而是能完成处方闭环的零售商\n\n当Best Buy宣布与Meta合作，在50多家门店内开设“Meta Lab”体验空间时，市场的第一反应往往是：电子产品零售商要抢眼镜店的生意了。这个直觉并不错，但它忽略了一个更关键的结构性事实——AI眼镜的购买决策，正在从“电子消费品”向“视力健康产品”迁移。而在这个迁移过程中，真正构成竞争壁垒的，不是门店数量或展示面积，而是能否在同一个场景里完成验光、处方、镜片定制和框架适配的闭环。\n\nGS在6月发布的一份专题研报中，系统评估了Best Buy与Meta合作对美国主要眼镜零售商的影响。结论清晰且反直觉：对于National Vision（EYE）和Warby Parker（WRBY）而言，这个合作并非威胁；对于EssilorLuxottica（ESLX）而言，反而是利好。真正需要关注的，是当渠道扩容加速了消费者教育之后，谁有能力将“尝鲜流量”转化为“处方收入”。\n\n这份报告的价值不在于它判断了股价涨跌，而在于它提供了一个分析框架：在AI眼镜从极客玩具走向大众消费品的过程中，竞争壁垒的构成要素正在被重新定义。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 消费者对AI眼镜的首要需求不是“体验”，而是“配好”\n\nGS在报告中披露了一个关键数据：超过50%的Best Buy消费者希望在购买AI眼镜前能够亲眼看到实物。这个数据本身并不令人意外，真正重要的是它揭示的消费者决策链条——人们走进门店，不只是为了摸一摸产品，而是为了确认“这副眼镜戴在我脸上是否合适、是否可以配上我的处方”。\n\n这正是眼镜零售商与电子产品零售商之间最本质的差异。National Vision在美国拥有超过1000家门店，每家门店都配备了验光师和现场镜片加工能\n\n[... middle omitted ...]\n\n始数据图表，并围绕报告中尚未完全回答的关键问题进行深度讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nBest Buy × Meta，护眼零售商慌不慌？\n\n**AI眼镜进Best Buy**\n\n**对三大眼镜零售商影响有多大？**\n\n---\n\n6月8日，Best Buy宣布与Meta合作，在50多家门店开设“Meta Lab”，展示Ray-Ban Meta、Oakley Meta等AI眼镜和VR设备，提供试戴、虚拟搭配等服务。\n\n这对专业眼镜零售商是威胁还是助攻？研报拆解了三家的情况：\n\n**1️⃣ National Vision（EYE）—— 影响最小**\n\n优势在于“一站式”：验光+配镜+取镜一次完成。如果顾客在Best Buy买AI眼镜需要配镜片，还得寄回实验室，流程很麻烦。而且National Vision已全面铺开Ray-Ban Meta，管理称这是店内卖得最快的SKU，客单价也最高。\n\n**2️⃣ Warby Parker（WRBY）—— 关注度上升，但非直接风险**\n\nWarby Parker计划2026年秋季推出与Google/Samsung合作的AI眼镜，初期只在自家337家门店和线上渠道销售，不走批发。研报认为Best Buy合作能扩大品类认知，反而可能帮Warby Parker引流。但市\n\n[... middle omitted ...]\n\n commentary following the announcement.\n\nBottom line: We are encouraged to see Best Buy and Meta's partnership, and its potential to expand adoption of AI smart glasses across the industry. Fo\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R041",
    "title": "GS：中国钛白粉出口韧性正在重塑全球定价权，而非简单的产能外溢",
    "digest": "[wechat_article.md]\n# GS：中国钛白粉出口韧性正在重塑全球定价权，而非简单的产能外溢\n\n中国钛白粉（TiO2）的出口数据，正在讲述一个与市场主流叙事不同的故事。\n\n过去两年，市场普遍认为中国钛白粉的全球扩张主要依赖低成本优势，且极易受到上游原料短缺（如硫磺问题）或贸易政策（如印度反倾销税）的扰动。但GS最新发布的这份研报显示，一个更深刻的结构性变化正在发生：中国钛白粉的出口供给弹性远超预期，即便在面临硫磺供应紧张的情况下，2026年前四个月的净出口量仍同比增加了8.8万吨，增幅达14%。这一数字不仅否定了“供给端会自动调节”的简单假设，更直接冲击了西方钛白粉生产商（如科慕、特诺、Kronos）在核心市场的定价能力。\n\n这份报告的核心判断是：市场低估了中国钛白粉出口的“韧性”，而这将导致2025年下半年西方生产商预期的涨价幅度低于预期。这不是一次性的数据波动，而是全球钛白粉定价权从供给侧结构性转移的信号。理解这一点，是判断未来12个月该行业资产价格走势的前提。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 中国出口的韧性正在打破传统的“供给-价格”调节逻辑\n\nGS分析师在报告中明确指出，他们长期将中国的净出口量视为衡量西方钛白粉生产商市场健康状况的关键指标。这一指标的逻辑在于：中国出口越多，全球市场供给越宽松，西方生产商的涨价空间就越小。\n\n然而，2026年以来的数据打破了两个市场共识。第一个共识是“硫磺问题会自然限制中国出口”。GS在报告中坦言，4月份出口数据的高企令他们感到意外，因为此前市场普遍预期上游硫磺的供应紧张会抑制中国工厂的开工率。但现实是，中国生产商的供应链韧性远超预期，他们通过调整原料结构或利用库存，成功维持了高水平的出口。第二个共识是“印度反倾销税的不确定性会抑制出口”。印度反倾销税目前仍处于暂停状态，且司法裁决时\n\n[... middle omitted ...]\n\n图表和模型参数，共同推演下半年全球钛白粉市场的多种可能路径。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国钛白粉出口，比想象中更猛\n\n📊出口数据超预期\n\n刚看完某外资投行的最新研报，4月中国钛白粉出口数据出来了，净出口量持续高位运行，前4个月累计同比增加8.8万吨（+14%）。\n\n1️⃣ 出口为何这么强？\n- 印度市场：4月出口飙升至3.2万吨，同比增1.4万吨，前4个月累计增3.2万吨（+28%）\n- 欧盟市场：4月出口2万吨，同比增0.4万吨，前4个月累计增1.9万吨（+32%）\n- 关键点：虽然中国钛白粉生产面临硫磺供应问题，但出口韧性比预期强太多\n\n2️⃣ 对市场意味着什么？\n- 中国高出口量会压制下半年价格涨幅\n- 印度反倾销税仍暂停中，一旦恢复将快速影响市场（因为中国在印度没有保税仓库）\n- 涂料需求（钛白粉最大下游）年初表现弱于预期，供需两端都在走软\n\n3️⃣ 企业层面看点\n- KRO（某钛白粉企业）受益于2025年底降负荷运行，2026上半年成本压力缓解\n- 2Q26 EBITDA预期从1900万上调至3600万，上调86%\n- 但需注意：下半年产量可能追上销量，供需平衡会变化\n\n整体看，中国钛白粉的全球竞争力还在提升，西方生产商压力不小。\n\n大家觉得印度反倾销税会恢复吗？欢迎一起讨论～\n\n#\n\n[... middle omitted ...]\n\nn anti-dumping duty (ADD) remains suspended, with no definitive timeline for a judicial decision regarding its potential reinstatement; however since China lacks bonded warehouses in India, an\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R004",
    "label": "Exhibit 1",
    "context": "EXHIBIT 1: May South Korea imports for SPE was \\$3.2bn, -5% MoM."
  },
  {
    "figure_id": "F002",
    "report_id": "R004",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: May South Korea imports for Japanese SPE was \\$651mn, -7% MoM."
  },
  {
    "figure_id": "F003",
    "report_id": "R004",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: South Korea SPE monthly import data has good directional correlation with Samsung and SK hynix's quarterly capex."
  },
  {
    "figure_id": "F004",
    "report_id": "R004",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: 1QCY26 capex came down QoQ for both Samsung and SK hynix due to seasonality and some front loaded infrastructure investments in 4Q25, but we expect their capex will pick up again soon. Capex (KRW B)"
  },
  {
    "figure_id": "F005",
    "report_id": "R004",
    "label": "Exhibit 6",
    "context": "EXHIBIT 5: May tester imports from Japan and Malaysia collectively was +5% MoM."
  },
  {
    "figure_id": "F006",
    "report_id": "R004",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: South Korea tester imports data shows good directional correlation with Advantest's South Korea sales."
  },
  {
    "figure_id": "F007",
    "report_id": "R004",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: Advantest's Quarterly Korean sales shows good correlation with Korean monthly imports. Advantest Quarterly KR Sales vs. KR 2M Import: 1QCY16-1QCY26"
  },
  {
    "figure_id": "F008",
    "report_id": "R004",
    "label": "Exhibit 10",
    "context": "EXHIBIT 9: May imports from Japan for WFE equipment where TEL has exposure, were collectively -27% MoM."
  },
  {
    "figure_id": "F009",
    "report_id": "R004",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: South Korea monthly WFE imports from Japan show good directional correlation with TEL's South Korea revenue."
  },
  {
    "figure_id": "F010",
    "report_id": "R004",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: TEL's Quarterly Korean sales shows decent correlation with Korean monthly imports. TEL Quarterly KR Sales vs. KR Import: 1st 2 Months of 1QCY16-1QCY26"
  },
  {
    "figure_id": "F011",
    "report_id": "R004",
    "label": "Exhibit 13",
    "context": "EXHIBIT 13: South Korea monthly SPE imports from Netherlands shows good directional correlation with ASML's South Korea revenue divided by 3. May Litho Imports of €928mn increased 28% MoM and \\~150% YoY."
  },
  {
    "figure_id": "F012",
    "report_id": "R004",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: Regressing ASML Korea's quarterly system sales on the first 2-month plus 1-month lag of import data, we obtain an $R^{2}$ of 81% and estimate that Q2 ASML Korea revenue will reach €2.31bn, down 26% QoQ from the record Q1"
  },
  {
    "figure_id": "F013",
    "report_id": "R004",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: Our regression indicates very strong KR sales at EUR 2.31Bn, down 18% sequentially due to the record level reached last quarter, implying that KR accounts for approximately 37% of total ASML system sales. EXHIBIT 16: We"
  },
  {
    "figure_id": "F014",
    "report_id": "R006",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Our preferred gauge suggests increased FX inflows in May"
  },
  {
    "figure_id": "F015",
    "report_id": "R006",
    "label": "Exhibit 2",
    "context": "Exhibit 2: FX conversion ratio for goods trade balance fell from April to May"
  },
  {
    "figure_id": "F016",
    "report_id": "R006",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Foreign investors started to buy CNY bonds in May China monthly bond flow in the interbank market"
  },
  {
    "figure_id": "F017",
    "report_id": "R006",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Banks' net external assets increased in May, and official FX reserves rose after adjusting for FX valuation effect"
  },
  {
    "figure_id": "F018",
    "report_id": "R007",
    "label": "Figure 1",
    "context": "Figure 1: US Credit Impulse vs. Growth/Value US credit impulse closely tracks the return spread between growth and value in MSCI China."
  },
  {
    "figure_id": "F019",
    "report_id": "R007",
    "label": "Figure 2",
    "context": "Figure 2: CN Credit Impulse vs. Growth/Value China credit impulse closely tracks the same spread since the 2018 A-share inclusion."
  },
  {
    "figure_id": "F020",
    "report_id": "R007",
    "label": "Figure 3",
    "context": "Figure 3: Aggregate Credit Impulse For Growth/Value Rotation"
  },
  {
    "figure_id": "F021",
    "report_id": "R012",
    "label": "Figure 1",
    "context": "Figure 1: SEK has underperformed since March G10 FX performance: since start March vs last 3d"
  },
  {
    "figure_id": "F022",
    "report_id": "R012",
    "label": "Figure 2",
    "context": "Figure 2: Food is a much larger share of consumption for frontier and EM economies, with Nigeria, Ghana, Pakistan, Egypt and the Philippines among those potentially most impacted Food as a share of household consumption"
  },
  {
    "figure_id": "F023",
    "report_id": "R012",
    "label": "Figure 3",
    "context": "Figure 3: CLP screens cheap relative to rest of LatAm"
  },
  {
    "figure_id": "F024",
    "report_id": "R012",
    "label": "Figure 4",
    "context": "Figure 4: INR positioning remains short"
  },
  {
    "figure_id": "F025",
    "report_id": "R013",
    "label": "Exhibit 1",
    "context": "Exhibit 1: For any given month, information on tanker movements firms up over time. Based on known voyages, it appears that net seaborne oil imports into China will decline even further in June vs May, and even July is tracking bel"
  },
  {
    "figure_id": "F026",
    "report_id": "R013",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Outbound tanker transit are still sharply below pre-conflict levels but notably improved since early May"
  },
  {
    "figure_id": "F027",
    "report_id": "R013",
    "label": "Exhibit 6",
    "context": "Exhibit 6: US seaborne net exports are nearly 4 mb/d higher than last year..."
  },
  {
    "figure_id": "F028",
    "report_id": "R013",
    "label": "Exhibit 7",
    "context": "Exhibit 7: ...whilst China's seaborne net imports are down \\~ 6mb/d"
  },
  {
    "figure_id": "F029",
    "report_id": "R013",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Based on the pace at which known tanker movements firm up, seaborne net exports from the US are tracking similar to April, which is also where May levels ended up US seaborne total-petroleum net exports: firming fan"
  },
  {
    "figure_id": "F030",
    "report_id": "R013",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Along similar lines, known tanker movements in/out of China suggest that June net imports will likely be even lower than May, and July is also tracking below the May level as well China seaborne total-petroleum net impor"
  },
  {
    "figure_id": "F031",
    "report_id": "R013",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Known spot crude deals entered into by Chinese players do not signal a pickup in buying interest yet China crude deals tracking Known crude supply agreements, relative to last day of delivery month (mb/d)"
  },
  {
    "figure_id": "F032",
    "report_id": "R013",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Expecting the Strait of Hormuz to open soon, German households have not been filling their heating oil tanks - consumption has continued but buying is delayed German heating oil tank fill Private household heating oil"
  },
  {
    "figure_id": "F033",
    "report_id": "R013",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Global energy prices compared"
  },
  {
    "figure_id": "F034",
    "report_id": "R013",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Benchmark crude oil prices"
  },
  {
    "figure_id": "F035",
    "report_id": "R013",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Calendar spreads Mo1 vs Mo2"
  },
  {
    "figure_id": "F036",
    "report_id": "R013",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Calendar spreads Mo2 vs Mo6"
  },
  {
    "figure_id": "F037",
    "report_id": "R013",
    "label": "Exhibit 19",
    "context": "Exhibit 19: WTI/Brent spread"
  },
  {
    "figure_id": "F038",
    "report_id": "R013",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Brent futures"
  },
  {
    "figure_id": "F039",
    "report_id": "R013",
    "label": "Exhibit 21",
    "context": "Exhibit 21: Brent CFD curve"
  },
  {
    "figure_id": "F040",
    "report_id": "R013",
    "label": "Exhibit 22",
    "context": "Exhibit 22: CFD curve structure Spread between week 2 and week 6 (\\$/bbl)"
  },
  {
    "figure_id": "F041",
    "report_id": "R013",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Brent DFL curve"
  },
  {
    "figure_id": "F042",
    "report_id": "R013",
    "label": "Exhibit 24",
    "context": "Exhibit 24: DFL curve structure Spread between month 1 and month 6 (\\$/bbl)"
  },
  {
    "figure_id": "F043",
    "report_id": "R013",
    "label": "Exhibit 25",
    "context": "Exhibit 25: Cash Dubai premium Platts Cash Dubai vs M2 Dubai swaps spread (\\$/bbl)"
  },
  {
    "figure_id": "F044",
    "report_id": "R013",
    "label": "Exhibit 26",
    "context": "Exhibit 26: Brent/Dubai spread (\\$/bbl)"
  },
  {
    "figure_id": "F045",
    "report_id": "R013",
    "label": "Exhibit 27",
    "context": "Exhibit 27: North sea"
  },
  {
    "figure_id": "F046",
    "report_id": "R013",
    "label": "Exhibit 29",
    "context": "Exhibit 29: Nigeria"
  },
  {
    "figure_id": "F047",
    "report_id": "R013",
    "label": "Exhibit 31",
    "context": "Exhibit 31: Russia"
  },
  {
    "figure_id": "F048",
    "report_id": "R013",
    "label": "Exhibit 28",
    "context": "Exhibit 28: Angola Differential to Dated Brent strip (\\$/bbl)"
  },
  {
    "figure_id": "F049",
    "report_id": "R013",
    "label": "Exhibit 30",
    "context": "Exhibit 30: Kazakhstan Differential to Dated Brent strip (\\$/bbl)"
  },
  {
    "figure_id": "F050",
    "report_id": "R013",
    "label": "Exhibit 32",
    "context": "Exhibit 32: Iran Differential to Dated Brent strip (\\$/bbl)"
  },
  {
    "figure_id": "F051",
    "report_id": "R013",
    "label": "Exhibit 33",
    "context": "Exhibit 33: Heavy vs Light Premium/(discount) for every 1 degree increase in API Gravity (\\$/bbl)"
  },
  {
    "figure_id": "F052",
    "report_id": "R013",
    "label": "Exhibit 34",
    "context": "Exhibit 34: Sweet vs Sour Premium/(discount) for every 1% increase in sulfur content (\\$/bbl)"
  },
  {
    "figure_id": "F053",
    "report_id": "R013",
    "label": "Exhibit 35",
    "context": "Exhibit 35: East vs West of Suez Premium/(discount) for West- over East-of-Suez crudes (\\$/bbl)"
  },
  {
    "figure_id": "F054",
    "report_id": "R013",
    "label": "Exhibit 36",
    "context": "Exhibit 36: Russian vs non-Russian origin Premium/(discount) for Russian crudes (\\$/bbl)"
  },
  {
    "figure_id": "F055",
    "report_id": "R013",
    "label": "Exhibit 37",
    "context": "Exhibit 37: Cracking netback margin - Northwest Europe"
  },
  {
    "figure_id": "F056",
    "report_id": "R013",
    "label": "Exhibit 38",
    "context": "Exhibit 38: Cracking netback margin - Northwest Europe"
  },
  {
    "figure_id": "F057",
    "report_id": "R013",
    "label": "Exhibit 39",
    "context": "Exhibit 39: Cracking netback margin - Southeast Asia"
  },
  {
    "figure_id": "F058",
    "report_id": "R013",
    "label": "Exhibit 40",
    "context": "Exhibit 40: Cracking netback margin - Southeast Asia"
  },
  {
    "figure_id": "F059",
    "report_id": "R013",
    "label": "Exhibit 41",
    "context": "Exhibit 41: Cracking netback margin - Western Mediterranean"
  },
  {
    "figure_id": "F060",
    "report_id": "R013",
    "label": "Exhibit 42",
    "context": "Exhibit 42: Cracking netback margin - USGC"
  },
  {
    "figure_id": "F061",
    "report_id": "R013",
    "label": "Exhibit 43",
    "context": "Exhibit 43: ## Refined product crack spreads vs Dated Brent; basis: Antwerp-Rotterdam-Amsterdam (\\$/bbl)"
  },
  {
    "figure_id": "F062",
    "report_id": "R013",
    "label": "Exhibit 44",
    "context": "Exhibit 44: Forward refining margins Based on typical European configuration (\\$/bbl)"
  },
  {
    "figure_id": "F063",
    "report_id": "R013",
    "label": "Exhibit 45",
    "context": "Exhibit 45: China Bohai Bay product crack spreads, excl. tax, \\$/bbl)"
  },
  {
    "figure_id": "F064",
    "report_id": "R013",
    "label": "Exhibit 46",
    "context": "Exhibit 46: Naphtha"
  },
  {
    "figure_id": "F065",
    "report_id": "R013",
    "label": "Exhibit 47",
    "context": "Exhibit 47: Gasoline"
  },
  {
    "figure_id": "F066",
    "report_id": "R013",
    "label": "Exhibit 48",
    "context": "Exhibit 48: Jet fuel"
  },
  {
    "figure_id": "F067",
    "report_id": "R013",
    "label": "Exhibit 49",
    "context": "Exhibit 49: Gasoil/diesel"
  },
  {
    "figure_id": "F068",
    "report_id": "R013",
    "label": "Exhibit 50",
    "context": "Exhibit 50: Gasoil/diesel"
  },
  {
    "figure_id": "F069",
    "report_id": "R013",
    "label": "Exhibit 51",
    "context": "Exhibit 51: High-sulphur fuel oil"
  },
  {
    "figure_id": "F070",
    "report_id": "R013",
    "label": "Exhibit 53",
    "context": "Exhibit 53: Refinery outages"
  },
  {
    "figure_id": "F071",
    "report_id": "R013",
    "label": "Exhibit 54",
    "context": "Exhibit 54: Refinery outages"
  },
  {
    "figure_id": "F072",
    "report_id": "R013",
    "label": "Exhibit 57",
    "context": "Exhibit 57: Observable crude oil and oil products inventories On land, at sea and in-transit (mln bbl)"
  },
  {
    "figure_id": "F073",
    "report_id": "R013",
    "label": "Exhibit 58",
    "context": "Exhibit 58: Observable crude oil inventories On land, at sea and in-transit (mln bbl)"
  },
  {
    "figure_id": "F074",
    "report_id": "R013",
    "label": "Exhibit 59",
    "context": "Exhibit 59: Observable crude oil and oil products inventories In commercial storage only (mln bbl)"
  },
  {
    "figure_id": "F075",
    "report_id": "R013",
    "label": "Exhibit 60",
    "context": "Exhibit 60: OECD commercial oil inventories Total oil, on land only (mln bbl)"
  },
  {
    "figure_id": "F076",
    "report_id": "R013",
    "label": "Exhibit 61",
    "context": "Exhibit 61: Observable refined oil products inventories On land, at sea and in-transit (mln bbl)"
  },
  {
    "figure_id": "F077",
    "report_id": "R013",
    "label": "Exhibit 62",
    "context": "Exhibit 62: Observable refined oil products inventories, on-land only (mln bbl)"
  },
  {
    "figure_id": "F078",
    "report_id": "R013",
    "label": "Exhibit 63",
    "context": "Exhibit 63: Observable crude oil inventories in China On land (mln bbl)"
  },
  {
    "figure_id": "F079",
    "report_id": "R013",
    "label": "Exhibit 64",
    "context": "Exhibit 64: Observable crude oil inventories outside China On land, at sea and in-transit (mln bbl)"
  },
  {
    "figure_id": "F080",
    "report_id": "R013",
    "label": "Exhibit 65",
    "context": "Exhibit 65: OPEC 9+3 Seaborne exports of crude oil and oil products (mb/d)"
  },
  {
    "figure_id": "F081",
    "report_id": "R013",
    "label": "Exhibit 66",
    "context": "Exhibit 66: Non-OPEC"
  },
  {
    "figure_id": "F082",
    "report_id": "R013",
    "label": "Exhibit 67",
    "context": "Exhibit 67: Saudi Arabia Seaborne crude oil exports (mb/d)"
  },
  {
    "figure_id": "F083",
    "report_id": "R013",
    "label": "Exhibit 68",
    "context": "Exhibit 68: Brazil and Guyana Seaborne exports of crude oil (30-day moving avg; mb/d)"
  },
  {
    "figure_id": "F084",
    "report_id": "R013",
    "label": "Exhibit 69",
    "context": "Exhibit 69: Russia Seaborne crude oil exports (mb/d)"
  },
  {
    "figure_id": "F085",
    "report_id": "R013",
    "label": "Exhibit 70",
    "context": "Exhibit 70: Iran Seaborne crude oil exports (mb/d)"
  },
  {
    "figure_id": "F086",
    "report_id": "R013",
    "label": "Exhibit 71",
    "context": "Exhibit 71: Total oil"
  },
  {
    "figure_id": "F087",
    "report_id": "R013",
    "label": "Exhibit 73",
    "context": "Exhibit 73: Gasoil and Heating Oil"
  },
  {
    "figure_id": "F088",
    "report_id": "R013",
    "label": "Exhibit 72",
    "context": "Exhibit 72: Brent and WTI"
  },
  {
    "figure_id": "F089",
    "report_id": "R013",
    "label": "Exhibit 74",
    "context": "Exhibit 74: Gasoline - NY Harbour RBOB"
  },
  {
    "figure_id": "F090",
    "report_id": "R013",
    "label": "Exhibit 75",
    "context": "Exhibit 75: Motor fuel imports Top 100 ports (mb/d)"
  },
  {
    "figure_id": "F091",
    "report_id": "R013",
    "label": "Exhibit 77",
    "context": "Exhibit 77: Clean products net imports Nigeria (30-day moving avg; mb/d)"
  },
  {
    "figure_id": "F092",
    "report_id": "R013",
    "label": "Exhibit 79",
    "context": "Exhibit 79: Global oil & gas capex (by Woodmac) (\\$bn)"
  },
  {
    "figure_id": "F093",
    "report_id": "R013",
    "label": "Exhibit 76",
    "context": "Exhibit 76: Seaborne crude oil arrivals - Europe Change vs seasonal average from 2016-23 (mb/d)"
  },
  {
    "figure_id": "F094",
    "report_id": "R013",
    "label": "Exhibit 78",
    "context": "Exhibit 78: Crude oil imports China, split by origin"
  },
  {
    "figure_id": "F095",
    "report_id": "R013",
    "label": "Exhibit 80",
    "context": "Exhibit 80: Upstream capital cost Index: 1Q 2000 = 100"
  },
  {
    "figure_id": "F096",
    "report_id": "R015",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Investors are split on de-risking the AI trade, with 41% remaining unhedged and another 41% rotating into other sectors or underweighting How are you currently hedging downside risk in the AI trade over the next 6-12 mon"
  },
  {
    "figure_id": "F097",
    "report_id": "R015",
    "label": "Exhibit 2",
    "context": "Exhibit 2: APAC ex-Japan growth expectations turned positive in June, marking a continued recovery from April's sharp downturn Net % expecting a stronger Global / APAC ex-Japan economy"
  },
  {
    "figure_id": "F098",
    "report_id": "R015",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Inflation expectations remain elevated but eased in June, though still sitting well above the long-term average Net % expecting higher inflation in Asia Pacific ex-Japan in the next 12 months"
  },
  {
    "figure_id": "F099",
    "report_id": "R015",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Corporate profit expectations strengthened further in June, well above the long-run average Net % expecting better corporate profits in Asia Pacific ex-Japan in the next 12 months"
  },
  {
    "figure_id": "F100",
    "report_id": "R015",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Concern that APAC ex-Japan earnings estimates are too high continue to fade in June, now at 14th percentile historically Net % deeming consensus EPS estimates for the coming year as high"
  },
  {
    "figure_id": "F101",
    "report_id": "R015",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Energy security concerns have normalized: high/extreme concern dropped 73pts since Apr, while moderate concern became the majority view How concerned are you about energy security risks for APAC region in current geopoli"
  },
  {
    "figure_id": "F102",
    "report_id": "R015",
    "label": "Exhibit 7",
    "context": "Exhibit 7: China growth sentiment remains negative, with net reading unchanged at -14% vs. May Net % expecting a stronger Chinese economy in the next 12 months"
  },
  {
    "figure_id": "F103",
    "report_id": "R015",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Japan growth expectations improved further in June, surpassing the long-term average Net % expecting a stronger Japanese economy over the next 12 months"
  },
  {
    "figure_id": "F104",
    "report_id": "R015",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Investors expect the next rate hike to be most likely in Jun When do you think the BOJ next rate hike will be? When do you think the BOJ next rate hike will be?"
  },
  {
    "figure_id": "F105",
    "report_id": "R015",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Investor optimism cooled after last month's improvement but remains broadly in line with historical norms FMS views on expected upside for Asia Pac ex-Japan equities over the next 12 months"
  },
  {
    "figure_id": "F106",
    "report_id": "R015",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Similar to Asia ex, optimism in Japan has normalized after last month's peak FMS views on expected upside for Japan equities over the next 12 months"
  },
  {
    "figure_id": "F107",
    "report_id": "R015",
    "label": "Exhibit 12",
    "context": "Exhibit 12: FMS investors still see APAC ex-Japan equities as slightly undervalued Net % saying Asia Pacific ex-Japan equities are overvalued"
  },
  {
    "figure_id": "F108",
    "report_id": "R015",
    "label": "Exhibit 13",
    "context": "Exhibit 13: AI upside still looks underappreciated. Only 9% of FMS investors say the positive AI impact on equities is more than fully priced in How much of the positive AI impact on equities is already reflected in the price?"
  },
  {
    "figure_id": "F109",
    "report_id": "R015",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Within China, AI/semis and buybacks/dividend remain key investor priorities FMS views on TWO most favorite themes in China"
  },
  {
    "figure_id": "F110",
    "report_id": "R015",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Earnings increasingly seen as key driver for Japan equities, rising to 41% in Jun, while policy normalization also gained traction at 27% Key themes for Japan equities in the near-to-medium term"
  },
  {
    "figure_id": "F111",
    "report_id": "R015",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Investor expectations for the Korea/Taiwan semis cycle eased from May but stay firmly positive in June FMS views on the semis cycle (Korea/Taiwan exports growth) over the next 12 months"
  },
  {
    "figure_id": "F112",
    "report_id": "R015",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Taiwan remains the clear AI-cycle beneficiary, while US gained momentum in Jun Which market benefits most from the next phase of the AI cycle?"
  },
  {
    "figure_id": "F113",
    "report_id": "R015",
    "label": "Exhibit 18",
    "context": "Exhibit 18: The absence of a clear AI play remains the primary concern for the Indian market. What is your key concern for Indian market?"
  },
  {
    "figure_id": "F114",
    "report_id": "R015",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Indonesia overtook India as investors' least preferred market, while North Asia remains the clear favorite Asia Pacific market sentiment: Net % overweight Asia Pacific market sentiment: Net % overweight (% saying overwei"
  },
  {
    "figure_id": "F115",
    "report_id": "R015",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Investors are cautious on ASEAN and Korea in the event of an economic downturn If global growth weakens further, you would first reduce exposure to...?"
  },
  {
    "figure_id": "F116",
    "report_id": "R015",
    "label": "Exhibit 21",
    "context": "Exhibit 21: FMS investors are now more overweight in Tech Hardware than Semis, with Financial Services emerging as a new favored sector Asia Pacific ex-Japan sector sentiment: Net % overweight APAC ex-Japan sector sentiment: Net % F"
  },
  {
    "figure_id": "F117",
    "report_id": "R015",
    "label": "Exhibit 22",
    "context": "Exhibit 22: June saw a rotation out of Materials and Consumer Discretionary (ex Retailing) into Financial Services and Telecom Monthly change in FMS investor positioning APAC ex-Japan sector sentiment: MoM ppt change in FMS investor"
  },
  {
    "figure_id": "F118",
    "report_id": "R015",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Semiconductors and Banks remain investor favorites in Japan, while Tech Hardware has risen to match Banks FMS opinion on the two most overweight sectors in Japan FMS opinion on the two most overweight sectors in Japan"
  },
  {
    "figure_id": "F119",
    "report_id": "R016",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Brokers are demonstrating strong performance, +7%/+5% vs. +1%/+3% of banks for A/H share since June 9. As of June 15 Price performance since June 9"
  },
  {
    "figure_id": "F120",
    "report_id": "R016",
    "label": "Exhibit 2",
    "context": "Exhibit 2: The average leverage for the offshore subsidiaries of the three brokers in our coverage is 11x, compared to the group average leverage of 6x As of 2025"
  },
  {
    "figure_id": "F121",
    "report_id": "R016",
    "label": "Exhibit 3",
    "context": "Exhibit 3: The average ROE for the offshore subsidiaries of the three brokers in our coverage is 16%, compared to the group average leverage of 9% As of 2025"
  },
  {
    "figure_id": "F122",
    "report_id": "R016",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Investors participating in IPOs over the past two years could have achieved approximately 40% returns on average in the first month Average post-IPO returns (in absolute terms for all HK Main Board IPOs)"
  },
  {
    "figure_id": "F123",
    "report_id": "R016",
    "label": "Exhibit 6",
    "context": "Exhibit 6: During the 2020-23 period, the investment income growth of our covered brokers ranged from a peak of $265\\%$ to a trough of $-72\\%$ YoY, with the valuation of H-shares for the brokers declining from a peak of 12x to a tr"
  },
  {
    "figure_id": "F124",
    "report_id": "R016",
    "label": "Exhibit 7",
    "context": "Exhibit 7: We therefore believe principal investment tends to exacerbate the volatility of brokers' earnings and not drive an uplift in their valuation multiples"
  },
  {
    "figure_id": "F125",
    "report_id": "R016",
    "label": "Exhibit 8",
    "context": "Exhibit 8: CICC's offshore business contributes the most to both revenue and profit, at over $40\\%$ , the highest among Chinese brokers As of 2025 International business contribution (2025)"
  },
  {
    "figure_id": "F126",
    "report_id": "R016",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Following CITICS' Rmb 16bn refinancing, we calculate the leverage of its international business will decrease from 16.6x to 10.6x, creating greater room for expansion"
  },
  {
    "figure_id": "F127",
    "report_id": "R017",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Primary GFA sold last week was $+1\\%$ wow and flat yoy in c.75 cities"
  },
  {
    "figure_id": "F128",
    "report_id": "R017",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Primary GFA sold YTD on average was -13% yoy in c.75 cities, and -11%/-43% vs. 2024/2023 level"
  },
  {
    "figure_id": "F129",
    "report_id": "R017",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Secondary GFA sold last week was flat wow and +1% yoy in c.20 cities Average weekly volume of secondary property sales"
  },
  {
    "figure_id": "F130",
    "report_id": "R017",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Secondary GFA sold YTD was $+1\\%$ yoy in c.20 cities, while $+22\\% / +8\\%$ vs. 2024/ secondary volume sold vs. 2022-25"
  },
  {
    "figure_id": "F131",
    "report_id": "R017",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Average CSI was -0.9pp wow and +6.3pp yoy Weekly Centraline Salesman Index (CSI) tracker in 4 cities"
  },
  {
    "figure_id": "F132",
    "report_id": "R017",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Average CAI was +0.1pp wow and -4.3pp yoy Weekly Centraline Seller Asking Index (CAI) tracker in 6 cities"
  },
  {
    "figure_id": "F133",
    "report_id": "R017",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Inventory balance was -0.2% wow, -4.7% from end-25 levels c.20 cities' total inventory breakdown by city tier (Indexed to Jan 2013)"
  },
  {
    "figure_id": "F134",
    "report_id": "R017",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Inventory month was -0.2% wow, representing -0.4% from end-25 levels c.20 cities' inventory months (12mth rolling) breakdown by city tier"
  },
  {
    "figure_id": "F135",
    "report_id": "R017",
    "label": "Exhibit 9",
    "context": "Exhibit 9: GSPC tracker implied monthly completions... GSPC tracker implied monthly GFA completion - based on GS float glass S-D model"
  },
  {
    "figure_id": "F136",
    "report_id": "R017",
    "label": "Exhibit 10",
    "context": "Exhibit 10: ...suggesting completions at a high-teens % yoy decline for May-26 % yoy change of GSPC - based on GS float glass S-D model"
  },
  {
    "figure_id": "F137",
    "report_id": "R019",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Overview of Liquid Cooling and Key Components ```mermaid graph TD"
  },
  {
    "figure_id": "F138",
    "report_id": "R019",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: Still Early Days for Liquid Cooling Evolution of frontier GPU rack computing power Rack power (kW) for frontier chips"
  },
  {
    "figure_id": "F139",
    "report_id": "R019",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: Single Phase DTC Dominant Today, and Two-Phase Seems to be the Future OVERVIEW OF KEY PIECES OF EQUIPMENT EXHIBIT 6: Key Equipment in Liquid Cooling Landscape"
  },
  {
    "figure_id": "F140",
    "report_id": "R019",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: Partnership Outlook by CDU OEM VERTIV. NVENT BOYD CORPORATION"
  },
  {
    "figure_id": "F141",
    "report_id": "R022",
    "label": "Exhibit 3",
    "context": "Exhibit 2: We estimate that restocking could add 4.8% of global seaborne crude oil trade demand if Gulf exports normalize by end of Jul'26 Global crude inventory change vs. Feb'26"
  },
  {
    "figure_id": "F142",
    "report_id": "R022",
    "label": "Exhibit 3",
    "context": "Exhibit 3: VLCC TCE elasticity to crude tanker net demand / (supply) VLCC TCE (China)'s elasticity (US\\$'000/day) to crude tanker S-D change"
  },
  {
    "figure_id": "F143",
    "report_id": "R022",
    "label": "Exhibit 5",
    "context": "Exhibit 5: VLCC delivery based on Jun'26 orderbook vs. Mar'26 orderbook"
  },
  {
    "figure_id": "F144",
    "report_id": "R022",
    "label": "Exhibit 6",
    "context": "Exhibit 6: VLCC delivery in 2026-30 vs. no. of vessels above 20yrs"
  },
  {
    "figure_id": "F145",
    "report_id": "R022",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Crude tanker / product tanker shipping demand breakdown 2025 crude tanker shipping demand"
  },
  {
    "figure_id": "F146",
    "report_id": "R022",
    "label": "Exhibit 12",
    "context": "Exhibit 9: Airlines & Airfreight: Sensitivity to oil price with / without fuel surcharge The above exhibits shows the negative / positive impact to net profit for every US\\$1/bbl higher / lower in oil price. Exhibit 10: Chinese a"
  },
  {
    "figure_id": "F147",
    "report_id": "R022",
    "label": "Exhibit 12",
    "context": "Exhibit 9: Airlines & Airfreight: Sensitivity to oil price with / without fuel surcharge The above exhibits shows the negative / positive impact to net profit for every US\\$1/bbl higher / lower in oil price. Exhibit 10: Chinese a"
  },
  {
    "figure_id": "F148",
    "report_id": "R022",
    "label": "Exhibit 11",
    "context": "Exhibit 11: EAL fuel surcharge for contract freight rate"
  },
  {
    "figure_id": "F149",
    "report_id": "R022",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Global Shipbuilding key monthly data overview Exhibit 14: Dynamic ROI vs. orderbook by ship type"
  },
  {
    "figure_id": "F150",
    "report_id": "R023",
    "label": "Exhibit 9",
    "context": "Exhibit 1: Our weekly composite index increased in the most recent week (-4% w/w); the bottleneck scale remained at '2'; overall bottleneck levels remain well below peak congestion levels when scale was at '10' and now imply levels"
  },
  {
    "figure_id": "F151",
    "report_id": "R023",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Our average weekly bottleneck score in June is tracking at 2.0; this result is down significantly from the Dec21/Jan22 peak of congestion and close to in line with the pre-Covid baseline GS Weekly Congestion Scale, Score"
  },
  {
    "figure_id": "F152",
    "report_id": "R023",
    "label": "Exhibit 6",
    "context": "Exhibit 6: 5/1\\* container ships backed up this week on the East/West Coast West vs. East Coast Container Ship Backlog, Weekly Average, Feb 2020 - June 2026"
  },
  {
    "figure_id": "F153",
    "report_id": "R023",
    "label": "Exhibit 7",
    "context": "Exhibit 7: West Coast Class 1 Rails' Intermodal Volume Growth, Week 1 - Week 52 YoY % growth"
  },
  {
    "figure_id": "F154",
    "report_id": "R023",
    "label": "Exhibit 8",
    "context": "Exhibit 8: West Coast intermodal carload growth (UNP and BNSF) is tracking up \\~16% YoY on average in June West Coast Class 1 Rail Intermodal Traffic YoY % Growth"
  },
  {
    "figure_id": "F155",
    "report_id": "R023",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Dwell for the more typical 20ft container chassis is well off peak congestion levels Chassis Street Dwell Time (20ft Containers)"
  },
  {
    "figure_id": "F156",
    "report_id": "R023",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Ocean Container Shipping Rates, China/East Asia to North America West Coast"
  },
  {
    "figure_id": "F157",
    "report_id": "R023",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Container Weighted Average Dwell Time at San Pedro's Bay, Days"
  },
  {
    "figure_id": "F158",
    "report_id": "R023",
    "label": "Exhibit 12",
    "context": "Exhibit 12: % of Containers Dwelling More than 5 Days"
  },
  {
    "figure_id": "F159",
    "report_id": "R023",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Rail Container Dwell Time, Days"
  },
  {
    "figure_id": "F160",
    "report_id": "R023",
    "label": "Exhibit 14",
    "context": "Exhibit 14: West Coast Ports' Inbound Loaded Containers -1.0% YoY in April"
  },
  {
    "figure_id": "F161",
    "report_id": "R023",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Door to Door Shipping Days, China to US"
  },
  {
    "figure_id": "F162",
    "report_id": "R023",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Total Truck Transportation Employee Count, Seasonally Adjusted"
  },
  {
    "figure_id": "F163",
    "report_id": "R023",
    "label": "Exhibit 17",
    "context": "Exhibit 17: PMI: Manufacturing Suppliers' Delivery Times, YoY, Seasonally Adjusted"
  },
  {
    "figure_id": "F164",
    "report_id": "R023",
    "label": "Exhibit 19",
    "context": "Exhibit 18: The weekly composite index (light blue) leads the monthly (dark blue); expect future monthly updates to confirm recent weekly trends"
  },
  {
    "figure_id": "F165",
    "report_id": "R023",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Our combined scale averaged '108' in April, indicating a bottleneck score of '2' but close to '1' when looking at all metrics (weekly and monthly combined) Weekly + Monthly Combined Congestion Scale\\*"
  },
  {
    "figure_id": "F166",
    "report_id": "R024",
    "label": "Figure 1",
    "context": "Figure 1: EM USD Aggregate 10s30s"
  },
  {
    "figure_id": "F167",
    "report_id": "R024",
    "label": "Figure 2",
    "context": "Figure 2: UST 10s30s yield curve slope"
  },
  {
    "figure_id": "F168",
    "report_id": "R024",
    "label": "Figure 3",
    "context": "Figure 3: Steepest and flattest 10s30s curves"
  },
  {
    "figure_id": "F169",
    "report_id": "R024",
    "label": "Figure 4",
    "context": "Figure 4: Largest 1w changes in 10s30s"
  },
  {
    "figure_id": "F170",
    "report_id": "R024",
    "label": "Figure 5",
    "context": "Figure 6: 10s30s curves vs. the 10y level relationship"
  },
  {
    "figure_id": "F171",
    "report_id": "R024",
    "label": "Figure 7",
    "context": "Figure 7: 1w change in aggregate 10s30s vs. 1w change in aggregate 10 spreads"
  },
  {
    "figure_id": "F172",
    "report_id": "R024",
    "label": "Figure 8",
    "context": "Figure 8: 1w change in 10s30s vs. 1w change in 10y spreads by issuer"
  },
  {
    "figure_id": "F173",
    "report_id": "R024",
    "label": "Figure 9",
    "context": "Figure 9: Historical EM aggregate 10s30s spread curve slope"
  },
  {
    "figure_id": "F174",
    "report_id": "R024",
    "label": "Figure 11",
    "context": "Figure 11: Historical EMBIG vs. CEMBI spread curve slope"
  },
  {
    "figure_id": "F175",
    "report_id": "R024",
    "label": "Figure 13",
    "context": "Figure 13: Historical sovereign vs. quasi-sovereign curve slope"
  },
  {
    "figure_id": "F176",
    "report_id": "R024",
    "label": "Figure 15",
    "context": "Figure 15: Historical EMBIGD curve slope by region"
  },
  {
    "figure_id": "F177",
    "report_id": "R024",
    "label": "Figure 10",
    "context": "Figure 10: Historical US Treasury 10s30s yield curve slope"
  },
  {
    "figure_id": "F178",
    "report_id": "R024",
    "label": "Figure 12",
    "context": "Figure 12: Historical EM IG vs. HY spread curve slope"
  },
  {
    "figure_id": "F179",
    "report_id": "R024",
    "label": "Figure 14",
    "context": "Figure 14: EM corporate vs. US HG corporate spread curve slope"
  },
  {
    "figure_id": "F180",
    "report_id": "R024",
    "label": "Figure 16",
    "context": "Figure 16: Historical CEMBI curve slope by region"
  },
  {
    "figure_id": "F181",
    "report_id": "R024",
    "label": "Figure 17",
    "context": "Figure 17: 10s30s spread curve slopes vs. 10y spread"
  },
  {
    "figure_id": "F182",
    "report_id": "R024",
    "label": "Figure 18",
    "context": "Figure 18: Asia issuers 10s30s spread curve"
  },
  {
    "figure_id": "F183",
    "report_id": "R024",
    "label": "Figure 19",
    "context": "Figure 19: CEEMEA issuers"
  },
  {
    "figure_id": "F184",
    "report_id": "R024",
    "label": "Figure 20",
    "context": "Figure 20: Latin America issuers"
  },
  {
    "figure_id": "F185",
    "report_id": "R024",
    "label": "Figure 21",
    "context": "Figure 21: 10s30s spread curve slopes vs. 10y spread"
  },
  {
    "figure_id": "F186",
    "report_id": "R024",
    "label": "Figure 22",
    "context": "Figure 22: EMBIG sovereign issuers"
  },
  {
    "figure_id": "F187",
    "report_id": "R024",
    "label": "Figure 23",
    "context": "Figure 23: EMBIG quasi-sovereign issuers"
  },
  {
    "figure_id": "F188",
    "report_id": "R024",
    "label": "Figure 24",
    "context": "Figure 24: CEMBI issuers"
  },
  {
    "figure_id": "F189",
    "report_id": "R024",
    "label": "Figure 25",
    "context": "Figure 25: 10s30s spread curve slopes vs. average credit rating"
  },
  {
    "figure_id": "F190",
    "report_id": "R024",
    "label": "Figure 26",
    "context": "Figure 26: Asia issuers 10s30s spread curve"
  },
  {
    "figure_id": "F191",
    "report_id": "R024",
    "label": "Figure 27",
    "context": "Figure 27: CEEMEA issuers"
  },
  {
    "figure_id": "F192",
    "report_id": "R024",
    "label": "Figure 28",
    "context": "Figure 28: Latin America issuers"
  },
  {
    "figure_id": "F193",
    "report_id": "R024",
    "label": "Figure 29",
    "context": "Figure 29: Steepest 10s30s spread curves across EM sovereign and corporate credit Figure 30: Steepest 10s30s curves vs. the 10y spread"
  },
  {
    "figure_id": "F194",
    "report_id": "R024",
    "label": "Figure 31",
    "context": "Figure 31: Steepest 10s30s curves and 1w change"
  },
  {
    "figure_id": "F195",
    "report_id": "R024",
    "label": "Figure 32",
    "context": "Figure 32: Flattest 10s30s spread curves across EM sovereign and corporate credit Figure 33: Flattest 10s30s curves vs. the 10y spread"
  },
  {
    "figure_id": "F196",
    "report_id": "R024",
    "label": "Figure 34",
    "context": "Figure 34: Flattest 10s30s curves and 1w change"
  },
  {
    "figure_id": "F197",
    "report_id": "R024",
    "label": "Figure 35",
    "context": "Figure 35: Largest 1w steepening across 10s30s spread curves Figure 36: 1w change in 10s30s curves vs. the current 10s30s"
  },
  {
    "figure_id": "F198",
    "report_id": "R024",
    "label": "Figure 37",
    "context": "Figure 37: Largest 1w steepening and current 10s30s slope"
  },
  {
    "figure_id": "F199",
    "report_id": "R024",
    "label": "Figure 38",
    "context": "Figure 38: Largest 1w flattening across 10s30s spread curves Figure 39: 1w change in 10s30s curves vs. the current 10s30s"
  },
  {
    "figure_id": "F200",
    "report_id": "R024",
    "label": "Figure 40",
    "context": "Figure 40: Largest 1w flattening and current 10s30s slope"
  },
  {
    "figure_id": "F201",
    "report_id": "R025",
    "label": "Figure 1",
    "context": "Figure 1: Japan real GDP"
  },
  {
    "figure_id": "F202",
    "report_id": "R025",
    "label": "Figure 2",
    "context": "Figure 2: Economy Watchers Index"
  },
  {
    "figure_id": "F203",
    "report_id": "R025",
    "label": "Figure 3",
    "context": "Figure 3: Economy Watchers Index, Current conditions index"
  },
  {
    "figure_id": "F204",
    "report_id": "R025",
    "label": "Figure 1",
    "context": "Figure 1: General account budget"
  },
  {
    "figure_id": "F205",
    "report_id": "R025",
    "label": "Figure 2",
    "context": "Figure 2: Gasoline retail price"
  },
  {
    "figure_id": "F206",
    "report_id": "R025",
    "label": "Figure 2",
    "context": "Figure 3: Subsidy fund outstandings by crude oil price scenario"
  },
  {
    "figure_id": "F207",
    "report_id": "R025",
    "label": "Figure 4",
    "context": "Figure 4: Fiscal spending to stabilize fuel prices"
  },
  {
    "figure_id": "F208",
    "report_id": "R025",
    "label": "Figure 1",
    "context": "Figure 1: Business confidence and profitability"
  },
  {
    "figure_id": "F209",
    "report_id": "R025",
    "label": "Figure 2",
    "context": "Figure 2: Capacity utilisation and unemployment"
  },
  {
    "figure_id": "F210",
    "report_id": "R025",
    "label": "Figure 3",
    "context": "Figure 3: New Zealand GDP growth"
  },
  {
    "figure_id": "F211",
    "report_id": "R025",
    "label": "Figure 1",
    "context": "Figure 1: China major export categories"
  },
  {
    "figure_id": "F212",
    "report_id": "R025",
    "label": "Figure 2",
    "context": "Figure 2: China's inflation dynamics"
  },
  {
    "figure_id": "F213",
    "report_id": "R025",
    "label": "Figure 3",
    "context": "Figure 3: CNY exchange rates"
  },
  {
    "figure_id": "F214",
    "report_id": "R025",
    "label": "Figure 4",
    "context": "Figure 4: Loan growth"
  },
  {
    "figure_id": "F215",
    "report_id": "R025",
    "label": "Figure 5",
    "context": "Figure 5: Taiwan export breakdown by products"
  },
  {
    "figure_id": "F216",
    "report_id": "R025",
    "label": "Figure 1",
    "context": "Figure 1: Distribution of income accounts"
  },
  {
    "figure_id": "F217",
    "report_id": "R025",
    "label": "Figure 1",
    "context": "Figure 1: Indonesia - BI-FXPI versus change in policy rate"
  },
  {
    "figure_id": "F218",
    "report_id": "R025",
    "label": "Figure 2",
    "context": "## BI preview: Another 25bp hike Given the still-elevated FX pressure, we still expect BI to hike again by another 25bp next week to 5.75%, before another 25bp hike in July to 6.00%. The elevated FX pressure is in part caused by gross FX reserves falling furth"
  },
  {
    "figure_id": "F219",
    "report_id": "R025",
    "label": "Figure 3",
    "context": "Figure 3: Philippines headline CPI vs. diffusion index $^{1}$"
  },
  {
    "figure_id": "F220",
    "report_id": "R025",
    "label": "Figure 1",
    "context": "Figure 1: FDI and FPI balance"
  },
  {
    "figure_id": "F221",
    "report_id": "R025",
    "label": "Figure 2",
    "context": "Figure 2: Gross service exports"
  },
  {
    "figure_id": "F222",
    "report_id": "R026",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Cumulative outperformance"
  },
  {
    "figure_id": "F223",
    "report_id": "R026",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Weekly hit ratio"
  },
  {
    "figure_id": "F224",
    "report_id": "R026",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Number of ideas, by market No. of \"Three in Three\" Ideas by country"
  },
  {
    "figure_id": "F225",
    "report_id": "R029",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: We forecast \\~\\$560 bln in upstream capital expenditures in 2026 including \\~\\$56 bln toward exploration"
  },
  {
    "figure_id": "F226",
    "report_id": "R029",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: The world has discovered abundant resources, largely in shale and shelf"
  },
  {
    "figure_id": "F227",
    "report_id": "R029",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: US majors operating cash flow is rising thanks to supply discipline"
  },
  {
    "figure_id": "F228",
    "report_id": "R029",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: And they will try not to break this discipline"
  },
  {
    "figure_id": "F229",
    "report_id": "R029",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: Weak correlation, but companies that were less shareholder-friendly based on 1Q26 reporting have actually seen larger share-price gains since the war began."
  },
  {
    "figure_id": "F230",
    "report_id": "R029",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: and the correlation is weaker before the war began Pre-War: Share Price Change vs Shareholder Return as % of CFO (From 2023 to Feb 28, 2026)"
  },
  {
    "figure_id": "F231",
    "report_id": "R029",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: US E&P's high capex growth does not translate to high share price"
  },
  {
    "figure_id": "F232",
    "report_id": "R029",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: The world needs more deepwater projects"
  },
  {
    "figure_id": "F233",
    "report_id": "R029",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: Of the \\~1.5 trillion bbl of resources discovered globally since 1900, about 32% remain idle (at the discovery stage). 32% of discoveries in last century sit undeveloped Life cycle of total discoverd resources from 1900"
  },
  {
    "figure_id": "F234",
    "report_id": "R029",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: Offshore projects require heavy capex before production"
  },
  {
    "figure_id": "F235",
    "report_id": "R029",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: Frac Spread & Hz Oil Rigs"
  },
  {
    "figure_id": "F236",
    "report_id": "R029",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: Shale supply has plateaued at \\~10 mln bopd Shale production by quarterly wedge"
  },
  {
    "figure_id": "F237",
    "report_id": "R029",
    "label": "EXHIBIT 13",
    "context": "EXHIBIT 13: Venezuela and Canada oil sands resources are massive"
  },
  {
    "figure_id": "F238",
    "report_id": "R029",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: We expect development capex to tick up slightly in 2027, but remain broadly flat versus 2025 levels."
  },
  {
    "figure_id": "F239",
    "report_id": "R029",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 16: We expect the decline in US onshore capex seen in 2025 to accelerate in 2026 US onshore capex (Bernstein estimates)"
  },
  {
    "figure_id": "F240",
    "report_id": "R029",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 17: Range of fiscal take by country"
  },
  {
    "figure_id": "F241",
    "report_id": "R029",
    "label": "EXHIBIT 18",
    "context": "EXHIBIT 18: Corruption Index by country"
  },
  {
    "figure_id": "F242",
    "report_id": "R029",
    "label": "EXHIBIT 19",
    "context": "EXHIBIT 19: Flag rig count in US and in the world."
  },
  {
    "figure_id": "F243",
    "report_id": "R029",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 21: Relative XOP lag supports a catch-up setup. Relatively performance of XOP & WTI YTD"
  },
  {
    "figure_id": "F244",
    "report_id": "R030",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: After a COVID-era profitability spike and a 2022 reset, Roku's steadily rising Platform revenue has led to improving EBITDA and FCF... In Millions Roku Segment Revenues"
  },
  {
    "figure_id": "F245",
    "report_id": "R030",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: ...accordingly, ROKU's stock price has also risen after Covid reset"
  },
  {
    "figure_id": "F246",
    "report_id": "R030",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: The Roku transaction appears to be dilutive (aprox. 10%) to EPS ex. synergies FOXA-ROKU Adjusted EPS Accretion/(Dilution) FY28 ($ per Share)"
  },
  {
    "figure_id": "F247",
    "report_id": "R030",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: The Roku acquisition price is in the high end of valuation comps - EV/Rev EV/Revenue (NTM)"
  },
  {
    "figure_id": "F248",
    "report_id": "R030",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: The Roku acquisition price is in the high end of valuation comps - EV/EBITDA EV/EBITDA (NTM)"
  },
  {
    "figure_id": "F249",
    "report_id": "R030",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: The Roku acquisition price is in the high end valuation comps - P/E P/E (NTM)"
  },
  {
    "figure_id": "F250",
    "report_id": "R030",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: LTM Fox's digital revenue through Tubi and Roku's Platform Revenues combined have been experiencing over $20\\%$ growth YoY Growth in recent quarters LTM Fox Tubi Revenue + Roku Platform Revenue"
  },
  {
    "figure_id": "F251",
    "report_id": "R030",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: Advertising is a key expected revenue synergy, as Fox's strong advertiser relationships and demand can be combined with Roku's scaled CTV inventory and 1P data to drive higher pricing and monetization. LTM Fox Advertis"
  },
  {
    "figure_id": "F252",
    "report_id": "R030",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: Exhibit 9 - Roku's OS had the larget US market share, but there are many competing platforms 2025 US Smart TV Shipments by OS"
  },
  {
    "figure_id": "F253",
    "report_id": "R033",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Change to 2028 consensus EBITA following results and the 2025 CMD (14th Nov), and change in share price in the next 30 days. More recently, as consensus has moved higher, the rate of consensus upgrades has been decreasin"
  },
  {
    "figure_id": "F254",
    "report_id": "R033",
    "label": "Exhibit 2",
    "context": "Exhibit 2: MS Gas turbine / power solutions supply model. We have updated our supply model for recent announcements, and the potential 2030 supply rises to 135GW by 2030 (we forecast 116GW supply in our Jan 2026 report: The capacit"
  },
  {
    "figure_id": "F255",
    "report_id": "R033",
    "label": "Exhibit 3",
    "context": "Exhibit 3: GE Vernova (single cycle) and Siemens Energy (combined cycle) customer commitments (based on calendar dates). Siemens Energy have guided to 'customer commitments' ending fiscal 2026 at 100GW. This would mean that the 'ra"
  },
  {
    "figure_id": "F256",
    "report_id": "R033",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Gas turbine order – 2025 full year order intake landed at 100GW (single cycle). Second-highest order level in history (since 2000). We expect a record year in order intake in 2026, and 1Q26 is annualizing at 117 GW."
  },
  {
    "figure_id": "F257",
    "report_id": "R033",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Price increase YOY on 2025 order intake. We have seen much sharper step-ups in pricing on new Power plant equipment orders at GEV and ENR, compared to Wartsila."
  },
  {
    "figure_id": "F258",
    "report_id": "R033",
    "label": "Exhibit6",
    "context": "Exhibit6: Cap Goods positioning data as of 31st Mar 2026. % of EU Funds overweight Schneider is relatively unchanged at 53% vs 18mths ago (but Global LOs have increased Schneider positions). Siemens Energy's EU LO ownership has cl"
  },
  {
    "figure_id": "F259",
    "report_id": "R035",
    "label": "Figure 1",
    "context": "## Janna Withrow Figure 1. AI Data Centers and State Power Costs"
  },
  {
    "figure_id": "F260",
    "report_id": "R035",
    "label": "Figure 2",
    "context": "Google Microsoft Softbank Other © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 2. Retail Rates and Renewable Generation v. Data Center Capacity"
  },
  {
    "figure_id": "F261",
    "report_id": "R035",
    "label": "Figure 2",
    "context": "Other © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 2. Retail Rates and Renewable Generation v. Data Center Capacity South West Midwest Northeast South West Midwest Northeast © 2026 Citi Inc. No redistribution without Citi's writ"
  },
  {
    "figure_id": "F262",
    "report_id": "R035",
    "label": "Figure 6",
    "context": "Figure 6. Events Calendar © 2026 Citi Inc. No redistribution without Citi's written permission. Figure 7. CapEx v. H100 Efficiency"
  },
  {
    "figure_id": "F263",
    "report_id": "R035",
    "label": "Figure 8",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 8. H100-Equivalent Concentration by State"
  },
  {
    "figure_id": "F264",
    "report_id": "R035",
    "label": "Figure 9",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 9. Sector Adoption Rates"
  },
  {
    "figure_id": "F265",
    "report_id": "R035",
    "label": "Figure 10",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 10. HY by Issuer"
  },
  {
    "figure_id": "F266",
    "report_id": "R035",
    "label": "Figure 11",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 11. HY Coupons"
  },
  {
    "figure_id": "F267",
    "report_id": "R035",
    "label": "Figure 12",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 12. Projected Model Releases"
  },
  {
    "figure_id": "F268",
    "report_id": "R035",
    "label": "Figure 13",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 13. Historical Model Releases"
  },
  {
    "figure_id": "F269",
    "report_id": "R037",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Our new base case STX forecast implies nearline price/EB of \\$19 in CY27 and \\$22 in CY28 vs. \\$22/\\$29 in our new bull case forecasts"
  },
  {
    "figure_id": "F270",
    "report_id": "R037",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Our new base case WDC forecast implies nearline price/EB near \\$19.50 in CY27 and \\$22 in CY28 vs. \\$22.50/\\$29 in our new bull case forecasts"
  },
  {
    "figure_id": "F271",
    "report_id": "R037",
    "label": "Exhibit 8",
    "context": "Exhibit 8: STX currently trades at 18x our CY27 base case EPS, though just 11.5x our new CY27 bull case EPS STX Implied P/E"
  },
  {
    "figure_id": "F272",
    "report_id": "R037",
    "label": "Exhibit 10",
    "context": "Exhibit 10: WDC currently trades at 17x our CY27 base case EPS, though just 11.5x our new CY27 bull case EPS WDC Implied P/E"
  },
  {
    "figure_id": "F273",
    "report_id": "R038",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Long-listed global software stock selection - performance over time"
  },
  {
    "figure_id": "F274",
    "report_id": "R038",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Wolters Kluwer Tax & Accounting segment vs Thomson Reuters Tax & Accounting Professionals segment"
  },
  {
    "figure_id": "F275",
    "report_id": "R038",
    "label": "Exhibit 4",
    "context": "Exhibit 4: European Software NTM P/E vs STOXX Europe 600"
  },
  {
    "figure_id": "F276",
    "report_id": "R038",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Amadeus P/NTM Earnings"
  },
  {
    "figure_id": "F277",
    "report_id": "R038",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Capgemini P/NTM Earnings"
  },
  {
    "figure_id": "F278",
    "report_id": "R038",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Dassault Systemes P/NTM Earnings"
  },
  {
    "figure_id": "F279",
    "report_id": "R038",
    "label": "Exhibit 8",
    "context": "Exhibit 8: HBX P/NTM Earnings"
  },
  {
    "figure_id": "F280",
    "report_id": "R038",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Indra P/NTM Earnings"
  },
  {
    "figure_id": "F281",
    "report_id": "R038",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Informa P/NTM Earnings"
  },
  {
    "figure_id": "F282",
    "report_id": "R038",
    "label": "Exhibit 11",
    "context": "Exhibit 11: IONOS P/NTM Earnings"
  },
  {
    "figure_id": "F283",
    "report_id": "R038",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Nemetschek Group P/NTM Earnings"
  },
  {
    "figure_id": "F284",
    "report_id": "R038",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Netcompany P/NTM Earnings"
  },
  {
    "figure_id": "F285",
    "report_id": "R038",
    "label": "Exhibit 14",
    "context": "Exhibit 14: RELX P/NTM Earnings"
  },
  {
    "figure_id": "F286",
    "report_id": "R038",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Sage Group P/NTM Earnings"
  },
  {
    "figure_id": "F287",
    "report_id": "R038",
    "label": "Exhibit 16",
    "context": "Exhibit 16: SAP P/NTM Earnings"
  },
  {
    "figure_id": "F288",
    "report_id": "R038",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Temenos P/NTM Earnings"
  },
  {
    "figure_id": "F289",
    "report_id": "R038",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Tieto P/NTM Earnings"
  },
  {
    "figure_id": "F290",
    "report_id": "R038",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Wolters Kluwer P/NTM Earnings"
  },
  {
    "figure_id": "F291",
    "report_id": "R038",
    "label": "Exhibit 22",
    "context": "## Appendix: MS European Software & Services Coverage Software & Services"
  },
  {
    "figure_id": "F292",
    "report_id": "R039",
    "label": "EXHIBIT 1",
    "context": "EXHIBIT 1: Maruti's stated powertrain mix ambition by FY30/31"
  },
  {
    "figure_id": "F293",
    "report_id": "R039",
    "label": "EXHIBIT 2",
    "context": "## INDIA BUYS AS MANY HYBRIDS AS IT IS OFFERED Strong Hybrid Retail Volumes"
  },
  {
    "figure_id": "F294",
    "report_id": "R039",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Toyota sells \\~80% of Strong Hybrids in India, but Maruti's volumes have also picked up since the last 2 years"
  },
  {
    "figure_id": "F295",
    "report_id": "R039",
    "label": "Exhibit 2",
    "context": "EXHIBIT 5: More doors, more buyers: Hybrid penetration tracks the size of the catalogue, and India has by far the fewest doors. Model counts are estimates; the relationship is not"
  },
  {
    "figure_id": "F296",
    "report_id": "R039",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: India will go from 8 strong-hybrid nameplates in 2025 to roughly 27 by 2030; expansion led by Hyundai's confirmed 8 by 2030 plan, Maruti's in-house series-HEV programme, and a wave of Korean, Japanese and Indian launches"
  },
  {
    "figure_id": "F297",
    "report_id": "R039",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: Over five years the average BEV loses two-thirds more of its value than the average hybrid - a line item the running-cost debate often leaves out"
  },
  {
    "figure_id": "F298",
    "report_id": "R039",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: When BEV subsidies were withdrawn across key EU markets, strong hybrids and not PHEVs absorbed displaced demand, now exceeding 1.2mn units/quarter and outpacing BEVs; Europe is India's upside scenario."
  },
  {
    "figure_id": "F299",
    "report_id": "R039",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: The revocation of the \\$7,500 EV tax credit sent BEV volumes down \\~55% QoQ; HEVs held firm at \\~575k/quarter, demonstrating that buyers re-price rather than abandon electrification - the most direct analogue for India's"
  },
  {
    "figure_id": "F300",
    "report_id": "R039",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: China: HEVs flatlined not by consumer choice but by policy design - Beijing's deliberate exclusion of strong hybrids from green plates and tax breaks is the downside bookend for India's hybrid market."
  },
  {
    "figure_id": "F301",
    "report_id": "R040",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Search intensity for Best Buy AI glasses has largely led peers, though we see an uptick in Warby Parker trends in recent weeks Trailing 4 week search intensity for: ai glasses best buy (US); america's best meta (US); ai"
  },
  {
    "figure_id": "F302",
    "report_id": "R041",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Chinese Net Exports"
  },
  {
    "figure_id": "F303",
    "report_id": "R041",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Chinese Net TiO2 Exports MoM, in kt"
  },
  {
    "figure_id": "F304",
    "report_id": "R041",
    "label": "Exhibit 5",
    "context": "Exhibit 5: GS EBITDA Revisions Exhibit 6: Existing Home Sales Remain Subdued in thousands"
  },
  {
    "figure_id": "F305",
    "report_id": "R041",
    "label": "Exhibit 7",
    "context": "Exhibit 7: US New home sales (level, SAAR) in thousands"
  }
]