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
    "title": "GS：AI牛市没能让美元走强，问题出在“质量”而非“数量”",
    "digest": "[wechat_article.md]\n# GS：AI牛市没能让美元走强，问题出在“质量”而非“数量”\n\n2026年，市场最反直觉的宏观画面之一正在展开：美股在AI热潮中持续跑赢全球，但美元却未能同步走强。按照传统框架，这几乎是一个定价异常——美股的“例外主义”理应转化为对美元资产的需求，进而推高美元汇率。然而，GS外汇策略团队的最新报告指出，这一关系的断裂并非偶然，而是揭示了本轮AI驱动的美股上涨在“质量”上的根本缺陷。\n\n这份由Lexi Kanter主笔的报告，核心判断出人意料：今年AI热潮带来的美股跑赢，很可能高估了美国经济的真实需求与美元资产的吸引力。美元之所以没有跟随美股起飞，不是因为市场不买账，而是因为这轮上涨的“纯度”不够——它太集中于少数公司、太依赖于短期盈利预期、且在全球范围内并未形成绝对优势。\n\n这不仅仅是一个外汇定价的技术问题。它直接关系到投资者如何理解当前资产价格背后的驱动力，以及下半年宏观交易的核心矛盾。\n\n> **KC评论：** GS这份报告的关键洞察在于，它把“美股涨但美元不涨”这个现象拆解成了三个可验证的机制。对于多数读者来说，这比单纯看汇率点位更有价值——它提供了一套判断框架，让你能判断未来什么信号会真正改变美元走势。完整报告里还包含11条正在交易的策略建议，以及每个机制的详细回归检验图表，值得深入阅读。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 美股跑赢的“含金量”被高估：对新兴市场的优势远不及发达市场\n\nGS首先指出，当前衡量美股相对表现的常用指标——标普500相对于MSCI全球除美国指数的比值——存在一个结构性失真。这个指数主要覆盖发达市场，而今年美股真正的跑赢幅度，在面对新兴市场时其实要小得多。\n\n数据显示，韩国和台湾这两个科技权重极高的亚洲市场，在本轮AI资本开支浪潮中受益显著，其股市涨幅甚至在某些阶段超\n\n[... middle omitted ...]\n\n或图表数据感兴趣，欢迎加入我们的知识星球微信群继续深入讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI热潮推着美元走，但没那么简单\n\n当AI遇上美元，一个微妙信号\n\n最近AI行情太猛了，美股一骑绝尘，但美元却没有跟着狂飙。投行研报拆解了背后的原因，信息量很大，值得记下来。\n\n1/ 美股跑赢全球，但美元反应“钝化”\n按历史规律，美股相对全球其他市场涨得越多，美元应该越强。但这次AI驱动的上涨，美元反而显得有点“拖后腿”。原因有三：\n\n- 美股跑赢更多是对发达市场，而非新兴市场。而资金流对新兴市场货币的影响更大，对发达市场货币的传导有限。\n- 盈利增长的“可持续性”很重要。近期美股盈利预期短期大幅上调，但市场担心两年后增速放缓。这种“冲劲”不如“持久力”能拉动美元。\n- 市场宽度太窄。AI相关股票集中上涨，市场参与度不高，这种行情对美元的溢出效应有限。\n\n2/ 全球都在涨，美元反而被“稀释”\nAI行情不是美股独享，全球股市（尤其亚洲的韩国、台湾等科技重镇）也跟着受益。当全球风险偏好一起回升时，美元通常承压。所以这次美股“例外”的强势，反而让美元比原本应该的走势更弱一些。\n\n3/ 关键变量：美股如果回调会怎样？\n研报认为，如果未来美股出现回调，而全球其他市场相对抗跌，那才是美元真正走弱的催化剂。目前AI行情对美\n\n[... middle omitted ...]\n\ne see three reasons that help explain the flatter Dollar relative to clear US equity outperformance. First, US equity outperformance is less pronounced versus EMs than DMs, and flows tend to m\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R002",
    "title": "Bernstein：供应链的“高运价”不是短期脉冲，而是结构性重定价",
    "digest": "[wechat_article.md]\n# Bernstein：供应链的“高运价”不是短期脉冲，而是结构性重定价\n\n全球供应链正处于一个罕见的“三高”叠加窗口：运价高、需求韧、运力紧。这轮运价上涨并非单纯的地缘事件脉冲，而是正在重塑海运、空运、陆运的定价基准。Bernstein最新发布的《供应链脉搏报告》给出了一个与市场主流叙事略有不同的判断：高运价并未压制需求，消费者的购买行为正在适应新的运费成本，而供给侧的约束正在从临时性转向结构性。这份报告的核心洞察是，当前供应链的盈利环境对货运代理和运输公司而言是近期的“舒适区”，但不同环节、不同公司的受益程度将出现显著分化。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮运价上涨的核心驱动力已从“事件冲击”切换为“供给约束”\n\n报告明确指出，当前海洋运价较冲突前水平已上涨超过100%，空运运价也高出40%-50%。但真正值得关注的不是涨幅本身，而是推动运价持续高位的底层逻辑正在发生切换。\n\n最初的红海危机和苏伊士运河绕行是典型的供给冲击，但经过几个季度的消化，市场已经部分适应了更长的航线。当前运价持续高位的核心原因，是运力供给的刚性约束：海洋运输面临新船交付高峰前的运力错配，空运则受限于海湾地区承运人的运力瓶颈和燃油附加费，而美国陆运市场则因监管执行趋严（语言、居住地、运营范围、工时、培训等要求）导致可用的卡车运力持续收紧。\n\n这意味着，即使地缘局势出现缓和，运价也不会迅速回到冲突前水平。供给侧的约束具有更强的粘性，尤其是在美国陆运市场，监管因素带来的运力退出是结构性的，而非周期性的。\n\n> **KC评论：** 市场往往习惯于用“地缘冲突缓和=运价回落”的线性逻辑来定价运输股，但Bernstein提醒我们，当前运价中有相当一部分是监管和运力结构变化带来的“硬成本”。这部分成本的回落速度会比想象中慢得多。完\n\n[... middle omitted ...]\n\n知识星球和微信群中继续讨论，获取完整报告解读和原始数据图表。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球物流运价飙涨，但需求依然坚挺\n\n运价高企，需求未减\n\n最近几个月，全球物流运价持续攀升。海运价格已比冲突前高出100%以上，空运价格也上涨了40-50%。但令人意外的是，需求依然保持韧性，4月集装箱运量同比增长4%，达到马士基全年增长预期的上限。\n\n1/ 海运：短期需求强劲，但需警惕供给过剩\n- 运价飙升：WCI和SCFI指数均比冲突前高出100%以上\n- 需求脉冲：季末前集中出货，叠加附加费上调预期\n- 但需注意：大量新船订单仍在路上，H2需求可能走弱\n\n2/ 空运：运价高位运行，AI和半导体支撑需求\n- 运力紧张：海湾航司运力受限，燃油附加费持续\n- 需求结构：AI、半导体、高价值电子产品是主要驱动力\n- 预计2026年需求增长2-3%（DHL和IATA预测）\n\n3/ 北美地面运输：供给端收紧是主因\n- 现货TL运价（不含燃油）同比上涨48%\n- 监管趋严（语言、居住地、运营范围等）推高运营成本\n- 需求端也有亮点：ISM制造业PMI连续多月扩张，国内多式联运量同比转正\n\n4/ 欧洲物流商分化明显\n- DSV：并购整合能力突出，DB Schenker收购后EPS有望超100丹麦克朗\n- DHL：多业务\n\n[... middle omitted ...]\n\ne Weiss\n\n+1 917 344 8433\n\njustine.weiss@bernsteinsg.com\n\nRecent months have seen freight rates continue to rise, with ocean freight rates now more than 100% above pre-conflict levels, driven b\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R003",
    "title": "GS铜业周：铜矿股正在交易一个“不存在的过剩”",
    "digest": "[wechat_article.md]\n# GS铜业周：铜矿股正在交易一个“不存在的过剩”\n\n铜价横盘，库存高企，关税阴云未散——这是当前市场对铜板块最直观的感受。但GS刚刚发布的年度铜业周前瞻材料，给出了一个与市场情绪截然相反的判断：**铜矿股的定价中隐含了太多悲观，而供给侧的真正约束才刚刚开始显现。**\n\n这不是一篇简单的会议预告。GS在材料中逐一拆解了全球主要铜矿上市公司的估值含义、增长路径和风险定价，得出的结论是：大多数铜矿股当前交易价格所隐含的铜价，已经低于现货水平。换句话说，市场在用“供过于求”的剧本给铜矿股定价，但产业层面的真实叙事却是“结构性短缺正在加深”。\n\n这份材料的核心价值，不在于GS对铜价本身的预测，而在于它提供了一个极其清晰的框架：**把每家公司股价倒推回其隐含的铜价假设，然后与现货铜价对比，就能直观判断市场在定价什么、又在忽略什么。**\n\n我们逐一拆解。\n\n> **KC评论：** GS这个“隐含铜价”的分析框架，是理解铜矿股当前定价锚点的最直接工具。如果一家公司股价隐含的铜价远低于现货，说明市场在用“衰退+过剩”的剧本定价；如果隐含铜价接近或高于现货，说明市场已经计入了供给紧张。完整报告中还包含了每家公司DCF模型的关键假设，如WACC、beta和终端增长率，这些参数对隐含铜价的敏感性极高，值得仔细对比。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 多数铜矿股定价已低于现货铜价，市场对供给过剩的担忧可能过度\n\nGS覆盖的铜矿公司中，有多家当前股价所隐含的铜价显著低于LME现货铜价。以南方铜业为例，其隐含铜价约为每吨11,600美元，比现货低约15%。Hudbay Minerals的隐含铜价约为每吨13,500美元，仅比现货低1%，若计入Copper World项目则进一步降至11,700美元，折价幅度达14%。First \n\n[... middle omitted ...]\n\n。欢迎加入我们的微信群，继续讨论铜矿股的真实定价和投资逻辑。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n铜矿板块，2026年关键变量在哪\n\n全球铜业观察\n\n某外资投行2026铜业周即将开幕，多家头部矿企高管将出席。看完这份研报，我整理了几个核心看点👇\n\n**1/ 成本压力见顶了吗？**\n能源和化学品通胀是短期焦点。市场想确认：成本是否已过峰值？全年指引能否兑现？品位下降、监管变化、置换资本开支等结构性挑战也会被讨论。\n\n**2/ 拉美监管环境**\n秘鲁、智利已完成一轮总统选举，巴西、阿根廷待选。管理层对政治变化后的监管预期，直接影响项目推进节奏。\n\n**3/ 铜供需与定价**\n通胀与宏观不确定性、利率预期、美国库存高企和关税讨论，都是近期焦点。会上将收集管理层对供需和定价的看法。\n\n**4/ 各家公司看点**\n- 某公司：Centinela C2扩产是核心，市场未充分定价其他棕地选项\n- 另一家：高运营杠杆，铜价反弹时弹性大，但短期现金流不确定性高\n- 还有一家：Grasberg矿重新爬坡，浸出项目降本增效，2027年毛利/磅或翻倍\n- 某公司：Cobre Panama重启是关键催化剂，近期有积极进展\n- 另几家：分别强调金铜双驱、估值折价、防守性等逻辑\n\n**5/ 风险提示**\n关税不确定性是短期最大风险；项\n\n[... middle omitted ...]\n\nhe short-term, cost headwinds related to energy and chemicals inflation are also on investors' minds, and this event will be an opportunity to understand how cost is performing against full ye\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R004",
    "title": "DB：ECB加息不是终点，而是规则框架下的“稳健”起点",
    "digest": "[wechat_article.md]\n# DB：ECB加息不是终点，而是规则框架下的“稳健”起点\n\nECB在6月会议上宣布加息25个基点，行长拉加德用“稳健”而非“强硬”来形容这一决定。市场对此的解读分化明显：一部分人认为这是本轮紧缩周期的尾声，另一部分人则担心通胀粘性将迫使ECB继续加码。DB最新发布的研报，通过一套严谨的政策规则框架，给出了一个清晰的判断：ECB的加息进程远未结束，但节奏和终点将由通胀结构而非总量决定。\n\n这份研报的核心价值不在于预测具体加息几次，而在于它提供了一个可复用的分析框架——用ECB自己的经济预测来检验其政策路径的合理性。结论是：即使采用最温和的情景假设，ECB也需要至少再加息一次；而如果通胀从能源领域向核心领域扩散的假设成立，终端利率可能比市场当前定价高出25-50个基点。\n\n这不仅仅是一份关于ECB的研报，它实际上在回答一个更根本的问题：在供给冲击主导的通胀环境中，中央银行应该如何校准政策？规则指引和相机抉择之间的张力，如何影响资产定价？\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 政策规则指向的终端利率，比市场定价更“鹰”\n\nDB的分析起点非常直接：将ECB 6月员工预测数据输入九种不同的货币政策规则，看这些规则会给出什么样的利率路径。这九种规则包括泰勒规则、平衡法规则、前瞻性规则、惯性规则等，涵盖了对通胀指标（整体HICP vs 核心HICP）和产出缺口指标（失业率 vs 产出缺口）的不同选择。\n\n结果是分层的。如果使用整体HICP作为通胀指标，泰勒型规则会建议ECB在年底前将利率大幅提升至4%左右，这显然是一个不切实际的激进路径。但DB明确指出，在能源供给冲击的背景下，ECB完全可以忽略基于整体通胀的规则信号——因为货币政策无法直接影响能源价格本身，只能关注其溢出效应和第二轮效应。\n\n更关键的是剔除了能源价格\n\n[... middle omitted ...]\n\nmarket dynamics。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n欧央行为什么还要加息？\n\n📐 政策规则告诉你，加息还没结束\n\n某外资投行用9条政策规则，套入欧央行自己的预测，发现：\n即便剔除能源，温和情景下，终点利率也在2.50%-2.75%。\n\n1️⃣ 规则怎么说？\n- 用核心通胀（剔除能源）的规则，中位数指向2.75%（约再加2次）\n- 温和情景下，中位数指向2.50%（约再加1次）\n- 3月到6月，欧央行上调通胀预测，规则建议额外加息25-50bp\n\n2️⃣ 哪些规则更靠谱？\n- 基于整体通胀的泰勒规则太激进，建议年底加到4%\n- 基于核心通胀+平滑参数的规则，更接近市场预期\n- 能源供给冲击下，央行应忽略直接能源效应，关注第二轮效应\n\n3️⃣ 不同情景的差异\n- 温和情景：终点2.50%，再加1次\n- 不利/严重情景：2027年才需进一步收紧\n- 当前能源期货介于基线与温和之间，支持再加1-2次\n\n4️⃣ 规则只是参考\n- 2020-2022年，规则建议激进紧缩，但央行没执行\n- 2024年降息周期，实际利率跟随规则的下沿\n- 拉加德说6月加息“稳健”，规则分析也支持这一点\n\n你觉得欧央行9月会再加一次吗？欢迎一起讨论。\n\n#学习笔记\n\n[source_miner\n\n[... middle omitted ...]\n\nhtening is warranted: The ECB's June rate hike was robust, supported even by the milder scenario. Using the ex-energy HICP forecasts, the median policy prescription under the baseline scenario\n\n[... middle omitted ...]\n\n(49) 69 910 00</td><td>Hong Kong</td><td>Tel: (81) 3 6730 1000</td></tr><tr><td>Australia</td><td></td><td>Tel: (852) 2203 8888</td><td></td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr></table>"
  },
  {
    "id": "R005",
    "title": "GS：山西煤矿事故将结构性重塑全球焦煤定价权",
    "digest": "[wechat_article.md]\n# GS：山西煤矿事故将结构性重塑全球焦煤定价权\n\n如果你只关心焦煤价格会涨到多少，这份GS报告给出的答案是每吨280美元。但真正值得你关注的，不是这个数字本身，而是它背后正在发生的三件事：中国正在失去高强度焦煤的自主供应能力，澳大利亚正在重新夺回对华定价权，而印度虽然需求增长最快，却始终无法成为价格的主导者。\n\n这份基于新加坡铁矿石周和焦煤会议的调研报告，提供了一个罕见的全景视角。报告最核心的判断是：山西矿难导致的1500-2000万吨产量损失，不是一次性的供应冲击，而是一次结构性重置。部分矿井可能永远无法恢复到满产状态，中国对优质进口焦煤的依赖正在从周期性变为结构性。\n\n这意味着，全球焦煤的定价锚正在从中国CFR价格，重新回到澳大利亚FOB指数。而这一转变，将影响从钢铁厂利润到矿业公司估值的整个链条。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 山西矿难不只损失了产量，还摧毁了中国对高强度焦煤的自给能力\n\nGS团队在会议上得到的反馈显示，山西事故后仍有约5000-5500万吨产能处于停产状态。市场已经消化了1500-2000万吨的年度产量损失，但真正关键的问题是：这些产能还能回来吗？\n\n与会交易商的判断并不乐观。部分矿井即使复产，产能利用率也可能只能恢复到之前的70-80%，而过去有些矿井的实际产出甚至可以达到名义产能的110%。监管问责的升级和地方官员的调查，正在让复产审批变得更加谨慎。\n\n> **KC评论：** 这里需要理解一个关键细节——损失的不仅是产量，更是特定品质的供应。山西事故中停产的主要是高强度、低挥发分的优质焦煤，这种煤蒙古和俄罗斯都无法替代。这意味着中国钢铁厂在配煤环节失去了关键的“骨架”原料，只能转向进口。完整报告中的图2和图3清晰地展示了这一冲击如何迅速拉平了澳大利亚煤和国内\n\n[... middle omitted ...]\n\n是美国煤能否成为变量、以及澳大利亚供应约束是否会比预期更紧。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n山西煤矿事故冲击，炼焦煤价格或再走高\n\n煤价逻辑在变\n\n刚参加完新加坡炼焦煤会议，信息量很大。山西矿难的影响比想象中更深远——不仅是产量损失，更可能是结构性供应重置。\n\n1/ 山西产量损失15-20Mt，高端煤缺口难补\n- 事故后中国国内减产约1500-2000万吨（截至8月），占年消费量约5%\n- 仍有5000-5500万吨产能处于停产状态，市场预期部分不会复产\n- 受损的主要是高强度（CSR）低挥发煤，蒙古和俄罗斯无法替代\n- 中国港口价已上涨约40美元/吨，澳煤价格首次与国内煤持平\n\n2/ 澳煤价格或测试260-280美元/吨\n- 当前澳煤现货约244美元/吨，贸易商预计下半年可能升至260-280美元\n- 中国需求转向澳洲高端煤，Tier1和Tier2品种流动性上升\n- 季节性检修（7-8月）后，9月补库可能进一步收紧优质煤市场\n\n3/ 印度需求长期增长，但定价权有限\n- 印度炼焦煤进口预计从8000万吨增至1.2亿吨以上\n- 但现货参与度低（仅约10%敞口），港口/堆场基础设施不如中国\n- 印度钢厂正通过更复杂的配煤技术，将中低品质煤比例从<10%提升至35-55%，吨煤成本节省10-15美元\n\n4\n\n[... middle omitted ...]\n\nions across both conferences were dominated by the recent Shanxi coal accident, with the focus on the headline volume loss and also the potential structural supply reset that may follow. Estim\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R006",
    "title": "摩根斯坦利：MS：中国5月成品油需求暴跌，电动车不是“冲击”，是“替代完成”",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：中国5月成品油需求暴跌，电动车不是“冲击”，是“替代完成”\n\n中国5月的成品油消费数据，发出了一个比市场预期更清晰的信号。\n\nMS最新发布的研报显示，中国5月隐含汽油和柴油需求同比分别下降12%和21%，总成品油消费同比下降13.5%。这个数字不是简单的“需求疲软”，而是结构性拐点的确认。报告明确指出，需求破坏的主要来源是公路运输和基建活动，而非航空或化工。\n\n换句话说，中国石油需求的长期故事，正在从“增长放缓”切换为“存量替代”。\n\n为什么这个判断比GDP增速或PMI数据更值得关注？因为成品油消费是经济活动最真实的“物理映射”——它不受库存周期、价格幻觉或统计口径的干扰。当汽油和柴油同时出现两位数下滑，且背后是电动车对燃油车的系统性替代时，投资者需要重新评估整个能源化工产业链的定价逻辑。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 柴油需求暴跌21%，基建和物流的“真实温度”比想象更低\n\n柴油是经济活动的“毛细血管”——它关联着卡车运输、工程机械、矿山开采和农业机械。5月21%的同比降幅，是疫情以来最深的单月跌幅之一。MS将其归因于“基建和物流需求放缓”，但这背后可能还有更深层的结构变化。\n\n传统上，柴油需求与固定资产投资高度相关。但这一次，数据似乎在说：即便基建投资名义增速没有大幅下滑，单位投资额的柴油消耗量正在下降。原因有二：一是新能源重卡和工程机械的渗透率在快速提升；二是物流行业的“集约化”趋势——更高效的路线规划和载具利用率降低了对柴油车的依赖。\n\n> **KC评论：** 柴油21%的降幅不是“经济崩了”，而是“经济结构变了”。基建投资可能还在，但拉动的柴油消费正在被电动化和效率提升抵消。完整报告里对柴油库存和炼厂开工率的数据拆解，能帮你判断这是短期波动还是长期趋势。\n\n![研报\n\n[... middle omitted ...]\n\n者一起，持续追踪这些关键变量的演变。我们每天更新，从不间断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国5月成品油消费降13.5%\n\n油车真的在失速\n\n航空煤油逆势增长5%，但汽油跌12%，柴油跌21%\n\n1️⃣ 需求结构性塌方\n投行研报数据显示，5月中国成品油消费同比降13.5%。其中柴油降幅最大（-21%），汽油次之（-12%）。主因是道路运输和基建活动放缓，而非航空或化工需求。\n\n2️⃣ 电动车加速替代\n高油价正在加速出行方式转变。共享出行和私家车都在向电动化迁移，传统燃油车需求被结构性挤压。这不是短期波动，而是长期趋势。\n\n3️⃣ 库存高企成隐忧\n尽管炼厂已大幅降负荷，燃料库存仍处高位。说明需求下滑的速度比供给收缩更快，供需失衡压力持续。\n\n4️⃣ 航空煤油是唯一亮点\n航煤消费同比增5%，显示航空出行需求仍有韧性。但体量较小，难以对冲道路燃料的萎缩。\n\n欢迎一起讨论：电动化对能源消费结构的影响，会不会比预期更快？\n\n#学习笔记\n\n[source_mineru.md]\n# China Energy & Chemicals | Asia Pacific\n\n## China NOW: Oil Consumption\n\n## Key Takeaways\n\nChina's implied gasoline a\n\n[... middle omitted ...]\n\nelieve the weakness reflects a combination of softer economic activity, slowing infrastructure and logistics demand, and accelerating substitution toward EV-dominated shared-mobility - high oi\n\n[... middle omitted ...]\n\n Co. Ltd. (002001.SZ)</td><td>E (01/26/2026)</td><td>Rmb29.75</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R007",
    "title": "BARC：标普500目标价7800，但真正支撑上涨的不是估值，是盈利",
    "digest": "[wechat_article.md]\n# BARC：标普500目标价7800，但真正支撑上涨的不是估值，是盈利\n\n当市场还在为中东停火、油价回落、AI资本开支是否见顶而反复博弈时，BARC策略团队做出了一个看似矛盾的决定：**上调标普500目标价，却同时下调了估值假设。**\n\n2026年底标普500目标价从7650上调至7800，2027年底目标价8800——这些数字本身并不惊人。真正值得关注的信号是，BARC将估值倍数从此前的约24倍下调至23.1倍，同时将2026年每股收益（EPS）预期从321美元大幅上调至337美元。\n\n**这意味着什么？** BARC认为，推动美股继续上涨的发动机正在切换：从流动性驱动、估值扩张，转向盈利驱动、基本面支撑。如果这个判断成立，那么投资者需要重新审视自己的持仓结构——哪些公司真正有盈利可见性，哪些只是搭了估值泡沫的顺风车。\n\n这份报告写于2026年6月19日，正值市场经历了一轮从地缘政治冲击到快速修复的完整周期。BARC的结论是：美股的牛市基础仍然完整，但支撑逻辑已经变了。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮上涨的底层逻辑，正在从“估值讲故事”转向“盈利证明自己”\n\n2026年上半年的美股走势，像一部浓缩的风险教育片。年初市场已经定价了大量好消息：全球宏观企稳、AI资本开支成为不可否认的顺风、市场领导力从超大型科技股向周期股和小盘股扩散。但高估值意味着容错空间极窄。\n\n2月，软件行业被AI颠覆的担忧引发抛售，跌幅抹去了该板块自2022年以来相对于标普500的全部超额收益。随后，对高杠杆软件公司的担忧蔓延至私募信贷市场，进而引发对长久期成长资产的全面重估。紧接着，中东战争爆发，石油价格飙升，市场开始担忧滞胀。\n\nBARC的策略是“看穿噪音”。当停火协议传出后，投资者迅速回归那些盈利可见性最\n\n[... middle omitted ...]\n\n球微信群里继续讨论——那里有更完整的原始素材和更及时的跟踪。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n标普目标上调至7800，逻辑在这\n\n📌 盈利驱动，而非估值\n\n某外资投行最新研报，把2026年底标普500目标价从7650上调至7800，同时将2026年每股盈利预测从\\$321上调至\\$337。\n\n核心逻辑很简单：盈利增长在扛大旗，估值反而小幅压缩（从24倍降至23倍），因为AI投资规模、融资方式和变现时间线仍有不确定性。\n\n1/ 盈利为什么能上修？\n- 一季度财报季超预期，科技板块EPS增速创2010年以来最佳\n- 再通胀压力支撑名义收入增长\n- 工业端需求向好，能部分对冲消费端走弱\n- 但消费确实在降温，是主要的下行抵消项\n\n2/ AI投资周期怎么看？\n- 研报认为“AI资本开支峰值”被推后了，供给约束+需求曲线变陡\n- 但风险也在累积：超大规模企业自有现金流 vs 资本开支的缺口在扩大，2028年可能更紧张\n- 融资结构越来越复杂，是下半年重点观察的风险点\n\n3/ 宏观环境：复杂但有支撑\n- 就业数据够强，衰退风险降低，但也让降息预期推后\n- 输入成本在涨，但还没到拖垮周期的程度\n- 美联储宽松退场后，盈利和AI投资的可视性要扛更多责任\n\n4/ 行业调仓\n- 金融和医疗保健下调至中性（金融的银行盈利上\n\n[... middle omitted ...]\n\nnot yet a growth shock large enough to derail the cycle. The equity bull case remains intact, but earnings and AI capex visibility must do more of the work as Fed support fades and positioning\n\n[... middle omitted ...]\n\nrior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request."
  },
  {
    "id": "R008",
    "title": "DB：机构外汇管理正从“被动不管理”转向“主动总组合”",
    "digest": "[wechat_article.md]\n# DB：机构外汇管理正从“被动不管理”转向“主动总组合”\n\n当一家大型养老金基金的管理者被问及如何管理汇率风险时，最常见的回答是“我们没有专门做这件事，因为它分散了我们对核心资产的关注”。这种回答正在被重新审视。\n\nDB近期发布了一份关于外汇风险管理从理论到实践的深度报告。报告的核心判断并非某个汇率走势的预测，而是一个更根本的转变：机构投资者正在将汇率风险管理从“后台被动合规”提升为“总组合层面的主动策略”。这家投行在与超过35家机构客户讨论后得出结论——不管理汇率风险本身就是一种风险决策，且往往是最低效的那种。\n\n为什么是现在？三个因素正在汇聚：第一，荷兰养老金改革等区域监管变化正倒逼机构重新审视风险敞口；第二，全球资产配置中非本币资产的比重持续上升，汇率波动对总回报的影响已无法忽略；第三，机构对“总组合方法”（TPA）的兴趣从理论探讨转向了如何落地执行。\n\n这份报告的价值不在于给出具体的做多或做空建议，而在于提供了一套机构可以照搬的思考框架。它回答了“管不管”、“管多少”、“用什么工具管”以及“管了之后如何应对流动性压力”这四个递进的问题。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 不管理汇率风险，本身就是最昂贵的风险决策\n\n报告开篇就直指一个长期存在的行业惯例：汇率风险往往被忽视，或者被分割到各个资产类别中单独管理。债券组合可能做了对冲，股票组合可能完全暴露，而私募市场的汇率风险则基本没有被系统性地处理。\n\n这种“碎片化管理”的后果是什么？DB指出，选择不对冲本身就是一种风险决策。如果这个决定是被动做出的——即因为“没人负责”或者“太复杂”——那么它对组合结果的影响往往是不对称的。当汇率波动恰好与核心资产回报负相关时，组合会承受双重打击。\n\n从区域分布来看，亚太地区的机构在讨论中对汇率管理的\n\n[... middle omitted ...]\n\n率风险到底怎么量化，或者如何用期权结构在基准约束下提升效率。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n汇率风险，你管还是不管？\n\n📌 别让汇率偷偷吃掉你的收益\n\n**外汇管理，从“要不要做”变成“怎么做”**\n\n最近和超过35家机构聊了同一个话题：汇率风险到底应该怎么管？结论很明确——以前是“要不要管”，现在是“怎么管到位”。\n\n1️⃣ **别再把汇率当“孤岛”**\n很多机构把汇率管理拆成独立部门，结果就是各管各的。债券多做了对冲，股票却裸奔。其实不主动管理汇率，本身就是一种风险决策。荷兰养老金改革已经推着大家往更主动的方向走了。\n\n2️⃣ **你的目标到底是什么？**\n这个问题其实挺根本的：做汇率管理是为了多赚钱，还是为了控风险？主流思路是——用核心资产赚收益，汇率这边负责“别添乱”。一套好的对冲框架，核心是稳住组合波动，同时尽量保住收益。\n\n3️⃣ **别跟基准跑偏了**\n很多基金拿MSCI这类未对冲指数当基准，做对冲时容易跑偏。但这不是死局，可以把基准约束写进框架里，依然能比传统方法更高效。\n\n4️⃣ **远期是基础，期权是进阶**\n远期还是主力工具，但期权越来越受欢迎。特别是那些必须完全对冲的基金，会用期权来增加灵活性、降低整体成本。\n\n5️⃣ **别只看持仓，要看“隐形敞口”**\n举个🌰：你买了美国\n\n[... middle omitted ...]\n\ne recently published Dynamic FX Portfolio Hedging: A deep dive and why you should use it and why and how to use a currency signal on applying this principle to FX risk management. Since the pa\n\n[... middle omitted ...]\n\nel: (81) 3 6730 1000</td></tr></table>\n\nDB AG  \n21 Moorfields  \nLondon EC2Y 9DB  \nUnited Kingdom  \nTel: (44) 20 7545 8000\n\nDB AG  \nFiliale Singapur  \nOne Raffles Quay, South Tower  \nSingapore 048583  \nTel: (65) 6423 8001"
  },
  {
    "id": "R009",
    "title": "NOM：电池行业已进入“三国分治”阶段，机器人电池是下一个价值高地",
    "digest": "[wechat_article.md]\n# NOM：电池行业已进入“三国分治”阶段，机器人电池是下一个价值高地\n\n全球电池产业正在经历一场静悄悄但极其深刻的分化。当多数市场参与者还在用“产能过剩”和“价格战”来概括行业现状时，NOM最新发布的全球电池深度报告给出了一个截然不同的判断：行业已经不再是单一维度的竞争，中国、韩国、日本三大电池阵营正在走向完全不同的战略路径，而机器人电池——这个目前仅占极小份额的细分市场——可能成为未来几年最被低估的价值增长点。\n\n这份报告的核心洞察并不复杂，但其含义却值得每一位关注先进制造和能源转型的决策者深思：全球电池需求仍在增长，但增长的结构正在发生质变。储能系统（ESS）电池将以17%的年复合增速成为增长最快的板块，到2030年达到926GWh；而电动汽车电池的增速将放缓至11%。更重要的是，中国企业凭借LFP电池和一体化供应链，已经拿下了全球78%的电动汽车电池和80%的储能电池市场份额。韩国和日本企业不再试图在规模上与中国正面竞争，而是分别转向了“高价值+本地化”和“AI数据中心”两个截然不同的赛道。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 中国电池的统治力比大多数人想象的要深，而且还在加固\n\nNOM报告中最引人注目的数字，是中国电池企业在全球市场的份额。2026年，中国在全球电动汽车电池和储能电池市场的份额预计分别达到78%和80%。这个数字之所以惊人，不仅在于其绝对高度，更在于它是在美国和欧洲持续加征关税、设置本地化壁垒的背景下实现的。\n\n中国电池的统治力根植于LFP（磷酸铁锂）化学体系的全面胜利。目前LFP已经占全球电池市场的61%，而中国几乎完全掌控了这条供应链。从锂资源加工到正极材料、隔膜、电解液，中国企业在每一个环节都拥有规模优势和成本优势。NOM报告指出，即使在海外市场，中国电池厂商凭借成本领先\n\n[... middle omitted ...]\n\n这些未解问题感兴趣，欢迎加入我们的社群，在微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球电池市场进入分化阶段\n\n🔋电池赛道，三国杀\n\n电池行业正进入一个分化加速的新阶段。某外资投行最新研报显示，未来全球电池需求将呈现两条明显不同的增长曲线。\n\n**1/ 储能电池 vs 动力电池，谁更快？**\n- 全球储能电池（ESS）需求预计2026-2030年每年增长17%，到2030年达到926GWh\n- 美国占全球储能需求约20%，主要驱动力来自AI数据中心、可再生能源并网和电网改造\n- 相比之下，电动车电池需求增速放缓至11%每年，到2030年达到1.8TWh\n\n**2/ 中韩日各走各的路**\n- 中国：绝对的产量王者，2026年预计占全球电动车/储能电池市场78%/80%的份额。核心武器是LFP磷酸铁锂（占全球电池市场61%）和完整的供应链\n- 韩国：转向高价值电动车和美国储能市场，利用美欧本地化要求建立护城河\n- 日本：瞄准AI数据中心服务器电池，目标到FY29实现1000亿日元收入\n\n**3/ 机器人电池，下一个蓝海？**\n研报特别提到一个有意思的方向——人形机器人电池。虽然需求量不大，但单价是电动车电池的3倍，预计2030年市场规模20-40亿美元。早期可能用高镍电池，但随着LFP性能提升和\n\n[... middle omitted ...]\n\nWh in 2030F. In this context, the industry's competitive landscape is becoming increasingly segmented. China is the clear volume leader, with 2026F global share at 78%/80% for EV/ESS batteries\n\n[... middle omitted ...]\n\n00-8130, JapanTel: +81 3 5255 1658 Fax: +81 3 5255 1747, 3272 0869</td></tr></table>\n\nCaring for the environment: to receive only the electronic versions of our research, please contact your sales representative.\n\n## NOM"
  },
  {
    "id": "R010",
    "title": "GS：炼油利润的韧性比原油价格更值得关注",
    "digest": "[wechat_article.md]\n# GS：炼油利润的韧性比原油价格更值得关注\n\n原油价格在美伊临时和平协议宣布后暴跌超过10美元，但炼油产品的利润率降幅却小得多。GS全球炼油产品利润率指数目前仍处于战前水平的两倍。\n\n这是一个被市场低估的信号。当所有人都在盯着布伦特原油的波动时，真正影响产业链利润结构的关键变量正在发生变化。GS最新发布的原油研报给出了一个核心判断：**炼油产品利润率的下降风险远小于原油价格，且结构性支撑因素将使其在2027年仍维持高位。**\n\n这份报告的价值不在于预测油价的方向——那是几乎不可能精准完成的任务——而在于揭示了能源产业链中利润分配的结构性变化。对于关注能源资产定价、炼化板块投资以及通胀传导的决策者而言，这可能是比原油价格本身更重要的观察维度。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 霍尔木兹海峡的重新开放对炼油利润的冲击远小于对原油的冲击\n\n市场普遍认为，一旦霍尔木兹海峡通行恢复正常，所有与地缘溢价相关的资产价格都会同步回落。但GS的数据显示，实际情况并非如此。\n\n自美伊临时和平协议宣布以来，原油价格下跌超过10美元，而炼油产品利润率的降幅明显更小。GS的全球炼油产品利润率指数仍维持在战前水平的两倍。这一差异背后是两种完全不同的供需逻辑。\n\n原油价格受制于全球供需平衡和地缘政治溢价的快速消退，而炼油产品利润率则受到更具体、更刚性的约束——炼厂产能利用率、产品库存水平以及不同馏分油的生产调配。这些因素不会因为一份和平协议就迅速改变。\n\n> **KC评论：** 这组数据指向一个容易被忽视的事实：即便地缘风险溢价消退，炼油环节的利润也不会同步回归“正常”。对于持有炼化资产或关注相关板块的投资者而言，这意味着需要重新评估估值框架中的利润中枢假设。完整报告中附有详细的全球炼油产品利润率指数走势图，展示了与原油价格的背\n\n[... middle omitted ...]\n\n欢迎来知识星球微信群里继续讨论，一起追踪这些关键变量的变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n炼厂利润还能撑多久\n\n利润底比油价厚\n\n原油跌超10美元，但炼厂利润只掉了一半。\n\n某外资投行最新研报拆了3个逻辑：\n\n1️⃣ 库存还在低位\n美国汽油/柴油库存低于近5年季节性区间，未来1-4个月还要继续去库。炼厂过去4个月优先保柴油和航煤，汽油产量被挤占。\n\n2️⃣ 供给恢复慢\n波斯湾炼厂仍有130万桶/日意外停产，修复需数月。即使中东局势缓和，成品油供应恢复比原油慢得多。\n\n3️⃣ 结构性支撑\n中国和印度炼厂新增产能延迟，俄罗斯炼厂持续遭袭，2027年全球炼厂利用率可能接近历史峰值。\n\n📊 核心判断：\n- 2026Q4美国柴油利润预计46美元/桶，欧洲31美元/桶（仍为2013-2019均值的2-3倍）\n- 2027年美国柴油利润38美元/桶，汽油22美元/桶\n- 利润下行风险比原油小，上行空间却更大\n\n如果霍尔木兹持续中断，柴油利润可能比基准高66%，而布伦特只高41%。\n\n#学习笔记\n\n[source_mineru.md]\nOIL ANALYST\n\n# High Product Margins for Longer; Smaller Downside Risks Than for Crude Pric\n\n[... middle omitted ...]\n\nust assumption before the announcement). We now expect US/EU diesel margins to moderate to \\$46/31/bbl by 2026Q4 (vs. \\$50/37 prior), still 2-3 times above their 2013-2019 seasonal averages, b\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R011",
    "title": "NOM：中国AI投资的真正引擎不是BAT，是“国家资本矩阵”",
    "digest": "[wechat_article.md]\n# NOM：中国AI投资的真正引擎不是BAT，是“国家资本矩阵”\n\n理解中国AI产业的融资结构，比理解其技术路线图更为关键。NOM在最新发布的亚洲宏观研究报告中，系统拆解了中国AI资本开支的资金来源。其核心判断是：中国AI投资的驱动力并非市场自发行为，而是一个由国家资本主导、多层级联动的“资金矩阵”。这与美国的私人资本主导模式形成了根本性差异。\n\n这份报告的价值不在于罗列数字，而在于揭示了资金流向背后的政策逻辑：中国正在用财政工具和国有资本，来对冲外部技术封锁和内部投资下行压力。对于关注中国科技产业、资产配置以及地缘风险的读者而言，理解这个资金矩阵的运作方式，是判断AI赛道未来走向的基本前提。\n\n报告指出，中国AI资本开支的规模与美国仍有量级差距，但其资金来源的“结构性”差异，可能比资金总量本身更重要。美国AI资本开支的绝大部分由超大规模云服务商驱动，而中国则通过中央与地方的多层资金工具，将“国家战略”转化为“实际投资”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 大基金的“三级跳”：从半导体到AI的全链条覆盖\n\n国家集成电路产业投资基金，俗称“大基金”，是中国半导体和AI领域最核心的国家级投资工具。NOM报告显示，大基金已运行三期，注册资本从第一期的1390亿元，跃升至第三期的3440亿元，累计规模接近7000亿元。这三期投资的演进路径，清晰地反映了中国产业政策的阶段性重心：第一期聚焦芯片制造、封测等下游环节；第二期向上游设备、材料等高壁垒领域延伸；第三期则全面覆盖AI产业链，包括存储芯片、光刻设备，甚至参与了AI初创公司DeepSeek的早期融资谈判。\n\n> **KC评论：** 大基金的投资路径不是随机的，它反映了一个清晰的“补链”逻辑。从下游制造到上游设备，再到AI全链条，每一步都在试图填补美国制裁留下\n\n[... middle omitted ...]\n\n信群中继续讨论上述未解问题，获取完整报告原文与更多独家解读。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国AI的钱从哪来\n\n📌 国家资本主导\n\nAI融资全拆解\n\n最近一份投行研报详细拆解了中国AI产业的资金来源，结论很清晰：**国家资本才是绝对主力**。和美国靠科技巨头自己砸钱不同，中国走的是“中央+地方+国企”多层级输血模式。\n\n1️⃣ **“大基金”三期，近7000亿**\n- 国家集成电路产业投资基金（大基金）三期累计注册资本近7000亿\n- 三期（2024年5月）规模最大，3440亿，覆盖芯片设计、制造到AI全链条\n- 2025年1月，三期联合成立了600亿的**国家AI产业投资基金**\n\n2️⃣ **超长期特别国债，AI首次被点名**\n- 2026年4月第二批2170亿中，**AI首次被明确列为支持领域**\n- 国家创业投资引导基金（2025年12月启动）首期1000亿，20年周期，专投芯片、AI、量子等前沿\n\n3️⃣ **“新政工具”撬动7万亿**\n- 2025年9月推出的5000亿政策性金融工具，约40%流向数字经济和AI\n- 这5000亿作为项目资本金，预计能撬动**超7万亿**的总投资\n\n4️⃣ **地方债很克制，但武汉例外**\n- 地方专项债中，仅2.7%流向新基建和战略性新兴产业\n- 但武\n\n[... middle omitted ...]\n\npending centered on cloud services and LLMs. With the renewed sharp declines in investment in Q2 and Beijing's commitment to stabilizing investment, we believe Beijing will likely accelerate b\n\n[... middle omitted ...]\n\nable upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R012",
    "title": "HSBC：中国AI算力需求三年翻五倍，这两家公司最受益",
    "digest": "[wechat_article.md]\n# HSBC：中国AI算力需求三年翻五倍，这两家公司最受益\n\n当大多数投资者还在为AI应用能否落地而争论时，算力基础设施的供需缺口已经给出了最直接的答案。\n\nHSBC证券最新发布的研报给出了一个清晰且大胆的判断：中国AI算力需求将在2028年达到2025年的5倍，而供给端受制于建设周期和GPU产能，将持续处于紧张状态。这意味着，算力租赁价格不仅不会下降，反而有望继续上行。\n\n这份报告的核心逻辑并不复杂：token消耗量在爆发式增长，中国超大规模云服务商（CSP）的资本开支在2026年将突破7000亿元人民币，接近翻倍。而新建一个AI数据中心通常需要18-24个月，供给缺口短期内无法弥合。\n\n在这轮算力军备竞赛中，HSBC明确看好两类公司：一类是拥有大规模AIDC产能的运营商，另一类是数据中心交换机供应商。报告首次覆盖了润泽科技（Range）和锐捷网络（Ruijie），均给予买入评级。\n\n这不仅是技术趋势的判断，更是一个关于稀缺资产定价的故事。\n\n> **KC评论：** HSBC的核心判断与市场普遍预期的“算力过剩论”形成鲜明反差。当很多人担心DeepSeek等高效模型会降低算力需求时，报告用token消耗量的实际数据证明，模型效率提升反而刺激了更大的使用量。这是一个典型的“杰文斯悖论”——效率提升带来更多需求，而非减少。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 三年五倍的增长背后，是token消耗量的指数级爆发\n\nHSBC估算，中国智能算力需求将从2025年的约0.7GW增长至2028年的约5.4GW，年复合增长率高达74%。这个数字的支撑点，是token消耗量的真实数据。\n\n根据国家数据局的数据，2026年3月中国日均token消耗量达到140万亿，较2025年12月增长40%。IDC的预测更为激进，全球\n\n[... middle omitted ...]\n\nrket dynamics。欢迎来知识星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI算力爆发，谁是赢家？\n\n📈算力需求5倍增长\n\nAI算力需求正在狂飙。投行研报预测，到2028年中国AI算力需求将达5GW，是2025年的5倍。字节、阿里、腾讯三大厂2025年资本开支合计3460亿，2026年预计翻倍至7000亿以上。但这跟美国同行比还有很大差距，增长空间依然可观。\n\n🔗网络升级，交换机市场爆发\n数据中心交换机是网络“交通指挥”，研报预计到2030年其市场规模达1180亿，年复合增长28%。原因有三：\n1️⃣ GPU集群扩大，网络层级增加\n2️⃣ 端口速率升级提升产品单价\n3️⃣ SuperPOD架构普及，机柜内互联交换机成新增长点\n\n📦供给紧张，GPU租赁继续涨价\n新AIDC建设通常需要18-24个月，供给瓶颈短期难解。H100租赁价格已从12元/GPU/小时涨到17元，涨了40%。腾讯云、阿里云等纷纷提价，幅度5%-34%。供给紧张下，提供GPU租赁的AIDC运营商将持续受益。\n\n🌏出海新机会：Token出口\n长期看，国内IDC运营商可以通过“Token出口”服务全球推理需求。中国模型成本优势、西部绿色电力便宜、建设成本低，都是竞争力。\n\n📊关注两类公司\n研报重点关注AIDC运营商和交\n\n[... middle omitted ...]\n\ndly boosting their capex, with the combined spending of ByteDance, Alibaba, and Tencent reaching RMB346bn in 2025 and set to more than double to over RMB700bn in 2026 (see Ex 6). This is still\n\n[... middle omitted ...]\n\nalyst, Head of A-share Transportation & Logistics Research\nDavid Wu +86 21 5066 2002\ndavid.wu@hsbcqh.com.cn\n\nAnalyst, A-share Transportation & Logistics Research\nWilliam Sun +86 21 5066 2061\nwilliam.x.d.sun@hsbcqh.com.cn"
  },
  {
    "id": "R013",
    "title": "摩根斯坦利：MS：AI硬件下一个瓶颈不是GPU，是MLCC",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：AI硬件下一个瓶颈不是GPU，是MLCC\n\n当市场还在为英伟达GPU的供应周期和ASIC的替代叙事争论不休时，MS最新发布的全球科技网络研讨会报告指向了一个更隐蔽、但可能更早到来的瓶颈——MLCC（多层陶瓷电容）。\n\n这不是一个关于“缺芯”的老故事。这是AI服务器功耗架构演进带来的被动元件质变。报告的核心判断是：MLCC正在从“跟着服务器出货量走”的被动元件，变成AI服务器性能升级的主动瓶颈。到2027年，AI服务器对MLCC的需求将逼近10亿美元，而全球前五大供应商的产能布局和产品升级节奏，将决定整个AI硬件供应链的交付上限。\n\n这个判断的背后，是三个正在同时发生的结构性变化：AI服务器功耗架构要求MLCC从“外围滤波”走向“近CPU/GPU嵌入”，中国AI芯片在推理侧的成本竞争力正在倒逼全球供应链重新定价，以及MLCC行业本身已经高度寡头化带来的供给刚性。\n\n我们逐一拆解。\n\n> **KC评论：** 这份报告最值得读的部分，不是MLCC需求预测本身，而是它如何把MLCC、中国AI芯片、先进封装和功率半导体放在同一个框架里分析。四者之间的联动关系，才是理解AI硬件供应链当前状态的关键。完整报告里有大量图表支撑这些联动判断，这里只提炼核心逻辑。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. MLCC正在从“被动跟随”变成AI服务器的主动瓶颈\n\n传统服务器中，MLCC是标准化的通用元件，需求增长主要跟着服务器出货量走。但AI服务器的功耗和电流密度已经让传统方案失效。MS分析师指出，新架构要求MLCC具备更高的电容值、更低的等效串联电感（ESL），并且要能嵌入到更靠近CPU和GPU的位置。\n\n这意味着三件事：单台AI服务器的MLCC用量和价值量都在提升；对供应商的技术能力要求跳升了一个台阶；产能\n\n[... middle omitted ...]\n\nmarket dynamics。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI芯片的下一个瓶颈在哪\n\nAI芯片的下一个战场\n\n不止是GPU，MLCC和先进封装也要跟上\n\n最近看了份外资投行的AI半导体研报，信息量很大，把核心逻辑拆给大家👇\n\n1️⃣ AI芯片不只是GPU\n- 云厂商都在做自己的定制芯片（ASIC）\n- 谷歌TPU已到第6代，AWS有Trainium，Meta有MTIA\n- 2025-2028年ASIC出货量预计大幅增长\n- 定制芯片在特定场景效率更高，不是GPU一家独大\n\n2️⃣ 中国AI芯片的“补课”路径\n- 单芯片不够强→多芯片封装→大集群→扩产能\n- 国产芯片在推理场景下，每token成本已接近NVIDIA\n- 字节跳动等公司token用量激增，说明AI需求真实在爆发\n- 研报重点关注寒武纪、沐曦、天数智芯\n\n3️⃣ MLCC——被忽视的AI瓶颈\n- AI服务器对MLCC（多层陶瓷电容）需求激增\n- 预计到2027年，AI服务器MLCC市场接近10亿美元\n- 全球前5大供应商占87%份额，格局很集中\n- 小型元件，卡住大算力\n\n4️⃣ 功率半导体的供需反转\n- 全球功率半导体龙头资本开支连降2年\n- 但工业自动化和AI需求在回暖\n- 供给收缩+需求改善=可能的\n\n[... middle omitted ...]\n\ntanley.com +44 20 7425-2803\n\nDaisy Dai, CFA\nEquity Analyst\nDaisy.Dai@morganstanley.com +852 2848-7310\n\nLydia Lin\nEquity Analyst\nLydia.Lin@morganstanley.com +852 2239-1572\n\n## MS\n\nOVERVIEW\n\n## \n\n[... middle omitted ...]\n\nroup AG (VACN.S)</td><td>E (03/21/2025)</td><td>SFr 706.80</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n## © 2026 MS"
  },
  {
    "id": "R014",
    "title": "GS：美国变压器缺的不是产能，是中国速度",
    "digest": "[wechat_article.md]\n# GS：美国变压器缺的不是产能，是中国速度\n\n这份来自GS的最新变压器出口追踪报告，在五月数据中揭示了一个被市场低估的信号：中国变压器总出口增速从4月的27%同比飙升至5月的72%。但真正值得关注的，不是这个数字本身，而是数字背后的结构性错配——美国本土变压器供需缺口高达72%，而中国供应商的交付速度是本土企业的四倍。\n\n这不是一个简单的“中国出口强劲”的故事。这是一场关于全球电力设备供应链重构中，速度与规模如何重新定义竞争格局的博弈。\n\nGS在这份报告中给出了明确的判断：美国电力变压器需求与本土供应的缺口，将从当前的72%收窄至2028年的57%。这个收窄幅度意味着什么？意味着即便考虑了所有已公布的美国本土扩产计划，短缺仍将持续存在。非传统供应商，包括中国企业，仍有明确的进入空间。\n\n报告覆盖的三家核心标的中，GS对思源电气和国电南瑞给予买入评级，对华明装备维持中性。但比个股评级更重要的，是报告揭示的行业逻辑：在变压器交付周期长达128周的美国市场，思源电气能在6-9个月内完成交付，产能扩张周期仅需一年左右。这种速度优势，正在改写全球电力设备的竞争规则。\n\n> **KC评论：** 72%的缺口听起来像是一个静态数字，但GS真正在说的是一个动态博弈——美国本土产能扩张需要2-3年，而中国供应商的扩产周期是一年。这中间的两年时间差，就是中国变压器企业最大的战略窗口。完整报告中对这个时间差的量化拆解，以及对各区域出口结构的详细分析，值得仔细推敲。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 五月出口数据爆发的真正推手，不是美国而是中东和非洲\n\n五月中国变压器出口增速从27%跃升至72%，表面看是全面开花，但拆解区域贡献后会发现，真正的结构性变化藏在结构里。\n\n非洲贡献了252%的同比增长，占出口总额的18%；中东\n\n[... middle omitted ...]\n\n快速把握市场动态。欢迎来知识星球微信群继续讨论这些未解问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月变压器出口数据大超预期\n\n全球变压器缺口，中国玩家加速补位\n\n最近翻到一份外资投行的变压器出口追踪报告，5月数据有点意思，分享几个核心观察👇\n\n**1/ 出口增速明显加快**\n5月中国变压器（>10MVA）出口额同比增长72%，相比4月的27%大幅提速。非洲（+252%）、中东（+152%）、美洲（+113%）是主要拉动力，这三个区域合计贡献了超60%的出口额。\n\n**2/ 美国市场需求持续强劲**\n对美出口5月同比增长114倍（低基数效应），环比+26%。从电压等级看，10-220MVA占52%，400-500MVA占29%，高端产品占比不低。\n\n**3/ 美国本土供给缺口仍在**\n研报估算，美国电力变压器需求-本土供给缺口将从当前的72%收窄到2028年的57%。虽然本土厂商在扩产（如Virginia Transformer在阿拉巴马建新厂），但变压器交货周期仍高达128周，产能扩张通常需要2-3年。\n\n**4/ 中国供应链的差异化优势**\n对比来看，思源电气（Sieyuan）的交货周期仅6-9个月（24-36周），扩产周期约1年。其第三期变压器工厂刚公告，目标年产值90-100亿元。这种敏捷供应链是\n\n[... middle omitted ...]\n\n, transformer exports to the US delivered 114x yoy growth on a low base, or $26\\%$ mom (vs $+95\\%$ yoy in April).\n\nJacqueline Du  \n+852-2978-1783 |  \njacqueline.du@gs.com  \nGS (Asia) L.L.C.\n\nW\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R015",
    "title": "JPM：中国楼市真正的拐点，不在成交量，在挂牌量",
    "digest": "[wechat_article.md]\n# JPM：中国楼市真正的拐点，不在成交量，在挂牌量\n\n这份JPM最新周度数据监测，在端午假期扰动之下，给出了一个值得认真对待的信号：中国房地产市场并非全面回暖，但一线城市二手房挂牌量的持续下降，正在为价格企稳构筑一个此前被市场低估的底部。这并非简单的“销售回暖”故事，而是一个关于供给收缩如何改变定价权的结构性变化。\n\n市场普遍关注成交量，因为它是情绪的晴雨表。但JPM的数据显示，真正关键的变化发生在供给端。一线城市二手房挂牌量已从3月峰值下降2.6%，上海单周挂牌量更是加速下降1.1%。当卖盘不再涌出，买方才有机会在议价中不再被动。这正是本轮周期与以往最大的不同。\n\n当然，端午假期打乱了所有周度数据的可比性。10城实时二手房成交同比从+13%骤降至0%，60城新房网签同比下滑23%。JPM特别指出，若与去年同期端午假期对比，10城及一线城市成交分别上升15%和10%。数据噪音之下，趋势并未逆转。\n\n但噪音本身也值得解读。假期效应暴露了市场的一个脆弱点：当前成交量的韧性高度依赖交易日的正常节奏，一旦遇到假期扰动，同比增速就会快速收窄。这意味着，市场尚未形成自我强化的内生动力。真正的考验在下半年，当政策脉冲效应消退，成交量能否在没有假期干扰的情况下维持正增长。\n\n> **KC评论：** JPM的数据提醒我们，不要被单一周的数据牵着走。端午假期造成的同比失真，在二手房网签数据中尤为明显——过去9周连续正增长的记录被中断。但剔除假期影响后，10城成交同比仍为正。这个细节在完整报告中有更细致的图表拆解，值得仔细对比。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮变化真正考验的是企业能否把规模转化为议价权\n\nJPM在信用债观点中明确提出“K型分化”正在加剧。5月统计局70城数据显示，一线城市二手房价格连续三个月环比上\n\n[... middle omitted ...]\n\n析，也方便人工快速把握市场动态。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n端午假期影响，楼市数据短期波动\n\n楼市短期扰动，但趋势还在\n\n端午节假期打乱了上周的楼市节奏，数据面看起来有点冷，但调整后其实还好。\n\n📊大陆市场速览\n1️⃣ 二手成交：10城冰山指数同比+0%（前值+13%），一线城市同比-3%（前值+14%）。但研报特别指出，剔除端午假期影响后，10城和一线城市同比+15%/+10%。\n2️⃣ 二手挂牌量：10城继续下降0.2%，一线城市降0.5%（上海降1.1%）。挂牌量自3月高点已降2.6%，这是支撑价格企稳的关键。\n3️⃣ 一手网签：60城同比-23%，同样受假期影响。但对比去年端午同期，实际增长60%（样本较小，仅供参考）。\n4️⃣ 二手网签：12城同比-13%，结束了连续9周的正增长。上海是唯一同比正增长的一线城市（+12%）。\n\n📊香港市场看点\n- 房价指数再涨0.6%W/W，YTD已涨10.4%，达到全年10-15%目标区间。研报预计下半年涨幅放缓至<5%。\n- 二手成交：35大屋苑仅43宗，同比-47%，创春节后新低（部分受天气影响）。\n- 经纪人信心指数从69.6降至68.2，仍高于50（看涨分界线）。\n\n📊信用市场观察\n- 投行研报认为，市场继续呈现K\n\n[... middle omitted ...]\n\ns.\n\n\\- Iceberg 10-city secondary listings (冰山指数二手挂牌量) fell further, down $0.2\\%$ W/W. Tier-1 cities' listings dropped $0.5\\%$ W/W, while Shanghai's dropped another $1.1\\%$ W/W (prior: $-0.6\\%$\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R016",
    "title": "JPM：存储芯片的“更高更久”周期，真正考验的是长协落地速度",
    "digest": "[wechat_article.md]\n# JPM：存储芯片的“更高更久”周期，真正考验的是长协落地速度\n\n过去三个月，亚洲存储芯片公司的股价上涨了44%到184%，同期费城半导体指数上涨20%到88%。这不是一个普通的周期波动。JPM在最新发布的存储市场研报中给出了一个明确的判断：存储芯片正处于一个“higher for longer”的上行周期，而这一轮周期的核心驱动力，已经从供需错配，转向了长期协议（LTA）的谈判进程与AI基础设施投资的再定价。\n\n这份报告的价值，不在于它重申了“存储短缺”这个市场已知的事实，而在于它提供了一个观察框架：当所有人都看到短缺时，真正决定股价能否从“盈利上修”切换到“估值重估”的关键变量，是LTA何时落地。报告承认，LTA谈判比预期更慢，但预计2026年下半年将迎来密集宣布期。这正是当前市场情绪与基本面之间，最值得关注的裂缝。\n\n**KC评论：** JPM的“higher for longer”不是一句口号。它的逻辑链是：短缺加剧 -> 长协锁定价格与量 -> 盈利可见性提升 -> 估值中枢上移。但当前市场只交易了前两步，第三步的“估值重估”还没有发生。这正是完整报告里最值得深挖的图表和假设。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 长协谈判的沉默期，恰恰是布局窗口\n\n5月以来，市场几乎没有听到新的存储长协公告。JPM认为，这并非需求出了问题，而是存储厂商在谈判条件上变得异常谨慎——价格条款、保护机制、预付款比例，每一项都在拉长谈判周期。三星的劳动罢工等公司治理事件，也分散了管理层的注意力。\n\n但报告特别指出，美光与Anthropic的战略协议是一个值得关注的信号。这份协议不仅涉及HBM、DRAM和SSD的长期供应，还包括美光参与Anthropic的H轮融资。这种“股权投资+长期供应”的合同结构，与NAND S\n\n[... middle omitted ...]\n\n人工快速把握全球市场的动态变化。欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n存储芯片的“高价时代”还能走多远？\n\n存储芯片，供需博弈进入深水区\n\n近期存储芯片股价涨幅惊人，过去1-3个月涨了44%-184%。但波动也很大，很多非基本面因素在搅局。马上进入业绩季，有几个关键点值得盯。\n\n**1/ 长期协议（LTA）是估值重估的关键**\n虽然LTA谈判比预期慢，但某外资投行认为，下半年会有更多公告，为存储芯片估值重估铺路。比如，美光与Anthropic签了AI内存供应协议，三星和SK海力士也是Anthropic的战略股东，类似的合作可能陆续有来。\n\n**2/ 内存短缺是“砍配置”的主因**\n最近市场担心AI模型降本（如DeepSeek）会导致内存需求减少，但报告指出，真正的驱动力是供应短缺。HBM4E采样从16Hi转向12Hi，也是客户在预算和性能间做取舍。短缺问题2027年可能比2026年更严重。\n\n**3/ 内存占CSP资本开支比例飙升**\n目前AI内存占云服务商资本开支的比例已从AI时代前的不到20%，飙升至2026年预计的52%以上。投资者需要看到AI服务收入加速，才能支撑这个价值占比。不过，内存的供需关系和战略重要性，决定了它理应获得比历史周期更高的价值份额。\n\n**4/ 中国\n\n[... middle omitted ...]\n\nin 2H26 to pave the way for a memory valuation re-rating. We reiterate our ‘higher for longer’ memory upcycle view and remain constructive on the memory stocks. We remain constructive on major\n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  },
  {
    "id": "R017",
    "title": "摩根斯坦利：MS：2027年CoWoS的蛋糕，NVIDIA切走一半，但真正的变量在CPU",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：2027年CoWoS的蛋糕，NVIDIA切走一半，但真正的变量在CPU\n\n当市场还在争论AI算力需求是否会在2026年见顶时，MS的一份最新报告给出了一个反直觉的判断：2027年，全球AI芯片的先进封装产能不仅不会过剩，反而会迎来新一轮结构性扩张，而推动这一轮增长的，不只有GPU。\n\n这份由Charlie Chan领衔的亚太科技团队发布的报告，核心在于首次系统性地拆解了台积电2027年的CoWoS产能分配。结论清晰且有力：NVIDIA依然是最大的单一客户，但真正让这份报告值得细读的，是它揭示了CPU正在成为先进封装的新变量，以及Google TPU生态中联发科的意外崛起。\n\n这不是一份简单的产能预测。它是一张2027年AI芯片竞争格局的路线图。谁在扩张，谁在收缩，谁在借势，都写在了CoWoS的订单里。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 2027年CoWoS总需求逼近270万片，NVIDIA占比降至45%但绝对值仍翻倍\n\nMS将台积电2027年底的CoWoS产能假设从17万片/月上调至20万片/月，这意味着全球AI XPU产业在2027年将实现约60%的同比增长。而根据供应链核查，全球CoWoS总需求将从2026年的约139万片飙升至2027年的约269万片，接近翻倍。\n\nNVIDIA的CoWoS消耗量预计增长57%，达到122万片。虽然其份额从2026年的56%下降到45%，但这并非需求减弱，而是因为其他玩家的增速更快。NVIDIA在CoWoS-L上的消耗量增长40%至91万片，主要服务于Rubin和Blackwell系列GPU。而CoWoS-R的订单激增则暗示了Vera CPU的出货量几乎翻倍——这一点与MS另一位分析师Joe Moore对NVIDIA数据中心收入增长\n\n[... middle omitted ...]\n\n字、某条供应链或某个假设有疑问，欢迎来星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n2027 年台积电 CoWoS 产能分配指南\n\n**2027 产能地图**\n\n**一张图看懂谁在用台积电先进封装**\n\n某外资投行最新研报更新了 2027 年全球 CoWoS 产能分配，信息量很大，我帮你拆解成三部分。\n\n**1/ 整体格局：需求还在狂飙**\n\n- 2027年全球CoWoS总需求预估年增93%，达到269.4万片晶圆\n- 台积电自己就包了大部分，年底总产能预估到20万片/月\n- 非台积电阵营也在追赶，ASE/SPIL和Amkor合计到年底扩到8万片/月\n\n**2/ 客户拆解：谁吃掉了最多的产能**\n\n- **NVIDIA 仍是老大**：2027年消耗122.2万片，年增57%。主力是CoWoS-L，用在Blackwell和Rubin GPU；CoWoS-R主要给Vera CPU（预估生产575万颗）\n- **AMD 增速最猛**：年增308%到53万片。MI455是重点，Venice CPU的CoWoS需求从5万片跳到27万片\n- **Broadcom 稳中有升**：年增61%到48.4万片。Google TPU（Ironwood+SunFish）占了大头\n- **联发科 是黑马**：从4万片\n\n[... middle omitted ...]\n\nS capacity assumption to 200kwpm by year-end (from 170kwpm), implying \\~60% Y/Y growth for the global AI XPU industry. Based on our industry checks, we break down TSMC's customer mix. Nvidia u\n\n[... middle omitted ...]\n\no Ltd (6515.TW)</td><td>O (04/17/2026)</td><td>NT$9,450.00</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n## © 2026 MS"
  },
  {
    "id": "R018",
    "title": "摩根斯坦利：MS：稀土磁材的“中国之外”叙事，产能不是最大变量",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：稀土磁材的“中国之外”叙事，产能不是最大变量\n\n当市场还在争论“中国稀土出口管制”会带来多大冲击时，MS近期与一位拥有35年行业经验的专家进行了深度对话，并发布了一份罕见的、聚焦于稀土永磁产业“中国之外”产能建设的研报。这份报告的核心判断，可能和许多人的直觉相反：美国规划的稀土永磁产能，到2028年理论上足以覆盖其当前的全部进口需求。但问题不在于能不能造出来，而在于造出来之后，谁用、用在哪、成本是多少。\n\n这份报告的价值不在于给出了一个简单的“看好”或“看空”结论，而是系统性地拆解了从产能到成本、从技术到应用、从军用到民用之间的多层逻辑断层。对于关注产业链安全、新能源上游材料以及全球制造业格局重组的读者而言，这是一份必须细读的框架性文件。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 美国规划的产能数字很漂亮，但“产出”和“产能”是两回事\n\n报告中最引人注目的数据是：美国钕铁硼（NdFeB）磁材产能到2028年可能达到约2.8万吨/年，如果加上已融资和潜在项目，这一数字可达3.5万吨，远期甚至可能超过5万吨。而美国当前从中国、越南和欧洲进口的散装磁材总量大约只有8500吨/年。单从数字看，美国规划的产能是其当前需求的3倍以上。\n\n但专家在讨论中反复强调了一个核心区别：产能不等于产出。决定实际产出的，不是厂房和设备，而是客户认证、金属/合金供应、良品率、工艺控制和成本竞争力。对于有经验的企业，从工厂设计到满产大约需要3年；而对于初创公司，这个时间可能接近6年。这意味着，即便2028年的产能数字是真实的，其实际产出能否达到8500吨，仍然高度不确定。\n\n> **KC评论：** 这是一个经典的“规划泡沫”问题。投资者在看到大量产能建设公告时，需要区分“可融资的计划”和“可交付的产出”。完整报告中详\n\n[... middle omitted ...]\n\n续讨论这些未解的问题，我们会持续跟踪产业链的每一个关键变量。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n稀土永磁：中国之外，谁在加速？\n\n海外稀土磁材产能大扩张\n\n1️⃣ 美国产能2028年或达2.8万吨/年\n投行研报指出，美国钕铁硼磁材产能预计2028年增至约2.8万吨/年，远超当前美国8.5千吨/年的进口量。但专家提醒：客户认证、金属合金供应和成本竞争力仍是关键变量，决定实际产出。\n\n2️⃣ 西方瓶颈：金属合金供应+工艺控制\n海外稀土磁材产业链的短板在“氧化物→金属”转换和薄带铸锭合金生产。有经验的公司从建厂到满产约需3年，初创企业可能需6年。\n\n3️⃣ 稀土减量：重稀土降幅大，轻稀土难替代\n过去20年，钕铁硼中稀土总含量仅从32%降至30.5%。真正的突破在重稀土：通过晶界扩散、晶粒细化等技术，镝、铽用量在某些应用中减少50%以上。钕镨的替代空间有限，铈/镧替代品仅填补了铁氧体和钕铁硼之间的性能空白。\n\n4️⃣ 中国控制已改变采购行为\n专家认为，中国稀土出口管制部分为保护产业地位。客户已开始转向非中国供应商进行认证。西方国防需求虽小（可能<500吨/年），但常与民用工业应用交织，使审批复杂化。\n\n5️⃣ 成本差距短期难缩小\n西方磁材质量有望3年内追上中国，但成本差距更大。专家估算，西方本土钕铁硼磁材可能比\n\n[... middle omitted ...]\n\nn covering current NdFeB imports (\\~8.5ktpa) if executed, but qualification, metal/alloy supply and cost will decide output.\n\n\\- NdPr substitution remains difficult; total rare earth content i\n\n[... middle omitted ...]\n\nkel Industries (NIC.AX)</td><td>E (04/09/2025)</td><td>A$0.96</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R019",
    "title": "GS：美光财报暴露了一个被低估的欧洲AI供应链信号",
    "digest": "[wechat_article.md]\n# GS：美光财报暴露了一个被低估的欧洲AI供应链信号\n\n当一家存储芯片公司季度收入同比增长346%，并给出超出市场预期15%的指引时，市场通常只看到了“存储周期向上”这一个故事。但GS欧洲半导体团队在这份最新研报中，揭示了一个更值得关注的信号：美光财报背后，欧洲AI赋能者正在进入一个需求可见性显著提升的阶段。\n\n美光3QFY26收入约415亿美元，同比增长346%，环比增长74%，远超市场预期的363亿美元。更关键的是，公司预计4QFY26收入将达到500亿美元，环比再增21%。数据中心收入单季超过250亿美元，折合年化运行率约1000亿美元。这些数字本身已经足够震撼，但GS分析师Alexander Duval及其团队真正想告诉市场的是：这些数字对欧洲半导体设备商和AI基础设施提供商意味着什么，而不仅仅是存储芯片本身。\n\n这份报告的核心判断是：美光的业绩和指引，为欧洲半导体设备股ASML、ASMI、BESI以及AI基础设施提供商NBIS提供了需求可见性改善的明确信号，但不同公司的受益逻辑和程度存在本质差异。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 存储供需紧张从周期性波动转向结构性锁定，设备商的订单可见性正在质变\n\n美光在财报中明确表示，AI正在推动数据中心的强劲增长，内存需求显著高于供应。公司预计这种供需失衡将持续到2027年之后，供应要到2028年才逐步改善。这不是一个典型的存储周期顶部信号，而是一个AI驱动的结构性短缺。\n\nGS团队关注到一个关键细节：美光已经签署了16份“照付不议”战略客户协议，覆盖数据中心、消费和汽车终端市场。这些协议不仅包含价格下限，还包含价格上限，五年内累计承诺收入在保底价格下约为1000亿美元。更值得注意的是，这些合同覆盖了美光预计DRAM出货量的约20%和NAND出货量的\n\n[... middle omitted ...]\n\n内容无法在公开文章中完全展开，欢迎加入我们的微信群继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n美光财报，带飞欧洲半导体\n\nAI存储需求爆发\n\n存储供需吃紧，欧洲设备商受益最大\n\n美光最新一季财报超预期，营收约415亿美元，同比猛增346%，环比增74%，比市场预期高出不少。更关键的是，下季度指引继续走高，预计营收500亿美元，比预期高15%。\n\n这意味着什么？AI对存储的需求太强了，数据中心营收超250亿美元，年化接近千亿级别。美光自己说，存储供应明显跟不上，这种供需失衡可能持续到2027年以后。\n\n对欧洲半导体设备商来说，这是个重要信号👇\n\n1️⃣ ASML是最大赢家\n存储芯片占ASML收入约40%，加上EUV光刻机交货周期超12个月，订单可见度很高。美光还和ASML签了多年EUV供应协议，未来EUV层数只会越来越多。\n\n2️⃣ ASMI偏逻辑芯片，但也有存储敞口\n虽然主要靠逻辑芯片需求驱动，存储紧张带来的供应链透明度提升，对它也是好事。\n\n3️⃣ BESI的混合键合技术是关键看点\n三大存储厂商都在测试BESI的混合键合方案，HBM需求持续走强，存储客户采用这项技术的可能性在增加。\n\n4️⃣ NBIS作为AI基础设施提供商\n从裸机到软件都有布局，还在扩大电力容量，AI需求的持续增长对它直接利好。\n\n[... middle omitted ...]\n\nve the Visible Alpha Consensus Data estimate of \\$36.3bn. Further, the company guided for 4QFY26 revenues of \\$50bn at the mid-point (up +21% qoq), which is c.15% above the Visible Alpha Conse\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R020",
    "title": "GS：日本造船业被低估的三个催化剂，不只是AI的替代品",
    "digest": "[wechat_article.md]\n# GS：日本造船业被低估的三个催化剂，不只是AI的替代品\n\n当全球资金疯狂涌入AI主题时，一个传统行业正在东京湾和长崎的船坞里悄然积累着未来三年的利润。GS在最新发布的日本造船业深度报告中，给出了一个与市场主流情绪截然相反的判断：日本造船股的盈利前景实际上正在向上移动，而市场对AI相关资产的追逐，反而制造了估值洼地。\n\n这份报告覆盖了名村造船、三井E&S和东京计器三家GS覆盖标的，同时追踪了日本发动机、古野电气、中国涂料等多家非覆盖公司。核心结论是：日本造船业已经锁定了未来三年半的订单，而即将到来的政策催化剂——产能扩张与防务需求——可能将这一景气周期从“周期性修复”升级为“结构性重估”。\n\n市场目前对日本造船股的谨慎态度，主要源于资金流向AI主题的挤出效应。但GS认为，这种谨慎恰恰忽略了基本面正在发生的实质性改善。截至2026年5月底，日本造船业的订单积压量达到2927万总吨，相当于未来三年半的产能已被填满。2026年前五个月的累计订单量同比仅微降2%，仍处于历史高位。\n\n> **KC评论：** 市场习惯把造船看作周期性行业，但GS这份报告的核心逻辑是，日本造船业正在经历从“周期”到“结构”的转变。订单积压不是问题，问题是产能不够——而这恰好是接下来政策要解决的事情。完整报告里对产能扩张的具体路线图、各公司受益程度的量化拆解，才是真正值得细读的部分。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 产能扩张政策正在改写日本造船业的增长天花板\n\n日本国土交通省海事局在2026年2月底宣布修订造船相关政策，启动产能扩张框架。关键条款是：企业必须制定从2024年水平扩张50%以上产能的计划，才有资格获得造船产业复兴基金的支持——该基金总额3500亿日元，为期10年。日本内阁预计在2026年夏季前后批准包含造船在内的1\n\n[... middle omitted ...]\n\n张节奏、防务订单的落地概率、以及各公司利润率弹性的量化拆解。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本造船业，催化剂还在路上\n\n造船业，还能看\n\n订单排到3.5年后，政策+国防需求双驱动\n\n最近翻了一份关于日本造船业的研报，信息量不小，直接拆解核心逻辑👇\n\n**1/ 订单排到了2029年**\n截至2026年5月，日本船企手持订单量高达2927万总吨，相当于未来3.5年的工作量。这个 backlog 处于历史高位，意味着未来几年的收入已经锁定。\n\n**2/ 两大催化剂值得关注**\n- **产能扩张**：日本国土交通省今年2月发布了造船业政策修订，允许企业申请3500亿日元的振兴基金，条件是产能较2024年提升50%以上。如果大船厂（如名村造船）开始扩产，订单量和估值预期都会上调。\n- **国防需求**：7月有经济财政白皮书和防卫白皮书，年底前修订三大安保文件，美国2027财年国防预算可能拨款18.5亿美元在日韩船厂造军舰。如果订单落地，东京计器（舰船部件供应商）和名村造船（维修业务）都会受益。\n\n**3/ 全球造船市场持续火热**\n受伊朗局势影响，运费飙升，原油油轮需求强劲，新船价格仍处历史高位。日本船厂虽然满负荷运转，但政策支持有望打开产能天花板。\n\n**4/ 几家非覆盖公司也值得看**\n- 日本发动机：\n\n[... middle omitted ...]\n\n industry: The order backlog as of end-May 2026 disclosed by the Japan Ship Exporters' Association was 29.27 mn GT, meaning the industry has already secured vessel demand scheduled for deliver\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R021",
    "title": "GS：热泵在英国卖的不是取暖，是空调",
    "digest": "[wechat_article.md]\n# GS：热泵在英国卖的不是取暖，是空调\n\n这份研报的核心判断，是在一个出奇炎热的英国夏天里形成的。当GS的分析师团队在伯明翰的InstallerSHOW上与欧洲热泵协会（EHPA）负责人以及五家核心设备供应商逐一交流时，他们捕捉到了一个正在发生的结构性转变：全球变暖正在推动空气-空气热泵（air-to-air heat pump）在英国和欧洲的加速渗透。这不是一个关于冬季取暖的故事，而是一个关于夏季制冷需求爆发的故事。对于长期关注欧洲能源转型的投资者而言，这意味着热泵市场的竞争逻辑、产品形态和估值框架，都需要因此重新校准。\n\n这份报告的价值，不仅在于它提供了英国热泵市场的最新一手数据——2025年销量约12.5万台，同比增长27%，渗透率仍不足1%——更在于它揭示了几个正在同时发生、且彼此强化的趋势：政策补贴的加码、中国供应商的激烈竞争、以及欧洲本土OEM通过产品线扩张和渠道护城河来应对的策略。以下是我们从这份研报中提炼出的五个关键洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 全球变暖正在改写热泵的产品逻辑：制冷功能成为新的增长引擎\n\nGS在研报中明确指出，全球变暖很可能会推动空气-空气热泵在英国和欧洲的进一步普及。这个判断的现场感极强——报告提到，在InstallerSHOW举办的那一周，英国和欧洲正经历异常高温。在这种天气下，热泵的制冷功能不再是锦上添花的附加项，而是变成了刚需。\n\n传统上，英国中央供暖系统围绕“湿回路”（即水循环散热片）设计，空气-空气热泵在2025年英国市场的销量占比不到10%。但EHPA总干事Paul Kenny向GS团队透露，这种情况可能会随时间改变，因为整个欧洲的空气-空气热泵市场规模大约是空气-水热泵的6倍。更关键的是，多个OEM正在积极响应安装商的反馈和规模经济需求，大\n\n[... middle omitted ...]\n\nket dynamics。欢迎来微信群继续讨论这些未解问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n热泵市场，正在悄悄换赛道\n\n**热泵市场的冷思考**\n\n刚刚结束的英国InstallerSHOW，跟几家欧洲热泵龙头聊了一圈。几个有意思的信号分享给大家👇\n\n1️⃣ **空气-空气热泵（ATA）正在成为新焦点**\n全球升温背景下，既能供暖又能制冷的ATA热泵被越来越多家庭关注。NIBE首次宣布进入这个市场，Viessmann也在英国推出新品。去年英国ATA销量仅2.5k台，但欧洲ATA市场是空气-水热泵的6倍——这个增量空间，不少厂商都在盯着。\n\n2️⃣ **英国热泵市场：政策红利+低渗透率=长逻辑**\n2025年英国热泵卖了12.5万台，同比增长27%。但对比每年180万台燃气锅炉销量，渗透率还不到1%。政府“温暖之家计划”目标2030年达45万台/年，补贴力度也在加码——空气源/地源热泵补贴7,500英镑，7月起燃油/LPG用户额外加1,500。\n\n3️⃣ **竞争格局：中国厂商是最大变量**\n欧洲厂商的核心壁垒在于安装商渠道——90%以上购买决策由安装商主导，他们习惯从贸易商采购。但中国厂商正通过低价+D2C模式渗透，Octopus Energy和PE背景的OEM也在抢份额。EHPA秘书长直言：热泵OE\n\n[... middle omitted ...]\n\nitions of a number of HVAC OEMs that are seeking to broaden their product ranges in response to installers' feedback and their need to achieve economies of scale. We expect innovations in the \n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R022",
    "title": "NOM：字节跳动的音乐App，正在用AI绕过版权战争",
    "digest": "[wechat_article.md]\n# NOM：字节跳动的音乐App，正在用AI绕过版权战争\n\n字节跳动旗下音乐平台Soda Music的DAU已逼近5000万，年增长仍高达50%，但它走的是一条与腾讯音乐截然不同的路：不烧钱买独家版权，靠广告变现，甚至默许AI翻唱绕过付费墙。NOM最新专家调研揭示，这家公司真正的野心不在音乐本身，而在成为AI音乐时代的规则制定者。\n\n这份报告最值得关注的判断，并非Soda Music的用户增长数字，而是其背后字节跳动对“音乐”这一品类的战略定位：一个用来消耗过剩广告库存、补齐内容生态短板的辅助型护城河，而非独立盈利中心。这与市场普遍将其视为“腾讯音乐挑战者”的叙事形成了根本差异。\n\n**NOM分析师在报告中提出一个关键问题：当版权预算受限时，AI音乐能否成为Soda Music的弯道超车点？** 答案或许比表面看起来更复杂。\n\n> **KC评论：** 这份报告的价值不在于告诉你Soda Music有多少用户，而在于揭示了字节跳动内部两个音乐App（Soda和番茄音乐）在相互竞争，且用户重叠度高达60-70%。这意味着字节跳动在音乐赛道的真实投入，可能远小于外界想象。完整报告中还有关于两个App用户画像的详细拆解，以及字节跳动对合并计划的明确表态。\n\n![研报原图 1](assets/xhs_card_01.png)\n\n## 1. 用户增长正在从“流量输血”转向“活动拉新”，边际效益递减已是定局\n\n截至2026年5月，Soda Music的DAU约为5000万，MAU为1.5亿。专家预计年底DAU将达到约6000万，同比增长约50%。这看似亮眼，但与2025年近100%的增速相比，减速信号已十分明显。\n\n**核心原因在于：抖音的流量转化池正在接近饱和。** 那些可以被抖音自然导流的“可转化用户”基本已被洗过一遍。剩余的用户要么缺乏使用音乐App的刚性需求，要么\n\n[... middle omitted ...]\n\n把握市场动态。欢迎来我们的星球微信群里继续讨论这些未解问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n抖音旗下音乐App，版权不多但AI很强\n\n🎵 音乐平台的另类玩法\n\n最近看了某外资投行对字节旗下Soda Music的专家访谈，发现这家音乐App的打法和腾讯音乐完全不一样。\n\n1/ 用户增长放缓，但基数不小\n截至2026年5月，Soda Music日活约5000万，月活1.5亿。预计年底日活达6000万，同比增长约50%——相比2025年翻倍增速明显放缓。原因是抖音导流的可转化用户池快见顶了。用户日均使用时长也从高峰的60-70分钟降到50分钟，被看小说、刷短剧抢走了时间。\n\n2/ 内部赛马，不合并\n字节旗下有两个音乐App：Soda Music和番茄音乐。两者独立运营，用户重叠率高达60-70%。Soda偏年轻男性，番茄偏年长女性（和番茄小说、番茄畅听、红果短剧生态联动）。专家说短期内没有合并计划。\n\n3/ 广告为主，订阅为辅\nSoda Music的收入结构很特别：广告占70%，订阅只占30%。而腾讯音乐是反过来的——订阅占60-70%。字节给Soda的定位不是追求增长，而是维持盈亏平衡，作为抖音生态的“护城河”，满足用户听歌需求、消化广告库存。\n\n4/ 版权少，但AI音乐可能是王牌\nSoda Music\n\n[... middle omitted ...]\n\n26 June 2026 with a manager from ByteDance's Red Fruit to shed some light on the AI animated drama and short drama industry's status quo and growth sustainability. Please approach your NOM sal\n\n[... middle omitted ...]\n\n front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R023",
    "title": "摩根斯坦利：MS：中国通胀的真相不在PPI，而在工资条",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：MS：中国通胀的真相不在PPI，而在工资条\n\n这可能是当下最反直觉的一个判断：中国近期转正的PPI，并非通胀回归的信号。\n\nMS在最新发布的亚洲经济报告中，直接点破了这个市场普遍存在的误解。报告明确指出，最近几个月PPI同比转正，主要驱动力是油价上涨，而非国内需求的实质性复苏。随着油价回落，这个“伪通胀”信号将很快消失。\n\n真正值得关注的，不是宏观价格指数，而是微观层面的三个指标：非大宗商品部门的利润率、工资增速、以及零售销售。这三个指标，才是判断中国能否从“通缩”走向“温和再通胀”的钥匙。\n\n这份由MS首席亚洲经济学家Chetan Ahya和首席中国经济学家邢自强领衔的报告，系统拆解了中国再通胀进程中的周期性与结构性力量。核心结论是：出口驱动的周期性改善正在发生，但结构性障碍仍未解除，一个2-3%的常态化通胀还不在视野之内。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. PPI转正是一场“油价幻觉”，零售数据才是真相\n\n市场对通胀的讨论，往往被PPI等价格指数牵着走。但MS提醒投资者，必须区分“价格回升”和“需求驱动的通胀”。\n\n报告指出，PPI在经历了约三年半的通缩后转正，但这并非可持续通胀的信号。过去几个月PPI的上行动力主要来自油价上涨。随着国际油价近期回落，这个动力正在消退。更关键的是，非大宗商品部门的利润率并未改善——换句话说，企业仍然没有重新获得定价权。\n\n与PPI形成鲜明对比的是零售销售数据。报告特别提到，随着消费品以旧换新政策效果消退，5月零售销售已经出现绝对收缩。酒店和交通领域的数据同样疲软：6月酒店每间可用客房收入（RevPAR）同比仅增长2%，尽管去年同期基数极低；端午节期间的航空客运增长也相当乏力。\n\n> **KC评论：** 零售数据是理解中国当前经济状态最直接的窗口。P\n\n[... middle omitted ...]\n\n速把握市场动态。欢迎来我们的星球微信群继续讨论这些未解问题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国通胀，走到哪了？\n\n**从出口改善看通胀**\n\n出口回暖，能带起通胀吗？\n\n---\n\n**1. 出口改善是核心变量**\n\n亚洲的资本开支超级周期，正在带动中国非半导体出口回暖。过去两个月，非半导体出口增速已接近两位数。出口改善会逐步传导到企业利润和工资，这是当前通胀回升的主要支撑。\n\n**2. 但别急着说“再通胀”**\n\nPPI转正≠持续通胀。最近PPI上涨更多是因为油价，而非企业定价能力恢复。非大宗商品部门的利润率仍然偏弱，5月零售数据甚至出现收缩，说明消费动力不足。\n\n**3. 三个结构性拖累**\n\n- **人口老龄化**：15-64岁劳动人口从2015年峰值10亿降至9.9亿，总人口自2022年起负增长\n- **房地产调整**：房地产投资占GDP比重已从2014年16%降至6%，低于2004年水平\n- **高储蓄率**：中国家庭储蓄率32%，远高于印度23%、美国4.6%和日本4.1%\n\n**4. 政策定力超预期**\n\n虽然2季度GDP增速可能放缓至4.4%，但政策仍保持克制。政府收入/GDP比率持续下降，15五规划明确以科技和供给为中心，社会福利改革和消费刺激仍将循序渐进。\n\n**5. 跟踪三个指\n\n[... middle omitted ...]\n\n capex supercycle drives a sustained improvement in China's exports.\n\nThis in turn will lift margins for select non-commodity sectors, providing modest support to wage growth and consumption w\n\n[... middle omitted ...]\n\nntee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n## © 2026 MS"
  },
  {
    "id": "R024",
    "title": "NOM：人民币中间价模型已释放一个明确信号",
    "digest": "[wechat_article.md]\n# NOM：人民币中间价模型已释放一个明确信号\n\n人民币兑美元中间价的定价模型，正在发生值得关注的偏移。NOM亚洲外汇策略团队最新发布的模型测算显示，其核心预测值较前次下调了152个基点，计入逆周期因子后的预测值也较前次下调了124个基点。这不是一次简单的技术调整，而是模型层面透露出一个信号：在外部压力与内部目标之间，政策天平正在微妙移动。\n\n这份报告的价值不在于给出一个具体的汇率预测数字，而在于它拆解了影响中间价的两个关键变量——模型本身如何定价，以及逆周期因子如何介入。对于关注人民币资产定价、跨境资本流动和出口企业汇兑风险的读者而言，理解这两个变量的变化方向，比知道6.80还是6.81更重要。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 模型预测的下调并非孤立事件，而是连续误差修正的延续\n\nNOM模型的最新预测值为6.8043，较前次官方预测值6.8195低了152个基点。更值得注意的是，这并非一次性的技术修正。报告附带的模型误差图显示，近期模型预测值与实际中间价之间的偏差已经持续了一段时间。误差不是随机波动，而是呈现出方向性。\n\n这意味着什么？模型是根据一系列可量化的输入变量——包括隔夜美元指数变动、主要货币对走势、市场情绪指标等——来生成预测的。当模型持续高估或低估实际中间价时，通常有两种解释：一是模型遗漏了某些关键变量，二是政策当局在模型之外施加了额外的影响。NOM的这份报告通过同时呈现“不含逆周期因子的模型预测”和“含逆周期因子的模型预测”，实际上为读者提供了一个观察窗口：哪些变化来自市场，哪些变化来自政策。\n\n> **KC评论：** 理解这份报告的关键不在于记住6.8043这个数字，而在于看懂它比前次预测低了152个基点。这意味着模型认为人民币应该比此前预期的更强。如果读者只看最终中间价数字，会错\n\n[... middle omitted ...]\n\n价机制的更深入拆解感兴趣，欢迎加入我们的星球微信群继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n人民币汇率模型给出新信号\n\n📉 6.8043\n\n某外资投行最新模型更新\n\n---\n\n最近看了份某外资投行的亚洲汇率研报，里面关于人民币的部分挺有意思。\n\n1️⃣ 模型投影更新\n最新模型显示，USD/CNY 投影值为 **6.8043**，比上次的 6.8195 低了 152 个基点。相比官方收盘价则低了 9 个基点——方向是偏强。\n\n2️⃣ 逆周期因子调整\n如果加入逆周期因子，模型投影是 **6.8071**，比前一次定盘价低了 124 个基点。说明政策层面也在引导节奏，但不改变方向。\n\n3️⃣ 值得关注的时间节点\n研报列了一串下半年关键事件：\n- 7 月底：政治局经济工作会议\n- 10 月初：国庆黄金周\n- 11 月：APEC 在深圳\n- 12 月中旬：中央经济工作会议\n- 年底：习主席访美（白宫确认）\n\n这些事件都会影响汇率预期和市场情绪。\n\n4️⃣ 模型误差在收窄\n从附图看，近期模型误差（未加逆周期因子）在缩小，说明模型对短期走势的捕捉能力在改善。\n\n🧠 整体感觉：模型方向偏强，但官方会通过逆周期因子平滑节奏，不是急转弯。下半年关键事件密集，汇率弹性可能会加大。\n\n欢迎一起讨论你对下半年人民币走势的看法\n\n[... middle omitted ...]\n\n33ae26d7635da345020d8e8b4fd540a091e77d32aebe383.jpg)  \nSource: NOM\n\nFig. 2: Recent model errors (without counter-cyclical factor adjustment)  \n![](images/1963728bcc5777d533c28c1ea979d6d6b7c7f2\n\n[... middle omitted ...]\n\nOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R025",
    "title": "DB：中国新能源车订单的“冰火两重天”已到关键分水岭",
    "digest": "[wechat_article.md]\n# DB：中国新能源车订单的“冰火两重天”已到关键分水岭\n\n中国新能源汽车市场正在经历一个罕见的“订单分裂”时刻。DB最新发布的周度订单追踪数据显示，2026年6月第三周，头部车企的周订单量呈现出截然不同的方向：比亚迪单周订单突破10万辆，环比暴增134%，而蔚来、华为鸿蒙智行（AITO）等品牌却出现两位数下滑。这不是简单的月度波动，而是竞争格局加速分化的信号。\n\n这份报告的核心判断是：在价格战常态化、消费者预期趋于理性的背景下，订单数据的“冰火两重天”正在揭示一个更深层的结构性变化——规模效应和品牌心智的差距，正从利润表传导至订单簿。那些能持续将流量转化为订单、将订单转化为交付、将交付转化为口碑的车企，正在获得指数级的优势。而这一趋势，可能在未来2-3个季度内决定中国新能源车行业的最终座次。\n\n为什么现在关注这个信号？因为6月第三周的数据恰好处于年中冲刺的关键节点。车企的促销政策、新车型上市节奏、以及消费者对补贴退坡的预期，都在这个时间窗口集中释放。DB的周度订单追踪，是市场上少数能实时捕捉这些动态的高频指标。它比月度销量数据更早揭示趋势，比市场情绪更接近真相。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 比亚迪单周破10万不是意外，而是规模效应的“临界点”爆发\n\n6月第三周，比亚迪新订单达到10.68万辆，环比增长134%，同比增长34%。这是一个令人瞩目的数字。但更值得关注的是环比增速：前一周（6月第二周）订单仅为4.57万辆，而去年同期为8万辆。这种“前低后高”的节奏，反映出比亚迪在年中促销节点上的精准发力。\n\n从结构上看，比亚迪的订单暴增并非来自单一车型的爆款效应，而是其“王朝+海洋”双网体系的全面开花。这种规模效应一旦形成，就会产生正向循环：更多的订单意味着更强的供应链议价权，更强的议价权意味着更低\n\n[... middle omitted ...]\n\n迎来星球的微信群里继续讨论，一起从高频数据中寻找结构性机会。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n比亚迪周订单破10万，蔚来同比涨近200%\n\n周订单激烈洗牌\n\n6月第三周（15-21日），新能源车市出现明显分化。比亚迪单周新订单10.68万，环比+134%，同比+34%，表现非常突出。\n\n其他玩家表现如何？\n\n1. **小米汽车环比+44%**：周订单7200台，同比+80%。产能爬坡后，订单增长有持续性。\n2. **零跑环比+22%**：周订单1.41万，性价比路线稳定放量。\n3. **理想环比+8%**，同比-34%：单周5900台，MEGA风波后的恢复仍需时间。\n4. **小鹏环比+8%**，同比+2%：周订单9000台，G6热度趋于平稳。\n5. **特斯拉环比-4%**，同比+5%：周订单1.26万，Model 3/Y改款后需求稳定。\n6. **蔚来同比+195%**，环比-26%：周订单1.45万，同比高增是因为去年基数低，但环比下滑值得关注。\n7. **HIMA（主问界）环比-36%**，同比+30%：周订单1.17万，M7改款后的爆发期已过。\n\n看点：比亚迪单周超10万，几乎是第二名吉利（2.42万）的4倍多。新势力中，蔚来、零跑、小米都在环比上行通道。\n\n研报未给出吉利和零跑的同比数据，\n\n[... middle omitted ...]\n\n16-22D</td><td rowspan=\"3\">WoW</td><td rowspan=\"3\">YoY</td></tr><tr><td colspan=\"2\">Week #</td></tr><tr><td colspan=\"2\">Calendar days</td></tr><tr><td colspan=\"7\">Weekly New Orders of key OEMs\n\n[... middle omitted ...]\n\nl: (44) 20 7545 8000\n\nDB Securities Inc.  \nThe DB Center  \n1 Columbus Circle  \nNew York, NY 10019  \nTel: (1) 212 250 2500\n\nDB AG  \nFiliale Singapur  \nOne Raffles Quay, South Tower  \nSingapore 048583  \nTel: (65) 6423 8001"
  },
  {
    "id": "R026",
    "title": "摩根斯坦利：中国消费的“5月裂口”比表面数据更值得警惕",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：中国消费的“5月裂口”比表面数据更值得警惕\n\n**一份来自摩根斯坦利的五月消费追踪报告，揭示了两个趋势：消费活动指数进一步下滑，而零售总额同比增速自2022年以来首次转负。但真正值得关注的，不是这些数字本身，而是它们共同指向的一个判断——支撑消费的短期政策效果正在衰减，而结构性压力尚未见底。**\n\n对于关注中国资产配置的投资者来说，这意味着什么？如果你仍在期待一场“消费复苏”来支撑企业盈利的V型反弹，这份报告提供了足够多的理由需要重新审视这个假设。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n![研报原图 2](assets/source_image_02.jpg)\n\n![研报原图 3](assets/source_image_03.jpg)\n\n摩根斯坦利的中国消费活动Z-Score，是一个基于五个高频指标的复合指数，覆盖了居民贷款、餐饮零售、商品零售（不含汽车）、乘用车销售和航空客运量。这个指数在五月继续走低，而MSCI中国指数的同比变化也同步下行。这不是一个孤立的月度波动——它是连续趋势的延续。\n\n> **KC评论：** 摩根斯坦利的Z-Score并非简单的零售数据加总，它的价值在于捕捉了“消费意愿”和“消费能力”的同步变化。当航空客运、餐饮和商品零售同时走软时，这说明消费者不仅在减少大额支出，连日常可选消费也在收缩。这才是真正值得警惕的信号。\n\n**零售总额同比增速在五月转为-0.6%，这是自2022年以来的首次负增长。** 报告指出，造成这一变化的核心原因有两个：以旧换新政策的刺激效果正在消退，以及就业市场的持续疲软。换句话说，政策驱动的消费脉冲已经释放完毕，而内生增长动力尚未接棒。\n\n对于企业决策者而言，这意味着一个更严峻的竞争环境正在形成。当整体蛋糕不再增长甚至缩小时，市场份额的争夺将变得更加残\n\n[... middle omitted ...]\n\n球和微信群继续讨论，我们会分享报告的原版图表和更详细的解读。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月消费数据，比想象更冷\n\n消费还在降温\n\n某外资投行最新研报拆了5个消费指标，5月的数据不太好看。\n\n1️⃣ 整体走弱\n5月消费Z-score继续下滑，航空客运、餐饮、商品零售都在减速。零售总额同比-0.6%，2022年以来首次转负。\n\n2️⃣ 两个微弱亮点\n- 居民贷款小幅回暖\n- 乘用车零售略有改善\n但这两个改善的幅度，远不足以对冲整体下行。\n\n3️⃣ 背后原因\n以旧换新政策效果在消退，就业市场持续疲软，出口对消费的拉动也有限。研报判断，后续消费可能继续放缓。\n\n💡 几个观察角度\n- 消费降级不是短期现象，结构性压力在积累\n- 政策刺激的脉冲效应越来越短，市场需要更实质的支撑\n- 出口好≠消费好，内外需传导链条在断裂\n\n你对后续消费走势怎么看？欢迎一起讨论。\n\n#学习笔记\n\n[source_mineru.md]\nChina Equity Strategy | Asia Pacific\n\n# China Five-factor Consumer Activity Z-Score vs. MSCI China\n\n## Key Takeaways\n\n\\- Consumer Z-score declined f\n\n[... middle omitted ...]\n\nt 1: China Five-factor Consumer Activity Z-Score vs. MSCI China YoY change – Consumer activity declined further in May  \n![](images/7d83a444ae23db8648bfedeeaea9a07604db199635c5f52c83b986120bbb\n\n[... middle omitted ...]\n\nntee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n## © 2026 MS"
  },
  {
    "id": "R027",
    "title": "DB：中国奢侈品进口的“五月寒”比数据本身更值得警惕",
    "digest": "[wechat_article.md]\n# DB：中国奢侈品进口的“五月寒”比数据本身更值得警惕\n\n2026年二季度开局，中国奢侈品进口数据给了市场一记清醒的耳光。\n\nDB最新发布的《China luxury import: Slower April-May vs. months of 1Q》报告显示，2026年4月至5月，中国奢侈品进口量同比下滑7.2%，而一季度这个数字还是正增长5.0%。这不是一个简单的季节性波动。进口量的环比恶化发生在市场普遍预期“消费温和复苏”的背景下，恰恰说明驱动奢侈品消费的核心力量——财富效应和消费者信心——正在重新走弱。\n\n这份报告最值得关注的判断不是“奢侈品卖不动了”，而是：**修复进程中的中国奢侈品市场，正在被两个同时出现的负向力量拖回原点——房价持续承压叠加股市财富效应快速消退。**\n\n一季度进口数据的改善，曾被部分投资者解读为消费信心的底部修复。DB的数据表明，那更像是春节错位和低基数的短暂共振。二季度头两个月的数据，正在把叙事拉回到一个更现实的框架里。\n\n> **KC评论：** 一季度+5.0%和二季度前两个月-7.2%的落差，不是统计噪声。它意味着那些基于“中国消费V型复苏”假设做多奢侈品股票的仓位，需要重新审视其核心逻辑。完整报告中有按品类、按国别拆分的详细进口量变化图表，能帮你判断哪些品牌的暴露最危险。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 手袋进口从+5.1%骤降至-11.2%，是二季度最弱的品类\n\n从品类结构看，手袋是二季度最受伤的板块。4-5月手袋进口量同比下降11.2%，而一季度还是正增长5.1%。其中，非皮革手袋从一季度的+7.5%降至-12.4%，皮革手袋从+2.5%降至-9.8%，跌幅几乎对称。\n\n更值得玩味的是5月单月数据。皮革手袋进口量同比下滑20.6%，是过去一年中最差的一个月\n\n[... middle omitted ...]\n\n迎来知识星球和微信群里继续讨论，一起追踪这些关键信号的演变。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国奢侈品进口，二季度明显降温了\n\n📉 二季度进口转弱\n\n某外资投行最新研报显示，中国奢侈品进口在4-5月同比下跌7.2%，明显不如一季度（+5.0%）。其中跌幅最大的是手袋，同比下降11.2%，珠宝降8.6%，手表降1.9%。5月单月，除了手表，其他品类全部同比下滑。\n\n**为什么？** 宏观数据给出了线索。\n\n1️⃣ **零售和财富效应都在走弱**\n- 4月零售销售额同比仅+0.2%，远低于一季度均值+3.3%\n- 5月进一步跌至-0.6%\n- 消费者信心指数4月同比+1.4%，较一季度均值+3.3%明显放缓\n\n2️⃣ **家庭资产负债表承压**\n- 全国房价同比仍跌4.8%（4月-4.9%）\n- 股市回报率从4月的+21%降至5月的+14.8%\n- 财富增长放缓，可选消费意愿自然减弱\n\n3️⃣ **各品类表现分化**\n- 手袋：皮革款5月进口量暴跌20.6%，而非皮革款仅跌3.1%\n- 珠宝：4月零售同比-23.1%，5月-11.2%，略有改善但仍疲软\n- 手表：瑞士出口至中国5月同比下降21.4%，但出口至亚洲整体仅-2.9%\n\n**关键判断**：一季度的小幅回暖并未延续到二季度。消费者信心恢复速度放\n\n[... middle omitted ...]\n\npts, respectively.\n\nFrom a macro data perspective, weaker YoY in retail and household wealth points to a discretionary spending environment that is tougher for a gradual cFX sales growth recov\n\n[... middle omitted ...]\n\n(49) 69 910 00</td><td>Hong Kong</td><td>Tel: (81) 3 6730 1000</td></tr><tr><td>Australia</td><td></td><td>Tel: (852) 2203 8888</td><td></td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr></table>"
  },
  {
    "id": "R028",
    "title": "GS：奶粉行业最坏的时候正在过去，但赢家已非旧面孔",
    "digest": "[wechat_article.md]\n# GS：奶粉行业最坏的时候正在过去，但赢家已非旧面孔\n\n中国奶粉行业正在经历一场“量价双杀”的尾部出清，但GS最新追踪的尼尔森与线上数据揭示了一个更微妙的信号：行业总量的收缩幅度在边际上趋于稳定，而真正的分化发生在品牌之间——不是国产与进口的简单二分，而是渠道能力、库存周期与品牌信任度的重新排序。\n\n这份发布于2026年5-6月的研报，覆盖了截至2026年4月的线下数据与5月的线上数据。对于关注中国消费品的投资者而言，核心判断只有一个：行业底部可能正在形成，但下一轮增长的受益者，不会是上一轮周期的全部赢家。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 线下降幅边际收窄，但量价结构尚未触底\n\nGS引用的尼尔森数据显示，2026年3-4月，中国婴幼儿配方奶粉线下市场同比下降8.2%，较1-2月的7.7%降幅有所扩大。但深入拆解后，信号并不完全悲观。\n\n关键在于结构：3-4月线下销量同比下降9%，较1-2月的8.7%降幅仅扩大0.3个百分点；而平均售价同比微增0.9%，较1-2月的1.1%增幅略有收窄。这意味着，行业的下行主要仍由销量驱动，而非价格战加剧。母婴店渠道下降7.3%，现代商超渠道下降20%，渠道分化持续。\n\n> **KC评论：** 量跌价稳的组合，说明行业正在经历“被动缩量”而非“主动降价”。这比量价齐跌更接近底部信号。但完整报告中的图表显示，线上渠道5月降幅扩大至19%，京东渠道更是同比下滑26%，这提示线上库存压力可能仍在释放中。想判断线上是否先于线下触底，需要看完整报告中的季度增长趋势图。\n\n![研报原图 2](assets/source_image_02.jpg)\n\n## 2. 伊利逆势转正，飞鹤仍在追赶市场\n\n品牌层面的分化是这份报告最值得细读的部分。\n\n伊利线下渠道在3-4月实现1.9%的同\n\n[... middle omitted ...]\n\n行研报摘要与数据合集，帮助你持续跟踪全球顶级机构的最新判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n奶粉线下增速还在跌，谁在悄悄抢份额？\n\n封面：奶粉线下8%下滑\n\n副标题：Yili逆势转正，A2份额微升\n\n**奶粉行业最新线下数据更新**\n\n3-4月线下奶粉市场同比下降8.2%，比1-2月的7.7%跌幅略有扩大。主要拖累在量——销量跌了9%，价格只微涨0.9%。\n\n**几个有意思的变化👇**\n\n1️⃣ **Yili是唯一销售正增长的大品牌**\n线下同比+1.9%（1-2月是-0.9%），主要靠母婴渠道+2.8%拉动。全渠道（含线上）约-2%。\n\n2️⃣ **Feihe跌幅收窄但仍落后大盘**\n线下同比-12%（1-2月是-15%），市占率21%环比略回升0.4pp，但同比仍降0.9pp。\n\n3️⃣ **A2在母婴渠道持续有韧性**\n同比+2.9%，市占率4.3%（环比+0.2pp，同比+0.4pp），靠量增4%驱动，价格还在降。\n\n4️⃣ **Biostime增长放缓但基数高**\n同比+22.4%（1-2月是+25.8%），市占率从7.8%降至7.5%。\n\n**线上渠道更惨烈**\n\n5月天猫/淘宝/京东合计奶粉销售同比-19%（4月-14%），京东拖累最大（-26%）。Feihe线上-31%，Yili线上\n\n[... middle omitted ...]\n\ny $9\\%$ while ASP grew by $0.9\\%$ yoy vs. $-8.7\\% / +1.1\\%$ yoy in Jan-Feb. By channel, we saw $7.3\\%$ decline in M&B (mom & baby stores) and $-20\\%$ decline from MT (modern trade) in Mar-Apr.\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R029",
    "title": "DB：德国养老金改革的最大变量不是延迟退休，而是强制入市",
    "digest": "[wechat_article.md]\n# DB：德国养老金改革的最大变量不是延迟退休，而是强制入市\n\n德国养老金改革专家组近日发布了33项改革提案。大多数分析聚焦于“延迟退休至67.5岁”或“取消提前退休优惠”——这些确实是重要信号，但并非最值得关注的变量。\n\n这份提案中真正具有结构性意义、且可能对全球资产配置产生深远影响的，是一个被多数中文媒体低估的条款：**引入强制性资本积累制，将2个百分点的毛工资收入强制投入资本市场，预计每年带来350亿欧元的增量资金。**\n\n这不是一个“养老金调整”的新闻，而是一个关于“德国是否会成为下一个瑞典式资本强国”的底层逻辑变化。\n\nDB在最新发布的研报中，将这一条款称为“game-changer”——改变游戏规则的元素。而这一判断，可能比你想象的更值得认真对待。\n\n---\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 德国正在复制瑞典模式，但规模可能远超预期\n\nDB研报明确指出，瑞典的“premium pension”体系是德国此次改革的直接模版。瑞典模式的核心逻辑是：在现收现付制（PAYG）之外，强制要求每个劳动者将一部分收入投入资本市场，通过长期复利积累个人养老金资产。\n\n德国提案的具体设计是：从2028年起，每年逐步增加0.5个百分点的强制缴存比例，到2031年达到2个百分点。这笔资金由雇主和雇员各承担一半，投入一个集中管理的公共养老金基金。\n\n关键数字：到2031年，每年新增资本市场的投资额将达到300至350亿欧元。\n\n> **KC评论：** 350亿欧元是什么概念？它相当于德国DAX指数成分股公司年分红总额的一半左右。而且，这还只是“强制部分”的规模。DB估计，同期改革后的私人养老金（需主动加入）可能带来每年约500亿欧元的资金流入。两者合计，德国每年将有超过800亿欧元的新增资金涌入资本市场。对于一个\n\n[... middle omitted ...]\n\n细节，以及这些变化对中国养老金改革的潜在启示。**\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n德国养老金改革，关键一步已落地\n\n德国养老金，动了真格\n\n德国养老金改革最新方案出炉，专家委员会一口气提了33条建议。核心逻辑很清晰：老龄化社会，现收现付制撑不住了，必须加一道“资本市场的安全垫”。\n\n1/ 最大的惊喜：强制入市\n- 从2028年起，员工和雇主各掏一部分，到2031年累计达到工资的2%\n- 这笔钱（每年约300-350亿欧元）会投入一个中央公共养老金基金，投资资本市场\n- 瑞典的“ premium pension ”模式是参考模板\n- 具体投股票还是债券？研报未给出明确比例，但强调想实现瑞典那样的回报，股票占比不能低\n\n2/ 稳住基本盘的务实操作\n- 退休年龄挂钩预期寿命：从67岁逐步提到67.5岁（2031-2041年）\n- 重新引入“可持续因子”：缴钱的人少了，养老金涨幅自动调低\n- 取消“63岁退休”的优惠通道\n- 把自由职业者（约370万人）纳入法定体系\n- 小额工作（月收入603欧元以下）不再免社保\n\n3/ 时间线看两个节点\n- 7月1日：两党联合执政委员会讨论，这是自设的deadline\n- 秋季立法程序：细节敲定，年底前通过\n\n德国正在做一件很多国家想做但不敢做的事：在公共养老金\n\n[... middle omitted ...]\n\nrs by including self-employed persons. The aggregate effect of all the proposals is a stabilisation of contributions to the PAYG system in the medium term (compared to the status quo ante). Th\n\n[... middle omitted ...]\n\n(49) 69 910 00</td><td>Hong Kong</td><td>Tel: (81) 3 6730 1000</td></tr><tr><td>Australia</td><td></td><td>Tel: (852) 2203 8888</td><td></td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr></table>"
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R001",
    "label": "Exhibit 1",
    "context": "Exhibit 2: US outperformance has been less pronounced versus EM equities than DM equities"
  },
  {
    "figure_id": "F002",
    "report_id": "R001",
    "label": "Exhibit 2",
    "context": "Exhibit 2: US outperformance has been less pronounced versus EM equities than DM equities MSCI World ex USA tracks developed markets, while MSCI ACWI ex USA covers both developed and emerging markets. Exhibit 3: US equity inflows"
  },
  {
    "figure_id": "F003",
    "report_id": "R001",
    "label": "Exhibit 2",
    "context": "Exhibit 2: US outperformance has been less pronounced versus EM equities than DM equities MSCI World ex USA tracks developed markets, while MSCI ACWI ex USA covers both developed and emerging markets. Exhibit 3: US equity inflows"
  },
  {
    "figure_id": "F004",
    "report_id": "R001",
    "label": "Exhibit 4",
    "context": "Exhibit 5: US forward earnings growth expectations alone explain much of the residual between Dollar performance and relative equity performance Univariate regression of the USD\\~log(S&P 500 / MSCI World ex-US) residual on US and"
  },
  {
    "figure_id": "F005",
    "report_id": "R001",
    "label": "Exhibit 4",
    "context": "Exhibit 6: Equity market breadth appears to limit FX spillovers"
  },
  {
    "figure_id": "F006",
    "report_id": "R001",
    "label": "Exhibit 6",
    "context": "Exhibit 7: Global equities have also benefited from the AI boom (in some cases more so than the US) making the more muted support for the Dollar less surprising We reference the following equity indices: the S&P 500, Euro Stoxx 6"
  },
  {
    "figure_id": "F007",
    "report_id": "R001",
    "label": "Exhibit 6",
    "context": "Exhibit 8: The broader equity impulse has clearly shifted from an expected drag to a support for the Dollar"
  },
  {
    "figure_id": "F008",
    "report_id": "R001",
    "label": "Exhibit 7",
    "context": "Exhibit 8: The broader equity impulse has clearly shifted from an expected drag to a support for the Dollar ## TRADE IDEAS ## Best Trade Ideas Across Assets For pricing, charts, and a list of previous recommendations, please visi"
  },
  {
    "figure_id": "F009",
    "report_id": "R002",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Global trade dashboard GLOBAL TRADE EXHIBIT 4: World trade volume growth EXHIBIT 5: US PMI and trade growth EXHIBIT 6: Value of US inventories per sector (excl. automotive)"
  },
  {
    "figure_id": "F010",
    "report_id": "R002",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: World trade volume growth EXHIBIT 5: US PMI and trade growth EXHIBIT 6: Value of US inventories per sector (excl. automotive) EXHIBIT 7: Real value of US inventories per sector (excl. automotive), adjusted for US p"
  },
  {
    "figure_id": "F011",
    "report_id": "R002",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 8: US monthly inventory / sales by sector"
  },
  {
    "figure_id": "F012",
    "report_id": "R002",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 8: US monthly inventory / sales by sector EXHIBIT 9: US inventory / sales"
  },
  {
    "figure_id": "F013",
    "report_id": "R002",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 9: US inventory / sales EXHIBIT 10: US retail inventory / sales"
  },
  {
    "figure_id": "F014",
    "report_id": "R002",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: US monthly inventory / sales by sector EXHIBIT 9: US inventory / sales EXHIBIT 10: US retail inventory / sales EXHIBIT 11: US inventory / sales ratio"
  },
  {
    "figure_id": "F015",
    "report_id": "R002",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: US inventory / sales EXHIBIT 10: US retail inventory / sales EXHIBIT 11: US inventory / sales ratio EXHIBIT 12: US ISM PMI: Customer inventories US ISM PMI: Customer inventories"
  },
  {
    "figure_id": "F016",
    "report_id": "R002",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: US retail inventory / sales EXHIBIT 11: US inventory / sales ratio EXHIBIT 12: US ISM PMI: Customer inventories US ISM PMI: Customer inventories EXHIBIT 13: US consumer spending on goods and services"
  },
  {
    "figure_id": "F017",
    "report_id": "R002",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 14: US real personal expenditure on durable goods ex-automotive"
  },
  {
    "figure_id": "F018",
    "report_id": "R002",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 15: EU-27 real retail sales ex-food, ex-fuel index"
  },
  {
    "figure_id": "F019",
    "report_id": "R002",
    "label": "EXHIBIT 13",
    "context": "EXHIBIT 15: EU-27 real retail sales ex-food, ex-fuel index EXHIBIT 16: China new export orders vs China exports China new export orders vs China exports"
  },
  {
    "figure_id": "F020",
    "report_id": "R002",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 17: US total trade growth"
  },
  {
    "figure_id": "F021",
    "report_id": "R002",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: EU-27 real retail sales ex-food, ex-fuel index EXHIBIT 16: China new export orders vs China exports China new export orders vs China exports EXHIBIT 17: US total trade growth US total trade growth EXHIBIT 18: China"
  },
  {
    "figure_id": "F022",
    "report_id": "R002",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 16: China new export orders vs China exports China new export orders vs China exports EXHIBIT 17: US total trade growth US total trade growth EXHIBIT 18: China total trade growth China total trade growth EXHIBIT 19: Eu"
  },
  {
    "figure_id": "F023",
    "report_id": "R002",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 17: US total trade growth US total trade growth EXHIBIT 18: China total trade growth China total trade growth EXHIBIT 19: Eurozone total trade growth Eurozone total trade growth EXHIBIT 20: Monthly developments in trad"
  },
  {
    "figure_id": "F024",
    "report_id": "R002",
    "label": "EXHIBIT 18",
    "context": "EXHIBIT 18: China total trade growth China total trade growth EXHIBIT 19: Eurozone total trade growth Eurozone total trade growth EXHIBIT 20: Monthly developments in trade value by lane"
  },
  {
    "figure_id": "F025",
    "report_id": "R002",
    "label": "EXHIBIT 20",
    "context": "EXHIBIT 23: Ocean dashboard"
  },
  {
    "figure_id": "F026",
    "report_id": "R002",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 21: Relative magnitude of trade lanes Selected intercontinental trade lanes by 2019 value (\\$tn) EXHIBIT 22: NY Fed Supply Chain Pressure index Global Supply Chain Pressure Index, standard deviations from the mean EXHIBI"
  },
  {
    "figure_id": "F027",
    "report_id": "R002",
    "label": "EXHIBIT 23",
    "context": "EXHIBIT 23: Ocean dashboard EXHIBIT 24: Suez Canal container vessel transits, both directions 30 day moving average EXHIBIT 25: Global schedule reliability for ocean shipping VOLUMES EXHIBIT 27: Global Seafreight TEUs"
  },
  {
    "figure_id": "F028",
    "report_id": "R002",
    "label": "EXHIBIT 24",
    "context": "EXHIBIT 24: Suez Canal container vessel transits, both directions 30 day moving average EXHIBIT 25: Global schedule reliability for ocean shipping VOLUMES EXHIBIT 27: Global Seafreight TEUs Global Seafreight TEUs EXHIBIT 26: Wei"
  },
  {
    "figure_id": "F029",
    "report_id": "R002",
    "label": "EXHIBIT 25",
    "context": "EXHIBIT 25: Global schedule reliability for ocean shipping VOLUMES EXHIBIT 27: Global Seafreight TEUs Global Seafreight TEUs EXHIBIT 26: Weighted average dwell time of truck-bound containers at San Pedro Bay ports EXHIBIT 28:"
  },
  {
    "figure_id": "F030",
    "report_id": "R002",
    "label": "EXHIBIT 27",
    "context": "EXHIBIT 27: Global Seafreight TEUs Global Seafreight TEUs EXHIBIT 26: Weighted average dwell time of truck-bound containers at San Pedro Bay ports EXHIBIT 28: Global Seafreight TEUs EXHIBIT 29: Breakdown of sea volumes by trad"
  },
  {
    "figure_id": "F031",
    "report_id": "R002",
    "label": "EXHIBIT 26",
    "context": "EXHIBIT 26: Weighted average dwell time of truck-bound containers at San Pedro Bay ports EXHIBIT 28: Global Seafreight TEUs EXHIBIT 29: Breakdown of sea volumes by trade lane, last 12 months Trade lane volume share in world se"
  },
  {
    "figure_id": "F032",
    "report_id": "R002",
    "label": "EXHIBIT 28",
    "context": "EXHIBIT 28: Global Seafreight TEUs EXHIBIT 29: Breakdown of sea volumes by trade lane, last 12 months Trade lane volume share in world seaborne container trade ## Headhaul routes EXHIBIT 30: Asia-North America TEUs Asia-North Am"
  },
  {
    "figure_id": "F033",
    "report_id": "R002",
    "label": "EXHIBIT 29",
    "context": "EXHIBIT 32: Asia-Indian subcontinent and Middle East TEUs"
  },
  {
    "figure_id": "F034",
    "report_id": "R002",
    "label": "EXHIBIT 30",
    "context": "EXHIBIT 30: Asia-North America TEUs Asia-North America TEUs EXHIBIT 31: Asia-Europe TEUs Asia-Europe TEUs EXHIBIT 32: Asia-Indian subcontinent and Middle East TEUs Asia-Indian subcontinent and Middle East TEUs EXHIBIT 33: EU-N"
  },
  {
    "figure_id": "F035",
    "report_id": "R002",
    "label": "EXHIBIT 31",
    "context": "EXHIBIT 31: Asia-Europe TEUs Asia-Europe TEUs EXHIBIT 32: Asia-Indian subcontinent and Middle East TEUs Asia-Indian subcontinent and Middle East TEUs EXHIBIT 33: EU-North America TEUs EU-North America TEUs ## Backhaul routes"
  },
  {
    "figure_id": "F036",
    "report_id": "R002",
    "label": "EXHIBIT 32",
    "context": "EXHIBIT 32: Asia-Indian subcontinent and Middle East TEUs Asia-Indian subcontinent and Middle East TEUs EXHIBIT 33: EU-North America TEUs EU-North America TEUs ## Backhaul routes EXHIBIT 34: North America-Asia TEUs North America"
  },
  {
    "figure_id": "F037",
    "report_id": "R002",
    "label": "EXHIBIT 34",
    "context": "EXHIBIT 34: North America-Asia TEUs North America-Asia TEUs EXHIBIT 35: EU-Asia TEUs EU-Asia TEUs EXHIBIT 36: Indian subcontinent and Middle East-Asia TEUs"
  },
  {
    "figure_id": "F038",
    "report_id": "R002",
    "label": "EXHIBIT 34",
    "context": "EXHIBIT 34: North America-Asia TEUs North America-Asia TEUs EXHIBIT 35: EU-Asia TEUs EU-Asia TEUs EXHIBIT 36: Indian subcontinent and Middle East-Asia TEUs Indian subcontinent and Middle East-Asia TEUs EXHIBIT 37: North Americ"
  },
  {
    "figure_id": "F039",
    "report_id": "R002",
    "label": "EXHIBIT 35",
    "context": "EXHIBIT 35: EU-Asia TEUs EU-Asia TEUs EXHIBIT 36: Indian subcontinent and Middle East-Asia TEUs Indian subcontinent and Middle East-Asia TEUs EXHIBIT 37: North America-Europe TEUs North America-Europe TEUs ## Intra-regional ro"
  },
  {
    "figure_id": "F040",
    "report_id": "R002",
    "label": "EXHIBIT 36",
    "context": "EXHIBIT 36: Indian subcontinent and Middle East-Asia TEUs Indian subcontinent and Middle East-Asia TEUs EXHIBIT 37: North America-Europe TEUs North America-Europe TEUs ## Intra-regional routes EXHIBIT 38: Asia-Asia seafreight TE"
  },
  {
    "figure_id": "F041",
    "report_id": "R002",
    "label": "EXHIBIT 38",
    "context": "EXHIBIT 38: Asia-Asia seafreight TEUs Asia-Asia seafreight TEUs EXHIBIT 39: EU-EU TEUs EU-EU TEUs ## Ports"
  },
  {
    "figure_id": "F042",
    "report_id": "R002",
    "label": "EXHIBIT 38",
    "context": "EXHIBIT 38: Asia-Asia seafreight TEUs Asia-Asia seafreight TEUs EXHIBIT 39: EU-EU TEUs EU-EU TEUs ## Ports EXHIBIT 41: US East Coast port volumes million TEUs"
  },
  {
    "figure_id": "F043",
    "report_id": "R002",
    "label": "EXHIBIT 39",
    "context": "EXHIBIT 39: EU-EU TEUs EU-EU TEUs ## Ports EXHIBIT 41: US East Coast port volumes million TEUs EXHIBIT 42: China container port weekly throughput million TEU"
  },
  {
    "figure_id": "F044",
    "report_id": "R002",
    "label": "EXHIBIT 41",
    "context": "EXHIBIT 41: US East Coast port volumes million TEUs EXHIBIT 42: China container port weekly throughput million TEU FREIGHT RATES"
  },
  {
    "figure_id": "F045",
    "report_id": "R002",
    "label": "EXHIBIT 41",
    "context": "EXHIBIT 44: Taiwanese shipping lines revenue growth"
  },
  {
    "figure_id": "F046",
    "report_id": "R002",
    "label": "EXHIBIT 42",
    "context": "EXHIBIT 44: Taiwanese shipping lines revenue growth YoY change"
  },
  {
    "figure_id": "F047",
    "report_id": "R002",
    "label": "EXHIBIT 44",
    "context": "EXHIBIT 44: Taiwanese shipping lines revenue growth YoY change ## Headhaul EXHIBIT 45: Shanghai-LA freight rate (\\$k/FEU) \\$k / FEU"
  },
  {
    "figure_id": "F048",
    "report_id": "R002",
    "label": "EXHIBIT 45",
    "context": "EXHIBIT 45: Shanghai-LA freight rate (\\$k/FEU) \\$k / FEU EXHIBIT 46: Shanghai-Rotterdam freight rate (\\$k/FEU) \\$k / FEU EXHIBIT 47: Shanghai-New York freight rate (\\$k/FEU)"
  },
  {
    "figure_id": "F049",
    "report_id": "R002",
    "label": "EXHIBIT 45",
    "context": "EXHIBIT 45: Shanghai-LA freight rate (\\$k/FEU) \\$k / FEU EXHIBIT 46: Shanghai-Rotterdam freight rate (\\$k/FEU) \\$k / FEU EXHIBIT 47: Shanghai-New York freight rate (\\$k/FEU) \\$k / FEU EXHIBIT 48: Rotterdam-New York"
  },
  {
    "figure_id": "F050",
    "report_id": "R002",
    "label": "EXHIBIT 46",
    "context": "EXHIBIT 46: Shanghai-Rotterdam freight rate (\\$k/FEU) \\$k / FEU EXHIBIT 47: Shanghai-New York freight rate (\\$k/FEU) \\$k / FEU EXHIBIT 48: Rotterdam-New York \\$k / FEU Backhaul"
  },
  {
    "figure_id": "F051",
    "report_id": "R002",
    "label": "EXHIBIT 47",
    "context": "EXHIBIT 47: Shanghai-New York freight rate (\\$k/FEU) \\$k / FEU EXHIBIT 48: Rotterdam-New York \\$k / FEU Backhaul EXHIBIT 50: Rotterdam - Shanghai \\$k / FEU"
  },
  {
    "figure_id": "F052",
    "report_id": "R002",
    "label": "EXHIBIT 48",
    "context": "EXHIBIT 48: Rotterdam-New York \\$k / FEU Backhaul EXHIBIT 50: Rotterdam - Shanghai \\$k / FEU EXHIBIT 51: New York-Rotterdam"
  },
  {
    "figure_id": "F053",
    "report_id": "R002",
    "label": "EXHIBIT 50",
    "context": "EXHIBIT 50: Rotterdam - Shanghai \\$k / FEU EXHIBIT 51: New York-Rotterdam FLEET EXHIBIT 52: Container shipping DWT"
  },
  {
    "figure_id": "F054",
    "report_id": "R002",
    "label": "EXHIBIT 50",
    "context": "EXHIBIT 50: Rotterdam - Shanghai \\$k / FEU EXHIBIT 51: New York-Rotterdam FLEET EXHIBIT 52: Container shipping DWT Container shipping DWT (M)"
  },
  {
    "figure_id": "F055",
    "report_id": "R002",
    "label": "EXHIBIT 51",
    "context": "EXHIBIT 51: New York-Rotterdam FLEET EXHIBIT 52: Container shipping DWT Container shipping DWT (M) EXHIBIT 53: Containership orders and orders / in service ratio Containership order books EXHIBIT 54: Largest shipping lines cap"
  },
  {
    "figure_id": "F056",
    "report_id": "R002",
    "label": "EXHIBIT 52",
    "context": "EXHIBIT 52: Container shipping DWT Container shipping DWT (M) EXHIBIT 53: Containership orders and orders / in service ratio Containership order books EXHIBIT 54: Largest shipping lines capacity evolution m TEUs EXHIBIT 55: To"
  },
  {
    "figure_id": "F057",
    "report_id": "R002",
    "label": "EXHIBIT 53",
    "context": "EXHIBIT 53: Containership orders and orders / in service ratio Containership order books EXHIBIT 54: Largest shipping lines capacity evolution m TEUs EXHIBIT 55: Top 10 shipping lines: current fleet and orders m TEU \\- Orders"
  },
  {
    "figure_id": "F058",
    "report_id": "R002",
    "label": "EXHIBIT 54",
    "context": "EXHIBIT 54: Largest shipping lines capacity evolution m TEUs EXHIBIT 55: Top 10 shipping lines: current fleet and orders m TEU \\- Orders from prior quarters - Orders from Q2 2026 EXHIBIT 56: Delivery schedule of ships no.of ship"
  },
  {
    "figure_id": "F059",
    "report_id": "R002",
    "label": "EXHIBIT 56",
    "context": "EXHIBIT 56: Delivery schedule of ships no.of ships EXHIBIT 57: Delivery schedule (TEUs) - Orders from prior quarters - Orders from Q2 2026"
  },
  {
    "figure_id": "F060",
    "report_id": "R002",
    "label": "EXHIBIT 56",
    "context": "EXHIBIT 56: Delivery schedule of ships no.of ships EXHIBIT 57: Delivery schedule (TEUs) - Orders from prior quarters - Orders from Q2 2026 EXHIBIT 58: Scrapped ships (TEUs) in 000TEUs"
  },
  {
    "figure_id": "F061",
    "report_id": "R002",
    "label": "EXHIBIT 57",
    "context": "EXHIBIT 57: Delivery schedule (TEUs) - Orders from prior quarters - Orders from Q2 2026 EXHIBIT 58: Scrapped ships (TEUs) in 000TEUs EXHIBIT 59: Scrapped ships and avg.age EXHIBIT 60: Average global containership speed"
  },
  {
    "figure_id": "F062",
    "report_id": "R002",
    "label": "EXHIBIT 58",
    "context": "EXHIBIT 58: Scrapped ships (TEUs) in 000TEUs EXHIBIT 59: Scrapped ships and avg.age EXHIBIT 60: Average global containership speed AIRFREIGHT EXHIBIT 61: Air dashboard"
  },
  {
    "figure_id": "F063",
    "report_id": "R002",
    "label": "EXHIBIT 59",
    "context": "EXHIBIT 59: Scrapped ships and avg.age EXHIBIT 60: Average global containership speed AIRFREIGHT EXHIBIT 61: Air dashboard"
  },
  {
    "figure_id": "F064",
    "report_id": "R002",
    "label": "EXHIBIT 61",
    "context": "EXHIBIT 61: Air dashboard FLEET EXHIBIT 62: Active global widebody planes no. of planes - Freighter - Passenger - Temporary freighter conversion - Combi EXHIBIT 63: Active global widebodies maximum takeoff weight MTOW (m)"
  },
  {
    "figure_id": "F065",
    "report_id": "R002",
    "label": "EXHIBIT 63",
    "context": "EXHIBIT 63: Active global widebodies maximum takeoff weight MTOW (m) - Freighter - Passenger - Temporary freighter conversion - Combi EXHIBIT 64: Global widebody jets in service, primary use as cargo"
  },
  {
    "figure_id": "F066",
    "report_id": "R002",
    "label": "EXHIBIT 64",
    "context": "EXHIBIT 64: Global widebody jets in service, primary use as cargo ■ Freighter ■ Temporary freighter conversion EXHIBIT 65: Widebody jets in service / storage Widebody jets in service / storage"
  },
  {
    "figure_id": "F067",
    "report_id": "R002",
    "label": "EXHIBIT 64",
    "context": "EXHIBIT 64: Global widebody jets in service, primary use as cargo ■ Freighter ■ Temporary freighter conversion EXHIBIT 65: Widebody jets in service / storage Widebody jets in service / storage EXHIBIT 66: Freighter orderbook #"
  },
  {
    "figure_id": "F068",
    "report_id": "R002",
    "label": "EXHIBIT 65",
    "context": "EXHIBIT 65: Widebody jets in service / storage Widebody jets in service / storage EXHIBIT 66: Freighter orderbook ## CAPACITY BALANCE AND LOAD FACTOR EXHIBIT 67: Air cargo capacity and chargable weight YoY YoY change"
  },
  {
    "figure_id": "F069",
    "report_id": "R002",
    "label": "EXHIBIT 66",
    "context": "EXHIBIT 66: Freighter orderbook ## CAPACITY BALANCE AND LOAD FACTOR EXHIBIT 67: Air cargo capacity and chargable weight YoY YoY change EXHIBIT 68: Total air cargo revenue growth YoY EXHIBIT 69: Air cargo capacity growth YoY Yo"
  },
  {
    "figure_id": "F070",
    "report_id": "R002",
    "label": "EXHIBIT 67",
    "context": "EXHIBIT 67: Air cargo capacity and chargable weight YoY YoY change EXHIBIT 68: Total air cargo revenue growth YoY EXHIBIT 69: Air cargo capacity growth YoY YoY change EXHIBIT 70: Chargeable weight growth YoY"
  },
  {
    "figure_id": "F071",
    "report_id": "R002",
    "label": "EXHIBIT 68",
    "context": "EXHIBIT 68: Total air cargo revenue growth YoY EXHIBIT 69: Air cargo capacity growth YoY YoY change EXHIBIT 70: Chargeable weight growth YoY YoY change by origin region EXHIBIT 71: Global Capacity Development m tons"
  },
  {
    "figure_id": "F072",
    "report_id": "R002",
    "label": "EXHIBIT 69",
    "context": "EXHIBIT 69: Air cargo capacity growth YoY YoY change EXHIBIT 70: Chargeable weight growth YoY YoY change by origin region EXHIBIT 71: Global Capacity Development m tons EXHIBIT 72: Total airfreight volumes and capacity (YoY)"
  },
  {
    "figure_id": "F073",
    "report_id": "R002",
    "label": "EXHIBIT 70",
    "context": "EXHIBIT 70: Chargeable weight growth YoY YoY change by origin region EXHIBIT 71: Global Capacity Development m tons EXHIBIT 72: Total airfreight volumes and capacity (YoY) FTK: Freight Ton Km; AFTK: Available Freight Ton Km EX"
  },
  {
    "figure_id": "F074",
    "report_id": "R002",
    "label": "EXHIBIT 71",
    "context": "EXHIBIT 71: Global Capacity Development m tons EXHIBIT 72: Total airfreight volumes and capacity (YoY) FTK: Freight Ton Km; AFTK: Available Freight Ton Km EXHIBIT 73: Total airfreight load factor EXHIBIT 74: Total freight ton"
  },
  {
    "figure_id": "F075",
    "report_id": "R002",
    "label": "EXHIBIT 72",
    "context": "EXHIBIT 72: Total airfreight volumes and capacity (YoY) FTK: Freight Ton Km; AFTK: Available Freight Ton Km EXHIBIT 73: Total airfreight load factor EXHIBIT 74: Total freight ton kms (YoY) Global freight ton kms EXHIBIT 75: In"
  },
  {
    "figure_id": "F076",
    "report_id": "R002",
    "label": "EXHIBIT 73",
    "context": "EXHIBIT 73: Total airfreight load factor EXHIBIT 74: Total freight ton kms (YoY) Global freight ton kms EXHIBIT 75: International airfreight volumes and capacity (YoY) FTK: Freight Ton Km; AFTK: Available Freight Ton Km EXHIBI"
  },
  {
    "figure_id": "F077",
    "report_id": "R002",
    "label": "EXHIBIT 74",
    "context": "EXHIBIT 77: International FTKs (YoY)"
  },
  {
    "figure_id": "F078",
    "report_id": "R002",
    "label": "EXHIBIT 75",
    "context": "EXHIBIT 75: International airfreight volumes and capacity (YoY) FTK: Freight Ton Km; AFTK: Available Freight Ton Km EXHIBIT 76: International airfreight load factor EXHIBIT 77: International FTKs (YoY) International freight ton"
  },
  {
    "figure_id": "F079",
    "report_id": "R002",
    "label": "EXHIBIT 76",
    "context": "EXHIBIT 76: International airfreight load factor EXHIBIT 77: International FTKs (YoY) International freight ton kms YoY ## VOLUMES EXHIBIT 78: International airfreight tons"
  },
  {
    "figure_id": "F080",
    "report_id": "R002",
    "label": "EXHIBIT 77",
    "context": "EXHIBIT 77: International FTKs (YoY) International freight ton kms YoY ## VOLUMES EXHIBIT 78: International airfreight tons EXHIBIT 79: International airfreight tons EXHIBIT 80: Asia-Pacific airfreight Asia Pacific airfreight"
  },
  {
    "figure_id": "F081",
    "report_id": "R002",
    "label": "EXHIBIT 78",
    "context": "EXHIBIT 78: International airfreight tons EXHIBIT 79: International airfreight tons EXHIBIT 80: Asia-Pacific airfreight Asia Pacific airfreight tons EXHIBIT 81: North America airfreight"
  },
  {
    "figure_id": "F082",
    "report_id": "R002",
    "label": "EXHIBIT 79",
    "context": "EXHIBIT 79: International airfreight tons EXHIBIT 80: Asia-Pacific airfreight Asia Pacific airfreight tons EXHIBIT 81: North America airfreight North America airfreight tons EXHIBIT 82: Europe airfreight"
  },
  {
    "figure_id": "F083",
    "report_id": "R002",
    "label": "EXHIBIT 80",
    "context": "EXHIBIT 80: Asia-Pacific airfreight Asia Pacific airfreight tons EXHIBIT 81: North America airfreight North America airfreight tons EXHIBIT 82: Europe airfreight Europe airfreight tons EXHIBIT 83: Middle East airfreight"
  },
  {
    "figure_id": "F084",
    "report_id": "R002",
    "label": "EXHIBIT 81",
    "context": "EXHIBIT 81: North America airfreight North America airfreight tons EXHIBIT 82: Europe airfreight Europe airfreight tons EXHIBIT 83: Middle East airfreight Middle East airfreight tons AIRPORT GATEWAYS"
  },
  {
    "figure_id": "F085",
    "report_id": "R002",
    "label": "EXHIBIT 82",
    "context": "EXHIBIT 82: Europe airfreight Europe airfreight tons EXHIBIT 83: Middle East airfreight Middle East airfreight tons AIRPORT GATEWAYS EXHIBIT 84: Frankfurt EXHIBIT 85: Heathrow"
  },
  {
    "figure_id": "F086",
    "report_id": "R002",
    "label": "EXHIBIT 83",
    "context": "EXHIBIT 83: Middle East airfreight Middle East airfreight tons AIRPORT GATEWAYS EXHIBIT 84: Frankfurt EXHIBIT 85: Heathrow EXHIBIT 86: Paris Paris cargo volumes"
  },
  {
    "figure_id": "F087",
    "report_id": "R002",
    "label": "EXHIBIT 84",
    "context": "EXHIBIT 84: Frankfurt EXHIBIT 85: Heathrow EXHIBIT 86: Paris Paris cargo volumes EXHIBIT 87: Amsterdam Schipol"
  },
  {
    "figure_id": "F088",
    "report_id": "R002",
    "label": "EXHIBIT 85",
    "context": "EXHIBIT 85: Heathrow EXHIBIT 86: Paris Paris cargo volumes EXHIBIT 87: Amsterdam Schipol EXHIBIT 88: Los Angeles LAX international cargo volumes"
  },
  {
    "figure_id": "F089",
    "report_id": "R002",
    "label": "EXHIBIT 86",
    "context": "EXHIBIT 86: Paris Paris cargo volumes EXHIBIT 87: Amsterdam Schipol EXHIBIT 88: Los Angeles LAX international cargo volumes EXHIBIT 89: Hong Kong Hong Kong cargo volumes"
  },
  {
    "figure_id": "F090",
    "report_id": "R002",
    "label": "EXHIBIT 87",
    "context": "EXHIBIT 87: Amsterdam Schipol EXHIBIT 88: Los Angeles LAX international cargo volumes EXHIBIT 89: Hong Kong Hong Kong cargo volumes EXHIBIT 90: Narita cargo volumes"
  },
  {
    "figure_id": "F091",
    "report_id": "R002",
    "label": "EXHIBIT 88",
    "context": "EXHIBIT 88: Los Angeles LAX international cargo volumes EXHIBIT 89: Hong Kong Hong Kong cargo volumes EXHIBIT 90: Narita cargo volumes EXHIBIT 91: Seoul Incheon"
  },
  {
    "figure_id": "F092",
    "report_id": "R002",
    "label": "EXHIBIT 89",
    "context": "EXHIBIT 89: Hong Kong Hong Kong cargo volumes EXHIBIT 90: Narita cargo volumes EXHIBIT 91: Seoul Incheon ## EXHIBIT 92: Miami-Dade"
  },
  {
    "figure_id": "F093",
    "report_id": "R002",
    "label": "EXHIBIT 90",
    "context": "EXHIBIT 90: Narita cargo volumes EXHIBIT 91: Seoul Incheon ## EXHIBIT 92: Miami-Dade Miami international cargo volumes"
  },
  {
    "figure_id": "F094",
    "report_id": "R002",
    "label": "EXHIBIT 91",
    "context": "EXHIBIT 91: Seoul Incheon ## EXHIBIT 92: Miami-Dade Miami international cargo volumes RATES EXHIBIT 93: Aggregate airfreight rate \\$/kg EXHIBIT 94: Global composite airfreight rate"
  },
  {
    "figure_id": "F095",
    "report_id": "R002",
    "label": "EXHIBIT 92",
    "context": "EXHIBIT 92: Miami-Dade Miami international cargo volumes RATES EXHIBIT 93: Aggregate airfreight rate \\$/kg EXHIBIT 94: Global composite airfreight rate Global composite airfreight rate (\\$/kg) EXHIBIT 95: Hongkong to USA yield"
  },
  {
    "figure_id": "F096",
    "report_id": "R002",
    "label": "EXHIBIT 93",
    "context": "EXHIBIT 93: Aggregate airfreight rate \\$/kg EXHIBIT 94: Global composite airfreight rate Global composite airfreight rate (\\$/kg) EXHIBIT 95: Hongkong to USA yields EXHIBIT 96: Shanghai to Germany yields"
  },
  {
    "figure_id": "F097",
    "report_id": "R002",
    "label": "EXHIBIT 94",
    "context": "EXHIBIT 94: Global composite airfreight rate Global composite airfreight rate (\\$/kg) EXHIBIT 95: Hongkong to USA yields EXHIBIT 96: Shanghai to Germany yields EXHIBIT 97: Amsterdam to USA yields"
  },
  {
    "figure_id": "F098",
    "report_id": "R002",
    "label": "EXHIBIT 95",
    "context": "EXHIBIT 95: Hongkong to USA yields EXHIBIT 96: Shanghai to Germany yields EXHIBIT 97: Amsterdam to USA yields EXHIBIT 98: Frankfurt to China yields"
  },
  {
    "figure_id": "F099",
    "report_id": "R002",
    "label": "EXHIBIT 96",
    "context": "EXHIBIT 96: Shanghai to Germany yields EXHIBIT 97: Amsterdam to USA yields EXHIBIT 98: Frankfurt to China yields EXHIBIT 99: Mumbai to UK yields"
  },
  {
    "figure_id": "F100",
    "report_id": "R002",
    "label": "EXHIBIT 97",
    "context": "EXHIBIT 97: Amsterdam to USA yields EXHIBIT 98: Frankfurt to China yields EXHIBIT 99: Mumbai to UK yields ## PARCEL"
  },
  {
    "figure_id": "F101",
    "report_id": "R002",
    "label": "EXHIBIT 98",
    "context": "EXHIBIT 98: Frankfurt to China yields EXHIBIT 99: Mumbai to UK yields ## PARCEL ## GERMANY EXHIBIT 100: EU consumer confidence and real retail sales growth"
  },
  {
    "figure_id": "F102",
    "report_id": "R002",
    "label": "EXHIBIT 100",
    "context": "EXHIBIT 100: EU consumer confidence and real retail sales growth EXHIBIT 101: Germany retail sales index, not in stores, stalls or markets Germany retail sales index, not in stores, stalls or markets (nominal) ## I. REQUIRED DISC"
  },
  {
    "figure_id": "F103",
    "report_id": "R002",
    "label": "EXHIBIT 100",
    "context": "EXHIBIT 100: EU consumer confidence and real retail sales growth EXHIBIT 101: Germany retail sales index, not in stores, stalls or markets Germany retail sales index, not in stores, stalls or markets (nominal) ## I. REQUIRED DISC"
  },
  {
    "figure_id": "F104",
    "report_id": "R004",
    "label": "Figure 2",
    "context": "Figure 2: Path of policy rates (ESTR) prescribed by a suite of monetary policy rules produced using the ECB's June staff baseline projections"
  },
  {
    "figure_id": "F105",
    "report_id": "R004",
    "label": "Figure 3",
    "context": "Figure 3: Oil and gas futures contracts vs the ECB's June alternative scenarios"
  },
  {
    "figure_id": "F106",
    "report_id": "R004",
    "label": "Figure 3",
    "context": "Figure 3: Oil and gas futures contracts vs the ECB's June alternative scenarios"
  },
  {
    "figure_id": "F107",
    "report_id": "R004",
    "label": "Figure 4",
    "context": "Figure 6: Severe scenario – policy rule prescriptions"
  },
  {
    "figure_id": "F108",
    "report_id": "R004",
    "label": "Figure 4",
    "context": "Figure 6: Severe scenario – policy rule prescriptions"
  },
  {
    "figure_id": "F109",
    "report_id": "R004",
    "label": "Figure 5",
    "context": "Figure 6: Severe scenario – policy rule prescriptions"
  },
  {
    "figure_id": "F110",
    "report_id": "R004",
    "label": "Figure 7",
    "context": "Figure 8: Difference between the policy rule prescriptions (pp) using the June staff projections vs the March projections – when HICP ex energy is used as the inflation measure in the rules"
  },
  {
    "figure_id": "F111",
    "report_id": "R004",
    "label": "Figure 7",
    "context": "Figure 8: Difference between the policy rule prescriptions (pp) using the June staff projections vs the March projections – when HICP ex energy is used as the inflation measure in the rules"
  },
  {
    "figure_id": "F112",
    "report_id": "R004",
    "label": "Figure 9",
    "context": "Figure 9: ESTR vs policy rule prescriptions (%) during the 2021-22 pandemic and energy shock"
  },
  {
    "figure_id": "F113",
    "report_id": "R004",
    "label": "Figure 10",
    "context": "Figure 10: ESTR vs policy rule prescriptions (%) during the latest rate cutting cycle"
  },
  {
    "figure_id": "F114",
    "report_id": "R005",
    "label": "Exhibit 1",
    "context": "Exhibit 3: Over the past 3-4 years, New entrants have led to lower Asian prices, with Australia remaining uncompetitive, to incentivise imports into China China HCC netback to Aus QLD vs. FOB price (spot)"
  },
  {
    "figure_id": "F115",
    "report_id": "R005",
    "label": "Exhibit 1",
    "context": "Exhibit 3: Over the past 3-4 years, New entrants have led to lower Asian prices, with Australia remaining uncompetitive, to incentivise imports into China China HCC netback to Aus QLD vs. FOB price (spot) Exhibit 4: Seaborne coal"
  },
  {
    "figure_id": "F116",
    "report_id": "R005",
    "label": "Exhibit 2",
    "context": "Exhibit 4: Seaborne coal freight rates have almost normalised to pre-war levels Seaborne freight (\\$/t) - Australia to China Exhibit 5: Australia remains a small share of China imports (\\~7% in 2025), with Aus exports to China do"
  },
  {
    "figure_id": "F117",
    "report_id": "R005",
    "label": "Exhibit 3",
    "context": "Exhibit 5: Australia remains a small share of China imports (\\~7% in 2025), with Aus exports to China down materially from pre-2020 Australia Coking Coal Export Volumes to China Exhibit 6: Mongolian and Russian coal has almost fu"
  },
  {
    "figure_id": "F118",
    "report_id": "R005",
    "label": "Exhibit 4",
    "context": "Exhibit 6: Mongolian and Russian coal has almost fully replaced imports from Australia, despite total import growth China's coking coal imports - share by country Exhibit 7: China imports are dominated by Mongolia (\\~50% in 2025)"
  },
  {
    "figure_id": "F119",
    "report_id": "R005",
    "label": "Exhibit 5",
    "context": "Exhibit 7: China imports are dominated by Mongolia (\\~50% in 2025), with 2026 volumes up \\~70% YTD compared to the same period last year China Coking Coal Import Volumes: Mongolia Exhibit 8: Total Russian exports have increased \\"
  },
  {
    "figure_id": "F120",
    "report_id": "R005",
    "label": "Exhibit 6",
    "context": "Exhibit 8: Total Russian exports have increased \\~6% compared to the same period last year Total Russia Coking Coal Export Volumes Exhibit 9: India met coal imports (Mt annualised)"
  },
  {
    "figure_id": "F121",
    "report_id": "R005",
    "label": "Exhibit 7",
    "context": "Exhibit 9: India met coal imports (Mt annualised) Global Coking Coal Prices Exhibit 10: Australian HCC, PCI and Semi-Soft prices"
  },
  {
    "figure_id": "F122",
    "report_id": "R005",
    "label": "Exhibit 8",
    "context": "Exhibit 11: Australia, US and China met coal prices"
  },
  {
    "figure_id": "F123",
    "report_id": "R005",
    "label": "Exhibit 9",
    "context": "Exhibit 9: India met coal imports (Mt annualised) Global Coking Coal Prices Exhibit 10: Australian HCC, PCI and Semi-Soft prices Exhibit 11: Australia, US and China met coal prices Australian Coal Supply Exhibit 12: QLD Coal"
  },
  {
    "figure_id": "F124",
    "report_id": "R005",
    "label": "Exhibit 10",
    "context": "Exhibit 13: Abbot Point (GLEN/Adani/QCoal) monthly exports (annualised)"
  },
  {
    "figure_id": "F125",
    "report_id": "R005",
    "label": "Exhibit 11",
    "context": "Exhibit 14: Hay Point (BHP) monthly exports (annualised)"
  },
  {
    "figure_id": "F126",
    "report_id": "R005",
    "label": "Exhibit 12",
    "context": "Exhibit 15: Dalrymple Bay (WHC/SMR/AAL) monthly exports (annualised)"
  },
  {
    "figure_id": "F127",
    "report_id": "R005",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Abbot Point (GLEN/Adani/QCoal) monthly exports (annualised) Exhibit 14: Hay Point (BHP) monthly exports (annualised) Exhibit 15: Dalrymple Bay (WHC/SMR/AAL) monthly exports (annualised) Exhibit 16: Gladstone (WHC)"
  },
  {
    "figure_id": "F128",
    "report_id": "R005",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Hay Point (BHP) monthly exports (annualised) Exhibit 15: Dalrymple Bay (WHC/SMR/AAL) monthly exports (annualised) Exhibit 16: Gladstone (WHC) monthly exports (annualised) ## Disclosure Appendix"
  },
  {
    "figure_id": "F129",
    "report_id": "R005",
    "label": "Exhibit 15",
    "context": "Exhibit 15: Dalrymple Bay (WHC/SMR/AAL) monthly exports (annualised) Exhibit 16: Gladstone (WHC) monthly exports (annualised) ## Disclosure Appendix ## Reg AC We, Matt Greene, Paul Young, Chris Bulgin and Riccardo D'Agata, hereb"
  },
  {
    "figure_id": "F130",
    "report_id": "R006",
    "label": "Exhibit 1",
    "context": "Exhibit 1: China monthly fuel consumption (including inventory movement) Exhibit 2: China fuel inventory and refiner run-rates: fuel inventory has been elevated since SOH disruptions despite significant run-rate cuts at refiner"
  },
  {
    "figure_id": "F131",
    "report_id": "R006",
    "label": "Exhibit 1",
    "context": "Exhibit 1: China monthly fuel consumption (including inventory movement) Exhibit 2: China fuel inventory and refiner run-rates: fuel inventory has been elevated since SOH disruptions despite significant run-rate cuts at refiner"
  },
  {
    "figure_id": "F132",
    "report_id": "R006",
    "label": "Exhibit 1",
    "context": "Exhibit 1: China monthly fuel consumption (including inventory movement) Exhibit 2: China fuel inventory and refiner run-rates: fuel inventory has been elevated since SOH disruptions despite significant run-rate cuts at refiner"
  },
  {
    "figure_id": "F133",
    "report_id": "R006",
    "label": "Exhibit 2",
    "context": "Exhibit 2: China fuel inventory and refiner run-rates: fuel inventory has been elevated since SOH disruptions despite significant run-rate cuts at refiners MS ASIA LIMITED+ Jack Lu"
  },
  {
    "figure_id": "F134",
    "report_id": "R007",
    "label": "FIGURE 2",
    "context": "The earnings growth engine is firing on all cylinders. Activity data remain constructive: industrial production is on the rise, ISM manufacturing PMI is finally back in expansionary territory, and both durable goods and S&P Global manufacturing output point to"
  },
  {
    "figure_id": "F135",
    "report_id": "R007",
    "label": "FIGURE 2",
    "context": "FIGURE 2. The yield-equity correlation is testing the lower bound of its historical range at current levels of nominal 10Y FIGURE 3. The prospect of resumed hikes has not typically derailed equities ahead of the event S&P 500 Performance Around Fed Reversal of"
  },
  {
    "figure_id": "F136",
    "report_id": "R007",
    "label": "FIGURE 3",
    "context": "FIGURE 3. The prospect of resumed hikes has not typically derailed equities ahead of the event S&P 500 Performance Around Fed Reversal of Easing In addition, AI capex continues to pose its own risks. While boosting EPS growth now, it also raises execution risk"
  },
  {
    "figure_id": "F137",
    "report_id": "R007",
    "label": "FIGURE 4",
    "context": "In addition, AI capex continues to pose its own risks. While boosting EPS growth now, it also raises execution risks later. We believe \"peak capex\" has been deferred further out, reflecting both persistent supply constraints in training compute capacity as wel"
  },
  {
    "figure_id": "F138",
    "report_id": "R007",
    "label": "FIGURE 5",
    "context": "From AI's S-Curve Is Steepening (1 June 2026). FIGURE 5. ...which is \\~26% above the Street.... FIGURE 6. ...driving operating cash flow pressure that we expect to intensify into 2028... Estimates from BARC' Internet research team. Note that for AMZN, capex is"
  },
  {
    "figure_id": "F139",
    "report_id": "R007",
    "label": "FIGURE 6",
    "context": "FIGURE 6. ...driving operating cash flow pressure that we expect to intensify into 2028... Estimates from BARC' Internet research team. Note that for AMZN, capex is AWS only, while OCF is total AMZN. FIGURE 7. ...which is not baked into consensus estimates All"
  },
  {
    "figure_id": "F140",
    "report_id": "R007",
    "label": "FIGURE 8",
    "context": "## Raise FY26 EPS estimate to \\$337 from \\$321 We raise our FY26 S&P 500 EPS estimate to \\$337 from \\$321, modestly below the Street's \\$341 and implying 20.8% Y/Y growth from \\$279 in FY25. Since our last update, three developments argue for a higher EPS esti"
  },
  {
    "figure_id": "F141",
    "report_id": "R007",
    "label": "FIGURE 8",
    "context": "Around our base case of \\$337, we estimate a relatively tight bull/bear range of \\$343/\\$329, underscoring that the core debate is less about directional earnings risk and more about the magnitude and persistence of key cyclical drivers. The dispersion is prim"
  },
  {
    "figure_id": "F142",
    "report_id": "R007",
    "label": "FIGURE 9",
    "context": "Data as of 10 June 2026. FIGURE 9. We estimate \\$337 in FY26 EPS (+21% Y/Y) vs. Street at \\$341 Data as of 16 Jun 2026 FIGURE 10. FY26 base, bull & bear case EPS scenarios Data as of 10 Jun 2026 Looking ahead, we introduce a preliminary FY27 EPS estimate of \\$"
  },
  {
    "figure_id": "F143",
    "report_id": "R007",
    "label": "FIGURE 11",
    "context": "Data as of 10 Jun 2026 Looking ahead, we introduce a preliminary FY27 EPS estimate of \\$389, reflecting a modest deceleration in growth. Our framework assumes a partial recovery in consumption on a Y/Y basis, coupled with continued strength in industrial produ"
  },
  {
    "figure_id": "F144",
    "report_id": "R007",
    "label": "FIGURE 11",
    "context": "Looking ahead, we introduce a preliminary FY27 EPS estimate of \\$389, reflecting a modest deceleration in growth. Our framework assumes a partial recovery in consumption on a Y/Y basis, coupled with continued strength in industrial production as the lagged eff"
  },
  {
    "figure_id": "F145",
    "report_id": "R007",
    "label": "FIGURE 12",
    "context": "FIGURE 12. FY27 base, bull & bear case EPS scenarios Data as of 10 Jun 2026 FIGURE 13. YTD revisions to full-year EPS are running well ahead of 10Y norms... FIGURE 14. ...with all quarters seeing a pickup in EPS estimates since the end of calendar 1Q26 Data as"
  },
  {
    "figure_id": "F146",
    "report_id": "R007",
    "label": "FIGURE 13",
    "context": "FIGURE 13. YTD revisions to full-year EPS are running well ahead of 10Y norms... FIGURE 14. ...with all quarters seeing a pickup in EPS estimates since the end of calendar 1Q26 Data as of 16 June 2026. FIGURE 15. FY26 EPS growth estimates for Tech industries, "
  },
  {
    "figure_id": "F147",
    "report_id": "R007",
    "label": "FIGURE 15",
    "context": "FIGURE 15. FY26 EPS growth estimates for Tech industries, YE25 vs. today Data as of 13 June 2026. FIGURE 16. Semis and IT Hardware account for more than half of the + \\$31 added to FY26 Street estimates YTD Data as of 16 June 2026. ## Raise 2026 price target t"
  },
  {
    "figure_id": "F148",
    "report_id": "R007",
    "label": "FIGURE 17",
    "context": "Our SOTP valuation framework assigns Big Tech a lower baseline multiple than in March (26x vs. 27.5x). We continue to believe the group offers durable earnings growth, but we trim our valuation assumptions to account for uncertainties around the scale, funding"
  },
  {
    "figure_id": "F149",
    "report_id": "R007",
    "label": "FIGURE 17",
    "context": "Applying the blended multiple takes our YE26 S&P 500 target up to 7800 from 7650, 23x our \\$337 FY26 EPS estimate. Our upwardly revised EPS estimate does the heavy lifting, as our valuation assumptions are reduced modestly from our last update. Our base case r"
  },
  {
    "figure_id": "F150",
    "report_id": "R007",
    "label": "FIGURE 18",
    "context": "FIGURE 18. 2026 base, bull & bear case PT scenarios Data as of 16 Jun 2026 Extending the horizon into 2027, we introduce targets of 8800 in our base case, 9600 in the bull case and 7100 in the bear case, reflecting a more tempered but still constructive long-d"
  },
  {
    "figure_id": "F151",
    "report_id": "R007",
    "label": "FIGURE 19",
    "context": "Extending the horizon into 2027, we introduce targets of 8800 in our base case, 9600 in the bull case and 7100 in the bear case, reflecting a more tempered but still constructive long-duration pathway for equities. These estimates are derived by modestly trimm"
  },
  {
    "figure_id": "F152",
    "report_id": "R007",
    "label": "FIGURE 21",
    "context": "Data as of 11 Jun 2026 ## Sector and factor recommendations As a preamble to our sector views, we'd point out that the evolution of the AI narrative continues to reshape market structure. Correlations within sectors have collapsed to historically low levels, r"
  },
  {
    "figure_id": "F153",
    "report_id": "R007",
    "label": "FIGURE 21",
    "context": "As a preamble to our sector views, we'd point out that the evolution of the AI narrative continues to reshape market structure. Correlations within sectors have collapsed to historically low levels, reflecting a market increasingly dominated by idiosyncratic e"
  },
  {
    "figure_id": "F154",
    "report_id": "R008",
    "label": "Figure 1",
    "context": "Figure 1: Currency risk – the underrated opportunity under the total portfolio approach Quick win: Centralised FX can improve risk control without requiring a full portfolio reorganisation. Heatmap summarising the themes that fe"
  },
  {
    "figure_id": "F155",
    "report_id": "R010",
    "label": "Exhibit 8",
    "context": "Exhibit 1: Refined Products Margins Have Fallen Less Since the Interim Peace Deal Announcement Than Crude Prices, With Our Global Refined Product Margin Index Still Double Its Pre-War Level Exhibit 2: We Have Nudged Down Our Di"
  },
  {
    "figure_id": "F156",
    "report_id": "R010",
    "label": "Exhibit 1",
    "context": "Exhibit 4: Already Low Storage, a Stretched Refining System, and Rapidly Recovering Demand Will Likely Keep Product Stocks at Low Levels Over the Next 12 Months"
  },
  {
    "figure_id": "F157",
    "report_id": "R010",
    "label": "Exhibit 2",
    "context": "Exhibit 4: Already Low Storage, a Stretched Refining System, and Rapidly Recovering Demand Will Likely Keep Product Stocks at Low Levels Over the Next 12 Months"
  },
  {
    "figure_id": "F158",
    "report_id": "R010",
    "label": "Exhibit 2",
    "context": "Exhibit 4: Already Low Storage, a Stretched Refining System, and Rapidly Recovering Demand Will Likely Keep Product Stocks at Low Levels Over the Next 12 Months Exhibit 5: High Diesel and Jet Fuel Margins Following the Hormuz Sho"
  },
  {
    "figure_id": "F159",
    "report_id": "R010",
    "label": "Exhibit 4",
    "context": "Exhibit 6: Nearly 1.3mb/d of Persian Gulf Refining Capacity Remains Under Unplanned Maintenance/Repair More Than Two Months After the Ceasefire Announcement"
  },
  {
    "figure_id": "F160",
    "report_id": "R010",
    "label": "Exhibit 4",
    "context": "Exhibit 6: Nearly 1.3mb/d of Persian Gulf Refining Capacity Remains Under Unplanned Maintenance/Repair More Than Two Months After the Ceasefire Announcement Exhibit 7: We Expect Diesel and Gasoline Margins to Stay Slightly Above"
  },
  {
    "figure_id": "F161",
    "report_id": "R010",
    "label": "Exhibit 5",
    "context": "Exhibit 7: We Expect Diesel and Gasoline Margins to Stay Slightly Above Market Forwards in 2026H2 and Remain Above 2025 Levels Through 2027 ## Two-Sided Risks to Margins, With a Smaller Downside Than for Crude"
  },
  {
    "figure_id": "F162",
    "report_id": "R010",
    "label": "Exhibit 6",
    "context": "Exhibit 8: We See a Limited Downside to Refined Products Margins if Demand Recovery Disappoints, and a Much Larger Upside for Diesel Margins Than For Gasoline in Case of Prolonged Disruptions to Hormuz Flows"
  },
  {
    "figure_id": "F163",
    "report_id": "R010",
    "label": "Exhibit 7",
    "context": "Exhibit 9: We See a Relatively Higher Upside for Diesel Margins Than for Crude Prices in Case of a Prolong Disruption to Gulf Flows, but a Smaller Upside for Gasoline Margins Price upside scenario assumes that Hormuz flows remain"
  },
  {
    "figure_id": "F164",
    "report_id": "R010",
    "label": "Exhibit 8",
    "context": "Exhibit 10: We See a Narrower Risk Range for Refined Products Than for Brent Prices Given Near-Term Tailwinds (Ongoing Middle East and Russia Refinery Outages, Low Current Stocks, Hurricane Season in the US) and Structural Support ("
  },
  {
    "figure_id": "F165",
    "report_id": "R010",
    "label": "Exhibit 10",
    "context": "Exhibit 11: We Expect US/Europe Diesel Refined Products Margins to Average \\$38/25/bbl in 2027 and US 3-2-1 Crack Spread to Average at \\$27/bbl"
  },
  {
    "figure_id": "F166",
    "report_id": "R012",
    "label": "Exhibit 2",
    "context": "## Robust token consumption brings strong AIDC demand ## AIDC is the core infrastructure for AI compute We believe AIDC is one of the key sections in the AI compute supply chain. As the physical infrastructure of compute, AIDCs process data and connect hardwar"
  },
  {
    "figure_id": "F167",
    "report_id": "R012",
    "label": "Exhibit 4",
    "context": "## Strong compute demand to drive accelerated growth; we expect China intelligent compute to grow at a CAGR of $74\\%$ over 2025-28e, reaching 5GW in 2028e With more advanced model launches in 2026, token consumption has shown strong growth. Per National Data A"
  },
  {
    "figure_id": "F168",
    "report_id": "R012",
    "label": "Exhibit 4",
    "context": "As GAI penetration is still in the early stages, we expect the strong compute demand to persist and expect China intelligent compute (@FP16, or 16-bit binary floating-point computer number format) to grow to over 12 ZFLOPS (10^3 EFLOPS) in 2028e, close to 8x v"
  },
  {
    "figure_id": "F169",
    "report_id": "R012",
    "label": "Exhibit 5",
    "context": "Exhibit 5. IDC estimates global agent token usage will grow to 152,667 peta in 2030e Exhibit 6. China CSPs continue to raise their capex Exhibit 7. We expect China intelligent compute to grow to c12,354 EFLOPS (@FP16) in 2028e Exhibit 8. We expect China intell"
  },
  {
    "figure_id": "F170",
    "report_id": "R012",
    "label": "Exhibit 6",
    "context": "Exhibit 6. China CSPs continue to raise their capex Exhibit 7. We expect China intelligent compute to grow to c12,354 EFLOPS (@FP16) in 2028e Exhibit 8. We expect China intelligent compute data centre demand to grow at a CAGR of 74% over 2025-28e and to reach "
  },
  {
    "figure_id": "F171",
    "report_id": "R012",
    "label": "Exhibit 7",
    "context": "Exhibit 7. We expect China intelligent compute to grow to c12,354 EFLOPS (@FP16) in 2028e Exhibit 8. We expect China intelligent compute data centre demand to grow at a CAGR of 74% over 2025-28e and to reach c5.4GW in 2028e Based on 1) our above forecast for C"
  },
  {
    "figure_id": "F172",
    "report_id": "R012",
    "label": "Exhibit 8",
    "context": "Exhibit 8. We expect China intelligent compute data centre demand to grow at a CAGR of 74% over 2025-28e and to reach c5.4GW in 2028e Based on 1) our above forecast for China's intelligent compute data centre capacity and the compute scale and pricing of mains"
  },
  {
    "figure_id": "F173",
    "report_id": "R012",
    "label": "Exhibit 3",
    "context": "## Supply is the bottleneck; leaders to gain market share We expect AIDC to face supply shortages; GPUaaS should see robust growth Due to strong AI demand and given limited GPU and AIDC capacity supply, since 2025, the GPUaaS market saw continued price hikes. "
  },
  {
    "figure_id": "F174",
    "report_id": "R012",
    "label": "Exhibit 3",
    "context": "Exhibit 10. H100 1-year rental price has continued to rise since 2026 Exhibit 11. Nebius raised further its GPU rental prices in May 2026 Exhibit 12. Many CSPs have announced cloud services price hikes since 1Q26"
  },
  {
    "figure_id": "F175",
    "report_id": "R012",
    "label": "Exhibit 12",
    "context": "Exhibit 12. Many CSPs have announced cloud services price hikes since 1Q26 Exhibit 13. Overview of leading third-party IDC suppliers' in-service IT capacity and plans ## SuperPOD cluster architecture increases AIDC operators' value proposition In the era of in"
  },
  {
    "figure_id": "F176",
    "report_id": "R012",
    "label": "Exhibit 14",
    "context": "Exhibit 14. SuperPOD brings higher requirements for data centre operators Exhibit 15. Range is gaining market share in China's third-party data centre space Exhibit 16. China data centre and GPUaaS suppliers overview"
  },
  {
    "figure_id": "F177",
    "report_id": "R012",
    "label": "Exhibit 17",
    "context": "## More upside to come: global expansion ## AIDC operators: key beneficiaries of domestic LLMs going global China's leading AIDC operators have expanded into overseas markets to help support domestic CSPs' overseas compute demand. In this AI era, with more adv"
  },
  {
    "figure_id": "F178",
    "report_id": "R012",
    "label": "Exhibit 17",
    "context": "## AIDC operators: key beneficiaries of domestic LLMs going global China's leading AIDC operators have expanded into overseas markets to help support domestic CSPs' overseas compute demand. In this AI era, with more advanced domestic LLMs gaining market share "
  },
  {
    "figure_id": "F179",
    "report_id": "R012",
    "label": "Exhibit 17",
    "context": "Exhibit 17. Weekly AI token usage on OpenRouter has surged since 2026 Exhibit 18. Chinese models have gained token share from US models since February 2026 Exhibit 19. Top Chinese models perform well in the Intelligence Index at lower costs Exhibit 20. Top Chi"
  },
  {
    "figure_id": "F180",
    "report_id": "R012",
    "label": "Exhibit 18",
    "context": "Exhibit 18. Chinese models have gained token share from US models since February 2026 Exhibit 19. Top Chinese models perform well in the Intelligence Index at lower costs Exhibit 20. Top Chinese models' blended API cost is only c20% of US models' Note: Blended"
  },
  {
    "figure_id": "F181",
    "report_id": "R012",
    "label": "Exhibit 23",
    "context": "GPUaaS refers to general GPU leasing, a concept that has attracted investor attention in both China and the US due to continued price hikes. In this section, we dig into the GPUaaS market in both markets. ## CSP capex: China has significant upside ByteDance, A"
  },
  {
    "figure_id": "F182",
    "report_id": "R012",
    "label": "Exhibit 23",
    "context": "ByteDance, Alibaba and Tencent together guided for 2026e capex to be over cRMB700bn (see Ex 6) (cUSD111bn), c16% of US hyperscalers' capex, showing substantial growth potential. We believe the GPUaaS market in China is at an early stage, and rising AI penetrat"
  },
  {
    "figure_id": "F183",
    "report_id": "R012",
    "label": "Exhibit 24",
    "context": "Exhibit 24. ... and in terms of % of revenue and operating cash flow Exhibit 25. Two leading US GPUaaS suppliers' revenue were a combined USD5.7bn in 2025 Exhibit 26. ... while eight leading suppliers in China only generated RMB6,970m (cUSD976m) revenue in 202"
  },
  {
    "figure_id": "F184",
    "report_id": "R012",
    "label": "Exhibit 25",
    "context": "Exhibit 25. Two leading US GPUaaS suppliers' revenue were a combined USD5.7bn in 2025 Exhibit 26. ... while eight leading suppliers in China only generated RMB6,970m (cUSD976m) revenue in 2025 Note: We calculate Sharetronic Data (300857 CH), Glory View (301396"
  },
  {
    "figure_id": "F185",
    "report_id": "R012",
    "label": "Exhibit 26",
    "context": "Exhibit 26. ... while eight leading suppliers in China only generated RMB6,970m (cUSD976m) revenue in 2025 Note: We calculate Sharetronic Data (300857 CH), Glory View (301396 CH), Lettall Electronic (603629 CH), Hongbo (002229 CH), China Bester Group Telecom ("
  },
  {
    "figure_id": "F186",
    "report_id": "R012",
    "label": "Exhibit 27",
    "context": "Note: We calculate Sharetronic Data (300857 CH), Glory View (301396 CH), Lettall Electronic (603629 CH), Hongbo (002229 CH), China Bester Group Telecom (603220 CH), Infore Environment (000967 CH), BONC (300166 CH), and Hongxin Electronics (300657 CH). Exhibit "
  },
  {
    "figure_id": "F187",
    "report_id": "R012",
    "label": "Exhibit 29",
    "context": "## China has energy/cost advantages; US has high-end GPU supply China's “Eastern data, Western compute” policy has shifted data centre supply from eastern China to western China. Meanwhile, the “compute power coordination” policy has gradually guided data cent"
  },
  {
    "figure_id": "F188",
    "report_id": "R012",
    "label": "Exhibit 29",
    "context": "Green power price in Western China is $c50\\%$ lower than the US industrial power price. For foundation model vendors, China's data centre buildings, civil engineering and electricity costs are generally lower than in the US. China's western electricity price w"
  },
  {
    "figure_id": "F189",
    "report_id": "R012",
    "label": "Exhibit 30",
    "context": "Exhibit 30. US data centre electricity consumption accounted for $7.7\\%$ of total in 2025 Exhibit 31. Average price of electricity to industrial consumers in US has risen over the last two years and reached USD0.0862/kWh in 2025 — Average Price of Electricity "
  },
  {
    "figure_id": "F190",
    "report_id": "R012",
    "label": "Exhibit 31",
    "context": "Exhibit 31. Average price of electricity to industrial consumers in US has risen over the last two years and reached USD0.0862/kWh in 2025 — Average Price of Electricity to Ultimate Consumers, Industrial Exhibit 32. Western China's green electricity price is $"
  },
  {
    "figure_id": "F191",
    "report_id": "R012",
    "label": "Exhibit 32",
    "context": "— Average Price of Electricity to Ultimate Consumers, Industrial Exhibit 32. Western China's green electricity price is $c50\\%$ lower than the US average industrial electricity price in 2025 Exhibit 33. Location breakdown of data centre racks in China in 2024:"
  },
  {
    "figure_id": "F192",
    "report_id": "R012",
    "label": "Exhibit 33",
    "context": "Exhibit 33. Location breakdown of data centre racks in China in 2024: over $50\\%$ in eastern China Exhibit 34. Western China's green electricity price is also c50% lower than China's average industrial electricity price in 2025 Cost-effectiveness of domestic G"
  },
  {
    "figure_id": "F193",
    "report_id": "R012",
    "label": "Exhibit 34",
    "context": "Exhibit 34. Western China's green electricity price is also c50% lower than China's average industrial electricity price in 2025 Cost-effectiveness of domestic GPUs is improving; US has access to advanced GPUs GPU supply remains tight in China due to US export"
  },
  {
    "figure_id": "F194",
    "report_id": "R012",
    "label": "Exhibit 35",
    "context": "Cost-effectiveness of domestic GPUs is improving; US has access to advanced GPUs GPU supply remains tight in China due to US export controls on high-end GPUs, resulting in higher GPU server procurement costs in China versus the US. However, in the long term, w"
  },
  {
    "figure_id": "F195",
    "report_id": "R012",
    "label": "Exhibit 37",
    "context": "North American neo-cloud vendors, like Nebius and Coreweave, have relatively sufficient supply of compute and develop and build their own hypervisor layer, a software layer beyond the bare metal GPU server, designed specifically for massive AI training and inf"
  },
  {
    "figure_id": "F196",
    "report_id": "R012",
    "label": "Exhibit 37",
    "context": "China's GPU leasing leaders' core moat lies in scarce GPU supply-chain access given the US export controls. The gross margin of China's GPU leasing vendors is around $20\\% - 30\\%$ , with a net profit margin of $10\\% - 15\\%$ . The sector is now exploring new bu"
  },
  {
    "figure_id": "F197",
    "report_id": "R012",
    "label": "Exhibit 38",
    "context": "Exhibit 38. ... but their adjusted EBITDA margin could reach over $60\\%$ Exhibit 39. US neo-cloud gross margins could reach a c70% level while China GPU rental gross margins stand at 20%-30% Exhibit 40. China GPU leasing vendors' net margin could reach 10-15% "
  },
  {
    "figure_id": "F198",
    "report_id": "R012",
    "label": "Exhibit 39",
    "context": "Exhibit 39. US neo-cloud gross margins could reach a c70% level while China GPU rental gross margins stand at 20%-30% Exhibit 40. China GPU leasing vendors' net margin could reach 10-15% depending on the type of accelerators ## Related Reports Spotlight: China"
  },
  {
    "figure_id": "F199",
    "report_id": "R014",
    "label": "Exhibit 1",
    "context": "Exhibit 2: China total transformer export value growth picked up to $72\\%$ yoy in May (vs $27\\%$ in April)"
  },
  {
    "figure_id": "F200",
    "report_id": "R014",
    "label": "Exhibit 1",
    "context": "Exhibit 2: China total transformer export value growth picked up to $72\\%$ yoy in May (vs $27\\%$ in April) Exhibit 3: China transformer export value to the US grew 114x yoy on a low base, or +26% mom (vs +95% yoy in April)"
  },
  {
    "figure_id": "F201",
    "report_id": "R014",
    "label": "Exhibit 1",
    "context": "Exhibit 2: China total transformer export value growth picked up to $72\\%$ yoy in May (vs $27\\%$ in April) Exhibit 3: China transformer export value to the US grew 114x yoy on a low base, or +26% mom (vs +95% yoy in April)"
  },
  {
    "figure_id": "F202",
    "report_id": "R014",
    "label": "Exhibit 2",
    "context": "Exhibit 4: Export transformer to the US market has seen a relatively volatile ASP in 10-220MVA due to volatile mix change..."
  },
  {
    "figure_id": "F203",
    "report_id": "R014",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Export transformer to the US market has seen a relatively volatile ASP in 10-220MVA due to volatile mix change... US PPI for Electric Power and Specialty Transformer vs CPI (Jan 2018 indexed to 100) US PPI for electric"
  },
  {
    "figure_id": "F204",
    "report_id": "R014",
    "label": "Exhibit 4",
    "context": "Exhibit 5: Transformer in the 220-330MVA category saw March-May rolling average pricing -29% yoy Exhibit 7: US power and specialty transformers' PPI rose earlier than other product categories, while switchgear pricing has caught"
  },
  {
    "figure_id": "F205",
    "report_id": "R014",
    "label": "Exhibit 6",
    "context": "Exhibit 8: Key raw materials for transformer, GOES, saw prices inch down Price index for transformer key materials (Jan 2018 indexed to 100)"
  },
  {
    "figure_id": "F206",
    "report_id": "R014",
    "label": "Exhibit 5",
    "context": "Exhibit 8: Key raw materials for transformer, GOES, saw prices inch down Price index for transformer key materials (Jan 2018 indexed to 100)"
  },
  {
    "figure_id": "F207",
    "report_id": "R014",
    "label": "Exhibit 7",
    "context": "Exhibit 7: US power and specialty transformers' PPI rose earlier than other product categories, while switchgear pricing has caught up in recent months (+12% yoy in May) Exhibit 8: Key raw materials for transformer, GOES, saw pri"
  },
  {
    "figure_id": "F208",
    "report_id": "R014",
    "label": "Exhibit 9",
    "context": "Exhibit 9: China total transformer export value picked up to $72\\%$ yoy in May (vs $27\\%$ in April) Exhibit 10: China transformer export value to the US grew 114x yoy on a low base, or $26\\%$ mom (vs $+95\\%$ yoy in April) Exhib"
  },
  {
    "figure_id": "F209",
    "report_id": "R014",
    "label": "Exhibit 9",
    "context": "Exhibit 9: China total transformer export value picked up to $72\\%$ yoy in May (vs $27\\%$ in April) Exhibit 10: China transformer export value to the US grew 114x yoy on a low base, or $26\\%$ mom (vs $+95\\%$ yoy in April) Exhib"
  },
  {
    "figure_id": "F210",
    "report_id": "R014",
    "label": "Exhibit 10",
    "context": "Exhibit 10: China transformer export value to the US grew 114x yoy on a low base, or $26\\%$ mom (vs $+95\\%$ yoy in April) Exhibit 11: China electronic meter export value was -11% yoy in May (vs flat in April) The author would"
  },
  {
    "figure_id": "F211",
    "report_id": "R014",
    "label": "Exhibit 11",
    "context": "Exhibit 11: China electronic meter export value was -11% yoy in May (vs flat in April) The author would like to thank Zhou Li, Hao Chen, Zhihan Ye, and Junfang Zhang for their contributions to this report. ## Disclosure Appendix"
  },
  {
    "figure_id": "F212",
    "report_id": "R015",
    "label": "Figure 1",
    "context": "Figure 1: Iceberg 10-city real time secondary daily sales 冰山指数实时二手每日成交 (十大城市) Note: The Y/Y decline in the week ending 21 June 2026 is due to the Dragon Boat Festival."
  },
  {
    "figure_id": "F213",
    "report_id": "R015",
    "label": "Figure 2",
    "context": "Figure 2: Iceberg tier-1 cities secondary listing volume 冰山指数二手挂牌量 (一线城市) ## 2. Mainland China – leading indicators from Centraline Figure 3: Centraline secondary asking price index vs. NBS secondary home price index M/M in tier"
  },
  {
    "figure_id": "F214",
    "report_id": "R015",
    "label": "Figure 2",
    "context": "Figure 4: Centraline secondary manager confidence index in tier-1 cities vs. three-month rolling secondary sales # 3. Mainland China – Weekly primary sales registrations"
  },
  {
    "figure_id": "F215",
    "report_id": "R015",
    "label": "Figure 3",
    "context": "Figure 4: Centraline secondary manager confidence index in tier-1 cities vs. three-month rolling secondary sales # 3. Mainland China – Weekly primary sales registrations Figure 5: 60-city weekly primary sales registrations (一手网签"
  },
  {
    "figure_id": "F216",
    "report_id": "R015",
    "label": "Figure 4",
    "context": "Figure 6: 60-city weekly primary sales registrations (一手网签) Note: The Y/Y decline in the week ending 21 June 2026 is due to the Dragon Boat Festival."
  },
  {
    "figure_id": "F217",
    "report_id": "R015",
    "label": "Figure 5",
    "context": "Figure 5: 60-city weekly primary sales registrations (一手网签) – compared with 2019-24 Note: The Y/Y decline in the week ending 21 June 2026 is due to the Dragon Boat Festival. Figure 6: 60-city weekly primary sales registrations ("
  },
  {
    "figure_id": "F218",
    "report_id": "R015",
    "label": "Figure 7",
    "context": "Figure 7: 12-city daily secondary sales registrations (二手网签) Note: The decline in the week ending 21 June 2026 is due to the Dragon Boat Festival. Figure 8: 12-city secondary sales registrations (二手网签) 7-day moving average Secon"
  },
  {
    "figure_id": "F219",
    "report_id": "R015",
    "label": "Figure 7",
    "context": "Figure 7: 12-city daily secondary sales registrations (二手网签) Note: The decline in the week ending 21 June 2026 is due to the Dragon Boat Festival. Figure 8: 12-city secondary sales registrations (二手网签) 7-day moving average Secon"
  },
  {
    "figure_id": "F220",
    "report_id": "R015",
    "label": "Figure 9",
    "context": "Figure 9: Midland weekend appointment volume (in 15 housing estates) Figure 10: Centraline – No. of secondary listings (for sale) Figure 11: Hong Kong weekly secondary transactions in 35 major estates"
  },
  {
    "figure_id": "F221",
    "report_id": "R015",
    "label": "Figure 9",
    "context": "Figure 9: Midland weekend appointment volume (in 15 housing estates) Figure 10: Centraline – No. of secondary listings (for sale) Figure 11: Hong Kong weekly secondary transactions in 35 major estates Figure 12: Hong Kong se"
  },
  {
    "figure_id": "F222",
    "report_id": "R015",
    "label": "Figure 10",
    "context": "Figure 10: Centraline – No. of secondary listings (for sale) Figure 11: Hong Kong weekly secondary transactions in 35 major estates Figure 12: Hong Kong secondary home prices (Centa-city Leading Index, or CCL) Figure 13: Cent"
  },
  {
    "figure_id": "F223",
    "report_id": "R015",
    "label": "Figure 11",
    "context": "Figure 11: Hong Kong weekly secondary transactions in 35 major estates Figure 12: Hong Kong secondary home prices (Centa-city Leading Index, or CCL) Figure 13: Centa Valuation Index (CVI) vs. secondary home prices (CCL) 1m roll"
  },
  {
    "figure_id": "F224",
    "report_id": "R015",
    "label": "Figure 12",
    "context": "Figure 12: Hong Kong secondary home prices (Centa-city Leading Index, or CCL) Figure 13: Centa Valuation Index (CVI) vs. secondary home prices (CCL) 1m rolling W/W"
  },
  {
    "figure_id": "F225",
    "report_id": "R015",
    "label": "Figure 14",
    "context": "Figure 14: Centa-Salesman Index (CSI) vs. secondary home prices (CCL) Figure 15: Centa-City Rental Index (CRI) # 6. Hong Kong – Tourist arrivals and resident departures"
  },
  {
    "figure_id": "F226",
    "report_id": "R015",
    "label": "Figure 14",
    "context": "Figure 14: Centa-Salesman Index (CSI) vs. secondary home prices (CCL) Figure 15: Centa-City Rental Index (CRI) # 6. Hong Kong – Tourist arrivals and resident departures"
  },
  {
    "figure_id": "F227",
    "report_id": "R015",
    "label": "Figure 16",
    "context": "Figure 16: Hong Kong seven-day rolling average total tourist arrivals minus resident departures ## 7. Share price update Figure 17: Mainland China Property – Weekly share price performance (%)"
  },
  {
    "figure_id": "F228",
    "report_id": "R015",
    "label": "Figure 16",
    "context": "Figure 19: Mainland China / Hong Kong Property & Conglomerates – Weekly share price performance by company type"
  },
  {
    "figure_id": "F229",
    "report_id": "R015",
    "label": "Figure 17",
    "context": "Figure 20: Short interest in Mainland China / Hong Kong Property – 30-day moving average"
  },
  {
    "figure_id": "F230",
    "report_id": "R015",
    "label": "Figure 18",
    "context": "Figure 18: Hong Kong Property & Conglomerates – Weekly share price performance (%) Figure 19: Mainland China / Hong Kong Property & Conglomerates – Weekly share price performance by company type Figure 20: Short interest in Mai"
  },
  {
    "figure_id": "F231",
    "report_id": "R015",
    "label": "Figure 19",
    "context": "Figure 19: Mainland China / Hong Kong Property & Conglomerates – Weekly share price performance by company type Figure 20: Short interest in Mainland China / Hong Kong Property – 30-day moving average Southbound holding as % of"
  },
  {
    "figure_id": "F232",
    "report_id": "R015",
    "label": "Figure 21",
    "context": "Figure 21: HK property average southbound holdings as % of free float ## 8. Credit recommendations"
  },
  {
    "figure_id": "F233",
    "report_id": "R015",
    "label": "Figure 22",
    "context": "Figure 22: JACI China HY Property Index: Performance since 2026 (January 2026 = 100)"
  },
  {
    "figure_id": "F234",
    "report_id": "R016",
    "label": "Figure 1",
    "context": "Figure 1: CSP capex and AI memory % share Figure 2: Relevant TAM % of CSP capex Figure 3: Memory vs CSP market cap trend"
  },
  {
    "figure_id": "F235",
    "report_id": "R016",
    "label": "Figure 1",
    "context": "Figure 1: CSP capex and AI memory % share Figure 2: Relevant TAM % of CSP capex Figure 3: Memory vs CSP market cap trend Figure 4: Absolute memory TAM % of CSP capex"
  },
  {
    "figure_id": "F236",
    "report_id": "R016",
    "label": "Figure 2",
    "context": "Figure 2: Relevant TAM % of CSP capex Figure 3: Memory vs CSP market cap trend Figure 4: Absolute memory TAM % of CSP capex"
  },
  {
    "figure_id": "F237",
    "report_id": "R016",
    "label": "Figure 3",
    "context": "Figure 3: Memory vs CSP market cap trend Figure 4: Absolute memory TAM % of CSP capex \\- HBM commands structurally higher demand growth over the rest of the market, pricing upside an option value. The HBM S-D imbalance and the"
  },
  {
    "figure_id": "F238",
    "report_id": "R016",
    "label": "Figure 7",
    "context": "Figure 7: Average memory share price performance around MU earnings date %"
  },
  {
    "figure_id": "F239",
    "report_id": "R016",
    "label": "Figure 7",
    "context": "Figure 7: Average memory share price performance around MU earnings date %"
  },
  {
    "figure_id": "F240",
    "report_id": "R016",
    "label": "Figure 7",
    "context": "Figure 7: Average memory share price performance around MU earnings date %"
  },
  {
    "figure_id": "F241",
    "report_id": "R016",
    "label": "Figure 8",
    "context": "Figure 8: Global memory makers' share price performance including SOX (Philadelphia Semiconductor index) % US\\$bn, % % chagnes"
  },
  {
    "figure_id": "F242",
    "report_id": "R017",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Global CoWoS demand breakdown: 2026e vs. 2027e Global CoWoS capacity demand by key customer Exhibit 2: Global CoWoS demand Y/Y growth profile"
  },
  {
    "figure_id": "F243",
    "report_id": "R017",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Global CoWoS demand breakdown with newly introduced 2027e numbers Exhibit 4: Global CoWoS capacity expansion by year end and by vendor Exhibit 5: Global CoWoS consumption, by customer NVIDIA Broadcom AMD Xilinx AWS/A"
  },
  {
    "figure_id": "F244",
    "report_id": "R017",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Global CoWoS capacity expansion by year end and by vendor Exhibit 5: Global CoWoS consumption, by customer NVIDIA Broadcom AMD Xilinx AWS/Annapurna AWS/Alchip Marvell GUC MediaTek Intel Habana Others ## Exhibit 6: AI"
  },
  {
    "figure_id": "F245",
    "report_id": "R017",
    "label": "Exhibit 10",
    "context": "Exhibit 10: P/E multiple trend of AI semis Exhibit 11: We still expect AI chip revenue to rise QoQ Data center/HPC semi revenue: NVIDIA + AMD Exhibit 12: TSMC's AI-related revenue 2024-29e CAGR could reach 60%"
  },
  {
    "figure_id": "F246",
    "report_id": "R017",
    "label": "Exhibit 10",
    "context": "Exhibit 10: P/E multiple trend of AI semis Exhibit 11: We still expect AI chip revenue to rise QoQ Data center/HPC semi revenue: NVIDIA + AMD Exhibit 12: TSMC's AI-related revenue 2024-29e CAGR could reach 60% ■ General-purpos"
  },
  {
    "figure_id": "F247",
    "report_id": "R017",
    "label": "Exhibit 11",
    "context": "Exhibit 13: AI GPU H100 per GPU per hour as of end-March"
  },
  {
    "figure_id": "F248",
    "report_id": "R017",
    "label": "Exhibit 12",
    "context": "Exhibit 14: AI ASIC equivalent computing power – 16x Inferentia 2 per hour Exhibit 15: NVIDIA 5090 graphic cards pricing has rebounded recently, mainly in response to market expectations for price hikes and strong AI inference dem"
  },
  {
    "figure_id": "F249",
    "report_id": "R017",
    "label": "Exhibit 13",
    "context": "Exhibit 13: AI GPU H100 per GPU per hour as of end-March Exhibit 14: AI ASIC equivalent computing power – 16x Inferentia 2 per hour Exhibit 15: NVIDIA 5090 graphic cards pricing has rebounded recently, mainly in response to mark"
  },
  {
    "figure_id": "F250",
    "report_id": "R017",
    "label": "Exhibit 14",
    "context": "Exhibit 14: AI ASIC equivalent computing power – 16x Inferentia 2 per hour Exhibit 15: NVIDIA 5090 graphic cards pricing has rebounded recently, mainly in response to market expectations for price hikes and strong AI inference dem"
  },
  {
    "figure_id": "F251",
    "report_id": "R020",
    "label": "Exhibit 3",
    "context": "Exhibit 5: Monthly domestic order intake and order backlog (gross tonnage)"
  },
  {
    "figure_id": "F252",
    "report_id": "R020",
    "label": "Exhibit 3",
    "context": "Exhibit 5: Monthly domestic order intake and order backlog (gross tonnage) Note: We use combined figures for major member companies of the Japan Ship Exporters' Association"
  },
  {
    "figure_id": "F253",
    "report_id": "R020",
    "label": "Exhibit 4",
    "context": "Exhibit 6: Global order backlog for alternative fuel capable ships (number of vessels) and their share of total order backlog Exhibit 7: Quarterly orders at Japanese shipbuilders and related companies"
  },
  {
    "figure_id": "F254",
    "report_id": "R020",
    "label": "Exhibit 5",
    "context": "Exhibit 7: Quarterly orders at Japanese shipbuilders and related companies Namura Shipbuilding data is calculated from the QoQ difference in the order backlog of the new shipbuilding business (while also adding back sales from th"
  },
  {
    "figure_id": "F255",
    "report_id": "R020",
    "label": "Exhibit 6",
    "context": "Exhibit 8: Quarterly operating profits for Japanese shipbuilding-related companies Furuno Electric's FY-end is February"
  },
  {
    "figure_id": "F256",
    "report_id": "R020",
    "label": "Exhibit 7",
    "context": "Exhibit 8: Quarterly operating profits for Japanese shipbuilding-related companies Furuno Electric's FY-end is February Exhibit 9: Road map for revitalization of Japan's shipbuilding industry"
  },
  {
    "figure_id": "F257",
    "report_id": "R020",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Quarterly operating profits for Japanese shipbuilding-related companies Furuno Electric's FY-end is February Exhibit 9: Road map for revitalization of Japan's shipbuilding industry"
  },
  {
    "figure_id": "F258",
    "report_id": "R023",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Non-commodity sector profit margins have stabilized but remain relatively weak... Exhibit 2: ...leading to subdued trends in wage growth Exhibit 3: As the effects of the consumption trade-in program have faded, this"
  },
  {
    "figure_id": "F259",
    "report_id": "R023",
    "label": "Exhibit 1",
    "context": "Exhibit 4: Hotel RevPAR indicates soft demand – June is tracking only 2% YoY despite a very low base in 2025"
  },
  {
    "figure_id": "F260",
    "report_id": "R023",
    "label": "Exhibit 2",
    "context": "Exhibit 2: ...leading to subdued trends in wage growth Exhibit 3: As the effects of the consumption trade-in program have faded, this has resulted in an outright contraction in headline retail sales Exhibit 4: Hotel RevPAR indi"
  },
  {
    "figure_id": "F261",
    "report_id": "R023",
    "label": "Exhibit 3",
    "context": "Exhibit 5: Policymakers are following the countercyclical growth model of pulling back policy stimulus when external demand is strong"
  },
  {
    "figure_id": "F262",
    "report_id": "R023",
    "label": "Exhibit 4",
    "context": "Exhibit 5: Policymakers are following the countercyclical growth model of pulling back policy stimulus when external demand is strong Exhibit 6: Augmented deficit has narrowed from 11.9% of GDP in Jan-26 to 10.9% of GDP in May"
  },
  {
    "figure_id": "F263",
    "report_id": "R023",
    "label": "Exhibit 5",
    "context": "Exhibit 7: Domestic gasoline prices have also risen by a peak of 26%, and have remained 18% higher than end-February levels"
  },
  {
    "figure_id": "F264",
    "report_id": "R023",
    "label": "Exhibit 6",
    "context": "Exhibit 7: Domestic gasoline prices have also risen by a peak of 26%, and have remained 18% higher than end-February levels Exhibit 8: Fuel CPI accelerated sharply but has likely peaked in ## Structural factors holding back ref"
  },
  {
    "figure_id": "F265",
    "report_id": "R023",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Domestic gasoline prices have also risen by a peak of 26%, and have remained 18% higher than end-February levels Exhibit 8: Fuel CPI accelerated sharply but has likely peaked in ## Structural factors holding back ref"
  },
  {
    "figure_id": "F266",
    "report_id": "R023",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Weakening demographic trend exerting pressure on growth Exhibit 10: Extensive adjustment means property sector should exert less of a drag on the broader economy going forward, but will also not be a significant growth"
  },
  {
    "figure_id": "F267",
    "report_id": "R023",
    "label": "Exhibit 9",
    "context": "Exhibit 11: Household savings rate remains elevated and has been rising"
  },
  {
    "figure_id": "F268",
    "report_id": "R023",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Household savings rate remains elevated and has been rising China 1Q surveyed household saving rate 35.0% (4Q trailing sum % of disposable income) # What would we be watching to track China reflation? Policy measures t"
  },
  {
    "figure_id": "F269",
    "report_id": "R023",
    "label": "Exhibit 12",
    "context": "Exhibit 12: China's non-tech exports showed broad-based improvement across passenger cars, intermediate goods and capital goods Exhibit 13: Sustained strong exports will lift capacity utilization ## Disclosure Section"
  },
  {
    "figure_id": "F270",
    "report_id": "R023",
    "label": "Exhibit 12",
    "context": "Exhibit 12: China's non-tech exports showed broad-based improvement across passenger cars, intermediate goods and capital goods Exhibit 13: Sustained strong exports will lift capacity utilization ## Disclosure Section"
  },
  {
    "figure_id": "F271",
    "report_id": "R025",
    "label": "Figure 2",
    "context": "Figure 2: Weekly new orders trend of key automakers (Li, NIO, XPeng, Leap, Xiaomi, Tesla) Figure 3: Weekly BYD, Geely, HIMA (mainly AITO) new orders trend Figure 4: Weekly HIMA (mainly AITO) new orders trend"
  },
  {
    "figure_id": "F272",
    "report_id": "R025",
    "label": "Figure 2",
    "context": "Figure 2: Weekly new orders trend of key automakers (Li, NIO, XPeng, Leap, Xiaomi, Tesla) Figure 3: Weekly BYD, Geely, HIMA (mainly AITO) new orders trend Figure 4: Weekly HIMA (mainly AITO) new orders trend Figure 5: Weekly"
  },
  {
    "figure_id": "F273",
    "report_id": "R025",
    "label": "Figure 3",
    "context": "Figure 3: Weekly BYD, Geely, HIMA (mainly AITO) new orders trend Figure 4: Weekly HIMA (mainly AITO) new orders trend Figure 5: Weekly Li Auto new orders trend Figure 6: Weekly NIO group new orders trend"
  },
  {
    "figure_id": "F274",
    "report_id": "R025",
    "label": "Figure 4",
    "context": "Figure 4: Weekly HIMA (mainly AITO) new orders trend Figure 5: Weekly Li Auto new orders trend Figure 6: Weekly NIO group new orders trend Figure 7: Weekly Tesla new orders trend"
  },
  {
    "figure_id": "F275",
    "report_id": "R025",
    "label": "Figure 5",
    "context": "Figure 5: Weekly Li Auto new orders trend Figure 6: Weekly NIO group new orders trend Figure 7: Weekly Tesla new orders trend Figure 8: Weekly Xiaomi new orders trend"
  },
  {
    "figure_id": "F276",
    "report_id": "R025",
    "label": "Figure 6",
    "context": "Figure 6: Weekly NIO group new orders trend Figure 7: Weekly Tesla new orders trend Figure 8: Weekly Xiaomi new orders trend Figure 9: Weekly XPeng new orders trend"
  },
  {
    "figure_id": "F277",
    "report_id": "R025",
    "label": "Figure 7",
    "context": "Figure 7: Weekly Tesla new orders trend Figure 8: Weekly Xiaomi new orders trend Figure 9: Weekly XPeng new orders trend ## Appendix 1"
  },
  {
    "figure_id": "F278",
    "report_id": "R025",
    "label": "Figure 8",
    "context": "Figure 8: Weekly Xiaomi new orders trend Figure 9: Weekly XPeng new orders trend ## Appendix 1 ## Important Disclosures For disclosures pertaining to recommendations or estimates made on securities other than the primary subje"
  },
  {
    "figure_id": "F279",
    "report_id": "R026",
    "label": "Exhibit 1",
    "context": "Exhibit 1: China Five-factor Consumer Activity Z-Score vs. MSCI China YoY change – Consumer activity declined further in May MS ASIA LIMITED+ Laura Wang Equity Strategist"
  },
  {
    "figure_id": "F280",
    "report_id": "R027",
    "label": "Figure 2",
    "context": "Figure 2: Limited improvement in lux imports YoY China monthly luxury import YoY Note: Mechanical watch import data as per NBS, Marh FHS data to be released on the 21st of April Figure 3: 1Q YoY improvement momentum did not carr"
  },
  {
    "figure_id": "F281",
    "report_id": "R027",
    "label": "Figure 3",
    "context": "Figure 3: 1Q YoY improvement momentum did not carry into 2Q China quarterly luxury import (volume, YoY)"
  },
  {
    "figure_id": "F282",
    "report_id": "R027",
    "label": "Figure 4",
    "context": "Figure 5: May volume import -11.1% in May, -6.3% in 3MA terms"
  },
  {
    "figure_id": "F283",
    "report_id": "R027",
    "label": "Figure 5",
    "context": "Figure 5: May volume import -11.1% in May, -6.3% in 3MA terms"
  },
  {
    "figure_id": "F284",
    "report_id": "R027",
    "label": "Figure 5",
    "context": "Figure 7: Italian handbag imports are down sequentially - 9.0% in units in Q2 vs. +6.3% in Q1"
  },
  {
    "figure_id": "F285",
    "report_id": "R027",
    "label": "Figure 6",
    "context": "Figure 8: French leather handbag imports are down -1.2% in units Q2 vs. +5.9% in Q1 Leather handbag unit import from FRA vs. RMS Asia cFX"
  },
  {
    "figure_id": "F286",
    "report_id": "R027",
    "label": "Figure 8",
    "context": "Figure 9: Jewellery import is down -7% in May vs. -10% in April; it is down -15% in 3MA terms"
  },
  {
    "figure_id": "F287",
    "report_id": "R027",
    "label": "Figure 9",
    "context": "Figure 9: Jewellery import is down -7% in May vs. -10% in April; it is down -15% in 3MA terms Monthly jewellery import volume from FRA ITA CHE vs. relevant sector cFX"
  },
  {
    "figure_id": "F288",
    "report_id": "R027",
    "label": "Figure 9",
    "context": "Figure 11: Swiss watch export to Asia +3% in May vs. -7% in April Monthly Swiss watch export to Asia (units) vs. relevant sector cFX"
  },
  {
    "figure_id": "F289",
    "report_id": "R027",
    "label": "Figure 11",
    "context": "Figure 11: Swiss watch export to Asia +3% in May vs. -7% in April Monthly Swiss watch export to Asia (units) vs. relevant sector cFX"
  },
  {
    "figure_id": "F290",
    "report_id": "R027",
    "label": "Figure 11",
    "context": "Figure 13: Wealth improvement driven by stock market returns is slowing and may contribute to a slower recovery in luxury spend in China"
  },
  {
    "figure_id": "F291",
    "report_id": "R027",
    "label": "Figure 13",
    "context": "Figure 14: Consumer confidence declined in April vs. the months of March and February China consumer confidence (1997=100)"
  },
  {
    "figure_id": "F292",
    "report_id": "R027",
    "label": "Figure 14",
    "context": "Figure 14: Consumer confidence declined in April vs. the months of March and February China consumer confidence (1997=100)"
  },
  {
    "figure_id": "F293",
    "report_id": "R027",
    "label": "Figure 14",
    "context": "Figure 15: Home prices were down -4.8% in May vs. -4.9% in April"
  },
  {
    "figure_id": "F294",
    "report_id": "R027",
    "label": "Figure 16",
    "context": "Figure 15: Home prices were down -4.8% in May vs. -4.9% in April"
  },
  {
    "figure_id": "F295",
    "report_id": "R027",
    "label": "Figure 15",
    "context": "Figure 18: Weaker apparel and footwear sales growth in 2Q China apparel and footwear sales (Monthly, February data are January and February combined)"
  },
  {
    "figure_id": "F296",
    "report_id": "R027",
    "label": "Figure 18",
    "context": "Figure 18: Weaker apparel and footwear sales growth in 2Q China apparel and footwear sales (Monthly, February data are January and February combined)"
  },
  {
    "figure_id": "F297",
    "report_id": "R027",
    "label": "Figure 19",
    "context": "Figure 20: Discretionary spending environment looks unfavourable for luxury recovery... China apparel and footwear spend vs. luxury import (Monthly)"
  },
  {
    "figure_id": "F298",
    "report_id": "R027",
    "label": "Figure 20",
    "context": "Figure 20: Discretionary spending environment looks unfavourable for luxury recovery... China apparel and footwear spend vs. luxury import (Monthly)"
  },
  {
    "figure_id": "F299",
    "report_id": "R027",
    "label": "Figure 21",
    "context": "Figure 21: ...which may put pressure on luxury cFX recovery in the region China apparel and footwear spend vs. luxury import (Monthly)"
  },
  {
    "figure_id": "F300",
    "report_id": "R028",
    "label": "Exhibit 3",
    "context": "Exhibit 3: The mom & baby channel declined by 7% yoy and modern trade declined by 20% yoy Exhibit 4: For modern trade and mom & baby stores, infant formula sales recorded a 9% volume decline with 0.9% ASP growth yoy ## Offline"
  },
  {
    "figure_id": "F301",
    "report_id": "R028",
    "label": "Exhibit 3",
    "context": "Exhibit 3: The mom & baby channel declined by 7% yoy and modern trade declined by 20% yoy Exhibit 4: For modern trade and mom & baby stores, infant formula sales recorded a 9% volume decline with 0.9% ASP growth yoy ## Offline"
  },
  {
    "figure_id": "F302",
    "report_id": "R028",
    "label": "Exhibit 5",
    "context": "Exhibit 7: Feihe's/Yili's market share increased in Mar-Apr in the offline market, while Mengniu's market share decreased Nielsen market share for leading brands"
  },
  {
    "figure_id": "F303",
    "report_id": "R028",
    "label": "Exhibit 5",
    "context": "Exhibit 8: Big local brands collectively took 62% market share, flattish vs. Jan-Feb, while MNCs saw market share gain of 0.3pp vs Jan-Feb Market share, % of total infant formula offline channel Market share, % of total infant form"
  },
  {
    "figure_id": "F304",
    "report_id": "R028",
    "label": "Exhibit 6",
    "context": "Exhibit 6: MNC players saw sequential market share trend mixed in Mar-Apr, Friesland/Danone/A2 value share increased while Wyeth decreased vs. Jan-Feb Offline international IMF brands market share by value Exhibit 8: Big local br"
  },
  {
    "figure_id": "F305",
    "report_id": "R028",
    "label": "Exhibit 6",
    "context": "Exhibit 6: MNC players saw sequential market share trend mixed in Mar-Apr, Friesland/Danone/A2 value share increased while Wyeth decreased vs. Jan-Feb Offline international IMF brands market share by value Exhibit 8: Big local br"
  },
  {
    "figure_id": "F306",
    "report_id": "R028",
    "label": "Exhibit 9",
    "context": "Exhibit 11: Tmall/Taobao IMF sales decreased by -2% in May vs 14% yoy in Apr mainly on volume growth Tmall/Taobao IMF monthly growth"
  },
  {
    "figure_id": "F307",
    "report_id": "R028",
    "label": "Exhibit 9",
    "context": "Exhibit 11: Tmall/Taobao IMF sales decreased by -2% in May vs 14% yoy in Apr mainly on volume growth Tmall/Taobao IMF monthly growth Exhibit 12: JD IMF sales declined at $-19\\% / -14\\%$ yoy in May/Apr JD IMF monthly growth"
  },
  {
    "figure_id": "F308",
    "report_id": "R028",
    "label": "Exhibit 10",
    "context": "Exhibit 12: JD IMF sales declined at $-19\\% / -14\\%$ yoy in May/Apr JD IMF monthly growth JD IMF Exhibit 13: Aptamil maintained its No.1 position with market share loss 0.9ppt mom to $20\\%$ ; A2 lost 2.7ppt market share in May Int"
  },
  {
    "figure_id": "F309",
    "report_id": "R028",
    "label": "Exhibit 11",
    "context": "Exhibit 13: Aptamil maintained its No.1 position with market share loss 0.9ppt mom to $20\\%$ ; A2 lost 2.7ppt market share in May International IMF value Market share (Tmall+Taobao) Exhibit 14: Feihe/Yili's Market share on Tmall/T"
  },
  {
    "figure_id": "F310",
    "report_id": "R028",
    "label": "Exhibit 12",
    "context": "Exhibit 14: Feihe/Yili's Market share on Tmall/Taobao was $14\\% /9\\%$ in May Domestic IMF value Market share (Tmall+Taobao)"
  },
  {
    "figure_id": "F311",
    "report_id": "R028",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Aptamil maintained its No.1 position with market share loss 0.9ppt mom to $20\\%$ ; A2 lost 2.7ppt market share in May International IMF value Market share (Tmall+Taobao) Exhibit 14: Feihe/Yili's Market share on Tmall/T"
  },
  {
    "figure_id": "F312",
    "report_id": "R028",
    "label": "Exhibit 16",
    "context": "Exhibit 17: GS tracking online channel sales decline at -31% yoy in May, vs. -47% in Apr Feihe: GS IMF tracker online sales yoy (Tmall/Taobao/JD)"
  },
  {
    "figure_id": "F313",
    "report_id": "R028",
    "label": "Exhibit 16",
    "context": "Exhibit 17: GS tracking online channel sales decline at -31% yoy in May, vs. -47% in Apr Feihe: GS IMF tracker online sales yoy (Tmall/Taobao/JD) Exhibit 18: Feihe Tmall/Taobao IMF sales increased by grew at $1\\%$ in May vs. $+26\\"
  },
  {
    "figure_id": "F314",
    "report_id": "R028",
    "label": "Exhibit 17",
    "context": "Exhibit 19: Feihe JD IMF sales decreased by $40\\%$ yoy in May following the $-60\\%$ yoy decline in Apr, mainly on weak volume since Jun 25 JD IMF monthly growth"
  },
  {
    "figure_id": "F315",
    "report_id": "R028",
    "label": "Exhibit 17",
    "context": "Exhibit 19: Feihe JD IMF sales decreased by $40\\%$ yoy in May following the $-60\\%$ yoy decline in Apr, mainly on weak volume since Jun 25 JD IMF monthly growth Firmus (JD)"
  },
  {
    "figure_id": "F316",
    "report_id": "R028",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Feihe JD IMF sales decreased by $40\\%$ yoy in May following the $-60\\%$ yoy decline in Apr, mainly on weak volume since Jun 25 JD IMF monthly growth Firmus (JD) ## Valuation and key risks ## Feihe (Neutral): Valuation"
  },
  {
    "figure_id": "F317",
    "report_id": "R028",
    "label": "Exhibit 20",
    "context": "Exhibit 20: GS tracking online channel sales point up to -17% in May vs -10% in Apr Exhibit 21: Yili omnichannel had flattish yoy trend for 2H25 vs 9% yoy sales growth by GSe Exhibit 23: Yili JD IMF sales declined by $-25\\%$ in"
  },
  {
    "figure_id": "F318",
    "report_id": "R028",
    "label": "Exhibit 20",
    "context": "Exhibit 22: Yili (including Pro-Kido) grew at +3% yoy in May vs. +33% in Apr Tmall/Taobao IMF monthly growth"
  },
  {
    "figure_id": "F319",
    "report_id": "R028",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Yili JD IMF sales declined by $-25\\%$ in May vs $-25\\%$ yoy in Apr, mainly on volume weakness JD IMF monthly growth Exhibit 22: Yili (including Pro-Kido) grew at +3% yoy in May vs. +33% in Apr Tmall/Taobao IMF monthly gr"
  },
  {
    "figure_id": "F320",
    "report_id": "R028",
    "label": "Exhibit 22",
    "context": "Exhibit 22: Yili (including Pro-Kido) grew at +3% yoy in May vs. +33% in Apr Tmall/Taobao IMF monthly growth Valuation and key risks Yili (Buy): Our 12-month Rmb35 TP is based on 2026E P/E of 18.9x (20% A/H premium to the target"
  },
  {
    "figure_id": "F321",
    "report_id": "R028",
    "label": "Exhibit 24",
    "context": "Exhibit 24: Junlebao's sales declined by $22.3\\%$ yoy, and Ausnutria sales declined by $28\\%$ yoy, both underperforming the market Offline sales growth Sales growth yoy (MT & MB channel combined) Exhibit 25: Yili sales grew by $1."
  },
  {
    "figure_id": "F322",
    "report_id": "R028",
    "label": "Exhibit 25",
    "context": "Exhibit 26: A2's sales declined by $25\\%$ yoy in May, vs $+27\\%$ yoy in Apr potentially due to supply cut Online sales growth"
  },
  {
    "figure_id": "F323",
    "report_id": "R028",
    "label": "Exhibit 26",
    "context": "Exhibit 26: A2's sales declined by $25\\%$ yoy in May, vs $+27\\%$ yoy in Apr potentially due to supply cut Online sales growth ## Disclosure Appendix ## Reg AC We, Leaf Liu, Peter Marks, Christina Liu, Rayanne Haidar and Valerie Zh"
  }
]